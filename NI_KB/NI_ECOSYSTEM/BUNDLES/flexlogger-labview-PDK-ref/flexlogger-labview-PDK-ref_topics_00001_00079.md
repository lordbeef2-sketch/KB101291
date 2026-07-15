# NI DOCUMENT BUNDLE: flexlogger-labview-PDK-ref

<!--NI_BUNDLE_CHUNK bundle=flexlogger-labview-PDK-ref start=1 end=79 -->
<!--NI_TOPIC bundle=flexlogger-labview-PDK-ref path=menus/categories/flexlogger/flexlogger/advanced-mnu.html language=enus -->
## TOPIC 00001: Advanced

- bundle_id: `flexlogger-labview-PDK-ref`
- source_path: `menus/categories/flexlogger/flexlogger/advanced-mnu.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger-labview-PDK-ref/raw/resource/enus/menus/categories/flexlogger/flexlogger/advanced-mnu.html
- document_id: `flexlogger-labview-PDK-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Advanced VIs to access advanced features for FlexLogger plugin development icon

### Advanced

Use the Advanced VIs to access advanced features for FlexLogger plugin development

[IMAGE alt='icon' src='advanced-mnu.png']

- [Set Plugin Timing VI](../../../../vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/set-plugin-timing-vi.html) Specify the timing configuration for the plugin's Process VI.
- [Set Plugin Resampling VI](../../../../vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/set-plugin-resampling-vi.html) Configure the plugin input resampling. These parameters control how input waveforms are aggregated. Since inputs to a plugin may be from multiple sources running at different rates, some kind of resampling strategy is required. Maximum or Minimum mode pick a rate based on the rate of the inputs mapped to this plugin. Custom rate specifies a fixed rate that the inputs will be resampled to regardless of the rate of the inputs. Block size and drift tolerance are also configurable. Block size determines the minimum amount of overlapping data to wait for until data is passed to the plugin. Drift Tolerance determines the maximum amount of data to save waiting for overlapping data. A larger Drift Tolerance potentially results in more memory usage while a small Drift Tolerance may result in issues aggregating data whose time bases have drifted relative to one another.
- [Remove Channels VI](../../../../vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/remove-channels-vi.html) Remove channels from the plugin.
- [Replace Producer Channels VI](../../../../vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/replace-producer-channels-vi.html) Replaces all existing producer channels with a new list of producer channels. This can be helpful for situations where configuration changes in such a way that all channels need to be recreated. This VI should be called conditionally when something about a channel has changed. Calling it every Configure Session.vi or Process.vi run will result in an infinite configuration loop.
- [Replace Channel Group VI](../../../../vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/replace-channel-group-vi.html) Replaces all the channels in the specified group with a new set of channels. This VI should be called conditionally when something about a channel has changed. Calling it every Configure Session.vi or Process.vi run will result in an infinite configuration loop.
- [Update Channels Unit VI](../../../../vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/update-channels-unit-vi.html) Updates the unit string for a set of channels. This VI will not cause another pass of the Configure Session state.
- [Get Data from Stream2 VI](../../../../vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/get-data-from-stream2-vi.html) This polymorphic VI contains several options for retrieving specfic pieces of data based on a specific unique identifier (either of a channel or parameter). Each individual VI takes a unique identifier and the results of either a setpoint or waveform read.
- [Remove Parameter VI](../../../../vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/parameteraccess/remove-parameter-vi.html) Use this VI to remove a parameter by name from the Plugin's collection of top level parameters.
- [Write Use Immediate Device Dialog VI](../../../../vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/write-use-immediate-device-dialog-vi.html) Use this VI to change the type of dialog shown at the group level in FlexLogger. An immediate dialog sends all property value changes immediately to the plugin allowing the plugin developer to add dynamic behaviors. An OK/Cancel dialog waits until OK is pressed to send all property value changes as single batch.
- [Set File Metadata VI](../../../../vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/set-file-metadata-vi.html) Use this VI to add top level file metadata into the TDMS log file. The parameters will be added to a group matching the display name of this plugin.
- [Log Event VI](../../../../vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/log-event-vi.html) This VI writes an event string into the Alarms and Events channel in the log file. It can be used to make notes from a plugin during test execution.
- [Write Trace Log VI](../../../../vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/write-trace-log-vi.html) Write Message to DebugView. You will need to download and install DebugView from Microsoft Sysinternals. Then run the executable to see the logged messages. This can be helpful when debugging plugins that run as part of FlexLogger. Use the Format Into String.vi to combine several pieces of information into a single string that can be logged. If there is an error on the error in terminal, the error code and string will also be included in the logged message. Note: When running DebugView, you can use the filter to only see messages that meet certain criteria. You can prefix all your debug messages to make it easy to only see these messages in DebugView since other applications may log messages to DebugView as well. Note: Any program that can view messages from OutputDebugString will be able to view these messages. This includes Visual Studio when it attaches to the NationalInstruments.IoDataPef.Engine.exe process under FlexLogger, which is the executable that runs the plug-ins.

Parent topic:

Plug-In Development

<!--NI_TOPIC bundle=flexlogger-labview-PDK-ref path=menus/categories/flexlogger/flexloggerpdk-mnu.html language=enus -->
## TOPIC 00002: Plug-In Development

- bundle_id: `flexlogger-labview-PDK-ref`
- source_path: `menus/categories/flexlogger/flexloggerpdk-mnu.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger-labview-PDK-ref/raw/resource/enus/menus/categories/flexlogger/flexloggerpdk-mnu.html
- document_id: `flexlogger-labview-PDK-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the FlexLogger Plugin Development Kit VIs to create plugins for FlexLogger icon

### Plug-In Development

Use the FlexLogger Plugin Development Kit VIs to create plugins for FlexLogger

[IMAGE alt='icon' src='flexloggerpdk-mnu.png']

- [Add Channels VI](../../../vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/add-channels-vi.html) Add channels to the plugin.
- [Get Valid Channels VI](../../../vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/get-valid-channels-vi.html) Get all non-disabled channels for the plugin. The list of channels can be used when reading the latest channel-specific parameters to determine which channel data to send to FlexLogger and how to send it. Plugin developers determine if channels can be disabled on with the option in the constructor for the respective channel.
- [Read Parameter VI](../../../vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/parameteraccess/read-parameter-vi.html) Read the latest plugin-level parameter value from FlexLogger. The parameter must first be created by a call of matching name and data type.
- [Write Parameter VI](../../../vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/parameteraccess/write-parameter-vi.html) Create or update a plugin-level parameter for users to interact with in FlexLogger.
- [Set Stream Timing VI](../../../vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/datahelpers/set-stream-timing-vi.html) Define the start time and dt for channel data written to FlexLogger as a 1D or 2D array of samples with Write Data.vi .
- [Read 1D Wfm (DBL)_v2 VI](../../../vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/datahelpers/read-1d-wfm-dbl-v2-vi.html) Read the latest values from FlexLogger as an array of waveforms. This VI accepts a list of channel waveform identifiers to read (that you pass in to the Create Channel VI typically called in the Initialize VI). If no channel identifiers are passed in, all available waveforms will be returned. Note: For Channel waveforms, use a colon in the unique identifier to specify a specific channel waveform (i.e. <channel identifier>:<waveform parameter name>), otherwise all waveforms associated with the unique identifier will be returned.
- [Read Latest Setpoints By Channel Identifier VI](../../../vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/datahelpers/read-latest-setpoints-by-channel-identifier-vi.html) Read the latest setpoint channel values from FlexLogger. The latest setpoint values are the values most recently entered into FlexLogger by the user. This VI accepts a list of channel identifiers to read. If no channel identifiers are passed, the latest value of all setpoint and waveform channels will be returned. The channel identifier list may contain identifiers from setpoint channels or the channel identifier from Multi or Single channel parameters.
- [Read 1D Wfm (Digital) VI](../../../vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/datahelpers/read-1d-wfm-digital-vi.html) Read the latest channel values from FlexLogger as an array of waveforms. This VI accepts a list of channel identifiers to read. If no channel identifiers are passed, waveforms of all setpoint and waveform channels will be returned. The channel identifier list may contain identifiers from setpoint channels or the channel identifier from Multi or Single Digital channel parameters.
- [Read Latest Digital Setpoints By Channel Identifier VI](../../../vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/datahelpers/read-latest-digital-setpoints-by-channel-identifier-vi.html) Read the latest setpoint channel values from FlexLogger. The latest setpoint values are the values most recently entered into FlexLogger by the user. This VI accepts a list of channel identifiers to read. If no channel identifiers are passed, the latest value of all digital setpoint and waveform channels will be returned. The channel identifier list may contain identifiers from setpoint channels or the channel identifier from Multi or Single channel parameters.
- [Write Data VI](../../../vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/datahelpers/write-data-vi.html) Write channel data to FlexLogger. The order of the data written should reflect the order of the plugin's valid channels, which is typically the order in which the channels were created.
- [Create Channel_v2 VI](../../../vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/create-channel-v2-vi.html) Creates a channel of the specified type.
- [Read Parameter VI](../../../vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/channel/parameteraccess/read-parameter-vi.html) Read the latest channel-specific parameter value from FlexLogger. The parameter must first be created by a call of matching name and data type.
- [Write Parameter VI](../../../vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/channel/parameteraccess/write-parameter-vi.html) Create or update a channel-specific parameter for users to interact with in FlexLogger.
- [Write Data Type VI](../../../vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/channel/write-data-type-vi.html) Sets the data type of a particular channel. Changing the data type changes which read and write VIs can use the channel and how the channel is presented in FlexLogger.
- [Advanced](../../../menus/categories/flexlogger/flexlogger/advanced-mnu.html) Use the Advanced VIs to access advanced features for FlexLogger plugin development

<!--NI_TOPIC bundle=flexlogger-labview-PDK-ref path=vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/channel/parameteraccess/read-boolean-vi.html language=enus -->
## TOPIC 00003: Read Boolean VI

- bundle_id: `flexlogger-labview-PDK-ref`
- source_path: `vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/channel/parameteraccess/read-boolean-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger-labview-PDK-ref/raw/resource/enus/vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/channel/parameteraccess/read-boolean-vi.html
- document_id: `flexlogger-labview-PDK-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Read the latest channel-specific parameter value from FlexLogger as a boolean operation. The parameter must first be created by a call of matching name and data type. icon Inputs/Outputs cPluginSDK_lvlibp_Channellvclass.png Channel in Channel In is the instance of the Channel.lvclass to operate on.

### Read Boolean VI

Read the latest channel-specific parameter value from FlexLogger as a boolean operation. The parameter must first be created by a call of matching name and data type.

[IMAGE alt='icon' src='read-boolean-vi.png']

#### Inputs/Outputs

| Channel in — Channel In is the instance of the Channel.lvclass to operate on. Name — Name is the name of the parameter. error in (no error) — The error in cluster can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. Channel out — Channel Out returns the instance of the Channel.lvclass. Value — Value is the value for this parameter or setpoint. Found — found returns TRUE if the parameter was found. error out — The error out cluster passes error or warning information out of a VI to be used by other VIs. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
| --- |

Parent topic:

Read Parameter VI

<!--NI_TOPIC bundle=flexlogger-labview-PDK-ref path=vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/channel/parameteraccess/read-dbl-vi.html language=enus -->
## TOPIC 00004: Read DBL VI

- bundle_id: `flexlogger-labview-PDK-ref`
- source_path: `vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/channel/parameteraccess/read-dbl-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger-labview-PDK-ref/raw/resource/enus/vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/channel/parameteraccess/read-dbl-vi.html
- document_id: `flexlogger-labview-PDK-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Read the latest channel-specific parameter value from FlexLogger as a double-precision, floating-point numeric. The parameter must first be created by a call of matching name and data type. icon Inputs/Outputs cPluginSDK_lvlibp_Channellvclass.png Channel in Channel In is the instance of the Channel.

### Read DBL VI

Read the latest channel-specific parameter value from FlexLogger as a double-precision, floating-point numeric. The parameter must first be created by a call of matching name and data type.

[IMAGE alt='icon' src='read-dbl-vi.png']

#### Inputs/Outputs

| Channel in — Channel In is the instance of the Channel.lvclass to operate on. Name — Name is the name of the parameter. error in (no error) — The error in cluster can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. Channel out — Channel Out returns the instance of the Channel.lvclass. Value — Value is the value for this parameter or setpoint. Found — found returns TRUE if the parameter was found. error out — The error out cluster passes error or warning information out of a VI to be used by other VIs. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
| --- |

Parent topic:

Read Parameter VI

<!--NI_TOPIC bundle=flexlogger-labview-PDK-ref path=vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/channel/parameteraccess/read-enum-vi.html language=enus -->
## TOPIC 00005: Read Enum VI

- bundle_id: `flexlogger-labview-PDK-ref`
- source_path: `vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/channel/parameteraccess/read-enum-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger-labview-PDK-ref/raw/resource/enus/vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/channel/parameteraccess/read-enum-vi.html
- document_id: `flexlogger-labview-PDK-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Read the latest channel-specific parameter value from FlexLogger as an enumerated constant. The parameter must first be created by a call of matching name and data type. icon Inputs/Outputs cPluginSDK_lvlibp_Channellvclass.png Channel in Channel In is the instance of the Channel.lvclass to operate o

### Read Enum VI

Read the latest channel-specific parameter value from FlexLogger as an enumerated constant. The parameter must first be created by a call of matching name and data type.

[IMAGE alt='icon' src='read-enum-vi.png']

#### Inputs/Outputs

| Channel in — Channel In is the instance of the Channel.lvclass to operate on. Name — Name is the name of the parameter. error in (no error) — The error in cluster can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. Found — found returns TRUE if the parameter was found. Channel out — Channel Out returns the instance of the Channel.lvclass. Value — Value is the value for this parameter or setpoint. Index — Index is the index value of the enum. error out — The error out cluster passes error or warning information out of a VI to be used by other VIs. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
| --- |

Parent topic:

Read Parameter VI

<!--NI_TOPIC bundle=flexlogger-labview-PDK-ref path=vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/channel/parameteraccess/read-i32-vi.html language=enus -->
## TOPIC 00006: Read I32 VI

- bundle_id: `flexlogger-labview-PDK-ref`
- source_path: `vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/channel/parameteraccess/read-i32-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger-labview-PDK-ref/raw/resource/enus/vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/channel/parameteraccess/read-i32-vi.html
- document_id: `flexlogger-labview-PDK-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Read the latest channel-specific parameter value from FlexLogger as a 32-bit long signed integer. The parameter must first be created by a call of matching name and data type. icon Inputs/Outputs cPluginSDK_lvlibp_Channellvclass.png Channel in Channel In is the instance of the Channel.lvclass to ope

### Read I32 VI

Read the latest channel-specific parameter value from FlexLogger as a 32-bit long signed integer. The parameter must first be created by a call of matching name and data type.

[IMAGE alt='icon' src='read-i32-vi.png']

#### Inputs/Outputs

| Channel in — Channel In is the instance of the Channel.lvclass to operate on. Name — Name is the name of the parameter. error in (no error) — The error in cluster can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. Channel out — Channel Out returns the instance of the Channel.lvclass. Value — Value is the value for this parameter or setpoint. Found — found returns TRUE if the parameter was found. error out — The error out cluster passes error or warning information out of a VI to be used by other VIs. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
| --- |

Parent topic:

Read Parameter VI

<!--NI_TOPIC bundle=flexlogger-labview-PDK-ref path=vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/channel/parameteraccess/read-parameter-vi.html language=enus -->
## TOPIC 00007: Read Parameter VI

- bundle_id: `flexlogger-labview-PDK-ref`
- source_path: `vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/channel/parameteraccess/read-parameter-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger-labview-PDK-ref/raw/resource/enus/vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/channel/parameteraccess/read-parameter-vi.html
- document_id: `flexlogger-labview-PDK-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Read the latest channel-specific parameter value from FlexLogger. The parameter must first be created by a call of matching name and data type. icon

### Read Parameter VI

Read the latest channel-specific parameter value from FlexLogger. The parameter must first be created by a call of matching name and data type.

[IMAGE alt='icon' src='read-parameter-vi.png']

- [Read Boolean VI](../../../../../../../../vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/channel/parameteraccess/read-boolean-vi.html) Read the latest channel-specific parameter value from FlexLogger as a boolean operation. The parameter must first be created by a call of matching name and data type.
- [Read DBL VI](../../../../../../../../vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/channel/parameteraccess/read-dbl-vi.html) Read the latest channel-specific parameter value from FlexLogger as a double-precision, floating-point numeric. The parameter must first be created by a call of matching name and data type.
- [Read Enum VI](../../../../../../../../vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/channel/parameteraccess/read-enum-vi.html) Read the latest channel-specific parameter value from FlexLogger as an enumerated constant. The parameter must first be created by a call of matching name and data type.
- [Read I32 VI](../../../../../../../../vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/channel/parameteraccess/read-i32-vi.html) Read the latest channel-specific parameter value from FlexLogger as a 32-bit long signed integer. The parameter must first be created by a call of matching name and data type.
- [Read String VI](../../../../../../../../vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/channel/parameteraccess/read-string-vi.html) Read the latest channel-specific parameter value from FlexLogger as a text string. The parameter must first be created by a call of matching name and data type.

Parent topic:

Plug-In Development

<!--NI_TOPIC bundle=flexlogger-labview-PDK-ref path=vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/channel/parameteraccess/read-string-vi.html language=enus -->
## TOPIC 00008: Read String VI

- bundle_id: `flexlogger-labview-PDK-ref`
- source_path: `vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/channel/parameteraccess/read-string-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger-labview-PDK-ref/raw/resource/enus/vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/channel/parameteraccess/read-string-vi.html
- document_id: `flexlogger-labview-PDK-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Read the latest channel-specific parameter value from FlexLogger as a text string. The parameter must first be created by a call of matching name and data type. icon Inputs/Outputs cPluginSDK_lvlibp_Channellvclass.png Channel in Channel In is the instance of the Channel.lvclass to operate on. cstr.p

### Read String VI

Read the latest channel-specific parameter value from FlexLogger as a text string. The parameter must first be created by a call of matching name and data type.

[IMAGE alt='icon' src='read-string-vi.png']

#### Inputs/Outputs

| Channel in — Channel In is the instance of the Channel.lvclass to operate on. Name — Name is the name of the parameter. error in (no error) — The error in cluster can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. Channel out — Channel Out returns the instance of the Channel.lvclass. Value — Value is the value for this parameter or setpoint. Found — found returns TRUE if the parameter was found. error out — The error out cluster passes error or warning information out of a VI to be used by other VIs. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
| --- |

Parent topic:

Read Parameter VI

<!--NI_TOPIC bundle=flexlogger-labview-PDK-ref path=vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/channel/parameteraccess/write-boolean-vi.html language=enus -->
## TOPIC 00009: Write Boolean VI

- bundle_id: `flexlogger-labview-PDK-ref`
- source_path: `vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/channel/parameteraccess/write-boolean-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger-labview-PDK-ref/raw/resource/enus/vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/channel/parameteraccess/write-boolean-vi.html
- document_id: `flexlogger-labview-PDK-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Create or update a channel-specific parameter for users to interact with in FlexLogger. This parameter is a boolean control. icon Inputs/Outputs cPluginSDK_lvlibp_Channellvclass.png Channel in Channel In is the instance of the Channel.lvclass to operate on. cstr.png Name Name is the name of the para

### Write Boolean VI

Create or update a channel-specific parameter for users to interact with in FlexLogger. This parameter is a boolean control.

[IMAGE alt='icon' src='write-boolean-vi.png']

#### Inputs/Outputs

| Channel in — Channel In is the instance of the Channel.lvclass to operate on. Name — Name is the name of the parameter. Value — Value is the value for this parameter or setpoint. error in (no error) — The error in cluster can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. Channel out — Channel Out returns the instance of the Channel.lvclass. error out — The error out cluster passes error or warning information out of a VI to be used by other VIs. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
| --- |

Parent topic:

Write Parameter VI

<!--NI_TOPIC bundle=flexlogger-labview-PDK-ref path=vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/channel/parameteraccess/write-dbl-vi.html language=enus -->
## TOPIC 00010: Write DBL VI

- bundle_id: `flexlogger-labview-PDK-ref`
- source_path: `vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/channel/parameteraccess/write-dbl-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger-labview-PDK-ref/raw/resource/enus/vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/channel/parameteraccess/write-dbl-vi.html
- document_id: `flexlogger-labview-PDK-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Create or update a channel-specific parameter for users to interact with in FlexLogger. This parameter is a double-precision, floating-point numeric. icon Inputs/Outputs cPluginSDK_lvlibp_Channellvclass.png Channel in Channel In is the instance of the Channel.lvclass to operate on. cstr.png Name Nam

### Write DBL VI

Create or update a channel-specific parameter for users to interact with in FlexLogger. This parameter is a double-precision, floating-point numeric.

[IMAGE alt='icon' src='write-dbl-vi.png']

#### Inputs/Outputs

| Channel in — Channel In is the instance of the Channel.lvclass to operate on. Name — Name is the name of the parameter. Value — Value is the value for this parameter or setpoint. error in (no error) — The error in cluster can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. Channel out — Channel Out returns the instance of the Channel.lvclass. error out — The error out cluster passes error or warning information out of a VI to be used by other VIs. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
| --- |

Parent topic:

Write Parameter VI

<!--NI_TOPIC bundle=flexlogger-labview-PDK-ref path=vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/channel/parameteraccess/write-enum-vi.html language=enus -->
## TOPIC 00011: Write Enum VI

- bundle_id: `flexlogger-labview-PDK-ref`
- source_path: `vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/channel/parameteraccess/write-enum-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger-labview-PDK-ref/raw/resource/enus/vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/channel/parameteraccess/write-enum-vi.html
- document_id: `flexlogger-labview-PDK-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Create or update a channel-specific parameter for users to interact with in FlexLogger. This parameter is an enumerated constant. icon Inputs/Outputs c1dstr.png Possible Values Possible Values specifies the possible values for the enum. cPluginSDK_lvlibp_Channellvclass.png Channel in Channel In is t

### Write Enum VI

Create or update a channel-specific parameter for users to interact with in FlexLogger. This parameter is an enumerated constant.

[IMAGE alt='icon' src='write-enum-vi.png']

#### Inputs/Outputs

| Possible Values — Possible Values specifies the possible values for the enum. Channel in — Channel In is the instance of the Channel.lvclass to operate on. Name — Name is the name of the parameter. Current Value — Current Value is the desired current value of the enum. error in (no error) — The error in cluster can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. Channel out — Channel Out returns the instance of the Channel.lvclass. error out — The error out cluster passes error or warning information out of a VI to be used by other VIs. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
| --- |

Parent topic:

Write Parameter VI

<!--NI_TOPIC bundle=flexlogger-labview-PDK-ref path=vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/channel/parameteraccess/write-i32-vi.html language=enus -->
## TOPIC 00012: Write I32 VI

- bundle_id: `flexlogger-labview-PDK-ref`
- source_path: `vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/channel/parameteraccess/write-i32-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger-labview-PDK-ref/raw/resource/enus/vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/channel/parameteraccess/write-i32-vi.html
- document_id: `flexlogger-labview-PDK-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Create or update a channel-specific parameter for users to interact with in FlexLogger. This parameter is a 32-bit long signed integer. icon Inputs/Outputs cPluginSDK_lvlibp_Channellvclass.png Channel in Channel In is the instance of the Channel.lvclass to operate on. cstr.png Name Name is the name

### Write I32 VI

Create or update a channel-specific parameter for users to interact with in FlexLogger. This parameter is a 32-bit long signed integer.

[IMAGE alt='icon' src='write-i32-vi.png']

#### Inputs/Outputs

| Channel in — Channel In is the instance of the Channel.lvclass to operate on. Name — Name is the name of the parameter. Value — Value is the value for this parameter or setpoint. error in (no error) — The error in cluster can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. Channel out — Channel Out returns the instance of the Channel.lvclass. error out — The error out cluster passes error or warning information out of a VI to be used by other VIs. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
| --- |

Parent topic:

Write Parameter VI

<!--NI_TOPIC bundle=flexlogger-labview-PDK-ref path=vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/channel/parameteraccess/write-n-channel-vi.html language=enus -->
## TOPIC 00013: Write N Channel VI

- bundle_id: `flexlogger-labview-PDK-ref`
- source_path: `vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/channel/parameteraccess/write-n-channel-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger-labview-PDK-ref/raw/resource/enus/vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/channel/parameteraccess/write-n-channel-vi.html
- document_id: `flexlogger-labview-PDK-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Create or update a channel-specific parameter for users to interact with in FlexLogger. This parameter allows a user to map multiple waveform channels to a plugin channel so the plugin channel can perform operations on the data. Note: This is only valid for Producer Channels created by the Create Ch

### Write N Channel VI

Create or update a channel-specific parameter for users to interact with in FlexLogger. This parameter allows a user to map multiple waveform channels to a plugin channel so the plugin channel can perform operations on the data.

**Note:** This is only valid for Producer Channels created by the **Create Channel.vi** and not a Setpoint Channel.

[IMAGE alt='icon' src='write-n-channel-vi.png']

#### Inputs/Outputs

| Channel in — Channel In is the instance of the Channel.lvclass to operate on. Name (Unique Channel Identifier) — Name (Unique Channel Identifier) is the name of the parameter for the channel(s). error in (no error) — The error in cluster can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. Channel out — Channel Out returns the instance of the Channel.lvclass. error out — The error out cluster passes error or warning information out of a VI to be used by other VIs. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
| --- |

Parent topic:

Write Parameter VI

<!--NI_TOPIC bundle=flexlogger-labview-PDK-ref path=vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/channel/parameteraccess/write-n-digital-channel-vi.html language=enus -->
## TOPIC 00014: Write N Digital Channel VI

- bundle_id: `flexlogger-labview-PDK-ref`
- source_path: `vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/channel/parameteraccess/write-n-digital-channel-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger-labview-PDK-ref/raw/resource/enus/vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/channel/parameteraccess/write-n-digital-channel-vi.html
- document_id: `flexlogger-labview-PDK-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Create or update a channel-specific parameter for users to interact with in FlexLogger. This parameter allows a user to map multiple digital waveform channels to a plugin channel so the plugin channel can perform operations on the data. Note: This is only valid for Producer Channels created by the C

### Write N Digital Channel VI

Create or update a channel-specific parameter for users to interact with in FlexLogger. This parameter allows a user to map multiple digital waveform channels to a plugin channel so the plugin channel can perform operations on the data.

**Note:** This is only valid for Producer Channels created by the **Create Channel.vi** and not a Setpoint Channel.

[IMAGE alt='icon' src='write-n-digital-channel-vi.png']

#### Inputs/Outputs

| Channel in — Channel In is the instance of the Channel.lvclass to operate on. Name (Unique Channel Identifier) — Name (Unique Channel Identifier) is the name of the parameter for the channel(s). error in (no error) — The error in cluster can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. Channel out — Channel Out returns the instance of the Channel.lvclass. error out — The error out cluster passes error or warning information out of a VI to be used by other VIs. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
| --- |

Parent topic:

Write Parameter VI

<!--NI_TOPIC bundle=flexlogger-labview-PDK-ref path=vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/channel/parameteraccess/write-parameter-vi.html language=enus -->
## TOPIC 00015: Write Parameter VI

- bundle_id: `flexlogger-labview-PDK-ref`
- source_path: `vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/channel/parameteraccess/write-parameter-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger-labview-PDK-ref/raw/resource/enus/vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/channel/parameteraccess/write-parameter-vi.html
- document_id: `flexlogger-labview-PDK-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Create or update a channel-specific parameter for users to interact with in FlexLogger. icon

### Write Parameter VI

Create or update a channel-specific parameter for users to interact with in FlexLogger.

[IMAGE alt='icon' src='write-parameter-vi.png']

- [Write Boolean VI](../../../../../../../../vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/channel/parameteraccess/write-boolean-vi.html) Create or update a channel-specific parameter for users to interact with in FlexLogger. This parameter is a boolean control.
- [Write DBL VI](../../../../../../../../vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/channel/parameteraccess/write-dbl-vi.html) Create or update a channel-specific parameter for users to interact with in FlexLogger. This parameter is a double-precision, floating-point numeric.
- [Write Enum VI](../../../../../../../../vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/channel/parameteraccess/write-enum-vi.html) Create or update a channel-specific parameter for users to interact with in FlexLogger. This parameter is an enumerated constant.
- [Write I32 VI](../../../../../../../../vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/channel/parameteraccess/write-i32-vi.html) Create or update a channel-specific parameter for users to interact with in FlexLogger. This parameter is a 32-bit long signed integer.
- [Write String VI](../../../../../../../../vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/channel/parameteraccess/write-string-vi.html) Create or update a channel-specific parameter for users to interact with in FlexLogger. This parameter is a text string.
- [Write Single Channel VI](../../../../../../../../vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/channel/parameteraccess/write-single-channel-vi.html) Create or update a channel-specific parameter for users to interact with in FlexLogger. This parameter allows a user to map a single waveform channel to a plugin channel so the plugin channel can perform operations on the data. Note: This is only valid for Producer Channels created by the Create Channel.vi and not a Setpoint Channel.
- [Write Single Digital Channel VI](../../../../../../../../vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/channel/parameteraccess/write-single-digital-channel-vi.html) Create or update a channel-specific parameter for users to interact with in FlexLogger. This parameter allows a user to map a single digital waveform channel to a plugin channel so the plugin channel can perform operations on the data. Note: This is only valid for Producer Channels created by the Create Channel.vi and not a Setpoint Channel.
- [Write N Channel VI](../../../../../../../../vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/channel/parameteraccess/write-n-channel-vi.html) Create or update a channel-specific parameter for users to interact with in FlexLogger. This parameter allows a user to map multiple waveform channels to a plugin channel so the plugin channel can perform operations on the data. Note: This is only valid for Producer Channels created by the Create Channel.vi and not a Setpoint Channel.
- [Write N Digital Channel VI](../../../../../../../../vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/channel/parameteraccess/write-n-digital-channel-vi.html) Create or update a channel-specific parameter for users to interact with in FlexLogger. This parameter allows a user to map multiple digital waveform channels to a plugin channel so the plugin channel can perform operations on the data. Note: This is only valid for Producer Channels created by the Create Channel.vi and not a Setpoint Channel.

Parent topic:

Plug-In Development

<!--NI_TOPIC bundle=flexlogger-labview-PDK-ref path=vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/channel/parameteraccess/write-single-channel-vi.html language=enus -->
## TOPIC 00016: Write Single Channel VI

- bundle_id: `flexlogger-labview-PDK-ref`
- source_path: `vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/channel/parameteraccess/write-single-channel-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger-labview-PDK-ref/raw/resource/enus/vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/channel/parameteraccess/write-single-channel-vi.html
- document_id: `flexlogger-labview-PDK-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Create or update a channel-specific parameter for users to interact with in FlexLogger. This parameter allows a user to map a single waveform channel to a plugin channel so the plugin channel can perform operations on the data. Note: This is only valid for Producer Channels created by the Create Cha

### Write Single Channel VI

Create or update a channel-specific parameter for users to interact with in FlexLogger. This parameter allows a user to map a single waveform channel to a plugin channel so the plugin channel can perform operations on the data.

**Note:** This is only valid for Producer Channels created by the **Create Channel.vi** and not a Setpoint Channel.

[IMAGE alt='icon' src='write-single-channel-vi.png']

#### Inputs/Outputs

| Channel in — Channel In is the instance of the Channel.lvclass to operate on. Name (Unique Channel Identifier) — Name (Unique Channel Identifier) is the name of the parameter for the channel(s). error in (no error) — The error in cluster can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. Channel out — Channel Out returns the instance of the Channel.lvclass. error out — The error out cluster passes error or warning information out of a VI to be used by other VIs. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
| --- |

Parent topic:

Write Parameter VI

<!--NI_TOPIC bundle=flexlogger-labview-PDK-ref path=vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/channel/parameteraccess/write-single-digital-channel-vi.html language=enus -->
## TOPIC 00017: Write Single Digital Channel VI

- bundle_id: `flexlogger-labview-PDK-ref`
- source_path: `vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/channel/parameteraccess/write-single-digital-channel-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger-labview-PDK-ref/raw/resource/enus/vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/channel/parameteraccess/write-single-digital-channel-vi.html
- document_id: `flexlogger-labview-PDK-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Create or update a channel-specific parameter for users to interact with in FlexLogger. This parameter allows a user to map a single digital waveform channel to a plugin channel so the plugin channel can perform operations on the data. Note: This is only valid for Producer Channels created by the Cr

### Write Single Digital Channel VI

Create or update a channel-specific parameter for users to interact with in FlexLogger. This parameter allows a user to map a single digital waveform channel to a plugin channel so the plugin channel can perform operations on the data.

**Note:** This is only valid for Producer Channels created by the **Create Channel.vi** and not a Setpoint Channel.

[IMAGE alt='icon' src='write-single-digital-channel-vi.png']

#### Inputs/Outputs

| Channel in — Channel In is the instance of the Channel.lvclass to operate on. Name (Unique Channel Identifier) — Name (Unique Channel Identifier) is the name of the parameter for the channel(s). error in (no error) — The error in cluster can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. Channel out — Channel Out returns the instance of the Channel.lvclass. error out — The error out cluster passes error or warning information out of a VI to be used by other VIs. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
| --- |

Parent topic:

Write Parameter VI

<!--NI_TOPIC bundle=flexlogger-labview-PDK-ref path=vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/channel/parameteraccess/write-string-vi.html language=enus -->
## TOPIC 00018: Write String VI

- bundle_id: `flexlogger-labview-PDK-ref`
- source_path: `vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/channel/parameteraccess/write-string-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger-labview-PDK-ref/raw/resource/enus/vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/channel/parameteraccess/write-string-vi.html
- document_id: `flexlogger-labview-PDK-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Create or update a channel-specific parameter for users to interact with in FlexLogger. This parameter is a text string. icon Inputs/Outputs cPluginSDK_lvlibp_Channellvclass.png Channel in Channel In is the instance of the Channel.lvclass to operate on. cstr.png Name Name is the name of the paramete

### Write String VI

Create or update a channel-specific parameter for users to interact with in FlexLogger. This parameter is a text string.

[IMAGE alt='icon' src='write-string-vi.png']

#### Inputs/Outputs

| Channel in — Channel In is the instance of the Channel.lvclass to operate on. Name — Name is the name of the parameter. Value — Value is the value for this parameter or setpoint. error in (no error) — The error in cluster can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. Channel out — Channel Out returns the instance of the Channel.lvclass. error out — The error out cluster passes error or warning information out of a VI to be used by other VIs. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
| --- |

Parent topic:

Write Parameter VI

<!--NI_TOPIC bundle=flexlogger-labview-PDK-ref path=vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/channel/write-data-type-vi.html language=enus -->
## TOPIC 00019: Write Data Type VI

- bundle_id: `flexlogger-labview-PDK-ref`
- source_path: `vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/channel/write-data-type-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger-labview-PDK-ref/raw/resource/enus/vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/channel/write-data-type-vi.html
- document_id: `flexlogger-labview-PDK-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the data type of a particular channel. Changing the data type changes which read and write VIs can use the channel and how the channel is presented in FlexLogger. icon Inputs/Outputs cPluginSDK_lvlibp_Channellvclass.png Channel in Channel In is the instance of the Channel.lvclass to operate on.

### Write Data Type VI

Sets the data type of a particular channel. Changing the data type changes which read and write VIs can use the channel and how the channel is presented in FlexLogger.

[IMAGE alt='icon' src='write-data-type-vi.png']

#### Inputs/Outputs

| Channel in — Channel In is the instance of the Channel.lvclass to operate on. Data Type — Data Type is the data type of the channel. Valid values are: Wfm (DBL) - for analog channels Wfm (Digital) - for digital channels String - for string channels error in (no error) — The error in cluster can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. Channel out — Channel Out returns the instance of the Channel.lvclass. error out — The error out cluster passes error or warning information out of a VI to be used by other VIs. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
| --- |

Parent topic:

Plug-In Development

<!--NI_TOPIC bundle=flexlogger-labview-PDK-ref path=vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/create-channel-v2-vi.html language=enus -->
## TOPIC 00020: Create Channel_v2 VI

- bundle_id: `flexlogger-labview-PDK-ref`
- source_path: `vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/create-channel-v2-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger-labview-PDK-ref/raw/resource/enus/vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/create-channel-v2-vi.html
- document_id: `flexlogger-labview-PDK-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a channel of the specified type. icon

### Create Channel_v2 VI

Creates a channel of the specified type.

[IMAGE alt='icon' src='create-channel-v2-vi.png']

- [Create Producer Channel_v2 VI](../../../../../../vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/producer-channel/create-producer-channel-v2-vi.html) Create a channel that sends data from the plugin to the FlexLogger application using Write Data.vi .
- [Create Setpoint Consumer Channel VI](../../../../../../vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/setpoint-consumer-channel/create-setpoint-consumer-channel-vi.html) Create a channel that allows a FlexLogger user to enter setpoint values. Those setpoint channel values are consumed by the plugin using Get Latest Setpoints.vi .
- [Create Derived Time Producer Channel_v2 VI](../../../../../../vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/derived-timing-producer-channel/create-derived-time-producer-channel-v2-vi.html) Creates a producer channel whose sample rate is controlled by the input channels to the plugin depending on the resampling mode selected.

Parent topic:

Plug-In Development

<!--NI_TOPIC bundle=flexlogger-labview-PDK-ref path=vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/derived-timing-producer-channel/create-derived-time-producer-channel-v2-vi.html language=enus -->
## TOPIC 00021: Create Derived Time Producer Channel_v2 VI

- bundle_id: `flexlogger-labview-PDK-ref`
- source_path: `vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/derived-timing-producer-channel/create-derived-time-producer-channel-v2-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger-labview-PDK-ref/raw/resource/enus/vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/derived-timing-producer-channel/create-derived-time-producer-channel-v2-vi.html
- document_id: `flexlogger-labview-PDK-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a producer channel whose sample rate is controlled by the input channels to the plugin depending on the resampling mode selected. icon Inputs/Outputs cu16.png Data Type Data Type is the data type of the channel. Valid values are: Wfm (DBL) - for analog channels Wfm (Digital) - for digital ch

### Create Derived Time Producer Channel_v2 VI

Creates a producer channel whose sample rate is controlled by the input channels to the plugin depending on the resampling mode selected.

[IMAGE alt='icon' src='create-derived-time-producer-channel-v2-vi.png']

#### Inputs/Outputs

| Data Type — Data Type is the data type of the channel. Valid values are: Wfm (DBL) - for analog channels Wfm (Digital) - for digital channels String - for string channels Display Group — Display Group is the group to display the channel within. Channels with the same Display Group will be grouped together in FlexLogger. Unique Channel Identifier — Unique Channel Identifier is the unique identifier for the channel. You can use this identifier to reference this channel when reading data in Process.vi. Default Channel Name — Default Channel Name is the default name for the channel when the plugin is added to FlexLogger. Parameters — Parameters is an instance of the Parameters.lvclass that can be created using members of the Parameters.lvclass library for advanced use cases. However, for most use cases, this input can be left unwired, and users should use the Write Parameter.vi to create channel parameters. error in (no error) — The error in cluster can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. Unit — Unit is the string value of units for this channel. Can Disable? — Can Disable? determines whether the channel can be disabled in the Channel Specification in FlexLogger. Producer Channel — Producer Channel is the created producer channel. error out — The error out cluster passes error or warning information out of a VI to be used by other VIs. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
| --- |

Parent topic:

Create Channel_v2 VI

<!--NI_TOPIC bundle=flexlogger-labview-PDK-ref path=vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/add-channels-vi.html language=enus -->
## TOPIC 00022: Add Channels VI

- bundle_id: `flexlogger-labview-PDK-ref`
- source_path: `vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/add-channels-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger-labview-PDK-ref/raw/resource/enus/vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/add-channels-vi.html
- document_id: `flexlogger-labview-PDK-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Add channels to the plugin. icon Inputs/Outputs cPluginSDK_lvlibp_Pluginlvclass.png Plugin in Plugin In is the instance of the user's Plugin.lvclass being passed in. c1dPluginSDK_lvlibp_Channellvclass.png Channels Channels is an array of channel objects of type Channel.lvclass. cerrcodeclst.png erro

### Add Channels VI

Add channels to the plugin.

[IMAGE alt='icon' src='add-channels-vi.png']

#### Inputs/Outputs

| Plugin in — Plugin In is the instance of the user's Plugin.lvclass being passed in. Channels — Channels is an array of channel objects of type Channel.lvclass. error in (no error) — The error in cluster can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. Plugin out — Plugin out is the instance of the user's Plugin.lvclass being passed out. error out — The error out cluster passes error or warning information out of a VI to be used by other VIs. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
| --- |

Parent topic:

Plug-In Development

<!--NI_TOPIC bundle=flexlogger-labview-PDK-ref path=vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/datahelpers/read-1d-wfm-dbl-v2-vi.html language=enus -->
## TOPIC 00023: Read 1D Wfm (DBL)_v2 VI

- bundle_id: `flexlogger-labview-PDK-ref`
- source_path: `vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/datahelpers/read-1d-wfm-dbl-v2-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger-labview-PDK-ref/raw/resource/enus/vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/datahelpers/read-1d-wfm-dbl-v2-vi.html
- document_id: `flexlogger-labview-PDK-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Read the latest values from FlexLogger as an array of waveforms. This VI accepts a list of channel waveform identifiers to read (that you pass in to the Create Channel VI typically called in the Initialize VI). If no channel identifiers are passed in, all available waveforms will be returned. Note:

### Read 1D Wfm (DBL)_v2 VI

Read the latest values from FlexLogger as an array of waveforms. This VI accepts a list of channel waveform identifiers to read (that you pass in to the Create Channel VI typically called in the Initialize VI). If no channel identifiers are passed in, all available waveforms will be returned.

**Note:** For Channel waveforms, use a colon in the unique identifier to specify a specific channel waveform (i.e. <channel identifier>:<waveform parameter name>), otherwise all waveforms associated with the unique identifier will be returned.

[IMAGE alt='icon' src='read-1d-wfm-dbl-v2-vi.png']

#### Inputs/Outputs

| Plugin in — Plugin In is the instance of the user's Plugin.lvclass being passed in. Unique Identifiers (empty = all) — Unique Identifiers (empty = all) is the unique channel identifiers to read data from. If this value is empty, all channels will be read. error in (no error) — The error in cluster can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. Plugin out — Plugin out is the instance of the user's Plugin.lvclass being passed out. Data — Data is the data in the specified format. Stream Names — Stream Names are the names of the data streams returned when reading data. error out — The error out cluster passes error or warning information out of a VI to be used by other VIs. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
| --- |

Parent topic:

Plug-In Development

<!--NI_TOPIC bundle=flexlogger-labview-PDK-ref path=vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/datahelpers/read-1d-wfm-digital-vi.html language=enus -->
## TOPIC 00024: Read 1D Wfm (Digital) VI

- bundle_id: `flexlogger-labview-PDK-ref`
- source_path: `vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/datahelpers/read-1d-wfm-digital-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger-labview-PDK-ref/raw/resource/enus/vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/datahelpers/read-1d-wfm-digital-vi.html
- document_id: `flexlogger-labview-PDK-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Read the latest channel values from FlexLogger as an array of waveforms. This VI accepts a list of channel identifiers to read. If no channel identifiers are passed, waveforms of all setpoint and waveform channels will be returned. The channel identifier list may contain identifiers from setpoint ch

### Read 1D Wfm (Digital) VI

Read the latest channel values from FlexLogger as an array of waveforms. This VI accepts a list of channel identifiers to read. If no channel identifiers are passed, waveforms of all setpoint and waveform channels will be returned. The channel identifier list may contain identifiers from setpoint channels or the channel identifier from Multi or Single Digital channel parameters.

[IMAGE alt='icon' src='read-1d-wfm-digital-vi.png']

#### Inputs/Outputs

| Plugin in — Plugin In is the instance of the user's Plugin.lvclass being passed in. Unique Channel Identifiers (empty = all) — Unique Channel Identifiers (empty = all) is the unique channel identifiers to read data from. If this value is empty, all channels will be read. error in (no error) — The error in cluster can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. Plugin out — Plugin out is the instance of the user's Plugin.lvclass being passed out. Digital Waveforms — Digital Waveforms is the digital waveform data being read. Stream Names — Stream Names are the names of the data streams returned when reading data. error out — The error out cluster passes error or warning information out of a VI to be used by other VIs. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
| --- |

Parent topic:

Plug-In Development

<!--NI_TOPIC bundle=flexlogger-labview-PDK-ref path=vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/datahelpers/read-latest-digital-setpoints-by-channel-identifier-vi.html language=enus -->
## TOPIC 00025: Read Latest Digital Setpoints By Channel Identifier VI

- bundle_id: `flexlogger-labview-PDK-ref`
- source_path: `vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/datahelpers/read-latest-digital-setpoints-by-channel-identifier-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger-labview-PDK-ref/raw/resource/enus/vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/datahelpers/read-latest-digital-setpoints-by-channel-identifier-vi.html
- document_id: `flexlogger-labview-PDK-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Read the latest setpoint channel values from FlexLogger. The latest setpoint values are the values most recently entered into FlexLogger by the user. This VI accepts a list of channel identifiers to read. If no channel identifiers are passed, the latest value of all digital setpoint and waveform cha

### Read Latest Digital Setpoints By Channel Identifier VI

Read the latest setpoint channel values from FlexLogger. The latest setpoint values are the values most recently entered into FlexLogger by the user. This VI accepts a list of channel identifiers to read. If no channel identifiers are passed, the latest value of all digital setpoint and waveform channels will be returned. The channel identifier list may contain identifiers from setpoint channels or the channel identifier from Multi or Single channel parameters.

[IMAGE alt='icon' src='read-latest-digital-setpoints-by-channel-identifier-vi.png']

#### Inputs/Outputs

| Plugin in — Plugin In is the instance of the user's Plugin.lvclass being passed in. Unique Channel Identifiers (empty = all) — Unique Channel Identifiers (empty = all) is the unique channel identifiers to read data from. If this value is empty, all channels will be read. error in (no error) — The error in cluster can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. Plugin out — Plugin out is the instance of the user's Plugin.lvclass being passed out. Names — Names is an array of unique unique channel identifier names. Values — Values are the latest values for the setpoint channels. error out — The error out cluster passes error or warning information out of a VI to be used by other VIs. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
| --- |

Parent topic:

Plug-In Development

<!--NI_TOPIC bundle=flexlogger-labview-PDK-ref path=vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/datahelpers/read-latest-setpoints-by-channel-identifier-vi.html language=enus -->
## TOPIC 00026: Read Latest Setpoints By Channel Identifier VI

- bundle_id: `flexlogger-labview-PDK-ref`
- source_path: `vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/datahelpers/read-latest-setpoints-by-channel-identifier-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger-labview-PDK-ref/raw/resource/enus/vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/datahelpers/read-latest-setpoints-by-channel-identifier-vi.html
- document_id: `flexlogger-labview-PDK-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Read the latest setpoint channel values from FlexLogger. The latest setpoint values are the values most recently entered into FlexLogger by the user. This VI accepts a list of channel identifiers to read. If no channel identifiers are passed, the latest value of all setpoint and waveform channels wi

### Read Latest Setpoints By Channel Identifier VI

Read the latest setpoint channel values from FlexLogger. The latest setpoint values are the values most recently entered into FlexLogger by the user. This VI accepts a list of channel identifiers to read. If no channel identifiers are passed, the latest value of all setpoint and waveform channels will be returned. The channel identifier list may contain identifiers from setpoint channels or the channel identifier from Multi or Single channel parameters.

[IMAGE alt='icon' src='read-latest-setpoints-by-channel-identifier-vi.png']

#### Inputs/Outputs

| Plugin in — Plugin In is the instance of the user's Plugin.lvclass being passed in. Unique Channel Identifiers (empty = all) — Unique Channel Identifiers (empty = all) is the unique channel identifiers to read data from. If this value is empty, all channels will be read. error in (no error) — The error in cluster can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. Names — Names is an array of unique unique channel identifier names. Plugin out — Plugin out is the instance of the user's Plugin.lvclass being passed out. Channel Setpoints — Channel Setpoints is an array of the latest setpoint values for each channel. error out — The error out cluster passes error or warning information out of a VI to be used by other VIs. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
| --- |

Parent topic:

Plug-In Development

<!--NI_TOPIC bundle=flexlogger-labview-PDK-ref path=vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/datahelpers/set-stream-timing-vi.html language=enus -->
## TOPIC 00027: Set Stream Timing VI

- bundle_id: `flexlogger-labview-PDK-ref`
- source_path: `vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/datahelpers/set-stream-timing-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger-labview-PDK-ref/raw/resource/enus/vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/datahelpers/set-stream-timing-vi.html
- document_id: `flexlogger-labview-PDK-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Define the start time and dt for channel data written to FlexLogger as a 1D or 2D array of samples with Write Data.vi. icon Inputs/Outputs cPluginSDK_lvlibp_Pluginlvclass.png Plugin in Plugin In is the instance of the user's Plugin.lvclass being passed in. catrn.png Start Time Start Time is used to

### Set Stream Timing VI

Define the start time and dt for channel data written to FlexLogger as a 1D or 2D array of samples with **Write Data.vi**.

[IMAGE alt='icon' src='set-stream-timing-vi.png']

#### Inputs/Outputs

| Plugin in — Plugin In is the instance of the user's Plugin.lvclass being passed in. Start Time — Start Time is used to define the start time for channel data written to FlexLogger. dt(sec) — dt(sec) is the sampling interval in seconds. error in (no error) — The error in cluster can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. Plugin out — Plugin out is the instance of the user's Plugin.lvclass being passed out. error out — The error out cluster passes error or warning information out of a VI to be used by other VIs. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
| --- |

Parent topic:

Plug-In Development

<!--NI_TOPIC bundle=flexlogger-labview-PDK-ref path=vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/datahelpers/write-1d-bool-nchan-1-sample-vi.html language=enus -->
## TOPIC 00028: Write 1D Bool (NChan 1 Sample) VI

- bundle_id: `flexlogger-labview-PDK-ref`
- source_path: `vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/datahelpers/write-1d-bool-nchan-1-sample-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger-labview-PDK-ref/raw/resource/enus/vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/datahelpers/write-1d-bool-nchan-1-sample-vi.html
- document_id: `flexlogger-labview-PDK-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Write channel data to FlexLogger as a 1D array of samples. The order of the data written should reflect the order of the plugin's valid channels, which is typically the order in which the channels were created. The timing information for this data is defined by Set Stream Timing.vi. icon Inputs/Outp

### Write 1D Bool (NChan 1 Sample) VI

Write channel data to FlexLogger as a 1D array of samples. The order of the data written should reflect the order of the plugin's valid channels, which is typically the order in which the channels were created. The timing information for this data is defined by Set Stream Timing.vi.

[IMAGE alt='icon' src='write-1d-bool-nchan-1-sample-vi.png']

#### Inputs/Outputs

| Plugin in — Plugin In is the instance of the user's Plugin.lvclass being passed in. Data — Data is the data in the specified format. error in (no error) — The error in cluster can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. Plugin out — Plugin out is the instance of the user's Plugin.lvclass being passed out. error out — The error out cluster passes error or warning information out of a VI to be used by other VIs. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
| --- |

Parent topic:

Write Data VI

<!--NI_TOPIC bundle=flexlogger-labview-PDK-ref path=vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/datahelpers/write-1d-dbl-nchan-1sample-vi.html language=enus -->
## TOPIC 00029: Write 1D DBL (NChan 1Sample) VI

- bundle_id: `flexlogger-labview-PDK-ref`
- source_path: `vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/datahelpers/write-1d-dbl-nchan-1sample-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger-labview-PDK-ref/raw/resource/enus/vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/datahelpers/write-1d-dbl-nchan-1sample-vi.html
- document_id: `flexlogger-labview-PDK-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Write channel data to FlexLogger as a 1D array of samples. The order of the data written should reflect the order of the plugin's valid channels, which is typically the order in which the channels were created. The timing information for this data is defined by Set Stream Timing.vi. icon Inputs/Outp

### Write 1D DBL (NChan 1Sample) VI

Write channel data to FlexLogger as a 1D array of samples. The order of the data written should reflect the order of the plugin's valid channels, which is typically the order in which the channels were created. The timing information for this data is defined by Set Stream Timing.vi.

[IMAGE alt='icon' src='write-1d-dbl-nchan-1sample-vi.png']

#### Inputs/Outputs

| Plugin in — Plugin In is the instance of the user's Plugin.lvclass being passed in. Data — Data is the data in the specified format. error in (no error) — The error in cluster can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. Plugin out — Plugin out is the instance of the user's Plugin.lvclass being passed out. error out — The error out cluster passes error or warning information out of a VI to be used by other VIs. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
| --- |

Parent topic:

Write Data VI

<!--NI_TOPIC bundle=flexlogger-labview-PDK-ref path=vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/datahelpers/write-1d-str-nchan-1-sample-vi.html language=enus -->
## TOPIC 00030: Write 1D STR (NChan 1 Sample) VI

- bundle_id: `flexlogger-labview-PDK-ref`
- source_path: `vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/datahelpers/write-1d-str-nchan-1-sample-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger-labview-PDK-ref/raw/resource/enus/vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/datahelpers/write-1d-str-nchan-1-sample-vi.html
- document_id: `flexlogger-labview-PDK-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Write channel data to FlexLogger as a 1D array of strings. The order of the data written should reflect the order of the plugin's valid channels, which is typically the order in which the channels were created. If the Time Stamps are not provided, the VI will compute them automatically using the tim

### Write 1D STR (NChan 1 Sample) VI

Write channel data to FlexLogger as a 1D array of strings. The order of the data written should reflect the order of the plugin's valid channels, which is typically the order in which the channels were created.
If the Time Stamps are not provided, the VI will compute them automatically using the timing information configured by Set Stream Timing.vi.

[IMAGE alt='icon' src='write-1d-str-nchan-1-sample-vi.png']

#### Inputs/Outputs

| Plugin in — Plugin In is the instance of the user's Plugin.lvclass being passed in. Data — Data is the data in the specified format. Time Stamps — Time Stamps are the time stamps for the string data. error in (no error) — The error in cluster can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. Plugin out — Plugin out is the instance of the user's Plugin.lvclass being passed out. error out — The error out cluster passes error or warning information out of a VI to be used by other VIs. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
| --- |

Parent topic:

Write Data VI

<!--NI_TOPIC bundle=flexlogger-labview-PDK-ref path=vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/datahelpers/write-1d-wfm-dbl-v2-vi.html language=enus -->
## TOPIC 00031: Write 1D Wfm (DBL)_v2 VI

- bundle_id: `flexlogger-labview-PDK-ref`
- source_path: `vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/datahelpers/write-1d-wfm-dbl-v2-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger-labview-PDK-ref/raw/resource/enus/vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/datahelpers/write-1d-wfm-dbl-v2-vi.html
- document_id: `flexlogger-labview-PDK-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Write channel data to FlexLogger as a 1D waveform. The order of the data written should reflect the order of the plugin's valid channels, which is typically the order in which the channels were created. The dt for the corresponding channels should be defined when creating the channel. If Auto Calcul

### Write 1D Wfm (DBL)_v2 VI

Write channel data to FlexLogger as a 1D waveform. The order of the data written should reflect the order of the plugin's valid channels, which is typically the order in which the channels were created. The dt for the corresponding channels should be defined when creating the channel.

If **Auto Calculate T0** is true, T0 of the first waveform after Configure Session.vi is called will be used to calculate subsequent T0 values. If the first waveform T0 value is 0, the time when Configure Session.vi completed will be used. Subsequent T0 values are calculated based on the previous T0 plus the previous waveform length multiplied by dt. The default is false and if the T0 is not an expected value, the VI will return errors.

[IMAGE alt='icon' src='write-1d-wfm-dbl-v2-vi.png']

#### Inputs/Outputs

| Auto Calculate T0 (f) — Auto Calculate T0 determines whether to automatically calculate and override the t0 of the waveform. If Auto Calculate T0 is TRUE, the t0 of the first waveform after Configure Session.vi is called will be used to calculate subsequent t0 values. If the first waveform t0 value is 0, the time when Configure Session.vi completed will be used. Subsequent t0 values are calculated based on the previous t0 plus the previous waveform length multiplied by dt. The default is FALSE, which will not modify the t0 value of the waveform, but this VI will return an error if the waveform is not continuous. Plugin in — Plugin In is the instance of the user's Plugin.lvclass being passed in. Data — Data is the data in the specified format. error in (no error) — The error in cluster can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. Plugin out — Plugin out is the instance of the user's Plugin.lvclass being passed out. error out — The error out cluster passes error or warning information out of a VI to be used by other VIs. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
| --- |

Parent topic:

Write Data VI

<!--NI_TOPIC bundle=flexlogger-labview-PDK-ref path=vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/datahelpers/write-1d-wfm-digital-v2-vi.html language=enus -->
## TOPIC 00032: Write 1D Wfm (Digital)_v2 VI

- bundle_id: `flexlogger-labview-PDK-ref`
- source_path: `vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/datahelpers/write-1d-wfm-digital-v2-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger-labview-PDK-ref/raw/resource/enus/vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/datahelpers/write-1d-wfm-digital-v2-vi.html
- document_id: `flexlogger-labview-PDK-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Write channel data to FlexLogger as a 1D waveform. The order of the data written should reflect the order of the plugin's valid channels, which is typically the order in which the channels were created. The dt for the corresponding channels should be defined when creating the channel. If Auto Calcul

### Write 1D Wfm (Digital)_v2 VI

Write channel data to FlexLogger as a 1D waveform. The order of the data written should reflect the order of the plugin's valid channels, which is typically the order in which the channels were created. The dt for the corresponding channels should be defined when creating the channel.

If **Auto Calculate T0** is true, T0 of the first waveform after Configure Session.vi is called will be used to calculate subsequent T0 values. If the first waveform T0 value is 0, the time when Configure Session.vi completed will be used. Subsequent T0 values are calculated based on the previous T0 plus the previous waveform length multiplied by dt. The default is false and if the T0 is not an expected value, the VI will return errors.

[IMAGE alt='icon' src='write-1d-wfm-digital-v2-vi.png']

#### Inputs/Outputs

| Auto Calculate T0 (f) — Auto Calculate T0 determines whether to automatically calculate and override the t0 of the waveform. If Auto Calculate T0 is TRUE, the t0 of the first waveform after Configure Session.vi is called will be used to calculate subsequent t0 values. If the first waveform t0 value is 0, the time when Configure Session.vi completed will be used. Subsequent t0 values are calculated based on the previous t0 plus the previous waveform length multiplied by dt. The default is FALSE, which will not modify the t0 value of the waveform, but this VI will return an error if the waveform is not continuous. Plugin in — Plugin In is the instance of the user's Plugin.lvclass being passed in. Data — Data is the data in the specified format. error in (no error) — The error in cluster can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. Plugin out — Plugin out is the instance of the user's Plugin.lvclass being passed out. error out — The error out cluster passes error or warning information out of a VI to be used by other VIs. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
| --- |

Parent topic:

Write Data VI

<!--NI_TOPIC bundle=flexlogger-labview-PDK-ref path=vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/datahelpers/write-2d-bool-nchan-nsamples-vi.html language=enus -->
## TOPIC 00033: Write 2D Bool (NChan NSamples) VI

- bundle_id: `flexlogger-labview-PDK-ref`
- source_path: `vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/datahelpers/write-2d-bool-nchan-nsamples-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger-labview-PDK-ref/raw/resource/enus/vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/datahelpers/write-2d-bool-nchan-nsamples-vi.html
- document_id: `flexlogger-labview-PDK-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Write channel data to FlexLogger as a 2D array of samples. The order of the data written should reflect the order of the plugin's valid channels, which is typically the order in which the channels were created. The timing information for this data is defined by Set Stream Timing.vi. icon Inputs/Outp

### Write 2D Bool (NChan NSamples) VI

Write channel data to FlexLogger as a 2D array of samples. The order of the data written should reflect the order of the plugin's valid channels, which is typically the order in which the channels were created. The timing information for this data is defined by Set Stream Timing.vi.

[IMAGE alt='icon' src='write-2d-bool-nchan-nsamples-vi.png']

#### Inputs/Outputs

| Plugin in — Plugin In is the instance of the user's Plugin.lvclass being passed in. Data — Data is the data in the specified format. error in (no error) — The error in cluster can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. Plugin out — Plugin out is the instance of the user's Plugin.lvclass being passed out. error out — The error out cluster passes error or warning information out of a VI to be used by other VIs. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
| --- |

Parent topic:

Write Data VI

<!--NI_TOPIC bundle=flexlogger-labview-PDK-ref path=vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/datahelpers/write-2d-dbl-nchan-nsamples-vi.html language=enus -->
## TOPIC 00034: Write 2D DBL (NChan NSamples) VI

- bundle_id: `flexlogger-labview-PDK-ref`
- source_path: `vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/datahelpers/write-2d-dbl-nchan-nsamples-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger-labview-PDK-ref/raw/resource/enus/vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/datahelpers/write-2d-dbl-nchan-nsamples-vi.html
- document_id: `flexlogger-labview-PDK-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Write channel data to FlexLogger as a 2D array of samples. The order of the data written should reflect the order of the plugin's valid channels, which is typically the order in which the channels were created. The timing information for this data is defined by Set Stream Timing.vi. icon Inputs/Outp

### Write 2D DBL (NChan NSamples) VI

Write channel data to FlexLogger as a 2D array of samples. The order of the data written should reflect the order of the plugin's valid channels, which is typically the order in which the channels were created. The timing information for this data is defined by Set Stream Timing.vi.

[IMAGE alt='icon' src='write-2d-dbl-nchan-nsamples-vi.png']

#### Inputs/Outputs

| Plugin in — Plugin In is the instance of the user's Plugin.lvclass being passed in. Data — Data is the data in the specified format. error in (no error) — The error in cluster can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. Plugin out — Plugin out is the instance of the user's Plugin.lvclass being passed out. error out — The error out cluster passes error or warning information out of a VI to be used by other VIs. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
| --- |

Parent topic:

Write Data VI

<!--NI_TOPIC bundle=flexlogger-labview-PDK-ref path=vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/datahelpers/write-data-vi.html language=enus -->
## TOPIC 00035: Write Data VI

- bundle_id: `flexlogger-labview-PDK-ref`
- source_path: `vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/datahelpers/write-data-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger-labview-PDK-ref/raw/resource/enus/vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/datahelpers/write-data-vi.html
- document_id: `flexlogger-labview-PDK-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Write channel data to FlexLogger. The order of the data written should reflect the order of the plugin's valid channels, which is typically the order in which the channels were created. icon

### Write Data VI

Write channel data to FlexLogger. The order of the data written should reflect the order of the plugin's valid channels, which is typically the order in which the channels were created.

[IMAGE alt='icon' src='write-data-vi.png']

- [Write 1D DBL (NChan 1Sample) VI](../../../../../../../../vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/datahelpers/write-1d-dbl-nchan-1sample-vi.html) Write channel data to FlexLogger as a 1D array of samples. The order of the data written should reflect the order of the plugin's valid channels, which is typically the order in which the channels were created. The timing information for this data is defined by Set Stream Timing.vi.
- [Write 2D DBL (NChan NSamples) VI](../../../../../../../../vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/datahelpers/write-2d-dbl-nchan-nsamples-vi.html) Write channel data to FlexLogger as a 2D array of samples. The order of the data written should reflect the order of the plugin's valid channels, which is typically the order in which the channels were created. The timing information for this data is defined by Set Stream Timing.vi.
- [Write 1D Wfm (DBL)_v2 VI](../../../../../../../../vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/datahelpers/write-1d-wfm-dbl-v2-vi.html) Write channel data to FlexLogger as a 1D waveform. The order of the data written should reflect the order of the plugin's valid channels, which is typically the order in which the channels were created. The dt for the corresponding channels should be defined when creating the channel. If Auto Calculate T0 is true, T0 of the first waveform after Configure Session.vi is called will be used to calculate subsequent T0 values. If the first waveform T0 value is 0, the time when Configure Session.vi completed will be used. Subsequent T0 values are calculated based on the previous T0 plus the previous waveform length multiplied by dt. The default is false and if the T0 is not an expected value, the VI will return errors.
- [Write 1D Bool (NChan 1 Sample) VI](../../../../../../../../vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/datahelpers/write-1d-bool-nchan-1-sample-vi.html) Write channel data to FlexLogger as a 1D array of samples. The order of the data written should reflect the order of the plugin's valid channels, which is typically the order in which the channels were created. The timing information for this data is defined by Set Stream Timing.vi.
- [Write 2D Bool (NChan NSamples) VI](../../../../../../../../vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/datahelpers/write-2d-bool-nchan-nsamples-vi.html) Write channel data to FlexLogger as a 2D array of samples. The order of the data written should reflect the order of the plugin's valid channels, which is typically the order in which the channels were created. The timing information for this data is defined by Set Stream Timing.vi.
- [Write 1D Wfm (Digital)_v2 VI](../../../../../../../../vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/datahelpers/write-1d-wfm-digital-v2-vi.html) Write channel data to FlexLogger as a 1D waveform. The order of the data written should reflect the order of the plugin's valid channels, which is typically the order in which the channels were created. The dt for the corresponding channels should be defined when creating the channel. If Auto Calculate T0 is true, T0 of the first waveform after Configure Session.vi is called will be used to calculate subsequent T0 values. If the first waveform T0 value is 0, the time when Configure Session.vi completed will be used. Subsequent T0 values are calculated based on the previous T0 plus the previous waveform length multiplied by dt. The default is false and if the T0 is not an expected value, the VI will return errors.
- [Write 1D STR (NChan 1 Sample) VI](../../../../../../../../vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/datahelpers/write-1d-str-nchan-1-sample-vi.html) Write channel data to FlexLogger as a 1D array of strings. The order of the data written should reflect the order of the plugin's valid channels, which is typically the order in which the channels were created. If the Time Stamps are not provided, the VI will compute them automatically using the timing information configured by Set Stream Timing.vi.

Parent topic:

Plug-In Development

<!--NI_TOPIC bundle=flexlogger-labview-PDK-ref path=vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/get-data-from-stream2-vi.html language=enus -->
## TOPIC 00036: Get Data from Stream2 VI

- bundle_id: `flexlogger-labview-PDK-ref`
- source_path: `vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/get-data-from-stream2-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger-labview-PDK-ref/raw/resource/enus/vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/get-data-from-stream2-vi.html
- document_id: `flexlogger-labview-PDK-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: This polymorphic VI contains several options for retrieving specfic pieces of data based on a specific unique identifier (either of a channel or parameter). Each individual VI takes a unique identifier and the results of either a setpoint or waveform read. icon

### Get Data from Stream2 VI

This polymorphic VI contains several options for retrieving specfic pieces of data based on a specific unique identifier (either of a channel or parameter). Each individual VI takes a unique identifier and the results of either a setpoint or waveform read.

[IMAGE alt='icon' src='get-data-from-stream2-vi.png']

- [Get Setpoint VI](../../../../../../../vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/get-setpoint-vi.html) Returns the subset of values that correspond to a particular unique identifier from the set of values returned by a Read Setpoint call. This works for both Plugin setpoints and Channel setpoints. If there are multiple setpoints associated with the unique identifier, only the first will be returned.
- [Get Setpoints VI](../../../../../../../vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/get-setpoints-vi.html) Returns the subset of values that correspond to a particular unique identifier from the set of values returned by a Read Setpoint call. This works for both Plugin setpoints and Channel setpoints.
- [Get Waveform VI](../../../../../../../vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/get-waveform-vi.html) Returns the subset of values returned by a Read 1D Wfm call that match the unique identifier. This works for both Plugin waveforms and Channel waveforms. If there are multiple waveforms associated with the unique identifier, only the first will be returned. Note: For Channel waveforms, use a colon in the unique identifier to specify a specific channel waveform (i.e. <channel identifier>:<waveform parameter name>), otherwise all waveforms associated with the unique identifier will be returned.
- [Get Waveforms VI](../../../../../../../vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/get-waveforms-vi.html) Returns the subset of values returned by a Read 1D Wfm call that match the unique identifier. This works for both Plugin waveforms and Channel waveforms. Note: For Channel waveforms, use a colon in the unique identifier to specify a specific channel waveform (i.e. <channel identifier>:<waveform parameter name>), otherwise all waveforms associated with the unique identifier will be returned.
- [Get Digital Setpoint VI](../../../../../../../vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/get-digital-setpoint-vi.html) Returns the subset of values returned by a Read Setpoint call that correspond to the unique identifier. This works for both Plugin setpoints and Channel setpoints. If there are multiple setpoints associated with the unique identifier, only the first will be returned.
- [Get Digital Setpoints VI](../../../../../../../vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/get-digital-setpoints-vi.html) Returns the subset of values that correspond to a particular unique identifier from the set of values returned by a Read Setpoint call. This works for both Plugin setpoints and Channel setpoints.
- [Get Digital Waveform VI](../../../../../../../vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/get-digital-waveform-vi.html) Returns the subset of values returned by a Read 1D Wfm (Digital) call that match the unique identifier. This works for both Plugin waveforms and Channel waveforms. If there are multiple waveforms associated with the unique identifier, only the first will be returned. Note: For Channel waveforms, use a colon in the unique identifier to specify a specific channel waveform (i.e. <channel identifier>:<waveform parameter name>), otherwise all waveforms associated with the unique identifier will be returned.
- [Get Digital Waveforms VI](../../../../../../../vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/get-digital-waveforms-vi.html) Returns the subset of values returned by a Read 1D Wfm (Digital) call that match the unique identifier. This works for both Plugin waveforms and Channel waveforms. Note: For Channel waveforms, use a colon in the unique identifier to specify a specific channel waveform (i.e. <channel identifier>:<waveform parameter name>), otherwise all waveforms associated with the unique identifier will be returned.

Parent topic:

Advanced

<!--NI_TOPIC bundle=flexlogger-labview-PDK-ref path=vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/get-digital-setpoint-vi.html language=enus -->
## TOPIC 00037: Get Digital Setpoint VI

- bundle_id: `flexlogger-labview-PDK-ref`
- source_path: `vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/get-digital-setpoint-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger-labview-PDK-ref/raw/resource/enus/vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/get-digital-setpoint-vi.html
- document_id: `flexlogger-labview-PDK-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the subset of values returned by a Read Setpoint call that correspond to the unique identifier. This works for both Plugin setpoints and Channel setpoints. If there are multiple setpoints associated with the unique identifier, only the first will be returned. icon Inputs/Outputs cPluginSDK_l

### Get Digital Setpoint VI

Returns the subset of values returned by a Read Setpoint call that correspond to the unique identifier. This works for both Plugin setpoints and Channel setpoints. If there are multiple setpoints associated with the unique identifier, only the first will be returned.

[IMAGE alt='icon' src='get-digital-setpoint-vi.png']

#### Inputs/Outputs

| Plugin in — Plugin In is the instance of the user's Plugin.lvclass being passed in. Unique Identifier — Unique Identifier is the unique identifier for the channel. Stream Names — Stream Names are the names of the data streams returned when reading data. Stream Values — Stream Values are the values corresponding to the Stream Names. Stream Values and Stream Names should be the same length, where every name in Stream Names has a corresponding value at the same index in Stream Values. error in (no error) — The error in cluster can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. Plugin out — Plugin out is the instance of the user's Plugin.lvclass being passed out. Value — Value is the value for this parameter or setpoint. Found? — found returns TRUE if the data was found. error out — The error out cluster passes error or warning information out of a VI to be used by other VIs. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
| --- |

Parent topic:

Get Data from Stream2 VI

<!--NI_TOPIC bundle=flexlogger-labview-PDK-ref path=vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/get-digital-setpoints-vi.html language=enus -->
## TOPIC 00038: Get Digital Setpoints VI

- bundle_id: `flexlogger-labview-PDK-ref`
- source_path: `vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/get-digital-setpoints-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger-labview-PDK-ref/raw/resource/enus/vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/get-digital-setpoints-vi.html
- document_id: `flexlogger-labview-PDK-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the subset of values that correspond to a particular unique identifier from the set of values returned by a Read Setpoint call. This works for both Plugin setpoints and Channel setpoints. icon Inputs/Outputs cPluginSDK_lvlibp_Pluginlvclass.png Plugin in Plugin In is the instance of the user'

### Get Digital Setpoints VI

Returns the subset of values that correspond to a particular unique identifier from the set of values returned by a Read Setpoint call. This works for both Plugin setpoints and Channel setpoints.

[IMAGE alt='icon' src='get-digital-setpoints-vi.png']

#### Inputs/Outputs

| Plugin in — Plugin In is the instance of the user's Plugin.lvclass being passed in. Unique Identifier — Unique Identifier is the unique identifier for the channel. Stream Names — Stream Names are the names of the data streams returned when reading data. Stream Values — Stream Values are the values corresponding to the Stream Names. Stream Values and Stream Names should be the same length, where every name in Stream Names has a corresponding value at the same index in Stream Values. error in (no error) — The error in cluster can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. Plugin out — Plugin out is the instance of the user's Plugin.lvclass being passed out. Values — Values are the latest values for the setpoint channels. Found? — found returns TRUE if the data was found. error out — The error out cluster passes error or warning information out of a VI to be used by other VIs. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
| --- |

Parent topic:

Get Data from Stream2 VI

<!--NI_TOPIC bundle=flexlogger-labview-PDK-ref path=vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/get-digital-waveform-vi.html language=enus -->
## TOPIC 00039: Get Digital Waveform VI

- bundle_id: `flexlogger-labview-PDK-ref`
- source_path: `vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/get-digital-waveform-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger-labview-PDK-ref/raw/resource/enus/vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/get-digital-waveform-vi.html
- document_id: `flexlogger-labview-PDK-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the subset of values returned by a Read 1D Wfm (Digital) call that match the unique identifier. This works for both Plugin waveforms and Channel waveforms. If there are multiple waveforms associated with the unique identifier, only the first will be returned. Note: For Channel waveforms, use

### Get Digital Waveform VI

Returns the subset of values returned by a Read 1D Wfm (Digital) call that match the unique identifier. This works for both Plugin waveforms and Channel waveforms. If there are multiple waveforms associated with the unique identifier, only the first will be returned.

**Note:** For Channel waveforms, use a colon in the unique identifier to specify a specific channel waveform (i.e. <channel identifier>:<waveform parameter name>), otherwise all waveforms associated with the unique identifier will be returned.

[IMAGE alt='icon' src='get-digital-waveform-vi.png']

#### Inputs/Outputs

| Plugin in — Plugin In is the instance of the user's Plugin.lvclass being passed in. Unique Identifier — Unique Identifier is the unique identifier for the channel. Stream Names — Stream Names are the names of the data streams returned when reading data. Stream Values — Stream Values are the values corresponding to the Stream Names. Stream Values and Stream Names should be the same length, where every name in Stream Names has a corresponding value at the same index in Stream Values. error in (no error) — The error in cluster can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. Plugin out — Plugin out is the instance of the user's Plugin.lvclass being passed out. Waveform — Waveform is the waveform data being read. Found? — found returns TRUE if the data was found. error out — The error out cluster passes error or warning information out of a VI to be used by other VIs. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
| --- |

Parent topic:

Get Data from Stream2 VI

<!--NI_TOPIC bundle=flexlogger-labview-PDK-ref path=vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/get-digital-waveforms-vi.html language=enus -->
## TOPIC 00040: Get Digital Waveforms VI

- bundle_id: `flexlogger-labview-PDK-ref`
- source_path: `vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/get-digital-waveforms-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger-labview-PDK-ref/raw/resource/enus/vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/get-digital-waveforms-vi.html
- document_id: `flexlogger-labview-PDK-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the subset of values returned by a Read 1D Wfm (Digital) call that match the unique identifier. This works for both Plugin waveforms and Channel waveforms. Note: For Channel waveforms, use a colon in the unique identifier to specify a specific channel waveform (i.e. <channel identifier>:<wav

### Get Digital Waveforms VI

Returns the subset of values returned by a Read 1D Wfm (Digital) call that match the unique identifier. This works for both Plugin waveforms and Channel waveforms.

**Note:** For Channel waveforms, use a colon in the unique identifier to specify a specific channel waveform (i.e. <channel identifier>:<waveform parameter name>), otherwise all waveforms associated with the unique identifier will be returned.

[IMAGE alt='icon' src='get-digital-waveforms-vi.png']

#### Inputs/Outputs

| Plugin in — Plugin In is the instance of the user's Plugin.lvclass being passed in. Unique Identifier — Unique Identifier is the unique identifier for the channel. Stream Names — Stream Names are the names of the data streams returned when reading data. Stream Values — Stream Values are the values corresponding to the Stream Names. Stream Values and Stream Names should be the same length, where every name in Stream Names has a corresponding value at the same index in Stream Values. error in (no error) — The error in cluster can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. Plugin out — Plugin out is the instance of the user's Plugin.lvclass being passed out. Waveforms — Waveforms is the array of waveform data being read. Found? — found returns TRUE if the data was found. error out — The error out cluster passes error or warning information out of a VI to be used by other VIs. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
| --- |

Parent topic:

Get Data from Stream2 VI

<!--NI_TOPIC bundle=flexlogger-labview-PDK-ref path=vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/get-setpoint-vi.html language=enus -->
## TOPIC 00041: Get Setpoint VI

- bundle_id: `flexlogger-labview-PDK-ref`
- source_path: `vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/get-setpoint-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger-labview-PDK-ref/raw/resource/enus/vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/get-setpoint-vi.html
- document_id: `flexlogger-labview-PDK-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the subset of values that correspond to a particular unique identifier from the set of values returned by a Read Setpoint call. This works for both Plugin setpoints and Channel setpoints. If there are multiple setpoints associated with the unique identifier, only the first will be returned.

### Get Setpoint VI

Returns the subset of values that correspond to a particular unique identifier from the set of values returned by a Read Setpoint call. This works for both Plugin setpoints and Channel setpoints. If there are multiple setpoints associated with the unique identifier, only the first will be returned.

[IMAGE alt='icon' src='get-setpoint-vi.png']

#### Inputs/Outputs

| Plugin in — Plugin In is the instance of the user's Plugin.lvclass being passed in. Unique Identifier — Unique Identifier is the unique identifier for the channel. Stream Names — Stream Names are the names of the data streams returned when reading data. Stream Values — Stream Values are the values corresponding to the Stream Names. Stream Values and Stream Names should be the same length, where every name in Stream Names has a corresponding value at the same index in Stream Values. error in (no error) — The error in cluster can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. Plugin out — Plugin out is the instance of the user's Plugin.lvclass being passed out. Value — Value is the value for this parameter or setpoint. Found? — found returns TRUE if the data was found. error out — The error out cluster passes error or warning information out of a VI to be used by other VIs. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
| --- |

Parent topic:

Get Data from Stream2 VI

<!--NI_TOPIC bundle=flexlogger-labview-PDK-ref path=vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/get-setpoints-vi.html language=enus -->
## TOPIC 00042: Get Setpoints VI

- bundle_id: `flexlogger-labview-PDK-ref`
- source_path: `vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/get-setpoints-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger-labview-PDK-ref/raw/resource/enus/vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/get-setpoints-vi.html
- document_id: `flexlogger-labview-PDK-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the subset of values that correspond to a particular unique identifier from the set of values returned by a Read Setpoint call. This works for both Plugin setpoints and Channel setpoints. icon Inputs/Outputs cPluginSDK_lvlibp_Pluginlvclass.png Plugin in Plugin In is the instance of the user'

### Get Setpoints VI

Returns the subset of values that correspond to a particular unique identifier from the set of values returned by a Read Setpoint call. This works for both Plugin setpoints and Channel setpoints.

[IMAGE alt='icon' src='get-setpoints-vi.png']

#### Inputs/Outputs

| Plugin in — Plugin In is the instance of the user's Plugin.lvclass being passed in. Unique Identifier — Unique Identifier is the unique identifier for the channel. Stream Names — Stream Names are the names of the data streams returned when reading data. Stream Values — Stream Values are the values corresponding to the Stream Names. Stream Values and Stream Names should be the same length, where every name in Stream Names has a corresponding value at the same index in Stream Values. error in (no error) — The error in cluster can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. Plugin out — Plugin out is the instance of the user's Plugin.lvclass being passed out. Values — Values are the latest values for the setpoint channels. Found? — found returns TRUE if the data was found. error out — The error out cluster passes error or warning information out of a VI to be used by other VIs. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
| --- |

Parent topic:

Get Data from Stream2 VI

<!--NI_TOPIC bundle=flexlogger-labview-PDK-ref path=vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/get-valid-channels-vi.html language=enus -->
## TOPIC 00043: Get Valid Channels VI

- bundle_id: `flexlogger-labview-PDK-ref`
- source_path: `vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/get-valid-channels-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger-labview-PDK-ref/raw/resource/enus/vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/get-valid-channels-vi.html
- document_id: `flexlogger-labview-PDK-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Get all non-disabled channels for the plugin. The list of channels can be used when reading the latest channel-specific parameters to determine which channel data to send to FlexLogger and how to send it. Plugin developers determine if channels can be disabled on with the option in the constructor f

### Get Valid Channels VI

Get all non-disabled channels for the plugin. The list of channels can be used when reading the latest channel-specific parameters to determine which channel data to send to FlexLogger and how to send it. Plugin developers determine if channels can be disabled on with the option in the constructor for the respective channel.

[IMAGE alt='icon' src='get-valid-channels-vi.png']

#### Inputs/Outputs

| Plugin in — Plugin In is the instance of the user's Plugin.lvclass being passed in. error in (no error) — The error in cluster can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. Plugin out — Plugin out is the instance of the user's Plugin.lvclass being passed out. Channels — Channels is an array of channel objects of type Channel.lvclass. error out — The error out cluster passes error or warning information out of a VI to be used by other VIs. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
| --- |

Parent topic:

Plug-In Development

<!--NI_TOPIC bundle=flexlogger-labview-PDK-ref path=vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/get-waveform-vi.html language=enus -->
## TOPIC 00044: Get Waveform VI

- bundle_id: `flexlogger-labview-PDK-ref`
- source_path: `vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/get-waveform-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger-labview-PDK-ref/raw/resource/enus/vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/get-waveform-vi.html
- document_id: `flexlogger-labview-PDK-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the subset of values returned by a Read 1D Wfm call that match the unique identifier. This works for both Plugin waveforms and Channel waveforms. If there are multiple waveforms associated with the unique identifier, only the first will be returned. Note: For Channel waveforms, use a colon i

### Get Waveform VI

Returns the subset of values returned by a Read 1D Wfm call that match the unique identifier. This works for both Plugin waveforms and Channel waveforms. If there are multiple waveforms associated with the unique identifier, only the first will be returned.

**Note:** For Channel waveforms, use a colon in the unique identifier to specify a specific channel waveform (i.e. <channel identifier>:<waveform parameter name>), otherwise all waveforms associated with the unique identifier will be returned.

[IMAGE alt='icon' src='get-waveform-vi.png']

#### Inputs/Outputs

| Plugin in — Plugin In is the instance of the user's Plugin.lvclass being passed in. Unique Identifier — Unique Identifier is the unique identifier for the channel. Stream Names — Stream Names are the names of the data streams returned when reading data. Stream Values — Stream Values are the values corresponding to the Stream Names. Stream Values and Stream Names should be the same length, where every name in Stream Names has a corresponding value at the same index in Stream Values. error in (no error) — The error in cluster can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. Plugin out — Plugin out is the instance of the user's Plugin.lvclass being passed out. Waveform — Waveform is the waveform data being read. Found? — found returns TRUE if the data was found. error out — The error out cluster passes error or warning information out of a VI to be used by other VIs. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
| --- |

Parent topic:

Get Data from Stream2 VI

<!--NI_TOPIC bundle=flexlogger-labview-PDK-ref path=vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/get-waveforms-vi.html language=enus -->
## TOPIC 00045: Get Waveforms VI

- bundle_id: `flexlogger-labview-PDK-ref`
- source_path: `vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/get-waveforms-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger-labview-PDK-ref/raw/resource/enus/vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/get-waveforms-vi.html
- document_id: `flexlogger-labview-PDK-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the subset of values returned by a Read 1D Wfm call that match the unique identifier. This works for both Plugin waveforms and Channel waveforms. Note: For Channel waveforms, use a colon in the unique identifier to specify a specific channel waveform (i.e. <channel identifier>:<waveform para

### Get Waveforms VI

Returns the subset of values returned by a Read 1D Wfm call that match the unique identifier. This works for both Plugin waveforms and Channel waveforms.

**Note:** For Channel waveforms, use a colon in the unique identifier to specify a specific channel waveform (i.e. <channel identifier>:<waveform parameter name>), otherwise all waveforms associated with the unique identifier will be returned.

[IMAGE alt='icon' src='get-waveforms-vi.png']

#### Inputs/Outputs

| Plugin in — Plugin In is the instance of the user's Plugin.lvclass being passed in. Unique Identifier — Unique Identifier is the unique identifier for the channel. Stream Names — Stream Names are the names of the data streams returned when reading data. Stream Values — Stream Values are the values corresponding to the Stream Names. Stream Values and Stream Names should be the same length, where every name in Stream Names has a corresponding value at the same index in Stream Values. error in (no error) — The error in cluster can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. Plugin out — Plugin out is the instance of the user's Plugin.lvclass being passed out. Waveforms — Waveforms is the array of waveform data being read. Found? — found returns TRUE if the data was found. error out — The error out cluster passes error or warning information out of a VI to be used by other VIs. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
| --- |

Parent topic:

Get Data from Stream2 VI

<!--NI_TOPIC bundle=flexlogger-labview-PDK-ref path=vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/log-event-vi.html language=enus -->
## TOPIC 00046: Log Event VI

- bundle_id: `flexlogger-labview-PDK-ref`
- source_path: `vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/log-event-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger-labview-PDK-ref/raw/resource/enus/vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/log-event-vi.html
- document_id: `flexlogger-labview-PDK-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: This VI writes an event string into the Alarms and Events channel in the log file. It can be used to make notes from a plugin during test execution. icon Inputs/Outputs cPluginSDK_lvlibp_Pluginlvclass.png Plugin in Plugin In is the instance of the user's Plugin.lvclass being passed in. cstr.png Mess

### Log Event VI

This VI writes an event string into the Alarms and Events channel in the log file. It can be used to make notes from a plugin during test execution.

[IMAGE alt='icon' src='log-event-vi.png']

#### Inputs/Outputs

| Plugin in — Plugin In is the instance of the user's Plugin.lvclass being passed in. Message — Message is the message string to write. error in (no error) — The error in cluster can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. Plugin out — Plugin out is the instance of the user's Plugin.lvclass being passed out. error out — The error out cluster passes error or warning information out of a VI to be used by other VIs. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
| --- |

Parent topic:

Advanced

<!--NI_TOPIC bundle=flexlogger-labview-PDK-ref path=vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/parameteraccess/read-boolean-vi.html language=enus -->
## TOPIC 00047: Read Boolean VI

- bundle_id: `flexlogger-labview-PDK-ref`
- source_path: `vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/parameteraccess/read-boolean-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger-labview-PDK-ref/raw/resource/enus/vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/parameteraccess/read-boolean-vi.html
- document_id: `flexlogger-labview-PDK-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Read the latest plugin-level parameter value from FlexLogger as a boolean operation. The parameter must first be created by a call of matching name and data type. icon Inputs/Outputs cPluginSDK_lvlibp_Pluginlvclass.png Plugin in Plugin In is the instance of the user's Plugin.lvclass being passed in.

### Read Boolean VI

Read the latest plugin-level parameter value from FlexLogger as a boolean operation. The parameter must first be created by a call of matching name and data type.

[IMAGE alt='icon' src='read-boolean-vi.png']

#### Inputs/Outputs

| Plugin in — Plugin In is the instance of the user's Plugin.lvclass being passed in. Name — Name is the name of the parameter. error in (no error) — The error in cluster can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. Plugin out — Plugin out is the instance of the user's Plugin.lvclass being passed out. Value — Value is the value for this parameter or setpoint. Found — found returns TRUE if the parameter was found. error out — The error out cluster passes error or warning information out of a VI to be used by other VIs. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
| --- |

Parent topic:

Read Parameter VI

<!--NI_TOPIC bundle=flexlogger-labview-PDK-ref path=vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/parameteraccess/read-dbl-vi.html language=enus -->
## TOPIC 00048: Read DBL VI

- bundle_id: `flexlogger-labview-PDK-ref`
- source_path: `vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/parameteraccess/read-dbl-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger-labview-PDK-ref/raw/resource/enus/vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/parameteraccess/read-dbl-vi.html
- document_id: `flexlogger-labview-PDK-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Read the latest plugin-level parameter value from FlexLogger as a double-precision, floating-point numeric. The parameter must first be created by a call of matching name and data type. icon Inputs/Outputs cPluginSDK_lvlibp_Pluginlvclass.png Plugin in Plugin In is the instance of the user's Plugin.l

### Read DBL VI

Read the latest plugin-level parameter value from FlexLogger as a double-precision, floating-point numeric. The parameter must first be created by a call of matching name and data type.

[IMAGE alt='icon' src='read-dbl-vi.png']

#### Inputs/Outputs

| Plugin in — Plugin In is the instance of the user's Plugin.lvclass being passed in. Name — Name is the name of the parameter. error in (no error) — The error in cluster can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. Plugin out — Plugin out is the instance of the user's Plugin.lvclass being passed out. Value — Value is the value for this parameter or setpoint. Found — found returns TRUE if the parameter was found. error out — The error out cluster passes error or warning information out of a VI to be used by other VIs. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
| --- |

Parent topic:

Read Parameter VI

<!--NI_TOPIC bundle=flexlogger-labview-PDK-ref path=vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/parameteraccess/read-enum-vi.html language=enus -->
## TOPIC 00049: Read Enum VI

- bundle_id: `flexlogger-labview-PDK-ref`
- source_path: `vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/parameteraccess/read-enum-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger-labview-PDK-ref/raw/resource/enus/vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/parameteraccess/read-enum-vi.html
- document_id: `flexlogger-labview-PDK-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Read the latest plugin-level parameter value from FlexLogger as an enumerated constant. The parameter must first be created by a call of matching name and data type. icon Inputs/Outputs cPluginSDK_lvlibp_Pluginlvclass.png Plugin in Plugin In is the instance of the user's Plugin.lvclass being passed

### Read Enum VI

Read the latest plugin-level parameter value from FlexLogger as an enumerated constant. The parameter must first be created by a call of matching name and data type.

[IMAGE alt='icon' src='read-enum-vi.png']

#### Inputs/Outputs

| Plugin in — Plugin In is the instance of the user's Plugin.lvclass being passed in. Name — Name is the name of the parameter. error in (no error) — The error in cluster can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. Found — found returns TRUE if the parameter was found. Plugin out — Plugin out is the instance of the user's Plugin.lvclass being passed out. Value — Value is the value for this parameter or setpoint. Index — Index is the index value of the enum. error out — The error out cluster passes error or warning information out of a VI to be used by other VIs. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
| --- |

Parent topic:

Read Parameter VI

<!--NI_TOPIC bundle=flexlogger-labview-PDK-ref path=vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/parameteraccess/read-i32-vi.html language=enus -->
## TOPIC 00050: Read I32 VI

- bundle_id: `flexlogger-labview-PDK-ref`
- source_path: `vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/parameteraccess/read-i32-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger-labview-PDK-ref/raw/resource/enus/vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/parameteraccess/read-i32-vi.html
- document_id: `flexlogger-labview-PDK-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Read the latest plugin-level parameter value from FlexLogger as a 32-bit long signed integer. The parameter must first be created by a call of matching name and data type. icon Inputs/Outputs cPluginSDK_lvlibp_Pluginlvclass.png Plugin in Plugin In is the instance of the user's Plugin.lvclass being p

### Read I32 VI

Read the latest plugin-level parameter value from FlexLogger as a 32-bit long signed integer. The parameter must first be created by a call of matching name and data type.

[IMAGE alt='icon' src='read-i32-vi.png']

#### Inputs/Outputs

| Plugin in — Plugin In is the instance of the user's Plugin.lvclass being passed in. Name — Name is the name of the parameter. error in (no error) — The error in cluster can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. Plugin out — Plugin out is the instance of the user's Plugin.lvclass being passed out. Value — Value is the value for this parameter or setpoint. Found — found returns TRUE if the parameter was found. error out — The error out cluster passes error or warning information out of a VI to be used by other VIs. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
| --- |

Parent topic:

Read Parameter VI

<!--NI_TOPIC bundle=flexlogger-labview-PDK-ref path=vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/parameteraccess/read-n-channel-vi.html language=enus -->
## TOPIC 00051: Read N Channel VI

- bundle_id: `flexlogger-labview-PDK-ref`
- source_path: `vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/parameteraccess/read-n-channel-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger-labview-PDK-ref/raw/resource/enus/vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/parameteraccess/read-n-channel-vi.html
- document_id: `flexlogger-labview-PDK-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Read the latest plugin-level parameter value from FlexLogger as a list of channel names. The parameter must first be created by a call of matching name and data type. icon Inputs/Outputs cPluginSDK_lvlibp_Pluginlvclass.png Plugin in Plugin In is the instance of the user's Plugin.lvclass being passed

### Read N Channel VI

Read the latest plugin-level parameter value from FlexLogger as a list of channel names. The parameter must first be created by a call of matching name and data type.

[IMAGE alt='icon' src='read-n-channel-vi.png']

#### Inputs/Outputs

| Plugin in — Plugin In is the instance of the user's Plugin.lvclass being passed in. Name (Unique Channel Identifier) — Name (Unique Channel Identifier) is the name of the parameter for the channel(s). error in (no error) — The error in cluster can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. Plugin out — Plugin out is the instance of the user's Plugin.lvclass being passed out. Channels — Channels is an array of channel objects of type Channel.lvclass. Found — found returns TRUE if the parameter was found. error out — The error out cluster passes error or warning information out of a VI to be used by other VIs. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
| --- |

Parent topic:

Read Parameter VI

<!--NI_TOPIC bundle=flexlogger-labview-PDK-ref path=vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/parameteraccess/read-n-digital-channels-vi.html language=enus -->
## TOPIC 00052: Read N Digital Channels VI

- bundle_id: `flexlogger-labview-PDK-ref`
- source_path: `vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/parameteraccess/read-n-digital-channels-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger-labview-PDK-ref/raw/resource/enus/vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/parameteraccess/read-n-digital-channels-vi.html
- document_id: `flexlogger-labview-PDK-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Read the latest plugin-level parameter value from FlexLogger. The value is multiple digital channel names. The parameter must first be created by a call of matching name and data type. icon Inputs/Outputs cPluginSDK_lvlibp_Pluginlvclass.png Plugin in Plugin In is the instance of the user's Plugin.lv

### Read N Digital Channels VI

Read the latest plugin-level parameter value from FlexLogger. The value is multiple digital channel names. The parameter must first be created by a call of matching name and data type.

[IMAGE alt='icon' src='read-n-digital-channels-vi.png']

#### Inputs/Outputs

| Plugin in — Plugin In is the instance of the user's Plugin.lvclass being passed in. Name (Unique Channel Identifier) — Name (Unique Channel Identifier) is the name of the parameter for the channel(s). error in (no error) — The error in cluster can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. Plugin out — Plugin out is the instance of the user's Plugin.lvclass being passed out. Channels — Channels is an array of channel objects of type Channel.lvclass. Found — found returns TRUE if the parameter was found. error out — The error out cluster passes error or warning information out of a VI to be used by other VIs. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
| --- |

Parent topic:

Read Parameter VI

<!--NI_TOPIC bundle=flexlogger-labview-PDK-ref path=vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/parameteraccess/read-parameter-vi.html language=enus -->
## TOPIC 00053: Read Parameter VI

- bundle_id: `flexlogger-labview-PDK-ref`
- source_path: `vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/parameteraccess/read-parameter-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger-labview-PDK-ref/raw/resource/enus/vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/parameteraccess/read-parameter-vi.html
- document_id: `flexlogger-labview-PDK-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Read the latest plugin-level parameter value from FlexLogger. The parameter must first be created by a call of matching name and data type. icon

### Read Parameter VI

Read the latest plugin-level parameter value from FlexLogger. The parameter must first be created by a call of matching name and data type.

[IMAGE alt='icon' src='read-parameter-vi.png']

- [Read I32 VI](../../../../../../../../vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/parameteraccess/read-i32-vi.html) Read the latest plugin-level parameter value from FlexLogger as a 32-bit long signed integer. The parameter must first be created by a call of matching name and data type.
- [Read String VI](../../../../../../../../vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/parameteraccess/read-string-vi.html) Read the latest plugin-level parameter value from FlexLogger as a text string. The parameter must first be created by a call of matching name and data type.
- [Read Boolean VI](../../../../../../../../vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/parameteraccess/read-boolean-vi.html) Read the latest plugin-level parameter value from FlexLogger as a boolean operation. The parameter must first be created by a call of matching name and data type.
- [Read Enum VI](../../../../../../../../vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/parameteraccess/read-enum-vi.html) Read the latest plugin-level parameter value from FlexLogger as an enumerated constant. The parameter must first be created by a call of matching name and data type.
- [Read DBL VI](../../../../../../../../vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/parameteraccess/read-dbl-vi.html) Read the latest plugin-level parameter value from FlexLogger as a double-precision, floating-point numeric. The parameter must first be created by a call of matching name and data type.
- [Read N Channel VI](../../../../../../../../vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/parameteraccess/read-n-channel-vi.html) Read the latest plugin-level parameter value from FlexLogger as a list of channel names. The parameter must first be created by a call of matching name and data type.
- [Read Single Channel VI](../../../../../../../../vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/parameteraccess/read-single-channel-vi.html) Read the latest plugin-level parameter value from FlexLogger. The value is a single channel name. The parameter must first be created by a call of matching name and data type.
- [Read N Digital Channels VI](../../../../../../../../vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/parameteraccess/read-n-digital-channels-vi.html) Read the latest plugin-level parameter value from FlexLogger. The value is multiple digital channel names. The parameter must first be created by a call of matching name and data type.
- [Read Single Digital Channel VI](../../../../../../../../vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/parameteraccess/read-single-digital-channel-vi.html) Read the latest plugin-level parameter value from FlexLogger. The value is a single digital channel name. The parameter must first be created by a call of matching name and data type.

Parent topic:

Plug-In Development

<!--NI_TOPIC bundle=flexlogger-labview-PDK-ref path=vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/parameteraccess/read-single-channel-vi.html language=enus -->
## TOPIC 00054: Read Single Channel VI

- bundle_id: `flexlogger-labview-PDK-ref`
- source_path: `vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/parameteraccess/read-single-channel-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger-labview-PDK-ref/raw/resource/enus/vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/parameteraccess/read-single-channel-vi.html
- document_id: `flexlogger-labview-PDK-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Read the latest plugin-level parameter value from FlexLogger. The value is a single channel name. The parameter must first be created by a call of matching name and data type. icon Inputs/Outputs cPluginSDK_lvlibp_Pluginlvclass.png Plugin in Plugin In is the instance of the user's Plugin.lvclass bei

### Read Single Channel VI

Read the latest plugin-level parameter value from FlexLogger. The value is a single channel name. The parameter must first be created by a call of matching name and data type.

[IMAGE alt='icon' src='read-single-channel-vi.png']

#### Inputs/Outputs

| Plugin in — Plugin In is the instance of the user's Plugin.lvclass being passed in. Name (Unique Channel Identifier) — Name (Unique Channel Identifier) is the name of the parameter for the channel(s). error in (no error) — The error in cluster can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. Plugin out — Plugin out is the instance of the user's Plugin.lvclass being passed out. Channel — Channel is the instance of the Channel.lvclass. Found — found returns TRUE if the parameter was found. error out — The error out cluster passes error or warning information out of a VI to be used by other VIs. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
| --- |

Parent topic:

Read Parameter VI

<!--NI_TOPIC bundle=flexlogger-labview-PDK-ref path=vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/parameteraccess/read-single-digital-channel-vi.html language=enus -->
## TOPIC 00055: Read Single Digital Channel VI

- bundle_id: `flexlogger-labview-PDK-ref`
- source_path: `vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/parameteraccess/read-single-digital-channel-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger-labview-PDK-ref/raw/resource/enus/vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/parameteraccess/read-single-digital-channel-vi.html
- document_id: `flexlogger-labview-PDK-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Read the latest plugin-level parameter value from FlexLogger. The value is a single digital channel name. The parameter must first be created by a call of matching name and data type. icon Inputs/Outputs cPluginSDK_lvlibp_Pluginlvclass.png Plugin in Plugin In is the instance of the user's Plugin.lvc

### Read Single Digital Channel VI

Read the latest plugin-level parameter value from FlexLogger. The value is a single digital channel name. The parameter must first be created by a call of matching name and data type.

[IMAGE alt='icon' src='read-single-digital-channel-vi.png']

#### Inputs/Outputs

| Plugin in — Plugin In is the instance of the user's Plugin.lvclass being passed in. Name (Unique Channel Identifier) — Name (Unique Channel Identifier) is the name of the parameter for the channel(s). error in (no error) — The error in cluster can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. Plugin out — Plugin out is the instance of the user's Plugin.lvclass being passed out. Channel — Channel is the instance of the Channel.lvclass. Found — found returns TRUE if the parameter was found. error out — The error out cluster passes error or warning information out of a VI to be used by other VIs. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
| --- |

Parent topic:

Read Parameter VI

<!--NI_TOPIC bundle=flexlogger-labview-PDK-ref path=vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/parameteraccess/read-string-vi.html language=enus -->
## TOPIC 00056: Read String VI

- bundle_id: `flexlogger-labview-PDK-ref`
- source_path: `vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/parameteraccess/read-string-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger-labview-PDK-ref/raw/resource/enus/vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/parameteraccess/read-string-vi.html
- document_id: `flexlogger-labview-PDK-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Read the latest plugin-level parameter value from FlexLogger as a text string. The parameter must first be created by a call of matching name and data type. icon Inputs/Outputs cPluginSDK_lvlibp_Pluginlvclass.png Plugin in Plugin In is the instance of the user's Plugin.lvclass being passed in. cstr.

### Read String VI

Read the latest plugin-level parameter value from FlexLogger as a text string. The parameter must first be created by a call of matching name and data type.

[IMAGE alt='icon' src='read-string-vi.png']

#### Inputs/Outputs

| Plugin in — Plugin In is the instance of the user's Plugin.lvclass being passed in. Name — Name is the name of the parameter. error in (no error) — The error in cluster can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. Plugin out — Plugin out is the instance of the user's Plugin.lvclass being passed out. Value — Value is the value for this parameter or setpoint. Found — found returns TRUE if the parameter was found. error out — The error out cluster passes error or warning information out of a VI to be used by other VIs. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
| --- |

Parent topic:

Read Parameter VI

<!--NI_TOPIC bundle=flexlogger-labview-PDK-ref path=vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/parameteraccess/remove-parameter-vi.html language=enus -->
## TOPIC 00057: Remove Parameter VI

- bundle_id: `flexlogger-labview-PDK-ref`
- source_path: `vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/parameteraccess/remove-parameter-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger-labview-PDK-ref/raw/resource/enus/vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/parameteraccess/remove-parameter-vi.html
- document_id: `flexlogger-labview-PDK-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use this VI to remove a parameter by name from the Plugin's collection of top level parameters. icon Inputs/Outputs cPluginSDK_lvlibp_Pluginlvclass.png Plugin in Plugin In is the instance of the user's Plugin.lvclass being passed in. cstr.png Name Name is the name of the parameter. cerrcodeclst.png

### Remove Parameter VI

Use this VI to remove a parameter by name from the Plugin's collection of top level parameters.

[IMAGE alt='icon' src='remove-parameter-vi.png']

#### Inputs/Outputs

| Plugin in — Plugin In is the instance of the user's Plugin.lvclass being passed in. Name — Name is the name of the parameter. error in (no error) — The error in cluster can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. Plugin out — Plugin out is the instance of the user's Plugin.lvclass being passed out. error out — The error out cluster passes error or warning information out of a VI to be used by other VIs. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
| --- |

Parent topic:

Advanced

<!--NI_TOPIC bundle=flexlogger-labview-PDK-ref path=vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/parameteraccess/write-boolean-vi.html language=enus -->
## TOPIC 00058: Write Boolean VI

- bundle_id: `flexlogger-labview-PDK-ref`
- source_path: `vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/parameteraccess/write-boolean-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger-labview-PDK-ref/raw/resource/enus/vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/parameteraccess/write-boolean-vi.html
- document_id: `flexlogger-labview-PDK-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Create or update a plugin-level parameter for users to interact with in FlexLogger. This parameter is a boolean operation. icon Inputs/Outputs cPluginSDK_lvlibp_Pluginlvclass.png Plugin in Plugin In is the instance of the user's Plugin.lvclass being passed in. cstr.png Name Name is the name of the p

### Write Boolean VI

Create or update a plugin-level parameter for users to interact with in FlexLogger. This parameter is a boolean operation.

[IMAGE alt='icon' src='write-boolean-vi.png']

#### Inputs/Outputs

| Plugin in — Plugin In is the instance of the user's Plugin.lvclass being passed in. Name — Name is the name of the parameter. Value — Value is the value for this parameter or setpoint. error in (no error) — The error in cluster can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. Plugin out — Plugin out is the instance of the user's Plugin.lvclass being passed out. error out — The error out cluster passes error or warning information out of a VI to be used by other VIs. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
| --- |

Parent topic:

Write Parameter VI

<!--NI_TOPIC bundle=flexlogger-labview-PDK-ref path=vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/parameteraccess/write-command-vi.html language=enus -->
## TOPIC 00059: Write Command VI

- bundle_id: `flexlogger-labview-PDK-ref`
- source_path: `vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/parameteraccess/write-command-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger-labview-PDK-ref/raw/resource/enus/vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/parameteraccess/write-command-vi.html
- document_id: `flexlogger-labview-PDK-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use this VI to create a command in FlexLogger. When you set this parameter, the plug-in will create a button in FlexLogger. Pressing the button in FlexLogger sends a notification to the plug-in. icon Inputs/Outputs cPluginSDK_lvlibp_Pluginlvclass.png Plugin in Plugin In is the instance of the user's

### Write Command VI

Use this VI to create a command in FlexLogger. When you set this parameter, the plug-in will create a button in FlexLogger. Pressing the button in FlexLogger sends a notification to the plug-in.

[IMAGE alt='icon' src='write-command-vi.png']

#### Inputs/Outputs

| Plugin in — Plugin In is the instance of the user's Plugin.lvclass being passed in. Name — Name is the name of the parameter. error in (no error) — The error in cluster can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. Plugin out — Plugin out is the instance of the user's Plugin.lvclass being passed out. error out — The error out cluster passes error or warning information out of a VI to be used by other VIs. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
| --- |

Parent topic:

Write Parameter VI

<!--NI_TOPIC bundle=flexlogger-labview-PDK-ref path=vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/parameteraccess/write-dbl-vi.html language=enus -->
## TOPIC 00060: Write DBL VI

- bundle_id: `flexlogger-labview-PDK-ref`
- source_path: `vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/parameteraccess/write-dbl-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger-labview-PDK-ref/raw/resource/enus/vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/parameteraccess/write-dbl-vi.html
- document_id: `flexlogger-labview-PDK-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Create or update a plugin-level parameter for users to interact with in FlexLogger. This parameter is a double-precision, floating-point numeric. icon Inputs/Outputs cPluginSDK_lvlibp_Pluginlvclass.png Plugin in Plugin In is the instance of the user's Plugin.lvclass being passed in. cstr.png Name Na

### Write DBL VI

Create or update a plugin-level parameter for users to interact with in FlexLogger. This parameter is a double-precision, floating-point numeric.

[IMAGE alt='icon' src='write-dbl-vi.png']

#### Inputs/Outputs

| Plugin in — Plugin In is the instance of the user's Plugin.lvclass being passed in. Name — Name is the name of the parameter. Value — Value is the value for this parameter or setpoint. error in (no error) — The error in cluster can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. Plugin out — Plugin out is the instance of the user's Plugin.lvclass being passed out. error out — The error out cluster passes error or warning information out of a VI to be used by other VIs. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
| --- |

Parent topic:

Write Parameter VI

<!--NI_TOPIC bundle=flexlogger-labview-PDK-ref path=vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/parameteraccess/write-enum-vi.html language=enus -->
## TOPIC 00061: Write Enum VI

- bundle_id: `flexlogger-labview-PDK-ref`
- source_path: `vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/parameteraccess/write-enum-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger-labview-PDK-ref/raw/resource/enus/vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/parameteraccess/write-enum-vi.html
- document_id: `flexlogger-labview-PDK-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Create or update a plugin-level parameter for users to interact with in FlexLogger. This parameter is an enumerated constant. icon Inputs/Outputs c1dstr.png Possible Values Possible Values specifies the possible values for the enum. cPluginSDK_lvlibp_Pluginlvclass.png Plugin in Plugin In is the inst

### Write Enum VI

Create or update a plugin-level parameter for users to interact with in FlexLogger. This parameter is an enumerated constant.

[IMAGE alt='icon' src='write-enum-vi.png']

#### Inputs/Outputs

| Possible Values — Possible Values specifies the possible values for the enum. Plugin in — Plugin In is the instance of the user's Plugin.lvclass being passed in. Name — Name is the name of the parameter. Current Value — Current Value is the desired current value of the enum. error in (no error) — The error in cluster can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. Plugin out — Plugin out is the instance of the user's Plugin.lvclass being passed out. error out — The error out cluster passes error or warning information out of a VI to be used by other VIs. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
| --- |

Parent topic:

Write Parameter VI

<!--NI_TOPIC bundle=flexlogger-labview-PDK-ref path=vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/parameteraccess/write-i32-vi.html language=enus -->
## TOPIC 00062: Write I32 VI

- bundle_id: `flexlogger-labview-PDK-ref`
- source_path: `vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/parameteraccess/write-i32-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger-labview-PDK-ref/raw/resource/enus/vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/parameteraccess/write-i32-vi.html
- document_id: `flexlogger-labview-PDK-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Create or update a plugin-level parameter for users to interact with in FlexLogger. This parameter is a 32-bit long signed integer. icon Inputs/Outputs cPluginSDK_lvlibp_Pluginlvclass.png Plugin in Plugin In is the instance of the user's Plugin.lvclass being passed in. cstr.png Name Name is the name

### Write I32 VI

Create or update a plugin-level parameter for users to interact with in FlexLogger. This parameter is a 32-bit long signed integer.

[IMAGE alt='icon' src='write-i32-vi.png']

#### Inputs/Outputs

| Plugin in — Plugin In is the instance of the user's Plugin.lvclass being passed in. Name — Name is the name of the parameter. Value — Value is the value for this parameter or setpoint. error in (no error) — The error in cluster can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. Plugin out — Plugin out is the instance of the user's Plugin.lvclass being passed out. error out — The error out cluster passes error or warning information out of a VI to be used by other VIs. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
| --- |

Parent topic:

Write Parameter VI

<!--NI_TOPIC bundle=flexlogger-labview-PDK-ref path=vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/parameteraccess/write-n-channel-vi.html language=enus -->
## TOPIC 00063: Write N Channel VI

- bundle_id: `flexlogger-labview-PDK-ref`
- source_path: `vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/parameteraccess/write-n-channel-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger-labview-PDK-ref/raw/resource/enus/vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/parameteraccess/write-n-channel-vi.html
- document_id: `flexlogger-labview-PDK-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Create or update a plugin-level parameter for users to interact with in FlexLogger. This parameter allows a user to map a multiple waveform channels to the plugin so the plugin can perform operations on the data. icon Inputs/Outputs cPluginSDK_lvlibp_Pluginlvclass.png Plugin in Plugin In is the inst

### Write N Channel VI

Create or update a plugin-level parameter for users to interact with in FlexLogger. This parameter allows a user to map a multiple waveform channels to the plugin so the plugin can perform operations on the data.

[IMAGE alt='icon' src='write-n-channel-vi.png']

#### Inputs/Outputs

| Plugin in — Plugin In is the instance of the user's Plugin.lvclass being passed in. Name (Unique Channel Identifier) — Name (Unique Channel Identifier) is the name of the parameter for the channel(s). error in (no error) — The error in cluster can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. Plugin out — Plugin out is the instance of the user's Plugin.lvclass being passed out. error out — The error out cluster passes error or warning information out of a VI to be used by other VIs. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
| --- |

Parent topic:

Write Parameter VI

<!--NI_TOPIC bundle=flexlogger-labview-PDK-ref path=vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/parameteraccess/write-n-digital-channel-vi.html language=enus -->
## TOPIC 00064: Write N Digital Channel VI

- bundle_id: `flexlogger-labview-PDK-ref`
- source_path: `vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/parameteraccess/write-n-digital-channel-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger-labview-PDK-ref/raw/resource/enus/vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/parameteraccess/write-n-digital-channel-vi.html
- document_id: `flexlogger-labview-PDK-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Create or update a plugin-level parameter for users to interact with in FlexLogger. This parameter allows a user to map multiple digital waveform channels to the plugin so the plugin can perform operations on the data. icon Inputs/Outputs cPluginSDK_lvlibp_Pluginlvclass.png Plugin in Plugin In is th

### Write N Digital Channel VI

Create or update a plugin-level parameter for users to interact with in FlexLogger. This parameter allows a user to map multiple digital waveform channels to the plugin so the plugin can perform operations on the data.

[IMAGE alt='icon' src='write-n-digital-channel-vi.png']

#### Inputs/Outputs

| Plugin in — Plugin In is the instance of the user's Plugin.lvclass being passed in. Name (Unique Channel Identifier) — Name (Unique Channel Identifier) is the name of the parameter for the channel(s). error in (no error) — The error in cluster can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. Plugin out — Plugin out is the instance of the user's Plugin.lvclass being passed out. error out — The error out cluster passes error or warning information out of a VI to be used by other VIs. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
| --- |

Parent topic:

Write Parameter VI

<!--NI_TOPIC bundle=flexlogger-labview-PDK-ref path=vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/parameteraccess/write-parameter-vi.html language=enus -->
## TOPIC 00065: Write Parameter VI

- bundle_id: `flexlogger-labview-PDK-ref`
- source_path: `vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/parameteraccess/write-parameter-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger-labview-PDK-ref/raw/resource/enus/vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/parameteraccess/write-parameter-vi.html
- document_id: `flexlogger-labview-PDK-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Create or update a plugin-level parameter for users to interact with in FlexLogger. icon

### Write Parameter VI

Create or update a plugin-level parameter for users to interact with in FlexLogger.

[IMAGE alt='icon' src='write-parameter-vi.png']

- [Write Boolean VI](../../../../../../../../vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/parameteraccess/write-boolean-vi.html) Create or update a plugin-level parameter for users to interact with in FlexLogger. This parameter is a boolean operation.
- [Write DBL VI](../../../../../../../../vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/parameteraccess/write-dbl-vi.html) Create or update a plugin-level parameter for users to interact with in FlexLogger. This parameter is a double-precision, floating-point numeric.
- [Write Enum VI](../../../../../../../../vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/parameteraccess/write-enum-vi.html) Create or update a plugin-level parameter for users to interact with in FlexLogger. This parameter is an enumerated constant.
- [Write I32 VI](../../../../../../../../vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/parameteraccess/write-i32-vi.html) Create or update a plugin-level parameter for users to interact with in FlexLogger. This parameter is a 32-bit long signed integer.
- [Write String VI](../../../../../../../../vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/parameteraccess/write-string-vi.html) Create or update a plugin-level parameter for users to interact with in FlexLogger. This parameter is a text string.
- [Write N Channel VI](../../../../../../../../vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/parameteraccess/write-n-channel-vi.html) Create or update a plugin-level parameter for users to interact with in FlexLogger. This parameter allows a user to map a multiple waveform channels to the plugin so the plugin can perform operations on the data.
- [Write Single Channel VI](../../../../../../../../vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/parameteraccess/write-single-channel-vi.html) Create or update a plugin-level parameter for users to interact with in FlexLogger. This parameter allows a user to map a single waveform channel to the plugin so the plugin can perform operations on the data.
- [Write Command VI](../../../../../../../../vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/parameteraccess/write-command-vi.html) Use this VI to create a command in FlexLogger. When you set this parameter, the plug-in will create a button in FlexLogger. Pressing the button in FlexLogger sends a notification to the plug-in.
- [Write N Digital Channel VI](../../../../../../../../vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/parameteraccess/write-n-digital-channel-vi.html) Create or update a plugin-level parameter for users to interact with in FlexLogger. This parameter allows a user to map multiple digital waveform channels to the plugin so the plugin can perform operations on the data.
- [Write Single Digital Channel VI](../../../../../../../../vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/parameteraccess/write-single-digital-channel-vi.html) Create or update a plugin-level parameter for users to interact with in FlexLogger. This parameter allows a user to map a single digital waveform channel to the plugin so the plugin can perform operations on the data.

Parent topic:

Plug-In Development

<!--NI_TOPIC bundle=flexlogger-labview-PDK-ref path=vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/parameteraccess/write-single-channel-vi.html language=enus -->
## TOPIC 00066: Write Single Channel VI

- bundle_id: `flexlogger-labview-PDK-ref`
- source_path: `vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/parameteraccess/write-single-channel-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger-labview-PDK-ref/raw/resource/enus/vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/parameteraccess/write-single-channel-vi.html
- document_id: `flexlogger-labview-PDK-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Create or update a plugin-level parameter for users to interact with in FlexLogger. This parameter allows a user to map a single waveform channel to the plugin so the plugin can perform operations on the data. icon Inputs/Outputs cPluginSDK_lvlibp_Pluginlvclass.png Plugin in Plugin In is the instanc

### Write Single Channel VI

Create or update a plugin-level parameter for users to interact with in FlexLogger. This parameter allows a user to map a single waveform channel to the plugin so the plugin can perform operations on the data.

[IMAGE alt='icon' src='write-single-channel-vi.png']

#### Inputs/Outputs

| Plugin in — Plugin In is the instance of the user's Plugin.lvclass being passed in. Name (Unique Channel Identifier) — Name (Unique Channel Identifier) is the name of the parameter for the channel(s). error in (no error) — The error in cluster can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. Plugin out — Plugin out is the instance of the user's Plugin.lvclass being passed out. error out — The error out cluster passes error or warning information out of a VI to be used by other VIs. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
| --- |

Parent topic:

Write Parameter VI

<!--NI_TOPIC bundle=flexlogger-labview-PDK-ref path=vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/parameteraccess/write-single-digital-channel-vi.html language=enus -->
## TOPIC 00067: Write Single Digital Channel VI

- bundle_id: `flexlogger-labview-PDK-ref`
- source_path: `vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/parameteraccess/write-single-digital-channel-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger-labview-PDK-ref/raw/resource/enus/vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/parameteraccess/write-single-digital-channel-vi.html
- document_id: `flexlogger-labview-PDK-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Create or update a plugin-level parameter for users to interact with in FlexLogger. This parameter allows a user to map a single digital waveform channel to the plugin so the plugin can perform operations on the data. icon Inputs/Outputs cPluginSDK_lvlibp_Pluginlvclass.png Plugin in Plugin In is the

### Write Single Digital Channel VI

Create or update a plugin-level parameter for users to interact with in FlexLogger. This parameter allows a user to map a single digital waveform channel to the plugin so the plugin can perform operations on the data.

[IMAGE alt='icon' src='write-single-digital-channel-vi.png']

#### Inputs/Outputs

| Plugin in — Plugin In is the instance of the user's Plugin.lvclass being passed in. Name (Unique Channel Identifier) — Name (Unique Channel Identifier) is the name of the parameter for the channel(s). error in (no error) — The error in cluster can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. Plugin out — Plugin out is the instance of the user's Plugin.lvclass being passed out. error out — The error out cluster passes error or warning information out of a VI to be used by other VIs. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
| --- |

Parent topic:

Write Parameter VI

<!--NI_TOPIC bundle=flexlogger-labview-PDK-ref path=vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/parameteraccess/write-string-vi.html language=enus -->
## TOPIC 00068: Write String VI

- bundle_id: `flexlogger-labview-PDK-ref`
- source_path: `vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/parameteraccess/write-string-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger-labview-PDK-ref/raw/resource/enus/vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/parameteraccess/write-string-vi.html
- document_id: `flexlogger-labview-PDK-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Create or update a plugin-level parameter for users to interact with in FlexLogger. This parameter is a text string. icon Inputs/Outputs cPluginSDK_lvlibp_Pluginlvclass.png Plugin in Plugin In is the instance of the user's Plugin.lvclass being passed in. cstr.png Name Name is the name of the paramet

### Write String VI

Create or update a plugin-level parameter for users to interact with in FlexLogger. This parameter is a text string.

[IMAGE alt='icon' src='write-string-vi.png']

#### Inputs/Outputs

| Plugin in — Plugin In is the instance of the user's Plugin.lvclass being passed in. Name — Name is the name of the parameter. Value — Value is the value for this parameter or setpoint. error in (no error) — The error in cluster can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. Plugin out — Plugin out is the instance of the user's Plugin.lvclass being passed out. error out — The error out cluster passes error or warning information out of a VI to be used by other VIs. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
| --- |

Parent topic:

Write Parameter VI

<!--NI_TOPIC bundle=flexlogger-labview-PDK-ref path=vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/remove-channels-vi.html language=enus -->
## TOPIC 00069: Remove Channels VI

- bundle_id: `flexlogger-labview-PDK-ref`
- source_path: `vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/remove-channels-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger-labview-PDK-ref/raw/resource/enus/vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/remove-channels-vi.html
- document_id: `flexlogger-labview-PDK-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Remove channels from the plugin. icon Inputs/Outputs cPluginSDK_lvlibp_Pluginlvclass.png Plugin in Plugin In is the instance of the user's Plugin.lvclass being passed in. c1dstr.png Unique Channel Identifiers to Delete Unique Channel Identifiers to Delete is the channel identifiers for the channels

### Remove Channels VI

Remove channels from the plugin.

[IMAGE alt='icon' src='remove-channels-vi.png']

#### Inputs/Outputs

| Plugin in — Plugin In is the instance of the user's Plugin.lvclass being passed in. Unique Channel Identifiers to Delete — Unique Channel Identifiers to Delete is the channel identifiers for the channels to remove. error in (no error) — The error in cluster can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. Plugin out — Plugin out is the instance of the user's Plugin.lvclass being passed out. error out — The error out cluster passes error or warning information out of a VI to be used by other VIs. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
| --- |

Parent topic:

Advanced

<!--NI_TOPIC bundle=flexlogger-labview-PDK-ref path=vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/replace-channel-group-vi.html language=enus -->
## TOPIC 00070: Replace Channel Group VI

- bundle_id: `flexlogger-labview-PDK-ref`
- source_path: `vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/replace-channel-group-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger-labview-PDK-ref/raw/resource/enus/vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/replace-channel-group-vi.html
- document_id: `flexlogger-labview-PDK-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Replaces all the channels in the specified group with a new set of channels. This VI should be called conditionally when something about a channel has changed. Calling it every Configure Session.vi or Process.vi run will result in an infinite configuration loop. icon Inputs/Outputs cPluginSDK_lvlibp

### Replace Channel Group VI

Replaces all the channels in the specified group with a new set of channels. This VI should be called conditionally when something about a channel has changed. Calling it every Configure Session.vi or Process.vi run will result in an infinite configuration loop.

[IMAGE alt='icon' src='replace-channel-group-vi.png']

#### Inputs/Outputs

| Plugin — Plugin specifies the instance of the Plugin.lvclass to operate on. Group Name — Group Name is the name of the Display Group to replace. Channels — Channels is an array of channel objects of type Channel.lvclass. error in (no error) — The error in cluster can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. Plugin — Plugin specifies the instance of the Plugin.lvclass to operate on. error out — The error out cluster passes error or warning information out of a VI to be used by other VIs. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
| --- |

Parent topic:

Advanced

<!--NI_TOPIC bundle=flexlogger-labview-PDK-ref path=vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/replace-producer-channels-vi.html language=enus -->
## TOPIC 00071: Replace Producer Channels VI

- bundle_id: `flexlogger-labview-PDK-ref`
- source_path: `vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/replace-producer-channels-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger-labview-PDK-ref/raw/resource/enus/vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/replace-producer-channels-vi.html
- document_id: `flexlogger-labview-PDK-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Replaces all existing producer channels with a new list of producer channels. This can be helpful for situations where configuration changes in such a way that all channels need to be recreated. This VI should be called conditionally when something about a channel has changed. Calling it every Confi

### Replace Producer Channels VI

Replaces all existing producer channels with a new list of producer channels. This can be helpful for situations where configuration changes in such a way that all channels need to be recreated. This VI should be called conditionally when something about a channel has changed. Calling it every Configure Session.vi or Process.vi run will result in an infinite configuration loop.

[IMAGE alt='icon' src='replace-producer-channels-vi.png']

#### Inputs/Outputs

| Plugin — Plugin specifies the instance of the Plugin.lvclass to operate on. Producer Channels — Producer Channels are the new producer channels used to replace the existing ones. error in (no error) — The error in cluster can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. Plugin — Plugin specifies the instance of the Plugin.lvclass to operate on. error out — The error out cluster passes error or warning information out of a VI to be used by other VIs. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
| --- |

Parent topic:

Advanced

<!--NI_TOPIC bundle=flexlogger-labview-PDK-ref path=vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/set-file-metadata-vi.html language=enus -->
## TOPIC 00072: Set File Metadata VI

- bundle_id: `flexlogger-labview-PDK-ref`
- source_path: `vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/set-file-metadata-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger-labview-PDK-ref/raw/resource/enus/vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/set-file-metadata-vi.html
- document_id: `flexlogger-labview-PDK-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use this VI to add top level file metadata into the TDMS log file. The parameters will be added to a group matching the display name of this plugin. icon Inputs/Outputs cPluginSDK_lvlibp_Pluginlvclass.png Plugin in Plugin In is the instance of the user's Plugin.lvclass being passed in. c1dcclst.png

### Set File Metadata VI

Use this VI to add top level file metadata into the TDMS log file. The parameters will be added to a group matching the display name of this plugin.

[IMAGE alt='icon' src='set-file-metadata-vi.png']

#### Inputs/Outputs

| Plugin in — Plugin In is the instance of the user's Plugin.lvclass being passed in. Metadata — Metadata is the file metadata to set. Name — Value — error in (no error) — The error in cluster can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. Plugin out — Plugin out is the instance of the user's Plugin.lvclass being passed out. error out — The error out cluster passes error or warning information out of a VI to be used by other VIs. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
| --- |
| Name — Value — |

Parent topic:

Advanced

<!--NI_TOPIC bundle=flexlogger-labview-PDK-ref path=vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/set-plugin-resampling-vi.html language=enus -->
## TOPIC 00073: Set Plugin Resampling VI

- bundle_id: `flexlogger-labview-PDK-ref`
- source_path: `vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/set-plugin-resampling-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger-labview-PDK-ref/raw/resource/enus/vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/set-plugin-resampling-vi.html
- document_id: `flexlogger-labview-PDK-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configure the plugin input resampling. These parameters control how input waveforms are aggregated. Since inputs to a plugin may be from multiple sources running at different rates, some kind of resampling strategy is required. Maximum or Minimum mode pick a rate based on the rate of the inputs mapp

### Set Plugin Resampling VI

Configure the plugin input resampling. These parameters control how input waveforms are aggregated. Since inputs to a plugin may be from multiple sources running at different rates, some kind of resampling strategy is required. Maximum or Minimum mode pick a rate based on the rate of the inputs mapped to this plugin. Custom rate specifies a fixed rate that the inputs will be resampled to regardless of the rate of the inputs. Block size and drift tolerance are also configurable. 

Block size determines the minimum amount of overlapping data to wait for until data is passed to the plugin. 

Drift Tolerance determines the maximum amount of data to save waiting for overlapping data. A larger Drift Tolerance potentially results in more memory usage while a small Drift Tolerance may result in issues aggregating data whose time bases have drifted relative to one another.

[IMAGE alt='icon' src='set-plugin-resampling-vi.png']

#### Inputs/Outputs

| Drift Tolerance (s) — Drift Tolerance (s) determines the maximum amount of data to save waiting for overlapping data. A larger Drift Tolerance potentially results in more memory usage while a small Drift Tolerance may result in issues aggregating data whose time bases have drifted relative to one another. Plugin in — Plugin In is the instance of the user's Plugin.lvclass being passed in. Resampling Mode — Resampling Mode specifies the type of resampling for input channels. Valid values are: No Resampling - Channels are not resampled. Custom Rate - Channels are resampled to the rate specified by Resampling Rate (Hz) Maximum Rate - Channels are resampled to the same rate as the input channel with the fastest sampling rate. Minimum Rate - Channels are resampled to the same rate as the input channel with the slowest sampling rate. Digital - for digital channels. OnDemand - for software timed channels. This can include software timed digital channels and analog output channels. Resampling Rate (Hz) — Resampling Rate (Hz) specifies the resampling rate when resamping mode is set to Custom Rate Block Size (s) — Block Size (s) determines the minimum amount of data to wait for until data is passed to the plugin. error in (no error) — The error in cluster can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. Plugin out — Plugin out is the instance of the user's Plugin.lvclass being passed out. error out — The error out cluster passes error or warning information out of a VI to be used by other VIs. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
| --- |

Parent topic:

Advanced

<!--NI_TOPIC bundle=flexlogger-labview-PDK-ref path=vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/set-plugin-timing-vi.html language=enus -->
## TOPIC 00074: Set Plugin Timing VI

- bundle_id: `flexlogger-labview-PDK-ref`
- source_path: `vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/set-plugin-timing-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger-labview-PDK-ref/raw/resource/enus/vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/set-plugin-timing-vi.html
- document_id: `flexlogger-labview-PDK-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specify the timing configuration for the plugin's Process VI. icon Inputs/Outputs cPluginSDK_lvlibp_Pluginlvclass.png Plugin in Plugin In is the instance of the user's Plugin.lvclass being passed in. cnclst.png Timing Parameters Timing Parameters are the timing parameters for this plugin. cenum.png

### Set Plugin Timing VI

Specify the timing configuration for the plugin's Process VI.

[IMAGE alt='icon' src='set-plugin-timing-vi.png']

#### Inputs/Outputs

| Plugin in — Plugin In is the instance of the user's Plugin.lvclass being passed in. Timing Parameters — Timing Parameters are the timing parameters for this plugin. Timing Method — Timing Method specifies when to call the Process.vi of the plugin. Valid values are: Periodic - Process.vi is called periodically, every Timing Period (ms) milliseconds. Custom Rate - Process.vi is called as fast as possible with no delay between calls. Timing Period (ms) is ignored. On Data Ready - Process.vi is called only when there is new data to read. In this mode, Timing Period (ms) acts as a timeout, where anything less than or equal to 0 will wait indefinitely for new data. If Timing Period (ms) is greater than zero, Process.vi will be called every Timing Period (ms) milliseconds or whenever there is new data. When setting this value greater than zero, Process.vi may be called when no data is available, so developers who want to use this timeout feature of On Data Ready should check if the data read is empty to determine if Process.vi was called due to a timeout. Triggered - Currently this option is not supported. Timing Period (ms) — Timing Period (ms) is only used if the Timing Method is Periodic or On Data Ready. For Periodic, Process.vi is called every Timing Period (ms) milliseconds. For On Data Ready, Process.vi is called when new data is available, or every Timing Period (ms) milliseconds if Timing Period (ms) is greater than 0. If Timing Period (ms) is less than or equal to 0, it is ignored and Process.vi will wait indefinitely for new data before being called. error in (no error) — The error in cluster can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. Plugin out — Plugin out is the instance of the user's Plugin.lvclass being passed out. error out — The error out cluster passes error or warning information out of a VI to be used by other VIs. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
| --- |
| Timing Method — Timing Method specifies when to call the Process.vi of the plugin. Valid values are: Periodic - Process.vi is called periodically, every Timing Period (ms) milliseconds. Custom Rate - Process.vi is called as fast as possible with no delay between calls. Timing Period (ms) is ignored. On Data Ready - Process.vi is called only when there is new data to read. In this mode, Timing Period (ms) acts as a timeout, where anything less than or equal to 0 will wait indefinitely for new data. If Timing Period (ms) is greater than zero, Process.vi will be called every Timing Period (ms) milliseconds or whenever there is new data. When setting this value greater than zero, Process.vi may be called when no data is available, so developers who want to use this timeout feature of On Data Ready should check if the data read is empty to determine if Process.vi was called due to a timeout. Triggered - Currently this option is not supported. Timing Period (ms) — Timing Period (ms) is only used if the Timing Method is Periodic or On Data Ready. For Periodic, Process.vi is called every Timing Period (ms) milliseconds. For On Data Ready, Process.vi is called when new data is available, or every Timing Period (ms) milliseconds if Timing Period (ms) is greater than 0. If Timing Period (ms) is less than or equal to 0, it is ignored and Process.vi will wait indefinitely for new data before being called. |

Parent topic:

Advanced

<!--NI_TOPIC bundle=flexlogger-labview-PDK-ref path=vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/update-channels-unit-vi.html language=enus -->
## TOPIC 00075: Update Channels Unit VI

- bundle_id: `flexlogger-labview-PDK-ref`
- source_path: `vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/update-channels-unit-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger-labview-PDK-ref/raw/resource/enus/vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/update-channels-unit-vi.html
- document_id: `flexlogger-labview-PDK-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Updates the unit string for a set of channels. This VI will not cause another pass of the Configure Session state. icon Inputs/Outputs cPluginSDK_lvlibp_Pluginlvclass.png Plugin in Plugin In is the instance of the user's Plugin.lvclass being passed in. c1dstr.png Channels Unique Identifier Channels

### Update Channels Unit VI

Updates the unit string for a set of channels. This VI will not cause another pass of the Configure Session state.

[IMAGE alt='icon' src='update-channels-unit-vi.png']

#### Inputs/Outputs

| Plugin in — Plugin In is the instance of the user's Plugin.lvclass being passed in. Channels Unique Identifier — Channels Unique Identifier is an array of unique identifiers for the channels to update. Unit — Unit is the string value of units for this channel. error in (no error) — The error in cluster can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. Plugin out — Plugin out is the instance of the user's Plugin.lvclass being passed out. error out — The error out cluster passes error or warning information out of a VI to be used by other VIs. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
| --- |

Parent topic:

Advanced

<!--NI_TOPIC bundle=flexlogger-labview-PDK-ref path=vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/write-use-immediate-device-dialog-vi.html language=enus -->
## TOPIC 00076: Write Use Immediate Device Dialog VI

- bundle_id: `flexlogger-labview-PDK-ref`
- source_path: `vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/write-use-immediate-device-dialog-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger-labview-PDK-ref/raw/resource/enus/vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/plugin/write-use-immediate-device-dialog-vi.html
- document_id: `flexlogger-labview-PDK-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use this VI to change the type of dialog shown at the group level in FlexLogger. An immediate dialog sends all property value changes immediately to the plugin allowing the plugin developer to add dynamic behaviors. An OK/Cancel dialog waits until OK is pressed to send all property value changes as

### Write Use Immediate Device Dialog VI

Use this VI to change the type of dialog shown at the group level in FlexLogger. An immediate dialog sends all property value changes immediately to the plugin allowing the plugin developer to add dynamic behaviors. An OK/Cancel dialog waits until OK is pressed to send all property value changes as single batch.

[IMAGE alt='icon' src='write-use-immediate-device-dialog-vi.png']

#### Inputs/Outputs

| Plugin in — Plugin In is the instance of the user's Plugin.lvclass being passed in. Use Immediate Device Dialog? — Use Immediate Device Dialog? determines whether to use the immediate device dialog. An immediate dialog sends all property value changes immediately to the plugin allowing the plugin developer to add dynamic behaviors. By default, this value is FALSE, and FlexLogger will not use an immediate device dialog. Set this value to TRUE to change the behavior to use an immediate device dialog. error in (no error) — The error in cluster can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. Plugin out — Plugin out is the instance of the user's Plugin.lvclass being passed out. error out — The error out cluster passes error or warning information out of a VI to be used by other VIs. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
| --- |

Parent topic:

Advanced

<!--NI_TOPIC bundle=flexlogger-labview-PDK-ref path=vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/producer-channel/create-producer-channel-v2-vi.html language=enus -->
## TOPIC 00077: Create Producer Channel_v2 VI

- bundle_id: `flexlogger-labview-PDK-ref`
- source_path: `vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/producer-channel/create-producer-channel-v2-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger-labview-PDK-ref/raw/resource/enus/vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/producer-channel/create-producer-channel-v2-vi.html
- document_id: `flexlogger-labview-PDK-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Create a channel that sends data from the plugin to the FlexLogger application using Write Data.vi. icon Inputs/Outputs cu16.png Data Type Data Type is the data type of the channel. Valid values are: Wfm (DBL) - for analog channels Wfm (Digital) - for digital channels String - for string channels cs

### Create Producer Channel_v2 VI

Create a channel that sends data from the plugin to the FlexLogger application using **Write Data.vi**.

[IMAGE alt='icon' src='create-producer-channel-v2-vi.png']

#### Inputs/Outputs

| Data Type — Data Type is the data type of the channel. Valid values are: Wfm (DBL) - for analog channels Wfm (Digital) - for digital channels String - for string channels Display Group — Display Group is the group to display the channel within. Channels with the same Display Group will be grouped together in FlexLogger. Unique Channel Identifier — Unique Channel Identifier is the unique identifier for the channel. You can use this identifier to reference this channel when reading data in Process.vi. Default Channel Name — Default Channel Name is the default name for the channel when the plugin is added to FlexLogger. Parameters — Parameters is an instance of the Parameters.lvclass that can be created using members of the Parameters.lvclass library for advanced use cases. However, for most use cases, this input can be left unwired, and users should use the Write Parameter.vi to create channel parameters. dt(sec) — dt(sec) is the sampling interval in seconds. error in (no error) — The error in cluster can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. Unit — Unit is the string value of units for this channel. Can Disable? — Can Disable? determines whether the channel can be disabled in the Channel Specification in FlexLogger. Producer Channel — Producer Channel is the created producer channel. error out — The error out cluster passes error or warning information out of a VI to be used by other VIs. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
| --- |

Parent topic:

Create Channel_v2 VI

<!--NI_TOPIC bundle=flexlogger-labview-PDK-ref path=vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/setpoint-consumer-channel/create-setpoint-consumer-channel-vi.html language=enus -->
## TOPIC 00078: Create Setpoint Consumer Channel VI

- bundle_id: `flexlogger-labview-PDK-ref`
- source_path: `vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/setpoint-consumer-channel/create-setpoint-consumer-channel-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger-labview-PDK-ref/raw/resource/enus/vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/setpoint-consumer-channel/create-setpoint-consumer-channel-vi.html
- document_id: `flexlogger-labview-PDK-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Create a channel that allows a FlexLogger user to enter setpoint values. Those setpoint channel values are consumed by the plugin using Get Latest Setpoints.vi. icon Inputs/Outputs cstr.png Display Group Display Group is the group to display the channel within. Channels with the same Display Group w

### Create Setpoint Consumer Channel VI

Create a channel that allows a FlexLogger user to enter setpoint values. Those setpoint channel values are consumed by the plugin using **Get Latest Setpoints.vi**.

[IMAGE alt='icon' src='create-setpoint-consumer-channel-vi.png']

#### Inputs/Outputs

| Display Group — Display Group is the group to display the channel within. Channels with the same Display Group will be grouped together in FlexLogger. Unique Channel Identifier — Unique Channel Identifier is the unique identifier for the channel. You can use this identifier to reference this channel when reading data in Process.vi. Default Channel Name — Default Channel Name is the default name for the channel when the plugin is added to FlexLogger. Parameters — Parameters is an instance of the Parameters.lvclass that can be created using members of the Parameters.lvclass library for advanced use cases. However, for most use cases, this input can be left unwired, and users should use the Write Parameter.vi to create channel parameters. Default Value — Default Value is the default value for the setpoint channel. error in (no error) — The error in cluster can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. Unit — Unit is the string value of units for this channel. Can Disable? — Can Disable? determines whether the channel can be disabled in the Channel Specification in FlexLogger. Setpoint Consumer Channel — Setpoint Consumer Channel is the created Setpoint Consumer Channel object. error out — The error out cluster passes error or warning information out of a VI to be used by other VIs. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
| --- |

Parent topic:

Create Channel_v2 VI

<!--NI_TOPIC bundle=flexlogger-labview-PDK-ref path=vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/write-trace-log-vi.html language=enus -->
## TOPIC 00079: Write Trace Log VI

- bundle_id: `flexlogger-labview-PDK-ref`
- source_path: `vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/write-trace-log-vi.html`
- source_url: https://docs-be.ni.com/bundle/flexlogger-labview-PDK-ref/raw/resource/enus/vi-lib/flexlogger/sdk/pluginsdk-lvlibp/pefclasses/sdk/write-trace-log-vi.html
- document_id: `flexlogger-labview-PDK-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Write Message to DebugView. You will need to download and install DebugView from Microsoft Sysinternals. Then run the executable to see the logged messages. This can be helpful when debugging plugins that run as part of FlexLogger. Use the Format Into String.vi to combine several pieces of informati

### Write Trace Log VI

Write **Message** to DebugView. You will need to download and install DebugView from Microsoft Sysinternals. Then run the executable to see the logged messages. This can be helpful when debugging plugins that run as part of FlexLogger. Use the **Format Into String.vi** to combine several pieces of information into a single string that can be logged. If there is an error on the **error in** terminal, the error code and string will also be included in the logged message.

Note: When running DebugView, you can use the filter to only see messages that meet certain criteria. You can prefix all your debug messages to make it easy to only see these messages in DebugView since other applications may log messages to DebugView as well.

Note: Any program that can view messages from OutputDebugString will be able to view these messages. This includes Visual Studio when it attaches to the NationalInstruments.IoDataPef.Engine.exe process under FlexLogger, which is the executable that runs the plug-ins.

[IMAGE alt='icon' src='write-trace-log-vi.png']

#### Inputs/Outputs

| Message — Message is the message string to write. error in (no error) — The error in cluster can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. error out — The error out cluster passes error or warning information out of a VI to be used by other VIs. The pop-up option Explain Error (or Explain Warning) gives more information about the error displayed. |
| --- |

Parent topic:

Advanced
