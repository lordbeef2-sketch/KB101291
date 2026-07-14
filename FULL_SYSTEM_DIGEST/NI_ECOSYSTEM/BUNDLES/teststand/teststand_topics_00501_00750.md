# NI DOCUMENT BUNDLE: teststand

<!--NI_BUNDLE_CHUNK bundle=teststand start=501 end=750 -->
<!--NI_TOPIC bundle=teststand path=labwindows-cvi-data-type-equivalencies-in-tes.html language=enus -->
## TOPIC 00501: LabWindows/CVI Data Type Equivalencies in TestStand

- bundle_id: `teststand`
- source_path: `labwindows-cvi-data-type-equivalencies-in-tes.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/labwindows-cvi-data-type-equivalencies-in-tes.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: TestStand provides number, string, enumeration, Boolean, and object reference built-in data types. TestStand also provides several standard named data types, including Path and Error. You can create container data types to hold any number of other data types. TestStand container data types are analo

### LabWindows/CVI Data Type Equivalencies in TestStand

TestStand provides number, string, enumeration, Boolean, and object reference built-in data types. TestStand also provides several standard named data types, including Path and Error. You can create container data types to hold any number of other data types. TestStand container data types are analogous to C structures in LabWindows/CVI.

LabWindows/CVI includes a greater variety of built-in data types than TestStand does. Appropriate or safe mappings between TestStand data types and LabWindows/CVI data types when calling code modules, are shown in the following table.

| LabWindows/CVI C Data Type | TestStand Data Type |
| --- | --- |
| char, unsigned char, short, unsigned short, long, unsigned long, float, or double | Number TestStand stores all numeric C data types as double-precision, floating-point numbers. TestStand does not set the format for a number property when assigning a value. |
| _int64, long long | Number {Signed 64-bit integer} |
| unsigned __int64, unsigned long long | Number {Unsigned 64-bit integer} |
| size_t | (32-bit TestStand) Number, (64-bit TestStand) Number {Unsigned 64-bit integer} |
| const char*, char[], const wchar_t*, const unsigned short*, wchar_t[], or unsigned short[] | Path, String, or Expression |
| enum | Number or Enumeration |
| IDispatch *pDispatch, IUnknown *pUnknown, or CAObjHandle objHandle | Object reference |
| Array of x | Array of TestStand (x) |
| Pointer to x | Object reference You can store a pointer a LabWindows/CVI code module returns in a TestStand object reference variable. You can then pass a pointer to a subsequent call to a LabWindows/CVI code module. |
| struct | Container |

Note

Parent topic:

LabWindows/CVI Adapter

Related concepts:

- Code Modules

<!--NI_TOPIC bundle=teststand path=labwindows-cvi.html language=enus -->
## TOPIC 00502: LabWindows/CVI

- bundle_id: `teststand`
- source_path: `labwindows-cvi.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/labwindows-cvi.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: TestStand includes a LabWindows™/CVI™ instrument driver, SessionMgr.fp, that provides a complete LabWindows/CVI ActiveX wrapper for the Session Manager server. The functions in the Advanced class of the driver contain the following additional functions to further simplify obtaining instrument API ha

### LabWindows/CVI

TestStand includes a LabWindows™/CVI™ instrument driver, SessionMgr.fp, that provides a complete LabWindows/CVI ActiveX wrapper for the Session Manager server. The functions in the Advanced class of the driver contain the following additional functions to further simplify obtaining instrument API handles in test code:

- SM_GetSession
- SM_GetHandle
- SM_ReleaseSession

The instrument help for the SessionMgr.fp provides an example of how to use these functions in a code module.

Parent topic:

Using Instrument Sessions in a Development Environment

<!--NI_TOPIC bundle=teststand path=launching-a-modal-dialog-labview.html language=enus -->
## TOPIC 00503: Launching a Modal Dialog - LabVIEW

- bundle_id: `teststand`
- source_path: `launching-a-modal-dialog-labview.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/launching-a-modal-dialog-labview.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Purpose This example demonstrates how to use LabVIEW to create a dialog box that is modal to the TestStand main application window. Example File Location <TestStand Public>\Examples\Fundamentals\Launching a Modal Dialog\LabVIEW\Launching a Modal Dialog.seq Highlighted Features LabVIEW Adapter Modal

### Launching a Modal Dialog - LabVIEW

#### Purpose

This example demonstrates how to use LabVIEW to create a dialog box that is modal to the TestStand main application window.

#### Example File
 Location

<TestStand
 Public>\Examples\Fundamentals\Launching a Modal
 Dialog\LabVIEW\Launching a Modal Dialog.seq

#### Highlighted Features

- LabVIEW Adapter
- Modal dialog boxes

#### Major API

None

#### Prerequisites

To run this example, you must have the LabVIEW development system installed.

Note

#### How to Use This Example

This example uses a LabVIEW Action step to call VIs configured to function as modal dialog boxes, just as if the step were calling any other VI.

To review how the VI must be configured, open the dialog.vi located in the <TestStand Public>\Examples\Fundamentals\Launching a Modal Dialog\LabVIEW directory. In the VI, the modal dialog starts with the Start Modal Dialog VI and ends with the End Modal Dialog VI. Each VI requires the sequence context from the calling TestStand sequence.

Review the instructions documented on the block diagram of the example VI to achieve proper functionality.

Parent topic:

Launching a Modal Dialog

Related concepts:

- TestStand Directory Structure
- Programming with the TestStand API in LabVIEW
- Making Dialog Boxes Modal to TestStand
- Sequence Context

<!--NI_TOPIC bundle=teststand path=launching-a-modal-dialog-mfc.html language=enus -->
## TOPIC 00504: Launching a Modal Dialog - MFC

- bundle_id: `teststand`
- source_path: `launching-a-modal-dialog-mfc.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/launching-a-modal-dialog-mfc.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Purpose This example demonstrates how to use C++ and the TestStand API to create a dialog box that is modal to the TestStand main application window. Example File Location <TestStand Public>\Examples\Fundamentals\Launching a Modal Dialog\MFC\Launching a Modal Dialog.seq Highlighted Features Modal di

### Launching a Modal Dialog - MFC

#### Purpose

This example demonstrates how to use C++ and the TestStand API to create a dialog box that is modal to the TestStand main application window.

#### Example File
 Location

<TestStand
 Public>\Examples\Fundamentals\Launching a Modal
 Dialog\MFC\Launching a Modal Dialog.seq

#### Highlighted Features

- Modal dialog boxes
- TestStand API

#### Major API

- Engine.NotifyStartOfModalDialogEx
- Engine.NotifyEndOfModalDialog

#### Prerequisites

C++ compiler

#### How to Use This Example

This example uses a C/C++ DLL Action step to call a function in a C++ DLL to create a modal dialog box.

To review how the function behaves, open ExampleModalDlg.cpp located in the <TestStand Public>\Examples\Fundamentals\Launching a Modal Dialog\MFC directory. The function calls the Engine.NotifyStartOfModalDialogEx method, which instructs the TestStand Engine that the DLL is creating a modal dialog box. After the dialog box is dismissed, the function calls the Engine.NotifyEndOfModalDialog method to end the modal dialog box state.

Parent topic:

Launching a Modal Dialog

Related concepts:

- TestStand Directory Structure
- Making Dialog Boxes Modal to TestStand
- Organizing Test Program Files with LabVIEW-Built Shared Libraries

<!--NI_TOPIC bundle=teststand path=launching-a-modal-dialog-net.html language=enus -->
## TOPIC 00505: Launching a Modal Dialog - .NET

- bundle_id: `teststand`
- source_path: `launching-a-modal-dialog-net.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/launching-a-modal-dialog-net.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Purpose This example demonstrates how to use .NET and the TestStand API to create a dialog box that is modal to the TestStand main application window. Example File Location <TestStand Public>\Examples\Fundamentals\Launching a Modal Dialog\DotNet\Launching a Modal Dialog.seq Highlighted Features Moda

### Launching a Modal Dialog - .NET

#### Purpose

This example demonstrates how to use .NET and the TestStand API to create a dialog box that is modal to the TestStand main application window.

#### Example File
 Location

<TestStand
 Public>\Examples\Fundamentals\Launching a Modal
 Dialog\DotNet\Launching a Modal Dialog.seq

#### Highlighted Features

- Modal dialog boxes
- TestStand API

#### Major API

- Engine.NotifyStartOfModalDialogEx
- Engine.NotifyEndOfModalDialog

#### Prerequisites

None

#### How to Use This Example

This example uses a .NET Action step to call a function in a .NET DLL to create a modal dialog box.

Parent topic:

Launching a Modal Dialog

Related concepts:

- TestStand Directory Structure
- Making Dialog Boxes Modal to TestStand

<!--NI_TOPIC bundle=teststand path=launching-a-modal-dialog.html language=enus -->
## TOPIC 00506: Launching a Modal Dialog

- bundle_id: `teststand`
- source_path: `launching-a-modal-dialog.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/launching-a-modal-dialog.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The <TestStand Public>\Examples\Fundamentals\Launching a Modal Dialog directory contains the following examples.

### Launching a Modal Dialog

The <TestStand
 Public>\Examples\Fundamentals\Launching a Modal Dialog
 directory contains the following examples.

- [Launching a Modal Dialog - LabVIEW](launching-a-modal-dialog-labview.html)
- [Launching a Modal Dialog - MFC](launching-a-modal-dialog-mfc.html)
- [Launching a Modal Dialog - .NET](launching-a-modal-dialog-net.html)

Parent topic:

Examples for Fundamentals

Related concepts:

- TestStand Directory Structure

<!--NI_TOPIC bundle=teststand path=launching-an-mfc-dialog-with-activex-controls.html language=enus -->
## TOPIC 00507: Launching an MFC Dialog with ActiveX Controls

- bundle_id: `teststand`
- source_path: `launching-an-mfc-dialog-with-activex-controls.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/launching-an-mfc-dialog-with-activex-controls.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Purpose This example demonstrates how to launch a Microsoft Foundation Classes (MFC) dialog box that contains an ActiveX control when you call the MFC DLL from TestStand. Example File Location <TestStand Public>\Examples\Fundamentals\Launching an MFC dialog With ActiveX Controls\Launching an MFC dia

### Launching an MFC Dialog with ActiveX Controls

#### Purpose

This example demonstrates how to launch a Microsoft Foundation Classes (MFC) dialog box that contains an ActiveX control when you call the MFC DLL from TestStand.

#### Example File
 Location

<TestStand
 Public>\Examples\Fundamentals\Launching an MFC dialog With ActiveX
 Controls\Launching an MFC dialog With ActiveX
 Controls.seq

#### Highlighted Features

Sequence Call step

#### Major API

N/A

#### Prerequisites

None

#### How to Use This Example

This example shows how to create and properly initialize a thread so it can launch an MFC dialog box that contains ActiveX controls. TestStand must initialize all execution threads for the ActiveX multithreaded concurrency model. MFC requires that any thread that launches a dialog box that contains ActiveX controls must be initialized as apartment-threaded. Therefore, to launch such a dialog box, you must create a temporary worker thread you initialize as apartment-threaded and have the worker launch the dialog box. Meanwhile, the original thread TestStand uses to call the function must wait for the worker thread to exit.

Note

Use Thread Apartment

Parent topic:

Examples for Fundamentals

Related concepts:

- TestStand Directory Structure

<!--NI_TOPIC bundle=teststand path=levels-of-precedence-in-operators.html language=enus -->
## TOPIC 00508: Levels of Precedence in Operators

- bundle_id: `teststand`
- source_path: `levels-of-precedence-in-operators.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/levels-of-precedence-in-operators.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Expression Type Operator Example primary Literal Identifier (expression){element1, element2, ...} 3.14 or Locals.String (Seconds() / 1000){1.0, 2.5, 5.0} postfix property[index]function Locals.Array[25] Len(Locals.String) unary ++, --, +, -, ~, !, NOT ++Locals.Number or -3.14 multiplicative *, /, %,

### Levels of Precedence in Operators

| Expression Type | Operator | Example |
| --- | --- | --- |
| primary | Literal Identifier (expression){element1, element2, ...} | 3.14 or Locals.String (Seconds() / 1000){1.0, 2.5, 5.0} |
| postfix | property[index]function | Locals.Array[25] Len(Locals.String) |
| unary | ++, --, +, -, ~, !, NOT | ++Locals.Number or -3.14 |
| multiplicative | *, /, %, MOD | 10 * Locals.Number |
| additive | +, - | 5 - Locals.Number |
| shift | <<, >> | Locals.Number >> 2 |
| range | .. | Locals.Array[1..3] |
| relational | <, >, <=, >= | Locals.Number <= 0.1 |
| equality | ==, <>, != | Locals.Number == 2.0 |
| bitwise AND | &, AND | Locals.Number & 0xFFFF |
| bitwise exclusive OR | ^, XOR | Locals.Number ^ 0xFFFF |
| bitwise inclusive OR | \|, OR | Locals.Number \| 0x0008 |
| logical AND | && | Locals.Bool && Step.Result.PassFail |
| logical OR | \|\| | Locals.Bool \|\| Step.Result.PassFail |
| conditional | ? : | Step.Result.PassFail ? 5.0 : 6.0 |
| assignment | =, +=, -=, *=, /=, %=, &=, ^=, \|=, <<=, >>= | Locals.Number += 2.0 |
| comma | , | Locals.Number1 = 5.0,Locals.Number2 = 6.0 |

Parent topic:

Expressions

<!--NI_TOPIC bundle=teststand path=license-checking.html language=enus -->
## TOPIC 00509: License Checking

- bundle_id: `teststand`
- source_path: `license-checking.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/license-checking.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The ApplicationMgr.Start method verifies that a license exists to run the application. When no license exists, the ApplicationMgr.Start method returns an error the application displays before exiting. When a license that is not activated or an evaluation license exists, the ApplicationMgr.Start meth

### License Checking

The ApplicationMgr.Start method verifies that a license exists to run the application. When no license exists, the ApplicationMgr.Start method returns an error the application displays before exiting. When a license that is not activated or an evaluation license exists, the ApplicationMgr.Start method prompts users to activate a license.

When the ApplicationMgr.IsEditor property is True, the ApplicationMgr.Start method requires a license that permits editing. When you call the ApplicationMgr.Start method when the ApplicationMgr.IsEditor property is False and later set the ApplicationMgr.IsEditor property to True, the ApplicationMgr.IsEditor property returns an error when it cannot obtain a license that permits editing.

Note

ApplicationMgr.Start

Parent topic:

Getting Started with User Interface Development

<!--NI_TOPIC bundle=teststand path=limitations-of-patch-deployments.html language=enus -->
## TOPIC 00510: Limitations of Patch Deployments

- bundle_id: `teststand`
- source_path: `limitations-of-patch-deployments.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/limitations-of-patch-deployments.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Limitations for MSI-based installer patches You can use installers for patch deployments to create smaller updates for a deployment, but patch installers cannot make all the changes that installers for full deployments can complete. Installers you build using the TestStand Deployment Utility for ful

### Limitations of Patch Deployments

#### Limitations for MSI-based installer
 patches

You can use installers for patch deployments to create smaller
 updates for a deployment, but patch installers cannot make all the changes that
 installers for full deployments can complete.

Installers you build using the
 TestStand Deployment Utility for full and patch deployments use Microsoft Windows
 Installer technology database files to indicate a Major Upgrade or a Minor Upgrade.
 Installers for full deployments perform Major Upgrades, which uninstall the previous
 installer for the full deployment and install the newer version of the installer for
 the full deployment. Installers for patch deployments perform only Minor Upgrades,
 which modify an existing installation without uninstalling the previous
 installation, leading to the following limitations:

- You cannot uninstall the files for a patch deployment without uninstalling the
 files for the full deployment.
- Installers for patch deployments cannot delete files. Create a new full
 deployment to upgrade the previous full deployment to remove files in a deployed
 test system.
- Installers for patch deployments cannot move files from one directory to
 another. You can change the destination of a file in a patch deployment, but the
 installer for the patch deployment leaves the file in the original location of
 the full deployment and installs a file with the same name in the new
 destination directory. Because the file remains in the original location,
 TestStand might find the original file in search paths before finding the new
 version of the file in a different location. If the file is a VI, LabVIEW might
 cross-link to the file during a mass compile.

Note

Additionally, the
 deployment utility does not support the following installer features:

- Select Windows Installer technology patching options, such as the following:
  - Windows Installer patch ( .msp ) file
  - Small Updates
- Creating new program item entries for patch deployments in the standard
 Microsoft Windows Control Panel facility for adding and removing programs Note You can,
 however, use the Installation Name option on the
 Installer Options tab of the deployment utility and the
 Version option in the Advanced Installer Options
 dialog box to update the program item entry text for the full installer upon
 which the patch installer depends.

Refer to Microsoft documentation for more information about these installer
 features.

#### Limitations for package-based installer patches

The following limitations exist for package-based package deployments:

- Patching is not supported for the single package build output. Patching only applies to the driver and component packages included in a repository or package distribution.
- The package company and product fields cannot be modified in a patch distribution since these fields are used to generate the package name. All other package attributes can be modified for a patch distribution.
- Package based deployments do not support updating individual files through a patch deployment. When installing a patch deployment, the package containing deployment files replaces the package installed on the test system.
- Packages for patch deployments cannot move files from one directory to another. You can change the destination of a file in a patch deployment, but the package for the patch deployment leaves the file in the original location of the full deployment and installs a file with the same name in the new destination directory. Because the file remains in the original location, TestStand might find the original file in search paths before finding the new version of the file in a different location. If the file is a VI, LabVIEW might cross-link to the file during a mass compile.

Parent topic:

Patching Deployments

Related concepts:

- Relationship of NI MSI-based Installer Architecture and Microsoft Windows Installer Technology
- Uninstalling a TestStand Deployment

<!--NI_TOPIC bundle=teststand path=limitations-with-sharing-instrument-sessions.html language=enus -->
## TOPIC 00511: Limitations with Sharing Instrument Sessions Among Processes

- bundle_id: `teststand`
- source_path: `limitations-with-sharing-instrument-sessions.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/limitations-with-sharing-instrument-sessions.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Any software component in any thread of a process can use Session Manager to discover and access instrument sessions that other components in the same process use. Instance handles that an instrument session creates are C-based API handles. Attempting to share C-based VISA, VXIplug&play, IVI C, or N

### Limitations with Sharing Instrument Sessions Among Processes

Any software component in any thread of a process can use Session Manager to discover and access instrument sessions that other components in the same process use. Instance handles that an instrument session creates are C-based API handles. Attempting to share C-based VISA, VXIplug&play, IVI C, or NI Switch Executive instance handles across processes results in an error. For example, you cannot use an IVI C-based handle that a step in the TestStand process creates in a VI code module that executes using the LabVIEW development system process.

*Custom::MyCustomName

Note

Parent topic:

Session Manager

<!--NI_TOPIC bundle=teststand path=list-connections.html language=enus -->
## TOPIC 00512: List Connections

- bundle_id: `teststand`
- source_path: `list-connections.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/list-connections.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can connect a ComboBox control, a ListBox control, or a ListBar page to a list a manager control provides, as shown in the following table. List Manager Control Adapters Application Manager Sequence files SequenceFileView Manager Sequences SequenceFileView Manager Step groups SequenceFileView Ma

### List Connections

You can connect a ComboBox control, a ListBox control, or a ListBar page to a list a manager control provides, as shown in the following table.

| List | Manager Control |
| --- | --- |
| Adapters | Application Manager |
| Sequence files | SequenceFileView Manager |
| Sequences | SequenceFileView Manager |
| Step groups | SequenceFileView Manager |
| Executions | ExecutionView Manager |
| Threads | ExecutionView Manager |
| Stack frames | ExecutionView Manager |

A manager control designates one item in each list as the selected item. A visible control you connect to a list displays the list and indicates the selected item. The visible control also allows users to change the selection unless the application state or control configuration prohibits changing the selection. When users change the selection, other controls that display the list or the selected list item update to display the new selection. For example, you can connect a SequenceFileView Manager control to a SequenceView control and connect the sequence file list to a combo box. When users change the file selection in the combo box, the SequenceView control updates to show the steps in the newly selected sequence file.

Call the following methods to connect a list to a ComboBox control, a ListBox control, or a ListBar page:

- ApplicationMgr.ConnectAdapterList
- SequenceFileViewMgr.ConnectSequenceFileList
- SequenceFileViewMgr.ConnectSequenceList
- SequenceFileViewMgr.ConnectStepGroupList
- ExecutionViewMgr.ConnectExecutionList
- ExecutionViewMgr.ConnectThreadList
- ExecutionViewMgr.ConnectCallStack

Parent topic:

Connecting Manager Controls to Visible Controls

Related concepts:

- Manager Controls
- Application Manager
- SequenceFileView Manager
- ExecutionView Manager

<!--NI_TOPIC bundle=teststand path=list-of-engine-callbacks.html language=enus -->
## TOPIC 00513: List of Engine Callbacks

- bundle_id: `teststand`
- source_path: `list-of-engine-callbacks.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/list-of-engine-callbacks.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following table lists the Engine callbacks TestStand defines, indicates where you must define the callback, and specifies when the engine calls the callback. Engine Callback Where You Define the Callback When the Engine Calls the Callback SequenceFilePreStep Any sequence file Before the TestStan

### List of Engine Callbacks

The following table lists the Engine callbacks TestStand defines, indicates where you must define the callback, and specifies when the engine calls the callback.

| Engine Callback | Where You Define the Callback | When the Engine Calls the Callback |
| --- | --- | --- |
| SequenceFilePreStep | Any sequence file | Before the TestStand Engine executes each step in the sequence file. |
| SequenceFilePostStep | Any sequence file | After the engine executes each step in the sequence file. The engine does not call this callback when a step errors. |
| SequenceFilePreInteractive | Any sequence file | Before the engine begins an interactive execution of steps in the sequence file. |
| SequenceFilePostInteractive | Any sequence file | After the engine completes an interactive execution of steps in the sequence file. |
| SequenceFileLoad | Any sequence file | When the engine loads the sequence file into memory. |
| SequenceFileUnload | Any sequence file | When the engine unloads the sequence file from memory. |
| SequenceFilePostResultListEntry | Any sequence file | After the engine fills out the step result for a step in the sequence file. |
| SequenceFilePostResults | Any sequence file | After the engine collects a step result in the sequence file and the number of collected results or the time since collected results were last processed exceeds a threshold. |
| SequenceFilePostStepRuntimeError | Any sequence file | After a step in the sequence file generates a run-time error. |
| SequenceFilePostStepFailure | Any sequence file | After a step in the sequence fails. |
| ProcessModelPreStep | Process model file | Before the engine executes each step in any client sequence file the process model calls and each step in any resulting subsequence calls. |
| ProcessModelPostStep | Process model file | After the engine executes each step in any client sequence file the process model calls and each step in any resulting subsequence calls. The engine does not call this callback when a step errors. |
| ProcessModelPreInteractive | Process model file | Before the engine begins an interactive execution of steps in a client sequence file and steps in any resulting subsequence calls. |
| ProcessModelPostInteractive | Process model file | After the engine completes an interactive execution of steps in a client sequence file and steps in any resulting subsequence calls. |
| ProcessModelPostResultListEntry | Process model file | After the engine fills out the step result for a step in any client sequence file the process model calls or in any resulting subsequence calls. |
| ProcessModelPostResults | Process model file | After the engine collects a step result for a step in any client sequence file the process model calls or in any resulting subsequence calls and the number of collected results or the time since collected results were last processed exceeds a threshold. |
| ProcessModelPostStepRuntimeError | Process model file | After a step generates a run-time error when the step is in a client sequence file the process model calls or in any resulting subsequence calls. |
| ProcessModelPostStepFailure | Process model file | After a step fails when the step is in a client sequence file the process model calls or in any resulting subsequence calls. |
| StationPreStep | StationCallbacks.seq | Before the engine executes each step in any sequence file. |
| StationPostStep | StationCallbacks.seq | After the engine executes each step in any sequence file. The engine does not call this callback when a step errors. |
| StationPreInteractive | StationCallbacks.seq | Before the engine begins any interactive execution. |
| StationPostInteractive | StationCallbacks.seq | After the engine completes any interactive execution. |
| StationPostResultListEntry | StationCallbacks.seq | After the engine fills out the step result for a step in any sequence file. |
| StationPostResults | StationCallbacks.seq | After the engine collects a step result for a step in any sequence file and the number of collected results or the time since collected results were last processed exceeds a threshold. |
| StationPostStepRuntimeError | StationCallbacks.seq | After any step generates a run-time error. |
| StationPostStepFailure | StationCallbacks.seq | After any step fails. |

Note

Parent topic:

Modifying Engine Callbacks

Related concepts:

- Engine Callbacks
- Caveats for Using Engine Callbacks
- Overriding PreBatch and PostBatch Model Callbacks
- Overriding PreUUT and PostUUT Batch Model Callbacks
- Overriding PreUUT and PostUUT Parallel Model Callbacks

<!--NI_TOPIC bundle=teststand path=loading-and-running-sequences.html language=enus -->
## TOPIC 00514: Loading and Running Sequences

- bundle_id: `teststand`
- source_path: `loading-and-running-sequences.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/loading-and-running-sequences.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The TestStand Sequence Editor includes menus, toolbars, windows, and panes you use to load workspace files and edit and run sequence files. Click Help»Help Topic to launch the NI TestStand Help for specific information about the active window, tab, or pane in the sequence editor. Completed solution

### Loading and Running Sequences

The TestStand Sequence Editor includes menus, toolbars, windows, and panes you use to load workspace files and edit and run sequence files. Click Help»Help Topic to launch the NI TestStand Help for specific information about the active window, tab, or pane in the sequence editor.

Note

<TestStand Public>\Tutorial\Solution

#### Starting TestStand

Start»NI
 TestStand

Note

administrator

#### Menu Bar

By default, the menu bar contains the File, Edit, View, Execute, Debug, Configure, Source Control, Tools, Window, and Help menus. The menus are fully customizable. You can create menus with any sequence editor commands you want. Browse the menus in the sequence editor to familiarize yourself with the contents of each menu.

#### Toolbars

By default, the sequence editor contains a toolbar with shortcuts to commonly used selections from the menu bar. The toolbar is fully customizable. You can create toolbars with buttons for any environment commands you want.

#### Windows and Panes

The sequence editor contains tabbed windows and panes you can float, dock, resize, and hide. You can customize the pane and tab layout to optimize development and debugging tasks. You can reset the user interface configuration state of the panes in the sequence editor by selecting View»Reset UI Configuration, which resets to a default configuration all modifications previously made to menus, toolbars, and the docking state of panes.

Note

Configure»Sequence Editor Options

Load Selected

OK

The Insertion Palette pane in the TestStand Sequence Editor displays items you can insert into a sequence file. The pane contains a Step Types list and a Templates list. The Step Types list displays the step type menu, and the Templates list displays user-defined template sequences, steps, and variables.

#### Status Bar

The status bar
 displays the following information for the sequence editor:

- User name of the current user.
- The environment in which the application is running.
- Name of the process model file the current sequence uses. You can double-click
 in this area to open that process model file.
- Number of steps you have selected.
- Total number of steps in the active sequence.
- File path of the active report after execution.

#### Organizing a TestStand System with Workspace and Project Files

Create a workspace to organize and access development files. Use workspaces early in development so you can easily keep track of files while you are developing. A workspace file (.tsw) contains references to any number of TestStand project files. A project file (.tpj) contains references to any number of other files of any type.

Use project files to organize related files and directories of files in the test system. You can insert any number of files into a project. For example, you can use a project file to organize a sequence file, code module source files, and other supporting files.

A workspace file opens on the Workspace pane, which displays the content of a workspace file. To open any file from the Workspace pane, double-click the file. To organize the files, use the options in the Edit menu to cut, copy, paste, and delete files in projects or project files in the workspace. You can also drag and drop files on the Workspace pane.

You can open only one workspace file at a time. If you have a workspace file open and you try to open or create another, TestStand prompts you to save the workspace file before opening or creating another file.

You must use workspace files to use the source code control (SCC) system features in TestStand. You can also use workspace files to deploy test systems with the TestStand Deployment Utility.

#### Loading a Workspace File

Complete the following steps to load and view a workspace file.

1. Select File»Open File and navigate to the <TestStand Public>\Tutorial directory.
2. Select Tutorial.tsw and click Open .
3. Expand the Using TestStand project, which contains all the sequence files used in the tutorials in this tutorial, including the Solution directory.

You can leave the workspace file open on the Workspace pane so you can directly open the sequence files for the tutorials in this tutorial, or you can close the Workspace pane and use the options in the File menu to open the sequence files. If you want to close the Workspace pane, select File»Close Workspace File and click No if TestStand prompts you to save the changes.

#### Creating Test Sequences and Sequence Files

A sequence consists of a series of steps. A step can perform many actions, such as initializing an instrument, performing a complex test, or controlling the flow of execution in a sequence.

A sequence file can contain one or more sequences. Sequence files can also contain global variables, which all sequences in the sequence file can access.The sequence editor color-codes sequences by type, such as Execution entry points, Configuration entry points, process model callback sequences, subsequences, and engine callbacks.

The Setup, Main, and Cleanup groups of the Steps pane display a list of the steps in the step group.TestStand executes the steps in the Setup step group first, the Main step group second, and the Cleanup step group last. The Setup step group typically contains steps that initialize instruments, fixtures, or a UUT. The Main step group typically contains the bulk of the steps in a sequence, including the steps that test the UUT. The Cleanup step group typically contains steps that power down or restore the initial state of instruments, fixtures, and the UUT.

A sequence can have any number of parameters and local variables. Use parameters to pass data to a sequence when you call the sequence as a subsequence. Use local variables for storing data relevant to the execution of the sequence, storing any other data needed only in the current sequence, maintaining counts, or holding intermediate values.

In the sequence editor, the Variables pane displays all the variables and properties the selected sequence has access to at run time. When you execute a sequence, the Variables pane displays the sequence context for the sequence currently selected on the Call Stack pane. The sequence context contains all the variables and properties accessible in the current execution. Use the Variables pane to examine and modify the values of these variables and properties when an execution is suspended.

The sequence editor opens each sequence file in a separate Sequence File window, which includes the Sequences pane, the Steps pane, and the Variables pane. The Sequences pane lists the name, comment, and requirements values for all sequences in the sequence file. Use the Sequences pane to select the active sequence to display on the Steps pane, to insert new sequences, and to delete existing sequences from a sequence file.

#### Loading a Sequence File

Complete the following steps to load and view a sequence file.

1. Select File»Open File and navigate to the <TestStand Public>\Tutorial directory.
2. Select Computer.seq and click Open . The Computer.seq sequence file is a simulated test of a computer in which you can designate various hardware components to fail. The sequence runs tests implemented as functions in a DLL. TestStand includes examples of DLLs written in LabVIEW, .NET, and LabWindows/CVI. Note If you left the Tutorial.tsw workspace file open from the Loading a Workspace File section of this tutorial, you can open Computer.seq from the Workspace pane by double-clicking Computer.seq in the list of files.
3. Select MainSequence on the Sequences pane.
4. Browse the contents of each pane in the Sequence File window. Ensure that the Sequences pane and the Steps pane are visible when you finish.

#### Executing a Sequence

You can execute a sequence directly or execute a sequence using a process model Execution entry point. The process model entry point sequence contains a series of steps that specify the high-level flow of an execution.

The TestStand Sequence Editor launches a separate Execution window for each execution you start using the Execute menu. Use the Execution window to view, or trace, steps as they execute, to monitor the values of variables and properties, and to examine test reports when the execution completes.

In Trace Mode, the Execution window shows the steps in the currently executing sequence and indicates the currently executing step. If the execution suspends, the Execution window shows the next step to execute and provides debugging options.

Before the execution begins, by default, the TestStand Sequence Analyzer analyzes the active sequence file and detects the most common situations that can cause run-time failures. The sequence analyzer prompts you to resolve the reported errors before you execute the sequence file. Carefully review any errors the sequence analyzer returns to prevent run-time failures. If you want to disable the sequence analyzer, click Debug»Sequence Analyzer»Toggle Analyze File Before Executing.

#### Executing a Sequence Directly

Complete the following steps to run MainSequence in the Computer.seq sequence file directly.

1. Select Configure»Station Options to launch the Station Options dialog box. The Execution tab contains options for configuring how an execution behaves. By default, the Enable Tracing option is enabled to specify that the sequence editor displays the progress of an execution with a yellow arrow icon that appears to the left of the currently executing step. This icon is called the execution pointer. The Execution tab also contains a Speed slider control that specifies the tracing speed of the execution. Use this option to slow down the tracing speed so you can observe each step as it executes. By default, the tracing speed is set to fast.
2. Adjust the Speed slider control to slow. Click OK to close the Station Options dialog box.
3. Select Execute»Run MainSequence . The sequence editor opens an Execution window to show the sequence as it executes. The first step in the Setup step group of MainSequence launches the Test Simulator dialog box. The Test Simulator dialog box prompts you to designate the computer component, if any, you want to fail during the execution.
4. Enable the RAM test option.
5. Click Done .
6. Observe the Execution window as it traces through the steps TestStand runs. After the execution completes, the Execution window dims, and the Status column of the RAM test contains the value Failed . Note If the tracing speed is too slow or fast, adjust the Speed slider control on the Execution tab of the Station Options dialog box.
7. Right-click the Execution window tab and select Close from the context menu to close the Execution window.

#### Executing a Sequence Using the Sequential Process Model

In addition to executing sequences directly, you can execute sequences using an Execution entry point, which is a sequence in a process model file that invokes a test sequence file, typically by calling the MainSequence callback in the client sequence file. Executing an Execution entry point performs a series of operations before and after calling MainSequence of the sequence file. Common operations of the process model include identifying the UUT, notifying the operator of pass/fail status, logging results, and generating reports.

The Sequential process model includes the following Execution entry points:

- Test UUTs Execution Entry Point —The Test UUTs Execution entry point initiates a loop that repeatedly identifies and tests UUTs.
- Single Pass Execution Entry Point —The Single Pass Execution entry point tests a single UUT without identifying it. Use the Single Pass Execution entry point when you want to debug tests or determine whether the sequence execution proceeds as you intended.

Complete the following steps to run MainSequence in the Computer.seq sequence file using the Test UUTs Execution entry point of the Sequential model.

1. Launch the Station Options dialog box.
2. Click the Model tab, verify that SequentialModel.seq is selected from the Station Model ring control to select the Sequential model as the default process model, and click OK .
3. Select Execute»Test UUTs . Before executing the steps in MainSequence , the process model sequence launches a UUT Information dialog box that prompts you for a serial number.
4. Enter any serial number and click OK .
5. Use the options in the Test Simulator dialog box to select any test other than the Video or CPU tests to fail. You can also allow all the tests of the UUT to pass.
6. Click Done . Observe the Execution window as the sequence executes. After completing the steps in MainSequence , the process model displays a banner that indicates the result of the UUT.
7. Click OK to close the UUT Result banner. TestStand generates a report, but does not display the report until you finish testing all the UUTs. TestStand launches the UUT Information dialog box again.
8. Repeat steps 4 through 7 using several different serial numbers.
9. Click Stop in the UUT Information dialog box to stop the loop and complete the execution. After the execution completes, TestStand displays the report on the Report pane of the Execution window for all the tested UUTs.
10. Review the test report, which includes the results for each UUT, and select Window»Close All Windows to close all the windows in the sequence editor.

#### Executing a Sequence Using the Batch
 Process Model

Use the Batch model to control a set of test sockets that
 test multiple UUTs as a group. For example, if you have a set of circuit boards
 attached to a common carrier, use the Batch model to ensure that you start and
 finish testing all boards at the same time. With the synchronization features of the
 Batch model, you can direct a step that applies to the batch as a whole to run only
 once per batch instead of once for each UUT. You can also specify whether certain
 steps or groups of steps cannot run on more than one UUT at a time or whether
 certain steps must run on all UUTs at the same time. The Batch model generates batch
 reports that summarize the test results for the UUTs in the batch.

Complete
 the following steps to run the BatchUUT.seq sequence file using the
 Test UUTs Execution entry point of the Batch model.

1. Open <TestStand Public>\Tutorial\BatchUUT.seq and examine
 the steps and comments in the sequence file to familiarize yourself with the
 functionality of the sequence. Note You do not need to change
 the default process model in the sequence editor for this tutorial. The
 BatchUUT.seq sequence file always uses the Batch model,
 regardless of the default process model of the sequence editor. Use the
 Advanced tab of the Sequence File Properties dialog box to specify the
 process model a sequence file uses.
2. Select Configure»Model Options to launch the Model
 Options dialog box.
3. In the Multiple UUT Settings section, change Number of Test
 Sockets to 2 and enable the Tile
 Execution Windows option. The Number of Test Sockets control
 specifies the number of UUTs to test in the batch.
4. In the Batch Settings section, select Don't Synchronize 
 from the Default Batch Synchronization ring control and click
 OK .
5. Select Execute»Test UUTs . Before executing the steps in
 MainSequence , the process model sequence launches the UUT
 Information dialog box for the Batch model, which prompts you for a batch serial
 number and UUT serial numbers for each test socket. You can also disable test
 sockets in the UUT Information dialog box.
6. Enter any batch serial number and UUT serial numbers. Click
 Go . Review the information in the Batch Model Example
 dialog box, then click OK . TestStand launches several
 different front panels to indicate the progress of the executions. Click
 OK to continue. After completing the steps in
 MainSequence , the process model launches the Batch Results
 dialog box, which displays a banner that indicates the result of the UUTs. You
 can view the batch report and individual UUT reports or start the next batch.
7. Click the View Batch Report button. From the pop-up list,
 you can select Entire File to show all tested batches or Current Only to show
 the most recently tested batch.
8. Select Current Only from the pop-up list. TestStand
 launches the default application associated with the file extension of the
 report, such as Internet Explorer for Automatic Test Markup Language (ATML),
 XML, and HTML reports and Microsoft Notepad for text reports. Note Enable Internet Explorer to
 run scripts if the browser launches a prompt. To use another application as
 an external report viewer, select Configure»External
 Viewers and follow the instructions in the Configure
 External Viewers dialog box. Refer to the Using External Report
 Viewers section of Customizing Reports, for
 more information about using external viewers.
9. Close Internet Explorer and click Next Batch in the Batch
 Results dialog box.
10. Repeat steps 6 through 9 for several different batches.
11. Click Stop in the UUT Information dialog box to complete
 the execution. After the execution completes, TestStand displays test reports on
 the Report pane of the Execution window for all batches and UUTs.
12. Examine the reports that include results for each batch and UUT.
13. Close all the windows in the sequence editor.

Parent topic:

Getting Started with TestStand

<!--NI_TOPIC bundle=teststand path=loading-and-unloading-python-modules.html language=enus -->
## TOPIC 00515: Loading and Unloading Python Modules

- bundle_id: `teststand`
- source_path: `loading-and-unloading-python-modules.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/loading-and-unloading-python-modules.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Load Option setting of the step will execute when Python module is configured to use the Global interpreter session created per instance of TestStand. Python modules are loaded dynamically for all other Global interpreter session options. The Unload Option setting for the step using Python modul

### Loading and Unloading Python Modules

The Load Option setting of the step will execute when Python module is configured to use the Global interpreter session created per instance of TestStand. Python modules are loaded dynamically for all other Global interpreter session options.

The Unload Option setting for the step using Python modules cannot be used. Once the Python modules are loaded in a Global interpreter session, they cannot be unloaded.

Parent topic:

Python Adapter

<!--NI_TOPIC bundle=teststand path=loading-subordinate-dlls.html language=enus -->
## TOPIC 00516: Loading Subordinate DLLs

- bundle_id: `teststand`
- source_path: `loading-subordinate-dlls.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/loading-subordinate-dlls.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: TestStand directly loads and runs the DLLs you specify on the C/C++ DLL Module tab for the C/C++ DLL Adapter or the LabWindows/CVI Module tab for the LabWindows/CVI Adapter. Because code modules most likely call subsidiary DLLs, such as instrument drivers, you must ensure that the operating system c

### Loading Subordinate DLLs

TestStand directly loads and runs the DLLs you specify on the C/C++ DLL Module tab for the C/C++ DLL Adapter or the LabWindows/CVI Module tab for the LabWindows/CVI Adapter. Because code modules most likely call subsidiary DLLs, such as instrument drivers, you must ensure that the operating system can find and load any DLL you specify.

The adapter attempts to load subordinate DLLs using the following search directory precedence:

1. The directory that contains the DLL the adapter calls directly
2. The Windows\System32 and Windows\System directories
3. The Windows directory
4. The current working directory of the application
5. The directories listed in the PATH environment variable

For compatibility purposes, when the adapter fails to load a DLL, the adapter temporarily sets the current working directory to the directory of the DLL and attempts to load subordinate DLLs using the following deprecated search directory precedence:

1. The directory that contains the application that loaded the adapter
2. The Windows\System32 and Windows\System directories
3. The Windows directory
4. The current working directory of the application, which the adapter sets to the directory that contains the DLL it calls directly
5. The directories listed in the PATH environment variable

Note

Use the TestStand Deployment Utility to deploy code modules and subsidiary DLLs for use with TestStand.

Parent topic:

Calling DLLs from TestStand

Related concepts:

- Organizing Test Program Files with LabVIEW-Built Shared Libraries
- Programming with the TestStand API in LabWindows/CVI
- Code Modules
- Deploying TestStand Systems

<!--NI_TOPIC bundle=teststand path=localize-custom-rules-tsa.html language=enus -->
## TOPIC 00517: Localizing Custom Rules in the TestStand Sequence Analyzer

- bundle_id: `teststand`
- source_path: `localize-custom-rules-tsa.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/localize-custom-rules-tsa.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `task`
- source_description: Complete the following steps to localize custom rules you create. Create a string resource file (.ini file) in the <TestStand Public>\Components\Language directory. To localize a custom rule category, add an ANALYZER_RULE_CATEGORIES section to the file and create tags and values for the custom rule

### Localizing Custom Rules in the TestStand
 Sequence Analyzer

Complete the following steps to localize
 custom rules you create.

1. Create a string resource
 file
 (.ini file) in the
 <TestStand Public>\Components\Language
 directory.
2. To localize a custom rule category, add an
 ANALYZER_RULE_CATEGORIES section to the file and create
 tags and values for the custom rule category.
3. To localize rule strings, add a new section to the file and create tags and
 values for the custom rule name, description, and enumeration item names.
4. In the Resource String Category control on the Advanced tab of the Edit Rule
 dialog box, enter the name of the custom rule category section you created for
 the tags of the custom rule name, description, and enumeration item names.

Parent topic:

TestStand Sequence Analyzer

Related concepts:

- Creating String Resource Files
- Search Directories

Related information:

- Edit Rule Dialog Box

<!--NI_TOPIC bundle=teststand path=localizing-user-interfaces.html language=enus -->
## TOPIC 00518: Localizing User Interfaces

- bundle_id: `teststand`
- source_path: `localizing-user-interfaces.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/localizing-user-interfaces.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The StationOptions.Language property specifies the current language. Localized TestStand applications use the Engine.GetResourceString method to obtain text in the current system language from language resource files. Call the ApplicationMgr.LocalizeAllControls method to localize all the user-visibl

### Localizing User Interfaces

The StationOptions.Language property specifies the current language. Localized TestStand applications use the Engine.GetResourceString method to obtain text in the current system language from language resource files.

Call the ApplicationMgr.LocalizeAllControls method to localize all the user-visible TestStand User Interface (UI) Control strings you configure at design time. Using the ApplicationMgr.LocalizeAllControls method reduces the number of strings you must explicitly localize using the Engine.GetResourceString method by localizing items such as list column headers in the SequenceView control, text in the StatusBar pane, captions in the Button control, and captions in the ListBar page.

Buttons and menu items you connect to commands automatically localize caption text.

The ApplicationMgr.LocalizeAllControls method operates only on TestStand UI Controls. For other controls and user interface elements, the application must set each item of localized text. The following table lists the TestStand Utility (TSUtil) library functions you can use to localize non-TestStand controls and menu items.

| ADE | TSUtil Library Localization Function |
| --- | --- |
| LabVIEW | TestStand - Get Resource String.vi TestStand - Localize Front Panel.vi TestStand - Localize Menu.vi Refer to the Full UI - Localize Operator Interface and to the Full UI - About Box example user interface VIs for examples of localizing user interfaces. |
| LabWindows/CVI | TS_LoadPanelResourceStrings TS_LoadMenuBarResourceStrings TS_SetAttrFromResourceString TS_GetResourceString TSUI_ApplicationMgrLocalizeAllControls Refer to the <TestStand Public>\\UserInterfaces\\Full-Featured\\CVI\\Source Code\\TestExec.c source file for an example of localizing user interface panels. |
| .NET | Localizer.LocalizeForm Localizer.LocalizeMenu |
| C++ (MFC) | Localizer.LocalizeWindow Localizer.LocalizeMenu Localizer.LocalizeString |

Parent topic:

User Interface Development Best Practices

Related concepts:

- Creating String Resource Files
- TestStand UI Controls
- Command Connections
- TestStand Utility Functions Library
- Example User Interfaces
- TestStand Directory Structure

<!--NI_TOPIC bundle=teststand path=locating-the-correct-code-module-in-32-bit-te.html language=enus -->
## TOPIC 00519: Locating the Correct Code Module in 32-bit TestStand and 64-bit TestStand

- bundle_id: `teststand`
- source_path: `locating-the-correct-code-module-in-32-bit-te.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/locating-the-correct-code-module-in-32-bit-te.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: If a single code module cannot simultaneously support 32-bit applications and 64-bit applications, you can use TestStand search directories or the $(Platform) path macro to associate a step or sequence with the 32-bit version and the 64-bit version of a code module.

### Locating the Correct Code Module in 32-bit TestStand and 64-bit TestStand

If a single code module cannot simultaneously support 32-bit applications and 64-bit applications, you can use TestStand search directories or the $(Platform) path macro to associate a step or sequence with the 32-bit version and the 64-bit version of a code module.

Parent topic:

64-bit TestStand and Migrating from 32-bit TestStand

Related concepts:

- Using TestStand Search Directories to Locate the Correct Code Module in 32-bit TestStand and 64-bit TestStand
- Using the $(Platform) Path Macro to Locate the Correct Code Module in 32-bit TestStand and 64-bit TestStand

<!--NI_TOPIC bundle=teststand path=locating-the-correct-dll-in-32-bit-teststand.html language=enus -->
## TOPIC 00520: Locating the Correct DLL in 32-bit TestStand and 64-bit TestStand

- bundle_id: `teststand`
- source_path: `locating-the-correct-dll-in-32-bit-teststand.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/locating-the-correct-dll-in-32-bit-teststand.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: TestStand executes C/C++ DLL code modules in-process. Similarly, TestStand executes LabWindows/CVI code modules in-process when you use the LabWindows/CVI Run-Time Engine. Although TestStand supports executing LabWindows/CVI code modules out-of-process using the LabWindows/CVI Development Environmen

### Locating the Correct DLL in 32-bit TestStand and 64-bit TestStand

TestStand executes C/C++ DLL code modules in-process. Similarly, TestStand executes LabWindows/CVI code modules in-process when you use the LabWindows/CVI Run-Time Engine. Although TestStand supports executing LabWindows/CVI code modules out-of-process using the LabWindows/CVI Development Environment, TestStand requires the bitness of the external code module to match the bitness of TestStand. Therefore, you must use separate 32-bit versions and 64-bit versions of DLL code modules for the C/C++ DLL Adapter or the LabWindows/CVI Adapter to simultaneously support 32-bit architectures and 64-bit architectures.

TestStand automatically locates the correct versions of C/C++ and LabWindows/CVI code modules in non-shared search directories, such as the <TestStand Public> directory. If the prototypes of the functions that the 32-bit version and 64-bit version of the DLLs export are identical and each version resides under the correct search directory, TestStand sequences and step types that depend on the code modules execute in 32-bit TestStand or in 64-bit TestStand without modification. (For prototypes that change, see Bitness Conditional Code for DLLs with Different 32-bit Interfaces and 64-bit Interfaces.)

If you migrate code modules you specify with paths relative to the sequence file or another location that 32-bit TestStand and 64-bit TestStand share and you no longer intend to support the 32-bit architecture, you can replace all DLL code modules with 64-bit versions in-place. If the prototypes of the functions that the 32-bit version and the 64-bit version of the DLLs export are identical, TestStand sequences that depend on the code modules execute in 64-bit TestStand but no longer execute in 32-bit TestStand.

If you migrate code modules you specify with paths relative to the sequence file or another location that 32-bit TestStand and 64-bit TestStand share and you need to simultaneously support the 32-bit architecture and the 64-bit architecture, complete the following steps to associate the bitness-specific version of the DLL with a step.

1. Create a win32 subdirectory and an x64 subdirectory in the
 directory that contains the DLL.
2. Move the 32-bit version of the DLL to the win32 subdirectory.
3. Place the 64-bit version of the DLL in the x64 subdirectory.
4. Update the module path to $(Platform)\filename.dll in the code module specification. 32-bit TestStand converts the path to win32\filename.dll , and 64-bit TestStand converts the path to x64\filename.dll .

Regardless of whether you need to simultaneously support 32-bit TestStand and 64-bit TestStand,
 NI recommends using the
 $(Platform) path macro and
 platform subdirectories for all C/C++ and
 LabWindows/CVI code modules you call that reside
 in directories that 32-bit TestStand and 64-bit
 TestStand share to simplify future migration.

Parent topic:

C/C++ DLL and LabWindows/CVI DLL Support for 64-bit TestStand

Related concepts:

- Using TestStand Search Directories to Locate the Correct Code Module in 32-bit TestStand and 64-bit TestStand
- TestStand Directory Structure
- Bitness-Conditional Code for DLLs with Different 32-bit Interfaces and 64-bit Interfaces

<!--NI_TOPIC bundle=teststand path=locking-toolbars-menus-panes.html language=enus -->
## TOPIC 00521: Locking Toolbars, Menus, and Panes

- bundle_id: `teststand`
- source_path: `locking-toolbars-menus-panes.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/locking-toolbars-menus-panes.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `task`
- source_description: You can configure the TestStand Sequence Editor to prevent a user from customizing the user interface. For example, you might want to prevent a user from rearranging the toolbars or panes within the application, or you might want to hide specific panes, buttons, and menus so the user cannot access s

### Locking Toolbars, Menus, and Panes

You can configure the TestStand Sequence Editor to prevent a user from customizing
 the user interface. For example, you might want to prevent a user from rearranging the
 toolbars or panes within the application, or you might want to hide specific panes, buttons,
 and menus so the user cannot access specific features.

1. Click Configure»Sequence Editor Options to open the
 Sequence Editor Options dialog box.
2. Select the UI Configuration tab.
3. Select Lock UI Configuration by Disabling the Following,
 then select the check box for each element or operation you want to lock in the
 user interface.

Parent topic:

TestStand Sequence Editor

<!--NI_TOPIC bundle=teststand path=log-in-log-out-execution.html language=enus -->
## TOPIC 00522: Log in/Log out Execution

- bundle_id: `teststand`
- source_path: `log-in-log-out-execution.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/log-in-log-out-execution.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The log in and log out procedure is implemented as a Front-End callback sequence, in which a sequence you call from the application contains the code that prompts the user for a login and processes the login. Call the LoginLogout Front-End callback when the application starts, when you want to give

### Log in/Log out Execution

The log in and log out procedure is implemented as a Front-End callback sequence, in which a sequence you call from the application contains the code that prompts the user for a login and processes the login. Call the LoginLogout Front-End callback when the application starts, when you want to give the user the ability to log in or log out, and when you want the user to log out before you shut down the engine. You call the LoginLogout callback by using the Engine.CallFrontEndCallbackEx method and passing LoginLogout for the sequenceNameParam parameter.

The LoginLogout callback logs out the currently logged-in user. Depending on the value of the arguments in the argumentList parameter, the LoginLogout callback can also log in a new user.

#### ArgumentList Parameter

The argumentList parameter to the Engine.CallFrontEndCallbackEx method is a property object that contains a set of subproperties. Each subproperty represents an argument. To create the PropertyObject object for the argumentList parameter, call the Engine.NewPropertyObject method as follows:

NewPropertyObject (PropValType_Container, False, "", 0)

Call the PropertyObject.SetValBoolean method on the newly created PropertyObject to specify the value of the first argument, logoutOnly. You can choose a True or a False setting, as shown in the following examples:

- SetValBoolean ("logoutOnly", PropOption_InsertIfMissing, True)
- SetValBoolean ("logoutOnly", PropOption_InsertIfMissing, False)

Finally, call the PropertyObject.SetValBoolean method to specify the value of the second argument, isInitialLogin. This argument indicates whether this is the initial login at application startup. The callback uses this information to implement the Automatically Login Windows System User feature for Microsoft Windows.

After you call the Engine.CallFrontEndCallbackEx method, release the PropertyObject you created for the argumentList parameter.

#### Special Handling of the User Interface Message UIMsg_EndExecution

To determine when a log out or log in/log out operation has completed, keep track of the Execution.Id property of the execution the Engine.CallFrontEndCallbackEx method returns. When you receive the UIMsg_EndExecution user interface message, you can use this handle to determine whether the completed execution is the Front-End callback you created. If you know when the LoginLogout callback completes, you can perform the following tasks:

- Update the display to show the name of the currently logged-in user. Obtain the User object for the current user from the Engine.CurrentUser property and then obtain the name of the user from the User.LoginName property. You can also use the User.FullName property if you prefer.
- Process command-line arguments after a user has logged in. Tip Do not load a sequence file or run an execution in response to command-line arguments until you give the user a chance to log in.
- Shut down after the last user logs out.
- Update the state of menu items and other controls that depend on user privileges. You must re-evaluate menu items and other controls that relate to process model entry points. The results of the name expressions and enabled expressions for entry points can vary depending on the current user.

Parent topic:

Writing an Application with the TestStand Engine API

Related concepts:

- Modifying Front-End Callbacks
- Shutting Down the Engine

<!--NI_TOPIC bundle=teststand path=logging-attribute-values.html language=enus -->
## TOPIC 00523: Logging Attribute Values

- bundle_id: `teststand`
- source_path: `logging-attribute-values.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/logging-attribute-values.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The default TestStand database schemas do not log attribute values that exist on result properties. The following examples demonstrate how you can customize a database schema in the Database Options dialog box to log attributes. Logging a Specific Attribute to a Single Field To log the value of a sp

### Logging Attribute Values

The default TestStand database schemas do not log attribute values that exist on result properties. The following examples demonstrate how you can customize a database schema in the Database Options dialog box to log attributes.

#### Logging a Specific Attribute to a
 Single Field

To log the value of a specifically-named attribute that can
 exist on a specific result property, retrieve the attribute value and store the
 value in a new field in a table.

For example, if the code modules stored
 optional, additional reason information in the attribute
 MyNameSpace.StatusReason on the Status
 property of steps, you can log the value of this attribute to a new field in the
 STEP_RESULT table by creating a new String column in the
 STEP_RESULT table and configuring the schema to include the
 following new column settings:

| Column Name | STATUS_REASON |
| --- | --- |
| Type | String |
| Size | 255 |
| Direction | Input (To DB) |
| Expected Properties | Logging.StepResult.Status.Attributes.MyNameSpace.StatusReason |
| Precondition | – |
| Expression | Logging.StepResult.Status.Attributes.MyNameSpace.StatusReason |

#### Logging Attributes for
 Properties

To log all attribute names and values for any property logged
 to the PROP_RESULT table, which includes most custom step
 properties and additional results, serialize the parent Attributes
 property for each result property and store the serialization to a new field in the
 PROP_RESULT table. For example, you can add a new string
 column, ATTRIBUTES, to the PROP_RESULT table and
 configure the schema to include the following new column settings:

| Column Name | ATTRIBUTES |
| --- | --- |
| Type | String |
| Size | 4096 |
| Direction | Input (To DB) |
| Expected Properties | – |
| Precondition | Logging.PropertyResult.HasAttributes |
| Expression | Logging.PropertyResult.Attributes.GetXML(0xF0F, 0) |

Note

Parent topic:

Database Known Issues

<!--NI_TOPIC bundle=teststand path=logging-binary-strings-in-databases.html language=enus -->
## TOPIC 00524: Logging Binary Strings in Databases

- bundle_id: `teststand`
- source_path: `logging-binary-strings-in-databases.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/logging-binary-strings-in-databases.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Typically, you cannot store binary data in a string since strings cannot contain zero bytes, and strings must not contain invalid multibyte character set (MBCS) sequences. However, the TestStand LabVIEW Adapter and the TestStand API function SetValBinary support assigning binary values to string var

### Logging Binary Strings in Databases

Typically, you cannot store binary data in a string since strings cannot contain zero bytes, and strings must not contain invalid multibyte character set (MBCS) sequences. However, the TestStand LabVIEW Adapter and the TestStand API function SetValBinary support assigning binary values to string variables or properties. TestStand stores binary string values as compressed and encoded binary data using only printable non-MBCS-lead-byte characters.

The default TestStand report generator process model plug-in generates the binary string values in the compressed encoded formats. See the Retrieving Binary String Values from Reports and Databases topic for more information about retrieving binary data from string values.

Parent topic:

Database Logging

Related concepts:

- Retrieving Binary String Values from Reports and Databases

<!--NI_TOPIC bundle=teststand path=logging-enumerations-as-strings.html language=enus -->
## TOPIC 00525: Logging Enumerations as Strings

- bundle_id: `teststand`
- source_path: `logging-enumerations-as-strings.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/logging-enumerations-as-strings.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The default TestStand schemas only log the numeric values for Enumeration data types in the PROP_RESULT and PROP_BINARY tables. To log the name/string value of all Enumeration types, you can modify the schema for the PROP_RESULT table in the following manner: Open Configure»Result Processing»Databas

### Logging Enumerations as Strings

The default TestStand schemas only log the numeric values for Enumeration data types
 in the PROP_RESULT and PROP_BINARY tables.

To log the name/string value of all Enumeration types, you can modify the schema for
 the PROP_RESULT table in the following manner:

1. Open Configure»Result Processing»Database to edit the
 schema TestStand uses for Database logging.
2. Select the DATA column in the
 PROP_RESULT table of the schema you are using and modify
 the Value To Log field to use a conditional expression: Logging.PropertyResultDetails.Type.ValueType==7?
Str(Logging.PropertyResult):Logging.PropertyResult Note If you are
 using a default schema, make a copy of the schema and edit the copy to make
 these changes.

Similarly, you can use the GetValString method on the
 Logging.PropertyResult object to obtain the string value of an
 enum and log it in a new column.

Note

Value To Log

To Log the string and numeric value of all enumeration types,
 modify the expression in step 2 above to:

```text
        Logging.PropertyResultDetails.Type.ValueType==7?
Logging.PropertyResult.GetValueDisplayName(“”,0):Logging.PropertyResult
      
```

To log an array of enumeration as a single string, modify the schema for the
 PROP_RESULT table as follows:

1. Open Configure»Result Processing»Database to edit the
 schema TestStand uses for Database logging.
2. Select the DATA column in the
 PROP_RESULT table of the schema you are using. Modify the
 Precondition expression
 from (Logging.PropertyResultDetails.Type.ValueType>0&& 
Logging.PropertyResultDetails.Type.ValueType<4)|| 
Logging.PropertyResultDetails.Type.ValueType==7 to
 (Logging.PropertyResultDetails.Type.ValueType<0&& Logging.PropertyResultDetails.Type.ValueType<4)|| 
Logging.PropertyResultDetails.Type.ValueType==7||
(Logging.PropertyResultDetails.Type.ValueType== 6/*array*/&&
Logging.PropertyResultDetails.Type.ElementType.ValueType==7/*enum*/)
3. Modify the Value To Log expression
 to (Logging.PropertyResultDetails.Type.ValueType==6/*array*/&&Logging. 
PropertyResultDetails.Type.ElementType.ValueType==7/*enum*/)? 
Str(Logging.PropertyResult,“%s”,1,False,“.”):Logging.PropertyResult

Note

PROP_RESULT

Parent topic:

Database Known Issues

Related concepts:

- PROP_RESULT Table Schema
- PROP_BINARY Table Schema

<!--NI_TOPIC bundle=teststand path=logging-offline-results-processing-utility-me.html language=enus -->
## TOPIC 00526: Logging Offline Results Processing Utility Messages to a File

- bundle_id: `teststand`
- source_path: `logging-offline-results-processing-utility-me.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/logging-offline-results-processing-utility-me.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Run the TestStand Offline Results Processing Utility with a redirection operator to store a log file of the information the utility writes to the command-line standard output. Refer to Microsoft documentation for more information about using command redirection operators. For example, use the follow

### Logging Offline Results Processing Utility Messages to a File

Run the TestStand Offline Results Processing Utility with a redirection operator to store a log file of the information the utility writes to the command-line standard output. Refer to Microsoft documentation for more information about using command redirection operators.

For example, use the following command to append all information or higher level messages to the end of a file named logfile.txt:

OfflineResultsProcessingUtility.exe /log-level Info >> logfile.txt

Use the following command to log all error or higher level messages to a file named logfile.txt, overwriting the file if it already exists:

OfflineResultsProcessingUtility.exe /log-level Error > logfile.txt

Parent topic:

TestStand Offline Results Processing Utility

<!--NI_TOPIC bundle=teststand path=logging-system-metadata-for-analysis.html language=enus -->
## TOPIC 00527: Logging Metadata for Analysis

- bundle_id: `teststand`
- source_path: `logging-system-metadata-for-analysis.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/logging-system-metadata-for-analysis.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `task`
- source_description: The Measurement Data Service (MDS) Result Processor stores test data in a structured format that you can use to get insight into the environmental conditions associated with tests. Configure Result Processing Click the wrench icon in the MDS Data Store row. Enable Include system metadata to allow Te

### Logging Metadata for Analysis

The Measurement Data Service (MDS) Result Processor stores test data in a structured
 format that you can use to get insight into the environmental conditions associated with
 tests.

1. Configure»Result Processing
2. Click the wrench icon in the MDS Data Store row.
3. Enable Include system metadata to allow TestStand to
 save the following information about the test system. 
 Connected NI hardware
 Connected hardware with NI VISA drivers
 Installed NI software
4. Complete the following steps to define more metadata.
  1. Enable Include custom metadata.
  2. Click the three dot button next to Custom metadata
 assembly and select your custom assembly. 
 Note To learn more about creating a custom
 metadata assembly, follow the *Example Custom Assembly*
 link below.
  3. In the Custom metadata class dropdown menu,
 select the metadata builder you want to use from your assembly.
5. Click OK twice.

Once you have run a test with MDS Data Store
 enabled, you can ask NI Nigel ™ AI questions about the results and
 conditions of that test. You can also use the MDS API for Python or LabVIEW to query
 historical data.

Parent topic:

Measurement Data Service Data Store

Related concepts:

- Measurement Data Service Data Store
- NI Nigel AI

Related information:

- Python API Example
- LabVIEW API Example
- Example Custom Assembly

<!--NI_TOPIC bundle=teststand path=lookup-strings.html language=enus -->
## TOPIC 00528: Lookup Strings

- bundle_id: `teststand`
- source_path: `lookup-strings.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/lookup-strings.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: To specify the dynamic property on which a method operates, pass a string that defines a complete path from the object on which you call the method to the specific property you want to access. This string is called a lookup string. Use the following techniques to specify different objects: To specif

### Lookup Strings

To specify the dynamic property on which a method operates, pass a string that defines a complete path from the object on which you call the method to the specific property you want to access. This string is called a lookup string. Use the following techniques to specify different objects:

- To specify the object itself, pass an empty string ( "" ).
- To specify a subproperty, pass the name of the subproperty.
- To specify a subproperty of a subproperty, pass a string that contains both names separated by a period ( . ).

For example, you can specify the error code property in a step object using the following lookup string:

"Result.Error.Code"

TestStand expressions require PropertyObject names to be strings that contain only letters, numbers, and underscores. PropertyObject names cannot contain spaces, start with a number, or be empty. For example, MyVariableName_2000 is a valid PropertyObject name. Names of elements in a PropertyObject array, such as sequence and step names, can contain any character. Instead of using lookup strings that contain array element names that might not be unique, such as step names, with methods that have a lookupString parameter, use a string that specifies the array index instead.

Note

PropertyObject

You can specify an attribute or type attribute using a lookup string. Use Attributes in a lookup string to specify the attributes of the property object and use TypeAttributes to specify the type attributes of the property object. For example, the following lookup string accesses an attribute of a local variable from a sequence:

"Locals.Foo.Attributes.MyAttributeNamespace.Attribute1"

Note

Attributes

TypeAttributes

When you specify a named array element using a lookup string, such as
 myarray["myelementname"], use the standard C-style backslash escaping
 technique to escape special characters in the string. For example, for a single backslash in
 the actual name, use two backslashes in the escaped name. Use the Utility.Escape method to
 escape a string as needed.

Parent topic:

Property Paths

Related concepts:

- Accessing Dynamic Properties

<!--NI_TOPIC bundle=teststand path=loop-results.html language=enus -->
## TOPIC 00529: Loop Results

- bundle_id: `teststand`
- source_path: `loop-results.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/loop-results.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: When you configure a step to loop, you can use the Record Result of Each Iteration option on the Looping panel of the Step Settings pane to direct TestStand to store a separate result for each loop iteration in the result list. In the result list, the results for the loop iterations immediately foll

### Loop Results

When you configure a step to loop, you can use the Record Result of Each Iteration option on the Looping panel of the Step Settings pane to direct TestStand to store a separate result for each loop iteration in the result list. In the result list, the results for the loop iterations immediately follow the result for the step as a whole.

TestStand adds a TS.LoopIndex numeric property to each loop iteration result to record the value of the loop index for the iteration. TestStand also adds the following special loop result properties to the main result for the step:

- TS.EndingLoopIndex —Value of the loop index when looping completes.
- TS.NumLoops —Number of times the step loops.
- TS.NumPassed —Number of loops for which the step status is Passed or Done .
- TS.NumFailed —Number of loops for which the step status is Failed .

Parent topic:

Result Collection

<!--NI_TOPIC bundle=teststand path=main-execution-entry-points-in-the-batch-proc.html language=enus -->
## TOPIC 00530: Main Execution Entry Points in the Batch Process Model

- bundle_id: `teststand`
- source_path: `main-execution-entry-points-in-the-batch-proc.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/main-execution-entry-points-in-the-batch-proc.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Batch process model includes the following main Execution entry point sequences: Test UUTs—Initiates an execution that controls a separate execution for each test socket using the Test UUTs - Test Socket Entry Point sequence. The Test UUTs sequence adds the main threads of those executions to a

### Main Execution Entry Points in the Batch Process Model

The Batch process model includes the following main Execution entry point sequences:

- Test UUTs—Initiates an execution that controls a separate execution for each test socket using the Test UUTs - Test Socket Entry Point sequence. The Test UUTs sequence adds the main threads of those executions to a Batch Synchronization object and controls the flow of execution using an instance of the ControllerAndSocketSynchronizationManager class of ManagedModelSupport.dll , located in <TestStand>\Components\Models\TestStandModels\ManagedModelSupport , so all test socket executions execute the MainSequence of the client sequence file together as a group. After a group of UUTs executes, the report generator process model plug-in generates a batch report, loops back to run the client sequence file on the next group of UUTs, and controls the subsidiary test socket executions to keep them synchronized. The Execute menu includes the Test UUTs item when a window for a client sequence file is active.
- Single Pass—Initiates an execution that controls a separate execution for each test socket using the Single Pass - Test Socket Entry Point sequence. The Single Pass sequence adds the main threads of those executions to a Batch Synchronization object and controls the flow of execution using an instance of the ControllerAndSocketSynchronizationManager class of ManagedModelSupport.dll , located in <TestStand>\Components\Models\TestStandModels\ManagedModelSupport , so all test socket executions execute the MainSequence of the client sequence file together as a group. After the group of UUTs executes, the Single Pass sequence generates a batch report and waits for all subsidiary executions to complete. The Execute menu includes the Single Pass item when a window for a client sequence file is active.

Parent topic:

Batch Process Model

Related concepts:

- Test UUTs Execution Entry Point in the Batch Process Model
- Test UUTs – Test Socket Entry Point Execution Entry Point in the Batch Process Model
- Batch Controller and Test Socket Synchronization Architecture
- TestStand Directory Structure
- Single Pass Execution Entry Point in the Batch Process Model
- Single Pass - Test Socket Entry Point in the Batch Process Model

<!--NI_TOPIC bundle=teststand path=main-execution-entry-points-in-the-parallel-p.html language=enus -->
## TOPIC 00531: Main Execution Entry Points in the Parallel Process Model

- bundle_id: `teststand`
- source_path: `main-execution-entry-points-in-the-parallel-p.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/main-execution-entry-points-in-the-parallel-p.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Parallel process model includes the following main Execution entry point sequences: Test UUTs—Initiates a hidden execution that controls the test socket executions it creates using the Test UUTs - Test Socket Entry Point sequence. The Execute menu includes the Test UUTs item when a window for a

### Main Execution Entry Points in the Parallel Process Model

The Parallel process model includes the following main Execution entry point sequences:

- Test UUTs—Initiates a hidden execution that controls the test socket executions it creates using the Test UUTs - Test Socket Entry Point sequence. The Execute menu includes the Test UUTs item when a window for a client sequence file is active.
- Single Pass—Initiates a hidden execution that controls the test socket executions it creates using the Single Pass - Test Socket Entry Point sequence. The Execute menu includes the Single Pass item when a window for a client sequence file is active.

Parent topic:

Parallel Process Model

Related concepts:

- Test UUTs Execution Entry Point in the Parallel Process Model
- Test UUTs – Test Socket Entry Point Execution Entry Point in the Parallel Process Model
- Single Pass Execution Entry Point in the Parallel Process Model
- Single Pass - Test Socket Execution Entry Point in the Parallel Process Model
- Hidden Execution Entry Points in the Parallel Process Model

<!--NI_TOPIC bundle=teststand path=main-sequence-and-client-sequence-file.html language=enus -->
## TOPIC 00532: Main Sequence and Client Sequence File

- bundle_id: `teststand`
- source_path: `main-sequence-and-client-sequence-file.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/main-sequence-and-client-sequence-file.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Main sequence initiates the tests on a UUT. The process model defines what is constant about the testing process, and Main sequences define the unique steps for the different types of tests to run. When you create a new sequence file, TestStand automatically inserts a Main sequence in the file.

### Main Sequence and Client Sequence File

The Main sequence initiates the tests on a UUT. The process model defines what is constant about the testing process, and Main sequences define the unique steps for the different types of tests to run. When you create a new sequence file, TestStand automatically inserts a Main sequence in the file. You must name each Main sequence MainSequence.

The process model invokes the Main sequence as part of the overall testing process. TestStand uses the station process model file to determine which process model file to use with the Main sequence unless the sequence file specifies a different process model file and you enabled the Allow Other Models option in the Station Options dialog box to allow sequence files to override the station model setting.

After TestStand identifies the process model to use with the Main sequence, the file that contains the Main sequence becomes a client sequence file of the process model.

Parent topic:

Process Models

<!--NI_TOPIC bundle=teststand path=making-a-custom-rule-configurable.html language=enus -->
## TOPIC 00533: Making a Custom Rule Configurable in the TestStand Sequence Analyzer

- bundle_id: `teststand`
- source_path: `making-a-custom-rule-configurable.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/making-a-custom-rule-configurable.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: If you want users to configure the custom rule you create, you must select one of the following rule configuration options on the Advanced tab of the Edit Rule dialog box: Use Rule Settings—Define a set of Boolean, number, string, or enumeration settings that users can set in the Rule Settings dialo

### Making a Custom Rule Configurable in the
 TestStand Sequence Analyzer

If you want users to configure the custom rule you create, you must select one of the
 following rule configuration options on the Advanced tab of the Edit Rule dialog box:

- Use Rule Settings —Define a set of Boolean, number, string, or
 enumeration settings that users can set in the Rule Settings dialog box, which the
 TestStand Sequence Analyzer launches when a user clicks the
 Settings button on the Rules pane or tab. The standard
 dialog box stores the settings for the rule that the analysis module accesses. In
 general, this option is easier to use because you do not have to write a rule
 configuration module or dialog box.
- Use Configuration Module —Create a rule configuration module
 that launches a dialog box the sequence analyzer launches when a user clicks the
 Settings button on the Rules pane or Rules tab. The
 dialog box you create stores custom data for the rule that the analysis module
 accesses. Select this option in the following situations:
  - You prefer a custom look for the dialog box users use to configure the
 rule.
  - You need to store data more complex than Boolean, number, string, or
 enumeration values, such as a list of string values.
  - You need to use custom controls, tree controls, or list controls in the
 dialog box.

Parent topic:

TestStand Sequence Analyzer

Related concepts:

- Accessing Rule Settings in Analysis Modules
- Creating Rule Configuration Modules in the TestStand Sequence Analyzer

Related information:

- Edit Rule Dialog Box
- Rule Settings Dialog Box

<!--NI_TOPIC bundle=teststand path=making-dialog-boxes-modal-to-teststand.html language=enus -->
## TOPIC 00534: Making Dialog Boxes Modal to TestStand

- bundle_id: `teststand`
- source_path: `making-dialog-boxes-modal-to-teststand.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/making-dialog-boxes-modal-to-teststand.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Code modules that TestStand calls can launch dialog boxes modal to TestStand application windows, such as the TestStand Sequence Editor or custom user interfaces. LabVIEW Use the TestStand - Start Modal Dialog and the TestStand - End Modal Dialog VIs, located on the Functions»TestStand palette in La

### Making Dialog Boxes Modal to TestStand

Code modules that TestStand calls can launch dialog boxes modal to TestStand application windows, such as the TestStand Sequence Editor or custom user interfaces.

#### LabVIEW

Use the TestStand -
 Start Modal Dialog and the TestStand - End Modal Dialog VIs, located on the
 Functions»TestStand palette in LabVIEW, to make a dialog
 box modal to TestStand application windows. Refer to the<TestStand
 Public>\Examples\Fundamentals\Launching a Modal Dialog\LabVIEW
 directory for examples of how to use these VIs.

#### LabWindows/CVI

Use the
 TS_StartModalDialogEx and TS_EndModalDialog
 functions the TestStand Utility Functions driver provides to make a dialog box modal
 to TestStand application windows. Refer to the
 <TestStand>\Components\StepTypes\MsgBox\msgbox.c
 source file for an example of to use these functions.

Parent topic:

Advanced User Interface Development

Related concepts:

- TestStand Directory Structure
- TestStand Utility Functions Library
- Launching a Modal Dialog

<!--NI_TOPIC bundle=teststand path=managed-code-consid.html language=enus -->
## TOPIC 00535: Managed Code Considerations for TestStand and .NET 8

- bundle_id: `teststand`
- source_path: `managed-code-consid.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/managed-code-consid.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: TestStand 2025 Q2 and later use .NET 8 to run .NET-based tools, utilities, and interfaces. Users working with .NET code in their TestStand projects and sequences should keep the following recommendations and resources in mind when developing their code. You should use the TestStandObjectReleaser uti

### Managed Code Considerations for TestStand and
 .NET 8

TestStand 2025 Q2 and later use .NET 8 to run .NET-based tools, utilities, and
 interfaces. Users working with .NET code in their TestStand projects and sequences
 should keep the following recommendations and resources in mind when developing
 their code.

- You should use the TestStandObjectReleaser 
 utility class in the
 NationalInstruments.TestStand.Utility 
 DLL under the
 NationalInstruments.TestStand.Utility 
 namespace to handle TestStand objects in managed code. This
 class identifies all TestStand objects that can be reached
 from the root object during construction and ensures proper
 disposal of these objects in the Dispose 
 method. You should call this utility to handle disposal of
 TestStand objects in the Dispose method. For protected override void Dispose(bool disposing) 
{ 
    using (new TestStandObjectReleaserExcludingEngineAndUIControls(this)) 
    { 
        if (disposing) 
        { 
            components?.Dispose(); 
        } 
        base.Dispose(disposing); 
    } 
}
- You should use the Microsoft.NetCore.App ,
 Microsoft.WindowsDesktop.App , and
 Microsoft.AspNetCore.App .NET
 runtimes when developing .NET 8-based TestStand applications
 and user interfaces. You can use the below format to include
 dependencies on these .NET
 runtimes. <ItemGroup>
<FrameworkReference 
 Include="Microsoft.WindowsDesktop.App" /> 
<FrameworkReference 
 Include="Microsoft.AspNetCore.App" />
</ItemGroup>
- The .NET 8 Assembly.Load and
 Assembly.LoadFrom methods both
 create new AssemblyLoadContext (ALC)
 objects with the isCollectible property set
 to False when called, and load the
 specified assembly in the newly created ALC object. This can
 cause typecasting and type missing exceptions when calling
 classes and methods from an assembly, as the same type may
 be loaded in multiple ALCs. This is especially likely when
 attempting to cast to a type with an exact, fully qualified
 type name results in a Type Mismatch or
 Type Missing exception. You can
 avoid this issue by using
 AssemblyLoadContext.LoadFromAssemblyPath 
 to reference the current ALC instead of
 Assembly.Load or
 Assembly.LoadFrom . The
 LoadFromAssemblyPath method loads
 the assembly directly into the ALC instance you invoke the
 method on, preventing you from creating copies of the same
 assembly in multiple load contexts.
  - If you see this error in a code module, you
 should load your assembly into the TestStand
 execution ALC. You can accomplish this by getting
 a reference to the execution ALC using
 AssemblyLoadContext currentContext = AssemblyLoadContext.GetLoadContext(Assembly.GetExecutingAssembly()); and
 then loading your assembly dynamically using
 currentContext.LoadFromAssemblyPath() .
  - If you see this error when using .NET Framework
 modules to load your assembly into the current
 ALC, use reflection to find the
 System.Runtime.Loader.AssemblyLoadContext 
 like in the below example. Assembly loadedAssembly = null; 
try 
{ 
 Assembly assemblyLoadContext = Type.GetType("System.Runtime.Loader.AssemblyLoadContext", throwOnError: false); 
 if (assemblyLoadContext != null) 
 { 
 MethodInfo getLoadContext = assemblyLoadContext.GetMethod( 
 "GetLoadContext", 
 BindingFlags.Static | BindingFlags.Public, 
 binder: null, 
 new[] { typeof(Assembly) }, 
 modifiers: null); 
 if (getLoadContext != null) 
 { 
 Assembly thisAssembly = Assembly.GetExecutingAssembly(); 
 object loadContext = getLoadContext.Invoke(null, new[] { thisAssembly }); 
 if (loadContext != null) 
 { 
 MethodInfo loadFromAssemblyPath = loadContext.GetType().GetMethod( 
 "LoadFromAssemblyPath", 
 new Type[] { typeof(string) }); 
 if (loadFromAssemblyPath != null) 
 { 
 loadedAssembly = (Assembly)loadFromAssemblyPath.Invoke(loadContext, new[] { fullPath }); 
 } 
 } 
 } 
 } 
} 
catch 
{ 
 // Ignore any exceptions and just fall back to loading the assembly the .NET Framework-compatible way 
} 
loadedAssembly = loadedAssembly ?? Assembly.LoadFrom(fullPath); 
return loadedAssembly;

Parent topic:

.NET Adapter

<!--NI_TOPIC bundle=teststand path=manager-controls.html language=enus -->
## TOPIC 00536: Manager Controls

- bundle_id: `teststand`
- source_path: `manager-controls.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/manager-controls.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Application Manager, SequenceFileView Manager, and ExecutionView Manager controls call the TestStand API to perform tasks such as loading files, launching executions, and retrieving sequence and execution information. Manager controls also notify you when application events occur, such as when a use

### Manager Controls

Application Manager, SequenceFileView Manager, and ExecutionView Manager controls call the TestStand API to perform tasks such as loading files, launching executions, and retrieving sequence and execution information. Manager controls also notify you when application events occur, such as when a user logs in, an execution reaches a breakpoint, or a user changes the file or sequence they are viewing. Manager controls are visible at design time and invisible at run time.

Connect the manager controls to visible TestStand User Interface (UI) Controls to display information or to allow users to select items to view.

Parent topic:

Getting Started with User Interface Development

Related concepts:

- Application Manager
- SequenceFileView Manager
- ExecutionView Manager
- Connecting Manager Controls to Visible Controls
- TestStand UI Controls

<!--NI_TOPIC bundle=teststand path=managing-memory-allocation-for-large-labview.html language=enus -->
## TOPIC 00537: Managing Memory Allocation for Large LabVIEW Data Sets

- bundle_id: `teststand`
- source_path: `managing-memory-allocation-for-large-labview.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/managing-memory-allocation-for-large-labview.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: LabVIEW automatically handles memory allocation. Because this process is automatic, LabVIEW copies data frequently. If the test system involves large sets of data, large and frequent data copies might result in an out-of-memory error.

### Managing Memory Allocation for Large LabVIEW Data Sets

LabVIEW automatically handles memory allocation. Because this process is automatic, LabVIEW copies data frequently.

If the test system involves large sets of data, large and frequent data copies might result in an out-of-memory error.

Parent topic:

Special Considerations for Using LabVIEW with TestStand Systems

Related concepts:

- Special Considerations for Using LabVIEW with TestStand Systems
- Reusing VIs

<!--NI_TOPIC bundle=teststand path=managing-menu-bars-and-menu-event-handling-in.html language=enus -->
## TOPIC 00538: Managing Menu Bars and Menu Event Handling in a LabVIEW User Interface

- bundle_id: `teststand`
- source_path: `managing-menu-bars-and-menu-event-handling-in.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/managing-menu-bars-and-menu-event-handling-in.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The TestStand VIs and functions palette contains the following VIs for creating and handling menu items that execute TestStand UI Control commands: TestStand - Insert Commands in Menu TestStand - Cleanup Menus TestStand - Remove Commands From Menus TestStand - Execute Menu Command Because maintainin

### Managing Menu Bars and Menu Event Handling in a LabVIEW User Interface

The TestStand VIs and functions palette contains the following VIs for creating and handling menu items that execute TestStand UI Control commands:

- TestStand - Insert Commands in Menu
- TestStand - Cleanup Menus
- TestStand - Remove Commands From Menus
- TestStand - Execute Menu Command

Because maintaining the current state of the menu bar can be difficult, NI recommends that you
 handle the menu bar only when required. The Event structure in a main event loop can
 include a case to handle the Menu Activation? event to determine when you open a
 menu or select a shortcut key that might be linked to a menu item. The block diagram
 that handles this event can then rebuild the menu bar.

The Full UI - Top-Level VI in the example user interfaces shows how to rebuild the menu bar. The Menu Activation? case in the main event loop of the VI determines which control has focus, if the control is a TestStand User Interface (UI) Control, and calls the Full UI - Rebuild Menu Bar VI to rebuild the menu bar. When you click the menu bar, LabVIEW does not automatically return focus to the control after handling a user menu event. The Menu Activation? case in the Full UI - Top-Level VI passes a reference for the control with focus to the Menu Selection (User) case so the application can later restore focus to the control.

You can add a Menu Selection (User) case to the Event structure in a main event loop to handle user menu selections but limit the tasks you perform in the Menu Selection (User) case to ensure that LabVIEW handles the menu selection in a timely manner. When the case performs ActiveX operations that can process messages or performs TestStand operations that can call back into LabVIEW, the application must perform these operations in a LabVIEW execution system other than user interface, such as standard or other 2.

The Full UI - Top-Level VI in the example user interfaces shows how to process user menu events. The VI uses the standard LabVIEW execution system. The Menu Selection (User) case in the main event loop calls the Full UI - Add To Menu Queue VI to queue the operation for processing the menu outside of the main event loop. The Full UI - Process Menu Queue VI waits for and processes queued operations. For TestStand menu items, the Full UI - Process Menu Queue VI calls the TestStand - Execute Menu Command VI to execute the appropriate TestStand command. For non-TestStand menu items, the VI calls the Full UI - Process User Menus VI, which you can customize to handle user menu selections.

The LabVIEW application menu items for copy, cut, and paste operate on LabVIEW controls only and do not operate on TestStand UI Controls. In addition, the TestStand menu commands operate on TestStand UI Controls only and not on LabVIEW controls. When you rebuild a LabVIEW menu in the Menu Activation? event case and you call the TestStand - Insert Commands in Menu VI to insert CommandKind_Edit_Copy, CommandKind_Edit_Cut, or CommandKind_Edit_Paste, pass False to the TestStand UI Control Has Focus control and "Edit" to the Top-Level Menu to Insert Into control to insert the corresponding LabVIEW application menu items instead of the TestStand menu command.

Parent topic:

Managing Menus and Menu Items

Related concepts:

- Using TestStand UI Controls in LabVIEW
- Example User Interfaces
- TestStand UI Controls

<!--NI_TOPIC bundle=teststand path=managing-menu-bars-in-a-labwindows-cvi-user-i.html language=enus -->
## TOPIC 00539: Managing Menu Bars in a LabWindows/CVI User Interface

- bundle_id: `teststand`
- source_path: `managing-menu-bars-in-a-labwindows-cvi-user-i.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/managing-menu-bars-in-a-labwindows-cvi-user-i.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The TestStand Utility Functions provide the following set of functions for creating and handling TestStand-specific menu items without requiring any additional code: TS_InsertCommandsInMenu TS_RemoveMenuCommands TS_CleanupMenu Use the TS_InsertCommandsInMenu function to create new menu items that ex

### Managing Menu Bars in a LabWindows/CVI User Interface

The TestStand Utility Functions provide the following set of functions for creating and handling TestStand-specific menu items without requiring any additional code:

- TS_InsertCommandsInMenu
- TS_RemoveMenuCommands
- TS_CleanupMenu

Use the TS_InsertCommandsInMenu function to create new menu items that execute commands you specify. To create menu items, you specify an array of command types, and the menu bar and menu IDs determine where to insert the commands. Each command type specifies a menu item or group of menu items to insert. You must also specify a handle to the Application Manager control, ExecutionView Manager control, or SequenceFileView Manager control to which the new menu items apply. TestStand uses a manager control to determine whether the menu item is visible or dimmed. TestStand installs a callback sequence for each menu item that automatically invokes the associated command when the user selects the menu item.

Call the TS_InsertCommandsInMenu function when the application rebuilds the menu bar in a MenuDimmerCallback function to populate the menu bar with commands that apply to the current state of the application. Before you call this function, you can call TS_RemoveMenuCommands to remove any menu items you previously inserted.

Refer to the RebuildMenuBar function in the <TestStand Public>\UserInterfaces\Full-Featured\CVI\Source Code\TestExec.c source file for an example of rebuilding the menu bar.

Parent topic:

Managing Menus and Menu Items

Related concepts:

- TestStand Directory Structure
- TestStand UI Controls

<!--NI_TOPIC bundle=teststand path=managing-menus-and-menu-items.html language=enus -->
## TOPIC 00540: Managing Menus and Menu Items

- bundle_id: `teststand`
- source_path: `managing-menus-and-menu-items.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/managing-menus-and-menu-items.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: TestStand applications that provide non-trivial menus can require a large amount of source code to build and update the state of menus and to handle events for menu items. Use the TestStand Utility (TSUtil) functions to create menu items that invoke TestStand commands to greatly reduce the amount of

### Managing Menus and Menu Items

TestStand applications that provide non-trivial menus can require a large amount of source code to build and update the state of menus and to handle events for menu items. Use the TestStand Utility (TSUtil) functions to create menu items that invoke TestStand commands to greatly reduce the amount of code required to implement menus in an application. TestStand automatically dims or enables these menu items according to the application state and sets their captions according to the language selection. The menu items execute commands automatically so that the application does not need to handle menu events or provide command implementations.

The application can also insert sets of dynamic menu items, such as a set of menu items to open files from the most recently used file list or a set of menu items that run the current sequence with each available process model entry point. To create TestStand menu items, you must first add TSUtil to the project.

Note

Note

Choose Items

MainMenu 2.0

OK

#### Updating Menus and Menu
 Items

The contents of a menu can vary depending on the current selection,
 other user input, or asynchronous execution state changes. Instead of updating a
 menu in response to any event or change that might affect the menu, update the state
 of a menu just before the menu displays when the user opens the menu. The following
 table lists the notification method different application development environments
 (ADEs) use to notify the application when a user is about to open a menu.

| ADE | Menu Open Notification Method |
| --- | --- |
| LabVIEW | <This VI>:Menu Activation? event |
| LabWindows/CVI | InstallMenuDimmerCallback |
| .NET | Form.MenuStart |
| C++ (MFC) | CWnd::OnInitMenuPopup |

Use the RemoveMenuCommands,
 InsertCommandsInMenu, and CleanupMenu
 TestStand Utility (TSUtil) functions in LabVIEW and LabWindows/CVI to handle the
 menu open notifications and remove and reinsert TestStand menu items. You can remove
 and insert TestStand commands in menus that contain non-TestStand menu items.

The InsertCommandsInMenu function accepts an array of
 CommandKinds enumeration constants. Depending on the element value and the
 application state, each array element can create a single menu item, a set of
 several menu items, or no menu items. The CommandKinds enumeration
 also provides constants that expand into the full set of items commonly found in
 test application top-level menus, such as the File menu, Debug menu, or Configure
 menu.

Refer to the examples in the
 <TestStand>\UserInterfaces\Full-Featured directory
 for sample code that handles menu open notification events.

Parent topic:

Advanced User Interface Development

Related concepts:

- TestStand Utility Functions Library
- Managing Menu Bars and Menu Event Handling in a LabVIEW User Interface
- Managing Menu Bars in a LabWindows/CVI User Interface
- TestStand Directory Structure

<!--NI_TOPIC bundle=teststand path=managing-process-model-entry-points.html language=enus -->
## TOPIC 00541: Managing Process Model Entry Points

- bundle_id: `teststand`
- source_path: `managing-process-model-entry-points.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/managing-process-model-entry-points.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: This topic requires a thorough understanding of process models and how you use them. Applications typically display the entry points the process model defines as menu items or buttons the user can select. Obtaining the Process Model Sequence File Complete the following steps to first obtain the proc

### Managing Process Model Entry Points

This topic requires a thorough understanding of process models and how you use them.

Applications typically display the entry points the process model defines as menu items or buttons the user can select.

#### Obtaining the Process Model Sequence File

Complete the following steps to first obtain the process model sequence file to determine which process model entry points apply to a given situation.

1. If you are displaying an execution, call the Execution.GetSequenceFile method of the execution and then call the SequenceFile.GetModelSequenceFile method on the sequence file the Execution.GetSequenceFile method returns. If the SequenceFile.GetModelSequenceFile method returns a NULL reference, continue to step 3. The sequence file the Execution.GetSequenceFile method returns is the client sequence file.
2. If you are displaying a sequence file, call the SequenceFile.GetModelSequenceFile method on the sequence file. If the SequenceFile.GetModelSequenceFile method returns a NULL reference, continue to step 3. The sequence file you display is the client sequence file.
3. If you are not displaying a sequence file or an execution, or if the execution or sequence file does not specify a model sequence file, call the Engine.GetStationModelSequenceFile method. If the Engine.GetStationModelSequenceFile method returns a NULL reference, no model sequence file currently applies. Otherwise, the Engine.GetStationModelSequenceFile method returns the applicable model sequence file. In this case, no client sequence file exists.

#### Obtaining the Applicable Entry Point Sequences

If no model sequence file applies to the current context in the user interface, no entry points currently apply. If a model sequence file does apply, you can determine which, if any, sequences in the file are entry points and whether they apply by enumerating all the sequences in the model sequence file. First, obtain the number of sequences from the SequenceFile.NumSequences property of the model sequence file. Then, obtain each individual sequence using the SequenceFile.GetSequence method. To obtain each sequence, pass indices 0 through (NumSequences – 1). Complete the following steps to determine if each sequence is an applicable entry point.

1. Is the Type property of the sequence equal to the value of the SeqType_CfgEntryPoint enumeration? If so, continue to step 5. If not, continue to step 2.
2. Is the Type property of the sequence equal to the value of the SeqType_ExeEntryPoint enumeration? If so, continue to step 3. If not, this sequence is not an applicable entry point.
3. Did you obtain the model sequence file from a client sequence file? If so, continue to step 4. If not, this sequence is not an applicable entry point. Notice that the latter case applies when you obtain the model sequence file by calling the Engine.GetStationModelSequenceFile method.
4. Does the client sequence file from which you obtained the model sequence file contain a sequence called MainSequence ? If so, continue to step 5. If not, this sequence is not an applicable entry point.
5. If the Sequence.ShowEntryPointForEditorOnly property is False or the application is a sequence editor, continue to step 6. If the Sequence.ShowEntryPointForEditorOnly property of the sequence is True and the application is not a sequence editor, this sequence is not an applicable entry point.
6. If the Sequence.ShowEntryPointForExeWindow property of the sequence is True and you are displaying an Execution window, this sequence is an applicable entry point. Add it to the list of entry point sequences. If not, continue to step 7.
7. If the Sequence.ShowEntryPointForFileWindow property of the sequence is True and you are displaying a sequence file, this sequence is an applicable entry point. Add it to the list of entry point sequences. If not, continue to step 8.
8. If the Sequence.ShowEntryPointForAllWindows property of the sequence is True , this sequence is an applicable entry point. Add it to the list of entry point sequences. If not, this sequence is not an applicable entry point.

You now have a list of applicable entry point sequences. The next step is to create the menu items and/or command buttons that allow the user to create executions from the entry points.

#### Creating the Menu Items

When creating an entry point, you must determine which menu or submenu in which to place it. You can place entry points by type, such as putting entry points of the SeqType_CfgEntryPoint type in the Configure menu and entry points of the SeqType_ExeEntryPoint type in the Execute menu, or you can use the Sequence.GetEntryPointMenuFromHint method of the entry point sequence. If the Sequence.GetEntryPointMenuFromHint method cannot find a menu that matches any of the menu hints for the entry point, place the entry point menu item by type.

After you determine the location of the menu item, obtain the string to display for the menu item by calling the Sequence.EvalEntryPointNameExpressionEx method of the entry point sequence. Pass a reference to the client sequence file as the parameter to the method, or pass a NULL reference if no client sequence file exists. Similarly, call the Sequence.EvalEntryPointEnabledExpressionEx method to determine whether to enable the menu item.

Note

Sequence.EvalEntryPointEnabledExpression

Priv_Execute

Priv_RunAnySequence

#### Executing an Entry Point

Consider the following situations for executing an entry point. If a client sequence file exists, you must first create an EditArgs object by calling the Engine.NewEditArgs method. Use the EditArgs object to specify which TestStand objects the user selects in the application. If the client sequence file is from an execution, call the EditArgs.SetSelectedExecution method of the newly created EditArgs object and pass a reference to the execution. If the client sequence file is from a Sequence File window, call the EditArgs.SetSelectedSequenceFile method and then call the EditArgs.AddSelectedSequence method and the EditArgs.AddSelectedStep method to add any currently selected steps and sequences.

Pass the following parameters as arguments to the Engine.NewExecution method:

| Parameter Name | What to Pass |
| --- | --- |
| sequenceFileParam | A reference to the client sequence file, or a NULL reference if no client sequence file exists. Depending on the application development environment you use, pass 0 or the Nothing keyword to indicate a NULL reference. |
| sequenceNameParam | The value of the Sequence.Name property of the entry point sequence. |
| processModelParam | A reference to the model sequence file. |
| breakAtFirstStep | False. |
| executionTypeMaskParam | If the value of the Sequence.EntryPointInitiallyHidden property of the entry point sequence is True, pass the value of the ExecTypeMask_InitiallyHidden constant. Otherwise, pass the ExecTypeMask_Normal constant. |
| sequenceArgsParam[Optional] | Leave this parameter unspecified. |
| editArgsParam[Optional] | Specify this parameter only if a client sequence file exists. Pass a reference to the EditArgs object you create according to the instructions earlier in this section. |
| InteractiveArgsParam[Optional] | Specify this parameter only if you want to create an interactive execution. |

Parent topic:

Writing an Application with the TestStand Engine API

Related concepts:

- Process Model Architecture
- Enforcing User Privileges
- Starting an Interactive Execution in an Application

<!--NI_TOPIC bundle=teststand path=managing-profiler-overhead.html language=enus -->
## TOPIC 00542: Managing Profiler Overhead

- bundle_id: `teststand`
- source_path: `managing-profiler-overhead.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/managing-profiler-overhead.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Managing Profiler Overhead The profiler collects information in events that describe the operations it displays. It takes a small amount of time and memory for TestStand to store a profiler event. However, if you profile sequences that execute large numbers of steps that run very quickly and you do

### Managing Profiler Overhead

#### Managing Profiler Overhead

The profiler collects information in events that describe the operations it displays. It takes a small amount of time and memory for TestStand to store a profiler event. However, if you profile sequences that execute large numbers of steps that run very quickly and you do not limit the events that the profiler collects, the profiler can collect a number of events large enough to consume a significant amount of time and memory. The number of events the profiler can collect before the effect on performance becomes problematic is system dependent.

If you collect more profiling data than your system can acceptably process, you can do the following to improve performance:

- Hide Selected Categories of Data —You can hide selected categories of data using the options in the View menu. Hiding large numbers of events improves the performance of the profiler window, but is less beneficial than reducing the amount of data collected.
- Reduce and/or Limit the Amount of Data —You can control the amount of data the profiler collects using the options in the Configure Data Collection dialog box. This is the most effective option for improving performance.
- Disable Profiler Display Updates —You can disable the Update Display button while collecting data. This has a small effect, but can reduce the amount that the operation of the profiler displays impacts the timestamps of the collected events, especially if the profiled operations consume all of the available cpu cores such that the profiler window must share a core with profiled operations.

Parent topic:

Execution Profiler

<!--NI_TOPIC bundle=teststand path=managing-sequence-files-in-an-application.html language=enus -->
## TOPIC 00543: Managing Sequence Files in an Application

- bundle_id: `teststand`
- source_path: `managing-sequence-files-in-an-application.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/managing-sequence-files-in-an-application.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: None Loading and Caching To obtain a reference to a sequence file on disk, call the Engine.GetSequenceFileEx method. If the sequence file is already in memory, the method returns a reference to the file in the cache. If the sequence file is not already in memory, this method loads the sequence file

### Managing Sequence Files in an Application

None

#### Loading and Caching

To obtain a reference to a sequence file on disk, call the Engine.GetSequenceFileEx method. If the sequence file is already in memory, the method returns a reference to the file in the cache. If the sequence file is not already in memory, this method loads the sequence file from disk and places it in the internal sequence file cache of the TestStand Engine. Every sequence file reference you obtain from the Engine.GetSequenceFileEx method causes the cache to increment an internal usage count for the sequence file. When you are finished with the sequence file, you must call the Engine.ReleaseSequenceFileEx method to decrement the usage count. If your development environment requires you to explicitly release COM references, you must call the Engine.ReleaseSequenceFileEx method before releasing the COM reference to the sequence file.

To create a new sequence file, call the Engine.NewSequenceFile method, which adds the new sequence file to the internal sequence file cache of the engine. Therefore, before you release a sequence file you obtain from the Engine.NewSequenceFile method, you must call the Engine.ReleaseSequenceFileEx method on the sequence file. The new sequence file contains one sequence named MainSequence. You can .

You can also use the SequenceFile.AddLoadReference method to add an additional load reference to a sequence file. You must call the Engine.ReleaseSequenceFileEx method to decrement the load reference.

#### Structure of a Sequence File

A sequence file contains an array of sequences. Each sequence contains Setup, Main, and Cleanup step groups. To access the sequences in a sequence file, use the following methods and properties of the SequenceFile object:

- NumSequences property
- GetSequence method
- GetSequenceByName method
- GetSequenceIndex method

To access the steps in a sequence, use the following methods of the Sequence object:

- GetNumSteps method
- GetStep method
- GetStepByName method
- GetStepIndex method

Notice that all of the functions for accessing steps use a StepGroups constant to specify the step group that contains the step.

#### Adding New Steps and Sequences

Every step you insert into a sequence must be a unique instance. If you want to use the same step in two sequences, you must insert separate copies of the step. If you want to repeat a step in a sequence, you must insert a separate copy of the step. You can make a copy of a step by calling the PropertyObject.Clone method. Thus, you can insert a step after you create it, clone it, or remove it from a sequence. This functionality also applies to inserting sequences into sequence files.

To create a new step, call the Engine.NewStep method and then pass an adapter key name and a step type name using the AdapterKeyNames and StepTypes constants. You can then insert the new step into a sequence using the Sequence.InsertStep method. Name the new step and specify its adapter and step-type-specific properties as necessary.

To create a new sequence, call the Engine.NewSequence method and insert the new sequence into a sequence file using the SequenceFile.InsertSequenceEx method. Name the new sequence with a name that is unique among the sequences in the sequence file.

Other methods you can use to implement sequence file editing are SequenceFile.RemoveSequence, SequenceFile.DeleteSequence, SequenceFile.SequenceNameExists, Sequence.RemoveStep, Sequence.DeleteStep, and Sequence.StepNameExists.

Parent topic:

Writing an Application with the TestStand Engine API

<!--NI_TOPIC bundle=teststand path=managing-step-type-version-compatibility.html language=enus -->
## TOPIC 00544: Managing Step Type Version Compatibility

- bundle_id: `teststand`
- source_path: `managing-step-type-version-compatibility.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/managing-step-type-version-compatibility.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: When you modify custom step types, consider the following caveats so you can avoid making changes that might jeopardize compatibility. Ensure that previously configured steps behave properly when you execute the steps using the modified custom step type. Ensure that new step instances based on the m

### Managing Step Type Version Compatibility

When you modify custom step types, consider the following caveats so you can avoid making changes that might jeopardize compatibility.

- Ensure that previously configured steps behave properly when you execute the steps using the modified custom step type.
- Ensure that new step instances based on the modified step type behave properly when you save a sequence file to an earlier version of TestStand that uses the original custom step type.
- Do not rename custom step type properties or change the functionality of existing properties. For example, when you have an existing property that performs a specified task and you later decide you want the property to do something completely different in a future instance of the step type, you break compatibility.
- When you create new properties, provide default values that preserve the functionality of previously created steps.
- When you extend enumerated values, do not change the functionality of previously used values.

Parent topic:

Custom Step Types

<!--NI_TOPIC bundle=teststand path=managing-type-revisions.html language=enus -->
## TOPIC 00545: Managing Type Revisions

- bundle_id: `teststand`
- source_path: `managing-type-revisions.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/managing-type-revisions.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: When you load a file that contains a type definition and another type definition with the same name already exists in memory, TestStand compares the two type definitions, including all the built-in and custom subproperties in the types. If the types are identical, TestStand continues to use the type

### Managing Type Revisions

When you load a file that contains a type definition and another type definition with the same name already exists in memory, TestStand compares the two type definitions, including all the built-in and custom subproperties in the types.

If the types are identical, TestStand continues to use the type in memory. If the types are not identical, TestStand attempts to resolve the type conflict. TestStand automatically selects the type with the latest version number when all of the following conditions exist:

- The version numbers of the types are different
- The PropTypeFlags_IsModifiedType type flag is disabled for both types
- The Always prompt the user to resolve the conflict option on the Version tab of the Step Type Properties dialog box or on the Version tab of the Type Properties dialog box is disabled for both types
- The Allow Automatic Type Conflict Resolution option on the File tab of the Station Options dialog box does not restrict automatic type conflict resolution in this situation

If TestStand cannot automatically resolve a type conflict, TestStand either launches the Type Conflict in File dialog box or, if TestStand is loading a file an execution calls, returns a run-time error.

Note

The Type Conflict in File dialog box prompts you to resolve the conflict. You can select to use or rename the type currently loaded in memory or use or rename the type in the file you are attempting to load. When you select to use one of the two versions of the type, TestStand converts all instances of the type to match the type version you select. If you rename one of the two versions of the type, TestStand modifies the instances of the type in memory that refer to the version of the type you select to refer to the renamed version.

Note

Parent topic:

Type Concepts

<!--NI_TOPIC bundle=teststand path=managing-users.html language=enus -->
## TOPIC 00546: Managing Users

- bundle_id: `teststand`
- source_path: `managing-users.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/managing-users.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the TestStand User Manager to maintain the list of users, user names, user passwords, user privileges, groups, group privileges, and members of groups. TestStand can limit the functionality of the TestStand Sequence Editor and User Interfaces depending on the privilege settings you specify in th

### Managing Users

Use the TestStand User Manager to maintain the list of users, user names, user passwords, user privileges, groups, group privileges, and members of groups. TestStand can limit the functionality of the TestStand Sequence Editor and User Interfaces depending on the privilege settings you specify in the user manager for the current user and the groups to which the user belongs.

By default, the sequence editor and the user interfaces launch the Login dialog box when you launch TestStand. You can customize the default login/logout implementation.

Use the User Manager tab of the Station Options dialog box to configure TestStand to enforce user privileges and to specify the location of the user manager configuration file.

Note

Parent topic:

Fundamentals

Related concepts:

- Modifying Front-End Callbacks
- Creating and Deleting Users Using API

<!--NI_TOPIC bundle=teststand path=managing-versioned-and-non-versioned-files.html language=enus -->
## TOPIC 00547: Managing Versioned and Non-Versioned Files

- bundle_id: `teststand`
- source_path: `managing-versioned-and-non-versioned-files.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/managing-versioned-and-non-versioned-files.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Versioned files are binary files that include a version resource, such as executables, DLLs, or LabVIEW packed project libraries. Non-versioned files are text files, such as .ini files, or binary files that do not include a version resource, such as VIs. MSI-based Installers use the version resource

### Managing Versioned and Non-Versioned Files

Versioned files are binary files that include a version resource, such as executables, DLLs, or LabVIEW packed project libraries. Non-versioned files are text files, such as .ini files, or binary files that do not include a version resource, such as VIs.

MSI-based Installers use the version resource of a file to determine what action to perform when the file already exists on the computer, as shown in the following table.

| Version Resource of MSI-based Installer File | Version Resource of File on Computer | Action MSI-based Installer Performs |
| --- | --- | --- |
| Later | Earlier | Overwrites file on computer |
| Earlier | Later | Does not install the file |
| Any | None | Overwrites file on computer |
| None | Any | Does not install the file |
| None | None | Uses creation and modified dates |

If you update the version of a file, you do not have to use the Force File to Install option on the Distributed Files tab of the TestStand Deployment Utility to include the file in the deployment.

MSI-based Installers evaluate the creation and modification dates of non-versioned files to determine what action to perform when the file already exists on the computer, as shown in the following table. Right-click a file in Microsoft Windows Explorer and select Properties from the context menu to view the modified and created dates.

| Modified Date of File on Computer | Created Date of File on Computer | Action MSI-based Installer Performs |
| --- | --- | --- |
| Later than created date | — | Does not install the file (prevents overwriting changes made to the file after original installation) |
| — | Later than modified date | Overwrites file on computer |
| Same as created date | Same as modified date | Overwrites file on computer |

Parent topic:

Building a Customized MSI-based Installer

Related concepts:

- Organizing Test Program Files with LabVIEW Packed Project Libraries

<!--NI_TOPIC bundle=teststand path=managing-versions-of-net-to-use-with-teststan.html language=enus -->
## TOPIC 00548: Managing Versions of .NET to Use with TestStand

- bundle_id: `teststand`
- source_path: `managing-versions-of-net-to-use-with-teststan.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/managing-versions-of-net-to-use-with-teststan.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The .NET Adapter uses .NET 8 to call assemblies, and the TestStand Sequence Editor and the example .NET user interfaces target .NET 8. Managing Versions of .NET to Use with TestStand 2023 Q4 and EarlierIn TestStand 2023 Q4 and earlier, the .NET Adapter uses the .NET Framework Common Language Runtime

### Managing Versions of .NET to Use with TestStand

The .NET Adapter uses .NET 8 to call assemblies, and the TestStand Sequence Editor
 and the example .NET user interfaces target .NET 8.

#### Managing Versions of .NET to Use with TestStand
 2023 Q4 and Earlier

In TestStand 2023 Q4 and earlier, the .NET Adapter
 uses the .NET Framework Common Language Runtime (CLR) version 4.0 to call
 assemblies, and the TestStand Sequence Editor and the example .NET user interfaces
 target .NET Framework 4.0.

.config

Note

For example, to specify that the sequence editor can load legacy C++/CLI
 assemblies, create in the <TestStand>\Bin directory a file
 named seqedit.exe.config that contains the following information:

<?xml version="1.0"?>

<configuration>

<startup
 useLegacyV2RuntimeActivationPolicy="true">

<supportedRuntime
 version="v4.0" />

</startup>

</configuration>

When you set the useLegacyV2RuntimeActivationPolicy="true"
 attribute to true, you force an application that uses the .NET
 Framework CLR 4.0 to load all legacy assemblies in the .NET Framework CLR 4.0,
 including legacy C++/CLI assemblies, but you also disable the ability to run
 multiple versions of the .NET Framework CLR in-process and side-by-side. Refer to
 Microsoft MSDN documentation for more information about using this configuration
 option.

Parent topic:

.NET Adapter

Related concepts:

- .NET Adapter

<!--NI_TOPIC bundle=teststand path=manual-migrate-result-options-any.html language=enus -->
## TOPIC 00549: Manually Migrating Result Processing Options from Any Version of TestStand

- bundle_id: `teststand`
- source_path: `manual-migrate-result-options-any.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/manual-migrate-result-options-any.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `task`
- source_description: Complete the following steps to manually migrate result processing options from TestStand 2010 SP1 or earlier for use with the process models in the current version of TestStand. Copy the TestStandModelReportOptions.ini and TestStandDatabaseOptions.ini files from the Cfg directory of TestStand 2010

### Manually Migrating Result Processing Options
 from Any Version of TestStand

Complete the following steps to manually
 migrate result processing options from TestStand 2010 SP1 or earlier for use with the
 process models in the current version of TestStand.

1. Copy the TestStandModelReportOptions.ini and
 TestStandDatabaseOptions.ini files from the
 Cfg directory of TestStand 2010 SP1 or earlier to the
 <TestStand Application Data>\Cfg directory of the
 current version TestStand.
2. Rename TestStandDatabaseOptions.ini to
 TestStandDatabaseSchemas.ini. 
 Note This procedure
 is not supported for migrating TestStand 4.0 or earlier default database
 schemas. If you want to use TestStand 4.0 or earlier default database
 schemas in TestStand 2012 or later, click the Reload NI
 Schemas button on the Schemas tab of the Database Options
 dialog box to launch the Reload NI Schemas dialog box, and click the
 2.x to 4.0 button to reload the default database
 schemas from TestStand 4.0 or earlier.
3. Use the Legacy Model Switcher tool with the command-line argument
 /migration to migrate the report
 options and database options from legacy TestStand 2010 process models to the
 TestStand 2012 or later process models. Confirm that you have enabled the
 options to migrate report and database options from the legacy models. 
 Note The /migration command-line
 argument disables the type version checking the Legacy Model Switcher tool
 ordinarily performs. This automatically merges the types in the report and
 database options in the equivalent legacy TestStand 2010 process models with
 the types in the current TestStand process models. NI does not recommend
 migrating types that were not originally shipped with TestStand because
 doing so can lead to loss of data.
4. Launch the TestStand Sequence Editor.
5. Select Configure»Result Processing to launch the
 Result Processing dialog box.
6. Enable the Show More Options option.
7. Verify that the Active Configuration ring control
 specifies Options from Legacy Models.

To migrate result processing options to the
 equivalent legacy TestStand 2010 process models, complete only step 1. However, NI does
 not recommend using the equivalent legacy TestStand 2010 process models unless you
 encounter an incompatibility in an existing test system when you use the current
 TestStand process models or other circumstances prevent you from using the current
 TestStand process models.

Parent topic:

Migrating to the Current Version of TestStand

Related concepts:

- Process Model Changes in TestStand 2012 or Later and the Migration Utility
- TestStand Migration Utility

Related information:

- Command Line Arguments

<!--NI_TOPIC bundle=teststand path=manually-adding-or-removing-files-to-or-from.html language=enus -->
## TOPIC 00550: Manually Adding or Removing Files to or from Deployments

- bundle_id: `teststand`
- source_path: `manually-adding-or-removing-files-to-or-from.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/manually-adding-or-removing-files-to-or-from.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: When you specify the files to include in the deployment on the System Source tab of the TestStand Deployment Utility, the deployment utility automatically includes all the files and the statically referenced dependencies in the deployment. You must manually add to the deployment dynamically referenc

### Manually Adding or Removing Files to or from Deployments

When you specify the files to include in the deployment on the System Source tab of the TestStand Deployment Utility, the deployment utility automatically includes all the files and the statically referenced dependencies in the deployment. You must manually add to the deployment dynamically referenced files, implicitly referenced files, and . You can also filter and exclude files from the deployment.

#### Dynamic References

The deployment utility automatically resolves statically referenced files, which are files that have a fixed path, but cannot resolve dynamically referenced files, which are files you specify using an expression. Files you specify using an expression might evaluate to different values depending on the values of other variables during execution because TestStand evaluates expression values only at run time after specifying the values of dependent variables. You must manually add dynamically referenced files to the TestStand workspace or to the directory from which you create the deployment. Do not add files that TestStand, the operating system, or other applications install.

The following are common sources of dynamically referenced files:

- Sequence Call steps that use an expression to specify the sequence file path
- Property Loader steps that use an expression to specify the path of the file that contains the property values to use
- VIs that use the Open VI Reference function to load other VIs
- DLLs that dynamically load other DLLs
- .NET assemblies that dynamically load other assemblies

#### Implicit References

Implicitly referenced files are files that are not code module dependencies or referenced explicitly but that are required for the test system to execute correctly. For example, a test system can include an external calibration file in the same directory as the user interface, but no TestStand steps or code modules reference the calibration file. Common implicitly referenced files include documentation, images, and operator instructions. You must manually add implicitly referenced files to the TestStand workspace or to the directory from which you create the deployment.

#### Servers

The deployment
 utility does not automatically deploy .NET or ActiveX/COM code modules because not
 enough information exists to include all the necessary files to ensure that the .NET
 assembly or ActiveX/COM server runs correctly. For example, the deployment utility
 can determine that a step automates Microsoft Excel as a server using the ActiveX
 steps in TestStand, but the deployment utility cannot determine which files in the
 Microsoft Office directory Excel requires to execute correctly. To ensure that the
 test system executes successfully on the test station computer, use custom commands
 to run the installer for the code module on the test station computer or add the
 code module and required support files to the TestStand workspace from which you
 create the deployment.

NI recommends that you use an installer for the code
 module and its dependencies to install the required files on the test station
 computer instead of including the files in the installer you build with the
 deployment utility because the existing installer might perform additional actions
 required for the correct functioning of the file at install time, such as creating
 registry keys, running other installers, or installing and starting required
 Microsoft Windows services.

Parent topic:

Creating Deployments

Related concepts:

- Filtering and Excluding Files
- Using a TestStand Workspace File to Create a Deployment
- Using a Directory to Create a Deployment
- Using Custom Commands to Execute Third-Party Installers

<!--NI_TOPIC bundle=teststand path=manually-select-process-models.html language=enus -->
## TOPIC 00551: Manually Selecting Process Models

- bundle_id: `teststand`
- source_path: `manually-select-process-models.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/manually-select-process-models.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `task`
- source_description: Complete the following steps if you want to manually select a process model to use for a test station: Select Configure»Station Options to launch the Station Options dialog box. Click the Model tab. Use the Station Model control to browse to the equivalent legacy TestStand 2010 process model you wan

### Manually Selecting Process Models

1. Complete the following steps if you want to manually select a process model to
 use for a test station:
  1. Select Configure»Station Options to launch the
 Station Options dialog box.
  2. Click the Model tab.
  3. Use the Station Model control to browse to the
 equivalent legacy TestStand 2010 process model you want to use located
 in
 <TestStand>\Components\Models\TestStandModels\TestStand
 2010 Process Models (Legacy).
2. Complete the following steps if you want to manually select a process model to
 use for a sequence file:
  1. Select Edit»Sequence File Properties to launch
 the Sequence File Properties dialog box.
  2. Click the Advanced tab.
  3. Select Require Specific Model in the
 Model Option control.
  4. Use the Model File control to browse to the
 equivalent legacy TestStand 2010 process model you want to use.

Parent topic:

Process Model Architecture

Related concepts:

- Search Directories

<!--NI_TOPIC bundle=teststand path=mapping-labwindows-cvi-parameters.html language=enus -->
## TOPIC 00552: Mapping LabWindows/CVI Parameters

- bundle_id: `teststand`
- source_path: `mapping-labwindows-cvi-parameters.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/mapping-labwindows-cvi-parameters.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: When you load a new code module prototype, the LabWindows/CVI Adapter uses the following guidelines, in order of priority, to copy the configured argument values for parameters from the old prototype to the new prototype. Map arguments based on parameter name and compatible type. Map arguments based

### Mapping LabWindows/CVI Parameters

When you load a new code module prototype, the LabWindows/CVI Adapter uses the following guidelines, in order of priority, to copy the configured argument values for parameters from the old prototype to the new prototype.

1. Map arguments based on parameter name and compatible type.
2. Map arguments based on position and compatible type.

Parent topic:

LabWindows/CVI Adapter

Related concepts:

- Search Directories

<!--NI_TOPIC bundle=teststand path=mapping-parameters.html language=enus -->
## TOPIC 00553: Module Adapter Parameter Mapping Guidelines

- bundle_id: `teststand`
- source_path: `mapping-parameters.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/mapping-parameters.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: When you load a new prototype for any adapter, each adapter uses the following guidelines to copy the configured argument values for parameters from the old prototype to the new prototype: Adapter Rules (in Order of Priority) for Mapping Arguments LabVIEW Map arguments based on parameter name and co

### Module Adapter Parameter Mapping
 Guidelines

When you load a new prototype for any adapter, each adapter uses the following guidelines to copy the configured argument values for parameters from the old prototype to the new prototype:

| Adapter | Rules (in Order of Priority) for Mapping Arguments |
| --- | --- |
| LabVIEW | Map arguments based on parameter name and compatible type. Map arguments based on connector pane position and compatible type. Map arguments based on compatible type, same input or output direction, and matching the prefix of the old parameter name with the new parameter name. Map arguments based on compatible type, same input or output direction, and matching the prefix of the new parameter name with the old parameter name. Use the map the step type specifies, if available. |
| LabWindows/CVI | Map arguments based on parameter name and compatible type. Map arguments based on position and compatible type. |
| C/C++ DLL | Does not specify any parameters or mapping rules. |
| .NET |  |
| ActiveX/COM |  |
| Sequence |  |
| HTBasic |  |
| Python Adapter | Map arguments based on parameter name and position. |

Parent topic:

Module Adapters

Related concepts:

- Module Adapters

<!--NI_TOPIC bundle=teststand path=maximizing-test-system-throughput.html language=enus -->
## TOPIC 00554: Maximizing Test System Throughput

- bundle_id: `teststand`
- source_path: `maximizing-test-system-throughput.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/maximizing-test-system-throughput.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Automated test systems are usually designed to maximize throughput by minimizing the time required to verify a unit under test (UUT). Test system architects spend a considerable amount of time optimizing test system performance. In a typical test system, the amount of time required for report genera

### Maximizing Test System Throughput

Automated test systems are usually designed to maximize throughput by minimizing the time required to verify a unit under test (UUT). Test system architects spend a considerable amount of time optimizing test system performance. In a typical test system, the amount of time required for report generation depends on a number of factors, including available resources (processor and memory), the format of the report to generate, the number of results, and additional data to log.

#### Recommended Report
 Options

NI benchmarks demonstrate the following patterns based on the
 report format, the number of step results or the size of the data sets you log, the
 number of cores in the test computer, and other options you configure in the Report
 Options dialog box:

- When you log 500 or fewer step results on a single- or multi-core computer,
 ASCII reports have the least negative impact to throughput, and XML reports have
 the most negative impact to throughput.
- When you log more than 500 step results or large data sets on a single- or
 multi-core computer, TSR reports have the least negative impact to throughput,
 and XML reports have the most negative impact to throughput.
- Asynchronous report generation on a single-core computer does not improve
 throughput, except in cases where a substantial amount of sequence execution
 time is spent waiting on operations that do not use the CPU, such as instrument
 I/O.
- Asynchronous report generation on a multi-core computer improves throughput for
 all report formats.

The following table summarizes the recommended options you configure in the
 Report Options dialog box, depending on your system configuration, when you optimize
 for test system throughput:

| Report Option | Single-Core Computers | Multi-Core Computers |  |  |
| --- | --- | --- | --- | --- |
| Value for ≤ 500 Step Results | Value for ≥ 500 Step Results | Value for ≤ 500 Step Results | Value for ≥ 500 Step Results |  |
| Format | ASCII, TSR*, ATML, HTML, XML (best to worst) | TSR, ASCII, ATML, HTML, XML (best to worst) | ASCII, ATML, TSR, HTML, XML (best to worst) | TSR, ASCII, ATML, HTML, XML (best to worst) |
| Asynchronous | False | False | True | True |
| On-the-Fly Report | False | False | False | False |
| Only Display Latest Results | False | False | False | False |

Note

#### Tradeoffs

Consider the
 impact to the following requirements when you optimize for test system
 throughput:

- Minimize report file size
- Include all necessary report content
- Interoperate with other processes and systems
- Support post-failure information recovery
- Generate reports immediately for the current UUT before testing the next
 UUT
- Generate multiple reports for each UUT
- Generate and view the report during test sequence execution

Parent topic:

Choosing the Appropriate Report Generation Strategy

Related concepts:

- Minimizing Report File Size
- Including All Necessary Report Content
- Interoperating with Other Processes and Systems
- Supporting Post-Failure Information Recovery
- Generating the Report for the Current UUT before Testing the Next UUT
- Generating Multiple Reports for Each UUT
- Generating and Viewing the Report during Test Sequence Execution
- Choosing the Appropriate Report Generation Strategy

<!--NI_TOPIC bundle=teststand path=mds-result-processor.html language=enus -->
## TOPIC 00555: Measurement Data Service Data Store

- bundle_id: `teststand`
- source_path: `mds-result-processor.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/mds-result-processor.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Measurement Data Service (MDS) Data Store collects and publishes test results and metadata. Metadata includes input parameters, output parameters, and system information. The MDS Data Store stores test data in a structured format for easy access and long-term tracking. You can use the MDS API fo

### Measurement Data Service Data Store

The Measurement Data Service (MDS) Data Store collects and publishes test results and
 metadata.

Metadata includes input parameters, output parameters, and system information. The MDS
 Data Store stores test data in a structured format for easy access and long-term
 tracking.

You can use the MDS API for Python or LabVIEW to query historical data.

The MDS Data Store integrates with NI Nigel™ AI, an AI assistant that
 uses natural language to query historical test results. Using the data from the MDS Data
 Store, Nigel can help teams to spot trends, review past performance, and make informed
 decisions without writing complex queries.

Parent topic:

Generating and Customizing TestStand Reports

Related tasks:

- Logging Metadata for Analysis

Related information:

- Python API Example
- LabVIEW API Example

<!--NI_TOPIC bundle=teststand path=measure-efficiency.html language=enus -->
## TOPIC 00556: Measure Efficiency

- bundle_id: `teststand`
- source_path: `measure-efficiency.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/measure-efficiency.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Purpose This example demonstrates how to use IO Configuration step types to communicate with the instrument for measuring efficiency. Example File Location <TestStand Public>\Examples\Interfacing with Hardware\InstrumentStudio\Efficiency\Efficiency.seq Highlighted Features IO Configuration Step Type

### Measure Efficiency

#### Purpose

This example demonstrates how to use IO Configuration step types to communicate with the instrument for measuring efficiency.

#### Example File
 Location

<TestStand
 Public>\Examples\Interfacing with
 Hardware\InstrumentStudio\Efficiency\Efficiency.seq

#### Highlighted Features

- IO Configuration Step Types
- Sweep Loop Step Type

#### Major API

None

#### Prerequisites

Complete the following steps before executing this example on 64-bit TestStand.

1. Install the following NI software: Note MAX and InstrumentStudio are included by default when you install NI-DCPower.MI Device Support for TestStand is included by default with NI-DCPower only when TestStand is already installed. You can install it separately with NI Package Manager once TestStand is installed.
  - LabVIEW (64-bit)
  - NI-DCPower
  - Measurement & Automation Explorer (MAX)
  - InstrumentStudio 2021 or later
  - MI Device Support for TestStand
2. Complete the following setup:
  - In TestStand, configure the LabVIEW Adapter to use the LabVIEW Development System.
  - Create a simulated device in MAX. Right click Devices and Interfaces»Create New »Simulated NI-DAQmx Device or Modular Instrument»Finish .
  - In the Create Simulated NI-DAQmx Device dialog, expand the node for Power Supplies and select the NI PXIe-4143.
  - For the newly added device, update the name of the device in MAX to dev2 and save the device.

#### How to Use This Example

Complete the following steps to use this example.

1. On the Steps pane of the MainSequence sequence, review the steps in the Setup step group.
  - The Get Sequence File Directory step gets the directory of the example sequence file.
  - The Identify CSV Output file step creates the output stream in the sequence file directory.
  - The Create DC Power Session and Apply Configuration step creates a session (dev2) in LabVIEW.
2. On the Steps pane, review the steps in the Main step group.
  - The Sweep DC Power - Current Vout step sweeps on the voltage values for the session (dev2) on channel 0 and the current values for the session (dev2) on channel 1.
  - The Measure Current And Voltage - Channel0 step measures the current and voltage for channel 0.
  - The Measure Current And Voltage - Channel1 step measures the current and voltage for channel 1.
  - The Calculate Efficiency step calculates the efficiency based on the measured voltage and current values against the values set in the preceding two steps.
3. On the Steps pane, review the steps in the Cleanup step group.
  - The Close Sessions step closes the sessions which have been opened in the current sequence.
4. Select Execute»Single Pass to run the sequence.
5. The voltage, current, and efficiency values are logged to <TestStand Public>\Examples\Interfacing with Hardware\InstrumentStudio\Efficiency\output.csv .

Parent topic:

InstrumentStudio

Related concepts:

- TestStand Directory Structure
- Step Groups

<!--NI_TOPIC bundle=teststand path=measure-quiescent-current.html language=enus -->
## TOPIC 00557: Measure Quiescent Current

- bundle_id: `teststand`
- source_path: `measure-quiescent-current.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/measure-quiescent-current.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Purpose This example demonstrates how to use IO Configuration step types to communicate with the instrument for measuring quiescent current. Example File Location <TestStand Public>\Examples\Interfacing with Hardware\InstrumentStudio\Quiescent Current\QuiescentCurrent.seq Highlighted Features IO Con

### Measure Quiescent Current

#### Purpose

This example demonstrates how to use IO Configuration step types to communicate with the instrument for measuring quiescent current.

#### Example File
 Location

<TestStand
 Public>\Examples\Interfacing with
 Hardware\InstrumentStudio\Quiescent
 Current\QuiescentCurrent.seq

#### Highlighted Features

- IO Configuration Step Types
- Sweep Loop Step Type

#### Major API

None

#### Prerequisites

Complete the following steps before executing this example on 64-bit TestStand.

1. Install the following NI software: Note MAX and InstrumentStudio are included by default when you install NI-DCPower.MI Device Support for TestStand is included by default with NI-DCPower only when TestStand is already installed. You can install it separately with NI Package Manager once TestStand is installed.
  - LabVIEW (64-bit)
  - NI-DCPower
  - Measurement & Automation Explorer (MAX)
  - InstrumentStudio 2021 or later
  - MI Device Support for TestStand
2. Complete the following setup:
  - In TestStand, configure the LabVIEW Adapter to use the LabVIEW Development System.
  - Create a simulated device in MAX. Right click Devices and Interfaces»Create New »Simulated NI-DAQmx Device or Modular Instrument»Finish .
  - In the Create Simulated NI-DAQmx Device dialog, expand the node for Power Supplies and select the NI PXIe-4143.
  - For the newly added device, update the name of the device in MAX to dev2 and save the device.

#### How to Use This Example

Complete the following steps to use this example.

1. On the Steps pane of the MainSequence sequence, review the steps in the Setup step group.
  - The Get Sequence File Directory step gets the directory of the example sequence file.
  - The Identify CSV Output file step creates the output stream in the sequence file directory.
  - The Create DC Power Session and Apply Configuration step creates a session (dev2) in LabVIEW.
2. On the Steps pane, review the steps in the Main step group.
  - The Sweep Instrument step sweeps on the voltage values for the session (dev2).
  - The Measure Current And Voltage step measures the current and voltage.
3. On the Steps pane, review the steps in the Cleanup step group.
  - The Close Sessions step closes the sessions which have been opened in the current sequence.
4. Select Execute»Single Pass to run the sequence.
5. The voltage, current, efficiency values are logged to <TestStand Public>\Examples\Interfacing with Hardware\InstrumentStudio\Quiescent Current\output.csv .

Parent topic:

InstrumentStudio

Related concepts:

- TestStand Directory Structure
- Step Groups

<!--NI_TOPIC bundle=teststand path=message-popup-step-type-automatically-dismiss.html language=enus -->
## TOPIC 00558: Message Popup Step Type - Automatically Dismissing

- bundle_id: `teststand`
- source_path: `message-popup-step-type-automatically-dismiss.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/message-popup-step-type-automatically-dismiss.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Purpose This example demonstrates the following two approaches for creating Message Popup steps that automatically dismiss after a condition is met: Dismissing the message after a set amount of time Dismissing the message after a set condition is met, such as detecting that a new UUT has been attach

### Message Popup Step Type - Automatically Dismissing

#### Purpose

This example demonstrates the following two approaches for creating Message Popup steps that automatically dismiss after a condition is met:

- Dismissing the message after a set amount of time
- Dismissing the message after a set condition is met, such as detecting that a new UUT has been attached to the test fixture

#### Example File
 Location

<TestStand
 Public>\Examples\Built-In Step Types\Message Popup Step
 Type\Message Popup Step Type - Automatically
 Dismissing.seq

#### Highlighted Features

- Message Popup Timeout
- Creating New Executions

#### Major API

Execution.Terminate

#### Prerequisites

None

#### How to Use This Example

Complete the following steps to review the sequences and steps in this example:

1. Select the UUT Detected step. In the Step Settings pane, select the Text and Buttons tab.
2. Observe that Button 1 is specified in the Timeout Button field, and the Time to wait field is set to three seconds. This setting configures the step to automatically select Button 1 and dismiss the message box after three seconds.
3. Select the Prompt for User Action sequence. Observe that this sequence creates a new execution to launch the dialog. The sequence will dismiss the dialog by terminating the execution. Note The Launch Dialog in new Execution step stores a reference to the new execution in the Locals.messageExecution variable using the Sequence Call Advanced Settings dialog box.
4. After launching the dialog, the sequence simulates polling for a UUT. In a real application, this section would typically call a code module which returns once the condition is met
5. Once the condition is met, the Execution.Terminate method of the TestStand API terminates the new execution, thereby dismissing the message popup.

Complete the following steps to run the example:

1. Select Execute»Single Pass to run the sequence.
2. Observe that the first message popup dismisses after three seconds.
3. Observe that the second message popup step dismisses once the Check for UUT condition is met.

Parent topic:

Examples for Built-In Step Types

Related concepts:

- TestStand Directory Structure
- Executions

<!--NI_TOPIC bundle=teststand path=message-popup-step-type-get-user-input.html language=enus -->
## TOPIC 00559: Message Popup Step Type - Get User Input

- bundle_id: `teststand`
- source_path: `message-popup-step-type-get-user-input.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/message-popup-step-type-get-user-input.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Purpose This example demonstrates how to use Message Popup steps to obtain user input using the following two methods: Using Buttons Using a Text Field The example determines what actions to take based on user selections. Example File Location <TestStand Public>\Examples\Built-In Step Types\Message

### Message Popup Step Type - Get User Input

#### Purpose

This example demonstrates how to use Message Popup steps to obtain user input using the following two methods:

- Using Buttons
- Using a Text Field

The example determines what actions to take based on user selections.

#### Example File
 Location

<TestStand
 Public>\Examples\Built-In Step Types\Message Popup Step
 Type\Message Popup Step Type - Get User Input.seq

#### Highlighted Features

- Case steps
- Error handling
- Message Popup steps
- Preconditions
- Select steps

#### Major API

None

#### Prerequisites

None

#### How to Use This Example

Complete the following steps to review the steps in the Buttons sequence. This sequence demonstrates how you can use a message popup step to prompt a user for input using buttons.

1. Select the Board Test Selection – Buttons step. In the Step Settings pane, select the Text and Buttons tab.
2. Observe that the button names are specified in the Button 1 through Button 5 fields. The message popup step will display all buttons with specified names.
3. The example uses a Select statement to respond to the user selection. The Select statement accesses the RunState.Sequence.Main["Board Test Selection - Buttons"].Result.ButtonHit property to check the button the user chooses.

Complete the following steps to review the steps in the PromptForInput sequence. This sequence demonstrates how you can use a message popup step to prompt a user for input using a response text box.

1. Select the Select Board to Test - Text Field step. In the Step Settings pane, select the Options tab.
2. Observe that the Enable Response Text Box option is enabled. This option adds a response text box to the message popup to receive user input.
3. The example uses a Select statement to respond to the user selection. The Select statement uses the expression Val(RunState.Sequence.Main["Select Board To Test - Text Field"].Result.Response) to check the response the user enters.
4. If an invalid value is entered, the default case notifies the user of the response. This step triggers a post action, in which the Select Board To Test - Text Field step executes again to allow the user to enter a valid response. Note The Val() expression function converts the text response string to a number.

Complete the following steps to run the example:

1. Select Execute»Single Pass to run the sequence.
2. When prompted, click a button or enter a value. Notice that the sequence responds differently based on the input you provide.

Parent topic:

Examples for Built-In Step Types

Related concepts:

- TestStand Directory Structure

<!--NI_TOPIC bundle=teststand path=microsoft-ado-ole-db-and-odbc-database-techno.html language=enus -->
## TOPIC 00560: Microsoft ADO, OLE DB, and ODBC Database Technologies

- bundle_id: `teststand`
- source_path: `microsoft-ado-ole-db-and-odbc-database-techno.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/microsoft-ado-ole-db-and-odbc-database-techno.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: TestStand uses Microsoft ActiveX Data Objects (ADO) database client technology. ADO, which is built on top of the Object Linking and Embedding Database (OLE DB), is one of several database interface technologies integrated into Microsoft Windows operating systems. Applications that use ADO, such as

### Microsoft ADO, OLE DB, and ODBC Database Technologies

TestStand uses Microsoft ActiveX Data Objects (ADO) database client technology. ADO, which is built on top of the Object Linking and Embedding Database (OLE DB), is one of several database interface technologies integrated into Microsoft Windows operating systems.

Applications that use ADO, such as TestStand, use the OLE DB interfaces indirectly. The OLE DB layer interfaces to databases directly through a specific OLE DB provider for the DBMS or through a generic Open Database Connectivity (ODBC) provider, which interfaces to a specific ODBC driver for the DBMS. The following figure shows the high-level relationships between TestStand and components of Windows database technologies.

[IMAGE alt='image' src='GUID-26176BC9-CCC3-48CC-9BF9-F7F75EED8362-a5.svg']

Refer to the Microsoft website at www.microsoft.com for more information about database technologies for Windows operating systems.

Parent topic:

TestStand Database Fundamentals

Related information:

- Microsoft Home Page

<!--NI_TOPIC bundle=teststand path=microsoft-visual-c-and-other-c-environments.html language=enus -->
## TOPIC 00561: Microsoft Visual C++ and Other C++ Environments

- bundle_id: `teststand`
- source_path: `microsoft-visual-c-and-other-c-environments.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/microsoft-visual-c-and-other-c-environments.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Microsoft Visual C++ code modules can call the LabWindows/CVI instrument driver, SessionMgr.fp, or use the compiler ActiveX support to call the Session Manager server directly.

### Microsoft Visual C++ and Other C++ Environments

Microsoft Visual C++ code modules can call the LabWindows/CVI instrument driver, SessionMgr.fp, or use the compiler ActiveX support to call the Session Manager server directly.

Parent topic:

Using Instrument Sessions in a Development Environment

<!--NI_TOPIC bundle=teststand path=microsoft-windows-merge-modules.html language=enus -->
## TOPIC 00562: Microsoft Windows Merge Modules

- bundle_id: `teststand`
- source_path: `microsoft-windows-merge-modules.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/microsoft-windows-merge-modules.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Microsoft Windows Installer technology uses merge module (.msm) files as a standard method for developers to specify logic among applications and to deliver shared code, files, resources, registry entries, and other components. Merge module files contain the database tables Windows Installer databas

### Microsoft Windows Merge Modules

Microsoft Windows Installer technology uses merge module (.msm) files as a
 standard method for developers to specify logic among applications and to deliver
 shared code, files, resources, registry entries, and other components. Merge module
 files contain the database tables Windows Installer database files require to
 install a component. You cannot install a merge module file directly. You must
 incorporate the merge module file into a Windows Installer database file. Because of
 this requirement, using merge module files with Windows Installer database files to
 install interdependent NI products can be problematic for the following reasons:

- Multiple merge module files can contain conflicting table entries, which prevents you from
 incorporating the merge module files into a single Windows Installer database
 file. Using the NI MSI-based installer architecture, NI distributions avoid this
 issue by using parts based on Windows Installer database files, which use
 independent table entries.
- Merge module files duplicate the content for every package that includes the merge module files,
 which can increase the amount of space needed for complex distributions. Using
 the NI MSI-based installer architecture, NI distributions avoid this issue by
 reusing parts in multiple products.

Parent topic:

Relationship of NI MSI-based Installer Architecture and Microsoft Windows Installer Technology

Related concepts:

- Relationship of NI MSI-based Installer Architecture and Microsoft Windows Installer Technology
- NI MSI-based Installer Architecture

<!--NI_TOPIC bundle=teststand path=migrate-ui-to-net.html language=enus -->
## TOPIC 00563: Migrating User Interfaces to .NET Core

- bundle_id: `teststand`
- source_path: `migrate-ui-to-net.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/migrate-ui-to-net.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `reference`
- source_description: Consider the following when migrating custom user interfaces to .NET Core: Ensure that your custom UI applications work correctly on high-DPI monitors by making them DPI-unaware. Follow the below methods to disable DPI awareness for your UI in different programming languages: For custom UIs develope

### Migrating User Interfaces to .NET
 Core

Consider the following when migrating custom user interfaces to .NET Core:

1. Ensure that your custom UI applications work correctly on high-DPI monitors by
 making them DPI-unaware. Follow the below methods to disable DPI awareness for
 your UI in different programming languages:
  - For custom UIs developed in C#, make your application DPI-unaware by
 calling the Application.SetHighDpiMode method with the
 HighDpiMode.DpiUnaware parameter before running the
 application in your main method, like in the following
 example: [STAThread] 

private static void Main(string[] args) 

{ 
 // Set the application to be DPI-unaware 

 Application.SetHighDpiMode(HighDpiMode.DpiUnaware); 

 // Your application initialization code here 

}
  - For custom UIs created with other programming languages, you can make them DPI-unaware by
 setting the dpiAware flag to
 False in the application’s manifest
 file. <dpiAware xmlns="http://schemas.microsoft.com/SMI/2005/WindowsSettings">false</dpiAware>
2. Update the .csproj file or the runtime configuration file
 for your custom user interface to depend on
 Microsoft.NETCore.App ,
 Microsoft.WindowsDesktop.App , and
 Microsoft.AspNetCore.App . You can use the below format to
 include dependencies on these .NET
 runtimes. <ItemGroup>
<FrameworkReference 
 Include="Microsoft.WindowsDesktop.App" /> 
<FrameworkReference 
 Include="Microsoft.AspNetCore.App" />
</ItemGroup>
3. If you want to run LabVIEW with .NET in your custom UI, create a token file
 named <ApplicationName>.ini next to your application
 which includes the following
 content: [LVRT] 

DisableDotNetFrameworkSupport=True Note This file must be created for any TestStand application that uses
 LabVIEW.
4. For .NET applications, set the EnableUnsafeBinaryFormatterSerialization 
 property to true in the .csproj 
 file. <PropertyGroup>
 <EnableUnsafeBinaryFormatterSerialization>true</EnableUnsafeBinaryFormatterSerialization>
</PropertyGroup>

Parent topic:

Creating Custom User Interfaces

Related concepts:

- Calling LabVIEW VIs That Invoke .NET Code in TestStand

<!--NI_TOPIC bundle=teststand path=migrating-additional-results-from-the-client.html language=enus -->
## TOPIC 00564: Migrating Additional Results from the Client Sequence

- bundle_id: `teststand`
- source_path: `migrating-additional-results-from-the-client.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/migrating-additional-results-from-the-client.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: As in previous versions of TestStand, you can use the following techniques in TestStand 2012 or later to modify the data to include in the report or database: Directly modifying ResultList Using the Execution.AddExtraResult method If you implemented these techniques in the client sequence file, you

### Migrating Additional Results from the Client Sequence

As in previous versions of TestStand, you can use the following techniques in TestStand 2012 or later to modify the data to include in the report or database:

- Directly modifying ResultList
- Using the Execution.AddExtraResult method

If you implemented these techniques in the client sequence file, you can use the client sequence file directly in TestStand 2012 or later without modification. If you implemented these techniques in the process model components in TestStand 2010 or earlier, you cannot directly migrate the component to TestStand 2012 or later.

Parent topic:

Migrating Custom Results Processing Components

Related concepts:

- Result Collection
- Migrating Modifications to Built-in Result Processors

<!--NI_TOPIC bundle=teststand path=migrating-changes-to-settings-of-the-default.html language=enus -->
## TOPIC 00565: Migrating Changes to Settings of the Default Result Processors

- bundle_id: `teststand`
- source_path: `migrating-changes-to-settings-of-the-default.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/migrating-changes-to-settings-of-the-default.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The most common customizations to result processing involve modifying the configuration of the existing report generator or database logger. You typically use the Report Options or Database Options dialog boxes to implement these changes. TestStand 2010 or earlier saves these configuration changes t

### Migrating Changes to Settings of the Default Result Processors

The most common customizations to result processing involve modifying the configuration of the existing report generator or database logger. You typically use the Report Options or Database Options dialog boxes to implement these changes. TestStand 2010 or earlier saves these configuration changes to disk in the TestStandModelReportOptions.ini and TestStandDatabaseOptions.ini files, respectively. TestStand 2012 or later stores the configuration data for all result processing in a single ResultProcessing.cfg configuration file.

Use the TestStand Migration Utility to migrate configuration data in the .ini files of previous versions of TestStand to the TestStand 2012 or later .cfg file. You can also use the utility to migrate result processing settings from TestStand 2010 or later to TestStand 2012. If you are migrating from a version of TestStand earlier than TestStand 2010, you must manually migrate the result processing settings.

Parent topic:

Migrating Custom Results Processing Components

<!--NI_TOPIC bundle=teststand path=migrating-custom-process-model-components.html language=enus -->
## TOPIC 00566: Migrating Custom Process Model Components

- bundle_id: `teststand`
- source_path: `migrating-custom-process-model-components.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/migrating-custom-process-model-components.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: In addition to modifying the existing components of the process model, you might have added completely new functionality to the process models. When migrating these types of customizations, consider creating a new process model plug-in to implement the same functionality. If it is possible to implem

### Migrating Custom Process Model Components

In addition to modifying the existing components of the process model, you might have added
 completely new functionality to the process models. When migrating these types of
 customizations, consider creating a new process model plug-in to implement the same
 functionality. If it is possible to implement custom components as a process model
 plug-in, NI recommends you do so because it can greatly simplify migration of custom
 components in versions of TestStand later than 2012.

If you want to manage the configuration of the process model plug-in using a method other than the existing Results Processing dialog box, change the process model plug-in category. The Result Processing dialog box displays only process model plug-ins with a category (ModelPlugin.CategorySpecific.Name) set to ResultProcessor.

If you want the new process model plug-in to always execute independently of any configuration settings, configure the model plug-in as a plug-in add-on by storing the process model plug-in in the <TestStand Public>\Components\Models\ModelPlugins\Addons directory. Refer to the Dynamic Client Sequence File example in TestStand 2012 or later for an example of using a process model add-on.

Parent topic:

Migrating Process Model Customizations to TestStand 2012 or Later

Related concepts:

- Creating Process Model Plug-ins
- TestStand Directory Structure
- Dynamically Set the Client Sequence File

<!--NI_TOPIC bundle=teststand path=migrating-custom-result-processors.html language=enus -->
## TOPIC 00567: Migrating Custom Result Processors

- bundle_id: `teststand`
- source_path: `migrating-custom-result-processors.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/migrating-custom-result-processors.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: For applications with specific result processing requirements, you can implement a customized result processing model plug-in. Because the TestStand 2010 or earlier process models did not support process model plug-ins, creating a custom result processor was a difficult process. Using TestStand 2010

### Migrating Custom Result Processors

For applications with specific result processing requirements, you can implement a customized result processing model plug-in. Because the TestStand 2010 or earlier process models did not support process model plug-ins, creating a custom result processor was a difficult process. Using TestStand 2010 or earlier to accomplish this task required you to implement the result processing code and correctly integrate it into the built-in process models. The TestStand 2012 or later process model plug-in architecture decouples custom result processing code from the process model so you can focus on the result processing code itself rather than integration with the process model. The process model plug-in architecture includes the following benefits:

- Process model plug-in sequences automatically populate with process model data, which avoids the need for you to create parameters in each calling sequence to pass data
- With process model plug-ins, you can implement functionality at any point in an execution without modifying the process model files
- You can migrate process model plug-ins to future versions of TestStand with little to no modification

To migrate custom result processing changes to TestStand 2012 or later, create a new result processing model plug-in that contains the same functionality. To ease development, you can use the Result Processing dialog box to create a template process model plug-in that contains all the necessary entry points and data types.

After you create the process model plug-in, use the following table as a guide to migrate functionality into the correct process model plug-in sequences.

| Type of Functionality | Likely Location in TestStand 2010 or Earlier Process Model Files | Corresponding Process Model Plug-in Sequence |
| --- | --- | --- |
| Configuration dialog box for custom options | Configuration entry point in model sequence | Model Plugin — Configure Standard Options |
| Initialization (one time) | ProcessSetup Callback PreUUTLoop Callback | Model Plugin — Begin |
| Initialization (per UUT) | PreUUT Callback | Model Plugin — UUT Start |
| Initialization (per batch) | PreBatch Callback | Model Plugin — Batch Start |
| Processing results (per UUT) | TestReport Callback LogToDatabase Callback | Model Plugin — UUT Done |
| Processing results (per batch) | BatchReport Callback | Model Plugin — Batch Done |
| Processing results (On-the-Fly) | ProcessModelPostResultList Entry Engine Callback | Model Plugin — OnTheFly Step Results |
| Clean-up (one time) | ProcessCleanup Callback PostUUTLoop Callback | Model Plugin — End |
| Clean-up (per UUT) | PostUUT Callback | Model Plugin — UUT Done |
| Clean-up (per batch) | PostBatch Callback | Model Plugin — Batch Done |

In addition to the process model plug-in sequences, the model plug-in template contains data types you can use to store configuration or other data relevant to the process model plug-in. Add any properties specific to your custom result processing functionality to the plug-in Options data type to store configuration options. An instance of this type exists in each process model plug-in entry point within the PlugInSpecific container. Use a code module in the Model Plugin — Configure Standard Options sequence to provide an interface for end users to set values for the properties you added.

TestStand stores this model plug-in specific data in a configuration file and automatically passes the data into the process model plug-in sequences when the process model calls the model plug-in sequence file.

Parent topic:

Migrating Custom Results Processing Components

Related concepts:

- Creating Process Model Plug-ins
- Model Plug-in Entry Points
- Model Plugin – Configure Standard Options
- Model Plugin – Begin
- Model Plugin – UUT Start
- Model Plugin – Batch Start
- Model Plugin – UUT Done
- Model Plugin – Batch Done
- Model Plugin – OnTheFly Step Results
- Model Plugin – End
- Configuring Process Model Plug-ins

<!--NI_TOPIC bundle=teststand path=migrating-custom-results-processing-component.html language=enus -->
## TOPIC 00568: Migrating Custom Results Processing Components

- bundle_id: `teststand`
- source_path: `migrating-custom-results-processing-component.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/migrating-custom-results-processing-component.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Many process model customizations relate to changing the way TestStand generates reports or logs data to databases. The scope of the changes determines the approach you take to implement customizations you made. You can migrate the following common types of result processing changes:

### Migrating Custom Results Processing Components

Many process model customizations relate to changing the way TestStand generates reports or logs data to databases. The scope of the changes determines the approach you take to implement customizations you made. You can migrate the following common types of result processing changes:

Parent topic:

Migrating Process Model Customizations to TestStand 2012 or Later

Related concepts:

- Migrating Changes to Settings of the Default Result Processors
- Migrating Modifications to Process Model Callbacks
- Migrating Additional Results from the Client Sequence
- Migrating Modifications to Built-in Result Processors
- Migrating Custom Result Processors

<!--NI_TOPIC bundle=teststand path=migrating-customizations-to-process-model-cal.html language=enus -->
## TOPIC 00569: Migrating Customizations to Process Model Callbacks

- bundle_id: `teststand`
- source_path: `migrating-customizations-to-process-model-cal.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/migrating-customizations-to-process-model-cal.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: If you made changes to callback definitions in TestStand 2010 or earlier, you can use the following techniques for migrating custom code: Modifying the callbacks in the process model file itselfUse this approach when you want to continue to use the default process model functionality.You will have t

### Migrating Customizations to Process Model Callbacks

If you made changes to callback definitions in TestStand 2010 or earlier, you can use the following techniques for migrating custom code:

- Modifying the callbacks in the process model file itself
  - Use this approach when you want to continue to use the default process model functionality.
  - You will have to migrate changes when you upgrade TestStand in the future.
- Implementing the custom callback in a process model plug-in add-on
  - Use this approach when you made complex callback modifications or if you completely rewrote the callbacks.
  - You can easily migrate changes to future versions of TestStand because you do not make any changes to the process model.

The following table summarizes the recommended approach for migrating changes to callbacks.

| Callback Name | Recommendation |
| --- | --- |
| PreUUTPostUUTPreBatchPostBatch | If you created a custom dialog box, migrate the callback code to a custom process model plug-in add-on. Add a Sequence Call step in the correct process model plug-in sequence to call the new callback. To suppress the default callback code in the TestStand 2012 or later process model, set the element that corresponds to the callback in the Locals.ModelPluginConfiguration.RuntimeVariables.ModelDialogsEnabled container to False in the Begin sequence of the process model plug-in. You can migrate changes to a modified version of the default dialog box. If you are using the default dialog box, you can integrate changes with the TestStand 2012 or later process model files. |
| PreUUTLoopPostUUTLoopPreBatchLoopPostBatchLoopProcessSetupProcessCleanup | Because these callbacks are empty by default, migrate the callback code to a custom process model plug-in. Add a Sequence Call step in the correct process model plug-in sequence to call the new callback. |
| ModelOptions | Because the ModelOptions callback must have access to the process model properties, migrate changes to this callback to the ModelOptions callback in the ModelSupport.seq sequence file. |
| Custom Callbacks | Migrate the custom code to a custom process model plug-in and add a Sequence Call step in the correct process model plug-in sequence to call the new callback. Create an empty definition for the custom callback in the process model file so that the client sequence file recognizes the custom callback at edit time, meaning that the callback icon appears green in the Sequences pane and is present in the Sequence File Callbacks dialog box. |

Parent topic:

Migrating Other Custom Built-in Process Model Components

Related concepts:

- Migrating Custom Result Processors
- Migrating Customizations to Process Model Dialog Boxes
- Migrating Process Model Customizations to TestStand 2012 or Later
- Migrating Modifications to Process Model Callbacks

<!--NI_TOPIC bundle=teststand path=migrating-customizations-to-process-model-dia.html language=enus -->
## TOPIC 00570: Migrating Customizations to Process Model Dialog Boxes

- bundle_id: `teststand`
- source_path: `migrating-customizations-to-process-model-dia.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/migrating-customizations-to-process-model-dia.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The default TestStand process models launch dialog boxes to indicate the test status and to gather information from end users. The following table provides information about changes to each dialog box. The modelsupport2.dll, located by default at <TestStand>\Components\Models\TestStandModels, includ

### Migrating Customizations to Process Model Dialog Boxes

The default TestStand process models launch dialog boxes to indicate the test status and to gather information from end users. The following table provides information about changes to each dialog box. The modelsupport2.dll, located by default at <TestStand>\Components\Models\TestStandModels, includes all the code for these dialog boxes.

If changes exist in the TestStand 2012 or later implementation of the dialog box, you can use a file differencing tool to check the differences and then integrate the changes into the customized code. Additionally, ensure that you build the DLL against the TestStand 2012 or later API. If you directly migrate a DLL from an earlier version of TestStand, rebuild the DLL against the TestStand 2012 or later API before you implement the DLL with TestStand 2012 or later.

| Customized Model Dialog Box | Location of Modified Code | Notes |
| --- | --- | --- |
| UUT Serial Number dialog box (Sequential process model) | modelsupport2.dll (uutdlg.c) | No changes exist in the TestStand 2012 or later version |
| UUT Status dialog box (Parallel process model) | modelsupport2.dll (paralleluutdlg.c) | Minor changes exist in the TestStand 2012 or later version |
| UUT Status dialog box (Batch process model) | modelsupport2.dll (batchuutdlg.c) | Minor changes exist in the TestStand 2012 or later version |
| UUT Result banner | modelsupport2.dll (banners.c) | Minor changes exist in the TestStand 2012 or later version |

If you implement custom dialog boxes that your custom process model calls, you can migrate the callbacks that implement these dialog boxes.

Parent topic:

Migrating Other Custom Built-in Process Model Components

Related concepts:

- TestStand Directory Structure
- Migrating Customizations to Process Model Callbacks

<!--NI_TOPIC bundle=teststand path=migrating-error-handling-customizations.html language=enus -->
## TOPIC 00571: Migrating Error Handling Customizations

- bundle_id: `teststand`
- source_path: `migrating-error-handling-customizations.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/migrating-error-handling-customizations.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following table outlines common error handling customization techniques and the recommended approach for migrating these changes to TestStand 2012 or later. Custom Error Handling Technique Recommended Approach for Migration to TestStand 2012 or Later Configuring the error handling behavior in th

### Migrating Error Handling Customizations

The following table outlines common error handling customization techniques and the recommended approach for migrating these changes to TestStand 2012 or later.

| Custom Error Handling Technique | Recommended Approach for Migration to TestStand 2012 or Later |
| --- | --- |
| Configuring the error handling behavior in the station options | Use the TestStand Migration Utility |
| Using the ProcessModelPostStepRuntimeError Engine callback in the process model | This callback has no changes in TestStand 2012 or later, and you can migrate any code in this callback directly to the TestStand 2012 or later process models |

Parent topic:

Migrating Other Custom Built-in Process Model Components

<!--NI_TOPIC bundle=teststand path=migrating-labview-code-modules-from-32-bit-te.html language=enus -->
## TOPIC 00572: Migrating LabVIEW Code Modules from 32-bit TestStand to 64-bit TestStand

- bundle_id: `teststand`
- source_path: `migrating-labview-code-modules-from-32-bit-te.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/migrating-labview-code-modules-from-32-bit-te.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Complete the following steps if you migrate code modules from 32-bit TestStand to 64-bit TestStand and you no longer intend to support the 32-bit architecture. Mass compile all the VIs. Regenerate the required packed project libraries with a supported version of 64-bit LabVIEW. Replace dependent DLL

### Migrating LabVIEW Code Modules from 32-bit TestStand to 64-bit TestStand

Complete the following steps if you migrate code modules from 32-bit TestStand to 64-bit TestStand and you no longer intend to support the 32-bit architecture.

1. Mass compile all the VIs.
2. Regenerate the required packed project libraries with a supported version of 64-bit LabVIEW.
3. Replace dependent DLLs with 64-bit versions.
4. In TestStand, select Tools»Update VI Calls to update Express VIs and property node calls with a supported version of 64-bit LabVIEW.

Parent topic:

LabVIEW Code Module Support for 64-bit TestStand

<!--NI_TOPIC bundle=teststand path=migrating-model-options-files.html language=enus -->
## TOPIC 00573: Migrating Model Options Files

- bundle_id: `teststand`
- source_path: `migrating-model-options-files.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/migrating-model-options-files.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The model options files have the following migration actions: Add configuration—Creates a new configuration in a configuration set called Migrated from TestStand <Version>. The Migration Utility automatically selects a unique name for the configuration if the tool has already used the default name i

### Migrating Model Options Files

The model options files have the following migration actions:

- Add configuration —Creates a new configuration in a configuration set called Migrated from TestStand <Version> . Note The Migration Utility automatically selects a unique name for the configuration if the tool has already used the default name in a previous completed migration. Refer to the migration report for the specific configuration names the tool uses.
- Overwrite legacy options —Copies the options files from TestStand 2010 SP1 or earlier to the current TestStand directory so you can use the previous configurations with the equivalent legacy TestStand 2010 process models in the current version of TestStand. When you migrate database options, the Migration Utility renames TestStandDatabaseOptions.ini to TestStandDatabaseSchemas.ini .
- Both —Adds a new configuration in the Migrated from TestStand <Version> configuration set and also copies the options files from a previous version of TestStand.

Parent topic:

Migrating Other Custom Built-in Process Model Components

<!--NI_TOPIC bundle=teststand path=migrating-modifications-to-built-in-result-pr.html language=enus -->
## TOPIC 00574: Migrating Modifications to Built-in Result Processors

- bundle_id: `teststand`
- source_path: `migrating-modifications-to-built-in-result-pr.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/migrating-modifications-to-built-in-result-pr.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: For more complex reporting customizations, you must often modify the underlying result processing code the process model calls. The format of results you generate determine in which process model components the modifications reside. Although the TestStand 2012 or later process models use the same un

### Migrating Modifications to Built-in Result Processors

For more complex reporting customizations, you must often modify the underlying
 result processing code the process model calls. The format of results you generate
 determine in which process model components the modifications reside. Although the
 TestStand 2012 or later process models use the same underlying components in many
 cases, most TestStand 2012 or later components include modifications to some extent
 with respect to the corresponding TestStand 2010 SP1 or earlier components. The
 TestStand 2012 or later process models depend on many of these changes to function
 properly.

Refer to the following table for more information about which components to migrate
 for common types of customizations and the complexity of changes for each component
 for TestStand 2012 or later. All files mentioned in the table are located in the
 <TestStand>\Components\Models\TestStandModels
 directory unless otherwise specified.

| Description of Customization | Likely Location of Changes in TestStand Components | Details on Changes in TestStand 2012 or Later |
| --- | --- | --- |
| Changing the appearance or formatting of the ATML or XML report | Report style sheets:ATML—TRML.xslXML—report.xsl, expand.xsl, horizontal.xsl | Significant changes exist in the TestStand 2012 or later versions of the ATML report style sheets.TestStand 2013 or later supports the approved version 6.01 of the ATML Test Results and Session Information schema the ATML standard defines. ATML reports that validate against version 6.01 of the schema can use the TR6_report.xsl, TR6_Horizontal.xsl, or TR6_Expand.xsl style sheets.TestStand 2012 or later supports the unapproved version 5.0 of the ATML Test Results and Session Information schema the ATML standard defines. ATML reports that validate against version 5.0 of the schema can use the TR5_report.xsl, TR5_Horizontal.xsl, or TR5_Expand.xsl style sheets.You can also use the ATML 2.02 standard in TestStand 2010 or later with the TRML.xsl style sheet or TR_horizontal.xsl style sheet. Note No plans exist to approve version 5.0 of the ATML Test Results and Session Information schema. |
| Changing the appearance or formatting of the report (text, HTML) | — | Refer to the Logging additional information to the report body rows for more information about these types of changes. |
| Logging additional information to the report header | AddReportHeader sequence in ReportGen_<format>.seq | Minor changes exist in the TestStand 2012 or later version of these components. |
| Logging additional information to the report footer | AddReportFooter sequence in ReportGen_<format>.seq | No changes exist in the TestStand 2012 or later version of these components. |
| Logging additional information to the report body (On-the-Fly disabled) | AddReportBody sequence in ReportGen_<format>.seq | Moderate changes exist in the TestStand 2012 or later version of these components. ATML—The ATMLSupport.dll file generates the report body. TestStand includes the source code for this DLL. XML—The XML generation process is built into the TestStand Engine and is not customizable. |
| Logging additional information to the report body (On-the-Fly enabled) | InitializeOTF and ProcessOTFStepResult sequences in ReportGen_<format>.seq | TestStand 2012 or later includes the ProcessModelPostResults Engine callback to handle on-the-fly results. This callback executes at various intervals as a result of the on-the-fly configuration settings. Because of this change, the on-the-fly result processor must handle multiple results. The functionality in the TestStand 2010 on-the-fly results generator was heavily modified to implement this change. TestStand 2012 or later implements the InitializeOTFReport and ProcessOTFStepResults sequences in ReportGen_<format>.seq for on-the-fly reporting. |

Parent topic:

Migrating Custom Results Processing Components

Related concepts:

- Migrating Process Model Customizations to TestStand 2012 or Later
- TestStand Directory Structure
- ATML Test Results Reports
- Process Model Support Files
- XML Reports

<!--NI_TOPIC bundle=teststand path=migrating-modifications-to-process-model-call.html language=enus -->
## TOPIC 00575: Migrating Modifications to Process Model Callbacks

- bundle_id: `teststand`
- source_path: `migrating-modifications-to-process-model-call.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/migrating-modifications-to-process-model-call.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Important similarities and differences exist in the way you use process model callbacks in TestStand 2012 or later and in previous versions of TestStand. Overriding Process Model Callbacks To customize result processing for a specific type of UUT, you typically override process model callbacks in a

### Migrating Modifications to Process Model Callbacks

Important similarities and differences exist in the way you use process model callbacks in TestStand 2012 or later and in previous versions of TestStand.

#### Overriding Process Model Callbacks

To customize result processing for a specific type of UUT, you typically override process model callbacks in a client sequence file. This technique remains the same in TestStand 2012 or later. You can override callbacks in the same manner as in earlier versions of TestStand. As a result of this similarity, you can seamlessly migrate client sequence files that override process model callbacks from earlier versions of TestStand to TestStand 2012 or later.

#### Migrating Modifications to Built-in
 Process Model Callback Definitions

Although the process of overriding
 callbacks has not changed, TestStand 2012 or later changes the location where it
 defines the callbacks. TestStand 2012 or later defines result processing callbacks
 in the process model and in the result processing model plug-in, but only the
 process model plug-in implementation contains any steps. The callback definition in
 the process model exists so that the client sequence file recognizes the callback at
 edit time, meaning that the callback icon appears green in the Sequences pane and is
 present in the Sequence File Callbacks dialog box.

Note

definition

If you modified the default functionality of a results
 processing callback by directly modifying the callback sequence in the process
 model, you must copy the modifications into the callback sequence in the
 corresponding process model plug-in sequence file. For example, if you added steps
 to the TestReport callback sequence in SequentialModel.seq in
 TestStand 2010 or earlier, you must migrate these changes to the TestReport callback
 sequence in the NI_ReportGenerator.seq result processing model
 plug-in.

The following table shows where TestStand 2012 or later defines the
 TestStand 2010 SP1 or earlier results processing callback sequences:

| Callback Sequence | Location of Callback Definition in TestStand 2012 or Later |
| --- | --- |
| TestReportBatchReportModifyReportHeaderModifyReportEntryModifyReportFooterReportOptionsModifyBatchReportHeaderModifyBatchReportEntryModifyBatchReportFooter | NI_ReportGenerator.seq (report generation result processing model plug-in) |
| DatabaseOptionsLogToDatabase | NI_DatabaseLogger.seq (database logging result processing model plug-in) |

#### Migrating Custom Result Processing Callbacks

If you created custom result processing callbacks in TestStand 2010 or earlier, you must migrate these callbacks and any steps that call the callbacks to the process model plug-in sequence file. To invoke the callback, create a Sequence Call step in the appropriate Model Plugin entry point. For example, if you created a custom callback to log additional information to the report immediately after TestStand generates the report, move this callback definition from the process model to the NI_ReportGenerator process model plug-in, then call the callback sequence in the Model Plugin — UUT Done plug-in entry point. Maintain a blank definition of the callback in the process model itself so client sequence file developers know that the callback is available to override.

Parent topic:

Migrating Custom Results Processing Components

Related concepts:

- Model Plug-in Entry Points
- Model Plugin – UUT Done

<!--NI_TOPIC bundle=teststand path=migrating-other-custom-built-in-process-model.html language=enus -->
## TOPIC 00576: Migrating Other Custom Built-in Process Model Components

- bundle_id: `teststand`
- source_path: `migrating-other-custom-built-in-process-model.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/migrating-other-custom-built-in-process-model.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Because the majority of changes in the TestStand 2012 or later process models relate to the process model plug-in architecture, the following components of the process models remain largely unchanged from the TestStand 2010 or earlier:

### Migrating Other Custom Built-in Process Model Components

Because the majority of changes in the TestStand 2012 or later process models relate to the process model plug-in architecture, the following components of the process models remain largely unchanged from the TestStand 2010 or earlier:

Parent topic:

Migrating Process Model Customizations to TestStand 2012 or Later

Related concepts:

- Migrating Customizations to Process Model Callbacks
- Migrating Customizations to Process Model Dialog Boxes
- Migrating Error Handling Customizations

<!--NI_TOPIC bundle=teststand path=migrating-process-model-customizations-to-tes.html language=enus -->
## TOPIC 00577: Migrating Process Model Customizations to TestStand 2012 or Later

- bundle_id: `teststand`
- source_path: `migrating-process-model-customizations-to-tes.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/migrating-process-model-customizations-to-tes.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Before you migrate customizations from TestStand 2010 or earlier into TestStand 2012 or later, NI recommends that you familiarize yourself with the process model plug-in architecture. Before you customize any process model files, NI recommends that you copy the default <TestStand>\Components\Models

### Migrating Process Model Customizations to TestStand 2012 or Later

Before you migrate customizations from TestStand 2010 or earlier into TestStand 2012 or later, NI
 recommends that you familiarize yourself with the process model plug-in
 architecture.

Note

<TestStand>\Components\Models

<TestStand Public>\Components\Models

<TestStand
 Public>

<TestStand
 Public>

The first step in successfully migrating existing customizations to TestStand 2012 or later is to determine where to implement changes in the newer process model files. Once you determine the new location for the customization, you must then consider how to integrate the changes with the changes present in the TestStand 2012 or later components.

In many cases, the TestStand components that contain the customizations you made also contain changes implemented in TestStand 2012 or later. This situation requires you to integrate the changes into a single file that contains the TestStand 2012 or later changes and the customizations you made. The approach you take for integrating files differs based on the following levels of complexity:

- Changes you made to the component are less complex than changes implemented in TestStand 2012 or later —Determine the changes you made to the component and reapply the customizations to a copy of the TestStand 2012 or later version of the component.
- Changes you made to the component are more complex than changes implemented in TestStand 2012 or later —Determine the changes between the TestStand 2012 or later version of the component and the original version of the component you modified and apply the TestStand 2012 or later improvements to the custom version of the component.

To facilitate this process, consider using one of the following recommended differ tools to quickly compare files.

| File Type | Recommended Differ Tool |
| --- | --- |
| Sequence file (.seq) | TestStand File Diff and Merge utility |
| VI (.vi) | LabVIEW Compare VIs dialog box |
| C code (.c, .h) | Select Edit»Diff in LabWindows/CVI |
| Other files (non-binary) | Third-party text differ |

#### Categories of Customizations

Customizations typically fall into one of following categories:

- Result processing components
- Built-in components
- Custom process model components

Parent topic:

Process Model Plug-In Architecture

Related concepts:

- Process Model Plug-In Architecture
- TestStand Directory Structure
- Migrating Custom Results Processing Components
- Migrating Other Custom Built-in Process Model Components
- Migrating Custom Process Model Components

<!--NI_TOPIC bundle=teststand path=migrating-teststand-2010-sp1-or-earlier-resul.html language=enus -->
## TOPIC 00578: Migrating TestStand 2010 SP1 or Earlier Result Processing Options to the Current Version of TestStand

- bundle_id: `teststand`
- source_path: `migrating-teststand-2010-sp1-or-earlier-resul.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/migrating-teststand-2010-sp1-or-earlier-resul.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Process models from TestStand 2012 and later include significant changes to implement a plug-in architecture for model sequence files. As a result, the result processing options files from TestStand 2010 SP1 or earlier are not compatible with TestStand 2012 or later process models without migration.

### Migrating TestStand 2010 SP1 or Earlier Result
 Processing Options to the Current Version of TestStand

Process models from TestStand 2012 and later include significant changes to implement a
 plug-in architecture for model sequence files. As a result, the result processing options
 files from TestStand 2010 SP1 or earlier are not compatible with TestStand 2012 or later
 process models without migration.

TestStand 2012 or later uses the plug-in mechanism to decouple result processing from the process
 models. As part of this change, the result processing options move from the
 TestStandModelReportOptions.ini and
 TestStandDatabaseOptions.ini files into a single
 ResultProcessing.cfg file located in the
 <TestStand Application Data>\Cfg directory, which stores
 configuration information for all result processing model plug-ins. Without migration
 through the TestStand Migration Utility or the Legacy Model Switcher tool to use legacy
 TestStand 2010 process models, results processing options files from TestStand 2010 SP1
 or earlier will not function properly in TestStand 2012 or later.

Note

ReportOptions

DatabaseOptions

| Migration Action | Description |
| --- | --- |
| Apply to new models | Creates a new configuration in a configuration set named Migrated from TestStand <Version>. The utility automatically selects a unique name for the configuration if the utility has already used the default name in a previously completed migration. Refer to the migration report for the specific configuration names the utility uses. |
| Apply to legacy models | Copies the options files from TestStand 2010 SP1 or earlier to the current TestStand directory so you can use the previous configurations with the equivalent legacy TestStand 2010 process models in the version of TestStand you're migrating to. When you migrate database options, the utility renames TestStandDatabaseOptions.ini to TestStandDatabaseSchemas.ini. |
| Apply to new and legacy models | Adds a new configuration in the Migrated from TestStand <Version> configuration set and copies the options files from the version of TestStand you're migrating from. |

If you are upgrading from TestStand 4.2.1 or earlier, you can manually migrate result
 processing options for use with TestStand 2012 or later process models or the equivalent
 legacy TestStand 2010 process models.

Parent topic:

Migrating to the Current Version of TestStand

Related information:

- TestStand Migration Guidance
- Legacy Model Switcher

<!--NI_TOPIC bundle=teststand path=migrating-to-the-current-version-of-teststand.html language=enus -->
## TOPIC 00579: Migrating to the Current Version of TestStand

- bundle_id: `teststand`
- source_path: `migrating-to-the-current-version-of-teststand.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/migrating-to-the-current-version-of-teststand.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `task`
- source_description: If you are upgrading from TestStand 2010 or later, you can use the TestStand Migration Utility to migrate customizations and configuration settings from the earlier version of TestStand. Consider the following when using the TestStand Migration Utility: The utility only moves files and does not upda

### Migrating to the Current Version of
 TestStand

If you are upgrading from TestStand 2010 or later, you can use the TestStand Migration
 Utility to migrate customizations and configuration settings from the earlier version of
 TestStand.

- The utility only moves files and does not update any other information or
 settings, such as registry keys.
- If the <TestStand Public>\Components directory of the
 previous version of TestStand includes files installed by an installer other
 than the TestStand installer, you may need to use that specific installer to
 move the files. Files installed by a different installer migrated by the
 TestStand Migration Utility may not function correctly or uninstall properly
 from the <TestStand Public>\Components directory of your
 target version of TestStand.
- The Migration Utility does not copy files in the
 <TestStand>\Examples ,
 <TestStand>\Tutorial , or
 <TestStand>\AdapterSupport directories. These
 directories do not appear in the Files to Migrate column of the utility.
- The TestStand 2024 Q4 Migration Utility does not migrate <TestStand
 LocalAppData>\layout_current.bin , <TestStand
 LocalAppData>\SeqEdit.xml , or <TestStand
 LocalAppData>\UserInterface.xml files from previous TestStand
 versions.

1. Launch the TestStand Migration Utility from the <National
 Instruments folder in your start menu. If you have more than one
 version of TestStand installed on the computer, the utility launches a dialog
 box where you specify the previous version of TestStand you want to migrate
 from. 
 Note When you migrate from
 TestStand 2010 SP1 or TestStand 2010 to the current version of TestStand,
 the utility migrates the report and database options to the format for
 result processing configuration options for the current version of
 TestStand.
2. Select the version of TestStand you are migrating from. The utility checks your
 computer for all the files you can migrate to determine if the files have
 changed since installation. The utility launches a status indicator dialog box
 during this process.
3. Use the Files to Copy control to select the files you
 want to copy. The utility selects files you added or modified in the version of
 TestStand you are migrating from by default.
4. Expand the directories in the Files to Copy control to
 view the files you can migrate and whether those files have changed since
 installation. The Conflicts column shows any conflicts
 that could affect the migration of your selected files. 
 Note The utility overwrites any
 file you create or modify in the current version of TestStand if the file
 also exists in the corresponding directory of the previous version of
 TestStand and if you select the file in the Files to
 Copy control. Although the utility creates a backup copy of
 all overwritten files, verify that the utility will not overwrite any files
 you intend to keep in the version of TestStand you are migrating to.
5. Click Migrate Files to begin the migration. 
 When the migration completes successfully, the utility generates a text
 file report that contains the results of the migration, including where the
 utility stored the file backups and which files were moved.

You can also upgrade manually, or migrate
 between 32-bit and 64-bit TestStand installations of the same version.

Related concepts:

- 64-bit TestStand and Migrating from 32-bit TestStand

Related information:

- TestStand Migration Guidance

<!--NI_TOPIC bundle=teststand path=minimizing-report-file-size.html language=enus -->
## TOPIC 00580: Minimizing Report File Size

- bundle_id: `teststand`
- source_path: `minimizing-report-file-size.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/minimizing-report-file-size.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Automated test systems can generate a significant amount of data when testing a unit under test (UUT). The amount of data generated depends on the complexity of the UUT to test and the capabilities of the test equipment. The size of the report generated depends on the format of the report and the am

### Minimizing Report File Size

Automated test systems can generate a significant amount of data when testing a unit under test
 (UUT). The amount of data generated depends on the complexity of the UUT to test and
 the capabilities of the test equipment. The size of the report generated depends on
 the format of the report and the amount of data to log. Primarily, system-level
 requirements of storage for traceability or analysis and the testing and debugging
 processes you use influence the amount of data to log in the report. In all cases,
 NI benchmarks show that the TSR report format is the most efficient at minimizing
 size on disk.

#### Recommended Report
 Options

The following table summarizes the recommended options you
 configure in the Report Options dialog box when you optimize for report
 size:

| Report Option | Value |
| --- | --- |
| Format | TSR*, ASCII, ATML, HTML, XML (best to worst) |
| Asynchronous | N/A |
| On-the-Fly Report | N/A |
| Only Display Latest Results | N/A |

Note

#### Tradeoffs

Consider the
 impact to the following requirements when you optimize for report size:

- Maximize test system throughput
- Include all necessary report content
- Interoperate with other processes and systems

Parent topic:

Choosing the Appropriate Report Generation Strategy

Related concepts:

- Maximizing Test System Throughput
- Including All Necessary Report Content
- Interoperating with Other Processes and Systems

<!--NI_TOPIC bundle=teststand path=mismatched-sections-synchronized-sections.html language=enus -->
## TOPIC 00581: Mismatched Sections - Synchronized Sections

- bundle_id: `teststand`
- source_path: `mismatched-sections-synchronized-sections.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/mismatched-sections-synchronized-sections.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Sections become mismatched when all the threads in a batch block at different Enter or Exit operations. This situation can occur when a sequence implements a conditional flow of execution as a result of preconditions, post actions, or other flow control operations. When TestStand detects mismatched

### Mismatched Sections - Synchronized Sections

Sections become mismatched when all the threads in a batch block at different Enter or Exit operations. This situation can occur when a sequence implements a conditional flow of execution as a result of preconditions, post actions, or other flow control operations.

When TestStand detects mismatched sections, the thread at the Enter or Exit step that appears earliest in the hierarchy of sequences and subsequences proceeds as if all threads in the batch are at the same step.

When multiple Enter and Exit operations are equally early in the hierarchy of sequences and subsequences, Enter operations proceed first.

Parent topic:

Synchronized Sections

<!--NI_TOPIC bundle=teststand path=mobile-device-test-demo.html language=enus -->
## TOPIC 00582: Mobile Device Test Demo

- bundle_id: `teststand`
- source_path: `mobile-device-test-demo.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/mobile-device-test-demo.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Purpose This example simulates the testing of a cellular phone with test steps that use the LabVIEW, LabWindows/CVI, and .NET Adapters. Example File Location <TestStand Public>\Examples\Demos\Mobile Device Test\Mobile Device Test.seq Highlighted Features Test step types Flow Control step types Repor

### Mobile Device Test Demo

#### Purpose

This example simulates the testing of a cellular phone with test steps that use the LabVIEW, LabWindows/CVI, and .NET Adapters.

#### Example File
 Location

<TestStand
 Public>\Examples\Demos\Mobile Device Test\Mobile Device
 Test.seq

#### Highlighted Features

- Test step types
- Flow Control step types
- Report generation

#### Major API

None

#### Prerequisites

None

Note

#### How to Use This Example

Complete the following steps to review the sequences and steps in the example.

1. Select the MainSequence in the Sequences pane and review the following steps in the Steps pane:
  - The Simulation Dialog step launches a dialog box to prompt you to select a test or tests you want to simulate to fail.
  - Notice that the test steps are configured to use different adapters based on the implementation of the code module.
2. Many of the tests are contained within a subsequence and are called using sequence call steps. Double-click a sequence call step to view the subsequence that it calls.
3. The code modules in this example implement simulated hardware calls and test functionality. Navigate to the <TestStand Public>\Examples\Demos\Mobile Device Test directory to view the source code for the code modules.

Complete the following steps to run the example.

1. Select Execute»Single Pass to run the sequence.
2. Select a UUT configuration in the dialog box.
3. When execution completes, review the report on the Report pane. The report for this example has been customized to demonstrate the following TestStand features for report customization:
  - The audio and user input test steps use the additional results feature to log the simulated data to the report.
  - The LCD Video and RF test steps use the ReportText field to log custom HTML code that contains an image generated in the code module.

You can run this example using the Batch or Parallel process models. Complete the following steps to run the example with a different process model.

1. Select Edit»Sequence File Properties .
2. On the Advanced tab, select Require Specific Model in the Model Option field.
3. Select ParallelModel.seq or BatchModel.seq in the Model File control.
4. Click OK to close the dialog box.
5. Select Execute»Single Pass to run the sequence. Notice that multiple instances of the test now execute.

Parent topic:

Examples for Demos

Related concepts:

- Programming with the TestStand API in LabVIEW
- Programming with the TestStand API in LabWindows/CVI
- TestStand Directory Structure

<!--NI_TOPIC bundle=teststand path=model-callbacks-in-the-batch-process-model.html language=enus -->
## TOPIC 00583: Model Callbacks in the Batch Process Model

- bundle_id: `teststand`
- source_path: `model-callbacks-in-the-batch-process-model.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/model-callbacks-in-the-batch-process-model.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Batch process model includes the following Model callbacks, which you can override with client sequence files: MainSequence—The Test UUTs - Test Socket Entry Point and Single Pass - Test Socket Entry Point sequences call the MainSequence callback, which is empty in the process model file. The cl

### Model Callbacks in the Batch Process Model

The Batch process model includes the following Model callbacks, which you can override with client sequence files:

- MainSequence —The Test UUTs - Test Socket
 Entry Point and Single Pass - Test Socket
 Entry Point sequences call the MainSequence callback, which is empty in the
 process model file. The client sequence file must contain a
 MainSequence callback that performs the tests on a
 UUT.
- PreMainSequence —The Test UUTs and Single Pass sequences call the
 PreMainSequence callback before the MainSequence executes. The PreMainSequence
 callback in the process model file is empty. Override this in the client file to
 perform an action before any code in the MainSequence executes.
- PostMainSequence —The Test UUTs and Single Pass sequences call the
 PostMainSequence callback after the MainSequence executes. The PostMainSequence
 callback in the process model file is empty. Override this in the client file to
 perform an action after all code in the MainSequence executes but before any
 Model Plug-ins execute.
- PreUUT —The test socket executions call the PreUUT callback, which calls
 the DoPreUUT sequence, which is empty in the process model file. When you override the
 PreUUT callback with a client sequence file to obtain the serial
 number for the UUT, override the PreBatch callback also. The PreBatch callback
 launches a dialog box to obtain the serial numbers for all the UUTs in the
 batch.
- PostUUT —The test socket executions call the Post UUT callback, which
 calls the DoPostUUT sequence, which is empty in the process model file. When you
 override the PostUUT callback with a client sequence file to display the result
 status for a UUT, override the PostBatch callback also. The PostBatch callback
 launches a dialog box to show the result status for all the UUTs in the
 batch.
- PreUUTLoop —Before the UUT loop begins, the Test UUTs — Test Socket Entry
 Point sequence calls the PreUUTLoop callback, which is empty in the process
 model file.
- PostUUTLoop —After the UUT loop terminates, the Test UUTs — Test Socket
 Entry Point sequence calls the PostUUTLoop callback, which is empty in the
 process model file.
- ReportOptions —The process model Execution entry point sequence calls the
 Model
 Plugins – Begin sequence in ModelSupport.seq . Model
 Plugins – Begin calls the Model Plugin –
 Initialize sequence in each plug-in instance. Model Plugin –
 Initialize in the NI_ReportGenerator.seq plug-in calls the
 ReportOptions callback so the client sequence file can modify the report
 options. The ReportOptions callback in the process model file is empty. This
 callback serves the same purpose as the more general ModelPluginOptions
 callback, but the report generator plug-in calls ReportOptions only for report
 generator plug-in instances and passes to it only reporting options.
- DatabaseOptions —The process model Execution entry point sequence calls
 the Model
 Plugins – Begin sequence in ModelSupport.seq . Model
 Plugins – Begin calls the Model Plugin –
 Initialize sequence in each plug-in instance. Model Plugin –
 Initialize in the NI_DatabaseLogger.seq plug-in calls the
 DatabaseOptions callback so the client sequence file can modify the database
 options. The DatabaseOptions callback in the process model file is empty. This
 callback serves the same purpose as the more general ModelPluginOptions
 callback, but the database logging plug-in calls DatabaseOptions only for
 database logging plug-in instances and passes to it only database options.
- ModelOptions —The process model Execution entry point sequence calls the
 Initialize Execution entry point sequence in ModelSupport.seq .
 After reading the test station model options from disk, the sequence calls the
 ModelOptions callback so the client sequence file can modify the model options.
 The ModelOptions callback in the process model file is empty. The client
 sequence file can change the value of the
 ModelPluginConfigurationToLoad parameter to specify
 the name of the model plug-in configuration to load from each model plug-in
 configuration file. The default value for the
 ModelPluginConfigurationToLoad parameter is an empty
 string, which directs the process model to load the active configuration from
 each model plug-in configuration file.
- TestReport —The Test UUTs and Single Pass Execution entry points call the
 Model Plugins – UUT Done sequence in ModelSupport.seq .
 ModelSupport.seq calls the Model Plugin – UUT Done entry
 point for each configured result processor. The
 NI_ReportGenerator.seq plug-in calls the TestReport
 callback from the UUT Done entry point to generate the contents of the report
 for one UUT. The report generator does not call the TestReport callback when you
 enable the On-The-Fly Reporting option in the Report Options dialog box. The
 report plug-in defines a report for a single UUT as a header, an entry for each
 step result, and a footer. When you do not want to override the entire
 TestReport callback, you can override the ModifyReportHeader, ModifyReportEntry,
 and ModifyReportFooter callbacks instead to customize the report. You can
 override ModifyReportEntry only when you select the Sequence option in the
 Report Options dialog box and the report format is HTML or ASCII text. The
 TestReport callback returns the report using the
 Report string parameter or the
 ReportSection object reference parameter.
 TestStand 2010 SP1 or earlier process models use the
 Report parameter. TestStand 2012 or later process
 models use the ReportSection parameter. If you
 override the TestReport callback, you must support the parameter that
 corresponds to the version of the process models you use. To support both
 methods of returning a report, use the ReportSection
 parameter to determine which parameter the invoking process model requires.
 If the ReportSection reference uses
 Nothing as the value, you must return the report as a
 string in the Report parameter. If the
 ReportSection reference uses a value other than
 Nothing, you must return the report by updating the
 ReportSection parameter. For HTML and ASCII
 text report formats, depending on the settings in the Report Options dialog
 box, the TestReport callback determines whether TestStand uses sequences or
 a DLL to build the report body. Select the Sequence option to more easily
 modify the reports TestStand generates. Select the DLL option to generate
 reports more efficiently. When you select the Sequence option in the
 Report Options dialog box, the TestReport callback calls the AddReportBody
 sequence in reportgen_html.seq or
 reportgen_txt.seq to build the report body. The report
 generator plug-in uses a series of sequences with steps that recursively
 process the result list for the execution. When you select the DLL option in
 the Report Options dialog box, the TestReport callback calls a function in
 modelsupport2.dll to build the report body. You can
 access the project and source code for the DLL built in LabWindows/CVI from
 the <TestStand>\Components\Models\TestStandModels
 directory. For XML reports, TestReport callback calls the
 AddReportBody sequence in reportgen_xml.seq. The report
 generator plug-in calls the PropertyObject.GetXML method. For ATML 2
 reports, the TestReport callback calls the GetATMLReport sequence in
 reportgen_atml.seq. The report generator plug-in in
 calls the Get_Atml_Report function in
 ATMLSupport.dll in the LabWindows/CVI project. For ATML
 5 reports, the TestReport callback calls the AddReportBody sequence in
 reportgen_atml.seq. The report generator plug-in calls
 the Get_Atml_ReportSection_For_Body function in
 ATMLSupport.dll. You can access the project and source
 code for the DLL built in LabWindows/CVI from the
 <TestStand>\Components\Models\TestStandModels\ATML
 directory.
- ModifyReportHeader —The TestReport callback calls the ModifyReportHeader callback so the client sequence file can modify the report header. The ModifyReportHeader callback receives parameters for the UUT information, the tentative report header text, and the report options. The ModifyReportHeader callback in the process model file is empty.
- ModifyReportEntry —The TestReport callback uses subsequences to call the ModifyReportEntry callback for each result in the result list for the UUT so the client sequence file can modify the entry point for each step result. The ModifyReportEntry callback receives parameters for an entry from the result list, the UUT information, the tentative report entry text, the report options, and a number that indicates the call stack depth at the time the step executed. TestStand does not call ModifyReportEntry callbacks when you enabled the DLL option in the Report Options dialog box. Instead, you must modify modelsupport2.dll , located in the <TestStand>\Components\Models\TestStandModels directory, to modify how step results appear in the report. The ModifyReportEntry callback in the process model file is empty.
- ModifyReportFooter —The TestReport callback calls the ModifyReportFooter callback so the client sequence file can modify the report footer. The ModifyReportFooter callback receives parameters for the UUT information, the tentative report footer text, and the report options. The ModifyReportFooter callback in the process model file is empty.
- GetReportFilePath —The report generator process model plug-in calls the GetReportFilePath callback so the client sequence file can inspect the report file path.
- LogToDatabase —Execution entry points call the LogToDatabase callback to
 populate a database with the results for one UUT. Execution entry points do not
 call the LogToDatabase callback when you enabled the Use On-The-Fly
 Logging option on the Logging Options tab of the Database Options
 dialog box. The LogToDatabase callback receives parameters for the UUT
 information, the result list for the UUT, and the database options.
- ProcessSetup —The Test UUTs and Single Pass Execution entry points call
 the ProcessSetup callback before creating the test socket executions so the
 client sequence file can execute any setup steps that must run only once during
 the execution of the process model. Only the controlling execution calls
 ProcessSetup. The test socket executions do not call the ProcessSetup
 callback.
- ProcessCleanup —The Test UUTs and Single Pass Execution entry points call
 the ProcessCleanup callback from the Cleanup step group so the client sequence
 file can execute any cleanup steps that must run only once during the execution
 of the process model. Only the controlling execution calls ProcessCleanup. The
 test socket executions do not call the ProcessCleanup callback.
- ModelPluginOptions —Execution entry points call the Model Plugins – Begin sequence in ModelSupport.seq , which calls the Initialize Model Plugins sequence. Initialize Model Plugins calls the ModelPluginOptions callback for each model plug-in instance so the client file can modify the model plug-in settings.
- ModelPluginConfiguration —Execution entry points call the Model Plugins – Begin sequence in ModelSupport.seq , which calls the Initialize Model Plugins sequence. Initialize Model Plugins calls the ModelPluginConfiguration callback so the client file can inspect or modify the set of model plug-ins the process model calls at run time.

The following callback sequences are unique to the Batch process model:

- PreBatch —Launches a dialog box to obtain the batch and UUT serial
 numbers.
- PostBatch —Displays a pass, fail, error, or terminated banner and batch
 and UUT reports for each test socket.
- PreBatchLoop —Before looping on a batch of UUTs, the process model calls
 the PreBatchLoop callback, which is empty in the process model file. Use the
 PreBatchLoop callback to perform an action before testing the batch.
- BatchReport —After looping on a batch of UUTs, the process model calls the
 PostBatchLoop callback, which is empty in the process model file. Use the
 PostBatchLoop callback to perform an action after testing all batches of
 UUTs.
- ModifyBatchReportHeader —The Test UUTs and Single Pass Execution entry
 points call the report generator process model plug-in, which calls the
 BatchReport callback to generate the contents of the batch report for the UUTs
 that ran in the last batch. The Batch process model defines a batch report for a
 single group of UUTs as a header, an entry for each UUT result, and a footer.
 When you do not want to override the entire BatchReport callback, you can
 override the ModifyBatchReportHeader, ModifyBatchReportEntry, and
 ModifyBatchReportFooter callbacks instead to customize the batch report.
- ModifyBatchReportHeader —The BatchReport callback calls the ModifyBatchReportHeader callback so the client sequence file can modify the batch report header. The ModifyBatchReportHeader callback receives parameters for the batch serial number, the tentative report header text, and the report options. The ModifyBatchReportHeader callback in the process model file is empty.
- ModifyBatchReportEntry —The BatchReport callback uses subsequences to call the ModifyBatchReportEntry callback for each test socket so the client sequence file can modify the entry for each UUT result for each test socket. The ModifyBatchReportEntry callback receives parameters for the test socket data, the batch serial number, the tentative report entry text, and the report options. The ModifyBatchReportEntry callback in the process model file is empty.
- ModifyBatchReportFooter —The BatchReport callback calls the ModifyBatchReportFooter callback so the client sequence file can modify the batch report footer. The ModifyBatchReportFooter callback receives parameters for the tentative report footer text and the report options. The ModifyBatchReportFooter callback in the process model file is empty.

Parent topic:

Batch Process Model

Related concepts:

- Test UUTs – Test Socket Entry Point Execution Entry Point in the Batch Process Model
- Single Pass - Test Socket Entry Point in the Batch Process Model
- Model Callbacks in the Batch Process Model
- TestStand Directory Structure
- Model Plugin – Begin
- Model Plugin – Initialize
- Model Plug in Client-File Callbacks
- Model Plugin – UUT Done
- On-the-Fly Report Generation
- On-the-Fly Database Logging
- ATML
- Main Execution Entry Points in the Batch Process Model
- Hidden Execution Entry Points in the Batch Process Model
- Overriding PreBatch and PostBatch Model Callbacks
- Overriding PreUUT and PostUUT Batch Model Callbacks
- Report Generation Functions and Sequences
- Utility Sequences in the Batch Process Model

<!--NI_TOPIC bundle=teststand path=model-callbacks-in-the-parallel-process-model.html language=enus -->
## TOPIC 00584: Model Callbacks in the Parallel Process Model

- bundle_id: `teststand`
- source_path: `model-callbacks-in-the-parallel-process-model.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/model-callbacks-in-the-parallel-process-model.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Parallel process model includes the following Model callbacks, which you can override with client sequence files: MainSequence—The Test UUTs - Test Socket Entry Point and Single Pass - Test Socket Entry Point sequences call the MainSequence callback, which is empty in the process model file. The

### Model Callbacks in the Parallel Process Model

The Parallel process model includes the following Model callbacks, which you can override with client sequence files:

- MainSequence —The Test UUTs - Test Socket
 Entry Point and Single Pass - Test Socket
 Entry Point sequences call the MainSequence callback, which is empty in the
 process model file. The client sequence file must contain a
 MainSequence callback that performs the tests on a
 UUT.
- PreMainSequence —The Test UUTs and Single Pass sequences call the
 PreMainSequence callback before the MainSequence executes. The PreMainSequence
 callback in the process model file is empty. Override this in the client file to
 perform an action before any code in the MainSequence executes.
- PostMainSequence —The Test UUTs and Single Pass sequences call the
 PostMainSequence callback after the MainSequence executes. The PostMainSequence
 callback in the process model file is empty. Override this in the client file to
 perform an action after all code in the MainSequence executes but before any
 Model Plug-ins execute.
- PreUUT —Calls the DoPreUUT sequence, which launches the UUT Information
 dialog box to obtain the UUT serial numbers for the test sockets. The Test UUTs
 — Test Socket Entry Point sequence calls the PreUUT callback at the beginning of
 each iteration of the UUT loop. When the operator enters a serial number, the
 code for the dialog box stores the serial number in the
 TestSocket.UUT.SerialNumber parameter. When the
 operator stops testing, the UUT loop terminates, and the code for the dialog box
 sets the TestSocket.ContinueTesting parameter to
 False .
- PostUUT —Calls the DoPostUUT sequence, which displays a pass, fail, error,
 or terminate banner to indicate the status of the test the
 MainSequence callback in the client sequence file performs
 on the UUT. The Test UUTs — Test Socket Entry Point sequence calls the PostUUT
 callback at the end of each iteration of the UUT loop.
- PreUUTLoop —Before the UUT loop begins, the Test UUTs — Test Socket Entry
 Point sequence calls the PreUUTLoop callback, which is empty in the process
 model file.
- PostUUTLoop —After the UUT loop terminates, the Test UUTs — Test Socket
 Entry Point sequence calls the PostUUTLoop callback, which is empty in the
 process model file.
- ReportOptions —The process model Execution entry point sequence calls the
 Model
 Plugins – Begin sequence in ModelSupport.seq . Model
 Plugins – Begin calls the Model Plugin –
 Initialize sequence in each plug-in instance. Model Plugin –
 Initialize in the NI_ReportGenerator.seq plug-in calls the
 ReportOptions callback so the client sequence file can modify the report
 options. The ReportOptions callback in the process model file is empty. This
 callback serves the same purpose as the more general ModelPluginOptions
 callback, but the report generator plug-in calls ReportOptions only for report
 generator plug-in instances and passes to it only reporting options.
- DatabaseOptions —The process model Execution entry point sequence calls
 the Model
 Plugins – Begin sequence in ModelSupport.seq . Model
 Plugins – Begin calls the Model Plugin –
 Initialize sequence in each plug-in instance. Model Plugin –
 Initialize in the NI_DatabaseLogger.seq plug-in calls the
 DatabaseOptions callback so the client sequence file can modify the database
 options. The DatabaseOptions callback in the process model file is empty. This
 callback serves the same purpose as the more general ModelPluginOptions
 callback, but the database logging plug-in calls DatabaseOptions only for
 database logging plug-in instances and passes to it only database options.
- ModelOptions —The process model Execution entry point sequence calls the
 Initialize Execution entry point sequence in ModelSupport.seq .
 After reading the test station model options from disk, the sequence calls the
 ModelOptions callback so the client sequence file can modify the model options.
 The ModelOptions callback in the process model file is empty. The client
 sequence file can change the value of the
 ModelPluginConfigurationToLoad parameter to specify
 the name of the model plug-in configuration to load from each model plug-in
 configuration file. The default value for the
 ModelPluginConfigurationToLoad parameter is an empty
 string, which directs the process model to load the active configuration from
 each model plug-in configuration file.
- TestReport —The Test UUTs and Single Pass Execution entry points call the
 Model Plugins – UUT Done sequence in ModelSupport.seq .
 ModelSupport.seq calls the Model Plugin – UUT Done entry
 point for each configured result processor. The
 NI_ReportGenerator.seq plug-in calls the TestReport
 callback from the UUT Done entry point to generate the contents of the report
 for one UUT. The report generator does not call the TestReport callback when you
 enable the On-The-Fly Reporting option in the Report Options dialog box. The
 report plug-in defines a report for a single UUT as a header, an entry for each
 step result, and a footer. When you do not want to override the entire
 TestReport callback, you can override the ModifyReportHeader, ModifyReportEntry,
 and ModifyReportFooter callbacks instead to customize the report. You can
 override ModifyReportEntry only when you select the Sequence option in the
 Report Options dialog box and the report format is HTML or ASCII text. The
 TestReport callback returns the report using the
 Report string parameter or the
 ReportSection object reference parameter.
 TestStand 2010 SP1 or earlier process models use the
 Report parameter. TestStand 2012 or later process
 models use the ReportSection parameter. If you
 override the TestReport callback, you must support the parameter that
 corresponds to the version of the process models you use. To support both
 methods of returning a report, use the ReportSection
 parameter to determine which parameter the invoking process model requires.
 If the ReportSection reference uses
 Nothing as the value, you must return the report as a
 string in the Report parameter. If the
 ReportSection reference uses a value other than
 Nothing, you must return the report by updating the
 ReportSection parameter. For HTML and ASCII
 text report formats, depending on the settings in the Report Options dialog
 box, the TestReport callback determines whether TestStand uses sequences or
 a DLL to build the report body. Select the Sequence option to more easily
 modify the reports TestStand generates. Select the DLL option to generate
 reports more efficiently. When you select the Sequence option in the
 Report Options dialog box, the TestReport callback calls the AddReportBody
 sequence in reportgen_html.seq or
 reportgen_txt.seq to build the report body. The report
 generator plug-in uses a series of sequences with steps that recursively
 process the result list for the execution. When you select the DLL option in
 the Report Options dialog box, the TestReport callback calls a function in
 modelsupport2.dll to build the report body. You can
 access the project and source code for the DLL built in LabWindows/CVI from
 the <TestStand>\Components\Models\TestStandModels
 directory. For XML reports, TestReport callback calls the
 AddReportBody sequence in reportgen_xml.seq. The report
 generator plug-in calls the PropertyObject.GetXML method. For ATML 2
 reports, the TestReport callback calls the GetATMLReport sequence in
 reportgen_atml.seq. The report generator plug-in in
 calls the Get_Atml_Report function in
 ATMLSupport.dll in the LabWindows/CVI project. For ATML
 5 reports, the TestReport callback calls the AddReportBody sequence in
 reportgen_atml.seq. The report generator plug-in calls
 the Get_Atml_ReportSection_For_Body function in
 ATMLSupport.dll. You can access the project and source
 code for the DLL built in LabWindows/CVI from the
 <TestStand>\Components\Models\TestStandModels\ATML
 directory.
- ModifyReportHeader —The TestReport callback calls the ModifyReportHeader callback so the client sequence file can modify the report header. The ModifyReportHeader callback receives parameters for the UUT information, the tentative report header text, and the report options. The ModifyReportHeader callback in the process model file is empty.
- GetReportFilePath —The report generator process model plug-in calls the GetReportFilePath callback so the client sequence file can inspect the report file path.
- ModifyReportEntry —The TestReport callback uses subsequences to call the ModifyReportEntry callback for each result in the result list for the UUT so the client sequence file can modify the entry point for each step result. The ModifyReportEntry callback receives parameters for an entry from the result list, the UUT information, the tentative report entry text, the report options, and a number that indicates the call stack depth at the time the step executed. TestStand does not call ModifyReportEntry callbacks when you enabled the DLL option in the Report Options dialog box. Instead, you must modify modelsupport2.dll , located in the <TestStand>\Components\Models\TestStandModels directory, to modify how step results appear in the report. The ModifyReportEntry callback in the process model file is empty.
- ModifyReportFooter —The TestReport callback calls the ModifyReportFooter callback so the client sequence file can modify the report footer. The ModifyReportFooter callback receives parameters for the UUT information, the tentative report footer text, and the report options. The ModifyReportFooter callback in the process model file is empty.
- LogToDatabase —Execution entry points call the LogToDatabase callback to
 populate a database with the results for one UUT. Execution entry points do not
 call the LogToDatabase callback when you enabled the Use On-The-Fly
 Logging option on the Logging Options tab of the Database Options
 dialog box. The LogToDatabase callback receives parameters for the UUT
 information, the result list for the UUT, and the database options.
- ProcessSetup —The Test UUTs and Single Pass Execution entry points call
 the ProcessSetup callback before creating the test socket executions so the
 client sequence file can execute any setup steps that must run only once during
 the execution of the process model. Only the controlling execution calls
 ProcessSetup. The test socket executions do not call the ProcessSetup
 callback.
- ProcessCleanup —The Test UUTs and Single Pass Execution entry points call
 the ProcessCleanup callback from the Cleanup step group so the client sequence
 file can execute any cleanup steps that must run only once during the execution
 of the process model. Only the controlling execution calls ProcessCleanup. The
 test socket executions do not call the ProcessCleanup callback.
- ModelPluginOptions —Execution entry points call the Model Plugins – Begin sequence in ModelSupport.seq , which calls the Initialize Model Plugins sequence. Initialize Model Plugins calls the ModelPluginOptions callback for each model plug-in instance so the client file can modify the model plug-in settings.
- ModelPluginConfiguration —Execution entry points call the Model Plugins – Begin sequence in ModelSupport.seq , which calls the Initialize Model Plugins sequence. Initialize Model Plugins calls the ModelPluginConfiguration callback so the client file can inspect or modify the set of model plug-ins the process model calls at run time.

Parent topic:

Parallel Process Model

Related concepts:

- Test UUTs – Test Socket Entry Point Execution Entry Point in the Parallel Process Model
- Single Pass - Test Socket Execution Entry Point in the Parallel Process Model
- Model Callbacks in the Batch Process Model
- Model Plugin – Begin
- Model Plugin – Initialize
- Model Plug in Client-File Callbacks
- Model Plugin – UUT Done
- On-the-Fly Report Generation
- TestStand Directory Structure
- On-the-Fly Database Logging
- Overriding PreUUT and PostUUT Parallel Model Callbacks

<!--NI_TOPIC bundle=teststand path=model-callbacks-in-the-sequential-process-mod.html language=enus -->
## TOPIC 00585: Model Callbacks in the Sequential Process Model

- bundle_id: `teststand`
- source_path: `model-callbacks-in-the-sequential-process-mod.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/model-callbacks-in-the-sequential-process-mod.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Sequential process model includes the following Model callbacks, which you can override with client sequence files: MainSequence—Test UUTs and Single Pass Execution entry point sequences call the MainSequence callback, which is empty in the process model file. The client sequence file must conta

### Model Callbacks in the Sequential Process Model

The Sequential process model includes the following Model callbacks, which you can override with client sequence files:

- MainSequence —Test UUTs and Single
 Pass
Execution
 entry point sequences call the MainSequence callback, which is empty in the
 process model file. The client sequence file must contain a
 MainSequence callback that performs the tests on a
 UUT.
- PreMainSequence —The Test UUTs and Single Pass sequences call the
 PreMainSequence callback before the MainSequence executes. The PreMainSequence
 callback in the process model file is empty. Override this in the client file to
 perform an action before any code in the MainSequence executes.
- PostMainSequence —The Test UUTs and Single Pass sequences call the
 PostMainSequence callback after the MainSequence executes. The PostMainSequence
 callback in the process model file is empty. Override this in the client file to
 perform an action after all code in the MainSequence executes but before any
 Model Plug-ins execute.
- PreUUT —Calls the DoPreUUT sequence, which launches the UUT Information
 dialog box to obtain the UUT serial number. The Test UUTs Execution entry point
 calls the PreUUT callback at the beginning of each iteration of the UUT loop.
 When the operator enters a UUT serial number, the IdentifyUUT step stores the
 serial number in the UUT.SerialNumber parameter, which is
 a local variable the Test UUTs sequence passes to the PreUUT callback. When the
 operator stops testing, the UUT loop terminates, and the IdentifyUUT step sets
 the ContinueTesting parameter to False .
 The ContinueTesting parameter is another local variable
 the Test UUTs sequence passes to the PreUUT callback.
- PostUUT —Calls the DoPostUUT sequence, which displays a pass, fail, error,
 or terminate banner to indicate the status of the test the
 MainSequence callback in the client sequence file performs
 on the UUT. The Test UUTs Execution entry point calls the PostUUT callback at
 the end of each iteration of the UUT loop.
- PreUUTLoop —Before the UUT loop begins, the Test UUTs Execution entry
 point calls the PreUUTLoop callback, which is empty in the process model file.
- PostUUTLoop —After the UUT loop terminates, the Test UUTs Execution entry
 point calls the PostUUTLoop callback, which is empty in the process model file.
- ReportOptions —The process model Execution entry point sequence calls the
 Model
 Plugins – Begin sequence in ModelSupport.seq . Model
 Plugins – Begin calls the Model Plugin –
 Initialize sequence in each plug-in instance. Model Plugin –
 Initialize in the NI_ReportGenerator.seq plug-in calls the
 ReportOptions callback so the client sequence file can modify the report
 options. The ReportOptions callback in the process model file is empty. This
 callback serves the same purpose as the more general ModelPluginOptions
 callback, but the report generator plug-in calls ReportOptions only for report
 generator plug-in instances and passes to it only reporting options.
- DatabaseOptions —The process model Execution entry point sequence calls
 the Model
 Plugins – Begin sequence in ModelSupport.seq . Model
 Plugins – Begin calls the Model Plugin –
 Initialize sequence in each plug-in instance. Model Plugin –
 Initialize in the NI_DatabaseLogger.seq plug-in calls the
 DatabaseOptions callback so the client sequence file can modify the database
 options. The DatabaseOptions callback in the process model file is empty. This
 callback serves the same purpose as the more general ModelPluginOptions
 callback, but the database logging plug-in calls DatabaseOptions only for
 database logging plug-in instances and passes to it only database options.
- ModelOptions —The process model Execution entry point sequence calls the
 Initialize Execution entry point sequence in ModelSupport.seq .
 After reading the test station model options from disk, the sequence calls the
 ModelOptions callback so the client sequence file can modify the model options.
 The ModelOptions callback in the process model file is empty. The client
 sequence file can change the value of the
 ModelPluginConfigurationToLoad parameter to specify
 the name of the model plug-in configuration to load from each model plug-in
 configuration file. The default value for the
 ModelPluginConfigurationToLoad parameter is an empty
 string, which directs the process model to load the active configuration from
 each model plug-in configuration file.
- TestReport —The Test UUTs and Single Pass Execution entry points call the
 Model
 Plugins – UUT Done sequence in ModelSupport.seq .
 ModelSupport.seq calls the Model Plugin – UUT Done entry
 point for each configured result processor. The
 NI_ReportGenerator.seq plug-in calls the TestReport
 callback from the UUT Done entry point to generate the contents of the report
 for one UUT. The report generator does not call the TestReport callback when you
 enable the On-The-Fly Reporting option in the Report Options dialog box. The
 report plug-in defines a report for a single UUT as a header, an entry for each
 step result, and a footer. When you do not want to override the entire
 TestReport callback, you can override the ModifyReportHeader, ModifyReportEntry,
 and ModifyReportFooter callbacks instead to customize the report. You can
 override ModifyReportEntry only when you select the Sequence option in the
 Report Options dialog box and the report format is HTML or ASCII text.The
 TestReport callback returns the report using the Report 
 string parameter or the ReportSection object reference
 parameter. TestStand 2010 SP1 or earlier process models use the
 Report parameter. TestStand 2012 or later process
 models use the ReportSection parameter. If you override
 the TestReport callback, you must support the parameter that corresponds to the
 version of the process models you use. To support both methods of returning a
 report, use the ReportSection parameter to determine
 which parameter the invoking process model requires. If the
 ReportSection reference uses Nothing 
 as the value, you must return the report as a string in the
 Report parameter. If the
 ReportSection reference uses a value other than
 Nothing , you must return the report by updating the
 ReportSection parameter.For HTML and ASCII text
 report formats, depending on the settings in the Report Options dialog box, the
 TestReport callback determines whether TestStand uses sequences or a DLL to
 build the report body. Select the Sequence option to more easily modify the
 reports TestStand generates. Select the DLL option to generate reports more
 efficiently.When you select the Sequence option in the Report Options dialog
 box, the TestReport callback calls the AddReportBody sequence in
 reportgen_html.seq or reportgen_txt.seq to
 build the report body. The report generator plug-in uses a series of sequences
 with steps that recursively process the result list for the execution. When you
 select the DLL option in the Report Options dialog box, the TestReport callback
 calls a function in modelsupport2.dll to build the report body.
 You can access the project and source code for the DLL built in LabWindows/CVI
 from the <TestStand>\Components\Models\TestStandModels 
 directory.For XML reports, TestReport callback calls the AddReportBody sequence
 in reportgen_xml.seq . The report generator plug-in calls the
 PropertyObject.GetXML method. For ATML 2 reports, the TestReport callback calls
 the GetATMLReport sequence in reportgen_atml.seq . The report
 generator plug-in in calls the Get_Atml_Report function in
 ATMLSupport.dll in the LabWindows/CVI project. For ATML 5
 reports, the TestReport callback calls the AddReportBody sequence in
 reportgen_atml.seq . The report generator plug-in calls the
 Get_Atml_ReportSection_For_Body function in
 ATMLSupport.dll . You can access the project and source code
 for the DLL built in LabWindows/CVI from the <TestStand>\Components\Models\TestStandModels\ATML 
 directory.
- ModifyReportHeader —The TestReport callback calls the ModifyReportHeader
 callback so the client sequence file can modify the report header. The
 ModifyReportHeader callback receives parameters for the UUT information, the
 tentative report header text, and the report options. The ModifyReportHeader
 callback in the process model file is empty.
- ModifyReportEntry —The TestReport callback uses subsequences to call the
 ModifyReportEntry callback for each result in the result list for the UUT so the
 client sequence file can modify the entry point for each step result. The
 ModifyReportEntry callback receives parameters for an entry from the result
 list, the UUT information, the tentative report entry text, the report options,
 and a number that indicates the call stack depth at the time the step executed.
 TestStand calls ModifyReportEntry callbacks when you generate HTML or ASCII text
 reports and enabled the Sequence option in the Report Options dialog box. In all
 other cases, you must modify modelsupport2.dll , located in the
 <TestStand>\Components\Models\TestStandModels 
 directory, to modify how step results appear in the report. The
 ModifyReportEntry callback in the process model file is empty.
- ModifyReportFooter —The TestReport callback calls the ModifyReportFooter callback so the client sequence file can modify the report footer. The ModifyReportFooter callback receives parameters for the UUT information, the tentative report footer text, and the report options. The ModifyReportFooter callback in the process model file is empty.
- GetReportFilePath —The report generator process model plug-in calls the GetReportFilePath callback so the client sequence file can inspect the report file path.
- LogToDatabase —Execution entry points call the Model Plugins – UUT
 Done sequence in ModelSupport.seq .
 ModelSupport.seq calls the Model Plugin – UUT Done entry
 point for each configured model plug-in. The
 NI_DatabaseLogger.seq plug-in calls the LogToDatabase
 callback from the UUT Done entry point to populate a database with the results
 for one UUT. The database logger does not call the LogToDatabase callback when
 you enable the Use On-The-Fly
 Logging option on the Logging Options tab of the Database Options
 dialog box. The LogToDatabase callback receives parameters for the UUT
 information, the result list for the UUT, and the database options.
- ProcessSetup —The Test UUTs and Single Pass Execution entry points call
 the ProcessSetup callback so the client sequence file can execute any setup
 steps that must run only once during the execution of the process model. The
 Process Setup callback in the process model file is empty.
- ProcessCleanup —The Test UUTs and Single Pass Execution entry points call
 the ProcessCleanup callback from the Cleanup step group so the client sequence
 file can execute any cleanup steps that must run only once during the execution
 of the process model. The Process Cleanup callback in the process model file is
 empty.
- ModelPluginOptions —Execution entry points call the Model Plugins – Begin sequence in ModelSupport.seq , which calls the Initialize Model Plugins sequence. Initialize Model Plugins calls the ModelPluginOptions callback for each model plug-in instance so the client file can modify the model plug-in settings.
- ModelPluginConfiguration —Execution entry points call the Model Plugins – Begin sequence in ModelSupport.seq , which calls the Initialize Model Plugins sequence. Initialize Model Plugins calls the ModelPluginConfiguration callback so the client file can inspect or modify the set of model plug-ins the process model calls at run time.

Parent topic:

Sequential Process Model

Related concepts:

- Test UUTs Execution Entry Point in the Sequential Process Model
- Single Pass Execution Entry Point in the Sequential Process Model
- Execution Entry Points in the Sequential Process Model
- Model Callbacks in the Batch Process Model
- Model Plugin – Begin
- Model Plugin – Initialize
- Model Plug in Client-File Callbacks
- Model Plugin – UUT Done
- On-the-Fly Report Generation
- TestStand Directory Structure
- On-the-Fly Database Logging

<!--NI_TOPIC bundle=teststand path=model-callbacks-you-can-override-to-alter-rep.html language=enus -->
## TOPIC 00586: Model Callbacks You Can Override to Alter Report Generation

- bundle_id: `teststand`
- source_path: `model-callbacks-you-can-override-to-alter-rep.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/model-callbacks-you-can-override-to-alter-rep.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following table lists the report generation Model callbacks you can override to alter the report generation for each client sequence file you run. Section of Report to Alter Model Callback to Override Header ModifyReportHeader Footer ModifyReportFooter Each step result ModifyReportEntryThe repor

### Model Callbacks You Can Override to Alter Report Generation

The following table lists the report generation Model callbacks you can override to alter the report generation for each client sequence file you run.

| Section of Report to Alter | Model Callback to Override |
| --- | --- |
| Header | ModifyReportHeader |
| Footer | ModifyReportFooter |
| Each step result | ModifyReportEntryNote The report generator process model plug-in calls this callback only when you generate HTML or text reports and select the Sequence option in the Select a Report Generator for Producing the Report Body section of the Contents tab of the Report Options dialog box. |
| Entire report | TestReport |
| Batch header | ModifyBatchReportHeader |
| Batch footer | ModifyBatchReportFooter |
| Each test socket result | ModifyBatchReportEntry |
| Entire batch report | BatchReport |

Additionally, you can use the Step.Result.ReportText property for each step in a client sequence file to add text to the step result in the report.

Parent topic:

Report Generation Functions and Sequences

<!--NI_TOPIC bundle=teststand path=model-plug-in-basic-step-time-report.html language=enus -->
## TOPIC 00587: Model Plug-in - Basic Step Time Report

- bundle_id: `teststand`
- source_path: `model-plug-in-basic-step-time-report.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/model-plug-in-basic-step-time-report.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Purpose This example demonstrates how to a basic step time report for each UUT so you can benchmark and analyze the performance of a sequence file. The example generates a summary report, a file of unprocessed data, and a report in format that includes processed time data. You can also run a stand-a

### Model Plug-in - Basic Step Time Report

#### Purpose

This example demonstrates how to a basic step time report for each UUT so you can benchmark and analyze the performance of a sequence file. The example generates a summary report, a file of unprocessed data, and a report in format that includes processed time data. You can also run a stand-alone executable to a basic step time report in .csv format to Excel format. You can basic step time reports in Excel format for multiple UUTs.

#### Example File Location

<TestStand Public>\Examples\Customizing Result Processing\ModelPlugin Basic Step
 Time Report\Install Basic Step Time Report Plugin.seq

#### Highlighted Features

Process model plug-in architecture

#### Major API

None

#### Prerequisites

You must have Microsoft Office Excel 2007 SP2 or later installed on the computer to a basic step time report in Excel format and to run the executable to a .csv file to Excel format. If Excel is not installed on the computer, this custom reporting plug-in generates only a .csv file.

#### How to Use This Example

You can use this example to a basic step time report. The example generates a summary report, a file of unprocessed data, and a report in format that includes processed time data. You can also run a stand-alone executable to a basic step time report in .csv format to Excel format. You can basic step time reports in Excel format for multiple UUTs.

#### Generating a Basic Step Time Report

Complete the following steps to use this example to generate a basic step time report.

1. Open <TestStand Public>\Examples\Customizing Result Processing\ModelPlugin
 Basic Step Time Report\SetupBasicStepTimeReportGenerator.seq , click
 OK in the About This Example dialog box to copy the example and
 support files to the <TestStand
 Public>\Components\Models\ModelPlugins directory, and click
 Yes in the Setup Simple Text Report Example Files dialog
 box.
2. Open a sequence file for which you want to generate a basic step time report.
3. Select Configure»Result Processing to launch the Result Processing dialog box.
4. Select Basic Step Time Report from the context menu to add the Basic Step Time Report plug-in to the active configuration.
5. Enable the checkbox in the Display column of the Basic Step Time Report plug-in to display the HTML summary report in the Report pane.
6. Click the icon in the Options column of the Basic Step Time Report plug-in to launch the Basic Step Time Report Configuration dialog box, in which you specify the directory in which to store the report and specify whether to launch the report in Excel.
7. Click OK in the Basic Step Time Report Configuration dialog box and in the Result Processing dialog box to return to the Sequence File window.
8. Execute the sequence file and view the reports.

#### Convert a .csv File to Excel Format

Complete the following steps to use a stand-alone application to convert a .csv file to Excel format.

1. Launch <TestStand Public>\Examples\Customizing Result Processing\ModelPlugin
 Basic Step Time Report\CsvToBasicStepTimeReportGenerator.exe .
2. Specify the path to the .csv file you want to convert in the Path of CSV Report control and specify the path to the Excel file you want to create in the Path of Basic Step Time Report control.
3. Enable the Launch Basic Step Time Report to open the report in Excel option and click OK .
4. View the report in Excel.

You can also use command-line arguments to launch the stand-alone application, specify the path to the .csv file, specify the path of the Excel file you want to create, and optionally display the file in Excel as follows:

CsvToBasicStepTimeReportGenerator.exe <Path of CSV Report> <Path of Excel File to Create> [/display]

#### Aggregating Basic Step Time Reports in Excel Format for Multiple UUTs

Complete the following steps to aggregate basic step time reports in Excel for multiple UUTs. The value in the ID column of the Raw Data worksheet must be unique across all the reports you want to aggregate.

1. Open the reports you want to combine in Excel.
2. In the main report file into which you want to aggregate all the data, unprotect the Raw Data worksheet.
3. Complete the following steps for each report file you want to aggregate into the main report file.
  1. From the Raw Data worksheet, copy the rows that correspond to the steps you want to include in the main report file.
  2. Paste the data you copied into the Steps section of the Raw Data worksheet of the main report file.
4. In the Raw Data worksheet of the main report file, click the Regenerate Processed Data and Graphs button update and overwrite the existing data and graphs in the Step, Sequence, and Sequence File worksheets.

#### Reports the Basic Step Time Report Generator Plug-In Creates

The Basic Step Time Report Generator plug-in generates a single report file for each UUT in , , and formats using the following filename format:

[Station ID][Sequence File Name][Test Socket Index][Batch Serial Number][UUT Serial Number][Time][Date].[html|csv|xls]

Microsoft Windows and Excel limit the number of characters in a file path. If the length of the file path for generated reports is less than 218 characters, the Basic Step Time Report Generator plug-in generates reports in HTML, .csv, and Excel format. If the length of the file path for generated reports is between 218 and 260 characters, the Basic Step Time Report Generator plug-in generates reports only in HTML and .csv formats. If the length of the file path for generated reports exceeds 260 characters, the Basic Step Time Report Generator plug-in does not generate any report and returns an error before executing the sequence file.

The Basic Step Time Report plug-in uses an underscore (_) in the place of the # character and invalid filename characters in a UUT or batch serial number.

#### HTML

TestStand displays the HTML report in the Report pane, and the HTML report links to the .csv and Excel reports.

The HTML report includes the following information for each UUT in the report header:

- Station ID
- Operator
- UUT Part Number (if non-empty)
- UUT Serial Number
- Batch Serial Number (if using the Batch model)
- TestSocket Index (if using the Batch or Parallel model)
- Date
- Time
- Execution Time
- UUT Result
- TSR Filename (if using the TestStand Offline Results Processing Utility)
- TSR ID (if using the TestStand Offline Results Processing Utility)
- TSR File Closed (if using the TestStand Offline Results Processing Utility)

#### .csv

The .csv report includes the following information for each UUT in the report header:

- Station ID
- Operator
- UUT Part Number (if non-empty)
- UUT Serial Number
- Batch Serial Number (if using the Batch model)
- TestSocket Index (if using the Batch or Parallel model)
- Date
- Time
- Execution Time
- UUT Result
- CSV File Format Version
- TSR Filename (if using the TestStand Offline Results Processing Utility)
- TSR ID (if using the TestStand Offline Results Processing Utility)
- TSR File Closed (if using the TestStand Offline Results Processing Utility)

For each step, the report includes the following information:

- Sequence Filename—Name of the sequence file that contains the step
- Sequence Name—Name of the sequence that contains the step
- Step Group—Name of the step group that contains the step
- Step ID—Unique ID of the step
- Step Name—Name of the step
- Parent ID—ID of the parent sequence call step
- Step Type—Type of the step
- ID—Unique execution ID of the step
- Status—Execution status of the step
- Start Time—Execution start time of the step
- Total Time—Total time the step takes to complete execution
- Module Time—Time the code module of the step takes or empty if the step uses the None adapter
- Sequence Call Sequence Filename—Path of the sequence file a non-asynchronous Sequence Call step calls
- Sequence Call Sequence Name—Name of the sequence a non-asynchronous Sequence Call step calls
- Number of Loops—Number of loops the step executes or empty if the step does not use looping
- Ending Loop Index—Index of the last iteration of the loop for the step or empty if the step does not use looping
- Loop Index—Index of the current iteration of the loop for the step or empty if the step does not use looping
- UUT Serial Number—Serial number of the UUT
- Batch Serial Number—Serial number of the batch that contains the UUT
- TestSocket Index—Index of the test socket the UUT uses

Note

#### Excel

The Excel report includes the following information for each UUT in an Excel workbook with the following worksheets:

- Step—Contains the following processed data for the steps used to test the UUT and graphs to show the average total time of the steps and the cumulative total time of the steps. You can modify the data and graphs in this worksheet. Note This worksheet does not contain information for the MainSequence Callback step from process model files.
  - Step Name
  - Step ID
  - Cumulative Total Time (of the step)
  - Cumulative Module Time (of the step)
  - Number of Execution
  - Average Total Time
  - Average Module Time
  - Max Total Time
  - Max Module Time
  - Min Total Time
  - Min Module Time
- Sequence—Contains the following processed data for the sequences used to test the UUT and graphs to show the average total time of the sequences and the percentage of the cumulative total time of the sequences. You can modify the data and graphs in this worksheet. Note This worksheet contains information only for non-asynchronous Sequence Call steps. You can modify the source code to insert data for Post Action Sequence Call, callback sequence, and asynchronous Sequence Call steps.
  - Sequence File Name
  - Sequence Name
  - Cumulative Total Time (of each Sequence Call step that calls the sequence, including subsequence time)
  - Cumulative Total Time (of each Sequence Call step that calls the sequence, excluding subsequence time)
  - Number of Times Sequence Call Steps Call into the Sequence
  - Average Total Time (excluding subsequence time)
  - Max Total Time (excluding subsequence time)
  - Min Total Time (excluding subsequence time)
- Sequence File—Contains the following processed data for the sequence files used to test the UUT and graphs to show the cumulative total time of the sequence files and the percentage of total time for the sequence files. You can modify the data and graphs in this worksheet.
  - Sequence Filename
  - Cumulative Total Time (of Sequence Call steps calling any sequence in the sequence file)
- Raw Data—Contains all the data from the .csv file in protected mode. Click the Regenerate Processed Data and Graphs button to update and overwrite the existing data and graphs in the Step, Sequence, and Sequence File worksheets.

Parent topic:

Examples for Customizing Result Processing

Related concepts:

- TestStand Directory Structure
- Process Model Plug-In Architecture

<!--NI_TOPIC bundle=teststand path=model-plug-in-categories.html language=enus -->
## TOPIC 00588: Model Plug-in Categories

- bundle_id: `teststand`
- source_path: `model-plug-in-categories.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/model-plug-in-categories.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Each model plug-in file specifies a category name to determine when a plug-in can be invoked or made available. For example, in the Result Processing dialog box, you can insert only plug-in instances with the "ResultProcessor" category name. Similarly, the Offline Results Processing Utility invokes

### Model Plug-in Categories

Each model plug-in file specifies a category name to determine when a plug-in can be invoked or made available. For example, in the Result Processing dialog box, you can insert only plug-in instances with the "ResultProcessor" category name. Similarly, the Offline Results Processing Utility invokes only plug-ins with the "ResultProcessor" category name. Therefore, do not use "ResultProcessor" as the category name for a plug-in you create that does not act as a result processor.

TestStand currently includes only results processing model plug-ins. You can use custom category names to define categories of model plug-ins you create that perform tasks other than results processing. For example, you might create categories of model plug-ins for automatically detecting and storing UUT serial numbers or for exchanging data with Enterprise Resource Planning systems.

Parent topic:

Configuring Process Model Plug-ins

<!--NI_TOPIC bundle=teststand path=model-plug-in-client-file-callbacks.html language=enus -->
## TOPIC 00589: Model Plug in Client-File Callbacks

- bundle_id: `teststand`
- source_path: `model-plug-in-client-file-callbacks.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/model-plug-in-client-file-callbacks.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: A client file can override the ModelPluginOptions or the ModelPluginConfiguration model callback to inspect or alter the plug-in options an end user configures. ModelPluginOptions The model calls the ModelPluginOptions callback once for each plug-in instance and passes the instance to the ModelPlugi

### Model Plug in Client-File Callbacks

A client file can override the ModelPluginOptions or the ModelPluginConfiguration model callback to inspect or alter the plug-in options an end user configures.

#### ModelPluginOptions

The model calls the ModelPluginOptions callback once for each plug-in instance and passes the instance to the ModelPlugin parameter. Use the subproperties of the Parameters.ModelPlugin.PluginSpecific.Options property to access plug-in-specific options. Use the Parameters.ModelPlugin.Base.SequenceFileName property to determine the plug-in to which the instance data belongs. The model calls the Model Plugin – Initialize entry point for each plug-in instance before calling the ModelPluginOptions callback so you can programmatically initialize or modify the plug-in instance before the model passes the instance to the client sequence file.

The NI_DatabaseLogger and the NI_ReportGenerator plug-ins also provide plug-in-specific DatabaseOptions and ReportOptions callbacks that client sequence files can override to access plug-in-specific options.

#### ModelPluginConfiguration

The model calls the ModelPluginConfiguration callback one time after calling the ModelPluginOptions callback for every plug-in instance. The model passes the entire set of configured plug-ins to the ModelPluginConfiguration parameter. Iterate through the Parameters.ModelPluginConfiguration.Plugins array to access each configured plug-in.

You can replace or reorder elements of the Parameters.ModelPluginConfiguration.Plugins array. You must ensure that the <NI_ModelPlugin>.Base.RuntimeVariables.InitializationState property is set to zero for each plug-in you add to the array. After the ModelPluginConfiguration callback completes, the process model calls the Model Plugin – Initialize entry point and the ModelPluginOptions callback for each plug-in in the array with a <NI_ModelPlugin>.Base.RuntimeVariables.InitializationState property set to zero.

Parent topic:

Process Model Plug-In Architecture

Related concepts:

- Model Plugin – Initialize

<!--NI_TOPIC bundle=teststand path=model-plug-in-entry-points.html language=enus -->
## TOPIC 00590: Model Plug-in Entry Points

- bundle_id: `teststand`
- source_path: `model-plug-in-entry-points.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/model-plug-in-entry-points.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: TestStand process models invoke model plug-ins by calling the following set of optional entry point sequences with a pre-defined set of parameters at specific points in the testing process. Model Plugin – Configure Standard Options Model Plugin – Configure Additional Options Model Plugin – Initializ

### Model Plug-in Entry Points

TestStand process models invoke model plug-ins by calling the following set of optional
 entry point sequences with a pre-defined set of parameters at specific points in the testing
 process.

- Model Plugin – Configure Standard Options
- Model Plugin – Configure Additional Options
- Model Plugin – Initialize
- Model Plugin – Begin
- Model Plugin – Pre Batch
- Model Plugin – Pre UUT
- Model Plugin – Batch Start
- Model Plugin – UUT Start
- Model Plugin – OnTheFly Step Results
- Model Plugin – UUT Done
- Model Plugin – Batch Done
- Model Plugin – Post UUT
- Model Plugin – Post Batch
- Model Plugin – End

To simplify the model plug-ins you create, implement only the entry points you need to
 perform specific tasks. The Configure Standard Options and the Configure Additional Options
 entry points provide functionality you invoke to allow end users to edit a model plug-in
 configuration. Process models invoke the remaining entry points at run time from the
 locations shown in bold text in the following tables.

Note

| Sequential Model Plug-in Entry Point Run-Time Order for Controller and Socket Threads |
| --- |
| Model Plugin - Initialize ModelOptions Callback Model Plugin - Begin Process Setup PreUUTLoop Callback [Begin UUT Loop] PreUUT Callback Model Plugin - Pre UUT If (!continueTesting) goto [End of UUT Loop] Model Plugin - UUT Start PreMainSequence Callback MainSequence Callback PostMainSequence Callback Model Plugin - OnTheFly Step Results Model Plugin - UUT Done Model Plugin - Post UUT PostUUT Callback [End of UUT Loop] PostUUTLoop Callback Process Cleanup Callback Model Plugin - End |

Note

| Parallel Model Plug-in Entry Point Run-Time Order |  |
| --- | --- |
| Controller Thread | Test Socket Threads |
| Model Plugin - Initialize ModelOptions Callback Model Plugin - Begin Process Setup |  |
|  | Model Plugin - Begin PreUUTLoop Callback [Begin UUT Loop] PreUUT Callback Model Plugin - Pre UUT If (!continueTesting) goto [End of UUT Loop] Model Plugin - UUT Start PreMainSequence Callback MainSequence Callback PostMainSequence Callback Model Plugin - OnTheFly Step Results Model Plugin - UUT Done Model Plugin - Post UUT PostUUT Callback [End of UUT Loop] PostUUTLoop Callback Model Plugin - End |
| Process Cleanup Callback Model Plugin - End |  |

| Batch Model Plug-in Entry Point Run-Time Order |  |
| --- | --- |
| Controller Thread | Test Socket Threads |
| Model Plugin - Initialize ModelOptions Callback Model Plugin - Begin Process Setup PreBatchLoop Callback |  |
|  | Model Plugin - Begin PreUUTLoop Callback |
| [Begin Batch Loop] PreBatch Callback Model Plugin - Pre Batch If (!continueTesting) goto [End of Batch Loop] |  |
| Model Plugin - Batch Start | [Begin UUT Loop] PreUUT Callback Model Plugin - Pre UUT If (!continueTesting) goto [End of UUT Loop] Model Plugin - UUT Start |
|  | PreMainSequence Callback MainSequence Callback PostMainSequence Callback Model Plugin - OnTheFly Step Results |
| Model Plugin -Batch Done | Model Plugin - UUT Done |
|  | Model Plugin - Post UUT PostUUT Callback |
| Model Plugin - Post Batch PostBatch Callback |  |
| [End of Batch Loop] | [End of UUT Loop] PostUUTLoop Callback Model Plugin - End |
| PostBatchLoop Callback Process Cleanup Callback Model Plugin - End |  |

Parent topic:

Structure of Plug-in Sequence Files

Related concepts:

- Plug-in Entry Point Parameters
- Model Plugin – Configure Standard Options
- Model Plugin – Configure Additional Options
- Model Plugin – Initialize
- Model Plugin – Begin
- Model Plugin – Pre Batch
- Model Plugin – Pre UUT
- Model Plugin – Batch Start
- Model Plugin – UUT Start
- Model Plugin – OnTheFly Step Results
- Model Plugin – UUT Done
- Model Plugin – Batch Done
- Model Plugin – Post UUT
- Model Plugin – Post Batch
- Model Plugin – End
- Batch Controller and Test Socket Synchronization Architecture

<!--NI_TOPIC bundle=teststand path=model-plug-in-simple-text-report.html language=enus -->
## TOPIC 00591: Model Plug-in - Simple Text Report

- bundle_id: `teststand`
- source_path: `model-plug-in-simple-text-report.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/model-plug-in-simple-text-report.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: <TestStand Public>\Examples\Customizing Result Processing\ModelPlugin Simple Text Report Purpose This example demonstrates how to implement a result processing process model plug-in using LabVIEW, LabWindows/CVI, and Microsoft Visual C#. Example File Location <TestStand Public>\Examples\Customizing

### Model Plug-in - Simple Text Report

<TestStand Public>\Examples\Customizing Result Processing\ModelPlugin Simple Text
 Report

#### Purpose

This example demonstrates how to implement a result processing process model plug-in using LabVIEW, LabWindows/CVI, and Microsoft Visual C#.

#### Example File Location

<TestStand Public>\Examples\Customizing Result Processing\ModelPlugin Simple Text
 Report\Install Simple Text Report Plugin.seq

#### Highlighted Features

Process model plug-in architecture

#### Major API

N/A

#### Prerequisites

None

#### How to Use This Example

You can use the <TestStand Public>\Examples\Customizing Result
 Processing\ModelPlugin Simple Text Report\SetupExamplePlugin.seq example sequence
 file to install a result processing process model plug-in that generates a simple text
 report you can use for system monitoring and debugging. NI recommends using the Microsoft
 Visual C# version if you intend to use the simple text reporting functionality only as
 provided.

#### LabVIEW

Complete the following steps to build and use the LabVIEW version of this example.

1. Open the <TestStand Public>\Examples\Customizing Result
 Processing\ModelPlugin Simple Text Report\LabVIEW\SimpleTextPlugin.lvproj file
 in LabVIEW.
2. Build the Build Simple Text Plugin build specification.
3. Confirm that the following files exist:
  - <TestStand Public>\Components\Models\ModelPlugins\NI_SimpleTextReport_LabVIEW\SimpleTextPlugin.llb
  - <TestStand Public>\Components\Models\ModelPlugins\NI_SimpleTextReport_LabVIEW.seq
4. Add and enable an instance of the LabVIEW simple text report process model plug-in in the Result Processing dialog box.

#### LabWindows/CVI

Complete the following steps to build and use the LabWindows/CVI version of this example.

1. Open the <TestStand Public>Examples\Customizing Result Processing\Model Plugin - Simple Text Report\CVI\SimpleTextReport.cws file in LabWindows/CVI.
2. Select Build»Create Debuggable Dynamic Link Library .
3. Copy the <TestStand Public>\Examples\Customizing Result
 Processing\ModelPlugin Simple Text Report\CVI\NI_SimpleTextReport_CVI.seq file
 to the <TestStand Public>\Components\Models\ModelPlugins 
 directory.
4. Confirm that the <TestStand Public>\Components\Models\ModelPlugins\NI_SimpleTextReport_CVI\NI_SimpleTextReport_CVI.dll file exists and has been overwritten by the version you just built.
5. Add and enable an instance of the LabWindows/CVI simple text report process model plug-in in the Result Processing dialog box.

#### Microsoft Visual C#

Complete the following steps to build and use the Microsoft Visual C# version of this example.

1. Open and build the <TestStand Public>\Examples\Customizing Result
 Processing\ModelPlugin Simple Text Report\DotNet\SimpleTextReport.sln 
 file.
2. Copy the <TestStand Public>\Examples\Customizing Result
 Processing\ModelPlugin Simple Text Report\DotNet\NI_SimpleTextReport_DotNet.seq 
 file to the <TestStand Public>\Components\Models\ModelPlugins 
 directory.
3. Create the <TestStand Public>\Components\Models\ModelPlugins\NI_SimpleTextReport_DotNet directory if it does not already exist.
4. Copy the <TestStand Public>\Examples\Customizing Result
 Processing\ModelPlugin Simple Text Report\DotNet\SimpleTextPlugin_DotNet.dll 
 file to the <TestStand
 Public>\Components\Models\ModelPlugins\NI_SimpleTextReport_DotNet 
 directory.
5. Copy the <TestStand Public>\Examples\Customizing Result
 Processing\ModelPlugin Simple Text
 Report\DotNet\NationalInstruments.TestStand.Utility.dll file to the
 <TestStand
 Public>\Components\Models\ModelPlugins\NI_SimpleTextReport_DotNet 
 directory.
6. Add and enable an instance of the Microsoft Visual C# simple text report process model plug-in in the Result Processing dialog box.

Parent topic:

Examples for Customizing Result Processing

Related concepts:

- TestStand Directory Structure
- Process Model Plug-In Architecture

<!--NI_TOPIC bundle=teststand path=model-plugin-batch-done.html language=enus -->
## TOPIC 00592: Model Plugin – Batch Done

- bundle_id: `teststand`
- source_path: `model-plugin-batch-done.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/model-plugin-batch-done.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the Batch Done entry point to perform an action after each batch completes. For example, a plug-in might generate a batch report that summarizes the results of all test socket threads. The Batch process model runs Batch Done and the UUT Done entry point in parallel. The Batch process model compl

### Model Plugin – Batch Done

Use the Batch Done entry point to perform an action after each batch completes. For example, a plug-in might generate a batch report that summarizes the results of all test socket threads.

The Batch process model runs Batch Done and the UUT Done entry point in parallel. The Batch process model completes all calls to the UUT Start entry point before calling Batch Done. The Sequential and Parallel process models do not call Batch Done.

Set the <NI_ModelPlugin>.Base.NewThread and <NI_ModelPlugin>.Base.UseDefaultNewThreadImplementation properties to True for the process model to invoke Batch Done in a new thread. When the process model invokes Batch Done in a new thread, it passes all parameters by value except for ModelPlugin and ModelPluginConfiguration.

The Batch Done entry point accepts the following parameters, which are the same as the UUT Done entry point:

| Parameter Name | Data Type |
| --- | --- |
| CallingThread | Reference |
| CallingThreadBlocker | Reference |
| MainSequenceResult | Reference |
| ModelPlugin | NI_ ModelPlugin |
| ModelPluginConfiguration | NI_ModelPluginConfiguration |
| ModelThreadType | NI_ModelThreadType |
| ModelData | Container |
| PriorIterationNewThread | Reference |
| ProcessModelClientPath | Path |
| StartDate | DateDetails |
| StartTime | TimeDetails |
| UUT | UUT |
| UUTStatus | String |

Parent topic:

Model Plug-in Entry Points

Related concepts:

- Model Plugin – UUT Done
- Model Plugin – UUT Start
- Plug-in Entry Point Parameters

<!--NI_TOPIC bundle=teststand path=model-plugin-batch-start.html language=enus -->
## TOPIC 00593: Model Plugin – Batch Start

- bundle_id: `teststand`
- source_path: `model-plugin-batch-start.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/model-plugin-batch-start.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the Batch Start entry point to perform setup or initialization tasks before testing each batch. The Batch process model calls Batch Start in the controller thread after calling the Pre Batch entry point. The Batch process model runs Batch Start and the UUT Start entry point in parallel. The Batc

### Model Plugin – Batch Start

Use the Batch Start entry point to perform setup or initialization tasks before testing each batch.

The Batch process model calls Batch Start in the controller thread after calling the Pre Batch entry point. The Batch process model runs Batch Start and the UUT Start entry point in parallel. The Batch process model completes the call to Batch Start before calling the UUT Done entry point in any socket. The Parallel and Sequential process models do not call Batch Start.

The Batch Start entry point accepts the following parameters, which are the same as the UUT Start entry point:

| Parameter Name | Data Type |
| --- | --- |
| ModelPlugin | NI_ ModelPlugin |
| ModelPluginConfiguration | NI_ModelPluginConfiguration |
| ModelThreadType | NI_ModelThreadType |
| ModelData | Container |
| ProcessModelClientPath | Path |
| StartDate | DateDetails |
| StartTime | TimeDetails |
| UUT | UUT |

Parent topic:

Model Plug-in Entry Points

Related concepts:

- Process Model Thread Types
- Model Plugin – Pre Batch
- Model Plugin – UUT Start
- Model Plugin – UUT Done
- Plug-in Entry Point Parameters

<!--NI_TOPIC bundle=teststand path=model-plugin-begin.html language=enus -->
## TOPIC 00594: Model Plugin – Begin

- bundle_id: `teststand`
- source_path: `model-plugin-begin.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/model-plugin-begin.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the Begin entry point to perform required setup or initialization tasks, such as opening files or establishing database connections. A process model calls Begin once in its controller thread and once in each test socket thread after calling the ModelPluginOptions and ModelPluginConfiguration cal

### Model Plugin – Begin

Use the Begin entry point to perform required setup or initialization tasks, such as opening files or establishing database connections.

A process model calls Begin once in its controller thread and once in each test socket thread after calling the ModelPluginOptions and ModelPluginConfiguration callbacks. In contrast, a process model calls the Initialize entry point only in the controller thread and before calling the ModelPluginOptions and ModelPluginConfiguration callbacks.

Process models complete the call to the Begin from the controller thread before calling Begin from any socket thread.

The Begin entry point accepts the following parameters:

| Parameter Name | Data Type |
| --- | --- |
| ModelPlugin | NI_ ModelPlugin |
| ModelPluginConfiguration | NI_ModelPluginConfiguration |
| ModelThreadType | NI_ModelThreadType |
| ModelData | Container |
| StartDate | DateDetails |
| StartTime | TimeDetails |
| ProcessModelClientPath | Path |
| ParentThread | Reference |

Parent topic:

Model Plug-in Entry Points

Related concepts:

- Process Model Thread Types
- Model Plug in Client-File Callbacks
- Model Plugin – Initialize
- Plug-in Entry Point Parameters

<!--NI_TOPIC bundle=teststand path=model-plugin-configure-additional-options.html language=enus -->
## TOPIC 00595: Model Plugin – Configure Additional Options

- bundle_id: `teststand`
- source_path: `model-plugin-configure-additional-options.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/model-plugin-configure-additional-options.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the Configure Additional Options entry point to launch a second dialog box to provide a way for plug-in end users to configure option settings for the instance of a plug-in. Typically, you do not need this entry point because you can present options in a single dialog box by using tabs, modal po

### Model Plugin – Configure Additional Options

Use the Configure Additional Options entry point to launch a second dialog box to provide a way for plug-in end users to configure option settings for the instance of a plug-in. Typically, you do not need this entry point because you can present options in a single dialog box by using tabs, modal popup dialog boxes, or other organizational methods to accommodate many options.

Use this entry point when you create a new plug-in by extending an existing plug-in and you want to provide a small number of additional options for the new plug-in without changing the options dialog box for the original plug-in. Configure Additional Options launches a second dialog box that contains options specific to the new plug-in, and the Configure Standard Options entry point launches the unchanged options dialog box from the original plug-in.

If a plug-in implements Configure Additional Options, the Options column of the Result Processing dialog box includes a second settings icon immediately to the right of the icon that invokes Configure Standard Options.

Use the Parameters.ModelPlugin.PluginSpecific.AdditionalOptions subproperty to store the additional options for the enhanced plug-in.

The Configure Additional Options entry point accepts the following parameters, which are the same as the Configure Standard Options entry point:

| Parameter Name | Data Type |
| --- | --- |
| Changed | Boolean |
| ProcessModel | Reference |
| ModelType | NI_ModelType |
| ModelPlugin | NI_ModelPlugin |

Parent topic:

Model Plug-in Entry Points

Related concepts:

- Model Plugin – Configure Standard Options
- Plug-in Entry Point Parameters

<!--NI_TOPIC bundle=teststand path=model-plugin-configure-standard-options.html language=enus -->
## TOPIC 00596: Model Plugin – Configure Standard Options

- bundle_id: `teststand`
- source_path: `model-plugin-configure-standard-options.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/model-plugin-configure-standard-options.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the Configure Standard Options entry point to provide a way to configure option settings for an instance of a plug-in. A plug-in that implements Configure Standard Options includes an icon in the Options column of the Result Processing dialog box. Model plug-in end users click the icon to invoke

### Model Plugin – Configure Standard Options

Use the Configure Standard Options entry point to provide a way to configure option settings for an instance of a plug-in. A plug-in that implements Configure Standard Options includes an icon in the Options column of the Result Processing dialog box. Model plug-in end users click the icon to invoke Configure Standard Options, which launches a modal dialog box in which the end user can view and edit options for the instance of the plug-in.

Use the Parameters.ModelPlugin.PluginSpecific.Options subproperty to store the plug-in-specific options for end users to configure in the dialog box the entry point launches.

Note

ModelPlugin.Base.ProcessOnTheFly

The Configure Standard Options entry point accepts the following parameters:

| Parameter Name | Data Type |
| --- | --- |
| Changed | Boolean |
| ProcessModel | Reference |
| ModelType | NI_ModelType |
| ModelPlugin | NI_ModelPlugin |

Parent topic:

Model Plug-in Entry Points

Related concepts:

- Model Plugin – OnTheFly Step Results
- Plug-in Entry Point Parameters

<!--NI_TOPIC bundle=teststand path=model-plugin-end.html language=enus -->
## TOPIC 00597: Model Plugin – End

- bundle_id: `teststand`
- source_path: `model-plugin-end.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/model-plugin-end.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the End entry point to perform required cleanup or finalization tasks, such as closing files or database connections. A process model calls End once in its controller thread and once in each test socket thread. Process models call End from the controller thread only after all calls to End from t

### Model Plugin – End

Use the End entry point to perform required cleanup or finalization tasks, such as closing files or database connections.

A process model calls End once in its controller thread and once in each test socket thread. Process models call End from the controller thread only after all calls to End from test socket threads complete. End is the last entry point the process model calls at run time after the UUT loop, if any, exits.

The End entry point accepts the following parameters:

| Parameter Name | Data Type |
| --- | --- |
| ModelPlugin | NI_ ModelPlugin |
| ModelPluginConfiguration | NI_ModelPluginConfiguration |
| ModelThreadType | NI_ModelThreadType |
| ModelData | Container |

Parent topic:

Model Plug-in Entry Points

Related concepts:

- Process Model Thread Types
- Plug-in Entry Point Parameters

<!--NI_TOPIC bundle=teststand path=model-plugin-initialize.html language=enus -->
## TOPIC 00598: Model Plugin – Initialize

- bundle_id: `teststand`
- source_path: `model-plugin-initialize.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/model-plugin-initialize.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: A process model calls the Initialize entry point once in its controller thread before calling any other run-time entry points and before calling the ModelPluginOptions and ModelPluginConfiguration callbacks. Typically, you implement Initialize only if you want to initialize variables or options befo

### Model Plugin – Initialize

A process model calls the Initialize entry point once in its controller thread before calling any other run-time entry points and before calling the ModelPluginOptions and ModelPluginConfiguration callbacks.

Typically, you implement Initialize only if you want to initialize variables or options before the process model calls the ModelPluginOptions and ModelPluginConfiguration callbacks. Because these callbacks can disable or remove plug-ins, no guarantee exists that the process model calls the End entry point for every plug-in that calls Initialize. Therefore, use the Begin entry point to perform any initialization that requires cleanup in End.

Do not use Initialize to perform initialization that depends on the values of model plug-in options because the subsequent ModelPluginOptions and ModelPluginConfiguration callbacks can alter the option values. Instead, use the Begin entry point to perform option-dependent initialization.

Initialize is the only run-time entry point in which you can change the enabled state of a plug-in instance.

Set the value of the FileGlobals.ModelPluginComponentDescription.Default.Base.AlwaysInitialize property to True for the process model to call the Initialize entry point and the ModelPluginOptions callback even if you do not enable the instance of the plug-in so that the plug-in and the client sequence file can dynamically enable or disable the instances of the plug-in.

If you set the value of the AlwaysInitialize property to False and the ModelPluginConfiguration callback enables a disabled instance of the plug-in, the process model calls the Initialize entry point and the ModelPluginOptions callback after the ModelPluginConfiguration callback returns.

The Initialize entry point accepts the following parameters:

| Parameter Name | Data Type |
| --- | --- |
| ModelPlugin | NI_ModelPlugin |
| ModelPluginConfiguration | NI_ModelPluginConfiguration |
| ModelData | Container |

Parent topic:

Model Plug-in Entry Points

Related concepts:

- Process Model Thread Types
- Model Plug in Client-File Callbacks
- Model Plugin – End
- Model Plugin – Begin
- Plug-in Entry Point Parameters

<!--NI_TOPIC bundle=teststand path=model-plugin-onthefly-step-results.html language=enus -->
## TOPIC 00599: Model Plugin – OnTheFly Step Results

- bundle_id: `teststand`
- source_path: `model-plugin-onthefly-step-results.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/model-plugin-onthefly-step-results.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the OnTheFly Step Results entry point to obtain step results during test execution. For example, when you enable the On-The-Fly Reporting option in the Report Options dialog box, the built-in reporting plug-in calls OnTheFly Step Results to append results information to the report during test ex

### Model Plugin – OnTheFly Step Results

Use the OnTheFly Step Results entry point to obtain step results during test execution. For example, when you enable the On-The-Fly Reporting option in the Report Options dialog box, the built-in reporting plug-in calls OnTheFly Step Results to append results information to the report during test execution.

A process model calls OnTheFly Step Results only for plug-ins configured to process results on-the-fly. The <NI_ModelPlugin>.Base.ProcessOnTheFly subproperty stores the on-the-fly setting. TestStand collects step results until the number of results exceeds a threshold value you specify and then passes the results through the process model to OnTheFly Step Results for processing. The number of results the entry point receives can vary depending on multiple factors, such as the options you specify in the Advanced Result Processing Settings dialog box.

A process model calls OnTheFly Step Results from all threads that generate results. Controller threads in the Batch and Parallel process models do not generate results.

Although a test socket thread can create multiple child threads, the TestStand process models prevent sockets from calling OnTheFly Step Results simultaneously for results from more than one thread in the same test socket. Therefore, OnTheFly Step Results can access per-socket data without additional synchronization.

The OnTheFly Step Results entry point accepts the following parameters:

| Parameter Name | Data Type |
| --- | --- |
| ModelPlugin | NI_ ModelPlugin |
| ModelData | Container |
| StartTime | TimeDetails |
| StartDate | DateDetails |
| UUT | UUT |
| Context | Reference |
| Steps | Reference Array |
| Results | Reference Array |
| CallbackNames | String Array |
| ParentIds | Numeric Array |
| ModelPluginConfiguration | NI_ModelPluginConfiguration |

The Steps, Results, CallbackNames, and ParentIds parameters are parallel arrays. For any given array index n, the result element at Results[n] and the values of Steps[n], CallbackNames[n], and ParentIds[n] represent the n<sup>th</sup> result and the step that generated the result, the callback name of the result, and the ID of the parent for that result, respectively.

Parent topic:

Model Plug-in Entry Points

Related concepts:

- Process Model Thread Types
- Plug-in Entry Point Parameters
- Subsequence Results

<!--NI_TOPIC bundle=teststand path=model-plugin-post-batch.html language=enus -->
## TOPIC 00600: Model Plugin – Post Batch

- bundle_id: `teststand`
- source_path: `model-plugin-post-batch.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/model-plugin-post-batch.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: A process model calls the Post Batch entry point after calling the Batch Done entry point. Post Batch is similar to Batch Done except that Post Batch never runs in a new thread and the Batch process model does not call Post Batch until every call to the Post UUT entry point completes. The Sequential

### Model Plugin – Post Batch

A process model calls the Post Batch entry point after calling the Batch Done entry point.

Post Batch is similar to Batch Done except that Post Batch never runs in a new thread and the Batch process model does not call Post Batch until every call to the Post UUT entry point completes.

The Sequential and Parallel process models do not call Post Batch.

The Post Batch entry point accepts the following parameters, which are the same as the Post UUT entry point:

| Parameter Name | Data Type |
| --- | --- |
| MainSequenceResult | Reference |
| ModelPlugin | NI_ ModelPlugin |
| ModelPluginConfiguration | NI_ModelPluginConfiguration |
| ModelThreadType | NI_ModelThreadType |
| ModelData | Container |
| ProcessModelClientPath | Path |
| StartDate | DateDetails |
| StartTime | TimeDetails |
| UUT | UUT |
| UUTStatus | String |

Parent topic:

Model Plug-in Entry Points

Related concepts:

- Model Plugin – Batch Done
- Model Plugin – Post UUT
- Plug-in Entry Point Parameters

<!--NI_TOPIC bundle=teststand path=model-plugin-post-uut.html language=enus -->
## TOPIC 00601: Model Plugin – Post UUT

- bundle_id: `teststand`
- source_path: `model-plugin-post-uut.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/model-plugin-post-uut.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: A process model calls the Post UUT entry point after calling the UUT Done entry point. Post UUT is similar to UUT Done except that Post UUT entry point never runs in a new thread and the Batch process model does not call the Post Batch entry point until every call to Post UUT completes. Post UUT acc

### Model Plugin – Post UUT

A process model calls the Post UUT entry point after calling the UUT Done entry point.

Post UUT is similar to UUT Done except that Post UUT entry point never runs in a new thread and the Batch process model does not call the Post Batch entry point until every call to Post UUT completes.

Post UUT accepts the following parameters, which are the same as UUT Done except for the CallingThread, CallingThreadBlocker, and PriorIterationNewThread parameters:

| Parameter Name | Data Type |
| --- | --- |
| MainSequenceResult | Reference |
| ModelPlugin | NI_ ModelPlugin |
| ModelPluginConfiguration | NI_ModelPluginConfiguration |
| ModelThreadType | NI_ModelThreadType |
| ModelData | Container |
| ProcessModelClientPath | Path |
| StartDate | DateDetails |
| StartTime | TimeDetails |
| UUT | UUT |
| UUTStatus | String |

Parent topic:

Model Plug-in Entry Points

Related concepts:

- Model Plugin – UUT Done
- Model Plugin – Post Batch
- Plug-in Entry Point Parameters

<!--NI_TOPIC bundle=teststand path=model-plugin-pre-batch.html language=enus -->
## TOPIC 00602: Model Plugin – Pre Batch

- bundle_id: `teststand`
- source_path: `model-plugin-pre-batch.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/model-plugin-pre-batch.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the Pre Batch entry point to identify the batch or determine whether to continue testing. The Batch process model calls Pre Batch in the controller thread before each batch. The Batch process model completes all calls to the Begin entry point before calling Pre Batch. The Batch process model com

### Model Plugin – Pre Batch

Use the Pre Batch entry point to identify the batch or determine whether to continue testing.

The Batch process model calls Pre Batch in the controller thread before each batch. The Batch process model completes all calls to the Begin entry point before calling Pre Batch. The Batch process model completes the call to Pre Batch from the controller thread before calling the Pre UUT entry point from any socket thread. The Parallel and Sequential process models do not call Pre Batch.

The Pre Batch entry point accepts the following parameters, which are the same as the Pre UUT entry point:

| Parameter Name | Data Type |
| --- | --- |
| ModelPlugin | NI_ ModelPlugin |
| ModelPluginConfiguration | NI_ModelPluginConfiguration |
| ModelThreadType | NI_ModelThreadType |
| ModelData | Container |
| ProcessModelClientPath | Path |
| StartDate | DateDetails |
| StartTime | TimeDetails |
| UUT | UUT |
| ContinueTesting | Boolean |

Parent topic:

Model Plug-in Entry Points

Related concepts:

- Process Model Thread Types
- Model Plugin – Begin
- Model Plugin – Pre UUT
- Plug-in Entry Point Parameters

<!--NI_TOPIC bundle=teststand path=model-plugin-pre-uut.html language=enus -->
## TOPIC 00603: Model Plugin – Pre UUT

- bundle_id: `teststand`
- source_path: `model-plugin-pre-uut.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/model-plugin-pre-uut.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the Pre UUT entry point to identify the UUT or determine whether to continue testing. A process model calls Pre UUT in the test socket thread before testing each UUT. The Batch process model completes the call to the Pre Batch entry point before calling Pre UUT for any test socket. The Pre UUT e

### Model Plugin – Pre UUT

Use the Pre UUT entry point to identify the UUT or determine whether to continue testing.

A process model calls Pre UUT in the test socket thread before testing each UUT.

The Batch process model completes the call to the Pre Batch entry point before calling Pre UUT for any test socket.

The Pre UUT entry point accepts the following parameters:

| Parameter Name | Data Type |
| --- | --- |
| ModelPlugin | NI_ ModelPlugin |
| ModelPluginConfiguration | NI_ModelPluginConfiguration |
| ModelThreadType | NI_ModelThreadType |
| ModelData | Container |
| ProcessModelClientPath | Path |
| StartDate | DateDetails |
| StartTime | TimeDetails |
| UUT | UUT |
| ContinueTesting | Boolean |

If the ContinueTesting parameter is False after the process model calls Pre UUT for every plug-in, the process model exits the UUT loop without calling the UUT Start, UUT Done, or Post UUT entry points. If multiple model plug-ins use conflicting values for ContinueTesting, TestStand uses the value set by the last plug-in to execute.

Parent topic:

Model Plug-in Entry Points

Related concepts:

- Process Model Thread Types
- Model Plugin – Pre Batch
- Plug-in Entry Point Parameters
- Model Plugin – UUT Start
- Model Plugin – UUT Done
- Model Plugin – Post UUT

<!--NI_TOPIC bundle=teststand path=model-plugin-uut-done.html language=enus -->
## TOPIC 00604: Model Plugin – UUT Done

- bundle_id: `teststand`
- source_path: `model-plugin-uut-done.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/model-plugin-uut-done.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the UUT Done entry point to perform an action after each UUT completes. For example, a plug-in might process the UUT test results and store the information in a report file or database tables. A process model calls UUT Done in each test socket thread after testing the UUT. The Batch process mode

### Model Plugin – UUT Done

Use the UUT Done entry point to perform an action after each UUT completes. For example, a plug-in might process the UUT test results and store the information in a report file or database tables.

A process model calls UUT Done in each test socket thread after testing the UUT.

The Batch process model runs UUT Done and the Batch Done entry point in parallel.

Set the <NI_ModelPlugin>.Base.NewThread and <NI_ModelPlugin>.Base.UseDefaultNewThreadImplementation properties to True for the process model to invoke UUT Done in a new thread. When the process model invokes UUT Done in a new thread, it passes all parameters by value except for ModelPlugin and ModelPluginConfiguration.

The UUT Done entry point accepts the following parameters, which are the same as the UUT Start entry point and include the additional UUTStatus, MainSequenceResult, CallingThread, CallingThreadBlocker, and PriorIterationNewThread parameters:

| Parameter Name | Data Type |
| --- | --- |
| CallingThread | Reference |
| CallingThreadBlocker | Reference |
| MainSequenceResult | Reference |
| ModelPlugin | NI_ ModelPlugin |
| ModelPluginConfiguration | NI_ModelPluginConfiguration |
| ModelThreadType | NI_ModelThreadType |
| ModelData | Container |
| PriorIterationNewThread | Reference |
| ProcessModelClientPath | Path |
| StartDate | DateDetails |
| StartTime | TimeDetails |
| UUT | UUT |
| UUTStatus | String |

Parent topic:

Model Plug-in Entry Points

Related concepts:

- Process Model Thread Types
- Model Plugin – Batch Done
- Plug-in Entry Point Parameters
- Model Plugin – UUT Start

<!--NI_TOPIC bundle=teststand path=model-plugin-uut-start.html language=enus -->
## TOPIC 00605: Model Plugin – UUT Start

- bundle_id: `teststand`
- source_path: `model-plugin-uut-start.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/model-plugin-uut-start.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the UUT Start entry point to perform setup or initialization tasks before testing each UUT. For example, a plug-in might use UUT Start to open per-UUT report files. A process model calls UUT Start in the test socket thread after calling the Pre UUT entry point but before testing the UUT. The Bat

### Model Plugin – UUT Start

Use the UUT Start entry point to perform setup or initialization tasks before testing each UUT. For example, a plug-in might use UUT Start to open per-UUT report files.

A process model calls UUT Start in the test socket thread after calling the Pre UUT entry point but before testing the UUT.

The Batch process model runs UUT Start and the Batch Start entry point in parallel.

The UUT Start entry point accepts the following parameters, which are the same as Pre UUT except for the ContinueTesting parameter:

| Parameter Name | Data Type |
| --- | --- |
| ModelPlugin | NI_ ModelPlugin |
| ModelPluginConfiguration | NI_ModelPluginConfiguration |
| ModelThreadType | NI_ModelThreadType |
| ModelData | Container |
| ProcessModelClientPath | Path |
| StartDate | DateDetails |
| StartTime | TimeDetails |
| UUT | UUT |

Parent topic:

Model Plug-in Entry Points

Related concepts:

- Process Model Thread Types
- Model Plugin – Pre UUT
- Model Plugin – Batch Start
- Plug-in Entry Point Parameters

<!--NI_TOPIC bundle=teststand path=modify-types-same-ver.html language=enus -->
## TOPIC 00606: Modifying Types Without Altering the Version Number

- bundle_id: `teststand`
- source_path: `modify-types-same-ver.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/modify-types-same-ver.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use PropertyObject Attributes to add data to or update data in a custom data type without needing to increment the version number of the custom type. Since object Attributes are an unstructured container, creating an Attribute within an instance of a custom type does not generate a type conf

### Modifying Types Without Altering the Version
 Number

You can use PropertyObject Attributes to add data to or update data in a
 custom data type without needing to increment the version number of the custom type.

Save As

Note

Help

»

About TestStand

If you need to use a custom type Attribute in a test sequence, you can create the Attribute
 in the unique instance of the custom type. If you use this method, you should write your test
 programs to ensure they function if the Attribute isn't created for a type instance.

NI_NotSupportedFeature

Figure 1.

[IMAGE alt='image' src='GUID-D56369F4-2DE7-4817-ADC6-5B6A3D10AC66-a5.png']

- UnsupportedFeatures : Should be structured as an array where each
 element represents a feature and contains the following:
  - FeatureId (String) : Unique identifier for the feature.
  - AnalyzerMessage (String) : Message you want to pass to users when
 the feature is unsupported.
  - MaximumTestStandVersion (String) : Maximum TestStand version that
 the feature can be used in. This value should follow the
 major.minor.revision.build format. Revision and build version
 values are optional.
  - MinimumTestStandVersion (String) : Minimum TestStand version that
 the feature can be used in. This value should follow the
 major.minor.revision.build format. Revision and build version
 values are optional.

```text
Message: The instance of type <TypeName> has some features which are not supported in current TestStand version: <AnalyzerMessage>.
```

Parent topic:

Modifying Types

Related concepts:

- Modifying Types
- TestStand Sequence Analyzer

<!--NI_TOPIC bundle=teststand path=modifying-callbacks.html language=enus -->
## TOPIC 00607: Modifying Callbacks

- bundle_id: `teststand`
- source_path: `modifying-callbacks.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/modifying-callbacks.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: TestStand includes Engine callback and Front-End callback sequences you can customize to meet specific needs.

### Modifying Callbacks

TestStand includes Engine callback and Front-End callback sequences you can customize to meet specific needs.

Parent topic:

Customizing Process Models and Callbacks

Related concepts:

- Modifying Engine Callbacks
- Modifying Front-End Callbacks
- Overriding PreBatch and PostBatch Model Callbacks
- Overriding PreUUT and PostUUT Batch Model Callbacks
- Overriding PreUUT and PostUUT Parallel Model Callbacks

<!--NI_TOPIC bundle=teststand path=modifying-cell-background-color-atml.html language=enus -->
## TOPIC 00608: Modifying Cell Background Color Based on Step Status in an ATML Test Results 6.01 or 5.0 Report

- bundle_id: `teststand`
- source_path: `modifying-cell-background-color-atml.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/modifying-cell-background-color-atml.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: None TR6_Horizontal.xsl or TR5_Horizontal.xsl Complete the following steps to modify the background color of the step status cell using the TR6_Horizontal.xsl or TR5_Horizontal.xsl file. Open the .xsl file you want to change. Search for the ADD_STATUS comment. Uncomment the following lines of code:<

### Modifying Cell Background Color Based on
 Step Status in an ATML Test Results 6.01 or 5.0 Report

None

#### TR6_Horizontal.xsl or
 TR5_Horizontal.xsl

Complete the following steps to modify the background
 color of the step status cell using the TR6_Horizontal.xsl or
 TR5_Horizontal.xsl file.

1. Open the .xsl file you want to change.
2. Search for the ADD_STATUS comment.
3. Uncomment the following lines of
 code: <xsl:variable name="cellBackgroundColor"
 <xsl:choose>
 <xsl:when test="$outcome = 'Passed'">#FFFF00</xsl:when>
 <xsl:otherwise><xsl:value-of select="$statusBackgroundColor"/></xsl:otherwise>
 <xsl:choose>
 <td style="background-color:{$cellBackgroundColor};width:{$gSecondColumnWidth};">
 The <xsl:when test="$outcome = 'Passed'">#FFFF00</xsl:when> expression changes the background color variable to yellow. You can use a custom XPath expression instead.
 ATML Test Results 2.02 Report Style Sheet does not need to be updated as it already references XPath.
4. Comment out the following line of code: <td
 style="color:{$statusColor};text-align:center;">
5. Optionally, you can add Failed.jpg to the
 C:\Images directory and uncomment the following lines of
 code after the ADD_IMG comment to add an image next to the UUT
 status text for Failed 
 steps: <xsl:if test="$outcome = 'Failed'">
 <img src = "C:\Images\Failed.jpg"/>
</xsl:if>

The following figure shows a modified report with yellow cells for steps with a
 Passed status using the TR6_Horizontal.xsl or
 TR5_Horizontal.xsl file.

[IMAGE alt='image' src='GUID-4865ED1E-F3D4-4773-9AA4-19E142AEFE44-a5.png']

#### TR6_report.xsl, TR5_report.xsl,
 TR6_Expand.xsl, or TR5_Expand.xsl

Complete the following steps to modify
 the background color of the step status cell using the
 TR6_report.xsl, TR5_report.xsl,
 TR6_Expand.xsl, or TR5_Expand.xsl file.

1. Open the .xsl file you want to change.
2. Search for the ADD_STATUS comment.
3. Uncomment the following lines of
 code: <xsl:variable name="cellBackgroundColor"
 <xsl:choose>
 <xsl:when test="$outcome = 'Passed'">#FFFF00</xsl:when>
 <xsl:otherwise><xsl:value-of select="$statusBackgroundColor"/></xsl:otherwise>
 <xsl:choose>
 <td style="background-color:{$cellBackgroundColor};width:{$gSecondColumnWidth};">
 The <xsl:when test="$outcome = 'Passed'">#FFFF00</xsl:when>expression changes the 
 background color variable to yellow. You can use a custom XPath expression instead.
 ATML Test Results 2.02 Report Style Sheet does not need to be updated as it already
 references XPath.
4. Comment out the following line of code: <td
 style="background-color:{$statusBackgroundColor};width:{$gSecondColumnWidth};">
5. Optionally, you can add Failed.jpg to the
 C:\Images directory and uncomment the following lines of
 code after the ADD_IMG comment to add an image next to the UUT
 status text for Failed 
 steps: <xsl:if test="$outcome = 'Failed'">
 <img src = "C:\Images\Failed.jpg"/>
</xsl:if>

The following figure shows a modified report with yellow cells for steps with a
 Passed status using the TR6_report.xsl,
 TR5_report.xsl, TR6_Expand.xsl, or
 TR5_Expand.xsl file.

[IMAGE alt='image' src='GUID-DD94196F-6583-47D5-832C-ACAC33E1136B-a5.png']

Parent topic:

Customizing ATML Test Results 6.01 or 5.0 Report Style Sheets

<!--NI_TOPIC bundle=teststand path=modifying-cell-background-color-xml.html language=enus -->
## TOPIC 00609: Modifying Cell Background Color Based on Step Status in an XML Report

- bundle_id: `teststand`
- source_path: `modifying-cell-background-color-xml.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/modifying-cell-background-color-xml.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: None horizontal.xsl Complete the following steps to modify the background color of the step status cell using the horizontal.xsl file. Open the horizontal.xsl file. Search for the ADD_IMG_STATUS comment. Replace the <td valign="middle" align="center"> line of code with the following code to set the

### Modifying Cell Background Color Based on Step Status in an XML Report

None

#### horizontal.xsl

Complete the following steps to modify the background color of the step status cell using the horizontal.xsl file.

1. Open the horizontal.xsl file.
2. Search for the ADD_IMG_STATUS comment.
3. Replace the <td valign="middle" align="center"> line of code with the
 following code to set the background color of step result cells to yellow for
 Passed 
 steps: <xsl:variable name="backgroundColor">
 <xsl:choose>
 <xsl:when test="Value = 'Passed'">#FFFF00</xsl:when>
 <xsl:otherwise>#FFFFFF</xsl:otherwise>
 </xsl:choose>
</xsl:variable>
<td valign="middle" align="center" bgcolor="{$backgroundColor}"> 
 Optionally, you can add Failed.jpg to the
 C:\Images directory and add the following lines of code
 after the <td valign="middle" align="center"> line of
 code to add an image next to the UUT status text for Failed 
 steps: <xsl:if test="Value = 'Failed'">
 <img src = "C:\Images\Failed.jpg"/>
</xsl:if>
4. Search for each of three instances of the ADD_COLUMN_DATA_1 comment and uncomment the following code for each instance: <td><xsl:value-of select="@testReferenceID"/></td> The expression "@testReferenceID" specifies the XPath expression to obtain the testReferenceID from the XML file. You must customize this XPath expression to match the data you want to add to the additional columns. Refer to the W3Schools website for more information on XPath. Refer to ATML Test Results 6.01 and 5.0 Report Structure for the XML object structure.

The following figure shows a modified report with yellow cells for steps with a Passed status using horizontal.xsl:

[IMAGE alt='image' src='GUID-C21BC6F9-A91B-4268-A650-1BDEBD6A66D4-a5.png']

#### report.xsl and expand.xsl

Complete the following steps to modify the background color of the step status cell using the report.xsl file and the expand.xsl file.

1. Open the report.xsl or expand.xsl file.
2. Search for the ADD_IMG_STATUS comment.
3. Replace the following code in the BGCOLOR 
 attribute: <xsl:call-template name="GetStatusBgColor">
 <xsl:with-param name="colors" select="$colors"/>
 <xsl:with-param name="status" select="Value"/>
</xsl:call-template> 
 with the following code to set the background color of step result cells to
 yellow for Passed steps. The <xsl:when test="Value =
 'Passed'">#FFFF00</xsl:when> expression changes the
 background color variable to yellow. You can use a custom XPath expression
 instead. <xsl:choose>
 <xsl:when test="Value = 'Passed'">#FFFF00</xsl:when>
 <xsl:otherwise>
 <xsl:call-template name="GetStatusBgColor">
 <xsl:with-param name="colors" select="$colors"/>
 <xsl:with-param name="status" select="Value"/>
 </xsl:call-template>
 </xsl:otherwise>
</xsl:choose> 
 Optionally, you can add Failed.jpg to the
 C:\Images directory and add the following lines of code
 after the WIDTH attribute and before the
 <font> tag to add an image next to the UUT status
 text for Failed 
 steps: <xsl:if test="Value = 'Failed'">
 <img src = "C:\Images\Failed.jpg"/>
</xsl:if>

The following figure shows a modified report with yellow cells for steps with a Passed status using report.xsl:

[IMAGE alt='image' src='GUID-6BDC624B-018E-48A3-BE86-632532261EE1-a5.png']

The following figure shows a modified report with yellow cells for steps with a Passed status using expand.xsl:

[IMAGE alt='image' src='GUID-6D647E83-41FC-49BF-9FE4-BB1B57D7E6C6-a5.png']

Parent topic:

Customizing XML Report Style Sheets

Related concepts:

- ATML Test Results 6.01 and 5.0 Report Structure

Related information:

- W3Schools

<!--NI_TOPIC bundle=teststand path=modifying-engine-callbacks.html language=enus -->
## TOPIC 00610: Modifying Engine Callbacks

- bundle_id: `teststand`
- source_path: `modifying-engine-callbacks.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/modifying-engine-callbacks.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The TestStand Engine invokes a set of Engine callbacks at specific points during execution. TestStand defines the set of Engine callbacks and the callback names because the engine controls the execution of steps and the loading and unloading of sequence files. Use Engine callbacks to configure TestS

### Modifying Engine Callbacks

The TestStand Engine invokes a set of Engine callbacks at specific points during execution. TestStand defines the set of Engine callbacks and the callback names because the engine controls the execution of steps and the loading and unloading of sequence files.

Use Engine callbacks to configure TestStand to call certain sequences at various points during a test, including before and after the execution of individual steps, before and after interactive executions, after loading a sequence file, or before unloading a sequence file.

TestStand categorizes Engine callbacks according to the file in which the callback appears. You can define Engine callbacks in sequence files, process model files, and in StationCallbacks.seq in the <TestStand Public>\Components\Callbacks\Station directory.

Note

StationCallbacks.seq

TestStand invokes Engine callbacks in normal sequence files only when executing steps in the sequence file or when loading or unloading the sequence file. TestStand invokes Engine callbacks in process model files when executing steps in the model file, steps in sequences the model calls, and steps in any nested calls to subsequences. TestStand invokes Engine callbacks in StationCallbacks.seq when TestStand executes steps on the test station.

You can use Engine callbacks in the following ways:

- Use the SequenceFileLoad callback to ensure that you configure external resources the sequence file uses only once before you execute the sequence. Usually, you initialize devices a sequence requires by creating steps in the Setup step group for the sequence. However, when you call the sequence repeatedly, you can move the Setup steps into a SequenceFileLoad callback for the subsequence file so that the steps run only when the sequence file loads.
- Use the StationPreStep and StationPostStep callbacks to accumulate statistics on all steps that execute on the test station. You can inspect the name and types of steps that accumulate data on specific steps.

Parent topic:

Modifying Callbacks

Related concepts:

- Engine Callbacks
- TestStand Directory Structure
- List of Engine Callbacks
- Caveats for Using Engine Callbacks
- Overriding PreBatch and PostBatch Model Callbacks
- Overriding PreUUT and PostUUT Batch Model Callbacks
- Overriding PreUUT and PostUUT Parallel Model Callbacks

<!--NI_TOPIC bundle=teststand path=modifying-front-end-callbacks.html language=enus -->
## TOPIC 00611: Modifying Front-End Callbacks

- bundle_id: `teststand`
- source_path: `modifying-front-end-callbacks.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/modifying-front-end-callbacks.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Front-End callbacks are sequences in the FrontEndCallbacks.seq file multiple user interface applications can call to share the same implementation for a specific operation. The FrontEndCallback.seq file TestStand installs in the <TestStand>\Components\Callbacks\FrontEnd directory contains one LoginL

### Modifying Front-End Callbacks

Front-End callbacks are sequences in the FrontEndCallbacks.seq file multiple user interface applications can call to share the same implementation for a specific operation. The FrontEndCallback.seq file TestStand installs in the <TestStand>\Components\Callbacks\FrontEnd directory contains one LoginLogout Front-End callback. The TestStand Sequence Editor and default user interfaces call the LoginLogout callback.

Use Front-End callbacks to implement operations so you can modify a Front-End callback without modifying the source code for the user interfaces or rebuilding the executables for the user interfaces. For example, to change how various user interfaces perform the login procedure, modify only the LoginLogout sequence in FrontEndCallbacks.seq.

To modify the default implementation of the Front-End callback or to create new Front-End callbacks, copy the FrontEndCallbacks.seq file from the <TestStand>\Components\Callbacks\FrontEnd directory to the <TestStand Public>\Components\Callbacks\FrontEnd directory and make any changes to the copy of the file. You can use functions in the TestStand API to invoke the modified Front-End callback from each user interface application you create. However, because you cannot edit the source for the sequence editor, you cannot make the sequence editor call new Front-End callbacks you create.

Parent topic:

Modifying Callbacks

Related concepts:

- Callback Sequences
- TestStand Directory Structure
- Copying Read-Only Files to Modify
- TestStand ActiveX API Overview

<!--NI_TOPIC bundle=teststand path=modifying-process-model-sequence-files.html language=enus -->
## TOPIC 00612: Modifying Process Model Sequence Files

- bundle_id: `teststand`
- source_path: `modifying-process-model-sequence-files.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/modifying-process-model-sequence-files.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: You must modify the process model sequence files directly to make changes that apply wherever TestStand uses the process model. TestStand installs the SequentialModel.seq, ParallelModel.seq, and BatchModel.seq process model sequence files and supporting files in the <TestStand>\Components\Models\Tes

### Modifying Process Model Sequence Files

You must modify the process model sequence files directly to make changes that apply wherever TestStand uses the process model.

TestStand installs the SequentialModel.seq, ParallelModel.seq, and BatchModel.seq process model sequence files and supporting files in the <TestStand>\Components\Models\TestStandModels directory. To modify the installed process model or to create a new process model, copy all the process model files from the <TestStand>\Components\Models\TestStandModels directory to <TestStand Public>\Components\Models and make changes to the copy.

In addition to editing process model sequence files, you can convert normal sequence files to process model sequence files. Complete the following steps to specify a sequence file as a process model sequence file.

1. Select the sequence file and select Edit»Sequence File Properties .
2. In the Sequence File Properties dialog box, click the Advanced tab.
3. Select Model from the Type ring control.
4. Click OK .

Although you edit a process model sequence file in a regular Sequence File window, the file includes Model entry points and Model callbacks. TestStand maintains special properties for entry point and callback sequences, and you can specify the values of these properties when you edit the sequences in a process model file.

When you access the Sequence Properties dialog box for any sequence in a model file, the dialog box contains a Model tab you use to specify the sequence as a normal sequence, a callback sequence, or an entry point sequence.

Parent topic:

Customizing Process Models and Callbacks

Related concepts:

- Sequential Process Model
- Parallel Process Model
- Batch Process Model
- TestStand Directory Structure
- Copying Read-Only Files to Modify
- Entry Point Sequences
- Using Callback Sequences to Modify Process Models
- Normal Sequences

<!--NI_TOPIC bundle=teststand path=modifying-type-instances-values-and-type-defi.html language=enus -->
## TOPIC 00613: Modifying Type Instances, Values, and Type Definitions

- bundle_id: `teststand`
- source_path: `modifying-type-instances-values-and-type-defi.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/modifying-type-instances-values-and-type-defi.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can modify the default type instances, values, and type definitions of TestStand data types. Type Instances With the exception of resizing arrays, you cannot change the subproperty structure of a variable, parameter, or property after you create it from a data type. You can, however, change the

### Modifying Type Instances, Values, and Type Definitions

You can modify the default type instances, values, and type definitions of TestStand data types.

#### Type Instances

With the exception of resizing arrays, you cannot change the subproperty structure of a variable, parameter, or property after you create it from a data type.

You can, however, change the subproperty structure of the data type itself. Changing the structure of a data type affects all variables, parameters, and properties that use the data type.

#### Values

Use the Value column on the Variables pane to modify the value of a variable, parameter, or property. For local variables, the data type value you specify at edit time is the initial value TestStand uses whenever it calls into the sequence. For parameters, the data type value is the default value TestStand uses when you do not pass an argument value explicitly.

#### Type Definitions

On the Types pane of the Types window, right-click a property on a type and select Properties from the context menu to launch the Type Properties dialog box, in which you can specify additional settings and edit the value of the property on the type.

In general, when you make changes to property values in a type, the changes do not affect all instances of the type. Enable the Apply Changes in this Dialog to all Loaded Instances of the Type option in the Type Properties dialog box to apply the change to all loaded instances of the type.

You can also rearrange properties on the Variables pane by dragging or copying the items you want to move. In general, the order of properties does not matter, but the order of sequence parameters affects how you configure a Sequence Call step that invokes the sequence.

Note

<TestStand>\Components\Models\TestStandModels

<TestStand Public>\Components\Models\TestStandModels

<TestStand Public>\Components\Models\TestStandModels

<TestStand Public>\Components\Models\TestStandModels

<TestStand>\Components\Models\TestStandModels

<TestStand>\Components\Models\ModelPlugins

<TestStand Public>\Components\Models\ModelPlugins

Parent topic:

Data Types

Related concepts:

- Specifying Array Sizes
- TestStand Directory Structure

<!--NI_TOPIC bundle=teststand path=modifying-types.html language=enus -->
## TOPIC 00614: Modifying Types

- bundle_id: `teststand`
- source_path: `modifying-types.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/modifying-types.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can modify the built-in and custom properties of step types you create and custom data types you create. However, you cannot modify the built-in step types and standard data types TestStand installs. Use the Copy and Paste context menu items to copy and rename an existing or built-in step type o

### Modifying Types

You can modify the built-in and custom properties of step types you create and custom data types you create. However, you cannot modify the built-in step types and standard data types TestStand installs.

Use the Copy and Paste context menu items to copy and rename an existing or built-in step type or standard data type on the Types pane of the Types window of the TestStand Sequence Editor.

When you modify a type, TestStand enables the PropTypeFlags_IsModifiedType type flag for the type. TestStand cannot automatically resolve type conflicts unless you disable the PropTypeFlags_IsModifiedType type flag. To disable the PropTypeFlags_IsModifiedType type flag, you typically increment the version number of the type on the Version tab of the Step Type Properties dialog box or on the Version tab of the Type Properties dialog box when you complete all the modifications to the type.

By default, the Before Saving Modified Types option on the File tab of the Station Options dialog box is set to Prompt to Increment Type Versions. This causes TestStand to launch the Modified Types Warning dialog box when you select File»Save <filename> and the sequence file or type palette contains types that are marked as modified. You can increment the type version or remove the modified mark on the type before saving, or save the type as modified.

When you open a file that was saved in an earlier version of TestStand, TestStand marks the file as modified when it automatically converts the file and upgrades built-in types and custom types that the file uses. Use the Do Not Mark Files as Modified if Modification is Caused Only by Automatic TestStand Version Upgrade option on the File tab of the Station Options dialog box to configure whether TestStand marks files as modified when upgrading files.

Note

<TestStand>\Components\Models\TestStandModels

<TestStand Public>\Components\Models\TestStandModels

<TestStand Public>\Components\Models\TestStandModels

<TestStand Public>\Components\Models\TestStandModels

<TestStand>\Components\Models\TestStandModels

<TestStand>\Components\Models\ModelPlugins

<TestStand Public>\Components\Models\ModelPlugins

Parent topic:

Type Concepts

Related concepts:

- Creating Custom Step Types
- Creating Custom Data Types
- Built-In Step Types
- Standard and Custom Data Types
- Managing Type Revisions
- Type Versioning
- TestStand Directory Structure

<!--NI_TOPIC bundle=teststand path=module-adapters.html language=enus -->
## TOPIC 00615: Module Adapters

- bundle_id: `teststand`
- source_path: `module-adapters.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/module-adapters.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The TestStand Engine uses module adapters to invoke code modules that sequences call. A code module is a program module from an ADE or programming language and can contain one or more functions that perform a specific test or other action. Module adapters load and call code modules, pass parameters

### Module Adapters

The TestStand Engine uses module adapters to invoke code modules that sequences call. A code module is a program module from an ADE or programming language and can contain one or more functions that perform a specific test or other action. Module adapters load and call code modules, pass parameters to code modules, and return values and status from code modules. TestStand handles core test management functionality, including the definition and execution of the overall testing process, user management, report generation, database logging, and more.

TestStand supports the following module adapters:

- ActiveX/COM Adapter
- C/C++ DLL Adapter
- HTBasic Adapter
- LabVIEW Adapter
- LabWindows/CVI Adapter
- .NET Adapter
- Sequence Adapter
- Python Adapter

Note

Select Configure»Adapters to configure an adapter.

To specify a code module for a step, use a Module tab of the Step Settings pane in the TestStand Sequence Editor and a Specify Module dialog box in a TestStand User Interface. The actual title of the Specify Module tab or dialog box is different for each adapter.

Adapters specific to an application development environment (ADE) can open the ADE, create source code for a new code module in the ADE, and display the source for an existing code module in the ADE. The adapters support stepping into the source code in the ADE while you execute the step from the TestStand Sequence Editor or a TestStand User Interface.

#### Source Code Templates

For each adapter that supports source code templates, the Module tab and the Specify Module dialog box display a command button for creating source code based on a template for the step. If more than one template is available for the adapter and step type combination you use to create the step, you can select from a list of the templates. If only one template is available, the adapter uses the template without giving you additional options.

Parent topic:

Fundamentals

Related concepts:

- Components of a TestStand System
- Code Modules
- Organizing Test Program Files with LabVIEW-Built Shared Libraries
- Programming with the TestStand API in LabVIEW
- Programming with the TestStand API in LabWindows/CVI
- Adapter and Code Module Support for 64-bit TestStand
- Driver Support for 64-bit TestStand

<!--NI_TOPIC bundle=teststand path=multiple-code-templates-per-step-type.html language=enus -->
## TOPIC 00616: Multiple Code Templates per Step Type

- bundle_id: `teststand`
- source_path: `multiple-code-templates-per-step-type.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/multiple-code-templates-per-step-type.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can specify more than one code template for a step type. For example, you might want to have code templates that contain example code for conducting the same type of tests with different types of instruments or data acquisition boards. When a step type has multiple code templates and you click t

### Multiple Code Templates per Step Type

You can specify more than one code template for a step type. For example, you might want to have code templates that contain example code for conducting the same type of tests with different types of instruments or data acquisition boards.

When a step type has multiple code templates and you click the Create Code button on the Module tab of the Step Settings pane, TestStand prompts you to select from a list of templates or uses the template you selected on the Module tab when it exists.

Parent topic:

Custom Step Types

<!--NI_TOPIC bundle=teststand path=multiple-numeric-limit-test-step-type-labview.html language=enus -->
## TOPIC 00617: Multiple Numeric Limit Test Step Type - LabVIEW

- bundle_id: `teststand`
- source_path: `multiple-numeric-limit-test-step-type-labview.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/multiple-numeric-limit-test-step-type-labview.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Purpose This example demonstrates how to use a Multiple Numeric Limit Test step with a LabVIEW code module. Example File Location <TestStand Public>\Examples\Built-In Step Types\Multiple Numeric Limit Test Step Type\LabVIEW\Multiple Numeric Limit Step Type.seq Highlighted Features Multiple Numeric L

### Multiple Numeric Limit Test Step Type - LabVIEW

#### Purpose

This example demonstrates how to use a Multiple Numeric Limit Test step with a LabVIEW code module.

#### Example File
 Location

<TestStand
 Public>\Examples\Built-In Step Types\Multiple Numeric Limit Test
 Step Type\LabVIEW\Multiple Numeric Limit Step Type.seq

#### Highlighted Features

Multiple Numeric Limit Test steps

#### Major API

None

#### Prerequisites

You must have the LabVIEW development system installed and you must configure the LabVIEW Adapter to use the LabVIEW development system.

#### How to Use This
 Example

This example contains four Multiple Numeric Limit Test steps. The
 first three steps obtain four measurement values and compare them to the following
 high and low values specified on the Limits tab of the Step Settings pane:

| Measurement | Comparison | Low Value | High Value |
| --- | --- | --- | --- |
| VOLTAGE 0 | GELE (>= <=) | 3 | 5 |
| VOLTAGE 1 | GELE (>= <=) | 3 | 5 |
| FREQUENCY | GELE (>= <=) | 110 | 125 |
| RMS | GELE (>= <=) | 0.5 | 1.0 |

Each step demonstrates a different way of using the Multiple Numeric Limit
 Test step functionality.

- The first step, Multiple Numeric Limit Test 1, calls a code module that inserts
 the measurement values one element at a time into the
 Step.NumericArray property. For example, the step inserts
 the value for the VOLTAGE 0 measurement in
 Step.NumericArray[0] , inserts the value for the
 VOLTAGE 1 measurement in
 Step.NumericArray[1] , and so on, as shown on the Data
 Source tab of the Step Settings pane.
- The second step, Multiple Numeric Limit Test 2, calls a code module that writes
 a single numeric array to the Step.NumericArray property
 instead of writing the four array elements individually.
- The third step, Multiple Numeric Limit Test 3, uses the <None> Adapter and
 therefore does not call a code module. The Data Source tab of the Step Settings
 pane for this step shows that the step obtains measurement values from local
 variables such as Locals.Voltage0 ,
 Locals.Voltage1 , and so on instead of from the
 Step.NumericArray property. The Statement steps in the
 Setup step group use expressions to assign these variables.
- The fourth step, Multiple Numeric Limit Test 4, is similar to the third step,
 but demonstrates the new EQ+/- comparison type supported by
 TestStand 2016 and later. See the table below for more information about this
 step's threshold values.

| Measurement | Comparison | Threshold | Nominal Value | Lower Threshold | Upper Threshold | Computed Low Limit | Computed High Limit |
| --- | --- | --- | --- | --- | --- | --- | --- |
| VOLTAGE 0 | EQ (==+/-) | Percentage | 4 | 25 | 25 | 3 | 5 |
| VOLTAGE 1 | EQ (==+/-) | PPM | 4 | 250000 | 250000 | 3 | 5 |
| FREQUENCY | EQ (==+/-) | Delta Value | 115 | 5 | 10 | 110 | 125 |
| RMS | EQ (==+/-) | Delta Value | 0.75 | 0.25 | 0.25 | 0.5 | 1 |

For a Multiple Numeric Limit Test step to pass, every test in the step must
 pass. You can try changing a limit to cause a test to fail, but ensure that you do
 not save any changes to the sequence file before executing the sequence or closing
 the sequence file.

Parent topic:

Multiple Numeric Limit Test Step Type

Related concepts:

- TestStand Directory Structure
- Step Groups

<!--NI_TOPIC bundle=teststand path=multiple-numeric-limit-test-step-type-labwind.html language=enus -->
## TOPIC 00618: Multiple Numeric Limit Test Step Type - LabWindows/CVI

- bundle_id: `teststand`
- source_path: `multiple-numeric-limit-test-step-type-labwind.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/multiple-numeric-limit-test-step-type-labwind.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Purpose This example demonstrates how to use a Multiple Numeric Limit Test step with a LabWindows/CVI code module. Example File Location <TestStand Public>\Examples\Built-In Step Types\Multiple Numeric Limit Test Step Type\CVI\Multiple Numeric Limit Step Type.seq Highlighted Features Multiple Numeri

### Multiple Numeric Limit Test Step Type - LabWindows/CVI

#### Purpose

This example demonstrates how to use a Multiple Numeric Limit Test step with a LabWindows/CVI code module.

#### Example File
 Location

<TestStand
 Public>\Examples\Built-In Step Types\Multiple Numeric Limit Test
 Step Type\CVI\Multiple Numeric Limit Step Type.seq

#### Highlighted Features

Multiple Numeric Limit Test steps

#### Major API

None

#### Prerequisites

You must have the LabWindows/CVI Run-Time Engine installed and you must configure the LabWindows/CVI Adapter to execute steps in-process. If you want to use the Execute Steps in an External Instance of CVI option, you must have the LabWindows/CVI development environment installed.

#### How to Use This
 Example

This example contains four Multiple Numeric Limit Test steps. The
 first three steps obtain four measurement values and compare them to the following
 high and low values specified on the Limits tab of the Step Settings pane:

| Measurement | Comparison | Low Value | High Value |
| --- | --- | --- | --- |
| VOLTAGE 0 | GELE (>= <=) | 3 | 5 |
| VOLTAGE 1 | GELE (>= <=) | 3 | 5 |
| FREQUENCY | GELE (>= <=) | 110 | 125 |
| RMS | GELE (>= <=) | 0.5 | 1.0 |

Each step demonstrates a different way of using the Multiple Numeric Limit
 Test step functionality.

- The first step, Multiple Numeric Limit Test 1, calls a code module that inserts
 the measurement values one element at a time into the
 Step.NumericArray property. For example, the step inserts
 the value for the VOLTAGE 0 measurement in
 Step.NumericArray[0] , inserts the value for the
 VOLTAGE 1 measurement in
 Step.NumericArray[1] , and so on, as shown on the Data
 Source tab of the Step Settings pane.
- The second step, Multiple Numeric Limit Test 2, calls a code module that writes
 a single numeric array to the Step.NumericArray property
 instead of writing the four array elements individually.
- The third step, Multiple Numeric Limit Test 3, uses the <None> Adapter and
 therefore does not call a code module. The Data Source tab of the Step Settings
 pane for this step shows that the step obtains measurement values from local
 variables such as Locals.Voltage0 ,
 Locals.Voltage1 , and so on instead of from the
 Step.NumericArray property. The Statement steps in the
 Setup step group use expressions to assign these variables.
- The fourth step, Multiple Numeric Limit Test 4, is similar to the third step,
 but demonstrates the new EQ+/- comparison type supported by
 TestStand 2016 and later. See the table below for more information about this
 step's threshold values.

| Measurement | Comparison | Threshold | Nominal Value | Lower Threshold | Upper Threshold | Computed Low Limit | Computed High Limit |
| --- | --- | --- | --- | --- | --- | --- | --- |
| VOLTAGE 0 | EQ (==+/-) | Percentage | 4 | 25 | 25 | 3 | 5 |
| VOLTAGE 1 | EQ (==+/-) | PPM | 4 | 250000 | 250000 | 3 | 5 |
| FREQUENCY | EQ (==+/-) | Delta Value | 115 | 5 | 10 | 110 | 125 |
| RMS | EQ (==+/-) | Delta Value | 0.75 | 0.25 | 0.25 | 0.5 | 1 |

For a Multiple Numeric Limit Test step to pass, every test in the step must
 pass. You can try changing a limit to cause a test to fail, but ensure that you do
 not save any changes to the sequence file before executing the sequence or closing
 the sequence file.

Parent topic:

Multiple Numeric Limit Test Step Type

Related concepts:

- TestStand Directory Structure
- Step Groups

<!--NI_TOPIC bundle=teststand path=multiple-numeric-limit-test-step-type-net.html language=enus -->
## TOPIC 00619: Multiple Numeric Limit Test Step Type - .NET

- bundle_id: `teststand`
- source_path: `multiple-numeric-limit-test-step-type-net.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/multiple-numeric-limit-test-step-type-net.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Purpose This example demonstrates how to use a Multiple Numeric Limit Test step with a .NET assembly code module. Example File Location <TestStand Public>\Examples\Built-In Step Types\Multiple Numeric Limit Test Step Type\DotNET\Multiple Numeric Limit Step Type.seq Highlighted Features Multiple Nume

### Multiple Numeric Limit Test Step Type - .NET

#### Purpose

This example demonstrates how to use a Multiple Numeric Limit Test step with a .NET assembly code module.

#### Example File
 Location

<TestStand
 Public>\Examples\Built-In Step Types\Multiple Numeric Limit Test
 Step Type\DotNET\Multiple Numeric Limit Step Type.seq

#### Highlighted Features

Multiple Numeric Limit Test steps

#### Major API

None

#### Prerequisites

None

#### How to Use This
 Example

This example contains four Multiple Numeric Limit Test steps. The
 first three steps obtain four measurement values and compare them to the following
 high and low values specified on the Limits tab of the Step Settings pane:

| Measurement | Comparison | Low Value | High Value |
| --- | --- | --- | --- |
| VOLTAGE 0 | GELE (>= <=) | 3 | 5 |
| VOLTAGE 1 | GELE (>= <=) | 3 | 5 |
| FREQUENCY | GELE (>= <=) | 110 | 125 |
| RMS | GELE (>= <=) | 0.5 | 1.0 |

Each step demonstrates a different way of using the Multiple Numeric Limit
 Test step functionality.

- The first step, Multiple Numeric Limit Test 1, calls a code module that inserts
 the measurement values one element at a time into the
 Step.NumericArray property. For example, the step inserts
 the value for the VOLTAGE 0 measurement in
 Step.NumericArray[0] , inserts the value for the
 VOLTAGE 1 measurement in
 Step.NumericArray[1] , and so on, as shown on the Data
 Source tab of the Step Settings pane.
- The second step, Multiple Numeric Limit Test 2, calls a code module that writes
 a single numeric array to the Step.NumericArray property
 instead of writing the four array elements individually.
- The third step, Multiple Numeric Limit Test 3, uses the <None> Adapter and
 therefore does not call a code module. The Data Source tab of the Step Settings
 pane for this step shows that the step obtains measurement values from local
 variables such as Locals.Voltage0 ,
 Locals.Voltage1 , and so on instead of from the
 Step.NumericArray property. The Statement steps in the
 Setup step group use expressions to assign these variables.
- The fourth step, Multiple Numeric Limit Test 4, is similar to the third step,
 but demonstrates the new EQ+/- comparison type supported by
 TestStand 2016 and later. See the table below for more information about this
 step's threshold values.

| Measurement | Comparison | Threshold | Nominal Value | Lower Threshold | Upper Threshold | Computed Low Limit | Computed High Limit |
| --- | --- | --- | --- | --- | --- | --- | --- |
| VOLTAGE 0 | EQ (==+/-) | Percentage | 4 | 25 | 25 | 3 | 5 |
| VOLTAGE 1 | EQ (==+/-) | PPM | 4 | 250000 | 250000 | 3 | 5 |
| FREQUENCY | EQ (==+/-) | Delta Value | 115 | 5 | 10 | 110 | 125 |
| RMS | EQ (==+/-) | Delta Value | 0.75 | 0.25 | 0.25 | 0.5 | 1 |

For a Multiple Numeric Limit Test step to pass, every test in the step must
 pass. You can try changing a limit to cause a test to fail, but ensure that you do
 not save any changes to the sequence file before executing the sequence or closing
 the sequence file.

Parent topic:

Multiple Numeric Limit Test Step Type

Related concepts:

- TestStand Directory Structure
- Step Groups

<!--NI_TOPIC bundle=teststand path=multiple-numeric-limit-test-step-type.html language=enus -->
## TOPIC 00620: Multiple Numeric Limit Test Step Type

- bundle_id: `teststand`
- source_path: `multiple-numeric-limit-test-step-type.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/multiple-numeric-limit-test-step-type.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The <TestStand Public>\Examples\Built-In Step Types\Multiple Numeric Limit Test Step Type directory contains the following examples.

### Multiple Numeric Limit Test Step Type

The <TestStand
 Public>\Examples\Built-In Step Types\Multiple Numeric Limit Test
 Step Type directory contains the following examples.

- [Multiple Numeric Limit Test Step Type - LabWindows/CVI](multiple-numeric-limit-test-step-type-labwind.html)
- [Multiple Numeric Limit Test Step Type - LabVIEW](multiple-numeric-limit-test-step-type-labview.html)
- [Multiple Numeric Limit Test Step Type - .NET](multiple-numeric-limit-test-step-type-net.html)

Parent topic:

Examples for Built-In Step Types

Related concepts:

- TestStand Directory Structure

<!--NI_TOPIC bundle=teststand path=multiple-window-applications.html language=enus -->
## TOPIC 00621: Multiple Window Applications

- bundle_id: `teststand`
- source_path: `multiple-window-applications.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/multiple-window-applications.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: A multiple window application includes at least one window that always exists to contain the Application Manager control. Although this window can be visible or invisible, it is typically visible and contains controls for users to open sequence files. Sequence File Window For each sequence file user

### Multiple Window Applications

A multiple window application includes at least one window that always exists to contain the Application Manager control. Although this window can be visible or invisible, it is typically visible and contains controls for users to open sequence files.

#### Sequence File Window

For each sequence file users open, the application creates a Sequence File window that contains a SequenceFileView Manager control and a SequenceView control to which the manager control connects. The application sets the SequenceFileViewMgr.UserData property to attach a handle, reference, or pointer that represents the window. When the application receives the ApplicationMgr.DisplaySequenceFile event, the application calls ApplicationMgr.GetSequenceFileViewMgr to determine whether a SequenceFileView Manager control currently displays the sequence file. If so, the application retrieves the window from the SequenceFileViewMgr.UserData property and activates the window. If no window currently displays the sequence file, the application creates a new window and sets the SequenceFileViewMgr.SequenceFile property to display the sequence file. Because the window displays only this sequence file, the application also sets the SequenceFileViewMgr.ReplaceSequenceFileOnClose property to False.

When a Sequence File window attempts to close and the SequenceFileViewMgr.SequenceFile property is NULL, the application closes the window immediately. When the SequenceFileViewMgr.SequenceFile property is not NULL, the application does not close the window. Instead, the application passes the sequence file to the ApplicationMgr.CloseSequenceFile method. When the application receives the SequenceFileViewMgr.SequenceFileChanged event with a NULL sequence file event parameter, the application closes the window that holds the SequenceFileView Manager control.

#### Execution Window

The Sequence File window contains controls for users to execute the sequence file the window displays. For each execution users start, the application creates an Execution window that contains an ExecutionView Manager control and a SequenceView control to which the manager control connects. The application sets the ExecutionViewMgr.UserData property to attach a handle, reference, or pointer that represents the window. When the application receives the ApplicationMgr.DisplayExecution event, the application calls the ApplicationMgr.GetExecutionViewMgr method to determine whether an ExecutionView Manager control currently displays the execution. If so, the application retrieves the window from the ExecutionViewMgr.UserData property and activates the window. If no window currently displays the execution, the application creates a new window and sets the ExecutionViewMgr.Execution property to display the execution. Because the window displays only this execution, the application also sets the ExecutionViewMgr.ReplaceExecutionOnClose property to False.

When an Execution window attempts to close and the ExecutionViewMgr.Execution property is NULL, the application closes the window immediately. When the ExecutionViewMgr.Execution property is not NULL, the application does not close the window. Instead, the application passes the execution to the ApplicationMgr.CloseExecution method. The application does not immediately close the Execution window to ensure that the window exists until the execution the window displays completes. When the application receives the ExecutionViewMgr.ExecutionChanged event with a NULL execution event parameter, the application closes the window that holds the ExecutionView Manager control.

#### Child Windows

A multiple window application can display multiple child windows instead of displaying sequence files and executions in separate top-level windows. Child windows can be visible or reside on tab control pages or similar locations that allow users to easily select which child window to view.

Parent topic:

User Interface Application Styles

Related concepts:

- Application Manager
- SequenceFileView Manager
- ExecutionView Manager

<!--NI_TOPIC bundle=teststand path=national-instruments-msi-based-installer-arch.html language=enus -->
## TOPIC 00622: NI MSI-based Installer Architecture

- bundle_id: `teststand`
- source_path: `national-instruments-msi-based-installer-arch.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/national-instruments-msi-based-installer-arch.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Microsoft Windows Installer technology works well for single, independent applications, but many NI products are interdependent and share sets of features. Therefore, NI developed an MSI-based installer architecture to accomplish the following tasks: Install, uninstall, or upgrade products independe

### NI MSI-based Installer Architecture

Microsoft Windows Installer technology works well for single, independent applications, but many
 NI products are interdependent and share sets of features. Therefore, NI developed
 an MSI-based installer architecture to accomplish the following tasks:

- Install, uninstall, or upgrade products independently or as part of a larger installation
- Define dependencies among products
- Provide a common user interface so all installations or uninstallations of NI products appear as
 a single operation, which is necessary because each NI product uses a series of
 smaller MSI-based installers

The NI MSI-based installer architecture uses parts, which represent the smallest unit the NI
 MSI-based installer requires to track by version or the largest indivisible group of
 features. Parts are Windows installation packages that contain one or more Windows
 Installer database files that include additional custom tables NI defines.

A product consists of one or more parts and an XML file that describes the product. You can include a part in several products to share common features among products. The XML file lists the product requirements and properties, such as the product name, description, and whether that product is redistributable, which means that you can include the product in other MSI-based installers. For example, you can include the LabWindows/CVI Run-Time Engine in an MSI-based installer you build with the TestStand Deployment Utility.

A distribution includes one or more parts and required support files for all the features of a product. Running the installer executable from the distribution media might display a list from which you can select features to install. Customizing this list changes the features a part installs or changes the set of parts to install. During installation, the setup application iterates through each part that contains the features you selected to install. If a part is not already installed or if the part is a later version than the part already installed on the computer, the setup application installs the part. If the part already installed on the computer specifies a version that is a later or equal version to the version of the part in the MSI-based installer, the MSI-based installer does not install that part. The MSI-based installer user interface represents the series of part installations as a single, unified installation by showing a progress bar for the current part and an overall progress bar for the installation of all the parts.

When you remove NI software, the MSI-based uninstaller user interface lists the products and
 patches installed on the computer from which you can select the products to remove.
 Before removing a product, the NI MSI-based uninstaller confirms that no other
 products on the computer require the product parts you want to uninstall.

When you modify features of a product, the NI MSI-based installer installs the parts required for
 the features you add and uninstalls parts for the features you remove. Before
 removing a part, the NI MSI-based uninstaller confirms that no other products on the
 computer require the parts you want to uninstall.

Parent topic:

Relationship of NI MSI-based Installer Architecture and Microsoft Windows Installer Technology

Related concepts:

- Relationship of NI MSI-based Installer Architecture and Microsoft Windows Installer Technology
- Redistributing MSI-based Installer Products in a Deployment
- Uninstalling a TestStand Deployment

<!--NI_TOPIC bundle=teststand path=nested-sections-synchronized-sections.html language=enus -->
## TOPIC 00623: Nested Sections - Synchronized Sections

- bundle_id: `teststand`
- source_path: `nested-sections-synchronized-sections.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/nested-sections-synchronized-sections.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Nested sections can occur within the same sequence or when you call a subsequence inside a synchronized section and the subsequence also contains a synchronized section. You must exit nested sections in the reverse order in which you entered the sections. When you nest one section inside another, Te

### Nested Sections - Synchronized Sections

Nested sections can occur within the same sequence or when you call a subsequence inside a synchronized section and the subsequence also contains a synchronized section. You must exit nested sections in the reverse order in which you entered the sections.

When you nest one section inside another, TestStand honors the inner section only when the type of the outer section is serial or parallel. TestStand ignores the inner section when the type of the outer section is One Thread Only. For example, when you nest one serial section in another serial section, each thread that enters the outer serial section proceeds only until the Enter step of the inner section and then waits for the other threads to reach the same Enter step of the inner section before completing the inner section.

Parent topic:

Synchronized Sections

<!--NI_TOPIC bundle=teststand path=net-adapter.html language=enus -->
## TOPIC 00624: .NET Adapter

- bundle_id: `teststand`
- source_path: `net-adapter.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/net-adapter.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the .NET Adapter to call .NET assemblies written in any .NET-compliant language, such as C# or Microsoft Visual Basic .NET. TestStand installs .NET if it is not present on your machine during installation, which allows you to take advantage of the capabilities of the .NET Adapter. You can config

### .NET Adapter

Note

Note

Parent topic:

Module Adapters

Related concepts:

- Code Modules
- .NET Code Module Support for 64-bit TestStand
- Adapter and Code Module Support for 64-bit TestStand
- AnyCPU Assemblies in 32-bit TestStand and 64-bit TestStand
- Module Adapter Parameter Mapping Guidelines
- Platform-Specific Assemblies in 32-bit TestStand and 64-bit TestStand
- Programming with the TestStand API in Microsoft Visual Basic .NET
- TestStand Sequence Analyzer

Related reference:

- TestStand 2024 Q4 Changes

<!--NI_TOPIC bundle=teststand path=net-code-module-support-for-64-bit-teststand.html language=enus -->
## TOPIC 00625: .NET Code Module Support for 64-bit TestStand

- bundle_id: `teststand`
- source_path: `net-code-module-support-for-64-bit-teststand.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/net-code-module-support-for-64-bit-teststand.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: When you migrate .NET code modules from 32-bit TestStand to 64-bit TestStand, NI recommends using platform-independent AnyCPU assemblies in shared locations. Use one of the following techniques to migrate platform-specific assemblies: Use the $(Platform) path macro. Place the assembly in a non-share

### .NET Code Module Support for 64-bit TestStand

When you migrate .NET code modules from 32-bit TestStand to 64-bit TestStand, NI recommends using
 platform-independent AnyCPU assemblies in shared locations. Use one of the following
 techniques to migrate platform-specific assemblies:

- Use the $(Platform) path macro.
- Place the assembly in a non-shared search directory.

Note

Parent topic:

Adapter and Code Module Support for 64-bit TestStand

Related concepts:

- AnyCPU Assemblies in 32-bit TestStand and 64-bit TestStand
- Platform-Specific Assemblies in 32-bit TestStand and 64-bit TestStand

<!--NI_TOPIC bundle=teststand path=net-hot-reload-ts.html language=enus -->
## TOPIC 00626: Enabling Code Module Hot Reloading During Step-Into Debugging in TestStand

- bundle_id: `teststand`
- source_path: `net-hot-reload-ts.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/net-hot-reload-ts.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `task`
- source_description: TestStand supports hot reloading of .NET code modules during step-into debugging to increase debugging efficiency. To enable code module hot reloading in TestStand: Create an environment variable named COMPLUS_ForceENC = 1. Configure your .NET step to use the Visual Studio Project or Solution where

### Enabling Code Module Hot Reloading During
 Step-Into Debugging in TestStand

TestStand supports hot reloading of .NET code modules during step-into debugging to
 increase debugging efficiency.

To enable code module hot reloading in
 TestStand:

1. Create an environment variable named COMPLUS_ForceENC =
 1.
2. Configure your .NET step to use the Visual Studio Project or Solution where
 your code is sourced.
3. Step into the configured .NET function from TestStand. This
 launches Visual Studio, where you can make changes to your
 .NET function and hot reload the code module once you
 finalize your changes.

Note

Note

Note

Visual Studio Unsupported .NET
 and .NET Framework Projects

Visual Studio
 Supported Code Changes (C# and Visual Basic)

Parent topic:

Debugging .NET Assemblies

Related information:

- Visual Studio Supported Code Changes (C# and Visual Basic)
- Visual Studio Unsupported .NET and .NET Framework Projects

<!--NI_TOPIC bundle=teststand path=net-support-ts-api.html language=enus -->
## TOPIC 00627: .NET Support for the TestStand API

- bundle_id: `teststand`
- source_path: `net-support-ts-api.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/net-support-ts-api.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: TestStand installs .NET interop assemblies for the TestStand API in the <TestStand>\API\DotNet\Assemblies directory and in the Global Assembly Cache (GAC). The interop assemblies support the current and earlier versions of the TestStand API, as shown in the following table. TestStand API Version .NE

### .NET Support for the TestStand API

TestStand installs .NET interop assemblies for the TestStand API in the
 <TestStand>\API\DotNet\Assemblies directory and in the Global
 Assembly Cache (GAC). The interop assemblies support the current and earlier versions of the
 TestStand API, as shown in the following table.

| TestStand API Version | .NET Version |  |
| --- | --- | --- |
| TestStand 2025 Q2 and later | .NET 8 (CLR 5.0 or later) |  |
| TestStand 2024 Q4 | For .NET Adapter | .NET 8 (CLR 5.0 or later) |
| For user interfaces | .NET Framework CLR 4.0 |  |
| TestStand 2012 — TestStand 2023 Q4 | .NET Framework CLR 4.0 |  |
| TestStand 4.0 — TestStand 2010 SP1 | .NET Framework CLR 2.0 |  |
| TestStand 3.5 or earlier | .NET Framework CLR 1.1 |  |

Parent topic:

Programming with the TestStand API in Different Languages

<!--NI_TOPIC bundle=teststand path=network-based-deployment-mechanisms.html language=enus -->
## TOPIC 00628: Network-Based Deployment Mechanisms

- bundle_id: `teststand`
- source_path: `network-based-deployment-mechanisms.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/network-based-deployment-mechanisms.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use a network drive or source code control (SCC) system to transfer test system files to test station computers, but you must also run an installer on the test station computer to correctly install the TestStand Runtime and other NI software. Because installers edit the registry, execute fil

### Network-Based Deployment Mechanisms

You can use a network drive or source code control (SCC) system to transfer test system files to
 test station computers, but you must also run an installer on the test station
 computer to correctly install the TestStand Runtime and other NI software. Because
 installers edit the registry, execute files, start Microsoft Windows services, call
 DLLs during installation, and other related tasks, copying test system files to the
 test station computer is not sufficient for the test system to function correctly.
 Because of the complexity of trying to reproduce all the actions an installer
 performs, NI strongly recommends that you use the NI installers or an installer you
 build with the TestStand Deployment Utility to install NI drivers and components and
 the TestStand Runtime.

#### Updating Test Systems Using a Network-Based Solution

When you create a new deployable image to replace an existing deployable image, delete the previous deployable image from the network drive or SCC system before you copy or check in the new version to ensure that the network drive or SCC system does not include files you removed from the deployable image.

By default, when you create a patch deployable image, the image includes only modified files. Check the patch deployable image into the SCC system or copy the image to the network drive and overwrite files in the existing full deployable image to ensure the network drive includes updated files.

If you use a network drive or SCC system to update test systems you deploy to test station computers, design the update process to manage network outages and race conditions.

#### Network Outages

When a test station computer cannot connect to other computers on the network during an update process, the test system might not update correctly with all the required files. For example, to change the prototype of a code module, you must update the code module and the sequences that call the code module. If the test station computer accesses and updates only the code module file but not the sequence files because of a network outage, the existing sequence files on the test station computer cannot load the new code module with the updated prototype, which causes failures in the test system.

You can prevent partial updates by using a temporary directory on the test station computer to store all the updates before moving the updates to the test system directory. You can design the update process so a network outage during the process of updating the temporary directory generates an error and does not copy the partial updates from the temporary directory to the test station directory, which leaves the functional test system unchanged.

#### Race Conditions

Race conditions occur when the results of a process depend on the order in which tasks complete. To avoid race conditions when you use a network-based solution to update test systems, you must make changes to the files in the central network location before the test station computers access the files.

For example, if you change a sequence file and the related code modules on a network drive just after a test station computer loads the sequence file but before TestStand loads the code modules, TestStand loads the old sequence file and the new code modules at the start of execution. This action might lead to incorrect test results if the new code modules require limits the old sequence files do not contain or might lead to errors executing the sequence file if the code module prototypes do not match the prototypes the sequence file expects. Race conditions can also occur when sequences load code modules dynamically because old sequence files might load incompatible new code modules.

You can avoid race conditions by ensuring that the test system does not load sequences during the update process. For example, you can avoid performing updates to files in the central network location during production testing or you can transfer updates to a temporary directory and then to the test system directory only when the test system unloads all the files.

#### Validating Network-Based Deployments

For cases where frequent updates are needed, a Continuous Integration and Delivery (CI/CD) approach can help ensure that the latest code is available on test computers, while still ensuring the code has been properly tested and validated. With a CI/CD approach, you automate much of the procedure to build, test, and deploy updates to test code to reduce overhead as much as possible. You can use third party tools, such as Jenkins, to implement this type of automation. For more information on using Jenkins to automate TestStand deployments, refer to the Getting Started with TestStand and Jenkins tutorial.

For more tightly controlled environments, validation requirements are typically very stringent, and therefore test system updates cannot occur frequently. For these test systems, define a separate repository or trunk where developers make changes and add new features to the test. Once the latest version of the test system has been finalized and validated, developers create a versioned branch of the trunk for use on production machines. This branch should be locked within source code control to prevent any changes to validated code. Once the new branch is completed and validated, create a new versioned branch containing the code.

Parent topic:

Choosing a Deployment Mechanism

Related concepts:

- Using a Network Drive to Deploy Test Systems
- Using a Source Code Control System to Deploy Test Systems
- Redistributing MSI-based Installer Products in a Deployment
- Patching Deployments

<!--NI_TOPIC bundle=teststand path=new-features-and-changes.html language=enus -->
## TOPIC 00629: TestStand New Features and Changes

- bundle_id: `teststand`
- source_path: `new-features-and-changes.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/new-features-and-changes.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Learn about updates, including new features and behavior changes, introduced in each version of TestStand. Discover what is new in the latest releases of TestStand.If you cannot find new features and changes for your version, it might not include user-facing updates. However, your version might incl

### TestStand
 New Features and Changes

Learn about updates, including new features and behavior changes, introduced in each
 version of TestStand.

TestStand

Note

Release Notes

Related information:

- TestStand Release Notes - Known Issues, Bug Fixes, and More

#### TestStand 2026 Q1 Changes

Learn about new features, behavior changes, and other updates in TestStand 2026
 Q1.

##### Step Type Isolation

Use
 the UseSeparateAlc and UseAlcFromStepType attributes to create a new assembly load
 context per step type. These attributes provide isolation for modules loaded for
 step settings pane, code module execution and substeps of the step
 type.

##### NI
 Nigel™ AI for Results

Enable system metadata logging
 and ask Nigel to analyse test results to root cause failures and get insight into
 your tests.

##### NI
 Nigel™ AI for Test Workflows

Ask Nigel to explain
 unfamiliar test sequences, so you can get up to speed.

##### Python
 3.14 Support

TestStand Python Adapter supports Python modules developed
 using Python 3.14. TestStand Python Adapter don't support free-threaded
 Python.

Related concepts:

- Measurement Data Service Data Store

Related tasks:

- Configuring Isolated Execution Environments for .NET Modules
- Logging Metadata for Analysis

#### TestStand 2025 Q3 Changes

Learn about new features, behavior changes, and other updates in TestStand 2025
 Q3.

##### Introducing NI Nigel™, AI Advisor

Nigel is your trusted test and measurement advisor, trained
 on the NI platform and ready to help when you need it. Change TestStand and sequence
 file settings, learn TestStand concepts, and more!

##### Import
 Specifications Using the Specifications Pane

Use the
 Specifications pane to import specifications directly from
 a SystemLink Enterprise server or Excel file and convert the imported specifications
 into steps, sweep loops, and variables in your sequence files. This functionality
 replaces the Specification Compliance Manager (SCM) tool specification import
 workflow.

Related concepts:

- Importing Specifications into TestStand Using the Specifications Pane
- NI Nigel AI

#### TestStand 2025 Q2 Changes

Learn about new features, behavior changes, and other updates in TestStand 2025
 Q2.

##### TestStand
 2025 Q2 Installation Location

If you install TestStand 2025 Q2 on a device
 where TestStand 2024 Q4 is already installed, TestStand 2025 Q2 installs as an
 update to TestStand 2024 Q4 rather than a separate instance of TestStand software.
 Installing TestStand 2025 Q2 on a device where no prior TestStand software is
 installed, or on a device where an older version of TestStand than 2024 Q4 is
 installed, installs TestStand 2025 Q2 as a separate software instance at
 C:\<Program Files>\National Instruments\TestStand
 2024.

##### .NET 8 Support Updates in
 TestStand

- TestStand Sequence Editor
- TestStand user interfaces and operator interfaces
- Tools such as the TestStand Sequence File Analyzer and TestStand File Diff
 and Merge Utility
- Step settings panels and substeps of all TestStand step types
- .NET-based plug-ins such as process models and the TestStand Sequence
 Analyzer

Note

##### Git
 Pane

The TestStand Sequence Editor provides a Git pane that allows you to
 connect to Git repositories on platforms including Azure DevOps, GitHub, and
 BitBucket and perform common version control operations from within the Sequence
 Editor. This new pane eliminates the need to perform version control operations on
 TestStand project files using a separate Git client.

##### TestStand
 Usage Within Continuous Integration Workflows

TestStand Development
 licenses now support the use of TestStand within continuous integration (CI) and
 continuous development (CD) workflows. Single-seat license users can now use their
 TestStand Development System licenses for both development purposes and CI/CD
 workflows, while volume license agreement (VLA) users can add the *TestStand
 Continuous Integration for VLAs* part number to their VLA to use TestStand
 in CI/CD workflows without using a development license seat. The TestStand End-User
 License Agreement (EULA) supports CI/CD uses of the TestStand Development System
 license.

##### API and UI
 Control Additions and Changes

- Properties
  - DotNetModule.AllowUnload
- Methods
  - DotNetAdapter.CacheAssemblyInfoEx
  - DotNetAdapter.IsClassValidEx

Note

Related concepts:

- Selecting a Source Code Control Provider
- Activating and Licensing TestStand
- Managed Code Considerations for TestStand and .NET 8
- Calling LabVIEW VIs That Invoke .NET Code in TestStand

Related reference:

- Migrating User Interfaces to .NET Core

#### TestStand 2024 Q4 Changes

Learn about new features, behavior changes, and other updates in TestStand 2024
 Q4.

##### .NET
 Adapter — .NET Assembly Execution Support

The .NET adapter now supports
 .NET 8 for .NET code module execution. You can still execute .NET Framework
 assemblies using .NET as long as the resources used in the .NET Framework assemblies
 are present in .NET 8.

- The IOConfig step type no longer works with the .NET
 Adapter. The device drivers are located in the .NET Framework GAC location,
 and .NET 8 does not support loading assemblies from the GAC.
- Creating remote objects in the TestStand .NET step using the
 CreateRemoteObject method is no longer supported.
- Calling into the following assemblies is no longer supported:
  - GAC assemblies
  - .NET assemblies with dependencies on GAC assemblies
  - C++/CLI assemblies
- Consider the following when working with .NET assemblies and LabVIEW:
  - .NET assemblies called by a VI are not automatically added to
 TestStand deployments. You must manually add these dependencies to
 deployments they are used in.
  - NET Framework assembly dependencies called by LabVIEW during the
 execution of a TestStand .NET step must be placed next to these .NET
 Framework assemblies to prevent runtime execution errors. These
 dependencies can be found in the LabVIEW installation
 directory.
  - Passing .NET objects between LabVIEW and TestStand is no longer
 supported.
- Sequence Editor layout files from previous TestStand versions are no longer
 supported.
- Consider the following when handling TestStand objects in managed code:
  - Explicitly dispose of instances of classes implementing
 IDisposable .
  - Explicitly assign null to class member variables of
 TestStand types, like Engine ,
 SequenceContext , and
 PropertyObject , when the class is no longer in
 use.
  - Explicitly assign null to static variables of
 TestStand types, like Engine ,
 SequenceContext , and
 PropertyObject , before shutting the TestStand
 Engine down.

##### Support
 for Using Sequence Files Across Multiple Versions of TestStand

The
 TestStand Engine no longer updates to a new version with every new release of
 TestStand. This allows you to use sequence files in multiple versions of TestStand
 without needing to use Save As to save the file for each
 version of TestStand you want to use it in. Save As now only
 needs to be used to run sequence files in versions of TestStand with different
 engine versions than the version it was originally written in. The engine version of
 your version of TestStand can be determined by consulting the program information at Help»About TestStand.

Features from later versions of TestStand are not supported in
 earlier versions of TestStand, even if the versions run on the same engine version.
 The TestStand Analyzer can detect these support mismatches and notify the
 user.

Support mismatches can also occur in custom types used between versions
 of TestStand. You can update your custom types according to the recommendations in
 *Modifying Types Without Altering the Version Number* to allow the
 TestStand Analyzer to detect and report support mismatches in custom data
 types.

##### Python
 Adapter — Support for Python Virtual Environments Created Using 'venv'

The
 TestStand Python Adapter now supports Python virtual environments created using the
 venv tool, in addition to virtual environments created using
 the earlier virtualenv tool.

##### LabVIEW
 Adapter — Source-Only VI Execution Support Through the Version-Independent Runtime
 Engine Support Feature

You can use the Version Independent
 Runtime Engine Support feature in the LabVIEW Adapter as an option
 to avoid potential issues when executing source-only VIs using the LabVIEW Runtime
 Engine through the LabVIEW adapter. These issues can occur if the LabVIEW version
 that the source-only VI was saved or mass-compiled in does not match the LabVIEW
 Runtime engine version, as VI version no longer gets updated during a save or
 mass-compile.

##### Auto Login
 for TestStand Default User

administrator

- A user clicks on the Login option
- The administrator account has a configured
 password
- Additional user accounts other than administrator are
 present

##### TestStand Sequence Editor Visual Design
 Updates

TestStand 2024 Q4 introduces visual changes to the TestStand
 Sequence Editor designed to provide better contrast in the Sequence Editor, provide
 relief in the menu and tool bars, and reduce the background colour of Sequence
 Editor panes.

##### New Help
 Delivery Experience

ni.com/docs

Note

online

offline

Note

##### API and UI
 Control Additions and Changes

- Enumeration and Constant Values
  - StepType_If
  - StepType_Else
  - StepType_ElseIf
  - StepType_For
  - StepType_ForEach
  - StepType_While
  - StepType_DoWhile
  - StepType_Break
  - StepType_Continue
  - StepType_Select
  - StepType_Case
  - StepType_End
  - StepType_StreamLoop
  - StepType_SweepLoop
  - StepType_Wait
  - VisualStudioDTEVersion_2022
- Properties
  - EngineVersionString
  - ChildExecutionIds
  - ParentExecutionId
- Methods
  - DisplayHelpTopicEx
  - GetExecution

Note

Related concepts:

- Modifying Types Without Altering the Version Number

Related tasks:

- Executing Source-Only VIs in LabVIEW Runtime Engine

Related information:

- Microsoft - Breaking Changes for Migration from .NET Framework to .NET
 Core

#### TestStand 2023 Q4 Changes

Learn about new features, behavior changes, and other updates in TestStand 2023
 Q4.

##### Build
 Source Files and Execute Feature

The new Build Source Files and
 Execute feature adds support for executing source-only VIs in
 TestStand using the TestStand LabVIEW adapter when it is configured to use the
 LabVIEW runtime engine. This feature adds this support by compiling LabVIEW modules
 necessary for execution into a Packed Project Library (PPL) before execution
 begins.

##### Import/Update from Specification Compliance Manager Tool

The new
 Import/Update from Specification Compliance Manager tool
 lets you connect to a Specification Compliance Manager (SCM) server from TestStand.
 You can import data from a server to a sequence file as variables to use in
 configuring measurement conditions, sweeps, and test limits. The tool also allows
 you to log results tied to imported data and pass the logged results back to SCM for
 analysis.

##### TestStand
 Installer Feed Optimization

Reduced TestStand ISO image size improves
 download times and decreases the necessary storage space for the ISO image.
 Installers for GraphControl, IVIStepTypes,
 Runtime32, and Runtime64 have been removed
 from the ISO image, but are still available for installation through NI Package
 Manager and NI Package Builder.

##### Improvements to Working with Variables

You can now filter variables and
 their properties by name in the Call Stack pane using the new
 Filter control on the Variables pane
 on the Sequence File tab.

##### Hot
 Reloading in Visual Studio 2022 for C# and C++ Code Modules

TestStand now
 supports modifying C# and C++ code modules during debugging sessions in Visual
 Studio (VS) 2022 without the need to reload the modules in TestStand to get the
 updated code modules reloaded to memory. This added functionality leverages the hot
 reloading capability in VS 2022.

##### Python
 Adapter Improvements

Improved TestStand performance when using the
 Enum data type with the TestStand Python adapter to pass
 Enum values between TestStand and Python code
 modules.

##### API and UI
 Control Additions and Changes

Note

- Enumeration and Constant Values
  - UIStyleFontType_Subtitle2
- Properties
  - ApplicationVersionString
  - BuildAndExecuteAtStartOfExecution
- Methods
  - ClearBuildAndExecuteCache
  - IsBuildAndExecuteEnabled

Note

Related tasks:

- Installing TestStand

<!--NI_TOPIC bundle=teststand path=ni-tdmsreference.html language=enus -->
## TOPIC 00630: NI_TDMSReference

- bundle_id: `teststand`
- source_path: `ni-tdmsreference.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/ni-tdmsreference.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the NI_TDMSReference standard data type to identify references to NI Technical Data Management Streaming (.tdms) files in the TestStand ResultList local variable so you can log .tdms data in reports and in databases. Visit ni.com/tdms for more information about the .tdms file format. The NI_TDMS

### NI_TDMSReference

Use the NI_TDMSReference standard data type to identify references to NI Technical Data
 Management Streaming (.tdms) files in the TestStand
 ResultList local variable so you can log
 .tdms data in reports and in databases. Visit
 ni.com/tdms for more information about the
 .tdms file format.

The NI_TDMSReference data type includes the following subproperties. The report includes references to these subproperties only when you define values for the subproperties.

- File —Absolute path to the .tdms file you want to log
 in the report or database. TestStand automatically creates a
 TestStand.Hyperlink attribute set to True 
 to include a hyperlink to the file in supported versions of ATML, XML, and HTML
 reports. If the value of the Hyperlink attribute is
 False , the report displays the path as a string, not a
 link. You can open links to the .tdms file directly from
 supported versions of ATML, XML, and HTML reports and view information about the
 .tdms file in text reports.
- Plugin —Name of the DataPlugin that generated the file.
- ChannelGroup —Name of the channel group in which the data is recorded.
- Channel —Name of the channel in which the data is recorded.

When you use the XML Packaging Utility to distribute ATML, XML, and HTML reports that include links to .tdms files, the utility also distributes the target file of the link.

Parent topic:

Using Standard Named Data Types

Related concepts:

- Including Hyperlinks in Reports
- Including Hyperlinks in a Report - TDMS File
- Type Concepts

<!--NI_TOPIC bundle=teststand path=nigel-ai.html language=enus -->
## TOPIC 00631: NI Nigel AI

- bundle_id: `teststand`
- source_path: `nigel-ai.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/nigel-ai.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: NI Nigel AI is an AI which brings a wealth of knowledge about TestStand into your design process. Nigel can offer development advice and test system design information to help you create projects and sequences. Nigel is powered by Microsoft Azure OpenAI. Introduced in TestStand 2025 Q3 Nigel can hel

### NI Nigel AI

NI Nigel AI is an AI which brings a wealth of knowledge about TestStand into your
 design process. Nigel can offer development advice and test system design information
 to help you create projects and sequences. Nigel is powered by Microsoft Azure
 OpenAI.

Introduced in TestStand 2025 Q3

- Finding examples to give you a solid starting point for a project
- Providing instructions for completing a specific task
- Explaining key TestStand and sequence design concepts
- Assisting with finding specific settings or dialog boxes in the TestStand
 environment
- Summarizing documentation topics
- Describing local hardware and software characteristics
- Answering questions about hardware functionality and configuration
- Analyzing published test data and metadata

#### Installing Nigel

NI Nigel AI for
 TestStand <Version Year>

[IMAGE alt='image' src='GUID-5EB314CA-5771-4B3F-BE39-00A8DD06A1C7-a5.png']

#### Accessing Nigel

Figure 2.

[IMAGE alt='image' src='GUID-8DA45B00-E65E-42E9-B435-A2E402C4DD1A-a5.svg']

Figure 3.

[IMAGE alt='image' src='GUID-E0376936-2D8F-47A6-8031-C837AA5926BF-a5.png']

After you open Nigel, you must log in to your
 ni.com user account and ensure it is associated with an
 active subscription license, multi-seat license, or Software Service Program for
 TestStand Development System.

Note

#### Accessing Nigel Chat
 History

Nigel stores a history of users' chats and questions, which you can access using the
 Chat History button next to the Create New
 Chat button. You can rename, delete, and pin chats in the chat
 history to organize your chats and allow easy access to important questions.

Figure 4.

[IMAGE alt='image' src='GUID-7A805F7A-14A9-4CC2-8183-C9742A6A60B6-a5.png']

#### Rate Limits

Access to Nigel is rate
 limited per user and is measured as Requests Per Day (RPD). The RPD limit is shared
 between the TestStand chat and all LabVIEW Nigel search functions.

#### Disabling Nigel

- You can disable the Discuss with Nigel feature by setting the
 Computer\HKEY_LOCAL_MACHINE\SOFTWARE\National Instruments\Nigel
 AI Advisor\DisableNigelSharing registry key ( DWORD
 (32-bit), 0 or 1 ) to 1.
- You can disable all Nigel features, including Discuss with Nigel, chat, and
 search, by setting the Computer\HKEY_LOCAL_MACHINE\SOFTWARE\National
 Instruments\Nigel AI Advisor\DisableNigel registry key
 ( DWORD (32-bit), 0 or 1 ) to 1.

Parent topic:

TestStand Tools and Utilities

Related information:

- NI Nigel AI on ni.com

<!--NI_TOPIC bundle=teststand path=no-visible-window-applications.html language=enus -->
## TOPIC 00632: No Visible Window Applications

- bundle_id: `teststand`
- source_path: `no-visible-window-applications.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/no-visible-window-applications.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: An application without a visible window is similar to a single window application. The application can execute command-line arguments and then exit, or the application can have a different mechanism to determine which files to load and execute. Although an invisible application does not require an E

### No Visible Window Applications

An application without a visible window is similar to a single window application. The application can execute command-line arguments and then exit, or the application can have a different mechanism to determine which files to load and execute.

Although an invisible application does not require an ExecutionView Manager control, the application can use a SequenceFileView Manager control to provide methods to launch an execution for a sequence file. Use the SequenceFileViewMgr.ExecutionEntryPoints property, the SequenceFileViewMgr.Run method, the SequenceFileViewMgr.RunSelectedSteps method, the SequenceFileViewMgr.LoopOnSelectedSteps method, and the SequenceFileViewMgr.GetCommand method to launch executions in an application without a visible window.

Parent topic:

User Interface Application Styles

Related concepts:

- Single Window Applications
- ExecutionView Manager
- SequenceFileView Manager

<!--NI_TOPIC bundle=teststand path=normal-sequences.html language=enus -->
## TOPIC 00633: Normal Sequences

- bundle_id: `teststand`
- source_path: `normal-sequences.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/normal-sequences.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: A normal sequence is any sequence other than a callback or an entry point. In process model files, use normal sequences as Utility subsequences that entry points or callbacks call. When you select Normal from the Type ring control on the Model tab of the Sequence Properties dialog box, the Model tab

### Normal Sequences

A normal sequence is any sequence other than a callback or an entry point. In process model files, use normal sequences as Utility subsequences that entry points or callbacks call. When you select Normal from the Type ring control on the Model tab of the Sequence Properties dialog box, the Model tab does not include any other options.

Parent topic:

Modifying Process Model Sequence Files

Related concepts:

- Process Model Architecture

<!--NI_TOPIC bundle=teststand path=normalization-numeric-values-pass-to-enumer.html language=enus -->
## TOPIC 00634: Normalization of Numeric Values Passed to Enumeration Parameter Values

- bundle_id: `teststand`
- source_path: `normalization-numeric-values-pass-to-enumer.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/normalization-numeric-values-pass-to-enumer.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: When you use TestStand to specify a VI for a LabVIEW step code module and the VI contains enumeration parameters but you pass a numeric value that is outside the range of valid enumeration values to an enumeration parameter, LabVIEW modifies the value to be within the valid range before executing th

### Normalization of Numeric Values Passed to
 Enumeration Parameter Values

When you use TestStand to specify a VI for a LabVIEW step code module and the VI contains
 enumeration parameters but you pass a numeric value that is outside the range of valid
 enumeration values to an enumeration parameter, LabVIEW modifies the value to be within
 the valid range before executing the VI, as the following table describes:

| TestStand Version | LabVIEW Version That Executes VI | Way in Which Numeric Value is Out of Range | LabVIEW Behavior |
| --- | --- | --- | --- |
| 2012 | 2012 or later | Numeric value is negative. | LabVIEW uses the first enumerated value in the list (0). |
| Numeric value is greater than the last enumerated value in the list. | LabVIEW uses the last enumerated value in the list. |  |  |
| Earlier than 2012 | Any numeric value. | LabVIEW does not modify any numeric value. If a numeric value is out of range, the behavior is undefined. |  |
| Earlier than 2012 | Any | Any numeric value. |  |

Parent topic:

LabVIEW Adapter

Related concepts:

- Code Modules

<!--NI_TOPIC bundle=teststand path=numeric-value-connections.html language=enus -->
## TOPIC 00635: Numeric Value Connections

- bundle_id: `teststand`
- source_path: `numeric-value-connections.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/numeric-value-connections.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: A numeric value connection graphically displays a numeric value that illustrates the status of the application. For example, you can use the ExecutionView Manager control to connect a numeric value to a StatusBar pane so that the StatusBar pane displays a progress bar that indicates the percentage o

### Numeric Value Connections

A numeric value connection graphically displays a numeric value that illustrates the status of the application. For example, you can use the ExecutionView Manager control to connect a numeric value to a StatusBar pane so that the StatusBar pane displays a progress bar that indicates the percentage of progress made in the current execution.

The NumericSources enumeration defines the set of values to which you can connect.

Call the ExecutionViewMgr.ConnectNumeric method to connect a numeric source to a StatusBar pane. Call the ExecutionViewMgr.GetNumericValue method to obtain a numeric value without connecting the value to a control.

Parent topic:

Information Source Connections

Related concepts:

- ExecutionView Manager

<!--NI_TOPIC bundle=teststand path=object-references-in-msvc.html language=enus -->
## TOPIC 00636: Object References in Microsoft Visual C++/#import

- bundle_id: `teststand`
- source_path: `object-references-in-msvc.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/object-references-in-msvc.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The #import directive generates a set of smart pointer C++ classes that simplify the task of maintaining references to objects. The constructors, destructors, and assignment operators in these classes automatically add references to the object and release the object as needed. Each TestStand API cla

### Object References in Microsoft Visual C++/#import

The #import directive generates a set of smart pointer C++ classes that simplify the task of maintaining references to objects. The constructors, destructors, and assignment operators in these classes automatically add references to the object and release the object as needed. Each TestStand API class includes a pointer class you can use to maintain a reference to a TestStand object. These pointer classes are named by appending the Ptr suffix to the name of the API class to which the pointer refers. For example, the following code declares a pointer to a TestStand Step object:

TS::StepPtr step;

All of the generated C++ classes use these pointer classes as method parameters and return values.

If a test function or method in a class receives a dispatch pointer as a parameter, declare a local variable of the correct pointer class and assign to it the dispatch pointer. The construction of the pointer adds a reference to the dispatch pointer and the destructor releases it, as shown in the following example:

void Example (LPDISPATCH sequenceContextDisp)

{

TS::SequenceContextPtr context = sequenceContextDisp;

TS::PropertyObjectPtr contextAsPropObj = context->AsPropertyObject();

}

Parent topic:

Programming with the TestStand API in Microsoft Visual C++

<!--NI_TOPIC bundle=teststand path=object-references.html language=enus -->
## TOPIC 00637: Object References

- bundle_id: `teststand`
- source_path: `object-references.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/object-references.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: All ActiveX objects maintain reference counts. Each object keeps track of the number of other objects that reference it so the object can determine when to free the resources it uses. Typically, you do not have to take any specific actions to maintain a reference count. However, you must help mainta

### Object References

All ActiveX objects maintain reference counts. Each object keeps track of the number of other objects that reference it so the object can determine when to free the resources it uses. Typically, you do not have to take any specific actions to maintain a reference count. However, you must help maintain the reference count if you call a method or property that returns an object or if you store a reference to an object in a global variable for use after the test module completes.

Parent topic:

ActiveX Automation Server Concepts

Related concepts:

- Adding and Releasing References

<!--NI_TOPIC bundle=teststand path=object-relationships.html language=enus -->
## TOPIC 00638: Object Relationships

- bundle_id: `teststand`
- source_path: `object-relationships.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/object-relationships.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Engine class is the only class in the core TestStand API for which you can create an object directly. The Engine class defines methods for creating objects for the other classes. In some cases, you can obtain objects for one class from another class. For example, you can obtain a Step object fro

### Object Relationships

The Engine class is the only class in the core TestStand API for which you can create an object directly. The Engine class defines methods for creating objects for the other classes. In some cases, you can obtain objects for one class from another class. For example, you can obtain a Step object from the Sequence object that contains the step.

Parent topic:

TestStand API Concepts

<!--NI_TOPIC bundle=teststand path=objects-classes-methods-properties-and-contro.html language=enus -->
## TOPIC 00639: Objects, Classes, Methods, Properties, and Controls

- bundle_id: `teststand`
- source_path: `objects-classes-methods-properties-and-contro.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/objects-classes-methods-properties-and-contro.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The interface for an ActiveX Automation server includes the following components: Object—A programmable software component that represents an instance of a class. You interact with the object using the methods, properties, and events the class defines. Class—Similar to a data type definition, except

### Objects, Classes, Methods, Properties, and Controls

The interface for an ActiveX Automation server includes the following components:

- Object —A programmable software component that represents an instance of a class. You interact with the object using the methods, properties, and events the class defines.
- Class —Similar to a data type definition, except that a class applies to objects rather than variables. A class defines a list of methods and properties you can use with respect to the objects you create as instances of the class. For some classes, you can create objects directly. For other classes, you can obtain objects only by calling a method or property on an existing object of another class.
- Method —Performs an operation or function on an object.
- Property —A value that stores and maintains a setting or attribute of an object.
- Control —A visible or invisible ActiveX component you use on user interface windows.

Parent topic:

ActiveX Automation Server Concepts

<!--NI_TOPIC bundle=teststand path=obtaining-a-different-interface-for-teststand.html language=enus -->
## TOPIC 00640: Obtaining a Different Interface for TestStand Objects in LabVIEW

- bundle_id: `teststand`
- source_path: `obtaining-a-different-interface-for-teststand.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/obtaining-a-different-interface-for-teststand.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: In some cases, you might need to obtain a different interface for a TestStand object than the current interface. In ActiveX/COM terminology, this action is called a QueryInterface. For example, when you have a Module reference to a LabVIEWModule object and need to access the LabVIEWModule interface

### Obtaining a Different Interface for TestStand Objects in LabVIEW

In some cases, you might need to obtain a different interface for a TestStand object than the current interface. In ActiveX/COM terminology, this action is called a QueryInterface.

For example, when you have a Module reference to a LabVIEWModule object and need to access the LabVIEWModule interface instead, perform a QueryInterface on the Module object to obtain the LabVIEWModule interface. In LabVIEW, use the Variant To Data function with the reference to accomplish this task.

The block diagram in the following figure shows how to obtain the LabVIEWModule interface of a Module object to obtain the VIDescription property of the object. Notice that you must release the reference the Variant To Data function returns when you are finished with it.

[IMAGE alt='image' src='GUID-CC2E9915-F1FA-4869-BEE9-E622BB4314F0-a5.png']

#### Selecting an ActiveXServer Class

Complete the following steps to select an ActiveX Server class (type) for an Automation refnum control or constant.

1. Right-click the Automation control or constant and select Select ActiveX Class»Browse to launch the Select Object From Type Library dialog box.
2. Select the appropriate ActiveX Server from the Type Library list control.
3. Confirm that the Show Creatable Objects Only option is not selected.
4. Select the required ActiveX Server Class in the Object control.
5. Click OK to close the Select Object From Type Library dialog box.

For example, the LabVIEWModule class is defined in the NI TestStand <version> Adapter API <version> Version 1.0 Server. To select the LabVIEWModule class, select NI TestStand <version> Adapter API <version> Version 1.0 as the ActiveX server, and then select LabVIEWModule as the required ActiveX Server Class in the Object control.

Parent topic:

Programming with the TestStand API in LabVIEW

<!--NI_TOPIC bundle=teststand path=odbc-data-source-administrator-dialog-box.html language=enus -->
## TOPIC 00641: ODBC Data Source Administrator Dialog Box

- bundle_id: `teststand`
- source_path: `odbc-data-source-administrator-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/odbc-data-source-administrator-dialog-box.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Navigate to the standard Microsoft Windows Control Panel facility for administrative tools and select Data Sources (ODBC) to launch the ODBC Data Source Administrator dialog box. The ODBC Data Source Administrator dialog box lists all the registered ODBC data sources. The dialog box contains tabs fo

### ODBC Data Source Administrator Dialog Box

Navigate to the standard Microsoft Windows Control Panel facility for administrative tools and select Data Sources (ODBC) to launch the ODBC Data Source Administrator dialog box.

The ODBC Data Source Administrator dialog box lists all the registered ODBC data sources. The dialog box contains tabs for defining data sources and viewing available drivers.

- User DSN —Defines data sources visible only to you.
- System DSN —Defines data sources for all users.
- File DSN —Specifies that the ODBC Administrator stores the data source definitions in a directory you specify.
- Drivers Tab —Displays the available drivers for the system.

For the User DSN and System DSN tabs, the ODBC Administrator stores the data source definitions in the Windows system registry. Click Add or Configure on these tabs to launch a driver-specific dialog box, in which you can configure a new or an existing data source. The system then saves the configuration for the data source in the registry or as a file.

Click Help to launch the Microsoft online help for any tab in the ODBC Data Source Administrator dialog box.

Parent topic:

Connecting to a Database with the ODBC Administrator

<!--NI_TOPIC bundle=teststand path=on-the-fly-database-logging.html language=enus -->
## TOPIC 00642: On-the-Fly Database Logging

- bundle_id: `teststand`
- source_path: `on-the-fly-database-logging.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/on-the-fly-database-logging.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: When you enable the Use On-The-Fly Logging option on the Logging Options tab of the Database Options dialog box, the process models progressively log result data concurrently with the execution instead of waiting until UUT testing completes. The database logging plug-in uses the Model Plugin – OnThe

### On-the-Fly Database Logging

When you enable the Use On-The-Fly Logging option on the Logging Options tab of the Database Options dialog box, the process models progressively log result data concurrently with the execution instead of waiting until UUT testing completes. The database logging plug-in uses the Model Plugin – OnTheFly Step Results entry point sequence to process the step results. The final data TestStand logs is almost identical to the data the process model generates at the end of execution.

When you use this option, you can use the Database Viewer application to view the data in the database tables while the sequence executes. Enable the Discard Results or Disable Results when not Required by Model option in the Model Options dialog box to conserve memory by discarding step results after TestStand logs each result.

When you use on-the-fly database logging with a schema that uses a stored procedure or command statements that do not use the INSERT command, you cannot define constraints for foreign keys in step result statements that reference primary keys in UUT results. Defining constraints for these types of foreign keys generates an error because the on-the-fly database logger cannot execute the statement to create the record that contains the primary key before executing the statement to create the record that contains the foreign key.

The Generic Recordset (NI) and TS 2.x–4.0 Generic Recordset (NI) database schemas use the TOP 1 clause in the command text for all statements, as the following example shows, to improve performance when logging results to a database by preventing the recordset from accessing existing records in the database:

SELECT TOP 1 * FROM <TABLE NAME>

This performance improvement is useful when you enable the Use On-The-Fly Logging option for database files larger than 500 MB.

Parent topic:

Database Logging

Related concepts:

- Model Plugin – OnTheFly Step Results
- Default TestStand Table Schemas

<!--NI_TOPIC bundle=teststand path=on-the-fly-report-generation.html language=enus -->
## TOPIC 00643: On-the-Fly Report Generation

- bundle_id: `teststand`
- source_path: `on-the-fly-report-generation.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/on-the-fly-report-generation.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: When you enable the On-The-Fly Reporting option on the Contents tab of the Report Options dialog box, the process models progressively generate the report concurrently with the execution instead of waiting until UUT testing completes. The final report TestStand generates is identical to the report t

### On-the-Fly Report Generation

When you enable the On-The-Fly Reporting option on the Contents tab of the Report Options dialog box, the process models progressively generate the report concurrently with the execution instead of waiting until UUT testing completes. The final report TestStand generates is identical to the report the process model generates at the end of execution. You can use on-the-fly reporting for all report formats.

When you use on-the-fly reporting, you can click the Report pane of the Execution window to view the report during the execution. When the Report pane is the active view of the Execution window while a sequence executes, the report periodically updates as TestStand processes step results.

In addition to generating the report concurrently with execution, on-the-fly reporting periodically persists the current report to a temporary file based on the persistence interval the process model sequences specify. TestStand deletes the temporary file and saves the final report to a file at the end of a UUT loop execution.

#### Configuring On-the-Fly Report Options

When you enable the Only Display Latest Results option on the Contents tab of the Report Options dialog box, on-the-fly reporting periodically purges internal data structures while testing the UUT. As a result, the report TestStand displays on the Report pane of the Execution window shows only the results for the steps on-the-fly reporting has not yet purged. The persisted temporary and final report files contain all the step results. TestStand always purges internal data structures when UUT testing completes.

Note

Use the Discard Results or Disable Results when not Required By Model option in the Model Options dialog box to conserve memory by discarding step results after TestStand records each result.

Note

#### On-the-Fly Report Server

In addition, you can use the on-the-fly report server in conjunction with objects of the ReportSection class to create a custom on-the-fly report in any format or layout, including custom report formats. The ProcessOTFStepResults sequence of the reportgen_atml.seq, reportgen_xml.seq, reportgen_html.seq, and reportgen_text.seq report generation sequence files, located in the <TestStand>\Components\Models\TestStandModels directory, calls the on-the-fly report server.

Parent topic:

Generating and Customizing TestStand Reports

Related concepts:

- Process Model Architecture
- Choosing the Appropriate Report Generation Strategy
- TestStand Directory Structure

<!--NI_TOPIC bundle=teststand path=options-for-stepping-out-of-a-microsoft-visua.html language=enus -->
## TOPIC 00644: Options for Stepping Out of a Microsoft Visual Studio Assembly

- bundle_id: `teststand`
- source_path: `options-for-stepping-out-of-a-microsoft-visua.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/options-for-stepping-out-of-a-microsoft-visua.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following table lists the options for stepping out of a Microsoft Visual Studio assembly. 12 Options for Stepping Out of a Microsoft Visual Studio Assembly Visual Studio Command for Stepping Out Result in TestStand Step Out Function executes. When you use this command on the last function in the

### Options for Stepping Out of a Microsoft Visual Studio Assembly

The following table lists the options for stepping out of a Microsoft Visual Studio assembly.

| Visual Studio Command for Stepping Out | Result in TestStand |
| --- | --- |
| Step Out | Function executes. When you use this command on the last function in the call stack, TestStand suspends execution on the next step in the sequence. |
| Step Into or Step Over | When you use this command on the last executable statement of the function, TestStand suspends execution on the next step in the sequence. |
| Continue | TestStand does not suspend execution when the function call returns |

Refer to the Visual Studio documentation for more information about debugging managed code in an external process.

Parent topic:

Debugging .NET Assemblies

Related concepts:

- Debugging .NET Assemblies

<!--NI_TOPIC bundle=teststand path=order-of-entry-point-execution-at-run-time.html language=enus -->
## TOPIC 00645: Order of Entry Point Execution at Run Time

- bundle_id: `teststand`
- source_path: `order-of-entry-point-execution-at-run-time.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/order-of-entry-point-execution-at-run-time.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The process model calls each plug-in entry point in the order in which the plug-in instance appears in the corresponding configuration file. For result processors, the order in which the plug-in instances appear in the Result Processing dialog box determines the order in which the instances appear i

### Order of Entry Point Execution at Run Time

The process model calls each plug-in entry point in the order in which the plug-in instance appears in the corresponding configuration file. For result processors, the order in which the plug-in instances appear in the Result Processing dialog box determines the order in which the instances appear in the corresponding configuration file.

When multiple configuration files define plug-in instances, the values of the <NI_ModelPluginConfiguration>.RunOrder property in each configuration file define the order in which the process model invokes the group of plug-in instances from each file. By default, the Addons.cfg configuration file contains a <NI_ModelPluginConfiguration>.RunOrder value of -10.0, which causes add-on plug-ins to run before result processor plug-ins in the ResultProcessing.cfg file, which uses the default value of 0.0 for the <NI_ModelPluginConfiguration>.RunOrder property.

Additionally, if the values of the <NI_ModelPlugin>.Base.RunOrder properties of plug-in instances found in each configuration file are not equal, the process models invoke plug-in instances in ascending order based on the value of the <NI_ModelPlugin>.Base.RunOrder property of the plug-in instance found in the corresponding configuration file.

Note

<NI_ModelPlugin>.Base.RunOrder

Base.RunOrder

ModelPluginComponentDescription.Default.Base.RunOrder

TestStand always calls the UUT Done and Batch Done entry points of plug-in instances configured to use a new thread before calling UUT Done and Batch Done entry points of plug-in instances not configured to use a new thread. TestStand uses the same guidelines to determine the calling order for UUT Done and Batch Done entry points of plug-in instances configured to use a new thread as well as the calling order for UUT Done and Batch Done entry points of plug-in instances not configured to use a new thread.

Parent topic:

Model Plug-in Entry Points

<!--NI_TOPIC bundle=teststand path=organizing-labview-based-teststand-systems.html language=enus -->
## TOPIC 00646: Organizing LabVIEW-Based TestStand Systems

- bundle_id: `teststand`
- source_path: `organizing-labview-based-teststand-systems.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/organizing-labview-based-teststand-systems.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: A LabVIEW-based TestStand system can utilize TestStand workspaces, sequence files, and sequences to organize and represent the architecture of the application in LabVIEW. TestStand sequences contain steps, which can call LabVIEW VI code modules. Depending on the architecture of the test system, thes

### Organizing LabVIEW-Based TestStand Systems

A LabVIEW-based TestStand system can utilize TestStand workspaces, sequence files, and sequences to organize and represent the architecture of the application in LabVIEW. TestStand sequences contain steps, which can call LabVIEW VI code modules. Depending on the architecture of the test system, these code module VIs can call utility VIs, which can in turn utilize VIs stored in vi.lib or other LabVIEW libraries.

TestStand supports the following LabVIEW organizational options for the VIs you create and use in a test system:

- LabVIEW projects ( .lvproj )
- LabVIEW packed project libraries ( .lvlibp )
- Stand-alone LabVIEW VIs ( .vi )
- LabVIEW libraries ( .llb )
- LabVIEW project libraries ( .lvlib )
- LabVIEW-built shared libraries ( .dll )

Consider the test system requirements when choosing an organizational approach for LabVIEW code module VIs and utility VIs. The approaches vary in impact on the maintenance, performance, robustness, and deployment of the test system.

Note

- NI recommends using a single version of LabVIEW to compile all the VIs for a test system.
- NI does not recommend using LabVIEW-generated .NET assemblies to develop a TestStand
 system.

Parent topic:

Effectively Using LabVIEW with TestStand

Related concepts:

- Programming with the TestStand API in LabVIEW
- Organizing Test Program Files with LabVIEW Projects
- Organizing Test Program Files with LabVIEW Packed Project Libraries
- Organizing Test Program Files with Stand-alone VIs
- Organizing Test Program Files with LabVIEW Libraries
- Organizing Test Program Files with LabVIEW Project Libraries
- Organizing Test Program Files with LabVIEW-Built Shared Libraries
- Calling LabVIEW VIs
- Getting Started with TestStand

<!--NI_TOPIC bundle=teststand path=organizing-test-program-files-lv-libraries.html language=enus -->
## TOPIC 00647: Organizing Test Program Files with LabVIEW Project Libraries

- bundle_id: `teststand`
- source_path: `organizing-test-program-files-lv-libraries.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/organizing-test-program-files-lv-libraries.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: LabVIEW project libraries (.lvlib) are collections of VIs, type definitions, shared variables, palette menu files, and other files, including other project libraries. In TestStand, you can call public VIs in a project library, but you cannot call private VIs. To call a VI in a project library, you m

### Organizing Test Program Files with LabVIEW Project Libraries

LabVIEW project libraries (.lvlib) are collections of VIs, type definitions, shared variables, palette menu files, and other files, including other project libraries.

In TestStand, you can call public VIs in a project library, but you cannot call private VIs. To call a VI in a project library, you must specify the path to the VI file. TestStand does not use qualified paths that include the project file name and VI name.

Using project libraries in TestStand includes the following advantages:

- You can avoid potential VI name collisions when you deploy multiple test systems to the same test station computer. Project libraries change the filenames of VIs they reference to a compound, qualified name that includes the project library filename so you can reference VIs with the same filename from different project libraries. For example, the Library.lvlib project library changes the filename of the test.vi it references to Library.lvlib:test.vi , and the LibraryTwo.lvlib project library changes the filename of the test.vi it references to LibraryTwo.lvlib:test.vi . When you reference a project library that another project library contains, the qualified name concatenates the parent project library name with the name of the project library it contains, such as ParentLibrary.lvlib:ReferencedLibrary.lvlib .
- You can enforce security settings, such as limiting public access to certain files or limiting editing permission for a collection of files to prevent calling support VIs the project library references or calling VIs the project library does not reference.
- You can organize files into a single hierarchy of items. When you reference a VI a project library references, LabVIEW also automatically references all the VIs in the project library. Similarly, when you load a VI a project library references, LabVIEW automatically loads the project library as well.

The project library must exist on the computer for TestStand or LabVIEW to execute a VI the project library references. If the project library is not available, LabVIEW breaks the VI to prevent it from running.

Refer to the LabVIEW Help for more information about project libraries.

Parent topic:

Organizing LabVIEW-Based TestStand Systems

Related concepts:

- Deploying Multiple Test Systems to the Same Test Station
- Deploying TestStand Systems
- Programming with the TestStand API in LabVIEW

<!--NI_TOPIC bundle=teststand path=organizing-test-program-files-lv-projects.html language=enus -->
## TOPIC 00648: Organizing Test Program Files with LabVIEW Projects

- bundle_id: `teststand`
- source_path: `organizing-test-program-files-lv-projects.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/organizing-test-program-files-lv-projects.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: LabVIEW projects are files that reference VIs, files necessary for those VIs to run properly, and supplemental files such as documentation or related links. You can use folders and libraries to group items in a hierarchy. LabVIEW projects provide a system-level view of the files an application requi

### Organizing Test Program Files with LabVIEW Projects

LabVIEW projects are files that reference VIs, files necessary for those VIs to run properly, and supplemental files such as documentation or related links. You can use folders and libraries to group items in a hierarchy.

LabVIEW projects provide a system-level view of the files an application requires. The LabVIEW Project Explorer helps developers easily find and organize files from within the development environment and provides functionality that addresses the challenges of managing and developing large LabVIEW applications.

Use LabVIEW projects to group together LabVIEW files and other files and to integrate with source code control providers. You can also use LabVIEW projects to prevent cross-linking by qualifying common VI names using project libraries for name spacing and to help you with large application development.

Refer to the LabVIEW Help for more information about LabVIEW projects.

#### Choosing When to Execute Code Modules Specified in a LabVIEW Project

Configure TestStand steps to execute code modules specified in a LabVIEW project if the test system meets any of the following conditions:

- The TestStand system includes multiple VIs with the same name
- Code module VIs use LabVIEW conditional disable structures that depend on custom symbols defined in a LabVIEW project
- Code module VIs use NI-DAQmx tasks, channels, and scales defined in a LabVIEW project
- LabVIEW FPGA Host VIs that use LabVIEW FPGA targets are defined under the My Computer target in a LabVIEW project

Parent topic:

Organizing LabVIEW-Based TestStand Systems

Related concepts:

- Calling LabVIEW VIs
- Getting Started with TestStand
- Programming with the TestStand API in LabVIEW

<!--NI_TOPIC bundle=teststand path=organizing-test-program-files-with-labview-bu.html language=enus -->
## TOPIC 00649: Organizing Test Program Files with LabVIEW-Built Shared Libraries

- bundle_id: `teststand`
- source_path: `organizing-test-program-files-with-labview-bu.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/organizing-test-program-files-with-labview-bu.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use the LabVIEW Application Builder to build a shared library, or DLL. TestStand can execute exported VIs in LabVIEW DLLs built using different versions of LabVIEW. Use the C/C++ DLL Adapter to configure a step to call one of the exported functions in the DLL. To create a DLL in LabVIEW, you

### Organizing Test Program Files with LabVIEW-Built Shared Libraries

You can use the LabVIEW Application Builder to build a shared library, or DLL. TestStand can execute exported VIs in LabVIEW DLLs built using different versions of LabVIEW. Use the C/C++ DLL Adapter to configure a step to call one of the exported functions in the DLL.

To create a DLL in LabVIEW, you must first create a LabVIEW project that refers to the VIs you want to export and then create a build specification. You must configure the type of each parameter for all exported VIs.

Refer to LabVIEW documentation for information about debugging LabVIEW DLLs.

Note

- To ensure that Microsoft Windows messages are handled during the execution of a LabVIEW DLL you
 build for use with TestStand, NI recommends that you disable the
 Delay operating system messages in shared library 
 option on the Advanced Page of the Shared Library Properties dialog box in
 the LabVIEW Professional Development System.
- LabVIEW does not support exporting every LabVIEW data type. You might have difficulty passing data to certain LabVIEW types from TestStand. You must also manually add parameter information when configuring the LabVIEW-generated DLL in TestStand.
- When you deploy a test system, you must install the version of the LabVIEW RTE that corresponds to the version of LabVIEW used to create the DLL on any computer that uses the DLL. You can include the appropriate RTE installer in an installer you build with the TestStand Deployment Utility.
- TestStand supports—but NI does not recommend—distributing DLLs with the same name that steps in
 a sequence file call.

Parent topic:

Organizing LabVIEW-Based TestStand Systems

Related concepts:

- Organizing Test Program Files with LabVIEW-Built Shared Libraries
- Organizing Test Program Files with LabVIEW Projects
- Deploying TestStand Systems
- Processing LabVIEW Code Modules for Deployment

<!--NI_TOPIC bundle=teststand path=organizing-test-program-files-with-labview-li.html language=enus -->
## TOPIC 00650: Organizing Test Program Files with LabVIEW Libraries

- bundle_id: `teststand`
- source_path: `organizing-test-program-files-with-labview-li.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/organizing-test-program-files-with-labview-li.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: LabVIEW libraries (LLBs) are files that group several VIs together in a .llb file. LLBs reduce the number of files on disk, making it easier to deploy a test system. Consider the following when working with LLBs: An installer cannot install a single VI to an LLB. You must overwrite the entire LLB to

### Organizing Test Program Files with LabVIEW Libraries

LabVIEW libraries (LLBs) are files that group several VIs together in a .llb file. LLBs reduce the number of files on disk, making it easier to deploy a test system.

Consider the following when working with LLBs:

- An installer cannot install a single VI to an LLB. You must overwrite the entire LLB to install additional files.
- When you make changes to an LLB, it is difficult to determine which files have changed.
- LLBs do not have hierarchy information, so all VIs are stored at the same level. However, for display purposes, you can mark VIs called from TestStand as top-level VIs in the LLB.
- LLBs do not have namespaces and cannot prevent name collisions.
- All VIs in an LLB are visible, so you cannot hide the names of private VIs and subVIs.
- LLBs do not have version resources, so multiple installers upgrading a single LLB might have unintended consequences.
- Removing files from an LLB and creating a patch deployment might break sequence files or VIs in the existing deployed test system. If you remove files from an LLB, verify that previous deployments do not require the files. Do not manually remove unchanged code module VIs from the patch deployable image. Instead, rely on the TestStand Deployment Utility to remove files that do not differ from the previous deployable image.

If you want to build LLBs of test VIs when creating a deployment of a test system, you must build the LLB and update the TestStand sequences that call test VIs to reference the LLB because the deployment utility does not create LLBs of top-level VIs. However, if the test VIs are already organized in LLBs, the deployment utility maintains the LLB structure.

NI recommends that you save VIs as individual files organized in directories instead of using
 LLBs, especially if multiple developers are working on the same project.

Parent topic:

Organizing LabVIEW-Based TestStand Systems

Related concepts:

- Deploying TestStand Systems
- Patching Deployments
- Programming with the TestStand API in LabVIEW
- Patching LabVIEW VIs
- Processing LabVIEW Code Modules for Deployment

<!--NI_TOPIC bundle=teststand path=organizing-test-program-files-with-labview-pa.html language=enus -->
## TOPIC 00651: Organizing Test Program Files with LabVIEW Packed Project Libraries

- bundle_id: `teststand`
- source_path: `organizing-test-program-files-with-labview-pa.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/organizing-test-program-files-with-labview-pa.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: LabVIEW packed project libraries are LabVIEW project libraries that package multiple LabVIEW-related files and dependencies into a single non-editable file (.lvlibp) that you can call from other VIs. In TestStand, you can directly open and call VIs exported from a LabVIEW packed project library, or

### Organizing Test Program Files with LabVIEW Packed Project Libraries

LabVIEW packed project libraries are LabVIEW project libraries that package multiple LabVIEW-related files and dependencies into a single non-editable file (.lvlibp) that you can call from other VIs.

In TestStand, you can directly open and call VIs exported from a LabVIEW packed project library, or you can access the VIs through a LabVIEW project.

#### Building Packed Project Libraries with LabVIEW

Although the TestStand Deployment Utility can build packed project libraries that contain code modules the test system uses, using LabVIEW to build packed project libraries offers the following advantages:

- You can create multiple packed project libraries and control which VIs you export from each packed project library. You can also group VIs into packed project libraries depending on functionality.
- You can more quickly create a deployment that contains pre-built packed project
 libraries because the deployment utility does not need to rebuild the packed project
 libraries.
- You can rebuild existing packed project libraries to include new exported VIs and maintain compatibility of the previously exported VIs.

Refer to the LabVIEW Help for more information about LabVIEW packed project libraries.

Parent topic:

Organizing LabVIEW-Based TestStand Systems

Related concepts:

- Organizing Test Program Files with LabVIEW Project Libraries
- Organizing Test Program Files with LabVIEW Projects
- Deploying TestStand Systems
- Calling LabVIEW VIs
- Getting Started with TestStand
- Programming with the TestStand API in LabVIEW

<!--NI_TOPIC bundle=teststand path=organizing-test-program-files-with-stand-alon.html language=enus -->
## TOPIC 00652: Organizing Test Program Files with Stand-alone VIs

- bundle_id: `teststand`
- source_path: `organizing-test-program-files-with-stand-alon.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/organizing-test-program-files-with-stand-alon.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: A stand-alone VI is a file on disk that is not part of a LabVIEW library and is not called in the context of a project. Code module VIs use functions that manipulate input from the user interface or other sources and display that information or move it to other files or computers.

### Organizing Test Program Files with Stand-alone VIs

A stand-alone VI is a file on disk that is not part of a LabVIEW library and is not called in the context of a project.

Code module VIs use functions that manipulate input from the user interface or other sources and display that information or move it to other files or computers.

Parent topic:

Organizing LabVIEW-Based TestStand Systems

Related concepts:

- Organizing Test Program Files with LabVIEW Libraries
- Organizing Test Program Files with LabVIEW Projects
- Calling LabVIEW VIs
- Getting Started with TestStand
- Programming with the TestStand API in LabVIEW

<!--NI_TOPIC bundle=teststand path=out-of-process-com-servers-in-32-bit-teststan.html language=enus -->
## TOPIC 00653: Out-of-Process COM Servers in 32-bit TestStand and 64-bit TestStand

- bundle_id: `teststand`
- source_path: `out-of-process-com-servers-in-32-bit-teststan.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/out-of-process-com-servers-in-32-bit-teststan.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Because COM inherently supports inter-process communication across architectures, only a single instance of an out-of-process COM server might be necessary to support the same adapter step in 32-bit TestStand and in 64-bit TestStand. By default, if only one version of the server is registered, TestS

### Out-of-Process COM Servers in 32-bit TestStand and 64-bit TestStand

Because COM inherently supports inter-process communication across architectures, only a single instance of an out-of-process COM server might be necessary to support the same adapter step in 32-bit TestStand and in 64-bit TestStand. By default, if only one version of the server is registered, TestStand automatically locates that version of the server. If a 32-bit version and a 64-bit version of the server are registered, 32-bit TestStand locates the 32-bit server, and 64-bit TestStand locates the 64-bit server. You can change this default behavior in the registry on a per-server basis to require matching bitness, but changing this behavior affects all clients of the server on the computer, not just TestStand. For out-of-process COM servers, TestStand relies on the launch behavior specified for the server in the Microsoft Windows Registry. There is no way within TestStand to control which bitness of an out-of-process COM server TestStand uses. The particular functionality and performance requirements of the server and the application determine any migration tasks you must perform.

Although out-of-process servers do not have to match the bitness of TestStand, problems might arise depending on the design and expected behavior of the server when the server bitness does not match the bitness of TestStand. For example, if a 64-bit version of the server is expected to be registered but is missing, TestStand automatically locates the 32-bit server by default. In this scenario, the step might function correctly during basic testing but might have poor performance, run out of memory unexpectedly, or exhibit other subtle differences in behavior.

Another issue to consider is that when you register a 32-bit version and a 64-bit version of a singleton server, the server is actually a doubleton composed of two separate singleton servers. 64-bit clients share a single instance of the 64-bit server, and 32-bit clients share a separate single instance of the 32-bit server. The design and functionality of the server determine the issues you must resolve.

Use bitness-conditional code with the ActiveX/COM Adapter when the 32-bit version and the 64-bit version of COM interfaces differ.

Parent topic:

ActiveX/COM Code Module Support for 64-bit TestStand

Related concepts:

- Bitness-Conditional Code for DLLs with Different 32-bit Interfaces and 64-bit Interfaces

<!--NI_TOPIC bundle=teststand path=override-sfps-runtime-error.html language=enus -->
## TOPIC 00654: Overriding Engine Callbacks - SequenceFilePostStepRuntimeError

- bundle_id: `teststand`
- source_path: `override-sfps-runtime-error.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/override-sfps-runtime-error.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Purpose This example demonstrates how to handle run-time errors using the SequenceFilePostStepRuntimeError Engine callback sequence. Example File Location <TestStand Public>\Examples\Fundamentals\Overriding Engine Callbacks\Overriding SequenceFilePostStepRuntimeError Callback.seq Highlighted Feature

### Overriding Engine Callbacks - SequenceFilePostStepRuntimeError

#### Purpose

This example demonstrates how to handle run-time errors using the SequenceFilePostStepRuntimeError Engine callback sequence.

#### Example File
 Location

<TestStand
 Public>\Examples\Fundamentals\Overriding Engine
 Callbacks\Overriding SequenceFilePostStepRuntimeError
 Callback.seq

#### Highlighted Features

Callbacks

#### Major API

Step.CancelStepCallback

#### Prerequisites

None

#### How to Use This Example

Complete the following steps to review the sequences and steps in this example.

1. On the Sequences pane, select the MainSequence . The MainSequence contains two Numeric Limit Test steps and one Sequence Call step.
2. On the Sequences pane, select the SubSequence sequence. The SubSequence sequence contains Numeric Limit Test steps, two of which are designed to cause run-time errors in the following ways to demonstrate how TestStand behaves when a run-time error occurs:
  - One test generates an error only the first time
  - One test generates an error every time
3. On the Sequences pane, select the SequenceFilePostStepRuntimeError callback. The first step, which uses the ActiveX/COM Adapter, sets the Step.CancelStepCallback property to True to suppress any other failure callbacks for a failed step.
4. On the Steps pane, select the Choose Action step.
5. On the Step Settings pane, click the Text and Buttons tab. The Message Expression control specifies an expression that provides information about the step that caused the run-time error, and the step specifies buttons so you can choose to retry the test, ignore the error, continue to the Cleanup step group, or terminate the execution. The Select step that follows the Choose Action step specifies the following cases that correspond to the buttons you can click in the message popup that the Choose Action step creates:
  - Case 1 ignores the error and changes the next step index to retry the step that caused the error
  - Case 2 ignores the error and specifies the step status as Error Suppressed .
  - Case 3 sets the RunState.Caller.Runstate.ErrorReported flag to True to prevent TestStand from displaying a run-time error dialog box because has already reported the error
  - Case 4 sets the RunState.Caller.Runstate.ErrorReported flag to True to prevent TestStand from displaying a run-time error dialog box because has already reported the error and then terminates the execution

Complete the following steps to run the example.

1. Select Execute»Single Pass to run the sequence.
2. TestStand launches the Error dialog box for the first step that causes a run-time error. Click the Retry button to run the step again. The step passes on the second attempt.
3. TestStand launches the Error dialog box for the next step that causes a run-time error. Click the Ignore Error button to continue executing the sequence.
4. When execution completes, review the report on the Report pane. The status of the first attempt of the Generate a run-time error only the first time step is Error, Retrying Step because you clicked the Retry button after the step caused a run-time error once. The status of the Generate a run-time error every time step is Error Suppressed because you clicked the Ignore Error button when the step caused a run-time error.

Parent topic:

Examples for Fundamentals

Related concepts:

- TestStand Directory Structure
- Callback Sequences
- Step Groups

<!--NI_TOPIC bundle=teststand path=overriding-engine-callbacks-sequencefileposts.html language=enus -->
## TOPIC 00655: Overriding Engine Callbacks - SequenceFilePostStepFailure

- bundle_id: `teststand`
- source_path: `overriding-engine-callbacks-sequencefileposts.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/overriding-engine-callbacks-sequencefileposts.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Purpose This example demonstrates how to retry or force failed steps to pass using the SequenceFilePostStepFailure Engine callback sequence. You can force steps in the MainSequence or in a subsequence. Example File Location <TestStand Public>\Examples\Fundamentals\Overriding Engine Callbacks\Overrid

### Overriding Engine Callbacks - SequenceFilePostStepFailure

#### Purpose

This example demonstrates how to retry or force failed steps to pass using the SequenceFilePostStepFailure Engine callback sequence. You can force steps in the MainSequence or in a subsequence.

#### Example File
 Location

<TestStand
 Public>\Examples\Fundamentals\Overriding Engine
 Callbacks\Overriding SequenceFilePostStepFailure
 Callback.seq

#### Highlighted Features

Callbacks

#### Major API

Step.CancelStepCallback

#### Prerequisites

None

#### How to Use This Example

Complete the following steps to review the sequences and steps in this example.

1. On the Sequences pane, select the MainSequence . The MainSequence contains two Numeric Limit Test steps and one Sequence Call step.
2. On the Sequences pane, select the SubSequence sequence. The SubSequence sequence contains Numeric Limit Test steps, three of which are designed to fail in the following ways to demonstrate how TestStand behaves when a step fails:
  - One test fails only the first time
  - One test fails every time
  - One test fails every time but does not cause the sequence to fail
3. On the Sequences pane, select the SequenceFilePostStepFailure callback. The first step, which uses the ActiveX/COM Adapter, sets the Step.CancelStepCallback property to True to suppress any other failure callbacks for a failed step, and a series of Statement steps collects information about the step failure.
4. On the Steps pane, select the Choose Action step.
5. On the Step Settings pane, click the Text and Buttons tab. The Message Expression control specifies an expression that provides information about the step failure, and the step specifies buttons so you can choose to retry the test, force the test to pass, continue the execution, or terminate the execution. The Select step that follows the Choose Action step specifies the following cases that correspond to the buttons you can click in the message popup that the Choose Action step creates:
  - Case 1 changes the next step index to retry the step that failed
  - Case 2 forces the failed step to pass
  - Case 3 continues the sequence without taking any other action
  - Case 4 terminates the execution

Complete the following steps to run the example.

1. Select Execute»Single Pass to run the sequence.
2. TestStand launches the Step Failed dialog box for the first step that fails. Click the Retry button to run the failed step again. The step passes on the second attempt.
3. TestStand launches the Step Failed dialog box for the next step that fails. Click the Force to Pass button to force the failed step to pass.
4. TestStand launches the Step Failed dialog box for the next step that fails. Click the Continue button to allow the step to fail without causing the sequence fail.
5. When execution completes, review the report on the Report pane. The status of the first attempt of the Fail only the first time step is Failed, Retrying Step because you clicked the Retry button after the step failed once. The status of the Fail every time step is Passed because you clicked the Force to Pass button when the step failed.

Parent topic:

Examples for Fundamentals

Related concepts:

- TestStand Directory Structure
- Callback Sequences

<!--NI_TOPIC bundle=teststand path=overriding-prebatch-and-postbatch-model-callb.html language=enus -->
## TOPIC 00656: Overriding PreBatch and PostBatch Model Callbacks

- bundle_id: `teststand`
- source_path: `overriding-prebatch-and-postbatch-model-callb.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/overriding-prebatch-and-postbatch-model-callb.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Purpose This example demonstrates how to override the PreBatch callback to customize the batch and test socket serial number entry and how to override the PostBatch callback to customize the batch and test socket status report. Example File Location <TestStand Public>\Examples\Modifying Process Mode

### Overriding PreBatch and PostBatch Model Callbacks

#### Purpose

This example demonstrates how to override the PreBatch callback to customize the batch and test socket serial number entry and how to override the PostBatch callback to customize the batch and test socket status report.

#### Example File
 Location

<TestStand
 Public>\Examples\Modifying Process Models\Overriding Model
 Callbacks - Batch Model\Overriding PreBatch and PostBatch
 Callbacks.seq

#### Highlighted Features

Batch process model

#### Major API

None

#### Prerequisites

None

#### How to Use This Example

This example overrides the PreBatch and PostBatch callbacks, but the OverrideSerialNumForBatchModel2.seq example sequence file overrides the PreUUT and PostUUT callbacks.

The advantages of overriding the PreBatch and PostBatch callbacks, and not the PreUUT and PostUUT callbacks, include the following:

- You can enable or disable test sockets.
- You can access data for test sockets you have disabled, terminated, or aborted.

The disadvantage is that you must set or retrieve information for each test socket in a loop instead of in parallel.

Parent topic:

Examples for Modifying Process Models

Related concepts:

- Model Callbacks in the Batch Process Model
- TestStand Directory Structure
- Batch Process Model
- Overriding PreUUT and PostUUT Batch Model Callbacks

<!--NI_TOPIC bundle=teststand path=overriding-preuut-and-postuut-batch-model-cal.html language=enus -->
## TOPIC 00657: Overriding PreUUT and PostUUT Batch Model Callbacks

- bundle_id: `teststand`
- source_path: `overriding-preuut-and-postuut-batch-model-cal.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/overriding-preuut-and-postuut-batch-model-cal.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Purpose This example demonstrates how to override the PreUUT callback to customize the batch and test socket serial number entry and how to override the PostUUT callback to customize the batch and test socket status report. Example File Location <TestStand Public>\Examples\Modifying Process Models\O

### Overriding PreUUT and PostUUT Batch Model Callbacks

#### Purpose

This example demonstrates how to override the PreUUT callback to customize the batch and test socket serial number entry and how to override the PostUUT callback to customize the batch and test socket status report.

#### Example File
 Location

<TestStand
 Public>\Examples\Modifying Process Models\Overriding Model
 Callbacks - Batch Model\Overriding PreUUT and PostUUT
 Callbacks.seq

#### Highlighted Features

Batch process model

#### Major API

None

#### Prerequisites

None

#### How to Use This Example

This example overrides the PreUUT and PostUUT callbacks, but the OverrideSerialNumForBatchModel1.seq example sequence file overrides the PreBatch and PostBatch callbacks.

The advantage of overriding the PreUUT and PostUUT callbacks, and not the PreBatch and PostBatch callbacks, is that TestStand executes the PreUUT and PostUUT callbacks in parallel for each test socket, and on some computers this might improve performance and allow for simpler code in the callbacks.

The disadvantages include the following:

- You can disable test sockets only in the PreBatch callback. You cannot disable test sockets in the PreUUT callback.
- Test sockets you have disabled, terminated, or aborted never call the PreUUT and PostUUT callbacks. If you want to record information for the test sockets, you must do so in the PreBatch and PostBatch callbacks.

Parent topic:

Examples for Modifying Process Models

Related concepts:

- Model Callbacks in the Batch Process Model
- TestStand Directory Structure
- Batch Process Model
- Overriding PreBatch and PostBatch Model Callbacks

<!--NI_TOPIC bundle=teststand path=overriding-preuut-and-postuut-parallel-model.html language=enus -->
## TOPIC 00658: Overriding PreUUT and PostUUT Parallel Model Callbacks

- bundle_id: `teststand`
- source_path: `overriding-preuut-and-postuut-parallel-model.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/overriding-preuut-and-postuut-parallel-model.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Purpose This example demonstrates how to override the default UUT Information dialog box in the Parallel process model, override the ModelOptions callback to disable the default dialog box, and override the PreUUT callback to define a new method for obtaining the serial number. Optionally, you can o

### Overriding PreUUT and PostUUT Parallel Model Callbacks

#### Purpose

This example demonstrates how to override the default UUT Information dialog box in the Parallel process model, override the ModelOptions callback to disable the default dialog box, and override the PreUUT callback to define a new method for obtaining the serial number. Optionally, you can override the PostUUT callback to obtain the status of a test socket after it finishes a run.

#### Example File
 Location

<TestStand
 Public>\Examples\Modifying Process Models\Overriding Model
 Callbacks - Parallel Model\Overriding PreUUT and PostUUT
 Callbacks.seq

#### Highlighted Features

Parallel process model

#### Major API

None

#### Prerequisites

None

#### How to Use This Example

Complete the following steps to run this example.

1. Select Execute»Test UUTs to run the sequence. Each test socket in the parallel execution launches a UUT Information dialog box that prompts you to enter a serial number. The dialog boxes launch because the default UUT Information dialog box for the Parallel process model has been disabled.
2. Enter any serial number in each UUT Information dialog box and click OK .
3. Click OK when TestStand displays the results of each test.
4. Click Cancel in each UUT Information dialog box to stop executing each test socket. Each Execution window displays a report.
5. Select Window»Close Completed Executions to close all the Execution windows.

Complete the following steps to review the sequences and steps used in the example.

1. On the Sequences pane, select the ModelOptions callback sequence.
2. On the Steps pane, select the Change setting to not show dialog step, which is a Statement step.
3. On the Step Settings pane, click the Expression edit tab. The Expression control specifies an expression that disables the default UUT Information dialog box for the Parallel process model.
4. On the Sequences pane, select the PreUUT callback sequence. This sequence specifies two Action steps that use the C/C++ DLL Adapter and call a DLL that returns screen size information TestStand uses to determine where the new dialog boxes need to launch on the screen. The TestSocket Serial Num Message Popup step, which is a Message Popup step, requests the serial number for each test socket TestStand executes in parallel.

You can complete the following steps to re-enable the default UUT Information dialog box.

1. On the Sequences pane, select the ModelOptions callback sequence.
2. On the Step Settings pane for the Change setting to not show dialog step, click the Properties tab.
3. Click Run Options on the Properties tab to show the Run Options panel.
4. Select Skip from the Run Mode ring control.
5. Select Execute»Test UUTs to run the sequence. Click No when TestStand prompts you to save changes to the sequence file. The default UUT Information dialog box launches to prompt you to enter test socket serial numbers.
6. Close the sequence file and do not save any changes.

Parent topic:

Examples for Modifying Process Models

Related concepts:

- Model Callbacks in the Parallel Process Model
- TestStand Directory Structure
- Parallel Process Model
- Organizing Test Program Files with LabVIEW-Built Shared Libraries

<!--NI_TOPIC bundle=teststand path=overriding-preuut-model-callbacks.html language=enus -->
## TOPIC 00659: Overriding PreUUT Model Callbacks

- bundle_id: `teststand`
- source_path: `overriding-preuut-model-callbacks.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/overriding-preuut-model-callbacks.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Purpose This example demonstrates how to override the PreUUT Model callback sequence to simulate scanning a serial number and performing a database query. When you do not override the PreUUT callback, the default process model prompts you to manually enter a serial number. Example File Location <Tes

### Overriding PreUUT Model Callbacks

#### Purpose

This example demonstrates how to override the PreUUT Model callback sequence to simulate scanning a serial number and performing a database query. When you do not override the PreUUT callback, the default process model prompts you to manually enter a serial number.

#### Example File
 Location

<TestStand
 Public>\Examples\Modifying Process Models\Overriding Model
 Callbacks - Sequential Model\CVI\Overriding the PreUUT
 Callback.seq

#### Highlighted Features

Callbacks

#### Major API

None

#### Prerequisites

You must have the LabWindows/CVI Run-Time Engine installed and you must configure the LabWindows/CVI Adapter to execute steps in-process. If you want to use the Execute Steps in an External Instance of CVI option, you must have the LabWindows/CVI development environment installed.

#### How to Use This Example

Complete the following steps to review the sequences and steps in this example.

1. On the Sequences pane, select the MainSequence . The MainSequence contains four Numeric Limit Test steps.
2. Select Edit»Sequence File Callbacks to launch the Sequence File Callbacks dialog box, in which you can select a callback to override. For the PreUUT callback, the Present column specifies yes. Click OK to close the Sequence File Callbacks dialog box.
3. On the Sequences pane, select the PreUUT callback. The IdentifyUUT step, which uses the C/C++ DLL Adapter, calls a DLL to simulate scanning a serial number and performing a database query.
4. Select Execute»Test UUTs to run the sequence. The PreUUT callback executes instead of the PreUUT callback in the process model, so TestStand does not launch the default UUT Information dialog box for you to manually enter a serial number.

You can click the Stop Testing button at any time to terminate the execution.

Parent topic:

Examples for Modifying Process Models

Related concepts:

- Model Callbacks in the Sequential Process Model
- Process Model Architecture
- TestStand Directory Structure
- Callback Sequences
- Organizing Test Program Files with LabVIEW-Built Shared Libraries

<!--NI_TOPIC bundle=teststand path=parallel-process-model.html language=enus -->
## TOPIC 00660: Parallel Process Model

- bundle_id: `teststand`
- source_path: `parallel-process-model.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/parallel-process-model.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Parallel process model, <TestStand>\Components\Models\TestStandModels\ParallelModel.seq, includes sequences for the following components: Main Execution entry pointsTest UUTsSingle Pass Hidden Execution entry pointsTest UUTs - Test Socket Entry PointSingle Pass - Test Socket Entry Point Configur

### Parallel Process Model

The Parallel process model,
 <TestStand>\Components\Models\TestStandModels\ParallelModel.seq,
 includes sequences for the following components:

- Main Execution entry points
  - Test UUTs
  - Single Pass
- Hidden Execution entry points
  - Test UUTs - Test Socket Entry Point
  - Single Pass - Test Socket Entry Point
- Configuration entry points
- Plug-in utility sequences
- Model callbacks
- Engine callbacks

Use the Parallel model to control multiple independent test sockets. With the Parallel model, you can start and stop testing on any test socket at any time. For example, if you have five test sockets for testing radios, you can load a new radio into an open test socket while the other test sockets continue testing other radios.

When you select the Single Pass Execution entry point, the Parallel model launches a separate execution for each test socket without prompting for UUT serial numbers.

Parent topic:

Process Model Architecture

Related concepts:

- TestStand Directory Structure
- Main Execution Entry Points in the Parallel Process Model
- Test UUTs Execution Entry Point in the Parallel Process Model
- Single Pass Execution Entry Point in the Parallel Process Model
- Hidden Execution Entry Points in the Parallel Process Model
- Test UUTs – Test Socket Entry Point Execution Entry Point in the Parallel Process Model
- Single Pass - Test Socket Execution Entry Point in the Parallel Process Model
- Configuration Entry Points
- Plug-in Utility Sequences
- Model Callbacks in the Parallel Process Model
- Engine Callback
- Overriding PreUUT and PostUUT Parallel Model Callbacks

<!--NI_TOPIC bundle=teststand path=parallel-test-strategies-demo.html language=enus -->
## TOPIC 00661: Parallel Test Strategies Demo

- bundle_id: `teststand`
- source_path: `parallel-test-strategies-demo.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/parallel-test-strategies-demo.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Purpose This example demonstrates how you can use built-in parallel testing features to improve test throughput. You can use the parallel or batch process models to test multiple units in parallel on a single test station. TestStand provides a set of synchronization steps to coordinate parallel and

### Parallel Test Strategies Demo

#### Purpose

This example demonstrates how you can use built-in parallel testing features to improve test throughput. You can use the parallel or batch process models to test multiple units in parallel on a single test station. TestStand provides a set of synchronization steps to coordinate parallel and batch testing.

You can use the Auto Schedule step type to further improve the performance of parallel tests by allowing TestStand to automatically reorder your test steps to better utilize hardware resources.

This example shows the effects of using these features and how they can improve the performance of your tests.

#### Example File
 Location

<TestStand
 Public>\Examples\Demos\Parallel Testing Strategies\Parallel
 Testing Strategies.seq

#### Highlighted Features

- Batch process model
- Auto Schedule step type

#### Major API

None

#### Prerequisites

None

#### How to Use This Example

To begin the demo, select Execute»Run MainSequence.

When the example starts, a new window appears to show the simulated test steps, the current instrument usage, and the total test time for each strategy so you can compare performance. The demo contains the following strategies:

- Sequential —In turn, each UUT performs a DMM test. Then, in turn, each UUT performs a Scope test.
- Parallel —In parallel, each UUT performs a DMM test and then a Scope test. A UUT locks each instrument it uses to ensure that it has exclusive use of the instrument.
- Auto-Scheduled —In parallel, each UUT performs a DMM test and then a Scope test. A UUT locks each instrument it uses to ensure that it has exclusive use of the instrument. The order in which the UUT performs the test varies depending on the availability of the instruments.
- Parallel with Additional DMM —In parallel, each UUT performs a DMM test using the first available DMM. Then, each UUT performs a Scope test. A UUT locks each instrument it uses to ensure that it has exclusive use of the instrument.
- Auto-Scheduled with Additional DMM —In parallel, each UUT performs a DMM test using the first available DMM. Then, each UUT performs a Scope test. A UUT locks each instrument it uses to ensure that it has exclusive use of the instrument. The order in which the UUT performs the tests varies depending on the availability of the instruments.

Note

Parent topic:

Examples for Demos

Related concepts:

- Parallel Process Model
- Batch Process Model
- TestStand Directory Structure

<!--NI_TOPIC bundle=teststand path=parsing-parameters-from-source-code.html language=enus -->
## TOPIC 00662: Parsing Parameters from Source Code

- bundle_id: `teststand`
- source_path: `parsing-parameters-from-source-code.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/parsing-parameters-from-source-code.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: When the C/C++ DLL Adapter parses the parameter list in the source code, it must interpret the parameter declarations. Each parameter must have a numeric, array, or object type, and the return value must have a numeric or void type. Some C parameter declarations can be ambiguous, as described in the

### Parsing Parameters from Source Code

When the C/C++ DLL Adapter parses the parameter list in the source code, it must interpret the parameter declarations. Each parameter must have a numeric, array, or object type, and the return value must have a numeric or void type. Some C parameter declarations can be ambiguous, as described in the following table. For example, char * and char [] can each represent either a NULL-terminated string or a fixed-size character array.

| C Data Type in Parameter Declaration in Source Code | Parameter Information on Module Tab |
| --- | --- |
| char * | Type:C String |
| char [] | Type: C String Buffer Number of Elements: -1 |
| char [nnn], where nnn is a numeric literal | Type: C String Buffer Number of Elements: nnn |
| wchar_t * | Type: Unicode String |
| wchar_t [] | Type: Unicode String Buffer Number of Elements: -1 |
| wchar_t [nnn], where nnn is a numeric literal | Type: Unicode String Buffer Number of Elements: nnn |
| int * | Type: Signed 32-bit integer Pass: Pointer to value |
| int [] | Type: Array Data Type: Signed 32-bit integer Number of Elements: -1 |
| int [nnn], where nnn is a numeric literal | Type: Array Data Type: Signed 32-bit integer Number of Elements: nnn |

Note

Parent topic:

C/C++ DLL Adapter

<!--NI_TOPIC bundle=teststand path=partial-project-libraries.html language=enus -->
## TOPIC 00663: Partial Project Libraries

- bundle_id: `teststand`
- source_path: `partial-project-libraries.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/partial-project-libraries.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: A partial project library is a copy of a project library that uses the same qualified name as the original project library but includes references to only a subset of the VIs the original project library references. When you attempt to redeploy VIs, the build in the TestStand Deployment Utility can

### Partial Project Libraries

A partial project library is a copy of a project library that uses the same qualified name as the original project library but includes references to only a subset of the VIs the original project library references.

When you attempt to redeploy VIs, the build in the TestStand Deployment Utility can fail when you attempt to include a partial project library and the original complete project library or when you attempt to include two copies of the same VI on the system. When you deploy custom LabVIEW-based step types to a development system and then attempt to include the step types in a new deployment, the build might fail.

#### Encountering Broken VIs with Partial Project Libraries

You might encounter broken VIs in partial project libraries in the following situations:

- Loading a VI that is part of a complete project library you load after loading a partial project library that does not contain the VI.For example, the complete project library <vi.lib>\Analysis\NI_AALBase.lvlib references <vi.lib>\Analysis\baseanly.llb\Mean.vi and <vi.lib>\Analysis\baseanly.llb\Median.vi . A deployment for a test system that requires only Mean.vi includes a partial project library named Image\NI_AALBase.lvlib that references only Image\Mean.vi . On a test station computer that includes the LabVIEW development system, the test system loads Image\Mean.vi , which in turn loads the partial project library Image\NI_AALBase.lvlib . If the test system loads <vi.lib>\Analysis\baseanly.llb\Median.vi after it loads Image\Mean.vi , LabVIEW tries to load the project library for Median.vi , locates the partial project library named NI_AALBase.lvlib in memory, and tries to use the partial project library as the project library for Median.vi . Because the partial project library in memory does not include a reference to Median.vi but shares the same name as the project library that does contain Median.vi , LabVIEW flags Median.vi as broken. Closing all VIs in memory unloads the partial project library Image\NI_AALBase.lvlib so you can reload Median.vi correctly because when LabVIEW loads <vi.lib>\Analysis\baseanly.llb\Median.vi , it loads <vi.lib>\Analysis\NI_AALBase.lvlib , which includes references to Median.vi . Loading Image\Mean.vi after you load <vi.lib>Analysis\baseanly.llb\Median.vi does not break Image\Mean.vi because <vi.lib>\Analysis\NI_AALBase.lvlib includes a reference to Mean.vi but cross-links <vi.lib>\Analysis\NI_AALBase.lvlib to reference Image\Mean.vi . You can avoid this issue by using packed project libraries that contain the VIs the test system requires. All files in a packed project library, including project libraries, use qualified names that begin with the name of the packed project library to avoid colliding with the names of files already in memory, such as partial project libraries.
- Building a LabVIEW user interface and enabling the Remove unused members of project libraries option on the Additional Exclusions page of the Shared Library Properties dialog box in LabVIEW. Launching the LabVIEW user interface loads the partial project libraries you create. If you configured the LabVIEW Adapter to use the LabVIEW Run-Time Engine (RTE) to run VIs and the version of the RTE matches the version of the RTE the user interface uses, LabVIEW returns broken VI errors when you execute a sequence file that includes a VI a project library references but the partial project library the user interface loaded does not include a reference to that VI. You can avoid this issue by disabling the Remove unused members of project libraries option and rebuilding the LabVIEW user interface.
- Loading multiple deployments that reference partial project libraries that have the same namespace but contain a different set of VIs. You can avoid this issue by building all VIs into packed project libraries with different names for each deployment to prevent name collisions among references to partial project libraries from different deployments. You can also call LabVIEW code modules in the context of different LabVIEW projects for each deployment because names of VIs and project libraries you call in the context of a project do not collide with full or partial project libraries loaded in a separate context.

Parent topic:

Preparing Source Components for Deployment

Related concepts:

- Organizing Test Program Files with LabVIEW Project Libraries
- Organizing Test Program Files with LabVIEW Packed Project Libraries
- Deploying VIs in LabVIEW Packed Project Libraries
- Troubleshooting LabVIEW Code Module Issues

<!--NI_TOPIC bundle=teststand path=partially-specifying-labview-clusters.html language=enus -->
## TOPIC 00664: Partially Specifying LabVIEW Clusters

- bundle_id: `teststand`
- source_path: `partially-specifying-labview-clusters.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/partially-specifying-labview-clusters.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: If you have a cluster with default values and you need to modify certain values on the cluster depending on an operation you want to perform, you can use partial clusters. In TestStand, you can specify whether to pass default values for individual elements of a cluster control that are recommended o

### Partially Specifying LabVIEW Clusters

If you have a cluster with default values and you need to modify certain values on the cluster depending on an operation you want to perform, you can use partial clusters.

In TestStand, you can specify whether to pass default values for individual elements of a cluster control that are recommended or optional. This behavior is referred to as partially specifying a cluster, or partial cluster passing.

To specify that you want to apply the default value to an element of a partial cluster, enable the Default option in the VI Parameter Table on the LabVIEW Module tab in the TestStand Sequence Editor or on the Module tab of the Edit LabVIEW VI Call dialog box in a TestStand User Interface.

Parent topic:

Special Considerations for Using LabVIEW with TestStand Systems

Related concepts:

- Reserving Loaded VIs for Execution
- Executing VIs with Separate Compiled Code

<!--NI_TOPIC bundle=teststand path=parts-of-a-teststand-application.html language=enus -->
## TOPIC 00665: Parts of a TestStand Application

- bundle_id: `teststand`
- source_path: `parts-of-a-teststand-application.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/parts-of-a-teststand-application.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following figure and corresponding descriptions illustrate how the major parts of a TestStand application interact. TestStand Sequence Editor—The TestStand Sequence Editor is a development environment in which you create, edit, execute, and debug sequences and the tests sequences call. Use the s

### Parts of a TestStand Application

The following figure and corresponding descriptions illustrate how the major parts of a TestStand
 application interact.

[IMAGE alt='image' src='GUID-C5E35507-B081-4272-8BCB-DF995810AA35-a5.svg']

- TestStand Sequence Editor—The TestStand Sequence Editor is a development environment in which
 you create, edit, execute, and debug sequences and the tests sequences call. Use
 the sequence editor to create and edit other components, such as step types and
 process models.
- TestStand User Interfaces—A TestStand User Interface is an application you deploy to a
 development system or a production station to provide a custom GUI for
 executing, debugging, or editing sequences. Simple user interfaces might only
 support running sequences, while more complex user interfaces or custom sequence
 editors might support editing, running, and debugging sequences.
- TestStand User Interface Controls—The user interfaces use the TestStand User Interface (UI)
 Controls, a collection of ActiveX controls for creating custom user interfaces
 and sequence editors in TestStand. These controls simplify common user interface
 tasks, such as displaying sequences and executions. You can use these controls
 in any programming environment that can host ActiveX controls.
- TestStand Engine—The TestStand Engine is a set of DLLs that exports an ActiveX Automation API.
 The TestStand Sequence Editor and UI Controls use the TestStand API, which you
 can call from any programming environment that supports access to ActiveX
 servers, including code modules you write in LabVIEW and LabWindows/CVI.
- Module Adapters—The TestStand Engine uses module adapters to invoke code modules written in a
 variety of languages and application development environments (ADEs), including
 LabVIEW and LabWindows/CVI. Module adapters load and call code modules, pass
 parameters to code modules, and return values and status from code modules.
 TestStand handles core test management functionality, including the definition
 and execution of the overall testing process, user management, report
 generation, database logging, and more.
- TestStand Deployment Utility—After you develop, customize, and debug a TestStand system, you can
 deploy the system to multiple test stations. The TestStand Deployment Utility
 simplifies the complex process of deploying a TestStand system by automating
 many of the steps involved, including collecting sequence files, code modules,
 configuration data for instruments, and support files for the test system. You
 can also use the deployment utility to create a full deployment installer or a
 patch deployment installer.

Parent topic:

Fundamentals

Related concepts:

- Components of a TestStand System
- Step Types
- Process Models
- Creating Custom User Interfaces
- TestStand UI Controls
- TestStand ActiveX API Overview
- Module Adapters
- Building a Customized MSI-based Installer
- Patching Deployments
- Deploying TestStand Systems

<!--NI_TOPIC bundle=teststand path=pass-existing-ts-containter-lv.html language=enus -->
## TOPIC 00666: Passing Existing TestStand Container Variables to LabVIEW

- bundle_id: `teststand`
- source_path: `pass-existing-ts-containter-lv.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/pass-existing-ts-containter-lv.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `task`
- source_description: Instead of passing each element of a cluster parameter individually, you can create a TestStand custom data type that maps to an entire LabVIEW cluster. Click the Create/Update Custom Data Type button, located in the Type column of the VI Parameter Table on the LabVIEW Module tab, to launch the Crea

### Passing Existing TestStand Container Variables
 to LabVIEW

Instead of passing each element of a cluster parameter individually, you can create a
 TestStand custom data type that maps to an entire LabVIEW cluster.

1. Click the Create/Update Custom Data Type
 [IMAGE alt='image' src='GUID-FF48C662-3652-46C1-9B3F-60333F1E96A8-a5.gif']
 button, located in the Type column of the VI
 Parameter Table on the LabVIEW Module tab,
 to launch the Create/Update Custom Data Type from Cluster
 dialog box.
2. create a TestStand custom data type, such as a container, that matches an
 existing LabVIEW cluster.
3. Use the LabVIEW Cluster Passing tab on the Type
 Properties dialog box for the new custom data type to specify how
 TestStand maps subproperties to elements in a LabVIEW cluster.

This example illustrates how to create an InputData custom data type to map cluster
 data to TestStand, and create a ContainerData local variable that is an instance of
 the InputData custom data type.

The following figure shows the Create/Update Custom Data Type from
 Cluster dialog box for the InputData data type:

[IMAGE alt='image' src='GUID-EF1F8EC5-9B6E-43BC-9A90-E4E8B434A795-a5.png']

The following figure shows the custom InputData data type on the
 Types window:

[IMAGE alt='image' src='GUID-F970FAF6-D929-41D8-A826-D83625494AC1-a5.png']

The following figure shows a VI Parameter Table in which the
 Input Cluster parameter data passes to the ContainerData
 local variable:

[IMAGE alt='image' src='GUID-CC8AE3DF-75CE-4D81-99F6-1E28F477EC47-a5.png']

Note

Parent topic:

Module Adapters

Related concepts:

- Passing Structs to Code Modules - LabVIEW DLL

<!--NI_TOPIC bundle=teststand path=passing-an-instance-of-a-labview-class-object.html language=enus -->
## TOPIC 00667: Passing an Instance of a LabVIEW Class Object

- bundle_id: `teststand`
- source_path: `passing-an-instance-of-a-labview-class-object.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/passing-an-instance-of-a-labview-class-object.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: TestStand supports passing an instance of a LabVIEW Class data type, also called a LabVIEW class object, wired to and from the connector pane of a member VI. You can store LabVIEW class objects in TestStand object reference variables. When TestStand passes an object reference variable that contains

### Passing an Instance of a LabVIEW Class Object

TestStand supports passing an instance of a LabVIEW Class data type, also called a LabVIEW class object, wired to and from the connector pane of a member VI. You can store LabVIEW class objects in TestStand object reference variables.

When TestStand passes an object reference variable that contains a LabVIEW class object to a code module, the class object is always passed by value. To ensure that changes made to a LabVIEW class object persist in a code module, you must pass the class object as an output from the code module and store the output in the TestStand object reference variable. The object reference variable will contain a new instance of the class object with the updated data.

#### Class Object Lifetime

The lifetime of the LabVIEW class object is the lifetime of the TestStand object reference variable that holds the LabVIEW class object. If the VI that creates the LabVIEW class object is running in the context of a LabVIEW project, the lifetime of the LabVIEW class object is the lifetime of the LabVIEW project. When the object reference is released either by going out-of-scope or by obtaining a new value, the LabVIEW class object is also released. This behavior is different than other LabVIEW reference data types, such as an I/O reference.

The VI that creates the reference determines the lifetime of LabVIEW reference data types stored in TestStand. As long as the VI that created the LabVIEW reference is reserved, the LabVIEW reference is valid. This is not the case for LabVIEW class objects. A LabVIEW class object remains valid even after the VI that originally created it is unreserved or closed. If LabVIEW is restarted, trying to use a LabVIEW class object a previous LabVIEW instance obtained results in an error because the LabVIEW class object is not valid in the new instance of LabVIEW. In addition, if you try to use the LabVIEW class object after you close the LabVIEW project context in which the LabVIEW class object exists, an error occurs because closing a LabVIEW project context releases all LabVIEW class objects created in the project context.

#### Calling a Compatible Class Member VI

When you select the VI Call option from the Call Type ring control on the LabVIEW Module tab in the TestStand Sequence Editor or on the Module tab of the Edit LabVIEW VI Call dialog box in a TestStand User Interface, you are responsible for calling the appropriate member VI for the LabVIEW class object stored in TestStand.

Because you can pass any instance of a LabVIEW class object to any member VI from TestStand, no guarantee exists that the LabVIEW class object you passed to the member VI is compatible with the class object the member VI expects. To help LabVIEW check that the class object you passed from TestStand to the member VI is compatible with the class object the member VI expects, add the Preserve Run-Time Class function to the member VI. The Preserve Run-Time Class function returns an error if two class objects are incompatible. You can work around this limitation by creating top-level wrapper VIs that call dynamic dispatch member VIs of LabVIEW class objects when you select the VI Call option from the Call Type ring control to configure LabVIEW steps.

Note

- LabVIEW 2012 or later returns an error if you call a dynamically dispatched member VI that passes a derived class on the dynamic dispatch input terminals. For the dynamic dispatch to work properly, you must select the Class Member Call option from the Call Type ring control when you configure the step.
- TestStand supports executing a VI with a LabVIEW Class Reference parameter only when you execute the VI as part of a running sequence. Edit substeps and OnNewStep Custom substeps do not execute as part of sequence execution and cannot contain direct LabVIEW Class Reference parameters. If you need to pass a LabVIEW Class Reference, serialize the reference to a string parameter.

Parent topic:

Calling LabVIEW Class Member VIs from TestStand

Related concepts:

- Calling LabVIEW Class Member VIs from TestStand
- Organizing Test Program Files with LabVIEW Projects
- Calling VIs on Remote Computers

<!--NI_TOPIC bundle=teststand path=passing-clusters-to-code-modules-labview.html language=enus -->
## TOPIC 00668: Passing Clusters to Code Modules - LabVIEW

- bundle_id: `teststand`
- source_path: `passing-clusters-to-code-modules-labview.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/passing-clusters-to-code-modules-labview.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: This example demonstrates how to pass a TestStand container as a LabVIEW cluster to a LabVIEW VI. The container consists of several different data types. The VIs are compiled into a DLL and called as functions. Example File Location <TestStand Public>\Examples\Fundamentals\Passing Clusters to Code M

### Passing Clusters to Code Modules - LabVIEW

This example demonstrates how to pass a TestStand container as a LabVIEW cluster to a LabVIEW VI. The container consists of several different data types. The VIs are compiled into a DLL and called as functions.

#### Example File
 Location

<TestStand
 Public>\Examples\Fundamentals\Passing Clusters to Code
 Modules\Passing Clusters to Code Modules.seq

#### Highlighted Features

- Data types
- LabVIEW Adapter
- Local variables

#### Major API

None

#### Prerequisites

You do not need to have the LabVIEW development system installed to use this example, but you must have the LabVIEW development system installed if you want to review the source VIs.

#### How to Use This Example

The sequence specifies ContainerOut and ContainerIn container local variables, which you can review on the Variables pane. When the sequence runs, TestStand copies the values in the ContainerOut container to the individual local variables, and then copies the values again to the ContainerIn container. A VI handles both operations. Before you run the sequence, the ContainerOut container contains values, the ContainerIn container contains default values, and the individual local variables contain default values.

Complete the following steps to use this example.

1. Select Execute»Test UUTs to run the sequence.
2. Enter any serial number in the UUT Information dialog box and click OK . TestStand launches a Results for Unbundle dialog box that lists values loaded from the individual local variables, which specified default values before you executed the sequence.
3. Click OK in the Results for Unbundle dialog box. TestStand launches another Results for Unbundle dialog box that lists values loaded from the ContainerIn container, which specified default values before you executed the sequence.
4. Click OK when TestStand informs you that the sequence passed.
5. Click Stop in the UUT Information dialog box to end the execution.

You can review the two Message Popup steps in the sequence to verify that the appropriate sources are providing values. You can open VI1.vi and VI2.vi, located in the <TestStand Public>\Examples\Fundamentals\Passing Clusters to Code Modules directory, to see how the data is being copied. The VI1.vi uses an unbundle function to separate the values from the cluster, and the VI2.vi uses a bundle function to combine individual values into a single cluster.

To pass a TestStand container as a cluster to a VI, you must complete the following tasks:

- Define the container as a custom data type.
- Specify that objects of the data type can be passed as clusters.
- Ensure that the Cluster Item Label for each item in the data type matches the label of the LabVIEW cluster.

Complete the following steps to use the Types window to review the data type definition for a container.

1. In the Sequence File window, right-click the ContainerIn container on the Variables pane and select View»Type Definition from the context menu to launch the Types window.
2. Right-click the ClusterType data type and select Properties from the context menu to launch the Type Properties dialog box. Because the sequence is using a VI, you must enable cluster passing for the data type.
3. Click the Cluster Passing tab. Notice that the Allow Objects of This Type to be Passed as LabVIEW Clusters option is enabled. The Cluster Item Label option for each item matches the control labels in the VI.
4. Click OK to close the Type Properties dialog box.

Parent topic:

Examples for Fundamentals

Related concepts:

- TestStand Directory Structure
- Data Types
- Programming with the TestStand API in LabVIEW
- Sequence Local Variables

<!--NI_TOPIC bundle=teststand path=passing-data-between-teststand-and-python.html language=enus -->
## TOPIC 00669: Passing Data between TestStand and Python

- bundle_id: `teststand`
- source_path: `passing-data-between-teststand-and-python.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/passing-data-between-teststand-and-python.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Purpose This example demonstrates how you can pass TestStand data types to Python code modules. Example File Location <TestStand Public>Examples\Fundamentals\Python\Passing Data to Python\Passing Data to Python.seq Highlighted Features Mapping of Python and TestStand types Major API None Prerequisit

### Passing Data between TestStand and Python

#### Purpose

This example demonstrates how you can pass TestStand data types to Python code modules.

#### Example File
 Location

<TestStand
 Public>Examples\Fundamentals\Python\Passing Data to Python\Passing
 Data to Python.seq

#### Highlighted Features

- Mapping of Python and TestStand types

#### Major API

None

#### Prerequisites

Complete the following steps to install the required software and configure TestStand.

1. Install a supported version of the CPython interpreter and add it to your PATH variable.
2. Install the following libraries for the version of Python you installed:
  - Python for Win32 (pywin32) extensions
  - NumPy module (required for the NumPy Array example)
3. In the Python Adapter Configuration dialog box, update the Python version TestStand uses to execute Python code modules. Note To run the example for Enums, you must use Python 3.6 or higher.

#### How to Use This Example

Note

UUTInterface

UUTDatabase

Review the sequences and steps in this example. Select a subsequence in the Sequences pane to view steps in the subsequence.

| Sequence Call step in the MainSequence sequence | Subsequence the step calls | Purpose | Details |
| --- | --- | --- | --- |
| Working with Number | Number | Demonstrates passing numbers (integers and real) between TestStand and the Python module. | The subsequence has four sections that demonstrate adding, subtracting, multiplying, and dividing two TestStand numbers in the Python module. The four sections, delineated by Label steps, use 64-bit signed integers, 64-bit unsigned integers, 64-bit double-precision floating-point number, and float and integer together respectively. An Additional Results step completes each section to provide a summary of the results. |
| Working with Boolean | Boolean | Demonstrates passing Boolean data between TestStand and the Python module. | The subsequence demonstrates the inversion of the Boolean state of a TestStand variable in a Python module. An Additional Results step provides a summary of the results. |
| Working with String | String | Demonstrates passing string data between TestStand and the Python module. | The subsequence demonstrates the concatenation of two TestStand strings in a Python module. An Additional Results step provides a summary of the results. |
| Working with List | List | Demonstrates passing data between TestStand arrays and Python lists. | The subsequence demonstrates different operations, such as sorting and converting array data to string data, the Python module performs on TestStand array data. |
| Working with Tuple | Tuple | Demonstrates passing data between TestStand containers and Python tuples. | The subsequence retrieves a single element from a TestStand container using a Python module, sets a Python attribute as a tuple using a TestStand container, and inserts a Python tuple attribute into a TestStand container. |
| Working with PyObject | PyObject | Demonstrates passing data between TestStand object references and Python objects (PyObject). | The Setup step group contains the following steps: The Create UUTInterface Object step and the Initialize Database step obtain the references to the instances of the Python classes that are instantiated in the Python module. TestStand stores the references in TestStand object reference variables. Steps in the Main and Cleanup step groups will use these references.The Main step group contains the following steps:The Get UUT Model Type step, which is an action step, gets the value in the static attribute of the Python class UUTInterface.The Get UUT Serial Number step, which is an action step, gets the value of the attribute serialNumber from the object of the class UUTInterface, whose reference was obtained earlier.The Create UUT Record in Database step, which is an action step, calls the createRecord method in the class instance object of Python class UUTDatabase, whose reference was obtained earlier.The Powerup UUT step, which is an action step, calls the PowerupUUT method in the class instance object of the Python class UUTInterface whose reference was obtained earlier.The UUT String Value Test step validates the serial number of the UUTInterface object.The UUT Multiple Numeric Limit Test step validates the range of ports assigned to the UUTInterface object.The UUT Numeric Limit Test step validates the voltage read by the UUTInterface object.The UUT Pass/Fail Test step validates the test result of the UUTInterface object. |
| Working with Dispatch | Dispatch | Demonstrates passing TestStand objects and COM objects implementing IDispatch between TestStand and the Python module. | The Main step group contains the following Action steps: The Pass Sequence Context as Parameter step passes the SequenceContext object as a parameter to the Python code module.The Pass Engine as Parameter step passes the Engine property as a parameter to the Python code module.The Pass COM Object as Parameter step passes the COM object, whose reference is held in an object reference variable. The Pre-Expression of the step makes the object reference variable hold a reference to a PropertyObject, which is a COM object. When the step uses the object reference variable as a parameter, it passes the COM object held by the variable to the Python code module. |
| Working with Enum | Enum | Demonstrates passing enumerations between TestStand and the Python module. | The Main step group contains the following Action steps: The Pass Enum Color step passes the TestStand enum as a Python enum parameter with a type of Enum to the Python code module.The Pass Flag Measurement step passes the TestStand enum as a Python enum parameter with a type of Flag to the Python code module.The Pass IntEnum FileOpenOption step passes the TestStand enum as a Python enum parameter with a type of IntEnum to the Python code module.The Pass IntFlag FilePermission step passes the TestStand enum as a Python enum parameter with a type of IntFlag to the Python code module. |
| Working with NumPy Array | NumPy Array | Demonstrates passing data between a TestStand array and a Python NumPy array. | The subsequence demonstrates passing TestStand arrays to a Python module and performing a sorting operation using NumPy arrays. |

Complete the following steps to run the example.

1. Click Execute»Single Pass to run the sequence.
2. When execution completes, review the report.

Parent topic:

Examples for Fundamentals

Related concepts:

- TestStand Directory Structure

<!--NI_TOPIC bundle=teststand path=passing-structs-to-code-modules-c.html language=enus -->
## TOPIC 00670: Passing Structs to Code Modules - C

- bundle_id: `teststand`
- source_path: `passing-structs-to-code-modules-c.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/passing-structs-to-code-modules-c.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Purpose This example demonstrates how to pass a TestStand container as a C-style struct to a function in a DLL. This example uses functions to pass the struct by both reference and value. For a DLL function to change the value of a TestStand container, you must pass the reference of the container to

### Passing Structs to Code Modules - C

#### Purpose

This example demonstrates how to pass a TestStand container as a C-style struct to a function in a DLL. This example uses functions to pass the struct by both reference and value. For a DLL function to change the value of a TestStand container, you must pass the reference of the container to the function.

Note

#### Example File
 Location

<TestStand
 Public>\Examples\Fundamentals\Passing Structs to Code
 Modules\C\Passing Structs to Code Modules.seq

#### Highlighted Features

- Calling DLLs from TestStand
- C/C++ DLL Adapter
- Local variables
- Data types

#### Major API

None

#### Prerequisites

C compiler or DLL

#### How to Use This Example

The sequence specifies sPacked8Out and sPacked8In container local variables, which you can review on the Variables pane. The sequence uses a C DLL to copy the values from the sPacked8Out container to the sPacked8In container first by reference and then by value.

Complete the following steps to use this example.

1. Select Execute»Test UUTs to run the sequence.
2. Enter any serial number in the UUT Information dialog box and click OK . TestStand launches a Get Results dialog box that lists values loaded from the sPacked8In container, which specified default values before you executed the sequence.
3. Click OK in the Get Results dialog box. TestStand launches another Get Results dialog box that lists values loaded from the sPacked8In container. The GetStructByRef2 step specifies a pre-expression that specifies a value of 0 for each variable, and then the GetStructByRef2 step specifies new values for each variable.
4. Click OK when TestStand informs you that the sequence passed.
5. Click Stop in the UUT Information dialog box to end the execution.

You can review the two Message Popup steps in the sequence to verify that the sPacked8In container is displaying the variable values. The functions the DLL is using are available in StructTest.cpp, located in the <TestStand Public>\Examples\Fundamentals\Passing Structs to Code Modules\C directory.

To pass a TestStand container as a struct to a DLL, you must define the container as a custom data type, and you must specify that objects of the data type can be passed as structs.

Complete the following steps to use the Types window to review the data type definition for a container.

1. In the Sequence File window, right-click the sPacked8In container on the Variables pane and select View»Type Definition from the context menu to launch the Types window.
2. Right-click the AllDataTypesPacked8 data type and select Properties from the context menu to launch the Type Properties dialog box. Because the sequence is using a DLL, you must enable C struct passing for the data type.
3. Click the C Struct Passing tab. Notice that the Allow Objects of This Type to be Passed as Structs option is enabled. The Packing ring control specifies the 8 Byte Boundary option, which is the packing scheme the DLL uses.
4. Click OK to close the Type Properties dialog box.
5. In the Types window, expand the AllDataTypesPacked8 data type. You can right-click each property and select Properties from the context menu to launch the Type Properties dialog box for each property of the data type. You can review each property to see how it is configured.

Parent topic:

Passing Structs to Code Modules

Related concepts:

- TestStand Directory Structure
- Calling DLLs from TestStand
- Organizing Test Program Files with LabVIEW-Built Shared Libraries
- Sequence Local Variables
- Data Types

<!--NI_TOPIC bundle=teststand path=passing-structs-to-code-modules-labview-dll.html language=enus -->
## TOPIC 00671: Passing Structs to Code Modules - LabVIEW DLL

- bundle_id: `teststand`
- source_path: `passing-structs-to-code-modules-labview-dll.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/passing-structs-to-code-modules-labview-dll.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Purpose This example demonstrates how to pass a TestStand container as a LabVIEW cluster to a LabVIEW VI. The container consists of several different data types. The VIs are compiled into a DLL and called as functions. VIs always use a 1-byte packing scheme when passing clusters as parameters. Examp

### Passing Structs to Code Modules - LabVIEW DLL

#### Purpose

This example demonstrates how to pass a TestStand container as a LabVIEW cluster to a LabVIEW VI. The container consists of several different data types. The VIs are compiled into a DLL and called as functions.

Note

#### Example File
 Location

<TestStand
 Public>\Examples\Fundamentals\Passing Structs to Code
 Modules\LabVIEW DLL\Passing Structs to Code Modules.seq

#### Highlighted Features

- LabVIEW Adapter
- Local variables
- Data types

#### Major API

None

#### Prerequisites

You do not need to have the LabVIEW development system installed to use this example, but you must have the LabVIEW development system installed if you want to review the source VIs.

#### How to Use This Example

The sequence specifies StructOut and StructIn container local variables, which you can review on the Variables pane. When the sequence runs, TestStand copies the values in the StructOut container to the individual local variables, and then copies the values again to the StructIn container. The LabVIEW DLL handles both operations. Before you run the sequence, the StructOut container contains values, the StructIn container contains default values, the individual local variables contains default values.

Complete the following steps to use this example.

1. Select Execute»Test UUTs to run the sequence.
2. Enter any serial number in the UUT Information dialog box and click OK . TestStand launches a Results for Unbundle dialog box that lists values loaded from the individual local variables, which specified default values before you executed the sequence.
3. Click OK in the Results for Unbundle dialog box. TestStand launches another Results for Unbundle dialog box that lists values loaded from the StructIn container, which specified default values before you executed the sequence.
4. Click OK when TestStand informs you that the sequence passed.
5. Click Stop in the UUT Information dialog box to end the execution.

You can review the two Message Popup steps in the sequence to verify that the appropriate sources are providing values. You can open LV DLL 1.vi and LV DLL 2.vi, located in the <TestStand Public>\Examples\Fundamentals\Passing Structs to Code Modules\LabVIEW DLL directory, to see how the data is being copied. The LV DLL 1.vi uses an unbundle function to separate the values from the cluster, and the LV DLL 2.vi uses a bundle function to combine individual values into a single cluster. The sequence is using LVStructTest.dll, into which LV DLL 1.vi and LV DLL 2.vi were built.

To pass a TestStand container as a struct to a DLL, you must define the container as a custom data type, and you must specify that objects of the data type can be passed as structs.

Complete the following steps to use the Types window to review the data type definition for a container.

1. In the Sequence File window, right-click the StructIn container on the Variables pane and select View»Type Definition from the context menu to launch the Types window.
2. Right-click the DType1 data type and select Properties from the context menu to launch the Type Properties dialog box. Because the sequence is using a DLL, you must enable C struct passing for the data type.
3. Click the C Struct Passing tab. Notice that the Allow Objects of This Type to be Passed as Structs option is enabled. The Packing ring control specifies the 8 Byte Boundary option, which is the packing scheme the DLL uses.
4. Click OK to close the Type Properties dialog box.
5. In the Types window, expand the DType1 data type. You can right-click each property and select Properties from the context menu to launch the Type Properties dialog box for each property of the data type. You can review each property to see how it is configured.

Parent topic:

Passing Structs to Code Modules

Related concepts:

- TestStand Directory Structure
- Programming with the TestStand API in LabVIEW
- Sequence Local Variables
- Data Types

<!--NI_TOPIC bundle=teststand path=passing-structs-to-code-modules-labwindows-cv.html language=enus -->
## TOPIC 00672: Passing Structs to Code Modules - LabWindows/CVI

- bundle_id: `teststand`
- source_path: `passing-structs-to-code-modules-labwindows-cv.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/passing-structs-to-code-modules-labwindows-cv.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Purpose This example demonstrates how to pass a TestStand container as a C-style struct to a function in a LabWindows/CVI DLL. The container consists of several different data types. For a DLL function to change the value of a TestStand container, you must pass the reference of the container to the

### Passing Structs to Code Modules - LabWindows/CVI

#### Purpose

This example demonstrates how to pass a TestStand container as a C-style struct to a function in a LabWindows/CVI DLL. The container consists of several different data types. For a DLL function to change the value of a TestStand container, you must pass the reference of the container to the function.

Note

#### Example File
 Location

<TestStand
 Public>\Examples\Fundamentals\Passing Structs to Code
 Modules\CVI\Passing Structs to Code Modules.seq

#### Highlighted Features

- LabWindows/CVI Adapter
- Local variables
- Data types

#### Major API

None

#### Prerequisites

You must have the LabWindows/CVI Run-Time Engine installed and you must configure the LabWindows/CVI Adapter to execute steps in-process. If you want to use the Execute Steps in an External Instance of CVI option, you must have the LabWindows/CVI development environment installed.

#### How to Use This Example

The sequence specifies a CVIStruct container local variable, which you can review on the Variables pane. When the sequence runs, TestStand copies the values in the CVIStruct container to the individual local variables, and then assigns new values to the CVIStruct container. The LabWindows/CVI DLL handles both operations. Before you run the sequence, the CVIStruct container contains values, and the individual local variables contains default values.

Complete the following steps to use this example.

1. Select Execute»Test UUTs to run the sequence.
2. Enter any serial number in the UUT Information dialog box and click OK . TestStand launches a Results for Unpacking dialog box that lists values loaded from the CVIStruct container and assigned to the individual local variables.
3. Click OK in the Results for Unpacking dialog box. TestStand launches another Results dialog box that lists values modified and saved back to the CVIStruct container.
4. Click OK when TestStand informs you that the sequence passed.
5. Click Stop in the UUT Information dialog box to end the execution.

You can review the two Message Popup steps in the sequence to verify that the appropriate sources are providing values. You can open CVIStructTestSource.c, located in the <TestStand Public>\Examples\Fundamentals\Passing Structs to Code Modules\CVI directory, to see how the data is being copied. The PassStructAndUnpack method accesses the values in the CVIStruct container and assigns the values to the individual method parameters. The PassStructAndModify method assigns arbitrary values to the elements of the CVIStruct container by reference. These assignments modify the container in TestStand. The sequence is using CVIStructTest.dll, into which the PassStructAndUnpack and PassStructAndModify methods were built.

To pass a TestStand container as a struct to a DLL, you must define the container as a custom data type, and you must specify that objects of the data type can be passed as structs.

Complete the following steps to use the Types window to review the data type definition for a container.

1. In the Sequence File window, right-click the CVIStruct container on the Variables pane and select View»Type Definition from the context menu to launch the Types window.
2. Right-click the CVIStructExample data type and select Properties from the context menu to launch the Type Properties dialog box. Because the sequence is using a DLL, you must enable C struct passing for the data type.
3. Click the C Struct Passing tab. Notice that the Allow Objects of This Type to be Passed as Structs option is enabled. The Packing ring control specifies the Default Adapter Packing option, which is the packing scheme the LabWindows/CVI DLL uses.
4. Click OK to close the Type Properties dialog box.
5. In the Types window, expand the CVIStructExample data type. You can right-click each property and select Properties from the context menu to launch the Type Properties dialog box for each property of the data type. You can review each property to see how it is configured.

Parent topic:

Passing Structs to Code Modules

Related concepts:

- TestStand Directory Structure
- Programming with the TestStand API in LabWindows/CVI
- Sequence Local Variables
- Data Types

<!--NI_TOPIC bundle=teststand path=passing-structs-to-code-modules-net.html language=enus -->
## TOPIC 00673: Passing Structs to Code Modules - .NET

- bundle_id: `teststand`
- source_path: `passing-structs-to-code-modules-net.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/passing-structs-to-code-modules-net.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Purpose This example demonstrates how to pass a TestStand container as a .NET struct to a method in an assembly. This example uses functions to pass the struct by both reference and value. For a method in an assembly to change the value of a TestStand container, you must pass the reference of the co

### Passing Structs to Code Modules - .NET

#### Purpose

This example demonstrates how to pass a TestStand container as a .NET struct to a method in an assembly. This example uses functions to pass the struct by both reference and value. For a method in an assembly to change the value of a TestStand container, you must pass the reference of the container to the method.

#### Example File
 Location

<TestStand
 Public>\Examples\Fundamentals\Passing Structs to Code
 Modules\DotNet\Passing Structs to Code Modules.seq

#### Highlighted Features

- .NET Adapter
- Local variables
- Data types

#### Major API

None

#### Prerequisites

None

#### How to Use This Example

The sequence specifies StructOut and StructIn container local variables, which you can review on the Variables pane. The sequence uses a .NET method to copy the values from the StructOut container to the StructIn container first by reference and then by value.

Complete the following steps to use this example.

1. Select Execute»Test UUTs to run the sequence.
2. Enter any serial number in the UUT Information dialog box and click OK . TestStand launches a Get Results dialog box that lists values loaded from the StructIn container, which specified default values before you executed the sequence.
3. Click OK in the Get Results dialog box. TestStand launches another Get Results dialog box that lists values loaded from the StructIn container. The second GetStructByRef step specifies a pre-expression that specifies a value of 0 for each variable, and then the step specifies new values for each variable.
4. Click OK when TestStand informs you that the sequence passed.
5. Click Stop in the UUT Information dialog box to end the execution.

You can review the two Message Popup steps in the sequence to verify that the StructIn container is displaying the variable values. The methods the assembly is using are available in StructPassingDotNet.dll, located in the <TestStand Public>\Examples\Fundamentals\Passing Structs to Code Modules\DotNet directory.

Parent topic:

Passing Structs to Code Modules

Related concepts:

- TestStand Directory Structure
- Sequence Local Variables
- Data Types

<!--NI_TOPIC bundle=teststand path=passing-structs-to-code-modules.html language=enus -->
## TOPIC 00674: Passing Structs to Code Modules

- bundle_id: `teststand`
- source_path: `passing-structs-to-code-modules.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/passing-structs-to-code-modules.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The <TestStand Public>\Examples\Fundamentals\Passing Structs to Code Modules directory contains the following examples.

### Passing Structs to Code Modules

The <TestStand
 Public>\Examples\Fundamentals\Passing Structs to Code
 Modules directory contains the following examples.

- [Passing Structs to Code Modules - C](passing-structs-to-code-modules-c.html)
- [Passing Structs to Code Modules - LabWindows/CVI](passing-structs-to-code-modules-labwindows-cv.html)
- [Passing Structs to Code Modules - LabVIEW DLL](passing-structs-to-code-modules-labview-dll.html)
- [Passing Structs to Code Modules - .NET](passing-structs-to-code-modules-net.html)

Parent topic:

Examples for Fundamentals

Related concepts:

- TestStand Directory Structure

<!--NI_TOPIC bundle=teststand path=password-protecting-types.html language=enus -->
## TOPIC 00675: Password-Protecting Types

- bundle_id: `teststand`
- source_path: `password-protecting-types.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/password-protecting-types.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can password-protect types so that other TestStand users cannot modify the types in the TestStand Sequence Editor. In the Types window, select one or more types you want to password-protect, right-click, and select Password Protect from the context menu to launch the Password Protect Type Defini

### Password-Protecting Types

You can password-protect types so that other TestStand users cannot modify the types in the TestStand Sequence Editor.

In the Types window, select one or more types you want to password-protect, right-click, and select Password Protect from the context menu to launch the Password Protect Type Definitions dialog box, in which you can enable or disable password protection and change the password settings for the selected types. Enable the Password Protection option to enable password protection for the types, enter a password in the New Password control, and verify the password in the Re-enter Password control.

After you enable password protection for the types, the types remain unlocked so you can continue to edit the types. TestStand automatically locks password-protected types when TestStand first loads the types. For example, when you restart TestStand or close and reopen all the files that reference the password-protected types, TestStand locks the types. When you restart TestStand, TestStand locks all password-protected types. You can also select one or more password-protected types, right-click, and select Lock from the context menu to explicitly lock the types.

To unlock types, select the types you want to unlock, right-click, and select Unlock from the context menu to launch the Unlock Type Definitions dialog box, in which you can enter the correct password to unlock any selected types to which the password applies. TestStand ignores any selected types that are already unlocked or for which you have not enabled password protection. If the password you enter does not apply to all of the selected types, TestStand launches the Unlock Failed for Some Type Definitions dialog box, which gives you the option to return to the Unlock Type Definitions dialog box and enter another password to unlock the remaining types.

TestStand also launches the Unlock Type Definitions dialog box when you attempt to edit a locked type. You must enter the correct password to unlock the type before you can edit the type.

The locked or unlocked state of a type is not a saved state but is instead an in-memory state that indicates whether TestStand currently permits editing of the password-protected type.

Note

- TestStand supports password-protecting types to deter unauthorized users from editing the types
 in the sequence editor. However, any TestStand user can continue to
 programmatically edit a locked type by using the TestStand PropertyObject
 API. NI does not recommend password-protecting types as the only way of
 protecting intellectual property.
- If you lock at least one type in an INI-formatted sequence file, the entire contents of the sequence file become protected and unreadable.

Parent topic:

Type Concepts

<!--NI_TOPIC bundle=teststand path=patching-custom-sequence-editors.html language=enus -->
## TOPIC 00676: Patching Custom Sequence Editors

- bundle_id: `teststand`
- source_path: `patching-custom-sequence-editors.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/patching-custom-sequence-editors.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: If you deployed a test system you created with a custom sequence editor, depending on the type of changes you make, you might need to complete the following tasks: Create a patch deployment for the custom sequence editor itself on the development computer on which the custom sequence editor resides

### Patching Custom Sequence Editors

If you deployed a test system you created with a custom sequence editor, depending on the type of changes you make, you might need to complete the following tasks:

- Create a patch deployment for the custom sequence editor itself on the development computer on which the custom sequence editor resides and install the custom sequence editor patch on test station computers and any other development computers that require the custom sequence editor.
- Create a patch deployment for the updated test system you created with the custom sequence editor on the development computer on which the custom sequence editor resides and install the patch deployment on test station computers you want to update.

Parent topic:

Patching Deployments

<!--NI_TOPIC bundle=teststand path=patching-deployments.html language=enus -->
## TOPIC 00677: Patching Deployments

- bundle_id: `teststand`
- source_path: `patching-deployments.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/patching-deployments.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the TestStand Deployment Utility and follow the same process NI recommends for creating a full deployment to create or patch deployments and to build installers for patch deployments from an existing TestStand 2013 or later deployment specification file (.tsd). You cannot create a patch deployme

### Patching Deployments

Use the TestStand Deployment Utility and follow the same process NI recommends for creating a
 full deployment to create or patch deployments and to build installers for patch
 deployments from an existing TestStand 2013 or later deployment specification file
 (.tsd).

Note

- You cannot create a patch deployment from a TestStand 2012 or earlier .tsd file because the file does not include information required to create a patch. You can recreate a new full deployment in TestStand 2013 or later based on the TestStand 2012 or earlier .tsd file. You can then create patch deployments from the TestStand 2013 version of the .tsd file.
- Once you create the full deployment, you must save the .tsd file and the installer for the deployment to create a patch deployment and installer.

For MSI-based installer deployments, you can use patch deployments to update individual files, to
 add features and add components to features, to return files to a known state, and
 to include or exclude updates to NI drivers or the TestStand Runtime in a deployed
 test system. You can also exclude new or modified files from a patch deployment, but
 you cannot remove files from a deployed system on a test station computer. Patch
 deployments typically are smaller in size than full deployments and might take less
 time to create on the development computer.

For package based deployments, you can use patches to include newly required drivers and components, and include updates to components in the deployment. Package based deployments do not support updating individual files through a patch deployment.

You can create a full deployment at any point during the patch deployment creation process. When you change to full deployment mode, options in the deployment utility might change as well. In most cases, the full deployment will be larger and take longer to download and install than a patch deployment.

#### Creating Cumulative Patch Deployments

By default, the deployment utility creates a cumulative patch deployment that depends on the previous full deployment and includes all the files that differ from the full deployment version of the file. If you make changes to the test system after you create and install a patch deployment on a test station computer, you can create a new patch deployment to include all the changes since the previous full deployment, including the changes in the first patch deployment you created. The newer installer for the patch deployment uses the same upgrade code but a later version number than the previous installer for the patch deployment to upgrade, or replace, the previous patch deployment on the test station computer. You can also create to control the installation order of patch deployments and to include only files modified since a previous patch deployment. The following figure illustrates the process of creating replacement or dependency patch deployments that install serially.

[IMAGE alt='image' src='GUID-5AEC3E99-DB3B-454E-BD4F-3F900E8F6B35-a5.svg']

#### Creating Dependency Patch Deployments from Baseline Patch Deployments

You can create a new, dependency patch deployment from a previous, baseline patch deployment instead of from a full deployment to enforce the order in which to install patch deployments and to minimize the size of a new patch deployment by including only the files that differ from the previous baseline patch deployment version of the file, as shown in the previous figure. When you build an installer for a dependency patch deployment, the deployment utility adds installer launch conditions to enforce installing patch deployments in the correct order.

As the number of patch deployments you create grows, consider creating a new full deployment or a baseline patch deployment.

You must designate a patch deployment as a baseline patch deployment before you create a dependency patch deployment by clicking the Make Baseline Patch Deployment button on the Mode tab of the deployment utility. To create a dependency patch deployment, enable the Depend on previous Baseline Patch Deployment option on the Mode tab of the TestStand Deployment Utility.

Because the deployment utility discards old data after you create a deployment, TestStand supports only one baseline patch deployment at a time, and you can create a baseline patch deployment only from the most recent patch deployment you created. If you create another baseline patch deployment, you can no longer depend on the previous baseline patch deployment. Creating a new deployment also erases data of previous patch deployments that you do not designate as baseline patch deployments.

Parent topic:

Creating Deployments

Related concepts:

- Deployment Process Overview
- Including Modified Files in a Patch Deployment
- Adding New Files to a Patch Deployment
- Including Unmodified Files in a Patch Deployment
- Including NI Drivers or the TestStand Runtime in a Patch Deployment and Installer
- Excluding New or Modified Files from a Patch Deployment
- Upgrade Codes That Affect MSI-based Installer Behavior
- Creating Deployments
- Differences between Patch Deployments and Full Deployments
- Differences between Standard Mode and Manual Mode
- Creating Independent Patch Deployments
- Limitations of Patch Deployments

<!--NI_TOPIC bundle=teststand path=patching-labview-vis.html language=enus -->
## TOPIC 00678: Patching LabVIEW VIs

- bundle_id: `teststand`
- source_path: `patching-labview-vis.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/patching-labview-vis.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: When you create a patch deployment for a test system that uses LabVIEW VIs, consider the following issues: Removing files from an LLB, packed project library, project library, or a project and creating a patch deployment might negatively affect sequence files or VIs in the existing deployed test sys

### Patching LabVIEW VIs

When you create a patch deployment for a test system that uses LabVIEW VIs, consider the following issues:

- Removing files from an LLB, packed project library, project library, or a project and creating a patch deployment might negatively affect sequence files or VIs in the existing deployed test system. To ensure compatibility, only add—do not delete—files to an LLB, packed project library, project library or project.
- If you do remove files from an LLB, verify that previous deployments do not require the files. Do not manually remove unchanged code module VIs from the source files. Instead, rely on the TestStand Deployment Utility to remove files that do not differ from the previous deployable image.
- The deployment utility automatically processes VIs by updating links to subVIs and other dependencies to ensure the VIs can execute without errors when run using the LabVIEW Run-Time Engine on a test station computer without the LabVIEW development system installed. Do not use a patch deployment to replace a VI with an unprocessed VI because doing so can break the VI because of missing dependencies or broken links to dependencies. Instead, make the changes to the source VIs and rely on the deployment utility to process the files and include required files in the patch deployable image.

Note

Parent topic:

ADE-specific Issues for MSI-based Installer Patches

Related concepts:

- Patching Deployments
- Organizing Test Program Files with LabVIEW Libraries
- Updating and Patching VIs in LabVIEW Projects
- Updating and Patching VIs in LabVIEW Packed Project Libraries
- Updating and Patching Stand-alone VIs

<!--NI_TOPIC bundle=teststand path=patching-labwindows-cvi-dlls-and-executables.html language=enus -->
## TOPIC 00679: Patching LabWindows/CVI DLLs and Executables

- bundle_id: `teststand`
- source_path: `patching-labwindows-cvi-dlls-and-executables.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/patching-labwindows-cvi-dlls-and-executables.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: When you create a patch deployment for a test system that uses LabWindows/CVI DLLs or executables, consider the following issues: You must add new DLL or executable dependencies, such as adding a new .uir file for a new dialog box, to the TestStand workspace to ensure the TestStand Deployment Utilit

### Patching LabWindows/CVI DLLs and Executables

When you create a patch deployment for a test system that uses LabWindows/CVI DLLs or executables, consider the following issues:

- You must add new DLL or executable dependencies, such as adding a new .uir file for a new dialog box, to the TestStand workspace to ensure the TestStand Deployment Utility includes the files in the patch deployment.
- If you build a DLL or executable with a newer version of LabWindows/CVI, you might need to install the new version of the LabWindows/CVI Run-Time Engine on the test station computer.
- Update the file version when you update a DLL or executable so installers can use the file version number to determine whether to install the DLL or executable on the test station computer.

Note

Parent topic:

ADE-specific Issues for MSI-based Installer Patches

Related concepts:

- Patching Deployments
- Managing Versioned and Non-Versioned Files

<!--NI_TOPIC bundle=teststand path=patching-microsoft.html language=enus -->
## TOPIC 00680: Patching Microsoft .NET Assemblies

- bundle_id: `teststand`
- source_path: `patching-microsoft.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/patching-microsoft.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: When you create a patch deployment for a test system that uses Microsoft .NET assemblies, consider the following issues: You must manually add new dependent assemblies to the patch deployment image to ensure the TestStand Deployment Utility includes the files in the patch deployment. If you build a

### Patching Microsoft .NET Assemblies

When you create a patch deployment for a test system that uses Microsoft .NET assemblies, consider the following issues:

- You must manually add new dependent assemblies to the patch deployment image to ensure the TestStand Deployment Utility includes the files in the patch deployment.
- If you build a DLL or executable against a newer version of .NET, you must install the
 new version of .NET on the test station computer.
- Update the file version when you update an assembly so installers can use the file version number to determine whether to install the assembly on the test station computer.

Note

Parent topic:

ADE-specific Issues for MSI-based Installer Patches

Related concepts:

- Patching Deployments
- Managing Versioned and Non-Versioned Files

<!--NI_TOPIC bundle=teststand path=path.html language=enus -->
## TOPIC 00681: Path

- bundle_id: `teststand`
- source_path: `path.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/path.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the Path standard data type to include hyperlinks in supported versions of ATML, XML, and HTML reports. NI recommends that you use relative paths, which can be relative to the sequence file that contains them or one of the TestStand search directories. Relative paths allow TestStand to find file

### Path

Use the Path standard data type to include hyperlinks in supported versions of ATML, XML, and HTML reports.

NI recommends that you use relative paths, which can be relative to the sequence file that
 contains them or one of the TestStand search directories. Relative paths allow
 TestStand to find files even when you install or copy the files to a location on the
 another computer that is different from the location of the files on the original
 computer.

When you use the TestStand Deployment Utility to create a deployable image of a test system, the utility attempts to replace absolute file path references to code module files with relative file path references.

Note

Parent topic:

Using Standard Named Data Types

Related concepts:

- Including Hyperlinks in Reports
- Search Directories
- Deploying TestStand Systems
- Creating a Deployable Image
- Processing TestStand Sequence Files for Deployment
- Including Hyperlinks in a Report - TDMS File

<!--NI_TOPIC bundle=teststand path=pausing-executions-cvi.html language=enus -->
## TOPIC 00682: Pausing Executions with Running Code Modules - LabWindows/CVI

- bundle_id: `teststand`
- source_path: `pausing-executions-cvi.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/pausing-executions-cvi.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Purpose A TestStand execution cannot break until all threads within the execution have been suspended. If one or more threads in the execution is running a code module, the execution will not break until all code modules complete. This example demonstrates two methods you can use to override this be

### Pausing Executions with Running Code Modules - LabWindows/CVI

#### Purpose

A TestStand execution cannot break until all threads within the execution have been suspended. If one or more threads in the execution is running a code module, the execution will not break until all code modules complete.

This example demonstrates two methods you can use to override this behavior:

- The Thread.ExternallySuspended property, which if set to True, allows an execution to be suspended even if the current thread is still executing a code module. You can use this option to configure the execution pausing behavior on a per code module basis.
- The Allow Break While in Code Modules station option, which allows any execution to be suspended even if one or more threads is still executing a code module. This setting is located in the Execution tab of the Station Options dialog. You can set this option at run-time, as shown in this example.

The example also demonstrates how you can poll the TestStand execution status within a code module and respond when the execution pauses.

#### Example File
 Location

<TestStand
 Public>\Examples\Fundamentals\Pausing Executions with Running Code
 Modules\CVI\Pausing Executions with Running Code
 Modules.seq

#### Highlighted Features

Debugging TestStand Executions

#### Major API

Thread.ExternallySuspended

#### Prerequisites

None

#### How to Use This
 Example

Complete the following steps to run the example:

1. Select Execute»Run MainSequence to execute the
 sequence.
2. This example shows three configuration cases. For each case, the code module
 dialog indicates the current settings for the
 Thread.ExternallySuspended property and the
 Allow Break While in Code Modules station
 option.
3. In case one, observe that the TestStand execution does not pause when it reaches
 the break step. The code module also continues executing.
4. After you dismiss the dialog, the execution will pause. Click the
 Resume button or press F5 to resume the
 execution.
5. In cases two and three, the execution is able to pause successfully, and the
 code module pauses the simulated testing operation. If you resume the execution
 in TestStand while the module is still running, observe that the module resumes
 testing.

Parent topic:

Pausing Executions with Running Code Modules

Related concepts:

- TestStand Directory Structure
- Debugging Executions

<!--NI_TOPIC bundle=teststand path=pausing-executions-labview.html language=enus -->
## TOPIC 00683: Pausing Executions with Running Code Modules - LabVIEW

- bundle_id: `teststand`
- source_path: `pausing-executions-labview.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/pausing-executions-labview.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Purpose A TestStand execution cannot break until all threads within the execution have been suspended. If one or more threads in the execution is running a code module, the execution will not break until all code modules complete. This example demonstrates two methods you can use to override this be

### Pausing Executions with Running Code Modules - LabVIEW

#### Purpose

A TestStand execution cannot break until all threads within the execution have been suspended. If one or more threads in the execution is running a code module, the execution will not break until all code modules complete.

This example demonstrates two methods you can use to override this behavior:

- The Thread.ExternallySuspended property, which if set to True, allows an execution to be suspended even if the current thread is still executing a code module. You can use this option to configure the execution pausing behavior on a per code module basis.
- The Allow Break While in Code Modules station option, which allows any execution to be suspended even if one or more threads is still executing a code module. This setting is located in the Execution tab of the Station Options dialog. You can set this option at run-time, as shown in this example.

The example also demonstrates how you can poll the TestStand execution status within a code module and respond when the execution pauses.

#### Example File
 Location

<TestStand
 Public>\Examples\Fundamentals\Pausing Executions with Running Code
 Modules\LabVIEW\Pausing Executions with Running Code
 Modules.seq

#### Highlighted Features

Debugging TestStand Executions

#### Major API

Thread.ExternallySuspended

#### Prerequisites

You must have the LabVIEW development system installed and configure the LabVIEW Adapter to use the LabVIEW development system.

#### How to Use This
 Example

Complete the following steps to run the example:

1. Select Execute»Run MainSequence to execute the
 sequence.
2. This example shows three configuration cases. For each case, the code module
 dialog indicates the current settings for the
 Thread.ExternallySuspended property and the
 Allow Break While in Code Modules station
 option.
3. In case one, observe that the TestStand execution does not pause when it reaches
 the break step. The code module also continues executing.
4. After you dismiss the dialog, the execution will pause. Click the
 Resume button or press F5 to resume the
 execution.
5. In cases two and three, the execution is able to pause successfully, and the
 code module pauses the simulated testing operation. If you resume the execution
 in TestStand while the module is still running, observe that the module resumes
 testing.

Parent topic:

Pausing Executions with Running Code Modules

Related concepts:

- TestStand Directory Structure
- Debugging Executions

<!--NI_TOPIC bundle=teststand path=pausing-executions-net.html language=enus -->
## TOPIC 00684: Pausing Executions with Running Code Modules - .NET

- bundle_id: `teststand`
- source_path: `pausing-executions-net.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/pausing-executions-net.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Purpose A TestStand execution cannot break until all threads within the execution have been suspended. If one or more threads in the execution is running a code module, the execution will not break until all code modules complete. This example demonstrates two methods you can use to override this be

### Pausing Executions with Running Code Modules - .NET

#### Purpose

A TestStand execution cannot break until all threads within the execution have been suspended. If one or more threads in the execution is running a code module, the execution will not break until all code modules complete.

This example demonstrates two methods you can use to override this behavior:

- The Thread.ExternallySuspended property, which if set to True, allows an execution to be suspended even if the current thread is still executing a code module. You can use this option to configure the execution pausing behavior on a per code module basis.
- The Allow Break While in Code Modules station option, which allows any execution to be suspended even if one or more threads is still executing a code module. This setting is located in the Execution tab of the Station Options dialog. You can set this option at run-time, as shown in this example.

The example also demonstrates how you can poll the TestStand execution status within a code module and respond when the execution pauses.

#### Example File
 Location

<TestStand
 Public>\Examples\Fundamentals\Pausing Executions with Running Code
 Modules\DotNet\Pausing Executions with Running Code
 Modules.seq

#### Highlighted Features

Debugging TestStand Executions

#### Major API

Thread.ExternallySuspended

#### Prerequisites

None

#### How to Use This
 Example

Complete the following steps to run the example:

1. Select Execute»Run MainSequence to execute the
 sequence.
2. This example shows three configuration cases. For each case, the code module
 dialog indicates the current settings for the
 Thread.ExternallySuspended property and the
 Allow Break While in Code Modules station
 option.
3. In case one, observe that the TestStand execution does not pause when it reaches
 the break step. The code module also continues executing.
4. After you dismiss the dialog, the execution will pause. Click the
 Resume button or press F5 to resume the
 execution.
5. In cases two and three, the execution is able to pause successfully, and the
 code module pauses the simulated testing operation. If you resume the execution
 in TestStand while the module is still running, observe that the module resumes
 testing.

Parent topic:

Pausing Executions with Running Code Modules

Related concepts:

- TestStand Directory Structure
- Debugging Executions

<!--NI_TOPIC bundle=teststand path=pausing-executions-with-running-code-modules.html language=enus -->
## TOPIC 00685: Pausing Executions with Running Code Modules

- bundle_id: `teststand`
- source_path: `pausing-executions-with-running-code-modules.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/pausing-executions-with-running-code-modules.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The <TestStand Public>\Examples\Fundamentals\Pausing Executions with Running Code Modules directory contains the following examples.

### Pausing Executions with Running Code Modules

The <TestStand
 Public>\Examples\Fundamentals\Pausing Executions with Running Code
 Modules directory contains the following examples.

- [Pausing Executions with Running Code Modules - LabWindows/CVI](pausing-executions-cvi.html)
- [Pausing Executions with Running Code Modules - LabVIEW](pausing-executions-labview.html)
- [Pausing Executions with Running Code Modules - .NET](pausing-executions-net.html)

Parent topic:

Examples for Fundamentals

Related concepts:

- TestStand Directory Structure

<!--NI_TOPIC bundle=teststand path=persisting-application-settings.html language=enus -->
## TOPIC 00686: Persisting Application Settings

- bundle_id: `teststand`
- source_path: `persisting-application-settings.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/persisting-application-settings.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The TestStand Engine stores Station Options dialog box settings, Insertion Palette step type and template list settings, and other settings that apply to all TestStand applications in files such as GeneralEngine.cfg and Templates.ini, located in the <TestStand Application Data>\Cfg directory. Howeve

### Persisting Application Settings

The TestStand Engine stores Station Options dialog box settings, Insertion Palette step type and template list settings, and other settings that apply to all TestStand applications in files such as GeneralEngine.cfg and Templates.ini, located in the <TestStand Application Data>\Cfg directory. However, each user interface also stores additional custom settings, including breaking on the first step of execution, breaking when a step fails, and listing the most recently used sequence files. The Application Manager control stores these settings in the configuration file the ApplicationMgr.ConfigFilePath property specifies.

The ApplicationMgr.BreakOnFirstStep, ApplicationMgr.PromptForOverwrite, ApplicationMgr.EditReadOnlyFiles, ApplicationMgr.MakeStepNamesUnique, and ApplicationMgr.SaveOnClose properties persist to the configuration file. Setting the value of one of these properties on the Application Manager control in a designer sets the default value for the property. The Application Manager control stores the default value in the configuration file it creates when a configuration file does not already exist. When the configuration file already exists, the Application Manager control loads the values of these properties from the file.

Parent topic:

User Interface Development Best Practices

Related concepts:

- TestStand Directory Structure
- Application Manager

<!--NI_TOPIC bundle=teststand path=pl-step-type-loading-limits-alias.html language=enus -->
## TOPIC 00687: Property Loader Step Type - Loading Limits from a File Containing Alias

- bundle_id: `teststand`
- source_path: `pl-step-type-loading-limits-alias.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/pl-step-type-loading-limits-alias.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Purpose This example demonstrates using the Property Loader step type to load the properties from a source containing alias names instead of property lookup strings. These aliases and corresponding properties are defined in a separate .pla file. The example loads properties at the beginning of the M

### Property Loader Step Type - Loading Limits from a File Containing Alias

#### Purpose

This example demonstrates using the Property Loader step type to load the properties from a source containing alias names instead of property lookup strings. These aliases and corresponding properties are defined in a separate .pla file. The example loads properties at the beginning of the MainSequence.

#### Example File
 Location

<TestStand
 Public>\Examples\Built-In Step Types\Property Loader Step Type\
 Property Loader - Loading Limits From File Containing Alias.seq

#### Highlighted Features

- Property Loader steps
- ReportOptions callback

#### Major API

None

#### Prerequisites

None

#### How to Use This Example

Complete the following steps to review the sequence functionality.

1. On the Steps pane, select the Property Loader step in the Setup step group.
2. On the Target File and Source Settings tab, observe that the file AliasNames.pla is specified for the Alias Location field. This file specifies alias names for various properties, making it easier to identify them in a limits file. Open the file in a text editor to review the contents.
3. On the Step Settings tab in the Step Settings pane, click the View Source File button in the sources table to open the properties file. Observe that the properties in the file are specified using the aliases defined in the alias file.

Complete the following steps to run this example.

1. Select Execute»Single Pass to run the sequence.
2. When execution completes, review the report on the Report pane. Ensure that the limits were changed based on the property loader step configuration.

Parent topic:

Examples for Built-In Step Types

Related concepts:

- TestStand Directory Structure

<!--NI_TOPIC bundle=teststand path=pl-step-type-loading-limits-excel.html language=enus -->
## TOPIC 00688: Property Loader Step Type - Loading Limits from a Microsoft Excel File

- bundle_id: `teststand`
- source_path: `pl-step-type-loading-limits-excel.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/pl-step-type-loading-limits-excel.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Purpose This example demonstrates how to use a Property Loader step type to load limits from a Microsoft Excel spreadsheet file. This example uses the LabWindows/CVI Adapter for Numeric Limit Test steps. Example File Location <TestStand Public>\Examples\Built-In Step Types\Property Loader Step Type\

### Property Loader Step Type - Loading Limits from a Microsoft Excel File

#### Purpose

This example demonstrates how to use a Property Loader step type to load limits from a Microsoft Excel spreadsheet file. This example uses the LabWindows/CVI Adapter for Numeric Limit Test steps.

#### Example File
 Location

<TestStand
 Public>\Examples\Built-In Step Types\Property Loader Step
 Type\Property Loader - Loading Limits From Excel.seq

#### Highlighted Features

- Property Loader steps
- ReportOptions callback

#### Major API

None

#### Prerequisites

You must have Microsoft Excel installed.

#### How to Use This Example

The Property Loader step starts reading data from the START LIMITS marker and reads data until it encounters the END LIMITS marker.

Complete the following steps to review the sequence functionality.

1. On the Steps pane, select the Property Loader step in the Setup step group.
2. On Target File and Source Settings tab in the step settings pane, review the properties selected in the Property Tree control. The step loads the Limits.Low and Limits.High values for each step.
3. On the Step Settings tab of the Steps pane, click the View File button in the sources table to open <TestStand Public>\Examples\Built-In Step Types\Property Loader Step Type\Limits.xls in Excel. The columns in the Excel file specify the properties to import, and the rows specify the names of the steps in the sequence.

Complete the following steps to run this example.

1. Select Execute»Single Pass to run the sequence.
2. When execution completes, review the report on the Report pane. The report indicates that TestStand updated the limits of the steps based on the values in the Excel file.
3. In the Limits.xls file, change the Flow Rate value from 1 to 1.1 and save the file.
4. Select Execute»Single Pass to run the sequence again.
5. When execution completes, review the report on the Report pane. The report indicates that the results have changed because of the updated step limits.

Parent topic:

Examples for Built-In Step Types

Related concepts:

- Programming with the TestStand API in LabWindows/CVI
- TestStand Directory Structure
- Step Groups

<!--NI_TOPIC bundle=teststand path=pl-step-type-loading-limits-mult-source.html language=enus -->
## TOPIC 00689: Property Loader Step Type - Loading Limits from Multiple Sources

- bundle_id: `teststand`
- source_path: `pl-step-type-loading-limits-mult-source.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/pl-step-type-loading-limits-mult-source.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Purpose This example demonstrates using the Property Loader step type to load data from multiple property loader sources. The example loads properties from GenericLimits to load limits for Voltage and Temperature and loads properties from SpeacializedLimits to override the limits for Voltage. Exampl

### Property Loader Step Type - Loading Limits from Multiple Sources

#### Purpose

This example demonstrates using the Property Loader step type to load data from multiple property loader sources. The example loads properties from GenericLimits to load limits for Voltage and Temperature and loads properties from SpeacializedLimits to override the limits for Voltage.

#### Example File
 Location

<TestStand
 Public>\Examples\Built-In Step Types\Property Loader Step Type\
 Property Loader - Loading Limits From Multiple Sources.seq

#### Highlighted Features

- Property Loader steps
- ReportOptions callback

#### Major API

None

#### Prerequisites

None

#### How to Use This Example

Complete the following steps to review the sequence functionality.

1. On the Steps pane, select the Property Loader step in the Setup step group.
2. On the Step Settings tab in the Step Settings pane, observe that two source locations are specified in the source table. This indicates that properties will be loaded from multiple sources, in this case two text files.
3. Navigate to the <TestStand Public>\Examples\Built-In Step Types\Property Loader Step Type directory and review the GenericLimits.txt and SpecializedLimits.txt files. Observe that both files have properties defined for the voltage test. In this case, the file specified last in the source table will take precedence.

Complete the following steps to run this example.

1. Select Execute»Single Pass to run the sequence.
2. When execution completes, review the report on the Report pane. Ensure that the limits were changed based on the property loader step configuration.

Parent topic:

Examples for Built-In Step Types

Related concepts:

- TestStand Directory Structure

<!--NI_TOPIC bundle=teststand path=pl-step-type-loading-limits-text.html language=enus -->
## TOPIC 00690: Property Loader Step Type - Loading Limits from Two Different Text Files

- bundle_id: `teststand`
- source_path: `pl-step-type-loading-limits-text.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/pl-step-type-loading-limits-text.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Purpose This example demonstrates how to use the Property Loader step to dynamically load step limits from different text files depending on user input. In the Setup step group of the MainSequence, the Message Popup step launches a dialog box to prompt the user to choose which file TestStand uses to

### Property Loader Step Type - Loading Limits from Two Different Text Files

#### Purpose

This example demonstrates how to use the Property Loader step to dynamically load step limits from different text files depending on user input.

In the Setup step group of the MainSequence, the Message Popup step launches a dialog box to prompt the user to choose which file TestStand uses to load limits values. The Select Limit File Statement step in the Setup step group selects the limit file. The expression for this step uses a conditional operation in which TestStand loads limits from RevisionALimits.txt when the value of the Result.ButtonHit property equals 1. The expression specifies that TestStand loads limits from RevisionBLimits.txt for all other cases.

When you write a sequence in which the user must choose between three or more limit files, use a Property Loader step for each limit file and use a precondition for each step that checks for user input. For example, when the Message Popup step specifies four buttons, each Property Loader step can check which button was clicked in the precondition.

#### Example File
 Location

<TestStand
 Public>\Examples\Built-In Step Types\Property Loader Step
 Type\Property Loader - Loading Limits From Different
 Files.seq

#### Highlighted Features

- Property Loader steps
- ReportOptions callback

#### Major API

None

#### Prerequisites

None

#### How to Use This Example

Complete the following steps to review the sequence functionality.

1. On the Steps pane, select the Property Loader step in the Setup step group.
2. On the Step Settings tab of the Step Settings pane, confirm that the source location in the sources table specifies the Locals.LimitFileToLoad variable. The value of this variable at run time determines which file TestStand loads.
3. Navigate to the <TestStand Public>\Examples\Built-In Step Types\Property Loader Step Type directory and review the RevisionALimits.txt and RevisionBLimits.txt files. Each file specifies a different set of limit values for the sequence.
4. On the Steps pane, select the Select Limit File step, which is an instance of a Statement step type. This step sets the Locals.LimitFileToLoad variable to the correct value depending on which file the user selects.

Complete the following steps to run this example.

1. Select Execute»Single Pass to run the sequence.
2. When prompted, select the Revision A Limits option.
3. When execution completes, review the report on the Report pane. The report indicates that all steps passed.
4. Select Execute»Single Pass to run the sequence again.
5. When prompted, select the Revision B Limits option.
6. When execution completes, review the report on the Report pane. The report indicates that not all steps passed because of the different set of limit values. The step results have not changed.

Parent topic:

Examples for Built-In Step Types

Related concepts:

- Step Groups
- TestStand Directory Structure

<!--NI_TOPIC bundle=teststand path=platform-specific-assemblies-in-32-bit-testst.html language=enus -->
## TOPIC 00691: Platform-Specific Assemblies in 32-bit TestStand and 64-bit TestStand

- bundle_id: `teststand`
- source_path: `platform-specific-assemblies-in-32-bit-testst.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/platform-specific-assemblies-in-32-bit-testst.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Complete the following steps to migrate platform-specific .NET assemblies when you no longer intend to support the 32-bit architecture. Replace existing 32-bit .NET code modules with 64-bit versions in-place. Move the assemblies located in the <TestStand Public> or other non-shared search directory

### Platform-Specific Assemblies in 32-bit TestStand and 64-bit TestStand

Complete the following steps to migrate platform-specific .NET assemblies when you no
 longer intend to support the 32-bit architecture.

1. Replace existing 32-bit .NET code modules with 64-bit versions in-place.
2. Move the assemblies located in the <TestStand Public> or other non-shared search directory to the equivalent 64-bit location.

If the 64-bit version of the interface remains unchanged, TestStand sequences that depend on the code modules execute in 64-bit TestStand but no longer execute in 32-bit TestStand.

If you need to simultaneously support both architectures with a .NET code module but cannot use an AnyCPU assembly, create a 32-bit version of the assembly and a 64-bit version of the assembly and use one of the following techniques to associate the assembly with the adapter:

- Use the $(Platform) path macro. Although the default 32-bit subdirectory for .NET projects is x86 in Microsoft Visual Studio, TestStand expands $(Platform) to win32 for the .NET Adapter just as it does for the C/C++ DLL and LabWindows/CVI Adapters.
- Use non-shared TestStand search directories.
- Write bitness-conditional code when the 32-bit version and the 64-bit version of a .NET code module use different interfaces.

Note

Note

Parent topic:

.NET Code Module Support for 64-bit TestStand

Related concepts:

- TestStand Directory Structure
- Using the $(Platform) Path Macro to Locate the Correct Code Module in 32-bit TestStand and 64-bit TestStand
- Components Directory
- Bitness-Conditional Code for DLLs with Different 32-bit Interfaces and 64-bit Interfaces

<!--NI_TOPIC bundle=teststand path=plug-and-play-instrument-drivers.html language=enus -->
## TOPIC 00692: Plug and Play Instrument Drivers

- bundle_id: `teststand`
- source_path: `plug-and-play-instrument-drivers.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/plug-and-play-instrument-drivers.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Plug and Play drivers simplify controlling and communicating with the instrument through a standard, straightforward programming model for all drivers. Plug and Play drivers exist for LabVIEW and LabWindows/CVI. Using Plug and Play Drivers with LabVIEW A LabVIEW Plug and Play instrument driver is a

### Plug and Play Instrument Drivers

Plug and Play drivers simplify controlling and communicating with the instrument through a standard, straightforward programming model for all drivers. Plug and Play drivers exist for LabVIEW and LabWindows/CVI.

#### Using Plug and Play Drivers with LabVIEW

A LabVIEW Plug and Play instrument driver is a set of VIs. Each VI corresponds to a programmatic operation for the instrument. National Instruments distributes LabVIEW Plug and Play instrument drivers with the block diagram source code so you can customize the VIs. You can create instrument control applications and systems by programmatically linking instrument driver VIs on the block diagram. LabVIEW Plug and Play instrument drivers usually use Virtual Instrument Software Architecture (VISA) functions to communicate with instruments.

In TestStand, you can call VIs that use LabVIEW Plug and Play instrument drivers. When you return a VISA reference to TestStand and later pass the reference to a different VI code module that uses the same instrument driver, store the reference in a TestStand LabVIEWIOReference variable. You can also use the LabVIEW Adapter to directly call VIs in an instrument driver.

#### Using Plug and Play Drivers with LabWindows/CVI

A LabWindows/CVI Plug and Play instrument driver is a set of ANSI C software routines exported from a DLL. You can call these instrument drivers from any development environment that supports calls into DLLs. You can also use a LabWindows/CVI instrument driver in LabVIEW when you convert the instrument driver using the Create VI Interface to CVI Instrument Driver tool available from the Instrument Driver Network at ni.com/idnet. LabWindows/CVI Plug and Play instrument drivers are based on the VXI plug & play standard architecture and usually use VISA functions to communicate with instruments.

In TestStand, you can call code modules that use LabWindows/CVI Plug and Play instrument drivers. When you return a C-based reference to TestStand and later pass the reference to a different code module that uses the same instrument driver, store the reference in a TestStand numeric variable. You can also use the LabWindows/CVI or C/C++ DLL Adapter to directly call the functions in an instrument driver.

Parent topic:

Instrument Drivers

Related concepts:

- Code Modules

Related information:

- NI Instrument Driver Network

<!--NI_TOPIC bundle=teststand path=plug-in-entry-point-parameters.html language=enus -->
## TOPIC 00693: Plug-in Entry Point Parameters

- bundle_id: `teststand`
- source_path: `plug-in-entry-point-parameters.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/plug-in-entry-point-parameters.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Model plug-in entry points accept the following parameters: Name Data Type Model Plug-in Entry Point Description CallbackNames String Array OnTheFly Step Results Each element in this array specifies the callback sequence name of the step result at the corresponding index in the Parameters.Results ar

### Plug-in Entry Point Parameters

Model plug-in entry points accept the following parameters:

| Name | Data Type | Model Plug-in Entry Point | Description |
| --- | --- | --- | --- |
| CallbackNames | String Array | OnTheFly Step Results | Each element in this array specifies the callback sequence name of the step result at the corresponding index in the Parameters.Results array. Callback names are the same as subsequence result property names. The callback name is SequenceCall for steps that TestStand generates within a sequence you run or within the subsequences it calls using Sequence Call steps. |
| CallingThread | Reference | UUT Done Batch Done | A reference to the test socket or controller thread that invoked the UUT Done or Batch Done entry point. If you configure the model plug-in to run in a new thread, the thread that runs the plug-in is a different thread from the thread the CallingThread parameter specifies. |
| CallingThreadBlocker | Reference | UUT Done Batch Done | Reference to a TestStand notification object. If the value of this reference is a value other than Nothing, a different thread is executing the entry point than is executing the process model. The calling thread that executes the process model does not proceed until the entry point sets this notification, which allows the entry point to safely copy parameter information that is subject to change if the process model proceeds to the next UUT or batch before the thread that runs the entry point completes. For example, the UUT Start entry point in the built-in reporting plug-in creates and stores a new report in ResultProcessor.RuntimeVariables.PerSocket[<socket index>].Specific.ReportInstance. The UUT Done entry point in the built-in reporting plug-in copies the value of that property to a local variable before setting this notification. |
| Context | SequenceContext | OnTheFly Step Results | A reference to the SequenceContext for the sequence that executes when the process model invokes the OnTheFly Step Results entry point. Because TestStand does not serialize the context to offline result files and does not pass the context to the OnTheFly Step Results entry point when processing an offline results file, do not use the Context parameter in a plug-in if an alternative implementation is possible. If a plug-in uses the Context parameter, set the FileGlobals.ResultProcessorComponentDescription.Default.CanProcessOfflineOnTheFlyResults property of the plug-in to False.This parameter does not necessarily correspond to the sequence that produces the step results OnTheFly Step Results receives because the results might have been accumulated from the execution of multiple sequences. If you must access the context for the sequence that generated the results, set the RunState.Execution.PostResultsCallback_PreFlushMask and RunState.Execution.PostResultsCallback_PostFlushMask properties in the Begin entry point to ensure that the process model invokes OnTheFly Step Results within the sequence that generates the results the plug-in processes. When you change settings that determine how often the process model invokes OnTheFly Step Results, do not change the settings such that the process model calls the entry point less frequently or under fewer conditions or you might violate the conditions another plug-in instance sets and expects. |
| ContinueTesting | Boolean (output) | Pre Batch Pre UUT | If this parameter is False after the process model calls the Pre UUT entry point for every plug-in, the process model exits the UUT loop without calling the UUT Start, UUT Done, or Post UUT entry points.If this parameter is False after the Batch process model calls the Pre Batch entry point for every plug-in, the Batch process model exits the batch loop without calling the Batch Start, Batch Done, or Post Batch entry points. The Batch process model also exits the UUT loop without calling the Pre UUT, UUT Start, UUT Done, or Post UUT entry points. If multiple model plug-ins use conflicting values for ContinueTesting, TestStand uses the value set by the last plug-in to execute. |
| MainSequenceResult | Reference | Post UUT UUT Done Post Batch Batch Done | A reference to the result of the process model call to the MainSequence callback in the client sequence file. The results of the client sequence file MainSequence are located in the MainSequenceResult.TS.SequenceCall.ResultList property. TestStand passes Nothing to this parameter for the Batch Done and Post Batch entry points. |
| ModelData | ContainerNote The actual data type varies at run time depending on the process model. For built-in process models, the data type can be NI_SequentialModelData, NI_ParallelModelData2, or NI_BatchModelData2. | Begin Pre Batch Pre UUT Batch Start UUT Start OnTheFly Step Results UUT Done Batch Done Post UUT Post Batch End | Contains model-specific information, such as the ModelOptions property. |
| ModelPlugin | NI_ModelPlugin | <All> | Configuration and run-time variables for the plug-in instance. |
| ModelPluginConfiguration | NI_ModelPluginConfiguration | Begin Pre Batch Pre UUT Batch Start UUT Start UUT Done Batch Done Post UUT Post Batch End | Configuration and run-time variables for the set of all active plug-in instances. The ModelPlugin parameter is also an element within the ModelPluginConfiguration.ModelPlugins array property. |
| ModelThreadType | NI_ModelThreadType | Begin Pre Batch Pre UUT Batch Start UUT Start UUT Done Batch Done Post UUT Post Batch End | Specifies whether the current thread is a model test socket thread, a model controller thread, or both. |
| ModelType | NI_ModelType | Configure Standard Options Configure Additional Options | String that indicates the type of the current process model. A dialog box that displays options that vary according to the type of model can use this value to determine which options to initially display. |
| ParentIds | Numeric Array | OnTheFly Step Results | Each element in this array specifies the result ID of the parent result for the result at the corresponding index in the Parameters.Results array. The parent is the result for the Sequence Call step that called the sequence that created the result. You can use parent IDs to reconstruct the hierarchy of sequence calls that generate results. The result for a process model MainSequence callback that invokes the MainSequence in the client file is at the root level of its thread and does not have a parent result. In this case, TestStand passes the negative value of the ID for the thread in which the step runs. TestStand negates the value so you can distinguish the thread ID from a result ID. |
| ParentThread | Reference | Begin | When a test socket thread calls the Begin entry point, the test socket passes its controller thread to the ParentThread parameter. If the calling thread is a controller thread, it passes Nothing to the ParentThread parameter even if the calling thread is also the test socket thread. Typically, a plug-in does not need to use the ParentThread parameter. |
| PriorIterationNewThread | Reference | UUT Done Batch Done | A reference to the thread that ran the entry point for the previous UUT or batch. The value is Nothing if the model did not invoke the previous call in a new thread. A plug-in can wait on this thread to ensure the model processes UUTs in chronological order. For example, if you configure the built-in reporting plug-in to store multiple UUT reports in the same file, the plug-in waits for this thread to complete before appending a new UUT report to the file, ensuring the plug-in stores reports in chronological order. |
| ProcessModelClientPath | Path | Begin Pre Batch Pre UUT Batch Start UUT Start UUT Done Batch Done Post UUT Post Batch | Absolute path to the client sequence file the process model is executing. |
| Results | Array of References | OnTheFly Step Results | An array of references to the step result PropertyObject instances TestStand has accumulated since the previous call to the OnTheFly Step Results entry point. Each element in the array is a TestStand reference. To access a result, you must dereference its reference. |
| StartDate | DateDetails | Begin Pre Batch Pre UUT Batch Start UUT Start OnTheFly Step Results UUT Done Batch Done Post UUT Post Batch | When passed to the Begin entry point, the StartDate parameter indicates when TestStand invoked the process model Execution entry point. Otherwise, the StartDate parameter indicates when the UUT in the current socket began testing or when the current batch began testing for a batch controller thread. |
| StartTime | TimeDetails | Begin Pre Batch Pre UUT Batch Start UUT Start OnTheFly Step Results UUT Done Batch Done Post UUT Post Batch | When passed to the Begin entry point, the StartTime parameter indicates when TestStand invoked the process model Execution entry point. Otherwise, the StartTime parameter indicates when the UUT in the current socket began testing or when the current batch began testing for a batch controller thread. |
| Step | Array of References | OnTheFly Step Results | An array of references to the steps that generated the corresponding elements of the Parameters.Results array. Each element in the array is a TestStand reference. To access a step, you must dereference its reference. Because TestStand does not serialize the steps to offline result files and does not pass the references to the OnTheFly Step Results entry point when processing an offline results file, do not use the Step parameter in a plug-in if an alternative implementation is possible. If a plug-in uses the Step parameter, set the FileGlobals.ResultProcessorComponentDescription.Default.CanProcessOfflineOnTheFlyResults property of the plug-in to False to indicate this situation. |
| UUT | UUT | Pre Batch Pre UUT Batch Start UUT Start OnTheFly Step Results UUT Done Batch Done Post UUT Post Batch | For the Pre UUT, UUT Start, UUT Done, Post UUT, and OnTheFly Step Results entry points, the UUT parameter contains the UUT information for the current test socket. For the Pre Batch, Batch Start, Batch Done, and Post Batch entry points, the parameter contains UUT information for the batch as a whole. |
| UUTStatus | String | UUT Done Post UUT Batch Done Post Batch | The result status of the UUT, such as Passed or Failed. TestStand does not currently use the value passed to the Batch Done and Post Batch entry points, and you can ignore it. |

Parent topic:

Structure of Plug-in Sequence Files

Related concepts:

- Model Plugin – OnTheFly Step Results
- Subsequence Results
- Model Plugin – UUT Done
- Model Plugin – Batch Done
- Process Model Thread Types
- Model Plugin – UUT Start
- Model Plugin – Begin
- Model Plugin – Pre Batch
- Model Plugin – Pre UUT
- Model Plugin – Post UUT
- Model Plugin – Batch Start
- Model Plugin – Post Batch
- Model Plugin – End
- Model Plugin – Configure Standard Options
- Model Plugin – Configure Additional Options
- Thread Safety of the PropertyObject API and TestStand Variables

<!--NI_TOPIC bundle=teststand path=plug-in-utility-sequences.html language=enus -->
## TOPIC 00694: Plug-in Utility Sequences

- bundle_id: `teststand`
- source_path: `plug-in-utility-sequences.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/plug-in-utility-sequences.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Process model Execution entry points call the following sequences in ModelSupport.seq: Initialize Execution Entry Point—Execution entry points call the Initialize Execution Entry Point sequence at the beginning of an execution. The Initialize Execution Entry Point sequence reads the test station mod

### Plug-in Utility Sequences

Process model Execution entry points call the following sequences in ModelSupport.seq:

- Initialize Execution Entry Point —Execution entry points call the Initialize Execution Entry Point sequence at the beginning of an execution. The Initialize Execution Entry Point sequence reads the test station model options from disk and calls the ModelOptions callback so the client sequence file can modify the model options, identifies the test station name and the current user, loads the set of model plug-in instances to run during model execution, and performs other initialization operations.
- Model Plugins – <entry point name> —Execution entry points call the Model Plugins – < entry point name > sequences to invoke the corresponding entry points for each enabled model plug-in instance.

Parent topic:

Features Common to All TestStand Process Models

Related concepts:

- Integrating Model Plug-ins with a Custom Process Model

<!--NI_TOPIC bundle=teststand path=pointers-and-handles-in-32-bit-teststand-and.html language=enus -->
## TOPIC 00695: Pointers and Handles in 32-bit TestStand and 64-bit TestStand

- bundle_id: `teststand`
- source_path: `pointers-and-handles-in-32-bit-teststand-and.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/pointers-and-handles-in-32-bit-teststand-and.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: TestStand C/C++ DLL Adapter and LabWindows/CVI Adapter steps can support pointers and pointer-sized handles from a single adapter step. For example, 32-bit TestStand and 64-bit TestStand recognize a char * (pointer to character) as a string and a CAObjHandle as a LabWindows/CVI ActiveX Automation Ha

### Pointers and Handles in 32-bit TestStand and 64-bit TestStand

TestStand C/C++ DLL Adapter and LabWindows/CVI Adapter steps can support pointers and pointer-sized handles from a single adapter step. For example, 32-bit TestStand and 64-bit TestStand recognize a char * (pointer to character) as a string and a CAObjHandle as a LabWindows/CVI ActiveX Automation Handle. Similarly, a single step can handle functions that take values by reference.

However, if you treat the pointer as a number, a single step cannot simultaneously support the 32-bit case and the 64-bit case. For example, 32-bit TestStand supports treating LabWindows/CVI ActiveX Automation Handles as 32-bit integers, and you can specify the type int instead of CAObjHandle in the C source prototype. You cannot use this strategy for 64-bit TestStand because the int data type is always 32 bits. In this case, for a 64-bit version of the DLL, you would have to replace the int (32-bit) data type with the long long (64-bit) data type, which would change the signature of the function and require a separate step and conditional code to work in 32-bit TestStand and in 64-bit TestStand.

NI recommends using the CAObjHandle data type in C prototypes in conjunction
 with the TestStand Object Reference data type in the sequence when you pass
 LabWindows/CVI ActiveX Automation Handles as parameters in adapter steps so the same
 TestStand step works in the 32-bit case and in the 64-bit case.

Using numbers as pointers when you pass NULL to a function can result in incorrect behavior. In 32-bit TestStand, you can specify the type of a pointer argument as a 32-bit integer in an adapter step and pass 0. Using this technique in 64-bit TestStand results in undefined behavior, such as data corruption or a crash. The code module expects all 64-bits of the pointer to be 0 for NULL, but 64-bit TestStand interprets the argument as only 32-bits, sets only the low order 32-bits, and leaves the high order bits undefined. In this case, to achieve correct results in 64-bit TestStand, you would have to set the type of the number in the prototype to a 64-bit integer and pass 0i64. However, the 64-bit-specific solution would not work in 32-bit TestStand.

To pass NULL as a parameter, specify the data type as a pointer in TestStand and pass
 Nothing. NI recommends this approach in all cases, regardless
 of migration or cross-platform support requirements, because TestStand converts
 Nothing to the correct NULL pointer representation for the
 current architecture. The Nothing constant is an Object Reference
 type and is thus a more semantically accurate representation of a NULL pointer than
 0 or 0i64.

For C DLLs that do not have associated type libraries or LabWindows/CVI embedded type
 information, TestStand cannot detect and warn when pointers are incorrectly treated
 as numbers. One situation in which this issue might arise is when you call Microsoft
 Win32 API functions in user32.dll or kernel32.dll
 from the TestStand C/C++ DLL Adapter. NI recommends that when you migrate to 64-bit
 TestStand, you review all C/C++ DLL and LabWindows/CVI Adapter steps that use these
 and similar APIs for incorrect use of the number 0 as NULL for
 pointers.

Parent topic:

C/C++ DLL and LabWindows/CVI DLL Support for 64-bit TestStand

Related concepts:

- Representing Pointers in Sequences in 32-bit TestStand and 64-bit TestStand

<!--NI_TOPIC bundle=teststand path=posting-user-interface-messages.html language=enus -->
## TOPIC 00696: Posting User Interface Messages

- bundle_id: `teststand`
- source_path: `posting-user-interface-messages.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/posting-user-interface-messages.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: TestStand currently supports posting user interface messages by calling the Thread.PostUIMessageEx method, which allows the steps of an execution to post progress events and user-defined events. Because the PostUIMessageEx method is a method of the Thread class, the thread and its associated executi

### Posting User Interface Messages

TestStand currently supports posting user interface messages by calling the Thread.PostUIMessageEx method, which allows the steps of an execution to post progress events and user-defined events. Because the PostUIMessageEx method is a method of the Thread class, the thread and its associated execution are automatically properties of the user interface message. You can send additional data using the numericDataParam and stringDataParam parameters of the method.

Parent topic:

User Interface Messages (UIMessages)

Related concepts:

- Execution Events
- User-Defined Events

<!--NI_TOPIC bundle=teststand path=preparing-source-components-for-deployment.html language=enus -->
## TOPIC 00697: Preparing Source Components for Deployment

- bundle_id: `teststand`
- source_path: `preparing-source-components-for-deployment.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/preparing-source-components-for-deployment.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the following best practices for test system development before you create a full or patch deployment: During Development Filenames—Use unique filenames in a test system to avoid file conflicts and to avoid including the wrong file in a deployment. Rename duplicate filenames, even if the files e

### Preparing Source Components for Deployment

[IMAGE alt='image' src='GUID-DF811C7A-9139-44BA-9A51-792339D3389D-a5.svg']

Use the following best practices for test system development before you create a full or patch deployment:

#### During Development

- Filenames —Use unique filenames in a test system to avoid file conflicts and to avoid including the wrong file in a deployment. Rename duplicate filenames, even if the files exist in different directories. Using files with the same name can cause sequences or the TestStand Deployment Utility to locate the wrong files, which can result in incorrect behavior. Using unique filenames ensures that TestStand locates the correct file even when you make changes to the search directories.
- Paths —Avoid using absolute paths because the paths might not exist on test station computers that use different operating systems, logical drive configurations, or other configuration settings, such as read-only settings. Using paths that are relative to the sequence file or to a search directory ensures that sequences locate required code modules even if you install the files to different directories on the test station computer from where the files exist on the development computer. Additionally, using relative paths avoids the use of complex file structures, which makes validating the deployment more complicated. Using absolute paths also prevents you from validating test sequences from the deployable image directory on the development computer because absolute paths point to the source files, not to the files in the deployable image directory. Additionally, the deployment utility attempts to replace absolute paths with relative paths while creating a deployment, which increases the deployment build time. To use absolute paths, you must ensure that the entire test system file and directory structures are identical on all development computers and test station computers that use the test system.
- DLLs —Use DLLs or LabVIEW packed project libraries to store code you share among different parts of the test system, such as code modules, or among different test systems that run on the same test station computer.
- Workspaces —Use a TestStand workspace during development to organize the files and static dependencies a project requires, which can simplify the deployment process. You must explicitly add dynamic dependencies to the workspace for the deployment utility to include. Additionally, you can use a workspace with a source code control system, which can aid the development and deployment process when multiple developers work on the same test system.
- TestStand Versions —Write all test sequences using the minimum version of TestStand the test system supports to avoid saving sequences with features or in a format the test system does not support.
- Sequence Files —Select Tools»Update Sequence Files to launch the Sequence File Converter tool, which you can use to ensure that you save the sequence files in the test system in the format you want with the correct version of TestStand and that the sequence files use the correct versions of custom data types and step types. If the test system dynamically loads and unloads a significant number of sequence files, use the binary file format to improve execution performance.
- Analysis Tools —Use the TestStand Sequence Analyzer in the TestStand Sequence Editor or the stand-alone sequence analyzer application to analyze sequence files and resolve any issues the analyzer might report before you use the TestStand Deployment Utility to create a deployment.
- Troubleshooting Tools —Use the Debug Options dialog box, the Sequence Hierarchy window, and the TestStand File Diff and Merge utility as debugging tools to troubleshoot issues with sequence files.
- Drivers —As you develop code modules, maintain a list of any NI drivers or
 components or third-party installers with version numbers the code modules
 require so you can easily determine which drivers the test system requires.

#### Before Deployment

- If you use the Insert Code Modules context menu item in the Workspace Browser dialog box or the Insert Code Modules context menu item in the Workspace pane for any of the included workspaces, delete the code modules and insert them again to refresh any code modules that might have been added or removed.
- Search Directories —If the deployment includes a SearchDirectories.cfg file, ensure that the file does not disable the sequence file directory and workspace file directory search paths in the test system. If the deployment utility cannot find the files in the image directory through search directories, which can happen if a search directory points to the source files, the utility attempts to create relative paths from the sequence file or workspace file, which might break the deployment.

#### LabVIEW

- Packed Project Libraries —Use LabVIEW packed project libraries to store code you share among different parts of the test system, such as code modules, or among different test systems that run on the same test station computer.
- VIs —Save VIs in a single version of LabVIEW to reduce the time required to create a deployment. If the test system requires multiple versions of LabVIEW, use packed project libraries.
- LabVIEW Versions —Mass compile all VIs with the active version of LabVIEW to avoid recompiling VIs each time you create a deployment, which slows deployment build times. Review the mass compile log file to identify any issues with compiling the VIs. The compiled code for 32-bit VIs and 64-bit VIs is not shared. If you are creating a 32-bit deployment and a 64-bit deployment, consider using LabVIEW packed project libraries or enabling the Separate compiled code from source file option on the General Settings page of the Project Library Properties dialog box in LabVIEW.
- Shared Variables —LabVIEW must create shared variables in the Shared Variable Engine before a test system can access the shared variables. The test station computer also requires a .alias file located in the same directory as the TestStand User Interface executable. The .alias file contains the IP address of the test station computer for LabVIEW code modules to use to resolve the references to the shared variable. When you call VIs in the context of a LabVIEW project, configure the LabVIEW Adapter to automatically deploy and undeploy shared variables or use the Deploy Library LabVIEW Utility step type to deploy shared variables. If any code modules in the deployment reference a shared variable outside the context of a LabVIEW project, the deployment will build successfully, but the shared variables will not be deployed on the target system, and the code modules will not run. To prevent this issue, ensure that the owning libraries of any shared variables are contained within a LabVIEW project, and that you include all such LabVIEW projects in the deployment.
- Bound Shared Variables —TestStand can deploy a shared variable bound to another shared variable only when you use an NI Publish-Subscribe Protocol (NI-PSP) URL to bind the shared variable to deploy to another shared variable. If you attempt to use a Deploy Library step to deploy a shared variable to a variable in a LabVIEW project, the deployment fails. Refer to the LabVIEW Help for more information about deploying shared variables and NI-PSP URLs.
- VI Calls —Select Tools»Update VI Calls to launch the Update VI Calls dialog box, in which you can verify that you compiled embedded Express VIs with the active version of LabVIEW and that all LabVIEW steps use the correct prototypes. Resolve any errors or warnings the Update VI Calls dialog box reports.

#### Validation

- Development Computer —Ensure that the test system software
 executes without errors on the development computer to reduce the time you spend
 diagnosing issues on the test station computer.
- Installed Software —Install the NI software the test system requires on
 the development computer, including the necessary patches or updates, the test
 system requires because the deployment utility can redistribute only the NI
 software installed on the computer you use to create the deployment.
  - Many NI driver installers provide different installation types that you
 can redistribute for development purposes or for only run-time purposes.
 The Full installation type is the most complete
 installation type. Installation types that support development consume
 more space in the installer and on disk after installation.
 Run-time-only installation types might exclude dependencies required to
 redeploy the development installation type. Distributions that NI
 builds, such as the NI Device Drivers DVD, always contain the full
 installation type for all products.
  - In most cases, you can install only one version of a hardware driver on
 the computer at a time. When you update drivers, validate that the
 latest version of the driver supports the existing hardware and executes
 correctly with the test system.
  - You can install multiple versions of some components, such as the
 LabVIEW Run-Time Engine (RTE) and LabWindows/CVI RTE, on the same
 computer. However, NI recommends using only one version of the LabVIEW
 RTE in a single test system to simplify deployment. When you build an
 installer with the deployment utility, the utility compiles all the
 LabVIEW files with the active version of LabVIEW, and you can run the
 VIs with the equivalent LabVIEW RTE. The LabVIEW Adapter can execute VIs
 faster using the LabVIEW RTE, but the LabVIEW RTE does not support
 debugging.
- Source Code Control System —Use a source code control
 system or other mechanism to ensure that you have the latest versions of the
 files the test system requires because the deployment utility includes only the
 files installed on the computer you use to create the deployment.
  - Verify that the required support files, such as limit files, images, and
 operator instructions, exist in the correct locations. Delete earlier
 versions of limit files to avoid including the incorrect version of the
 file. Receiving a File Not Found error is typically preferable to using
 incorrect limits. Because the deployment utility cannot detect support
 files that steps do not statically reference, you must manually add these types of dynamically referenced files to
 the TestStand workspace for the deployment utility to include them in
 the deployment.
  - Ensure that you include the latest build of binary files, such as
 executables or DLLs for user interfaces, code modules, code module
 dependencies, and support files. Combining earlier and later versions of
 executables or DLLs might create errors that are difficult to track
 down. Using a dedicated build
 computer can minimize these types of issues.
- Configuration Files —If you deploy configuration files,
 validate that the files use the correct settings. For example, the following
 settings can affect execution speed and the functionality of the test system:
  - When you enable execution tracing, user interfaces can provide
 additional information about the execution, such as the current
 execution step, the status of steps, and so on, but test systems execute
 faster with tracing disabled.
  - Incorrect search directories can cause the test system to locate the
 wrong files or can prevent the test system from finding the files at
 all.

Parent topic:

Deployment Process Overview

Related concepts:

- Patching Deployments
- Search Directories
- Customizing Components You Deploy
- Using a TestStand Workspace File to Create a Deployment
- Manually Adding or Removing Files to or from Deployments
- Organizing Test Program Files with LabVIEW Packed Project Libraries
- Using Multiple LabVIEW Versions in a Test System
- Deploying Network-Published Shared Variables
- Resolving References to Shared Variables
- Redistributing MSI-based Installer Products in a Deployment
- Using a Dedicated Build Computer
- Configuration Files
- Deploying Stand-alone VIs
- Deploying VIs in LabVIEW Packed Project Libraries
- Deploying VIs in LabVIEW Projects
- Troubleshooting LabVIEW Code Module Issues

<!--NI_TOPIC bundle=teststand path=printing-and-exporting-data-in-database-viewe.html language=enus -->
## TOPIC 00698: Printing and Exporting Data in Database Viewer

- bundle_id: `teststand`
- source_path: `printing-and-exporting-data-in-database-viewe.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/printing-and-exporting-data-in-database-viewe.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can print and export the data displayed in the data grid of the Edit Data and Execute SQL tabs. You can also print binary data displayed in the tabs of the Binary Data Viewer. Select File»Print or use the <Ctrl+P> keyboard shortcut to launch the Print dialog box, in which you can configure optio

### Printing and Exporting Data in Database Viewer

You can print and export the data displayed in the data grid of the Edit Data and Execute SQL tabs. You can also print binary data displayed in the tabs of the Binary Data Viewer.

Select File»Print or use the <Ctrl+P> keyboard shortcut to launch the Print dialog box, in which you can configure options for printing the data in the currently selected tab.

Select File»Export Document to export the data in the currently selected tab and launch the Export Document dialog box, in which you can select the file format for the exported data.

Parent topic:

Database Viewer Application

<!--NI_TOPIC bundle=teststand path=privileges.html language=enus -->
## TOPIC 00699: Privileges

- bundle_id: `teststand`
- source_path: `privileges.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/privileges.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The TestStand User Manager stores user and group privileges as Boolean properties and organizes the privileges in the following categories: Operate—Privileges for executing sequences and terminating and aborting executions. Debug—Privileges for controlling execution flow, executing manual and intera

### Privileges

The TestStand User Manager stores user and group privileges as Boolean properties and organizes the privileges in the following categories:

- Operate —Privileges for executing sequences and terminating and aborting executions.
- Debug —Privileges for controlling execution flow, executing manual and interactive executions, and editing station global variables and run-time variables.
- Develop —Privileges for editing and saving sequence files, editing and saving workspace files, and using source code control.
- Configure —Privileges for editing process model files and configuring station options, users, adapters, application settings, and report, database logging, and model options.
- Custom —Custom privileges you define. Customize the NI_UserCustomPrivileges data type to add new privileges.

You can grant all privileges in a specific category for each user or group in the user manager, and you can grant specific privileges for each user or group. In addition, when you add a user as a member of a group, TestStand grants the user all the privileges of the group. TestStand grants a privilege to a user or group when the property value for the privilege is True or when the value of the GrantAll property in any enclosing parent privilege category is True. For example, a user has the privilege to terminate an execution when one of the following properties is True:

- <User>.Privileges.Operate.Terminate
- <User>.Privileges.Operate.GrantAll
- <User>.Privileges.GrantAll
- <Group>.Privileges.Operate.Terminate
- <Group>.Privileges.Operate.GrantAll
- <Group>.Privileges.GrantAll

Note

Privileges

GrantAll

Privileges.GrantAll

GrantAll

True

GrantAll

False

TestStand also grants all privileges to a user when you disable privilege checking on the User Manager tab of the Station Options dialog box.

Parent topic:

Managing Users

<!--NI_TOPIC bundle=teststand path=process-model-architecture.html language=enus -->
## TOPIC 00700: Process Model Architecture

- bundle_id: `teststand`
- source_path: `process-model-architecture.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/process-model-architecture.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: To better understand the information in this section, familiarize yourself with process models, entry points, and the relationship between a process model and a client sequence file. The Sequential, Parallel, and Batch process models use the same basic structure for running a test sequence. Using th

### Process Model Architecture

To better understand the information in this section, familiarize yourself with process models, entry points, and the relationship between a process model and a client sequence file.

The Sequential, Parallel, and Batch process models use the same basic structure for running a test sequence. Using the Test UUTs or Single Pass Execution entry point, the process models run test sequences, generate reports, and log unit under test (UUT) results to a database according to configuration settings, as shown in the following figure.

[IMAGE alt='image' src='GUID-4409553B-174B-4838-96CC-993662F3247B-a5.svg']

The main differences between the process models are the number of UUTs each process model runs for the Test UUTs or Single Pass Execution entry points and the way each process model relates to and synchronizes with UUTs.

Note

Note

Parent topic:

Fundamentals

Related concepts:

- Process Models
- Entry Points
- Main Sequence and Client Sequence File
- Sequential Process Model
- Parallel Process Model
- Batch Process Model
- Database Logging
- Process Model Plug-In Architecture

<!--NI_TOPIC bundle=teststand path=process-model-changes-in-teststand-2012-or-la.html language=enus -->
## TOPIC 00701: Process Model Changes in TestStand 2012 or Later and the Migration Utility

- bundle_id: `teststand`
- source_path: `process-model-changes-in-teststand-2012-or-la.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/process-model-changes-in-teststand-2012-or-la.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The TestStand 2012 or later process models include significant changes to implement a plug-in architecture for model sequence files. TestStand 2012 or later uses the plug-in mechanism to decouple result processing from the process models. As part of this change, the result processing options in Test

### Process Model Changes in TestStand 2012 or Later and the Migration Utility

TestStandModelReportOptions.ini

TestStandDatabaseOptions.ini

ResultProcessing.cfg

<TestStand Application Data>

\Cfg\ModelPlugins

Note

ReportOptions

DatabaseOptions

Use the following migration actions in the utility to migrate the result processing configuration options from TestStand 2010 SP1 or earlier installed on the computer to the current version of TestStand:

- Apply to new models —Creates a new configuration in a configuration set named Migrated from TestStand Version . The utility automatically selects a unique name for the configuration if the utility has already used the default name in a previously completed migration. Refer to the migration report for the specific configuration names the utility uses.
- Apply to legacy models —Copies the options files from TestStand 2010 SP1 or earlier to the current TestStand directory so you can use the previous configurations with the equivalent legacy TestStand 2010 process models in TestStand 2012 or later. When you migrate database options, the utility renames TestStandDatabaseOptions.ini to TestStandDatabaseSchemas.ini .
- Apply to new and legacy models —Adds a new configuration in the Migrated from TestStand Version configuration set and copies the options files from TestStand 2010 SP1 or earlier.

Note

ModelSupport.seq

ModelSupport.seq

Parent topic:

TestStand Migration Utility

Related concepts:

- Search Directories

Related tasks:

- Manually Migrating Result Processing Options from Any Version of TestStand

<!--NI_TOPIC bundle=teststand path=process-model-plug-in-architecture.html language=enus -->
## TOPIC 00702: Process Model Plug-In Architecture

- bundle_id: `teststand`
- source_path: `process-model-plug-in-architecture.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/process-model-plug-in-architecture.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: To better understand the information in this section, NI recommends that you familiarize yourself with the Process Models and the Process Model Architecture topics. TestStand 2012 or later process models use sequence files called process model plug-ins to process test results and create result files

### Process Model Plug-In Architecture

To better understand the
 information in this section, NI recommends that you familiarize yourself with the
 Process Models and the Process Model Architecture topics.

TestStand 2012 or
 later process models use sequence files called process model plug-ins to process
 test results and create result files. Each plug-in contains sequences TestStand
 calls during process model execution to accomplish results processing tasks, such as
 report generation and database logging tasks. TestStand includes built-in plug-ins
 to handle report generation, database logging, and raw result logging. You can
 create custom process model plug-ins to extend or modify the functionality of the
 TestStand process models without changing the TestStand process model files
 directly.

The TestStand 2012 or later process models include significant
 changes to implement a plug-in architecture for model sequence files. You can use
 the to achieve the following functionality:

- Decouple result processing, which includes report generation and database
 logging, from the process models to simplify the model files and sequence
 files
- More easily customize report generation and database logging functionality
 without having to modify the process model files and vice versa
- Output multiple reports and log to multiple databases
- Increase throughput by creating reports or logging data asynchronously to test
 execution
- Log result data in a fast and compact raw result format for at a time other than
 when sequence execution occurs or on a different computer

The following image illustrates the modular approach the TestStand 2012 or later
 process models use to interact with result processing model plug-ins. Because of the
 additional layers the process model plug-in architecture introduces, you can make
 changes to result processing functionality by modifying only the process model
 plug-in code or by creating a new custom process model plug-in without modifying the
 process model itself.

[IMAGE alt='image' src='GUID-3A3FCADA-0F70-4893-A602-D6265EE26355-a5.svg']

Although the TestStand 2012 or later process model plug-in
 architecture contains additional layers of abstraction between the process model and
 the actual result processing code, the underlying components that implement report
 generation and database logging are similar to the TestStand 2010 or earlier
 components. Even though some changes exist among the versions of the components, the
 TestStand 2012 or later components are compatible with the TestStand 2010 and 2012
 process models.

#### Similarities between the TestStand
 2012 or Later and TestStand 2010 Process Models

The TestStand 2012 or
 later process models maintain the following similarities with respect to the
 TestStand 2010 or earlier process model files:

- The same sequences and DLLs implement core functionality for report generation
 and database logging
- Report generation and database logging configuration options do not
 significantly change
- Callbacks defined in the process model file implement UUT & Serial Number
 tracking
- The modelsupport2.dll implements process model dialog
 boxes

#### Differences between the TestStand
 2012 or Later and TestStand 2010 Process Models

Although many similarities
 exist, the TestStand 2012 or later process models include the following significant
 architecture differences:

- Process model plug-ins, not process model files, implement result
 processing
- Subsequences contain process model Execution Entry point functionality
- Modified existing components support the process model plug-in architecture

If you encounter an incompatibility in an existing test system when you use the
 TestStand 2012 or later process models or other circumstances prevent you from using
 the TestStand 2012 or later process models, you can use the equivalent legacy
 TestStand 2010 process models. You can use the Legacy Model Switcher tool to replace
 the TestStand 2012 or later process models with equivalent legacy TestStand 2010
 process models.

Note

- If you migrate a custom legacy process model file to TestStand 2012, you
 must also migrate the corresponding ModelSupport.seq file
 from the earlier version of TestStand, or you must use the equivalent legacy
 TestStand 2010 process models, which include a legacy
 ModelSupport.seq file.
- This document reflects only the TestStand 2012 or later process models. If
 you are using the equivalent legacy TestStand 2010 process models, refer to
 the TestStand 2010 documentation for information about those process
 models.

#### Result Processing
 Improvements

You can use the built-in reporting, database, and offline
 results process model plug-ins to generate reports, log data to databases, and store
 results in compact offline result files for processing later, respectively. You can
 also create custom result processing plug-ins.

You can create multiple result
 processing configurations, which are named sets of instances of plug-ins you
 configure to accomplish a specific task, such as creating multiple reports with
 different formats or logging data to multiple databases. Creating multiple report
 processing configurations to use as the active configuration can help you quickly
 change how TestStand processes results. You can create result processing
 configurations to process results inline, meaning at run time, or offline. For
 example, you can specify to process offline results differently from inline results
 or you can specify to process offline result files differently when you store the
 files in different locations.

Select Configure»Result
 Processing to launch the default Result Processing dialog box, in
 which you enable or disable the installed built-in and custom result processing
 plug-ins in the active result processing configuration and also configure how the
 plug-ins process test results. You can insert multiple instances of the same plug-in
 with various configuration options.

#### TestStand Offline Results Processing
 Utility

You can use the TestStand Offline Results Processing Utility to
 process raw results files and generate reports at a time other than when sequence
 execution occurs or on a different computer,such as in situations in which
 performance is more important than generating immediate reports.

Parent topic:

Process Model Architecture

Related concepts:

- Process Models
- Process Model Architecture
- Creating Process Model Plug-ins
- Dynamically Set the Client Sequence File
- Migrating Process Model Customizations to TestStand 2012 or Later

<!--NI_TOPIC bundle=teststand path=process-model-support-files.html language=enus -->
## TOPIC 00703: Process Model Support Files

- bundle_id: `teststand`
- source_path: `process-model-support-files.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/process-model-support-files.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Many sequences in the TestStand process model files call functions in DLLs and subsequences in other sequence files. The following table lists the process model support files TestStand installs in the <TestStand>\Components\Models\TestStandModels directory. File Name Description ATMLSupport.dll DLL

### Process Model Support Files

Many sequences in the TestStand process model files call functions in DLLs and subsequences in other sequence files. The following table lists the process model support files TestStand installs in the <TestStand>\Components\Models\TestStandModels directory.

| File Name | Description |
| --- | --- |
| ATMLSupport.dll | DLL that contains C functions the process model sequences call to generate ATML reports. |
| ATMLSupport.lib | Import library for ATMLSupport.dll. |
| banners.c | C source for functions that display status banners. |
| BatchModel.seq | Entry point and Model callbacks for the Batch process model. |
| batchuutdlg.c | C source for the functions that launch the UUT Information dialog box for the Batch process model. The modelsupport2.dll includes this file, but the default process model, SequentialModel.seq, does not call this file. |
| c_report.c | C source for generating XML, HTML, and ASCII text reports for the DLL option in the Select a Report Generator for Producing the Report Body section of the Contents tab of the Report Options dialog box. The NI_ReportGenerator.seq model plug-in calls this code. |
| ColorselectPopup.c | C source for the functions that launch a dialog box in which you can select a color. |
| ColorSelectPopup.h | C header file that contains declarations for the function in ColorselectPopup.c. |
| main.c | C source for utility functions. |
| ManagedModelSupport.dll | An assembly that contains utility methods process models call. |
| ModelOptions.c | C source for the functions that launch the Model Options dialog box and read and write the model options from and to disk. |
| modelpanels.h | C header file that contains declarations for the panels in modelpanels.uir. |
| modelpanels.uir | LabWindows/CVI user interface resource file that contains panels the functions in modelsupport2.dll use. |
| ModelSupport.seq | A sequence file that contains utility sequences process models call. |
| modelsupport2.dll | DLL that contains C functions the process model sequences call. Includes functions that launch the Report Options and Model Options dialog boxes, read and write those options from and to disk, determine the report file pathname, obtain the UUT serial number from the operator, and display status banners. You must use the LabWindows/CVI Full Development System with the Interface to Win32 API feature installed to rebuild this DLL. |
| modelsupport2.fp | LabWindows/CVI function panels for the functions in modelsupport2.dll. |
| modelsupport2.lib | Import library in Microsoft Visual C/C++ format for modelsupport2.dll. |
| modelsupport2.prj | LabWindows/CVI project that builds modelsupport2.dll and modelsupport2.cws. |
| NI_ResultsProcessorTemplate.seq | A template sequence file the Result Processing dialog box copies when end users create a new result processing model plug-in. |
| ParallelModel.seq | Entry point and Model callbacks for the Parallel process model. |
| paralleluutdlg.c | C source for the functions that launch the UUT Information dialog box for the Parallel process model. The modelsupport2.dll includes this file, but the default process model, SequentialModel.seq, does not call this file. |
| PropertyObject.xsd | XML schema that defines the contents of the XML the PropertyObject.GetXML method generates and the PropertyObject.SetXML method requires. TestStand XML reports that Report.xsd defines also use PropertyObject.xsd. |
| report.c | C source for functions that launch the Report Options dialog box, read and write the report options from and to disk, and determine the report file pathname. The NI_ReportGenerator.seq model plug-in calls these sequences. |
| report.h | C header file that contains declarations for the functions in report.c. |
| Report.xsd | XML schema that defines the contents of TestStand XML reports. |
| reportgen_atml.seq | Subsequences that add the header, result entries, and footer for a UUT to an ATML report. The NI_ReportGenerator.seq model plug-in calls these subsequences. |
| reportgen_html.seq | Subsequences that add the header, result entries, and footer for a UUT to an HTML report. The NI_ReportGenerator.seq model plug-in calls these subsequences. |
| reportgen_txt.seq | Subsequences that add the header, result entries, and footer for a UUT to an ASCII text report. The NI_ReportGenerator.seq model plug-in calls these subsequences. |
| reportgen_xml.seq | Subsequences that add the header, result entries, and footer for a UUT to an XML report. The NI_ReportGenerator.seq model plug-in calls these subsequences. |
| ResultProcessing.c | C source for functions that launch the Result Processing dialog box and read and write the process model plug-in configuration files from and to disk. |
| ResultProcessing.h | C header file that contains declarations for the functions in ResultProcessing.c. |
| SequentialModel.seq | Entry point and Model callbacks for the Sequential process model. |
| uutdlg.c | C source for the function that launches the UUT Information dialog box to obtain the UUT serial number from the operator. |

You can view the contents of the reportgen_atml.seq, reportgen_xml.seq, reportgen_html.seq, and reportgen_txt.seq files in the TestStand Sequence Editor. These files are model sequence files and contain an empty ModifyReportEntry callback you can override with a client sequence file. Each reportgen sequence file includes a PutOneResultInReport sequence that calls the ModifyReportEntry callback.

The TestStand process model sequence files also contain an empty ModifyReportEntry callback, even though no sequences in the process model sequence files call the ModifyReportEntry callback directly. The files contain a ModifyReportEntry callback so that the ModifyReportEntry callback appears in the Sequence File Callbacks dialog box for the client sequence file.

Parent topic:

Process Model Architecture

Related concepts:

- TestStand Directory Structure
- ATML
- Batch Process Model
- Parallel Process Model
- Sequential Process Model
- Model Callbacks in the Sequential Process Model
- Report Generation Functions and Sequences

<!--NI_TOPIC bundle=teststand path=process-model-thread-types.html language=enus -->
## TOPIC 00704: Process Model Thread Types

- bundle_id: `teststand`
- source_path: `process-model-thread-types.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/process-model-thread-types.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: A process model can call plug-in entry points from multiple threads. The Batch process model and the Parallel process model create a separate thread and execution for each test socket and create a controller thread and execution to coordinate the activity of the socket threads. A process model calls

### Process Model Thread Types

A process model can call plug-in entry points from multiple threads. The Batch process model and the Parallel process model create a separate thread and execution for each test socket and create a controller thread and execution to coordinate the activity of the socket threads. A process model calls some entry points from both socket and controller threads and other entry points only from socket threads or only from controller threads.

When a process model invokes a plug-in entry point, the model passes a parameter of type NI_ModelThreadType to the plug-in. The parameter includes the IsController and IsTestSocket Boolean subproperties. Plug-ins can use these subproperties to determine the type of model thread that invokes the plug-in. For example, a Begin entry point might perform a general operation when the controller thread invokes the entry point or a socket-specific operation when a socket thread invokes the entry point.

The Sequential process model creates only one thread that coordinates and performs testing, so the Sequential process model always sets the IsController and IsTestSocket subproperties to True.

Plug-in instance properties that update at run time are called run-time variables. A plug-in uses the following subproperties to store run-time variables specific to the plug-in:

- <NI_ModelPlugin>.PluginSpecific.RuntimeVariables of type <plug-in name> RuntimeVariables
- <NI_ModelPlugin>.PluginSpecific.RuntimeVariables.PerSocket of type array of <plug-in name> PerSocketRuntimeVariables

The process model sets the PerSocket property array to have one element for each test socket. Therefore, you can add a property to the <plug-in name>PerSocketRuntimeVariables data type to create a run-time variable that has a separate value for each socket thread.

When you use the Batch or Parallel process models to invoke a plug-in, the plug-in executes as a
 multithreaded sequence because the model invokes plug-in entry points in the
 controller thread and the socket threads. Therefore, you can access properties of
 the plug-in instance from multiple threads in parallel. TestStand ensures that read
 and write operations to TestStand property values and array element values are
 atomic. However, NI recommends that you use the following strategies to ensure that
 different threads safely share access to plug-in instance variables:

- Add run-time variables only to the <plug-in name> RuntimeVariables and <plug-in name> PerSocketRuntimeVariables data types.
- If a run-time variable must have a unique value for each test socket, add the variable to the <plug-in name> PerSocketRuntimeVariables data type.
- Use a TestStand lock or other synchronization method to ensure a thread has exclusive access to the plug-in run-time variables when required.

Parent topic:

Process Model Plug-In Architecture

Related concepts:

- Model Plug-in Entry Points
- Batch Controller and Test Socket Synchronization Architecture
- Avoid Batch Synchronization Sections in Process Model Plug-in Entry Points
- Thread Safety of the PropertyObject API and TestStand Variables

<!--NI_TOPIC bundle=teststand path=process-model-types.html language=enus -->
## TOPIC 00705: Process Model Types

- bundle_id: `teststand`
- source_path: `process-model-types.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/process-model-types.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Model plug-ins typically do not need to determine the type of process model that invokes the plug-in. However, plug-in entry points can inspect the ModelType subproperty of the ModelData parameter to determine the type of process model that invokes the plug-in. Possible values of the ModelType field

### Process Model Types

Model plug-ins typically do not need to determine the type of process model that invokes the plug-in. However, plug-in entry points can inspect the ModelType subproperty of the ModelData parameter to determine the type of process model that invokes the plug-in. Possible values of the ModelType field for the built-in process models include Sequential, Parallel, or Batch.

For example, if the value of the ModelType subproperty of the ModelData parameter is Batch, the built-in reporting model plug-in synchronizes its controller and socket threads to ensure it generates the batch report from the controller thread before generating UUT reports from test socket threads so that reports appear in the expected order when the threads write the reports to the same file.

Parent topic:

Process Model Plug-In Architecture

Related concepts:

- Model Plug-in Entry Points

<!--NI_TOPIC bundle=teststand path=process-models.html language=enus -->
## TOPIC 00706: Process Models

- bundle_id: `teststand`
- source_path: `process-models.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/process-models.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Testing a UUT requires more than just executing a set of tests. Usually, the test system must perform a series of operations before and after it executes the sequence that performs the tests. Common operations of the process model include identifying the UUT, notifying the operator of pass/fail stat

### Process Models

Testing a UUT requires more than just executing a set of tests. Usually, the test system must perform a series of operations before and after it executes the sequence that performs the tests. Common operations of the process model include identifying the UUT, notifying the operator of pass/fail status, logging results, and generating reports. The set of operations and the flow of execution is called a process model. A TestStand process model is a sequence file you can use to define standard testing operations so you do not have to re-implement the same operations in every sequence file you write.

TestStand includes predefined Sequential, Parallel, and Batch models you can modify or replace. Use the Sequential model to run a test sequence on one UUT at a time. Use the Parallel and Batch models to run the same test sequence on multiple UUTs simultaneously.

You can modify an existing TestStand process model or you can create a custom process model. The ability to modify a process model is essential because the testing process can vary depending on production lines, production sites, or company systems and practices. You can edit a process model in the same way you edit other sequence files. You can also use client sequence files to customize various model operations by overriding the callback sequences process models define.

Parent topic:

TestStand Building Blocks

Related concepts:

- Configuring Logging to Custom Database
- TestStand Process Models
- Sequential Process Model
- Parallel Process Model
- Batch Process Model
- Modifying Process Model Sequence Files
- Process Model Architecture
- Process Model Plug-In Architecture
- Process Model Support Files

<!--NI_TOPIC bundle=teststand path=processing-files-for-deployment.html language=enus -->
## TOPIC 00707: Processing Files for Deployment

- bundle_id: `teststand`
- source_path: `processing-files-for-deployment.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/processing-files-for-deployment.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The TestStand Deployment Utility copies most files unmodified from the source directory to the image directory when you create a deployment. However, the deployment utility makes changes to some LabVIEW-based code modules and TestStand sequence files to ensure the files run correctly on the test sta

### Processing Files for Deployment

The TestStand Deployment Utility copies most files unmodified from the source directory to the image directory when you create a deployment. However, the deployment utility makes changes to some LabVIEW-based code modules and TestStand sequence files to ensure the files run correctly on the test station computer.

Enable the Include without Processing Item or Dependencies option on the Distributed Files tab of the deployment utility to force the deployment utility to copy the files unmodified from the source folder to the image folder, which can be appropriate when you include the following types of files in a deployment:

- Files with an associated checksum
- VIs compiled in a LabVIEW version other than the active version of LabVIEW
- Files you do not want the deployment utility to modify, such as LabVIEW user interface source files or support files
- LabVIEW NXG GLL binaries

Parent topic:

Creating Deployments

Related concepts:

- Processing LabVIEW Code Modules for Deployment
- Processing TestStand Sequence Files for Deployment

<!--NI_TOPIC bundle=teststand path=processing-labview-code-modules-for-deploymen.html language=enus -->
## TOPIC 00708: Processing LabVIEW Code Modules for Deployment

- bundle_id: `teststand`
- source_path: `processing-labview-code-modules-for-deploymen.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/processing-labview-code-modules-for-deploymen.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The TestStand Deployment Utility can make changes to VIs, projects, and project libraries when you create a deployment. VIs The deployment utility uses the active version of the LabVIEW Development System on the build computer to process code module VIs for a deployment. The deployment utility also

### Processing LabVIEW Code Modules for Deployment

The TestStand Deployment Utility can make changes to VIs, projects, and project libraries when you create a deployment.

#### VIs

The deployment utility
 uses the active version of the LabVIEW Development System on the build computer to
 process code module VIs for a deployment. The deployment utility also builds a list
 of dependencies to include in the deployment. However, if you use the VI Server to
 call VIs dynamically, you must manually add the VIs to the deployment because the
 deployment utility cannot automatically include VIs you call dynamically.

Code
 module dependencies can include subVIs, VIs in vi.lib,
 non-operating system DLLs, external subroutines, amd run-time menus. The deployment
 utility includes these dependencies in the deployment to ensure that the code
 modules execute correctly on test station computers. For example, test station
 computers typically use only the LabVIEW Run-Time Engine (RTE), which does not
 include vi.lib. Deploying code module VIs that call
 vi.lib VIs to a test station computer with only the LabVIEW RTE
 installed without using the deployment utility to first process the code module VIs
 results in broken VIs on the test station computer.

You can also configure the
 deployment utility to change other aspects of VIs, such as changing the destination
 of code module VIs and subVIs. Use the LabVIEW VI Options dialog box to modify the
 behavior of VIs in the deployment in the following ways:

- Output VIs to packed project libraries
- Remove block diagrams for all VIs
- Apply a new password to all VIs
- Check for broken VIs
- Remove unused polymorphic VIs
- Consolidate VIs that different LabVIEW projects share
- Exclude dependent VIs located in vi.lib ,
 user.lib , or instr.lib

#### LabVIEW Projects

If a TestStand sequence file executes VIs in the context of a LabVIEW project, the deployment utility applies the following changes to the copy of the LabVIEW project it includes in the deployment:

- Updates file path references in the LabVIEW project to correspond to the deployable image file paths
- Removes files from the LabVIEW project that the test system does not use
- Converts folders that LabVIEW automatically populates into static folders

#### LabVIEW Project Libraries

The deployment utility minimizes the size of the deployable image by creating a partial project library that does not include VIs from LabVIEW project libraries the test system does not use.

#### VIs that Call DLLs

You can use the deployment utility to build an installer that contains VIs that call into DLLs with dependencies, such as other DLLs or configuration files. Alternatively, you can call DLLs from a TestStand step.

For DLLs that VIs and TestStand steps call, the deployment utility automatically includes in the deployment the DLLs and the statically referenced dependencies of the DLLs. The deployment utility does not automatically include dynamically referenced dependencies or implicitly referenced dependencies. You can manually add the DLLs, the dynamically referenced dependencies, and the implicitly referenced dependencies to the TestStand workspace or to the directory from which you create the deployment to maintain the same file and directory structure on the test station computer so the DLL can correctly locate the dependencies in the test system you deploy.

Parent topic:

Processing Files for Deployment

Related concepts:

- Organizing Test Program Files with LabVIEW Project Libraries
- Using a Dedicated Build Computer
- Manually Adding or Removing Files to or from Deployments
- Customizing Components You Deploy
- Organizing Test Program Files with LabVIEW Packed Project Libraries
- Partial Project Libraries
- Deploying 32-bit TestStand and 64-bit TestStand Systems
- Deploying VIs in LabVIEW Packed Project Libraries
- Deploying VIs in LabVIEW Projects
- Deploying Stand-alone VIs
- Troubleshooting LabVIEW Code Module Issues

<!--NI_TOPIC bundle=teststand path=processing-labview-nxg-code-modules-for-deplo.html language=enus -->
## TOPIC 00709: Processing LabVIEW NXG Code Modules for Deployment

- bundle_id: `teststand`
- source_path: `processing-labview-nxg-code-modules-for-deplo.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/processing-labview-nxg-code-modules-for-deplo.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: TestStand Deployment Utility supports deploying sequence files which call LabVIEW NXG code modules. LabVIEW NXG steps can be configured in the following ways: Project and GLL are Both Specified— These steps can execute using the LabVIEW NXG development system to execute the VI directly, or using the

### Processing LabVIEW NXG Code Modules for Deployment

TestStand Deployment Utility supports deploying sequence files which call LabVIEW NXG code modules. LabVIEW NXG steps can be configured in the following ways:

- Project and GLL are Both Specified — These steps can execute using the LabVIEW NXG development system to execute the VI directly, or using the LabVIEW NXG Run-Time Engine to execute the VI within the GLL. In this case, TestStand enforces that the specified GLL must match the GLL output configured in the project and component in LabVIEW NXG. When deploying these types of steps, TestStand Deployment Utility automatically regenerates the GLL from the project before deploying to ensure that the latest code is used.
- GLL Specified, Project Not Specified — These steps must be executed using the LabVIEW NXG Run-Time Engine to execute the VIs built into the GLL. When deploying these types of steps, the GLL file is deployed as-is because no source files are present to rebuild it.
- Project Specified, GLL Not Specified — These steps can execute using the LabVIEW NXG Development System to execute the VI directly. Deployment is not supported for these steps by TestStand Deployment Utility. An error is generated indicating that a GLL is required.

Note

#### Configuring LabVIEW NXG Files

After analyzing a sequence with LabVIEW NXG code modules, the referenced GLLs are displayed in the distributed files tab. You can configure the destination for the GLL file. Like other code module types, TestStand Deployment Utility ensures that the sequence file is updated to reference the correct files if the files are deployed within the same base destination as the calling sequence file.

To include LabVIEW NXG source files in the deployment, click LabVIEW options, and select the LabVIEW NXG options tab. Enable the Include LabVIEW NXG Source Files option. With this option selected, LabVIEW NXG projects, components, and VIs will also be displayed in the distributed files tab. Only referenced files are displayed in the distributed files tab, but all files included in the project will be included in the deployment. You can configure the destination for the source project, but not for contained components and VIs; these files will be deployed to a location relative to the project.

#### Deploying the LabVIEW NXG Run-Time
 Engine in an MSI-based Installer

Because the LabVIEW NXG Run-Time Engine
 is a NI package it is not directly available as a dependency in an MSI-based
 installer. However, if you enable the Automatically Include Required
 Installers option in the Drivers and Components dialog, TestStand
 Deployment Utility will include the Run-Time Engine package within the installer
 folder. When the installer is executed, it will invoke NI Package Manager to install
 the Run-Time Engine package.

Parent topic:

Processing Files for Deployment

<!--NI_TOPIC bundle=teststand path=processing-net-deployment.html language=enus -->
## TOPIC 00710: Processing .NET Code Modules for Deployment

- bundle_id: `teststand`
- source_path: `processing-net-deployment.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/processing-net-deployment.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: If you are using TestStand 2024 Q4 or later, you must manually add .NET code modules and support files, like runtimeconfig.json and deps.json files, when creating deployments that call .NET assemblies. You must manually add .NET code module files to your deployments for both: deployments that call .

### Processing .NET Code Modules for
 Deployment

If you are using TestStand 2024 Q4 or later, you must manually add .NET code modules and
 support files, like runtimeconfig.json and
 deps.json files, when creating deployments that call .NET
 assemblies.

- deployments that call .NET code using the .NET Adapter, and
- deployments that include other files, like VIs, that call .NET code during their
 operation.

Note

Parent topic:

Processing Files for Deployment

<!--NI_TOPIC bundle=teststand path=processing-teststand-sequence-files-for-deplo.html language=enus -->
## TOPIC 00711: Processing TestStand Sequence Files for Deployment

- bundle_id: `teststand`
- source_path: `processing-teststand-sequence-files-for-deplo.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/processing-teststand-sequence-files-for-deplo.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The TestStand Deployment Utility replaces absolute file path references with relative file path references because the location of files on a development computer might be different from the paths on the test station computer. For example, on the development computer, you might save files in the C:\

### Processing TestStand Sequence Files for Deployment

The TestStand Deployment Utility replaces absolute file path references with relative file path references because the location of files on a development computer might be different from the paths on the test station computer. For example, on the development computer, you might save files in the C:\Dev\TestSystem directory but install files on the test station computer in the C:\<Program Files>\TestSystem directory.

The deployment utility updates absolute path references in sequence files to use relative path references that initiate from one of the following search directories:

- Current sequence file directory
- <TestStand>
- Windows\System32
- Windows
- <TestStand Public>

When the code module file you reference does not exist in one of these search directories, the deployment utility does not update the absolute paths. Therefore, the test sequence might not execute correctly on the test station computer.

The deployment utility also updates paths to code modules if you change the destination of code module files. For example, if a code module and its calling sequence file exist in the same source files directory but you change the destination directory for the code module to a subdirectory, the deployment utility updates the sequence file to use the new path to the code module when you create the deployment.

When you output VIs to packed project libraries, the deployment utility updates all appropriate steps in the sequence file to use the correct VI path and namespace.

Note

Parent topic:

Processing Files for Deployment

Related concepts:

- Search Directories
- TestStand Directory Structure
- Organizing Test Program Files with LabVIEW Packed Project Libraries
- Deploying 32-bit TestStand and 64-bit TestStand Systems

<!--NI_TOPIC bundle=teststand path=profiler-window-graphs.html language=enus -->
## TOPIC 00712: Profiler Window Graphs

- bundle_id: `teststand`
- source_path: `profiler-window-graphs.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/profiler-window-graphs.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Profiler Window Graphs The tabs in the top half of the Execution Profiler window display the following graphs: Item Usage per Thread Thread Usage per Item Select an operation or row in the graph to display it in the Operations or Threads table below the graph. When you change the selection and focus

### Profiler Window Graphs

#### Profiler Window Graphs

The tabs in the top half of the Execution Profiler window display the following graphs:

- Item Usage per Thread
- Thread Usage per Item

Select an operation or row in the graph to display it in the Operations or Threads table below the graph. When you change the selection and focus in a table, the selection and focus also change in the graphs when applicable.

The red portion of an operation indicates the time during which the thread blocks waiting to acquire an item. The green portion of an operation indicates the time during which the thread owns or uses an item. While an operation is blocked, its frame is red. While an operation is in use, its frame is blue. After an operation completes, its frame is black.

Select Edit»Copy to copy the entire image of the graph to the clipboard, including the portions of the graph that are not visible because of the scroll position.

The profiler window graphs include the following controls:

- Zoom % —Controls the amount of horizontal space a given unit of time occupies on the time line. Increase the value to increase the display size of the operations. Use the horizontal scrollbar when the operations require more horizontal space than is available.
- Auto Fit —Select Auto Fit to adjust the time scale so all operations fit horizontally within the graph, if possible. Deselect Auto Fit to enable the Zoom % control. 

 Note 

 If a graph has focus, you can zoom in or out using ctrl-mouse-wheel. If the mouse cursor is over the graph, the graph zooms based on the mouse cursor location. You can also choose the Zoom to Selection command from the View menu.

You can drag a bounding box around operations in a graph to select them. You can extend or modify the selection by shift or ctrl clicking on additional operations. The graphs display ruler lines at the start and end of the selection so that you can more easily observe the relative positions of other operations.

- [Item Usage per Thread Graph](item-usage-per-thread-graph.html)
- [Thread Usage per Item Graph](thread-usage-per-item-graph.html)

Parent topic:

Execution Profiler

<!--NI_TOPIC bundle=teststand path=programmatically-displaying-and-configuring-t.html language=enus -->
## TOPIC 00713: Programmatically Displaying and Configuring the Profiler

- bundle_id: `teststand`
- source_path: `programmatically-displaying-and-configuring-t.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/programmatically-displaying-and-configuring-t.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Programmatically Displaying and Configuring the Profiler There is at most one profiler per TestStand application process. Accessing any static method or property of the class NationalInstruments.TestStandProfiler.Profiler from the <TestStand>\Tools\Profiler\$(Platform)\Profiler.dll assembly, except

### Programmatically Displaying and Configuring the Profiler

#### Programmatically Displaying and Configuring the Profiler

There is at most one profiler per TestStand application process. Accessing any static method or property of the class NationalInstruments.TestStandProfiler.Profilerfrom the <TestStand>\Tools\Profiler\$(Platform)\Profiler.dll assembly, except for the Close() method and the IsOpen property, automatically creates the profiler if needed before performing the specified action. Call the Close() method to close the profiler window and discard its data. The Comparing Resource Usage Strategies.seq file in the <TestStand>\Examples\Parallel Testing\Comparing Resource Usage Strategies directory contains a SequenceFileLoad callback sequence that contains example steps that launch and configure the profiler.

The Profiler enables you to programmatically:

- Load and Save profiler data
- Clear the profiler window
- Specify what types of information the profiler collects and displays
- Start of stop data collection and data display
- Activate, select data, and copy information from a specified table or graph
- Set other options, such as time units, window size and position, and splitter bar location

For example, to isolate a section of your sequence for profiling, you might insert a step before the section that sets Profiler.DataCollectionEnabled and a step at the end of the section, which clears Profiler.DataCollectionEnabled.

Note

Parent topic:

Execution Profiler

Related concepts:

- Search Directories

Related information:

- Execution Profiler Window

<!--NI_TOPIC bundle=teststand path=programmatically-updating-a-configuration-fil.html language=enus -->
## TOPIC 00714: Programmatically Updating a Configuration File

- bundle_id: `teststand`
- source_path: `programmatically-updating-a-configuration-fil.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/programmatically-updating-a-configuration-fil.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: If you deploy a new model plug-in to an existing TestStand installation and you want to automatically add an instance of the new plug-in to an existing configuration file, call the AddResultProcessingPluginToConfiguration or AddModelPluginToConfiguration functions in ModelSupport2.dll as defined in

### Programmatically Updating a Configuration File

If you deploy a new model plug-in to an existing TestStand installation and you want to automatically add an instance of the new plug-in to an existing configuration file, call the AddResultProcessingPluginToConfiguration or AddModelPluginToConfiguration functions in ModelSupport2.dll as defined in ResultProcessing.h located in the <Teststand>\Components\Models\TestStandModels directory.

You can call RemoveResultProcessingPluginFromConfiguration or RemoveModelPluginFromConfiguration to remove instances of a plug-in from a configuration file.

If you want to make arbitrary edits to an existing configuration file, you can load and save the file with the PropertyObjectFile interface. You can paste the following expression into a Statement step to create an example of how to modify a configuration file:

Locals.File = RunState.Engine.NewPropertyObjectFile(FileType_PropertyObjectFile), // don't forget to create Locals.File as an Object Reference variable

Locals.File.AsPropertyObjectFile.Path = RunState.Engine.GetTestStandPath(TestStandPath_Config) + "\\ModelPlugins\\ResultProcessing.cfg",

Locals.File.AsPropertyObjectFile.ReadFile(ConflictHandler_Error), // load the configuration file

// add expressions to change values as desired under: Locals.File->Data.ModelPluginConfigurationSet

Locals.File.AsPropertyObjectFile.WriteFile(WriteFileFormat_Current) // write back any changes to the configuration file

Parent topic:

Configuring Process Model Plug-ins

Related concepts:

- TestStand Directory Structure

<!--NI_TOPIC bundle=teststand path=programming-with-the-teststand-api-in-csharp.html language=enus -->
## TOPIC 00715: Programming with the TestStand API in C#

- bundle_id: `teststand`
- source_path: `programming-with-the-teststand-api-in-csharp.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/programming-with-the-teststand-api-in-csharp.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: In C#, you can access the TestStand ActiveX API by adding the NationalInstruments.TestStand.Interop.API component as a reference in a project. To add a reference to the TestStand 4.0 or later API assembly in Visual Studio, select the project in the Solution Explorer. Select Project»Add Reference to

### Programming with the TestStand API in C#

In C#, you can access the TestStand ActiveX API by adding the NationalInstruments.TestStand.Interop.API component as a reference in a project.

To add a reference to the TestStand 4.0 or later API assembly in Visual Studio, select the project in the Solution Explorer. Select Project»Add Reference to launch the Reference Manager dialog box. Click Assemblies»Extensions and select the TestStand <Version> <APIName> Interop Assembly component from the list. Click OK to close the Reference Manager dialog box. Then, expand the References node for the project in the Solution Explorer, right-click the new reference and select Properties from the context menu. In the Properties panel, change the Embed Interop Types setting to False. If this setting is True, using any constants such as PropertyOptions in your code will result in compiler errors

If the TestStand Interop assemblies do not appear in the Reference Manager dialog box, exit all running copies of Visual Studio, launch the TestStand Version Selector, select the current version of TestStand, and click the Make Active button.

After you add the NationalInstruments.TestStand.Interop.API component as a reference in a project, add the following directive at the top of the source file:

using NationalInstruments.TestStand.Interop.API;

All TestStand classes, methods, and properties are available in the Microsoft Visual Studio object browser and are accessible from the C# source code. Help text for classes, methods, and properties appears in Microsoft IntelliSense.

To control NI instruments from a .NET assembly, you must also complete the following tasks:

- Install the appropriate NI driver for the instrument you want to control. Ensure you install the correct NI .NET API for the version of the NI driver you installed. For some NI drivers, you must manually select .NET support options in the installer.
- Add a reference to the corresponding NI driver .NET API assembly to the project. The TSM
 Accelerometer with .NET and the Part Average Testing with .NET examples include
 Visual Studio projects that reference the TSM Code Module API and some NI .NET
 APIs and demonstrate how to invoke those APIs. Refer to the TestStand
 Semiconductor Module Manual for more information about these
 examples.

Visit ni.com/info and enter the Info Code NETAPIdriversupport for information about the available NI .NET APIs and the versions of the NI drivers each supports.

#### Upgrading TestStand

When you upgrade to a full, non-service pack version of TestStand and you want to continue to use existing code modules and applications in the later version, you must update the .NET assembly references in Visual Studio projects. The assemblies you build using TestStand APIs are compatible only with the version of TestStand, including service packs, you reference in Visual Studio projects.

#### Upgrading Instrument Drivers

When you upgrade to a later version of an instrument driver .NET API, you do not need to update the .NET assembly references in Visual Studio projects. NI instrument driver .NET API installers ensure that references to earlier versions of the instrument driver .NET API assembly are automatically redirected to the current version of the assembly if the earlier version assembly does not exist.

Parent topic:

Programming with the TestStand API in Different Languages

Related concepts:

- TestStand API Concepts
- .NET Support for the TestStand API

Related information:

- TestStand Semiconductor Module Manual

<!--NI_TOPIC bundle=teststand path=programming-with-the-teststand-api-in-cvi.html language=enus -->
## TOPIC 00716: Programming with the TestStand API in LabWindows/CVI

- bundle_id: `teststand`
- source_path: `programming-with-the-teststand-api-in-cvi.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/programming-with-the-teststand-api-in-cvi.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use the TestStand API or TestStand User Interface (UI) Controls from LabWindows/CVI code modules and user interface source code. Refer to the ActiveX Library topic of the LabWindows/CVI Online Help for fundamental information about ActiveX concepts and how to access ActiveX servers from LabW

### Programming with the TestStand API in LabWindows/CVI

You can use the TestStand API or TestStand User Interface (UI) Controls from LabWindows/CVI code modules and user interface source code.

Refer to the ActiveX Library topic of the LabWindows/CVI Online Help for fundamental information about ActiveX concepts and how to access ActiveX servers from LabWindows/CVI.

Parent topic:

Programming with the TestStand API in Different Languages

Related concepts:

- TestStand UI Controls
- Programming with the TestStand API in LabWindows/CVI

<!--NI_TOPIC bundle=teststand path=programming-with-the-teststand-api-in-htbasic.html language=enus -->
## TOPIC 00717: Programming with the TestStand API in HTBasic

- bundle_id: `teststand`
- source_path: `programming-with-the-teststand-api-in-htbasic.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/programming-with-the-teststand-api-in-htbasic.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: HTBasic uses a CSUB library TestStand provides to access the TestStand ActiveX API. The CSUB library contains HTBasic subroutines for the GetVal and SetVal methods in the TestStand API. Accessing Property Values in HTBasic You can access the values of built-in properties using Get and Set subroutine

### Programming with the TestStand API in
 HTBasic

HTBasic uses a CSUB library
 TestStand provides to access the TestStand ActiveX API. The CSUB library contains
 HTBasic subroutines for the GetVal and SetVal
 methods in the TestStand API.

#### Accessing Property Values in
 HTBasic

You can access the values of built-in properties using
 Get and Set subroutines in the TestStand API
 CSUB library. The name of each Get or Set
 subroutine starts with Getval or Setval, followed
 by the data type name.

Note

| Function Name | TestStand Type | HTBasic type |
| --- | --- | --- |
| Getvalnumber | Number | REAL |
| Setvalnumber | Number | REAL |
| Getvalstring | String | STRING |
| Setvalstring | String | STRING |
| Getvalboolean | Boolean | INTEGER |
| Setvalboolean | Boolean | INTEGER |
| Getvalnumarray | Array of Number | Array of REAL |
| Setvalnumarray | Array of Number | Array of REAL |
| Getvalstrarray | Array of String | Array of STRING |
| Setvalstrarray | Array of String | Array of STRING |

```text
SUB Test
 
REAL Realnum
CALL Getvalnumber("Step.Limits.High",0,Realnum)
CALL Setvalnumber("Step.Result.Numeric",0,Realnum)
 
SUBEND
```

#### Using Strings in
 HTBasic

You must choose HTBasic string variables that are large enough to
 contain the string property values from TestStand. If the HTBasic variable is not
 large enough, TestStand truncates the value of the string you obtain.

Note

#### Using Arrays in HTBasic

You
 can use the CSUB library subroutines to exchange one- or two-dimensional arrays
 between TestStand and HTBasic. When retrieving an array from TestStand, you must
 choose HTBasic array variables as large as the TestStand array. If the HTBasic array
 is smaller, TestStand returns the ERROR 16 Improper or Inconsistent Dimensions
 error.

```text
SUB Test2dstr
 
DIM Strings$ (2, 5) [30]
CALL Getvalstrarray ("Local.StringArray2",1,Strings$ (*) )
 
SUBEND
```

The following example shows the equivalent TestStand declaration for the numeric
 array, assuming that the HTBasic OPTION BASE is zero: StringArray2 Array of
 Strings [0 .. 2] [0 . . 5]

Parent topic:

Programming with the TestStand API in Different Languages

Related concepts:

- Accessing Arrays Using API - HTBasic
- Accessing Properties Using API

<!--NI_TOPIC bundle=teststand path=programming-with-the-teststand-api-in-labview.html language=enus -->
## TOPIC 00718: Programming with the TestStand API in LabVIEW

- bundle_id: `teststand`
- source_path: `programming-with-the-teststand-api-in-labview.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/programming-with-the-teststand-api-in-labview.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use the TestStand API or TestStand User Interface (UI) Controls from LabVIEW test and user interface VIs. Refer to the LabVIEW documentation for more information about ActiveX concepts and how to use LabVIEW as an ActiveX client.

### Programming with the TestStand API in LabVIEW

You can use the TestStand API or TestStand User Interface (UI) Controls from LabVIEW test and user interface VIs.

Refer to the LabVIEW documentation for more information about ActiveX concepts and how to use LabVIEW as an ActiveX client.

Parent topic:

Programming with the TestStand API in Different Languages

Related concepts:

- TestStand UI Controls
- Programming with the TestStand API in LabVIEW

<!--NI_TOPIC bundle=teststand path=programming-with-the-teststand-api-msvb.html language=enus -->
## TOPIC 00719: Programming with the TestStand API in Microsoft Visual Basic .NET

- bundle_id: `teststand`
- source_path: `programming-with-the-teststand-api-msvb.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/programming-with-the-teststand-api-msvb.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: In Microsoft Visual Basic .NET, you can access the TestStand ActiveX API by first adding the NationalInstruments.TestStand.Interop.API component as a reference in a project. To add a reference to the TestStand 4.0 or later API assembly in Visual Studio, select the project in the Solution Explorer. S

### Programming with the TestStand API in Microsoft Visual Basic .NET

In Microsoft Visual Basic .NET, you can access the TestStand ActiveX API by first adding the NationalInstruments.TestStand.Interop.API component as a reference in a project.

To add a reference to the TestStand 4.0 or later API assembly in Visual Studio, select the project in the Solution Explorer. Select Project»Add Reference to launch the Reference Manager dialog box. Click Assemblies»Extensions and select the TestStand <Version> <APIName> Interop Assembly component from the list. Click OK to close the Reference Manager dialog box. Then, right-click the project and select Properties, click the References tab, and select the new reference. In the Properties panel, change the Embed Interop Types setting to False. If this setting is True, using any constants such as PropertyOptions in your code will result in compiler errors

If the TestStand Interop assemblies do not appear in the Reference Manager dialog box, exit all running copies of Visual Studio, launch the TestStand Version Selector, select the current version of TestStand, and click the Make Active button.

After you add the NationalInstruments.TestStand.Interop.API component as a reference in a project, add the following directive at the top of the source file:

Imports NationalInstruments.TestStand.Interop.API

All TestStand classes, methods, and properties are available in the Microsoft Visual Studio object browser and are accessible from the Visual Basic .NET source code. Help text for classes, methods, and properties appears in Microsoft IntelliSense.

When you create a new project in a supported version of Visual Studio, you must set Project Properties»Build»Platform Target to x86 so the project can access the TestStand API and User Interface (UI) Controls on 64-bit versions of Microsoft Windows.

Parent topic:

Programming with the TestStand API in Different Languages

Related concepts:

- TestStand API Concepts
- .NET Support for the TestStand API

<!--NI_TOPIC bundle=teststand path=programming-with-the-teststand-api-msvc.html language=enus -->
## TOPIC 00720: Programming with the TestStand API in Microsoft Visual C++

- bundle_id: `teststand`
- source_path: `programming-with-the-teststand-api-msvc.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/programming-with-the-teststand-api-msvc.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: None Using #import You can use the #import compiler directive to automatically generate C++ classes for Microsoft Visual Studio to access the objects defined in TestStand type libraries. To generate C++ classes for TestStand, you must first add the <TestStand>\Bin directory to the list of additional

### Programming with the TestStand API in Microsoft Visual C++

None

#### Using #import

You can use the #import compiler directive to automatically generate C++ classes for Microsoft Visual Studio to access the objects defined in TestStand type libraries.

To generate C++ classes for TestStand, you must first add the <TestStand>\Bin directory to the list of additional include directories in the Visual C++ project settings.

TestStand adds TestStand API directories to the list of include directories that Microsoft Visual Studio uses to locate files.

In Visual Studio 2010 or later, enable the Enable TestStand Include Directories option on the NI TestStand property page of the Project Properties dialog box for a C++ project to specify whether to use TestStand include directories.

After you update the include directories, add the following directive at the top of the source file:

#import "teapi.dll"

When compiling this directive, Visual C++ generates teapi.tlh and teapi.tli in a Debug or Release directory that contains the intermediate files for the project. The generated files contain definitions of C++ classes that correspond to the TestStand API classes. Each C++ class contains methods for each of the corresponding TestStand API methods and properties.

By default, Visual C++ encloses the TestStand-generated classes within a TS namespace to avoid possible conflicts with other C++ identifiers that have the same names. As a result, when using the generated classes, you must prefix each class name with TS::, as in TS::Sequence. To avoid the need to prefix the class names with the namespace, you can add the no_namespace attribute to the import directive. You can also add a using namespace TS statement after the import directive, as shown in the following examples:

#import "teapi.dll" no_namespace

or

#import "teapi.dll"

using namespace TS;

In addition to teapi.dll, you can import the following files:

- TsAdpApi.tlb —Import this type library file to access the TestStand Adapters API. The default namespace for the TestStand Adapters API is TSAdp .
- tsui.dll and tsuisupp.dll —Import these DLLs to access the TestStand User Interface (UI) Controls API. The default namespace for tsui.dll is TSUI and the default namespace for tsuisupp.dll is TSUISUPP .

The tsapivc.h and tsapivc.cpp files import the type libraries for the TestStand API, TestStand Adapters API, and TestStand UI Controls API.

If you plan to use the TestStand API in many different source files, you might want to add the #import directive to the precompiled header file. Use tsapivc.h and tsapivc.cpp to more easily use the TestStand API in many different files. These files are located in the <TestStand>\API\VC directory. To use these files, include tsapivc.h in the precompiled header and include tsapivc.cpp in a single source file in the project so you can access the TestStand API C++ classes in all of the source files that use the precompiled header.

#### Using Microsoft Foundation Classes (MFC) Wrappers

TestStand does not install MFC wrappers for accessing the TestStand API. If you have source code that uses the tsapimfc.cpp and tsapimfc.h files from a previous version of TestStand, complete one of the following actions when you upgrade TestStand:

- Convert the code that uses MFC wrappers to use the Microsoft Visual Studio #import wrappers instead. Use the tsapivc.cpp and tsapivc.h files to access the TestStand API using these wrappers.
- Use Visual Studio to generate MFC wrappers for TestStand.
- Continue to use the wrappers provided by a previous version of TestStand.

Parent topic:

Programming with the TestStand API in Different Languages

Related concepts:

- TestStand Directory Structure

<!--NI_TOPIC bundle=teststand path=programming-with-the-teststand-api.html language=enus -->
## TOPIC 00721: Programming with the TestStand API in Different Languages

- bundle_id: `teststand`
- source_path: `programming-with-the-teststand-api.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/programming-with-the-teststand-api.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use the TestStand API in the following programming languages.

### Programming with the TestStand API in Different Languages

You can use the TestStand API in the following programming languages.

- [Programming with the TestStand API in LabVIEW](programming-with-the-teststand-api-in-labview.html)
- [Programming with the TestStand API in LabWindows/CVI](programming-with-the-teststand-api-in-cvi.html)
- [Programming with the TestStand API in Microsoft Visual Basic .NET](programming-with-the-teststand-api-msvb.html)
- [Programming with the TestStand API in C#](programming-with-the-teststand-api-in-csharp.html)
- [Programming with the TestStand API in Microsoft Visual C++](programming-with-the-teststand-api-msvc.html)
- [Programming with the TestStand API in HTBasic](programming-with-the-teststand-api-in-htbasic.html)
- [.NET Support for the TestStand API](net-support-ts-api.html) TestStand installs .NET interop assemblies for the TestStand API in the <TestStand>\API\DotNet\Assemblies directory and in the Global Assembly Cache (GAC). The interop assemblies support the current and earlier versions of the TestStand API, as shown in the following table.

Parent topic:

TestStand ActiveX API Overview

Related concepts:

- Accessing Properties Using API

<!--NI_TOPIC bundle=teststand path=prop-analogwaveform-table-schema.html language=enus -->
## TOPIC 00722: PROP_ANALOGWAVEFORM Table Schema

- bundle_id: `teststand`
- source_path: `prop-analogwaveform-table-schema.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/prop-analogwaveform-table-schema.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The default TestStand schema logs analog waveform data, such as the LabVIEWAnalogWaveform, NI_IviWave, and NI_IviWavePair data types, to this table. 18 PROP_ANALOGWAVEFORM Table Schema Column Name Data Type Description ID Primary Key Unique value that identifies each entry in the table. PROP_RESULT

### PROP_ANALOGWAVEFORM Table Schema

The default TestStand schema logs analog waveform data, such as the LabVIEWAnalogWaveform, NI_IviWave, and NI_IviWavePair data types, to this table.

| Column Name | Data Type | Description |
| --- | --- | --- |
| ID | Primary Key | Unique value that identifies each entry in the table. |
| PROP_RESULT | Foreign Key | Property ID from the PROP_RESULT table that associates the result with the generic property result. |
| INITIAL_T | Date/Time | Trigger time of the waveform. |
| DELTA_T | Number | Time interval in seconds between data points in the waveform. |
| INITIAL_X | Number | Offset of the waveform. |
| DELTA_X | Number | Interval between data points in the waveform. |
| UPPER_BOUNDS | String | Upper bounds of the waveform. For example, "[4][5]". |
| LOWER_BOUNDS | String | Lower bounds of the waveform. For example, "[0][0]". |
| DATA_FORMAT | String | Data format of the DATA field. Refer to Logging Binary and String Database Values for more information about writing values to binary columns. |
| DATA | Binary | Values of the waveform. |
| ATTRIBUTES | String | Attributes information associated with the waveform. |

Parent topic:

Default TestStand Table Schemas

<!--NI_TOPIC bundle=teststand path=prop-binary-table-schema.html language=enus -->
## TOPIC 00723: PROP_BINARY Table Schema

- bundle_id: `teststand`
- source_path: `prop-binary-table-schema.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/prop-binary-table-schema.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The default TestStand schema logs array data, such numeric arrays, to this table. 17 PROP_BINARY Table Schema Column Name Data Type Description ID Primary Key Unique value that identifies each entry in the table. PROP_RESULT Foreign Key Property ID from the PROP_RESULT table that associates the resu

### PROP_BINARY Table Schema

The default TestStand schema logs array data, such numeric arrays, to this table.

| Column Name | Data Type | Description |
| --- | --- | --- |
| ID | Primary Key | Unique value that identifies each entry in the table. |
| PROP_RESULT | Foreign Key | Property ID from the PROP_RESULT table that associates the result with the generic property result. |
| UPPER_BOUNDS | String | Upper bounds of the data portion of the array. For example, "[4][5]". |
| LOWER_BOUNDS | String | Lower bounds of the data portion of the array. For example, "[0][0]". |
| DATA FORMAT | String | Data format of the DATA field. Refer to Logging Binary and String Database Values for more information about writing values to binary columns. |
| DATA | Binary | Values of the array. |

Parent topic:

Default TestStand Table Schemas

<!--NI_TOPIC bundle=teststand path=prop-digitalwaveform-table-schema.html language=enus -->
## TOPIC 00724: PROP_DIGITALWAVEFORM Table Schema

- bundle_id: `teststand`
- source_path: `prop-digitalwaveform-table-schema.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/prop-digitalwaveform-table-schema.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The default TestStand schema logs analog waveform data, such as the LabVIEWDigitalWaveform data type, to this table. 19 PROP_DIGITALWAVEFORM Table Schema Column Name Data Type Description ID Primary Key Unique value that identifies each entry in the table. PROP_RESULT Foreign Key Property ID from th

### PROP_DIGITALWAVEFORM Table Schema

The default TestStand schema logs analog waveform data, such as the LabVIEWDigitalWaveform data type, to this table.

| Column Name | Data Type | Description |
| --- | --- | --- |
| ID | Primary Key | Unique value that identifies each entry in the table. |
| PROP_RESULT | Foreign Key | Property ID from the PROP_RESULT table that associates the result with the generic property result. |
| INITIAL_T | Date/Time | Trigger time of the waveform. |
| DELTA_T | Number | Time interval in seconds between data points in the waveform. |
| UPPER_BOUNDS | String | Upper bounds of the data portion of the waveform. For example, "[4][5]". |
| LOWER_BOUNDS | String | Lower bounds of the data portion of the waveform. For example, "[0][0]". |
| TRANSITIONS | Binary | 1D array of 4-byte integers (I4) in which each element represents the transition location for the corresponding sample in data. |
| DATA | Binary | 1D or 2D array of 1-byte integer (I1) values. Valid values include the following: ValueDigital Data State00 (force down)11 (force up)2Z (force off)3L (compare low)4H (compare high)5X (compare unknown)6T (compare off)7V (compare valid) |
| Value | Digital Data State |  |
| 0 | 0 (force down) |  |
| 1 | 1 (force up) |  |
| 2 | Z (force off) |  |
| 3 | L (compare low) |  |
| 4 | H (compare high) |  |
| 5 | X (compare unknown) |  |
| 6 | T (compare off) |  |
| 7 | V (compare valid) |  |
| ATTRIBUTES | String | Attributes information associated with the waveform. |

Parent topic:

Default TestStand Table Schemas

<!--NI_TOPIC bundle=teststand path=prop-numericlimit-table-schema.html language=enus -->
## TOPIC 00725: PROP_NUMERICLIMIT Table Schema

- bundle_id: `teststand`
- source_path: `prop-numericlimit-table-schema.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/prop-numericlimit-table-schema.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The default TestStand schema logs the limit information for a Numeric Limit Test step and a Multiple Numeric Limit Test step to this table. 20 PROP_NUMERICLIMIT Table Schema Column Name Data Type Description ID Primary Key Unique value that identifies each entry in the table. PROP_RESULT Foreign Key

### PROP_NUMERICLIMIT Table Schema

The default TestStand schema logs the limit information for a Numeric Limit Test step and a Multiple Numeric Limit Test step to this table.

| Column Name | Data Type | Description |
| --- | --- | --- |
| ID | Primary Key | Unique value that identifies each entry in the table. |
| PROP_RESULT | Foreign Key | Property ID from the PROP_RESULT table that associates the result with the generic property result. |
| COMP_OPERATOR | String | The comparison operator for the numeric limit result. |
| THRESHOLD_TYPE | String | The type of threshold used by the numeric limit step type when using the EQT (== +/-) comparison type. |
| NOMINAL_VALUE | String | The base limit value of the numeric limit step, when you use the EQT (== +/-) comparison type. |
| UPPER_THRESHOLD | String | The higher threshold value, which is used along with the Nominal Value and the Threshold type to compute the HIGH_LIMIT. |
| LOWER_THRESHOLD | String | The lower threshold value, which is used along with the Nominal Value and the Threshold type to compute the LOW_LIMIT. |
| HIGH_LIMIT | String | The high limit for the numeric limit comparison. |
| LOW_LIMIT | String | The low limit for the numeric limit comparison. |
| UNITS | String | A label that describes the units for the measurement. |
| STATUS | String | The status of the numeric limit comparison. |

Parent topic:

Default TestStand Table Schemas

<!--NI_TOPIC bundle=teststand path=prop-result-table-schema.html language=enus -->
## TOPIC 00726: PROP_RESULT Table Schema

- bundle_id: `teststand`
- source_path: `prop-result-table-schema.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/prop-result-table-schema.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The default TestStand schema logs information about the properties in a step result to this table for steps. If necessary, the default TestStand schema logs additional information about specific property data types in the other tables named with the PROP prefix. 16 PROP_RESULT Table Schema Column Na

### PROP_RESULT Table Schema

The default TestStand schema logs information about the properties in a step result to this table for steps. If necessary, the default TestStand schema logs additional information about specific property data types in the other tables named with the PROP prefix.

| Column Name | Data Type | Description |
| --- | --- | --- |
| ID | Primary Key | Unique value that identifies each entry in the table. |
| STEP_RESULT | Foreign Key | Step ID from the STEP_RESULT table that associates the result with a step. |
| PROP_PARENT | Foreign Key | Property ID from the PROP_RESULT table that associates the result with a parent result. |
| ORDER_NUMBER | Number | The order in which the property results are processed for a step result. |
| NAME | String | Name of the property. |
| PATH | String | Descriptive string path to the property within the step result. |
| CATEGORY | Number | Type of property. Valid values include 0 (unknown), 1 (built-in), 2 (custom), 3 (additional), 4 (parameter). |
| TYPE_VALUE | Number | The property data type. Valid values include 0 (container), 1 (string), 2 (Boolean), 3 (number), and 5 (reference). |
| TYPE_NAME | String | Display name of the property data type. |
| DISPLAY_FORMAT | String | Numeric display format of the property. |
| DATA | String | Value of the property. The default schema sets this value for all intrinsic values, which includes string, numeric, Boolean, and Enumeration values. |

Note

Value to Log

Logging.PropertyResultDetails.Type.TypeName

Note

Parent topic:

Default TestStand Table Schemas

<!--NI_TOPIC bundle=teststand path=properties-common-to-all-step-types.html language=enus -->
## TOPIC 00727: Properties Common to All Step Types

- bundle_id: `teststand`
- source_path: `properties-common-to-all-step-types.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/properties-common-to-all-step-types.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: TestStand defines multiple built-in step type properties common to all step types. Right-click a step and select Properties from the context menu to launch the Step Type Properties dialog box. You can examine and modify the values of the built-in step type properties in the Types window. Changes to

### Properties Common to All Step Types

TestStand defines multiple built-in step type properties common to all step types. Right-click a step and select Properties from the context menu to launch the Step Type Properties dialog box. You can examine and modify the values of the built-in step type properties in the Types window.

Note

The class step type properties exist only in the step type itself. TestStand uses the class step type properties to define how the step type works for all step instances. Step instances do not contain copies of the class step type properties.

The instance step type properties exist in each step instance. Each step you create with the step type includes a copy of the instance step type properties. TestStand uses the default value you specify for a step type property as the initial value of the property in each new step you create.

After you create a step, you can change the values of the properties for a step type instance, but these changes do not propagate to other step type instances. When you create a custom step type, you can prevent users from changing the values of specific instance step type properties in the steps they create. For example, you can use the Edit substep of a step type to set the Status Expression for the step, in which case you do not want users to explicitly change the Status Expression value. Some of the built-in step types, such as the Numeric Limit Test and the String Value Test, prevent you from changing the value of the instance step type properties.

Parent topic:

Custom Step Types

<!--NI_TOPIC bundle=teststand path=properties.html language=enus -->
## TOPIC 00728: Properties

- bundle_id: `teststand`
- source_path: `properties.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/properties.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: A property can store a single value or a multidimensional array of values of the same data type. A value can be a number, string, Boolean, .NET object reference, or ActiveX object reference. TestStand stores numbers as 64-bit, floating-point values in the IEEE 754 format. Values are not containers a

### Properties

A property can store a single value or a multidimensional array of values of the same data type.

A value can be a number, string, Boolean, .NET object reference, or ActiveX object reference. TestStand stores numbers as 64-bit, floating-point values in the IEEE 754 format. Values are not containers and thus cannot contain subproperties.

TestStand uses the following major categories of properties, defined by the kinds of values the properties contain:

- Single-valued property —A single value. TestStand supports number, string, Boolean, and object reference single-valued properties.
- Array property —An array of values. TestStand supports number, string, Boolean, and object reference array properties.
- Property-array property —A value that is an array of subproperties of a single type.
- Container property —Contains no values but contains multiple subproperties. Container properties are analogous to clusters in LabVIEW and to structures in C/C++.

Parent topic:

TestStand Building Blocks

Related concepts:

- Built-In and Custom Properties

<!--NI_TOPIC bundle=teststand path=property-flags-that-affect-reports.html language=enus -->
## TOPIC 00729: Property Flags That Affect Reports

- bundle_id: `teststand`
- source_path: `property-flags-that-affect-reports.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/property-flags-that-affect-reports.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Set the PropFlags_IncludeInReport, PropFlags_IsLimit, and PropFlags_IsMeasurementValue flags to identify the result properties to automatically display in the report. The PropFlags_IncludeInReport flag specifies to include a property in the report. For properties that hold limit values or output val

### Property Flags That Affect Reports

Set the PropFlags_IncludeInReport, PropFlags_IsLimit, and PropFlags_IsMeasurementValue flags to identify the result properties to automatically display in the report.

The PropFlags_IncludeInReport flag specifies to include a property in the report. For properties that hold limit values or output values, use the PropFlags_IsLimit and PropFlags_IsMeasurementValue flags to selectively exclude limits or output values according to the options you select in the Report Options dialog box. When you set a reporting flag for an array or container property, TestStand sets the flag for all array elements or subproperties within the container property.

Parent topic:

Generating and Customizing TestStand Reports

<!--NI_TOPIC bundle=teststand path=property-loader-plugins-database-table-schema.html language=enus -->
## TOPIC 00730: Property Loader Plugins - Database Table Schemas

- bundle_id: `teststand`
- source_path: `property-loader-plugins-database-table-schema.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/property-loader-plugins-database-table-schema.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Database Table Schemas The Property Loader step type includes a plugin to support importing and exporting properties to and from a database. This topic describes the table schemas that the database plugin requires and creates when exporting properties. The database plugin is responsible for establis

### Property Loader Plugins - Database Table Schemas

#### Database Table Schemas

The Property Loader step type includes a plugin to support importing and exporting properties to and from a database. This topic describes the table schemas that the database plugin requires and creates when exporting properties.

Note

- The database plugin is responsible for establishing a connection with the database. There is no such dependency on the step, unlike with the Legacy Property Loader step.
- The Property Loader step also supports importing and exporting limits from .csv, .txt, and .xlsx (Microsoft Excel) file types. Refer to the Property Loader Plugins - File Formats topic for more information about storing limits in these files.
- See the Legacy Property Loader Step - Loading Limit Values from Databases topic for more information about database table schemas for the Legacy Property Loader step.

#### GROUPS_DESC Table Structure

The following table describes the schema that defines the property groups, their names, and their values. Some columns are optional and can be null, meaning that they do not have to contain values.

| Column Name | Data Type | Can Be Null? | Purpose |
| --- | --- | --- | --- |
| GROUP_ID | Primary Key, String | No | Unique value that identifies each entry in the table. |
| NAME | String | Yes | Stores the name of the property groups. |
| DESCRIPTION | String | Yes | Stores a description of the properties. |

See the following image for an example of a GROUP_DESC table. Each row represents a different property group. In this case, there is only one group, called New Properties.

[IMAGE alt='image' src='GUID-37B21A09-EA9D-414A-B4F4-F84D63C245A3-a5.png']

#### PROPERTIES Table Structure

The following table describes the schema that defines the columns used by the Property Loader. Some columns are optional and can be null, meaning that they do not have to contain values.

| Column Name | Data Type | Can Be Null? | Purpose |
| --- | --- | --- | --- |
| ID | Primary Key, Number | No | Unique value that identifies each entry in the table |
| GROUP_ID | Foreign Key, String | No | The corresponding GROUP_ID column of the GROUP_DESC table. |
| SEQUENCE_FILE_NAME | String | Yes | Indicates the name of the sequence file in which the property exists. |
| SEQUENCE_NAME | String | Yes | Indicates the name of the sequence that each property will be imported into. If the sequence name for a property is blank, the property will be imported into all sequences within the sequence file. |
| CATEGORY | String | No | Indicates the location of each property. The location can be one of the following literal values. {StationGlobals}—Indicates that the property is a station global variable. {FileGlobals}—Indicates that the property is a file global variable. {Locals}—Indicates that the property is a local variable within a sequence. {Parameters}—Indicates that the property is a sequence parameter. {Attributes}—Indicates that the property is a sequence attribute.If the category is not one of the above values, CATEGORY must specify a value the can uniquely identify the step property. Typically, that is either the name or ID of a step, and the columns to the right specify the property of the step. See the example PROPERTIES table image below for more information about step name and ID formats. |
| PROPERTY_LOOKUP | String | No | Indicates the lookup string of the property whose value will be updated. If the lookup is specified using an alias, the alias name is represented within <>. Refer to Rows 2, 3, 5, and 6 in the example image below for an example of alias name representation.If the lookup is for a container, the name of the container is enclosed in [] and suffixed with .Type. The VALUE column is null in this case. Refer to column 13 in the example image below for an example of array representation.If the database was exported with type information, values in this column will also contain the type information after the lookup string, enclosed within {}. |
| VALUE | String | Yes | Indicates the value of the property to be imported. |

See the following image for an example of a PROPERTIES table. When the PROPERTIES table contains data associated with step properties, either the step name, step ID, or both should be specified in the CATEGORY column. Rows 1-6 demonstrate valid ways to specify these values.

[IMAGE alt='image' src='GUID-89A0A7B5-CB4A-4AAC-800F-E976BE1425E1-a5.png']

#### ALIAS Table Structure

The following table describes the schema that defines alias names for the Property Loader step. The Property Loader step allows you to optionally specify alias names for properties within the database table. Aliases allow you to refer to properties within the database with meaningful names, rather than a property lookup string. When a PROPERTIES file contains aliases, a corresponding ALIAS table must be associated with the PROPERTIES table.

Note

ALIAS

| Column Name | Data Type | Can Be Null? | Purpose |
| --- | --- | --- | --- |
| ALIAS_NAME | Primary Key, String | No | The alias name. |
| PROPERTY_LOOKUP | String | No | The lookup string that maps the alias name to the property. |

See the following image for an example of an ALIAS table that shows the mapping between alias names and their lookup strings. Note that the alias name PowerOnLimitLow is used in the PROPERTIES table example above.

[IMAGE alt='image' src='GUID-674EEFB2-0BC0-409E-A2CB-6AF6BDB94217-a5.png']

Parent topic:

Using the Property Loader Step Type

<!--NI_TOPIC bundle=teststand path=property-loader-plugins-file-formats.html language=enus -->
## TOPIC 00731: Property Loader Plugins - File Formats

- bundle_id: `teststand`
- source_path: `property-loader-plugins-file-formats.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/property-loader-plugins-file-formats.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: File Formats The Property Loader step type and the Import/Export Properties tool includes file plugins to support .csv, .txt, and .xlsx (Microsoft Excel) file types. This topic describes the required delimiter characters, file structure, special property formats, and property aliases for these file

### Property Loader Plugins - File Formats

#### File Formats

The Property Loader step type and the Import/Export Properties tool includes file plugins to support .csv, .txt, and .xlsx (Microsoft Excel) file types. This topic describes the required delimiter characters, file structure, special property formats, and property aliases for these file formats.

Note

- The Property Loader step also supports importing and exporting properties from a database. Refer to the Property Loader Plugins - Database Format topic for more information about storing properties in a database.
- See the Legacy Property Loader Step - Loading Limit Values from Files topic for more information about different file formats for the Legacy Property Loader step.

#### Delimiter Characters

#### Column Delimiters

The primary difference between the file types is the delimiter character used to separate columns of data. The following table describes the column delimiter used for each file format:

| File Format | Column Delimiter |
| --- | --- |
| .csv | Comma |
| .txt | Tab character |
| .xlsx | None. .xlsx files should be opened and edited with Microsoft Excel or another application capable of supporting .xlsx files. |

#### Row Termination Characters

In all file formats, new-line characters are used to terminate each row of data.

#### Field Delimiters

Data values, or fields, within the file may optionally be enclosed in double quotes. However, when certain characters are present in a field, the field must be enclosed in double quotes. The following table describes the cases in which fields must be enclosed in double quotes:

| File Format | Cases Where Field Must Be Enclosed in Double Quotes |
| --- | --- |
| .csv | Fields containing commas Fields containing leading or trailing spaces Fields containing line breaks Fields containing double quotes. When a field contains double quotes, each double quote must be preceded by another double quote to serve as an escape character. |
| .txt | Fields containing tab characters Fields containing leading or trailing spaces Fields containing line breaks Fields containing double quotes. When a field contains double quotes, each double quote must be preceded by another double quote to serve as an escape character. |
| .xlsx | None. It is not necessary to enclose fields in double quotes in .xlsx files. |

#### File Structure

See the following image for an example of a Property Loader source file in the correct structure for use with the Property Loader plugins.

Note

[IMAGE alt='image' src='GUID-C56DF630-7E10-45BD-8807-BBA3FD534A24-a5.png']

The purpose of each element in the file is described in the following table:

| File Element | Position in Example File | Purpose |
| --- | --- | --- |
| <PropertyGroup> start and end markers | Cells A1, A6 | Indicate the beginning and end of the TestStand property data to be imported from the file. The <PropertyGroup> start marker contains the name and ID of the data, and should be unique within the file. Optionally, a description can be included in the <PropertyGroup> start tag.Any data that is not enclosed within the <PropertyGroup> start and end tags is ignored. |
| <Sequence> column header | Cell A2 | Indicates that this column represents the name of the sequence that each property will be imported into. If the sequence name for a property is blank, the property will be imported into all sequences.Note: This column is optional. If the <Sequence> column does not exist in the file, all Locals, Parameters, Sequence Attributes, and step properties will be imported into all sequences within the sequence file. |
| <Category> column header | Cell B2 | Indicates that this column represents the location of each property. The location can be one of the following literal values: {StationGlobals}—Indicates that the property is a station global variable. {FileGlobals}—Indicates that the property is a file global variable. {Locals}—Indicates that the property is a local variable within a sequence. {Parameters}—Indicates that the property is a sequence parameter. {Attributes}—Indicates that the property is a sequence attribute. If the name defined in the <PropertyGroup> start tag is GlobalProperties, the property is instead a sequence file attribute.If the category is not one of the above values, the category must specify a value the can uniquely identify the step property. Typically, that is either the name or ID of a step, and the columns to the right specify the property of the step. See the Identifying Steps section below for more information about supported step name and ID formats. |
| <PropertyLookup> column header | Cell C2 | Indicates that this column represents the lookup string of each property. If the value is enclosed in angle brackets (< and >), the value represents an alias name.If the file was exported with type information, this column will also contain the type information after the lookup string, enclosed within curly brackets ({ and }). |
| <Value> column header | Cell D2 | Indicates that this column represents the value of each property to be imported. |
| Property data for simple data types (string, number, boolean) | Row 3 | Each string, numeric, or boolean property is represented by one row in the file. |
| Property data for containers | Rows 4, 5 | Each container is represented by two rows in the file. The first row contains the names of each field in the container, and the second row contains the values of each field. Note that additional columns are used to represent container fields and values. |

#### Identifying Steps

When the file contains data associated with step properties, either the step name, step ID, or both should be specified in the <Category> column. The following image demonstrates each method of identifying a step within a file.

[IMAGE alt='image' src='GUID-1711087A-9BD7-4D59-AC9A-351F279B705F-a5.png']

#### Special Property Formats

The following sections describe the file format for properties in arrays and nested containers.

#### Arrays

See the following image for an example of a file containing an array of numbers:

[IMAGE alt='image' src='GUID-C0EF2F1F-EC62-4DEC-95EB-5EC77E9CE3EC-a5.png']

In this example, cell C3 contains the lookup string of the array, followed by information about the dimensions of the array enclosed in curly brackets {}. Rows 4-8 represent the value of each element in the array, with the value of the <PropertyLookup> column indicating which element in the array is represented by the row of data.

#### Nested Containers

See the following image for an example of a file with a container property that contains another container as a field:

[IMAGE alt='image' src='GUID-B47E6D7B-DCBC-4F90-A5DF-ADD4F7CACD39-a5.png']

In this example, the local variable SampleContainer, represented on rows 3 and 4, includes a field named SubData, which is also a container. Note that the field names and values for the SubData container are represented on rows 5 and 6 of the file, below the rows for basic data type fields within the parent container.

#### Property Aliases

The Property Loader allows you to optionally specify alias names for properties within a file. Aliases allow you to refer to properties within the file with meaningful names, rather than a property lookup string. When a file contains aliases, a .pla (Property Loader Alias) file must be associated with the file. The .pla file contains the mapping between aliases and property lookup strings.

#### Using Aliases within a Limits File

When aliases are used within a file, the <PropertyLookup> column will be replaced with an <AliasName> column. See the following image for an example of a file with aliases instead of property lookup strings:

[IMAGE alt='image' src='GUID-D2E35FFB-B396-44EB-8CEE-08CE4FFF6BB4-a5.png']

Column C in this example contains the alias name for each property defined in the file.

#### Property Alias Files

In order for the Property Loader to load properties with alias names into a sequence file, a .pla file must be specified when the file is imported. The .pla file is encoded in XML, as seen in the following example:

<?xml version="1.0" encoding="utf-8"?>

<AliasItems xmlns:ts="www.ni.com/TestStand ">

<AliasItem AliasName="Test Result Value" PropertyLookup="Sequence[MainSequence].Locals.TestResult" />

<AliasItem AliasName="Test Data Source" PropertyLookup="Sequence[MainSequence].Step[My Test Step].DataSource" />

</AliasItems>

In this example, each <AliasItem> tag defines an alias and its associated property lookup string.

The .pla file will be created automatically during the export process if aliases are defined, and can be modified outside of TestStand if the alias names or property lookup strings need to be updated.

Parent topic:

Using the Property Loader Step Type

<!--NI_TOPIC bundle=teststand path=property-loader-step-type-loading-limits-db.html language=enus -->
## TOPIC 00732: Property Loader Step Type - Loading Limits from a Database

- bundle_id: `teststand`
- source_path: `property-loader-step-type-loading-limits-db.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/property-loader-step-type-loading-limits-db.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Purpose This example demonstrates how to use the Property Loader step type to load step properties, such as limits for Numeric Limit Test steps, from a database. Example File Location <TestStand Public>\Examples\Built-In Step Types\Property Loader Step Type\Property Loader - Loading Limits From a Da

### Property Loader Step Type - Loading Limits from a Database

#### Purpose

This example demonstrates how to use the Property Loader step type to load step properties, such as limits for Numeric Limit Test steps, from a database.

#### Example File
 Location

<TestStand
 Public>\Examples\Built-In Step Types\Property Loader Step
 Type\Property Loader - Loading Limits From a Database.seq

#### Highlighted Features

- Database step types
- Database Viewer Application
- Property Loader steps

#### Major API

None

#### Prerequisites

TestStand
 loads the property values from the Access.mdb file located in the
 same directory as the sequence file. (32-bit TestStand) You must have the Microsoft
 Jet 4.0 Object Linking and Embedding Database (OLE DB) Provider installed. (64-bit
 TestStand) You must have the Microsoft Access Database Engine 2010 Redistributable
 installed. Visit ni.com/info and enter the Info Code
 64TSaccdb to access the NI support article, Using Microsoft
 Access Databases with 64-bit TestStand, for more information about installing this
 provider.

#### How to Use This Example

This example uses a Property Loader step to load property values, including local variable values and step limits, from a Microsoft Access database file. The Property Loader step applies these values to the sequence before the test steps execute, which demonstrates how the limits and variables can be loaded each time a sequence executes.

Complete the following steps to review the Property Loader step settings.

1. On the Steps pane, select the Property Loader step in the Setup step group.
2. On the Step Settings tab of the Steps pane, review the items in the sources table. In this table, the database is configured as the properties source.
3. On the Target File and Source Settings tab, review the properties selected in the Property Tree control. The step loads the Comp , Limits.Low , and Limits.High values for each step specified, as well as a local and file global variable.

Complete the following steps to run this example.

1. Select Execute»Single Pass to run the sequence.
2. When execution completes, review the report on the Report pane. The report indicates that the Video step failed because the test result of 65 was not within the acceptable limits.
3. Complete the following steps to edit the database to include an acceptable value.
  1. Select Tools»Database Viewer to launch the TestStand Database Viewer application.
  2. Select File»Open , browse to <TestStand Public>\Examples\Built-In Step Types\Property Loader Step Type\Access.mdb , and click OK .
  3. Right-click the STEP_PROPERTIES table in the Database Explorer pane and select View Data .
  4. Right-click the table and select Edit Data .
  5. Change the value of the LIMITS_LOW field for the video record from 71 to 60 . Click the Submit button to submit the values to the database.
  6. Close the Database Viewer application.
4. Select Execute»Single Pass to run the sequence again.
5. When execution completes, review the report on the Report pane. The report indicates that the Video step passed because the test result is now within the acceptable limits.

Parent topic:

Examples for Built-In Step Types

Related concepts:

- TestStand Directory Structure
- Step Groups

<!--NI_TOPIC bundle=teststand path=property-loader-step-type-loading-limits-for.html language=enus -->
## TOPIC 00733: Property Loader Step Type - Loading Limits for Multiple Sequences

- bundle_id: `teststand`
- source_path: `property-loader-step-type-loading-limits-for.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/property-loader-step-type-loading-limits-for.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Purpose This example demonstrates using the Property Loader step type to load the properties for multiple sequences in a client sequence file. The example loads properties at the beginning of the MainSequence. Example File Location <TestStand Public>\Examples\Built-In Step Types\Property Loader Step

### Property Loader Step Type - Loading Limits for Multiple Sequences

#### Purpose

This example demonstrates using the Property Loader step type to load the properties for multiple sequences in a client sequence file. The example loads properties at the beginning of the MainSequence.

#### Example File
 Location

<TestStand
 Public>\Examples\Built-In Step Types\Property Loader Step
 Type\Property Loader - Loading Limits For Multiple
 Sequences.seq

#### Highlighted Features

Property Loader steps

#### Major API

None

#### Prerequisites

None

#### How to Use This Example

Complete the following steps to change properties that already exist in a sequence.

1. Select the MainSequence .
2. On the Steps pane, select the Property Loader step.
3. On the Step Settings pane, click the Step Settings tab. Click the View File button in the sources table to open propertyData.txt , which is located in the same directory as the example sequence file and is the file the Property Loader step is using to specify property values. The text file specifies a data block for each sequence in the sequence file so the step can load different values for the same property in different sequences. The Start and End of Data markers for the data block include the name of the sequence. In the text file, the Properties for Sequence 1 section specifies the limits for the Numeric Limit Test step as 15 for Limits.Low and 20 for Limits.High . The text file contains very specific formatting to which you must adhere for the Property Loader step to function correctly. The best method for generating a file for use with a Property Loader step is to specify the properties in the sequence file and then select Tools»Import/Export Properties to launch the Import/Export Properties dialog box, in which you can generate a file that a Property Loader step can use.
4. Select Execute»Single Pass to run the sequence.
5. When execution completes, review the report on the Report pane. Notice that the limit values in each subsequence have changed to the values specified by the property file.

Parent topic:

Examples for Built-In Step Types

Related concepts:

- TestStand Directory Structure

<!--NI_TOPIC bundle=teststand path=property-paths.html language=enus -->
## TOPIC 00734: Property Paths

- bundle_id: `teststand`
- source_path: `property-paths.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/property-paths.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: A property path is a chain of period-delimited subproperties that selects a particular subproperty of an object. A property path typically specifies the location of a property or variable in the active sequence context. For example, the active sequence context contains the Station Globals object, wh

### Property Paths

A property path is a chain of period-delimited subproperties that selects a particular subproperty of an object. A property path typically specifies the location of a property or variable in the active sequence context. For example, the active sequence context contains the Station Globals object, which contains a TS property that holds the current User object. To refer to the current User object, use the StationGlobals.TS.CurrentUser property path.

You can use the sequence context and property paths to access variables and step properties in expressions and through calls to the TestStand API from code modules.

You can specify a complete path, regardless of the length or complexity of the path, when all of the elements in the path are dynamic properties. For example, to specify the error code in the third step of the Main step group of the currently executing sequence, use the following path:

"RunState.Sequence.Main[2].Result.Error.Code"

Parent topic:

TestStand API Concepts

Related concepts:

- Expressions
- Sequence Context

<!--NI_TOPIC bundle=teststand path=property-settings-specific-to-data-types.html language=enus -->
## TOPIC 00735: Property Settings Specific to Data Types

- bundle_id: `teststand`
- source_path: `property-settings-specific-to-data-types.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/property-settings-specific-to-data-types.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: TestStand data type properties include some settings that are specific to types. You can examine and modify the values of these settings in the Types window. Right-click a data type and select Properties from the context menu to launch the Type Properties dialog box.

### Property Settings Specific to Data Types

TestStand data type properties include some settings that are specific to types. You can examine and modify the values of these settings in the Types window. Right-click a data type and select Properties from the context menu to launch the Type Properties dialog box.

Parent topic:

Data Types

<!--NI_TOPIC bundle=teststand path=propertyobject-attributes.html language=enus -->
## TOPIC 00736: PropertyObject Attributes

- bundle_id: `teststand`
- source_path: `propertyobject-attributes.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/propertyobject-attributes.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can create attributes for TestStand PropertyObjects, such as variables, steps, module parameters, and type definitions. Use attributes to store additional information about a PropertyObject within a sequence file or type palette file, such as the author of a sequence. Every PropertyObject includ

### PropertyObject Attributes

You can create attributes for TestStand PropertyObjects, such as variables, steps, module parameters, and type definitions. Use attributes to store additional information about a PropertyObject within a sequence file or type palette file, such as the author of a sequence. Every PropertyObject includes an Attributes property, which is an unstructured container that stores arbitrary data.

Use container subproperties under the Attributes property to serve as attribute namespaces. NI
 recommends that you create a uniquely named container or hierarchy of containers
 under which you store attribute variables to avoid name conflicts, such as
 CompanyName.AttributeCategory.Attribute. The name NI is
 reserved at the root level for National Instruments.

#### Editing Attributes

Select Advanced»Edit Attributes from the Sequences pane context menu to launch the Attributes dialog box, in which you can create and edit attributes for the sequence. When the sequence includes attributes, you can click the Edit Attributes button in the Sequence column of the Sequences pane to launch the Attributes dialog box.

Right-click a PropertyObject on the Variables pane and select Advanced»Edit Attributes from the context menu to launch the PropertyObject Attributes dialog box, in which you can create and edit attributes. PropertyObjects with attributes include an Edit Attributes button in the Name column of the Variables pane.

Click the Edit Attributes button on the General panel of the Properties tab on the Step Settings pane to launch the Attributes dialog box for steps. Steps with attributes include the word Attributes in the step description.

Right-click a parameter on the Module tab of the Step Settings pane in the sequence editor or in the Specify Module dialog box in user interfaces and select Edit Attributes from the context menu to launch the Attributes dialog box for a module parameter. Parameters with attributes include an Edit Attributes button in the Name column of the Parameters Table. When editing a LabVIEW or .NET code module, you can edit attributes for fields of containers and elements of arrays. TestStand associates parameter attributes with the code module parameter, which TestStand stores with the step configuration information, not with the parameter value that TestStand passes to the code module.

#### Managing Attributes

Right-click a type in the Types window of the sequence editor, select Properties from the context menu, click the Advanced button on the General tab of the Properties dialog box, and select Attributes to launch the Attributes dialog box for a type definition. When editing the attributes of a type definition, you can edit both attributes and type attributes. For a type definition, attributes determine the default values of the attributes of type instances. Type attributes are attributes for the type definition and do not exist for type instances.

Enable the Include Attributes option on the Contents tab of the Report Options dialog box or enable the PropFlags_IncludeInReport flag on both an attribute and on the PropertyObject object that owns the top-level attribute to include attribute information in reports. Typically, a report generator does not recursively apply the PropFlags_IncludeInReport flag from a property to its attributes.

The default TestStand database schemas do not log attribute values for result properties. You can customize a database logging schema to log attributes.

Enable the Attributes option on the Filter tab of the Find/Replace in Files dialog box and in the Find/Replace dialog box to include the attributes and type attributes of variables and properties in search results.

The TestStand File Diff and Merge utility detects and merges attribute differences. Right-click an item and select Advanced»Edit Attributes from the context menu or click the Edit Attributes button in the Name column of the utility to launch the related Attributes dialog box. When you right-click an item and select Replace Item Values in File <filename> from the context menu, TestStand also copies attribute values.

You can specify an attribute or type attribute using a lookup string. Use Attributes in a lookup string to specify the attributes of the property object and use TypeAttributes to specify the type attributes of the property object. For example, the following lookup string accesses an attribute of a local variable from a sequence:

"Locals.Foo.Attributes.AttributeNamespace.Attribute1"

Note

- If a property object has a subproperty named Attributes or TypeAttributes, the subproperty takes
 precedence over the attributes or type attributes in a lookup string. As a
 result, some TestStand features, such as accessing attributes using lookup
 strings, undo, and find and replace, do not support attributes if the parent
 property object also has a subproperty named Attributes. NI does not
 recommend using attributes and a subproperty named Attributes on the same
 property object. You can convert the subproperty to attributes or rename the
 subproperty.
- You cannot specify an attribute or type attribute with a lookup string you pass to a method in the TestStand API if you also use the PropOption_InsertIfMissing option in the method call. Using the PropOption_InsertIfMissing option with a lookup string that contains Attributes or TypeAttributes causes methods in the TestStand API to create a subproperty for Attributes or TypeAttributes.

Parent topic:

Properties

Related concepts:

- Default TestStand Table Schemas
- Logging Attribute Values

<!--NI_TOPIC bundle=teststand path=prototypes-for-analysis-modules.html language=enus -->
## TOPIC 00737: Prototypes for Analysis Modules

- bundle_id: `teststand`
- source_path: `prototypes-for-analysis-modules.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/prototypes-for-analysis-modules.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The TestStand Sequence Analyzer requires that analysis modules use the following specific prototypes. LabVIEW The VI connector pane must use an ActiveX Refnum input with the ActiveX class set to TSAnalyzer.AnalysisContext and can optionally include an Error Out cluster output or a Boolean, an I32 nu

### Prototypes for Analysis Modules

The TestStand Sequence Analyzer requires that analysis modules use the following specific
 prototypes.

#### LabVIEW

The VI connector pane must use an ActiveX Refnum input with
 the ActiveX class set to
 TSAnalyzer.AnalysisContext
 and can optionally include an Error Out cluster output or a
 Boolean, an I32 numeric, and a string output, which represent the unbundled elements
 of an Error Out cluster. You can use the Unbundle by Name
 function in LabVIEW to obtain the individual elements of the Error
 Out cluster.

#### LabWindows/CVI

The function prototype must be one of the following:

void Function(CAObjHandle analysisContext);

bool Function(CAObjHandle analysisContext, char errorMessage[]);

int Function(CAObjHandle analysisContext, char errorMessage[]);

where analysisContext is an input that contains an instance of the
 TSAnalyzer.AnalysisContext
 ActiveX class, and errorMessage is a string buffer of 1024
 characters in which the function returns error messages for the analysis module
 code.

#### Microsoft Visual C#

The method prototype must be one of the following:

void
 Method(NationalInstruments.TestStand.Interop.SequenceAnalyzer.AnalysisContext
 analysisContext);

bool
 Method(NationalInstruments.TestStand.Interop.SequenceAnalyzer.AnalysisContext
 analysisContext, out string errorMessage);

where analysisContext is an input that contains an instance of the
 AnalysisContext COM interop class and
 errorMessage is an output string in which the method returns
 error messages for the analysis module code.

#### Microsoft Visual C++

The function prototype must be one of the following:

void Function(TSAnalyzer::AnalysisContext *analysisContext);

bool Function(TSAnalyzer::AnalysisContext *analysisContext, char
 errorMessage[]);

int Function(TSAnalyzer::AnalysisContext *analysisContext, char
 errorMessage[]);

where analysisContext is an input that contains an instance of the
 TSAnalyzer.AnalysisContext ActiveX class, and
 errorMessage is a string buffer of 1024 characters in which the
 function returns error messages for the analysis module code.

Parent topic:

Creating Analysis Modules for Custom Rules

Related concepts:

- Implementing Analysis Modules

Related information:

- AnalysisContext

<!--NI_TOPIC bundle=teststand path=python-adapter-known-limitations.html language=enus -->
## TOPIC 00738: Python Adapter Known Limitations

- bundle_id: `teststand`
- source_path: `python-adapter-known-limitations.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/python-adapter-known-limitations.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following are the known limitations when using Python Adapter: You cannot use Python interpreters other than CPython, such as PyPy. You cannot pass .NET objects between Python and TestStand. You cannot call a function in a class with the @classmethod attribute. You cannot log a return value unle

### Python Adapter Known Limitations

The following are the known limitations when using Python Adapter:

- You cannot use Python interpreters other than CPython, such as PyPy.
- You cannot pass .NET objects between Python and TestStand.
- You cannot call a function in a class with the @classmethod attribute.
- You cannot log a return value unless it is stored in a TestStand variable.
- You cannot use default values. Values for all the parameters of a Python function need to be specified.
- You cannot pass parameters using a keyword (or named) argument.
- You cannot convert an empty container, or a container that does not have any data, between TestStand and Python.
- You cannot convert an Array of unstructured containers from TestStand to Python.
- You cannot use TestStand to create or edit Python code.

Parent topic:

Python Adapter

<!--NI_TOPIC bundle=teststand path=python-adapter.html language=enus -->
## TOPIC 00739: Python Adapter

- bundle_id: `teststand`
- source_path: `python-adapter.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/python-adapter.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Python Adapter provides advanced functionality for calling Python code modules from TestStand. Before using the Python Adapter in TestStand, install the required version of the CPython interpreter. During installation of the CPython interpreter, you must enable the option for adding the Python

### Python Adapter

The Python Adapter provides advanced functionality for calling Python code modules from TestStand.

Note

Install the following Python packages to enable specific workflows:

| Package | Version | Workflow |
| --- | --- | --- |
| Python for Win32 (pywin32) | 228 | Passing TestStand objects or ActiveX objects that implement IDispatch between TestStand and Python. |
| Numpy | 1.19.1 | Passing an array of numbers from TestStand to Python as a NumPy array. |
| debugpy | – | Perform step into debugging operations on Python modules. |
| Jedi | – | View additional elements used in Python code modules, including inner classes, function and attribute names defined in a base class, and imported classes, attributes, and functions. |

You can use the Python Adapter to complete the following tasks:

- Execute Python scripts ( .py ) on disk by:
  - Calling a function defined in a module.
  - Getting/Setting the attributes defined in a module.
  - Creating a class instance.
  - Calling a member function or static function defined in the class.
  - Getting/Setting member attributes or static attributes defined in the class.
- Execute Python scripts in supported Python versions. Refer to the TestStand Release Notes for
 supported Python versions.
- Execute Python scripts out-of-process in the CPython interpreter.
- Convert data between Python and TestStand variables.
- Store/reuse the Python object in a TestStand variable (Object Reference).

You can also use multiple Python interpreter sessions to perform the following tasks:

- Execute Python scripts in parallel.
- Use multiple Python versions, such as 3.6 and 3.8, simultaneously in TestStand.

When you specify a module for a step, the TestStand Sequence Editor displays the Python Module Tab. TestStand User Interfaces launch the Edit Python Call dialog box.

Use the Python Adapter Configuration Dialog Box to configure the Python version and Python virtual environment path to use with the Python Adapter.

Parent topic:

Module Adapters

Related information:

- Python Download
- Edit Python Call Dialog Box
- Python Adapter Configuration Dialog Box

<!--NI_TOPIC bundle=teststand path=python-code-module-support-for-64-bit-teststa.html language=enus -->
## TOPIC 00740: Python Code Module Support for 64-bit TestStand

- bundle_id: `teststand`
- source_path: `python-code-module-support-for-64-bit-teststa.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/python-code-module-support-for-64-bit-teststa.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: When you migrate Python code modules from 32-bit TestStand to 64-bit TestStand, NI recommends that you install the 64-bit CPython interpreter of the intended version in the test system. Once the 64-bit CPython interpreter is installed, you should also update the PATH environment variable with the pa

### Python Code Module Support for 64-bit TestStand

When you migrate Python code modules from 32-bit TestStand to 64-bit TestStand, NI recommends
 that you install the 64-bit CPython interpreter of the intended version in the test
 system. Once the 64-bit CPython interpreter is installed, you should also update the
 PATH environment variable with the path to the interpreter.

Parent topic:

64-bit TestStand and Migrating from 32-bit TestStand

<!--NI_TOPIC bundle=teststand path=python-interpreter-sessions.html language=enus -->
## TOPIC 00741: Python Interpreter Sessions

- bundle_id: `teststand`
- source_path: `python-interpreter-sessions.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/python-interpreter-sessions.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use the Advanced Settings Dialog to specify which Python interpreter session to use for executing the step. You can specify one of the following options: Object Reference—Use the interpreter session present in interpreter reference Per Thread—Use the interpreter session created per TestStand

### Python Interpreter Sessions

You can use the Advanced Settings Dialog to specify which Python interpreter session to use for executing the step. You can specify one of the following options:

- Object Reference —Use the interpreter session present in interpreter reference
- Per Thread —Use the interpreter session created per TestStand thread
- Per Execution —Use the interpreter session created per TestStand execution
- Global —Use the interpreter session created once per TestStand application

You can use multiple Python interpreter session to execute Python scripts in parallel or use multiple Python versions simultaneously.

#### Execute Python Scripts in Parallel

CPython is one of the most used Python interpreters. It has a Global Interpreter Lock (GIL) due to which only one Python thread can be executing at any given point of time. Hence, you cannot perform any multi-threaded operation in Python to execute operations in parallel.

National Instruments recommends you to use multiple Python interpreter session to execute Python modules in parallel. If you want to handle device instruments using Python, you should create an interpreter session for each instrument so that all instruments can be operated in parallel.

#### Use Multiple Python Versions Simultaneously

You can also use multiple Python interpreter sessions to use different Python versions together in the same TestStand execution.

Note

Parent topic:

Python Adapter

<!--NI_TOPIC bundle=teststand path=python-namespaces.html language=enus -->
## TOPIC 00742: Python Namespaces

- bundle_id: `teststand`
- source_path: `python-namespaces.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/python-namespaces.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Namespaces enable TestStand to load multiple Python modules with the same name from different locations, or to assign the full type name to a class. When you specify a Python module for the Python Adapter to use, TestStand assigns a namespace to the module. If the module you specify is under a packa

### Python Namespaces

Namespaces enable TestStand to load multiple Python modules with the same name from different locations, or to assign the full type name to a class.

When you specify a Python module for the Python Adapter to use, TestStand assigns a namespace to the module. If the module you specify is under a package, TestStand calculates the namespace from the top most package. If the module you specify is not under a package, the namespace contains only the module name.

#### Compatibility

In earlier versions of TestStand before namespace support was introduced, type names of classes did not contain namespaces. If you use the type() function to determine the data type of a parameter of a function, you may encounter errors that were not present when using the earlier version of TestStand. Update your type validation code to resolve such errors.

Parent topic:

Python Adapter

Related information:

- Packages in Python

<!--NI_TOPIC bundle=teststand path=range-checking-strict-and-loose-enumerations.html language=enus -->
## TOPIC 00743: Range Checking: Strict and Loose Enumerations

- bundle_id: `teststand`
- source_path: `range-checking-strict-and-loose-enumerations.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/range-checking-strict-and-loose-enumerations.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: TestStand enumerations can be either strict or loose. A loose enumeration can take on any numeric value. Enumerations in C, C++, and C# can be described as loose in this sense. A strict enumeration can take on only those values specified by its enumerators. Attempting to set a strict TestStand enume

### Range Checking: Strict and Loose Enumerations

TestStand enumerations can be either strict or loose. A loose enumeration can take on any numeric value. Enumerations in C, C++, and C# can be described as loose in this sense. A strict enumeration can take on only those values specified by its enumerators. Attempting to set a strict TestStand enumeration to a value that does not correspond to its enumerators results in an error. Use the Edit Enumerators dialog box to specify that an enumeration data type is strict or loose.

Parent topic:

Getting Started Creating a TestStand Enumeration

<!--NI_TOPIC bundle=teststand path=reading-from-csv-files-with-data-streams-step.html language=enus -->
## TOPIC 00744: Reading from CSV Files with Data Streams Step Types

- bundle_id: `teststand`
- source_path: `reading-from-csv-files-with-data-streams-step.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/reading-from-csv-files-with-data-streams-step.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the New CSV Input Stream step type to open a CSV file for reading and store a reference to it. In addition to specifying the path to the input file, you can specify a tag to search for and/or some number of lines to skip. These options enable reading from files that are not completely homogenous

### Reading from CSV Files with Data Streams Step Types

Use the New CSV Input Stream step type to open a CSV file for reading and store a reference to it. In addition to specifying the path to the input file, you can specify a tag to search for and/or some number of lines to skip. These options enable reading from files that are not completely homogenous. For example, it is common for a CSV file to have metadata at the top (the date, time, operator id, location, etc.) followed by column headers, and then the main data table. The combination of scanning for a specific string and/or skipping a fixed number of lines allows the New CSV Input Record Stream step type to prepare such a file for reading with a for each loop. You can use the API to read more complex files.

Note

You must close the CSV file when you are finished. You can close the CSV file by calling the InputRecordStream.Close() method through the API. Alternatively, you can configure the For Each step type to close the file automatically when the loop terminates.

Parent topic:

Using the Data Streams Step Type

<!--NI_TOPIC bundle=teststand path=reading-parameter-information-for-a-dll.html language=enus -->
## TOPIC 00745: Reading Parameter Information for a DLL

- bundle_id: `teststand`
- source_path: `reading-parameter-information-for-a-dll.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/reading-parameter-information-for-a-dll.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: When a DLL contains export information or when a DLL file contains a type library, the LabWindows/CVI and C/C++ DLL Adapters automatically populate the Function control on the Module tab of the step with all the function names exported from the DLL. In addition, when you select a function in the DLL

### Reading Parameter Information for a DLL

When a DLL contains export information or when a DLL file contains a type library, the LabWindows/CVI and C/C++ DLL Adapters automatically populate the Function control on the Module tab of the step with all the function names exported from the DLL.

In addition, when you select a function in the DLL, the adapter queries the export information or the type library for the parameter list information and displays it in the Parameters Table control on the Module tab. When the adapter cannot determine parameter information, you must enter the parameter information manually.

Parent topic:

Calling DLLs from TestStand

Related concepts:

- Programming with the TestStand API in LabWindows/CVI
- Organizing Test Program Files with LabVIEW-Built Shared Libraries
- Adding Type Libraries to LabWindows/CVI DLLs
- Generating Type Library Information to Include in a DLL

<!--NI_TOPIC bundle=teststand path=redistributing-msi-based-installer-products-i.html language=enus -->
## TOPIC 00746: Redistributing MSI-based Installer Products in a Deployment

- bundle_id: `teststand`
- source_path: `redistributing-msi-based-installer-products-i.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/redistributing-msi-based-installer-products-i.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can install a product and then include that product in an MSI-based installer you build to redistribute the product with a deployment. NI provides product distributions for you to include in the deployments you create. By redistributing products in a single, customized MSI-based installer that i

### Redistributing MSI-based Installer Products in a Deployment

You can install a product and then include that product in an MSI-based installer you build to
 redistribute the product with a deployment. NI provides product distributions for
 you to include in the deployments you create. By redistributing products in a
 single, customized MSI-based installer that includes only the features of the
 product the test system requires, you can streamline the installation process so
 users can avoid separately installing multiple products with specialized feature
 sets. Redistributing products in a single MSI-based installer also avoids the need
 to distribute multiple distribution media along with the test system you deploy.

#### Redistribution Using Merge Modules in TestStand 3.0 and 3.1

In TestStand 3.0 and 3.1, you could use the deployment utility to redistribute the TestStand Engine by recreating the MSI-based installer from a Microsoft Windows Installer database file and a large number of merge modules. However, using this technique caused the following issues:

- You could not extract merge modules once you merged the files into a Windows Installer database file. Therefore, the TestStand MSI-based installer had to include copies of all the merge modules needed to rebuild itself, which nearly doubled the size of the TestStand MSI-based installer.
- Merging a large number of merge modules and building MSI-based installers was time-consuming and
 did not scale well for large distributions with multiple products, such as
 multiple NI drivers.
- This technique supported only a few NI products. Adding support for other NI products was
 difficult because no standard existed for obtaining merge module dependencies.
 The deployment utility hard-coded dependency information for all merge modules
 TestStand installed. Additionally, no registry existed for all the merge modules
 installed on a computer, and the deployment utility could use only the merge
 modules TestStand installed.

#### Redistribution Using the NI MSI-based
 Installer Architecture in TestStand 3.5 or Later

To overcome the issues of
 using merge modules to redistribute products, NI developed an MSI-based installer
 architecture to create and redistribute parts using the same binary files to install
 and uninstall parts and to create distributions. Use the NI MSI-based installer
 architecture to accomplish the following tasks:

- Provide a consistent experience across NI development systems, such as
 TestStand, LabVIEW, and LabWindows/CVI.
- Create distributions that consist of one developer part, any number of
 redistributable NI parts, and support files required to install the parts. The
 developer part contains files you add to the distribution by using the
 deployment utility and MSI-based installer tables that perform actions
 associated with those files during installation, such as registering ActiveX
 Automation servers, creating shortcuts, and importing hardware configuration
 files into Measurement & Automation Explorer.
- Upgrade the NI MSI-based installer architecture independently of upgrading
 TestStand.
- Define a framework to register products and dependencies during
 installation.
- Provide a way for products to define different flavors, which are subsets of
 features that you can redistribute, such as a run-time version that excludes
 development features.

Parent topic:

Relationship of NI MSI-based Installer Architecture and Microsoft Windows Installer Technology

Related concepts:

- Microsoft Windows Merge Modules
- NI MSI-based Installer Architecture

<!--NI_TOPIC bundle=teststand path=registering-a-crash-recovery-sequence.html language=enus -->
## TOPIC 00747: Registering a Crash Recovery Sequence

- bundle_id: `teststand`
- source_path: `registering-a-crash-recovery-sequence.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/registering-a-crash-recovery-sequence.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can register sequences to respond to a crash in your TestStand application to return any hardware or other system assets into a good state. The sequences are executed by an external process and run without a process model or a logged-in user. Since multiple crash recovery sequences can be regist

### Registering a Crash Recovery Sequence

You can register sequences to respond to a crash in your TestStand application to return any hardware or other system assets into a good state. The sequences are executed by an external process and run without a process model or a logged-in user. Since multiple crash recovery sequences can be registered, the order in which the sequences will be executed is the order in which they are registered.

Any errors encountered in executing crash recovery sequences are recorded in a log file, and a dialog displays the location of the log file. Similar to the main application TestStand crash log, this log file stores the errors from a maximum of 100 crash callbacks.

To register a sequence for execution in the case of a crash you must call Engine.RegisterSequenceToExecuteOnCrash with the sequence name and file path to be executed. This function returns a unique ID that can be used to unregister the sequence later with a call to Engine.UnregisterSeuqenceToExecuteOnCrash.

Parent topic:

Crash Recovery for TestStand Applications

<!--NI_TOPIC bundle=teststand path=relationship-of-national-instruments-msi-base.html language=enus -->
## TOPIC 00748: Relationship of NI MSI-based Installer Architecture and Microsoft Windows Installer Technology

- bundle_id: `teststand`
- source_path: `relationship-of-national-instruments-msi-base.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/relationship-of-national-instruments-msi-base.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use Microsoft Windows Installer technology in conjunction with the NI MSI-based installer architecture to redistribute NI drivers and other software components, such as run-time engines, with a deployment. A Windows Installer installs, uninstalls, and repairs applications. For a single application,

### Relationship of NI MSI-based Installer
 Architecture and Microsoft Windows Installer Technology

Use Microsoft Windows Installer technology in conjunction with the NI MSI-based installer
 architecture to redistribute NI drivers and other software components, such as
 run-time engines, with a deployment.

A Windows Installer installs, uninstalls, and repairs applications. For a single application, a Windows installation package includes a Windows Installer database file (.msi), which contains all the information a Windows Installer requires to install or uninstall an application and to run the setup user interface.

You can use Windows Installer technology to accomplish the following tasks:

- Support unattended program installation —You can script a program installation according to administrator instructions.
- Help prevent certain forms of inter-program conflicts —The MSI-based installer enforces installation rules that help prevent conflicts that can occur when an installation or removal operation makes updates to or deletes a DLL an existing program shares.
- Diagnose and repair corrupted programs —You can determine whether an installed program has missing or corrupted files and repair the program by reinstalling only the missing or corrupted files.
- Reliably remove existing programs —The MSI-based installer can remove any program it previously installed, including all associated registry entries and program files, except for files other installed software shares.
- Support on-demand installation of program features —The MSI-based installer can initially install only a minimal subset of program features. You can automatically install additional components the first time you use a feature that requires the components.
- Restore the original computer state if an installation failure occurs —A Windows Installer records all changes made to the computer during the program installation process and can restore the computer to its initial state, also known as a rollback.

Parent topic:

Building a Customized MSI-based Installer

Related concepts:

- NI MSI-based Installer Architecture
- Redistributing MSI-based Installer Products in a Deployment

<!--NI_TOPIC bundle=teststand path=releasing-activex-references-in-labview.html language=enus -->
## TOPIC 00749: Releasing ActiveX References in LabVIEW

- bundle_id: `teststand`
- source_path: `releasing-activex-references-in-labview.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/releasing-activex-references-in-labview.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: When a method or property returns an ActiveX reference, you must use the Automation Close function in LabVIEW to release the reference. If you do not release the ActiveX reference, LabVIEW does not release it for you until the VI hierarchy finishes executing. Repeatedly opening references to objects

### Releasing ActiveX References in LabVIEW

When a method or property returns an ActiveX reference, you must use the Automation Close function in LabVIEW to release the reference.

Note

Parent topic:

Adding and Releasing References

<!--NI_TOPIC bundle=teststand path=remote-execution-in-32-bit-teststand-and-64-b.html language=enus -->
## TOPIC 00750: Remote Execution in 32-bit TestStand and 64-bit TestStand

- bundle_id: `teststand`
- source_path: `remote-execution-in-32-bit-teststand-and-64-b.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/remote-execution-in-32-bit-teststand-and-64-b.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: When you select Use Remote Computer in Execution Options on the Sequence Call Module tab or Run Sequence on Remote Computer in the Multithreading and Remote Execution option in the Edit Sequence Call dialog box of a TestStand User Interface to execute a sequence remotely, you can select the bitness

### Remote Execution in 32-bit TestStand and 64-bit TestStand

When you select Use Remote Computer in Execution Options on the Sequence Call Module tab or Run Sequence on Remote Computer in the Multithreading and Remote Execution option in the Edit Sequence Call dialog box of a TestStand User Interface to execute a sequence remotely, you can select the bitness of the TestStand remote engine to use. By default, TestStand connects to the remote engine with the matching bitness if available on the specified host. To specify the bitness of the TestStand remote engine to use on the remote computer, use a 32\\ prefix to use the 32-bit TestStand Engine or use a 64\\ prefix to use the 64-bit TestStand Engine in the Remote Host control of the Sequence Call Advanced Settings dialog box or in the Remote Host control in the Remote Execution Settings dialog box of a TestStand User Interface.

You can use remote sequence execution as a workaround to use 32-bit TestStand features that 64-bit TestStand does not support. For example, 64-bit TestStand can use 32-bit TestStand to execute a sequence that uses the HTBasic Adapter. Similarly, you can specify that 64-bit TestStand use 32-bit TestStand to execute sequences that invoke 32-bit code modules or vice versa. Complete the following steps to call into a specific bitness of TestStand on the same computer.

1. Enable the Allow Sequence Calls from Remote Computer to Run on this Computer option on the Remote Execution tab of the Station Options dialog box.
2. Specify 32\\localhost or 64\\localhost for the remote host setting of the sequence call.

Note

Parent topic:

Sequence Call Adapter Support for 64-bit TestStand
