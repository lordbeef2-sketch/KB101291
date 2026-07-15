# NI DOCUMENT BUNDLE: veristand-steps-for-teststand

<!--NI_BUNDLE_CHUNK bundle=veristand-steps-for-teststand start=1 end=15 -->
<!--NI_TOPIC bundle=veristand-steps-for-teststand path=vsts_comp/2025Q1.html language=enus -->
## TOPIC 00001: VeriStand Steps for TestStand 2025 Q1

- bundle_id: `veristand-steps-for-teststand`
- source_path: `vsts_comp/2025Q1.html`
- source_url: https://docs-be.ni.com/bundle/veristand-steps-for-teststand/raw/resource/enus/vsts_comp/2025Q1.html
- document_id: `veristand-steps-for-teststand`
- page_type: `leaf`
- content_type: `reference`
- source_description: Application Software Support VeriStand Steps for TestStand 2025 Q1 supports the following application software versions, including service packs. TestStand VeriStand 2021 SP1 2023 Q3+, 2024, 2025 2022 2023 Q3+, 2024, 2025 2023 2023 Q3+, 2024, 2025

### VeriStand Steps for TestStand 2025 Q1

#### Application Software Support

VeriStand Steps for TestStand 2025 Q1 supports the following application software versions, including service packs.

| TestStand | VeriStand |
| --- | --- |
| 2021 SP1 | 2023 Q3+, 2024, 2025 |
| 2022 | 2023 Q3+, 2024, 2025 |
| 2023 | 2023 Q3+, 2024, 2025 |

<!--NI_TOPIC bundle=veristand-steps-for-teststand path=vsts_comp/2026Q1.html language=enus -->
## TOPIC 00002: VeriStand Steps for TestStand 2026 Q1

- bundle_id: `veristand-steps-for-teststand`
- source_path: `vsts_comp/2026Q1.html`
- source_url: https://docs-be.ni.com/bundle/veristand-steps-for-teststand/raw/resource/enus/vsts_comp/2026Q1.html
- document_id: `veristand-steps-for-teststand`
- page_type: `leaf`
- content_type: `reference`
- source_description: Application Software Support VeriStand Steps for TestStand 2026 Q1 supports the following application software versions, including service packs. TestStand VeriStand 2021 SP1 2023 Q3+, 2024, 2025 2022 2023 Q3+, 2024, 2025 2023 2023 Q3+, 2024, 2025 2024 Not Supported 2025 2025 Q4 2026 2026 Q1 Beginni

### VeriStand Steps for TestStand 2026 Q1

#### Application Software Support

VeriStand Steps for TestStand 2026 Q1 supports the following application software versions, including service packs.

| TestStand | VeriStand |
| --- | --- |
| 2021 SP1 | 2023 Q3+, 2024, 2025 |
| 2022 | 2023 Q3+, 2024, 2025 |
| 2023 | 2023 Q3+, 2024, 2025 |
| 2024 | Not Supported |
| 2025 | 2025 Q4 |
| 2026 | 2026 Q1 |

Note

Beginning with TestStand 2025, VeriStand Steps for TestStand are supported only when the communication method between gateway and VeriStand is set to gRPC.

Open the VeriStand application, navigate to File -> Preferences -> Ports, and change the Communication method to gRPC.
 Restart VeriStand.exe, VeriStand Project Explorer.exe or the veristand-server.exe after applying the change.

<!--NI_TOPIC bundle=veristand-steps-for-teststand path=vsts_help/overview.html language=enus -->
## TOPIC 00003: VeriStand Steps for TestStand

- bundle_id: `veristand-steps-for-teststand`
- source_path: `vsts_help/overview.html`
- source_url: https://docs-be.ni.com/bundle/veristand-steps-for-teststand/raw/resource/enus/vsts_help/overview.html
- document_id: `veristand-steps-for-teststand`
- page_type: `leaf`
- content_type: `reference`
- source_description: Overview The VeriStand Steps for TestStand are sets of custom steps that allow you to automate VeriStand and develop/reuse test sequences for hardware-in-the-loop (HIL) systems. This document describes how to download these steps and provides reference information for each step. For information on n

### VeriStand Steps for TestStand

#### Overview

The VeriStand Steps for TestStand are sets of custom steps that allow you to automate VeriStand and develop/reuse test sequences for hardware-in-the-loop (HIL) systems.

This document describes how to download these steps and provides reference information for each step. For information on new features in each release, refer to the
 [release notes.](https://www.ni.com/en/support/documentation/release-notes/product.veristand-steps-for-teststand.html)

#### Downloading the VeriStand Steps for TestStand

This product is available for download from the
 [download page.](https://www.ni.com/en/support/downloads/software-products/download.veristand-steps-for-teststand.html)

Follow the prompts from NI Package Manager to install the product.

<!--NI_TOPIC bundle=veristand-steps-for-teststand path=vsts_help/veristand-version-selection.html language=enus -->
## TOPIC 00004: VeriStand Version Selection

- bundle_id: `veristand-steps-for-teststand`
- source_path: `vsts_help/veristand-version-selection.html`
- source_url: https://docs-be.ni.com/bundle/veristand-steps-for-teststand/raw/resource/enus/vsts_help/veristand-version-selection.html
- document_id: `veristand-steps-for-teststand`
- page_type: `leaf`
- content_type: `reference`
- source_description: VeriStand Steps for TestStand uses the latest version of VeriStand installed on the machine by default. Before switching the active VeriStand version, make sure to close any open instances of TestStand. To switch the active VeriStand version, launch VeriStandVersionSelector.exe from the following pa

### VeriStand Version Selection

VeriStand Steps for TestStand uses the latest version of VeriStand installed on the machine by default.

Before switching the active VeriStand version, make sure to close any open instances of TestStand.

To switch the active VeriStand version, launch VeriStandVersionSelector.exe from the following path:

<Public Documents>\National Instruments\TestStand <Version>\Components\VeriStandTestStandSteps\VeriStandVersionSelector.exe

The VeriStand Version Selector lists the supported VeriStand versions to choose from.

| VeriStand Version | Selection Value |
| --- | --- |
| 2023 | 1 |
| 2024 | 2 |
| 2025 | 3 |

For example, to choose 2023, enter selection value as 1 and press Enter.

This sets the active version of VeriStand to use, and closes the VeriStand Version Selector process.

Note

<!--NI_TOPIC bundle=veristand-steps-for-teststand path=vsts_ref/close-veristand.html language=enus -->
## TOPIC 00005: Close VeriStand

- bundle_id: `veristand-steps-for-teststand`
- source_path: `vsts_ref/close-veristand.html`
- source_url: https://docs-be.ni.com/bundle/veristand-steps-for-teststand/raw/resource/enus/vsts_ref/close-veristand.html
- document_id: `veristand-steps-for-teststand`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Close VeriStand step to close the VeriStand application. If VeriStand Project Explorer process is started by the Open VeriStand Project or Connect step, this step stops the VeriStand Project Explorer process.

### Close VeriStand

Use the Close VeriStand step to close the VeriStand application.
 If VeriStand Project Explorer process is started by the Open VeriStand Project or Connect step, this step stops the VeriStand Project Explorer process.

<!--NI_TOPIC bundle=veristand-steps-for-teststand path=vsts_ref/connect.html language=enus -->
## TOPIC 00006: Connect

- bundle_id: `veristand-steps-for-teststand`
- source_path: `vsts_ref/connect.html`
- source_url: https://docs-be.ni.com/bundle/veristand-steps-for-teststand/raw/resource/enus/vsts_ref/connect.html
- document_id: `veristand-steps-for-teststand`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Connect step to deploy the system definition or connect to a pre-deployed system definition. Use the General edit tab in the TestStand Sequence Editor to configure the Connect step. The Connect settings panel contains the following configuration controls: System Definition Path – Path to the

### Connect

Use the
 Connect
 step to deploy the system definition or connect to a pre-deployed system definition.

Use the
 General
 edit tab in the
 [TestStand Sequence Editor](https://www.ni.com/docs/en-US/bundle/teststand/page/tsref/infotopics/seqeditor.htm)
 to configure the
 Connect
 step.

The
 Connect settings panel
 contains the following configuration controls:

- System Definition Path – Path to the NI VeriStand system definition file you want to deploy. If you have already configured an Open VeriStand Project step, this step provides suggestions for the active system definition file based on the open project.
- Calibration File Path – Path to the NI VeriStand calibration file.
- Specify By Expression Checkbox – Specifies whether you provide the system definition/calibration file path using literal strings or expressions that TestStand evaluates at runtime.
- Gateway Address – VeriStand gateway address to the machine running the VeriStand gateway.
- Deploy Checkbox – Enable to deploy the configured system definition file. Disable to connect to the pre-deployed system definition.
- Timeout – The maximum amount of time, in milliseconds, to wait for the connection process to complete before returning an error.
- Step Reference Output – Returns a reference to the deployment. Use a TestStand variable of type Object Reference.
 
 Note 
 The Step Reference Output control only accepts TestStand variables. It does not support creating expressions that use multiple variables.
  - You can specify a TestStand variable in the text box to store the deployment reference.
  - By default, the deployment reference is stored in a TestStand variable named OutputOf_<StepID> in the current sequence file context. This variable is accessible only in the current sequence file.
  - In the dependent step (e.g., Set channel values ), if you specify the deployment reference using the combo box suggestions, the default variable would be used to get the reference. You can also use the variable from Step Reference Output in the Connect step to override the default variable and specify the deployment reference.

The default variable created in the
 Connect
 panel is accessible only within the sequence file. If linking steps across sequence files, specify a TestStand variable to store the deploy reference and pass this variable as a parameter in a sequence call to enable cross-file access.

Note

- File path suggestions in the Connect step appear as either absolute or relative paths. Suggestions are based on the VeriStand project path you specify in the Open VeriStand Project step.
- The Connect step launches the VeriStand Project Explorer process. Use the Close VeriStand step to stop the process.

<!--NI_TOPIC bundle=veristand-steps-for-teststand path=vsts_ref/control-real-time-sequence.html language=enus -->
## TOPIC 00007: Control Real-Time Sequence

- bundle_id: `veristand-steps-for-teststand`
- source_path: `vsts_ref/control-real-time-sequence.html`
- source_url: https://docs-be.ni.com/bundle/veristand-steps-for-teststand/raw/resource/enus/vsts_ref/control-real-time-sequence.html
- document_id: `veristand-steps-for-teststand`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Control Real-Time Sequence step to abort, stop, run, pause, single step or undeploy the real-time sequence. Use the General edit tab in the TestStand Sequence Editor to configure the Control Real-Time Sequence step. The Control Real-Time Sequence settings panel contains the following configu

### Control Real-Time Sequence

Use the
 Control Real-Time Sequence
 step to abort, stop, run, pause, single step or undeploy the real-time sequence.

Use the
 General
 edit tab in the
 [TestStand Sequence Editor](https://www.ni.com/docs/en-US/bundle/teststand/page/teststand-sequence-editor.html)
 to configure the
 Control Real-Time Sequence
 step.

The Control Real-Time Sequence settings panel contains the following configuration controls:

- Real-Time Sequence – Specifies the real-time sequence reference using the combo box suggestions.
 You can also use the variable from Step Reference Output control in the Run Real-Time Sequence step to specify the real-time sequence reference. Refer to Step Reference Output in the Run Real-Time Sequence step for more details.
- Specify By Expression Checkbox - Specifies whether you provide the real-time sequence reference using combo box selection or variables TestStand evaluates at run time.
- Control Action - Abort/Stop/Run/Pause/Single Step/Undeploy the real-time sequence execution.

<!--NI_TOPIC bundle=veristand-steps-for-teststand path=vsts_ref/disconnect.html language=enus -->
## TOPIC 00008: Disconnect

- bundle_id: `veristand-steps-for-teststand`
- source_path: `vsts_ref/disconnect.html`
- source_url: https://docs-be.ni.com/bundle/veristand-steps-for-teststand/raw/resource/enus/vsts_ref/disconnect.html
- document_id: `veristand-steps-for-teststand`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Disconnect step to undeploy or disconnect the specified deployment. Use the General edit tab in the TestStand Sequence Editor to configure the Disconnect step. The Disconnect settings panel contains the following configuration controls: Deployment – Specifies the deployment reference using t

### Disconnect

Use the
 Disconnect
 step to undeploy or disconnect the specified deployment.

Use the
 General
 edit tab in the
 [TestStand Sequence Editor](https://www.ni.com/docs/en-US/bundle/teststand/page/tsref/infotopics/seqeditor.htm)
 to configure the Disconnect step.

The Disconnect settings panel contains the following configuration controls:

- Deployment – Specifies the deployment reference using the combo box suggestions.
 You can also use the variable from Step Reference Output control in the Connect step to specify the deployment reference. Refer to Step Reference Output in the Connect step for more details.
- Specify By Expression Checkbox – Specifies whether you provide the deployment reference using combo box selection or variables TestStand evaluates at run time.
- Undeploy System Definition – Determines whether the system definition file should be undeployed before disconnecting. If set to False , the Real-Time (RT) target(s) will continue running the system definition even after the VeriStand Gateway has disconnected.
 Note 
 This parameter configuration is skipped for Windows targets.

<!--NI_TOPIC bundle=veristand-steps-for-teststand path=vsts_ref/get-channel-values.html language=enus -->
## TOPIC 00009: Get Channel Values

- bundle_id: `veristand-steps-for-teststand`
- source_path: `vsts_ref/get-channel-values.html`
- source_url: https://docs-be.ni.com/bundle/veristand-steps-for-teststand/raw/resource/enus/vsts_ref/get-channel-values.html
- document_id: `veristand-steps-for-teststand`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Get Channel Values step to acquire the current value for the selected channels, aliases, or parameters from the specified system definition. Use the General edit tab in the TestStand Sequence Editor to configure the Get Channel Values step. The Get Channel Values settings panel contains the

### Get Channel Values

Use the
 Get Channel Values
 step to acquire the current value for the selected channels, aliases, or parameters from the specified system definition.

Use the
 General
 edit tab in the
 [TestStand Sequence Editor](https://www.ni.com/docs/en-US/bundle/teststand/page/teststand-sequence-editor.html)
 to configure the
 Get Channel Values
 step.

The
 Get Channel Values
 settings panel contains the following configuration controls:

- Deployment - Specifies the deployment reference using the combo box suggestions.
 You can also use the variable from Step Reference Output control in the Connect step to specify the deployment reference. Refer to Step Reference Output in theConnect step for more details.
- Specify By Expression Checkbox - Specifies whether you provide the deployment reference using combo box selection or variables TestStand evaluates at run time.
- System Definition Path - Use this to enable channel selection when the system definition path cannot be evaluated at edit time from the deployment reference.
- Channels Table - The channels table can be used to configure the channels for the specified deployment.
 The Channels Table is only available when valid system definition is provided in the deployment or system definition path controls within this step. 
 The table has 3 columns:
  - Channels: You can specify a channel/model parameter/alias using the native VeriStand channel browser.
  - Units: Units of the selected channel value.
  - Channel value: Specify a TestStand variable to store the channel value.

<!--NI_TOPIC bundle=veristand-steps-for-teststand path=vsts_ref/open-veristand-project.html language=enus -->
## TOPIC 00010: Open VeriStand Project

- bundle_id: `veristand-steps-for-teststand`
- source_path: `vsts_ref/open-veristand-project.html`
- source_url: https://docs-be.ni.com/bundle/veristand-steps-for-teststand/raw/resource/enus/vsts_ref/open-veristand-project.html
- document_id: `veristand-steps-for-teststand`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Open VeriStand Project step to launch VeriStand application and open the specified VeriStand project. The file specified in this step serves as the source for file suggestions in successive TestStand Steps. Use the General edit tab in the TestStand Sequence Editor to configure the Open VeriS

### Open VeriStand Project

Use the
 Open VeriStand Project
 step to launch VeriStand application and open the specified VeriStand project. The file specified in this step serves as the source for file suggestions in successive TestStand Steps.

Use the
 General
 edit tab in the
 [TestStand Sequence Editor](https://www.ni.com/docs/en-US/bundle/teststand/page/teststand-sequence-editor.html)
 to configure the
 Open VeriStand Project
 step.

The
 Step Settings for Open VeriStand Project
 contains the following configuration controls:

- Project Path – Path to the VeriStand project you want to use.
- Specify By Expression Checkbox – Specifies whether you provide the project path using literal strings or expressions that TestStand evaluates at run time.
- Launch VeriStand Checkbox – Specifies whether to launch the VeriStand application.
 Note 
 If the VeriStand application is already running before this step is executed, the specified project may fail to open, and the step will issue a warning.
- User Interfaces
  - Specifies VeriStand screens to be opened on launching the VeriStand application. You can configure multiple VeriStand screens.
  - Show Workspace (Legacy) – Enable the checkbox to open the VeriStand Workspace window. This is not supported along with veristand-server.exe.

Note

Open VeriStand Project

Close VeriStand

<!--NI_TOPIC bundle=veristand-steps-for-teststand path=vsts_ref/run-real-time-sequence.html language=enus -->
## TOPIC 00011: Run Real-Time Sequence

- bundle_id: `veristand-steps-for-teststand`
- source_path: `vsts_ref/run-real-time-sequence.html`
- source_url: https://docs-be.ni.com/bundle/veristand-steps-for-teststand/raw/resource/enus/vsts_ref/run-real-time-sequence.html
- document_id: `veristand-steps-for-teststand`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Run Real-Time Sequence step to run a VeriStand Real-Time Sequence. Use the General edit tab in the TestStand Sequence Editor to configure the Run Real-Time Sequence step. The Run Real-Time Sequence settings panel contains the following configuration controls: Deployment - Specifies the deplo

### Run Real-Time Sequence

Use the
 Run Real-Time Sequence
 step to run a VeriStand Real-Time Sequence.

Use the
 General
 edit tab in the
 [TestStand Sequence Editor](https://www.ni.com/docs/en-US/bundle/teststand/page/teststand-sequence-editor.html)
 to configure the Run Real-Time Sequence step.

The Run Real-Time Sequence settings panel contains the following configuration controls:

- Deployment - Specifies the deployment reference using the combo box suggestions.
 You can also use the variable from Step Reference Output control in the Connect step to specify the deployment reference. Refer to Step Reference Output in the Connect step for more details.
- Specify By Expression Checkbox [Deployment] - Specifies whether you provide the deployment reference using combo box selection or variables TestStand evaluates at runtime.
- System Definition Path - Use this to enable channel selection when the system definition path cannot be evaluated at edit time from the deployment reference.
- Real-Time Sequence - Path to the NI VeriStand Real-Time Sequence file you want to run. Supported file types are ‘.nivsseq’ and ‘.csv’.
 Note 
 The suggestions displayed in the file path control are generated based on the project file configuration specified in the Open VeriStand Project step.
- Specify By Expression Checkbox [Real-Time Sequence] - Specifies whether you provide the real-time sequence path using literal strings or expressions TestStand evaluates at runtime.
- Target Name - The name of the target on which to execute the sequence. The suggestions are provided based on the system definition file configuration from deployment or the system definition path control.
- Time-Step Timeout - The timeout in milliseconds within which the sequence must complete each time step.
- Sequence Parameter Table - Auto-populated list of sequence parameters from the current real-time sequence selection. The parameter table is not supported if the real-time sequence is specified using TestStand expression/variable.
 The table contains the following columns:
  - Name: Name of the sequence parameter.
  - Description: Description of the sequence parameter.
  - DataType: Data type of the sequence parameter.
  - Units: Units associated with the variable value.
  - EvaluationMethod: Specifies whether the parameter is evaluated by value or by reference.
  - ValueType: Specifies whether the value is constant or channel.
  - ValueExpression: Specifies the sequence parameter value. A TestStand variable/expression can be used to configure the value.
- Step Reference Output - Returns a reference to the real-time sequence. Use a TestStand variable of type Object Reference.
  - You can specify a TestStand variable in the text box to store the real-time sequence reference.
  - By default, the real-time sequence reference is stored in a TestStand variable named OutputOf_<StepID> in the current sequence file context. This variable is accessible only in the current sequence file.
  - In the dependent step (e.g., Control Real-Time Sequence ), if you specify the real-time sequence reference using the combo box suggestions, the default variable would be used to get the reference. You can also use the same variable from the Step Reference Output in the Run Real-Time Sequence step to override the default variable and specify the real-time sequence reference.

The default variable created in the
 Run Real-Time Sequence
 panel is accessible only within the sequence file. If linking steps across sequence files, specify a TestStand variable to store the real-time sequence reference and pass this variable as a parameter in a sequence call to enable cross-file access.

<!--NI_TOPIC bundle=veristand-steps-for-teststand path=vsts_ref/set-channel-values.html language=enus -->
## TOPIC 00012: Set Channel Values

- bundle_id: `veristand-steps-for-teststand`
- source_path: `vsts_ref/set-channel-values.html`
- source_url: https://docs-be.ni.com/bundle/veristand-steps-for-teststand/raw/resource/enus/vsts_ref/set-channel-values.html
- document_id: `veristand-steps-for-teststand`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Set Channel Values step to specify values for available channels, aliases, or parameters available within the specified system definition. Use the General edit tab in the TestStand Sequence Editor to configure the Set Channel Values step. The Set Channel Values settings panel contains the fo

### Set Channel Values

Use the
 Set Channel Values
 step to specify values for available channels, aliases, or parameters available within the specified system definition.

Use the
 General
 edit tab in the
 [TestStand Sequence Editor](https://www.ni.com/docs/en-US/bundle/teststand/page/teststand-sequence-editor.html)
 to configure the
 Set Channel Values
 step.

The
 Set Channel Values
 settings panel contains the following configuration controls:

- Deployment - Specifies the deployment reference using the combo box suggestions.
 You can also use the variable from Step Reference Output control in the Connect step to specify the deployment reference. Refer to Step Reference Output in the Connect step for more details.
- Specify By Expression Checkbox - Specifies whether you provide the deployment reference using combo box selection or variables that TestStand evaluates at run time.
- System Definition Path - Use this to enable channel selection when the system definition path cannot be evaluated at edit time from the deployment reference.
- Channels Table - The channels table can be used to configure the channels for the specified deployment.
 The Channels Table is only available when valid system definition is provided in the deployment or system definition path controls within this step. 
 The table has three columns:
  - Channels: You can specify a channel/model parameter/alias using the native VeriStand channel browser.
  - Units: Units of the selected channel value.
  - Channel Value: Value to be configured for the channel. A constant or TestStand variable/expression can be used to specify a value.

<!--NI_TOPIC bundle=veristand-steps-for-teststand path=vsts_ref/start-logging.html language=enus -->
## TOPIC 00013: Start Logging

- bundle_id: `veristand-steps-for-teststand`
- source_path: `vsts_ref/start-logging.html`
- source_url: https://docs-be.ni.com/bundle/veristand-steps-for-teststand/raw/resource/enus/vsts_ref/start-logging.html
- document_id: `veristand-steps-for-teststand`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Start Logging step to log the channels configuration in the specified logging specification file. Use the General edit tab in the TestStand Sequence Editor to configure the Start Logging step. The Start Logging settings panel contains the following configuration controls: Deployment – Specif

### Start Logging

Use the
 Start Logging
 step to log the channels configuration in the specified logging specification file.

Use the
 General
 edit tab in the
 [TestStand Sequence Editor](https://www.ni.com/docs/en-US/bundle/teststand/page/teststand-sequence-editor.html)
 to configure the
 Start Logging
 step.

The
 Start Logging
 settings panel contains the following configuration controls:

- Deployment – Specifies the deployment reference using the combo box suggestions.
 You can also use the variable from Step Reference Output control in the Connect step to specify the deployment reference. Refer to Step Reference Output in the Connect step for more details.
- Specify By Expression Checkbox [Deployment] - Specifies whether you provide the deployment reference using combo box selection or variables that TestStand evaluates at run time.
- Logging Specification Path - Path to the NI VeriStand logging specification file you want to run.
 Note 
 The suggestions displayed in the file path control are generated based on the project file configuration specified in the Open VeriStand Project step.
- Specify By Expression Checkbox [Logging Specification Path] - Specifies whether you provide the logging specification path using literal strings or expressions that TestStand evaluates at run time.
- Step Reference Output - Returns a reference to the data logging session. Use a TestStand variable of type Object Reference.
  - You can specify a TestStand variable in the text box to store the data logging session reference.
  - By default, the data logging session reference is stored in a TestStand variable named OutputOf_<StepID> in the current sequence file context. This variable is accessible only in the current sequence file.
  - In the dependent step (e.g., Stop logging), if you specify the data logging session reference using the combo box suggestions, the default variable would be used to get the reference. You can also use the variable from Step Reference Output in the Start Logging step to override the default variable and specify the data logging session reference.

The default variable created in the Start Logging panel is accessible only within the sequence file. If linking steps across sequence files, specify a TestStand variable to store the data logging session reference and pass this variable as a parameter in a sequence call to enable cross-file access.

<!--NI_TOPIC bundle=veristand-steps-for-teststand path=vsts_ref/stop-logging.html language=enus -->
## TOPIC 00014: Stop Logging

- bundle_id: `veristand-steps-for-teststand`
- source_path: `vsts_ref/stop-logging.html`
- source_url: https://docs-be.ni.com/bundle/veristand-steps-for-teststand/raw/resource/enus/vsts_ref/stop-logging.html
- document_id: `veristand-steps-for-teststand`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Stop Logging step to stop the data logging session started by the Start Logging step. Use the General edit tab in the TestStand Sequence Editor to configure the Stop Logging step. The Stop Logging settings panel contains the following configuration controls: Logging Session – Specifies the d

### Stop Logging

Use the
 Stop Logging
 step to stop the data logging session started by the Start Logging step.

Use the
 General
 edit tab in the
 [TestStand Sequence Editor](https://www.ni.com/docs/en-US/bundle/teststand/page/teststand-sequence-editor.html)
 to configure the
 Stop Logging
 step.

The
 Stop Logging
 settings panel contains the following configuration controls:

- Logging Session – Specifies the data logging session reference using the combo box suggestions.
 You can also use the variable from Step Reference Output control in the Start Logging step to specify the data logging session reference. Refer to Step Reference Output in the Start Logging step for more details.
- Specify By Expression Checkbox - Specifies whether you provide the data logging session reference using combo box selection or variables that TestStand evaluates at run time.

<!--NI_TOPIC bundle=veristand-steps-for-teststand path=vsts_ref/wait-for-real-time-sequence.html language=enus -->
## TOPIC 00015: Wait for Real-Time Sequence

- bundle_id: `veristand-steps-for-teststand`
- source_path: `vsts_ref/wait-for-real-time-sequence.html`
- source_url: https://docs-be.ni.com/bundle/veristand-steps-for-teststand/raw/resource/enus/vsts_ref/wait-for-real-time-sequence.html
- document_id: `veristand-steps-for-teststand`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Wait for Real-Time Sequence step to wait for the Real-Time Sequence to complete the execution. Use the General edit tab in the TestStand Sequence Editor to configure the Wait for Real-Time Sequence step. The Wait for Real-Time Sequence settings panel contains the following configuration cont

### Wait for Real-Time Sequence

Use the
 Wait for Real-Time Sequence
 step to wait for the Real-Time Sequence to complete the execution.

Use the
 General
 edit tab in the
 [TestStand Sequence Editor](https://www.ni.com/docs/en-US/bundle/teststand/page/tsref/infotopics/seqeditor.htm)
 to configure the
 Wait for Real-Time Sequence
 step.

The
 Wait for Real-Time Sequence
 settings panel contains the following configuration controls:

- Real-Time Sequence – Specifies the real-time sequence reference using the combo box suggestions.
 You can also use the variable from Step Reference Output control in the Run Real-Time Sequence step to specify the real-time sequence reference. Refer to Step Reference Output in the Run Real-Time Sequence step for more details.
- Specify By Expression Checkbox - Specifies whether you provide the real-time sequence reference using combo box selection or variables that TestStand evaluates at run time.
- Result Expression - Optionally specify a TestStand variable to store the return value from a real-time Sequence.
- Timeout - The timeout in milliseconds within which the sequence must complete the action. A negative value indicates an infinite timeout.
