# NI DOCUMENT BUNDLE: veristand-net-api-ref

<!--NI_BUNDLE_CHUNK bundle=veristand-net-api-ref start=251 end=500 -->
<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-iproject-connect__bool.html language=enus -->
## TOPIC 00251: Connect(bool)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-iproject-connect__bool.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-iproject-connect__bool.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic Error Connect(bool show_progress)RemarksConnects an NI VeriStand project on the host computer to the target. This method only establishes a connection to a target. It does not deploy the system definition file. Use Deploy() to deploy a s

### Connect(bool)

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public [Error](nationalinstruments-veristand-clientapi-stimulusresult.html) Connect(bool show_progress)

#### Remarks

Connects an NI VeriStand project on the host computer to the target. This method only establishes a connection to a target. It does not deploy the system definition file. Use [Deploy()](nationalinstruments-veristand-clientapi-iproject-deploy.html) to deploy a system definition file to the target.

This method includes the option to display a connection progress dialog.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| show_progress | bool | Specifies whether to display a progress dialog while connecting. |

#### Returns

Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0.

Parent topic:

IProject Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-iproject-deploy.html language=enus -->
## TOPIC 00252: Deploy()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-iproject-deploy.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-iproject-deploy.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Deploys the system definition file associated with an NI VeriStand project to the target. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic Error Deploy()ReturnsReturns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0.

### Deploy()

Deploys the system definition file associated with an NI VeriStand project to the target.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public [Error](nationalinstruments-veristand-clientapi-stimulusresult.html) Deploy()

#### Returns

Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0.

Parent topic:

IProject Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-iproject-deploy__bool.html language=enus -->
## TOPIC 00253: Deploy(bool)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-iproject-deploy__bool.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-iproject-deploy__bool.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Deploys the system definition file associated with an NI VeriStand project to the target. This method includes the option to display a deployment progress dialog. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic Error Deploy(bool show_progress)ParametersNameTypeDescriptionshow_progress

### Deploy(bool)

Deploys the system definition file associated with an NI VeriStand project to the target. This method includes the option to display a deployment progress dialog.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public [Error](nationalinstruments-veristand-clientapi-stimulusresult.html) Deploy(bool show_progress)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| show_progress | bool | Specifies whether to display a progress dialog while deploying. |

#### Returns

Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0.

Parent topic:

IProject Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-iproject-disconnect.html language=enus -->
## TOPIC 00254: Disconnect()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-iproject-disconnect.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-iproject-disconnect.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Disconnects an NI VeriStand project from the target. This method does not stop execution of the system definition file on the target. If you want to stop execution, use Undeploy. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic Error Disconnect()ReturnsReturns an NationalInstruments.Ve

### Disconnect()

Disconnects an NI VeriStand project from the target. This method does not stop execution of the system definition file on the target. If you want to stop execution, use [Undeploy](nationalinstruments-veristand-clientapi-iproject-undeploy.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public [Error](nationalinstruments-veristand-clientapi-stimulusresult.html) Disconnect()

#### Returns

Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0.

Parent topic:

IProject Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-iproject-opentool__string.html language=enus -->
## TOPIC 00255: OpenTool(string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-iproject-opentool__string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-iproject-opentool__string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Opens a Workspace tool for an NI VeriStand project. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic Error OpenTool(string tool_path)ParametersNameTypeDescriptiontool_pathstringThe path to the Workspace tool VI.ReturnsReturns an NationalInstruments.VeriStand.Error object. If no error o

### OpenTool(string)

Opens a Workspace tool for an NI VeriStand project.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public [Error](nationalinstruments-veristand-clientapi-stimulusresult.html) OpenTool(string tool_path)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| tool_path | string | The path to the Workspace tool VI. |

#### Returns

Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0.

Parent topic:

IProject Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-iproject-openworkspace.html language=enus -->
## TOPIC 00256: OpenWorkspace()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-iproject-openworkspace.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-iproject-openworkspace.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Opens the Workspace window for an NI VeriStand project. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic Error OpenWorkspace()ReturnsReturns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0.

### OpenWorkspace()

Opens the **Workspace** window for an NI VeriStand project.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public [Error](nationalinstruments-veristand-clientapi-stimulusresult.html) OpenWorkspace()

#### Returns

Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0.

Parent topic:

IProject Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-iproject-quit.html language=enus -->
## TOPIC 00257: Quit()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-iproject-quit.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-iproject-quit.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sends a message to NI VeriStand to quit the project and application. When you call this method, the project disconnects from any targets to which it is connected, closes all tools including the Workspace window, and shuts down. Then NI VeriStand quits completely. SyntaxNamespace: NationalInstruments

### Quit()

Sends a message to NI VeriStand to quit the project and application. When you call this method, the project disconnects from any targets to which it is connected, closes all tools including the **Workspace** window, and shuts down. Then NI VeriStand quits completely.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public [Error](nationalinstruments-veristand-clientapi-stimulusresult.html) Quit()

#### Returns

Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0.

Parent topic:

IProject Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-iproject-run.html language=enus -->
## TOPIC 00258: Run()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-iproject-run.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-iproject-run.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Runs an NI VeriStand project. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic Error Run()ReturnsReturns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0.

### Run()

Runs an NI VeriStand project.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public [Error](nationalinstruments-veristand-clientapi-stimulusresult.html) Run()

#### Returns

Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0.

Parent topic:

IProject Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-iproject-run__bool.html language=enus -->
## TOPIC 00259: Run(bool)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-iproject-run__bool.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-iproject-run__bool.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Runs an NI VeriStand project. This method includes the option to display a progress dialog. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic Error Run(bool show_progress)ParametersNameTypeDescriptionshow_progressboolSpecifies whether to display the progress dialog.ReturnsReturns an Nat

### Run(bool)

Runs an NI VeriStand project. This method includes the option to display a progress dialog.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public [Error](nationalinstruments-veristand-clientapi-stimulusresult.html) Run(bool show_progress)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| show_progress | bool | Specifies whether to display the progress dialog. |

#### Returns

Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0.

Parent topic:

IProject Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-iproject-sendtoolmessage__string-string-byte_arr1-uint-out.html language=enus -->
## TOPIC 00260: SendToolMessage(string, string, byte[], uint, out byte[])

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-iproject-sendtoolmessage__string-string-byte_arr1-uint-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-iproject-sendtoolmessage__string-string-byte_arr1-uint-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sends a message or command to a Workspace tool for an NI VeriStand project, as well as data required by the case that handles the command. You can use this method with any Workspace tool that registers to receive the command you specify. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic

### SendToolMessage(string, string, byte[], uint, out byte[])

Sends a message or command to a Workspace tool for an NI VeriStand project, as well as data required by the case that handles the command. You can use this method with any Workspace tool that registers to receive the command you specify.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public [Error](nationalinstruments-veristand-clientapi-stimulusresult.html) SendToolMessage(string tool_path, string command, byte[] data, uint timeout, out byte[] response)

#### Remarks

This instance sends data to a tool as a byte array of 8-bit unsigned integer values. You also can use the other instance of [SendToolMessage(string, string, string, uint, out string)](nationalinstruments-veristand-clientapi-iproject-sendtoolmessage__string-string-string-uint-out.html) to send data as a string of human-readable characters.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| tool_path | string | The path to the tool VI. |
| command | string | The message or command to send to the tool. |
| data | byte[] | The data to send to the tool. |
| timeout | uint | The time in milliseconds to wait for a response from the tool before returning an error. |
| response | out byte[] | Returns the response from the tool to command . |

#### Returns

Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0.

Parent topic:

IProject Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-iproject-sendtoolmessage__string-string-string-uint-out.html language=enus -->
## TOPIC 00261: SendToolMessage(string, string, string, uint, out string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-iproject-sendtoolmessage__string-string-string-uint-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-iproject-sendtoolmessage__string-string-string-uint-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sends a message or command to a Workspace tool for an NI VeriStand project, as well as data required by the case that handles the command. You can use this method with any Workspace tool that registers to receive the command you specify. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic

### SendToolMessage(string, string, string, uint, out string)

Sends a message or command to a Workspace tool for an NI VeriStand project, as well as data required by the case that handles the command. You can use this method with any Workspace tool that registers to receive the *command*  you specify.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public [Error](nationalinstruments-veristand-clientapi-stimulusresult.html) SendToolMessage(string tool_path, string command, string data, uint timeout, out string response)

#### Remarks

This instance sends string data to a tool. You also can use the other instance of SendToolMessage(string, string, string, uint, out string) to send data as a byte array of 8-bit unsigned integer values.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| tool_path | string | The path to the tool VI. |
| command | string | The message or command to send to the tool. |
| data | string | The data to send to the tool. This input expects only human-readable string characters. If you send other string characters, such as a null character, this method might truncate the message during transmission to the tool. If the data you want to send contains null characters, convert the string to a byte array and use the other instance of SendToolMessage(string, string, string, uint, out string) to send the data to the tool. |
| timeout | uint | The time in milliseconds to wait for a response from the tool before returning an error. |
| response | out string | Returns the response from the tool to the command . |

#### Returns

Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0.

Parent topic:

IProject Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-iproject-undeploy.html language=enus -->
## TOPIC 00262: Undeploy()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-iproject-undeploy.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-iproject-undeploy.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Undeploys the system definition file associated with an NI VeriStand project from the target. Undeploying the system definition file stops execution on the target. If you want to disconnect from the target without stopping system definition file execution, use Disconnect. SyntaxNamespace: NationalIn

### Undeploy()

Undeploys the system definition file associated with an NI VeriStand project from the target. Undeploying the system definition file stops execution on the target. If you want to disconnect from the target without stopping system definition file execution, use [Disconnect](nationalinstruments-veristand-clientapi-iproject-disconnect.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public [Error](nationalinstruments-veristand-clientapi-stimulusresult.html) Undeploy()

#### Returns

Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0.

Parent topic:

IProject Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-iproject-visible.html language=enus -->
## TOPIC 00263: Visible

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-iproject-visible.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-iproject-visible.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the visible state of the NI VeriStand Project Explorer window. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic bool Visible { get; set; }ReturnsTRUE specifies that the window is visible.

### Visible

Gets or sets the visible state of the NI VeriStand **Project Explorer** window.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public bool Visible { get; set; }

#### Returns

TRUE specifies that the window is visible.

Parent topic:

IProject Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-iproject.html language=enus -->
## TOPIC 00264: IProject Interface

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-iproject.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-iproject.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Interface to automate an NI VeriStand project. Use the GetIProject(string, string, string, string) method of the Factory class to access this interface and specify the project you want to automate. Derives fromNoneSyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic interface IProjectPrope

### IProject Interface

Interface to automate an NI VeriStand project. Use the [GetIProject(string, string, string, string)](nationalinstruments-veristand-clientapi-factory-getiproject__string-string-string-string.html) method of the [Factory](nationalinstruments-veristand-clientapi-factory.html) class to access this interface and specify the project you want to automate.

#### Derives from

None

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public interface IProject

#### Properties

| Name | Description |
| --- | --- |
| Visible | Gets or sets the visible state of the NI VeriStand Project Explorer window. |

#### Methods

| Name | Description |
| --- | --- |
| Close() | Closes an NI VeriStand project along with the Workspace window and any Workspace tools. |
| CloseWorkspace() | Closes the Workspace window. |
| Connect() | Connects an NI VeriStand project on the host computer to the target. This method only establishes a connection to a target. It does not deploy the system definition file. Use Deploy() to deploy a system definition file to the target. |
| Connect(bool) |  |
| Deploy() | Deploys the system definition file associated with an NI VeriStand project to the target. |
| Deploy(bool) | Deploys the system definition file associated with an NI VeriStand project to the target. This method includes the option to display a deployment progress dialog. |
| Disconnect() | Disconnects an NI VeriStand project from the target. This method does not stop execution of the system definition file on the target. If you want to stop execution, use Undeploy. |
| OpenTool(string) | Opens a Workspace tool for an NI VeriStand project. |
| OpenWorkspace() | Opens the Workspace window for an NI VeriStand project. |
| Quit() | Sends a message to NI VeriStand to quit the project and application. When you call this method, the project disconnects from any targets to which it is connected, closes all tools including the Workspace window, and shuts down. Then NI VeriStand quits completely. |
| Run(bool) | Runs an NI VeriStand project. This method includes the option to display a progress dialog. |
| Run() | Runs an NI VeriStand project. |
| SendToolMessage(string, string, byte[], uint, out byte[]) | Sends a message or command to a Workspace tool for an NI VeriStand project, as well as data required by the case that handles the command. You can use this method with any Workspace tool that registers to receive the command you specify. |
| SendToolMessage(string, string, string, uint, out string) | Sends a message or command to a Workspace tool for an NI VeriStand project, as well as data required by the case that handles the command. You can use this method with any Workspace tool that registers to receive the command you specify. |
| Undeploy() | Undeploys the system definition file associated with an NI VeriStand project from the target. Undeploying the system definition file stops execution on the target. If you want to disconnect from the target without stopping system definition file execution, use Disconnect. |

Parent topic:

NationalInstruments.VeriStand.ClientAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-iruntimeconfigurationmanager-applyconfigurationtocustomdevice__string-string-uint.html language=enus -->
## TOPIC 00265: ApplyConfigurationToCustomDevice(string, string, uint)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-iruntimeconfigurationmanager-applyconfigurationtocustomdevice__string-string-uint.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-iruntimeconfigurationmanager-applyconfigurationtocustomdevice__string-string-uint.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Applies the configuration from the configurationFilePath to the runtime configurable section specified by runtimeConfigurableSectionPath . SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic Error ApplyConfigurationToCustomDevice(string runtimeConfigurableSectionPath, string configuration

### ApplyConfigurationToCustomDevice(string, string, uint)

Applies the configuration from the *configurationFilePath*  to the runtime configurable section specified by *runtimeConfigurableSectionPath* .

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public [Error](nationalinstruments-veristand-clientapi-stimulusresult.html) ApplyConfigurationToCustomDevice(string runtimeConfigurableSectionPath, string configurationFilePath, uint timeout)

#### Remarks

This method removes any previously applied configuration from the specified section before applying the new one.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| runtimeConfigurableSectionPath | string | Path to the Custom Device's runtime configurable section |
| configurationFilePath | string | Path to the file containing the runtime configuration |
| timeout | uint | Time in milliseconds to wait for the operation to complete before returning an error. |

#### Returns

Returns an [Error](nationalinstruments-veristand-clientapi-stimulusresult.html) object. If no error occurs, the Code property of the Error object is 0.

Parent topic:

IRuntimeConfigurationManager Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-iruntimeconfigurationmanager-applyconfigurationtocustomdevice__string-string.html language=enus -->
## TOPIC 00266: ApplyConfigurationToCustomDevice(string, string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-iruntimeconfigurationmanager-applyconfigurationtocustomdevice__string-string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-iruntimeconfigurationmanager-applyconfigurationtocustomdevice__string-string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Applies the configuration from the configurationFilePath to the runtime configurable section specified by runtimeConfigurableSectionPath . Note: The default timeout is 5000 milliseconds. Use the overloaded method to specify a different timeout value. SyntaxNamespace: NationalInstruments.VeriStand.Cl

### ApplyConfigurationToCustomDevice(string, string)

Applies the configuration from the *configurationFilePath*  to the runtime configurable section specified by *runtimeConfigurableSectionPath* . Note: The default timeout is 5000 milliseconds. Use the overloaded method to specify a different timeout value.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public [Error](nationalinstruments-veristand-clientapi-stimulusresult.html) ApplyConfigurationToCustomDevice(string runtimeConfigurableSectionPath, string configurationFilePath)

#### Remarks

This method removes any previously applied configuration from the specified section before applying the new one.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| runtimeConfigurableSectionPath | string | Path to the Custom Device's runtime configurable section |
| configurationFilePath | string | Path to the file containing the runtime configuration |

#### Returns

Returns an [Error](nationalinstruments-veristand-clientapi-stimulusresult.html) object. If no error occurs, the Code property of the Error object is 0.

Parent topic:

IRuntimeConfigurationManager Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-iruntimeconfigurationmanager-getactiveconfiguration__string-out-out.html language=enus -->
## TOPIC 00267: GetActiveConfiguration(string, out string, out string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-iruntimeconfigurationmanager-getactiveconfiguration__string-out-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-iruntimeconfigurationmanager-getactiveconfiguration__string-out-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the Runtime Configuration of the specified runtimeConfigurableSectionPath . SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic Error GetActiveConfiguration(string runtimeConfigurableSectionPath, out string configurationFilePath, out string configurationFileMD5Checksum)ParametersName

### GetActiveConfiguration(string, out string, out string)

Gets the Runtime Configuration of the specified *runtimeConfigurableSectionPath* .

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public [Error](nationalinstruments-veristand-clientapi-stimulusresult.html) GetActiveConfiguration(string runtimeConfigurableSectionPath, out string configurationFilePath, out string configurationFileMD5Checksum)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| runtimeConfigurableSectionPath | string | Path to the Custom Device's runtime configurable section. |
| configurationFilePath | out string | Path to the file containing the runtime configuration applied on runtimeConfigurableSectionPath . |
| configurationFileMD5Checksum | out string | MD5 of the configurationFilePath . |

#### Returns

Returns an [Error](nationalinstruments-veristand-clientapi-stimulusresult.html) object. If no error occurs, the Code property of the Error object is 0.

Parent topic:

IRuntimeConfigurationManager Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-iruntimeconfigurationmanager-getactiveconfigurationlist__out-out-out.html language=enus -->
## TOPIC 00268: GetActiveConfigurationList(out string[], out string[], out string[])

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-iruntimeconfigurationmanager-getactiveconfigurationlist__out-out-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-iruntimeconfigurationmanager-getactiveconfigurationlist__out-out-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the list of all Runtime Configurations. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic Error GetActiveConfigurationList(out string[] runtimeConfigurableSectionPaths, out string[] configurationFilePaths, out string[] configurationFileMD5Checksums)ParametersNameTypeDescriptionrunt

### GetActiveConfigurationList(out string[], out string[], out string[])

Gets the list of all Runtime Configurations.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public [Error](nationalinstruments-veristand-clientapi-stimulusresult.html) GetActiveConfigurationList(out string[] runtimeConfigurableSectionPaths, out string[] configurationFilePaths, out string[] configurationFileMD5Checksums)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| runtimeConfigurableSectionPaths | out string[] | The list of all custom device's runtime configurable section paths. |
| configurationFilePaths | out string[] | The list of all runtime configuration file paths. |
| configurationFileMD5Checksums | out string[] | The list of all MD5s of the configurationFilePaths . |

#### Returns

Returns an [Error](nationalinstruments-veristand-clientapi-stimulusresult.html) object. If no error occurs, the Code property of the Error object is 0.

Parent topic:

IRuntimeConfigurationManager Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-iruntimeconfigurationmanager-registerforruntimeconfigurationchange__string-eventhandler_runtimeconfigurationchangeeventargs..html language=enus -->
## TOPIC 00269: RegisterForRuntimeConfigurationChange(string, EventHandler< RuntimeConfigurationChangeEventArgs >)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-iruntimeconfigurationmanager-registerforruntimeconfigurationchange__string-eventhandler_runtimeconfigurationchangeeventargs..html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-iruntimeconfigurationmanager-registerforruntimeconfigurationchange__string-eventhandler_runtimeconfigurationchangeeventargs..html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Registers an event handler that will be invoked when a change is applied to a particular RuntimeConfigurableSection by the ApplyConfigurationToCustomDevice or RemoveConfigurationFromCustomDevice APIs. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic Error RegisterForRuntimeConfiguratio

### RegisterForRuntimeConfigurationChange(string, EventHandler< RuntimeConfigurationChangeEventArgs >)

Registers an event handler that will be invoked when a change is applied to a particular RuntimeConfigurableSection by the ApplyConfigurationToCustomDevice or RemoveConfigurationFromCustomDevice APIs.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public [Error](nationalinstruments-veristand-clientapi-stimulusresult.html) RegisterForRuntimeConfigurationChange(string runtimeConfigurableSectionPath, EventHandler< RuntimeConfigurationChangeEventArgs > runtimeConfigurationChangeEvent)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| runtimeConfigurableSectionPath | string | Path to the Custom Device's runtime configurable section. |
| runtimeConfigurationChangeEvent | EventHandler< RuntimeConfigurationChangeEventArgs > | Event handler to be called when the event is raised. |

#### Returns

Error indicating whether registration was successful (e.g. if the runtime configurable section was valid)

Parent topic:

IRuntimeConfigurationManager Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-iruntimeconfigurationmanager-removeconfigurationfromcustomdevice__string-uint.html language=enus -->
## TOPIC 00270: RemoveConfigurationFromCustomDevice(string, uint)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-iruntimeconfigurationmanager-removeconfigurationfromcustomdevice__string-uint.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-iruntimeconfigurationmanager-removeconfigurationfromcustomdevice__string-uint.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Removes the configurations from the specified section. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic Error RemoveConfigurationFromCustomDevice(string runtimeConfigurableSectionPath, uint timeout)ParametersNameTypeDescriptionruntimeConfigurableSectionPathstringPath to the Custom Devi

### RemoveConfigurationFromCustomDevice(string, uint)

Removes the configurations from the specified section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public [Error](nationalinstruments-veristand-clientapi-stimulusresult.html) RemoveConfigurationFromCustomDevice(string runtimeConfigurableSectionPath, uint timeout)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| runtimeConfigurableSectionPath | string | Path to the Custom Device's runtime configurable section. |
| timeout | uint | Time in milliseconds to wait for the operation to complete before returning an error. |

#### Returns

Returns an [Error](nationalinstruments-veristand-clientapi-stimulusresult.html) object. If no error occurs, the Code property of the Error object is 0.

Parent topic:

IRuntimeConfigurationManager Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-iruntimeconfigurationmanager-removeconfigurationfromcustomdevice__string.html language=enus -->
## TOPIC 00271: RemoveConfigurationFromCustomDevice(string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-iruntimeconfigurationmanager-removeconfigurationfromcustomdevice__string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-iruntimeconfigurationmanager-removeconfigurationfromcustomdevice__string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Removes the configurations from the specified section. Note: The default timeout is 5000 milliseconds. Use the overloaded method to specify a different timeout value. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic Error RemoveConfigurationFromCustomDevice(string runtimeConfigurableSe

### RemoveConfigurationFromCustomDevice(string)

Removes the configurations from the specified section. Note: The default timeout is 5000 milliseconds. Use the overloaded method to specify a different timeout value.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public [Error](nationalinstruments-veristand-clientapi-stimulusresult.html) RemoveConfigurationFromCustomDevice(string runtimeConfigurableSectionPath)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| runtimeConfigurableSectionPath | string | Path to the Custom Device's runtime configurable section. |

#### Returns

Returns an [Error](nationalinstruments-veristand-clientapi-stimulusresult.html) object. If no error occurs, the Code property of the Error object is 0.

Parent topic:

IRuntimeConfigurationManager Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-iruntimeconfigurationmanager-unregisterforruntimeconfigurationchange__string-eventhandler_runtimeconfigurationchangeeventargs..html language=enus -->
## TOPIC 00272: UnregisterForRuntimeConfigurationChange(string, EventHandler< RuntimeConfigurationChangeEventArgs >)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-iruntimeconfigurationmanager-unregisterforruntimeconfigurationchange__string-eventhandler_runtimeconfigurationchangeeventargs..html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-iruntimeconfigurationmanager-unregisterforruntimeconfigurationchange__string-eventhandler_runtimeconfigurationchangeeventargs..html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: UnRegisters an event handler that will be invoked when a change is applied to a particular RuntimeConfigurableSection by the ApplyConfigurationToCustomDevice or RemoveConfigurationFromCustomDevice APIs. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic Error UnregisterForRuntimeConfigur

### UnregisterForRuntimeConfigurationChange(string, EventHandler< RuntimeConfigurationChangeEventArgs >)

UnRegisters an event handler that will be invoked when a change is applied to a particular RuntimeConfigurableSection by the ApplyConfigurationToCustomDevice or RemoveConfigurationFromCustomDevice APIs.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public [Error](nationalinstruments-veristand-clientapi-stimulusresult.html) UnregisterForRuntimeConfigurationChange(string runtimeConfigurableSectionPath, EventHandler< RuntimeConfigurationChangeEventArgs > runtimeConfigurationChangeEvent)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| runtimeConfigurableSectionPath | string | Path to the Custom Device's runtime configurable section. |
| runtimeConfigurationChangeEvent | EventHandler< RuntimeConfigurationChangeEventArgs > | Event handler to be called when the event is raised. |

#### Returns

Error indicating whether unregistration was successful (e.g. if the runtime configurable section was valid)

Parent topic:

IRuntimeConfigurationManager Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-iruntimeconfigurationmanager.html language=enus -->
## TOPIC 00273: IRuntimeConfigurationManager Interface

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-iruntimeconfigurationmanager.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-iruntimeconfigurationmanager.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Interface to manage configurations that can be modified at runtime without the need to undeploy. Derives fromNoneSyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic interface IRuntimeConfigurationManagerMethodsNameDescriptionApplyConfigurationToCustomDevice(string, string, uint)Applies th

### IRuntimeConfigurationManager Interface

Interface to manage configurations that can be modified at runtime without the need to undeploy.

#### Derives from

None

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public interface IRuntimeConfigurationManager

#### Methods

| Name | Description |
| --- | --- |
| ApplyConfigurationToCustomDevice(string, string, uint) | Applies the configuration from the configurationFilePath to the runtime configurable section specified by runtimeConfigurableSectionPath . |
| ApplyConfigurationToCustomDevice(string, string) | Applies the configuration from the configurationFilePath to the runtime configurable section specified by runtimeConfigurableSectionPath . Note: The default timeout is 5000 milliseconds. Use the overloaded method to specify a different timeout value. |
| GetActiveConfiguration(string, out string, out string) | Gets the Runtime Configuration of the specified runtimeConfigurableSectionPath . |
| GetActiveConfigurationList(out string[], out string[], out string[]) | Gets the list of all Runtime Configurations. |
| RegisterForRuntimeConfigurationChange(string, EventHandler< RuntimeConfigurationChangeEventArgs >) | Registers an event handler that will be invoked when a change is applied to a particular RuntimeConfigurableSection by the ApplyConfigurationToCustomDevice or RemoveConfigurationFromCustomDevice APIs. |
| RemoveConfigurationFromCustomDevice(string) | Removes the configurations from the specified section. Note: The default timeout is 5000 milliseconds. Use the overloaded method to specify a different timeout value. |
| RemoveConfigurationFromCustomDevice(string, uint) | Removes the configurations from the specified section. |
| UnregisterForRuntimeConfigurationChange(string, EventHandler< RuntimeConfigurationChangeEventArgs >) | UnRegisters an event handler that will be invoked when a change is applied to a particular RuntimeConfigurableSection by the ApplyConfigurationToCustomDevice or RemoveConfigurationFromCustomDevice APIs. |

Parent topic:

NationalInstruments.VeriStand.ClientAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-isequencecontrol-abort.html language=enus -->
## TOPIC 00274: Abort()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-isequencecontrol-abort.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-isequencecontrol-abort.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Aborts the sequence. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic void Abort()

### Abort()

Aborts the sequence.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public void Abort()

Parent topic:

ISequenceControl Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-isequencecontrol-abort__out.html language=enus -->
## TOPIC 00275: Abort(out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-isequencecontrol-abort__out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-isequencecontrol-abort__out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Aborts the sequence. If an error occurs, this instance outputs an error object. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic void Abort(out Error error)ParametersNameTypeDescriptionerrorout ErrorThe error object.

### Abort(out Error)

Aborts the sequence. If an error occurs, this instance outputs an error object.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public void Abort(out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| error | out Error | The error object. |

Parent topic:

ISequenceControl Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-isequencecontrol-getreturnvalue.html language=enus -->
## TOPIC 00276: GetReturnValue()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-isequencecontrol-getreturnvalue.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-isequencecontrol-getreturnvalue.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the return value for the sequence. This function will fail if the sequence has not completed execution. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic DataValue GetReturnValue()ReturnsReturns the return value of the sequence.

### GetReturnValue()

Gets the return value for the sequence. This function will fail if the sequence has not completed execution.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public [DataValue](nationalinstruments-veristand-data-datavalue.html) GetReturnValue()

#### Returns

Returns the return value of the sequence.

Parent topic:

ISequenceControl Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-isequencecontrol-getreturnvalue__out.html language=enus -->
## TOPIC 00277: GetReturnValue(out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-isequencecontrol-getreturnvalue__out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-isequencecontrol-getreturnvalue__out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the return value for the sequence. This function will fail if the sequence has not completed execution. If an error occurs, this instance outputs an error object. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic DataValue GetReturnValue(out Error error)ParametersNameTypeDescriptio

### GetReturnValue(out Error)

Gets the return value for the sequence. This function will fail if the sequence has not completed execution. If an error occurs, this instance outputs an error object.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public [DataValue](nationalinstruments-veristand-data-datavalue.html) GetReturnValue(out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| error | out Error | The error object. |

#### Returns

Returns the return value of the sequence.

Parent topic:

ISequenceControl Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-isequencecontrol-getsequencetime.html language=enus -->
## TOPIC 00278: GetSequenceTime()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-isequencecontrol-getsequencetime.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-isequencecontrol-getsequencetime.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the relative time since the sequence started, as determined by the delta t at which the sequence executes and the number of executed iterations. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic double GetSequenceTime()ReturnsReturns the relative time since the sequence started.

### GetSequenceTime()

Gets the relative time since the sequence started, as determined by the delta t at which the sequence executes and the number of executed iterations.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public double GetSequenceTime()

#### Returns

Returns the relative time since the sequence started.

Parent topic:

ISequenceControl Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-isequencecontrol-getsequencetime__out.html language=enus -->
## TOPIC 00279: GetSequenceTime(out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-isequencecontrol-getsequencetime__out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-isequencecontrol-getsequencetime__out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the relative time since the sequence started, as determined by the delta t at which the sequence executes and the number of executed iterations. If an error occurs, this instance outputs an error object. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic double GetSequenceTime(out E

### GetSequenceTime(out Error)

Gets the relative time since the sequence started, as determined by the delta t at which the sequence executes and the number of executed iterations. If an error occurs, this instance outputs an error object.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public double GetSequenceTime(out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| error | out Error | The error object. |

#### Returns

Returns the relative time since the sequence started.

Parent topic:

ISequenceControl Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-isequencecontrol-instancenumber.html language=enus -->
## TOPIC 00280: InstanceNumber

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-isequencecontrol-instancenumber.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-isequencecontrol-instancenumber.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the instance number of the sequence. This corresponds to the nth time this sequence appears in the stimulus profile session. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic int InstanceNumber { get; }

### InstanceNumber

Gets the instance number of the sequence. This corresponds to the *n*th time this sequence appears in the stimulus profile session.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public int InstanceNumber { get; }

Parent topic:

ISequenceControl Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-isequencecontrol-name.html language=enus -->
## TOPIC 00281: Name

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-isequencecontrol-name.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-isequencecontrol-name.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the qualified name of the sequence, which identifies the sequence in the stimulus profile session. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic string Name { get; }

### Name

Gets the qualified name of the sequence, which identifies the sequence in the stimulus profile session.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public string Name { get; }

Parent topic:

ISequenceControl Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-isequencecontrol-owner.html language=enus -->
## TOPIC 00282: Owner

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-isequencecontrol-owner.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-isequencecontrol-owner.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the owning stimulus profile session. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic IStimulusProfileSession Owner { get; }

### Owner

Gets the owning stimulus profile session.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public [IStimulusProfileSession](nationalinstruments-veristand-clientapi-istimulusprofilesession.html) Owner { get; }

Parent topic:

ISequenceControl Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-isequencecontrol-pause.html language=enus -->
## TOPIC 00283: Pause()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-isequencecontrol-pause.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-isequencecontrol-pause.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Pauses the sequence. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic void Pause()

### Pause()

Pauses the sequence.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public void Pause()

Parent topic:

ISequenceControl Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-isequencecontrol-pause__out.html language=enus -->
## TOPIC 00284: Pause(out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-isequencecontrol-pause__out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-isequencecontrol-pause__out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Pauses the sequence. If an error occurs, this instance outputs an error object. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic void Pause(out Error error)ParametersNameTypeDescriptionerrorout ErrorThe error object.

### Pause(out Error)

Pauses the sequence. If an error occurs, this instance outputs an error object.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public void Pause(out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| error | out Error | The error object. |

Parent topic:

ISequenceControl Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-isequencecontrol-run.html language=enus -->
## TOPIC 00285: Run()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-isequencecontrol-run.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-isequencecontrol-run.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Runs the sequence. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic void Run()

### Run()

Runs the sequence.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public void Run()

Parent topic:

ISequenceControl Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-isequencecontrol-run__out.html language=enus -->
## TOPIC 00286: Run(out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-isequencecontrol-run__out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-isequencecontrol-run__out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Runs the sequence. If an error occurs, this instance outputs an error object. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic void Run(out Error error)ParametersNameTypeDescriptionerrorout ErrorThe error object.

### Run(out Error)

Runs the sequence. If an error occurs, this instance outputs an error object.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public void Run(out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| error | out Error | The error object. |

Parent topic:

ISequenceControl Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-isequencecontrol-sequence.html language=enus -->
## TOPIC 00287: Sequence

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-isequencecontrol-sequence.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-isequencecontrol-sequence.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the sequence configuration data. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic SequenceCallInfo Sequence { get; }

### Sequence

Gets the sequence configuration data.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public [SequenceCallInfo](nationalinstruments-veristand-clientapi-sequencecallinfo.html) Sequence { get; }

Parent topic:

ISequenceControl Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-isequencecontrol-sequencecomplete.html language=enus -->
## TOPIC 00288: SequenceComplete

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-isequencecontrol-sequencecomplete.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-isequencecontrol-sequencecomplete.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Event triggered when a sequence completes execution. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic DOnSequenceComplete SequenceComplete

### SequenceComplete

Event triggered when a sequence completes execution.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public [DOnSequenceComplete](nationalinstruments-veristand-clientapi-donsequencecomplete__object-sequencecompleteeventargs.html) SequenceComplete

Parent topic:

ISequenceControl Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-isequencecontrol-singlestep.html language=enus -->
## TOPIC 00289: SingleStep()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-isequencecontrol-singlestep.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-isequencecontrol-singlestep.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Single-steps the sequence. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic void SingleStep()

### SingleStep()

Single-steps the sequence.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public void SingleStep()

Parent topic:

ISequenceControl Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-isequencecontrol-singlestep__out.html language=enus -->
## TOPIC 00290: SingleStep(out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-isequencecontrol-singlestep__out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-isequencecontrol-singlestep__out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Single-steps the sequence. If an error occurs, this instance outputs an error object. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic void SingleStep(out Error error)ParametersNameTypeDescriptionerrorout ErrorThe error object.

### SingleStep(out Error)

Single-steps the sequence. If an error occurs, this instance outputs an error object.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public void SingleStep(out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| error | out Error | The error object. |

Parent topic:

ISequenceControl Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-isequencecontrol-state.html language=enus -->
## TOPIC 00291: State

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-isequencecontrol-state.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-isequencecontrol-state.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the current execution state of the sequence. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic SequenceState State { get; }

### State

Gets the current execution state of the sequence.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public [SequenceState](nationalinstruments-veristand-clientapi-sequencestate.html) State { get; }

Parent topic:

ISequenceControl Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-isequencecontrol-statechange.html language=enus -->
## TOPIC 00292: StateChange

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-isequencecontrol-statechange.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-isequencecontrol-statechange.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Event triggered when a sequence changes execution state. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic DOnSequenceStateChange StateChange

### StateChange

Event triggered when a sequence changes execution state.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public [DOnSequenceStateChange](nationalinstruments-veristand-clientapi-donsequencestatechange__object-sequencestatechangeeventargs.html) StateChange

Parent topic:

ISequenceControl Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-isequencecontrol-stop.html language=enus -->
## TOPIC 00293: Stop()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-isequencecontrol-stop.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-isequencecontrol-stop.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Stops the sequence. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic void Stop()

### Stop()

Stops the sequence.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public void Stop()

Parent topic:

ISequenceControl Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-isequencecontrol-stop__out.html language=enus -->
## TOPIC 00294: Stop(out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-isequencecontrol-stop__out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-isequencecontrol-stop__out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Stops the sequence. If an error occurs, this instance outputs an error object. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic void Stop(out Error error)ParametersNameTypeDescriptionerrorout ErrorThe error object.

### Stop(out Error)

Stops the sequence. If an error occurs, this instance outputs an error object.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public void Stop(out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| error | out Error | The error object. |

Parent topic:

ISequenceControl Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-isequencecontrol.html language=enus -->
## TOPIC 00295: ISequenceControl Interface

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-isequencecontrol.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-isequencecontrol.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Automates and monitors the execution of a sequence in a stimulus profile session. Derives fromNoneSyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic interface ISequenceControlPropertiesNameDescriptionInstanceNumberGets the instance number of the sequence. This corresponds to the nth time

### ISequenceControl Interface

Automates and monitors the execution of a sequence in a stimulus profile session.

#### Derives from

None

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public interface ISequenceControl

#### Properties

| Name | Description |
| --- | --- |
| InstanceNumber | Gets the instance number of the sequence. This corresponds to the nth time this sequence appears in the stimulus profile session. |
| Name | Gets the qualified name of the sequence, which identifies the sequence in the stimulus profile session. |
| Owner | Gets the owning stimulus profile session. |
| Sequence | Gets the sequence configuration data. |
| State | Gets the current execution state of the sequence. |

#### Methods

| Name | Description |
| --- | --- |
| Abort(out Error) | Aborts the sequence. If an error occurs, this instance outputs an error object. |
| Abort() | Aborts the sequence. |
| GetReturnValue(out Error) | Gets the return value for the sequence. This function will fail if the sequence has not completed execution. If an error occurs, this instance outputs an error object. |
| GetReturnValue() | Gets the return value for the sequence. This function will fail if the sequence has not completed execution. |
| GetSequenceTime() | Gets the relative time since the sequence started, as determined by the delta t at which the sequence executes and the number of executed iterations. |
| GetSequenceTime(out Error) | Gets the relative time since the sequence started, as determined by the delta t at which the sequence executes and the number of executed iterations. If an error occurs, this instance outputs an error object. |
| Pause(out Error) | Pauses the sequence. If an error occurs, this instance outputs an error object. |
| Pause() | Pauses the sequence. |
| Run() | Runs the sequence. |
| Run(out Error) | Runs the sequence. If an error occurs, this instance outputs an error object. |
| SingleStep() | Single-steps the sequence. |
| SingleStep(out Error) | Single-steps the sequence. If an error occurs, this instance outputs an error object. |
| Stop(out Error) | Stops the sequence. If an error occurs, this instance outputs an error object. |
| Stop() | Stops the sequence. |

#### Events

| Name | Description |
| --- | --- |
| SequenceComplete | Event triggered when a sequence completes execution. |
| StateChange | Event triggered when a sequence changes execution state. |

Parent topic:

NationalInstruments.VeriStand.ClientAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-istimulus-getstimulusprofilefile__out.html language=enus -->
## TOPIC 00296: GetStimulusProfileFile(out string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-istimulus-getstimulusprofilefile__out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-istimulus-getstimulusprofilefile__out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the stimulus profile file that is running on the target. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic Error GetStimulusProfileFile(out string file_path)RemarksThe method is valid for the original version of the NI VeriStand Stimulus Profile Editor only. In NI VeriStand 2011 an

### GetStimulusProfileFile(out string)

Gets the stimulus profile file that is running on the target.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public [Error](nationalinstruments-veristand-clientapi-stimulusresult.html) GetStimulusProfileFile(out string file_path)

#### Remarks

The method is valid for the original version of the NI VeriStand Stimulus Profile Editor only. In NI VeriStand 2011 and later, this method is maintained for compatibility purposes only. Use the members of the Stimulus Profile Execution API to interact with stimulus profiles in NI VeriStand 2011 and later.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| file_path | out string | Returns the path to the stimulus profile file. |

#### Returns

Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0.

Parent topic:

IStimulus Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-istimulus-getstimulusprofilemanagerstate__out.html language=enus -->
## TOPIC 00297: GetStimulusProfileManagerState(out StimulusState)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-istimulus-getstimulusprofilemanagerstate__out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-istimulus-getstimulusprofilemanagerstate__out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the state of the stimulus profile manager. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic Error GetStimulusProfileManagerState(out StimulusState state)RemarksThe method is valid for the original version of the NI VeriStand Stimulus Profile Editor only. In NI VeriStand 2011 and l

### GetStimulusProfileManagerState(out StimulusState)

Gets the state of the stimulus profile manager.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public [Error](nationalinstruments-veristand-clientapi-stimulusresult.html) GetStimulusProfileManagerState(out StimulusState state)

#### Remarks

The method is valid for the original version of the NI VeriStand Stimulus Profile Editor only. In NI VeriStand 2011 and later, this method is maintained for compatibility purposes only. Use the members of the Stimulus Profile Execution API to interact with stimulus profiles in NI VeriStand 2011 and later.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| state | out StimulusState | The StimulusState of the stimulus profile manager. |

#### Returns

Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0.

Parent topic:

IStimulus Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-istimulus-getstimulusprofileresult__out-out.html language=enus -->
## TOPIC 00298: GetStimulusProfileResult(out StimulusResult, out string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-istimulus-getstimulusprofileresult__out-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-istimulus-getstimulusprofileresult__out-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the results of the last stimulus profile that ran on the target, including whether it passed, failed, or received an error. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic Error GetStimulusProfileResult(out StimulusResult result, out string file_result)RemarksThe method is valid

### GetStimulusProfileResult(out StimulusResult, out string)

Gets the results of the last stimulus profile that ran on the target, including whether it passed, failed, or received an error.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public [Error](nationalinstruments-veristand-clientapi-stimulusresult.html) GetStimulusProfileResult(out StimulusResult result, out string file_result)

#### Remarks

The method is valid for the original version of the NI VeriStand Stimulus Profile Editor only. In NI VeriStand 2011 and later, this method is maintained for compatibility purposes. Use the members of the Stimulus Profile Execution API to interact with stimulus profiles in NI VeriStand 2011 and later.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| result | out StimulusResult | The StimulusResult of the stimulus profile. |
| file_result | out string | The file name of a .csv file containing the results of the last stimulus profile file that ran on the target. |

#### Returns

Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0.

Parent topic:

IStimulus Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-istimulus-reservestimulusprofilemanager.html language=enus -->
## TOPIC 00299: ReserveStimulusProfileManager()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-istimulus-reservestimulusprofilemanager.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-istimulus-reservestimulusprofilemanager.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reserves the stimulus profile manager and prevents other clients from running stimulus profile files. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic Error ReserveStimulusProfileManager()RemarksThe method is valid for the original version of the NI VeriStand Stimulus Profile Editor on

### ReserveStimulusProfileManager()

Reserves the stimulus profile manager and prevents other clients from running stimulus profile files.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public [Error](nationalinstruments-veristand-clientapi-stimulusresult.html) ReserveStimulusProfileManager()

#### Remarks

The method is valid for the original version of the NI VeriStand Stimulus Profile Editor only. In NI VeriStand 2011 and later, this method is maintained for compatibility purposes only. Use the members of the Stimulus Profile Execution API to interact with stimulus profiles in NI VeriStand 2011 and later.

#### Returns

Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0.

Parent topic:

IStimulus Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-istimulus-runstimulusprofile__string-string-uint-bool-bool.html language=enus -->
## TOPIC 00300: RunStimulusProfile(string, string, uint, bool, bool)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-istimulus-runstimulusprofile__string-string-uint-bool-bool.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-istimulus-runstimulusprofile__string-string-uint-bool-bool.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: This method is deprecated in NI VeriStand 2010 and later. Use the RunStimulusProfile instance in the IStimulus2 interface instead. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic Error RunStimulusProfile(string file_path, string base_log_path, uint timeout, bool auto_start, bool stop_

### RunStimulusProfile(string, string, uint, bool, bool)

This method is deprecated in NI VeriStand 2010 and later. Use the [RunStimulusProfile](nationalinstruments-veristand-clientapi-istimulus2-runstimulusprofile__string-string-uint-bool-bool-string_arr1.html) instance in the [IStimulus2](nationalinstruments-veristand-clientapi-istimulus2.html) interface instead.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public [Error](nationalinstruments-veristand-clientapi-stimulusresult.html) RunStimulusProfile(string file_path, string base_log_path, uint timeout, bool auto_start, bool stop_on_disconnect)

#### Remarks

Runs a stimulus profile and logs data to a TDMS file in the directory you specify.

The method is valid for the original version of the NI VeriStand Stimulus Profile Editor only. In NI VeriStand 2011 and later, this method is maintained for compatibility purposes only. Use the members of the Stimulus Profile Execution API to interact with stimulus profiles in NI VeriStand 2011 and later.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| file_path | string | The path to the stimulus profile file. |
| base_log_path | string | The directory where NI VeriStand saves the logged TDMS files for the stimulus profile. This parameter applies only to relative log file paths. If this parameter is empty, this method saves the log files in a default location. |
| timeout | uint | The length of time in milliseconds to wait for the stimulus profile to start the test before the operation times out. |
| auto_start | bool | Specifies whether to start running the stimulus profile file on the target as soon as the file finishes downloading. If false, you must use an external trigger, such as a custom device, to start running the stimulus profile file on the target. |
| stop_on_disconnect | bool | Specifies whether to stop running the stimulus profile file on the target when you disconnect from the target. If false, the stimulus profile file continues running on the target after you close NI VeriStand and disconnect from the target. |

#### Returns

Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0.

Parent topic:

IStimulus Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-istimulus-stopstimulusprofile.html language=enus -->
## TOPIC 00301: StopStimulusProfile()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-istimulus-stopstimulusprofile.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-istimulus-stopstimulusprofile.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Stops the currently running stimulus profile file. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic Error StopStimulusProfile()RemarksThe method is valid for the original version of the NI VeriStand Stimulus Profile Editor only. In NI VeriStand 2011 and later, this method is maintained

### StopStimulusProfile()

Stops the currently running stimulus profile file.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public [Error](nationalinstruments-veristand-clientapi-stimulusresult.html) StopStimulusProfile()

#### Remarks

The method is valid for the original version of the NI VeriStand Stimulus Profile Editor only. In NI VeriStand 2011 and later, this method is maintained for compatibility purposes only. Use the members of the Stimulus Profile Execution API to interact with stimulus profiles in NI VeriStand 2011 and later.

#### Returns

Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0.

Parent topic:

IStimulus Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-istimulus-unreservestimulusprofilemanager.html language=enus -->
## TOPIC 00302: UnreserveStimulusProfileManager()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-istimulus-unreservestimulusprofilemanager.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-istimulus-unreservestimulusprofilemanager.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Unreserves the stimulus profile manager. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic Error UnreserveStimulusProfileManager()RemarksThe method is valid for the original version of the NI VeriStand Stimulus Profile Editor only. In NI VeriStand 2011 and later, this method is maintain

### UnreserveStimulusProfileManager()

Unreserves the stimulus profile manager.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public [Error](nationalinstruments-veristand-clientapi-stimulusresult.html) UnreserveStimulusProfileManager()

#### Remarks

The method is valid for the original version of the NI VeriStand Stimulus Profile Editor only. In NI VeriStand 2011 and later, this method is maintained for compatibility purposes only. Use the members of the Stimulus Profile Execution API to interact with stimulus profiles in NI VeriStand 2011 and later.

#### Returns

Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0.

Parent topic:

IStimulus Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-istimulus.html language=enus -->
## TOPIC 00303: IStimulus Interface

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-istimulus.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-istimulus.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Some members of this interface are deprecated in NI VeriStand 2010 and later. Use the IStimulusProfileSession interface instead. Derives fromNoneSyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic interface IStimulusRemarksInterface to control stimulus generation. The members of this inte

### IStimulus Interface

Some members of this interface are deprecated in NI VeriStand 2010 and later. Use the [IStimulusProfileSession](nationalinstruments-veristand-clientapi-istimulusprofilesession.html) interface instead.

#### Derives from

None

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public interface IStimulus

#### Remarks

Interface to control stimulus generation.

The members of this interface control stimulus generation in the original version of the NI VeriStand Stimulus Profile Editor. In NI VeriStand 2011 and later, this interface is maintained for compatibility purposes only. Use the members of the Stimulus Profile Execution API to interact with stimulus profiles in NI VeriStand 2011 and later.

#### Methods

| Name | Description |
| --- | --- |
| GetStimulusProfileFile(out string) | Gets the stimulus profile file that is running on the target. |
| GetStimulusProfileManagerState(out StimulusState) | Gets the state of the stimulus profile manager. |
| GetStimulusProfileResult(out StimulusResult, out string) | Gets the results of the last stimulus profile that ran on the target, including whether it passed, failed, or received an error. |
| ReserveStimulusProfileManager() | Reserves the stimulus profile manager and prevents other clients from running stimulus profile files. |
| RunStimulusProfile(string, string, uint, bool, bool) | This method is deprecated in NI VeriStand 2010 and later. Use the RunStimulusProfile instance in the IStimulus2 interface instead. |
| StopStimulusProfile() | Stops the currently running stimulus profile file. |
| UnreserveStimulusProfileManager() | Unreserves the stimulus profile manager. |

Parent topic:

NationalInstruments.VeriStand.ClientAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-istimulus2-runstimulusprofile__string-string-uint-bool-bool-string_arr1.html language=enus -->
## TOPIC 00304: RunStimulusProfile(string, string, uint, bool, bool, string[])

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-istimulus2-runstimulusprofile__string-string-uint-bool-bool-string_arr1.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-istimulus2-runstimulusprofile__string-string-uint-bool-bool-string_arr1.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Start the stimulus generation defined by the file. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic Error RunStimulusProfile(string file_path, string base_log_path, uint timeout, bool auto_start, bool stop_on_disconnect, string[] parameter_files)RemarksThe method is valid for the origi

### RunStimulusProfile(string, string, uint, bool, bool, string[])

Start the stimulus generation defined by the file.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public [Error](nationalinstruments-veristand-clientapi-stimulusresult.html) RunStimulusProfile(string file_path, string base_log_path, uint timeout, bool auto_start, bool stop_on_disconnect, string[] parameter_files)

#### Remarks

The method is valid for the original version of the NI VeriStand Stimulus Profile Editor only. In NI VeriStand 2011 and later, this method is maintained for compatibility purposes only. Use the members of the Stimulus Profile Execution API to interact with stimulus profiles in NI VeriStand 2011 and later.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| file_path | string | The path to the stimulus profile file. |
| base_log_path | string | The directory where NI VeriStand saves the logged TDMS files for the stimulus profile. This parameter applies only to relative log file paths. If this parameter is empty, this method saves the log files in a default location. |
| timeout | uint | The length of time in milliseconds to wait for the stimulus profile to start the test before the operation times out. |
| auto_start | bool | Specifies whether to start running the stimulus profile file on the target as soon as the file finishes downloading. If false, you must use an external trigger, such as a custom device, to start running the stimulus profile file on the execution host. |
| stop_on_disconnect | bool | Specifies whether to stop running the stimulus profile file on the target when you disconnect from the target. If false, the stimulus profile file continues running on the execution host after you close NI VeriStand and disconnect from the execution host. |
| parameter_files | string[] | The file paths of custom model parameter files to apply. If you do not specify custom parameter files, this method uses the parameter files stored in the stimulus profile file. |

#### Returns

Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0.

Parent topic:

IStimulus2 Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-istimulus2.html language=enus -->
## TOPIC 00305: IStimulus2 Interface

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-istimulus2.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-istimulus2.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: This interface is deprecated in VeriStand 2011 and later. Use the IStimulusProfileSession interface instead. Interface to control stimulus generation. Use the GetIStimulus2 method of the Factory class to access this interface. Derives fromIStimulusSyntaxNamespace: NationalInstruments.VeriStand.Clien

### IStimulus2 Interface

This interface is deprecated in VeriStand 2011 and later. Use the [IStimulusProfileSession](nationalinstruments-veristand-clientapi-istimulusprofilesession.html) interface instead. Interface to control stimulus generation. Use the [GetIStimulus2](nationalinstruments-veristand-clientapi-factory-getistimulus2__string.html) method of the [Factory](nationalinstruments-veristand-clientapi-factory.html) class to access this interface.

#### Derives from

- IStimulus

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public interface IStimulus2 : IStimulus

#### Remarks

This interface also inherits the methods of the [IStimulus](nationalinstruments-veristand-clientapi-istimulus.html) interface.

The members of this interface control stimulus generation in the original version of the NI VeriStand Stimulus Profile Editor. In NI VeriStand 2011 and later, this interface is maintained for compatibility purposes only. Use the members of the Stimulus Profile Execution API to interact with stimulus profiles in NI VeriStand 2011 and later.

#### Methods

| Name | Description |
| --- | --- |
| RunStimulusProfile(string, string, uint, bool, bool, string[]) | Start the stimulus generation defined by the file. |

Parent topic:

NationalInstruments.VeriStand.ClientAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-istimulusprofilesession-abort.html language=enus -->
## TOPIC 00306: Abort()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-istimulusprofilesession-abort.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-istimulusprofilesession-abort.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Aborts the Stimulus Profile Session. If an error occurs, this instance throws an exception. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic void Abort()

### Abort()

Aborts the Stimulus Profile Session. If an error occurs, this instance throws an exception.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public void Abort()

Parent topic:

IStimulusProfileSession Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-istimulusprofilesession-abort__out.html language=enus -->
## TOPIC 00307: Abort(out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-istimulusprofilesession-abort__out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-istimulusprofilesession-abort__out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Aborts the Stimulus Profile Session. If an error occurs, this instance outputs an error object. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic void Abort(out Error error)ParametersNameTypeDescriptionerrorout ErrorThe error object.

### Abort(out Error)

Aborts the Stimulus Profile Session. If an error occurs, this instance outputs an *error*  object.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public void Abort(out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| error | out Error | The error object. |

Parent topic:

IStimulusProfileSession Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-istimulusprofilesession-deploy__bool-out-out.html language=enus -->
## TOPIC 00308: Deploy(bool, out string, out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-istimulusprofilesession-deploy__bool-out-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-istimulusprofilesession-deploy__bool-out-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Deploys the Stimulus Profile Session. If an error occurs, this instance outputs an error object. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic void Deploy(bool auto_start, out string session_id, out Error error)ParametersNameTypeDescriptionauto_startboolIf true, starts sequences imm

### Deploy(bool, out string, out Error)

Deploys the Stimulus Profile Session. If an error occurs, this instance outputs an *error*  object.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public void Deploy(bool auto_start, out string session_id, out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| auto_start | bool | If true, starts sequences immediately upon deploy. If false, waits for an external Run command. |
| session_id | out string | The ID of the Stimulus Profile Session. |
| error | out Error | The error object. |

Parent topic:

IStimulusProfileSession Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-istimulusprofilesession-deploy__bool-out.html language=enus -->
## TOPIC 00309: Deploy(bool, out string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-istimulusprofilesession-deploy__bool-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-istimulusprofilesession-deploy__bool-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Deploys the Stimulus Profile Session. If an error occurs, this instance throws an exception. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic void Deploy(bool auto_start, out string session_id)ParametersNameTypeDescriptionauto_startboolIf true, starts sequences immediately upon deploy.

### Deploy(bool, out string)

Deploys the Stimulus Profile Session. If an error occurs, this instance throws an exception.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public void Deploy(bool auto_start, out string session_id)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| auto_start | bool | If true, starts sequences immediately upon deploy. If false, waits for an external Run command. |
| session_id | out string | The ID of the Stimulus profile session. |

Parent topic:

IStimulusProfileSession Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-istimulusprofilesession-deployed.html language=enus -->
## TOPIC 00310: Deployed

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-istimulusprofilesession-deployed.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-istimulusprofilesession-deployed.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates whether the Stimulus Profile Session is deployed. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic bool Deployed { get; }Returnstrue if the session is deployed.

### Deployed

Indicates whether the Stimulus Profile Session is deployed.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public bool Deployed { get; }

#### Returns

true if the session is deployed.

Parent topic:

IStimulusProfileSession Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-istimulusprofilesession-description.html language=enus -->
## TOPIC 00311: Description

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-istimulusprofilesession-description.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-istimulusprofilesession-description.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the description of the Stimulus Profile Session. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic string Description { get; }

### Description

Gets the description of the Stimulus Profile Session.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public string Description { get; }

Parent topic:

IStimulusProfileSession Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-istimulusprofilesession-lock__string-string-out.html language=enus -->
## TOPIC 00312: Lock(string, string, out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-istimulusprofilesession-lock__string-string-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-istimulusprofilesession-lock__string-string-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Locks the Stimulus Profile Session with the new_password . If the session is locked, any attempts to modify its execution state fail. If an error occurs, this instance outputs an error object. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic void Lock(string old_password, string new_pa

### Lock(string, string, out Error)

Locks the Stimulus Profile Session with the *new_password* . If the session is locked, any attempts to modify its execution state fail. If an error occurs, this instance outputs an error object.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public void Lock(string old_password, string new_password, out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| old_password | string | The previous password for the Stimulus Profile Session. If the session is not already locked, this parameter is ignored. |
| new_password | string | The password to use to lock the Stimulus Profile Session. The session does not lock if this string is empty. |
| error | out Error | The error object. |

Parent topic:

IStimulusProfileSession Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-istimulusprofilesession-lock__string-string.html language=enus -->
## TOPIC 00313: Lock(string, string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-istimulusprofilesession-lock__string-string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-istimulusprofilesession-lock__string-string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Locks the Stimulus Profile Session with the new_password . If the session is locked, any attempts to modify its execution state fail. If an error occurs, this instance throws an exception. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic void Lock(string old_password, string new_passwo

### Lock(string, string)

Locks the Stimulus Profile Session with the *new_password* . If the session is locked, any attempts to modify its execution state fail. If an error occurs, this instance throws an exception.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public void Lock(string old_password, string new_password)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| old_password | string | The previous password for the Stimulus Profile Session. If the session is not already locked, this parameter is ignored. |
| new_password | string | The password to use to lock the Stimulus Profile Session. The session does not lock if this string is empty. |

Parent topic:

IStimulusProfileSession Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-istimulusprofilesession-locked.html language=enus -->
## TOPIC 00314: Locked

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-istimulusprofilesession-locked.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-istimulusprofilesession-locked.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates whether the Stimulus Profile Session is locked. If the session is locked, any attempts to modify its execution state fail. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic bool Locked { get; }Returnstrue if the session is locked.

### Locked

Indicates whether the Stimulus Profile Session is locked. If the session is locked, any attempts to modify its execution state fail.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public bool Locked { get; }

#### Returns

true if the session is locked.

Parent topic:

IStimulusProfileSession Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-istimulusprofilesession-name.html language=enus -->
## TOPIC 00315: Name

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-istimulusprofilesession-name.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-istimulusprofilesession-name.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the name of the Stimulus Profile Session. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic string Name { get; }

### Name

Gets the name of the Stimulus Profile Session.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public string Name { get; }

Parent topic:

IStimulusProfileSession Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-istimulusprofilesession-pause.html language=enus -->
## TOPIC 00316: Pause()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-istimulusprofilesession-pause.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-istimulusprofilesession-pause.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Pauses the Stimulus Profile Session. If an error occurs, this instance throws an exception. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic void Pause()

### Pause()

Pauses the Stimulus Profile Session. If an error occurs, this instance throws an exception.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public void Pause()

Parent topic:

IStimulusProfileSession Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-istimulusprofilesession-pause__out.html language=enus -->
## TOPIC 00317: Pause(out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-istimulusprofilesession-pause__out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-istimulusprofilesession-pause__out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Pauses the Stimulus Profile Session. If an error occurs, this instance outputs an error object. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic void Pause(out Error error)ParametersNameTypeDescriptionerrorout ErrorThe error object.

### Pause(out Error)

Pauses the Stimulus Profile Session. If an error occurs, this instance outputs an error object.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public void Pause(out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| error | out Error | The error object. |

Parent topic:

IStimulusProfileSession Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-istimulusprofilesession-run.html language=enus -->
## TOPIC 00318: Run()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-istimulusprofilesession-run.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-istimulusprofilesession-run.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Runs the Stimulus Profile Session. If an error occurs, this instance throws an exception. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic void Run()

### Run()

Runs the Stimulus Profile Session. If an error occurs, this instance throws an exception.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public void Run()

Parent topic:

IStimulusProfileSession Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-istimulusprofilesession-run__out.html language=enus -->
## TOPIC 00319: Run(out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-istimulusprofilesession-run__out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-istimulusprofilesession-run__out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Runs the Stimulus Profile Session. If an error occurs, this instance outputs an error object. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic void Run(out Error error)ParametersNameTypeDescriptionerrorout ErrorThe error object.

### Run(out Error)

Runs the Stimulus Profile Session. If an error occurs, this instance outputs an error object.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public void Run(out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| error | out Error | The error object. |

Parent topic:

IStimulusProfileSession Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-istimulusprofilesession-sequencenames.html language=enus -->
## TOPIC 00320: SequenceNames

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-istimulusprofilesession-sequencenames.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-istimulusprofilesession-sequencenames.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the qualified sequence names of all the sequences in the Stimulus Profile Session. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic string[] SequenceNames { get; }

### SequenceNames

Gets the qualified sequence names of all the sequences in the Stimulus Profile Session.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public string[] SequenceNames { get; }

Parent topic:

IStimulusProfileSession Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-istimulusprofilesession-sessioncomplete.html language=enus -->
## TOPIC 00321: SessionComplete

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-istimulusprofilesession-sessioncomplete.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-istimulusprofilesession-sessioncomplete.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Callback invoked when the session finishes execution. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic DOnSessionComplete SessionComplete

### SessionComplete

Callback invoked when the session finishes execution.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public [DOnSessionComplete](nationalinstruments-veristand-clientapi-donsessioncomplete__object-eventargs.html) SessionComplete

Parent topic:

IStimulusProfileSession Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-istimulusprofilesession-sessionundeploy.html language=enus -->
## TOPIC 00322: SessionUndeploy

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-istimulusprofilesession-sessionundeploy.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-istimulusprofilesession-sessionundeploy.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Callback invoked when the session is undeployed. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic DOnSessionUndeploy SessionUndeploy

### SessionUndeploy

Callback invoked when the session is undeployed.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public [DOnSessionUndeploy](nationalinstruments-veristand-clientapi-donsessionundeploy__object-eventargs.html) SessionUndeploy

Parent topic:

IStimulusProfileSession Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-istimulusprofilesession-singlestep.html language=enus -->
## TOPIC 00323: SingleStep()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-istimulusprofilesession-singlestep.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-istimulusprofilesession-singlestep.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Single-steps the Stimulus Profile Session. If an error occurs, this instance throws an exception. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic void SingleStep()

### SingleStep()

Single-steps the Stimulus Profile Session. If an error occurs, this instance throws an exception.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public void SingleStep()

Parent topic:

IStimulusProfileSession Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-istimulusprofilesession-singlestep__out.html language=enus -->
## TOPIC 00324: SingleStep(out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-istimulusprofilesession-singlestep__out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-istimulusprofilesession-singlestep__out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Single-steps the Stimulus Profile Session. If an error occurs, this instance outputs an error object. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic void SingleStep(out Error error)ParametersNameTypeDescriptionerrorout ErrorThe error object.

### SingleStep(out Error)

Single-steps the Stimulus Profile Session. If an error occurs, this instance outputs an error object.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public void SingleStep(out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| error | out Error | The error object. |

Parent topic:

IStimulusProfileSession Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-istimulusprofilesession-stop.html language=enus -->
## TOPIC 00325: Stop()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-istimulusprofilesession-stop.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-istimulusprofilesession-stop.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Stops the Stimulus Profile Session. If an error occurs, this instance throws an exception. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic void Stop()

### Stop()

Stops the Stimulus Profile Session. If an error occurs, this instance throws an exception.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public void Stop()

Parent topic:

IStimulusProfileSession Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-istimulusprofilesession-stop__out.html language=enus -->
## TOPIC 00326: Stop(out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-istimulusprofilesession-stop__out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-istimulusprofilesession-stop__out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Stops the Stimulus Profile Session. If an error occurs, this instance outputs an error object. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic void Stop(out Error error)ParametersNameTypeDescriptionerrorout ErrorThe error object.

### Stop(out Error)

Stops the Stimulus Profile Session. If an error occurs, this instance outputs an error object.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public void Stop(out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| error | out Error | The error object. |

Parent topic:

IStimulusProfileSession Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-istimulusprofilesession-this__string.html language=enus -->
## TOPIC 00327: this[string sequence_name]

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-istimulusprofilesession-this__string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-istimulusprofilesession-this__string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a reference to the sequence specified by the qualified sequence name in the Stimulus Profile Session. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic ISequenceControl this[string sequence_name] { get; }ParametersNameTypeDescriptionsequence_namestringThe sequence for which to get

### this[string sequence_name]

Gets a reference to the sequence specified by the qualified sequence name in the Stimulus Profile Session.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public [ISequenceControl](nationalinstruments-veristand-clientapi-isequencecontrol.html) this[string sequence_name] { get; }

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| sequence_name | string | The sequence for which to get the reference. |

Parent topic:

IStimulusProfileSession Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-istimulusprofilesession-undeploy.html language=enus -->
## TOPIC 00328: Undeploy()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-istimulusprofilesession-undeploy.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-istimulusprofilesession-undeploy.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Undeploys the Stimulus Profile Session. If an error occurs, this instance throws an exception. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic void Undeploy()

### Undeploy()

Undeploys the Stimulus Profile Session. If an error occurs, this instance throws an exception.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public void Undeploy()

Parent topic:

IStimulusProfileSession Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-istimulusprofilesession-undeploy__out.html language=enus -->
## TOPIC 00329: Undeploy(out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-istimulusprofilesession-undeploy__out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-istimulusprofilesession-undeploy__out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Undeploys the Stimulus Profile Session. If an error occurs, this instance outputs an error object. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic void Undeploy(out Error error)ParametersNameTypeDescriptionerrorout ErrorThe error object.

### Undeploy(out Error)

Undeploys the Stimulus Profile Session. If an error occurs, this instance outputs an error object.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public void Undeploy(out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| error | out Error | The error object. |

Parent topic:

IStimulusProfileSession Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-istimulusprofilesession-unlock__string-out.html language=enus -->
## TOPIC 00330: Unlock(string, out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-istimulusprofilesession-unlock__string-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-istimulusprofilesession-unlock__string-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Unlocks the Stimulus Profile Session. If an error occurs, this instance outputs an error object. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic void Unlock(string password, out Error error)ParametersNameTypeDescriptionpasswordstringThe password for the locked session.errorout ErrorTh

### Unlock(string, out Error)

Unlocks the Stimulus Profile Session. If an error occurs, this instance outputs an error object.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public void Unlock(string password, out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| password | string | The password for the locked session. |
| error | out Error | The error object. |

Parent topic:

IStimulusProfileSession Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-istimulusprofilesession-unlock__string.html language=enus -->
## TOPIC 00331: Unlock(string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-istimulusprofilesession-unlock__string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-istimulusprofilesession-unlock__string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Unlocks the Stimulus Profile Session. If an error occurs, this instance throws an exception. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic void Unlock(string password)ParametersNameTypeDescriptionpasswordstringThe password for the locked session.

### Unlock(string)

Unlocks the Stimulus Profile Session. If an error occurs, this instance throws an exception.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public void Unlock(string password)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| password | string | The password for the locked session. |

Parent topic:

IStimulusProfileSession Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-istimulusprofilesession.html language=enus -->
## TOPIC 00332: IStimulusProfileSession Interface

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-istimulusprofilesession.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-istimulusprofilesession.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Interface to control and monitor Stimulus Profile Session execution. Derives fromNoneSyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic interface IStimulusProfileSessionRemarksUse the GetIStimulusProfileSession(string, string, SequenceCallInfo[], string) method of the Factory class to ac

### IStimulusProfileSession Interface

Interface to control and monitor Stimulus Profile Session execution.

#### Derives from

None

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public interface IStimulusProfileSession

#### Remarks

Use the [GetIStimulusProfileSession(string, string, SequenceCallInfo[], string)](nationalinstruments-veristand-clientapi-factory-getistimulusprofilesession__string-string-sequencecallinfo_arr1-string.html) method of the [Factory](nationalinstruments-veristand-clientapi-factory.html) class to access this interface.

#### Properties

| Name | Description |
| --- | --- |
| Deployed | Indicates whether the Stimulus Profile Session is deployed. |
| Description | Gets the description of the Stimulus Profile Session. |
| Locked | Indicates whether the Stimulus Profile Session is locked. If the session is locked, any attempts to modify its execution state fail. |
| Name | Gets the name of the Stimulus Profile Session. |
| SequenceNames | Gets the qualified sequence names of all the sequences in the Stimulus Profile Session. |
| this[string sequence_name] | Gets a reference to the sequence specified by the qualified sequence name in the Stimulus Profile Session. |

#### Methods

| Name | Description |
| --- | --- |
| Abort(out Error) | Aborts the Stimulus Profile Session. If an error occurs, this instance outputs an error object. |
| Abort() | Aborts the Stimulus Profile Session. If an error occurs, this instance throws an exception. |
| Deploy(bool, out string) | Deploys the Stimulus Profile Session. If an error occurs, this instance throws an exception. |
| Deploy(bool, out string, out Error) | Deploys the Stimulus Profile Session. If an error occurs, this instance outputs an error object. |
| Lock(string, string) | Locks the Stimulus Profile Session with the new_password . If the session is locked, any attempts to modify its execution state fail. If an error occurs, this instance throws an exception. |
| Lock(string, string, out Error) | Locks the Stimulus Profile Session with the new_password . If the session is locked, any attempts to modify its execution state fail. If an error occurs, this instance outputs an error object. |
| Pause() | Pauses the Stimulus Profile Session. If an error occurs, this instance throws an exception. |
| Pause(out Error) | Pauses the Stimulus Profile Session. If an error occurs, this instance outputs an error object. |
| Run(out Error) | Runs the Stimulus Profile Session. If an error occurs, this instance outputs an error object. |
| Run() | Runs the Stimulus Profile Session. If an error occurs, this instance throws an exception. |
| SingleStep() | Single-steps the Stimulus Profile Session. If an error occurs, this instance throws an exception. |
| SingleStep(out Error) | Single-steps the Stimulus Profile Session. If an error occurs, this instance outputs an error object. |
| Stop(out Error) | Stops the Stimulus Profile Session. If an error occurs, this instance outputs an error object. |
| Stop() | Stops the Stimulus Profile Session. If an error occurs, this instance throws an exception. |
| Undeploy() | Undeploys the Stimulus Profile Session. If an error occurs, this instance throws an exception. |
| Undeploy(out Error) | Undeploys the Stimulus Profile Session. If an error occurs, this instance outputs an error object. |
| Unlock(string, out Error) | Unlocks the Stimulus Profile Session. If an error occurs, this instance outputs an error object. |
| Unlock(string) | Unlocks the Stimulus Profile Session. If an error occurs, this instance throws an exception. |

#### Events

| Name | Description |
| --- | --- |
| SessionComplete | Callback invoked when the session finishes execution. |
| SessionUndeploy | Callback invoked when the session is undeployed. |

Parent topic:

NationalInstruments.VeriStand.ClientAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-iudpchannelstreamsession-byteorder.html language=enus -->
## TOPIC 00333: ByteOrder

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-iudpchannelstreamsession-byteorder.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-iudpchannelstreamsession-byteorder.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets a value indicating the byte order for the UDP data. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic ByteOrder ByteOrder { get; set; }

### ByteOrder

Gets or sets a value indicating the byte order for the UDP data.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public [ByteOrder](nationalinstruments-veristand-clientapi-byteorder.html) ByteOrder { get; set; }

Parent topic:

IUDPChannelStreamSession Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-iudpchannelstreamsession-clientport.html language=enus -->
## TOPIC 00334: ClientPort

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-iudpchannelstreamsession-clientport.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-iudpchannelstreamsession-clientport.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets a value indicating the port on the client to which to stream the UDP data. This value is ignored if Multicast is true. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic ushort ClientPort { get; set; }

### ClientPort

Gets or sets a value indicating the port on the client to which to stream the UDP data. This value is ignored if Multicast is true.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public ushort ClientPort { get; set; }

Parent topic:

IUDPChannelStreamSession Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-iudpchannelstreamsession-deployudpchannelstreamsession__out-out-out-out-out.html language=enus -->
## TOPIC 00335: DeployUDPChannelStreamSession(out string, out ushort, out int, out int[], out int[])

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-iudpchannelstreamsession-deployudpchannelstreamsession__out-out-out-out-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-iudpchannelstreamsession-deployudpchannelstreamsession__out-out-out-out-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Deploys the UDP Channel Stream session. The VeriStand Gateway publishes the channels specified by this session to a UDP multicast address. The maximum size of a UDP packet over IPv4 is 65,535 bytes. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic Error DeployUDPChannelStreamSession(ou

### DeployUDPChannelStreamSession(out string, out ushort, out int, out int[], out int[])

Deploys the UDP Channel Stream session. The VeriStand Gateway publishes the channels specified by this session to a UDP multicast address.

Note

The maximum size of a UDP packet over IPv4 is 65,535 bytes.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public [Error](nationalinstruments-veristand-clientapi-stimulusresult.html) DeployUDPChannelStreamSession(out string address, out ushort port, out int max_packet_size, out int[] channel_ids, out int[] packet_ids)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| address | out string | The multicast address to which the VeriStand Gateway publishes the data. |
| port | out ushort | The multicast address port to which the VeriStand Gateway publishes the data. |
| max_packet_size | out int | The maximum UDP packet size, in bytes, that the VeriStand Gateway successfully published. |
| channel_ids | out int[] | The channel IDs for each channel in the session. Each UDP packet contains a list of channel IDs that it uses to look up channel data. |
| packet_ids | out int[] | The packet IDs. The VeriStand Gateway might publish one or more packets corresponding to this stream session. |

#### Returns

Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0.

Parent topic:

IUDPChannelStreamSession Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-iudpchannelstreamsession-maxrate.html language=enus -->
## TOPIC 00336: MaxRate

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-iudpchannelstreamsession-maxrate.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-iudpchannelstreamsession-maxrate.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets a value indicating the maximum rate at which to stream UDP data. The actual stream rate will be coerced to an even divisor of the individual target rates in the system definition. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic double MaxRate { get; set; }

### MaxRate

Gets or sets a value indicating the maximum rate at which to stream UDP data. The actual stream rate will be coerced to an even divisor of the individual target rates in the system definition.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public double MaxRate { get; set; }

Parent topic:

IUDPChannelStreamSession Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-iudpchannelstreamsession-multicast.html language=enus -->
## TOPIC 00337: Multicast

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-iudpchannelstreamsession-multicast.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-iudpchannelstreamsession-multicast.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets a value indicating whether to broadcast the UDP data to a multicast address. If this value is false, the UDP data will be sent directly to the client address that deploys the UDP stream session. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic bool Multicast { get; set; }

### Multicast

Gets or sets a value indicating whether to broadcast the UDP data to a multicast address. If this value is false, the UDP data will be sent directly to the client address that deploys the UDP stream session.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public bool Multicast { get; set; }

Parent topic:

IUDPChannelStreamSession Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-iudpchannelstreamsession-undeployudpchannelstreamsession.html language=enus -->
## TOPIC 00338: UndeployUDPChannelStreamSession()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-iudpchannelstreamsession-undeployudpchannelstreamsession.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-iudpchannelstreamsession-undeployudpchannelstreamsession.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Undeploys a UDP channel streaming session and instructs the VeriStand Gateway to stop publishing UDP data. If a client has a request open for a channel, the VeriStand Gateway continues to publish data even after this method executes. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic Err

### UndeployUDPChannelStreamSession()

Undeploys a UDP channel streaming session and instructs the VeriStand Gateway to stop publishing UDP data.

Note

If a client has a request open for a channel, the VeriStand Gateway continues to publish data even after this method executes.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public [Error](nationalinstruments-veristand-clientapi-stimulusresult.html) UndeployUDPChannelStreamSession()

#### Returns

Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0.

Parent topic:

IUDPChannelStreamSession Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-iudpchannelstreamsession.html language=enus -->
## TOPIC 00339: IUDPChannelStreamSession Interface

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-iudpchannelstreamsession.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-iudpchannelstreamsession.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Interface for deploying and undeploying UDP Channel Stream sessions. Derives fromNoneSyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic interface IUDPChannelStreamSessionRemarksUse the GetIUDPChannelStreamSession method of the IWorkspace2 interface to access this interface. PropertiesNam

### IUDPChannelStreamSession Interface

Interface for deploying and undeploying UDP Channel Stream sessions.

#### Derives from

None

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public interface IUDPChannelStreamSession

#### Remarks

Use the [GetIUDPChannelStreamSession](nationalinstruments-veristand-clientapi-iworkspace2-getiudpchannelstreamsession__string_arr1.html) method of the [IWorkspace2](nationalinstruments-veristand-clientapi-iworkspace2.html) interface to access this interface.

#### Properties

| Name | Description |
| --- | --- |
| ByteOrder | Gets or sets a value indicating the byte order for the UDP data. |
| ClientPort | Gets or sets a value indicating the port on the client to which to stream the UDP data. This value is ignored if Multicast is true. |
| MaxRate | Gets or sets a value indicating the maximum rate at which to stream UDP data. The actual stream rate will be coerced to an even divisor of the individual target rates in the system definition. |
| Multicast | Gets or sets a value indicating whether to broadcast the UDP data to a multicast address. If this value is false, the UDP data will be sent directly to the client address that deploys the UDP stream session. |

#### Methods

| Name | Description |
| --- | --- |
| DeployUDPChannelStreamSession(out string, out ushort, out int, out int[], out int[]) | Deploys the UDP Channel Stream session. The VeriStand Gateway publishes the channels specified by this session to a UDP multicast address. Note The maximum size of a UDP packet over IPv4 is 65,535 bytes. |
| UndeployUDPChannelStreamSession() | Undeploys a UDP channel streaming session and instructs the VeriStand Gateway to stop publishing UDP data. Note If a client has a request open for a channel, the VeriStand Gateway continues to publish data even after this method executes. |

Parent topic:

NationalInstruments.VeriStand.ClientAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-iworkspace-getaliaslist__out-out.html language=enus -->
## TOPIC 00340: GetAliasList(out string[], out string[])

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-iworkspace-getaliaslist__out-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-iworkspace-getaliaslist__out-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets all the aliases defined for channels in the system, and the channels to which each alias corresponds. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic Error GetAliasList(out string[] aliases, out string[] channels)ParametersNameTypeDescriptionaliasesout string[]The list of all the

### GetAliasList(out string[], out string[])

Gets all the aliases defined for channels in the system, and the channels to which each alias corresponds.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public [Error](nationalinstruments-veristand-clientapi-stimulusresult.html) GetAliasList(out string[] aliases, out string[] channels)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| aliases | out string[] | The list of all the aliases defined for channels on the target. |
| channels | out string[] | The names of the channels that correspond to the aliases . |

#### Returns

Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0.

Parent topic:

IWorkspace Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-iworkspace-getchannelvectorvalues__string-out-out-out.html language=enus -->
## TOPIC 00341: GetChannelVectorValues(string, out uint, out uint, out double[])

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-iworkspace-getchannelvectorvalues__string-out-out-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-iworkspace-getchannelvectorvalues__string-out-out-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the vector values of a channel on the target. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic Error GetChannelVectorValues(string channel, out uint rowDim, out uint colDim, out double[] values)RemarksUse the IModelManager2 interface for getting the model parameter values. Targets

### GetChannelVectorValues(string, out uint, out uint, out double[])

Gets the vector values of a channel on the target.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public [Error](nationalinstruments-veristand-clientapi-stimulusresult.html) GetChannelVectorValues(string channel, out uint rowDim, out uint colDim, out double[] values)

#### Remarks

Use the [IModelManager2](nationalinstruments-veristand-clientapi-imodelmanager2.html) interface for getting the model parameter values.

Targets/Controller/Simulation Models/Models/delay_random/Inports/In1

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| channel | string | The name of the channel. You must enter the full path to the channel as specified in the system definition file. For example: |

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| rowDim | out uint | The number of rows in the vector array. |
| colDim | out uint | The number of columns in the vector array. |
| values | out double[] | The vector values. |

#### Returns

Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0.

Parent topic:

IWorkspace Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-iworkspace-getenginestate__out-out-out-out.html language=enus -->
## TOPIC 00342: GetEngineState(out SystemState, out string, out string, out string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-iworkspace-getenginestate__out-out-out-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-iworkspace-getenginestate__out-out-out-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: This method is deprecated in NI VeriStand 2010 and later. Use the GetSystemState method instead. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic Error GetEngineState(out SystemState state, out string workspace_file, out string systemdefinition_file, out string ip_address)RemarksReturn

### GetEngineState(out SystemState, out string, out string, out string)

This method is deprecated in NI VeriStand 2010 and later. Use the [GetSystemState](nationalinstruments-veristand-clientapi-iworkspace2-getsystemstate__out-out-out.html) method instead.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public [Error](nationalinstruments-veristand-clientapi-stimulusresult.html) GetEngineState(out SystemState state, out string workspace_file, out string systemdefinition_file, out string ip_address)

#### Remarks

Returns the current state of the VeriStand Engine.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| state | out SystemState | The current SystemState of the VeriStand Engine. |
| workspace_file | out string | The current system definition file. The workspace file does not exist in NI VeriStand 2010 and later. |
| systemdefinition_file | out string | The current system definition file. |
| ip_address | out string | The IP address of the system. |

#### Returns

Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0.

Parent topic:

IWorkspace Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-iworkspace-getmultiplechannelvalues__string_arr1-out.html language=enus -->
## TOPIC 00343: GetMultipleChannelValues(string[], out double[])

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-iworkspace-getmultiplechannelvalues__string_arr1-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-iworkspace-getmultiplechannelvalues__string_arr1-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the values of multiple scalar channels running on the target. To get the values of vector channels, use the GetChannelVectorValues method. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic Error GetMultipleChannelValues(string[] names, out double[] newValues)RemarksUse the IModelMa

### GetMultipleChannelValues(string[], out double[])

Gets the values of multiple scalar channels running on the target. To get the values of vector channels, use the [GetChannelVectorValues](nationalinstruments-veristand-clientapi-iworkspace-getchannelvectorvalues__string-out-out-out.html) method.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public [Error](nationalinstruments-veristand-clientapi-stimulusresult.html) GetMultipleChannelValues(string[] names, out double[] newValues)

#### Remarks

Use the [IModelManager2](nationalinstruments-veristand-clientapi-imodelmanager2.html) interface for getting the model parameter values.

Targets/Controller/Simulation Models/Models/delay_random/Inports/In1

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| names | string[] | The names of the channels. You must enter the full path to each channel as specified in the system definition file. For example: |

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| newValues | out double[] | The values of the specified channels. |

#### Returns

Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0.

Parent topic:

IWorkspace Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-iworkspace-getmultiplesystemnodesdata__string_arr1-out.html language=enus -->
## TOPIC 00344: GetMultipleSystemNodesData(string[], out NodeInfo[])

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-iworkspace-getmultiplesystemnodesdata__string_arr1-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-iworkspace-getmultiplesystemnodesdata__string_arr1-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets information about multiple nodes in the system definition file. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic Error GetMultipleSystemNodesData(string[] names, out NodeInfo[] infos)Remarks Targets/Controller/Simulation Models/Models/delay_random/Inports/In1 ParametersNameTypeDes

### GetMultipleSystemNodesData(string[], out NodeInfo[])

Gets information about multiple nodes in the system definition file.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public [Error](nationalinstruments-veristand-clientapi-stimulusresult.html) GetMultipleSystemNodesData(string[] names, out NodeInfo[] infos)

#### Remarks

Targets/Controller/Simulation Models/Models/delay_random/Inports/In1

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| names | string[] | The names of the nodes. You must enter the full path to each node as specified in the system definition file. For example: |

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| infos | out NodeInfo[] | Information about the nodes. Refer to the NodeInfo class for more information about the types of data this parameter returns. |

#### Returns

Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0.

Parent topic:

IWorkspace Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-iworkspace-getsinglechannelvalue__string-out.html language=enus -->
## TOPIC 00345: GetSingleChannelValue(string, out double)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-iworkspace-getsinglechannelvalue__string-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-iworkspace-getsinglechannelvalue__string-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the value of a single channel on the target. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic Error GetSingleChannelValue(string name, out double newVal)RemarksUse the IModelManager2 interface for getting the model parameter values. Targets/Controller/Simulation Models/Models/dela

### GetSingleChannelValue(string, out double)

Gets the value of a single channel on the target.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public [Error](nationalinstruments-veristand-clientapi-stimulusresult.html) GetSingleChannelValue(string name, out double newVal)

#### Remarks

Use the [IModelManager2](nationalinstruments-veristand-clientapi-imodelmanager2.html) interface for getting the model parameter values.

Targets/Controller/Simulation Models/Models/delay_random/Inports/In1

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | The name of the channel. You must enter the full path to the channel as specified in the system definition file. For example: |

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| newVal | out double | The value of the specified channel. |

#### Returns

Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0.

Parent topic:

IWorkspace Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-iworkspace-getsystemnodechannellist__string-out.html language=enus -->
## TOPIC 00346: GetSystemNodeChannelList(string, out NodeInfo[])

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-iworkspace-getsystemnodechannellist__string-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-iworkspace-getsystemnodechannellist__string-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a list of all the channels under the nodeName you specify. This method performs a recursive search. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic Error GetSystemNodeChannelList(string nodeName, out NodeInfo[] channels)ParametersNameTypeDescriptionnodeNamestringThe name of the n

### GetSystemNodeChannelList(string, out NodeInfo[])

Gets a list of all the channels under the *nodeName*  you specify. This method performs a recursive search.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public [Error](nationalinstruments-veristand-clientapi-stimulusresult.html) GetSystemNodeChannelList(string nodeName, out NodeInfo[] channels)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| nodeName | string | The name of the node for which you want to see all channels. If this parameter is empty, this method gets all the channels in the system. |
| channels | out NodeInfo[] | An array containing information about all the channels. You can index this array and use the members of the NodeInfo class to get specific information about each channel, such as its name, path, GUID, and whether it is readable, writable, scalable, faultable, and so on. |

#### Returns

Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0.

Parent topic:

IWorkspace Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-iworkspace-getsystemnodechildren__string-out.html language=enus -->
## TOPIC 00347: GetSystemNodeChildren(string, out NodeInfo[])

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-iworkspace-getsystemnodechildren__string-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-iworkspace-getsystemnodechildren__string-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets all child nodes, including channels, of the nodeName you specify. This method does not perform a recursive search. You can use the GetSystemNodeChannelList to perform a recursive search of all the channels under a specified node. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic Er

### GetSystemNodeChildren(string, out NodeInfo[])

Gets all child nodes, including channels, of the *nodeName*  you specify. This method does not perform a recursive search. You can use the [GetSystemNodeChannelList](nationalinstruments-veristand-clientapi-iworkspace-getsystemnodechannellist__string-out.html) to perform a recursive search of all the channels under a specified node.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public [Error](nationalinstruments-veristand-clientapi-stimulusresult.html) GetSystemNodeChildren(string nodeName, out NodeInfo[] nodes)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| nodeName | string | The name of the node for which you want to see all child nodes. |
| nodes | out NodeInfo[] | An array containing information about all the child nodes. You can index this array and use the members of the NodeInfo class to get specific information about each node, such as its name, path, GUID, and, if the node is a channel, information about the channel. |

#### Returns

Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0.

Parent topic:

IWorkspace Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-iworkspace-lockworkspacefile__string-string.html language=enus -->
## TOPIC 00348: LockWorkspaceFile(string, string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-iworkspace-lockworkspacefile__string-string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-iworkspace-lockworkspacefile__string-string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: This method is deprecated in NI VeriStand 2010 and later. Use the LockConnection method instead. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic Error LockWorkspaceFile(string old_password, string new_password)RemarksLocks a running workspace configuration so that a user must provide

### LockWorkspaceFile(string, string)

This method is deprecated in NI VeriStand 2010 and later. Use the [LockConnection](nationalinstruments-veristand-clientapi-iworkspace2-lockconnection__string-string.html) method instead.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public [Error](nationalinstruments-veristand-clientapi-stimulusresult.html) LockWorkspaceFile(string old_password, string new_password)

#### Remarks

Locks a running workspace configuration so that a user must provide a password to stop running the configuration. The configuration must be running when you call this method. If the configuration has an existing password, you must provide the password to the *old_password*  parameter in order to set the new password.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| old_password | string | The existing password for the configuration. If no password exists, this method ignores this parameter. |
| new_password | string | The password to use to lock the configuration. |

#### Returns

Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0.

Parent topic:

IWorkspace Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-iworkspace-onsystemstatechange.html language=enus -->
## TOPIC 00349: OnSystemStateChange

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-iworkspace-onsystemstatechange.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-iworkspace-onsystemstatechange.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Callback invoked when a system state changes. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic DOnSystemStateChange OnSystemStateChange

### OnSystemStateChange

Callback invoked when a system state changes.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public [DOnSystemStateChange](nationalinstruments-veristand-clientapi-donsystemstatechange__byte.html) OnSystemStateChange

Parent topic:

IWorkspace Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-iworkspace-runworkspacefile__string-bool-bool-uint-string-string.html language=enus -->
## TOPIC 00350: RunWorkspaceFile(string, bool, bool, uint, string, string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-iworkspace-runworkspacefile__string-bool-bool-uint-string-string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-iworkspace-runworkspacefile__string-bool-bool-uint-string-string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: This method is deprecated in NI VeriStand 2010 and later. Use the ConnectToSystem(string, DeployOptions) method instead. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic Error RunWorkspaceFile(string file_path, bool launchworkspace, bool deploysystemdefinition, uint timeout, string use

### RunWorkspaceFile(string, bool, bool, uint, string, string)

This method is deprecated in NI VeriStand 2010 and later. Use the [ConnectToSystem(string, DeployOptions)](nationalinstruments-veristand-clientapi-iworkspace2-connecttosystem__string-deployoptions.html) method instead.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public [Error](nationalinstruments-veristand-clientapi-stimulusresult.html) RunWorkspaceFile(string file_path, bool launchworkspace, bool deploysystemdefinition, uint timeout, string user_name, string password)

#### Remarks

Runs the workspace configuration you specify. If a configuration is already running when you call this method, the method returns an error.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| file_path | string | The path to the configuration. |
| launchworkspace | bool | Specifies whether to launch the Workspace window. This input is ignored in NI VeriStand 2010 and later. |
| deploysystemdefinition | bool | Specifies whether to deploy the system definition file before running the workspace. |
| timeout | uint | The time allowed for the VeriStand Gateway to successfully deploy the system definition to the target(s) and for the target(s) to achieve active running state. If timeout is exceeded, deployment is cancelled. |
| user_name | string | The user name to use to access the NI VeriStand project. This parameter is ignored in NI VeriStand 2010 and later. |
| password | string | The password associated with the user_name you enter. This input is ignored in NI VeriStand 2010 and later. |

#### Returns

Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0.

Parent topic:

IWorkspace Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-iworkspace-setchannelvectorvalues__string-double_arr1.html language=enus -->
## TOPIC 00351: SetChannelVectorValues(string, double[])

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-iworkspace-setchannelvectorvalues__string-double_arr1.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-iworkspace-setchannelvectorvalues__string-double_arr1.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the vector values of a channel on the target. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic Error SetChannelVectorValues(string channel, double[] newValues)RemarksUse the IModelManager2 interface for setting the model parameter values. Targets/Controller/Simulation Models/Model

### SetChannelVectorValues(string, double[])

Sets the vector values of a channel on the target.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public [Error](nationalinstruments-veristand-clientapi-stimulusresult.html) SetChannelVectorValues(string channel, double[] newValues)

#### Remarks

Use the [IModelManager2](nationalinstruments-veristand-clientapi-imodelmanager2.html) interface for setting the model parameter values.

Targets/Controller/Simulation Models/Models/delay_random/Inports/In1

int[,] array2D = new int[,] { { 1, 2 }, { 3, 4 }, { 5, 6 }, { 7, 8 } };

you can convert it to a 1D array of the form:

int[,] array1DTransformed = new int[,] {1,3,5,7,2,4,6,8};

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| channel | string | The name of the channel. You must enter the full path to the channel as specified in the system definition file. For example: |

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| newValues | double[] | The vector values. This parameter expects a 1D array. If the channel expects two-dimensional data, convert the 2D channel data into a 1D array before passing it to this method. For example, if the 2D array of channel data is: |

#### Returns

Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0.

Parent topic:

IWorkspace Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-iworkspace-setmultiplechannelvalues__string_arr1-double_arr1.html language=enus -->
## TOPIC 00352: SetMultipleChannelValues(string[], double[])

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-iworkspace-setmultiplechannelvalues__string_arr1-double_arr1.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-iworkspace-setmultiplechannelvalues__string_arr1-double_arr1.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the values of multiple channels on the target. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic Error SetMultipleChannelValues(string[] names, double[] values)RemarksUse the IModelManager2 interface for setting the model parameter values. Targets/Controller/Simulation Models/Model

### SetMultipleChannelValues(string[], double[])

Sets the values of multiple channels on the target.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public [Error](nationalinstruments-veristand-clientapi-stimulusresult.html) SetMultipleChannelValues(string[] names, double[] values)

#### Remarks

Use the [IModelManager2](nationalinstruments-veristand-clientapi-imodelmanager2.html) interface for setting the model parameter values.

Targets/Controller/Simulation Models/Models/delay_random/Inports/In1

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| names | string[] | The names of the channels. You must enter the full path to each channel as specified in the system definition file. For example: |

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| values | double[] | The values to set. |

#### Returns

Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0.

Parent topic:

IWorkspace Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-iworkspace-setsinglechannelvalue__string-double.html language=enus -->
## TOPIC 00353: SetSingleChannelValue(string, double)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-iworkspace-setsinglechannelvalue__string-double.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-iworkspace-setsinglechannelvalue__string-double.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of a single channel on the target. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic Error SetSingleChannelValue(string name, double newVal)RemarksUse the IModelManager2 interface for setting the model parameter values. Targets/Controller/Simulation Models/Models/delay_ra

### SetSingleChannelValue(string, double)

Sets the value of a single channel on the target.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public [Error](nationalinstruments-veristand-clientapi-stimulusresult.html) SetSingleChannelValue(string name, double newVal)

#### Remarks

Use the [IModelManager2](nationalinstruments-veristand-clientapi-imodelmanager2.html) interface for setting the model parameter values.

Targets/Controller/Simulation Models/Models/delay_random/Inports/In1

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | The name of the channel. You must enter the full path to the channel as specified in the system definition file. For example: |

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| newVal | double | The value to set. |

#### Returns

Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0.

Parent topic:

IWorkspace Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-iworkspace-stopworkspacefile__string.html language=enus -->
## TOPIC 00354: StopWorkspaceFile(string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-iworkspace-stopworkspacefile__string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-iworkspace-stopworkspacefile__string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: This method is deprecated in NI VeriStand 2010 and later. Use the DisconnectFromSystem method instead. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic Error StopWorkspaceFile(string password)RemarksStops running the current configuration. ParametersNameTypeDescriptionpasswordstringThe

### StopWorkspaceFile(string)

This method is deprecated in NI VeriStand 2010 and later. Use the [DisconnectFromSystem](nationalinstruments-veristand-clientapi-iworkspace2-disconnectfromsystem__string-bool.html) method instead.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public [Error](nationalinstruments-veristand-clientapi-stimulusresult.html) StopWorkspaceFile(string password)

#### Remarks

Stops running the current configuration.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| password | string | The password for the configuration. This parameter is only used if the configuration is locked. |

#### Returns

Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0.

Parent topic:

IWorkspace Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-iworkspace-unlockworkspacefile__string.html language=enus -->
## TOPIC 00355: UnlockWorkspaceFile(string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-iworkspace-unlockworkspacefile__string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-iworkspace-unlockworkspacefile__string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: This method is deprecated in NI VeriStand 2010 and later. Use the UnlockConnection method of the IWorkspace2 interface instead. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic Error UnlockWorkspaceFile(string password)RemarksUnlocks the currently running workspace configuration. Param

### UnlockWorkspaceFile(string)

This method is deprecated in NI VeriStand 2010 and later. Use the [UnlockConnection](nationalinstruments-veristand-clientapi-iworkspace2-unlockconnection__string.html) method of the [IWorkspace2](nationalinstruments-veristand-clientapi-iworkspace2.html) interface instead.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public [Error](nationalinstruments-veristand-clientapi-stimulusresult.html) UnlockWorkspaceFile(string password)

#### Remarks

Unlocks the currently running workspace configuration.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| password | string | The password for the configuration. |

#### Returns

Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0.

Parent topic:

IWorkspace Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-iworkspace.html language=enus -->
## TOPIC 00356: IWorkspace Interface

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-iworkspace.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-iworkspace.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Interface to perform basic workspace operations, such as getting and setting channel data. The IWorkspace2 interface inherits the members of this interface and provides extended functionality. Derives fromNoneSyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic interface IWorkspaceMethodsN

### IWorkspace Interface

Interface to perform basic workspace operations, such as getting and setting channel data.

Note

The [IWorkspace2](nationalinstruments-veristand-clientapi-iworkspace2.html) interface inherits the members of this interface and provides extended functionality.

#### Derives from

None

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public interface IWorkspace

#### Methods

| Name | Description |
| --- | --- |
| GetAliasList(out string[], out string[]) | Gets all the aliases defined for channels in the system, and the channels to which each alias corresponds. |
| GetChannelVectorValues(string, out uint, out uint, out double[]) | Gets the vector values of a channel on the target. |
| GetEngineState(out SystemState, out string, out string, out string) | This method is deprecated in NI VeriStand 2010 and later. Use the GetSystemState method instead. |
| GetMultipleChannelValues(string[], out double[]) | Gets the values of multiple scalar channels running on the target. To get the values of vector channels, use the GetChannelVectorValues method. |
| GetMultipleSystemNodesData(string[], out NodeInfo[]) | Gets information about multiple nodes in the system definition file. |
| GetSingleChannelValue(string, out double) | Gets the value of a single channel on the target. |
| GetSystemNodeChannelList(string, out NodeInfo[]) | Gets a list of all the channels under the nodeName you specify. This method performs a recursive search. |
| GetSystemNodeChildren(string, out NodeInfo[]) | Gets all child nodes, including channels, of the nodeName you specify. This method does not perform a recursive search. You can use the GetSystemNodeChannelList to perform a recursive search of all the channels under a specified node. |
| LockWorkspaceFile(string, string) | This method is deprecated in NI VeriStand 2010 and later. Use the LockConnection method instead. |
| RunWorkspaceFile(string, bool, bool, uint, string, string) | This method is deprecated in NI VeriStand 2010 and later. Use the ConnectToSystem(string, DeployOptions) method instead. |
| SetChannelVectorValues(string, double[]) | Sets the vector values of a channel on the target. |
| SetMultipleChannelValues(string[], double[]) | Sets the values of multiple channels on the target. |
| SetSingleChannelValue(string, double) | Sets the value of a single channel on the target. |
| StopWorkspaceFile(string) | This method is deprecated in NI VeriStand 2010 and later. Use the DisconnectFromSystem method instead. |
| UnlockWorkspaceFile(string) | This method is deprecated in NI VeriStand 2010 and later. Use the UnlockConnection method of the IWorkspace2 interface instead. |

#### Events

| Name | Description |
| --- | --- |
| OnSystemStateChange | Callback invoked when a system state changes. |

Parent topic:

NationalInstruments.VeriStand.ClientAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-iworkspace2-asyncdisconnectfromsystem__string-bool.html language=enus -->
## TOPIC 00357: AsyncDisconnectFromSystem(string, bool)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-iworkspace2-asyncdisconnectfromsystem__string-bool.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-iworkspace2-asyncdisconnectfromsystem__string-bool.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Asynchronously disconnects the VeriStand Gateway from all connected targets. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic void AsyncDisconnectFromSystem(string password, bool undeploy_system_definition)ParametersNameTypeDescriptionpasswordstringThe password for the current connecti

### AsyncDisconnectFromSystem(string, bool)

Asynchronously disconnects the VeriStand Gateway from all connected targets.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public void AsyncDisconnectFromSystem(string password, bool undeploy_system_definition)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| password | string | The password for the current connection, if the connection is locked. |
| undeploy_system_definition | bool | Specifies whether to undeploy the system definition file before disconnecting. If you set this parameter to false, the target(s) continue to to run the system definition after the VeriStand Gateway disconnects. |

Parent topic:

IWorkspace2 Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-iworkspace2-connecttosystem__string-bool-uint.html language=enus -->
## TOPIC 00358: ConnectToSystem(string, bool, uint)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-iworkspace2-connecttosystem__string-bool-uint.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-iworkspace2-connecttosystem__string-bool-uint.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Connects the VeriStand Gateway to one or more targets running the system definition file you specify. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic Error ConnectToSystem(string systemdefintion_file_path, bool deploy_system_definition, uint timeout)RemarksFor example code and more in

### ConnectToSystem(string, bool, uint)

Connects the VeriStand Gateway to one or more targets running the system definition file you specify.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public [Error](nationalinstruments-veristand-clientapi-stimulusresult.html) ConnectToSystem(string systemdefintion_file_path, bool deploy_system_definition, uint timeout)

#### Remarks

For example code and more information about this method, refer to one of the following help topics:

LabVIEW Walkthrough: Opening and Running a Project

C# Walkthrough: Opening and Running a Project

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| systemdefintion_file_path | string | The path to the system definition file that is running on the target(s). |
| deploy_system_definition | bool | Specifies whether to deploy the system definition file. If you set this parameter to false, the target(s) must already be running the system definition file before you call this method. |
| timeout | uint | The maximum amount of time, in milliseconds, to wait for the connection process to complete before returning an error. |

#### Returns

Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0.

Parent topic:

IWorkspace2 Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-iworkspace2-connecttosystem__string-deployoptions.html language=enus -->
## TOPIC 00359: ConnectToSystem(string, DeployOptions)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-iworkspace2-connecttosystem__string-deployoptions.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-iworkspace2-connecttosystem__string-deployoptions.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Connects the VeriStand Gateway to one or more targets running the system definition file you specify. You can also deploy the system definition file with a calibration file. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic Error ConnectToSystem(string systemdefinition_file_path, Deploy

### ConnectToSystem(string, DeployOptions)

Connects the VeriStand Gateway to one or more targets running the system definition file you specify. You can also deploy the system definition file with a calibration file.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public [Error](nationalinstruments-veristand-clientapi-stimulusresult.html) ConnectToSystem(string systemdefinition_file_path, DeployOptions options)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| systemdefinition_file_path | string | The path to the system definition file that is running on the target(s). |
| options | DeployOptions | A data structure that contains options for deploying the system definition file, including whether to deploy it, a calibration file to deploy, and a timeout. |

#### Returns

Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0.

Parent topic:

IWorkspace2 Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-iworkspace2-disconnectfromsystem__string-bool.html language=enus -->
## TOPIC 00360: DisconnectFromSystem(string, bool)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-iworkspace2-disconnectfromsystem__string-bool.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-iworkspace2-disconnectfromsystem__string-bool.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Disconnects the VeriStand Gateway from all connected Real-Time(RT) targets. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic Error DisconnectFromSystem(string password, bool undeploy_system_definition)ParametersNameTypeDescriptionpasswordstringThe password for the current connection, i

### DisconnectFromSystem(string, bool)

Disconnects the VeriStand Gateway from all connected Real-Time(RT) targets.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public [Error](nationalinstruments-veristand-clientapi-stimulusresult.html) DisconnectFromSystem(string password, bool undeploy_system_definition)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| password | string | The password for the current connection, if the connection is locked. |
| undeploy_system_definition | bool | Specifies whether to undeploy the system definition file before disconnecting. If you set this parameter to false, the Real-Time(RT) target(s) continue to run the system definition after the VeriStand Gateway disconnects. Note This parameter configuration is skipped for Windows targets. |

#### Returns

Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0.

Parent topic:

IWorkspace2 Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-iworkspace2-disconnecttarget__string-bool.html language=enus -->
## TOPIC 00361: DisconnectTarget(string, bool)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-iworkspace2-disconnecttarget__string-bool.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-iworkspace2-disconnecttarget__string-bool.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Disconnects the VeriStand Gateway from a specified target in the system. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic Error DisconnectTarget(string target, bool undeploy_system_definition)ParametersNameTypeDescriptiontargetstringSpecifies the target to disconnect.undeploy_system_de

### DisconnectTarget(string, bool)

Disconnects the VeriStand Gateway from a specified target in the system.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public [Error](nationalinstruments-veristand-clientapi-stimulusresult.html) DisconnectTarget(string target, bool undeploy_system_definition)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| target | string | Specifies the target to disconnect. |
| undeploy_system_definition | bool | Specifies whether to undeploy the system definition file before disconnecting. If you set this parameter to false, the target(s) continue to to run the system definition after the VeriStand Gateway disconnects. |

#### Returns

Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0.

Parent topic:

IWorkspace2 Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-iworkspace2-getchannelvalues__string_arr1-out.html language=enus -->
## TOPIC 00362: GetChannelValues(string[], out DataArray[])

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-iworkspace2-getchannelvalues__string_arr1-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-iworkspace2-getchannelvalues__string_arr1-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets values for the channels you specify. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic Error GetChannelValues(string[] names, out DataArray[] values)RemarksUse the IModelManager2 interface for getting the model parameter values. ParametersNameTypeDescriptionnamesstring[]The names o

### GetChannelValues(string[], out DataArray[])

Gets values for the channels you specify.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public [Error](nationalinstruments-veristand-clientapi-stimulusresult.html) GetChannelValues(string[] names, out DataArray[] values)

#### Remarks

Use the [IModelManager2](nationalinstruments-veristand-clientapi-imodelmanager2.html) interface for getting the model parameter values.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| names | string[] | The names of the channels for which to get values. |
| values | out DataArray[] | The values of the channels. |

#### Returns

Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0.

Parent topic:

IWorkspace2 Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-iworkspace2-getiudpchannelstreamsession__string_arr1.html language=enus -->
## TOPIC 00363: GetIUDPChannelStreamSession(string[])

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-iworkspace2-getiudpchannelstreamsession__string_arr1.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-iworkspace2-getiudpchannelstreamsession__string_arr1.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Accesses the IUDPChannelStreamSession interface, which you can use to view buffered waveform data published by the VeriStand Gateway. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic IUDPChannelStreamSession GetIUDPChannelStreamSession(string[] channels)ParametersNameTypeDescriptioncha

### GetIUDPChannelStreamSession(string[])

Accesses the [IUDPChannelStreamSession](nationalinstruments-veristand-clientapi-iudpchannelstreamsession.html) interface, which you can use to view buffered waveform data published by the VeriStand Gateway.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public [IUDPChannelStreamSession](nationalinstruments-veristand-clientapi-iudpchannelstreamsession.html) GetIUDPChannelStreamSession(string[] channels)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| channels | string[] | The channels for which to open the UDP Stream Session. You can specify alias names or full paths to channels, as defined in the system definition file. |

#### Returns

Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0.

Parent topic:

IWorkspace2 Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-iworkspace2-getsystemdefinitionmd5checksum__out.html language=enus -->
## TOPIC 00364: GetSystemDefinitionMD5Checksum(out string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-iworkspace2-getsystemdefinitionmd5checksum__out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-iworkspace2-getsystemdefinitionmd5checksum__out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the MD5 of the deployed system definition. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic Error GetSystemDefinitionMD5Checksum(out string md5)ParametersNameTypeDescriptionmd5out stringMD5 of the deployed system definitionReturnsReturns an NationalInstruments.VeriStand.Error obje

### GetSystemDefinitionMD5Checksum(out string)

Gets the MD5 of the deployed system definition.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public [Error](nationalinstruments-veristand-clientapi-stimulusresult.html) GetSystemDefinitionMD5Checksum(out string md5)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| md5 | out string | MD5 of the deployed system definition |

#### Returns

Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0.

Parent topic:

IWorkspace2 Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-iworkspace2-getsystemnodewaveformlist__string-out.html language=enus -->
## TOPIC 00365: GetSystemNodeWaveformList(string, out NodeInfo[])

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-iworkspace2-getsystemnodewaveformlist__string-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-iworkspace2-getsystemnodewaveformlist__string-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a list of all the waveforms under the nodeName you specify. This method performs a recursive search. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic Error GetSystemNodeWaveformList(string nodeName, out NodeInfo[] waveforms)ParametersNameTypeDescriptionnodeNamestringThe name of th

### GetSystemNodeWaveformList(string, out NodeInfo[])

Gets a list of all the waveforms under the *nodeName*  you specify. This method performs a recursive search.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public [Error](nationalinstruments-veristand-clientapi-stimulusresult.html) GetSystemNodeWaveformList(string nodeName, out NodeInfo[] waveforms)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| nodeName | string | The name of the node for which you want to see all channels. If this parameter is empty, this method gets all the channels in the system. |
| waveforms | out NodeInfo[] | An array containing information about all the waveforms. You can index this array and use the members of the NodeInfo class to get specific information about each waveform, such as its name, path, GUID, and data type. |

#### Returns

Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0.

Parent topic:

IWorkspace2 Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-iworkspace2-getsystemstate__out-out-out.html language=enus -->
## TOPIC 00366: GetSystemState(out SystemState, out string, out string[])

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-iworkspace2-getsystemstate__out-out-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-iworkspace2-getsystemstate__out-out-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the current state of the system to which the VeriStand Gateway is connected. Use the ConnectToSystem(string, DeployOptions) method to connect to a system. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic Error GetSystemState(out SystemState state, out string systemdefinition_file,

### GetSystemState(out SystemState, out string, out string[])

Gets the current state of the system to which the VeriStand Gateway is connected. Use the [ConnectToSystem(string, DeployOptions)](nationalinstruments-veristand-clientapi-iworkspace2-connecttosystem__string-deployoptions.html) method to connect to a system.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public [Error](nationalinstruments-veristand-clientapi-stimulusresult.html) GetSystemState(out SystemState state, out string systemdefinition_file, out string[] targets)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| state | out SystemState | The SystemState. |
| systemdefinition_file | out string | The path to the system definition file for the system. |
| targets | out string[] | The list of targets to which the system definition file is currently deployed. |

#### Returns

Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0.

Parent topic:

IWorkspace2 Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-iworkspace2-gettargetstate__string-out.html language=enus -->
## TOPIC 00367: GetTargetState(string, out TargetState)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-iworkspace2-gettargetstate__string-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-iworkspace2-gettargetstate__string-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the current state of a target. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic Error GetTargetState(string target, out TargetState state)ParametersNameTypeDescriptiontargetstringThe target name. stateout TargetStateCurrent state of the target.ReturnsReturns an NationalInstruments

### GetTargetState(string, out TargetState)

Gets the current state of a target.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public [Error](nationalinstruments-veristand-clientapi-stimulusresult.html) GetTargetState(string target, out TargetState state)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| target | string | The target name. |
| state | out TargetState | Current state of the target. |

#### Returns

Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0.

Parent topic:

IWorkspace2 Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-iworkspace2-lockconnection__string-string.html language=enus -->
## TOPIC 00368: LockConnection(string, string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-iworkspace2-lockconnection__string-string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-iworkspace2-lockconnection__string-string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Locks the current VeriStand Gateway connection. If the connection already is locked, you must provide the current password in order to set a new one. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic Error LockConnection(string old_password, string new_password)ParametersNameTypeDescrip

### LockConnection(string, string)

Locks the current VeriStand Gateway connection. If the connection already is locked, you must provide the current password in order to set a new one.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public [Error](nationalinstruments-veristand-clientapi-stimulusresult.html) LockConnection(string old_password, string new_password)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| old_password | string | The current password for the connection, if it previously was locked. |
| new_password | string | The new password to use to lock the connection. |

#### Returns

Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0.

Parent topic:

IWorkspace2 Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-iworkspace2-ongatewayerrornotification.html language=enus -->
## TOPIC 00369: OnGatewayErrorNotification

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-iworkspace2-ongatewayerrornotification.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-iworkspace2-ongatewayerrornotification.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Event for an unhandled error on the VeriStand Gateway. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic DOnGatewayErrorNotification OnGatewayErrorNotification

### OnGatewayErrorNotification

Event for an unhandled error on the VeriStand Gateway.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public [DOnGatewayErrorNotification](nationalinstruments-veristand-clientapi-dongatewayerrornotification__error.html) OnGatewayErrorNotification

Parent topic:

IWorkspace2 Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-iworkspace2-ongatewaystatusnotification.html language=enus -->
## TOPIC 00370: OnGatewayStatusNotification

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-iworkspace2-ongatewaystatusnotification.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-iworkspace2-ongatewaystatusnotification.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Event for status notifications from the VeriStand Gateway. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic DOnGatewayStatusNotification OnGatewayStatusNotification

### OnGatewayStatusNotification

Event for status notifications from the VeriStand Gateway.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public [DOnGatewayStatusNotification](nationalinstruments-veristand-clientapi-dongatewaystatusnotification__string.html) OnGatewayStatusNotification

Parent topic:

IWorkspace2 Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-iworkspace2-reconnecttosystem__string-deployoptions.html language=enus -->
## TOPIC 00371: ReconnectToSystem(string, DeployOptions)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-iworkspace2-reconnecttosystem__string-deployoptions.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-iworkspace2-reconnecttosystem__string-deployoptions.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reconnects the VeriStand Gateway to a target within the system definition file used by the Gateway. You can also redeploy the system definition file. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic Error ReconnectToSystem(string target, DeployOptions options)ParametersNameTypeDescript

### ReconnectToSystem(string, DeployOptions)

Reconnects the VeriStand Gateway to a target within the system definition file used by the Gateway. You can also redeploy the system definition file.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public [Error](nationalinstruments-veristand-clientapi-stimulusresult.html) ReconnectToSystem(string target, DeployOptions options)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| target | string | The target to reconnect to the Gateway. This target must be defined in the initial system definition used by the VeriStand Gateway. |
| options | DeployOptions | A data structure that contains options for deploying the system definition file, including whether to deploy it, a calibration file to deploy, and a timeout. Note: There is an option to specify the system definition file path but this is unused during reconnection. Instead, the file specified at the original deployment is used. |

#### Returns

Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0.

Parent topic:

IWorkspace2 Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-iworkspace2-restartengine__string-string-string-string.html language=enus -->
## TOPIC 00372: RestartEngine(string, string, string, string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-iworkspace2-restartengine__string-string-string-string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-iworkspace2-restartengine__string-string-string-string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Restart the VeriStand engine on the given protected target. If needed, reset it as a startup application. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic Error RestartEngine(string ip, string os, string username, string password)ParametersNameTypeDescriptionipstringIP address of the t

### RestartEngine(string, string, string, string)

Restart the VeriStand engine on the given protected target. If needed, reset it as a startup application.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public [Error](nationalinstruments-veristand-clientapi-stimulusresult.html) RestartEngine(string ip, string os, string username, string password)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| ip | string | IP address of the target. |
| os | string | Operating system on the target. |
| username | string | Username on the target. |
| password | string | Password on the target. |

#### Returns

An error with a failure message.

Parent topic:

IWorkspace2 Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-iworkspace2-restartengine__string-string.html language=enus -->
## TOPIC 00373: RestartEngine(string, string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-iworkspace2-restartengine__string-string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-iworkspace2-restartengine__string-string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Restart the VeriStand engine on the given target. If needed, reset it as a startup application. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic Error RestartEngine(string ip, string os)ParametersNameTypeDescriptionipstringIP address of the target.osstringOperating system on the target

### RestartEngine(string, string)

Restart the VeriStand engine on the given target. If needed, reset it as a startup application.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public [Error](nationalinstruments-veristand-clientapi-stimulusresult.html) RestartEngine(string ip, string os)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| ip | string | IP address of the target. |
| os | string | Operating system on the target. |

#### Returns

An error with a failure message.

Parent topic:

IWorkspace2 Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-iworkspace2-setchannelvalues__string_arr1-dataarray_arr1.html language=enus -->
## TOPIC 00374: SetChannelValues(string[], DataArray[])

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-iworkspace2-setchannelvalues__string_arr1-dataarray_arr1.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-iworkspace2-setchannelvalues__string_arr1-dataarray_arr1.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets values for the channels you specify. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic Error SetChannelValues(string[] names, DataArray[] newVals)RemarksUse the IModelManager2 interface for setting the model parameter values. ParametersNameTypeDescriptionnamesstring[]The names of t

### SetChannelValues(string[], DataArray[])

Sets values for the channels you specify.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public [Error](nationalinstruments-veristand-clientapi-stimulusresult.html) SetChannelValues(string[] names, DataArray[] newVals)

#### Remarks

Use the [IModelManager2](nationalinstruments-veristand-clientapi-imodelmanager2.html) interface for setting the model parameter values.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| names | string[] | The names of the channels for which to set values. |
| newVals | DataArray[] | The values to set. |

#### Returns

Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0.

Parent topic:

IWorkspace2 Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-iworkspace2-startdatalogging__string-loginfo.html language=enus -->
## TOPIC 00375: StartDataLogging(string, LogInfo)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-iworkspace2-startdatalogging__string-loginfo.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-iworkspace2-startdatalogging__string-loginfo.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Starts logging data for the specified configuration_name . SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic Error StartDataLogging(string configuration_name, LogInfo logging_configuration)ParametersNameTypeDescriptionconfiguration_namestringA unique name for the logging configuration.

### StartDataLogging(string, LogInfo)

Starts logging data for the specified *configuration_name* .

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public [Error](nationalinstruments-veristand-clientapi-stimulusresult.html) StartDataLogging(string configuration_name, LogInfo logging_configuration)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| configuration_name | string | A unique name for the logging configuration. |
| logging_configuration | LogInfo | Specifies configuration settings for the log file. Use the LogInfo properties to specify the values this input expects, such as the path to the log file, trigger settings, and the rate at which to log data. |

#### Returns

Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0.

Parent topic:

IWorkspace2 Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-iworkspace2-stopdatalogging__string.html language=enus -->
## TOPIC 00376: StopDataLogging(string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-iworkspace2-stopdatalogging__string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-iworkspace2-stopdatalogging__string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Stops logging data for the specified configuration_name . SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic Error StopDataLogging(string configuration_name)ParametersNameTypeDescriptionconfiguration_namestringThe name of the configuration for which to terminate logging. ReturnsReturns a

### StopDataLogging(string)

Stops logging data for the specified *configuration_name* .

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public [Error](nationalinstruments-veristand-clientapi-stimulusresult.html) StopDataLogging(string configuration_name)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| configuration_name | string | The name of the configuration for which to terminate logging. |

#### Returns

Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0.

Parent topic:

IWorkspace2 Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-iworkspace2-targetstatechangeevent.html language=enus -->
## TOPIC 00377: TargetStateChangeEvent

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-iworkspace2-targetstatechangeevent.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-iworkspace2-targetstatechangeevent.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Event for target state change from the VeriStand Gateway. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic EventHandler< TargetStateChangeEventArgs > TargetStateChangeEvent

### TargetStateChangeEvent

Event for target state change from the VeriStand Gateway.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public EventHandler< [TargetStateChangeEventArgs](nationalinstruments-veristand-clientapi-targetstatechangeeventargs.html) > TargetStateChangeEvent

Parent topic:

IWorkspace2 Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-iworkspace2-unlockconnection__string.html language=enus -->
## TOPIC 00378: UnlockConnection(string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-iworkspace2-unlockconnection__string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-iworkspace2-unlockconnection__string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Unlocks the current VeriStand Gateway connection. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic Error UnlockConnection(string password)ParametersNameTypeDescriptionpasswordstringThe password for the current connection.ReturnsReturns an NationalInstruments.VeriStand.Error object. If

### UnlockConnection(string)

Unlocks the current VeriStand Gateway connection.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public [Error](nationalinstruments-veristand-clientapi-stimulusresult.html) UnlockConnection(string password)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| password | string | The password for the current connection. |

#### Returns

Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0.

Parent topic:

IWorkspace2 Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-iworkspace2.html language=enus -->
## TOPIC 00379: IWorkspace2 Interface

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-iworkspace2.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-iworkspace2.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Interface to perform basic workspace operations, such as getting, setting, and logging channel data. Derives fromIWorkspaceSyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic interface IWorkspace2 : IWorkspaceRemarksThis interface also inherits the methods of the IWorkspace interface. For

### IWorkspace2 Interface

Interface to perform basic workspace operations, such as getting, setting, and logging channel data.

#### Derives from

- IWorkspace

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public interface IWorkspace2 : IWorkspace

#### Remarks

IWorkspace

For example code and more information about this interface, refer to one of the following help topics:

LabVIEW Walkthrough: Opening and Running a Project

C# Walkthrough: Opening and Running a Project

#### Methods

| Name | Description |
| --- | --- |
| AsyncDisconnectFromSystem(string, bool) | Asynchronously disconnects the VeriStand Gateway from all connected targets. |
| ConnectToSystem(string, DeployOptions) | Connects the VeriStand Gateway to one or more targets running the system definition file you specify. You can also deploy the system definition file with a calibration file. |
| ConnectToSystem(string, bool, uint) | Connects the VeriStand Gateway to one or more targets running the system definition file you specify. |
| DisconnectFromSystem(string, bool) | Disconnects the VeriStand Gateway from all connected Real-Time(RT) targets. |
| DisconnectTarget(string, bool) | Disconnects the VeriStand Gateway from a specified target in the system. |
| GetChannelValues(string[], out DataArray[]) | Gets values for the channels you specify. |
| GetIUDPChannelStreamSession(string[]) | Accesses the IUDPChannelStreamSession interface, which you can use to view buffered waveform data published by the VeriStand Gateway. |
| GetSystemDefinitionMD5Checksum(out string) | Gets the MD5 of the deployed system definition. |
| GetSystemNodeWaveformList(string, out NodeInfo[]) | Gets a list of all the waveforms under the nodeName you specify. This method performs a recursive search. |
| GetSystemState(out SystemState, out string, out string[]) | Gets the current state of the system to which the VeriStand Gateway is connected. Use the ConnectToSystem(string, DeployOptions) method to connect to a system. |
| GetTargetState(string, out TargetState) | Gets the current state of a target. |
| LockConnection(string, string) | Locks the current VeriStand Gateway connection. If the connection already is locked, you must provide the current password in order to set a new one. |
| ReconnectToSystem(string, DeployOptions) | Reconnects the VeriStand Gateway to a target within the system definition file used by the Gateway. You can also redeploy the system definition file. |
| RestartEngine(string, string) | Restart the VeriStand engine on the given target. If needed, reset it as a startup application. |
| RestartEngine(string, string, string, string) | Restart the VeriStand engine on the given protected target. If needed, reset it as a startup application. |
| SetChannelValues(string[], DataArray[]) | Sets values for the channels you specify. |
| StartDataLogging(string, LogInfo) | Starts logging data for the specified configuration_name . |
| StopDataLogging(string) | Stops logging data for the specified configuration_name . |
| UnlockConnection(string) | Unlocks the current VeriStand Gateway connection. |

#### Events

| Name | Description |
| --- | --- |
| OnGatewayErrorNotification | Event for an unhandled error on the VeriStand Gateway. |
| OnGatewayStatusNotification | Event for status notifications from the VeriStand Gateway. |
| TargetStateChangeEvent | Event for target state change from the VeriStand Gateway. |

Parent topic:

NationalInstruments.VeriStand.ClientAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logchannel-channel_group.html language=enus -->
## TOPIC 00380: channel_group

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logchannel-channel_group.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logchannel-channel_group.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the name of the channel group to use for the channel in the log file. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic string channel_group { get; set; }ReturnsIf no name is specified, the log file uses the name of the owning section of the channel.

### channel_group

Gets or sets the name of the channel group to use for the channel in the log file.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public string channel_group { get; set; }

#### Returns

If no name is specified, the log file uses the name of the owning section of the channel.

Parent topic:

LogChannel Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logchannel-channel_name.html language=enus -->
## TOPIC 00381: channel_name

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logchannel-channel_name.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logchannel-channel_name.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets a name to use for the channel in the log file. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic string channel_name { get; set; }ReturnsIf no name is specified, the log file uses the name of the channel node.

### channel_name

Gets or sets a name to use for the channel in the log file.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public string channel_name { get; set; }

#### Returns

If no name is specified, the log file uses the name of the channel node.

Parent topic:

LogChannel Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logchannel-channel_path.html language=enus -->
## TOPIC 00382: channel_path

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logchannel-channel_path.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logchannel-channel_path.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the path to the channel or its alias. The path matches the node hierarchy that appears in the System Explorer window configuration tree. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic string channel_path { get; }

### channel_path

Gets the path to the channel or its alias. The path matches the node hierarchy that appears in the **System Explorer** window configuration tree.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public string channel_path { get; }

Parent topic:

LogChannel Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logchannel-logchannel__string-string-string-string_arr1-string_arr1.html language=enus -->
## TOPIC 00383: LogChannel(string, string, string, string[], string[])

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logchannel-logchannel__string-string-string-string_arr1-string_arr1.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logchannel-logchannel__string-string-string-string_arr1-string_arr1.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the LogChannel class and configures properties of the log file. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic LogChannel(string channel_path, string channel_name, string channel_group, string[] property_names, string[] property_values)ParametersNameType

### LogChannel(string, string, string, string[], string[])

Initializes a new instance of the [LogChannel](nationalinstruments-veristand-clientapi-logchannel.html) class and configures properties of the log file.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public LogChannel(string channel_path, string channel_name, string channel_group, string[] property_names, string[] property_values)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| channel_path | string | Specifies the path to the channel or its alias, as specified in the system definition file. |
| channel_name | string | Specifies a name to use for the channel in the log file. If this parameter is empty, the log file uses the name of the channel node. |
| channel_group | string | Specifies the name of the channel group to use for the channel in the log file. If this parameter is empty, the log file uses the name of the owning section of the channel. |
| property_names | string[] | Specifies and returns an array of property name strings to use for metadata in the log file. |
| property_values | string[] | Specifies and returns an array of property value strings to use for metadata in the log file. |

Parent topic:

LogChannel Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logchannel-logchannel__string.html language=enus -->
## TOPIC 00384: LogChannel(string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logchannel-logchannel__string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logchannel-logchannel__string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the LogChannel class. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic LogChannel(string channel_path)ParametersNameTypeDescriptionchannel_pathstringSpecifies the path to the channel to log, or its alias.

### LogChannel(string)

Initializes a new instance of the [LogChannel](nationalinstruments-veristand-clientapi-logchannel.html) class.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public LogChannel(string channel_path)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| channel_path | string | Specifies the path to the channel to log, or its alias. |

Parent topic:

LogChannel Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logchannel-properties.html language=enus -->
## TOPIC 00385: properties

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logchannel-properties.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logchannel-properties.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a dictionary containing property name and property value strings. These properties are written as metadata to the channel in the log file. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic Dictionary< string, string > properties { get; }

### properties

Gets a dictionary containing property name and property value strings. These properties are written as metadata to the channel in the log file.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public Dictionary< string, string > properties { get; }

Parent topic:

LogChannel Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logchannel.html language=enus -->
## TOPIC 00386: LogChannel Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logchannel.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logchannel.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the logging properties for individual channels. Derives fromNoneSyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic class LogChannelConstructorsNameDescriptionLogChannel(string, string, string, string[], string[])Initializes a new instance of the LogChannel class and configures

### LogChannel Class

Represents the logging properties for individual channels.

#### Derives from

None

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public class LogChannel

#### Constructors

| Name | Description |
| --- | --- |
| LogChannel(string, string, string, string[], string[]) | Initializes a new instance of the LogChannel class and configures properties of the log file. |
| LogChannel(string) | Initializes a new instance of the LogChannel class. |

#### Properties

| Name | Description |
| --- | --- |
| channel_group | Gets or sets the name of the channel group to use for the channel in the log file. |
| channel_name | Gets or sets a name to use for the channel in the log file. |
| channel_path | Gets the path to the channel or its alias. The path matches the node hierarchy that appears in the System Explorer window configuration tree. |
| properties | Gets a dictionary containing property name and property value strings. These properties are written as metadata to the channel in the log file. |

Parent topic:

NationalInstruments.VeriStand.ClientAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-analogedgetrigger-analogedgetrigger__string-double-slope-bool.html language=enus -->
## TOPIC 00387: AnalogEdgeTrigger(string, double, Slope, bool)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-analogedgetrigger-analogedgetrigger__string-double-slope-bool.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-analogedgetrigger-analogedgetrigger__string-double-slope-bool.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the AnalogEdgeTrigger class. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic AnalogEdgeTrigger(string channelPath, double threshold, Slope slope, bool strictEdge)ParametersNameTypeDescriptionchannelPathstringThe system definition path of the chann

### AnalogEdgeTrigger(string, double, Slope, bool)

Initializes a new instance of the AnalogEdgeTrigger class.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public AnalogEdgeTrigger(string channelPath, double threshold, Slope slope, bool strictEdge)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| channelPath | string | The system definition path of the channel to monitor. |
| threshold | double | The threshold that the channel must pass above or below for the trigger condition to occur. |
| slope | Slope | Specifies whether the slope is rising or falling. |
| strictEdge | bool | Specifies whether the channel value must strictly pass above or below the specified threshold. If the value is false, the channel value only needs to reach the threshold. If the value is true, the channel value must pass beyond the threshold in the direction of the slope. |

Parent topic:

AnalogEdgeTrigger Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-analogedgetrigger-slope.html language=enus -->
## TOPIC 00388: Slope

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-analogedgetrigger-slope.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-analogedgetrigger-slope.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets a value indicating whether the slope is rising or falling. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic Slope Slope { get; set; }

### Slope

Gets or sets a value indicating whether the slope is rising or falling.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public [Slope](nationalinstruments-veristand-clientapi-logging-slope.html) Slope { get; set; }

Parent topic:

AnalogEdgeTrigger Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-analogedgetrigger-strictedge.html language=enus -->
## TOPIC 00389: StrictEdge

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-analogedgetrigger-strictedge.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-analogedgetrigger-strictedge.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets a value indicating whether the channel value must strictly pass above or below the specified threshold. If the value is false, the channel value only needs to reach the threshold. If the value is true, the channel value must pass beyond the threshold in the direction of the slope. Synta

### StrictEdge

Gets or sets a value indicating whether the channel value must strictly pass above or below the specified threshold. If the value is false, the channel value only needs to reach the threshold. If the value is true, the channel value must pass beyond the threshold in the direction of the slope.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public bool StrictEdge { get; set; }

Parent topic:

AnalogEdgeTrigger Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-analogedgetrigger-threshold.html language=enus -->
## TOPIC 00390: Threshold

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-analogedgetrigger-threshold.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-analogedgetrigger-threshold.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets a value indicating the threshold that the channel must pass above or below for the trigger condition to occur. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic double Threshold { get; set; }

### Threshold

Gets or sets a value indicating the threshold that the channel must pass above or below for the trigger condition to occur.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public double Threshold { get; set; }

Parent topic:

AnalogEdgeTrigger Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-analogedgetrigger.html language=enus -->
## TOPIC 00391: AnalogEdgeTrigger Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-analogedgetrigger.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-analogedgetrigger.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies a trigger condition that occur on an analog edge. Derives fromSingleChannelTriggerSyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic class AnalogEdgeTrigger : SingleChannelTriggerConstructorsNameDescriptionAnalogEdgeTrigger(string, double, Slope, bool)Initializes a new

### AnalogEdgeTrigger Class

Specifies a trigger condition that occur on an analog edge.

#### Derives from

- SingleChannelTrigger

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public class AnalogEdgeTrigger : SingleChannelTrigger

#### Constructors

| Name | Description |
| --- | --- |
| AnalogEdgeTrigger(string, double, Slope, bool) | Initializes a new instance of the AnalogEdgeTrigger class. |

#### Properties

| Name | Description |
| --- | --- |
| Slope | Gets or sets a value indicating whether the slope is rising or falling. |
| StrictEdge | Gets or sets a value indicating whether the channel value must strictly pass above or below the specified threshold. If the value is false, the channel value only needs to reach the threshold. If the value is true, the channel value must pass beyond the threshold in the direction of the slope. |
| Threshold | Gets or sets a value indicating the threshold that the channel must pass above or below for the trigger condition to occur. |

Parent topic:

NationalInstruments.VeriStand.ClientAPI.Logging

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-dataloggingserializationbinder-bindtoname__type-out-out.html language=enus -->
## TOPIC 00392: BindToName(Type, out string, out string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-dataloggingserializationbinder-bindtoname__type-out-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-dataloggingserializationbinder-bindtoname__type-out-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines the assembly name and type name for the specified serializedType . SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic void BindToName(Type serializedType, out string assemblyName, out string typeName)ParametersNameTypeDescriptionserializedTypeTypeThe Type of the object

### BindToName(Type, out string, out string)

Determines the assembly name and type name for the specified *serializedType* .

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public void BindToName(Type serializedType, out string assemblyName, out string typeName)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| serializedType | Type | The Type of the object to serialize. |
| assemblyName | out string | The assembly name of the specified serializedType . |
| typeName | out string | The type name of the specified serializedType . |

Parent topic:

DataLoggingSerializationBinder Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-dataloggingserializationbinder-bindtotype__string-string.html language=enus -->
## TOPIC 00393: BindToType(string, string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-dataloggingserializationbinder-bindtotype__string-string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-dataloggingserializationbinder-bindtotype__string-string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines the Type of the object with the specified typeName . SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic Type BindToType(string assemblyName, string typeName)ParametersNameTypeDescriptionassemblyNamestringThe name of the assembly to bind the type to.typeNamestringThe na

### BindToType(string, string)

Determines the Type of the object with the specified *typeName* .

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public Type BindToType(string assemblyName, string typeName)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| assemblyName | string | The name of the assembly to bind the type to. |
| typeName | string | The name of the type to bind. |

#### Returns

The Type of the object with the specified *typeName* .

Parent topic:

DataLoggingSerializationBinder Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-dataloggingserializationbinder-dataloggingserializationbinder.html language=enus -->
## TOPIC 00394: DataLoggingSerializationBinder()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-dataloggingserializationbinder-dataloggingserializationbinder.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-dataloggingserializationbinder-dataloggingserializationbinder.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the DataLoggingSerializationBinder class. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic DataLoggingSerializationBinder()

### DataLoggingSerializationBinder()

Initializes a new instance of the [DataLoggingSerializationBinder](nationalinstruments-veristand-clientapi-logging-dataloggingserializationbinder.html) class.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public DataLoggingSerializationBinder()

Parent topic:

DataLoggingSerializationBinder Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-dataloggingserializationbinder.html language=enus -->
## TOPIC 00395: DataLoggingSerializationBinder Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-dataloggingserializationbinder.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-dataloggingserializationbinder.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides a custom serialization binder for handling DataLogging known types during deserialization. Derives fromISerializationBinderSyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic class DataLoggingSerializationBinder : ISerializationBinderConstructorsNameDescriptionDataLogging

### DataLoggingSerializationBinder Class

Provides a custom serialization binder for handling DataLogging known types during deserialization.

#### Derives from

- ISerializationBinder

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public class DataLoggingSerializationBinder : ISerializationBinder

#### Constructors

| Name | Description |
| --- | --- |
| DataLoggingSerializationBinder() | Initializes a new instance of the DataLoggingSerializationBinder class. |

#### Methods

| Name | Description |
| --- | --- |
| BindToName(Type, out string, out string) | Determines the assembly name and type name for the specified serializedType . |
| BindToType(string, string) | Determines the Type of the object with the specified typeName . |

Parent topic:

NationalInstruments.VeriStand.ClientAPI.Logging

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-dataloggingsessionerroreventargs-error.html language=enus -->
## TOPIC 00396: Error

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-dataloggingsessionerroreventargs-error.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-dataloggingsessionerroreventargs-error.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a value indicating the error that occurred during the data logging session. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic Error Error { get; }ReturnsError information, including a numeric code and a string message.

### Error

Gets a value indicating the error that occurred during the data logging session.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public Error Error { get; }

#### Returns

Error information, including a numeric code and a string message.

Parent topic:

DataLoggingSessionErrorEventArgs Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-dataloggingsessionerroreventargs-sessionname.html language=enus -->
## TOPIC 00397: SessionName

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-dataloggingsessionerroreventargs-sessionname.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-dataloggingsessionerroreventargs-sessionname.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a value indicating the unique name of the data logging session. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic string SessionName { get; }ReturnsThe name of the data logging session.

### SessionName

Gets a value indicating the unique name of the data logging session.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public string SessionName { get; }

#### Returns

The name of the data logging session.

Parent topic:

DataLoggingSessionErrorEventArgs Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-dataloggingsessionerroreventargs.html language=enus -->
## TOPIC 00398: DataLoggingSessionErrorEventArgs Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-dataloggingsessionerroreventargs.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-dataloggingsessionerroreventargs.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides data about errors that occur during data logging sessions for the DataLoggingSessionError event. Derives fromEventArgsSyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic class DataLoggingSessionErrorEventArgs : EventArgsPropertiesNameDescriptionErrorGets a value indicatin

### DataLoggingSessionErrorEventArgs Class

Provides data about errors that occur during data logging sessions for the [DataLoggingSessionError](nationalinstruments-veristand-clientapi-logging-idatalogging-dataloggingsessionerror.html) event.

#### Derives from

- EventArgs

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public class DataLoggingSessionErrorEventArgs : EventArgs

#### Properties

| Name | Description |
| --- | --- |
| Error | Gets a value indicating the error that occurred during the data logging session. |
| SessionName | Gets a value indicating the unique name of the data logging session. |

Parent topic:

NationalInstruments.VeriStand.ClientAPI.Logging

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-dataloggingsessionstarteventargs-sessionname.html language=enus -->
## TOPIC 00399: SessionName

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-dataloggingsessionstarteventargs-sessionname.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-dataloggingsessionstarteventargs-sessionname.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a value indicating the unique name of the data logging session. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic string SessionName { get; }ReturnsThe name of the data logging session.

### SessionName

Gets a value indicating the unique name of the data logging session.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public string SessionName { get; }

#### Returns

The name of the data logging session.

Parent topic:

DataLoggingSessionStartEventArgs Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-dataloggingsessionstarteventargs.html language=enus -->
## TOPIC 00400: DataLoggingSessionStartEventArgs Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-dataloggingsessionstarteventargs.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-dataloggingsessionstarteventargs.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides data about a new data logging session for the DataLoggingSessionStart event. Derives fromEventArgsSyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic class DataLoggingSessionStartEventArgs : EventArgsPropertiesNameDescriptionSessionNameGets a value indicating the unique n

### DataLoggingSessionStartEventArgs Class

Provides data about a new data logging session for the [DataLoggingSessionStart](nationalinstruments-veristand-clientapi-logging-idatalogging-dataloggingsessionstart.html) event.

#### Derives from

- EventArgs

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public class DataLoggingSessionStartEventArgs : EventArgs

#### Properties

| Name | Description |
| --- | --- |
| SessionName | Gets a value indicating the unique name of the data logging session. |

Parent topic:

NationalInstruments.VeriStand.ClientAPI.Logging

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-dataloggingsessionstate.html language=enus -->
## TOPIC 00401: DataLoggingSessionState Enumeration

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-dataloggingsessionstate.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-dataloggingsessionstate.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the state of a data logging session. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic enum DataLoggingSessionStateMembersNameValueDescriptionWaitingOnTrigger0Specifies that the data logging session is waiting on the start trigger condition. Triggered1Specifies that th

### DataLoggingSessionState Enumeration

Specifies the state of a data logging session.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public enum DataLoggingSessionState

#### Members

| Name | Value | Description |
| --- | --- | --- |
| WaitingOnTrigger | 0 | Specifies that the data logging session is waiting on the start trigger condition. |
| Triggered | 1 | Specifies that the data logging session start trigger condition has occurred, and that the data logging session is waiting on the stop trigger condition. |
| PostTrigger | 2 | Specifies that the data logging session stop trigger condition has occurred, and that the data logging session post-trigger countdown is not complete. |
| Complete | 3 | The data logging session is complete and will not log any more data. |
| Idle | 4 | Specifies that the data logging session is idle. |
| Error | 5 | Specifies that the data logging session encountered an error. |

Parent topic:

NationalInstruments.VeriStand.ClientAPI.Logging

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-dataloggingsessionstatechangeeventargs-sessionname.html language=enus -->
## TOPIC 00402: SessionName

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-dataloggingsessionstatechangeeventargs-sessionname.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-dataloggingsessionstatechangeeventargs-sessionname.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a value indicating the unique name of the data logging session. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic string SessionName { get; }ReturnsThe name of the data logging session.

### SessionName

Gets a value indicating the unique name of the data logging session.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public string SessionName { get; }

#### Returns

The name of the data logging session.

Parent topic:

DataLoggingSessionStateChangeEventArgs Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-dataloggingsessionstatechangeeventargs-state.html language=enus -->
## TOPIC 00403: State

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-dataloggingsessionstatechangeeventargs-state.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-dataloggingsessionstatechangeeventargs-state.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a value indicating the state of the data logging session. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic DataLoggingSessionState State { get; }ReturnsAn enumeration of DataLoggingSessionState.

### State

Gets a value indicating the state of the data logging session.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public [DataLoggingSessionState](nationalinstruments-veristand-clientapi-logging-dataloggingsessionstate.html) State { get; }

#### Returns

An enumeration of [DataLoggingSessionState](nationalinstruments-veristand-clientapi-logging-dataloggingsessionstate.html).

Parent topic:

DataLoggingSessionStateChangeEventArgs Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-dataloggingsessionstatechangeeventargs.html language=enus -->
## TOPIC 00404: DataLoggingSessionStateChangeEventArgs Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-dataloggingsessionstatechangeeventargs.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-dataloggingsessionstatechangeeventargs.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides data about the state of a data logging session for the DataLoggingSessionStateChange event. Derives fromEventArgsSyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic class DataLoggingSessionStateChangeEventArgs : EventArgsPropertiesNameDescriptionSessionNameGets a value in

### DataLoggingSessionStateChangeEventArgs Class

Provides data about the state of a data logging session for the [DataLoggingSessionStateChange](nationalinstruments-veristand-clientapi-logging-idatalogging-dataloggingsessionstatechange.html) event.

#### Derives from

- EventArgs

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public class DataLoggingSessionStateChangeEventArgs : EventArgs

#### Properties

| Name | Description |
| --- | --- |
| SessionName | Gets a value indicating the unique name of the data logging session. |
| State | Gets a value indicating the state of the data logging session. |

Parent topic:

NationalInstruments.VeriStand.ClientAPI.Logging

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-dataloggingsessionstopeventargs-logfilepaths.html language=enus -->
## TOPIC 00405: LogFilePaths

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-dataloggingsessionstopeventargs-logfilepaths.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-dataloggingsessionstopeventargs-logfilepaths.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a value indicating the paths to all log files generated during the current data logging session. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic string[] LogFilePaths { get; }ReturnsAn array containing the paths to all log files generated during the data logging session.

### LogFilePaths

Gets a value indicating the paths to all log files generated during the current data logging session.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public string[] LogFilePaths { get; }

#### Returns

An array containing the paths to all log files generated during the data logging session.

Parent topic:

DataLoggingSessionStopEventArgs Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-dataloggingsessionstopeventargs-sessionname.html language=enus -->
## TOPIC 00406: SessionName

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-dataloggingsessionstopeventargs-sessionname.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-dataloggingsessionstopeventargs-sessionname.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a value indicating the unique name of the data logging session. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic string SessionName { get; }ReturnsThe name of the data logging session.

### SessionName

Gets a value indicating the unique name of the data logging session.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public string SessionName { get; }

#### Returns

The name of the data logging session.

Parent topic:

DataLoggingSessionStopEventArgs Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-dataloggingsessionstopeventargs.html language=enus -->
## TOPIC 00407: DataLoggingSessionStopEventArgs Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-dataloggingsessionstopeventargs.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-dataloggingsessionstopeventargs.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides data about a data logging session that stopped for the DataLoggingSessionStop event. Derives fromEventArgsSyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic class DataLoggingSessionStopEventArgs : EventArgsPropertiesNameDescriptionLogFilePathsGets a value indicating the

### DataLoggingSessionStopEventArgs Class

Provides data about a data logging session that stopped for the [DataLoggingSessionStop](nationalinstruments-veristand-clientapi-logging-idatalogging-dataloggingsessionstop.html) event.

#### Derives from

- EventArgs

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public class DataLoggingSessionStopEventArgs : EventArgs

#### Properties

| Name | Description |
| --- | --- |
| LogFilePaths | Gets a value indicating the paths to all log files generated during the current data logging session. |
| SessionName | Gets a value indicating the unique name of the data logging session. |

Parent topic:

NationalInstruments.VeriStand.ClientAPI.Logging

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-dataloggingspecification-createtemporarylogfiles.html language=enus -->
## TOPIC 00408: CreateTemporaryLogFiles

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-dataloggingspecification-createtemporarylogfiles.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-dataloggingspecification-createtemporarylogfiles.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets a value indicating whether to create temporary log files, that get deleted when the session is stopped or cleared. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic bool CreateTemporaryLogFiles { get; set; }

### CreateTemporaryLogFiles

Gets or sets a value indicating whether to create temporary log files, that get deleted when the session is stopped or cleared.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public bool CreateTemporaryLogFiles { get; set; }

Parent topic:

DataLoggingSpecification Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-dataloggingspecification-customrate.html language=enus -->
## TOPIC 00409: CustomRate

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-dataloggingspecification-customrate.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-dataloggingspecification-customrate.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets a value indicating the requested rate in Hertz at which data will be logged. The actual rates at which data is logged may be coerced to an even divisor of the rates at which the targets in the system definition produce data. This property is ignored unless LogDataAtTargetRate is false.

### CustomRate

Gets or sets a value indicating the requested rate in Hertz at which data will be logged. The actual rates at which data is logged may be coerced to an even divisor of the rates at which the targets in the system definition produce data. This property is ignored unless LogDataAtTargetRate is false.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public double CustomRate { get; set; }

Parent topic:

DataLoggingSpecification Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-dataloggingspecification-dataloggingspecification__logfile-trigger-double-bool-trigger-double-segmentingspecification-bool-bool-double-int.html language=enus -->
## TOPIC 00410: DataLoggingSpecification(LogFile, Trigger, double, bool, Trigger, double, SegmentingSpecification, bool, bool, double, int)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-dataloggingspecification-dataloggingspecification__logfile-trigger-double-bool-trigger-double-segmentingspecification-bool-bool-double-int.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-dataloggingspecification-dataloggingspecification__logfile-trigger-double-bool-trigger-double-segmentingspecification-bool-bool-double-int.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the DataLoggingSpecification class. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic DataLoggingSpecification(LogFile logFile, Trigger startTrigger, double preTriggerDuration, bool retriggerable, Trigger stopTrigger, double postTriggerDuration, Seg

### DataLoggingSpecification(LogFile, Trigger, double, bool, Trigger, double, SegmentingSpecification, bool, bool, double, int)

Initializes a new instance of the DataLoggingSpecification class.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public DataLoggingSpecification(LogFile logFile, Trigger startTrigger, double preTriggerDuration, bool retriggerable, Trigger stopTrigger, double postTriggerDuration, SegmentingSpecification segmentingSpecification, bool segmentFileOnTrigger, bool logDataAtTargetRate, double customRate, int minimumBufferSize)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| logFile | LogFile | The log file specification for the data logging session. This includes information about the type of log files to create and the channels to log. |
| startTrigger | Trigger | The condition used to determine when to start logging. |
| preTriggerDuration | double | The duration in seconds of data that is logged before the start trigger condition occurs. |
| retriggerable | bool | Specifies whether logging is retriggerable. If this is true, then data logging can be triggered by the start trigger condition after it has completed logging data from the previous start trigger instance. |
| stopTrigger | Trigger | The condition used to determine when to stop logging. |
| postTriggerDuration | double | The duration in seconds of data that is logged after the stop trigger condition occurs. |
| segmentingSpecification | SegmentingSpecification | The condition that determines when to segment a log file. When the condition occurs, the current instance of the log file is closed, and data continues to be logged to a new log file instance. |
| segmentFileOnTrigger | bool | Specifies whether to create a new file instance each time the start trigger condition occurs. Segmenting the log file for each start trigger instance ensures that all data logged to a file is contiguous in time. |
| logDataAtTargetRate | bool | Gets or sets a value indicating whether data is logged at the rate at which the target is running. Set this property to true to log all data produced by a target. If this property is false, data is logged using the rate specified by customRate. |
| customRate | double | The requested rate in Hertz at which data will be logged. The actual rates at which data is logged may be coerced to an even divisor of the rates at which the targets in the system definition produce data. This property is ignored unless LogDataAtTargetRate is false. |
| minimumBufferSize | int | The minimum size of data buffered while logging. Increasing the minimum buffer size can improve logging performance but requires additional memory resources. |

Parent topic:

DataLoggingSpecification Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-dataloggingspecification-dataloggingspecification__logfile-trigger-double-long-trigger-double-segmentingspecification-bool-bool-double-int.html language=enus -->
## TOPIC 00411: DataLoggingSpecification(LogFile, Trigger, double, long, Trigger, double, SegmentingSpecification, bool, bool, double, int)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-dataloggingspecification-dataloggingspecification__logfile-trigger-double-long-trigger-double-segmentingspecification-bool-bool-double-int.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-dataloggingspecification-dataloggingspecification__logfile-trigger-double-long-trigger-double-segmentingspecification-bool-bool-double-int.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the DataLoggingSpecification class. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic DataLoggingSpecification(LogFile logFile, Trigger startTrigger, double preTriggerDuration, long retriggerCount, Trigger stopTrigger, double postTriggerDuration, Se

### DataLoggingSpecification(LogFile, Trigger, double, long, Trigger, double, SegmentingSpecification, bool, bool, double, int)

Initializes a new instance of the DataLoggingSpecification class.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public DataLoggingSpecification(LogFile logFile, Trigger startTrigger, double preTriggerDuration, long retriggerCount, Trigger stopTrigger, double postTriggerDuration, SegmentingSpecification segmentingSpecification, bool segmentFileOnTrigger, bool logDataAtTargetRate, double customRate, int minimumBufferSize)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| logFile | LogFile | The log file specification for the data logging session. This includes information about the type of log files to create and the channels to log. |
| startTrigger | Trigger | The condition used to determine when to start logging. |
| preTriggerDuration | double | The duration in seconds of data that is logged before the start trigger condition occurs. |
| retriggerCount | long | Specifies the number of retriggers. If this is greater than zero, then data logging can be triggered by the start trigger condition after it has completed logging data from the previous start trigger instance. A negative value means infinite retriggering. A value of zero means no retriggering. |
| stopTrigger | Trigger | The condition used to determine when to stop logging. |
| postTriggerDuration | double | The duration in seconds of data that is logged after the stop trigger condition occurs. |
| segmentingSpecification | SegmentingSpecification | The condition that determines when to segment a log file. When the condition occurs, the current instance of the log file is closed, and data continues to be logged to a new log file instance. |
| segmentFileOnTrigger | bool | Specifies whether to create a new file instance each time the start trigger condition occurs. Segmenting the log file for each start trigger instance ensures that all data logged to a file is contiguous in time. |
| logDataAtTargetRate | bool | Gets or sets a value indicating whether data is logged at the rate at which the target is running. Set this property to true to log all data produced by a target. If this property is false, data is logged using the rate specified by customRate. |
| customRate | double | The requested rate in Hertz at which data will be logged. The actual rates at which data is logged may be coerced to an even divisor of the rates at which the targets in the system definition produce data. This property is ignored unless LogDataAtTargetRate is false. |
| minimumBufferSize | int | The minimum size of data buffered while logging. Increasing the minimum buffer size can improve logging performance but requires additional memory resources. |

Parent topic:

DataLoggingSpecification Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-dataloggingspecification-dataloggingspecification__logfile.html language=enus -->
## TOPIC 00412: DataLoggingSpecification(LogFile)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-dataloggingspecification-dataloggingspecification__logfile.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-dataloggingspecification-dataloggingspecification__logfile.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the DataLoggingSpecification class with default settings. The log is set to start immediately and log indefinitely. Data is logged at the rate at which the targets are running. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic DataLoggingSpecificati

### DataLoggingSpecification(LogFile)

Initializes a new instance of the DataLoggingSpecification class with default settings. The log is set to start immediately and log indefinitely. Data is logged at the rate at which the targets are running.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public DataLoggingSpecification(LogFile logFile)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| logFile | LogFile | The log file specification for the data logging session. This includes information about the type of log files to create and the channels to log. |

Parent topic:

DataLoggingSpecification Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-dataloggingspecification-logdataagainstabsolutetimebase.html language=enus -->
## TOPIC 00413: LogDataAgainstAbsoluteTimeBase

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-dataloggingspecification-logdataagainstabsolutetimebase.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-dataloggingspecification-logdataagainstabsolutetimebase.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets a value indicating whether to log data against an absolute time base from the system clock on the target. If this value is false, no timing information will be added to the log file. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic bool LogDataAgainstAbsoluteTimeBa

### LogDataAgainstAbsoluteTimeBase

Gets or sets a value indicating whether to log data against an absolute time base from the system clock on the target. If this value is false, no timing information will be added to the log file.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public bool LogDataAgainstAbsoluteTimeBase { get; set; }

Parent topic:

DataLoggingSpecification Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-dataloggingspecification-logdataattargetrate.html language=enus -->
## TOPIC 00414: LogDataAtTargetRate

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-dataloggingspecification-logdataattargetrate.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-dataloggingspecification-logdataattargetrate.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets a value indicating whether data is logged at the rate at which the target is running. Set this property to true to log all data produced by a target. If this property is false, data is logged using the rate specified by CustomRate. SyntaxNamespace: NationalInstruments.VeriStand.ClientAP

### LogDataAtTargetRate

Gets or sets a value indicating whether data is logged at the rate at which the target is running. Set this property to true to log all data produced by a target. If this property is false, data is logged using the rate specified by CustomRate.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public bool LogDataAtTargetRate { get; set; }

Parent topic:

DataLoggingSpecification Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-dataloggingspecification-logfile.html language=enus -->
## TOPIC 00415: LogFile

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-dataloggingspecification-logfile.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-dataloggingspecification-logfile.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets a value indicating the log file specification for the data logging session. This includes information about the type of log files to create and the channels to log. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic LogFile LogFile { get; set; }

### LogFile

Gets or sets a value indicating the log file specification for the data logging session. This includes information about the type of log files to create and the channels to log.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public [LogFile](nationalinstruments-veristand-clientapi-logging-logfile.html) LogFile { get; set; }

Parent topic:

DataLoggingSpecification Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-dataloggingspecification-minimumbuffersize.html language=enus -->
## TOPIC 00416: MinimumBufferSize

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-dataloggingspecification-minimumbuffersize.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-dataloggingspecification-minimumbuffersize.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets a value indicating the minimum size of data buffered while logging. Increasing the minimum buffer size can improve logging performance but requires additional memory resources. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic int MinimumBufferSize { get; set; }

### MinimumBufferSize

Gets or sets a value indicating the minimum size of data buffered while logging. Increasing the minimum buffer size can improve logging performance but requires additional memory resources.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public int MinimumBufferSize { get; set; }

Parent topic:

DataLoggingSpecification Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-dataloggingspecification-posttriggerduration.html language=enus -->
## TOPIC 00417: PostTriggerDuration

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-dataloggingspecification-posttriggerduration.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-dataloggingspecification-posttriggerduration.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets a value indicating the duration in seconds of data that is logged after the stop trigger condition occurs. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic double PostTriggerDuration { get; set; }

### PostTriggerDuration

Gets or sets a value indicating the duration in seconds of data that is logged after the stop trigger condition occurs.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public double PostTriggerDuration { get; set; }

Parent topic:

DataLoggingSpecification Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-dataloggingspecification-pretriggerduration.html language=enus -->
## TOPIC 00418: PreTriggerDuration

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-dataloggingspecification-pretriggerduration.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-dataloggingspecification-pretriggerduration.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets a value indicating the duration in seconds of data that is logged before the start trigger condition occurs. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic double PreTriggerDuration { get; set; }

### PreTriggerDuration

Gets or sets a value indicating the duration in seconds of data that is logged before the start trigger condition occurs.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public double PreTriggerDuration { get; set; }

Parent topic:

DataLoggingSpecification Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-dataloggingspecification-retriggerable.html language=enus -->
## TOPIC 00419: Retriggerable

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-dataloggingspecification-retriggerable.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-dataloggingspecification-retriggerable.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets a value indicating whether logging is retriggerable. If this is true, then data logging can be triggered by the start trigger condition after it has completed logging data from the previous start trigger instance. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic bo

### Retriggerable

Gets or sets a value indicating whether logging is retriggerable. If this is true, then data logging can be triggered by the start trigger condition after it has completed logging data from the previous start trigger instance.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public bool Retriggerable { get; set; }

Parent topic:

DataLoggingSpecification Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-dataloggingspecification-retriggercount.html language=enus -->
## TOPIC 00420: RetriggerCount

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-dataloggingspecification-retriggercount.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-dataloggingspecification-retriggercount.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the number of retriggering. A negative value means infinite retriggering. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic long RetriggerCount { get; set; }

### RetriggerCount

Gets or sets the number of retriggering. A negative value means infinite retriggering.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public long RetriggerCount { get; set; }

Parent topic:

DataLoggingSpecification Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-dataloggingspecification-segmentfileontrigger.html language=enus -->
## TOPIC 00421: SegmentFileOnTrigger

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-dataloggingspecification-segmentfileontrigger.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-dataloggingspecification-segmentfileontrigger.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets a value indicating whether to create a new file instance each time the start trigger condition occurs. Segmenting the log file for each start trigger instance ensures that all data logged to a file is contiguous in time. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpu

### SegmentFileOnTrigger

Gets or sets a value indicating whether to create a new file instance each time the start trigger condition occurs. Segmenting the log file for each start trigger instance ensures that all data logged to a file is contiguous in time.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public bool SegmentFileOnTrigger { get; set; }

Parent topic:

DataLoggingSpecification Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-dataloggingspecification-segmentingspecification.html language=enus -->
## TOPIC 00422: SegmentingSpecification

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-dataloggingspecification-segmentingspecification.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-dataloggingspecification-segmentingspecification.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets a value indicating the condition that determines when to segment a log file. When the condition occurs, the current instance of the log file is closed, and data continues to be logged to a new log file instance. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic Segm

### SegmentingSpecification

Gets or sets a value indicating the condition that determines when to segment a log file. When the condition occurs, the current instance of the log file is closed, and data continues to be logged to a new log file instance.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public [SegmentingSpecification](nationalinstruments-veristand-clientapi-logging-segmentingspecification.html) SegmentingSpecification { get; set; }

Parent topic:

DataLoggingSpecification Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-dataloggingspecification-setlogfilesreadonlyonclose.html language=enus -->
## TOPIC 00423: SetLogFilesReadOnlyOnClose

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-dataloggingspecification-setlogfilesreadonlyonclose.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-dataloggingspecification-setlogfilesreadonlyonclose.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets a value indicating whether log files should be set as read-only after being closed. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic bool SetLogFilesReadOnlyOnClose { get; set; }

### SetLogFilesReadOnlyOnClose

Gets or sets a value indicating whether log files should be set as read-only after being closed.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public bool SetLogFilesReadOnlyOnClose { get; set; }

Parent topic:

DataLoggingSpecification Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-dataloggingspecification-starttrigger.html language=enus -->
## TOPIC 00424: StartTrigger

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-dataloggingspecification-starttrigger.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-dataloggingspecification-starttrigger.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets a value indicating the condition used to determine when to start logging. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic Trigger StartTrigger { get; set; }

### StartTrigger

Gets or sets a value indicating the condition used to determine when to start logging.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public [Trigger](nationalinstruments-veristand-clientapi-logging-trigger.html) StartTrigger { get; set; }

Parent topic:

DataLoggingSpecification Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-dataloggingspecification-stoplogondataloss.html language=enus -->
## TOPIC 00425: StopLogOnDataLoss

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-dataloggingspecification-stoplogondataloss.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-dataloggingspecification-stoplogondataloss.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets a value indicating whether to stop logging data in the case of data loss. The default value is true. If this value is false and data loss occurs, an error will be generated, but data logging will continue. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic bool StopL

### StopLogOnDataLoss

Gets or sets a value indicating whether to stop logging data in the case of data loss. The default value is true. If this value is false and data loss occurs, an error will be generated, but data logging will continue.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public bool StopLogOnDataLoss { get; set; }

Parent topic:

DataLoggingSpecification Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-dataloggingspecification-stoptrigger.html language=enus -->
## TOPIC 00426: StopTrigger

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-dataloggingspecification-stoptrigger.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-dataloggingspecification-stoptrigger.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets a value indicating the condition used to determine when to stop logging. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic Trigger StopTrigger { get; set; }

### StopTrigger

Gets or sets a value indicating the condition used to determine when to stop logging.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public [Trigger](nationalinstruments-veristand-clientapi-logging-trigger.html) StopTrigger { get; set; }

Parent topic:

DataLoggingSpecification Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-dataloggingspecification.html language=enus -->
## TOPIC 00427: DataLoggingSpecification Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-dataloggingspecification.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-dataloggingspecification.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies properties for a data logging session. Derives fromNoneSyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic class DataLoggingSpecificationConstructorsNameDescriptionDataLoggingSpecification(LogFile)Initializes a new instance of the DataLoggingSpecification class with defa

### DataLoggingSpecification Class

Specifies properties for a data logging session.

#### Derives from

None

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public class DataLoggingSpecification

#### Constructors

| Name | Description |
| --- | --- |
| DataLoggingSpecification(LogFile) | Initializes a new instance of the DataLoggingSpecification class with default settings. The log is set to start immediately and log indefinitely. Data is logged at the rate at which the targets are running. |
| DataLoggingSpecification(LogFile, Trigger, double, long, Trigger, double, SegmentingSpecification, bool, bool, double, int) | Initializes a new instance of the DataLoggingSpecification class. |
| DataLoggingSpecification(LogFile, Trigger, double, bool, Trigger, double, SegmentingSpecification, bool, bool, double, int) | Initializes a new instance of the DataLoggingSpecification class. |

#### Properties

| Name | Description |
| --- | --- |
| CreateTemporaryLogFiles | Gets or sets a value indicating whether to create temporary log files, that get deleted when the session is stopped or cleared. |
| CustomRate | Gets or sets a value indicating the requested rate in Hertz at which data will be logged. The actual rates at which data is logged may be coerced to an even divisor of the rates at which the targets in the system definition produce data. This property is ignored unless LogDataAtTargetRate is false. |
| LogDataAgainstAbsoluteTimeBase | Gets or sets a value indicating whether to log data against an absolute time base from the system clock on the target. If this value is false, no timing information will be added to the log file. |
| LogDataAtTargetRate | Gets or sets a value indicating whether data is logged at the rate at which the target is running. Set this property to true to log all data produced by a target. If this property is false, data is logged using the rate specified by CustomRate. |
| LogFile | Gets or sets a value indicating the log file specification for the data logging session. This includes information about the type of log files to create and the channels to log. |
| MinimumBufferSize | Gets or sets a value indicating the minimum size of data buffered while logging. Increasing the minimum buffer size can improve logging performance but requires additional memory resources. |
| PostTriggerDuration | Gets or sets a value indicating the duration in seconds of data that is logged after the stop trigger condition occurs. |
| PreTriggerDuration | Gets or sets a value indicating the duration in seconds of data that is logged before the start trigger condition occurs. |
| Retriggerable | Gets or sets a value indicating whether logging is retriggerable. If this is true, then data logging can be triggered by the start trigger condition after it has completed logging data from the previous start trigger instance. |
| RetriggerCount | Gets or sets the number of retriggering. A negative value means infinite retriggering. |
| SegmentFileOnTrigger | Gets or sets a value indicating whether to create a new file instance each time the start trigger condition occurs. Segmenting the log file for each start trigger instance ensures that all data logged to a file is contiguous in time. |
| SegmentingSpecification | Gets or sets a value indicating the condition that determines when to segment a log file. When the condition occurs, the current instance of the log file is closed, and data continues to be logged to a new log file instance. |
| SetLogFilesReadOnlyOnClose | Gets or sets a value indicating whether log files should be set as read-only after being closed. |
| StartTrigger | Gets or sets a value indicating the condition used to determine when to start logging. |
| StopLogOnDataLoss | Gets or sets a value indicating whether to stop logging data in the case of data loss. The default value is true. If this value is false and data loss occurs, an error will be generated, but data logging will continue. |
| StopTrigger | Gets or sets a value indicating the condition used to determine when to stop logging. |

Parent topic:

NationalInstruments.VeriStand.ClientAPI.Logging

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-defaulttrigger-defaultresult.html language=enus -->
## TOPIC 00428: DefaultResult

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-defaulttrigger-defaultresult.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-defaulttrigger-defaultresult.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets a value indicating whether the trigger always evaluates to true or false. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic bool DefaultResult { get; set; }

### DefaultResult

Gets or sets a value indicating whether the trigger always evaluates to true or false.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public bool DefaultResult { get; set; }

Parent topic:

DefaultTrigger Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-defaulttrigger-defaulttrigger__bool.html language=enus -->
## TOPIC 00429: DefaultTrigger(bool)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-defaulttrigger-defaulttrigger__bool.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-defaulttrigger-defaulttrigger__bool.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the DefaultTrigger class. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic DefaultTrigger(bool defaultResult)ParametersNameTypeDescriptiondefaultResultboolThe default result to which the trigger always evaluates.

### DefaultTrigger(bool)

Initializes a new instance of the DefaultTrigger class.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public DefaultTrigger(bool defaultResult)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| defaultResult | bool | The default result to which the trigger always evaluates. |

Parent topic:

DefaultTrigger Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-defaulttrigger.html language=enus -->
## TOPIC 00430: DefaultTrigger Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-defaulttrigger.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-defaulttrigger.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies a trigger that always evaluates to a certain result. Derives fromTriggerSyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic class DefaultTrigger : TriggerConstructorsNameDescriptionDefaultTrigger(bool)Initializes a new instance of the DefaultTrigger class. PropertiesName

### DefaultTrigger Class

Specifies a trigger that always evaluates to a certain result.

#### Derives from

- Trigger

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public class DefaultTrigger : Trigger

#### Constructors

| Name | Description |
| --- | --- |
| DefaultTrigger(bool) | Initializes a new instance of the DefaultTrigger class. |

#### Properties

| Name | Description |
| --- | --- |
| DefaultResult | Gets or sets a value indicating whether the trigger always evaluates to true or false. |

Parent topic:

NationalInstruments.VeriStand.ClientAPI.Logging

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-delimiter.html language=enus -->
## TOPIC 00431: Delimiter Enumeration

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-delimiter.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-delimiter.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the delimiter for columns in the text log file. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic enum DelimiterMembersNameValueDescriptionTab0Specifies a tab delimiter. Comma1Specifies a comma delimiter.

### Delimiter Enumeration

Specifies the delimiter for columns in the text log file.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public enum Delimiter

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Tab | 0 | Specifies a tab delimiter. |
| Comma | 1 | Specifies a comma delimiter. |

Parent topic:

NationalInstruments.VeriStand.ClientAPI.Logging

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-digitaledgetrigger-digitaledgetrigger__string-slope.html language=enus -->
## TOPIC 00432: DigitalEdgeTrigger(string, Slope)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-digitaledgetrigger-digitaledgetrigger__string-slope.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-digitaledgetrigger-digitaledgetrigger__string-slope.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the DigitalEdgeTrigger class. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic DigitalEdgeTrigger(string channelPath, Slope slope)ParametersNameTypeDescriptionchannelPathstringThe system definition path of the channel to monitor.slopeSlopeSpecifies

### DigitalEdgeTrigger(string, Slope)

Initializes a new instance of the DigitalEdgeTrigger class.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public DigitalEdgeTrigger(string channelPath, Slope slope)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| channelPath | string | The system definition path of the channel to monitor. |
| slope | Slope | Specifies whether the slope is rising or falling. |

Parent topic:

DigitalEdgeTrigger Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-digitaledgetrigger-slope.html language=enus -->
## TOPIC 00433: Slope

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-digitaledgetrigger-slope.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-digitaledgetrigger-slope.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets a value indicating whether the slope is rising or falling. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic Slope Slope { get; set; }

### Slope

Gets or sets a value indicating whether the slope is rising or falling.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public [Slope](nationalinstruments-veristand-clientapi-logging-slope.html) Slope { get; set; }

Parent topic:

DigitalEdgeTrigger Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-digitaledgetrigger.html language=enus -->
## TOPIC 00434: DigitalEdgeTrigger Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-digitaledgetrigger.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-digitaledgetrigger.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies a trigger condition that occur on an digital edge. Derives fromSingleChannelTriggerSyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic class DigitalEdgeTrigger : SingleChannelTriggerConstructorsNameDescriptionDigitalEdgeTrigger(string, Slope)Initializes a new instance of

### DigitalEdgeTrigger Class

Specifies a trigger condition that occur on an digital edge.

#### Derives from

- SingleChannelTrigger

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public class DigitalEdgeTrigger : SingleChannelTrigger

#### Constructors

| Name | Description |
| --- | --- |
| DigitalEdgeTrigger(string, Slope) | Initializes a new instance of the DigitalEdgeTrigger class. |

#### Properties

| Name | Description |
| --- | --- |
| Slope | Gets or sets a value indicating whether the slope is rising or falling. |

Parent topic:

NationalInstruments.VeriStand.ClientAPI.Logging

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-fileconflictoperation.html language=enus -->
## TOPIC 00435: FileConflictOperation Enumeration

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-fileconflictoperation.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-fileconflictoperation.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies options for what to do if a file already exists at the specified location. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic enum FileConflictOperationMembersNameValueDescriptionCreateUnique0Create a new file with a unique path. AppendToExisting1Append to the existing

### FileConflictOperation Enumeration

Specifies options for what to do if a file already exists at the specified location.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public enum FileConflictOperation

#### Members

| Name | Value | Description |
| --- | --- | --- |
| CreateUnique | 0 | Create a new file with a unique path. |
| AppendToExisting | 1 | Append to the existing file. |
| OverwriteExisting | 2 | Overwrite the existing file. |

Parent topic:

NationalInstruments.VeriStand.ClientAPI.Logging

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-footprintsegmentingspecification-footprintsegmentingspecification__int-ulong-uint.html language=enus -->
## TOPIC 00436: FootprintSegmentingSpecification(int, ulong, uint)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-footprintsegmentingspecification-footprintsegmentingspecification__int-ulong-uint.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-footprintsegmentingspecification-footprintsegmentingspecification__int-ulong-uint.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the FootprintSegmentingSpecification class. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic FootprintSegmentingSpecification(int maxInstances, ulong size, uint sizeCheckPeriod)ParametersNameTypeDescriptionmaxInstancesintThe maximum number of file

### FootprintSegmentingSpecification(int, ulong, uint)

Initializes a new instance of the FootprintSegmentingSpecification class.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public FootprintSegmentingSpecification(int maxInstances, ulong size, uint sizeCheckPeriod)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| maxInstances | int | The maximum number of file instances that can be created. A value of -1 indicates that an unlimited number of file instances can be created. |
| size | ulong | The minimum size in bytes at which a log file will be segmented. |
| sizeCheckPeriod | uint | The minimum period in milliseconds at which the size of the file is checked. |

Parent topic:

FootprintSegmentingSpecification Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-footprintsegmentingspecification-size.html language=enus -->
## TOPIC 00437: Size

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-footprintsegmentingspecification-size.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-footprintsegmentingspecification-size.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets a value indicating the minimum size in bytes at which a log file will be segmented. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic ulong Size { get; set; }

### Size

Gets or sets a value indicating the minimum size in bytes at which a log file will be segmented.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public ulong Size { get; set; }

Parent topic:

FootprintSegmentingSpecification Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-footprintsegmentingspecification-sizecheckperiod.html language=enus -->
## TOPIC 00438: SizeCheckPeriod

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-footprintsegmentingspecification-sizecheckperiod.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-footprintsegmentingspecification-sizecheckperiod.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets a value indicating the minimum period in milliseconds at which the size of the file is checked. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic uint SizeCheckPeriod { get; set; }

### SizeCheckPeriod

Gets or sets a value indicating the minimum period in milliseconds at which the size of the file is checked.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public uint SizeCheckPeriod { get; set; }

Parent topic:

FootprintSegmentingSpecification Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-footprintsegmentingspecification.html language=enus -->
## TOPIC 00439: FootprintSegmentingSpecification Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-footprintsegmentingspecification.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-footprintsegmentingspecification.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies to segment log files after they reach a certain size in bytes. Derives fromSegmentingSpecificationSyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic class FootprintSegmentingSpecification : SegmentingSpecificationConstructorsNameDescriptionFootprintSegmentingSpecificati

### FootprintSegmentingSpecification Class

Specifies to segment log files after they reach a certain size in bytes.

#### Derives from

- SegmentingSpecification

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public class FootprintSegmentingSpecification : SegmentingSpecification

#### Constructors

| Name | Description |
| --- | --- |
| FootprintSegmentingSpecification(int, ulong, uint) | Initializes a new instance of the FootprintSegmentingSpecification class. |

#### Properties

| Name | Description |
| --- | --- |
| Size | Gets or sets a value indicating the minimum size in bytes at which a log file will be segmented. |
| SizeCheckPeriod | Gets or sets a value indicating the minimum period in milliseconds at which the size of the file is checked. |

Parent topic:

NationalInstruments.VeriStand.ClientAPI.Logging

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-formulatrigger-addvariablemapping__string-string.html language=enus -->
## TOPIC 00440: AddVariableMapping(string, string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-formulatrigger-addvariablemapping__string-string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-formulatrigger-addvariablemapping__string-string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds a mapping of a variable name used in the formula to a system definition channel path. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic void AddVariableMapping(string variableName, string channelPath)ParametersNameTypeDescriptionvariableNamestringThe name of the variable us

### AddVariableMapping(string, string)

Adds a mapping of a variable name used in the formula to a system definition channel path.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public void AddVariableMapping(string variableName, string channelPath)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| variableName | string | The name of the variable used in the formula. |
| channelPath | string | The system definition path of the channel to evaluate in the formula. |

Parent topic:

FormulaTrigger Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-formulatrigger-formula.html language=enus -->
## TOPIC 00441: Formula

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-formulatrigger-formula.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-formulatrigger-formula.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets a value indicating the formula to evaluate. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic string Formula { get; set; }

### Formula

Gets or sets a value indicating the formula to evaluate.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public string Formula { get; set; }

Parent topic:

FormulaTrigger Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-formulatrigger-formulatrigger.html language=enus -->
## TOPIC 00442: FormulaTrigger()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-formulatrigger-formulatrigger.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-formulatrigger-formulatrigger.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the FormulaTrigger class. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic FormulaTrigger()

### FormulaTrigger()

Initializes a new instance of the FormulaTrigger class.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public FormulaTrigger()

Parent topic:

FormulaTrigger Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-formulatrigger-getmappedvariablenames.html language=enus -->
## TOPIC 00443: GetMappedVariableNames()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-formulatrigger-getmappedvariablenames.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-formulatrigger-getmappedvariablenames.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the names of all variables that have defined mappings to system definition channels. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic string[] GetMappedVariableNames()ReturnsThe variable names that have defined mappings to system definition channels.

### GetMappedVariableNames()

Returns the names of all variables that have defined mappings to system definition channels.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public string[] GetMappedVariableNames()

#### Returns

The variable names that have defined mappings to system definition channels.

Parent topic:

FormulaTrigger Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-formulatrigger-getvariablemapping__string.html language=enus -->
## TOPIC 00444: GetVariableMapping(string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-formulatrigger-getvariablemapping__string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-formulatrigger-getvariablemapping__string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the system definition channel mapped to the specified variable. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic string GetVariableMapping(string variableName)ParametersNameTypeDescriptionvariableNamestringThe name of the variable used in the formula.ReturnsThe system d

### GetVariableMapping(string)

Returns the system definition channel mapped to the specified variable.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public string GetVariableMapping(string variableName)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| variableName | string | The name of the variable used in the formula. |

#### Returns

The system definition path of the channel to evaluate in the formula.

Parent topic:

FormulaTrigger Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-formulatrigger.html language=enus -->
## TOPIC 00445: FormulaTrigger Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-formulatrigger.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-formulatrigger.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies a trigger condition based on a Boolean expression that operates on a set of channel values. Derives fromTriggerSyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic class FormulaTrigger : TriggerConstructorsNameDescriptionFormulaTrigger()Initializes a new instance of the F

### FormulaTrigger Class

Specifies a trigger condition based on a Boolean expression that operates on a set of channel values.

#### Derives from

- Trigger

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public class FormulaTrigger : Trigger

#### Constructors

| Name | Description |
| --- | --- |
| FormulaTrigger() | Initializes a new instance of the FormulaTrigger class. |

#### Properties

| Name | Description |
| --- | --- |
| Formula | Gets or sets a value indicating the formula to evaluate. |

#### Methods

| Name | Description |
| --- | --- |
| AddVariableMapping(string, string) | Adds a mapping of a variable name used in the formula to a system definition channel path. |
| GetMappedVariableNames() | Returns the names of all variables that have defined mappings to system definition channels. |
| GetVariableMapping(string) | Returns the system definition channel mapped to the specified variable. |

Parent topic:

NationalInstruments.VeriStand.ClientAPI.Logging

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-idatalogging-cleardataloggingsession__string.html language=enus -->
## TOPIC 00446: ClearDataLoggingSession(string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-idatalogging-cleardataloggingsession__string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-idatalogging-cleardataloggingsession__string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Removes given session from list of active sessions and deletes any temporary log files created. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic Error ClearDataLoggingSession(string sessionName)ParametersNameTypeDescriptionsessionNamestringSpecifies the unique name of the data

### ClearDataLoggingSession(string)

Removes given session from list of active sessions and deletes any temporary log files created.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public [Error](nationalinstruments-veristand-clientapi-logging-dataloggingsessionstate.html) ClearDataLoggingSession(string sessionName)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| sessionName | string | Specifies the unique name of the data logging session. |

#### Returns

Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0.

Parent topic:

IDataLogging Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-idatalogging-dataloggingsessionerror.html language=enus -->
## TOPIC 00447: DataLoggingSessionError

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-idatalogging-dataloggingsessionerror.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-idatalogging-dataloggingsessionerror.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Callback invoked when a data logging session produces an error. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic EventHandler< DataLoggingSessionErrorEventArgs > DataLoggingSessionError

### DataLoggingSessionError

Callback invoked when a data logging session produces an error.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public EventHandler< [DataLoggingSessionErrorEventArgs](nationalinstruments-veristand-clientapi-logging-dataloggingsessionerroreventargs.html) > DataLoggingSessionError

Parent topic:

IDataLogging Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-idatalogging-dataloggingsessionstart.html language=enus -->
## TOPIC 00448: DataLoggingSessionStart

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-idatalogging-dataloggingsessionstart.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-idatalogging-dataloggingsessionstart.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Callback invoked when a new data logging session starts. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic EventHandler< DataLoggingSessionStartEventArgs > DataLoggingSessionStart

### DataLoggingSessionStart

Callback invoked when a new data logging session starts.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public EventHandler< [DataLoggingSessionStartEventArgs](nationalinstruments-veristand-clientapi-logging-dataloggingsessionstarteventargs.html) > DataLoggingSessionStart

Parent topic:

IDataLogging Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-idatalogging-dataloggingsessionstatechange.html language=enus -->
## TOPIC 00449: DataLoggingSessionStateChange

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-idatalogging-dataloggingsessionstatechange.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-idatalogging-dataloggingsessionstatechange.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Callback invoked when a data logging session changes state. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic EventHandler< DataLoggingSessionStateChangeEventArgs > DataLoggingSessionStateChange

### DataLoggingSessionStateChange

Callback invoked when a data logging session changes state.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public EventHandler< [DataLoggingSessionStateChangeEventArgs](nationalinstruments-veristand-clientapi-logging-dataloggingsessionstatechangeeventargs.html) > DataLoggingSessionStateChange

Parent topic:

IDataLogging Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-idatalogging-dataloggingsessionstop.html language=enus -->
## TOPIC 00450: DataLoggingSessionStop

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-idatalogging-dataloggingsessionstop.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-idatalogging-dataloggingsessionstop.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Callback invoked when a data logging session stops. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic EventHandler< DataLoggingSessionStopEventArgs > DataLoggingSessionStop

### DataLoggingSessionStop

Callback invoked when a data logging session stops.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public EventHandler< [DataLoggingSessionStopEventArgs](nationalinstruments-veristand-clientapi-logging-dataloggingsessionstopeventargs.html) > DataLoggingSessionStop

Parent topic:

IDataLogging Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-idatalogging-downloadlogfiles__string-string_arr1-string-out.html language=enus -->
## TOPIC 00451: DownloadLogFiles(string, string[], string, out Error[])

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-idatalogging-downloadlogfiles__string-string_arr1-string-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-idatalogging-downloadlogfiles__string-string_arr1-string-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a local copies for the given log files. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic Error DownloadLogFiles(string sessionName, string[] logFileNames, string targetDir, out Error[] errors)ParametersNameTypeDescriptionsessionNamestringSession that created this file.l

### DownloadLogFiles(string, string[], string, out Error[])

Creates a local copies for the given log files.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public [Error](nationalinstruments-veristand-clientapi-logging-dataloggingsessionstate.html) DownloadLogFiles(string sessionName, string[] logFileNames, string targetDir, out Error[] errors)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| sessionName | string | Session that created this file. |
| logFileNames | string[] | The names of the log file to download. |
| targetDir | string | The target directory at which to create the log file. |
| errors | out Error[] | An array of NationalInstruments.VeriStand.Error objects corresponding to each file to be downloaded. If no error occurs, the Code property of the Error object is 0. |

#### Returns

Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0.

Parent topic:

IDataLogging Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-idatalogging-getallcompletelogfiles__string-out.html language=enus -->
## TOPIC 00452: GetAllCompleteLogFiles(string, out string[])

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-idatalogging-getallcompletelogfiles__string-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-idatalogging-getallcompletelogfiles__string-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the file paths of all log files generated by the data logging session. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic Error GetAllCompleteLogFiles(string sessionName, out string[] logFilePaths)ParametersNameTypeDescriptionsessionNamestringSpecifies the unique name of

### GetAllCompleteLogFiles(string, out string[])

Returns the file paths of all log files generated by the data logging session.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public [Error](nationalinstruments-veristand-clientapi-logging-dataloggingsessionstate.html) GetAllCompleteLogFiles(string sessionName, out string[] logFilePaths)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| sessionName | string | Specifies the unique name of the data logging session. |
| logFilePaths | out string[] | Indicates the file paths of all log files generated by the data logging session. |

#### Returns

Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0.

Parent topic:

IDataLogging Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-idatalogging-getalldataloggingsessionsnames__out.html language=enus -->
## TOPIC 00453: GetAllDataLoggingSessionsNames(out string[])

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-idatalogging-getalldataloggingsessionsnames__out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-idatalogging-getalldataloggingsessionsnames__out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the session names of all data logging sessions. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic Error GetAllDataLoggingSessionsNames(out string[] sessionNames)ParametersNameTypeDescriptionsessionNamesout string[]Indicates the session names of all data logging sessions.

### GetAllDataLoggingSessionsNames(out string[])

Returns the session names of all data logging sessions.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public [Error](nationalinstruments-veristand-clientapi-logging-dataloggingsessionstate.html) GetAllDataLoggingSessionsNames(out string[] sessionNames)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| sessionNames | out string[] | Indicates the session names of all data logging sessions. |

#### Returns

Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0.

Parent topic:

IDataLogging Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-idatalogging-getcurrentlogfileinfo__string-out-out-out.html language=enus -->
## TOPIC 00454: GetCurrentLogFileInfo(string, out string, out long, out DateTime)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-idatalogging-getcurrentlogfileinfo__string-out-out-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-idatalogging-getcurrentlogfileinfo__string-out-out-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns information about the current log file for the data logging session. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic Error GetCurrentLogFileInfo(string sessionName, out string logFilePath, out long size, out DateTime startTime)ParametersNameTypeDescriptionsessionNamest

### GetCurrentLogFileInfo(string, out string, out long, out DateTime)

Returns information about the current log file for the data logging session.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public [Error](nationalinstruments-veristand-clientapi-logging-dataloggingsessionstate.html) GetCurrentLogFileInfo(string sessionName, out string logFilePath, out long size, out DateTime startTime)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| sessionName | string | Specifies the unique name of the data logging session. |
| logFilePath | out string | Indicates the file path of the current log file. |
| size | out long | Indicates the file size in bytes of the current log file. |
| startTime | out DateTime | Indicates the time when the current log file was opened. |

#### Returns

Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0.

Parent topic:

IDataLogging Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-idatalogging-getdataloggingsessionspecification__string-out.html language=enus -->
## TOPIC 00455: GetDataLoggingSessionSpecification(string, out DataLoggingSpecification)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-idatalogging-getdataloggingsessionspecification__string-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-idatalogging-getdataloggingsessionspecification__string-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the data logging specification for the data logging session. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic Error GetDataLoggingSessionSpecification(string sessionName, out DataLoggingSpecification dataLoggingSpecification)ParametersNameTypeDescriptionsessionNamestrin

### GetDataLoggingSessionSpecification(string, out DataLoggingSpecification)

Returns the data logging specification for the data logging session.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public [Error](nationalinstruments-veristand-clientapi-logging-dataloggingsessionstate.html) GetDataLoggingSessionSpecification(string sessionName, out DataLoggingSpecification dataLoggingSpecification)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| sessionName | string | Specifies the unique name of the data logging session. |
| dataLoggingSpecification | out DataLoggingSpecification | Specifies the settings of the data logging session. |

#### Returns

Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0.

Parent topic:

IDataLogging Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-idatalogging-getdataloggingsessionstate__string-out.html language=enus -->
## TOPIC 00456: GetDataLoggingSessionState(string, out DataLoggingSessionState)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-idatalogging-getdataloggingsessionstate__string-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-idatalogging-getdataloggingsessionstate__string-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the state of the data logging session. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic Error GetDataLoggingSessionState(string sessionName, out DataLoggingSessionState state)ParametersNameTypeDescriptionsessionNamestringSpecifies the unique name of the data logging ses

### GetDataLoggingSessionState(string, out DataLoggingSessionState)

Returns the state of the data logging session.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public [Error](nationalinstruments-veristand-clientapi-logging-dataloggingsessionstate.html) GetDataLoggingSessionState(string sessionName, out DataLoggingSessionState state)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| sessionName | string | Specifies the unique name of the data logging session. |
| state | out DataLoggingSessionState | Indicates the state of the data logging session. |

#### Returns

Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0.

Parent topic:

IDataLogging Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-idatalogging-getlasterror__string-out.html language=enus -->
## TOPIC 00457: GetLastError(string, out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-idatalogging-getlasterror__string-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-idatalogging-getlasterror__string-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the last error generated by the data logging session. If no error has been generated, the Code property of the Error object is 0. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic Error GetLastError(string sessionName, out Error lastError)ParametersNameTypeDescriptionses

### GetLastError(string, out Error)

Returns the last error generated by the data logging session. If no error has been generated, the Code property of the Error object is 0.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public [Error](nationalinstruments-veristand-clientapi-logging-dataloggingsessionstate.html) GetLastError(string sessionName, out Error lastError)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| sessionName | string | Specifies the unique name of the data logging session. |
| lastError | out Error | Indicates the last error generated by the data logging specification. If no error has been generated, the Code property of the Error object is 0. |

#### Returns

Returns an NationalInstruments.VeriStand.Error object indicating the status of the request. If no error occurs, the Code property of the Error object is 0.

Parent topic:

IDataLogging Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-idatalogging-logfileclosed.html language=enus -->
## TOPIC 00458: LogFileClosed

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-idatalogging-logfileclosed.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-idatalogging-logfileclosed.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Callback invoked when a data logging session on the host computer closes a log file. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic EventHandler< LogFileClosedEventArgs > LogFileClosedSee AlsoNationalInstruments.VeriStand.ClientAPI.Logging.IDataLogging.NewLogFilesComplete

### LogFileClosed

Callback invoked when a data logging session on the host computer closes a log file.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public EventHandler< [LogFileClosedEventArgs](nationalinstruments-veristand-clientapi-logging-logfileclosedeventargs.html) > LogFileClosed

#### See Also

- NationalInstruments.VeriStand.ClientAPI.Logging.IDataLogging.NewLogFilesComplete

Parent topic:

IDataLogging Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-idatalogging-logfileopened.html language=enus -->
## TOPIC 00459: LogFileOpened

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-idatalogging-logfileopened.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-idatalogging-logfileopened.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Callback invoked when a data logging session on the host computer opens a log file. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic EventHandler< LogFileOpenedEventArgs > LogFileOpened

### LogFileOpened

Callback invoked when a data logging session on the host computer opens a log file.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public EventHandler< [LogFileOpenedEventArgs](nationalinstruments-veristand-clientapi-logging-logfileopenedeventargs.html) > LogFileOpened

Parent topic:

IDataLogging Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-idatalogging-newlogfilescomplete.html language=enus -->
## TOPIC 00460: NewLogFilesComplete

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-idatalogging-newlogfilescomplete.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-idatalogging-newlogfilescomplete.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Callback invoked when a target generates a new log file. Features that perform logging on a target rather than the host, such as DAQ tasks and XNET raw frame data logging, generate this event. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic EventHandler< NewLogFilesCompleteEve

### NewLogFilesComplete

Callback invoked when a target generates a new log file. Features that perform logging on a target rather than the host, such as DAQ tasks and XNET raw frame data logging, generate this event.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public EventHandler< [NewLogFilesCompleteEventArgs](nationalinstruments-veristand-clientapi-logging-newlogfilescompleteeventargs.html) > NewLogFilesComplete

#### See Also

- NationalInstruments.VeriStand.ClientAPI.Logging.IDataLogging.LogFileClosed

Parent topic:

IDataLogging Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-idatalogging-startdataloggingsession__string-dataloggingspecification.html language=enus -->
## TOPIC 00461: StartDataLoggingSession(string, DataLoggingSpecification)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-idatalogging-startdataloggingsession__string-dataloggingspecification.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-idatalogging-startdataloggingsession__string-dataloggingspecification.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Starts a new data logging session. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic Error StartDataLoggingSession(string sessionName, DataLoggingSpecification dataLoggingSpecification)ParametersNameTypeDescriptionsessionNamestringSpecifies the unique name of the data logging se

### StartDataLoggingSession(string, DataLoggingSpecification)

Starts a new data logging session.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public [Error](nationalinstruments-veristand-clientapi-logging-dataloggingsessionstate.html) StartDataLoggingSession(string sessionName, DataLoggingSpecification dataLoggingSpecification)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| sessionName | string | Specifies the unique name of the data logging session. |
| dataLoggingSpecification | DataLoggingSpecification | Specifies the settings of the data logging session. |

#### Returns

Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0.

Parent topic:

IDataLogging Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-idatalogging-stopdataloggingsession__string-bool-out.html language=enus -->
## TOPIC 00462: StopDataLoggingSession(string, bool, out string[])

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-idatalogging-stopdataloggingsession__string-bool-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-idatalogging-stopdataloggingsession__string-bool-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Stops the data logging session. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic Error StopDataLoggingSession(string sessionName, bool clearSession, out string[] logFilePaths)ParametersNameTypeDescriptionsessionNamestringSpecifies the unique name of the data logging session.cle

### StopDataLoggingSession(string, bool, out string[])

Stops the data logging session.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public [Error](nationalinstruments-veristand-clientapi-logging-dataloggingsessionstate.html) StopDataLoggingSession(string sessionName, bool clearSession, out string[] logFilePaths)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| sessionName | string | Specifies the unique name of the data logging session. |
| clearSession | bool | If true, removes given session from list of active sessions and deletes any temporary log files created. |
| logFilePaths | out string[] | Indicates the file paths of all log files generated by the data logging session. |

#### Returns

Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0.

Parent topic:

IDataLogging Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-idatalogging-stopdataloggingsession__string-out.html language=enus -->
## TOPIC 00463: StopDataLoggingSession(string, out string[])

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-idatalogging-stopdataloggingsession__string-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-idatalogging-stopdataloggingsession__string-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Stops the data logging session. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic Error StopDataLoggingSession(string sessionName, out string[] logFilePaths)ParametersNameTypeDescriptionsessionNamestringSpecifies the unique name of the data logging session.logFilePathsout string

### StopDataLoggingSession(string, out string[])

Stops the data logging session.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public [Error](nationalinstruments-veristand-clientapi-logging-dataloggingsessionstate.html) StopDataLoggingSession(string sessionName, out string[] logFilePaths)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| sessionName | string | Specifies the unique name of the data logging session. |
| logFilePaths | out string[] | Indicates the file paths of all log files generated by the data logging session. |

#### Returns

Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0.

Parent topic:

IDataLogging Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-idatalogging.html language=enus -->
## TOPIC 00464: IDataLogging Interface

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-idatalogging.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-idatalogging.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies an interface to automate data logging in the VeriStand Gateway. Derives fromNoneSyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic interface IDataLoggingMethodsNameDescriptionClearDataLoggingSession(string)Removes given session from list of active sessions and deletes a

### IDataLogging Interface

Specifies an interface to automate data logging in the VeriStand Gateway.

#### Derives from

None

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public interface IDataLogging

#### Methods

| Name | Description |
| --- | --- |
| ClearDataLoggingSession(string) | Removes given session from list of active sessions and deletes any temporary log files created. |
| DownloadLogFiles(string, string[], string, out Error[]) | Creates a local copies for the given log files. |
| GetAllCompleteLogFiles(string, out string[]) | Returns the file paths of all log files generated by the data logging session. |
| GetAllDataLoggingSessionsNames(out string[]) | Returns the session names of all data logging sessions. |
| GetCurrentLogFileInfo(string, out string, out long, out DateTime) | Returns information about the current log file for the data logging session. |
| GetDataLoggingSessionSpecification(string, out DataLoggingSpecification) | Returns the data logging specification for the data logging session. |
| GetDataLoggingSessionState(string, out DataLoggingSessionState) | Returns the state of the data logging session. |
| GetLastError(string, out Error) | Returns the last error generated by the data logging session. If no error has been generated, the Code property of the Error object is 0. |
| StartDataLoggingSession(string, DataLoggingSpecification) | Starts a new data logging session. |
| StopDataLoggingSession(string, bool, out string[]) | Stops the data logging session. |
| StopDataLoggingSession(string, out string[]) | Stops the data logging session. |

#### Events

| Name | Description |
| --- | --- |
| DataLoggingSessionError | Callback invoked when a data logging session produces an error. |
| DataLoggingSessionStart | Callback invoked when a new data logging session starts. |
| DataLoggingSessionStateChange | Callback invoked when a data logging session changes state. |
| DataLoggingSessionStop | Callback invoked when a data logging session stops. |
| LogFileClosed | Callback invoked when a data logging session on the host computer closes a log file. |
| LogFileOpened | Callback invoked when a data logging session on the host computer opens a log file. |
| NewLogFilesComplete | Callback invoked when a target generates a new log file. Features that perform logging on a target rather than the host, such as DAQ tasks and XNET raw frame data logging, generate this event. |

Parent topic:

NationalInstruments.VeriStand.ClientAPI.Logging

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-inrangetrigger-highlimit.html language=enus -->
## TOPIC 00465: HighLimit

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-inrangetrigger-highlimit.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-inrangetrigger-highlimit.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets a value indicating the high limit of the range. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic double HighLimit { get; set; }

### HighLimit

Gets or sets a value indicating the high limit of the range.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public double HighLimit { get; set; }

Parent topic:

InRangeTrigger Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-inrangetrigger-inrangetrigger__string-double-double-bool.html language=enus -->
## TOPIC 00466: InRangeTrigger(string, double, double, bool)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-inrangetrigger-inrangetrigger__string-double-double-bool.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-inrangetrigger-inrangetrigger__string-double-double-bool.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the InRangeTrigger class. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic InRangeTrigger(string channelPath, double lowLimit, double highLimit, bool invert)ParametersNameTypeDescriptionchannelPathstringThe system definition path of the channel to

### InRangeTrigger(string, double, double, bool)

Initializes a new instance of the InRangeTrigger class.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public InRangeTrigger(string channelPath, double lowLimit, double highLimit, bool invert)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| channelPath | string | The system definition path of the channel to monitor. |
| lowLimit | double | The low limit of the range. |
| highLimit | double | The high limit of the range. |
| invert | bool | Specifies whether to invert the range check. If the range check is inverted, then the trigger condition occurs when the value falls outside the specified range. |

Parent topic:

InRangeTrigger Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-inrangetrigger-invert.html language=enus -->
## TOPIC 00467: Invert

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-inrangetrigger-invert.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-inrangetrigger-invert.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets a value indicating whether to invert the range check. If the range check is inverted, then the trigger condition occurs when the value falls outside the specified range. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic bool Invert { get; set; }

### Invert

Gets or sets a value indicating whether to invert the range check. If the range check is inverted, then the trigger condition occurs when the value falls outside the specified range.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public bool Invert { get; set; }

Parent topic:

InRangeTrigger Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-inrangetrigger-lowlimit.html language=enus -->
## TOPIC 00468: LowLimit

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-inrangetrigger-lowlimit.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-inrangetrigger-lowlimit.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets a value indicating the low limit of the range. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic double LowLimit { get; set; }

### LowLimit

Gets or sets a value indicating the low limit of the range.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public double LowLimit { get; set; }

Parent topic:

InRangeTrigger Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-inrangetrigger.html language=enus -->
## TOPIC 00469: InRangeTrigger Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-inrangetrigger.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-inrangetrigger.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies a trigger condition that occurs when a value falls within a specified range. Derives fromSingleChannelTriggerSyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic class InRangeTrigger : SingleChannelTriggerConstructorsNameDescriptionInRangeTrigger(string, double, double, b

### InRangeTrigger Class

Specifies a trigger condition that occurs when a value falls within a specified range.

#### Derives from

- SingleChannelTrigger

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public class InRangeTrigger : SingleChannelTrigger

#### Constructors

| Name | Description |
| --- | --- |
| InRangeTrigger(string, double, double, bool) | Initializes a new instance of the InRangeTrigger class. |

#### Properties

| Name | Description |
| --- | --- |
| HighLimit | Gets or sets a value indicating the high limit of the range. |
| Invert | Gets or sets a value indicating whether to invert the range check. If the range check is inverted, then the trigger condition occurs when the value falls outside the specified range. |
| LowLimit | Gets or sets a value indicating the low limit of the range. |

Parent topic:

NationalInstruments.VeriStand.ClientAPI.Logging

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-logfile-basefilepath.html language=enus -->
## TOPIC 00470: BaseFilePath

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-logfile-basefilepath.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-logfile-basefilepath.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets a value indicating the base file path used to specify the log file path. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic string BaseFilePath { get; set; }

### BaseFilePath

Gets or sets a value indicating the base file path used to specify the log file path.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public string BaseFilePath { get; set; }

Parent topic:

LogFile Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-logfile-fileconflictoperation.html language=enus -->
## TOPIC 00471: FileConflictOperation

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-logfile-fileconflictoperation.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-logfile-fileconflictoperation.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets a value indicating the operation to take if a file already exists at the specified path. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic FileConflictOperation FileConflictOperation { get; set; }

### FileConflictOperation

Gets or sets a value indicating the operation to take if a file already exists at the specified path.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public [FileConflictOperation](nationalinstruments-veristand-clientapi-logging-fileconflictoperation.html) FileConflictOperation { get; set; }

Parent topic:

LogFile Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-logfile-loggingchannels.html language=enus -->
## TOPIC 00472: LoggingChannels

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-logfile-loggingchannels.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-logfile-loggingchannels.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Logfile logging channels. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic HashSet< string > LoggingChannels { get; }

### LoggingChannels

Logfile logging channels.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public HashSet< string > LoggingChannels { get; }

Parent topic:

LogFile Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-logfile.html language=enus -->
## TOPIC 00473: LogFile Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-logfile.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-logfile.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies information about a log file. Derives fromNoneSyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic class LogFilePropertiesNameDescriptionBaseFilePathGets or sets a value indicating the base file path used to specify the log file path. FileConflictOperationGets or sets a v

### LogFile Class

Specifies information about a log file.

#### Derives from

None

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public class LogFile

#### Properties

| Name | Description |
| --- | --- |
| BaseFilePath | Gets or sets a value indicating the base file path used to specify the log file path. |
| FileConflictOperation | Gets or sets a value indicating the operation to take if a file already exists at the specified path. |
| LoggingChannels | Logfile logging channels. |

Parent topic:

NationalInstruments.VeriStand.ClientAPI.Logging

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-logfileclosedeventargs-logfilepath.html language=enus -->
## TOPIC 00474: LogFilePath

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-logfileclosedeventargs-logfilepath.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-logfileclosedeventargs-logfilepath.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a value indicating the path to the log file. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic string LogFilePath { get; }ReturnsThe path to the log file.

### LogFilePath

Gets a value indicating the path to the log file.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public string LogFilePath { get; }

#### Returns

The path to the log file.

Parent topic:

LogFileClosedEventArgs Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-logfileclosedeventargs-sessionname.html language=enus -->
## TOPIC 00475: SessionName

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-logfileclosedeventargs-sessionname.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-logfileclosedeventargs-sessionname.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a value indicating the unique name of the data logging session. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic string SessionName { get; }ReturnsThe name of the data logging session.

### SessionName

Gets a value indicating the unique name of the data logging session.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public string SessionName { get; }

#### Returns

The name of the data logging session.

Parent topic:

LogFileClosedEventArgs Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-logfileclosedeventargs.html language=enus -->
## TOPIC 00476: LogFileClosedEventArgs Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-logfileclosedeventargs.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-logfileclosedeventargs.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides data about a closed log file for the LogFileClosed event. Derives fromEventArgsSyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic class LogFileClosedEventArgs : EventArgsPropertiesNameDescriptionLogFilePathGets a value indicating the path to the log file. SessionNameGets

### LogFileClosedEventArgs Class

Provides data about a closed log file for the [LogFileClosed](nationalinstruments-veristand-clientapi-logging-idatalogging-logfileclosed.html) event.

#### Derives from

- EventArgs

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public class LogFileClosedEventArgs : EventArgs

#### Properties

| Name | Description |
| --- | --- |
| LogFilePath | Gets a value indicating the path to the log file. |
| SessionName | Gets a value indicating the unique name of the data logging session. |

Parent topic:

NationalInstruments.VeriStand.ClientAPI.Logging

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-logfileopenedeventargs-logfilepath.html language=enus -->
## TOPIC 00477: LogFilePath

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-logfileopenedeventargs-logfilepath.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-logfileopenedeventargs-logfilepath.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a value indicating the path to the log file. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic string LogFilePath { get; }ReturnsThe path to the log file.

### LogFilePath

Gets a value indicating the path to the log file.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public string LogFilePath { get; }

#### Returns

The path to the log file.

Parent topic:

LogFileOpenedEventArgs Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-logfileopenedeventargs-sessionname.html language=enus -->
## TOPIC 00478: SessionName

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-logfileopenedeventargs-sessionname.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-logfileopenedeventargs-sessionname.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a value indicating the unique name of the data logging session. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic string SessionName { get; }ReturnsThe name of the data logging session.

### SessionName

Gets a value indicating the unique name of the data logging session.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public string SessionName { get; }

#### Returns

The name of the data logging session.

Parent topic:

LogFileOpenedEventArgs Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-logfileopenedeventargs.html language=enus -->
## TOPIC 00479: LogFileOpenedEventArgs Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-logfileopenedeventargs.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-logfileopenedeventargs.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides data about an opened log file for the LogFileOpened event. Derives fromEventArgsSyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic class LogFileOpenedEventArgs : EventArgsPropertiesNameDescriptionLogFilePathGets a value indicating the path to the log file. SessionNameGet

### LogFileOpenedEventArgs Class

Provides data about an opened log file for the [LogFileOpened](nationalinstruments-veristand-clientapi-logging-idatalogging-logfileopened.html) event.

#### Derives from

- EventArgs

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public class LogFileOpenedEventArgs : EventArgs

#### Properties

| Name | Description |
| --- | --- |
| LogFilePath | Gets a value indicating the path to the log file. |
| SessionName | Gets a value indicating the unique name of the data logging session. |

Parent topic:

NationalInstruments.VeriStand.ClientAPI.Logging

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-newlogfilescompleteeventargs-logfilepaths.html language=enus -->
## TOPIC 00480: LogFilePaths

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-newlogfilescompleteeventargs-logfilepaths.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-newlogfilescompleteeventargs-logfilepaths.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a value indicating the paths to all newly produced log files. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic string[] LogFilePaths { get; }ReturnsAn array containing the paths to all log files.

### LogFilePaths

Gets a value indicating the paths to all newly produced log files.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public string[] LogFilePaths { get; }

#### Returns

An array containing the paths to all log files.

Parent topic:

NewLogFilesCompleteEventArgs Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-newlogfilescompleteeventargs-source.html language=enus -->
## TOPIC 00481: Source

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-newlogfilescompleteeventargs-source.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-newlogfilescompleteeventargs-source.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a value indicating the feature that generated the log files, such as a waveform DAQ task or the Embedded Data Logger custom device. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic string Source { get; }ReturnsThe source of the log files.

### Source

Gets a value indicating the feature that generated the log files, such as a waveform DAQ task or the Embedded Data Logger custom device.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public string Source { get; }

#### Returns

The source of the log files.

Parent topic:

NewLogFilesCompleteEventArgs Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-newlogfilescompleteeventargs-target.html language=enus -->
## TOPIC 00482: Target

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-newlogfilescompleteeventargs-target.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-newlogfilescompleteeventargs-target.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a value indicating the name of the target that contains the log files. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic string Target { get; }ReturnsThe name of the target.

### Target

Gets a value indicating the name of the target that contains the log files.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public string Target { get; }

#### Returns

The name of the target.

Parent topic:

NewLogFilesCompleteEventArgs Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-newlogfilescompleteeventargs.html language=enus -->
## TOPIC 00483: NewLogFilesCompleteEventArgs Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-newlogfilescompleteeventargs.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-newlogfilescompleteeventargs.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides data about newly produced log files on a target for the NewLogFilesComplete event. Derives fromEventArgsSyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic class NewLogFilesCompleteEventArgs : EventArgsPropertiesNameDescriptionLogFilePathsGets a value indicating the paths

### NewLogFilesCompleteEventArgs Class

Provides data about newly produced log files on a target for the [NewLogFilesComplete](nationalinstruments-veristand-clientapi-logging-idatalogging-newlogfilescomplete.html) event.

#### Derives from

- EventArgs

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public class NewLogFilesCompleteEventArgs : EventArgs

#### Properties

| Name | Description |
| --- | --- |
| LogFilePaths | Gets a value indicating the paths to all newly produced log files. |
| Source | Gets a value indicating the feature that generated the log files, such as a waveform DAQ task or the Embedded Data Logger custom device. |
| Target | Gets a value indicating the name of the target that contains the log files. |

Parent topic:

NationalInstruments.VeriStand.ClientAPI.Logging

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-segmentingspecification-maxinstances.html language=enus -->
## TOPIC 00484: MaxInstances

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-segmentingspecification-maxinstances.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-segmentingspecification-maxinstances.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets a value indicating the maximum number of file instances that can be created. A value of -1 indicates that an unlimited number of file instances can be created. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic int MaxInstances { get; set; }

### MaxInstances

Gets or sets a value indicating the maximum number of file instances that can be created. A value of -1 indicates that an unlimited number of file instances can be created.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public int MaxInstances { get; set; }

Parent topic:

SegmentingSpecification Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-segmentingspecification-segmentingspecification.html language=enus -->
## TOPIC 00485: SegmentingSpecification()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-segmentingspecification-segmentingspecification.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-segmentingspecification-segmentingspecification.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the SegmentingSpecification class with an unlimited number of file instances. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic SegmentingSpecification()

### SegmentingSpecification()

Initializes a new instance of the SegmentingSpecification class with an unlimited number of file instances.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public SegmentingSpecification()

Parent topic:

SegmentingSpecification Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-segmentingspecification-segmentingspecification__int.html language=enus -->
## TOPIC 00486: SegmentingSpecification(int)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-segmentingspecification-segmentingspecification__int.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-segmentingspecification-segmentingspecification__int.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the SegmentingSpecification class. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic SegmentingSpecification(int maxInstances)ParametersNameTypeDescriptionmaxInstancesintThe maximum number of file instances that can be created. A value of -1 indicat

### SegmentingSpecification(int)

Initializes a new instance of the SegmentingSpecification class.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public SegmentingSpecification(int maxInstances)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| maxInstances | int | The maximum number of file instances that can be created. A value of -1 indicates that an unlimited number of file instances can be created. |

Parent topic:

SegmentingSpecification Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-segmentingspecification.html language=enus -->
## TOPIC 00487: SegmentingSpecification Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-segmentingspecification.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-segmentingspecification.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies a condition that determines when to segment log files during data logging. This base class specifies never to segment the log file. Derives fromNoneSyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic class SegmentingSpecificationConstructorsNameDescriptionSegmentingSpeci

### SegmentingSpecification Class

Specifies a condition that determines when to segment log files during data logging. This base class specifies never to segment the log file.

#### Derives from

None

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public class SegmentingSpecification

#### Constructors

| Name | Description |
| --- | --- |
| SegmentingSpecification() | Initializes a new instance of the SegmentingSpecification class with an unlimited number of file instances. |
| SegmentingSpecification(int) | Initializes a new instance of the SegmentingSpecification class. |

#### Properties

| Name | Description |
| --- | --- |
| MaxInstances | Gets or sets a value indicating the maximum number of file instances that can be created. A value of -1 indicates that an unlimited number of file instances can be created. |

Parent topic:

NationalInstruments.VeriStand.ClientAPI.Logging

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-singlechanneltrigger-channelpath.html language=enus -->
## TOPIC 00488: ChannelPath

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-singlechanneltrigger-channelpath.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-singlechanneltrigger-channelpath.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets a value indicating the system definition path of the channel to monitor. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic string ChannelPath { get; set; }

### ChannelPath

Gets or sets a value indicating the system definition path of the channel to monitor.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public string ChannelPath { get; set; }

Parent topic:

SingleChannelTrigger Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-singlechanneltrigger-singlechanneltrigger__string.html language=enus -->
## TOPIC 00489: SingleChannelTrigger(string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-singlechanneltrigger-singlechanneltrigger__string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-singlechanneltrigger-singlechanneltrigger__string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the SingleChannelTrigger class. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic SingleChannelTrigger(string channelPath)ParametersNameTypeDescriptionchannelPathstringThe system definition path of the channel to monitor.

### SingleChannelTrigger(string)

Initializes a new instance of the SingleChannelTrigger class.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public SingleChannelTrigger(string channelPath)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| channelPath | string | The system definition path of the channel to monitor. |

Parent topic:

SingleChannelTrigger Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-singlechanneltrigger.html language=enus -->
## TOPIC 00490: SingleChannelTrigger Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-singlechanneltrigger.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-singlechanneltrigger.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies a trigger whose condition is based on a single channel value. Derives fromTriggerSyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic class SingleChannelTrigger : TriggerConstructorsNameDescriptionSingleChannelTrigger(string)Initializes a new instance of the SingleChannel

### SingleChannelTrigger Class

Specifies a trigger whose condition is based on a single channel value.

#### Derives from

- Trigger

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public class SingleChannelTrigger : Trigger

#### Constructors

| Name | Description |
| --- | --- |
| SingleChannelTrigger(string) | Initializes a new instance of the SingleChannelTrigger class. |

#### Properties

| Name | Description |
| --- | --- |
| ChannelPath | Gets or sets a value indicating the system definition path of the channel to monitor. |

Parent topic:

NationalInstruments.VeriStand.ClientAPI.Logging

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-slope.html language=enus -->
## TOPIC 00491: Slope Enumeration

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-slope.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-slope.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies a rising or falling slope. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic enum SlopeMembersNameValueDescriptionRising0Specifies a rising slope. Falling1Specifies a falling slope.

### Slope Enumeration

Specifies a rising or falling slope.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public enum Slope

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Rising | 0 | Specifies a rising slope. |
| Falling | 1 | Specifies a falling slope. |

Parent topic:

NationalInstruments.VeriStand.ClientAPI.Logging

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-tdmschannel-addproperty__string-tdmspropertydatatype-object.html language=enus -->
## TOPIC 00492: AddProperty(string, TdmsPropertyDataType, object)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-tdmschannel-addproperty__string-tdmspropertydatatype-object.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-tdmschannel-addproperty__string-tdmspropertydatatype-object.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds a new TdmsProperty with the specified name, data type, and value to the TdmsChannel. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic TdmsProperty AddProperty(string name, TdmsPropertyDataType dataType, object value)ParametersNameTypeDescriptionnamestringThe name of the pr

### AddProperty(string, TdmsPropertyDataType, object)

Adds a new TdmsProperty with the specified name, data type, and value to the TdmsChannel.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public [TdmsProperty](nationalinstruments-veristand-clientapi-logging-tdmsproperty.html) AddProperty(string name, TdmsPropertyDataType dataType, object value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | The name of the property. |
| dataType | TdmsPropertyDataType | A TdmsPropertyDataType value that specifies the data type of the TDMS property. |
| value | object | The value of the property. |

#### Returns

The newly added TdmsProperty.

Parent topic:

TdmsChannel Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-tdmschannel-addproperty__tdmsproperty.html language=enus -->
## TOPIC 00493: AddProperty(TdmsProperty)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-tdmschannel-addproperty__tdmsproperty.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-tdmschannel-addproperty__tdmsproperty.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds the specified TdmsProperty to the TdmsChannel. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic void AddProperty(TdmsProperty tdmsProperty)ParametersNameTypeDescriptiontdmsPropertyTdmsPropertyThe TdmsProperty to add.

### AddProperty(TdmsProperty)

Adds the specified TdmsProperty to the TdmsChannel.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public void AddProperty(TdmsProperty tdmsProperty)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| tdmsProperty | TdmsProperty | The TdmsProperty to add. |

Parent topic:

TdmsChannel Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-tdmschannel-channelpath.html language=enus -->
## TOPIC 00494: ChannelPath

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-tdmschannel-channelpath.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-tdmschannel-channelpath.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets a value indicating the system definition path of the channel to log. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic string ChannelPath { get; set; }

### ChannelPath

Gets or sets a value indicating the system definition path of the channel to log.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public string ChannelPath { get; set; }

Parent topic:

TdmsChannel Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-tdmschannel-description.html language=enus -->
## TOPIC 00495: Description

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-tdmschannel-description.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-tdmschannel-description.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets a value indicating the description of the TDMS channel. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic string Description { get; set; }

### Description

Gets or sets a value indicating the description of the TDMS channel.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public string Description { get; set; }

Parent topic:

TdmsChannel Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-tdmschannel-getproperty__string.html language=enus -->
## TOPIC 00496: GetProperty(string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-tdmschannel-getproperty__string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-tdmschannel-getproperty__string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the specified TDMS property associated with this TdmsChannel. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic TdmsProperty GetProperty(string name)ParametersNameTypeDescriptionnamestringThe name of the propertyReturnsIf the property exists on the TDMS channel, returns

### GetProperty(string)

Returns the specified TDMS property associated with this TdmsChannel.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public [TdmsProperty](nationalinstruments-veristand-clientapi-logging-tdmsproperty.html) GetProperty(string name)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | The name of the property |

#### Returns

If the property exists on the TDMS channel, returns a TdmsProperty that represents the property specified by name (parameter); otherwise, returns null.

Parent topic:

TdmsChannel Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-tdmschannel-getpropertynames.html language=enus -->
## TOPIC 00497: GetPropertyNames()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-tdmschannel-getpropertynames.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-tdmschannel-getpropertynames.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns an array of property names for the TDMS channel. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic string[] GetPropertyNames()ReturnsAn array of property names for the TDMS channel.

### GetPropertyNames()

Returns an array of property names for the TDMS channel.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public string[] GetPropertyNames()

#### Returns

An array of property names for the TDMS channel.

Parent topic:

TdmsChannel Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-tdmschannel-name.html language=enus -->
## TOPIC 00498: Name

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-tdmschannel-name.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-tdmschannel-name.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets a value indicating the name of the TDMS channel. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic string Name { get; set; }

### Name

Gets or sets a value indicating the name of the TDMS channel.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public string Name { get; set; }

Parent topic:

TdmsChannel Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-tdmschannel-tdmschannel__string-string.html language=enus -->
## TOPIC 00499: TdmsChannel(string, string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-tdmschannel-tdmschannel__string-string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-tdmschannel-tdmschannel__string-string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the TdmsChannel class. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic TdmsChannel(string name, string channelPath)ParametersNameTypeDescriptionnamestringThe name of the TDMS channel.channelPathstringThe system definition path of the channel to lo

### TdmsChannel(string, string)

Initializes a new instance of the TdmsChannel class.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public TdmsChannel(string name, string channelPath)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | The name of the TDMS channel. |
| channelPath | string | The system definition path of the channel to log. |

Parent topic:

TdmsChannel Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-tdmschannel.html language=enus -->
## TOPIC 00500: TdmsChannel Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-tdmschannel.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-tdmschannel.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies a TDMS channel to log. Derives fromNoneSyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic class TdmsChannelConstructorsNameDescriptionTdmsChannel(string, string)Initializes a new instance of the TdmsChannel class. PropertiesNameDescriptionChannelPathGets or sets a value

### TdmsChannel Class

Specifies a TDMS channel to log.

#### Derives from

None

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public class TdmsChannel

#### Constructors

| Name | Description |
| --- | --- |
| TdmsChannel(string, string) | Initializes a new instance of the TdmsChannel class. |

#### Properties

| Name | Description |
| --- | --- |
| ChannelPath | Gets or sets a value indicating the system definition path of the channel to log. |
| Description | Gets or sets a value indicating the description of the TDMS channel. |
| Name | Gets or sets a value indicating the name of the TDMS channel. |

#### Methods

| Name | Description |
| --- | --- |
| AddProperty(TdmsProperty) | Adds the specified TdmsProperty to the TdmsChannel. |
| AddProperty(string, TdmsPropertyDataType, object) | Adds a new TdmsProperty with the specified name, data type, and value to the TdmsChannel. |
| GetProperty(string) | Returns the specified TDMS property associated with this TdmsChannel. |
| GetPropertyNames() | Returns an array of property names for the TDMS channel. |

Parent topic:

NationalInstruments.VeriStand.ClientAPI.Logging
