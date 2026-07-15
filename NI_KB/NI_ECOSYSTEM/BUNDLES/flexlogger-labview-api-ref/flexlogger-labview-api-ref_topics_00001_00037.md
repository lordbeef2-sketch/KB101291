# NI DOCUMENT BUNDLE: flexlogger-labview-api-ref

<!--NI_BUNDLE_CHUNK bundle=flexlogger-labview-api-ref start=1 end=37 -->
<!--NI_TOPIC bundle=flexlogger-labview-api-ref path=menus/categories/flexlogger/flexloggerautomation-mnu.html language=enus -->
## TOPIC 00001: Automation

- bundle_id: `flexlogger-labview-api-ref`
- source_path: `menus/categories/flexlogger/flexloggerautomation-mnu.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger-labview-api-ref/raw/resource/enus/menus/categories/flexlogger/flexloggerautomation-mnu.html
- document_id: `flexlogger-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the FlexLogger Automation VIs to control FlexLogger from LabVIEW icon

### Automation

Use the FlexLogger Automation VIs to control FlexLogger from LabVIEW

[IMAGE alt='icon' src='flexloggerautomation-mnu.png']

- [FlexLogger - Connect to FlexLogger VI](../../../vi-lib/flexlogger/automation/flexlogger-connect-to-flexlogger-vi.html) Connects to a FlexLogger application. If there is no instance of FlexLogger to connect to, this VI will launch an instance of FlexLogger and connect to it. The output FlexLogger launched indicates if a new instance of FlexLogger was launched. Note: This must be called before any other FlexLogger automation call since the session output from this VI is required by the other VIs.
- [FlexLogger - Open Project VI](../../../vi-lib/flexlogger/automation/flexlogger-open-project-vi.html) Loads a FlexLogger Project using the Project path passed in. If the Project path is empty, a popup dialog will allow you to browse for the Project path. Browse labels allow you to change the default labels used for this browse dialog. If a different project is currently loaded, it will be closed without saving any changes and the specified project will be loaded. If the same project is already open, it will stay loaded in its current state. Call FlexLogger - Get Test State.vi after project load is complete to check if the project is in the idle state or has configuration errors.
- [FlexLogger - Get Current Project Path VI](../../../vi-lib/flexlogger/automation/flexlogger-get-current-project-path-vi.html) Gets the path to the currently loaded FlexLogger project file (*.flxproj).
- [FlexLogger - Save VI](../../../vi-lib/flexlogger/automation/flexlogger-save-vi.html) Saves the currently loaded project. Select an instance of this polymorphic VI to see more details.
- [FlexLogger - Close Project VI](../../../vi-lib/flexlogger/automation/flexlogger-close-project-vi.html) Closes the currently loaded project and discards all unsaved changes.
- [FlexLogger - Disconnect from FlexLogger VI](../../../vi-lib/flexlogger/automation/flexlogger-disconnect-from-flexlogger-vi.html) Disconnects from a FlexLogger instance. If Close FlexLogger is true, it will also close the FlexLogger application without saving any changes. If the value is false, FlexLogger will remain running.
- [FlexLogger - Channel VI](../../../vi-lib/flexlogger/automation/flexlogger-channel-vi.html) Get or Set channel information for the currently loaded project. Select an instance of this polymorphic VI to see more details.
- [FlexLogger - Data Rate VI](../../../vi-lib/flexlogger/automation/flexlogger-data-rate-vi.html) Get or Set the Date Rate (Hz) configured for the selected Data Rate Level . Select an instance of this polymorphic VI to see more details.
- [FlexLogger - Test Properties VI](../../../vi-lib/flexlogger/automation/flexlogger-test-properties-vi.html) Get, Set, or Remove the Test properties used for the test. Select an instance of this polymorphic VI to see more details.
- [FlexLogger - Log File VI](../../../vi-lib/flexlogger/automation/flexlogger-log-file-vi.html) Get, Set, or Remove the information about the log file for the currently loaded project. Select an instance of this polymorphic VI to see more details.
- [FlexLogger - Test State VI](../../../vi-lib/flexlogger/automation/flexlogger-test-state-vi.html) Get or Set the current Test state for the FlexLogger project. Select an instance of this polymorphic VI to see more details.
- [FlexLogger - Add User Note to Log File VI](../../../vi-lib/flexlogger/automation/flexlogger-add-user-note-to-log-file-vi.html) Adds a Note to the test file. The file will also include a timestamp for when the note was added. The test state must be running for the note to be added to the file, otherwise an error is returned.

<!--NI_TOPIC bundle=flexlogger-labview-api-ref path=vi-lib/flexlogger/automation/flexlogger-add-user-note-to-log-file-vi.html language=enus -->
## TOPIC 00002: FlexLogger - Add User Note to Log File VI

- bundle_id: `flexlogger-labview-api-ref`
- source_path: `vi-lib/flexlogger/automation/flexlogger-add-user-note-to-log-file-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger-labview-api-ref/raw/resource/enus/vi-lib/flexlogger/automation/flexlogger-add-user-note-to-log-file-vi.html
- document_id: `flexlogger-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds a Note to the test file. The file will also include a timestamp for when the note was added. The test state must be running for the note to be added to the file, otherwise an error is returned. icon Inputs/Outputs cgnrn.png FlexLogger session in FlexLogger session is a reference to the currentl

### FlexLogger - Add User Note to Log File VI

Adds a **Note** to the test file. The file will also include a timestamp for when the note was added. The test state must be running for the note to be added to the file, otherwise an error is returned.

[IMAGE alt='icon' src='flexlogger-add-user-note-to-log-file-vi.png']

#### Inputs/Outputs

| FlexLogger session in — FlexLogger session is a reference to the currently running FlexLogger application. Use the Connect to FlexLogger VI to get the current session. Note — Note is the user note to add to the log file. error in (no error) — error in can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. FlexLogger session out — FlexLogger session is a reference to the currently running FlexLogger application. Use the Connect to FlexLogger VI to get the current session. error out — error out passes error or warning information out of a VI to be used by other VIs. Right-click the error out indicator on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Automation

<!--NI_TOPIC bundle=flexlogger-labview-api-ref path=vi-lib/flexlogger/automation/flexlogger-channel-vi.html language=enus -->
## TOPIC 00003: FlexLogger - Channel VI

- bundle_id: `flexlogger-labview-api-ref`
- source_path: `vi-lib/flexlogger/automation/flexlogger-channel-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger-labview-api-ref/raw/resource/enus/vi-lib/flexlogger/automation/flexlogger-channel-vi.html
- document_id: `flexlogger-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Get or Set channel information for the currently loaded project. Select an instance of this polymorphic VI to see more details. icon

### FlexLogger - Channel VI

Get or Set channel information for the currently loaded project. Select an instance of this polymorphic VI to see more details.

[IMAGE alt='icon' src='flexlogger-channel-vi.png']

- [FlexLogger - Get Channel Names VI](../../../vi-lib/flexlogger/automation/subvis/flexlogger-get-channel-names-vi.html) Get the list of Channel names for the currently loaded project. You can filter the list by configured channels, input and output channels, and analog and digital channels. By default, this VI returns all configured channels in the project.
- [FlexLogger - Get Channel Data Rate Level VI](../../../vi-lib/flexlogger/automation/subvis/flexlogger-get-channel-data-rate-level-vi.html) Get the Data rate info for the specified Channel name . The Actual data rate may differ from the Data rate associated with the Data rate level if the hardware doesn't support the specified value. Only DAQ channels support data rate information. Call the Get Channel Names instance of this VI to get a list of valid channel names.
- [FlexLogger - Get Channel Enabled VI](../../../vi-lib/flexlogger/automation/subvis/flexlogger-get-channel-enabled-vi.html) Get the Enabled state for the specified Channel name . The enabled state indicates if the channel is enabled. No data is read from disabled channels. Call the Get Channel Names instance of this VI to get a list of valid channel names.
- [FlexLogger - Get Channel Logging Enabled VI](../../../vi-lib/flexlogger/automation/subvis/flexlogger-get-channel-logging-enabled-vi.html) Get the logging state for the specified Channel name . The logging state indicates if the channel will be logged in the TDMS file. Call the Get Channel Names instance of this VI to get a list of valid channel names.
- [FlexLogger - Get Channel Value VI](../../../vi-lib/flexlogger/automation/subvis/flexlogger-get-channel-value-vi.html) Gets the Value for the specified Channel name . For digital channels, a value of 0 indicates the channel is low and 1 indicates the channel is high. Call the Get Channel Names instance of this VI to get a list of valid channel names.
- [FlexLogger - Get Channel Values VI](../../../vi-lib/flexlogger/automation/subvis/flexlogger-get-channel-values-vi.html) Gets the Values on the specified Channel names . For digital channels, a value of 0 indicates the channel is low and 1 indicates the channel is high. Call the Get Channel Names instance of this VI to get a list of valid channel names.
- [FlexLogger - Set Channel Data Rate Level VI](../../../vi-lib/flexlogger/automation/subvis/flexlogger-set-channel-data-rate-level-vi.html) Set the Data rate level for the specified Channel name . There are three options for analog input channels (Slow, Medium, Fast). Counter and Digital Input channels only support a single data rate level. The OnDemand data rate level can include static digital channels and analog output channels. Only DAQ channels support data rate levels. Call the Get Channel Names instance of this VI to get a list of valid channel names. Call the Data Rate VI to get or set the date rate for the various data rate levels.
- [FlexLogger - Set Channel Enabled VI](../../../vi-lib/flexlogger/automation/subvis/flexlogger-set-channel-enabled-vi.html) Sets the Enabled state for the specified Channel name . When a channel is disabled (i.e. enabled is False), no data is acquired from that channel. Call the Get Channel Names instance of this VI to get a list of valid channel names. Note: Not all channels support setting the enabled state.
- [FlexLogger - Set Channel Logging Enabled VI](../../../vi-lib/flexlogger/automation/subvis/flexlogger-set-channel-logging-enabled-vi.html) Sets the logging state for the specified Channel name . When logging is disabled (i.e. enabled is False), no data is logged to TDMS for that channel. Call the Get Channel Names instance of this VI to get a list of valid channel names. Note: Not all channels support setting the logging state.
- [FlexLogger - Set Channel Value VI](../../../vi-lib/flexlogger/automation/subvis/flexlogger-set-channel-value-vi.html) Sets the Value on the specified Channel name . For digital channels, specify 0 to set the channel low. Any other value will set the channel high. Call the Get Channel Names instance of this VI to get a list of valid channel names.
- [FlexLogger - Set Channel Values VI](../../../vi-lib/flexlogger/automation/subvis/flexlogger-set-channel-values-vi.html) Sets the Values on the specified Channel names . For digital channels, specify 0 to set the channel low. Any other value will set the channel high. Call the Get Channel Names instance of this VI to get a list of valid channel names.

Parent topic:

Automation

<!--NI_TOPIC bundle=flexlogger-labview-api-ref path=vi-lib/flexlogger/automation/flexlogger-close-project-vi.html language=enus -->
## TOPIC 00004: FlexLogger - Close Project VI

- bundle_id: `flexlogger-labview-api-ref`
- source_path: `vi-lib/flexlogger/automation/flexlogger-close-project-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger-labview-api-ref/raw/resource/enus/vi-lib/flexlogger/automation/flexlogger-close-project-vi.html
- document_id: `flexlogger-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Closes the currently loaded project and discards all unsaved changes. icon Inputs/Outputs cgnrn.png FlexLogger session in FlexLogger session is a reference to the currently running FlexLogger application. Use the Connect to FlexLogger VI to get the current session. cerrcodeclst.png error in (no erro

### FlexLogger - Close Project VI

Closes the currently loaded project and discards all unsaved changes.

[IMAGE alt='icon' src='flexlogger-close-project-vi.png']

#### Inputs/Outputs

| FlexLogger session in — FlexLogger session is a reference to the currently running FlexLogger application. Use the Connect to FlexLogger VI to get the current session. error in (no error) — error in can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. FlexLogger session out — FlexLogger session is a reference to the currently running FlexLogger application. Use the Connect to FlexLogger VI to get the current session. error out — error out passes error or warning information out of a VI to be used by other VIs. Right-click the error out indicator on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Automation

<!--NI_TOPIC bundle=flexlogger-labview-api-ref path=vi-lib/flexlogger/automation/flexlogger-connect-to-flexlogger-vi.html language=enus -->
## TOPIC 00005: FlexLogger - Connect to FlexLogger VI

- bundle_id: `flexlogger-labview-api-ref`
- source_path: `vi-lib/flexlogger/automation/flexlogger-connect-to-flexlogger-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger-labview-api-ref/raw/resource/enus/vi-lib/flexlogger/automation/flexlogger-connect-to-flexlogger-vi.html
- document_id: `flexlogger-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Connects to a FlexLogger application. If there is no instance of FlexLogger to connect to, this VI will launch an instance of FlexLogger and connect to it. The output FlexLogger launched indicates if a new instance of FlexLogger was launched. Note: This must be called before any other FlexLogger aut

### FlexLogger - Connect to FlexLogger VI

Connects to a FlexLogger application. If there is no instance of FlexLogger to connect to, this VI will launch an instance of FlexLogger and connect to it. The output **FlexLogger launched** indicates if a new instance of FlexLogger was launched.

Note: This must be called before any other FlexLogger automation call since the session output from this VI is required by the other VIs.

[IMAGE alt='icon' src='flexlogger-connect-to-flexlogger-vi.png']

#### Inputs/Outputs

| error in (no error) — error in can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. FlexLogger session out — FlexLogger session is a reference to the currently running FlexLogger application. You can wire this output to other FlexLogger Automation VIs. FlexLogger launched — FlexLogger launched returns TRUE if FlexLogger was launched as a result of calling this VI. If FlexLogger was already running, this returns FALSE. error out — error out passes error or warning information out of a VI to be used by other VIs. Right-click the error out indicator on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Automation

<!--NI_TOPIC bundle=flexlogger-labview-api-ref path=vi-lib/flexlogger/automation/flexlogger-data-rate-vi.html language=enus -->
## TOPIC 00006: FlexLogger - Data Rate VI

- bundle_id: `flexlogger-labview-api-ref`
- source_path: `vi-lib/flexlogger/automation/flexlogger-data-rate-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger-labview-api-ref/raw/resource/enus/vi-lib/flexlogger/automation/flexlogger-data-rate-vi.html
- document_id: `flexlogger-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Get or Set the Date Rate (Hz) configured for the selected Data Rate Level. Select an instance of this polymorphic VI to see more details. icon

### FlexLogger - Data Rate VI

Get or Set the **Date Rate (Hz)** configured for the selected **Data Rate Level**. Select an instance of this polymorphic VI to see more details.

[IMAGE alt='icon' src='flexlogger-data-rate-vi.png']

- [FlexLogger - Get Data Rate for Data Rate Level VI](../../../vi-lib/flexlogger/automation/subvis/flexlogger-get-data-rate-for-data-rate-level-vi.html) Get the Date rate (Hz) configured for the selected Data rate level . There are three data rate levels available for analog input channels (Slow, Medium, Fast), and a single data rate level for counters, and digital inputs. The OnDemand data rate level can include static digital channels and analog output channels. Note: The data rate level only applies to DAQ channels.
- [FlexLogger - Set Data Rate for Data Rate Level VI](../../../vi-lib/flexlogger/automation/subvis/flexlogger-set-data-rate-for-data-rate-level-vi.html) Sets the Data rate (Hz) for the selected Data rate level . For analog input channels, there are three available data rate levels (Slow, Medium, Fast), and for counter and digital input channels, there's a single data rate level available. The OnDemand data rate level can include static digital channels and analog output channels. Note: The data rate level only applies to DAQ channels.

Parent topic:

Automation

<!--NI_TOPIC bundle=flexlogger-labview-api-ref path=vi-lib/flexlogger/automation/flexlogger-disconnect-from-flexlogger-vi.html language=enus -->
## TOPIC 00007: FlexLogger - Disconnect from FlexLogger VI

- bundle_id: `flexlogger-labview-api-ref`
- source_path: `vi-lib/flexlogger/automation/flexlogger-disconnect-from-flexlogger-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger-labview-api-ref/raw/resource/enus/vi-lib/flexlogger/automation/flexlogger-disconnect-from-flexlogger-vi.html
- document_id: `flexlogger-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Disconnects from a FlexLogger instance. If Close FlexLogger is true, it will also close the FlexLogger application without saving any changes. If the value is false, FlexLogger will remain running. icon Inputs/Outputs cgnrn.png FlexLogger session in FlexLogger session is a reference to the currently

### FlexLogger - Disconnect from FlexLogger VI

Disconnects from a FlexLogger instance. If **Close FlexLogger** is true, it will also close the FlexLogger application without saving any changes. If the value is false, FlexLogger will remain running.

[IMAGE alt='icon' src='flexlogger-disconnect-from-flexlogger-vi.png']

#### Inputs/Outputs

| FlexLogger session in — FlexLogger session is a reference to the currently running FlexLogger application. Use the Connect to FlexLogger VI to get the current session. Close FlexLogger (T) — Close FlexLogger determines whether to close the FlexLogger application when disconnecting. Default is TRUE. error in (no error) — error in can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. error out — error out passes error or warning information out of a VI to be used by other VIs. Right-click the error out indicator on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Automation

<!--NI_TOPIC bundle=flexlogger-labview-api-ref path=vi-lib/flexlogger/automation/flexlogger-get-current-project-path-vi.html language=enus -->
## TOPIC 00008: FlexLogger - Get Current Project Path VI

- bundle_id: `flexlogger-labview-api-ref`
- source_path: `vi-lib/flexlogger/automation/flexlogger-get-current-project-path-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger-labview-api-ref/raw/resource/enus/vi-lib/flexlogger/automation/flexlogger-get-current-project-path-vi.html
- document_id: `flexlogger-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the path to the currently loaded FlexLogger project file (*.flxproj). icon Inputs/Outputs cgnrn.png FlexLogger session in FlexLogger session is a reference to the currently running FlexLogger application. Use the Connect to FlexLogger VI to get the current session. cerrcodeclst.png error in (no

### FlexLogger - Get Current Project Path VI

Gets the path to the currently loaded FlexLogger project file (*.flxproj).

[IMAGE alt='icon' src='flexlogger-get-current-project-path-vi.png']

#### Inputs/Outputs

| FlexLogger session in — FlexLogger session is a reference to the currently running FlexLogger application. Use the Connect to FlexLogger VI to get the current session. error in (no error) — error in can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. FlexLogger session out — FlexLogger session is a reference to the currently running FlexLogger application. Use the Connect to FlexLogger VI to get the current session. Project path — Project path returns the absolute path to the currently loaded project in FlexLogger. error out — error out passes error or warning information out of a VI to be used by other VIs. Right-click the error out indicator on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Automation

<!--NI_TOPIC bundle=flexlogger-labview-api-ref path=vi-lib/flexlogger/automation/flexlogger-log-file-vi.html language=enus -->
## TOPIC 00009: FlexLogger - Log File VI

- bundle_id: `flexlogger-labview-api-ref`
- source_path: `vi-lib/flexlogger/automation/flexlogger-log-file-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger-labview-api-ref/raw/resource/enus/vi-lib/flexlogger/automation/flexlogger-log-file-vi.html
- document_id: `flexlogger-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Get, Set, or Remove the information about the log file for the currently loaded project. Select an instance of this polymorphic VI to see more details. icon

### FlexLogger - Log File VI

Get, Set, or Remove the information about the log file for the currently loaded project. Select an instance of this polymorphic VI to see more details.

[IMAGE alt='icon' src='flexlogger-log-file-vi.png']

- [FlexLogger - Get Log File Info VI](../../../vi-lib/flexlogger/automation/subvis/flexlogger-get-log-file-info-vi.html) Gets the information about the log file settings for the currently loaded project. Base path , and File name can have formatters included (i.e. {Year}, {Hour}, etc.).
- [FlexLogger - Set Log File Info VI](../../../vi-lib/flexlogger/automation/subvis/flexlogger-set-log-file-info-vi.html) Sets the information about the log file settings for the currently loaded project. Base path , and File name can have formatters included (i.e. {Year}, {Hour}, etc.). Call this VI before the test has started to set the log file info that will be used when the test starts. Once the test starts, any changes to these settings will not take effect until the next test starts.
- [FlexLogger - Get Log Files from Data Files Pane VI](../../../vi-lib/flexlogger/automation/subvis/flexlogger-get-log-files-from-data-files-pane-vi.html) Get log files from the Data Files pane in the project that match the specified Log file type . The log files are sorted chronologically by their file creation times. The most recent file is at the end of the array. Use the Remove Log Files instance of this VI to remove log files from the project.
- [FlexLogger - Remove Log Files from Data Files Pane VI](../../../vi-lib/flexlogger/automation/subvis/flexlogger-remove-log-files-from-data-files-pane-vi.html) Removes all log files from the Data Files pane in the project. Set Delete files to True to also delete the log files from disk.

Parent topic:

Automation

<!--NI_TOPIC bundle=flexlogger-labview-api-ref path=vi-lib/flexlogger/automation/flexlogger-open-project-vi.html language=enus -->
## TOPIC 00010: FlexLogger - Open Project VI

- bundle_id: `flexlogger-labview-api-ref`
- source_path: `vi-lib/flexlogger/automation/flexlogger-open-project-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger-labview-api-ref/raw/resource/enus/vi-lib/flexlogger/automation/flexlogger-open-project-vi.html
- document_id: `flexlogger-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Loads a FlexLogger Project using the Project path passed in. If the Project path is empty, a popup dialog will allow you to browse for the Project path. Browse labels allow you to change the default labels used for this browse dialog. If a different project is currently loaded, it will be closed wit

### FlexLogger - Open Project VI

Loads a FlexLogger Project using the **Project path** passed in. If the Project path is empty, a popup dialog will allow you to browse for the Project path. **Browse labels** allow you to change the default labels used for this browse dialog. If a different project is currently loaded, it will be closed without saving any changes and the specified project will be loaded. If the same project is already open, it will stay loaded in its current state.

Call **FlexLogger - Get Test State.vi** after project load is complete to check if the project is in the idle state or has configuration errors.

[IMAGE alt='icon' src='flexlogger-open-project-vi.png']

#### Inputs/Outputs

| FlexLogger session in — FlexLogger session is a reference to the currently running FlexLogger application. Use the Connect to FlexLogger VI to get the current session. Project path (*.flxproj) — Project path specifies the path to the project to open. Browse labels — Browse labels defines the labels to place on the browse dialog when browsing for a project path. prompt — Custom message that appears as the title of the file dialog box. (Windows and Linux) The default dialog box title is Choose or Enter Path of File. (macOS) The default dialog box title is Select File or Create New File. pattern label — Label to display in the file dialog box next to the custom pattern. button label — Label to display on the OK or Current Directory button in the file dialog box. If you configure the Express VI to allow the user to select directories, use this input to specify a label for the Current Directory button. If the configuration does not allow the user to select directories, use this input to specify a label for the OK button. error in (no error) — error in can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. FlexLogger session out — FlexLogger session is a reference to the currently running FlexLogger application. Use the Connect to FlexLogger VI to get the current session. error out — error out passes error or warning information out of a VI to be used by other VIs. Right-click the error out indicator on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. |
| --- |
| prompt — Custom message that appears as the title of the file dialog box. (Windows and Linux) The default dialog box title is Choose or Enter Path of File. (macOS) The default dialog box title is Select File or Create New File. pattern label — Label to display in the file dialog box next to the custom pattern. button label — Label to display on the OK or Current Directory button in the file dialog box. If you configure the Express VI to allow the user to select directories, use this input to specify a label for the Current Directory button. If the configuration does not allow the user to select directories, use this input to specify a label for the OK button. |

Parent topic:

Automation

<!--NI_TOPIC bundle=flexlogger-labview-api-ref path=vi-lib/flexlogger/automation/flexlogger-save-project-as-vi.html language=enus -->
## TOPIC 00011: FlexLogger - Save Project As VI

- bundle_id: `flexlogger-labview-api-ref`
- source_path: `vi-lib/flexlogger/automation/flexlogger-save-project-as-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger-labview-api-ref/raw/resource/enus/vi-lib/flexlogger/automation/flexlogger-save-project-as-vi.html
- document_id: `flexlogger-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Saves the currently loaded project to a specified location with a given project name. icon Inputs/Outputs cgnrn.png FlexLogger session in FlexLogger session is a reference to the currently running FlexLogger application. Use the Connect to FlexLogger VI to get the current session. cstr.png Project n

### FlexLogger - Save Project As VI

Saves the currently loaded project to a specified location with a given project name.

[IMAGE alt='icon' src='flexlogger-save-project-as-vi.png']

#### Inputs/Outputs

| FlexLogger session in — FlexLogger session is a reference to the currently running FlexLogger application. Use the Connect to FlexLogger VI to get the current session. Project name — Project name is the new name for the project file and containing folder. Location — Location is the path to the parent directory where the project folder should be saved. error in (no error) — error in can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. FlexLogger session out — FlexLogger session is a reference to the currently running FlexLogger application. Use the Connect to FlexLogger VI to get the current session. error out — error out passes error or warning information out of a VI to be used by other VIs. Right-click the error out indicator on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. |
| --- |

Parent topic:

FlexLogger - Save VI

<!--NI_TOPIC bundle=flexlogger-labview-api-ref path=vi-lib/flexlogger/automation/flexlogger-save-project-vi.html language=enus -->
## TOPIC 00012: FlexLogger - Save Project VI

- bundle_id: `flexlogger-labview-api-ref`
- source_path: `vi-lib/flexlogger/automation/flexlogger-save-project-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger-labview-api-ref/raw/resource/enus/vi-lib/flexlogger/automation/flexlogger-save-project-vi.html
- document_id: `flexlogger-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Saves the currently loaded project. icon Inputs/Outputs cgnrn.png FlexLogger session in FlexLogger session is a reference to the currently running FlexLogger application. Use the Connect to FlexLogger VI to get the current session. cerrcodeclst.png error in (no error) error in can accept error infor

### FlexLogger - Save Project VI

Saves the currently loaded project.

[IMAGE alt='icon' src='flexlogger-save-project-vi.png']

#### Inputs/Outputs

| FlexLogger session in — FlexLogger session is a reference to the currently running FlexLogger application. Use the Connect to FlexLogger VI to get the current session. error in (no error) — error in can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. FlexLogger session out — FlexLogger session is a reference to the currently running FlexLogger application. Use the Connect to FlexLogger VI to get the current session. error out — error out passes error or warning information out of a VI to be used by other VIs. Right-click the error out indicator on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. |
| --- |

Parent topic:

FlexLogger - Save VI

<!--NI_TOPIC bundle=flexlogger-labview-api-ref path=vi-lib/flexlogger/automation/flexlogger-save-vi.html language=enus -->
## TOPIC 00013: FlexLogger - Save VI

- bundle_id: `flexlogger-labview-api-ref`
- source_path: `vi-lib/flexlogger/automation/flexlogger-save-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger-labview-api-ref/raw/resource/enus/vi-lib/flexlogger/automation/flexlogger-save-vi.html
- document_id: `flexlogger-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Saves the currently loaded project. Select an instance of this polymorphic VI to see more details. icon

### FlexLogger - Save VI

Saves the currently loaded project. Select an instance of this polymorphic VI to see more details.

[IMAGE alt='icon' src='flexlogger-save-vi.png']

- [FlexLogger - Save Project VI](../../../vi-lib/flexlogger/automation/flexlogger-save-project-vi.html) Saves the currently loaded project.
- [FlexLogger - Save Project As VI](../../../vi-lib/flexlogger/automation/flexlogger-save-project-as-vi.html) Saves the currently loaded project to a specified location with a given project name.

Parent topic:

Automation

<!--NI_TOPIC bundle=flexlogger-labview-api-ref path=vi-lib/flexlogger/automation/flexlogger-test-properties-vi.html language=enus -->
## TOPIC 00014: FlexLogger - Test Properties VI

- bundle_id: `flexlogger-labview-api-ref`
- source_path: `vi-lib/flexlogger/automation/flexlogger-test-properties-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger-labview-api-ref/raw/resource/enus/vi-lib/flexlogger/automation/flexlogger-test-properties-vi.html
- document_id: `flexlogger-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Get, Set, or Remove the Test properties used for the test. Select an instance of this polymorphic VI to see more details. icon

### FlexLogger - Test Properties VI

Get, Set, or Remove the **Test properties** used for the test. Select an instance of this polymorphic VI to see more details.

[IMAGE alt='icon' src='flexlogger-test-properties-vi.png']

- [FlexLogger - Get Test Properties VI](../../../vi-lib/flexlogger/automation/subvis/flexlogger-get-test-properties-vi.html) Get the Test properties used for the test. These properties are logged to the file. Any properties that have the Prompt on start flag set will cause a popup to appear at the beginning of each test to enter the specified property. An example of a test property you might want to have a popup for to enter a different value for each test might be technician name or product ID. Use the Set Test Properties instance of this VI to set these properties.
- [FlexLogger - Set Test Properties VI](../../../vi-lib/flexlogger/automation/subvis/flexlogger-set-test-properties-vi.html) Sets the Test properties to log to file when a test starts. New properties will be added or existing properties with the same Name will be updated with the new settings. To remove test properties, use the Remove Test Properties instance of this VI.
- [FlexLogger - Remove Test Properties VI](../../../vi-lib/flexlogger/automation/subvis/flexlogger-remove-test-properties-vi.html) Removes the test properties with the Test property names . Pass an empty array to remove all test properties.

Parent topic:

Automation

<!--NI_TOPIC bundle=flexlogger-labview-api-ref path=vi-lib/flexlogger/automation/flexlogger-test-state-vi.html language=enus -->
## TOPIC 00015: FlexLogger - Test State VI

- bundle_id: `flexlogger-labview-api-ref`
- source_path: `vi-lib/flexlogger/automation/flexlogger-test-state-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger-labview-api-ref/raw/resource/enus/vi-lib/flexlogger/automation/flexlogger-test-state-vi.html
- document_id: `flexlogger-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Get or Set the current Test state for the FlexLogger project. Select an instance of this polymorphic VI to see more details. icon

### FlexLogger - Test State VI

Get or Set the current **Test state** for the FlexLogger project. Select an instance of this polymorphic VI to see more details.

[IMAGE alt='icon' src='flexlogger-test-state-vi.png']

- [FlexLogger - Get Test State VI](../../../vi-lib/flexlogger/automation/subvis/flexlogger-get-test-state-vi.html) Get the current Test state and Test time (seconds) for the FlexLogger project. The Test time starts counting from 0 when the test starts and stops updating when the test is paused or stopped. If a test is stopped, the time will indicate the test time of the last test until a new test is started.
- [FlexLogger - Set Test State VI](../../../vi-lib/flexlogger/automation/subvis/flexlogger-set-test-state-vi.html) Sets the Test state to control when a test starts, stops, pauses, and resumes. If the current state of the test doesn't support the requested test state (i.e. current state is idle and Test state is Pause), an error will be returneds. Use the Get Test State instance of this VI to determine the current test state.

Parent topic:

Automation

<!--NI_TOPIC bundle=flexlogger-labview-api-ref path=vi-lib/flexlogger/automation/subvis/flexlogger-get-channel-data-rate-level-vi.html language=enus -->
## TOPIC 00016: FlexLogger - Get Channel Data Rate Level VI

- bundle_id: `flexlogger-labview-api-ref`
- source_path: `vi-lib/flexlogger/automation/subvis/flexlogger-get-channel-data-rate-level-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger-labview-api-ref/raw/resource/enus/vi-lib/flexlogger/automation/subvis/flexlogger-get-channel-data-rate-level-vi.html
- document_id: `flexlogger-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Get the Data rate info for the specified Channel name. The Actual data rate may differ from the Data rate associated with the Data rate level if the hardware doesn't support the specified value. Only DAQ channels support data rate information. Call the Get Channel Names instance of this VI to get a

### FlexLogger - Get Channel Data Rate Level VI

Get the **Data rate info** for the specified **Channel name**. The **Actual data rate** may differ from the **Data rate** associated with the **Data rate level** if the hardware doesn't support the specified value. 

Only DAQ channels support data rate information.

Call the **Get Channel Names** instance of this VI to get a list of valid channel names.

[IMAGE alt='icon' src='flexlogger-get-channel-data-rate-level-vi.png']

#### Inputs/Outputs

| FlexLogger session in — FlexLogger session is a reference to the currently running FlexLogger application. Use the Connect to FlexLogger VI to get the current session. Channel name — Channel name is the name of the channel to query. error in (no error) — error in can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. FlexLogger session out — FlexLogger session is a reference to the currently running FlexLogger application. Use the Connect to FlexLogger VI to get the current session. Data rate info — Data rate info contains information about the Data Rate Level in FlexLogger. Data rate level — Data rate level specifies the data rate level for a channel in FlexLogger. Valid values are: Analog - Slow - for analog channels on the slow data rate level. Analog - Medium - for analog channels on the medium data rate level. Analog - Fast - for analog channels on the fast data rate level. Counter - for counter channels. Digital - for digital channels. OnDemand - for software timed channels. This can include software timed digital channels and analog output channels. Data rate — Data rate specifies the user requested data rate for the channel. Actual data rate — Actual data rate specifies the actual data rate this channel is acquiring at. error out — error out passes error or warning information out of a VI to be used by other VIs. Right-click the error out indicator on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. |
| --- |
| Data rate level — Data rate level specifies the data rate level for a channel in FlexLogger. Valid values are: Analog - Slow - for analog channels on the slow data rate level. Analog - Medium - for analog channels on the medium data rate level. Analog - Fast - for analog channels on the fast data rate level. Counter - for counter channels. Digital - for digital channels. OnDemand - for software timed channels. This can include software timed digital channels and analog output channels. Data rate — Data rate specifies the user requested data rate for the channel. Actual data rate — Actual data rate specifies the actual data rate this channel is acquiring at. |

Parent topic:

FlexLogger - Channel VI

<!--NI_TOPIC bundle=flexlogger-labview-api-ref path=vi-lib/flexlogger/automation/subvis/flexlogger-get-channel-enabled-vi.html language=enus -->
## TOPIC 00017: FlexLogger - Get Channel Enabled VI

- bundle_id: `flexlogger-labview-api-ref`
- source_path: `vi-lib/flexlogger/automation/subvis/flexlogger-get-channel-enabled-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger-labview-api-ref/raw/resource/enus/vi-lib/flexlogger/automation/subvis/flexlogger-get-channel-enabled-vi.html
- document_id: `flexlogger-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Get the Enabled state for the specified Channel name. The enabled state indicates if the channel is enabled. No data is read from disabled channels. Call the Get Channel Names instance of this VI to get a list of valid channel names. icon Inputs/Outputs cgnrn.png FlexLogger session in FlexLogger ses

### FlexLogger - Get Channel Enabled VI

Get the **Enabled** state for the specified **Channel name**. The enabled state indicates if the channel is enabled. No data is read from disabled channels.

Call the **Get Channel Names** instance of this VI to get a list of valid channel names.

[IMAGE alt='icon' src='flexlogger-get-channel-enabled-vi.png']

#### Inputs/Outputs

| FlexLogger session in — FlexLogger session is a reference to the currently running FlexLogger application. Use the Connect to FlexLogger VI to get the current session. Channel name — Channel name is the name of the channel to query. error in (no error) — error in can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. FlexLogger session out — FlexLogger session is a reference to the currently running FlexLogger application. Use the Connect to FlexLogger VI to get the current session. Enabled — Enabled specifies whether or not this channel is enabled. error out — error out passes error or warning information out of a VI to be used by other VIs. Right-click the error out indicator on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. |
| --- |

Parent topic:

FlexLogger - Channel VI

<!--NI_TOPIC bundle=flexlogger-labview-api-ref path=vi-lib/flexlogger/automation/subvis/flexlogger-get-channel-logging-enabled-vi.html language=enus -->
## TOPIC 00018: FlexLogger - Get Channel Logging Enabled VI

- bundle_id: `flexlogger-labview-api-ref`
- source_path: `vi-lib/flexlogger/automation/subvis/flexlogger-get-channel-logging-enabled-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger-labview-api-ref/raw/resource/enus/vi-lib/flexlogger/automation/subvis/flexlogger-get-channel-logging-enabled-vi.html
- document_id: `flexlogger-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Get the logging state for the specified Channel name. The logging state indicates if the channel will be logged in the TDMS file. Call the Get Channel Names instance of this VI to get a list of valid channel names. icon Inputs/Outputs cgnrn.png FlexLogger session in FlexLogger session is a reference

### FlexLogger - Get Channel Logging Enabled VI

Get the logging state for the specified **Channel name**. The logging state indicates if the channel will be logged in the TDMS file.

Call the **Get Channel Names** instance of this VI to get a list of valid channel names.

[IMAGE alt='icon' src='flexlogger-get-channel-logging-enabled-vi.png']

#### Inputs/Outputs

| FlexLogger session in — FlexLogger session is a reference to the currently running FlexLogger application. Use the Connect to FlexLogger VI to get the current session. Channel name — Channel name is the name of the channel to query. error in (no error) — error in can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. FlexLogger session out — FlexLogger session is a reference to the currently running FlexLogger application. Use the Connect to FlexLogger VI to get the current session. Logging Enabled — Enabled specifies whether or not this channel is enabled. error out — error out passes error or warning information out of a VI to be used by other VIs. Right-click the error out indicator on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. |
| --- |

Parent topic:

FlexLogger - Channel VI

<!--NI_TOPIC bundle=flexlogger-labview-api-ref path=vi-lib/flexlogger/automation/subvis/flexlogger-get-channel-names-vi.html language=enus -->
## TOPIC 00019: FlexLogger - Get Channel Names VI

- bundle_id: `flexlogger-labview-api-ref`
- source_path: `vi-lib/flexlogger/automation/subvis/flexlogger-get-channel-names-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger-labview-api-ref/raw/resource/enus/vi-lib/flexlogger/automation/subvis/flexlogger-get-channel-names-vi.html
- document_id: `flexlogger-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Get the list of Channel names for the currently loaded project. You can filter the list by configured channels, input and output channels, and analog and digital channels. By default, this VI returns all configured channels in the project. icon Inputs/Outputs cgnrn.png FlexLogger session in FlexLogg

### FlexLogger - Get Channel Names VI

Get the list of **Channel names** for the currently loaded project. You can filter the list by configured channels, input and output channels, and analog and digital channels. By default, this VI returns all configured channels in the project.

[IMAGE alt='icon' src='flexlogger-get-channel-names-vi.png']

#### Inputs/Outputs

| FlexLogger session in — FlexLogger session is a reference to the currently running FlexLogger application. Use the Connect to FlexLogger VI to get the current session. Channel name filter — Channel name filter defines what channel types to include when querying channel names. Configured Channels — Configured Channels specifies whether to only return configured channels in the Channels names array. Set this to TRUE to only return configured channels. If this is FALSE, the Channels names array will contain both configued and unconfigured channel names. Input Channels — Input Channels specifies whether to return input channels in the Channels names array. Set this to TRUE to include input channels. If this is FALSE, the Channels names array will not contain input channels names. Output Channels — Output Channels specifies whether to return output channels in the Channels names array. Set this to TRUE to include output channels. If this is FALSE, the Channels names array will not contain output channels names. Analog Channels — Analog Channels specifies whether to return analog channels in the Channels names array. Set this to TRUE to include analog channels. If this is FALSE, the Channels names array will not contain analog channels. Digital Channels — Digital Channels specifies whether to return digital channels in the Channels names array. Set this to TRUE to include digital channels. If this is FALSE, the Channels names array will not contain digital channels. error in (no error) — error in can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. FlexLogger session out — FlexLogger session is a reference to the currently running FlexLogger application. Use the Connect to FlexLogger VI to get the current session. Channel names — Channel names is an array of channel names in FlexLogger's Channel Specification. This array can be filtered using the Channel name filter. error out — error out passes error or warning information out of a VI to be used by other VIs. Right-click the error out indicator on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. |
| --- |
| Configured Channels — Configured Channels specifies whether to only return configured channels in the Channels names array. Set this to TRUE to only return configured channels. If this is FALSE, the Channels names array will contain both configued and unconfigured channel names. Input Channels — Input Channels specifies whether to return input channels in the Channels names array. Set this to TRUE to include input channels. If this is FALSE, the Channels names array will not contain input channels names. Output Channels — Output Channels specifies whether to return output channels in the Channels names array. Set this to TRUE to include output channels. If this is FALSE, the Channels names array will not contain output channels names. Analog Channels — Analog Channels specifies whether to return analog channels in the Channels names array. Set this to TRUE to include analog channels. If this is FALSE, the Channels names array will not contain analog channels. Digital Channels — Digital Channels specifies whether to return digital channels in the Channels names array. Set this to TRUE to include digital channels. If this is FALSE, the Channels names array will not contain digital channels. |

Parent topic:

FlexLogger - Channel VI

<!--NI_TOPIC bundle=flexlogger-labview-api-ref path=vi-lib/flexlogger/automation/subvis/flexlogger-get-channel-value-vi.html language=enus -->
## TOPIC 00020: FlexLogger - Get Channel Value VI

- bundle_id: `flexlogger-labview-api-ref`
- source_path: `vi-lib/flexlogger/automation/subvis/flexlogger-get-channel-value-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger-labview-api-ref/raw/resource/enus/vi-lib/flexlogger/automation/subvis/flexlogger-get-channel-value-vi.html
- document_id: `flexlogger-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the Value for the specified Channel name. For digital channels, a value of 0 indicates the channel is low and 1 indicates the channel is high. Call the Get Channel Names instance of this VI to get a list of valid channel names. icon Inputs/Outputs cgnrn.png FlexLogger session in FlexLogger sess

### FlexLogger - Get Channel Value VI

Gets the **Value** for the specified **Channel name**. For digital channels, a value of 0 indicates the channel is low and 1 indicates the channel is high.

Call the **Get Channel Names** instance of this VI to get a list of valid channel names.

[IMAGE alt='icon' src='flexlogger-get-channel-value-vi.png']

#### Inputs/Outputs

| FlexLogger session in — FlexLogger session is a reference to the currently running FlexLogger application. Use the Connect to FlexLogger VI to get the current session. Channel name — Channel name is the name of the channel to query. error in (no error) — error in can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. FlexLogger session out — FlexLogger session is a reference to the currently running FlexLogger application. Use the Connect to FlexLogger VI to get the current session. Value — Value returns the current value on the channel. For Digital channels, the value will be 0 for low and 1 for high. Time stamp — Time stamp is the time at which the value on the channel was read. error out — error out passes error or warning information out of a VI to be used by other VIs. Right-click the error out indicator on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. |
| --- |

Parent topic:

FlexLogger - Channel VI

<!--NI_TOPIC bundle=flexlogger-labview-api-ref path=vi-lib/flexlogger/automation/subvis/flexlogger-get-channel-values-vi.html language=enus -->
## TOPIC 00021: FlexLogger - Get Channel Values VI

- bundle_id: `flexlogger-labview-api-ref`
- source_path: `vi-lib/flexlogger/automation/subvis/flexlogger-get-channel-values-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger-labview-api-ref/raw/resource/enus/vi-lib/flexlogger/automation/subvis/flexlogger-get-channel-values-vi.html
- document_id: `flexlogger-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the Values on the specified Channel names. For digital channels, a value of 0 indicates the channel is low and 1 indicates the channel is high. Call the Get Channel Names instance of this VI to get a list of valid channel names. icon Inputs/Outputs cgnrn.png FlexLogger session in FlexLogger ses

### FlexLogger - Get Channel Values VI

Gets the **Values** on the specified **Channel names**. For digital channels, a value of 0 indicates the channel is low and 1 indicates the channel is high.

Call the **Get Channel Names** instance of this VI to get a list of valid channel names.

[IMAGE alt='icon' src='flexlogger-get-channel-values-vi.png']

#### Inputs/Outputs

| FlexLogger session in — FlexLogger session is a reference to the currently running FlexLogger application. Use the Connect to FlexLogger VI to get the current session. Channel names — Channel names is the array of channels to get values for. error in (no error) — error in can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. FlexLogger session out — FlexLogger session is a reference to the currently running FlexLogger application. Use the Connect to FlexLogger VI to get the current session. Values — Values is an array of channel values for each channel in the Channel names input control. Time stamps — Time stamps is an array of time stamps corresponding to the Values returned by this VI. error out — error out passes error or warning information out of a VI to be used by other VIs. Right-click the error out indicator on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. |
| --- |

Parent topic:

FlexLogger - Channel VI

<!--NI_TOPIC bundle=flexlogger-labview-api-ref path=vi-lib/flexlogger/automation/subvis/flexlogger-get-data-rate-for-data-rate-level-vi.html language=enus -->
## TOPIC 00022: FlexLogger - Get Data Rate for Data Rate Level VI

- bundle_id: `flexlogger-labview-api-ref`
- source_path: `vi-lib/flexlogger/automation/subvis/flexlogger-get-data-rate-for-data-rate-level-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger-labview-api-ref/raw/resource/enus/vi-lib/flexlogger/automation/subvis/flexlogger-get-data-rate-for-data-rate-level-vi.html
- document_id: `flexlogger-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Get the Date rate (Hz) configured for the selected Data rate level. There are three data rate levels available for analog input channels (Slow, Medium, Fast), and a single data rate level for counters, and digital inputs. The OnDemand data rate level can include static digital channels and analog ou

### FlexLogger - Get Data Rate for Data Rate Level VI

Get the **Date rate (Hz)** configured for the selected **Data rate level**. There are three data rate levels available for analog input channels (Slow, Medium, Fast), and a single data rate level for counters, and digital inputs. The OnDemand data rate level can include static digital channels and analog output channels.

Note: The data rate level only applies to DAQ channels.

[IMAGE alt='icon' src='flexlogger-get-data-rate-for-data-rate-level-vi.png']

#### Inputs/Outputs

| FlexLogger session in — FlexLogger session is a reference to the currently running FlexLogger application. Use the Connect to FlexLogger VI to get the current session. Data rate level — Data rate level specifies the data rate level for a channel in FlexLogger. Valid values are: Analog - Slow - for analog channels on the slow data rate level. Analog - Medium - for analog channels on the medium data rate level. Analog - Fast - for analog channels on the fast data rate level. Counter - for counter channels. Digital - for digital channels. OnDemand - for software timed channels. This can include software timed digital channels and analog output channels. error in (no error) — error in can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. FlexLogger session out — FlexLogger session is a reference to the currently running FlexLogger application. Use the Connect to FlexLogger VI to get the current session. Data rate (Hz) — Data rate (Hz) returns the data rate in hertz for the requested Data rate level. error out — error out passes error or warning information out of a VI to be used by other VIs. Right-click the error out indicator on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. |
| --- |

Parent topic:

FlexLogger - Data Rate VI

<!--NI_TOPIC bundle=flexlogger-labview-api-ref path=vi-lib/flexlogger/automation/subvis/flexlogger-get-log-file-info-vi.html language=enus -->
## TOPIC 00023: FlexLogger - Get Log File Info VI

- bundle_id: `flexlogger-labview-api-ref`
- source_path: `vi-lib/flexlogger/automation/subvis/flexlogger-get-log-file-info-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger-labview-api-ref/raw/resource/enus/vi-lib/flexlogger/automation/subvis/flexlogger-get-log-file-info-vi.html
- document_id: `flexlogger-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the information about the log file settings for the currently loaded project. Base path, and File name can have formatters included (i.e. {Year}, {Hour}, etc.). icon Inputs/Outputs cgnrn.png FlexLogger session in FlexLogger session is a reference to the currently running FlexLogger application.

### FlexLogger - Get Log File Info VI

Gets the information about the log file settings for the currently loaded project. **Base path**, and **File name** can have formatters included (i.e. {Year}, {Hour}, etc.).

[IMAGE alt='icon' src='flexlogger-get-log-file-info-vi.png']

#### Inputs/Outputs

| FlexLogger session in — FlexLogger session is a reference to the currently running FlexLogger application. Use the Connect to FlexLogger VI to get the current session. error in (no error) — error in can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. FlexLogger session out — FlexLogger session is a reference to the currently running FlexLogger application. Use the Connect to FlexLogger VI to get the current session. Base path — Base path is the base path of the log file specified in FlexLogger's Logging Specification. File name — File name is the name of the log file. error out — error out passes error or warning information out of a VI to be used by other VIs. Right-click the error out indicator on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. File description — File description is the description of the log file. |
| --- |

Parent topic:

FlexLogger - Log File VI

<!--NI_TOPIC bundle=flexlogger-labview-api-ref path=vi-lib/flexlogger/automation/subvis/flexlogger-get-log-files-from-data-files-pane-vi.html language=enus -->
## TOPIC 00024: FlexLogger - Get Log Files from Data Files Pane VI

- bundle_id: `flexlogger-labview-api-ref`
- source_path: `vi-lib/flexlogger/automation/subvis/flexlogger-get-log-files-from-data-files-pane-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger-labview-api-ref/raw/resource/enus/vi-lib/flexlogger/automation/subvis/flexlogger-get-log-files-from-data-files-pane-vi.html
- document_id: `flexlogger-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Get log files from the Data Files pane in the project that match the specified Log file type. The log files are sorted chronologically by their file creation times. The most recent file is at the end of the array. Use the Remove Log Files instance of this VI to remove log files from the project. ico

### FlexLogger - Get Log Files from Data Files Pane VI

Get log files from the Data Files pane in the project that match the specified **Log file type**. The log files are sorted chronologically by their file creation times. The most recent file is at the end of the array.

Use the **Remove Log Files** instance of this VI to remove log files from the project.

[IMAGE alt='icon' src='flexlogger-get-log-files-from-data-files-pane-vi.png']

#### Inputs/Outputs

| FlexLogger session in — FlexLogger session is a reference to the currently running FlexLogger application. Use the Connect to FlexLogger VI to get the current session. Log file type (TDMS) — Log file type is the type of log file. Valid values are: TDMS, TDMS backup file, or CVS error in (no error) — error in can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. FlexLogger session out — FlexLogger session is a reference to the currently running FlexLogger application. Use the Connect to FlexLogger VI to get the current session. Log files — Log files is an array of all the logged files matching the requested Log file type for the currently loaded project in FlexLogger. error out — error out passes error or warning information out of a VI to be used by other VIs. Right-click the error out indicator on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. |
| --- |

Parent topic:

FlexLogger - Log File VI

<!--NI_TOPIC bundle=flexlogger-labview-api-ref path=vi-lib/flexlogger/automation/subvis/flexlogger-get-test-properties-vi.html language=enus -->
## TOPIC 00025: FlexLogger - Get Test Properties VI

- bundle_id: `flexlogger-labview-api-ref`
- source_path: `vi-lib/flexlogger/automation/subvis/flexlogger-get-test-properties-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger-labview-api-ref/raw/resource/enus/vi-lib/flexlogger/automation/subvis/flexlogger-get-test-properties-vi.html
- document_id: `flexlogger-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Get the Test properties used for the test. These properties are logged to the file. Any properties that have the Prompt on start flag set will cause a popup to appear at the beginning of each test to enter the specified property. An example of a test property you might want to have a popup for to en

### FlexLogger - Get Test Properties VI

Get the **Test properties** used for the test. These properties are logged to the file. Any properties that have the **Prompt on start** flag set will cause a popup to appear at the beginning of each test to enter the specified property. An example of a test property you might want to have a popup for to enter a different value for each test might be technician name or product ID.

Use the **Set Test Properties** instance of this VI to set these properties.

[IMAGE alt='icon' src='flexlogger-get-test-properties-vi.png']

#### Inputs/Outputs

| FlexLogger session in — FlexLogger session is a reference to the currently running FlexLogger application. Use the Connect to FlexLogger VI to get the current session. error in (no error) — error in can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. FlexLogger session out — FlexLogger session is a reference to the currently running FlexLogger application. Use the Connect to FlexLogger VI to get the current session. Test properties — Test properties is an array of properties for the current test. Name — Name is the name of the property. Value — Value is the value of the test property. Prompt on start — Prompt on start specifies whether to prompt the user for the value of the property when the test is started. error out — error out passes error or warning information out of a VI to be used by other VIs. Right-click the error out indicator on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. |
| --- |
| Name — Name is the name of the property. Value — Value is the value of the test property. Prompt on start — Prompt on start specifies whether to prompt the user for the value of the property when the test is started. |

Parent topic:

FlexLogger - Test Properties VI

<!--NI_TOPIC bundle=flexlogger-labview-api-ref path=vi-lib/flexlogger/automation/subvis/flexlogger-get-test-state-vi.html language=enus -->
## TOPIC 00026: FlexLogger - Get Test State VI

- bundle_id: `flexlogger-labview-api-ref`
- source_path: `vi-lib/flexlogger/automation/subvis/flexlogger-get-test-state-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger-labview-api-ref/raw/resource/enus/vi-lib/flexlogger/automation/subvis/flexlogger-get-test-state-vi.html
- document_id: `flexlogger-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Get the current Test state and Test time (seconds) for the FlexLogger project. The Test time starts counting from 0 when the test starts and stops updating when the test is paused or stopped. If a test is stopped, the time will indicate the test time of the last test until a new test is started. ico

### FlexLogger - Get Test State VI

Get the current **Test state** and **Test time (seconds)** for the FlexLogger project. The **Test time** starts counting from 0 when the test starts and stops updating when the test is paused or stopped. If a test is stopped, the time will indicate the test time of the last test until a new test is started.

[IMAGE alt='icon' src='flexlogger-get-test-state-vi.png']

#### Inputs/Outputs

| FlexLogger session in — FlexLogger session is a reference to the currently running FlexLogger application. Use the Connect to FlexLogger VI to get the current session. error in (no error) — error in can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. FlexLogger session out — FlexLogger session is a reference to the currently running FlexLogger application. Use the Connect to FlexLogger VI to get the current session. Test state — Test state specifies the current state of the test in FlexLogger. Valid values are: Idle - Channels have finished configuring, test is ready to run. Running - Test is running. Paused - Test is paused. Invalid configuration - the current configuration is not valid. Not configured - no channels that support logging are configured. Test time (seconds) — Test time is the current running time of the test in seconds. error out — error out passes error or warning information out of a VI to be used by other VIs. Right-click the error out indicator on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. |
| --- |

Parent topic:

FlexLogger - Test State VI

<!--NI_TOPIC bundle=flexlogger-labview-api-ref path=vi-lib/flexlogger/automation/subvis/flexlogger-remove-log-files-from-data-files-pane-vi.html language=enus -->
## TOPIC 00027: FlexLogger - Remove Log Files from Data Files Pane VI

- bundle_id: `flexlogger-labview-api-ref`
- source_path: `vi-lib/flexlogger/automation/subvis/flexlogger-remove-log-files-from-data-files-pane-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger-labview-api-ref/raw/resource/enus/vi-lib/flexlogger/automation/subvis/flexlogger-remove-log-files-from-data-files-pane-vi.html
- document_id: `flexlogger-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Removes all log files from the Data Files pane in the project. Set Delete files to True to also delete the log files from disk. icon Inputs/Outputs cgnrn.png FlexLogger session in FlexLogger session is a reference to the currently running FlexLogger application. Use the Connect to FlexLogger VI to g

### FlexLogger - Remove Log Files from Data Files Pane VI

Removes all log files from the Data Files pane in the project. Set **Delete files** to True to also delete the log files from disk.

[IMAGE alt='icon' src='flexlogger-remove-log-files-from-data-files-pane-vi.png']

#### Inputs/Outputs

| FlexLogger session in — FlexLogger session is a reference to the currently running FlexLogger application. Use the Connect to FlexLogger VI to get the current session. — Delete files specifies whether to also delete the log files from disk. error in (no error) — error in can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. FlexLogger session out — FlexLogger session is a reference to the currently running FlexLogger application. Use the Connect to FlexLogger VI to get the current session. error out — error out passes error or warning information out of a VI to be used by other VIs. Right-click the error out indicator on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. |
| --- |

Parent topic:

FlexLogger - Log File VI

<!--NI_TOPIC bundle=flexlogger-labview-api-ref path=vi-lib/flexlogger/automation/subvis/flexlogger-remove-test-properties-vi.html language=enus -->
## TOPIC 00028: FlexLogger - Remove Test Properties VI

- bundle_id: `flexlogger-labview-api-ref`
- source_path: `vi-lib/flexlogger/automation/subvis/flexlogger-remove-test-properties-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger-labview-api-ref/raw/resource/enus/vi-lib/flexlogger/automation/subvis/flexlogger-remove-test-properties-vi.html
- document_id: `flexlogger-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Removes the test properties with the Test property names. Pass an empty array to remove all test properties. icon Inputs/Outputs cgnrn.png FlexLogger session in FlexLogger session is a reference to the currently running FlexLogger application. Use the Connect to FlexLogger VI to get the current sess

### FlexLogger - Remove Test Properties VI

Removes the test properties with the **Test property names**. Pass an empty array to remove all test properties.

[IMAGE alt='icon' src='flexlogger-remove-test-properties-vi.png']

#### Inputs/Outputs

| FlexLogger session in — FlexLogger session is a reference to the currently running FlexLogger application. Use the Connect to FlexLogger VI to get the current session. Test property names (all) — Test property names is an array of property names to remove. error in (no error) — error in can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. FlexLogger session out — FlexLogger session is a reference to the currently running FlexLogger application. Use the Connect to FlexLogger VI to get the current session. error out — error out passes error or warning information out of a VI to be used by other VIs. Right-click the error out indicator on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. |
| --- |

Parent topic:

FlexLogger - Test Properties VI

<!--NI_TOPIC bundle=flexlogger-labview-api-ref path=vi-lib/flexlogger/automation/subvis/flexlogger-set-channel-data-rate-level-vi.html language=enus -->
## TOPIC 00029: FlexLogger - Set Channel Data Rate Level VI

- bundle_id: `flexlogger-labview-api-ref`
- source_path: `vi-lib/flexlogger/automation/subvis/flexlogger-set-channel-data-rate-level-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger-labview-api-ref/raw/resource/enus/vi-lib/flexlogger/automation/subvis/flexlogger-set-channel-data-rate-level-vi.html
- document_id: `flexlogger-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Set the Data rate level for the specified Channel name. There are three options for analog input channels (Slow, Medium, Fast). Counter and Digital Input channels only support a single data rate level. The OnDemand data rate level can include static digital channels and analog output channels. Only

### FlexLogger - Set Channel Data Rate Level VI

Set the **Data rate level** for the specified **Channel name**. There are three options for analog input channels (Slow, Medium, Fast). Counter and Digital Input channels only support a single data rate level. The OnDemand data rate level can include static digital channels and analog output channels.

Only DAQ channels support data rate levels.

Call the **Get Channel Names** instance of this VI to get a list of valid channel names.
Call the **Data Rate VI** to get or set the date rate for the various data rate levels.

[IMAGE alt='icon' src='flexlogger-set-channel-data-rate-level-vi.png']

#### Inputs/Outputs

| FlexLogger session in — FlexLogger session is a reference to the currently running FlexLogger application. Use the Connect to FlexLogger VI to get the current session. Channel name — Channel name is the name of the channel to update. Data rate level — Data rate level specifies the data rate level for a channel in FlexLogger. Valid values are: Analog - Slow - for analog channels on the slow data rate level. Analog - Medium - for analog channels on the medium data rate level. Analog - Fast - for analog channels on the fast data rate level. Counter - for counter channels. Digital - for digital channels. OnDemand - for software timed channels. This can include software timed digital channels and analog output channels. error in (no error) — error in can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. FlexLogger session out — FlexLogger session is a reference to the currently running FlexLogger application. Use the Connect to FlexLogger VI to get the current session. error out — error out passes error or warning information out of a VI to be used by other VIs. Right-click the error out indicator on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. |
| --- |

Parent topic:

FlexLogger - Channel VI

<!--NI_TOPIC bundle=flexlogger-labview-api-ref path=vi-lib/flexlogger/automation/subvis/flexlogger-set-channel-enabled-vi.html language=enus -->
## TOPIC 00030: FlexLogger - Set Channel Enabled VI

- bundle_id: `flexlogger-labview-api-ref`
- source_path: `vi-lib/flexlogger/automation/subvis/flexlogger-set-channel-enabled-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger-labview-api-ref/raw/resource/enus/vi-lib/flexlogger/automation/subvis/flexlogger-set-channel-enabled-vi.html
- document_id: `flexlogger-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the Enabled state for the specified Channel name. When a channel is disabled (i.e. enabled is False), no data is acquired from that channel. Call the Get Channel Names instance of this VI to get a list of valid channel names. Note: Not all channels support setting the enabled state. icon Inputs

### FlexLogger - Set Channel Enabled VI

Sets the **Enabled** state for the specified **Channel name**. When a channel is disabled (i.e. enabled is False), no data is acquired from that channel.

Call the **Get Channel Names** instance of this VI to get a list of valid channel names.

Note: Not all channels support setting the enabled state.

[IMAGE alt='icon' src='flexlogger-set-channel-enabled-vi.png']

#### Inputs/Outputs

| FlexLogger session in — FlexLogger session is a reference to the currently running FlexLogger application. Use the Connect to FlexLogger VI to get the current session. Channel name — Channel name is the name of the channel to update. Enabled (T) — Enabled specifies whether or not this channel is enabled. error in (no error) — error in can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. FlexLogger session out — FlexLogger session is a reference to the currently running FlexLogger application. Use the Connect to FlexLogger VI to get the current session. error out — error out passes error or warning information out of a VI to be used by other VIs. Right-click the error out indicator on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. |
| --- |

Parent topic:

FlexLogger - Channel VI

<!--NI_TOPIC bundle=flexlogger-labview-api-ref path=vi-lib/flexlogger/automation/subvis/flexlogger-set-channel-logging-enabled-vi.html language=enus -->
## TOPIC 00031: FlexLogger - Set Channel Logging Enabled VI

- bundle_id: `flexlogger-labview-api-ref`
- source_path: `vi-lib/flexlogger/automation/subvis/flexlogger-set-channel-logging-enabled-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger-labview-api-ref/raw/resource/enus/vi-lib/flexlogger/automation/subvis/flexlogger-set-channel-logging-enabled-vi.html
- document_id: `flexlogger-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the logging state for the specified Channel name. When logging is disabled (i.e. enabled is False), no data is logged to TDMS for that channel. Call the Get Channel Names instance of this VI to get a list of valid channel names. Note: Not all channels support setting the logging state. icon Inp

### FlexLogger - Set Channel Logging Enabled VI

Sets the logging state for the specified **Channel name**. When logging is disabled (i.e. enabled is False), no data is logged to TDMS for that channel.

Call the **Get Channel Names** instance of this VI to get a list of valid channel names.

Note: Not all channels support setting the logging state.

[IMAGE alt='icon' src='flexlogger-set-channel-logging-enabled-vi.png']

#### Inputs/Outputs

| FlexLogger session in — FlexLogger session is a reference to the currently running FlexLogger application. Use the Connect to FlexLogger VI to get the current session. Channel name — Channel name is the name of the channel to update. Enabled (T) — Enabled specifies whether or not this channel is enabled. error in (no error) — error in can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. FlexLogger session out — FlexLogger session is a reference to the currently running FlexLogger application. Use the Connect to FlexLogger VI to get the current session. error out — error out passes error or warning information out of a VI to be used by other VIs. Right-click the error out indicator on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. |
| --- |

Parent topic:

FlexLogger - Channel VI

<!--NI_TOPIC bundle=flexlogger-labview-api-ref path=vi-lib/flexlogger/automation/subvis/flexlogger-set-channel-value-vi.html language=enus -->
## TOPIC 00032: FlexLogger - Set Channel Value VI

- bundle_id: `flexlogger-labview-api-ref`
- source_path: `vi-lib/flexlogger/automation/subvis/flexlogger-set-channel-value-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger-labview-api-ref/raw/resource/enus/vi-lib/flexlogger/automation/subvis/flexlogger-set-channel-value-vi.html
- document_id: `flexlogger-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the Value on the specified Channel name. For digital channels, specify 0 to set the channel low. Any other value will set the channel high. Call the Get Channel Names instance of this VI to get a list of valid channel names. icon Inputs/Outputs cgnrn.png FlexLogger session in FlexLogger session

### FlexLogger - Set Channel Value VI

Sets the **Value** on the specified **Channel name**. For digital channels, specify 0 to set the channel low. Any other value will set the channel high.

Call the **Get Channel Names** instance of this VI to get a list of valid channel names.

[IMAGE alt='icon' src='flexlogger-set-channel-value-vi.png']

#### Inputs/Outputs

| FlexLogger session in — FlexLogger session is a reference to the currently running FlexLogger application. Use the Connect to FlexLogger VI to get the current session. Channel name — Channel name is the name of the channel to update. Value — Value is value to set on the channel. For Digital channels use 0 to set the channel low and any other value to set the channel high. error in (no error) — error in can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. FlexLogger session out — FlexLogger session is a reference to the currently running FlexLogger application. Use the Connect to FlexLogger VI to get the current session. error out — error out passes error or warning information out of a VI to be used by other VIs. Right-click the error out indicator on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. |
| --- |

Parent topic:

FlexLogger - Channel VI

<!--NI_TOPIC bundle=flexlogger-labview-api-ref path=vi-lib/flexlogger/automation/subvis/flexlogger-set-channel-values-vi.html language=enus -->
## TOPIC 00033: FlexLogger - Set Channel Values VI

- bundle_id: `flexlogger-labview-api-ref`
- source_path: `vi-lib/flexlogger/automation/subvis/flexlogger-set-channel-values-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger-labview-api-ref/raw/resource/enus/vi-lib/flexlogger/automation/subvis/flexlogger-set-channel-values-vi.html
- document_id: `flexlogger-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the Values on the specified Channel names. For digital channels, specify 0 to set the channel low. Any other value will set the channel high. Call the Get Channel Names instance of this VI to get a list of valid channel names. icon Inputs/Outputs cgnrn.png FlexLogger session in FlexLogger sessi

### FlexLogger - Set Channel Values VI

Sets the **Values** on the specified **Channel names**. For digital channels, specify 0 to set the channel low. Any other value will set the channel high.

Call the **Get Channel Names** instance of this VI to get a list of valid channel names.

[IMAGE alt='icon' src='flexlogger-set-channel-values-vi.png']

#### Inputs/Outputs

| FlexLogger session in — FlexLogger session is a reference to the currently running FlexLogger application. Use the Connect to FlexLogger VI to get the current session. Channel names — Channel names is the array of channels to set values for. Values — Values is an array of values to set on for each of the corresponding channels in Channel names. error in (no error) — error in can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. FlexLogger session out — FlexLogger session is a reference to the currently running FlexLogger application. Use the Connect to FlexLogger VI to get the current session. error out — error out passes error or warning information out of a VI to be used by other VIs. Right-click the error out indicator on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. |
| --- |

Parent topic:

FlexLogger - Channel VI

<!--NI_TOPIC bundle=flexlogger-labview-api-ref path=vi-lib/flexlogger/automation/subvis/flexlogger-set-data-rate-for-data-rate-level-vi.html language=enus -->
## TOPIC 00034: FlexLogger - Set Data Rate for Data Rate Level VI

- bundle_id: `flexlogger-labview-api-ref`
- source_path: `vi-lib/flexlogger/automation/subvis/flexlogger-set-data-rate-for-data-rate-level-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger-labview-api-ref/raw/resource/enus/vi-lib/flexlogger/automation/subvis/flexlogger-set-data-rate-for-data-rate-level-vi.html
- document_id: `flexlogger-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the Data rate (Hz) for the selected Data rate level. For analog input channels, there are three available data rate levels (Slow, Medium, Fast), and for counter and digital input channels, there's a single data rate level available. The OnDemand data rate level can include static digital channe

### FlexLogger - Set Data Rate for Data Rate Level VI

Sets the **Data rate (Hz)** for the selected **Data rate level**. For analog input channels, there are three available data rate levels (Slow, Medium, Fast), and for counter and digital input channels, there's a single data rate level available. The OnDemand data rate level can include static digital channels and analog output channels.

Note: The data rate level only applies to DAQ channels.

[IMAGE alt='icon' src='flexlogger-set-data-rate-for-data-rate-level-vi.png']

#### Inputs/Outputs

| FlexLogger session in — FlexLogger session is a reference to the currently running FlexLogger application. Use the Connect to FlexLogger VI to get the current session. Data rate level — Data rate level specifies the data rate level for a channel in FlexLogger. Valid values are: Analog - Slow - for analog channels on the slow data rate level. Analog - Medium - for analog channels on the medium data rate level. Analog - Fast - for analog channels on the fast data rate level. Counter - for counter channels. Digital - for digital channels. OnDemand - for software timed channels. This can include software timed digital channels and analog output channels. Data rate (Hz) — Data rate (Hz) sets the data rate in hertz for the Data rate level. error in (no error) — error in can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. FlexLogger session out — FlexLogger session is a reference to the currently running FlexLogger application. Use the Connect to FlexLogger VI to get the current session. error out — error out passes error or warning information out of a VI to be used by other VIs. Right-click the error out indicator on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. |
| --- |

Parent topic:

FlexLogger - Data Rate VI

<!--NI_TOPIC bundle=flexlogger-labview-api-ref path=vi-lib/flexlogger/automation/subvis/flexlogger-set-log-file-info-vi.html language=enus -->
## TOPIC 00035: FlexLogger - Set Log File Info VI

- bundle_id: `flexlogger-labview-api-ref`
- source_path: `vi-lib/flexlogger/automation/subvis/flexlogger-set-log-file-info-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger-labview-api-ref/raw/resource/enus/vi-lib/flexlogger/automation/subvis/flexlogger-set-log-file-info-vi.html
- document_id: `flexlogger-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the information about the log file settings for the currently loaded project. Base path, and File name can have formatters included (i.e. {Year}, {Hour}, etc.). Call this VI before the test has started to set the log file info that will be used when the test starts. Once the test starts, any ch

### FlexLogger - Set Log File Info VI

Sets the information about the log file settings for the currently loaded project. **Base path**, and **File name** can have formatters included (i.e. {Year}, {Hour}, etc.). Call this VI before the test has started to set the log file info that will be used when the test starts. Once the test starts, any changes to these settings will not take effect until the next test starts.

[IMAGE alt='icon' src='flexlogger-set-log-file-info-vi.png']

#### Inputs/Outputs

| FlexLogger session in — FlexLogger session is a reference to the currently running FlexLogger application. Use the Connect to FlexLogger VI to get the current session. Base path — Base path is the base path of the log file specified in FlexLogger's Logging Specification. File name — File name is the name of the log file. error in (no error) — error in can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. File description — File description is the description of the log file. FlexLogger session out — FlexLogger session is a reference to the currently running FlexLogger application. Use the Connect to FlexLogger VI to get the current session. error out — error out passes error or warning information out of a VI to be used by other VIs. Right-click the error out indicator on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. |
| --- |

Parent topic:

FlexLogger - Log File VI

<!--NI_TOPIC bundle=flexlogger-labview-api-ref path=vi-lib/flexlogger/automation/subvis/flexlogger-set-test-properties-vi.html language=enus -->
## TOPIC 00036: FlexLogger - Set Test Properties VI

- bundle_id: `flexlogger-labview-api-ref`
- source_path: `vi-lib/flexlogger/automation/subvis/flexlogger-set-test-properties-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger-labview-api-ref/raw/resource/enus/vi-lib/flexlogger/automation/subvis/flexlogger-set-test-properties-vi.html
- document_id: `flexlogger-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the Test properties to log to file when a test starts. New properties will be added or existing properties with the same Name will be updated with the new settings. To remove test properties, use the Remove Test Properties instance of this VI. icon Inputs/Outputs cgnrn.png FlexLogger session in

### FlexLogger - Set Test Properties VI

Sets the **Test properties** to log to file when a test starts. New properties will be added or existing properties with the same Name will be updated with the new settings. To remove test properties, use the **Remove Test Properties** instance of this VI.

[IMAGE alt='icon' src='flexlogger-set-test-properties-vi.png']

#### Inputs/Outputs

| FlexLogger session in — FlexLogger session is a reference to the currently running FlexLogger application. Use the Connect to FlexLogger VI to get the current session. Test properties — Test properties is an array of properties for the current test. Name — Name is the name of the property. Value — Value is the value of the test property. Prompt on start — Prompt on start specifies whether to prompt the user for the value of the property when the test is started. error in (no error) — error in can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. FlexLogger session out — FlexLogger session is a reference to the currently running FlexLogger application. Use the Connect to FlexLogger VI to get the current session. error out — error out passes error or warning information out of a VI to be used by other VIs. Right-click the error out indicator on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. |
| --- |
| Name — Name is the name of the property. Value — Value is the value of the test property. Prompt on start — Prompt on start specifies whether to prompt the user for the value of the property when the test is started. |

Parent topic:

FlexLogger - Test Properties VI

<!--NI_TOPIC bundle=flexlogger-labview-api-ref path=vi-lib/flexlogger/automation/subvis/flexlogger-set-test-state-vi.html language=enus -->
## TOPIC 00037: FlexLogger - Set Test State VI

- bundle_id: `flexlogger-labview-api-ref`
- source_path: `vi-lib/flexlogger/automation/subvis/flexlogger-set-test-state-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger-labview-api-ref/raw/resource/enus/vi-lib/flexlogger/automation/subvis/flexlogger-set-test-state-vi.html
- document_id: `flexlogger-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the Test state to control when a test starts, stops, pauses, and resumes. If the current state of the test doesn't support the requested test state (i.e. current state is idle and Test state is Pause), an error will be returneds. Use the Get Test State instance of this VI to determine the curre

### FlexLogger - Set Test State VI

Sets the **Test state** to control when a test starts, stops, pauses, and resumes. If the current state of the test doesn't support the requested test state (i.e. current state is idle and **Test state** is Pause), an error will be returneds. 

Use the **Get Test State** instance of this VI to determine the current test state.

[IMAGE alt='icon' src='flexlogger-set-test-state-vi.png']

#### Inputs/Outputs

| FlexLogger session in — FlexLogger session is a reference to the currently running FlexLogger application. Use the Connect to FlexLogger VI to get the current session. Test action — Test state action is the action to perform on the current test. Valid values are: Start - starts the test. Stop - stops the test. Pause - pauses the test. Resume - resumes the test. error in (no error) — error in can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. FlexLogger session out — FlexLogger session is a reference to the currently running FlexLogger application. Use the Connect to FlexLogger VI to get the current session. error out — error out passes error or warning information out of a VI to be used by other VIs. Right-click the error out indicator on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. |
| --- |

Parent topic:

FlexLogger - Test State VI
