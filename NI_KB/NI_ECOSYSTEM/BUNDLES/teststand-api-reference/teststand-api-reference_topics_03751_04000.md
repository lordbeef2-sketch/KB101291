# NI DOCUMENT BUNDLE: teststand-api-reference

<!--NI_BUNDLE_CHUNK bundle=teststand-api-reference start=3751 end=4000 -->
<!--NI_TOPIC bundle=teststand-api-reference path=tsref/general-tab-file-differ-options-dialog-box.html language=enus -->
## TOPIC 03751: General Tab - File Differ Options Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/general-tab-file-differ-options-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/general-tab-file-differ-options-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: General Tab The General tab contains the following options: Automatically Merge Types —TestStand automatically resolves type conflicts when loading sequence files and type palette files. Disable this option when you want to see type differences when you compare two files. When you compare three file

### General Tab - File Differ Options Dialog Box

#### General Tab

The General tab contains the following options:

- Automatically Merge Types 
 —TestStand automatically resolves type conflicts when loading sequence files and type palette files. Disable this option when you want to see type differences when you compare two files. When you compare three files, the utility always resolves types, so this option does not apply.
 When you enable this option, the following options also become available:
 
 Note 
 If you change the Automatically Merge Types, Load Type Palettes, or Allow Automatic Type Conflict Resolution options after you load and compare files and you then click
 OK
 to close the File Differ Options dialog box, the utility reloads and recompares the files. When you compare three files, recomparing the files recreates the merged file but without the edits you previously specified.
  - Load Type Palettes 
 —The utility loads the type palettes before loading any files to compare. Use this option to merge any changes in the type palettes into the types the files contain. This is the same behavior as opening a file in the
 TestStand Sequence Editor 
 or in a
 TestStand User Interface 
 . If you do not enable this option, the types in the files might not be up to date and might result in a type conflict.
  - Load Process Model 
 —The utility loads the process model associated with each sequence file before comparing the files. Use this option to merge any changes in the process model into the types the sequence files contain. This is the same behavior as opening a file in the sequence editor or in a user interface. If you do not enable this option, the types in the files might not be up to date and might result in a type conflict.
  - Allow Automatic Type Conflict Resolution 
 —Specifies when you want TestStand to automatically resolve type conflicts. TestStand normally resolves type conflicts when it loads a file with a version of a type that differs from the version of the type currently in memory and when you enable the
 Use the definition that has the highest version number 
 option on the
 Version 
 tab of the
 Type Properties 
 dialog box or on the
 Version 
 tab of the
 Step Type Properties 
 dialog box for both versions of the type. In this case, TestStand updates the file with the lower version of the type to use the higher version. 
 The Allow Automatic Type Conflict Resolution ring control contains the following options:
    - Always (same as TestStand 4.0.x or earlier) 
 —Always allows automatic type conflict resolution by using version numbers, which can cause unintended propagation of types between files. For example, if you open a sequence file with a version of a type later than the version of the type currently in a type palette file, TestStand updates the type palette file and every file you subsequently open to use the later version. The updated type propagates to other files without warning or notifying you.
    - Only if Type Palette Files will not be Modified (default) 
 —Disallows automatic type conflict resolution when the outcome of the resolution modifies a type palette file. This ensures that the application never uses a version of a type that is different than the version of the type in the type palette file without an explicit confirmation through the
 Type Conflict in File 
 dialog box.
    - Only if a Type Palette File has the Higher Version 
 —Further restricts automatic type conflict resolution. This option includes the same restrictions as the Only if Type Palette Files will not be Modified (default) option and includes the restriction that the type must be in a type palette file for automatic type conflict resolution to occur. Effectively, this option allows automatic type conflict resolution only in the case in which a type palette file has the later version of the type and a non-type palette file has the earlier version of the type.
 For example, this option does not allow automatic type conflict resolution between two sequence files for types that are not in type palette files. The Only if Type Palette Files will not be Modified (default) option does allow this.
    - Never 
 —Disallows all
 automatic type conflict resolution 
 . When TestStand loads two different versions of a type, TestStand always prompts you or reports a type conflict error. When you select this option, opening files from TestStand versions earlier than the current version almost always results in type conflict prompts. Use this option only for debugging purposes or to ensure that all files have exactly the same version of every type.
- Allow Editing of Read-Only Files 
 —When you enable this option, you can make changes to files in memory that are marked as read-only on disk. You cannot save changes to a read-only file. You must save the file with a new name to preserve any changes.
- Require Step IDs To Match (Requires Rediffing Files) 
 —This option is disabled by default. When comparing steps, by default the utility compares the steps by comparing the unique step IDs and step names and uses the comparison that returns the most matches. Enable this option to override the default behavior and specify that the utility compares the unique step IDs when matching two steps from two different files.
 Note 
 If you make changes to this option after you load and compare files and you then click
 OK
 to close the File Differ Options dialog box, the utility reloads and recompares the files. When you compare three files, recomparing the files recreates the merged file but without the edits you previously specified.
- Include Values In Property Names 
 —Includes the value for properties of basic types in the property name.
- Show Underlying Property Names 
 —Shows the real name of a property instead of its display name. This option applies only to NI-installed types.
- When Diffing Two Files, Treat First File As The Base File 
 —When you compare two files, the utility regards the first file as the base file. When you enable this option, the first file does not show any differences, and all differences appear in the second file.
- Ignore Differences in Sequence Order 
 —When you enable this option, you sort the sequences in the sequence file into alphabetical order before they are diffed. This allows you to see the differences in the sequences when a sequence changes location in the other file.
- File Background Color 
 —The background color to use for each file in the
 File list 
 and
 Differences table 
 in the utility. Click the
 Change File Background Color 
 button or double-click a file to launch the Microsoft Windows Color dialog box, in which you can select a new color. To reset to the default color, select the first color available in the Custom colors section of the Color dialog box.

#### See Also

[Managing Type Revisions](/csh?context=ts_tsfundamentals_types_revision)

[Step Type Properties dialog box](step-type-properties-dialog-box.html)

[Type Conflict in File dialog box](type-conflict-in-file-dialog-box.html)

[Type Properties dialog box](type-properties-dialog-box.html)

Parent topic:

File Differ Options Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/general-tab-properties-dialog-box.html language=enus -->
## TOPIC 03752: General Tab - Properties Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/general-tab-properties-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/general-tab-properties-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: General Tab The General tab contains the following options: Type —The data type of the property. Value —The value for the property. For object reference properties, click Release to set the value to Nothing . Numeric Format —Launches the Numeric Format dialog box, in which you can specify the format

### General Tab - Properties Dialog Box

#### General Tab

The General tab contains the following options:

- Type 
 —The data type of the property.
- Value 
 —The value for the property. For object reference properties, click
 Release 
 to set the value to
 Nothing 
 .
- Numeric Format 
 —Launches the
 Numeric Format 
 dialog box, in which you can specify the format TestStand uses to display the value of a numeric property.
 Note 
 This control is available only for numeric and numeric array properties.
- Comment 
 —The comment for the property.
- Advanced 
 —Displays a submenu with the following options:
  - Flags 
 —Launches the
 Edit Flags 
 dialog box, in which you can modify the flags for the property.
  - Attributes 
 —Launches the
 Attributes 
 dialog box, in which you can create and edit attributes for the property.

#### See Also

[Attributes dialog box](attributes-dialog-box.html)

[Edit Flags dialog box](edit-flags-dialog-box.html)

[Numeric Format dialog box](numeric-format-dialog-box.html)

Parent topic:

Properties Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/general-tab-sequence-editor-options-dialog-bo.html language=enus -->
## TOPIC 03753: General Tab - Sequence Editor Options Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/general-tab-sequence-editor-options-dialog-bo.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/general-tab-sequence-editor-options-dialog-bo.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: General Tab The General tab contains the following options: Close Completed Execution Displays on Execution Start —Closes all completed Execution windows automatically when you start a new execution. Disable 'View User Manager' Command —Disables the User Manager menu and toolbar items. Allow Editing

### General Tab - Sequence Editor Options Dialog Box

#### General Tab

The General tab contains the following options:

- Close Completed Execution Displays on Execution Start 
 —Closes all completed Execution windows automatically when you start a new execution.
- Disable 'View User Manager' Command 
 —Disables the User Manager menu and toolbar items.
- Allow Editing of Read-Only Files 
 —When you enable this option, you can make changes in the
 TestStand Sequence Editor 
 to files marked as read-only on disk. You cannot save changes to the read-only file. You must save the file with a new name to preserve any changes.
- Show List View Tooltips 
 —Disables the tooltip that displays the entire contents of a field. A tooltip is useful for viewing a field longer than the column that displays the field.
- Make Step Names Unique when Inserting Steps 
 —Configures the sequence editor to ensure that step names are unique when you insert steps in a sequence. This option applies to any inserted step, whether you create a new step or copy and paste a step from another sequence.
- File Menu MRU List Size for Sequence Files 
 —Specifies the number of sequence files that appear in the File Menu MRU list.
- File Menu MRU List Size for Workspace Files 
 —Specifies the number of workspace files that appear in the File Menu MRU list.
- Save before Running 
 —Configures the sequence editor to never save modified files, to always save modified files, or to prompt you to save modified files before running.
- Back Up Sequence Files when Resaving in Older or Newer Format 
 —Configures the sequence editor to never backup, always backup, or to prompt you to backup sequence files you resave with an older or newer format.

Parent topic:

Sequence Editor Options Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/general-tab-sequence-file-properties-dialog-b.html language=enus -->
## TOPIC 03754: General Tab - Sequence File Properties Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/general-tab-sequence-file-properties-dialog-b.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/general-tab-sequence-file-properties-dialog-b.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: General Tab The General tab contains the following options: Full Path —The location of the sequence file on disk. Size —The size of the sequence file on the disk drive. Saved —The time at which you last saved the sequence file. File Revision —The sequence file version number. A version number consis

### General Tab - Sequence File Properties Dialog Box

#### General Tab

The General tab contains the following options:

- Full Path 
 —The location of the sequence file on disk.
- Size 
 —The size of the sequence file on the disk drive.
- Saved 
 —The time at which you last saved the sequence file.
- File Revision 
 —The sequence file version number. A version number consists of four integer numbers you separate with periods. The numbers from left to right denote the Major, Minor, Revision, and Build version. You can manually specify the version number or select
 Configure»Station Options 
 and set the
 Auto Increment Sequence File Version 
 option on the
 File 
 tab of the
 Station Options 
 dialog box. This control specifies that the sequence editor increments the version number each time you save the modified sequence file.
- Sequence File Version 
 —The TestStand version in which the sequence file was saved.
- Load Option 
 —Specifies one of the following load option settings for every step in the sequence file.
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
  - Use step load option 
 —Specifies whether TestStand loads each code module according to the Load Option for the particular step that calls the code module. Use the
 Run Options panel 
 on the
 Step Settings 
 pane in the sequence editor or the
 Run Options 
 tab of the
 Step Properties 
 dialog box from a
 TestStand User Interface 
 to update the Load Option settings.
- Unload Option 
 —Specifies when the steps in the sequence file release the references to code modules. TestStand unloads a code module when all steps that refer to the code module can unload. This option specifies one of the following unload option settings for every step in the sequence file:
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
  - Use step unload option 
 —Specifies whether TestStand unloads each code module according to the unload option for the particular step that calls the code module. Use the
 Run Options panel 
 on the
 Step Settings 
 pane or the
 Run Options 
 tab of the
 Step Properties 
 dialog box from a user interface to update the Unload Option settings.
 Note 
 If you enable the Optimize Non-Reentrant Calls to this Sequence option on the
 [General](general-tab-sequence-properties-dialog-box.html)
 tab of the
 [Sequence Properties](sequence-properties-dialog-box.html)
 dialog box, TestStand maintains a loaded copy of the sequence until the execution is complete and does not unload the code modules for the sequence until after the execution ends, even if you attempt to unload the sequence and regardless of the Unload Option setting for the sequence file or the steps in the sequence. Because you cannot programmatically edit a loaded sequence, disable this option if you need to modify the sequence at run time.
- Sequence File Globals 
 —The lifetime of the sequence file global variables and whether multiple executions share the sequence file global variable values. You can select one of the following settings:
 
 Note 
 For either setting, if a sequence file unloads from memory and an execution later reloads the file, the execution creates a new run-time copy of the file globals and initializes them to their default values.
  - Separate File Globals for Each Execution 
 —Specifies whether each execution that runs the file creates a separate run-time copy of the global variables and initializes them to their default values. This command is the default setting. Threads within an execution share the run-time copy for the execution.
  - All Executions Share the Same File Globals 
 —Specifies that the first execution that runs the sequence file creates a run-time copy of the global variables and initializes them to their default values. Any other execution that runs the file concurrently uses the same global variables. When the last execution that uses the file globals completes, TestStand discards the file globals. A common use case for selecting this option might be when you want to share variables between multiple executions you start with the Batch or Parallel process model.
- Comment 
 —Places a comment in the documentation TestStand generates for the sequence file.
- File Format 
 —The format of the file.
 Choose from one of the following formats: 
 
 Notice 
 If you change a file you store in an SCC system from XML or INI to binary, you must update the SCC system to set the file type as binary. Otherwise the SCC provider might incorrectly process the binary content of the file that appears to be white space, resulting in a corrupt file.
  - INI (format available in TestStand 3.
 x 
 or earlier)
 Note 
 The Sequence File Properties dialog box no longer provides the option to change from another file format to INI. Reading INI files is still supported. Saving files in the INI format will be deprecated in a future release of TestStand.
  - XML (most readable, largest)
 Note 
 National Instruments reserves the right to change the XML file format in future releases to support new features and to improve usability.
  - Binary (fastest and smallest)
- Requirements List 
 —Provides a mechanism for notating product and unit requirements the sequence file covers. This control contains a list of strings where each string represents a single requirement. You can also notate requirements information in the
 Workspace Object Properties 
 and
 Sequence Properties 
 dialog boxes, the
 Step Settings 
 pane in the sequence editor, or the
 Step Properties 
 dialog box in a user interface.
 Note 
 External requirements management packages, such as NI Requirements Gateway, define the format of the values that represent a requirement. A requirements management software package can use the TestStand API to retrieve or specify requirement values for sequence files using the
 [PropertyObjectFile](../tsapiref/propertyobjectfile.html)
 interface.

#### See Also

[PropertyObjectFile](../tsapiref/propertyobjectfile.html)

[Sequence File Translators](/csh?context=ts_tsfundamentals_translators)

[Sequence Properties dialog box](sequence-properties-dialog-box.html)

[Station Options dialog box](station-options-dialog-box.html)

[Step Properties dialog box](step-properties-dialog-box.html)

[Step Settings Pane](step-settings-pane.html)

[Workspace Object Properties dialog box](workspace-object-properties-dialog-box.html)

Parent topic:

Sequence File Properties Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/general-tab-sequence-properties-dialog-box.html language=enus -->
## TOPIC 03755: General Tab - Sequence Properties Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/general-tab-sequence-properties-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/general-tab-sequence-properties-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: General Tab The General tab contains the following options: On Step Failure —Specifies whether the execution flow jumps to the Cleanup step group if a step sets the status of the sequence to Failed . Select one of the following options from the ring control: No Action —Specifies that a failure does

### General Tab - Sequence Properties Dialog Box

#### General Tab

The General tab contains the following options:

- On Step Failure 
 —Specifies whether the execution flow jumps to the Cleanup step group if a step sets the status of the sequence to
 Failed 
 . Select one of the following options from the ring control:
 
 Note 
 This option takes precedence over Goto Destination post action settings.
  - No Action 
 —Specifies that a failure does not cause the execution flow to jump to the Cleanup step group.
  - Goto Cleanup 
 —Specifies that a failure causes the execution flow to jump to the Cleanup step group.
  - Use Station Option 
 —Specifies that a failure causes the execution flow to jump to the Cleanup step group if you have enabled the Immediately Goto Cleanup On Sequence Failure option on the
 Execution 
 tab of the
 Station Options 
 dialog box. If you disable the Immediately Goto Cleanup on Sequence Failure option and the step sets the status of the sequence to
 Failed 
 , the execution flow continues without jumping to the Cleanup step group. Use Station Option is selected by default.
- Disable Result Recording for All Steps 
 —Prevents TestStand from adding results for the steps in the sequence to the
 result list 
 .
- Optimize Non-Reentrant Calls to this Sequence 
 —Decreases the time it takes TestStand to call the sequence after the first call to the sequence in an execution. When you disable this option, TestStand initializes a new copy of each custom step property in a sequence each time it calls the sequence. TestStand performs this initialization so the sequence always begins executing with the initial property values the steps in the sequence specify. This initialization is only necessary if a sequence relies on the initial value of a custom step property and then modifies the value. Few sequences rely on this information.
 When you enable this option, TestStand initializes the values of custom step properties in the sequence the first time it calls the sequence in an execution. TestStand reuses the values of the custom step properties when it calls the sequence again. If the same sequence is called at the same time in different threads or recursively within the same thread, TestStand creates unique copies of the custom step properties. 
 Note 
 When you enable this option, TestStand maintains a loaded copy of the sequence until the execution is complete and does not unload the code modules for the sequence until after the execution ends, even if you attempt to unload the sequence and regardless of the Unload Option setting for the sequence file or the steps in the sequence. Because you cannot programmatically edit a loaded sequence, disable this option if you need to modify the sequence at run time.
- Comment 
 —Places a comment for the sequence in the All Sequences view. The sequence comment also appears in the documentation TestStand generates for the sequence file.
- Requirements List 
 —Provides a mechanism for notating product and unit requirements the sequence covers. This control contains a list of strings where each string represents a single requirement. You can also notate requirements information in the
 Workspace Object Properties 
 and
 Sequence Properties 
 dialog boxes, the
 Step Settings 
 pane in the
 TestStand Sequence Editor 
 , or the
 Step Properties 
 dialog box in a
 TestStand User Interface 
 .
 Note 
 External requirements management packages, such as NI Requirements Gateway, define the format of the values that represent a requirement. A requirements management software package can use the TestStand API to retrieve or specify requirement values from
 [Sequence](../tsapiref/sequence.html)
 objects.
- Preconditions 
 —Launches the
 Preconditions 
 dialog box, in which you can specify the conditions that must be
 True 
 for each step in the sequence to run. When you access this dialog box from the
 Preconditions panel 
 on the Properties tab of the
 Step Settings 
 pane or in the
 Step Properties 
 dialog box, it applies only to a particular step. When you access the dialog box from the Sequence Properties dialog box, you can view and edit the preconditions for each step in the sequence.
- Advanced 
 —Displays a submenu with the following options:
  - Flags 
 —Launches the
 Edit Flags 
 dialog box, in which you can modify the property flags for the sequence.
  - Attributes 
 —Launches the
 Attributes 
 dialog box, in which you can create and edit attributes for the sequence.

If the sequence file is a process model file, the Sequence Properties dialog box also has a
 [Model](model-tab-sequence-properties-dialog-box.html)
 tab.

#### See Also

[Attributes dialog box](attributes-dialog-box.html)

[Edit Flags dialog box](edit-flags-dialog-box.html)

[Preconditions dialog box](preconditions-dialog-box.html)

[Sequence](../tsapiref/sequence.html)

[Sequence Properties dialog box](sequence-properties-dialog-box.html)

[Station Options dialog box](station-options-dialog-box.html)

[Step Properties dialog box](step-properties-dialog-box.html)

[Step Settings Pane](step-settings-pane.html)

[Workspace Object Properties dialog box](workspace-object-properties-dialog-box.html)

Parent topic:

Sequence Properties Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/general-tab-step-properties-dialog-box.html language=enus -->
## TOPIC 03756: General Tab - Step Properties Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/general-tab-step-properties-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/general-tab-step-properties-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: General Tab The General tab contains the following options: Type —The type for the step. Change Step Type —Displays a submenu from which you select the type of step you want TestStand to convert the existing step to. TestStand discards any values in properties of the current step type that do not ex

### General Tab - Step Properties Dialog Box

#### General Tab

The General tab contains the following options:

- Type 
 —The type for the step.
  - Change Step Type 
 —Displays a submenu from which you select the type of step you want TestStand to convert the existing step to. TestStand discards any values in properties of the current step type that do not exist in the new step type. TestStand uses the default values for properties in the new step type that do not exist in the current step type.
- Adapter 
 —The adapter the step uses. You can change the adapter by selecting a different adapter in the ring control. TestStand discards module and parameter information unless you are changing the adapter from the LabWindows/CVI Adapter to the C/C++ DLL Adapter or vice versa.
  - Specify Module 
 —Launches the Specify Module dialog box for the selected step. The dialog box is specific to the module adapter assigned to the step. Use the Specify Module dialog box to specify the
 code module 
 the step calls. You can also specify options TestStand uses when it calls the step.
- Description 
 —A description of the step that varies according to the type of step and the adapter it uses.
- Comment 
 —Places a comment for the step in the Step Group list view. The step comment also appears in the documentation TestStand generates for the sequence file.
- Edit 
 —Launches a dialog box in which you can edit the settings unique to the type of the step. The button caption varies according to the type of the step. Refer to the Edit <
 Step Name 
 > dialog box for the step you have inserted for more information.
- Preconditions 
 —Launches the
 Preconditions 
 dialog box, in which you can specify the conditions that must be
 True 
 for the step to execute.
- Additional Results 
 —Launches the
 Additional Results 
 dialog box, in which you can add and configure values to add to the result list of a step when the step executes.
- Advanced 
 —Displays a submenu with the following option:
  - Attributes 
 —Launches the
 Attributes 
 dialog box, in which you can create and edit attributes for the step.

#### See Also

[Additional Results dialog box](additional-results-dialog-box.html)

[Attributes dialog box](attributes-dialog-box.html)

[Module Tabs and Specify Module Dialog Boxes](specify-module-tabs-and-dialog-boxes.html)

[Preconditions dialog box](preconditions-dialog-box.html)

Parent topic:

Step Properties Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/general-tab-step-type-properties-dialog-box.html language=enus -->
## TOPIC 03757: General Tab - Step Type Properties Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/general-tab-step-type-properties-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/general-tab-step-type-properties-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: General Tab Use the General tab to specify the following information: A name, description, and comment for the step type. The default module adapter and the default code module the step type calls. After you create an instance step type, you can use the Properties tab on the Step Settings pane in th

### General Tab - Step Type Properties Dialog Box

#### General Tab

Use the General tab to specify the following information:

- A name, description, and comment for the step type.
- The default module adapter and the default
 code module 
 the step type calls.

Note

- After you create an instance step type, you can use the
 Properties 
 tab on the
 Step Settings 
 pane in the sequence editor or the
 Step Type Properties 
 dialog box in a user interface to change the adapter and code module call.
- When you want code module changes to propagate to all instances of the step type, complete the following steps.
  1. Change all instances of the step type to use the <None> adapter so the step does not call a code module.
  2. Create a Post-Step
 substep 
 for the step type.
  3. Call the code module from this substep instead of specifying a default adapter and code module.
- When you do not want sequence developers to change or edit the default code module call, enable the
 Specify Module 
 option on the
 Disable Properties 
 tab.

The General tab contains the following options:

- Designate an Icon 
 —An icon for the step type. When you enable this option, you can select from a list of icons in the
 [<TestStand>](/csh?context=ts_tsfundamentals_directories)
 \Components\Icons 
 and
 [<TestStand Public>](/csh?context=ts_tsfundamentals_directories)
 \Components\Icons 
 directories. TestStand displays the icon next to the step names for all steps that use the step type. When you disable this option, TestStand displays the icon of the module adapter for each step. If you can use any module adapter with the step type, it is best to disable this option.
- Default Step Name Expression 
 —A string expression TestStand evaluates when you create a new step with the step type. TestStand uses the value of the expression as the name of the new step. If a step with the same name already exists in the sequence, TestStand appends
 _
 n 
 to the name to make it unique. When you want to store the name in a string resource file, you can use the
 ResStr 
 expression function to retrieve the name from the file. Storing the name in a string resource file is useful when you want to display the name in different languages.
- Step Description Expression 
 —A string expression TestStand evaluates whenever it displays the Description field for a step. TestStand uses the value of the expression as the contents of the Description field for the step. If you include the
 %ModuleDescription 
 macro in a string you surround with double quotes, TestStand replaces the
 %ModuleDescription 
 macro with text the module adapter provides that describes the code module the step uses.
- Designate an Adapter 
 —A single module adapter for the step type. When you enable this option, all steps you create with the step type use the module adapter you designate, regardless of the module adapter you select in the Adapter ring control. A sequence developer can change the adapter after creating the step using the
 Properties 
 tab of the
 Step Settings 
 pane or in the
 Step Properties 
 dialog box of a
 TestStand User Interface 
 .
 You can choose from a list of all the module adapters. If the step type does not require a module adapter, select
 <None>
 from the module adapter list. When you designate a module adapter, a
 Default Module
 button is visible. Click
 Default Module
 when you want to specify the default module call for all steps you create with the step type. A sequence developer can change the module call after creating the step using the
 [Module](module-tab-step-settings-pane.html)
 tab of the
 [Step Settings](step-settings-pane.html)
 pane or in the
 [Specify Module](specify-module-tabs-and-dialog-boxes.html)
 dialog box of a user interface. 
 You can prevent the sequence developer from specifying a module for a step type by enabling the
 Specify Module
 option on the
 [Disable Properties](disable-properties-tab-step-type-properties-d.html)
 tab. For example, a sequence developer cannot specify a module for the Statement step type because Statement steps do not call code modules. 
 Note 
 If you want a step type to specify a call to a code module and you do not want the sequence developer to change or edit the module call, National Instruments recommends that you create a Post-Step
 [substep](substeps-tab-step-type-properties-dialog-box.html)
 instead of specifying a default adapter and code module. When you create this substep you typically do not specify a default adapter and code module for the step type and you enable the
 Specify Module
 option on the
 [Disable Properties](disable-properties-tab-step-type-properties-d.html)
 tab.
- Preconditions 
 —Launches the
 Preconditions 
 dialog box, in which you can specify the default conditions that must be
 True 
 for new steps of the step type to execute.

Click the
 Advanced
 button to launch a menu that contains the following options:

- Flags 
 —Launches the
 Edit Flags 
 dialog box, in which you can modify the property flags. Typically, you need to configure property flags only when you develop a relatively sophisticated custom step type.
- Attributes 
 —Launches the
 Attributes 
 dialog box, in which you can create and edit the default attributes for the steps you create with the step type.
- Block Structure 
 —Launches the
 Block Structure 
 dialog box, in which you can modify the block structure settings for steps you create with the step type. The
 Flow Control step types 
 , such as
 If 
 ,
 Else If 
 , and
 End 
 , use these built-in properties.
- Default Additional Results 
 —Launches the
 Configure Default Additional Results 
 dialog box, in which you can configure default additional results for the step. The step type must have a default module to configure default parameter additional results.
- Preconfigured Additional Results 
 —Launches the
 Configure Preconfigured Additional Results 
 dialog box, in which you can configure the additional results hints for the step type. The additional results hints define a list of preconfigured custom additional results you can choose to log when you edit the additional results of a step in a user interface.
- Attach to this File (If you do not attach the type, TestStand saves the type with the file only if this file contains instances of the type.) 
 —TestStand saves the type in the sequence file or type palette file regardless of whether the file contains any variables, parameters, or properties that use the type. This option applies only to the current file. When you create a new type in a file or copy an existing type from another file, TestStand automatically enables this option. When you copy a variable, parameter, or property that uses the type into another sequence file and the sequence file does not contain the type, TestStand automatically disables this option.
 Disable this option when you only want to save the type when the file that contains the type also contains a variable, parameter, or property that uses it. If you delete the variable, parameter, or property, TestStand does not delete the type. However, next time you save the file TestStand will not save the type.
- Comment 
 —The text that appears in the Comment field for the step type in the list view. TestStand copies the comment into each step you create with the step type. You can change the comment for each step after you create the step.

#### See Also

[Attributes dialog box](attributes-dialog-box.html)

[Block Structure dialog box](block-structure-dialog-box.html)

[Configure Default Additional Results dialog box](configure-default-additional-results-dialog-b.html)

[Configure Preconfigured Additional Results dialog box](configure-preconfigured-additional-results-di.html)

[Creating Custom Step Types](/csh?context=ts_tsfundamentals_custom_step_types_create)

[Edit Flags dialog box](edit-flags-dialog-box.html)

[Flow Control Step Types](flow-control-step-types.html)

[Module Tabs and Specify Module Dialog Boxes](specify-module-tabs-and-dialog-boxes.html)

[Preconditions dialog box](preconditions-dialog-box.html)

[Step Properties dialog box](step-properties-dialog-box.html)

[Step Settings Pane](step-settings-pane.html)

Parent topic:

Step Type Properties Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/general-tab-type-properties-dialog-box.html language=enus -->
## TOPIC 03758: General Tab - Type Properties Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/general-tab-type-properties-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/general-tab-type-properties-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: General Tab The General tab contains the following options: Value —The default value TestStand assigns to all variables, parameters, and properties you create with the data type. This value is the initial value for any newly created instances of the type or for instances of the type in which this pr

### General Tab - Type Properties Dialog Box

#### General Tab

The General tab contains the following options:

- Value 
 —The default value TestStand assigns to all variables, parameters, and properties you create with the data type. This value is the initial value for any newly created instances of the type or for instances of the type in which this property did not yet exist. You can change the value in each individual variable, parameter, or property after you create it. When an instance of a type contains this property, further changes to the value in the type definition do not affect the value in the instance unless you enable the
 Apply Value to All Loaded Instances of the Type 
 option and you have the file that contains the instance open when making the change.
- Release 
 —Sets the value of the object reference to
 Nothing 
 .
 Note 
 This option is available only when the type is object reference.
- Apply Value to All Loaded Instances of the Type 
 —Changes the values in all properties that are instances of the type for files currently in memory. Instances of the type in files not currently loaded are not updated. This option is available only when the property specifies a value.
- Attach to this File (If you do not attach the type, TestStand saves the type with the file only if this file contains instances of the type.) 
 —When you enable this option, TestStand saves the type in the sequence file or type palette file regardless of whether the file contains any variables, parameters, or properties that use the type. When you create a new type in a file or copy an existing type from another file, TestStand automatically enables this option. When you copy a variable, parameter, or property that uses the type into another sequence file or type palette file and the file does not contain the type, TestStand adds the type to the file, but does not enable this option. 
 Disable this option when you only want to save the type when the file that contains the type also contains a variable, parameter, or property that uses it. If you delete the variable, parameter, or property, TestStand does not delete the type. However, next time you save the file TestStand will not save the type.
 Note 
 This option does not appear when operating on the subproperty of a type and applies only to the current file.
- Numeric Format 
 —Launches the
 Numeric Format 
 dialog box, in which you can specify the format TestStand uses to display the value of a numeric property. This control is available only for numeric properties and numeric array properties.
- Comment 
 —The default comment TestStand assigns to all variables, parameters, and properties you create with the data type.
- Advanced 
 —Displays a submenu with the following options:
  - Flags 
 —Launches the
 Edit Flags 
 dialog box, in which you can modify the property flags for the data type.
  - Attributes 
 —Launches the
 Attributes 
 dialog box, in which you can create and edit the default attributes TestStand assigns to all variables, parameters, and properties you create with the data type.

#### See Also

[Attributes dialog box](attributes-dialog-box.html)

[Edit Flags dialog box](edit-flags-dialog-box.html)

[Numeric Format dialog box](numeric-format-dialog-box.html)

Parent topic:

Type Properties Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/general-tab-workspace-object-properties-dialo.html language=enus -->
## TOPIC 03759: General Tab - Workspace Object Properties Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/general-tab-workspace-object-properties-dialo.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/general-tab-workspace-object-properties-dialo.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: General Tab The General tab contains the following options: Path Name —The relative or absolute path of the file. Last Modified —The date and time the file was last modified on the local system. Project —The SCC provider project the file is associated with. Status —Indicates whether the file is chec

### General Tab - Workspace Object Properties Dialog Box

#### General Tab

The General tab contains the following options:

- Path Name 
 —The relative or absolute path of the file.
- Last Modified 
 —The date and time the file was last modified on the local system.
- Project 
 —The SCC provider project the file is associated with.
- Status 
 —Indicates whether the file is checked in or checked out of the SCC provider.
- Source Control Properties 
 —Launches an SCC provider dialog box, which contains the properties of the file.
- Requirements List 
 —Provides a mechanism for notating product and unit requirements the workspace or project covers. This control contains a list of strings where each string represents a single requirement. You can also notate requirements information in the
 Sequence File Properties 
 dialog box, the
 Sequence Properties 
 dialog box, the
 Step Settings 
 pane in the
 TestStand Sequence Editor 
 , or the
 Step Properties 
 dialog box from a
 TestStand User Interface 
 .
 Note 
 External requirements management packages, such as NI Requirements Gateway, define the format of the values that represent a requirement. A requirements management software package can use the TestStand API to retrieve or specify requirement values for workspace and project files using the
 [PropertyObjectFile](../tsapiref/propertyobjectfile.html)
 interface.

#### See Also

[PropertyObjectFile](../tsapiref/propertyobjectfile.html)

[Sequence File Properties dialog box](sequence-file-properties-dialog-box.html)

[Sequence Properties dialog box](sequence-properties-dialog-box.html)

[Step Properties dialog box](step-properties-dialog-box.html)

[Step Settings Pane](step-settings-pane.html)

Parent topic:

Workspace Object Properties Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/generate-report-dialog-box.html language=enus -->
## TOPIC 03760: Generate Report Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/generate-report-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/generate-report-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Click the Generate Report button on the TestStand File Diff and Merge utility toolbar or select File»Generate Report to launch the Generate Report dialog box, in which you can specify a file path for an XML that documents the differences found or merges performed in the specified files. You can also

### Generate Report Dialog Box

Click the
 Generate Report
 button on the
 [TestStand File Diff and Merge](teststand-file-diff-and-merge-utility.html)
 utility
 [toolbar](toolbar-buttons-and-shortcuts-teststand-file.html)
 or select
 File»Generate Report
 to launch the Generate Report dialog box, in which you can specify a file path for an XML that documents the differences found or merges performed in the specified files. You can also enter comments for the report itself or for each file you are comparing, including the final merged file. You can also specify how to view the report after it is generated.

The XML file uses the DifferStyleSheet.xslt style sheet located in the
 [<TestStand>](/csh?context=ts_tsfundamentals_directories)
 \Components\Stylesheets\FileDiffer
 directory. Use the
 [XML Packaging Utility](xml-packaging-utility.html)
 to package the files necessary to view the XML report on a computer that does not have TestStand installed.

The Generate Report dialog box contains the following options:

- Report Path 
 —File path of the report to create.
- Report Comments 
 —Comments for the complete report.
- Base File Comments 
 —Comments for the base file. This option is available only when you compare three files.
- File 1 Comments 
 —Comments for the first file.
- File 2 Comments 
 —Comments for the second file.
- Merged File Comments 
 —Comments for the final merged file. This option is available only when you compare three files.
- Launch Viewer When Done 
 —When you enable this option, the utility launches the report in the viewer application associated with the XML extension.

You must specify a report path before you can click the
 Save
 button.

#### See Also

[TestStand File Diff and Merge Utility](teststand-file-diff-and-merge-utility.html)

[XML Packaging Utility](xml-packaging-utility.html)

Parent topic:

TestStand File Diff and Merge Utility

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/generic-parameters-net-call-parameters.html language=enus -->
## TOPIC 03761: Generic Parameters - .NET Call Parameters

- bundle_id: `teststand-api-reference`
- source_path: `tsref/generic-parameters-net-call-parameters.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/generic-parameters-net-call-parameters.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Generic Parameters The .NET Adapter supports all fully-specified generic types that the public members of an assembly use. Thus, the adapter supports any generic type used as a parameter, return value, property, or field type in a public member. For example, you can call an assembly with a method th

### Generic Parameters - .NET Call Parameters

#### Generic Parameters

The .NET Adapter supports all fully-specified generic types that the public members of an assembly use. Thus, the adapter supports any generic type used as a parameter, return value, property, or field type in a public member. For example, you can call an assembly with a method that takes the
 List<Int32>
 type as a parameter and you can create instances of the type and call members on the type.

You can view the fully-specified generic types at the bottom of the Root Class list control on the
 [.NET Module](net-module-tab.html)
 tab.

#### See Also

[Edit .NET Call dialog box](edit-net-call-dialog-box.html)

[Mapping Parameters](/csh?context=ts_tsref_parameters)

[Step Settings Pane](step-settings-pane.html)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/get-error-info-operation-edit-ivi-tools-step.html language=enus -->
## TOPIC 03762: Get Error Info Operation - Edit IVI Tools Step Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/get-error-info-operation-edit-ivi-tools-step.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/get-error-info-operation-edit-ivi-tools-step.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Get Error Info Operation The Get Error Info operation returns error information for the last IVI error for a given IVI session. The operation retrieves and then clears the error information for the instrument session. The error information includes a primary error code, a secondary error code, and a

### Get Error Info Operation - Edit IVI Tools Step Dialog Box

#### Get Error Info Operation

The Get Error Info operation returns error information for the last IVI error for a given IVI session. The operation retrieves and then clears the error information for the instrument session. The error information includes a primary error code, a secondary error code, and an error elaboration string. The error information is the same as the values held in the following IVI attributes:

IVI_ATTR_PRIMARY_ERROR

IVI_ATTR_SECONDARY_ERROR

IVI_ATTR_ERROR_ELABORATION

The Get Error Info operation contains the following options:

- Primary Error Code 
 —A variable or property to which the step assigns a primary error code for the session or Execution thread. A value of
 VI_SUCCESS (0) 
 indicates no error occurred. A positive value indicates a warning. A negative value indicates an error.
- Secondary Error Code 
 —A variable or property to which the step assigns the secondary error code for the session or execution thread. If the primary error code is a nonzero value, the secondary error code can further describe the error or warning condition. A value of
 VI_SUCCESS (0) 
 indicates no further description.
- Error Elaboration 
 —A variable or property to which the step assigns the error elaboration string for the session or execution thread. If the primary error code is a nonzero value, the elaboration string can further describe the error or warning condition.

Parent topic:

Edit IVI Tools Step Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/get-information-operation-edit-ivi-dmm-step-d.html language=enus -->
## TOPIC 03763: Get Information Operation - Edit IVI Dmm Step Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/get-information-operation-edit-ivi-dmm-step-d.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/get-information-operation-edit-ivi-dmm-step-d.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Get Information Operation The Get Information operation retrieves low-level status and information from the DMM. This operation queries and retrieves the range value when the instrument is autoranging the aperture time and units. You must specify an expression that contains a variable or property to

### Get Information Operation - Edit IVI Dmm Step Dialog Box

#### Get Information Operation

The Get Information operation retrieves low-level status and information from the DMM. This operation queries and retrieves the range value when the instrument is autoranging the aperture time and units. You must specify an expression that contains a variable or property to which the step assigns the retrieved value.

The Get Information operation contains the following options:

- Get Auto Range Value 
 —A variable or property to which the step assigns the range value when the DMM is auto-ranging. When the Range Mode setting is set to Auto Range On, the Range setting does not accurately reflect the current range. If you are auto-ranging the DMM, use this control to retrieve the range to which the instrument has set itself.
- Get Aperture Time Info 
 —Returns information about the aperture time. This operation only works on instrument drivers that support the Device Info Ext extension.
  - Time 
 —A variable or property to which the step assigns the aperture time, also known as the integration time. The Units control returns units of aperture time.
  - Units 
 —A variable or property to which the step assigns the units of aperture time. A value of
 1 
 specifies the aperture time in powerline cycles. A value of
 0 
 specifies the aperture time, in seconds.

Parent topic:

Edit IVI Dmm Step Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/get-information-operation-edit-ivi-fgen-step.html language=enus -->
## TOPIC 03764: Get Information Operation - Edit IVI Fgen Step Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/get-information-operation-edit-ivi-fgen-step.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/get-information-operation-edit-ivi-fgen-step.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Get Information Operation The Get Information operation retrieves low-level status and information from the function generator. You can query the instrument for the maximum number of waveforms, the maximum and minimum waveform size, and the quantum value the function generator allows. You can query

### Get Information Operation - Edit IVI Fgen Step Dialog Box

#### Get Information Operation

The Get Information operation retrieves low-level status and information from the function generator. You can query the instrument for the maximum number of waveforms, the maximum and minimum waveform size, and the quantum value the function generator allows. You can query the instrument for the maximum loop count for sequences, the maximum number of sequences, and the maximum and minimum sequence length. You must specify an expression that contains a variable or property to which the step assigns the retrieved value.

The Get Information operation contains the following options:

- Get Max Num Waveforms 
 —A variable or property to which the step assigns the maximum number of arbitrary waveforms the function generator allows.
- Get Max Waveform Size 
 —A variable or property to which the step assigns the maximum number of points the function generator allows in an arbitrary waveform.
- Get Min Waveform Size 
 —A variable or property to which the step assigns the minimum number of points the function generator allows in an arbitrary waveform.
- Get Waveform Quantum 
 —A variable or property to which the step assigns the quantum value the function generator allows.
- Get Max Loop Count 
 —A variable or property to which the step assigns the maximum number of times the function generator can repeat an arbitrary waveform in a sequence.
- Get Max Num Sequences 
 —A variable or property to which the step assigns the maximum number of sequences the function generator allows.
- Get Max Sequence Length 
 —A variable or property to which the step assigns the maximum number of arbitrary waveforms the function generator allows in a sequence.
- Get Min Sequence Length 
 —A variable or property to which the step assigns the minimum number of arbitrary waveforms the function generator allows in a sequence.

Parent topic:

Edit IVI Fgen Step Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/get-information-operation-edit-ivi-scope-step.html language=enus -->
## TOPIC 03765: Get Information Operation - Edit IVI Scope Step Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/get-information-operation-edit-ivi-scope-step.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/get-information-operation-edit-ivi-scope-step.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Get Information Operation The Get Information operation retrieves low-level status and information from the function generator. You can query the instrument for the current sampling mode, the actual number of points the function generator acquires for each channel, the effective sample rate of the a

### Get Information Operation - Edit IVI Scope Step Dialog Box

#### Get Information Operation

The Get Information operation retrieves low-level status and information from the function generator. You can query the instrument for the current sampling mode, the actual number of points the function generator acquires for each channel, the effective sample rate of the acquired waveform using the current configuration in samples per second, and the probe attenuation value the function generator automatically senses. You can also determine whether an acquisition is in progress or complete. You must specify an expression that contains a variable or property to which the step assigns the retrieved value.

The Get Information operation contains the following options:

- Get Actual Record Length 
 —A variable or property to which the step assigns the actual number of points the oscilloscope acquires for each channel. After calling the Configure operation, call the Get Actual Record Length operation to determine the size of the waveforms the oscilloscope acquires with the Read or Fetch operations. The value is equal to or greater than the minimum number of points the Min Record Length setting specifies. The oscilloscope can use records of varying sizes depending on the acquisition type.
- Get Sample Rate 
 —A variable or property to which the step assigns the effective sample rate of the acquired waveform using the current configuration in samples per second.
- Get Sample Mode 
 —A variable or property to which the step assigns the current sampling mode for the oscilloscope.
 
 Supported Value
 DescriptionEquivalent Time (1)
 Specifies that the oscilloscope uses equivalent-time sampling.
 Real Time (0)
 Specifies that the oscilloscope uses real-time sampling.
- Get Acquisition Status 
 —A variable or property to which the step assigns a value that indicates if an acquisition is in progress, is complete, or if the status is unknown. Typically, this operation is only called in a sequence of calls to other low-level driver operations, such as the Initiate operation. If the driver cannot query the instrument to determine the state of the instrument, the operation returns Status Unknown.
 Note 
 This operation does not check the instrument status. 
 
 Supported Value
 DescriptionComplete (1)
 Specifies that the acquisition is complete.
 In Progress (0)
 Specifies that the acquisition is in progress.
 Status Unknown (-1)
 Specifies that the driver cannot query the instrument to determine the state of the instrument or that the status is unknown.
- Get Auto Probe Sense Value 
 —A variable or property to which the step assigns the probe attenuation value the oscilloscope automatically senses. After you attach the probe to a channel, the probe uses the returned value as the scaling factor for attenuating the input. When the auto probe sense capability is not enabled, this function returns the current manual probe attenuation setting.
  - Channel 
 —The channel name on which to perform the operation.
  - Value 
 —The property or variable name to which the step assigns the returned value.

Parent topic:

Edit IVI Scope Step Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/get-information-operation-ivi-switching-mode.html language=enus -->
## TOPIC 03766: Get Information Operation (IVI Switching Mode) - Edit IVI Switch Step Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/get-information-operation-ivi-switching-mode.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/get-information-operation-ivi-switching-mode.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Get Information Operation (IVI Switching Mode) Channel Info Tab You can retrieve specific information for specified channels using the Channel Info tab, which contains the following three controls for this purpose: Info 1, Info 2, and Info 3. The Channel Info tab also contains a listbox with a list

### Get Information Operation (IVI Switching Mode) - Edit IVI Switch Step Dialog Box

#### Get Information Operation (IVI Switching Mode)

#### Channel Info Tab

You can retrieve specific information for specified channels using the Channel Info tab, which contains the following three controls for this purpose: Info 1, Info 2, and Info 3.

The Channel Info tab also contains a listbox with a list of channels. Use the
 Add
 and
 Remove
 buttons to add new channels and remove existing channels form the list.

- Channel Name 
 —The name of a channel. The channel name must evaluate to be a valid virtual channel name as the IVI configuration tool for the logical name being used defines.

#### Info 1 Tab

The Info 1 tab of the Channel Info tab for the Get Information operation contains the following channel-specific options:

- Get Bandwidth 
 —A variable or property to which the step assigns the value that indicates the bandwidth of the channel, in hertz. The value is on a per-channel basis and may not take into account the other switches that make up a path to or from this channel.
- Get Characteristics Impedance 
 —A variable or property to which the step assigns the value that indicates the characteristic impedance of the channel, in ohms. The value is on a per-channel basis and may not take into account the other switches that make up a path to or from this channel.
- Get Max AC Voltage 
 —A variable or property to which the step assigns the value that indicates the maximum AC voltage, in volts RMS, the channel can handle. The value is on a per-channel basis and may not take into account the other switches that make up a path for this channel.
- Get Max Carry AC Current 
 —A variable or property to which the step assigns the value that indicates the maximum AC current, in amperes, the channel can carry. The value is on a per-channel basis and may not take into account the other switches that make up a path to or from this channel.
- Get Max Carry DC Current 
 —A variable or property to which the step assigns the value that indicates the maximum DC current, in amperes, the channel can carry. The value is on a per-channel basis and may not take into account the other switches that make up a path to or from this channel.

#### Info 2 Tab

The Info 2 tab of the Channel Info tab for the Get Information operation contains the following channel-specific options:

- Get Max Carry DC Power 
 —A variable or property to which the step assigns the value that indicates the maximum DC power, in Watts, the channel can handle. The value is on a per-channel basis and may not take into account the other switches that make up a path to or from this channel.
- Get Max DC Voltage 
 —A variable or property to which the step assigns the value that indicates the maximum DC voltage, in volts, the channel can handle. The value is on a per-channel basis and may not take into account the other switches that make up a path to or from this channel.
- Get Max Switching AC Current 
 —A variable or property to which the step assigns the value that indicates the maximum AC current, in amperes, the channel can switch. The value is on a per-channel basis and may not take into account the other switches that make up a path to or from this channel.
- Get Max Switching AC Power 
 —A variable or property to which the step assigns the value that indicates the maximum AC power, in volt-amperes, the channel can switch. The value is on a per-channel basis and may not take into account the other switches that make up a path for this channel.
- Get Max Switching DC Current 
 —A variable or property to which the step assigns the value that indicates the maximum DC current, in amperes, the channel can switch. The value is on a per-channel basis and may not take into account the other switches that make up a path to or from this channel.

#### Info 3 Tab

The Info 3 tab of the Channel Info tab for the Get Information operation contains the following channel-specific options:

- Get Max Switching DC Power 
 —A variable or property to which the step assigns the value that indicates the maximum DC power, in Watts, the channel can switch. The value is on a per-channel basis and may not take into account the other switches that make up a path to or from this channel.
- Get Settling Time 
 —A variable or property to which the step assigns the value that indicates the maximum total settling time, in seconds, for the channel before the signal going through it is considered stable. The returned value includes both the activation time for the channel as well as any debounce time. The value is on a per-channel basis and may not take into account the other switches make up a path to or from this channel.
- Get Wire Mode 
 —A variable or property to which the step assigns the value that indicates the number of conductors in the current channel. The value is on a per-channel basis and may not take into account the other switches that make up a path to or from this channel. For example, the return value is
 2 
 when the channel has two conductors.
- Is Configuration Channel 
 —A variable or property to which the step assigns a Boolean value that indicates whether the specific driver uses the channel for internal path creation. For example, if you specify a column-to-column connection in a matrix, the specific driver must typically use at least one row channel to make the connection.
- Is Source Channel 
 —A variable or property to which the step assigns the Boolean value that indicates whether the particular channel is a Source channel. If you attempt to connect two channels that are either sources or have their own connections to sources, the path creation operation returns an error. The term source can be from either the instrument or the UUT perspective. As a result, the driver must ensure with each connection that another connection within the switch module does not connect to another source. Defining a channel as a source prevents other channels from being connected that may cause damage to the channels, devices, or system.

Parent topic:

Get Information Operation (IVI Switching Mode) - Edit IVI Switch Step Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/get-information-operation-ivi-switching-mode2.html language=enus -->
## TOPIC 03767: Get Information Operation (IVI Switching Mode) - Edit IVI Switch Step Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/get-information-operation-ivi-switching-mode2.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/get-information-operation-ivi-switching-mode2.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Get Information Operation (IVI Switching Mode) Switch Info Tab The Switch Info tab for the Get Information operation contains the following options: Can Connect —Returns a value that indicates whether the switch module can create a given path without actually creating the path. Channel 1 —The end po

### Get Information Operation (IVI Switching Mode) - Edit IVI Switch Step Dialog Box

#### Get Information Operation (IVI Switching Mode)

#### Switch Info Tab

The Switch Info tab for the Get Information operation contains the following options:

- Can Connect 
 —Returns a value that indicates whether the switch module can create a given path without actually creating the path.
 
 The return value is valid at the time the step is called. You can make a successful connection when the Can Connect operation return value is
 Path Available 
 . Any other return value gives a reason why an attempt at a connection between the channels fails. If an implicit connection exists between the two specified channels, the Can Connect operation returns a warning that the connection already exists.
 
 Supported Value
 DescriptionChannel Not Available (6)
 Specifies that the driver cannot create a path between the two channels because one of the channels is a Configuration channel and thus unavailable for external connections.
 Path Available (1)
 Specifies that the driver can create a path at this time.
 Path Exists (2)
 Specifies that the explicit path between the channels already exists.
 Path Unsupported (3)
 Specifies that the instrument is not capable of creating a path between the two channels.
 Resource In Use (4)
 Specifies that, although the path is valid, the driver cannot create the path at this moment because the switch module is currently using one or more of the required channels to create another path. You must destroy the other path before you create this one.
 Source Conflict (5)
 Specifies that the instrument cannot create a path between the two channels because both are connected to a different source channel.
  - Channel 1 
 —The end points for the path you are creating.
  - Channel 2 
 —The end points for the path you are creating.
  - Destination 
 —A variable or property to which the step assigns the return value.
- Is Scanning 
 —A variable or property to which the step assigns the value that indicates whether the switch module is currently scanning through the scan list. Polling this function is one way to determine if the switch module scanning is complete. You can also use the Wait operation and enable the Wait For Scan Complete option, which blocks until the scan is complete. If the instrument is waiting for a trigger, TestStand returns a value of
 True 
 .
- Is Debounced 
 —A variable or property to which a step assigns the value that indicates whether or not all signals flowing through the switch have settled and whether it is safe to make a measurement at this time.
- Get Path 
 —Returns the list of connections, as comma-delimited channel pairs, established to connect the two given channels.
 
 Use the Get Path operation to understand the signal characteristics of the path and to provide an
 explicit path 
 for Set Path in the Configure Scan operation. The first and last names in the path are the channel names of the path and all others channels in the path are Configuration channels. The only valid paths that can be returned are those explicitly set using Set Path or a Connect/Disconnect operation. If no explicit path exists between the two specified channels, TestStand returns an error.
  - Channel 1 
 —The end points for the path you are trying to retrieve.
  - Channel 2 
 —The end points for the path you are trying to retrieve.
  - Destination 
 —A variable or property to which the step assigns the path.
- Get Number of Columns 
 —A variable or property to which a step assigns the value that indicates the maximum number of channels on the column of a matrix or scanner. If the switch module is a scanner, this value is the number of input channels. The number returned is dependent on the wire mode settings.
- Get Number of Rows 
 —A variable or property to which a step assigns the value that indicates the maximum number of channels on the row of a matrix or scanner. If the switch module is a scanner, this value is the number of output channels (commons) of the scanner. The number returned is dependent on the wire mode settings.

#### See Also

[Route Specification Strings](/csh?context=ts_tsref_route_spec_string)

Parent topic:

Get Information Operation (IVI Switching Mode) - Edit IVI Switch Step Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/get-information-operation-ivi-switching-mode3.html language=enus -->
## TOPIC 03768: Get Information Operation (IVI Switching Mode) - Edit IVI Switch Step Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/get-information-operation-ivi-switching-mode3.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/get-information-operation-ivi-switching-mode3.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Get Information Operation (IVI Switching Mode) The Get Information operation in IVI Switching mode retrieves low-level status and information from the instrument. You can also use the Get Information operation to acquire switch information and channel information. You must specify an expression that

### Get Information Operation (IVI Switching Mode) - Edit IVI Switch Step Dialog Box

#### Get Information Operation (IVI Switching Mode)

The Get Information operation in IVI Switching mode retrieves low-level status and information from the instrument. You can also use the Get Information operation to acquire switch information and channel information. You must specify an expression that contains a variable or property to which the step assigns the retrieved value.

The Edit IVI Switch Step dialog box for the Get Information operation in IVI Switching mode contains the following tabs:

- Switch Info Tab 
 —Specifies which information to retrieve from the switch module.
- Channel Info Tab 
 —Specifies which channel information to retrieve from the switch module.

Parent topic:

IVI Switching Mode - Edit IVI Switch Step Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/get-information-operation-switch-executive-mo.html language=enus -->
## TOPIC 03769: Get Information Operation (Switch Executive Mode) - Edit IVI Switch Step Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/get-information-operation-switch-executive-mo.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/get-information-operation-switch-executive-mo.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Get Information Operation (Switch Executive Mode) In Switch Executive mode, use the Get Information operation to find routes and determine whether the virtual device is debounced. You must specify an expression that contains a variable or property to which the step assigns the retrieved value. The F

### Get Information Operation (Switch Executive Mode) - Edit IVI Switch Step Dialog Box

#### Get Information Operation (Switch Executive Mode)

In Switch Executive mode, use the Get Information operation to find routes and determine whether the virtual device is debounced. You must specify an expression that contains a variable or property to which the step assigns the retrieved value.

The Find Route section in this dialog box takes two Endpoint channels as inputs and returns a route string and enumerated status value. The Channel 1 and Channel 2 controls specify the Endpoint channels to use when finding the route.

The Get Information operation contains the following options, which are located in the Find Route section:

- Channel 1 
 —Specifies one endpoint as input to find a route.
- Channel 2 
 —Specifies one endpoint as input to find a route.
- Destination 
 —A variable or property to which the step assigns the value that indicates the resulting route string. If a connection exists or if a connection can possibly be made between the two passed channels, the route string contains information that specifies the route.
- Status 
 —A variable or property to which the step assigns a status value.
 
 Supported Value
 DescriptionChannel Not Available (6)
 Specifies that the driver cannot create a path between the two channels because one of the channels is a Configuration channel and thus unavailable for external connections.
 Path Available (1)
 Specifies that the driver can create a path at this time.
 Path Exists (2)
 Specifies that the explicit path between the channels already exists.
 Path Unsupported (3)
 Specifies that the instrument is not capable of creating a path between the two channels.
 Resource In Use (4)
 Specifies that, although the path is valid, the driver cannot create the path at this moment because the switch module is currently using one or more of the required channels to create another path. You must destroy the other path before creating this one.
 Source Conflict (5)
 Specifies that the instrument cannot create a path between the two channels because both are connected to a different Source channel.
- Is Debounced 
 —A variable or property to which the step assigns the status of whether the switches are debounced.

Parent topic:

Switch Executive Mode - Edit IVI Switch Step Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/get-latest-version-dialog-box.html language=enus -->
## TOPIC 03770: Get Latest Version Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/get-latest-version-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/get-latest-version-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Select Get Latest Version from the Source Control menu or the Workspace context menu to launch the Get Latest Version dialog box, in which you can copy the latest version of the listed files in the workspace from source control to the local computer. The Get Latest Version dialog box contains the fo

### Get Latest Version Dialog Box

Select
 Get Latest Version
 from the Source Control menu or the Workspace context menu to launch the Get Latest Version dialog box, in which you can copy the latest version of the listed files in the workspace from source control to the local computer.

The Get Latest Version dialog box contains the following options:

- Files 
 —The list of files. You must check the files TestStand copies to the local computer.
- Select All 
 —Checks all the files displayed in the list control.
- Advanced 
 —Launches an SCC provider-specific dialog box, in which you can specify advanced source control options when getting the latest versions of files.

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/get-process-affinity-operation-cpu-affinity-s.html language=enus -->
## TOPIC 03771: Get Process Affinity Operation - CPU Affinity Step Configuration Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/get-process-affinity-operation-cpu-affinity-s.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/get-process-affinity-operation-cpu-affinity-s.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Get Process Affinity Operation Use the Get Process Affinity operation to obtain the current process affinity mask. This affinity mask represents the set of CPUs on which the process is allowed to run. Select the Get Process Affinity option on the CPU Affinity Step Configuration dialog box to display

### Get Process Affinity Operation - CPU Affinity Step Configuration Dialog Box

#### Get Process Affinity Operation

Use the Get Process Affinity operation to obtain the current process affinity mask. This affinity mask represents the set of CPUs on which the process is allowed to run. Select the
 Get Process Affinity
 option on the CPU Affinity Step Configuration dialog box to display the Get Process Affinity operation settings.

The Get Process Affinity operation contains the following option:

- Location to Store Process Affinity Mask (numeric value) 
 —The location to store a numeric value that is the affinity mask for the current process. The mask is represented as a numeric value. For example, a value of
 10 
 (
 0b00001010 
 ) represents CPUs 2 and 4 in a quad-core system.

#### See Also

[CPU Affinity Step Configuration dialog box](cpu-affinity-step-configuration-dialog-box.html)

[CPU Affinity step](cpu-affinity-step.html)

Parent topic:

CPU Affinity Step Configuration Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/get-process-affinity-operation.html language=enus -->
## TOPIC 03772: Get Process Affinity Operation

- bundle_id: `teststand-api-reference`
- source_path: `tsref/get-process-affinity-operation.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/get-process-affinity-operation.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Get Process Affinity Operation Use the Get Process Affinity operation to obtain the current process affinity mask. This affinity mask represents the set of CPUs on which the process is allowed to run. Select the Get Process Affinity option on the CPU Affinity edit tab to display the Get Process Affi

### Get Process Affinity Operation

#### Get Process Affinity Operation

Use the Get Process Affinity operation to obtain the current process affinity mask. This affinity mask represents the set of CPUs on which the process is allowed to run. Select the
 Get Process Affinity
 option on the CPU Affinity edit tab to display the Get Process Affinity operation settings.

The Get Process Affinity operation contains the following option:

- Location to Store Process Affinity Mask (numeric value) 
 —The location to store a numeric value that is the affinity mask for the current process. The mask is represented as a numeric value. For example, a value of
 10 
 (
 0b00001010 
 ) represents CPUs 2 and 4 in a quad-core system.

#### See Also

[CPU Affinity Step Configuration dialog box](cpu-affinity-step-configuration-dialog-box.html)

[CPU Affinity step](cpu-affinity-step.html)

Parent topic:

CPU Affinity Edit Tab

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/get-session-info-operation-edit-ivi-tools-ste.html language=enus -->
## TOPIC 03773: Get Session Info Operation - Edit IVI Tools Step Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/get-session-info-operation-edit-ivi-tools-ste.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/get-session-info-operation-edit-ivi-tools-ste.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Get Session Info Operation Use the Get Session Info operation to retrieve the low-level session manager instrument session as well as the API class handles and references to the IVI instrument. Do not pass an instrument handle between operating system processes because instrument driver handles you

### Get Session Info Operation - Edit IVI Tools Step Dialog Box

#### Get Session Info Operation

Use the Get Session Info operation to retrieve the low-level session manager instrument session as well as the API class handles and references to the IVI instrument.

Note

#### Get Session Info Operation

The Get Session Info operation contains the following options:

- Session Manager Reference 
 —A variable or property to which the step assigns a COM pointer to the
 InstrSession 
 object that session manager creates for the specified logical name. You can use an
 InstrSession 
 object to obtain an instrument API handle or reference.
- Class Driver C Handle 
 —A variable or property to which the step assigns the C-based class driver API handle for the specified logical name. You can use a class handle to control an instrument with an IVI class driver.
- Specific Driver C Handle 
 —A variable or property to which the step assigns the C-based specific driver API handle for the specified logical name. You can use a class handle to control an instrument independent of the IVI class driver.
- ActiveX Control Reference 
 —A variable or property to which the step assigns the COM pointer to the Measurement Studio for Visual Basic ActiveX control for the class the logical name specifies. You can use a control reference to interact with the instrument using the Measurement Studio COM interface.

#### See Also

[Session Manager Support for 64-bit TestStand](/csh?context=ts_tsfundamentals_64sessionmanager)

Parent topic:

Edit IVI Tools Step Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/get-status-operation-batch-settings-edit-tab.html language=enus -->
## TOPIC 03774: Get Status Operation - Batch Settings Edit Tab

- bundle_id: `teststand-api-reference`
- source_path: `tsref/get-status-operation-batch-settings-edit-tab.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/get-status-operation-batch-settings-edit-tab.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Get Status Operation Use the Get Status operation to obtain information about the current state of the batch. Enable the Get Status option on the left of the Batch Settings panel. The Get Status operation contains the following options: Batch Name or Reference Expression —The batch on which to perfo

### Get Status Operation - Batch Settings Edit Tab

#### Get Status Operation

Use the Get Status operation to obtain information about the current state of the batch. Enable the
 Get Status
 option on the left of the Batch Settings panel.

The Get Status operation contains the following options:

- Batch Name or Reference Expression 
 —The batch on which to perform the operation. You can specify the batch by name or by the object reference you receive when you create the batch using the Use Object Reference for the Batch Reference Lifetime option.
- Optional Output
  - Batch Exists? 
 —The location to store a Boolean value that indicates whether the batch already exists.
  - Number of Threads Waiting at Synchronized Sections 
 — The location to store a numeric value representing the number of threads waiting to enter or exit synchronized sections.
  - Number of Threads in Batch 
 —The location to store the numeric value that is the number of threads currently part of the batch.
  - Default Batch Synchronization 
 —The location to store a numeric value that specifies the default method of batch synchronization the batch uses.

Parent topic:

Batch Settings Edit Tab

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/get-status-operation-batch-specification-step.html language=enus -->
## TOPIC 03775: Get Status Operation - Batch Specification Step Configuration Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/get-status-operation-batch-specification-step.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/get-status-operation-batch-specification-step.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Get Status Operation Use the Get Status operation to obtain information about the current state of the batch. The Get Status operation contains the following options: Batch Name or Reference Expression —The batch on which to perform the operation. You can specify the batch by name or by the object r

### Get Status Operation - Batch Specification Step Configuration Dialog Box

#### Get Status Operation

Use the Get Status operation to obtain information about the current state of the batch.

The Get Status operation contains the following options:

- Batch Name or Reference Expression 
 —The batch on which to perform the operation. You can specify the batch by name or by the object reference you receive when you create the batch using the Use Object Reference for the Batch Reference Lifetime option.
- Batch Exists? (optional output) 
 —The location for storing a Boolean value that indicates whether the batch already exists.
- Number of Threads Waiting at Synchronized Sections (optional output) 
 —The location for storing a numeric value representing the number of threads waiting to enter or exit synchronized sections.
- Number of Threads in Batch (optional output) 
 —The location for storing the numeric value that is the number of threads currently part of the batch.
- Default Batch Synchronization (optional output) 
 —The location for storing a numeric value that specifies the default method of batch synchronization the batch uses.

Parent topic:

Batch Specification Step Configuration Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/get-status-operation-lock-settings-edit-tab.html language=enus -->
## TOPIC 03776: Get Status Operation - Lock Settings Edit Tab

- bundle_id: `teststand-api-reference`
- source_path: `tsref/get-status-operation-lock-settings-edit-tab.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/get-status-operation-lock-settings-edit-tab.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Get Status Operation Use the Get Status operation to obtain information about an existing lock or to determine whether a particular lock exists. Enable the Get Status option on the left of the Lock Settings panel. The Get Status operation contains the following options: Lock Name or Reference Expres

### Get Status Operation - Lock Settings Edit Tab

#### Get Status Operation

Use the Get Status operation to obtain information about an existing lock or to determine whether a particular lock exists. Enable the
 Get Status
 option on the left of the Lock Settings panel.

The Get Status operation contains the following options:

- Lock Name or Reference Expression 
 —The lock on which to perform the operation. You can specify the lock by name or by the object reference you receive when you create the lock using the Use Object Reference for the Lock Reference Lifetime option.
- Optional Output
  - Lock Exists? 
 —The location to store a Boolean value that indicates whether the lock exists.
  - Number of Threads Waiting to Lock the Lock 
 — A location to store the number of threads waiting to lock the lock.

Parent topic:

Lock Settings Edit Tab

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/get-status-operation-lock-step-configuration.html language=enus -->
## TOPIC 03777: Get Status Operation - Lock Step Configuration Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/get-status-operation-lock-step-configuration.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/get-status-operation-lock-step-configuration.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Get Status Operation Use the Get Status operation to obtain information about an existing lock or to determine whether a particular lock exists. Insert a Lock step and select Configure Lock from the context menu for the step. Select Get Status from the Operation ring control in the Lock Step Configu

### Get Status Operation - Lock Step Configuration Dialog Box

#### Get Status Operation

Use the Get Status operation to obtain information about an existing lock or to determine whether a particular lock exists. Insert a Lock step and select
 Configure Lock
 from the context menu for the step. Select
 Get Status
 from the Operation ring control in the Lock Step Configuration dialog box.

The Get Status operation contains the following options:

- Lock Name or Reference Expression 
 —The lock on which to perform the operation. You can specify the lock by name or by the object reference you receive when you create the lock using the Use Object Reference for the Lock Reference Lifetime option.
- Lock Exists? (optional output) 
 —The location for storing a Boolean value that indicates whether the lock exists.
- Number of Threads Waiting to Lock the Lock (optional output) 
 —The location for storing the number of threads waiting to lock the lock.

Parent topic:

Lock Step Configuration Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/get-status-operation-notification-settings-ed.html language=enus -->
## TOPIC 03778: Get Status Operation - Notification Settings Edit Tab

- bundle_id: `teststand-api-reference`
- source_path: `tsref/get-status-operation-notification-settings-ed.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/get-status-operation-notification-settings-ed.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Get Status Operation Use the Get Status operation to obtain information about the state of the Notification object. Enable the Get Status option on the left of the Notification Settings panel. The Get Status operation contains the following options: Notification Name or Reference Expression —The Syn

### Get Status Operation - Notification Settings Edit Tab

#### Get Status Operation

Use the Get Status operation to obtain information about the state of the Notification object. Enable the
 Get Status
 option on the left of the Notification Settings panel.

The Get Status operation contains the following options:

- Notification Name or Reference Expression 
 —The Synchronization object on which to perform the operation. You can specify the notification by name or by the object reference you receive when you create the notification using the Use Object Reference for the Notification Reference Lifetime option.
- Optional Output
  - Notification Exists? 
 —A location to store a Boolean value that indicates whether the Synchronization object exists.
  - Number of Threads Waiting for Notification 
 —A location to store a numeric value that corresponds to the number of threads waiting on the notification.
  - Is Set? 
 —The location for storing a Boolean value that indicates whether the notification is in a Set state.
  - Is Auto Clear? 
 —The location for storing a Boolean value that indicates whether the notification clears itself after one thread receives the notification. The value of this setting is only meaningful when the notification is in a Set state.
  - Location to Store Data (optional output) 
 — A location to store the notification data, if any. Leave this control blank when you do not want to store the data. The
 type of the location must be compatible 
 with the data the notification sends.

Parent topic:

Notification Settings Edit Tab

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/get-status-operation-notification-step-config.html language=enus -->
## TOPIC 03779: Get Status Operation - Notification Step Configuration Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/get-status-operation-notification-step-config.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/get-status-operation-notification-step-config.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Get Status Operation Use the Get Status operation to obtain information about the state of the Notification object. The Get Status operation contains the following options: Notification Name or Reference Expression —The Synchronization object on which to perform the operation. You can specify the no

### Get Status Operation - Notification Step Configuration Dialog Box

#### Get Status Operation

Use the Get Status operation to obtain information about the state of the Notification object.

The Get Status operation contains the following options:

- Notification Name or Reference Expression 
 —The Synchronization object on which to perform the operation. You can specify the notification by name or by the object reference you receive when you create the notification using the Use Object Reference for the Notification Reference Lifetime option.
- Notification Exists? (optional output) 
 —A location to store a Boolean value that indicates whether the Synchronization object exists.
- Number of Threads Waiting for Notification (optional output) 
 —A location to store a numeric value that corresponds to the number of threads waiting on the notification.
- Is Set 
 —A location to store a Boolean value that indicates whether the notification is in a Set state.
- Is Auto Clear (optional output) 
 —A location to store a Boolean value that indicates whether the notification clears itself after one thread receives the notification. The value of this setting is only meaningful when the notification is in a Set state.
- Location to Store Data (optional output) 
 — A location to store the notification data, if any. Leave this control blank when you do not want to store the data. The type of the
 location must be compatible with the data 
 the notification sends.

Parent topic:

Notification Step Configuration Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/get-status-operation-queue-settings-edit-tab.html language=enus -->
## TOPIC 03780: Get Status Operation - Queue Settings Edit Tab

- bundle_id: `teststand-api-reference`
- source_path: `tsref/get-status-operation-queue-settings-edit-tab.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/get-status-operation-queue-settings-edit-tab.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Get Status Operation Use the Get Status operation to obtain information about the current state of a queue. Enable the Get Status option on the left of the Queue Settings panel. The Get Status operation contains the following options: Queue Name or Reference Expression —The queue on which to perform

### Get Status Operation - Queue Settings Edit Tab

#### Get Status Operation

Use the Get Status operation to obtain information about the current state of a queue. Enable the
 Get Status
 option on the left of the Queue Settings panel.

The Get Status operation contains the following options:

- Queue Name or Reference Expression 
 —The queue on which to perform the operation. You can specify the queue by name or by the object reference you receive when you create the queue using the Use Object Reference for the Queue Reference Lifetime option.
- Optional Output
  - Queue Exists? 
 —The location to store a Boolean value that indicates whether the Synchronization object exists.
  - Number of Threads Waiting to Enqueue 
 —The location for storing the number of threads waiting to enqueue data.
  - Number of Threads Waiting to Dequeue 
 —The location for storing the number of threads waiting to dequeue data.
  - Maximum Number of Elements 
 —The location for storing the maximum number of elements of the queue.
  - Number of Elements 
 — The location for storing the number of elements in the queue.
  - Location to Store Array of Queue Elements 
 —An array property in which to store the elements of the queue. If you specify an array property in this control, all queue elements must be of the same data type as the array you specify, and no queue element can be an array. The step reports a run-time error if you specify a value in this control and the queue items do not meet these conditions.

Parent topic:

Queue Settings Edit Tab

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/get-status-operation-queue-step-configuration.html language=enus -->
## TOPIC 03781: Get Status Operation - Queue Step Configuration Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/get-status-operation-queue-step-configuration.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/get-status-operation-queue-step-configuration.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Get Status Operation Use the Get Status operation to obtain information about the current state of a queue. The Get Status operation contains the following options: Queue Name or Reference Expression —The queue on which to perform the operation. You can specify the queue by name or by the object ref

### Get Status Operation - Queue Step Configuration Dialog Box

#### Get Status Operation

Use the Get Status operation to obtain information about the current state of a queue.

The Get Status operation contains the following options:

- Queue Name or Reference Expression 
 —The queue on which to perform the operation. You can specify the queue by name or by the object reference you receive when you create the queue using the Use Object Reference for the Queue Reference Lifetime option.
- Queue Exists? (optional output) 
 —A location to store a Boolean value that indicates whether the Synchronization object exists.
- Number of Threads Waiting to Enqueue (optional output) 
 —The location for storing the number of threads waiting to enqueue data.
- Number of Threads Waiting to Dequeue (optional output) 
 —The location for storing the number of threads waiting to dequeue data.
- Maximum Number of Elements (optional output) 
 —The location for storing the maximum number of elements of the queue.
- Number of Elements (optional output) 
 —The location for storing the number of elements in the queue.
- Location to Store Array of Queue Elements (optional output) 
 —An array property in which to store the elements of the queue. If you specify an array property in this control, all queue elements must be of the same data type as the array you specify, and no queue element can be an array. The step reports a run-time error if you specify a value in this control and the queue items do not meet these conditions.

Parent topic:

Queue Step Configuration Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/get-status-operation-rendezvous-settings-edit.html language=enus -->
## TOPIC 03782: Get Status Operation - Rendezvous Settings Edit Tab

- bundle_id: `teststand-api-reference`
- source_path: `tsref/get-status-operation-rendezvous-settings-edit.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/get-status-operation-rendezvous-settings-edit.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Get Status Operation You can use the Get Status operation to obtain information about the current state of a rendezvous. enable the Get Status option on the left of the Rendezvous Settings panel. The Get Status operation contains the following options: Rendezvous Name or Reference Expression —The re

### Get Status Operation - Rendezvous Settings Edit Tab

#### Get Status Operation

You can use the Get Status operation to obtain information about the current state of a rendezvous. enable the
 Get Status
 option on the left of the Rendezvous Settings panel.

The Get Status operation contains the following options:

- Rendezvous Name or Reference Expression 
 —The rendezvous on which to perform the operation. You can specify the rendezvous by name or by the object reference you receive when you create the rendezvous using the Use Object Reference for the Rendezvous Reference Lifetime option.
- Optional Output
  - Rendezvous Exists? 
 —A location to store a Boolean value that indicates if the rendezvous exists.
  - Number of Threads Waiting for Rendezvous 
 —The location for storing the number of threads waiting on the rendezvous operation.
  - Number of Threads Per Rendezvous 
 —The location for storing the number of threads that must rendezvous before the step permits the threads to continue execution past the rendezvous point.

Parent topic:

Rendezvous Settings Edit Tab

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/get-status-operation-rendezvous-step-configur.html language=enus -->
## TOPIC 03783: Get Status Operation - Rendezvous Step Configuration Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/get-status-operation-rendezvous-step-configur.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/get-status-operation-rendezvous-step-configur.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Get Status Operation You can use the Get Status operation to obtain information about the current state of a rendezvous. The Get Status operation contains the following options: Rendezvous Name or Reference Expression —The rendezvous on which to perform the operation. You can specify the rendezvous

### Get Status Operation - Rendezvous Step Configuration Dialog Box

#### Get Status Operation

You can use the Get Status operation to obtain information about the current state of a rendezvous.

The Get Status operation contains the following options:

- Rendezvous Name or Reference Expression 
 —The rendezvous on which to perform the operation. You can specify the rendezvous by name or by the object reference you receive when you create the rendezvous using the Use Object Reference for the Rendezvous Reference Lifetime option.
- Rendezvous Exists? (optional output) 
 —The location for storing a Boolean value that indicates whether the rendezvous exists.
- Number of Threads Waiting for Rendezvous (optional output) 
 —The location for storing the number of threads waiting on the rendezvous operation.
- Number of Threads Per Rendezvous (optional output) 
 —The location for storing the number of threads that must rendezvous before the step permits the threads to continue execution past the rendezvous point.

Parent topic:

Rendezvous Step Configuration Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/get-status-operation-semaphore-settings-edit.html language=enus -->
## TOPIC 03784: Get Status Operation - Semaphore Settings Edit Tab

- bundle_id: `teststand-api-reference`
- source_path: `tsref/get-status-operation-semaphore-settings-edit.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/get-status-operation-semaphore-settings-edit.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Get Status Operation Use the Get Status operation to obtain information about the current state of the semaphore. Enable the Get Status option on the left of the Semaphore Settings panel. The Get Status operation contains the following options: Semaphore Name or Reference Expression —The semaphore o

### Get Status Operation - Semaphore Settings Edit Tab

#### Get Status Operation

Use the Get Status operation to obtain information about the current state of the semaphore. Enable the
 Get Status
 option on the left of the Semaphore Settings panel.

The Get Status operation contains the following options:

- Semaphore Name or Reference Expression 
 —The semaphore on which to perform the operation. You can specify the semaphore by name or by the object reference you receive when you create the semaphore using the Use Object Reference for the Semaphore Reference Lifetime option.
- Optional Output
  - Semaphore Exists? 
 —The location for storing a Boolean value that indicates whether the semaphore exists.
  - Number of Threads Waiting to Acquire the Semaphore 
 —The location for storing the number of threads waiting to acquire the semaphore.
  - Initial Semaphore Count 
 —The location for storing the initial semaphore count.
  - Current Count 
 —The location for storing the current value of the semaphore count.

Parent topic:

Semaphore Settings Edit Tab

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/get-status-operation-semaphore-step-configura.html language=enus -->
## TOPIC 03785: Get Status Operation - Semaphore Step Configuration Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/get-status-operation-semaphore-step-configura.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/get-status-operation-semaphore-step-configura.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Get Status Operation Use the Get Status operation to obtain information about the current state of the semaphore. The Get Status operation contains the following options: Semaphore Name or Reference Expression —The semaphore on which to perform the operation. You can specify the semaphore by name or

### Get Status Operation - Semaphore Step Configuration Dialog Box

#### Get Status Operation

Use the Get Status operation to obtain information about the current state of the semaphore.

The Get Status operation contains the following options:

- Semaphore Name or Reference Expression 
 —The semaphore on which to perform the operation. You can specify the semaphore by name or by the object reference you receive when you create the semaphore using the Use Object Reference for the Semaphore Reference Lifetime option.
- Semaphore Exists? (optional output) 
 —A location to store a Boolean value that indicates whether the semaphore exists.
- Number of Threads Waiting to Acquire the Semaphore (optional output) 
 —The location for storing the number of threads waiting to acquire the semaphore.
- Initial Semaphore Count (optional output) 
 —The location for storing the initial semaphore count.
- Current Count (optional output) 
 —The location for storing the current value of the semaphore count.

Parent topic:

Semaphore Step Configuration Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/get-system-affinity-operation-cpu-affinity-ed.html language=enus -->
## TOPIC 03786: Get System Affinity Operation -- CPU Affinity Edit Tab

- bundle_id: `teststand-api-reference`
- source_path: `tsref/get-system-affinity-operation-cpu-affinity-ed.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/get-system-affinity-operation-cpu-affinity-ed.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Get System Affinity Operation Use the Get System Affinity operation to obtain the default system affinity mask. This affinity mask represents the CPUs available to the system and cannot be changed. Select the Get System Affinity option on the CPU Affinity edit tab to display the Get Process Affinity

### Get System Affinity Operation -- CPU Affinity Edit Tab

#### Get System Affinity Operation

Use the Get System Affinity operation to obtain the default system affinity mask. This affinity mask represents the CPUs available to the system and cannot be changed. Select the
 Get System Affinity
 option on the CPU Affinity edit tab to display the Get Process Affinity operation settings.

The Get System Affinity operation contains the following option:

- Location to Store System Affinity Mask (numeric value) 
 —The location to store a numeric value that is the affinity mask for the system. The mask is represented as a numeric value. For example, a value of
 10 
 (
 0b00001010 
 ) represents CPUs 2 and 4 in a quad-core system.

#### See Also

[CPU Affinity Step Configuration dialog box](cpu-affinity-step-configuration-dialog-box.html)

[CPU Affinity step](cpu-affinity-step.html)

Parent topic:

CPU Affinity Edit Tab

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/get-system-affinity-operation-cpu-affinity-st.html language=enus -->
## TOPIC 03787: Get System Affinity Operation -- CPU Affinity Step Configuration Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/get-system-affinity-operation-cpu-affinity-st.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/get-system-affinity-operation-cpu-affinity-st.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Get System Affinity Operation Use the Get System Affinity operation to obtain the default system affinity mask. This affinity mask represents the CPUs available to the system and cannot be changed. Select the Get System Affinity option on the CPU Affinity Step Configuration dialog box to display the

### Get System Affinity Operation -- CPU Affinity Step Configuration Dialog Box

#### Get System Affinity Operation

Use the Get System Affinity operation to obtain the default system affinity mask. This affinity mask represents the CPUs available to the system and cannot be changed. Select the
 Get System Affinity
 option on the CPU Affinity Step Configuration dialog box to display the Get System Affinity operation settings.

The Get System Affinity operation contains the following option:

- Location to Store System Affinity Mask (numeric value) 
 —The location to store a numeric value that is the affinity mask for the system. The mask is represented as a numeric value. For example, a value of
 10 
 (
 0b00001010 
 ) represents CPUs 2 and 4 in a quad-core system.

#### See Also

[CPU Affinity Step Configuration dialog box](cpu-affinity-step-configuration-dialog-box.html)

[CPU Affinity step](cpu-affinity-step.html)

Parent topic:

CPU Affinity Step Configuration Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/get-thread-affinity-operation-cpu-affinity-ed.html language=enus -->
## TOPIC 03788: Get Thread Affinity Operation -- CPU Affinity Edit Tab

- bundle_id: `teststand-api-reference`
- source_path: `tsref/get-thread-affinity-operation-cpu-affinity-ed.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/get-thread-affinity-operation-cpu-affinity-ed.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Get Thread Affinity Operation Use the Get Thread Affinity operation to obtain the current thread affinity mask. This affinity mask represents the set of CPUs on which the thread is allowed to run. Select the Get Thread Affinity option on the CPU Affinity edit tab to display the Get Thread Affinity o

### Get Thread Affinity Operation -- CPU Affinity Edit Tab

#### Get Thread Affinity Operation

Use the Get Thread Affinity operation to obtain the current thread affinity mask. This affinity mask represents the set of CPUs on which the thread is allowed to run. Select the
 Get Thread Affinity
 option on the CPU Affinity edit tab to display the Get Thread Affinity operation settings.

The Get Thread Affinity operation contains the following option:

- Location to Store Thread Affinity Mask (numeric value) 
 —The location to store a numeric value that is the affinity mask for the current thread. The mask is represented as a numeric value. For example, a value of
 10 
 (
 0b00001010 
 ) represents CPUs 2 and 4 in a quad-core system.

#### See Also

[CPU Affinity Step Configuration dialog box](cpu-affinity-step-configuration-dialog-box.html)

[CPU Affinity step](cpu-affinity-step.html)

Parent topic:

CPU Affinity Edit Tab

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/get-thread-affinity-operation-cpu-affinity-st.html language=enus -->
## TOPIC 03789: Get Thread Affinity Operation -- CPU Affinity Step Configuration Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/get-thread-affinity-operation-cpu-affinity-st.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/get-thread-affinity-operation-cpu-affinity-st.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Get Thread Affinity Operation Use the Get Thread Affinity operation to obtain the current thread affinity mask. This affinity mask represents the set of CPUs on which the thread is allowed to run. Select the Get Thread Affinity option on the CPU Affinity Step Configuration dialog box to display the

### Get Thread Affinity Operation -- CPU Affinity Step Configuration Dialog Box

#### Get Thread Affinity Operation

Use the Get Thread Affinity operation to obtain the current thread affinity mask. This affinity mask represents the set of CPUs on which the thread is allowed to run. Select the
 Get Thread Affinity
 option on the CPU Affinity Step Configuration dialog box to display the Get Thread Affinity operation settings.

The Get Thread Affinity operation contains the following option:

- Location to Store Thread Affinity Mask (numeric value) 
 —The location to store a numeric value that is the affinity mask for the current thread. The mask is represented as a numeric value. For example, a value of
 10 
 (
 0b00001010 
 ) represents CPUs 2 and 4 in a quad-core system.

#### See Also

[CPU Affinity Step Configuration dialog box](cpu-affinity-step-configuration-dialog-box.html)

[CPU Affinity step](cpu-affinity-step.html)

Parent topic:

CPU Affinity Step Configuration Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/get-thread-priority-operation-thread-priority.html language=enus -->
## TOPIC 03790: Get Thread Priority Operation - Thread Priority Settings Edit Tab

- bundle_id: `teststand-api-reference`
- source_path: `tsref/get-thread-priority-operation-thread-priority.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/get-thread-priority-operation-thread-priority.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Get Thread Priority Operation Use the Get Thread Priority operation to obtain the current priority setting for the current thread. Enable the Get Priority option on the left of the Thread Priority Settings panel. The Get Thread Priority operation contains the following option: Location to Store Thre

### Get Thread Priority Operation - Thread Priority Settings Edit Tab

#### Get Thread Priority Operation

Use the Get Thread Priority operation to obtain the current priority setting for the current thread. Enable the
 Get Priority
 option on the left of the Thread Priority Settings panel.

The Get Thread Priority operation contains the following option:

- Location to Store Thread Priority (numeric value) 
 —The location for storing a numeric value that is the priority setting for the current thread. When you set the thread priority for a sequence, it is a good idea to save the previous priority in the Setup step group and restore the priority in the Cleanup step group.

Parent topic:

Thread Priority Settings Edit Tab

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/get-thread-priority-operation-thread-priority2.html language=enus -->
## TOPIC 03791: Get Thread Priority Operation - Thread Priority Configuration Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/get-thread-priority-operation-thread-priority2.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/get-thread-priority-operation-thread-priority2.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Get Thread Priority Operation Use the Get Thread Priority operation to obtain the current priority setting for the current thread. The Get Thread Priority operation contains the following option: Location to Store Thread Priority (numeric value) —The location for storing a numeric value that is the

### Get Thread Priority Operation - Thread Priority Configuration Dialog Box

#### Get Thread Priority Operation

Use the Get Thread Priority operation to obtain the current priority setting for the current thread.

The Get Thread Priority operation contains the following option:

- Location to Store Thread Priority (numeric value) 
 —The location for storing a numeric value that is the priority setting for the current thread. When you set the thread priority for a sequence, it is a good idea to save the previous priority in the Setup step group and restore the priority in the Cleanup step group.

Parent topic:

Thread Priority Configuration Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/git-pane.html language=enus -->
## TOPIC 03792: Git Pane

- bundle_id: `teststand-api-reference`
- source_path: `tsref/git-pane.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/git-pane.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: The Git pane in the TestStand Sequence Editor allows you to connect to Git repositories and perform the following version control operations: Account — Click the Account button to log in to a remote Git repository server. The login dialog lets you select which Git repository server you connect to. G

### Git Pane

The Git pane in the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 allows you to connect to Git repositories and perform the following version control operations:

- Account 
 — Click the
 Account 
 button to log in to a remote Git repository server. The login dialog lets you select which Git repository server you connect to.
- Git Config 
 — Click the
 Git Config 
 button to configure the username and email you use for Git commits.
- Tools 
 — Click the
 Tools 
 button to configure external tools used to compare and merge files for specific file extensions.

Git pane contains the following sections:

#### Git Repository

You can perform the following operations in the Git Repository section:

- Select a Git repository from among the list of Git repositories you opened from the Git pane. The list of Git repositories in the Repositories drop-down list is empty until you open a repository.
- Browse to a local system folder containing a Git repository.
- Clone a remote repository to a local system folder by providing the remote repository URL and the local folder path where the cloned repository should be created.
 Note 
 TestStand’s Git pane supports https URLs when cloning a remote repository.

#### Git Changes

You can perform the following actions in the Git Changes section:

- Fetch changes from a remote repository.
- Pull changes from a remote repository into your local repository.
- Push changes from your local repository to a remote repository.
- Select a Git branch from among the list of Git branches available from the selected Git repository.
- Create a new branch based on an existing branch.
- Commit changes to your local repository or Commit and Push changes to a remote repository.
 Note 
 You must provide a commit message before you can commit your changes.
- Merge another branch into the current branch.
- Abort an ongoing merge and revert to the state prior to the merge.
- View the file lists for changed files, files staged for commmit, or files unmerged due to merge conflicts.
- Compare changed files.
 Note 
 TestStand uses the application defined in Diff Tools for the corresponding file extension.
- Stage changes.
- Address file merge conflicts by accepting incoming changes, keeping the current file state, or using the merge tool defined for the file extension to manually merge changes between the two files.
- Discard changes in a file or unstage a staged file.
- Ignore a file by adding it to the .gitignore file, so that any changes to it are not considered as changes.

Notice

Git

Parent topic:

Panes

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/gll-source-code-files-dialog-box.html language=enus -->
## TOPIC 03793: GLL Source Code Files Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/gll-source-code-files-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/gll-source-code-files-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Click the GLL Source Code button on the LabVIEW NXG Module tab of the Step Settings pane to launch the GLL Source Code Files Dialog. This dialog is only available when configuring a LabVIEW NXG step using the LabVIEW NXG Runtime Engine. The dialog displays the Project Path currently configured for a

### GLL Source Code Files Dialog Box

Click the
 GLL Source Code
 button on the
 [LabVIEW NXG Module](labview-nxg-module-tab.html)
 tab of the Step Settings pane to launch the GLL Source Code Files Dialog. This dialog is only available when configuring a LabVIEW NXG step using the LabVIEW NXG Runtime Engine. The dialog displays the Project Path currently configured for a step. You can also choose the LabVIEW NXG project that contains the source files for the GLL currently selected in the step.

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/globals-context-menu.html language=enus -->
## TOPIC 03794: Globals Context Menu

- bundle_id: `teststand-api-reference`
- source_path: `tsref/globals-context-menu.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/globals-context-menu.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Globals Context Menu To access the Globals context menu, right-click a global variable, subproperty, or the background area of the window. The Globals context menu can contain the following items: Insert Station Global —A submenu from which you select the data type for the global variable you want t

### Globals Context Menu

#### Globals Context Menu

To access the Globals context menu, right-click a global variable, subproperty, or the background area of the window. The Globals context menu can contain the following items:

- Insert Station Global 
 —A submenu from which you select the
 data type 
 for the global variable you want to insert.
 If you want to insert a global variable with a custom data type, you must create a named data type first. You can create a named data type in the
 [Types](types-window.html)
 window. After you create the named data type, it appears in the Types submenu of the Insert Globals submenu.
- Cut 
 —Removes the selected variable and places it on the clipboard.
- Copy 
 —Copies the selected variable to the clipboard.
- Paste 
 —Inserts the variable from the clipboard.
- Delete 
 —Deletes the variable.
- Rename 
 —Displays a control for renaming the selected global variable or subproperty.
- Advanced 
 —Displays a submenu with the following items:
  - Edit Flags 
 —Launches the
 Edit Flags 
 dialog box, in which you can modify the flags for the global variable or subproperty.
  - Edit Attributes 
 —Launches the
 Attributes 
 dialog box, in which you can create and edit attributes for the global variable or subproperty.
- Reload Station Globals 
 —Discards the current station global variables and reloads the station global variables from disk. Use this command to discard edits you make to the station global variables. If you do not reload the station global variables, the edits are saved when you exit the
 TestStand Sequence Editor 
 .
 Note 
 You can only select this command when no executions are running.

#### See Also

[Attributes dialog box](attributes-dialog-box.html)

[Edit Flags dialog box](edit-flags-dialog-box.html)

[Types Window](types-window.html)

Parent topic:

Station Globals Window

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/goto-step.html language=enus -->
## TOPIC 03795: Goto Step

- bundle_id: `teststand-api-reference`
- source_path: `tsref/goto-step.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/goto-step.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use a Goto step to define the next step the TestStand Engine executes. You usually use a Label step as the target of a Goto step, which you can use to rearrange or delete other steps in a sequence without having to change the specification of targets in Goto steps. Configuring the Step Use the Desti

### Goto Step

Use a Goto step to define the next step the TestStand Engine executes. You usually use a
 [Label](label-step.html)
 step as the target of a Goto step, which you can use to rearrange or delete other steps in a sequence without having to change the specification of targets in Goto steps.

#### Configuring the Step

Use the
 [Destination](destination-edit-tab.html)
 edit tab in the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 and the
 [Edit Goto Step](edit-goto-step-dialog-box.html)
 dialog box in a
 [TestStand User Interface](teststand-user-interfaces.html)
 to specify the target for the Goto step. You cannot select an Else or Else If step as the target of a Goto Step.

#### Step Properties

The Goto step type does not define any additional step properties other than
 [custom properties common to all steps](/csh?context=ts_tsfundamentals_custom_result_props)
 .

#### See Also

[Flow Control Step Types](flow-control-step-types.html)

Parent topic:

Flow Control Step Types

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/help-menu-execution-profiler.html language=enus -->
## TOPIC 03796: Help Menu - Execution Profiler

- bundle_id: `teststand-api-reference`
- source_path: `tsref/help-menu-execution-profiler.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/help-menu-execution-profiler.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Help Menu The Help menu contains the following options. Help Overview —Displays this help file. Help Topic —Displays help for the active display.

### Help Menu - Execution Profiler

#### Help Menu

The Help menu contains the following options.

- Help Overview 
 —Displays this help file.
- Help Topic 
 —Displays help for the active display.

Parent topic:

Menus - Execution Profiler

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/help-menu.html language=enus -->
## TOPIC 03797: Help Menu

- bundle_id: `teststand-api-reference`
- source_path: `tsref/help-menu.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/help-menu.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: The Help menu in the TestStand Sequence Editor contains the following options: NI TestStand Help —Launches the NI TestStand Help . Help Topic —Displays the help topic for the item you currently have selected if help is available. Guide To Documentation —Displays the Guide to TestStand Documentation

### Help Menu

The Help menu in the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 contains the following options:

- NI TestStand Help 
 —Launches the
 NI TestStand Help 
 .
- Help Topic 
 —Displays the help topic for the item you currently have selected if help is available.
- Guide To Documentation 
 —Displays the
 Guide to TestStand Documentation 
 topic of the
 NI TestStand Help 
 .
- Getting Started 
 —Launches the
 Getting Started with TestStand 
 manual.
- Find Examples 
 —Displays the help topic for the
 NI TestStand Example Programs 
 .
- Check for Updates 
 —Launches the NI Update Service. This option is available only when you have installed the NI Update Service.
- Web Resources 
 —Takes you directly to the
 TestStand Support 
 page at
 ni.com 
 .
- Discussion Forum 
 —Takes you directly to the
 TestStand Discussion Forum 
 at
 ni.com 
 .
- Patents 
 —Displays National Instruments software-related patent information.
- About NI TestStand 
 —Displays the splash screen for the sequence editor, which contains version information and registration information for the application.

Parent topic:

Menus

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/help-menu2.html language=enus -->
## TOPIC 03798: Help Menu

- bundle_id: `teststand-api-reference`
- source_path: `tsref/help-menu2.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/help-menu2.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: The Help menu in a TestStand User Interface contains the following options: Menu items marked with an asterisk ( * ) appear only in Editor Mode. About this Application —Launches an About box with version information. NI TestStand Help* —Launches the NI TestStand Help . Help Topic —Displays the help

### Help Menu

TestStand User Interface

Note

*

- About this Application 
 —Launches an About box with version information.
- NI TestStand Help* 
 —Launches the
 NI TestStand Help 
 .
- Help Topic 
 —Displays the help topic for the item you currently have selected if help is available.
- Guide To Documentation* 
 —Displays the
 Guide to TestStand Documentation 
 topic of the
 NI TestStand Help 
 .
- Getting Started* 
 —Launches the
 Getting Started with TestStand 
 manual.
- Web Resources* 
 —Takes you directly to the
 TestStand Support 
 page at
 ni.com 
 .
- Discussion Forum* 
 —Takes you directly to the
 TestStand Discussion Forum 
 at
 ni.com 
 .
- Patents* 
 —Displays National Instruments software-related patent information.

Parent topic:

TestStand User Interface Menus and Tabs

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/hide-soft-front-panel-operation-edit-ivi-dmm.html language=enus -->
## TOPIC 03799: Hide Soft Front Panel Operation - Edit IVI Dmm Step Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/hide-soft-front-panel-operation-edit-ivi-dmm.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/hide-soft-front-panel-operation-edit-ivi-dmm.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Hide Soft Front Panel Operation Hides the soft front panel for the DMM. You can use the Show Soft Front Panel operation to display a hidden panel.

### Hide Soft Front Panel Operation - Edit IVI Dmm Step Dialog Box

#### Hide Soft Front Panel Operation

Hides the soft front panel for the DMM. You can use the Show Soft Front Panel operation to display a hidden panel.

Parent topic:

Edit IVI Dmm Step Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/hide-soft-front-panel-operation-edit-ivi-fgen.html language=enus -->
## TOPIC 03800: Hide Soft Front Panel Operation - Edit IVI Fgen Step Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/hide-soft-front-panel-operation-edit-ivi-fgen.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/hide-soft-front-panel-operation-edit-ivi-fgen.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Hide Soft Front Panel Operation Hides the soft front panel for the function generator. You can use the Show Soft Front Panel operation to display a hidden panel.

### Hide Soft Front Panel Operation - Edit IVI Fgen Step Dialog Box

#### Hide Soft Front Panel Operation

Hides the soft front panel for the function generator. You can use the Show Soft Front Panel operation to display a hidden panel.

Parent topic:

Edit IVI Fgen Step Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/hide-soft-front-panel-operation-edit-ivi-powe.html language=enus -->
## TOPIC 03801: Hide Soft Front Panel Operation - Edit IVI Power Supply Step Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/hide-soft-front-panel-operation-edit-ivi-powe.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/hide-soft-front-panel-operation-edit-ivi-powe.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Hide Soft Front Panel Operation Hides the soft front panel for the power supply. You can use the Show Soft Front Panel operation to display a hidden panel.

### Hide Soft Front Panel Operation - Edit IVI Power Supply Step Dialog Box

#### Hide Soft Front Panel Operation

Hides the soft front panel for the power supply. You can use the Show Soft Front Panel operation to display a hidden panel.

Parent topic:

Edit IVI Power Supply Step Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/hide-soft-front-panel-operation-edit-ivi-scop.html language=enus -->
## TOPIC 03802: Hide Soft Front Panel Operation - Edit IVI Scope Step Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/hide-soft-front-panel-operation-edit-ivi-scop.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/hide-soft-front-panel-operation-edit-ivi-scop.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Hide Soft Front Panel Operation Hides the soft front panel for the oscilloscope. You can use the Show Soft Front Panel operation to display a hidden panel.

### Hide Soft Front Panel Operation - Edit IVI Scope Step Dialog Box

#### Hide Soft Front Panel Operation

Hides the soft front panel for the oscilloscope. You can use the Show Soft Front Panel operation to display a hidden panel.

Parent topic:

Edit IVI Scope Step Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/hide-soft-front-panel-operation-edit-ivi-tool.html language=enus -->
## TOPIC 03803: Hide Soft Front Panel Operation - Edit IVI Tools Step Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/hide-soft-front-panel-operation-edit-ivi-tool.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/hide-soft-front-panel-operation-edit-ivi-tool.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Hide Soft Front Panel Operation Hides the soft front panel. You can use the Show Soft Front Panel operation to display a hidden panel.

### Hide Soft Front Panel Operation - Edit IVI Tools Step Dialog Box

#### Hide Soft Front Panel Operation

Hides the soft front panel. You can use the
 [Show Soft Front Panel](show-soft-front-panel-operation-edit-ivi-tool.html)
 operation to display a hidden panel.

Parent topic:

Edit IVI Tools Step Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/htbasic-adapter-configuration-dialog-box.html language=enus -->
## TOPIC 03804: HTBasic Adapter Configuration Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/htbasic-adapter-configuration-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/htbasic-adapter-configuration-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Select Configure»Adapters , select the HTBasic Adapter in the list control, and click Configure to launch the HTBasic Adapter Configuration dialog box. The HTBasic Adapter runs subroutines by communicating with a special program running in an HTBasic application called the HTBasic server. This serve

### HTBasic Adapter Configuration Dialog Box

Select
 Configure»Adapters
 , select the HTBasic Adapter in the list control, and click
 Configure
 to launch the HTBasic Adapter Configuration dialog box.

The HTBasic Adapter runs subroutines by communicating with a special program running in an HTBasic application called the HTBasic server. This server can be the HTBasic development version or the HTBasic run-time version. Specify which server the adapter uses by selecting the appropriate option in the HTBasic Server to Use section.

The HTBasic Adapter Configuration dialog box contains the following options:

- Use HTBasic Runtime server 
 —The location of the run-time version of the HTBasic server.
- Use HTBasic Development server 
 —The location of the development version of the HTBasic server.
- HTBasic Default Working Directory 
 —Specifies where the HTBasic Adapter sets the working directory before invoking a subroutine. This setting applies only to HTBasic steps that set the
 Working Directory 
 option for the step to
 Use adapter default 
 . The ring control contains the following four items:
 
 The default value is Subroutine file directory. The
 Browse 
 button and edit box are enabled only when you select the Use specified directory option.
  - Do not change working directory
  - HTBasic server directory
  - Subroutine file directory
  - Use specified directory

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/htbasic-module-tab.html language=enus -->
## TOPIC 03805: HTBasic Module Tab

- bundle_id: `teststand-api-reference`
- source_path: `tsref/htbasic-module-tab.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/htbasic-module-tab.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: To display the HTBasic Module tab in the TestStand Sequence Editor , insert a step configured to use the HTBasic Adapter and select Specify Module or Step Settings from the context menu. The HTBasic Module tab contains the following options: Subroutine File Pathname —The HTBasic program file that co

### HTBasic Module Tab

To display the HTBasic Module tab in the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 , insert a step configured to use the HTBasic Adapter and select
 Specify Module
 or
 Step Settings
 from the context menu.

The HTBasic Module tab contains the following options:

- Subroutine File Pathname 
 —The HTBasic program file that contains the subroutine the step calls. You can specify an absolute or relative path name for the HTBasic program file. Relative path names are relative to the TestStand
 search directory paths 
 . Use the
 Edit Search Directories 
 dialog box to customize the search directory paths.
 To load and call a subroutine, you must write the subroutine file to disk in the HTBasic application using the
 Store
 command instead of the
 Save
 command. HTBasic can only programmatically load and run stored subroutines.
- Subroutine Name 
 —The name of the subroutine the step calls. HTBasic requires that the subroutine name length cannot exceed 15 characters and the first character must be uppercase. The HTBasic adapter interprets the first character as uppercase even if you specify lowercase.
- Show HTBasic Application When Called 
 —When the HTBasic Adapter executes a step that calls an HTBasic subroutine, the HTBasic Adapter does not activate the HTBasic application. Enable this option when you want to activate the HTBasic application.
- HTBasic Working Directory 
 —The options for the HTBasic Adapter to set for the working directory of the HTBasic server before invoking the subroutine. Enable this option when the test code assumes a particular working directory path.
 The HTBasic Working Directory ring control contains the following five options: 
 
 The default value is Use adapter default. The
 Browse 
 button and edit box are available only when you select the Use specified directory option.
  - Use adapter default
  - Do not change working directory
  - HTBasic server directory
  - Subroutine file directory
  - Use specified directory

The following buttons are available only when you have installed an HTBasic development environment:

- Edit Subroutine 
 —Edits a subroutine that already exists.
- Create Subroutine 
 —Creates a code shell for a subroutine. If the HTBasic file you specify does not already exist, the HTBasic Adapter creates the file. If the file already exists, the HTBasic Adapter prompts you to replace the file. If the HTBasic code template file exists for the step type you selected for this step, the HTBasic Adapter uses the template to create the new subroutine.

#### See Also

[Edit Search Directories dialog box](edit-search-directories-dialog-box.html)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/i-o-controls-labview-nxg-vi-call-parameters.html language=enus -->
## TOPIC 03806: I/O Controls - LabVIEW NXG VI Call Parameters

- bundle_id: `teststand-api-reference`
- source_path: `tsref/i-o-controls-labview-nxg-vi-call-parameters.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/i-o-controls-labview-nxg-vi-call-parameters.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: I/O Controls Some of the LabVIEW NXG I/O controls are represented as clusters with two elements, DeviceName and SessionNumber. You can specify either a DeviceName or a SessionNumber. You can specify either a device name or a session number. The session number will always be used if it is not zero. T

### I/O Controls - LabVIEW NXG VI Call Parameters

#### I/O Controls

Some of the LabVIEW NXG I/O controls are represented as clusters with two elements, DeviceName and SessionNumber. You can specify either a DeviceName or a SessionNumber. You can specify either a device name or a session number. The session number will always be used if it is not zero. The session number can be used in other development environments, such as LabWindows/CVI, as long as they are in the same process. You can use the TestStand data type, LabVIEWIOControl, to create variables for I/O controls.

Note

0

0

0

The following I/O control references are represented this way:

- VISA
- IVI
- DAQmx Task Name
- DAQmx Channel Name

Parent topic:

LabVIEW NXG Data Types in TestStand

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/i-o-controls-labview-vi-call-parameters.html language=enus -->
## TOPIC 03807: I/O Controls - LabVIEW VI Call Parameters

- bundle_id: `teststand-api-reference`
- source_path: `tsref/i-o-controls-labview-vi-call-parameters.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/i-o-controls-labview-vi-call-parameters.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: I/O Controls Some of the LabVIEW I/O controls are represented as clusters with two elements, DeviceName and SessionNumber. You can specify either a device name or a session number. The session number will always be used if it is not zero. The session number can be used in other development environme

### I/O Controls - LabVIEW VI Call Parameters

#### I/O Controls

Some of the LabVIEW I/O controls are represented as clusters with two elements, DeviceName and SessionNumber. You can specify either a device name or a session number. The session number will always be used if it is not zero. The session number can be used in other development environments, such as LabWindows/CVI, as long as they are in the same process. You can use the TestStand data type, LabVIEWIOControl, to create variables for I/O controls.

Note

0

0

0

The following I/O control references are represented this way:

- VISA
- IVI
- FieldPoint
- Motion
- DAQmx Task Name
- DAQmx Channel Name

#### See Also

[LabVIEW Data Types in TestStand](/csh?context=ts_tsref_labview_data_types)

[Mapping Parameters](/csh?context=ts_tsref_parameters)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/identifier-for-teststand-steps-in-property-lo.html language=enus -->
## TOPIC 03808: Identifier for TestStand Steps in Property Loader Source

- bundle_id: `teststand-api-reference`
- source_path: `tsref/identifier-for-teststand-steps-in-property-lo.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/identifier-for-teststand-steps-in-property-lo.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: You can configure property loader to specify what to be used as the step identifier in property loader source during export and import. You can specify an expression to be used to calculate the identifier for a given TestStand step. The following table provides examples of different expressions that

### Identifier for TestStand Steps in Property Loader Source

You can configure property loader to specify what to be used as the step identifier in property loader source during export and import.

You can specify an expression to be used to calculate the identifier for a given TestStand step.

The following table provides examples of different expressions that specify how to identify TestStand steps.

| How to identify steps | Expression |
| --- | --- |
| StepName | Step.Name |
| TestStand’s unique step id | Step.TS.Id |
| Both step name and id | Step.Name + " (" + Step.TS.Id + ")" |
| Step Name without including spaces in the beginning or end | Trim(Step.Name) |
| Adding prefix “Step” to TestStand’s unique step id | “Step” + Step.TS.Id |

Note

Note

Parent topic:

Configuring a Property Loader Source

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/if-condition-edit-tab.html language=enus -->
## TOPIC 03809: If Condition Edit Tab

- bundle_id: `teststand-api-reference`
- source_path: `tsref/if-condition-edit-tab.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/if-condition-edit-tab.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the If Condition edit tab in the TestStand Sequence Editor to configure the If step. The If Condition edit tab contains the following options: Conditional Expression —The expression that must evaluate to True for the steps within the Else If block to execute. If the expression evaluates to False

### If Condition Edit Tab

Use the If Condition edit tab in the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 to configure the If step.

The If Condition edit tab contains the following options:

- Conditional Expression 
 —The expression that must evaluate to
 True 
 for the steps within the Else If block to execute. If the expression evaluates to
 False 
 , the execution proceeds to the next Else If, Else, or End step for the If block.
- Condition Builder 
 —Launches the
 Condition Builder 
 dialog box, which you can use to build conditional
 expressions 
 that refer to the execution statuses of other steps.

#### See Also

[Condition Builder dialog box](preconditions-dialog-box.html)

[Flow Control Step Types](flow-control-step-types.html)

Parent topic:

If Step

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/if-step.html language=enus -->
## TOPIC 03810: If Step

- bundle_id: `teststand-api-reference`
- source_path: `tsref/if-step.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/if-step.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use an If step to define a block of steps that execute if a condition is met. Configuring the Step Use the If Condition edit tab in the TestStand Sequence Editor and the Configure If Condition dialog box in a TestStand User Interface to configure the If step. Step Properties In addition to the commo

### If Step

Use an If step to define a block of steps that execute if a condition is met.

#### Configuring the Step

Use the
 [If Condition](if-condition-edit-tab.html)
 edit tab in the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 and the
 [Configure If Condition](configure-if-condition-dialog-box.html)
 dialog box in a
 [TestStand User Interface](teststand-user-interfaces.html)
 to configure the If step.

#### Step Properties

In addition to the
 [common custom properties](/csh?context=ts_tsfundamentals_custom_result_props)
 , the If step type defines the following step properties:

- Step.ConditionExpr 
 —The expression that must evaluate to
 True 
 for the steps within the If block to execute.

#### See Also

[Flow Control Step Types](flow-control-step-types.html)

Parent topic:

Flow Control Step Types

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/import-export-properties-dialog-box.html language=enus -->
## TOPIC 03811: Import/Export Properties Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/import-export-properties-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/import-export-properties-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Select Tools»Import/Export Properties to launch the Import/Export Properties dialog box, where you can import values from a property loader source or export values to a property loader source. When you edit a sequence file, you can import values from a database or file into step properties or variab

### Import/Export Properties Dialog Box

Select
 Tools»Import/Export Properties
 to launch the Import/Export Properties dialog box, where you can import
values from a property loader source or export values to a property loader source.

When you edit a sequence file, you can import values from a database or file into step properties or variables. You can also export values from step properties or variables to a database or file. The Import/Export Properties tool always uses the current sequence file open in the Sequence
Editor to perform the import/export operation.

When you are importing, the tool gives you the following options:

- Add 
 —Adds a new property loader source.
- Remove 
 —Removes the currently selected property loader source.
- Move Up 
 —Moves the currently selected property loader source up by one level.
- Move Down 
 —Moves the currently selected property loader source down by one level.

Note

The Import/Export Properties tool displays the following tabs, depending on whether you are performing an import or export operation:

- Import Options
- Export Options
- Property Selector

Click the
 Preview
 button to launch the Import Preview dialog box, which displays a
 [preview of the changes](previewing-your-imported-data.html)
 for the target sequence file.

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/import-export-properties-dialog-box2.html language=enus -->
## TOPIC 03812: Import/Export Properties Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/import-export-properties-dialog-box2.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/import-export-properties-dialog-box2.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Properties Tab The Properties tab for database locations contains the following options: Sequence —Selects the sequence to import values to or export values from. Step Name Column —The name of the column in the SQL statement that contains the names of the sequence steps and variable scopes that defi

### Import/Export Properties Dialog Box

#### Properties Tab

The Properties tab for database locations contains the following options:

- Sequence 
 —Selects the sequence to import values to or export values from.
- Step Name Column 
 —The name of the column in the SQL statement that contains the names of the sequence steps and variable scopes that define the rows of data. Click the
 Expression Browse 
 button to launch the
 Expression Browser 
 dialog box.
- Properties 
 —The names of the variables and properties to import or export. The Variables pane contains the properties and variables available in the selected sequence file and sequence. The Selected list control contains the properties and variables you select.
 Click the
 Limits
 button to add all limit properties to the Selected list control. 
 To add one or more properties to the Selected list control, select the properties in the Available Properties tree and click the single right arrow button (
 >
 ). Click the double right arrow button (
 >>
 ) to add all of the properties present in the Available Properties tree to the Selected list control. 
 To deselect one or more properties, select them in the Selected list control and click the single left arrow button (
 <
 ). Click the double left arrow button (
 <<
 ) to remove all of the properties in the Selected list control.
  - Property Name 
 —The currently selected property in the Selected list control. For array element properties, you must edit the property name to specify the array index. If you select a container or array property, TestStand stores the contents of the property as an XML stream.
  - Column Name/Number 
 —The name or number of the column where the step imports or exports the property.
- Append data type to column name 
 —When you enable this option, TestStand automatically appends the name of the data type for the property to the column name for a property when you select a property from the available list.
- Max size for column names 
 —The maximum number of characters for a column name. Many databases limit the size of a column name. Use the ring control to select the limits for the DBMS TestStand supports by default.
- Create Columns 
 —Launches the
 Create Columns 
 dialog box. TestStand automatically populates the dialog box with the list of any column names that you specify and the SQL statement does not return. You typically use the Create Columns dialog box to add new columns to a database table.

#### See Also

[Create Columns dialog box](create-columns-dialog-box.html)

[Expression Browser dialog box](expression-browser-dialog-box.html)

Parent topic:

Database Data Location - Legacy Import/Export Properties Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/import-export-properties-tool.html language=enus -->
## TOPIC 03813: Import/Export Properties Tool

- bundle_id: `teststand-api-reference`
- source_path: `tsref/import-export-properties-tool.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/import-export-properties-tool.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Import/Export Properties Tool Select Tools»Import/Export Properties to launch the Import/Export Properties dialog box, where you can import values from a property loader source or export values to a property loader source. When you edit a sequence file, you can import values from a database or file

### Import/Export Properties Tool

#### Import/Export Properties Tool

Select
 Tools»Import/Export Properties
 to launch the Import/Export Properties dialog box, where you can import
values from a property loader source or export values to a property loader source.

When you edit a sequence file, you can import values from a database or file into step properties or variables. You can also export values from step properties or variables to a database or file. The Import/Export Properties tool always uses the current sequence file open in the Sequence
Editor to perform the import/export operation.

When you are importing, the tool gives you the following options:

- Add 
 —Adds a new property loader source.
- Remove 
 —Removes the currently selected property loader source.
- Move Up 
 —Moves the currently selected property loader source up by one level.
- Move Down 
 —Moves the currently selected property loader source down by one level.

Note

The Import/Export Properties tool displays the following tabs, depending on whether you are performing an import or export operation:

- Import Options
- Export Options
- Property Selector

Click the
 Preview
 button to launch the Import Preview dialog box, which displays a
 [preview of the changes](previewing-your-imported-data.html)
 for the target sequence file.

Note

- No sequence is selected in the sequence list.
- The sequence file is locked and viewable.

Parent topic:

Property Loader Step

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/import-items-from-file-dialog-box.html language=enus -->
## TOPIC 03814: Import Items from File Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/import-items-from-file-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/import-items-from-file-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Click the Import button in the Configure Sequence Analyzer Available Rules dialog box to launch the Import Items from File dialog box, in which you import custom rules and analysis module specifications from a rules file to the computer. The Import Items from File dialog box contains the following i

### Import Items from File Dialog Box

Click the
 Import
 button in the
 [Configure Sequence Analyzer Available Rules](configure-sequence-analyzer-available-rules-d.html)
 dialog box to launch the Import Items from File dialog box, in which you import custom rules and analysis module specifications from a rules file to the computer.

The Import Items from File dialog box contains the following items:

- Select File to Import From 
 —Path of the rules file to use.
- Select Items to Import 
 —Lists the custom rules and analysis module specifications in the rules file that you can import.
- Import 
 —Imports the items you select from the rules file to the computer.

#### See Also

[Configure Sequence Analyzer Available Rules dialog box](configure-sequence-analyzer-available-rules-d.html)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/import-options-tab-import-export-properties-t.html language=enus -->
## TOPIC 03815: Import Options Tab - Import/Export Properties Tool

- bundle_id: `teststand-api-reference`
- source_path: `tsref/import-options-tab-import-export-properties-t.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/import-options-tab-import-export-properties-t.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Import Options Tab The Import Options tab contains the following options: Source Type —Specifies the type of the property loader source from which values are imported to TestStand properties. Source Location —Specifies location of the property loader source from which data will be imported to TestSt

### Import Options Tab - Import/Export Properties Tool

#### Import Options Tab

The Import Options tab contains the following options:

- Source Type 
 —Specifies the type of the property loader source from which values are
imported to TestStand properties.
- Source Location 
 —Specifies location of the property loader source from which data will be imported to TestStand properties. If the property loader source is a file, this field specifies the file path. If the property loader source is a database, this field specifies the connection string.
- Import Values To 
 —Specifies the target sequence to which values will be
imported. Use the provided dropdown to select the correct target sequence.
 Note 
 Select
 <Current Sequence>
 to import values to the current sequence and
 <All Sequences>
 imports values to all the sequences in the target sequence file.
- Import All Properties From Source 
 —When you enable this option, TestStand ignores the selected
property list and imports all properties from the property loader source.
- When Property Not Present In Source 
 —Specifies the action performed when a property is not
found in the source.
- When Property Not Present In Destination 
 —Specifies the action performed when a property is
not found in the sequence file.
 Note 
 ‘Create Property’ requires property loader source to have the type
information.
- Identify Steps By 
 —Specifies the lookup to uniquely identify a step in the
sequence file.
- Alias Location 
 —Specifies the location of the alias. If property loader source is file, this
specifies the location of alias file and if property loader source is database, this specifies the
name of the alias table.
- Import Preview 
 —Launches the Import Preview dialog box, which displays the
 preview of the
changes 
 for the target sequence file when performing an import from the current selected source.

Parent topic:

Import/Export Properties Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/import-options-tab-import-export-properties-t_2.html language=enus -->
## TOPIC 03816: Import Options Tab - Import/Export Properties Tool

- bundle_id: `teststand-api-reference`
- source_path: `tsref/import-options-tab-import-export-properties-t_2.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/import-options-tab-import-export-properties-t_2.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Import Options Tab The Import Options tab contains the following options: Source Type —Specifies the type of the property loader source from which values are imported to TestStand properties. Source Location —Specifies location of the property loader source from which data will be imported to TestSt

### Import Options Tab - Import/Export Properties Tool

#### Import Options Tab

The Import Options tab contains the following options:

- Source Type 
 —Specifies the type of the property loader source from which values are
imported to TestStand properties.
- Source Location 
 —Specifies location of the property loader source from which data will be imported to TestStand properties. If the property loader source is a file, this field specifies the file path. If the property loader source is a database, this field specifies the connection string.
- Import Values To 
 —Specifies the target sequence to which values will be
imported. Use the provided dropdown to select the correct target sequence.
 Note 
 Select
 <Current Sequence>
 to import values to the current sequence and
 <All Sequences>
 imports values to all the sequences in the target sequence file.
- Import All Properties From Source 
 —When you enable this option, TestStand ignores the selected
property list and imports all properties from the property loader source.
- When Property Not Present In Source 
 —Specifies the action performed when a property is not
found in the source.
- When Property Not Present In Destination 
 —Specifies the action performed when a property is
not found in the sequence file.
 Note 
 ‘Create Property’ requires property loader source to have the type
information.
- Identify Steps By 
 —Specifies the lookup to uniquely identify a step in the
sequence file.
- Alias Location 
 —Specifies the location of the alias. If property loader source is file, this
specifies the location of alias file and if property loader source is database, this specifies the
name of the alias table.
- Import Preview 
 —Launches the Import Preview dialog box, which displays the
 preview of the
changes 
 for the target sequence file when performing an import from the current selected source.

Parent topic:

Import/Export Properties Tool

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/import-prototype-from-csv-file-dialog-box.html language=enus -->
## TOPIC 03817: Import Prototype from CSV File Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/import-prototype-from-csv-file-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/import-prototype-from-csv-file-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: To launch the Import Prototype from CSV File dialog, navigate to the New CSV Input Stream edit tab or the Configure New CSV Input Stream dialog box and click Import Prototype. The Import Prototype from CSV File dialog shows a view of the CSV file specified in the step. Select the first line of the r

### Import Prototype from CSV File Dialog Box

To launch the Import Prototype from CSV File dialog, navigate to the
 [New CSV Input Stream edit tab](new-csv-input-record-stream-edit-tab.html)
 or the
 [Configure New CSV Input Stream dialog box](new-csv-input-record-stream-dialog-box.html)
 and click Import Prototype.

The Import Prototype from CSV File dialog shows a view of the CSV file specified in the step. Select the first line of the
 [record prototype](record-prototypes.html)
 in the file and click OK to import the prototype and close the dialog. TestStand creates subproperties in the container specified in the step for each field in the prototype specified in the file. Existing subproperties with names matching fields in the prototype are updated to match the prototype. Existing subproperties that do not correspond to fields in the prototype are retained or removed depending on the setting of the Allow Extra Fields in Record checkbox. If retained, the order and positions of extra fields within the container may change.

Parent topic:

New CSV Input Stream Step

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/import-update-automatic-properties-panel-type.html language=enus -->
## TOPIC 03818: Import/Update Automatic Properties Panel Types from .NET Assembly Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/import-update-automatic-properties-panel-type.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/import-update-automatic-properties-panel-type.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: In the Types window, right-click a Step Type containing a TS_AutoPropsStepSettings property, then click Import/Update AutoProps Types to launch the Import/Update Automatic Properties Panel Types from .NET Assembly dialog box. The dialog box contains the following options: .NET Assembly —The path of

### Import/Update Automatic Properties Panel Types from .NET Assembly Dialog Box

In the Types window, right-click a Step Type containing a
 TS_AutoPropsStepSettings
 property, then click
 Import/Update AutoProps Types
 to launch the Import/Update Automatic Properties Panel Types from .NET Assembly dialog box.

The dialog box contains the following options:

- .NET Assembly 
 —The path of the .NET assembly from which TestStand imports the Automatic Properties Panel types.
- Class 
 —The name of the class which implements the
 IAutoPropsPanel 
 interface. This class defines the Automatic Properties Panel structure to which TestStand imports the types.
- Prefix (Optional) 
 —Specifies the prefix to prepend to each type name.
- Import types into file 
 —Specifies the types file or sequence file to which TestStand imports the types when you click
 Import 
 .

Note

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/import-update-from-specification-compliance-m.html language=enus -->
## TOPIC 03819: Import/Update from Specification Compliance Manager (SCM) Tool

- bundle_id: `teststand-api-reference`
- source_path: `tsref/import-update-from-specification-compliance-m.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/import-update-from-specification-compliance-m.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Select Tools»Import/Update from Specification Compliance Manager (SCM) to launch the Manage Specifications dialog box, where you can import specifications from a product defined in the Specification Compliance Manager to a sequence. The Import/Update from Specification Compliance Manager (SCM) tool

### Import/Update from Specification Compliance Manager (SCM) Tool

Select
 Tools»Import/Update from Specification Compliance Manager (SCM)
 to launch the Manage Specifications dialog box, where you can import
specifications from a product defined in the Specification Compliance Manager to a sequence.

The Import/Update from Specification Compliance Manager (SCM) tool always imports to the current sequence file open in the Sequence Editor.

#### SCM Tool Dialog

#### OK Button

Saves the SCM configuration to the active sequene file. The button is enabled only after selecting one or more categories - see
 [Product Configuration View](product-configuration-view.html)
 .

#### Cancel Button

Exits the SCM configuration dialog, ignoring any changes made.

#### See Also

[Connection Configuration View](connection-configuration-view.html)

[View Differences Dialog](view-differences-dialog.html)

[Specification Compliance Manager Report Options Dialog Box](specification-compliance-manager-report-optio.html)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/incomplete-executions-dialog-box.html language=enus -->
## TOPIC 03820: Incomplete Executions Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/incomplete-executions-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/incomplete-executions-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: TestStand launches the Incomplete Executions dialog box when you attempt to shutdown while executions are running. The list control displays all incomplete executions. The Incomplete Executions dialog box contains the following controls: Terminate All —Initiates a terminate operation for all incompl

### Incomplete Executions Dialog Box

TestStand launches the Incomplete Executions dialog box when you attempt to shutdown while executions are running. The list control displays all incomplete executions.

The Incomplete Executions dialog box contains the following controls:

- Terminate All 
 —Initiates a terminate operation for all incomplete executions.
- Abort All 
 —Initiates an abort operation for all incomplete executions.
- Cancel 
 —Cancels the shutdown and leaves the executions running.

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/init-operation-edit-ivi-tools-step-dialog-box.html language=enus -->
## TOPIC 03821: Init Operation - Edit IVI Tools Step Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/init-operation-edit-ivi-tools-step-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/init-operation-edit-ivi-tools-step-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Init Operation The Init operation initializes a driver or I/O resource session for the specified logical name with the specified options. IVI steps automatically initialize an instrument session with default options for the specified logical name if a session for the logical name does not already ex

### Init Operation - Edit IVI Tools Step Dialog Box

#### Init Operation

The Init operation initializes a driver or I/O resource session for the specified logical name with the specified options.

IVI steps automatically initialize an instrument session with default options for the specified logical name if a session for the logical name does not already exist. IVI steps add a reference to the session for the current execution so that the instrument session remains open for the duration of the execution.

You typically use the Init operation only when you want to initialize a session with non-default options. If the session might have been previously initialized, specify
 Close and Init
 for the Reinitialization Action to ensure that TestStand applies the specified options.

The Init operation contains the following options:

- Perform Id Query 
 —When you enable this option, the Init operation performs an identification query on the instrument.
- Reset 
 —When you enable this option, the Init operation resets the instrument. The Reset operation places the instrument in a known state. For an IEEE 488.2 instrument, the Reset operation sends the command string
 "*RST" 
 to the instrument. Reset also sends the default setup commands to the instrument to configure settings for the proper operation of the instrument driver.
- Additional Initialization Options 
 —Additional options, separated by commas, that IVI supports.
Some examples include:
 Simulate=1 
 RangeCheck=1 
 QueryInstrStatus=1 
 Cache=1 
 RecordCoercions=1 
 InterchangeCheck=1 
 UseSpecificSimulation=1
- ReInitialization Action 
 —The behavior of the Init operation when you call Init on a previously-opened instrument session.
 
 Supported Value
 DescriptionLoop (0)
 Specifies that if an active session to the current logical name exists, calling Init has no effect.
 Close and Init (1)
 Specifies that if an active session to the current logical name exists, the session is closed and a new one is opened.
 Raise Error (2)
 Specifies that if an active session to the current logical name exists, calling Init causes an error.

Parent topic:

Edit IVI Tools Step Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/initiate-operation-edit-ivi-dmm-step-dialog-b.html language=enus -->
## TOPIC 03822: Initiate Operation - Edit IVI Dmm Step Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/initiate-operation-edit-ivi-dmm-step-dialog-b.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/initiate-operation-edit-ivi-dmm-step-dialog-b.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initiate Operation The Initiate operation initiates a measurement. When this operation executes, the DMM leaves the idle state and waits for a trigger. Use the Fetch operation to retrieve the measurement the Initiate operation starts. This operation does not check the instrument status. Typically, t

### Initiate Operation - Edit IVI Dmm Step Dialog Box

#### Initiate Operation

The Initiate operation initiates a measurement. When this operation executes, the DMM leaves the idle state and waits for a trigger. Use the
 [Fetch](fetch-operation-edit-ivi-scope-step-dialog-bo2.html)
 operation to retrieve the measurement the Initiate operation starts. This operation does not check the instrument status. Typically, this operation is only called in a sequence of calls to other low-level driver operations, such as the Fetch operation.

Parent topic:

Edit IVI Dmm Step Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/initiate-operation-edit-ivi-fgen-step-dialog.html language=enus -->
## TOPIC 03823: Initiate Operation - Edit IVI Fgen Step Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/initiate-operation-edit-ivi-fgen-step-dialog.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/initiate-operation-edit-ivi-fgen-step-dialog.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initiate Operation Initiates signal generation when the instrument is idle. When the function generator is in the idle state, this operation moves the function generator to the output generation state. When the function generator is already in the output generation state, this operation performs no

### Initiate Operation - Edit IVI Fgen Step Dialog Box

#### Initiate Operation

Initiates signal generation when the instrument is idle. When the function generator is in the idle state, this operation moves the function generator to the output generation state. When the function generator is already in the output generation state, this operation performs no action.

The instrument must be in the generation state after you call the Initiate operation. Also, you must be able to configure the output of the function generator regardless of whether the function generator is in the idle state or the generation state. You are only required to call the Initiate operation when you abort signal generation by calling the Abort operation.

Many function generators constantly generate an output signal and do not require you to initiate signal generation. If a function generator is always outputting the currently configured signal, this operation performs no action.

Some function generators require that you abort signal generation before configuring the instrument and initiate signal generation after configuring the instrument. The specific drivers for these types of instruments must compensate for this restriction and allow you to configure the instrument without requiring the user to call the
 [Abort](abort-operation-edit-ivi-fgen-step-dialog-box.html)
 and Initiate operations. These types of instruments often display a significant performance increase if you configure the output while the instrument is not generating a signal.

You are not required to call the Initiate and Abort operations. These operations have no impact on interchangeability. Use these operations to optimize the application for instruments that exhibit increased performance when output configuration is performed while the instrument is not generating a signal.

Parent topic:

Edit IVI Fgen Step Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/initiate-operation-edit-ivi-power-supply-step.html language=enus -->
## TOPIC 03824: Initiate Operation - Edit IVI Power Supply Step Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/initiate-operation-edit-ivi-power-supply-step.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/initiate-operation-edit-ivi-power-supply-step.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initiate Operation Directs the power supply to wait for a trigger. When the power supply is not currently waiting for a trigger, this operation causes the power supply to wait for a trigger. When the power supply is already waiting for a trigger, this operation performs no action.

### Initiate Operation - Edit IVI Power Supply Step Dialog Box

#### Initiate Operation

Directs the power supply to wait for a trigger. When the power supply is not currently waiting for a trigger, this operation causes the power supply to wait for a trigger. When the power supply is already waiting for a trigger, this operation performs no action.

Parent topic:

Edit IVI Power Supply Step Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/initiate-operation-edit-ivi-scope-step-dialog.html language=enus -->
## TOPIC 03825: Initiate Operation - Edit IVI Scope Step Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/initiate-operation-edit-ivi-scope-step-dialog.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/initiate-operation-edit-ivi-scope-step-dialog.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initiate Operation The Initiate operation initiates an acquisition. After calling this operation, the oscilloscope leaves the idle state and waits for a trigger. The oscilloscope acquires a waveform for each enabled channel. This operation does not check the instrument status. Typically, this operat

### Initiate Operation - Edit IVI Scope Step Dialog Box

#### Initiate Operation

The Initiate operation initiates an acquisition. After calling this operation, the oscilloscope leaves the idle state and waits for a trigger. The oscilloscope acquires a waveform for each enabled channel. This operation does not check the instrument status. Typically, this operation is only called in a sequence of calls to other low-level driver operations, such as the
 [Fetch](fetch-operation-edit-ivi-scope-step-dialog-bo2.html)
 operation.

Parent topic:

Edit IVI Scope Step Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/input-buffer-string-control.html language=enus -->
## TOPIC 03826: Input Buffer String Control

- bundle_id: `teststand-api-reference`
- source_path: `tsref/input-buffer-string-control.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/input-buffer-string-control.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Input Buffer string control to pass input data directly to the VI. The LabVIEW Adapter automatically copies the Step.InBuf property value into the Input Buffer string control when the property exists.

### Input Buffer String Control

Use the
 Input Buffer
 string control to pass input data directly to the VI. The LabVIEW Adapter automatically copies the
 Step.InBuf
 property value into the
 Input Buffer
 string control when the property exists.

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/input-tab-configure-sweep-loop-dialog-box.html language=enus -->
## TOPIC 03827: Input Tab - Configure Sweep Loop Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/input-tab-configure-sweep-loop-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/input-tab-configure-sweep-loop-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Input Tab Specifies the InputRecordStream or CSV file that provides values for sweep parameters using the Stream strategy . An input stream is not required if no parameters use the Stream strategy. When input is enabled, the Sweep Loop will advance the input stream one record at the beginning of eac

### Input Tab - Configure Sweep Loop Dialog Box

#### Input Tab

Specifies the
 [InputRecordStream](the-inputrecordstream-and-outputrecordstream.html)
 or CSV file that provides values for sweep parameters using the
 [Stream strategy](stream-sweep-parameter-strategy.html)
 . An input stream is not required if no parameters use the Stream strategy.

Note

The Input tab contains the following options:

- Enable Input 
 —Check this box to enable input for this loop. If checked, the input controls are enabled, and the Sweep Loop will read the next record from the specified
 InputRecordStream 
 or CSV file at the beginning of each iteration. Data from the stream will be stored to the locations specified for parameters using the Stream Strategy on the
 Sweep Parameters tab 
 .
- Specify file path by expression 
 —Check this box to choose the CSV File Path by entering an expression.
- Input via CSV 
 —Browse to and select the CSV file to read from.
  - CSV File Path 
 —Specify the CSV file path to read from.
  - Data Tag 
 —Specify a tag that defines the start location.
    - Ignore Case 
 —Select this checkbox to make comparisons case-insensitive for Data Tag.
- Skip lines 
 —Specify the number of lines to skip before reading. If both Data Tag and Skip Lines are provided, the tag is searched for first. When the tag is found, the specified number of lines are skipped. Reading continues from the next line in the CSV file.
- Separator Character 
 —Choose a separator character from the drop down menu.
- Input via Stream 
 —An object reference specifying the
 InputRecordStream 
 to read from.
- Auto Close 
 —Check this box to automatically clean up the input stream at the end of the loop. When this box is checked, upon terminating the loop, the Sweep Loop step closes the stream and sets the object reference in the
 InputRecordStream 
 expression to
 Nothing 
 .
 Note 
 Automatic cleanup only occurs if the loop terminates normally by completing its sweep or through a
 [Break step](break-step.html)
 . Cleanup does not occur if execution flow exits the loop for some other reason, such as through a
 [Goto step](goto-step.html)
 .

#### See Also

[Sweep Loop Step](sweep-loop-step.html)

[Sweep Loop Parameters Tab](sweep-parameters-tab-configure-sweep-loop-dia.html)

[Sweep Loop Output Tab](output-tab-configure-sweep-loop-dialog-box.html)

Parent topic:

Configure Sweep Loop Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/input-tab.html language=enus -->
## TOPIC 03828: Input Tab

- bundle_id: `teststand-api-reference`
- source_path: `tsref/input-tab.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/input-tab.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the InputRecordStream or CSV file that provides values for sweep parameters using the Stream strategy . An input stream is not required if no parameters use the Stream strategy. When input is enabled, the Sweep Loop will advance the input stream one record at the beginning of each iteratio

### Input Tab

InputRecordStream

Stream strategy

Note

The Input tab contains the following options:

- Enable Input 
 —Check this box to enable input for this loop. If checked, the input controls are enabled, and the Sweep Loop will read the next record from the specified
 InputRecordStream 
 or CSV file at the beginning of each iteration. Data from the stream will be stored to the locations specified for parameters using the Stream Strategy on the
 Sweep Parameters tab 
 .
- Specify file path by expression 
 —Check this box to choose the CSV File Path by entering an expression.
- Input via CSV 
 —Browse to and select the CSV file to read from.
  - CSV File Path 
 —Specify the CSV file path to read from.
  - Data Tag 
 —Specify a tag that defines the start location.
    - Ignore Case 
 —Select this checkbox to make comparisons case-insensitive for Data Tag.
  - Skip lines 
 —Specify the number of lines to skip before reading. If both Data Tag and Skip Lines are provided, the tag is searched for first. When the tag is found, the specified number of lines are skipped. Reading continues from the next line in the CSV file.
  - Separator Character 
 —Choose a separator character from the drop down menu.
- Input via Stream 
 —An object reference specifying the
 InputRecordStream 
 to read from.
- Auto Close 
 —Check this box to automatically clean up the input stream at the end of the loop. When this box is checked, upon terminating the loop, the Sweep Loop step closes the stream and sets the object reference in the
 InputRecordStream 
 expression to
 Nothing 
 .
 Note 
 Automatic cleanup only occurs if the loop terminates normally by completing its sweep or through a
 [Break step](break-step.html)
 . Cleanup does not occur if execution flow exits the loop for some other reason, such as through a
 [Goto step](goto-step.html)
 .

#### See Also

[Sweep Loop Step](sweep-loop-step.html)

[Sweep Loop Parameters Tab](sweep-parameters-tab.html)

[Sweep Loop Output Tab](output-tab.html)

Parent topic:

Sweep Loop Edit Tabs

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/insertion-palette-pane-sequence-file-tab.html language=enus -->
## TOPIC 03829: Insertion Palette Pane - Sequence File Tab

- bundle_id: `teststand-api-reference`
- source_path: `tsref/insertion-palette-pane-sequence-file-tab.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/insertion-palette-pane-sequence-file-tab.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Insertion Palette Pane The TestStand User Interfaces display items you can insert into sequence files on the Insertion Palette pane. The pane contains two lists: Step Types and Templates. The Step Types list displays the step type menu, and the Templates list displays user-defined template sequences

### Insertion Palette Pane - Sequence File Tab

#### Insertion Palette Pane

The
 [TestStand User Interfaces](teststand-user-interfaces.html)
 display items you can insert into sequence files on the Insertion Palette pane. The pane contains two lists: Step Types and Templates. The Step Types list displays the step type menu, and the Templates list displays user-defined template sequences, steps, and variables.

#### Step Types List

The Step Types list contains the step types from the loaded type palette files and from the active sequence file. Before you insert a step that can use any module adapter, such as the Action, Numeric Limit Test, Multiple Numeric Limit Test, String Value Test, and Pass/Fail Test step types, you must select an adapter by clicking on an adapter icon above the Step Types list. You can customize the structure of the Step Type list menu in the
 [Step Type Menu Editor](step-type-menu-editor-dialog-box.html)
 dialog box by selecting
 Customize
 from the context menu of the Step Types list. You can also specify which adapters are available using the
 [Adapter Configuration](adapter-configuration-dialog-box.html)
 dialog box. TestStand stores the settings for the Step Types list, including any customizations to the list of steps or available adapters, in the
 [<TestStand Application Data>](/csh?context=ts_tsfundamentals_directories)
 \Cfg\GeneralEngine.cfg
 file.

Note

GeneralEngine.cfg

custom TestStand User Interfaces

Steps

#### Templates List

Use the Templates list to hold copies of steps, variables, and sequences you reuse during the development of sequence files. For example, you can add a step that calls a specific LabVIEW VI you typically use, or a sequence that contains common setup steps, cleanup steps, and local variables.

Drag steps from the
 [Steps](steps-pane-sequence-file-tab.html)
 pane, variables from the
 [Variables](variables-pane-sequence-file-tab.html)
 pane, and sequences from the
 [Sequences](sequences-pane-sequence-file-tab.html)
 pane and drop them on the Templates list to add steps, variables, or sequences to the Templates list. Use the context menu to rename, copy, paste, delete, import, and export the items in the Templates list. Use drag and drop to rearrange the items in the list. Select
 Insert Folder
 from the context menu to add folders to the list. TestStand stores the settings for the Templates list, including any modifications to the list, in the
 [<TestStand Application Data>](/csh?context=ts_tsfundamentals_directories)
 \Cfg\Templates.ini
 file.

You must drag a sequence, step, or variable from the Templates list to a sequence file, make changes, drag the item back to the Templates list, and delete the original item from the Templates list to edit the item.

Step templates differ from
 [custom step types](/csh?context=ts_tsfundamentals_custom_step_types)
 , which have similar functionality but different use cases.

#### Inserting Sequences, Steps, and Variables

You can use one of the following operations to insert a step from the Step Types list to the Steps pane, or a sequence, step, and variable from the Templates list to the Sequences, Steps, and Variables panes:

- Double-click an item on the Insertion Palette pane. TestStand inserts the item above the current step, sequence, or variable depending on the type of the item.
- Select an item on the Insertion Palette pane and press <Enter>. TestStand inserts the item below the current step, sequence, or variable depending on the type of the item.
- Right-click an item on the Insertion Palette pane and select
 Insert 
 . TestStand inserts the item below the current step, sequence, or variable depending on the type of the item.
- Drag an item from the Insertion Palette pane and drop the item in the corresponding pane that contains a list of that type of items.

#### See Also

[Adapter Configuration dialog box](adapter-configuration-dialog-box.html)

[Sequences Pane](sequences-pane-sequence-file-tab.html)

[Step Type Menu Editor dialog box](step-type-menu-editor-dialog-box.html)

[Steps Pane](steps-pane-sequence-file-tab.html)

[Steps Pane Context Menu](steps-pane-context-menu-sequence-file-tab.html)

[Variables Pane](variables-pane-sequence-file-tab.html)

Parent topic:

Sequence File Tab

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/insertion-palette-pane.html language=enus -->
## TOPIC 03830: Insertion Palette Pane

- bundle_id: `teststand-api-reference`
- source_path: `tsref/insertion-palette-pane.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/insertion-palette-pane.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: The Insertion Palette pane in the TestStand Sequence Editor and the TestStand User Interface displays items you can insert into a sequence file. The pane contains a Step Types list, a Templates list, and an IO Configurations list. The Step Types list displays the step type menu, and the Templates li

### Insertion Palette Pane

TestStand Sequence Editor

TestStand User Interface

Note

#### Step Types List

The Step Types list contains the step types from the loaded type palette files specified in the
 [Types](types-window.html)
 window and from the active Sequence File window. Before you insert a step that can use any module adapter, such as the
 [Action](action-step.html)
 ,
 [Numeric Limit Test](numeric-limit-test-step.html)
 ,
 [Multiple Numeric Limit Test](multiple-numeric-limit-test-step.html)
 ,
 [String Value Test](string-value-test-step.html)
 , and
 [Pass/Fail Test](pass-fail-test-step.html)
 step types, you must select an adapter by clicking on an adapter icon above the Step Types list. You can customize the structure of the Step Type list menu in the
 [Step Type Menu Editor](step-type-menu-editor-dialog-box.html)
 dialog box by selecting
 Customize
 from the context menu of the Step Types list. You can also specify which adapters are available using the
 [Adapter Configuration](adapter-configuration-dialog-box.html)
 dialog box. TestStand stores the settings for the Step Types list, including any customizations to the list of steps or available adapters, in the
 [<TestStand Application Data>](/csh?context=ts_tsfundamentals_directories)
 \Cfg\GeneralEngine.cfg
 file.

Note

GeneralEngine.cfg

TestStand Sequence Editor

custom TestStand User Interfaces

Steps

#### Templates List

Use the Templates list to hold copies of steps, variables, and sequences you reuse during the development of sequence files. For example, you can add a step that calls a specific LabVIEW VI you typically use or a sequence that contains common setup steps, cleanup steps, and local variables.

Drag steps from the
 [Steps](steps-pane-sequence-file-window.html)
 pane, variables from the
 [Variables](variables-pane-sequence-file-window4.html)
 pane, and sequences from the
 [Sequences](sequences-pane-sequence-file-window.html)
 pane and drop them on the Templates list to add steps, variables, or sequences to the Templates list. Use the context menu to rename, copy, paste, delete, import, and export the items in the Templates list. You can drag and drop items to rearrange the list. Select
 Insert Folder
 from the context menu to add folders to the list. TestStand stores the settings for the Templates list, including any modifications to the list, in the
 [<TestStand Application Data>](/csh?context=ts_tsfundamentals_directories)
 \Cfg\Templates.ini
 file.

You must drag a sequence, step, or variable from the Templates list to a sequence file, make changes, drag the item back to the Templates list, and delete the original item from the Templates list to edit the item.

Step templates differ from
 [custom step types](/csh?context=ts_tsfundamentals_custom_step_types)
 , which have similar functionality but different use cases.

#### IO Configurations List

The IO Configurations list contains the exported IO Configuration files that are present in the
 %public%\Documents\National Instruments\TestStand\Shared\IO Configurations\
 folder. For any IO Configuration file, you can see all the IO sessions defined in it by clicking
 Expand
 . The IO Configurations list reflects the state of the folder. For example, when you add a new IO Configuration file to the folder, the IO Configurations list updates to include the new file. If you delete an existing IO Configuration file from the folder, the IO Configurations list updates to remove the IO Configuration. Renaming an IO configuration within the IO Configurations list renames the file in the folder.

#### Using an IO Configuration

You can perform the following operations on an IO Configuration in the IO Configurations list:

- Delete 
 —You can delete any configuration listed in the IO Configurations list by selecting the configuration and then clicking
 Delete 
 or by using the context menu. Deleting an IO Configuration from IO Configurations list will also delete the corresponding file from
 %public%\Documents\National Instruments\TestStand\Shared\IO Configurations 
 folder. However, you cannot delete IO sessions defined in a specific IO Configuration.
 Note 
 You cannot undo the delete operation.
- Rename 
 —You can rename IO Configurations in the IO Configurations list by selecting the Configuration and then pressing <F2> or by using the context menu. Once you rename a particular IO configuration, the name updates in the IO Configurations list and the file on disk is renamed.
- Edit 
 —You can edit an IO Configuration by using the context menu. After you edit a configuration, TestStand launches the editor with the specific IO Configuration.
 Note 
 InstrumentStudio 2019 is the only supported editor in TestStand 2019.
- View Details 
 —You can see additional information about a configuration or session by hovering over a specific IO Configuration in the Configurations View or by using the context menu and clicking
 View Detail 
 . The IO Configuration dialog opens and displays detailed information about the configuration.
- Use in a TestStand Sequence File 
 —You can use one of the following operations to to create new hardware sessions associated with an IO configuration, apply an IO configuration to an existing IO session, sweep on IO session attributes, and close all IO sessions opened:
  - Double-click an IO Configuration in the IO Configurations list. TestStand inserts a new Create Sessions and Apply Configuration step. When initialized, the new step uses a copy of all the IO Configurations you select.
  - Select IO Configuration item(s) on the IO Configurations list and press <Enter>. TestStand inserts a new Create Sessions and Apply Configuration step. When initialized, the new step uses a copy of all the IO Configurations you select.
  - Right-click an IO Configuration item on the IO Configurations list and select
 Insert 
 . TestStand inserts a new Create Sessions and Apply Configuration step. When initialized, the new step uses a copy of all the IO Configurations you select.
  - Drag an IO Configuration item from the IO Configurations list and drop the item in the steps view. TestStand inserts a new Create Sessions and Apply Configuration step. When initialized, the new step uses a copy of all the IO Configurations you select.

#### Inserting Sequences, Steps, and Variables

You can use one of the following operations to insert a step from the Step Types list to the Steps pane, or a sequence, step, and variable from the Templates list to the Sequences, Steps, and Variables panes:

- Double-click an item on the Insertion Palette pane. TestStand inserts the item above the current step, sequence, or variable depending on the type of the item.
- Select an item on the Insertion Palette pane and press <Enter>. TestStand inserts the item below the current step, sequence, or variable depending on the type of the item.
- Right-click an item on the Insertion Palette pane and select
 Insert 
 . TestStand inserts the item below the current step, sequence, or variable depending on the type of the item.
- Drag an item from the Insertion Palette pane and drop the item in the corresponding pane that contains a list of that type of items.

#### See Also

[Adapter Configuration dialog box](adapter-configuration-dialog-box.html)

[Sequences Pane](sequences-pane-sequence-file-window.html)

[Step Type Menu Editor dialog box](step-type-menu-editor-dialog-box.html)

[Steps Pane](steps-pane-sequence-file-window.html)

[Steps Pane Context Menu](steps-pane-context-menu-sequence-file-window.html)

[Types Window](types-window.html)

[Variables Pane](variables-pane-sequence-file-window4.html)

Parent topic:

Panes

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/installation-destination-options-distributed.html language=enus -->
## TOPIC 03831: Installation Destination Options - Distributed Files Tab - TestStand Deployment Utility

- bundle_id: `teststand-api-reference`
- source_path: `tsref/installation-destination-options-distributed.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/installation-destination-options-distributed.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Distributed Files Tab Installation Destination Options The following table lists the options available in the Installation Destination ring control on the Distributed Files tab of the TestStand Deployment Utility . The table maps each option to a complete directory path on the target system for Micr

### Installation Destination Options - Distributed Files Tab - TestStand Deployment Utility

#### Distributed Files Tab

#### Installation Destination Options

The following table lists the options available in the Installation Destination ring control on the
 [Distributed Files](distributed-files-tab-teststand-deployment-ut.html)
 tab of the
 [TestStand Deployment Utility](teststand-deployment-utility.html)
 . The table maps each option to a complete directory path on the target system for Microsoft Windows 10/8.1/7.

Note

user

Note

| Installation Destination Option | Windows Directory Path on Target System |
| --- | --- |
| Installation Directory* | The directory the Installer Directory option on the Installer Options tab of the TestStand Deployment Utility defines. |
| TestStand Directory | <TestStand> |
| Windows Directory* | C:\\Windows |
| Windows System Directory* | C:\\Windows\\system (64-bit TestStand) Not Applicable |
| Windows System32 Directory | C:\\Windows\\System32 (64-bit TestStand) 64-bit operating system directory Note 32-bit files using this destination are installed to the C:\\Windows\\SysWOW64 directory when deployed to a computer using a 64-bit operating system. |
| Program Files Directory | C:\\<Program Files> Note 32-bit files using this destination are installed to the C:\\Program Files (x86) directory when deployed to a computer using a 64-bit operating system. |
| Start Menu Programs Directory* | C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs |
| Startup Directory | C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Startup |
| Desktop Directory | C:\\Users\\< user >\\Desktop |
| Personal Directory | C:\\Users\\< user >\\Documents |
| Temp Directory* | C:\\Users\\< user >\\AppData\\Local\\Temp |
| National Instruments Directory | C:\\<Program Files>\\National Instruments |
| TestStand Public Documents Directory | <TestStand Public> If you specify an environment file and select the Determine File Destinations Using Environment File option, TestStand uses the specified environment file to determine the path for this destination. |
| TestStand Application Data Directory | <TestStand Application Data> If you specify an environment file and select the Determine File Destinations Using Environment File option, TestStand uses the specified environment file to determine the path for this destination. |
| (64-bit TestStand only) System WOW64 Directory* | C:\\Windows\\SysWOW64 (32-bit operating system directory) |
| National Instruments Public Directory | C:\\<ProgramData>\\National Instruments This directory is the parent of the <TestStand Public> directory. |
| Global TestStand Application Data Directory | <TestStand Application Data> This destination is available only if you enable the Determine File Destinations Using Environment File option. Use this option to deploy files to the default TestStand configuration directory, even when using an environment file, to determine file destinations. |

#### See Also

[Deploying TestStand Systems](/csh?context=ts_10203)

Parent topic:

Distributed Files Tab - TestStand Deployment Utility

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/installer-cache-dialog-box.html language=enus -->
## TOPIC 03832: Installer Cache Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/installer-cache-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/installer-cache-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Enable the Prompt Before Copying Installers to Product Cache option on the System Source tab of the TestStand Deployment Utility , enable the Install TestStand Runtime option on the Installer Options tab, and click Build to launch the Installer Cache dialog box. When the deployment utility builds an

### Installer Cache Dialog Box

Enable the
 Prompt Before Copying Installers to Product Cache
 option on the
 [System Source](system-source-tab-teststand-deployment-utilit.html)
 tab of the
 [TestStand Deployment Utility](teststand-deployment-utility.html)
 , enable the
 Install TestStand Runtime
 option on the
 [Installer Options](installer-options-tab-teststand-deployment-ut.html)
 tab, and click
 Build
 to launch the Installer Cache dialog box.

When the deployment utility builds an installer that contains National Instruments components or drivers it might create a local copy in the
 C:\ProgramData\NI Parts
 directory on Windows 10/8.1/7.

This optimization improves the speed when you create installers and eliminates the need to insert DVDs or CDs that contain the drivers. However, when you use this optimization you increase the amount of disk space needed because you must store the drivers on the local hard disk.

Use this dialog box to select which National Instruments Installers are copied to the local cache. Any installers you select are copied to the local hard disk. When you cancel this dialog box, the build aborts.

#### See Also

[TestStand Deployment Utility](teststand-deployment-utility.html)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/installer-options-tab-teststand-deployment-ut.html language=enus -->
## TOPIC 03833: Installer Options Tab - TestStand Deployment Utility

- bundle_id: `teststand-api-reference`
- source_path: `tsref/installer-options-tab-teststand-deployment-ut.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/installer-options-tab-teststand-deployment-ut.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Installer Options Tab Use the Installer Options tab to configure the settings the TestStand Deployment Utility uses to create an installer of the files included in the deployment and to specify which components to include from TestStand and other National Instruments software, such as hardware drive

### Installer Options Tab - TestStand Deployment Utility

#### Installer Options Tab

Use the Installer Options tab to configure the settings the TestStand Deployment Utility uses to
 [create an installer of the files included in the deployment](/csh?context=ts_tsdeploysystem_buildinstaller)
 and to
 [specify which components to include](/csh?context=ts_tsdeploysystem_identifyingcomponents)
 from TestStand and other National Instruments software, such as hardware drivers. This tab is enabled if you select the
 MSI-Based installer build output
 option in the mode tab.

Note

- Refer to
 <National Instruments>\_Legal Information.txt 
 for information about including legal information in installers built with NI products.
- You must save the full deployment installer to
 create a patch deployment installer 
 .
- (64-bit TestStand) The 64-bit TestStand Deployment Utility created a 64-bit installer that you cannot install on 32-bit operating systems.

The Installer Options tab contains the following options:

- Installation Name 
 —Enter the name for the installer to use in its titlebar and in the standard Windows Control Panel facility for adding and removing programs. Use a name that uniquely identifies the deployment and describes what the deployment installs.
- Installer Directory 
 —The directory in which the deployment utility builds the installer.
- Install TestStand Runtime 
 —Enable this option to install the TestStand Runtime, which is required to execute TestStand sequences on the test station computer and includes the TestStand Engine.
- Drivers and Components 
 —Launches the Drivers and Components dialog box, in which you can specify redistributable National Instruments drivers and components installed on the development computer to include in the deployment utility installer, such as the LabWindows/CVI Run-Time Engine. When you select an item to install, the deployment utility automatically checks for dependencies. For example, selecting the NI-488.2 driver automatically includes Measurement & Automation Explorer.
- Advanced Options 
 —Launches the Advanced Installer Options dialog box, in which you can further customize the installer you build with the deployment utility.
- Custom Commands 
 —Launches the Custom Commands dialog box, in which you configure commands that do not have corresponding options in the deployment utility for the deployment utility installer to execute after installing all files and before rebooting the computer, such as to complete the following tasks:
- Launch installers for redistributable National Instruments drivers or components, third-party components, or user interfaces.
- Run gacutil.exe to install a .NET assembly into the GAC.
- Synchronize files in a source code control system or revision control system.
- Run a batch file or executable with command-line arguments to complete a series of complex operations.
 You can use directory macros in the
 Command and Argument 
 control in the Custom Commands dialog box to avoid using fixed paths when you specify the command or the command arguments on different computers.
 Note 
 Refer to
 <National Instruments>\_Legal Information.txt
 for information about including legal information in installers built with NI products.
- Hide License Dialog 
 —When you enable this option, the installer does not prompt the user for license activation when installing National Instruments software packages that require license activation, such as the TestStand Runtime. You must have an activated license to run TestStand. Use this option when you want to install an activated license file as part of your installer. This option is dimmed when you enable the
 Include Network License Server Settings 
 option in the Advanced Installer Options dialog box.
 Note 
 For each system that you deploy, you must activate a TestStand license, typically a unique copy of the TestStand Base Deployment System License or the TestStand Debug Deployment Environment License.
- Start Menu Item Group 
 —Defines the name of the Microsoft Windows Start menu group to which the deployment utility installer adds items when you enable the
 Create Program Item 
 option on the Distributed Files tab.
- Default Installation Base Directory 
 —Defines the base directory the installer uses as the default installation location when you select
 Installation Directory 
 in the Installation Destination option on the Distributed Files tab. To specify an absolute path, select
 Absolute Path 
 and enter the absolute path into the Default Installation Base Directory control.
 Note 
 When you select the
 [<TestStand>](/csh?context=ts_tsfundamentals_directories)
 directory as a base directory, the installer installs files into the
 <TestStand>
 directory with the same version and bitness of the deployment utility that created the installer.
- Do Not Ask User for Installation Directory 
 —Enable this option to prevent users from modifying the default installation directory by disabling the installer prompt for an alternate location. When you enable this option, the installer uses the directory the Default Installation Base Directory and Default Installation Subdirectory options specify.
- Default Installation Subdirectory 
 —Defines the subdirectory under the default installation base directory when you select
 Installation Directory 
 in the Installation Destination option on the Distributed Files tab.
 Note 
 When you specify
 Absolute Path
 in the Default Installation Base Directory control, the deployment utility uses directory specified in the
 Default Installation
 control as the default subdirectory.
- Default Installation Directory 
 —An absolute path the installer uses as the default installation location. This option is only visible when you specify
 Absolute Path 
 in the
 Default Installation Base Directory 
 control.
- Installation Language 
 —Specify the language the installer uses during installation. Options include English, French, German, Japanese, Korean, and Chinese Simplified.

#### See Also

[Advanced Installer Options dialog box](advanced-installer-options-dialog-box.html)

[Custom Commands dialog box](custom-commands-dialog-box.html)

[Deploying TestStand Systems](/csh?context=ts_10203)

[Drivers and Components dialog box](drivers-and-components-dialog-box.html)

Licensing Options for TestStand Systems
 section of Chapter 1,
 Introduction to TestStand
 , of the
 [Getting Started with TestStand](/csh?context=ts_8010)
 manual

[TestStand Licensing Options](/csh?context=ts_9050)

Parent topic:

TestStand Deployment Utility

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/invocation-info-cluster.html language=enus -->
## TOPIC 03834: Invocation Info Cluster

- bundle_id: `teststand-api-reference`
- source_path: `tsref/invocation-info-cluster.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/invocation-info-cluster.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Invocation Info cluster to pass additional information to the VI. The following table lists the elements of the Invocation Info cluster, specifies the data type of the cluster element, and describes how the LabVIEW Adapter uses each cluster element. Cluster Element Data Type TestStand Proper

### Invocation Info Cluster

Use the
 Invocation Info
 cluster to pass additional information to the VI.

The following table lists the elements of the
 Invocation Info
 cluster, specifies the data type of the cluster element, and describes how the LabVIEW Adapter uses each cluster element.

| Cluster Element | Data Type | TestStand Property to Which the Adapter Copies the Value |
| --- | --- | --- |
| Test Name |  | The adapter uses the name of the step that invokes the test VI. |
| loop # |  | The adapter uses the loop count when the step that invokes the test VI loops on the step. |
| Sequence Path |  | The adapter uses the name and absolute path of the sequence file that runs the test VI. |
| UUT Info |  | The adapter uses the value from the RunState.Root.Locals.UUT.SerialNumber property, when the property exists. Otherwise, the adapter copies an empty string. Use the Serial Number String option in the Legacy VI Settings dialog box to specify an expression the LabVIEW Adapter evaluates at run time to generate a value to pass to the UUT Info element. |
| UUT # |  | The adapter uses the value from the RunState.Root.Locals.UUT.UUTLoopIndex property, when the property exists. Otherwise, the adapter copies an empty string. Use the UUT Iteration Number option in the Legacy VI Settings dialog box to specify an expression the LabVIEW Adapter evaluates at run time to generate a value to pass to the UUT # element. |

#### See Also

[Legacy VI Settings dialog box](legacy-vi-settings-dialog-box.html)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/io-configuration-dialog-box.html language=enus -->
## TOPIC 03835: IO Configuration Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/io-configuration-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/io-configuration-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Select View Detail in the context menu for a configuration in the IO Configurations list to launch the IO Configuration dialog box from the TestStand Sequence Editor or a TestStand User Interface . The IO Configuration dialog box contains the following items: Configuration Details —The details for t

### IO Configuration Dialog Box

Select
 View Detail
 in the context menu for a configuration in the IO Configurations list to launch the IO Configuration dialog box from the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 or a
 [TestStand User Interface](teststand-user-interfaces.html)
 .

The IO Configuration dialog box contains the following items:

- Configuration Details 
 —The details for the selected configuration. It contains the following information:
  - Name 
 —The name of the configuration file.
  - Path 
 —The path of the configuration file. You can edit the configuration by clicking
 Edit IO Configuration 
 . This launches the editor registered for your configuration. The configuration automatically updates after you dismiss the editor. Click
 Open Containing Folder 
 to open the folder which contains the files.
  - Editor Description 
 —The description of the editor used to handle the selected configuration file.
- Session(s) 
 —Displays the list of IO sessions present in the selected configuration.
- Session Description 
 —Displays the description of the currently selected session.
- Attributes List 
 —Displays a read-only list of attribute names and current values for the selected IO session.

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/io-configuration-step-types.html language=enus -->
## TOPIC 03836: IO Configuration Step Types

- bundle_id: `teststand-api-reference`
- source_path: `tsref/io-configuration-step-types.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/io-configuration-step-types.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use one of the following IO Configuration step types to create IO sessions, apply IO configurations to an existing IO session, and close IO sessions for NI Modular Instruments including NI-SCOPE, NI-DCPower, NI-DMM and NI-FGEN using InstrumentStudio. Create Sessions and Apply Configuration Apply Con

### IO Configuration Step Types

Use one of the following IO Configuration step types to create IO sessions, apply IO configurations to an existing IO session, and close IO sessions for NI Modular Instruments including NI-SCOPE, NI-DCPower, NI-DMM and NI-FGEN using InstrumentStudio.

- Create Sessions and Apply Configuration
- Apply Configuration
- Close Sessions

Note

- To use IO Configuration step types, you must
 download and install InstrumentStudio and iPXI driver software 
 .
- To use IO Configuration step types with the Python Adapter, you must use a Global interpreter session.

To edit an IO Configuration step type in the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 , use the edit tabs on the
 [Step Settings](step-settings-pane.html)
 pane. The tabs available update based on the type of step you select.

To edit an IO Configuration step type when you use a
 [TestStand User Interface](teststand-user-interfaces.html)
 , select
 Edit
 from the context menu for the step or click
 Configure
 <Step Name>
 on the
 [General](general-tab-step-properties-dialog-box.html)
 tab of the
 [Step Properties](step-properties-dialog-box.html)
 dialog box.

#### See Also

[Step Properties dialog box](step-properties-dialog-box.html)

[Step Settings Pane](step-settings-pane.html)

[Python Interpreter Sessions](/csh?context=ts_tsref_python_interp_sessions)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/io-configurations-options-dialog-box.html language=enus -->
## TOPIC 03837: IO Configurations Options Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/io-configurations-options-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/io-configurations-options-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Select Configure»IO Configurations Options to launch the IO Configurations Options dialog box. The IO Configurations Options dialog box contains the following options: Editors List —A list of all the IO Configuration Editors installed on the machine. It has following columns: Name —The name of the e

### IO Configurations Options Dialog Box

Select
 Configure»IO Configurations Options
 to launch the IO Configurations Options dialog box.

The IO Configurations Options dialog box contains the following options:

- Editors List 
 —A list of all the IO Configuration Editors installed on the machine. It has following columns:
  - Name 
 —The name of the editor. Hovering over a plugin displays a tooltip with a brief description about the plugin.
  - Version 
 —The versions that are supported by the editor. You can use the dropdown to choose which version TestStand uses.
  - Is Available 
 —Specifies whether TestStand can use the editor. Hovering over this column will display a tooltip with additional information about why TestStand cannot use a plugin.

TestStand creates Session variables automatically. To specify the location where the variables are created, click
 Configure»Station Options»Preferences
 and select an option from the
 Context of Automatically Created Variables
 ring control.

#### See Also

[Preferences Tab - Station Options Dialog Box](preferences-tab-station-options-dialog-box.html)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/io-session-dialog-box.html language=enus -->
## TOPIC 03838: IO Session Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/io-session-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/io-session-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Click Edit IO Session on an NI_IOSession type variable in the Variables Pane to launch the IO Session dialog box from the TestStand Sequence Editor or a TestStand User Interface . The IO Session dialog box contains the following options: Session Details —The details for the selected session. It cont

### IO Session Dialog Box

Click
 Edit IO Session
 on an NI_IOSession type variable in the Variables Pane to launch the IO Session dialog box from the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 or a
 [TestStand User Interface](teststand-user-interfaces.html)
 .

The IO Session dialog box contains the following options:

- Session Details 
 —The details for the selected session. It contains the following information:
  - Logical Name 
 —The logical name of the instrument for which a session is created. You can edit this value to point to a different Logical Name.
  - Instrument Type 
 —The type of the instrument for which a session is created. Select a different instrument type using the dropdown menu.
  - Model Name 
 —The model name of the instrument for which a session is created. You can edit this value to point to a different Model Name.
  - Location 
 —The chassis and the slot number in which the instrument is installed.
  - Channel(s) 
 —The names of the channels supported by the instrument.
- Advanced 
 —The list of IO sessions present in the selected configuration.
  - Flags 
 —Launches the
 Edit Flags 
 dialog box, in which you can modify the property flags for the data type.
  - Attributes 
 —Launches the
 Attributes 
 dialog box, in which you can create and edit the default attributes TestStand assigns to all variables, parameters, and properties you create with the data type.

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/items-table.html language=enus -->
## TOPIC 03839: Items Table

- bundle_id: `teststand-api-reference`
- source_path: `tsref/items-table.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/items-table.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Items Table The Items table contains a list of all code modules, steps, UUTs, batches, lots, and synchronization objects for which the Execution Profiler has recorded events. Each row in the table displays the following information about an item: Index —The zero-based index of the item. The profiler

### Items Table

#### Items Table

The Items table contains a list of all code modules, steps, UUTs, batches, lots, and synchronization objects for which the Execution Profiler has recorded events. Each row in the table displays the following information about an item:

- Index 
 —The zero-based index of the item. The profiler assigns indexes in the order in which it encounters items.
- Item Name 
 —The name of the item. See
 Execution Profiler»Item Names 
 .
- Source 
 —Shows Step Type Module, Step Module, Step, UUT, Batch, Lot, Lock, Auto Schedule, Batch Synchronization, Wait, Rendezvous, Queue, Notification, or Semaphore depending on the operation the item performs.
- Actual Time in Use 
 —The time the item was in use or locked by any thread. For items that can be in use simultaneously by multiple threads, the value of the Actual Time in Use column is the union of the times in use for all threads, not the sum, thus overlapping usages do not further increase this value.
- Percent Actual Time in Use 
 —The percentage of the total profile time during which the item was in the In Use state by any thread. If a synchronization item is in use for a high percentage of the total time, verify that the Cumulative Time Blocked does not indicate a performance issue.
- Cumulative Time 
 —The sum of the times the item was in the In Use or Blocked states for all threads.
- Cumulative Time in Use 
 —The sum of the times the item was in the In Use state for all threads.
- Cumulative Time Blocked 
 —The sum of the times the item was in the Blocked state for all threads. If threads spend a significant amount of time in the Blocked state waiting to use a resource that a lock or other synchronization item protects, you might be able to improve performance by adding another instance of the resource to the system.
- Average 
 —The average time taken by all operations on the item.
- Maximum 
 —The longest time taken by any operation on the item.
- Minimum 
 —The shortest time taken by any operation on the item.
- Operations 
 —The number of operations that use the item.
- Accessing Threads 
 —The number of unique threads that use the item.
- File 
 —The base name of the sequence file that contains the steps that generated the events for the operations that use the item. The column displays ellipses (…) if the events are from multiple files.

#### See Also

[Profiler Window Tables](profiler-window-tables.html)

[Synchronization Step Types](synchronization-step-types.html)

Parent topic:

Profiler Window Tables

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/ivi-step-types.html language=enus -->
## TOPIC 03840: IVI Step Types

- bundle_id: `teststand-api-reference`
- source_path: `tsref/ivi-step-types.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/ivi-step-types.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the IVI step types to configure and acquire data from Interchangeable Virtual Instrument ( IVI )class instruments. Use an initial IVI step to configure an instrument and use one or more subsequent IVI steps to perform measurements. (64-bit TestStand) 64-bit TestStand does not support IVI step ty

### IVI Step Types

IVI step types

IVI

Note

does not support

TestStand includes the following IVI step types:

- Dmm
- Scope
- Fgen
- Power Supply
- Switch
- Tools

TestStand uses the instrument logical name to reference a session to an instrument. Use National Instruments Measurement & Automation Explorer to configure instrument logical names. TestStand initializes the instrument session when you first configure the instrument and closes the instrument session when the execution closes. When two executions reference the same logical name, TestStand shares the session, and the session closes when TestStand releases the last execution of the two.

IVI step types use the National Instruments Session Manager to share named instrument connections. You can also use Session Manager to share instrument connections in
 [code modules](/csh?context=ts_tsfundamentals_bldgblocks_codemodules)
 even when you do not use IVI step types. Refer to the
 NI Session Manager Help
 . located in
 <Program Files>\National Instruments\Shared\Session Manager
 , for more information about how to use Session Manager.

Although you can use IVI steps to configure and acquire data from IVI class instruments, you must use code modules for the following tasks and situations:

- To control instruments to ensure optimal performance by precisely specifying the instrument driver calls
- To call specific driver functions an IVI class does not support
- To interleave instrument control operations with other code that must reside 
in a single code module
- When the instrument does not conform to an IVI class
- When no IVI driver exists for the instrument

Right-click an IVI step and select
 Edit
 <step type>
 from the context menu to configure and select an operation for the step to perform. You can also click the
 Edit
 <step type>
 button on the edit tab of the
 [Step Settings](step-settings-pane.html)
 pane.

When TestStand configures an instrument, the instrument driver might force a settings value. Configuring an instrument in TestStand might result in an error that indicates an invalid value for a particular setting because TestStand does not validate the instrument-based values until the configuration actually occurs. When you edit a step that configures an instrument, click the
 Validate
 button in the Edit IVI
 <Step Name>
 dialog box to test the configuration before you close the dialog box.

Use the instrument soft front panel, which is a graphical display panel for the instrument, to interact directly with the instrument session TestStand controls.

To edit an IVI step type in the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 , click the
 Edit <
 Step Type Name
 >
 button on the edit tab of the
 [Step Settings](step-settings-pane.html)
 pane.

TestStand User Interface

Edit

Edit

General

Step Properties

Note

- With IVI-C drivers, you cannot use the same instrument driver session in more than one operating system process simultaneously.
- The instrument handles that TestStand IVI step types create cannot be used within LabVIEW VIs that execute using the LabVIEW development environment. The underlying C-based handle can only be used within the TestStand process. If the LabVIEW code modules invoke IVI class- and driver-specific VIs, National Instruments does not recommend using the TestStand IVI step types at the same time.

#### See Also

[Effectively Using LabVIEW with TestStand](/csh?context=ts_10208)

[Instrument Drivers](/csh?context=ts_tsref_instrument_drivers)

[IVI Step Types (Example)](/csh?context=ts_8117)

[Session Manager (Example)](/csh?context=ts_8135)

[Session Manager Support for 64-bit TestStand](/csh?context=ts_tsfundamentals_64sessionmanager)

[Step Properties dialog box](step-properties-dialog-box.html)

[Step Settings Pane](step-settings-pane.html)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/ivi-switching-mode-edit-ivi-switch-step-dialo.html language=enus -->
## TOPIC 03841: IVI Switching Mode - Edit IVI Switch Step Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/ivi-switching-mode-edit-ivi-switch-step-dialo.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/ivi-switching-mode-edit-ivi-switch-step-dialo.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: IVI Switching Mode The IVI Switch step type supports the following IVI switch operations: Connect/Disconnect —Connects or disconnects the Source and Destination channels in the switch instrument. Configure Scan —Configures the switch module for scanning. Start Scan —Initiates a scanning operation. W

### IVI Switching Mode - Edit IVI Switch Step Dialog Box

#### IVI Switching Mode

The IVI Switch step type supports the following IVI switch operations:

- Connect/Disconnect 
 —Connects or disconnects the Source and Destination channels in the switch instrument.
- Configure Scan 
 —Configures the switch module for scanning.
- Start Scan 
 —Initiates a scanning operation.
- Wait 
 —Blocks operations until all switches debounce for an instrument.
- Configure Switch 
 —Configures channels as Configuration or Source channels and configures specific paths between channels.
- Send Software Trigger 
 —Sends a software trigger command to trigger the instrument during a scanning operation.
- Abort Scan 
 —Cancels a scanning operation.
- Get Information 
 —Retrieves low-level status and information from the instrument.

Parent topic:

Edit IVI Switch Step Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/label-edit-tab.html language=enus -->
## TOPIC 03842: Label Edit Tab

- bundle_id: `teststand-api-reference`
- source_path: `tsref/label-edit-tab.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/label-edit-tab.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Label edit tab in the TestStand Sequence Editor to configure the Label step. The Label edit tab contains the following options: Label Description —The description for the step. Hide Icon —When you enable this option, the Label step icon is not visible in the Step column on the Steps pane in

### Label Edit Tab

Use the Label edit tab in the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 to configure the Label step.

The Label edit tab contains the following options:

- Label Description 
 —The description for the step.
- Hide Icon 
 —When you enable this option, the Label step icon is not visible in the Step column on the
 Steps 
 pane in the
 Sequence File 
 window.
- Hide Status 
 —When you enable this option, the
 step status 
 evaluates to a string containing a single white space character, and the step result is disabled.
- Hide Name 
 —When you enable this option, the step name is not visible in the Step column on the Steps pane.

#### See Also

[Built-In Step Types](built-in-step-types.html)

[Sequence File Window](sequence-file-window.html)

Parent topic:

Label Step

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/label-step.html language=enus -->
## TOPIC 03843: Label Step

- bundle_id: `teststand-api-reference`
- source_path: `tsref/label-step.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/label-step.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use a Label step as the target for a Goto step. Use Label steps to rearrange or delete other steps in a sequence without having to change the specification of targets in Goto steps. Label steps do not pass or fail and by default do not record results. After a Label step executes, the TestStand Engin

### Label Step

Use a Label step as the target for a
 [Goto](goto-step.html)
 step. Use Label steps to rearrange or delete other steps in a sequence without having to change the specification of targets in Goto steps.

Label steps do not pass or fail and by default do not record results. After a Label step executes, the TestStand Engine sets the
 [step status](/csh?context=ts_tsfundamentals_step_status_values_table)
 to
 Done
 or
 Error
 . You can edit a Label step to specify a description that appears next to the Label step name in the sequence editor.

#### Configuring the Step

Use the
 [Label](label-edit-tab.html)
 edit tab in the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 and the
 [Edit Label Step](edit-label-step-dialog-box.html)
 dialog box in a
 [TestStand User Interface](teststand-user-interfaces.html)
 to configure the Label step.

#### Step Properties

In addition to the
 [common custom properties](/csh?context=ts_tsfundamentals_custom_result_props)
 , the Label step type defines the following step property:

- Step.Description 
 —A string that appears next to the step name in the sequence editor.

#### See Also

[Built-In Step Types](built-in-step-types.html)

Parent topic:

Built-In Step Types

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/labview-adapter-configuration-dialog-box.html language=enus -->
## TOPIC 03844: LabVIEW Adapter Configuration Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/labview-adapter-configuration-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/labview-adapter-configuration-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Select Configure»Adapters , select the LabVIEW Adapter in the list control, and click Configure to launch the LabVIEW Adapter Configuration dialog box, which contains Select or Type Which LabVIEW Server to Use, Options, and LabVIEW Project Settings sections. If no LabVIEW Runtime versions are instal

### LabVIEW Adapter Configuration Dialog Box

Configure»Adapters

Configure

Note

#### Selecting a LabVIEW Server

The Select or Type Which LabVIEW Server to Use section contains the following options for specifying the server or engine the LabVIEW Adapter uses:

- LabVIEW Runtime 
 —The
 version of the LabVIEW Runtime 
 to use for loading and executing VI
 code modules 
 . Selecting this option runs VIs in the same process as TestStand to provide optimal performance when calling VIs. When you select this option, you cannot create or edit VIs from TestStand.
 
 This control lists only the supported versions of the LabVIEW Runtime. When you only have an older version of LabVIEW installed, this control is disabled.
  - Version 
 —Select the LabVIEW Runtime version that matches the version of the VIs that TestStand executes.
 
 Select the
 Auto detect using VI version 
 option in the Version control to let TestStand automatically detect the version of the LabVIEW Runtime to use when executing a LabVIEW code module VI. Use this option when you have VIs saved in different versions of LabVIEW and you want them to always run in the LabVIEW Runtime without mass compiling to a specific LabVIEW version. You can also use this option when you create a deployment to ensure that TestStand uses the correct LabVIEW Runtime version to execute VIs you deploy.
 Note 
 TestStand can use newer versions of the LabVIEW Runtime when you install LabVIEW on your development system. You can include newer versions of the LabVIEW Runtime in deployments using the
 [Drivers and Components](drivers-and-components-dialog-box.html)
 dialog box of the
 [TestStand Deployment Utility](teststand-deployment-utility.html)
 . If you do not have a LabVIEW development system installed on the computer, the default value of the LabVIEW Runtime option is
 Auto detect using VI version
 , and you do not need to
 [deploy](/csh?context=ts_10203)
 the
 Adapters.cfg
 file that specifies the LabVIEW Runtime version to use.
 When using IO Configuration step types with LabVIEW to control NI Modular Instruments, if the LabVIEW Adapter is configured to use the LabVIEW Runtime and the
 Auto detect using VI version
 option is selected in the
 Version
 control, the LabVIEW Adapter will use a pre-defined LabVIEW version to execute the IO Configuration step types. This might lead to errors when using the IO session handle in other VIs. To resolve the issue open
 <TestStand>\Components\Language\English\IOConfigurationStrings.ini
 and modify the value of
 DEFAULT_LV_RTE_VERSION_FOR_IPXI_VI
 to match the LabVIEW version of the VIs that you are currently using in your sequence file.
 If you see a version mismatch error on executing source-only VIs when this option is enabled, then refer to
 [Executing source-only VIs in LabVIEW Runtime Engine](/csh?context=ts_tsref_executing_sovi_in_lvrte)
  - Execute 'Same as caller' VIs Using Multiple Threads 
 —Specifies whether TestStand configures the LabVIEW Runtime to use
 multiple execution threads to execute VIs 
 with the preferred execution system set to
 same as caller 
 .
  - Number of Threads 
 —The number of LabVIEW execution threads TestStand configures the LabVIEW Runtime to use to execute VIs with the preferred execution system set to
 same as caller 
 .
  - Additional Threads Inherit Calling Thread's CPU Affinity 
 —Specifies whether TestStand sets the CPU affinity of additional LabVIEW execution threads to the CPU affinity of the TestStand execution thread.
 Note 
 The Execute 'Same as caller' VIs Using Multiple Threads, Number of Threads, and Additional Threads Inherit Calling Thread's CPU Affinity options apply only when TestStand executes VIs using the LabVIEW Runtime and apply only to VIs with the preferred execution system set to
 same as caller
 . If you modify any of these options, the changes do not take effect until the next time you start the TestStand application.
 The LabVIEW Runtime option performs the same behavior as the Always Run VI in LabVIEW Runtime option in the
 [LabVIEW Advanced Settings](labview-advanced-settings-window.html)
 window in the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 or on the
 [Advanced Settings](advanced-settings-tab-edit-labview-vi-call-di.html)
 tab of the
 [Edit LabVIEW VI Call](edit-labview-vi-call-dialog-box.html)
 dialog box in a
 [TestStand User Interface](teststand-user-interfaces.html)
 . However, the
 Auto detect using VI version
 option applies to all LabVIEW steps in a sequence.
- Enable Build Source Files and Execute 
 —Enable this option to use the
 Build Source Files and Execute 
 feature.
 Note 
 Enabling the
 Enable Build Source Files and Execute
 option will enable the
 Enable Version Independent Runtime Engine
 option.
 Changes made to this option do not take effect until you restart the TestStand application.
- Enable Version Independent Runtime Engine 
 —Specifies whether
 Version Independent Runtime Engine 
 support is enabled in the LabVIEW Adapter. This option applies to all instances of LabVIEW runtimes, version 2017 or later, that are used by the TestStand application.
 When you enable this option, the LabVIEW runtime server is set to
 Auto detect using VI version 
 by default.
 Note 
 You can enable the
 Enable Version Independent Runtime Engine
 option only if your machine has LabVIEW runtime version 2017 or later installed.
 Changes made to this option do not take effect until you restart the TestStand application.
- Enable Debugging and Tracing 
 —Configures the LabVIEW Runtimes loaded by TestStand to accept remote connections from LabVIEW Development Systems and LabVIEW Desktop Execution Trace Toolkit (DETT) to support debugging and tracing of VIs executed using the TestStand Sequence Editor. You can use the LabVIEW Development System to debug VIs and the DETT to capture execution events for VIs executing on the local machine. Refer to the
 Debugging and Tracing of VIs Executed Using the LabVIEW Runtime 
 topic for more information about using the
 Enable Debugging and Tracing 
 option.
 Note 
 The
 Enable Debugging and Tracing
 option applies to VIs executed using the LabVIEW 2015 Runtime or later.
 Debugging VIs is only supported in the TestStand Sequence Editor.
 Tracing VIs is supported in both the TestStand Sequence Editor and a TestStand User Interface.
- Development System (Active Version) 
 —To use LabVIEW to create or edit VIs or to debug VIs TestStand calls, you must select this option so VIs execute in the active version of the LabVIEW development environment. You must have the LabVIEW development system installed on the same computer as TestStand to use this option. If the text
 Not Allowed 
 appears next to a LabVIEW version, TestStand no longer allows connecting to that version of LabVIEW. Select one of the following options to indicate which LabVIEW version to launch:
 
 Note 
 Although the LabVIEW adapter configuration dialog will display the most recently opened version of LabVIEW Development System as the active version of LabVIEW, if multiple versions of LabVIEW are open at the same time on the system, the first version of LabVIEW launched will be used by the LabVIEW adapter and related tools to create or edit or debug VIs. This behavior is the consequence of how Out-of-Process ActiveX Servers are designed and implemented. 
 Note 
 TestStand supports invoking cross-bitness code modules by executing the VIs only in the LabVIEW development environment and does not support using the LabVIEW Runtime. In addition, the TestStand Deployment Utility only supports packaging VIs for LabVIEW code modules of the same bitness as the deployment utility.
  - Use Active LabVIEW Version 
 —Launches the current active 32-bit LabVIEW or 64-bit LabVIEW development environment, with a preference to match the bitness of TestStand. This is the default option.
  - Use Active 32-bit Version 
 —Launches the current active 32-bit LabVIEW development environment.
  - Use Active 64-bit Version 
 —Launches the current active 64-bit LabVIEW development environment.
- Other Executable 
 —Uses a
 LabVIEW executable 
 you build with the Build Executable functionality in LabVIEW. When you select this option, you cannot create or edit VIs from TestStand or debug VIs TestStand calls. The version of the VIs that TestStand executes must match the version of the LabVIEW Runtime or the version of LabVIEW that built the executable.
 To use this option, enter the ActiveX Automation server name associated with the LabVIEW executable. You must install and register the executable on the same computer as TestStand. Launch the executable once to register it as an ActiveX Automation server. The
 [<TestStand Public>](/csh?context=ts_tsfundamentals_directories)
 \Components\RuntimeServers\LabVIEW 
 directory contains an example server VI and application build script for LabVIEW.
 Note 
 (Windows 10) Microsoft Windows requires you to log in as a user with administrator privileges to register a server. LabVIEW cannot register ActiveX Automation servers on Windows Vista when building executables without elevation.

#### Configuring Other Options

The Options section contains the following options:

- Reserve Loaded VIs for Execution 
 —Specifies whether LabVIEW
 reserves each VI 
 to run when TestStand loads the VI. When a VI is reserved for execution, any references the VI creates during execution remain valid until the VI is unreserved. VIs LabVIEW reserves take less time to call. However, you cannot edit the VIs in LabVIEW unless you click
 Edit VI 
 on the
 LabVIEW Module tab or Specify Module 
 dialog box or select
 Edit Code 
 from the context menu for the calling step.
 TestStand unreserves a VI under the following circumstances:
 
 The Reserve Loaded VIs for Execution option eliminates the need to use permanent reference VIs for sharing LabVIEW references between step modules.
 You can create a reference in a VI one step in a sequence calls, use the reference in a VI a second step calls, and close the reference in a third step. For example, you can create a file refnum from Open File, use the reference in Read File or Write File, and close the reference using Close File when you no longer need the reference.
 A LabVIEW reference exists only as long as the VI that creates it is reserved. When you set the Unload Option for a step that calls a VI to Unload After a Step Executes or Unload When Precondition Fails, the LabVIEW references the step creates might be destroyed on completion of the step. If you do not reserve VIs for execution, you can use the permanent reference VIs to maintain LabVIEW references between steps. Refer to the
 Accessing Arrays Using API from LabVIEW Code Modules 
 example program for more information.
  - When you select
 File»Unload All Modules 
 .
  - When the VI is unloaded based on sequence file or step unload options.
  - When you open a VI for editing from within TestStand.
- Always run VI in Packed Project Library 
 —Overrides the VI configured in the code module with the VI in the packed project library. You can select the packed project library in the Override Module Settings window for the step.
 Note 
 Using this option requires that user
 [configures override module settings](/csh?context=ts_tsref_ppl_debug)
 for each step.
- Automatically Build Packed Project Libraries at the Start of Execution 
 —Builds the packed project library at the start of execution if the packed project library is missing or out-of-date.
- Code Template Policy 
 —Specify the templates to use during code creation. The following options are available:
  - Allow Only New Templates 
 —Only searches for new code templates.
 When you select this option and create a new VI using the LabVIEW Module tab, TestStand creates a new VI based on the code template for the specified step type. When the step type has multiple code templates available, TestStand launches the
 Choose Code Template 
 dialog box, in which you can select the code template to use for the new VI.
  - Allow Only Legacy Templates 
 —Only searches for legacy code templates.
 When you select this option and create a new VI using the LabVIEW Module tab, TestStand launches the Optional Parameters dialog box, in which you select the optional parameters, such as
 Input Buffer 
 ,
 Invocation Info 
 , or
 Sequence Context ActiveX Pointer 
 , you want to include as input parameters for the VI.
  - Allow New and Legacy Templates 
 —Searches for both new and legacy templates.
 When you select this option and create a new VI using the LabVIEW Module tab, TestStand launches the Choose Code Template dialog box, in which you can select the code template to use for the new VI.
- Legacy VI Settings 
 —Launches the
 Legacy VI Settings 
 dialog box, in which you can configure settings relevant to calling legacy test VIs. The Legacy VI Settings dialog box contains
 expressions 
 the LabVIEW Adapter evaluates to generate values to pass to the VI in the various
 Invocation Info 
 cluster fields. Legacy VIs can use the
 Invocation Info
 cluster 
 as an optional input.

#### Configuring LabVIEW Project Settings

The LabVIEW Project Settings section contains the following options:

- Auto Deploy Shared Variables on First Load of any VI in a Project 
 —When you enable this option, TestStand deploys to the local computer
 shared variables 
 defined in LabVIEW libraries within the LabVIEW projects you use in TestStand. The deployment of shared variables occurs the first time TestStand loads a LabVIEW step that references the project during execution. Ensure that the LabVIEW library to deploy contains only shared variables.
 Note 
 Enabling this option does not deploy shared variables defined in LabVIEW packed project libraries specified in LabVIEW projects you use in TestStand. Use the
 [Deploy Library](deploy-library-step-labview-utility-step-type.html)
 step type to deploy or undeploy to the local computer the shared variables defined in a LabVIEW packed project library file.
 TestStand can deploy a shared variable bound to another shared variable only when you use an NI Publish-Subscribe Protocol (NI-PSP) URL to bind the shared variable to deploy to another shared variable. If you attempt to use a Deploy Library step to deploy a shared variable to a variable in a LabVIEW project, the deployment fails. Refer to the
 LabVIEW Help
 for more information about deploying shared variables and NI-PSP URLs.
- Auto Undeploy Shared Variables on Last Unload of all VIs in a Project 
 —When you enable this option, TestStand undeploys the shared variables defined in LabVIEW libraries within the LabVIEW project after TestStand unloads the last LabVIEW step that references the LabVIEW project. TestStand automatically enables this option when you enable the
 Auto Deploy Shared Variables on First Load of any VI in a Project 
 option.
 Note 
 If you do not want TestStand to automatically deploy shared variables, leave the Auto Deploy Shared Variables on First Load of any VI in a Project option disabled.

#### See Also

[Caveats for Configuring the LabVIEW Adapter to Use a LabVIEW Runtime or Other Executable Server](/csh?context=ts_tsref_labview_rte_other_exec)

[Choose Code Template dialog box](choose-code-template-dialog-box.html)

[Deploying Network-Published Shared Variables](/csh?context=ts_tslabview_variable)

[Deploying TestStand Systems](/csh?context=ts_10203)

[Drivers and Components dialog box](drivers-and-components-dialog-box.html)

[LabVIEW Module tab](labview-module-tab.html)

[Legacy VI Settings dialog box](legacy-vi-settings-dialog-box.html)

[Organizing LabVIEW-Based TestStand Systems](/csh?context=ts_tslabview_project)

[Specify Module dialog box](specify-module-tabs-and-dialog-boxes.html)

[Symmetric Multiprocessing in VIs Executed from TestStand](/csh?context=ts_tslabview_smp)

[TestStand Deployment Utility](teststand-deployment-utility.html)

[Version Independent Runtime Engine Support](/csh?context=ts_tsref_vire_support)

[Build Source Files and Execute](/csh?context=ts_tsref_build_and_execute)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/labview-advanced-settings-window.html language=enus -->
## TOPIC 03845: LabVIEW Advanced Settings Window

- bundle_id: `teststand-api-reference`
- source_path: `tsref/labview-advanced-settings-window.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/labview-advanced-settings-window.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Click the Advanced Settings button on the LabVIEW Module tab of the Step Settings pane to launch the LabVIEW Advanced Settings window. In the LabVIEW Advanced Settings window, you can configure the LabVIEW adapter to always run the VI using a LabVIEW Run-Time Engine or to execute the VI on a remote

### LabVIEW Advanced Settings Window

Click the
 Advanced Settings
 button on the
 [LabVIEW Module](labview-module-tab.html)
 tab of the Step Settings pane to launch the LabVIEW Advanced Settings window.

In the LabVIEW Advanced Settings window, you can configure the LabVIEW adapter to always run the VI using a LabVIEW Run-Time Engine or to execute the VI on a remote system. To select a VI for remote call, enable the
 Run VI on a Remote Computer
 option.

The LabVIEW Advanced Settings window contains the following options:

- Run VI on a Remote Computer 
 —Specifies a VI for remote call. This section contains the following options:
  - Remote Host 
 —The remote computer to use to run the VI.
  - Specify Expression For Host 
 —Specifies whether the Remote Host control contains an expression the LabVIEW Adapter evaluates at run time to determine the name of the remote host.
  - Remote Project Path 
 —The path and name of the LabVIEW project the step calls on the remote computer. When you specify an absolute or relative path, the remote computer loads the LabVIEW project into memory, if it is not already open. When the path is relative, the remote computer interprets the path as relative to the application directory, if applicable. Specifying a remote LabVIEW project path is optional.
  - Remote VI Path 
 —The path and name of the VI the step calls on the remote system. When you specify an absolute or relative path, the remote computer loads the VI into memory, if it is not already open. When the path is relative, the remote computer interprets the path as relative to the application directory, if applicable. If a VI of the same name is already in memory, the VI is used regardless of whether the path of the VI is the same as the path specified.
 Note 
 If a path is not specified in the Remote VI Path control, the remote system will download the VI specified in the VI Pathname control on the
 [LabVIEW Module](labview-module-tab.html)
 tab, if it is not already in memory and if the remote system is running LabVIEW Real-Time Module to which TestStand can download.
 If the step calls an Express VI, the Remote VI Path control is disabled. Express VIs are downloaded to a real-time system that uses LabVIEW if supported by TestStand.
 If the step uses a Remote Project Path, the Remote VI Path control specifies the URL of the VI within the defined LabVIEW project.
  - Port Number 
 —The TCP/IP port number to use to connect to the remote system.
  - Timeout (ms) 
 —The time, in milliseconds, to wait for a connection before timing out.
- Always Run VI in LabVIEW Run-Time Engine 
 —When you enable this option, you can always use a LabVIEW Run-Time Engine (RTE) to run the VI, regardless of the global
 LabVIEW Adapter 
 setting. TestStand selects the appropriate version of the LabVIEW RTE according to the version of LabVIEW in which you last compiled the VI. This guarantees that the VI will always be loaded with a specific version of the LabVIEW RTE, even if another version exists. Use this option when you do not want the global settings for the adapter to affect the tools and step types you create.
 Note 
 TestStand can use newer versions of the LabVIEW RTE when you install LabVIEW on your development system. You can include newer versions of the LabVIEW RTE in deployments using the
 [Drivers and Components](drivers-and-components-dialog-box.html)
 dialog box of the
 [TestStand Deployment Utility](teststand-deployment-utility.html)
 .
 When the "Version Independent Runtime Engine" option is enabled in the LabVIEW adapter and the LabVIEW Runtime Engine Version is set to a specific version rather than AutoDetect, then the VI in this step will be loaded using the runtime version selected in the adapter rather than the VI version.
 If you see an error saying that the matching runtime is missing or the compiled code is missing even though the files were mass compiled, then refer to
 [Executing source-only VIs in LabVIEW Runtime Engine](/csh?context=ts_tsref_executing_sovi_in_lvrte)
- Array Parameters Match LabVIEW Array Dimensions 
 —Constrain array parameters to match the size of the corresponding LabVIEW array control or indicator in every dimension. When enabled, the data at each index of a multi-dimensional array in TestStand and the corresponding control or indicator in LabVIEW will be the same when passing arrays during execution.
 Note 
 After you change this option, you must reload the module before you can execute it. An error indicator on the Module tab of the
 [Step Settings](step-settings-pane.html)
 pane will prompt you to reload the module.

#### See Also

[Calling VIs on Remote Computers](/csh?context=ts_tslabview_remote)

[Drivers and Components dialog box](drivers-and-components-dialog-box.html)

[Edit LabVIEW VI Call dialog box](edit-labview-vi-call-dialog-box.html)

[LabVIEW Adapter](/csh?context=ts_tsref_labview)

[LabVIEW Module Tab](labview-module-tab.html)

[TestStand Deployment Utility](teststand-deployment-utility.html)

Parent topic:

LabVIEW Module Tab

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/labview-module-tab.html language=enus -->
## TOPIC 03846: LabVIEW Module Tab

- bundle_id: `teststand-api-reference`
- source_path: `tsref/labview-module-tab.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/labview-module-tab.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Insert a step configured to use the LabVIEW Adapter and select Specify Module or Step Settings from the context menu to display the LabVIEW Module tab in the TestStand Sequence Editor . You can use the LabVIEW Module tab to complete the following tasks: Specify whether the step calls a member VI fro

### LabVIEW Module Tab

Insert a step configured to use the LabVIEW Adapter and select
 Specify Module
 or
 Step Settings
 from the context menu to display the LabVIEW Module tab in the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 .

You can use the LabVIEW Module tab to complete the following tasks:

- Specify whether the step calls a member VI from a LabVIEW class or calls a VI that is a not a member of a LabVIEW class
- Select the LabVIEW project that refers to the VI (optional)
- Select the VI the step executes
- Create and edit a VI or an optional LabVIEW project in LabVIEW
- Select an Express VI and convert an Express VI to a standard VI
- Specify whether LabVIEW shows the front panel of the VI when TestStand calls the VI

The LabVIEW Module tab contains the following options:

- Call Type 
 —The type of call the step uses. Select one of the following options. The option you select affects the other options available on the tab.
  - VI Call 
 —TestStand calls the VI without LabVIEW dynamic dispatching.
  - Class Member Call 
 —Select a member VI from a LabVIEW class. LabVIEW activates dynamic dispatching when required. When you select Class Member Call, you cannot execute the member call remotely.
 Note 
 You must have LabVIEW 2012 or later to use LabVIEW dynamic dispatching when calling LabVIEW classes in TestStand.
  - Property Node Call 
 —Configures a Property Node call for a LabVIEW I/O reference or a LabVIEW class.
 Note 
 You must have LabVIEW 2013 or later to run a Property Node call. You must use the LabVIEW 2013 Development Environment to configure the Property Node call.
- Project Path 
 —The path of the LabVIEW project the step uses. The control contains a most recently used (MRU) list of the last five selected LabVIEW projects. Specifying a LabVIEW project is optional.
- Browse for LabVIEW Project 
 —Launches the Select the Step's LabVIEW Project File dialog box, in which you can browse for the LabVIEW project (
 .lvproj 
 ) file to open.
- Create LabVIEW Project 
 —Creates an empty LabVIEW project. If the LabVIEW project you specify does not already exist, the LabVIEW Adapter creates it. If the file already exists, the LabVIEW Adapter prompts you to overwrite the existing file.
- Edit LabVIEW Project 
 —Edits an existing LabVIEW project.
- Edit LabVIEW Class 
 —Edits an existing LabVIEW class.
 Note 
 The Edit LabVIEW Class option is available only when you select
 Property Node Call
 as the Call Type.
- Select Express VI 
 —Use the LabVIEW browse button to select the Express VI you want to call. The LabVIEW browse button displays a pop-up menu that lists all the Express VIs found in the currently selected LabVIEW functions palette view. To select an Express VI not found in the menu, select the
 Browse 
 menu item. Once you select an Express VI, you can configure the VI call.
 Note 
 Calls to Express VIs are embedded within the sequence file, not stored on disk.
- Convert Express VI to Standard VI 
 —Converts an Express VI to a standard VI by detaching the Express VI from the module, creating a standard VI on disk that calls the Express VI, and reconfiguring the module to call the new VI. You must distribute this wrapper VI with the sequence file.
- Convert Property Node to Standard VI 
 —Converts a Property Node to a standard VI by detaching the embedded Property Node from the module, creating a standard VI which contains the Property Node, changing the call type of the step to
 VI Call 
 , and then reconfiguring the step to call the new VI. You must distribute this wrapper VI with the sequence file.
- Show VI Front Panel 
 —When you enable this option, the front panel of the VI opens when the LabVIEW Adapter calls the VI.
- Create VI 
 —Creates a code shell for the VI. If the VI file you specify does not already exist, the LabVIEW Adapter creates it. If the file already exists, the LabVIEW Adapter prompts you to overwrite the existing file. If a VI code template file exists for the step type you are using for the step, the LabVIEW Adapter uses the template to create the new VI.
- Edit VI 
 —Edits an existing VI. If the step uses a LabVIEW project, the VI opens in the LabVIEW project.
 Note 
 This button uses the label Open VI when you have specified a VI in a LabVIEW packed project library. If the step uses an Express VI, the button uses the label Configure VI and configures the Express VI the wrapper VI calls.
- Reload VI Prototype 
 —Allows the user to refresh the parameter information of the VI.
- Advanced Settings 
 —Launches the
 LabVIEW Advanced Settings dialog 
 , in which you can configure a LabVIEW step to execute a VI on a remote system or with a LabVIEW Run-Time Engine.
- Override Module Settings 
 —Launches the
 Override Module Settings 
 window, in which you can configure a LabVIEW step to run the VI in a packed project library.
- Show VI Help 
 —Displays the help associated with the VI.
- Undock/Dock LabVIEW VI Help 
 —Attaches or detaches the VI Help panel from the Module tab.
- VI Parameter Table 
 —Contains information about each control or indicator wired to the connector pane of the VI. These are the parameters of the VI.
 
 Note 
 The VI Parameter Table displays parameters according to the order in the VI context help image.
  - Parameter Name 
 —Caption text or label text, if no caption exists, of the control or indicator.
 Note 
 Parameters with attributes include an
 Edit Attributes
 button in the Name column of the VI Parameter Table. You can edit attributes for fields of containers and elements of arrays. TestStand associates parameter attributes with the module parameter, which TestStand stores with the step configuration information, not with the parameter value that TestStand passes to the module. Right-click an item in the VI Parameter Table to access the
 [VI Parameter Table](for-module-tabs-parameters-table-context-menu.html)
 context menu, from which you can launch the
 [Attributes](attributes-dialog-box.html)
 dialog box.
  - Type 
 —TestStand
 equivalent data type 
 for the control or indicator.
 For one-dimensional arrays, you can specify an expression value for the entire array, or you can specify values for each element of the array. Use the plus (
 + 
 ) buttons to insert a new element in the array, and the minus (
 - 
 ) buttons to remove specific elements from the array.
When you select
 Binary String 
 in the Type column of the VI Parameter Table on the LabVIEW Module tab to store a LabVIEW string that contains binary data in a TestStand property, TestStand handles the string data in different ways depending on the version of LabVIEW you are using, as the following table describes.
 LabVIEW Version
 TestStand BehaviorLabVIEW 2012 or later Development System on a non-multibyte operating system
 LabVIEW 2009 SP1 or later Development System on a multibyte operating system
 LabVIEW 2009 SP1 or later RTE on any operating system
 TestStand compresses the binary data, encodes the compressed data, and stores the compressed data using only printable ASCII characters. To pass a compressed string to a VI, select
 Binary String
 in the Type column. TestStand unencodes and decompresses the binary data the string stores before passing it to the VI.
 LabVIEW 2011 SP1 or earlier Development System on a non-multibyte operating system
 LabVIEW 2009 or earlier Development System on a multibyte system
 LabVIEW 2009 or earlier RTE on any operating system
 TestStand escapes the string before storing it and substitutes hexadecimal codes for the unprintable characters, such as the NUL character, in the string. To pass an escaped string to a VI, select
 Binary String
 in the Type column. TestStand unescapes the string before passing it to the VI and substitutes the correct character values for the hexadecimal values in the escaped string. 
 Note 
 To retrieve the raw binary data stored in a string variable in TestStand, call the
 
 [PropertyObject.GetValBinary](../tsapiref/propertyobject-getvalbinary.html)
 method of the TestStand API. See the
 [Retrieving Binary String Values from Reports and Databases](/csh?context=ts_tsreports_retrievingbinarystrings)
 topic for more information about retrieving binary data from string values.
    - Create/Update Custom Data Type 
 —Launches the
 Create/Update Custom Data Type from Cluster 
 dialog box, in which you can configure a new custom data type or update an existing custom data type.
    - Apply Cluster Passing Changes 
 —Updates a VI parameter that contains a subproperty that no longer maps to the correct cluster element. You can use this button to update the parameter and automatically map the subproperty to the correct cluster element.
 This button might also appear when TestStand cannot
 automatically map a subproperty to the correct element 
 and the Value column of the VI Parameter Table contains a '??? <Unknown Value>' error for the subproperty.
  - In/Out 
 —Specifies whether the parameter is an input (control on the VI front panel wired to the connector pane) or an output (indicator on the VI front panel wired to the connector pane).
  - Log 
 —When you enable this option, the step logs the parameter as an additional result. Enabling this option is equivalent to using the checkbox next to the additional result name on the
 Additional Results panel 
 of the
 Properties 
 tab of the
 Step Settings pane 
 .
  - Default 
 —When you enable this option, TestStand uses the default value of the control for the parameter, cluster element, or array element. This option is not available when the terminal of the VI is marked as Required.
  - Value 
 —A TestStand expression. For input parameters, TestStand passes the value of this expression to the VI unless you place a checkmark in the option in the Default column. For output parameters, TestStand stores the data the VI outputs in the location this expression specifies. To help you enter an expression in the Value column, click the
 Expression Browse 
 button to launch the
 Expression Browser 
 dialog box. For enumerated types, a combo box displays all valid values for the type. You can also use an expression with an enumerated type.
 Note 
 For Express VIs, specify a valid value for each control on the connector pane to prevent an error when you configure or run the VI.
- VI Context Help Image and Description 
 —Displays the context help image of the VI as shown in the LabVIEW Context Help dialog and displays the description of the VI from the Documentation tab of the LabVIEW VI Properties dialog box. When you click a label or terminal of the VI icon, TestStand highlights the parameter in the VI Parameter Table.

#### Specifying a VI

The LabVIEW Module tab contains the following options when you select
 VI Call
 from the Call Type ring control.

- VI Path 
 —The path of the VI the step calls. The path specifies a different location, depending on if the VI is an Express VI or whether the VI is contained in a LabVIEW project, as the following table describes.
 VI Type
 BehaviorExpress VI
 The path specifies the name of the Express VI.
 A VI that is not contained in a LabVIEW project
 The path is the path to the VI on disk, within a LLB, or within a packed project library.
 A VI that is contained in a LabVIEW project
 The path is the URL of the VI within the project instead of an absolute or relative path. 
 The VI Path ring control contains the following options, in which you can specify if the VI is a standard VI or a wrapper for an Express VI. The control contains an MRU list of the last five selected VIs. If a workspace is opened, the MRU list also contains all of the VIs in the workspace for which TestStand can calculate an absolute path. A line divides the most recently selected VIs and the VIs found in the workspace.
- Browse for VI 
 —Launches an
 Open File 
 dialog box, in which you can browse for an independent VI, a LabVIEW library (
 .llb 
 ), or LabVIEW packed project library (
 .lvlibp 
 ) file to open. The LabVIEW Module tab provides different options for specifying a VI in a LabVIEW library or packed project library, as the following table describes.
 File Type You Select
 BehaviorLabVIEW library (
 .llb
 )
 Browses into the library and launches the
 [Select a VI](select-a-vi-dialog-box.html)
 dialog box, in which you can select a VI the library contains.
 LabVIEW packed project library (
 .lvlibp
 )
 Displays the content of the packed project library file and launches the
 [Select a VI from a LabVIEW Packed Project Library](select-a-vi-from-a-labview-packed-project-lib.html)
 dialog box, in which you can select a VI the packed project library exports to open.
- Browse for VI in LabVIEW Project 
 —Launches the
 Select VI From LabVIEW Project 
 dialog box, in which you can select a VI from the LabVIEW project the step uses. The control returns the URL within the LabVIEW project rather than an absolute or relative pathname for the file. This option is available only when you specify a LabVIEW project file in the Project Path control.
- Add or Remove VIs from LabVIEW Project 
 —Launches the
 Add or Remove Items from LabVIEW Project 
 dialog box, in which you can add, create, or remove VIs from the LabVIEW project the step uses. This option is available only when you specify a LabVIEW project file in the Project Path control.

#### Specifying a Class Member

The LabVIEW Module tab contains the following options when you select
 Class Member Call
 from the Call Type ring control.

- Class Path 
 —The path of the LabVIEW class the step uses. The Class Path control contains a list of the five most recently selected LabVIEW classes.
 Click the
 Browse for LabVIEW Member 
 button, located to the right of the Member Name control, to launch the
 Select a Class Member from LabVIEW Class 
 dialog box, in which you can select a LabVIEW class member VI to call from the specified LabVIEW class.
- Browse for LabVIEW Class 
 —Launches the
 Select the Step's LabVIEW Class File 
 dialog box, in which you browse for a LabVIEW class (
 .lvclass 
 ) file or a LabVIEW library (
 .llb 
 ) or LabVIEW packed project library (
 .lvlibp 
 ) file that contains a LabVIEW class file. The LabVIEW Module tab provides different options for specifying a class in a LabVIEW library or packed project library, as the following table describes.
 File Type You Select
 BehaviorLabVIEW library (
 .llb
 )
 Launches the
 [Select a Class from LabVIEW LLB](select-a-class-from-labview-llb-dialog-box.html)
 dialog box, in which you can review the files the LLB file contains and select a LabVIEW class file to open.
 LabVIEW packed project library (
 .lvlibp
 )
 Launches the
 [Select a Class from LabVIEW Packed Project Library](select-a-class-from-labview-packed-project-li.html)
 dialog box, in which you can review the content of the packed project library file and select a LabVIEW class file from the packed project library to open.
- Browse for LabVIEW Class in LabVIEW Project 
 —Launches the
 Select a Class from LabVIEW Project 
 dialog box, in which you can select a LabVIEW class to call from the LabVIEW project you specify. This option is available only when you specify a LabVIEW project file in the Project Path control.
- Member Name 
 —The name of the public member from the LabVIEW class the step uses.
- Browse for LabVIEW Member 
 —Launches the
 Select a Class Member from LabVIEW Class 
 dialog box, in which you can select a LabVIEW class member VI to call from the specified LabVIEW class.
- Browse for LabVIEW Class Member in LabVIEW Project 
 —Launches the
 Select a Class Member from LabVIEW Project 
 dialog box, in which you can select a LabVIEW class member VI to call from the specified LabVIEW project. This option is available only when you specify a LabVIEW project file in the Project Path control.

#### Specifying a Property Node

The LabVIEW Module tab contains the following options when you select
 Property Node Call
 from the Call Type ring control.

- Configure Settings for Property Node 
 —Launches the
 Configure Property Node 
 dialog box, in which you can specify the I/O Reference type or the LabVIEW class and select properties for the Property Node call.
- Regenerate Property Node 
 —Rebuilds the Property Node call using the current step settings.

#### See Also

[Add or Remove Items from LabVIEW Project dialog box](add-or-remove-items-from-labview-project-dial.html)

[Attributes dialog box](attributes-dialog-box.html)

[Calling LabVIEW Property Nodes from TestStand](/csh?context=ts_tslabview_property_node)

[Create/Update Custom Data Type from Cluster dialog box](create-update-custom-data-type-from-cluster-d.html)

[Cross-Bitness Support using the LabVIEW development system](/csh?context=ts_tsfundamentals_64lvcrossbitnesssupport)

[Edit Search Directories dialog box](edit-search-directories-dialog-box.html)

[Effectively Using LabVIEW with TestStand](/csh?context=ts_10208)

[Express VIs and Property Node Calls in 32-bit TestStand and 64-bit TestStand](/csh?context=ts_tsfundamentals_64lvexpvipropnodecalls)

[Expression Browser dialog box](expression-browser-dialog-box.html)

[LabVIEW Advanced Settings dialog](labview-advanced-settings-window.html)

[LabVIEW Code Module Support for 64-bit TestStand](/csh?context=ts_tsfundamentals_64lvcodemodules)

[LabVIEW Data Types in TestStand](/csh?context=ts_tsref_labview_data_types)

[Migrating LabVIEW Code Modules from 32-bit TestStand to 64-bit TestStand](/csh?context=ts_tsfundamentals_64lvcodemodulesmigrate)

[Open File dialog box](open-file-dialog-box.html)

[Parameters Table Context Menu for Module Tabs](for-module-tabs-parameters-table-context-menu.html)

[Configure Property Node dialog box](configure-property-node-dialog-box.html)

[Select a VI dialog box](select-a-vi-dialog-box.html)

[Select a VI from a LabVIEW Packed Project Library dialog box](select-a-vi-from-a-labview-packed-project-lib.html)

[Select VI From LabVIEW Project dialog box](select-vi-from-labview-project-dialog-box.html)

[Simultaneously Supporting 32-bit TestStand and 64-bit TestStand](/csh?context=ts_tsfundamentals_64lvcodemodulestsbitness)

[Step Settings Pane](step-settings-pane.html)

[Update VI Calls dialog box](update-vi-lv-nxg-vi-calls-dialog-box.html)

[Updating Cluster Element Mapping](/csh?context=ts_tsref_labview_cluster_params_update)

[Using the $(Platform) Path Macro to Locate the Correct Code Module in 32-bit TestStand and 64-bit TestStand](/csh?context=ts_tsfundamentals_64platformmacro)

[Updating VI Dependencies](/csh?context=ts_tsref_updating_vi_dependencies)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/labview-nxg-adapter-configuration-dialog-box.html language=enus -->
## TOPIC 03847: LabVIEW NXG Adapter Configuration Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/labview-nxg-adapter-configuration-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/labview-nxg-adapter-configuration-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: To launch the LabVIEW NXG Adapter Configuration dialog box, which contains Select Which LabVIEW NXG Server to Use and Adapter Settings sections, select Configure»Adapters , select the LabVIEW NXG Adapter in the list control, and click Configure . If no LabVIEW NXG Runtime versions are installed, the

### LabVIEW NXG Adapter Configuration Dialog Box

Configure»Adapters

Configure

Note

#### Selecting a LabVIEW NXG Server

The Select Which LabVIEW NXG Server to Use section contains the following options for specifying the server or engine the LabVIEW NXG Adapter uses:

- LabVIEW NXG Run-time Engine 
 —Selecting this option runs VIs in the same process as TestStand to provide optimal performance when calling VIs. To execute VIs in the LabVIEW NXG Runtime, the VIs should have been built into a GLL.
- Active LabVIEW NXG Development System 
 —To use LabVIEW NXG to create or edit VIs or to debug VIs TestStand calls, you must select this option so VIs execute in the supported LabVIEW NXG development environment. You must have the LabVIEW NXG development system installed on the same computer as TestStand to use this option.

Note

Note

#### Adapter Settings

The Adapter Settings section contains the following options:

- Automatically Build Missing or Outdated GLLs at Start of Execution 
 —When enabled, TestStand validates that the GLL configured in a step matches the GLL path expected for the project and VI specified for the step. If the GLL path matches but it hasn't been built or the GLL present is stale (the binary doesn't match the code in the source files) at the time of execution, TestStand automatically triggers a build of the GLL before executing it. If the GLL doesn't match the expected GLL, TestStand returns an error.
 Note 
 TestStand must launch the LabVIEW NXG development system to perform the validations mentioned above and to build a GLL. By enabling this option, the LabVIEW NXG development system runs on the machine even though the LabVIEW NXG Adapter is set to use the LabVIEW NXG Run-time Engine.
 To optimize the performance of deployed systems, NI recommends that GLLs are pre-built and this option is disabled. Building large components can take time and this slows down execution.
- Validate GLL Path 
 —When enabled, TestStand validates that the GLL path configured in the step matches the GLL path specified in the Build Output Directory of the specified component in LabVIEW NXG. The project, component, and target specified in the step are used to determine the expected GLL path. Enabling the
 Automatically Build Missing GLL 
 option also enables the
 Validate the GLL Path 
 option.
- Disable Early Access Warning Dialog 
 —Enable this option to prevent the Early Access Dialog from being displayed when using LabVIEW NXG steps.

#### See Also

[Choose Code Template dialog box](choose-code-template-dialog-box.html)

[LabVIEW NXG Module tab](labview-nxg-module-tab.html)

Organizing LabVIEW NXG-Based TestStand Systems

[Specify Module dialog box](specify-module-tabs-and-dialog-boxes.html)

[TestStand Deployment Utility](teststand-deployment-utility.html)

Parent topic:

LabVIEW NXG Adapter

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/labview-nxg-adapter.html language=enus -->
## TOPIC 03848: LabVIEW NXG Adapter

- bundle_id: `teststand-api-reference`
- source_path: `tsref/labview-nxg-adapter.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/labview-nxg-adapter.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: The LabVIEW NXG Adapter is hidden by default. Use the Adapter Configuration dialog box to configure the LabVIEW NXG Adapter. The LabVIEW NXG Adapter provides advanced functionality for calling LabVIEW NXG VIs from TestStand. You can use the LabVIEW NXG Adapter to complete the following tasks: Call V

### LabVIEW NXG Adapter

Note

Adapter Configuration

- Call VIs with arbitrary connector panes.
- Call VIs that belong to a component in a LabVIEW NXG project.
- Configure and call LabVIEW NXG Property Nodes using I/O References.
- Run VIs using the LabVIEW NXG development system.
- Run VIs using the LabVIEW NXG Run-Time Engine.
- Create and edit VIs from TestStand.
- Debug VIs (step in/step out) from TestStand.

When you specify a module for a step, the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 displays the
 [LabVIEW NXG Module](labview-nxg-module-tab.html)
 tab and
 [TestStand User Interfaces](teststand-user-interfaces.html)
 launch the
 [Edit LabVIEW NXG VI Call](edit-labview-nxg-vi-call-dialog-box.html)
 dialog box.

The LabVIEW NXG Adapter can run VIs using the LabVIEW NXG development system or the LabVIEW NXG Run-Time Engine (RTE).

LabVIEW NXG Adapter Configuration

Note

#### See Also

[Adapter and Code Module Support for 64-bit TestStand](/csh?context=ts_tsfundamentals_64adapterscodemodules)

[Mapping Parameters](/csh?context=ts_tsref_parameters)

[Organizing LabVIEW-Based TestStand Systems](/csh?context=ts_tslabview_system)

Programming with the TestStand API in LabVIEW NXG

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/labview-nxg-advanced-settings-window.html language=enus -->
## TOPIC 03849: LabVIEW NXG Advanced Settings Window

- bundle_id: `teststand-api-reference`
- source_path: `tsref/labview-nxg-advanced-settings-window.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/labview-nxg-advanced-settings-window.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Click the Advanced Settings button on the LabVIEW NXG Module tab of the Step Settings pane to launch the LabVIEW NXG Advanced Settings window. In the LabVIEW NXG Advanced Settings window, you can configure the LabVIEW NXG adapter to always run the VI using the LabVIEW NXG Run-time engine. The LabVIE

### LabVIEW NXG Advanced Settings Window

Click the
 Advanced Settings
 button on the
 [LabVIEW NXG Module](labview-nxg-module-tab.html)
 tab of the Step Settings pane to launch the LabVIEW NXG Advanced Settings window.

In the LabVIEW NXG Advanced Settings window, you can configure the LabVIEW NXG adapter to always run the VI using the LabVIEW NXG Run-time engine.

The LabVIEW NXG Advanced Settings window contains the following:

- Always Run VI in LabVIEW NXG Run-Time Engine 
 —When you enable this option, you can always use a LabVIEW NXG Run-time engine (RTE) to run the VI, regardless of the global
 LabVIEW NXG Adapter 
 setting. Use this option when you do not want the global settings for the adapter to affect the tools and step types you create.

Parent topic:

LabVIEW NXG Module Tab

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/labview-nxg-data-types-in-teststand.html language=enus -->
## TOPIC 03850: LabVIEW NXG Data Types in TestStand

- bundle_id: `teststand-api-reference`
- source_path: `tsref/labview-nxg-data-types-in-teststand.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/labview-nxg-data-types-in-teststand.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: TestStand provides number, string, Boolean, and object reference built-in data types. TestStand also provides several standard named data types, including Path, Error, LabVIEWAnalogWaveform, and others. You can create container data types to hold any number of other data types. TestStand container d

### LabVIEW NXG Data Types in TestStand

TestStand provides number, string, Boolean, and object reference built-in data types. TestStand also provides several standard named data types, including Path, Error, LabVIEWAnalogWaveform, and others. You can create container data types to hold any number of other data types. TestStand container data types are analogous to LabVIEW NXG clusters. You can use references to external objects, such as ActiveX (Microsoft ActiveX) objects or VISA sessions, between different types of
 [code modules](/csh?context=ts_tsfundamentals_bldgblocks_codemodules)
 .

LabVIEW NXG includes a greater variety of built-in data types than TestStand does, so TestStand converts LabVIEW NXG data types in certain ways when calling VIs.

#### Converting LabVIEW NXG Numeric Representations

The following table shows how TestStand converts LabVIEW NXG numeric representations:

| LabVIEW NXG Numeric Representation | TestStand Data Type |
| --- | --- |
| Real number (U8, U16, U32, I8, I16, I32, SGL, or DBL) | Number |
| 64-bit integer numeric (I64) | Number {Signed 64-bit integer} |
| Unsigned 64-bit integer numeric (UI64) | Number {Unsigned 64-bit integer} |
| Fixed-point numeric | TestStand does not support calling VIs with fixed-point numeric indicators or controls. |
| Complex number (CSG or CDB) | Number TestStand maps each part of the complex number to separate TestStand Number properties. |

#### Converting LabVIEW NXG Controls and Indicators

The following table shows how TestStand converts LabVIEW NXG controls or indicators:

| LabVIEW NXG Control or Indicator | TestStand Data Type |
| --- | --- |
| Enum (U32, U16, or U8) | Enumeration |
| Ring control (Text Ring, Menu Ring, Text and Picture Ring, or Picture Ring) | Number |
| String | String |
| Path | Path or string |
| ActiveX Control or Automation Refnum | Object reference |
| Waveform | LabVIEWAnalogWaveform To create variables for I64 or UI64 Waveforms, you must create a new custom data type, because the representation of the Y element that corresponds to the standard LabVIEWAnalogWaveform data type is set to double-precision 64-bit floating-point. |
| Refnum (File I/O, VI, Menu, Queue, TCP connection, and so on) | Number {Signed 64-bit integer} You cannot use references to internal LabVIEW NXG objects inside TestStand or in other types of code modules. You can store only references to LabVIEW NXG objects in TestStand properties and then pass the properties to other VIs. |
| Timestamp | String TestStand converts the LabVIEW NXG Timestamp data type to a System Time data type and then to a string data type with the m/d/yyyy h:mm:ss.sss AM/PM format, where m Month as number without leading zero d Day of the month as number without leading zero yyyy Four-digit year h Hour of the day, without leading zero (12-hour clock) mm Minute of the hour, with leading zero ss Second of the minute, with leading zero sss Milliseconds of the second, with leading zero AM/PM AM or PM uppercase TestStand rounds fractions of a second to the nearest millisecond. |
| m | Month as number without leading zero |
| d | Day of the month as number without leading zero |
| yyyy | Four-digit year |
| h | Hour of the day, without leading zero (12-hour clock) |
| mm | Minute of the hour, with leading zero |
| ss | Second of the minute, with leading zero |
| sss | Milliseconds of the second, with leading zero |
| AM/PM | AM or PM uppercase |
| Error I/O | Error By default, when a VI uses the standard LabVIEW NXG error out cluster as an output parameter, TestStand automatically passes that value into the Step.Result.Error property for the step. You can also update the value manually. If an error occurs during execution of the VI and the error out cluster is passed to Step.Result.Error , TestStand launches the Run-Time Error dialog box by default. |
| Array of x | Array of TestStand ( x ) |
| Variant | Any TestStand data type Note Passing LabVIEW NXG I/O references (DAQmx Task Name, DAQmx Channel Name, VISA Resource Name, etc.) through TestStand as a variant is not supported. Use the LabVIEWIOControl instead. |
| Cluster | Container |
| I/O controls (DAQmx Task Name, DAQmx Channel Name, VISA Resource Name) | LabVIEWIOControl |

Parent topic:

LabVIEW NXG Adapter

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/labview-nxg-module-tab.html language=enus -->
## TOPIC 03851: LabVIEW NXG Module Tab

- bundle_id: `teststand-api-reference`
- source_path: `tsref/labview-nxg-module-tab.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/labview-nxg-module-tab.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Insert a step configured to use the LabVIEW NXG Adapter and select Specify Module or Step Settings from the context menu to display the LabVIEW NXG Module tab in the TestStand Sequence Editor . You can use the LabVIEW NXG Module tab to complete the following tasks: Select the LabVIEW NXG project tha

### LabVIEW NXG Module Tab

Insert a step configured to use the LabVIEW NXG Adapter and select
 Specify Module
 or
 Step Settings
 from the context menu to display the LabVIEW NXG Module tab in the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 .

You can use the LabVIEW NXG Module tab to complete the following tasks:

- Select the LabVIEW NXG project that refers to the VI if the step will execute in the LabVIEW NXG Development System
- Select the GLL that contains the VI if the step will execute in the LabVIEW NXG Runtime
- Select the VI the step executes
- Create and edit a VI or a LabVIEW NXG project in LabVIEW NXG
- Specify whether LabVIEW NXG shows the front panel of the VI when TestStand calls the VI in the LabVIEW NXG Run-time Engine

Note

1. Module configured to run in the LabVIEW NXG Development System 
 —The Step settings pane for a LabVIEW NXG module uses this view when the
 Always run in LabVIEW NXG Runtime Engine 
 option is disabled in the
 Advanced Settings Window 
 and when the LabVIEW NXG Development System is selected as the Server for execution in the
 LabVIEW NXG Adapter Configuration dialog box 
 . This view is used to configure the module settings that are required to execute a VI in the context of a LabVIEW NXG project in the Development System.
 This view has the following options: 
 
 Note 
 To show the Front Panel of a VI that is executing in the LabVIEW NXG Development System, choose the
 Separate Window
 option under the
 Run Behavior
 options of the VI's Panel properties. When VIs with
 Separate Window
 enabled are executed from TestStand, their Front Panels are displayed in front of TestStand's main window.
  - Project Path 
 —The path of the LabVIEW NXG project the step uses. The control contains a most recently used (MRU) list of the last ten selected LabVIEW NXG projects. Every LabVIEW NXG VI must be contained in a project so specifying the project is mandatory, unlike for LabVIEW modules.
  - Browse for LabVIEW NXG Project 
 —Launches the Select the Step's LabVIEW NXG Project File dialog box, which you can use to browse for the LabVIEW NXG project (
 .lvproject 
 ) file to open.
  - Create LabVIEW NXG Project 
 —Creates an empty LabVIEW NXG project. If the LabVIEW NXG project you specify does not already exist, the LabVIEW NXG Adapter creates it. If the file already exists, the LabVIEW NXG Adapter prompts you to overwrite the existing file.
  - Module Name 
 —The
 Module Qualified Name 
 of the VI the step calls. The control contains an MRU list of the last ten VIs selected for the configured project.
  - Browse for VI 
 —Launches the
 Select Module from Project 
 dialog box, which you can use to select a VI from the project that the step is configured to use.
  - Configure Settings For Property Node 
 —Displays the Configure Property Node (link to help topic) dialog, in which you can specify the I/O Reference type and select properties for the Property Node call. This option is only enabled if a valid project is specified in the Project Path.
  - Undock/Dock LabVIEW VI Help 
 —Attaches or detaches the VI Help panel from the Module tab.
  - VI Description 
 —Displays the description of the VI from the VI Description window in the Document tab of the LabVIEW NXG VI Properties pane.
  - Parameter Description 
 —Displays the description of the parameter selected in the Parameter Table. This is the description available in the Description window in the Items Tab of a LabVIEW NXG VI's properties pane, when the corresponding control or indicator is selected.
2. Module configured to run in the LabVIEW NXG Runtime Engine 
 —The Step settings pane for a LabVIEW NXG module uses this view when the
 Always run in LabVIEW NXG Runtime Engine 
 option is enabled in the
 Advanced Settings window 
 or when the LabVIEW NXG Runtime Engine is selected as the Server for execution in the
 LabVIEW NXG Adapter Configuration 
 dialog box. The following options are used to configure the module to execute a VI from a GLL in the LabVIEW NXG Runtime Engine:
  - GLL Path 
 —The path of GLL the step uses. The control contains a most recently used (MRU) list of the last ten selected GLLs.
  - Browse for GLL 
 —Launches the
 Select the GLL for the Step 
 dialog box which you can use to browse for the GLL (
 .gll 
 ) to open.
  - GLL Source code 
 —This option launches the
 GLL Source Code Files Dialog 
 where the user can specify the project that contains the component used to build the GLL configured in the step.
  - Module Name 
 —The
 Module Qualified Name 
 of the VI the step calls. The control contains an MRU list of the last ten VIs selected for the configured GLL.
  - Browse for VI 
 —Launches the
 Select Module from GLL 
 dialog box, in which you can select a VI from the GLL that the step is configured to use.
  - Show VI Front Panel 
 —When you enable this option, the front panel of the VI opens when the LabVIEW NXG Adapter calls the VI and closes when it is done executing. The button has two modes:
    - Show Front Panel Modal 
 —The Front Panel is shown as a dialog box that is modal to TestStand's main window.
    - Show Front Panel Modeless 
 —The Front Panel is shown as a dialog box that is not modal to TestStand's main window. You can still interact with TestStand while this dialog box is shown.
3. Some options are common to both views:
  - Edit LabVIEW NXG Project 
 —Edits the configured LabVIEW NXG project, if any.
  - Advanced Settings 
 —Launches the
 LabVIEW NXG Advanced Settings window 
 , in which you can configure a LabVIEW NXG step to execute a VI with the LabVIEW NXG Run-time engine.
  - Reload VI Prototype 
 —Allows the user to refresh the parameter information of the VI.
  - Create VI 
 —Displays the Create Module dialog box. The Create Module dialog box allows you to specify the name and location of the new VI in the project. When you hit OK on the dialog, TestStand creates a code shell for the VI specified and adds it to the project at the specified location. If a VI with the same path already exists, the LabVIEW NXG Adapter prompts you to overwrite the existing file. If a VI code template file exists for the step type you are using for the step, the LabVIEW NXG Adapter uses the template to create the new VI. When configuring a step using the Runtime Engine, the project and Module Qualified Name should be specified for this option to work correctly.
  - Edit VI 
 —Edits an existing VI, opening it in the LabVIEW NXG project. When configuring a step using the Runtime Engine, the project and Module Qualified Name should be specified for this option to work correctly.
  - VI Parameter Table 
 —Contains information about each control or indicator wired to the connector pane of the VI. These are the parameters of the VI.
    - Parameter Name 
 —Label text of the control or indicator.
 Note 
 Parameters with attributes include an
 Edit Attributes
 button in the Name column of the VI Parameter Table. You can edit attributes for fields of containers and elements of arrays. TestStand associates parameter attributes with the module parameter, which TestStand stores with the step configuration information, not with the parameter value that TestStand passes to the module. Right-click an item in the VI Parameter Table to access the
 [VI Parameter Table](for-module-tabs-parameters-table-context-menu.html)
 context menu, from which you can launch the
 [Attributes](attributes-dialog-box.html)
 dialog box.
    - Type 
 —TestStand
 equivalent data type 
 for the control or indicator.
 For one-dimensional arrays, you can specify an expression value for the entire array, or you can specify values for each element of the array. Use the plus (
 + 
 ) buttons to insert a new element in the array, and the minus (
 - 
 ) buttons to remove specific elements from the array.
When you select
 Binary String 
 in the Type column of the VI Parameter Table on the LabVIEW NXG Module tab to store a LabVIEW NXG string that contains binary data in a TestStand property. TestStand compresses the binary data, encodes the compressed data, and stores the compressed data using only printable ASCII characters. To pass a compressed string to a VI, select
 Binary String 
 in the Type column. TestStand unencodes and decompresses the binary data the string stores before passing it to the VI.
 Note 
 To retrieve the raw binary data stored in a string variable in TestStand, call the
 
 [PropertyObject.GetValBinary](../tsapiref/propertyobject-getvalbinary.html)
 method of the TestStand API. See the
 [Retrieving Binary String Values from Reports and Databases](/csh?context=ts_tsreports_retrievingbinarystrings)
 topic for more information about retrieving binary data from string values.
    - Create/Update Custom Data Type 
 —Launches the
 Create/Update Custom Data Type from Cluster 
 dialog box, in which you can configure a new custom data type or update an existing custom data type.
    - Apply Cluster Passing Changes 
 —Updates a VI parameter that contains a subproperty that no longer maps to the correct cluster element. You can use this button to update the parameter and automatically map the subproperty to the correct cluster element.
This button might also appear when TestStand cannot
 automatically map a subproperty to the correct element 
 and the Value column of the VI Parameter Table contains a '??? <Unknown Value>' error for the subproperty.
  - In/Out 
 —Specifies whether the parameter is an input (control on the VI front panel wired to the connector pane) or an output (indicator on the VI front panel wired to the connector pane).
  - Log 
 —When you enable this option, the step logs the parameter as an additional result. Enabling this option is equivalent to using the checkbox next to the additional result name on the
 Additional Results panel 
 of the
 Properties 
 tab of the
 Step Settings pane 
 .
  - Default 
 —When you enable this option, TestStand uses the default value of the control for the parameter, cluster element, or array element. This option is not available when the terminal of the VI is marked as Required.
  - Value 
 —A TestStand expression. For input parameters, TestStand passes the value of this expression to the VI unless you place a checkmark in the option in the Default column. For output parameters, TestStand stores the data the VI outputs in the location this expression specifies. To help you enter an expression in the Value column, click the
 Expression Browse 
 button to launch the
 Expression Browser 
 dialog box. For enumerated types, a combo box displays all valid values for the type. You can also use an expression with an enumerated type.

#### Automatically populating the GLL Path

LabVIEW NXG specifies the output directory of a GLL that is the build output of a component for a specific target. This implies that if a project and a Module Qualified Name are specified in a LabVIEW NXG module, then there is a definitive GLL path that must be used in the step. 
The GLL path configured in a LabVIEW NXG module must match the path expected by LabVIEW NXG based on the project and the Module Qualified Name (component and target properties). A step that is configured with a GLL that is different from this expected path returns an error.

Note

Automatically Build Missing GLLs at the Start of Execution

Validate GLL Path

LabVIEW NXG Adapter Configuration Dialog

Note

#### See Also

[Attributes dialog box](attributes-dialog-box.html)

[Calling LabVIEW NXG property Nodes from TestStand](/csh?context=ts_tslabview_property_node)

[Create/Update Custom Data Type from Cluster dialog box](create-update-custom-data-type-from-cluster-d.html)

[Effectively Using LabVIEW NXG with TestStand](../tslabviewnxg/effectively-using-labview-nxg-with-teststand.html)

[Expression Browser dialog box](expression-browser-dialog-box.html)

[LabVIEW NXG Advanced Settings Window](labview-nxg-advanced-settings-window.html)

[LabVIEW NXG Data Types in TestStand](/csh?context=ts_tsref_labview_data_types)

[Open File dialog box](open-file-dialog-box.html)

[Parameters Table Context Menu for Module Tabs](for-module-tabs-parameters-table-context-menu.html)

[Configure Property Node dialog box](configure-property-node-dialog-box.html)

[Select Module from Project dialog box](select-module-from-project-dialog-box.html)

[Select Module from DLL dialog box](select-module-from-gll-dialog-box.html)

[Step Settings Pane](step-settings-pane.html)

[Update VI/LV NXG VI Calls dialog box](update-vi-lv-nxg-vi-calls-dialog-box.html)

[Updating Cluster Element Mapping](/csh?context=ts_tsref_labview_cluster_params_update)

Parent topic:

LabVIEW NXG Adapter

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/labview-nxg-vi-help-window.html language=enus -->
## TOPIC 03852: LabVIEW NXG VI Help Window

- bundle_id: `teststand-api-reference`
- source_path: `tsref/labview-nxg-vi-help-window.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/labview-nxg-vi-help-window.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: The LabVIEW NXG Module tab displays the context help as a panel on the tab or as a floating window. Click Undock/Dock LabVIEW NXG VI Help to attach or detach the context help from the LabVIEW NXG Module tab. The help window displays the Parameter description of the parameter that is selected in the

### LabVIEW NXG VI Help Window

The
 [LabVIEW NXG Module](labview-nxg-module-tab.html)
 tab displays the context help as a panel on the tab or as a floating window. Click
 Undock/Dock LabVIEW NXG VI Help
 to attach or detach the context help from the LabVIEW NXG Module tab.

The help window displays the Parameter description of the parameter that is selected in the VI Parameter Table. The parameter description is the content shown in the LabVIEW NXG Context Help window when hovering over a control or indicator.

Parent topic:

LabVIEW NXG Module Tab

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/labview-utility-step-types.html language=enus -->
## TOPIC 03853: LabVIEW Utility Step Types

- bundle_id: `teststand-api-reference`
- source_path: `tsref/labview-utility-step-types.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/labview-utility-step-types.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use one of the following LabVIEW Utility step types to simplify running a VI on a remote computer and to deploy or undeploy shared variables. Check Remote System Status Run VI Asynchronously Deploy Library To edit a LabVIEW utility step type in the TestStand Sequence Editor , use the edit tabs on th

### LabVIEW Utility Step Types

Use one of the following LabVIEW Utility step types to simplify running a VI on a remote computer and to deploy or undeploy shared variables.

- Check Remote System Status
- Run VI Asynchronously
- Deploy Library

To edit a LabVIEW utility step type in the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 , use the edit tabs on the
 [Step Settings](step-settings-pane.html)
 pane. The tabs available update based on the type of step you select.

To edit a LabVIEW utility step type when you use a
 [TestStand User Interface](teststand-user-interfaces.html)
 , select
 Edit
 from the context menu for the step or click
 Configure
 <Step Name>
 on the
 [General](general-tab-step-properties-dialog-box.html)
 tab of the
 [Step Properties](step-properties-dialog-box.html)
 dialog box.

#### See Also

[Calling VIs on Remote Computers](/csh?context=ts_tslabview_remote)

[Step Properties dialog box](step-properties-dialog-box.html)

[Step Settings Pane](step-settings-pane.html)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/labview-utility-step-types2.html language=enus -->
## TOPIC 03854: LabVIEW Utility Step Types

- bundle_id: `teststand-api-reference`
- source_path: `tsref/labview-utility-step-types2.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/labview-utility-step-types2.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: LabVIEW NXG Utility step types include: Run LabVIEW NXG VI Asynchronously To edit a LabVIEW NXG utility step type in the TestStand Sequence Editor , use the edit tabs on the Step Settings pane. The tabs available update based on the type of step you select. To edit a LabVIEW NXG utility step type wh

### LabVIEW Utility Step Types

LabVIEW NXG Utility step types include:

- Run LabVIEW NXG VI Asynchronously

To edit a LabVIEW NXG utility step type in the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 , use the edit tabs on the
 [Step Settings](step-settings-pane.html)
 pane. The tabs available update based on the type of step you select.

To edit a LabVIEW NXG utility step type when you use a
 [TestStand User Interface](teststand-user-interfaces.html)
 , select
 Edit
 from the context menu for the step or click
 Configure
 <Step Name>
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

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/labview-vi-help-window.html language=enus -->
## TOPIC 03855: LabVIEW VI Help Window

- bundle_id: `teststand-api-reference`
- source_path: `tsref/labview-vi-help-window.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/labview-vi-help-window.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Displays the context help image of the VI as shown in the LabVIEW Context Help window. The LabVIEW Module tab displays the context help as a panel on the tab or as a floating window. Click Undock/Dock LabVIEW VI Help to attach or detach the context help from the LabVIEW Module tab. When you click on

### LabVIEW VI Help Window

Displays the context help image of the VI as shown in the LabVIEW Context Help window. The
 [LabVIEW Module](labview-module-tab.html)
 tab displays the context help as a panel on the tab or as a floating window. Click
 Undock/Dock LabVIEW VI Help
 to attach or detach the context help from the LabVIEW Module tab.

When you click on any label or connector inside the VI icon, the parameter control automatically selects that parameter on the LabVIEW Module tab. The connector pane also blinks to indicate which parameter is selected on the LabVIEW Module tab.

#### See Also

[Effectively Using LabVIEW with TestStand](/csh?context=ts_10208)

[LabVIEW Module Tab](labview-module-tab.html)

Parent topic:

LabVIEW Module Tab

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/labview-vi-options-dialog-box.html language=enus -->
## TOPIC 03856: LabVIEW VI Options Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/labview-vi-options-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/labview-vi-options-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Launch the TestStand Deployment Utility and select LabVIEW Options on the Distributed Files tab to launch the LabVIEW VI Options dialog box. The LabVIEW VI Options dialog box contains the following options: LabVIEW Options Tab General LabVIEW VI Options Remove Block Diagrams —When you enable this op

### LabVIEW VI Options Dialog Box

Launch the
 [TestStand Deployment Utility](teststand-deployment-utility.html)
 and select
 LabVIEW Options
 on the
 [Distributed Files](distributed-files-tab-teststand-deployment-ut.html)
 tab to launch the LabVIEW VI Options dialog box.

The LabVIEW VI Options dialog box contains the following options:

#### LabVIEW Options Tab

- General LabVIEW VI Options
  - Remove Block Diagrams 
 —When you enable this option, the deployment utility removes the block diagrams of VIs in the deployment to prevent users from viewing and editing the block diagrams. If you enable this option, you cannot also enable the Apply New Password option. You can remove block diagrams for VIs that are part of XControls.
  - Apply New Password 
 —Enable this control to lock VIs to prevent editing. Applying a password is incompatible with removing VI diagrams. This option is disabled when you enable the Remove VI Diagrams option.
  - Password 
 —Launches a dialog box in which you can set the password to apply. VIs that already have a password retain their original password. When you lock VIs with a password, you cannot edit them without entering the password.
  - Check for Broken VIs 
 —When you enable this option, the deployment utility checks for broken VIs during analysis and after building the deployable image. This option is disabled by default to improve performance. Enable this option when you want to debug VI errors.
 Note 
 When you deselect a sequence file in the Distributed Files control of the Distributed Files tab to exclude the sequence file from the deployment, the VIs the sequence file calls remain in the deployment. The deployment utility does not confirm whether the VIs are broken during analysis. However, the deployment utility always checks all VIs in a TestStand project during an analysis to determine whether the VIs are broken after a build.
 The deployment utility attempts to find all the dependencies of VIs before it checks for broken VIs. If the utility does not find one or more dependencies of the VIs, the utility reports those dependencies as missing and does not check for broken VIs, even when the
 Check for Broken VIs
 option is enabled. National Instruments recommends that before you attempt to deploy again after finding missing VIs, you mass compile the VIs or run the TestStand Sequence Analyzer to identify possible issues with the deployment.
  - Include Packed Library Source Files Specified in Steps 
 —Include the source and binary files you specify in the LabVIEW
 Override Module Settings 
 window. This option is only enabled if the Output VIs to a Packed Project Library option is disabled
  - Rebuild Packed Libraries During Build 
 —Rebuild packed libraries using source files specified in the LabVIEW
 Override Module Settings 
 window. When this option is enabled, the TSDU analysis and build process may be slower if large packed libraries are included in the deployment. This option is enabled when the Include Packed Library Source Files Specified in Steps setting is enabled
  - SubVI Location (end path with .LLB to place files in a VI library) 
 —The location to save subVIs. This location must be a relative path.
 If the specified path uses the
 .llb 
 extension, the location is a LabVIEW VI library. Otherwise, the location is a directory.
  - Include Module Files for LabVIEW Substeps 
 —If enabled, the TestStand Deployment Utility detects and includes in the deployment any LabVIEW code modules specified in substeps of custom step types used by deployed sequence files. Code modules for substeps of NI step types are not included regardless of this setting. If you select the
 Output VIs to a Packed Project Library 
 option, this option is disabled, since building substep VIs into a packed library would require changes to the substep module path. In this case, NI recommends using a separate packed project library to contain substep VIs.
- Packed Project Library Options
  - Output VIs to Packed Project Library 
 —When you enable this option, the deployment utility
 builds a LabVIEW packed project library 
 for the VIs you deploy.
    - Enable Debugging 
 —When you enable this option, the deployment utility builds a LabVIEW packed project library with debugging information.
  - Options 
 —Launches the
 Packed Project Library Options 
 dialog box, in which you can configure options for how the deployment utility builds LabVIEW packed project libraries, such as the base library name, versioning information, descriptive information about the build, and source file options.
  - Copy files from vi.lib before build 
 —Ensures that a copy of all dependencies in
 vi.lib 
 are copied into the source distribution, which TestStand Deployment Utility uses to build the Packed Library.
  - Copy files from user.lib before build 
 —Ensures that a copy of all dependencies in
 user.lib 
 are copied into the source distribution, which TestStand Deployment Utility uses to build the Packed Library.
  - Copy files from instr.lib before build 
 —Ensures that a copy of all dependencies in
 instr.lib 
 are copied into the source distribution, which TestStand Deployment Utility uses to build the Packed Library.
- Exclusions 
 —Contains the following options for
 excluding certain files 
 from the deployment:
  - Exclude Files from VI lib 
 —Excludes all files in the
 vi.lib 
 directory from the deployment.
  - Exclude Files from User lib 
 —Excludes all files in the
 user.lib 
 directory from the deployment.
  - Exclude Files from Instr lib 
 —Excludes all files in the
 instr.lib 
 directory from the deployment.
  - Remove unused members of project libraries 
 —Removes unused project library members during the build process. If you enable this option, LabVIEW includes only VIs from the library you call directly from the block diagram. Enabling this option reduces the application size, since LabVIEW does not include the other VIs referenced by the same project library unless the VIs are referenced by other VIs that are included in the deployment.
  - Modify project library file after removing unused members 
 —If you remove unused members of the project library, enable this option to direct LabVIEW to modify the library so that the library file does not refer to the removed members. If you do not modify the project library, the deployment may take longer to build.
  - Exclude Dependent Shared Libraries (LabVIEW 2014 and Later) 
 —Reduces the overall number of files in a deployment. Enabling this option limits the number of shared libraries that LabVIEW copies. When you create a deployment and then link to a file in that deployment from another deployment, LabVIEW traditionally copies the linked file. When this option is enabled, LabVIEW retains the links relative to the original files instead of copying the files during the build.
  - Exclude Dependent Packed Libraries (LabVIEW 2014 and Later) 
 —When you enable this option, LabVIEW excludes copies of dependent packed project libraries to which you link from other deployments. To exclude dependent packed project library files, LabVIEW retains the links relative to the original dependent packed project libraries instead of copying those files during the build. For example, if you create a deployment and then a subsequent deployment, you can relatively link the subsequent deployment to a file in the first deployment. If you leave this option disabled, LabVIEW copies the dependent packed library file to which you linked instead of retaining the relative link to that file.
- Optimizations 
 —Contains the following options for optimizing files in the deployment:
  - Remove Unused VI Components 
 —Removes unused polymorphic VI instances code modules reference. This option does not remove any files that are directly referenced in a sequence or workspace project.
 Note 
 Enabling the Remove Unused VI Components option disables certain editing and debugging options, such as wiring a new type to a polymorphic VI or making type changes across several VIs by editing a type definition.
  - Consolidate Files Shared By Projects 
 —When you enable this option, the deployment utility consolidates all files in LabVIEW projects into a single, merged project. This consolidation increases build speed and decreases disk usage for multiple projects that share common subVIs by making a single source distribution for every project. This optimization is not always possible because two projects might compile the same source VI differently, which can result in slower build times.
 If the deployment utility cannot consolidate all projects, the utility returns a warning that explains why consolidation is not possible and builds the distribution without consolidating the projects.
 When you disable this option, the deployment utility builds one LabVIEW source distribution
 
 for each LabVIEW project. If multiple LabVIEW projects share files, the deployment utility includes multiple copies of the shared files.
  - Enable SSE2 Optimizations 
 —When you enable this option, the deployment utility uses SSE2 optimizations to compile VIs, which can improve execution speed. This option is enabled by default. Do not enable this option if you are using processors that do not support the SSE2 instruction set. Refer to the
 LabVIEW Help 
 for more information about which processors and National Instruments devices support SSE2.

#### LabVIEW NXG Options Tab

- General LabVIEW NXG VI Options
  - Include LabVIEW NXG Source Files 
 —When you enable this option, the LabVIEW NXG projects referenced by your sequence files are included in the deployment. All source files referenced by the projects are included. Enable this option if you want to view or edit LabVIEW NXG source code on a deployment target. If this option is disabled, only GLL files referenced by sequence files are included in the deployment. After changing this setting, click
 Ananlyze Source Files 
 to update the included files.
  - Include Module Files for LabVIEW NXG Substeps 
 —If enabled, the TestStand Deployment Utility detects and includes in the deployment any LabVIEW NXG code modules specified in substeps of custom step types used by deployed sequence files. Code modules for substeps of NI step types are not included regardless of this setting.

#### See Also

[Deploying TestStand Systems](/csh?context=ts_10203)

[Effectively Using LabVIEW with TestStand](/csh?context=ts_10208)

[TestStand Deployment Utility](teststand-deployment-utility.html)

Parent topic:

Distributed Files Tab - TestStand Deployment Utility

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/labwindows-cvi-adapter-configuration-dialog-b.html language=enus -->
## TOPIC 03857: LabWindows/CVI Adapter Configuration Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/labwindows-cvi-adapter-configuration-dialog-b.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/labwindows-cvi-adapter-configuration-dialog-b.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Select Configure»Adapters , select the LabWindows Adapter in the list control, and click Configure to launch the LabWindows/CVI Adapter Configuration dialog box. The LabWindows/CVI Adapter Configuration dialog box contains the following options: Show Function Arguments in Step Description —When you

### LabWindows/CVI Adapter Configuration Dialog Box

Select
 Configure»Adapters
 , select the LabWindows Adapter in the list control, and click
 Configure
 to launch the LabWindows/CVI Adapter Configuration dialog box.

The LabWindows/CVI Adapter Configuration dialog box contains the following options:

- Show Function Arguments in Step Description 
 —When you enable this option, the description for a step in the
 TestStand Sequence Editor 
 and the
 TestStand User Interfaces 
 include the parameters with the function. When you disable the option, the description displays only the function and module name.
- Default Struct Packing 
 —Specifies how the LabWindows/CVI Adapter packs
 structure parameters 
 it passes. Set the packing options to match the default for structure packing in the application development environment. You can select 1-, 2-, 4-, 8-, or 16-byte boundaries.
 Note 
 The compatibility mode of the LabWindows/CVI development environment you use to create DLLs determines the choice for the structure packing value, as follows:
 For LabWindows/CVI, the default structure packing can be 1- or 8-byte. For example, in Microsoft Visual C++ compatibility mode, LabWindows/CVI has a default of 8-byte packing.
 Visual C++ and Symantec C++ have a default of 8-byte packing.
 LabVIEW, Borland C++, and Watcom C++ have a default of 1-byte packing.

The
 [Step Execution section](/csh?context=ts_tsref_cvimodselectingwheretoexecute)
 contains the following options:

- Execute Steps in an
 External Instance 
 of CVI—Specifies which project the LabWindows/CVI Adapter uses to run
 code modules 
 .
- Pathname of the LabWindows/CVI Project Containing the Execution Server 
 —The pathname of the LabWindows/CVI project file the LabWindows/CVI Adapter uses to run steps out-of-process.
- Execute Step
 In-Process 
 (CVI is NOT Required for This Mode)—This is the fastest mode for running steps. However, you cannot debug
 .c 
 files in this mode. For a
 .c 
 file, TestStand locates the corresponding
 .obj 
 file and uses it in the place of the
 .c 
 file.
 You can debug DLLs in this mode when you launch this application from the DLL development environment. Refer to the
 LabWindows/CVI Help
 for more information.
- Code Template Policy 
 —Specify the code module templates to use during code creation. The following options are available:
  - Allow Only New Templates 
 —Only searches for new code module templates.
 When you select this option, the Code Template ring control on the
 LabWindows/CVI Module 
 tab contains only the new code templates associated with the step type.
  - Allow Only Legacy Templates 
 —Only searches for legacy code module templates, which are files you can call from previous versions of TestStand.
 When you select this option, the Code Template ring control on the LabWindows/CVI Module tab contains only the legacy code templates associated with the step type.
  - Allow New and Legacy Templates 
 —Searches for both new and legacy code module templates.
 When you select this option, the Code Template ring control on the LabWindows/CVI Module tab contains all the code templates associated with the step type.

#### See Also

[Calling Legacy LabWindows/CVI Code Modules](/csh?context=ts_tsref_lwcvicalllegacycodemods)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/labwindows-cvi-module-tab.html language=enus -->
## TOPIC 03858: LabWindows/CVI Module Tab

- bundle_id: `teststand-api-reference`
- source_path: `tsref/labwindows-cvi-module-tab.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/labwindows-cvi-module-tab.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Insert a step configured to use the LabWindows/CVI Adapter and select Specify Module or Step Settings from the context menu to display the LabWindows/CVI Module tab in the TestStand Sequence Editor . You can use the LabWindows/CVI Module tab to specify the function prototype, which includes the data

### LabWindows/CVI Module Tab

Insert a step configured to use the LabWindows/CVI Adapter and select
 Specify Module
 or
 Step Settings
 from the context menu to display the LabWindows/CVI Module tab in the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 .

You can use the LabWindows/CVI Module tab to specify the function prototype, which includes the data type of each parameter and the values to pass for each parameter. The Parameters Table control shows all the available parameters for the function call and an entry for the return value. You can insert, remove, or rearrange the order of the parameters.

code module

Note

The LabWindows/CVI Module tab contains the following options:

- Module 
 —The pathname of the code module file that contains the function the step calls. You can specify an absolute or relative pathname for the module file. Relative pathnames are relative to the TestStand
 search directory paths 
 . Use the
 Edit Search Directories 
 dialog box to customize the search directory paths.
With the exception of
 custom user interfaces 
 , you cannot use a
 side-by-side version of the LabWindows/CVI Run-Time Engine (RTE) 
 with
 .lib 
 ,
 .obj 
 , or
 .c 
 code modules. These code modules always use the default LabWindows/CVI RTE even when the module is an import library for a DLL that uses the side-by-side version of the LabWindows/CVI RTE. To call a DLL code module that uses the side-by-side version of the LabWindows/CVI RTE in this case, specify the code module with the path of the DLL, not the path of the import library.
If you select a debug
 .dll 
 built by LabWindows CVI 2019 or later, then the CVI Project File to Open on the CVI Source Code Files Window updates to the LabWindows/CVI
 .prj 
 file that was used to build the selected
 .dll 
 .
- Reload Prototype 
 —Requests that the LabWindows/CVI Adapter query the code module for prototype information for the currently selected function. If a DLL contains export information or a type library or there is a type library with the same name as the DLL file and the function is defined in the type library, TestStand uses the prototype.
 Note 
 If you create a DLL using LabWindows/CVI 7.1 or later, TestStand can read the prototype information for the currently selected function without the use of a type library. 
 If the code module is a debug
 .dll 
 built by LabWindows/CVI 2019 or later, then the CVI Project File to Open and the Source File that Contains Function on the CVI Source Code Files Window updates to the LabWindows/CVI
 .prj 
 and
 .c 
 that were used to build the
 .dll 
 .
- Always Run In Process 
 —Specifies whether the step always runs in-process even if the LabWindows/CVI Adapter is
 configured to run out-of-process 
 . Use this option when you do not want the global settings for the adapter to affect the tools and step types you create for use with the LabWindows/CVI Adapter.
- Function 
 —Selects the function in the code module the step calls. The LabWindows/CVI Adapter attempts to read the code module file and find the names of all functions. When the code module type is not a C source file, the LabWindows/CVI Adapter populates the Function Name ring control with the names of all the functions the code module contains.
 If you select a debug
 .dll 
 built by LabWindows/CVI 2019 or later as the Module, then the Source File that Contains Function on the CVI Source Code Files Window updates to the
 .c 
 file path that was used to build the
 .dll 
 .
- Code Template 
 —The
 code template 
 to which the module call adheres. TestStand lists the code templates the step type defines. The Code Template control contains the following default options:
  - None 
 —Specifies if the module call does not adhere to a prototype of any code template. When you select this option, the
 New 
 and
 Delete 
 buttons in the Parameters Table are enabled.
  - Default template for LabWindows/CVI 
 —Specifies whether the module adheres to the default template for the LabWindows/CVI adapter.
  - Legacy default template 
 —Specifies whether the module adheres to the legacy prototype of the LabWindows/CVI Adapter. TestStand includes this option when you enable legacy templates on the LabWindows/CVI Adapter Configuration dialog box.
- Parameters Table 
 —Shows all of the available parameters for the function call and an entry for the return value. The Parameters Table control contains the following columns:
 
 When you select a parameter in the Parameters Table control, the Parameter Details Table control contains the specific details about the parameter. The data type (Numeric, String, Enumeration, Object, C Struct, or Array) determines the information required for a parameter. As an alternative to specifying the function name and the parameter values, you can use the Function Call control to directly edit the function name and all the function arguments at once. To insert or remove parameters, click
 New 
 or
 Delete 
 . To rearrange the parameter order, select the parameter you want to move and click
 Move Up 
 or
 Move Down 
 . You must select the
 None 
 code template before attempting to insert, remove, or rearrange parameters.
  - Parameter Name 
 —A symbolic name for the parameter.
 Note 
 Parameters with attributes include an
 Edit Attributes
 button in the Name column of the Parameters Table. TestStand associates parameter attributes with the module parameter, which TestStand stores with the step configuration information, not with the parameter value that TestStand passes to the module. Right-click an item in the Parameters Table to access the
 [Parameters Table](for-module-tabs-parameters-table-context-menu.html)
 context menu, from which you can launch the
 [Attributes](attributes-dialog-box.html)
 dialog box.
  - Description 
 —The short description of the parameter type using ANSI C syntax.
  - Create/Update Custom Data Type 
 —Launches the
 Create/Update Custom Data Type from Struct 
 dialog box, in which you can configure a new custom data type or update an existing custom data type.
  - Log 
 —When you enable this option, the step logs the parameter as an additional result. Enabling this option is equivalent to using the checkbox next to the additional result name on the
 Additional Results panel 
 of the
 Properties 
 tab of the
 Step Settings 
 pane. For in/out parameters, enabling this option enables the [In] parameter and the [Out] parameter on the Additional Results panel. This option is indeterminate for in/out parameters if you specify to log only the [In] parameter value or only the [Out] parameter value. If this option is indeterminate, a tooltip specifies whether the Additional Results panel specifies to log the [In] parameter value or the [Out] parameter value.
  - Value Expression 
 —The argument expression to pass.
- Parameter Details Table 
 —The data type of each parameter and additional information according to each parameter type. The Category ring control specifies a group of data types to list in the Type ring control. The categories include:
 Numeric 
 ,
 String 
 ,
 Enumeration 
 ,
 Object 
 ,
 C Struct 
 ,
 Arrays 
 ,
 TestData 
 ,
 TestError 
 , and
 Pointer/Handle 
 . The Type control specifies the data type of the function parameter.
 Note 
 The LabWindows/CVI Adapter supports numeric return values, which includes Boolean, void*, and void.
- Create Code 
 —Creates the source code shell for the function.
 If the source file you specify does not already exist, the LabWindows/CVI Adapter creates it. If the file already exists, the LabWindows/CVI Adapter dialog box opens and gives you the choice of replacing the current function or adding the new function shell above the current function. If a code template file exists for the step type you use for the step, the LabWindows/CVI Adapter uses the template to create the shell of the new function. If the project file you specify does not already exist, the LabWindows/CVI Adapter creates a new project file and adds the source file to it.
- Edit Code 
 —Edits the source code for the function. The LabWindows/CVI Adapter launches a copy of LabWindows/CVI and opens the source file. When you specify a project file in the Source Code tab, the LabWindows/CVI Adapter also opens the project in LabWindows/CVI.
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
 —Checks for any conflicts between the source code and the parameter information on the Module tab.
- Source Code Files 
 —Launches the
 CVI Source Code Files 
 window, in which you can specify the pathname for the source file and project file that implements the function the module calls.
- Function Call 
 —Directly edits the function name and all of function arguments at once.

#### Editing the Function Call

You can use various controls in the Module tab to edit the function name and the argument values of the function. Alternatively, you can use the Function Call control to directly edit the function name and all of the function arguments at once. In the Function Call control, edit the call just as you would in a source code editor. If you enter a different number of arguments than the function prototype specifies or enter a different argument type, TestStand prompts you to alter the prototype to match the number and type of arguments you specify.

When you edit a call in the Function Call control, the
 Revert
 and
 Accept
 buttons are visible. All other controls are dimmed.

- Accept 
 —Applies the changes you made in the Function Call control.
- Revert 
 —Discards the changes you make in the Function Call control.

#### See Also

[Attributes dialog box](attributes-dialog-box.html)

[Calling Legacy LabWindows/CVI Code Modules](/csh?context=ts_tsref_lwcvicalllegacycodemods)

[CVI Source Code Files Window](cvi-source-code-files-window.html)

[Edit Search Directories dialog box](edit-search-directories-dialog-box.html)

[Locating the Correct DLL in 32-bit TestStand and 64-bit TestStand](/csh?context=ts_tsfundamentals_64locatingdlls)

[Parameters Table Context Menu for Module Tabs](for-module-tabs-parameters-table-context-menu.html)

[Step Settings Pane](step-settings-pane.html)

[Using Side-by-Side Versions of the LabWindows/CVI Run-Time Engine with TestStand](/csh?context=ts_tsfundamentals_sxscvirte)

[Using the $(Platform) Path Macro to Locate the Correct Code Module in 32-bit TestStand and 64-bit TestStand](/csh?context=ts_tsfundamentals_64platformmacro)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/layout-tab-configure-message-popup-step-dialo.html language=enus -->
## TOPIC 03859: Layout Tab - Configure Message Popup Step Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/layout-tab-configure-message-popup-step-dialo.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/layout-tab-configure-message-popup-step-dialo.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Layout Tab The Layout tab contains the following options: Center Dialog —Positions the dialog box at the center in relation to the screen. Top Coordinate —An expression that determines the position of the dialog box relative to the top of the screen. Left Coordinate —An expression that determines th

### Layout Tab - Configure Message Popup Step Dialog Box

#### Layout Tab

The Layout tab contains the following options:

- Center Dialog 
 —Positions the dialog box at the center in relation to the screen.
  - Top Coordinate 
 —An expression that determines the position of the dialog box relative to the top of the screen.
  - Left Coordinate 
 —An expression that determines the position of the dialog box relative to the left side of the screen.
- Control Arrangement 
 —The order, location, and alignment for the controls in the dialog box.
  - Control Order 
 —The order of the message, response, and file controls in the dialog box.
  - Button Location 
 —Specifies where to position the buttons in the dialog box.
  - Button Alignment 
 —The alignment of the buttons in the dialog box.
- Dialog Options 
 —The following miscellaneous options in the dialog box:
  - Make Floating 
 —When you enable this option, the dialog box stays on top of the TestStand application. You can interact with the main application window while the dialog box is visible.
  - Make Modal 
 —When you enable this option, the dialog box is modal to the TestStand application. You cannot interact with the main application window until the dialog box is dismissed.
  - Resize Option 
 —When you enable this option, you can resize the dialog box.
 Note 
 This option is not available when the dialog box is modal.

Parent topic:

Configure Message Popup Step Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/legacy-csv-txt-and-excel-plugins.html language=enus -->
## TOPIC 03860: Legacy .CSV, .TXT, and Excel Plugins

- bundle_id: `teststand-api-reference`
- source_path: `tsref/legacy-csv-txt-and-excel-plugins.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/legacy-csv-txt-and-excel-plugins.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Legacy .CSV, .TXT, and Excel Plugins The Legacy .CSV, .TXT, and Excel plugins contain the following plugin-specific options: Decimal Point — The decimal point setting TestStand uses to import and export properties. If you specify a different decimal point for numeric values when you export and impor

### Legacy .CSV, .TXT, and Excel Plugins

#### Legacy .CSV, .TXT, and Excel Plugins

The Legacy .CSV, .TXT, and Excel plugins contain the following plugin-specific options:

- Decimal Point 
 — The decimal point setting TestStand uses to import and export properties.
 Notice 
 If you specify a different decimal point for numeric values when you export and
import values from a file, the imported values are not correct.
- Start of Data Marker 
 — The string that designates the beginning of a block of limit data. The
marker string must appear at the beginning of a row. The marker string in this control and in
the file do not require surrounding quotes. Include the <FILE> or <SEQUENCE> tag within
the marker to instruct TestStand to automatically substitute the name of the sequence or file on
which the step operates. Select <FILE> or <SEQUENCE> from the drop-down list to insert
the tag.
- End of Data Marker 
 — The string that designates the end of a block of limit data. The marker
string must appear at the beginning of a row. The marker string in this control and in the file
do not require surrounding quotes. Include the <FILE> or <SEQUENCE> tag within the
marker to instruct TestStand to automatically substitute the name of the sequence or file on
which the step operates. Select <FILE> or <SEQUENCE> from the drop-down list to insert
the tag.
- When Start Marker Not Found 
 — Action when Start Data Marker is not found in the
property loader source.
- Skip Rows That Begin With 
 — Causes the Import or Export command to ignore all rows that
begin with the string you specify in this control. This feature is useful when the file includes
comment lines.
- First Row of Data Specifies Step Property for Each Column 
 — Defines the step property
names for each column as the first row of each data block in the file. When you disable this
option, you must use the Specify Column to Step Property Mapping text box to specify the list
of property names. Separate the property names with commas, as shown in the following
example: Limits.Low, Limits.High, Limits.String.

Parent topic:

Legacy Plugins

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/legacy-database-plugins.html language=enus -->
## TOPIC 03861: Legacy Database Plugins

- bundle_id: `teststand-api-reference`
- source_path: `tsref/legacy-database-plugins.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/legacy-database-plugins.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Legacy Database Plugins The legacy database plugin contains the following plugin-specific options: SQL Select Statement — The SQL statement property loader plugin uses to import property and variable values. The SQL statement must return a recordset that includes the column names you specify. Step N

### Legacy Database Plugins

#### Legacy Database Plugins

The legacy database plugin contains the following plugin-specific options:

- SQL Select Statement 
 — The SQL statement property loader plugin uses to import property
and variable values. The SQL statement must return a recordset that includes the column
names you specify.
- Step Name Column 
 — The name of the SQL statement column that contains the names of the
sequence steps and variable scopes that define the rows of data.
- Max size for column names 
 — The maximum number of characters for a column name. Many
databases limit the size of a column name. Use the control to select the limit for any DBMS
TestStand supports by default.
- Append data type to column name 
 — When you enable this control, TestStand automatically
appends the name of the data type of a property to the column name for a property when you
select a property from the Available list.
- Only Import Rows that Match the Specified Column Values 
 — When you enable this
option, the step loads only the rows that match the specific column values. When you disable
this control, the Column Values section is dimmed.
- Values 
 — The column values that each row must match. The Name/Number, Value, and Format
String controls specify the settings for the currently selected mapping. Use New, Cut, Copy,
and Paste to create a new item in the list, remove items from the list, and rearrange the items in
the list.
  - Name/Number 
 — An expression TestStand evaluates at run time to determine the name of
the column. To refer to a column by the order of the column in the SQL statement,
specify an expression that returns a one-based number without surrounding quotes.
  - Value 
 — An expression TestStand evaluates at run time to determine the filter value of a
column. Include the <FILE> or <SEQUENCE> tag within a value expression to instruct
TestStand to automatically substitute the name of the sequence or file on which the step
operates. To insert the <FILE> or <SEQUENCE> tag, select it from the drop-down list.
  - Format String 
 — Specifies how to convert a string value when comparing a column value
to a string expression. Typically, you use this control when comparing data from a
column that is of the date-time or currency type.

Parent topic:

Legacy Plugins

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/legacy-import-export-properties-dialog-box.html language=enus -->
## TOPIC 03862: Legacy Import/Export Properties Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/legacy-import-export-properties-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/legacy-import-export-properties-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Select Tools»Import/Export Properties to launch the Import/Export Properties dialog box. In TestStand 2016 and later, the Legacy Property Loader step is no longer listed in the default type palettes installed by TestStand. If you open a sequence file with a legacy step, the legacy step type will app

### Legacy Import/Export Properties Dialog Box

Tools»Import/Export Properties

Note

Legacy Property Loader

<TestStand>
\Components\StepTypes\Database\LegacyImportExportTool.ini

Importing and Exporting with a Legacy Source

When you edit a sequence file, you can select
 Tools»Import/Export Properties
 to import values from a database, file, or clipboard into step properties or variables or to export values from step properties or variables to a database, file, or clipboard.

The Import/Export Properties dialog box contains the following tabs when you select
 File
 or
 Clipboard
 in the Data Location ring control:

- Source/Destination
- Properties

The Import/Export Properties dialog box contains the following tabs when you select
 Database
 from the Data Location ring control:

- Source/Destination
- Properties
- Additional Columns

In addition to the tabs, the Import/Export Properties dialog box contains the following options:

- Export 
 —Exports the properties and variables you specify on the Properties and Additional Columns tabs. The ring control to the left of the
 Export 
 button specifies whether to create new rows in the database or file or to overwrite any previously written rows for the step or variable group. For databases, when the Additional Columns tab specifies column values that match an existing record, only records that match these specified values are overwritten.
 Note 
 If you set the decimal symbol character on the computer to use the comma character, do not leave the digit grouping symbol set to the comma because Microsoft Excel misinterprets the floating-point values you paste into Excel or export to an Excel file from TestStand.
- Import 
 —Imports the properties and variables you specify on the Properties tab. The Additional Columns tab defines the set of column values that a record must match before loading values from the record.
 Note 
 The Import/Export Properties dialog box requires that the names of the steps you import be uniquely named; otherwise, the import operation reports an error.
 If you edit the limits text (
 .txt
 ) or comma-delimited (
 .csv
 ) file using Microsoft Excel, Excel strips off quotation mark characters that surround string values when using the Text Import Wizard or when automatically opening
 .csv
 files. The TestStand
 [Property Loader step](legacy-property-loader-step.html)
 attempts to import the value from the limits file with quotation marks if importing without quotation marks fails.

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/legacy-model-switcher.html language=enus -->
## TOPIC 03863: Legacy Model Switcher

- bundle_id: `teststand-api-reference`
- source_path: `tsref/legacy-model-switcher.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/legacy-model-switcher.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: If you encounter an incompatibility in an existing test system when you use the TestStand 2012 or later process models or other circumstances prevent you from using the TestStand 2012 or later process models, you can use the equivalent legacy TestStand 2010 process models. However, National Instrume

### Legacy Model Switcher

Note

ModelSupport.seq

ModelSupport.seq

You can
 [manually select the equivalent legacy TestStand 2010 process models](/csh?context=ts_tsref_manually_select_process_model)
 to use. Alternatively, you can use the Legacy Model Switcher tool to replace the TestStand 2012 or later process models with equivalent legacy TestStand 2010 process models located in
 [<TestStand>](/csh?context=ts_tsfundamentals_directories)
 \Components\Models\TestStandModels
 or vice versa. This tool does not affect any custom process models.

You can also use the Legacy Model Switcher to migrate the result processing options from the
 [TestStand 2012 or later process models](/csh?context=ts_tsfundamentals_process_model_plugin_arch)
 to the equivalent legacy TestStand 2010 process models or vice versa.

You must restart all TestStand applications for the new settings to take effect.

You can launch the Legacy Model Switcher tool in the following ways:

- (Windows 8.1) Click the
 NI Launcher 
 tile on the Start screen and select
 TestStand»Tools»Compatibility»TestStand Legacy Model Switcher 
 .
- (Windows 10 or 7) Select
 Start»All Programs»National Instruments»TestStand»Tools»Compatibility»TestStand Legacy Model Switcher 
 .
- Run
 [<TestStand>](/csh?context=ts_tsfundamentals_directories)
 \Components\Models\TestStandModels\TestStand 2010 Process Models (Legacy)\LegacyModelSwitcher.exe 
 .

You can also use the
 /NEW
 or
 /LEGACY
 command-line arguments to programmatically select which TestStand process models to use.

The Legacy Model Switcher contains the following options:

- Use New Models 
 —Specifies to use the default TestStand 2012 or later process models.
  - Migrate Report Options from Legacy Models 
 —Creates a new configuration in a configuration set called Options from Legacy Models. The tool automatically selects a unique name for the configuration if the programatically tool has already used the default name in a previous completed migration. Refer to the migration report for the specific configuration names the tool uses.
  - Migrate Database Options from Legacy Models 
 —Creates a new configuration in a configuration set called Options from Legacy Models. The tool automatically selects a unique name for the configuration if the programatically tool has already used the default name in a previous completed migration. Refer to the migration report for the specific configuration names the tool uses.
- Use Legacy Models 
 —Specifies to use the equivalent legacy TestStand 2010 process models.
  - Migrate Report Options from New Models 
 —Select a configuration to migrate to use with the equivalent legacy TestStand 2010 process models. Migrating report options from the default TestStand 2010 process models overwrites any existing legacy-style options files.
  - Migrate Database Options from New Models 
 —Select a configuration to migrate to use with the equivalent legacy TestStand 2010 process models. Migrating database options from the default TestStand 2010 process models overwrites any existing legacy-style options files.

#### See Also

[Result Processing dialog box](result-processing-dialog-box.html)

[TestStand Offline Results Processing Utility](/csh?context=ts_tsref_offline_processing_utility)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/legacy-plugins.html language=enus -->
## TOPIC 03864: Legacy Plugins

- bundle_id: `teststand-api-reference`
- source_path: `tsref/legacy-plugins.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/legacy-plugins.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Legacy Plugins Legacy .CSV, .TXT, and Excel Plugins Legacy Database Plugins

### Legacy Plugins

#### Legacy Plugins

[Legacy .CSV, .TXT, and Excel Plugins](legacy-csv-txt-and-excel-plugins.html)

[Legacy Database Plugins](legacy-database-plugins.html)

Parent topic:

Property Loader Plugins

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/legacy-property-loader-step.html language=enus -->
## TOPIC 03865: Legacy Property Loader Step

- bundle_id: `teststand-api-reference`
- source_path: `tsref/legacy-property-loader-step.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/legacy-property-loader-step.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Legacy Property Loader step to dynamically load property and variable values from a text file, a Microsoft Excel file, or a database management system (DBMS) at run time. In TestStand 2016 and later, the Legacy Property Loader step is no longer listed in the default type palettes installed b

### Legacy Property Loader Step

Note

- In TestStand 2016 and later, the Legacy Property Loader step is no
longer listed in the default type palettes installed by TestStand. If you open a
sequence file with a legacy step, the legacy step type will appear in the insert step
menu, and you can still execute sequences that contain the legacy Property Loader
steps. The
 Legacy Import/Export Properties tool 
 in the Tools menu is not installed by
default. You can manually add the legacy tool by importing the
 <TestStand>
\Components\StepTypes\Database\LegacyImportExportTool.ini 
 file
in the Tools menu. See the
 Importing and Exporting with a Legacy Source 
 topic
for more information.
- The Legacy Property Loader step type supports only ANSI file formats.

The Property Loader step type can load limits from all TestStand-supported databases except MySQL. You can apply the values you load to the current sequence. For example, you can develop a sequence that tests two different models of a cellular phone, where each model requires unique limit values for each step. When you use step properties to specify the limit values, include a Property Loader step in the Setup step group of the sequence to initialize the property and variable values each time before the steps in the
 [Main step group](/csh?context=ts_tsfundamentals_bldgblocks_stepgroups)
 execute.

You can also load values for properties into sequences so that all subsequent invocations of the sequences in the file use the dynamically loaded property values. For example, include a Property Loader step in a
 [ProcessSetup](/csh?context=ts_tsfundamentals_sequential_model_callbacks)
 model callback sequence the execution calls once so the execution can call the client sequence file multiple times with the dynamically loaded property values.

#### Configuring the Step

Use the
 [Edit Property Loader](edit-legacy-property-loader-dialog-box3.html)
 dialog box in the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 and in a
 [TestStand User Interface](teststand-user-interfaces.html)
 to configure the Property Loader step.

#### Step Properties

In addition to the
 [common custom properties](/csh?context=ts_tsfundamentals_custom_result_props)
 , the Property Loader step type defines the following step properties:

- Step.Result.NumPropertiesRead 
 —The total number of values the step loaded from the file or database.
- Step.Result.NumPropertiesApplied 
 —The total number of values the step assigned to properties or variables. A number less than the value of the
 Step.Result.NumPropertiesRead 
 property indicates the step was unable to update properties or variables.
- Step.ColumnListSource 
 —The name of the DatabaseColumnValue array variable or property that stores the list of column comparisons you use to filter the rows in a database recordset. By default, the value is
 Step.ColumnList 
 .
- Step.ColumnList 
 —The column comparisons TestStand makes on a recordset before TestStand loads recordset values into a property. The property must be an array of DatabaseColumnValue custom data types, which contain the following subproperties:
  - ColumnName 
 —The name or number of the column on which to perform the comparison.
  - Data 
 —The expression TestStand evaluates at run time to compare against the column value.
  - FormatString 
 —An optional
 format string 
 for dates, times, and currencies. Use the empty string (
 "" 
 ) to use the default format.
  - Direction 
 —An enumerated value that specifies the parameter direction as
 In 
 ,
 Out 
 ,
 In/Out 
 , or
 Return 
 .
  - Type 
 —An enumerated value that specifies the parameter type as
 String 
 ,
 Number 
 ,
 Boolean 
 , or
 Date/Time 
 .
  - Size 
 —The maximum size of a string parameter.
  - WriteNull 
 —Not used.
  - Status 
 —Not used.
- Step.PropertiesListSource 
 —The name of the DatabasePropertyMapping array variable or property that stores the list of variables and properties in which to load data. By default, the value is
 Step.PropertiesList 
 .
- Step.PropertiesList 
 —The list of variables and properties in which to load data. The list must be an array of DatabasePropertyMapping custom data types. Each element of the array defines a mapping of source data to a TestStand variable or property. The DatabasePropertyMapping custom data type contains the following subproperties:
  - PropertyName 
 —The name of the property or variable to which TestStand assigns a value.
  - PropertyType 
 —The scope of the property or variable. Valid values are
 0 
 = Step,
 1 
 = Local,
 2 
 = File Global, and
 3 
 = Station Global.
  - DataType 
 —The TestStand type of the property. Valid values are
 1 
 = String,
 2 
 = Boolean, and
 3 
 = Number.
  - ColumnName 
 —The name of the column from which TestStand obtains the value.
- Step.DataSourceType 
 —Specifies where the step imports property values from. Valid values are
 2 
 = File and
 3 
 = Database.
- Step.Database 
 —The SQL statement handle and settings for importing property values from a database to a sequence file. The
 Database 
 step property contains the following subproperties:
  - SQLStatementHandle 
 —The name of the variable or property that contains the SQL statement handle the step uses at run time to load values.
  - SQLStatement 
 —The SQL statement the
 Edit Property Loader 
 dialog box uses to populate ring controls that contain column names.
  - StepNameColumn 
 —The name of the column in the recordset that contains the names of the steps and variable scopes that define the rows of data.
  - AppendTypeName 
 —Specifies whether TestStand appends the data type name of the property to the column name when selecting a property from the available list.
  - FilterUsingColumnList 
 —Specifies whether the step loads only the rows that match the specific column value.
  - MaxColumnSize 
 —The maximum number of characters for a column name.
- Step.File 
 —The file and settings for importing property values from a file to a sequence file. The
 File 
 step property contains the following subproperties:
  - Path 
 —A literal pathname for the data file.
  - DecimalPoint 
 —The type of decimal point the file uses.
  - UseExpr 
 —Specifies whether TestStand uses
 Step.File.Path 
 or
 Step.File.FileExpr 
 for the pathname of the data file.
  - FileExpr 
 —A pathname expression TestStand evaluates at run time.
  - Format 
 —The type of delimiters in the file and the file type. Valid values are
 Tab 
 ,
 Comma 
 , or
 Excel 
 .
  - Start.MarkerExpr 
 —The expression for the starting marker.
  - EndMarkerExpr 
 —The expression for the ending marker.
  - Skip 
 —The string that causes the step type to ignore the row when the string appears at the beginning of the row.
  - MapColumnsUsingFirstRow 
 —Specifies whether the first row of each data block in the data file contains the names of the step properties into which the step loads the property values.
  - ColumnMapping 
 —The names of the properties into which the step loads the values when
 Step.File.MapColumnsUsingFirstRow 
 is
 False 
 .
- Step.SequenceFile 
 —The path to the sequence file to import properties to.
- Step.Sequence 
 —The sequence to which the step imports properties.
- Step.ExpandToRelatedExecutions 
 —Specifies that TestStand applies imported property values to sequences running in related executions, which include the original execution and all executions TestStand invoked or invokes using a
 Sequence Call step 
 .
- Step.UseCurrentSequence 
 —Specifies to import properties to the run-time copy of the sequence that includes the step. Otherwise, imported properties apply to all invocations of the sequences the step imports to.
- Step.UseCurrentFile 
 —Specifies to import properties to the sequence file that includes the step.
- Step.ImportAll 
 —Specifies whether the step attempts to import all property values listed in a file into the selected sequence files.
- Step.StartMarkerMissingAction 
 —Specifies the action the step takes when TestStand does not find the start marker in the file. Valid values are
 1 
 = Stop and error and
 2 
 = Skip sequence.

Parent topic:

Built-In Step Types

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/legacy-vi-settings-dialog-box.html language=enus -->
## TOPIC 03866: Legacy VI Settings Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/legacy-vi-settings-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/legacy-vi-settings-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Click Legacy VI Settings in the LabVIEW Adapter Configuration dialog box to launch the Legacy VI Settings dialog box, in which you can configure settings relevant to calling legacy test VIs . The Legacy VI Settings dialog box contains expressions the LabVIEW Adapter evaluates to generate values to p

### Legacy VI Settings Dialog Box

Click
 Legacy VI Settings
 in the
 [LabVIEW Adapter Configuration](labview-adapter-configuration-dialog-box.html)
 dialog box to launch the Legacy VI Settings dialog box, in which you can configure settings relevant to calling
 [legacy test VIs](/csh?context=ts_tsref_labview_legacy)
 . The Legacy VI Settings dialog box contains
 [expressions](/csh?context=ts_tsfundamentals_bldgblocks_expressions)
 the LabVIEW Adapter evaluates to generate values to pass to the VI in the various
 [Invocation Info](invocation-info-cluster.html)
 cluster fields. Legacy VIs can use the
 Invocation Info
 cluster as an optional input.

The Legacy VI Settings dialog box contains the following options:

- Invocation Info Parameter UUT Information Source Expressions 
 —Use this section to specify expressions for the elements in the
 Invocation Info 
 cluster in legacy VIs.
  - UUT Iteration Number 
 —The expression the LabVIEW Adapter evaluates at run time to generate a value to pass to the
 UUT # 
 element of the
 Invocation Info 
 cluster.
  - Serial Number String 
 —The expression the LabVIEW Adapter evaluates at run time to generate a value to pass to the
 UUT Info 
 element of the
 Invocation Info 
 cluster.

#### See Also

[LabVIEW Adapter Configuration dialog box](labview-adapter-configuration-dialog-box.html)

[Calling Legacy LabVIEW VIs](/csh?context=ts_tsref_labview_legacy)

Parent topic:

LabVIEW Adapter Configuration Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/limits-tab-edit-multiple-numeric-limit-test-d.html language=enus -->
## TOPIC 03867: Limits Tab - Edit Multiple Numeric Limit Test Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/limits-tab-edit-multiple-numeric-limit-test-d.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/limits-tab-edit-multiple-numeric-limit-test-d.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Limits Tab The Limits tab contains the following options: Comparison Type —The type of comparison the step type performs to determine the step status . The following table lists the available comparison types. Comparisons use 14 digits of precision. Type Description EQ (==) Numeric Measurement = Low

### Limits Tab - Edit Multiple Numeric Limit Test Dialog Box

#### Limits Tab

The Limits tab contains the following options:

- Comparison Type 
 —The type of comparison the step type performs to determine the
 step status 
 . The following table lists the available comparison types. Comparisons use 14 digits of precision.
 Type
 Description
 EQ (==)
 Numeric Measurement = Low Limit
 EQT (==+/-)
 Numeric Measurement >= Computed Low Limit and <= Computed High Limit, as shown in the table following the Threshold Type option below.
 NE (!=)
 Numeric Measurement != Low Limit
 GT (>)
 Numeric Measurement > Low Limit
 LT (<)
 Numeric Measurement < Low Limit
 GE (>=)
 Numeric Measurement >= Low Limit
 LE (<=)
 Numeric Measurement <= Low Limit
 GTLT (><)
 Numeric Measurement > Low Limit and < High Limit
 GELE (>=<=)
 Numeric Measurement >= Low Limit and <= High Limit
 GELT (>=<)
 Numeric Measurement >= Low Limit and < High Limit
 GTLE (><=)
 Numeric Measurement > Low Limit and <= High Limit
 LTGT (<>)
 Numeric Measurement < Low Limit or > High Limit
 LEGE (<=>=)
 Numeric Measurement <= Low Limit or >= High Limit
 LEGT (<=>)
 Numeric Measurement <= Low Limit or > High Limit
 LTGE (<>=)
 Numeric Measurement < Low Limit or >= High Limit
 No Comparison
 TestStand makes no Pass/Fail determination, and sets the status to
 Passed
 automatically.
- Threshold Type 
 —The type of threshold the step type uses to compute the low and high limit
values to be used with the
 EQT(== +/-) 
 comparison type to determine the step status. This
control is available only when you use the
 EQT (== +/-) 
 comparison type. The following
table lists the available threshold types and how the step type computes the Low Limit and
High Limit for each threshold type.
 Threshold Type
 Computed Low Limit
 Computed High LimitPercentage (% of Nominal Value)
 Nominal Value - (Nominal Value * Lower Threshold / 100)
 Nominal Value + (Nominal Value * Upper Threshold / 100)
 Parts Per Million (PPM of Nominal Value)
 Nominal Value - (Nominal Value * Lower Threshold / 1000000)
 Nominal Value + (Nominal Value * Upper Threshold / 1000000)
 Delta Value (Variation from Nominal Value)
 Nominal Value - Lower Threshold
 Nominal Value + Upper Threshold
- Nominal Value 
 —The base limit value, when you use the
 EQT (== +/-) 
 comparison type.
This control is available only when you use the
 EQT (== +/-) 
 comparison type.
- Low Limit 
 —The lower limit, when you use comparisons that have two limits. This control also specifies the limit when you use comparisons that have only one limit.
- High Limit 
 —The higher limit when you use comparisons that have two limits. This control is not available when you use comparisons that have only one limit.

- Measurement Must Be 
 —The one or two limit values the step uses to perform the limit comparison.
- Units 
 —A label that describes the measurement units for the limits and the value for which the step checks limits. The units you specify appear in both the report and the result database.
 Use the drop-down ring controls adjacent to the Units control to select standard units and prefixes. Select the
 Short Name
 option in each ring control to toggle between the long and short names for a unit or prefix. 
 Note 
 The unit and unit prefix are for display and documentation purposes and do not scale the measured value or affect the limit comparison. 
 You can choose to display the limit values in real, integer, unsigned integer, hexadecimal, octal, or binary formats. Click
 Edit Numeric Format 
 to launch the
 Numeric Format 
 dialog box, in which you can further customize the format with which to display the limit values.
- Name 
 —The name TestStand assigns to the element in the result array. TestStand displays this name in the report.
- Measurement Set 
 —The number of measurements and the name of the measurements on which the step operates, and displays the comparison type and limits for each measurement.

Use the
 Add
 and
 Remove
 buttons to add new measurements to the measurement set and remove existing measurements from the list.

#### See Also

[Numeric Format dialog box](numeric-format-dialog-box.html)

Parent topic:

Edit Multiple Numeric Limit Test Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/limits-tab-edit-numeric-limit-test-dialog-box.html language=enus -->
## TOPIC 03868: Limits Tab - Edit Numeric Limit Test Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/limits-tab-edit-numeric-limit-test-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/limits-tab-edit-numeric-limit-test-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Limits Tab The Limits tab contains the following options: Comparison Type —The type of comparison the step type performs to determine the step status . The following table lists the available comparison types. Comparisons use 14 digits of precision. Type Description EQ (==) Numeric Measurement = Low

### Limits Tab - Edit Numeric Limit Test Dialog Box

#### Limits Tab

The Limits tab contains the following options:

- Comparison Type 
 —The type of comparison the step type performs to determine the
 step status 
 . The following table lists the available comparison types. Comparisons use 14 digits of precision.
 Type
 Description
 EQ (==)
 Numeric Measurement = Low Limit
 EQT (==+/-)
 Numeric Measurement >= Computed Low Limit and <= Computed High Limit, as shown in the table following the Threshold Type option below.
 NE (!=)
 Numeric Measurement != Low Limit
 GT (>)
 Numeric Measurement > Low Limit
 LT (<)
 Numeric Measurement < Low Limit
 GE (>=)
 Numeric Measurement >= Low Limit
 LE (<=)
 Numeric Measurement <= Low Limit
 GTLT (><)
 Numeric Measurement > Low Limit and < High Limit
 GELE (>=<=)
 Numeric Measurement >= Low Limit and <= High Limit
 GELT (>=<)
 Numeric Measurement >= Low Limit and < High Limit
 GTLE (><=)
 Numeric Measurement > Low Limit and <= High Limit
 LTGT (<>)
 Numeric Measurement < Low Limit or > High Limit
 LEGE (<=>=)
 Numeric Measurement <= Low Limit or >= High Limit
 LEGT (<=>)
 Numeric Measurement <= Low Limit or > High Limit
 LTGE (<>=)
 Numeric Measurement < Low Limit or >= High Limit
 No Comparison
 TestStand makes no Pass/Fail determination, and sets the status to
 Passed
 automatically.
- Threshold Type 
 —The type of threshold the step type uses to compute the low and high limit
values to be used with the
 EQT (== +/-) 
 comparison type to determine the step status. This
control is available only when you use the
 EQT (== +/-) 
 comparison type. The following
table lists the available threshold types and how the step type computes the Low Limit and
High Limit for each threshold type.
 Threshold Type
 Computed Low Limit
 Computed High LimitPercentage (% of Nominal Value)
 Nominal Value - (Nominal Value * Lower Threshold / 100)
 Nominal Value + (Nominal Value * Upper Threshold / 100)
 Parts Per Million (PPM of Nominal Value)
 Nominal Value - (Nominal Value * Lower Threshold / 1000000)
 Nominal Value + (Nominal Value * Upper Threshold / 1000000)
 Delta Value (Variation from Nominal Value)
 Nominal Value - Lower Threshold
 Nominal Value + Upper Threshold
- Nominal Value 
 —The base limit value, when you use the
 EQT (== +/-) 
 comparison type.
This control is available only when you use the
 EQT (== +/-) 
 comparison type.
- Low Limit 
 —The lower limit when you use comparisons that have two limits. Also specifies the limit when you use comparisons that have only one limit.
- High Limit 
 —The higher limit when you use comparisons that have two limits. This control is not available when you use comparisons that have only one limit.
- Measurement Must Be 
 —The one or two limit values the step uses to perform the limit comparison.
- Units 
 —A label that describes the measurement units for the limits and the value for which the step checks limits. The units you specify appear in both the report and the result database.
 Use the drop-down ring controls adjacent to the Units control to select standard units and prefixes. Select the
 Short Name
 option in each ring control to toggle between the long and short names for a unit or prefix. 
 Note 
 The unit and unit prefix are for display and documentation purposes and do not scale the measured value or affect the limit comparison.

You can choose to display the limit values in real, integer, unsigned integer, hexadecimal, octal, or binary formats. Click
 Numeric Format
 to launch the
 [Numeric Format](numeric-format-dialog-box.html)
 dialog box, in which you can further customize the format with which to display the limit values. Changes to the numeric format do not affect the limit values or the comparison operation the step performs.

#### See Also

[Numeric Format dialog box](numeric-format-dialog-box.html)

Parent topic:

Edit Numeric Limit Test Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/limits-tab-edit-string-value-dialog-box.html language=enus -->
## TOPIC 03869: Limits Tab - Edit String Value Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/limits-tab-edit-string-value-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/limits-tab-edit-string-value-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Limits Tab The Limits tab contains the following options: Comparison Type —The type of comparison to perform. Expected String Value —The string or pattern the step expects. The regular expression pattern follows the standard ECMAScript grammar. Refer to the Microsoft documentation for regular expres

### Limits Tab - Edit String Value Dialog Box

#### Limits Tab

The Limits tab contains the following options:

- Comparison Type 
 —The type of comparison to perform.
- Expected String Value 
 —The string or pattern the step expects.
 Note 
 The regular expression pattern follows the standard ECMAScript grammar. Refer to the
 [Microsoft documentation for regular expressions](https://docs.microsoft.com/en-us/cpp/standard-library/regular-expressions-cpp?view=vs-2019)
 for more information.

Parent topic:

Edit String Value Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/limits-tab-multiple-numeric-limit-test-edit-t.html language=enus -->
## TOPIC 03870: Limits Tab - Multiple Numeric Limit Test Edit Tabs

- bundle_id: `teststand-api-reference`
- source_path: `tsref/limits-tab-multiple-numeric-limit-test-edit-t.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/limits-tab-multiple-numeric-limit-test-edit-t.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Limits Tab The Limits tab of the Multiple Numeric Limit Test contains the following options: Measurement Table —The number and name of the measurements on which the step operates, and displays the comparison type and limits for each measurement. Use the buttons to the right of the control to add, re

### Limits Tab - Multiple Numeric Limit Test Edit Tabs

#### Limits Tab

The Limits tab of the Multiple Numeric Limit Test contains the following options:

- Measurement Table 
 —The number and name of the measurements on which the step operates, and displays the comparison type and limits for each measurement. Use the buttons to the right of the control to add, remove, and reorder the measurements.
- Comparison Type 
 —The type of comparison the step type performs to determine the
 step status 
 . The following table lists the available comparison types. Comparisons use 14 digits of precision.
 Type
 Description
 EQ (==)
 Numeric Measurement = Low Limit
 EQT (==+/-)
 Numeric Measurement >= Computed Low Limit and <= Computed High Limit, as shown in the table following the Threshold Type option below.
 NE (!=)
 Numeric Measurement != Low Limit
 GT (>)
 Numeric Measurement > Low Limit
 LT (<)
 Numeric Measurement < Low Limit
 GE (>=)
 Numeric Measurement >= Low Limit
 LE (<=)
 Numeric Measurement <= Low Limit
 GTLT (><)
 Numeric Measurement > Low Limit and < High Limit
 GELE (>=<=)
 Numeric Measurement >= Low Limit and <= High Limit
 GELT (>=<=)
 Numeric Measurement >= Low Limit and < High Limit
 GTLE (><=)
 Numeric Measurement > Low Limit and <= High Limit
 LTGT (<>)
 Numeric Measurement < Low Limit or > High Limit
 LEGE (<=>=)
 Numeric Measurement <= Low Limit or >= High Limit
 LEGT (<=>)
 Numeric Measurement <= Low Limit or > High Limit
 LTGE (<>=)
 Numeric Measurement < Low Limit or >= High Limit
 No Comparison
 TestStand makes no Pass/Fail determination, and sets the status to
 Passed
 automatically.
- Threshold Type 
 —The type of threshold the step type uses to compute the low and high limit
values to be used with the
 EQT (== +/-) 
 comparison type to determine the step status. This
control is available only when you use the
 EQT (== +/-) 
 comparison type. The following
table lists the available threshold types and how the step type computes the Low Limit and
High Limit for each threshold type.
 Threshold Type
 Computed Low Limit
 Computed High LimitPercentage (% of Nominal Value)
 Nominal Value - (Nominal Value * Lower Threshold / 100)
 Nominal Value + (Nominal Value * Upper Threshold / 100)
 Parts Per Million (PPM of Nominal Value)
 Nominal Value - (Nominal Value * Lower Threshold / 1000000)
 Nominal Value + (Nominal Value * Upper Threshold / 1000000)
 Delta Value (Variation from Nominal Value)
 Nominal Value - Lower Threshold
 Nominal Value + Upper Threshold
- Nominal Value 
 —The base limit value, when you use the
 EQT (== +/-) 
 comparison type.
This control is available only when you use the
 EQT (== +/-) 
 comparison type.
- Low 
 —The lower limit when you use comparisons that have two limits. Also specifies the limit when you use comparisons that have only one limit.
- High 
 —The higher limit when you use comparisons that have two limits. This control is not available when you use comparisons that have only one limit.
- Units 
 —A label that describes the measurement units for the limits and the value for which the step checks limits. The units you specify appear in both the report and the result database.
 Use the drop-down ring controls adjacent to the Units control to select standard units and prefixes. Select the
 Short Name
 option in each ring control to toggle between the long and short names for a unit or prefix. 
 Note 
 The unit and unit prefix are for display and documentation purposes and do not scale the measured value or affect the limit comparison.
- Numeric Format 
 —TestStand displays the limit values in Real, Integer, Unsigned Integer, Hexadecimal, Octal, or Binary formats. Select
 Custom 
 to launch the
 Numeric Format 
 dialog box, in which you can further customize the format with which to display the limit values.
- Measurement Must Be 
 —Displays the one or two limit values the step uses to perform the limit comparison.

#### See Also

[Numeric Format dialog box](numeric-format-dialog-box.html)

Parent topic:

Multiple Numeric Limit Test Edit Tabs

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/limits-tab-numeric-limit-test-edit-tabs.html language=enus -->
## TOPIC 03871: Limits Tab - Numeric Limit Test Edit Tabs

- bundle_id: `teststand-api-reference`
- source_path: `tsref/limits-tab-numeric-limit-test-edit-tabs.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/limits-tab-numeric-limit-test-edit-tabs.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Limits Tab The Limits tab of the Numeric Limit Test contains the following options: Comparison Type —The type of comparison the step type performs to determine the step status . The following table lists the available comparison types. Comparisons use 14 digits of precision. Type Description EQ (==)

### Limits Tab - Numeric Limit Test Edit Tabs

#### Limits Tab

The Limits tab of the Numeric Limit Test contains the following options:

- Comparison Type 
 —The type of comparison the step type performs to determine the
 step status 
 . The following table lists the available comparison types. Comparisons use 14 digits of precision.
 Type
 Description
 EQ (==)
 Numeric Measurement = Low Limit
 EQT (==+/-)
 Numeric Measurement >= Computed Low Limit and <= Computed High Limit, as shown in the table following the Threshold Type option below.
 NE (!=)
 Numeric Measurement != Low Limit
 GT (>)
 Numeric Measurement > Low Limit
 LT (<)
 Numeric Measurement < Low Limit
 GE (>=)
 Numeric Measurement >= Low Limit
 LE (<=)
 Numeric Measurement <= Low Limit
 GTLT (><)
 Numeric Measurement > Low Limit and < High Limit
 GELE (>=<=)
 Numeric Measurement >= Low Limit and <= High Limit
 GELT (>=<=)
 Numeric Measurement >= Low Limit and < High Limit
 GTLE (><=)
 Numeric Measurement > Low Limit and <= High Limit
 LTGT (<>)
 Numeric Measurement < Low Limit or > High Limit
 LEGE (<=>=)
 Numeric Measurement <= Low Limit or >= High Limit
 LEGT (<=>)
 Numeric Measurement <= Low Limit or > High Limit
 LTGE (<>=)
 Numeric Measurement < Low Limit or >= High Limit
 No Comparison
 TestStand makes no Pass/Fail determination, and sets the status to
 Passed
 automatically.
- Threshold Type 
 —The type of threshold the step type uses to compute the low and high limit
values to be used with the
 EQT (== +/-) 
 comparison type to determine the step status. This
control is available only when you use the
 EQT (== +/-) 
 comparison type. The following
table lists the available threshold types and how the step type computes the Low Limit and
High Limit for each threshold type.
 Threshold Type
 Computed Low Limit
 Computed High LimitPercentage (% of Nominal Value)
 Nominal Value - (Nominal Value * Lower Threshold / 100)
 Nominal Value + (Nominal Value * Upper Threshold / 100)
 Parts Per Million (PPM of Nominal Value)
 Nominal Value - (Nominal Value * Lower Threshold / 1000000)
 Nominal Value + (Nominal Value * Upper Threshold / 1000000)
 Delta Value (Variation from Nominal Value)
 Nominal Value - Lower Threshold
 Nominal Value + Upper Threshold
- Nominal Value 
 —The base limit value, when you use the
 EQT (== +/-) 
 comparison type.
This control is available only when you use the
 EQT (== +/-) 
 comparison type.
- Low 
 —The lower limit when you use comparisons that have two limits. Also specifies the limit when you use comparisons that have only one limit.
- High 
 —The higher limit when you use comparisons that have two limits. This control is not available when you use comparisons that have only one limit.
- Units 
 —A label that describes the measurement units for the limits and the value for which the step checks limits. The units you specify appear in both the report and the result database.
 Use the drop-down ring controls adjacent to the Units control to select standard units and prefixes. Select the
 Short Name
 option in each ring control to toggle between the long and short names for a unit or prefix. 
 Note 
 The unit and unit prefix are for display and documentation purposes and do not scale the measured value or affect the limit comparison.
- Numeric Format 
 —TestStand displays the limit values in Real, Integer, Unsigned Integer, Hexadecimal, Octal, or Binary formats. Select
 Custom 
 to launch the
 Numeric Format 
 dialog box, in which you can further customize the format with which to display the limit values.
- Measurement Must Be 
 —Displays the one or two limit values the step uses to perform the limit comparison.

Parent topic:

Numeric Limit Test Edit Tabs

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/limits-tab-string-value-test-edit-tabs.html language=enus -->
## TOPIC 03872: Limits Tab - String Value Test Edit Tabs

- bundle_id: `teststand-api-reference`
- source_path: `tsref/limits-tab-string-value-test-edit-tabs.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/limits-tab-string-value-test-edit-tabs.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Limits Tab The Limits tab of the String Value Test contains the following options: Comparison Type —The type of comparison to perform. Expected String Value —The string or pattern the step expects. The regular expression pattern follows the standard ECMAScript grammar. Refer to the Microsoft documen

### Limits Tab - String Value Test Edit Tabs

#### Limits Tab

The Limits tab of the String Value Test contains the following options:

- Comparison Type 
 —The type of comparison to perform.
- Expected String Value 
 —The string or pattern the step expects.
 Note 
 The regular expression pattern follows the standard ECMAScript grammar. Refer to the
 [Microsoft documentation for regular expressions](https://docs.microsoft.com/en-us/cpp/standard-library/regular-expressions-cpp?view=vs-2019)
 for more information.

Parent topic:

String Value Test Edit Tabs

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/list-bar.html language=enus -->
## TOPIC 03873: List Bar

- bundle_id: `teststand-api-reference`
- source_path: `tsref/list-bar.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/list-bar.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: The list bar control, located at the left edge of a TestStand User Interface window, displays a list of the open sequence files and executions. Click Sequence Files to display the Sequence File list. Click Executions to display the Executions list. When you display the Sequence Files list, the Seque

### List Bar

The list bar control, located at the left edge of a
 [TestStand User Interface](teststand-user-interfaces.html)
 window, displays a list of the open sequence files and executions. Click
 Sequence Files
 to display the Sequence File list. Click
 Executions
 to display the Executions list.

When you display the Sequence Files list, the
 [Sequence File](sequence-file-tab.html)
 tab becomes visible to the right of the list bar control and displays the content of the selected sequence file. When you display the Executions list, the
 [Execution](execution-tab.html)
 tab and
 [Report](report-tab.html)
 tab become visible to the right of the list bar control and display the state of the selected execution.

#### See Also

[Execution Tab](execution-tab.html)

[Report Tab](report-tab.html)

[Sequence File Tab](sequence-file-tab.html)

Parent topic:

TestStand User Interface Menus and Tabs

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/load-sequence-prototype-dialog-box.html language=enus -->
## TOPIC 03874: Load Sequence Prototype Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/load-sequence-prototype-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/load-sequence-prototype-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Click the Module tab of the Step Settings pane of the TestStand Sequence Editor or launch the Edit Sequence Call dialog box from a TestStand User Interface , disable the Use Prototype of Sequence option, and click Load Prototype to launch the Load Sequence Prototype dialog box. When you use the Load

### Load Sequence Prototype Dialog Box

Click the
 Module
 tab of the
 [Step Settings](step-settings-pane.html)
 pane of the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 or launch the
 [Edit Sequence Call](edit-sequence-call-dialog-box.html)
 dialog box from a
 [TestStand User Interface](teststand-user-interfaces.html)
 , disable the
 Use Prototype of Sequence
 option, and click
 Load Prototype
 to launch the Load Sequence Prototype dialog box.

When you use the
 Load Prototype
 button on the Module tab of the Step Settings pane of a Sequence Call step to load prototype information from a different sequence and the sequence from which you load the prototype includes the same parameters as the original sequence plus additional parameters, TestStand passes the additional parameters to the sequence you call.

The Load Sequence Prototype dialog box contains the following options:

- Use Current File 
 —Enable this option to load prototype information from a sequence in the sequence file you are currently editing. The File Pathname control dims when you enable this option.
- File Pathname 
 —The pathname of the sequence file that contains the sequence from which you want to load prototype information.
- Sequence 
 —The names of the sequences in the sequence file you specify.

#### See Also

[Edit Sequence Call dialog box](edit-sequence-call-dialog-box.html)

[Step Settings Pane](step-settings-pane.html)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/loading-limit-values-from-databases.html language=enus -->
## TOPIC 03875: Loading Limit Values from Databases

- bundle_id: `teststand-api-reference`
- source_path: `tsref/loading-limit-values-from-databases.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/loading-limit-values-from-databases.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Loading Limit Values from Databases You can use the recordset an Open SQL Statement step returns to load limit values. Each row of the recordset table pertains to a particular step in a sequence or to a variable scope, as shown in the following table. The column headings correspond to the names of p

### Loading Limit Values from Databases

#### Loading Limit Values from Databases

You can use the recordset an
 [Open SQL Statement](open-sql-statement-step.html)
 step returns to load limit values. Each row of the recordset table pertains to a particular step in a sequence or to a variable scope, as shown in the following table. The column headings correspond to the names of properties in the steps or variable scopes. Each row contains values only for the columns that define properties or variables that exist in the step or variable scope that corresponds to that row.

| STEPNAME | LIMITS_HIGH | LIMITS_LOW | LIMITS_STRING | POWER_ON | COUNT | SEQUENCE NAME |
| --- | --- | --- | --- | --- | --- | --- |
| Voltage at Pin A | 11.0 | 9.0 | — | — | — | Phone Test.seq |
| Voltage at Pin B | 9.5 | 8.5 | — | — | — | Phone Test.seq |
| Self Test Output | — | — | "SYS OK" | — | — | Phone Test.seq |
| <Locals> | — | — | — | — | 100 | Phone Test.seq |
| <File Globals> | — | — | — | — | 99 | Phone Test.seq |
| <Station Globals> | — | — | — | False | — | Phone Test.seq |
| Frequency at Pin A | 100,000 | 10,000 | — | — | — | Frequency Test.seq |
| Frequency at Pin B | 90,000 | 9,000 | — | — | — | Frequency Test.seq |
| Self Test Output | — | — | "OK" | — | — | Frequency Test.seq |

The Property Loader step filters the data an SQL statement returns so you load only values from rows that contain specific column values, which is equivalent to using starting and ending data markers in a text or Microsoft Excel file. For example, you can load only the rows in the table where the SEQUENCE NAME field contains the value
 Phone Test.seq
 .

Parent topic:

Legacy Property Loader Step

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/loading-limit-values-from-files.html language=enus -->
## TOPIC 03876: Loading Limit Values from Files

- bundle_id: `teststand-api-reference`
- source_path: `tsref/loading-limit-values-from-files.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/loading-limit-values-from-files.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Loading Limit Values from Files You can use tab-delimited text files ( .txt ), comma-delimited text files ( .csv ), or Microsoft Excel files ( .xls ) to load limit values. The following tab-delimited limits text file includes one data block starting and ending data markers specify. Start Marker <Ste

### Loading Limit Values from Files

#### Loading Limit Values from Files

You can use tab-delimited text files (
 .txt
 ), comma-delimited text files (
 .csv
 ), or Microsoft Excel files (
 .xls
 ) to load limit values. The following tab-delimited limits text file includes one data block starting and ending data markers specify.

| Start Marker |  |  |  |
| --- | --- | --- | --- |
|  |  |  |  |
| <Step Name> | Limits.Low | Limits.High | Limits.String |
| Voltage at Pin A | 9.0 | 11.0 |  |
| Voltage at Pin B | 8.5 | 9.5 |  |
| Self Test Output |  |  | "SYS OK" |
|  |  |  |  |
| <Locals> |  | Variable Value |  |
| Count |  | 100 |  |
|  |  |  |  |
| <FileGlobals> |  | Variable Value |  |
| Count |  | 99 |  |
|  |  |  |  |
| <StationGlobals> |  | Variable Value |  |
| Power_On |  | False |  |
|  |  |  |  |
| End Marker |  |  |  |

In the step name section of this example file, the row names correspond to step names, and the column headings correspond to the names of step properties. Each row contains values only for the columns that define properties that exist in the step that corresponds to that row.

In the locals, file globals, and
 [station globals variable](/csh?context=ts_tsfundamentals_station_global_variables)
 sections, each row specifies the name of the property and corresponding property value.

Starting and ending data markers designate the bounds of the block of data. A data file can contain more than one block of data.

Select
 Tools»Import/Export Properties
 to export property and variable data in the appropriate block format. When you specify starting and ending data markers in the text controls in the
 [Import/Export Properties](legacy-import-export-properties-dialog-box.html)
 dialog box, enter the marker text without double quotation marks. When you specify starting and ending data markers in the expression controls in the
 [Edit Property Loader](edit-legacy-property-loader-dialog-box3.html)
 dialog box, you must surround literal marker text values with double quotation marks.

Parent topic:

Legacy Property Loader Step

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/localization-tab-station-options-dialog-box.html language=enus -->
## TOPIC 03877: Localization Tab - Station Options Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/localization-tab-station-options-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/localization-tab-station-options-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Localization Tab The Localization tab specifies the station language and other regional settings. By default, TestStand installs only strings for English . The Localization tab contains the following options: Select a Language —The language TestStand uses to display text. The language setting determ

### Localization Tab - Station Options Dialog Box

#### Localization Tab

The Localization tab specifies the station language and other regional settings. By default,
 [TestStand installs only strings for English](/csh?context=ts_tsfundamentals_resource_strings_format)
 .

The Localization tab contains the following options:

- Select a Language 
 —The language TestStand uses to display text. The language setting determines the set of string resource files TestStand uses.
 Note 
 Changes to this setting do not take effect until you restart TestStand.
- Use Localized Decimal Point 
 —When you enable this option, TestStand uses the decimal point character you set in the Regional Options on the Microsoft Windows Control Panel. If you do not set this option, TestStand uses the period character as the decimal point symbol.
 Note 
 This option decreases the speed at which TestStand compares and processes strings.

Parent topic:

Station Options Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/locals-context-menu-sequence-file-tab.html language=enus -->
## TOPIC 03878: Locals Context Menu - Sequence File Tab

- bundle_id: `teststand-api-reference`
- source_path: `tsref/locals-context-menu-sequence-file-tab.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/locals-context-menu-sequence-file-tab.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Locals Context Menu To access the context menu, right-click the Locals item on the Variables pane. The items in the Locals context menu vary depending on whether you right-click a local variable or local variable subproperty. The Locals context menu can contain the following items: Insert Local —A s

### Locals Context Menu - Sequence File Tab

#### Locals Context Menu

To access the context menu, right-click the Locals item on the
 [Variables](variables-pane-sequence-file-tab.html)
 pane. The items in the Locals context menu vary depending on whether you right-click a local variable or local variable subproperty.

The Locals context menu can contain the following items:

- Insert Local 
 —A submenu from which you select the data type for the local variable you want to insert.
 If you want to insert a local variable with a
 custom data type 
 , you must create a named data type.
 After you create the named data type, it appears in the Type submenu of the Insert Local submenu.
 If you insert an array, the
 Array Bounds 
 dialog box launches.
 Notice that sequences always start with one local variable,
 ResultList 
 . If you delete this local variable, TestStand cannot
 collect results 
 for the sequence.
- Cut 
 —Removes the selected local variable and places it on the clipboard.
- Copy 
 —Copies the selected local variable to the clipboard.
- Paste 
 —Inserts the local variable from the clipboard.
- Delete 
 —Deletes the local variable.
- Copy Value 
 —Copies the value of the selected property to the clipboard.
- Rename 
 —Displays a control for renaming the selected local variable or subproperty.
- Advanced 
 —Launches a submenu that contains the following options:
  - Edit Flags 
 —Launches the
 Edit Flags 
 dialog box, in which you can modify the flags for the local variable or subproperty.
  - Edit Attributes 
 —Launches the
 Attributes 
 dialog box, in which you can create and edit attributes for the local variable or subproperty.
- Numeric Format 
 —Launches the
 Numeric Format 
 dialog box, in which you can specify the format TestStand uses to display the value of a numeric property. This control is available only for numeric properties and numeric array properties.
- Representation 
 —The numeric data type standard to use for a number variable or parameter.
  - Double-Precision 64-bit Floating Point (default) 
 —Specifies double-precision, 64-bit floating-point representation.
  - Signed 64-bit Integer 
 —Specifies signed 64-bit integer representation.
  - Unsigned 64-bit Integer 
 —Specifies unsigned 64-bit integer representation.
- Propagate to Subsequence 
 —Specifies whether a local variable is visible at run time in subsequences the sequence calls. The variable continues to propagate as the call chain extends. Typically, you configure local variables to propagate to automatically pass a set of values to all subsequences a sequence calls.
- Allow Propagation from Caller 
 —Specifies which variable takes precedence when a subsequence defines a variable with the same name as a variable a calling sequence propagates. When you disable this option, TestStand preserves the local variable in the subsequence. When you enable this option, TestStand replaces the variable in the subsequence with the variable the caller propagates.
 When a propagated variable replaces an existing sequence variable, TestStand generates an error if the types of the variables do not match.

#### See Also

[Array Bounds dialog box](array-bounds-dialog-box.html)

[Attributes dialog box](attributes-dialog-box.html)

[Edit Flags dialog box](edit-flags-dialog-box.html)

[Numeric Format dialog box](numeric-format-dialog-box.html)

[Variables Pane](variables-pane-sequence-file-tab.html)

Parent topic:

Variables Pane - Sequence File Tab

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/locals-context-menu-sequence-file-window.html language=enus -->
## TOPIC 03879: Locals Context Menu - Sequence File Window

- bundle_id: `teststand-api-reference`
- source_path: `tsref/locals-context-menu-sequence-file-window.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/locals-context-menu-sequence-file-window.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Locals Context Menu To access the context menu, right-click the Locals item in the Variables pane. The items in the Locals context menu may vary depending on whether you right-click a local variable or local variable subproperty. The Locals context menu can contain the following items: Insert Local

### Locals Context Menu - Sequence File Window

#### Locals Context Menu

To access the context menu, right-click the Locals item in the
 [Variables](variables-pane-sequence-file-window4.html)
 pane. The items in the Locals context menu may vary depending on whether you right-click a local variable or local variable subproperty.

The Locals context menu can contain the following items:

- Insert Local 
 —A submenu from which you select the data type for the local variable you want to insert.
 If you want to insert a local variable with a
 custom data type 
 , you must create a named data type. You can create a named data type in the
 Types 
 window. 
 After you create the named data type, it appears in the Type submenu of the Insert Local submenu.
 If you insert an array, the
 Array Bounds 
 dialog box launches.
 Notice that sequences always start with one local variable,
 ResultList 
 . If you delete this local variable, TestStand cannot
 collect results 
 for the sequence.
- Cut 
 —Removes the selected local variable and places it on the clipboard.
- Copy 
 —Copies the selected local variable to the clipboard.
- Paste 
 —Inserts the local variable from the clipboard.
- Delete 
 —Deletes the local variable.
- Copy Value 
 —Copies the value of the selected property to the clipboard.
- Rename 
 —Displays a control for renaming the selected local variable or subproperty.
- Advanced 
 —Launches a submenu that contains the following options:
  - Edit Flags 
 —Launches the
 Edit Flags 
 dialog box, in which you can modify the flags for the local variable or subproperty.
  - Edit Attributes 
 —Launches the
 Attributes 
 dialog box, in which you can create and edit attributes for the local variable or subproperty.
- Numeric Format 
 —Launches the
 Numeric Format 
 dialog box, in which you can specify the format TestStand uses to display the value of a numeric property. This control is available only for numeric properties and numeric array properties.
- Representation 
 —The numeric data type standard to use for a number variable or parameter.
  - Double-Precision 64-bit Floating Point (default) 
 —Specifies double-precision, 64-bit floating-point representation.
  - Signed 64-bit Integer 
 —Specifies signed 64-bit integer representation.
  - Unsigned 64-bit Integer 
 —Specifies unsigned 64-bit integer representation.
- Propagate to Subsequence 
 —Specifies whether a local variable is visible at run time in subsequences the sequence calls. The variable continues to propagate as the call chain extends. Typically, you configure local variables to propagate to automatically pass a set of values to all subsequences a sequence calls.
- Allow Propagation from Caller 
 —Specifies which variable takes precedence when a subsequence defines a variable with the same name as a variable a calling sequence propagates. When you disable this option, TestStand preserves the local variable in the subsequence. When you enable this option, TestStand replaces the variable in the subsequence with the variable the caller propagates.
 When a propagated variable replaces an existing sequence variable, TestStand generates an error if the types of the variables do not match.
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

#### See Also

[Array Bounds dialog box](array-bounds-dialog-box.html)

[Attributes dialog box](attributes-dialog-box.html)

[Edit Flags dialog box](edit-flags-dialog-box.html)

[Numeric Format dialog box](numeric-format-dialog-box.html)

[Sequences Pane](sequences-pane-sequence-file-window.html)

[Steps Pane](steps-pane-sequence-file-window.html)

[Types Window](types-window.html)

[Variables Pane](variables-pane-sequence-file-window4.html)

Parent topic:

Variables Pane - Sequence File Window

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/lock-operation-lock-settings-edit-tab.html language=enus -->
## TOPIC 03880: Lock Operation - Lock Settings Edit Tab

- bundle_id: `teststand-api-reference`
- source_path: `tsref/lock-operation-lock-settings-edit-tab.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/lock-operation-lock-settings-edit-tab.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Lock Operation To use a lock to guarantee that only one thread executes certain steps at a time, insert a Lock step before the steps you want to protect and configure it to perform a Lock operation. Enable the Lock option on the left of the Lock Settings panel. The Lock operation contains the follow

### Lock Operation - Lock Settings Edit Tab

#### Lock Operation

To use a lock to guarantee that only one thread executes certain steps at a time, insert a Lock step before the steps you want to protect and configure it to perform a Lock operation. Enable the
 Lock
 option on the left of the Lock Settings panel.

The Lock operation contains the following options:

- Lock Name or Reference Expression 
 —The lock on which to perform the operation. You can specify the lock by name or by the object reference you receive when you create the lock using the Use Object Reference in the Lock Reference Lifetime option. Specify multiple locks using either a string array containing the names of the locks or an object reference array containing object references to the locks.
- Create Lock 
 —Instructs the operation to automatically create the lock, if the lock does not exist, using the name you specify. Locks you create with this option have a reference lifetime of Same as Execution. Unlike the locks created with the Create operation, you cannot store an object reference to the lock.
 The Lock Operation Lifetime you specify for this operation applies only to the length of time you acquire the lock, not the lifetime of the lock itself. The object you retrieve from the Use Object Reference option is not the lock object itself but an object that unlocks the lock when you destroy it. To obtain a reference to the Lock object itself or to choose a lifetime for the Lock object that is different from Same As Execution, you must use the Create operation.
- Lock Operation Lifetime 
 —Specifies how long you want the thread to lock the lock. The attributes of this option are the same as those of
 Synchronization object reference lifetimes 
 . Once the lifetime of the last Lock operation for the owning thread ends, the lock becomes available again for a thread to lock.
 
 Note 
 The Lock Reference Lifetime object you can acquire in the Create operation and the Lock Operation Lifetime object you can acquire in the Lock operation are two distinct objects and are not interchangeable. When using the Use Object Reference option for the Lock Operation Lifetime, do not use the same variable in which you store a reference to the Lock Reference Lifetime object. TestStand clears any variable you specify for the Use Object Reference option before storing the object that controls the Lock Operation Lifetime. Therefore, the reference to the Lock object is lost if you choose the variable that contains it as the variable to also contain the Lock Operation Lifetime object.
  - Same as Sequence 
 —Releases the object reference after the sequence executes.
  - Same as Thread 
 —Releases the object reference after the thread completes.
  - Use Object Reference 
 —Use this option when you want to explicitly control the lifetime of the object reference or when you want to refer to the object using an object reference variable.
- Timeout Enabled, Timeout Expression, Timeout Causes Run-Time Error 
 —The timeout behavior when waiting to acquire the Lock. If a timeout occurs, the
 Step.Result.TimeoutOccurred 
 property is set to
 True 
 .

Parent topic:

Lock Settings Edit Tab

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/lock-operation-lock-step-configuration-dialog.html language=enus -->
## TOPIC 03881: Lock Operation - Lock Step Configuration Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/lock-operation-lock-step-configuration-dialog.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/lock-operation-lock-step-configuration-dialog.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Lock Operation To guarantee that only one thread executes certain steps at a time, insert a Lock step before the steps you want to protect and select Configure Lock from the context menu for the step. Select Lock from the Operation ring control in the Lock Step Configuration dialog box. The Lock ope

### Lock Operation - Lock Step Configuration Dialog Box

#### Lock Operation

To guarantee that only one thread executes certain steps at a time, insert a
 [Lock step](lock-step.html)
 before the steps you want to protect and select
 Configure Lock
 from the context menu for the step. Select
 Lock
 from the Operation ring control in the Lock Step Configuration dialog box.

The Lock operation contains the following options:

- Lock Name or Reference Expression 
 —The lock on which to perform the operation. You can specify the lock by name or by the object reference you receive when you create the lock using the Use Object Reference option in the Lock Reference Lifetime option. You can specify multiple locks using either a string array containing the names of the locks or an object reference array containing object references to the locks. When you specify multiple locks, the Lock operation attempts to lock all of the locks. If the operation cannot lock all of the locks, it unlocks the ones it has so far and tries again after a random delay. This continues until the operation either succeeds in locking all of the locks or the timeout you specify occurs. When you lock all of the locks a thread requires in a single Lock operation, you avoid the possibility of deadlock. However, when you lock more than one lock at a time, you lose the guarantee of first in first out (FIFO) ordering of which thread gets to lock a particular lock first.
- Create If Does Not Exist 
 —Specifies whether the operation automatically creates the lock(s) you specify by name. Locks you create with this option have a reference lifetime of Same as Execution. Unlike the Create operation, you do not have the option of storing an object reference to the lock. The Lock Operation Lifetime you specify for this operation applies only to the length of time you acquire the lock, not the lifetime of the lock itself. The object you obtain with Use Object Reference is not the lock object itself, but instead it is an object that unlocks the lock when you destroy it. To obtain a reference to the Lock object itself or to choose a lifetime for the Lock object that is different from Same As Execution, you must use the Create operation.
- Lock Operation Lifetime 
 —Specifies how long you want the thread to lock the lock. The attributes of this option are the same as those of
 Synchronization object reference lifetimes 
 . Once the lifetime of the last Lock operation for the owning thread ends, the lock again becomes available for a thread to lock.
 
 Note 
 The Lock Reference Lifetime object you can acquire in the Create operation and the Lock Operation Lifetime object you can acquire here are two distinct objects and are not interchangeable. When using the Use Object Reference option for the Lock Operation Lifetime, do not use the same variable in which you store a reference to the Lock Reference Lifetime object. TestStand clears any variable you specify for the Use Object Reference option before storing the object that controls the Lock Operation Lifetime. Therefore, the reference to the Lock object is lost if you choose the variable that contains it as the variable to also contain the Lock Operation Lifetime object.
  - Same as Sequence 
 —Releases the object reference after the current sequence executes.
  - Same as Thread 
 —Releases the object reference after all sequences in the current thread execute.
  - Use Object Reference 
 —Use this option when you want to explicitly control the lifetime of the object reference or when you want to refer to the object using an object reference variable.
- Timeout Enabled, Timeout Expression, Timeout Causes Run-Time Error 
 —The timeout behavior when waiting to acquire the Lock. If a timeout occurs, the
 Step.Result.TimeoutOccurred 
 property is set to
 True 
 .

Parent topic:

Lock Step Configuration Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/lock-settings-edit-tab.html language=enus -->
## TOPIC 03882: Lock Settings Edit Tab

- bundle_id: `teststand-api-reference`
- source_path: `tsref/lock-settings-edit-tab.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/lock-settings-edit-tab.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Insert a Lock step and select Edit Lock Settings or Step Settings from the context menu to launch the Lock Settings edit tab. The following operations are available when you use the Lock step type: Create —Creates a lock reference. Lock —Guarantees that only one thread executes certain steps at a ti

### Lock Settings Edit Tab

Insert a Lock step and select
 Edit Lock Settings
 or
 Step Settings
 from the context menu to launch the Lock Settings edit tab. The following operations are available when you use the Lock step type:

- Create 
 —Creates a lock reference.
- Lock 
 —Guarantees that only one thread executes certain steps at a time.
- Early Unlock 
 —Releases the lock before the lock operation lifetime expires.
- Get Status 
 —Finds out information about an existing lock or determines if a particular lock exists.

#### See Also

[Synchronization Step Types](synchronization-step-types.html)

Parent topic:

Lock Step

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/lock-step-configuration-dialog-box.html language=enus -->
## TOPIC 03883: Lock Step Configuration Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/lock-step-configuration-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/lock-step-configuration-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Select Configure Lock in the context menu for the step to launch the Lock Step Configuration dialog box from a TestStand User Interface . You can also click Configure Lock on the General tab of the Step Properties dialog box. In the Lock Step Configuration dialog box, select an operation for the ste

### Lock Step Configuration Dialog Box

Select
 Configure Lock
 in the context menu for the step to launch the Lock Step Configuration dialog box from a
 [TestStand User Interface](teststand-user-interfaces.html)
 . You can also click
 Configure Lock
 on the
 [General](general-tab-step-properties-dialog-box.html)
 tab of the
 [Step Properties](step-properties-dialog-box.html)
 dialog box. In the Lock Step Configuration dialog box, select an operation for the step to perform.

The following operations are available when you use the Lock step type:

- Create 
 —Creates a lock reference.
- Lock 
 —Guarantees that only one thread executes certain steps at a time.
- Early Unlock 
 —Releases the lock before the lock operation lifetime expires.
- Get Status 
 —Finds out information about an existing lock or determines if a particular lock exists.

#### See Also

[Step Properties dialog box](step-properties-dialog-box.html)

[Synchronization Step Types](synchronization-step-types.html)

Parent topic:

Lock Step

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/lock-step.html language=enus -->
## TOPIC 03884: Lock Step

- bundle_id: `teststand-api-reference`
- source_path: `tsref/lock-step.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/lock-step.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use a Lock step to ensure that only one thread can access a particular resource or data item at a time. For example, when you examine and update the value of a global variable from multiple threads or executions, use a lock to ensure that only one thread examines and updates the variable at a time.

### Lock Step

Use a Lock step to ensure that only one thread can access a particular resource or data item at a time. For example, when you examine and update the value of a global variable from multiple threads or executions, use a lock to ensure that only one thread examines and updates the variable at a time. Multiple threads waiting to lock an item wait in first-in first-out order for the item to become available.

Lock operation

Note

Synchronization

Properties

Step Settings

#### Configuring the Step

Use the
 [Lock Settings](lock-settings-edit-tab.html)
 edit tab in the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 and the
 [Lock Step Configuration](lock-step-configuration-dialog-box.html)
 dialog box in a
 [TestStand User Interface](teststand-user-interfaces.html)
 to configure the Lock step.

#### Step Properties

In addition to the
 [common custom properties](/csh?context=ts_tsfundamentals_custom_result_props)
 , the Lock step type defines the following step properties:

- Step.Result.TimeoutOccurred 
 —Exists only when you configure the step for the Lock operation. TestStand sets the value to
 True 
 when the lock operation times out.
 Note 
 If you configure the step to use the Lock operation programmatically using the
 Step.Operation
 property, you must also create the
 Step.Result.TimeoutOccurred
 property using the
 newProperty(
 ) method for the step to execute successfully.
- Step.NameOrRefExpr 
 —Contains the Lock
 Name 
 expression for the
 Create 
 operation and the Lock Name or Reference expression for all other Lock operations. For the Lock operation, the expression can also specify an array of names or references.
- Step.LifetimeRefExpr 
 —The object reference expression for the Lock Reference
 Lifetime 
 or the Lock Operation Lifetime when you set either lifetime to Use Object Reference.
- Step.TimeoutEnabled 
 —The
 Timeout 
 Enabled setting for the Lock operation.
- Step.TimeoutExpr 
 —The Timeout expression, in seconds, for the Lock operation.
- Step.ErrorOnTimeout 
 —The Timeout Causes Run-Time Error setting for the Lock operation.
- Step.AlreadyExistsExpr 
 —Contains the Already Exists expression for the Create operation or the Lock Exists expression for the
 Get Status 
 operation.
- Step.NumThreadsWaitingExpr 
 —The Number of Threads Waiting to Lock the Lock expression for the Get Status operation.
- Step.Operation 
 —A value that specifies the operation for the step to perform. The valid values are
 0 
 = Create,
 1 
 = Lock,
 2 
 = Early Unlock, and
 3 
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
- Step.LockLifetime 
 —A value that specifies the lifetime setting to use for the Lock operation. The valid values are
 0 
 = Same as Sequence,
 1 
 = Same as Thread,
 2 
 = Use Object Reference, and
 3 
 = Same as Execution.
- Step.CreateIfDoesNotExist 
 —The Create If Does Not Exist setting for the Lock operation.

#### See Also

[Restricting Execution Flow with Lock Steps (Example)](/csh?context=ts_8182)

[Synchronization Step Types](synchronization-step-types.html)

[Thread-Safety of the PropertyObject API and TestStand Variables](/csh?context=ts_tsapiref_threadsafetyapi)

Parent topic:

Synchronization Step Types

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/lock-unlock-file-dialog-box.html language=enus -->
## TOPIC 03885: Lock/Unlock File Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/lock-unlock-file-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/lock-unlock-file-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: TestStand launches the Lock File dialog box when you attempt to lock a protected file. TestStand launches the Unlock File dialog box when you attempt to edit or save a protected sequence file that is locked or when you double-click the lock icon in a non-viewable list view of the Sequence File windo

### Lock/Unlock File Dialog Box

Variables

Sequence File Properties

Note

TestStand Sequence Editor

The Lock File dialog box contains the following options:

- New Password 
 —Enter a password to lock the file. If the file was previously locked, the dialog box displays a masked version of the current password.
- Re-enter Password 
 —Re-enter the password for confirmation.

The Unlock File dialog box contains the following options:

- Password 
 —Enter a password to unlock the file.
- Remember Password 
 —Select one of the following options:
  - No 
 —TestStand does not remember the password.
  - For Current Session 
 —TestStand stores the password in the password cache but does not persist the password between TestStand sessions. Each time you attempt to open a locked sequence file, TestStand tries to unlock it using the passwords in the password cache. Use the
 Clear Password Cache 
 button on the
 Preferences 
 tab of the
 Station Options 
 dialog box to clear the password cache.
  - For Current and Future Sessions 
 —TestStand stores the password in the password cache and persists the password between TestStand sessions. Each time you attempt to open a locked sequence file, TestStand tries to unlock it using the passwords in the password cache. Use the
 Clear Password Cache 
 button on the
 Preferences 
 tab of the
 Station Options 
 dialog box to clear the password cache.

#### See Also

[Sequence File Properties dialog box](sequence-file-properties-dialog-box.html)

[Station Options dialog box](station-options-dialog-box.html)

[Variables Pane](variables-pane-execution-window.html)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/locking-toolbars-menus-panes.html language=enus -->
## TOPIC 03886: Locking Toolbars, Menus, and Panes

- bundle_id: `teststand-api-reference`
- source_path: `tsref/locking-toolbars-menus-panes.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/locking-toolbars-menus-panes.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: You can configure the TestStand Sequence Editor to prevent a user from customizing the user interface. For example, you might want to prevent a user from rearranging the toolbars or panes within the application, or you might want to hide specific panes, buttons, and menus so the user cannot access s

### Locking Toolbars, Menus, and Panes

You can configure the TestStand Sequence Editor to prevent a user from customizing the user interface. For example, you might want to prevent a user from rearranging the toolbars or panes within the application, or you might want to hide specific panes, buttons, and menus so the user cannot access specific features.

1. Click
 Configure»Sequence Editor Options 
 to open the
 Sequence Editor Options 
 dialog box.
2. Select the
 UI Configuration 
 tab.
3. Select
 Lock UI Configuration by Disabling the Following 
 , then select the check box for each element or operation you want to lock in the user interface.

Parent topic:

TestStand Sequence Editor Menus, Panes, and Windows

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/logging-data-link-options-tab-database-option.html language=enus -->
## TOPIC 03887: Logging/Data Link Options Tab - Database Options Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/logging-data-link-options-tab-database-option.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/logging-data-link-options-tab-database-option.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Logging/Data Link Options Tab Data Link Options Section The Data Link Options section of the Logging/Data Link Options Tab contains the following options: Database Management System —The name of the DBMS to which you want to log data. Because of the different requirements of each DBMS, TestStand mig

### Logging/Data Link Options Tab - Database Options Dialog Box

#### Logging/Data Link Options Tab

#### Data Link Options Section

The Data Link Options section of the Logging/Data Link Options Tab contains the following options:

- Database Management System 
 —The name of the DBMS to which you want to log data. Because of the different requirements of each DBMS, TestStand might log data to each DBMS differently. By default, TestStand supports Microsoft Access, Oracle, Microsoft SQL Server, MySQL, and Sybase. You can select one of the supported DBMS systems using this ring control. TestStand uses this value to determine how to generate SQL scripts and can access the value within expression values in a schema.
- Connection String Expression 
 —The connection string expression TestStand uses to open a data source to log results to. This control requires a string expression which the TestStand process model evaluates at run time. The expression can be a literal value or a string you build using variables or properties. If the value is a literal string, you must encapsulate the string value with quotes (
 "" 
 ).
 Note 
 Refer to the documentation for the database you use to determine whether and how you can communicate to the database securely. National Instruments recommends that you do not use a plain text password to connect to databases with sensitive information. 
 You can update the contents of this control in any of the following ways:
  - Browse 
 —Edits a connection string expression in the
 Expression Browser 
 dialog box.
  - Build 
 —Constructs the connection string using the
 Data Link Properties 
 dialog box.
  - Use .udl File 
 —Specifies a Microsoft Data Link (
 .udl 
 ) filename and updates the Connection String Expression control with the filename, as shown in the following example:
 "FILE NAME=C:\\Program Files\\Common Files\\System\\OLE DB\\Data Links\\Access.udl" 
 The text in the data link file specifies the connection string.
  - Load .udl File 
 —Specifies a Microsoft Data Link (
 .udl 
 ) filename and imports the connection string from the file to the control.
- Save .udl File 
 —Specifies a Microsoft Data Link (
 .udl 
 ) filename and exports the connection string from the control to the file.
- View Data 
 —Launches the
 Database Viewer application 
 and connects to the DBMS using the parameters specified in the connection string.
- Share Data Link Between Executions 
 —Instructs TestStand to share references for connections to a DBMS when multiple executions use the same connection string.
 
 Note 
 You must enable the
 Share Data Link Between Executions
 option to eliminate possible contention for access to a shared database file from multiple executions, and when you enable more than one database result processing plug-ins in the
 [Result Processing](result-processing-dialog-box.html)
 dialog box.

#### See Also

[Data Link Properties dialog box](data-link-properties-dialog-box.html)

[Database Known Issues](/csh?context=ts_tsfundamentals_database_known_issues)

[Database Logging](/csh?context=ts_tsfundamentals_database_connectivity)

[Database Viewer](database-viewer-application.html)

[Expression Browser dialog box](expression-browser-dialog-box.html)

[Configuring Connection Strings](/csh?context=ts_tsref_dbviewer_connectionstrings)

Parent topic:

Logging/Data Link Options Tab - Database Options Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/logging-data-link-options-tab-database-option2.html language=enus -->
## TOPIC 03888: Logging/Data Link Options Tab - Database Options Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/logging-data-link-options-tab-database-option2.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/logging-data-link-options-tab-database-option2.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Logging/Data Link Options Tab The Logging/Data Link Options tab contains the following sections: Logging Options —Specifies general options for database logging, such as the type of data to log, whether TestStand logs to a database after testing a UUT, or whether TestStand logs concurrently with an

### Logging/Data Link Options Tab - Database Options Dialog Box

#### Logging/Data Link Options Tab

The Logging/Data Link Options tab contains the following sections:

- Logging Options 
 —Specifies general options for database logging, such as the type of data to log, whether TestStand logs to a database after testing a UUT, or whether TestStand logs concurrently with an execution.
- Data Link Options 
 —Specifies the data link information the process model requires to connect to a database and log data.

Parent topic:

Database Options Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/logging-data-link-options-tab-database-option3.html language=enus -->
## TOPIC 03889: Logging/Data Link Options Tab - Database Options Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/logging-data-link-options-tab-database-option3.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/logging-data-link-options-tab-database-option3.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Logging/Data Link Options Tab Logging Options Section The Logging Options section of the Logging/Data Link Options tab contains the following options: Disable Database Logging —Enable this option when you do not want TestStand to log data to a database. Use On-The-Fly Logging —Specifies whether Test

### Logging/Data Link Options Tab - Database Options Dialog Box

#### Logging/Data Link Options Tab

#### Logging Options Section

The Logging Options section of the Logging/Data Link Options tab contains the following options:

- Disable Database Logging 
 —Enable this option when you do not want TestStand to log data to a database.
- Use On-The-Fly Logging 
 —Specifies whether TestStand logs to a database after testing a UUT, or logs concurrently with the execution. When you enable this option, the process model uses Post Result callback sequences to process new results. When you disable this option, database logging occurs after the testing of each UUT completes.
 Note 
 If you attempt to use on-the-fly database logging with a schema that uses stored procedure statements or command statements that do not use the INSERT command, you cannot define constraints for foreign keys in step result statements that reference primary keys in a UUT result statement or foreign keys in a step result statement that references its own primary keys. When you define constraints for these types of foreign keys, an error will occur because the on-the-fly database logger cannot execute the statement to create the record that contains the primary key before executing the statement to create the record that contains the foreign key.
 The Generic Recordset (NI) and TS 2.x—4.0 Generic Recordset (NI)
 [database schemas](/csh?context=ts_tsfundamentals_default_teststand_tables)
 use the TOP 1 clause in the command text for all statements, as the following example shows, to improve performance when logging results to a database by preventing the recordset from accessing existing records in the database:
 SELECT TOP 1 * FROM <TABLE NAME>
 This performance improvement is useful when you enable the Use On-The-Fly Logging option for database files larger than 500 MB.
- Include Execution Times 
 —Enable this option when you want to log the total step execution time and the time each
 code module 
 takes to execute.
- Use Transaction Processing 
 —Instructs TestStand to begin a transaction operation before logging each UUT result and commits the transaction operation after logging the UUT results. If TestStand fails to log results for a UUT, TestStand rolls the transaction operation back to prevent the partial results from being logged. This option is not available when you enable Use On-The-Fly-Logging in the Logging Options section.
- Include Step Results 
 —Enable this option when you want to log the results of each step. Disable this option when you only want to include information about each UUT you test.
- Include Measurements 
 —Enable this option when you want to log the measurement values steps acquire. The default schemas recognizes specific step properties as containing values to log. These include properties such as
 Result.Numeric, Result.String 
 , and
 Result.Measurement 
 . For the Numeric Limit Test built-in step type,
 Result.Numeric 
 contains the numeric measurement the step acquires. For the String Value Test built-in step type,
 Result.String 
 contains the measurement value the step returns in string form. For the Multiple Numeric Limit step type,
 Result.Measurement[].Data 
 contains the numeric measurements the step acquires.
- Include Test Limits 
 —Enable this option when you want to log values step types use as test limits. The default schemas recognize specific step properties as containing test limits. These properties include
 Limit.Low 
 ,
 Limit.High 
 ,
 Limit.String 
 , and
 Comp 
 . The Numeric Limit Test compares the measurement value it acquires against
 Limit.Low 
 ,
 Limit.High 
 , or both, and uses
 Comp 
 to select the type of comparison to make. The String Value Test compares the string it acquires against
 Limit.String 
 and uses
 Comp 
 to indicate whether to ignore the case in the comparison.
- Result Filtering Expression 
 —Specifies which step results appear in the database by specifying an expression the database logger evaluates for each step result. The database logger includes the step in the database if the expression evaluates to
 True 
 . You can use any subproperty in the Result property of the step, but you must use
 Logging.StepResult 
 in place of
 Step.Result 
 . For example, if you want to include only failing steps in the database, set the expression to
 Logging.StepResult.Status == "Failed" 
 . You can use the ring control to the right of the Result Filtering Expression control to select one of the following predefined
 expressions 
 :
 
 Open the
 Expression Browser 
 dialog box, in which you can build the expression by clicking the
 Expression Browse 
 button.
  - All Results
  - Exclude Passed/Done/Skipped
  - Passed/Done Only
  - Exclude Flow Control

#### See Also

[Expression Browser dialog box](expression-browser-dialog-box.html)

Parent topic:

Logging/Data Link Options Tab - Database Options Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/logging-teststand-values-to-binary-and-string.html language=enus -->
## TOPIC 03890: Logging TestStand Values to Binary and String Database Column Types

- bundle_id: `teststand-api-reference`
- source_path: `tsref/logging-teststand-values-to-binary-and-string.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/logging-teststand-values-to-binary-and-string.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Database logging supports writing intrinsic values and arrays to binary and string columns. Use the following table to determine how TestStand writes values to binary and string columns. Use the Format control on the Column/Parameter section of the Database Options dialog box to customize how TestSt

### Logging TestStand Values to Binary and String Database Column Types

Database logging supports writing intrinsic values and arrays to binary and string columns. Use the following table to determine how TestStand writes values to binary and string columns.

Use the
 Format
 control on the
 [Column/Parameter](schemas-tab-database-options-dialog-box2.html)
 section of the
 [Database Options](database-options-dialog-box.html)
 dialog box to customize how TestStand writes values to binary columns. The supported formats include 8-byte real (R8), 8-byte integer (I8), 8-byte unsigned integer (UI8), 4-byte real (R4), 4-byte integer (I4), 2-byte integer (I2), and 1-byte integer (I1).

| TestStand Value | Database Column Type |  |  |
| --- | --- | --- | --- |
| Binary | varchar | BSTR |  |
| Number/Enumeration | Use the Format column to specify format. The default format is R8. | Formatted value contains a period decimal point character. | Formatted value contains a period decimal point character. |
| Number/Enumeration {Signed 64-bit Integer} | Use the Format column to specify format. The default format is I8. | Formatted value contains a signed decimal integer. | Formatted value contains a signed decimal integer. |
| Number/Enumeration {Unsigned 64-bit Integer} | Use the Format column to specify format. The default format is UI8. | Formatted value contains an unsigned decimal integer. | Formatted value contains an unsigned decimal integer. |
| Array of Number | TestStand concatenates the binary representation of each value. Use the Format column to specify format. The default format is R8. | TestStand concatenates each formatted value, where the value contains a period decimal point character and \\r\\n delimits each element. | TestStand concatenates each formatted value, where the value contains a period decimal point character and \\r\\n delimits each element. |
| Array of Number {Signed 64-bit Integer} | TestStand concatenates the binary representation of each value. Use the Format column to specify format. The default format is I8. | TestStand concatenates each formatted value, where each value contains a signed decimal integer and \\r\\n delimits each element. | TestStand concatenates each formatted value, where each value contains a signed decimal integer and \\r\\n delimits each element. |
| Array of Number {Unsigned 64-bit Integer} | TestStand concatenates the binary representation of each value. Use the Format column to specify format. The default format is UI8. | TestStand concatenates each formatted value, where each value contains an unsigned decimal integer and \\r\\n delimits each element. | TestStand concatenates each formatted value, where each value contains an unsigned decimal integer and \\r\\n delimits each element. |
| Array Enumeration (All Representations) | TestStand concatenates the binary representation of each numeric value. Use the Format column to specify format. The default format is R8. | TestStand concatenates each formatted value, where the value contains a period decimal point character and \\r\\n delimits each element. For each element value, TestStand adds a prefix of [Index]= , where Index is the element index. | TestStand concatenates each formatted value, where the value contains a period decimal point character and \\r\\n delimits each element. For each element value, TestStand adds a prefix of [Index]= , where Index is the element index. |
| Boolean | Use the Format column to specify format. The default format is I1. | String contains either a 0 or 1 character. | String contains either a 0 or 1 character. |
| Array of Boolean | TestStand concatenates the binary representation of each value. Use the Format column to specify format. The default format is I1. | TestStand concatenates either a 0 or 1 character, and \\r\\n delimits each element. | TestStand concatenates either a 0 or 1 character, and \\r\\n delimits each element. |
| String | TestStand logs the value as a Unicode string. See the Note below this table for more details. | TestStand logs the value as a multi-byte string. See the Note below this table for more details. | TestStand logs the value as a Unicode string. See the Note below this table for more details. |
| Array of String | TestStand concatenates each value as a Unicode string, where the NUL character delimits each element and two NUL characters terminate the value. | TestStand concatenates each value as a multi-byte string, and \\r\\n escapes and delimits each string element. | TestStand concatenates each value as a Unicode string, and \\r\\n escapes and delimits each string element. |
| Reference | Not supported. | Not supported. | Not supported. |
| Array of Reference | Not supported. | Not supported. | Not supported. |
| Container | Not supported. | Not supported. | Not supported. |
| Array of Container (String elements only) | TestStand concatenates each value as a Unicode string, where the NUL character delimits each element and two NUL characters terminate the value. For each element value, TestStand adds a prefix of "[Name]=", where Name is the property name. | TestStand concatenates each value as a multi-byte string, and \\r\\n delimits each element. For each element value, TestStand adds a prefix of "[Name]=", where Name is the property name. | TestStand concatenates each value as a Unicode string, and \\r\\n delimits each element. For each element value, TestStand adds a prefix of "[Name]=", where Name is the property name. |
| Array of Container (Number elements with same type only) | TestStand concatenates the binary representation of each numeric value. Use the Format column to specify format. The default format is R8. | TestStand concatenates each formatted value, where the value contains a period decimal point character and \\r\\n delimits each element. For each element value, TestStand adds a prefix of "[Name]=", where Name is the property name. | TestStand concatenates each formatted value, where the value contains a period decimal point character and \\r\\n delimits each element. For each element value, TestStand adds a prefix of "[Name]=", where Name is the property name. |
| Array of Container (Boolean elements only) | TestStand concatenates the binary representation of each value. Use the Format column to specify format. The default format is I1. | TestStand concatenates either a 0 or 1 character, and \\r\\n delimits each element. For each element value, TestStand adds a prefix of "[Name]=", where Name is the property name. | TestStand concatenates either a 0 or 1 character, and \\r\\n delimits each element. For each element value, TestStand adds a prefix of "[Name]=", where Name is the property name. |
| Array of Container (Array of Number elements with same type only) | TestStand concatenates the binary representation of each numeric value. Use the Format column to specify format. The default format is R8. | TestStand concatenates each formatted value, where the value contains a period decimal point character and \\r\\n delimits each element. For each element value, TestStand adds a prefix of "[Name]=", where Name is the property name. | TestStand concatenates each formatted value, where the value contains a period decimal point character and \\r\\n delimits each element. For each element value, TestStand adds a prefix of "[Name]=", where Name is the property name. |
| Array of Container (Array of Boolean elements only) | TestStand concatenates the binary representation of each value. Use the Format column to specify format. The default format is I1. | TestStand concatenates either a 0 or 1 character, and \\r\\n delimits each element. For each element value, TestStand adds a prefix of "[Name]=", where Name is the property name. | TestStand concatenates either a 0 or 1 character, and \\r\\n delimits each element. For each element value, TestStand adds a prefix of "[Name]=", where Name is the property name. |
| Array of Container (Array of String elements only) | TestStand concatenates each value as a Unicode string, where the NUL character delimits each element and two NUL characters terminate the value. For each element value, TestStand adds a prefix of ""[Name]=", where Name is the property name. | TestStand concatenates each value as a multi-byte string, and \\r\\n escapes and delimits each string element. For each element value, TestStand adds a prefix of "[Name]=", where Name is the property name. | TestStand concatenates each value as a Unicode string, and \\r\\n escapes and delimits each string element. For each element value, TestStand adds a prefix of "[Name]=", where Name is the property name. |
| Array of Container (Heterogeneous with Number, Boolean, and String elements, Array of Number elements, Array of Boolean elements, and Array of String elements only) | Not supported. | String contains multi-byte string, formatted numeric value, or 0 or 1 character, respectively, and \\r\\n delimits each element. For each element value, TestStand adds a prefix of "[Name]=", where Name is the property name. | String contains multi-byte string, formatted numeric value, or 0 or 1 character, respectively, and \\r\\n delimits each element. For each element value, TestStand adds a prefix of "[Name]=", where Name is the property name. |
| Array of Container (Container) | Not supported. | Not supported. | Not supported. |
| Array of Container (Reference) | Not supported. | Not supported. | Not supported. |
| Array of Container (Array of any type other than Number, Boolean, and String elements) | Not supported. | Not supported. | Not supported. |

Note

SetValBinary

Retrieving Binary String Values from Reports and Databases

#### See Also

[Database Options dialog box](database-options-dialog-box.html)

Parent topic:

Schemas Tab - Database Options Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/logout-modified-files-dialog-box.html language=enus -->
## TOPIC 03891: Logout Modified Files Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/logout-modified-files-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/logout-modified-files-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: TestStand launches the Logout Modified Files dialog box when you attempt to log out of TestStand without saving one or more modified files. You can select the files to save before logging out. The list control displays all modified files. Files for which you have permission to save are selected by d

### Logout Modified Files Dialog Box

TestStand launches the Logout Modified Files dialog box when you attempt to log out of TestStand without saving one or more modified files. You can select the files to save before logging out. The list control displays all modified files. Files for which you have permission to save are selected by default, and read-only files are not selected by default. Files for which you do not have permission to save are dimmed.

The Logout Modified Files dialog box contains the following options:

- Save Checked Files 
 —TestStand saves the selected files and continues with logout.
- Logout without Saving 
 —TestStand does not save the files and continues with logout.
- Cancel 
 —TestStand does not save any files and does not logout.

#### See Also

[Close All Windows Modified Files dialog box](close-all-windows-modified-files-dialog-box.html)

[Save All Modified Files dialog box](save-all-modified-files-dialog-box.html)

[Shutdown Modified Files dialog box](shutdown-modified-files-dialog-box.html)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/loop-count-tab-loop-on-selected-steps-dialog.html language=enus -->
## TOPIC 03892: Loop Count Tab - Loop on Selected Steps Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/loop-count-tab-loop-on-selected-steps-dialog.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/loop-count-tab-loop-on-selected-steps-dialog.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Loop Count Tab The Loop Count tab contains the following options: Loop Count —The maximum number of times TestStand executes the selected steps. Loop Indefinitely —When you enable this option, an interactive execution loops indefinitely until a step condition occurs or you terminate or abort the exe

### Loop Count Tab - Loop on Selected Steps Dialog Box

#### Loop Count Tab

The Loop Count tab contains the following options:

- Loop Count 
 —The maximum number of times TestStand executes the selected steps.
- Loop Indefinitely 
 —When you enable this option, an interactive execution loops indefinitely until a step condition occurs or you terminate or abort the execution. When you enable this option, the Loop Count control is disabled.
- Stop on Condition 
 —When you enable this option, TestStand stops the interactive execution when any
 step status 
 is
 Error 
 ,
 Passed 
 , or
 Failed 
 .

Note

Stop Expression

True

Parent topic:

Loop on Selected Steps Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/loop-information-tab.html language=enus -->
## TOPIC 03893: Loop Information Tab

- bundle_id: `teststand-api-reference`
- source_path: `tsref/loop-information-tab.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/loop-information-tab.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Loop Information Tab to specify the following variables: Offset —Specify the numeric variable or property in which to store the current offset during each iteration of the loop. For zero-based one-dimensional arrays, the offset is equal to the index of the array. For multi-dimensional arrays

### Loop Information Tab

Use the Loop Information Tab to specify the following variables:

- Offset 
 —Specify the numeric variable or property in which to store the current offset during each iteration of the loop. For zero-based one-dimensional arrays, the offset is equal to the index of the array. For multi-dimensional arrays, the offset is the linearized index of the array. For streams, the offset is a zero-based counter of the number of loop iterations.
- Iteration 
 —Specify the string variable or property in which to store the current loop iteration. This value represents the loop offset of each parameter in relation to its nesting level. This is a single value to represent the offset of all parameters at the same level.

#### See Also

[Sweep Loop Step](sweep-loop-step.html)

[Sweep Loop Parameters Tab](sweep-parameters-tab.html)

[Sweep Loop Output Tab](output-tab.html)

[Sweep Loop Input Tab](input-tab.html)

Parent topic:

Configure Sweep Loop Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/loop-information-tab2.html language=enus -->
## TOPIC 03894: Loop Information Tab

- bundle_id: `teststand-api-reference`
- source_path: `tsref/loop-information-tab2.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/loop-information-tab2.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Loop Information Tab to specify the following variables: Offset —Specify the numeric variable or property in which to store the current offset during each iteration of the loop. For zero-based one-dimensional arrays, the offset is equal to the index of the array. For multi-dimensional arrays

### Loop Information Tab

Use the Loop Information Tab to specify the following variables:

- Offset 
 —Specify the numeric variable or property in which to store the current offset during each iteration of the loop. For zero-based one-dimensional arrays, the offset is equal to the index of the array. For multi-dimensional arrays, the offset is the linearized index of the array. For streams, the offset is a zero-based counter of the number of loop iterations.
- Iteration 
 —Specify the string variable or property in which to store the current loop iteration. This value represents the loop offset of each parameter in relation to its nesting level. This is a single value to represent the offset of all parameters at the same level.

#### See Also

[Sweep Loop Step](sweep-loop-step.html)

[Sweep Loop Parameters Tab](sweep-parameters-tab.html)

[Sweep Loop Output Tab](output-tab.html)

[Sweep Loop Input Tab](input-tab.html)

Parent topic:

Sweep Loop Edit Tabs

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/loop-on-selected-steps-dialog-box.html language=enus -->
## TOPIC 03895: Loop on Selected Steps Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/loop-on-selected-steps-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/loop-on-selected-steps-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Select Execute»Loop on Selected Steps or select Loop on Selected Steps from the Steps pane context menu to launch the Loop on Selected Steps dialog box, in which you can specify the number of times to loop, as well as a stop expression TestStand evaluates after executing each step. If you execute st

### Loop on Selected Steps Dialog Box

Select
 Execute»Loop on Selected Steps
 or select
 Loop on Selected Steps
 from the
 [Steps](steps-pane-context-menu-sequence-file-window.html)
 pane context menu to launch the Loop on Selected Steps dialog box, in which you can specify the number of times to loop, as well as a stop expression TestStand evaluates after executing each step.

If you execute steps in a Sequence File window, you initiate the interactive execution as an independent, top-level execution. When you execute steps in an Execution window for a suspended sequence execution, you initiate a nested-interactive execution as an extension of the suspended execution.

The Loop on Selected Steps dialog box contains the following tabs:

- Loop Count 
 —The number of loop iterations the interactive execution performs and any stop conditions.
- Stop Expression 
 —A custom expression that determines whether the interactive execution stops.

#### See Also

[Steps Pane Context Menu](steps-pane-context-menu-sequence-file-window.html)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/loop-options-tab-step-properties-dialog-box.html language=enus -->
## TOPIC 03896: Loop Options Tab - Step Properties Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/loop-options-tab-step-properties-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/loop-options-tab-step-properties-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Loop Options Tab The Loop Options tab of the Step Properties dialog box configures an individual step to run repeatedly in a loop when it executes. To loop on several steps at once, place the steps in a new sequence, create a Sequence Call step that calls the sequence, and then loop on the Sequence

### Loop Options Tab - Step Properties Dialog Box

#### Loop Options Tab

The Loop Options tab of the Step Properties dialog box configures an individual step to run repeatedly in a loop when it executes. To loop on several steps at once, place the steps in a new sequence, create a Sequence Call step that calls the sequence, and then loop on the Sequence Call step.

The Loop Options tab contains the following options:

- Loop Type 
 —Specifies one of the following types of looping for the step:
  - None 
 —TestStand does not loop on the step. This is the default value.
  - Fixed number of loops 
 —TestStand loops on the step a specified number of times and determines the final pass or fail status of the step based on the percentage of loop iterations in which the
 step status 
 is
 Passed 
 .
  - Pass/Fail count 
 —TestStand loops on the step until the step passes or fails a specified number of times or until a maximum number of loop iterations complete. TestStand determines the final status of the step based on whether the specified number of passes or failures occurred or whether the maximum number of loop iterations was reached.
  - Custom 
 —Customizes the looping behavior for the step. You can specify a Loop Initialization expression, a Loop Increment expression, a Loop While expression, and a final Loop Status expression. The following example code illustrates the order in which TestStand uses the loop
 expressions 
 :
 Loop_Initialization_Expression;
 while (Loop_While_Expression == True)
 { 
 Execute_Step;
 Loop_Increment_Expression; 
 }
 Loop_Status_Expression;
- Record Result of Each Iteration 
 —Adds the step result to the
 sequence results list 
 after each loop iteration. TestStand also adds the final result it computes for the step loop as a whole if you have enabled the Result Recording Option on the
 Run Options panel 
 of the Step Settings pane for the step.
- Loop Initialization Expression 
 —The expression TestStand evaluates before looping. For the Fixed number of loops option, the expression is
 RunState.LoopIndex = 0 
 .
- Loop Increment Expression 
 —The expression TestStand evaluates before and after executing each step. For the Fixed number of loops option, the expression is
 RunState.LoopIndex += 1 
 .
- Loop While Expression 
 —The expression TestStand evaluates before executing the step. If the expression evaluates to
 True 
 , TestStand executes the step. Otherwise, the looping stops. For the Fixed number of loops option, the default expression is
 RunState.LoopIndex < 10 
 .
- Loop Status Expression 
 —The expression TestStand evaluates to determine the status for the final cumulative result. For the Fixed number of loops option, the default expression is
 RunState.LoopNumPassed / RunState.LoopNumIterations < 1 ? "Failed" : "Passed"

Note

Parent topic:

Step Properties Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/looping-panel-step-settings-pane.html language=enus -->
## TOPIC 03897: Looping Panel - Step Settings Pane

- bundle_id: `teststand-api-reference`
- source_path: `tsref/looping-panel-step-settings-pane.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/looping-panel-step-settings-pane.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Looping Panel The Looping panel configures an individual step to run repeatedly in a loop when the step executes. Use the Loop Type ring control to select the type of looping for the step. TestStand determines the final status of the step based on the number of passes, failures, or loop iterations t

### Looping Panel - Step Settings Pane

#### Looping Panel

The Looping panel configures an individual step to run repeatedly in a loop when the step executes. Use the Loop Type
ring control to select the type of looping for the step. TestStand determines the final status of the step based on the
number of passes, failures, or loop iterations that occur. To loop on several steps at once, place the steps in a new sequence, create a
 [Sequence Call step](sequence-call-step.html)
 that calls the sequence, and then loop on the Sequence Call step.

The Looping panel contains the following options:

- Loop Type 
 —Specifies one of the following types of looping for the step:
  - None 
 —TestStand does not loop on the step. This is the default value.
  - Fixed number of loops 
 —TestStand loops on the step a specified number of times and determines the final pass or fail status of the step based on the percentage of loop iterations in which the
 step status 
 is
 Passed 
 .
  - Pass/Fail count 
 —TestStand loops on the step until the step passes or fails a specified number of times or until a maximum number of loop iterations complete. TestStand determines the final status of the step based on whether the specified number of passes or failures occurred or whether the maximum number of loop iterations was reached.
  - Custom 
 —Customizes the looping behavior for the step. You can specify a Loop Initialization expression, a Loop Increment expression, a Loop While expression, and a final Loop Status expression. The following example code illustrates the order in which TestStand uses the loop
 expressions 
 :
 Loop_Initialization_Expression;
 while (Loop_While_Expression == True)
 { 
 Execute_Step;
 Loop_Increment_Expression; 
 }
 Loop_Status_Expression;
- Record Result of Each Iteration 
 —Adds the step result to the sequence results list after each loop iteration. TestStand also adds the final
 result 
 it computes for the step loop as a whole if you have enabled the Result Recording Option on the
 Run Options panel 
 of the Step Settings pane for the step.
- Loop Count 
 —Use this section to specify the number of times to loop, as well as a stop expression TestStand evaluates after executing each step. This section is available only when you select
 Fixed number of loops 
 or
 Pass/Fail count 
 for the
 Loop Type 
 .
- Loop Initialization Expression 
 —The expression TestStand evaluates before looping. For the Fixed number of loops option, the expression is
 RunState.LoopIndex = 0 
 .
- Loop Increment Expression 
 —The expression TestStand evaluates before and after executing each step. For the Fixed number of loops option, the expression is
 RunState.LoopIndex += 1 
 .
- Loop While Expression 
 —The expression TestStand evaluates before executing the step. If the expression evaluates to
 True 
 , TestStand executes the step. Otherwise, the looping stops. For the Fixed number of loops option, the default expression is
 RunState.LoopIndex < 10 
 .
- Loop Status Expression 
 —The expression TestStand evaluates to determine the status for the final cumulative result. For the Fixed number of loops option, the default expression is
 RunState.LoopNumPassed / RunState.LoopNumIterations < 1 ? "Failed" : "Passed"

Note

#### See Also

[Flow Control Step Types](flow-control-step-types.html)

[Run Options panel](run-options-panel-step-settings-pane.html)

[Sequence Call Step](sequence-call-step.html)

Parent topic:

Properties Tab - Step Settings Pane

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/manage-result-processing-configurations-dialo.html language=enus -->
## TOPIC 03898: Manage Result Processing Configurations Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/manage-result-processing-configurations-dialo.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/manage-result-processing-configurations-dialo.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Select Manage Configurations in the Active Configuration control in the Result Processing dialog box to launch the Manage Result Processing Configurations dialog box, in which you create or delete result processing configurations. You can create multiple result processing configurations, which are n

### Manage Result Processing Configurations Dialog Box

Select
 Manage Configurations
 in the
 Active Configuration
 control in the
 [Result Processing](result-processing-dialog-box.html)
 dialog box to launch the Manage Result Processing Configurations dialog box, in which you create or delete result processing configurations.

You can create multiple result processing configurations, which are named sets of model plug-in instances you configure to accomplish a specific task, such as creating multiple reports with different formats or logging data to multiple databases. Creating multiple report processing configurations to use as the active configuration can help you quickly change how TestStand processes results. You can create result processing configurations to process results inline, meaning at run time, or offline. For example, you can specify to process offline results differently from inline results or you can specify to process offline result files differently when you store the files in different locations.

Use the Active Configuration control in the expanded Result Processing dialog box to select the configuration to use to process results at run time. Use the
 [TestStand Offline Results Processing Utility](/csh?context=ts_tsref_offline_processing_utility)
 to select the configuration to use to process results offline.

The Manage Result Processing Configurations dialog box contains the following options:

- Configuration List 
 —List of result processing configurations. By default, the Manage Result Processing Configurations dialog box includes the following two configurations you can edit but not delete or rename:
  - <Default for Inline Processing> 
 —Default active configuration for processing results at run time.
  - <Default for Offline Processing> 
 —Default configuration the TestStand Offline Results Processing Utility uses.
- Insert New 
 —Inserts a new configuration in the Configuration List.
- Cut 
 —Removes the selected configuration and places it on the clipboard.
- Copy 
 —Copies the selected configuration to the clipboard.
- Paste 
 —Inserts the configuration from the clipboard into the Configuration List.
- Rename 
 —Renames the selected configuration.
- Reset to Defaults 
 —Deletes all configurations and replaces them with only the <Default for Inline Processing> and <Default for Offline Processing> configurations.

#### See Also

[Result Processing dialog box](result-processing-dialog-box.html)

[TestStand Offline Results Processing Utility](/csh?context=ts_tsref_offline_processing_utility)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/measure-operation-edit-ivi-power-supply-step.html language=enus -->
## TOPIC 03899: Measure Operation - Edit IVI Power Supply Step Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/measure-operation-edit-ivi-power-supply-step.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/measure-operation-edit-ivi-power-supply-step.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Measure Operation The Measure operation takes a measurement on the output signal and returns the measured value. This operation causes a voltage and/or current measurement to be taken at the output terminals. You must enable the Measurement extension before using this operation. The returned value i

### Measure Operation - Edit IVI Power Supply Step Dialog Box

#### Measure Operation

The Measure operation takes a measurement on the output signal and returns the measured value. This operation causes a voltage and/or current measurement to be taken at the output terminals. You must enable the Measurement extension before using this operation. The returned value is the actual voltage or current reading.

The Edit IVI Power Supply Step dialog box for the Measure operation contains the following tabs:

- Channels 
 —The channel name and the measurement to perform.
- Operation Settings 
 —Specifies where the dialog box saves and reloads the operation settings.

Parent topic:

Edit IVI Power Supply Step Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/measure-operation-edit-ivi-power-supply-step2.html language=enus -->
## TOPIC 03900: Measure Operation - Edit IVI Power Supply Step Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/measure-operation-edit-ivi-power-supply-step2.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/measure-operation-edit-ivi-power-supply-step2.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Measure Operation Operation Settings Tab The Operation Settings tab for the Measure operation contains the following channel-specific option: Settings Property/Variable —The name of the property or variable in which TestStand stores the settings when you click OK in this dialog box. Click Load to re

### Measure Operation - Edit IVI Power Supply Step Dialog Box

#### Measure Operation

#### Operation Settings Tab

The Operation Settings tab for the Measure operation contains the following channel-specific option:

- Settings Property/Variable 
 —The name of the property or variable in which TestStand stores the settings when you click
 OK 
 in this dialog box. Click
 Load 
 to reload the settings from the specified property or variable location.

Parent topic:

Measure Operation - Edit IVI Power Supply Step Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/menu-tab-step-type-properties-dialog-box.html language=enus -->
## TOPIC 03901: Menu Tab - Step Type Properties Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/menu-tab-step-type-properties-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/menu-tab-step-type-properties-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Menu Tab Use the Menu tab to specify the menu item name that appears for the step type in the Insert Step context menu. Use the Step Type Menu Editor dialog box to organize the Step Types list of the Insertion Palette and the Insert Step submenu of the Steps pane context menu . The Menu tab contains

### Menu Tab - Step Type Properties Dialog Box

#### Menu Tab

Use the Menu tab to specify the menu item name that appears for the step type in the Insert Step context menu. Use the
 [Step Type Menu Editor](step-type-menu-editor-dialog-box.html)
 dialog box to organize the
 [Step Types list](insertion-palette-pane.html)
 of the
 [Insertion Palette](insertion-palette-pane.html)
 and the Insert Step submenu of the
 [Steps pane context menu](steps-pane-context-menu-sequence-file-window.html)
 .

The Menu tab contains the following options:

- Item Name Expression 
 —An expression for the step type name that appears in the Insert Step submenu.
 Note 
 If you specify a literal string in this control, you must enclose it in double quotation marks. When you want to use a name from a
 [string resource file](/csh?context=ts_tsfundamentals_resource_strings_format)
 , use the
 ResStr
 expression function to retrieve the name from the file.

Use the
 [Step Type Menu Editor](step-type-menu-editor-dialog-box.html)
 dialog box to organize the Step Types list of the
 [Insertion Palette](insertion-palette-pane.html)
 and the Insert Step submenu of the
 [Steps](steps-pane-context-menu-sequence-file-window.html)
 pane context menu.

#### See Also

[Insertion Palette](insertion-palette-pane.html)

[Step Type Menu Editor dialog box](step-type-menu-editor-dialog-box.html)

[Steps Pane Context Menu](steps-pane-context-menu-sequence-file-window.html)

Parent topic:

Step Type Properties Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/menus-execution-profiler.html language=enus -->
## TOPIC 03902: Menus - Execution Profiler

- bundle_id: `teststand-api-reference`
- source_path: `tsref/menus-execution-profiler.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/menus-execution-profiler.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Menus The Execution Profiler includes the following menus. File menu Edit menu View menu Help menu

### Menus - Execution Profiler

#### Menus

The Execution Profiler includes the following menus.

- File 
 menu
- Edit 
 menu
- View 
 menu
- Help 
 menu

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/menus-teststand-file-diff-and-merge-utility.html language=enus -->
## TOPIC 03903: Menus - TestStand File Diff and Merge Utility

- bundle_id: `teststand-api-reference`
- source_path: `tsref/menus-teststand-file-diff-and-merge-utility.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/menus-teststand-file-diff-and-merge-utility.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Menus The TestStand File Diff and Merge utility contains File, Edit, View, Search, and Help menus. The File menu contains the following options: Select Files to Diff —Launches the Select Files dialog box, in which you select the files you want to compare. Save Modified Files —Writes the content of t

### Menus - TestStand File Diff and Merge Utility

#### Menus

The TestStand File Diff and Merge utility contains File, Edit, View, Search, and Help menus.

The File menu contains the following options:

- Select Files to Diff 
 —Launches the
 Select Files 
 dialog box, in which you select the files you want to compare.
- Save Modified Files 
 —Writes the content of the files to disk. This option is available only when you compare two files.
- Save File 1 
 —Writes the content of File 1 to disk. This option is available only when you compare two files.
- Save File 1 As 
 —Writes the content of File 1 to disk using a new name you specify. The utility shows the new filename in the
 File list 
 and
 Differences table 
 . This option is available only when you compare two files.
- Save File 2 
 —Writes the content of File 2 to disk. This option is available only when you compare two files.
- Save File 2 As 
 —Writes the content of File 2 to disk using a new name you specify. The utility shows the new filename in the
 File list 
 and
 Differences table 
 . This option is available only when you compare two files.
- Save Merged File 
 —Writes the content of the merged file to disk. If a conflict exists in the merged file, the save fails. This option is available only when you compare three files.
- Save Merged File As 
 —Writes the content of the merged file to disk using a new name you specify. The utility shows the new filename in the
 File list 
 and
 Differences table 
 . This option is available only when you compare three files.
- Generate Report 
 —Launches the
 Generate Report 
 dialog box, in which you can specify a file path for an XML that documents the differences found or merges performed in the specified files.
- Exit 
 —Closes the current utility session.

The Edit menu contains the following option:

- Options 
 —Launches the
 File Differ Options 
 dialog box, in which you can configure settings for the utility, including options for loading and automatically merging types, managing type conflict resolution, and so on.

The View menu contains the following options:

- Show/Hide 
 —Launches a submenu that contains the following options for showing or hiding controls in the utility.
  - File List 
 —Show or hide the File list.
  - Filters 
 —Show or hide the
 Filters 
 tab.
- Collapse All 
 —Collapses all items in the Differences table.
- Expand All 
 —Expands all items in the Differences table.
- Rediff Files 
 —Compares the selected files again. When you compare three files, this option recreates the merged file.
- Switch Sides 
 —Swaps File 1 and File 2. The utility swaps filename and contents in the
 File list 
 and
 Differences table 
 . This option is available only when you compare two files.

The Search menu contains the following options:

- Find Next Difference 
 —Navigates to the next difference among the files. The utility determines the item with focus and steps into the item to find the next difference.
- Find Previous Difference 
 —Navigates to the previous difference among the files. The utility determines the item with focus and steps into the item to find the previous difference.
- Find Next Difference Over 
 —Navigates to the next difference among the files. The utility determines the item with focus and steps over the item to find the next difference.
- Find Previous Difference Over 
 —Navigates to the previous difference among the files. The utility determines the item with focus and steps over the item to find the previous difference.
- Find Next Conflict 
 —Navigates to the next conflict among the files. This option is available only when you compare three files and conflicts exist in the merged file.
- Find Previous Conflict 
 —Navigates to the previous conflict among the files. This option is available only when you compare three files and conflicts exist in the merged file.

The Help menu contains the following options:

- NI TestStand Help 
 —Launches the
 NI TestStand Help 
 .
- Help 
 —Displays the primary
 TestStand File Diff and Merge Utility 
 help topic.
- About TestStand File Differ 
 —Displays version information for the utility.

#### See Also

[File Differ Options dialog box](file-differ-options-dialog-box.html)

[Generate Report dialog box](generate-report-dialog-box.html)

[Select Files dialog box](select-files-dialog-box.html)

Parent topic:

TestStand File Diff and Merge Utility

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/menus-teststand-sequence-analyzer-application.html language=enus -->
## TOPIC 03904: Menus - TestStand Sequence Analyzer Application

- bundle_id: `teststand-api-reference`
- source_path: `tsref/menus-teststand-sequence-analyzer-application.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/menus-teststand-sequence-analyzer-application.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Menus The stand-alone TestStand Sequence Analyzer application contains File, Edit, Project, and Help menus. The File menu contains the following options: New Sequence Analyzer Project —Creates a new analyzer project. Open Sequence Analyzer Project —Opens an existing analyzer project. Close —Closes t

### Menus - TestStand Sequence Analyzer Application

#### Menus

The stand-alone TestStand Sequence Analyzer application contains File, Edit, Project, and Help menus.

The File menu contains the following options:

- New Sequence Analyzer Project 
 —Creates a new analyzer project.
- Open Sequence Analyzer Project 
 —Opens an existing analyzer project.
- Close 
 —Closes the analyzer project.
- Save 
 —Writes the content of the analyzer project to disk.
- Save As 
 —Writes the content of the analyzer project to disk using a new name you specify.
- Most Recently Used Projects 
 —Lists the most recently opened analyzer projects.
- Exit 
 —Closes the current sequence analyzer session.

The Edit menu contains the following options:

- Available Rules 
 —Launches the
 Configure Sequence Analyzer Available Rules 
 dialog box, in which you create and edit custom analyzer rules and analysis modules.
- Sequence Analyzer Options 
 —Launches the
 Sequence Analyzer Options 
 dialog box, in which you specify options to enable debugging of LabVIEW analyzer modules and to cache sequence files during analysis.

The Project menu contains the following options:

- Analyze 
 —Starts analyzing the analyzer project and shows messages on the
 Messages 
 tab as the sequence analyzer generates each message.
- Stop Analysis 
 —Stops analyzing the analyzer project. The sequence analyzer waits for the currently executing analysis modules to complete before stopping the analysis.
- Generate Analysis Report 
 —Launches a file dialog box in which you can save an XML report file to use in an external viewer for the most recent analysis. The XML file uses the
 AnalyzerReportViewer.xsl 
 style sheet located in the
 [<TestStand>](/csh?context=ts_tsfundamentals_directories)
 \Components\Stylesheets\Analyzer 
 directory. Use the
 XML Packaging Utility 
 to package the files necessary to view the XML report on a computer that does not have TestStand installed.
 When you generate a report file, the sequence analyzer provides a snapshot of the most recent analysis, including a list of the analyzed files, a list of the rules and settings used during the analysis, and a list of all the generated messages.

The Help menu contains the following options:

- NI TestStand Help 
 —Launches the
 NI TestStand Help 
 .
- Help Topic 
 —Displays the help topic for the item you currently have selected.
- About Sequence Analyzer 
 —Displays version information for the sequence analyzer.

#### See Also

[Configure Sequence Analyzer Available Rules dialog box](configure-sequence-analyzer-available-rules-d.html)

[Sequence Analyzer Options dialog box](sequence-analyzer-options-dialog-box2.html)

[XML Packaging Utility](xml-packaging-utility.html)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/menus.html language=enus -->
## TOPIC 03905: Menus

- bundle_id: `teststand-api-reference`
- source_path: `tsref/menus.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/menus.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: The menus at the top of the Sequence Editor window contain commands common to other applications, such as Open, Save, Copy, and Paste, as well as commands specific to TestStand. You can customize the toolbars and menus to organize the available commands in the sequence editor menus and define the ic

### Menus

The menus at the top of the Sequence Editor window contain commands common to other applications, such as Open, Save, Copy, and Paste, as well as commands specific to TestStand. You can
 [customize the toolbars and menus](/csh?context=ts_tsref_customizing_toolbars_menus)
 to organize the available commands in the sequence editor menus and define the icon, text, and shortcut for each command.

#### See Also

[Customizing Toolbars and Menus](/csh?context=ts_tsref_customizing_toolbars_menus)

Parent topic:

TestStand Sequence Editor Menus, Panes, and Windows

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/merge-tab-select-files-dialog-box.html language=enus -->
## TOPIC 03906: Merge Tab - Select Files Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/merge-tab-select-files-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/merge-tab-select-files-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Merge Tab The Merge tab contains the following options: Base —File path of the base sequence file from which modified versions originate. File 1 —File path of the first modified sequence file. File 2 —File path of the second modified sequence file. Merged —File path of the resulting merged file to c

### Merge Tab - Select Files Dialog Box

#### Merge Tab

The Merge tab contains the following options:

- Base 
 —File path of the base sequence file from which modified versions originate.
- File 1 
 —File path of the first modified sequence file.
- File 2 
 —File path of the second modified sequence file.
- Merged 
 —File path of the resulting merged file to create.

Click the
 Switch Files
 button to reorder the Base, File 1, and File 2 paths.

You must specify all files before you can click
 OK
 .

Parent topic:

Select Files Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/message-popup-edit-tabs.html language=enus -->
## TOPIC 03907: Message Popup Edit Tabs

- bundle_id: `teststand-api-reference`
- source_path: `tsref/message-popup-edit-tabs.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/message-popup-edit-tabs.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Message Popup edit tabs in the TestStand Sequence Editor to specify the settings for a Message Popup step. The Step Settings pane for a Message Popup step contains the following tabs: Text and Buttons —The text for the title and buttons, as well as button behaviors. Options —Specifies whethe

### Message Popup Edit Tabs

Use the Message Popup edit tabs in the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 to specify the settings for a Message Popup step.

The Step Settings pane for a Message Popup step contains the following tabs:

- Text and Buttons 
 —The text for the title and buttons, as well as button behaviors.
- Options 
 —Specifies whether the dialog box displays a response text box, and an image or a web page.
- Layout 
 —The modality settings, the location of the dialog box, and the arrangement of the controls on the dialog box.

#### See Also

[Built-In Step Types](built-in-step-types.html)

Parent topic:

Message Popup Step

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/message-popup-edit-tabs2.html language=enus -->
## TOPIC 03908: Message Popup Edit Tabs

- bundle_id: `teststand-api-reference`
- source_path: `tsref/message-popup-edit-tabs2.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/message-popup-edit-tabs2.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Layout Tab The Layout tab contains the following options: Center Dialog —Positions the dialog box at the center in relation to the screen. Left Coordinate —An expression that determines the position of the dialog box relative to the left side of the screen. Top Coordinate —An expression that determi

### Message Popup Edit Tabs

#### Layout Tab

The Layout tab contains the following options:

- Center Dialog 
 —Positions the dialog box at the center in relation to the screen.
  - Left Coordinate 
 —An expression that determines the position of the dialog box relative to the left side of the screen.
  - Top Coordinate 
 —An expression that determines the position of the dialog box relative to the top of the screen.
- Control Arrangement 
 —The order, location, alignment, and other miscellaneous options for the controls on the dialog box.
  - Control Order 
 —The order of the message, response, and file controls on the dialog box.
  - Button Location 
 —Specifies where to position the buttons on the dialog box.
  - Button Alignment 
 —The alignment of the buttons on the dialog box.
- Dialog Options 
 —Specifies the following miscellaneous options for the dialog box:
  - Make Floating 
 —When you enable this option, the dialog box stays on top of the TestStand application. You can interact with the main application window while the dialog box is visible.
  - Make Modal 
 —When you enable this option, the dialog box is modal to the TestStand application. You cannot interact with the main application window until the dialog box is dismissed.
  - Resize Option 
 —When you enable this option, you can resize the dialog box.
 Note 
 This option is not available when the dialog box is modal.

Parent topic:

Message Popup Edit Tabs

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/message-popup-edit-tabs3.html language=enus -->
## TOPIC 03909: Message Popup Edit Tabs

- bundle_id: `teststand-api-reference`
- source_path: `tsref/message-popup-edit-tabs3.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/message-popup-edit-tabs3.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Options Tab The Options tab contains the following options: Enable Response Textbox —When you enable this option, a string control displays to prompt the operator for a response. Initial Response String —The initial string that appears in the dialog box. Use the Font/Color Selection button to specif

### Message Popup Edit Tabs

#### Options Tab

The Options tab contains the following options:

- Enable Response Textbox 
 —When you enable this option, a string control displays to prompt the operator for a response.
  - Initial Response String 
 —The initial string that appears in the dialog box. Use the
 Font/Color Selection 
 button to specify the font and the background color for the response text.
  - Max Response String Length 
 —The maximum number of characters a user can input for the string. If you do not want to specify a maximum response string length, enter -1 in this control.
  - Number of Lines Visible 
 —The number of visible text lines in the response text box.
- Display Image or Web Page 
 —Specifies whether to display an image (
 .gif 
 ,
 .bmp 
 ,
 .ico 
 ,
 .jpg 
 ,
 .jpeg 
 ,
 .png 
 ) or a web page (
 .htm 
 ,
 .html 
 ,
 .xhtml 
 ,
 .shtml 
 ,
 .mht 
 ,
 .mhtml 
 ,
 .txt 
 ,
 .xml 
 ,
 .asp 
 ) in the dialog box.
  - File Source 
 —Specifies where the step loads the file from. You can select from the following options:
    - File 
 —A literal path to the file to load.
    - File By Expression 
 —An expression that evaluates a path to the file to load.
    - Step 
 —Imports a file into the step.
  - File Pathname 
 —The path or expression to the file to load when you select
 File 
 or
 File by Expression 
 as the File Source.
  - Imported Filename 
 —The file to import when you select
 Step 
 as the
 File Source 
 .
  - Import 
 —Loads the specified file into the step.
 Note 
 If you import a web page into the step, you cannot use relative paths to external files within the web page.

Parent topic:

Message Popup Edit Tabs

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/message-popup-edit-tabs4.html language=enus -->
## TOPIC 03910: Message Popup Edit Tabs

- bundle_id: `teststand-api-reference`
- source_path: `tsref/message-popup-edit-tabs4.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/message-popup-edit-tabs4.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Text and Buttons Tab The Text and Buttons tab contains the following options: Title Expression —The text the step displays as the title of the Configure Message Popup Step dialog box. The default value is NameOf<Step> , where <Step> is the name of the Message Popup step. You can specify a literal st

### Message Popup Edit Tabs

#### Text and Buttons Tab

The Text and Buttons tab contains the following options:

- Title Expression 
 —The text the step displays as the title of the Configure Message Popup Step dialog box. The default value is
 NameOf<Step> 
 , where
 <Step> 
 is the name of the Message Popup step. You can specify a literal string or string expression TestStand evaluates at run time.
- Message Expression 
 —The text the step displays as the message in the Configure Message Popup Step dialog box. You can specify a literal string or string expression TestStand evaluates at run time. Click
 Font/Color Selection 
 to specify the font for the message text and the background color of the panel.
- Button Label Expressions 
 —This section contains six button labels you can use to specify literal strings or string
 expressions 
 TestStand evaluates at run time. The button does not appear when the label is empty. You must specify text for at least one button. You can enter a double underscore character before the letter you want to use as a shortcut key, for example,
 __OK 
 enables the <Alt-O> shortcut, and
 E__xit 
 enables the <Alt-X> shortcut. Click the
 Font/Color Selection 
 button to specify the font for the label text and the background color of the button. You can customize the layout of the buttons on the Layout tab of the Message Popup Edit pane.
- Button Options 
 —TestStand associates the following buttons with various default behaviors of dialog boxes.
  - Default 
 —Specifies which button, if any, uses <Enter> as the shortcut key.
  - Cancel 
 —Specifies which button, if any, uses <Esc> as the shortcut key.
  - Active Control 
 —Specifies one of the six buttons or the input string as the initially active control.
  - Timeout 
 —Specifies which message box button activates automatically after a timeout period expires.
  - Time to Wait (sec) 
 —The timeout period in seconds. Use this option to create a Message Popup step that displays a notification message which automatically dismisses itself after a short delay, such as when an operator is not present to acknowledge the message.

Parent topic:

Message Popup Edit Tabs

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/message-popup-step.html language=enus -->
## TOPIC 03911: Message Popup Step

- bundle_id: `teststand-api-reference`
- source_path: `tsref/message-popup-step.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/message-popup-step.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use a Message Popup step to display messages to the user and to receive response strings from the user. For example, you can use a Message Popup step to warn the user when a calibration routine fails. By default, Message Popup steps do not pass or fail. After a step executes, TestStand sets the step

### Message Popup Step

Use a Message Popup step to display messages to the user and to receive response strings from the user. For example, you can use a Message Popup step to warn the user when a calibration routine fails.

By default, Message Popup steps do not pass or fail. After a step executes, TestStand sets the
 [step status](/csh?context=ts_tsfundamentals_step_status_values_table)
 to
 Done
 or
 Error
 .

#### Configuring the Step

Use the
 [Message Popup edit tabs](message-popup-edit-tabs.html)
 in the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 and the
 [Configure Message Popup Step](configure-message-popup-step-dialog-box.html)
 dialog box in a
 [TestStand User Interface](teststand-user-interfaces.html)
 to specify the settings for the Message Popup step.

#### Step Properties

In addition to the
 [common custom properties](/csh?context=ts_tsfundamentals_custom_result_props)
 , the Message Popup step type defines the following step properties:

- Step.Result.ButtonHit 
 —The one-based index of the button you select.
- Step.Result.Response 
 —The response text the user entered.
- Step.TitleExpr 
 —The expression for the string that appears as the title of the message popup dialog box.
- Step.MessageExpr 
 —The expression for the string that appears as the text message in the message popup dialog box.
- Step.MessageFontData 
 —The font for the text message in the message popup dialog box.
- Step.Button1Label 
 ,
 Button2Label 
 ,
 Button3Label 
 ,
 Button4Label 
 ,
 Button5Label 
 , and
 Button6Label 
 —The expression for the label text for each button.
- Step.ButtonFontData 
 —The font for the label text for buttons in the message popup dialog box.
- Step.ShowResponse 
 —Enables the response text box control in the message popup dialog box.
- Step.NumberLines 
 —The number of visible text lines in the response text box.
- Step.MaxResponseLength 
 —The maximum number of characters the user can enter in the response text box control.
- Step.RespFontData 
 —The font for the response text box control in the message popup dialog box.
- Step.DefaultResponseExpr 
 —The initial text string the step displays in the response text box control.
- Step.FileData 
 —The step displays an image or web page in the message popup dialog box.
- Step.ActiveCtrl 
 —Identifies one of the six buttons or the input string as the active control.
- Step.DefaultButton 
 —Specifies which button, if any, uses
 <Enter> 
 as a shortcut key.
- Step.CancelButton 
 —Specifies which button, if any, uses
 <Esc> 
 as a shortcut key.
- Step.TimerButton 
 —The index of the button that activates automatically after a timeout elapses. A value of zero indicates no timeout occurs.
- Step.TimeToWait 
 —The number of seconds before the button
 Step.TimerButton 
 specifies activates.
- Step.Position.Top 
 and
 Step.Position.Left 
 —The location of the message popup dialog box when CenterDialog is
 False 
 .
- Step.CenterDialog 
 —The message popup dialog box appears in the center of the screen.
- Step.Modal 
 —The message popup dialog box is modal to the TestStand application.
- Step.Floating 
 —The message popup dialog box appears on top of the TestStand application.
- Step.CtrlArrangement 
 —The order for the controls in the message popup dialog box.
- Step.ButtonLocation 
 —Specifies whether to display the buttons on the bottom or side of the message popup dialog box.
- Step.ButtonAlignment 
 —Specifies whether to align the buttons in the center, left, right, top, or bottom of the message popup dialog box.
- Step.ResizeDialog 
 —Specifies whether the message popup dialog box is resizable.

#### See Also

[Built-In Step Types](built-in-step-types.html)

Parent topic:

Built-In Step Types

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/messages-tab-context-menu-teststand-sequence.html language=enus -->
## TOPIC 03912: Messages Tab Context Menu - TestStand Sequence Analyzer Application

- bundle_id: `teststand-api-reference`
- source_path: `tsref/messages-tab-context-menu-teststand-sequence.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/messages-tab-context-menu-teststand-sequence.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Messages Tab Messages Tab Context Menu Right-click an item in the Messages list on the Messages tab to launch the context menu, which can contain the following options depending on the item you select: Goto Location —Opens the TestStand file and locates the object that caused the message. You can al

### Messages Tab Context Menu - TestStand Sequence Analyzer Application

#### Messages Tab

#### Messages Tab Context Menu

Right-click an item in the Messages list on the Messages tab to launch the context menu, which can contain the following options depending on the item you select:

- Goto Location 
 —Opens the TestStand file and locates the object that caused the message. You can also double-click a message in the Messages list to go to the location of the object in the TestStand file that caused the message.
- Mark Message as Ignored in Analyzer Project 
 —Ignores the messages you select in subsequent analysis sessions and moves the messages from the Active Messages view of each Messages tab that includes the messages to the
 Messages the Analyzer Project Ignores 
 view of each tab. When you mark a message as ignored, the sequence analyzer prompts you for text that provides the justification to ignore the message. The Justification to Ignore column displays the text you enter for the messages. 
 Select this option only when you are sure the issue will not cause a run-time error. For example, if the subsequent analyzer session reports an undefined local variable in a step expression and you know a step in the sequence creates that local variable, you can safely ignore the error message. As another example, if the TestStand Sequence Analyzer warns about a potentially unused variable and you know a
 code module 
 uses the variable, you can safely ignore the message.
 When you mark a message as ignored, the sequence analyzer adds a copy of the ignored message to the list of ignored messages in the current analyzer project. The sequence analyzer ignores the message in subsequent analysis sessions for the current analyzer project.
 If the sequence analyzer generates a message when analyzing a file that contains a TestStand type, the analyzer also generates a nearly identical message when analyzing other files that contain the same type. The messages for each file differ only with respect to the specified filename. When you mark any of these messages as ignored, the analyzer ignores the messages for all files that contain the type.
 Disable a rule on the
 Rules 
 tab of the TestStand Sequence Analyzer application to ignore all messages for that rule in subsequent analysis.
- Mark Message as Fixed 
 —Marks the messages you select as fixed and moves the messages from the Active Messages view of each Messages tab that includes the messages to the Fixed view of each tab. When you mark an issue as fixed, the sequence analyzer reports the message again in subsequent analysis sessions if you do not fix the issue itself.
- Mark Message as Active 
 —Marks the messages you select as active and moves the messages from the ignored messages view or the Messages Fixed view of each Messages tab that includes the messages to the Active Messages view of each tab.
- Delete Message 
 —Removes the messages you select from the current project. This option is available only for dimmed messages in the ignored messages view, which indicates that the most recent analysis of the current, sequence file, or workspace file did not generate the message.
- Goto Rule 
 —Locates the rule on the Rules tab of the sequence analyzer application so you can disable or configure the rule.
- Columns 
 —Launches the Columns context menu, which you use to show and hide columns. The Text column menu item is always dimmed because you cannot hide the Text column.

Parent topic:

Messages Tab - TestStand Sequence Analyzer Application

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/messages-tab-teststand-sequence-analyzer-appl.html language=enus -->
## TOPIC 03913: Messages Tab - TestStand Sequence Analyzer Application

- bundle_id: `teststand-api-reference`
- source_path: `tsref/messages-tab-teststand-sequence-analyzer-appl.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/messages-tab-teststand-sequence-analyzer-appl.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Messages Tab Use the Messages tab to view and resolve the messages for the most recent analysis of the current TestStand Sequence Analyzer project, sequence file, or workspace file in the order in which the analyzer generated them. The sequence analyzer overwrites the content of the Messages tab eac

### Messages Tab - TestStand Sequence Analyzer Application

#### Messages Tab

Use the Messages tab to view and resolve the messages for the most recent analysis of the current TestStand Sequence Analyzer project, sequence file, or workspace file in the order in which the analyzer generated them. The sequence analyzer overwrites the content of the Messages tab each time you start an analysis session.

The Analyzer Messages tab contains the following controls:

- Show 
 —Filters the messages to show in the Messages list. You can also show the list of analyzed files. The Show ring control contains the following options:
  - Active Messages 
 —Shows the messages in the current analyzer project, sequence file, or workspace file that represent the issues you must address by marking the message as ignored or fixed.
  - Ignored Messages 
 —Shows the messages in the current analyzer project, sequence file, or workspace file that you marked to ignore in future analysis. The sequence analyzer maintains this list and does not report these messages again in subsequent analysis sessions.
 Right-click a message and select
 Mark Message as Active 
 from the context menu to return the message to the Active Messages view.
 Dimmed messages in the Ignored Messages view indicate that the most recent analysis of the current project, sequence file, or workspace file did not generate the message. You cannot make dimmed messages active, but you can right-click the dimmed message and select
 Delete Message 
 from the context menu to remove the message from the current project.
  - Messages Marked as Fixed 
 —Shows the messages in the current analyzer project, sequence file, or workspace file that you marked as fixed. The sequence analyzer reports these messages again in future analysis sessions if you do not fix the issue itself.
 Right-click a message and select
 Mark Message as Active 
 from the
 context menu 
 to return the message to the Active Messages view.
- Group By 
 —Specifies how to group the messages in the Messages list. Click the column headers to resort the list. The Group By ring control contains the following options:
  - <None> 
 —Shows the messages in the order in which the sequence analyzer generated them.
  - Severity 
 —Groups the messages in alphabetical order by message severity level.
  - Rule 
 —Groups the messages in alphabetical order by the rule associated with each message.
  - Category 
 —Groups the messages in alphabetical order by the category of the rule associated with each message.
  - Text 
 —Groups the messages in alphabetical order by the message text.
  - File 
 —Groups the messages in alphabetical order by the file that generated the message.
  - Location 
 —Groups the messages in alphabetical order by the property path of the object that generated the message.
- Messages List 
 —List of messages for the current analyzer project, sequence file, or workspace file in the order in which the sequence analyzer generated them. The sequence analyzer adds new messages to the bottom of the list.
 Right-click the list to display the context menu, which you use to resolve each message and specify which columns to show or hide. You can also right-click the column header to show or hide columns. Click the column header to resort the messages in the list. Drag the column header to reorder the columns.
- Message Details 
 —Details for the analysis message you select, including suggestions for how to fix the related issue. This control is empty when you select more than one message.
- Generate Analysis Report 
 —Saves the messages for the most recent analysis in an XML report file to use in an external viewer. The XML file uses the
 AnalyzerReportViewer.xsl 
 style sheet, located in the
 [<TestStand>](/csh?context=ts_tsfundamentals_directories)
 \Components\Stylesheets\Analyzer 
 directory. Use the
 XML Packaging Utility 
 to package the files necessary to view the XML report on a computer that does not have TestStand installed.
 When you generate a report file, the sequence analyzer provides a snapshot of the most recent analysis, including a list of the analyzed files, a list of the rules and settings used during the analysis, and a list of all the generated messages.

#### See Also

[Messages Tab Context Menu](messages-tab-context-menu-teststand-sequence.html)

[XML Packaging Utility](xml-packaging-utility.html)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/mode-tab-teststand-deployment-utility.html language=enus -->
## TOPIC 03914: Mode Tab - TestStand Deployment Utility

- bundle_id: `teststand-api-reference`
- source_path: `tsref/mode-tab-teststand-deployment-utility.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/mode-tab-teststand-deployment-utility.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Mode Tab Use the Mode tab to create a full deployment or a patch deployment and to specify related settings for each type of deployment. The options on this tab apply only to the type of deployment you create. Changing the type of deployment might change the options available on this tab. The Mode t

### Mode Tab - TestStand Deployment Utility

#### Mode Tab

Use the Mode tab to create a full deployment or a
 [patch](/csh?context=ts_tsdeploysystem_createpatch)
 deployment and to specify related settings for each type of deployment.

Note

type of deployment

The Mode tab contains the following options:

- Deployment Version 
 —Indicates the software version number to use to identify the deployment. The deployment utility auto increments the version by default each time you update the deployment.
  - MSI-based installers 
 —The version number has the format
 X.X.X 
 . After a successful build, the third number in the version increments. If you enable the Lock to Deployment Version option on the Advanced Installer Options dialog box, the Version option on the Mode tab also determines the installer version number.
  - Package-based installers 
 —The version number has the format
 X.X.X.X 
 . After a successful build, the fourth number in the version increments. If you enable the Lock to Deployment Version option on the Configure Package Options dialog box, the Version option on the Mode tab determines the package version number.
- Output type 
 —Select one of the following build outputs. Refer to the Choosing a Build Output topic for more information about how to select the best setting for your application.
  - Deployable Image Only 
 —The deployment files are moved to the specified image directory on the System Source tab.
  - MSI-Based Installer 
 —In addition to the deployable image, the deployment utility creates an installer to distribute the system. When you select this option, the Installer tab is enabled, which you can use to configure the installer.
  - Package-Based Distribution 
 —In addition to the deployable image, the deployment utility creates a package distribution. When you select this option, the Package Distribution Options tab is enabled, which you can use to configure the package distribution. You can configure the package output type using the options below:
    - Single Package 
 —The files in the image directory are packaged into a single .nipkg file. Dependencies you select are referenced by the package, and must be installed on the deployment target to install the package.
    - Repository 
 —In addition to the main package, all dependent packages are also included in the deployment (the repository). A feed is generated which references all included packages in the repository. To install the deployment, you can register the feed in NI Package Manager on the target machine.
    - Package Installer 
 —In addition to the main package, all dependent packages are also included in the deployment. A standalone installer is generated which installs all the packages on a machine. The installer will also install NI Package Manager if it is not present on the machine.
- Create new Full Deployment 
 —Creates a new full deployment that contains all the files in the test system.
- Create new Patch Deployment 
 —Creates a new patch deployment that contains only the subset of files that have changed since the previous full or
 dependency patch deployment 
 . This option is available only when you have previously created a full deployment.
 Note 
 (32-bit TestStand) You must use the 32-bit TestStand Deployment Utility to create a patch for a 32-bit full deployment. (64-bit TestStand) You must use the 64-bit TestStand Deployment Utility to create a patch for a 64-bit full deployment. Create a new full deployment to update a 32-bit test system to a 64-bit test system.
- Depend on previous Full Deployment 
 —Creates a patch deployment based on the previous full deployment.
- Depend on previous Baseline Patch Deployment 
 —Creates a patch deployment based on the previous
 baseline patch deployment 
 . This option is available only when you have previously created a baseline patch deployment.
- Make Baseline Patch Deployment 
 —Designates a patch deployment as a
 baseline patch deployment 
 , which you can use to create dependency patch deployments that contain only the files that differ from the previous patch deployment version of the file.
 TestStand supports only one baseline patch deployment at a time, and you can create a baseline patch deployment only from the most recent patch deployment you created. You must designate a patch deployment as a baseline patch deployment before you create another patch deployment. If you create another baseline patch deployment, you can no longer depend on the previous baseline patch deployment. Creating a new deployment also erases data of previous patch deployments that you do not designate as baseline patch deployments.
 This option is available only when you have previously created a patch deployment.
- User Files to Include 
 —Contains the following options to control which files to include in the patch deployment.
 Note 
 This option is not available for package-based distributions. Patch deployments for path distributions always contain user files.
  - Modified Files 
 —Includes new or modified files from the previous full or baseline patch deployment in the patch deployment. You might need to also include files you did not explicitly modify to ensure that all the included files execute correctly.
 When you select this option, the deployment utility creates a temporary full
 deployable image 
 , compares the checksums of all the files in the temporary full deployable image to the checksums of all the files in the previous full deployable image to generate a list of modified files, and then deletes all but the modified files from the temporary full deployable image to create the patch deployable image.
  - None 
 —Does not include any files from the previous full or baseline patch deployment in the patch deployment. Use this option to build a patch deployment installer that contains only updated drivers and components.
  - Manual Mode 
 —Use this option to
 manually specify 
 files to include, to include additional files, and to replace existing files in the patch deployment.
- Upgrades and Patches to Include 
 —Contains the following options to control which updates and patches to deploy for National Instruments products in the patch deployment.
 Note 
 This option is not available for package-based distributions. Patch deployments for patch distributions always update the TestStand runtime and drivers.
  - TestStand Runtime and Drivers 
 —Includes all installed TestStand Runtime and National Instruments driver updates and patches that support redistribution.
  - TestStand Runtime 
 —Includes all available TestStand Runtime updates and patches that support redistribution.
  - Drivers 
 —Includes all available National Instruments driver updates and patches that support redistribution.
  - None 
 —Does not include any TestStand Runtime or National Instruments driver updates or patches.
- Overview 
 —Describes the User Files to Include option you select.

#### See Also

[Creating Dependency Patch Deployments](/csh?context=ts_tsdeploysystem_createpatch)

[Patching Deployments](/csh?context=ts_tsdeploysystem_createpatch)

Parent topic:

TestStand Deployment Utility

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/model-options-dialog-box.html language=enus -->
## TOPIC 03915: Model Options Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/model-options-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/model-options-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Select Configure»Model Options to launch the Model Options dialog box. The Model Options dialog box contains one or more of the following options, depending on which process model is selected: Number of Test Sockets —The number of UUTs the system can test simultaneously. The Parallel and Batch proce

### Model Options Dialog Box

Select
 Configure»Model Options
 to launch the Model Options dialog box.

The Model Options dialog box contains one or more of the following options, depending on which process model is selected:

- Number of Test Sockets 
 —The number of UUTs the system can test simultaneously. The Parallel and Batch process models launch a separate test sequence execution for each test socket.
 When running under a model, a sequence can inspect the value of
 RunState.TestSockets.MyIndex
 to determine the zero-based index of the test socket on which it is running. The value of
 RunState.TestSockets.Count
 indicates the number of test sockets in the system. 
 This option is available only when you are using the Batch or Parallel process models.
- Hide Execution Windows 
 —When you enable this option, the user interface application does not display the Execution window and report for individual test socket executions. This option is available only when you are using the Batch or Parallel process models.
- Tile Execution Windows 
 —When you enable this option, the user interface application arranges test socket Execution windows so they do not overlap. This option is available only when you are using the Batch or Parallel process models. The
 TestStand Sequence Editor 
 honors this option when displaying windows in tabs or in separate windows. The example
 TestStand User Interfaces 
 do not support this option.
- Bring UUT Dialog to Front When Status Changes 
 —Enable this control to activate the UUT dialog box whenever a UUT completes testing or when a test socket execution terminates. This option is available only when you are using the Parallel process model.
- Sequential Batch Mode 
 —When you enable this option, the model runs test socket executions one at a time in ascending test socket order. This option is available only when you are using the Batch process model.
- Default Batch Synchronization 
 —The
 batch synchronization 
 for sequence files that do not change their Batch Synchronization setting from the default value of
 Use model setting 
 .
 Because the default batch synchronization setting for a step is
 Use sequence file setting
 and the default batch synchronization setting for a sequence file is
 Use model setting
 , setting the Default Batch Synchronization setting in the model effectively changes the batch synchronization setting for all steps that do not specify a non-default setting. This option is available only when you are using the Batch model.
- Discard Results or Disable Results when not Required by Model 
 —Specifies if the process model discards results after the Post Result callback sequences execute when using
 on-the-fly report generation 
 or
 database logging 
 , or disables result collection for the execution when report generation and database logging are disabled. This option is available when you are using the Sequential, Parallel, or Batch process models.
 Note 
 If you have configured the process model to use multiple process model plug-ins, the process model discards or disables results only when you have configured all process model plug-ins to process results on-the-fly.

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/model-tab-sequence-properties-dialog-box.html language=enus -->
## TOPIC 03916: Model Tab - Sequence Properties Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/model-tab-sequence-properties-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/model-tab-sequence-properties-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Model Tab The Model tab contains the following options: Type —Lists the different types of sequences a process model file can contain. The following are the different types of sequences: Normal —Any sequence other than a callback sequence or entry point. When you select this option, nothing else app

### Model Tab - Sequence Properties Dialog Box

#### Model Tab

The Model tab contains the following options:

- Type 
 —Lists the different types of sequences a process model file can contain. The following are the different types of sequences:
  - Normal 
 —Any sequence other than a callback sequence or entry point. When you select this option, nothing else appears on the Model tab.
  - Callback 
 —Model callbacks are sequences entry point sequences call and the client sequence file can override. When you select this option, the following control is visible:
    - Copy Steps and Local Variables When Creating an Overriding Sequence 
 —Determines the behavior of TestStand when you click
 Add 
 in the
 Sequence File Callbacks 
 dialog box to create an overriding sequence in the client file. When you enable this option, TestStand copies all the steps and local variables in the callback sequence in the model file to the callback sequence you create in the client file. TestStand always copies the sequence parameters regardless of the option setting.
  - Execution Entry Point 
 and
 Configuration Entry Point 
 —Each entry point is a sequence in the process model file that invokes a test sequence file from the menus in the
 TestStand Sequence Editor 
 or a
 TestStand User Interface 
 . When you select either of these entry points, the following controls appear on the Model tab:
    - Entry Point Name Expression 
 —A string expression for the menu item name of the entry point. If you specify a literal string for the menu item name, you must enclose it in double quotation marks. To store the name in a
 string resource file 
 , use the
 ResStr 
 expression function to retrieve the name from the file.
    - Entry Point Enabled Expression 
 —A Boolean expression TestStand evaluates to determine whether to enable the menu item for the entry point. If the expression evaluates to
 False 
 , TestStand dims the entry point in the menu. If the expression is empty, the entry point in the menu.
    - Menu Hint 
 —A menu for the entry point. If you leave the Menu Hint control empty, TestStand uses the default menu for the entry point type. To specify the menu for the entry point, select one of the following options from the ring control:
 File 
 ,
 Edit 
 ,
 View 
 ,
 Execute 
 ,
 Debug 
 ,
 Configure 
 ,
 Window 
 , and
 Help 
 .
 You can enter one or more names directly in the control. If you specify multiple names, you must separate them with commas. TestStand uses the first menu name in the list it can find in the user interface. This option is useful when you use multiple user interfaces that have different menu names. If TestStand cannot find any menus in the user interface with the names you list in the control, it uses the default menu for the entry point type.
    - Allow Interactive Execution of Entry Point 
 —When you enable this option, you can invoke the entry point for steps you run interactively.
    - Entry Point Ignores Client File 
 —Prevents the sequence from using the client file. This option prevents TestStand from preloading the client sequence file when you run the entry point, even if the client sequence file is set to preload when execution begins. For example, the Configure Result Processing entry point uses this option so the
 Configure»Result Processing 
 command is available for you to use even when TestStand is unable to preload the modules in the active sequence file.
 Note 
 If you are using the equivalent legacy TestStand 2010 process models, the Configure Report Options entry point uses this option so the
 Configure»Report Options
 command is available for you to use even when TestStand is unable to preload the modules in the active sequence file. 
 When you run the entry point, TestStand uses the callback implementations in the model file regardless of whether the client file overrides them.
    - Hide Entry Point Execution 
 —Prevents TestStand from displaying an Execution window for the execution of the entry point. When you enable this option, you do not see a window for the execution unless a run-time error or breakpoint occurs.
    - Save Modified Sequence Files Before Execution 
 —Causes TestStand to save the contents of windows to disk when you invoke the entry point. If this option is enabled when you run the entry point, TestStand checks all windows that have pathnames. When one or more windows have changes you have not yet saved, TestStand prompts you to save the changes. When you click
 Yes 
 , TestStand saves the files.
    - Show Entry Point Only in Editor 
 —Causes the entry point to only appear in the sequence editor and not in the user interfaces.
    - Show Entry Point for All Windows 
 —Causes the entry point to appear in the menu regardless of the type of currently active window, if any. For example, because the Configure Result Processing entry point configures the result processing options for the model and has no client-specific effects, you might want to access it from any window or even when no window is active. When you enable this option, TestStand dims the remaining two options.
 Note 
 If you are using the equivalent legacy TestStand 2010 process models, the Configure Report Options entry point configures the report options for the model and has no client-specific effects, you might want to access it from any window or even when no window is active. When you enable this option, TestStand dims the remaining two options.
    - Show Entry Point when Client File Window is Active 
 —Causes the entry point to appear in the menu when a Sequence File window is the active window. For example, the Execution entry points appear in the Execute menu only when a sequence file is active.
    - Show Entry Point when Execution Window is Active 
 —Causes the entry point to appear in the menu when an Execution window is the active window.

#### See Also

[Sequence File Callbacks dialog box](select-sequence-file-callbacks-dialog-box.html)

Parent topic:

Sequence Properties Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/model-tab-station-options-dialog-box.html language=enus -->
## TOPIC 03917: Model Tab - Station Options Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/model-tab-station-options-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/model-tab-station-options-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Model Tab The Model tab specifies the model options for the station and for sequences. The Model tab contains the following options: Use Station Model —Enables the Station Model control, which specifies the pathname of the station model sequence file. When you disable this option, no station model i

### Model Tab - Station Options Dialog Box

#### Model Tab

The Model tab specifies the model options for the station and for sequences.

The Model tab contains the following options:

- Use Station Model 
 —Enables the Station Model control, which specifies the pathname of the station model sequence file. When you disable this option, no station model is in effect and individual sequence files have no process model unless they explicitly specify one. Usually, sequence files do not explicitly specify process model files.
- Allow Other Models 
 —Allows sequence files to specify a process model file other than the current station model file. When you disable this option, you can only load sequence files that do not specify a process model file and sequences that specify the current station model file as their process model file. Use the
 Advanced 
 tab of the
 Sequence File Properties 
 dialog box to specify a specific process model for a client sequence file.
- Station Model 
 —The pathname of the station model sequence file.

#### See Also

[Sequence File Properties dialog box](sequence-file-properties-dialog-box.html)

Parent topic:

Station Options Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/modified-types-warning-dialog-box.html language=enus -->
## TOPIC 03918: Modified Types Warning Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/modified-types-warning-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/modified-types-warning-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: TestStand launches the Modified Types Warning dialog box when all of the following conditions are true: You select File»Save . The sequence file or type palette contains types marked as modified . The Before Saving Modified Types option on the File tab of the Station Options dialog box is set to Pro

### Modified Types Warning Dialog Box

TestStand launches the Modified Types Warning dialog box when all of the following conditions are true:

- You select
 File»Save 
 .
- The sequence file or type palette contains
 types marked as modified 
 .
- The Before Saving Modified Types option on the
 File 
 tab of the
 Station Options 
 dialog box is set to
 Prompt to Increment Version Types 
 .

The Modified Types Warning dialog box contains the following options:

- Modified Types 
 —Displays a list of types which are currently marked as modified.
- Increment Type Versions 
 —Instructs TestStand to increment the version of the type.
  - Version Number to Increment 
 —Specifies whether to increment the Major, Minor, Revision, or Build Number in the version.
- Do Not Increment Type Versions 
 —When you enable this option, TestStand saves the types without incrementing the version of the types.
  - Remove Modified Mark From Types 
 —When you enable this option, the modified mark for types is removed before saving.
- Save these settings and do not prompt again 
 —Instructs TestStand to use the specified settings as the default in the future. You can edit the default settings on the
 File 
 tab of the
 Station Options 
 dialog box.

#### See Also

[Station Options dialog box](station-options-dialog-box.html)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/modify-boolean-value-dialog-box.html language=enus -->
## TOPIC 03919: Modify Boolean Value Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/modify-boolean-value-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/modify-boolean-value-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: TestStand launches the Modify Boolean Value dialog box when you attempt to display the properties of an element of an array of Booleans. The Modify Boolean Value dialog box contains the following options: Name —The name of the property, and the index of an array property such as MyArray[0] . Boolean

### Modify Boolean Value Dialog Box

TestStand launches the Modify Boolean Value dialog box when you attempt to display the properties of an element of an array of Booleans.

The Modify Boolean Value dialog box contains the following options:

- Name 
 —The name of the property, and the index of an array property such as
 MyArray[0] 
 .
- Boolean Value 
 —The value of the array element, or the initial or default value variables, parameters, or properties you create with the data type use.

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/modify-numeric-value-dialog-box.html language=enus -->
## TOPIC 03920: Modify Numeric Value Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/modify-numeric-value-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/modify-numeric-value-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: TestStand launches the Modify Numeric Value dialog box when you attempt to display the properties of an element of an array of numerics. The Modify Numeric Value dialog box contains the following options: Name —The name of the property, and the index of an array property such as MyArray[0] . Numeric

### Modify Numeric Value Dialog Box

TestStand launches the Modify Numeric Value dialog box when you attempt to display the properties of an element of an array of numerics.

The Modify Numeric Value dialog box contains the following options:

- Name 
 —The name of the property, and the index of an array property such as
 MyArray[0] 
 .
- Numeric Value 
 —The value of the array element, or the initial or default value all variables, parameters, or properties you create with the data type use.

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/modify-reference-value-dialog-box.html language=enus -->
## TOPIC 03921: Modify Reference Value Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/modify-reference-value-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/modify-reference-value-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: TestStand launches the Modify Reference Value dialog box when you attempt to display the properties of an element of an array of references. The Modify Reference Value dialog box contains the following options: Name —The name of the property, and the index of an array property such as MyArray[0] . R

### Modify Reference Value Dialog Box

TestStand launches the Modify Reference Value dialog box when you attempt to display the properties of an element of an array of references.

The Modify Reference Value dialog box contains the following options:

- Name 
 —The name of the property, and the index of an array property such as
 MyArray[0] 
 .
- Reference Value 
 —The value of the array element, or the initial or default value all variables, parameters, or properties you create with the data type use.
- Release 
 —Sets the value of the array element to
 Nothing 
 .

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/modify-string-value-dialog-box.html language=enus -->
## TOPIC 03922: Modify String Value Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/modify-string-value-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/modify-string-value-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: TestStand launches the Modify String Value dialog box when you attempt to display the properties of an element of an array of strings. The Modify String Value dialog box contains the following options: Name —The name of the property, and the index of an array property such as MyArray[0] . String Val

### Modify String Value Dialog Box

TestStand launches the Modify String Value dialog box when you attempt to display the properties of an element of an array of strings.

The Modify String Value dialog box contains the following options:

- Name 
 —The name of the property, and the index of an array property such as
 MyArray[0] 
 .
- String Value 
 —The value of the array element, or the initial or default value all variables, parameters, or properties you create with the data type use.

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/module-qualified-name-and-qualified-name.html language=enus -->
## TOPIC 03923: Module Qualified Name and Qualified Name

- bundle_id: `teststand-api-reference`
- source_path: `tsref/module-qualified-name-and-qualified-name.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/module-qualified-name-and-qualified-name.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: The Module Qualified Name is used to specify the VI selected from a project in a LabVIEW NXG module. This value specifies the VI that will be run when the step is executed in the LabVIEW NXG Development system. It has the following format: <Target Name> : <ComponentName.gcomp>:<Qualified Name of VI>

### Module Qualified Name and Qualified Name

The Module Qualified Name is used to specify the VI selected from a project in a LabVIEW NXG module. This value specifies the VI that will be run when the step is executed in the LabVIEW NXG Development system. It has the following format:
 <Target Name> : <ComponentName.gcomp>:<Qualified Name of VI>

The Qualified Name of a VI is used to specify the VI selected in a GLL in a LabVIEW NXG module. This value determines which VI from the GLL specified is executed when the module is run in the LabVIEW NXG Runtime Engine. It is the value displayed in the Fully Qualified Name window in the Item tab of the gcomp document that contains the VI, when the VI is selected in LabVIEW NXG. It has the following format:
 <NameSpace>:<OptionalNestedNameSpace1>:<OptionalNestedNameSpace2>..:<OptionalNestedNameSpacen>:VIName.gvi

An example of Module Qualified Name:
 PC:Library.gcomp:Main:Measurements:TestVoltage.gvi

The Qualified Name in the example above:
 Main:Measurements:TestVoltage.gvi

The Module Qualified Name and the Qualified Name of a LabVIEW NXG module must always be in sync, with the Qualified Name being a part of the Module Qualified Name. This ensures that the same VI runs for a LabVIEW NXG module, whether it is being run in the Development System in the context of a project or in the Runtime Engine, from a GLL.

The Module Qualified Name consists of the following:

- Target Name 
 —The target for which the component(gcomp) is selected to build. A component can have multiple targets in LabVIEW NXG but the LabVIEW NXG module will use the GLL that is built for the target specified in the Module Qualified Name.
- Component Name 
 —The component name specified the name of the component that the VI belongs to, including the
 .gcomp 
 extension.
- Namespaces 
 —The Component name is followed by one or more colon separated namespaces that the VI belongs to.
- VI Name 
 —The name of the VI including the
 .gvi 
 extension

The Namespaces and VI Name also constitute the Qualified Name of the VI.

#### Module Properties Modified When the Module Qualified Name Is Updated

When the Module Qualified Name of a LabVIEW NXG module is specified, the following properties of the module are also populated:

- Qualified Name
- Target
- Component Absolute Qualified Name
- VI Absolute Qualified Name

#### Module Properties Modified When the Qualified Name Is Updated

The Qualified Name of a VI can be selected when the step is configured to run in the Runtime engine. When this property is updated, the Module Qualified Name property also gets updated to reflect the new VI being called. The Module Qualified Name is only updated if it is a valid non-empty value.

Parent topic:

LabVIEW NXG Module Tab

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/module-tab-edit-c-c-dll-call-dialog-box.html language=enus -->
## TOPIC 03924: Module Tab - Edit C/C++ DLL Call Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/module-tab-edit-c-c-dll-call-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/module-tab-edit-c-c-dll-call-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Module Tab The Module tab contains the following options: Module Pathname —The pathname of the DLL file that contains the function the step calls. You can specify an absolute or relative pathname for the DLL file. Relative pathnames are relative to the TestStand search directory paths. Use the Edit

### Module Tab - Edit C/C++ DLL Call Dialog Box

#### Module Tab

The Module tab contains the following options:

- Module Pathname 
 —The pathname of the DLL file that contains the function the step calls. You can specify an absolute or relative pathname for the DLL file. Relative pathnames are relative to the TestStand search directory paths. 
Use the
 Edit Search Directories 
 dialog box to
 customize the search directory paths 
 .
- Function Name 
 —Selects the function in the
 code module 
 the step calls. If a DLL file contains a type library or if a type library exists with the same name as the DLL file, the C/C++ DLL Adapter automatically populates the Function Name ring control with all of the function names in the type library. Otherwise, the C/C++ DLL Adapter reads the DLL file and finds the names of all
 functions the DLL exports 
 . The C/C++ DLL Adapter also includes the names of exported, static C++ class methods that use data types TestStand supports. When a DLL type library contains links to a help file for a function, you can click the
 ? 
 button to access the help.
- Reload Prototype 
 —Allows the user to refresh the parameter information for the function call. When you create a DLL using LabWindows/CVI 7.1 or later, TestStand can read the prototype information for the currently selected function without the use of a type library.
- Edit Prototype 
 —Enables you to edit the function prototype. The C/C++ DLL Adapter disables this control when it reads a function prototype from the code module type library. Enable this control to manually edit the function prototype.
- Parameters Table 
 —Shows all of the available parameters for the function call and an entry for the return value. The Parameters Table control contains the following columns:
 
 If a DLL file contains a type library or if a type library exists with the same base name as the DLL file that resides in the same directory as the DLL file, the C/C++ DLL Adapter queries the type library for the parameter list information. In addition, if a DLL file contains export information, such as C++ type information Visual Studio creates, the C/C++ DLL Adapter obtains the parameter list information from the DLL file. If the adapter finds parameter list information for the function it displays, it automatically updates the Parameters section when you select a new function in the Function Name ring control. You can request the C/C++ DLL Adapter to query the type information for the currently selected function at any time by clicking
 Reload Prototype 
 . If the module file does not have type information, you must enter parameter information manually.
 When you select a parameter in the view, the specific details about it are displayed in the Parameter Details Table control. To insert or remove parameters, click
 New
 or
 Delete
 . To rearrange the parameter order, select the parameter you want to move and click
 Move Up
 or
 Move Down
 . You must select the
 None
 code template before attempting to insert, remove or rearrange parameters.
  - Name 
 —A symbolic name for the parameter.
 Note 
 Parameters with attributes include an Edit Attributes button in the Name column of the Parameters Table. TestStand associates parameter attributes with the module parameter, which TestStand stores with the step configuration information, not with the parameter value that TestStand passes to the module. Right-click an item in the Parameters Table to access the
 [Parameters Table](for-specify-module-dialog-boxes-parameters-ta.html)
 context menu, from which you can launch the
 [Attributes](attributes-dialog-box.html)
 dialog box. You cannot edit attributes for the real and imaginary parts of complex parameters and complex vector parameters in the C/C++ DLL Adapter.
  - Description 
 —The short description of the parameter type using C++ syntax.
  - Log 
 —When you enable this option, the step logs the parameter as an additional result. Enabling this option is equivalent to using the checkbox next to the additional result name in the
 Additional Results 
 dialog box. For in/out parameters, enabling this option enables the [In] parameter and the [Out] parameter in the Additional Results dialog box. This option is indeterminate for in/out parameters if you specify to log only the [In] parameter value or only the [Out] parameter value. If this option is indeterminate, a tooltip specifies whether the Additional Results dialog box specifies to log the [In] parameter value or the [Out] parameter value.
  - Value Expression 
 —The argument expression to pass.
- Parameter Details Table 
 —The data type of each parameter and additional information according to each parameter type.
 
 Note 
 The C/C++ DLL Adapter supports numeric return values, which includes Boolean, void*, and void.
  - Category 
 —A group of data types to list in the Data Type control. The following categories are available in the Category ring control:
 Numeric 
 ,
 Boolean 
 ,
 String 
 ,
 Enumeration 
 ,
 Object 
 ,
 TS Object 
 ,
 C Struct 
 ,
 Arrays 
 , selected
 C++ class 
 , and
 Pointer/Handle 
 types.
- Prototype 
 —The prototype of the specified function in C/C++ syntax.
- Function Call 
 —Directly edits the function name and all of function arguments at once.

#### Editing the Function Call

You can use the various controls on the Module tab to edit the function name and the argument values of the function. You can also use the Function Call control to directly edit the function name and all of the function arguments at once. In the Function Call control, edit the call just as you would in a source code editor. If you enter a different number of arguments than the function prototype specifies, TestStand launches the
 [Prototypes Conflict](prototypes-conflict-dialog-box.html)
 dialog box, in which you can alter the prototype to match the number of arguments you specify.

When you make a change in the Function Call control, the following buttons appear while all other controls dim:

- Browse 
 —Inserts variables, properties, or
 expression operators 
 into the Function Call control.
- Go to Error 
 —Goes to the highlighted syntax error in the Function Call control.
- Accept 
 —Applies the changes you make in the Function Call control.
- Revert 
 —Discards the changes you make in the Function Call control.

Note

#### See Also

[Additional Results dialog box](additional-results-dialog-box.html)

[Attributes dialog box](attributes-dialog-box.html)

[Edit Search Directories dialog box](edit-search-directories-dialog-box.html)

[Exporting Class Methods and Functions in Microsoft Visual Studio](/csh?context=ts_tsref_exporting_in_net)

[Locating the Correct DLL in 32-bit TestStand and 64-bit TestStand](/csh?context=ts_tsfundamentals_64locatingdlls)

[Expression Operators](/csh?context=ts_tsfundamentals_operators_expression)

[Parameters Table Context Menu for Specify Module Dialog Boxes](for-specify-module-dialog-boxes-parameters-ta.html)

[Prototypes Conflict dialog box](prototypes-conflict-dialog-box.html)

[Using Side-by-Side Versions of the LabWindows/CVI Run-Time Engine with TestStand](/csh?context=ts_tsfundamentals_sxscvirte)

[Using the $(Platform) Path Macro to Locate the Correct Code Module in 32-bit TestStand and 64-bit TestStand](/csh?context=ts_tsfundamentals_64platformmacro)

Parent topic:

Edit C/C++ DLL Call Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/module-tab-edit-labview-vi-call-dialog-box.html language=enus -->
## TOPIC 03925: Module Tab - Edit LabVIEW VI Call Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/module-tab-edit-labview-vi-call-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/module-tab-edit-labview-vi-call-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Module Tab You can use the Module tab to complete the following tasks: Specify whether the step calls a member VI from a LabVIEW class or calls a VI that is a not a member of a LabVIEW class Select the LabVIEW project that refers to the VI (optional) Select the VI the step executes Create and edit a

### Module Tab - Edit LabVIEW VI Call Dialog Box

#### Module Tab

You can use the Module tab to complete the following tasks:

- Specify whether the step calls a member VI from a LabVIEW class or calls a VI that is a not a member of a LabVIEW class
- Select the LabVIEW project that refers to the VI (optional)
- Select the VI the step executes
- Create and edit a VI or an optional LabVIEW project in LabVIEW
- Select an Express VI and convert an Express VI to a standard VI
- Specify whether LabVIEW shows the front panel of the VI when TestStand calls the VI

Use the Module tab of the Edit LabVIEW VI Call dialog box to configure the LabVIEW module. The Module tab contains the following options:

- Call Type 
 —The type of call the step uses. Select one of the following options. The option you select affects the other options available on the tab.
  - VI Call 
 —TestStand calls the VI without LabVIEW dynamic dispatching.
  - Class Member Call 
 —Select a member VI from a LabVIEW class. LabVIEW activates dynamic dispatching when required. When you select Class Member Call, you cannot execute the member call remotely.
 Note 
 You must have LabVIEW 2012 or later to use LabVIEW dynamic dispatching when calling LabVIEW classes in TestStand.
  - Property Node Call 
 —Configures a Property Node call for a LabVIEW I/O reference or a LabVIEW class.
 Note 
 You must have LabVIEW 2013 or later to run a Property Node call. You must use the LabVIEW 2013 Development Environment to configure the Property Node call.
- Project Path 
 —The path of the LabVIEW project the step uses. The control contains a most recently used (MRU) list of the last five selected LabVIEW projects. Specifying a LabVIEW project is optional.
- Browse for LabVIEW Project 
 —Launches the Select the Step's LabVIEW Project File dialog box, in which you can browse for the LabVIEW project (
 .lvproj 
 ) file to open.
- Create LabVIEW Project 
 —Creates an empty LabVIEW project. If the LabVIEW project you specify does not already exist, the LabVIEW Adapter creates it. If the file already exists, the LabVIEW Adapter prompts you to overwrite the existing file.
- Edit LabVIEW Project 
 —Edits an existing LabVIEW project.
- Select Express VI 
 —Use the LabVIEW browse button to select the Express VI you want to call. The LabVIEW browse button displays a pop-up menu that lists all the Express VIs found in the currently selected LabVIEW functions palette view. To select an Express VI not found in the menu, select the
 Browse 
 menu item. Once you select an Express VI, you can configure the VI call.
 Note 
 Calls to Express VIs are embedded within the sequence file, not stored on disk.
- Convert Express VI to Standard VI 
 —Converts an Express VI to a standard VI by detaching the Express VI from the module, creating a standard VI on disk that calls the Express VI, and reconfiguring the module to call the new VI. You must distribute this wrapper VI with the sequence file.
- Show VI Front Panel 
 —When you enable this option, the front panel of the VI opens when the LabVIEW Adapter calls the VI.
- Create VI 
 —Creates a code shell for the VI. If the VI file you specify does not already exist, the LabVIEW Adapter creates it. If the file already exists, the LabVIEW Adapter prompts you to overwrite the existing file. If a VI code template file exists for the step type you are using for the step, the LabVIEW Adapter uses the template to create the new VI.
- Edit VI 
 —Edits an existing VI. If the step uses a LabVIEW project, the VI opens in the LabVIEW project.
 Note 
 This button uses the label Open VI when you have specified a VI in a LabVIEW packed project library. If the step uses an Express VI, the button uses the label Configure VI and configures the Express VI the wrapper VI calls.
- Reload VI Prototype 
 —Allows the user to refresh the parameter information of the VI.
- Show VI Help 
 —Displays the help associated with the VI.
- VI Parameter Table 
 —Contains information about each control or indicator wired to the connector pane of the VI. These are the parameters of the VI.
 
 Note 
 The VI Parameter Table displays parameters according to the order in the VI context help image.
  - Parameter Name 
 —Caption text or label text, if no caption exists, of the control or indicator.
 Note 
 Parameters with attributes include an
 Edit Attributes
 button in the Name column of the VI Parameter Table. You can edit attributes for fields of containers and elements of arrays. TestStand associates parameter attributes with the module parameter, which TestStand stores with the step configuration information, not with the parameter value that TestStand passes to the module. Right-click an item in the VI Parameter Table to access the
 [VI Parameter Table](for-specify-module-dialog-boxes-parameters-ta.html)
 context menu, from which you can launch the
 [Attributes](attributes-dialog-box.html)
 dialog box.
  - Type 
 —TestStand
 equivalent data type 
 for the control or indicator.
 For one-dimensional arrays, you can specify an expression value for the entire array, or you can specify values for each element of the array. Use the plus (
 + 
 ) buttons to insert a new element in the array, and the minus (
 - 
 ) buttons to remove specific elements from the array.
When you select
 Binary String 
 in the Type column of the VI Parameter Table on the LabVIEW Module tab to store a LabVIEW string that contains binary data in a TestStand property, TestStand handles the string data in different ways depending on the version of LabVIEW you are using, as the following table describes.
 LabVIEW Version
 TestStand BehaviorLabVIEW 2012 or later Development System on a non-multibyte operating system
 LabVIEW 2009 SP1 or later Development System on a multibyte operating system
 LabVIEW 2009 SP1 or later RTE on any operating system
 TestStand compresses the binary data, encodes the compressed data, and stores the compressed data using only printable ASCII characters. To pass a compressed string to a VI, select
 Binary String
 in the Type column. TestStand unencodes and decompresses the binary data the string stores before passing it to the VI.
 LabVIEW 2011 SP1 or earlier Development System on a non-multibyte operating system
 LabVIEW 2009 or earlier Development System on a multibyte system
 LabVIEW 2009 or earlier RTE on any operating system
 TestStand escapes the string before storing it and substitutes hexadecimal codes for the unprintable characters, such as the NUL character, in the string. To pass an escaped string to a VI, select
 Binary String
 in the Type column. TestStand unescapes the string before passing it to the VI and substitutes the correct character values for the hexadecimal values in the escaped string. 
 Note 
 To retrieve the raw binary data stored in a string variable in TestStand, call the
 
 [PropertyObject.GetValBinary](../tsapiref/propertyobject-getvalbinary.html)
 method of the TestStand API. See the
 [Retrieving Binary String Values from Reports and Databases](/csh?context=ts_tsreports_retrievingbinarystrings)
 topic for more information about retrieving binary data from string values.
    - Create/Update Custom Data Type 
 —Launches the
 Create/Update Custom Data Type from Cluster 
 dialog box, in which you can configure a new custom data type or update an existing custom data type.
    - Apply Cluster Passing Changes 
 —Updates a VI parameter that contains a subproperty that no longer maps to the correct cluster element. You can use this button to update the parameter and automatically map the subproperty to the correct cluster element.
 This button might also appear when TestStand
 cannot automatically map a subproperty to the correct element 
 and the Value column of the VI Parameter Table contains a '??? <Unknown Value>' error for the subproperty.
  - In/Out 
 —Specifies whether the parameter is an input (control on the VI front panel wired to the connector pane) or an output (indicator on the VI front panel wired to the connector pane).
  - Default 
 —When you enable this option, TestStand uses the default value of the control for the parameter, cluster element, or array element. This option is not available when the terminal of the VI is marked as Required.
  - Value 
 —A TestStand expression. For input parameters, TestStand passes the value of this expression to the VI unless you place a checkmark in the option in the Default column. For output parameters, TestStand stores the data the VI outputs in the location this expression specifies. To help you enter an expression in the Value column, click the
 Expression Browse 
 button to launch the
 Expression Browser 
 dialog box. For enumerated types, a combo box displays all valid values for the type. You can also use an expression with an enumerated type.
 Note 
 For Express VIs, specify a valid value for each control on the connector pane to prevent an error when you configure or run the VI.
- VI Context Help Image and Description 
 —Displays the context help image of the VI as shown in the LabVIEW Context Help window and displays the description of the VI from the Documentation tab of the LabVIEW VI Properties dialog box. When you click a label or terminal of the VI icon, TestStand highlights the parameter in the VI Parameter Table.

#### Specifying a VI

The LabVIEW Module tab contains the following options when you select
 VI Call
 from the Call Type ring control.

- VI Path 
 —The path of the VI the step calls. The path specifies a different location, depending on if the VI is an Express VI or whether the VI is contained in a LabVIEW project, as the following table describes.
 VI Type
 BehaviorExpress VI
 The path specifies the name of the Express VI.
 A VI that is not contained in a LabVIEW project
 The path is the path to the VI on disk, within a LLB, or within a packed project library.
 A VI that is contained in a LabVIEW project
 The path is the URL of the VI within the project instead of an absolute or relative path. 
 The VI Path ring control contains the following options, in which you can specify if the VI is a standard VI or a wrapper for an Express VI. The control contains an MRU list of the last five selected VIs. If a workspace is opened, the MRU list also contains all of the VIs in the workspace for which TestStand can calculate an absolute path. A line divides the most recently selected VIs and the VIs found in the workspace.
- Browse for VI 
 —Launches an
 Open File 
 dialog box, in which you can browse for an independent VI, a LabVIEW library (
 .llb 
 ), or LabVIEW packed project library (
 .lvlibp 
 ) file to open. The LabVIEW Module tab provides different options for specifying a VI in a LabVIEW library or packed project library, as the following table describes.
 File Type You Select
 BehaviorLabVIEW library (
 .llb
 )
 Browses into the library and launches the
 [Select a VI](select-a-vi-dialog-box.html)
 dialog box, in which you can select a VI the library contains.
 LabVIEW packed project library (
 .lvlibp
 )
 Displays the content of the packed project library file and launches the
 [Select a VI from a LabVIEW Packed Project Library](select-a-vi-from-a-labview-packed-project-lib.html)
 dialog box, in which you can select a VI the packed project library exports to open.
- Browse for VI in LabVIEW Project 
 —Launches the
 Select VI From LabVIEW Project 
 dialog box, in which you can select a VI from the LabVIEW project the step uses. The control returns the URL within the LabVIEW project rather than an absolute or relative pathname for the file. This option is available only when you specify a LabVIEW project file in the Project Path control.
- Add or Remove VIs from LabVIEW Project 
 —Launches the
 Add or Remove Items from LabVIEW Project 
 dialog box, in which you can add, create, or remove VIs from the LabVIEW project the step uses. This option is available only when you specify a LabVIEW project file in the Project Path control.

#### Specifying a Class Member

The LabVIEW Module tab contains the following options when you select
 Class Member Call
 from the Call Type ring control.

- Class Path 
 —The path of the LabVIEW class the step uses. The Class Path control contains a list of the five most recently selected LabVIEW classes.
 Click the
 Browse for LabVIEW Member 
 button, located to the right of the Member Name control, to launch the
 Select a Class Member from LabVIEW Class 
 dialog box, in which you can select a LabVIEW class member VI to call from the specified LabVIEW class.
- Browse for LabVIEW Class 
 —Launches the
 Select the Step's LabVIEW Class File 
 dialog box, in which you browse for a LabVIEW class (
 .lvclass 
 ) file or a LabVIEW library (
 .llb 
 ) or LabVIEW packed project library (
 .lvlibp 
 ) file that contains a LabVIEW class file. The LabVIEW Module tab provides different options for specifying a class in a LabVIEW library or packed project library, as the following table describes.
 File Type You Select
 BehaviorLabVIEW library (
 .llb
 )
 Launches the
 [Select a Class from LabVIEW LLB](select-a-class-from-labview-llb-dialog-box.html)
 dialog box, in which you can review the files the LLB file contains and select a LabVIEW class file to open.
 LabVIEW packed project library (
 .lvlibp
 )
 Launches the
 [Select a Class from LabVIEW Packed Project Library](select-a-class-from-labview-packed-project-li.html)
 dialog box, in which you can review the content of the packed project library file and select a LabVIEW class file from the packed project library to open.
- Browse for LabVIEW Class in LabVIEW Project 
 —Launches the
 Select a Class from LabVIEW Project 
 dialog box, in which you can select a LabVIEW class to call from the LabVIEW project you specify. This option is available only when you specify a LabVIEW project file in the Project Path control.
- Member Name 
 —The name of the public member from the LabVIEW class the step uses.
- Browse for LabVIEW Member 
 —Launches the
 Select a Class Member from LabVIEW Class 
 dialog box, in which you can select a LabVIEW class member VI to call from the specified LabVIEW class.
- Browse for LabVIEW Class Member in LabVIEW Project 
 —Launches the
 Select a Class Member from LabVIEW Project 
 dialog box, in which you can select a LabVIEW class member VI to call from the specified LabVIEW project. This option is available only when you specify a LabVIEW project file in the Project Path control.

#### Specifying a Property Node

The LabVIEW Module tab contains the following options when you select
 Property Node Call
 from the Call Type ring control.

- Configure Settings for Property Node 
 —Launches the
 Configure Property Node 
 dialog box, in which you can specify the I/O Reference type or the LabVIEW class and select properties for the Property Node call.
- Regenerate Property Node 
 —Rebuilds the Property Node call using the current step settings.

#### See Also

[Calling LabVIEW Property Nodes from TestStand](/csh?context=ts_tslabview_property_node)

[Configure Property Node dialog box](configure-property-node-dialog-box.html)

[Cross-Bitness Support using the LabVIEW development system](/csh?context=ts_tsfundamentals_64lvcrossbitnesssupport)

[Express VIs and Property Node Calls in 32-bit TestStand and 64-bit TestStand](/csh?context=ts_tsfundamentals_64lvexpvipropnodecalls)

[LabVIEW Code Module Support for 64-bit TestStand](/csh?context=ts_tsfundamentals_64lvcodemodules)

[LabVIEW Data Types in TestStand](/csh?context=ts_tsref_labview_data_types)

[Migrating LabVIEW Code Modules from 32-bit TestStand to 64-bit TestStand](/csh?context=ts_tsfundamentals_64lvcodemodulesmigrate)

[Simultaneously Supporting 32-bit TestStand and 64-bit TestStand](/csh?context=ts_tsfundamentals_64lvcodemodulestsbitness)

[Updating Cluster Element Mapping](/csh?context=ts_tsref_labview_cluster_params_update)

[Using the $(Platform) Path Macro to Locate the Correct Code Module in 32-bit TestStand and 64-bit TestStand](/csh?context=ts_tsfundamentals_64platformmacro)

Parent topic:

Edit LabVIEW VI Call Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/module-tab-edit-labwindows-cvi-module-call-di.html language=enus -->
## TOPIC 03926: Module Tab - Edit LabWindows/CVI Module Call Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/module-tab-edit-labwindows-cvi-module-call-di.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/module-tab-edit-labwindows-cvi-module-call-di.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Module Tab You can use the Module tab to specify the function prototype, which includes the data type of each parameter and the values to pass for each parameter. The Parameters Table control shows all the available parameters for the function call and an entry for the return value. You can insert,

### Module Tab - Edit LabWindows/CVI Module Call Dialog Box

#### Module Tab

You can use the Module tab to specify the function prototype, which includes the data type of each parameter and the values to pass for each parameter. The Parameters Table control shows all the available parameters for the function call and an entry for the return value. You can insert, remove, or rearrange the order of the parameters.

The Module tab contains the following options:

- Module Pathname 
 —The pathname of the code module file that contains the function the step calls. You can specify an absolute or relative pathname for the module file. Relative pathnames are relative to the TestStand search directory paths. Use the
 Edit Search Directories 
 dialog box to
 customize the search directory paths 
 .If you select a debug
 .dll 
 built by LabWindows CVI 2019 or later, then the CVI Project File to Open on the Source Code Tab updates to the LabWindows/CVI .prj file that was used to build the selected
 .dll 
 .
- Function Name 
 —Selects the function in the code module the step calls. The LabWindows/CVI Adapter attempts to read the code module file and find the names of all functions. If the code module type is not a C source file, the LabWindows/CVI Adapter populates the Function Name ring control with the names of all the functions the code module contains.If you select a debug
 .dll 
 built by LabWindows/CVI 2019 or later as the Module, then the Source File that Contains Function on the Source Code Tab updates to the
 .c 
 file path that was used to build the
 .dll 
 .
- Reload Prototype 
 —Requests that the LabWindows/CVI Adapter query the code module for prototype information for the currently selected function. When a DLL contains export information or a type library or there is a type library with the same name as the DLL file and the function is defined in the type library, TestStand uses the prototype.
 Note 
 If you create a DLL using LabWindows/CVI 7.1 or later, TestStand can read the prototype information for the currently selected function without the use of a type library. 
 If the code module is a debug
 .dll 
 built by LabWindows/CVI 2019 or later, then the CVI Project File to Open and the Source File that Contains Function on the Source Code Tab updates to the LabWindows/CVI
 .prj 
 and
 .c 
 that were used to build the
 .dll 
 .
- Edit Prototype 
 —Displays the function prototype for editing. The LabWindows/CVI Adapter disables this control when it reads a function prototype from the code module.
- Always Run In Process 
 —Specifies whether the step always runs in-process even when the LabWindows/CVI Adapter is configured to run out-of-process. Use this option when you do not want the global settings for the adapter to affect the tools and step types you create for use with the LabWindows/CVI Adapter.
- Parameters Table 
 —Shows all of the available parameters for the function call and an entry for the return value. The Parameters Table control contains the following columns:
 
 When you select a parameter in the Parameters Table control, the Parameter Details Table control contains the specific details about the parameter. The data type (Numeric, String, Enumeration, Object, C Struct, or Array) determines the information required for a parameter. As an alternative to specifying the function name and the parameter values, you can use the Function Call control to directly edit the function name and all the function arguments at once. To insert or remove parameters, click
 New 
 or
 Delete 
 . To rearrange the parameter order, select the parameter you want to move and click
 Move Up 
 or
 Move Down 
 .
  - Name 
 —A symbolic name for the parameter.
 Note 
 Parameters with attributes include an
 Edit Attributes
 button in the Name column of the Parameters Table. TestStand associates parameter attributes with the module parameter, which TestStand stores with the step configuration information, not with the parameter value that TestStand passes to the module. Right-click an item in the Parameters Table to access the
 [Parameters Table](for-specify-module-dialog-boxes-parameters-ta.html)
 context menu, from which you can launch the
 [Attributes](attributes-dialog-box.html)
 dialog box.
  - Description 
 —The short description of the parameter type using ANSI C syntax.
  - Log 
 —When you enable this option, the step logs the parameter as an additional result. Enabling this option is equivalent to using the checkbox next to the additional result name in the
 Additional Results 
 dialog box. For in/out parameters, enabling this option enables the [In] parameter and the [Out] parameter in the Additional Results dialog box. This option is indeterminate for in/out parameters if you specify to log only the [In] parameter value or only the [Out] parameter value. If this option is indeterminate, a tooltip specifies whether the Additional Results dialog box specifies to log the [In] parameter value or the [Out] parameter value.
  - Value Expression 
 —The argument expression to pass.
- Parameter Details Table 
 —The data type of each parameter and additional information according to each parameter type. The Category ring control specifies a group of data types to list in the Type ring control. The categories include:
 Numeric 
 ,
 String 
 ,
 Enumeration 
 ,
 Object 
 ,
 C Struct 
 ,
 Arrays 
 ,
 TestData 
 ,
 TestError 
 , and
 Pointer/Handle 
 . The Type control specifies the data type of the function parameter.
 Note 
 The LabWindows/CVI Adapter supports numeric return values, which includes Boolean, void*, and void.
- Prototype 
 —The prototype of the specified function in C syntax.
- Create 2.0 Prototype 
 —Discards the current parameters and values in the Parameters Table control and replaces the prototype with the TestStand 2.0.
 x 
 standard prototype.
- Function Call 
 —Directly edits the function name and all of function arguments at once.

#### Editing the Function Call

You can use various controls in the Module tab to edit the function name and the argument values of the function. Alternatively, you can use the Function Call control to directly edit the function name and all of the function arguments at once. In the Function Call control, edit the call just as you would in a source code editor. If you enter a number of arguments different than the function prototype specifies, TestStand launches the
 [Prototypes Conflict](prototypes-conflict-dialog-box.html)
 dialog box, in which you can alter the prototype to match the number of arguments you specify.

When you edit a call in the Function Call control, the
 Browse
 ,
 Revert
 ,
 Accept
 , or
 Go to Error
 buttons are visible. All other controls are dimmed.

- Browse 
 —Inserts variables, properties, or
 expression operators 
 into the Function Call control.
- Revert 
 —Discards the changes you make in the Function Call control.
- Accept 
 —Applies the changes you made in the Function Call control.
- Go to Error 
 —Shows the highlighted syntax errors in the Function Call control.

#### See Also

[Additional Results dialog box](additional-results-dialog-box.html)

[Attributes dialog box](attributes-dialog-box.html)

[Edit Search Directories dialog box](edit-search-directories-dialog-box.html)

[Expression Operators](/csh?context=ts_tsfundamentals_operators_expression)

[Locating the Correct DLL in 32-bit TestStand and 64-bit TestStand](/csh?context=ts_tsfundamentals_64locatingdlls)

[Parameters Table Context Menu for Specify Module Dialog Boxes](for-specify-module-dialog-boxes-parameters-ta.html)

[Prototypes Conflict dialog box](prototypes-conflict-dialog-box.html)

[Using Side-by-Side Versions of the LabWindows/CVI Run-Time Engine with TestStand](/csh?context=ts_tsfundamentals_sxscvirte)

[Using the $(Platform) Path Macro to Locate the Correct Code Module in 32-bit TestStand and 64-bit TestStand](/csh?context=ts_tsfundamentals_64platformmacro)

Parent topic:

Edit LabWindows/CVI Module Call Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/module-tab-edit-net-call-dialog-box.html language=enus -->
## TOPIC 03927: Module Tab - Edit .NET Call Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/module-tab-edit-net-call-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/module-tab-edit-net-call-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Module Tab The Module tab contains the following options: Assembly —The absolute or relative file path of the assembly the step calls. Relative pathnames are relative to the TestStand search directory paths. Use the Edit Search Directories dialog box to customize the search directory paths . Browse

### Module Tab - Edit .NET Call Dialog Box

#### Module Tab

The Module tab contains the following options:

- Assembly 
 —The absolute or relative file path of the assembly the step calls. Relative pathnames are relative to the TestStand search directory paths. Use the
 Edit Search Directories 
 dialog box to
 customize the search directory paths 
 .
  - Browse for Assembly 
 —Launches a Browse dialog box in which you can specify a pathname for the assembly.
 Note 
 Starting with TestStand 2024 Q4, browsing the Global Assembly Cache (GAC) is no longer supported.
 Calling C++/CLI assemblies from a .NET step is no longer supported.
- Advanced Settings 
 —Launches the
 Advanced Settings 
 window, in you can control the lifetime of an object the .NET step creates.
- Reload Assemblies and Prototypes 
 —The .NET Adapter reloads the information about classes, methods, and properties in the assembly for each specified call and updates the prototype specified for the calls, if needed.
- Root Class 
 —The name of the class on which the first call in a chain of calls for the step operates. When you select an assembly, the .NET Adapter populates this control with a list of classes defined for the assembly.
- Edit Code 
 —Launches Microsoft Visual Studio to edit the code associated with the call currently selected in the .NET Invocation control. If you have not specified a project or source file on the
 Source Code 
 tab, TestStand launches an Open File dialog box and prompts you to browse for the files. Because you can specify Edit Code operations for multiple calls in a single step, the project file you select applies to any other calls you make in the same step, but you must specify a new source file for each individual call.
 Note 
 You must have a supported version of Visual Studio installed and a valid call currently selected in the .NET Invocation control to use the
 Edit Code
 button.
- Create Code 
 —Launches Visual Studio to create a shell function by using the member name of the call currently selected in the .NET Invocation control as the name of the method to create and the class name of the call as the class in which to create the function. If you have not specified a project or source file on the Source Code tab, TestStand launches an Open File dialog box and prompts you to browse for the files. Because you can specify Create Code operations for multiple calls in a single step, the project file you select applies to any other calls you make in the same step, but you must specify a new source file for each individual call.
 Note 
 You must have a supported version of Visual Studio installed and a call with a valid class name currently selected in the .NET Invocation control to use the
 Create Code
 button. 
 The .NET Adapter appends the newly created function to the end of the source file you select on the Source Code tab. If a code template file exists for the step type you use for the step, the adapter uses the template to create the shell for the new function. If the project file you specify on the Source Code tab is not in the Visual Studio solution, the adapter prompts you to add it. If the source file you specify on the Source Code tab is not in the project, the adapter prompts you to add it. If you already have the source code for the function, click the
 Edit Code 
 button instead to edit the code associated with the call currently selected in the .NET Invocation control.
 If template source code exists for the step type you use for the step, the .NET Adapter inserts the parameter information from the template source code into the new function shell. If the step type does not have a code template, TestStand uses the default template for the adapter.
 When the .NET Adapter creates the code, the adapter launches a copy of Visual Studio and displays the file in Visual Studio.
- .NET Invocation 
 —The chain of calls the step completes at run time. Right-click, double-click, or press <Ctrl-Space> to show the list of members available to call. Select a member name in the list of members or type the member name to specify it. Press <Enter> or <Tab> to insert the call currently selected in the member list into the .NET Invocation control. Enter a period (
 . 
 ) character or click the <Click here to add a call> text to show a list of members available for the next call.
 After you specify the calls, the .NET Invocation control shows the signature of the call. TestStand shows calls you incorrectly or partially specify in red. Parameters that contain invalid values or required parameters that you have not yet specified display in red even if the call is valid.
 Click anywhere on the call signature to select the call and view or edit its parameters in the Parameters Table. TestStand shows the currently selected call in bold in the .NET Invocation control. Click anywhere on a particular parameter in the signature to highlight the parameter in the Parameters Table. TestStand shows the selected parameter in bold in the .NET Invocation control.
 For the first call in the chain you specify in the .NET Invocation control, the member shows only constructors, static members, and the following special case types:
 
 For subsequent calls in the chain, the member list shows the instance members of the class that is the return value type of the previous call.
  - Use Existing Object 
 —Use this call type to specify an existing object to use instead of calling a constructor. The Parameters Table for this call contains an
 Existing Object 
 parameter for you to specify, and this parameter must contain the value of a valid object reference—or basic type in the case of the
 System.String 
 class or other similar basic classes—that refers to the object on which to perform the next call. If you specify a struct—which is a value type—and not a class—which is a reference type—for the root class of the step, you can also specify a variable or property of a named data type that corresponds to the struct. Click the
 Create Type from Struct 
 button to launch the
 Create Custom Data Type from Struct 
 dialog box and create a named data type. If you specify an instance of a named data type, the .NET Adapter creates a temporary .NET struct and copies the corresponding fields between the struct and the TestStand variable.
 Note 
 Starting with TestStand 2024 Q4, 'Create Remote Object' is no longer supported.
- Parameters Table 
 —Contains the parameters and return values for all calls in the step. The Parameters Table lists parameters for each call under a row that displays the member name for the call. The Parameters Table contains the following columns:
  - Parameter Name 
 —The name of the parameter. For properties and fields, the first call the Parameter Name column contains a combo box you can use to switch between Get Property and Set Property. If a public version of a Get or Set does not exist for the property or field, the combo box does not include the option.
 Note 
 Parameters with attributes include an
 Edit Attributes
 button in the Name column of the Parameters Table. You can edit attributes for fields of structs and elements of arrays. TestStand associates parameter attributes with the module parameter, which TestStand stores with the step configuration information and not with the parameter value that TestStand passes to the module. Right-click an item in the Parameters Table to and select
 Edit Attributes
 from the
 [Parameters Table](for-module-tabs-parameters-table-context-menu.html)
 context menu to launch the
 [Attributes](attributes-dialog-box.html)
 dialog box.
  - Type 
 —.NET data type for the parameter.
 For one-dimensional arrays, you can specify an expression value for the entire array, or you can specify values for each element of the array. Use the plus (
 + 
 ) buttons to insert a new element in the array, and the minus (
 - 
 ) buttons to remove specific elements from the array.
    - Create Type from Struct 
 —If the data type is a struct, such as a .NET value type, this button appears in the cell and launches the
 Create Custom Data Type from Struct 
 dialog box, in which you can configure a new custom data type to use as the variable type for passing the struct parameter.
  - In/Out 
 —Indicates whether the parameter is an input, output, or both.
  - Log 
 —When you enable this option, the step logs the parameter as an additional result. Enabling this option is equivalent to using the checkbox next to the additional result name in the
 Additional Results 
 dialog box. For in/out parameters, enabling this option enables the [In] parameter and the [Out] parameter in the Additional Results dialog box. This option is indeterminate for in/out parameters if you specify to log only the [In] parameter value or only the [Out] parameter value. If this option is indeterminate, a tooltip specifies whether the Additional Results dialog box specifies to log the [In] parameter value or the [Out] parameter value.
  - Dispose 
 —When you enable this option, TestStand calls the
 Dispose 
 method on the .NET object when the output parameter references are released. If the object does not implement the IDisposable interface, this option is ignored.
  - Use Default Value 
 —When you enable this option, TestStand uses the default value of the parameter. An option appears in this column only for parameters that have default values.
  - Value 
 —A TestStand expression. For input parameters, TestStand passes the value of this expression. For output parameters, TestStand stores the data the method returns in the location this expression specifies. To help you enter an expression in the Value column, click the
 Expression Browse 
 button to launch the
 Expression Browser 
 dialog box. For enumerated types, a combo box displays all valid values for the type. You can also use an expression for an enumerated type. Refer to the
 .NET Call Parameters 
 topic for more information about using enumeration parameters.In addition, you can store all .NET types directly in a TestStand object reference variable, which is useful when you want to store a .NET array without making a copy and do not need to access the array directly from TestStand.

#### See Also

[.NET Code Module Support for 64-bit TestStand](/csh?context=ts_tsfundamentals_64netcodemodules)

[Additional Results dialog box](additional-results-dialog-box.html)

[Advanced Settings Window](advanced-settings-window.html)

[AnyCPU Assemblies in 32-bit TestStand and 64-bit TestStand](/csh?context=ts_tsfundamentals_64anycpuassemblies)

[Attributes dialog box](attributes-dialog-box.html)

[Create Custom Data Type from Struct Dialog box](create-custom-data-type-from-struct-dialog-bo.html)

[DotNetCall.LoadPrototypeFromSignature](../tsapiref/dotnetcall-loadprototypefromsignature.html)

[Edit Search Directories dialog box](edit-search-directories-dialog-box.html)

[Expression Browser dialog box](expression-browser-dialog-box.html)

[Parameters Table Context Menu for Module Tabs](for-module-tabs-parameters-table-context-menu.html)

[Platform-Specific Assemblies in 32-bit TestStand and 64-bit TestStand](/csh?context=ts_tsfundamentals_64platformspecificassemblies)

[Using the $(Platform) Path Macro to Locate the Correct Code Module in 32-bit TestStand and 64-bit TestStand](/csh?context=ts_tsfundamentals_64platformmacro)

Parent topic:

Edit .NET Call Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/module-tab-edit-python-call-dialog-box.html language=enus -->
## TOPIC 03928: Module Tab - Edit Python Call Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/module-tab-edit-python-call-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/module-tab-edit-python-call-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Python Module Tab To display the Python Module tab in the TestStand Sequence Editor, insert a step configured to use the Python Adapter and select Specify Module or Step Settings from the context menu. To display the Python Module tab in the TestStand User Interfaces, insert a step configured to use

### Module Tab - Edit Python Call Dialog Box

#### Python Module Tab

To display the Python Module tab in the TestStand Sequence Editor, insert a step configured to use the Python Adapter and select
 Specify Module
 or
 Step Settings
 from the context menu. To display the Python Module tab in the TestStand User Interfaces, insert a step configured to use the Python Adapter and select
 Specify Module
 from the context menu.

Note

The Python Module tab contains the following options:

- Module 
 —Relative or absolute path of the Python module to execute. The Python module can be a
 .py 
 file or a directory which contains a
 __init__.py 
 file.
 Note 
 When you specify a relative path, the Python Adapter will determine the absolute path using the following search directories in order:
 TestStand search directories.
 If a virtual environment is specified, Python search directories specific to the virtual environment.
 Python search directories specific to the main installation of the configured Python version.
  - Browse for Module 
 —Launches a Browse dialog box in which you can specify a path for the Python code module.
  - View 
 —Opens the configured Python module in application configured in Python Adapter configuration dialog box.
- Advanced Settings 
 —Launches the advanced settings dialog to specify the Python interpreter session to use for executing specified code module.
- Reload Python Module 
 —Performs reload of the configured Python module and updates the parameter list for the specified Python function.
- Namespace 
 —Displays the namespace of the selected module. To learn how TestStand determines the namespace, refer to
 Python Namespaces 
 .
- Operation Scope 
 —Specifies scope of the operation to be performed. It contains the following values:
  - Module
  - Class
  - Class Instance
- Operation Type 
 —Specifies operation to perform. It contains the following values:
  - Create Class Instance
  - Call Method
  - Get Attribute
  - Set Attribute
- Class Name 
 —Name of the Python class existing in the specified module to be used during execution.
- Class Instance 
 —Location of object reference variable holding an instance of the Python class.
- Function or Attribute Name 
 —Name of the Python attribute or function existing in the specified module to be used during execution.
- Parameters Table 
 —Contains the parameters and return values for the configured operation in the step. The Parameters Table contains the following columns:
  - Parameter Name
  - Parameter Type 
 —Python type of the parameter.
  - Log 
 —Option that enables step to log the parameter as an additional result.
 Note 
 Enabling this option is equivalent to using the checkbox next to the additional result name on the Additional Results panel of the Properties tab of the Step Settings pane.
  - Value 
 —TestStand expression.
 Note 
 For input parameters, TestStand passes the value of this expression. For output parameters, TestStand stores the data the method returns in the location this expression specifies.
  - Parameter Add Button 
 —Adds a new parameter to the end of the parameter list.
  - Parameter Remove Button 
 —Removes the selected parameter.
  - Parameter Move Up Button 
 —Swap the position of current selected parameter and parameter above it.
  - Parameter Move Down Button 
 —Swap the position of current selected parameter and parameter below it.

Parent topic:

Edit Python Call Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/module-tab-step-settings-pane.html language=enus -->
## TOPIC 03929: Module Tab - Step Settings Pane

- bundle_id: `teststand-api-reference`
- source_path: `tsref/module-tab-step-settings-pane.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/module-tab-step-settings-pane.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Module Tab Use the Module tab of the Step Settings pane to specify which code module a step calls. The Module tab displays one of the adapter-specific module tabs for a step, which you can use to specify which function, VI, or sequence call the step calls and the parameters of the invocation. For a

### Module Tab - Step Settings Pane

#### Module Tab

Use the Module tab of the Step Settings pane to specify which
 [code module](/csh?context=ts_tsfundamentals_bldgblocks_codemodules)
 a step calls. The Module tab displays one of the
 [adapter-specific module tabs](specify-module-tabs-and-dialog-boxes.html)
 for a step, which you can use to specify which function, VI, or sequence call the step calls and the parameters of the invocation.

For a step that does not call a code module, the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 hides the Module tab.

#### See Also

[Module Adapters](/csh?context=ts_tsfundamentals_module_adapters)

Parent topic:

Step Settings Pane

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/move-selected-operations-dialog-box.html language=enus -->
## TOPIC 03930: Move Selected Operations Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/move-selected-operations-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/move-selected-operations-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Move Selected Operations Dialog Box Use the Move Selected Operations Dialog Box to change the position of a group of operations on the time axis. You can align a group of operations with another group to make it easier to visually compare the groups. The dialog contains the following controls: Mark

### Move Selected Operations Dialog Box

#### Move Selected Operations Dialog Box

Use the Move Selected Operations Dialog Box to change the position of a group of operations on the time axis. You can align a group of operations with another group to make it easier to visually compare the groups. The dialog contains the following controls:

- Mark with color/Do not mark 
 —Specify whether to mark the selected operations with a selected color so that they are visually distinguished as a group.
- Current Initial Time 
 —Indicates the initial time of the first operation in the group.
- New Initial Time 
 —Specifies the new initial time of the first operation in the group. All other operations in the group move by the same offset.
- Move to Unique Threads 
 —Specifies whether to move the selected operations to new pretend threads with unique ids such that the selected operations are more easily distinguished from other operations in the original threads that also reside in the destination location on the time axis.

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/multiple-numeric-limit-test-edit-tabs.html language=enus -->
## TOPIC 03931: Multiple Numeric Limit Test Edit Tabs

- bundle_id: `teststand-api-reference`
- source_path: `tsref/multiple-numeric-limit-test-edit-tabs.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/multiple-numeric-limit-test-edit-tabs.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Multiple Numeric Limit Test edit tabs in the TestStand Sequence Editor to customize the type of comparison and limits TestStand uses to set the step status . The Step Settings pane for the Multiple Numeric Limit Test step contains the following tabs: Limits —Specifies for each measurement th

### Multiple Numeric Limit Test Edit Tabs

Use the Multiple Numeric Limit Test edit tabs in the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 to customize the type of comparison and limits TestStand uses to set the
 [step status](/csh?context=ts_tsfundamentals_step_status_values_table)
 .

The Step Settings pane for the Multiple Numeric Limit Test step contains the following tabs:

- Limits 
 —Specifies for each measurement the type of limit comparison the step performs, the limit values the step uses, as well as the format and units of the value and limits.
- Data Source 
 —The data source for the measurement value the step compares to limit values.

#### See Also

[Test Step Types](test-step-types.html)

Parent topic:

Multiple Numeric Limit Test Step

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/multiple-numeric-limit-test-step.html language=enus -->
## TOPIC 03932: Multiple Numeric Limit Test Step

- bundle_id: `teststand-api-reference`
- source_path: `tsref/multiple-numeric-limit-test-step.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/multiple-numeric-limit-test-step.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: The Multiple Numeric Limit Test step limit checks a set of related measurements. Use the Multiple Numeric Limit Test step to check limits for multiple measurements in a single step instead of using several Numeric Limit Test steps to limit test a set of related measurements. Use the Multiple Numeric

### Multiple Numeric Limit Test Step

The Multiple Numeric Limit Test step limit checks a set of related measurements. Use the Multiple Numeric Limit Test step to check limits for multiple measurements in a single step instead of using several Numeric Limit Test steps to limit test a set of related measurements.

Use the Multiple Numeric Limit Test step to test limits for any number of measurements. Each measurement can have independent limits, units, display format, data source, and comparison type. Configure each measurement the same way you configure an individual Numeric Limit Test step. A Multiple Numeric Limit test step passes when all of measurements pass.

#### Configuring the Step

Use the
 [Multiple Numeric Limit Test edit tabs](multiple-numeric-limit-test-edit-tabs.html)
 in the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 and the
 [Edit Multiple Numeric Limit Test](edit-multiple-numeric-limit-test-dialog-box.html)
 dialog box in a
 [TestStand User Interface](teststand-user-interfaces.html)
 to customize the type of comparison and limits TestStand uses to set the
 [step status](/csh?context=ts_tsfundamentals_step_status_values_table)
 .

#### Step Properties

In addition to the
 [common custom properties](/csh?context=ts_tsfundamentals_custom_result_props)
 , the Multiple Numeric Limit Test step type defines the following step properties:

- Step.Result.Measurement 
 —An array that stores the measurements you configure for the step. Each element of the measurement array
is an instance of the NI_LimitMeasurement data type. The NI_LimitMeasurement type defines the following fields:
  - Limits.Low 
 ,
 High 
 ,
 LowExpr 
 ,
 HighExpr 
 ,
 UseLowExpr 
 , and
 UseHighExpr 
 —The limits for the comparison.
  - Units 
 —A label that describes the measurement units for the limits and the measurement value.
  - Comp 
 —The
 type of comparison 
 , such as EQ.
  - CompExpr 
 —The comparison operation using an expression.
  - UseCompExpr 
 —The step uses the expression to compare the measurement values.
  - Data 
 —Stores the numeric measurement value. The step 
obtains this value from the corresponding element in
 Step.NumericArray 
 or from the data source you specify.
  - Status 
 —Stores the result of the comparison of the measurement value with the limits. The result is
 Passed 
 or
 Failed 
 .
- Step.DataSource 
 —An expression that identifies the numeric array that provides the data values for all measurements when you do not use a separate data source for each measurement.
- Step.NumericArray 
 —A numeric array that is the default data source
 Step.DataSource 
 specifies.
- Step.UseIndividualDataSources 
 —When this property is
 True 
 , the step stores separate data source
 expressions 
 for each measurement in the
 Step.DataSourceArray 
 . When this property is
 False 
 , the step obtains the data values for each measurement from the numeric array the
 Step.DataSource 
 property specifies.
- Step.DataSourceArray 
 —A data source for each measurement element in the measurement array.
- Step.ExpectedNumMeasure 
 —The number of measurements for 
the step.
- Step.ExtraDataAction 
 —Specifies how the step processes data 
when the numeric array contains more elements than the number of measurements. The step can apply a specific measurement to extra data, repeat the measurement set again, generate a run-time error, or ignore the extra data.
- Step.MeasToRepeat 
 —A measurement to repeat when the
 Step.ExtraDataAction 
 is set to
 RepeatOne 
 .
- Step.ExtraMeasAction 
 —Specifies how the step responds when the numeric array contains fewer elements than the expected number of measurements. Options include ignoring the extra measurements or generating a run-time error.

Note

#### See Also

[Multiple Numeric Limit Test Step Type (Example)](/csh?context=ts_8125)

[Step Types You Can Use with Any Module Adapter](/csh?context=ts_tsfundamentals_universal_step_types)

Parent topic:

Test Step Types

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/net-adapter-configuration-dialog-box.html language=enus -->
## TOPIC 03933: .NET Adapter Configuration Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/net-adapter-configuration-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/net-adapter-configuration-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Select Configure»Adapters to launch the .NET Adapter Configuration dialog box. Select the .NET Adapter in the list control and click Configure . The .NET Adapter Configuration dialog box contains the following option: Show Arguments in Step Description —Specifies whether the description for steps th

### .NET Adapter Configuration Dialog Box

Select
 Configure»Adapters
 to launch the .NET Adapter Configuration dialog box. Select the .NET Adapter in the list control and click
 Configure
 .

The .NET Adapter Configuration dialog box contains the following option:

- Show Arguments in Step Description 
 —Specifies whether the description for steps that use the .NET Adapter includes the arguments steps pass to the methods they call.
- Version of Visual Studio to Use for Create and Edit Code 
 —The version of Microsoft Visual Studio that the .NET Adapter uses to perform Create Code and Edit Code operations.
- Version of Visual Studio to Use for Debugging 
 —The version of Visual Studio that the .NET Adapter uses to
 debug code modules 
 .

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/net-module-tab.html language=enus -->
## TOPIC 03934: .NET Module Tab

- bundle_id: `teststand-api-reference`
- source_path: `tsref/net-module-tab.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/net-module-tab.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: To display the .NET Module tab in the TestStand Sequence Editor , insert a step configured to use the .NET Adapter and select Specify Module or Step Settings from the context menu. The .NET Module tab contains the following options: Assembly —The absolute or relative file path of the assembly the st

### .NET Module Tab

To display the .NET Module tab in the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 , insert a step configured to use the .NET Adapter and select
 Specify Module
 or
 Step Settings
 from the context menu. The .NET Module tab contains the following options:

- Assembly 
 —The absolute or relative file path of the assembly the step calls. Relative pathnames are relative to the TestStand
 search directory paths 
 . Use the 
 Edit Search Directories 
 dialog box to customize the search directory paths. For assembly files, the Assembly ring control contains a most recently used list of the last five assemblies selected.
  - Browse for Assembly 
 —Launches a Browse dialog box in which you can specify a pathname for the assembly.
 Note 
 Starting with TestStand 2024 Q4, browsing the Global Assembly Cache (GAC) is no longer supported.
- Advanced Settings 
 —Launches the
 Advanced Settings 
 window, in you can control the lifetime of an object the .NET step creates.
- Reload Assemblies and Prototypes 
 —The .NET Adapter reloads the information about classes, methods, and properties in the assembly for each specified call and updates the prototype specified for the calls, if needed.
- Root Class 
 —The name of the class on which the first call in a chain of calls for the step operates. When you select an assembly, the .NET Adapter populates this control with a list of classes defined for the assembly. Any fully-specified generic types referenced in the assembly will also appear at the bottom of this list.
- Edit Code 
 —Launches Microsoft Visual Studio to edit the code for a call currently selected in the .NET Invocation control. If you have not specified a project or source file in the
 .NET Source Code Files 
 window, TestStand launches an Open File dialog box and prompts you to browse for the files. Because you can specify Edit Code operations for multiple calls in a single step, the project file you select applies to any other calls you make in the same step, but you must specify a new source file for each individual call.
 Note 
 You must have a supported version of Visual Studio installed and the currently selected call in the .NET Invocation control must be fully specified and valid for you to use the
 Edit Code
 button.
- Create Code 
 —Launches Visual Studio to create a shell function by using the member name of the call currently selected in the .NET Invocation control as the name of the method to create and the class name of the call as the class in which to create the function. If you have not specified a project or source file in the .NET Source Code Files window, TestStand launches an Open File dialog box and prompts you to browse for the files. Because you can specify Create Code operations for multiple calls in a single step, the project file you select applies to any other calls you make in the same step, but you must specify a new source file for each individual call.
 Note 
 You must have a supported version of Visual Studio installed and a call with a valid class name currently selected in the .NET Invocation control to use the
 Create Code
 button. 
 The .NET Adapter appends the newly created function to the end of the source file you select in the .NET Source Code Files window. If a code template file exists for the step type you use for the step, the adapter uses the template to create the shell for the new function. If the project file you specify in the .NET Source Code Files window is not in the Visual Studio solution, the adapter prompts you to add it. If the source file you specify in the .NET Source Code Files window is not in the project, the adapter prompts you to add it. If you already have the source code for the function, click the
 Edit Code 
 button instead to edit the code associated with the call currently selected in the .NET Invocation control.
 If template source code exists for the step type you use for the step, the .NET Adapter inserts the parameter information from the template source code into the new function shell. If the step type does not have a code template, TestStand uses the default template for the adapter.
 When the .NET Adapter creates the code, the adapter launches a copy of Visual Studio and displays the file in Visual Studio.
- .NET Source Code Files 
 —Launches the
 .NET Source Code Files 
 window, in which you can specify the pathname for the source file, project file, and solution file for Visual Studio that implement the functions the
 code module 
 calls. You must have a supported version of Visual Studio installed to launch the .NET Source Code Files window.
- .NET Invocation 
 —The chain of calls the step completes at run time. Right-click, double-click, or press <Ctrl-Space> to show the list of members available to call. Select a member name in the list of members or type the member name to specify it. Press <Enter> or <Tab> to insert the call currently selected in the member list into the .NET Invocation control. Enter a period (
 . 
 ) character or click the <Click here to add a call> text to show a list of members available for the next call.
 
 After you specify the calls, the .NET Invocation control shows the signatures of each call in the chain of calls. TestStand shows in red calls you incorrectly or partially specify. Parameters that contain invalid values or required parameters that you have not yet specified display in red even if the call is valid.
 Click anywhere on a call signature to select the call and view or edit its parameters in the Parameters Table. TestStand shows the currently selected call in bold in the .NET Invocation control. Click a particular parameter in the signature to highlight the parameter in the Parameters Table. TestStand shows the selected parameter in bold in the .NET Invocation control.
 For the first call in the chain you specify in the .NET Invocation control, the member list shows only constructors, static members, and the following special case call types:
 
 For subsequent calls in the chain you specify in the .NET Invocation control, the member list shows the instance members of the class that corresponds to the return value of the previous call.
 Note 
 Hover your cursor over a member name in the .NET Invocation control to view any XML help that has been defined for that member.
  - Use Existing Object 
 —Use this call type to specify an existing object to use instead of calling a constructor. The Parameters Table for this call contains an
 Existing Object 
 parameter for you to specify. You must specify a valid TestStand object reference variable or basic type variable (in the case of the
 System.String 
 type,
 System.Int32 
 type, or other basic types) that refers to the object on which to perform the next call. If you specify a struct instead of a class for the root class of the step, you can also specify an instance of a TestStand custom data type that corresponds to the struct instead of a TestStand object reference variable because a struct is a .NET value type, and a class is a .NET reference type.
 Click the
 Create Type from Struct 
 button in the Parameters Table to launch the
 Create Custom Data Type from Struct 
 dialog box and create a named data type. If you specify an instance of a named data type, the .NET Adapter creates a temporary .NET struct and copies the corresponding fields between the struct and the TestStand variable.
 Note 
 Starting with TestStand 2024 Q4, 'Create Remote Object' is no longer supported.
- Parameters Table 
 —Contains the parameters and return values for all calls in the step. The Parameters Table lists parameters for each call under a row that displays the member name for the call. The Parameters Table contains the following columns:
  - Parameter Name 
 —The name of the parameter. For properties and fields, the Parameter Name column contains a combo box you can use to switch between GetProperty and SetProperty. If a public version of a Get or Set does not exist for the property or field, the combo box does not include the option.
 Note 
 Parameters with attributes include an
 Edit Attributes
 button in the Name column of the Parameters Table. You can edit attributes for fields of structs and elements of arrays. TestStand associates parameter attributes with the module parameter, which TestStand stores with the step configuration information and not with the parameter value that TestStand passes to the module. Right-click an item in the Parameters Table to and select
 Edit Attributes
 from the
 [Parameters Table](for-module-tabs-parameters-table-context-menu.html)
 context menu to launch the
 [Attributes](attributes-dialog-box.html)
 dialog box.
  - Type 
 —.NET data type for the parameter.
 For one-dimensional arrays, you can specify an expression value for the entire array, or you can specify values for each element of the array. Use the plus (
 + 
 ) buttons to insert a new element in the array, and the minus (
 - 
 ) buttons to remove specific elements from the array.
    - Create Type from Struct 
 —If the data type is a struct, such as a .NET value type, this button appears in the cell and launches the
 Create Custom Data Type from Struct 
 dialog box, in which you can configure a new custom data type to use as the variable type for passing the struct parameter.
  - In/Out 
 —Indicates whether the parameter is an input, output, or both.
  - Log 
 —When you enable this option, the step logs the parameter as an additional result. Enabling this option is equivalent to using the checkbox next to the additional result name on the
 Additional Results panel 
 of the
 Properties 
 tab of the
 Step Settings 
 pane. For in/out parameters, enabling this option enables the [In] parameter and the [Out] parameter on the Additional Results panel. This option is indeterminate for in/out parameters if you specify to log only the [In] parameter value or only the [Out] parameter value. If this option is indeterminate, a tooltip specifies whether the Additional Results panel specifies to log the [In] parameter value or the [Out] parameter value.
  - Dispose 
 —When you enable this option, TestStand calls the
 Dispose 
 method on the .NET object when the output parameter references are released. If the object does not implement the IDisposable interface, this option is ignored.
  - Use Default Value 
 —When you enable this option, TestStand uses the default value of the parameter. An option appears in this column only for parameters that have default values.
  - Value 
 —A TestStand expression. For input parameters, TestStand passes the value of this expression. For output parameters, TestStand stores the data the method returns in the location this expression specifies. To help you enter an expression in the Value column, click the
 Expression Browse 
 button to launch the
 Expression Browser 
 dialog box. For enumerated types, a combo box displays all valid values for the type. You can also use an expression for an enumerated type. Refer to the
 .NET Call Parameters 
 topic for more information about using enumeration parameters.In addition, you can store all .NET types directly in a TestStand object reference variable, which is useful when you want to store a .NET array without making a copy and do not need to access the array directly from TestStand.

#### See Also

[.NET Code Module Support for 64-bit TestStand](/csh?context=ts_tsfundamentals_64netcodemodules)

[Advanced Settings Window](advanced-settings-window.html)

[AnyCPU Assemblies in 32-bit TestStand and 64-bit TestStand](/csh?context=ts_tsfundamentals_64anycpuassemblies)

[Attributes dialog box](attributes-dialog-box.html)

[Create Custom Data Type from Struct Dialog box](create-custom-data-type-from-struct-dialog-bo.html)

[DotNetCall.LoadPrototypeFromSignature](../tsapiref/dotnetcall-loadprototypefromsignature.html)

[Edit Search Directories dialog box](edit-search-directories-dialog-box.html)

[Expression Browser dialog box](expression-browser-dialog-box.html)

[.NET Source Code Files Window](net-source-code-files-window.html)

[Parameters Table Context Menu for Module Tabs](for-module-tabs-parameters-table-context-menu.html)

[Platform-Specific Assemblies in 32-bit TestStand and 64-bit TestStand](/csh?context=ts_tsfundamentals_64platformspecificassemblies)

[Step Settings Pane](step-settings-pane.html)

[Using the $(Platform) Path Macro to Locate the Correct Code Module in 32-bit TestStand and 64-bit TestStand](/csh?context=ts_tsfundamentals_64platformmacro)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/net-source-code-files-window.html language=enus -->
## TOPIC 03935: .NET Source Code Files Window

- bundle_id: `teststand-api-reference`
- source_path: `tsref/net-source-code-files-window.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/net-source-code-files-window.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Click the Source Code Files button on the .NET Module tab to launch the .NET Source Code Files window, in which you can specify the source file, project file, and solution file that contains the source code for the class members the .NET step calls. You must have a supported version of Microsoft Vis

### .NET Source Code Files Window

Source Code Files

.NET Module

Note

The .NET Source Code Files window contains the following options:

- Source File 
 —The pathname of the source file. If you have multiple calls on the .NET step and the calls reside in various source files, you can leave this control empty and TestStand prompts you to specify a source file when you click the
 Edit Code 
 or
 Create Code 
 button on the .NET Module tab. Because you can perform Edit Code or Create Code operations for multiple calls in a single step, the source file you select applies to any other calls you make in the same step. You can enter an absolute or relative pathname. Relative pathnames are relative to the TestStand
 search directory paths 
 .
- Visual Studio Project File 
 —The pathname of the project file. You must specify an existing project file. If you do not specify a project file, TestStand launches an Open File dialog box and prompts you to specify a project file when you click the
 Edit Code 
 or
 Create Code 
 button on the .NET Module tab. Because you can perform Edit Code or Create Code operations for multiple calls in a single step, the project file you select applies to any other calls you make in the same step. You can enter an absolute or relative pathname. Relative pathnames are relative to the TestStand search directory paths.
- Visual Studio Solution File (optional) 
 —The pathname of the solution file. You must specify an existing solution file. You can enter an absolute or relative pathname. Relative pathnames are relative to the TestStand search directory paths.

#### See Also

[.NET Module Tab](net-module-tab.html)

Parent topic:

.NET Module Tab

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/net-struct-passing-tab-type-properties-dialog.html language=enus -->
## TOPIC 03936: .NET Struct Passing Tab - Type Properties Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/net-struct-passing-tab-type-properties-dialog.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/net-struct-passing-tab-type-properties-dialog.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: .NET Struct Passing Tab You can use the .NET Adapter to pass a TestStand variable or property to a structure parameter for a method or a property in an assembly. The data type of the variable or property you pass must contain all of the fields the structure parameter expects. If a data type contains

### .NET Struct Passing Tab - Type Properties Dialog Box

#### .NET Struct Passing Tab

You can use the .NET Adapter to pass a TestStand variable or property to a structure parameter for a method or a property in an assembly. The data type of the variable or property you pass must contain all of the fields the structure parameter expects. If a data type contains a subproperty that is a named data type, you must separately configure the named data type to allow the .NET Adapter to pass objects of the data type as a structure.

Use the .NET Struct Passing tab to specify how TestStand maps the subproperties of a data type to the elements of a structure parameter.

The .NET Struct Passing tab contains the following options:

- Allow Objects of this Type to be Passed as .NET Structs 
 —Maps this data type to a .NET structure.
- Property 
 —Use this ring control to select a subproperty of the data type in order to display the type and specify the name of the structure element TestStand maps to the property.
 If a subproperty of the data type is a named type, the control does not include the subproperties of the type in the ring control. You must separately configure the named data type to allow the .NET Adapter to pass objects of the named type as a structure, and specify the structure elements to map.
- Exclude When Passing Struct 
 —When you enable this option, TestStand does not include the selected subproperty in the mapping between the data type and the structure.
- Type 
 —The data type of the selected subproperty. This is a read-only field.
- Struct Element Name 
 —The name of the structure element to which TestStand maps the property.

Parent topic:

Type Properties Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/new-csv-input-record-stream-dialog-box.html language=enus -->
## TOPIC 03937: New CSV Input Record Stream Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/new-csv-input-record-stream-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/new-csv-input-record-stream-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the New CSV Input Record Stream dialog box in a TestStand User Interface to configure the New CSV Input Record Stream step. The New CSV Input Record Stream dialog box contains the following options: CSV File Path —Specify the path to the CSV file to read, either by browsing to the file or using

### New CSV Input Record Stream Dialog Box

Use the New CSV Input Record Stream dialog box in a
 [TestStand User Interface](teststand-user-interfaces.html)
 to configure the New CSV Input Record Stream step.

The New CSV Input Record Stream dialog box contains the following options:

- CSV File Path 
 —Specify the path to the CSV file to read, either by browsing to the file or using an expression. To specify by expression, check the
 Specify by Expression 
 check box.
- Input Record Stream Reference 
 —Expression that specifies where to store the reference to the CsvFileInputRecordStream the step creates.
- Field Mapping (Optional) 
 —Sets the CsvFileInputRecordStream.FieldMapping property of the newly created stream.
- Simple Formatting Settings 
 —These settings allow you navigate simple formatting common in many CSV files.
  - Scan for Tag 
 —Check the Scan for Tag checkbox to enable the associated expression control and specify a string to search the file for. Reading continues from the line immediately following the tag. Check the
 Ignore Case 
 check box to make comparisons case-insensitive.
  - Skip Lines 
 —Check the
 Skip Lines 
 checkbox to enable the associated expression control and specify the number of lines to skip before reading. If both
 Scan for Tag 
 and
 Skip Lines 
 are enabled, the tag is searched for first. Once the tag is found, the specified number of lines are skipped. Reading continues from the next line in the CSV file.
- Parse Record Prototype Group Box 
 —Check the Parse Record Prototype checkbox to enable the controls in the corresponding group box.
  - Prototype 
 —Specifies a container that defines the prototype for this stream. At run time, TestStand verifies that the prototype in the file matches the specified container.
  - Allow Extra Fields in Record 
 —Allows subproperties of the specified container to be a superset of the fields specified by the prototype in the file. If this box is unchecked, extra fields in the container result in a run-time error.
  - Import Prototype Button 
 —Launches the Import Prototype From CSV File dialog.

Parent topic:

New CSV Input Stream Step

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/new-csv-input-record-stream-edit-tab.html language=enus -->
## TOPIC 03938: New CSV Input Record Stream Edit Tab

- bundle_id: `teststand-api-reference`
- source_path: `tsref/new-csv-input-record-stream-edit-tab.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/new-csv-input-record-stream-edit-tab.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the New CSV Input Record Stream edit tab in the TestStand Sequence Editor to configure the New CSV Input Record Stream step. The New CSV Input Record Stream edit tab contains the following options: CSV File Path —Specify the path to the CSV file to read, either by browsing to the file or using a

### New CSV Input Record Stream Edit Tab

Use the New CSV Input Record Stream edit tab in the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 to configure the New CSV Input Record Stream step.

The New CSV Input Record Stream edit tab contains the following options:

- CSV File Path 
 —Specify the path to the CSV file to read, either by browsing to the file or using an expression. To specify by expression, check the
 Specify by Expression 
 check box.
- Input Record Stream Reference 
 —Expression that specifies where to store the reference to the CsvFileInputRecordStream the step creates.
- Field Mapping (Optional) 
 —Sets the CsvFileInputRecordStream.FieldMapping property of the newly created stream.
- Simple Formatting Settings 
 —These settings allow you navigate simple formatting common in many CSV files.
  - Scan for Tag 
 —Check the Scan for Tag checkbox to enable the associated expression control and specify a string to search the file for. Reading continues from the line immediately following the tag. Check the
 Ignore Case 
 check box to make comparisons case-insensitive.
  - Skip Lines 
 —Check the
 Skip Lines 
 checkbox to enable the associated expression control and specify the number of lines to skip before reading. If both
 Scan for Tag 
 and
 Skip Lines 
 are enabled, the tag is searched for first. Once the tag is found, the specified number of lines are skipped. Reading continues from the next line in the CSV file.
- Parse Record Prototype Group Box 
 —Check the Parse Record Prototype checkbox to enable the controls in the corresponding group box.
  - Prototype 
 —Specifies a container that defines the prototype for this stream. At run time, TestStand verifies that the prototype in the file matches the specified container.
  - Allow Extra Fields in Record 
 —Allows subproperties of the specified container to be a superset of the fields specified by the prototype in the file. If this box is unchecked, extra fields in the container result in a run-time error.
  - Import Prototype Button 
 —Launches the Import Prototype From CSV File dialog.

Parent topic:

New CSV Input Stream Step

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/new-csv-input-stream-step.html language=enus -->
## TOPIC 03939: New CSV Input Stream Step

- bundle_id: `teststand-api-reference`
- source_path: `tsref/new-csv-input-stream-step.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/new-csv-input-stream-step.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use a New CSV Input Stream step to create a new CsvFileInputRecordStream . Configuring the Step Use the New CSV Input Stream edit tab in the TestStand Sequence Editor or the Configure New CSV Input Stream dialog box in a TestStand User Interface to configure the New CSV Input Stream step.

### New CSV Input Stream Step

Use a New CSV Input Stream step to create a new
 [CsvFileInputRecordStream](csvfileinputrecordstream-and-csvfileoutputrec.html)
 .

#### Configuring the Step

Use the
 [New CSV Input Stream edit tab](new-csv-input-record-stream-edit-tab.html)
 in the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 or the
 [Configure New CSV Input Stream dialog box](new-csv-input-record-stream-dialog-box.html)
 in a
 [TestStand User Interface](teststand-user-interfaces.html)
 to configure the New CSV Input Stream step.

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/new-csv-output-record-stream-edit-tab.html language=enus -->
## TOPIC 03940: New CSV Output Record Stream Edit Tab

- bundle_id: `teststand-api-reference`
- source_path: `tsref/new-csv-output-record-stream-edit-tab.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/new-csv-output-record-stream-edit-tab.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the New CSV Output Record Stream edit tab in the TestStand Sequence Editor to configure the New CSV Output Record Stream step. The New CSV Output Record Stream edit tab contains the following options: CSV File Path —Specify the path to the CSV file to write, either by browsing to the file or usi

### New CSV Output Record Stream Edit Tab

Use the New CSV Output Record Stream edit tab in the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 to configure the New CSV Output Record Stream step.

The New CSV Output Record Stream edit tab contains the following options:

- CSV File Path 
 —Specify the path to the CSV file to write, either by browsing to the file or using an expression. To specify by expression, check the
 Specify by Expression 
 check box.
- File Open Mode 
 —Expression that specifies the file open mode for the underlying CSV file. The mode can be any of the following FileOpenModes constants:
  - FileOpenMode_NoOptions 
 —Create the file if it does not exist. Fail with a runtime error if the file exists.
  - FileOpenMode_Truncate 
 —If the file exists, overwrite it, deleting the previous contents. Create a new file if it does not exist.
  - FileOpenMode_Append 
 —If the file exists, append to the end of it, preserving the existing contents. Create a new file if it does not exist.
  - FileOpenMode_Uniquify 
 —Create a new file if it does not exist. If a file with the specified path exists, attempt to make the file name unique by appending “_” (underscore) plus a numeric suffix to the file name. For example, if AlreadyExists.csv already exists, AlreadyExists_2.csv is tried, then AlreadyExists_3.csv, etc. until a unique name has been found. If a unique name is not found after 10000 attempts, the operation fails with a runtime error.
- Flush After Every Write 
 —Sets the CsvFileOutputRecordStream.AutoFlush property on the CsvFileOutputRecordStream the step creates.
 Note 
 Enabling AutoFlush will adversely impact performance.
- Output Record Stream Reference (Optional) 
 —Expression that specifies where to store the reference to the CsvFileOutputRecordStream the step creates.
- Tag (Optional) 
 —Expression that specifies a string data tag to write to the CSV file before any headers or data.
- Field Headers (Optional) 
 —Expression that specifies the field names for the CsvFileOutputRecordStream. The specified headers are written immediately to the underlying CSV file. The expression may be either a container or an array of strings. If a container is specified, its subproperty names define the field headers. If an array of strings is specified, the array elements define the field headers. In addition, if
 Attach to Execution 
 is checked, the field headers will be written to the Report View for the associated ExecutionOutputRecordStream.
  - Specify Prototype 
 —Writes both the field names and data types to the CSV file as a
 prototype 
 .
- Header Mapping (Optional) 
 —Specifies the mapping from elements (either subproperties or array elements) in the field headers to fields in the stream. The mapping is a comma-separated list of index ranges. For example, "0, 3-5, 8-7" specifies that elements 0, 3, 4, 5, 8, and 7 specify the field names. The final range in the list may be open-ended. For example, "2, 3-" indicates that elements 2, 3, and all elements beyond 3 specify the field names.
- Attach to Execution 
 —Check the
 Attach to Execution 
 checkbox to attach the newly created stream to the current execution.
  - Stream Name 
 —The name of the
 ExecutionOutputRecordStream 
 to associate the newly created CsvFileOutputRecordStream with. If an ExecutionOutputRecordStream with the specified name is already attached to the current execution, the existing one is used. Otherwise, a new ExecutionOutputRecordStream is created with the specified name. You can use the stream name directly with the
 Write Record step type 
 . You can also use it to retrieve the ExecutionOutputRecordStream by invoking ExecutionOutputRecordStreams.GetStream() via the Execution.OutputRecordStreams property of the current execution.
  - Execution Output Record Stream (Optional) 
 —Expression that specifies where to store the reference to the ExecutionOutputRecordStream the step creates or retrieves.
  - Report View 
 —These options control how the ExecutionOutputRecordStream displays information in the Report View.
    - Records to Display 
 —Specifies that value of the ExecutionOutputRecordStream.NumRecordsToDisplayInReportView property of the ExecutionOutputRecordStream. Specify -1 to indicate all records should be displayed. Specify 0 to indicate that no records should be displayed.
    - Set Active Report 
 —Check the Set Active Report checkbox to cause the ExecutionOutputRecordStream to become the active report displayed in the Report View for the current execution. If you leave the box unchecked, you can view the ExecutionOutputRecordStream in the Report View by selecting it manually from the Active Report menu item.

Parent topic:

New CSV Output Stream Step

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/new-csv-output-stream-step.html language=enus -->
## TOPIC 03941: New CSV Output Stream Step

- bundle_id: `teststand-api-reference`
- source_path: `tsref/new-csv-output-stream-step.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/new-csv-output-stream-step.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use a New CSV Output Stream step to create a new CsvFileOutputRecordStream and optionally attach it to the current execution. Configuring the Step Use the New CSV Output Stream edit tab in the TestStand Sequence Editor or the Configure New CSV Output Stream dialog box in a TestStand User Interface t

### New CSV Output Stream Step

Use a New CSV Output Stream step to create a new
 [CsvFileOutputRecordStream](csvfileinputrecordstream-and-csvfileoutputrec.html)
 and optionally attach it to the current execution.

#### Configuring the Step

Use the
 [New CSV Output Stream edit tab](new-csv-output-record-stream-edit-tab.html)
 in the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 or the
 [Configure New CSV Output Stream dialog box](create-csv-output-record-stream-dialog-box.html)
 in a
 [TestStand User Interface](teststand-user-interfaces.html)
 to configure the New CSV Output Stream step.

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/new-data-link-dialog-box.html language=enus -->
## TOPIC 03942: New Data Link Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/new-data-link-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/new-data-link-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Select File»New Data Link , click <Ctrl+N>, or click the New Data Link button in the Database Explorer pane to launch the New Data Link dialog box, in which you can configure new database connections. The New Data Link dialog box contains the following options: Connection Name —Specifies a name for

### New Data Link Dialog Box

Select
 File»New Data Link
 , click <Ctrl+N>, or click the
 New Data Link
 button in the
 [Database Explorer](database-explorer.html)
 pane to launch the New Data Link dialog box, in which you can configure new database connections.

The New Data Link dialog box contains the following options:

- Connection Name 
 —Specifies a name for the new database connection. You must enter a value in this option. Multiple open connections cannot share a connection name. If another connection with the same name already exists, the dialog box displays an error next to the text box when you click
 OK 
 .
- Connection String 
 —Specifies the connection string to use to connect to the database. Multiple open connections cannot share the same connection string. If another connection with the same connection string exists, the dialog box displays an error next to the text box when you click
 OK 
 .

Click
 OK
 to create a new database connection with the specified parameters and add the connection to the Connection List. The Database Viewer populates the Database Object View with the objects present in the database when the connection is created.

#### See Also

[Configuring Connection Strings](/csh?context=ts_tsref_dbviewer_connectionstrings)

Parent topic:

Database Viewer Application

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/new-execution-sequence-call-advanced-settings.html language=enus -->
## TOPIC 03943: New Execution - Sequence Call Advanced Settings Window

- bundle_id: `teststand-api-reference`
- source_path: `tsref/new-execution-sequence-call-advanced-settings.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/new-execution-sequence-call-advanced-settings.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: New Execution The Sequence Call Advanced Settings window contains the following options when you select Use New Execution in the Execution Options control on the Module tab: Initially Suspended —When you enable this option, TestStand creates the new execution in a suspended state. Call the Execution

### New Execution - Sequence Call Advanced Settings Window

#### New Execution

The Sequence Call Advanced Settings window contains the following options when you select
 Use New Execution
 in the
 Execution Options
 control on the
 [Module](sequence-call-module-tab.html)
 tab:

- Initially Suspended 
 —When you enable this option, TestStand creates the new execution in a suspended state. Call the Execution.Resume method in the TestStand API to start the execution.
- Initially Hidden and Disable Tracing 
 —When you enable this option, the window for the new execution is initially hidden and tracing is initially disabled.
 Note 
 If you enable the Initially Hidden and Disable Tracing option, TestStand ignores the Break on Entry option in this window when calling new executions.
- Restartable 
 —When you enable this option, the execution can be restarted after it completes.
- Close Window when Done 
 —When you enable this option, TestStand closes the window for the execution when the execution completes.
- Use Single-Threaded Apartment 
 —Specifies whether the concurrency model of the thread is initialized as single-threaded apartment (STA) or multi-threaded apartment (MTA). By default, TestStand initializes new executions and threads to use the multi-threaded apartment model. A thread must use the single-threaded apartment model if the thread creates or launches a dialog box that contains ActiveX controls.
 If you use this option to launch a sequence that contains a step that displays an ActiveX control, you might need to set the
 Load
 option in the
 [Run Options panel](run-options-panel-step-settings-pane.html)
 of the
 [Step Settings](step-settings-pane.html)
 pane to
 Load Dynamically
 to ensure that TestStand loads the module the step in the thread initialized as STA calls.
- Wait for Execution to Complete 
 —Specifies whether to wait for the execution to complete. The following options are available in the ring control:
  - Before executing next step 
 —Calling sequence waits for the execution to complete before executing another step. TestStand propagates status and error information from the asynchronous execution call to the waiting sequence, and adds results for the asynchronous execution call to the results of the step.
  - Do not wait 
 —Calling sequence does not wait for the execution to complete. Use this option and insert a Wait step in the sequence when you want to obtain the results and control whether TestStand copies status and error information from an asynchronous execution call to the Wait step.
  - At end of current sequence 
 —Calling sequence waits for the execution to complete before the calling sequence returns. TestStand propagates status and error information from the asynchronous execution call to the waiting sequence. However, TestStand does not add results for the asynchronous execution call to the results of the waiting sequence. Use the
 Do not wait 
 option and use a Wait step if you want to obtain the results and control whether TestStand copies status and error information from the asynchronous execution call to the Wait step.
- Process Model Option 
 —Specifies which process model the new execution uses. The following options are available in the ring control:
  - Do not use a process model 
 —The new execution does not run under a process model.
  - Use process model of the specified client file 
 —The execution runs under the process model the sequence file you call specifies as the model of the sequence file. If the file you call does not specify a model, the execution runs under the default station model. When you select this option, you can use the
 Sequence Call Module 
 tab to designate which entry point to call in the process model. Typically, the Process Model entry point calls
 MainSequence 
 in the client sequence file you specify.
  - Use a specific process model 
 —When you select this option, you can use the controls on the
 Sequence Call Module 
 tab to specify the process model under which the new execution runs. When you select this option, you can use the
 Sequence Call Module 
 tab to designate which entry point to call in the process model. Typically, the Process Model entry point calls
 MainSequence 
 in the client sequence file you specify.
- Additional Execution Type Mask Settings (optional) 
 —Passes a numeric value that specifies the
 execution mask settings 
 for the new execution. Refer to
 ExecutionTypeMask 
 for a list of available type mask settings. The settings you specify in this control are combined with any execution mask settings other options in the dialog box specify.
- Store an Object Reference to the New Execution in (optional) 
 —Stores a reference to the new
 Execution 
 object in the ActiveX reference variable you specify. You can use this reference in subsequent calls to the TestStand API. You can also use this reference in a Wait step to wait for the execution to complete.
- Break on Entry 
 —When you enable this option, TestStand suspends the execution before executing the first step.
 Note 
 If you enable the Initially Hidden and Disable Tracing option in this window, TestStand ignores the Break on Entry option when calling new executions.
- CPU Affinity for Initial Thread of Execution 
 —The CPUs on which the initial thread of the execution executes. The following options are available in the ring control:
 
 Refer to
 Using TestStand on SMP Systems 
 for more information about optimizing TestStand performance on symmetric multiprocessing (SMP) systems for multithreaded applications.
  - Use Station Option for CPU Affinity 
 —TestStand uses the
 Default CPU Affinity For Threads station option 
 on the Preferences tab of the Station Options dialog box as the CPU affinity of the initial thread.
  - Use CPU Affinity of Caller 
 —TestStand uses the CPU affinity of the calling sequence as the CPU affinity of the initial thread.
  - Use All CPUs 
 —TestStand uses all CPUs available to the process as the CPU affinity of the initial thread.
  - Use Custom CPU affinity 
 —TestStand determines the CPU affinity of the initial thread using an expression that evaluates to a numeric value, where each bit represents a CPU. The lowest order bit represents the first CPU. For example, a value of
 12 
 (
 1100 
 ) represents CPUs 3 and 4 on a quad-core computer. A value of
 -1 
 represents all CPUs available to the process.

#### See Also

[CPU Affinity Mask Support for 64-bit TestStand](/csh?context=ts_tsfundamentals_64cpuaffinitymask)

[Execution](../tsapiref/execution.html)

[ExecutionTypeMask](../tsapiref/executiontypemask.html)

[Sequence Call Module Tab](sequence-call-module-tab.html)

[Step Settings Pane](step-settings-pane.html)

[Using TestStand on SMP Systems](/csh?context=ts_tsfundamentals_smp_clarification)

Parent topic:

Sequence Call Advanced Settings Window

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/new-thread-sequence-call-advanced-settings-wi.html language=enus -->
## TOPIC 03944: New Thread - Sequence Call Advanced Settings Window

- bundle_id: `teststand-api-reference`
- source_path: `tsref/new-thread-sequence-call-advanced-settings-wi.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/new-thread-sequence-call-advanced-settings-wi.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: New Thread The Sequence Call Advanced Settings window contains the following options when you select Use New Thread in the Execution Options control on the Module tab: Automatically Wait for the Thread to Complete at the End of the Current Sequence —When you enable this option, the calling sequence

### New Thread - Sequence Call Advanced Settings Window

#### New Thread

The Sequence Call Advanced Settings window contains the following options when you select
 Use New Thread
 in the
 Execution Options
 control on the
 [Module](sequence-call-module-tab.html)
 tab:

- Automatically Wait for the Thread to Complete at the End of the Current Sequence 
 —When you enable this option, the calling sequence waits for the thread it launches to complete before the calling sequence returns. TestStand propagates status and error information from the asynchronous thread call to the waiting sequence. However, TestStand does not add results for the asynchronous thread call to the results of the waiting sequence. Disable this option and use a Wait step if you want to obtain the results and control whether TestStand copies status and error information from the asynchronous thread call to the Wait step.
- Initially Suspended 
 —When you enable this option, TestStand creates the new thread in a suspended state. Call the
 Thread.Resume 
 method in the TestStand API to start the thread.
 
 Note 
 If you select Resume in the Debug menu of the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 , TestStand does not resume an
initially suspended thread.
- Use Single-Threaded Apartment 
 —Specifies whether the concurrency model of the thread is initialized as single-threaded apartment (STA) or multi-threaded apartment (MTA). By default, TestStand initializes new executions and threads to use the multi-threaded apartment model. A thread must use the single-threaded apartment model if the thread creates or launches a dialog box that contains ActiveX controls.
 If you use this option to launch a sequence that contains a step that displays an ActiveX control, you may need to set the Load Option in the
 [Run Options panel](run-options-panel-step-settings-pane.html)
 of the
 [Step Settings](step-settings-pane.html)
 pane to
 Load Dynamically.
 This ensures that TestStand loads the module the step calls in the thread initialized as STA.
- Store an Object Reference to the New Thread in (optional) 
 —Stores a reference to the new
 Thread 
 object in the object reference variable you specify. You can use this reference in subsequent calls to the TestStand API. You can also use this reference in a Wait step to wait for the thread to complete.
- CPU Affinity for New Thread 
 —The CPUs on which the new thread executes. The ring control contains the following options:
 
 Refer to
 Using TestStand on SMP Systems 
 for more information about optimizing TestStand performance on symmetric multiprocessing (SMP) systems for multithreaded applications.
  - Use Station Option for CPU Affinity 
 —TestStand uses the
 Default CPU Affinity For Threads station option 
 on the Preferences tab of the Station Options dialog box as the CPU affinity of the new thread.
  - Use CPU Affinity of Caller 
 —TestStand uses the CPU affinity of the calling sequence as the CPU affinity of the new thread.
  - Use All CPUs 
 —TestStand uses all CPUs available to the process as the CPU affinity of the new thread.
  - Use Custom CPU Affinity 
 —TestStand determines the CPU affinity of the new thread using an expression that evaluates to a numeric value, where each bit represents a CPU. The lowest order bit represents the first CPU. For example, a value of
 12 
 (
 1100 
 ) represents CPUs 3 and 4 on a quad-core computer. A value of
 -1 
 represents all CPUs available to the process.

#### See Also

[CPU Affinity Mask Support for 64-bit TestStand](/csh?context=ts_tsfundamentals_64cpuaffinitymask)

[Step Settings Pane](step-settings-pane.html)

[Thread](../tsapiref/thread.html)

[Thread.Resume](../tsapiref/thread-resume.html)

[Using TestStand on SMP Systems](/csh?context=ts_tsfundamentals_smp_clarification)

Parent topic:

Sequence Call Advanced Settings Window

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/new-user-dialog-box.html language=enus -->
## TOPIC 03945: New User Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/new-user-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/new-user-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Call the Engine.DisplayNewUserDialog method to launch the New User dialog box. The New User dialog box contains the following options: User Name —A case-sensitive login name. Full Name —Adds additional information about the name of the user. Comment —Adds additional information about the user. Passw

### New User Dialog Box

Call the
 [Engine.DisplayNewUserDialog](../tsapiref/engine-displaynewuserdialog.html)
 method to launch the New User dialog box.

The New User dialog box contains the following options:

- User Name 
 —A case-sensitive login name.
- Full Name 
 —Adds additional information about the name of the user.
- Comment 
 —Adds additional information about the user.
- Password 
 —A case-sensitive password.
- Confirm Password 
 —Confirms the specified case-sensitive password in the Password control.
- User Profile 
 —Selects a profile, which defines an initial set of privilege settings to give the new user.

#### See Also

[Engine.DisplayNewUserDialog](../tsapiref/engine-displaynewuserdialog.html)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/notification-settings-edit-tab.html language=enus -->
## TOPIC 03946: Notification Settings Edit Tab

- bundle_id: `teststand-api-reference`
- source_path: `tsref/notification-settings-edit-tab.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/notification-settings-edit-tab.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: To display the Notification Settings edit tab in the TestStand Sequence Editor , insert a Notification step and select Edit Notification Settings or Step Settings from the context menu. The following operations are available when you use the Notification step type: Create —Creates a reference to a n

### Notification Settings Edit Tab

To display the Notification Settings edit tab in the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 , insert a Notification step and select
 Edit Notification Settings
 or
 Step Settings
 from the context menu. The following operations are available when you use the Notification step type:

- Create 
 —Creates a reference to a new or existing Notification object.
- Set 
 —Notifies one or more threads that an event has occurred or a condition has been met. When the notification is in a Set state, Wait operations on the notification succeed immediately.
- Clear 
 —Clears the state of the notification so subsequent Wait operations block until the next Set Operation.
- Pulse 
 —Notifies one or all currently waiting threads.
- Wait 
 —Waits until you Set or Pulse the notification. When the notification is already in a Set state, the Wait operation completes immediately.
- Get Status 
 —Obtains information about the state of a
 Notification 
 object.

#### See Also

[Synchronization Step Types](synchronization-step-types.html)

Parent topic:

Notification Step

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/notification-step-configuration-dialog-box.html language=enus -->
## TOPIC 03947: Notification Step Configuration Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/notification-step-configuration-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/notification-step-configuration-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Select Configure Notification in the context menu for the step to launch the Notification Step Configuration dialog box from a TestStand User Interface . You can also click Configure Notification on the General tab of the Step Properties dialog box. In the Notification Step Configuration dialog box,

### Notification Step Configuration Dialog Box

Select
 Configure Notification
 in the context menu for the step to launch the Notification Step Configuration dialog box from a
 [TestStand User Interface](teststand-user-interfaces.html)
 . You can also click
 Configure Notification
 on the
 [General](general-tab-step-properties-dialog-box.html)
 tab of the
 [Step Properties](step-properties-dialog-box.html)
 dialog box. In the Notification Step Configuration dialog box, select an operation for the step to perform.

The following operations are available when you use the Notification step type:

- Create 
 —Creates a reference to a new or existing Notification object.
- Set 
 —Notifies one or more threads that an event has occurred or a condition has been met. When the notification is in a Set state, Wait operations on the notification succeed immediately.
- Clear 
 —Clears the state of the notification so subsequent Wait operations block until the next Set Operation.
- Pulse 
 —Notifies one or all currently waiting threads.
- Wait 
 —Waits until you Set or Pulse the notification. If the notification is already in a Set state, the Wait operation completes immediately.
- Get Status 
 —Obtains information about the state of a
 Notification 
 object.

#### See Also

[Step Properties dialog box](step-properties-dialog-box.html)

[Synchronization Step Types](synchronization-step-types.html)

Parent topic:

Notification Step

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/notification-step.html language=enus -->
## TOPIC 03948: Notification Step

- bundle_id: `teststand-api-reference`
- source_path: `tsref/notification-step.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/notification-step.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use a Notification step to notify threads when a particular event or condition occurs. You can also pass data to the threads you notify. Configuring the Step Use the Notification Settings edit tab in the TestStand Sequence Editor and the Notification Step Configuration dialog box in a TestStand User

### Notification Step

Use a Notification step to notify threads when a particular event or condition occurs. You can also pass data to the threads you notify.

#### Configuring the Step

Use the
 [Notification Settings](notification-settings-edit-tab.html)
 edit tab in the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 and the
 [Notification Step Configuration](notification-step-configuration-dialog-box.html)
 dialog box in a
 [TestStand User Interface](teststand-user-interfaces.html)
 to configure the Notification step.

#### Step Properties

In addition to the
 [common custom properties](/csh?context=ts_tsfundamentals_custom_result_props)
 , the Notification step type defines the following step properties:

- Step.Result.TimeoutOccurred 
 —Exists only when you configure the step for the Wait operation. TestStand sets the value to
 True 
 when the
 Wait operation 
 times out.
 Note 
 If you configure the step to use the Wait operation programmatically, you must also create the
 Step.Result.TimeoutOccurred
 property using the
 newProperty(
 ) method for the step to execute successfully.
- Step.NameOrRefExpr 
 —Contains the Notification
 Name 
 expression for the
 Create operation 
 and the Notification Name or Reference expression for all other Notification operations. For the Wait operation, the expression can also specify an array of names or references.
- Step.LifetimeRefExpr 
 —The object reference expression for the Notification Reference
 Lifetime 
 when you set the lifetime to Use Object Reference.
- Step.TimeoutEnabled 
 —The
 Timeout 
 Enabled setting for the Wait operation.
- Step.TimeoutExpr 
 —The Timeout expression, in seconds, for the Wait operation.
- Step.ErrorOnTimeout 
 —The Timeout Causes Run-Time Error setting for the Wait operation.
- Step.AlreadyExistsExpr 
 —Contains the Already Exists expression for the Create operation or the Notification Exists expression for the
 Get Status operation 
 .
- Step.NumThreadsWaitingExpr 
 —The expression that specifies where to store the number of threads waiting on the notification for the Get Status operation.
- Step.Operation 
 —A value that specifies the operation for the step to perform. The valid values are
 0 
 = Create,
 1 
 = Set,
 2 
 = Clear,
 3 
 = Pulse,
 4 
 = Wait, and
 5 
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
- Step.DataExpr 
 —Contains the Data Value expression for the Set or Pulse operation or the Location to Store Data expression for the Wait or Get Status operation.
- Step.ByRef 
 —The Boolean value that specifies to store the data by object reference instead of by value for the Set or Pulse operation.
- Step.WhichNotificationExpr 
 —The expression that specifies where to store the array offset of the notification to which the Wait operation responds.
- Step.IsSetExpr 
 —The expression that specifies for the Get Status operation where the step stores the Boolean value that indicates the Set state of the notification.
- Step.IsAutoClearExpr 
 —The expression that specifies for the Get Status operation where to store the Boolean value that indicates the AutoClear state of the notification.
- Step.AutoClear 
 —The AutoClear setting for the Set operation.
- Step.PulseNotifyOpt 
 —The setting for the Pulse operation that indicates the threads to send a pulse notification to. The valid values are
 0 
 = Notify First Waiting Thread and
 1 
 = Notify All Waiting Threads.

#### See Also

[Configuring Test Sockets to Wait for Notifications (Example)](/csh?context=ts_8183)

Parent topic:

Synchronization Step Types

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/numeric-format-dialog-box.html language=enus -->
## TOPIC 03949: Numeric Format Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/numeric-format-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/numeric-format-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Click Edit Numeric Format in the Properties dialog box for a numeric array, variable, or property or select Numeric Format from the context menu for a local variable to launch the Numeric Format dialog box. You can also launch this dialog box from other locations. For example, click Edit Format on t

### Numeric Format Dialog Box

Click
 Edit Numeric Format
 in the Properties dialog box for a numeric array, variable, or property or select
 Numeric Format
 from the context menu for a local variable to launch the Numeric Format dialog box. You can also launch this dialog box from other locations. For example, click
 Edit Format
 on the
 [Contents](contents-tab-report-options-dialog-box.html)
 tab of the
 [Report Options](report-options-dialog-box.html)
 dialog box or on the
 [General](general-tab-properties-dialog-box.html)
 tab of the
 [Properties](properties-dialog-box.html)
 dialog box.

Use this dialog box to specify the format TestStand uses to display the value of a numeric variable or property. Changes to the numeric format affect only the display value and do not affect the underlying numeric value of the variable or property. For example, a value of
 5.11111
 displays as
 0x5
 when you select hexadecimal as the format type, even though the underlying value is not a whole number. In addition, text searches you perform with the
 [Find/Replace](find-replace-in-files-dialog-box.html)
 dialog box and the
 [Find in Files](find-replace-dialog-box.html)
 dialog box compare using the formatted value instead of the decimal value.

The Numeric Format dialog box contains the following options:

- Sample 
 —A sample number to which the dialog box applies the current format settings. You can enter different numbers to test the effects of the format settings.
- Formatted Number 
 —Displays the effect of the format settings on the sample number.
- Type 
 —The numeric format type. You can choose one of the following options from the ring control: Real, Integer, Unsigned Integer, Hexadecimal, Octal, Binary, or <
 Use Default 
 >.
 When you select <
 Use Default 
 >, the numeric variable or property does not specify a format and displays using the default TestStand format of
 %.17g 
 unless you specify the format in another option, such as the Default Numeric Format control on the Contents tab of the Report Options dialog box.
- Number of Fractional Digits 
 —The number of digits to display after the decimal point. This control is only visible when you set Type to Real and do not set Exponent to Automatic. If the value to format contains more fractional digits than this control specifies, the fractional portion of the formatted number rounds to the specified number of fractional digits. If the value to format contains fewer fractional digits than this control specifies, the Display Trailing Zeros control determines whether to append zeros to reach the specified number of fractional digits.
- Maximum Number of Significant Digits 
 —The maximum number of significant digits to display. This control only appears when you set Type to Real and Exponent to Automatic.
- Minimum Number of Digits 
 —The minimum number of digits to display. This control is only visible when you do not set Type to Real. If the value to format contains fewer digits than the minimum, this option prefixes the formatted number with leading zeros.
- Minimum Field Width 
 —The minimum number of characters in the formatted number. If the number does not contain the minimum number of characters, TestStand appends spaces before or after the number according to the setting of the Align Left control.
- Sign 
 —Indicates that a sign prefixes the formatted number. The following options are available in the ring control: Minus Sign Only, Plus or Minus Sign, or Space or Minus Sign.
- Exponent 
 —Specifies whether the number appears in scientific notation. The following options are available in the ring control:
  - No 
 —Do not use scientific notation.
  - Yes 
 —Use scientific notation.
  - Automatic 
 —Use the most compact form of notation for the current value.
- Display Trailing Zeros 
 —Appends zeros to the fractional portion of the formatted number if the value to format contains fewer fractional digits than the number the Number of Fractional Digits control specifies. This control applies only when you set Type to Real and the formatted number does not contain an exponent.
- Align Left 
 —When you enable this option, the formatted number aligns to the left edge of the field. The alignment is applied before removing the trailing zeros.
- Fill Width with Leading Zeros 
 —When you enable this option, TestStand fills the empty space before the number with zeros. This option applies only when you set Type to Real and disable the Align Left option.
- Always Show Decimal Point 
 —When you enable this option, the formatted number includes a decimal point even when it does not have a fractional portion. This control applies only when you set Type to Real and the formatted number does not contain an exponent.
- Show Radix Prefix 
 —Specifies whether a radix prefix precedes binary, octal, or hexadecimal numbers.
- Use Uppercase Letters 
 —Specifies whether radix prefixes, exponent characters, and hexadecimal digits appear in uppercase.
- Format 
 —The underlying format code the dialog box settings specify.
- Custom 
 —Enables editing of the underlying format code in the Format control. TestStand supports standard numeric format specifiers. Use the following format:
 %[Flags][Width][.Precision]<Type> 
 with the following valid values:
 
 Note 
 The syntax of the numeric format string is identical to the format string that the C
 printf
 function accepts, with the following exceptions:
 Place a
 $
 character after the
 %
 character in the format string to remove trailing zeros after the decimal point.
 Use a format code of
 %b
 to format a number in binary.
 Specify an empty string to set the format to the default numeric format.
  - Flags 
 — -, +, $, 0, #, blank)
  - Width 
 —0 ... 15
  - Precision 
 —0 ... 15
  - Type 
 —d, i, u, x, X, o, O, b, B, e, E, f, g, G
- Check Format 
 —Checks the validity of any underlying format code you enter in the Format control. This control is only visible when you enable the Custom control.

#### See Also

[Find/Replace dialog box](find-replace-in-files-dialog-box.html)

[Find in Files dialog box](find-replace-dialog-box.html)

[Properties dialog box](properties-dialog-box.html)

[Report Options dialog box](report-options-dialog-box.html)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/numeric-limit-test-edit-tabs.html language=enus -->
## TOPIC 03950: Numeric Limit Test Edit Tabs

- bundle_id: `teststand-api-reference`
- source_path: `tsref/numeric-limit-test-edit-tabs.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/numeric-limit-test-edit-tabs.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Numeric Limit Test edit tabs in the TestStand Sequence Editor to customize the type of comparison and limits TestStand uses to set the step status . The Step Settings pane for the Numeric Limit Test step contains the following tabs: Limits —The type of limit comparison the step performs, the

### Numeric Limit Test Edit Tabs

Use the Numeric Limit Test edit tabs in the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 to customize the type of comparison and limits TestStand uses to set the
 [step status](/csh?context=ts_tsfundamentals_step_status_values_table)
 .

The Step Settings pane for the Numeric Limit Test step contains the following tabs:

- Limits 
 —The type of limit comparison the step performs, the limit values the step uses, as well as the format and units of the value and limits.
- Data Source 
 —The data source for the measurement value the step compares to limit values.

#### See Also

[Test Step Types](test-step-types.html)

Parent topic:

Numeric Limit Test Step

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/numeric-limit-test-step.html language=enus -->
## TOPIC 03951: Numeric Limit Test Step

- bundle_id: `teststand-api-reference`
- source_path: `tsref/numeric-limit-test-step.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/numeric-limit-test-step.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: The Numeric Limit Test step calls a code module that returns a single measurement value. After the code module executes, the Numeric Limit Test step type compares the measurement value to predefined limits. If the measurement value is within the bounds of the limits, the step type sets the step stat

### Numeric Limit Test Step

The Numeric Limit Test step calls a
 [code module](/csh?context=ts_tsfundamentals_bldgblocks_codemodules)
 that returns a single measurement value.

After the code module executes, the Numeric Limit Test step type compares the measurement value to predefined limits. If the measurement value is within the bounds of the limits, the step type sets the
 [step status](/csh?context=ts_tsfundamentals_step_status_values_table)
 to
 Passed
 . Otherwise, it sets the step status to
 Failed
 .

#### Configuring the Step

Use the
 [Numeric Limit Test edit tabs](numeric-limit-test-edit-tabs.html)
 in the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 and the
 [Edit Numeric Limit Test](edit-numeric-limit-test-dialog-box.html)
 dialog box in a
 [TestStand User Interface](teststand-user-interfaces.html)
 to customize the type of comparison and limits TestStand uses to set the step status.

A Numeric Limit Test step uses the
 Step.Result.Numeric
 property to store the measurement value. A code module can set the value of
 Step.Result.Numeric
 in the following ways:

- LabVIEW Adapter 
 —Specify
 Step.Result.Numeric 
 as the Value expression for a Numeric output of a VI on the
 LabVIEW Module 
 tab.
- LabWindows/CVI, C/C++ DLL, .NET, ActiveX/COM, or Sequence Adapter 
 —Pass
 Step.Result.Numeric 
 as a reference parameter to a subsequence or code module.
- LabVIEW or LabWindows/CVI Adapter 
 —The LabVIEW 
and LabWindows/CVI Adapters update the value of
 Step.Result.Numeric 
 automatically after calling legacy code modules. The LabVIEW Adapter updates the value of
 Step.Result.Numeric 
 based on the value of the Numeric Measurement element of the
 Test Data 
 cluster the VI returns. The LabWindows/CVI Adapter updates the value of
 Step.Result.Numeric 
 based on the value of the measurement 
field of the
 tTestData 
 parameter it passes to the C function.
- All Adapters 
 —Use the
 TestStand API 
 to set the value of
 Step.Result.Numeric 
 directly in a code module.

By default, the step type uses the value of the
 Step.Result.Numeric
 property as the numeric measurement to compare the limits against.

#### Step Properties

In addition to the
 [common custom properties](/csh?context=ts_tsfundamentals_custom_result_props)
 , the Numeric Limit Test step type defines the following step properties:

- Step.Result.Numeric 
 —The numeric measurement value. Usually, you set this value in the code module.
- Step.Result.Units 
 —A label that indicates the unit of measurement.
- Step.RawLimits.Low 
 ,
 High 
 ,
 Nominal 
 —The limit values stored with the default TestStand format of
 %.17g 
 . These properties are used to compute the low and high limit values that are used with the
 EQT (== +/-) 
 comparison type.
- Step.Limits.Low 
 ,
 High 
 ,
 LowExpr 
 ,
 HighExpr 
 ,
 UseLowExpr 
 , and
 UseHighExpr 
 —The limits for the comparison.
- Step.Comp 
 —The
 type of comparison 
 , such as EQ.
- Step.CompExpr 
 —The comparison operation using an expression.
- Step.UseCompExpr 
 —The step uses the expression to compare the measurement values.
- Step.InBuf 
 —An arbitrary string the LabVIEW and LabWindows/CVI Adapters pass to the test in the
 Input Buffer 
 control or
 tTestData 
 structure of legacy code modules. This property exists to maintain compatibility with previous test executives. Usually, code modules you develop for TestStand receive data as input parameters or access data as properties using the TestStand API.
- Step.DataSource 
 —A numeric expression the step type uses to set the value of
 Step.Result.Numeric 
 . The default value of the expression is "
 Step.Result.Numeric 
 ", which has the effect of using the value the code module sets. You can customize this expression when you 
do not want to set the value of
 Step.Result.Numeric 
 in the code module.

You can use a Numeric Limit Test step without a code module, which is useful when you want to limit-check a value you have already acquired. To set up this limit check, select
 <None>
 as the module adapter before you insert the step in the sequence and configure
 Step.DataSource
 to specify the value you have already acquired.

Note

#### See Also

[Calling Legacy LabVIEW Code Modules](/csh?context=ts_tsref_labview_legacy)

[Calling Legacy LabWindows/CVI Code Modules](/csh?context=ts_tsref_lwcvicalllegacycodemods)

[Step Types You Can Use with Any Module Adapter](/csh?context=ts_tsfundamentals_universal_step_types)

Parent topic:

Test Step Types

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/numeric-parameters-c-c-dll-call-parameters.html language=enus -->
## TOPIC 03952: Numeric Parameters - C/C++ DLL Call Parameters

- bundle_id: `teststand-api-reference`
- source_path: `tsref/numeric-parameters-c-c-dll-call-parameters.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/numeric-parameters-c-c-dll-call-parameters.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Numeric Parameters The following settings are available in the Data Type ring control when you select Numeric for the category type. Numeric Data Type Setting Equivalent C Data Type Signed 8-bit Integer char Unsigned 8-bit Integer unsigned char Signed 16-bit Integer short Unsigned 16-bit Integer uns

### Numeric Parameters - C/C++ DLL Call Parameters

#### Numeric Parameters

The following settings are available in the Data Type ring control when you select
 Numeric
 for the category type.

| Numeric Data Type Setting | Equivalent C Data Type |
| --- | --- |
| Signed 8-bit Integer | char |
| Unsigned 8-bit Integer | unsigned char |
| Signed 16-bit Integer | short |
| Unsigned 16-bit Integer | unsigned short |
| Signed 32-bit Integer | long |
| Unsigned 32-bit Integer | unsigned long |
| Signed 64-bit Integer | long long, __int64 |
| Unsigned 64-bit Integer | unsigned long long, unsigned __int64 |
| 32-bit Real Number | float |
| 64-bit Real Number | double |

#### Pass by Value or by Reference

When you select the Numeric category for a parameter, the C/C++ DLL Adapter displays the Pass control. which specifies whether TestStand passes the value of the argument you specify in the Value Expression control or passes a pointer to the argument. If you select
 By Pointer (*)
 or
 By Reference (&)
 , the adapter passes a pointer to the argument value.

If you choose to pass a pointer, the argument you specify in the Value Expression control must be the name of a variable or property. When you select the
 Numeric
 category for the return value, you may leave the Value control empty or specify the name of a variable or property.

Note

NULL

Nothing

0

#### Result Actions

The C/C++ DLL Adapter displays the Result Action ring control and the Set Error.Code to Value option for return values and parameters you pass by pointer. Depending on the settings of these controls, TestStand can automatically set the
 Error.Occurred
 and
 Error.Code
 properties of the step according to the value in the numeric argument when the function returns.

Use the Result Action ring control to configure TestStand to set the
 Error.Occurred
 property to
 True
 when the return value or parameter value after the call is greater than zero, less than zero, equal to zero, or not equal to zero. Use the Set Error.Code to Value option to request TestStand to assign the output value of the argument to the
 Error.Code
 property.

Note

Error.Code

Error.Code

#### Enumeration Parameters

When you select a Numeric parameter that accepts an enumerated type from a
 [code module](/csh?context=ts_tsfundamentals_bldgblocks_codemodules)
 that has a type library, the Value Expression control becomes a combo box from which you can select elements of the enumeration. You can also enter an enumeration name or the corresponding numeric value of the enumeration directly into the Value Expression control or the Function Call control.

Note

enum [tag] : __int64 {enum-list} [declarator];

unsigned __int64 {enum-list} [declarator];

#### See Also

[Enumeration Parameters](enumeration-parameters-c-c-dll-call-parameter.html)

[Mapping Parameters](/csh?context=ts_tsref_parameters)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/numeric-parameters-labview-nxg-vi-call-parame.html language=enus -->
## TOPIC 03953: Numeric Parameters - LabVIEW NXG VI Call Parameters

- bundle_id: `teststand-api-reference`
- source_path: `tsref/numeric-parameters-labview-nxg-vi-call-parame.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/numeric-parameters-labview-nxg-vi-call-parame.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Numeric Parameters The LabVIEW NXG Adapter supports all the LabVIEW NXG numeric data types. Some numeric data types require special handling. The imaginary and real parts of a complex number are stored in two different variables. For an array of complex numbers, specify two arrays. The first array h

### Numeric Parameters - LabVIEW NXG VI Call Parameters

#### Numeric Parameters

The LabVIEW NXG Adapter supports all the LabVIEW NXG numeric data types. Some numeric data types require special handling. The imaginary and real parts of a complex number are stored in two different variables. For an array of complex numbers, specify two arrays. The first array holds all the real parts and the second array holds all the imaginary parts. The size of the arrays must be the same. Quad and unsigned quad data types are stored as
 Number {Signed 64-bit Integer}
 and
 Number {Unsigned 64-bit Integer}
 , respectively.

[References to LabVIEW NXG internal objects](references-labview-vi-call-parameters2.html)
 , such as files and queues, are treated as signed 64-bit integers. They are not usable inside of TestStand.

LabVIEW NXG Ring controls are also mapped to Numeric parameters in TestStand.

#### See Also

[LabVIEW NXG Data Types in TestStand](labview-nxg-data-types-in-teststand.html)

[Mapping Parameters](/csh?context=ts_tsref_parameters)

[References](references-labview-vi-call-parameters.html)

Parent topic:

LabVIEW NXG Data Types in TestStand

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/numeric-parameters-labview-vi-call-parameters.html language=enus -->
## TOPIC 03954: Numeric Parameters - LabVIEW VI Call Parameters

- bundle_id: `teststand-api-reference`
- source_path: `tsref/numeric-parameters-labview-vi-call-parameters.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/numeric-parameters-labview-vi-call-parameters.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Numeric Parameters The LabVIEW Adapter supports all of the LabVIEW numeric data types. Some numeric data types require special handling. Extended precision data types are stored as doubles since there is no equivalent data type in TestStand. The imaginary and real parts of a complex number are store

### Numeric Parameters - LabVIEW VI Call Parameters

#### Numeric Parameters

The LabVIEW Adapter supports all of the LabVIEW numeric data types. Some numeric data types require special handling. Extended precision data types are stored as doubles since there is no equivalent data type in TestStand. The imaginary and real parts of a complex number are stored in two different variables. For an array of complex numbers, specify two arrays. The first array holds all of the real parts and the second array holds all of the imaginary parts. The size of the arrays must be the same. Quad and unsigned quad data types are stored as
 Number {Signed 64-bit Integer}
 and
 Number {Unsigned 64-bit Integer}
 , respectively.

[References to LabVIEW internal objects](references-labview-vi-call-parameters.html)
 , such as files and queues, are treated as unsigned longs. They are not usable inside of TestStand.

When you select a numeric parameter that accepts an
 [enumerated type](enumeration-parameters-labview-vi-call-parame.html)
 , the Value column becomes a combo box from which you can select elements of the enumeration.

#### See Also

[Enumeration Parameters](enumeration-parameters-labview-vi-call-parame.html)

[LabVIEW Data Types in TestStand](/csh?context=ts_tsref_labview_data_types)

[Mapping Parameters](/csh?context=ts_tsref_parameters)

[References](references-labview-vi-call-parameters.html)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/numeric-parameters-labwindows-cvi-call-parame.html language=enus -->
## TOPIC 03955: Numeric Parameters - LabWindows/CVI Call Parameters

- bundle_id: `teststand-api-reference`
- source_path: `tsref/numeric-parameters-labwindows-cvi-call-parame.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/numeric-parameters-labwindows-cvi-call-parame.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Numeric Parameters The following settings are available in the Data Type ring control when you select Numeric for the category type: Numeric Data Type Setting Equivalent C Data Type Signed 8-bit Integer char Unsigned 8-bit Integer unsigned char Signed 16-bit Integer short Unsigned 16-bit Integer uns

### Numeric Parameters - LabWindows/CVI Call Parameters

#### Numeric Parameters

The following settings are available in the Data Type ring control when you select
 Numeric
 for the category type:

| Numeric Data Type Setting | Equivalent C Data Type |
| --- | --- |
| Signed 8-bit Integer | char |
| Unsigned 8-bit Integer | unsigned char |
| Signed 16-bit Integer | short |
| Unsigned 16-bit Integer | unsigned short |
| Signed 32-bit Integer | long |
| Unsigned 32-bit Integer | unsigned long |
| Signed 64-bit Integer | long long, __int64 |
| Unsigned 64-bit Integer | unsigned long long, unsigned __int64 |
| 32-bit Real Number | float |
| 64-bit Real Number | double |

#### Pass by Value or by Reference

When you select the Numeric category for a parameter, the LabWindows/CVI Adapter displays the Pass control. This control specifies whether TestStand passes the value of the argument you specify in the Value Expression control or passes a pointer to the argument. If you select
 By Reference (by pointer)
 , the LabWindows/CVI Adapter passes a pointer to the argument value.

If you choose to pass a pointer, the argument you specify in the Value Expression control must be the name of a variable or property. When you select the Numeric category for the return value, you may leave the Value Expression control empty or specify the name of a variable or property.

Note

NULL

Nothing

0

#### Result Actions

The LabWindows/CVI Adapter displays the Result Action ring control and the Set Error.Code to Value option for return values and parameters you pass by pointer. Depending on the settings of these controls, TestStand can automatically set the
 Error.Occurred
 and
 Error.Code
 properties of the step according to the value in the numeric argument when the function returns.

Use the Result Action ring control to configure TestStand to set the
 Error.Occurred
 property to
 True
 when the return value or parameter value after the call is greater than zero, less than zero, equal to zero, or not equal to zero. Use the Set Error.Code control to request TestStand to assign the output value of the argument to the
 Error.Code
 property.

Note

Error.Code

Error.Code

#### Enumeration Parameters

When you select a Numeric parameter that accepts an enumerated type from a
 [code module](/csh?context=ts_tsfundamentals_bldgblocks_codemodules)
 that has a type library, the Value Expression control becomes a combo box where you select elements of the enumeration. You can also enter an enumeration name or the corresponding numeric value for the enumeration directly into the Value Expression or Function Call controls.

#### See Also

[Enumeration Parameters](enumeration-parameters-labwindows-cvi-call-pa.html)

[Mapping Parameters](/csh?context=ts_tsref_parameters)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/numeric-parameters-net-call-parameters.html language=enus -->
## TOPIC 03956: Numeric Parameters - .NET Call Parameters

- bundle_id: `teststand-api-reference`
- source_path: `tsref/numeric-parameters-net-call-parameters.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/numeric-parameters-net-call-parameters.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Numeric Parameters The .NET Adapter supports most of the .NET numeric data types. However, TestStand does not natively support the System.Decimal data type and instead converts it to a double-precision, floating-point number if you store it in a TestStand number variable. This can result in a loss o

### Numeric Parameters - .NET Call Parameters

#### Numeric Parameters

The .NET Adapter supports most of the .NET numeric data types. However, TestStand does not natively support the
 System.Decimal
 data type and instead converts it to a double-precision, floating-point number if you store it in a TestStand number variable. This can result in a loss of precision because the
 System.Decimal
 data type can store numbers with a higher precision than the double-precision, floating-point data type. You can, however, store
 System.Decimal
 data type values in TestStand object reference variables that store the .NET value directly and thus preserve the precision, but you cannot then access the value in TestStand directly.

#### Enumeration Parameters

Use the ring control in the Value column of the Parameters Table on the
 [.NET Module](net-module-tab.html)
 tab of the
 [Step Settings](step-settings-pane.html)
 pane in the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 or on the
 [Module](module-tab-edit-net-call-dialog-box.html)
 tab of the
 [Edit .NET Call](edit-net-call-dialog-box.html)
 dialog box in a
 [TestStand User Interface](teststand-user-interfaces.html)
 to select one of the enumeration values or enter an expression that evaluates to a number, a string that corresponds to the enumeration value, or a compatible TestStand enumeration data type.

To pass an enumeration parameter to a .NET code module using a number, specify a TestStand expression that evaluates to a number. The number must have a numeric representation compatible with the .NET integer type: unsigned 64-bit integer for
 ulong
 , signed 64-bit integer for
 long
 , or the default representation
 float 64
 .

To pass an enumeration parameter using a string, specify a TestStand expression that evaluates to a string for the value parameter. When the .NET Adapter enumeration uses the
 Flags
 attribute, you can pass multiple values of the bit field by separating each element in a string, such as
 "enum 1, enum2"
 .

To pass an enumeration parameter using the TestStand enumeration data type, specify a TestStand expression that evaluates to an enumeration that is compatible with the underlying .NET enum. To be compatible, the TestStand type and underlying .NET type must have identical sets of enumerators. Both types must have the same number of enumerators matching in both name and numeric value, as well as compatible numeric representations. The order in which the enumerators are defined does not matter.

#### See Also

[Edit .NET Call dialog box](edit-net-call-dialog-box.html)

[Mapping Parameters](/csh?context=ts_tsref_parameters)

[Step Settings Pane](step-settings-pane.html)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/object-parameters-c-c-dll-call-parameters.html language=enus -->
## TOPIC 03957: Object Parameters - C/C++ DLL Call Parameters

- bundle_id: `teststand-api-reference`
- source_path: `tsref/object-parameters-c-c-dll-call-parameters.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/object-parameters-c-c-dll-call-parameters.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Object Parameters The Object category includes the ActiveX Automation IDispatch Pointer, ActiveX Automation IUnknown Pointer, and LabWindows/CVI ActiveX Automation Handle data types. Use these types to pass a reference to a TestStand object to the DLL function. You can also use these types to pass t

### Object Parameters - C/C++ DLL Call Parameters

#### Object Parameters

The Object category includes the ActiveX Automation IDispatch Pointer, ActiveX Automation IUnknown Pointer, and LabWindows/CVI ActiveX Automation Handle data types. Use these types to pass a reference to a TestStand object to the DLL function. You can also use these types to pass the value of an object reference property to the DLL function.

If you specify an object reference property as the value of an object parameter, TestStand passes the value of the property. Otherwise, TestStand passes a reference to the property object you specify. The DLL function can use the property object reference in conjunction with the
 [TestStand API](/csh?context=ts_tsapiref_teststand_activex_api_overview)
 to get and set the values of properties in the object, to add properties to the object, and so on.

#### Pass by Value or by Reference

When you select the Object category for a parameter, the C/C++ DLL Adapter displays the Pass control. This control specifies whether TestStand passes the value of the argument you specify in the Value Expression control or passes a pointer to the argument. If you select
 By Pointer (*)
 or
 By Reference (&)
 , the C/C++ DLL Adapter passes a pointer to the argument value.

If you choose to pass a pointer, the argument you specify in the Value Expression control must be the name of a variable or property.

Note

NULL

Nothing

0

#### See Also

[Mapping Parameters](/csh?context=ts_tsref_parameters)

[Pointers and Handles in 32-bit TestStand and 64-bit TestStand](/csh?context=ts_tsfundamentals_64pointerhandles)

[Representing Pointers in Sequences in 32-bit TestStand and 64-bit TestStand](/csh?context=ts_tsfundamentals_64pointers)

[Representing Pointer-Sized Numbers in Sequences in 32-bit TestStand and 64-bit TestStand](/csh?context=ts_tsfundamentals_64pointersizednumbers)

[TestStand ActiveX API Overview](/csh?context=ts_tsapiref_teststand_activex_api_overview)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/object-parameters-labwindows-cvi-call-paramet.html language=enus -->
## TOPIC 03958: Object Parameters - LabWindows/CVI Call Parameters

- bundle_id: `teststand-api-reference`
- source_path: `tsref/object-parameters-labwindows-cvi-call-paramet.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/object-parameters-labwindows-cvi-call-paramet.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Object Parameters The Object category includes the ActiveX Automation IDispatch Pointer (IDispatch *), ActiveX Automation IUnknown Pointer (IUnknown *), and LabWindows/CVI ActiveX Automation Handle (CAObjHandle) data types. Use these types to pass a reference to a TestStand object to the DLL functio

### Object Parameters - LabWindows/CVI Call Parameters

#### Object Parameters

The Object category includes the ActiveX Automation IDispatch Pointer (IDispatch *), ActiveX Automation IUnknown Pointer (IUnknown *), and LabWindows/CVI ActiveX Automation Handle (CAObjHandle) data types. Use these types to pass a reference to a TestStand object to the DLL function. You can also use these types to pass the value of an object reference property to the DLL function.

If you specify an object reference property as the value of an object parameter, TestStand passes the value of the property. Otherwise, TestStand passes a reference to the property object you specify. The DLL function can use the property object reference in conjunction with the
 [TestStand API](/csh?context=ts_tsapiref_teststand_activex_api_overview)
 to get and set the values of properties in the object, to add properties to the object, and so on.

Note

int

long

CAObjHandle

CAObjHandle

CAObjHandle

#### Pass by Value or by Reference

When you select the Object category for a parameter, the LabWindows/CVI Adapter displays the Pass control. This control specifies whether TestStand passes the value of the argument you specify in the Value Expression control or passes a pointer to the argument. If you select
 By Reference (by pointer)
 , the LabWindows/CVI Adapter passes a pointer to the argument value.

When the DLL function stores the value of the object for later use after the function returns, the function must properly add an additional reference to the ActiveX Automation IDispatch Pointer or ActiveX Automation IUnknown Pointer or duplicate the LabWindows/CVI ActiveX Automation Handle. When you pass the object by reference and the DLL function alters the value of the reference, the function must release the original reference.

When you pass an array of object references that use the CAObjHandle data type and the DLL function alters the value of any of the array elements, do not use the function to discard the original handles the array elements contain. TestStand discards the original handles after the call completes.

If you choose to pass a pointer, the argument you specify in the Value Expression control must be the name of a variable or property.

Note

NULL

Nothing

0

#### See Also

[Mapping Parameters](/csh?context=ts_tsref_parameters)

[Pointers and Handles in 32-bit TestStand and 64-bit TestStand](/csh?context=ts_tsfundamentals_64pointerhandles)

[Representing Pointers in Sequences in 32-bit TestStand and 64-bit TestStand](/csh?context=ts_tsfundamentals_64pointers)

[Representing Pointer-Sized Numbers in Sequences in 32-bit TestStand and 64-bit TestStand](/csh?context=ts_tsfundamentals_64pointersizednumbers)

[TestStand ActiveX API Overview](/csh?context=ts_tsapiref_teststand_activex_api_overview)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/odbc-data-source-administrator-dialog-box.html language=enus -->
## TOPIC 03959: ODBC Data Source Administrator Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/odbc-data-source-administrator-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/odbc-data-source-administrator-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Navigate to Administrative Tools on the Microsoft Windows Control Panel and select Data Sources (ODBC) to launch the ODBC Data Source Administrator dialog box. The ODBC Data Source Administrator dialog box lists all the registered ODBC data sources. The dialog box contains tabs for defining data sou

### ODBC Data Source Administrator Dialog Box

Navigate to
 Administrative Tools
 on the Microsoft Windows Control Panel and select
 Data Sources (ODBC)
 to launch the ODBC Data Source Administrator dialog box.

The ODBC Data Source Administrator dialog box lists all the registered ODBC data sources. The dialog box contains tabs for defining data sources and viewing available drivers.

- User DSN 
 —Defines data sources visible only to you.
- System DSN 
 —Defines data sources for all users.
- File DSN 
 —Sets the ODBC Administrator to store the data source definitions in a directory you specify.
- Drivers Tab 
 —Displays the available drivers for the system.

For the User DSN and System DSN tabs, the ODBC Administrator stores the data source definitions in the Windows system registry. Click
 Add
 or
 Configure
 on these tabs to launch a driver-specific dialog box, in which you can configure a new or an existing data source. The system then saves the configuration for the data source in the registry or as a file.

Click
 Help
 to launch the Microsoft online help for any tab in the ODBC Data Source Administrator dialog box.

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/offline-results-file-generation-options-dialo.html language=enus -->
## TOPIC 03960: Offline Results File Generation Options Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/offline-results-file-generation-options-dialo.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/offline-results-file-generation-options-dialo.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Click the icon in the Options column of the Offline Results File plug-in in the Result Processing dialog box to launch the Offline Results File Generation Options dialog box, in which you specify options for an instance of the offline results plug-in, such as determining the directory location for r

### Offline Results File Generation Options Dialog Box

Result Processing

TestStand Offline Results Processing Utility

Note

The Offline Results File Generation Options dialog box contains the following options:

- Directory in Which to Store Result Files 
 —Specifies the directory in which the plug-in instance stores offline result files.
 Note 
 If the combination of the result filename and its directory exceed 259 characters, standard Microsoft Windows functions and applications, such as
 CopyFile()
 and Windows Explorer, that you might use to manage the file do not operate correctly. As a workaround, select a directory with a shorter path, access the directory using a mapped drive letter, or specify the "\\?\" prefix Windows requires to denote extended length paths. Refer to Microsoft MSDN documentation for more information about naming files, paths, and namespaces.
- File Name Format 
 —Shows the components of the filename the plug-in selects. You cannot edit this control. If a file with the same name already exists, the plug-in appends a number to the filename.
- Store Results as They are Generated (On-the-fly) 
 —Enable this option to write results to the file on-the-fly. Disable this option to write results to the file after each UUT completes. Use the
 Advanced Result Processing Settings 
 dialog box to configure on-the-fly result processing.
- Limit the Number of UUTs per File 
 —Specifies to store all the results from an execution in a single file or to create a new result file when the current file contains the results for the number of UUTs you specify. The limit is an approximate threshold that TestStand might exceed to keep the results for all the UUTs in a particular batch within the same results file.
- Automatically Start Offline Result Processing Utility 
 —Enable this option to start the TestStand Offline Results Processing Utility when the offline results plug-in creates a new results file and the utility is not already running.
- Exit When Processing Completes 
 —Enable this option to automatically exit the offline results processing utility when processing is complete. This option has no effect when you have already launched the utility.
- Start Minimized to Tray 
 —Enable this option to automatically start the offline results processing utility minimized in the Microsoft Windows System Notification Area (system tray) of the taskbar.
- Open Offline Results Processing Utility 
 —Launches the TestStand Offline Results Processing Utility.

#### See Also

[Advanced Result Processing Settings dialog box](advanced-result-processing-settings-dialog-bo.html)

[Result Processing dialog box](result-processing-dialog-box.html)

[TestStand Offline Results Processing Utility](/csh?context=ts_tsref_offline_processing_utility)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/open-database-step.html language=enus -->
## TOPIC 03961: Open Database Step

- bundle_id: `teststand-api-reference`
- source_path: `tsref/open-database-step.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/open-database-step.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use an Open Database step to open a database for use in TestStand. The Open Database step returns a database handle you can use to open SQL statements. Configuring the Step Use the Edit Open Database dialog box in the TestStand Sequence Editor or in a TestStand User Interface to configure the Open D

### Open Database Step

Use an Open Database step to open a database for use in TestStand. The Open Database step returns a database handle you can use to open SQL statements.

#### Configuring the Step

Use the
 [Edit Open Database](edit-open-database-dialog-box.html)
 dialog box in the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 or in a
 [TestStand User Interface](teststand-user-interfaces.html)
 to configure the Open Database step.

#### Step Properties

In addition to the
 [common custom properties](/csh?context=ts_tsfundamentals_custom_result_props)
 , the Open Database step type defines the following step properties:

- Step.ConnectionString 
 —A string expression that contains the name of the data link to open.
- Step.DatabaseHandle 
 —The numeric variable or property the step type assigned as the value of the opened database handle.

#### See Also

[Database Step Types](database-step-types.html)

Parent topic:

Database Step Types

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/open-file-dialog-box.html language=enus -->
## TOPIC 03962: Open File Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/open-file-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/open-file-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: TestStand launches the Open File dialog box when TestStand requires you to specify the name and location of a file, such as selecting File»Open . The Open File dialog box contains the following options: Directory History —A list of directories in which files were previously opened from. Look In —The

### Open File Dialog Box

TestStand launches the Open File dialog box when TestStand requires you to specify the name and location of a file, such as selecting
 File»Open
 .

The Open File dialog box contains the following options:

- Directory History 
 —A list of directories in which files were previously opened from.
- Look In 
 —The name of the current directory. The list control displays the contents of the current directory.
- File Name 
 —The name of the file to select.
- Files of Type 
 —The file types to display in the list control that displays the contents of the current directory.
- Use Absolute Path 
 —When you enable this option, TestStand includes the absolute path for the selected file.
- Current Folder 
 —Selects the current directory. This option is available only when selecting the module path in the Python Adapter.

An Open File dialog box launches when you click the
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
 . TestStand then launches additional file selection dialog boxes depending on the type of LabVIEW file you open, as the following table describes.

| LabVIEW File Type | TestStand Behavior |
| --- | --- |
| LabVIEW library ( .llb ) | Browses into the library and launches the Select a VI dialog box, in which you can select a VI the library contains. |
| LabVIEW packed project library ( .lvlibp ) | Displays the content of the packed project library file and launches the Select a VI from a LabVIEW Packed Project Library dialog box, in which you can select a VI the packed project library exports to open. |

#### See Also

[Edit LabVIEW VI Call dialog box](edit-labview-vi-call-dialog-box.html)

[LabVIEW Module Tab](labview-module-tab.html)

[Select a VI dialog box](select-a-vi-dialog-box.html)

[Select a VI from a LabVIEW Packed Project Library dialog box](select-a-vi-from-a-labview-packed-project-lib.html)

[Step Settings Pane](step-settings-pane.html)

[Edit Python Call Dialog Box - Python Module Tab](module-tab-edit-python-call-dialog-box.html)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/open-multiple-file-dialog-box.html language=enus -->
## TOPIC 03963: Open Multiple File Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/open-multiple-file-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/open-multiple-file-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: TestStand launches the Open Multiple File dialog box when TestStand requires you to specify the name and location of one or more files, such as when you add files to a workspace. The Open Multiple File dialog box contains the following options: Directory History —A list of directories in which files

### Open Multiple File Dialog Box

TestStand launches the Open Multiple File dialog box when TestStand requires you to specify the name and location of one or more files, such as when you add files to a workspace.

The Open Multiple File dialog box contains the following options:

- Directory History 
 —A list of directories in which files were previously opened from.
- Look in 
 —The name of the current directory. The list control displays the contents of the current directory.
- File Name 
 —The file the
 Add 
 button adds to the Selected Paths control.
- Files of Type 
 —The file types to display in the list control that displays the contents of the current directory.
- Use Absolute Path 
 —When you enable this option, TestStand includes the absolute path for the selected file.
- Selected Paths 
 —The list of selected files. Click
 Remove 
 to delete the selected item from the list, or click
 Remove All 
 to delete all items from the list.

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/open-sql-statement-step.html language=enus -->
## TOPIC 03964: Open SQL Statement Step

- bundle_id: `teststand-api-reference`
- source_path: `tsref/open-sql-statement-step.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/open-sql-statement-step.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: After you open a database, use an Open SQL Statement step to select the set of data with which to work. An Open SQL Statement step returns a statement handle you can use in Data Operation steps. Configuring the Step Use the Edit Open SQL Statement dialog box in the TestStand Sequence Editor or in a

### Open SQL Statement Step

After you open a database, use an Open SQL Statement step to select the set of data with which to work. An Open SQL Statement step returns a statement handle you can use in
 [Data Operation](data-operation-step.html)
 steps.

#### Configuring the Step

Use the
 [Edit Open SQL Statement](edit-open-sql-statement-dialog-box.html)
 dialog box in the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 or in a
 [TestStand User Interface](teststand-user-interfaces.html)
 to configure the Open SQL Statement step.

#### Step Properties

In addition to the
 [common custom properties](/csh?context=ts_tsfundamentals_custom_result_props)
 , the Open SQL Statement step type defines the following step properties:

- Step.PageSize 
 —The number of records in a page for the SQL statement.
- Step.CommandTimeout 
 —The amount of time, in seconds, TestStand waits while attempting to issue a command to the open database connection.
- Step.CacheSize 
 —The cache size for the SQL statement.
- Step.MaxRecordsToSelect 
 —The maximum number of records the SQL statement can return.
- Step.CursorType 
 —The cursor type the SQL statement uses.
- Step.CursorLocation 
 —Specifies where the data source maintains cursors for a connection.
- Step.MarshalOptions 
 —The marshal options for the updated records in the SQL statement.
- Step.LockType 
 —The lock type for the records the SQL statement selects.
- Step.CommandType 
 —The command type of the SQL statement.
- Step.DatabaseHandle 
 —The name of the variable or property that contains the database handle with which you open the SQL statement.
- Step.StatementHandle 
 —The numeric variable or property the step type assigned as the value of the SQL statement handle.
- Step.SQLStatement 
 —A string expression that contains the SQL command.
- Step.NumberOfRecordsSelected 
 —The numeric variable or property to which the step assigns the number of records the SQL statement returns.
- Step.RequiresParameters 
 —Specifies whether the SQL statement requires input or output parameters to execute. When this property is
 False 
 , the step immediately executes the SQL statement. When this property is
 True 
 , the step only prepares the SQL statement, and a subsequent Data Operation step must perform an Execute operation that defines the parameters for the statement.

#### See Also

[Database Step Types](database-step-types.html)

Parent topic:

Database Step Types

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/open-teststand-sql-file-dialog-box.html language=enus -->
## TOPIC 03965: Open TestStand SQL File Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/open-teststand-sql-file-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/open-teststand-sql-file-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Select File»Open TestStand SQL Files to launch the Open TestStand SQL File dialog box. This menu option is enabled when at least one database connection is open in the Database Viewer. Use the Open TestStand SQL File dialog box to open .sql files that TestStand provides directly in the Database View

### Open TestStand SQL File Dialog Box

Select
 File»Open TestStand SQL Files
 to launch the Open TestStand SQL File dialog box. This menu option is enabled when at least one database connection is open in the Database Viewer.

Use the Open TestStand SQL File dialog box to open .sql files that TestStand provides directly in the Database Viewer or to explore the TestStand .sql files directory.

The dialog box contains the following options:

- Database Provider 
 —Specifies, by default, the database provider of the selected connection in the Database Viewer so you can view all the .sql files associated with the selected database provider. You can view the .sql files associated with the following databases that TestStand supports:
  - Access
  - MySQL
  - Oracle
  - SQL Server
  - Sybase
- TestStand Version 
 —Specifies the TestStand versions associated with the .sql files you want to view. You can select the following versions:
 
 TestStand version 2012 and later 
 is the default selection. This option filters and displays the .sql filenames associated with the selected version. Hover over a filename to display the absolute path of the .sql file.
  - 2.x to 4.0
  - 4.1 to 2010 SP1
  - 2012 and later
  - All
- Open 
 —Opens the selected .sql file that is selected in the list and creates a new
 Execute SQL 
 tab that contains the .sql file content. You can select multiple .sql files in the list and click the
 Open 
 button to create multiple Execute SQL tabs.
 Note 
 Double-clicking a .sql file also opens that file and creates a new Execute SQL tab that contains the .sql file content.
- Explore 
 —Opens the directory of the selected .sql file.

Parent topic:

Database Viewer Application

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/operations-table.html language=enus -->
## TOPIC 03966: Operations Table

- bundle_id: `teststand-api-reference`
- source_path: `tsref/operations-table.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/operations-table.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Operations Table The Operations table displays a list of all the operations the Execution Profiler recorded. Each row in the table displays the following information about an operation: Index —The zero-based index of the operation. The profiler assigns indexes in the order in which it encounters ope

### Operations Table

#### Operations Table

The Operations table displays a list of all the operations the Execution Profiler recorded. Each row in the table displays the following information about an operation:

- Index 
 —The zero-based index of the operation. The profiler assigns indexes in the order in which it encounters operations.
- Operation 
 —The source of the operation, such as Step, UUT, Lock, Step Module, etc, followed by a description of the action performed. Examples:
 Step Module: Execute 
 ,
 Step Module: Load 
 ,
 Notification: Set 
 ,
 Queue: Enqueue 
 .
- State 
 —The current state of the operation. Possible states are Blocked, In Use, Aborted, Timed Out, and Completed.
- Item Name 
 —The name of the item the operation acts upon.
- Events 
 —The number of events the profiler recorded for the operation.
- Completed 
 —Displays
 True 
 if the operation completed, which a state of Completed, Timed Out, or Aborted indicates.
- Start Time 
 —The time of the first event in the operation, measured since the first recorded event.
- End Time 
 —The time of the last event in the operation, or the current time if the operation is not complete, measured since the first recorded event.
- Duration 
 —The time between the values of the Start Time and the End Time columns.
- Time Blocked 
 —The time the operation blocked its thread while waiting to acquire a synchronization item.
- Time in Use 
 —The length of time the operation used its item.
- Test Socket 
 —The zero-based test socket index, if any, for the thread in which the operation takes place. The test socket index indicates the UUT position or test fixture on which the thread operates.
- Thread ID 
 —The TestStand thread ID. This value is unique to each thread.
- Thread 
 —The display name of the thread in which the operation takes place.
- Step 
 —The name of the step that generated the events in the operation. The column displays ellipses (
 … 
 ) if the events are from multiple steps.
- Step Index 
 —The index in a step group of the step that generated the events in the operation. The column displays ellipses (
 … 
 ) if the events are from different step indexes.
- Step Group 
 —The step group of the steps that generated the events in the operation. The column displays ellipses (
 … 
 ) if the events are from multiple step groups.
- Sequence 
 —The name of the sequence that contains the steps that generated the events in the operation. The column displays ellipses (
 … 
 ) if the events are from multiple sequences.
- File 
 —The base name of the sequence file that contains the steps that generated the events in the operation. The column displays ellipses (
 … 
 ) if the events are from multiple files.
- Resource Alternative Index 
 —The zero-based index of the resource alternative the Use Auto Scheduled Resource step selects. Use the Use Auto Scheduled Resource steps to specify alternative sets of resources. The resource set the step actually acquires varies according to the availability of resources at the time the step executes. This column is empty when the event is not for a Use Auto Scheduled Resource step or when the step specifies only one resource alternative.
- Module Path 
 —The file path of the code module associated with the operation. To populate this column, select
 File»Configure Data Collection 
 , then enable
 Module Paths and Environments 
 .
- Module Environment 
 —Information about the module execution environment that might affect performance. To populate this column, select
 File»Configure Data Collection 
 , then enable
 Module Paths and Environments 
 .
- Module Inputs and Outputs 
 —A JSON representation of the values passed to and from the code module. To populate this column, select
 File»Configure Data Collection 
 , then enable
 Module Inputs 
 and/or
 Module Outputs 
 .

#### See Also

[Profiler Window Tables](profiler-window-tables.html)

[Synchronization Step Types](synchronization-step-types.html)

[Using the Configure Data Collection Dialog Box](configure-data-collection-dialog-box.html)

Parent topic:

Profiler Window Tables

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/operators-functions-tab-expression-browser-di.html language=enus -->
## TOPIC 03967: Operators/Functions Tab - Expression Browser Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/operators-functions-tab-expression-browser-di.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/operators-functions-tab-expression-browser-di.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Operators/Functions Tab The Operators/Functions tab contains the following options: Description —The help text for the currently selected operator or function. Replace and Insert —Replaces or inserts a function, operator, or constant at the cursor location in the Expression control. See Also Express

### Operators/Functions Tab - Expression Browser Dialog Box

#### Operators/Functions Tab

The Operators/Functions tab contains the following options:

- Description 
 —The help text for the currently selected operator or function.
- Replace 
 and
 Insert 
 —Replaces or inserts a function, operator, or constant at the cursor location in the Expression control.

#### See Also

[Expression Functions](../tsfundamentals/expression-functions.html)

[Expression Operators](/csh?context=ts_tsfundamentals_operators_expression)

[Levels of Precedence in Operators](/csh?context=ts_tsfundamentals_operators_precedence)

[Special Constant Values](/csh?context=ts_tsfundamentals_special_constant_values)

[Special String Characters](/csh?context=ts_tsfundamentals_special_string_characters)

Parent topic:

Expression Browser Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/optional-parameters-dialog-box.html language=enus -->
## TOPIC 03968: Optional Parameters Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/optional-parameters-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/optional-parameters-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: To launch the Optional Parameters dialog box, click Create VI on the Edit LabVIEW VI Call dialog box after you configure the LabVIEW Adapter with the Allow Legacy and New Templates or Allow Only Legacy Templates option in the LabVIEW Adapter Configuration dialog box. Use this dialog box to specify w

### Optional Parameters Dialog Box

To launch the Optional Parameters dialog box, click
 Create VI
 on the
 [Edit LabVIEW VI Call dialog box](edit-labview-vi-call-dialog-box.html)
 after you configure the LabVIEW Adapter with the
 Allow Legacy and New Templates
 or
 Allow Only Legacy Templates
 option in the
 [LabVIEW Adapter Configuration](labview-adapter-configuration-dialog-box.html)
 dialog box.

Use this dialog box to specify which optional parameters are wired to the legacy VI connector pane.

The Optional Parameters dialog box contains the following options:

- Input Buffer 
 —An optional parameter that you can wire to the connector pane of the VI. This option dims if the Step.InBuf property does not exist for the step you are editing. For example, the
 Input Buffer 
 control dims for an Action step.
- Sequence Context ActiveX Pointer 
 —An optional parameter that you can wire to the connector pane of the VI.
- Invocation Info 
 —An optional parameter that you can wire to the connector pane of the VI.

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/options-pane-current-sequence-analyzer-projec.html language=enus -->
## TOPIC 03969: Options Pane - Current Sequence Analyzer Project Window

- bundle_id: `teststand-api-reference`
- source_path: `tsref/options-pane-current-sequence-analyzer-projec.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/options-pane-current-sequence-analyzer-projec.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Options Pane Use the Options pane to enable or disable the following options: Analyze Skipped Steps —Enable this option to analyze steps for which you set the Run Mode option to Skip. Analyze Subsequences —Enable this option to analyze sequence files that Sequence Call steps call from analyzed seque

### Options Pane - Current Sequence Analyzer Project Window

#### Options Pane

Use the Options pane to enable or disable the following options:

- Analyze Skipped Steps 
 —Enable this option to analyze steps for which you set the Run Mode option to Skip.
- Analyze Subsequences 
 —Enable this option to analyze sequence files that
 Sequence Call steps 
 call from analyzed sequence files. When you use
 expressions 
 in Sequence Call steps to call sequence files, you must add each file to the Sequence Files to Analyze list on the
 Files 
 pane of the
 Current Sequence Analyzer Project 
 window separately.
- Analyze Model Sequence Files 
 —Enable this option to analyze process model sequence files associated with analyzed sequence files.
- Automatically Save Project File 
 —Enable this option to automatically save the project file when you close the file the
 TestStand Sequence Editor 
 or stand-alone
 TestStand Sequence Analyzer application 
 . The default project (
 MyAnalyzerProject.tsaproj 
 ) the sequence editor creates at first launch enables this option. The sequence analyzer disables this option for all other analyzer project files you create.

#### See Also

[Current Sequence Analyzer Project Window](current-sequence-analyzer-project-window.html)

[Sequence Call Step](sequence-call-step.html)

[TestStand Sequence Analyzer Application](teststand-sequence-analyzer-application.html)

Parent topic:

Current Sequence Analyzer Project Window

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/options-tab-configure-message-popup-step-dial.html language=enus -->
## TOPIC 03970: Options Tab - Configure Message Popup Step Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/options-tab-configure-message-popup-step-dial.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/options-tab-configure-message-popup-step-dial.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Options Tab The Options tab contains the following options: Enable Response Text Box —When you enable this option, a string control prompts the operator for a response. Initial Response String —The initial string that appears in the dialog box. You can use the pre-expression built-in property for th

### Options Tab - Configure Message Popup Step Dialog Box

#### Options Tab

The Options tab contains the following options:

- Enable Response Text Box 
 —When you enable this option, a string control prompts the operator for a response.
  - Initial Response String 
 —The initial string that appears in the dialog box. You can use the pre-expression built-in property for the step to assign a value to this step property at run time. Click
 Font/Color Selection 
 to specify the font and the background color for the response text.
  - Max Response String Length 
 —The maximum number of characters a user can input for the string. When you do not want to specify a maximum response string length, enter
 -1 
 in this control.
  - Number of Visible Lines 
 —The number of visible text lines in the response text box.
- Display Image or Web Page 
 —Specifies whether to display an image (
 .gif 
 ,
 .bmp 
 ,
 .ico 
 ,
 .jpg 
 ,
 .jpeg 
 ,
 .png 
 ) or a web page (
 .htm 
 ,
 .html 
 ,
 .xhtml 
 ,
 .shtml 
 ,
 .mht 
 ,
 .mhtml 
 ,
 .txt 
 ,
 .xml 
 ,
 .asp 
 ) in the dialog box.
  - File Source 
 —Where the step loads the file from. You can select from the following options:
    - File 
 —A literal path to the file to load.
    - File by Expression 
 —An expression that evaluates a path to the file to load.
    - Step 
 —Import a file into the step.
- File Pathname 
 —The path or expression to the file to load when you select
 File 
 or
 File by Expression 
 as the File Source.
- Imported Filename 
 —The file to import when you select
 Step 
 as the File Source.
- Import 
 —Loads the specified file into the step when you select
 Step 
 as the File Source.
 Note 
 If you import a web page into the step, you cannot use relative paths to external files within the web page.

Parent topic:

Configure Message Popup Step Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/options-tab-teststand-sequence-analyzer-appli.html language=enus -->
## TOPIC 03971: Options Tab - TestStand Sequence Analyzer Application

- bundle_id: `teststand-api-reference`
- source_path: `tsref/options-tab-teststand-sequence-analyzer-appli.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/options-tab-teststand-sequence-analyzer-appli.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Options Tab Use the Options tab to enable or disable the following options: Analyze Skipped Steps —Enable this option to analyze steps for which you set the Run Mode option to Skip. Analyze Subsequences —Enable this option to analyze sequence files that Sequence Call steps call from analyzed sequenc

### Options Tab - TestStand Sequence Analyzer Application

#### Options Tab

Use the Options tab to enable or disable the following options:

- Analyze Skipped Steps 
 —Enable this option to analyze steps for which you set the Run Mode option to Skip.
- Analyze Subsequences 
 —Enable this option to analyze sequence files that
 Sequence Call steps 
 call from analyzed sequence files. When you use
 expressions 
 in Sequence Call steps to call sequence files, you must add each file to the Sequence Files to Analyze list on the
 Files 
 tab of the sequence analyzer application separately.
- Analyze Model Sequence Files 
 —Enable this option to analyze process model sequence files associated with analyzed sequence files.
- Automatically Save Project File 
 —Enable this option to automatically save the project file when you close the file in the
 TestStand Sequence Editor 
 or sequence analyzer application. The default project (
 MyAnalyzerProject.tsaproj 
 ) the sequence editor creates at first launch enables this option. The sequence analyzer disables this option for all other analyzer project files you create.

#### See Also

[Sequence Call Step](sequence-call-step.html)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/output-pane-context-menu.html language=enus -->
## TOPIC 03972: Output Pane Context Menu

- bundle_id: `teststand-api-reference`
- source_path: `tsref/output-pane-context-menu.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/output-pane-context-menu.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Output Pane Context Menu The items in the context menu for the Output pane vary according to the location you click in the window. The Output Pane context menu can contain the following items: Select Columns —Specifies which columns the TestStand Sequence Editor displays on the pane. Enable the colu

### Output Pane Context Menu

#### Output Pane Context Menu

The items in the context menu for the Output pane vary according to the location you click in the window. The Output Pane context menu can contain the following items:

- Select Columns 
 —Specifies which columns the
 TestStand Sequence Editor 
 displays on the pane. Enable the columns you want to display.
- Show Messages with 
 —The severities and categories of the messages the sequence editor displays. When you disable a severity or category, the sequence editor does not discard the message.
- Clear Execution Messages when Run 
 —When you enable this option, the sequence editor removes output messages associated with completed executions when you start a new execution. The context used to evaluate an OutputMessage expression function or passed to the
 Engine.NewOutputMessage 
 method specifies the execution associated with a message.
- Goto Location in 
 —TestStand locates the step, sequence, or file in the sequence file or execution that posted the message.
- Cut 
 —Removes the selected messages and places them on the clipboard.
- Copy 
 —Copies the selected messages to the clipboard.
- Delete 
 —Deletes the selected messages.
- Clear All 
 —Removes all messages from the pane.
- Select All 
 —Highlights all the messages on the pane.

#### See Also

[Engine.NewOutputMessage](../tsapiref/engine-newoutputmessage.html)

Parent topic:

Output Pane

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/output-pane.html language=enus -->
## TOPIC 03973: Output Pane

- bundle_id: `teststand-api-reference`
- source_path: `tsref/output-pane.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/output-pane.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: The Output pane of the TestStand Sequence Editor displays information messages, warnings, and error messages. By default, the Output pane is empty. Use the OutputMessage expression function , the Engine.NewOutputMessage method, and the OutputMessage.Post method to generate the messages you want to d

### Output Pane

The Output pane of the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 displays information messages, warnings, and error messages. By default, the Output pane is empty. Use the
 [OutputMessage expression function](../tsfundamentals/expression-functions.html)
 , the
 [Engine.NewOutputMessage](../tsapiref/engine-newoutputmessage.html)
 method, and the
 [OutputMessage.Post](../tsapiref/outputmessage-post.html)
 method to generate the messages you want to display. Each message specifies a severity and a timestamp. The message can also specify an icon, a category, and additional execution information. Clicking on a message takes you to the step that generates the message.

By default, the sequence editor generates output messages for any information a source code control (SCC) provider generates.

The Output pane contains the following columns:

- Icon 
 —The icon for a message.
- Message 
 —The text for a message.
- Time Stamp 
 —The date and time TestStand posted the message.
- Category 
 —The category assigned to the message. TestStand uses the Source Control category for messages an SCC provider generates, and the Uncategorized category for messages that do not specify a category.
- Severity 
 —Displays one of the following severities: Information, Warning, or Error.
- Step 
 —The name of the step that is executing when TestStand posts a message from an execution.
- Sequence 
 —The name of the sequence that is executing when TestStand posts a message from an execution.
- Sequence File 
 —The name of the sequence file that is executing when TestStand posts a message from an execution.
- Execution ID 
 —The ID of the execution that posts a message.
- Thread ID 
 —The ID of the thread that posts a message from an execution.

#### See Also

[Engine.NewOutputMessage](../tsapiref/engine-newoutputmessage.html)

[Expression Functions](../tsfundamentals/expression-functions.html)

[Output Messages (Example)](/csh?context=ts_8127)

[OutputMessage.Post](../tsapiref/outputmessage-post.html)

Parent topic:

Panes

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/output-tab-configure-sweep-loop-dialog-box.html language=enus -->
## TOPIC 03974: Output Tab - Configure Sweep Loop Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/output-tab-configure-sweep-loop-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/output-tab-configure-sweep-loop-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Output Tab Specifies the output stream or CSV file to log sweep data to. An output stream is not required, but if one is specified, at least one sweep parameter must be logged. Failing to log any sweep parameters with output enabled results in a run-time error. The Output tab contains the following

### Output Tab - Configure Sweep Loop Dialog Box

#### Output Tab

Specifies the output stream or CSV file to log sweep data to. An output stream is not required, but if one is specified, at least one sweep parameter must be logged. Failing to log any sweep parameters with output enabled results in a run-time error.

The Output tab contains the following option for all non-Stream parameter types:

- Enable Output to Stream/CSV File 
 —Check this box to enable output for this loop. If checked, the output controls are enabled, and the Sweep Loop will write sweep parameters with the log option set at the end of each iteration.
- Output to CSV File 
 —Browse to and select the CSV file to write.
  - Specify file path by expression 
 —Check this box to choose the Directory Path and CSV File Path by entering an expression.
  - Directory Path 
 —Browse to and select the directory path of the CSV file to write.
  - CSV File Name 
 —Specify the CSV file name.
  - Data Tag 
 —Expression that specifies a string data tag to write to the CSV file before any headers or data.
  - File Open Mode 
 —Expression that specifies the file open mode for the underlying CSV file. The mode can be any of the following FileOpenModes constants:
    - FileOpenMode_NoOptions 
 —Create the file if it does not exist. Fail with a runtime error if the file exists.
    - FileOpenMode_Truncate 
 —If the file exists, overwrite it, deleting the previous contents. Create a new file if it does not exist.
    - FileOpenMode_Append 
 —If the file exists, append to the end of it, preserving the existing contents. Create a new file if it does not exist.
    - FileOpenMode_Uniquify 
 —Create a new file if it does not exist. If a file with the specified path exists, attempt to make the file name unique by appending “_” (underscore) plus a numeric suffix to the file name. For example, if AlreadyExists.csv already exists, AlreadyExists_2.csv is tried, then AlreadyExists_3.csv, etc. until a unique name has been found. If a unique name is not found after 10000 attempts, the operation fails with a runtime error.
  - Separator Character 
 —Choose a separator character from the drop down menu.
  - Output to Stream
    - Output Record Stream 
 —Specifies the stream to log sweep parameters to. The expression can be either an object reference or a string. If it is an object reference, it must refer to an
 OutputRecordStream 
 or
 ExecutionOutputRecordStream 
 . If it is a string, it must be the name of an
 ExecutionOutputRecordStream 
 attached to the current execution.
    - Auto Close 
 —Check this box to automatically clean up the output stream at the end of the loop. When this box is checked, upon terminating the loop, the Sweep Loop step closes the stream. If the stream was specified by an object reference, the loop sets the object reference in the Output Record Stream expression to
 Nothing 
 .
 Note 
 Automatic cleanup only occurs if the loop terminates normally by completing its sweep or through a
 [Break step](break-step.html)
 . Cleanup does not occur if execution flow exits the loop for some other reason, such as through a
 [Goto step](goto-step.html)
 .

#### See Also

[Sweep Loop Step](sweep-loop-step.html)

[Sweep Loop Parameters Tab](sweep-parameters-tab-configure-sweep-loop-dia.html)

[Sweep Loop Input Tab](input-tab-configure-sweep-loop-dialog-box.html)

Parent topic:

Configure Sweep Loop Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/output-tab.html language=enus -->
## TOPIC 03975: Output Tab

- bundle_id: `teststand-api-reference`
- source_path: `tsref/output-tab.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/output-tab.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the output stream to log sweep data to. An output stream is not required, but if one is specified, at least one sweep parameter must be logged. Failing to log any sweep parameters with output enabled results in a run-time error. The Output tab contains the following option for all non-Stre

### Output Tab

Specifies the output stream to log sweep data to. An output stream is not required, but if one is specified, at least one sweep parameter must be logged. Failing to log any sweep parameters with output enabled results in a run-time error.

The Output tab contains the following option for all non-Stream parameter types:

- Automatically open Execution view of Sweep Loop Tables when executing 
 —Check this box to display the Test Vector and Value Summary Table View upon step execution.
 Note 
 This table will not launch if any sweep parameters in the step execute with the Stream strategy.

The Output tab contains the following options for the Stream parameter type:

- Enable Output to Stream/CSV File 
 —Check this box to enable output for this loop. If checked, the output controls are enabled, and the Sweep Loop will write sweep parameters with the log option set at the end of each iteration.
- Output to CSV File 
 —Browse to and select the CSV file to write.
  - Specify file path by expression 
 —Check this box to choose the Directory Path and CSV File Path by entering an expression.
  - Directory Path 
 —Browse to and select the directory path of the CSV file to write.
  - CSV File Name 
 —Specify the CSV file name.
  - Data Tag 
 —Expression that specifies a string data tag to write to the CSV file before any headers or data.
  - File Open Mode 
 —Expression that specifies the file open mode for the underlying CSV file. The mode can be any of the following FileOpenModes constants:
    - FileOpenMode_NoOptions 
 —Create the file if it does not exist. Fail with a runtime error if the file exists.
    - FileOpenMode_Truncate 
 —If the file exists, overwrite it, deleting the previous contents. Create a new file if it does not exist.
    - FileOpenMode_Append 
 —If the file exists, append to the end of it, preserving the existing contents. Create a new file if it does not exist.
    - FileOpenMode_Uniquify 
 —Create a new file if it does not exist. If a file with the specified path exists, attempt to make the file name unique by appending “_” (underscore) plus a numeric suffix to the file name. For example, if AlreadyExists.csv already exists, AlreadyExists_2.csv is tried, then AlreadyExists_3.csv, etc. until a unique name has been found. If a unique name is not found after 10000 attempts, the operation fails with a runtime error.
  - Separator Character 
 —Choose a separator character from the drop down menu.
  - Output to Stream
    - Output Record Stream 
 —Specifies the stream to log sweep parameters to. The expression can be either an object reference or a string. If it is an object reference, it must refer to an
 OutputRecordStream 
 or
 ExecutionOutputRecordStream 
 . If it is a string, it must be the name of an
 ExecutionOutputRecordStream 
 attached to the current execution.
    - Auto Close 
 —Check this box to automatically clean up the output stream at the end of the loop. When this box is checked, upon terminating the loop, the Sweep Loop step closes the stream. If the stream was specified by an object reference, the loop sets the object reference in the Output Record Stream expression to
 Nothing 
 .
 Note 
 Automatic cleanup only occurs if the loop terminates normally by completing its sweep or through a
 [Break step](break-step.html)
 . Cleanup does not occur if execution flow exits the loop for some other reason, such as through a
 [Goto step](goto-step.html)
 .

#### See Also

[Sweep Loop Step](sweep-loop-step.html)

[Sweep Loop Parameters Tab](sweep-parameters-tab.html)

[Sweep Loop Input Tab](input-tab.html)

Parent topic:

Sweep Loop Edit Tabs

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/override-module-settings-tab-edit-labview-vi.html language=enus -->
## TOPIC 03976: Override Module Settings Tab - Edit LabVIEW VI Call Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/override-module-settings-tab-edit-labview-vi.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/override-module-settings-tab-edit-labview-vi.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Override Module Settings Tab The LabVIEW Override Module Settings tab contains the following options: Always Run VI in Packed Project Library —Overrides the code module and runs the VI in the packed project library you configure below. This option is available only if the step is configured to call

### Override Module Settings Tab - Edit LabVIEW VI Call Dialog Box

#### Override Module Settings Tab

The LabVIEW Override Module Settings tab contains the following options:

- Always Run VI in Packed Project Library 
 —Overrides the code module and runs the VI in the packed project library you configure below.
 Note 
 This option is available only if the step is configured to call a VI in the context of a project and the project has a build specification configured to build a packed project library containing that VI.
- Source Project Path 
 —Specifies the path of the LabVIEW project configured in the step. This path cannot be changed and must match the path of the project configured for the code module VI.
- Build Specification 
 —Specifies the build specification to use to build the packed project library at the start of execution.
- Project Path 
 —Specifies the path of the LabVIEW project to use when running the VI in the packed project library.
- VI Path 
 —Specifies the path of the VI in the packed project library that executes.
- Binary Class Path 
 —Specifies the path of the LabVIEW class in the packed project library that executes.

#### See Also

[Switching between VIs and Packed Project Libraries](/csh?context=ts_tsref_ppl_debug)

Parent topic:

Edit LabVIEW VI Call Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/override-module-settings-window.html language=enus -->
## TOPIC 03977: Override Module Settings Window

- bundle_id: `teststand-api-reference`
- source_path: `tsref/override-module-settings-window.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/override-module-settings-window.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Click the Override Code Module button on the LabVIEW Module tab of the Step Settings pane to launch the Override Module Settings window. The LabVIEW Override Module Settings window contains the following options: Always Run VI in Packed Project Library —Overrides the code module and runs the VI in t

### Override Module Settings Window

Click the
 Override Code Module
 button on the
 [LabVIEW Module](labview-module-tab.html)
 tab of the Step Settings pane to launch the Override Module Settings window.

The LabVIEW Override Module Settings window contains the following options:

- Always Run VI in Packed Project Library 
 —Overrides the code module and runs the VI in the packed project library you configure below.
 Note 
 This option is available only if the step is configured to call a VI in the context of a project and the project has a build specification configured to build a packed project library containing that VI.
- Source Project Path 
 —Specifies the path of the LabVIEW project configured in the step. This path cannot be changed and must match the path of the project configured for the code module VI.
- Build Specification 
 —Specifies the build specification to use to build the packed project library at the start of execution.
- Project Path 
 —Specifies the path of the LabVIEW project to use when running the VI in the packed project library.
- VI Path 
 —Specifies the path of the VI in the packed project library that executes.
- Binary Class Path 
 —Specifies the path of the LabVIEW class in the packed project library that executes.

#### See Also

[Switching between VIs and Packed Project Libraries](/csh?context=ts_tsref_ppl_debug)

[Edit LabVIEW VI Call dialog box](edit-labview-vi-call-dialog-box.html)

[LabVIEW Module tab](labview-module-tab.html)

Parent topic:

LabVIEW Module Tab

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/package-distribution-tab-teststand-deployment.html language=enus -->
## TOPIC 03978: Package Distribution Tab - TestStand Deployment Utility

- bundle_id: `teststand-api-reference`
- source_path: `tsref/package-distribution-tab-teststand-deployment.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/package-distribution-tab-teststand-deployment.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Package Distribution Options Tab Use the Package Distribution Options tab to configure the settings the TestStand Deployment Utility uses to create a package distribution of the files included in the deployment, and to specify which components to include from TestStand and other National Instruments

### Package Distribution Tab - TestStand Deployment Utility

#### Package Distribution Options Tab

Use the Package Distribution Options tab to configure the settings the TestStand Deployment Utility uses to create a package distribution of the files included in the deployment, and to specify which components to include from TestStand and other National Instruments software. The Package Distribution Options tab is enabled when you select the
 package-based distribution build output
 option in the mode tab

The Package Distribution Options tab contains the following options:

- Display Name 
 —Specifies a user-friendly name for the package. The name is displayed in NI Package manager.
- Output Directory 
 —The directory in which the deployment utility builds the package distribution.
- Install TestStand Runtime 
 —Enable this option to install the TestStand Runtime, which is required to execute TestStand sequences on the test station computer and includes the TestStand Engine.
- Dependencies 
 —Launches the Dependencies dialog box, in which you can specify dependencies for the package from a list of packages on the development computer installer, such as the LabWindows/CVI Run-Time Engine. If the build output is configured to the Repository or Package installer option, required dependency packages are included in the build output. If you set the build output to Single Package, the dependent packages are not included and must be present on the target machine before you can install the deployed package.
- Configure Package Attributes 
 —Launches the Configure Package Attributes dialog box, in which you can customize the attributes of the package which contains the files in the deployment.

#### See Also

[Advanced Installer Options dialog box](advanced-installer-options-dialog-box.html)

[Custom Commands dialog box](custom-commands-dialog-box.html)

[Deploying TestStand Systems](/csh?context=ts_10203)

[Drivers and Components dialog box](drivers-and-components-dialog-box.html)

Licensing Options for TestStand Systems
 section of Chapter 1,
 Introduction to TestStand
 , of the
 [Getting Started with TestStand](/csh?context=ts_8010)
 manual

[TestStand Licensing Options](/csh?context=ts_9050)

Parent topic:

TestStand Deployment Utility

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/packed-project-library-options-dialog-box.html language=enus -->
## TOPIC 03979: Packed Project Library Options Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/packed-project-library-options-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/packed-project-library-options-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Click the Options button in the Output VIs to Packed Project Library section of the LabVIEW VI Options dialog box to launch the Packed Project Library Options dialog box, in which you can configure options for how the TestStand Deployment Utility builds LabVIEW packed project libraries. The Packed P

### Packed Project Library Options Dialog Box

Click the
 Options
 button in the Output VIs to Packed Project Library section of the
 [LabVIEW VI Options](labview-vi-options-dialog-box.html)
 dialog box to launch the Packed Project Library Options dialog box, in which you can configure options for how the
 [TestStand Deployment Utility](teststand-deployment-utility.html)
 builds LabVIEW packed project libraries.

The Packed Project Library Options dialog box contains the following options:

- Base Library Name 
 —The base name the deployment utility uses for packed project library files.
 LabVIEW cannot load two packed project libraries with the same name at the same time. The deployment utility modifies the base library name to ensure that each packed project library file has a unique filename. If the deployment utility builds packed project libraries to multiple
 installation destinations 
 , the deployment utility appends a unique number to each filename after building the first file. If you build a packed project library for VIs called in the context of a LabVIEW project, the deployment utility adds the project name to the base library name.
- Version from Installer 
 —When you enable this option, the deployment utility uses the version of the installer you specify in the
 Advanced Installer Options 
 dialog box to specify the version of the packed project libraries. If you do not enable this option, you must manually specify the version number of the packed project libraries.
- Version Number 
 —Manually specify a version number of the packed project libraries. The version number contains the following components:
  - Major 
 —The major revision number.
  - Minor 
 —The minor revision number.
  - Fix 
 —A revision number to correct existing issues.
  - Build 
 —The specific build number.
    - Auto Increment 
 —Enable this option to specify that the deployment utility automatically increments the build number each time you build.
- Properties 
 —Packed project libraries contain the following internal properties you can view by right-clicking a packed project library file in Microsoft Windows Explorer and selecting
 Properties 
 from the context menu:
  - Product Name 
 —The name you want to display to users.
  - Legal Copyright 
 —The copyright statement you want to display to users.
  - Company Name 
 —The company name you want to display to users.
  - Internal Name 
 —A name intended for only internal use.
  - Description 
 —Information you want to provide to users about the packed project library file.
- Packed Library Source Options 
 —Contains the following options:
  - Include Source for Rebuilding Packed Project Libraries 
 —When you enable this option, the deployment utility includes a copy of the source files and LabVIEW project files required to rebuild the packed project libraries the deployment utility creates during the build.
    - Source Destination 
 —The base directory in which the deployment utility places packed project library source files. The list of source destinations is the same as the list of
 installation destinations 
 in the Installation Destination ring control on the Distributed Files tab.
 Note 
 When you select TestStand Directory, the installer installs files into the directory for the version of TestStand that created the installer.
    - Source Destination Subdirectory 
 —A subdirectory, under the default installation base directory, in which the deployment utility places packed project library source files.

#### See Also

[Advanced Installer Options dialog box](advanced-installer-options-dialog-box.html)

[Installation Destination Options](installation-destination-options-distributed.html)

[LabVIEW VI Options dialog box](labview-vi-options-dialog-box.html)

[Organizing Test Program Files with LabVIEW Packed Project Libraries](/csh?context=ts_tslabview_ppl)

[TestStand Deployment Utility](teststand-deployment-utility.html)

Parent topic:

LabVIEW VI Options Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/panes.html language=enus -->
## TOPIC 03980: Panes

- bundle_id: `teststand-api-reference`
- source_path: `tsref/panes.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/panes.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: A pane is a rectangular area of an application with borders that are bound to adjacent panes. You can use the mouse to resize the boundary between two panes, allowing one pane to occupy more of the space between two panes. The TestStand Sequence Editor uses windows to show sequence files, executions

### Panes

A pane is a rectangular area of an application with borders that are bound to adjacent panes. You can use the mouse to resize the boundary between two panes, allowing one pane to occupy more of the space between two panes. The
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 uses windows to show sequence files, executions, sequence hierarchies, the current sequence analyzer project, station globals, types, and the user manager. The sequence editor uses panes to show all other information.

#### Docking, Hiding, and Floating Panes

You can configure the display state of a pane to one of the following: dock, hide, floating, or auto-hide.

You can rearrange panes in the sequence editor by dragging the title bar of a pane to a new location within the sequence editor window. As you drag the pane from the current location, the sequence editor detaches the pane and displays docking guides. The docking guides show you where you can place the pane. As you move the mouse over a docking guide, the sequence editor highlights where the pane will relocate when dropped.

If you drop a pane on an area other than a docking guide or outside the entire application window, the sequence editor displays the pane in a separate floating window. You can also float a pane by right-clicking the title bar of the pane and selecting
 Floating
 . You can re-dock the pane to the previous location by double-clicking the title bar of the floating pane, right-clicking the title bar of the pane and deselecting
 Floating
 , or you can drag the title bar of the pane back to a docking guide within the sequence editor.

You can hide a pane by clicking the Close icon (
 [IMAGE alt='image' src='../images/Close.gif']
 ) in the top right corner of the pane or by right-clicking the title bar of the pane and selecting
 Hide
 . You can redisplay a hidden pane by selecting the pane in the View menu of the sequence editor.

If you want to configure a pane to automatically hide when the pane is not in use, click the Auto Hide icon (
 [IMAGE alt='image' src='../images/AutoHide.gif']
 ) in the top right corner of the pane or right-click the title bar of the pane and select
 Auto Hide
 . When you activate a different area of the sequence editor, the sequence editor hides the pane temporarily and only displays the tab for the hidden pane. You can redisplay the pane by moving the mouse over the tab for the hidden pane. The pane remains visible as long as the mouse is over the pane or you use the pane

#### Saving and Resetting Pane Configurations

You can use the
 [UI Configuration](ui-configuration-tab-sequence-editor-options.html)
 tab of the
 [Sequence Editor Options](sequence-editor-options-dialog-box.html)
 dialog box to save the configuration state of the panes in the sequence editor. You can also specify whether the sequence editor resets the user interface configuration on startup.

You can reset the user interface configuration state of the panes in the sequence editor by selecting the
 View»Reset UI Configuration
 . The Reset UI Configuration command loads the configuration you specify when you enable the Automatically Load Configuration at Startup setting on the
 [UI Configuration](ui-configuration-tab-sequence-editor-options.html)
 tab of the
 [Sequence Editor Options](sequence-editor-options-dialog-box.html)
 dialog box, otherwise the Reset UI Configuration command loads the default Small Screen Example or Large Screen Example configuration depending on the screen resolution. TestStand considers a 1280 x 1024 minimum screen resolution as large screen. You can also select any saved configuration on the UI Configuration tab of the Sequence Editor Options dialog box and click
 Load Selected
 .

Note

<TestStand Application Data>

<TestStand Application Data>

GeneralEngine.cfg

Templates.ini

#### Locking Pane Configurations

You can configure the sequence editor to prevent a user from customizing the user interface panes by enabling the
 Lock UI Configuration by Disabling the Following
 option on the
 [UI Configuration](ui-configuration-tab-sequence-editor-options.html)
 tab of the
 [Sequence Editor Options](sequence-editor-options-dialog-box.html)
 dialog box and specifying the operations the sequence editor prevents. For example, you might want to prevent a user from rearranging the toolbars or panes within the application, or you might want to hide specific panes, buttons, and menus so the user cannot access specific features. You can also select
 View»Lock/Unlock UI Configuration
 .

#### See Also

[Sequence Editor Options dialog box](sequence-editor-options-dialog-box.html)

[View Menu](view-menu.html)

Parent topic:

TestStand Sequence Editor Menus, Panes, and Windows

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/parameter-name-mapping-dialog-box.html language=enus -->
## TOPIC 03981: Parameter Name/Mapping Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/parameter-name-mapping-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/parameter-name-mapping-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: TestStand launches the Parameter Name/Mapping dialog box when you click Parameter Mapping on the Edit LabVIEW VI Call dialog box for the default module you specify on the General tab of the Step Type Properties dialog box. Use the Parameter Name/Mapping dialog box to specify whether the LabVIEW Adap

### Parameter Name/Mapping Dialog Box

TestStand launches the Parameter Name/Mapping dialog box when you click
 Parameter Mapping
 on the
 [Edit LabVIEW VI Call](edit-labview-vi-call-dialog-box.html)
 dialog box for the default module you specify on the
 [General](general-tab-step-type-properties-dialog-box.html)
 tab of the
 [Step Type Properties](step-type-properties-dialog-box.html)
 dialog box.

Use the Parameter Name/Mapping dialog box to specify whether the LabVIEW Adapter automatically enters argument values for specifically-named VI parameters. For example, if you create a step type configured to use a specific express VI as a default module, you can specify step-specific properties that map to the control names and indicators you can wire to the VI connector pane depending on how you configure the express VI.

The Parameter Name/Mapping dialog box contains the following options:

- Parameter Name List 
 —A list of parameter names and corresponding expression values. Click
 Add 
 to add a parameter name to the list, and click
 Delete 
 to remove the selected parameter name from the list.
- Parameter Name 
 —The parameter name for the selected item in the list.
- Value Expression 
 —The expression value associated with the parameter selected in the list.

#### See Also

[Edit LabVIEW VI Call dialog box](edit-labview-vi-call-dialog-box.html)

[LabVIEW Data Types in TestStand](/csh?context=ts_tsref_labview_data_types)

[Mapping Parameters](/csh?context=ts_tsref_parameters)

[Step Type Properties dialog box](step-type-properties-dialog-box.html)

Parent topic:

Edit LabVIEW VI Call Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/parameters-context-menu-sequence-file-tab.html language=enus -->
## TOPIC 03982: Parameters Context Menu - Sequence File Tab

- bundle_id: `teststand-api-reference`
- source_path: `tsref/parameters-context-menu-sequence-file-tab.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/parameters-context-menu-sequence-file-tab.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Parameters Context Menu To access the context menu, right-click the Parameters item on the Variables pane. The items in the context menu vary depending on whether you right-click a parameter or parameter subproperty. The Parameters context menu can contain the following items: Insert Parameter —A su

### Parameters Context Menu - Sequence File Tab

#### Parameters Context Menu

To access the context menu, right-click the Parameters item on the
 [Variables](variables-pane-sequence-file-tab.html)
 pane. The items in the context menu vary depending on whether you right-click a parameter or parameter subproperty.

The Parameters context menu can contain the following items:

- Insert Parameter 
 —A submenu from which you select the data type for the parameter you want to insert.
 If you want to insert a parameter with a
 custom data type 
 , you must create a named data type.
 After you create the named data type, it appears in the Type submenu of the Insert Parameter submenu.
 If you insert an array, the
 Array Bounds 
 dialog box launches.
- Cut 
 —Removes the selected parameter or subproperty and places it on the clipboard.
- Copy 
 —Copies the selected parameter or subproperty to the clipboard.
- Paste 
 —Inserts the parameter or subproperty from the clipboard.
- Delete 
 —Deletes the parameter.
- Copy Value 
 —Copies the value of the selected property to the clipboard.
- Rename 
 —Displays a control for renaming the selected parameter or subproperty.
- Pass By Reference 
 —The parameter is a reference to the argument the calling sequence passes to the parameter. Passing a parameter by reference allows the subsequence to change the actual value of the argument in the calling sequence.
 When you disable this option for a parameter, TestStand copies the argument value the calling sequence passes as the parameter. This prevents the subsequence from changing the value of the argument in the calling sequence. Copying a large object or array you pass as a parameter can degrade performance.
 Enable this option when you want to return a value from a subsequence to the calling sequence or to reduce the time it takes to pass a large object or array to a subsequence. Disable the option when you want to guarantee that any changes a subsequence makes to a parameter do not affect the argument in the calling sequence.
 Note 
 Do not pass a parameter by reference to a subsequence you call in a separate thread unless you want the new thread to see changes you make to the variable in the calling sequence after the sequence call returns.
- Check Type 
 —TestStand verifies that the data type and representation of the argument you pass as a parameter is compatible with the data type and representation of the parameter. For example, TestStand reports a run-time error when you set this option for a String parameter and then pass a numeric value instead.
 Although type checking is usually a fast operation, you can disable this option when you want to avoid any possible overhead. You can also disable this option when you want to pass arguments with different types or representations in the same parameter field for calls. To pass arguments in this way, specify
 Container 
 as the data type for the parameter and disable the Check Type option. You can use the
 PropertyExists 
 expression function to determine whether the argument a calling sequence passes to the container parameter contains a particular subproperty.
- Advanced 
 —Launches a submenu that contains the following options:
  - Edit Flags 
 —Launches the
 Edit Flags 
 dialog box, in which you can modify the flags for the parameter or subproperty.
  - Edit Attributes 
 —Launches the
 Attributes 
 dialog box, in which you can create and edit attributes for the parameter or subproperty.
- Numeric Format 
 —Launches the
 Numeric Format 
 dialog box, in which you can specify the format TestStand uses to display the value of a numeric property. This control is available only for numeric properties and numeric array properties.
- Representation 
 —The numeric data type standard to use for a number variable or parameter.
  - Double-Precision 64-bit Floating Point (default) 
 —Specifies double-precision, 64-bit floating-point representation.
  - Signed 64-bit Integer 
 —Specifies signed 64-bit integer representation.
  - Unsigned 64-bit Integer 
 —Specifies unsigned 64-bit integer representation.

#### See Also

[Array Bounds dialog box](array-bounds-dialog-box.html)

[Attributes dialog box](attributes-dialog-box.html)

[Edit Flags dialog box](edit-flags-dialog-box.html)

[Numeric Format dialog box](numeric-format-dialog-box.html)

[Variables Pane](variables-pane-sequence-file-tab.html)

Parent topic:

Variables Pane - Sequence File Tab

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/parameters-context-menu-sequence-file-window.html language=enus -->
## TOPIC 03983: Parameters Context Menu - Sequence File Window

- bundle_id: `teststand-api-reference`
- source_path: `tsref/parameters-context-menu-sequence-file-window.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/parameters-context-menu-sequence-file-window.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Parameters Context Menu To access the context menu, right-click the Parameters item on the Variables pane. The items in the context menu vary depending on whether you right-click a parameter or parameter subproperty. The Parameters context menu can contain the following items: Insert Parameter —A su

### Parameters Context Menu - Sequence File Window

#### Parameters Context Menu

To access the context menu, right-click the Parameters item on the
 [Variables](variables-pane-sequence-file-window4.html)
 pane. The items in the context menu vary depending on whether you right-click a parameter or parameter subproperty.

The Parameters context menu can contain the following items:

- Insert Parameter 
 —A submenu from which you select the data type for the parameter you want to insert.
 If you want to insert a parameter with a
 custom data type 
 , you must create a named data type. You can create a named data type in the
 Types 
 window.
 After you create the named data type, it appears in the Type submenu of the Insert Parameter submenu.
 If you insert an array, the
 Array Bounds 
 dialog box launches.
- Cut 
 —Removes the selected parameter or subproperty and places it on the clipboard.
- Copy 
 —Copies the selected parameter or subproperty to the clipboard.
- Paste 
 —Inserts the parameter or subproperty from the clipboard.
- Delete 
 —Deletes the parameter.
- Copy Value 
 —Copies the value of the selected property to the clipboard.
- Rename 
 —Displays a control for renaming the selected parameter or subproperty.
- Pass By Reference 
 —The parameter is a reference to the argument the calling sequence passes to the parameter. Passing a parameter by reference allows the subsequence to change the actual value of the argument in the calling sequence.
 When you disable this option for a parameter, TestStand copies the argument value the calling sequence passes as the parameter. This prevents the subsequence from changing the value of the argument in the calling sequence. Copying a large object or array you pass as a parameter can degrade performance.
 Enable this option when you want to return a value from a subsequence to the calling sequence or to reduce the time it takes to pass a large object or array to a subsequence. Disable the option when you want to guarantee that any changes a subsequence makes to a parameter do not affect the argument in the calling sequence.
 Note 
 Do not pass a parameter by reference to a subsequence you call in a separate thread unless you want the new thread to see changes you make to the variable in the calling sequence after the sequence call returns.
- Check Type 
 —TestStand verifies that the data type and representation of the argument you pass as a parameter is compatible with the data type and representation of the parameter. For example, TestStand reports a run-time error when you set this option for a String parameter and then pass a numeric value instead.
 Although type checking is usually a fast operation, you can disable this option when you want to avoid any possible overhead. You can also disable this option when you want to pass arguments with different types or representations in the same parameter field for calls. To pass arguments in this way, specify
 Container 
 as the data type for the parameter and disable the Check Type option. You can use the
 PropertyExists 
 expression function to determine whether the argument a calling sequence passes to the container parameter contains a particular subproperty.
- Advanced 
 —Launches a submenu that contains the following options:
  - Edit Flags 
 —Launches the
 Edit Flags 
 dialog box, in which you can modify the flags for the parameter or subproperty.
  - Edit Attributes 
 —Launches the
 Attributes 
 dialog box, in which you can create and edit attributes for the parameter or subproperty.
- Numeric Format 
 —Launches the
 Numeric Format 
 dialog box, in which you can specify the format TestStand uses to display the value of a numeric property. This control is available only for numeric properties and numeric array properties.
- Representation 
 —The numeric data type standard to use for a number variable or parameter.
  - Double-Precision 64-bit Floating Point (default) 
 —Specifies double-precision, 64-bit floating-point representation.
  - Signed 64-bit Integer 
 —Specifies signed 64-bit integer representation.
  - Unsigned 64-bit Integer 
 —Specifies unsigned 64-bit integer representation.
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

#### See Also

[Array Bounds dialog box](array-bounds-dialog-box.html)

[Attributes dialog box](attributes-dialog-box.html)

[Edit Flags dialog box](edit-flags-dialog-box.html)

[Numeric Format dialog box](numeric-format-dialog-box.html)

[Sequences Pane](sequences-pane-sequence-file-window.html)

[Steps Pane](steps-pane-sequence-file-window.html)

[Types Window](types-window.html)

[Variables Pane](variables-pane-sequence-file-window4.html)

Parent topic:

Variables Pane - Sequence File Window

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/pass-fail-test-step.html language=enus -->
## TOPIC 03984: Pass/Fail Test Step

- bundle_id: `teststand-api-reference`
- source_path: `tsref/pass-fail-test-step.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/pass-fail-test-step.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: The Pass/Fail Test step calls a code module that makes its own pass/fail determination. After the code module executes, the Pass/Fail Test step type evaluates the Step.Result.PassFail property. If Step.Result.PassFail is True , the step type sets the step status to Passed . If Step.Result.PassFail i

### Pass/Fail Test Step

The Pass/Fail Test step calls a
 [code module](/csh?context=ts_tsfundamentals_bldgblocks_codemodules)
 that makes its own pass/fail determination.

After the code module executes, the Pass/Fail Test step type evaluates the
 Step.Result.PassFail
 property. If
 Step.Result.PassFail
 is
 True
 , the step type sets the
 [step status](/csh?context=ts_tsfundamentals_step_status_values_table)
 to
 Passed
 . If
 Step.Result.PassFail
 is
 False
 , the step type sets the step status to
 Failed
 .

#### Configuring the Step

Use the
 [Data Source](data-source-edit-tab.html)
 edit tab in the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 and the
 [Edit Pass/Fail Source](edit-pass-fail-source-dialog-box.html)
 dialog box in a
 [TestStand User Interface](teststand-user-interfaces.html)
 to specify the data source for the Boolean value the Pass/Fail Test step uses to determine whether the step passes.

A code module can set the value of
 Step.Result.PassFail
 in the following ways:

- LabVIEW Adapter 
 —Specify
 Step.Result.PassFail 
 as the Value expression for a Boolean output of a VI on the
 LabVIEW Module 
 tab.
- LabWindows/CVI, C/C++ DLL, .NET, ActiveX/COM, or Sequence Adapter 
 —Pass
 Step.Result.PassFail 
 as a reference parameter to a subsequence or code module.
- LabVIEW or LabWindows/CVI Adapter 
 —The LabVIEW 
and LabWindows/CVI Adapters update the value of
 Step.Result.PassFail 
 automatically after calling legacy 
code modules. The
 LabVIEW Adapter 
 updates the value of
 Step.Result.PassFail 
 based on the value of the Pass/Fail Flag element of the
 Test Data 
 cluster the VI returns. The
 LabWindows/CVI Adapter 
 updates the value of
 Step.Result.PassFail 
 based on the value of the result field of the tTestData parameter it passes to the C function.
- All Adapters 
 —Use the
 TestStand API 
 to set the value of
 Step.Result.PassFail 
 directly in a code module.

By default, the step type uses the value of the
 Step.Result.PassFail
 Boolean property to determine whether the step passes or fails. To customize the Boolean expression that determines whether the step passes, select
 Edit Data Source
 from the context menu for the step or click the
 [Data Source](data-source-edit-tab.html)
 tab of the
 [Step Settings](step-settings-pane.html)
 pane.

#### Step Properties

In addition to the
 [common custom properties](/csh?context=ts_tsfundamentals_custom_result_props)
 , the Pass/Fail Test step type defines the following step properties:

- Step.Result.PassFail 
 —The Boolean pass/fail flag. Pass is
 True 
 . Fail is
 False 
 . Usually, you set this value in the code module or with a custom pass/fail source expression.
- Step.InBuf 
 —An arbitrary string the LabVIEW and LabWindows/CVI Adapters pass to the test in the
 Input Buffer 
 control or
 tTestData 
 structure of legacy code modules. 
This property exists to maintain compatibility with previous test executives. Usually, code modules you develop for TestStand receive data as input parameters or access data as properties using the TestStand API.
- Step.DataSource 
 —The Boolean expression the step uses to set 
the value of
 Step.Result.PassFail 
 . The default value of the expression is
 "Step.Result.PassFail" 
 , which has the effect 
of using the value the code module sets. You can customize 
this expression when you do not want to set the value of
 Step.Result.PassFail 
 in the code module. For example, you 
can set the data source expression to refer to multiple variables and properties, such as
 RunState.PreviousStep.Result.Numeric * Locals.Attenuation > 12 
 .

#### See Also

[Calling Legacy LabVIEW Code Modules](/csh?context=ts_tsref_labview_legacy)

[Calling Legacy LabWindows/CVI Code Modules](/csh?context=ts_tsref_lwcvicalllegacycodemods)

[Step Types You Can Use with Any Module Adapter](/csh?context=ts_tsfundamentals_universal_step_types)

Parent topic:

Test Step Types

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/password-protect-type-definitions-dialog-box.html language=enus -->
## TOPIC 03985: Password Protect Type Definitions Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/password-protect-type-definitions-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/password-protect-type-definitions-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: In the Types window, select one or more types you want to password-protect , right-click, and select Password Protect from the context menu to launch the Password Protect Type Definitions dialog box, in which you can enable or disable password protection and change the password settings for the sele

### Password Protect Type Definitions Dialog Box

Types

password-protect

Password Protect

context menu

Note

- TestStand supports password-protecting types to deter unauthorized users from editing the types in the sequence editor. However, any TestStand user can continue to programmatically edit a locked type by using the TestStand
 PropertyObject 
 API. National Instruments does not recommend password-protecting types as the only way of protecting intellectual property.
- If you lock at least one type in an INI-formatted sequence file, the entire content of the sequence file becomes protected and unreadable.

After you enable password protection for the types, the types remain unlocked so you can continue to edit the types. TestStand automatically locks password-protected types when TestStand first loads the types. For example, when you restart TestStand or close and reopen all the files that reference the password-protected types, TestStand locks the types. When you restart TestStand, TestStand locks all password-protected types. You can also select one or more password-protected types, right-click, and select
 Lock
 from the context menu to explicitly lock the types. TestStand prompts for the password before you can edit a locked type.

The Password Protect Type Definitions dialog box contains the following options:

- Enable Password Protection 
 —Enable this option to enable password protection for the types. The types must be unlocked to edit the types in the sequence editor. Unlocking types prompts you to enter the password.
- New Password 
 —Enter the password you want the sequence editor to require to unlock the types.
- Re-enter Password 
 —Re-enter the password for confirmation.
- Clear Password History 
 —Clears the password history of the types. When you change the password for the selected types, TestStand adds the old password to the password history of the types. TestStand uses these stored passwords during type conflict resolution in order to avoid having to prompt the user for a password when resolving conflicts for locked types. When you resolve a type conflict or when TestStand resolves a type conflict automatically, if the type being replaced is locked and the type replacing it has the same password as the type being replaced or has the password of the type being replaced stored in its password history, TestStand does not prompt for a password. In all other cases in which type conflict resolution replaces or modifies a locked type, TestStand prompts for a password to unlock the type in order to verify that the user has permission to modify the type. If the user presses the Clear Password History button, when the user dismisses the dialog with the OK button, the dialog box clears the password history after setting the password, so if the user changes the password and clears the password history of a type at the same time, the type’s password history will be empty when the dialog box is done.

#### See Also

[Unlock Type Definitions dialog box](unlock-type-definitions-dialog-box.html)

[Types Window](types-window.html)

[Types Window Context Menu](types-window-context-menu.html)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/pointer-handle-parameters-c-c-dll-call-parame.html language=enus -->
## TOPIC 03986: Pointer/Handle Parameters - C/C++ DLL Call Parameters

- bundle_id: `teststand-api-reference`
- source_path: `tsref/pointer-handle-parameters-c-c-dll-call-parame.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/pointer-handle-parameters-c-c-dll-call-parame.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Pointer/Handle Parameters Use a Pointer/Handle parameter to pass the address of a pointer parameter from a C/C++ DLL code module to TestStand and from TestStand to the code module. Usually, you must allocate a pointer inside a function the code module exports and return the pointer as a void* return

### Pointer/Handle Parameters - C/C++ DLL Call Parameters

#### Pointer/Handle Parameters

Use a Pointer/Handle parameter to pass the address of a pointer parameter from a C/C++ DLL
 [code module](/csh?context=ts_tsfundamentals_bldgblocks_codemodules)
 to TestStand and from TestStand to the code module.

Usually, you must allocate a pointer inside a function the code module exports and return the pointer as a void* return value. TestStand stores the pointer as an object reference, and you can later pass the reference to a different function in the code module. You must release the pointer inside the code module when you no longer need it.

Any pointer, array, or string parameter is compatible with the Pointer/Handle parameter category.

The Variables pane displays
 Pointer:Address
 , where
 Address
 is a hexadecimal number that corresponds to the address of the pointer, when TestStand stores a pointer as an object reference.

#### Pass by Value or Reference

When you select the Pointer/Handle category for a parameter, the C/C++ DLL Adapter displays the Pass control, which specifies whether TestStand passes the value of the argument you specify in the Value Expression control or passes a pointer to the argument. If you select
 By Pointer
 (
 *
 ) or
 By Reference
 (
 &
 ), the adapter passes a pointer to the argument value.

Note

0

#### See Also

[Mapping Parameters](/csh?context=ts_tsref_parameters)

[Pointers and Handles in 32-bit TestStand and 64-bit TestStand](/csh?context=ts_tsfundamentals_64pointerhandles)

[Representing Pointers in Sequences in 32-bit TestStand and 64-bit TestStand](/csh?context=ts_tsfundamentals_64pointers)

[Representing Pointer-Sized Numbers in Sequences in 32-bit TestStand and 64-bit TestStand](/csh?context=ts_tsfundamentals_64pointersizednumbers)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/pointer-handle-parameters-labwindows-cvi-call.html language=enus -->
## TOPIC 03987: Pointer/Handle Parameters - LabWindows/CVI Call Parameters

- bundle_id: `teststand-api-reference`
- source_path: `tsref/pointer-handle-parameters-labwindows-cvi-call.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/pointer-handle-parameters-labwindows-cvi-call.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Pointer/Handle Parameters Use a Pointer/Handle parameter to pass the address of a pointer parameter from a LabWindows/CVI code module to TestStand and from TestStand to the code module. Usually, you must allocate a pointer inside a function the code module exports and return the pointer as a void* r

### Pointer/Handle Parameters - LabWindows/CVI Call Parameters

#### Pointer/Handle Parameters

Use a Pointer/Handle parameter to pass the address of a pointer parameter from a LabWindows/CVI
 [code module](/csh?context=ts_tsfundamentals_bldgblocks_codemodules)
 to TestStand and from TestStand to the code module.

Usually, you must allocate a pointer inside a function the code module exports and return the pointer as a void* return value. TestStand stores the pointer as an object reference, and you can later pass the reference to a different function in the code module. You must release the pointer inside the code module when you no longer need it.

Any pointer, array, or string parameter is compatible with the Pointer/Handle parameter category.

The Variables Pane displays
 Pointer:Address
 , where
 Address
 is a hexadecimal number that corresponds to the address of the pointer, when TestStand stores a pointer as an object reference.

#### Pass by Value or by Reference

When you select the Pointer/Handle category for a parameter, the LabWindows/CVI Adapter displays the Pass control, which specifies whether TestStand passes the value of the argument you specify in the Value Expression control or passes a pointer to the argument. If you select
 By Reference
 (by pointer), the LabWindows/CVI Adapter passes a pointer to the argument value.

Note

Nothing

0

#### See Also

[Mapping Parameters](/csh?context=ts_tsref_parameters)

[Pointers and Handles in 32-bit TestStand and 64-bit TestStand](/csh?context=ts_tsfundamentals_64pointerhandles)

[Representing Pointers in Sequences in 32-bit TestStand and 64-bit TestStand](/csh?context=ts_tsfundamentals_64pointers)

[Representing Pointer-Sized Numbers in Sequences in 32-bit TestStand and 64-bit TestStand](/csh?context=ts_tsfundamentals_64pointersizednumbers)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/post-actions-panel-step-settings-pane.html language=enus -->
## TOPIC 03988: Post Actions Panel - Step Settings Pane

- bundle_id: `teststand-api-reference`
- source_path: `tsref/post-actions-panel-step-settings-pane.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/post-actions-panel-step-settings-pane.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Post Actions Panel The Post Actions panel specifies what type of action occurs after the step executes. You can make the action conditional on the pass/fail status of the step or on any custom condition expression. You can enable the Use Custom Condition option, enter a custom expression that evalua

### Post Actions Panel - Step Settings Pane

#### Post Actions Panel

The Post Actions panel specifies what type of action occurs after the step executes. You can make the action conditional on the pass/fail status of the step or on any custom condition expression. You can enable the Use Custom Condition option, enter a custom expression that evaluates to
 True
 or
 False
 , and select the appropriate actions from the On Condition True and On Condition False ring controls.

The Post Actions panel contains the following categories:

- On Pass 
 —An action that occurs when the step completes with a status of
 Passed 
 .
- On Fail 
 —An action that occurs when the step completes with a status of
 Failed 
 .
- On Condition True 
 —The action that occurs when the step completes and the custom condition expression evaluates to
 True 
 . This option replaces the On Pass option when you enable Use Custom Condition. You cannot select an Else or Else If step as the target of a post action.
- On Condition False 
 —The action that occurs when the step completes and the custom condition expression evaluates to
 False 
 . This option replaces the On Fail option when you enable Use Custom Condition. You cannot select an Else or Else If step as the target of a post action.
- Use Custom Condition 
 —Specifies whether a custom condition controls the post action for the step.

The following post actions appear in the ring controls for the On Pass, On Fail, On Condition True, and On Condition False controls:

- Goto next step 
 —Execution continues normally with the next step. This is the default value.
- Goto step 
 —Execution branches to the destination you select. You can branch to any step in the current step group, to the end of the current step group, or to the Cleanup step group. If the post action for a step specifies if execution branches to the Cleanup step group and the current step is in the Cleanup step group, execution proceeds normally with the next step in the Cleanup step group. You cannot select an Else or Else If step as the target of a post action.
- Terminate execution 
 —Execution
 terminates 
 .
- Call sequence 
 —TestStand calls a sequence before continuing to the next step. You can select any sequence in the sequence file. TestStand does not pass any arguments to the sequence. If the sequence has parameters, TestStand uses their default values.
- Break 
 —TestStand suspends before continuing to the next step.

Parent topic:

Properties Tab - Step Settings Pane

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/post-actions-tab-step-properties-dialog-box.html language=enus -->
## TOPIC 03989: Post Actions Tab - Step Properties Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/post-actions-tab-step-properties-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/post-actions-tab-step-properties-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Post Actions Tab The Post Actions tab of the Step Properties dialog box specifies an action that occurs after a step executes. You can make the action conditional on the Pass/Fail status of the step or on any custom condition. The Post Actions tab contains the following options: On Pass —An action t

### Post Actions Tab - Step Properties Dialog Box

#### Post Actions Tab

The Post Actions tab of the Step Properties dialog box specifies an action that occurs after a step executes. You can make the action conditional on the Pass/Fail status of the step or on any custom condition.

The Post Actions tab contains the following options:

- On Pass 
 —An action that occurs when the step completes with a status of
 Passed 
 .
 The following post actions appear in the ring controls for the On Pass, On Fail, On Condition True, and On Condition False controls:
  - Goto next step 
 —Execution continues normally with the next step. This is the default value.
  - Goto destination 
 —Execution branches to the destination you select. You can branch to any step in any step group, to the end of the current step group, or to the Cleanup step group. If the post action for a step specifies that execution branches to the Cleanup step group and the current step is in the Cleanup step group, execution proceeds normally with the next step in the Cleanup step group. You cannot select an Else or Else If step as the target of a post action.
  - Terminate execution 
 —Execution
 terminates 
 .
  - Call sequence 
 —TestStand calls a sequence before continuing to the next step. You can select any sequence in the sequence file. TestStand does not pass any arguments to the sequence. If the sequence has parameters, TestStand uses their default values.
  - Break 
 —TestStand suspends before continuing to the next step.
- Destination Step (ID or Name) 
 —The destination step for the On Pass, On Fail, On Condition True, and On Condition False controls.
 Note 
 For steps that do not have a
 Passed
 or
 Failed
 status, you can use a custom condition. For example, the TestStand Engine sets the status of an Action step type to
 Done
 , rather than
 Passed
 or
 Failed
 . You can select the Specify Custom Condition option and enter a custom condition expression that evaluates to
 True
 or
 False
 . Then, select the appropriate post actions in the On Condition True and On Condition False ring controls. When you want to unconditionally perform a post action, enter
 True
 in the Custom Condition Expression control.
- On Fail 
 —An action that occurs when the step completes with a status of
 Failed 
 .
- Specify Custom Condition 
 —A custom condition controls the post action for the step.
- Custom Condition Expression 
 —The Boolean expression that controls the post action for the step.
- On Condition True 
 —The action that occurs when the step completes and the custom condition expression evaluates to
 True 
 . You cannot select an Else or Else If step as the target of a post action.
- On Condition False 
 —The action that occurs when the step completes and the custom condition expression evaluates to
 False 
 . You cannot select an Else or Else If step as the target of a post action.

Parent topic:

Step Properties Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/power-supply-step.html language=enus -->
## TOPIC 03990: Power Supply Step

- bundle_id: `teststand-api-reference`
- source_path: `tsref/power-supply-step.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/power-supply-step.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use an IVI Power Supply step to instruct DC power supplies to control the output voltages and currents and to measure output values at the output terminals. Configuring the Step Use the Edit IVI Power Supply Step dialog box in the TestStand Sequence Editor and in a TestStand User Interface to config

### Power Supply Step

Use an IVI Power Supply step to instruct DC power supplies to control the output voltages and currents and to measure output values at the output terminals.

#### Configuring the Step

Use the
 [Edit IVI Power Supply Step](edit-ivi-power-supply-step-dialog-box2.html)
 dialog box in the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 and in a
 [TestStand User Interface](teststand-user-interfaces.html)
 to configure the IVI Power Supply step.

#### Step Operations

The IVI Power Supply step type supports the following operations:

- Configure 
 —Configures the instrument to match the state the step specifies.
- Show Soft Front Panel 
 —Shows the soft front panel (SFP) for the instrument.
- Hide Soft Front Panel 
 —Hides the SFP for the instrument.
- Measure 
 —Takes a measurement on the output signal and returns the measured value.
- Initiate 
 —Directs the power supply to wait for a trigger.
- Abort 
 —Cancels the wait for a trigger.
- Send Software Trigger 
 —Sends a software trigger command to trigger the instrument.
- Reset Output Protection 
 —Resets the output protection feature after an overvoltage or overcurrent condition occurs.
- Get Information 
 —Retrieves low-level status and information from the instrument.

#### Step Properties

In addition to the
 [common custom properties](/csh?context=ts_tsfundamentals_custom_result_props)
 , the IVI Power Supply step type defines the following step properties:

- Step.Result.Reading 
 —The measurement values for the Measure operation. The property data type is an array of NI_IviSinglePoint.
- Step.LogicalName 
 —The logical name expression.
- Step.InstrOperation 
 —A value that specifies the operation you configured the step to perform.
- Step.SettingsSource 
 —The name of the property or variable where the step loads and stores the settings for the operation.
- Step.Configuration 
 —The settings for the Configure operation. The data type of this property is NI_IviDCPowerConfig.
- Step.SoftFrontPanel 
 —The settings for the Show Soft Front Panel operation. The data type of this property is NI_IviSoftFrontPanel.
- Step.Readings 
 —The settings for the Measure operation. The data type of this property is NI_IviDCPowerReadings.
- Step.GetInfo 
 —The settings for the Get Information operation.
- Step.ResetOutputProtection 
 —The channel setting for the Reset Output Protection operation.

#### See Also

[Edit IVI Power Supply Step Dialog Box](edit-ivi-power-supply-step-dialog-box2.html)

Parent topic:

IVI Step Types

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/precondition-builder-dialog-box.html language=enus -->
## TOPIC 03991: Precondition Builder Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/precondition-builder-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/precondition-builder-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Click the Precondition Builder button on the Preconditions panel of the Properties tab of the Step Settings pane to launch the Precondition Builder dialog box in the TestStand Sequence Editor . The Conditions listbox shows the preconditions of the selected step. The label above the listbox includes

### Precondition Builder Dialog Box

Click the
 Precondition Builder
 button on the Preconditions panel of the
 [Properties](properties-tab-step-settings-pane.html)
 tab of the
 [Step Settings](step-settings-pane.html)
 pane to launch the Precondition Builder dialog box in the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 .

The Conditions listbox shows the preconditions of the selected step. The label above the listbox includes the name of the step. The following items can appear in the Conditions listbox:

- Step status condition expression 
 —Step status condition refers to the
 status 
 of other steps in the sequence. In the listbox, step status conditions begin with
 PASS 
 ,
 NOT PASS 
 ,
 FAIL 
 ,
 NOT FAIL 
 ,
 ERROR 
 ,
 NOT ERROR 
 ,
 EXECUTED 
 , or
 NOT EXECUTED 
 , and the name of the step follows.
- Arbitrary expression 
 —You can enter an item that contains an arbitrary expression.
- AllOf block 
 —Brackets multiple
 expressions 
 and evaluates to
 True 
 if all the expressions in the block evaluate to
 True 
 . Each
 AllOf 
 block consists of a line containing
 AllOf 
 and another line containing
 End AllOf 
 .
- AnyOf block 
 —Brackets multiple expression and evaluates to
 True 
 if one or more expressions in the block evaluate to
 True 
 . Each
 AnyOf 
 block consists of a line containing
 AnyOf 
 and another line containing
 End AnyOf 
 .
 Note 
 You can nest one or more blocks within another block. A block treats a nested block as just another expression.

The Precondition Builder dialog box contains the following buttons:

- Cut 
 or
 Copy 
 —Cuts or copies a single precondition or an entire block you select on an
 AllOf 
 or
 AnyOf 
 line in the listbox. The
 Cut 
 and
 Copy 
 buttons dim when you select an
 End AllOf 
 or
 End AnyOf 
 line.
- Paste 
 —Pastes the previously cut or copied precondition below the currently selected precondition.
- Insert New Expression 
 —Inserts an empty, arbitrary expression below the current line in the Condition listbox.
- Insert AllOf 
 —Inserts an empty
 AllOf 
 block below the current line in the Condition listbox.
- Insert AnyOf 
 —Inserts an empty
 AnyOf 
 block below the current line in the Condition listbox.
 To nest a block within an existing block, select the
 AllOf
 or
 AnyOf
 line of the existing block and click
 Insert AnyOf
 or
 Insert AllOf
 . 
 To add a block at the same level as an existing block, select the
 End AllOf
 or
 End AnyOf
 line of the existing block and click
 Insert AnyOf
 or the
 Insert AllOf
 .
- Change Group 
 —When you select an
 AllOf 
 line, you can click
 Change to AnyOf 
 to change the block to an
 AnyOf 
 block. When you select an
 AnyOf 
 , you can click
 Change to AllOf 
 to change the block to an
 AllOf 
 block.
- Ungroup 
 —When you select the
 AllOf 
 line or
 AnyOf 
 line of a block that contains only one expression or that is nested within another block, you can click
 Ungroup 
 to remove the block but keep the contents of the block.
- Edit/View Expression 
 —Views or modifies an expression line in the Condition listbox. You can enter or modify the expression manually in the text box. You can also click the
 Expression Browse 
 button to launch the
 Expression Browser 
 dialog box, in which you can interactively build an expression from lists of available variables, properties, and
 expression operators 
 .
- Insert Step Status 
 —Designs a step status expression. Use the ring control and listbox to choose a step group and step in the sequence. Enable the
 Negate 
 option to negate the meaning of an expression. The Insert Step Status section contains the following command buttons:
  - Insert Step Pass 
 —Inserts an expression that is
 True 
 when the status for the most recent execution of the selected step is
 Passed 
 .
  - Insert Step Fail 
 —Inserts an expression that is
 True 
 when the status for the most recent execution of the selected step is
 Failed 
 .
  - Insert Step Error 
 —Inserts an expression that is
 True 
 when the status of the most recent execution of the selected step is
 Error 
 , which indicates a run-time error occurred in the step.
  - Insert Step Executed 
 —Inserts an expression that is
 True 
 when the status for the most recent execution of the selected step is anything other than an empty string.
 For example, if you select the
 ROM
 step, enable the
 Negate
 option and click
 Insert Step Pass
 , TestStand inserts a line containing
 NOT PASS ROM
 in the listbox.

#### See Also

[Expression Browser dialog box](expression-browser-dialog-box.html)

[Expression Operators](/csh?context=ts_tsfundamentals_operators_expression)

[Step Settings Pane](step-settings-pane.html)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/preconditions-dialog-box.html language=enus -->
## TOPIC 03992: Preconditions Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/preconditions-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/preconditions-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Click Preconditions in the Sequence Properties dialog box or the Step Properties dialog box to launch the Preconditions dialog box. The Step Group and Step controls indicate the step to which the preconditions apply. When you launch the Preconditions dialog box from the Sequence Properties dialog bo

### Preconditions Dialog Box

Click
 Preconditions
 in the
 [Sequence Properties](sequence-properties-dialog-box.html)
 dialog box or the
 [Step Properties](step-properties-dialog-box.html)
 dialog box to launch the Preconditions dialog box.

The Step Group and Step controls indicate the step to which the preconditions apply. When you launch the Preconditions dialog box from the Sequence Properties dialog box, you can use these controls to select any step group and step in the sequence. When you launch the Preconditions dialog box from the Step Properties dialog box or context menu, these controls are not available.

The Preconditions listbox shows the
 [preconditions](precondition-builder-dialog-box.html)
 of the selected step. The label above the listbox includes the name of the step.

#### See Also

[Precondition Builder dialog box](precondition-builder-dialog-box.html)

[Sequence Properties dialog box](sequence-properties-dialog-box.html)

[Step Properties dialog box](step-properties-dialog-box.html)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/preconditions-panel-step-settings-pane.html language=enus -->
## TOPIC 03993: Preconditions Panel - Step Settings Pane

- bundle_id: `teststand-api-reference`
- source_path: `tsref/preconditions-panel-step-settings-pane.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/preconditions-panel-step-settings-pane.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Preconditions Panel The Preconditions panel specifies the conditions that must evaluate to True for TestStand to execute a step during the normal flow of execution in a sequence, such as running a step only if a previous step passes. The Preconditions panel contains the following options: Preconditi

### Preconditions Panel - Step Settings Pane

#### Preconditions Panel

The Preconditions panel specifies the conditions that must evaluate to
 True
 for TestStand to execute a step during the normal flow of execution in a sequence, such as running a step only if a previous step passes. The Preconditions panel contains the following options:

- Precondition Expression 
 —The expression that must evaluate to
 True 
 to execute the step.
- Precondition Builder 
 —Launches the
 Preconditions Builder 
 dialog box, in which you can build a precondition expression using
 step statuses 
 , AllOf and AnyOf conditional groups, and subexpressions.
- Expression Browser Dialog Box 
 —Launches the
 Expression Browser 
 dialog box.
- Check Expression for Errors 
 —Verifies the syntax of the
 expression 
 in the Expression control.

#### See Also

[Expression Browser dialog box](expression-browser-dialog-box.html)

[Preconditions Builder dialog box](precondition-builder-dialog-box.html)

Parent topic:

Properties Tab - Step Settings Pane

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/preferences-tab-station-options-dialog-box.html language=enus -->
## TOPIC 03994: Preferences Tab - Station Options Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/preferences-tab-station-options-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/preferences-tab-station-options-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Preferences Tab The Preferences tab specifies general options for TestStand. The Preferences tab contains the following options: Show Hidden Properties —Displays hidden properties. Most hidden properties are built-in step properties TestStand uses. Prompt to Find Files —Launches the File Not Found d

### Preferences Tab - Station Options Dialog Box

#### Preferences Tab

The Preferences tab specifies general options for TestStand.

The Preferences tab contains the following options:

- Show Hidden Properties 
 —Displays hidden properties. Most hidden properties are built-in step properties TestStand uses.
- Prompt to Find Files 
 —Launches the
 File Not Found 
 dialog box when TestStand cannot find necessary files in the current directory
 search path 
 .
- Reload Documents when Opening Workspace 
 —Loads the documents you had open when you last closed the workspace file. If this option is enabled when you load the workspace, the
 TestStand Sequence Editor 
 reloads the documents.
- Reload Last Workspace at Startup 
 —Loads the workspace that was open when you last closed the sequence editor. If this option is enabled when you launch TestStand, the sequence editor opens the workspace.
- Specify Steps in Expression 
 —Specifies whether TestStand prompts to determine whether to use the name or the unique ID as a step index in a sequence array when inserting the step in an expression on the
 Expression Browser 
 dialog box.
 Note 
 Steps that specify a post action that references another step, Goto steps, Wait steps or preconditions always use the unique ID to reference a step instead of the step name.
- Context of Automatically Created Variables 
 —Specifies the location where TestStand creates automatically generated variables.
- Configuration Directory 
 —The location of the configuration directory. When this value is changed, TestStand displays the Copy Configuration Settings dialog box, in which you can copy the files in the current configuration directory to the new location.
  - <TestStand Default Location> 
 —The default location, which is
 [<TestStand Application Data>](/csh?context=ts_tsfundamentals_directories)
 \Cfg 
 .
 Note 
 TestStand stores the configuration directory path in the Windows registry under the key
 HKEY_LOCAL_MACHINE\SOFTWARE\National Instruments\TestStand\<TestStand Version>\CfgLocation
 . You must have write authority to the Windows registry to change this value. (32-bit TestStand) On 64-bit operating systems, this registry key appears only in the 32-bit registry. Use the path
 HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\National Instruments\TestStand
 to access the key in the registry editor. 
 Note 
 The Configuration Directory setting is only available when running in the global environment. The Configuration Directory setting will be disabled if the engine is currently running in a custom environment.
- Use Computer Name for Station ID 
 —When you enable this option, TestStand identifies the test station with the name of the computer or with a name you provide.
- Default CPU Affinity for Threads 
 —The CPUs on which threads execute for threads TestStand creates and for the user interface thread. This value is a number where each bit represents a CPU. The lowest order bit represents the first CPU. For example, a value of
 12 
 , which is 1100 in binary, represents CPUs 3 and 4 on a quad-core computer. A value of -
 1 
 represents all CPUs available to the process. Use the
 0b 
 prefix to specify a binary number, such as
 0b1100 
 .
Refer to
 Using TestStand on SMP Systems 
 for more information about optimizing TestStand performance on symmetric multiprocessing (SMP) systems for multithreaded applications.
- Preload Progress Dialog Box Delay 
 —Specifies the number of seconds TestStand waits before launching the
 Preload Progress 
 dialog box when preloading modules for execution or opening a file. Use a negative value to disable the Preload Progress dialog box.
- Debug Options 
 —Launches the
 Debug Options 
 dialog box.
- Expression Editing Options 
 —Launches the
 Expression Editing Options 
 dialog box, in which you can customize how TestStand highlights identifiers, operators, constants, and values in expression controls.
- Clear Password Cache 
 —Clears the passwords you stored in the password cache when you enabled the Remember Passwords option in the
 Unlock File 
 dialog box or the
 Unlock Type Definitions 
 dialog box.

#### See Also

[Debug Options dialog box](debug-options-dialog-box.html)

[Expression Browser dialog box](expression-browser-dialog-box.html)

[Expression Editing Options dialog box](expression-editing-options-dialog-box.html)

[File Format Options dialog box](file-format-options-dialog-box.html)

[File Not Found dialog box](file-not-found-dialog-box.html)

[Lock/Unlock File dialog box](lock-unlock-file-dialog-box.html)

[Preload Progress dialog box](preload-progress-dialog-box.html)

[Unlock Type Definitions dialog box](unlock-type-definitions-dialog-box.html)

[Using TestStand on SMP Systems](/csh?context=ts_tsfundamentals_smp_clarification)

[IO Configurations Options Dialog Box](io-configurations-options-dialog-box.html)

Parent topic:

Station Options Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/preload-progress-dialog-box.html language=enus -->
## TOPIC 03995: Preload Progress Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/preload-progress-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/preload-progress-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: When you open or execute a large sequence file that contains multiple code modules that might take a long time to preload, TestStand launches the Preload Progress dialog box, which displays a progress indicator as TestStand preloads the code modules. TestStand calculates the percent completion value

### Preload Progress Dialog Box

When you open or execute a large sequence file that contains multiple
 [code modules](/csh?context=ts_tsfundamentals_bldgblocks_codemodules)
 that might take a long time to preload, TestStand launches the Preload Progress dialog box, which displays a progress indicator as TestStand preloads the code modules.

Note

Enable Build Source Files and Execute

The Preload Progress dialog box launches only after a delay period you specify and only when you open or execute a sequence file that specifies an appropriate preload option or contains a step that specifies an appropriate preload option, as the following table describes. The Preload Progress dialog box includes only the code modules specified by steps or contained in sequence files that specify an appropriate preload option.

| Action You Perform | Sequence File Properties Load Option | Step Properties Load Option |
| --- | --- | --- |
| Open a sequence file | Preload when opening sequence file | — |
| Use step load option | Preload when opening sequence file |  |
| Execute a sequence file | Preload when execution begins | — |
| Use step load option | Preload when execution begins |  |

General

Sequence File Properties

Run Options

Step Settings

TestStand Sequence Editor

Run Options

Step Properties

TestStand User Interface

Note

TestStand Sequence Analyzer

By default, the Preload Progress dialog box launches after a delay period of 3 seconds. You can use the Preload Progress Dialog Box Delay option on the
 [Preferences](preferences-tab-station-options-dialog-box.html)
 tab of the
 [Station Options](station-options-dialog-box.html)
 dialog box to modify the delay period value. You can also use the
 [StationOptions.PreloadProgressDelay](../tsapiref/stationoptions-preloadprogressdelay.html)
 property of the TestStand API to programmatically modify the delay period value. Specify a negative value to disable the Preload Progress dialog box but continue to preload the sequence file.

GetSeqFile_PreloadModules

Engine.GetSequenceFileEx

ExecTypeMask_DisplayPreloadProgress

Engine.NewExecution

SequenceContext.NewExecution

Note

Preload when opening sequence file

Preload when execution begins

GetSeqFile_PreloadModules

ExecTypeMask_DisplayPreloadProgress

Click the
 Cancel
 button in the Preload Progress dialog box when you open a sequence file to cancel the preload and open the sequence file without preloading the code modules.

Click the
 Cancel
 button in the Preload Progress dialog box when you execute a sequence file to cancel the preload and prevent the execution from initiating.

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/previewing-your-imported-data.html language=enus -->
## TOPIC 03996: Previewing Your Imported Data

- bundle_id: `teststand-api-reference`
- source_path: `tsref/previewing-your-imported-data.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/previewing-your-imported-data.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Previewing Your Imported Data The Import Preview dialog box displays the preview of the Import operation performed on the sequence file. The preview displays the values of properties before and after import is done. You can launch this dialog box in the following ways: Click the Import Preview butto

### Previewing Your Imported Data

#### Previewing Your Imported Data

The Import Preview dialog box displays the preview of the Import operation performed on the
sequence file. The preview displays the values of properties before and after import is done. You can launch this dialog box in the following ways:

- Click the
 Import Preview 
 button in the Step Settings pane of the Property Loader step type.
- Click the
 Import Preview 
 button in the Import/Export Properties tool.

The Import Preview dialog box contains the following information:

- Source List 
 —Displays the property loader source that you are using to import values and a
count of changes and insertions introduced in the sequence file to which values are being
imported.
- Differences Table 
 —Displays the differences grouped by sequences, file global variables, file
properties, and types for each specified file.
- Filters Tab 
 —Displays the filters applied for the Differences Table. The Filters tab contains the following options:
  - All 
 —Hides all items with no differences. When you enable this option, the
 Step Properties 
 and
 Element 
 options are disabled.
  - Step Properties 
 —Hides all the properties under a step with no differences.
  - Element 
 —Hides all the elements of a property with no differences.
  - Condense Nested Differences 
 —Hides the subelements of a property that do not have differences and shows only the subproperty that does have a difference. When a property condenses, the parent item of the property replaces the property in the Differences table with the only subelement of the property that has a difference. The utility replaces the name of the subelement in the Differences table with a lookup string, such as
 Locals.Container.Number 
 , that represents the path from the parent element of the property to the only subelement of the property that has a difference.
- External Diff Tool Tab 
 —Enable the
 Use External Differ Tool 
 option when you want to specify an external tool to compare string properties and comments in two files. When you enable this option, the following additional options become available:
 
 Right-click on a string property in the Differences Table whose value has changed after performing import and select
 Launch External Diff Tool 
 to launch the external tool that you specified.
  - Location 
 —The absolute file path to the external tool you want to use.
  - Arguments 
 —The arguments to pass to the external tool. The arguments must always begin with
 %1%2 
 .

Parent topic:

Property Loader Step

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/print-dialog-box.html language=enus -->
## TOPIC 03997: Print Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/print-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/print-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: If at least one tab is open in the Database Viewer, select File»Print to launch the Print dialog box, in which you can define a page header and print, quick print, or preview a document. The Print dialog box includes the following options: Print —Launches the standard Print dialog box, in which you

### Print Dialog Box

If at least one tab is open in the Database Viewer, select
 File»Print
 to launch the Print dialog box, in which you can define a page header and print, quick print, or preview a document.

The Print dialog box includes the following options:

- Print 
 —Launches the standard Print dialog box, in which you can specify settings for printing the grid that displays the data in the selected tab.
- Quick Print 
 —Automatically prints the data grid in the selected tab using the default printer.
- Print Preview 
 —Launches the standard Print Preview dialog box.

Parent topic:

Database Viewer Application

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/problem-reading-function-parameter-list-dialo.html language=enus -->
## TOPIC 03998: Problem Reading Function Parameter List Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/problem-reading-function-parameter-list-dialo.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/problem-reading-function-parameter-list-dialo.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: The C/C++ Module tab or the Edit C/C++ Call dialog box launches the Problem Reading Function Parameter List dialog box when you select a function in a DLL for which the type library does not contain enough information to determine whether a function parameter is a pointer to a single item or an arra

### Problem Reading Function Parameter List Dialog Box

The
 [C/C++ Module](c-c-dll-module-tab.html)
 tab or the
 [Edit C/C++ Call](edit-c-c-dll-call-dialog-box.html)
 dialog box launches the Problem Reading Function Parameter List dialog box when you select a function in a DLL for which the type library does not contain enough information to determine whether a function parameter is a pointer to a single item or an array of items.

The Problem Reading Function Parameter List dialog box contains the following options:

- DLL File 
 —The DLL file path.
- Function Name 
 —The selected function name.
- Parameter Name 
 —The parameter for which the type library does not contain enough information.
- Array Element Type 
 —The data type of the parameter.
- Parameter Number 
 —The position of the parameter.
- Pointer to Single Item 
 —Specifies whether the parameter is a pointer to a single item.
- Array 
 —Specifies whether the parameter is an array. The list control displays additional information required to specify the dimensions of the array or the size of the specific dimension.

#### See Also

[C/C++ Module Tab](c-c-dll-module-tab.html)

[Edit C/C++ Call dialog box](edit-c-c-dll-call-dialog-box.html)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/product-configuration-view.html language=enus -->
## TOPIC 03999: Product Configuration View

- bundle_id: `teststand-api-reference`
- source_path: `tsref/product-configuration-view.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/product-configuration-view.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Product Configuration View Product A listing of the product names collected from the SCM server as defined in the Connection Configuration View . You must select a product to view and select its associated categories. The product name is saved as an SCM attribute. Categories A listing of category na

### Product Configuration View

#### Product Configuration View

#### Product

A listing of the product names collected from the SCM server as defined in the
 [Connection Configuration View](connection-configuration-view.html)
 . You must select a product to view and select its associated categories. The product name is saved as an SCM attribute.

#### Categories

A listing of category names associated with the selected product name. A category represents a common collection of product specifications. You must select one or more categories to get the associated product specifications. The categories are saved as an SCM attribute.

#### Refresh Button

Retrieves categories for the selected product when there is existing SCM data in the active sequence file. The Refresh button does not appear if SCM data is not present in the active sequence file.

Note

#### View Changes Button

Launches the View Differences dialog box, which displays a preview of the changes for the active sequence file when importing newly retrieved SCM data. The View Changes button only appears if differences are detected between SCM data in the active sequence file and newly retrieved SCM data after clicking the Refresh button.

#### See Also

[Import/Update from Specification Compliance Manager (SCM) Tool](import-update-from-specification-compliance-m.html)

[View Differences Dialog](view-differences-dialog.html)

[Specification Compliance Manager Report Options Dialog Box](specification-compliance-manager-report-optio.html)

Parent topic:

Import/Update from Specification Compliance Manager (SCM) Tool

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/profiler-window-tables.html language=enus -->
## TOPIC 04000: Profiler Window Tables

- bundle_id: `teststand-api-reference`
- source_path: `tsref/profiler-window-tables.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/profiler-window-tables.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Profiler Window Tables The tabs in the bottom half of the Execution Profiler window display the following tables: Summary Items Executions Threads Operations Events Rows with a dark background indicate the current selection. A row surrounded dashed lines indicate the current focus. Available menu it

### Profiler Window Tables

#### Profiler Window Tables

The tabs in the bottom half of the Execution Profiler window display the following tables:

- Summary
- Items
- Executions
- Threads
- Operations
- Events

Rows with a dark background indicate the current selection. A row surrounded dashed lines indicate the current focus. Available menu items vary according to the current selection or focus. When you change the selection and focus in a table, the selection and focus also change in the graphs when applicable.

You can sort tables by any column or by multiple columns using secondary sorts. Click the column heading once to sort the column in ascending order, which a triangle icon indicates. Click the column heading again to sort the column in descending order, which an inverted triangle icon indicates. Click the column heading a third time to exit sorting mode. When you apply a sort to a column without removing a sort in another column, the new column becomes the primary sort. A smaller triangle icon indicates a secondary sort.

Select
 Edit»Copy
 to copy column headings and the text of the rows you select to the clipboard.

Right-click a row in the current table and select the
 Select Associated
 context menu item to select and view rows from another table. For example, right-click a row in the Operations table and select
 Select Associated»Events
 to select and view the events that comprise the operations you selected in the Operations table.

Parent topic:

TestStand Environment Reference Help
