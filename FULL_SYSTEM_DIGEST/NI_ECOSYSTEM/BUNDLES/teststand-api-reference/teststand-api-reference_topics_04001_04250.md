# NI DOCUMENT BUNDLE: teststand-api-reference

<!--NI_BUNDLE_CHUNK bundle=teststand-api-reference start=4001 end=4250 -->
<!--NI_TOPIC bundle=teststand-api-reference path=tsref/profiles-pane-context-menu.html language=enus -->
## TOPIC 04001: Profiles Pane Context Menu

- bundle_id: `teststand-api-reference`
- source_path: `tsref/profiles-pane-context-menu.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/profiles-pane-context-menu.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: The Profiles pane context menu can contain the following items: Process Files Using < Profile Name > —Uses the profile you select to process the selected files. Clear Inbox of Profile —Deletes all files in the inbox. Clear Outbox of Profile —Deletes all files in the outbox. Retry Processing Selected

### Profiles Pane Context Menu

The Profiles pane context menu can contain the following items:

- Process Files Using <
 Profile Name
 > 
 —Uses the profile you select to process the selected files.
- Clear Inbox of Profile 
 —Deletes all files in the inbox.
- Clear Outbox of Profile 
 —Deletes all files in the outbox.
- Retry Processing Selected Files Using <
 Profile Name
 > 
 —Uses the profile you select to reprocess selected files if processing errors exist.
- Process Selected Files Immediately Using <
 Profile Name
 > 
 —Uses the profile you select to immediately process the selected files before processing any other queued files. The utility opens two slots more than the number of threads you specify in the
 TestStand Offline Results Processing Utility Settings 
 dialog box to handle this request.
- Process Selected Files Again Using <
 Profile Name
 > 
 —Moves the selected files to the inbox and reprocesses them using the profile you select.
- Force Move File to Outbox of <
 Profile Name
 > 
 —Immediately moves the selected file to the outbox of the profile you select. If a name collision exists, the utility renames the file you select and the corresponding report files with unique names.
- Delete Selected Files 
 —Deletes the files you select.
- New Profile 
 —Creates a new profile.
- Delete Profile 
 —Deletes the profile you select.
- Open Containing Folder in Explorer 
 —Opens Microsoft Windows Explorer in the directory that contains the file you selected.
- Copy Paths of Selected Files 
 —Copies to the clipboard the paths of the file you selected.

#### See Also

[TestStand Offline Results Processing Utility Settings dialog box](teststand-offline-results-processing-utility.html)

Parent topic:

TestStand Offline Results Processing Utility Menus

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/profiles-pane.html language=enus -->
## TOPIC 04002: Profiles Pane

- bundle_id: `teststand-api-reference`
- source_path: `tsref/profiles-pane.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/profiles-pane.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: The Profiles pane includes a list of profiles to use to process files. The Profiles pane includes the following options: Profile Name —Specifies the unique profile name for command-line arguments and log files. Activate —Processes the available files in the inbox. The utility determines the optimum

### Profiles Pane

The Profiles pane includes a list of profiles to use to process files. The Profiles pane includes the following options:

- Profile Name 
 —Specifies the unique profile name for command-line arguments and log files.
- Activate 
 —Processes the available files in the inbox. The utility determines the optimum number of available files in the inbox to process at the same time. Use the
 TestStand Offline Results Processing Utility Settings 
 dialog box to adjust the number of files to process simultaneously.
 Note 
 When you launch the utility, it automatically activates profiles that were active during the previous processing session.
- Pause 
 —Pauses processing files in the inbox. The utility finishes processing the currently processing files and does not start processing any new files.
- Processing Configuration 
 —Specifies the result processing configuration set to use to process the raw results files.
  - New Configuration 
 —Launches the
 Manage Result Processing Configurations 
 dialog box, in which you create or delete result processing configurations.
  - Edit Configuration 
 —Launches the
 Result Processing 
 dialog box, in which you can enable or disable only the installed built-in and custom result processing model plug-ins in the active result processing configuration and configure how the model plug-ins process test results.
- Inbox 
 —Specifies the directory in which to store raw results files. When you create a new file in this directory, the utility adds the file to the inbox and processes the file if the profile is active.
- Outbox 
 —Specifies the directory in which to store raw results files and reports after processing.
- Callback file 
 —Specifies the sequence file to use as the callback file when processing the raw results files. This option supersedes the default callbacks file you selected in the TestStand Offline Results Processing Utility Settings dialog box. If you do not specify a callback file in this option, the utility uses the default callback file. If you do not specify a default callback file, the utility does not use any callback file. Click the
 Clear Settings 
 button to reset the callback file to the default setting if you made changes to this option.

#### See Also

[Manage Result Processing Configurations dialog box](manage-result-processing-configurations-dialo.html)

[Result Processing dialog box](result-processing-dialog-box.html)

[TestStand Offline Results Processing Utility Settings](teststand-offline-results-processing-utility.html)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/properties-dialog-box.html language=enus -->
## TOPIC 04003: Properties Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/properties-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/properties-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Call the PropertyObject.DisplayPropertiesDialog method to launch the Properties dialog box. The Properties dialog box contains the following tabs: General —Changes the value, numeric format, flags, and comments for a property. Bounds —Specifies array sizes. See Also PropertyObject.DisplayPropertiesD

### Properties Dialog Box

Call the
 [PropertyObject.DisplayPropertiesDialog](../tsapiref/propertyobject-displaypropertiesdialog.html)
 method to launch the Properties dialog box.

The Properties dialog box contains the following tabs:

- General 
 —Changes the value, numeric format, flags, and comments for a property.
- Bounds 
 —Specifies array sizes.

#### See Also

[PropertyObject.DisplayPropertiesDialog](../tsapiref/propertyobject-displaypropertiesdialog.html)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/properties-tab-edit-legacy-property-loader-di.html language=enus -->
## TOPIC 04004: Properties Tab - Edit Legacy Property Loader Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/properties-tab-edit-legacy-property-loader-di.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/properties-tab-edit-legacy-property-loader-di.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Properties Tab The Properties tab contains the following options when you select Database in the Data Location ring control: Data Link Name —The name of the data link the dialog box uses to populate the Step Name Column ring control and to create columns. Click Select Data Link to select a predefine

### Properties Tab - Edit Legacy Property Loader Dialog Box

#### Properties Tab

The Properties tab contains the following options when you select Database in the Data Location ring control:

- Data Link Name 
 —The name of the data link the dialog box uses to populate the Step Name Column ring control and to create columns. Click
 Select Data Link 
 to select a predefined data link in the
 Select Data Link 
 dialog box.
- Statement Handle (Number) 
 —The name of the variable or property that contains the SQL statement handle the step uses to import values at run time. The variable or property is of the Number data type. Acquire a reference to a handle by calling an Open SQL Statement step.
- SQL SELECT Statement 
 —The SQL statement the dialog box uses at edit time to create columns and populate ring controls that contain column names. The SQL SELECT Statement ring control contains a list of the Open SQL Statement steps in the current sequence file. TestStand will only populate the ring controls when the selected SQL Statement step uses a literal string or an expression that is valid at edit time.
- Step Name Column 
 —The name of the SQL statement column that contains the names of the sequence steps and variable scopes that define the rows of data.
- Properties List Source 
 —The name of the variable or property in which to store the property mappings the step performs. The variable or property must be a
 DatabasePropertyMapping 
 array.
- Import to Run-time Sequence Only 
 —Specifies whether the imported properties only affect the invocation of the currently running sequence, or whether the imported properties affect all future invocations of one or more sequences in a selected sequence file. When you import properties to the currently running sequence, you typically place the Property Loader step in the Setup step group for the sequence the step updates. When the import operation applies to all future invocations of sequences, you typically execute the Property Loader step before calling the selected sequences multiple times.
 Note 
 If you disable this option, you must specify a valid sequence file and sequence. When the sequence you specify is the current sequence or when you specify
 <ALL SEQUENCES
 >, the step also applies the values to the run-time copy of the sequence.
  - Use Current Sequence File 
 —Selects the file where the step is located.
  - Sequence File 
 —The path of the sequence file into which to import variables and properties. Enable the Use Current Sequence File option to select the sequence file of the step. You must specify a valid sequence filename for the step to work properly.
  - Sequence 
 —The name of the sequence into which to import variables and properties. The specified sequence must exist in the specified sequence file. Select the <
 ALL SEQUENCES 
 > tag from the drop-down list to instruct TestStand to import variables and properties for all of the sequences in the specified sequence file. You must specify a valid sequence name for the step to work properly.
- Properties 
 —The mapping of column names to variables or properties the step loads. The section contains two lists of variables and properties. The Available list control contains the properties and variables available in the selected sequence file and sequence. The Selected list control contains the properties and variables you select.
 Click the
 Limits>
 button to add all limit properties to the Selected list control. 
 You can add one or more properties to the Selected list control by selecting items in the Available properties tree and clicking the single right arrow button (>). The double right arrow button (>>) adds all of the properties present in the Variables pane to the Selected list control. 
 To deselect one or more properties, select them in the Selected list control and click the single left arrow button (<). Click the double left arrow button (<<) to remove all of the properties in the Selected list control.
  - Property Name 
 —The currently selected property in the Selected list control.
  - Column Name/Number 
 —The name or index of the column from which the step loads the property.
- Apply Imported Values to Related Executions 
 —When you enable this option, the imported values are shared among related executions. Related executions include the original execution that the application and all subsequent executions TestStand invokes using a Sequence Call step initiates. For example, when you use the Batch process model, related executions include the following: the controlling execution, all test socket executions, and any additional executions these executions invoke.
- Append data type to column name 
 —When you enable this control, TestStand automatically appends the name of the data type of a property to the column name for a property when you select a property from the Available list.
- Max size for column names 
 —The maximum number of characters for a column name. Many databases limit the size of a column name. Use the ring control to select the limit for any DBMS TestStand supports by default.
- Create Columns 
 —Launches the
 Create Columns 
 dialog box. TestStand automatically populates the dialog box with the list of column names that you have selected but the SQL statement does not return. You typically use the Create Columns dialog box to add new columns to a database table for any newly selected properties.

Use the
 Expression Browse
 button to launch the
 [Expression Browser](expression-browser-dialog-box.html)
 dialog box for controls which contain TestStand
 [expressions](/csh?context=ts_tsfundamentals_bldgblocks_expressions)
 .

#### See Also

[Create Columns dialog box](create-columns-dialog-box.html)

[Expression Browser dialog box](expression-browser-dialog-box.html)

[Select Data Link dialog box](select-data-link-dialog-box.html)

Parent topic:

Edit Legacy Property Loader Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/properties-tab-edit-legacy-property-loader-di2.html language=enus -->
## TOPIC 04005: Properties Tab - Edit Legacy Property Loader Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/properties-tab-edit-legacy-property-loader-di2.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/properties-tab-edit-legacy-property-loader-di2.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Properties Tab The Properties tab contains the following options when you select File from the Data Location ring control: Properties List Source —The name of the variable or property in which to store the property mappings the step performs. The variable or property must be a DatabasePropertyMappin

### Properties Tab - Edit Legacy Property Loader Dialog Box

#### Properties Tab

The Properties tab contains the following options when you select File from the Data Location ring control:

- Properties List Source 
 —The name of the variable or property in which to store the property mappings the step performs. The variable or property must be a
 DatabasePropertyMapping 
 array.
- Import to Run-time Sequence Only 
 —When you enable this option, the imported properties affect only the invocation of the currently running sequence, or whether the imported properties affect all future invocations of one or more sequences in a selected sequence file. When you import properties to the currently running sequence, you typically place the Property Loader step in the Setup step group for the sequence the step updates. When the import operation applies to all future invocations of sequences, you typically execute the Property Loader step before calling the selected sequences multiple times.
 Note 
 If you disable this option, you must specify a valid sequence file and sequence. When the sequence you specify is the current sequence or when you specify
 <ALL SEQUENCES>
 , the step also applies values to the run-time copy of the sequence.
  - Use Current Sequence File 
 —Selects the file where the step is located.
  - Sequence File 
 —The path of the sequence file into which to import variables and properties. Enable the
 Use Current Sequence File 
 option to select the sequence file of the step. You must specify a valid sequence filename for the step to work properly.
  - Sequence 
 —The name of the sequence into which to import variables and properties. The specified sequence must exist in the specified sequence file. Select the
 <ALL SEQUENCES> 
 tag from the drop-down list to instruct TestStand to import variables and properties for all of the sequences in the specified sequence file. You must specify a valid sequence name for the step to work properly.
- Properties 
 —The mapping of column names to variables or properties the step loads. The section contains two lists of variables and properties. The Variables pane contains the properties and variables available in the selected sequence file and sequence. The Selected list control contains the properties and variables you select.
 Click the
 Limits >
 button to add all limit properties to the Selected list control. 
 To add one or more properties to the Selected list control, select items in the Available properties tree and click the single right arrow button (>). Click the double right arrow button (>>) to add all of the properties in the Available properties tree to the Selected list control. 
 Click the
 Add
 button to add properties to the Selected list control when the expression in the Sequence File or Sequence options cannot be evaluated and the Available properties tree is empty. 
 To deselect one or more properties, select them in the Selected list control and click the single left arrow button (<). The double left arrow button (<<) removes all of the properties from the Selected list control.
  - Import All Properties from Data Location 
 —When you enable this option, TestStand ignores the selected property list and imports all properties from the file or clipboard instead. This option does not apply when importing from databases.
  - Property Name 
 —The currently selected property in the Selected list control. When you select a container or array property, TestStand stores the contents of the property as an XML stream.
- Apply Imported Values to Related Executions 
 —When you enable this option, related executions share the imported values. Related executions include the original execution that the application and all subsequent executions TestStand invokes using a Sequence Call step initiates. For example, when you use the Batch process model, related executions include the following: the controlling execution, all test socket executions, and any additional executions these executions invoke.

Parent topic:

Edit Legacy Property Loader Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/properties-tab-legacy-import-export-propertie.html language=enus -->
## TOPIC 04006: Properties Tab - Legacy Import/Export Properties Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/properties-tab-legacy-import-export-propertie.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/properties-tab-legacy-import-export-propertie.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Properties Tab The Properties tab for file or clipboard locations contains the following options: Sequence —Selects the sequence to import values to or export values from. Properties —The names of the variables and properties to import or export. This section displays the available variables and pro

### Properties Tab - Legacy Import/Export Properties Dialog Box

#### Properties Tab

The Properties tab for file or clipboard locations contains the following options:

- Sequence 
 —Selects the sequence to import values to or export values from.
- Properties 
 —The names of the variables and properties to import or export. This section displays the available variables and properties in the selected sequence, and a list control that contains the variables and properties you select.
 Use the Limits (>) button to add all limit properties to the Selected list control. 
 You can add one or more properties to the Selected list control by selecting items from the Properties section and clicking the single right arrow button (>). The double right arrow button (>>) adds all of the properties to the Selected list control. You can also add properties to the Selected List control using the
 Add
 button. 
 To deselect one or more properties, select them in the Selected list control and click the single left arrow button (<). The double left arrow button (<<) removes all of the properties in the Selected list control.
  - Import All Properties from Data Location 
 —TestStand ignores the selected property list and import all properties from the file or clipboard instead. This option does not apply when importing from databases.
  - Property Name 
 —The currently selected property in the Selected list control. When you select a container or array property, TestStand stores the contents of the property as an XML stream.

Parent topic:

File or Clipboard Data Location - Legacy Import/Export Properties Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/properties-tab-step-settings-pane.html language=enus -->
## TOPIC 04007: Properties Tab - Step Settings Pane

- bundle_id: `teststand-api-reference`
- source_path: `tsref/properties-tab-step-settings-pane.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/properties-tab-step-settings-pane.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Properties Tab To examine and modify the values of properties of a step, select Step Settings from the context menu for a step in the Steps pane of the Sequence File window. You can select multiple steps and configure shared properties for each step at the same time. The Properties tab contains the

### Properties Tab - Step Settings Pane

#### Properties Tab

To examine and modify the values of properties of a step, select
 Step Settings
 from the context menu for a step in the
 [Steps](steps-pane-execution-window.html)
 pane of the Sequence File window. You can select multiple steps and configure shared properties for each step at the same time.

The Properties tab contains the following panels:

- General 
 —The name, type, adapter, icon and comment for the step. The panel also displays the description of a step.
- Run Options 
 —Various options for loading and running the
 code module 
 .
- Looping 
 —When you enable this option, TestStand loops on the step. TestStand can loop a fixed number of times or loop until a specified number of iterations pass or fail. You can also customize the loop conditions.
- Post Actions 
 —The action to take when the step finishes executing.
- Switching 
 —When you enable this option, TestStand performs switching operations before the step executes and after the step executes.
- Synchronization 
 —Specifies when TestStand postpones execution of this step or other steps to synchronize the execution of multiple steps. You can also use the
 Synchronization step types 
 to perform more advanced types of synchronization.
- Expressions 
 —
 Expressions 
 TestStand executes before and after the step executes.
- Preconditions 
 —The conditions that must be
 True 
 for the step to execute.
- Requirements 
 —Provides a mechanism for notating product and unit requirements the step covers. This control contains a list of strings where each string represents a single requirement. You can also notate requirements information in the
 Workspace Object Properties 
 ,
 Sequence File Properties 
 , and
 Sequence Properties 
 dialog boxes.
- Additional Results 
 —Adds and configures additional results. An additional result is a value TestStand adds to the result list of a step when the step executes and when you skip a step or force the step to pass or fail. An additional result can be a module parameter or a custom additional result in which you specify the name and value of the result.
- Property Browser 
 —Browses the built-in and custom properties of the step. The Property Browser is read-only during execution.

#### See Also

[Sequence Properties dialog box](sequence-properties-dialog-box.html)

[Sequence File Properties dialog box](sequence-file-properties-dialog-box.html)

[Steps Pane](steps-pane-execution-window.html)

[Synchronization Step Types](synchronization-step-types.html)

[Workspace Object Properties dialog box](workspace-object-properties-dialog-box.html)

Parent topic:

Step Settings Pane

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/properties-tab-user-group-properties-dialog-b.html language=enus -->
## TOPIC 04008: Properties Tab - User/Group Properties Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/properties-tab-user-group-properties-dialog-b.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/properties-tab-user-group-properties-dialog-b.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Properties Tab The Properties tab displays the settings for an individual user or user group. The tab contains the following options: User/Group Name —A case-insensitive login or group name. Full Name —The descriptive full name of the user. This control is visible for individual users only. Comment

### Properties Tab - User/Group Properties Dialog Box

#### Properties Tab

The Properties tab displays the settings for an individual user or user group. The tab contains the following options:

- User/Group Name 
 —A case-insensitive login or group name.
- Full Name 
 —The descriptive full name of the user. This control is visible for individual users only.
- Comment 
 —Additional information about the user or group.
- Password 
 —A case-sensitive password for the user. This control is visible for individual users only.
- Confirm Password 
 —Confirms the specified case-sensitive password in the Password control. This control is visible for individual users only.
- Group Privileges 
 —Lists the groups of which the user is a member. This control is visible for individual users only.
- Group Members 
 —Lists the users that are members of the selected group. This control is visible for user groups only.
- Advanced 
 —Displays a submenu with the following options:
  - Flags 
 —Launches the
 Edit Flags 
 dialog box, in which you can modify the property flags for the user or group.
  - Attributes 
 —Launches the
 Attributes 
 dialog box, in which you can create and edit attributes for the user or group.

#### See Also

[Attributes dialog box](attributes-dialog-box.html)

[Edit Flags dialog box](edit-flags-dialog-box.html)

Parent topic:

User/Group Properties Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/property-browser-panel-step-settings-pane.html language=enus -->
## TOPIC 04009: Property Browser Panel - Step Settings Pane

- bundle_id: `teststand-api-reference`
- source_path: `tsref/property-browser-panel-step-settings-pane.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/property-browser-panel-step-settings-pane.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Property Browser Panel The Property Browser panel displays the built-in and custom properties for the step. You can examine and modify the values of these properties. You can also access the properties of a step using the Variables pane of a Sequence File window or Execution window. You can sort the

### Property Browser Panel - Step Settings Pane

#### Property Browser Panel

The Property Browser panel displays the built-in and custom properties for the step. You can examine and modify the values of these properties. You can also access the properties of a step using the Variables pane of a Sequence File window or Execution window.

You can sort the contents of the Property Browser panel. Click any column header to sort the view by the values of that column in increasing order. Click the column header again to sort the values in decreasing order. Click the column header a third time to restore the values to the unsorted order.

The Property Browser Panel contains the following options:

- Filter 
 —Used to filter variables and properties by name. To clear the filter, click the X button. Use the Show match sub-properties option to display the sub-properties of containers that match the current filter.
 Note 
 Array elements, including steps, are not filtered out unless all array elements and their sub-properties are filtered out.

Note

#### See Also

[Variables Pane - Execution Window](variables-pane-execution-window.html)

[Variables Pane - Sequence File Window](variables-pane-sequence-file-window4.html)

Parent topic:

Properties Tab - Step Settings Pane

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/property-loader-plugins.html language=enus -->
## TOPIC 04010: Property Loader Plugins

- bundle_id: `teststand-api-reference`
- source_path: `tsref/property-loader-plugins.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/property-loader-plugins.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Property Loader Plugins Property Loader plugins read data from a property loader source during import, write data to a property loader source during export, and validate the property loader source when using an analyzer. Creating Property Loader Plugins National Instruments recommends that you copy

### Property Loader Plugins

#### Property Loader Plugins

Property Loader plugins read data from a property loader source during import, write data to a
property loader source during export, and validate the property loader source when using an
analyzer.

#### Creating Property Loader Plugins

National Instruments recommends that you copy a plugin template from the
 <TestStand>\Components\PropertyLoader\Templates\<Environment>
 directory to the
 <TestStand Public>\Components\PropertyLoader
\<YourPluginName>
 directory, where
 <Environment>
 is LabVIEW, CVI, C#, or VC, and
 <YourPluginName>
 is the descriptive name or the unique ID of the property loader plugin.

Note

NI also recommends using your company name as part of the directory name to avoid
potential conflicts with other custom plugins. Make sure the DLL or lvlib is present under the
 <TestStandPublic>\Components\PropertyLoader
 directory.

Note

TestStand ships with property loader plugins that support the following source
types:

- Comma Delimited Text 
 (.csv)
- Tab Delimited Text 
 (.txt)
- Excel file 
 (.xlsx)
- Databases 
 (Access, MySQL, SQLServer, Sybase, and Oracle version 12c or later)

See the
 [File Formats](/csh?context=ts_tsref_propertyloaderplugins_fileformat)
 topic for more information about the required file structures for the .csv, .txt, Execl plugins. See the
 [Database Table Schemas](/csh?context=ts_tsref_propertyloaderplugins_dbformat)
 topic for more information about the required table schemas for the database plugin.

TestStand also includes
 [legacy plugins](legacy-plugins.html)
 for use with the
 [Legacy Import/Export Properties tool](legacy-import-export-properties-dialog-box.html)
 that support the same source types listed above.

#### Interfaces Used by Property Loader Plugin and Property Loader Framework

Property loader plugin framework should pass all the required information, such as configuration and properties list to import/export, to the property loader plugin.

Also, property loader plugin should return information of properties existing in the source and their value to the property loader framework.

Use the following defined interface and enums to communicate information between property loader framework and plugin. All the interfaces specified below are implemented by the property loader framework and are passed to the plugin as parameters. Plugin usees the parameters to perform import/export.

- For plugins created in .NET, the parameters are passed as interface.
- For plugins created in C, the parameters are passed as IDispatch*.
- For plugins created in CVI, the parameters are passed as CAObjHandle.
- For plugins created in LabVIEW, the parameters are passed as Automation Refnum.

Parent topic:

Property Loader Step

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/property-loader-step.html language=enus -->
## TOPIC 04011: Property Loader Step

- bundle_id: `teststand-api-reference`
- source_path: `tsref/property-loader-step.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/property-loader-step.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Property Loader step to dynamically load property and variable values from a property loader source (a file or database containing data for your property objects). The new Property Loader features more intuitive user interfaces, logs more details in the result list, supports the use of alias

### Property Loader Step

Use the Property Loader step to
 [dynamically load](import-export-properties-tool.html)
 property and variable values from a
 [property loader source](configuring-a-property-loader-source.html)
 (a file or
 [database](using-a-database-as-a-property-loader-source.html)
 containing data for your property objects). The new
Property Loader features more intuitive user interfaces, logs more details in the result list,
supports the use of
 [alias names](/csh?context=ts_tsref_plaliasnames)
 , and allows you to
 [preview your imported data](previewing-your-imported-data.html)
 before you
finalize the import operation.

The Property Loader also features
 [plugins](property-loader-plugins.html)
 to support importing and exporting data
to and from custom formats. You can import and export to and from an Excel workbook
(.xlsx) file even on machines that do not have Microsoft Excel installed.

You can apply the values you load to the sequence executing in the current thread. For
example, you can develop a sequence that tests two different models of cellular phone, where
each model requires unique limit values for each step. To specify limit values, include a
Property Loader step in the Setup step group of the sequence to initialize the property and
variable values of the sequence.

You can also load values for properties into sequences so that all subsequent invocations of the
sequences in the file use the dynamically loaded property values. For example, include a
Property Loader step in a ProcessSetup model callback sequence the execution calls once so
the execution can call the client sequence file multiple times with the dynamically loaded
property values.

Note

Legacy Property Loader

Legacy Import/Export Properties tool

<TestStand>
\Components\StepTypes\Database\LegacyImportExportTool.ini

Importing and Exporting with a Legacy Source

Parent topic:

Built-In Step Types

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/property-selector-import-export-properties-to.html language=enus -->
## TOPIC 04012: Property Selector - Import/Export Properties Tool

- bundle_id: `teststand-api-reference`
- source_path: `tsref/property-selector-import-export-properties-to.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/property-selector-import-export-properties-to.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Property Selector The Property Selector is used to select properties for which values will be imported using the Property Loader step type. The Property Selector contains the following options: Filters — It is used to filter the properties that are being displayed in the Properties List. Use the fil

### Property Selector - Import/Export Properties Tool

#### Property Selector

The Property Selector is used to select properties for which values will be imported
using the Property Loader step type. The Property Selector contains the following options:

- Filters 
 — It is used to filter the properties that are being displayed in the Properties List. Use
the filters context menu to change filter options. The filters context menu contains the
following options:
  - All Properties 
 —Displays all the properties present in the target sequence file.
  - Selected Properties 
 —Displays only selected properties.
  - Limit Properties 
 —Displays only limit properties in the target sequence file.
- Views 
 — It is used to change the view of the Properties List. Use the views context menu to
change view. The views context menu has following options:
  - Display Names 
 —Shows the display names for the properties in the properties list.
  - Property Names 
 —Shows the real name of a property instead of its display name for the
properties in the properties list.
  - Alias Names 
 —Shows the alias names for various properties present in the properties list.
  - Combined Sequences 
 —Shows a list of properties which are grouped together based on
their category (Steps, Locals, Parameters, FileGlobals, StationGlobals). These categories
contain all the properties/variables present in the target sequence file. For Example, local
variables for all the sequences in the target sequence file is displayed as a child of Locals
container.
- Search 
 —Use it to search for a property in the properties list. Specify the property name in the
search box and then click on search button or hit Enter key to perform search. Remove the text
in the search field or click on clear search button to display the properties list which was
getting displayed before performing search.
- Load Source Prototype 
 —All the properties existing in the specified property loader source
will be selected in the properties list.
- Clear Property Selector 
 —Clears all the selections made in the properties list and clears all
the property loader groups.
- Property Selector Dialog 
 —Launch the Property Selector dialog box.
- Properties List 
 —Properties List displays all the properties in the target sequence file. It
displays the selection state of properties which are present in the selected property loader
group. You can check the property to add it into the selected property loader group which will
be exported to the Property Loader source. The properties list contains following items:
  - Name— 
 Specifies the display name or the real name of the property as configured in the
views.
  - Type 
 —Specifies the data type for the property.
  - Group Names 
 —Specifies the name of the property loader group in which the property is
present.
  - Alias Names 
 —Specifes the alias name for a property. The alias name can be edited by
editing the value in this column. Alias name specified for a property in the combined
sequences view will be applied for all sequence and steps while alias name specified for a
property in other view will be applied for the specific sequence and step.

Parent topic:

Import/Export Properties Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/property-selector-import-export-properties-to_2.html language=enus -->
## TOPIC 04013: Property Selector - Import/Export Properties Tool

- bundle_id: `teststand-api-reference`
- source_path: `tsref/property-selector-import-export-properties-to_2.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/property-selector-import-export-properties-to_2.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Property Selector The Property Selector is used to select properties for which values will be imported using the Property Loader step type. The Property Selector contains the following options: Filters — It is used to filter the properties that are being displayed in the Properties List. Use the fil

### Property Selector - Import/Export Properties Tool

#### Property Selector

The Property Selector is used to select properties for which values will be imported
using the Property Loader step type. The Property Selector contains the following options:

- Filters 
 — It is used to filter the properties that are being displayed in the Properties List. Use
the filters context menu to change filter options. The filters context menu contains the
following options:
  - All Properties 
 —Displays all the properties present in the target sequence file.
  - Selected Properties 
 —Displays only selected properties.
  - Limit Properties 
 —Displays only limit properties in the target sequence file.
- Views 
 — It is used to change the view of the Properties List. Use the views context menu to
change view. The views context menu has following options:
  - Display Names 
 —Shows the display names for the properties in the properties list.
  - Property Names 
 —Shows the real name of a property instead of its display name for the
properties in the properties list.
  - Alias Names 
 —Shows the alias names for various properties present in the properties list.
  - Combined Sequences 
 —Shows a list of properties which are grouped together based on
their category (Steps, Locals, Parameters, FileGlobals, StationGlobals). These categories
contain all the properties/variables present in the target sequence file. For Example, local
variables for all the sequences in the target sequence file is displayed as a child of Locals
container.
- Search 
 —Use it to search for a property in the properties list. Specify the property name in the
search box and then click on search button or hit Enter key to perform search. Remove the text
in the search field or click on clear search button to display the properties list which was
getting displayed before performing search.
- Load Source Prototype 
 —All the properties existing in the specified property loader source
will be selected in the properties list.
- Clear Property Selector 
 —Clears all the selections made in the properties list and clears all
the property loader groups.
- Property Selector Dialog 
 —Launch the Property Selector dialog box.
- Properties List 
 —Properties List displays all the properties in the target sequence file. It
displays the selection state of properties which are present in the selected property loader
group. You can check the property to add it into the selected property loader group which will
be exported to the Property Loader source. The properties list contains following items:
  - Name— 
 Specifies the display name or the real name of the property as configured in the
views.
  - Type 
 —Specifies the data type for the property.
  - Group Names 
 —Specifies the name of the property loader group in which the property is
present.
  - Alias Names 
 —Specifes the alias name for a property. The alias name can be edited by
editing the value in this column. Alias name specified for a property in the combined
sequences view will be applied for all sequence and steps while alias name specified for a
property in other view will be applied for the specific sequence and step.

Parent topic:

Import/Export Properties Tool

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/property-selector-property-loader-step.html language=enus -->
## TOPIC 04014: Property Selector - Property Loader Step

- bundle_id: `teststand-api-reference`
- source_path: `tsref/property-selector-property-loader-step.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/property-selector-property-loader-step.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Property Selector The Property Selector is used to select properties for which values will be imported using the Property Loader step type. The Property Selector contains the following options: Select Sequence —Specifies the target sequence file into which values will be imported. Select <Current Se

### Property Selector - Property Loader Step

#### Property Selector

The Property Selector is used to select properties for which values will be imported
using the Property Loader step type. The Property Selector contains the following options:

- Select Sequence 
 —Specifies the target sequence file into which values will be imported.
 Note 
 Select
 <Current Sequence>
 to import values to the current sequence and
 <All Sequences>
 to import values to all the sequences in the target sequence file.
- Property Loader Groups 
 —Specifies the property loader groups from which values will be imported.
- Precondition 
 —Determines whether a specified group should be considered for import.
 Note 
 Use the
 “$(GroupName)”
 and
 “S(GroupId)”
 macros in the expression to denote the name and ID of a group.
- Description 
 —Describes the property loader groups from which values will be imported.
- Filters 
 —Filters the properties displayed in the Properties List. The Filters context menu contains the following options:
  - All Properties 
 —Displays all properties in the target sequence file.
  - Selected Properties 
 —Displays only selected properties in the target sequence file.
  - Limit Properties 
 —Displays only limit properties in the target sequence file.
- Views 
 —Determines the view of the Properties List. The Views context menu has following options:
  - Display Names 
 —Shows the display names of properties in the Properties List.
  - Property Names 
 —Shows the real names of properties in the Properties List, rather than their display names.
  - Alias Names 
 —Shows the alias names of properties in the Properties List.
  - Combined Sequences 
 —Shows a list of properties grouped together based on their category (
 Steps, Locals, Parameters, FileGlobals, StationGlobals 
 ). These categories contain all the properties/variables in the target sequence file. For example, local variables for all sequences in the target sequence file are displayed as a child of the
 Locals 
 container.
- Search 
 —Searches for a property in the Properties List. Specify the property name in the search field and click the
 Search 
 button or press the <Enter> key to perform a search. Delete the text in the search field or click the
 Clear Search 
 button to revert to the Properties List that was displayed before you performed a search.
- Load Source Prototype 
 —Loads all properties in the specified property loader source. By default, these loaded properties will be selected in the Properties List.
- Clear Property Selector 
 —Clears all selections made in the Properties List and clears all property loader groups.
- Property Selector Dialog 
 —Launches the Property Selector dialog box.
- Properties List 
 —Displays all properties in the target sequence file. The Properties List also displays the selection state of properties in the specified property loader group. Enable the checkmark next to a property to add it into the specified property loader group that will be exported to the property loader source. The Properties List displays following items:
  - Name 
 —Specifies the display name or the real name of the property, depending on the View that you have configured.
  - Type 
 —Specifies the data type of the property.
  - Group Names 
 —Specifies the name of the property loader group in which the property exists.
  - Alias Names 
 —Specifes the alias name of the property. You can edit the value in this column to modify the alias name.
 Note 
 The alias name specified for a property in the Combined Sequences View is applied to all sequences and steps. An alias name specified for a property in any other view is applied to a specific sequence and step.

Parent topic:

Target File and Source Settings Tab

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/prototypes-conflict-dialog-box.html language=enus -->
## TOPIC 04015: Prototypes Conflict Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/prototypes-conflict-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/prototypes-conflict-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: TestStand launches the Prototypes Conflict dialog box when you click Create Code on the Source Code tab of a Specify Module dialog box and when the prototype of the code template is different than the prototype specified on the Module tab. The Prototypes Conflict dialog box contains the following op

### Prototypes Conflict Dialog Box

TestStand launches the Prototypes Conflict dialog box when you click
 Create Code
 on the Source Code tab of a Specify Module dialog box and when the prototype of the code template is different than the prototype specified on the Module tab.

The Prototypes Conflict dialog box contains the following options:

- Use the Prototype from the Code Template and Update the Prototype In the Module Tab 
 —TestStand uses the prototype the
 code module 
 specifies and to replace the prototype on the Module tab with the prototype the code template specifies.
- Keep the Current Parameter Values 
 —TestStand keeps the current parameter values when refreshing the prototype on the Module tab.
- Use the Prototype from the Module Tab 
 —TestStand ignores the code template prototype and to use the prototype the Module tab specifies.

#### See Also

[Module Tabs and Specify Module Dialog Boxes](specify-module-tabs-and-dialog-boxes.html)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/provider-tab-data-link-properties-dialog-box.html language=enus -->
## TOPIC 04016: Provider Tab - Data Link Properties Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/provider-tab-data-link-properties-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/provider-tab-data-link-properties-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provider Tab Typically, a provider communicates with a specific database management system (DBMS) such as Oracle or SQL Server. With the Microsoft Object Linking and Embedded Database (OLE DB) Provider for ODBC Drivers, you can use any ODBC driver. Some providers have limited functionality . Refer t

### Provider Tab - Data Link Properties Dialog Box

#### Provider Tab

Typically, a provider communicates with a specific database management system (DBMS) such as Oracle or SQL Server. With the Microsoft Object Linking and Embedded Database (OLE DB) Provider for ODBC Drivers, you can use any ODBC driver. Some providers have
 [limited functionality](/csh?context=ts_tsfundamentals_database_known_issues)
 . Refer to the
 [NI TestStand Readme](http://www.ni.com/r/tz6q4z)
 for information about recommended database client software.

Click
 Help
 to launch the Microsoft online help for this tab.

#### See Also

[Database Known Issues](/csh?context=ts_tsfundamentals_database_known_issues)

Parent topic:

Data Link Properties Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/pulse-operation-notification-settings-edit-ta.html language=enus -->
## TOPIC 04017: Pulse Operation - Notification Settings Edit Tab

- bundle_id: `teststand-api-reference`
- source_path: `tsref/pulse-operation-notification-settings-edit-ta.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/pulse-operation-notification-settings-edit-ta.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Pulse Operation Use the Pulse operation to notify one or all currently waiting threads. This operation differs from the Set operation because it notifies only the threads already waiting when the Pulse operation occurs. Threads that wait on the notification after a Pulse operation occurs block until

### Pulse Operation - Notification Settings Edit Tab

#### Pulse Operation

Use the Pulse operation to notify one or all currently waiting threads. This operation differs from the Set operation because it notifies only the threads already waiting when the Pulse operation occurs. Threads that wait on the notification after a Pulse operation occurs block until you Set or Pulse the notification again. A Pulse operation places the notification in a Cleared state, even if the notification was in a Set state before the Pulse operation. Enable the
 Pulse
 option on the left of the Notification Settings panel.

The Pulse operation contains the following options:

- Notification Name or Reference Expression 
 —The notification on which to perform the operation. You can specify the notification by name or by the object reference you receive when you create the notification using the Use Object Reference for the Notification Reference Lifetime option.
- Data Value (optional) 
 —An optional data element to send with the pulse notification. The data can be of any type (number, string, Boolean, object reference, structured type (container), or arrays of these types). When you later wait on the notification, you must store the element into a location of an appropriate type. By default, the notification stores a copy of the data value you specify. However, when you enable the Store Data by Reference Instead of by Value option, the operation stores an ActiveX reference to the value instead. If you later store this reference into an object reference variable in the Wait operation, you can access the data using the TestStand API
 PropertyObject 
 interface and the ActiveX/COM Adapter.
- Store Data by Reference Instead of by Value 
 —Specifies how to store the data you specify in the Data Value control. Enable the option to store an ActiveX reference to the property. Leave the option disabled to store a copy of the data.
- Notify First Waiting Thread (If Any) 
 and
 Notify All Waiting Threads (If Any) 
 —Specify whether to notify all currently waiting threads or just the first waiting thread.

#### See Also

[PropertyObject](../tsapiref/propertyobject.html)

Parent topic:

Notification Settings Edit Tab

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/pulse-operation-notification-step-configurati.html language=enus -->
## TOPIC 04018: Pulse Operation - Notification Step Configuration Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/pulse-operation-notification-step-configurati.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/pulse-operation-notification-step-configurati.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Pulse Operation Use the Pulse operation to notify one or all currently waiting threads. This operation differs from the Set operation because it notifies only the threads already waiting when the Pulse operation occurs. Threads that wait on the notification after a Pulse operation occurs block until

### Pulse Operation - Notification Step Configuration Dialog Box

#### Pulse Operation

Use the Pulse operation to notify one or all currently waiting threads. This operation differs from the Set operation because it notifies only the threads already waiting when the Pulse operation occurs. Threads that wait on the notification after a Pulse operation occurs block until you Set or Pulse the notification again. A Pulse operation places the notification in a Cleared state, even if the notification was in a Set state before the Pulse operation.

The Pulse operation contains the following options:

- Notification Name or Reference Expression 
 —The notification on which to perform the operation. You can specify the notification by name or by the object reference you receive when you create the notification using the Use Object Reference for the Notification Reference Lifetime option.
- Data Value (optional) 
 —An optional data element to send with the pulse notification. The data can be of any type (number, string, Boolean, object reference, structured type (container), or arrays of these types). When you later wait on the notification, you must store the element into a location of an appropriate type. By default, the notification stores a copy of the data value you specify. However, when you enable the Store Data by Reference Instead of by Value option, the operation stores an ActiveX reference to the value instead. If you later store this reference into an object reference variable in the Wait operation, you can access the data using the TestStand API
 PropertyObject 
 interface and the ActiveX/COM Adapter.
- Store Data by Reference Instead of by Value 
 —Specifies how to store the data you specify in the Data Value control. Enable the option to store an ActiveX reference to the property. Leave the option disabled to store a copy of the data.
- Notify First Waiting Thread (If Any) 
 and
 Notify All Waiting Threads (If Any) 
 —Specify whether to notify all currently waiting threads or just the first waiting thread.

#### See Also

[PropertyObject](../tsapiref/propertyobject.html)

Parent topic:

Notification Step Configuration Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/python-adapter-configuration-dialog-box.html language=enus -->
## TOPIC 04019: Python Adapter Configuration Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/python-adapter-configuration-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/python-adapter-configuration-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Select Configure»Adapters to launch the Adapter Configuration dialog box. Select the Python adapter in the list control and click Configure . The Python Adapter Configuration dialog box contains the following options: Interpreter to use —Interpreter session to use for execution. It contains the foll

### Python Adapter Configuration Dialog Box

Select
 Configure»Adapters
 to launch the Adapter Configuration dialog box. Select the
 Python
 adapter in the list control and click
 Configure
 .
The Python Adapter Configuration dialog box contains the following options:

- Interpreter to use 
 —Interpreter session to use for execution. It contains the following options:
  - Global 
 —All Python modules execute in a single instance of the Python interpreter.
  - Per Execution 
 —Each execution uses a separate instance of the Python interpreter to execute modules.
  - Per Thread 
 —Each thread uses a separate instance of the Python interpreter to execute modules.
- Display Console for Interpreter Sessions 
 —Specifies whether to display a console window for the Python interpreter session when executing the Python module.
- Virtual Environment 
 —Directory path of the virtual environment to use for executing the Python code module. Leave the field empty to use the default environment.
 Note 
 TestStand supports virtual environments created using the virtualenv or venv tool.
- Reload Modified Modules Before Execution 
 —
 If you enable this option prior to execution, TestStand will reload an updated Python module without unloading other modules or restarting TestStand execution. Immediately before executing the step, if TestStand determines that the configured module is modified, TestStand then reloads the module. 
 Note 
 Enable this option only in test development and debugging environments. In production environments, disable this option.
 TestStand reloads only the module which is directly called from the step.
 Reloading the module will re-initialize all global variables of the module.
 If you modify a module that defines a class and another module stores an instance of that class, TestStand does not reload the second module when it reloads the first one. You must reload the second module to discard any instances of the objects and create new instances.
 If any Python object such as a class instance exists, and you modify the object, you must recreate the class instance after reloading the module.
- Enable Debugging 
 —Enables step into debugging operations when executing a Python module. You must install Visual Studio Code and configure your machine as described in
 Debugging Python Modules 
 .
- Enable Just My Code 
 —Specifies whether you want to debug installed libraries when you step into a Python code module.
- Executable Path 
 —File path, including the file name
 python.exe 
 , of the Python executable to use to perform step into operations when debugging Python modules.
 Note 
 In TestStand 2024 Q2 and subsequent versions, TestStand determines the executable path to use for stepping into Python modules.
- Version 
 —Python version to use for executing the Python code module.
- Application Path 
 —Location of the external application to use for viewing Python code modules.
- Arguments 
 —Command line arguments to use when launching the Python module viewer application.
 Note 
 The string
 %ModulePath%
 is the placeholder that must be a part of the argument string. TestStand uses this placeholder to provide the external application with the path to the Python code module.

#### See Also

[Python Parameter Passing Tab](python-parameter-passing-tab-type-properties.html)

[Python Module Tab](module-tab-edit-python-call-dialog-box.html)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/python-call-parameters.html language=enus -->
## TOPIC 04020: Python Call Parameters

- bundle_id: `teststand-api-reference`
- source_path: `tsref/python-call-parameters.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/python-call-parameters.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: The Python Adapter converts data between TestStand and Python when calling functions or using attributes in Python. The table below contains the mapping of data types between TestStand and Python. TestStand Python 2.7 Python 3.6+ Notes Floating Point Number float float Python has infinite precision

### Python Call Parameters

The Python Adapter converts data between TestStand and Python when calling functions or using attributes in Python. 
The table below contains the mapping of data types between TestStand and Python.

| TestStand | Python 2.7 | Python 3.6+ | Notes |
| --- | --- | --- | --- |
| Floating Point Number | float | float | Python has infinite precision for numeric data types. When converting the numeric types from Python to TestStand, data loss may occur due to overflow or underflow of a numeric value. TestStand passes numeric constants to Python using the default float type for the constant. If you want to pass numeric constants to Python as integers, change the numeric representation of constants by using the expression function Int64() or UInt64() . |
| Signed 64 Number | long | int |  |
| Unsigned 64 Number | long | int |  |
| Enum (Floating Point Representation) | float | enum | TestStand passes enums to Python modules as Python enums only if you specify a type mapping for the TestStand enum. Otherwise, TestStand passes enums to Python modules as numbers. |
| Enum (Signed 64 Representation) | long | enum |  |
| Enum (Unsigned 64 Representation) | long | enum |  |
| Boolean | bool | bool | — |
| String | str | str | — |
| Container | tuple | tuple | — |
| Array (Excluding Array of Numbers) | list | list | The type of array elements in a Python list depends on the type of array elements in TestStand. For example, Array of Strings in TestStand maps to a list of strings in Python. |
| Array of Numbers | list or NumPy array | list or NumPy array | You must install the NumPy module to pass an array of numbers from TestStand to Python as a NumPy array. TestStand passes an array of numbers to a Python module as a list or NumPy array. You can define the behavior of passing Array of Numbers to Python in any of the following ways: Specify the default behavior for passing an array of numbers to Python in the Advanced Settings Dialog for Python . Override the default behavior for subproperties of a named container in the Python Parameter Passing tab of custom data type properties. Override the default behavior by explicitly configuring the Parameter Type to List or NumPy Array in the Python Module tab . |

Note

Note

When you set the parameter type to Dynamic, TestStand uses the type of the evaluated expression to determine how to pass the data to Python.

#### See Also

[Python Enumeration Parameters](enumeration-parameters-python-call-parameters.html)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/python-parameter-passing-tab-type-properties.html language=enus -->
## TOPIC 04021: Python Parameter Passing Tab - Type Properties Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/python-parameter-passing-tab-type-properties.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/python-parameter-passing-tab-type-properties.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Python Parameter Passing Tab Depending on the custom data type, the Python Parameter Passing tab provides different options for mapping a TestStand type to a Python type. For a TestStand container, specify how TestStand maps the subproperties of a data type to the elements of a tuple parameter. If a

### Python Parameter Passing Tab - Type Properties Dialog Box

#### Python Parameter Passing Tab

Depending on the custom data type, the Python Parameter Passing tab provides different options for mapping a TestStand type to a Python type.

For a TestStand container, specify how TestStand maps the subproperties of a data type to the elements of a tuple parameter. If a data type contains a subproperty that is a named data type, you must separately configure the named data type.

The Python Parameter Passing tab contains the following options:

- Property 
 —Select a subproperty of the data type to display the type and index of the data in the tuple.
 You must separately configure the named data type to exclude its subproperties when passing a tuple by selecting
 Exclude When Passing Tuple
 , then select the behavior for passing its subproperties in the
 Pass Property as
 pull-down menu.
- Exclude When Passing Tuple 
 —Exclude the selected subproperty in the mapping between the data type and the structure.
- Type 
 —The data type of the selected subproperty. This is a read-only field.
- Index of Property in Tuple 
 —The index of the element in the tuple. You can use the index to access the data in the tuple inside the Python code module.
- Pass Property as 
 —Defines the behavior for passing a subproperty from TestStand to Python when the subproperty type is an array of numbers. It contains the following options:
  - Dynamic 
 —Use the behavior specified in the Python Adapter Configuration dialog box for passing an array of numbers.
  - List 
 —Pass the property from TestStand to Python as a list.
  - NumPy Array 
 —Pass the property from TestStand to Python as a NumPy array.

For a TestStand enumeration, specify the Python module containing the enumeration definition and the Python enumeration that the TestStant enum type will be passed into the Python module as.

The Python Parameter Passing tab contains the following options:

- Module 
 —The path to a Python (
 .py 
 ) module on disk. Click
 Browse 
 to browse for a Python module. Click
 View 
 to view the module in a text editor.
- Namespace 
 —Displays the namespace of the selected module. To learn how TestStand determines the namespace, refer to
 Python Namespaces 
 .
- Enum 
 —Select an enum from a list of enums present in the specified module.
 If the list does not show an enumeration which is present in the module, you can type the enumeration name into the text field.

#### See Also

[Python Adapter Configuration Dialog Box](python-adapter-configuration-dialog-box.html)

Parent topic:

Type Properties Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/queue-settings-edit-tab.html language=enus -->
## TOPIC 04022: Queue Settings Edit Tab

- bundle_id: `teststand-api-reference`
- source_path: `tsref/queue-settings-edit-tab.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/queue-settings-edit-tab.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: To display the Queue Settings edit tab in the TestStand Sequence Editor , insert a Queue step and select Edit Queue Settings or Step Settings from the context menu. The following operations are available when you use the Queue step type: Create —Creates a reference to a new or existing Queue object.

### Queue Settings Edit Tab

To display the Queue Settings edit tab in the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 , insert a Queue step and select
 Edit Queue Settings
 or
 Step Settings
 from the context menu. The following operations are available when you use the Queue step type:

- Create 
 —Creates a reference to a new or existing Queue object.
- Enqueue 
 —Adds new elements to the queue.
- Dequeue 
 —Removes an element and/or stores the data from an element.
- Flush 
 —Empties the queue and optionally retrieves all the elements from the queue.
- Get Status 
 —Obtains information about the current state of the queue.

#### See Also

[Synchronization Step Types](synchronization-step-types.html)

Parent topic:

Queue Step

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/queue-step-configuration-dialog-box.html language=enus -->
## TOPIC 04023: Queue Step Configuration Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/queue-step-configuration-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/queue-step-configuration-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Select Configure Queue in the context menu for the step to launch the Queue Step Configuration dialog box from a TestStand User Interface . You can also click Configure Queue on the General tab of the Step Properties dialog box. In the Queue Step Configuration dialog box, select an operation for the

### Queue Step Configuration Dialog Box

Select
 Configure Queue
 in the context menu for the step to launch the Queue Step Configuration dialog box from a
 [TestStand User Interface](teststand-user-interfaces.html)
 . You can also click
 Configure Queue
 on the
 [General](general-tab-step-properties-dialog-box.html)
 tab of the
 [Step Properties](step-properties-dialog-box.html)
 dialog box. In the Queue Step Configuration dialog box, select an operation for the step to perform.

The following operations are available when you use the Queue step type:

- Create 
 —Creates a reference to a new or existing Queue object.
- Enqueue 
 —Adds new elements to the queue.
- Dequeue 
 —Removes an element and/or stores the data from an element.
- Flush 
 —Empties the queue and optionally retrieves all the elements from the queue.
- Get Status 
 —Obtains information about the current state of the queue.

#### See Also

[Step Properties dialog box](step-properties-dialog-box.html)

[Synchronization Step Types](synchronization-step-types.html)

Parent topic:

Queue Step

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/queue-step.html language=enus -->
## TOPIC 04024: Queue Step

- bundle_id: `teststand-api-reference`
- source_path: `tsref/queue-step.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/queue-step.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use a Queue step to synchronize the production and consumption of data among threads. An Enqueue operation places a data item on the queue and blocks when the queue is full. A Dequeue operation removes an item from the queue and blocks when the queue is empty. When multiple threads block on the same

### Queue Step

Use a Queue step to synchronize the production and consumption of data among threads. An
 [Enqueue operation](enqueue-operation-queue-step-configuration-di.html)
 places a data item on the queue and blocks when the queue is full. A
 [Dequeue operation](dequeue-operation-queue-step-configuration-di.html)
 removes an item from the queue and blocks when the queue is empty. When multiple threads block on the same Queue operation, the threads unblock in first-in first-out order.

#### Configuring the Step

Use the
 [Queue Settings](queue-settings-edit-tab.html)
 edit tab in the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 and the
 [Queue Step Configuration](queue-step-configuration-dialog-box.html)
 dialog box in a
 [TestStand User Interface](teststand-user-interfaces.html)
 to configure the Queue step.

#### Step Properties

In addition to the
 [common custom properties](/csh?context=ts_tsfundamentals_custom_result_props)
 , the Queue step type defines the following step properties:

- Step.Result.TimeoutOccurred 
 —Exists only when you configure the step for the
 Enqueue 
 or
 Dequeue 
 operation. TestStand sets the value to
 True 
 when an Enqueue or Dequeue operation times out.
 Note 
 If you configure the step to use the Enqueue or Dequeue operation programmatically using the
 Step.Operation
 property, you must also create the
 Step.Result.TimeoutOccurred
 property using the
 newProperty(
 ) method for the step to execute successfully.
- Step.NameOrRefExpr 
 —Contains the Queue
 Name 
 expression for the Create operation and the Queue Name or Reference expression for all other Queue operations. For the Dequeue operation, the expression can also specify an array of names or references.
- Step.LifetimeRefExpr 
 —The object reference expression for the Queue Reference
 Lifetime 
 when you set the lifetime to Use Object Reference.
- Step.TimeoutEnabled 
 —The
 Timeout 
 Enabled setting for the Enqueue or Dequeue operation.
- Step.TimeoutExpr 
 —The Timeout expression, in seconds, for the Enqueue or Dequeue operation.
- Step.ErrorOnTimeout 
 —The Timeout Causes Run-Time Error setting for the Enqueue or Dequeue operation.
- Step.AlreadyExistsExpr 
 —Contains the Already Exists expression for the
 Create 
 operation or the Queue Exists expression for the
 Get Status operation 
 .
- Step.MaxNumElementsExpr 
 —The expression that specifies the maximum number of queue elements for the
 Create operation 
 .
- Step.MaxNumElementsOutExpr 
 —The expression that specifies where to store the maximum number of queue elements for the Get Status operation.
- Step.NumThreadsWaitingEnqueueExpr 
 —The expression that specifies where to store the number of threads waiting to enqueue for the Get Status operation.
- Step.NumThreadsWaitingDequeueExpr 
 —The expression that specifies where to store the number of threads waiting to dequeue for the Get Status operation.
- Step.Operation 
 —A value that specifies the operation for the step to perform. The valid values are
 0 
 = Create,
 1 
 = Enqueue,
 2 
 = Dequeue,
 3 
 = Flush, and
 4 
 = Get Status.
- Step.Lifetime 
 —A value that specifies the lifetime setting to use for the Create operation. The valid values are
 0 
 = Same as Sequence,
 1 
 = Same as Thread,
 2 
 = Use Object Reference, and
 3 
 = Same as Execution.
- Step.NumElementsExpr 
 —The expression that specifies where to store the current number of queue elements for the Get Status operation.
- Step.DataExpr 
 —Contains the New Element to Enqueue expression for the Enqueue operation, the Location to Store Element expression for the Dequeue operation, and the Location to Store Array of Queue Elements expression for the
 Flush 
 or Get Status operation.
- Step.ByRef 
 —The Boolean value that specifies to store a queue element by object reference instead of by value for the Enqueue operation.
- Step.EnqueueLocation 
 —A value that specifies the location to store the queue element for the Enqueue operation. The valid values are
 0 
 = Front of Queue and
 1 
 = Back of Queue.
- Step.DequeueLocation 
 —A value that specifies the location from which to remove the queue element for the Dequeue operation. The valid values are
 0 
 = Front of Queue and
 1 
 = Back of Queue.
- Step.FullQueueOption 
 —A value that specifies the options for the If the Queue is Full setting of the Enqueue operation. The valid values are
 0 
 = Wait,
 1 
 = Discard Front Element,
 2 
 = Discard Back Element, and
 3 
 = Do Not Enqueue.
- Step.RemoveElement 
 —A Boolean value that specifies to remove the element from the queue when the step performs the Dequeue operation.
- Step.WhichQueueExpr 
 —The expression that specifies where to store the array offset of the queue on which the Dequeue operation occurs.

#### See Also

[Coordinating Test Socket Data with Queue Steps (Example)](/csh?context=ts_8184)

Parent topic:

Synchronization Step Types

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/quick-drop-dialog-box.html language=enus -->
## TOPIC 04025: Quick Drop Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/quick-drop-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/quick-drop-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: The Quick Drop dialog box is an easy way to insert objects into the TestStand Sequence Editor without using mouse clicks. You can use Quick Drop to insert steps, sequences, and variables into the sequence file. Select Edit»Launch Quick Drop or use the keyboard shortcut <Ctrl + Space> to launch the Q

### Quick Drop Dialog Box

The Quick Drop dialog box is an easy way to insert objects into the TestStand Sequence Editor without using mouse clicks. You can use Quick Drop to insert steps, sequences, and variables into the sequence file.

Select
 Edit»Launch Quick Drop
 or use the keyboard shortcut <Ctrl + Space> to launch the Quick Drop dialog box.

The Quick Drop dialog box contains the following elements:

- Search Box 
 —Filters the items displayed in the list box based on the string you enter.
- List Box 
 —Displays all items you can insert into the sequence file. Select an item using the arrow keys, then press <Enter> to insert the item. These items include:
  - Steps 
 —All steps listed in the insertion palette and templates.
 Note 
 If the step is not adapter specific, you can choose the adapter to use for the step.
  - Sequences 
 —New sequences, sequences listed in templates, and sequence callbacks such as ReportOptions or PreUUT.
  - Variables 
 —All basic, built-in, custom data types and variables in templates.
 Note 
 You can choose to insert an array variant of the variable.
- Group Dropdown 
 —Displays groups into which you can insert the selected item. Depending on the type of item you select, you can insert it into the following groups:
  - Setup, Main, and Cleanup—available when a step is in focus.
  - Locals, Parameters, FileGlobals, and StationGlobals—available when a variable is in focus.

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/read-operation-edit-ivi-dmm-step-dialog-box.html language=enus -->
## TOPIC 04026: Read Operation - Edit IVI Dmm Step Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/read-operation-edit-ivi-dmm-step-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/read-operation-edit-ivi-dmm-step-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Read Operation The Read operation initiates and returns a measurement from an instrument. Read is a higher-level acquisition operation that encapsulates some of the details of using the Initiate and Fetch operations. If the Sample Count setting is greater than 1 and the Multi Point extension is enab

### Read Operation - Edit IVI Dmm Step Dialog Box

#### Read Operation

The Read operation initiates and returns a measurement from an instrument. Read is a higher-level acquisition operation that encapsulates some of the details of using the Initiate and Fetch operations. If the Sample Count setting is greater than
 1
 and the Multi Point extension is enabled, the Read operation returns an array of values. Otherwise, the operation returns a single value.

The returned value is either the actual reading the Measurement Function setting defines, or a value that indicates that an over-range condition occurred.

If an over-range condition occurs, the reading parameter contains an IEEE-defined not a number (NaN) value. To test a value for the over-range condition, specify a status expression in the Set Status if Over-Range control. If a timeout occurs before the Read operation completes, the Set Status on Timeout control determines the
 [step status](/csh?context=ts_tsfundamentals_step_status_values_table)
 .

The Read operation contains the following options:

- Data Type 
 —Specifies whether the step expects a single value or array of values. The step coerces the data type of the
 Step.Result.Reading 
 property to
 NI_IviSinglePoint 
 or
 NI_IviWave 
 , respectively.
- Measurement Destination 
 —A variable or property, as the following table describes, to which the step assigns the measurement value.
 Value Type
 Data Type of the Variable or PropertySingle values
 Number or
 NI_IviSinglePoint
 Array of values
 Array of Number or
 NI_IviWave 
 The default configuration for the step specifies
 Step.Result.Reading 
 as the destination. When you edit the step, the step automatically coerces the data type of the
 Step.Result.Reading 
 property to
 NI_IviSinglePoint 
 or
 NI_IviWave 
 , based on the value of the Data Type control. If you do not specify
 Step.Result.Reading 
 as the destination, TestStand copies the measurement value to the
 Step.Result.Reading.Data 
 property at run time unless the Copy Data to Execution Results option is disabled.
- Timeout (ms) 
 —The timeout, in milliseconds, for the operation. The Timeout setting applies to the length of time between initializing a call to Read and completing the data acquisition, not the time the DMM requires for computations or to transfer data across the instrumentation bus. To set an infinite timeout, set Timeout to
 -1 
 .
- Set Status on Timeout 
 —The status for the step result when a timeout condition occurs. When you leave this control blank, the step ignores timeout conditions.
- Set Status if Over-Range 
 —The status for the step result when a timeout condition occurs. When you leave this control blank, the step does not check for an over-range condition.
- Copy Data To Execution Results 
 —When you enable this option, TestStand copies the measurement value stored in the property
 Step.Result.Reading.Data 
 to the step result. When you disable this control, TestStand cannot include the measurement in a report or log the measurement to a database. For single-point measurements, this option is always enabled.

Parent topic:

Edit IVI Dmm Step Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/read-operation-edit-ivi-scope-step-dialog-box.html language=enus -->
## TOPIC 04027: Read Operation - Edit IVI Scope Step Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/read-operation-edit-ivi-scope-step-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/read-operation-edit-ivi-scope-step-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Read Operation Channels Tab The Channels tab for the Read operation contains the following channel-specific options: Name —The name of the channel to read. The channel name must be a valid virtual channel name as the IVI configuration for the logical name being used defines. Waveform Type —The type

### Read Operation - Edit IVI Scope Step Dialog Box

#### Read Operation

#### Channels Tab

The Channels tab for the Read operation contains the following channel-specific options:

- Name 
 —The name of the channel to read. The channel name must be a valid virtual channel name as the IVI configuration for the logical name being used defines.
- Waveform Type 
 —The type of data to retrieve from the oscilloscope. Depending on this value, the returned data is a single value (for a measurement), a one-dimensional array (Waveform), or a two-dimensional array (Waveform Min Max).
 
 Supported Value
 DescriptionAmplitude (15)
 High Voltage less the Low Voltage, in volts, over the entire waveform.
 Negative Duty Cycle (13)
 Ratio of the Negative Width to the Period of an integer number of cycles in the waveform, expressed as a percentage.
 Positive Duty Cycle (14)
 Ratio of the Positive Width to the Period of an integer number of cycles in the waveform, expressed as a percentage.
 Fall Time (1)
 Length of time, in seconds, for a falling edge of the signal to fall from the high reference level to the low reference level.
 Frequency (2)
 Frequency, in hertz, of one complete cycle in the waveform.
 Overshoot (18)
 Relative waveform distortion that follows an edge transition.
 Period (3)
 Length of time, in seconds, of one complete cycle in the waveform.
 Preshoot (19)
 Relative waveform distortion that precedes an edge transition.
 Rise Time (0)
 Length of time, in seconds, for a rising edge of the signal to rise from the low reference level to the high reference level.
 Average Voltage (10)
 Arithmetic average, in volts, measured over the entire waveform.
 Cycle Average Voltage (17)
 Arithmetic average, in volts, over an integer number of cycles in the waveform.
 Cycle Rms Voltage (16)
 True root-mean-square (RMS) voltage over an integer number of cycles in the waveform.
 High Voltage (8)
 Voltage that corresponds to 100% when using the reference levels. The oscilloscope calculates this value using either the min/max or histogram methods. The min/max method uses the maximum value found. The histogram method uses a common value found above the middle of the waveform.
 Low Voltage (9)
 Voltage that corresponds to 0% when using the reference levels. The oscilloscope calculates this value using either the min/max or histogram methods. The min/max method uses the minimum value found. The histogram method uses a common value found below the middle of the waveform.
 Max Voltage (6)
 Maximum amplitude, in volts, found in the entire waveform.
 Min Voltage (7)
 Minimum amplitude, in volts, found in the entire waveform.
 Peak To Peak Voltage (5)
 Absolute difference, in volts, between the Max Voltage and the Min Voltage.
 Rms Voltage (4)
 True root-mean-square (RMS) voltage of the entire waveform.
 Negative Width (11)
 Length of time, in seconds, between the mid-reference level points of a negative pulse in the waveform.
 Positive Width (12)
 Length of time, in seconds, between the mid-reference level points of a positive pulse in the waveform.
 Waveform (-1)
 Specifies that the Read or Fetch operation acquires a waveform with the current configuration. If specified, Read returns a one-dimensional array of points.
 Min/Max (-2)
 Specifies that the Read or Fetch operation acquires a min-max waveform that is a two-dimensional array. This constant is valid only when the Acquisition Type is set to Peak Detect or Envelope.
- Data Type 
 —Specifies whether the step expects a single value, an array of values, or a wave pair. The step coerces the data type of the elements in the array property,
 Step.Result.Reading 
 , to
 NI_IviSinglePoint 
 ,
 NI_IviWave 
 , or
 NI_IviWavePair 
 respectively.
- Measurement Destination 
 —A variable or property to which the step assigns the measurement value. For single values, the data type of the variable or property must be Number or
 NI_IviSinglePoint 
 . For an array of values, the data type of the variable or property must be array of Number or
 NI_IviWave 
 . For a wave pair, the data type of the variable or property must be a two-dimensional array of Number or
 NI_IviWavePair 
 . The default configuration for the step specifies
 Step.Result.Reading 
 as the destination. This property is an array of container where the size of the array is equal to the number of channels specified for the Read or Fetch operation. When you edit the step, the step automatically resizes the array and coerces the data type of each element of the array to
 NI_IviSinglePoint 
 ,
 NI_IviWave 
 , or
 NI_IviWavePair 
 , based on the value of the Data Type control for each channel. If you do not specify
 Step.Result.Reading 
 as the destination, TestStand copies the measurement value to the Data subproperty in each array element at run time unless the Copy Data to Execution Results option is disabled.
- Set Status if Over-Range 
 —The status for the step result when a timeout condition occurs. When you leave this control blank, the step does not check for an over-range condition.
- Copy Data to Execution Results 
 —When you enable this option, TestStand copies the measurement value stored in the property
 Step.Result.Reading.Data 
 to the step result. When you enable this control, TestStand does not include the measurement in a report or log the measurement to a database. For single-point measurements, this setting is always enabled.
- Timeout (mS) 
 —The timeout, in milliseconds, for the operation. The Timeout setting applies to the length of time between initializing a call to Read and completing the data acquisition, not the time the instrument requires for computations or to transfer data across the instrumentation bus. To set an infinite timeout, set Timeout to
 -1 
 .
- Set Status on Timeout 
 —The status for the step result when a timeout condition occurs. When you leave this control blank, the step ignores timeout conditions.

Parent topic:

Read Operation - Edit IVI Scope Step Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/read-operation-edit-ivi-scope-step-dialog-box2.html language=enus -->
## TOPIC 04028: Read Operation - Edit IVI Scope Step Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/read-operation-edit-ivi-scope-step-dialog-box2.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/read-operation-edit-ivi-scope-step-dialog-box2.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Read Operation The Read operation initiates an acquisition and retrieves the measured value(s) from a previously started acquisition for the listed channels. Read initiates a new measurement on all channels. You can obtain data from multiple channels or different types of data from a single channel

### Read Operation - Edit IVI Scope Step Dialog Box

#### Read Operation

The Read operation initiates an acquisition and retrieves the measured value(s) from a previously started acquisition for the listed channels. Read initiates a new measurement on all channels. You can obtain data from multiple channels or different types of data from a single channel based on a single trigger condition.

The returned value is either the actual reading, in units the Waveform Type defines, or a value that indicates that an over-range condition occurred. When an over-range condition occurs, the reading parameter contains an IEEE-defined not a number (NaN) value. To test a value for the over-range condition, enable the
 Set Status if Over-Range
 control. If a timeout occurs before the Read operation completes, the Set Status on Timeout control determines the
 [step status](/csh?context=ts_tsfundamentals_step_status_values_table)
 .

The Edit IVI Scope Step dialog box for the Read operation contains the following tabs:

- Channels 
 —Specifies which channels to read, the type of data to retrieve, and where to store the data.
- Operation Settings 
 —Specifies where the dialog box saves and reloads the operation settings.

Parent topic:

Edit IVI Scope Step Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/read-operation-edit-ivi-scope-step-dialog-box3.html language=enus -->
## TOPIC 04029: Read Operation - Edit IVI Scope Step Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/read-operation-edit-ivi-scope-step-dialog-box3.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/read-operation-edit-ivi-scope-step-dialog-box3.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Read Operation Operation Settings Tab The Operation Settings tab for the Read operation contains the following channel-specific option: Settings Property/Variable —The name of the property or variable in which TestStand stores the settings when you click OK . Click the Load button to reload the sett

### Read Operation - Edit IVI Scope Step Dialog Box

#### Read Operation

#### Operation Settings Tab

The Operation Settings tab for the Read operation contains the following channel-specific option:

- Settings Property/Variable 
 —The name of the property or variable in which TestStand stores the settings when you click
 OK 
 . Click the
 Load 
 button to reload the settings from the specified property or variable location.

Parent topic:

Read Operation - Edit IVI Scope Step Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/record-operation-tab-edit-data-operation-dial.html language=enus -->
## TOPIC 04030: Record/Operation Tab - Edit Data Operation Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/record-operation-tab-edit-data-operation-dial.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/record-operation-tab-edit-data-operation-dial.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Record/Operation Tab The Record/Operation tab contains the following options: Statement Handle (Number) —The name of the Number variable or property that contains the SQL statement handle on which to operate. Operation —The operation the step performs on the selected record. Select one of the follow

### Record/Operation Tab - Edit Data Operation Dialog Box

#### Record/Operation Tab

The Record/Operation tab contains the following options:

- Statement Handle (Number) 
 —The name of the Number variable or property that contains the SQL statement handle on which to operate.
- Operation 
 —The operation the step performs on the selected record. Select one of the following options from the ring control:
  - Fetch – Fetch Record Only 
 —No operation is performed on this record.
  - Set – Update Values in Record 
 —Sets the values of the selected record. The Column List Source control contains the name of a variable or property that lists the assignments the step performs. Specify the assignments in the
 Column/Parameter Values 
 tab. You must issue a Put operation to update the selected record with any pending change to the values of the record.
  - Get – Retrieve Values from Record 
 —Gets the values from the selected record. The Column List Source control contains the name of a variable or property that lists the assignments the step performs. Specify the assignments in the
 Column/Parameter Values 
 tab.
  - Put – Write Record to Database 
 —Updates the selected record with any pending changes to the values of the record.
  - Delete – Remove Record from Database 
 —Deletes the selected record from the database.
  - Set and Put – Update Values and Write Record 
 —Equivalent to a Set operation that a Put operation follows.
  - Execute – Set Parameters and Execute 
 —Creates and sets the parameters for an SQL statement and executes the statement. You only use this operation with SQL statements that require parameters. Subsequent Execute operations do not recreate the parameters. Instead, they only set the parameter values before executing the statement. The Column List Source control contains the name of a variable or property that lists the parameters the step creates or sets. Specify the assignments in the
 Column/Parameter Values 
 tab.
 Note 
 To retrieve the values of output parameters, use a separate Data Operation step that specifies a Close operation.
  - Close – Close and Get Output Parameters 
 —Closes a previously executed SQL statement and retrieves the values of the specified parameters. Specify the assignments in the
 Column/Parameter Values 
 tab.
- Column List Source 
 —The name of the variable or property in which to store the list of mappings between SQL columns and TestStand variables or properties. The Column List Source variable or property must be a
 DatabaseColumnValue 
 array.
- Record to Operate On 
 —Specifies whether the step operates on the current record, fetches a new record, or creates a new record. Select one of the following options from the ring control:
  - New – Create New Record 
 —Creates a new record and operate on this new record.
  - Current – Use Current Record 
 —Operates on a record you previously fetched or created.
  - Next – Fetch Next Record 
 —Fetches the next record for the SQL statement.
  - Previous – Fetch Previous Record 
 —Fetches the previous record for the SQL statement.
  - Index – Fetch Record by Index 
 —Fetches the record with the index you specify in the Record Index control.
- Record Index 
 —A literal numeric value or a numeric expression TestStand evaluates at run time.

Note

Click the
 Expression Browse
 button to launch the
 [Expression Browser](expression-browser-dialog-box.html)
 dialog box for a control that contains a TestStand expression.

#### See Also

[Expression Browser dialog box](expression-browser-dialog-box.html)

Parent topic:

Edit Data Operation Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/record-prototypes.html language=enus -->
## TOPIC 04031: Record Prototypes

- bundle_id: `teststand-api-reference`
- source_path: `tsref/record-prototypes.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/record-prototypes.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: You can specify the record prototype in a CSV file you wish to read using a CsvFileInputRecordStream . The prototype defines the name and data type of each field or column in the CSV file. Specifying a prototype simplifies mapping columns in the CSV file to their corresponding variables in a TestSta

### Record Prototypes

You can specify the record prototype in a CSV file you wish to read using a
 [CsvFileInputRecordStream](csvfileinputrecordstream-and-csvfileoutputrec.html)
 . The prototype defines the name and data type of each field or column in the CSV file. Specifying a prototype simplifies mapping columns in the CSV file to their corresponding variables in a TestStand sequence. Specifying a prototype can also help prevent accidentally reading data from the wrong CSV file at run time.

A record prototype is specified by two rows in the CSV file. The first row defines the name of each field. The second row defines the data type of each field. The names must be legal TestStand property names.

The table below displays the supported data types.

| Data Type Specified in CSV File | Corresponding TestStand Data Type |
| --- | --- |
| String | String |
| Boolean | Boolean |
| Float64 | Number (Default Representation) |
| Int64 | Number (Signed 64-bit Integer Representation) |
| Unt64 | Number (Unsigned 64-bit Integer Representation) |
| Enum:<TYPE_NAME> | Enumeration with the specified type name. |

For example, if the first two lines defining a prototype in a CSV file are:

- Enabled,UnitId,Mode,Temperature,Voltage,ChangeCount,Color
- Boolean,UInt64,String,Float64,Float64,UInt64,Enum:Color

Then the first two rows of data in this file could be:

- TRUE,37,"Default",100.0,12.1,1,"Red"
- FALSE,38,"Sleep",93.7,6.0,2,"Blue"

You can add record prototype information to a CSV file manually. TestStand can also write prototype information for you in CSV files generated using the
 [New CSV Output Stream](new-csv-output-stream-step.html)
 step, or by using the
 [CsvFileOutputRecordStream.WriteRecordPrototype](../tsapiref/csvfileoutputrecordstream-writerecordprototyp.html)
 API method.

When reading CSV files, you can configure the
 [New CSV Input Record Stream](new-csv-input-stream-step.html)
 step to parse and verify the prototype at run time. Columns in the CSV file are automatically matched by name to the corresponding subproperties in the record container.

#### See Also

[CsvFileInputRecordStream](csvfileinputrecordstream-and-csvfileoutputrec.html)

[CsvFileOutputRecordStream.WriteRecordPrototype](../tsapiref/csvfileoutputrecordstream-writerecordprototyp.html)

[New CSV Input Stream step](new-csv-input-stream-step.html)

[New CSV Output Stream step](new-csv-output-stream-step.html)

Parent topic:

New CSV Input Stream Step

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/references-labview-vi-call-parameters.html language=enus -->
## TOPIC 04032: References - LabVIEW VI Call Parameters

- bundle_id: `teststand-api-reference`
- source_path: `tsref/references-labview-vi-call-parameters.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/references-labview-vi-call-parameters.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: References Most LabVIEW references are not usable inside of TestStand and are treated as unsigned longs. Additionally, LabVIEW references cannot be used across LabVIEW environments. For example, if you obtain a VI reference as an output after calling a VI using an ActiveX Automation server and try t

### References - LabVIEW VI Call Parameters

#### References

Most LabVIEW references are not usable inside of TestStand and are treated as unsigned longs. Additionally, LabVIEW references cannot be used across LabVIEW environments. For example, if you obtain a VI reference as an output after calling a VI using an ActiveX Automation server and try to pass this reference to a VI running in a run-time engine, this reference will be invalid in the run-time engine environment.

An ActiveX Automation reference from LabVIEW is stored in a TestStand object reference, and the TestStand
 [ActiveX/COM Adapter](/csh?context=ts_tsref_activexcom)
 can use the reference. When you specify an object reference property as the value of an ActiveX parameter to a VI, TestStand passes the value of the property. When you pass a reference to a TestStand object, the VI can use the property object reference in conjunction with the TestStand API to get and set the values of properties in the object, to add properties to the object, and so on.

A .NET reference from LabVIEW is stored in a TestStand object reference. The
 [.NET Adapter](/csh?context=ts_tsref_net)
 can use the .NET reference if the .NET objects derive from MarshalByRefObject or are serializable.

#### See Also

[LabVIEW Data Types in TestStand](/csh?context=ts_tsref_labview_data_types)

[Mapping Parameters](/csh?context=ts_tsref_parameters)

[Programming with the TestStand API in LabVIEW](/csh?context=ts_tsapiref_labview)

[Sharing .NET Objects Between LabVIEW and TestStand](/csh?context=ts_tsfundamentals_object_ref)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/references-labview-vi-call-parameters2.html language=enus -->
## TOPIC 04033: References - LabVIEW VI Call Parameters

- bundle_id: `teststand-api-reference`
- source_path: `tsref/references-labview-vi-call-parameters2.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/references-labview-vi-call-parameters2.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: References Most LabVIEW NXG references are not usable inside of TestStand and are treated as signed 64-bit integers. Additionally, LabVIEW NXG references cannot be used across LabVIEW NXG environments. For example, if you obtain a file reference as an output after calling a VI using the LabVIEW NXG

### References - LabVIEW VI Call Parameters

#### References

Most LabVIEW NXG references are not usable inside of TestStand and are treated as signed 64-bit integers. Additionally, LabVIEW NXG references cannot be used across LabVIEW NXG environments. For example, if you obtain a file reference as an output after calling a VI using the LabVIEW NXG Development environment and try to pass this reference to a VI running in a run-time engine, this reference will be invalid in the run-time engine environment.

An ActiveX Automation reference from LabVIEW NXG is stored in a TestStand object reference, and the TestStand
 [ActiveX/COM Adapter](/csh?context=ts_tsref_activexcom)
 can use the reference. When you specify an object reference property as the value of an ActiveX parameter to a VI, TestStand passes the value of the property. When you pass a reference to a TestStand object, the VI can use the property object reference in conjunction with the TestStand API to get and set the values of properties in the object, to add properties to the object, and so on.

#### See Also

[LabVIEW NXG Data Types in TestStand](labview-nxg-data-types-in-teststand.html)

[Mapping Parameters](/csh?context=ts_tsref_parameters)

Programming with the TestStand API in LabVIEW NXG

Parent topic:

LabVIEW NXG Data Types in TestStand

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/regular-expressions.html language=enus -->
## TOPIC 04034: Regular Expressions

- bundle_id: `teststand-api-reference`
- source_path: `tsref/regular-expressions.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/regular-expressions.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: TestStand supports a limited subset of regular expression syntax that other applications or operating systems support. A regular expression in TestStand can contain any of the following tokens: Token Explanation Example . (period) Match 1 character. a.t matches act and apt but not abort or at * (ast

### Regular Expressions

TestStand supports a limited subset of regular expression syntax that other applications or operating systems support. A regular expression in TestStand can contain any of the following tokens:

| Token | Explanation | Example |
| --- | --- | --- |
| . (period) | Match 1 character. | a.t matches act and apt but not abort or at |
| * (asterisk) | Match 0 or more occurrences of the preceding character or {expression}. | 0*1 matches 1 , 01 , 001 , etc. a.* matches act , apt , abort , and at |
| + (plus sign) | Match 1 or more occurrences of the preceding character or {expression}. | 0+1 matches 01 , 001 , 0001 , etc. {ab}+c matches abc, ababc, but not c |
| ? (question mark) | Match 0 or 1 occurrences of the preceding character or {expression}. | 0?1 matches 1 , 01 , but not 001 |
| \| (pipe) | Matches either the preceding or following character or {expression}. | a3\|4b matches a3b or a4b |
| ^ (caret) | Matches the beginning of a line. | ^int matches any line that begins with int |
| $ (dollar sign) | Matches the end of a line. | done$ matches any line that ends with done |
| {} (curly braces) | Groups characters or expressions . | {a3}\|{4b} matches a3 or 4b |
| [] (brackets) | Matches any one character or range listed within the brackets. | [a-z] matches every occurrence of lowercase letters [abc] matches every occurrence of a , b or c |
| ~ (tilde) | When appearing immediately after the left bracket, negates the contents of the set. | [~a-z] matches anything except lowercase letters [a-z~A-Z] matches all letters and the " ~ " character |
| \\t (backslash t) | Matches any tab character. | \\t3 matches every occurrence of a tab that a 3 follows |
| \\x (backslash x) | Matches any character specified in hex. | \\x2a matches every occurrence of the " * " character |
| \\ (backslash) | Used if any of the above characters themselves are to be included in the search. | \\-\\?\\\\ matches every occurrence of " - " that " ? " and " \\ " follow |

Parent topic:

Search For Tab - Find/Replace in Files Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/release-operation-semaphore-settings-edit-tab.html language=enus -->
## TOPIC 04035: Release Operation - Semaphore Settings Edit Tab

- bundle_id: `teststand-api-reference`
- source_path: `tsref/release-operation-semaphore-settings-edit-tab.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/release-operation-semaphore-settings-edit-tab.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Release Operation Use the Release operation when you want direct control over the count or when you use semaphores in a way that requires unmatched increments and decrements. When you enable the Auto Release option for the Acquire operation, do not explicitly release the semaphore using the Release

### Release Operation - Semaphore Settings Edit Tab

#### Release Operation

Use the Release operation when you want direct control over the count or when you use semaphores in a way that requires unmatched increments and decrements. When you enable the Auto Release option for the Acquire operation, do not explicitly release the semaphore using the Release operation. Enable the
 Release
 option on the left of the Semaphore Settings panel.

The Release operation contains the following option:

- Semaphore Name or Reference Expression 
 —The semaphore on which to perform the operation. You can specify the semaphore by name or by the object reference you receive when you create the semaphore using the Use Object Reference for the Semaphore Reference Lifetime option.

The Release operation immediately increments the count for the semaphore. If you perform the Acquire operation with the Auto Release option enabled, do not use the Release operation. Typically, you use the Release operation only on semaphores that require unmatched increments and decrements. For example, when you create a semaphore with an initial count of zero, all threads block when they perform an acquire. You can then perform Release operations to release the threads when you are ready.

Parent topic:

Semaphore Settings Edit Tab

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/release-operation-semaphore-step-configuratio.html language=enus -->
## TOPIC 04036: Release Operation - Semaphore Step Configuration Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/release-operation-semaphore-step-configuratio.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/release-operation-semaphore-step-configuratio.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Release Operation Use the Release operation when you want direct control over the count or when you use semaphores in a way that requires unmatched increments and decrements. When you enable the Auto Release option for the Acquire operation, do not explicitly release the semaphore using the Release

### Release Operation - Semaphore Step Configuration Dialog Box

#### Release Operation

Use the Release operation when you want direct control over the count or when you use semaphores in a way that requires unmatched increments and decrements. When you enable the Auto Release option for the Acquire operation, do not explicitly release the semaphore using the Release operation.

The Release operation contains the following option:

- Semaphore Name or Reference Expression 
 —The semaphore on which to perform the operation. You can specify the semaphore by name or by the object reference you receive when you create the semaphore using the Use Object Reference for the Semaphore Reference Lifetime option.

The Release operation immediately increments the count for the semaphore. If you perform the Acquire operation with the Auto Release option enabled, do not use the Release operation. Typically, you use the Release operation only on semaphores that require unmatched increments and decrements. For example, if you create a semaphore with an initial count of zero, all threads block when they perform an acquire. You can then perform Release operations to release the threads when you are ready.

Parent topic:

Semaphore Step Configuration Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/remote-computer-sequence-call-advanced-settin.html language=enus -->
## TOPIC 04037: Remote Computer - Sequence Call Advanced Settings Window

- bundle_id: `teststand-api-reference`
- source_path: `tsref/remote-computer-sequence-call-advanced-settin.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/remote-computer-sequence-call-advanced-settin.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Remote Computer The Sequence Call Advanced Settings window contains the following options when you select Use Remote Computer in the Execution Options control on the Module tab: Specify Expression for Host —Indicates whether you specify the remote host name through literal strings or through express

### Remote Computer - Sequence Call Advanced Settings Window

#### Remote Computer

The Sequence Call Advanced Settings window contains the following options when you select
 Use Remote Computer
 in the
 Execution Options
 control on the
 [Module](sequence-call-module-tab.html)
 tab:

- Specify Expression for Host 
 —Indicates whether you
 specify the remote host name 
 through literal strings or through
 expressions 
 TestStand evaluates at run time. When you disable this option, click the
 Browse Remote Host 
 button to select a remote host name on the network. When you enable this option, click the
 Expression Browse 
 button to build an expression.
- Remote Host 
 —The name of the remote host. This option applies only when you disable
 Specify Expression for Host 
 .
- Remote Host Expression 
 —The expression TestStand evaluates to acquire the name of the remote host. This option applies only when you enable
 Specify Expression for Host 
 .

Note

- For remote sequence calls, the sequence file pathnames are relative to the remote host.
- To make a remote call to 64-bit TestStand from 32-bit TestStand or vice versa, prefix the remote host name with
 64\\ 
 or
 32\\ 
 . You can use this functionality to implement mixed bitness tests where some sequences use 32-bit code modules and some sequences use 64-bit code modules. If you enable remote executions on the
 Remote Execution 
 tab of the
 Station Options 
 dialog box and specify
 localhost 
 as the computer name, remote executions can run on the same computer as the calling execution. For example, if you specify
 32\\localhost 
 from a sequence running in 64-bit TestStand, the sequence call runs the called sequence on the same computer using the 32-bit TestStand remote engine.

#### See Also

[Remote Execution in 32-bit TestStand and 64-bit TestStand](/csh?context=ts_tsfundamentals_64remoteexecution)

Parent topic:

Sequence Call Advanced Settings Window

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/remote-execution-settings-dialog-box.html language=enus -->
## TOPIC 04038: Remote Execution Settings Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/remote-execution-settings-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/remote-execution-settings-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Launch the Edit Sequence Call dialog box, select Run Sequence on a Remote Computer from the ring control in the Multithreading and Remote Execution section, and click Settings to launch the Remote Execution Settings dialog box. The Remote Execution Settings dialog box contains the following options:

### Remote Execution Settings Dialog Box

Launch the
 [Edit Sequence Call](edit-sequence-call-dialog-box.html)
 dialog box, select
 Run Sequence on a Remote Computer
 from the ring control in the Multithreading and Remote Execution section, and click
 Settings
 to launch the Remote Execution Settings dialog box.

The Remote Execution Settings dialog box contains the following options:

- Specify Expression for Host 
 —Indicates whether you specify the remote host name through literal strings or through
 expressions 
 TestStand evaluates at run time. When you disable this option, click the
 File Browse 
 button to select a remote host name on the network. When you enable this option, click the
 Expression Browse 
 button to build an expression.
- Remote Host 
 —The name of the remote host.
- Remote Host Expression 
 —The expression TestStand evaluates to acquire the name of the remote host.

Note

#### See Also

[Edit Sequence Call dialog box](edit-sequence-call-dialog-box.html)

[Configuring TestStand as a Server for Remote Execution](/csh?context=ts_tsfundamentals_remote_sequence_execution)

[Remote Execution in 32-bit TestStand and 64-bit TestStand](/csh?context=ts_tsfundamentals_64remoteexecution)

Parent topic:

Edit Sequence Call Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/remote-execution-tab-station-options-dialog-b.html language=enus -->
## TOPIC 04039: Remote Execution Tab - Station Options Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/remote-execution-tab-station-options-dialog-b.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/remote-execution-tab-station-options-dialog-b.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Remote Execution Tab The Remote Execution tab configures whether remote machines can run sequences on a computer . TestStand does not support remotely executing a sequence across different TestStand versions, for example, remotely executing a TestStand 2013 sequence from a computer running TestStand

### Remote Execution Tab - Station Options Dialog Box

#### Remote Execution Tab

The Remote Execution tab
 [configures whether remote machines can run sequences on a computer](/csh?context=ts_tsfundamentals_remote_sequence_execution)
 .

Note

(Windows 10/8.1/7) Windows launches a User Account Control (UAC) elevation prompt for you to manually resolve when you change the settings for remote execution.

The Remote Execution tab contains the following options:

- Allow Sequence Calls from Remote Computers to Run on this Computer 
 —When you enable this option, a remote computer can run a sequence on this station.
  - Allow All Users Access from Remote Computers 
 —When you enable this option, all users from remote computers can run sequences on this computer. When you enable this option, you do not have to configure access permissions for the remote TestStand server using the
 dcomcnfg 
 application.
 Note 
 When you change this setting, TestStand modifies the registry in the same manner as the
 dcomcnfg
 application.
- Show the System Tray Icon while the TestStand Remote Engine is Active on this Machine 
 —When you enable this option, TestStand displays a system tray icon for each instance of the TestStand Remote Engine running on a system. The tooltip and context menu contain status information for the remote engine.

Parent topic:

Station Options Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/remote-settings-window.html language=enus -->
## TOPIC 04040: Remote Settings Window

- bundle_id: `teststand-api-reference`
- source_path: `tsref/remote-settings-window.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/remote-settings-window.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Insert a Call Executable step into a sequence and click Remote Settings in the Configure Call Executable dialog box to launch the Remote Settings window in a TestStand User Interface . The Remote Settings window contains the following options: Run Executable on a Remote Computer —Enable this option

### Remote Settings Window

Insert a
 [Call Executable step](call-executable-step.html)
 into a sequence and click
 Remote Settings
 in the
 [Configure Call Executable](configure-call-executable-dialog-box.html)
 dialog box to launch the Remote Settings window in a
 [TestStand User Interface](teststand-user-interfaces.html)
 .

The Remote Settings window contains the following options:

- Run Executable on a Remote Computer 
 —Enable this option to allow the executable to run on a remote computer.
 Note 
 You must configure the
 [TestStand Remote EXE Server](teststand-remote-exe-server-dialog-box.html)
 to run executables on a remote computer before running the step.
- Remote Host 
 —The computer name or IP address of the remote computer on which to run the executable.
- Specify Host by Expression 
 —Enter an expression for the remote host field.
- Port Number 
 —The port number of the remote host.
- Password 
 —The password configured on the remote host.
- Password by Expression 
 —Enter an expression for the password field.

#### See Also

[Call Executable Step](call-executable-step.html)

[Configure Call Executable dialog box](configure-call-executable-dialog-box.html)

[TestStand Remote EXE Server](teststand-remote-exe-server-dialog-box.html)

Parent topic:

Configure Call Executable Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/remote-settings-window2.html language=enus -->
## TOPIC 04041: Remote Settings Window

- bundle_id: `teststand-api-reference`
- source_path: `tsref/remote-settings-window2.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/remote-settings-window2.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Insert a Call Executable step into a sequence and click Remote Settings on the Call Settings tab of the Step Settings pane to launch the Remote Settings window in the TestStand Sequence Editor . The Remote Settings window contains the following options: Run Executable on a Remote Computer —Enable th

### Remote Settings Window

Insert a
 [Call Executable step](call-executable-step.html)
 into a sequence and click
 Remote Settings
 on the
 [Call Settings](call-executable-edit-tabs.html)
 tab of the Step Settings pane to launch the Remote Settings window in the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 .

The Remote Settings window contains the following options:

- Run Executable on a Remote Computer 
 —Enable this option to allow the executable to run on a remote computer.
 Note 
 You must configure the
 [TestStand Remote EXE Server](teststand-remote-exe-server-dialog-box.html)
 to run executables on a remote computer before running the step.
- Remote Host 
 —The computer name or IP address of the remote computer on which to run the executable.
- Specify Host by Expression 
 —Enter an expression for the remote host field.
- Port Number 
 —The port number of the remote host.
- Password 
 —The password configured on the remote host.
- Password by Expression 
 —Enter an expression for the password field.

#### See Also

[Call Settings Tab](call-executable-edit-tabs.html)

[Call Executable Step](call-executable-step.html)

[TestStand Remote EXE Server](teststand-remote-exe-server-dialog-box.html)

Parent topic:

Call Settings Tab - Call Executable Edit Tabs

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/remove-thread-operation-batch-settings-edit-t.html language=enus -->
## TOPIC 04042: Remove Thread Operation - Batch Settings Edit Tab

- bundle_id: `teststand-api-reference`
- source_path: `tsref/remove-thread-operation-batch-settings-edit-t.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/remove-thread-operation-batch-settings-edit-t.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Remove Thread Operation Use the Remove Thread operation to remove a TestStand thread from a group of batch threads. Select the Remove Thread option on the left of the Batch Settings panel. The Remove Thread operation contains the following option: Object Reference to Thread —The thread you want to r

### Remove Thread Operation - Batch Settings Edit Tab

#### Remove Thread Operation

Use the Remove Thread operation to remove a TestStand thread from a group of batch threads. Select the
 Remove Thread
 option on the left of the Batch Settings panel.

The Remove Thread operation contains the following option:

- Object Reference to Thread 
 —The thread you want to remove from the batch.

Parent topic:

Batch Settings Edit Tab

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/remove-thread-operation-batch-specification-s.html language=enus -->
## TOPIC 04043: Remove Thread Operation - Batch Specification Step Configuration Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/remove-thread-operation-batch-specification-s.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/remove-thread-operation-batch-specification-s.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Remove Thread Operation Use the Remove Thread operation to remove a TestStand thread from a group of batch threads. The Remove Thread operation contains the following option: Object Reference to Thread —The thread you want to remove from the batch.

### Remove Thread Operation - Batch Specification Step Configuration Dialog Box

#### Remove Thread Operation

Use the Remove Thread operation to remove a TestStand thread from a group of batch threads.

The Remove Thread operation contains the following option:

- Object Reference to Thread 
 —The thread you want to remove from the batch.

Parent topic:

Batch Specification Step Configuration Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/rendezvous-operation-rendezvous-settings-edit.html language=enus -->
## TOPIC 04044: Rendezvous Operation - Rendezvous Settings Edit Tab

- bundle_id: `teststand-api-reference`
- source_path: `tsref/rendezvous-operation-rendezvous-settings-edit.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/rendezvous-operation-rendezvous-settings-edit.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Rendezvous Operation Enable the Rendezvous option on the left of the Rendezvous Settings panel. The Rendezvous operation contains the following options: Rendezvous Name or Reference Expression —The rendezvous on which to perform the operation. You can specify the rendezvous by name or by the object

### Rendezvous Operation - Rendezvous Settings Edit Tab

#### Rendezvous Operation

Enable the
 Rendezvous
 option on the left of the Rendezvous Settings panel.

The Rendezvous operation contains the following options:

- Rendezvous Name or Reference Expression 
 —The rendezvous on which to perform the operation. You can specify the rendezvous by name or by the object reference you receive when you create the rendezvous using the Use Object Reference for the Rendezvous Reference Lifetime option.
- Timeout Enabled, Timeout Expression, Timeout Causes Run-Time Error 
 —A timeout behavior when waiting to rendezvous with other threads. If a timeout occurs, the
 Step.Result.TimeoutOccurred 
 property is set to
 True 
 .

Parent topic:

Rendezvous Settings Edit Tab

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/rendezvous-operation-rendezvous-step-configur.html language=enus -->
## TOPIC 04045: Rendezvous Operation - Rendezvous Step Configuration Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/rendezvous-operation-rendezvous-step-configur.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/rendezvous-operation-rendezvous-step-configur.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Rendezvous Operation The Rendezvous operation contains the following options: Rendezvous Name or Reference Expression —The rendezvous on which to perform the operation. You can specify the rendezvous by name or by the object reference you receive when you create the rendezvous using the Use Object R

### Rendezvous Operation - Rendezvous Step Configuration Dialog Box

#### Rendezvous Operation

The Rendezvous operation contains the following options:

- Rendezvous Name or Reference Expression 
 —The rendezvous on which to perform the operation. You can specify the rendezvous by name or by the object reference you receive when you create the rendezvous using the Use Object Reference for the Rendezvous Reference Lifetime option.
- Timeout Enabled, Timeout Expression, Timeout Causes Run-Time Error 
 —A timeout behavior when waiting to rendezvous with other threads. If a timeout occurs, the
 Step.Result.TimeoutOccurred 
 property is set to
 True 
 .

Parent topic:

Rendezvous Step Configuration Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/rendezvous-settings-edit-tab.html language=enus -->
## TOPIC 04046: Rendezvous Settings Edit Tab

- bundle_id: `teststand-api-reference`
- source_path: `tsref/rendezvous-settings-edit-tab.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/rendezvous-settings-edit-tab.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: To display the Rendezvous Settings edit tab in the TestStand Sequence Editor , insert a Rendezvous step and select Edit Rendezvous Settings or Step Settings from the context menu. The following operations are available when you use the Rendezvous step type: Create —Creates a rendezvous reference. Re

### Rendezvous Settings Edit Tab

To display the Rendezvous Settings edit tab in the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 , insert a Rendezvous step and select
 Edit Rendezvous Settings
 or
 Step Settings
 from the context menu. The following operations are available when you use the Rendezvous step type:

- Create 
 —Creates a rendezvous reference.
- Rendezvous 
 —Wait for other step before proceeding.
- Get Status 
 —Obtains information about the current state of a rendezvous.

#### See Also

[Synchronization Step Types](synchronization-step-types.html)

Parent topic:

Rendezvous Step

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/rendezvous-step-configuration-dialog-box.html language=enus -->
## TOPIC 04047: Rendezvous Step Configuration Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/rendezvous-step-configuration-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/rendezvous-step-configuration-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Select Configure Rendezvous in the context menu for the step to launch the Rendezvous Step Configuration dialog box from a TestStand User Interface . You can also click Configure Rendezvous on the General tab of the Step Properties dialog box. In the Rendezvous Step Configuration dialog box, select

### Rendezvous Step Configuration Dialog Box

Select
 Configure Rendezvous
 in the context menu for the step to launch the Rendezvous Step Configuration dialog box from a
 [TestStand User Interface](teststand-user-interfaces.html)
 . You can also click
 Configure Rendezvous
 on the
 [General](general-tab-step-properties-dialog-box.html)
 tab of the
 [Step Properties](step-properties-dialog-box.html)
 dialog box. In the Rendezvous Step Configuration dialog box, select an operation for the step to perform.

The following operations are available when you use the Rendezvous step type:

- Create 
 —Creates a rendezvous reference.
- Rendezvous 
 —Wait for other step before proceeding.
- Get Status 
 —Obtains information about the current state of a rendezvous.

#### See Also

[Step Properties dialog box](step-properties-dialog-box.html)

[Synchronization Step Types](synchronization-step-types.html)

Parent topic:

Rendezvous Step

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/rendezvous-step.html language=enus -->
## TOPIC 04048: Rendezvous Step

- bundle_id: `teststand-api-reference`
- source_path: `tsref/rendezvous-step.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/rendezvous-step.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use a Rendezvous step to make threads wait for each other before proceeding past a location you specify. Each thread blocks as it performs the Rendezvous operation . When the number of blocked threads reaches the total number you specified when you created the rendezvous, the rendezvous unblocks all

### Rendezvous Step

Use a Rendezvous step to make threads wait for each other before proceeding past a location you specify. Each thread blocks as it performs the
 [Rendezvous operation](rendezvous-operation-rendezvous-step-configur.html)
 . When the number of blocked threads reaches the total number you specified when you created the rendezvous, the rendezvous unblocks all the waiting threads, and the threads resume execution.

#### Configuring the Step

Use the
 [Rendezvous Settings](rendezvous-settings-edit-tab.html)
 edit tab in the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 and the
 [Rendezvous Step Configuration](rendezvous-step-configuration-dialog-box.html)
 dialog box in a
 [TestStand User Interface](teststand-user-interfaces.html)
 to configure the Rendezvous step.

#### Step Properties

In addition to the
 [common custom properties](/csh?context=ts_tsfundamentals_custom_result_props)
 , the Rendezvous step type defines the following step properties:

- Step.Result.TimeoutOccurred 
 —Exists only when you configure the step for the Rendezvous operation. TestStand sets the value to
 True 
 when the Rendezvous operation times out.
 Note 
 If you configure the step to use the Rendezvous operation programmatically using the
 Step.Operation
 property, you must also create the
 Step.Result.TimeoutOccurred
 property using the
 newProperty(
 ) method for the step to execute successfully.
- Step.NameOrRefExpr 
 —Contains the Rendezvous
 Name 
 expression for the
 Create 
 operation and the Rendezvous Name or Reference expression for all other Rendezvous operations.
- Step.LifetimeRefExpr 
 —The object reference expression for the Rendezvous Reference
 Lifetime 
 when you set the lifetime to Use Object Reference.
- Step.TimeoutEnabled 
 —The
 Timeout 
 Enabled setting for the Rendezvous operation.
- Step.TimeoutExpr 
 —The Timeout expression, in seconds, for the Rendezvous operation.
- Step.ErrorOnTimeout 
 —The Timeout Causes Run-Time Error setting for the Rendezvous operation.
- Step.AlreadyExistsExpr 
 —Contains the Already Exists expression for the
 Create operation 
 or the Rendezvous Exists expression for the
 Get Status operation 
 .
- Step.RendezvousCountExpr 
 —The Number of Threads Per Rendezvous expression for the Create operation.
- Step.NumThreadsWaitingExpr 
 —The Number of Threads Waiting for Rendezvous expression for the
 Get Status 
 operation.
- Step.Operation 
 —A value that specifies the operation for the step to perform. The valid values are
 0 
 = Create,
 1 
 = Rendezvous, and
 2 
 = Get Status.
- Step.Lifetime 
 —A value that specifies the
 Lifetime 
 setting to use for the Create operation. The valid values are
 0 
 = Same as Sequence,
 1 
 = Same as Thread,
 2 
 = Use Object Reference, and
 3 
 = Same as Execution.
- Step.RendezvousCountOutExpr 
 —The Number of Threads Per Rendezvous expression for the Get Status operation.

#### See Also

[Controlling Multi-Threaded Execution Flow with Rendezvous and Semaphore Steps (Example)](/csh?context=ts_8185)

[Lifetime](/csh?context=ts_tsref_sync_objects_lifetime)

[Name](/csh?context=ts_tsref_sync_objects_name)

[Timeout](/csh?context=ts_tsref_sync_objects_timeout)

Parent topic:

Synchronization Step Types

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/replace-step-code-dialog-box.html language=enus -->
## TOPIC 04049: Replace Step Code Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/replace-step-code-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/replace-step-code-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: The C/C++ Module tab and the Edit C/C++ DLL Call dialog box launch the Replace Step Code dialog box when you click Create Code and when a function by the same name already exists inside the specified source code file. The Replace Step Code dialog box contains the following options: Source Code (< fi

### Replace Step Code Dialog Box

The
 [C/C++ Module](c-c-dll-module-tab.html)
 tab and the
 [Edit C/C++ DLL Call](edit-c-c-dll-call-dialog-box.html)
 dialog box launch the Replace Step Code dialog box when you click
 Create Code
 and when a function by the same name already exists inside the specified source code file.

The Replace Step Code dialog box contains the following options:

- Source Code (<
 filename
 >) 
 —Contains the source code for the specified file. By default, the dialog box automatically selects the existing function in the source file. You can also edit the source code within this control.
- Code to Insert 
 —The new code to replace the existing function in the source code file.
- Replace/Insert 
 —Replaces the selected text in the Source Code control with the code from the Code to Insert control. When no text is selected in the Source Code control, use this control to insert the code at the selected cursor location. You can also edit the source code after you replace or insert code within the source code control.
- Reset 
 —Cancels all edits performed in the Source Code control and reselects the original function previously located in the same file.

#### See Also

[C/C++ Module Tab](c-c-dll-module-tab.html)

[Edit C/C++ DLL Call dialog box](edit-c-c-dll-call-dialog-box.html)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/replace-text-in-all-paths-dialog-box.html language=enus -->
## TOPIC 04050: Replace Text in All Paths Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/replace-text-in-all-paths-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/replace-text-in-all-paths-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Launch the Edit Paths dialog box and click Replace to launch the Replace Text in All Paths dialog box. The Replace Text in All Paths dialog box contains the following options: Replace —The text to replace in all of the paths. With —The text to replace in the existing text. Case Sensitive —Specifies

### Replace Text in All Paths Dialog Box

Launch the
 [Edit Paths](edit-paths-dialog-box.html)
 dialog box and click
 Replace
 to launch the Replace Text in All Paths dialog box.

The Replace Text in All Paths dialog box contains the following options:

- Replace 
 —The text to replace in all of the paths.
- With 
 —The text to replace in the existing text.
- Case Sensitive 
 —Specifies whether the matching of characters is case-sensitive or case-insensitive.
- Replace All 
 —Performs the replace operation.

#### See Also

[Edit Paths dialog box](edit-paths-dialog-box.html)

[Edit Paths in Files dialog box](edit-paths-in-files-dialog-box.html)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/report-file-pathname-tab-report-options-dialo.html language=enus -->
## TOPIC 04051: Report File Pathname Tab - Report Options Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/report-file-pathname-tab-report-options-dialo.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/report-file-pathname-tab-report-options-dialo.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Report File Pathname Tab You can specify a fixed pathname to use for all report files or you can specify options the report generator uses to generate report file pathnames. The Report File Pathname tab of the Report Options dialog box contains a Generate Report File Path section, which provides a g

### Report File Pathname Tab - Report Options Dialog Box

#### Report File Pathname Tab

You can specify a fixed pathname to use for all report files or you can specify options the report generator uses to generate report file pathnames. The Report File Pathname tab of the Report Options dialog box contains a Generate Report File Path section, which provides a graphical indicator to illustrate how the options you select affect the names and contents of the report files.

The controls located on the Report File Pathname tab vary according to the process model you use. The Report File Pathname tab contains the following options:

- Specify Fixed Report File Path 
 —When you enable this option, TestStand automatically enables the
 Report File Path 
 control, in which you can specify a pathname that applies to all report files. You must specify an absolute pathname. Each report file the report generator creates overwrites the previous report file unless you enable the
 Append if File Already Exists 
 option on the
 Contents 
 tab.
- Generate Report File Path 
 —When you enable this option, you enable controls in which you can specify how the process model builds a pathname for report files.
 Note 
 Using NI DataFinder to index TestStand report files in directories to which TestStand writes report files can lead to report generation errors in
TestStand because of file access contention issues. Refer to the
 [Using NI DataFinder with TestStand](/csh?context=ts_tsreports_datafinder)
 topic for information about how to avoid these issues.
  - Type of Model 
 —Specify
 Sequential 
 ,
 Batch 
 , or
 Parallel 
 to determine which report options to display. If you
 create a custom process model 
 based on the default TestStand process model and you do not
 modify the default report settings in the process model sequence file 
 , the custom process model uses the report options defined by the process model type.
  - Use Temporary File 
 —Enables the control in which you set the pathname for a temporary report file. TestStand deletes the file when you exit the
 TestStand Sequence Editor 
 or a
 TestStand User Interface 
 . Enable this option when you do not want to save the test report.
  - File/Directory Options 
 —The directory and the file in which the report generator writes the report file. The following options are available in the ring control:
 
 Note 
 The following options are not available when you enable the Specify Report File Path by Expression option. You can
 [substitute functionality](/csh?context=ts_tsref_specifyreportfilepath_byexpression)
 for these options.
    - Client Sequence File Directory 
 —The directory that contains the client sequence file. For example, if you select Test UUTs from the
 Execute 
 menu when the
 d:\Tests\MySeqs\Seq2.seq 
 sequence file is active, the process model writes the report file in the
 d:\Tests\MySeqs 
 directory.
    - <TestStand Temp Directory>\Reports\ 
 —The
 TestStand Temp Directory 
 is a subdirectory named
 TestStand 
 in the directory the TEMP environment variable specifies, which by default is
 %USERPROFILE%\AppData\Local\Temp 
 on Microsoft Windows 10/8.1/7.
    - Specific Directory 
 —The directory you specify in the string control that appears under the ring control. You must enter an absolute path in the string control.
    - Specify Report File Path by Expression 
 —A TestStand expression that
 specifies the report file path 
 . Use the ring control to view a list of predefined macros, such as
 $(ClientFileName) 
 ,
 $(UUTStatus) 
 ,
 $(FileDate) 
 , and
 $(FileTime) 
 .
  - Base Name 
 —The base name for the report filename. Depending on the settings for other options, the report generator might add text to the base name. Do not include a file extension in this control.
  - Batch Base Name 
 —The base name for the batch report filename. Depending on the settings for other options, the report generator might add text to the batch base name. Do not include a file extension in this control. This control is available only when you use the Batch process model.
  - Prefix Sequence File Name to Report File Name 
 —Adds the base name of the client sequence file to the beginning of the name you specify in the Base Name control. For example, if the client filename is
 auto.seq 
 and you enter
 report 
 in the Base Name control, TestStand names an HTML version of the report
 auto_report.html 
 .
  - Add Time and Date to File Name 
 —Appends a string containing the current time and date in localized format to the base name of the report file. For example,
 auto_report.html 
 becomes
 auto_report[12 47 54 PM][6 24 99].html 
 . Select
 Append Time First 
 ,
 Append Date First 
 ,
 Time Only 
 , or
 Date Only 
 from the ring control to specify how the time and date append to the filename.
  - Force File Name to be Unique 
 —Appends a unique numeric value to the report filename if the file already exists. For example,
 auto_report.html 
 becomes
 auto_report_00002.html 
 .
  - Use Standard Extension for Report Format 
 —TestStand applies the file format extension that corresponds to the report format you specify on the Contents tab of this dialog box. Otherwise, you can enter a file format extension, such as
 doc 
 in the Extension control. Notice that you do not include the dot character in the entry.
- New UUT Report File for Each UUT 
 —Appends a string containing the current UUT serial number to the base name of the report file. For example,
 uut_report.html 
 becomes
 uut_report[SN000001].html 
 . This setting is not available when you select Store UUT Report in Batch Report File.
- New UUT Report File for Each Batch 
 —Appends a string containing the batch serial number to the base name of the report file. For example,
 uut_report.html 
 becomes
 uut_report[B10].html 
 . This setting is not available when you select Store UUT Report in Batch Report File.
- New UUT Report File for Each Test Socket 
 —Appends a string containing the test socket number to the base name of the report file. For example,
 auto_report.html 
 becomes
 uut_report[0].html 
 . This setting is not available when you select Store UUT Report in Batch Report File.
- New Batch Report File for Each Batch 
 —Appends a string containing the batch serial number to the base name of the report file. For example,
 batch_report.html 
 becomes
 batch_report[B10].html 
 .
- Store UUT Report in Batch Report File 
 —Stores UUT reports in the same file as the batch report. This control is available only when you use the Batch process model.

#### See Also

[Execute Menu](execute-menu.html)

[Specifying Report File Paths by Expression](/csh?context=ts_tsref_specifyreportfilepath_byexpression)

Parent topic:

Report Options Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/report-options-dialog-box.html language=enus -->
## TOPIC 04052: Report Options Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/report-options-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/report-options-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: In the Result Processing dialog box, click the icon in the Options column for the built-in reporting plug-in to launch the Report Options dialog box, in which you can customize the generation of report files. The settings you choose in the Report Options dialog box apply to all executions that use t

### Report Options Dialog Box

Result Processing

Note

- If you are using the equivalent legacy TestStand 2010 process models, select
 Configure»Report Options 
 to launch the Report Options dialog box.
- National Instruments recommends storing reports, offline result files, and databases locally instead of over a network for reliability and performance concerns. If you require a network storage solution, configure TestStand to store data locally and use a separate process or application to transfer files to and from the network.

The Report Options dialog box contains the following tabs:

- Contents 
 —General options for report generation, such as the type of data to include in the report, the report format, whether TestStand generates a report after testing a UUT, or whether TestStand generates a report concurrently with the execution.
- Report File Pathname 
 —Provides a graphical indicator to illustrate how options you select affect the names and contents of the report files. You can specify that all batch and UUT reports reside in the same file, that all reports reside in separate files, or one of several intermediate configurations.

#### See Also

[Result Processing dialog box](result-processing-dialog-box.html)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/report-pane-execution-window.html language=enus -->
## TOPIC 04053: Report Pane - Execution Window

- bundle_id: `teststand-api-reference`
- source_path: `tsref/report-pane-execution-window.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/report-pane-execution-window.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Report Pane By default, an execution only generates a report when you start the execution through an Execution entry point , such as Test UUTs or Single Pass. Select Configure»Result Processing to launch the Result Processing dialog box and then launch the Report Options dialog box for an instance o

### Report Pane - Execution Window

#### Report Pane

By default, an execution only generates a report when you start the execution through an
 [Execution entry point](/csh?context=ts_tsfundamentals_using_exe_entry_points)
 , such as Test UUTs or Single Pass. Select
 Configure»Result Processing
 to launch the
 [Result Processing](result-processing-dialog-box.html)
 dialog box and then launch the
 [Report Options](report-options-dialog-box.html)
 dialog box for an instance of the built-in reporting plug-in to set options that control report generation. The built-in reporting plug-in can generate reports in HTML, ASCII-text,
 [XML](/csh?context=ts_tsreports_xml)
 , and
 [ATML](/csh?context=ts_tsreports_atml)
 formats.

You can also use an external application to view reports in these or other formats by selecting
 View»Launch Report Viewer
 when an Execution window is active. Select
 Configure»External Viewers
 to launch the
 [Configure External Viewers](configure-external-viewers-dialog-box.html)
 dialog box and specify the external application TestStand launches to display a particular report format.

Note

- If you are using the equivalent legacy TestStand 2010 process models, select
 Configure»Report Options 
 to launch the Report Options dialog box and set options that control report generation.
- If the sequence generates a large number of results, it can take a substantial amount of time to load and display the report. If the report does not appear in an acceptable amount of time, select
 Configure»Result Processing 
 to launch the Result Processing dialog box and then launch the Report Options dialog box for the built-in reporting plug-in to specify a filter expression that reduces the number of results in the report. If you are using the equivalent legacy TestStand 2010 process models and the report does not appear in an acceptable amount of time, select
 Configure»Report Options 
 to specify a filter expression that reduces the number of results in the report. Another way to display a large report quickly is to change the report format to ASCII-text.

The Report pane contains the following options:

- Back 
 —Navigates to the previous page in the set of pages you have viewed. This button is available only for HTML and XML reports.
- Forward 
 —Navigates to the next page in the set of pages you have viewed. This button is available only for HTML and XML reports.
- Stop 
 —Cancels the current navigation or page display operation. This button is available only for HTML and XML reports.
- Refresh 
 —Reloads and redisplays the current page. This button is available only for HTML and XML reports.
- Home 
 —Navigates to the first page in the set of pages you have viewed. This button is available only for HTML and XML reports.
- Viewer 
 —Launches an external viewer application to display the current report.
- Print 
 —Prints the current report.The Print button is enabled only when Default Printer is configured on your machine.
- Active Report 
 —Lists the reports that reporting plug-in instances create. This control is available only when you create multiple reports.
- Open Report Location 
 —Opens File Explorer in the location where the currently displayed report is saved and selects the file.

#### See Also

[ATML](/csh?context=ts_tsreports_atml)

[Configure External Viewers dialog box](configure-external-viewers-dialog-box.html)

[Report Options dialog box](report-options-dialog-box.html)

[Result Processing dialog box](result-processing-dialog-box.html)

Parent topic:

Execution Window

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/report-tab.html language=enus -->
## TOPIC 04054: Report Tab

- bundle_id: `teststand-api-reference`
- source_path: `tsref/report-tab.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/report-tab.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: The Report tab in a TestStand User Interface displays the report for the selected execution. The user interface displays the Report tab when you view the list of open executions in the list bar control. By default, an execution only generates a report when you start the execution through an Executio

### Report Tab

The Report tab in a
 [TestStand User Interface](teststand-user-interfaces.html)
 displays the report for the selected execution. The user interface displays the Report tab when you view the list of open executions in the
 [list bar](list-bar.html)
 control.

By default, an execution only generates a report when you start the execution through an Execution entry point, such as Test UUTs or Single Pass. Select
 Configure»Result Processing
 to launch the
 [Result Processing](result-processing-dialog-box.html)
 dialog box and then launch the
 [Report Options](report-options-dialog-box.html)
 dialog box for the built-in reporting plug-in to set options that control report generation. The default process model can generate reports in HTML, ASCII-text,
 [XML](/csh?context=ts_tsreports_xml)
 , and
 [ATML](/csh?context=ts_tsreports_atml)
 formats.

Viewer

Configure»External Viewers

Configure External Viewers

Note

Configure»Report Options

The Report tab contains the following options:

- Back 
 —Navigates to the previous page in the set of pages you have viewed. This button is available only for HTML and XML reports.
- Forward 
 —Navigates to the next page in the set of pages you have viewed. This button is available only for HTML and XML reports.
- Stop 
 —Cancels the current navigation or page display operation. This button is available only for HTML and XML reports.
- Refresh 
 —Reloads and redisplays the current page. This button is available only for HTML and XML reports.
- Home 
 —Navigates to the first page in the set of pages you have viewed. This button is available only for HTML and XML reports.
- Viewer 
 —Launches an external viewer application to display the current report.
- Print 
 —Prints the current report.The Print button is enabled only when Default Printer is configured on your machine.
- Active Report 
 —Lists the reports that reporting plug-in instances create. This control is available only when you create multiple reports.
- Open Report Location 
 —Opens File Explorer in the location where the currently displayed report is saved and selects the file.

#### See Also

[ATML](/csh?context=ts_tsreports_atml)

[Configure External Viewers dialog box](configure-external-viewers-dialog-box.html)

[List Bar](list-bar.html)

[Report Options dialog box](report-options-dialog-box.html)

[Result Processing dialog box](result-processing-dialog-box.html)

Parent topic:

TestStand User Interface Menus and Tabs

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/requirements-panel-step-settings-pane.html language=enus -->
## TOPIC 04055: Requirements Panel - Step Settings Pane

- bundle_id: `teststand-api-reference`
- source_path: `tsref/requirements-panel-step-settings-pane.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/requirements-panel-step-settings-pane.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Requirements Panel The Requirements panel provides a mechanism for notating product and unit requirements the step covers. You can also notate requirements information in the Workspace Object Properties , Sequence File Properties , and Sequence Properties dialog boxes. The Requirements panel contain

### Requirements Panel - Step Settings Pane

#### Requirements Panel

The Requirements panel provides a mechanism for notating product and unit requirements the step covers. You can also notate requirements information in the
 [Workspace Object Properties](workspace-object-properties-dialog-box.html)
 ,
 [Sequence File Properties](sequence-file-properties-dialog-box.html)
 , and
 [Sequence Properties](sequence-properties-dialog-box.html)
 dialog boxes.

The Requirements panel contains the following option:

- Requirements List 
 —A list of strings where each string represents a single requirement.
 Note 
 External requirements management packages, such as NI Requirements Gateway, define the format of the values that represent a requirement. A requirements management software package can use the TestStand API to retrieve or specify requirement values from
 [Step](../tsapiref/step.html)
 objects.

#### See Also

[Sequence File Properties dialog box](sequence-file-properties-dialog-box.html)

[Sequence Properties dialog box](sequence-properties-dialog-box.html)

[Step](../tsapiref/step.html)

[Workspace Object Properties dialog box](workspace-object-properties-dialog-box.html)

Parent topic:

Properties Tab - Step Settings Pane

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/requirements-tab-step-properties-dialog-box.html language=enus -->
## TOPIC 04056: Requirements Tab - Step Properties Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/requirements-tab-step-properties-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/requirements-tab-step-properties-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Requirements Tab The Requirements tab provides a mechanism for notating product and unit requirements the step covers. You can also notate requirements information in the Workspace Object Properties , Sequence File Properties , and Sequence Properties dialog boxes. The Requirements tab contains the

### Requirements Tab - Step Properties Dialog Box

#### Requirements Tab

The Requirements tab provides a mechanism for notating product and unit requirements the step covers. You can also notate requirements information in the
 [Workspace Object Properties](workspace-object-properties-dialog-box.html)
 ,
 [Sequence File Properties](sequence-file-properties-dialog-box.html)
 , and
 [Sequence Properties](sequence-properties-dialog-box.html)
 dialog boxes.

The Requirements tab contains the following option:

- Requirements List 
 —A list of strings where each string represents a single requirement.
 Note 
 External requirements management packages, such as NI Requirements Gateway, define the format of the values that represent a requirement. A requirements management software package can use the TestStand API to retrieve or specify requirement values from
 [Step](../tsapiref/step.html)
 objects.

#### See Also

[Sequence File Properties dialog box](sequence-file-properties-dialog-box.html)

[Sequence Properties dialog box](sequence-properties-dialog-box.html)

[Step](../tsapiref/step.html)

[Workspace Object Properties dialog box](workspace-object-properties-dialog-box.html)

Parent topic:

Step Properties Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/reset-operation-edit-ivi-tools-step-dialog-bo.html language=enus -->
## TOPIC 04057: Reset Operation - Edit IVI Tools Step Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/reset-operation-edit-ivi-tools-step-dialog-bo.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/reset-operation-edit-ivi-tools-step-dialog-bo.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reset Operation The Reset operation places the instrument in a known state. For an IEEE 488.2 instrument, the Reset operation sends the command string "*RST" to the instrument. Reset also sends the default setup commands to the instrument to configure settings for the proper operation of the instrum

### Reset Operation - Edit IVI Tools Step Dialog Box

#### Reset Operation

The Reset operation places the instrument in a known state. For an IEEE 488.2 instrument, the Reset operation sends the command string
 "*RST"
 to the instrument. Reset also sends the default setup commands to the instrument to configure settings for the proper operation of the instrument driver.

Parent topic:

Edit IVI Tools Step Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/reset-output-protection-operation-edit-ivi-po.html language=enus -->
## TOPIC 04058: Reset Output Protection Operation - Edit IVI Power Supply Step Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/reset-output-protection-operation-edit-ivi-po.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/reset-output-protection-operation-edit-ivi-po.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reset Output Protection Operation Resets the output protection of the power supply on a specific channel after an overvoltage or overcurrent condition occurs. An overvoltage condition occurs when the output voltage is equal to or greater than the value of the OVP Limit setting and the OVP Enabled se

### Reset Output Protection Operation - Edit IVI Power Supply Step Dialog Box

#### Reset Output Protection Operation

Resets the output protection of the power supply on a specific channel after an overvoltage or overcurrent condition occurs. An overvoltage condition occurs when the output voltage is equal to or greater than the value of the OVP Limit setting and the OVP Enabled setting is set to
 True
 . An overcurrent condition occurs when the output current is equal to or greater than the value of the Current Limit setting and the Current Limit Behavior setting is set to Current Trip.

When either an overvoltage condition or an overcurrent condition occurs, the output protection of the power supply disables the output. You can use this operation to reset the output protection after an overvoltage or overcurrent condition occurs. Once the output protection is reset, the power supply resumes generating a power signal.

You can use Query Output State in the Get Information operation to determine whether the power supply is in an overvoltage or overcurrent state.

Note

The Reset Output Protection operation contains the following option:

- Channel Name 
 —The name of the channel on which to operate. The channel name must be a valid virtual channel name as the IVI configuration for the logical name being used defines.

Parent topic:

Edit IVI Power Supply Step Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/resolve-differences-between-function-call-and.html language=enus -->
## TOPIC 04059: Resolve Differences between Function Call and Prototype Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/resolve-differences-between-function-call-and.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/resolve-differences-between-function-call-and.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: TestStand launches the Resolve Differences between Function Call and Prototype dialog box when you click Accept on the C/C++ Module tab, the LabWindows/CVI Module tab, the Module tab of the Edit LabWindows/CVI Module Call dialog box, or the Module tab of the Edit C/C++ DLL Call dialog box and the nu

### Resolve Differences between Function Call and Prototype Dialog Box

TestStand launches the Resolve Differences between Function Call and Prototype dialog box when you click
 Accept
 on the
 [C/C++ Module](c-c-dll-module-tab.html)
 tab, the
 [LabWindows/CVI Module](labwindows-cvi-module-tab.html)
 tab, the Module tab of the
 [Edit LabWindows/CVI Module Call](edit-labwindows-cvi-module-call-dialog-box.html)
 dialog box, or the Module tab of the
 [Edit C/C++ DLL Call](edit-c-c-dll-call-dialog-box.html)
 dialog box and the number of parameters specified in the Function Call control does not match the number of parameters in the Parameters Table control.

The Resolve Differences between Function Call and Prototype dialog box contains the following options:

- Add parameter(s) to the function prototype 
 —TestStand adds the additional parameters in the function prototype to the Parameters list.
- Delete the last parameter(s) from the function prototype 
 —TestStand deletes any additional parameters in the Parameters list that are not specified in the function prototype.
- Discard the last argument(s) to the function 
 —TestStand ignores any extra arguments defined in the function prototype that have no equivalent parameter in the Parameters list.
- Keep existing arguments 
 —TestStand does not discard the argument values for any additional parameters in the Parameters list that are not specified in the function prototype.

#### See Also

[C/C++ Module Tab](c-c-dll-module-tab.html)

[Edit C/C++ DLL Call dialog box](edit-c-c-dll-call-dialog-box.html)

[Edit LabWindows/CVI Module Call dialog box](edit-labwindows-cvi-module-call-dialog-box.html)

[LabWindows/CVI Module Tab](labwindows-cvi-module-tab.html)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/resolve-file-saving-conflict-dialog-box.html language=enus -->
## TOPIC 04060: Resolve File Saving Conflict Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/resolve-file-saving-conflict-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/resolve-file-saving-conflict-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: TestStand launches the Resolve File Saving Conflict dialog box when a TestStand application attempts to save the in-memory content of a file to disk and another application modified the original file on disk. The Resolve File Saving Conflict dialog box contains the following options: Save changes an

### Resolve File Saving Conflict Dialog Box

TestStand launches the Resolve File Saving Conflict dialog box when a TestStand application attempts to save the in-memory content of a file to disk and another application modified the original file on disk.

The Resolve File Saving Conflict dialog box contains the following options:

- Save changes and overwrite <
 filename
 > 
 —TestStand ignores the changes to the file on disk and to replace the file on disk with the contents of the in-memory copy of the file.
- Do not save changes and preserve <
 filename
 > 
 —TestStand does not save the in-memory changes to the file to disk. The file is not automatically reloaded.

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/result-processing-dialog-box.html language=enus -->
## TOPIC 04061: Result Processing Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/result-processing-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/result-processing-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Select Configure»Result Processing to launch the default Result Processing dialog box, in which you enable or disable the installed built-in and custom result processing plug-ins in the active result processing configuration and also configure how the plug-ins process test results. Use the built-in

### Result Processing Dialog Box

Select
 Configure»Result Processing
 to launch the default Result Processing dialog box, in which you enable or disable the installed built-in and custom result processing plug-ins in the active result processing configuration and also configure how the plug-ins process test results.

Use the built-in reporting, database, and offline results plug-ins to generate reports, log data to databases, and store results in compact offline result files for processing later, respectively.

Enable the
 Show More Options
 control in the Result Processing dialog box to display additional options to insert or delete instances of result processing plug-ins, change the order in which TestStand invokes the plug-ins, and specify whether TestStand invokes the plug-ins serially or in parallel using separate threads.

In the expanded Result Processing dialog box, you can also create and manage result processing configurations. The <Default for Inline Processing> configuration is the default active configuration for processing results at run time. The <Default for Offline Processing> configuration is the default configuration the
 [TestStand Offline Results Processing Utility](/csh?context=ts_tsref_offline_processing_utility)
 uses.

You can also
 [create custom result processing model plug-ins](advanced-result-processing-settings-dialog-bo.html)
 .

The expanded Result Processing dialog box includes the following options:

- Active Configuration 
 —Select the active result processing configuration TestStand uses to process results inline at run time. Select
 Manage Configurations 
 to launch the
 Manage Result Processing Configurations 
 dialog box, in which you create or delete result processing configurations.
- Plug-in Instance Table 
 —Displays the result processing plug-in instances and options in the active configuration. You can insert multiple instances of the same plug-in with various configuration options to accomplish specific tasks, such as creating multiple reports with different formats or logging data to multiple databases. The table includes the following columns:
  - Output 
 —Indicates the type of output the result processing plug-in creates. Use descriptive names.
  - Enabled 
 —Specifies whether TestStand invokes the plug-in instance when processing results.
  - Display 
 —Appears only when the active configuration includes a plug-in instance configured to display a report in the TestStand
 Report 
 pane. Of the built-in model plug-ins, only the reporting plug-in displays a report. When you include multiple instances of the built-in reporting plug-in, use the Display column to specify which plug-in instance report to display in the Report pane. At run time, you can use the
 Active Report 
 control on the Report pane toolbar to view reports from other plug-in instances. Disable the checkbox in the Display column of all reporting plug-in instances to create reports but not display them in the Report pane.
  - Options 
 —Includes a summary of the most important option settings for the plug-in instance. Click the icon in the Options column for each built-in plug-in to launch the Options dialog box, in which you configure options specific to the plug-in.
  - New Thread 
 —Use the following options to specify how TestStand invokes the plug-in:
    - Yes 
 —Invokes the plug-in in a new thread and processes results in parallel with other plug-ins and with the testing of subsequent UUTs.
    - No 
 —Waits for the plug-in to complete its processing before invoking the next plug-in listed in the Plug-in Instance Table, including plug-ins configured to use a new thread.
    - Yes, Complete before next UUT 
 —Invokes the plug-in in a new thread and waits for the plug-in to complete before testing begins on the next UUT.
- Insert New Plug-in Instance 
 —Select from a list of installed result processing plug-ins to insert a new instance of the plug-in in the Plug-in Instance Table.
- Cut 
 —Removes the selected plug-in instance and places it on the clipboard.
- Copy 
 —Copies the selected plug-in instance to the clipboard.
- Paste 
 —Inserts the plug-in instance from the clipboard into the Plug-in Instance Table.
- Move Up 
 —Moves the selected plug-in instance up one row in the Plug-in Instance Table.
- Move Down 
 —Moves the selected plug-in instance down one row in the Plug-in Instance Table.
- Reset to Defaults 
 —Replaces the contents of the current active configuration with one instance of each installed result processing plug-in configured to the default state and prompts you to define the configuration for inline or offline processing. If you select offline processing, TestStand does not insert an instance of the offline results plug-in.
- Advanced 
 —Launches the
 Advanced Result Processing Settings 
 dialog box, in which you configure on-the-fly result processing options that apply to all instances of plug-ins in all configurations, such as specifying and managing the processing interval and specifying the maximum number of results.
- Show More Options 
 —Enable this control to display additional options to insert or delete instances of result processing plug-ins, change the order in which TestStand invokes the plug-ins, and specify whether TestStand invokes the plug-ins serially or in parallel using separate threads. Disable this control to hide most of the controls in the Result Processing dialog box and limit editing to only the plug-in instances that exist in the active configuration.

#### See Also

[Advanced Result Processing Settings dialog box](advanced-result-processing-settings-dialog-bo.html)

[Manage Result Processing Configurations dialog box](manage-result-processing-configurations-dialo.html)

[Process Model Plug-In Architecture](/csh?context=ts_tsfundamentals_process_model_plugin_arch)

[TestStand Offline Results Processing Utility](/csh?context=ts_tsref_offline_processing_utility)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/revision-query-operation-edit-ivi-tools-step.html language=enus -->
## TOPIC 04062: Revision Query Operation - Edit IVI Tools Step Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/revision-query-operation-edit-ivi-tools-step.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/revision-query-operation-edit-ivi-tools-step.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Revision Query Operation The Revision Query operation queries the instrument driver and instrument for current revisions. The operation returns the revision of the instrument driver and firmware for the instrument you are using. The Revision Query operation contains the following options: Driver Rev

### Revision Query Operation - Edit IVI Tools Step Dialog Box

#### Revision Query Operation

The Revision Query operation queries the instrument driver and instrument for current revisions. The operation returns the revision of the instrument driver and firmware for the instrument you are using.

The Revision Query operation contains the following options:

- Driver Revision 
 —A variable or property to which the step assigns the revision information for the instrument driver.
- Instrument Revision 
 —A variable or property to which the step assigns the revision information for the instrument firmware.

Parent topic:

Edit IVI Tools Step Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/ring-control-parameters-labview-vi-call-param.html language=enus -->
## TOPIC 04063: Ring Control Parameters - LabVIEW VI Call Parameters

- bundle_id: `teststand-api-reference`
- source_path: `tsref/ring-control-parameters-labview-vi-call-param.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/ring-control-parameters-labview-vi-call-param.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Ring Control Parameters When you configure calls to VIs that use ring controls as parameters and you are using LabVIEW 2012 or later, the Value column of the VI Parameter Table on the LabVIEW Module tab shows a ring control for LabVIEW ring control input parameters. The ring control contains the ite

### Ring Control Parameters - LabVIEW VI Call Parameters

#### Ring Control Parameters

When you configure calls to VIs that use ring controls as parameters and you are using LabVIEW 2012 or later, the Value column of the VI Parameter Table on the
 [LabVIEW Module](labview-module-tab.html)
 tab shows a ring control for LabVIEW ring control input parameters. The ring control contains the items in the LabVIEW ring control.

In TestStand 2016 and later, LabVIEW ring controls are
 [enumeration parameters](enumeration-parameters-labview-vi-call-parame.html)
 . In addition to selecting a value from the Ring control elements or passing in a Number variable, you can also specify a TestStand Enum variable as the value of a Ring control parameter. For more information about the behavior of enumeration parameters with respect to Ring controls, refer to the
 [Enumeration Parameters](enumeration-parameters-labview-vi-call-parame.html)
 help topic.

Note

At edit time, TestStand stores the numeric value and the string label value of the ring control parameter value you select.

When you pass a ring control value as a parameter to TestStand at run time, TestStand stores only the numeric value. In addition, for input parameters at run time, TestStand passes the numeric value to LabVIEW without checking whether the numeric value is within range. This behavior is similar to LabVIEW.

TestStand supports
 [all numeric representations](/csh?context=ts_tsref_labview_data_types)
 of a ring control parameter.

When you reload a VI prototype and you specify an expression for the ring control parameter, TestStand always retains the expression.

The following table describes how TestStand updates ring control parameter values in a similar way to LabVIEW when you reload a VI prototype and you do not specify an expression for the ring control parameter.

| Change You Make to LabVIEW Ring Control Values | Effect You See in TestStand VI Parameter Table | Effect You See in TestStand Step Properties |
| --- | --- | --- |
| You delete the numeric value currently stored in the step property. | TestStand displays the numeric value because it cannot find a corresponding string label. | TestStand always retains the numeric value. |
| You update the string label but retain the numeric value currently stored in the step property. | TestStand retains the numeric value and updates the corresponding string label to match the numeric value. | TestStand always retains the numeric value and updates the corresponding string label to match the numeric value. |

#### See Also

[LabVIEW Data Types in TestStand](/csh?context=ts_tsref_labview_data_types)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/rule-settings-dialog-box.html language=enus -->
## TOPIC 04064: Rule Settings Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/rule-settings-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/rule-settings-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Click the Settings button located to the right of the rule name, if available, in the Rule column on the Rules pane of the Current Sequence Analyzer Project window or on the Rules tab of the stand-alone TestStand Sequence Analyzer application to launch the Rule Settings dialog box. The list of setti

### Rule Settings Dialog Box

Click the
 Settings
 button located to the right of the rule name, if available, in the Rule column on the
 [Rules](rules-pane-current-sequence-analyzer-project.html)
 pane of the
 [Current Sequence Analyzer Project](current-sequence-analyzer-project-window.html)
 window or on the
 [Rules](rules-tab-teststand-sequence-analyzer-applica.html)
 tab of the stand-alone
 [TestStand Sequence Analyzer application](teststand-sequence-analyzer-application.html)
 to launch the Rule Settings dialog box.

The list of settings and values in the Rule Settings dialog box varies according to the settings for the rule. For example, for the built-in Count Sequences statistics rule, you can set the rule to count the number of sequences only in the sequence file or for the entire analysis.

#### See Also

[Current Sequence Analyzer Project Window](current-sequence-analyzer-project-window.html)

[TestStand Sequence Analyzer Application](teststand-sequence-analyzer-application.html)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/rules-pane-current-sequence-analyzer-project.html language=enus -->
## TOPIC 04065: Rules Pane - Current Sequence Analyzer Project Window

- bundle_id: `teststand-api-reference`
- source_path: `tsref/rules-pane-current-sequence-analyzer-project.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/rules-pane-current-sequence-analyzer-project.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Rules Pane Use the Rules pane to enable, disable, and configure rules to use for analysis in the current TestStand Sequence Analyzer project. The Rules pane contains the following columns: Rule —List of all the rules available on the computer, grouped by category. Place a checkmark in the option nex

### Rules Pane - Current Sequence Analyzer Project Window

#### Rules Pane

Use the Rules pane to enable, disable, and configure rules to use for analysis in the current TestStand Sequence Analyzer project. The Rules pane contains the following columns:

- Rule 
 —List of all the rules available on the computer, grouped by category. Place a checkmark in the option next to the rule name or category to enable or disable the rule or entire category for analysis. Click the
 Settings 
 button located to the right of the rule name, if available, to launch the
 Rule Settings 
 dialog box or a custom dialog box, in which you can change rule settings.
 Note 
 You cannot disable or delete the
 [built-in rules](/csh?context=ts_tsref_sequence_analyzer_rules_descriptions)
 in the Analysis Errors category.
- Severity 
 —Severity level of the rule. Use this ring control to change the severity level. When you change a value that is not the rule default, the Severity value changes to bold text.
- Description 
 —Detailed description of the rule.

#### See Also

[Rule Settings dialog box](rule-settings-dialog-box.html)

[TestStand Sequence Analyzer](/csh?context=ts_tsref_sequence_analyzer_overview)

[TestStand Sequence Analyzer Rules Descriptions](/csh?context=ts_tsref_sequence_analyzer_rules_descriptions)

Parent topic:

Current Sequence Analyzer Project Window

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/rules-tab-configure-sequence-analyzer-availab.html language=enus -->
## TOPIC 04066: Rules Tab - Configure Sequence Analyzer Available Rules Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/rules-tab-configure-sequence-analyzer-availab.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/rules-tab-configure-sequence-analyzer-availab.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Rules Tab Use the Rules tab to add, remove, and edit custom TestStand Sequence Analyzer rules on the computer. The Rules tab contains the following sections: BuiltinRules.tsarules —Shows the ID, name, category, severity, and description of the built-in rules that National Instruments provides in the

### Rules Tab - Configure Sequence Analyzer Available Rules Dialog Box

#### Rules Tab

Use the Rules tab to add, remove, and edit custom TestStand Sequence Analyzer
 [rules](/csh?context=ts_tsref_sa_creating_custom_rules)
 on the computer.

The Rules tab contains the following sections:

- BuiltinRules.tsarules 
 —Shows the ID, name, category, severity, and description of the
 built-in rules 
 that National Instruments provides in the
 [<TestStand>](/csh?context=ts_tsfundamentals_directories)
 \Components\Analyzer\BuiltinRules.tsarules 
 file.
 Note 
 You cannot modify the built-in rules.
- CustomRules.tsarules 
 —Shows the ID, name, category, severity, and description of the custom rules on the computer. TestStand stores custom rules in the
 [<TestStand Application Data>](/csh?context=ts_tsfundamentals_directories)
 \Cfg\CustomRules.tsarules 
 file.

Right-click a rule and select
 Insert Rule
 from the context menu to create a custom rule. You can also click the
 New Rule
 button located to the right of the
 <Insert New Rule>
 item in the Rule ID column to launch the Edit Rule dialog box.

Double-click a rule, right-click a rule and select
 Edit Rule
 from the context menu, or click the
 Edit Rule
 button located to the right of the Rule ID column to launch the
 [Edit Rule](edit-rule-dialog-box.html)
 dialog box, in which you can view general and advanced settings for built-in rules and create and edit general and advanced settings for custom rules. You can also edit the general settings of custom rules directly on the Rules tab.

You can drag and drop custom rules to change the order of the list. The order of the rules in this list does not affect the order of the rules on the
 [Rules](rules-pane-current-sequence-analyzer-project.html)
 pane of the
 [Current Sequence Analyzer Project](current-sequence-analyzer-project-window.html)
 window in the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 or on the
 [Rules](rules-tab-teststand-sequence-analyzer-applica.html)
 tab of the stand-alone
 [TestStand Sequence Analyzer application](teststand-sequence-analyzer-application.html)
 , which always shows the rules in alphabetical order. You can cut, copy, paste, and delete custom rules.

#### See Also

[Current Sequence Analyzer Project Window](current-sequence-analyzer-project-window.html)

[Creating Custom Rules](/csh?context=ts_tsref_sa_creating_custom_rules)

[Edit Rule dialog box](edit-rule-dialog-box.html)

[TestStand Sequence Analyzer Application](teststand-sequence-analyzer-application.html)

[TestStand Sequence Analyzer Rules Descriptions](/csh?context=ts_tsref_sequence_analyzer_rules_descriptions)

Parent topic:

Configure Sequence Analyzer Available Rules Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/rules-tab-teststand-sequence-analyzer-applica.html language=enus -->
## TOPIC 04067: Rules Tab - TestStand Sequence Analyzer Application

- bundle_id: `teststand-api-reference`
- source_path: `tsref/rules-tab-teststand-sequence-analyzer-applica.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/rules-tab-teststand-sequence-analyzer-applica.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Rules Tab Use the Rules tab to enable, disable, and configure rules to use for analysis in the current TestStand Sequence Analyzer project. The Rules tab contains the following columns: Rule —List of all the rules available on the computer, grouped by category. Place a checkmark in the option next t

### Rules Tab - TestStand Sequence Analyzer Application

#### Rules Tab

Use the Rules tab to enable, disable, and configure rules to use for analysis in the current TestStand Sequence Analyzer project. The Rules tab contains the following columns:

- Rule 
 —List of all the rules available on the computer, grouped by category. Place a checkmark in the option next to the rule name or category to enable or disable the rule or entire category for analysis. Click the
 Settings 
 button located to the right of the rule name, if available, to launch the
 Rule Settings 
 dialog box or a custom dialog box, in which you can change rule settings.
 Note 
 You cannot disable or delete the
 [built-in rules](/csh?context=ts_tsref_sequence_analyzer_rules_descriptions)
 in the Analysis Errors category.
- Severity 
 —Severity level of the rule. Use this ring control to change the severity level. When you change a value that is not the rule default, the Severity value changes to bold text.
- Description 
 —Detailed description of the rule.

#### See Also

[Rule Settings dialog box](rule-settings-dialog-box.html)

[TestStand Sequence Analyzer Rules Descriptions](/csh?context=ts_tsref_sequence_analyzer_rules_descriptions)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/run-lv-nxg-vi-asynchronously-edit-tab.html language=enus -->
## TOPIC 04068: Run LV NXG VI Asynchronously Edit Tab

- bundle_id: `teststand-api-reference`
- source_path: `tsref/run-lv-nxg-vi-asynchronously-edit-tab.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/run-lv-nxg-vi-asynchronously-edit-tab.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Insert a Run VI Asynchronously step and select Edit Run LV NXG VI Asynchronously or Step Settings from the context menu to display the Run LV NXG VI Asynchronously edit tab in the TestStand Sequence Editor . Use the Run LV NXG VI Asynchronously edit tab to specify the VI to run. When TestStand execu

### Run LV NXG VI Asynchronously Edit Tab

Insert a Run VI Asynchronously step and select
 Edit Run LV NXG VI Asynchronously
 or
 Step Settings
 from the context menu to display the Run LV NXG VI Asynchronously edit tab in the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 .

Use the Run LV NXG VI Asynchronously edit tab to specify the VI to run. When TestStand executes the Run LV NXG VI Asynchronously step, TestStand launches a dynamically-generated sequence in a new thread which executes the VI.

The Run LV NXG VI Asynchronously edit tab contains the following options:

- Specified VI 
 —The name of the project/GLL and VI to run in the step. Click
 Specify VI 
 to launch the
 Edit LabVIEW NXG VI Call 
 dialog box, in which you can specify the prototype and parameters of the VI. When you select multiple Run LV NXG VI Asynchronously steps, TestStand dims the Specify VI button.
- Store an Object Reference to the New Thread in (optional) 
 —The location to store the reference to the new
 Thread 
 object the step creates. You can use this reference in subsequent calls to the TestStand API. You can also use this reference in a
 Wait 
 step to wait for the thread to complete.
- Automatically Wait for the Thread to Complete at the End of the Current Sequence 
 —Specifies whether the calling sequence does not complete execution until the thread this step launches completes execution.
- Context to Pass as ThisContext for VI Arguments 
 —The context the step uses when you pass
 ThisContext 
 as a parameter. Select from the following options:
  - Use Context of Calling Thread (Accessing the context of the calling thread requires additional synchronization for thread safety.) 
 —When you specify
 ThisContext 
 as an argument for a parameter of a VI, TestStand uses the context of the calling thread. If you enable this option, also enable the
 Automatically Wait for the Thread to Complete at the End of the Current Sequence 
 option to ensure that TestStand does not clean up the context of the calling thread before the asynchronous VI completes.
 Notice 
 Using the context of the calling thread in the newly created thread can lead to race conditions and crashes because the calling thread continues to execute in parallel, and TestStand might create or remove variables in the context of the calling thread while the sequence is running or when the sequence completes. TestStand does not automatically
ensure thread safety for structural changes to variables, such as adding or removing subproperties.
  - Use Context of New Thread (National Instruments recommends using this option if you do not need direct access to data from the calling sequence.) 
 —When you specify
 ThisContext 
 as an argument for a parameter of a VI, TestStand uses the context of the new thread. If you need to access variables from the context of the calling thread, pass the variables as parameters to the VI instead.

Note

#### See Also

[LabVIEW NXG Utility Step Types](labview-utility-step-types2.html)

[Step Properties dialog box](step-properties-dialog-box.html)

[Wait Step](wait-step.html)

Parent topic:

Run VI Asynchronously Step - LabVIEW Utility Step Types

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/run-lv-nxg-vi-asynchronously-step-configurati.html language=enus -->
## TOPIC 04069: Run LV NXG VI Asynchronously Step Configuration Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/run-lv-nxg-vi-asynchronously-step-configurati.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/run-lv-nxg-vi-asynchronously-step-configurati.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Select Configure Run LV NXG VI Asynchronously in the context menu for the step to launch the Run LV NXG VI Asynchronously Step Configuration dialog box from a TestStand User Interface . You can also click Configure Run LV NXG VI Asynchronously on the General tab of the Step Properties dialog box. Wh

### Run LV NXG VI Asynchronously Step Configuration Dialog Box

Select
 Configure Run LV NXG VI Asynchronously
 in the context menu for the step to launch the Run LV NXG VI Asynchronously Step Configuration dialog box from a
 [TestStand User Interface](teststand-user-interfaces.html)
 . You can also click
 Configure Run LV NXG VI Asynchronously
 on the
 [General](step-properties-dialog-box.html)
 tab of the
 [Step Properties](step-properties-dialog-box.html)
 dialog box.

When TestStand executes the Run LV NXG VI Asynchronously step, TestStand launches a dynamically-generated sequence in a new thread which executes the VI.

The Run LV NXG VI Asynchronously Step Configuration dialog box contains the following options:

- Store an Object Reference to the New Thread in (optional) 
 —The location to store the reference to the new Thread object the step creates. You can use this reference in subsequent calls to the TestStand API. You can also use this reference in a
 Wait 
 step to wait for the thread to complete.
- Automatically Wait for the Thread to Complete at the End of the Current Sequence 
 —Specifies whether the calling sequence does not complete execution until the thread this step launches completes execution.
- Port Number 
 —The TCP/IP port number to use to connect to the remote system.
- Timeout (ms) 
 —The time, in milliseconds, to wait for a connection before timing out. A value of
 –1 
 indicates to wait indefinitely.
- Specified VI 
 —The local path of the LabVIEW NXG project/GLL and VI to run. Click the LabVIEW NXG icon to launch the
 Edit LabVIEW NXG VI Call 
 dialog box, in which you can specify the prototype and parameters of the VI.
- Context to Pass as ThisContext for VI Arguments 
 —The context the step uses when you pass
 ThisContext 
 as a parameter. Select from the following options:
  - Use Context of Calling Thread (Accessing the context of the calling thread requires additional synchronization for thread safety.) 
 —When you specify
 ThisContext 
 as an argument for a parameter of a VI, TestStand uses the context of the calling thread. If you enable this option, also enable the
 Automatically Wait for the Thread to Complete at the End of the Current Sequence 
 option to ensure that TestStand does not clean up the context of the calling thread before the asynchronous VI completes.
 Notice 
 Using the context of the calling thread in the newly created thread can lead to race conditions and crashes because the calling thread continues to execute in parallel, and TestStand might create or remove variables in the context of the calling thread while the sequence is running or when the sequence completes. TestStand does not automatically
ensure thread safety for structural changes to variables, such as adding or removing subproperties.
  - Use Context of New Thread (National Instruments recommends using this option if you do not need direct access to data from the calling sequence.) 
 —When you specify
 ThisContext 
 as an argument for a parameter of a VI, TestStand uses the context of the new thread. If you need to access variables from the context of the calling thread, pass the variables as parameters to the VI instead.

#### See Also

[Edit LabVIEW NXG VI Call dialog box](edit-labview-nxg-vi-call-dialog-box.html)

[LabVIEW NXG Utility Step Types](labview-utility-step-types2.html)

[Step Properties dialog box](step-properties-dialog-box.html)

[Wait Step](wait-step.html)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/run-options-panel-step-settings-pane.html language=enus -->
## TOPIC 04070: Run Options Panel - Step Settings Pane

- bundle_id: `teststand-api-reference`
- source_path: `tsref/run-options-panel-step-settings-pane.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/run-options-panel-step-settings-pane.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Run Options Panel The Run Options panel contains the following options: Load Option —Specifies one of the following Load Option settings for the step: Preload when opening sequence file —Loads the code module when TestStand loads into memory the sequence that contains the step. TestStand does not pr

### Run Options Panel - Step Settings Pane

#### Run Options Panel

The Run Options panel contains the following options:

- Load Option 
 —Specifies one of the following Load Option settings for the step:
  - Preload when opening sequence file 
 —Loads the
 code module 
 when TestStand loads into memory the sequence that contains the step.
 Note 
 TestStand does not preload
 [Sequence Call](sequence-call-step.html)
 step code modules that you specify by expression or that
 [call a custom sequence file](/csh?context=ts_tsfundamentals_translators)
 .
  - Preload when execution begins 
 —Loads the code module when any sequence in the sequence file that contains the step begins executing. This value is the default setting.
  - Load dynamically 
 —Does not load the code module until the step is ready to call it.
 Note 
 Typically, you must dynamically load
 [steps that execute conditionally based on bitness](/csh?context=ts_tsfundamentals_64bitnessconditionalcode)
 . If you preload steps that depend on bitness-specific code modules, the version of the step that does not match the bitness of TestStand fails to load and returns an error even though the bitness-conditional code prevents the step from executing.
- Unload Option 
 —Specifies when the step releases the reference to its code module. TestStand unloads a code module when all steps that refer to the code module can unload. This option specifies one of the following Unload Option settings for the step:
 
 Note 
 If you enable the Optimize Non-Reentrant Calls to this Sequence option on the
 [General](general-tab-sequence-properties-dialog-box.html)
 tab of the
 [Sequence Properties](sequence-properties-dialog-box.html)
 dialog box, TestStand does not unload the code modules for the sequence until after the execution ends, regardless of the Unload Option setting for the sequence file or the steps in the sequence.
  - Unload when precondition fails 
 —Unload the code module when the precondition for the step evaluates to
 False 
 .
  - Unload after step executes 
 —Unload the code module after the step finishes executing.
  - Unload after sequence executes 
 —Unload the code module after the sequence that contains it finishes executing.
  - Unload when sequence file is unloaded 
 —Unload the code module when TestStand unloads the sequence file that contains the step from memory. This value is the default setting.
- Run Mode 
 —Sets the following run-mode values for the step:
  - Normal 
 —The step executes normally.
  - Skip 
 —The step does not execute. Instead, the
 step status 
 is set to Skipped.
  - Force Pass 
 —The step does not execute. Instead, the step status is set to Passed.
  - Force Fail 
 —The step does not execute. Instead, the step status is set to Failed.
- Precondition Evaluation in Interactive Mode 
 —Determines whether TestStand evaluates the step precondition when you run the step interactively. This control contains the following options:
  - Evaluate precondition
  - Do not evaluate precondition
  - Use station option
- TestStand Window Activation 
 —Determines whether the TestStand application activates its window when the step completes. This control contains the following options:
  - Activate when step completes
  - If initially active, re-activate when step completes
  - No activation
- Result Recording Option 
 —Determines whether the contents of the Result property for the step are added to the
 result list 
 for the sequence. Select from the following recording options:
  - Disabled 
 —No result is recorded.
  - Enabled 
 —A result is recorded.
  - Enabled (override sequence setting) 
 —A result is recorded even if the value of
 Sequence.DisableResults 
 is
 True 
 .
- Step Failure Causes Sequence Failure 
 —TestStand maintains an internal status value for each executing sequence. When TestStand sets the status property of a step to
 Failed 
 , and you have enabled this option for the step, TestStand sets the internal sequence status value to
 Failed 
 . If the internal status of the sequence is Failed when the sequence returns, TestStand sets the status of the calling step to
 Failed 
 . This affects steps that use the
 Sequence Call 
 step type or the
 Action 
 step type with the Sequence Adapter. Steps that use the
 Pass/Fail Test 
 ,
 Numeric Limit Test 
 ,
 Multiple Numeric Limit Test 
 , and
 String Value Test 
 step types with the
 Sequence Adapter 
 overwrite the step status.
- Ignore Run-Time Errors 
 —Prevents the step from reporting a run-time error to the sequence. When a step causes a run-time error, the step stops executing, and TestStand sets the status of the step to
 Error 
 . when you disable this option, TestStand also sets the internal status of the sequence to
 Error 
 , and execution branches to the Cleanup step group for the sequence. When you enable this option, TestStand does not set the internal status of the sequence to
 Error 
 . Instead, TestStand resets the
 Error.Occurred 
 property of the step to
 False 
 and execution continues normally with the next step. The value of the
 Result.Status 
 property remains set to
 Error 
 for the step.
- Ignore Termination 
 —Controls the response of TestStand when a subsequence you call from this step causes the execution to terminate. When you enable this option, TestStand
 terminates the subsequence 
 and sets the status of the calling step to
 Terminated 
 but allows the calling sequence to proceed normally from the next step. In most cases, only process model files use this option. This option has no effect when you abort an execution.

The Run Options tab displays the following options for Sequence Call steps:

- Sequence Call Trace Setting 
 —Controls tracing for calls to a subsequence. The ring control contains the following options:
  - Use current trace setting 
 —Maintains the current tracing state when it calls the subsequence. This is the default value. In most cases, only process model files use other values for this option.
  - Enable tracing in sequence 
 —Enables tracing for calls to the subsequence, and it restores the original tracing state when the subsequence returns.
  - Disable tracing in sequence 
 —Disables tracing for calls to the subsequence, and restores the original tracing state when the subsequence returns. However, when you enable the Allow Tracing into Sequence Calls Marked with Tracing "Disabled" option on the
 Execution 
 tab of the
 Station Options 
 dialog box, TestStand ignores this setting and does not alter the tracing state when it calls the subsequence.
  - Use initial execution setting 
 —Enables the tracing state unless the execution was created while tracing was disabled. Typically, a process model uses this setting to control the tracing state when the model calls
 MainSequence 
 in the client sequence file.

#### See Also

[Sequence File Translators](/csh?context=ts_tsfundamentals_translators)

[Sequence Properties dialog box](sequence-properties-dialog-box.html)

Parent topic:

Properties Tab - Step Settings Pane

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/run-options-tab-step-properties-dialog-box.html language=enus -->
## TOPIC 04071: Run Options Tab - Step Properties Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/run-options-tab-step-properties-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/run-options-tab-step-properties-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Run Options Tab The Run Options tab contains the following options: Load Option —Specifies one of the following load option settings for the step: Preload when opening sequence file —Loads the code module when TestStand loads into memory the sequence that contains the step. TestStand does not preloa

### Run Options Tab - Step Properties Dialog Box

#### Run Options Tab

The Run Options tab contains the following options:

- Load Option 
 —Specifies one of the following load option settings for the step:
  - Preload when opening sequence file 
 —Loads the
 code module 
 when TestStand loads into memory the sequence that contains the step.
 Note 
 TestStand does not preload
 [Sequence Call](sequence-call-step.html)
 step code modules that you specify by expression or that
 [call a custom sequence file](/csh?context=ts_tsfundamentals_translators)
 .
  - Preload when execution begins 
 —Loads the code module when any sequence in the sequence file that contains the step begins executing. This value is the default setting.
  - Load dynamically 
 —Does not load the code module until the step is ready to call it.
- Unload Option 
 —Specifies when the step releases the reference to its code module. TestStand unloads a code module when all steps that refer to the code module can unload. This option specifies one of the following Unload Option settings for the step:
 
 Note 
 If you enable the Optimize Non-Reentrant Calls to this Sequence option on the
 [General](general-tab-sequence-properties-dialog-box.html)
 tab of the
 [Sequence Properties](sequence-properties-dialog-box.html)
 dialog box, TestStand does not unload the code modules for the sequence until after the execution ends, regardless of the Unload Option setting for the sequence file or the steps in the sequence.
  - Unload when precondition fails 
 —Unload the code module when the precondition for the step evaluates to
 False 
 .
  - Unload after step executes 
 —Unload the code module after the step finishes executing.
  - Unload after sequence executes 
 —Unload the code module after the sequence that contains it finishes executing.
  - Unload when sequence file closes 
 —Unload the code module when TestStand unloads the sequence file that contains the step from memory. This value is the default setting.
- Run Mode 
 —Sets the following run-mode values for the step:
  - Normal 
 —The step executes normally.
  - Skip 
 —The step does not execute. Instead, the
 step status 
 is set to
 Skipped 
 .
  - Force Pass 
 —The step does not execute. Instead, the step status is set to
 Passed 
 .
  - Force Fail 
 —The step does not execute. Instead, the step status is set to
 Failed 
 .
- Precondition Evaluation in Interactive Mode 
 —Determines whether TestStand evaluates the step precondition when you run the step interactively. This control contains the following options:
  - Use Station Options
  - Evaluate Precondition
  - Do Not Evaluate Precondition
- TestStand Window Activation 
 —Determines whether the TestStand application activates its window when the step completes. This control contains the following options:
  - No Activation
  - Activate When Step Completes
  - If Initially Active, Reactivate When Step Completes
- Breakpoint Settings 
 —Specifies whether TestStand suspends execution at this step before executing it. This section contains the following options:
 
 Note 
 You can also set the breakpoint state for a step by selecting
 Toggle Breakpoint
 in the context menu or by clicking to the left of the step icon in the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 .
  - Set Breakpoint 
 —The breakpoint is set. Disable this option to delete the breakpoint.
  - Configure 
 —Launches the
 Breakpoint Settings 
 dialog box, in which you can configure whether the breakpoint is disabled. You can also configure the pass count and conditional expression settings.
- Result Recording Option 
 —Determines whether the contents of the Result property for the step are added to the
 result list 
 for the sequence. Select from the following recording options:
  - Disabled 
 —No result is recorded.
  - Enabled 
 —A result is recorded.
  - Enabled (override sequence setting) 
 —A result is recorded even if the value of
 Sequence.DisableResults 
 is
 True 
 .
- Step Failure Causes Sequence Failure 
 —TestStand maintains an internal status value for each executing sequence. When TestStand sets the status property of a step to
 Failed 
 , and you have enabled this option for the step, TestStand sets the internal sequence status value to
 Failed 
 . If the internal status of the sequence is
 Failed 
 when the sequence returns, TestStand sets the status of the calling step to
 Failed 
 . This affects steps that use the Sequence Call step type or the Action step type with the Sequence Adapter. Steps that use the Pass/Fail Test, Numeric Limit Test, Multiple Numeric Limit Test, and String Value Test step types with the Sequence Adapter overwrite the step status.
- Ignore Run-Time Errors 
 —Prevents the step from reporting a run-time error to the sequence. When a step causes a run-time error, the step stops executing, and TestStand sets the status of the step to
 Error 
 . When you disable this option, TestStand also sets the internal status of the sequence to
 Error 
 , and execution branches to the Cleanup step group for the sequence. When you enable this option, TestStand does not set the internal status of the sequence to
 Error 
 . Instead, TestStand resets the
 Error.Occurred 
 property of the step to
 False 
 and execution continues normally with the next step. The value of the
 Result.Status 
 property remains set to
 Error 
 for the step.

If the step is a Sequence Call, the Run Options tab displays the following options:

- Sequence Call Trace Setting 
 —Controls tracing for calls to a subsequence. The following options are available in the ring control:
  - Use current trace setting 
 —Maintains the current tracing state when TestStand calls the subsequence. This is the default value. In most cases, only process model files use other values for this option.
  - Enable tracing in sequence 
 —Enables tracing for calls to the subsequence. TestStand restores the original tracing state when the subsequence returns.
  - Disable tracing in sequence 
 —Disables tracing for calls to the subsequence, and restores the original tracing state when the subsequence returns. However, when you enable the Allow Tracing into Sequence Calls Marked with Tracing "Disabled" option on the
 Execution 
 tab of the
 Station Options 
 dialog box, TestStand ignores this setting and does not alter the tracing state when it calls the subsequence.
  - Use initial execution setting 
 —Enables the tracing state unless the execution was created while tracing was disabled. Typically, a process model uses this setting to control the tracing state when the model calls
 MainSequence 
 in the client sequence file.
- Ignore Termination 
 —Controls the response of TestStand when a subsequence you call from this step causes execution to
 terminate 
 . When you enable this option, TestStand terminates the subsequence and sets the status of the calling step to
 Terminated 
 but allows the calling sequence to proceed normally from the next step. In most cases, only process model files use this option. This option has no effect when you abort an execution.

#### See Also

[Breakpoint Settings dialog box](breakpoint-settings-dialog-box.html)

[Sequence File Translators](/csh?context=ts_tsfundamentals_translators)

[Sequence Properties dialog box](sequence-properties-dialog-box.html)

[Station Options dialog box](station-options-dialog-box.html)

Parent topic:

Step Properties Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/run-time-error-dialog-box.html language=enus -->
## TOPIC 04072: Run-Time Error Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/run-time-error-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/run-time-error-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: TestStand launches the Run-Time Error dialog box when a run-time error occurs in an execution. This dialog box displays a detailed description of the error, the error code and error code description, if any, as well as the step, sequence, and sequence file where the error occurred. Certain errors in

### Run-Time Error Dialog Box

TestStand launches the Run-Time Error dialog box when a run-time error occurs in an execution.

This dialog box displays a detailed description of the error, the error code and error code description, if any, as well as the step, sequence, and sequence file where the error occurred. Certain errors include additional details. Click
 Expand/Collapse Details
 to view or hide these additional details. If there are no additional details, the button is hidden.

The Run-Time Error dialog box gives you the following options for handling a run-time error:

- Run Cleanup 
 —Execution proceeds to the Cleanup step group for the sequence. Run Cleanup is the default action when you have disabled the Show Dialog On Run-Time Error option on the
 Executions 
 tab of the
 Station Options 
 dialog box.
- Retry 
 —TestStand runs the step again.
- Ignore 
 —TestStand does not set the internal status of the sequence to
 Error 
 . Instead, TestStand resets the
 Error.Occurred 
 property of the step to
 False 
 and execution continues normally with the next step in the sequence. The
 Result.Status 
 property of the step remains set to
 Error 
 .
- Abort Immediately 
 —TestStand stops execution immediately without running any cleanup steps.

The Run-Time Error dialog box also provides two further options:

- Break 
 —When you select
 Run Cleanup 
 ,
 Retry 
 , or
 Ignore 
 and then enable this option, TestStand suspends execution at the step that caused the run-time error. This option is disabled when you select
 Abort Immediately 
 .
- Do Not Show Dialog Box Again for this Execution 
 —This option prevents the Run-Time Error dialog box from opening for any run-time errors that occur later in the execution. This option is disabled when you select
 Retry 
 .

#### See Also

[Station Options dialog box](station-options-dialog-box.html)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/run-vi-asynchronously-edit-tab.html language=enus -->
## TOPIC 04073: Run VI Asynchronously Edit Tab

- bundle_id: `teststand-api-reference`
- source_path: `tsref/run-vi-asynchronously-edit-tab.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/run-vi-asynchronously-edit-tab.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Insert a Run VI Asynchronously step and select Edit Run VI Asynchronously or Step Settings from the context menu to display the Run VI Asynchronously edit tab in the TestStand Sequence Editor . Use the Run VI Asynchronously edit tab to specify the remote system, port number, and VI to run. When Test

### Run VI Asynchronously Edit Tab

Insert a Run VI Asynchronously step and select
 Edit Run VI Asynchronously
 or
 Step Settings
 from the context menu to display the Run VI Asynchronously edit tab in the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 .

Use the Run VI Asynchronously edit tab to specify the remote system, port number, and VI to run. When TestStand executes the Run VI Asynchronously step, TestStand launches a dynamically-generated sequence in a new thread which executes the VI on a remote system.

The Run VI Asynchronously edit tab contains the following options:

- Hostname 
 —The remote system. Leave this option empty to use the local computer.
 Note 
 The Run VI Asynchronously step does not support running a VI on a remote Microsoft Windows computer.
- Specify Remote Host by Expression 
 —Enable this option to specify that the Hostname control contains an expression the step evaluates at run time to determine the name of the remote host.
- Port Number 
 —The TCP/IP port number to use to connect to the remote system.
- Timeout (ms) 
 —The time, in milliseconds, to wait for a connection before timing out. A value of
 –1 
 indicates to wait indefinitely.
- Specified VI 
 —The local path of the VI to run on the remote system. Click
 Specify VI 
 to launch the
 Edit LabVIEW VI Call 
 dialog box, in which you can specify the prototype and parameters of the VI. When you select multiple Run VI Asynchronously steps, TestStand dims the Specify VI button.
- Store an Object Reference to the New Thread in (optional) 
 —The location to store the reference to the new
 Thread 
 object the step creates. You can use this reference in subsequent calls to the TestStand API. You can also use this reference in a
 Wait 
 step to wait for the thread to complete.
- Automatically Wait for the Thread to Complete at the End of the Current Sequence 
 —Specifies whether the calling sequence does not complete execution until the thread this step launches completes execution.
- Context to Pass as ThisContext for VI Arguments 
 —The context the step uses when you pass
 ThisContext 
 as a parameter. Select from the following options:
  - Use Context of Calling Thread (Accessing the context of the calling thread requires additional synchronization for thread safety.) 
 —When you specify
 ThisContext 
 as an argument for a parameter of a VI, TestStand uses the context of the calling thread. If you enable this option, also enable the
 Automatically Wait for the Thread to Complete at the End of the Current Sequence 
 option to ensure that TestStand does not clean up the context of the calling thread before the asynchronous VI completes.
 Notice 
 Using the context of the calling thread in the newly created thread can lead to race conditions and crashes because the calling thread continues to execute in parallel, and TestStand might create or remove variables in the context of the calling thread while the sequence is running or when the sequence completes. TestStand does not automatically ensure thread safety for structural changes to variables, such as adding or removing subproperties.
  - Use Context of New Thread (National Instruments recommends using this option if you do not need direct access to data from the calling sequence.) 
 —When you specify
 ThisContext 
 as an argument for a parameter of a VI, TestStand uses the context of the new thread. If you need to access variables from the context of the calling thread, pass the variables as parameters to the VI instead.

#### See Also

[Calling VIs on Remote Computers](/csh?context=ts_tslabview_remote)

[Edit LabVIEW VI Call dialog box](edit-labview-vi-call-dialog-box.html)

[LabVIEW Utility Step Types](labview-utility-step-types.html)

[Thread](../tsapiref/thread.html)

[Wait Step](wait-step.html)

Parent topic:

Run VI Asynchronously Step - LabVIEW Utility Step Types

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/run-vi-asynchronously-step-configuration-dial.html language=enus -->
## TOPIC 04074: Run VI Asynchronously Step Configuration Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/run-vi-asynchronously-step-configuration-dial.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/run-vi-asynchronously-step-configuration-dial.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Select Configure Run VI Asynchronously in the context menu for the step to launch the Run VI Asynchronously Step Configuration dialog box from a TestStand User Interface . You can also click Configure Run VI Asynchronously on the General tab of the Step Properties dialog box. Use the Run VI Asynchro

### Run VI Asynchronously Step Configuration Dialog Box

Select
 Configure Run VI Asynchronously
 in the context menu for the step to launch the Run VI Asynchronously Step Configuration dialog box from a
 [TestStand User Interface](teststand-user-interfaces.html)
 . You can also click
 Configure Run VI Asynchronously
 on the
 [General](step-properties-dialog-box.html)
 tab of the
 [Step Properties](step-properties-dialog-box.html)
 dialog box.

Use the Run VI Asynchronously Step Configuration dialog box to specify the remote system, port number, and VI to run. When TestStand executes the Run VI Asynchronously step, TestStand launches a dynamically-generated sequence in a new thread which executes the VI on a remote system.

The Run VI Asynchronously Step Configuration dialog box contains the following options:

- Hostname 
 —The remote system. Leave this option empty to use the local computer.
 Note 
 The Run VI Asynchronously step does not support running a VI on a remote Microsoft Windows computer.
- Specify Remote Host by Expression 
 —Enable this option to specify that the Hostname control contains an expression the step evaluates at run time to determine the name of the remote host.
- Port Number 
 —The TCP/IP port number to use to connect to the remote system.
- Timeout (ms) 
 —The time, in milliseconds, to wait for a connection before timing out. A value of
 –1 
 indicates to wait indefinitely.
- Store an Object Reference to the New Thread in (optional) 
 —The location to store the reference to the new Thread object the step creates. You can use this reference in subsequent calls to the TestStand API. You can also use this reference in a
 Wait 
 step to wait for the thread to complete.
- Automatically Wait for the Thread to Complete at the End of the Current Sequence 
 —Specifies whether the calling sequence does not complete execution until the thread this step launches completes execution.
- Specified VI 
 —The local path of the VI to run on the remote system. Click the LabVIEW icon to launch the
 Edit LabVIEW VI Call 
 dialog box, in which you can specify the prototype and parameters of the VI.
- Context to Pass as ThisContext for VI Arguments 
 —The context the step uses when you pass
 ThisContext 
 as a parameter. Select from the following options:
  - Use Context of Calling Thread (Accessing the context of the calling thread requires additional synchronization for thread safety.) 
 —When you specify
 ThisContext 
 as an argument for a parameter of a VI, TestStand uses the context of the calling thread. If you enable this option, also enable the
 Automatically Wait for the Thread to Complete at the End of the Current Sequence 
 option to ensure that TestStand does not clean up the context of the calling thread before the asynchronous VI completes.
 Notice 
 Using the context of the calling thread in the newly created thread can lead to race conditions and crashes because the calling thread continues to execute in parallel, and TestStand might create or remove variables in the context of the calling thread while the sequence is running or when the sequence completes. TestStand does not automatically
ensure thread safety for structural changes to variables, such as adding or removing subproperties.
  - Use Context of New Thread (National Instruments recommends using this option if you do not need direct access to data from the calling sequence.) 
 —When you specify
 ThisContext 
 as an argument for a parameter of a VI, TestStand uses the context of the new thread. If you need to access variables from the context of the calling thread, pass the variables as parameters to the VI instead.

#### See Also

[Calling VIs on Remote Computers](/csh?context=ts_tslabview_remote)

[Edit LabVIEW VI Call dialog box](edit-labview-vi-call-dialog-box.html)

[LabVIEW Utility Step Types](labview-utility-step-types.html)

[Step Properties dialog box](step-properties-dialog-box.html)

[Wait Step](wait-step.html)

Parent topic:

Run VI Asynchronously Step - LabVIEW Utility Step Types

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/run-vi-asynchronously-step-labview-utility-st.html language=enus -->
## TOPIC 04075: Run VI Asynchronously Step - LabVIEW Utility Step Types

- bundle_id: `teststand-api-reference`
- source_path: `tsref/run-vi-asynchronously-step-labview-utility-st.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/run-vi-asynchronously-step-labview-utility-st.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Run VI Asynchronously Step Use a Run VI Asynchronously step to run a VI in a new thread in the TestStand execution. The step launches a dynamically-generated sequence by executing the VI in a step and then returns when the VI completes. This step is particularly useful when you are downloading and r

### Run VI Asynchronously Step - LabVIEW Utility Step Types

#### Run VI Asynchronously Step

Use a Run VI Asynchronously step to run a VI in a new thread in the TestStand execution.

#### Configuring the Step

Use the
 [Run VI Asynchronously](run-vi-asynchronously-edit-tab.html)
 edit tab in the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 and the
 [Run VI Asynchronously Step Configuration](run-vi-asynchronously-step-configuration-dial.html)
 dialog box in a
 [TestStand User Interface](teststand-user-interfaces.html)
 to specify the remote system, port number, and VI to download and run.

#### Step Properties

In addition to the common custom properties, the Run VI Asynchronously step type defines the following step properties:

- Step.RemoteHost 
 —The computer name or IP address of the remote computer. The
 Step.RemoteHostByExpr 
 property specifies whether the step interprets this property value as an expression or as a string.
- Step.RemoteHostByExpr 
 —When this property is
 True 
 , the step interprets the
 Step.RemoteHost 
 property value as an expression. When this property is
 False 
 , the step interprets the value as a string.
- Step.PortNumber 
 —The remote host port number.
- Step.Timeout 
 —The number of seconds to wait to connect to the remote computer.
- Step.VIModule 
 —The settings for the VI the step calls.

#### See Also

[Calling VIs on Remote Computers](/csh?context=ts_tslabview_remote)

[LabVIEW Utility Step Types](labview-utility-step-types.html)

Parent topic:

LabVIEW Utility Step Types

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/run-vi-asynchronously-step-labview-utility-st2.html language=enus -->
## TOPIC 04076: Run VI Asynchronously Step - LabVIEW Utility Step Types

- bundle_id: `teststand-api-reference`
- source_path: `tsref/run-vi-asynchronously-step-labview-utility-st2.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/run-vi-asynchronously-step-labview-utility-st2.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Run LV NXG VI Asynchronously Step Use a Run LV NXG VI Asynchronously step to run a VI in a new thread in the TestStand execution. The step launches a dynamically-generated sequence by executing the VI in a step and then returns when the VI completes. Configuring the Step Use the Run LV NXG VI Asynch

### Run VI Asynchronously Step - LabVIEW Utility Step Types

#### Run LV NXG VI Asynchronously Step

Use a Run LV NXG VI Asynchronously step to run a VI in a new thread in the TestStand execution.

#### Configuring the Step

Use the
 [Run LV NXG VI Asynchronously](run-lv-nxg-vi-asynchronously-edit-tab.html)
 edit tab in the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 and the
 [Run LV NXG VI Asynchronously Step Configuration](run-lv-nxg-vi-asynchronously-step-configurati.html)
 dialog box in a
 [TestStand User Interface](teststand-user-interfaces.html)
 to specify the VI to run.

#### Step Properties

In addition to the common custom properties, the Run LV NXG VI Asynchronously step type defines the following step properties:

- Step.GVIModule 
 —The settings for the VI the step calls.

Parent topic:

LabVIEW Utility Step Types

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/save-all-modified-files-dialog-box.html language=enus -->
## TOPIC 04077: Save All Modified Files Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/save-all-modified-files-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/save-all-modified-files-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: TestStand launches the Save All Modified Files dialog box when you attempt to save all files and one or more files are read-only or when you do not have the necessary privileges to save the files. The list control displays all modified files. You can select which files to save, as the following tabl

### Save All Modified Files Dialog Box

TestStand launches the Save All Modified Files dialog box when you attempt to save all files and one or more files are read-only or when you do not have the necessary privileges to save the files.

The list control displays all modified files. You can select which files to save, as the following table describes.

| File Type | Availability |
| --- | --- |
| Files for which you have permission to save | Selected to save by default |
| Files for which you do not have permission to save | Dimmed |
| Read-only files | Not selected to save by default |

The Save All Modified Files dialog box contains the following options:

- Save Checked Files 
 —TestStand saves the selected files.
- Cancel 
 —TestStand does not save any files.

#### See Also

[Close All Windows Modified Files dialog box](close-all-windows-modified-files-dialog-box.html)

[Logout Modified Files dialog box](logout-modified-files-dialog-box.html)

[Shutdown Modified Files dialog box](shutdown-modified-files-dialog-box.html)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/schema-validation-dialog-box.html language=enus -->
## TOPIC 04078: Schema Validation Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/schema-validation-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/schema-validation-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Click Validate in the Schema section of the Database Options dialog box to launch the Schema Validation dialog box. Validation attempts to determine whether the statement and column information for the selected schema matches the tables and columns in the database the connection string on the Data L

### Schema Validation Dialog Box

Click
 Validate
 in the
 [Schema](schemas-tab-database-options-dialog-box.html)
 section of the
 [Database Options](database-options-dialog-box.html)
 dialog box to launch the Schema Validation dialog box.

Validation attempts to determine whether the statement and column information for the selected schema matches the tables and columns in the database the connection string on the
 [Data Link Options](logging-data-link-options-tab-database-option.html)
 section specifies.

The Schema Validation dialog box contains the following controls:

- Message Level 
 —Shows the level of messages displayed in the list box.
  - Errors and Warnings 
 —Displays both errors and warnings in the list box.
  - Errors Only 
 —Displays only errors in the list box.
  - Warnings Only 
 —Displays only warnings in the list box.
- Differences 
 —Displays the differences TestStand found when comparing the schema to the data source.
- SQL Tools 
 —The SQL commands to generate when you click the
 Generate SQL 
 button. The ring control contains the following options:
  - Add Missing Items 
 —Generates SQL commands to insert the missing tables and columns listed in the Differences control.
  - Drop All Schema Tables 
 —Generates SQL commands to delete the tables the schema defines.
  - Clear All Schema Tables 
 —Generates SQL commands to delete the records from the tables the schema defines.
- Generate SQL 
 —Launches the
 Database Viewer application 
 , opens the data source, and places the generated SQL commands in an Execute SQL window.
- Revalidate 
 —Revalidates the current schema against the database.

#### See Also

[Database Options dialog box](database-options-dialog-box.html)

[Database Viewer](database-viewer-application.html)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/schemas-context-menu-and-shortcut-keys-databa.html language=enus -->
## TOPIC 04079: Schemas Context Menu and Shortcut Keys - Database Options Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/schemas-context-menu-and-shortcut-keys-databa.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/schemas-context-menu-and-shortcut-keys-databa.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Schemas Context Menu and Shortcut Keys Schemas Context Menu Right-click Schema/Statement/Column or Parameter in the Schema Section to access the context menu. The context menu contains the following options: New —Creates new Schema/Statement/Column or Parameter. Copy —Copies the selected item to the

### Schemas Context Menu and Shortcut Keys - Database Options Dialog Box

#### Schemas Context Menu and Shortcut Keys

#### Schemas Context Menu

Right-click Schema/Statement/Column or Parameter in the
 [Schema Section](schemas-tab-database-options-dialog-box.html)
 to access the context menu.

The context menu contains the following options:

- New 
 —Creates new Schema/Statement/Column or Parameter.
- Copy 
 —Copies the selected item to the clipboard.
- Cut 
 —Removes the selected item and places it on the clipboard
- Paste 
 —Pastes the item from the clipboard.
- Delete 
 —Deletes the selected item.

#### Shortcut Keys

You may use the following shortcut keys:

- Ctrl+N 
 —Creates a new schema/statement/column or parameter.
- Ctrl+X 
 —Removes the selected item and keeps it in the clipboard.
- Ctrl+C 
 —Copies the selected item to the clipboard.
- Ctrl+V 
 —Inserts the item from the clipboard at the end of the list.
- Del 
 —Deletes the selected item.
- Ctrl+Up 
 —Moves the selected item up in the list.
- Ctrl+Down 
 —Moves the selected item down in the list.
- Arrow Keys 
 —Navigates the schemas, statements, columns / parameters.

Parent topic:

Schemas Tab - Database Options Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/schemas-tab-database-options-dialog-box.html language=enus -->
## TOPIC 04080: Schemas Tab - Database Options Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/schemas-tab-database-options-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/schemas-tab-database-options-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Schemas Tab Schema Section The Schema section contains the following options: Name —Specifies the name of the schema. Comment —Specifies the comment for the schema. Validate —Launches the Schema Validation dialog box, which determines whether the statement and column information for the selected sch

### Schemas Tab - Database Options Dialog Box

#### Schemas Tab

#### Schema Section

The Schema section contains the following options:

- Name 
 —Specifies the name of the schema.
- Comment 
 —Specifies the comment for the schema.
- Validate 
 —Launches the
 Schema Validation 
 dialog box, which determines whether the statement and column information for the selected schema matches the tables and columns in the database specified by the connection string on the Logging Options/Data Link tab.
- Build .sql File 
 —Specifies the file path of the
 .sql 
 file that contains the SQL commands that generate the tables and columns of the selected schema.
 Note 
 The Build .sql File option does not produce complete SQL files. Use the generated SQL files as a starting point for the selected schema.
- Allow Editing of Schema 
 —Enables controls that edit the schema.
 Note 
 To ensure that installers for newer versions of TestStand do not overwrite the schema customizations, create a copy of the National Instruments schema using the
 [Schemas Context Menu and Shortcut Keys](schemas-context-menu-and-shortcut-keys-databa.html)
 . Make changes to the new copy of the schema and click the checkbox next to the new schema to identify it as the default.

Parent topic:

Schemas Tab - Database Options Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/schemas-tab-database-options-dialog-box2.html language=enus -->
## TOPIC 04081: Schemas Tab - Database Options Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/schemas-tab-database-options-dialog-box2.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/schemas-tab-database-options-dialog-box2.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Schemas Tab Column/Parameter Section For recordset statements, TestStand expects the recordset to return the specified column names. The order of the columns in the list control is arbitrary. For command statements, TestStand creates a parameter for each item in the list. Depending on whether the pa

### Schemas Tab - Database Options Dialog Box

#### Schemas Tab

#### Column/Parameter Section

For recordset statements, TestStand expects the recordset to return the specified column names. The order of the columns in the list control is arbitrary. For command statements, TestStand creates a parameter for each item in the list. Depending on whether the parameter is an input or an output operation, TestStand will set or get the value. While the name of the parameter is arbitrary, the order of the parameters in the list must match the required parameters for the statement. For parameterized statements, the order of the parameters in the list must correspond to the required parameters for the statement.

The Columns/Parameters section contains the following options:

- Name 
 —Edits the name of the column or parameter. For recordset statements, the name must match a column in the returned recordset. For parameterized statements, the name is arbitrary.
- Type 
 —The data type of the column or parameter value. The following options are available in the ring control: Small Integer, Integer, Big Integer, Unsigned Big Integer, Float, Double-Precision, String (BSTR), String (varchar), Boolean, Binary, Date/Time, and GUID.
- Size 
 —The maximum number of bytes TestStand writes to or reads from a column or parameter. If the column does not have a size limitation, you can specify
 0 
 to instruct TestStand to write or read the entire value.
 
 Note 
 Database logging schemas that use stored procedures reserve memory to buffer the logging of large binary column values. If you configure database logging to open a separate connection for each socket and you use the Parallel or Batch process models with a high number of test sockets, database logging can report an out-of-memory error. Enable the
 Share Data Link Between Executions
 option on the
 [Data Link Options](logging-data-link-options-tab-database-option.html)
 section of the
 [Database Options](database-options-dialog-box.html)
 dialog box, or lower the limit on the size of binary data that TestStand logs for each binary column.
- Direction 
 —Specifies whether the column or parameter is an input or output value. The following options are available in the ring control:
  - Input 
 —TestStand writes the column value or parameter to the database.
  - Output 
 —Specifies whether TestStand retrieves the column value or parameter from the database. This option is valid only for statements of type stored procedure.
  - Input/Output 
 —Specifies whether TestStand writes and retrieves the column value or parameter. This option is valid only for statements of type stored procedure.
  - Return Value 
 —TestStand retrieves the parameter value as a return value from the database. This option is valid only for statements of type stored procedure.
- Expected Properties 
 —The properties that must exist before TestStand assigns or retrieves a value for the column or parameter. Leave this control empty to instruct TestStand not to require any expected properties.
- Precondition 
 —An expression that must evaluate to
 True 
 before TestStand assigns or retrieves a value for the column or parameter. Leave this control empty to instruct TestStand not to apply a precondition.
- Value to Log/Value 
 —An expression the column or parameter evaluates to obtain the input value to log or the variable property location to store the retrieved output value, respectively.
 Note 
 When the database logger does not evaluate a column expression at run-time because the properties listed in the Expected Properties control do not exist or the Precondition expression evaluates to
 False
 , the database logger assigns a NULL value to the database column. When the database logger evaluates an Expression for a column of type
 string
 , and the value returned from the expression is empty, the database logger assigns an empty string value to the column.
- Format 
 —Instructs TestStand how to
 format a Date/Time string 
 or array value when assigning the column value. Select a format from the list or type a custom format in the edit box. This control is enabled only when the column type is Date/Time or binary. Refer to
 Logging Binary and String Database Values 
 for more information about writing values to binary and string columns.
- Primary Key 
 —Enable this section to specify that the database column is a primary key. The primary key column must contain unique values.
 
 Note 
 Multiple primary keys are not supported in a single statement.
  - Type 
 —Specifies how TestStand obtains a unique primary key value to assign to a new record. The following options are available in the ring control:
    - Auto Generated/Counter 
 —TestStand requests the value the database assigns to the new record.
    - Store GUID Value 
 —TestStand generates a unique string value. The database column type must be GUID or String and must use at least 36 bytes for a string.
    - Get Value from Recordset 
 —TestStand executes the SQL command specified in the Command Text control and retrieves the value returned in the first column in the first record of the recordset.
    - Get Value from Output Parameter 
 —TestStand executes the SQL command specified in the Command Text control and retrieves the value returned as an output parameter.
    - Get Value from Return Value 
 —TestStand executes the SQL command specified in the Command Text control and retrieves the return value.
    - Use Expression Value 
 —TestStand evaluates the value specified in the Expression control to determine the primary key value. The primary key value must evaluate to a unique value for the specified column or parameter.
  - Command Text 
 —The text of a command the statement issues against the data link to obtain the primary key value. Only use this control when you select Get Value from Recordset or Get Value from Output Parameter in the Type ring control.
- Foreign Key 
 —Enable this section to specify that the database column is a foreign key. A foreign key is a column that references a primary key in a table.
  - Statement 
 —Select the statement that contains the primary key column in which the foreign key references. TestStand automatically assigns the primary key value to the column or parameter. 
 
 TestStand logs data in the order of statements in the schema. A foreign key statement is valid if the database table to which the foreign key statement logs is logged before the selected statement logs. To log a valid foreign key, select the foreign key statement in one of the following ways:
 
 Note that the foreign key statement ring control lists valid statements only if the statement type is not "Stored Procedure". If the statement type is "Stored Procedure", the ring control lists all statements.
    1. Choose a statement that is above the parent statement (statement of the selected column) or select the parent statement.
    2. Choose a statement such that the database table to which the chosen statement logs is logged before parent statement (statement of the selected column) logs the data.

Note

log attribute values

#### See Also

[Format Strings for Database Date Values](/csh?context=ts_tsfundamentals_strings_format)

[Logging Attribute Values](/csh?context=ts_tsfundamentals_logging_attribute_values)

[Logging Binary and String Database Values](logging-teststand-values-to-binary-and-string.html)

Parent topic:

Schemas Tab - Database Options Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/schemas-tab-database-options-dialog-box3.html language=enus -->
## TOPIC 04082: Schemas Tab - Database Options Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/schemas-tab-database-options-dialog-box3.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/schemas-tab-database-options-dialog-box3.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Schemas Tab A schema defines how TestStand logs results to a database. A schema consists of a list of statements and each statement consists of a list of columns. The Schemas tab contains the following sections: Schema —Displays the setting for the selected schema. Click the checkbox next to the sch

### Schemas Tab - Database Options Dialog Box

#### Schemas Tab

A schema defines how TestStand logs results to a database. A schema consists of a list of statements and each statement consists of a list of columns.

The Schemas tab contains the following sections:

- Schema 
 —Displays the setting for the selected schema. Click the checkbox next to the schema you want the TestStand process model to use as the default schema.
 Use the up and down arrow buttons to control the order of the items in the list. Use the
 Import 
 and
 Export 
 buttons to share one or more schemas with another test station.
 Note 
 You cannot move a statement up if the following two conditions are true:
 One or more columns in the statement you want to move has a foreign key set to the statement above.
 The statement above does not log to the same table as any other statement higher in the list.
 You cannot move a statement down if the following two conditions are true:
 One or more columns in the statement below has a foreign key set to the statement you want to move.
 No statement above logs to the same table as the statement you want to move.
- Statement 
 —Displays the settings for the selected statement. Expand a schema to view the list of statements in the schema.
- Column/Parameter 
 —Displays the settings for the selected column/parameter. Expand a statement to view the list of columns/parameters in the statement.

The Schemas tab also contains the following controls:

- Schemas Context Menu and Shortcut Keys 
 —Edits the items in the view.
- Reload NI Schemas 
 —Reloads all the default NI schemas TestStand installs.

#### See Also

[Schema Validation dialog box](schema-validation-dialog-box.html)

Parent topic:

Database Options Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/schemas-tab-database-options-dialog-box4.html language=enus -->
## TOPIC 04083: Schemas Tab - Database Options Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/schemas-tab-database-options-dialog-box4.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/schemas-tab-database-options-dialog-box4.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Schemas Tab Statement Section Statements define the type of results on which the schema operates and the conditions that must be True before TestStand logs the results. Statements also define the database action to perform. In addition, statements specify what database columns or parameters to log a

### Schemas Tab - Database Options Dialog Box

#### Schemas Tab

#### Statement Section

Statements define the type of results on which the schema operates and the conditions that must be
 True
 before TestStand logs the results. Statements also define the database action to perform. In addition, statements specify what database columns or parameters to log and what TestStand
 [expressions](/csh?context=ts_tsfundamentals_bldgblocks_expressions)
 to evaluate in order to determine the column or parameter values.

The Statements section contains the following options:

- Name 
 —Edits the name of the statement. Typically, the statement name has the same name as the database table to which it logs data.
- Type 
 —The type of statement. You can select one of the following options from the ring control:
  - Recordset 
 —When you enable this option, the statement returns a recordset. For the columns defined on the
 Columns/Parameters 
 section, TestStand inserts a new record into the recordset. You would typically use an SQL SELECT command that returns a recordset with this option.
  - Command 
 —When you enable this option, TestStand executes a command for each result that applies to the statement. For each column defined on the
 Columns/Parameters 
 section, TestStand creates a parameter. This type of statement is called a parameterized statement. For input parameters, TestStand assigns the column value to the parameter before executing the statement. For output parameters, TestStand retrieves the parameter value after executing the statement. You would typically use an SQL INSERT command that contains the question mark
 "?" 
 keyword to specify the parameters.
  - Stored Procedure 
 —When you enable this option, TestStand executes a stored procedure for each result that applies to the statement. For each column defined on the Columns/Parameters tab, TestStand creates a parameter. For input parameters, TestStand assigns the column value to the parameter before executing the statement. For output parameters, TestStand retrieves the parameter value after executing the statement. Stored procedures can also return a value in addition to output parameters.
 Note 
 If you attempt to use on-the-fly database logging with a schema that uses stored procedure statements or command statements that do not use the SQL INSERT command, you cannot define constraints for foreign keys in step result statements that reference primary keys in a UUT result statement or foreign keys in a step result statement that references their own primary keys. If you define constraints for these types of foreign keys, an error will occur because the on-the-fly database logger cannot execute the statement to create the record that contains the primary key before executing the statement to create the record that contains the foreign key.
- Command Text 
 —The text of a command the statement issues against the data link. While this is typically an SQL SELECT or SQL INSERT statement, you can use any type of command statement the database provider recognizes, including stored procedure calls.
- Apply To 
 —The class of results on which the statement operates. The following options are available in the ring control:
  - UUT Result 
 —TestStand applies the statement once per UUT.
  - Step Result 
 —TestStand applies the statement to each step result.
  - Property Result 
 —TestStand applies the statement to each subproperty of a step result.
- Types to Log 
 —The data types of results for which the statement applies. For step results, the type must be the name of a TestStand step type. For property results, the type must be the name of a TestStand data type. This option does not apply to a UUT Result. Leave the control empty to instruct TestStand not to require any type matching.
- Expected Properties 
 —The properties that must exist before TestStand applies the statement to a particular result. Leave the control empty to instruct TestStand not to require any expected properties.
- Precondition 
 —An expression that must evaluate to
 True 
 before TestStand applies the statement to a particular result. Leave the control empty to instruct TestStand not to apply a precondition.
- Cursor Type 
 —The type of server or client cursor for the statement. The following options are available in the ring control:
  - Unspecified 
 —Do not specify a cursor type.
  - Forward Only 
 —Identical to a static cursor except you can only scroll forward through records. This option improves performance when you want to make a single pass through a set of records.
  - Keyset 
 —Similar to dynamic cursor, except you cannot see records other users add. Records other users delete are inaccessible from your set of records. Data changes by other users within records are visible.
  - Dynamic 
 —Additions, changes, and deletions other users perform are visible. All types of movement through the set of records are allowed.
  - Static 
 —Additions, changes, and deletions other users perform are not visible.
- Cursor Location 
 —Specifies where the data source maintains cursors for a connection. The following options are available in the ring control:
  - Server 
 —Uses cursors the data provider supplies. These cursors are sometimes very flexible and allow for additional sensitivity to reflect changes other users make to the actual data.
  - Client 
 —Uses client-side cursors a local cursor library supplies. Local cursor engines often allow many features driver supplied cursors do not.
- Lock Type 
 —Specifies when the data source locks a record. The following options are available in the ring control:
  - Unspecified 
 —Do not specify a lock type.
  - Read Only 
 —You cannot alter the data in a record.
  - Pessimistic 
 —The provider does what is necessary to ensure successful editing of the records, usually by locking records at the data source immediately upon editing.
  - Optimistic 
 —The provider only locks records when you send the data back to the database.
  - Batch Optimistic 
 —Required for batch updates.
 Note 
 If you attempt to set the lock type to Read-Only for the record set statement where one or more statements in the schema has foreign key dependency on the statement and Use On-The-Fly is set for database logging, On-the-fly database logger may not be able to update the recordset.
- Traversing Options 
 —Launches the
 Traversing Options 
 dialog box, in which you can specify if subsequent statements can process the current UUT, the step or property result, or the sub-results of the step or property result.

#### See Also

[Traversing Options dialog box](traversing-options-dialog-box.html)

Parent topic:

Schemas Tab - Database Options Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/scope-step.html language=enus -->
## TOPIC 04084: Scope Step

- bundle_id: `teststand-api-reference`
- source_path: `tsref/scope-step.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/scope-step.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use an IVI Scope step to acquire a voltage waveform from an analog input signal using oscilloscopes. Configuring the Step Use the Edit IVI Scope Step dialog box in the TestStand Sequence Editor and in a TestStand User Interface to configure the IVI Scope step. Step Operations The IVI Scope step type

### Scope Step

Use an IVI Scope step to acquire a voltage waveform from an analog input signal using oscilloscopes.

#### Configuring the Step

Use the
 [Edit IVI Scope Step](edit-ivi-scope-step-dialog-box.html)
 dialog box in the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 and in a
 [TestStand User Interface](teststand-user-interfaces.html)
 to configure the IVI Scope step.

#### Step Operations

The IVI Scope step type supports the following operations:

- Configure 
 —Configures the instrument to match the state the step specifies.
- Show Soft Front Panel 
 —Displays the soft front panel (SFP) for the instrument.
- Hide Soft Front Panel 
 —Hides the SFP for the instrument.
- Read 
 —Initiates and returns a measurement from the instrument.
- Initiate 
 —Initiates a measurement.
- Fetch 
 —Returns a measured value from a measurement the Initiate operation has started.
- Abort 
 —Cancels the wait for a trigger.
- Auto Setup 
 —Performs an automatic setup on the instrument.
- Get Information 
 —Retrieves low-level status and information from the instrument.

#### Step Properties

In addition to the
 [common custom properties](/csh?context=ts_tsfundamentals_custom_result_props)
 , the IVI Scope step type defines the following step properties:

- Step.Result.Reading 
 —The measurement values for the Read and Fetch operations. This property is a container array, and the size of the array equals the number of channels you specify for the Read or Fetch operation. The data type of each element of the array is NI_IviSinglePoint, NI_IviWave, or NI_IviWavePair.
- Step.LogicalName 
 —The logical name expression.
- Step.InstrOperation 
 —A value that specifies the operation you configured the step to perform.
- Step.SettingsSource 
 —The name of the property or variable where the step loads and stores the settings for the operation.
- Step.Configuration 
 —The settings for the Configure operation. The data type of this property is NI_IviScopeConfig.
- Step.SoftFrontPanel 
 —The settings for the Show Soft Front Panel operation. The data type of this property is NI_IviSoftFrontPanel.
- Step.Readings 
 —The settings for the Read and Fetch operations. The data type of this property is NI_IviScopeReadings. The Channels subproperty is an NI_IviScopeChannel array.
- Step.GetInfo 
 —The settings for the
 Get Information operation 
 .

#### See Also

[IVI Step Types](ivi-step-types.html)

Parent topic:

IVI Step Types

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/search-for-tab-find-replace-in-files-dialog-b.html language=enus -->
## TOPIC 04085: Search For Tab - Find/Replace in Files Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/search-for-tab-find-replace-in-files-dialog-b.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/search-for-tab-find-replace-in-files-dialog-b.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Search For Tab The Search For tab contains the following options: Find —The string or regular expression to search for. When the Regular Expression option is enabled, you can specify a regular expression. This control contains a ring control you can use to select a previously used string. Match Case

### Search For Tab - Find/Replace in Files Dialog Box

#### Search For Tab

The Search For tab contains the following options:

- Find 
 —The string or regular expression to search for. When the Regular Expression option is enabled, you can specify a regular expression. This control contains a ring control you can use to select a previously used string.
  - Match Case 
 —Specifies whether the matching of characters is case-sensitive or case-insensitive. For example, if
 CHR 
 is the specified text and you enable the Match Case option, TestStand finds
 CHR 
 but not
 Chr 
 .
  - Match Whole Word Only 
 —Finds the specified text only when the characters surrounding it are spaces, punctuation marks, or other characters not considered parts of a word. TestStand treats the following characters as part of a word:
 A 
 through
 Z 
 ,
 a 
 through
 z 
 ,
 0 
 through
 9 
 , and the underscore (
 _ 
 ).
  - Regular Expression 
 —If you enable this option, TestStand treats certain characters in the Find text box as
 regular expression characters 
 instead of literal characters.
- Search in 
 —Use the following controls to specify the files in which to search:
  - Opened File 
 —TestStand searches in an open sequence file. In the ring control, you can choose Station Globals, Type Palettes, Users, or any open sequence file.
  - All Sequence Files under Directory 
 —Searches in all sequence files located in the directory you specify and any subdirectories.
  - Specific Sequence Files 
 —Searches in all of the sequence files listed in the list control. Use
 Add Files 
 ,
 Remove 
 , and
 Remove All 
 to edit the list of files to search.
  - All Sequence Files in Current Workspace 
 —Searches in all sequence files the currently opened workspace contains. This option is available only when a workspace is open.
  - All Open Sequence Files 
 —Searches in all currently opened sequence files in the
 TestStand Sequence Editor 
 .
  - Recursively Search Sequence Files Called as Subsequences 
 —Specifies that for each sequence file in which you search, the search includes any subsequence files the sequence file calls.
- Display in Find Results 2 
 —TestStand displays the results of the search in the Find Results 2 pane of the sequence editor.

#### See Also

[Regular Expressions](regular-expressions.html)

Parent topic:

Find/Replace in Files Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/select-a-class-from-labview-llb-dialog-box.html language=enus -->
## TOPIC 04086: Select a Class from LabVIEW LLB Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/select-a-class-from-labview-llb-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/select-a-class-from-labview-llb-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Complete the following steps to launch the Select a Class from LabVIEW LLB dialog box, in which you can review the files the LLB file contains and select a LabVIEW class ( .lvclass ) file to open. On the LabVIEW Module tab of the Step Settings pane in the TestStand Sequence Editor or on the Module t

### Select a Class from LabVIEW LLB Dialog Box

Complete the following steps to launch the Select a Class from LabVIEW LLB dialog box, in which you can review the files the
 [LLB](/csh?context=ts_tslabview_llb)
 file contains and select a LabVIEW class (
 .lvclass
 ) file to open.

1. On the
 LabVIEW Module 
 tab of the
 Step Settings 
 pane in the
 TestStand Sequence Editor 
 or on the Module tab of the
 Edit LabVIEW VI Call 
 dialog box in a
 TestStand User Interface 
 , select the
 Class Member Call 
 option from the Call Type ring control.
2. Click the
 Browse for LabVIEW Class 
 button, located to the right of the Class Path control, to launch the
 Select the Step’s LabVIEW Class File 
 dialog box.
3. Select an LLB file and click
 Open 
 .

The select a Class from LabVIEW LLB dialog box contains the following options:

- Files contained in LLB 
 —A list of files in the LLB. The columns in this control specify the filename, whether the file is top-level, and the date modified for each file in the LLB.
- Display File Types 
 —Filters the types of files to display in the list of files in the LLB.

#### See Also

[Calling LabVIEW Class Member VIs from TestStand](/csh?context=ts_tslabview_class)

[Edit LabVIEW VI Call dialog box](edit-labview-vi-call-dialog-box.html)

[Module Tab - Step Settings Pane](module-tab-step-settings-pane.html)

[Organizing Test Program Files with LabVIEW Libraries](/csh?context=ts_tslabview_llb)

[Select a Class from LabVIEW Project dialog box](select-a-class-from-labview-project-dialog-bo.html)

[Select a Class from LabVIEW Packed Project Library dialog box](select-a-class-from-labview-packed-project-li.html)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/select-a-class-from-labview-packed-project-li.html language=enus -->
## TOPIC 04087: Select a Class from LabVIEW Packed Project Library Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/select-a-class-from-labview-packed-project-li.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/select-a-class-from-labview-packed-project-li.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Complete the following steps to launch the Select a Class from LabVIEW Packed Project Library dialog box, in which you can review the content of the packed project library file and select a LabVIEW class ( .lvclass ) file from the packed project library to open. On the LabVIEW Module tab of the Step

### Select a Class from LabVIEW Packed Project Library Dialog Box

Complete the following steps to launch the Select a Class from LabVIEW Packed Project Library dialog box, in which you can review the content of the
 [packed project library](/csh?context=ts_tslabview_ppl)
 file and select a LabVIEW class (
 .lvclass
 ) file from the packed project library to open.

1. On the
 LabVIEW Module 
 tab of the
 Step Settings 
 pane in the
 TestStand Sequence Editor 
 or on the Module tab of the
 Edit LabVIEW VI Call 
 dialog box in a
 TestStand User Interface 
 , select the
 Class Member Call 
 option from the Call Type ring control.
2. Click the
 Browse for LabVIEW Class 
 button, located to the right of the Class Path Control, to launch the
 Select the Step’s LabVIEW Class File 
 dialog box.
3. Select a LabVIEW packed project library (
 .lvlibp 
 ) file and click
 Open 
 .

Note

Calling a LabVIEW class member VI from a packed project library can be faster than calling an individual member VI independent of a packed project library. When you open a member VI from a packed project library, LabVIEW consolidates the types for all the VIs included in the packed project library during the load process. You cannot load a member VI in a packed project library independent of the other member VIs in the packed project library.

#### See Also

[Calling LabVIEW Class Member VIs from TestStand](/csh?context=ts_tslabview_class)

[Open File dialog box](open-file-dialog-box.html)

[Organizing Test Program Files with LabVIEW Packed Project Libraries](/csh?context=ts_tslabview_ppl)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/select-a-class-from-labview-project-dialog-bo.html language=enus -->
## TOPIC 04088: Select a Class from LabVIEW Project Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/select-a-class-from-labview-project-dialog-bo.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/select-a-class-from-labview-project-dialog-bo.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Complete the following steps to launch the Select a Class from LabVIEW Project dialog box, in which you can select a LabVIEW class ( .lvclass ) file to call from the specified LabVIEW project . On the LabVIEW Module tab of the Step Settings pane in the TestStand Sequence Editor or on the Module tab

### Select a Class from LabVIEW Project Dialog Box

Complete the following steps to launch the Select a Class from LabVIEW Project dialog box, in which you can select a
 [LabVIEW class](/csh?context=ts_tslabview_class)
 (
 .lvclass
 ) file to call from the specified
 [LabVIEW project](/csh?context=ts_tslabview_project)
 .

1. On the
 LabVIEW Module 
 tab of the
 Step Settings 
 pane in the
 TestStand Sequence Editor 
 or on the Module tab of the
 Edit LabVIEW VI Call 
 dialog box in a
 TestStand User Interface 
 , select the
 Class Member Call 
 option from the Call Type ring control.
2. Specify a LabVIEW project (
 .lvproj 
 ) file in the Project Path control.
3. Click the
 Browse for LabVIEW Class in LabVIEW Project 
 button, located to the right of the Class Path control.

Click the
 Refresh
 button, which is available only when TestStand has not yet loaded the LabVIEW project for execution, to reload the project control.

#### See Also

[Calling LabVIEW Class Member VIs from TestStand](/csh?context=ts_tslabview_class)

[Edit LabVIEW VI Call dialog box](edit-labview-vi-call-dialog-box.html)

[Module Tab - Step Settings Pane](module-tab-step-settings-pane.html)

[Organizing Test Program Files with LabVIEW Projects](/csh?context=ts_tslabview_project)

[Select a Class from LabVIEW Project dialog box](select-a-class-from-labview-project-dialog-bo.html)

[Select a Class from LabVIEW Packed Project Library dialog box](select-a-class-from-labview-packed-project-li.html)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/select-a-class-member-from-labview-class-dial.html language=enus -->
## TOPIC 04089: Select a Class Member From LabVIEW Class Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/select-a-class-member-from-labview-class-dial.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/select-a-class-member-from-labview-class-dial.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Complete the following steps to launch the Select a Class Member from LabVIEW Class dialog box, in which you can select a LabVIEW class member VI to call from the specified LabVIEW class. On the LabVIEW Module tab of the Step Settings pane in the TestStand Sequence Editor or on the Module tab of the

### Select a Class Member From LabVIEW Class Dialog Box

Complete the following steps to launch the Select a Class Member from LabVIEW Class dialog box, in which you can select a
 [LabVIEW class](/csh?context=ts_tslabview_class)
 member VI to call from the specified LabVIEW class.

1. On the
 LabVIEW Module 
 tab of the
 Step Settings 
 pane in the
 TestStand Sequence Editor 
 or on the Module tab of the
 Edit LabVIEW VI Call 
 dialog box in a
 TestStand User Interface 
 , select the
 Class Member Call 
 option from the Call Type ring control.
2. Specify a LabVIEW class (
 .lvclass 
 ) file in the Class Path control.
3. Click the
 Browse for LabVIEW Member 
 button, located to the right of the Member Name control.

#### See Also

[Calling LabVIEW Class Member VIs from TestStand](/csh?context=ts_tslabview_class)

[Edit LabVIEW VI Call dialog box](edit-labview-vi-call-dialog-box.html)

[Module Tab - Step Settings Pane](module-tab-step-settings-pane.html)

[Select a Class from LabVIEW Project dialog box](select-a-class-from-labview-project-dialog-bo.html)

[Select a Class from LabVIEW Packed Project Library dialog box](select-a-class-from-labview-packed-project-li.html)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/select-a-class-member-from-labview-project-di.html language=enus -->
## TOPIC 04090: Select a Class Member from LabVIEW Project Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/select-a-class-member-from-labview-project-di.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/select-a-class-member-from-labview-project-di.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Complete the following steps to launch the Select a Class Member from LabVIEW Project dialog box, in which you can select a LabVIEW class member VI to call from the specified LabVIEW project . On the LabVIEW Module tab of the Step Settings pane in the TestStand Sequence Editor or on the Module tab o

### Select a Class Member from LabVIEW Project Dialog Box

Complete the following steps to launch the Select a Class Member from LabVIEW Project dialog box, in which you can select a
 [LabVIEW class](/csh?context=ts_tslabview_class)
 member VI to call from the specified
 [LabVIEW project](/csh?context=ts_tslabview_project)
 .

1. On the
 LabVIEW Module 
 tab of the
 Step Settings 
 pane in the
 TestStand Sequence Editor 
 or on the Module tab of the
 Edit LabVIEW VI Call 
 dialog box in a
 TestStand User Interface 
 , select the
 Class Member Call 
 option from the Call Type ring control.
2. Select a LabVIEW project (
 .lvproj 
 ) file in the Project Path control.
3. Click the
 Browse for LabVIEW Class Member in LabVIEW Project 
 button, located to the right of the Member Name control.

Click the
 Refresh
 button, which is available only when TestStand has not yet loaded the LabVIEW project for execution, to reload the project control.

#### See Also

[Calling LabVIEW Class Member VIs from TestStand](/csh?context=ts_tslabview_class)

[Edit LabVIEW VI Call dialog box](edit-labview-vi-call-dialog-box.html)

[Module Tab - Step Settings Pane](module-tab-step-settings-pane.html)

[Organizing Test Program Files with LabVIEW Projects](/csh?context=ts_tslabview_project)

[Select a Class from LabVIEW Project dialog box](select-a-class-from-labview-project-dialog-bo.html)

[Select a Class from LabVIEW Packed Project Library dialog box](select-a-class-from-labview-packed-project-li.html)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/select-a-vi-dialog-box.html language=enus -->
## TOPIC 04091: Select a VI Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/select-a-vi-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/select-a-vi-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Click the Browse for VI button on the LabVIEW Module tab of the Step Settings pane in the TestStand Sequence Editor or in the Edit LabVIEW VI Call dialog box in a TestStand User Interface and double-click an LLB file to display the contents of the LLB file and launch the Select a VI dialog box. The

### Select a VI Dialog Box

Click the
 Browse for VI
 button on the
 [LabVIEW Module](labview-module-tab.html)
 tab of the
 [Step Settings](step-settings-pane.html)
 pane in the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 or in the
 [Edit LabVIEW VI Call](edit-labview-vi-call-dialog-box.html)
 dialog box in a
 [TestStand User Interface](teststand-user-interfaces.html)
 and double-click an LLB file to display the contents of the LLB file and launch the Select a VI dialog box.

The Select a VI dialog box contains the following options:

- Files contained in LLB 
 —A list of files in the LLB. This option contains two columns which display the filename and whether the file is top-level.
- Display File Types 
 —The file types to display in the list box that displays the files in the LLB.

#### See Also

[Edit LabVIEW VI Call dialog box](edit-labview-vi-call-dialog-box.html)

[LabVIEW Module Tab](labview-module-tab.html)

[Open File dialog box](open-file-dialog-box.html)

[Open Multiple File dialog box](open-multiple-file-dialog-box.html)

[Step Settings Pane](step-settings-pane.html)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/select-a-vi-from-a-labview-packed-project-lib.html language=enus -->
## TOPIC 04092: Select a VI from a LabVIEW Packed Project Library Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/select-a-vi-from-a-labview-packed-project-lib.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/select-a-vi-from-a-labview-packed-project-lib.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Double-click a LabVIEW packed project library ( .lvlibp ) file in the list control of the Open File dialog box to display the contents of the packed project library file and launch the Select a VI from a LabVIEW Packed Project Library dialog box, in which you can select a VI from the packed project

### Select a VI from a LabVIEW Packed Project Library Dialog Box

Double-click a LabVIEW packed project library (
 .lvlibp
 ) file in the list control of the
 [Open File](open-file-dialog-box.html)
 dialog box to display the contents of the packed project library file and launch the Select a VI from a LabVIEW Packed Project Library dialog box, in which you can select a VI from the packed project library to open.

Calling a VI from a packed project library is faster than calling an individual VI independent of a packed project library. When you open a VI from a packed project library, LabVIEW consolidates the types for all the VIs included in the packed project library during the load process. You cannot load a VI in a packed project library independent of the other VIs in the packed project library.

#### See Also

[Open File dialog box](open-file-dialog-box.html)

[Organizing Test Program Files with LabVIEW Packed Project Libraries](/csh?context=ts_tslabview_ppl)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/select-code-templates-to-add-to-step-type-dia.html language=enus -->
## TOPIC 04093: Select Code Templates To Add To Step Type Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/select-code-templates-to-add-to-step-type-dia.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/select-code-templates-to-add-to-step-type-dia.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Complete the following steps to launch the Select Code Templates To Add To Step Type dialog box, in which you can select one or more existing code modules to associate with the step type. Open the Types window. Launch the Step Type Properties dialog box. Click Add on the Code Templates tab. The list

### Select Code Templates To Add To Step Type Dialog Box

Complete the following steps to launch the Select Code Templates To Add To Step Type dialog box, in which you can select one or more existing
 [code modules](/csh?context=ts_tsfundamentals_bldgblocks_codemodules)
 to associate with the step type.

1. Open the
 Types 
 window.
2. Launch the
 Step Type Properties 
 dialog box.
3. Click
 Add 
 on the
 Code Templates 
 tab.

The listbox contains the code modules on disk, as well as the name and type for each code module. To associate one or more code modules in the listbox, check each item you want to associate and click
 OK
 .

#### See Also

[Step Type Properties dialog box](step-type-properties-dialog-box.html)

[Types Window](types-window.html)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/select-data-link-dialog-box.html language=enus -->
## TOPIC 04094: Select Data Link Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/select-data-link-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/select-data-link-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Click Select Data Link in the Edit Step dialog boxes for the Database step types, such as the Data Link tab of the Edit Open Database dialog box, to launch the Select Data Link dialog box. When you edit a Database step, the Edit Step dialog box might require access to the database in order to displa

### Select Data Link Dialog Box

Click
 Select Data Link
 in the Edit Step dialog boxes for the Database step types, such as the
 [Data Link](data-link-tab-edit-open-database-dialog-box.html)
 tab of the
 [Edit Open Database](edit-open-database-dialog-box.html)
 dialog box, to launch the Select Data Link dialog box.

When you edit a Database step, the Edit Step dialog box might require access to the database in order to display a list of available tables in the database or a list of columns in a table. With TestStand, you can define a set of data links you can reuse whenever you edit a Database step. A data link typically includes a name of a server, a name of a database, a user ID, and a password. You can predefine a data link to speed up the development whenever you edit a Database step.

The Select Data Link dialog box lists the currently defined data links. When you select a data link, TestStand attempts to open a connection to the data source. When TestStand successfully opens the data link, TestStand leaves the connection open for later use.

The Select Data Link dialog box contains the following options:

- New 
 or
 Edit 
 —Launches the
 Edit Data Link 
 dialog box, in which you can create new data links or edit existing data links.
- Remove 
 —Deletes the currently selected data link for the list.
- View 
 —Launches the
 Database Viewer application 
 and opens the connection string within the viewer.
- Selected Data Link is Open 
 —Indicates whether a connection is open for the currently selected data link. You can manually close an open connection by disabling the control while the data link is selected.

#### See Also

[Database Viewer](database-viewer-application.html)

[Edit Data Link dialog box](edit-data-link-dialog-box.html)

[Edit Open Database dialog box](edit-open-database-dialog-box.html)

[Configuring Connection Strings](/csh?context=ts_tsref_dbviewer_connectionstrings)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/select-directory-dialog-box.html language=enus -->
## TOPIC 04095: Select Directory Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/select-directory-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/select-directory-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: TestStand launches the Select Directory dialog box when TestStand requires you to specify the location of a directory. The Select Directory dialog box contains the following options: Directory History —A list of directories from which files were previously opened. Look In —The name of the current di

### Select Directory Dialog Box

TestStand launches the Select Directory dialog box when TestStand requires you to specify the location of a directory.

The Select Directory dialog box contains the following options:

- Directory History 
 —A list of directories from which files were previously opened.
- Look In 
 —The name of the current directory. The list control displays the contents of the current directory.
- Directory 
 —The currently selected directory.
- Use Absolute Path 
 —When you enable this option, TestStand includes the absolute path for the selected directory.

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/select-edit-tab.html language=enus -->
## TOPIC 04096: Select Edit Tab

- bundle_id: `teststand-api-reference`
- source_path: `tsref/select-edit-tab.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/select-edit-tab.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Select edit tab in the TestStand Sequence Editor to configure the Select step. The Select edit tab contains the following options: Item to Compare —The expression that determines which Case block within the Select block executes. Case Sensitive (for string values) —Specifies whether to use a

### Select Edit Tab

Use the Select edit tab in the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 to configure the Select step.

The Select edit tab contains the following options:

- Item to Compare 
 —The expression that determines which Case block within the Select block executes.
- Case Sensitive (for string values) 
 —Specifies whether to use a case-sensitive string comparison when the value for the step contains strings. The default value is
 OFF 
 , or case-insensitive.

#### See Also

[Flow Control Step Types](flow-control-step-types.html)

Parent topic:

Select Step

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/select-files-dialog-box.html language=enus -->
## TOPIC 04097: Select Files Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/select-files-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/select-files-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Select File»Select Files to Diff in the TestStand File Diff and Merge utility or click the Select Files to Diff button on the utility toolbar to launch the Select Files dialog box, in which you select the files you want to compare. The Select Files dialog box contains the following tabs: Diff —Speci

### Select Files Dialog Box

Select
 File»Select Files to Diff
 in the
 [TestStand File Diff and Merge](teststand-file-diff-and-merge-utility.html)
 utility or click the
 Select Files to Diff
 button on the utility toolbar to launch the Select Files dialog box, in which you select the files you want to compare.

The Select Files dialog box contains the following tabs:

- Diff 
 —Specify two sequence files or type palette files you want to compare.
- Merge 
 —Specify three sequence files you want to compare—a base file from which modified versions originate and two modified versions—and a fourth sequence file to become the resulting merged file to create.

Click the
 Options
 button to launch the
 [File Differ Options](file-differ-options-dialog-box.html)
 dialog box, in which you can configure settings for the utility, including options for loading and automatically merging types, managing type conflict resolution, and so on.

#### See Also

[File Differ Options dialog box](file-differ-options-dialog-box.html)

[TestStand File Diff and Merge Utility](teststand-file-diff-and-merge-utility.html)

Parent topic:

TestStand File Diff and Merge Utility

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/select-module-from-gll-dialog-box.html language=enus -->
## TOPIC 04098: Select Module From GLL Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/select-module-from-gll-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/select-module-from-gll-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Click the Browse for VI button on the LabVIEW NXG Module tab of the Step Settings pane or in the Edit LabVIEW NXG VI Call dialog box, when configuring the step using LabVIEW NXG Runtime, to launch the Select Module From GLL dialog box. The GLL Path control has the GLL path configured in the module.

### Select Module From GLL Dialog Box

Click the Browse for VI button on the
 [LabVIEW NXG Module](labview-nxg-module-tab.html)
 tab of the Step Settings pane or in the
 [Edit LabVIEW NXG VI Call](edit-labview-nxg-vi-call-dialog-box.html)
 dialog box, when configuring the step using LabVIEW NXG Runtime, to launch the Select Module From GLL dialog box.

The
 GLL Path
 control has the GLL path configured in the module. You can choose a different GLL using the Browse button, which launches a File Browse dialog. Any new GLL Path selected is set on the LabVIEW NXG module.

Use the
 search
 field to search for VIs in the GLL. 
The GLL tree view lists the following:

- The GLL name
- The Namespaces in the GLL
- The VIs contained in the Namespaces

The
 Selected Module
 control lists the Qualified Name of the VI selected in the tree view. 
When you click OK after selecting a VI in the dialog, the selected Qualified Name is set on the LabVIEW NXG Module.

#### See Also

[Edit LabVIEW NXG VI Call dialog box](edit-labview-nxg-vi-call-dialog-box.html)

[LabVIEW NXG Module tab](labview-nxg-module-tab.html)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/select-module-from-project-dialog-box.html language=enus -->
## TOPIC 04099: Select Module From Project Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/select-module-from-project-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/select-module-from-project-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Click the Browse for VI button on the LabVIEW NXG Module tab of the Step Settings pane or in the Edit LabVIEW NXG VI Call dialog box, when configuring the step using LabVIEW NXG Development System, to launch the Select Module From Project dialog box. Use this dialog box to select the VI you want to

### Select Module From Project Dialog Box

Click the
 Browse for VI
 button on the
 [LabVIEW NXG Module](labview-nxg-module-tab.html)
 tab of the Step Settings pane or in the
 [Edit LabVIEW NXG VI Call](edit-labview-nxg-vi-call-dialog-box.html)
 dialog box, when configuring the step using LabVIEW NXG Development System, to launch the Select Module From Project dialog box.

Use this dialog box to select the VI you want to call from the LabVIEW NXG project. The project tree lists the following:

- The Project
- The Targets supported by Components in the Project
- The Components under each Target
- The Namespaces under each Component
- The VIs under each Namespace.

Click the
 Refresh
 button to reload the project control tree. Use the
 Search
 field to search for VIs/Components in the project.
The
 VI Description
 pane lists the description of the VI selected in the project tree. 
The
 Selected Module
 control displays the Module Qualified Name of the selected VI. 
When you hit OK after selecting a VI in the dialog, the selected
 Module Qualified Name
 is set on the LabVIEW NXG Module.

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/select-multiple-directory-dialog-box.html language=enus -->
## TOPIC 04100: Select Multiple Directory Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/select-multiple-directory-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/select-multiple-directory-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: TestStand launches the Select Multiple Directory dialog box when TestStand requires you to specify the location of one or more directories. The Select Multiple Directory dialog box contains the following options: Directory History —A list of directories in which files were previously opened from. Lo

### Select Multiple Directory Dialog Box

TestStand launches the Select Multiple Directory dialog box when TestStand requires you to specify the location of one or more directories.

The Select Multiple Directory dialog box contains the following options:

- Directory History 
 —A list of directories in which files were previously opened from.
- Look in 
 —The name of the current directory.
- Directory 
 —The contents of the current directory.
- Use Absolute Path 
 —When you enable this option, TestStand includes the absolute path for the selected directories.
- Selected Paths 
 —The list of selected directories. Click
 Remove 
 to delete the selected item from the list, or click
 Remove All 
 to delete all items from the list.

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/select-sequence-file-callbacks-dialog-box.html language=enus -->
## TOPIC 04101: Select Sequence File Callbacks Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/select-sequence-file-callbacks-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/select-sequence-file-callbacks-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Select Edit»Sequence File Callbacks to launch the Select Sequence File Callbacks dialog box, which lists every callback sequence you can override in the sequence file. The columns in the list display the name of the callback and indicate whether the callback is an Engine or Model callback. For each

### Select Sequence File Callbacks Dialog Box

Select
 Edit»Sequence File Callbacks
 to launch the Select Sequence File Callbacks dialog box, which lists every callback sequence you can override in the sequence file. The columns in the list display the name of the callback and indicate whether the callback is an
 [Engine](/csh?context=ts_tsfundamentals_engine_callbacks)
 or
 [Model](/csh?context=ts_tsfundamentals_bldgblocks_callbacksequences)
 callback. For each callback, select or clear the checkbox to add or remove it from the sequence file.

The following restrictions apply to the SequenceFileLoad and SequenceFileUnload callbacks:

- TestStand may hang when it executes a SequenceFileLoad callback that calls into another sequence file which contains a SequenceFileLoad callback that calls back into the original sequence file. This can occur with any number of levels of sequence files as long as the dependencies among the SequenceFileLoad callbacks exist between sequence files.
- TestStand may enter an infinite loop when it executes a SequenceFileUnload callback that calls into another sequence file which contains a SequenceFileUnload callback that calls back into the original sequence file. Select
 Debug»Terminate All 
 to break the infinite loop.
- Do not define a SequenceFileLoad or SequenceFileUnload callback in the
 StationCallbacks.seq 
 sequence file. TestStand does not call these callbacks.

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/select-sequence-file-dialog-box.html language=enus -->
## TOPIC 04102: Select Sequence File Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/select-sequence-file-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/select-sequence-file-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Select Edit»Diff Sequence File Against when a Sequence File window is active in the TestStand Sequence Editor and more than one sequence file is opened in the sequence editor to launch the Select Sequence File dialog box, in which you can select a second sequence file to diff against the sequence fi

### Select Sequence File Dialog Box

Select
 Edit»Diff Sequence File Against
 when a Sequence File window is active in the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 and more than one sequence file is opened in the sequence editor to launch the Select Sequence File dialog box, in which you can select a second sequence file to diff against the sequence file associated with the active window. The sequence editor displays the differences between the two sequence files in the
 [TestStand File Diff and Merge](teststand-file-diff-and-merge-utility.html)
 utility.

The Select Sequence File dialog box contains the following option:

- Select Opened Sequence File to Diff 
 —The currently opened sequence files in the sequence editor. The sequence file associated with the active window is not included in the list.

Click the
 File Browse
 button to select a sequence file from disk instead of using a sequence file the sequence editor already loaded. When you have made modifications to a file, you can select the version of the file on disk to compare to the file you are modifying.

#### See Also

[TestStand File Diff and Merge Utility](teststand-file-diff-and-merge-utility.html)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/select-session-dialog-box.html language=enus -->
## TOPIC 04103: Select Session Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/select-session-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/select-session-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use this dialog box to choose the specific sessions to close. You can choose an existing Create Session and Apply Configuration step, or specific IO session variables defined as Locals, Parameters, FileGlobals, or StationGlobals. This dialog allows you to filter the available sessions through the se

### Select Session Dialog Box

Use this dialog box to choose the specific sessions to close. You can choose an existing Create Session and Apply Configuration step, or specific IO session variables defined as Locals, Parameters, FileGlobals, or StationGlobals. This dialog allows you to filter the available sessions through the search box and select multiple sessions to close.

Parent topic:

Close Sessions Step

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/select-step.html language=enus -->
## TOPIC 04104: Select Step

- bundle_id: `teststand-api-reference`
- source_path: `tsref/select-step.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/select-step.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use a Select step to define a block of steps that encloses sub-blocks Case steps define. The Select step specifies an expression that determines which Case block executes. Configuring the Step Use the Select edit tab in the TestStand Sequence Editor and the Configure Select dialog box in a TestStand

### Select Step

Use a Select step to define a block of steps that encloses sub-blocks
 [Case](case-step.html)
 steps define. The Select step specifies an expression that determines which Case block executes.

#### Configuring the Step

Use the
 [Select](select-edit-tab.html)
 edit tab in the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 and the
 [Configure Select](configure-select-dialog-box.html)
 dialog box in a
 [TestStand User Interface](teststand-user-interfaces.html)
 to configure the Select step.

#### Step Properties

In addition to the
 [common custom properties](/csh?context=ts_tsfundamentals_custom_result_props)
 , the Select step type defines the following step property:

- Step.ItemExpr 
 —The expression that determines which Case block within the Select block executes.

#### See Also

[Flow Control Step Types](flow-control-step-types.html)

Parent topic:

Flow Control Step Types

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/select-types-dialog-box.html language=enus -->
## TOPIC 04105: Select Types Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/select-types-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/select-types-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Enable the Search Only Within Objects that are Instances of the Following Types option and click Select on the Filter tab of the Find in Files dialog box to launch the Select Types dialog box, in which you can select a subset of the types currently loaded in memory. Use the <Shift> and <Ctrl> keys t

### Select Types Dialog Box

Enable the
 Search Only Within Objects that are Instances of the Following Types
 option and click
 Select
 on the
 [Filter](filter-tab-find-replace-in-files-dialog-box.html)
 tab of the
 [Find in Files](find-replace-in-files-dialog-box.html)
 dialog box to launch the Select Types dialog box, in which you can select a subset of the types currently loaded in memory. Use the <Shift> and <Ctrl> keys to select more than one type in the list.

#### See Also

[Find in Files dialog box](find-replace-in-files-dialog-box.html)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/select-variable-or-session-dialog-box.html language=enus -->
## TOPIC 04106: Select Variable or Session Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/select-variable-or-session-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/select-variable-or-session-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Launch the Select Variable or Session dialog box by clicking Select Variable in the Parameter Value/Session column . The dialog box shows all available variables. Find a specific value by searching or filtering by name or type. This dialog box contains the following tabs: Variables —Lists variables

### Select Variable or Session Dialog Box

Launch the Select Variable or Session dialog box by clicking Select Variable in the
 [Parameter Value/Session column](sweep-parameters-tab.html)
 . The dialog box shows all available variables. Find a specific value by searching or filtering by name or type.

This dialog box contains the following tabs:

- Variables 
 —Lists variables of types other than I/O Session. This tab has the following options:
  - Filter:Name 
 —Enter text to filter the variables by name.
  - Filter:Type 
 —Select the data type to filter variables with. By default, this filter matches the parameter data type.
- Sessions 
 —Lists all variables of type IO Session. This tab has the following option:
  - Filter:Name 
 —Enter text to filter the variables by name.

Note

This dialog box contains the following option:

- Selected 
 —Shows the selected variable. Invalid types, such as containers, cannot be selected.

Parent topic:

Sweep Loop Step

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/select-vi-from-labview-project-dialog-box.html language=enus -->
## TOPIC 04107: Select VI From LabVIEW Project Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/select-vi-from-labview-project-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/select-vi-from-labview-project-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Click the Browse for VI in LabVIEW Project button on the LabVIEW Module tab of the Step Settings pane or in the Edit LabVIEW VI Call dialog box to launch the Select VI From LabVIEW Project dialog box. Use this dialog box to select the VI you want to call from the LabVIEW project control. Click the R

### Select VI From LabVIEW Project Dialog Box

Click the
 Browse for VI in LabVIEW Project
 button on the
 [LabVIEW Module](labview-module-tab.html)
 tab of the Step Settings pane or in the
 [Edit LabVIEW VI Call](edit-labview-vi-call-dialog-box.html)
 dialog box to launch the Select VI From LabVIEW Project dialog box.

Refresh

Search Project

Note

Refresh

#### See Also

[Edit LabVIEW VI Call dialog box](edit-labview-vi-call-dialog-box.html)

[LabVIEW Module tab](labview-module-tab.html)

[Organizing Test Program Files with LabVIEW Projects](/csh?context=ts_tslabview_project)

Parent topic:

LabVIEW Module Tab

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/self-test-operation-edit-ivi-tools-step-dialo.html language=enus -->
## TOPIC 04108: Self Test Operation - Edit IVI Tools Step Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/self-test-operation-edit-ivi-tools-step-dialo.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/self-test-operation-edit-ivi-tools-step-dialo.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Self Test Operation The Self Test operation causes the instrument to perform a self-test. The operation waits for the instrument to complete the test. It then queries the instrument for the results and returns them. The Self Test operation contains the following options: Test Result —A variable or p

### Self Test Operation - Edit IVI Tools Step Dialog Box

#### Self Test Operation

The Self Test operation causes the instrument to perform a self-test. The operation waits for the instrument to complete the test. It then queries the instrument for the results and returns them.

The Self Test operation contains the following options:

- Test Result 
 —A variable or property to which the step assigns the numeric result from the self-test. Returns
 0 
 for no error (test passed).
- Test Message 
 —A variable or property to which the step assigns the self-test status message.

Parent topic:

Edit IVI Tools Step Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/semaphore-settings-edit-tab.html language=enus -->
## TOPIC 04109: Semaphore Settings Edit Tab

- bundle_id: `teststand-api-reference`
- source_path: `tsref/semaphore-settings-edit-tab.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/semaphore-settings-edit-tab.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Insert a Semaphore step and select Edit Semaphore Settings or Step Settings from the context menu to display the Semaphore Settings edit tab in the TestStand Sequence Editor . The following operations are available when you use the Semaphore step type: Create —Creates a reference to a new or existin

### Semaphore Settings Edit Tab

Insert a Semaphore step and select
 Edit Semaphore Settings
 or
 Step Settings
 from the context menu to display the Semaphore Settings edit tab in the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 .

The following operations are available when you use the Semaphore step type:

- Create 
 —Creates a reference to a new or existing Semaphore object.
- Acquire (decrement) 
 —You must perform this operation before you access a resource a semaphore protects.
- Release (increment) 
 —Gives you direct control over the count. You can also use this operation to use semaphores in a way that requires unmatched increments and decrements.
 Note 
 If you enable Auto Release in the Acquire operation, do not explicitly release the semaphore using the Release operation.
- Get Status 
 —Obtains information about the current state of the semaphore.

#### See Also

[Synchronization Step Types](synchronization-step-types.html)

Parent topic:

Semaphore Step

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/semaphore-step-configuration-dialog-box.html language=enus -->
## TOPIC 04110: Semaphore Step Configuration Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/semaphore-step-configuration-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/semaphore-step-configuration-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Select Configure Semaphore in the context menu for the step to launch the Semaphore Step Configuration dialog box from a TestStand User Interface . You can also click Configure Semaphore on the General tab of the Step Properties dialog box. In the Semaphore Step Configuration dialog box, select an o

### Semaphore Step Configuration Dialog Box

Select
 Configure Semaphore
 in the context menu for the step to launch the Semaphore Step Configuration dialog box from a
 [TestStand User Interface](teststand-user-interfaces.html)
 . You can also click
 Configure Semaphore
 on the
 [General](general-tab-step-properties-dialog-box.html)
 tab of the
 [Step Properties](step-properties-dialog-box.html)
 dialog box. In the Semaphore Step Configuration dialog box, select an operation for the step to perform.

The following operations are available when you use the Semaphore step type:

- Create 
 —Creates a reference to a new or existing Semaphore object.
- Acquire (decrement) 
 —You must perform this operation before you access a resource a semaphore protects.
- Release (increment) 
 —Gives you direct control over the count. You can also use this operation to control semaphores in a way that requires unmatched increments and decrements.
 Note 
 If you enable Auto Release in the Acquire operation, do not explicitly release the semaphore using the Release operation.
- Get Status 
 —Obtains information about the current state of the semaphore.

#### See Also

[Step Properties dialog box](step-properties-dialog-box.html)

[Synchronization Step Types](synchronization-step-types.html)

Parent topic:

Semaphore Step

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/semaphore-step.html language=enus -->
## TOPIC 04111: Semaphore Step

- bundle_id: `teststand-api-reference`
- source_path: `tsref/semaphore-step.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/semaphore-step.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use a Semaphore step to limit concurrent access to a resource to a specific number of threads. A semaphore stores a numeric count, and threads can increment (release) or decrement (acquire) the count as long as the count stays equal to or greater than zero. When a decrement causes the count to drop

### Semaphore Step

Use a Semaphore step to limit concurrent access to a resource to a specific number of threads. A semaphore stores a numeric count, and threads can increment (release) or decrement (acquire) the count as long as the count stays equal to or greater than zero. When a decrement causes the count to drop below zero, the thread that attempts to decrement the count blocks until the count increases. When multiple threads wait to decrement a semaphore and another thread increments the count, the semaphore unblocks the threads in first-in first-out order.

A semaphore with an initial count of one behaves like a
 [lock](lock-step.html)
 because a one-count semaphore restricts access to a single thread at a time. Unlike a lock, however, a thread cannot acquire a one-count semaphore multiple times without first releasing the semaphore after each acquire. When a thread attempts to acquire the semaphore a second time without releasing it, the count is zero, and the thread blocks.

#### Configuring the Step

Use the
 [Semaphore Settings](semaphore-settings-edit-tab.html)
 edit tab in the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 and the
 [Semaphore Step Configuration](semaphore-step-configuration-dialog-box.html)
 dialog box in a
 [TestStand User Interface](teststand-user-interfaces.html)
 to configure the Semaphore step.

#### Step Properties

In addition to the
 [common custom properties](/csh?context=ts_tsfundamentals_custom_result_props)
 , the Semaphore step type defines the following step properties:

- Step.Result.TimeoutOccurred 
 —Exists only when you configure the step for the
 Acquire 
 operation. TestStand sets the value to
 True 
 when the Acquire operation times out.
 Note 
 If you configure the step to use the Acquire operation programmatically using the
 Step.Operation
 property, you must also create the
 Step.Result.TimeoutOccurred
 property using the
 newProperty(
 ) method for the step to execute successfully.
- Step.NameOrRefExpr 
 —Contains the Semaphore
 Name 
 expression for the
 Create 
 operation and the Semaphore Name or Reference expression for all other Semaphore operations.
- Step.AutoRelease 
 —A Boolean value that specifies whether the Acquire operation automatically performs a release when the Acquire lifetime expires.
- Step.LifetimeRefExpr 
 —The object reference expression for the Semaphore Reference
 Lifetime 
 or the Acquire Reference Lifetime when you set either lifetime to
 Use Object Reference 
 .
- Step.TimeoutEnabled 
 —The
 Timeout 
 Enabled setting for the Acquire operation.
- Step.TimeoutExpr 
 —The Timeout expression, in seconds, for the Acquire operation.
- Step.ErrorOnTimeout 
 —The Timeout Causes Run-Time Error setting for the Acquire operation.
- Step.AlreadyExistsExpr 
 —Contains the Already Exists expression for the Create operation or the Semaphore Exists expression for the Get Status operation.
- Step.InitialCountExpr 
 —The Initial Semaphore Count expression for the Create operation.
- Step.NumThreadsWaitingExpr 
 —The Number of Threads Waiting to Acquire the Semaphore expression for the
 Get Status 
 operation.
- Step.Operation 
 —A value that specifies the operation for the step to perform. The valid values are
 0 
 = Set Thread Priority and
 1 
 = Get Thread Priority.
- Step.Lifetime 
 —A value that specifies the lifetime setting to use for the Create operation. The valid values are
 0 
 = Same as Sequence,
 1 
 = Same as Thread,
 2 
 = Use Object Reference, and
 3 
 = Same as Execution.
- Step.InitialCountOutExpr 
 —The Initial Semaphore Count expression for the Get Status operation.
- Step.AcquireLifetime 
 —A value that specifies the lifetime setting for the Acquire operation. The valid values are
 0 
 = Same as Sequence,
 1 
 = Same as Thread, and
 2 
 = Use Object Reference. The Acquire operation uses this setting only when
 Step.AutoRelease 
 is
 True 
 .
- Step.CurrentCountExpr 
 —The Current Count expression for the Get Status operation.

#### See Also

[Controlling Multi-Threaded Execution Flow with Rendezvous and Semaphore Steps (Example)](/csh?context=ts_8185)

[Synchronization Step Types](synchronization-step-types.html)

Parent topic:

Synchronization Step Types

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/send-software-trigger-operation-ivi-switching.html language=enus -->
## TOPIC 04112: Send Software Trigger Operation (IVI Switching Mode) - Edit IVI Switch Step Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/send-software-trigger-operation-ivi-switching.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/send-software-trigger-operation-ivi-switching.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Send Software Trigger Operation (IVI Switching Mode) The Send Software Trigger operation sends a software command to trigger the instrument. The Send Software Trigger operation does not affect the behavior of the instrument when the Trigger Input option is not set to Software.

### Send Software Trigger Operation (IVI Switching Mode) - Edit IVI Switch Step Dialog Box

#### Send Software Trigger Operation (IVI Switching Mode)

The Send Software Trigger operation sends a software command to trigger the instrument. The Send Software Trigger operation does not affect the behavior of the instrument when the Trigger Input option is not set to Software.

Parent topic:

IVI Switching Mode - Edit IVI Switch Step Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/send-sw-trigger-operation-edit-ivi-dmm-step-d.html language=enus -->
## TOPIC 04113: Send SW Trigger Operation - Edit IVI Dmm Step Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/send-sw-trigger-operation-edit-ivi-dmm-step-d.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/send-sw-trigger-operation-edit-ivi-dmm-step-d.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Send Software Trigger Operation The Send Software Trigger operation sends a software trigger command to trigger the instrument. This operation affects the behavior of the instrument when the Trigger Source setting is set to Software Trig and when the Software Trigger extension is enabled. This opera

### Send SW Trigger Operation - Edit IVI Dmm Step Dialog Box

#### Send Software Trigger Operation

The Send Software Trigger operation sends a software trigger command to trigger the instrument. This operation affects the behavior of the instrument when the Trigger Source setting is set to Software Trig and when the Software Trigger extension is enabled. This operation does not check the instrument status. Typically, this operation is only called in a sequence of calls to other low-level driver operations, such as the Initiate operation.

Parent topic:

Edit IVI Dmm Step Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/send-sw-trigger-operation-edit-ivi-fgen-step.html language=enus -->
## TOPIC 04114: Send SW Trigger Operation - Edit IVI Fgen Step Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/send-sw-trigger-operation-edit-ivi-fgen-step.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/send-sw-trigger-operation-edit-ivi-fgen-step.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Send Software Trigger Operation Sends a software trigger command to trigger the instrument. This operation sends a software trigger when a Trigger Source setting is set to Software Trigger. You must enable the Software Trigger extension to use this option.

### Send SW Trigger Operation - Edit IVI Fgen Step Dialog Box

#### Send Software Trigger Operation

Sends a software trigger command to trigger the instrument. This operation sends a software trigger when a Trigger Source setting is set to Software Trigger.

Note

Parent topic:

Edit IVI Fgen Step Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/send-sw-trigger-operation-edit-ivi-power-supp.html language=enus -->
## TOPIC 04115: Send SW Trigger Operation - Edit IVI Power Supply Step Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/send-sw-trigger-operation-edit-ivi-power-supp.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/send-sw-trigger-operation-edit-ivi-power-supp.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Send Software Trigger Operation Updates the voltage level and current limit when a DC power supply is in the wait for trigger state. This operation sends a software trigger when the Trigger Source setting is set to Software. After the trigger occurs, the voltage level and current limit are updated w

### Send SW Trigger Operation - Edit IVI Power Supply Step Dialog Box

#### Send Software Trigger Operation

Updates the voltage level and current limit when a DC power supply is in the wait for trigger state. This operation sends a software trigger when the Trigger Source setting is set to Software. After the trigger occurs, the voltage level and current limit are updated with the values of triggered current limit and the triggered voltage level.

Note

Parent topic:

Edit IVI Power Supply Step Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/sequence-adapter-configuration-dialog-box.html language=enus -->
## TOPIC 04116: Sequence Adapter Configuration Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/sequence-adapter-configuration-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/sequence-adapter-configuration-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Select Configure»Adapters , select the Sequence Adapter in the list control, and click Configure to launch the Sequence Adapter Configuration dialog box. The Sequence Adapter Configuration dialog box contains the following option: Show Arguments in Step Description —Specifies whether the description

### Sequence Adapter Configuration Dialog Box

Select
 Configure»Adapters
 , select the Sequence Adapter in the list control, and click
 Configure
 to launch the Sequence Adapter Configuration dialog box.

The Sequence Adapter Configuration dialog box contains the following option:

- Show Arguments in Step Description 
 —Specifies whether the description for the step displays the parameters for the sequence.

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/sequence-analyzer-options-dialog-box.html language=enus -->
## TOPIC 04117: Sequence Analyzer Options Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/sequence-analyzer-options-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/sequence-analyzer-options-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Click the Sequence Analyzer Options button in the Analysis Results pane or select Debug»Sequence Analyzer»Sequence Analyzer Options to launch the Sequence Analyzer Options dialog box. The sequence editor requires an enabled ConfigApp user privilege to change some options in the Sequence Analyzer Opt

### Sequence Analyzer Options Dialog Box

Sequence Analyzer Options

Analysis Results pane

Debug»Sequence Analyzer»Sequence Analyzer Options

Note

ConfigApp user privilege

The Sequence Analyzer Options dialog box contains the following options:

- Analyze File Before Executing 
 —Enable this option to
 analyze the active sequence file 
 when you initiate an execution. You can also click the
 Toggle Analyze File Before Executing 
 button on the Sequence Analyzer toolbar or select
 Debug»Sequence Analyzer»Toggle Analyze File Before Executing 
 to enable or disable this option. Enabling this option can help you find errors early during development. When you enable this option and the analysis of the active sequence file takes longer than a few seconds, the sequence editor launches the Analyzing Sequence File dialog box to show the progress and allow you to stop analysis.
- Cache Sequence File During Analysis 
 —Keep sequence files loaded in memory during analysis to improve performance. When you enable this option, the TestStand Sequence Analyzer keeps sequence files loaded in memory until the analysis session completes or until limited available memory exists on the computer. When you disable this option, the sequence analyzer unloads each sequence file immediately after analysis.
 Note 
 When this option is enabled, type conflicts might occur between the types in the cached sequence files. As a result, you might obtain different results when analyzing a project with this option enabled than when you analyze the project with it disabled.
- Current Project Settings 
 —Contains the following options for the current analyzer project:
  - Project Path 
 —The path of the current analyzer project. You can change the path of the current analyzer project by selecting
 File»Save <
 filename
 > As 
 when the
 Current Sequence Analyzer Project 
 window is active.
  - Analyze Skipped Steps 
 —Enable this option to analyze steps for which you set the Run Mode option to Skip.
  - Analyze Subsequences 
 —Enable this option to analyze sequence files that
 Sequence Call steps 
 call from analyzed sequence files. When you use
 expressions 
 in Sequence Call steps to call sequence files, you must add each file to the Sequence Files to Analyze list on the
 Files 
 pane of the Current Sequence Analyzer Project window separately.
  - Analyze Model Sequence Files 
 —Enable this option to analyze process model sequence files associated with analyzed sequence files.
  - Automatically Save Project File 
 —Enable this option to automatically save the project file when you close the file in the
 TestStand Sequence Editor 
 or stand-alone
 TestStand Sequence Analyzer application 
 . The default project (
 MyAnalyzerProject.tsaproj 
 ) the sequence editor creates at first launch enables this option. The sequence analyzer disables this option for all other analyzer project files you create.
- Available Rules 
 —Launch the
 Configure Sequence Analyzer Available Rules 
 dialog box, in which you create and edit
 custom analyzer rules 
 and
 analysis modules 
 .

#### See Also

[Analyzing a Sequence File or Workspace File in the TestStand Sequence Editor](/csh?context=ts_tsref_sa_analyzing_se)

[Configure Sequence Analyzer Available Rules dialog box](configure-sequence-analyzer-available-rules-d.html)

[Creating Analysis Modules for Custom Rules](/csh?context=ts_tsref_sa_creating_analysis_modules)

[Creating Custom Rules](/csh?context=ts_tsref_sa_creating_custom_rules)

[Current Sequence Analyzer Project Window](current-sequence-analyzer-project-window.html)

[Sequence Call Step](sequence-call-step.html)

[TestStand Sequence Analyzer Application](teststand-sequence-analyzer-application.html)

[Toolbar Buttons and Shortcuts](toolbar-buttons-and-shortcuts.html)

[User and Group Privileges](user-and-group-privileges.html)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/sequence-analyzer-options-dialog-box2.html language=enus -->
## TOPIC 04118: Sequence Analyzer Options Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/sequence-analyzer-options-dialog-box2.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/sequence-analyzer-options-dialog-box2.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: In the TestStand Sequence Analyzer, select Edit»Sequence Analyzer Options to launch the Sequence Analyzer Options dialog box, which contains the following options: Cache Sequence File During Analysis —Keep sequence files loaded in memory during analysis to improve performance. When you enable this o

### Sequence Analyzer Options Dialog Box

In the TestStand Sequence Analyzer, select
 Edit»Sequence Analyzer Options
 to launch the Sequence Analyzer Options dialog box, which contains the following options:

- Cache Sequence File During Analysis 
 —Keep sequence files loaded in memory during analysis to improve performance. When you enable this option, the TestStand Sequence Analyzer keeps sequence files loaded in memory until the analysis session completes or until limited available memory exists on the computer. When you disable this option, the sequence analyzer unloads each sequence file immediately after analysis.
 Note 
 When this option is enabled, type conflicts might occur between the types in the cached sequence files. As a result, you might obtain different results when analyzing a project with this option enabled than when you analyze the project with it disabled.

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/sequence-call-advanced-settings-window.html language=enus -->
## TOPIC 04119: Sequence Call Advanced Settings Window

- bundle_id: `teststand-api-reference`
- source_path: `tsref/sequence-call-advanced-settings-window.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/sequence-call-advanced-settings-window.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: To launch the Sequence Call Advanced Settings window in the TestStand Sequence Editor , add a Sequence Call step to the sequence file. Then, select Specify Module from the context menu to open the Module tab and click the Configure Execution Option button. The options on the window change depending

### Sequence Call Advanced Settings Window

To launch the Sequence Call Advanced Settings window in the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 , add a Sequence Call step to the sequence file. Then, select
 Specify Module
 from the context menu to open the
 [Module](sequence-call-module-tab.html)
 tab and click the
 Configure Execution Option
 button.

The options on the window change depending on the execution option you select. The following options are available:

- Use New Thread
- Use New Execution
- Use Remote Computer

Parent topic:

Sequence Call Module Tab

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/sequence-call-module-tab.html language=enus -->
## TOPIC 04120: Sequence Call Module Tab

- bundle_id: `teststand-api-reference`
- source_path: `tsref/sequence-call-module-tab.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/sequence-call-module-tab.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: To display the Sequence Call Module edit tab in the TestStand Sequence Editor , insert a Sequence Call step or configure a step to use the Sequence Adapter and select Specify Module or Step Settings from the context menu. The Sequence Call Module edit tab contains the following options: File Pathnam

### Sequence Call Module Tab

To display the Sequence Call Module edit tab in the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 , insert a Sequence Call step or configure a step to use the Sequence Adapter and select
 Specify Module
 or
 Step Settings
 from the context menu. The Sequence Call Module edit tab contains the following options:

- File Pathname 
 —The pathname of the sequence file or a reference to a
 SequenceFile 
 object. This option is available only when you disable the
 Specify By Expression 
 option.
- File Path or Reference 
 —The expression for the sequence file pathname. This control is available only when you enable the Specify By Expression option and takes the place of the File Pathname control.
- Sequence 
 —The name of the sequence in the sequence file you specify. When you use
 expressions 
 , use this option to specify an expression for the sequence name.
- Sequence Comment 
 —The comment associated with the sequence that the step calls.
- Client Path or Reference 
 —The pathname or reference of the client sequence filename when the step runs the sequence in a new execution and the
 Execution Settings 
 specifies to use a process model. This control is available only when you select Use New Execution in Execution Options.
- File Path or Reference 
 —The expression for the client sequence file. This control is available only when you enable Specify By Expression and takes the place of the Client Path or Reference control when you select Use New Execution in Execution Options.
- Model Pathname 
 —The pathname or reference of the model sequence file when the step runs the sequence in a new execution and the
 Execution Settings 
 specifies to use a process model. When you use expressions, use this option to specify an expression for the client sequence file. This control is available only when you select Use New Execution in the Execution Options control of the
 Sequence Call Advanced Settings 
 window.
- Model Path or Reference 
 —An expression for the client sequence file. This control is available only when you select Use New Execution in Execution Options and enable Specify By Expression. This control takes the place of the Model Pathname control.
- Entry Point 
 —The name of the entry point when the step runs the sequence in a new execution and the Execution Settings dialog box specifies to use a process model. When you use expressions, use this option to specify an expression for the entry point name. This control is available only when you select Use New Execution in Execution Options.
- Entry Point Comment 
 —The comment associated with the entry point sequence that the step calls.
- Specify By Expression 
 —Enable this option to specify that the sequence name and sequence file pathname are expressions that TestStand evaluates at run time. When you use literal strings, you enter the actual pathname of the sequence file in the File Pathname control. When you enable this option, you cannot use the Use Prototype of Sequence option. When you use expressions, you specify an expression in the Sequence control.
 Note 
 If the Sequence Call step specifies the
 Preload when opening sequence file
 or
 Preload when execution begins
 [load option](run-options-panel-step-settings-pane.html)
 , and you enable the Specify By Expression option for the step or the step
 [calls a custom sequence file](/csh?context=ts_tsfundamentals_translators)
 , TestStand does not preload the
 [code module](/csh?context=ts_tsfundamentals_bldgblocks_codemodules)
 and behaves as if you selected the
 Load dynamically
 load option for the step.
- Use Current File 
 —When you enable this option, the step calls a sequence in the sequence file you are currently editing. The File Pathname or File Path or Reference control dims when you enable this option.
- Execution Options 
 —Launches a floating pane in which you can configure multithreading and remote execution settings. The floating pane varies according to the selection you make in the Execution Options ring control. The following options are available in the ring control:
  - None 
 —Calls the sequence synchronously without using a new thread or execution. The calling sequence waits until the called sequence completes. This is the default setting.
  - Use New Thread 
 —Runs the sequence in a new thread.
  - Use New Execution 
 —Runs the sequence in a new execution.
  - Use Remote Computer 
 —Runs the sequence on a remote computer.
 Note 
 TestStand does not support remotely executing a sequence across different TestStand versions, for example, remotely executing a TestStand 2013 sequence from a computer running TestStand 2010.
- Use Prototype of Sequence 
 —Enable this option to specify to update the contents of the Parameters Table control whenever you select a different sequence from the Sequence ring control. This option is not available when you enable the Specify by Expression option. When this option is disabled, use the
 Load Prototype 
 button to update the contents of the Parameters Table by selecting the parameters from an existing sequence.
- Load Prototype 
 —Loads a prototype from a sequence that has the same parameter list definition as the sequences the step might call. Use this button to update the contents of the Parameters Table when you enable the Specify By Expression option.
 Note 
 Load Prototype
 does not support parameters that have the
 shared
 flag set. Such parameters will be excluded. Enable
 Use Prototype of Sequence
 instead to also include parameters that have the
 shared
 flag set.
- Parameters 
 —The Parameters section contains the following items:
 
 Note 
 When you call a sequence on a remote host, you can pass single-valued properties or arrays of number, Boolean, and string properties by value or by reference. You can also pass container properties or object reference properties to a remote sequence if the receiving parameter type is an object reference property.
  - Parameters Table 
 —Displays the parameters the step passes to the sequence. The contents of the Parameters Table control must be consistent with the parameter definitions in the sequence the step calls. You must extract the parameter definitions from the sequence or from another sequence that has the same parameter list.
 The Parameters Table control contains the following columns: 
 
 Although the parameter list the step uses must be consistent with the parameter list the sequence defines, the step can specify fewer or more parameters than the sequence specifies. The data types for the parameters in the step must be compatible with the corresponding parameters in the sequence. The Sequence Adapter uses the default values for the parameters the step does not pass explicitly. The Sequence Adapter passes additional parameters if the step defines more parameters than the sequence specifies. 
 When you use the Load Prototype button on the Module tab of the Step Settings pane of a Sequence Call step to load prototype information from a different sequence and the sequence from which you load the prototype includes the same parameters as the original sequence plus additional parameters, TestStand passes the additional parameters to the sequence you call.
    - Name 
 —A symbolic name for the parameter.
 Note 
 Parameters with attributes include an Edit Attributes button in the Name column of the Parameters Table. TestStand associates parameter attributes with the module parameter, which TestStand stores with the step configuration information, not with the parameter value that TestStand passes to the module. Right-click an item in the Parameters Table to access the
 [Parameters Table](for-module-tabs-parameters-table-context-menu.html)
 context menu, from which you can launch the
 [Attributes](attributes-dialog-box.html)
 dialog box.
    - Type 
 —The TestStand data type for the parameter.
    - Log 
 —When you enable this option, the step logs the parameter as an additional result. Enabling this option is equivalent to using the checkbox next to the additional result name on the
 Additional Results panel 
 of the
 Properties 
 tab of the
 Step Settings 
 pane. For in/out parameters, enabling this option enables the [In] parameter and the [Out] parameter on the Additional Results panel. This option is indeterminate for in/out parameters if you specify to log only the [In] parameter value or only the [Out] parameter value. If this option is indeterminate, a tooltip specifies whether the Additional Results panel specifies to log the [In] parameter value or the [Out] parameter value.
    - Use Default 
 —When you enable this option, the step passes the default value the sequence defines for the parameter.
    - Value 
 —The argument the step passes for a parameter. You can specify an expression TestStand evaluates at run time.
 Note 
 When you pass an array to a sequence, the Sequence Adapter does not alter the array bounds. For example, if a sequence defines a parameter with bounds [
 0..2
 ] and a Sequence Call step passes an array with bounds [
 3..5
 ], the called sequence must access the array with bounds [
 3..5
 ], not [
 0..2
 ].
    - How Passed 
 —Specifies whether the step passes the parameter by value or by reference. If the step passes the parameter by reference, the subsequence can change the value of the parameter argument. The parameter definition in the sequence determines whether the step passes the argument by value or by reference.
    - Comment 
 —The comment associated with the parameter for the sequence that the step calls.

#### See Also

[Attributes dialog box](attributes-dialog-box.html)

[Built-In Step Types](built-in-step-types.html)

[Parameters Table Context Menu for Module Tabs](for-module-tabs-parameters-table-context-menu.html)

[Sequence Call Advanced Settings Window](sequence-call-advanced-settings-window.html)

[Sequence File Translators](/csh?context=ts_tsfundamentals_translators)

[SequenceFile](../tsapiref/sequencefile.html)

[Step Settings Pane](step-settings-pane.html)

[Remote Execution in 32-bit TestStand and 64-bit TestStand](/csh?context=ts_tsfundamentals_64remoteexecution)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/sequence-call-step.html language=enus -->
## TOPIC 04121: Sequence Call Step

- bundle_id: `teststand-api-reference`
- source_path: `tsref/sequence-call-step.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/sequence-call-step.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Sequence Call step to call another sequence in the current sequence file or in another sequence file. The Sequence Call step always uses the Sequence Adapter . Configuring the Step Use the Sequence Call Module edit tab in the TestStand Sequence Editor and the Edit Sequence Call dialog box in

### Sequence Call Step

Use the Sequence Call step to call another sequence in the current sequence file or in another sequence file. The Sequence Call step always uses the
 [Sequence Adapter](/csh?context=ts_tsref_sequence)
 .

#### Configuring the Step

Use the
 [Sequence Call Module](sequence-call-module-tab.html)
 edit tab in the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 and the
 [Edit Sequence Call](edit-sequence-call-dialog-box.html)
 dialog box in a
 [TestStand User Interface](teststand-user-interfaces.html)
 to configure the Sequence Call step.

#### Step Properties

The Sequence Call step type does not define any additional step properties other than the
 [common custom properties](/csh?context=ts_tsfundamentals_custom_result_props)
 all steps contain. TestStand adds the following properties at runtime to the results for Sequence Call steps in sequences you configured to run in a new thread or execution.

- AsyncMode 
 —Set to
 True 
 when the Sequence Call step ran the sequence in a new thread. Set to
 False 
 if the Sequence Call step ran the sequence in a new execution.
- AsyncID 
 —The value of the
 ID 
 property of the thread or execution running the sequence.

#### See Also

[Built-In Step Types](built-in-step-types.html)

[Executing Sequences in Parallel (Example)](/csh?context=ts_8115)

[Sequence Adapter](/csh?context=ts_tsref_sequence)

Parent topic:

Built-In Step Types

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/sequence-context-control.html language=enus -->
## TOPIC 04122: Sequence Context Control

- bundle_id: `teststand-api-reference`
- source_path: `tsref/sequence-context-control.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/sequence-context-control.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Sequence Context control to obtain a reference to the TestStand SequenceContext object. You can use the sequence context to access all the objects, variables, and properties in the execution. See Also Sequence Context

### Sequence Context Control

Use the
 Sequence Context
 control to obtain a reference to the TestStand
 [SequenceContext](../tsapiref/sequencecontext.html)
 object. You can use the
 [sequence context](/csh?context=ts_tsfundamentals_seq_con)
 to access all the objects, variables, and properties in the execution.

#### See Also

[Sequence Context](/csh?context=ts_tsfundamentals_seq_con)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/sequence-editor-options-dialog-box.html language=enus -->
## TOPIC 04123: Sequence Editor Options Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/sequence-editor-options-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/sequence-editor-options-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Select Configure»Sequence Editor Options to launch the Sequence Editor Options dialog box. The Sequence Editor Options dialog box contains the following tabs: General —Miscellaneous options that apply to the TestStand Sequence Editor . UI Configuration —Defines layouts to preserve window pane positi

### Sequence Editor Options Dialog Box

Select
 Configure»Sequence Editor Options
 to launch the Sequence Editor Options dialog box.

The Sequence Editor Options dialog box contains the following tabs:

- General 
 —Miscellaneous options that apply to the
 TestStand Sequence Editor 
 .
- UI Configuration 
 —Defines layouts to preserve window pane positions and toolbar settings and locks specific user interface components of the sequence editor.

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/sequence-file-converter.html language=enus -->
## TOPIC 04124: Sequence File Converter

- bundle_id: `teststand-api-reference`
- source_path: `tsref/sequence-file-converter.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/sequence-file-converter.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Sequence File Converter tool to resave sequence files on disk using the current version of TestStand. Command-Line Usage SequenceFileConverter.exe [-Help] [-Recursive] [-Quiet] [-UpdateVersion] [-Unlock:<PasswordList>] [-Format:<Format>] [-Protect:<Mode>:<Password>] <file or directory path>

### Sequence File Converter

Use the Sequence File Converter tool to resave sequence files on disk using the current version of TestStand.

#### Command-Line Usage

SequenceFileConverter.exe [-Help] [-Recursive] [-Quiet] [-UpdateVersion] [-Unlock:<PasswordList>] [-Format:<Format>] [-Protect:<Mode>:<Password>] <file or directory path> [-env <environment path>]

#### Example

SequenceFileConverter.exe -Recursive -Unlock:myPass,myOtherPass -Format:Binary -Protect:View:myPass "C:\My Test Directory"

This example shows how to complete the following tasks:

- Unlock all files under
 "C:\My Test Directory" 
 using either "
 myPass 
 " or "
 myOtherPass 
 ".
- Convert unlocked files to binary format.
- Set password protection to prevent viewing of the converted files, using "
 myPass 
 ".
 Note 
 TestStand supports password-protecting sequence files to deter editing and viewing within the sequence editor and user interfaces that use the TestStand User Interface (UI) Controls. The TestStand API limits access to a file protected from viewing but cannot prevent access to the file content during execution. National Instruments does not recommend using passwords as the only way of protecting intellectual property.

#### Command-Line Options

The following list describes all of the available options you can use in the command line for the sequence file converter:

- Help 
 —Launches a dialog box that contains an explanation of the command-line arguments.
- Recursive 
 —Applies changes to files found in directories below the specified directory.
- Quiet 
 —Disables the prompt to confirm conversion and prompts to unlock files.
- UpdateVersion 
 —Saves sequence files with the current version of TestStand even if no other modifications to the file exist.
- Unlock:<
 PasswordList
 > 
 —Attempts to unlock files for editing using a comma delimited password list.
 Note 
 This does not remove password protection.
- Format:<
 Format
 > 
 —Converts all files to the specified format. Possible values for
 <Format> 
 are binary, INI, and XML.
- Protect:<
 Mode
 >:<
 Password
 > 
 —Protects all files with
 <password> 
 . Possible values for
 <Mode> 
 are Edit, View, and Disable.
 Note 
 The Disable value removes password protection from all files unlocked during conversion.
- env<
 environment path
 > 
 —Launches the Sequence File Converter tool in the evironment defined by the
 .tsenv 
 file located at the path you specify. Click
 here 
 for more information about
 .tsenv 
 files and
 here 
 for more information about choosing an evironment with the
 -env 
 command line switch.

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/sequence-file-documentation-dialog-box.html language=enus -->
## TOPIC 04125: Sequence File Documentation Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/sequence-file-documentation-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/sequence-file-documentation-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Select Tools»Sequence File Documentation to launch the Sequence File Documentation dialog box, in which you can generate an HTML or text document that contains all information about the sequences and steps in a selected sequence file. The Sequence File Documentation dialog box contains the following

### Sequence File Documentation Dialog Box

Select
 Tools»Sequence File Documentation
 to launch the Sequence File Documentation dialog box, in which you can generate an HTML or text document that contains all information about the sequences and steps in a selected sequence file.

The Sequence File Documentation dialog box contains the following options:

- Generate Documentation For 
 —The name and location of the sequence file.
- File Format 
 —The file format of the documentation file. The options are HTML and Text.
- Destination File Path 
 —The name and location of the documentation file to create.

The Properties/Variables section contains the following options:

- Show Parameters 
 —When you enable this option, sequence parameters are visible in the documentation file.
- Show Sequence File Globals 
 —When you enable this option, sequence file global variables are visible in the documentation file.
- Show Locals 
 —When you enable this option, sequence local variables are visible in the documentation file.
- Show Station Globals 
 —When you enable this option, the current station global variables are visible in the documentation file.

The Value Display Options subsection contains the following options:

- Show Subproperties 
 —Enable this control to make the subproperties of structured variables visible in the documentation file.
- Show Array Elements 
 —Enable this control to make the elements of array variables visible in the documentation file.
- Maximum Number of Elements to Show 
 —The maximum number of array elements from an array variable to include in the documentation file.
- Show Hidden Properties 
 —Enable this control to make variables or properties marked as hidden visible in the documentation file.

Enable the
 Launch Viewer When Done
 option to specify that the documentation tool opens the documentation file in a viewer application.

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/sequence-file-properties-dialog-box.html language=enus -->
## TOPIC 04126: Sequence File Properties Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/sequence-file-properties-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/sequence-file-properties-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Select Edit»Sequence File Properties to launch the Sequence File Properties dialog box for the sequence file. The Sequence File Properties dialog box contains the following tabs: General —The path and size of the file. You can also specify the version and comment for the file, the load and unload be

### Sequence File Properties Dialog Box

Select
 Edit»Sequence File Properties
 to launch the Sequence File Properties dialog box for the sequence file.

The Sequence File Properties dialog box contains the following tabs:

- General 
 —The path and size of the file. You can also specify the version and comment for the file, the load and unload behaviors of steps, the file format, and whether file globals are shared between executions.
- Advanced 
 —The type of sequence file and the model to use for normal sequence files.
- Synchronization 
 —Determines the synchronization options the steps use if a step specifies to use the sequence file setting.

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/sequence-file-tab.html language=enus -->
## TOPIC 04127: Sequence File Tab

- bundle_id: `teststand-api-reference`
- source_path: `tsref/sequence-file-tab.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/sequence-file-tab.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: A TestStand User Interface displays the Sequence File tab when you view the list of open sequence files in the list bar control. The Sequence File tab displays the contents of the selected sequence file. The Sequence File tab contains the following panes: Steps —The steps in the current sequence. Va

### Sequence File Tab

A
 [TestStand User Interface](teststand-user-interfaces.html)
 displays the Sequence File tab when you view the list of open sequence files in the
 [list bar](list-bar.html)
 control. The Sequence File tab displays the contents of the selected sequence file.

The Sequence File tab contains the following panes:

- Steps 
 —The steps in the current sequence.
- Variables 
 —Displays the sequence context for the selected sequence file. When editing a sequence file, you can modify values of existing properties and variables as well as insert and delete variables.
- Sequences 
 —The sequences in the selected file and selects the sequence to display in the Steps List.
- Insertion Palette 
 —Displays objects that you can insert into sequence files. The control has two lists. The Step Types list displays the TestStand step type menu, and the Templates list displays user-defined template sequences, steps, and variables. The Insertion Palette control is visible only in Editor Mode.

The following buttons appear along the bottom of the Sequence File tab:

- Test UUTs 
 —Starts a Test UUTs execution using the current sequence file. This button is visible only when the selected sequence file uses a process model that includes a Test UUTs Execution entry point.
- Single Pass 
 —Starts a Single Pass execution using the current sequence file. This button is visible only when the selected sequence file uses a process model that includes a Single Pass Execution entry point.
- Run <Selected Sequence> 
 —Executes the selected sequence without generating a report.

#### See Also

[List Bar](list-bar.html)

Parent topic:

TestStand User Interface Menus and Tabs

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/sequence-file-window.html language=enus -->
## TOPIC 04128: Sequence File Window

- bundle_id: `teststand-api-reference`
- source_path: `tsref/sequence-file-window.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/sequence-file-window.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: The TestStand Sequence Editor launches a separate Sequence File window for each sequence file you open using the File menu. To open an existing sequence file into a Sequence File window, select File»Open File . To create a new Sequence File window, select File»New»Sequence File . The Sequence File w

### Sequence File Window

The
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 launches a separate Sequence File window for each sequence file you open using the
 [File](file-menu.html)
 menu. To open an existing sequence file into a Sequence File window, select
 File»Open File
 . To create a new Sequence File window, select
 File»New»Sequence File
 . The Sequence File window contains the following panes:

- Sequences 
 —Displays a list of the sequence in the sequence file. Use this view to create new sequences and to cut, copy, and paste sequences.
- Steps 
 —Displays the steps in a specific sequence. The Steps pane has three groups: Main, Setup, and Cleanup. Expand a group to view the contents of the Main, Setup, or Cleanup group.
- Variables 
 —Displays the variables the selected steps on the Steps pane can access at run-time. The variables include locals, parameters, file globals, station globals and the RunState property of the sequence context.

Use the tabs at the bottom of the Sequence File window to navigate between the open panes. You can float or dock these panes anywhere within the Sequence File window.

In addition to the panes in the Sequence File window, the sequence editor window contains the
 [Step Settings](step-settings-pane.html)
 pane, which displays the module and settings for the selected step or steps on the Steps pane of the Sequence File window.

The
 [Status Bar](status-bar.html)
 displays information about the selected steps on the Steps pane of the Sequence File window.

Use the
 [Types](types-window.html)
 window to edit step types and custom data types attached to the sequence file.

#### See Also

[File Menu](file-menu.html)

[Status Bar](status-bar.html)

[Step Settings Pane](step-settings-pane.html)

[Types Window](types-window.html)

Parent topic:

TestStand Sequence Editor Menus, Panes, and Windows

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/sequence-hierarchy-window.html language=enus -->
## TOPIC 04129: Sequence Hierarchy Window

- bundle_id: `teststand-api-reference`
- source_path: `tsref/sequence-hierarchy-window.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/sequence-hierarchy-window.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Sequence Hierarchy window in the TestStand Sequence Editor to display a graph of the sequence call and callback sequence relationships among sequence files and sequences to more easily visualize, navigate, and maintain test sequences. The Sequence Hierarchy window does not provide a way to e

### Sequence Hierarchy Window

Use the Sequence Hierarchy window in the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 to display a graph of the sequence call and callback sequence relationships among sequence files and sequences to more easily visualize, navigate, and maintain test sequences. The Sequence Hierarchy window does not provide a way to edit Sequence Call steps and does not show execution flow while running.

Use the options on the
 [Sequence Hierarchy toolbar](toolbar-buttons-and-shortcuts.html)
 to configure the layout and horizontal and vertical direction of the graph and to arrange the nodes and links. Adjust the default graph layout to your needs before printing or saving the graph to disk, if necessary. The
 Sequence Hierarchy
 toolbar contains the following buttons:

| Command Name | Shortcut | Icon | Description |
| --- | --- | --- | --- |
| Graph Layout | — |  | The layout of the graph. The button displays the currently selected layout. Click this button to launch a submenu that contains the following layout options: Layered Digraph —A layered graph that groups edges into layers so no two edges in the same layer cross. This layout option reduces link crossings and produces clean graphs. This is the default option. Tree Graph —A layered graph that displays rapidly. Link overlapping can occur if cycles exist in the graph. Links can cross nodes if a node has more than one parent node. |
| Graph Direction | — |  | The horizontal or vertical orientation of the graph. The button displays the currently selected layout. Click this button to launch a submenu that contains the following graph direction options: Horizontal —Displays a horizontal graph. Vertical —Displays a vertical graph. |
| Expand All Nodes | <*> |  | Expands all the nodes in the graph. |
| Collapse All Nodes | <⁄> |  | Collapses all the nodes in the graph. |
| Expand One Level | <+> |  | Expands all nodes one level. |
| Collapse One Level | <-> |  | Collapses all nodes one level. |
| Allow Rearranging Nodes | — |  | Enables or disables the rearranging of nodes on the Call Graph pane of the Sequence Hierarchy window. Rearranging nodes is allowed by default. Click this button to disallow rearranging nodes. The icon changes to when rearranging is not allowed. Click this button again to restore the default setting. |
| Update From Sequences | — |  | Recreates the graph starting at the root sequence. The new graph reflects any changes you made to the call hierarchy in the sequence file. When you refresh the graph, the color palette might change. |

Use the following methods to open the Sequence Hierarchy window:

- Select
 View»Sequence File»Display File Hierarchy 
 to display the hierarchy of all the sequences in the current sequence file or select
 View»Sequence File»Display Hierarchy Using»<
 Entry Point Name
 > 
 to display the hierarchy from that entry point using the current sequence file as the client sequence file.
- Right-click the list of steps on the
 Steps 
 pane of the
 Sequence File 
 window and select
 Display File Hierarchy 
 from the context menu to display the hierarchy of all sequences in the sequence file or
 Display Hierarchy Using»<
 Entry Point Name
 > 
 from the context menu to display the hierarchy from that entry point using the current sequence file as a client sequence file.
- Right-click one or more sequences in the list of sequences on the
 Sequences 
 pane of the Sequence File window and select
 Display Sequence Hierarchy 
 from the context menu to display the hierarchy of the selected sequence or sequences, select
 Display File Hierarchy 
 from the context menu to display the hierarchy of all the sequences in the sequence file, or select
 Display Hierarchy Using»<
 Entry Point Name
 > 
 from the context menu to display the hierarchy from that entry point using the current sequence file as a client sequence file.
 If you do not select any sequences, the Display File Hierarchy option is available, and the Display Sequence Hierarchy option is disabled. If you select one or more sequences, the Display File Hierarchy is disabled, and the Display Sequence Hierarchy option is available.
- Right-click a sequence file in the list of sequence files on the
 Windows 
 pane or on the
 Workspace 
 pane and select
 Display File Hierarchy 
 from the context menu to display the hierarchy of all sequences in the sequence file, or select
 Display Hierarchy Using»<
 Entry Point Name
 > 
 from the context menu to display the hierarchy from that entry point using the current sequence file as a client sequence file.

Note

Entry Point Name

The Sequence Hierarchy window contains the following panes:

- Call Graph 
 —The sequence call graph.
- Legend 
 —The sequence files the Sequence Hierarchy window uses when creating the graph, the types of sequence calls, and the different sequence types the sequence files use.
- Graph Overview 
 —Shows a reduced-scale view of the graph and supports panning and zooming of the graph.

To restore hidden Call Graph, Legend, and Graph Overview panes, right-click the Sequence Hierarchy window and select the pane you want to restore, or select the hidden pane from the View submenu of the context menu. You can also select
 View»Hierarchy»Call Graph, Legend, or Overview
 to restore the hidden panes.

#### See Also

[Sequence File Window](sequence-file-window.html)

[Sequences Pane](sequences-pane-sequence-file-window.html)

[Sequences Pane Context Menu](sequences-pane-context-menu-sequence-file-win.html)

[Steps Pane](steps-pane-sequence-file-window.html)

[Toolbar Buttons and Shortcuts](toolbar-buttons-and-shortcuts.html)

[Windows Pane](windows-pane.html)

[Workspace Pane](workspace-pane.html)

Parent topic:

TestStand Sequence Editor Menus, Panes, and Windows

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/sequence-properties-dialog-box.html language=enus -->
## TOPIC 04130: Sequence Properties Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/sequence-properties-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/sequence-properties-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Select Sequence Properties from the context menu on the Sequences pane or select Edit»Sequence Properties to launch the Sequence Properties dialog box. The Sequence Properties dialog box contains the following tabs: General —Contains settings that affect how TestStand executes steps in the sequence.

### Sequence Properties Dialog Box

Select
 Sequence Properties
 from the context menu on the Sequences pane or select
 Edit»Sequence Properties
 to launch the Sequence Properties dialog box.

The Sequence Properties dialog box contains the following tabs:

- General 
 —Contains settings that affect how TestStand executes steps in the sequence.
- Model 
 —This tab is only visible when the sequence file you are editing is a process model file.

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/sequences-pane-context-menu-sequence-file-tab.html language=enus -->
## TOPIC 04131: Sequences Pane Context Menu - Sequence File Tab

- bundle_id: `teststand-api-reference`
- source_path: `tsref/sequences-pane-context-menu-sequence-file-tab.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/sequences-pane-context-menu-sequence-file-tab.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sequences Pane Context Menu To access the context menu, right-click the Sequences pane. The items in the context menu vary depending on whether you right-click a sequence or the background area of the pane. The Sequences pane context menu can contain the following items: Insert Sequence —Adds a new

### Sequences Pane Context Menu - Sequence File Tab

#### Sequences Pane Context Menu

To access the context menu, right-click the
 [Sequences](sequences-pane-sequence-file-tab.html)
 pane. The items in the context menu vary depending on whether you right-click a sequence or the background area of the pane.

The Sequences pane context menu can contain the following items:

- Insert Sequence 
 —Adds a new sequence to the sequence file.
- Cut 
 —Removes the selected sequence and places it on the clipboard.
- Copy 
 —Copies the selected sequence to the clipboard.
- Paste 
 —Inserts the sequence from the clipboard.
- Delete 
 —Deletes the sequence.
- Rename 
 —Edits the name of the selected sequence.
- Advanced 
 —Launches a submenu that contains the following option:
  - Edit Attributes 
 —Launches the
 Attributes 
 dialog box, in which you can create and edit attributes for the sequence.
- Sequence File Callbacks 
 —Launches the
 Sequence File Callbacks 
 dialog box for the sequence file.
- Sequence Properties 
 —Launches the
 Sequence Properties 
 dialog box for the selected sequence. Use the Sequence Properties dialog box to view and edit the built-in properties of the selected sequence. Usually, the Sequence Properties dialog box has a single tab, the General tab, but if the current sequence file is a process model file, the Sequence Properties dialog box also has a Model tab.

#### See Also

[Attributes dialog box](attributes-dialog-box.html)

[Sequence File Callbacks dialog box](select-sequence-file-callbacks-dialog-box.html)

[Sequence Properties dialog box](sequence-properties-dialog-box.html)

[Sequences Pane](sequences-pane-sequence-file-tab.html)

Parent topic:

Sequences Pane - Sequence File Tab

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/sequences-pane-context-menu-sequence-file-win.html language=enus -->
## TOPIC 04132: Sequences Pane Context Menu - Sequence File Window

- bundle_id: `teststand-api-reference`
- source_path: `tsref/sequences-pane-context-menu-sequence-file-win.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/sequences-pane-context-menu-sequence-file-win.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sequences Pane Context Menu To access the context menu, right-click the Sequences pane. The items in the context menu vary depending on whether you right-click a sequence or the background area of the pane. The Sequences pane context menu can contain the following items: Insert Sequence —Adds a new

### Sequences Pane Context Menu - Sequence File Window

#### Sequences Pane Context Menu

To access the context menu, right-click the
 [Sequences](sequences-pane-sequence-file-window.html)
 pane. The items in the context menu vary depending on whether you right-click a sequence or the background area of the pane.

The Sequences pane context menu can contain the following items:

- Insert Sequence 
 —Adds a new sequence to the sequence file.
- Run <
 Sequence Name
 > 
 —Initiates an execution of the active sequence without using a process model.
- Cut 
 —Removes the selected sequence and places it on the clipboard.
- Copy 
 —Copies the selected sequence to the clipboard.
- Paste 
 —Inserts the sequence from the clipboard.
- Delete 
 —Deletes the sequence.
- Rename 
 —Edits the name of the selected sequence.
- Advanced 
 —Launches a submenu that contains the following option:
  - Edit Attributes 
 —Launches the
 Attributes 
 dialog box, in which you can create and edit attributes for the sequence.
- Sequence File Callbacks 
 —Launches the
 Sequence File Callbacks 
 dialog box for the sequence file.
- Sequence Properties 
 —Launches the
 Sequence Properties 
 dialog box for the selected sequence. Use the Sequence Properties dialog box to view and edit the built-in properties of the selected sequence. Usually, the Sequence Properties dialog box has a single tab, the General tab, but if the current sequence file is a process model file, the Sequence Properties dialog box also has a Model tab.
- Display Sequence Hierarchy 
 —Displays a graph in the
 Sequence Hierarchy 
 window of the hierarchy of the selected sequence or sequences. This option is available only when you select one or more sequences when you access the context menu.
- Display File Hierarchy 
 —Displays a graph in the Sequence Hierarchy window of the hierarchy of all sequences in the sequence file. This option is available only when you do not select any sequence when you access the context menu.
- Display Hierarchy Using 
 —Displays a graph in the Sequence Hierarchy window of the hierarchy of all sequence calls starting at the process model entry point you select. The list of entry points varies according to the process model the sequence file uses. This option uses the current sequence file as a client sequence file.
- View 
 —Lists the available panes or windows for a sequence file. These commands are available only when a Sequence File window is active.
  - Steps 
 —Displays the
 Steps 
 pane where you edit the steps in the Setup, Main, and Cleanup step groups for the sequence file.
  - Sequences 
 —Displays the
 Sequences 
 pane where you edit the sequences in the sequence file.
  - Variables 
 —Displays the
 Variables 
 pane where you edit the locals, parameters, and file globals for the sequence file and station globals.
  - Types 
 —Displays the
 Types 
 window where you can edit step types, custom data types, and built-in data types. The
 TestStand Sequence Editor 
 selects the active sequence file in the Type Palettes window.
- Columns 
 —
  - Comments 
 —When you enable this option, the pane displays comments for each sequence. Use the
 Sequence Properties 
 dialog box to edit the comment for a sequence.
  - Requirements 
 —When you enable this option, the pane displays requirements for sequences. Use the
 Sequence Properties 
 dialog box to edit the list of requirements for a sequence.

#### See Also

[Attributes dialog box](attributes-dialog-box.html)

[Sequence Hierarchy Window](sequence-hierarchy-window.html)

[Sequence File Callbacks dialog box](select-sequence-file-callbacks-dialog-box.html)

[Sequence Properties dialog box](sequence-properties-dialog-box.html)

[Sequences Pane](sequences-pane-sequence-file-window.html)

[Steps Pane](steps-pane-sequence-file-window.html)

[Types Window](types-window.html)

[Variables Pane](variables-pane-sequence-file-window4.html)

Parent topic:

Sequences Pane - Sequence File Window

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/sequences-pane-sequence-file-tab.html language=enus -->
## TOPIC 04133: Sequences Pane - Sequence File Tab

- bundle_id: `teststand-api-reference`
- source_path: `tsref/sequences-pane-sequence-file-tab.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/sequences-pane-sequence-file-tab.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sequences Pane The Sequences pane lists the name, comment, and requirements values for all sequences in the sequence file. Use the Sequences pane to select the active sequence to display on the Steps pane and to insert new sequences and delete existing sequences from a sequence file. The Sequences p

### Sequences Pane - Sequence File Tab

#### Sequences Pane

The Sequences pane lists the name, comment, and requirements values for all sequences in the sequence file. Use the Sequences pane to select the active sequence to display on the
 [Steps](steps-pane-sequence-file-tab.html)
 pane and to insert new sequences and delete existing sequences from a sequence file. The
 [Sequences](sequences-pane-context-menu-sequence-file-tab.html)
 pane context menu contains commands for editing the list of sequences and displaying the
 [Sequence Properties](sequence-properties-dialog-box.html)
 and the
 [Sequence File Callbacks](select-sequence-file-callbacks-dialog-box.html)
 dialog boxes. You can also select
 Edit»Sequence Properties
 to launch the Sequence Properties dialog box for the selected sequence and select
 Edit»Sequence File Callbacks
 to launch the Sequence File Callbacks dialog box and add callback sequences to the sequence file.

You can sort the contents of the Sequences pane. Click any column header to sort the view by the values of that column in increasing order. Click the column header again to sort the values in decreasing order. Click the column header a third time to restore the values to the unsorted order.

#### See Also

[Sequence File Callbacks dialog box](select-sequence-file-callbacks-dialog-box.html)

[Sequence Properties dialog box](sequence-properties-dialog-box.html)

[Sequences Pane Context Menu](sequences-pane-context-menu-sequence-file-tab.html)

[Steps Pane](steps-pane-sequence-file-tab.html)

Parent topic:

Sequence File Tab

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/sequences-pane-sequence-file-window.html language=enus -->
## TOPIC 04134: Sequences Pane - Sequence File Window

- bundle_id: `teststand-api-reference`
- source_path: `tsref/sequences-pane-sequence-file-window.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/sequences-pane-sequence-file-window.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sequences Pane The Sequences pane lists the name, comment, and requirements values for all sequences in the sequence file. Use the Sequences pane to select the active sequence to display on the Steps pane, to insert new sequences, and to delete existing sequences from a sequence file. The Sequences

### Sequences Pane - Sequence File Window

#### Sequences Pane

The Sequences pane lists the name, comment, and requirements values for all sequences in the sequence file. Use the Sequences pane to select the active sequence to display on the
 [Steps](steps-pane-sequence-file-window.html)
 pane, to insert new sequences, and to delete existing sequences from a sequence file. The
 [Sequences pane context menu](sequences-pane-context-menu-sequence-file-win.html)
 contains commands for editing the list of sequences, running a sequence, displaying the
 [Sequence Properties](sequence-properties-dialog-box.html)
 and the
 [Sequence File Callbacks](select-sequence-file-callbacks-dialog-box.html)
 dialog boxes, and specifying whether to display the comments and requirements columns on the pane. You can also select
 Edit»Sequence Properties
 to launch the Sequence Properties dialog box for the selected sequence, and select
 Edit»Sequence File Callbacks
 to launch the Sequence File Callbacks dialog box and add callback sequences to the sequence file.

You can sort the contents of the Sequences pane. Click any column header to sort the view by the values of that column in increasing order. Click the column header again to sort the values in decreasing order. Click the column header a third time to restore the values to the unsorted order.

#### Sequence Types

Each sequence displays a different colored icon to indicate what type of sequence it is. The following table lists the types of sequences you can use.

| Sequence Type | Icon | Description |
| --- | --- | --- |
| Normal |  | A sequence that is not a callback or entry point sequence. |
| Callback |  | A sequence used to handle common tasks, such as serial number inquiry or report logging. |
| Execution Entry Point |  | A sequence in a process model file that invokes a test sequence file, typically by calling the MainSequence callback in the client sequence file. |
| Configuration Entry Point |  | A sequence in the process model file that configures a feature of the process model and usually saves configuration information in a .ini file in the <TestStand Application Data>\\cfg directory. |
| Reserved Callback |  | A sequence that designates templates for newly inserted callbacks. |

#### See Also

[Sequence File Callbacks dialog box](select-sequence-file-callbacks-dialog-box.html)

[Sequence Properties dialog box](sequence-properties-dialog-box.html)

[Sequences Pane Context Menu](sequences-pane-context-menu-sequence-file-win.html)

[Steps Pane](steps-pane-sequence-file-window.html)

Parent topic:

Sequence File Window

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/set-get-check-attributes-operation-edit-ivi-t.html language=enus -->
## TOPIC 04135: Set/Get/Check Attributes Operation - Edit IVI Tools Step Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/set-get-check-attributes-operation-edit-ivi-t.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/set-get-check-attributes-operation-edit-ivi-t.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Set/Get/Check Attributes Operation The Set/Get/Check Attributes operation contains a list control, which contains the attributes you are operating on. Use the Add and Remove buttons to add new attributes and remove existing attributes from the list. The Attribute section in the Edit IVI Tools Step d

### Set/Get/Check Attributes Operation - Edit IVI Tools Step Dialog Box

#### Set/Get/Check Attributes Operation

The Set/Get/Check Attributes operation contains a list control, which contains the attributes you are operating on. Use the
 Add
 and
 Remove
 buttons to add new attributes and remove existing attributes from the list.

The Attribute section in the Edit IVI Tools Step dialog box for the Set/Get/Check Attributes operation contains the following attribute-specific options:

- Operation 
 —Specifies whether the step gets the value, sets the value, or verifies the value of the attribute.
- Name or ID 
 —The index of the IVI attribute or the name of the IVI attribute.
- Channel Name 
 —The name of the channel to operate on. The channel name must be a valid virtual channel name as the IVI configuration for the logical name being used defines. This setting applies only to attributes of channels.
- Value 
 —For Set and Check operations, the control specifies the attribute value to assign or verify. For Get operations, the control specifies a variable or property to which the step assigns the returned value.

Parent topic:

Edit IVI Tools Step Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/set-operation-notification-settings-edit-tab.html language=enus -->
## TOPIC 04136: Set Operation - Notification Settings Edit Tab

- bundle_id: `teststand-api-reference`
- source_path: `tsref/set-operation-notification-settings-edit-tab.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/set-operation-notification-settings-edit-tab.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Set Operation Use the Set operation to notify one or more threads that an event has occurred or a condition has been met. When the notification is in a Set state, Wait operations on the notification succeed immediately. Enable the Set option on the left of the Notification Settings panel. The Set op

### Set Operation - Notification Settings Edit Tab

#### Set Operation

Use the Set operation to notify one or more threads that an event has occurred or a condition has been met. When the notification is in a Set state, Wait operations on the notification succeed immediately. Enable the
 Set
 option on the left of the Notification Settings panel.

The Set operation contains the following options:

- Notification Name or Reference Expression 
 —The notification on which to perform the operation. You can specify the notification by name or by the object reference you receive when you create the notification using the Use Object Reference for the Notification Reference Lifetime option.
- Data Value (optional) 
 —An optional data element to store with the set state of the notification. Threads that wait on the notification can then optionally retrieve this data. The data can be any type, including a number, string, Boolean, object reference, structured type (container), or arrays of these types. When you later wait on the notification, you must store the element into a location with the appropriate type. By default, the notification stores a copy of the value. However, when you enable the Store Data by Reference Instead of by Value option, the operation stores an ActiveX reference to the value instead. If you later store this reference into an object reference variable in the Wait operation, you can access the data using the TestStand API PropertyObject interface and the ActiveX/COM Adapter.
- Store Data by Reference Instead of by Value 
 —Specifies how to store the data you specify in the Data Value control. Enable the option when you want to store an ActiveX reference to the property. Disable the option when you want to store a copy of the data.
- Auto Clear After Notifying One Thread 
 —When you enable this option, TestStand clears the state of the notification after one thread receives the notification. Once you clear the state of a notification, subsequent Wait operations block until you perform another Set operation.

Parent topic:

Notification Settings Edit Tab

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/set-operation-notification-step-configuration.html language=enus -->
## TOPIC 04137: Set Operation - Notification Step Configuration Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/set-operation-notification-step-configuration.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/set-operation-notification-step-configuration.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Set Operation Use the Set operation to notify one or more threads that an event has occurred or a condition has been met. When the notification is in a Set state, Wait operations on the notification succeed immediately. The Set operation contains the following options: Notification Name or Reference

### Set Operation - Notification Step Configuration Dialog Box

#### Set Operation

Use the Set operation to notify one or more threads that an event has occurred or a condition has been met. When the notification is in a Set state, Wait operations on the notification succeed immediately.

The Set operation contains the following options:

- Notification Name or Reference Expression 
 —The notification on which to perform the operation. You can specify the notification by name or by the object reference you receive when you create the notification using the Use Object Reference for the Notification Reference Lifetime option.
- Data Value (optional) 
 —An optional data element to store with the set state of the notification. Threads that wait on the notification can then optionally retrieve this data. The data can be any type, including a number, string, Boolean, object reference, structured type (container), or arrays of these types. When you later wait on the notification, you must store the element into a location with the appropriate type. By default, the notification stores a copy of the value. However, when you enable the Store Data by Reference Instead of by Value option, the operation stores an ActiveX reference to the value instead. If you later store this reference into an object reference variable in the Wait operation, you can access the data using the TestStand API
 PropertyObject 
 interface and the ActiveX/COM Adapter.
- Store Data by Reference Instead of by Value 
 —Specifies how to store the data you specify in the Data Value control. Enable the option when you want to store an ActiveX reference to the property. Disable the option when you want to store a copy of the data.
- Auto Clear After Notifying One Thread 
 —When you enable this option, TestStand clears the state of the notification after one thread receives the notification. Once you clear the state of a notification, subsequent Wait operations block until you perform another Set operation.

#### See Also

[PropertyObject](../tsapiref/propertyobject.html)

Parent topic:

Notification Step Configuration Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/set-process-affinity-operation-cpu-affinity-e.html language=enus -->
## TOPIC 04138: Set Process Affinity Operation - CPU Affinity Edit Tab

- bundle_id: `teststand-api-reference`
- source_path: `tsref/set-process-affinity-operation-cpu-affinity-e.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/set-process-affinity-operation-cpu-affinity-e.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Set Process Affinity Operation Use the Set Process Affinity operation to modify the current process affinity mask, which represents the set of CPUs on which the process is allowed to run. When you set the process affinity for a sequence, save the previous affinity in the Setup step group and restore

### Set Process Affinity Operation - CPU Affinity Edit Tab

#### Set Process Affinity Operation

Use the Set Process Affinity operation to modify the current process affinity mask, which represents the set of CPUs on which the process is allowed to run. When you set the process affinity for a sequence, save the previous affinity in the Setup step group and restore the affinity in the Cleanup step group. Select the
 Set Process Affinity
 option on the CPU Affinity edit tab to display the Set Process Affinity operation settings.

The Set Process Affinity operation contains the following option:

- New Process Affinity 
 —A numeric value expression that indicates the new affinity mask for the process. The new process affinity mask must be a subset of the system affinity mask.
 Note 
 If you modify the process affinity mask after the thread affinity is set, the thread affinity is reset to match the process affinity. If you modify both the process affinity mask and the thread affinity mask, modify the process affinity mask first, then modify the thread affinity mask.

#### See Also

[CPU Affinity Step Configuration dialog box](cpu-affinity-step-configuration-dialog-box.html)

[CPU Affinity step](cpu-affinity-step.html)

Parent topic:

CPU Affinity Edit Tab

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/set-process-affinity-operation-cpu-affinity-s.html language=enus -->
## TOPIC 04139: Set Process Affinity Operation - CPU Affinity Step Configuration Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/set-process-affinity-operation-cpu-affinity-s.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/set-process-affinity-operation-cpu-affinity-s.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Set Process Affinity Operation Use the Set Process Affinity operation to modify the current process affinity mask, which represents the set of CPUs on which the process is allowed to run. When you set the process affinity for a sequence, save the previous affinity in the Setup step group and restore

### Set Process Affinity Operation - CPU Affinity Step Configuration Dialog Box

#### Set Process Affinity Operation

Use the Set Process Affinity operation to modify the current process affinity mask, which represents the set of CPUs on which the process is allowed to run. When you set the process affinity for a sequence, save the previous affinity in the Setup step group and restore the affinity in the Cleanup step group. Select the
 Set Process Affinity
 option on the CPU Affinity Step Configuration dialog box to display the Set Process Affinity operation settings.

The Set Process Affinity operation contains the following option:

- New Process Affinity 
 —A numeric value expression that indicates the new affinity mask for the process. The new process affinity mask must be a subset of the system affinity mask.
 Note 
 If you modify the process affinity mask after the thread affinity is set, the thread affinity is reset to match the process affinity. When you are modifying both the process affinity mask and the thread affinity mask, modify the process affinity mask first, then modify the thread affinity mask.

#### See Also

[CPU Affinity Step Configuration dialog box](cpu-affinity-step-configuration-dialog-box.html)

[CPU Affinity step](cpu-affinity-step.html)

Parent topic:

CPU Affinity Step Configuration Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/set-thread-affinity-operation-cpu-affinity-ed.html language=enus -->
## TOPIC 04140: Set Thread Affinity Operation - CPU Affinity Edit Tab

- bundle_id: `teststand-api-reference`
- source_path: `tsref/set-thread-affinity-operation-cpu-affinity-ed.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/set-thread-affinity-operation-cpu-affinity-ed.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Set Thread Affinity Operation Use the Set Thread Affinity operation to modify the current thread affinity mask. This affinity mask represents the set of CPUs on which the thread is allowed to run. When you set the thread affinity for a sequence, save the previous affinity in the Setup step group and

### Set Thread Affinity Operation - CPU Affinity Edit Tab

#### Set Thread Affinity Operation

Use the Set Thread Affinity operation to modify the current thread affinity mask. This affinity mask represents the set of CPUs on which the thread is allowed to run. When you set the thread affinity for a sequence, save the previous affinity in the Setup step group and restore the affinity in the Cleanup step group. Select the
 Set Thread Affinity
 option on the CPU Affinity edit tab to display the Set Thread Affinity operation settings.

The Set Thread Affinity operation contains the following option:

- New Thread Affinity 
 —A numeric value expression that indicates the new affinity mask for the thread. The new thread affinity mask must be a subset of the process affinity mask.
 Note 
 If you modify the process affinity mask after setting the thread affinity, the thread affinity is reset to match the process affinity. If you are modifying both the process affinity mask and the thread affinity mask, modify the process affinity mask first, then modify the thread affinity mask.

#### See Also

[CPU Affinity Step Configuration dialog box](cpu-affinity-step-configuration-dialog-box.html)

[CPU Affinity step](cpu-affinity-step.html)

Parent topic:

CPU Affinity Edit Tab

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/set-thread-affinity-operation-cpu-affinity-st.html language=enus -->
## TOPIC 04141: Set Thread Affinity Operation - CPU Affinity Step Configuration Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/set-thread-affinity-operation-cpu-affinity-st.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/set-thread-affinity-operation-cpu-affinity-st.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Set Thread Affinity Operation Use the Set Thread Affinity operation to modify the current thread affinity mask. This affinity mask represents the set of CPUs on which the thread is allowed to run. When you set the thread affinity for a sequence, save the previous affinity in the Setup step group and

### Set Thread Affinity Operation - CPU Affinity Step Configuration Dialog Box

#### Set Thread Affinity Operation

Use the Set Thread Affinity operation to modify the current thread affinity mask. This affinity mask represents the set of CPUs on which the thread is allowed to run. When you set the thread affinity for a sequence, save the previous affinity in the Setup step group and restore the affinity in the Cleanup step group. Select the
 Set Thread Affinity
 option on the CPU Affinity Step Configuration dialog box to display the Set Thread Affinity operation settings.

The Set Thread Affinity operation contains the following option:

- New Thread Affinity 
 —A numeric value expression that indicates the new affinity mask for the thread. The new thread affinity mask must be a subset of the process affinity mask.
 Note 
 If you modify the process affinity mask after setting the thread affinity, the thread affinity is reset to match the process affinity. When you are modifying both the process affinity mask and the thread affinity mask, modify the process affinity mask first, then modify the thread affinity mask.

#### See Also

[CPU Affinity Step Configuration dialog box](cpu-affinity-step-configuration-dialog-box.html)

[CPU Affinity step](cpu-affinity-step.html)

Parent topic:

CPU Affinity Step Configuration Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/set-thread-priority-operation-thread-priority.html language=enus -->
## TOPIC 04142: Set Thread Priority Operation - Thread Priority Settings Edit Tab

- bundle_id: `teststand-api-reference`
- source_path: `tsref/set-thread-priority-operation-thread-priority.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/set-thread-priority-operation-thread-priority.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Set Thread Priority Operation Use the Set Thread Priority operation to raise or lower the priority of the current thread. Enable the Set Priority option on the left of the Thread Priority Settings panel. The Set Thread Priority operation contains the following option: New Thread Priority —A numeric

### Set Thread Priority Operation - Thread Priority Settings Edit Tab

#### Set Thread Priority Operation

Use the Set Thread Priority operation to raise or lower the priority of the current thread. Enable the
 Set Priority
 option on the left of the Thread Priority Settings panel.

The Set Thread Priority operation contains the following option:

- New Thread Priority 
 —A numeric value expression that indicates the new priority for the thread. If you specify the priority as a numeric constant, the name that corresponds to the priority is shown in the indicator control. Use the drop-down list for this control to specify a priority constant for one of the valid priority settings.
 Valid ValuesValue
 Definition
 -15
 Idle
 -2
 Low
 -1
 Below Normal
 0
 Normal
 1
 Above Normal
 2
 High
 15
 Time Critical

Parent topic:

Thread Priority Settings Edit Tab

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/set-thread-priority-operation-thread-priority2.html language=enus -->
## TOPIC 04143: Set Thread Priority Operation - Thread Priority Configuration Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/set-thread-priority-operation-thread-priority2.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/set-thread-priority-operation-thread-priority2.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Set Thread Priority Operation Use the Set Thread Priority operation to raise or lower the priority of the current thread. The Set Thread Priority operation contains the following option: New Thread Priority —A numeric value expression that indicates the new priority for the thread. If you specify th

### Set Thread Priority Operation - Thread Priority Configuration Dialog Box

#### Set Thread Priority Operation

Use the Set Thread Priority operation to raise or lower the priority of the current thread.

The Set Thread Priority operation contains the following option:

- New Thread Priority 
 —A numeric value expression that indicates the new priority for the thread. If you specify the priority as a numeric constant, the name that corresponds to the priority shown in the indicator control. Use the drop-down list for this control to specify a priority constant for one of the valid priority settings.
 Valid ValuesValue
 Definition
 -15
 Idle
 -2
 Low
 -1
 Below Normal
 0
 Normal
 1
 Above Normal
 2
 High
 15
 Time Critical

Parent topic:

Thread Priority Configuration Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/shortcuts-dialog-box.html language=enus -->
## TOPIC 04144: Shortcuts Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/shortcuts-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/shortcuts-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Click Shortcuts on the Distributed Files tab of TestStand Deployment Utility to launch the Shortcuts dialog box, in which you can create shortcuts in the system installer. The Shortcuts dialog box contains the following options: The installer, not the deployable image directory, creates the shortcut

### Shortcuts Dialog Box

Click
 Shortcuts
 on the
 [Distributed Files](distributed-files-tab-teststand-deployment-ut.html)
 tab of
 [TestStand Deployment Utility](teststand-deployment-utility.html)
 to launch the Shortcuts dialog box, in which you can create shortcuts in the system installer.

Note

- Shortcuts 
 —The current list of shortcuts. You can edit the properties of a shortcut by selecting the shortcut and then editing the Shortcut Base Path, Shortcut Relative Path, and Shortcut Command Line Arguments.
- Shortcut Base Path 
 —The base directory the installer uses as the location for the shortcut.
- Shortcut Relative Path 
 —A subdirectory under the Shortcut Base Path the installer uses as the location for the shortcut.
- Shortcut Command Line Arguments 
 —The command-line arguments for the shortcut.
 Note 
 This option is not available for package-based distributions.
- Shortcut Start in 
 —Specifies the current working directory to use when you launch the application with this shortcut. If you do not specify a path, the installer uses the directory in which the target file installs. You can specify absolute paths and paths relative to the current working directory. Use relative paths when you want to call the shortcut from another process or from the command line.
 Note 
 Double-clicking a shortcut with a relative path uses the default Windows working directory (typically
 C:\Windows\System32
 ) as the current working directory, which can cause unexpected behavior. 
 Note 
 This option is not available for package-based distributions.
- Add Shortcut 
 —Creates a new shortcut based on the Shortcut Base Path, Shortcut Relative Path, and Shortcut Command Line Arguments.
- Delete Shortcut 
 —Removes the currently selected shortcut. This button is disabled if no shortcuts exist.

#### See Also

[TestStand Deployment Utility](teststand-deployment-utility.html)

Parent topic:

Distributed Files Tab - TestStand Deployment Utility

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/show-soft-front-panel-operation-edit-ivi-dmm.html language=enus -->
## TOPIC 04145: Show Soft Front Panel Operation - Edit IVI Dmm Step Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/show-soft-front-panel-operation-edit-ivi-dmm.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/show-soft-front-panel-operation-edit-ivi-dmm.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Show Soft Front Panel Operation SFP Options Tab The SFP Options tab for the Show Soft Front Panel operation contains the following options: Allow Control —When you enable this option, the soft front panel (SFP) responds to user input. Automatically Close Window When Execution is Released —When you e

### Show Soft Front Panel Operation - Edit IVI Dmm Step Dialog Box

#### Show Soft Front Panel Operation

#### SFP Options Tab

The SFP Options tab for the Show Soft Front Panel operation contains the following options:

- Allow Control 
 —When you enable this option, the soft front panel (SFP) responds to user input.
- Automatically Close Window When Execution is Released 
 —When you enable this option, the SFP closes when the execution is released. If not, the instrument session remains open until the SFP is closed.
- Wait for User to Close Before Continuing 
 —When you enable this option, the execution waits for the SFP to close before continuing to the next step.
- Allow User to Close 
 —When you enable this option, the user can close the SFP window.
- Show Modal 
 —When you enable this option, the SFP window is modal to the Main Application window.
- Auto Read Interval 
 —The rate at which the SFP reads or fetches measurements to update the SFP display.

Parent topic:

Show Soft Front Panel Operation - Edit IVI Dmm Step Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/show-soft-front-panel-operation-edit-ivi-dmm2.html language=enus -->
## TOPIC 04146: Show Soft Front Panel Operation - Edit IVI Dmm Step Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/show-soft-front-panel-operation-edit-ivi-dmm2.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/show-soft-front-panel-operation-edit-ivi-dmm2.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Show Soft Front Panel Operation Operation Settings Tab The Operation Settings tab for the Show Soft Front Panel operation contains the following option: Settings Property/Variable —The name of the property or variable in which TestStand stores the settings when you click OK in this dialog box. Click

### Show Soft Front Panel Operation - Edit IVI Dmm Step Dialog Box

#### Show Soft Front Panel Operation

#### Operation Settings Tab

The Operation Settings tab for the Show Soft Front Panel operation contains the following option:

- Settings Property/Variable 
 —The name of the property or variable in which TestStand stores the settings when you click
 OK 
 in this dialog box. Click
 Load 
 to reload the settings from the specified property or variable location.

Parent topic:

Show Soft Front Panel Operation - Edit IVI Dmm Step Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/show-soft-front-panel-operation-edit-ivi-dmm3.html language=enus -->
## TOPIC 04147: Show Soft Front Panel Operation - Edit IVI Dmm Step Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/show-soft-front-panel-operation-edit-ivi-dmm3.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/show-soft-front-panel-operation-edit-ivi-dmm3.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Show Soft Front Panel Operation Window Options Tab The Window Options tab for the Show Soft Front Panel operation contains the following options: Window Title —The title to display on the soft front panel (SFP) window. Location —The location and size of the SFP window.

### Show Soft Front Panel Operation - Edit IVI Dmm Step Dialog Box

#### Show Soft Front Panel Operation

#### Window Options Tab

The Window Options tab for the Show Soft Front Panel operation contains the following options:

- Window Title 
 —The title to display on the soft front panel (SFP) window.
- Location 
 —The location and size of the SFP window.

Parent topic:

Show Soft Front Panel Operation - Edit IVI Dmm Step Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/show-soft-front-panel-operation-edit-ivi-dmm4.html language=enus -->
## TOPIC 04148: Show Soft Front Panel Operation - Edit IVI Dmm Step Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/show-soft-front-panel-operation-edit-ivi-dmm4.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/show-soft-front-panel-operation-edit-ivi-dmm4.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Show Soft Front Panel Operation The IVI DMM soft front panel (SFP) displays the actual voltage and current levels TestStand measures. Additionally, use the SFP to configure, acquire, and display new measured values either continuously or manually. You can also use the SFP to configure the measuremen

### Show Soft Front Panel Operation - Edit IVI Dmm Step Dialog Box

#### Show Soft Front Panel Operation

The IVI DMM soft front panel (SFP) displays the actual voltage and current levels TestStand measures. Additionally, use the SFP to configure, acquire, and display new measured values either continuously or manually. You can also use the SFP to configure the measurement range.

The Edit IVI Dmm Step dialog box for the Show Soft Front Panel operation contains the following tabs:

- SFP Options 
 —The behavior for the SFP when displayed.
- Window Options 
 —The window title and display location for the SFP.
- Operation Settings 
 —Specifies where the dialog saves and reloads the operation settings.

Parent topic:

Edit IVI Dmm Step Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/show-soft-front-panel-operation-edit-ivi-fgen.html language=enus -->
## TOPIC 04149: Show Soft Front Panel Operation - Edit IVI Fgen Step Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/show-soft-front-panel-operation-edit-ivi-fgen.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/show-soft-front-panel-operation-edit-ivi-fgen.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Show Soft Front Panel Operation SFP Options Tab The SFP Options tab for the Show Soft Front Panel operation contains the following options: Allow Control —When you enable this option, the soft front panel (SFP) responds to user input. Automatically Close Window When Execution is Released —When you e

### Show Soft Front Panel Operation - Edit IVI Fgen Step Dialog Box

#### Show Soft Front Panel Operation

#### SFP Options Tab

The SFP Options tab for the Show Soft Front Panel operation contains the following options:

- Allow Control 
 —When you enable this option, the soft front panel (SFP) responds to user input.
- Automatically Close Window When Execution is Released 
 —When you enable this option, the SFP closes when the execution is released. If not, the instrument session remains open until the SFP is closed.
- Wait for User to Close before Continuing 
 —When you enable this option, the execution waits for the SFP to close before continuing to the next step.
- Allow User to Close 
 —When you enable this option, the user can close the SFP window.
- Show Modal 
 —When you enable this option, the SFP window is modal to the Main Application window.

Parent topic:

Show Soft Front Panel Operation - Edit IVI Fgen Step Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/show-soft-front-panel-operation-edit-ivi-fgen2.html language=enus -->
## TOPIC 04150: Show Soft Front Panel Operation - Edit IVI Fgen Step Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/show-soft-front-panel-operation-edit-ivi-fgen2.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/show-soft-front-panel-operation-edit-ivi-fgen2.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Show Soft Front Panel Operation Operation Settings Tab The Operation Settings tab for the Show Soft Front Panel operation contains the following option: Settings Property/Variable —The name of the property or variable in which TestStand stores the settings when you click OK . Click Load to reload th

### Show Soft Front Panel Operation - Edit IVI Fgen Step Dialog Box

#### Show Soft Front Panel Operation

#### Operation Settings Tab

The Operation Settings tab for the Show Soft Front Panel operation contains the following option:

- Settings Property/Variable 
 —The name of the property or variable in which TestStand stores the settings when you click
 OK 
 . Click
 Load 
 to reload the settings from the specified property or variable location.

Parent topic:

Show Soft Front Panel Operation - Edit IVI Fgen Step Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/show-soft-front-panel-operation-edit-ivi-fgen3.html language=enus -->
## TOPIC 04151: Show Soft Front Panel Operation - Edit IVI Fgen Step Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/show-soft-front-panel-operation-edit-ivi-fgen3.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/show-soft-front-panel-operation-edit-ivi-fgen3.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Show Soft Front Panel Operation Window Options Tab The Window Options tab for the Show Soft Front Panel operation contains the following options: Window Title —The title to display in the soft front panel (SFP) window. Location —The location and size of the SFP window.

### Show Soft Front Panel Operation - Edit IVI Fgen Step Dialog Box

#### Show Soft Front Panel Operation

#### Window Options Tab

The Window Options tab for the Show Soft Front Panel operation contains the following options:

- Window Title 
 —The title to display in the soft front panel (SFP) window.
- Location 
 —The location and size of the SFP window.

Parent topic:

Show Soft Front Panel Operation - Edit IVI Fgen Step Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/show-soft-front-panel-operation-edit-ivi-fgen4.html language=enus -->
## TOPIC 04152: Show Soft Front Panel Operation - Edit IVI Fgen Step Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/show-soft-front-panel-operation-edit-ivi-fgen4.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/show-soft-front-panel-operation-edit-ivi-fgen4.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Show Soft Front Panel Operation The function generator soft front panel (SFP) displays the channel waveforms the function generator is requested to output. Use The SFP to specify the output signal for each channel. You can select a functional signal, a stored arbitrary waveform, or a stored sequence

### Show Soft Front Panel Operation - Edit IVI Fgen Step Dialog Box

#### Show Soft Front Panel Operation

The function generator soft front panel (SFP) displays the channel waveforms the function generator is requested to output. Use The SFP to specify the output signal for each channel. You can select a functional signal, a stored arbitrary waveform, or a stored sequence of arbitrary waveforms. Additionally, use the SFP to configure the frequency, DC offset, amplitude, and duty cycle for the output signal.

The Edit IVI Dmm Step dialog box for the Show Soft Front Panel operation contains the following tabs:

- SFP Options 
 —The behavior for the SFP when displayed.
- Window Options 
 —The window title and display location for the SFP.
- Operation Settings 
 —Specifies where the dialog box saves and reloads the operation settings.

Parent topic:

Edit IVI Fgen Step Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/show-soft-front-panel-operation-edit-ivi-powe.html language=enus -->
## TOPIC 04153: Show Soft Front Panel Operation - Edit IVI Power Supply Step Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/show-soft-front-panel-operation-edit-ivi-powe.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/show-soft-front-panel-operation-edit-ivi-powe.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Show Soft Front Panel Operation SFP Options Tab The SFP Options tab for the Show Soft Front Panel operation contains the following options: Allow Control —When you enable this option, the soft front panel (SFP) responds to user input. Automatically Close Window When Execution is Released —When you e

### Show Soft Front Panel Operation - Edit IVI Power Supply Step Dialog Box

#### Show Soft Front Panel Operation

#### SFP Options Tab

The SFP Options tab for the Show Soft Front Panel operation contains the following options:

- Allow Control 
 —When you enable this option, the soft front panel (SFP) responds to user input.
- Automatically Close Window When Execution is Released 
 —When you enable this option, the SFP is closed when the execution is released. If not, the instrument session remains open until the SFP is closed.
- Wait for User to Close before Continuing 
 —When you enable this option, the execution waits for the SFP to close before continuing to the next step.
- Allow User to Close 
 —When you enable this option, the user can close the SFP window.
- Show Modal 
 —When you enable this option, the SFP window is modal to the Main Application window.
- Auto Read Interval 
 —The rate at which the SFP reads or fetches measurements to update the SFP display.

Parent topic:

Show Soft Front Panel Operation - Edit IVI Power Supply Step Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/show-soft-front-panel-operation-edit-ivi-powe2.html language=enus -->
## TOPIC 04154: Show Soft Front Panel Operation - Edit IVI Power Supply Step Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/show-soft-front-panel-operation-edit-ivi-powe2.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/show-soft-front-panel-operation-edit-ivi-powe2.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Show Soft Front Panel Operation Operation Settings Tab The Operation Settings tab for the Show Soft Front Panel operation contains the following option: Settings Property/Variable —The name of the property or variable in which TestStand stores the settings when you click OK in this dialog box. Click

### Show Soft Front Panel Operation - Edit IVI Power Supply Step Dialog Box

#### Show Soft Front Panel Operation

#### Operation Settings Tab

The Operation Settings tab for the Show Soft Front Panel operation contains the following option:

- Settings Property/Variable 
 —The name of the property or variable in which TestStand stores the settings when you click
 OK 
 in this dialog box. Click
 Load 
 to reload the settings from the specified property or variable location.

Parent topic:

Show Soft Front Panel Operation - Edit IVI Power Supply Step Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/show-soft-front-panel-operation-edit-ivi-powe3.html language=enus -->
## TOPIC 04155: Show Soft Front Panel Operation - Edit IVI Power Supply Step Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/show-soft-front-panel-operation-edit-ivi-powe3.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/show-soft-front-panel-operation-edit-ivi-powe3.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Show Soft Front Panel Operation Window Options Tab The Window Options tab for the Show Soft Front Panel operation contains the following options: Window Title —The title to display on the soft front panel (SFP) window. Location —The location and size of the SFP window.

### Show Soft Front Panel Operation - Edit IVI Power Supply Step Dialog Box

#### Show Soft Front Panel Operation

#### Window Options Tab

The Window Options tab for the Show Soft Front Panel operation contains the following options:

- Window Title 
 —The title to display on the soft front panel (SFP) window.
- Location 
 —The location and size of the SFP window.

Parent topic:

Show Soft Front Panel Operation - Edit IVI Power Supply Step Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/show-soft-front-panel-operation-edit-ivi-powe4.html language=enus -->
## TOPIC 04156: Show Soft Front Panel Operation - Edit IVI Power Supply Step Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/show-soft-front-panel-operation-edit-ivi-powe4.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/show-soft-front-panel-operation-edit-ivi-powe4.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Show Soft Front Panel Operation The power supply soft front panel (SFP) displays the current output voltage level setting, and displays the measured voltage and current levels. Within the SFP, you can configure the output voltage level and whether a channel output signal is enabled. You can also con

### Show Soft Front Panel Operation - Edit IVI Power Supply Step Dialog Box

#### Show Soft Front Panel Operation

The power supply soft front panel (SFP) displays the current output voltage level setting, and displays the measured voltage and current levels. Within the SFP, you can configure the output voltage level and whether a channel output signal is enabled. You can also configure the SFP to acquire and display new measured values continuously or manually.

The Edit IVI Power Supply Step dialog box for the Show Soft Front Panel operation contains the following tabs:

- SFP Options 
 —The behavior for the SFP when displayed.
- Window Options 
 —The window title and display location for the SFP.
- Operation Settings 
 —Specifies where the dialog box saves and reloads the operation settings.

Parent topic:

Edit IVI Power Supply Step Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/show-soft-front-panel-operation-edit-ivi-scop.html language=enus -->
## TOPIC 04157: Show Soft Front Panel Operation - Edit IVI Scope Step Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/show-soft-front-panel-operation-edit-ivi-scop.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/show-soft-front-panel-operation-edit-ivi-scop.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Show Soft Front Panel Operation SFP Options Tab The SFP Options tab for the Show Soft Front Panel operation contains the following options: Allow Control —When you enable this option, the soft front panel (SFP) responds to user input. Automatically Close Window When Execution is Released —When you e

### Show Soft Front Panel Operation - Edit IVI Scope Step Dialog Box

#### Show Soft Front Panel Operation

#### SFP Options Tab

The SFP Options tab for the Show Soft Front Panel operation contains the following options:

- Allow Control 
 —When you enable this option, the soft front panel (SFP) responds to user input.
- Automatically Close Window When Execution is Released 
 —When you enable this option, the SFP is closed when the execution is released. If not, the instrument session remains open until the SFP is closed.
- Wait for User to Close before Continuing 
 —When you enable this option, the execution waits for the SFP to close before continuing to the next step.
- Allow User to Close 
 —When you enable this option, the user can close the SFP window.
- Show Modal 
 —When you enable this option, the SFP window is modal to the Main Application window.
- Auto Read Interval 
 —The rate at which the SFP reads or fetches measurements to update the SFP display.

Parent topic:

Show Soft Front Panel Operation - Edit IVI Scope Step Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/show-soft-front-panel-operation-edit-ivi-scop2.html language=enus -->
## TOPIC 04158: Show Soft Front Panel Operation - Edit IVI Scope Step Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/show-soft-front-panel-operation-edit-ivi-scop2.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/show-soft-front-panel-operation-edit-ivi-scop2.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Show Soft Front Panel Operation Operation Settings Tab The Operation Settings tab for the Show Soft Front Panel operation contains the following option: Settings Property/Variable —The name of the property or variable in which TestStand stores the settings when you click OK . Click Load to reload th

### Show Soft Front Panel Operation - Edit IVI Scope Step Dialog Box

#### Show Soft Front Panel Operation

#### Operation Settings Tab

The Operation Settings tab for the Show Soft Front Panel operation contains the following option:

- Settings Property/Variable 
 —The name of the property or variable in which TestStand stores the settings when you click
 OK 
 . Click
 Load 
 to reload the settings from the specified property or variable location.

Parent topic:

Show Soft Front Panel Operation - Edit IVI Scope Step Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/show-soft-front-panel-operation-edit-ivi-scop3.html language=enus -->
## TOPIC 04159: Show Soft Front Panel Operation - Edit IVI Scope Step Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/show-soft-front-panel-operation-edit-ivi-scop3.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/show-soft-front-panel-operation-edit-ivi-scop3.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Show Soft Front Panel Operation Window Options Tab The Window Options tab for the Show Soft Front Panel operation contains the following options: Window Title —The title to display on the soft front panel (SFP) window. Location —The location and size of the SFP window.

### Show Soft Front Panel Operation - Edit IVI Scope Step Dialog Box

#### Show Soft Front Panel Operation

#### Window Options Tab

The Window Options tab for the Show Soft Front Panel operation contains the following options:

- Window Title 
 —The title to display on the soft front panel (SFP) window.
- Location 
 —The location and size of the SFP window.

Parent topic:

Show Soft Front Panel Operation - Edit IVI Scope Step Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/show-soft-front-panel-operation-edit-ivi-scop4.html language=enus -->
## TOPIC 04160: Show Soft Front Panel Operation - Edit IVI Scope Step Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/show-soft-front-panel-operation-edit-ivi-scop4.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/show-soft-front-panel-operation-edit-ivi-scop4.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Show Soft Front Panel Operation The oscilloscope soft front panel (SFP) displays the waveform TestStand acquires. Use the SFP to configure the horizontal seconds per division for the display, and the absolute value and center offset of the input range in volts for each channel. Additionally, use the

### Show Soft Front Panel Operation - Edit IVI Scope Step Dialog Box

#### Show Soft Front Panel Operation

The oscilloscope soft front panel (SFP) displays the waveform TestStand acquires. Use the SFP to configure the horizontal seconds per division for the display, and the absolute value and center offset of the input range in volts for each channel. Additionally, use the SFP to configure, acquire, and display new measured waveforms either continuously or manually.

The Edit IVI Scope Step dialog box for the Show Soft Front Panel operation contains the following tabs:

- SFP Options 
 —The behavior for the SFP when displayed.
- Window Options 
 —The window title and display location for the SFP.
- Operation Settings 
 —Specifies where the dialog box saves and reloads the operation settings.

Parent topic:

Edit IVI Scope Step Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/show-soft-front-panel-operation-edit-ivi-tool.html language=enus -->
## TOPIC 04161: Show Soft Front Panel Operation - Edit IVI Tools Step Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/show-soft-front-panel-operation-edit-ivi-tool.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/show-soft-front-panel-operation-edit-ivi-tool.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Show Soft Front Panel Operation The tool soft front panel (SFP) displays a panel you can use to perform low-level operations on an instrument. These operations include initializing or closing an instrument session, resetting the instrument, performing a self test, querying the instrument for revisio

### Show Soft Front Panel Operation - Edit IVI Tools Step Dialog Box

#### Show Soft Front Panel Operation

The tool soft front panel (SFP) displays a panel you can use to perform low-level operations on an instrument. These operations include initializing or closing an instrument session, resetting the instrument, performing a self test, querying the instrument for revision or error information, and setting or getting attribute values.

The Edit IVI Tools Step dialog box for the Show Soft Front Panel operation contains the following tabs:

- SFP Options 
 —The behavior for the SFP when displayed.
- Window Options 
 —The window title and display location for the SFP.
- Operation Settings 
 —Specifies where the dialog saves and reloads the operation settings.

Parent topic:

Edit IVI Tools Step Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/show-soft-front-panel-operation-edit-ivi-tool2.html language=enus -->
## TOPIC 04162: Show Soft Front Panel Operation - Edit IVI Tools Step Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/show-soft-front-panel-operation-edit-ivi-tool2.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/show-soft-front-panel-operation-edit-ivi-tool2.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Show Soft Front Panel Operation Operation Settings Tab The Operation Settings tab for the Show Soft Front Panel operation contains the following option: Settings Property/Variable —The name of the property or variable in which TestStand stores the settings when you click OK . Click the Load button t

### Show Soft Front Panel Operation - Edit IVI Tools Step Dialog Box

#### Show Soft Front Panel Operation

#### Operation Settings Tab

The Operation Settings tab for the Show Soft Front Panel operation contains the following option:

- Settings Property/Variable 
 —The name of the property or variable in which TestStand stores the settings when you click
 OK 
 . Click the
 Load 
 button to reload the settings from the specified property or variable location.

Parent topic:

Show Soft Front Panel Operation - Edit IVI Tools Step Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/show-soft-front-panel-operation-edit-ivi-tool3.html language=enus -->
## TOPIC 04163: Show Soft Front Panel Operation - Edit IVI Tools Step Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/show-soft-front-panel-operation-edit-ivi-tool3.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/show-soft-front-panel-operation-edit-ivi-tool3.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Show Soft Front Panel Operation SFP Options Tab The SFP Options tab for the Show Soft Front Panel operation contains the following options: Allow Control —When you enable this option, the soft front panel (SFP) responds to user input. Automatically Close Window When Execution is Released —When you e

### Show Soft Front Panel Operation - Edit IVI Tools Step Dialog Box

#### Show Soft Front Panel Operation

#### SFP Options Tab

The SFP Options tab for the Show Soft Front Panel operation contains the following options:

- Allow Control 
 —When you enable this option, the soft front panel (SFP) responds to user input.
- Automatically Close Window When Execution is Released 
 —When you enable this option, the SFP closes when the execution is released. If not, the instrument session remains open until the SFP is closed.
- Wait for User to Close before Continuing 
 —When you enable this option, the execution waits for the SFP to close before continuing to the next step.
- Allow User to Close 
 —Specifies whether the user can close the SFP window.
- Show Modal 
 —Specifies whether the SFP window is modal to the Main Application window.

Parent topic:

Show Soft Front Panel Operation - Edit IVI Tools Step Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/show-soft-front-panel-operation-edit-ivi-tool4.html language=enus -->
## TOPIC 04164: Show Soft Front Panel Operation - Edit IVI Tools Step Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/show-soft-front-panel-operation-edit-ivi-tool4.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/show-soft-front-panel-operation-edit-ivi-tool4.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Show Soft Front Panel Operation Window Options Tab The Window Options tab for the Show Soft Front Panel operation contains the following options: Window Title —The title to display in the soft front panel (SFP) window. Location —The location and size of the SFP window.

### Show Soft Front Panel Operation - Edit IVI Tools Step Dialog Box

#### Show Soft Front Panel Operation

#### Window Options Tab

The Window Options tab for the Show Soft Front Panel operation contains the following options:

- Window Title 
 —The title to display in the soft front panel (SFP) window.
- Location 
 —The location and size of the SFP window.

Parent topic:

Show Soft Front Panel Operation - Edit IVI Tools Step Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/shutdown-modified-files-dialog-box.html language=enus -->
## TOPIC 04165: Shutdown Modified Files Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/shutdown-modified-files-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/shutdown-modified-files-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: TestStand launches the Shutdown Modified Files dialog box when you attempt to shut down TestStand without saving one or more modified files. You can select the files to save before shutting down. The list control displays all modified files. Files for which you have permission to save are selected b

### Shutdown Modified Files Dialog Box

TestStand launches the Shutdown Modified Files dialog box when you attempt to shut down TestStand without saving one or more modified files. You can select the files to save before shutting down. The list control displays all modified files. Files for which you have permission to save are selected by default, and read-only files are not selected by default. Files for which you do not have permission to save are dimmed.

The Shutdown Modified Files dialog box contains the following options:

- Save Checked Files 
 —TestStand saves the selected files and continues with the shutdown process.
- Exit without Saving 
 —TestStand does not save the files and continues with the shutdown process.
- Cancel 
 —TestStand does not save the files and requests Microsoft Windows not to shut down.

#### See Also

[Close All Windows Modified Files dialog box](close-all-windows-modified-files-dialog-box.html)

[Logout Modified Files dialog box](logout-modified-files-dialog-box.html)

[Save All Modified Files dialog box](save-all-modified-files-dialog-box.html)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/smart-rename-dialog-box.html language=enus -->
## TOPIC 04166: Smart Rename Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/smart-rename-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/smart-rename-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Select Smart Rename in the context menu of the Variables Pane in the Sequence File Window to launch the Smart Rename dialog box. The Smart Rename dialog box allows you to rename a variable and then update all references to that variable within the variable’s scope. For a Local variable or a Paramete

### Smart Rename Dialog Box

Select
 Smart Rename
 in the
 [context menu](variables-pane-context-menu-sequence-file-win.html)
 of the
 [Variables Pane](variables-pane-sequence-file-window4.html)
 in the
 [Sequence File Window](sequence-file-window.html)
 to launch the Smart Rename dialog box.

The Smart Rename dialog box allows you to rename a variable and then update all references to
that variable within the variable’s scope.

Note

Note

The Smart Rename feature can find and process multiple
 [types of variable references](types-of-variable-references-smart-rename-dia.html)
 .

You can choose to simply perform the Smart Rename operation in default mode or you can preview the operation in preview mode. TestStand provides a status message once the operation is complete.

#### Default Mode

In the default mode, you can specify the new name of the variable and set the search options.
TestStand will find and update all the
 [auto-resolved references](types-of-variable-references-smart-rename-dia.html)
 , in addition to
the type of references checked in the Search Options. If any
 [possible references](types-of-variable-references-smart-rename-dia.html)
 are identified,
the dialog switches to the Preview Mode when you click
 OK
 and displays all the identified
references and allows you to update the unresolved ones. Any references that remain
unresolved when the operation is complete will be reported as part of the operation status
displayed in the Output Window.

The default mode offers the following search options:

- Variable Root 
 —Displays the fully qualified name of the parent of the variable being renamed.
If the variable renamed is an array element, the Variable Root will display the full name of the
array.
- Current Name 
 —Displays the current name of the variable.
- New Name 
 —You can enter the new name of the variable in this input window. If the new name
entered is invalid, an error provider will be displayed next to this window. Hovering over the
provider will list the reason for the error in a tooltip.
- Process Comments 
 —If this option is checked, TestStand will update any comments where the
fully qualified variable name is found.
- Process String Literals 
 —If this option is checked, TestStand will update any string literals
where the fully qualified variable name is found. String literals can be literal string values used
in TestStand expressions or it could be the value of a String variable.
- Preview 
 —Clicking on this button or using the <Ctrl+P> keyboard shortcut will
display a preview of the Smart Rename operation.
- OK 
 —Clicking on this button will commit all the changes and complete the Smart
Rename operation.
- Cancel 
 —Clicking on this button will cancel any changes made during this operation.

#### Preview Mode

You can preview the changes that will occur during the Smart Rename operation in the preview mode. Click the
 Preview
 button or use the <Ctrl+P> keyboard shortcut to switch the Smart Rename dialog box into preview mode.

The preview mode displays information in the following areas:

- References 
 —Lists all the references identified for the variable. The variables are grouped
based on
 reference type 
 .
The name of each item in this list specifies the location of that reference(s) in the sequence
file. Each item can contain multiple references to the variable and the same location can
appear under multiple groups. You can click on an item and the value expression for that
location will be displayed in the New Expression window.
When you accept the changes in the dialog, every item that is checked in this list will be
updated and every item that is unchecked will retain its original value.
- New Expression 
 —Displays the value of the location corresponding to the item
selected in the References view. If the corresponding item is checked in the References view, this
window will be editable and you can update the value as required. Once the value is modified,
clicking the
 Refresh 
 button, pressing <F5>, or navigating away from the New Expression window
will update the value of that location to the modified value and refresh the preview based on the new value.

Clicking the
 Refresh
 button or pressing <F5> will refresh the preview. You may need to refresh the preview after modifying the name in
the New Name window or updating the value displayed in the New Expression window.

#### Operation Status

TestStand will update the output window with the status of the operation once it is complete. The status messages contain the following information:

- The number of references that were updated.
- The number of references that could not be updated, either because they were possible
references that needed user input or because you unchecked a reference item in the preview
mode.
- For each reference that could not be updated, an output message will indicate its location.
Double-clicking on this message in the output window will take you to the actual
location of the reference in Sequence Editor and highlight it.

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/source-code-control-operations-dialog-box.html language=enus -->
## TOPIC 04167: Source Code Control Operations Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/source-code-control-operations-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/source-code-control-operations-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Open a workspace and select Add to Source Code Control , Check Out , Check In , or Undo Checkout from the context menu to launch the Source Code Control Operations dialog box. The TestStand Sequence Editor also launches this dialog box when you perform source code control (SCC) operations and enable

### Source Code Control Operations Dialog Box

Open a workspace and select
 Add to Source Code Control
 ,
 Check Out
 ,
 Check In
 , or
 Undo Checkout
 from the context menu to launch the Source Code Control Operations dialog box.

The
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 also launches this dialog box when you perform source code control (SCC) operations and enable the
 Use Dialog Box for File Checkout
 option on the
 [Source Control](source-control-tab-station-options-dialog-box.html)
 tab of the
 [Station Options](station-options-dialog-box.html)
 dialog box.

The Source Code Control Operations dialog box contains the following options:

- Files 
 —The list of files. You must check the files TestStand copies to the local computer.
- Select All 
 —Checks all the files displayed in the list control.
- Advanced 
 —Launches a dialog box for the SCC provider, which you can use to specify advanced source control options when checking out files.
- Keep Checked Out 
 —Instructs TestStand to check out the file after performing a check in operation.
- Comment 
 —A comment to include in the source control when checking in files.

#### See Also

[Station Options dialog box](station-options-dialog-box.html)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/source-code-tab-edit-c-c-dll-call-dialog-box.html language=enus -->
## TOPIC 04168: Source Code Tab - Edit C/C++ DLL Call Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/source-code-tab-edit-c-c-dll-call-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/source-code-tab-edit-c-c-dll-call-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Source Code Tab Use the Source Code tab to generate the source code for the DLL function, edit the source code, and resolve differences between the parameter list in the source code and the parameter information on the Module tab. TestStand can call the step code module even if you do not use the So

### Source Code Tab - Edit C/C++ DLL Call Dialog Box

#### Source Code Tab

Use the Source Code tab to generate the source code for the DLL function, edit the source code, and resolve differences between the parameter list in the source code and the parameter information on the
 [Module](module-tab-edit-c-c-dll-call-dialog-box.html)
 tab. TestStand can call the step
 [code module](/csh?context=ts_tsfundamentals_bldgblocks_codemodules)
 even if you do not use the Source Code tab.

The Source Code tab contains the following options:

- Create Code in Text File (Functions Only) 
 —Select this option when you want the C/C++ DLL Adapter to create and edit code using the default application Microsoft Windows associates with the file extension. When you select this option, you only specify the source file containing the function. When you select this option, the C/C++ DLL Adapter uses the C/C++ code template associated with the step type to create code. You cannot use this option to create C++ class methods.
- Create Code in Microsoft Visual Studio 
 —Select this option when you want the C/C++ DLL Adapter to create and edit code using a fully integrated interface with Microsoft Visual Studio. When you select this option, you must specify the source file and project file that contains the function. Optionally, you can also specify a Visual Studio solution file. When you select this option, the C/C++ DLL Adapter uses the Visual C++ .NET code template associated with the step type to create code.
- Source File that Contains Function 
 —The pathname of the source file. You must specify an existing source file when creating code in Visual Studio. If you want to create a new source file in a text file, you must enter an absolute pathname. If you are using an existing source file, you can enter an absolute or relative pathname. Relative pathnames are relative to the TestStand search directory paths. Use the
 Edit Search Directories 
 dialog box to
 customize the search directory paths 
 .
- Microsoft Visual Studio Project File 
 —The pathname of the project file. You must specify an existing project file. You can enter an absolute or relative pathname. Relative pathnames are relative to the TestStand search directory paths.
- Visual Studio Solution File 
 —The pathname of the solution file. You must specify an existing solution file. You can enter an absolute or relative pathname. Relative pathnames are relative to the TestStand search directory paths.
- Create Code 
 —Creates the source code shell for the function. You must specify an existing source file when creating code in Visual Studio. If the source file you specify does not already exist when creating code in a text file, the adapter creates it. If the file already exists, the C/C++ DLL Adapter appends the function to the end of the file. If a code template file exists for the step type you are using for the step, the C/C++ DLL Adapter uses the template to create the shell of the new function. If the project file you specify is not in the solution, the C/C++ DLL Adapter prompts you to add it. If the source file you specify is not in the project, the C/C++ DLL Adapter prompts you to add it. If you already have the source code for the function, click
 Edit Code 
 .
 If template source code exists for the step type you use for the step, the adapter inserts the parameter information from the template source code into the new function shell. The adapter also uses the template parameter list to complete the parameter information on the Module tab. If the step type does not have a code template, TestStand uses the default template for the C/C++ DLL Adapter. When the Module tab already contains parameter information that differs from the parameter list in the template, the C/C++ DLL Adapter launches a dialog box in which you can resolve the conflict. Enable
 Use Prototype from Module Tab
 when you want to use the prototype the Module tab specifies. 
 When the C/C++ DLL Adapter creates the code, the adapter launches the application currently registered on the system for the type of the file, such as Visual Studio for
 .cpp
 files, and displays the file in the application.
- Edit Code 
 —Edits the source code for the function if the source code already exists.
- Verify Prototype 
 —Checks for any
 conflicts between the source code and the parameter information 
 on the Module tab.
- Use Prototype from Module Tab 
 —TestStand ignores the code template prototype and to use the prototype the Module tab specifies.

#### See Also

[Edit Search Directories dialog box](edit-search-directories-dialog-box.html)

[Parsing Parameters from Source Code](/csh?context=ts_tsref_parsing_parameters_from_source_code)

Parent topic:

Edit C/C++ DLL Call Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/source-code-tab-edit-labwindows-cvi-module-ca.html language=enus -->
## TOPIC 04169: Source Code Tab - Edit LabWindows/CVI Module Call Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/source-code-tab-edit-labwindows-cvi-module-ca.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/source-code-tab-edit-labwindows-cvi-module-ca.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Source Code Tab Use the Source Code tab to generate the source code for the function, edit the source code, and to resolve differences between the parameter list in the source code and the parameter information on the Module tab. You do not have to use the Source Code tab for TestStand to call the c

### Source Code Tab - Edit LabWindows/CVI Module Call Dialog Box

#### Source Code Tab

Use the Source Code tab to generate the source code for the function, edit the source code, and to resolve differences between the parameter list in the source code and the parameter information on the Module tab. You do not have to use the Source Code tab for TestStand to call the
 [code module](/csh?context=ts_tsfundamentals_bldgblocks_codemodules)
 .

Note

If LabWindows/CVI 2019 or later is the active LabWindows/CVI installation, then the Module Pathname on the Module Tab updates to the
 .dll
 that the LabWindows/CVI project builds. If all the build configurations in the LabWindows/CVI project do not create the same
 .dll
 file path, a dialog appears, and you can choose which
 .dll
 to select as the Module path.

The Source Code tab contains the following options:

- Source File that Contains Function 
 —The pathname of the source file. If you want to create a new source file, you must enter an absolute pathname. If you are using an existing source file, you can enter an absolute or relative pathname. Relative pathnames are relative to the
 TestStand search directories 
 .
- CVI Project File to Open 
 —The pathname of the LabWindows/CVI project file. If the code module is a DLL or static library, you must enter the name of the LabWindows/CVI project used to create the DLL or static library file. If the code module is an object module, you can also specify a project.
- Create Code 
 —Creates the source code shell for the function.
 If the source file you specify does not already exist, the LabWindows/CVI Adapter creates it. If the file already exists, the LabWindows/CVI Adapter appends the function to the end of the file. If a code template file exists for the step type you are using for the step, the LabWindows/CVI Adapter uses the template to create the shell of the new function. If multiple code templates exist based on the step type and the
 [code template policy settings](labwindows-cvi-adapter-configuration-dialog-b.html)
 , TestStand launches the
 [Choose Code Template](choose-code-template-dialog-box.html)
 dialog box, in which you can select the code template to use for the new code module. If the project file you specify does not already exist, the LabWindows/CVI Adapter creates a new project file and adds the source file to it. Enable the
 Use Prototype from Module Tab
 option when you want to use the prototype the Module tab specifies.
- Edit Code 
 —Edits the source code for the function.
 When you click
 Create Code
 or
 Edit Code
 , the LabWindows/CVI Adapter launches a copy of LabWindows/CVI and opens the source file. When you specify a project file in the Source Code tab, the LabWindows/CVI Adapter also opens the project in LabWindows/CVI. When you click
 Create Code
 and the function already exists in the file, a dialog box launches and gives you the choice of replacing the current function or adding the new function shell above the current function. 
 Note 
 If LabWindows/CVI returns a warning when you open a project that some TestStand API files were not found, remove the files from the project and then add them again from the
 <National Instruments>\Shared\CVI\instr\TestStand\API
 directory. The
 <National Instruments>
 directory is located at
 C:\<Program Files>
 . The
 <CVI>
 directory is located at
 C:\<Program Files>\National Instruments
 .
- Verify Prototype 
 —Checks for any
 conflicts between the source code and the parameter information 
 on the Module tab.
- Use Prototype from Module Tab 
 —TestStand ignores the code template prototype and to use the prototype the Module tab specifies.

#### See Also

[Parsing Parameters from Source Code](/csh?context=ts_tsref_parsing_parameters_from_source_code)

Parent topic:

Edit LabWindows/CVI Module Call Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/source-code-tab-edit-net-call-dialog-box.html language=enus -->
## TOPIC 04170: Source Code Tab - Edit .NET Call Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/source-code-tab-edit-net-call-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/source-code-tab-edit-net-call-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Source Code Tab Use the Source Code tab to specify the source file, project file, and solution file that contains the source code for the class members the .NET step calls. TestStand can call the step code module even if you do not use the Source Code tab. You must have a supported version of Micros

### Source Code Tab - Edit .NET Call Dialog Box

#### Source Code Tab

Use the Source Code tab to specify the source file, project file, and solution file that contains the source code for the class members the .NET step calls. TestStand can call the step code module even if you do not use the Source Code tab.

Note

The Source Code tab contains the following options:

- Source File 
 —The pathname of the source file. If you have multiple calls on the .NET step and the calls reside in various source files, you can leave this control empty and TestStand prompts you to specify a source file when you click the
 Edit Code 
 or
 Create Code 
 button on the
 Module 
 tab. Because you can perform Edit Code or Create Code operations for multiple calls in a single step, the source file you select applies to any other calls you make in the same step. You can enter an absolute or relative pathname. Relative pathnames are relative to the TestStand search directory paths.
- Visual Studio Project File 
 —The pathname of the project file. You must specify an existing project file. If you do not specify a project file, TestStand launches the .NET Source Code Files window and prompts you to specify a project file when you click the
 Edit Code 
 or
 Create Code 
 button on the .NET Module tab. Because you can perform Edit Code or Create Code operations for multiple calls in a single step, the project file you select applies to any other calls you make in the same step. You can enter an absolute or relative pathname. Relative pathnames are relative to the TestStand search directory paths.
- Visual Studio Solution File (optional) 
 —The pathname of the solution file. You must specify an existing solution file. You can enter an absolute or relative pathname. Relative pathnames are relative to the TestStand
 search directory paths 
 .

#### See Also

[Edit Search Directories dialog box](edit-search-directories-dialog-box.html)

Parent topic:

Edit .NET Call Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/source-control-menu.html language=enus -->
## TOPIC 04171: Source Control Menu

- bundle_id: `teststand-api-reference`
- source_path: `tsref/source-control-menu.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/source-control-menu.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: You can use TestStand workspace files to access the files in a source code control (SCC) system . When TestStand loads a workspace, the properties of a workspace specify whether TestStand attempts to connect to an SCC provider. When TestStand successfully connects to an SCC provider, you can use the

### Source Control Menu

You can use TestStand workspace files to access the files in a
 [source code control (SCC) system](/csh?context=ts_tsfundamentals_scc_selecting)
 . When TestStand loads a workspace, the properties of a workspace specify whether TestStand attempts to connect to an SCC provider. When TestStand successfully connects to an SCC provider, you can use the commands in the Source Control menu.

To configure the properties of a workspace, right-click the workspace item in the
 [Workspace](workspace-pane.html)
 pane of the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 or the
 [Workspace Browser](workspace-browser-dialog-box.html)
 dialog box and select
 Properties
 to launch the
 [Workspace Object Properties](workspace-object-properties-dialog-box.html)
 dialog box. By default a workspace uses the default SCC provider the system specifies. You can configure the workspace to use the default SCC provider or a specific provider, and you can specify any provider specific options when you connect to the provider.

The
 [Source Control](source-control-tab-station-options-dialog-box.html)
 tab of the
 [Station Options](station-options-dialog-box.html)
 dialog box displays the default SCC provider for a computer system, and specifies how TestStand behaves when you check files in and out of SCC.

TestStand integrates with any SCC system that supports the Microsoft SCC interface.

You can access source control commands through the sequence editor using either the
 [Workspace](context-menu-workspace-pane.html)
 context menu for any file or project in the workspace, or the Source Control menu. The Source Control menu contains the following items, which are available when a workspace file is open and the active window is a Sequence File window:

- Get Latest Version 
 —Copies the latest version of the selected project or file from source control to the local computer. Click
 Advanced Options 
 to launch a dialog box that varies based on the SCC provider.
- Check Out 
 —Checks the selected file out of source control and places an editable copy of the file on the local computer. Click
 Advanced Options 
 to launch a dialog box that varies based on the SCC provider.
 Note 
 Before you make changes to a file, check the file out of source control. If, for a file checked into source control, you make a local copy of the file editable and then make changes, TestStand asks if you want to reload the file when you try to check the file out. When you reload the file, the version checked into source control overwrites the version on the local computer and you lose the changes you have made to the local file.
- Check In 
 —Checks the selected file into source control.
- Undo Check Out 
 —Checks the selected file back into source control and discards any changes you have made to the file. Click
 Advanced Options 
 to launch a dialog box that varies based on the SCC provider.
- Add to Source Code Control 
 —Adds the selected project or file to source code control.
- Remove from Source Code Control 
 —Removes the selected project or file from source code control. You can only access this option from the Source Code Control menu in the sequence editor.
 Note 
 Some SCC providers delete the local computer copy of the files you remove from source control using this option.
- Show History 
 —Shows the SCC history of the selected file. The history gives you information about the previous versions of the file.
- Show Differences 
 —Shows the differences between the two files you select to compare. For example, you can compare the local copy of a file with the same file checked into source control. The SCC provider determines the application that TestStand launches to compare two files. You can configure the SCC provider to use the
 TestStand File Diff and Merge 
 utility to compare sequence files, or you can use any third-party text differ application to compare sequence files that use the INI or XML file formats.
- SCC Properties 
 —The SCC properties for the selected file.
- Properties 
 —Shows the properties of the selected file. This option is available only from the context menu for a file in a workspace. This option launches a dialog box that contains the following tabs:
  - General 
 —The pathname of the file, the date the file was last modified, and the SCC status of the file.
  - Source Control 
 —Displays the source control project and launches the SCC provider. Click
 Advanced Options 
 to launch a dialog box that varies based on the SCC provider. For a workspace item, this tab also enables you to change and connect to an SCC provider and change the source control user name.
 Note 
 This tab is only visible for workspace and project items.
- Refresh All Status 
 —Refreshes the SCC status of all files in the workspace and verifies that the files exist on disk.
- SCC Provider Options 
 —Displays options for the SCC system.
- Run SCC 
 —Launches the SCC provider. You can access this option by selecting
 Source Control»Run 
 , by clicking the
 Run 
 button on the
 Source Control 
 tab of the
 Workspace Object Properties 
 dialog box, or by clicking the
 Run 
 button on the Project File Properties dialog box. You can launch the Workspace Object Properties or Project File Properties dialog boxes by right-clicking the workspace or project in the workspace and selecting
 Properties 
 from the context menu.

#### See Also

[Selecting a Source Code Control Provider](/csh?context=ts_tsfundamentals_scc_selecting)

[Station Options dialog box](station-options-dialog-box.html)

[TestStand File Diff and Merge Utility](teststand-file-diff-and-merge-utility.html)

[Workspace Context Menu](context-menu-workspace-pane.html)

[Workspace Browser dialog box](workspace-browser-dialog-box.html)

[Workspace Object Properties dialog box](workspace-object-properties-dialog-box.html)

[Workspace Pane](workspace-pane.html)

Parent topic:

Menus

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/source-control-tab-station-options-dialog-box.html language=enus -->
## TOPIC 04172: Source Control Tab - Station Options Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/source-control-tab-station-options-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/source-control-tab-station-options-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Source Control Tab TestStand integrates with any source code control (SCC) system that supports the Microsoft SCC interface . You can check files and projects in and out of the SCC system from a TestStand workspace . The Source Control tab contains the following controls when a workspace file is ope

### Source Control Tab - Station Options Dialog Box

#### Source Control Tab

TestStand
 [integrates with any source code control (SCC) system that supports the Microsoft SCC interface](/csh?context=ts_tsfundamentals_scc_selecting)
 . You can check files and projects in and out of the
 [SCC system from a TestStand workspace](source-control-menu.html)
 .

The Source Control tab contains the following controls when a workspace file is open:

- Check Out Source File(s) when Edited 
 —When you enable this option, a dialog box prompts you to check out a file when you edit a sequence file checked into source control in the current workspace.
- Prompt to Add to Source Code Control when Inserting File into Workspace 
 —TestStand prompts you to add a file to the source control system when you insert the file into the workspace.
- Use Dialog Box for File Checkout 
 —Launches the Check Out Files dialog box, which lists the files you are checking out when you check out files using the Workspace window.
- Display Only Selected Files in Source Code Control Dialog Boxes 
 —Displays only selected workspace files in Source Code Control dialog boxes. When this option is not set, the Source Code Control dialog boxes include all files under the selected item in the workspace.
- System Default Source Code Control Provider 
 —The default SCC provider for the operating system. This setting reflects the value stored in the Microsoft Windows registry for the system SCC settings located in the string key
 HKEY_LOCAL_MACHINE\Software\SourceCodeControlProvider\ProviderRegKey 
 . The key specifies the name of the
 HKEY_LOCAL_MACHINE\Software 
 registry key that contains the SCC provider server name and path. (32-bit TestStand) On 64-bit operating systems, this registry key appears only in the 32-bit registry. Use the path
 HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\SourceCodeControlProvider\ProviderRegKey 
 to access the key in the registry editor.
 If the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 loads a workspace file which does not specify an SCC provider name, TestStand connects to the system default SCC provider to perform SCC operations for the workspace. 
 When the value of this setting is empty, TestStand only connects to an SCC provider if the
 [WorkspaceFile](../tsapiref/workspacefile.html)
 object specifies a specific provider name.

#### See Also

[Selecting a Source Code Control Provider](/csh?context=ts_tsfundamentals_scc_selecting)

[Source Control Menu](source-control-menu.html)

[WorkspaceFile](../tsapiref/workspacefile.html)

Parent topic:

Station Options Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/source-control-tab-workspace-object-propertie.html language=enus -->
## TOPIC 04173: Source Control Tab - Workspace Object Properties Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/source-control-tab-workspace-object-propertie.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/source-control-tab-workspace-object-propertie.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Source Control Tab The Source Control tab contains the following options: Provider Name —The SCC provider name associated with the workspace file. Source Control Project —The SCC project name associated with the project file or folder. Source Control Username —The user name currently logged in for t

### Source Control Tab - Workspace Object Properties Dialog Box

#### Source Control Tab

The Source Control tab contains the following options:

- Provider Name 
 —The SCC provider name associated with the workspace file.
- Source Control Project 
 —The SCC project name associated with the project file or folder.
- Source Control Username 
 —The user name currently logged in for the SCC system.
- Run <
 Source Control System
 > 
 —Launches the main application for the SCC system.

#### See Also

[Selecting a Source Code Control Provider](/csh?context=ts_tsfundamentals_scc_selecting)

Parent topic:

Workspace Object Properties Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/source-destination-tab-legacy-import-export-p.html language=enus -->
## TOPIC 04174: Source/Destination Tab - Legacy Import/Export Properties Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/source-destination-tab-legacy-import-export-p.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/source-destination-tab-legacy-import-export-p.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Source/Destination Tab The Source/Destination tab for file or clipboard locations contains the following options: Data Location —Specifies whether TestStand imports/exports data to the clipboard, a file, or a database. File Location —The file location. This control is dimmed when you select clipboar

### Source/Destination Tab - Legacy Import/Export Properties Dialog Box

#### Source/Destination Tab

The Source/Destination tab for file or clipboard locations contains the following options:

- Data Location 
 —Specifies whether TestStand imports/exports data to the clipboard, a file, or a database.
- File Location 
 —The file location. This control is dimmed when you select clipboard as the file location.
- Format 
 —The file or clipboard data format. The file format can be tab-delimited text (
 .txt 
 ), comma-delimited text (
 .csv 
 ), or an Excel file (
 .xls 
 ). The clipboard format can be tab-delimited text (
 .txt 
 ) or comma-delimited text (
 .csv 
 ).
- Decimal Point 
 —The decimal point setting TestStand uses to import and export properties.
 Notice 
 If you specify a different decimal point for numeric values when you export and import values from a file, the imported values are not correct.
- Start of Data Marker 
 —The string that designates the beginning of a block of limit data. The marker string must appear at the beginning of a row. The marker string in this control and in the file do not require surrounding quotes.
 Include the
 <FILE>
 or
 <SEQUENCE>
 tag within the marker to instruct TestStand to automatically substitute the name of the sequence or file on which the step operates. Select
 <FILE>
 or
 <SEQUENCE>
 from the drop-down list to insert the tag.
- End of Data Marker 
 —The string that designates the end of a block of limit data. The marker string must appear at the beginning of a row. The marker string in this control and in the file do not require surrounding quotes.
 Include the
 <FILE>
 or
 <SEQUENCE>
 tag within the marker to instruct TestStand to automatically substitute the name of the sequence or file on which the step operates. Select
 <FILE>
 or
 <SEQUENCE>
 from the drop-down list to insert the tag.
- Skip Rows That Begin With 
 —Causes the Import or Export command to ignore all rows that begin with the string you specify in this control. This feature is useful when the file includes comment lines.
- First Row of Data Specifies Step Property for Each Column 
 —Defines the step property names for each column as the first row of each data block in the file. When you disable this option, you must use the Specify Column to Step Property Mapping text box to specify the list of property names. Separate the property names with commas, as shown in the following example:
 Limits.Low
 ,
 Limits.High
 ,
 Limits.String

Parent topic:

File or Clipboard Data Location - Legacy Import/Export Properties Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/source-destination-tab-legacy-import-export-p2.html language=enus -->
## TOPIC 04175: Source Destination Tab - Legacy Import/Export Properties Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/source-destination-tab-legacy-import-export-p2.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/source-destination-tab-legacy-import-export-p2.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Source Destination Tab The Source/Destination tab for database locations contains the following options: Data Link Name —The name of the data link the Data Link Properties dialog box uses to import and export. Click Select Data Link to select a predefined data link from a list. SQL Statement —The SQ

### Source Destination Tab - Legacy Import/Export Properties Dialog Box

#### Source Destination Tab

The Source/Destination tab for database locations contains the following options:

- Data Link Name 
 —The name of the
 data link 
 the
 Data Link Properties 
 dialog box uses to import and export. Click
 Select Data Link 
 to select a predefined data link from a list.
- SQL Statement 
 —The SQL statement the dialog box uses to import and export property and variable values. The SQL statement must return a recordset that includes the column names you specify.
- Build 
 —Constructs the
 SQL statement 
 . You cannot use the
 Build 
 button to edit an existing SQL statement expression.

Click the
 Expression Browse
 button to launch the
 [Expression Browser](expression-browser-dialog-box.html)
 dialog box.

#### See Also

[Build SQL Select Statement dialog box](build-sql-select-statement-dialog-box.html)

[Data Link Properties dialog box](data-link-properties-dialog-box.html)

[Edit Open SQL Statement dialog box](edit-open-sql-statement-dialog-box.html)

[Expression Browser dialog box](expression-browser-dialog-box.html)

Parent topic:

Database Data Location - Legacy Import/Export Properties Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/source-tab-edit-legacy-property-loader-dialog.html language=enus -->
## TOPIC 04176: Source Tab - Edit Legacy Property Loader Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/source-tab-edit-legacy-property-loader-dialog.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/source-tab-edit-legacy-property-loader-dialog.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Source Tab The Source tab contains the following options when you select File from the Data Location ring control: Select Specific File —A specific file TestStand evaluates at run time for the file pathname. File Location —The file pathname. Use Expression to Specify File —A string expression TestSt

### Source Tab - Edit Legacy Property Loader Dialog Box

#### Source Tab

The Source tab contains the following options when you select File from the Data Location ring control:

- Select Specific File 
 —A specific file TestStand evaluates at run time for the file pathname.
  - File Location 
 —The file pathname.
- Use Expression to Specify File 
 —A string expression TestStand evaluates at run time for the file pathname.
  - File Name 
 —The expression for the file.
- Format 
 —The file format. Valid formats are tab-delimited text (
 .txt 
 ), comma-delimited text (
 .csv 
 ), and Excel files (
 .xls 
 ).
 Note 
 If you edit the limits text (
 .txt
 ) or comma-delimited (
 .csv
 ) file using Microsoft Excel, Excel strips off quotation mark characters that surround string values when using the Text Import Wizard or when automatically opening
 .csv
 files. The TestStand Property Loader features attempt to import the value from the limits file with quotation marks if importing without quotation marks fails.
- Decimal Point 
 —The decimal point character TestStand uses to parse the limit data in the file.
 Notice 
 If you specify a different decimal point for numeric values when you export and import values from a file, the imported values are not correct.
- Start of Data Marker 
 —The string that designates the beginning of a block of data.
- End of Data Marker 
 —The string that designates the end of a block of data.
 You can specify literal strings for the beginning and ending markers, or you can specify string
 [expressions](/csh?context=ts_tsfundamentals_bldgblocks_expressions)
 TestStand evaluates at run time. The marker strings must appear in the first column of the file. If you specify an empty expression ("") for the starting and ending markers, the step type assumes that the file contains a single block of data. 
 Include the
 <FILE>
 or
 <SEQUENCE>
 tag within the Start of Data Marker or End of Data Marker to instruct TestStand to automatically substitute the name of the sequence or file on which the step operates. To insert the
 <FILE>
 or
 <SEQUENCE>
 tag, select it from the drop-down list next to the option.
- When Start Marker not Found 
 —The action to take if the start marker for one of the selected sequences is not found in the source file.
 
 Note 
 When you select Skip Sequence the step will not error if the start marker is not found, and the properties related to the sequence are not imported. Use the
 Stop and Error
 option to ensure that properties are imported for all sequences.
  - Stop and Error 
 —If the start marker is not found a run-time error occurs. This is the default setting.
  - Skip Sequence 
 —If the start marker is not found the step does not error. If you selected to import to
 <ALL SEQUENCES> 
 and the start marker is not found for one of the sequences, the step continues to import the properties for the next sequence.
- Skip Rows that Begin With 
 —Ignores all rows that begin with the specified string. Use this feature when the limits file includes comment lines.
- First Row of Data Specifies Step Property for Each Column 
 —Excludes the step property names from each column in the first row of each data block in the limits file. When you disable this option, you must use the Specify Column to Step Property Mapping text box to specify the list of property names. Separate the property names with commas, as in the following example:
 Limits.Low
 ,
 Limits.High
 ,
 Limits.String

Parent topic:

Edit Legacy Property Loader Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/specification-compliance-manager-report-optio.html language=enus -->
## TOPIC 04177: Specification Compliance Manager Report Options Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/specification-compliance-manager-report-optio.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/specification-compliance-manager-report-optio.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specification Compliance Manager Report Options Dialog Box The Specification Compliance Manager Report Options dialog box allows you to specify options for the SCM Data plug-in. The settings you choose in the Specification Compliance Manager Report Options dialog box apply to all executions that use

### Specification Compliance Manager Report Options Dialog Box

#### Specification Compliance Manager Report Options Dialog Box

The Specification Compliance Manager Report Options dialog box allows you to specify options for the SCM Data plug-in. The settings you choose in the Specification Compliance Manager Report Options dialog box apply to all executions that use the Test UUTs and Single Pass Execution entry points. You can open the dialog box by clicking the icon in the Options column for the SCM Data reporting plug-in in the
 [Results Processing](result-processing-dialog-box.html)
 dialog box.

The Specification Compliance Manager Report Options dialog box contains the following options:

- Report Directory 
 —The directory in which the report generator writes the report file. The following options are available in the ring control:
  - Client Sequence File Directory 
 —The directory that contains the client sequence file. For example, if you select Test UUTs from the
 Execute 
 menu when the d:\Tests\MySeqs\seq2.seq sequence file is active, the process model writes the report in the d:\Tests\Myseqs directory.
  - Specific Directory 
 —The directory you specify in the string control that appears under the ring control. You must enter an absolute path in the string control.
- Report Filename 
 —The format of the filename.
- Upload Report To Specification Compliance Manager 
 —Sets the SCM Data plug-in to automatically upload the SCM data file to SCM after report is generated.

#### See Also

[Import/Update from Specification Compliance Manager (SCM) Tool](import-update-from-specification-compliance-m.html)

Parent topic:

Import/Update from Specification Compliance Manager (SCM) Tool

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/specify-module-tabs-and-dialog-boxes.html language=enus -->
## TOPIC 04178: Specify Module Tabs and Dialog Boxes

- bundle_id: `teststand-api-reference`
- source_path: `tsref/specify-module-tabs-and-dialog-boxes.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/specify-module-tabs-and-dialog-boxes.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: To specify a module for a step, you must use a Module tab of the Step Settings pane in the TestStand Sequence Editor and a Specify Module dialog box in a TestStand User Interface . The actual title of the Specify Module tab or dialog box is different for each adapter. The following table lists the n

### Specify Module Tabs and Dialog Boxes

To specify a module for a step, you must use a Module tab of the
 [Step Settings](step-settings-pane.html)
 pane in the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 and a Specify Module dialog box in a
 [TestStand User Interface](teststand-user-interfaces.html)
 . The actual title of the Specify Module tab or dialog box is different for each adapter.

The following table lists the names of the various tabs and dialog boxes that open when you right-click a step in the sequence editor or a user interface and select
 Specify Module
 from the context menu or click
 Specify Module
 in the
 [Step Properties](step-properties-dialog-box.html)
 dialog box of a user interface.

| Module Adapter | Module Tab on Step Settings Pane | Specify Module Dialog Box that Appears | Description |
| --- | --- | --- | --- |
| LabVIEW Adapter | LabVIEW Module Tab | Edit LabVIEW VI Call | Calls LabVIEW VIs. |
| LabVIEW NXG Adapter | LabVIEW NXG Module Tab | Edit LabVIEW NXG VI Call | Calls LabVIEW NXG VIs in the context of a project or from a GLL. |
| LabWindows/CVI Adapter | LabWindows/CVI Module Tab | Edit LabWindows/CVI Module Call | Calls C functions. The function can be in an object file, library file, or DLL. It can also be in a source file when you are executing out-of-process using the LabWindows/CVI development environment and the source file is part of a LabWindows/CVI project. |
| C/C++ DLL Adapter | C/C++ DLL Module Tab | Edit C/C++ DLL Call | Calls C functions and static global and class C++ methods in a DLL. |
| .NET Adapter | .NET Module Tab | Edit .NET Call | Calls .NET assemblies written in any .NET-compliant language, such as C# and Microsoft Visual Basic .NET. |
| ActiveX/COM Adapter | ActiveX/COM Module Tab | Edit ActiveX/COM Call | Calls methods and access the properties of an object in an ActiveX Automation server. |
| HTBasic Adapter | HTBasic Module Tab | Edit HTBasic Subroutine Call | Calls HTBasic subroutines with no parameters. TestStand and HTBasic exchange data using the TestStand API. TestStand supports HTBasic version 7.2 or later. (64-bit TestStand) The HTBasic Adapter is not supported. |
| Sequence Adapter | Sequence Call Module Tab | Edit Sequence Call | Calls subsequences with parameters. The built-in Sequence Call step uses this adapter. |
| Sequence Adapter | Sequence Call Module Tab | Edit Sequence Call | Calls subsequences with parameters. The built-in Sequence Call step uses this adapter. |
| Python Adapter | Python Module Tab | Edit Python Call | Calls Python functions and attributes. The functions and attributes can belong to the Python module or the Python class. |

#### Source Code Templates

For each adapter that supports source code templates, the Module tab and the Specify Module dialog box displays a command button for creating source code based on a template for the step. If more than one template is available for the adapter/step type combination you use to create the step, the adapter selects from a list of the templates. If only one template is available, the adapter uses that template.

#### $(Platform) Macro in Directory Paths

You can use the
 $(Platform)
 macro in directory paths to support 32-bit code modules and 64-bit code modules with a single adapter step. The macro expands to
 win32
 for 32-bit TestStand and to
 x64
 for 64-bit TestStand. For example,
 C:\bin\$(Platform)\module.dll
 expands to
 C:\bin\win32\module.dll
 or to
 C:\bin\x64\module.dll
 .

Note

#### See Also

[Choose Code Template dialog box](choose-code-template-dialog-box.html)

[Developing Platform Independent Test Systems (Example)](/csh?context=ts_8230)

[Sequence Call](sequence-call-step.html)

[Step Properties dialog box](step-properties-dialog-box.html)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/specify-parameter-as-array-or-pointer-dialog.html language=enus -->
## TOPIC 04179: Specify Parameter as Array or Pointer Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/specify-parameter-as-array-or-pointer-dialog.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/specify-parameter-as-array-or-pointer-dialog.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: The LabWindows/CVI Module tab and the C/C++ DLL Module tab launch the Specify Parameter as Array or Pointer dialog box when you click the error indicator button for a parameter the adapter read from the prototype in the DLL, but the adapter cannot determine whether the parameter must be passed as a

### Specify Parameter as Array or Pointer Dialog Box

The
 [LabWindows/CVI Module](labwindows-cvi-module-tab.html)
 tab and the
 [C/C++ DLL Module](c-c-dll-module-tab.html)
 tab launch the Specify Parameter as Array or Pointer dialog box when you click the error indicator button for a parameter the adapter read from the prototype in the DLL, but the adapter cannot determine whether the parameter must be passed as a pointer or an array. For example, if a DLL exports a long * parameter, the adapter does not know whether to treat the parameter as a numeric value you pass by reference or an array of numeric values.

Select from one of the following options:

- Pointer 
 —The adapter must pass the argument as a pointer to a single object.
- Array 
 —The adapter must pass the argument as an array of multiple objects.
- Cancel 
 —The adapter does not update the prototype.

#### See Also

[C/C++ DLL Module Tab](c-c-dll-module-tab.html)

[LabWindows/CVI Module Tab](labwindows-cvi-module-tab.html)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/specify-sequence-call-expressions-dialog-box.html language=enus -->
## TOPIC 04180: Specify Sequence Call Expressions Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/specify-sequence-call-expressions-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/specify-sequence-call-expressions-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Double-click an expression node or right-click an expression node and select Select Sequence To Use from the context menu in the Sequence Hierarchy window to launch the Specify Sequence Call Expressions dialog box, in which you can simulate the sequence and sequence file to which the expressions in

### Specify Sequence Call Expressions Dialog Box

Double-click an expression node or right-click an expression node and select
 Select Sequence To Use
 from the context menu in the
 [Sequence Hierarchy](sequence-hierarchy-window.html)
 window to launch the Specify Sequence Call Expressions dialog box, in which you can simulate the sequence and sequence file to which the
 [expressions](/csh?context=ts_tsfundamentals_bldgblocks_expressions)
 in the Sequence Call step evaluate at run time.

The Specify Sequence Call Expressions dialog box contains the following options:

- Use Current File 
 —Calls a sequence in the sequence file you are currently editing.
- File Pathname Expression 
 —The expression for the sequence file pathname. You specify this expression in the Sequence Call step. This expression is for reference and is read-only.
- Specify File Pathname 
 —The pathname of the sequence file that contains the sequence you want to call.
- Sequence Expression 
 —An expression for the sequence name. You specify this expression in the Sequence Call step. This expression is for reference and is read-only.
- Specify Sequence 
 —The names of the sequences in the sequence file you specify.

#### See Also

[Sequence Hierarchy Window](sequence-hierarchy-window.html)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/sql-statement-tab-edit-open-sql-statement-dia.html language=enus -->
## TOPIC 04181: SQL Statement Tab - Edit Open SQL Statement Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/sql-statement-tab-edit-open-sql-statement-dia.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/sql-statement-tab-edit-open-sql-statement-dia.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: SQL Statement Tab The SQL Statement tab contains the following options: Database Handle (Number) —The name of the variable or property that contains the database handle you obtain from an Open Database step. The variable or property is of the Number data type. Statement Handle (Number) —A variable o

### SQL Statement Tab - Edit Open SQL Statement Dialog Box

#### SQL Statement Tab

The SQL Statement tab contains the following options:

- Database Handle (Number) 
 —The name of the variable or property that contains the database handle you obtain from an Open Database step. The variable or property is of the Number data type.
- Statement Handle (Number) 
 —A variable or property to which the step assigns the value of the SQL statement handle. The variable or property is of the Number data type. If you leave the control blank, the step automatically releases the SQL statement handle after executing the step. You must release this handle by calling a Close SQL Statement step and using this handle value as the handle to close.
- SQL Statement 
 —The SQL statement the step opens. You can specify the SQL statement as a literal string or as an expression TestStand evaluates at run time. Click
 Build 
 to construct the SQL statement.
 Note 
 When you set the
 Command Type
 control on the
 [Advanced](advanced-tab-edit-open-sql-statement-dialog-b.html)
 tab to "Stored Procedure," specify the name of the stored procedure in quotes in the SQL Statement field.
 You cannot use the
 Build
 button to edit an existing
 [SQL statement expression](/csh?context=ts_tsfundamentals_sql)
 .
- Build 
 —Launches the
 Build SQL Select Statement 
 dialog box, in which you can construct an SQL select statement.
- Number of Records Selected (optional) 
 —A variable or property to which the step assigns the number of records the SQL statement returns. The variable or property is of the Number data type.
- Statement Requires Parameters 
 —Specifies whether the SQL statement requires input or output parameters. If it does not require input or output parameters, the step immediately executes the SQL statement. If it does require input or output parameters, the step prepares only the SQL statement and a subsequent Data Operation step must perform an Execute Operation that defines the parameters for the statement.

#### See Also

[Build SQL Select Statement dialog box](build-sql-select-statement-dialog-box.html)

[Structure Query Language (SQL)](/csh?context=ts_tsfundamentals_sql)

Parent topic:

Edit Open SQL Statement Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/standard-input-tab-call-executable-edit-tabs.html language=enus -->
## TOPIC 04182: Standard Input Tab - Call Executable Edit Tabs

- bundle_id: `teststand-api-reference`
- source_path: `tsref/standard-input-tab-call-executable-edit-tabs.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/standard-input-tab-call-executable-edit-tabs.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Standard Input Tab Use the Standard Input tab in the TestStand Sequence Editor to specify the standard input the step passes to the call. You must configure the step to wait for the call to use this tab. Input Method —Specifies how the step creates the standard input for the executable. This option

### Standard Input Tab - Call Executable Edit Tabs

#### Standard Input Tab

Use the Standard Input tab in the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 to specify the standard input the step passes to the call. You must configure the step to wait for the call to use this tab.

- Input Method 
 —Specifies how the step creates the standard input for the executable. This option is valid only when the step is waiting on the executable. The ring control contains the following options:
  - No Input 
 —Provides no standard input to the executable. If you redirect either the standard output or the error to a variable or property, this option provides an empty string as an input. When you specify the No Input, Ignore Standard Output, and Ignore Standard Error options, the executable uses a default console window, if created, in which users can manually enter standard input. The executable displays standard output and errors in the default console window.
  - Expression 
 —Use an expression that the step evaluates at run time to determine the standard input.
  - String 
 —Use a literal string as standard input.
  - File on Local Machine 
 —Redirect the content of a file on the local machine as a standard input.
  - File on Remote Machine 
 —Redirects the content of a file on the remote machine as standard input. This option is available only when calling remote executables. Relative pathnames are relative to the working directory the call specifies.
- Input Expression 
 —An expression that the step evaluates at run time to determine the standard input for the executable.
- Input String 
 —A literal string that the step uses as standard input for the executable.
- Input File Path 
 —Absolute or relative pathname for the local or remote file to use as standard input.
- Specify Input File Path By Expression 
 —Enable this option to specify that the input file pathname is an expression the step evaluates at run time.

Parent topic:

Call Executable Edit Tabs

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/standard-input-tab-configure-call-executable.html language=enus -->
## TOPIC 04183: Standard Input Tab - Configure Call Executable Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/standard-input-tab-configure-call-executable.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/standard-input-tab-configure-call-executable.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Standard Input Tab Use the Standard Input tab in the Configure Call Executable dialog box in a TestStand User Interface to specify the standard input the step passes to the call. You must configure the step to wait for the call to use this tab. Input Method —Specifies how the step creates the standa

### Standard Input Tab - Configure Call Executable Dialog Box

#### Standard Input Tab

Use the Standard Input tab in the Configure Call Executable dialog box in a
 [TestStand User Interface](teststand-user-interfaces.html)
 to specify the standard input the step passes to the call. You must configure the step to wait for the call to use this tab.

- Input Method 
 —Specifies how the step creates the standard input for the executable. This option is valid only when the step is waiting on the executable. The ring control contains the following options:
  - No Input 
 —Provides no standard input to the executable. If you redirect either the standard output or the error to a variable or property, this option provides an empty string as an input. When you specify the No Input, Ignore Standard Output, and Ignore Standard Error options, the executable uses a default console window, if created, in which users can manually enter standard input. The executable displays standard output and errors in the default console window.
  - Expression 
 —Use an expression that the step evaluates at run time to determine the standard input.
  - String 
 —Use a literal string as standard input.
  - File on Local Machine 
 —Redirect the content of a file on the local machine as a standard input.
  - File on Remote Machine 
 —Redirects the content of a file on the remote machine as standard input. This option is available only when calling remote executables. Relative pathnames are relative to the working directory the call specifies.
- Input Expression 
 —An expression that the step evaluates at run time to determine the standard input for the executable.
- Input String 
 —A literal string that the step uses as standard input for the executable.
- Input File Path 
 —Absolute or relative pathname for the local or remote file to use as standard input.
- Specify Input File Path By Expression 
 —Enable this option to specify that the input file pathname is an expression the step evaluates at run time.

Parent topic:

Configure Call Executable Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/standard-output-error-tab-call-executable-edi.html language=enus -->
## TOPIC 04184: Standard Output/Error Tab - Call Executable Edit Tabs

- bundle_id: `teststand-api-reference`
- source_path: `tsref/standard-output-error-tab-call-executable-edi.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/standard-output-error-tab-call-executable-edi.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Standard Output/Error Tab Use the Standard Output/Error tab in the TestStand Sequence Editor to specify where the step stores the standard output and any errors from the call. You must configure the step to wait for the call to use this tab. Output Destination —Specifies how the step stores the stan

### Standard Output/Error Tab - Call Executable Edit Tabs

#### Standard Output/Error Tab

Use the Standard Output/Error tab in the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 to specify where the step stores the standard output and any errors from the call. You must configure the step to wait for the call to use this tab.

- Output Destination 
 —Specifies how the step stores the standard output from the executable. This option is valid only when waiting on the executable. The ring control contains the following options:
  - Ignore 
 —Ignore any standard output from the executable.
  - Store in Variable/Property 
 —Store standard output to a variable or property.
  - Save to Local Machine 
 —Redirect the standard output to a file on the local machine. Relative pathnames are relative to the working directory the call specifies for non-remote calls and relative to the sequence file directory for remote calls. TestStand overwrites the file if it already exists.
  - Save to Remote Machine 
 —Redirect the standard output to a file on the remote machine. Relative pathnames are relative to the working directory the call specifies. TestStand overwrites the file if it already exists.
- Output Location 
 —An expression the step evaluates at run time to determine the variable or property in which to store the standard output from the executable.
- Output File Path 
 —Absolute or relative pathname for the file in which the step stores the standard output from the executable.
- Specify Output File Path By Expression 
 —Enable this option to specify that the output file pathname is an expression the step evaluates at run time.
- Error Destination 
 —Specifies how the step stores the standard error from the executable. This option is valid only when waiting on the executable. The ring control contains the following options:
  - Ignore 
 —Ignore any standard error from the executable.
  - Store in Variable/Property 
 —Store standard error to a variable or property.
  - Save to Local Machine 
 —Redirect the standard error to a file on the local machine. Relative pathnames are relative to the working directory the call specifies for non-remote calls and relative to the sequence file directory for remote calls. TestStand overwrites the file if it already exists.
  - Save to Remote Machine 
 —Redirect the standard error to a file on the remote machine. Relative pathnames are relative to the working directory the call specifies. TestStand overwrites the file if it already exists.
- Error Location 
 —Expression that the step evaluates at run time to determine the variable or property in which to store the standard error from the executable.
- Set Error.Msg to Standard Error Text 
 —When you enable this option, the step copies the standard error to
 Step.Result.Error.Msg 
 . This option is available only when you store the standard error in a variable or property.
- Error File Path 
 —Absolute or relative pathname for the file in which the step stores the standard error from the executable.
- Specify Error Path By Expression 
 —Enable this option to specify that the error file pathname is an expression the step evaluates at run time.
- If Standard Error Is Non-Empty 
 —Specifies whether the step sets the
 step status 
 to
 Failed 
 or
 Error 
 when the executable returns standard error. This setting takes precedence over the Exit Code Failure Condition if both conditions are met.

Parent topic:

Call Executable Edit Tabs

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/standard-output-error-tab-configure-call-exec.html language=enus -->
## TOPIC 04185: Standard Output/Error Tab - Configure Call Executable Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/standard-output-error-tab-configure-call-exec.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/standard-output-error-tab-configure-call-exec.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Standard Output/Error Tab Use the Standard Output/Error tab in the Configure Call Executable dialog box in a TestStand User Interface to specify where the step stores the standard output and any errors from the call. You must configure the step to wait for the call to use this tab. Output Destinatio

### Standard Output/Error Tab - Configure Call Executable Dialog Box

#### Standard Output/Error Tab

Use the Standard Output/Error tab in the Configure Call Executable dialog box in a
 [TestStand User Interface](teststand-user-interfaces.html)
 to specify where the step stores the standard output and any errors from the call. You must configure the step to wait for the call to use this tab.

- Output Destination 
 —Specifies how the step stores the standard output from the executable. This option is valid only when waiting on the executable. The ring control contains the following options:
  - Ignore 
 —Ignore any standard output from the executable.
  - Store in Variable/Property 
 —Store standard output to a variable or property.
  - Save to Local Machine 
 —Redirect the standard output to a file on the local computer. Relative pathnames are relative to the working directory the call specifies for non-remote calls and relative to the sequence file directory for remote calls. TestStand overwrites the file if it already exists.
  - Save to Remote Machine 
 —Redirect the standard output to a file on the remote computer. Relative pathnames are relative to the working directory the call specifies. TestStand overwrites the file if it already exists.
- Output Location 
 —An expression the step evaluates at run time to determine the variable or property in which to store the standard output from the executable.
- Output File Path 
 —Absolute or relative pathname for the file in which the step stores the standard output from the executable.
- Specify Output File Path By Expression 
 —Enable this option to specify that the output file pathname is an expression the step evaluates at run time.
- Error Destination 
 —Specifies how the step stores the standard error from the executable. This option is valid only when waiting on the executable. The ring control contains the following options:
  - Ignore 
 —Ignore any standard error from the executable.
  - Store in Variable/Property 
 —Store standard error to a variable or property.
  - Save to Local Machine 
 —Redirect the standard error to a file on the local computer. Relative pathnames are relative to the working directory the call specifies for non-remote calls and relative to the sequence file directory for remote calls. TestStand overwrites the file if it already exists.
  - Save to Remote Machine 
 —Redirect the standard error to a file on the remote computer. Relative pathnames are relative to the working directory the call specifies. TestStand overwrites the file if it already exists.
- Error Location 
 —Expression that the step evaluates at run time to determine the variable or property in which to store the standard error from the executable.
- Set Error.Msg to Standard Error Text 
 —When you enable this option, the step copies the standard error to
 Step.Result.Error.Msg 
 . This option is available only when you store the standard error in a variable or property.
- Error File Path 
 —Absolute or relative pathname for the file in which the step stores the standard error from the executable.
- Specify Error Path By Expression 
 —Enable this option to specify that the error file pathname is an expression the step evaluates at run time.
- If Standard Error Is Non-Empty 
 —Specifies whether the step sets the
 step status 
 to
 Failed 
 or
 Error 
 when the executable returns standard error. This setting takes precedence over the Exit Code Failure Condition if both conditions are met.

Parent topic:

Configure Call Executable Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/start-scan-operation-ivi-switching-mode-edit.html language=enus -->
## TOPIC 04186: Start Scan Operation (IVI Switching Mode) - Edit IVI Switch Step Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/start-scan-operation-ivi-switching-mode-edit.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/start-scan-operation-ivi-switching-mode-edit.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Start Scan Operation (IVI Switching Mode) The Start Scan operation initiates a scan using the scan list the Configure Scan operation previously defined. Use the Abort Scan operation to stop the Start Scan operation. The instrument generates the first scan advanced output trigger after the Start Scan

### Start Scan Operation (IVI Switching Mode) - Edit IVI Switch Step Dialog Box

#### Start Scan Operation (IVI Switching Mode)

The Start Scan operation initiates a scan using the scan list the Configure Scan operation previously defined. Use the Abort Scan operation to stop the Start Scan operation.

The instrument generates the first scan advanced output trigger after the Start Scan operation. If the switch module activates the first switch upon the download of the scan list, the instrument must ensure that no scan advanced output trigger is generated.

Once the switch module is scanning, operations other than the Send Software Trigger, Start Scan, and Abort Scan are invalid. Calling the Start Scan operation during a scan returns the switch module to the default state and begins the scan again.

Parent topic:

IVI Switching Mode - Edit IVI Switch Step Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/start-stop-count-sweep-parameter-strategy.html language=enus -->
## TOPIC 04187: Start, Stop, Count Sweep Parameter Strategy

- bundle_id: `teststand-api-reference`
- source_path: `tsref/start-stop-count-sweep-parameter-strategy.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/start-stop-count-sweep-parameter-strategy.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Start, Stop, Count strategy with the Sweep Loop step to specify a range of values to sweep over. When the Start, Stop, Count strategy is selected for a sweep parameter, the following additional options are available: Start —Specifies the first value for the sweep. Stop —Specifies the final v

### Start, Stop, Count Sweep Parameter Strategy

Use the Start, Stop, Count strategy with the
 [Sweep Loop](sweep-loop-step.html)
 step to specify a range of values to sweep over. When the Start, Stop, Count strategy is selected for a sweep parameter, the following additional options are available:

- Start 
 —Specifies the first value for the sweep.
- Stop 
 —Specifies the final value for the sweep.
- Count 
 —Specifies the number of sweep points. This number must be greater than or equal to 2.
- Distribution 
 —Select one of the following options to specify how to distribute the sweep points:
  - Linear 
 —Spread the sweep points evenly between Start and Stop.
  - Decade 
 —Separate the sweep points between each decade by the specified number of points, such that the ratio of two consecutive numbers is the same.
  - Octave 
 —Separate the sweep points between each octave by the specified number of points, such that the ratio of two consecutive numbers is the same.
  - Geometric Progression 
 —Spread the sweep points logarithmically between Start and Stop.

The table below displays examples of sweep settings.

| Start | Stop | Count | Distribution | Sweep Parameter Values |
| --- | --- | --- | --- | --- |
| 1 | 5 | 5 | Linear | 1, 2, 3, 4, 5 |
| 0 | 100 | 6 | Linear | 0, 20, 40, 60, 80, 100 |
| 5 | 1 | 5 | Linear | 5, 4, 3, 2, 1 |
| 1 | 1000 | 2 | Decade | 1, 3.162277660168, 10, 31.62277660168, 100, 316.2277660168, 1000 |
| 1 | 16 | 2 | Octave | 1, 1.414213562373, 2, 2.828427124746, 4, 5.656854249492, 8, 11.31370849898, 16 |
| 1 | 1000 | 4 | Geometric Progression | 1, 10, 100, 1000 |
| 1000 | 1 | 4 | Geometric Progression | 1000, 100, 10, 1 |

Sweep parameter values may have any numeric representation. The representation in the Type column defines the representation for the sweep. The Stop option must have the same representation as Start.

64

Note

64

If represented using the default (64-bit floating point) representation, the value must be less than or equal to 2
 <sup>53</sup>
 . This is the largest positive integer such that it and all smaller positive integers can be represented exactly.

Parent topic:

Sweep Parameter Strategies

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/start-stop-step-sweep-parameter-strategy.html language=enus -->
## TOPIC 04188: Start, Stop, Step Sweep Parameter Strategy

- bundle_id: `teststand-api-reference`
- source_path: `tsref/start-stop-step-sweep-parameter-strategy.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/start-stop-step-sweep-parameter-strategy.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Start, Stop, Step strategy with the Sweep Loop step to specify a range of values to sweep over. When the Start, Stop, Step strategy is selected for a sweep parameter, the following additional options are available: Start —Specifies the first value for the sweep. Stop —Specifies the ending li

### Start, Stop, Step Sweep Parameter Strategy

Use the Start, Stop, Step strategy with the
 [Sweep Loop](sweep-loop-step.html)
 step to specify a range of values to sweep over. When the Start, Stop, Step strategy is selected for a sweep parameter, the following additional options are available:

- Start 
 —Specifies the first value for the sweep.
- Stop 
 —Specifies the ending limit for the sweep. The Stop value may or may not be included in the sweep depending on the Start and Step values.
 Note 
 A Stop value without an exact floating point representation may fall outside the specified range if the direction of the sweep is reversed. You may need to modify fractional Stop values to accommodate the specified range.
- Step 
 —Specifies the step size for the sweep.
- Distribution 
 —Select Linear or Geometric Progression to specify how to distribute the sweep points. If Linear is selected, the Step value is added to the current value to calculate the next sweep value. If Geometric Progression is selected, the current value is multiplied by the Step value to calculate the next value.

The table below displays examples of sweep settings.

| Start | Stop | Step | Distribution | Sweep Parameter Values |
| --- | --- | --- | --- | --- |
| 1 | 5 | 1 | Linear | 1, 2, 3, 4, 5 |
| 0 | 100 | 40 | Linear | 0, 40, 80 |
| 5 | 1 | -2 | Linear | 5, 3, 1 |
| 1 | INF | 100 | Linear | 1, 101, 201, 301, 401, ... |
| 1 | 1000 | 10 | Geometric Progression | 1, 10, 100, 1000 |
| 20 | 3 | 0.5 | Geometric Progression | 20, 10, 5 |
| 1 | INF | 100 | Geometric Progression | 1, 100, 10000, 1e6, 1e8, ... |

Sweep parameter values may have any numeric representation. The representation of the Start option defines the representation for the sweep. The Stop and Step options must have the same representation as Start.

Parent topic:

Sweep Parameter Strategies

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/statement-step.html language=enus -->
## TOPIC 04189: Statement Step

- bundle_id: `teststand-api-reference`
- source_path: `tsref/statement-step.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/statement-step.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use a Statement step to execute expressions . For example, you can use a Statement step to increment the value of a local variable in a sequence. By default, Statement steps do not pass or fail. When the step cannot evaluate the expression or when the expression sets Step.Result.Error.Occurred to Tr

### Statement Step

Use a Statement step to execute
 [expressions](/csh?context=ts_tsfundamentals_bldgblocks_expressions)
 . For example, you can use a Statement step to increment the value of a local variable in a sequence.

By default, Statement steps do not pass or fail. When the step cannot evaluate the expression or when the expression sets
 Step.Result.Error.Occurred
 to
 True
 , TestStand sets the
 [step status](/csh?context=ts_tsfundamentals_step_status_values_table)
 to
 Error
 . Otherwise, TestStand sets the step status to
 Done
 .

#### Configuring the Step

Use the
 [Expression](expression-edit-tab.html)
 edit tab in the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 and the
 [Edit Statement](edit-statement-dialog-box.html)
 dialog box in a
 [TestStand User Interface](teststand-user-interfaces.html)
 to specify expressions for a Statement step.

#### Step Properties

The Statement step type does not define any additional step properties other than
 [custom properties common to all steps](/csh?context=ts_tsfundamentals_custom_result_props)
 .

#### See Also

[Built-In Step Types](built-in-step-types.html)

Parent topic:

Built-In Step Types

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/station-globals-window.html language=enus -->
## TOPIC 04190: Station Globals Window

- bundle_id: `teststand-api-reference`
- source_path: `tsref/station-globals-window.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/station-globals-window.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: You can view and edit global variables in the Station Globals window of the TestStand Sequence Editor , which you can access by selecting the Station Globals menu item in the View menu of the sequence editor. You can also view and edit the global variables in the Variables pane of the Sequence File

### Station Globals Window

You can view and edit global variables in the Station Globals window of the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 , which you can access by selecting the Station Globals menu item in the
 [View](view-menu.html)
 menu of the sequence editor. You can also view and edit the global variables in the Variables pane of the Sequence File and Execution windows.

Use the
 [Globals](globals-context-menu.html)
 context menu to insert new variables and to reload station globals variables from disk.

You can sort the contents of the Station Globals window. Click any column header to sort the view by the values of that column in increasing order. Click the column header again to sort the values in decreasing order. Click the column header a third time to restore the values to the unsorted order.

The Station Globals Window contains the following options:

- Filter 
 —Used to filter variables and properties by name. To clear the filter, click the X button. Use the Show match sub-properties option to display the sub-properties of containers that match the current filter.
 Note 
 Array elements, including steps, are not filtered out unless all array elements and their sub-properties are filtered out.

Note

#### See Also

[Globals Context Menu](globals-context-menu.html)

[Station Global Variables](/csh?context=ts_tsfundamentals_station_global_variables)

[Variables Pane - Execution Window](variables-pane-execution-window.html)

[Variables Pane - Sequence File Window](variables-pane-sequence-file-window4.html)

[View Menu](view-menu.html)

Parent topic:

TestStand Sequence Editor Menus, Panes, and Windows

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/station-options-dialog-box.html language=enus -->
## TOPIC 04191: Station Options Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/station-options-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/station-options-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Select Configure»Station Options to launch the Station Options dialog box, in which you can set preferences for the TestStand station. The settings you choose affect all TestStand Sequence Editor and User Interface sessions that run on the computer. TestStand stores most station options in <TestStan

### Station Options Dialog Box

Select
 Configure»Station Options
 to launch the Station Options dialog box, in which you can set preferences for the TestStand station. The settings you choose affect all TestStand Sequence Editor and User Interface sessions that run on the computer. TestStand stores most station options in
 [<TestStand Application Data>](/csh?context=ts_tsfundamentals_directories)
 \Cfg\GeneralEngine.cfg
 .

The Station Options dialog box contains the following tabs:

- Execution 
 —Contains operations for breakpoints, tracing, and interactive execution.
- Time Limits 
 —The time limits for executions. When you specify a time limit, choose an action to take when the time limit expires.
- File 
 —Options for files, types, and version numbers.
- Preferences 
 —General options for the station, such as the name of the test station.
- Model 
 —The process model file for the station as a whole and whether each individual sequence may specify its own process model file.
- User Manager 
 —Specifies whether TestStand enforces user privileges. It also specifies the location of the user manager configuration file.
- Localization 
 —The language in which to display text and other region-specific settings.
- Remote Execution 
 —Specifies whether remote test stations may run sequences on this test station.
- Source Control 
 —General options that apply to source code control operations.

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/status-bar-analysis-results-pane.html language=enus -->
## TOPIC 04192: Status Bar - Analysis Results Pane

- bundle_id: `teststand-api-reference`
- source_path: `tsref/status-bar-analysis-results-pane.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/status-bar-analysis-results-pane.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Status Bar The Analysis Results pane status bar contains the following items, arranged from left to right: Status of Analysis —Current status of the analysis session, such as Analyzing, Completed, Stopped, or Not Analyzed. Messages Selected —Number of messages you have selected. Number of Messages —

### Status Bar - Analysis Results Pane

#### Status Bar

The Analysis Results pane status bar contains the following items, arranged from left to right:

- Status of Analysis 
 —Current status of the analysis session, such as Analyzing, Completed, Stopped, or Not Analyzed.
- Messages Selected 
 —Number of messages you have selected.
- Number of Messages 
 —Number of messages in the Messages list on the Analyzer Messages tab the TestStand Sequence Analyzer generated for the current analysis, including the number of Active, Ignored, and Fixed messages.
- Number of Files 
 —Number of files analyzed.

Parent topic:

Analysis Results Pane

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/status-bar-teststand-file-diff-and-merge-util.html language=enus -->
## TOPIC 04193: Status Bar - TestStand File Diff and Merge Utility

- bundle_id: `teststand-api-reference`
- source_path: `tsref/status-bar-teststand-file-diff-and-merge-util.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/status-bar-teststand-file-diff-and-merge-util.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Status Bar The TestStand File Diff and Merge utility status bar contains the following items, arranged from left to right: Environment —The TestStand environment in which the application is running. Remaining Conflicts —The number of unresolved conflicts in the merged file. This item is available on

### Status Bar - TestStand File Diff and Merge Utility

#### Status Bar

The TestStand File Diff and Merge utility status bar contains the following items, arranged from left to right:

- Environment 
 —The TestStand
 environment 
 in which the application is running.
- Remaining Conflicts 
 —The number of unresolved conflicts in the merged file. This item is available only when you compare three files.
- Property Moved 
 —Shows the icon the Item column of the
 Differences table 
 uses for a property that has moved to a different location in the other file or files.
- Property Moved And Modified 
 —Shows the icon the Item column of the Differences table uses for a property that has moved to a different location in the other file or files and has been modified in that other location.
- Conflict 
 —Shows how the Differences table represents a conflict.
- Insertion 
 —Shows how the Differences table represents an insertion.
- Deletion 
 —Shows how the Differences table represents a deletion.
- Value Change 
 —Shows how the Differences table represents a value change.
- Ignored Change 
 —Shows how the Differences table represents an ignored change.
- Differences in SubProperties 
 —Shows how the Differences table represents a property with differences in its elements or subproperties.

Parent topic:

TestStand File Diff and Merge Utility

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/status-bar.html language=enus -->
## TOPIC 04194: Status Bar

- bundle_id: `teststand-api-reference`
- source_path: `tsref/status-bar.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/status-bar.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: The Status bar in the TestStand Sequence Editor contains the following elements, which are arranged from left to right: User —The user name of the user currently logged in. Environment —The TestStand environment in which the application is running. Model —The process model the current sequence uses.

### Status Bar

The Status bar in the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 contains the following elements, which are arranged from left to right:

- User 
 —The user name of the user currently logged in.
- Environment 
 —The TestStand
 environment 
 in which the application is running.
- Model 
 —The process model the current sequence uses. Double-click to open the process model.
- Selected Steps 
 —The number of selected steps and the zero-based indexes of the selected steps. This portion of the status bar is only visible in the Sequence File window.
- Number of Steps 
 —The number of steps in the step list. This portion of the status bar is only visible in the Sequence File window.
- Report Location 
 —The location of the test report for the Execution window. Double-click to open File Explorer in the location where the currently displayed report is saved. Usually, the process model populates the Report Location with the pathname of the file to which the model writes the report. This element may not be available until after executing the client sequence.
 During an execution, each execution has a test report. When you click the
 [Report](report-pane-execution-window.html)
 pane, the Execution window displays the location of the test report for the execution in the rightmost box on the Status bar. Usually, the process model populates the Report Location with the pathname of the file to which the model writes the report.

#### See Also

[Report Pane](report-pane-execution-window.html)

Parent topic:

TestStand Sequence Editor Menus, Panes, and Windows

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/status-bar2.html language=enus -->
## TOPIC 04195: Status Bar

- bundle_id: `teststand-api-reference`
- source_path: `tsref/status-bar2.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/status-bar2.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: The TestStand Sequence Analyzer status bar contains the following items, arranged from left to right: Environment —The TestStand environment in which the application is running. Status of Analysis —Current status of the analysis session, such as Analyzing, Completed, Stopped, or Not Analyzed. Messag

### Status Bar

The TestStand Sequence Analyzer status bar contains the following items, arranged from left to right:

- Environment 
 —The TestStand
 environment 
 in which the application is running.
- Status of Analysis 
 —Current status of the analysis session, such as Analyzing, Completed, Stopped, or Not Analyzed.
- Messages Selected 
 —Number of messages you have selected.
- Number of Messages 
 —Number of messages in the Messages list on the
 Analyzer Messages 
 tab the sequence analyzer generated for the current analysis, including the number of Active, Ignored, and Fixed messages.
- Number of Files 
 —Number of files analyzed.

#### See Also

[Analyzer Messages](analyzer-messages-tab-analysis-results-pane.html)
 tab

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/status-bar3.html language=enus -->
## TOPIC 04196: Status Bar

- bundle_id: `teststand-api-reference`
- source_path: `tsref/status-bar3.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/status-bar3.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: The Status bar control, located at the bottom of a TestStand User Interface window, displays the following application state information within its panes, listed in order from left to right: User —Visible for all tabs. Environment —The TestStand environment in which the application is running. Model

### Status Bar

The Status bar control, located at the bottom of a
 [TestStand User Interface](teststand-user-interfaces.html)
 window, displays the following application state information within its panes, listed in order from left to right:

- User 
 —Visible for all tabs.
- Environment 
 —The TestStand
 environment 
 in which the application is running.
- Model 
 —Visible for all tabs.
- Selected Steps 
 —Visible for the
 Sequence File 
 tab and
 Execution 
 tab.
- Number of Steps 
 —Visible for the Sequence File tab and Execution tab.
- Report Location 
 —Visible for the
 Report 
 tab.

#### See Also

[Execution Tab](execution-tab.html)

[Report Tab](report-tab.html)

[Sequence File Tab](sequence-file-tab.html)

Parent topic:

TestStand User Interface Menus and Tabs

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/status-tab-update-vi-calls-dialog-box.html language=enus -->
## TOPIC 04197: Status Tab - Update VI Calls Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/status-tab-update-vi-calls-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/status-tab-update-vi-calls-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Status Tab Displays the status log of all the updates. If a minute or more passes and you do not see any progress messages, click the LabVIEW window to make it active and check for any error dialog boxes. If an error dialog box asks you to continue or stop, always choose Continue . See Also Effectiv

### Status Tab - Update VI Calls Dialog Box

#### Status Tab

Displays the status log of all the updates.

Note

Continue

#### See Also

[Effectively Using LabVIEW with TestStand](/csh?context=ts_10208)

Parent topic:

Update VI/LV NXG VI Calls Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/step-properties-dialog-box.html language=enus -->
## TOPIC 04198: Step Properties Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/step-properties-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/step-properties-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: To examine and modify the values of built-in properties of a step, select Properties from the context menu for a step in the list view of a sequence file in a TestStand User Interface , or call the Engine.DisplayStepPropDialog method. The Step Properties dialog box contains the following tabs: Gener

### Step Properties Dialog Box

To examine and modify the values of built-in properties of a step, select
 Properties
 from the context menu for a step in the list view of a sequence file in a
 [TestStand User Interface](teststand-user-interfaces.html)
 , or call the
 [Engine.DisplayStepPropDialog](../tsapiref/engine-displaysteppropdialog.html)
 method.

The Step Properties dialog box contains the following tabs:

- General 
 — Contains buttons that launch the Specify Module dialog box, the step-type-specific Edit dialog boxes, and the
 Preconditions 
 dialog box.
- Run Options 
 —Various options for loading and running the step
 code module 
 .
- Post Actions 
 —The action to take when the step finishes executing.
- Loop Options 
 —Specifies whether TestStand loops on the step. TestStand can loop a fixed number of times or loop until a specified number of iterations pass or fail. You can also customize the loop conditions.
- Switching 
 —Specifies whether TestStand performs switching operations before the step executes and after the step executes.
- Synchronization 
 —Specifies when TestStand postpones execution of this step or other steps to synchronize the execution of multiple steps. You can also use the Synchronization step types to perform more advanced types of synchronization.
- Expressions 
 —
 Expressions 
 TestStand executes before and after the step executes.
- Requirements 
 —Provides a mechanism for notating product and unit requirements the step covers. This control contains a list of strings where each string represents a single requirement. You can also notate requirements information in the
 Workspace Object Properties 
 ,
 Sequence File Properties 
 , and
 Sequence Properties 
 dialog boxes.

#### See Also

[Engine.DisplayStepPropDialog](../tsapiref/engine-displaysteppropdialog.html)

[Module Tabs and Specify Module Dialog Boxes](specify-module-tabs-and-dialog-boxes.html)

[Sequence File Properties dialog box](sequence-file-properties-dialog-box.html)

[Sequence Properties dialog box](sequence-properties-dialog-box.html)

[Workspace Object Properties dialog box](workspace-object-properties-dialog-box.html)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/step-settings-pane.html language=enus -->
## TOPIC 04199: Step Settings Pane

- bundle_id: `teststand-api-reference`
- source_path: `tsref/step-settings-pane.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/step-settings-pane.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Step Settings pane of the TestStand Sequence Editor to edit the settings of the selected steps in the Steps pane of the active Sequence File window or Execution window. You can modify the values of built-in properties of steps, edit the step-type-specific properties of steps, or specify the

### Step Settings Pane

TestStand Sequence Editor

Steps

Note

You can display the Step Settings pane by right-clicking the steps on the Steps pane and selecting
 Step Settings
 from the context menu, or by selecting
 View»Step Settings
 from the
 [View](view-menu.html)
 menu.

The Step Settings pane contains the following tabs:

- Properties 
 —The values of built-in properties of selected steps.
- Module 
 —The
 code module 
 the selected step calls.
- <
 Step Type
 > Edit Tab 
 —Step-type-specific properties of the selected steps.

#### See Also

[Steps Pane](steps-pane-execution-window.html)

[View Menu](view-menu.html)

Parent topic:

Panes

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/step-settings-tab.html language=enus -->
## TOPIC 04200: Step Settings Tab

- bundle_id: `teststand-api-reference`
- source_path: `tsref/step-settings-tab.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/step-settings-tab.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Step Settings Tab The Step Settings tab of the Property Loader step contains the following options: Sources —Specifies the list of property loader sources on which the step operates. Use the buttons to the right of the control to add, remove, and reorder the sources. The various options that can be

### Step Settings Tab

#### Step Settings Tab

The Step Settings tab of the Property Loader step contains the following options:

Sources
 —Specifies the list of property loader sources on which the step operates. Use the
buttons to the right of the control to add, remove, and reorder the sources. The various options
that can be configured using sources are as follows:

- Source Name—Specifies the name of the property loader source. Use the checkbox to
enable/disable the currently selected source.
- Source Type—Specifies the types of the property loader source from which values are imported to TestStand properties.
- Source Location—Specifies location of the property loader source from which data will
be imported to TestStand properties. If property loader source is file, this specifies the file
path and if property loader source is database, this specifies the connection string.
- View—View the contents of the currently selected property loader source.
- Add—Adds a new source.
- Remove—Removes the currently selected source.
- Move Up—Moves the currently selected source up by one level.
- Move Down—Moves the currently selected source down by one level.

Import All Properties from Source
 —When you enable this option, TestStand ignores the
selected property list and imports all properties from the property loader source.

Apply Imported Values to Related Executions
 —When you enable this option, related
executions share the imported values. Related executions include the original execution that
the application and all subsequent executions TestStand invokes using a SequenceCall step
initiates. For example, when you use the Batch process model, related executions include the
following: the controlling execution, all test socket executions, and any additional executions
these executions invoke.

Import Values To
 —Specifies the target sequence to which values will be imported.

Note

<Current Sequence>

<All Sequences>

When Property Not Present in Source
 —Specifies the action performed when a property is
not found in the source.

When Property Not Present in Destination
 —Specifies the action performed when a
property is not found in the target sequence.

Note

Comments
 —Specifies the comment associated with the currently selected Property Loader
source.

Import Preview
 —Launch the Import Preview dialog which displays the preview of the
changes for the target sequence file when performing import from the current selected source.

Import Preview from All Source
 —Launch the Import Preview dialog which displays the
preview of the changes for the target sequence file when performing import from all the
enabled sources.

Note

Log Data
 —Use the dropbox to select the kind of result logging that needs to be done while
generating report for the property loader step type. The various options that are present are as
follows:

- All Information - Choose this option to log property loader source information, sequence
file path and list of updated properties with its old and new value.
- Summary - Choose this option to log property loader source information and sequence
file path.
- None - Choose this option to don’t log anything in the generated report.

Parent topic:

Configuring a Property Loader Source

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/step-type-edit-tab-step-settings-pane.html language=enus -->
## TOPIC 04201: Step Type Edit Tab - Step Settings Pane

- bundle_id: `teststand-api-reference`
- source_path: `tsref/step-type-edit-tab-step-settings-pane.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/step-type-edit-tab-step-settings-pane.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Step Type Edit Tab Use the Step Type Edit tab to specify step-type-specific properties of a step. The tabs available update based on the type of step you select. Some step types do not support displaying settings on the tab and instead contain buttons to launch edit or configuration dialog boxes. Wh

### Step Type Edit Tab - Step Settings Pane

#### Step Type Edit Tab

Use the Step Type Edit tab to specify step-type-specific properties of a step. The tabs available update based on the type of step you select. Some step types do not support displaying settings on the tab and instead contain buttons to launch edit or configuration dialog boxes. When you open a Step Type Edit tab that contains a button, click the button to launch the edit or configuration dialog box that corresponds to the step type.

The following table lists the name and associated edit tab (in the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 ) or configuration dialog box (in a
 [TestStand User Interface](teststand-user-interfaces.html)
 ) you use to configure instances of the specified step type. Some step types provide the same tab or dialog box to configure steps in both the sequence editor or a user interface.

| Step Type | Edit Tab in the Sequence Editor | Dialog Box in a User Interface |
| --- | --- | --- |
| Built-In Step Types |  |  |
| Synchronization Step Types |  |  |
| Database Step Types |  |  |
| IVI Step Types |  |  |
| LabVIEW Utility Step Types |  |  |
| Property Loader | Edit Property Loader Dialog Box |  |
| Lock | Lock Settings Edit Tab | Lock Step Configuration Dialog Box |
| Rendezvous | Rendezvous Settings Edit Tab | Rendezvous Step Configuration Dialog Box |
| Queue | Queue Settings Edit Tab | Queue Step Configuration Dialog Box |
| Notification | Notification Settings Edit Tab | Notification Step Configuration Dialog Box |
| Wait | Wait Settings Edit Tab | Wait Step Configuration Dialog Box |
| Batch Synchronization | Batch Synchronization Settings Edit Tab | Batch Synchronization Step Configuration Dialog Box |
| Auto Schedule | Auto Schedule Settings Edit Tab | Configure Auto Schedule Step Dialog Box |
| Use Auto Scheduled Resource | Auto Scheduled Resource Settings Edit Tab | Configure Use Auto Scheduled Resource Step Dialog Box |
| Thread Priority | Thread Priority Settings Edit Tab | Thread Priority Configuration Dialog Box |
| Semaphore | Semaphore Settings Edit Tab | Semaphore Step Configuration Dialog Box |
| Batch Specification | Batch Settings Edit Tab | Batch Specification Step Configuration Dialog Box |
| CPU Affinity | CPU Affinity Edit Tab | CPU Affinity Step Configuration Dialog Box |
| Open Database | Edit Open Database Dialog Box |  |
| Open SQL Statement | Edit Open SQL Statement Dialog Box |  |
| Close SQL Statement | Edit Close SQL Statement Dialog Box |  |
| Close Database | Edit Close Database Dialog Box |  |
| Data Operation | Edit Data Operation Dialog Box |  |
| Dmm | Edit IVI Dmm Step Dialog Box |  |
| Scope | Edit IVI Scope Step Dialog Box |  |
| Fgen | Edit IVI Fgen Step Dialog Box |  |
| Power Supply | Edit IVI Power Supply Step Dialog Box |  |
| Switch | Edit IVI Switch Step Dialog Box |  |
| Tools | Edit IVI Tools Step Dialog Box |  |
| Check Remote System Status | Check Remote System Status Edit Tab | Check Remote System Status Step Configuration Dialog Box |
| Run VI Asynchronously | Run VI Asynchronously Edit Tab | Run VI Asynchronously Step Configuration Dialog Box |
| Deploy Library | Deploy Library Edit Tab | Deploy Library Step Configuration Dialog Box |

Note

Parent topic:

Step Settings Pane

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/step-type-menu-editor-dialog-box.html language=enus -->
## TOPIC 04202: Step Type Menu Editor Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/step-type-menu-editor-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/step-type-menu-editor-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Select Customize from the context menu in the Step Types list of the Insertion Palette , or select Step Type Menu Editor from the context menu in the View Types For panel of the Types window to launch the Step Type Menu Editor dialog box in the TestStand Sequence Editor , in which you can use any co

### Step Type Menu Editor Dialog Box

Select
 Customize
 from the context menu in the Step Types list of the
 [Insertion Palette](insertion-palette-pane.html)
 , or select
 Step Type Menu Editor
 from the context menu in the View Types For panel of the
 [Types](types-window.html)
 window to launch the Step Type Menu Editor dialog box in the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 , in which you can use any combination of different type palette files. You can use the Step Type Menu Editor dialog box to ensure that the Step Types list of the Insertion Palette and the Insert Step submenu of the
 [Steps](steps-pane-context-menu-sequence-file-window.html)
 pane context menu properly organizes the step types the type palette files contain. The changes you make in the Step Type Menu Editor dialog box appear in both the Step Types list and the Insert Step submenu.

<TestStand Application Data>

GeneralEngine.cfg

Station Options

Note

GeneralEngine.cfg

GeneralEngine.cfg

The Step Type Menu Editor dialog box contains the following options:

- Groups and Step Types 
 —All step types that appear in the menu. Steps types reside in groups, which appear as folders in the menu. Groups do not appear as items in the menu. Instead, step types that reside in the same group appear together in the menu. However, you can designate that a group appears as a submenu. In this case, the contents of the group appear in a submenu within the menu.
 You can drag and drop step types and groups within the tree control to change the order of appearance of the step types in the menu. When you drag an item over a group, the group highlights to indicate that you can insert the item into the group. A line between two items indicates the item you drag can drop between the items the line separates.
- Preview Menu 
 —Displays a menu that previews the appearance of the Insert Step submenu.
- Move Up/Move Down 
 —Changes the relative order of groups or step types at a particular level in the tree. Use the drag and drop method to change the level of an item in the tree.
- Add Group 
 —Adds a new group to the bottom of the list of groups. Use the drag and drop method to move the group within the tree control.
- Remove Group 
 —Removes the selected group. You can remove a group only if it is empty.
- Rename Group 
 —Renames the selected group in the tree control. Typically, the group name does not appear in the menu. When you move a type palette file to a new system, TestStand use the group name to determine when to group step types from the new file in the same group as existing step types. Step types that specify the same group name appear together even if the step types reside in different files.
- Remove Type 
 —Removes the selected step type. You can only remove a step type not currently loaded into memory. Use this option to remove menu information for step types you no longer need.
- Group Settings/Step Type Settings 
 —Changes the appearance of groups or step types in the menu. Different controls are visible depending on whether you select a group or a step type in the tree.
  - Hide 
 —Removes the selected group or step type from the menu.
  - Separator 
 —Places menu separators around the selected group.
  - Submenu 
 —Causes all step types and subgroups in the selected group to appear inside a submenu.
  - Submenu Display Name Expression 
 —An expression that determines the name of the submenu item if the group appears as a submenu. If the expression is empty or evaluates to an empty string, the submenu name defaults to the name of the group.
 Click the
 Expression Browse
 button to launch the
 [Expression Browser](expression-browser-dialog-box.html)
 dialog box, in which you can browse for properties and functions to build the Submenu Display Name Expression.

#### See Also

[Expression Browser dialog box](expression-browser-dialog-box.html)

[Insertion Palette](insertion-palette-pane.html)

[Steps Pane Context Menu](steps-pane-context-menu-sequence-file-window.html)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/step-type-properties-dialog-box.html language=enus -->
## TOPIC 04203: Step Type Properties Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/step-type-properties-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/step-type-properties-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Select Properties from the context menu for a step type in the Types window to examine and modify the values of the built-in properties. The Step Type properties dialog box contains the following tabs: General —The name, description, and comment for the step type. You can also specify an icon and mo

### Step Type Properties Dialog Box

Select
 Properties
 from the context menu for a step type in the Types window to examine and modify the values of the built-in properties.

The Step Type properties dialog box contains the following tabs:

- General 
 —The name, description, and comment for the step type. You can also specify an icon and module adapter.
- Menu 
 —The menu item name that appears for the step type in the Step Types list of the
 Insertion Palette 
 and Insert Step submenu of the
 Steps 
 pane context menu. Use the
 Step Type Menu Editor 
 dialog box to organize the Step Types list and the Insert Step submenu.
- Substeps 
 —Substeps for the step type. Use substeps to define standard actions, other than calling the
 code module 
 , TestStand performs for all instances of the step type.
- Default Run Options 
 —The initial run option settings for new steps you create from the step type.
- Default Post Actions 
 —The initial post action settings for new steps you create from the step type.
- Default Expressions 
 —The initial expression settings for new steps you create from the step type.
- Disable Properties 
 —Prevents sequence developers from modifying the settings of built-in instance step type properties in individual steps.
- Code Templates 
 —Associates one or more code templates with the step type.
- Version 
 —The version of a type and how TestStand resolves differences between type definitions in separate files.
- Default Loop Options 
 —The initial loop option settings for new steps you create from the step type.
- Default Switching 
 —The initial switching settings for new steps you create from the step type.
- Default Synchronization 
 —The initial synchronization settings for new steps you create from the step type.

Note

Step Properties

The following commands are available at all times in the Step Type Properties dialog box:

- Apply Changes in this Dialog Box to all Loaded Steps of this Type 
 —When you enable this option, the changes you make also apply to all instances of the step type currently in memory. Enabling this option does not update instances of the step type in files not currently loaded.
- View Changes 
 —A list of the properties you have changed since you opened the Step Type Properties dialog box.

Note

#### See Also

[Insertion Palette](insertion-palette-pane.html)

[Step Properties dialog box](step-properties-dialog-box.html)

[Step Settings Pane](step-settings-pane.html)

[Step Type Menu Editor dialog box](step-type-menu-editor-dialog-box.html)

[Steps Pane Context Menu](steps-pane-context-menu-sequence-file-window.html)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/steps-pane-context-menu-execution-tab.html language=enus -->
## TOPIC 04204: Steps Pane Context Menu - Execution Tab

- bundle_id: `teststand-api-reference`
- source_path: `tsref/steps-pane-context-menu-execution-tab.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/steps-pane-context-menu-execution-tab.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Steps Pane Context Menu When execution is suspended at a breakpoint, you can access a context menu for the Steps pane by right-clicking the name or icon of a step. The Steps pane context menu can contain the following items: Breakpoint —Launches a submenu that contains the following options for modi

### Steps Pane Context Menu - Execution Tab

#### Steps Pane Context Menu

When execution is suspended at a breakpoint, you can access a context menu for the
 [Steps](steps-pane-execution-tab.html)
 pane by right-clicking the name or icon of a step.

The Steps pane context menu can contain the following items:

- Breakpoint 
 —Launches a submenu that contains the following options for modifying the breakpoint settings:
  - Toggle Breakpoint 
 —Sets or clears the breakpoint state for the selected steps.
  - Breakpoint Settings 
 —Launches the
 Breakpoint Settings 
 dialog box for the selected step.
- Run Mode 
 —Launches a submenu from which you can set the run mode for the selected steps. The following run mode values are possible:
  - Force to Pass 
 —The step does not execute. Instead, the status of the step is set to
 Passed 
 .
  - Force to Fail 
 —The step does not execute. Instead, the status of the step is set to
 Failed 
 .
  - Skip 
 —The step does not execute. Instead, the status of the step is set to
 Skipped 
 .
  - Normal 
 —The step executes normally.
 Note 
 TestStand does not load the
 [code module](/csh?context=ts_tsfundamentals_bldgblocks_codemodules)
 when the Run Mode for the step is set to Force to Pass, Force to Fail, or Skip.
- Unload and Open Module 
 —Unloads the LabVIEW code module and its dependencies, and opens them in LabVIEW for editing.
- Run Selected Steps 
 Runs the selected steps in interactive mode.
- Loop on Selected Steps 
 —Loops on the selected steps in interactive mode. Before running the steps, this command launches the
 Loop on Selected Steps 
 dialog box, in which you can specify the number of times to loop and a stop condition TestStand evaluates after it executes each step.
- Set Next Step to Cursor 
 —TestStand starts from the selected step when you resume execution.
- Show Step in Variables 
 —Moves from the Steps pane to the
 Variables 
 pane and selects the step you were viewing on the Steps pane. Use this command to view the values of the custom properties of a step after it executes.
- Show Step in Sequence File 
 —Displays the selected step in a Sequence File window.
- Step List Configurations 
 —Lists the layouts the
 Edit Step List Configurations 
 dialog box defines.
  - <
 Default
 > 
 —The default layout for the
 TestStand Sequence Editor 
 .
  - Edit Step List Configurations 
 —Launches the
 Edit Step List Configurations 
 dialog box, in which you can create or modify step list configurations.

#### See Also

[Breakpoint Settings dialog box](breakpoint-settings-dialog-box.html)

[Edit Step List Configurations dialog box](edit-step-list-configurations-dialog-box.html)

[Loop on Selected Steps dialog box](loop-on-selected-steps-dialog-box.html)

[Steps Pane](steps-pane-execution-tab.html)

[Variables Pane](variables-pane-execution-tab.html)

Parent topic:

Steps Pane - Execution Tab

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/steps-pane-context-menu-execution-window.html language=enus -->
## TOPIC 04205: Steps Pane Context Menu - Execution Window

- bundle_id: `teststand-api-reference`
- source_path: `tsref/steps-pane-context-menu-execution-window.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/steps-pane-context-menu-execution-window.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Steps Pane Context Menu When execution is suspended at a breakpoint, you can access a context menu for the Steps pane by right-clicking the name or icon of a step. The Steps pane context menu can contain the following items: Breakpoint —Launches a submenu that contains the following options for modi

### Steps Pane Context Menu - Execution Window

#### Steps Pane Context Menu

When execution is suspended at a breakpoint, you can access a context menu for the
 [Steps](steps-pane-execution-window.html)
 pane by right-clicking the name or icon of a step.

The Steps pane context menu can contain the following items:

- Breakpoint 
 —Launches a submenu that contains the following options for modifying the breakpoint settings:
  - Toggle Breakpoint 
 —Sets or clears the breakpoint state for the selected steps.
  - Breakpoint Settings 
 —Launches the
 Breakpoint Settings 
 dialog box for the selected step.
- Run Mode 
 —Launches a submenu from which you can set the run mode for the selected steps. The following run mode values are possible:
  - Force to Pass 
 —The step does not execute. Instead, the status of the step is set to
 Passed 
 .
  - Force to Fail 
 —The step does not execute. Instead, the status of the step is set to
 Failed 
 .
  - Skip 
 —The step does not execute. Instead, the status of the step is set to
 Skipped 
 .
  - Normal 
 —The step executes normally.
 Note 
 TestStand does not load the
 [code module](/csh?context=ts_tsfundamentals_bldgblocks_codemodules)
 when the Run Mode for the step is set to Force to Pass, Force to Fail, or Skip.
- Set Next Step to Cursor 
 —TestStand starts from the selected step when you resume execution.
- Run Selected Steps 
 —Runs the selected steps in interactive mode.
- Loop on Selected Steps 
 —Loops on the selected steps in interactive mode. Before running the steps, this command launches the
 Loop on Selected Steps 
 dialog box, in which you can specify the number of times to loop, and a stop condition TestStand evaluates after it executes each step.
- Show Step in Variables 
 —Moves from the Steps pane to the
 Variables 
 pane and selects the step you were viewing on the Steps pane. Use this command to view the values of the custom properties of a step after it executes.
- Show Step in Sequence File 
 —Displays the selected step in a
 Sequence File window 
 .
- Step List Configurations 
 —Lists the layouts the
 Edit Step List Configurations 
 dialog box defines.
  - <
 Default
 > 
 —The default layout for the
 TestStand Sequence Editor 
 .
  - Edit Step List Configurations 
 —Launches the
 Edit Step List Configurations 
 dialog box, in which you can create or modify step list configurations.
- View 
 —Lists the available panes or windows for an execution. These commands are available only when an Execution window is active.
  - Steps 
 —Displays the
 Steps 
 pane, where you can trace the execution of steps.
  - Variables 
 —Displays the
 Variables 
 pane, where you can view and modify variables and properties values for the active context when an execution is suspended.
  - Report 
 —Displays the
 Report 
 pane, where you can view the report for the execution.

#### See Also

[Breakpoint Settings dialog box](breakpoint-settings-dialog-box.html)

[Edit Step List Configurations dialog box](edit-step-list-configurations-dialog-box.html)

[Loop on Selected Steps dialog box](loop-on-selected-steps-dialog-box.html)

[Report Pane](report-pane-execution-window.html)

[Steps Pane](steps-pane-execution-window.html)

[Variables Pane](variables-pane-execution-window.html)

Parent topic:

Steps Pane - Execution Window

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/steps-pane-context-menu-sequence-file-tab.html language=enus -->
## TOPIC 04206: Steps Pane Context Menu - Sequence File Tab

- bundle_id: `teststand-api-reference`
- source_path: `tsref/steps-pane-context-menu-sequence-file-tab.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/steps-pane-context-menu-sequence-file-tab.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Steps Pane Context Menu To access the context menu, right-click the Steps pane. The items in the context menu vary depending on whether you right-click a step or the background area of the pane. The Steps pane context menu can contain the following items: Insert Step —Selects the type of step you wa

### Steps Pane Context Menu - Sequence File Tab

#### Steps Pane Context Menu

To access the context menu, right-click the Steps pane. The items in the context menu vary depending on whether you right-click a step or the background area of the pane.

The Steps pane context menu can contain the following items:

- Insert Step 
 —Selects the type of step you want to insert into the sequence.
 You can use many of the steps types in the Insert Step submenu to call
 code modules 
 . Of these step types, some can work with all module adapters, while others require a specific module adapter. Each module adapter calls a category of code modules, such as LabVIEW VIs, LabWindows/CVI source or object modules, or DLLs. Some module adapters also know how to control the ADEs in which you build these types of code modules.
 Before you insert a step that can call a code module using any adapter, you must select the appropriate module adapter for the type of code module you want the step to call. Select the adapter icon from the
 Insertion Palette 
 . If a step type in the Insert Step submenu can work with any adapter, the icon for the module adapter currently selected in the toolbar appears beside the step type. When you insert a step, the adapter icon also appears beside the step name.
 When a step type in the Insert Step submenu works with only one specific module adapter, the icon for the module adapter appears beside the step type. After you insert a step using one of these step types, the adapter icon also appears beside the step name.
 When you insert a step that does not call a code module, such as a Goto or Label step, the currently selected adapter has no effect. These step types have unique icons. These icons appear next to the step types in the Insert Step submenu and next to the steps you create using these step types.
- Adapter 
 —Selects the module adapter to use for inserting new steps.
- Edit Menu 
 —The full name of the Edit Menu item varies according to the type of the selected step. For example, the menu item name is Edit Message Settings for a Message Popup step, Edit Limits for a Numeric List Test step, and Edit Destination for a Goto step. For each step, the menu item invokes a dialog box in which you edit the settings unique to the type of the step. Some step types, such as the Label step and the Action step, do not have step-type-specific settings. For these step types, this menu item is disabled. When a step type has more than one Edit substep, the step type may provide more than one Edit menu item.
- Specify Module 
 —Launches the
 Specify Module 
 dialog box for the selected step, according to the module adapter for the step. Use the Specify Module dialog box to specify the code module the step calls. You can also specify options TestStand uses when it calls the step.
- Edit Code 
 —Displays the source code for the code module the step calls. TestStand uses the module adapter for the step to determine the appropriate application in which to display the source code.
- Preconditions 
 —Launches the
 Preconditions 
 dialog box, in which you can specify the conditions that must be true for each step in the sequence to run. When you launch this dialog box from the
 General 
 tab of the
 Step Properties 
 dialog box, it applies only to a particular step. When you launch the dialog box from the
 General 
 tab of the
 Sequence Properties 
 dialog box, you can view and edit the preconditions for each step in the sequence.
- Breakpoint 
 —Launches a submenu that contains the following options for modifying the breakpoint settings:
  - Toggle Breakpoint 
 —Sets or clears the breakpoint state for the selected steps.
  - Breakpoint Settings 
 —Launches the
 Breakpoint Settings 
 dialog box for the selected step.
- Run Mode 
 —Displays a submenu from which you can set the following run mode values for the selected steps:
  - Force to Pass 
 —TestStand does not execute the step. Instead, TestStand automatically sets the status of the step to
 Passed 
 .
  - Force to Fail 
 —TestStand does not execute the step. Instead, TestStand automatically sets the status of the step to
 Failed 
 .
  - Skip 
 —TestStand does not execute the step. Instead, TestStand automatically sets the status of the step to
 Skipped 
 .
  - Normal 
 —The step executes normally.
 Note 
 TestStand does not load the code module when the Run Mode for the step is set to Force to Pass, Force to Fail, or Skip.
- Cut 
 —Removes the selected steps and places them onto the clipboard. The
 TestStand Sequence Editor 
 maintains the unique IDs for the steps for the first paste operation and generates new unique IDs for the steps in subsequent paste operations.
- Copy 
 —Copies the selected steps and places the steps into the clipboard. The sequence editor does not maintain the unique IDs for the steps.
- Paste 
 —Inserts the steps from the clipboard below the currently selected step or at the end of the sequence. The sequence editor maintains the unique IDs for the steps for the first paste operation and generates new unique IDs for the steps in subsequent paste operations.
- Delete 
 —Removes the selected steps from the step list.
- Rename 
 —Edit the name of the selected step. The sequence editor does not alter unique IDs for the step.
- Run Selected Steps 
 —Runs the selected steps in
 interactive mode 
 .
- Run Selected Steps Using 
 —Executes the selected steps using the process model entry point you select. When you loop on steps with an entry point such as Single Pass, the process model can generate a report and log the results to a database.
- Loop on Selected Steps 
 —Loops on the selected steps in interactive mode. Before running the steps, this command launches the
 Loop On Selected Steps 
 dialog box, in which you can specify how many times to loop.
- Loop on Selected Steps Using 
 —Interactively loops on the selected steps using the process model entry point you select. When you loop on steps with an entry point such as Single Pass, the process model can generate a report and log the results to a database.
- Step List Configurations 
 —Lists the layouts the
 Edit Step List Configurations 
 dialog box defines.
  - <Default> 
 —The default layout for the sequence editor.
  - Edit Step List Configuration 
 —Launches the
 Edit Step List Configurations 
 dialog box, in which you can create and modify layouts and settings for the Steps pane of the user interface.
- Step Properties 
 —Launches the
 Step Properties 
 dialog box, in which you can examine and modify the values of built-in properties of a step.

#### See Also

[Breakpoint Settings dialog box](breakpoint-settings-dialog-box.html)

[Edit Step List Configurations dialog box](edit-step-list-configurations-dialog-box.html)

[Insertion Palette Pane](insertion-palette-pane-sequence-file-tab.html)

[Loop On Selected Steps dialog box](loop-on-selected-steps-dialog-box.html)

[Preconditions dialog box](preconditions-dialog-box.html)

[Sequence Properties dialog box](sequence-properties-dialog-box.html)

[Specify Module Tabs and Dialog Boxes](specify-module-tabs-and-dialog-boxes.html)

[Step Properties dialog box](step-properties-dialog-box.html)

Parent topic:

Steps Pane - Sequence File Tab

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/steps-pane-context-menu-sequence-file-window.html language=enus -->
## TOPIC 04207: Steps Pane Context Menu - Sequence File Window

- bundle_id: `teststand-api-reference`
- source_path: `tsref/steps-pane-context-menu-sequence-file-window.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/steps-pane-context-menu-sequence-file-window.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Steps Pane Context Menu To access the context menu, right-click the Steps pane. The items in the context menu vary depending on whether you right-click a step or the background area of the pane. The Steps pane context menu can contain the following items: Insert Step —Selects the type of step you wa

### Steps Pane Context Menu - Sequence File Window

#### Steps Pane Context Menu

To access the context menu, right-click the
 [Steps](steps-pane-sequence-file-window.html)
 pane. The items in the context menu vary depending on whether you right-click a step or the background area of the pane.

The Steps pane context menu can contain the following items:

- Insert Step 
 —Selects the type of step you want to insert into the sequence.
 You can use many of the steps types in the Insert Step submenu to call
 [code modules](/csh?context=ts_tsfundamentals_bldgblocks_codemodules)
 . Of these step types, some can work with all module adapters, while others require a specific module adapter. Each module adapter calls a category of code modules, such as LabVIEW VIs, LabWindows/CVI source or object modules, or DLLs. Some module adapters also know how to control the ADEs in which you build these types of code modules. 
 Before you insert a step that can call a code module using any adapter, you must select the appropriate module adapter for the type of code module you want the step to call. Select the adapter icon from the
 [Insertion Palette](insertion-palette-pane.html)
 . If a step type in the Insert Step submenu can work with any adapter, the icon for the module adapter currently selected in the toolbar appears beside the step type. When you insert a step, the adapter icon also appears beside the step name. 
 When a step type in the Insert Step submenu works with only one specific module adapter, the icon for the module adapter appears beside the step type. After you insert a step using one of these step types, the adapter icon also appears beside the step name. 
 When you insert a step that does not call a code module, such as a Goto or Label step, the currently selected adapter has no effect. These step types have unique icons. These icons appear next to the step types in the Insert Step submenu and next to the steps you create using these step types.
- Surround Selection With 
 —Surrounds the selected block of contiguous steps with a default set of corresponding begin and end Flow Control or Auto Schedule steps. You can select from the following step types, and you can
 configure custom step types to appear in this list 
 :
  - If
  - For
  - For Each
  - While
  - Do While
  - Select
  - Case
  - Auto Schedule
  - Use Auto Scheduled Resource
- Edit Menu 
 —The full name of the Edit Menu item varies according to the type of the selected step. For example, the menu item name is Text and Buttons for a Message Popup step, Edit Limits for a Numeric List Test step, and Edit Destination for a Goto step. For each step, the menu item either displays a tab of the
 Step Settings 
 pane or invokes a dialog box in which you edit the settings unique to the type of the step. Some step types, such as the Label step and the Action step, do not have step-type-specific settings. For these step types, this menu item is disabled. When a step type has more than one Edit substep, the step type may provide more than one Edit menu item.
- Specify Module 
 —Opens the
 Module 
 tab on the
 Step Settings 
 pane for the selected step, according to the module adapter for the step. Use the Module tab to specify the code module the step calls. You can also specify options TestStand uses when it calls the step.
- Edit Code 
 —Displays the source code for the code module the step calls. TestStand uses the module adapter for the step to determine the appropriate application in which to display the source code.
- Step Settings 
 —Displays the
 Step Settings 
 pane where you can specify the module and settings for the active step or steps selected on the Steps pane of a Sequence File window. The Step Settings pane also displays the module and settings for the selected step or steps on the Steps pane of an Execution window.
- New Subsequence from Steps 
 —Allows you to
 create a subsequence from selected steps 
 .
- Breakpoint 
 —Launches a submenu that contains the following options for modifying the breakpoint settings:
  - Toggle Breakpoint 
 —Sets or clears the breakpoint state for the selected steps.
  - Breakpoint Settings 
 —Launches the
 Breakpoint Settings 
 dialog box for the selected step.
- Run Mode 
 —Displays a submenu from which you can set the following run mode values for the selected steps:
  - Force to Pass 
 —The step does not execute. Instead, the status of the step is set to
 Passed 
 .
  - Force to Fail 
 —The step does not execute. Instead, the status of the step is set to
 Failed 
 .
  - Skip 
 —The step does not execute. Instead, the status of the step is set to
 Skipped 
 .
  - Normal 
 —The step executes normally.
 Note 
 TestStand does not load the code module when the Run Mode for the step is set to Force to Pass, Force to Fail, or Skip.
- Cut 
 —Removes the selected steps and places them onto the clipboard. The
 TestStand Sequence Editor 
 maintains the unique IDs for the steps for the first paste operation and generates new unique IDs for the steps in subsequent paste operations.
- Copy 
 —Copies the selected steps and places the steps into the clipboard. The sequence editor does not maintain the unique IDs for the steps.
- Paste 
 —Inserts the steps from the clipboard below the currently selected step or at the end of the sequence. The sequence editor maintains the unique IDs for the steps for the first paste operation and generates new unique IDs for the steps in subsequent paste operations.
- Delete 
 —Removes the selected steps from the step list.
- Run Selected Steps 
 —Runs the selected steps in
 interactive mode 
 .
- Run Selected Steps Using 
 —Executes the selected steps using the process model entry point you select. When you loop on steps with an entry point such as Single Pass, the process model can generate a report and log the results to a database. The Run Selected Steps Using command is available only in a Sequence File window.
- Loop on Selected Steps 
 —Loops on the selected steps in interactive mode. Before running the steps, this command launches the
 Loop On Selected Steps 
 dialog box, in which you can specify how many times to loop.
- Loop on Selected Steps Using 
 —Interactively loops on the selected steps using the process model entry point you select. When you loop on steps with an entry point such as Single Pass, the process model can generate a report and log the results to a database. The Loop on Selected Steps Using command is available only in a Sequence File window.
- Step List Configurations 
 —Lists the layouts the
 Edit Step List Configurations 
 dialog box defines.
  - <Default> 
 —The default layout for the sequence editor.
  - Edit Step List Configuration 
 —Launches the
 Edit Step List Configurations 
 dialog box, in which you can create and modify layouts and settings for the Steps pane of the sequence editor.
- View 
 —Lists the available panes or windows for a sequence file. These commands are available only when a Sequence File window is active.
  - Steps 
 —Displays the
 Steps 
 pane where you edit the steps in the Setup, Main, and Cleanup step groups for the sequence file.
  - Sequences 
 —Displays the
 Sequences 
 pane where you edit the sequences in the sequence file.
  - Variables 
 —Displays the
 Variables 
 pane where you edit the locals, parameters, and file globals for the sequence file and station globals.
  - Types 
 —Displays the
 Types 
 window where you can edit step types, custom data types, and built-in data types. The sequence editor selects the active sequence file in the Type Palettes window.
- Display File Hierarchy 
 —Displays a graph in the
 Sequence Hierarchy 
 window of the hierarchy of all sequences in the sequence file.
- Display Hierarchy Using 
 —Displays a graph in the Sequence Hierarchy window of the hierarchy of all sequence calls starting at the process model entry point you select. The list of entry points varies according to the process model the sequence file uses. This option uses the current sequence file as a client sequence file.

#### See Also

[Adding Step Types to Surround Selection With Context Menu](/csh?context=ts_tsfundamentals_addtoencapsulatewithcm)

[Breakpoint Settings dialog box](breakpoint-settings-dialog-box.html)

[Edit Step List Configurations dialog box](edit-step-list-configurations-dialog-box.html)

[Insertion Palette](insertion-palette-pane.html)

[Loop On Selected Steps dialog box](loop-on-selected-steps-dialog-box.html)

[Sequence Hierarchy Window](sequence-hierarchy-window.html)

[Sequences Pane](sequences-pane-sequence-file-window.html)

[Steps Pane](steps-pane-sequence-file-window.html)

[Step Settings Pane](step-settings-pane.html)

[Types Window](types-window.html)

[Variables Pane](variables-pane-sequence-file-window4.html)

Parent topic:

Steps Pane - Sequence File Window

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/steps-pane-execution-tab.html language=enus -->
## TOPIC 04208: Steps Pane - Execution Tab

- bundle_id: `teststand-api-reference`
- source_path: `tsref/steps-pane-execution-tab.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/steps-pane-execution-tab.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Steps Pane The Steps pane displays a list of steps in the currently executing step group for the sequence invocation currently selected on the Call Stack pane. The Steps pane contains the following columns: Step —The name and icon of the step. Click in the space to the left of the step icon to toggl

### Steps Pane - Execution Tab

#### Steps Pane

The Steps pane displays a list of steps in the currently executing step group for the sequence invocation currently selected on the
 [Call Stack](call-stack-pane-execution-tab.html)
 pane. The Steps pane contains the following columns:

- Step 
 —The name and icon of the step. Click in the space to the left of the step icon to toggle the breakpoint for the step.
- Description 
 —A description of the step that varies according to the type of step and the module adapter that it uses.
- Settings 
 —The properties of the step that contain non-default values.
- Status 
 —The value of the status property for the step. If the step has not yet executed, the status is an empty string. After the step executes, the status reflects the results of the execution. Possible status values can vary based on the type of step. Typical values include
 Passed 
 ,
 Failed 
 ,
 Done 
 , and
 Error 
 .

When execution is suspended at a breakpoint, you can view the steps of any of the active sequences on the callstack. Use the
 [Call Stack](call-stack-pane-execution-tab.html)
 pane to select the active sequence invocation to display on the Steps pane. Use the
 [Threads](threads-pane-execution-tab.html)
 pane to select which thread the Call Stack pane displays.

#### Tracing Enabled

Use the
 Tracing Enabled
 item in the
 [Execute](execute-menu2.html)
 menu to enable or disable tracing.

If you enable tracing, the
 [TestStand User Interfaces](teststand-user-interfaces.html)
 display the progress of an execution with a yellow arrow icon located to the left of the icon for the currently executing step. This icon is called the execution pointer. When the execution suspends at a breakpoint, the Steps pane displays the execution pointer next to the step that runs when execution resumes. After each step completes, the Execution tab updates the contents of the Steps pane and the position of the execution pointer.

If tracing is disabled, the Execution tab does not update until execution suspends at a breakpoint. The Steps pane might display no steps at all, or it might contain the steps and execution pointer displayed at the most recent breakpoint. Disable tracing when you want to avoid using computer time to display the progress of the execution.

When execution is suspended, you can access the
 [Steps Pane](steps-pane-context-menu-execution-tab.html)
 context menu by right-clicking the Steps pane.

#### See Also

[Call Stack Pane](call-stack-pane-execution-tab.html)

[Execute Menu](execute-menu2.html)

[Steps Pane Context Menu](steps-pane-context-menu-execution-tab.html)

[Threads Pane](threads-pane-execution-tab.html)

Parent topic:

Execution Tab

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/steps-pane-execution-window.html language=enus -->
## TOPIC 04209: Steps Pane - Execution Window

- bundle_id: `teststand-api-reference`
- source_path: `tsref/steps-pane-execution-window.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/steps-pane-execution-window.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Steps Pane The Steps pane displays a list of steps in the currently executing step group for the sequence invocation currently selected on the Call Stack pane. The toolbar contains the following buttons: Command Name Shortcut Icon Description Resume <F5> Continues the execution when the sequence exe

### Steps Pane - Execution Window

#### Steps Pane

The Steps pane displays a list of steps in the currently executing step group for the sequence invocation currently selected on the
 [Call Stack](call-stack-pane.html)
 pane.

The toolbar contains the following buttons:

| Command Name | Shortcut | Icon | Description |
| --- | --- | --- | --- |
| Resume | <F5> |  | Continues the execution when the sequence execution is suspended at a breakpoint. |
| Restart |  | Initiates a restart of the execution in the active Execution window . The TestStand Sequence Analyzer does not reanalyze sequences when you restart an execution. |  |
| Break | <Ctrl-F9> |  | Suspends the active execution after completing the execution of the current step. |
| Terminate Execution | <Ctrl-Shift-F9> |  | Terminates a running or suspended execution. A running execution only terminates after completing the currently executing step. When you terminate an execution, TestStand runs the Cleanup step groups for all active sequences on the call stack. |
| Step Into | <F8> |  | Enters and suspends within a function, VI, or sequence the step calls. If the step calls a code module TestStand cannot suspend within, TestStand suspends the execution at the next step. Note When you step into a VI from TestStand and then select Return to Caller without executing the VI, any values you change in the controls or indicators of the suspended VI are not returned to TestStand. |
| Step Over | <F10> |  | Executes the step to which the execution pointer points when the sequence execution is in a breakpoint state. If the step is a Sequence Call step to another sequence, Step Over executes the entire sequence. The execution then enters a breakpoint state on the step following the Sequence Call step. If the engine encounters a breakpoint within the Sequence Call step, the execution pauses at the breakpoint. |
| Step Out | <Shift-F8> |  | Resumes execution through the end of the current sequence and suspends/pauses on the next step in the calling sequence. |
| Resume All | — |  | Continues any suspended execution. |
| Break All | — |  | Suspends all executions. A running execution only suspends after completing the currently executing step. |
| Terminate All | — |  | Terminates all running or suspended executions. A running execution only terminates after completing the currently executing step. When you terminate an execution, TestStand runs the Cleanup step groups for all active sequences on the call stack. |

The Steps pane contains the following columns:

- Step 
 —The name and icon of the step. Click in the space to the left of the step icon to toggle the breakpoint for the step.
- Description 
 —A description of the step that varies according to the type of step and the module adapter that it uses.
- Settings 
 —The properties of the step that contain non-default values.
- Status 
 —The value of the status property for the step. If the step has not yet executed, the status is an empty string. After the step executes, the status reflects the results of the execution. Possible status values can vary based on the type of step. Typical values include
 Passed 
 ,
 Failed 
 ,
 Done 
 , and
 Error 
 .

When execution is suspended at a breakpoint, you can view the steps of any of the active sequences on the callstack. Use the
 [Call Stack](call-stack-pane.html)
 pane to select the active sequence invocation to display on the Steps pane. Use the
 [Threads](threads-pane.html)
 pane to select which thread the Call Stack pane displays.

#### Tracing Enabled

Use the
 Tracing Enabled
 item in the
 [Execute](execute-menu.html)
 menu to enable or disable tracing.

If you enable tracing, the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 displays the progress of an execution with a yellow arrow icon located to the left of the icon for the currently executing step. This icon is called the execution pointer. When the execution suspends at a breakpoint, the Steps pane displays the execution pointer next to the step that runs when execution resumes. After each step completes, the Execution window updates the contents of the Steps pane, the position of the execution pointer, and the values of any watch expressions on the
 [Watch View](watch-view-pane.html)
 pane.

If tracing is disabled, the Execution window does not update until execution suspends at a breakpoint. The Steps pane might display no steps at all, or it might contain the steps and execution pointer displayed at the most recent breakpoint. Disable tracing when you want to avoid using computer time to display the progress of the execution.

When execution is suspended, you can access the
 [Steps Pane](steps-pane-context-menu-execution-window.html)
 context menu by right-clicking the Steps pane.

#### See Also

[Call Stack Pane](call-stack-pane.html)

[Execute Menu](execute-menu.html)

[Steps Pane Context Menu](steps-pane-context-menu-execution-window.html)

[Threads Pane](threads-pane.html)

[Watch View Pane](watch-view-pane.html)

Parent topic:

Execution Window

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/steps-pane-sequence-file-tab.html language=enus -->
## TOPIC 04210: Steps Pane - Sequence File Tab

- bundle_id: `teststand-api-reference`
- source_path: `tsref/steps-pane-sequence-file-tab.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/steps-pane-sequence-file-tab.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Steps Pane The Setup, Main, and Cleanup groups of the Steps pane display a list of the steps in the step group. This list is called the step list. The step list contains the following default columns: Step —Displays the name of the step and the step icon. Click to the left of the step icon to toggle

### Steps Pane - Sequence File Tab

#### Steps Pane

The Setup, Main, and Cleanup groups of the Steps pane display a list of the steps in the step group. This list is called the step list. The step list contains the following default columns:

- Step 
 —Displays the name of the step and the step icon. Click to the left of the step icon to toggle the breakpoint for the step. If you add a comment for a step, the comment appears in light text above the step name.
- Description 
 —Displays a description of the step that varies according to the type of step and the adapter with which it was created.
- Settings 
 —Displays the properties of the step that contain non-default values. Use the
 Step Properties 
 dialog box to specify step settings.

You can insert new steps in a sequence by dragging and dropping one or more files on to the Steps pane of a user interface in Editor Mode. TestStand inserts Action steps for the files you select and selects the corresponding module adapter. TestStand sets the module path to the name of the file if the file resides in the TestStand search directories. Otherwise, TestStand sets the module path to the absolute path of the file.

By default, the
 [Step Settings](step-settings-pane.html)
 pane contains the following view configurations:
 <Default>
 ,
 Requirements
 ,
 Large
 , and
 Grid
 . Use the
 Step List Configurations
 context menu in the Steps pane to select the configuration the Steps pane uses to display step details. Use the
 [Edit Step List Configurations](edit-step-list-configurations-dialog-box.html)
 dialog box to create and modify layouts and settings for the Steps pane.

Note

Large

#### See Also

[Edit Step List Configurations dialog box](edit-step-list-configurations-dialog-box.html)

[Specify Module Tabs and Dialog Boxes](specify-module-tabs-and-dialog-boxes.html)

[Step Properties dialog box](step-properties-dialog-box.html)

[Step Settings](step-settings-pane.html)
 pane

Parent topic:

Sequence File Tab

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/steps-pane-sequence-file-window.html language=enus -->
## TOPIC 04211: Steps Pane - Sequence File Window

- bundle_id: `teststand-api-reference`
- source_path: `tsref/steps-pane-sequence-file-window.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/steps-pane-sequence-file-window.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Steps Pane The toolbar contains the following buttons: Command Name Shortcut Icon Description Test UUTs <F5> Initiates an execution using the active sequence file as the client sequence file for the Test UUTs Execution entry point in the process model. Single Pass <Ctrl+F5> Initiates an execution us

### Steps Pane - Sequence File Window

#### Steps Pane

The toolbar contains the following buttons:

| Command Name | Shortcut | Icon | Description |
| --- | --- | --- | --- |
| Test UUTs | <F5> |  | Initiates an execution using the active sequence file as the client sequence file for the Test UUTs Execution entry point in the process model. |
| Single Pass | <Ctrl+F5> |  | Initiates an execution using the active sequence file as the client sequence file for the Single Pass Execution entry point in the process model. |
| Run < Sequence > | — |  | Initiates an execution of the active sequence without using a process model. |
| Analyze < file or project name > | — |  | Starts analysis. If the Current Sequence Analyzer Project window is active, the TestStand Sequence Analyzer analyzes the project. If a sequence file or workspace file is active, the sequence analyzer analyzes the sequence file or workspace file using the rules and settings from the current sequence analyzer project. |

When the sequence file is running, the toolbar displays the following buttons:

| Command Name | Shortcut | Icon | Description |
| --- | --- | --- | --- |
| Resume All | — |  | Continues any suspended execution. |
| Break All | — |  | Suspends all executions. A running execution only suspends after completing the currently executing step. |
| Terminate All | — |  | Terminates all running or suspended executions. A running execution only terminates after completing the currently executing step. When you terminate an execution, TestStand runs the Cleanup step groups for all active sequences on the call stack. |

The Setup, Main, and Cleanup groups of the Steps pane display a list of the steps in the step group. This list is called the step list. The step list contains the following default columns:

- Step 
 —Displays the name of the step and the step icon. Click to the left of the step icon to toggle the breakpoint for the step. If you add a comment for a step, the comment appears in light text above the step name.
 You can distinguish between step types on the Steps pane according to the colors the icons use. The following table lists the color corresponding to each step type: 
 Step Type
 ColorTest
 Magenta
 Action
 Green
 Sequence Call
 Blue
 Label
 Purple
 Flow Control
 Brown
 Other
 Green
- Description 
 —Displays a description of the step that varies according to the type of step and the adapter with which it was created.
- Settings 
 —Displays the properties of the step that contain non-default values. Use the
 Step Settings 
 pane to specify step settings.

You can insert new steps in a sequence by dragging and dropping one or more files on to the Steps pane. TestStand inserts Action steps for the files you select and selects the corresponding module adapter. TestStand sets the module path to the name of the file if the file resides in the TestStand search directories. Otherwise, TestStand sets the module path to the absolute path of the file.

By default, the
 [Step Settings](step-settings-pane.html)
 pane contains the following view configurations:
 <Default>
 ,
 Requirements
 , and
 Large
 . Use the
 Step List Configurations
 context menu in the Steps pane to select the configuration the Steps pane uses to display step details. Use the
 [Edit Step List Configurations](edit-step-list-configurations-dialog-box.html)
 dialog box to create and modify layouts and settings for the Steps pane.

Note

Large

#### See Also

[Edit Step List Configurations dialog box](edit-step-list-configurations-dialog-box.html)

[Steps Pane Context Menu](steps-pane-context-menu-sequence-file-window.html)

[Step Settings pane](step-settings-pane.html)

Parent topic:

Sequence File Window

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/stop-expression-tab-loop-on-selected-steps-di.html language=enus -->
## TOPIC 04212: Stop Expression Tab - Loop on Selected Steps Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/stop-expression-tab-loop-on-selected-steps-di.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/stop-expression-tab-loop-on-selected-steps-di.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Stop Expression Tab The Stop Expression tab contains the following options: Specify Custom Stop Expression —When you enable this option, TestStand stops the interactive execution when the expression in the Stop Expression control evaluates to True . When you enable this option, the Stop On Condition

### Stop Expression Tab - Loop on Selected Steps Dialog Box

#### Stop Expression Tab

The Stop Expression tab contains the following options:

- Specify Custom Stop Expression 
 —When you enable this option, TestStand stops the interactive execution when the expression in the Stop Expression control evaluates to
 True 
 . When you enable this option, the Stop On Condition control dims on the
 Loop Count 
 tab.
- Stop Expression 
 —The custom expression, which stops the interactive expression when it evaluates to
 True 
 . Click the
 Expression Browse 
 button to launch the
 Expression Browser 
 dialog box.

#### See Also

[Expression Browser dialog box](expression-browser-dialog-box.html)

Parent topic:

Loop on Selected Steps Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/stream-loop-dialog-box.html language=enus -->
## TOPIC 04213: Stream Loop Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/stream-loop-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/stream-loop-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Stream Loop dialog box in a TestStand User Interface to configure the Stream Loop step. Input Group Box The Input group box in the Stream Loop dialog box contains the following options: Input Record Stream —Specifies an object reference to the InputRecordStream over which to iterate. Auto Cl

### Stream Loop Dialog Box

Use the Stream Loop dialog box in a
 [TestStand User Interface](teststand-user-interfaces.html)
 to configure the Stream Loop step.

#### Input Group Box

The
 Input
 group box in the Stream Loop dialog box contains the following options:

- Input Record Stream 
 —Specifies an object reference to the
 InputRecordStream 
 over which to iterate.
  - Auto Close 
 —Check this box to automatically clean up the input stream at the end of the loop. When this box is checked, upon terminating the loop, the Stream Loop step closes the stream and sets the object reference in the
 InputRecordStream 
 expression to
 Nothing 
 .
 Note 
 Cleanup occurs only if the loop terminates normally by encountering the end of file (EOF) or as a result of a
 [Break step](break-step.html)
 . Cleanup does not occur if execution flow exits the loop for some other reason, such as via a
 [Goto step](goto-step.html)
 . 
 Leave this box unchecked to continue using the stream after the loop terminates and/or close the stream yourself by calling the
 InputRecordStream.Close 
 method through the TestStand API.
- Input Record 
 —Specifies where to store the next record read from the input stream. The record may be a container, array, or string.
  - If the record is a container, the subproperties represent the fields.
  - If the record is an array, each array element represents a field.
  - If the record is a string, the fields are represented as comma-separated values.
- Field Mapping 
 —(Optional) Specifies the mapping from fields in the stream to elements of the record. The mapping is a comma-separated list of index ranges. For example, "0, 3-5, 8-7" specifies that fields 0 through 5 in the record read from the stream be stored to elements 0, 3, 4, 5, 8, and 7 of the record in the step. The final range in the list may be open-ended. For example, "2, 3-" indicates that fields be stored to elements 2, 3, and all elements beyond 3 of the record in the step.
 If the input record is a container, the range list may include individual subproperty names. For example, "Temperature, Pressure, 0-1" specifies that fields 0 through 3 of the record from the stream be stored to subproperties Temperature and Pressure, followed by the subproperties with index 0 and index 1. 
 Field mapping is not supported when the record specified in the step is a string. Specifying a field mapping with a string record results in a run-time error.
- Iteration 
 —(Optional) An expression that determines the numeric variable or property in which to store the current loop iteration. This is the zero-based offset from the beginning of the loop.

#### Output Group Box

The Output
 group box in the Stream Loop dialog box contains the following options:

- Enable Output 
 —Check this box to enable output for this loop. If checked, the output controls are enabled, and the stream loop will write the specified output record to the specified output stream at the end of each iteration.
- Output Record Stream 
 —Specifies the stream to which to write output data. The expression can be either an object reference or a string. If it is an object reference, it must refer to an
 [OutputRecordStream](../tsapiref/outputrecordstream.html) 
 or
 [ExecutionOutputRecordStream](executionoutputrecordstream-and-executionoutp.html) 
 . If it is a string, it must be the name of an
 ExecutionOutputRecordStream 
 attached to the current execution.
  - Auto Close 
 —Check this box to automatically clean up the output stream at the end of the loop. When this box is checked, upon terminating the loop, the Stream Loop step closes the stream and sets the object reference in the Output Record Stream expression to
 Nothing 
 .
 Note 
 Automatic cleanup occurs only if the loop terminates normally by encountering the end of file (EOF) or a
 [Break step](break-step.html)
 . Cleanup does not occur if execution flow exits the loop for some other reason, such as through a
 [Goto step](goto-step.html)
 . 
 Leave this box unchecked to continue using the stream after the loop terminates and/or close the stream yourself by calling the
 OutputRecordStream.Close 
 method through the TestStand API.
- Output Record 
 —Specifies the record to write to the output stream. The record may be a container or an array.
  - If the record is a container, the subproperties represent the fields.
  - If the record is an array, each array element represents a field.
- Use Input Record 
 —When checked, the record specified by the Input Record expression also specifies the output record. Checking Use Input Record when the input record is a string causes a run-time error because the output record cannot be a string.
- Field Mapping 
 —Specifies the mapping from elements of the record to fields in the stream. The mapping is a comma-separated list of index ranges. For example, "0, 3-5, 8-7" specifies that elements 0, 3, 4, 5, 8, and 7 of the record be written as the fields "0-5" in the stream. The final range in the list may be open-ended. For example, "2, 3-" indicates that elements 2, 3, and all elements beyond 3 of the record be written to the stream.
 If the output record is a container, the range list may include individual subproperty names. For example, "Temperature, Pressure, 0-1" specifies that the subproperties "Temperature" and "Pressure," as well as the elements 0 and 1, be written as fields to the stream.

#### Data Streams API Notes

The Stream Loop step is designed to work with any object that implements the
 InputRecordStream
 or
 OutputRecordStream
 interfaces. The loop reads records using the
 InputRecordStream.ReadRecord
 method. It writes records using the
 OutputRecordStream.WriteRecord
 method. Auto close functionality invokes
 InputRecordStream.Close
 or
 OutputRecordStream.Close
 as appropriate.

For optimization, the step may pre-evaluate the mapping and pass a reordered record consisting of aliases along with an empty mapping string to the underlying stream. This may be done instead of passing the specified mapping string directly to
 ReadRecord
 or
 WriteRecord
 .

#### See Also

[InputRecordStream.ReadRecord](../tsapiref/inputrecordstream-readrecord.html)

[InputRecordStream.Close](../tsapiref/inputrecordstream-close.html)

[OutputRecordStream.WriteRecord](../tsapiref/outputrecordstream-writerecord.html)

[OutputRecordStream.Close](../tsapiref/outputrecordstream-close.html)

[ExecutionOutputRecordStream.WriteRecord](../tsapiref/executionoutputrecordstream-writerecord.html)

[ExecutionOutputRecordStream.Close](../tsapiref/executionoutputrecordstream-close.html)

Parent topic:

Stream Loop Step

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/stream-loop-edit-tab.html language=enus -->
## TOPIC 04214: Stream Loop Edit Tab

- bundle_id: `teststand-api-reference`
- source_path: `tsref/stream-loop-edit-tab.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/stream-loop-edit-tab.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Stream Loop edit tab in the TestStand Sequence Editor to configure the Stream Loop step. Input Group Box The Input group box in the Stream Loop edit tab contains the following options: Input Record Stream —Specifies an object reference to the InputRecordStream over which to iterate. Auto Clo

### Stream Loop Edit Tab

Use the Stream Loop edit tab in the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 to configure the Stream Loop step.

#### Input Group Box

The
 Input
 group box in the Stream Loop edit tab contains the following options:

- Input Record Stream 
 —Specifies an object reference to the
 InputRecordStream 
 over which to iterate.
  - Auto Close 
 —Check this box to automatically clean up the input stream at the end of the loop. When this box is checked, upon terminating the loop, the Stream Loop step closes the stream and sets the object reference in the
 InputRecordStream 
 expression to
 Nothing 
 .
 Note 
 Cleanup occurs only if the loop terminates normally by encountering the end of file (EOF) or as a result of a
 [Break step](break-step.html)
 . Cleanup does not occur if execution flow exits the loop for some other reason, such as via a
 [Goto step](goto-step.html)
 . 
 Leave this box unchecked to continue using the stream after the loop terminates and/or close the stream yourself by calling the
 InputRecordStream.Close 
 method through the TestStand API.
- Input Record 
 —Specifies where to store the next record read from the input stream. The record may be a container, array, or string.
  - If the record is a container, the subproperties represent the fields.
  - If the record is an array, each array element represents a field.
  - If the record is a string, the fields are represented as comma-separated values.
- Field Mapping 
 —(Optional) Specifies the mapping from fields in the stream to elements of the record. The mapping is a comma-separated list of index ranges. For example, "0, 3-5, 8-7" specifies that fields 0 through 5 in the record read from the stream be stored to elements 0, 3, 4, 5, 8, and 7 of the record in the step. The final range in the list may be open-ended. For example, "2, 3-" indicates that fields be stored to elements 2, 3, and all elements beyond 3 of the record in the step.
 If the input record is a container, the range list may include individual subproperty names. For example, "Temperature, Pressure, 0-1" specifies that fields 0 through 3 of the record from the stream be stored to subproperties Temperature and Pressure, followed by the subproperties with index 0 and index 1. 
 Field mapping is not supported when the record specified in the step is a string. Specifying a field mapping with a string record results in a run-time error.
- Iteration 
 —(Optional) An expression that determines the numeric variable or property in which to store the current loop iteration. This is the zero-based offset from the beginning of the loop.

#### Output Group Box

The Output
 group box in the Stream Loop edit tab contains the following options:

- Enable Output 
 —Check this box to enable output for this loop. If checked, the output controls are enabled, and the stream loop will write the specified output record to the specified output stream at the end of each iteration.
- Output Record Stream 
 —Specifies the stream to which to write output data. The expression can be either an object reference or a string. If it is an object reference, it must refer to an
 [OutputRecordStream](../tsapiref/outputrecordstream.html) 
 or
 [ExecutionOutputRecordStream](executionoutputrecordstream-and-executionoutp.html) 
 . If it is a string, it must be the name of an
 ExecutionOutputRecordStream 
 attached to the current execution.
  - Auto Close 
 —Check this box to automatically clean up the output stream at the end of the loop. When this box is checked, upon terminating the loop, the Stream Loop step closes the stream and sets the object reference in the Output Record Stream expression to
 Nothing 
 .
 Note 
 Automatic cleanup occurs only if the loop terminates normally by encountering the end of file (EOF) or a
 [Break step](break-step.html)
 . Cleanup does not occur if execution flow exits the loop for some other reason, such as through a
 [Goto step](goto-step.html)
 . 
 Leave this box unchecked to continue using the stream after the loop terminates and/or close the stream yourself by calling the
 OutputRecordStream.Close 
 method through the TestStand API.
- Output Record 
 —Specifies the record to write to the output stream. The record may be a container or an array.
  - If the record is a container, the subproperties represent the fields.
  - If the record is an array, each array element represents a field.
- Use Input Record 
 —When checked, the record specified by the Input Record expression also specifies the output record. Checking Use Input Record when the input record is a string causes a run-time error because the output record cannot be a string.
- Field Mapping 
 —Specifies the mapping from elements of the record to fields in the stream. The mapping is a comma-separated list of index ranges. For example, "0, 3-5, 8-7" specifies that elements 0, 3, 4, 5, 8, and 7 of the record be written as the fields "0-5" in the stream. The final range in the list may be open-ended. For example, "2, 3-" indicates that elements 2, 3, and all elements beyond 3 of the record be written to the stream.
 If the output record is a container, the range list may include individual subproperty names. For example, "Temperature, Pressure, 0-1" specifies that the subproperties "Temperature" and "Pressure," as well as the elements 0 and 1, be written as fields to the stream.

#### Data Streams API Notes

The Stream Loop step is designed to work with any object that implements the
 InputRecordStream
 or
 OutputRecordStream
 interfaces. The loop reads records using the
 InputRecordStream.ReadRecord
 method. It writes records using the
 OutputRecordStream.WriteRecord
 method. Auto close functionality invokes
 InputRecordStream.Close
 or
 OutputRecordStream.Close
 as appropriate.

For optimization, the step may pre-evaluate the mapping and pass a reordered record consisting of aliases along with an empty mapping string to the underlying stream. This may be done instead of passing the specified mapping string directly to
 ReadRecord
 or
 WriteRecord
 .

#### See Also

[InputRecordStream.ReadRecord](../tsapiref/inputrecordstream-readrecord.html)

[InputRecordStream.Close](../tsapiref/inputrecordstream-close.html)

[OutputRecordStream.WriteRecord](../tsapiref/outputrecordstream-writerecord.html)

[OutputRecordStream.Close](../tsapiref/outputrecordstream-close.html)

[ExecutionOutputRecordStream.WriteRecord](../tsapiref/executionoutputrecordstream-writerecord.html)

[ExecutionOutputRecordStream.Close](../tsapiref/executionoutputrecordstream-close.html)

Parent topic:

Stream Loop Step

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/stream-loop-step.html language=enus -->
## TOPIC 04215: Stream Loop Step

- bundle_id: `teststand-api-reference`
- source_path: `tsref/stream-loop-step.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/stream-loop-step.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Stream Loop step to define a block of steps that execute once for each element in an InputRecordStream . Configuring the Step Use the Stream Loop edit tab in the TestStand Sequence Editor or the Configure Stream Loop dialog in a TestStand User Interface to configure the Stream Loop step.

### Stream Loop Step

Use the Stream Loop step to define a block of steps that execute once for each element in an
 [InputRecordStream](the-inputrecordstream-and-outputrecordstream.html)
 .

#### Configuring the Step

Use the
 [Stream Loop edit tab](stream-loop-edit-tab.html)
 in the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 or the
 [Configure Stream Loop dialog](stream-loop-dialog-box.html)
 in a
 [TestStand User Interface](teststand-user-interfaces.html)
 to configure the Stream Loop step.

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/stream-sweep-parameter-strategy.html language=enus -->
## TOPIC 04216: Stream Sweep Parameter Strategy

- bundle_id: `teststand-api-reference`
- source_path: `tsref/stream-sweep-parameter-strategy.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/stream-sweep-parameter-strategy.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Stream strategy with the Sweep Loop step to specify a parameter that sweeps over the values in an InputRecordStream. To use the Stream strategy, all parameters must be at level 0. No parameters can be nested. When the Stream strategy is selected for a sweep parameter, the following additiona

### Stream Sweep Parameter Strategy

Sweep Loop

InputRecordStream.

Note

When the Stream strategy is selected for a sweep parameter, the following additional option is available:

- Field/Column ID 
 —Specifies the field in the input record containing the sweep parameter value. For any
 InputRecordStream 
 , the field ID may be a number specifying the zero-based index of the field within the record. If the stream is a
 CsvFileInputRecordStream 
 that has a
 prototype 
 , the ID can also be the string name of the field.

Parent topic:

Sweep Parameter Strategies

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/string-parameters-c-c-dll-call-parameters.html language=enus -->
## TOPIC 04217: String Parameters - C/C++ DLL Call Parameters

- bundle_id: `teststand-api-reference`
- source_path: `tsref/string-parameters-c-c-dll-call-parameters.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/string-parameters-c-c-dll-call-parameters.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: String Parameters When using string parameters, use the C String Buffer or Unicode String Buffer type when you want the function to be able to change the contents of the argument in TestStand. Use the C String or Unicode String type when the DLL function does not modify the argument. You can pass a

### String Parameters - C/C++ DLL Call Parameters

#### String Parameters

When using string parameters, use the C String Buffer or Unicode String Buffer type when you want the function to be able to change the contents of the argument in TestStand. Use the C String or Unicode String type when the DLL function does not modify the argument. You can pass a literal string, a TestStand string property, or an expression that evaluates to a string as the value of a string parameter.

The following settings are available in the Data Type ring control when you select String for the category type.

| String Data Type Setting | Equivalent C Data Type |
| --- | --- |
| C String | const char * |
| C String Buffer | char[] |
| Unicode String | const wchar_t * or cont unsigned short * |
| Unicode String Buffer | wchar_t[] or unsigned shortp[] |

If you specify one of the string buffer types, the C/C++ DLL Adapter copies the contents of the string argument and a trailing zero element into a temporary buffer before calling the function. Specify the minimum size of the temporary buffer in the
 Buffer Size
 control. If the string value is longer than the buffer size you specify, the C/C++ DLL Adapter resizes the temporary buffer so it is large enough to hold contents of the string argument and the trailing zero element. After the DLL function returns, TestStand copies the value from the temporary buffer back to the string argument.

Note

If you specify the C String or Unicode String type, the C/C++ DLL Adapter passes the address of the actual string directly to the function without copying it to a buffer. The code module must not change the contents of the string.

Note

NULL

Nothing

0

#### See Also

[Mapping Parameters](/csh?context=ts_tsref_parameters)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/string-parameters-labview-nxg-vi-call-paramet.html language=enus -->
## TOPIC 04218: String Parameters - LabVIEW NXG VI Call Parameters

- bundle_id: `teststand-api-reference`
- source_path: `tsref/string-parameters-labview-nxg-vi-call-paramet.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/string-parameters-labview-nxg-vi-call-paramet.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: String Parameters When you configure calls to VIs that use strings as parameters, you can store the string data as a binary string when reading the data from the VI or when passing the data to the VI. This option is necessary because LabVIEW NXG strings can contain binary data, including NUL charact

### String Parameters - LabVIEW NXG VI Call Parameters

#### String Parameters

When you configure calls to VIs that use strings as parameters, you can store the string data as a binary string when reading the data from the VI or when passing the data to the VI. This option is necessary because LabVIEW NXG strings can contain binary data, including NUL characters, but TestStand strings cannot contain NUL characters.

Use the ring control in the Type column of the VI Parameter Table on the
 [LabVIEW NXG Module](labview-nxg-module-tab.html)
 tab to select ASCII String or Binary String. The default value is ASCII String. TestStand does not modify the values of the ASCII strings it passes to or from VIs.

Select
 Binary String
 in the Type column of the VI Parameter Table to store a LabVIEW NXG string that contains binary data in a TestStand property. TestStand compresses the binary data, encodes the compressed data, and stores the compressed data using only printable ASCII characters. To pass a compressed string to a VI, select
 Binary String
 in the Type column. TestStand unencodes and decompresses the binary data the string stores before passing it to the VI.

Other LabVIEW NXG data types treated as strings in TestStand include Timestamps and Paths.

#### See Also

[Edit LabVIEW NXG VI Call dialog box](edit-labview-nxg-vi-call-dialog-box.html)

[LabVIEW NXG Data Types in TestStand](labview-nxg-data-types-in-teststand.html)

[LabVIEW NXG I/O Controls](i-o-controls-labview-nxg-vi-call-parameters.html)

[LabVIEW NXG Module Tab](labview-nxg-module-tab.html)

[Mapping Parameters](/csh?context=ts_tsref_parameters)

[PropertyObject.GetValBinary](../tsapiref/propertyobject-getvalbinary.html)

Parent topic:

LabVIEW NXG Data Types in TestStand

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/string-parameters-labview-vi-call-parameters.html language=enus -->
## TOPIC 04219: String Parameters - LabVIEW VI Call Parameters

- bundle_id: `teststand-api-reference`
- source_path: `tsref/string-parameters-labview-vi-call-parameters.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/string-parameters-labview-vi-call-parameters.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: String Parameters When you configure calls to VIs that use strings as parameters, you can specify to store the string data as a binary string when reading the data from the VI or when passing the data to the VI. This option is necessary because LabVIEW strings can contain binary data, including NUL

### String Parameters - LabVIEW VI Call Parameters

#### String Parameters

When you configure calls to VIs that use strings as parameters, you can specify to store the string data as a binary string when reading the data from the VI or when passing the data to the VI. This option is necessary because LabVIEW strings can contain binary data, including NUL characters, but TestStand strings cannot contain NUL characters.

Use the ring control in the Type column of the VI Parameter Table on the
 [LabVIEW Module](labview-module-tab.html)
 tab to select ASCII String or Binary String. The default value is ASCII String. TestStand does not modify the values of ASCII strings it passes to or from VIs.

Select
 Binary String
 in the Type column of the VI Parameter Table to store a LabVIEW string that contains binary data in a TestStand property. TestStand handles the string data in different ways depending on the version of LabVIEW you are using, as the following table describes.

| LabVIEW Version | TestStand Behavior |
| --- | --- |
| LabVIEW 2012 or later Development System on a non-multibyte operating system LabVIEW 2009 SP1 or later Development System on a multibyte operating system LabVIEW 2009 SP1 or later RTE on any operating system | TestStand compresses the binary data, encodes the compressed data, and stores the compressed data using only printable ASCII characters. To pass a compressed string to a VI, select Binary String in the Type column. TestStand unencodes and decompresses the binary data the string stores before passing it to the VI. |
| LabVIEW 2011 SP1 or earlier Development System on a non-multibyte operating system LabVIEW 2009 or earlier Development System on a multibyte system LabVIEW 2009 or earlier RTE on any operating system | TestStand escapes the string before storing it and substitutes hexadecimal codes for the unprintable characters, such as the NUL character, in the string. To pass an escaped string to a VI, select Binary String in the Type column. TestStand unescapes the string before passing it to the VI and substitutes the correct character values for the hexadecimal values in the escaped string. |

Other LabVIEW data types treated as strings in TestStand include Timestamps, Paths, Pictures, and all of the DAQmx references except DAQmx Task Name and DAQmx Channel Name. Use the TestStand LabVIEWIOControl data type to hold a reference to a DAQmx Task Name or DAQmx Channel Name.

Note

- To retrieve the raw data in TestStand when the binary data is compressed, call the
 PropertyObject.GetValBinary 
 method of the TestStand API on the variable that stores the binary string.
- TestStand does not automatically translate binary strings for controls like graphs. You must indicate that the parameter is a binary string.
- Do not modify the value of the SessionNumber property of the LabVIEWIOControl data type yourself. The value of the SessionNumber property refers to an internal session for the device the DeviceName property specifies. Always set the value of the SessionNumber property to
 0 
 initially, and use TestStand to populate the value of the SessionNumber property at run time if the property is an output parameter.
 In a VI that takes an I/O reference as an input, use the DeviceName property to pass the name of the device and set the SessionNumber property to
 0 
 . The output I/O parameter, which you use if you plan to use the device in another VI, populates the SessionNumber property, and you can then use the SessionNumber property in other VIs. If the value of the SessionNumber property is not
 0 
 , LabVIEW ignores the DeviceName property.

#### See Also

[Edit LabVIEW VI Call dialog box](edit-labview-vi-call-dialog-box.html)

[LabVIEW Data Types in TestStand](/csh?context=ts_tsref_labview_data_types)

[LabVIEW I/O Controls](i-o-controls-labview-vi-call-parameters.html)

[LabVIEW Module Tab](labview-module-tab.html)

[Mapping Parameters](/csh?context=ts_tsref_parameters)

[PropertyObject.GetValBinary](../tsapiref/propertyobject-getvalbinary.html)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/string-parameters-labwindows-cvi-call-paramet.html language=enus -->
## TOPIC 04220: String Parameters - LabWindows/CVI Call Parameters

- bundle_id: `teststand-api-reference`
- source_path: `tsref/string-parameters-labwindows-cvi-call-paramet.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/string-parameters-labwindows-cvi-call-paramet.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: String Parameters When using string parameters, use the C String Buffer or Unicode String Buffer type when you want the function to be able to change the contents of the argument in TestStand. Use the C String or Unicode String type when the DLL function does not modify the argument. You can pass a

### String Parameters - LabWindows/CVI Call Parameters

#### String Parameters

When using string parameters, use the C String Buffer or Unicode String Buffer type when you want the function to be able to change the contents of the argument in TestStand. Use the C String or Unicode String type when the DLL function does not modify the argument. You can pass a literal string, a TestStand string property, or an expression that evaluates to a string as the value of a string parameter.

The following settings are available in the Data Type ring control when you select
 String
 for the category type:

| String Data Type Setting | Equivalent C Data Type |
| --- | --- |
| C String | const char * |
| C String Buffer | char[] |
| Unicode String | const wchar_t * or const unsigned short * |
| Unicode String Buffer | wchar_t[] or unsigned short[] |

If you specify one of the string buffer types, the LabWindows/CVI Adapter copies the contents of the string argument and a trailing zero element into a temporary buffer before calling the function. Specify the minimum size of the temporary buffer in the Buffer Size control. If the string value is longer than the buffer size you specify, the LabWindows/CVI Adapter resizes the temporary buffer to be large enough to hold contents of the string argument and the trailing zero element. After the function returns, TestStand copies the value from the temporary buffer back to the string argument.

Note

If you specify the C String or Unicode String type, the LabWindows/CVI Adapter passes the address of the actual string directly to the function without copying it to a buffer. The code module must not change the contents of the string.

Note

NULL

Nothing

0

#### See Also

[Mapping Parameters](/csh?context=ts_tsref_parameters)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/string-value-test-edit-tabs.html language=enus -->
## TOPIC 04221: String Value Test Edit Tabs

- bundle_id: `teststand-api-reference`
- source_path: `tsref/string-value-test-edit-tabs.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/string-value-test-edit-tabs.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the String Value Test edit tabs in the TestStand Sequence Editor to specify the type of comparison and limits TestStand uses to set the step status and the string the step expects to receive. The Step Settings pane for the String Value Test step contains the following tabs: Limits –The string co

### String Value Test Edit Tabs

Use the String Value Test edit tabs in the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 to specify the type of comparison and limits TestStand uses to set the
 [step status](/csh?context=ts_tsfundamentals_step_status_values_table)
 and the string the step expects to receive.

The Step Settings pane for the String Value Test step contains the following tabs:

- Limits 
 –The string comparison the step performs.
- Data Source 
 –The data source for the string value the step compares.

Note

\r

\n

\r

\n

#### See Also

[Test Step Types](test-step-types.html)

Parent topic:

String Value Test Step

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/string-value-test-step.html language=enus -->
## TOPIC 04222: String Value Test Step

- bundle_id: `teststand-api-reference`
- source_path: `tsref/string-value-test-step.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/string-value-test-step.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: The String Value Test step calls a code module that returns a string value. After the code module executes, the String Value Test step type compares the string the step obtains to the string the step expects to receive. If the string the step obtains matches the string the step expects, the step typ

### String Value Test Step

The String Value Test step calls a
 [code module](/csh?context=ts_tsfundamentals_bldgblocks_codemodules)
 that returns a string value.

After the code module executes, the String Value Test step type compares the string the step obtains to the string the step expects to receive. If the string the step obtains matches the string the step expects, the step type sets the
 [step status](/csh?context=ts_tsfundamentals_step_status_values_table)
 to
 Passed
 . Otherwise, it sets the step status to
 Failed
 .

#### Configuring the Step

Use the
 [String Value Test edit tabs](string-value-test-edit-tabs.html)
 in the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 and the
 [Edit String Value](edit-string-value-dialog-box.html)
 dialog box in a
 [TestStand User Interface](teststand-user-interfaces.html)
 to specify the type of comparison and limits TestStand uses to set the step status and the string the step expects to receive.

A String Value Test step uses the
 Step.Result.String
 property 
to store the string value. A code module can set the value of
 Step.Result.String
 in the following ways:

- LabVIEW Adapter 
 —Specify
 Step.Result.String 
 as the Value expression for a Numeric output of a VI on the
 LabVIEW Module 
 tab.
- LabWindows/CVI 
 ,
 C/C++ DLL 
 ,
 .NET 
 ,
 ActiveX/COM 
 , or
 Sequence Adapter 
 —Pass
 Step.Result.String 
 as a reference parameter to a subsequence or code module.
- LabVIEW or LabWindows/CVI Adapter 
 —The LabVIEW and LabWindows/CVI Adapters update the value of
 Step.Result.String 
 automatically after calling legacy code modules. The LabVIEW Adapter updates the value of
 Step.Result.String 
 based on the value of the String Measurement element of the
 Test Data 
 cluster the VI returns. The LabWindows/CVI Adapter updates the value of
 Step.Result.String 
 based on the value of the stringMeasurement field of the
 tTestData 
 parameter it passes to the C function.
- All Adapters 
 —Use the
 TestStand API 
 to set the value of
 Step.Result.String 
 directly in a code module.

By default, the step type uses the value of the
 Step.Result.String
 property as the string value to compare the limits against.

#### Step Properties

In addition to the
 [common custom properties](/csh?context=ts_tsfundamentals_custom_result_props)
 , the String Value Test step type defines the following step properties:

- Step.Result.String 
 —The string value. Usually, you set this value in the code module.
- Step.Limits.String 
 ,
 StringExpr 
 , and
 UseStringExpr 
 —The expected string for the string comparison.
- Step.Comp 
 —The
 type of comparison 
 .
- Step.CompExpr 
 —The comparison operation using an expression.
- Step.UseCompExpr 
 —The step uses the expression to compare the string values.
- Step.InBuf 
 —An arbitrary string the LabVIEW and LabWindows/CVI Adapters pass to the test in the Input Buffer control or
 tTestData 
 structure of legacy code modules. 
This property maintains compatibility with previous test executives. Usually, code modules you develop for TestStand receive data as input parameters or access data as properties using the TestStand API.
- Step.DataSource 
 —A string expression the step type uses to set the value of
 Step.Result.String 
 . The default value of the expression is
 "Step.Result.String" 
 , which has the effect of using the value that the code module sets. You can customize this expression when you do not want to set the value of
 Step.Result.String 
 in the code module.

You can use a String Value Test step without a code module, which is useful when you want to test a string you have already acquired. Select
 <None>
 as the module adapter before you insert the step in the sequence and configure
 Step.DataSource
 to specify the string you have already acquired.

#### See Also

[Calling Legacy LabVIEW Code Modules](/csh?context=ts_tsref_labview_legacy)

[Calling Legacy LabWindows/CVI Code Modules](/csh?context=ts_tsref_lwcvicalllegacycodemods)

[Step Types You Can Use with Any Module Adapter](/csh?context=ts_tsfundamentals_universal_step_types)

Parent topic:

Test Step Types

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/struct-parameters-net-call-parameters.html language=enus -->
## TOPIC 04223: Struct Parameters - .NET Call Parameters

- bundle_id: `teststand-api-reference`
- source_path: `tsref/struct-parameters-net-call-parameters.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/struct-parameters-net-call-parameters.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Struct Parameters You can pass struct parameters using the .NET Adapter in any of the following ways: You can store and pass struct parameters using TestStand object reference variables. Use this approach to store the actual .NET struct in the object reference, which can improve speed and efficiency

### Struct Parameters - .NET Call Parameters

#### Struct Parameters

You can pass struct parameters using the .NET Adapter in any of the following ways:

- You can store and pass struct parameters using TestStand object reference variables. 
 Use this approach to store the actual .NET struct in the object reference, which can improve speed and efficiency because TestStand does not need to convert the struct to a TestStand variable type. However, you cannot directly access the data from TestStand without using additional .NET calls.
- You can create a TestStand custom data type that matches the structure of the .NET struct. Click the
 Create Type from Struct 
 button on the
 .NET Module 
 tab of the
 Step Settings 
 pane in the
 TestStand Sequence Editor 
 or on the
 Module 
 tab of the
 Edit .NET Call 
 dialog box in a
 TestStand User Interface 
 to launch the
 Create Custom Data Type from Struct 
 dialog box to create the custom data type. You can then create TestStand variables of the custom data type and pass the variables as arguments for parameters of the .NET struct type.
 Use this approach to see and use all the fields of the struct directly in TestStand as native TestStand variables. However, this approach has greater overhead than using object reference variables because the .NET Adapter must copy the fields between the .NET struct and the TestStand custom data type variable.
- You can specify individual TestStand variables to store and pass each field of a .NET struct. Expand the struct parameter in the Parameters Table on the .NET Module tab of the Step Settings pane in the sequence editor or on the Module tab of the Edit .NET Call dialog box in a user interface to specify individual fields.
 Use this approach to store one or more fields directly in TestStand variables and use them from TestStand without having to create a TestStand custom data type and to use each field separately. However, this approach is less efficient than using object reference variables or custom data types.

#### See Also

[Create Custom Data Type from Struct dialog box](create-custom-data-type-from-struct-dialog-bo.html)

[Edit .NET Call dialog box](edit-net-call-dialog-box.html)

[Mapping Parameters](/csh?context=ts_tsref_parameters)

[.NET Struct Passing](net-struct-passing-tab-type-properties-dialog.html)
 tab on the
 [Type Properties dialog box](type-properties-dialog-box.html)

[Passing a Struct to a .NET Assembly (Example)](/csh?context=ts_8206)

[Step Settings Pane](step-settings-pane.html)

[Type Properties dialog box](type-properties-dialog-box.html)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/structure-parameters-c-c-dll-call-parameters.html language=enus -->
## TOPIC 04224: Structure Parameters - C/C++ DLL Call Parameters

- bundle_id: `teststand-api-reference`
- source_path: `tsref/structure-parameters-c-c-dll-call-parameters.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/structure-parameters-c-c-dll-call-parameters.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Structure Parameters You can pass variables and properties you create with named data types to function parameters that accept structures. When you create or edit a data type, you specify whether the type can be a structure argument and how the type represents itself in memory when you pass it to a

### Structure Parameters - C/C++ DLL Call Parameters

#### Structure Parameters

You can pass variables and properties you create with named data types to function parameters that accept structures. When you create or edit a data type, you specify whether the type can be a structure argument and how the type represents itself in memory when you pass it to a
 [structure
 parameter](c-struct-passing-tab-type-properties-dialog-b.html)
 .

If you build a LabWindows/CVI module DLL with the
 Add NI Type Information resource to DLL
 option enabled, you can use the
 Create/Update Custom Data Type
 button on the LabWindows/CVI Module Tab to access the Create/Update Custom Data Type from Struct Dialog to create the TestStand container type.

Note

- You can pass
 NULL 
 to a structure pointer parameter by passing an empty object reference or the constant
 Nothing 
 . Do not pass the constant
 0 
 .
- The C/C++ DLL Adapter cannot call functions that specify structure parameters that contain pointers to memory which the function allocates or deallocates.

#### Type, and Pass by Value or by Reference

When you select the C Struct category for a parameter, the C/C++ DLL Adapter displays the Type and Pass controls. The Type control specifies the TestStand named data type the adapter uses to determine how to pack the structure elements in memory. The Pass control specifies whether TestStand passes the value of the argument you specify in the Value Expression control or passes a pointer to the argument. If you select
 By Pointer (*)
 or
 By Reference (&)
 , the adapter passes a pointer to the argument value. If you choose to pass a pointer, the argument you specify in the Value Expression control must be the name of a variable or property.

#### See Also

[Mapping Parameters](/csh?context=ts_tsref_parameters)

[Passing a Struct to a C DLL (Example)](/csh?context=ts_8147)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/structure-parameters-labwindows-cvi-call-para.html language=enus -->
## TOPIC 04225: Structure Parameters - LabWindows/CVI Call Parameters

- bundle_id: `teststand-api-reference`
- source_path: `tsref/structure-parameters-labwindows-cvi-call-para.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/structure-parameters-labwindows-cvi-call-para.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Structure Parameters You can pass variables and properties you create with named data types to function parameters that accept structures. When you create or edit a data type, you specify whether the type can be a C structure argument and how the type represents itself in memory when you pass it to

### Structure Parameters - LabWindows/CVI Call Parameters

#### Structure Parameters

You can pass variables and properties you create with named data types to function parameters that accept structures. When you create or edit a data type, you specify whether the type can be a C structure argument and how the type represents itself in memory when you pass it to a
 [structure parameter](c-struct-passing-tab-type-properties-dialog-b.html)
 . When you specify the data to pass for the struct parameter on the
 [Module](module-tab-step-settings-pane.html)
 tab of the
 [Step Settings](step-settings-pane.html)
 pane, you only need to specify an expression that evaluates to data with the data type.

Note

- You can pass
 NULL 
 to a structure pointer parameter by passing an empty object reference or the constant
 Nothing 
 . Do not pass the constant
 0 
 .
- The LabWindows/CVI Adapter cannot call functions which specify structure parameters that contain pointers to memory that the function allocates or deallocates.

#### Type, and Pass by Value or by Reference

When you select the C Struct category for a parameter, the LabWindows/CVI Adapter displays the Type and Pass controls. The Type control specifies the TestStand named data type the adapter uses to determine how to pack the structure elements in memory. The Pass control specifies whether TestStand passes the value of the argument you specify in the Value Expression control or passes a pointer to the argument. If you select
 By Reference (by pointer)
 , the adapter passes a pointer to the argument value. When you pass a C struct by reference, a member of the C struct uses the CAObjHandle data type, and the function alters the value of the struct member, do not use the function to discard the original handle. TestStand discards the original handle after the call completes.

If you choose to pass a pointer, the argument you specify in the Value Expression control must be the name of a variable or property.

#### See Also

[Mapping Parameters](/csh?context=ts_tsref_parameters)

[Passing a Struct to a C DLL (Example)](/csh?context=ts_8147)

[Type Properties dialog box](type-properties-dialog-box.html)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/substeps-tab-step-type-properties-dialog-box.html language=enus -->
## TOPIC 04226: Substeps tab - Step Type Properties Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/substeps-tab-step-type-properties-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/substeps-tab-step-type-properties-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Substeps tab Use the Substeps tab to specify Pre-Step, Post-Step, Edit, and Custom substeps for the step type. Substeps use substep code modules to define standard actions, other than calling the step code module , TestStand performs for all instances of the step type. The Substeps tab contains the

### Substeps tab - Step Type Properties Dialog Box

#### Substeps tab

Use the Substeps tab to specify Pre-Step, Post-Step, Edit, and Custom substeps for the step type. Substeps use substep code modules to define standard actions, other than calling the step
 [code module](/csh?context=ts_tsfundamentals_bldgblocks_codemodules)
 , TestStand performs for all instances of the step type.

The Substeps tab contains the following options:

- Adapter 
 —The adapter for the next substep you insert into the substep list.
- <
 Substep List
 > 
 —The substeps for the step type. Substeps of the same category always appear continuously in the list. Use the
 Move Up 
 and
 Move Down 
 buttons to reorder substeps within a category. The order of the substeps in the list defines the order in which Pre- and Post-Step Substeps execute and the order in which the menu items for Edit substeps appear in the context menu of individual sequence views in the Sequence File window.
- Add 
 —Displays a menu from which you select the category of substep to insert into the substep list. You can select from the following categories of substeps: Pre-Step Substep, Post-Step Substep, Edit Substep, and Custom Substep.
 Note 
 With the exception of substeps named OnNewStep, TestStand does not call custom substeps. Use the
 [TestStand API](/csh?context=ts_tsapiref_teststand_activex_api_overview)
 to invoke a custom substep from a code module or user interface. You can create a custom substep named OnNewStep for TestStand to call each time you create a new step of that type. For example, the built-in
 [If](if-step.html)
 step type uses an OnNewStep substep to insert a matching
 [End](end-step.html)
 step.
- Delete 
 —Deletes the selected substep from the substep list.
- Specify Module 
 —Launches the Specify Module dialog box for the selected substep in the substep list.
- Rename 
 —Changes the name of the selected substep.
- Move Up 
 —Moves the selected substep up within the group of substeps of the same category in the substep list.
- Move Down 
 —Moves the selected substep down within the group of substeps of the same category in the substep list.
- Substep Info 
 —The controls in this section are only visible when you select an Edit substep from the substep list.
  - Menu Item Name Expression 
 —The name of the menu item that invokes the Edit substep in the context menu of individual sequence views in the Sequence File window.
 Note 
 If you specify a literal string in this control, you must enclose it in double quotation marks. If you want to use a name from a
 [string resource file](/csh?context=ts_tsfundamentals_resource_strings_format)
 , you can use the
 ResStr
 expression function to retrieve the name from the file.
  - Supports Edit as Read-Only 
 —When you enable this option, the Edit substep code module checks the TestStand API
 Step.EditAsReadOnly 
 property. If the
 Step.EditAsReadOnly 
 property is
 True 
 , the dialog box opens in read-only mode. If you do not want to open the dialog box in read-only mode, leave this option disabled so the
 TestStand Sequence Editor 
 does not call the Edit substep for read-only steps.

#### See Also

[End Step](end-step.html)

[Module Tabs and Specify Module Dialog Boxes](specify-module-tabs-and-dialog-boxes.html)

[Step.EditAsReadOnly](../tsapiref/step-editasreadonly.html)

Parent topic:

Step Type Properties Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/summary-table.html language=enus -->
## TOPIC 04227: Summary Table

- bundle_id: `teststand-api-reference`
- source_path: `tsref/summary-table.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/summary-table.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Summary Table The Summary table contains the following information: Items —The number of unique code modules, steps, UUTS, batches, lots, and synchronization objects the profiler has identified from the events it displays. Executions —The number of TestStand executions that contain threads that have

### Summary Table

#### Summary Table

The Summary table contains the following information:

- Items 
 —The number of unique code modules, steps, UUTS, batches, lots, and synchronization objects the profiler has identified from the events it displays.
- Executions 
 —The number of TestStand executions that contain threads that have generated the events the profiler displays.
- Threads 
 —The number of TestStand threads that have generated the events the profiler displays.
- Operations 
 —The total number of operations the profiler has identified from the events it displays.
- Incomplete Operations 
 —The number of operations in progress.
- Time Span of Selected Operations 
 —The time interval from the beginning of the first selected operation to the end of the last selected operation. If you enabled the Blocked Threads option in the
 View 
 menu of the Execution Profiler window, the time span includes the time during which the selected operations are in the Blocked state. Otherwise, the time span includes only the time during which the selected operations are in the In Use state.
- Visible Events 
 —The number of events the profiler displays.
- Hidden Events 
 —The number of events the profiler records but does not display based on the current settings.
- First Event Time 
 —The time and date of the first recorded event.
- Last Event Time 
 —The time and date of the last recorded event.
- Total Time Span 
 —The time interval between the first and last recorded events. The profiler uses this value to calculate other values as a percentage of the total time.
- Lock Events 
 —The number of events the profiler has recorded from Lock operations.
- Auto Schedule Use Resource Events 
 —The number of events the profiler has recorded from Use Auto Scheduled Resource operations.
- Batch Synchronized Section Events 
 —The number of events the profiler has recorded from Batch Synchronization operations.
- Notification Events 
 —The number of events the profiler has recorded from Notification operations.
- Queue Events 
 —The number of events the profiler has recorded from Queue operations.
- Rendezvous Events 
 —The number of events the profiler has recorded from Rendezvous operations.
- Semaphore Events 
 —The number of events the profiler has recorded from Semaphore operations.
- Wait Events 
 —The number of events the profiler has recorded from Wait operations.
- Step Type Module Events 
 —The number of events the profiler has recorded for step type substep modules.
- Step Module Events 
 —The number of events the profiler has recorded for step code module operations.
- UUT Events 
 —The number of events the profiler has recorded for UUTs.
- Batch Events 
 —The number of events the profiler has recorded for Batches.
- Lot Events 
 —The number of events the profiler has recorded for Lots.
- Process Model Events 
 —The number of events the profiler has recorded from any operations performed in process models.
- Events hidden due to insufficient duration of operations 
 —The number of events the profiler records but does not display because the completed operations they belong to are shorter than the specified minimum duration to display.

#### See Also

[Profiler Window Tables](profiler-window-tables.html)

[Synchronization Step Types](synchronization-step-types.html)

[View Menu](view-menu-execution-profiler.html)

Parent topic:

Profiler Window Tables

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/sweep-loop-edit-tabs.html language=enus -->
## TOPIC 04228: Sweep Loop Edit Tabs

- bundle_id: `teststand-api-reference`
- source_path: `tsref/sweep-loop-edit-tabs.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/sweep-loop-edit-tabs.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Sweep Parameters tab , Input tab , Output tab , and Loop Information tab in the TestStand Sequence Editor to define a set of sweep parameters and a block of steps to sweep over. See Also Data Streams Step Types

### Sweep Loop Edit Tabs

Use the
 [Sweep Parameters tab](sweep-parameters-tab.html)
 ,
 [Input tab](input-tab.html)
 ,
 [Output tab](output-tab.html)
 , and
 [Loop Information tab](loop-information-tab2.html)
 in the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 to define a set of sweep parameters and a block of steps to sweep over.

#### See Also

[Data Streams Step Types](/csh?context=ts_tsref_data_streams_types)

Parent topic:

Sweep Loop Step

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/sweep-loop-step-sessions.html language=enus -->
## TOPIC 04229: Sweep Loop Step - Sessions

- bundle_id: `teststand-api-reference`
- source_path: `tsref/sweep-loop-step-sessions.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/sweep-loop-step-sessions.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use a Sweep Loop step type to sweep on the instrument attributes specified by an IO session. In the Sweep Loop step, you can configure a sweep parameter to sweep on an IO session rather than a TestStand variable. When configured to sweep on a IO Session, Sweep Loop allows you to configure the instru

### Sweep Loop Step - Sessions

Use a Sweep Loop step type to sweep on the instrument attributes specified by an IO session.

In the Sweep Loop step, you can configure a sweep parameter to sweep on an IO session rather than a TestStand variable. When configured to sweep on a IO Session, Sweep Loop allows you to configure the instrument attribute, channel, and a variable that stores the sweep parameter value. These settings are in addition to the standard settings of a sweep parameter such as Strategy and its related settings. When Sweep Loop executes, it automatically sets the instrument attribute on the IO session configured for each parameter. Users can use the variable setting to store the sweep parameter value for use in other steps. You can configure multiple sweep parameters to sweep on IO sessions.

#### Step Properties

In addition to the
 [common custom properties](/csh?context=ts_tsfundamentals_custom_result_props)
 , the Sweep Session step type defines the following step properties:

- Step.Parameters.SessionSettings—The session information is stored in this container.

#### See Also

[Data Streams Step Types](/csh?context=ts_tsref_data_streams_types)

Parent topic:

Sweep Loop Step

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/sweep-loop-step.html language=enus -->
## TOPIC 04230: Sweep Loop Step

- bundle_id: `teststand-api-reference`
- source_path: `tsref/sweep-loop-step.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/sweep-loop-step.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Sweep Loop step to define a set of sweep parameters and a block of steps to loop over. Configuring the Step Use the Sweep Loop edit tabs in the TestStand Sequence Editor to configure the Sweep Loop step. You can also use the Configure Sweep Loop dialog box in a TestStand User Interface to co

### Sweep Loop Step

Use the Sweep Loop step to define a set of sweep parameters and a block of steps to loop over.

#### Configuring the Step

Use the
 [Sweep Loop](sweep-loop-edit-tabs.html)
 edit tabs in the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 to configure the Sweep Loop step. You can also use the
 [Configure Sweep Loop](configure-sweep-loop-dialog-box.html)
 dialog box in a
 [TestStand User Interface](teststand-user-interfaces.html)
 to configure the Sweep Loop step.

#### See Also

[Data Streams Step Types](/csh?context=ts_tsref_data_streams_types)

Parent topic:

Flow Control Step Types

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/sweep-parameter-strategies.html language=enus -->
## TOPIC 04231: Sweep Parameter Strategies

- bundle_id: `teststand-api-reference`
- source_path: `tsref/sweep-parameter-strategies.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/sweep-parameter-strategies.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Sweep Parameters tab in the Step Settings panel of the Sweep Loop step to select a sweep parameter strategy. The Sweep Loop step supports the following sweep strategies: Start, Stop, Step Start, Stop, Count Array Constant Capture Value Stream Start, Stop, Step and Start, Stop, Count strategi

### Sweep Parameter Strategies

Use the
 [Sweep Parameters](sweep-parameters-tab.html)
 tab in the Step Settings panel of the Sweep Loop step to select a sweep parameter strategy.

The
 [Sweep Loop](sweep-loop-step.html)
 step supports the following sweep strategies:

- Start, Stop, Step
- Start, Stop, Count
- Array
- Constant
- Capture Value
- Stream

Note

Parent topic:

Sweep Loop Step

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/sweep-parameters-tab-configure-sweep-loop-dia.html language=enus -->
## TOPIC 04232: Sweep Parameters Tab - Configure Sweep Loop Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/sweep-parameters-tab-configure-sweep-loop-dia.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/sweep-parameters-tab-configure-sweep-loop-dia.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sweep Parameters Tab Use the Sweep Parameters tab to configure sweep parameters and strategies. Number of Test Vectors —(Read-only) Indicates the number of iterations the sweep loop will execute if it runs to completion. Errors and Warnings —Visible only when errors or warnings are present. Indicate

### Sweep Parameters Tab - Configure Sweep Loop Dialog Box

#### Sweep Parameters Tab

Use the Sweep Parameters tab to configure sweep parameters and strategies.

- Number of Test Vectors 
 —(Read-only) Indicates the number of iterations the sweep loop will execute if it runs to completion.
- Errors and Warnings 
 —Visible only when errors or warnings are present. Indicates the number of errors and warnings in the sweep step is shown in the top left corner of this tab. Click on the number to see a list of all errors and warnings, and click on an individual item to highlight the source of the error.

#### Sweep Parameters Table

This table displays the sweep parameters. It contains the following columns:

- Enable or Disable 
 —Enable or disable a parameter.
 Note 
 You can also enable or disable a parameter by navigating to
 Properties>>Expressions
 . Set a pre-expression and set the Parameter to true/false. The expression will run at the start of each loop. This option will enable or disable the parameter at run time, but the edit time view in step settings will not change.
- Parameter Name 
 —Specify a symbolic name for the parameter.
- Nesting Level 
 —View the integer value that indicates the nesting level of the parameter. The default and highest nesting level is 0. This value increases as the nesting level increases. For more information, see the Configuring Parameter Nested Levels section below.
- Type 
 —Select the data type of the parameter. The values that this parameter iterates over must be this type.
 
 Note 
 When TestStand loads Sweep Loop steps from older versions of TestStand, it evaluates the expressions in the Sweep Strategy and Parameter Value and updates the parameter's Type accordingly. If the Specification property was set to "Expression" in the old step, TestStand updates the parameter's Type based on the values specified in the Strategy options, such as Start, Array, or Constant.
  - I/O Session 
 —Sweep on the instrument attributes specified by an I/O Session.
  - All other types 
 —The sweep parameter values of this type are stored in the variable of the same type specified in the Parameter Value/Session column.
    - Number
    - String
    - Boolean
    - Enumeration
- Write to Output Stream 
 —Check to write this sweep parameter to the output stream specified on the
 Output 
 tab at the end of each iteration.
 Note 
 This checkbox has no effect if output is disabled.
- Parameter Value/Session 
 —Specify the location to store the sweep parameter value. Select options based on the configuration of the Type column. You can choose a variable of the selected parameter type by launching the
 Select Variable or Session 
 dialog from the button in Parameter Value/Session.
  - If you configure the sweep parameter as an
 I/O Session 
 , specify the TestStand variable that stores the I/O session. Available I/O sessions will be listed in the dropdown menu.
  - If you select any other data type, specify a variable of that type to store the parameter value for each iteration of the loop.
- [Count],{Range} 
 —(Read-only) Displays summary information about this sweep parameter.

You can edit the table by clicking the following buttons.

- Add Parameter 
 —Adds a new sweep parameter to the table. The new parameter has the same settings as the selected parameter.
- Add Parameter from CSV File 
 —Imports new sweep parameters to the table from a CSV file. All imported parameters will be added below the selected parameter. Click the dropdown menu beside the Add Parameter icon to access this option.
 Note 
 If Stream parameters already exist in the Step or parameters are nested, this option only allows you to add parameters from the CSV file as an array.
- Remove Parameter 
 —Removes a sweep parameter from the table.
- Move Parameter Up 
 —Moves the selected sweep parameter(s) up one row in the table. You can also move a parameter by dragging it to a new position in the list.
- Move Parameter Down 
 —Moves the selected sweep parameter(s) down one row in the table. You can also move a parameter by dragging it to a new position in the list.
- Indent Parameter Right 
 —Changes the nested level of the selected sweep parameter. See the Configuring Parameter Nested Levels section below.
- Indent Parameter Left 
 —Changes the nested level of the selected sweep parameter. See the Configuring Parameter Nested Levels section below.
- Open Table View 
 —Displays the Test Vector Table or the Value Summary Table.

#### Automatic Variable Creation

When you specify a parameter name, TestStand automatically creates a variable of the data type that matches the parameter data type. TestStand updates the Parameter Value/Session field to reference this variable. If the parameter is renamed or its type changed, the name or type of the automatically created variable is updated. The type of a variable will not be updated if there are any references to it. The name of a variable will not be updated if there are any unconfirmed references to it.

Note

TestStand creates the variable under one of the following: Locals, Parameters, FileGlobals, or StationGlobals. You can specify where TestStand should create variables by changing the option in
 Station Options>>Preferences>>Context of Automatically Created Variables
 .

Note

TestStand does not automatically delete variables that were automatically created in StationGlobals.

An automatically created variable will be deleted under the following conditions:

- The parameter Type changes to Session
- The value changes to reference a different variable
- The parameter is deleted and there are no other references to the variable in the sequence file

Note

#### Configuring Parameter Nested Levels

Change the nested level of a sweep parameter by moving the parameter to the left or right in the Sweep Parameters Table. Change the level of a parameter to run a parallel or nested sweep.

Note

- Parallel sweep 
 — Run more than one parameter synchronously by assigning the parameters the same nested level. Parameters at the same level will iterate on the same step, and must contain the same number of values.
- Nested sweep 
 — Create nested sweep loops by moving the selected parameter to the right underneath the parameter within which you want to create a nested sweep loop.
 Note 
 You can create nested sweep loops at multiple levels. However, sweep parameter levels must occur in increasing order.

#### Sweep Parameter Strategy Table

This table displays the strategy settings for the selected sweep parameter. It can contain the following rows:

- Strategy 
 —Specifies the
 sweep parameter strategy 
 for this parameter. The Strategy row is always present.
- Mode 
 —Specifies whether the values for a Strategy are specified using expressions or constants. If the mode is Static, the Strategy should be specified using constants. If the mode is Dynamic, TestStand expressions, which will be evaluated at run time, can be used to specify the Strategy.
 Note 
 In the case of Dynamic parameters, all values displayed in the panel and the Test Vector Table at edit time can change at run time.
- Start 
 —Specifies the start value for a
 Start, Stop, Step 
 or
 Start, Stop, Count 
 strategy.
- Stop 
 —Specifies the stop value for a Start, Stop, Step or Start, Stop, Count strategy.
- Step 
 —Specifies the step value for a Start, Stop, Step strategy. This field is not configurable for the Start, Stop, Count strategy.
- Count 
 —Specifies the number of points for a Start, Stop, Count strategy or the number of array elements for the Array (1D List) strategy. This field is not configurable for the Start, Stop, Step strategy.
- Distribution 
 —Specifies if a Start, Stop, Step strategy is linear or geometric progression, or if a Start, Stop, Count strategy is linear, geometric progression, decade, or octave.
- Numeric Format 
 —Specifies the numeric format of all numeric parameters for all strategies.
- Array 
 —Specifies the array for an
 Array (1D List) 
 strategy when the Mode is set to Dynamic.
- Constant 
 —Specifies the value for a
 Constant 
 strategy.
- Field/Column ID 
 —Specifies the field or column of the
 InputRecordStream 
 specified on the Input tab when using a
 Stream 
 strategy.
- Values 
 —Lists the values for the parameter, as specified by the strategy. The values shown are read-only for all Strategies except the Array Strategy in Static mode. If you disable any item in the Values list, that item will be discarded when generating the strategy values and the final test vectors.
- Edit as Static Array 
 —Allows you to change the current Strategy to Array and the mode to Static, while retaining the populated values. The values can then be edited like a regular static Array parameter.

This table displays the following additional rows for I/O Sessions:

- Attribute 
 —Specifies the instrument attribute in the session you want to sweep on.
- Channel 
 —Specifies the channel on the instrument you want to sweep on. This setting is available only if the instrument supports multiple channels.
- Variable 
 —Specifies the TestStand variable used to store the sweep values in an iteration.

#### Values Table

Use this table to view and manipulate the values for the selected sweep parameter. Disable specific values for static arrays. The disabled values will not be used as a part of test vector generation and will not appear in the Value Summary table. The Values table is read-only for all strategies except Array.

Note

#### Behavior of Dynamic Parameters

Dynamic parameter values use TestStand expressions, which are evaluated at run time. Unlike Static parameter values, the values generated by Dynamic parameters can only be estimated at edit time. This results in the following behavior and functionality:

- In Start, Stop, Step and Start, Stop, Count Strategies, expressions are captured at loop start and not sampled again.
- Values in the Test Vector Table cannot be enabled or disabled.
- Values in the Value Table cannot be manually changed.
- If you rename or change the type of a Dynamic parameter in the Step Settings, the Test Vector Table will be marked as out of sync. Refresh the table to reflect your changes.

#### See Also

[Sweep Loop Step](sweep-loop-step.html)

[Sweep Loop Input Tab](input-tab-configure-sweep-loop-dialog-box.html)

[Sweep Loop Output Tab](output-tab-configure-sweep-loop-dialog-box.html)

Parent topic:

Configure Sweep Loop Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/sweep-parameters-tab.html language=enus -->
## TOPIC 04233: Sweep Parameters Tab

- bundle_id: `teststand-api-reference`
- source_path: `tsref/sweep-parameters-tab.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/sweep-parameters-tab.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Sweep Parameters tab to configure sweep parameters and strategies. Number of Test Vectors —(Read-only) Indicates the number of iterations the sweep loop will execute if it runs to completion. Errors and Warnings —Visible only when errors or warnings are present. Indicates the number of error

### Sweep Parameters Tab

Use the Sweep Parameters tab to configure sweep parameters and strategies.

- Number of Test Vectors 
 —(Read-only) Indicates the number of iterations the sweep loop will execute if it runs to completion.
- Errors and Warnings 
 —Visible only when errors or warnings are present. Indicates the number of errors and warnings in the sweep step is shown in the top right corner of this tab. Click on the number to see a list of all errors and warnings, and click on an individual item to highlight the source of the error.

#### Sweep Parameters Table

This table displays the sweep parameters. It contains the following columns:

- Enable or Disable 
 —Enable or disable a parameter.
 Note 
 You can also enable or disable a parameter by navigating to
 Properties>>Expressions
 . Set a pre-expression and set the Parameter to true/false. The expression will run at the start of each loop. This option will enable or disable the parameter at run time, but the edit time view in step settings will not change.
- Parameter Name 
 —Specify a symbolic name for the parameter.
- Nesting Level 
 —View the integer value that indicates the nesting level of the parameter. The default and highest nesting level is 0. This value increases as the nesting level increases. For more information, see the Configuring Parameter Nested Levels section below.
- Type 
 —Select the data type of the parameter. The values that this parameter iterates over must be this type.
 
 Note 
 When TestStand loads Sweep Loop steps from older versions of TestStand, it evaluates the expressions in the Sweep Strategy and Parameter Value and updates the parameter's Type accordingly. If the Specification property was set to "Expression" in the old step, TestStand updates the parameter's Type based on the values specified in the Strategy options, such as Start, Array, or Constant.
  - I/O Session 
 —Sweep on the instrument attributes specified by an I/O Session.
  - All other types 
 —The sweep parameter values of this type are stored in the variable of the same type specified in the Parameter Value/Session column.
    - Number
    - String
    - Boolean
    - Enumeration
- Write to Output Stream 
 —Check to write this sweep parameter to the output stream specified on the
 Output 
 tab at the end of each iteration.
 Note 
 This checkbox has no effect if output is disabled.
- Parameter Value/Session 
 —Specify the location to store the sweep parameter value. Select options based on the configuration of the Type column. You can choose a variable of the selected parameter type by launching the
 Select Variable or Session 
 dialog from the button in Parameter Value/Session.
  - If you configure the sweep parameter as an
 I/O Session 
 , specify the TestStand variable that stores the I/O session. Available I/O sessions will be listed in the dropdown menu.
  - If you select any other data type, specify a variable of that type to store the parameter value for each iteration of the loop.
- [Count],{Range} 
 —(Read-only) Displays summary information about this sweep parameter.

You can edit the table by clicking the following buttons.

- Add Parameter 
 —Adds a new sweep parameter to the table. The new parameter has the same settings as the selected parameter.
- Add Parameter from CSV File 
 —Imports new sweep parameters to the table from a CSV file. All imported parameters will be added below the selected parameter. Click the dropdown menu beside the Add Parameter icon to access this option.
 Note 
 If Stream parameters already exist in the Step or parameters are nested, this option only allows you to add parameters from the CSV file as an array.
- Remove Parameter 
 —Removes a sweep parameter from the table.
- Move Parameter Up 
 —Moves the selected sweep parameter(s) up one row in the table. You can also move a parameter by dragging it to a new position in the list.
- Move Parameter Down 
 —Moves the selected sweep parameter(s) down one row in the table. You can also move a parameter by dragging it to a new position in the list.
- Indent Parameter Right 
 —Changes the nested level of the selected sweep parameter. See the Configuring Parameter Nested Levels section below.
- Indent Parameter Left 
 —Changes the nested level of the selected sweep parameter. See the Configuring Parameter Nested Levels section below.
- Open Table View 
 —Displays the Test Vector Table or the Value Summary Table.

#### Automatic Variable Creation

When you specify a parameter name, TestStand automatically creates a variable of the data type that matches the parameter data type. TestStand updates the Parameter Value/Session field to reference this variable. If the parameter is renamed or its type changed, the name or type of the automatically created variable is updated. The type of a variable will not be updated if there are any references to it. The name of a variable will not be updated if there are any unconfirmed references to it.

Note

TestStand creates the variable under one of the following: Locals, Parameters, FileGlobals, or StationGlobals. You can specify where TestStand should create variables by changing the option in
 Station Options>>Preferences>>Context of Automatically Created Variables
 .

Note

TestStand does not automatically delete variables that were automatically created in StationGlobals.

An automatically created variable will be deleted under the following conditions:

- The parameter Type changes to Session
- The value changes to reference a different variable
- The parameter is deleted and there are no other references to the variable in the sequence file

Note

#### Configuring Parameter Nested Levels

Change the nested level of a sweep parameter by moving the parameter to the left or right in the Sweep Parameters Table. Change the level of a parameter to run a parallel or nested sweep.

Note

- Parallel sweep 
 — Run more than one parameter synchronously by assigning the parameters the same nested level. Parameters at the same level will iterate on the same step, and must contain the same number of values.
- Nested sweep 
 — Create nested sweep loops by moving the selected parameter to the right underneath the parameter within which you want to create a nested sweep loop.
 Note 
 You can create nested sweep loops at multiple levels. However, sweep parameter levels must occur in increasing order.

#### Sweep Parameter Strategy Table

This table displays the strategy settings for the selected sweep parameter. It can contain the following rows:

- Strategy 
 —Specifies the
 sweep parameter strategy 
 for this parameter. The Strategy row is always present.
- Mode 
 —Specifies whether the values for a Strategy are specified using expressions or constants. If the mode is Static, the Strategy should be specified using constants. If the mode is Dynamic, TestStand expressions, which will be evaluated at run time, can be used to specify the Strategy.
 Note 
 In the case of Dynamic parameters, all values displayed in the panel and the Test Vector Table at edit time can change at run time.
- Start 
 —Specifies the start value for a
 Start, Stop, Step 
 or
 Start, Stop, Count 
 strategy.
- Stop 
 —Specifies the stop value for a Start, Stop, Step or Start, Stop, Count strategy.
- Step 
 —Specifies the step value for a Start, Stop, Step strategy. This field is not configurable for the Start, Stop, Count strategy.
- Count 
 —Specifies the number of points for a Start, Stop, Count strategy or the number of array elements for the Array (1D List) strategy. This field is not configurable for the Start, Stop, Step strategy.
- Distribution 
 —Specifies if a Start, Stop, Step strategy is linear or geometric progression, or if a Start, Stop, Count strategy is linear, geometric progression, decade, or octave.
- Numeric Format 
 —Specifies the numeric format of all numeric parameters for all strategies.
- Array 
 —Specifies the array for an
 Array (1D List) 
 strategy when the Mode is set to Dynamic.
- Constant 
 —Specifies the value for a
 Constant 
 strategy.
- Field/Column ID 
 —Specifies the field or column of the
 InputRecordStream 
 specified on the Input tab when using a
 Stream 
 strategy.
- Values 
 —Lists the values for the parameter, as specified by the strategy. The values shown are read-only for all Strategies except the Array Strategy in Static mode. If you disable any item in the Values list, that item will be discarded when generating the strategy values and the final test vectors.
- Edit as Static Array 
 —Allows you to change the current Strategy to Array and the mode to Static, while retaining the populated values. The values can then be edited like a regular static Array parameter.

This table displays the following additional rows for I/O Sessions:

- Attribute 
 —Specifies the instrument attribute in the session you want to sweep on.
- Channel 
 —Specifies the channel on the instrument you want to sweep on. This setting is available only if the instrument supports multiple channels.
- Variable 
 —Specifies the TestStand variable used to store the sweep values in an iteration.

#### Values Table

Use this table to view and manipulate the values for the selected sweep parameter. Disable specific values for static arrays. The disabled values will not be used as a part of test vector generation and will not appear in the Value Summary table. The Values table is read-only for all strategies except Array.

Note

#### Behavior of Dynamic Parameters

Dynamic parameter values use TestStand expressions, which are evaluated at run time. Unlike Static parameter values, the values generated by Dynamic parameters can only be estimated at edit time. This results in the following behavior and functionality:

- In Start, Stop, Step and Start, Stop, Count Strategies, expressions are captured at loop start and not sampled again.
- Values in the Test Vector Table cannot be enabled or disabled.
- Values in the Value Table cannot be manually changed.
- If you rename or change the type of a Dynamic parameter in the Step Settings, the Test Vector Table will be marked as out of sync. Refresh the table to reflect your changes.

#### See Also

[Sweep Loop Step](sweep-loop-step.html)

[Sweep Loop Input Tab](input-tab.html)

[Sweep Loop Output Tab](output-tab.html)

Parent topic:

Sweep Loop Edit Tabs

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/switch-executive-mode-edit-ivi-switch-step-di.html language=enus -->
## TOPIC 04234: Switch Executive Mode - Edit IVI Switch Step Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/switch-executive-mode-edit-ivi-switch-step-di.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/switch-executive-mode-edit-ivi-switch-step-di.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Switch Executive Mode The IVI Switch step type supports the following Switch Executive operations: Connect/Disconnect —Connects or disconnects switch routes for a virtual device. Wait —Blocks until all switches debounce for a virtual device. Get Information —Retrieves low-level status and informatio

### Switch Executive Mode - Edit IVI Switch Step Dialog Box

#### Switch Executive Mode

The IVI Switch step type supports the following Switch Executive operations:

- Connect/Disconnect 
 —Connects or disconnects switch routes for a virtual device.
- Wait 
 —Blocks until all switches debounce for a virtual device.
- Get Information 
 —Retrieves low-level status and information from a virtual device.

Parent topic:

Edit IVI Switch Step Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/switch-step.html language=enus -->
## TOPIC 04235: Switch Step

- bundle_id: `teststand-api-reference`
- source_path: `tsref/switch-step.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/switch-step.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use an IVI Switch step to connect and disconnect paths and routes , to determine the connectivity of two switches or the state of a route, and to query the state of the switch module or virtual device. A switch is an instrument that can establish a connection between two I/O channels. The IVI Switch

### Switch Step

Use an IVI Switch step to connect and disconnect paths and
 [routes](/csh?context=ts_tsref_route_spec_string)
 , to determine the connectivity of two switches or the state of a route, and to query the state of the switch module or virtual device. A switch is an instrument that can establish a connection between two I/O channels.

The IVI Switch step type provides a high-level programming layer for instruments compliant with the IVI Switch class and NI Switch Executive virtual devices. The IVI Switch step type also supports IVI-compliant instruments that can perform trigger scanning and trigger-synchronized path connection and disconnection.

NI Switch Executive is an intelligent switch management and routing application you can use with TestStand to interactively configure switch devices from multiple vendors as a single virtual device. You can specify intuitive names for each channel within the virtual switch device and use an end-to-end routing feature to automatically find switch routes by selecting the channels you want to connect. Refer to the
 [National Instruments website](http://ni.com/switchexecutive)
 at
 ni.com/switchexecutive
 for more information about NI Switch Executive.

Use the
 [Switching panel](switching-panel-step-settings-pane.html)
 on the
 [Properties](properties-tab-step-settings-pane.html)
 tab of the
 [Step Settings](step-settings-pane.html)
 pane to connect and disconnect routes required for steps in sequences. When you install NI Switch Executive, you can also use the Switching panel to specify a switching action TestStand performs around the execution of the step.

#### Configuring the Step

Use the
 [Edit IVI Switch Step](edit-ivi-switch-step-dialog-box.html)
 dialog box in the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 and in a
 [TestStand User Interface](teststand-user-interfaces.html)
 to configure the IVI Switch step.

#### Step Operations

The IVI Switch step type supports the following IVI Switch class operations:

- Connect/Disconnect 
 —Connects or disconnects the Source and Destination channels in the switch instrument.
- Configure Scan 
 —Configures the switch instrument for scanning.
- Start Scan 
 —Initiates a scanning operation.
- Wait 
 —Blocks operations until all switches debounce for an instrument.
- Configure Switch 
 —Configures channels as Configuration or Source channels and configures specific paths between channels.
- Send Software Trigger 
 —Sends a software command to trigger the instrument during a scanning operation.
- Abort Scan 
 —Cancels a scanning operation.
- Get Information 
 —Retrieves low-level status and information from the instrument.

The IVI Switch step type supports the following NI Switch Executive operations:

- Connect/Disconnect 
 —Connects or disconnects switch routes for a virtual device.
- Wait 
 —Blocks operations until all switches debounce for a virtual device.
- Get Information 
 —Retrieves low-level status and information from a virtual device.

#### Step Properties

In addition to the
 [common custom properties](/csh?context=ts_tsfundamentals_custom_result_props)
 , the IVI Switch step type defines the following step properties:

- Step.LogicalName 
 —The logical name expression.
- Step.InstrOperation 
 —A value that specifies the operation you configured the step to perform.
- Step.SettingsSource 
 —The name of the property or variable where the step loads and stores the settings for the operation.
- Step.IviOperation 
 —A value that specifies the operation you configured the step to perform for IVI Switching mode.
- Step.ConnectDisconnect 
 —The settings for the Connect/Disconnect operation.
- Step.SoftFrontPanel 
 —The settings for the Show Soft Front Panel operation. The data type of this property is NI_IviSoftFrontPanel.
- Step.GetInfo 
 —The settings for the Get Information operation.
- Step.ScanningConfig 
 —The settings for the Configure Scan operation.
- Step.Wait 
 —The settings for the Wait operation.
- Step.Configure 
 —The settings for the Configure operation.

#### See Also

[IVI Step Types](ivi-step-types.html)

[Switching (Example)](/csh?context=ts_8138)

Parent topic:

IVI Step Types

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/switching-panel-step-settings-pane.html language=enus -->
## TOPIC 04236: Switching Panel - Step Settings Pane

- bundle_id: `teststand-api-reference`
- source_path: `tsref/switching-panel-step-settings-pane.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/switching-panel-step-settings-pane.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Switching Panel The Switching panel specifies a switching action TestStand performs around the execution of the step. This feature is available only when you install NI Switch Executive software. The Switching panel contains the following options: Enable Switching —When you enable this option, TestS

### Switching Panel - Step Settings Pane

#### Switching Panel

The Switching panel specifies a switching action TestStand performs around the execution of the step. This feature is available only when you install NI Switch Executive software.

The Switching panel contains the following options:

- Enable Switching 
 —When you enable this option, TestStand performs a switching action for the step.
- Switch Executive Virtual Device 
 —An expression TestStand evaluates at run time to determine the virtual device on which TestStand performs the switching action.
 Note 
 TestStand does not release an NI Switch Executive virtual device until all executions that use it complete and close.
- Operation 
 —Specifies whether to connect or disconnect the specified routes or disconnect all previously connected routes. This operation returns as soon as the instrument is ready for another operation, which may occur before or after the switches involved settle. Use the
 Wait for Debounce before Executing Step 
 option when you want to wait until all switches have debounced. You can choose from the following options:
  - Connect 
 —Connects the paths for the specified routes in the Route(s) to Connect control.
  - Disconnect 
 —Disconnects the paths the specified routes in the Route(s) to Disconnect control define.
  - DisconnectAll 
 —Disconnects all previously created paths.
  - Connect/Disconnect 
 —Connects the paths for the routes specified in the Route(s) to Connect control and disconnects the paths specified in the Route(s) to Disconnect control. Use the
 Operation Order 
 ring control to specify whether the Disconnect operation occurs before or after the Connect operation.
- Route(s) to Connect 
 —The routes you are connecting. The expression must be a valid
 route specification string 
 as the NI Switch Executive configuration for the virtual device name you are using defines. The string can be a combination of route group alias names, route names, and physical route paths.
- Route(s) to Disconnect 
 —The routes you are disconnecting. The expression must be a valid
 route specification string 
 as the NI Switch Executive configuration for the virtual device name you are using defines. The string can be a combination of route group alias names, route names, and physical route paths.
- Multiconnect Mode 
 —The behavior when more than one connection operation occurs on a specific route. The following options are available:
  - No Multiconnect 
 —A route can only be connected once. Any attempt to reconnect an already connected route results in an error.
  - Multiconnect Routes 
 —A route can be connected multiple times. The route must contain the same endpoints and path. NI Switch Executive automatically reference counts the routes. If you issue multiple connect operations for a specific route, the route is not physically disconnected until an equal number of disconnect operations occur. You can either issue the Disconnect operation manually or use a lifetime setting for the route. The Disconnect All operation disconnects a route even if the route reference count is greater than one.
  - Use Default Setting for Route 
 —Use the setting defined for the route in the NI Switch Executive software.
- Operation Order 
 —Specifies whether the Disconnect operation occurs before or after the Connect operation. The following options are available:
  - Disconnect before Connect 
 —Disconnect the specified routes before connecting any routes. This is the typical mode of operation.
  - Disconnect after Connect 
 —Connect the specified routes before disconnecting any routes. Use this mode of operation when you are switching electric current and want to ensure that a load is always connected to the source.
- Connection Lifetime 
 —The lifetime TestStand applies to the routes specified for connect/disconnect actions. You can specify whether you want the route to exist until manually disconnected later, or until the step, sequence, thread, or execution completes. When you use the Multiconnect Mode, a route can exist longer if another step specifies its own lifetime for the same route. Selecting a lifetime other than manual guarantees that the route stays connected as long as the step, sequence, thread, or execution in which you connect is executing. When you manually disconnect a route previously connected using a non-manual lifetime setting, TestStand releases the reference to the route for the last step that performed a Connect operation for that route.
- Wait for Debounce before Executing Step 
 —When you enable this option, the operation waits for all switches to debounce before returning to TestStand. The wait for debounce occurs after both Connect and Disconnect operations are complete.

#### See Also

[Route Specification Strings](/csh?context=ts_tsref_route_spec_string)

[Switching (Example)](/csh?context=ts_8138)

Parent topic:

Properties Tab - Step Settings Pane

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/switching-tab-step-properties-dialog-box.html language=enus -->
## TOPIC 04237: Switching Tab - Step Properties Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/switching-tab-step-properties-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/switching-tab-step-properties-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Switching Tab The Switching tab of the Step Properties dialog box specifies a switching action TestStand performs around the execution of the step. This feature is available only when you install NI Switch Executive software. The Switching tab contains the following options: Enable Switching —When y

### Switching Tab - Step Properties Dialog Box

#### Switching Tab

The Switching tab of the Step Properties dialog box specifies a switching action TestStand performs around the execution of the step. This feature is available only when you install NI Switch Executive software.

The Switching tab contains the following options:

- Enable Switching 
 —When you enable this option, TestStand performs a switching action for the step.
- Switch Executive Virtual Device 
 —An expression TestStand evaluates at run time to determine the virtual device on which TestStand performs the switching action.
- Operation 
 —Specifies whether to connect or disconnect the specified routes or disconnect all previously connected routes. This operation returns as soon as the instrument is ready for another operation, which might occur before or after the switches involved settle. Use the
 Wait for Debounce before Executing Step 
 option when you want to wait until all switches have debounced. You can choose from the following options:
  - Connect 
 —Connects the paths for the specified routes in the Route(s) to Connect control.
  - Disconnect 
 —Disconnects the paths that the specified routes in the Route(s) to Disconnect control define.
  - Disconnect All 
 —Disconnects all previously created paths.
  - Connect/Disconnect 
 —Connects the paths for the routes specified in the Route(s) to Connect control and disconnects the paths specified in the Route(s) to Disconnect control. Use the
 Operation Order 
 ring control to specify whether the Disconnect operation occurs before or after the Connect operation.
- Route(s) to Connect 
 —The routes you are connecting. The expression must be a valid
 route specification string 
 as the NI Switch Executive configuration for the virtual device name you are using defines. The string can be a combination of route group alias names, route names, and physical route paths.
- Route(s) to Disconnect 
 —The routes you are disconnecting. The expression must be a valid
 route specification string 
 as the NI Switch Executive configuration for the virtual device name you are using defines. The string can be a combination of route group alias names, route names, and physical route paths.
- Multiconnect Mode 
 —The behavior when more than one connection operation occurs on a specific route. The following options are available:
  - Multiconnect Routes 
 —A route can be connected multiple times. The route must contain the same endpoints and path. NI Switch Executive automatically reference counts the routes. If you issue multiple connect operations for a specific route, the route is not physically disconnected until an equal number of disconnect operations occur. You can either issue the Disconnect operation manually or use a lifetime setting for the route. The Disconnect All operation disconnects a route even if the route reference count is greater than one.
  - No Multiconnect 
 —A route can only be connected once. Any attempt to reconnect an already connected route results in an error.
  - Use Default Setting for Route 
 —Use the setting defined for the route in the NI Switch Executive software.
- Operation Order 
 —Specifies whether the Disconnect operation occurs before or after the Connect operation. The following options are available:
  - Disconnect before Connect 
 —Disconnect the specified routes before connecting any routes. This is the typical mode of operation.
  - Connect before Disconnect 
 —Connect the specified routes before disconnecting any routes. Use this mode of operation when you are switching electric current and want to ensure that a load is always connected to the source.
- Connection Lifetime 
 —The lifetime TestStand applies to the routes specified for connect/disconnect actions. You can specify whether you want the route to exist until manually disconnected later, or until the step, sequence, thread, or execution completes. When you use the Multiconnect Mode, a route can exist longer if another step specifies its own lifetime for the same route. Selecting a lifetime other than manual guarantees that the route stays connected as long as the step, sequence, thread, or execution in which you connect is executing. If you manually disconnect a route previously connected using a non-manual lifetime setting, TestStand releases the reference to the route for the last step that performed a Connect operation for the route.
- Wait for Debounce before Executing Step 
 —When you enable this option, the operation waits for all switches to debounce before returning to TestStand. The wait for debounce occurs after both Connect and Disconnect operations are complete.

#### See Also

[Route Specification Strings](/csh?context=ts_tsref_route_spec_string)

Parent topic:

Step Properties Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/synchronization-panel-step-settings-pane.html language=enus -->
## TOPIC 04238: Synchronization Panel - Step Settings Pane

- bundle_id: `teststand-api-reference`
- source_path: `tsref/synchronization-panel-step-settings-pane.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/synchronization-panel-step-settings-pane.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Synchronization Panel The Synchronization panel specifies a synchronization action TestStand performs around the execution of the step. You can specify if a lock protects the execution of the step or if the step synchronizes with other steps in a batch execution. The Synchronization panel contains t

### Synchronization Panel - Step Settings Pane

#### Synchronization Panel

The Synchronization panel specifies a synchronization action TestStand performs around the execution of the step. You can specify if a lock protects the execution of the step or if the step synchronizes with other steps in a batch execution.

The Synchronization panel contains the following options:

- Use Lock to Allow Only One Thread at a Time to Execute the Step 
 —When you enable this option, the step acquires a lock before it executes and releases the lock after it completes.
- Lock Name or Reference Expression 
 —The lock the step acquires and releases. Enter a string expression to specify the name of an existing lock. You can also enter an expression that evaluates to an object reference to an existing Lock object. Leave the control empty to specify if TestStand uses a lock unique to the step.
- Batch Synchronization 
 —The
 batch synchronization operation 
 the step enters before it executes and exits after it completes.
  - No synchronization 
 —Steps do not use batch synchronization.
  - One thread only (first thread executes step, remaining threads skip) 
 —Only one thread in the batch executes a step. When that thread executes the step, all remaining threads in the batch skip the step. The threads in the batch then continue together.
  - Parallel (all threads enter simultaneously) 
 —TestStand releases all the threads simultaneously when all threads in the batch arrive at their respective instances of a step. Each thread blocks after executing the step until all threads continue together.
  - Serial (one thread at a time) 
 —Steps use a Serial section to ensure that each thread in the batch executes each step sequentially and in the order you specify when you create the batch with the Batch Specification step type. When all threads in a batch arrive at a step, TestStand releases one thread at a time in ascending order. As each thread executes the step, the next thread in the batch executes the step. After all threads in the batch execute the step, they continue to the next step.
  - Use model setting 
 —Steps use the batch synchronization setting in the
 Sequence File Properties 
 dialog box for the process model. New sequences specify this setting by default.
  - Use sequence file setting 
 —Steps use the batch synchronization setting the Sequence File Properties dialog box defines for the sequence file the step is in.

#### See Also

[Sequence File Properties dialog box](sequence-file-properties-dialog-box.html)

[Synchronization Step Types](synchronization-step-types.html)

Parent topic:

Properties Tab - Step Settings Pane

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/synchronization-step-types.html language=enus -->
## TOPIC 04239: Synchronization Step Types

- bundle_id: `teststand-api-reference`
- source_path: `tsref/synchronization-step-types.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/synchronization-step-types.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use Synchronization step types to pass data between and perform other operations in multiple threads of an execution, multiple running executions in the same process, and executions running in different processes or on separate computers. You can use the name attribute of synchronization objects to

### Synchronization Step Types

Use Synchronization step types to pass data between and perform other operations in multiple threads of an execution, multiple running executions in the same process, and executions running in different processes or on separate computers. You can use the
 [name attribute](/csh?context=ts_tsref_sync_objects_name)
 of
 [synchronization objects](/csh?context=ts_tsref_sync_objects)
 to perform synchronization operations between executions within a single process or between separate processes and computers.

Most Synchronization step types create and control a particular type of Synchronization object. TestStand includes the following Synchronization step types:

- Lock
- Rendezvous
- Queue
- Notification
- Wait
- Batch Synchronization
- Auto Schedule
- Use Auto Scheduled Resource
- Thread Priority
- Semaphore
- Batch Specification
- CPU Affinity

In the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 , use the edit tab on the
 [Step Settings](step-settings-pane.html)
 pane to configure Synchronization step types. Select an operation for the step to perform and specify the settings for the operation you select. Some operations store output values to variables you specify. You can leave optional outputs empty. You do not write
 [code modules](/csh?context=ts_tsfundamentals_bldgblocks_codemodules)
 for Synchronization steps.

In a
 [TestStand User Interface](teststand-user-interfaces.html)
 , right-click the step and select
 Configure
 <step type>
 from the context menu to configure Synchronization step types. You can also click the
 Configure
 <step type>
 button on the
 [General](general-tab-step-properties-dialog-box.html)
 tab of the
 [Step Properties](step-properties-dialog-box.html)
 dialog box.

#### Resource Usage Profiler

The
 [Resource Usage Profiler](/csh?context=ts_9920)
 to view and record the resources a multithreaded TestStand system uses over a period of time. The profiler records resource usage and TestStand thread synchronization operations the system performs as long as the profiler window is open.

#### See Also

[Comparing Resource Usage Strategies (Example)](/csh?context=ts_8130)

[Resource Usage Profiler](/csh?context=ts_9920)

[Step Settings Pane](step-settings-pane.html)

[Step Properties dialog box](step-properties-dialog-box.html)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/synchronization-tab-sequence-file-properties.html language=enus -->
## TOPIC 04240: Synchronization Tab - Sequence File Properties Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/synchronization-tab-sequence-file-properties.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/synchronization-tab-sequence-file-properties.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Synchronization Tab The Synchronization tab contains the following options: Batch Synchronization —A batch synchronization setting for the sequence file. The batch synchronization setting applies to each step in the sequence file that specifies the Use sequence file setting batch synchronization opt

### Synchronization Tab - Sequence File Properties Dialog Box

#### Synchronization Tab

The Synchronization tab contains the following options:

- Batch Synchronization 
 —A batch synchronization setting for the sequence file. The batch synchronization setting applies to each step in the sequence file that specifies the
 Use sequence file setting 
 batch synchronization option, which is the default for all TestStand step types. TestStand supports the following settings:
  - Use model setting 
 —Steps use the batch synchronization setting in the
 Sequence File Properties 
 dialog box for the process model. New sequences specify this setting by default.
  - No synchronization 
 —Batch synchronization is not used for steps.
  - Serial (one thread at a time) 
 —Steps use a Serial section to ensure that each thread in the batch executes each step sequentially and in the order you specify when you create the batch. When all threads in a batch arrive at a step, TestStand release one thread at a time in ascending order according to the order number you assign to the threads when you add them to the batch using the Batch Specification step type. As each thread executes the step, the next thread in the batch executes the step. After all threads in the batch execute the step, they continue to the next step.
  - Parallel (all threads enter simultaneously) 
 —TestStand releases all the threads simultaneously when all threads in the batch arrive at their respective instances of a step. Each thread blocks after executing the step until all threads continue together.
  - One thread only (first thread executes step, remaining threads skip) 
 —Only one thread in the batch executes a step. Typically, you use this type of section to perform an operation that applies to the batch as a whole, such as raising the temperature in a test chamber. When all threads in a batch arrive at their respective instances of the step, TestStand releases only the thread with the lowest order number. When that thread executes the step, all remaining threads in the batch skip the step. The threads in the batch then continue together.

#### See Also

[Sequence File Properties dialog box](sequence-file-properties-dialog-box.html)

Parent topic:

Sequence File Properties Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/synchronization-tab-step-properties-dialog-bo.html language=enus -->
## TOPIC 04241: Synchronization Tab - Step Properties Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/synchronization-tab-step-properties-dialog-bo.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/synchronization-tab-step-properties-dialog-bo.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Synchronization Tab The Synchronization tab of the Step Properties dialog box specifies a synchronization action TestStand performs around the execution of the step. You can specify that a lock protects the execution of the step or that the step synchronizes with other steps in a batch execution. Th

### Synchronization Tab - Step Properties Dialog Box

#### Synchronization Tab

The Synchronization tab of the Step Properties dialog box specifies a synchronization action TestStand performs around the execution of the step. You can specify that a lock protects the execution of the step or that the step synchronizes with other steps in a batch execution.

The Synchronization tab contains the following options:

- Use Lock to Allow Only One Thread at a Time to Execute the Step 
 —When you enable this option, the step acquires a lock before it executes and releases the lock after it completes.
- Lock Name or Reference Expression 
 —The lock the step acquires and releases. Enter a string expression to specify the name of an existing lock. You can also enter an expression that evaluates to an object reference to an existing Lock object. Leave the control empty to specify if TestStand uses a lock unique to the step.
- Batch Synchronization 
 —The
 batch synchronization operation 
 the step enters before it executes and exits after it completes..
  - Use sequence file setting 
 —Steps use the batch synchronization setting located in the
 Sequence File Properties 
 dialog box for the sequence file the step is in.
  - Use model setting 
 —Steps use the batch synchronization setting in the
 Sequence File Properties 
 dialog box for the process model. New sequences specify this setting by default.
  - No synchronization 
 —No batch synchronization is used for steps.
  - Serial (one thread at a time) 
 —Steps use a Serial section to ensure that each thread in the batch executes each step sequentially and in the order you specify when you create the batch. When all threads in a batch arrive at a step, TestStand releases one thread at a time in ascending order according to the order number you assign to the threads when you add them to the batch using the Batch Specification step type. As each thread executes the step, the next thread in the batch executes the step. After all threads in the batch execute the step, they continue to the next step.
  - Parallel (all threads enter simultaneously) 
 —TestStand releases all the threads simultaneously when all threads in the batch arrive at their respective instances of a step. Each thread blocks after executing the step until all threads continue together.
  - One thread only (first thread executes step, remaining threads skip) 
 —Only one thread in the batch executes a step. Typically, you use this type of section to perform an operation that applies to the batch as a whole, such as raising the temperature in a test chamber. When all threads in a batch arrive at their respective instances of the step, TestStand releases only the thread with the lowest order number. When that thread executes the step, all remaining threads in the batch skip the step. The threads in the batch then continue together.

#### See Also

[Sequence File Properties dialog box](sequence-file-properties-dialog-box.html)

[Synchronization Step Types](synchronization-step-types.html)

Parent topic:

Step Properties Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/system-source-tab-teststand-deployment-utilit.html language=enus -->
## TOPIC 04242: System Source Tab - TestStand Deployment Utility

- bundle_id: `teststand-api-reference`
- source_path: `tsref/system-source-tab-teststand-deployment-utilit.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/system-source-tab-teststand-deployment-utilit.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: System Source Tab Use the System Source tab to select the workspace file or directory that specifies which files to deploy and the location to create the deployment image. The System Source tab contains the following options: Deploy Files —Contains the following options for specifying the location o

### System Source Tab - TestStand Deployment Utility

#### System Source Tab

Use the System Source tab to select the workspace file or directory that
 [specifies which files to deploy](/csh?context=ts_tsdeploysystem_identifyingcomponents)
 and the location to create the deployment image.

The System Source tab contains the following options:

- Deploy Files 
 —Contains the following options for specifying the location on the computer of the files to deploy.
  - From TestStand Workspace File 
 —When you enable this option, the deployment utility deploys a workspace file you specify.
 When deploying a workspace file, the deployment utility analyzes the workspace for any dependent files. For example, the deployment utility searches the steps in every sequence of a sequence file in the workspace file to find the referenced
 code modules 
 and continues recursively searching until the utility analyzes all the files in the workspace hierarchy.
 Note 
 The deployment utility does not require that you include in the workspace file all code modules, excluding .NET and ActiveX code modules, that test sequences reference, but you must include all support files—such as property loader files, image files associated with Message Popup steps, dynamically called code modules and support files, .NET and ActiveX code modules, and other data files code modules require—to correctly create a deployable image or installer of a TestStand system. 
 You can automatically
 exclude certain files from any deployment 
 by editing the
 Filter.ini 
 file, located in the
 [<TestStand Application Data>](/csh?context=ts_tsfundamentals_directories)
 \Cfg 
 directory.
  - Load Workspace in Sequence Editor 
 —The deployment utility loads into the
 TestStand Sequence Editor 
 the workspace file that the From TestStand Workspace File control specifies. This control is dimmed when the From TestStand Workspace File option is disabled.
  - From Directory 
 —When you enable this option, the deployment utility includes files organized in a directory you specify. Enable the
 Include Subdirectories 
 option to also include files in subdirectories of the directory you specify. You can use this option as an alternative to using a workspace file.
    - Include Subdirectories 
 —When you enable this option, the deployment utility includes all files in the subdirectories of the path the From Directory control specifies. This option is dimmed when the From Directory option is disabled.
  - From TestStand Public Directories 
 —When you enable this option, the deployment utility includes files from the
 [<TestStand Public>](/csh?context=ts_tsfundamentals_directories)
 \Components 
 ,
 [<TestStand Public>](/csh?context=ts_tsfundamentals_directories)
 \CodeTemplates 
 , and
 [<TestStand Public>](/csh?context=ts_tsfundamentals_directories)
 \TestStand
 version
 \UserInterfaces 
 directories.
 Note 
 (32-bit TestStand) The deployment utility includes files from the 32-bit TestStand
 [<TestStand Public>](/csh?context=ts_tsfundamentals_directories)
 directories. (64-bit TestStand)The deployment utility includes files from the 64-bit TestStand
 [<TestStand Public>](/csh?context=ts_tsfundamentals_directories)
 directories.
  - From TestStand Configuration Directory 
 —When you enable this option, the deployment utility includes files from the
 Cfg 
 directory. Refer to the
 <TestStand Application Data> Directory 
 topic for more information about the files in this directory.
- Engine Environment Options 
 —Contains settings to configure the active engine environment settings for the deployment. Refer to the
 Deploying with Environments 
 topic for more information on using these settings
  - Engine Environment File 
 —The environment file (
 .tsenv 
 ) used by the TestStand Deployment Utility to find files in a custom <TestStand Public> directory and/or <TestStand Application> directory.
  - Use Environment File To Determine Deployed File Destinations 
 —If you select this option, files you deploy to the <TestStand Public> and <TestStand Application Data> directories will instead be deployed to the custom locations specified in the environment file. To use this option, the paths specified in the environment file must be relative. With this option enabled, the TestStand Deployment Utility also includes the environment file in the deployment. Refer to the
 Deploying to Custom Environment Directories 
 section in the
 Deploying with Environments 
 topic for more information about this setting.
- Location of Deployable Image 
 —The directory to which the deployment utility will copy an image of the system. This image can be copied over the network or put in an installer.

#### See Also

[Deploying TestStand Systems](/csh?context=ts_10203)

Parent topic:

TestStand Deployment Utility

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/tab-context-menu.html language=enus -->
## TOPIC 04243: Tab Context Menu

- bundle_id: `teststand-api-reference`
- source_path: `tsref/tab-context-menu.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/tab-context-menu.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: To access the context menu, right-click a tab in the sequence editor. The items in the context menu vary depending on the type of tab you click. The tab context menu can contain the following items: Close —Closes the tab. Close All But This —Closes all tabs but the active tab. Copy Full Path —Copies

### Tab Context Menu

To access the context menu, right-click a tab in the sequence editor. The items in the context menu vary depending on the type of tab you click.

The tab context menu can contain the following items:

- Close 
 —Closes the tab.
- Close All But This 
 —Closes all tabs but the active tab.
- Copy Full Path 
 —Copies the full path of the file to the clipboard.
- Open Containing Folder 
 —Opens the directory where the file resides.
- New Horizontal Tab Group 
 —Creates a horizontal group of tabs. Available only when you have more than one tab open.
- New Vertical Tab Group 
 —Creates a vertical group of tabs. Available only when you have more than one tab open.
- Move to Next Tab Group 
 —Moves the tab to the next available tab group. Available only when you have more than one tab open.
- Move to Previous Tab Group 
 —Moves the tab to the previous available tab group. Available only when you have more than one tab open.

You can also middle-click a tab to close the tab.

Parent topic:

TestStand Sequence Editor Menus, Panes, and Windows

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/target-file-and-source-settings-tab.html language=enus -->
## TOPIC 04244: Target File and Source Settings Tab

- bundle_id: `teststand-api-reference`
- source_path: `tsref/target-file-and-source-settings-tab.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/target-file-and-source-settings-tab.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Target File and Source Settings Tab The Target File and Source Settings tab of the Property Loader step contains the following options: Identify Step By —Specifies the lookup to uniquely identify a step in the sequence file. Select <Step Name> to import the Step.Name property, <Step ID> to identify

### Target File and Source Settings Tab

#### Target File and Source Settings Tab

The Target File and Source Settings tab of the Property Loader step contains the following options:

- Identify Step By 
 —Specifies the lookup to uniquely identify a step in the sequence file.
 Note 
 Select
 <Step Name>
 to import the
 Step.Name
 property,
 <Step ID>
 to identify a step by its
 Step.ID
 property, and
 <Step Name and ID>
 to identify a step by the string
 Step.Name + " (" + Step.TS.Id + ")"
 .
- Use Current File 
 -Use the current sequence file as the target sequence file.
- Select Sequence File 
 —Specifies the location of the target sequence file to which values
will be imported.
- Select Sequence 
 —Specifies the target sequence to which values will be imported.
 Note 
 Select
 <Current Sequence>
 to import values to the current sequence and
 <All Sequences>
 to import values to all the sequences in the target sequence file.
- Alias Location 
 —Specifies the location of the
 alias 
 . If the property loader source is a file, this field 
specifies the location of the alias file. If the property loader source is a database, this specifies field specifies 
the name of the alias table.
- Property Selector 
 —Use this control to specify various properties for which values will be
imported from the selected property loader source. Use the Property Selector to select the properties from a list of all the properties and variables available in the selected sequence
file and sequence.

Note

- The
 Import All Data From Source 
 option on the
 Step Settings tab 
 is enabled.
- The sequence file is not editable.

Parent topic:

Configuring a Property Loader Source

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/test-data-cluster.html language=enus -->
## TOPIC 04245: Test Data Cluster

- bundle_id: `teststand-api-reference`
- source_path: `tsref/test-data-cluster.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/test-data-cluster.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: The LabVIEW Adapter uses the Test Data cluster to return result data from the VI to TestStand, which then uses the data to make a pass/fail determination. The following table lists the elements of the Test Data cluster, specifies the data type of the cluster element, describes how the LabVIEW Adapte

### Test Data Cluster

The LabVIEW Adapter uses the
 Test Data
 cluster to return result data from the VI to TestStand, which then uses the data to make a pass/fail determination.

The following table lists the elements of the
 Test Data
 cluster, specifies the data type of the cluster element, describes how the LabVIEW Adapter uses each cluster element, and specifies the TestStand property to which the adapter copies the cluster element value.

| Cluster Element | Data Type | Description | TestStand Property to Which the Adapter Copies the Value |
| --- | --- | --- | --- |
| PASS/FAIL Flag |  | The test VI sets this element to indicate whether the test passed. Valid values are True (PASS) or False (FAIL). | Step.Result.PassFail |
| Numeric Measurement |  | Numeric measurement the test VI returns. | Step.Result.Numeric |
| String Measurement |  | String value the test VI returns. | Step.Result.String |
| Report Text |  | Output message to include in the report. | Step.Result.ReportText |

#### Legacy Test Data Cluster

The LabVIEW Adapter also supports a legacy version of the
 Test Data
 cluster from the LabVIEW Test Executive. The LabVIEW Test Executive
 Test Data
 cluster does not contain a
 Report Text
 element but instead contains the
 Comment
 and
 User Output
 string elements.

The following table lists the elements of the legacy
 Test Data
 cluster, specifies the data type of the cluster element, describes how the LabVIEW Adapter uses each cluster element, and specifies the TestStand property to which the adapter copies the cluster element value.

| Cluster Element | Data Type | Description | TestStand Property to Which the Adapter Copies the Value |
| --- | --- | --- | --- |
| Comment |  | Output message to include in the report. | Step.Result.ReportText |
| User Output |  | String value the test VI returns. | Step.Result.UserOutput |

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/test-step-types.html language=enus -->
## TOPIC 04246: Test Step Types

- bundle_id: `teststand-api-reference`
- source_path: `tsref/test-step-types.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/test-step-types.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: TestStand comes with the following four step types for performing Boolean, numeric, and string tests. Pass/Fail Test Numeric Limit Test Multiple Numeric Limit Test String Value Test To edit a test step type in the TestStand Sequence Editor , use the edit tabs on the Step Settings pane. The tabs avai

### Test Step Types

TestStand comes with the following four step types for performing Boolean, numeric, and string tests.

- Pass/Fail Test
- Numeric Limit Test
- Multiple Numeric Limit Test
- String Value Test

To edit a test step type in the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 , use the edit tabs on the
 [Step Settings](step-settings-pane.html)
 pane. The tabs available update based on the type of step you select.

To edit a test step type in a
 [TestStand User Interface](teststand-user-interfaces.html)
 , select
 Edit
 from the context menu for the step or click
 Edit
 on the
 [General](general-tab-step-properties-dialog-box.html)
 tab of the
 [Step Properties](step-properties-dialog-box.html)
 dialog box.

#### See Also

[Step Properties dialog box](step-properties-dialog-box.html)

[Step Settings Pane](step-settings-pane.html)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/test-vector-and-value-summary-table-view.html language=enus -->
## TOPIC 04247: Test Vector and Value Summary Table View

- bundle_id: `teststand-api-reference`
- source_path: `tsref/test-vector-and-value-summary-table-view.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/test-vector-and-value-summary-table-view.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Test Vector and Value Summary Table View to interact with values and test vectors from a sweep across selected parameters. To access these tables, open the Step Settings pane of a Sweep Loop step, select the Sweep Parameters tab, and click Open Table View . In this view, you can switch betwe

### Test Vector and Value Summary Table View

Use the Test Vector and Value Summary Table View to interact with values and test vectors from a sweep across selected parameters. To access these tables, open the Step Settings pane of a Sweep Loop step, select the Sweep Parameters tab, and click
 Open Table View
 . In this view, you can switch between the Test Vector Table and the Value Summary Table.

The Table View displays the following tabs:

- Edit 
 —Displays test vectors and summary of values for selected parameters at edit time. Dynamic parameter values are estimated, and are only indicated in the Edit view.
 Note 
 If you rename or change the type of a Dynamic parameter in the Step Settings, the Test Vector Table will be marked as out of sync. Refresh the table to reflect your changes.
- Execution 
 —Displays test vectors and summary of values for selected parameters at run time.

#### Test Vector Table

This table displays the following details:

- Number of Test Vectors 
 —Indicates the number of loops the sweep loop will execute if allowed to run to completion. This number is an estimate for Dynamic parameters since Dynamic parameter values may change at run time.
- Offset 
 —Displays the offset value of each test vector. For zero-based one-dimensional arrays, the offset is equal to the index of the array. For multi-dimensional arrays, the offset is the linearized index of the array. For streams, the offset is a zero-based counter of the number of loop iterations.
- Iteration 
 —Displays the iteration value of each test vector. This value represents the loop offset of each parameter in relation to its level of nesting. All parameters at the same level have a single value representing their offset"
- Parameter characteristics 
 —Indicates whether the values are static, dynamic, or being logged. This information is stored in each test vector column's header.

Use this table to perform the following actions on the selected parameters:

- Sort and filter 
 —View the test vectors for selected parameters. Filter and group specific values or ranges of values.
 Note 
 Filtering the Test Vector Table does not affect the operation at run time. Ensure that the rows you want to exclude at run time are disabled at edit time.
- Enable/disable (Edit tab only) 
 —Enable or disable test vectors or ranges of test vectors for an individual or group of rows. Dynamic parameter values displayed in the Test Vector Table cannot be enabled or disabled.
- Copy 
 —Copy selected test vector rows and column headers to the clipboard in a comma delimited text format.
- Export to CSV File 
 —Save the test vectors generated on the Edit Tab or the Execution Tab to a CSV file.
 Note 
 You can only export the data of completed executions. This option will be disabled when test vectors are being generated.
- View Data (Execution tab only) 
 —View the data for a particular run of the step.

#### Value Summary Table

This table displays read-only parameter values across selected parameters.

#### See Also

[Sweep Loop Step](sweep-loop-step.html)

[Sweep Loop Parameters Tab](sweep-parameters-tab.html)

Parent topic:

Sweep Parameters Tab

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/testdata-parameter-labwindows-cvi-call-parame.html language=enus -->
## TOPIC 04248: TestData Parameter - LabWindows/CVI Call Parameters

- bundle_id: `teststand-api-reference`
- source_path: `tsref/testdata-parameter-labwindows-cvi-call-parame.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/testdata-parameter-labwindows-cvi-call-parame.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: TestData Parameter The TestData data type was used in TestStand 2.0. x with the C/CVI Standard Prototype Adapter, which required you to use a specific prototype. This parameter type represents a C structure that contains input and output data for the code module . Use this parameter for compatibilit

### TestData Parameter - LabWindows/CVI Call Parameters

#### TestData Parameter

The TestData data type was used in TestStand 2.0.
 x
 with the C/CVI Standard Prototype Adapter, which required you to use a specific prototype. This parameter type represents a C structure that contains input and output data for the
 [code module](/csh?context=ts_tsfundamentals_bldgblocks_codemodules)
 .

Note

The Pass Sequence Context option specifies whether the LabWindows/CVI Adapter passes a sequence context to the code module. Enable this option when you want to call the TestStand API in the code module or when the code module must pass the sequence context to another function.

#### See Also

[Calling Legacy LabWindows/CVI Code Modules](/csh?context=ts_tsref_lwcvicalllegacycodemods)

[Mapping Parameters](/csh?context=ts_tsref_parameters)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/testerror-parameter-labwindows-cvi-call-param.html language=enus -->
## TOPIC 04249: TestError Parameter - LabWindows/CVI Call Parameters

- bundle_id: `teststand-api-reference`
- source_path: `tsref/testerror-parameter-labwindows-cvi-call-param.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/testerror-parameter-labwindows-cvi-call-param.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: TestError Parameter The TestError data type was used in TestStand 2.0. x with the C/CVI Standard Prototype Adapter, which required you to use a specific prototype. This parameter type represents a C structure that contains output data for the code module. Use this parameter for compatibility purpose

### TestError Parameter - LabWindows/CVI Call Parameters

#### TestError Parameter

The TestError data type was used in TestStand 2.0.
 x
 with the C/CVI Standard Prototype Adapter, which required you to use a specific prototype. This parameter type represents a C structure that contains output data for the code module.

Note

#### See Also

[Calling Legacy LabWindows/CVI Code Modules](/csh?context=ts_tsref_lwcvicalllegacycodemods)

[Mapping Parameters](/csh?context=ts_tsref_parameters)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/teststand-api-tab-expression-browser-dialog-b.html language=enus -->
## TOPIC 04250: TestStand API Tab - Expression Browser Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/teststand-api-tab-expression-browser-dialog-b.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/teststand-api-tab-expression-browser-dialog-b.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: TestStand API Tab Use the TestStand API tab to build a call to a property or method in the TestStand API for a variable or property in the sequence context. The TestStand API tab contains the following options: Show Objects with Interface —TestStand only displays objects with a specific interface in

### TestStand API Tab - Expression Browser Dialog Box

#### TestStand API Tab

Use the TestStand API tab to build a call to a property or method in the TestStand API for a variable or property in the sequence context.

The TestStand API tab contains the following options:

- Show Objects with Interface 
 —TestStand only displays objects with a specific interface in the sequence context tree control.
- Show Members of Interface 
 —The interface and the property or method to call.
- Replace 
 and
 Insert 
 —Replaces or inserts a call to a property or method for a variable or property in the sequence context at the cursor location in the Expression control.

Parent topic:

Expression Browser Dialog Box
