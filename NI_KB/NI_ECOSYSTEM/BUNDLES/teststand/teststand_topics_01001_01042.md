# NI DOCUMENT BUNDLE: teststand

<!--NI_BUNDLE_CHUNK bundle=teststand start=1001 end=1042 -->
<!--NI_TOPIC bundle=teststand path=using-teststand-ui-controls-in-labview.html language=enus -->
## TOPIC 01001: Using TestStand UI Controls in LabVIEW

- bundle_id: `teststand`
- source_path: `using-teststand-ui-controls-in-labview.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/using-teststand-ui-controls-in-labview.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can create custom user interfaces and create user interfaces for other components, such as custom step types. Use the TestStand User Interface (UI) Controls on the Controls»TestStand palette in LabVIEW to develop a custom user interface application, including custom sequence editors. When you pl

### Using TestStand UI Controls in LabVIEW

You can create custom user interfaces and create user interfaces for other components, such as custom step types. Use the TestStand User Interface (UI) Controls on the Controls»TestStand palette in LabVIEW to develop a custom user interface application, including custom sequence editors.

When you place TestStand UI Controls on the front panel of a VI, you can use the LabVIEWActiveX functionality to program the controls. You can also configure the controls interactively using the LabVIEW ActiveX Property Browser or control property pages if available. Right-click the control and select Property Browser from the context menu to open the LabVIEW ActiveX Property Browser. Right-click the control and select Properties from the context menu to launch the property page.

#### TestStand VIs and Functions

The TestStand VIs and functions on the Functions»TestStand palette in LabVIEW are the LabVIEW versions of the functions in the TestStand Utility (TSUtil) Functions Library.

Use the TestStand VIs and functions for the following tasks:

- Inserting menu items that automatically execute commands the TestStand UI Controls provide
- Localizing the strings in a user interface
- Making dialog boxes VIs launch modal to TestStand applications
- Determining whether an execution that calls a VI code module is terminating or aborting
- Allowing the calling execution thread to suspend when a VI code module performs a lengthy operation
- Setting and obtaining the values of TestStand properties and variables

Right-click the VI on the Functions palette or on the block diagram and select Help from the context menu to access the help for the VI.

#### TestStand Version Selector

The TestStand Version Selector installs the Controls»TestStand palette and the Functions»TestStand palette when it detects an installation of LabVIEW. If you have just installed a new version of LabVIEW, the palettes do not appear in LabVIEW until you launch the TestStand Engine, at which point the TestStand Version Selector detects the new version of LabVIEW and installs the palette files. You can also launch the TestStand Version Selector, select the current version of TestStand, and click the Make Active button to re-activate the current version of TestStand and to re-install the palette files.

Note

Parent topic:

Using TestStand UI Controls in Different Environments

Related concepts:

- TestStand UI Controls
- TestStand Utility Functions Library
- Starting and Shutting Down TestStand from a .NET User Interface
- Programming with the TestStand API in LabVIEW
- Starting and Shutting Down TestStand from a LabVIEW User Interface

<!--NI_TOPIC bundle=teststand path=using-teststand-ui-controls-in-labwindows-cvi.html language=enus -->
## TOPIC 01002: Using TestStand UI Controls in LabWindows/CVI

- bundle_id: `teststand`
- source_path: `using-teststand-ui-controls-in-labwindows-cvi.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/using-teststand-ui-controls-in-labwindows-cvi.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can create custom user interfaces and create user interfaces for other components, such as custom step types. Use the TestStand User Interface (UI) Controls in the LabWindows/CVI development environment to develop a custom user interface application, including custom sequence editors. Creating a

### Using TestStand UI Controls in LabWindows/CVI

You can create custom user interfaces and create user interfaces for other components, such as custom step types. Use the TestStand User Interface (UI) Controls in the LabWindows/CVI development environment to develop a custom user interface application, including custom sequence editors.

#### Creating and Configuring ActiveX Controls

In the LabWindows/CVI User Interface Editor, select Create»ActiveX and select a user interface control beginning with TestStand UI to add a TestStand UI Control to a panel. Double-click the control to launch the standard LabWindows/CVI Edit Control dialog box, in which you can configure the control. Right-click the control and select Properties from the context menu to open the property pages the UI control supports.

#### Programming with ActiveX Controls

To access the methods, properties, and events specific to an ActiveX control, you must use the ActiveX driver for the control. The TestStand UI Controls driver and additional support instrument drivers are located in the <TestStand>\API\CVI directory. TestStand copies these instrument driver files (.h, .c, .fp, and .obj) to the <National Instruments>\Shared\CVI\instr\TestStand\API directory. The TestStand Version Selector copies API files for earlier versions of LabWindows/CVI to the appropriate locations.

Add the following function panel files to the LabWindows/CVI project for a TestStand application and add the corresponding header files in the source code files that use the API:

- TestStand UI Controls 
 (tsui.fp) —Functions for dynamically creating controls, calling methods and accessing properties on controls, and handling events from the controls.
- TestStand UI Support Library 
 (tsuisupp.fp) —Functions for various collections the TestStand UI Controls driver uses.
- TestStand Utility Functions 
 (tsutil.fp) —Utility functions for managing menu items that correspond to TestStand commands, localizing strings in user interfaces, making dialog boxes associated with LabWindows/CVI code modules modal to TestStand applications, and checking if an execution that calls a code module has stopped.
- TestStand API 
 (tsapicvi.fp) —Provides low-level access to TestStand objects.

For each interface the ActiveX control supports, the driver contains a function you can use to programmatically create an instance of the ActiveX control. The ActiveX driver also includes functions you can use to register callback functions for receiving events the control defines.

When you store ActiveX controls in .uir files, you do not need to use the creation functions the driver includes because the control is created when you load the panel from the file using the LoadPanel function. You identify the control in subsequent calls to User Interface Library functions with the constant name you assigned to the control in the User Interface Editor.

When you use other functions in the driver, you must identify the control with a unique object handle that LabWindows/CVI then associates with the control. You obtain this handle when you call the GetObjHandleFromActiveXCtrl function using the constant name for the control. This handle is cached in the control, and you do not need to discard the handle explicitly.

LabWindows/CVI requires you to initialize a thread as apartment-threaded before you can use ActiveX controls in a program. When you do not initialize the thread before creating an ActiveX control or before loading a panel containing an ActiveX control from a .uir file, LabWindows/CVI automatically initializes the thread to apartment-threaded. When you use the CA_InitActiveXThreadStyleForCurrentThread function to initialize the thread yourself, you must use COINIT_APARTMENTTHREADED as the threading model.

#### Include Files and Instrument Search
 Directories

The TestStand Version Selector automatically adds the additional required API files to
 shared directories for the installed versions of LabWindows/CVI. If you have just installed
 a new version of LabWindows/CVI, the API files are not available until after you launch the
 TestStand Engine, at which point the TestStand Version Selector detects the new version of
 LabWindows/CVI and copies the required API files. You can also launch the TestStand Version
 Selector, select the current version of TestStand, and click the Make
 Active button to re-activate the current version of TestStand and to re-copy
 the API files.

Note

Parent topic:

Using TestStand UI Controls in Different Environments

Related concepts:

- TestStand UI Controls
- TestStand Directory Structure
- Starting and Shutting Down TestStand from a LabWindows/CVI User Interface
- Launching an MFC Dialog with ActiveX Controls
- Programming with the TestStand API in LabWindows/CVI

<!--NI_TOPIC bundle=teststand path=using-teststand-ui-controls-in-ms-net.html language=enus -->
## TOPIC 01003: Using TestStand UI Controls in Microsoft Visual Studio

- bundle_id: `teststand`
- source_path: `using-teststand-ui-controls-in-ms-net.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/using-teststand-ui-controls-in-ms-net.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: To use the TestStand User Interface (UI) Controls in Microsoft Visual Studio, drag the TestStand UI Controls from the TestStand tab on the Visual Studio Toolbox onto a form. When you create a new project in a supported version of Visual Studio, select Project»Project Name Properties, click the Build

### Using TestStand UI Controls in Microsoft
 Visual Studio

To use the TestStand User Interface (UI) Controls in Microsoft Visual Studio, drag the TestStand UI Controls from the TestStand tab on the Visual Studio Toolbox onto a form.

When you create a new project in a supported version of Visual Studio, select Project»Project Name Properties, click the Build tab, and select x86 from the Platform Target ring control in the General section of the dialog box so the project can access the TestStand API and UI Controls on 64-bit versions of Microsoft Windows.

Visit ni.com/info and enter the Info Code tsuivs2010 to access
 the NI KnowledgeBase article 5NK6NKXU, Why do I Receive an Error when Using Visual
 Studio 2010 to Build a TestStand User Interface?, for information about building
 TestStand user interfaces in Visual Studio 2010.

If the Visual Studio Toolbox window does not display the TestStand tab when you edit a form, or if the TestStand Interop assemblies do not appear in the Add References dialog box, exit all running copies of Visual Studio, launch the TestStand Version Selector, select the current version of TestStand, and click the Make Active button.

You must also add references to the TestStand Interop assemblies and the TestStand Utility (TSUtil) assembly to the project.

When you create a Multiple Document Interface (MDI) application with TestStand UI Controls
 on an MDI child form, Microsoft .NET resets the properties you programmatically set on the
 TestStand UI Controls to default values when you set the MdiParent property
 on the child form. .NET resets these properties because .NET destroys and recreates ActiveX
 controls on a form when you set the property on the form. To avoid this issue, set the
 TestStand control properties after you set the MdiParent property on the
 form or place all TestStand UI Controls and other ActiveX controls on a Panel control
 instead of directly on the form.

Note

Parent topic:

Using TestStand UI Controls in Different Environments

Related concepts:

- TestStand UI Controls
- Adding Assembly References in Microsoft Visual Studio
- TestStand Utility Functions Library
- Starting and Shutting Down TestStand from a .NET User Interface
- Programming with the TestStand API in C#

<!--NI_TOPIC bundle=teststand path=using-teststand-ui-controls-in-msvc.html language=enus -->
## TOPIC 01004: Using TestStand UI Controls in Microsoft Visual C++

- bundle_id: `teststand`
- source_path: `using-teststand-ui-controls-in-msvc.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/using-teststand-ui-controls-in-msvc.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: To use the TestStand User Interface (UI) Controls in Microsoft Visual C++, add the TestStand Utility (TSUtil) Functions Library to the project. The TSUtilCPP.cpp and TSUtilCPP.h files automatically import the type libraries for the TestStand API and the TestStand User Interface (UI) Controls. You ca

### Using TestStand UI Controls in Microsoft Visual C++

To use the TestStand User Interface (UI) Controls in Microsoft Visual C++, add the TestStand Utility (TSUtil) Functions Library to the project. The TSUtilCPP.cpp and TSUtilCPP.h files automatically import the type libraries for the TestStand API and the TestStand User Interface (UI) Controls.

You can view the header files the #import directive generates for the TestStand API type libraries by opening the tsui.tlh, tsuisupp.tlh, and tsapi.tlh files Visual C++ creates in the Debug or Release directory. The header files the #import directive generates define a C++ class for each object class in the TestStand API. The I prefix in class names denotes ActiveX controls and objects you can create without calling another class. The header files use macros to define a corresponding smart pointer class for each object class. Each smart pointer class uses the name of the corresponding class and adds a Ptr suffix. Typically, you use only smart pointer classes in an application because the smart pointer releases the reference to the object when the pointer is destroyed. For example, instead of using the SequenceFile class, use the SequenceFilePtr class.

Note

#import

Select Insert ActiveX Control from the dialog box context menu and select a control that begins with TestStand UI to add a TestStand UI Control to a dialog box as a resource.

When you programmatically create a TestStand UI Control in an MFC container, you must remove the WS_CLIPSIBLINGS style from the control window for the TestStand UI Control to remain visible inside an MFC Group Box control. If you do not remove the WS_CLIPSIBLINGS style, a native MFC control always obscures the TestStand UI Control, even when the MFC control comes after the TestStand UI Control in the tab order.

#### Obtaining an Interface Pointer and
 CWnd for an ActiveX Control

Complete the following steps to obtain an
 interface pointer to an ActiveX control, such as a TestStand User Interface (UI)
 control, that you insert into an Microsoft Foundation Class (MFC) dialog
 resource.

1. Add a CWnd member to the dialog class for the control as
 follows: CWnd mExprEditCWnd;
2. Insert the following code into the OnInitDialog method of the
 dialog class: mExprEditCWnd.Attach(GetDlgItem
 (IDC_MYEXPRESSIONEDIT)->m_hWnd);
3. Obtain the interface pointer from the CWnd member as
 follows: TSUI::IExpressionEditPtr myExprEdit =
 mExprEditCWnd.GetControlUnknown();

Note

DoDataExchange

CWnd

DoDataExchange

Parent topic:

Using TestStand UI Controls in Different Environments

Related concepts:

- TestStand UI Controls
- TestStand Utility Functions Library
- TestStand ActiveX API Overview
- Programming with the TestStand API in Microsoft Visual C++

<!--NI_TOPIC bundle=teststand path=using-the-platform-path-macro-to-locate-the-c.html language=enus -->
## TOPIC 01005: Using the $(Platform) Path Macro to Locate the Correct Code Module in 32-bit TestStand and 64-bit TestStand

- bundle_id: `teststand`
- source_path: `using-the-platform-path-macro-to-locate-the-c.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/using-the-platform-path-macro-to-locate-the-c.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use the $(Platform) path macro to simultaneously associate a step or sequence with the 32-bit version and the 64-bit version of a code module. 32-bit TestStand expands the $(Platform) macro to win32, and 64-bit TestStand expands the macro to x64. All adapters that require paths to code modul

### Using the $(Platform) Path Macro to Locate the Correct Code Module in 32-bit TestStand and 64-bit TestStand

You can use the $(Platform) path macro to simultaneously associate a step or sequence with the 32-bit version and the 64-bit version of a code module. 32-bit TestStand expands the $(Platform) macro to win32, and 64-bit TestStand expands the macro to x64. All adapters that require paths to code modules support the $(Platform) macro.

The TestStand Engine API supports the $(Platform) macro in the following methods:

- Engine.FindFileEx
- Engine.FindPath
- Engine.ExpandPathMacros

The Engine.FindFileEx and Engine.FindPath methods expand the $(Platform) macro automatically when searching for files or paths. The Engine.ExpandPathMacros method evaluates and expands the $(Platform) macro in a path string to provide lower-level access to the macro functionality when needed.

When a path name includes the $(Platform) macro, TestStand ignores the Search Subdirectories setting in the Edit Search Directories dialog box to avoid the conflicts that would otherwise arise when multiple copies of a file with the same name reside under the same root directory.

Parent topic:

Locating the Correct Code Module in 32-bit TestStand and 64-bit TestStand

Related concepts:

- Adapter and Code Module Support for 64-bit TestStand

<!--NI_TOPIC bundle=teststand path=using-the-teststand-version-selector.html language=enus -->
## TOPIC 01006: Using the TestStand Version Selector

- bundle_id: `teststand`
- source_path: `using-the-teststand-version-selector.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/using-the-teststand-version-selector.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Although you can install more than one version of TestStand on a computer, only one version of TestStand can be active and run at a time. The TestStand Version Selector application indicates the active version of TestStand and can activate a different version of TestStand. The TestStand Version Sele

### Using the TestStand Version Selector

Although you can install more than one version of TestStand on a computer, only one
 version of TestStand can be active and run at a time. The TestStand Version Selector
 application indicates the active version of TestStand and can activate a different version
 of TestStand.

TSVerSelect.exe

<Program Files>\National Instruments\Shared\TestStand Version
 Selector

Start

»

NI

»

TestStand Version Selector

Note

/reqadmin

The Current Active Version control shows the currently active
 version of TestStand. Select a version in the Installed TestStand
 Versions control and click Activate to activate a
 specific version of TestStand. The Path to 32-bit Version and
 Path to 64-bit Version controls show the locations of the
 selected version of TestStand.

When activation is complete, the selector displays a message to indicate success or
 display any warnings. Click Launch 32-bit or Launch
 64-bit to run the sequence editor application for the active version and
 bitness of TestStand.

If you activate TestStand and run a TestStand User Interface from a previous TestStand
 version, the user interface uses the TestStand Engine, step types, and components for
 the active TestStand version. User interfaces and sequence editors created with older
 versions of TestStand may not run as expected if a newer version of TestStand is
 active.

Parent topic:

TestStand Version Selector

<!--NI_TOPIC bundle=teststand path=using-two-separate-variables-to-represent-poi.html language=enus -->
## TOPIC 01007: Using Two Separate Variables to Represent Pointer-Sized Numbers in Sequences in 32-bit TestStand and 64-bit TestStand

- bundle_id: `teststand`
- source_path: `using-two-separate-variables-to-represent-poi.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/using-two-separate-variables-to-represent-poi.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: When you cannot change the representation of a variable, such as in a type instance, create one instance of the variable for 32-bit TestStand and another instance of the variable for 64-bit TestStand. Use bitness-conditional code to access the appropriate variable.

### Using Two Separate Variables to Represent Pointer-Sized Numbers in Sequences in 32-bit TestStand and 64-bit TestStand

When you cannot change the representation of a variable, such as in a type instance, create one instance of the variable for 32-bit TestStand and another instance of the variable for 64-bit TestStand. Use bitness-conditional code to access the appropriate variable.

Parent topic:

Representing Pointer-Sized Numbers in Sequences in 32-bit TestStand and 64-bit TestStand

<!--NI_TOPIC bundle=teststand path=using-type-palette-files-to-restrict-automati.html language=enus -->
## TOPIC 01008: Using Type Palette Files to Restrict Automatic Type Conflict Resolution

- bundle_id: `teststand`
- source_path: `using-type-palette-files-to-restrict-automati.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/using-type-palette-files-to-restrict-automati.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: To avoid unwanted type version propagation, create all types in type palette files and use the default behavior of the Allow Automatic Type Conflict Resolution option on the File tab of the Station Options dialog box. Common Scenarios for Allow Automatic Type Conflict Resolution Options The followin

### Using Type Palette Files to Restrict Automatic Type Conflict Resolution

To avoid unwanted type version propagation, create all types in type palette files and use the default behavior of the Allow Automatic Type Conflict Resolution option on the File tab of the Station Options dialog box.

#### Common Scenarios for Allow Automatic
 Type Conflict Resolution Options

The following table lists each of the
 Allow Automatic Type Conflict Resolution options on the File tab of the Station
 Options dialog box and common scenarios for using each option.

| Allow Automatic Type Conflict Resolution Option | Common Scenarios for Option |
| --- | --- |
| Only if Type Palette Files will not be Modified (default) | You want type palette files to be the only location in which you strictly define types. You do not want to allow any changes to types located in type palette files without the user explicitly deciding to do so. |
| Only if a Type Palette File has the Higher Version | You want type palette files to be the only location in which you strictly define types. You do not want to allow any changes to types located in type palette files without the user explicitly deciding to do so. You do not want to allow automatic conflict resolution for types that exist only in sequence files and not in type palette files to avoid mismatched versions of types. |
| Always (same as TestStand 4.0.x or earlier) | None. Use this option only for compatibility with versions of TestStand earlier than version 4.1. |
| Never | You want to ensure that all files use exactly the same version of all their types. |

Parent topic:

Managing Type Revisions

<!--NI_TOPIC bundle=teststand path=using-variables-and-properties.html language=enus -->
## TOPIC 01009: Using Variables and Properties

- bundle_id: `teststand`
- source_path: `using-variables-and-properties.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/using-variables-and-properties.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can create and use variables and properties and monitor the values of the variables and properties. You can define the following types of variables to share data among steps of a sequence or among several sequences: Local variables store data relevant to only the current sequence. Only steps wit

### Using Variables and Properties

You can create and use variables and properties and monitor the values of the variables and properties.

You can define the following types of variables to share data among steps of a sequence or among several sequences:

- Local variables store data relevant to only the current sequence. Only steps within the sequence that defines the local variable can access these variables.
- Sequence file global variables store data relevant to the entire sequence file. Each sequence and step in the sequence file can directly access these global variables.
- Station global variables persist across different executions. The TestStand Engine maintains the value of station global variables in a file on the computer on which TestStand is running.

In the sequence editor, the Variables pane displays all the variables and properties the selected sequence can access at run time. In the Execution window, the Variables pane displays the sequence context for the sequence invocation currently selected on the Call Stack pane. The sequence context contains all the variables and properties the steps in the selected sequence invocation can access. Use the Variables pane to examine and modify the values of these variables and properties when the sequence is in a suspended state, such as when paused at a breakpoint.

Note

<TestStand Public>\Tutorial\Solution

#### Creating Local Variables

Complete the following steps to create and use local variables. You can apply the concepts you learn in this tutorial to sequence file global and station global variables.

1. Open <TestStand Public>\Tutorial\Computer2.seq , which you created in Editing Steps in a Sequence.
2. Select File»Save <filename> As and save the sequence file as Computer4.seq in the <TestStand Public>\Tutorial directory.
3. Click the Variables pane in the Sequence File window. Expand the Locals item to view the local variables currently defined for MainSequence . Each sequence includes a ResultList local variable, which is an empty array of container properties. TestStand uses this variable to store step results for result processing.
4. On the Variables pane, right-click Locals , select Insert Local»Number from the context menu to insert a new numeric local variable, and rename the local variable LoopIndex .
5. Complete the following steps to insert and configure a For step.
  1. Click the Steps pane in the Sequence File window and insert a Flow Control»For step below the Retry Power On step. Notice that TestStand also adds an End step below the For step.
  2. Drag the End step below the RAM step. TestStand automatically indents the Retry Power On, CPU Test, ROM, and RAM steps between the For and End steps.
  3. Click the For step and click the For Loop tab of the Step Settings pane.
  4. Enter 5 in the Number of Loops control.
  5. For the Loop Variable control, click the Expression Browser button to launch the Expression Browser dialog box, in which you can interactively build an expression by selecting from lists of variables, properties, operators, functions, and the TestStand API. TestStand supports all applicable expression operators and syntax you can use in C, C++, Java, and Visual Basic .NET. You can also call the TestStand API directly from within expressions. All TestStand controls that accept expressions provide context-sensitive editing features, such as drop-down lists, syntax checking, and expression coloring to help you create expressions. At any point while editing an expression, you can press <Ctrl-Space> to show a drop-down list of valid expression elements.
  6. Expand the Locals item on the Variables/Properties tab of the Expression Browser dialog box. Each item in the top section of the Variables/Properties tab is a property or variable of TestStand.
  7. Select the LoopIndex variable under the Locals property and click the Insert button. The Expression Browser enters Locals.LoopIndex in the Expression control. Note To refer to a subproperty, use a period to separate the name of the property from the name of the subproperty. For example, reference the LoopIndex subproperty of the Locals property as Locals.LoopIndex.
  8. Click the Check Expression for Errors button to verify that the expression contains valid syntax.
  9. In the Expression Browser dialog box, click OK to return to the For Loop tab of the Step Settings pane. The Loop Variable control now contains the Locals.LoopIndex expression. Notice that the Custom Loop section shows the expressions TestStand uses when executing the For step when using a fixed number of loops.
6. Select Execute»Break on First Step to remove the checkmark that appears to the left of the menu item and disable this option, which you enabled in the Step Mode Execution section of Debugging Sequences.
7. Save the changes and select Execute»Single Pass .
8. Click Done in the Test Simulator dialog box.
9. After the sequence executes, review the test report, which shows that TestStand executed the steps within the loop (Retry Power On, CPU Test, ROM, and RAM) five times.
10. Close the Execution window. Leave the sequence file open for the next tutorial.

#### Using the Execution Window Variables
 Pane

Before executing the steps in a sequence, TestStand creates a
 run-time copy of the sequence to maintain separate local variable and step property
 values for each sequence invocation. When an execution completes, TestStand discards
 the run-time sequence copy.

For each active sequence, TestStand maintains a
 sequence context that contains references to the run-time copy of the sequence so
 you can access all the objects, variables, and properties that relate to the
 execution of the sequence.

The contents of the sequence context vary depending
 on the currently executing sequence and step, the location of the active sequence in
 the call stack, and the identity of the execution in which the active sequence
 resides. Depending on the current state of execution, sequence context subproperties
 might not exist. When a property exists, the contents of the property can
 vary.

The Variables pane displays the sequence context for the sequence
 invocation currently selected on the Call Stack pane. The sequence context contains
 all the variables and properties the steps in the selected sequence invocation can
 access. Use the Variables pane to examine and modify the values of these variables
 and properties when the sequence is in a suspended state, such as when paused at a
 breakpoint.

| Sequence Context Subproperty | Description |
| --- | --- |
| Locals | Contains local variables in the current sequence. Only the current sequence can access these variables. |
| Parameters | Contains parameter variables in the current sequence. Only the current sequence or calling sequences can access these variables. |
| FileGlobals | Contains file global variables in the current sequence file. All the sequences in the current sequence file can access these variables. |
| StationGlobals | Contains station global variables on the computer. Any sequence on the current computer can access these variables. Station global variables are stored on disk and the values persist even after you close TestStand. |
| ThisContext | Contains a reference to the current sequence context. You typically use this property to pass the entire sequence context as an argument to a subsequence or a step code module. |
| RunState | Contains properties that describe the current state of execution. |
| Step | Contains the properties in the currently executing step. The Step property exists only while a step executes. The property does not exist when the execution is between steps, such as at a breakpoint. |

Complete the following steps to use the Variables pane of the Execution
 window to examine the value of the LoopIndex variable while TestStand executes the
 Computer4.seq sequence file you created in the previous
 tutorial.

1. Insert a breakpoint at the End step associated with the For loop you created in
 the previous tutorial.
2. Select Execute»Single Pass .
3. Click Done in the Test Simulator dialog box. The
 execution suspends on the End step.
4. Click the tab for the Variables pane of the Execution window and expand the
 Locals section.
5. Select the LoopIndex property. The numeric value of
 LoopIndex is 0 .
6. Click the tab for the Steps pane of the Execution window and click the
 Resume button on the Debug toolbar. The execution
 resumes and suspends at the End step again.
7. Click the tab for the Variables pane again. The value of
 Locals.LoopIndex is now 1 . Leave the
 execution in the suspended state for the next tutorial.

#### Docking the Variables Pane

The sequence editor contains tabbed windows and panes you can float, dock, resize, and hide. Some panes, such as the Variables pane, must stay attached to the associated Sequence File or Execution window.

Complete the following steps to display the Steps and Variables panes at the same time.

1. In the Execution window, click the tab for the Variables pane and drag it to the right
 using the tab, not the title bar. As you drag the pane from the current location, the
 sequence editor detaches the pane and displays docking guides. The docking guides show you
 where you can place the pane. As you move the mouse over a docking guide, the sequence
 editor highlights where the pane will relocate when dropped.
2. Drop the pane on the right-most docking guide, so the pane appears to the right of the
 Steps panes.
3. Click the tab for the Steps pane and click the Resume button on the Debug toolbar. The execution resumes and suspends at the End step again. The value of Locals.LoopIndex on the Variables pane is now 2 .
4. Drag the title bar of the Variables pane and drop it on the center docking guide, to
 return the Variables pane to the previous location. Notice that the tab for the Variables
 pane now appears to the left of the tab for the Steps pane instead of to the right.
5. Click the tab for the Variables pane, drag it to the right, and drop it on the Steps pane tab to adjust the order of the tabs. Leave the execution in the suspended state for the next tutorial. Note Select View»Reset UI Configuration at any time to restore the panes to the original state.

#### Using the Watch View
 Pane

The Watch View pane of the Execution window displays the values of
 watch expressions you enter. The values in the Watch View pane update when execution
 suspends at a breakpoint. When you enable tracing, the sequence editor also updates
 the values after each step executes. The Watch View pane highlights viewed and
 changed watch expression values in red text.

Enter watch expressions to
 monitor values of variables and properties as you trace or step through a sequence.
 You can drag individual variables or properties from the Variables pane to the Watch
 View pane. When you specify a container property, array property, or a
 PropertyObject reference as a watch expression, you can use the Watch View pane to
 expand the subproperties to view the values.

Complete the following steps to
 create a watch expression that uses the LoopIndex property.

1. Select the LoopIndex property on the Variables pane of
 the Execution window and drag the property to the Watch View pane. The value of
 the LoopIndexwatch expression is 2 .
2. Edit the LoopIndex watch expression directly in the Watch Expression column on
 the Watch View pane to change the expression to the following: Str
 (Locals.LoopIndex * 20) + "%"
3. Click the tab for the Steps pane of the Execution window and click the
 Resume button on the Debug toolbar. The execution
 resumes and suspends at the End step again. The value of the watch expression
 changes from 40% to 60% . Note The watch expression pane
 might display an Error in argument message before
 displaying 60% because the watch expression is not valid
 during a subsequence execution.
4. Click the breakpoint icon to the left of the End step in the Execution window to
 remove the breakpoint.
5. Resume and complete the execution.
6. Close the Execution window.
7. Select Debug»Breakpoints/Watches to launch the Edit
 Breakpoints/Watch Expressions dialog box, in which you can review and edit the
 breakpoints and watch expressions associated with the current workspace.
 TestStand saves and reloads breakpoints and watch expressions using an options
 file associated with the current workspace or a default options file when no
 workspace is loaded.
8. Review the contents of the Breakpoints and Watch Expressions tabs in the Edit
 Breakpoints/Watch Expressions dialog box, delete the breakpoint and expression
 you created for this tutorial, and click Done to close
 the dialog box.
9. Close the sequence file.

Parent topic:

Getting Started with TestStand

Related concepts:

- Editing Steps in a Sequence
- Debugging Sequences

<!--NI_TOPIC bundle=teststand path=utilities-for-msvc.html language=enus -->
## TOPIC 01010: Utilities for Microsoft Visual C++/#import

- bundle_id: `teststand`
- source_path: `utilities-for-msvc.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/utilities-for-msvc.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: TestStand provides a set of declarations in the tsvcutil.h file, located in the <TestStand Public>\API\VC directory, to simplify the task of programming when you use the #import directive. Because all identifiers in this header file are enclosed within the namespace TSUTIL, you must prefix all uses

### Utilities for Microsoft Visual C++/#import

TestStand provides a set of declarations in the tsvcutil.h file, located in the <TestStand Public>\API\VC directory, to simplify the task of programming when you use the #import directive. Because all identifiers in this header file are enclosed within the namespace TSUTIL, you must prefix all uses of the templates and classes with TSUTIL::. This file contains the following templates and classes:

- SafeArray template —Simplifies the task of programming with SafeArrays and Standard Template Library containers such as vectors. The following example demonstrates how to convert the SafeArray of PropertyObjectFile objects the Engine.GetTypeUsageLocations method returns into a vector of PropertyObjectFilePtr pointers: #include "tsapivc.h" #include "tsvcutil.h" #include <vector> void GetFilesUsingTypeName(TS::IEngine *engine, const char *typeName, std::vector<TS::PropertyObjectFilePtr> &filesVector) { SAFEARRAY *fileSAFEARRAY; // Get the SAFEARRAY of PropertyObjectFiles fileSAFEARRAY = engine->GetTypeUsageLocations(typeName); // Create a SafeArray object to take ownership of the array returned above. TSUTIL::SafeArray<LPDISPATCH,VT_DISPATCH> fileArray; fileArray.Set(fileSAFEARRAY, true); // Put the SafeArray into a vector fileArray.GetVector(filesVector); } The following example shows how to convert the SafeArray of strings the Engine.DisplayFileDialog method returns into a vector of _bstr_t strings: #include "tsapivc.h" #include "tsvcutil.h" #include <vector> void DisplayFileDialog(TS::IEngine *engine, std::vector<_bstr_t> &selectedPathsVector) { TSUTIL::SafeArray<BSTR, VT_BSTR> selectedPathsSafeArray; TSUTIL::SafeArray<BSTR, VT_BSTR> absolutePathsSafeArray; VARIANT_BOOL gotPath; gotPath = engine->DisplayFileDialog("" /* dialog title */, "" /* ok button */, "" /* initial path */, &selectedPathsSafeArray, &absolutePathsSafeArray, TS::OpenFile_UseAbsolutePath | TS::OpenFile_HideMultiSelectListCtrl, "seq", TS::WinFileDlg_HIDEREADONLY | TS::WinFileDlg_FILEMUSTEXIST | TS::WinFileDlg_ALLOWMULTISELECT, "SequenceFiles|*.seq||", vtMissing /* current file */, &vtMissing, &vtMissing); if (gotPath) absolutePathsSafeArray.GetVector(selectedPathsVector); }
- param_bstr_t class —Receives strings from output parameters, as shown in the following example: TS::PropertyValueTypes elemType; long numElements; TSUTIL::param_bstr_t lowerBounds; TSUTIL::param_bstr_t upperBounds; array->GetDimensions("", 0, &lowerBounds, &upperBounds, &numElements, &elemType);
- IsOfType template —Determines whether a TestStand object implements a specific API class. For example, the following code determines whether the object the PropertyObject pointer objectPtr references is actually a Step object: TS::PropertyObjectPtr objectPtr; bool objectIsStep = (IsOfTypeFunctor<TS::Step>::ObjectIsOfType(*objectPtr));

Parent topic:

Programming with the TestStand API in Microsoft Visual C++

Related concepts:

- TestStand Directory Structure

<!--NI_TOPIC bundle=teststand path=utility-sequences-in-the-batch-process-model.html language=enus -->
## TOPIC 01011: Utility Sequences in the Batch Process Model

- bundle_id: `teststand`
- source_path: `utility-sequences-in-the-batch-process-model.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/utility-sequences-in-the-batch-process-model.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Batch process model sequences call the plug-in utility sequences and the following utility sequences: Restart TestSocket—The ProcessDialogRequests sequence calls the Restart TestSocket sequence to restart the execution for the test socket the request specifies. Initialize TestSocket—The controll

### Utility Sequences in the Batch Process Model

The Batch process model sequences call the plug-in utility sequences and the following utility sequences:

- Restart TestSocket —The ProcessDialogRequests sequence calls the Restart TestSocket sequence to restart the execution for the test socket the request specifies.
- Initialize TestSocket —The controlling execution calls the Initialize TestSocket sequence to initialize the data for and create the test socket executions.
- Tile Execution Windows —The controlling execution calls the Tile Execution Windows sequence to tile the test socket Execution windows by building a list of executions and posting a UIMessage to the user interface that requests window tiling. The Tile Execution Windows sequence tiles only running, non-disabled test socket executions.
- Add TestSocket Threads to Batch —The Test UUTs and Single
 Pass Execution entry points call the Add TestSocket Threads to Batch
 sequence from the controlling execution to add the main threads of the test
 socket executions to a Batch Synchronization object. The threads remove
 themselves from the batch in the Test UUTs - Test Socket
 Entry Point and the Single Pass - Test Socket
 Entry Point sequences after running the Main sequence of the client
 sequence file to clean up the state of the batch in case the sequence terminates
 or the client sequence file did not properly handle batch synchronization.
- ProcessDialogRequests —The controlling execution calls the
 ProcessDialogRequests sequence from the Test UUTs Execution entry point sequence
 after displaying the Batch UUT Information dialog box, which enqueues requests
 for sequence names into the ModelData.DialogRequestQueue 
 parameter. The ProcessDialogRequests sequence loops while waiting for those
 requests. When the ProcessDialogRequests sequence receives a request, it calls
 the requested sequence. Additionally, the ProcessDialogRequests sequence
 periodically calls the MonitorBatchThreads method of the
 ControllerAndSocketSynchronizationManager class to verify
 the state of and update the information for the test socket executions.
- Run Batch Info Dialog —The controlling execution calls the Run Batch Info
 Dialog sequence from a new thread in the Test UUTs Execution entry point to
 initialize and run the dialog box in which users enter serial numbers and view
 the results for a particular run of the batch.
- View TestSocket Report —The ProcessDialogRequests sequence calls this dialog box request callback to enable the View Report button in the UUT Information dialog box. Click the View Report button to launch a report viewer for the report file for the test socket the request specifies.
- View TestSocket Report – Current Only —The ProcessDialogRequests sequence calls this dialog box request callback to enable the View Report button in the UUT Information dialog box. Click the View Report button to launch a report viewer for the last report generated for the test socket the request specifies. This sequence differs from the View TestSocket Report sequence because it shows only the last report instead of the whole report file.
- View Batch Report —The ProcessDialogRequests sequence calls this dialog box request callback to enable the View Report button in the UUT Information dialog box. Click the View Report button to launch a report viewer for the batch report file.
- View Batch Report – Current Only —The ProcessDialogRequests sequence calls this dialog box request callback to enable the View Report button in the UUT Information dialog box. Click the View Report button to launch a report viewer for the last batch report generated. This sequence differs from the View Batch Report sequence in that it shows only the last report instead of the whole batch report file.

Parent topic:

Batch Process Model

Related concepts:

- Plug-in Utility Sequences
- Test UUTs Execution Entry Point in the Batch Process Model
- Single Pass Execution Entry Point in the Batch Process Model
- Test UUTs – Test Socket Entry Point Execution Entry Point in the Batch Process Model
- Single Pass - Test Socket Entry Point in the Batch Process Model
- Hidden Execution Entry Points in the Batch Process Model
- Main Execution Entry Points in the Batch Process Model
- Model Callbacks in the Batch Process Model

<!--NI_TOPIC bundle=teststand path=utility-sequences-in-the-parallel-process-mod.html language=enus -->
## TOPIC 01012: Utility Sequences in the Parallel Process Model

- bundle_id: `teststand`
- source_path: `utility-sequences-in-the-parallel-process-mod.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/utility-sequences-in-the-parallel-process-mod.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Parallel process model sequences call the plug-in utility sequences, and the main Execution entry points in the Parallel process model use the following additional utility sequences: Initialize TestSocket—The controlling execution calls the Initialize TestSocket sequence to initialize the data f

### Utility Sequences in the Parallel Process Model

The Parallel process model sequences call the plug-in utility sequences, and the main Execution entry points in the Parallel process model use the following additional utility sequences:

- Initialize TestSocket —The controlling execution calls the Initialize TestSocket sequence to initialize the data for and create the test socket executions.
- Tile Execution Windows —The controlling execution calls the Tile Execution Windows sequence to tile the test socket Execution windows by building a list of executions and posting a UIMessage to the user interface that requests window tiling.
- Monitor Threads —The ProcessDialogRequests sequence calls the Monitor Threads sequence periodically from the controlling execution to determine whether any of the test socket executions terminated or aborted. The Monitor Threads sequence updates the ModelData for terminated or aborted test sockets to indicate the new state and updates the UUT Information dialog box the controlling execution launches.
- ProcessDialogRequests —The controlling execution calls the
 ProcessDialogRequests sequence from the Test UUTs sequence
 after displaying the UUT Information dialog box, which enqueues requests for
 sequence names into the ModelData.DialogRequestQueue 
 parameter. The ProcessDialogRequests sequence loops while waiting for those
 requests. When the ProcessDialogRequests sequence receives a request, it calls
 the requested sequence. Additionally, the ProcessDialogRequests sequence
 periodically calls the Monitor Threads sequence to verify the state of and
 update the information for the test socket executions.
- Run UUT Info Dialog —The controlling execution calls the Run UUT Info
 Dialog sequence from a new thread in the Test UUTs Execution entry point to
 initialize and launches the UUT Information dialog box the Test UUTs Execution
 entry point uses to display information and gather serial numbers for the test
 socket executions.
- Continue TestSocket —The ProcessDialogRequests sequence calls the Continue TestSocket callback to notify the test socket to continue executing. The test socket execution waits on the notification in the default implementation of the PreUUT and PostUUT callbacks.
- Terminate TestSocket —The ProcessDialogRequests sequence calls this dialog box request callback. The Terminate TestSocket sequence terminates the execution for the test socket the request specifies.
- Abort TestSocket —The ProcessDialogRequests sequence calls this dialog box request callback. The Abort TestSocket sequence aborts the execution for the test socket the request specifies.
- Restart TestSocket —The ProcessDialogRequests sequence calls this dialog box request callback. The Restart TestSocket sequence restarts the execution for the test socket the request specifies and re-tiles the Execution windows to include the Execution window the Restart TestSocket sequence restarts.
- Terminate All TestSockets —The ProcessDialogRequests sequence calls this dialog box request callback. The Terminate All TestSockets sequence terminates all the test socket executions.
- Abort All TestSockets —The ProcessDialogRequests sequence calls this dialog box request callback. The Abort All TestSockets sequence aborts all the test socket executions.
- Stop All TestSockets —The ProcessDialogRequests sequence calls this dialog box request callback. The Stop All TestSockets sequence sets a flag for each test socket execution to stop after completing the current UUT test sequence. The sequence also sets a notification for test socket executions to continue to that point without interruption.
- View TestSocket Report —The ProcessDialogRequests sequence calls this dialog box request callback to enable the View Report button in the UUT Information dialog box. Click the View Report button to launch a report viewer for the report file for the test socket the request specifies.
- View TestSocket Report – Current Only —The ProcessDialogRequests sequence calls this dialog box request callback to enable the View Report button in the UUT Information dialog box. Click the View Report button to launch a report viewer for the last report generated for the test socket the request specifies. This sequence differs from the View TestSocket Report sequence in that it shows only the last report instead of the whole report file.

Parent topic:

Parallel Process Model

Related concepts:

- Plug-in Utility Sequences
- Test UUTs Execution Entry Point in the Parallel Process Model
- Model Callbacks in the Parallel Process Model

<!--NI_TOPIC bundle=teststand path=uut-result-table-schema.html language=enus -->
## TOPIC 01013: UUT_RESULT Table Schema

- bundle_id: `teststand`
- source_path: `uut-result-table-schema.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/uut-result-table-schema.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The default TestStand schema logs station, batch, UUT, and execution information to this table. 13 UUT_RESULT Table Schema Column Name Data Type Description ID Primary Key Unique value that identifies each entry in the table. For Access and SQL Server, the default process model assumes this column i

### UUT_RESULT Table Schema

The default TestStand schema logs station, batch, UUT, and execution information to this table.

| Column Name | Data Type | Description |
| --- | --- | --- |
| ID | Primary Key | Unique value that identifies each entry in the table. For Access and SQL Server, the default process model assumes this column increments automatically. For Oracle, the default process model uses an Oracle SQL sequence to generate a unique number. |
| STATION_ID | String | Station ID, usually the computer name. |
| BATCH_SERIAL_NUMBER | String | Serial number of the batch. This applies only to executions that use the Batch process model. |
| TEST_SOCKET_INDEX | Number | Test socket for the UUT. This applies only to executions that use the Parallel or Batch process models. |
| UUT_SERIAL_NUMBER | String | Serial number of the UUT. |
| USER_LOGIN_NAME | String | Login name of the user who tested the UUT. |
| START_DATE_TIME | Date-time | Time and date at which the UUT test began executing. |
| EXECUTION_TIME | Number | Number of seconds the UUT test took to execute. |
| UUT_STATUS | String | Status of the UUT test. |
| UUT_ERROR_CODE | Number | Error code when the UUT test status is Error. |
| UUT_ERROR_MESSAGE | String | Error message when the UUT test status is Error. |
| PART_NUMBER | String | Part number for the UUT. |
| TSR_FILE_NAME | String | Name of the offline results log file that created the UUT record. |
| TSR_FILE_ID | String | ID of the offline results log file that created the UUT record. |
| TSR_FILE_CLOSED | Boolean | Indicates whether the offline results file was closed properly. |

Parent topic:

Default TestStand Table Schemas

<!--NI_TOPIC bundle=teststand path=validate-and-verify-runtime-behavior-of-impor.html language=enus -->
## TOPIC 01014: Validate and Verify Runtime Behavior of Import

- bundle_id: `teststand`
- source_path: `validate-and-verify-runtime-behavior-of-impor.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/validate-and-verify-runtime-behavior-of-impor.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can run the analyzer to validate the settings configured by the user in property loader step and also to validate the property loader source. You can use Import Preview, which launches the Import Preview Dialog, displaying the state of the sequence file after importing. It also shows what proper

### Validate and Verify Runtime Behavior of Import

You can run the analyzer to validate the settings configured by the user in property loader step and also to validate the property loader source.

You can use Import Preview, which launches the Import Preview Dialog, displaying the state of the sequence file after importing. It also shows what properties are updated, along with the old and new values.

You can choose to log the lookup of the updated property and its old and new value in the property loader step. After executing the step, you can verify the updated properties and their values by looking at the logged results.

Parent topic:

Using the Property Loader Step Type

<!--NI_TOPIC bundle=teststand path=validating-deployments.html language=enus -->
## TOPIC 01015: Validating Deployments

- bundle_id: `teststand`
- source_path: `validating-deployments.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/validating-deployments.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Before you deploy a test system to production computers, complete the following steps. Test the deployment on the development computer you used to create the deployment. Test the deployable image. Test the installer or package distribution you build with the TestStand Deployment Utility. Validate th

### Validating Deployments

[IMAGE alt='image' src='GUID-6E36B858-E172-46C2-9EA7-A52114758DC8-a5.svg']

Before you deploy a test system to production computers, complete the following steps.

1. Test the deployment on the development computer you used to create the deployment.
2. Test the deployable image.
3. Test the installer or package distribution you build with the TestStand Deployment Utility.
4. Validate the test system and user interfaces on test station computers.

#### Testing on Development Computers

Development computers include the necessary tools to fix issues in the test system and rebuild the deployment, but you cannot use development computers to fully test whether the installer you build with the deployment utility installs all the required dependencies because the development computer already includes these files. For example, if the test system requires a DLL in the Windows\System directory or a .NET assembly in the Global Assembly Cache (GAC) and you do not include those components in the deployment, the test system most likely functions correctly on the development computer because the files already exist on the computer. However, when you deploy the test system to another computer that does not already include those files, the test system might not function correctly because the deployment did not include those files.

#### Testing Deployable Images

When you specify the files to include in the deployment on the System Source tab of the deployment utility, the deployment utility copies all the files and their statically referenced dependencies to a directory called the deployable image. The deployment utility creates the deployable image regardless of the deployment mechanism you use.

Use the following techniques to test the deployable image and resolve issues you discover before you create an installer with the deployment utility:

- Run the TestStand Sequence Analyzer on all the sequence files in the deployable image directory to confirm that the deployment includes all the necessary dependencies. This technique works only when the test system does not use absolute paths because the analyzer uses the source file from the absolute path instead of the copy of the file in the deployable image directory.
- Execute the test system from the deployable image directory. This technique works only when the development computer includes the hardware the test system requires and when the test system does not use absolute paths because the test system executes source files from the absolute paths and does not execute the copies of the files in the deployable image directory.You might execute a combination of source files and files from the deployable image directory if the deployment includes files from the <TestStand> , <TestStand Public> , or <TestStand Application Data> directories or if you are using search directories. To ensure that TestStand loads the correct file, copy the files from the deployable image directory to the <TestStand> , <TestStand Public> , <TestStand Application Data> , or to the correct search directory on the development computer.You also might need to back up the deployable image directory or perform TestStand configuration changes before you execute the test system to avoid modifying or adding files to the deployable image directory during testing. For example, executing a test system might create or modify files in the deployable image directory or log test results to manufacturing databases.

#### Testing Distributions You Build with the Deployment Utility

Do not test an installer you build with the deployment utility on the development computer for the following reasons:

- If the installer you build with the deployment utility installs files to the same locations as the source files on the development computer, the installer overwrites those original files, which might cause you to lose work. The installer provides no warning that it overwrites the source files.
- If the installer you build with the deployment utility contains a driver with an install type other than Full , installing the driver might remove features of the driver from the development computer.
- Testing a deployment installer on the development computer does not detect missing dependent files, components, or drivers because the development computer already includes these files.

To effectively test the installer or package you build with the deployment utility, install the deployment on a separate computer that has only the operating system installed. If you are testing a single package or repository distribution type, you will need to install NI Package Manager on the test machine before installing the package.

#### Testing on Test Stations

Using a test station computer to test the deployment can help you identify additional required components or dependencies. When practical, test deployments on all supported operating systems on an extra, inactive test station computer that is identical to production test station computers to prevent disrupting the manufacturing process. If you do not have an extra test station computer, configure a virtual machine with the supported operating systems to test the deployment for missing code modules or required drivers. If the test system uses a hardware abstraction layer, run validation tests on the virtual machine using a software simulation of the hardware to identify issues with the deployment.

You can also run the TestStand Sequence Analyzer on the test station computer to identify issues to correct.

#### Validation Testing

Write validation tests for basic functionality of the test system to verify that the test system performs as designed. Validation tests use known inputs for the test system and verify that the test system returns the correct results. For example, you can test a functioning UUT and a UUT with known defects to confirm that the test system reports the outcome of testing the UUTs correctly. Many test systems use simulated measurements for testing to manage the difficulty of maintaining a large inventory of UUTs for validation.

#### User Interface Testing

Test the functionality of user interfaces as you develop them and validate that the test station computers include the dependencies the user interfaces require, such as files the user interface loads or references dynamically. Testing user interfaces on test station computers can also help you identify differences between development computers and test station computers, such as screen resolution issues.

Previous:Transferring Files

Parent topic:

Deployment Process Overview

Related concepts:

- Choosing a Deployment Mechanism
- TestStand Directory Structure
- Identifying Components to Deploy
- Transferring Files

<!--NI_TOPIC bundle=teststand path=variables.html language=enus -->
## TOPIC 01016: Variables

- bundle_id: `teststand`
- source_path: `variables.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/variables.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Variables are properties you can freely create in certain contexts. Variables can apply globally to a sequence file or locally to a particular sequence. You can also use station global variables with values that persist across different executions and across different invocations of the sequence edi

### Variables

Variables are properties you can freely create in certain contexts. Variables can apply globally to a sequence file or locally to a particular sequence. You can also use station global variables with values that persist across different executions and across different invocations of the sequence editor or user interfaces. The TestStand Engine maintains the value of station global variables in the StationGlobals.ini file in the <TestStand Application Data>\Cfg directory.

You can use TestStand variables to share data among tests written in different programming languages, even if the data representations are incompatible. You can pass values you store in variables and properties to code modules. You can also use the TestStand API to access variable and property values directly from code modules. Each step in a sequence can include properties. The type of step determines its set of properties.

When executing sequences, TestStand maintains a SequenceContext object that contains references to all global variables, all local variables, and all step properties in active sequences. The contents of the SequenceContext object vary according to the currently executing sequence and step. When you pass a SequenceContext object reference to a code module, you can use the code module to access information stored within the SequenceContext object.

Parent topic:

TestStand Building Blocks

Related concepts:

- Station Global Variables
- TestStand ActiveX API Overview
- Step Types
- Sequence Local Variables

<!--NI_TOPIC bundle=teststand path=version-independent-run-time-engine-support.html language=enus -->
## TOPIC 01017: Version Independent Run-Time Engine Support

- bundle_id: `teststand`
- source_path: `version-independent-run-time-engine-support.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/version-independent-run-time-engine-support.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Version Independent Runtime Engine support was introduced in LabVIEW 2017 and allows the LabVIEW runtime to load source files, such as VIs and projects, and build outputs, such as packed project libraries (PPLs), DLLs, and executables that were saved or built in an older version of LabVIEW. For exam

### Version Independent Run-Time Engine Support

Version Independent Runtime Engine support was introduced in LabVIEW 2017 and allows the LabVIEW runtime to load source files, such as VIs and projects, and build outputs, such as packed project libraries (PPLs), DLLs, and executables that were saved or built in an older version of LabVIEW.

For example, a PPL built in LabVIEW 2017 can now be loaded and executed by the LabVIEW 2018 runtime.

TestStand 2016 SP1 supports this feature in the LabVIEW Adapter. Enabling this feature in TestStand reduces the number of LabVIEW runtime engines that would have to be loaded into the TestStand process to execute LabVIEW code modules.

PPL build specifications in LabVIEW also have an option to specify whether the build output subscribes to this feature. LabVIEW enables these options by default for PPL build specifications you create in LabVIEW 2017 and later.

Disabling the option binds a PPL build specification to a specific version of LabVIEW, prevents any changes to the performance profiles, and helps you avoid unexpected problems resulting from compiler upgrades.

For more information about this feature in LabVIEW, refer to the LabVIEW Help.

Enable Version Independent Runtime Engine

Note

When you enable this adapter option, Version Independent Runtime Engine support is enabled for all instances of LabVIEW runtimes, version 2017 or later, that are used by the TestStand application. TestStand can load and execute LabVIEW files saved in LabVIEW 2017 or later in a later version of the LabVIEW runtime.

For example, if a TestStand sequence calls LabVIEW code modules saved in LabVIEW 2017 and Version Independent Runtime Engine support is enabled, then these LabVIEW files will be loaded and executed in the LabVIEW 2018 Runtime Engine.

When Version Independent Runtime Engine support is disabled, the version of the VI called in TestStand, and all its dependencies, must match the version of the runtime being used to load or run the VI.

Note

- The LabVIEW 2017 runtime does not allow the loading of VIs, PPLs, or DLLs saved in LabVIEW 2016 or earlier, even if Version Independent Runtime Engine support is enabled. The support for this feature in TestStand applies only to LabVIEW 2018 and later runtimes when loading LabVIEW files saved in LabVIEW 2017 or later.
- The Version Independent Runtime feature is enabled in LabVIEW Development System, version 2017 and later, by default. TestStand 2019 and later versions will not modify this setting on the active LabVIEW Development System.

#### Errors on Loading a VI with Version Independent Runtime Engine Support Enabled

If a VI is reported as broken in TestStand when Version Independent Runtime Engine support is enabled, complete the following steps to resolve the issue:

1. Open the VI in the LabVIEW development system. If the VI is broken, fix any errors in the VI and save it.
2. Ensure that neither the VI nor any of its dependencies are saved in LabVIEW 2016 or earlier.
3. If the VI is not broken in the LabVIEW development system when Version Independent Runtime Engine support is disabled, the issue may be that the VI has dependencies in LabVIEW folders such as vi.lib, user.lib , or instr.lib . To resolve this issue, NI recommends that you create a deployment of your sequence files and VIs and execute the sequence files from the deployed image. Use the TestStand Deployment Utility to create a deployment of your sequence file(s) and LabVIEW VIs.

Parent topic:

LabVIEW Adapter

Related concepts:

- TestStand Deployment Utility

Related information:

- LabVIEW Adapter Configuration Dialog Box

<!--NI_TOPIC bundle=teststand path=versioning-translators-and-custom-sequence-fi.html language=enus -->
## TOPIC 01018: Versioning Translators and Custom Sequence Files

- bundle_id: `teststand`
- source_path: `versioning-translators-and-custom-sequence-fi.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/versioning-translators-and-custom-sequence-fi.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: When you edit a custom sequence file format, you can increment the following information: Version number of the file format—Identifies the structure and syntax of the file. File version number—Identifies the revision of the contents of the file. When the contents of a custom sequence file includes a

### Versioning Translators and Custom Sequence Files

When you edit a custom sequence file format, you can increment the following information:

- Version number of the file format —Identifies the structure and syntax of the file.
- File version number —Identifies the revision of the contents of the file.

When the contents of a custom sequence file includes a file format version number, a translator can read files with the current file format and files with an earlier file format, and the translator can identify newer file formats it does not support. When a translator callback accesses the contents of the file, the translator ensures that it can support the file format version. For example, the CanTranslate callback uses the version number to determine whether the translator can load the file. In addition, TestStand displays the return value from the GetFileFormatVersion callback in reports the Workspace Documentation tool creates.

When the contents of a custom sequence file includes a file version number or revision, implement the translator to assign the version to the PropertyObjectFile.Version property in the TranslateToSequenceFile callback and return the version in the GetFileVersion callback to ensure that the Sequence File Properties dialog box displays the file version number and the Sequence File Documentation and Workspace Documentation tools display the file version number in reports you create.

When the file formats between version numbers differ significantly, consider creating two translators in a single DLL or a separate translator in two DLLs to simplify the code necessary to translate each file format. When files contain header fields that identify the file format and the CanTranslate callback uses these fields, ensure that using two translators does not affect the performance of opening files in TestStand.

Parent topic:

Sequence File Translators

<!--NI_TOPIC bundle=teststand path=vi-calling-net-ts.html language=enus -->
## TOPIC 01019: Calling LabVIEW VIs That Invoke .NET Code in TestStand

- bundle_id: `teststand`
- source_path: `vi-calling-net-ts.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/vi-calling-net-ts.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: TestStand applications like the TestStand Sequence Editor and TestStand C# User Interfaces are .NET Core processes in TestStand 2025 Q2 and later. Consider the following to ensure functionality when using TestStand to call LabVIEW VIs that invoke .NET code and vice versa: TestStand is a .NET Core pr

### Calling LabVIEW VIs That Invoke .NET Code in
 TestStand

TestStand applications like the TestStand Sequence Editor and TestStand C# User
 Interfaces are .NET Core processes in TestStand 2025 Q2 and later.

- TestStand is a .NET Core process, and does not support calling LabVIEW VIs that
 invoke .NET Framework assemblies in the LabVIEW Runtime Engine. VIs which invoke
 .NET Framework assemblies can still run if you execute them in the LabVIEW ADE
 from TestStand.
- TestStand supports calling LabVIEW VIs that invoke .NET Core assemblies in both
 the LabVIEW Runtime Engine and the LabVIEW ADE.
- Loading TestStand UI controls in LabVIEW may cause issues, as the TestStand
 engine loads the .NET Core runtime by default and LabVIEW uses a .NET Framework
 runtime. You can prevent these issues by preventing LabVIEW from loading the
 .NET Framework: Note Disabling the .NET Framework is only supported
 in LabVIEW 2025 and later.
  - If you are developing a TestStand user interface in LabVIEW: Note You must restart LabVIEW for changes to
 the LabVIEW.ini configuration file to take
 effect.
    1. Open your LabVIEW configuration file at
 <LabVIEW>\LabVIEW.ini and add the
 key value pair
 DisableDotNetFrameworkSupport=True under
 the [LabVIEW] section. This prevents the
 LabVIEW ADE from loading the .NET Framework runtime into the
 process, disables any features that use .NET framework for that
 session, and allows LabVIEW to load the .NET Core runtime.
    2. Prevent the LabVIEW runtime engine from executing VIs which call
 into .NET framework assemblies by adding a new section in
 LabVIEW.ini named
 [LVRT] and adding the key value pair
 DisableDotNetFrameworkSupport=True below
 it.
    3. Enable LabVIEW to load the .NET Core frameworks needed by
 TestStand by copying the contents of
 <TestStand>\AdapterSupport\DotNetSupport\DotnetCore.runtimeconfig.json 
 and replacing the contents of
 <LabVIEW>\LabVIEW.runtimeconfig.json 
 with the copied data.
  - If you are executing a TestStand user interface built using LabVIEW or
 another supported language: Note TestStand user interface examples
 possess the necessary configuration file changes to load correctly
 in LabVIEW.
    1. Open the configuration file present next to your executable. For
 example, in the LabVIEW User Interface shipping example, this
 would be TestExec.ini which is present next
 to
 <TestStand>\UserInterfaces\Full-Featured\LabVIEW\Source
 Code\TestExec.exe or <TestStand
 Public>\UserInterfaces\Full-Featured\LabVIEW\Source
 Code\TestExec.exe .
    2. Prevent the LabVIEW runtime engine loaded by TestStand from
 loading .NET Framework by adding a new section in your
 .ini file named [LVRT] 
 and adding the key value pair
 DisableDotNetFrameworkSupport=True below
 it.
    3. Add the key value pairs
 DisableDotNetFrameworkSupport=True and
 DotNetCoreRuntimeConfigPath=<TestStand>\AdapterSupport\DotNetSupport\DotnetCore.runtimeconfig.json 
 under the section with the same name as your executable to allow
 LabVIEW to load the .NET Core runtime and the necessary .NET
 Core frameworks.

Parent topic:

LabVIEW Adapter

Related reference:

- Migrating User Interfaces to .NET Core

<!--NI_TOPIC bundle=teststand path=view-connections.html language=enus -->
## TOPIC 01020: View Connections

- bundle_id: `teststand`
- source_path: `view-connections.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/view-connections.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can connect manager controls to specific TestStand User Interface (UI) Controls to display the steps in a sequence file or an execution, the report for an execution, the sequence context for a sequence file or execution, and the set of step types and templates users can insert into sequence file

### View Connections

You can connect manager controls to specific TestStand User Interface (UI) Controls to display the steps in a sequence file or an execution, the report for an execution, the sequence context for a sequence file or execution, and the set of step types and templates users can insert into sequence files.

Connect a SequenceFileView Manager control or an ExecutionView Manager control to a SequenceView control to display the steps of a sequence from a sequence file or execution. You can also connect an ExecutionView Manager control to a ReportView control to display the report for the execution.

Connect a SequenceFileView Manager control or an ExecutionView Manager control to a VariablesView control to display the sequence context for the sequence file or execution.

Connect a SequenceFileView Manager control to an InsertionPalette control so users can insert steps and template items into a sequence file by dragging or double-clicking.

Call the following methods to connect to view controls:

- SequenceFileViewMgr.ConnectSequenceView
- SequenceFileViewMgr.ConnectVariables
- SequenceFileViewMgr.ConnectInsertionPalette
- ExecutionViewMgr.ConnectExecutionView
- ExecutionViewMgr.ConnectReportView
- ExecutionViewMgr.ConnectVariables

Parent topic:

Connecting Manager Controls to Visible Controls

Related concepts:

- Manager Controls
- TestStand UI Controls
- SequenceFileView Manager
- ExecutionView Manager
- Sequence Context
- Visible Controls

<!--NI_TOPIC bundle=teststand path=viewing-examples-tsa.html language=enus -->
## TOPIC 01021: Viewing Examples in the Sequence Analyzer

- bundle_id: `teststand`
- source_path: `viewing-examples-tsa.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/viewing-examples-tsa.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `task`
- source_description: Complete the following steps to show the example rules and analysis modules that use LabVIEW, LabWindows/CVI, Microsoft Visual C#, and Microsoft Visual C++ modules in the TestStand Sequence Analyzer. Launch the Configure Sequence Analyzer Available Rules dialog box. Click the Import button to launch

### Viewing Examples in the Sequence
 Analyzer

Complete the following steps to show the
 example rules and analysis modules that use LabVIEW, LabWindows/CVI, Microsoft Visual
 C#, and Microsoft Visual C++ modules in the TestStand Sequence Analyzer.

1. Launch the Configure Sequence Analyzer Available Rules
 dialog box.
2. Click the Import button to launch the Import
 Items from File dialog box.
3. Click the Browse button and browse to
 <TestStand Public>\Examples\TestStand
 Debugging Features\Custom Analyzer Rules -
 <RuleName>\<Environment> directory and select the
 example rules file (.tsarules) you want to import in the
 Select File to Import From control, where
 <RuleName> is the rule name and <Environment> is one of the
 following: LabVIEW, CVI,
 CSharp, or VC.
4. Enable all example rules and analysis modules in the Select Items to
 Import list.
5. Click the Import button to add the example rules and
 analysis modules to all new and existing sequence analyzer projects on the
 computer.
6. Click Close in the Import Items from File dialog box to
 return to the Configure Sequence Analyzer Available Rules dialog box.

The sequence analyzer adds the example rules and analysis modules to the
 CustomRules.tsarules section on the Rules tab and on the
 Analysis Modules tab of the Configure Sequence Analyzer Available Rules dialog box
 and adds an Example category to the Rules pane of the Current Sequence Analyzer
 Project window or the Rules tab of the stand-alone sequence analyzer
 application.

<TestStand Public>\Examples\AnalyzerCustomRules

Note

<TestStand>\Components\Analyzer\NIAnalysisModules

Parent topic:

TestStand Sequence Analyzer

Related concepts:

- Search Directories

Related tasks:

- Creating Custom Rules in the TestStand Sequence Analyzer

Related information:

- TestStand Sequence Analyzer Environment Reference
- Configure Sequence Analyzer Available Rules Dialog Box
- Current Sequence Analyzer Project Window
- Import Items from File Dialog Box

<!--NI_TOPIC bundle=teststand path=viewing-xml-help-for-net-code-modules.html language=enus -->
## TOPIC 01022: Viewing XML Help for .NET Code Modules

- bundle_id: `teststand`
- source_path: `viewing-xml-help-for-net-code-modules.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/viewing-xml-help-for-net-code-modules.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: If you export XML Documentation files when building .NET code modules and you want TestStand to display help information for a code module in the Sequence Editor, place the XML Documentation file next to the .NET code module loaded by TestStand. If the XML Documentation file is not in the same folde

### Viewing XML Help for .NET Code Modules

Note

Parent topic:

.NET Adapter

Related concepts:

- .NET Adapter

<!--NI_TOPIC bundle=teststand path=visible-controls.html language=enus -->
## TOPIC 01023: Visible Controls

- bundle_id: `teststand`
- source_path: `visible-controls.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/visible-controls.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The TestStand User Interface (UI) Controls in the following table are visible at design time and run time and are similar to common Microsoft Windows UI controls. Connect visible TestStand UI Controls to manager controls to display information or to allow users to select items to view. Control Name

### Visible Controls

The TestStand User Interface (UI) Controls in the following table are visible at design time and run time and are similar to common Microsoft Windows UI controls. Connect visible TestStand UI Controls to manager controls to display information or to allow users to select items to view.

| Control Name | Description |
| --- | --- |
| Button | Connect a manager control to a Button control to specify that the button performs a common user interface command, such as "Open Sequence File." The Button control uses a localized caption and automatically enables or disables according to the application state. |
| CheckBox | Connect a manager control to a CheckBox control so users can toggle the state of a common user interface command, such as "Break on Step Failure." |
| ComboBox | Connect a manager control to a ComboBox control so users can view or select from a list of adapters, sequence files, sequences, step groups, executions, threads, or stack frames. |
| ExpressionEdit | Use an ExpressionEdit control so users can edit a TestStand expression with syntax coloring, popup help, and statement completion. Although you typically do not need to edit expressions in a user interface application, you can connect a manager control to a read-only ExpressionEdit control to display text information about the application state, such as the pathname of the selected sequence file or the name of the current user. You can also use ExpressionEdit controls in dialog boxes for step types and in tools in which you prompt users to enter a TestStand expression. |
| InsertionPalette | Connect a SequenceFileView Manager control to an InsertionPalette control so users can insert steps and template items into a sequence file by dragging or double-clicking. |
| Label | Connect a manager control to a Label control to display text information about the application state in the label, such as the name of the current user or the status of the current unit under test (UUT). |
| ListBar | Use a ListBar control to display multiple pages, where each page contains a list of items users can view or select. Connect a manager control to a ListBar page so users can view and select from a list of adapters, sequence files, sequences, step groups, executions, threads, or stack frames. |
| ListBox | Connect a manager control to a ListBox control so users can view or select from a list of adapters, sequence files, sequences, step groups, executions, threads, or stack frames. |
| ReportView | Connect an ExecutionView Manager control to a ReportView control to display the report for the selected execution. |
| SequenceView | Connect a SequenceFileView Manager control or an ExecutionView Manager control to a SequenceView control to display the steps of a sequence from a sequence file or execution. The SequenceView control displays the steps in a list with columns you specify when you configure the control. |
| StatusBar | Connect a manager control to panes of a StatusBar control to display textual, image, or progress information about the application state. You can programmatically control individual StatusBar panes to display custom information. |
| VariablesView | Connect a SequenceFileView Manager control or an ExecutionView Manager control to a VariablesView control to display the sequence context for the sequence file or execution. |

Parent topic:

Getting Started with User Interface Development

Related concepts:

- TestStand UI Controls
- Manager Controls
- SequenceFileView Manager
- ExecutionView Manager

<!--NI_TOPIC bundle=teststand path=vxiplug-play-base-interface.html language=enus -->
## TOPIC 01024: VXIplug&play Base Interface

- bundle_id: `teststand`
- source_path: `vxiplug-play-base-interface.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/vxiplug-play-base-interface.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use VXIplug&play and IVI instrument sessions to obtain an ActiveX reference to a VXIplug&play base interface. You can use this interface to call the following required VXIplug&play non-initialization methods without calling particular driver APIs: VPPBase.Error_Query VPPBase.Error_Message VP

### VXIplug&play Base Interface

You can use VXIplug&play and IVI instrument sessions to obtain an ActiveX reference to a VXIplug&play base interface. You can use this interface to call the following required VXIplug&play non-initialization methods without calling particular driver APIs:

- VPPBase.Error_Query
- VPPBase.Error_Message
- VPPBase.Revision_Query
- VPPBase.Self_Test
- VPPBase.Reset

For example, you can use the VXIplug&play base interface to create a
 utility that resets or self-tests all instruments in the system.

Parent topic:

Session Manager

Related information:

- VPPBase API Reference

<!--NI_TOPIC bundle=teststand path=what-software-do-i-install-to-use-instrument.html language=enus -->
## TOPIC 01025: What Software Do I Install to Use Instrument Sessions?

- bundle_id: `teststand`
- source_path: `what-software-do-i-install-to-use-instrument.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/what-software-do-i-install-to-use-instrument.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: You must install the Session Manager ActiveX server to use instrument sessions. The Session Manager ActiveX server requires NI-VISA but does not require LabVIEW, TestStand, LabWindows/CVI, the LabWindows/CVI Run-Time Engine, or IVI. As an ActiveX server, Session Manager runs only on Microsoft Window

### What Software Do I Install to Use Instrument Sessions?

You must install the Session Manager ActiveX server to use instrument sessions. The Session Manager ActiveX server requires NI-VISA but does not require LabVIEW, TestStand, LabWindows/CVI, the LabWindows/CVI Run-Time Engine, or IVI. As an ActiveX server, Session Manager runs only on Microsoft Windows platforms.

Parent topic:

Session Manager

<!--NI_TOPIC bundle=teststand path=why-use-instrument-sessions.html language=enus -->
## TOPIC 01026: Why Use Instrument Sessions?

- bundle_id: `teststand`
- source_path: `why-use-instrument-sessions.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/why-use-instrument-sessions.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Instrument sessions are useful when you must share instrument API handles within a single process among loosely coupled software components. A test management system is an example of a system that can benefit from instrument sessions. Using named instrument sessions can include the following advanta

### Why Use Instrument Sessions?

Instrument sessions are useful when you must share instrument API handles within a single process among loosely coupled software components. A test management system is an example of a system that can benefit from instrument sessions.

Using named instrument sessions can include the following advantages:

- Reduced Coupling —You do not have to pass instrument handle variables among software components. Instead, each component specifies a logical instrument name to obtain a session. Components then acquire the API handle from the session. Because you specify a logical instrument name to access a session, components that are not explicitly connected to each other can access the same session and thereby share an API handle. Because the session initializes and closes the API handle as needed, components that use the session do not need to be aware of the relative order in which they execute.
- Reduced Programming Language Barriers —Code modules written in different languages can share the same session without passing handles that might not easily convert among languages.
- Lifetime Control —Because instrument sessions are ActiveX objects with reference counts, you can tie the lifetime of the session to the lifetime of an ActiveX reference variable and eliminate the need to explicitly close the instrument in languages that support ActiveX reference variables. Multiple variables can reference the same session. The session closes when its last reference releases. Because a session lives as long as a reference to it exists, you do not have to coordinate the lifetime of the session among multiple threads or processes that use it.
- Efficiency and Correctness —A session initializes the API handle only when necessary. For example, if a component uses a logical instrument name and calls a subcomponent that uses the same logical name, the subcomponent can share the session that its caller initializes. Sharing the session avoids the overhead of initializing a second API handle. By sharing a session, you also avoid the possibility of using a second API handle with the same instrument resource, which might invalidate the internal state of the first API handle.
- Virtual Instrument Selection —You can query Session Manager to obtain a list of logical and/or virtual instrument names from which to make a selection. You can also narrow the query to a subset of the available session names. For example, you might make one of the following queries:
  - All virtual instrument and/or logical names for sessions that provide an instrument API handle to an IVI Switch class driver.
  - All virtual instrument and/or logical names for sessions that provide an instrument API handle for a specific VXI plug&play driver.

Note

plug&play

Parent topic:

Session Manager

<!--NI_TOPIC bundle=teststand path=windows-10-8-1-7-firewall-settings-local.html language=enus -->
## TOPIC 01027: Windows 10/8.1/7 Firewall Settings - Windows Firewall Settings for the Local Computer - Setting Up TestStand for Accessing Synchronization Objects Remotely

- bundle_id: `teststand`
- source_path: `windows-10-8-1-7-firewall-settings-local.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/windows-10-8-1-7-firewall-settings-local.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Complete the following steps to configure the Microsoft Windows firewall on the local computer. Log in as a user with administrator privileges. Navigate to the standard Windows Control Panel facility for Windows firewall and click Allow an app or a program or feature through Windows Firewall on the

### Windows 10/8.1/7 Firewall Settings - Windows Firewall Settings for the Local Computer - Setting Up TestStand for Accessing Synchronization Objects Remotely

Complete the following steps to configure the Microsoft Windows firewall on the local computer.

1. Log in as a user with administrator privileges.
2. Navigate to the standard Windows Control Panel facility for Windows firewall and click Allow an app or a program or feature through Windows Firewall on the left panel of the Windows Firewall window to launch the Allowed Apps or Programs window.
3. Complete the following steps to add exceptions for the REngine.exe application with the firewall enabled.
  1. Click the Allow another app or program button to launch the Add an App or Program dialog box.
  2. Click Browse and select the client application, such as <TestStand>\Bin\SeqEdit.exe .
  3. Click Add to close the Add ann App or Program dialog box.
  4. Click OK to close the Allowed Apps or Programs window.
4. Click Advanced settings on the left panel of the Windows Firewall window to launch the Windows Firewall with Advanced Security window.
5. Complete the following steps to specify a security exception for Distributed Connection Object Model (DCOM).
  1. Click Inbound Rules on the left panel of the Windows Firewall with Advanced Security window to display the list of inbound rules.
  2. Click New Rule on the Actions pane to launch the New Inbound Rule Wizard.
  3. Select Port and click the Next button.
  4. Select TCP , select Specific local ports , enter 135 in the Specific local ports control, and click Next .
  5. Select Allow the connection and click Next .
  6. Ensure that the Domain, Private, and Public options have checkmarks and click Next .
  7. In the Name control, enter DCOM and click Finish to close the New Inbound Rule Wizard.

Parent topic:

Windows Firewall Settings for the Local Computer - Setting Up TestStand for Accessing Synchronization Objects Remotely

Related concepts:

- Search Directories

<!--NI_TOPIC bundle=teststand path=windows-10-8-1-7-firewall-settings-remote.html language=enus -->
## TOPIC 01028: Windows 10/8.1/7 Firewall Settings - Windows Firewall Settings for the Remote Computer - Setting Up TestStand for Accessing Synchronization Objects Remotely

- bundle_id: `teststand`
- source_path: `windows-10-8-1-7-firewall-settings-remote.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/windows-10-8-1-7-firewall-settings-remote.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Complete the following steps to configure the Microsoft Windows firewall on the computer that creates the synchronization object. Log in as a user with administrator privileges. Navigate to the standard Windows Control Panel facility for Windows firewall and click Allow an app or a program or featur

### Windows 10/8.1/7 Firewall Settings - Windows Firewall Settings for the Remote Computer - Setting Up TestStand for Accessing Synchronization Objects Remotely

Complete the following steps to configure the Microsoft Windows firewall on the computer that creates the synchronization object.

1. Log in as a user with administrator privileges.
2. Navigate to the standard Windows Control Panel facility for Windows firewall and click Allow an app or a program or feature through Windows Firewall on the left panel of the Windows Firewall window to launch the Allowed Apps or Programs window.
3. Complete the following steps to add exceptions for the REngine.exe application with the firewall enabled.
  1. Click the Allow another app or program button to launch the Add an App or Program dialog box.
  2. Click Browse and select the client application, such as <TestStand>\Bin\SeqEdit.exe .
  3. Click Add to close the Add an App or Program dialog box.
  4. Click OK to close the Allowed Apps or Programs window.
4. Click Advanced settings on the left panel of the Windows Firewall window to launch the Windows Firewall with Advanced Security window.
5. Complete the following steps to specify a security exception for Distributed Component Object Model (DCOM).
  1. Click Inbound Rules on the left panel of the Windows Firewall with Advanced Security window to display the list of inbound rules.
  2. Click New Rule on the Actions pane to launch the New Inbound Rule Wizard.
  3. Select Port and click the Next button.
  4. Select TCP , select Specific local ports , enter 135 in the Specific local ports control, and click Next .
  5. Select Allow the connection and click Next .
  6. Ensure that the Domain, Private, and Public options have checkmarks and click Next .
  7. In the Name control, enter DCOM and click Finish to close the New Inbound Rule Wizard.

Parent topic:

Windows Firewall Settings for the Remote Computer - Setting Up TestStand for Accessing Synchronization Objects Remotely

Related concepts:

- Search Directories

<!--NI_TOPIC bundle=teststand path=windows-firewall-settings-for-remote-servers.html language=enus -->
## TOPIC 01029: Windows Firewall Settings for Remote Servers

- bundle_id: `teststand`
- source_path: `windows-firewall-settings-for-remote-servers.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/windows-firewall-settings-for-remote-servers.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the following information to configure the Windows firewall on the server computer to allow the TestStand client to access the REngine.exe application. Complete the following steps to configure the Windows firewall on the server computer. Log in as a user with administrator privileges. Navigate

### Windows Firewall Settings for Remote Servers

Use the following information to configure the Windows firewall on the server computer to allow the TestStand client to access the REngine.exe application.

Complete the following steps to configure the Windows firewall on the server computer.

1. Log in as a user with administrator privileges.
2. Navigate to the standard Windows Control Panel facility for Windows firewall and click Allow an app or a program or feature through Windows Firewall on the left panel of the Windows Firewall window to launch the Allowed Apps or Programs window.
3. Complete the following steps to add exceptions for the REngine.exe application with the firewall enabled.
  1. Click the Allow another app or program button to launch the Add an App or Program dialog box.
  2. Click Browse and select <TestStand>\Bin\REngine.exe .
  3. Click Add to close the Add an App or Program dialog box.
  4. Click OK to close the Allowed Apps or Programs window.
4. Click Advanced settings on the left panel of the Windows Firewall window to launch the Windows Firewall with Advanced Security window.
5. Complete the following steps to specify a security exception for DCOM.
  1. Click Inbound Rules on the left panel of the Windows Firewall with Advanced Security window to display the list of inbound rules.
  2. Click New Rule on the Actions pane to launch the New Inbound Rule Wizard.
  3. Select Port and click the Next button.
  4. Select TCP , select Specific local ports , enter 135 in the Specific local ports control, and click Next .
  5. Select Allow the connection and click Next.
  6. Ensure that the Domain , Private , and Public options are enabled and click Next .
  7. In the Name control, enter DCOM and click Finish to close the New Inbound Rule Wizard.

Parent topic:

Setting Windows System Security on a Remote Server

Related concepts:

- Setting Windows System Security on a Remote Server

<!--NI_TOPIC bundle=teststand path=windows-firewall-settings-for-the-local-clien.html language=enus -->
## TOPIC 01030: Windows Firewall Settings for the Local Client

- bundle_id: `teststand`
- source_path: `windows-firewall-settings-for-the-local-clien.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/windows-firewall-settings-for-the-local-clien.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the following information to configure the Windows firewall on the client computer to allow the REngine.exe application to access the TestStand client. Complete the following steps to configure the Windows firewall on the client computer. Log in as a user with administrator privileges. Navigate

### Windows Firewall Settings for the Local Client

Use the following information to configure the Windows firewall on the client computer to allow the REngine.exe application to access the TestStand client.

Complete the following steps to configure the Windows firewall on the client computer.

1. Log in as a user with administrator privileges.
2. Navigate to the standard Windows Control Panel facility for Windows firewall and click Allow an app or a program or feature through Windows Firewall on the left panel of the Windows Firewall window to launch the Allowed Apps or Programs window.
3. Complete the following steps to add exceptions for the client application with the firewall enabled.
  1. Click the Allow another app or program button to launch the Add an App or Program dialog box.
  2. Click Browse and select the client application, such as <TestStand>\Bin\SeqEdit.exe .
  3. Click Add to close the Add an App or Program dialog box.
  4. Click OK to close the Allowed Apps or Programs window.
4. Click Advanced settings on the left panel of the Windows Firewall window to launch the Windows Firewall with Advanced Security window.
5. Complete the following steps to specify a security exception for DCOM.
  1. Click Inbound Rules on the left panel of the Windows Firewall with Advanced Security window to display the list of inbound rules.
  2. Click New Rule on the Actions pane to launch the New Inbound Rule Wizard.
  3. Select Port and click the Next button.
  4. Select TCP , select Specific local ports , enter 135 in the Specific local ports control, and click Next .
  5. Select Allow the connection and click Next .
  6. Ensure that the Domain , Private , and Public options are enabled and click Next .
  7. In the Name control, type DCOM and click Finish to close the New Inbound Rule Wizard.

Parent topic:

Settings Windows System Security on a Local Client

Related concepts:

- Settings Windows System Security on a Local Client

<!--NI_TOPIC bundle=teststand path=windows-firewall-settings-for-the-local-compu.html language=enus -->
## TOPIC 01031: Windows Firewall Settings for the Local Computer - Setting Up TestStand for Accessing Synchronization Objects Remotely

- bundle_id: `teststand`
- source_path: `windows-firewall-settings-for-the-local-compu.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/windows-firewall-settings-for-the-local-compu.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the following information to configure the Microsoft Windows firewall on the local computer to allow the TSAutoMgr.exe application to access the TestStand client. Windows 10/8.1/7 Firewall Settings

### Windows Firewall Settings for the Local Computer - Setting Up TestStand for Accessing Synchronization Objects Remotely

Use the following information to configure the Microsoft Windows firewall on the local computer to allow the TSAutoMgr.exe application to access the TestStand client.

- Windows 10/8.1/7 Firewall Settings

Parent topic:

Setting Up TestStand for Accessing Synchronization Objects Remotely

<!--NI_TOPIC bundle=teststand path=windows-firewall-settings-for-the-remote-comp.html language=enus -->
## TOPIC 01032: Windows Firewall Settings for the Remote Computer - Setting Up TestStand for Accessing Synchronization Objects Remotely

- bundle_id: `teststand`
- source_path: `windows-firewall-settings-for-the-remote-comp.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/windows-firewall-settings-for-the-remote-comp.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the following information to configure the Microsoft Windows firewall on the computer that creates the synchronization object to allow TestStand to access the TSAutoMgr.exe application. Windows 10/8.1/7 Firewall Settings

### Windows Firewall Settings for the Remote Computer - Setting Up TestStand for Accessing Synchronization Objects Remotely

Use the following information to configure the Microsoft Windows firewall on the computer that creates the synchronization object to allow TestStand to access the TSAutoMgr.exe application.

- Windows 10/8.1/7 Firewall Settings

Parent topic:

Setting Up TestStand for Accessing Synchronization Objects Remotely

<!--NI_TOPIC bundle=teststand path=windows-vista-firewall-settings-local.html language=enus -->
## TOPIC 01033: Windows Vista Firewall Settings - Windows Firewall Settings for the Local Computer - Setting Up TestStand for Accessing Synchronization Objects Remotely

- bundle_id: `teststand`
- source_path: `windows-vista-firewall-settings-local.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/windows-vista-firewall-settings-local.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Complete the following steps to configure the Microsoft Windows firewall on the local computer. Log in as a user with administrator privileges. Navigate to the standard Windows Control Panel facility for Windows firewall and select the Change settings option in the Windows Firewall window to launch

### Windows Vista Firewall Settings - Windows Firewall Settings for the Local Computer - Setting Up TestStand for Accessing Synchronization Objects Remotely

Complete the following steps to configure the Microsoft Windows firewall on the local computer.

1. Log in as a user with administrator privileges.
2. Navigate to the standard Windows Control Panel facility for Windows firewall and select the Change settings option in the Windows Firewall window to launch the Windows Firewall Settings dialog box.
3. Complete the following steps to add exceptions for the client application with the firewall enabled.
  1. Click the Exceptions tab.
  2. Click the Add program button to launch the Add a Program dialog box.
  3. Click Browse and select the client application, such as <TestStand>\Bin\TSAutoMgr.exe .
  4. Click OK to close the Add a Program dialog box.
  5. Click the Add port button to launch the Add a Port dialog box.
  6. In the Name control, type DCOM .
  7. In the Port Number control, type 135 .
  8. Select the TCP option and click OK to close the Add a Port dialog box.
4. Click OK to close the Windows Firewall Settings dialog box.

Parent topic:

Windows Firewall Settings for the Local Computer - Setting Up TestStand for Accessing Synchronization Objects Remotely

Related concepts:

- Search Directories

<!--NI_TOPIC bundle=teststand path=windows-vista-firewall-settings-remote.html language=enus -->
## TOPIC 01034: Windows Vista Firewall Settings - Windows Firewall Settings for the Remote Computer - Setting Up TestStand for Accessing Synchronization Objects Remotely

- bundle_id: `teststand`
- source_path: `windows-vista-firewall-settings-remote.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/windows-vista-firewall-settings-remote.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Complete the following steps to configure the Microsoft Windows firewall on the computer that creates the synchronization object. Log in as a user with administrator privileges. Navigate to the standard Windows Control Panel facility for Windows firewall and select the Change settings option in the

### Windows Vista Firewall Settings - Windows Firewall Settings for the Remote Computer - Setting Up TestStand for Accessing Synchronization Objects Remotely

Complete the following steps to configure the Microsoft Windows firewall on the computer that creates the synchronization object.

1. Log in as a user with administrator privileges.
2. Navigate to the standard Windows Control Panel facility for Windows firewall and select the Change settings option in the Windows Firewall window to launch the Windows Firewall Settings dialog box.
3. Complete the following steps to add exceptions for the TSAutoMgr.exe application with the firewall enabled.
  1. Click the Exceptions tab.
  2. Click the Add program button to launch the Add a Program dialog box.
  3. Click Browse and select <TestStand>\Bin\TSAutoMgr.exe .
  4. Click OK to close the Add a Program dialog box.
  5. Click the Add port button to launch the Add a Port dialog box.
  6. In the Name control, type DCOM .
  7. In the Port Number control, type 135 .
  8. Select the TCP option and click OK to close the Add a Port dialog box.
4. Click OK to close the Windows Firewall Settings dialog box.

Parent topic:

Windows Firewall Settings for the Remote Computer - Setting Up TestStand for Accessing Synchronization Objects Remotely

Related concepts:

- Search Directories

<!--NI_TOPIC bundle=teststand path=workspaces.html language=enus -->
## TOPIC 01035: Workspaces

- bundle_id: `teststand`
- source_path: `workspaces.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/workspaces.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Create a workspace to organize and access development files. Use workspaces early in development so you can easily keep track of files while you are developing. A workspace file (.tsw) contains references to any number of TestStand project files. A project file (.tpj) contains references to any numb

### Workspaces

Create a workspace to organize and access development files. Use workspaces early in development so you can easily keep track of files while you are developing. A workspace file (.tsw) contains references to any number of TestStand project files. A project file (.tpj) contains references to any number of other files of any type.

Use project files to organize related files and directories of files in the test system. You can insert any number of files into a project. For example, you can use a project file to organize a sequence file, code module source files, and other supporting files.

When you use a workspace, you must define at least one project. However, defining multiple projects in a workspace can help you better organize a test system. For example, you can define product model projects that contain all the tests required for the specific product model. When a model becomes obsolete, you can remove only the corresponding project from the workspace to update the test system.

Use workspace files to help organize and access development files, to perform source code control (SCC) operations in the TestStand Sequence Editor or in a TestStand User Interface, and to store debugging information, such as breakpoints and watch expressions.

In the TestStand Sequence Editor, use the Workspace pane to view and edit a workspace file and the project files it references. You can open only one workspace file at a time. To open an existing workspace file, select File»Open File. To create a new workspace file, select File»New»Workspace File.

#### Source Code Control

Use workspace files early in development to easily access files in a source code control
 (SCC) system. When TestStand loads a workspace, the properties of a workspace specify
 whether TestStand attempts to connect to an SCC provider. When TestStand successfully
 connects to an SCC provider, you can use the commands in the Workspace context menu and the
 Source Control menu to check out and check in files from SCC. If an SCC provider returns
 warning or error messages when performing SCC operations, the sequence editor displays the
 messages in the Output pane.

To perform SCC operations on files from within TestStand, select an SCC provider on the
 Source Control tab of the Station Options dialog box and configure the SCC settings for the
 workspace on the Source Control tab of the Workspace Object Properties dialog box.

Note

Note

#### Inserting Code Modules in a Workspace

You can right-click a sequence file in the workspace and select Insert Code Modules from the context menu to automatically include the code modules a sequence file uses. However, if you are using a workspace only to create a deployment, NI does not recommend this technique.

Note

CodeModules

Insert Code Modules

#### Refreshing the Code Modules Directory in a Workspace

When a sequence file in a workspace changes or if you are using a workspace to interface with an SCC system, complete the following steps to manually refresh the code modules directory to avoid deploying files that the test system no longer requires.

1. Delete the current code modules directory from the workspace.
2. Right-click the sequence files for which you want to add code modules.
3. Select Insert Code Modules from the context menu.

#### System Deployment

You can use a workspace and project files to specify all the required files the TestStand Deployment Utility collects to successfully distribute a test system to a target computer. The deployment utility creates an image or an installer for the test system.

Parent topic:

TestStand Building Blocks

Related concepts:

- Selecting a Source Code Control Provider
- Using a TestStand Workspace File to Create a Deployment
- Deploying TestStand Systems
- Creating a Deployable Image
- Building a Customized MSI-based Installer

Related information:

- Git Pane

<!--NI_TOPIC bundle=teststand path=writing-app-teststand-engine-api.html language=enus -->
## TOPIC 01036: Writing an Application with the TestStand Engine API

- bundle_id: `teststand`
- source_path: `writing-app-teststand-engine-api.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/writing-app-teststand-engine-api.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use the TestStand Engine API to write a complete application. NI strongly recommends using the TestStand User Interface (UI) Controls to write a TestStand application.

### Writing an Application with the TestStand Engine API

You can use the TestStand Engine API to write a complete application.

Note

Parent topic:

TestStand API Overview

Related concepts:

- Writing an Application with the TestStand User Interface Controls

<!--NI_TOPIC bundle=teststand path=writing-application-with-tsui-controls.html language=enus -->
## TOPIC 01037: Writing an Application with the TestStand User Interface Controls

- bundle_id: `teststand`
- source_path: `writing-application-with-tsui-controls.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/writing-application-with-tsui-controls.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can create or customize a user interface application using the TestStand User Interface (UI) Controls based on the various example user interface applications TestStand provides. Refer to the NI TestStand UI Controls API Reference Help for more information about the TestStand UI Controls API.

### Writing an Application with the TestStand User Interface Controls

You can create or customize a user interface application using the TestStand User Interface (UI) Controls based on the various example user interface applications TestStand provides.

Refer to the NI TestStand UI Controls API Reference Help for more information about the TestStand UI Controls API.

Parent topic:

TestStand API Overview

Related concepts:

- Creating Custom User Interfaces

<!--NI_TOPIC bundle=teststand path=writing-to-csv-files-with-data-streams-step-t.html language=enus -->
## TOPIC 01038: Writing to CSV Files with Data Streams Step Types

- bundle_id: `teststand`
- source_path: `writing-to-csv-files-with-data-streams-step-t.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/writing-to-csv-files-with-data-streams-step-t.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the New CSV Output Stream step type to create a CSV file for writing and store a reference to it. The file open mode controls the behavior if the specified file already exists. After you open the file, you can write to it using the Write Record step type or the TestStand API. Each invocation of

### Writing to CSV Files with Data Streams Step Types

Use the New CSV Output Stream step type to create a CSV file for writing and store a reference to it. The file open mode controls the behavior if the specified file already exists. After you open the file, you can write to it using the Write Record step type or the TestStand API.

Each invocation of a Write Record step writes a single row of data to the output CSV file. You can specify a row using either a container or an array. If you specify a container, the subproperties of the container correspond to columns in the CSV file. If you specify an array, each array element corresponds to a column in the CSV file.

You can also write to the output file using the TestStand API. See for example OutputRecordStream.WriteRecord(), CsvFileOutputRecordStream.WriteLine(), and CsvFileOutputRecordStream.WriteFieldHeaders(). You must close the CSV file when you are finished with it by calling the OutputRecordStream.Close() method.

Parent topic:

Using the Data Streams Step Type

<!--NI_TOPIC bundle=teststand path=xml-packaging-utility.html language=enus -->
## TOPIC 01039: XML Packaging Utility

- bundle_id: `teststand`
- source_path: `xml-packaging-utility.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/xml-packaging-utility.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the XML Packaging Utility to copy local XML and HTML report files you select, including related style sheets, image files, and referenced files, to a destination directory you specify so you can view the XML report on a computer that does not have TestStand installed. You can launch the utility

### XML Packaging Utility

Use the XML Packaging Utility to copy local XML and HTML report files you select,
 including related style sheets, image files, and referenced files, to a destination
 directory you specify so you can view the XML report on a computer that does not have
 TestStand installed.

You can launch the utility in the following ways:

- Select Tools»Package XML/HTML Files for Distribution in the TestStand Sequence Editor.
- (Windows 8.1) Click the NI Launcher tile on the Start screen and select TestStand»Tools»TestStand XML Packaging Utility .
- (Windows 10 or 7) Select Start»All Programs»National Instruments»TestStand»Tools»TestStand XML Packaging Utility .

XmlPack.ini

XmlPack.ini

<TestStand Application Data>

\Cfg

COMMON_EXTENSIONS

XmlPack.ini

.docx

.xlsx

"docx, xlsx"

COMMON_EXTENSIONS

.tdms

Note

After the utility completes the packing, the selected and referenced files reside in the specified destination directory. 
The utility substitutes all file references to use the files copied to the destination directory. For distribution, you can compact, deliver, and extract the destination directory to view the copied files at the distribution location.

To package XML files, first click Add in the XML Packaging Utility dialog box and select one or more XML files to package. The files appear in the XML Files list. Use the Destination Folder control to specify the directory in which the utility copies the files to in the Destination Folder control. Click Pack to package the XML and other referenced files.

The XML Packaging Utility dialog box contains the following options:

- XML Files —The XML files to be processed.
- Add —Launches the Add XML files dialog box, in which you can specify the XML files to add to the XML Files list.
- Remove —Deletes the file or files selected in the XML Files list.
- Pack —Packages the files in the XML Files list and copies them to the directory the Destination Folder control specifies. When packaging completes, the Referenced Files list shows the packaged files. The utility stops packaging files if an error occurs during packaging.
- Destination Folder —The directory in which the utility copies the packaged files. You can specify an existing directory or enter the path of a new directory for the utility to create. If the specified directory does not yet exist and you click Pack , the utility prompts you to confirm that you want to create it. If you do not confirm the creation of the new directory, the utility stops packaging the files.
- Referenced Files (packaged) —After the utility completes the packaging process, this control lists the files the utility copies to the directory the Destination Folder control specifies. The utility renames any duplicate filenames using an incremental suffix and updates any reference to a duplicated name. If the packaging process fails, or if an XML file is added or removed, the list of packaged files is reset.
- Referenced Objects (not packaged) —After the utility completes the packaging process, this control lists the objects the packaged files reference, such as ActiveX or Java class objects. The utility does not package these objects with the files but lists them in this control so you can verify that the objects exist in the destination directory. If an XML file is added or removed, the list of referenced objects is reset.
- Exit —Closes the XML Packaging Utility dialog box.

When packaging the files, the utility displays the following icons to the left of the XML Files list and the Referenced Files list:

- Checkmark —Indicates that the utility successfully parsed an XML file.
- X —Indicates that an error occurred for the file.
- Diamond —Indicates that an HTML file is not in XHTML format but the utility processed the file.

Note

<National Instruments>\Shared\TestStand

Note

#### Command-Line Usage

You can execute the utility from the command line using the following syntax:

XMLPack [[-v] file-list [ file-list* ] dest-folder]

The following table describes the elements of this command-line syntax.

| Syntax Element | Description |
| --- | --- |
| -v | Represents verbose mode, which displays messages. |
| file-list | A valid directory or path and filename that can contain wildcard characters, such as * and ?. |
| dest-folder | A valid directory or path, which might not exist. If it does not exist, TestStand creates it. |

Square brackets contain optional command-line arguments. If you do not specify an argument, the dialog-based XML Packaging Utility launches.

When run from the command line, the utility returns an error code of 0 if successful and non-zero if an error occurred.

Parent topic:

TestStand Tools and Utilities

Related concepts:

- Including Hyperlinks in a Report
- Search Directories
- NI_TDMSReference
- Displaying Measurement Data as Graphs

Related information:

- XML Packaging Utility Environment Reference

<!--NI_TOPIC bundle=teststand path=xml-report-style-sheets.html language=enus -->
## TOPIC 01040: XML Report Style Sheets

- bundle_id: `teststand`
- source_path: `xml-report-style-sheets.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/xml-report-style-sheets.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Apply a style sheet to an XML report to specify how a web browser or external viewer application displays the XML content. Use the Style Sheet control on the Contents tab of the Report Options dialog box to select the style sheet to apply to an XML report. The <xml-style sheet> node of an XML report

### XML Report Style Sheets

Apply a style sheet to an XML report to specify how a web browser or external viewer application displays the XML content. Use the Style Sheet control on the Contents tab of the Report Options dialog box to select the style sheet to apply to an XML report.

The <xml-style sheet> node of an XML report contains the URL path of the style sheet to apply to the XML file, as shown in the following example in which the <xml-style sheet> node references the built-in horizontal.xsl TestStand style sheet:

<?xml-style sheet type="text/xsl" href="C:\Program Files\National
 Instruments\TestStand
 2014\Components\Models\TestStandModels\StyleSheets\horizontal.xsl"?>

#### Built-in Style Sheets

TestStand provides the following style sheets, located in the <TestStand>\Components\Models\TestStandModels\StyleSheets directory. You can customize the style sheets directly.

- horizontal.xsl —Displays reports in a horizontal, tabular, indented format
 with data for each step in one or more rows, as shown in the following
 figure.
- report.xsl —Displays reports in a vertical, tabular, indented format with
 data for each step in multiple rows, as shown in the following figure.
 Customizable, color-coded rows visually separate relevant information, such as
 step group, status, and so on.
- expand.xsl —Displays reports similar to report.xsl , with
 expandable and collapsible sections for each step or for the entire report, as
 shown in the following figure. The report displays each step result as a
 separate table.

#### Using Foreign Characters in XML Report Style Sheets

Using some foreign characters in the XML report style sheets might result in the error "An invalid character was found in text content." To work around this issue, use the HTML code equivalent for the foreign character or add the appropriate encoding attribute to the <xsl:output> tag of the style sheet.

Parent topic:

XML Reports

Related concepts:

- TestStand Directory Structure
- Customizing XML Report Style Sheets
- Choosing the Appropriate Report Generation Strategy

<!--NI_TOPIC bundle=teststand path=xml-reports.html language=enus -->
## TOPIC 01041: XML Reports

- bundle_id: `teststand`
- source_path: `xml-reports.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/xml-reports.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: TestStand generates two types of XML reports: XML reports that validate against the TestStand Report schema, Report.xsd, which conforms to the XML W3C Schema. Report.xsd is located in the <TestStand>\Components\Models\TestStandModels directory. Automatic Test Markup Language (ATML) reports that vali

### XML Reports

TestStand generates two types of XML reports:

- XML reports that validate against the TestStand Report schema, Report.xsd ,
 which conforms to the XML W3C Schema. Report.xsd is located in
 the <TestStand>\Components\Models\TestStandModels 
 directory.
- Automatic Test Markup Language (ATML) reports that validate against the ATML Test Results and
 Session Information schema, TestResults.xsd , which the ATML
 standard defines. TestResults.xsd is located in the
 <TestStand>\Components\Models\TestStandModels\ATML\Schemas 
 directory.

By default, TestStand generates ATML reports. You cannot modify the XML TestStand generates, the TestStand Report schema, or the ATML Test Results and Session Information report schema, but you can customize how TestStand ATML and XML reports appear when displayed in a browser. Additionally, you can write XML report generators to generate custom XML reports.

Note

- All TestStand report generators support generating reports that contain 64-bit integer data types. Signed 64-bit integers use the %d format string, and unsigned 64-bit integers use the %u format string.
- XML reports might display a table of measurement data instead of a graph under certain conditions.

Parent topic:

Generating and Customizing TestStand Reports

Related concepts:

- TestStand Directory Structure
- ATML
- ATML Test Results Reports
- Displaying Measurement Data in an XML Report
- Comparing Report Format Features

<!--NI_TOPIC bundle=teststand path=year-based-and-major.html language=enus -->
## TOPIC 01042: Year-Based and Major.Minor Version Equivalents

- bundle_id: `teststand`
- source_path: `year-based-and-major.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/year-based-and-major.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Versions of TestStand that follow year-based versioning continue to use major.minor notation for some features. The following table lists year-based TestStand versions and the equivalent major.minor notation. 2 TestStand Versions and the Equivalent Major.Minor Notation Year-Based Version Major.Minor

### Year-Based and Major.Minor Version Equivalents

Versions of TestStand that follow year-based versioning continue to use major.minor notation for some features. The following table lists year-based TestStand versions and the equivalent major.minor notation.

| Year-Based Version | Major.Minor Internal Version | Engine Version |
| --- | --- | --- |
| TestStand 2025 Q2 | 24.9 | 23.0.0 |
| TestStand 2024 Q4 | 24.8 | 23.0.0 |
| TestStand 2023 Q4 | 23.8 | 23.0.0.49152 |
| TestStand 2022 Q4 | 22.0 | 22.0.0.49152 |
| TestStand 2021 SP1 | 21.1 | 21.1.0.49154 |
| TestStand 2021 | 21.0 | 21.0.0.49156 |
| TestStand 2020 | 20.0 | 20.0.0.49180 |
| TestStand 2019 | 19.0 | 19.0.0.170 |
| TestStand 2017 SP1 | 17.1 | 17.1.0.130 |
| TestStand 2017 | 17.0 | 17.0.0.184 |
| TestStand 2016 SP1 | 16.1 | 16.1.0.52 |
| TestStand 2016 | 16.0 | 16.0.0.193 |
