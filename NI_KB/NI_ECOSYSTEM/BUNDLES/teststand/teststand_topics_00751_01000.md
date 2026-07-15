# NI DOCUMENT BUNDLE: teststand

<!--NI_BUNDLE_CHUNK bundle=teststand start=751 end=1000 -->
<!--NI_TOPIC bundle=teststand path=rendering-html-elements-atml.html language=enus -->
## TOPIC 00751: Rendering HTML Elements and New Line Characters in an ATML Test Results 6.01 or 5.0 Report

- bundle_id: `teststand`
- source_path: `rendering-html-elements-atml.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/rendering-html-elements-atml.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Complete the following steps to ensure a report renders HTML elements and new line characters using the TR6_Horizontal.xsl, TR5_Horizontal.xsl, TR6_report.xsl, TR5_report.xsl, TR6_Expand.xsl, or TR5_Expand.xsl files. Open the .xsl file you want to change. Search for the Customization variables comme

### Rendering HTML Elements and New Line Characters in an ATML Test Results 6.01 or 5.0 Report

Complete the following steps to ensure a report renders HTML elements and new line characters using the TR6_Horizontal.xsl, TR5_Horizontal.xsl, TR6_report.xsl, TR5_report.xsl, TR6_Expand.xsl, or TR5_Expand.xsl files.

1. Open the .xsl file you want to change.
2. Search for the Customization variables comment.
3. Search for the gDisplayNewLineAndHTMLElementInStringProperty variable and change the value of the select attribute from "false" to "true", which results in the following line of code: <xsl:variable name="gDisplayNewLineAndHTMLElementInStringProperty"select="true()"/>

For example, if you create a local string variable named StringContainingHTMLElementAndNewLine and specify Locals.StringContainingHTMLElementAndNewLine="<b>Hello\n\World</b>" in the TestStand expression, executing the sequence file generates a modified report, as shown for each file type in the following figures:

TR6_Horizontal.xsl or TR5_Horizontal.xsl

[IMAGE alt='image' src='GUID-F56B197E-C092-4D73-85B5-7E34D937B09D-a5.png']

TR6_report.xsl or TR5_report.xsl

[IMAGE alt='image' src='GUID-F2640200-BA71-4C62-B436-B683D591A2D9-a5.png']

TR6_Expand.xsl or TR5_Expand.xsl

[IMAGE alt='image' src='GUID-660A0F5A-DCD0-4280-8A8A-8F5B380AC5EF-a5.png']

Parent topic:

Customizing ATML Test Results 6.01 or 5.0 Report Style Sheets

<!--NI_TOPIC bundle=teststand path=rendering-html-elements-xml.html language=enus -->
## TOPIC 00752: Rendering HTML Elements and New Line Characters in an XML Report

- bundle_id: `teststand`
- source_path: `rendering-html-elements-xml.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/rendering-html-elements-xml.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Complete the following steps to ensure a report renders HTML elements and new line characters using the horizontal.xsl, report.xsl, or expand.xsl files. Open the .xsl file you want to change. Search for the Customization variables comment. Search for the gDisplayNewLineAndHTMLElementInStringProperty

### Rendering HTML Elements and New Line Characters in an XML Report

Complete the following steps to ensure a report renders HTML elements and new line characters using the horizontal.xsl, report.xsl, or expand.xsl files.

1. Open the .xsl file you want to change.
2. Search for the Customization variables comment.
3. Search for the gDisplayNewLineAndHTMLElementInStringProperty variable and
 change the value of the select attribute from "false" to "true", which results
 in the following line of code:
 <xsl:variable name="gDisplayNewLineAndHTMLElementInStringProperty"select="true()"/>

For example, if you create a local string variable named StringContainingHTMLElementAndNewLine and specify Locals.StringContainingHTMLElementAndNewLine="<b>Hello\n\World</b>" in the TestStand expression, executing the sequence file generates a modified report.

#### horizontal.xsl

The following figure shows the modified report using horizontal.xsl:

[IMAGE alt='image' src='GUID-211B916F-A2AB-4BB2-97F8-F2F62B473F7B-a5.png']

#### report.xsl

The following figure shows the modified report using report.xsl:

[IMAGE alt='image' src='GUID-002A4DC1-8A92-482D-997D-E41D15631086-a5.png']

#### expand.xsl

The following figure shows the modified report using expand.xsl:

[IMAGE alt='image' src='GUID-C0BF799C-23D1-4501-A194-2657888E242E-a5.png']

Parent topic:

Customizing XML Report Style Sheets

<!--NI_TOPIC bundle=teststand path=report-generation-functions-and-sequences.html language=enus -->
## TOPIC 00753: Report Generation Functions and Sequences

- bundle_id: `teststand`
- source_path: `report-generation-functions-and-sequences.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/report-generation-functions-and-sequences.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: When you want to customize report generation for a test station, modify the default report generator process model plug-in or create a new report generator process model plug-in. To modify an installed default process model plug-in, copy all files from the <TestStand>\Components\Models\TestStandMode

### Report Generation Functions and Sequences

When you want to customize report generation for a test station, modify the default report generator process model plug-in or create a new report generator process model plug-in.

To modify an installed default process model plug-in, copy all files from the <TestStand>\Components\Models\TestStandModels directory and <TestStand>\Components\Models\ModelPlugins\NI_ReportGenerator.seq to the <TestStand Public>\Components\Models\TestStandModels and <TestStand Public>\Components\Models\ModelPlugins directories and make changes to the copied files. Rename the files after you modify them if you want to create a separate custom model plug-in to prevent the copied model plug-in from overwriting the default plug-in.

Note

- If you modify any process model or process model plug-in types, open and save all the process models and process model plug-ins that use the modified types to ensure you avoid a type conflict.
- If you do not rename the files and you use the files in a future version of TestStand, changes
 NI makes to the component might not be compatible with the modified version
 of the component. Storing new and customized files in the
 <TestStand Public> directory ensures that new
 installations of the same version of TestStand do not override the
 customizations and ensures that uninstalling TestStand does not remove the
 files you customize.

Parent topic:

Process Model Architecture

Related concepts:

- TestStand Directory Structure
- Type Versioning
- Copying Read-Only Files to Modify
- Default Report Generator Process Model Plug-in Sequences that Generate Reports
- Default Process Model Sequences and Functions for Generating Step Results
- Model Callbacks You Can Override to Alter Report Generation

<!--NI_TOPIC bundle=teststand path=representing-pointer-sized-numbers-in-sequenc.html language=enus -->
## TOPIC 00754: Representing Pointer-Sized Numbers in Sequences in 32-bit TestStand and 64-bit TestStand

- bundle_id: `teststand`
- source_path: `representing-pointer-sized-numbers-in-sequenc.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/representing-pointer-sized-numbers-in-sequenc.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Avoid using pointer-sized integers in sequences because no equivalent TestStand numeric data type exists. An example of a pointer-sized integer is the size_t type in C/C++, which is the size of a pointer but is intended to be used as a true integer data type. The TestStand Number data type supports

### Representing Pointer-Sized Numbers in Sequences in 32-bit TestStand and 64-bit TestStand

Avoid using pointer-sized integers in sequences because no equivalent TestStand numeric data type exists. An example of a pointer-sized integer is the size_t type in C/C++, which is the size of a pointer but is intended to be used as a true integer data type.

The TestStand Number data type supports the following representations:

- 64-bit double-precision, floating-point (default representation)
- 64-bit signed integer
- 64-bit unsigned integer

Use the default 64-bit double-precision, floating-point representation to store signed and unsigned 32-bit integers because the 64-bit double-precision, floating-point representation can represent all possible 32-bit integer values. For 32-bit integers, the default 64-bit double-precision, floating-point representation is more appropriate than using the 64-bit signed or unsigned integer representations because TestStand supports automatic conversion between the default representation and 32-bit integer types in module adapter steps. A 64-bit double-precision, floating-point representation cannot exactly represent all possible 64-bit integer values, so TestStand does not allow automatic conversion between Numbers with the 64-bit double-precision, floating-point representation and 64-bit integer data types.

If no workaround exists to using pointer-sized integers in TestStand, use one of the following strategies:

- Use an Object Reference data type to store the number as a pointer.
- Use a TestStand Number data type with representation based on bitness.
- Use two separate variables.

Parent topic:

64-bit TestStand and Migrating from 32-bit TestStand

Related concepts:

- Using an Object Reference to Represent Pointer-Sized Numbers in Sequences in 32-bit TestStand and 64-bit TestStand
- Using a TestStand Number with Representation Based on Bitness to Represent Pointer-Sized Numbers in Sequences in 32-bit TestStand and 64-bit TestStand
- Using Two Separate Variables to Represent Pointer-Sized Numbers in Sequences in 32-bit TestStand and 64-bit TestStand

<!--NI_TOPIC bundle=teststand path=representing-pointers-in-sequences-in-32-bit.html language=enus -->
## TOPIC 00755: Representing Pointers in Sequences in 32-bit TestStand and 64-bit TestStand

- bundle_id: `teststand`
- source_path: `representing-pointers-in-sequences-in-32-bit.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/representing-pointers-in-sequences-in-32-bit.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the Object Reference data type to manipulate and store pointers and pointer-sized handles in TestStand sequences regardless of architecture. The Object Reference data type automatically matches the bitness of TestStand. If you use the LabWindows/CVI or C/C++ DLL Adapters, use the appropriate poi

### Representing Pointers in Sequences in 32-bit TestStand and 64-bit TestStand

Use the Object Reference data type to manipulate and store pointers and pointer-sized handles in TestStand sequences regardless of architecture. The Object Reference data type automatically matches the bitness of TestStand. If you use the LabWindows/CVI or C/C++ DLL Adapters, use the appropriate pointer/handle parameter type when you specify a prototype.

Using the Number data type to store pointers as 32-bit integers worked well in previous versions
 of TestStand because the default representation of the Number data type supports
 automatic conversion to and from 32-bit integer types. If you use the Number data
 type to represent a 64-bit pointer, the Number must use a signed or unsigned 64-bit
 integer representation. Storing 32-bit pointers in 64-bit integers does not work
 well in TestStand because you cannot automatically convert Numbers with 64-bit
 integer representations to and from 32-bit integer types. NI does not recommend
 using a numeric data type for storing pointers.

Use the pointer/handle parameter type and the constant Object Reference Nothing instead of a numeric parameter type and the constant Number 0 to represent NULL pointers.

Parent topic:

64-bit TestStand and Migrating from 32-bit TestStand

<!--NI_TOPIC bundle=teststand path=required-visual-studio-components-for-buildin.html language=enus -->
## TOPIC 00756: Required Visual Studio Components for Building Custom C# User Interfaces

- bundle_id: `teststand`
- source_path: `required-visual-studio-components-for-buildin.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/required-visual-studio-components-for-buildin.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: To build custom C# user interfaces, you must install additional components with Visual Studio. TestStand includes two directories containing example C# user interfaces: <TestStand Public>\UserInterfaces\Full-Featured\CSharp\Source Code <TestStand Public>\UserInterfaces\Simple\CSharp\Source Code If y

### Required Visual Studio Components for Building Custom C# User Interfaces

To build custom C# user interfaces, you must install additional components with Visual Studio.

TestStand includes two directories containing example C# user interfaces:

- <TestStand Public>\UserInterfaces\Full-Featured\CSharp\Source Code
- <TestStand Public>\UserInterfaces\Simple\CSharp\Source Code

If you use the files in these directories as a starting point for creating custom user interfaces, you must install the Desktop development with C++ component for the version of Visual Studio you use. This component includes the MSVC Visual C++ build tools, which are required for building C# user interfaces in TestStand. You can install Desktop development with C++ during the initial Visual Studio installation or launch the Visual Studio installer to modify your existing installation.

Parent topic:

Example User Interfaces

Related concepts:

- Example User Interfaces
- TestStand Directory Structure

<!--NI_TOPIC bundle=teststand path=reserving-loaded-vis-for-execution.html language=enus -->
## TOPIC 00757: Reserving Loaded VIs for Execution

- bundle_id: `teststand`
- source_path: `reserving-loaded-vis-for-execution.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/reserving-loaded-vis-for-execution.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Enable the Reserve Loaded VIs for Execution option in the LabVIEW Adapter Configuration dialog box to reserve any VIs TestStand loads for calling with the LabVIEW Adapter. Use this option to avoid reloading VIs when they are used and to make references you create in a VI you call from TestStand—such

### Reserving Loaded VIs for Execution

Enable the Reserve Loaded VIs for Execution option in the LabVIEW Adapter Configuration dialog box to reserve any VIs TestStand loads for calling with the LabVIEW Adapter.

Use this option to avoid reloading VIs when they are used and to make references you create in a VI you call from TestStand—such as I/O, ActiveX, and synchronization references—persist across calls to other VIs. You can store these references in a TestStand property and pass them to subsequent VIs you call from TestStand.

#### Editing a Reserved VI

|  | When you open a reserved VI in LabVIEW, the Run arrow indicates the VI is reserved, and you cannot edit the VI. |
| --- | --- |

|  | To edit a VI TestStand has reserved, click the Edit VI button on the LabVIEW Module tab in the TestStand Sequence Editor or on the Module tab of the Edit LabVIEW VI Call dialog box in a TestStand User Interface. You can also right-click the step and select Edit Code from the context menu to open the VI in TestStand. |
| --- | --- |

You can also select File»Unload All Modules in the TestStand Sequence Editor before you open the VI in LabVIEW.

#### Closing References to a Reserved VI

You must close any references you create to VIs. When TestStand loads and reserves VIs, LabVIEW does not automatically close the references until TestStand unloads the VIs that created the references. Failing to close the references might result in a memory leak in the test system.

#### Reserving VIs Affects the LabVIEW VI
 Server Run VI Method

By default, TestStand enables the Reserve
 Loaded VIs for Execution option in the LabVIEW Adapter Configuration
 dialog box so that all VIs TestStand loads remain in memory. Enabling this option
 improves execution time because TestStand does not need to load and unload
 VIs.

When running a VI reserved for execution, LabVIEW creates a proxy VI to
 call the VI configured in the TestStand step as a subVI of the proxy. Therefore,
 LabVIEW considers VIs called from TestStand as subVIs.

When you open and run a
 subVI as a top-level VI in LabVIEW, LabVIEW returns error code 1000. Additionally,
 if you use the Open VI Reference function to open a VI that TestStand marks as
 reserved for execution, the VI opens as a top-level VI, and you then use the VI
 Server Run VI method, LabVIEW returns error 1000.

You can use the following
 techniques to work around this LabVIEW behavior:

- Create a wrapper VI that calls the VI as a subVI. You can then use the Open VI
 Reference function to open the wrapper VI and run it with the Run VI method of
 the VI Server.
- Make the VI re-entrant.
- On the Run Options panel of the Step Settings pane of the LabVIEW step that
 calls the VI, change the Load Option setting to
 Load dynamically and the Unload
 Option setting to Unload after step
 executes .

Parent topic:

Special Considerations for Using LabVIEW with TestStand Systems

Related concepts:

- Reusing VIs
- Partially Specifying LabVIEW Clusters

<!--NI_TOPIC bundle=teststand path=resolving-references-to-shared-variables.html language=enus -->
## TOPIC 00758: Resolving References to Shared Variables

- bundle_id: `teststand`
- source_path: `resolving-references-to-shared-variables.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/resolving-references-to-shared-variables.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: LabVIEW VIs can use shared variables deployed on remote targets. NI recommends specifying these VIs using a LabVIEW project, which also has the remote target defined, and executing these VIs using a LabVIEW project from TestStand. When you deploy a LabVIEW project library or execute these VIs in Tes

### Resolving References to Shared Variables

LabVIEW VIs can use shared variables deployed on remote targets. NI recommends specifying these
 VIs using a LabVIEW project, which also has the remote target defined, and executing
 these VIs using a LabVIEW project from TestStand.

When you deploy a LabVIEW project library or execute these VIs in TestStand on a remote target, LabVIEW must determine how to resolve the target name stored in the network path for the variable. When you configure a target in a LabVIEW project, LabVIEW stores the IP address for the target in an aliases file located in the same directory as the project. The aliases file uses the same base name as the project and a .aliases file extension.

When executing VIs in the main application instance, the server you configured the LabVIEW Adapter to use in the LabVIEW Adapter Configuration dialog box determines the aliases file LabVIEW uses in the following ways:

- LabVIEW Run-Time Engine —LabVIEW looks for an aliases file with the same name and location as the TestStand application, such as SeqEdit.aliases for the TestStand Sequence Editor and TestExec.aliases for a TestStand User Interface. You must quit and restart the TestStand application after you copy the aliases file from the project directory to the application directory.
- Development System —LabVIEW looks for an aliases file, LabVIEW.aliases , located in the same directory as the LabVIEW development system executable. You must quit and restart LabVIEW after you copy the aliases file from the project directory to the LabVIEW directory.
- Other Executable —LabVIEW looks for an aliases file with the same name and location as the LabVIEW executable server, such as TestStandLVRTS.aliases for TestStandLVRTS.exe and TestExec.aliases for a user interface. You must quit and restart the executable after you copy the aliases file from the project directory to the executable directory.

When the test system executes VIs specified in a LabVIEW project, LabVIEW looks for an alias file with the same name and location as the specified LabVIEW project.

Note

Parent topic:

Deploying Network-Published Shared Variables

Related concepts:

- Organizing Test Program Files with LabVIEW Projects
- Organizing Test Program Files with LabVIEW Project Libraries
- Programming with the TestStand API in LabVIEW

<!--NI_TOPIC bundle=teststand path=resource-names-resource-usage-profiler.html language=enus -->
## TOPIC 00759: Resource Names - Resource Usage Profiler

- bundle_id: `teststand`
- source_path: `resource-names-resource-usage-profiler.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/resource-names-resource-usage-profiler.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Resource Names You typically name TestStand locks after the resources the locks protect, such as DMM1 or DC Power Supply. When the Resource Usage Profiler displays information about a resource, such as the name of the resource, the profiler is actually describing the lock that protects the resource.

### Resource Names - Resource Usage Profiler

#### Resource Names

You typically name TestStand locks after the resources the locks protect, such as DMM1 or DC Power Supply. When the Resource Usage Profiler displays information about a resource, such as the name of the resource, the profiler is actually describing the lock that protects the resource.

If you create a lock or another type of synchronization object with an empty name, TestStand names the object for you, such as Unnamed Synchronization Object - <N>. TestStand also automatically selects a resource name in the following cases:

- When you use the Use Lock to Allow Only One Thread at a Time to Execute the Step option on the Synchronization panel of the Properties tab of the Step Settings pane and not specifying an existing lock
- When you use the Batch Synchronization option on the Synchronization panel of the Properties tab of the Step Settings pane
- When you use a Wait step
- When you use a Use Auto Scheduled Resource step

In these cases, TestStand creates a resource name by combining the unique ID of the step with the run-time ID of the file that contains the step. However, for readability, the profiler window shows the name of the step as the resource name. If the step name is not a unique resource name, the profiler appends the unique resource name that TestStand creates to the step name. For Use Auto Scheduled Resource steps that do not have unique names, the profiler first attempts to make the step name unique by appending a description of the locks the step acquires.

Parent topic:

Item Names

Related information:

- Step Settings Pane
- Use Auto Scheduled Resource Step
- Wait Step

<!--NI_TOPIC bundle=teststand path=resource-strings-and-internationalization.html language=enus -->
## TOPIC 00760: Resource Strings and Internationalization

- bundle_id: `teststand`
- source_path: `resource-strings-and-internationalization.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/resource-strings-and-internationalization.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: To provide a way for both the application developer and the end-user to internationalize the text of applications and dialog boxes, TestStand provides a resource string file mechanism for storing all the application text in a central location. You can change the strings the application displays by e

### Resource Strings and Internationalization

To provide a way for both the application developer and the end-user to internationalize the text of applications and dialog boxes, TestStand provides a resource string file mechanism for storing all the application text in a central location. You can change the strings the application displays by editing or creating .ini files in a text editor.

To add string support for the internationalization of the application, use the Engine.GetResourceString method to obtain the text for the windows and controls. You can add strings to an existing string file or create a new string file in the appropriate directory under the <TestStand Public>\Components\Language directory. Ensure that you create a unique category for the strings.

Parent topic:

Writing an Application with the TestStand Engine API

Related concepts:

- Creating String Resource Files
- TestStand Directory Structure

<!--NI_TOPIC bundle=teststand path=result-collection.html language=enus -->
## TOPIC 00761: Result Collection

- bundle_id: `teststand`
- source_path: `result-collection.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/result-collection.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: TestStand automatically collects the results of each step. You can configure result collection for each step on the Run Options panel of the Step Settings pane. You can disable result collection for an entire sequence in the Sequence Properties dialog box or completely disable result collection on a

### Result Collection

TestStand automatically collects the results of each step. You can configure result collection for each step on the Run Options panel of the Step Settings pane. You can disable result collection for an entire sequence in the Sequence Properties dialog box or completely disable result collection on a computer in the Station Options dialog box.

You can generate a report and log results to a database to process the collected test results.

Each sequence includes a ResultList local variable, which is an empty
 array of container properties that you can access using Locals.ResultList.
 TestStand appends a new container property, the step result, to the end of the
 ResultList array before a step executes. After the step executes,
 TestStand copies the contents of the Result subproperty for the step into the step result in
 the ResultList array.

Each step type can define different contents for the Result subproperty of the step, and TestStand can append step results that contain Result properties from different step types to the same ResultList array. When TestStand copies the Result property for a step to the step result, TestStand also adds the name of the step, the position of the step in the sequence, and other identifying information. For a step that calls a subsequence, TestStand also adds the ResultList array variable from the subsequence.

Using the TestStand API, a process model can request that TestStand insert additional step properties in the step results for all steps automatically. A code module can also use the TestStand API to insert additional step result information for a particular step.

#### Report Generation

When you run a sequence using the Test UUTs or Single Pass Execution entry point, the report generator model plug-in generates the report by traversing the results for the main sequence in the client sequence file and all the subsequences it calls.

Parent topic:

Executions

Related concepts:

- Database Logging
- Custom Result Properties
- Exceptions to Custom Result Properties
- Standard Result Properties
- Loop Results

Related information:

- Locals Context Menu - Sequence File Tab

<!--NI_TOPIC bundle=teststand path=retrieving-binary-string-values-from-reports.html language=enus -->
## TOPIC 00762: Retrieving Binary String Values from Reports and Databases

- bundle_id: `teststand`
- source_path: `retrieving-binary-string-values-from-reports.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/retrieving-binary-string-values-from-reports.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The TestStand LabVIEW Adapter and the TestStand API function PropertyObject.SetValBinary support assigning binary values to string variables or properties. TestStand stores binary string values as compressed and encoded binary data using only printable non-MBCS-lead-byte characters. The default Test

### Retrieving Binary String Values from Reports and Databases

The TestStand LabVIEW Adapter and the TestStand API function PropertyObject.SetValBinary support assigning binary values to string variables or properties. TestStand stores binary string values as compressed and encoded binary data using only printable non-MBCS-lead-byte characters. The default TestStand report generator and database logging process model plug-ins store the binary string values in the compressed encoded format.

To retrieve the binary data from a string value in reports or databases, you must first assign the string value to a TestStand string property either by calling the PropertyObject.SetValString method or by copying the value into a string property in the TestStand Variables View. Then you must retrieve the binary value using the PropertyObject.GetValBinary method on the string property.

Note

Parent topic:

Generating and Customizing TestStand Reports

<!--NI_TOPIC bundle=teststand path=reusing-vis.html language=enus -->
## TOPIC 00763: Reusing VIs

- bundle_id: `teststand`
- source_path: `reusing-vis.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/reusing-vis.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: If a user interface calls a VI that the test program also calls as a code module, you must ensure that the name of the VI called from the user interface does not match the name of the VI when it is called as a code module. Apply a prefix to all dependent VIs when building the user interface into a s

### Reusing VIs

If a user interface calls a VI that the test program also calls as a code module, you must ensure that the name of the VI called from the user interface does not match the name of the VI when it is called as a code module.

Apply a prefix to all dependent VIs when building the user interface into a stand-alone application to avoid a naming conflict among the dependencies of the user interface executable and the code module VIs called from test sequences.

Note

Parent topic:

Special Considerations for Using LabVIEW with TestStand Systems

Related concepts:

- Using TestStand UI Controls in LabVIEW
- Deploying Network-Published Shared Variables
- Managing Memory Allocation for Large LabVIEW Data Sets
- Reserving Loaded VIs for Execution

<!--NI_TOPIC bundle=teststand path=reverting-a-patch-deployment.html language=enus -->
## TOPIC 00764: Reverting a Patch Deployment

- bundle_id: `teststand`
- source_path: `reverting-a-patch-deployment.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/reverting-a-patch-deployment.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the following table to determine how to revert a patch deployment based on the deployment mechanism you use. 44 Reverting a Patch Deployment Deployment Mechanism Action to Take to Revert Patch Deployment Installers Uninstall the files for the full deployment, which uninstalls all associated patc

### Reverting a Patch Deployment

Use the following table to determine how to revert a patch deployment based on the deployment mechanism you use.

| Deployment Mechanism | Action to Take to Revert Patch Deployment |
| --- | --- |
| Installers | Uninstall the files for the full deployment, which uninstalls all associated patch deployments. Reinstall the version of the full deployment and previous patch deployments you want. |
| Source Code Control System | Force-synchronize files to a date earlier than the patch deployment you want to revert. |
| Network Drive | Create a list of all files in the patch deployable image. For each file, determine if the file exists in the full deployable image or in previous patch deployable images. If the file exists in the deployable image, copy the latest version of the file to the network drive. If the file does not exist in the deployable image, delete the file from the network drive. |

Parent topic:

Patching Deployments

Related concepts:

- Choosing a Deployment Mechanism
- Building a Customized MSI-based Installer
- Using a Source Code Control System to Deploy Test Systems
- Using a Network Drive to Deploy Test Systems

<!--NI_TOPIC bundle=teststand path=route-specification-strings.html language=enus -->
## TOPIC 00765: Route Specification Strings

- bundle_id: `teststand`
- source_path: `route-specification-strings.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/route-specification-strings.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: When you instruct TestStand to connect or disconnect routes defined in an NI Switch Executive virtual device, you must specify a route specification string. The syntax of a route specification string consists of a series of routes that ampersands (&) delimit. NI Switch Executive ignores white space

### Route Specification Strings

When you instruct TestStand to connect or disconnect routes defined in an NI Switch Executive virtual device, you must specify a route specification string. The syntax of a route specification string consists of a series of routes that ampersands (&) delimit. NI Switch Executive ignores white space characters between tokens in a route specification string.

The syntax for a route specification string is as follows:

routeOrGroup { & routeOrGroup } { & routeOrGroup } . . .

Where routeOrGroup is one of the following:

- Route name
- Route group name
- Fully-specified path—Enclosed in square brackets and consisting of a series of channels that " -> " delimits. The following shows the format of a fully-specified path:
 [ channel {-> channel } {-> channel} . . . ]

A channel must be one of the following:

- Channel alias name
- Unique name—A combination of the IVI device logical name and IVI channel name that a "/" delimiter separates
- IVI channel name

Channels on either end of a bracketed, fully specified path must not be a Configuration or a Hardwired channel. Only one end channel can be a Source channel. The inner channels in a route specification string must be either a Configuration or Hardwired channel. The following are examples of route specification strings:

[SampleMatrix1/c0->SampleMatrix1/r1->SampleMatrix1/c4]

[Scope->R3->SampleMatrix1/c6]

ArbToInput & ScopeToOutput

PowerDevice & [Scope->R3->UUT_Out]

To specify a route specification string in an expression, the expression must return a valid route specification string when TestStand evaluates the expression. The following are examples of expressions that return valid route specification strings:

"PowerDevice & [Scope->R3->UUT_Out]"

Locals.MyRouteGroupName + "& ScopeToOutput"

SwitchFindRoute("DeviceName", "DeviceChan1", "DeviceChan2") + "&" + Locals.RouteName

Note

- You can use NI Switch Executive to find an available path at run time by slightly modifying the syntax. Remove the square brackets and replace them with the two endpoints of the route that a -> delimits.
- Any channel, other than an endpoint, within a route specification string must be reserved for routing or directly hardwired to one of the endpoint channels. Channels, other than endpoints, must not be configuration channels.
- When connecting a route, the list of channels may only include a single source channel either explicitly or implicitly by means of a previous connection. Attempts to connect two sources together will result in an error.
- You can use the SwitchFindRoute expression function to dynamically determine a physical route path at run time.

Parent topic:

Instrument Drivers

Related concepts:

- Expressions

<!--NI_TOPIC bundle=teststand path=run-time-errors.html language=enus -->
## TOPIC 00766: Run-Time Errors

- bundle_id: `teststand`
- source_path: `run-time-errors.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/run-time-errors.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: TestStand generates a run-time error when it encounters a condition that prevents a sequence from executing. For example, when a precondition refers to the status of a step that does not exist, TestStand generates a run-time error when it attempts to evaluate the precondition. TestStand also generat

### Run-Time Errors

TestStand generates a run-time error when it encounters a condition that prevents a sequence from executing. For example, when a precondition refers to the status of a step that does not exist, TestStand generates a run-time error when it attempts to evaluate the precondition. TestStand also generates a run-time error when a code module causes an access violation or any other exception.

TestStand does not use run-time errors to indicate UUT test failures. Instead, a run-time error indicates a problem exists with the testing process itself and testing cannot continue. Usually, a code module reports a run-time error when it detects an error in a hardware or software resource it uses to perform a test.

When a run-time error occurs, the sequence runs steps in the Cleanup step group, if not already executing, and returns to the calling sequence. When a subsequence with a run-time error returns to a calling sequence, TestStand sets the calling sequence step status to Error, and the calling sequence continues to propagate the run-time error up the call stack unless you enabled the Ignore Run-Time Errors option on the Run Options panel of the Step Settings pane for the Sequence Call step. When you enable this setting, TestStand ignores the error for the thread, and the thread execution continues normally. If TestStand returns the run-time error to the root sequence invocation, the result status for the execution is Error.

To interactively handle run-time errors, configure TestStand to launch the Run-Time Error dialog box in the event of an error by selecting Show Dialog from the On Run-Time Error ring control on the Execution tab of the Station Options dialog box.

You can also invoke Post-Step RunTime Error Engine callbacks when a run-time error occurs.

Parent topic:

Result Collection

Related concepts:

- List of Engine Callbacks

<!--NI_TOPIC bundle=teststand path=runstate-subproperties.html language=enus -->
## TOPIC 00767: RunState Subproperties

- bundle_id: `teststand`
- source_path: `runstate-subproperties.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/runstate-subproperties.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The RunState property object contains properties that describe the state of execution in the sequence invocation. Sequence Context Subproperty Description Engine Engine object in which the sequence invocation executes. Root Sequence context for the root sequence invocation. When you initiate an exec

### RunState Subproperties

The RunState property object contains properties that describe the state of execution in the sequence invocation.

| Sequence Context Subproperty | Description |
| --- | --- |
| Engine | Engine object in which the sequence invocation executes. |
| Root | Sequence context for the root sequence invocation. When you initiate an execution using a process model entry point, the property is the sequence context for the entry point. For example, when you use an entry point from the default TestStand process model, the Root property is the sequence context of the Test UUTs or the Single Pass sequence. When you initiate an execution on a sequence without using a Process Model entry point, the Root property object is the sequence context for the sequence you run. |
| Main | Sequence context for the least-nested sequence that is not in a process model. When you initiate an execution using the default process model entry point, the Main property is the sequence context of the Main sequence. When you initiate an execution on a sequence without using a process model entry point, the Main property object is the sequence context for whichever sequence you run. |
| ThisContext | Reference to the current sequence context. You usually use this property to pass the entire sequence context as an argument to another sequence or a code module. |
| Caller | Sequence context for the sequence that called the current sequence. This property does not exist in the root sequence context. |
| CallingStep | Run-time copy of the Step object for the step that called the current sequence. This property does not exist in the root sequence context. Any changes to property values in this object only modify the execution version of the object. |
| InitialSelection | Contains references to properties, steps, sequences, sequence files, and executions that are selected or active when you start an execution. When the Sequence File window is active, the InitialSelection property contains non-execution versions of the selected objects. When an Execution window is active, the InitialSelection property contains execution versions of the selected steps, properties, and sequences as well as non-execution versions of the selected sequence file. You usually use this property in custom Tools menu commands to operate on the selected objects in a sequence file.Note Whenever you make changes to subproperty values in non-execution versions of a PropertyObject, Step, Sequence, or SequenceFile object the InitialSelection property contains, you modify the non-execution version of the object. TestStand saves the modifications when you save the selected sequence file. Whenever you modify the selected file or the objects it contains from a code module, you must increment the SelectedFile.ChangeCount subproperty of InitialSelection. |
| Report | Report object for the execution. |
| Execution | Execution object in which the sequence invocation runs. |
| Thread | Thread object in which the sequence invocation executes. |
| TestSockets | Container that holds the number of test sockets the user has configured to execute, as well as a test socket index unique to each test socket. |
| SequenceFile | The SequenceFile object for the sequence invocation. Refer to SequenceFile Object Subproperties for the contents of the SequenceFile property. Note TestStand saves any changes you make to property values of a SequenceFile object when you save the sequence file. |
| Sequence | Run-time copy of the Sequence object for the sequence invocation. The Sequence object contains the parameters, local variables, and steps for the sequence. Any changes you make to property values in this object only modify the execution version of the object. Refer to Sequence Object Subproperties for the contents of the Sequence property. Note Built-in properties of sequences are flagged to be shared at run time. Changes to built-in properties within the run-time copy of the sequence also edit the original Sequence object in the sequence file. |
| PreviousStep | Run-time copy of the Step object for the previously executed step in the sequence invocation. The property exists only after the first step in a step group executes. Changes to property values in this object only modify the execution version of the object. Note Built-in properties of steps are flagged to be shared at run time. Changes to built-in properties within the run-time copy of the step also edit the original Step object in the sequence file. |
| Step | Run-time copy of the Step object for the currently executing step. This property does not exist when the execution pauses between steps, for example, at a breakpoint. Changes to property values in this object only modify the execution version of the object. Note Built-in properties of steps are flagged to be shared at run time. Changes to built-in properties within the run-time copy of the step also edit the original Step object in the sequence file. |
| NextStep | Run-time copy of the Step object for the step that follows the currently executing step in the sequence. This property does not exist during and after the execution of the last step in a sequence step group. Changes to property values in this object only modify the execution version of the object. Note Built-in properties of steps are flagged to be shared at run time. Changes to built-in properties within the run-time copy of the step also edit the original Step object in the sequence file. |
| SequenceError | Container that holds the error code, message, and occurred flag to report to the step that calls the sequence. |
| ErrorReported | Indicates whether TestStand sent a BREAK ON RTE message to the user interface for the error the SequenceError property stores. Typically, a user interface launches a Run-Time Error dialog box when it receives a BREAK ON RTE message. When a sequence with an error returns, TestStand transfers the value of ErrorReported to the context of the calling sequence. This prevents the calling sequence from generating a duplicate BREAK ON RTE message for the error the subsequence returns. |
| IsProcessModel | Indicates whether the sequence invocation is a sequence in the process model. |
| Tracing | Indicates whether tracing is active for the sequence invocation. |
| SequenceFailed | Indicates whether the current status of the sequence invocation is Failed. Note Setting this property to True causes the sequence to fail, but the execution does not go to the Cleanup step group when the sequence or the station options specify to immediately go to cleanup on sequence failure. Set the value of RunState.GotoCleanup to True to force a sequence to go to the Cleanup step group. |
| GotoCleanup | Indicates whether the execution proceeds to the Cleanup step group after completing the currently executing step. Note Changes to property values in this object only modify the execution version of the object. |
| StepGroup | Contains the name of the step group—Main, Setup, or Cleanup—the sequence invocation is executing. By modifying the value of this property, you can specify the step group TestStand executes next. Note Changes to property values in this object only modify the execution version of the object. |
| CallStackDepth | Zero-based index of the currently executing sequence in the call stack. For example, when the call stack contains three sequence invocations, CallStackDepth is 2. The sequence call stack includes calls to process model sequences, including calls to entry points. |
| PreviousStepIndex | Zero-based index of the previously executed step in the step group. TestStand sets the property value to -1 before executing the first step in a sequence step group. Note This property exists only for steps other than the first step of each step group. |
| StepIndex | Zero-based index of the currently executing step in the step group. TestStand sets the property value to -1 when the execution is between steps, such as at a breakpoint. |
| NextStepIndex | Zero-based index of the step that follows the currently executing step in the step group. TestStand sets the property value to -1 when executing the last step in a sequence step group. By modifying the value of this property, you can specify the step TestStand executes next. Note Changes you make to this property do not immediately affect the value of the RunState.NextStep property object. |
| LoopIndex | Loop index for the active step in the sequence invocation. By default, steps you configure to loop use this property to store the loop index. The value of the loop index depends on the looping construct you choose to use for the step. |
| NumStepsExecuted | Number of steps that executed in the sequence invocation. |
| LoopNumPassed | Number of iterations a looping step completes with a status of Passed or Done. |
| LoopNumFailed | Number of iterations a looping step completes with a status of Failed. |
| LoopNumIterations | Number of iterations a looping step completes. |
| ProcessModelClient | The SequenceFile object for the client sequence file of the process model. This property exists only for executions you initiate through a process model entry point. Note When you save the sequence file, TestStand saves any changes you make to property values in the SequenceFile object. |
| IsEditor | Indicates whether the current graphical user interface (GUI) is a sequence editor. |

Parent topic:

Sequence Context

Related concepts:

- InitialSelection Subproperties
- Sequence Object Subproperties
- SequenceFile Object Subproperties

<!--NI_TOPIC bundle=teststand path=runstate.html language=enus -->
## TOPIC 00768: RunState.Step and Other Step Objects

- bundle_id: `teststand`
- source_path: `runstate.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/runstate.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: All Step objects include custom properties including a Result subproperty, which contains the Error, Status, and Common subproperties. The sequence context references steps in various locations. The RunState.NextStep, RunState.PreviousStep, and Runstate.Step properties contain run-time copies of the

### RunState.Step and Other Step Objects

All Step objects include custom properties including a Result subproperty, which contains the Error, Status, and Common subproperties.

The sequence context references steps in various locations. The RunState.NextStep, RunState.PreviousStep, and Runstate.Step properties contain run-time copies of the Step object for the steps that are executing next, previously executed, and currently executing, respectively.

The Step objects within the RunState.Sequence property contain a run-time copy of the current sequence invocation. The Step objects within sequences under the RunState.SequenceFile.Data.Seq property contain the edit-time copy of the currently executing sequence file.

All Step objects include custom properties and built-in properties. The Result built-in step property contains the Error, Status, ReportText, and Common subproperties.

Parent topic:

RunState Subproperties

<!--NI_TOPIC bundle=teststand path=search-directories.html language=enus -->
## TOPIC 00769: Search Directories

- bundle_id: `teststand`
- source_path: `search-directories.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/search-directories.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: TestStand includes a list of search directories module adapters use to resolve relative paths of code modules for steps and substeps in step types and to locate code modules when executing steps. TestStand also uses the search directories to resolve relative pathnames for files and directories when

### Search Directories

TestStand includes a list of search directories module adapters use to resolve relative paths of code modules for steps and substeps in step types and to locate code modules when executing steps. TestStand also uses the search directories to resolve relative pathnames for files and directories when calling the TestStand API Engine.FindFileEx and Engine.FindPath methods.

Select Configure»Search Directories in the TestStand Sequence Editor to launch the Edit Search Directories dialog box, in which you can view and edit the default list of search paths. The list of default directories includes specific TestStand directories and Microsoft Windows system directories, and you can add custom directories to the list. Use relative paths when possible to specify file locations. The paths that appear first in the list take precedence over the paths that appear later in the list. You can exclude directories, reorder directories, search subdirectories, and specify file extension restrictions for directories.

TestStand includes the following directories by default, in order of precedence:

- Current sequence file directory
- Current workspace directory
- Application directory (disabled by default)
- <TestStand Public> directory
- <TestStand> directory
- <TestStand>\Bin directory
- Initial working directory (disabled by default)
- Windows system directory
- Windows directory
- PATH environment variable (disabled by default)
- <TestStand Public>\Components directory
- <TestStand><\Components directory

When you list a directory and a subdirectory within that directory, TestStand performs a double search. You might want to use a double search only when both directories contain a file with the same name but different content. In most cases, include only the higher level directory.

If the search directory is non-recursive, TestStand appends the relative path to the search directory path to determine if the file exists. As soon as TestStand finds the file, the search stops.

If the search directory is recursive, TestStand appends the relative path to all the
 subdirectories too. NI recommends using the recursive option sparingly to avoid
 performance issues and to reduce the risk of matching incorrect files with the same
 name.

Parent topic:

Module Adapters

Related concepts:

- Using Substeps
- TestStand Directory Structure
- Configuring Search Directories for Deployment
- Locating the Correct Code Module in 32-bit TestStand and 64-bit TestStand
- Using TestStand Search Directories to Locate the Correct Code Module in 32-bit TestStand and 64-bit TestStand

<!--NI_TOPIC bundle=teststand path=sections-in-xml-report-style-sheets.html language=enus -->
## TOPIC 00770: Sections in XML Report Style Sheets

- bundle_id: `teststand`
- source_path: `sections-in-xml-report-style-sheets.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/sections-in-xml-report-style-sheets.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The TestStand XML report style sheets include a VBScript section, a JavaScript section, and an XSLT section. VBScript Section This section contains one function, GetLocalizedDecimalPoint(), to return the localized decimal point. JavaScript Section This section contains JavaScript functions and varia

### Sections in XML Report Style
 Sheets

The TestStand XML report style
 sheets include a VBScript section, a JavaScript section, and an XSLT
 section.

#### VBScript Section

This section contains
 one function, GetLocalizedDecimalPoint(), to return the localized decimal
 point.

#### JavaScript Section

This section contains
 JavaScript functions and variables that the XSLT code in later sections uses to
 translate the XML document. This section includes the following
 subsections:

#### JavaScript Section 1

This section
 contains the following functions that initialize the global variables and other
 helper functions:

- InitStylesheetPath—Initializes the global path variable, which stores the
 absolute path of the style sheet.
- InitFlagGlobalVariables—Initializes global variables, such as
 gIncludeArrayMeasurement, which acts as a flag to determine how to add array
 data to the XML output.
- (horizontal.xsl) SetColumnSpanConstant—Initializes a global variable for the
 column span of the generated tables.
- (report.xsl) and (expand.xsl) InitColorGlobalVariables—Initializes all color
 global variables.

#### JavaScript Section 2

This section
 contains the following functions to handle localized decimal values:

- SetLocalizedDecimalPoint—Sets the localized decimal point to use for all numeric
 values and stores the localized decimal point in a global variable.
- ReturnLocalizedDecimalVal_Node—Replaces the decimal point in the value node with
 the localized decimal point.

#### JavaScript Section 3

This section
 contains the following functions to handle indentation and block levels for the
 tables in the report:

- SetResultLevel—Sets the depth of the results to process.
- SetBlockLevel—Sets the block level of the results to process.
- GetResultLevel—Returns the depth of the results to process.
- GetBlockLevel—Returns the block level of the results to process.
- InitBlockLevelArray—Creates the BlockLevelArray and initializes the array to 0.
- ProcessCurrentBlockLevel—Processes the block level of the step, adds required
 <blockquote> tags for the current block levels, and closes the HTML table if
 required.
- GetIndentationString—Generates an indentation string based on the block level.
- (report.xsl) and (horizontal.xsl) GetAddTable—Indicates whether you can add a
 table to the report.
- (report.xsl) and (horizontal.xsl) SetAddTable—Specifies whether you can add a
 table to the report.
- (horizontal.xsl) GetStdIndentationString—Returns the string that represents the
 standard indentation.
- (horizontal.xsl) GetInitialIndentation—Returns the initial indentation.

#### JavaScript Section 4

This section
 contains the following functions to insert looping step results in the
 report:

- InitLoopArray—Initializes the global array that stores loop index counts.
- BeginLoopIndices—Stores information to process loop index step results.
- (horizontal.xsl) and (report.xsl) GetLoopIndicesTableEntry—Returns the HTML for
 the Table Row of the Loop Indices button control.
- TestForStartLoopIndex—Opens the <DIV> and increments the loop stack depth
 counter for the first loop step result.
- TestForEndLoopIndex—Closes the <DIV> and decreases the loop stack depth
 counter for the last loop step result.
- InitLoopingInfoArray—Initializes globals information to support looping Sequence
 Call steps.
- StoreCurrentLoopingLevel—Stores information to support looping Sequence Call
 steps.
- RestoreLoopingLevel—Restores information to support looping Sequence Call steps.

#### JavaScript Section 5

This section
 contains the following functions to insert arrays in the report as graph
 objects:

- GraphArray—Creates the graph object to display a graph in the report:
- AddElementToGraph—Adds a new numeric value to the graph.
- GetGraphData—Returns the array that contains the data points on the graph.
- GetArrayGraph—Returns the graph object that corresponds to the input array.
- AddArrayToReportAsGraph—Adds an array to the report as a graph.

#### JavaScript Section 6

This section
 contains the following functions to insert tables in the report:

- (horizontal.xsl) and (report.xsl)BeginTable—Adds a <TABLE> tag to the report.
- (horizontal.xsl) and (report.xsl) EndTable—Adds a </TABLE> tag to the report.
- (horizontal.xsl) AddIndentStartTag—Adds a <BLOCKQUOTE> tag to the report.
- (horizontal.xsl) AddIndentEndTag—Adds a </BLOCKQUOTE> tag to the report.
- IsTableCreationNecessary—Determines if a step in the current block satisfies the
 filtering condition and returns True to indicate that the block requires a new
 table. Use this function in filtering steps for Sequence Call steps.

#### JavaScript Section 7

This section
 contains the following utility functions:

- (report.xsl) and (expand.xsl)GetAbsolutePath—Returns the absolute path to the
 directory that contains the style sheet.
- (report.xsl) and (expand.xsl) GetModuleTime—Returns the module time property.
- (report.xsl) and (expand.xsl) GetFolderPath—Converts all '\' characters in the
 path to '/', removes the filename from the input path, and returns the folder
 path.
- GetTotalTimeInHHMMSSFormat—Adds the total execution time in HHMMSS format to the
 report.
- AddEndingBlockQuotesForCurrentSequence—Adds the </BLOCKQUOTE> tag to the
 report after processing a Sequence Call step.
- GetSerialNumber—Returns the serial number of the input UUT node or returns NONE.
- GetResultId—Returns the result ID.
- GetLoopIndex—Adds the loop index property of the step to the report.
- IsNotFlowControlStep—Returns True if the step is not aFlow Control step.
- GetStepNameAddition—Returns the report text to add to the step name property for
 Flow Control steps.
- RemoveIllegalCharacters—Adds the <br> tag for any newline characters and
 removes the \r character from the text.
- GetLinkURL—Returns the complete file URL or only the filename, depending on
 whether you store absolute or relative paths for the style sheet.
- AddPropertyToReport—Determines whether to add a PropertyObject to the report
 based on the IncludeMeasurement and IncludeLimits report options.
- IsGraphControlInstalled—Determines whether the TSGraphControl2.ocx ActiveX
 control is installed.
- (report.xsl) GetStepBgColor—Returns the background color for the step.

#### (expand.xsl) Javascript Section 8

This
 section contains the following functions to support the expand and collapse
 functionality:

- GetIdFromNode—Creates an ID for the node to use as the ID attribute in the
 resulting HTML document.
- GetId—Calls the GetIdFromNode function to create an ID for the input node.
- GetDIVStyleFromNode—Returns the style value for a <DIV>, depending on the
 step result status.
- GetDIVStyle—Calls the GetDIVStyleFromNode function to determine the style.
- GetStepResultImageFromNode—Returns the <IMG> text for the step result input.
- GetStepResultImage—Calls the GetStepResultImageFromNode function to retrieve the
 IMG text.

#### (expand.xsl) Javascript Section 9

This
 section contains the following table and filtering condition functions:

- (horizontal.xsl) and (report.xsl)BeginTableForSequence—Determines whether to
 create a table for Sequence Call steps.
- (horizontal.xsl) and (report.xsl) EndTableForSequence—Determines whether to add
 a </TABLE> tag for a Sequence Call step.
- IsTableCreatedForSequence—Returns True if a new table is required.
- SetEnableResultFiltering—Sets or resets the report filtering flag.
- CheckIfStepSatisfiesFilteringCondition—Determines whether a step satisfies the
 filtering condition.
- CheckIfStepSatisfiesFilteringCondition_node—Calls the
 CheckIfStepSatisfiesFilteringCondition function to determine whether a step
 satisfies the filtering condition.

#### XSLT Section

This section contains XSLT
 code that transforms XML to HTML. This section includes the following
 subsections:

#### XSLT Section 1

The transformation
 process to convert XML to HTML starts in this section, which initiates the creation
 of the HTML page. From this section, the transformation execution flow branches into
 various templates based on the element or attribute name of the XML tags in the
 report. This section contains the following subsection:

- (report.xsl) and (expand.xsl)XSLT Section 1.1—JavaScript functions to include
 with the generated HTML file to support the expand and collapse functionality.

#### XSLT Section 2

This section contains
 templates that transform a UUT report. This section contains the following
 subsections:

- XSLT Section 2.1—Template that processes UUT <Report> elements. This section
 adds the UUT report header and applies relevant templates that generate the UUT
 report body.
- XSLT Section 2.2—Templates that include XPath expressions to add data to the UUT
 report header, such as BatchSerialNumber, TestSocketIndex, SerialNumber and
 TotalTime.
- XSLT Section 2.3—Template that the TEResult template calls recursively to
 process Sequence Call step results. The generation of the UUT report body begins
 when the transformation process applies this template to the step result that
 corresponds to the Main sequence. This sequence creates a new table, adds
 indentation, and applies the TEResult template to each step result under the
 <ResultList> element.
- XSLT Section 2.4—Template that adds the sequence file path to the header of the
 sequence report table. The header consists of the sequence name and the sequence
 file path where the sequence exists.
- XSLT Section 2.5—Templates that process individual step results, add new rows to
 the report for each step, and add appropriate step result information. This
 section uses specific templates that handle steps with PostResults callbacks,
 looping properties, and Flow Control steps. This section recursively calls the
 ResultList template in XML Section 2.3 to handle Sequence Call steps.
- XSLT Section 2.6—Templates that add the step name and step execution status to
 the report table.
- (horizontal.xsl) XSLT Section 2.7—Template that adds the measurement array of
 Multiple Numeric Limit Test steps to the report.
- XSLT Section 2.8—Template that adds the error message and report text to the
 report table.
- XSLT Section 2.9—Templates that add the interactive execution number to the
 report.
- XSLT Section 2.10—Template that adds server information to the report.
- XSLT Section 2.11—Templates that handle summary information for loops of a
 particular step when looping is enabled for the step or when the user loops or
 runs only selected steps.
- XSLT Section 2.12—Templates that create the critical failure stack table for
 failed tests.
- XSLT Section 2.13—Template that adds the module time to the report.

#### XSLT Section 3

This section contains
 templates that transform a batch report. From this section, the transformation
 execution flow branches into various templates based on the element or attribute
 name of the XML tags in the report. This section contains the following
 subsections:

- XSLT Section 3.1—Template that processes the batch header table and calls the
 template that builds the batch report table.
- XSLT Section 3.2—Template that builds the batch report table.
- XSLT Section 3.3—Template that adds data to the batch report table.

#### XSLT Section 4

This section contains
 templates that templates in XSLT Section 2 and XSLT Section 3 use. This section
 contains the following subsections:

- XSLT Section 4.1—Template that processes the StationID and login name.
- XSLT Section 4.2—Template that processes the StartDate and StartTime of the
 report.

#### XSLT Section 5

This section contains
 templates that insert all flagged information and additional results in the report
 table. This section contains the following subsections:

- XSLT Section 5.1—Templates that process empty cell values, standard indentation,
 and comparison type.
- XSLT Section 5.2—Template that processes the status color configured in the
 report options.
- (expand.xsl) XSLT Section 5.3—Template that processes the status background
 color configured in the report options.
- XSLT Section 5.4—Template that inserts flagged values in the report.
- XSLT Section 5.5—Template that adds values in the report if the flag to include
 it in the report is enabled.
- XSLT Section 5.6—Template that generates a result row to insert in the table.
- XSLT Section 5.7—Template that generates the indentation based on the level.
- XSLT Section 5.8—Template that inserts an array in the report as a table.
- XSLT Section 5.9—Template for the array dimensions.
- XSLT Section 5.10—Template that returns whether the step failure caused the
 sequence to fail.
- (report.xsl) and (expand.xsl) XSLT Section 5.11—Template for the step background
 color configured in the report options.
- (horizontal.xsl) XSLT Section 5.12—Template that removes white spaces from a
 string.
- (horizontal.xsl) XSLT Section 5.13—Template that returns whether the step
 failure caused the sequence to fail from the Step status property.

Parent topic:

XML Report Style Sheets

Related concepts:

- XML Report Style Sheets

<!--NI_TOPIC bundle=teststand path=selecting-a-source-code-control-provider.html language=enus -->
## TOPIC 00771: Selecting a Source Code Control Provider

- bundle_id: `teststand`
- source_path: `selecting-a-source-code-control-provider.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/selecting-a-source-code-control-provider.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Microsoft Source Code Control (MSSCC)-Based ProvidersTestStand supports several third-party source code control (SCC) providers. Available SCC operations in TestStand are the same regardless of the third-party provider you select. Specific support or functionality for each operation varies by provid

### Selecting a Source Code Control Provider

#### Microsoft Source Code Control
 (MSSCC)-Based Providers

TestStand supports several third-party source code control
 (SCC) providers. Available SCC operations in TestStand are the same regardless of the
 third-party provider you select. Specific support or functionality for each operation varies
 by provider.

In some cases, you might decide to use a specific SCC provider because
 your company has standardized on that application. If not, you must decide which provider
 you want to use for managing files. Consult the SCC administrator at your company to find
 out if you must use a specific provider.

After you select and install an SCC provider,
 you must configure TestStand to work with that provider. You can configure a TestStand
 workspace to work with only one SCC provider at a time.

TestStand integrates with any
 32-bit SCC provider that supports the Microsoft Source Code Control Interface. 64-bit
 TestStand supports 32-bit SCC providers only and does not support 64-bit SCC
 providers.

NI supports the following third-party SCC providers with TestStand:

- Helix Core
- SVN (PushOK plugins)

The following third-party SCC providers are allowed but not supported:

- IBM Rational ClearCase
- MKS Source Integrity
- Serena Version Manager (PVCS)
- Microsoft Visual SourceSafe

#### Git-Based Providers

The TestStand Sequence
 Editor supports source code control using Git-based providers through the
 Git pane. You can connect to your Git repositories and perform common
 version control operations using the Git pane, and can also work with local Git repositories
 without using a Git provider. You can use the Git pane to work with any source folder in a
 Git repository without the need to create a TestStand workspace file.

- Microsoft Azure DevOps
- GitHub
- BitBucket

Parent topic:

TestStand Building Blocks

Related concepts:

- Workspaces

Related information:

- Git Pane

<!--NI_TOPIC bundle=teststand path=selecting-where-labwindows-cvi-steps-execute.html language=enus -->
## TOPIC 00772: LabWindows/CVI Step Execution Locations

- bundle_id: `teststand`
- source_path: `selecting-where-labwindows-cvi-steps-execute.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/selecting-where-labwindows-cvi-steps-execute.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the Step Execution section in the LabWindows/CVI Adapter Configuration dialog box to select where steps execute. The LabWindows/CVI Adapter can run code modules in-process or out-of-process, as the following table describes. Where Code Modules Execute Description In-process In the same process a

### LabWindows/CVI Step Execution
 Locations

Use the Step Execution section in the LabWindows/CVI Adapter Configuration dialog box to select
 where steps execute. The LabWindows/CVI Adapter can run code modules in-process or
 out-of-process, as the following table describes.

| Where Code Modules Execute | Description |
| --- | --- |
| In-process | In the same process as the sequence editor or a user interface you are running, without using the LabWindows/CVI development environment. |
| Out-of-process | In an external instance of the LabWindows/CVI development environment. |

The LabWindows/CVI Adapter uses two different copies of the LabWindows/CVI development
 environment. The adapter uses one copy to execute code modules for out-of-process step
 execution. By default, the adapter opens
 <TestStand Public>\AdapterSupport\CVI\tscvirun.prj
 in this copy of LabWindows/CVI. Use this copy of LabWindows/CVI to edit the projects you
 use to create DLLs, static libraries, and object files.

Parent topic:

LabWindows/CVI Adapter

Related concepts:

- Out-of-Process LabWindows/CVI Code Module Execution
- In-Process LabWindows/CVI Code Module Execution
- Search Directories

<!--NI_TOPIC bundle=teststand path=sequence-adapter.html language=enus -->
## TOPIC 00773: Sequence Adapter

- bundle_id: `teststand`
- source_path: `sequence-adapter.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/sequence-adapter.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the Sequence Adapter to pass parameters when you make a call to a subsequence. You can call a subsequence in the current sequence file, in another sequence file, or a sequence file on a remote system. You can also make recursive sequence calls and call sequences asynchronously in a new thread or

### Sequence Adapter

Note

Hidden

When you specify a module for a step, the TestStand Sequence Editor displays the Sequence Module tab and TestStand User Interfaces launch the Edit Sequence Call dialog box.

You can use the Sequence Adapter for a step type that can use any module adapter. Using the Sequence Adapter this way is similar to using the built-in Sequence Call step type, except that the Sequence Call step sets the step status to Passed instead of Done when no failure or error occurs.

After the Sequence Call step executes, the Sequence Adapter can set the step status. If no run-time error occurs, the adapter does not set the step status, which is Done or Passed, depending on the type of step. If the sequence the step calls fails, the adapter sets the step status to Failed. If a run-time error occurs in the sequence, the adapter sets the step status to Error and sets the Result.Error.Occurred property to True. The adapter also sets the Result.Error.Code and Result.Error.Msg properties to the values of these same properties in the subsequence step that generated the run-time error.

Use the Variables pane in the Sequence File window to define parameters for a sequence, including the parameter name, the TestStand data type of the parameter, the default value of the parameter, and whether to pass the argument by value or by reference. You can specify a literal value, pass a variable or property by reference or by value, or use the default value the subsequence defines for the parameter.

Parent topic:

Module Adapters

Related concepts:

- Adapter and Code Module Support for 64-bit TestStand
- CPU Affinity Mask Support for 64-bit TestStand
- Module Adapter Parameter Mapping Guidelines
- Remote Execution in 32-bit TestStand and 64-bit TestStand
- Sequence Call Adapter Support for 64-bit TestStand

Related information:

- Sequence Call Step
- Sequence Adapter Configuration Dialog Box

<!--NI_TOPIC bundle=teststand path=sequence-analyzer-install-utility.html language=enus -->
## TOPIC 00774: Sequence Analyzer Install Utility

- bundle_id: `teststand`
- source_path: `sequence-analyzer-install-utility.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/sequence-analyzer-install-utility.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the command-line Sequence Analyzer Install Utility application, AnalyzerInstallUtil.exe, located in the <TestStand>\Bin directory to automatically install or uninstall custom rules and analysis modules without user interaction from a rules file you create and export to a target computer. Use the

### Sequence Analyzer Install Utility

Use the command-line Sequence Analyzer Install Utility application,
 AnalyzerInstallUtil.exe, located in the
 <TestStand>\Bin
 directory to automatically install or uninstall custom rules and analysis modules
 without user interaction from a rules file you create and export to a target computer.

Use the following syntax to invoke the Sequence Analyzer Install Utility, which adds all
 new and replaces all existing custom rules and analysis modules from the rules file on
 the target computer and shows a list of the items installed:

AnalyzerInstallUtil.exe [-U] [-S] <MyRules.tsarules>

The [-U] option uninstalls from the target computer existing custom
 rules and analysis modules that correspond to items in the rules file. The tool removes
 from the target computer rules with the same rule ID and analysis modules with the same
 path and function as rules and analysis modules in the rules file.

The [-S] option instructs the tool to operate in silent mode and not
 list the items installed or uninstalled.

Parent topic:

Deploying Custom Rules and Analysis Modules

Related concepts:

- Search Directories

<!--NI_TOPIC bundle=teststand path=sequence-call-adapter-support-for-64-bit-test.html language=enus -->
## TOPIC 00775: Sequence Call Adapter Support for 64-bit TestStand

- bundle_id: `teststand`
- source_path: `sequence-call-adapter-support-for-64-bit-test.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/sequence-call-adapter-support-for-64-bit-test.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: When you migrate Sequence Call Adapter steps from 32-bit TestStand to 64-bit TestStand, you typically do not have to provide separate sequence files for each architecture because you can create bitness-independent sequences. However, for sequence files that reside in non-shared search directories, y

### Sequence Call Adapter Support for 64-bit TestStand

When you migrate Sequence Call Adapter steps from 32-bit TestStand to 64-bit TestStand, you typically do not have to provide separate sequence files for each architecture because you can create bitness-independent sequences. However, for sequence files that reside in non-shared search directories, you must move the sequence files to a shared location before migrating, or you must copy the sequence files to the equivalent 64-bit location. The Sequence Call Adapter supports the $(Platform) path macro, and you can use the Engine.Is64Bit property in preconditions to write bitness-conditional code. You can also use the Engine.Is64Bit property in an expression to specify the path to a sequence file.

Additionally, when you migrate from 32-bit TestStand to 64-bit TestStand, you must consider the behavior of the CPU affinity and the remote execution settings for Sequence Call steps.

Parent topic:

Adapter and Code Module Support for 64-bit TestStand

Related concepts:

- Using TestStand Search Directories to Locate the Correct Code Module in 32-bit TestStand and 64-bit TestStand
- Using the $(Platform) Path Macro to Locate the Correct Code Module in 32-bit TestStand and 64-bit TestStand
- CPU Affinity Mask Support for 64-bit TestStand
- Remote Execution in 32-bit TestStand and 64-bit TestStand

<!--NI_TOPIC bundle=teststand path=sequence-context.html language=enus -->
## TOPIC 00776: Sequence Context

- bundle_id: `teststand`
- source_path: `sequence-context.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/sequence-context.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Before executing the steps in a sequence, TestStand creates a run-time copy of the sequence to maintain separate local variable and step property values for each sequence invocation. A sequence context is an object in the TestStand API that represents the execution state of a sequence. For each acti

### Sequence Context

Before executing the steps in a sequence, TestStand creates a run-time copy of the sequence to maintain separate local variable and step property values for each sequence invocation.

A sequence context is an object in the TestStand API that represents the execution state of a sequence. For each active sequence, TestStand maintains a sequence context that contains a reference to the run-time copy of the sequence so you can access all the objects, variables, and properties that relate to the execution of the sequence.

The contents of the sequence context vary depending on the currently executing sequence and step, the location of the active sequence in the call stack, and the identity of the execution in which the active sequence resides. Depending on the current state of execution, sequence context subproperties might not exist. When a property exists, the contents of the property can vary.

The sequence context Step subproperty is an example of a property that depends on the execution state. During execution, the Step property exists only when a step is executing. When execution suspends between steps, the Step property does not exist. When it exists, the contents of the Step property are the contents of the currently executing step.

#### Referring to Subproperties

To refer to a subproperty, use a period to separate the name of the property from the name of the subproperty. For example, refer to the CurrentUser subproperty in the TS subproperty of the StationGlobals property as StationGlobals.TS.CurrentUser.

Parent topic:

Executions

Related concepts:

- Accessing the Sequence Context
- Top-Level Properties
- InitialSelection Subproperties
- Sequence Object Subproperties
- RunState.Step and Other Step Objects
- RunState Subproperties
- SequenceFile Object Subproperties
- Station Globals TS Subproperty

<!--NI_TOPIC bundle=teststand path=sequence-file-converter.html language=enus -->
## TOPIC 00777: Sequence File Converter

- bundle_id: `teststand`
- source_path: `sequence-file-converter.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/sequence-file-converter.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the Sequence File Converter tool to resave sequence files on disk using the current version of TestStand. You can also change the file format to binary, XML, or INI, and you can change the protection setting for the files. You can launch the tool in the following ways: Select Tools»Update Sequen

### Sequence File Converter

Use the Sequence File Converter tool to resave sequence files on disk using the
 current version of TestStand. You can also change the file format to binary, XML, or
 INI, and you can change the protection setting for the files.

You can launch the tool in the following ways:

- Select Tools»Update Sequence Files in the TestStand Sequence Editor or a in full-featured TestStand User Interface.
- (Windows 8.1) Click the NI Launcher tile on the Start screen and select TestStand»Tools»TestStand Sequence File Converter .
- (Windows 10 or 7) Select Start»All Programs»National Instruments»TestStand»Tools»TestStand Sequence File Converter .
- Run <TestStand>\Bin\SequenceFileConverter.exe .

The application window displays a view of the directories and files on disk. You can change the base path of the view by entering a path in the toolbar, by selecting a directory using the Browse button, or by double-clicking on folders in the view.

Use the Edit menu and the context menu to change the file format and protection setting for the files you select in the view. Setting changes made to sequence files in the sequence file converter application are not are written to disk until you select Edit»Apply Changes, click Apply Changes in the toolbar, or select Update Files from the context menu.

#### Command-Line Usage

SequenceFileConverter.exe [-Help] [-Recursive] [-Quiet] [-UpdateVersion] [-Unlock:<PasswordList>] [-Format:<Format>] [-Protect:<Mode>:<Password>] <file or directory path> [-env <environment path>]

#### Example

SequenceFileConverter.exe -Recursive -Unlock:myPass,myOtherPass -Format:Binary -Protect:View:myPass "C:\My Test Directory"

This example shows how to complete the following tasks:

- Unlock all files under "C:\My Test Directory" using either " myPass " or " myOtherPass ".
- Convert unlocked files to binary format.
- Set password protection to prevent viewing of the converted files, using " myPass ".
 
 Note 

 TestStand supports password-protecting sequence files to deter editing and viewing within the sequence editor and user interfaces that use the TestStand User Interface (UI) Controls. The TestStand API limits access to a file protected from viewing but cannot prevent access to the file content during execution. National Instruments does not recommend using passwords as the only way of protecting intellectual property.

#### Command-Line Options

The following list describes all of the available options you can use in the command line for the sequence file converter:

- Help —Launches a dialog box that contains an explanation of the command-line arguments.
- Recursive —Applies changes to files found in directories below the specified directory.
- Quiet —Disables the prompt to confirm conversion and prompts to unlock files.
- UpdateVersion —Saves sequence files with the current version of TestStand even if no other modifications to the file exist.
- Unlock:<PasswordList> —Attempts to unlock files for editing using a comma delimited password list. 
 
 Note 

 This does not remove password protection.
- Format:<Format> —Converts all files to the specified format. Possible values for <Format> are binary, INI, and XML.
- Protect:<Mode>:<Password> —Protects all files with <password> . Possible values for <Mode> are Edit, View, and Disable.
 
 Note 

 The Disable value removes password protection from all files unlocked during conversion.
- env<environment path> —Launches the Sequence File
 Converter tool in the evironment defined by the .tsenv file
 located at the path you specify. Consult Defining an Environment 
 for more information about .tsenv files and Choosing an
 Environment for more information about choosing an evironment with
 the -env command line switch.

Parent topic:

TestStand Tools and Utilities

Related concepts:

- Search Directories
- Defining an Environment
- Choosing an Environment

<!--NI_TOPIC bundle=teststand path=sequence-file-global-variables.html language=enus -->
## TOPIC 00778: Sequence File Global Variables

- bundle_id: `teststand`
- source_path: `sequence-file-global-variables.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/sequence-file-global-variables.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Each sequence file can contain any number of global variables, which you can access from any step or sequence within the sequence file in which you define the global variables. View and edit the global variables on the Variables pane. Use the Value column in the Variables pane to modify string, nume

### Sequence File Global Variables

Each sequence file can contain any number of global variables, which you can access from any step or sequence within the sequence file in which you define the global variables. View and edit the global variables on the Variables pane. Use the Value column in the Variables pane to modify string, numeric, and Boolean values.

Parent topic:

Sequences

<!--NI_TOPIC bundle=teststand path=sequence-file-translators-ex.html language=enus -->
## TOPIC 00779: Sequence File Translators

- bundle_id: `teststand`
- source_path: `sequence-file-translators-ex.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/sequence-file-translators-ex.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Purpose This example demonstrates how to create and use a sequence file translators, which is a DLL that TestStand uses to load sequence files in custom formats. A translator implements a set of required callbacks that TestStand invokes to determine the types of files the translator can open and to

### Sequence File Translators

#### Purpose

This example demonstrates how to create and use a sequence file translators, which is a DLL that TestStand uses to load sequence files in custom formats. A translator implements a set of required callbacks that TestStand invokes to determine the types of files the translator can open and to load a custom file as a TestStand sequence file. You can use translators to open files in custom formats. Once TestStand loads a custom file as a TestStand sequence file, you can operate on the file like any other TestStand sequence file. However, you cannot save changes in the TestStand sequence file back to the original format.

The example directory contains projects for example translators written in LabVIEW, LabWindows/CVI, and Microsoft Visual C++. The examples illustrate translating text and XML files and contain a template project you can use to develop a translator in each development environment. Each example can translate the corresponding text or XML file located in the same directory as the example.

#### Example File
 Location

<TestStand
 Public>\Examples\Fundamentals\Sequence File Translators -
 Examples\SetupExampleTranslators.seq

#### Highlighted Features

Sequence file translators

#### Major API

N/A

#### Prerequisites

Before you attempt to open a file in a custom format, you must install the example translator DLL and support files to the appropriate directories in one of the following ways:

- Automatic Installation (recommended) —Open the SetupExampleTranslators.seq example sequence file and run the MainSequence to select the examples to set up.
- Manual Installation —Complete the following steps to manually move the translator DLL and support files:
  1. Open the TextTranslator or XMLTranslator directory for one of the examples in the <TestStand Public>\Examples\Fundamentals\Sequence File Translators - Examples directory, and copy the translator DLL from the selected directory to the <TestStand Public>\Components\Translators directory.
  2. Copy the NI_ExampleTranslatorTypes.ini type file from the <TestStand Public>\Examples\Fundamentals\Sequence File Translators - Examples directory to the <TestStand Public>\Components\TypePalettes directory.
  3. Copy the FrontPanel.uir and StepType.dll files from the <TestStand Public>\Examples\Fundamentals\Sequence File Translators - Examples\Common directory to the <TestStand Public>\Components\StepTypes\Translators directory.

You must restart the TestStand Sequence Editor so that TestStand can load the example translator DLL.

#### How to Use This Example

To open a file with a custom format, select File»Open to launch the Open File dialog box. The Files of Type control in the Open File dialog box contains the new file extensions the translator supports. Browse to the examples directory that corresponds to the development environment you are using and the custom format for which you installed a translator and select SampleFile.

Note

<TestStand Public>\Components\Translators

Parent topic:

Examples for Fundamentals

Related concepts:

- Sequence File Translators
- TestStand Directory Structure

<!--NI_TOPIC bundle=teststand path=sequence-file-translators.html language=enus -->
## TOPIC 00780: Sequence File Translators

- bundle_id: `teststand`
- source_path: `sequence-file-translators.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/sequence-file-translators.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: TestStand uses custom sequence file translators to load test description files saved in a custom format, such as text or XML. The translator reads the contents of the custom sequence file, translates the content to a TestStand sequence file, and opens the TestStand sequence file in the TestStand Seq

### Sequence File Translators

TestStand uses custom sequence file translators to load test description files saved in a custom format, such as text or XML. The translator reads the contents of the custom sequence file, translates the content to a TestStand sequence file, and opens the TestStand sequence file in the TestStand Sequence Editor or a TestStand User Interface. A custom sequence file translator can use predefined step types to simplify the mapping of common operations the custom file format defines to TestStand steps in sequence files.

Within the sequence editor or user interface, you can perform all typical operations TestStand sequence files support, such as executing and debugging sequences, diffing files, adding custom sequence files to workspaces, and deploying custom sequence files. However, you cannot automatically save changes you make to the sequence file in the sequence editor or user interface back to the custom sequence file format. You must make all changes to the custom sequence file directly.

You can create sequence file translators in various development environments, use versioning schemes with custom files, and deploy translators with TestStand. Refer to the <TestStand Public>\Examples\Fundamentals\Sequence File Translators - Examples directory for example custom sequence files and translators.

Note

#### Sequence File Translator Functions

A
 TestStand sequence file translator DLL must export and implement the following C callback
 functions. When a translator DLL does not export all the callback functions, TestStand does
 not load the DLL.

- CanTranslate
- GetDescription
- GetExtension
- GetFileFormatVersion
- GetFileVersion
- GetTranslatorCount
- IsCurrentFileVersion
- TranslateToSequenceFile

#### Error Handling

Each callback function contains three parameters for error handling—an error code, an error
 string, and the maximum length for the error string. When an error occurs within a callback
 function, set the error code to a non-zero value. When the value you assign is a TestStand
 error code, TestStand uses the standard error code description. The callback function can
 copy additional error details to the standard error message string. However, the callback
 must not exceed the specified number of bytes for the maximum length for the error message.
 TestStand uses the error message string the callback function specifies.

Note

<TestStand
 Public>\Examples\Fundamentals\Sequence File Translators - Examples

Parent topic:

Extending TestStand

Related concepts:

- Creating a Sequence File Translator DLL
- TestStand Directory Structure
- Sequence File Translators
- Deploying TestStand Systems

<!--NI_TOPIC bundle=teststand path=sequence-files.html language=enus -->
## TOPIC 00781: Sequence Files

- bundle_id: `teststand`
- source_path: `sequence-files.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/sequence-files.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: A sequence file (.seq) contains any number of sequences, a set of types the sequence file uses, and any global variables steps and sequences in the file share. TestStand includes the following types of sequence files: Normal sequence files—Most sequence files you create are normal sequence files tha

### Sequence Files

A sequence file (.seq) contains any number of sequences, a set of types the sequence file uses, and any global variables steps and sequences in the file share.

TestStand includes the following types of sequence files:

- Normal sequence files—Most sequence files you create are normal sequence files that include sequences to test UUTs.
- Process model sequence files—Normal sequence files specify that they always use the station process model, a specific process model, or no process model.
- Callback sequence files—TestStand uses callback sequences under specific circumstances. Sequence files can contain sequences that override these callbacks. Usually, an application has one Station callback sequence file and one Front-End callback sequence file.

From within the TestStand Sequence Editor, use the Sequence File Properties dialog box to specify the type of sequence, the sequence file process model settings, and other sequence file properties.

Sequence files contain the type definitions for every step, property, and variable the sequence file contains. Use the Types pane to view and edit the types a sequence file contains.

#### Viewing the Hierarchy of Sequence Calls

Use the Sequence Hierarchy window in the TestStand Sequence Editor to display a graph of the sequence call and callback sequence relationships among sequence files and sequences to more easily visualize, navigate, and maintain test sequences.

#### Comparing and Merging Sequence Files

The TestStand File Diff and Merge utility is a stand-alone application you can use to compare and merge non-type differences between two or three sequence files and compare type differences among two sequence files or type palette files.

#### Password-Protecting Sequence
 Files

TestStand supports password-protecting sequence files to discourage
 editing and viewing within the TestStand Sequence Editor and TestStand User
 Interfaces that use the TestStand User Interface (UI) Controls. The TestStand API
 limits access to a file protected from viewing but cannot prevent access to the file
 content during execution. NI does not recommend using passwords as the only way of
 protecting intellectual property.

#### Analyzing Sequence Files

Use the TestStand Sequence Analyzer in the TestStand Sequence Editor or the stand-alone sequence analyzer application to analyze projects outside of the TestStand Sequence Editor.

Parent topic:

Sequences

Related concepts:

- Sequences
- Normal Sequences
- TestStand Process Models
- Callback Sequences
- Type Concepts
- TestStand UI Controls
- Executing Sequences in Parallel
- Sequence File Global Variables

<!--NI_TOPIC bundle=teststand path=sequence-local-variables.html language=enus -->
## TOPIC 00782: Sequence Local Variables

- bundle_id: `teststand`
- source_path: `sequence-local-variables.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/sequence-local-variables.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use local variables for storing data relevant to the execution of the sequence, such as maintaining counts or holding intermediate values. You can pass local variables by value or by reference to any step in the sequence that calls a subsequence or any step that calls a code module that uses a modul

### Sequence Local Variables

Use local variables for storing data relevant to the execution of the sequence, such as maintaining counts or holding intermediate values. You can pass local variables by value or by reference to any step in the sequence that calls a subsequence or any step that calls a code module that uses a module adapter. You can also access local variables from code modules of steps in the sequence using the TestStand API.

Note

View and edit the local variables in the Variables pane of the Sequence File window. Use the Value column in the Variables pane to modify string, numeric, and Boolean values.

You can create an unlimited number of local variables in a sequence.

Parent topic:

Sequences

Related concepts:

- Variables
- Code Modules
- Module Adapters
- TestStand ActiveX API Overview

<!--NI_TOPIC bundle=teststand path=sequence-object-subproperties.html language=enus -->
## TOPIC 00783: Sequence Object Subproperties

- bundle_id: `teststand`
- source_path: `sequence-object-subproperties.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/sequence-object-subproperties.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Each SequenceFile object in the sequence context contains an array of Sequence objects in the Data.Seq subproperty. The RunState.Sequence subproperty of the sequence context is the Sequence object for the current sequence invocation. The RunState.Sequence subproperty is a run-time copy of the RunSta

### Sequence Object Subproperties

Each SequenceFile object in the sequence context contains an array of Sequence objects in the Data.Seq subproperty. The RunState.Sequence subproperty of the sequence context is the Sequence object for the current sequence invocation. The RunState.Sequence subproperty is a run-time copy of the RunState.SequenceFile.Data.Seq array element for the currently executing sequence.

Each Sequence object in the sequence context contains an array of Step objects for each step group. The RunState.Step subproperty of the sequence context is a Step object in the RunState.SequenceSequence object. The RunState.Step subproperty represents the currently executing step.

| Sequence Context Subproperty | Description |
| --- | --- |
| Parameters | Contains the parameters of the sequence. In the RunState.Sequence object, the parameters contain the values the calling sequence passes. In non-execution instances of Sequence objects, the parameters contain their default values. |
| Locals | Contains the local variables of the sequence. In the RunState.Sequence object, the local variables contain the current values in the sequence invocation. In non-execution instances of Sequence objects, the local variables contain their default values. |
| ResultList | In the RunState.Sequence object, the ResultList local variable contains an array of step results for the sequence invocation. ResultList local variables are empty in non-execution instances of Sequence objects. |
| Main | Contains an array of all Step objects in the Main step group. |
| Setup | Contains an array of all Step objects in the Setup step group. |
| Cleanup | Contains an array of all Step objects in the Cleanup step group. |

Parent topic:

RunState Subproperties

<!--NI_TOPIC bundle=teststand path=sequence-parameters.html language=enus -->
## TOPIC 00784: Sequence Parameters

- bundle_id: `teststand`
- source_path: `sequence-parameters.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/sequence-parameters.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Each sequence includes its own parameters you can use to pass data to a subsequence you call. Using parameters in this way is analogous to wiring data to terminals when you call a subVI in LabVIEW and to passing arguments to a function call in LabWindows/CVI. You can also specify a default value for

### Sequence Parameters

Each sequence includes its own parameters you can use to pass data to a subsequence you call. Using parameters in this way is analogous to wiring data to terminals when you call a subVI in LabVIEW and to passing arguments to a function call in LabWindows/CVI. You can also specify a default value for each parameter.

You can specify the number of parameters and the data type of each parameter. You can select a value to pass to the parameter or use the default value of the parameter. You can pass sequence parameters by value or by reference to any step that calls a subsequence or any step that calls a code module that uses the LabVIEW, LabWindows/CVI, C/C++ DLL, .NET, or ActiveX/COM Adapter. You can also access parameters from code modules of steps in the sequence by using the TestStand API.

View and edit the parameters for a sequence on the Variables pane of the Sequence File window. Use the Value column on the Variables pane to modify string, numeric, and Boolean values.

NI recommends that you carefully analyze use cases and create extensible, parameterized code
 modules when you develop a TestStand system so you can more easily reuse the code
 modules with different parameters for future systems. However, code modules that are
 highly parameterized might be difficult to use and maintain.

Parent topic:

Sequences

Related concepts:

- Module Adapters
- TestStand ActiveX API Overview

<!--NI_TOPIC bundle=teststand path=sequencefile-object-subproperties.html language=enus -->
## TOPIC 00785: SequenceFile Object Subproperties

- bundle_id: `teststand`
- source_path: `sequencefile-object-subproperties.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/sequencefile-object-subproperties.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following sequence context subproperties are SequenceFile objects: RunState.SequenceFile RunState.ProcessModelClient RunState.InitialSelection.SelectedFile When you save the sequence file, TestStand saves any changes you make to property values in a SequenceFile object. Sequence Context Subprope

### SequenceFile Object Subproperties

The following sequence context subproperties are SequenceFile objects:

- RunState.SequenceFile
- RunState.ProcessModelClient
- RunState.InitialSelection.SelectedFile

When you save the sequence file, TestStand saves any changes you make to property values in a SequenceFile object.

| Sequence Context Subproperty | Description |
| --- | --- |
| ChangeCount | The number of changes you have made to the SequenceFile object. You must increment this property whenever you modify other SequenceFile object properties from a code module. The increment indicates to the sequence editor that you have changed the sequence file. |
| LastSavedChangeCount | The value of the ChangeCount property when the sequence editor last saved the sequence file. |
| Data | Contains the sequences and file global variables in the sequence file. |
| Seq | Subproperty of Data. Contains an array of all Sequence objects in the sequence file. |
| File Global Defaults | Subproperty of Data. Contains the default values for the global variables in the sequence file. |
| Requirements | Contains a Links string array subproperty that represents the product and unit requirements the file covers. |
| Path | The absolute pathname of the sequence file. |

Parent topic:

RunState Subproperties

<!--NI_TOPIC bundle=teststand path=sequencefileview-manager.html language=enus -->
## TOPIC 00786: SequenceFileView Manager

- bundle_id: `teststand`
- source_path: `sequencefileview-manager.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/sequencefileview-manager.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The SequenceFileView Manager control performs the following tasks to manage how other visible TestStand User Interface (UI) Controls view and interact with a selected sequence file: Designates a sequence file as the selected sequence file. Tracks which sequence, step group, and steps users select in

### SequenceFileView Manager

The SequenceFileView Manager control performs the following tasks to manage how other visible TestStand User Interface (UI) Controls view and interact with a selected sequence file:

- Designates a sequence file as the selected sequence file.
- Tracks which sequence, step group, and steps users select in the sequence file.
- Tracks which variables or properties users select in the sequence file.
- Displays aspects of the sequence file in the visible TestStand UI Controls to which the SequenceFileView Manager control connects.
- Enables visible TestStand UI Controls to which the SequenceFileView Manager control connects to change the selected file, sequence, step group, and steps.
- Provides editing and saving commands.
- Provides methods for executing the sequence file users select.

An application needs one SequenceFileView Manager control for each location, such as a window, form, or panel, in which you display a sequence file or let users select a sequence file.

Parent topic:

Manager Controls

Related concepts:

- TestStand UI Controls

<!--NI_TOPIC bundle=teststand path=sequences.html language=enus -->
## TOPIC 00787: Sequences

- bundle_id: `teststand`
- source_path: `sequences.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/sequences.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: A sequence contains a series of steps and can consist of the following components: Setup step group Main step group Cleanup step group Sequence local variables Sequence file global variables Sequence parameters Callback sequences The following figure illustrates the structure of a sequence file. Bui

### Sequences

A sequence contains a series of steps and can consist of the following components:

- Setup step group
- Main step group
- Cleanup step group
- Sequence local variables
- Sequence file global variables
- Sequence parameters
- Callback sequences

The following figure illustrates the structure of a sequence file.

[IMAGE alt='image' src='GUID-768BCF45-1C89-45A4-8540-1115A6FE42D5-a5.svg']

#### Built-In Sequence Properties

Sequences include built-in properties you can specify using the Sequence Properties dialog box. For example, you can specify that the flow of execution jumps to the Cleanup step group whenever a step sets the status of the sequence to Failed.

Parent topic:

TestStand Building Blocks

Related concepts:

- Step Groups
- Sequence Local Variables
- Sequence File Global Variables
- Sequence Parameters
- Callback Sequences
- Sequence Files
- Executing Sequences in Parallel

<!--NI_TOPIC bundle=teststand path=sequential-process-model.html language=enus -->
## TOPIC 00788: Sequential Process Model

- bundle_id: `teststand`
- source_path: `sequential-process-model.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/sequential-process-model.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Sequential process model, <TestStand>\Components\Models\TestStandModels\SequentialModel.seq, includes sequences for the following components: Execution entry pointsTest UUTsSingle Pass Configuration entry points Model callbacks Plug-in utility sequences Engine callbacks

### Sequential Process Model

The Sequential process model, <TestStand>\Components\Models\TestStandModels\SequentialModel.seq, includes sequences for the following components:

- Execution entry points
  - Test UUTs
  - Single Pass
- Configuration entry points
- Model callbacks
- Plug-in utility sequences
- Engine callbacks

Parent topic:

Process Model Architecture

Related concepts:

- TestStand Directory Structure
- Execution Entry Points in the Sequential Process Model
- Test UUTs Execution Entry Point in the Sequential Process Model
- Single Pass Execution Entry Point in the Sequential Process Model
- Configuration Entry Points
- Model Callbacks in the Sequential Process Model
- Plug-in Utility Sequences
- Engine Callback

<!--NI_TOPIC bundle=teststand path=session-locking.html language=enus -->
## TOPIC 00789: Session Locking

- bundle_id: `teststand`
- source_path: `session-locking.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/session-locking.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Lock a session before you acquire and use its instrument API handle when you want to prevent another thread or process from simultaneously using the same instrument handle. Use the following methods to implement session locking: InstrSession.GetLockState InstrSession.LockSession InstrSession.UnlockS

### Session Locking

Lock a session before you acquire and use its instrument API handle when you want to prevent another thread or process from simultaneously using the same instrument handle. Use the following methods to implement session locking:

- InstrSession.GetLockState
- InstrSession.LockSession
- InstrSession.UnlockSession
- InstrSessionMgr.GetUniqueKeyName

Session locking is effective only when all components that access the session use the locking functions properly. Locking a session blocks other threads or processes that lock the session before they use it. Locking a session in one component cannot prevent another component that fails to call the locking functions from caching the instrument handle and using the instrument API on that handle. In this way, a session lock is like an operating system critical section or mutex you use to control access to a shared resource.

Unlike an operating system mutex, however, the thread that calls the InstrSession.LockSession method does not own the lock. Instead, the key string you pass to the method owns the lock. Pass the Thread ID or Process ID as the key string to lock on a per-thread or per-process basis. Pass a string that uniquely identifies the object that owns the lock, such as TestFixture1, to lock on an object basis. Pass a key string that you obtain by calling the InstrSessionMgr.GetUniqueKeyName method to lock on an absolute basis.

If you call the InstrSession.LockSession method on a session that is already locked with a different key, the calling thread sleeps until you acquire the lock or until the timeout period you specify expires.

Parent topic:

Session Manager

<!--NI_TOPIC bundle=teststand path=session-manager-ex.html language=enus -->
## TOPIC 00790: Session Manager

- bundle_id: `teststand`
- source_path: `session-manager-ex.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/session-manager-ex.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The <TestStand Public>\Examples\Interfacing with Hardware\Session Manager directory contains the following examples.

### Session Manager

The <TestStand
 Public>\Examples\Interfacing with Hardware\Session
 Manager directory contains the following examples.

- [Session Manager - LabWindows/CVI](session-manager-labwindows-cvi.html)
- [Session Manager - LabVIEW](session-manager-labview.html)

Parent topic:

Examples for Interfacing with Hardware

Related concepts:

- TestStand Directory Structure
- Session Manager Support for 64-bit TestStand

<!--NI_TOPIC bundle=teststand path=session-manager-labview.html language=enus -->
## TOPIC 00791: Session Manager - LabVIEW

- bundle_id: `teststand`
- source_path: `session-manager-labview.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/session-manager-labview.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Purpose This example demonstrates how to use NI Session Manager to share named instrument handles between LabVIEW code modules. Example File Location <TestStand Public>\Examples\Interfacing with Hardware\Session Manager\LabVIEW\Session Manager.seq Highlighted Features IVI NI Session Manager Major AP

### Session Manager - LabVIEW

#### Purpose

This example demonstrates how to use NI Session Manager to share named instrument handles
 between LabVIEW code modules.

#### Example File
 Location

<TestStand
 Public>\Examples\Interfacing with Hardware\Session
 Manager\LabVIEW\Session Manager.seq

#### Highlighted Features

- IVI
- NI Session Manager

#### Major API

None

#### Prerequisites

You must complete the following steps before you can run this example.

1. Ensure that you have the LabVIEW development system installed and you configure the LabVIEW Adapter to use the LabVIEW development system.
2. Install the following software:
  - Measurement & Automation Explorer (MAX)
  - IVI Compliance Package, including the LabVIEW Support portion of the IVI Class
 Drivers
3. Complete the following steps to download and install an IVI-compliant instrument driver for the IVI DMM class that the example can use, such as hp34401a .
  1. Refer to the Instrument Driver Network at ni.com/idnet .
  2. Search for the manufacturer or the type of instrument you want to download. In MAX, the driver installer automatically creates a driver session entry under the Driver Sessions item and populates the software module information under the Instrument Driver Software Module item in the Advanced folder.
4. Complete the following steps to create a logical name for the session.
  1. In MAX, expand the IVI Drivers category.
  2. Right-click the Logical Names item in the configuration tree and select Create New from the context menu.
  3. Complete the configuration panel for the new logical name, which is "SampleDMM" . Logical names are case-sensitive. In the Driver Session control, specify the driver session you downloaded.

#### How to Use This Example

The Get DMM Session step obtains a reference to the session named "SampleDMM", which the Locals.logicalName local variable specifies. When the step creates the session, Session Manager initializes the instrument session and the step stores the reference in the DMM_Reference local variable so the session must continue to exist until the sequence completes.

The remaining steps in the sequence call code modules. Each code module calls Session Manager and obtains the instrument handle for the session the Locals.logicalName local variable specifies. Because the Get DMM Session step ensures that the session exists for the life of the sequence, each module uses the same session and the instrument initializes and closes only once.

Note

Parent topic:

Session Manager

Related concepts:

- TestStand Directory Structure
- Effectively Using LabVIEW with TestStand
- Session Manager Support for 64-bit TestStand

<!--NI_TOPIC bundle=teststand path=session-manager-labwindows-cvi.html language=enus -->
## TOPIC 00792: Session Manager - LabWindows/CVI

- bundle_id: `teststand`
- source_path: `session-manager-labwindows-cvi.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/session-manager-labwindows-cvi.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Purpose This example demonstrates how to use NI Session Manager to share named instrument handles between LabWindows/CVI code modules. Example File Location <TestStand Public>\Examples\Interfacing with Hardware\Session Manager\CVI\Session Manager.seq Highlighted Features IVI NI Session Manager Major

### Session Manager - LabWindows/CVI

#### Purpose

This example demonstrates how to use NI Session Manager to share named instrument handles
 between LabWindows/CVI code modules.

#### Example File
 Location

<TestStand
 Public>\Examples\Interfacing with Hardware\Session
 Manager\CVI\Session Manager.seq

#### Highlighted Features

- IVI
- NI Session Manager

#### Major API

None

#### Prerequisites

You must complete the following steps before you can run this example.

1. Ensure that you have the LabWindows/CVI Run-Time Engine installed and you configure the LabWindows/CVI Adapter to execute steps in-process. If you want to use the Execute Steps in an External Instance of CVI option, you must have the LabWindows/CVI development environment installed.
2. Install the following software:
  - Measurement & Automation Explorer (MAX)
  - IVI Compliance Package
3. Complete the following steps to download and install an IVI-compliant instrument driver for the IVI DMM class that the example can use, such as hp34401a .
  1. Refer to the Instrument Driver Network at ni.com/idnet .
  2. Search for the manufacturer or the type of instrument you want to download. In MAX, the driver installer automatically creates a driver session entry under the Driver Sessions item and populates the software module information under the Instrument Driver Software Module item in the Advanced folder.
4. Complete the following steps to create a logical name for the session.
  1. In MAX, expand the IVI Drivers category.
  2. Right-click the Logical Names item in the configuration tree and select Create New from the context menu.
  3. Complete the configuration panel for the new logical name, "SampleDMM" . Logical names are case-sensitive. In the Driver Session control, specify the driver session you downloaded.

#### How to Use This Example

The Get DMM Session step obtains a reference to the session named "SampleDMM", which the Locals.logicalName local variable specifies. When the step creates the session, Session Manager initializes the instrument session and the step stores the reference in the DMM_Reference local variable so the session must continue to exist until the sequence completes.

The remaining steps in the sequence call code modules. Each code module calls Session Manager and obtains the instrument handle for the session the Locals.logicalName local variable specifies. Because the Get DMM Session step ensures that the session exists for the life of the sequence, each module uses the same session and the instrument initializes and closes only once.

Note

Parent topic:

Session Manager

Related concepts:

- TestStand Directory Structure
- Session Manager Support for 64-bit TestStand

<!--NI_TOPIC bundle=teststand path=session-manager-support-for-64-bit-teststand.html language=enus -->
## TOPIC 00793: Session Manager Support for 64-bit TestStand

- bundle_id: `teststand`
- source_path: `session-manager-support-for-64-bit-teststand.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/session-manager-support-for-64-bit-teststand.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: TestStand installs and registers separate 32-bit NI Session Manager and 64-bit NI Session Manager servers on computers running 64-bit Microsoft Windows, even when you install only 32-bit TestStand. The 64-bit Session Manager works similarly to the 32-bit Session Manager. However, you cannot share se

### Session Manager Support for 64-bit TestStand

TestStand installs and registers separate 32-bit NI Session Manager and 64-bit NI Session Manager servers on computers running 64-bit Microsoft Windows, even when you install only 32-bit TestStand. The 64-bit Session Manager works similarly to the 32-bit Session Manager. However, you cannot share session handles the out-of-process Session Manager creates between 32-bit processes and 64-bit processes because different servers generate the 32-bit session handles and 64-bit session handles. For example, if 64-bit TestStand calls a 32-bit LabVIEW VI, you cannot use session handles created in the LabVIEW VI in 64-bit TestStand or vice versa. Similarly, you cannot share handles between 32-bit TestStand and 64-bit TestStand when one instance of TestStand uses remote execution to invoke the other instance of TestStand.

Parent topic:

64-bit TestStand and Migrating from 32-bit TestStand

<!--NI_TOPIC bundle=teststand path=session-manager.html language=enus -->
## TOPIC 00794: Session Manager

- bundle_id: `teststand`
- source_path: `session-manager.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/session-manager.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use Session Manager to obtain instrument sessions. Session Manager returns a reference to the session object with the name you specify. If the session object you specify does not yet exist, Session Manager creates it and returns a reference to the new session. You can also query the names and catego

### Session Manager

Use Session Manager to obtain instrument sessions.

Session Manager returns a reference to the session object with the name you specify. If the
 session object you specify does not yet exist, Session Manager creates it and returns a
 reference to the new session. You can also query the names and categories of available
 sessions.

Session Manager is a single instance, in-process server that is globally available to all software components in the process.

Various types of modules in an application can use Session Manager to obtain instrument session objects and configuration information, as shown in the following figure.

[IMAGE alt='image' src='GUID-F6716ABB-74DC-470F-857A-A6FBFC710211-a5.gif']

Application modules can also use an instrument session to obtain instrument API handles, as shown in the following figure.

[IMAGE alt='image' src='GUID-78856834-860E-4DE0-993E-EC2A430A9428-a5.gif']

Parent topic:

TestStand Tools and Utilities

<!--NI_TOPIC bundle=teststand path=setting-the-preferred-execution-system-of-lab.html language=enus -->
## TOPIC 00795: Setting the Preferred Execution System of LabVIEW VIs to Prevent Deadlock

- bundle_id: `teststand`
- source_path: `setting-the-preferred-execution-system-of-lab.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/setting-the-preferred-execution-system-of-lab.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: When a VI calls methods of the TestStand API, you must correctly set the Preferred Execution System on the Execution page of the VI Properties dialog box for the VIs. When you call synchronous methods that do not return until the LabVIEW server executes a VI on behalf of TestStand, the VI that calls

### Setting the Preferred Execution System of LabVIEW VIs to Prevent Deadlock

When a VI calls methods of the TestStand API, you must correctly set the Preferred Execution System on the Execution page of the VI Properties dialog box for the VIs.

When you call synchronous methods that do not return until the LabVIEW server executes a VI on behalf of TestStand, the VI that calls these methods and the VI that TestStand attempts to run using the LabVIEW VI Server cannot run in the same LabVIEW execution system. When the VIs attempt to run in the same execution system, the execution of the synchronous TestStand method consumes the execution system in which the VI needs to run, causing deadlock. Since most TestStand API methods are synchronous, you should consider this when calling any TestStand API method from a LabVIEW user interface.

Because LabVIEW handles ActiveX communication through the user interface execution system, you cannot set either of the VIs in this scenario to run in the user interface execution system. For example, you can have a LabVIEW code module that calls the Engine.NewExecution method followed by the Execution.WaitForEndEx method and a new execution that calls LabVIEW code modules. Deadlock can occur when either VI in this scenario uses same as caller or user interface as the preferred execution system.

To avoid deadlock, use the Execution page of the VI Properties dialog box to select a different preferred execution system, such as other 1 or other 2, for each VI.

Parent topic:

Programming with the TestStand API in LabVIEW

<!--NI_TOPIC bundle=teststand path=setting-up-teststand-for-accessing-synchroniz.html language=enus -->
## TOPIC 00796: Setting Up TestStand for Accessing Synchronization Objects Remotely

- bundle_id: `teststand`
- source_path: `setting-up-teststand-for-accessing-synchroniz.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/setting-up-teststand-for-accessing-synchroniz.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: To create and access a synchronization object on another computer, you must configure Microsoft Windows system security on both computers. This help file uses the following terms: Remote computer—The computer that creates the synchronization object. Local computer—The computer that accesses the sync

### Setting Up TestStand for Accessing Synchronization Objects Remotely

To create and access a synchronization object on another computer, you must configure Microsoft Windows system security on both computers. This help file uses the following terms:

- Remote computer —The computer that creates the synchronization object.
- Local computer —The computer that accesses the synchronization object.

#### Setting Windows System Security on the Remote Computer

You must configure the Distributed Component Object Model (DCOM) settings and Microsoft Windows firewall settings on the computer that creates the synchronization object to allow users to access and launch the TestStand TSAutoMgr.exe server remotely.

#### Setting Windows System Security on the Local Computer

You must configure DCOM settings and Windows firewall settings on the computer that accesses the synchronization object remotely.

Parent topic:

Using the Synchronization Step Type

<!--NI_TOPIC bundle=teststand path=setting-windows-system-security-on-a-remote-s.html language=enus -->
## TOPIC 00797: Setting Windows System Security on a Remote Server

- bundle_id: `teststand`
- source_path: `setting-windows-system-security-on-a-remote-s.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/setting-windows-system-security-on-a-remote-s.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: You must configure the Distributed Component Object Model (DCOM) settings and Windows firewall settings to allow users to access and launch the TestStand server remotely.

### Setting Windows System Security on a Remote Server

You must configure the Distributed Component Object Model (DCOM) settings and Windows firewall settings to allow users to access and launch the TestStand server remotely.

Parent topic:

Configuring Remote Executions

Related concepts:

- DCOM Settings for Remote Servers
- Windows Firewall Settings for Remote Servers

<!--NI_TOPIC bundle=teststand path=settings-windows-system-security-on-a-local-c.html language=enus -->
## TOPIC 00798: Settings Windows System Security on a Local Client

- bundle_id: `teststand`
- source_path: `settings-windows-system-security-on-a-local-c.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/settings-windows-system-security-on-a-local-c.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: You must configure DCOM settings and Windows firewall settings on the local client computer when you use the TestStand API on the remote server to access objects on the local client. For example, when you pass a property object as an argument to a sequence running on a TestStand remote server and th

### Settings Windows System Security on a Local Client

You must configure DCOM settings and Windows firewall settings on the local client computer when you use the TestStand API on the remote server to access objects on the local client. For example, when you pass a property object as an argument to a sequence running on a TestStand remote server and that sequence attempts to access subproperties of the parameter, the remote server must be able to access the property object on the client computer.

Parent topic:

Configuring Remote Executions

Related concepts:

- DCOM Settings for a Local Client
- Windows Firewall Settings for the Local Client
- Setting Windows System Security on a Remote Server

<!--NI_TOPIC bundle=teststand path=shutdown-events.html language=enus -->
## TOPIC 00799: Shutdown Events

- bundle_id: `teststand`
- source_path: `shutdown-events.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/shutdown-events.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: TestStand generates the UIMsg_ShutDownComplete or the UIMsg_ShutDownCancelled event after you call the Engine.ShutDown method. This event informs you that the shutdown request has ended.

### Shutdown Events

TestStand generates the UIMsg_ShutDownComplete or the UIMsg_ShutDownCancelled event after you call the Engine.ShutDown method. This event informs you that the shutdown request has ended.

Parent topic:

Handling Specific User Interface Messages

Related concepts:

- Shutting Down the Engine

<!--NI_TOPIC bundle=teststand path=shutting-down-the-engine.html language=enus -->
## TOPIC 00800: Shutting Down the Engine

- bundle_id: `teststand`
- source_path: `shutting-down-the-engine.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/shutting-down-the-engine.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: You shut down the engine just before you exit the application and when you log out the current user. Shutting down the engine is a two-pass process in which you release sequence files and wait for their unload callbacks to complete. NI recommends that you call the ApplicationMgr.Shutdown method to s

### Shutting Down the Engine

You shut down the engine just before you exit the application and when you log out the current user. Shutting down the engine is a two-pass process in which you release sequence files and wait for their unload callbacks to complete.

Note

- NI recommends that you call the ApplicationMgr.Shutdown method to shut down the engine for an
 application you develop with the TestStand User Interface (UI)
 Controls.
- For a .NET user interface, refer to the Additional Considerations for .NET Application to Properly Shutdown TestStand section of the Starting and Shutting Down TestStand from a .NET User Interface topic for more information about properly starting and shutting down TestStand from .NET applications.

#### First Pass

Complete the following tasks in the first pass of this process.

- Unload all sequence files and close all completed executions. The application must release all references to sequence files and executions so TestStand can unload all associated sequence files and run any unload callbacks they include.
- Call the Engine.ShutDown method and pass False for the final parameter.

The first pass ends when you receive the UIMsg_ShutDownComplete or UIMsg_ShutDownCancelled UIMessage. If you receive the UIMsg_ShutDownComplete event, continue with pass two. If you receive the UIMsg_ShutDownCancelled event instead, resume the normal operation of the application. The user can cancel shutdown by clicking Cancel in the Waiting for Execution to Complete Timeout dialog box, which TestStand launches for executions that do not end within their allotted time.

#### Second Pass

Complete the following tasks in the second pass of this process.

- Close all executions TestStand created as a result of the first pass. Release references to all executions and close the windows you used to display them.
- Call the LoginLogout Front-End callback sequence and pass True for the logoutOnly argument.
- When the LoginLogout callback completes and you receive the UIMsg_EndExecution event, call the Engine.ShutDown method again but pass True for the final parameter.

The second pass ends when you receive the UIMsg_ShutDownComplete event. When you receive this event and you are shutting down in preparation to exit the application, the application can safely exit. If you are shutting down because the current user logged out, you can resume normal operation.

Note

Parent topic:

Writing an Application with the TestStand Engine API

Related concepts:

- Starting and Shutting Down TestStand from a .NET User Interface
- User Interface Messages (UIMessages)
- Log in/Log out Execution

<!--NI_TOPIC bundle=teststand path=simultaneously-supporting-32-bit-teststand-an.html language=enus -->
## TOPIC 00801: Simultaneously Supporting 32-bit TestStand and 64-bit TestStand

- bundle_id: `teststand`
- source_path: `simultaneously-supporting-32-bit-teststand-an.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/simultaneously-supporting-32-bit-teststand-an.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: If you need to simultaneously support the 32-bit architecture and the 64-bit architecture, use source only VIs for all LabVIEW code modules. The appropriate LabVIEW development system compiles and adds the compiled VI code to the LabVIEW object cache if the code is not already present in the cache.

### Simultaneously Supporting 32-bit TestStand and 64-bit TestStand

If you need to simultaneously support the 32-bit architecture and the 64-bit architecture, use source only VIs for all LabVIEW code modules. The appropriate LabVIEW development system compiles and adds the compiled VI code to the LabVIEW object cache if the code is not already present in the cache. Subsequent calls use the code in the LabVIEW object cache.

If you are using packed project libraries or VIs that depend on DLLs, complete the following steps to associate the bitness-specific version of the packed project library or VI with a step.

1. Create a win32 subdirectory and an x64 subdirectory in the sequence file directory.
2. Move the bitness-specific version of the packed project library or VI into the appropriate subdirectory.
3. Update the module path to $(Platform)\filename.lvlibp or $(Platform)\filename.vi . 32-bit TestStand converts the path to win32\filename.lvlibp or win32\filename.vi , and 64-bit TestStand converts the path to x64\filename.lvlibp or x64\filename.vi .

Parent topic:

LabVIEW Code Module Support for 64-bit TestStand

<!--NI_TOPIC bundle=teststand path=single-pass-execution-entry-point-in-the-batc.html language=enus -->
## TOPIC 00802: Single Pass Execution Entry Point in the Batch Process Model

- bundle_id: `teststand`
- source_path: `single-pass-execution-entry-point-in-the-batc.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/single-pass-execution-entry-point-in-the-batc.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Single Pass Execution entry point is the sequence the controlling execution runs. Open <TestStand>\Components\Models\TestStandModels\BatchModel.seq in the TestStand Sequence Editor and select the Single Pass sequence on the Sequences pane to examine the Batch process model Single Pass Execution

### Single Pass Execution Entry Point in the Batch Process Model

The Single Pass Execution entry point is the sequence the controlling execution runs.

Open <TestStand>\Components\Models\TestStandModels\BatchModel.seq in the TestStand Sequence Editor and select the Single Pass sequence on the Sequences pane to examine the Batch process model Single Pass Execution entry point, which performs the following significant actions:

1. Calls the Initialize Execution Entry Point plug-in utility sequence.
2. Calls the Initialize ModelData sequence.
3. Calls the Model Plugins – Begin sequence.
4. Calls the ProcessSetup callback.
5. Calls the PreBatchLoop callback.
6. Creates and initializes the test socket executions.
7. Calls the WaitForTestSockets method to wait for and monitor test socket executions until the test sockets reach the Initialize synchronization point.
8. Calls the Add TestSocket Threads to Batch utility sequence.
9. Calls the AllowTestSocketsToContinue method to notify test sockets to continue past the Initialize synchronization point.
10. Calls the WaitForTestSockets method to wait for and monitor test socket executions until the test sockets reach the GetUUTSerialNumber synchronization point.
11. Calls the PreBatch callback.
12. Calls the Model Plugins – Pre Batch sequence.
13. When no more UUTs exist, sets the ContinueTesting test socket data variable to False for all the test sockets and marks all test sockets as enabled to allow currently disabled test sockets to complete execution.
14. Calls the AllowTestSocketsToContinue method to notify test sockets to continue past the GetUUTSerialNumber synchronization point. If no more UUTs exist, skips to .
15. Calls the Model Plugins – Batch Start sequence.
16. Calls the WaitForTestSockets method to wait for and monitor test socket executions until the test sockets reach the ReadyToRun synchronization point.
17. Calls the Tile Execution Windows utility sequence.
18. Calls the AllowTestSocketsToContinue method to notify test sockets to continue past the ReadyToRun synchronization point.
19. Calls the WaitForTestSockets method to wait for and monitor test socket executions until the test sockets reach the PostMainSequence synchronization point. The test sockets do not block at this synchronization point.
20. Calls the Model Plugins – Batch Done sequence
21. Calls the WaitForTestSockets method to wait for and monitor test socket executions until the test sockets reach the ReAddToBatch synchronization point.
22. Calls the Add TestSocket Threads to Batch utility sequence to add test socket execution threads back to the batch specification.
23. Calls the AllowTestSocketsToContinue method to notify test sockets to continue past the ReAddToBatch synchronization point.
24. Calls the WaitForTestSockets utility method to wait for and monitor test socket executions until the test sockets reach the AfterPostUUT synchronization point.
25. Calls the Model Plugins – Post Batch sequence.
26. Calls the PostBatch callback.
27. Calls the AllowTestSocketsToContinue method to notify test sockets to continue
 past the AfterPostUUT synchronization point.
28. Calls the WaitAndCheckExecutionStateForAllTestSockets method to determine the
 first UUT error, if one occurred, and whether any UUTs terminated or aborted.
 Waits for all test socket executions to complete.
29. Calls the PostBatchLoop callback. Performs any cleanup operations related to initialization operations performed in the PreBatch callback here or in the ProcessCleanup callback when the process model skips steps through .
30. Calls the ProcessCleanup callback.
31. Calls the Model Plugins – End sequence. Custom process model plug-ins should perform any cleanup operations related to initialization operations performed in the Model Plugin – PreBatch entry point here when the process model skips steps through .

Parent topic:

Main Execution Entry Points in the Batch Process Model

Related concepts:

- Main Execution Entry Points in the Batch Process Model
- TestStand Directory Structure
- Plug-in Utility Sequences
- Model Plugin – Begin
- Model Callbacks in the Batch Process Model
- Single Pass - Test Socket Entry Point in the Batch Process Model
- Utility Sequences in the Batch Process Model
- Model Plugin – Pre Batch
- Model Plugin – Batch Start
- Model Plugin – Batch Done
- Model Plugin – Post Batch
- Model Plugin – End

<!--NI_TOPIC bundle=teststand path=single-pass-execution-entry-point-in-the-para.html language=enus -->
## TOPIC 00803: Single Pass Execution Entry Point in the Parallel Process Model

- bundle_id: `teststand`
- source_path: `single-pass-execution-entry-point-in-the-para.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/single-pass-execution-entry-point-in-the-para.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Single Pass main Execution entry point is the sequence the controlling execution runs. Open <TestStand>\Components\Models\TestStandModels\ParallelModel.seq in the TestStand Sequence Editor and select the Single Pass sequence on the Sequences pane to examine the Parallel process model Single Pass

### Single Pass Execution Entry Point in the Parallel Process Model

The Single Pass main Execution entry point is the sequence the controlling execution runs.

Open <TestStand>\Components\Models\TestStandModels\ParallelModel.seq in the TestStand Sequence Editor and select the Single Pass sequence on the Sequences pane to examine the Parallel process model Single Pass Execution entry point, which performs the following significant actions:

1. Calls the Initialize Execution Entry Point plug-in utility sequence.
2. Calls the Model Plugins – Begin sequence.
3. Calls the ProcessSetup callback.
4. Calls the Run UUT Info Dialog utility sequence.
5. Creates and initializes the test socket executions.
6. Waits for test socket executions to complete.
7. Calls the ProcessCleanup callback.
8. Calls the Model Plugins – End sequence.

Parent topic:

Main Execution Entry Points in the Parallel Process Model

Related concepts:

- Main Execution Entry Points in the Parallel Process Model
- TestStand Directory Structure
- Plug-in Utility Sequences
- Model Plugin – Begin
- Model Callbacks in the Parallel Process Model
- Utility Sequences in the Parallel Process Model
- Single Pass - Test Socket Execution Entry Point in the Parallel Process Model
- Model Plugin – End

<!--NI_TOPIC bundle=teststand path=single-pass-execution-entry-point-in-the-sequ.html language=enus -->
## TOPIC 00804: Single Pass Execution Entry Point in the Sequential Process Model

- bundle_id: `teststand`
- source_path: `single-pass-execution-entry-point-in-the-sequ.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/single-pass-execution-entry-point-in-the-sequ.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Open <TestStand>\Components\Models\TestStandModels\SequentialModel.seq in the TestStand Sequence Editor and select the Single Pass sequence on the Sequences pane to examine the Sequential process model Single Pass Execution entry point. The Single Pass entry point performs the same actions as the Te

### Single Pass Execution Entry Point in the Sequential Process Model

Open <TestStand>\Components\Models\TestStandModels\SequentialModel.seq in the TestStand Sequence Editor and select the Single Pass sequence on the Sequences pane to examine the Sequential process model Single Pass Execution entry point. The Single Pass entry point performs the same actions as the Test UUTs entry point except that Single Pass does not include a loop for testing multiple UUTs.

Parent topic:

Execution Entry Points in the Sequential Process Model

Related concepts:

- TestStand Directory Structure
- Execution Entry Points in the Sequential Process Model
- Test UUTs Execution Entry Point in the Sequential Process Model

<!--NI_TOPIC bundle=teststand path=single-pass-test-socket-entry-point-execution.html language=enus -->
## TOPIC 00805: Single Pass - Test Socket Execution Entry Point in the Parallel Process Model

- bundle_id: `teststand`
- source_path: `single-pass-test-socket-entry-point-execution.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/single-pass-test-socket-entry-point-execution.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Single Pass – Test Socket Entry Point is the Execution entry point sequence the test socket executions run. The controlling execution creates the test socket executions in the Single Pass Execution entry point sequence. Open <TestStand>\Components\Models\TestStandModels\ParallelModel.seq in the

### Single Pass - Test Socket Execution Entry
 Point in the Parallel Process Model

The Single Pass – Test Socket Entry Point is the Execution entry point sequence the test socket executions run. The controlling execution creates the test socket executions in the Single Pass Execution entry point sequence.

Open <TestStand>\Components\Models\TestStandModels\ParallelModel.seq in the TestStand Sequence Editor and select the Single Pass - Test Socket Entry Point sequence on the Sequences pane to examine the Parallel process model Single Pass - Test Socket Entry Point Execution entry point, which performs the following significant actions:

1. Calls the Initialize Execution Entry Point plug-in utility sequence.
2. Calls the Model Plugins – Begin sequence.
3. Calls the PreUUTLoop callback.
4. Calls the PreUUT callback. When no more UUTs exist, skips to .
5. Calls the Model Plugins – Pre UUT sequence. When no more UUTs exist, skips to .
6. Calls the Model Plugins – UUT Start sequence.
7. Calls the PreMainSequence callback.
8. Calls the MainSequence callback.
9. Calls the PostMainSequence callback.
10. Calls the Model Plugins – UUT Done sequence.
11. Calls the Model Plugins – Post UUT sequence.
12. Calls the PostUUT callback.
13. Calls the PostUUTLoop callback. Performs any cleanup operations related to initialization operations performed in the PreUUT callback here when no UUTs exist and the process model steps through .
14. Calls the Model Plugins – End sequence. Custom process model plug-ins should perform any cleanup operations related to initialization operations performed in the Model Plugin – PreUUT entry point here when no UUTs exist and the process model steps through .

Parent topic:

Hidden Execution Entry Points in the Parallel Process Model

Related concepts:

- Single Pass Execution Entry Point in the Parallel Process Model
- Main Execution Entry Points in the Parallel Process Model
- TestStand Directory Structure
- Plug-in Utility Sequences
- Model Plugin – Begin
- Model Callbacks in the Parallel Process Model
- Model Plugin – Pre UUT
- Model Plugin – UUT Start
- Model Plugin – UUT Done
- Model Plugin – Post UUT
- Model Plugin – End

<!--NI_TOPIC bundle=teststand path=single-window-applications.html language=enus -->
## TOPIC 00806: Single Window Applications

- bundle_id: `teststand`
- source_path: `single-window-applications.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/single-window-applications.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: A single window application typically displays one execution and sequence file at a time. Users can select the execution and sequence file to display from a ListBar, ComboBox, or ListBox control. The examples in the <TestStand>\UserInterfaces\Full-Featured and <TestStand>\UserInterfaces\Simple direc

### Single Window Applications

A single window application typically displays one execution and sequence file at a time. Users can select the execution and sequence file to display from a ListBar, ComboBox, or ListBox control. The examples in the <TestStand>\UserInterfaces\Full-Featured and <TestStand>\UserInterfaces\Simple directories are single window applications.

A single window application contains one Application Manager control, one SequenceFileView Manager control, and one ExecutionView Manager control. To display sequences, connect the SequenceFileView Manager and ExecutionView Manager controls to separate SequenceView controls, alternate a connection from each manager control to a single SequenceView control, or leave one or both manager controls unconnected to a SequenceView control.

In the examples in the Full-Featured directory, the SequenceFileView Manager control and the ExecutionView Manager control connect to separate SequenceView controls, and only one SequenceView control is visible at a time. Visibility depends on whether you select to view sequence files or executions.

In the examples in the Simple directory, the ExecutionView Manager control connects to the SequenceView control. Because the SequenceFileView Manager control does not connect to a SequenceView control, these examples display only sequences for the current execution, not sequences from the sequence file selection.

Parent topic:

User Interface Application Styles

Related concepts:

- TestStand Directory Structure
- Application Manager
- SequenceFileView Manager
- ExecutionView Manager

<!--NI_TOPIC bundle=teststand path=sle-attributes-conditions-specs.html language=enus -->
## TOPIC 00807: SLE Attributes, Conditions, and Specifications

- bundle_id: `teststand`
- source_path: `sle-attributes-conditions-specs.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/sle-attributes-conditions-specs.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Data imported into TestStand is saved in a file global for use in sequences as variables to configure measurement conditions, sweeps, and test limits. SLE Attributes Save SLE Attributes to the SLE_SM_Specifications file global by clicking OK in the SLE Configuration dialog box. The SLE Configuration

### SLE Attributes, Conditions, and
 Specifications

Data imported into TestStand is saved in a file global for use in sequences as variables
 to configure measurement conditions, sweeps, and test limits.

#### SLE
 Attributes

[IMAGE alt='image' src='GUID-37AC2948-5108-49F7-B535-6F9EB30E9D48-a5.png']

Save SLE Attributes to the SLE_SM_Specifications file global
 by clicking OK in the SLE Configuration
 dialog box. The SLE Configuration dialog box utilizes this data
 to support the re-configuration of product specifications.

- APIToken —The SLE API Token set in the
 Connection Configuration view. The value is
 encrypted to the Windows user and machine.
- ProductID —The product ID set in the Product
 Configuration view.
- ServerAddress —The SLE URL set in the Connection
 Configuration view.
- CategoryNames —A list of category names set in the
 Product Configuration view.

#### SLE
 Specification Conditions

The SLE_SM_Specifications
 file global contains the saved conditions for all specifications. They are the first
 properties listed under SLE_SM_Specifications. The type of each
 property matches the expected type of the condition in your specification source,
 and the property names match the names of the conditions in your specification
 source.

[IMAGE alt='image' src='GUID-8D5C97B0-7929-41AD-B4ED-3C7C5F216778-a5.png']

[IMAGE alt='image' src='GUID-11234B81-635C-49C7-A8EC-D0623E1C3222-a5.png']

#### SLE
 Specifications

Specifications are saved as containers under the
 SLE_SM_Specifications file global. The
 Specifications pane uses the specification ID for the name
 of the container since IDs have to be unique in a product. All specification ID
 characters invalid in property names are replaced with underscores. Units are also
 ignored for property names.

- Id —The ID for the product specification defined by the
 user. This is necessary because the container name might not match the
 actual specification ID in SLE.
- Name —The descriptive name of the product specification.
- MeasurementValue —The current measurement for the
 specification. When this property is set in a sequence either through an
 output module parameter or an expression, it will be automatically logged
 along with the conditions.
- Type —The type of specification. Values are either
 Parametric or Functional .
- <Specification Limits> —For parametric
 specifications, all specification limit values are stored after the above
 properties. The limit property names are the following:
  - Min —Minimum acceptable value for the product
 specification during testing.
  - Typical —Typical value for the product
 specification during testing.
  - Max —Maximum acceptable value for the product
 specification during testing.
  - Unit —Measurement unit for the product
 specification.
- <Conditions> —The condition values for the
 specification are stored after the specification limits. The names match the
 names in SLE when possible.

[IMAGE alt='image' src='GUID-F019F09E-1C06-464D-8845-741C0F51DC43-a5.png']

#### Condition Values

A condition value can be a number, a string, an array of
 numbers, an array of strings, or a numeric range.

For single values and array
 values, a property matching the value type is created.

| Numeric Range Format | Description |
| --- | --- |
| [MIN..] | A container is created with Min and Max sub-properties. The Max property is set to INF. |
| [..MAX] | A container is created with Min and Max sub-properties. The Min property is set to INF. |
| [MIN..MAX] | A container is created with Min and Max sub-properties. |
| [MIN..VAL1..MAX] | A container is created with Min, Value1, and Max sub-properties. For intermediate range values, properties with the format Value<Counter> will be created to hold the intermediate values. In this example, the intermediate range value VAL1 will be stored in Value1. |
| [MIN..VAL1..VAL2..] | A container is created with Min, Value1, Value2, and Max sub-properties. The Max property is set to INF. |

Parent topic:

Importing Specifications into TestStand Using the Specifications Pane

Related tasks:

- Exporting Values to an SLE Server from TestStand

<!--NI_TOPIC bundle=teststand path=sp-batch-test-socket-ex-entry-point.html language=enus -->
## TOPIC 00808: Single Pass - Test Socket Entry Point in the Batch Process Model

- bundle_id: `teststand`
- source_path: `sp-batch-test-socket-ex-entry-point.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/sp-batch-test-socket-ex-entry-point.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Single Pass – Test Socket Entry Point is the Execution entry point sequence the test socket executions run. The controlling execution creates the test socket executions in the Single Pass Execution entry point sequence. Open <TestStand>\Components\Models\TestStandModels\BatchModel.seq in the Tes

### Single Pass - Test Socket Entry Point in the Batch Process Model

The Single Pass – Test Socket Entry Point is the Execution entry point sequence the test socket executions run. The controlling execution creates the test socket executions in the Single Pass Execution entry point sequence.

Open <TestStand>\Components\Models\TestStandModels\BatchModel.seq in the TestStand Sequence Editor and select the Single Pass - Test Socket Entry Point sequence on the Sequences pane to examine the Batch process model Single Pass - Test Socket Entry Point Execution entry point, which performs the following significant actions:

1. Calls the Initialize Execution Entry Point plug-in utility sequence.
2. Calls the SyncWithController method to synchronize with the controlling execution at the Initialize synchronization point. The method waits until the controlling execution allows the test socket to continue past the Initialize synchronization point.
3. Calls the Model Plugins – Begin sequence.
4. Calls the PreUUTLoop callback.
5. Calls the SyncWithController method to synchronize with the controlling execution at the GetUUTSerialNumber synchronization point. The method waits until the controlling execution allows the test socket to continue past the GetUUTSerialNumber synchronization point. When no more UUTs exist, skips to .
6. Calls the PreUUT callback. When no more UUTs exist, skips to .
7. Calls the Model Plugins – Pre UUT sequence. When no more UUTs exist, skips to .
8. Calls the Model Plugins – UUT Start sequence.
9. Calls the SyncWithController method to synchronize with the controlling execution at the ReadyToRun synchronization point. The method waits until the controlling execution allows the test socket to continue past the ReadyToRun synchronization point.
10. Calls the PreMainSequence callback.
11. Calls the MainSequence callback.
12. Calls the PostMainSequence callback.
13. Removes the test socket thread from the batch specification in case the MainSequence terminates or the client sequence file does not properly handle batch synchronization. The controlling execution adds the thread to back to the batch specification before continuing past the next synchronization point.
14. Calls the SyncWithController method to synchronize with the controlling execution at the PostMainSequence synchronization point. The method waits until the controlling execution allows the test socket to continue past the PostMainSequence synchronization point.
15. Calls the Model Plugins – UUT Done sequence.
16. Calls the Model Plugins – Post UUT sequence.
17. Calls the SyncWithController method to synchronize with the controlling execution at the ReAddToBatch synchronization point. The method waits until the controlling execution allows the test socket to continue past the ReAddToBatch synchronization point.
18. Calls the PostUUT callback.
19. Calls the SyncWithController method to synchronize with the controlling execution at the AfterPostUUT synchronization point.
20. Calls the PostUUTLoop callback. Performs any cleanup operations related to initialization operations performed in the PreUUT callback here when the process model skips steps through .
21. Calls the Model Plugins – End sequence. Custom process model plug-ins should perform any cleanup operations related to initialization operations performed in the Model Plugin – PreUUT entry point here when the process model skips steps through .

Parent topic:

Hidden Execution Entry Points in the Batch Process Model

Related concepts:

- Single Pass Execution Entry Point in the Batch Process Model
- Main Execution Entry Points in the Batch Process Model
- TestStand Directory Structure
- Plug-in Utility Sequences
- Model Plugin – Begin
- Model Callbacks in the Batch Process Model
- Model Plugin – Pre UUT
- Model Plugin – UUT Start
- Model Callbacks in the Parallel Process Model
- Model Plugin – UUT Done
- Model Plugin – Post UUT
- Model Plugin – End

<!--NI_TOPIC bundle=teststand path=spec-pane.html language=enus -->
## TOPIC 00809: Importing Specifications into TestStand Using the Specifications Pane

- bundle_id: `teststand`
- source_path: `spec-pane.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/spec-pane.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the Specifications pane to connect to SystemLink Enterprise (SLE) Specification Manager or import a specification file and import data to a sequence file as variables. You can use these imported variables when configuring measurement conditions, sweeps, and test limits. If you import data from S

### Importing Specifications into TestStand Using the Specifications Pane

Use the Specifications pane to connect to SystemLink Enterprise
 (SLE) Specification Manager or import a specification file and import data to a sequence
 file as variables. You can use these imported variables when configuring measurement
 conditions, sweeps, and test limits. If you import data from SLE Specification Manager, the
 SLE data plug-in also allows you to pass results tied to imported data back to SLE for
 analysis.

Note

Parent topic:

TestStand Sequence Editor

<!--NI_TOPIC bundle=teststand path=special-considerations-for-a-labview-custom-u.html language=enus -->
## TOPIC 00810: Special Considerations for a LabVIEW Custom User Interface

- bundle_id: `teststand`
- source_path: `special-considerations-for-a-labview-custom-u.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/special-considerations-for-a-labview-custom-u.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Consider the following guidelines when running LabVIEW user interfaces: You must close all running LabVIEW user interfaces before you exit Microsoft Windows. When you shut down, restart, or log off of Windows while a user interface is running, the user interface cancels the operation and might exit

### Special Considerations for a LabVIEW Custom User Interface

Consider the following guidelines when running LabVIEW user interfaces:

- You must close all running LabVIEW user interfaces before you exit Microsoft Windows. When you shut down, restart, or log off of Windows while a user interface is running, the user interface cancels the operation and might exit with an error.
- When you run a LabVIEW user interface in the LabVIEW development system, you can call remote VIs only when the VI is the same or earlier version as the LabVIEW development system. TestStand does not support calling VIs on remote computers when you save a VI without the block diagram and the version of the VI is different than the active version of LabVIEW installed on the computer.
- By default, you can run only one copy of a LabVIEW-built executable at a time, which prevents the TestStand /useexisting command-line option from working. Add the "allowmultipleinstances = TRUE" option to the INI options file in the same directory as the LabVIEW-built executable to allow more than one copy to execute at a time.
- (LabVIEW 2013 SP1 or earlier) A LabVIEW user interface reports object leaks on shutdown when you
 pass a TestStand object as the ActiveXData parameter of a
 UIMessage in the UIMessage callback VI. LabVIEW does not release the object
 reference until LabVIEW unloads the callback VI. Visit
 ni.com/info and enter the Info Code
 4H6DULT3 to access the NI KnowledgeBase article
 PropertyObjects Were Not Released Warning When Using LabVIEW for more
 information about using a dynamically called VI to ensure that LabVIEW releases
 the object.
- To prevent a LabVIEW user interface from hanging while running in LabVIEW, do not call subroutine VIs from inside a VI used as an ActiveX callback VI. Instead, change the execution priority of the VIs to a value other than subroutine.

Parent topic:

Using TestStand UI Controls in LabVIEW

Related concepts:

- Calling VIs on Remote Computers

<!--NI_TOPIC bundle=teststand path=special-considerations-for-using-labview-with.html language=enus -->
## TOPIC 00811: Special Considerations for Using LabVIEW with TestStand Systems

- bundle_id: `teststand`
- source_path: `special-considerations-for-using-labview-with.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/special-considerations-for-using-labview-with.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Learn the recommendations and restrictions for using LabVIEW components with TestStand. You might need to complete additional work to ensure that the LabVIEW and TestStand components interoperate correctly.

### Special Considerations for Using LabVIEW with TestStand Systems

Learn the recommendations and restrictions for using LabVIEW components with TestStand. You might
 need to complete additional work to ensure that the LabVIEW and TestStand components
 interoperate correctly.

Parent topic:

Effectively Using LabVIEW with TestStand

Related concepts:

- Managing Memory Allocation for Large LabVIEW Data Sets

<!--NI_TOPIC bundle=teststand path=special-constant-values.html language=enus -->
## TOPIC 00812: Special Constant Values

- bundle_id: `teststand`
- source_path: `special-constant-values.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/special-constant-values.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: TestStand declares a number of constant values. Some values, like the keywords True and False, are similar to values used in other environments. Other values are used less often. The following table lists all known constant definitions and their common uses. TestStand is not case sensitive for const

### Special Constant Values

TestStand declares a number of
 constant values. Some values, like the keywords True and
 False, are similar to values used in other environments. Other
 values are used less often. The following table lists all known constant definitions
 and their common uses.

Note

true

True

TRUE

| Constant | Definition | Use |
| --- | --- | --- |
| 1.23e-4 | Floating Point Constant | Range approximately 1.7E-308 to 1.7E+308 with 15 significant digits. Note The Use Localized Decimal Point option on the Localization tab of the Station Options dialog box and your operating system settings determine the decimal point character you use in a floating point number. |
| 1234, 0xFFFF, 0b1011 | 32-bit Integer Constant | Range -2147483648 to 4294967295. TestStand supports hexadecimal and binary formats with this type of constant with the use of the 0x and 0b prefixes. TestStand treats hexadecimal and binary versions of these constants as unsigned values with a range of 0 to 4294967295. TestStand converts and represents these constants internally as double-precision, floating-point numbers. |
| 1234i64, 0xFFFFi64, 0b1011i64 | 64-bit Signed Integer Constant | Range -9223372036854775808i64 to 9223372036854775807i64. TestStand supports hexadecimal and binary formats with this type of constant with the use of the 0x and 0b prefixes. However, if the high order bit is set, TestStand interprets the constant as a negative value. |
| 1234ui64, 0xFFFFui64, 0b1011ui64 | 64-bit Unsigned Integer Constant | Range 0ui64 to 18446744073709551615ui64. TestStand supports hexadecimal and binary formats with this type of constant with the use of the 0x and 0b prefixes. |
| True/False | Boolean Constant | True or False. |
| "1234wxyz" | String Constant | Refer to Special String Characters for more information. |
| @"C:\\Windows\\temp" | Unescaped String Constant | Add an @ before the enclosed quotes to turn a string constant into an unescaped string constant. Unlike for regular string constants, backslashes are left as is instead of specifying an escape sequence. Use "" for " within an unescaped string constant. |
| Nothing | Object Reference Constant | You can determine whether an object reference refers to an object by comparing the reference to Nothing. You can release the object to which an object reference refers by setting the value of the reference to Nothing in an expression. TestStand handles the garbage collection of references set equal to Nothing when it retrieves all memory that has gone out of scope. This reference is the equivalent of Nothing in Microsoft Visual Basic .NET, null in C# .NET, or NULL in LabWindows/CVI and Microsoft Visual C++. |
| PI | PI Constant (3.141592...) | The ratio of the circumference of a circle to its diameter. |
| NAN | Not a Number | A numeric value that is not a valid number. The value is equivalent to a quiet NaN value. TestStand also displays NAN for signaling NaN values. IND is a special kind of quiet NaN value. Note TestStand treats NAN and IND as equivalent in expression comparisons. |
| IND | Indeterminate Number | A numeric value that is indeterminate. The value is equivalent to a special kind of quiet NaN value. Some numeric operations, such as Sqrt(-1), will result in an indeterminate value. Note TestStand treats NAN and IND as equivalent in expression comparisons. |
| INF | Infinite Number | A numeric value that is infinite or negative infinite. Equivalent to an INF value in Visual C++. |

Note

Parent topic:

Expressions

<!--NI_TOPIC bundle=teststand path=special-string-characters.html language=enus -->
## TOPIC 00813: Special String Characters

- bundle_id: `teststand`
- source_path: `special-string-characters.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/special-string-characters.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: When located within the quotes of a string, the following characters are considered known escape sequences. The following table describes how TestStand interprets these characters. 8 Special String Characters String Character Interpretation in String \\ Backslash \n Line feed \r Carriage return \xNN

### Special String Characters

When located within the quotes of a string, the following characters are considered known escape sequences. The following table describes how TestStand interprets these characters.

| String Character | Interpretation in String |
| --- | --- |
| \\\\ | Backslash |
| \\n | Line feed |
| \\r | Carriage return |
| \\xNN | Hexadecimal character code |
| \\NN | LabVIEW-style hexadecimal character codeValid only for uncompressed binary data. |
| \\" | Quote |
| \\t | Tab |

Note

- Always enclose strings in quotes.
- String literals in TestStand expressions use a backslash as the escape character, similar to other programming languages like C/C++ and C#. Therefore, if you specify a path using a string literal in an expression, such as for the parameter value of a code module, you must use two backslash characters for each actual backslash the string value requires because TestStand interprets the first backslash character as escaping the character after it. If the character after the first backslash has a special meaning, such as \n (new line) or \t (tab), TestStand replaces the backslash character and the character which follows it with the corresponding special character code. However, if you are storing a path directly in a string variable programmatically or by using the Variables view, use one backslash character per actual backslash because, unlike string literals in expressions, the value of a string variable is not considered escaped and TestStand does not interpret the backslash characters in such strings as having any special meaning.

Parent topic:

Expressions

<!--NI_TOPIC bundle=teststand path=specify-report-file-path-by-expression.html language=enus -->
## TOPIC 00814: Specify Report File Path by Expression

- bundle_id: `teststand`
- source_path: `specify-report-file-path-by-expression.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/specify-report-file-path-by-expression.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: To specify an expression that generates the report file path during execution, select Specify Report File Path by Expression from the File/Directory Options ring control on the Report File Pathname tab of the Report Options dialog box. When you select this option, the expression controls become visi

### Specify Report File Path by Expression

To specify an expression that generates the report file path during execution, select Specify Report File Path by Expression from the File/Directory Options ring control on the Report File Pathname tab of the Report Options dialog box. When you select this option, the expression controls become visible depending on the process model you use. If you are using the Sequential or Parallel process model, or if you are using the Batch process model and you select ATML Report Document as the report format, only the Report File Path expression control is visible. If you are using the Batch process model and you select a report format other than ATML Report Document, both the Report File Path and Batch Report File Path expression controls are visible.

For example, to store an XML report file in the C:\Temp\Reports directory with the filename stored in a variable FileGlobals.ReportFileName in the current process model, use the expression "C:\\Temp\\Reports\\" + FileGlobals.ReportFileName + ".xml".

Note

- $(Batch) —Replaces the macro with the batch serial number. The $(Batch) macro creates new Batch Report files for each serial number in the batch. 
 
 Note 

 You can use the $(Batch) macro only with the Batch process model.
- $(ClientFileDir) —Replaces the macro with the directory that contains the client sequence file. For example, if you execute the client sequence saved as c:\Tests\TestSequences\TestSequence1.seq using an Execution entry point, $(ClientFileDir) specifies the c:\Tests\TestSequences directory.
 
 Note 

 If you use the $(ClientFileDir) macro without saving the sequence file to disk, the macro evaluates to the <TestStand>\Temp directory.
- $(ClientFileName) —Replaces the macro with the name of the client sequence file. For example, if you execute the client sequence file saved as c:\Tests\TestSequences\TestSequence1.seq using an Execution entry point, the $(ClientFileName) macro evaluates to the string "TestSequence1" .
 
 Note 

 If you use the $(ClientFileName) macro without saving the sequence file to disk, the report generator replaces the macro with the string "Unsaved Sequence File". You can modify the string by changing the ModelStrings.ini language file.
- $(Desktop) —Replaces the macro with the directory path of the desktop.
- $(FileExtension) —Replaces the macro with a file format extension that corresponds to the report format you specify on the Contents tab of the Report Options dialog box. For example, if you specify the report file format as HTML, the process model replaces the macro with the string "html" .
- $(FileDate) —Replaces the macro with a string containing the current date in localized format when the report is first saved.
- $(FileDay) —Replaces the macro with a string containing the numeric day of the month when the report is first saved.
- $(FileMonth) —Replaces the macro with a string containing the numeric month when the report is first saved.
- $(FileTime) —Replaces the macro with a string containing the current time in localized format when the report is first saved.
- $(FileYear) —Replaces the macro with a string containing the numeric year when the report is first saved.
- $(PublicDocumentsDir) —Replaces the macro with the file system directory that contains documents common to all users. A typical path is C:\Users\Public\Documents on Microsoft Windows 10/8.1/7.
- $(StationID) —Replaces the macro with the station ID.
- $(TempDir) —Replaces the macro with the <TestStandTemp> directory.
- $(TestSocket) —Replaces the macro with TestSocketIndex during run time. This macro creates new report files for each test socket.
 
 Note 

 The $(TestSocket) macro is invalid in the Batch Report File Path expression.
- $(TestStandExecutableDir) —Replaces the macro with the directory of the TestStand executable. For example, if you are using the TestStand Sequence Editor, the <TestStand>\Bin directory path replaces this macro.
- $(TestStandPublicDir) —Replaces the macro with the <TestStand Public> directory, in which TestStand stores publicly editable files.
- $(Unique) —Replaces the macro with a unique numeric value if the file already exists in the path. If you use more than one $(Unique) macro in the Report File Path expression, TestStand replaces only the first instance from left with the unique numerical value. For example, if you specify the Report File Path expression as "C:\\Temp$(Unique)\\TSReports$(Unique)\\Report$(Unique).xml" and C:\\Temp\\TSReports\\Report.xml already exists, the process model saves the report file path at C:\Temp0001\Reports\Report.xml .
 
 Note 

 You cannot use the $(Unique) macro as a stand-alone directory or filename in the Report File Path or the Batch Report File Path expression.
- $(UserDocumentsDir) —Replaces the macro with the My Documents desktop item.
- $(UserName) —Replaces the macro with the user name of the currently logged in user. 
 
 Note 

 If no user is currently logged in, an empty string replaces the $(UserName) macro.
- $(UUT) —Replaces the macro with the UUT serial number. This macro creates new UUT report files for each UUT. 
 
 Note 
If you use the $(UUT) macro and the UUT serial number is the same for two different UUT loops, the new report file might overwrite the older report file when the Append if File Already Exists option on the Contents tab is disabled. To avoid overwriting the file, use the $(Unique), $(FileTime), or $(FileDate) macros, or enable the Append if File Already Exists option.
The $(UUT) macro is invalid in the Batch Report File Path expression.
- $(UUTStatus) —Replaces the macro with the UUT status during run time. When you use the $(UUTStatus) macro, TestStand creates separate files for each UUT status. If the UUT Report File Path expression contains the $(UUTStatus) and $(UUT) macros, TestStand creates new UUT report files for each UUT status. If the UUT Report File Path expression contains the $(UUTStatus) and $(TestSocket) macros when using the Parallel or Batch process model, for each test socket index, TestStand creates separate files for each UUT status. If the UUT Report File Path expression contains the $(UUTStatus) and $(Batch) macros, for each batch serial number, TestStand creates separate files for each UUT status.
 
 Note 
If you use on-the-fly (OTF) reporting with the $(UUTStatus) macro in the Report File Path expression, the process model creates the temporary file used during OTF reporting in the <TestStand>\Temp directory. The process model copies the temporary file to the correct location when the execution completes.
If you use the $(UUTStatus) macro in the Report File Path expression and execute the sequence file using the Test UUTs Execution entry point, TestStand displays only the complete report for the last UUT status at the end of the execution.
The $(UUTStatus) macro is invalid in the Batch Report File Path expression.
- $(UUTPartNum) —Specifies the UUT part number.
 
 Note 
If you use the $(UUTPartNum) macro and the UUT part number is the same for two different UUT loops, the new report file might overwrite the older report file when the Append if File Already Exists option on the Contents tab is disabled. To avoid overwriting the file, use the $(Unique), $(FileTime), or $(FileDate) macros, or enable the Append if File Already Exists option.
The $(UUTPartNum) macro is invalid in the Batch Report File Path expression control.

#### Processing Report and Batch Report File Path Expressions

The process model generates the report and batch report file paths by evaluating the Report and Batch Report File Path expressions and then replacing the macros. Since the expression is evaluated first, you can also define macros in variables. When you use the Sequential model, TestStand evaluates all Report File Path expressions in the context of the entry point sequence at run time. When you use the Batch or Parallel process model, TestStand evaluates all Report File Path expressions in the context of the test socket Execution entry point sequence at run time. For example, if you execute the sequence file in the Batch process model using the Test UUTs Execution entry point, the process model evaluates all Report File Path expressions in the context of the Test UUTs - Test Socket Entry Point sequence.

The Report File Path and Batch Report File Path expression controls use the context of the first Execution entry point in the current process model to perform syntax checking on the expressions. The Report Options dialog box stores the Report File Path expression separately for each process model. Therefore, you might see different Report File Path expressions when you switch to a different process model.

Note

- Because the Report File Path is an expression, a " / " precedes all escape characters.
- The static text box in the Report Options dialog box shows the evaluated report file path as you edit the expression. The static text box does not evaluate or replace the $(UUTStatus) , $(UUT) , $(TestSocket) , and $(Batch) macros.
- If the output format of the report is an ATML report, report generation will always create a new file for each UUT regardless of Report File Path expression. The ATML report format does not support multiple UUT reports in one file.

The process model determines the report file path at different points during the execution of the process model depending on the macro you use, according to the following guidelines:

- If the Report File Path expression contains the $(UUT) macro, the report generator determines the report file path before calling the MainSequence callback sequence for each UUT.
- If the Report File Path expression contains the $(UUTPartNum) macro, the report generator determines the report file path before calling the MainSequence callback sequence for each UUT.
- If the Report File Path expression contains the $(TestSocket) macro, the report generator determines the report file path before calling the MainSequence callback for the first UUT in the test socket.
- If the Report File Path expression contains the $(Batch) macro, the report generator determines the report file path before calling the MainSequence callback for the first UUT in the batch.
- If the Report File Path expression contains the $(UUTStatus) macro, the report generator determines the report file path after calling the MainSequence callback. The $(UUTStatus) macro causes the process model to group UUT reports into different files according to their status. For example, if a Report File Path expression contains the $(UUTStatus) and $(TestSocket) macros, the process model stores all the PASSED UUT results for a given test socket in one file and stores all FAILED UUT results for a given test socket in another file. The process model keeps track of the UUT files generated for each UUT status and appends them as necessary. The following example illustrates the recommended usage of the $(UUTStatus) macro for process models.
  - Sequential model —Use the $(UUTStatus) macro in the Report File Path expression to generate report files containing UUT reports for UUTs with the same UUT status in the same file. For example, to obtain all PASSED results in the file path " C:\TestStandReports\Report_Passed.xml " and FAILED results in the file path " C:\TestStandReports\Report_Failed.xml ", use the expression "C:\\TestStandReports\\Report_$(UUTStatus).xml" as the report file path.
  - Parallel model —Use the $(UUTStatus) and $(TestSocket) macros in the Report File Path expression to generate report files containing UUT reports of UUTs with the same UUT status in the same file for each test socket. For example, to obtain for each test socket all PASSED results of test socket index 1 in the file path C:\TestStandReports\TestSocketIndex_1\Report_Passed.xml , all FAILED results of test socket index 1 in the file path " C:\TestStandReports\\TestSocketNo_1\Report_Failed.xml ", and so on, use the expression "C:\\TestStandReports\\TestSocketIndex_$(TestSocket)\\Report_$(UUTStatus).xml" as the report file path.
  - Batch Model —Use the $(UUTStatus) and $(Batch) macros in the Report File Path expression to group all UUT reports within the batch that have similar UUT status into one UUT Report file. For example, to obtain for each batch all PASSED results of a batch with batch number 'abc' in the file path " C:\TestStandReports\Batch_abc\Report_Passed.xml ", all FAILED results of a batch with batch number 'abc' in the file path " C:\TestStandReports\Batch_abc\Report_Failed.xml ", and so on, use the expression "C:\TestStandReports\Batch_$(Batch)\Report_$(UUTStatus).xml" as the report file path.

Parent topic:

Customizing Reports with Expressions

Related concepts:

- Search Directories
- Expressions

Related information:

- Report Options Dialog Box

<!--NI_TOPIC bundle=teststand path=specifying-an-empty-array.html language=enus -->
## TOPIC 00815: Specifying an Empty Array

- bundle_id: `teststand`
- source_path: `specifying-an-empty-array.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/specifying-an-empty-array.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Defining an initially empty array is useful when you do not know the maximum array size the sequence requires during execution and when you want to save memory during the periods of execution when the sequence does not use the array. Enable the Empty option in the Array Bounds dialog box when you wa

### Specifying an Empty Array

Defining an initially empty array is useful when you do not know the maximum array size the sequence requires during execution and when you want to save memory during the periods of execution when the sequence does not use the array. Enable the Empty option in the Array Bounds dialog box when you want the array to be initially empty. When you enable this option, the Upper Bounds control for each dimension dims.

You must use the TestStand API to both resize and insert elements into empty arrays.

Parent topic:

Specifying Array Sizes

Related concepts:

- Dynamic Array Sizing

<!--NI_TOPIC bundle=teststand path=specifying-and-changing-control-connections.html language=enus -->
## TOPIC 00816: Specifying and Changing Control Connections

- bundle_id: `teststand`
- source_path: `specifying-and-changing-control-connections.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/specifying-and-changing-control-connections.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: An application typically establishes control connections after loading the window that contains the controls to connect, but the application can establish or change control connections at any time. You can make the same connection from a manager control to multiple visible controls. For example, whe

### Specifying and Changing Control Connections

An application typically establishes control connections after loading the window that contains the controls to connect, but the application can establish or change control connections at any time.

You can make the same connection from a manager control to multiple visible controls. For example, when you connect two combo boxes to the sequence list of a SequenceFileView Manager control, both combo boxes display the selected sequence in the current file. When the selection in one combo box changes, the other combo box updates to show the new selection. However, a visible control or a connectable element of a visible control, such as a ListBar page or a StatusBar pane, can have only one connection of a particular type.

When you connect a manager control to a visible control that has an existing connection, the new connection replaces the existing connection.

Parent topic:

Connecting Manager Controls to Visible Controls

Related concepts:

- Manager Controls
- Visible Controls
- SequenceFileView Manager

<!--NI_TOPIC bundle=teststand path=specifying-array-sizes.html language=enus -->
## TOPIC 00817: Specifying Array Sizes

- bundle_id: `teststand`
- source_path: `specifying-array-sizes.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/specifying-array-sizes.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: In the context menu of each window or pane in which you can insert a variable, parameter, or property, select Insert<item>»Array of»<data type> to insert an array. When you insert an array, the TestStand Sequence Editor launches the Array Bounds dialog box, in which you can set and modify the array

### Specifying Array Sizes

In the context menu of each window or pane in which you can insert a variable, parameter, or property, select Insert<item>»Array of»<data type> to insert an array. When you insert an array, the TestStand Sequence Editor launches the Array Bounds dialog box, in which you can set and modify the array bounds. The following figure shows the settings for a three-dimensional array.

[IMAGE alt='image' src='GUID-5B0E625A-A89D-4DE4-8691-2187D85E3956-a5.png']

The first and outermost dimension contains five elements, with 0 as the minimum index and 4 as the maximum index. The second dimension contains 10 elements, with 1 as the minimum index and 10 as the maximum index. The third and innermost dimension contains three elements, with –1 as the minimum index and 1 as the maximum index.

After you create the variable, parameter, or property as an array, you can modify the array bounds by clicking the Resize Array button in the Name column of the list view to launch the Array Bounds dialog box.

Parent topic:

Creating Instances of Data Types

<!--NI_TOPIC bundle=teststand path=specifying-process-model-files.html language=enus -->
## TOPIC 00818: Specifying Process Model Files

- bundle_id: `teststand`
- source_path: `specifying-process-model-files.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/specifying-process-model-files.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The station process model file is the process model file TestStand uses for all sequence files on the current test station. The Sequential model is the default station model file. Use the Station Options dialog box to select a different station model file and to specify whether individual sequence f

### Specifying Process Model Files

The station process model file is the process model file TestStand uses for all sequence files on the current test station.

The Sequential model is the default station model file. Use the Station Options dialog box to select a different station model file and to specify whether individual sequence files can use their own process model files.

When you allow individual sequence files to specify their own process model files, use the Sequence File Properties dialog box to specify the process model file for the sequence file. You can also specify that a sequence file does not use a process model.

Parent topic:

Process Models

<!--NI_TOPIC bundle=teststand path=specifying-string-buffer-size-in-a-type-libra.html language=enus -->
## TOPIC 00819: Specifying String Buffer Size in a Type Library

- bundle_id: `teststand`
- source_path: `specifying-string-buffer-size-in-a-type-libra.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/specifying-string-buffer-size-in-a-type-libra.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Complete the following steps to embed string buffer size information in a type library in LabWindows/CVI so that TestStand automatically specifies the correct string buffer size for a string parameter. In LabWindows/CVI, open a function panel (.fp) file. In the Function Tree Editor, select the funct

### Specifying String Buffer Size in a Type Library

Complete the following steps to embed string buffer size information in a type library in LabWindows/CVI so that TestStand automatically specifies the correct string buffer size for a string parameter.

1. In LabWindows/CVI, open a function panel ( .fp ) file.
2. In the Function Tree Editor, select the function panel window that corresponds to the function you want to edit and select Edit»Edit Function Panel Window to launch the Function Panel Editor.
3. Complete the following steps to create a data type for the parameter. You must complete these steps only once for each .fp file.
  1. Select Options»Data Types to launch the Edit Data Type List dialog box.
  2. Enter char [1024] in the Type control and click Add .
  3. Click Done to close the Edit Data Type List dialog box.
4. On the function panel, select the control for the string parameter and select Edit»Edit Control to launch the Edit Input Control dialog box.
5. Select char [1024] from the Data type control and click OK to close the Edit Input Control dialog box.
6. Save the changes to the function panel file.
7. Select Build»Create Debuggable Dynamic Link Library to rebuild the DLL. Click OK when LabWindows/CVI prompts you that the files are created.

Parent topic:

Adding Type Libraries to LabWindows/CVI DLLs

Related concepts:

- Adding Type Libraries to LabWindows/CVI DLLs
- Generating Type Library Information to Include in a DLL

<!--NI_TOPIC bundle=teststand path=specifying-the-configuration-file-location.html language=enus -->
## TOPIC 00820: Specifying the Configuration File Location

- bundle_id: `teststand`
- source_path: `specifying-the-configuration-file-location.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/specifying-the-configuration-file-location.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The default value of the ApplicationMgr.ConfigFilePath property is %TestStandLocalAppData%\UserInterface.xml, in which %TestStandLocalAppData% is a macro that expands to a directory to which the currently logged-in user has permission to write files. The directory is typically <User Directory>\AppDa

### Specifying the Configuration File Location

The default value of the ApplicationMgr.ConfigFilePath property is %TestStandLocalAppData%\UserInterface.xml, in which %TestStandLocalAppData% is a macro that expands to a directory to which the currently logged-in user has permission to write files. The directory is typically <User Directory>\AppData\Local\National Instruments\TestStand on Microsoft Windows 10/8.1/7. Set the ApplicationMgr.ConfigFilePath property before the application calls the ApplicationMgr.Start method to change the configuration file location.

When you specify a relative file path or just a filename, the file location is relative to the directory that contains the application. When users who do not have Windows administrator privileges can run the application, you must store the configuration file in a location to which users have permission to write files.

Parent topic:

Persisting Application Settings

Related concepts:

- TestStand Directory Structure

<!--NI_TOPIC bundle=teststand path=sql-ts.html language=enus -->
## TOPIC 00821: Structured Query Language (SQL)

- bundle_id: `teststand`
- source_path: `sql-ts.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/sql-ts.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Structured Query Language (SQL) is a widely supported standard for database access. You can use SQL commands to manipulate rows and columns in database tables in TestStand. The following SQL commands are commonly used for database table manipulation in TestStand: CREATE TABLE SELECT INSERT UPDAT

### Structured Query Language (SQL)

The Structured Query Language (SQL) is a widely supported standard for database access.
 You can use SQL commands to manipulate rows and columns in database tables in
 TestStand.

- CREATE TABLE
- SELECT
- INSERT
- UPDATE
- DELETE

Consult the SQL API reference at www.w3schools.com/sql/default.asp for information on the
 usage of these and othe SQL commands.

Parent topic:

TestStand Database Fundamentals

Related information:

- W3 SQL API Reference

<!--NI_TOPIC bundle=teststand path=standard-and-custom-data-types.html language=enus -->
## TOPIC 00822: Standard and Custom Data Types

- bundle_id: `teststand`
- source_path: `standard-and-custom-data-types.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/standard-and-custom-data-types.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: When you create a variable or property, you specify its data type. In some cases, you use a built-in data type, such as a number or a Boolean. In other cases, you might want to use an arbitrarily complex data structure by defining a custom named data type you can reuse with other variables or proper

### Standard and Custom Data Types

When you create a variable or property, you specify its data type. In some cases, you use a built-in data type, such as a number or a Boolean. In other cases, you might want to use an arbitrarily complex data structure by defining a custom named data type you can reuse with other variables or properties.

When you define a custom named data type, the data type must use a unique name. You can add or delete subproperties in each named data type you create without restriction. For example, you might create a Transmitter data type that contains subproperties such as NumChannels and PowerLevel.

TestStand defines a set of standard named data types, which include Error, CommonResults, Path, Expression, and NI_TDMSReference. You can add subproperties to some standard named data types, but you cannot delete any of the built-in subproperties.

Note

Although each variable or property you create with a named data type has the same data structure, the variable or property can contain different values.

Parent topic:

TestStand Building Blocks

Related concepts:

- Data Types
- Modifying Types

<!--NI_TOPIC bundle=teststand path=standard-result-properties.html language=enus -->
## TOPIC 00823: Standard Result Properties

- bundle_id: `teststand`
- source_path: `standard-result-properties.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/standard-result-properties.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: In addition to copying step properties to step results, TestStand also adds a set of standard properties to each step result as subproperties of the Step.Result.TS property, as described in the following table. 11 Standard Result Properties Standard Result Property Description TS.StartTime Time at w

### Standard Result Properties

In addition to copying step properties to step results, TestStand also adds a set of standard properties to each step result as subproperties of the Step.Result.TS property, as described in the following table.

| Standard Result Property | Description |
| --- | --- |
| TS.StartTime | Time at which the step began executing, specifically the number of seconds since the TestStand Engine initialized. |
| TS.TotalTime | Number of seconds the step took to execute, including the time for all step options, such as preconditions, expressions, post actions, module loading, and module execution. |
| TS.ModuleTime | Number of seconds the code module took to execute. |
| TS.Index | Zero-based position of the step in the step group. |
| TS.StepName | Name of the step. |
| TS.StepGroup | Step group that contains the step. The values are Main, Setup, or Cleanup. |
| TS.StepId | Unique step ID, which is a GUID represented as a string that begins with “ID#:” and contains 26 characters (only alphanumeric characters and the special characters “#”, “ :”, “+”, and “/”). TestStand attempts to maintain globally unique step IDs, but copying files on disk does not prevent duplicate IDs. Note The TS.StepId property is not the same as the STEP_ID used for database schemas. |
| TS.Id | A number TestStand assigns to the step result. The number is unique with respect to all other step results in the current TestStand session. |
| TS.InteractiveExeNum | A number TestStand assigns to an interactive execution. The number is unique with respect to all other interactive executions in the current TestStand session. TestStand adds this property only when you run the step interactively. |
| TS.StepType | Name of the step type. |
| TS.Server | The name of the server computer on which the step runs the subsequence it calls. TestStand adds this property only for Sequence Call steps that run subsequences on a remote computer. |
| TS.StepCausedSequenceFailure | TestStand adds this property only when the step fails. The value is True when the step failure causes the sequence to fail. The value is False when the step failure does not cause the sequence to fail or when the sequence has already failed. |
| TS.BlockLevel | Indicates the number of blocks that encloses the step, such as If and For steps. The value is zero for top-level steps. |

Parent topic:

Result Collection

Related concepts:

- Result Collection
- Custom Result Properties

<!--NI_TOPIC bundle=teststand path=starting-an-interactive-execution-in-an-appli.html language=enus -->
## TOPIC 00824: Starting an Interactive Execution in an Application

- bundle_id: `teststand`
- source_path: `starting-an-interactive-execution-in-an-appli.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/starting-an-interactive-execution-in-an-appli.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can start an interactive execution from an execution suspended at a breakpoint using the Thread.DoInteractiveExecution method or as a new execution using the Engine.NewExecution method. Creating the InteractiveArgs Object When you start an interactive execution, create an InteractiveArgs object

### Starting an Interactive Execution in an Application

You can start an interactive execution from an execution suspended at a breakpoint using the Thread.DoInteractiveExecution method or as a new execution using the Engine.NewExecution method.

#### Creating the InteractiveArgs Object

When you start an interactive execution, create an InteractiveArgs object and then pass it to the Thread.DoInteractiveExecution method or the Engine.NewExecution method. Use the InteractiveArgs object to specify which steps to run and whether and how the execution loops.

To determine whether and how the user of the application wants the execution to loop, use the dialog box that launches when you call the Engine.DisplayLoopOnStepsDialog method or write a custom dialog box to launch instead. Next, call the Engine.NewInteractiveArgs method to create the InteractiveArgs object. Set the InteractiveArgs.StepGroup, InteractiveArgs.LoopCount, and InteractiveArgs.StopExpression properties of the object as needed. You do not have to set the InteractiveArgs.LoopCount or InteractiveArgs.StopExpression properties if you do not want the interactive execution to loop. Finally, call the InteractiveArgs.AddStepIndex method for each step you want to run, passing the zero-based step index for each step. In an interactive execution, you can only run steps located in the same sequence and step group. You can then pass the InteractiveArgs object to the Engine.NewExecution method or the Thread.DoInteractiveExecution method.

#### Starting as a New Execution

Create a new interactive execution in the same manner as you would create a new execution to execute a specific sequence, but instead pass an InteractiveArgs parameter. Create an InteractiveArgs object and then pass it to the Engine.NewExecution method.

#### Starting From a Suspended Execution

If you are currently displaying an execution that is suspended at a breakpoint, you can start an interactive execution on steps in the current step group and in the current thread of the execution by calling the Engine.DoInteractiveExecution method on the current thread with an InteractiveArgs object.

Note

Parent topic:

Writing an Application with the TestStand Engine API

Related concepts:

- Executing a Sequence in an Application

<!--NI_TOPIC bundle=teststand path=starting-and-shutting-down-teststand-cvi.html language=enus -->
## TOPIC 00825: Starting and Shutting Down TestStand from a LabWindows/CVI User Interface

- bundle_id: `teststand`
- source_path: `starting-and-shutting-down-teststand-cvi.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/starting-and-shutting-down-teststand-cvi.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: When you initialize the user interface application, use the TSUI_ApplicationMgrStart driver function to invoke the ApplicationMgr.Start method, which starts the TestStand Engine and logs in a user. LabWindows/CVI applications typically wait for user input by calling the RunUserInterface() function a

### Starting and Shutting Down TestStand from a LabWindows/CVI User Interface

When you initialize the user interface application, use the TSUI_ApplicationMgrStart driver function to invoke the ApplicationMgr.Start method, which starts the TestStand Engine and logs in a user.

LabWindows/CVI applications typically wait for user input by calling the RunUserInterface() function after loading and displaying the main user interface panel. The RunUserInterface() function handles all events, such as menu selections, control value changes, and ActiveX control events.

Typically, you click the Close box or execute the Exit command through a TestStand menu or a Button control to stop a user interface application. For user interface events that request the user interface to close, the user interface must call the TSUI_ApplicationMgrShutdown function to unload sequence files, log out, and trigger an OnApplicationCanExit event. When the function determines that the engine can shut down, the canExitNow output parameter returns True. The user interface application then calls the QuitUserInterface() function, which causes the preceding RunUserInterface() call to return. After the application exits the function call to RunUserInterface(), the user interface application must call TSUI_ApplicationMgrShutdown a second time to complete the cleanup process and shut down the engine.

Parent topic:

Startup and Shutdown

Related concepts:

- Startup and Shutdown
- TestStand UI Controls

<!--NI_TOPIC bundle=teststand path=starting-and-shutting-down-teststand-from-a.html language=enus -->
## TOPIC 00826: Starting and Shutting Down TestStand from a .NET User Interface

- bundle_id: `teststand`
- source_path: `starting-and-shutting-down-teststand-from-a.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/starting-and-shutting-down-teststand-from-a.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: When you initialize the user interface application, use the ApplicationWrapper.Run method in the NationalInstruments.TestStand.Utility namespace to load the main form for the application that contains the TestStand Application Manager and other TestStand UI controls. The Run method calls System.Wind

### Starting and Shutting Down TestStand from a .NET User Interface

When you initialize the user interface application, use the ApplicationWrapper.Run method in the NationalInstruments.TestStand.Utility namespace to load the main form for the application that contains the TestStand Application Manager and other TestStand UI controls. The Run method calls System.Windows.Forms.Application.Run, which handles all events, such as menu selections, control value changes, and ActiveX control events. The method also works around exceptions that can occur on shutdown.

Use the MainForm_Load event to initialize the TestStand UI controls and use the ApplicationMgr.Start method to initialize the TestStand engine and log in a user.

Typically, you click the Close box or execute the Exit command through a TestStand menu or button control to stop an application. When operations request the form to close, the form raises the Closing event, where you must call the ApplicationMgr.Shutdown method to initiate shutdown of TestStand. If the return value from the Shutdown method indicates that shutdown is not complete, you must cancel the Close event. When shutdown is complete, TestStand raises the ApplicationMgr.ExitApplication event, where you call the Close method on the form.

Refer to the simple user interface examples for C# and .NET to see how to properly start and shut down TestStand.

#### Additional Considerations for .NET
 Applications to Properly Shut Down TestStand

The TestStand engine shutdown process requires the proper release of all references
 to TestStand objects, such as variables, sequence files, and the TestStand engine
 itself. When using the TestStand engine in a .NET application, you must consider the
 following challenges:

- TestStand reports object leaks —The .NET CLR uses a form
 of automatic memory management, which includes garbage collection to reclaim
 memory, that is no longer in use. When the last reference to a TestStand COM
 object is released, .NET places the object reference into garbage collection,
 and the object is finalized at a later time. If the TestStand engine performs a
 shutdown before garbage collection finalizes TestStand objects, and you have the
 TestStand debug option Report Object Leaks enabled,
 TestStand reports non-finalized objects as leaks, even though the application no
 longer holds a reference to the objects.
- TestStand engine cannot shut down —Some global objects of
 .NET can retain references to TestStand objects that are passed to events of
 TestStand controls on Windows forms. If the application exits before releasing
 these references, the TestStand engine cannot perform a shutdown and some
 necessary tasks, such as saving some TestStand files.

To work around these challenges, NI recommends designing a TestStand .NET application
 to use a separate application domain instead of the default application domain and
 to force garbage collection and disposal of the TestStand engine.

A TestStand .NET application should perform the following startup and shutdown
 tasks:

1. Create the TestStand engine in the default application domain.
2. Create a new application domain and perform the following operations in that
 domain:
  - Create the TestStand engine to obtain a reference to the existing engine
 created by the default application domain.
  - Perform any startup operations on the engine object.
  - Perform operations that use the engine object, including loading and
 running the main form for the application.
  - Close any forms loaded into the application domain.
  - Release all TestStand objects, including the engine, created in the
 application domain.
  - Unload the application domain to ensure that all TestStand object
 references are finalized.
3. Force garbage collection of all object generations.
4. Force the release and finalization of the TestStand Engine COM object created in
 the default application domain.

To perform many of the previously listed tasks, you can call the
 LaunchTestStandApplicationInNewDomain.LaunchProtected method in
 the NationalInstruments.TestStand.Utility assembly. The
 LaunchProtected method creates an instance of the TestStand
 engine, loads a new application domain, calls a delegate main entry point in the
 application domain, and, before returning, the method properly unloads the
 application domain, forces garbage collection, and finalizes the TestStand engine
 COM object.

To properly cleanup before it returns, the
 LaunchTestStandApplicationInNewDomain.LaunchProtected method
 uses TSHelper.DoSynchronousGCForCOMObjectDestruction to force
 garbage collection by calling System.GC.Collect and
 GC.WaitForPendingFinalizers twice and calling
 System.Runtime.InteropServices.Marshal.FinalReleaseComObject on
 the engine reference.

Note

FinalReleaseComObject

InvalidComObjectException

Note

TestStandObjectReleaser

NationalInstruments.TestStand.Utility

LaunchTestStandApplicationInNewDomain.LaunchProtected

Refer to the source code file,
 <TestStand>\API\DotNET\Source\TSUtil\TSUtil.cs, for more
 information about the implementation of the
 LaunchTestStandApplicationInNewDomain class and the
 TSHelper class that it uses.

The following example code illustrates the recommended way to use the TestStand
 engine in .NET:

```text
using NationalInstruments.TestStand.Utility;
using NationalInstruments.TestStand.Interop.API;
[STAThread]
static void Main(string[] args)
{
    // Create application domain, call MainEntryPoint, and 
    // cleanup before return.
    LaunchTestStandApplicationInNewDomain.LaunchProtected(
        new LaunchTestStandApplicationInNewDomain.
            MainEntryPointDelegateWithArgs(MainEntryPoint),
        args,
        "TestStand Application",
        new LaunchTestStandApplicationInNewDomain.
            DisplayErrorMessageDelegate(DisplayErrorMessage));
}
// Main entry point executed in new application domain.
private static void MainEntryPoint(string[] args)
{
    // Obtain a reference to existing Engine.
    Program._engine = new Engine();
    Program._engine.LoadTypePaletteFilesEx(
        TypeConflictHandlerTypes.ConflictHandler_Prompt, 0);
    // Launch your application here.
    // e.g., Application.Run(new MainForm());
    // Engine clean up.
    Program._engine = null;
}
// Called if exception occurs in MainEntryPoint.
private static void DisplayErrorMessage(string caption, string message)
{
    // Handle error here.
    // e.g., MessageBox.Show(message, caption);
}
private static Engine _engine = null;
```

Refer to the simple user interface examples for C# and .NET to see how to use a
 separate application domain to properly shut down TestStand.

Parent topic:

Startup and Shutdown

Related concepts:

- TestStand UI Controls
- Managed Code Considerations for TestStand and .NET 8

<!--NI_TOPIC bundle=teststand path=starting-and-shutting-down-teststand-labview.html language=enus -->
## TOPIC 00827: Starting and Shutting Down TestStand from a LabVIEW User Interface

- bundle_id: `teststand`
- source_path: `starting-and-shutting-down-teststand-labview.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/starting-and-shutting-down-teststand-labview.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Invoke the ApplicationMgr.Start method to start TestStand, as shown in the Simple OI - Top-Level VI and in the Full UI - Top-Level VI example user interface VIs. User interface applications wait in a main event loop after starting TestStand. The main event loop must handle the events that stop the u

### Starting and Shutting Down TestStand from a LabVIEW User Interface

Invoke the ApplicationMgr.Start method to start TestStand, as shown in the Simple OI - Top-Level VI and in the Full UI - Top-Level VI example user interface VIs.

User interface applications wait in a main event loop after starting TestStand. The main event loop must handle the events that stop the user interface application. The main event loop can also handle other events, such as menu selections and LabVIEW control changes.

Typically, you click the Close box or execute the Exit command through a TestStand menu or a Button control to stop a user interface application.

When you click the Close box, the Event structure in the main event loop handles the Panel Close? event. The block diagram that handles the event invokes the ApplicationMgr.Shutdown method and discards the event. When the ApplicationMgr.Shutdown method returns True to indicate TestStand is ready to shut down, the main event loop stops. When the ApplicationMgr.Shutdown method returns False, the main event loop waits because TestStand cannot shut down until the executions complete or you unload sequence files. When TestStand is ready, the Application Manager control generates the ApplicationMgr.ExitApplication event.

The callback VI for the ApplicationMgr.ExitApplication event generates a LabVIEW Quit Application user event, which the example user interface VIs handle, to inform the main event loop to stop.

Refer to the following example user interface VIs for examples of the main event loop and how to shut down TestStand. These VIs also provide examples of creating, generating, and handling the Quit Application event.

- Simple OI - Top-Level VI
- Simple OI - ExitApplication Event Callback
- Full UI - Top-Level VI
- Full UI - Create LabVIEW Application Events
- Full UI - ExitApplication Event Callback

Parent topic:

Startup and Shutdown

Related concepts:

- Example User Interfaces

<!--NI_TOPIC bundle=teststand path=startup-and-shutdown.html language=enus -->
## TOPIC 00828: Startup and Shutdown

- bundle_id: `teststand`
- source_path: `startup-and-shutdown.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/startup-and-shutdown.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: As a final step in the initialization of the application, call the ApplicationMgr.Start method to initialize the Application Manager control and launch the LoginLogout Front-End callback sequence if you did not set the ApplicationMgr.LoginOnStart property to False. Complete the following steps to sh

### Startup and Shutdown

As a final step in the initialization of the application, call the ApplicationMgr.Start method to initialize the Application Manager control and launch the LoginLogout Front-End callback sequence if you did not set the ApplicationMgr.LoginOnStart property to False.

Complete the following steps to shut down the application.

1. When the application holds any references to TestStand objects, such as sequence files or executions, handle the ApplicationMgr.QueryShutdown event by canceling the shutdown process or releasing the TestStand object references the application holds.
2. Call the ApplicationMgr.Shutdown method. When the method returns True , exit the application. When the method returns False , do not exit the application. Leaving the application running allows the method to shut down any running executions and unload sequence files. When the shut down process completes, TestStand User Interface (UI) Controls the Application Manager control generates the ApplicationMgr.ExitApplication event to notify you to exit the application. If the application cancels the shutdown process, the Application Manager control generates the ApplicationMgr.ShutDownCancelled event, which occurs when users choose not to terminate a busy execution. Note When you use the TestStand User Interface (UI) Controls to create an Exit button or an Exit menu option that invokes the Exit command, the button or menu option automatically calls the ApplicationMgr.Shutdown method for you.
3. Exit the application in the event handler you create for the ApplicationMgr.ExitApplication event. The window in which the Application Manager control resides must exist until you receive the ApplicationMgr.ExitApplication event.

Parent topic:

Getting Started with User Interface Development

Related concepts:

- Application Manager
- Modifying Front-End Callbacks
- TestStand UI Controls

<!--NI_TOPIC bundle=teststand path=statement-step-type.html language=enus -->
## TOPIC 00829: Statement Step Type

- bundle_id: `teststand`
- source_path: `statement-step-type.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/statement-step-type.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Purpose This example demonstrates how to use an expression in a Statement step to dynamically change the high and low limits of a Numeric Limit Test step. NI typically recommends that you use expressions when you configure a Numeric Limit Test step or to use a Property Loader step to change limits,

### Statement Step Type

#### Purpose

This example
 demonstrates how to use an expression in a Statement step to dynamically change the
 high and low limits of a Numeric Limit Test step.

Note

#### Example File
 Location

<TestStand
 Public>\Examples\Built-In Step Types\Statement Step Type\Statement
 Step Type.seq

#### Highlighted Features

Expressions

#### Major API

None

#### Prerequisites

None

#### How to Use This Example

Complete the following steps to use this example.

1. On the Steps pane, select the Numeric Limit Test step.
2. On the Step Settings pane, click the Limits tab. The comparison type for the step is currently GELE (>= <=) , with a high value of 10 and a low value of 0 . When accessed from the Numeric Limit Test step, the numeric limits for the Numeric Limit Test step are Step.Limit.High and Step.Limit.Low . However, another step cannot access the variables Step.Limit.High and Step.Limit.Low , as shown in this example. Instead, you must explicitly specify the step that specifies the properties you want to access.
3. On the Steps pane, select the A Statement that changes the numeric limits step, which is a Statement step.
4. On the Step Settings pane, click the Expression edit tab. The Expression tab contains two expressions, separated by a comma, that specify the high limit as 11 and the low limit as 0 : RunState.Sequence.Main["Numeric Limit Test"].Limits.High = 11, RunState.Sequence.Main["Numeric Limit Test"].Limits.Low = 0 The expressions specify that you want to use the Numeric Limit Test step to specify the properties you want to access. Alternatively, you could use the following expression: 'RunState.NextStep.Limits.High'
5. Select Execute»Single Pass to run the sequence.
6. When the execution completes, review the report. For the Numeric Limit Test step, the High Limit value is 11 , and the Low Limit value is 0 .

Because the Statement step executed before the Numeric Limit Test step in the sequence, changing the limits after the Numeric Limit Test executes does not change the limit values.

Parent topic:

Examples for Built-In Step Types

Related concepts:

- TestStand Directory Structure
- Expressions

<!--NI_TOPIC bundle=teststand path=station-global-variables.html language=enus -->
## TOPIC 00830: Station Global Variables

- bundle_id: `teststand`
- source_path: `station-global-variables.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/station-global-variables.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Station global variables are variables specific to a computer that you can access from all steps and sequences on that computer. Any changes you make to the value of a station global variable are reflected in all other steps and sequences. Use the Station Globals window of the TestStand Sequence Edi

### Station Global Variables

Station global variables are variables specific to a computer that you can access from all steps and sequences on that computer. Any changes you make to the value of a station global variable are reflected in all other steps and sequences.

Use the Station Globals window of the TestStand Sequence Editor to create station global variables. Creating a station global variable is similar to creating a variable of any other scope. You can access and use station global variables similarly to variables of other scopes, such as local variables.

Note

While running, TestStand stores the station global variables in the StationGlobals property object.

TestStand saves the station global variables in the StationGlobals.ini file in the <TestStand Application Data>\Cfg directory automatically when you close the TestStand Engine. You can also save the station global variables from the Station Globals window or by calling the Engine.CommitGlobalsToDisk method.

Note

The TestStand Deployment Utility does not automatically deploy the station global variables. You can include the StationGlobals.ini file in the deployment image, but doing so might remove any station global variables that exist on the target computer to which you deploy the image.

Note

Execution.RunTimeVariables

Thread.RunTimeVariables

Parent topic:

Variables

Related concepts:

- Sequence Local Variables
- Station Globals TS Subproperty
- <TestStand Application Data> Directory

<!--NI_TOPIC bundle=teststand path=station-globals-ts-subproperty.html language=enus -->
## TOPIC 00831: Station Globals TS Subproperty

- bundle_id: `teststand`
- source_path: `station-globals-ts-subproperty.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/station-globals-ts-subproperty.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The StationGlobals property object contains the station global variables for the TestStand Engine invocation. Each TestStand session maintains a single copy of the station global variables in memory. Any modifications you make to a station global property affect all executions in the current TestSta

### Station Globals TS Subproperty

The StationGlobals property object contains the station global variables for the TestStand Engine invocation. Each TestStand session maintains a single copy of the station global variables in memory. Any modifications you make to a station global property affect all executions in the current TestStand session and future TestStand sessions.

TestStand creates a TS subproperty in the StationGlobals property to hold the standard station global variables TestStand defines.

| Sequence Context Subproperty | Description |
| --- | --- |
| TS | Contains the TestStand-specific station global variables. |
| LastUserName | Login name of the user that logged in most recently. |
| CurrentUser | User object for the currently logged-in user. This property does not exist when no user has logged in. Refer to User and Group Privileges for more information about the User standard data type. |

Parent topic:

Sequence Context

Related concepts:

- Station Global Variables

<!--NI_TOPIC bundle=teststand path=step-execution.html language=enus -->
## TOPIC 00832: Step Execution

- bundle_id: `teststand`
- source_path: `step-execution.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/step-execution.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Depending on the options you specify when you configure a step, a step performs multiple actions as it executes. The following table lists the most common actions a step can take, in the order the step performs them. Action Number Description Remarks 1 Allocate step result — 2 Enter batch synchroniz

### Step Execution

Depending on the options you specify when you configure a step, a step performs multiple actions as it executes. The following table lists the most common actions a step can take, in the order the step performs them.

| Action Number | Description | Remarks |
| --- | --- | --- |
| 1 | Allocate step result | — |
| 2 | Enter batch synchronization section | When option is set |
| 3 | Check run mode for Skip | Sets the corresponding status on the step, then proceeds to Action Number 34 |
| 4 | Evaluate precondition | When False, performs Action Number 29, then proceeds to Action Number 33 |
| 5 | Acquire step lock | When option is set |
| 6 | Check run mode for Force Pass or Force Fail | Sets the corresponding status on the step, then proceeds to Action Number 30 |
| 7 | Load module if not already loaded | — |
| 8 | Execute step switching | — |
| 9 | Evaluate Loop Initialization expression | Only when looping |
| 10 | Evaluate Loop While expression, skip to Action Number 27 when False | Only when looping |
| 11 | Allocate loop iteration result | Only when looping |
| 12 | Call Pre-Step Engine callbacks | — |
| 13 | Evaluate Pre-Expression | — |
| 14 | Call Pre-Step substeps for step type | — |
| 15 | Process additional results for input parameters | — |
| 16 | Call module | — |
| 17 | Process additional results for output parameters | — |
| 18 | Call Post-Step substeps for step type | TestStand calls Post-Step substeps even when the user code module generates a run-time error, which enables Post-Step substeps to perform error handling, when appropriate. If Post-Step substeps clear run-time errors, proceed to Action Number 19. If step is configured to ignore run-time errors, proceed to Action Number 23. |
| 19 | Evaluate Post-Expression | — |
| 20 | Evaluate Status expression | — |
| 21 | Call Post-Step Engine callbacks | — |
| 22 | Call Post-Step Failure Engine callback | Only when loop iteration fails |
| 23 | Populate loop iteration result | Only when looping |
| 24 | Call Post-ResultList Entry Engine callback | Only when looping |
| 25 | Call Post-Results Engine callback | Only when looping |
| 26 | Evaluate Loop Increment expression, return to Action Number 10 | Only when looping |
| 27 | Evaluate Loop Status expression | Only when looping |
| 28 | Disconnect switching routes with step lifetime | — |
| 29 | Unload module when required | — |
| 30 | Update sequence failed state | — |
| 31 | Call Post-Step Failure Engine callback | Only when step fails |
| 32 | Execute post action | — |
| 33 | Release step lock | When option is set |
| 34 | Exit batch synchronization section | When option is set |
| 35 | Populate step result | Custom additional results also populate at this time. However, additional results for input and output parameters populate immediately before and after Action Number 16, respectively. |
| 36 | Call Post-ResultList Entry Engine callback | — |
| 37 | Call Post-Results Engine callback | — |

Usually, a step performs only a subset of these actions depending on the configuration of the step and the test station. When TestStand detects a run-time error in one of these actions, it calls the Post-Step Error Engine callbacks. When you do not define these callbacks or when the callbacks do not reset the error state for the step, TestStand executes the following actions to clean up the execution of the step:

- If the error occurs before the step calls the code module, TestStand does not call the code
 module and proceeds to Action Number 28.
- If the error occurs while the step is calling the code module, TestStand proceeds to Action
 Number 28.
- If the error occurs after the step calls the code module, TestStand calls Action Number 21, if
 it is not already called, and proceeds to Action Number 28.
- If a run-time error occurs in a loop iteration, TestStand also populates the loop iteration
 result, Action Number 23.

Parent topic:

Executions

Related concepts:

- Updating the Status Bar Using UI Messages

<!--NI_TOPIC bundle=teststand path=step-groups.html language=enus -->
## TOPIC 00833: Step Groups

- bundle_id: `teststand`
- source_path: `step-groups.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/step-groups.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: TestStand executes the steps in the following step group order: Setup—Typically contains steps that initialize instruments, fixtures, or a UUT. Main—Typically contains the bulk of the steps in a sequence, including the steps that test the UUT. Cleanup—Typically contains steps that power off or resto

### Step Groups

TestStand executes the steps in the following step group order:

1. Setup —Typically contains steps that initialize instruments, fixtures, or a UUT.
2. Main —Typically contains the bulk of the steps in a sequence, including the steps that test the UUT.
3. Cleanup —Typically contains steps that power off or restore the initial state of instruments, fixtures, and the UUT.

Use separate step groups to ensure that the steps in the Cleanup step group execute regardless of whether the sequence completes successfully or whether a run-time error occurs in the sequence. If a step in the Setup or Main step group causes a run-time error to occur or if the operator terminates the execution, the flow of execution stops and jumps to the Cleanup step group. Steps in the Cleanup group always run even when some of the steps in the Setup group do not run. When a step in the Cleanup group causes a run-time error, execution continues to the next step in the Cleanup group.

When a run-time error occurs in a sequence, TestStand reports the run-time error to the calling sequence. Execution in the calling sequence jumps to the Cleanup step group in the calling sequence. This process continues up the call stack to the top-level sequence. Thus, when a run-time error occurs, TestStand terminates execution after running all the Cleanup steps in all the sequences in the sequence call stack.

Parent topic:

Sequences

<!--NI_TOPIC bundle=teststand path=step-result-table-schema.html language=enus -->
## TOPIC 00834: STEP_RESULT Table Schema

- bundle_id: `teststand`
- source_path: `step-result-table-schema.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/step-result-table-schema.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The default TestStand schema logs common subproperties of all steps to this table. 14 STEP_RESULT Table Schema Column Name Data Type Description ID Primary Key Unique value that identifies each entry in the table. For Microsoft Access and Microsoft SQL Server, the default process model assumes that

### STEP_RESULT Table Schema

The default TestStand schema logs common subproperties of all steps to this table.

| Column Name | Data Type | Description |
| --- | --- | --- |
| ID | Primary Key | Unique value that identifies each entry in the table. For Microsoft Access and Microsoft SQL Server, the default process model assumes that this column increments automatically. For Oracle, the default process model uses an Oracle SQL sequence to generate a unique number. |
| UUT_RESULT | Foreign Key | Unit Under Test (UUT) ID from the UUT_RESULT table that associates the step result with a UUT. |
| STEP_PARENT | Foreign Key | ID of the parent sequence call step result when the step is a step in a subsequence. |
| STEP_NAME | String | Name of the step. |
| STEP_TYPE | String | Name of the step type. |
| STEP_GROUP | String | Step group that contains the step. The value is "Main", "Setup", or "Cleanup". |
| STEP_INDEX | Number | Zero-based position of the step in the step group. |
| STEP_ID | String | Unique ID of the step. Note This Step_ID property is not the same as the TS.StepId used to report test results. |
| STATUS | String | Status of the step. |
| REPORT_TEXT | String | Report text of the step. |
| ERROR_CODE | Number | Error code when the step status is Error. |
| ERROR_MESSAGE | String | Error message when the step status is Error. |
| CAUSED_SEQFAIL | Boolean | Indicates whether the step failure caused the sequence to fail. |
| MODULE_TIME | Number | Number of seconds the step module took to execute. |
| TOTAL_TIME | Number | Number of seconds the step took to execute, including module execution and all step options, such as preconditions, expressions, post actions, and module loading. |
| NUM_LOOPS | Number | Number of loops the step executed, if any. |
| NUM_PASSED | Number | Number of loops the step returned with a status of Passed, if any. |
| NUM_FAILED | Number | Number of loops the step returned with a status of Failed, if any. |
| ENDING_LOOP_INDEX | Number | The loop index after executing the ending loop. |
| LOOP_INDEX | Number | The value of the loop index for an iteration of the step. |
| INTERACTIVE_EXENUM | Number | Number TestStand assigns to an interactive execution. The number is unique with respect to all other interactive executions in the current TestStand session. TestStand adds this property only when you run the step interactively. |
| ORDER_NUMBER | Number | The order in which the step executed within the execution. |

Parent topic:

Default TestStand Table Schemas

<!--NI_TOPIC bundle=teststand path=step-results.html language=enus -->
## TOPIC 00835: Step Results

- bundle_id: `teststand`
- source_path: `step-results.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/step-results.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: A model plug-in can receive step results after a UUT completes or on-the-fly. After UUT Completion After each UUT completes, the process model calls the Model Plugin – UUT Done entry point and uses the MainSequenceResult parameter to pass a reference to the result of the process model Sequence Call

### Step Results

A model plug-in can receive step results after a UUT completes or on-the-fly.

#### After UUT Completion

After each UUT completes, the process model calls the Model Plugin – UUT Done entry point and uses the MainSequenceResult parameter to pass a reference to the result of the process model Sequence Call step that calls the client file. The Parameters.MainSequenceResult.TS.SequenceCall.ResultList array contains the step results of the top-level client sequence. If a result in the array is a Sequence Call step result, the TS.SequenceCall.ResultsList property of the subsequence includes the results of all steps in the subsequence. The TS.SequenceCall.Sequence, TS.SequenceCall.SequenceFile, and TS.SequenceCall.Status properties include the sequence name, sequence file path, and result status for the subsequence.

A plug-in that processes results, such as a report generator or a database logger, typically recursively traverses the TS.SequenceCall.ResultsList array, including results of subsequences, to generate a report or log results to a database.

#### On-The-Fly

If you enable a plug-in to process results on-the-fly by setting the ProcessOnTheFly subproperty to True, TestStand progressively collects results concurrent with the test execution. When TestStand collects a result and exceeds a threshold in time or in the number of collected results, the process model passes the results collected since the last time TestStand exceeded the threshold to the Model Plugin – OnTheFly Step Results entry point for processing.

A plug-in that processes results on-the-fly, such as a report generator or a database logger, typically appends data to a report or logs the data to a database while iterating through each array of results the model passes to the OnTheFly Step Results entry point.

#### On-The-Fly - Provisional Results

TestStand cannot determine the result status of a Sequence Call step before the subsequence
 completes. Therefore, TestStand does not generate the final parent result for the steps of a
 subsequence until the subsequence completes. To support process model plug-ins that must
 immediately identify the parent result for each child result, TestStand generates a
 provisional result for a Sequence Call step before executing the steps in the subsequence.

Similarly, TestStand cannot determine the result status of a step that loops before all the
 loop iterations in the step complete. Therefore, TestStand does not generate the final step
 result of a step that loops until all loop iterations complete. To support process model
 plug-ins that display loop information, such as the loop index, the number of loops that
 passed, and the number of loops that failed, while the step loops and before loop iterations
 complete, TestStand generates a provisional result for steps that loop.

The ID of a provisional result is the same as the ID of the corresponding final result.
 TestStand passes provisional results only to the Model Plugin - OnTheFly Step Results
 plug-in entry point and PostResults engine callback. Use the existence of the
 TS.Provisional Boolean subproperty to identify provisional results.

Additionally, TestStand generates a provisional result after executing all the steps in a
 sequence that executes in a new thread. Some process model plug-ins can use this provisional
 result to re-process results collected for steps that executed in a new thread. The ID of
 the provisional result is the same as the ID of the corresponding Sequence Call step that
 executed the sequence. Use the existence of the TS.ThreadComplete Boolean
 subproperty to identify this provisional result.

In a Model Plugin - OnTheFly Step Results plug-in entry point, you use or ignore
 provisional results depending on what the plug-in requires.

Parent topic:

Process Model Plug-In Architecture

Related concepts:

- Model Plugin – UUT Done
- Model Plugin – OnTheFly Step Results
- Executions

<!--NI_TOPIC bundle=teststand path=step-seqcall-table-schema.html language=enus -->
## TOPIC 00836: STEP_SEQCALL Table Schema

- bundle_id: `teststand`
- source_path: `step-seqcall-table-schema.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/step-seqcall-table-schema.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The default TestStand schema logs subproperties of the Sequence Call step to this table. 15 STEP_SEQCALL Table Schema Column Name Data Type Description ID Primary Key Unique value that identifies each entry in the table. STEP_RESULT Foreign Key Step ID from the STEP_RESULT table that associates the

### STEP_SEQCALL Table Schema

The default TestStand schema logs subproperties of the Sequence Call step to this table.

| Column Name | Data Type | Description |
| --- | --- | --- |
| ID | Primary Key | Unique value that identifies each entry in the table. |
| STEP_RESULT | Foreign Key | Step ID from the STEP_RESULT table that associates the result with a step. |
| SEQUENCE_NAME | String | The name of the sequence that was called. |
| SEQUENCE_FILE_PATH | String | The path to the sequence file. |

Parent topic:

Default TestStand Table Schemas

<!--NI_TOPIC bundle=teststand path=step-status.html language=enus -->
## TOPIC 00837: Step Status

- bundle_id: `teststand`
- source_path: `step-status.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/step-status.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Every step has a ResultStatus property, which is a string constant that indicates the result of the step execution. Although TestStand imposes no restrictions on the values to which the step or the code module of the step can set the status property, TestStand and the built-in step types use and rec

### Step Status

Every step has a ResultStatus property, which is a string constant that indicates the result of the step execution. Although TestStand imposes no restrictions on the values to which the step or the code module of the step can set the status property, TestStand and the built-in step types use and recognize the values that appear in the following table.

| String Value | Meaning | Source of the Status Value |
| --- | --- | --- |
| Passed | Indicates the step performed a test that passed, or the step did not execute because the run mode for the step is Force Pass. | Step, code module, or TestStand |
| Failed | Indicates the step performed a test that failed, or the step did not execute because the run mode for the step is Force Fail.When you enable the Step Failure Causes Sequence Failure option on the Run Options panel of the Step Settings pane, TestStand sets the sequence status to Failed when a step fails. When the sequence returns as Failed, the Sequence Call step also fails. In this way, a step failure in a subsequence can propagate up through the chain of Sequence Call steps. By default, TestStand enables the Step Failure Causes Sequence Failure option for most step types.You can also control how execution proceeds after a step failure causes a sequence to fail. To configure an execution to jump to the Cleanup step group upon failure, enable the Immediately Goto Cleanup on Sequence Failure option in the Sequence Properties dialog box. By default, TestStand disables this option. | Step, code module, or TestStand |
| Error | Indicates a run-time error occurred. | TestStand |
| Done | Indicates the step completed without setting the status. | TestStand |
| Terminated | Indicates the step did not set the status and a request to terminate the execution occurred while executing the step. When you request to terminate an execution, the currently executing sequence invocation for each thread waits for the current running step to complete before initiating termination. A terminating sequence runs steps in the Cleanup step group, if not already executing, and returns to the calling sequence. When a terminating subsequence returns to a calling sequence, TestStand sets the calling sequence step status to Terminated, and the calling sequence continues the termination process up the call stack unless you enabled the Ignore Termination option on the Run Options panel of the Step Settings pane for the Sequence Call step. When you enable this setting, TestStand ignores the termination of the execution for the thread, and the thread execution continues normally. If TestStand returns the request to terminate the execution to the root sequence invocation, the result status for the execution is Terminated. | TestStand |
| Skipped | Indicates the step did not execute because the run mode for the step is Skip. | TestStand |
| Running | Indicates the step is currently running. | TestStand |
| Looping | Indicates the step is currently running in loop mode. | TestStand |

#### Failures

When you enable the Step Failure Causes Sequence Failure option on the Run Options panel of the Step Settings pane, TestStand sets the sequence status to Failed when a step fails. When the sequence returns as Failed, the Sequence Call step also fails. In this way, a step failure in a subsequence can propagate up through the chain of Sequence Call steps. By default, TestStand enables the Step Failure Causes Sequence Failure option for most step types.

You can also control how execution proceeds after a step failure causes a sequence to fail. To configure an execution to jump to the Cleanup step group upon failure, enable the Immediately Goto Cleanup on Sequence Failure option in the Sequence Properties dialog box. By default, TestStand disables this option.

#### Terminations

When you request to terminate an execution, the currently executing sequence invocation for each thread waits for the current running step to complete before initiating termination. A terminating sequence runs steps in the Cleanup step group, if not already executing, and returns to the calling sequence. When a terminating subsequence returns to a calling sequence, TestStand sets the calling sequence step status to Terminated, and the calling sequence continues the termination process up the call stack unless you enabled the Ignore Termination option on the Run Options panel of the Step Settings pane for the Sequence Call step. When you enable this setting, TestStand ignores the termination of the execution for the thread, and the thread execution continues normally. If TestStand returns the request to terminate the execution to the root sequence invocation, the result status for the execution is Terminated.

Parent topic:

Result Collection

Related concepts:

- Built-In Step Types

<!--NI_TOPIC bundle=teststand path=step-type-combination.html language=enus -->
## TOPIC 00838: Step Type Combination

- bundle_id: `teststand`
- source_path: `step-type-combination.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/step-type-combination.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Select Combine with Step Type from the Types window context menu to combine the functionality of two step types into a single new step type. Use this feature when the sequences commonly use steps of two different step types together to perform an operation that would be more convenient to perform wi

### Step Type Combination

Select Combine with Step Type from the Types window context menu to combine the functionality of two step types into a single new step type. Use this feature when the sequences commonly use steps of two different step types together to perform an operation that would be more convenient to perform with a single step. For example, you can combine a step type that reads a measurement from a specialized instrument with the Numeric Limit Test step type in order to read a measurement and check limits on it in a single step.

Note

Parent topic:

TestStand Sequence Editor

<!--NI_TOPIC bundle=teststand path=step-types-that-do-not-use-module-adapters.html language=enus -->
## TOPIC 00839: Step Types That Do Not Use Module Adapters

- bundle_id: `teststand`
- source_path: `step-types-that-do-not-use-module-adapters.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/step-types-that-do-not-use-module-adapters.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following step types do not use module adapters. When you create an instance of one of these step types, you use the edit tabs or dialog boxes, which you access through the context menu of the step or the Step Settings pane, to configure the step. You do not specify a code module. Flow Control S

### Step Types That Do Not Use Module Adapters

The following step types do not use module adapters. When you create an instance of one of these step types, you use the edit tabs or dialog boxes, which you access through the context menu of the step or the Step Settings pane, to configure the step. You do not specify a code module.

- Flow Control
- Statement
- Label
- Message Popup
- Call Executable
- Property Loader
- Legacy Property Loader
- FTP Files
- Additional Results
- Synchronization Step Types
- Database Step Types
- IVI Step Types
- LabVIEW Utility Step Types

Note

Parent topic:

Built-In Step Types

<!--NI_TOPIC bundle=teststand path=step-types-that-work-with-specific-module-ada.html language=enus -->
## TOPIC 00840: Step Types That Work with Specific Module Adapters

- bundle_id: `teststand`
- source_path: `step-types-that-work-with-specific-module-ada.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/step-types-that-work-with-specific-module-ada.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following step types use specific module adapters. When you create an instance of one of these step types, use the edit tabs or dialog boxes, which you access through the context menu of the step or the Step Settings pane, to configure the step. Sequence Call Run VI Asynchronously

### Step Types That Work with Specific Module Adapters

The following step types use specific module adapters. When you create an instance of one of these step types, use the edit tabs or dialog boxes, which you access through the context menu of the step or the Step Settings pane, to configure the step.

- Sequence Call
- Run VI Asynchronously

Parent topic:

Built-In Step Types

<!--NI_TOPIC bundle=teststand path=step-types-you-can-use-with-any-module-adapte.html language=enus -->
## TOPIC 00841: Step Types You Can Use with Any Module Adapter

- bundle_id: `teststand`
- source_path: `step-types-you-can-use-with-any-module-adapte.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/step-types-you-can-use-with-any-module-adapte.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use the following built-in step types with any module adapter: Pass/Fail Test Numeric Limit Test Multiple Numeric Limit Test String Value Test Action When you insert a step in a sequence, you must select a module adapter in the Step Types list of the Insertion Palette or from the Adapter rin

### Step Types You Can Use with Any Module Adapter

You can use the following built-in step types with any module adapter:

- Pass/Fail Test
- Numeric Limit Test
- Multiple Numeric Limit Test
- String Value Test
- Action

When you insert a step in a sequence, you must select a module adapter in the Step Types list of the Insertion Palette or from the Adapter ring control on the TestStand Sequence Editor toolbar. TestStand assigns the adapter you selected when you insert the step. Once you add a step, you can change the adapter associated with the selected step on the General panel on the Step Settings pane.

Note

Configure»Adapters

When you select the <None> adapter, the step does not call a code module.

To specify the code module the step calls, select Specify Module from the step context menu or click the Module tab on the Step Settings pane.

Parent topic:

Built-In Step Types

Related concepts:

- Step Types That Work with Specific Module Adapters

<!--NI_TOPIC bundle=teststand path=step-types.html language=enus -->
## TOPIC 00842: Step Types

- bundle_id: `teststand`
- source_path: `step-types.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/step-types.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Just as each property or variable has a data type, each step has a step type. Each step of a type includes the built-in step properties and any number of custom step properties the step defines. Although all steps of the same type have the same properties, the values of those properties can differ.

### Step Types

Just as each property or variable has a data type, each step has a step type. Each step of a type includes the built-in step properties and any number of custom step properties the step defines. Although all steps of the same type have the same properties, the values of those properties can differ. The step type specifies the initial values of all the step properties.

You can create a test application using only the predefined step types, and you can also create custom step types to define standard, reusable classes of steps that apply specifically to the application.

#### Source Code Templates

You can define a source code template for a new step type. When you create a new step of a particular type, you can use a source code template to generate source code for the code module of the step. You can also create additional code templates for built-in step types when you create a new step type.

#### Multiple Code Templates per Step Type

You can specify more than one code template for a step type. For example, you might want to have code templates that contain example code for conducting the same type of tests with different types of instruments or data acquisition boards. When a step type has multiple code templates and you click the Create Code button on the Module tab of the Step Settings pane, TestStand prompts you to select from a list of templates or uses the template you selected on the Module tab when it exists.

Parent topic:

Steps

Related concepts:

- Built-In Step Types
- Built-In Step Properties
- Custom Step Properties
- Creating Custom Step Types
- Code Modules
- Instrument Control Step Types

<!--NI_TOPIC bundle=teststand path=steps.html language=enus -->
## TOPIC 00843: Steps

- bundle_id: `teststand`
- source_path: `steps.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/steps.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: A step can perform many actions, such as initializing an instrument, performing a complex test, or controlling the flow of execution in a sequence. Steps perform these actions through several types of mechanisms, including jumping to another step, executing an expression, calling a subsequence, or c

### Steps

A step can perform many actions, such as initializing an instrument, performing a complex test, or controlling the flow of execution in a sequence. Steps perform these actions through several types of mechanisms, including jumping to another step, executing an expression, calling a subsequence, or calling an external code module.

Steps can include built-in and custom properties. For steps that call code modules, the module adapter uses the built-in step properties to store parameters to pass to the code module and to specify where to store results the code module returns.

Not all steps call code modules. Some steps perform standard actions you configure using panes and dialog boxes. In this case, the panes and dialog boxes use the custom step properties to store the configuration settings you specify.

Parent topic:

TestStand Building Blocks

Related concepts:

- Code Modules
- Built-In Step Properties
- Custom Step Properties
- Module Adapters
- Updating the Status Bar Using UI Messages
- TestStand Building Blocks

<!--NI_TOPIC bundle=teststand path=storing-additional-information-for-uuts-and-t.html language=enus -->
## TOPIC 00844: Storing Additional Information for UUTs and Test Stations in Process Models

- bundle_id: `teststand`
- source_path: `storing-additional-information-for-uuts-and-t.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/storing-additional-information-for-uuts-and-t.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Where to Access the UUT and StationInfo Variables to Make Changes You can access the UUT as Parameters.UUT and the StationInfo as Parameters.ModelData.StationInfo in client file callbacks such as PreUUT or in process model plug-in entry points such as Model Plugin - Pre UUT. You can access the UUT i

### Storing Additional Information for UUTs and Test Stations in Process Models

#### Where to Access the UUT and StationInfo Variables to Make Changes

You can access the UUT as Parameters.UUT and the StationInfo as Parameters.ModelData.StationInfo in client file callbacks such as PreUUT or in process model plug-in entry points such as Model Plugin - Pre UUT.

Note

Parameters.ModelData.BatchUUT

AdditionalData

#### UUT Data Type
 Subproperties

The UUT data type in the default process models includes the
 subproperties described in the following table for storing UUT information. The
 AdditionalData container subproperty was added in TestStand
 2013.

| Subproperty | Type | Content | How to Include in Report | How to Include in Database Logging |
| --- | --- | --- | --- | --- |
| SerialNumber | String | UUT serial number | The default report generator process model plug-in automatically adds the UUT serial number to a report. | The default schemas for database logging automatically log the UUT serial number to the UUT_RESULT table. |
| BatchSerialNumber | String | Batch serial number | The default report generator process model plug-in automatically adds the batch serial number to a report. | The default schemas for database logging automatically log the batch serial number to the UUT_RESULT table. |
| PartNumber | String | UUT part number | The default report generator process model plug-in automatically adds the UUT part number, if specified, to a report. | The default schemas for database logging automatically log the UUT part number to the UUT_RESULT table. |
| AdditionalData | Unstructured Container | You can add subproperties of any data type to this container to store additional information associated with a UUT.For example, you can add subproperties to the Locals.UUT.AdditionalData container in the default process model entry points at edit-time, or you can programmatically add subproperties at run-time where the process model passes this variable. | To specify that all subproperties automatically appear in a report, set the IncludeInReport property flag on the AdditionalData property. To specify that only a subset of subproperties automatically appear in a report, set the IncludeInReport property flag on only the subproperties you want to include. | The default schemas for database logging do not automatically log any additional data. To log subproperties of the AdditionalData container, customize the schema in the Database Options dialog box and the database tables in a database management system (DBMS). |

#### NI_StationInfo Data
 Type

The NI_StationInfo data type in the default process
 models includes the subproperties described in the following table for storing
 station information. The AdditionalData container subproperty was
 added in TestStand 2013.

| Subproperty | Type | Content | How to Include in Report | How to Include in Database Logging |
| --- | --- | --- | --- | --- |
| StationID | String | Station ID | The default report generator process model plug-in automatically adds the station ID to a report. | The default schemas for database logging automatically log the station ID to the UUT_RESULT table. |
| LoginName | String | User login name | The default report generator process model plug-in automatically adds the user login name to a report. | The default schemas for database logging automatically log the user login name to the UUT_RESULT table. |
| AdditionalData | Unstructured Container | You can add subproperties of any data type to this container to store additional information associated with a station.For example, you can add subproperties to the Locals.ModelData.StationInfo.AdditionalData container in the default process model entry points at edit-time, or you can programmatically add subproperties at run-time where the process model passes this variable. | The default report generator process model plug-ins do not include any additional data in the report file. To include the subproperties of the AdditionalData container in the report, you must customize a report generator process model plug-in. | The default schemas for database logging do not automatically log any additional data. To log subproperties of the AdditionalData container, customize the schema in the Database Options dialog box and the database tables in a DBMS. |

Parent topic:

Generating and Customizing TestStand Reports

Related concepts:

- Model Callbacks in the Parallel Process Model
- Model Plugin – Pre UUT
- Model Plugin – Pre Batch
- Default TestStand Table Schemas
- UUT_RESULT Table Schema
- TestStand Database Fundamentals
- Property Flags That Affect Reports

<!--NI_TOPIC bundle=teststand path=storing-types-in-files-and-memory.html language=enus -->
## TOPIC 00845: Storing Types in Files and Memory

- bundle_id: `teststand`
- source_path: `storing-types-in-files-and-memory.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/storing-types-in-files-and-memory.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: TestStand files store the definition for each step type and data type the file uses. You can also specify that a file always saves the definition for a type, even when the file does not currently use the type. Because many files can use the same type, many files can contain the definition for the ty

### Storing Types in Files and Memory

TestStand files store the definition for each step type and data type the file uses. You can also specify that a file always saves the definition for a type, even when the file does not currently use the type. Because many files can use the same type, many files can contain the definition for the type. All sequence files, for example, might contain the definitions for the Pass/Fail Test step type and the Error standard data type.

TestStand allows only one definition for each uniquely named type in memory. The type can appear in multiple files, but only one underlying definition of the type exists in memory. When you modify the type in one file, the type definition updates in all loaded files.

Parent topic:

Type Concepts

Related concepts:

- Error and CommonResults
- Modifying Type Instances, Values, and Type Definitions

<!--NI_TOPIC bundle=teststand path=string-resource-file-format.html language=enus -->
## TOPIC 00846: String Resource File Format

- bundle_id: `teststand`
- source_path: `string-resource-file-format.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/string-resource-file-format.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: String resource files must use the .ini file extension and use the following format: [category1] tag1 = "string value 1" tag2 = "string value 2" [category2] tag1 = "string value 1" tag2 = "string value 2" When you create new entries in a string resource file or create a string resource file for cust

### String Resource File Format

String resource files must use the .ini file extension and use the following format:

```text
[category1]
tag1 = "string value 1"
tag2 = "string value 2"
```

```text
[category2]
tag1 = "string value 1"
tag2 = "string value 2"
```

When you create new entries in a string resource file or create a string resource file for custom components, use unique category names to avoid conflicts with the default names TestStand uses. For example, begin new category names with a unique ID, such as a company prefix.

You can create an unlimited number of categories and tag names. You can create strings of unlimited size, but you must break a string with more than 512 characters into multiple lines. Each line includes a LineNNNN tag suffix, where NNNN is the line number with zero padding, as shown in the following example:

```text
[category1]
tag1 Line0001 = "This is the first sentence of a long "
tag1 Line0002 = "paragraph. This is the second sentence."
```

You can use the escape codes in the following table to insert unprintable characters.

| Escape Code | Description |
| --- | --- |
| \\n | Embedded linefeed character. |
| \\r | Carriage return character. |
| \\t | Tab character. |
| \\xnn | Hexadecimal value that represents the character. For example, \\x1B represents the ASCII ESC character. |
| \\\\ | Backslash character. |
| \\" | Double quotation mark. |

Parent topic:

Creating String Resource Files

<!--NI_TOPIC bundle=teststand path=strings-in-msvc.html language=enus -->
## TOPIC 00847: Strings in Microsoft Visual C++/#import

- bundle_id: `teststand`
- source_path: `strings-in-msvc.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/strings-in-msvc.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Typically, the classes the #import directive generates use the _bstr_t class for passing and returning string values. The exception is string output parameters, which are returned as type BSTR. TestStand provides a class called param_bstr_t that includes most of the same methods as the _bstr_t class

### Strings in Microsoft Visual C++/#import

Typically, the classes the #import directive generates use the _bstr_t class for passing and returning string values. The exception is string output parameters, which are returned as type BSTR. TestStand provides a class called param_bstr_t that includes most of the same methods as the _bstr_t class and simplifies the task of receiving string output parameters.

Parent topic:

Programming with the TestStand API in Microsoft Visual C++

Related concepts:

- Utilities for Microsoft Visual C++/#import

<!--NI_TOPIC bundle=teststand path=structure-of-plug-in-sequence-files.html language=enus -->
## TOPIC 00848: Structure of Plug-in Sequence Files

- bundle_id: `teststand`
- source_path: `structure-of-plug-in-sequence-files.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/structure-of-plug-in-sequence-files.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Model plug-ins include specific entry points, entry point parameters, and data types.

### Structure of Plug-in Sequence Files

Model plug-ins include specific entry points, entry point parameters, and data types.

Parent topic:

Process Model Plug-In Architecture

Related concepts:

- Model Plug-in Entry Points
- Plug-in Entry Point Parameters

<!--NI_TOPIC bundle=teststand path=structure-of-teststand-executions.html language=enus -->
## TOPIC 00849: Structure of TestStand Executions

- bundle_id: `teststand`
- source_path: `structure-of-teststand-executions.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/structure-of-teststand-executions.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Purpose This example demonstrates the concepts of executions, threads, and call stacks and shows how they interact. The example also shows how you can use the Call Stack pane and the Threads pane to view the current status of an execution. Example File Location <TestStand Public>\Examples\Fundamenta

### Structure of TestStand Executions

#### Purpose

This example demonstrates the concepts of executions, threads, and call stacks and shows how they interact. The example also shows how you can use the Call Stack pane and the Threads pane to view the current status of an execution.

#### Example File
 Location

<TestStand
 Public>\Examples\Fundamentals\Structure of TestStand
 Executions\Structure of TestStand Executions.seq

#### Highlighted Features

- Sequence Call step type
- Call Stack pane
- Threads pane

#### Major API

None

#### Prerequisites

None

#### How to Use This
 Example

Complete the following steps to review the sequences and steps in
 the example.

1. On the Sequences pane, select the MainSequence . This
 sequence contains three Sequence Call steps, which represent three distinct
 methods of calling a subsequence.
2. Click the Call SubSequence step and navigate to the
 Module tab of the Step Settings pane. Notice that the Execution Options for this
 sequence call are set to None, which indicates that this sequence does not
 execute in a new thread or execution.
3. Click the Call NewThread step and navigate to the
 Execution Options of this step. Notice that this sequence call is set to execute
 in a new thread, which means that execution of the MainSequence continues as the
 New Thread sequence executes.
4. Click the Call NewExecution step and navigate to the
 Execution Options of this step. Notice that this sequence call is set to execute
 in a new TestStand execution, which means that TestStand manages execution of
 the NewExecution sequence independently from the current execution.

Complete the following steps to run the example.

1. Select Execute»Single Pass to run the sequence.
2. During execution, message prompts explain the structure of TestStand executions.
 After you dismiss each message, the corresponding Sequence Call step executes,
 and TestStand automatically pauses execution so you can examine each concept
 being demonstrated.
3. When you are ready to continue to the next step in the example, click the green
 Resume button on the Debug toolbar. This process
 repeats until execution completes.

Parent topic:

Examples for Fundamentals

Related concepts:

- TestStand Directory Structure

<!--NI_TOPIC bundle=teststand path=subsequence-results.html language=enus -->
## TOPIC 00850: Subsequence Results

- bundle_id: `teststand`
- source_path: `subsequence-results.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/subsequence-results.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: When a step calls a subsequence or generates a call to a callback sequence, TestStand creates a special property result of the Step.Result.TS property to store the result of the subsequence unless the callback or sequence disables results. The following table lists the name of the subproperty for ea

### Subsequence Results

When a step calls a subsequence or generates a call to a callback sequence, TestStand creates a special property result of the Step.Result.TS property to store the result of the subsequence unless the callback or sequence disables results. The following table lists the name of the subproperty for each type of subsequence call.

| Result Subproperty Name | Type of Subsequence Call |
| --- | --- |
| TS.SequenceCall | Sequence Call |
| TS.PostAction | Post Action callback |
| TS.SequenceFilePreStep | SequenceFilePreStep callback |
| TS.SequenceFilePostStep | SequenceFilePostStep callback |
| TS.ProcessModelPreStep | ProcessModelPreStep callback |
| TS.ProcessModelPostStep | ProcessModelPostStep callback |
| TS.StationPreStep | StationPreStep callback |
| TS.StationPostStep | StationPostStep callback |
| TS.SequenceFilePreInteractive | SequenceFilePreInteractive callback |
| TS.SequenceFilePostInteractive | SequenceFilePostInteractive callback |
| TS.ProcessModelPreInteractive | ProcessModelPreInteractive callback |
| TS.ProcessModelPostInteractive | ProcessModelPostInteractive callback |
| TS.StationPreInteractive | StationPreInteractive callback |
| TS.StationPostInteractive | StationPostInteractive callback |
| TS.SequenceFilePostResultListEntry | SequenceFilePostResultListEntry callback |
| TS.ProcessModelPostResultListEntry | ProcessModelPostResultListEntry callback |
| TS.StationPostResultListEntry | StationPostResultListEntry callback |
| TS.SequenceFilePostStepRuntimeError | SequenceFilePostStepRuntimeError callback |
| TS.ProcessModelPostStepRuntimeError | ProcessModelPostStepRuntimeError callback |
| TS.StationPostStepRuntimeError | StationPostStepRuntimeError callback |
| TS.SequenceFilePostStepFailure | SequenceFilePostFailure callback |
| TS.ProcessModelPostStepFailure | ProcessModelPostStepFailure callback |
| TS.StationPostStepFailure | StationPostStepFailure callback |

TestStand adds the following properties to the subproperty for each subsequence:

- ThreadID —ID of the thread used to execute the sequence.
- SequenceFile —Absolute path of the sequence file that contains the subsequence.
- SequenceFileVersion —Version of the sequence file that contains the subsequence.
- Sequence —Name of the subsequence the step called.
- Status —Status of the subsequence the step called.
- ResultList —Value of Locals.ResultList for the subsequence the step called. This property contains the results for the steps in the subsequence.

Parent topic:

Result Collection

Related concepts:

- Callback Sequences
- List of Engine Callbacks
- Result Collection
- Custom Result Properties

<!--NI_TOPIC bundle=teststand path=supporting-post-failure-information-recovery.html language=enus -->
## TOPIC 00851: Supporting Post-Failure Information Recovery

- bundle_id: `teststand`
- source_path: `supporting-post-failure-information-recovery.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/supporting-post-failure-information-recovery.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: In the case of a catastrophic failure, analyzing step result information collected during the execution might be a critical component of the troubleshooting process. You can configure TestStand to generate reports on-the-fly while testing a unit under test (UUT). By default, TestStand generates and

### Supporting Post-Failure Information Recovery

In the case of a catastrophic failure, analyzing step result information collected during the execution might be a critical component of the troubleshooting process.

You can configure TestStand to generate reports on-the-fly while testing a unit under test (UUT). By default, TestStand generates and persists the on-the-fly report after collecting 500 step results or after every 1.5 seconds of execution time, whichever occurs first. Logging reports to disk can be slow and negatively impact throughput.

In some cases, you can improve performance by changing the values of the Processing Interval or the Maximum Number of Results options in the Advanced Result Processing Settings dialog box. You can also improve performance by enabling the Only Display Latest Results option on the Contents tab of the Report Options dialog box.

NI benchmarks show that TSR reports provide better throughput while generating an on-the-fly
 report.

#### Recommended Report
 Options

The following table summarizes the recommended options you
 configure in the Report Options dialog box when you optimize for post-failure
 information recovery:

| Report Option | Value |
| --- | --- |
| Format | TSR*, ATML, XML, ASCII, HTML (best to worst) |
| Asynchronous | N/A |
| On-the-Fly Report | True |
| Only Display Latest Results | True |

Note

#### Tradeoffs

Consider the
 impact to the following requirements when you optimize for post-failure information
 recovery:

- Maximize test system throughput
- Interoperate with other processes and systems
- Generate and view the report during test sequence execution

Parent topic:

Choosing the Appropriate Report Generation Strategy

Related concepts:

- Maximizing Test System Throughput
- Interoperating with Other Processes and Systems
- Generating and Viewing the Report during Test Sequence Execution
- Generating the Report for the Current UUT before Testing the Next UUT
- On-the-Fly Report Generation

<!--NI_TOPIC bundle=teststand path=sweep-loop-strategies.html language=enus -->
## TOPIC 00852: Sweep Loop Strategies

- bundle_id: `teststand`
- source_path: `sweep-loop-strategies.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/sweep-loop-strategies.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Example File Location <TestStand Public>\Examples\Fundamentals\Using Sweep Loops\Sweep Loop Strategies Demo\Sweep Loop Strategies.seq Highlighted Features Sweep Loops Major API SetBreakSettings Prerequisites None How to Use This Example Complete the following steps to run the example: Select Execute

### Sweep Loop Strategies

#### Example File
 Location

<TestStand
 Public>\Examples\Fundamentals\Using Sweep Loops\Sweep Loop
 Strategies Demo\Sweep Loop Strategies.seq

#### Highlighted Features

- Sweep Loops

#### Major API

- SetBreakSettings

#### Prerequisites

None

#### How to Use This Example

Complete the following steps to run the example:

1. Select Execute»Run Mainsequence to execute the sequence
2. When the first breakpoint is hit, ensure that Locals.SweepLoopParameterValues is added to the Watch Window during execution.
3. At each breakpoint, observe the difference in the sweep loop strategies. The strategy for ConstantValue resets the variables value to the value set in the parameters list of the sweep loop even though it is incremented during an iteration of the loop. The strategy for CaptureValue retains the new value when a new iteration of the loop starts.

Parent topic:

Using Sweep Loops

Related concepts:

- TestStand Directory Structure

<!--NI_TOPIC bundle=teststand path=switch-executive.html language=enus -->
## TOPIC 00853: Switch Executive

- bundle_id: `teststand`
- source_path: `switch-executive.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/switch-executive.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Description This example demonstrates how to use TestStand to integrate and perform switching operations with NI Switch Executive. Example File Location <TestStand Public>\Examples\Interfacing with Hardware\Switch Executive\Switch Executive.seq Highlighted Features NI Switch Executive integration IV

### Switch Executive

#### Description

This example demonstrates how to use TestStand to integrate and perform switching operations with NI Switch Executive.

#### Example File
 Location

<TestStand
 Public>\Examples\Interfacing with Hardware\Switch Executive\Switch
 Executive.seq

#### Highlighted Features

- NI Switch Executive integration
- IVI Switch step type
- Switching panel

#### Major API

None

#### Prerequisites

This example assumes you have installed a release or evaluation version of NI Switch Executive. This example also assumes the SwitchExecutiveExample virtual device exists and the SampleMatrix1 and SampleMatrix2 IVI logical names are configured to run in simulation mode.

The virtual device is created when you install NI Switch Executive. If the device and/or logical names have been removed, you can recover them by performing the following steps:

1. Open the Windows command line and type cd <National Instruments>/switch
 executive , where <National Instruments> is
 the NI directory, which is C:\Program Files (x86)\National
 Instruments by default.
2. Enter the command SwitchExecutive s to recreate the virtual device and logical names.

#### How to Use This Example

The sequence performs switching operations using the Switching panel on the Properties tab of the Step Settings pane and the IVI Switch step type. Using the Switching panel, any step can perform switching operations while the step executes or perform switching setup for subsequent steps.

You can monitor IVI switching operations by launching NI I/O Trace prior to running this example. You must enable tracing of calls to the IVI Switch API.

Visit ni.com/ivi for more information about IVI.

Parent topic:

Examples for Interfacing with Hardware

Related concepts:

- TestStand Directory Structure

<!--NI_TOPIC bundle=teststand path=switch-vis-ppls.html language=enus -->
## TOPIC 00854: Switching between VIs and Packed Project Libraries

- bundle_id: `teststand`
- source_path: `switch-vis-ppls.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/switch-vis-ppls.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `task`
- source_description: The LabVIEW Adapter allows you to easily switch the configuration of a step between executing a VI and executing a VI in a packed project library without having to modify the step. You can also configure the LabVIEW Adapter to automatically build a missing or out-of-date packed project library at th

### Switching between VIs and Packed Project
 Libraries

The LabVIEW Adapter allows you to easily switch the configuration of a step between
 executing a VI and executing a VI in a packed project library without having to modify the
 step. You can also configure the LabVIEW Adapter to automatically build a missing or
 out-of-date packed project library at the start of execution.

In previous versions of TestStand, after
 you build the packed project library in LabVIEW, you would have to modify the step to
 point to the VI in the packed project library. Now, if the step is configured to call a
 VI in the context of a project and the project has a build specification configured to
 build a packed project library containing that VI, you can choose to execute the VI in
 the packed project library instead of the VI.

1. Set the following settings in the Override Module Settings
 window for a step calling a VI:
  1. Select the build specification for the VI.
  2. Set the path of the VI in the packed project library.
  3. Optional: Set the path of the project to use when executing the VI in
 the packed project library.
2. Enable the Always run VI in Packed Project Library
 option in the LabVIEW Adapter Configuration dialog box or
 step settings. 
 Note Enabling Always run VI in Packed Project Library in
 the LabVIEW Adapter Configuration dialog box overrides
 the module settings for all LabVIEW steps and always run the VI in the
 packed project library. You must configure the VI settings in the
 Override Module Settings window to yse this
 option.
 Note 
 The LabVIEW Adapter will automatically run the VI in the packed project
 library and project configured in the Override Module
 Settings window instead of the VI and project configured in the
 step.
3. If LabVIEW Development System is installed, you can enable automatically
 building the packed project library at the start of execution by enabling the
 Automatically Build Packed Project Libraries at the Start of
 Execution option in the LabVIEW Adapter
 Configuration dialog box.

Parent topic:

LabVIEW Adapter

<!--NI_TOPIC bundle=teststand path=symmetric-multiprocessing-in-vis-executed-fro.html language=enus -->
## TOPIC 00855: Symmetric Multiprocessing in VIs Executed from TestStand

- bundle_id: `teststand`
- source_path: `symmetric-multiprocessing-in-vis-executed-fro.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/symmetric-multiprocessing-in-vis-executed-fro.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: LabVIEW can use multiple execution threads to execute VIs called from TestStand. Executing VIs with multiple threads can improve performance on multi-core and multi-processor systems, particularly when the VIs contain complex data flows, such as parallel loops, branched wires, or asynchronous commun

### Symmetric Multiprocessing in VIs Executed
 from TestStand

LabVIEW can use multiple
 execution threads to execute VIs called from TestStand. Executing VIs with multiple
 threads can improve performance on multi-core and multi-processor systems,
 particularly when the VIs contain complex data flows, such as parallel loops,
 branched wires, or asynchronous communication with hardware devices.

When
 TestStand calls a VI, the number of execution threads LabVIEW uses to run the VI
 depends on the following factors:

- Whether you enable the Execute ‘Same as caller’ VIs Using Multiple Threads
 option in the LabVIEW Adapter Configuration dialog box
- The setting of the Preferred Execution System option on the Execution page of
 the VI Properties dialog box in LabVIEW
- The version of LabVIEW that executes the VI

Note

- By default, in scenarios that do not include TestStand, LabVIEW uses
 multiple threads to execute VIs if the preferred execution system of the VIs
 is not set to user interface .
- LabVIEW always uses a single thread to execute VIs for which the preferred
 execution system is user interface . NI strongly
 discourages using the user interface preferred
 execution system for VIs you call from TestStand. The remainder of
 information in this topic excludes consideration of the user
 interface preferred execution system.

#### LabVIEW 2009 or Later

The
 following table shows how these factors apply when you execute VIs using the LabVIEW
 2009 or later development system or Run-Time Engine (RTE).

| LabVIEW Setting:Preferred Execution System | TestStand Option:Execute 'Same as caller' VIs Using Multiple Threads |  |
| --- | --- | --- |
| Enabled | Disabled |  |
| same as caller | Multiple threads | Single thread |
| Not same as caller | Multiple threads | Multiple threads |

#### LabVIEW 8.6.1 or
 Earlier

The following shows how these factors apply when you execute VIs
 using the LabVIEW 8.6.1 or earlier development system or RTE.

| LabVIEW Setting:Preferred Execution System | TestStand Option:Execute 'Same as caller' VIs Using Multiple Threads |  |
| --- | --- | --- |
| Enabled | Disabled |  |
| same as caller | Single thread | Single thread |
| Not same as caller | Multiple threads | Multiple threads |

#### Configuring CPU Affinity and the
 Number of LabVIEW RTE Execution Threads

Using the LabVIEW Adapter, you can
 configure the CPU affinity for LabVIEW development system or RTE execution threads,
 and you can configure and the number of execution threads the LabVIEW RTE uses to
 execute VIs. You can adjust these settings to optimize performance for a particular
 system.

Parent topic:

Effectively Using LabVIEW with TestStand

Related concepts:

- Programming with the TestStand API in LabVIEW
- Configuring the CPU Affinity for LabVIEW Execution Threads
- Configuring the Number of LabVIEW RTE Execution Threads
- Using TestStand on SMP Systems

<!--NI_TOPIC bundle=teststand path=synchronization-object-support-for-64-bit-tes.html language=enus -->
## TOPIC 00856: Synchronization Object Support for 64-bit TestStand

- bundle_id: `teststand`
- source_path: `synchronization-object-support-for-64-bit-tes.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/synchronization-object-support-for-64-bit-tes.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use a prefix to share synchronization objects between 32-bit TestStand and 64-bit TestStand. When the synchronization object name begins with an asterisk or computer name, you can use a 32 or 64 prefix to specify using 32-bit TestStand or 64-bit TestStand to host the out-of-process synchroni

### Synchronization Object Support for 64-bit TestStand

You can use a prefix to share synchronization objects between 32-bit TestStand and 64-bit TestStand. When the synchronization object name begins with an asterisk or computer name, you can use a 32 or 64 prefix to specify using 32-bit TestStand or 64-bit TestStand to host the out-of-process synchronization object. For example, the name 64*syncobj specifies a synchronization object called *syncobj in the 64-bit TestStand Synchronization Server, even when used from 32-bit TestStand. If you do not use a bitness prefix, 32-bit TestStand hosts out-of-process synchronization objects in a 32-bit process, and 64-bit TestStand hosts out-of-process synchronization objects in a 64-bit process.

Note

64

Parent topic:

64-bit TestStand and Migrating from 32-bit TestStand

<!--NI_TOPIC bundle=teststand path=synchronization-step-types-auto-schedule.html language=enus -->
## TOPIC 00857: Synchronization Step Types - Auto Schedule

- bundle_id: `teststand`
- source_path: `synchronization-step-types-auto-schedule.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/synchronization-step-types-auto-schedule.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Purpose This example demonstrates the Auto Schedule and Use Auto Scheduled Resource step types. These step types are used to dynamically determine the order in which a UUT uses its required resources to minimize delays that occur while the UUT waits for a resource to become available. Example File L

### Synchronization Step Types - Auto Schedule

#### Purpose

This example demonstrates the Auto Schedule and Use Auto Scheduled Resource step types. These step types are used to dynamically determine the order in which a UUT uses its required resources to minimize delays that occur while the UUT waits for a resource to become available.

#### Example File
 Location

<TestStand
 Public>\Examples\Built-In Step Types\Synchronization Step
 Types\Synchronization Step Types - Auto Schedule.seq

#### Highlighted Features

- Auto Schedule step type
- Use Auto Scheduled Resource step type
- Batch process model

#### Major API

None

#### Prerequisites

None

#### How to Use This Example

Complete the following steps to review the sequences and steps in the example.

1. On the Sequences pane, select the MainSequence . The Auto Schedule step at the beginning of the test defines a block of Use Auto Scheduled Resource sub-blocks. When the test sequence executes, each test socket executes each Use Auto Scheduled Resource sub-block once. The order in which the sub-blocks execute can vary between test sockets to improve execution time.
2. Select one of the Use Auto Scheduled Resource steps and navigate to the Auto Scheduled Resource Settings Edit Tab on the Step Settings pane. Notice that at least one resource name is defined in the Resource Lock Alternatives list. The UUT does not execute the test steps in this Use Auto Scheduled Resource sub-block until it has exclusive access to the resources in this list.
3. Select each of the Use Auto Scheduled Resource steps to compare the settings for the Resource Lock Alternatives. You can specify multiple resource lock alternatives to indicate that the sub-block can execute if any of the alternatives are available. To lock access to all of these resources before executing the sub-block, use an array of lock names to specify that a section must lock multiple resources. In this case, no locks are reserved unless all resources are available.

Complete the following steps to run the example.

1. Select Execute»Single Pass to run the sequence.
2. A prompt appears that describes the Resource Usage Profiler, which is a tool to monitor the status of synchronization objects in a test sequence. You can use this tool to observe the execution order of test steps in a test sequence with Auto Schedule steps. You can choose to launch the tool to view additional details during the test.
3. As the test sequence executes, dialog boxes indicate the current status of the tests. Notice that each UUT is only able to execute a Use Auto Scheduled Resource sub-block if it is able to gain exclusive access to the required resources.
4. Once execution completes, you can examine the test report for each UUT to notice the order of execution. The Auto Schedule steps do not guarantee a specific execution order for each test step. The order can vary among test sockets and among executions. You can run the test sequence additional times to compare the execution order among different test runs.

Parent topic:

Examples for Built-In Step Types

Related concepts:

- TestStand Directory Structure
- Batch Process Model

<!--NI_TOPIC bundle=teststand path=synchronization-step-types-batch-synchronizat.html language=enus -->
## TOPIC 00858: Synchronization Step Types - Batch Synchronization

- bundle_id: `teststand`
- source_path: `synchronization-step-types-batch-synchronizat.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/synchronization-step-types-batch-synchronizat.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Purpose This example demonstrates the Batch Synchronization step types and step settings available when you use the Batch process model. Use Batch synchronization to coordinate test operations among all test sockets in a batch and and to execute test steps selectively, concurrently, or sequentially.

### Synchronization Step Types - Batch Synchronization

#### Purpose

This example demonstrates the Batch Synchronization step types and step settings available when you use the Batch process model. Use Batch synchronization to coordinate test operations among all test sockets in a batch and and to execute test steps selectively, concurrently, or sequentially.

#### Example File
 Location

<TestStand
 Public>\Examples\Built-In Step Types\Synchronization Step
 Types\Synchronization Step Types - Batch
 Synchronization.seq

#### Highlighted Features

- Batch Synchronization step type
- Batch Synchronization step settings
- Batch process model

#### Major API

None

#### Prerequisites

None

#### How to Use This
 Example

Complete the following steps to review the sequences and steps in
 the example.

1. On the Sequences pane, select the MainSequence . The
 MainSequence contains four Sequence Call steps that correspond to the different
 approaches demonstrated in this example. When executed, the Batch process model
 executes four instances of this sequence, referred to as sockets 0 through
 3.
2. On the Sequences pane, select the Voltage Tests sequence.
 This sequence uses the Batch Synchronization step settings to synchronize
 execution of individual steps. Observe that the two Apply Voltage Stimulus steps
 enable the One thread only option on the Synchronization
 pane of the step settings, indicating that only a single test socket execute
 these steps during execution. The two Voltage Response steps enable the
 Parallel option on the Synchronization pane of the
 step settings, indicating that all test sockets execute these steps
 concurrently.
3. On the Sequences pane, select the Temperature Tests 
 sequence. This sequence uses the Batch Synchronization step type to define a
 block of steps that execute serially, meaning that only one socket executes each
 test at a time but that all sockets execute both test steps. Execution does not
 continue beyond the Batch Synchronization block until all sockets have completed
 the block.
4. On the Sequences pane, select the Stress Tests sequence.
 This sequence uses the Batch Synchronization step type to define blocks of steps
 that execute in parallel. For each block, all test sockets concurrently execute
 the test steps. Execution does not continue beyond the block until all sockets
 have completed all test steps within the block.
5. On the Sequences pane, select the Current Tests sequence.
 The steps in this sequence do not have any Batch Synchronization settings
 applied, meaning that each test socket executes these steps as soon as the
 execution reaches this sequence. It is not necessary to specify Batch
 Synchronization settings for every step in a sequence file using the Batch
 process model.

Complete the following steps to run the example.

1. Select Execute»Single Pass to run the sequence.
2. As the test sequence executes, dialog boxes indicate the current status of the
 tests. Notice that the tests execute concurrently, serially, or only on a single
 socket according to the Batch Synchronization settings for each step.

Parent topic:

Examples for Built-In Step Types

Related concepts:

- Batch Process Model
- TestStand Directory Structure

<!--NI_TOPIC bundle=teststand path=synchronization-step-types-lock.html language=enus -->
## TOPIC 00859: Synchronization Step Types - Lock

- bundle_id: `teststand`
- source_path: `synchronization-step-types-lock.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/synchronization-step-types-lock.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Purpose This example demonstrates how to use the Lock synchronization step to restrict execution flow in a sequence file that uses the Batch process model. When a lock is active, only one thread at a time can access the steps the lock contains. Example File Location <TestStand Public>\Examples\Built

### Synchronization Step Types - Lock

#### Purpose

This example demonstrates how to use the Lock synchronization step to restrict execution flow in a sequence file that uses the Batch process model. When a lock is active, only one thread at a time can access the steps the lock contains.

#### Example File
 Location

<TestStand
 Public>\Examples\Built-In Step Types\Synchronization Step
 Types\Synchronization Step Types - Lock.seq

#### Highlighted Features

- Batch process model
- Lock step type

#### Major API

None

#### Prerequisites

None

#### How to Use This Example

Complete the following steps to review the sequence functionality.

1. Select Edit»Sequence File Properties to launch the Sequence File Properties dialog box. On the Advanced tab, the Model File control specifies the Batch process model, which will run the test sequence in multiple parallel executions (test sockets).
2. On the Sequences pane, select the MainSequence .
3. Review the steps in the MainSequence . The steps specify the following behaviors:
  - The sequence uses Lock steps to ensure that only one test socket is executing the single-threaded steps at a given time, which is useful in cases where the step requires a shared resource, such as an instrument, that only one step at a time can use.
  - In section one, the sequence first creates and then performs the lock operation in the Create and Lock "Lock 1" step. Once one test socket calls the Lock "Lock 1" step, all other test sockets wait at the step until the original socket releases the lock in the Unlock "Lock 1" step.
  - In section three, for the Single-threaded Test 5 step, notice that the Synchronization panel of the Properties tab of the Step Settings pane contains a Use Lock to Allow Only One Thread at a Time to Execute the Step option, which is enabled. This option applies a lock for the step without the need for lock steps.
  - In section four, the Create Lock step stores the lock reference in a local variable. The lock operation uses this variable to identify the lock, and stores a reference to the lock operation in a second variable.

Complete the following steps to run this example.

1. Select the Execute menu and confirm that a checkmark appears next to the Tracing Enabled option.
2. Select Execute»Single Pass to run the sequence. TestStand creates three test sockets, and each test socket executes the MainSequence . The multi-threaded steps execute simultaneously across all test sockets. Observe that the locked code runs only on a single socket at any given time.

Parent topic:

Examples for Built-In Step Types

Related concepts:

- Batch Process Model
- TestStand Directory Structure

<!--NI_TOPIC bundle=teststand path=synchronization-step-types-notification-and-w.html language=enus -->
## TOPIC 00860: Synchronization Step Types - Notification and Wait

- bundle_id: `teststand`
- source_path: `synchronization-step-types-notification-and-w.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/synchronization-step-types-notification-and-w.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Purpose This example demonstrates how to use the Notification and Wait synchronization steps in a sequence file to specify that one test socket waits to receive a notification from another step before continuing the execution. A Notification step can send messages between multiple test sockets and c

### Synchronization Step Types - Notification and Wait

#### Purpose

This example demonstrates how to use the Notification and Wait synchronization steps in a sequence file to specify that one test socket waits to receive a notification from another step before continuing the execution. A Notification step can send messages between multiple test sockets and can optionally contain data.

#### Example File
 Location

<TestStand
 Public>\Examples\Built-In Step Types\Synchronization Step
 Types\Synchronization Step Types - Notification &
 Wait.seq

#### Highlighted Features

- Notification step type
- Wait step type

#### Major API

None

#### Prerequisites

None

#### How to Use This Example

Complete the following steps to review the sequence functionality.

1. On the Sequences pane, select the MainSequence .
2. Complete the following steps to review the steps in the MainSequence .
  1. Select the Notification step. On the Notification Settings edit tab, notice that the Create operation is selected. This step creates a new notification and names it "Event 1".
  2. Select the Wait for Notification step. On the Notification Settings edit tab, notice that the Wait operation is selected. This step waits until TestStand calls the Set operation on the "Stimulus Started" notification from the "Start Stimulus" execution. On the Preconditions panel of the Properties tab of the Step Settings pane, the Precondition Expression control contains an expression that ensures that only Test Socket 1 waits for the notification. The other test socket skips this step.
  3. Open the Start Stimulus sequence. Select the Initialize Stimulus step. The Wait Settings edit tab specifies that the Wait step introduces a 2-second delay in the sequence to simulate starting the stimulus.
  4. Select the Set "Stimulus Starting" Notification step. On the Notification Settings edit tab, notice that the Set operation is selected. This step sends the notification. If another thread is waiting for the notification, that thread may now continue execution.

Complete the following steps to run this example.

1. Select Execute»Single Pass to run the sequence.
2. Notice that the main execution waits for the initialization to complete before entering the Main step group.
3. 2.3. Notice that the Wait for "Stimulus Started" Notification step does not complete until the “Start Stimulus” sequence sets the notification indicating that the stimulus has started.

Parent topic:

Examples for Built-In Step Types

Related concepts:

- TestStand Directory Structure

<!--NI_TOPIC bundle=teststand path=synchronization-step-types-queue.html language=enus -->
## TOPIC 00861: Synchronization Step Types - Queue

- bundle_id: `teststand`
- source_path: `synchronization-step-types-queue.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/synchronization-step-types-queue.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Purpose This example demonstrates how to use the Queue synchronization step in a sequence file that uses the Batch process model. You can use a Queue step to pass data between threads or across executions while avoiding race conditions. Example File Location <TestStand Public>\Examples\Built-In Step

### Synchronization Step Types - Queue

#### Purpose

This example demonstrates how to use the Queue synchronization step in a sequence file that uses the Batch process model. You can use a Queue step to pass data between threads or across executions while avoiding race conditions.

#### Example File
 Location

<TestStand
 Public>\Examples\Built-In Step Types\Synchronization Step
 Types\Synchronization Step Types - Queue.seq

#### Highlighted Features

- Batch process model
- Queue step type

#### Major API

None

#### Prerequisites

None

#### How to Use This Example

The Queue step is similar to a Notification step in that you can send data between multiple test sockets. Queue steps can contain multiple data values. This example demonstrates how to complete the following tasks for a queue:

- Enqueue —Add an element to a queue.
- Dequeue —Remove an element from a queue or store the data from the element.
- Get Status —Obtain information about the current state of the queue.
- Flush —Empty the queue and optionally obtain all the elements from the queue.

Complete the following steps to review the sequence functionality.

1. Select Edit»Sequence File Properties to launch the Sequence File Properties dialog box.
2. On the Sequences pane, select the MainSequence .
3. Complete the following steps to review the steps in the MainSequence .
  1. In section one, select the Create Queue 1 step. On the Queue Settings edit tab, notice that the Create operation is selected. This step creates a new queue named "Queue 1".
  2. Select the Enqueue One Element sequence, then select the Enqueue Data step. On the Queue Settings edit tab, notice that the Enqueue operation is selected. This step adds a new element, the value of the Locals.EnqueueData variable, to the queue.
  3. Select the Dequeue Data step. On the Queue Settings edit tab, notice that the Dequeue operation is selected. This step removes an element from the queue. If the queue is empty, the step waits until data is available to dequeue, as shown in section two.
  4. In section three, select the Get Status step. This step uses the Get Status operation places the current contents of the queue into the Locals.QueueStatus variable without modifying the state of the queue.
  5. Select the Flush Queue step. On the Queue Settings edit tab, notice that the Flush operation is selected. This step removes all data from the queue. TestStand places the data in the location specified in the Location to Store Array of Queue Elements control. In this case, TestStand places the data in the Locals.FlushedQueue variable.

Complete the following steps to run this example.

1. Select Execute»Single Pass to run the sequence.
2. Read the text in each section popup message for information about the behavior of that section.

Parent topic:

Examples for Built-In Step Types

Related concepts:

- Batch Process Model
- TestStand Directory Structure
- Synchronization Step Types - Notification and Wait

<!--NI_TOPIC bundle=teststand path=synchronization-step-types-rendezvous-and-sem.html language=enus -->
## TOPIC 00862: Synchronization Step Types - Rendezvous and Semaphore

- bundle_id: `teststand`
- source_path: `synchronization-step-types-rendezvous-and-sem.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/synchronization-step-types-rendezvous-and-sem.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Purpose This example demonstrates how to use the Rendezvous and Semaphore synchronization steps to control multi-threaded execution flow between threads or across executions in a sequence file that uses the Batch process model. A Rendezvous step will make a set number of threads wait until all threa

### Synchronization Step Types - Rendezvous and Semaphore

#### Purpose

This example demonstrates how to use the Rendezvous and Semaphore synchronization steps to control multi-threaded execution flow between threads or across executions in a sequence file that uses the Batch process model.

- A Rendezvous step will make a set number of threads wait until all threads specified are at the same point and ready to proceed. Unlike batch synchronization, rendezvous steps can be used to synchronize any TestStand threads or executions, without requiring the batch process model.
- A Semaphore step is similar to the Lock step in functionality, except that you can specify any number of threads instead of just one.

#### Example File
 Location

<TestStand
 Public>\Examples\Built-In Step Types\Synchronization Step
 Types\Synchronization Step Types - Rendezvous &
 Semaphore.seq

#### Highlighted Features

- Batch process model
- Rendezvous step type
- Semaphore step type

#### Major API

None

#### Prerequisites

None

#### How to Use This Example

This example uses the Rendezvous or Semaphore steps to synchronize four test sockets in a batch test.

Complete the following steps to review the sequence functionality.

1. Select Edit»Sequence File Properties to launch the Sequence File Properties dialog box. On the Advanced tab, the Model File control specifies the Batch process model, which will run the test sequence in multiple parallel executions (test sockets).
2. On the Sequences pane, select the MainSequence .
3. Complete the following steps to review the steps in the MainSequence .
  1. Select the Create Semaphore 1 step. On the Semaphore Settings edit tab, notice that the Create operation is selected. This step creates a new semaphore named "Semaphore 1". The Initial Semaphore Count control specifies a value of 2 , which indicates that two test sockets can execute the semaphore section at any given time. The Acquire Semaphore 1 step and Release Semaphore 1 step represent the start and end of the semaphore section.
  2. Select the Create Rendezvous 1 step. On the Rendezvous Settings edit tab, notice that the Create operation is selected. This step creates a new rendezvous named "Rendezvous 1". The Number of Threads per Rendezvous control specifies a value of 4 , which indicates that when one test socket reaches the Start Rendezvous step, the socket waits for the other three sockets before continuing execution.

Complete the following steps to run this example.

1. Select Execute»Single Pass to run the sequence. TestStand creates four test sockets, and each test socket executes the MainSequence . When the executions reach the Acquire Semaphore 1 step, two test sockets enter the semaphore section and the remaining two sockets wait. When the first two test sockets execute the Release Semaphore 1 step, the remaining two test sockets enter the semaphore section. When the test sockets reach the Rendezvous step, the test sockets wait until all test sockets reach the step before execution continues.

Parent topic:

Examples for Built-In Step Types

Related concepts:

- Batch Process Model
- TestStand Directory Structure

<!--NI_TOPIC bundle=teststand path=synchronized-sections.html language=enus -->
## TOPIC 00863: Synchronized Sections

- bundle_id: `teststand`
- source_path: `synchronized-sections.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/synchronized-sections.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Place a Batch Synchronization step at the beginning of a section of steps in a sequence and specify an Enter operation for the step. Place another Batch Synchronization step at the end of the section of steps and specify an Exit operation for the step. You must place the Enter and Exit steps in the

### Synchronized Sections

Place a Batch Synchronization step at the beginning of a section of steps in a sequence and specify an Enter operation for the step. Place another Batch Synchronization step at the end of the section of steps and specify an Exit operation for the step. You must place the Enter and Exit steps in the same sequence file, but you do not have to place the Enter and Exit steps in the same step group.

Each thread in a batch that enters a synchronized section blocks at the Enter step until all the other threads in the batch arrive at their respective instances of the Enter step. A thread cannot re-enter a section it has already entered. Each thread in a batch that reaches the end of the synchronized section blocks at the Exit step until all the other threads in the batch arrive at their respective instances of the Exit step.

You can use the following types of synchronized sections in sequence files:

- Serial —Use a Serial section to ensure that each thread in the batch executes the steps in the section sequentially and in the order you specify when you create the batch. When all threads in a batch arrive at their respective instances of an Enter step for a Serial section, TestStand releases one thread at a time in ascending order according to the order numbers you assign to the threads when you use a Batch Specification step to add the threads to the batch. As each thread reaches the Exit step for the section, the next thread in the batch proceeds from the Enter step. After all the threads in the batch arrive at the Exit step, the threads exit the section together.
- Parallel —Use a Parallel section to run each thread independently. When all threads in a batch arrive at their respective instances of an Enter step for a Parallel section, TestStand releases all the threads at once. As each thread reaches the Exit step for the section, the thread blocks until all the threads in the batch reach the Exit step. After all the threads in the batch arrive at the Exit step, the threads exit the section together.
- One Thread Only —Use a One Thread Only section to specify that only one thread in the batch executes the steps in the section. Typically, you use this type of section to perform an operation that applies to the batch as a whole, such as raising the temperature in a test chamber. When all threads in a batch arrive at their respective instances of an Enter step for a One Thread Only section, TestStand releases only one thread. When that thread arrives at the Exit step for the section, all remaining threads in the batch jump from the Enter step to the Exit step, skipping the steps within the section. All the threads in the batch exit the section together.
 
 Note 

 For nested sections, TestStand ignores the inner section when the type of the outer section is set to One Thread Only.

Parent topic:

Using the Synchronization Step Type

Related information:

- Batch Specification Step
- Batch Synchronization Step
- Semaphore Step

<!--NI_TOPIC bundle=teststand path=tcp-ports-for-the-labview-runtimes.html language=enus -->
## TOPIC 00864: TCP Ports for the LabVIEW Runtimes

- bundle_id: `teststand`
- source_path: `tcp-ports-for-the-labview-runtimes.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/tcp-ports-for-the-labview-runtimes.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: When the Enable Debugging and Tracing LabVIEW Adapter option is enabled, all LabVIEW Runtimes 2015 and later loaded by TestStand open a TCP port. The DETT uses this TCP port to trace VIs executed in the LabVIEW Runtimes. You can obtain the port number for a specific LabVIEW Runtime by clicking the T

### TCP Ports for the LabVIEW Runtimes

When the Enable Debugging and Tracing LabVIEW Adapter option is enabled, all LabVIEW Runtimes 2015 and later loaded by TestStand open a TCP port. The DETT uses this TCP port to trace VIs executed in the LabVIEW Runtimes.

You can obtain the port number for a specific LabVIEW Runtime by clicking the TCP Ports button in the LabVIEW Adapter Configuration dialog box.

Note

Parent topic:

Tracing with the DETT

<!--NI_TOPIC bundle=teststand path=template-files-for-different-development-envi.html language=enus -->
## TOPIC 00865: Template Files for Different Development Environments

- bundle_id: `teststand`
- source_path: `template-files-for-different-development-envi.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/template-files-for-different-development-envi.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Because different module adapters require different types of code modules, code templates typically correspond to a particular programming language in a specific development environment. The <TestStand>\CodeTemplates directory includes the default code templates for each development environment, as

### Template Files for Different Development Environments

Because different module adapters require different types of code modules, code templates typically correspond to a particular programming language in a specific development environment. The <TestStand>\CodeTemplates directory includes the default code templates for each development environment, as the following table describes.

| Subdirectory Name | Template Description |
| --- | --- |
| Default_Template | Legacy default template |
| DefaultC++.NET | Default template for C++ in Microsoft Visual Studio |
| DefaultCSharp.NET | Default template for C# in Visual Studio |
| DefaultCVI | Default template for C in LabWindows/CVI |
| DefaultHTB72_Template | Default template for HTBasic 7.2 |
| DefaultHTB80_Template | Default template for HTBasic 8.0 |
| DefaultLabVIEW | Default template for LabVIEW |
| DefaultVB.NET | Default template for Microsoft Visual Basic .NET |
| DefaultVC++_Template | Default template for C++ in Visual Studio |

Each subdirectory includes the source file for the module adapter and a .ini file that contains parameter information and a description string TestStand displays for the code template. TestStand uses the directory names from the <TestStand>\CodeTemplates or <TestStand Public>\CodeTemplates directory as the code template name to display in the Code Templates tab of the Step Type Properties dialog box.

Code templates for the LabVIEW, LabWindows/CVI, and C/C++ DLL Adapters can have any number of parameters compatible with the data types you can specify on the Module tab of the Step Settings pane for those adapters.

When TestStand uses a code template for a DLL to create skeleton code, it compares the parameter list in the source file to the parameter information on the Module tab. When these two sources of information do not match, TestStand prompts you to select which prototype to use for the skeleton code. When you use the prototype from the template source file, TestStand updates the Module tab to match the prototype in the template source file. However, the template source file does not contain sufficient information for TestStand to update the Value controls for the parameters on the Module tab. Use the Parameter Name/Value Mappings section of the Edit Code Template dialog box to specify entries for TestStand to place in the Value controls. TestStand stores the parameter values in the .ini file in the template subdirectory.

#### Legacy Code Templates

In TestStand 3.5 or earlier, code template directories contain source files for multiple development environments. For example, a legacy code template directory might include one .c file for the LabWindows/CVI Adapter and multiple VIs for the LabVIEW Adapter, where each VI corresponds to the different combinations of parameter options users can set in the Edit LabVIEW VI Call dialog box. TestStand includes these legacy code templates to provide compatibility with previous versions of TestStand. The [TemplateType] section of the config.ini file in each code template directory includes Type = "Legacy" for legacy code templates.

#### Legacy Code Templates for LabVIEW

Legacy code templates for the LabVIEW Adapter always specify Test Data and Error Out clusters as parameters. The VIs for each LabVIEW Adapter legacy code template specify various combinations of the Input Buffer, Invocation Info, and Sequence Context parameters. When TestStand uses a legacy LabVIEW template VI to create skeleton code, it selects the correct VI to use according to the current settings in the Optional Parameters dialog box in TestStand 3.5 or earlier.

#### Legacy Code Templates for LabWindows/CVI

Legacy code templates for the LabWindows/CVI Adapter always specify two parameters—a pointer to a tTestData structure and a pointer to a tTestError structure. When TestStand uses a legacy LabWindows/CVI template module to create skeleton code, it validates the function prototype in the template module against this requirement. TestStand reports an error when the prototype is incorrect.

Parent topic:

Creating and Customizing Code Template Files

Related concepts:

- TestStand Directory Structure
- Programming with the TestStand API in LabVIEW
- Programming with the TestStand API in LabWindows/CVI
- Organizing Test Program Files with LabVIEW-Built Shared Libraries

<!--NI_TOPIC bundle=teststand path=terminating-and-aborting-executions.html language=enus -->
## TOPIC 00866: Terminating and Aborting Executions

- bundle_id: `teststand`
- source_path: `terminating-and-aborting-executions.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/terminating-and-aborting-executions.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The menus in the TestStand Sequence Editor and TestStand User Interfaces include commands to stop execution before the execution completes normally. The TestStand API includes corresponding methods to stop execution from inside a code module or to determine whether the execution stopped. You can iss

### Terminating and Aborting Executions

The menus in the TestStand Sequence Editor and TestStand User Interfaces include commands to stop execution before the execution completes normally. The TestStand API includes corresponding methods to stop execution from inside a code module or to determine whether the execution stopped. You can issue a stop request at any time to stop one execution or all executions. Stop requests do not take effect in each execution until the currently executing code module for each thread in the execution returns control.

When you terminate an execution, all the Cleanup steps, including subsequences the Cleanup steps call, execute normally and disregard the pending termination. If you terminate an execution, or reselect Terminate while a Cleanup step is running and the step monitors for termination, the step terminates prematurely, and TestStand proceeds to execute the next Cleanup step. Terminating a Cleanup step terminates only that step, and the execution proceeds with the next Cleanup step. When you terminate an execution while the client sequence file is running, the default process model continues to run, possibly testing the next UUT or generating a report.

When you abort an execution, the Cleanup steps do not run, and the process model does not continue. Abort an execution in cases when you want an execution to completely stop as soon as possible. In general, it is better to terminate execution so the Cleanup steps can return the system to a known state. Abort an execution only when you are debugging or when you are sure it is safe to skip the Cleanup steps for a sequence.

Parent topic:

Executing Sequences

Related concepts:

- TestStand ActiveX API Overview
- Checking for Suspended or Stopped Execution within Code Modules

<!--NI_TOPIC bundle=teststand path=termination-monitor-labview.html language=enus -->
## TOPIC 00867: Termination Monitor - LabVIEW

- bundle_id: `teststand`
- source_path: `termination-monitor-labview.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/termination-monitor-labview.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Purpose This example demonstrates the use of the Termination Monitor VIs in LabVIEW. The Termination Monitor allows a code module to stop executing if TestStand attempts to terminate or abort the execution. Example File Location <TestStand Public>\Examples\Fundamentals\Termination Monitor\LabVIEW\Te

### Termination Monitor - LabVIEW

#### Purpose

This example demonstrates the use of the Termination Monitor VIs in LabVIEW. The Termination Monitor allows a code module to stop executing if TestStand attempts to terminate or abort the execution.

#### Example File
 Location

<TestStand
 Public>\Examples\Fundamentals\Termination
 Monitor\LabVIEW\Termination Monitor.seq

#### Highlighted Features

- LabVIEW Adapter
- Termination Monitor

#### Major API

None

#### Prerequisites

To run this example, you must have the LabVIEW development system installed and you must configure the LabVIEW Adapter to use the LabVIEW development system.

Note

#### How to Use This Example

This example uses a LabVIEW Action step to call a VI that runs indefinitely. Since this VI uses the Termination Monitor functions, it is able to stop when TestStand attempts to terminate or abort the execution. If the VI did not include the Termination Monitor functions, TestStand would be unable to terminate or abort the execution.

To review the configuration of the VI, open Termination Monitor Example.vi located at <TestStand Public>\Examples\Fundamentals\Termination Monitor\LabVIEW\Termination Monitor Example.vi. In the VI, observe that the TestStand - Initialize Termination Monitor VI is used to create a reference to the Termination Monitor object.

Every 100 milliseconds, the TestStand - Get Termination Monitor Status VI is called to determine whether TestStand is attempting to stop the execution. If so, the VI exits.

Note that the Termination Monitor VIs require the SequenceContext of the calling sequence. The SequenceContext is passed to the code module as a parameter.

Complete the following steps to run the example:

1. Select Execute»Single Pass to run the sequence.
2. When the TerminationMonitorExample VI front panel appears, the sequence will execute indefinitely.
3. On the Debug toolbar in TestStand, click the red Terminate button to terminate the execution. Observe that the execution terminates successfully.

Parent topic:

Termination Monitor

Related concepts:

- TestStand Directory Structure
- Programming with the TestStand API in LabVIEW
- Checking for Suspended or Stopped Execution within Code Modules

<!--NI_TOPIC bundle=teststand path=termination-monitor-labwindows-cvi.html language=enus -->
## TOPIC 00868: Termination Monitor - LabWindows/CVI

- bundle_id: `teststand`
- source_path: `termination-monitor-labwindows-cvi.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/termination-monitor-labwindows-cvi.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Purpose This example demonstrates the use of the Termination Monitor function in LabWindows/CVI. The Termination Monitor allows a code module to stop executing if TestStand attempts to terminate or abort the execution. Example File Location <TestStand Public>\Examples\Fundamentals\Termination Monito

### Termination Monitor - LabWindows/CVI

#### Purpose

This example demonstrates the use of the Termination Monitor function in LabWindows/CVI. The Termination Monitor allows a code module to stop executing if TestStand attempts to terminate or abort the execution.

#### Example File
 Location

<TestStand
 Public>\Examples\Fundamentals\Termination Monitor\CVI\Termination
 Monitor.seq

#### Highlighted Features

- LabWindows/CVI Adapter
- Termination Monitor

#### Major API

None

#### Prerequisites

None

#### How to Use This Example

This example uses a CVI Action step to call a function in a C DLL that runs indefinitely. Since it uses the Termination Monitor functionality, the function is able to stop when TestStand attempts to terminate or abort the execution. If the function did not call the Termination Monitor method, TestStand would be unable to terminate or abort the execution.

To review the functions used in this example, open Termination Monitor Example.c located at <TestStand Public>\Examples\Fundamentals\Termination Monitor\CVI\Termination Monitor Example.c.

The TS_CancelDialogIfExecutionStops method is used to search for a request from TestStand to stop the execution. This method automatically initiates a timer callback, which will call the QuitUserInterfacemethod if TestStand is attempting to terminate or abort the execution.

Note that theTS_CancelDialogIfExecutionStops method requires the panel handle of the onscreen dialog and the SequenceContext of the calling sequence as parameters. This method also assumes that the calling code has control of the dialog through a call to theRunUserInterface method.

Complete the following steps to run the example:

1. In TestStand, select Execute»Single Pass to run the sequence.
2. When the TerminationMonitorExample dialog appears, the sequence will execute indefinitely.
3. On the Debug toolbar in TestStand, click the red Terminate button to terminate the execution. Observe that the execution terminates successfully.

Parent topic:

Termination Monitor

Related concepts:

- TestStand Directory Structure
- Programming with the TestStand API in LabWindows/CVI
- Checking for Suspended or Stopped Execution within Code Modules

<!--NI_TOPIC bundle=teststand path=termination-monitor-net.html language=enus -->
## TOPIC 00869: Termination Monitor - .NET

- bundle_id: `teststand`
- source_path: `termination-monitor-net.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/termination-monitor-net.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Purpose This example demonstrates the use of the Termination Monitor function in .NET. The Termination Monitor allows a code module to stop executing if TestStand attempts to terminate or abort the execution. Example File Location <TestStand Public>\Examples\Fundamentals\Termination Monitor\dotNET\T

### Termination Monitor - .NET

#### Purpose

This example demonstrates the use of the Termination Monitor function in .NET. The Termination Monitor allows a code module to stop executing if TestStand attempts to terminate or abort the execution.

#### Example File
 Location

<TestStand
 Public>\Examples\Fundamentals\Termination
 Monitor\dotNET\Termination Monitor.seq

#### Highlighted Features

- .NET Adapter
- Termination Monitor

#### Major API

None

#### Prerequisites

None

#### How to Use This Example

This example uses a .NET Action step to call a function in a .NET assembly that runs indefinitely. Since it uses the Termination Monitor functionality, the function is able to stop when TestStand attempts to terminate or abort execution. If the function did not call the Termination Monitor method, TestStand would be unable to terminate or abort the execution.

To review the functions used in this example, open Termination Monitor Example Form.cs located at <TestStand Public>\Examples\Fundamentals\Termination Monitor\dotNET\Termination Monitor Example\Termination Monitor Example Form.cs.

In the InitializeTerminationStateChecking()method, notice that the Execution.InitTerminationMonitor method from the TestStand API is used to initialize the termination monitor and obtain a reference to data required by other Termination Monitor functions. Every 100 milliseconds, the state of the execution is queried with the Execution.GetTerminationMonitorStatus method from the TestStand API. If TestStand is attempting to terminate or abort the execution, this code module finishes its execution.

Complete the following steps to run the example:

1. In TestStand, select Execute»Single Pass to run the sequence.
2. When the TerminationMonitorExample dialog appears, the sequence will execute indefinitely.
3. On the Debug toolbar in TestStand, click the red Terminate button to terminate the execution. Observe that the execution terminates successfully.

Parent topic:

Termination Monitor

Related concepts:

- TestStand Directory Structure
- Checking for Suspended or Stopped Execution within Code Modules

<!--NI_TOPIC bundle=teststand path=termination-monitor.html language=enus -->
## TOPIC 00870: Termination Monitor

- bundle_id: `teststand`
- source_path: `termination-monitor.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/termination-monitor.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The <TestStand Public>\Examples\Fundamentals\Termination Monitor directory contains the following examples.

### Termination Monitor

The <TestStand
 Public>\Examples\Fundamentals\Termination Monitor
 directory contains the following examples.

- [Termination Monitor - LabWindows/CVI](termination-monitor-labwindows-cvi.html)
- [Termination Monitor - LabVIEW](termination-monitor-labview.html)
- [Termination Monitor - .NET](termination-monitor-net.html)

Parent topic:

Examples for Fundamentals

Related concepts:

- TestStand Directory Structure

<!--NI_TOPIC bundle=teststand path=test-uuts-execution-entry-point-in-the-batch.html language=enus -->
## TOPIC 00871: Test UUTs Execution Entry Point in the Batch Process Model

- bundle_id: `teststand`
- source_path: `test-uuts-execution-entry-point-in-the-batch.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/test-uuts-execution-entry-point-in-the-batch.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Test UUTs main Execution entry point is the sequence the controlling execution runs. Open <TestStand>\Components\Models\TestStandModels\BatchModel.seq in the TestStand Sequence Editor and select the Test UUTs sequence on the Sequences pane to examine the Batch process model Test UUTs Execution e

### Test UUTs Execution Entry Point in the Batch Process Model

The Test UUTs main Execution entry point is the sequence the controlling execution runs.

Open <TestStand>\Components\Models\TestStandModels\BatchModel.seq in the TestStand Sequence Editor and select the Test UUTs sequence on the Sequences pane to examine the Batch process model Test UUTs Execution entry point, which performs the following significant actions:

1. Calls the Initialize Execution Entry Point plug-in utility sequence.
2. Calls the Initialize ModelData sequence.
3. Calls the Model Plugins – Begin sequence.
4. Calls the ProcessSetup callback.
5. Calls the PreBatchLoop callback.
6. Creates and initializes the test socket executions.
7. Calls the Run Batch Info Dialog utility sequence.
8. Calls the WaitForTestSockets method to wait for and monitor test socket executions until the test sockets reach the Initialize synchronization point.
9. Calls the Add TestSocket Threads to Batch utility sequence.
10. Calls the AllowTestSocketsToContinue method to notify test sockets to continue past the Initialize synchronization point.
11. Begins the Batch For loop.
12. Calls the WaitForTestSockets method to wait for and monitor test socket executions until the test sockets reach the GetUUTSerialNumber synchronization point.
13. Calls the PreBatch callback.
14. Calls the Model Plugins – Pre Batch sequence.
15. When no more UUTs exist, sets the ContinueTesting test socket data variable to False for all the test sockets and marks all test sockets as enabled to allow currently disabled test sockets to complete execution.
16. Calls the Add TestSocket Threads to Batch utility sequence to add enabled test socket threads to the batch specification and remove disabled test sockets from the batch specification so they do not block running threads.
17. Calls the AllowTestSocketsToContinue method to notify test sockets to continue past the GetUUTSerialNumber synchronization point. If no more UUTs exist, skips to .
18. Calls the Model Plugins – Batch Start sequence.
19. Calls the WaitForTestSockets method to wait for and monitor test socket executions until the test sockets reach the ReadyToRun synchronization point.
20. Calls the Tile Execution Windows utility sequence.
21. Calls the AllowTestSocketsToContinue method to notify test sockets to continue past the ReadyToRun synchronization point.
22. Calls the WaitForTestSockets method to wait for and monitor test socket executions until the test sockets display the test socket reach the PostMainSequence synchronization point. The test sockets do not block at this synchronization point.
23. Calls the Model Plugins – Batch Done sequence
24. Calls the WaitForTestSockets method to wait for and monitor test socket executions until the test sockets reach the ReAddToBatch synchronization point.
25. Calls the Add TestSocket Threads to Batch utility sequence to add test socket execution threads back to the batch specification.
26. Calls the AllowTestSocketsToContinue method to notify test sockets to continue past the ReAddToBatch synchronization point.
27. Calls the WaitForTestSockets utility method to wait for and monitor test socket executions until the test sockets reach the AfterPostUUT synchronization point.
28. Calls the Model Plugins – Post Batch sequence
29. Calls the PostBatch callback.
30. Waits for the Status dialog box. When TestStand launches the PostBatch callback Status dialog box, the sequence waits for you to dismiss the dialog box if you have not already done so.
31. Calls the AllowTestSocketsToContinue method to notify test sockets to continue past the AfterPostUUT synchronization point.
32. Ends the Batch For loop, looping back to begin the next batch.
33. Calls the WaitAndCheckExecutionStateForAllTestSockets method to determine the first UUT error, if one occurred, and whether any UUTs terminated or aborted. Waits for all test socket executions to complete.
34. Calls the PostBatchLoop callback. Performs any cleanup operations related to initialization operations performed in the PreBatch callback here or in the ProcessCleanup callback when the process model skips steps through .
35. Calls the ProcessCleanup callback.
36. Calls the Model Plugins – End sequence. Custom process model plug-ins should perform any cleanup operations related to initialization operations performed in the Model Plugin – PreBatch entry point here when the process model skips steps through .

Parent topic:

Main Execution Entry Points in the Batch Process Model

Related concepts:

- Main Execution Entry Points in the Batch Process Model
- TestStand Directory Structure
- Plug-in Utility Sequences
- Model Plugin – Begin
- Model Callbacks in the Batch Process Model
- Test UUTs – Test Socket Entry Point Execution Entry Point in the Batch Process Model
- Utility Sequences in the Batch Process Model
- Model Plugin – Pre Batch
- Model Plugin – Batch Start
- Model Plugin – Batch Done
- Model Plugin – Post Batch
- Model Plugin – End

<!--NI_TOPIC bundle=teststand path=test-uuts-execution-entry-point-in-the-parall.html language=enus -->
## TOPIC 00872: Test UUTs Execution Entry Point in the Parallel Process Model

- bundle_id: `teststand`
- source_path: `test-uuts-execution-entry-point-in-the-parall.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/test-uuts-execution-entry-point-in-the-parall.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Test UUTs main Execution entry point is the sequence the controlling execution runs. Open <TestStand>\Components\Models\TestStandModels\ParallelModel.seq in the TestStand Sequence Editor and select the Test UUTs sequence on the Sequences pane to examine the Parallel process model Test UUTs Execu

### Test UUTs Execution Entry Point in the Parallel Process Model

The Test UUTs main Execution entry point is the sequence the controlling execution runs.

Open <TestStand>\Components\Models\TestStandModels\ParallelModel.seq in the TestStand Sequence Editor and select the Test UUTs sequence on the Sequences pane to examine the Parallel process model Test UUTs Execution entry point, which performs the following significant actions:

1. Calls the Initialize Execution Entry Point plug-in utility sequence.
2. Calls the Model Plugins – Begin sequence.
3. Calls the ProcessSetup callback.
4. Calls the Run UUT Info Dialog utility sequence.
5. Creates and initializes the test socket executions.
6. Calls the ProcessDialogRequests utility sequence.
7. Waits for test socket executions to complete.
8. Calls the ProcessCleanup callback.
9. Calls the Model Plugins – End sequence.

Parent topic:

Main Execution Entry Points in the Parallel Process Model

Related concepts:

- Main Execution Entry Points in the Parallel Process Model
- TestStand Directory Structure
- Plug-in Utility Sequences
- Model Plugin – Begin
- Model Callbacks in the Parallel Process Model
- Utility Sequences in the Parallel Process Model
- Test UUTs – Test Socket Entry Point Execution Entry Point in the Parallel Process Model
- Model Plugin – End

<!--NI_TOPIC bundle=teststand path=test-uuts-execution-entry-point-in-the-sequen.html language=enus -->
## TOPIC 00873: Test UUTs Execution Entry Point in the Sequential Process Model

- bundle_id: `teststand`
- source_path: `test-uuts-execution-entry-point-in-the-sequen.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/test-uuts-execution-entry-point-in-the-sequen.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Open <TestStand>\Components\Models\TestStandModels\SequentialModel.seq in the TestStand Sequence Editor and select the Test UUTs sequence on the Sequences pane to examine the Sequential process model Test UUTs Execution entry point, which performs the following significant actions: Calls the Initial

### Test UUTs Execution Entry Point in the Sequential Process Model

Open <TestStand>\Components\Models\TestStandModels\SequentialModel.seq in the TestStand Sequence Editor and select the Test UUTs sequence on the Sequences pane to examine the Sequential process model Test UUTs Execution entry point, which performs the following significant actions:

1. Calls the Initialize Execution Entry Point plug-in utility sequence.
2. Calls the Model Plugins – Begin sequence.
3. Calls the ProcessSetup callback.
4. Calls the PreUUTLoop callback.
5. Initiates the UUT For loop.
6. Calls the PreUUT callback. When no more UUTs exist, skips to .
7. Calls the Model Plugins – Pre UUT sequence. When no more UUTs exist, skips to .
8. Calls the Model Plugins – UUT Start sequence.
9. Calls the PreMainSequence callback.
10. Calls the MainSequence callback.
11. Calls the PostMainSequence callback.
12. Calls the Model Plugins – UUT Done sequence.
13. Calls the Model Plugins – Post UUT sequence.
14. Calls the PostUUT callback.
15. Ends the UUT For loop block, looping back to begin the next UUT.
16. Calls the PostUUTLoop callback. Performs any cleanup operations related to initialization operations performed in the PreUUT callback here or in the ProcessCleanup callback when the process model exits the UUT loop.
17. Calls the ProcessCleanup callback.
18. Calls the Model Plugins – End sequence. Custom process model plug-ins should perform any cleanup operations related to initialization operations performed in the Model Plugin – PreUUT entry point here when the process model exits the UUT loop.

Parent topic:

Execution Entry Points in the Sequential Process Model

Related concepts:

- TestStand Directory Structure
- Execution Entry Points in the Sequential Process Model
- Plug-in Utility Sequences
- Model Plugin – Begin
- Model Callbacks in the Sequential Process Model
- Model Plugin – Pre UUT
- Model Plugin – UUT Start
- Model Callbacks in the Parallel Process Model
- Model Plugin – UUT Done
- Model Plugin – Post UUT
- Model Plugin – End

<!--NI_TOPIC bundle=teststand path=test-uuts-test-socket-entry-point-batch.html language=enus -->
## TOPIC 00874: Test UUTs – Test Socket Entry Point Execution Entry Point in the Batch Process Model

- bundle_id: `teststand`
- source_path: `test-uuts-test-socket-entry-point-batch.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/test-uuts-test-socket-entry-point-batch.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Test UUTs – Test Socket Entry Point is the Execution entry point sequence the test socket executions run. The controlling execution creates the test socket executions in the Test UUTs Execution entry point sequence. Open <TestStand>\Components\Models\TestStandModels\BatchModel.seq in the TestSta

### Test UUTs – Test Socket Entry Point Execution Entry Point in the Batch Process Model

The Test UUTs – Test Socket Entry Point is the Execution entry point sequence the test socket executions run. The controlling execution creates the test socket executions in the Test UUTs Execution entry point sequence.

Open <TestStand>\Components\Models\TestStandModels\BatchModel.seq in the TestStand Sequence Editor and select the Test UUTs – Test Socket Entry Point sequence on the Sequences pane to examine the Batch process model Test UUTs – Test Socket entry point Execution entry point, which performs the following significant actions:

1. Calls the Initialize Execution Entry Point plug-in utility sequence.
2. Calls the SyncWithController method to synchronize with the controlling execution at the Initialize synchronization point. The method waits until the controlling execution allows the test socket to continue past the Initialize synchronization point.
3. Calls the Model Plugins – Begin sequence.
4. Calls the PreUUTLoop callback.
5. Begins the UUT For loop.
6. Calls the SyncWithControllerAtRestart method to synchronize with the controlling execution at the GetUUTSerialNumber synchronization point. The method waits until the controlling execution allows the test socket to continue past the GetUUTSerialNumber synchronization point. When no more UUTs exist, skips to .
7. Calls the PreUUT callback. When no more UUTs exist, skips to .
8. Calls the Model Plugins – Pre UUT sequence. When no more UUTs exist, skips to .
9. Calls the PreMainSequence callback.
10. Calls the Model Plugins – UUT Start sequence.
11. Calls the SyncWithController method to synchronize with the controlling execution at the ReadyToRun synchronization point. The method waits until the controlling execution allows the test socket to continue past the ReadyToRun synchronization point.
12. Calls the MainSequence callback.
13. Removes the test socket thread from the batch specification in case the main sequence terminates or the client sequence file does not properly handle batch synchronization. The controlling execution adds the thread back to the batch specification before continuing past the next synchronization point.
14. Calls the SyncWithController method to synchronize with the controlling execution at the PostMainSequence synchronization point. The method does not does not wait for the controlling execution at this synchronization point.
15. Calls the PostMainSequence callback.
16. Calls the Model Plugins – UUT Done sequence.
17. Calls the Model Plugins – Post UUT sequence.
18. Calls the SyncWithController utility method to synchronize with the controlling execution at the ReAddToBatch synchronization point. The method waits until the controlling execution allows the test sockets to continue past the ReAddToBatch synchronization point.
19. Calls the PostUUT callback.
20. Calls the SyncWithController method to synchronize with the controlling execution at the AfterPostUUT synchronization point. The method waits until the controlling execution allows the test socket to continue past the AfterPostUUT synchronization point.
21. Ends the UUT For loop block, looping back to begin the next UUT For loop iteration.
22. Calls the PostUUTLoop callback. Performs any cleanup operations related to initialization operations performed in the PreUUT callback here when the process model skips steps through .
23. Calls the Model Plugins – End sequence. Custom process model plug-ins should perform any cleanup operations related to initialization operations performed in the Model Plugin – PreUUT entry point here when the process model skips steps through .

Parent topic:

Hidden Execution Entry Points in the Batch Process Model

Related concepts:

- Test UUTs Execution Entry Point in the Batch Process Model
- Main Execution Entry Points in the Batch Process Model
- TestStand Directory Structure
- Plug-in Utility Sequences
- Model Plugin – Begin
- Model Callbacks in the Batch Process Model
- Model Plugin – Pre UUT
- Model Callbacks in the Parallel Process Model
- Model Plugin – UUT Start
- Model Plugin – UUT Done
- Model Plugin – Post UUT
- Model Plugin – End

<!--NI_TOPIC bundle=teststand path=test-uuts-test-socket-entry-point-parallel.html language=enus -->
## TOPIC 00875: Test UUTs – Test Socket Entry Point Execution Entry Point in the Parallel Process Model

- bundle_id: `teststand`
- source_path: `test-uuts-test-socket-entry-point-parallel.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/test-uuts-test-socket-entry-point-parallel.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Test UUTs – Test Socket Entry Point is the Execution entry point sequence the test socket executions run. The controlling execution creates the test socket executions in the Test UUTs Execution entry point sequence. Open <TestStand>\Components\Models\TestStandModels\ParallelModel.seq in the Test

### Test UUTs – Test Socket Entry Point Execution Entry Point in the Parallel Process Model

The Test UUTs – Test Socket Entry Point is the Execution entry point sequence the test socket executions run. The controlling execution creates the test socket executions in the Test UUTs Execution entry point sequence.

Open <TestStand>\Components\Models\TestStandModels\ParallelModel.seq in the TestStand Sequence Editor and select the Test UUTs – Test Socket Entry Point sequence on the Sequences pane to examine the Parallel process model Test UUTs – Test Socket Entry Point Execution entry point, which performs the following significant actions:

1. Calls the Initialize Execution Entry Point plug-in utility sequence.
2. Calls the Model Plugins – Begin sequence.
3. Calls the PreUUTLoop callback.
4. Initiates the UUT For loop.
5. Calls the PreUUT callback. When no more UUTs exist, skips to .
6. Calls the Model Plugins – Pre UUT sequence. When no more UUTs exist, skips to .
7. Calls the Model Plugins – UUT Start sequence.
8. Calls the PreMainSequence callback.
9. Calls the MainSequence callback.
10. Calls the PostMainSequence callback.
11. Calls the Model Plugins – UUT Done sequence.
12. Calls the Model Plugins – Post UUT sequence.
13. Calls the PostUUT callback.
14. Ends the UUT For loop block, looping back to begin the next UUT.
15. Calls the PostUUTLoop callback. Performs any cleanup operations related to initialization operations performed in the PreUUT callback here when the process model exits the UUT loop.
16. Calls the Model Plugins – End sequence. Custom process model plug-ins should perform any cleanup operations related to initialization operations performed in the Model Plugin – PreUUT entry point here when the process model exits the UUT loop.

Parent topic:

Hidden Execution Entry Points in the Parallel Process Model

Related concepts:

- Test UUTs Execution Entry Point in the Parallel Process Model
- Main Execution Entry Points in the Parallel Process Model
- TestStand Directory Structure
- Plug-in Utility Sequences
- Model Plugin – Begin
- Model Callbacks in the Parallel Process Model
- Model Plugin – Pre UUT
- Model Plugin – UUT Start
- Model Plugin – UUT Done
- Model Plugin – Post UUT
- Model Plugin – End

<!--NI_TOPIC bundle=teststand path=testing-uuts-in-parallel-batch-model.html language=enus -->
## TOPIC 00876: Testing UUTs in Parallel - Batch Model

- bundle_id: `teststand`
- source_path: `testing-uuts-in-parallel-batch-model.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/testing-uuts-in-parallel-batch-model.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Purpose This example demonstrates how to use the Batch process model to test multiple UUTs simultaneously by running a sequence once for each test socket in the system. The Batch process model generates a batch report that summarizes the results for the UUTs in the batch. Example File Location <Test

### Testing UUTs in Parallel - Batch Model

#### Purpose

This example demonstrates how to use the Batch process model to test multiple UUTs simultaneously by running a sequence once for each test socket in the system. The Batch process model generates a batch report that summarizes the results for the UUTs in the batch.

#### Example File
 Location

<TestStand
 Public>\Examples\Parallel Testing\Testing UUTs in Parallel - Batch
 Model\Testing UUTs in Parallel - Batch Model.seq

#### Highlighted Features

- Batch process model
- Batch Synchronization step
- Flow Control steps
- Synchronization panel

#### Major API

None

#### Prerequisites

None

#### How to Use This Example

The Set Chamber Temperature step in the MainSequence applies an action to the entire UUT batch. The Synchronization panel of the Properties tab of the Step Settings pane for the step sets the Batch Synchronization option to One thread only because the sequence needs to execute this action only once for the entire batch.

The Pulse Test step calls the Pulse Test subsequence, which you can select on the Sequences pane. This sequence contains Batch Synchronization steps that create a serial synchronized section around the other steps in the sequence to force all the UUTs in the batch to execute the steps on one UUT before the next UUT can begin. In a real-world application, controlling UUT execution in a batch can be useful in cases in which you have only one set of testing equipment available for certain procedures.

The Frequency Sweep step in the MainSequence does not specify any synchronization options, and so all UUTs run this step in parallel.

Select Execute»Single Pass to run the sequence and review the behavior of the batch execution. When the test completes, the sequence launches a dialog box that displays the time required to perform the frequency test on all UUTs. The dialog box divides the total time by the number of UUTs and displays the test time per UUT to illustrate how you can increase throughput by testing UUTs in parallel.

Note

- By default, a sequence file uses the Sequential process model, but you can use the Station Model control on the Model tab of the Station Options dialog box to specify that the Batch process model is the default model for all sequence files.
- You can use the Model Options dialog box to configure the number of test sockets you want to use for the batch.

Parent topic:

Examples for Parallel Testing

Related concepts:

- Batch Process Model
- TestStand Directory Structure
- Sequential Process Model

<!--NI_TOPIC bundle=teststand path=testing-uuts-in-parallel-parallel-model.html language=enus -->
## TOPIC 00877: Testing UUTs in Parallel - Parallel Model

- bundle_id: `teststand`
- source_path: `testing-uuts-in-parallel-parallel-model.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/testing-uuts-in-parallel-parallel-model.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Purpose This example demonstrates use of the Parallel process model to test multiple UUTs in parallel. With the Parallel process model, each UUT executes independently, and you can start and stop testing on any test socket at any time. Example File Location <TestStand Public>\Examples\Parallel Testi

### Testing UUTs in Parallel - Parallel Model

#### Purpose

This example demonstrates use of the Parallel process model to test multiple UUTs in parallel. With the Parallel process model, each UUT executes independently, and you can start and stop testing on any test socket at any time.

#### Example File
 Location

<TestStand
 Public>\Examples\Parallel Testing\Testing UUTs in Parallel -
 Parallel Model\Testing UUTs in Parallel - Parallel
 Model.seq

#### Highlighted Features

Parallel process model

#### Major API

None

#### Prerequisites

None

#### How to Use This Example

Complete the following steps to review the sequences and steps in the example.

1. Open Testing UUTs in Parallel - Parallel Model.seq , select Edit»Sequence File Properties and click the Advanced tab. The settings on this tab specify that the Parallel process model executes this sequence file. You can configure any sequence file to use the Parallel process model by opening the file, navigating to the Advanced tab of the Sequence File Properties dialog box, selecting Require Specific Model for the Model Option setting, and then selecting ParallelModel.seq from the Model File control.
2. On the Sequences pane, select the MainSequence . This sequence contains one Sequence Call step and one Numeric Limit Test with an associated LabWindows\CVI code module.
3. On the Sequences pane, select the PreUUTLoop sequence. This sequence is a callback from the Parallel process model. Steps in this sequence execute this code only once before any UUTs are tested. The Set Chamber Temperature step simulates a setup operation that must be performed to prepare the test station for UUT testing, but it needs to be performed only once before any tests begin.
4. On the Sequences pane, select the Pulse Test sequence. This sequence simulates a test that can execute on only one test socket at a time. In many cases, a test station testing multiple UUTs in parallel must share resources (such as hardware) between test sockets to ensure multiple sockets do not attempt to access the resource at the same time.
5. Observe the Enter Locked Section step at the beginning of the sequence and the Exit Locked Section step at the end of the sequence. These steps use the Lock synchronization object in TestStand to ensure only one test socket executes this sequence at a time.

Complete the following steps to run the example.

1. Select Execute»Test UUTs to run the sequence.
2. The Set Chamber Temperature dialog box indicates the simulated chamber heating process. This code executes before any UUTs are tested.
3. The UUT Information dialog box displays once the chamber heating process is complete. Use this dialog box to enter a serial number for the UUT and start or stop the execution for each test socket.
4. Once testing has started on a test socket, dialog boxes indicate the status of the tests. Observe that the Parallel model allows each UUT to start and stop testing independently. However, the Lock steps in the Pulse Test sequence cause that sequence to execute on only one test socket at a time. This behavior demonstrates the ability to synchronize among test sockets when using the Parallel model.

Parent topic:

Examples for Parallel Testing

Related concepts:

- Parallel Process Model
- TestStand Directory Structure

<!--NI_TOPIC bundle=teststand path=teststand-2017-changes.html language=enus -->
## TOPIC 00878: TestStand 2017 Changes

- bundle_id: `teststand`
- source_path: `teststand-2017-changes.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/teststand-2017-changes.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `reference`
- source_description: Learn about new features, behavior changes, and other updates in TestStand 2017. Data Streams Step TypesTestStand Data Streams provide a simple way to read data from or write data to CSV (comma separated value) files. Basic Data Streams functionality is provided by the Data Streams step types as wel

### TestStand 2017 Changes

Learn about new features, behavior changes, and other updates in TestStand
 2017.

#### Data Streams Step Types

TestStand
 Data Streams provide a simple way to read data from or write data to CSV (comma separated
 value) files. Basic Data Streams functionality is provided by the Data Streams step types as
 well as an update to the existing For Each step type. Use these step types to quickly and
 easily create sequences that consume or produce CSV file data.

Data Streams step
 types are built on an underlying public API that you can call directly to handle more
 complex applications. At the core of the Data Streams feature are two COM (Component Object
 Model) interfaces: InputRecordStream and
 OutputRecordStream. Advanced users can create custom implementations of
 these interfaces to enable TestStand sequences to work with any producer or consumer of data
 that has a logical structure similar to a table.

To get started using the feature, use
 the example code provided with TestStand 2017 at <TestStand Public
 Directory>\Examples\Fundamentals\Using Data Streams.

#### Crash Recovery for TestStand
 Applications

TestStand 2017 has the option to generate a log containing execution
 information and use the NI Error Reporting Service, NIER, to automatically generate a crash
 dump file. You can use a crash dump file to diagnose the root cause of a crash. In cases
 where the crash is in an NI product, you can send the crash dump file to NI support
 engineers for diagnosis. TestStand also offers a way to register a custom sequence to
 execute in an external process in response to a crash.

TestStand Crash Log—When a
 crash occurs TestStand generates a log file in the directory
 <TestStand_LocalAppData>\CrashLogs. Only the last 100 crash
 logs are saved, after which the earliest log file will be deleted and a new log file is
 created.

NIER Crash Dump—Using the same error reporting service as LabVIEW, TestStand
 generates a NIER crash dump in
 <TestStand_LocalAppData>\NIERdump.

#### TestStand Crash Log and Dump
 File

You can use a configuration file to specify settings for the dump and
 TestStand specific log file. The configuration file is an .ini file in
 the same directory as the TestStand application. The name of the configuration file must be
 same as the executable name of the TestStand application.

In the configuration file,
 create a section with the same name as the name of the executable. Use the following tokens
 and values to specify the options:

| Token Name | Value | Purpose |
| --- | --- | --- |
| TSLogType | None | Do not create TestStand crash log. By default, TestStand crash log is created. |
| NIER | False | Do not create NIER crash dump. By default, NIER crash dump is created. |
| NIERDumpType | Full | Create full (instead of mini) NIER crash dump. By default, mini dump file is created. |
| LogVariables | True | Enable logging of Locals, Parameters, and FileGlobals in the TestStand specific log file. By default, Locals, Parameters, and FileGlobals are not logged in the TestStand log file. |

Note

Code
 modules should not register to functions like SetUnhandledExceptionFilter,
 set_invalid_parameter_handler, and set_purecall_handler
 to handle application crashes. Crash logging due to running out of memory is not
 supported.

#### Registering a Crash Recovery
 Sequence

You can register sequences to respond to a crash in your TestStand
 application to return any hardware or other system assets to a good state. The sequences are
 executed by an external process and run without a process model or a logged-in user. Since
 multiple crash recovery sequences can be registered, the order in which the sequences will
 be executed is the order in which they are registered.

Any errors encountered in
 executing crash recovery sequences are recorded in a log file, and a dialog displays the
 location of the log file. Similar to the main application TestStand crash log, this log file
 stores the errors from a maximum of 100 crash callbacks.

To register a sequence for
 execution in the case of a crash you must call Engine.RegisterSequenceToExecuteOnCrash with
 the sequence name and file path to be executed. This function returns a unique ID that can
 be used to unregister the sequence later with a call to
 Engine.UnregisterSequenceToExecuteOnCrash.

#### Support for Package Distribution in the
 TestStand Deployment Utility

TestStand Deployment Utility now supports building
 package distributions in addition to MSI-based installers. Use the Output
 Type control on the Mode tab to configure the TestStand
 Deployment Utility to build a package-based installer. This control has 3 settings:

- Deployable Image Only —The deployment files are moved to the
 specified image directory on the System Source tab.
- MSI-Based Installer —In addition to the deployable image, the
 deployment utility creates an installer to distribute the system. When you select this
 option, the Installer tab is enabled, which you can use to configure
 the installer.
- Package-Based Distribution —In addition to the deployable image,
 the deployment utility creates a package distribution. When you select this option, the
 Package Distribution Options tab is enabled, which you can use to
 configure the package distribution. You can configure the package output type using the
 options below:
  - Single Package —The files in the image directory are packaged
 into a single .nipkg file. Dependencies you select are referenced
 by the package, and must be installed on the deployment target to install the
 package.
  - Repository —In addition to the main package, all dependent
 packages are also included in the deployment (the repository). A feed is generated
 which references all included packages in the repository. To install the deployment,
 you can register the feed in NI Package Manager on the target machine.
  - Package Installer —In addition to the main package, all
 dependent packages are also included in the deployment. A standalone installer is
 generated which installs all the packages on a machine. The installer will also
 install NI Package Manager if it is not present on the machine.

#### Configuring the Package Settings in the
 TestStand Deployment Utility

Package distribution settings are configured on the
 Installer tab. The package name is generated from the Installation
 name you specify. To configure additional settings for the package, click the
 Advanced Options button.

Note

Include Required Certificate
 Packages

To include package-based dependencies, click
 the Dependencies button. For each dependency you select, you can
 configure the dependency level:

- Required — The package cannot be installed unless the dependency
 is on the system or can be found by NI Package Manager through a registered feed. These
 packages are included in the deployment in feed or package distribution mode.
- Recommended/Optional — The package can be installed without these
 dependencies. They are not included in feed or package distribution mode.

The following features are currently not supported in package mode:

- Advanced File Options (creating shortcuts, program items, or registering as an ActiveX
 server)
- Custom Commands
- Including readme files or license agreements
- Media spanning

#### Support for LabVIEW NXG in the TestStand
 Deployment Utility

TestStand Deployment Utility supports deploying sequence files
 which call LabVIEW NXG code modules. LabVIEW NXG steps can be configured in the following
 ways:

- Project and GLL are Both Specified— These steps can execute using the LabVIEW NXG
 development system to execute the VI directly, or using the LabVIEW NXG Run-Time Engine to
 execute the VI within the GLL. In this case, TestStand enforces that the specified GLL
 must match the GLL output configured in the project and component in LabVIEW NXG. When
 deploying these types of steps, TestStand Deployment Utility automatically regenerates the
 GLL from the project before deploying to ensure that the latest code is used.
- GLL Specified, Project Not Specified— These steps must be executed using the LabVIEW NXG
 Run-Time Engine to execute the VIs built into the GLL. When deploying these types of
 steps, the GLL file is deployed as-is because no source files are present to rebuild
 it.
- Project Specified, GLL Not Specified— These steps can execute using the LabVIEW NXG
 Development System to execute the VI directly. Deployment is not supported for these steps
 by TestStand Deployment Utility. An error is generated indicating that a GLL is
 required.

Note

#### Configuring LabVIEW NXG Files in the
 TestStand Deployment Utility

After analyzing a sequence with LabVIEW NXG code
 modules, the referenced GLLs are displayed in the distributed files tab. You can configure
 the destination for the GLL file. Like other code module types, TestStand Deployment Utility
 ensures that the sequence file is updated to reference the correct files if the files are
 deployed within the same base destination as the calling sequence file.

To include
 LabVIEW NXG source files in the deployment, click LabVIEW options,
 and select the LabVIEW NXG options tab. Enable the Include LabVIEW NXG Source
 Files option. With this option selected, LabVIEW NXG projects, components, and
 VIs will also be displayed in the distributed files tab. Only referenced files are displayed
 in the distributed files tab, but all files included in the project will be included in the
 deployment. You can configure the destination for the source project, but not for contained
 components and VIs; these files will be deployed to a location relative to the
 project.

#### Deploying the LabVIEW NXG Run-Time Engine in
 an MSI-based Installer in the TestStand Deployment Utility

Because the LabVIEW
 NXG Run-Time Engine is a National Instruments package it is not directly available as a
 dependency in an MSI-based installer. However, if you enable the Automatically
 Include Required Installers option in the Drivers and Components dialog,
 TestStand Deployment Utility will include the Run-Time Engine package within the installer
 folder. When the installer is executed, it will invoke NI Package Manager to install the
 Run-Time Engine package.

#### Limitations in the TestStand Deployment
 Utility

The following LabVIEW step features are not currently supported with
 LabVIEW NXG Steps:

- Generating a PPL for deployment. This feature is no longer necessary because LabVIEW NXG
 does not create PPLs.
- Merging of LabVIEW NXG projects.

#### Early Access Support for LabVIEW
 NXG

TestStand 2017 provides early access support for LabVIEW NXG. The LabVIEW NXG
 Adapter is suitable for developing simple test systems, or augmenting existing test systems,
 but has limitations that may not be acceptable for all applications. National Instruments
 recommends that you fully evaluate LabVIEW NXG before using it in a TestStand
 system.

Consider the following topics when evaluating LabVIEW NXG for your test
 system:

- Processor architecture—The LabVIEW NXG Adapter is only available in 64-bit
 TestStand.
- LabVIEW NXG Classes—TestStand 2017 does not support LabVIEW NXG classes.
- GLL Support—TestStand 2017 enables the ability to build GLLs for use with the run-time
 engine. GLLs can be executed through the LabVIEW NXG adapter but cannot be called directly
 from VIs.
- Debugging—LabVIEW NXG 2.0 does not support building debuggable GLLs. TestStand 2017
 supports debugging LabVIEW NXG code modules in the development environment.
- COM Automation Support—Invoke nodes are not available in LabVIEW NXG. All Properties and
 Methods of the TestStand API are available through the TestStand palette in LabVIEW
 NXG.
- Modules and Toolkits—LabVIEW NXG is not supported in TestStand Semiconductor Module
 applications.
- Data types Support—The following data types present in LabVIEW NXG are not supported in
 the LabVIEW NXG Adapter:
  - Variants
  - Digital Waveform
  - Digital Table

#### LabVIEW NXG Adapter

TestStand 2017
 offers early access support for calling into code modules developed in LabVIEW NXG 2.0 with
 the LabVIEW NXG Adapter. The LabVIEW NXG Adapter provides advanced functionality for calling
 VIs from TestStand. You can use the LabVIEW NXG Adapter to complete the following
 tasks:

- Call VIs that exist in a LabVIEW NXG project or a LabVIEW NXG GLL.
- View the VI description and parameter descriptions through the Module tab in Step
 Settings.
- Run VIs using the LabVIEW NXG Development System.
- Run VIs in GLLs using the LabVIEW NXG Run-Time Engine.
- Create and edit VIs from TestStand if the LabVIEW NXG Development System is
 installed.
- Auto-build a LabVIEW NXG GLL from the LabVIEW NXG project when executing in the LabVIEW
 NXG Run-Time Engine.

For a LabVIEW NXG test step, specify the module in the Module tab of the Step Settings
 pane by defining the Project or GLL path, the VI name, and the desired parameters. The
 LabVIEW NXG Adapter requires the Project or GLL Path and the VI name to be
 defined.

The LabVIEW NXG Adapter can run VIs using the LabVIEW NXG Development System
 or the LabVIEW NXG Run-Time Engine. You must build your VIs into a GLL containing your VIs
 when using the Run-Time Engine. Additionally, recompilation of GLLs is required when
 modifications are made to the original VIs.

Use the LabVIEW NXG Adapter
 Configuration dialog box to switch between executions using the LabVIEW NXG
 Development System and the LabVIEW NXG Run-Time Engine.

The Adapter Configuration also
 includes the option to Automatically Build Missing GLLs at Start of
 Execution. This option allows you to run a step in the Run-Time Engine which
 only has the project and VI specified. The LabVIEW NXG Adapter builds the GLL if
 necessary.

Use the LabVIEW NXG Advanced Settings dialog box in
 the Step Settings pane to access the option Always Run VI in LabVIEW NXG Run-Time
 Engine. This option allows you to execute an individual code module in the
 Run-Time Engine, regardless of the server setting for the LabVIEW NXG Adapter.

#### TestStand LabVIEW NXG Conversion
 Utility

Use the TestStand LabVIEW NXG Conversion Utility to convert TestStand
 files that use LabVIEW code modules to refer to their converted LabVIEW NXG code modules.
 You can convert TestStand Workspaces (.tsw), Sequence Files
 (.seq), TestStand Deployment Specification files (.tsd),
 and the folders containing those files using the TestStand LabVIEW NXG Conversion Utility.

Note

The Conversion Utility
 application window contains the following panes:

- Files pane — This pane displays items added for conversion, their dependencies, and
 their status. The pane also indicates duplicate files and files that are called in a
 recursive loop (a file that calls itself at some point in its dependency hierarchy) that
 were added for conversion. You can navigate to the file from this pane by right clicking
 the file and selecting the Open Original option.
- Preview pane — This pane displays a preview of the output directory. When you start a
 preview, preconversion checks run on the files added for conversion, and any errors or
 warnings are reported in the log.
- Log pane — This pane displays and logs error, warning, and information messages that are
 generated during the conversion process.
- Call Hierarchy pane — This pane displays the call hierarchy of items and is shown when
 you click the Call Hierarchy button on any log message. The
 Call Hierarchy button appears only if the log message is about an
 item undergoing conversion.

#### TestStand API in LabVIEW
 NXG

TestStand 2017 includes full access to the TestStand API in LabVIEW NXG
 through the addition of a TestStand palette to the Functions palette. The palette includes
 VIs to call into the TestStand API as well as basic COM automation functionality to handle
 references to TestStand classes.

Note

#### Operator Interfaces in LabVIEW
 NXG

TestStand 2017 includes early access support for developing TestStand operator
 interfaces in LabVIEW NXG. TestStand 2017 populates the LabVIEW NXG controls palette with
 the same user interface controls as well as the same ApplicationMgr, ExecutionView, and
 SequenceFileView controls as is offered in other development environments. Overall
 development of TestStand operator interfaces offers a similar experience in LabVIEW NXG as
 LabVIEW.

To help get started with operator interface development in LabVIEW NXG, new
 versions of the Simple and Full-Featured UIs written fully in LabVIEW NXG are available as
 shipping examples with TestStand 2017. The examples can be found in the
 <TestStand Public>\TestStand 2017\UserInterfaces\
 directory.

#### HTBasic Adapter

In TestStand 2017 and later,
 the HTBasic Adapter is hidden by default. You can enable the HTBasic Adapter in 32-bit
 TestStand by selecting Configure»Adapters and opening the HTBasic Adapter Configuration Dialog
 Box.

#### INI Format

Saving to INI file format will be
 disallowed in future versions of TestStand.

Parent topic:

Updates and Changes for TestStand Extended Support Versions

<!--NI_TOPIC bundle=teststand path=teststand-2017-sp1-changes.html language=enus -->
## TOPIC 00879: TestStand 2017 SP1 Changes

- bundle_id: `teststand`
- source_path: `teststand-2017-sp1-changes.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/teststand-2017-sp1-changes.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `reference`
- source_description: Learn about new features, behavior changes, and other updates in TestStand 2017 SP1. LabVIEW Run-Time Engine Error Reporting ImprovementsThe LabVIEW Adapter can provide detailed error information about broken VIs when used with the LabVIEW 2018 or later run-time engine. Refer to Error Reporting for

### TestStand 2017 SP1 Changes

Learn about new features, behavior changes, and other updates in TestStand 2017
 SP1.

#### LabVIEW Run-Time Engine Error Reporting
 Improvements

The LabVIEW Adapter can provide detailed error information about
 broken VIs when used with the LabVIEW 2018 or later run-time engine. Refer to Error
 Reporting for Broken VIs in the LabVIEW Run-Time Engine for more information.

#### Use of TestStand Tools Without
 Activation

TestStand 2017 SP1 enables the use of several TestStand Tools without
 activation.

#### User-Editable Installer Executable
 Names

You can now set the installer name when you create distributions using the
 TestStand Deployment Utility.

#### Property Loader Comment Support for CSV,
 Excel, and Text Files

You can now use // characters to denote a
 comment in a CSV, Excel, or text file that the Property Loader step ignores when
 reading.

Note

#### INI File Support

Saving to and
 reading from TestStand files that use the INI file format will be deprecated in future
 versions of TestStand.

You can change the file format of a TestStand file to XML or
 binary formats in the following ways:

- Use the File Format Options dialog box, by selecting the
 File tab of the Station Options dialog box.
- Use the General tab of the Sequence File
 Properties dialog box, by selecting Edit»Sequence File
 Properties in the Sequence Editor.
- Use the Update Sequence Files tool, by selecting the
 Tools menu in the Sequence Editor.

Notice

#### Change
 in Installer File Name

(Windows) When you build an installer in TestStand, the
 default name of the executable changed from setup.exe to
 install.exe. This behavior change may have potential impact to post-build
 processes that rely on the setup.exe name. To specify a different name for
 the executable, use the Installer name option on the Product Information page of the
 Installer Properties dialog box.

Parent topic:

Updates and Changes for TestStand Extended Support Versions

Related concepts:

- Activating and Licensing TestStand

<!--NI_TOPIC bundle=teststand path=teststand-2019-changes.html language=enus -->
## TOPIC 00880: TestStand 2019 Changes

- bundle_id: `teststand`
- source_path: `teststand-2019-changes.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/teststand-2019-changes.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `reference`
- source_description: Learn about new features, behavior changes, and other updates in TestStand 2019. Quick Drop Dialog BoxIn previous versions of TestStand, you could only insert objects into the TestStand Sequence Editor using mouse clicks.TestStand 2019 introduces the Quick Drop dialog box, an easy way of inserting s

### TestStand 2019 Changes

Learn about new features, behavior changes, and other updates in TestStand
 2019.

#### Quick Drop Dialog Box

In previous
 versions of TestStand, you could only insert objects into the TestStand Sequence Editor
 using mouse clicks.TestStand 2019 introduces the Quick Drop dialog box,
 an easy way of inserting steps, sequences, and variables directly from a dialog without
 using mouse clicks.

#### Marking Sequence Analyzer Messages as Ignored
 in Sequence Files

The sequence analyzer provides the ability to mark analysis
 messages as ignored in sequence files. Marking an analysis message as ignored in a sequence
 file stores the message in the sequence file so that the sequence analyzer does not report
 the message for subsequent analysis of the sequence file. When you mark a message as
 ignored, the sequence analyzer now prompts for text that serves as a justification to ignore
 the message. The sequence analyzer stores the justification text with the analysis message
 and displays it in the Analysis Results pane when displaying ignored
 messages.

#### TestStand Deployment Utility
 Updates

The TestStand Deployment Utility added the following features:

- Support for building packages and offline package installers in the 32-bit TestStand
 Deployment Utility.
- A fourth field to the deployment version number and package version number in package
 distributions, using the format X.X.X.X. You can auto-increment the fourth field of the
 package version after each successful build, allowing you to rebuild packages without
 changing the major.minor.patch fields of the package version. For MSI Based Installers,
 the fourth field is not present to maintain compatibility with previous versions of
 TestStand, and versions continue to use the format X.X.X.
- Filtering options in the Package Dependencies dialog which allow you to configure the
 relationship of dependent packages. These options allow you to filter by the visibility
 level, package type, or specific search text.
- Support for deploying steps which use the Python adapter. The deployment utility
 includes any Python files included. TSDU also provides information for what versions of
 the Python interpreter are required, and what virtual environments are used by steps in
 the deployment.
- An option to configure whether code modules of step types are deployed for LabVIEW and
 LabVIEW NXG. When enabled, TSDU includes code modules in substeps of custom step types you
 create.
- Support for deploying files specified in the Override Module settings for LabVIEW
 steps.

#### Multicore Scaling
 Improvements

TestStand 2019 includes extensive optimizations for multicore
 processors. These improvements can significantly increase throughput for systems with high
 core counts running short duration tests on multiple UUTs in parallel. Performance
 improvements depend heavily on the specifications of your system.

#### PDF Report Generation

TestStand
 2019 introduces an option to generate PDF reports which look the same as the report
 generated through the result processor. The PDF report works for all formats except text.
 Even if OTF is enabled, PDF reports are generated only at the end of execution (PDF reports
 will not be generated for intermediate reports).

Navigate to
 Configure»Result Processing, click the icon in the Options column
 to launch the Report Options dialog, then select Generate PDF
 Report.

#### Data Streams Enhancements

TestStand
 2019 adds improved support for the data streams features.

- Stream Loop Step Type—Define a block of steps that execute for each element in
 an InputRecordStream . Optionally, you can specify an
 OutputRecordStream to write a record to at the end of each
 iteration.
- CSV Record Prototypes—CSV record streams now support specification of field names and
 data types. Use record prototypes to automatically map columns in a CSV file to records in
 a field.

#### Parametric Sweep

TestStand 2019
 adds the Sweep Loop step type to support Parametric Sweep applications. Use the Sweep Loop
 step type to define a set of sweep parameters and a block of steps to execute for each set
 of values the parameters sweep over. You can specify the range of each sweep parameter using
 one of several strategies. The default strategy is Start/Stop/Step. Other strategies include
 defining the sweep parameter as a constant value or specifying each value in the range using
 an array. Optionally, you can specify an OutputRecordStream to write sweep
 parameters (including outputs) at the end of each iteration.

#### Switching between Packed Project Libraries
 and VIs

The LabVIEW adapter now allows you to switch between packed project
 libraries and source VIs without having to reconfigure the step. This makes it easier for
 you to debug your packed project libraries. In previous versions of TestStand, you would
 have to reconfigure the step to point to the source VI in order to debug the issues present
 in a packed project library being called from a TestStand step. Now you can specify the
 packed project library source in the same step, which allows for seamless debugging.
 Additionally you can rebuild the packed project library from TestStand without switching to
 LabVIEW. In order to use this feature, navigate to the Override Module
 Settings window from the LabVIEW Step Settings panel to
 specify the source files (Project, VI, Build specification) of the packed project library.
 This window also provides a per-step override option, which allows you to choose between
 source VI or packed project library.

In the LabVIEW Adapter
 Configuration dialog box, you can override the module settings for all LabVIEW
 code modules to run either a source VI or a packed project library. You can also select the
 option of automatically building the packed project library. View these options on the
 Advanced tab in the LabVIEW Adapter
 Configuration dialog box.

#### LabWindows/CVI Integration
 Improvements

TestStand 2019 includes several improvements to the LabWindows/CVI
 adapter for TestStand that make the programming and debugging experience easier. There are
 three requirements for using these features:

- Install LabWindows/CVI 2019.
- In the LabWindows/CVI 2019 ADE, enable Add NI Type Information resource to
 DLL under Target Settings»Type Information .
- Rebuild DLLs that TestStand steps call using the LabWindows/CVI adapter.

#### Improved Handling of C
 Structs

Older versions of TestStand required users to manually create objects to
 represent C structs.This process was complicated, prone to error, and it required users to
 manually update their TestStand object every time the struct changed.

LabWindows/CVI
 2019 embeds information about structs into the LabWindows/CVI DLL and TestStand 2019 can
 read it. The TestStand LabWindows/CVI adapter now has a Create/Update Data
 Type button that can automatically generate a TestStand custom type
 definition to represent the C struct. If the struct changes in the LabWindows/CVI code
 module, users can update the TestStand type with a click of a button.

#### Improved Handling of Enums

Older
 versions of TestStand required the user to manually create enums to match the enums used in
 C. Enum information is now embedded into the LabWindows/CVI DLL, so users can automatically
 import and update their TestStand enums. When a function with an unknown enum is selected,
 the Create/Update Data Type option will appear.

#### Source Code Navigation

Older
 versions of TestStand required users to locate the .c file and the
 LabWindows/CVI project the first time they attempted to step into a LabWindows/CVI code
 module. LabWindows/CVI 2019 embeds the location of the .c and project file
 into the LabWindows/CVI DLL. When TestStand loads the DLL, it automatically fills this
 information into the Specify Module panel.

#### Pointer vs. Array Ambiguity

In C,
 pointer and one-dimensional array parameters have the same data type in function signatures.
 Even if you specify an array parameter using square braces, it is still passed as a pointer.
 Because C treats both syntaxes identically, earlier versions of TestStand required users to
 manually select whether a parameter was an array or pointer every time they called a
 LabWindows/CVI module with them.

TestStand 2019 automatically detects if a parameter
 is declared as an array using square brace syntax, and automatically defines the parameter
 as an array in the adapter. If the parameter includes an array size, Test Stand will
 automatically use that as the array size.

Additionally, users can use the
 ///OUT syntax to specify a parameter as a pointer. This will allow users
 to avoid the prompt. For more information, see the following tutorial: Using Source Code
 Tags to Enhance LabWindows™/CVI™ Code Documentation.

#### Python Adapter

The Python Adapter
 provides advanced functionality for calling Python code modules from TestStand. You can use
 the Python Adapter to complete the following tasks:

- Execute Python scripts ( .py ) on disk by:
  - Calling a function defined in a module.
  - Getting/Setting the attributes defined in a module.
  - Creating a class instance.
  - Calling a member function or static function defined in the class.
  - Getting/Setting member attributes or static attributes defined in the class.
- Execute Python scripts in Python versions 2.7 or 3.6+.
- Execute Python scripts out-of-process in the CPython interpreter.
- Convert data between Python and TestStand variables.
- Store/reuse the Python object in a TestStand variable (Object Reference).

You can also use multiple Python interpreter sessions to perform the following tasks:

- Execute Python scripts in parallel.
- Use multiple Python versions, such as 2.7 and 3.6, simultaneously in TestStand.

When you specify a module for a step, the TestStand Sequence Editor displays the
 Python Module tab. TestStand User Interfaces launch the
 Edit Python Call dialog box.

Use the Python Adapter
 Configuration dialog box to configure the Python version and Python virtual
 environment path to use with the Python Adapter.

Before using the Python Adapter in
 TestStand, you must install the required version of the CPython interpreter.

Note

#### IO Configuration Step
 Types

TestStand 2019 adds IO Configuration step types to control NI Modular
 Instruments NI-SCOPE, NI-DCPower, NI-DMM and NI-FGEN using InstrumentStudio. You can
 initialize an IO session, apply an IO configuration to an existing IO session and close an
 existing IO session for NI Modular Instruments. You can also use the Sweep Loop step type to
 sweep on the instrument attributes specified by an IO session.

Note

#### Deprecation of the INI File
 Format

Configuring TestStand files to save using the INI file format is deprecated
 in TestStand 2019. Saving files in INI file format will be deprecated in a future release of
 TestStand. In TestStand 2019, the following user interfaces now restrict you to selecting
 only the XML or binary formats:

- The File Format Options dialog box displayed when you select the
 File tab of the Station Options dialog box.
- The General tab of the Sequence File
 Properties dialog box displayed when you select Edit»Sequence File Properties in the Sequence Editor.
- The Update Sequence Files tool displayed when you select the Tools 
 menu in the Sequence Editor.

Note

#### Sequence File API

TestStand 2019
 introduces enforcing absolute paths for input parameter for the TestStand API's
 SequenceFile.Save() and
 SequenceAdapter.GetSequenceFile() methods. Previously, these methods did
 not enforce absolute paths for the input parameters.

Parent topic:

Updates and Changes for TestStand Extended Support Versions

Related information:

- Documentation Tags for Source Code in LabWindows/CVI
- Python Homepage

<!--NI_TOPIC bundle=teststand path=teststand-2020-changes.html language=enus -->
## TOPIC 00881: TestStand 2020 Changes

- bundle_id: `teststand`
- source_path: `teststand-2020-changes.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/teststand-2020-changes.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `reference`
- source_description: Learn about new features, behavior changes, and other updates in TestStand 2020. TestStand Sequence Editor Visual Design UpdatesTestStand 2020 introduces a streamlined visual design to the TestStand Sequence Editor. In addition to cosmetic changes, the sequence editor has the following changes: By d

### TestStand 2020 Changes

Learn about new features, behavior changes, and other updates in TestStand
 2020.

#### TestStand Sequence Editor Visual Design
 Updates

TestStand 2020 introduces a streamlined visual design to the TestStand
 Sequence Editor. In addition to cosmetic changes, the sequence editor has the following
 changes:

- By default, the sequence editor toolbar now only displays buttons that are global in
 scope. Buttons that provide functionality restricted to a single window or pane are now
 located in the relevant window or pane.
- Panes or tabs that provide configuration options for a single window are fixed to the
 relevant window.
- On the Steps pane, steps now have syntax highlighting. The icon color for a step
 indicates which type of step it is.
- Checkboxes in the Select Sequence File Callbacks dialog box simplify the process of
 selecting callback sequences.

#### Python Adapter
 Improvements

TestStand 2020 adds support for Python 3.8. You can now use the
 Python Adapter to perform the following tasks:

- Pass COM objects between TestStand and Python code modules.
- Map enums in TestStand to enums in Python code modules.
- Map arrays of numbers in TestStand to NumPy arrays in Python code modules.
- Include or exclude subproperties of a container of a named data type when passing it
 between TestStand and a Python code module.
- Enter either an individual file or a directory as a code module path for the Python
 Adapter.

#### Regular Expression Support

Regular
 expressions are now a supported comparison type for String Value Test steps. You can also
 use regular expressions as parameters for the CheckStrLimit,
 FindPattern, MatchPattern, and
 SearchPatternAndReplace expression functions.

#### InstrumentStudio Integration
 Improvements

TestStand 2020 introduces improvements to integration with
 InstrumentStudio. You can now perform the following tasks:

- Use Python code modules with IO Configuration step types.
- Pass the NI_IOSession data type between TestStand and Python code
 modules.

Parent topic:

Updates and Changes for TestStand Extended Support Versions

<!--NI_TOPIC bundle=teststand path=teststand-2021-changes.html language=enus -->
## TOPIC 00882: TestStand 2021 Changes

- bundle_id: `teststand`
- source_path: `teststand-2021-changes.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/teststand-2021-changes.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `reference`
- source_description: Learn about new features, behavior changes, and other updates in TestStand 2021. Sweep Loop Step EnhancementsTestStand 2021 expands the functionality of the existing Sweep Loop step. These updates include the following changes: You can create nested and parallel sweeps of parameters by changing the

### TestStand 2021 Changes

Learn about new features, behavior changes, and other updates in TestStand
 2021.

#### Sweep Loop Step
 Enhancements

TestStand 2021 expands the functionality of the existing Sweep Loop
 step. These updates include the following changes:

- You can create nested and parallel sweeps of parameters by changing the level of one or
 more parameters in a Sweep Loop step.
- TestStand automatically creates a variable when you specify a parameter name.
- You can choose between Static and Dynamic mode to specify whether values for a Strategy
 are specified using constants or expressions.
- You can use the Table View to interact with values and test vectors resulting from a
 sweep across selected parameters at edit time and run time. This functionality includes
 the ability to enable or disable, filter, and export test vectors.
- At execution time, use Table View to monitor captured data as well as the parameters in
 the Sweep Loop step.
- Added functionality to import and export parameter and test vector data to or from a CSV
 file.

#### Dropped
 Support for LabVIEW NXG Features

- LabVIEW NXG adapter
- LabVIEW NXG operator interfaces

#### New API and UI Controls

Note

- Enumeration and Constant Values
  - AutoCreateVariableLocationOption_Locals
  - AutoCreateVariableLocationOption_Parameters
  - AutoCreateVariableLocationOption_FileGlobals
  - AutoCreateVariableLocationOption_StationGlobals
  - EdgeStyle_UI
- Properties
  - AutoCreateVariableLocation
  - FrameEdgeUIStyleColor
  - GridLineColor
  - HeaderForegroundColor
  - InRedo
  - InUndo

Note

Parent topic:

Updates and Changes for TestStand Extended Support Versions

<!--NI_TOPIC bundle=teststand path=teststand-2021-sp1-changes.html language=enus -->
## TOPIC 00883: TestStand 2021 SP1 Changes

- bundle_id: `teststand`
- source_path: `teststand-2021-sp1-changes.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/teststand-2021-sp1-changes.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `reference`
- source_description: Learn about new features, behavior changes, and other updates in TestStand 2021 SP1. Enhanced Python Module Debugging The Python Adapter now supports step-into debugging of Python modules. Users who want to perform step-into operations with Python modules must install additional software, including

### TestStand 2021 SP1 Changes

Learn about new features, behavior changes, and other updates in TestStand 2021
 SP1.

#### Enhanced Python Module Debugging

- The Python Adapter now supports step-into debugging of Python modules. Users who want to
 perform step-into operations with Python modules must install additional software,
 including Visual Studio Code.

#### Support for HMTL Reports in Modern
 Browsers

- TestStand 2021 SP1 removes the dependency on Microsoft Internet Explorer for viewing
 TestStand reports. You can now view TestStand default reports in a modern browser without
 manually changing security settings.

#### Improved Error Reporting

- When possible, TestStand now provides information indicating where in the sequence file
 the error occurred.
- The error dialog box now displays information regarding the cause and possible
 resolutions for the error.

#### Updates to Input and Output Stream Parameter
 Capabilities

- Capabilities added to import parameters from and export parameters to CSV files.
- The Test Vector table is now marked as out-of-sync when changes are made to dynamic
 parameters in the Step Settings.

#### New and Obsolete API and UI
 Controls

TestStand 2021 SP1 includes the following new enumeration and constant
 values, properties and methods.

Note

- Enumeration and Constant Values
  - CommonDlgOptions_DisableGotoLocation
  - ReportViewButton_OpenReportLocation
  - VersionConstant_PatchVersion
- Properties
  - PatchVersion
  - SectionHeaderFontName
  - SectionHeaderFontSize
- Methods
  - DebugJustMyCode
  - DisplayErrorDialog
  - EnableDebugging
  - PythonExecutablePath
- Obsolete Properties, Methods, and Events Note Although some
 TestStand components, such as the TestStand Sequence Editor, expose .NET assemblies,
 TestStand does not support the use of undocumented .NET APIs.
  - ReportViewButton_FontSize

Parent topic:

Updates and Changes for TestStand Extended Support Versions

Related tasks:

- Debugging Python Modules

<!--NI_TOPIC bundle=teststand path=teststand-2022-q4-changes.html language=enus -->
## TOPIC 00884: TestStand 2022 Q4 Changes

- bundle_id: `teststand`
- source_path: `teststand-2022-q4-changes.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/teststand-2022-q4-changes.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `reference`
- source_description: Learn about new features, behavior changes, and other updates in TestStand 2022 Q4. Python Adapter Improvements Namespace Support — The Python Adapter now supports using namespaces when loading Python modules. Previously, TestStand would use only the file name when loading a Python module, which wou

### TestStand 2022 Q4 Changes

Learn about new features, behavior changes, and other updates in TestStand 2022
 Q4.

#### Python Adapter Improvements

- Namespace Support — The Python Adapter now supports using namespaces when loading Python
 modules. Previously, TestStand would use only the file name when loading a Python module,
 which would create a conflict when loading modules in different directories with the same
 name. You can now specify namespaces for Python modules and use modules with the same file
 name.
- Debugging Enhancements — You can now configure the Python Adapter to allow updates to
 Python code modules during execution. If you enable this option prior to execution,
 TestStand will reload an updated Python module without unloading other modules or
 restarting TestStand execution.
- Improved Information Displayed — If you install the Jedi package, TestStand can now
 display additional Python elements used in your code modules. With Jedi, you can configure
 the step settings for a Python step to use inner classes, methods and attributes from base
 classes for a selected child class, and classes, attributes, and functions available in
 the current namespace.

#### Expression Editor Improvements

- Delimiter Highlighting—The expression editor adds new visual assistance for finding and
 manipulating nested delimiters such as parentheses, brackets, and braces. Place your
 cursor to the left of a delimiter and the expression editor makes the matching pair bold.
 Click <Ctrl + ]> to toggle the cursor between the matching
 delimiters, or <Ctrl + Shift + ]> to select the matching
 delimiters and everything between them.
- Fixed Width Font—On machines where Lucida Sans Typewriter is installed, the expression
 editor uses that font to display text in the expression editor. When the font is absent,
 the expression editor uses the default TestStand font. One method for obtaining Lucida
 Sans Typewriter is to install Microsoft Office applications on the machine.

#### Floating-Point Number Representation in XML
 Sequence Files

TestStand 2022 Q4 fixes a bug in how floating-point numbers were
 stored in XML sequence files. Sequence files saved in binary format are unaffected by the
 bug. The fix for this issue is backwards compatible with existing sequence files but may
 produce unexpected differences when saving sequence files created with older versions of
 TestStand.

- Bug Details—TestStand Number objects with the default representation are standard IEEE
 double-precision floating point data types, sometimes called float64 .
 This type corresponds to the double data type in languages such as Java and .NET. In most
 cases C/C++ doubles use this format as well. Float64 is a binary data
 format. When TestStand stores Number objects in XML sequence files, the binary
 float64 format is converted to a base-10 (decimal) format. The
 conversion from binary to decimal format is not exact in all cases. If there is
 insufficient precision, the round-trip conversion may lead to a different value when the
 file is read. For IEEE double-precision floating-point numbers, 17 decimal digits are
 required to guarantee stable round-trip conversion. Previous versions of TestStand
 stored 16 decimal digits, causing the bug. Note Binary sequence files are
 not affected by this issue because binary sequence files store floating point numbers in
 their raw binary format.
- Bug Fix Details—TestStand 2022 Q4 uses 17 decimal digits when storing TestStand Number
 objects (with the default float64 representation) in XML sequence files.
- Impact—This change impacts saving sequence files. Existing sequence files will continue
 to load as before. (There was no issue with the loading code. The issue was purely the
 missing digit in the saved file.) Just as before, the value of number of objects read from
 an XML sequence file saved using prior versions of TestStand may differ from the value
 originally saved. The value read will match the value read with older versions of
 TestStand, so this should not cause compatibility issues. However, if you modify an XML
 sequence file created with an older version of TestStand, save the file with a different
 name, and then compare it to the original version using a differ, you may notice very
 small numeric differences in the values of saved numbers. For example, in some cases the
 original file may contain "3122.55" while the 2022 Q4 (22.0) version of the file
 contains "3122.5500000000002". This change is a result of the fact that
 "3122.5500000000002" is actually a more accurate numeric encoding of the underlying
 binary format in this example. Note The difference in numeric value will be
 small even though the length of the decimal encoding may be longer. Once a
 sequence file has been saved using TestStand 2022 Q4, round-trip conversions between
 binary and XML format will be stable.

#### New API and UI Controls

Note

- Enumeration and Constant Values
  - UIStyleColor_Background
  - UIStyleColor_Background2
  - UIStyleColor_Foreground
  - UIStyleColor_GridLine
  - UIStyleColor_HeaderForeground
  - UIStyleColor_SelectedBackground
  - UIStyleColor_SelectedForeground
  - UIStyleFontType_Proportional
  - UIStyleFontType_Monospaced
  - UIStyleFontType_SectionHeader
- Properties
  - GetColor
  - GetFontTypeName
  - GetFontTypeSize
- Methods
  - ReloadModifiedModulesDuringExecution

Note

Parent topic:

Updates and Changes for TestStand Extended Support Versions

<!--NI_TOPIC bundle=teststand path=teststand-activex-api-overview.html language=enus -->
## TOPIC 00885: TestStand ActiveX API Overview

- bundle_id: `teststand`
- source_path: `teststand-activex-api-overview.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/teststand-activex-api-overview.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use the TestStand ActiveX Automation server API to access the internal data of TestStand sequences and steps or to create and control sequence executions.

### TestStand ActiveX API Overview

You can use the TestStand ActiveX Automation server API to access the internal data of TestStand sequences and steps or to create and control sequence executions.

- [ActiveX Automation Server Concepts](activex-automation-server-concepts.html)
- [TestStand API Concepts](teststand-api-concepts.html)
- [Programming with the TestStand API in Different Languages](programming-with-the-teststand-api.html)

Parent topic:

TestStand API Overview

<!--NI_TOPIC bundle=teststand path=teststand-api-concepts.html language=enus -->
## TOPIC 00886: TestStand API Concepts

- bundle_id: `teststand`
- source_path: `teststand-api-concepts.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/teststand-api-concepts.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Core API Classes, Properties, and Methods topic includes a complete listing of the classes in the core TestStand API. The Adapter API Classes, Properties, and Methods topic includes a listing of adapter classes.

### TestStand API Concepts

The Core API Classes, Properties, and Methods topic includes a complete listing of the classes in the core TestStand API. The Adapter API Classes, Properties, and Methods topic includes a listing of adapter classes.

- [Accessing Built-in Properties](accessing-built-in-properties.html)
- [Accessing Dynamic Properties](accessing-dynamic-properties.html)
- [Acquiring a Derived Class from the PropertyObject Class](acquiring-a-derived-class.html)
- [Object Relationships](object-relationships.html)
- [Property Paths](property-paths.html)
- [Thread Concurrency Models](thread-concurrency-models.html)

Parent topic:

TestStand ActiveX API Overview

<!--NI_TOPIC bundle=teststand path=teststand-application-data-directory.html language=enus -->
## TOPIC 00887: <TestStand Application Data> Directory

- bundle_id: `teststand`
- source_path: `teststand-application-data-directory.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/teststand-application-data-directory.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The <TestStand Application Data> directory is hidden by default and contains configuration files users generally do not edit but an application can edit. The directory includes the Cfg subdirectory, which contains configuration files for TestStand Engine, TestStand Sequence Editor, and TestStand Use

### <TestStand Application Data>
 Directory

The <TestStand Application Data> directory is hidden by default and
 contains configuration files users generally do not edit but an application can
 edit. The directory includes the Cfg subdirectory, which
 contains configuration files for TestStand Engine, TestStand Sequence Editor, and
 TestStand User Interface options, as shown in the following table. You might need to
 deploy these files to a target computer when creating a deployment.

| Directory Name | Contents |
| --- | --- |
| SeqEdit directory | Default and saved layout files for the sequence editor. |
| Analyzer.ini | Settings for the TestStand Sequence Analyzer. |
| ConnectionSource.ini | Datalink list the Database and Legacy Property Loader step types use for configuration. |
| CustomRules.tsarules | Information about custom sequence analyzer rules and analysis modules. |
| DatabaseViewerOptions.ini | Configuration options for the Database Viewer application. |
| Deployment Utility RecentFiles.ini | Most recently used file list for the TestStand Deployment Utility. |
| DeploymentUtilityOptions.ini | Configuration options for the deployment utility. |
| DocGen.ini | Configuration options for the Sequence File Documentation tool. |
| EngineParts.ini | Deployment utility uses this file when you include the TestStand Engine in an installer. Note Do not edit this file. |
| ExpressMenu | Cache of Express VI menu for the specified LabVIEW version. |
| Filter.ini | List of files to exclude from deployment. |
| ModelPlugins\\ResultProcessing.cfg | Configuration options for result processing model plug-ins. |
| PLPropertyLoader.ini | Configuration options for the Legacy Property Loader Import/Export Properties tool. |
| ImportExportTool.ini | Configuration options for the Import/Export Properties tool. |
| StationGlobals.ini | Definitions and values of station global variables. |
| Templates.ini | Templates configuration for the Insertion Palette in the sequence editor. |
| Adapters.cfg | Settings related to the TestStand adapters. |
| SearchDirectories.cfg | Specifies TestStand search directories. |
| TypePalettes.cfg | Specifies locations of type palette files. |
| StartupCfg.ini | Settings needed prior to engine construction. |
| GeneralEngine.cfg | General engine settings including most station options. |
| TestStandModelOptions.ini | Model options for built-in process models. |
| TestStandDatabaseSchemas.ini | Database schemas for result logging. |
| TestStandPersistedOptions.opt | Persisted breakpoints and watch expressions to use when no workspace is loaded. |
| ToolMenu.ini | List of Tools menu items. |
| Users.ini | List of TestStand users. |
| XmlPack.ini | Contains a comma-separated string of file extensions for files you want to distribute using the XML Packaging Utility. |

Note

TestStandModelReportOptions.ini

TestStandDatabaseOptions.ini

ResultProcessing.cfg

<TestStand Application Data>\Cfg\ModelPlugins

TestStandDatabaseOptions.ini

TestStandDatabaseSchemas.ini

ResultProcessing.cfg

Parent topic:

TestStand Directory Structure

Related concepts:

- Creating Deployments
- Deploying TestStand Systems
- Customizing the Tools Menu
- Filtering and Excluding Files

<!--NI_TOPIC bundle=teststand path=teststand-building-blocks.html language=enus -->
## TOPIC 00888: TestStand Building Blocks

- bundle_id: `teststand`
- source_path: `teststand-building-blocks.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/teststand-building-blocks.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the following TestStand building blocks to create test systems.

### TestStand Building Blocks

Use the following TestStand building blocks to create test systems.

- [Sequences](sequences.html)
- [Steps](steps.html)
- [Code Modules](code-modules.html)
- [Properties](properties.html)
- [Variables](variables.html)
- [Expressions](expressions.html)
- [Process Models](process-models.html)
- [Standard and Custom Data Types](standard-and-custom-data-types.html)
- [Automatic Result Collection](automatic-result-collection.html)
- [Callback Sequences](callback-sequences.html)
- [Workspaces](workspaces.html)
- [Selecting a Source Code Control Provider](selecting-a-source-code-control-provider.html)

Parent topic:

Parts of a TestStand Application

<!--NI_TOPIC bundle=teststand path=teststand-components.html language=enus -->
## TOPIC 00889: Components of a TestStand System

- bundle_id: `teststand`
- source_path: `teststand-components.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/teststand-components.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: TestStand is designed for use in a test system along with hardware, drivers, and additional software to optimize TestStand for your application. Use the following list of typical TestStand system components as a starting point for building your test system. This topic should list all the products an

### Components of a TestStand System

TestStand is designed for use in a test system along with hardware, drivers, and
 additional software to optimize TestStand for your application. Use the following list of
 typical TestStand system components as a starting point for building your test system.

| Component | Notes |
| --- | --- |
| TestStand | Install TestStand using NI Package Manager. TestStand includes the TestStand engine, sequence editor, and user interface. |
| Code Modules | Code modules are programs invoked by TestStand. Create code modules in the supported application development environment (ADE) or programming language of your choice. |
| Module Adapters | Module adapters invoke code modules that your TestStand sequences call. TestStand installs several module adapters including, LabVIEW, .NET, and Python. This allows you to load and call code modules, pass parameters to code modules, and return values and status from code modules you created in a variety of programming languages. |
| Hardware and Drivers | The hardware and drivers required for your system depend on the device, component, and properties you want to test. Visit ni.com to explore the ecosystem of NI test and measurement hardware. |

Related concepts:

- Parts of a TestStand Application
- Module Adapters

Related information:

- Installing, Updating, Repairing, and Removing NI
 Software

<!--NI_TOPIC bundle=teststand path=teststand-constants-and-enums-cvi.html language=enus -->
## TOPIC 00890: Programming with TestStand API Constants and Enumerations in LabWindows/CVI

- bundle_id: `teststand`
- source_path: `teststand-constants-and-enums-cvi.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/teststand-constants-and-enums-cvi.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Some TestStand API methods require string and numeric constant input arguments. The acceptable values of these arguments are organized into groups that correspond to different properties and methods. For example, the PropertyObject.SetValNumber method includes an options input argument that accepts

### Programming with TestStand API Constants and Enumerations in LabWindows/CVI

Some TestStand API methods require string and numeric constant input arguments. The acceptable values of these arguments are organized into groups that correspond to different properties and methods. For example, the PropertyObject.SetValNumber method includes an options input argument that accepts many different numeric constants.

The header file for the ActiveX driver defines all constants and enumerations the methods and properties require. The constant and enumeration names start with a prefix, such as TS_, followed by the constant or enumeration name.

Note

tsapicvi.fp

TS_

NI TestStand Help

For example, the ActiveX driver defines the RunModes constant as follows:

#define TS_RunMode_Normal "Normal"

#define TS_RunMode_Skip "Skip"

#define TS_RunMode_ForceFail "Fail"

#define TS_RunMode_ForcePass "Pass"

The ActiveX driver defines the StepGroups enumeration as follows:

enum TSEnum_StepGroups

{

TS_StepGroup_Setup = 0,

TS_StepGroup_Main = 1,

TS_StepGroup_Cleanup = 2,

TS_StepGroupsForceSizeToFourBytes = 0xFFFFFFFF

};

For parameters of functions that use an enumeration type, the LabWindows/CVI function panel displays the list of enumerations in a ring control.

For parameters of functions that specify a numeric constant, use the bitwise-OR operator to specify multiple options. For example, the following code sets a local variable only when the variable does not already exist:

int options = PropOption_DoNothingIfExists | PropOption_InsertIfMissing;

tsErrChk (TS_PropertySetValNumber(seqContext, &errorInfo, "Locals.NumericValue", options, rand()));

Parent topic:

Programming with the TestStand API in LabWindows/CVI

<!--NI_TOPIC bundle=teststand path=teststand-constants-and-enums-labview.html language=enus -->
## TOPIC 00891: Programming with TestStand API Constants and Enumerations in LabVIEW

- bundle_id: `teststand`
- source_path: `teststand-constants-and-enums-labview.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/teststand-constants-and-enums-labview.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Some TestStand API methods require string and numeric constant input arguments. The acceptable values of these arguments are organized into groups that correspond to different properties and methods. For example, the PropertyObject.SetValNumber method includes an options input argument that accepts

### Programming with TestStand API Constants and Enumerations in LabVIEW

Some TestStand API methods require string and numeric constant input arguments. The acceptable values of these arguments are organized into groups that correspond to different properties and methods. For example, the PropertyObject.SetValNumber method includes an options input argument that accepts many different numeric constants.

To facilitate programming with the TestStand API within VIs and to help you manage all the available string and numeric constants for the TestStand API properties and methods, TestStand provides the following enumerated constant VIs:

- TestStand API String Constants VI —Locate and select the string constant arguments you can use with TestStand API properties and methods.
- TestStand API Numeric Constants VI —Locate and select the various numeric constant arguments you can use with TestStand API properties and methods.

Use both of these VIs in conjunction with the constants associated with the TestStand API methods and properties.

The block diagram in the following figure shows how to use the TestStand API Numeric Constants VI to obtain the value of the PropOptions_NoOptions constant.

[IMAGE alt='image' src='GUID-1C637F55-2B35-44BB-B5C2-665FC2EAF2EA-a5.png']

#### Combining Multiple Numeric Constants

Use the OR function in LabVIEW to combine more than one numeric constant. When you need to combine more than two constants, use the Compound Arithmetic function and set the mode to OR.

#### Creating Enumeration Input Parameters

Some TestStand API methods require enumeration input arguments. For these methods, right-click the input parameter on the Invoke Node in LabVIEW, select Create»Constant from the context menu to create a LabVIEW ring constant, and select the value you want in the resulting constant.

Parent topic:

Programming with the TestStand API in LabVIEW

<!--NI_TOPIC bundle=teststand path=teststand-crash-log-and-dump-file.html language=enus -->
## TOPIC 00892: TestStand Crash Log and Dump File

- bundle_id: `teststand`
- source_path: `teststand-crash-log-and-dump-file.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/teststand-crash-log-and-dump-file.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: TestStand creates the following files after a TestStand application crash: Dump file in <TestStand_LocalAppData>\NIERDump directory TestStand specific log file in <TestStand_LocalAppData>\CrashLogs directory You can use the configuration file to specify settings for the dump and TestStand specific l

### TestStand Crash Log and Dump File

TestStand creates the following files after a TestStand application crash:

- Dump file in <TestStand_LocalAppData>\NIERDump directory
- TestStand specific log file in <TestStand_LocalAppData>\CrashLogs directory

You can use the configuration file to specify settings for the dump and TestStand specific log file. The configuration file is an .ini file in the same directory as the TestStand application. The name of the configuration file must be same as the executable name of the TestStand application.

In the configuration file, create a section with the same name as the name of the executable. Use the following tokens and values to specify the options:

| Token Name | Value | Purpose |
| --- | --- | --- |
| TSLogType | None | Do not create TestStand crash log.By default, TestStand crash log is created. |
| NIER | False | Do not create NIER crash dump. By default, NIER crash dump is created. |
| NIERDumpType | Full | Create full (instead of mini) NIER crash dump.By default, mini dump file is created. |
| LogVariables | True | Enable logging of Locals, Parameters, and FileGlobals in the TestStand specific log file.By default, Locals, Parameters, and FileGlobals are not logged in the TestStand log file. |

Note

Note

The different configuration options combined with the number of different environments supported by TestStand affects how the crash recovery feature operates. Below is a table of different behaviors produced by the crash recovery feature in different scenarios:

| Behavior | Using TestStand 2017 in LabVIEW ADE | Using TestStand 2017 in all other scenarios | Using older version of TestStand in LabVIEW ADE | Using older version of TestStand in LabVIEW-built executable | Using older version of TestStand in all other scenarios |
| --- | --- | --- | --- | --- | --- |
| TestStand crash log | Created | Created | Not created | Not created | Not created |
| NIER dump | Created by TestStand | Created by TestStand | Created by LabVIEW | Created by LabVIEW | Not created |
| Send data to NI server | NIER dump is sent to NI server on user consent. | No data is sent to NI server. | NIER dump is sent to NI server on user consent. | No data is sent to NI server. | N/A |
| TSLogType=none in configuration file | TestStand log is not created. NIER dump is created. | TestStand log is not created. NIER dump is created. | N/A | N/A | N/A |
| NIER=false in configuration file | TestStand log is created. NIER dump is not created. | TestStand log is created. NIER dump is not created. | NIER dump is not created. | NIER dump is not created. | N/A |

#### Restrictions of using the feature

- Code modules should not register to functions like SetUnhandledExceptionFilter, set_invalid_parameter_handler, and set_purecall_handler to handle application crash.
- Crash due to out of memory is not supported.

Parent topic:

Crash Recovery for TestStand Applications

<!--NI_TOPIC bundle=teststand path=teststand-database-fundamentals.html language=enus -->
## TOPIC 00893: TestStand Database Fundamentals

- bundle_id: `teststand`
- source_path: `teststand-database-fundamentals.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/teststand-database-fundamentals.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: To use database logging in TestStand, you must have a working knowledge of database concepts, SQL, and database management system (DBMS) client software. Review the following key concepts for using databases with TestStand and the following key Microsoft Windows features TestStand uses to communicat

### TestStand Database Fundamentals

To use database logging in TestStand, you must have a working knowledge of database concepts, SQL, and database management system (DBMS) client software.

Review the following key concepts for using databases with TestStand and the following key Microsoft Windows features TestStand uses to communicate with a database management system (DBMS).

- [Databases and Tables](databases-and-tables.html)
- [Database Sessions](database-sessions.html)
- [Microsoft ADO, OLE DB, and ODBC Database Technologies](microsoft-ado-ole-db-and-odbc-database-techno.html)
- [Structured Query Language (SQL)](sql-ts.html) The Structured Query Language (SQL) is a widely supported standard for database access. You can use SQL commands to manipulate rows and columns in database tables in TestStand.
- [Format Strings for Database Date Values](format-strings-for-database-date-values.html)

Parent topic:

Database Logging

<!--NI_TOPIC bundle=teststand path=teststand-database-result-tables.html language=enus -->
## TOPIC 00894: TestStand Database Result Tables

- bundle_id: `teststand`
- source_path: `teststand-database-result-tables.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/teststand-database-result-tables.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use the default table schemas, modify the existing schemas, or create new schemas. Creating Default Result Tables with the Database Viewer Use the TestStand Database Viewer to create the default result tables the schema requires. You can also use the Database Viewer application to view data

### TestStand Database Result Tables

You can use the default table schemas, modify the existing schemas, or create new schemas.

#### Creating Default Result Tables with the Database Viewer

Use the TestStand Database Viewer to create the default result tables the schema requires. You can also use the Database Viewer application to view data in a database, edit table information, and execute SQL commands.

Note

Parent topic:

Database Logging

Related concepts:

- Default TestStand Table Schemas
- Adding Support for Other Database Management Systems
- Data Links
- Database Viewer—Creating Result Tables
- Logging Attribute Values

<!--NI_TOPIC bundle=teststand path=teststand-definition.html language=enus -->
## TOPIC 00895: TestStand Overview

- bundle_id: `teststand`
- source_path: `teststand-definition.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/teststand-definition.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: TestStand is test management software that helps you develop, debug, and deploy test systems and provides full visibility into testing processes and results. TestStand helps engineers quickly develop robust automated test and validation systems. Below is the product definition. In the angle brackets

### TestStand Overview

TestStand is test management software that helps you develop, debug, and deploy test
 systems and provides full visibility into testing processes and results. TestStand helps
 engineers quickly develop robust automated test and validation systems.

Related information:

- TestStand Licensing Options
- Interactive Activation Guide

#### TestStand Key Features

- Develop test sequences that integrate code modules written in any programming
 language
- Profile and optimize speed and parallelism before deploying test systems to
 production
- Meet the needs of any environment with extensible plug-ins for reporting, database
 logging, and connectivity to other systems
- Deploy test systems with increased throughput that run at production speed

<!--NI_TOPIC bundle=teststand path=teststand-deployment-utility.html language=enus -->
## TOPIC 00896: TestStand Deployment Utility

- bundle_id: `teststand`
- source_path: `teststand-deployment-utility.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/teststand-deployment-utility.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the deployment utility to create a deployable image or a patch deployment of a TestStand system and an optional installer. You can launch the TestStand Deployment Utility in the following ways: Select Tools»Deploy TestStand System in the TestStand Sequence Editor. (Windows 8.1) Click the NI Laun

### TestStand Deployment Utility

Use the deployment utility to create a deployable image or a patch deployment of
 a TestStand system and an optional installer.

You can launch the TestStand Deployment Utility in the following ways:

- Select Tools»Deploy TestStand System in the TestStand Sequence Editor.
- (Windows 8.1) Click the NI Launcher tile on the Start screen and select TestStand»Tools»TestStand Deployment Utility .
- (Windows 10 or 7) Select Start»All Programs»National Instruments»TestStand»Tools»TestStand Deployment Utility .

Note

.tsd

Note

Note

The deployment utility window contains the following tabs:

- Mode—Use this tab to create a full deployment or a patch deployment and to specify related settings for each type of deployment.
- System Source—Use this tab to specify the workspace file or directory that specifies which files to deploy and the location to create the deployment image.
- Distributed Files—Use this tab to view the files included in the deployment and configures the installer destination location and settings for each file.
- Installer Options—Use this tab to configure installer settings for the deployment and specifies which components to include from TestStand and other National Instruments software, such as hardware drivers.
- Package Installer Options—Use this tab to configure package-based distribution settings.
- Build Status—Use this tab to view progress and log information when analyzing files to include in a deployment and when building a deployment image and installer.

The deployment utility also contains the following buttons:

- Load —Loads the deployment settings from a previously saved ( .tsd ) file.
- Save —Saves the current deployment settings to the currently loaded ( .tsd ) file. When you create a patch deployment, the deployment utility appends the patch deployment information to the .tsd file.
- Save As —Saves the current deployment settings to a new ( .tsd ) file.
- New —Resets the current deployment settings to a new ( .tsd ) file.
- Build —Creates a deployable image and installer, according to the settings on the Installer Options tab.
- Done —Exits the deployment utility.

Parent topic:

TestStand Tools and Utilities

Related concepts:

- Patching Deployments
- Sequence Files
- Code Modules
- Process Models
- Deploying the TestStand Runtime
- Activating and Licensing TestStand
- Deploying TestStand Systems

Related information:

- TestStand Deployment Utility Environment Reference
- TestStand Deployment Utility Messages

<!--NI_TOPIC bundle=teststand path=teststand-directory-structure.html language=enus -->
## TOPIC 00897: TestStand Directory Structure

- bundle_id: `teststand`
- source_path: `teststand-directory-structure.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/teststand-directory-structure.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: To comply with Microsoft Windows restrictions on writing to the Program Files directory, TestStand 4.1 or later installs some files in different locations from previous versions of TestStand. Refer to the Directory Relocation section of the NI TestStand Version 4.2 Release Notes for more information

### TestStand Directory Structure

To comply with Microsoft Windows restrictions on writing to the Program Files directory, TestStand 4.1 or later installs some files in different locations from previous versions of TestStand. Refer to the Directory Relocation section of the NI TestStand Version 4.2 Release Notes for more information about specific directories and files relocated in TestStand 4.1 or later.

TestStand 2014 or later installs files in the following default directories:

| Directory | 32-bit TestStand | 64-bit TestStand |
| --- | --- | --- |
| <TestStand> | (32-bit Windows) C:\\Program Files\\National Instruments\\TestStand <version>(64-bit Windows) C:\\Program Files (x86)\\National Instruments\\TestStand <version> | C:\\Program Files\\National Instruments\\TestStand <version> |
| <TestStand Public> | (Windows 10/8.1/7) C:\\Users\\Public\\Documents\\National Instruments\\TestStand <version> (32-bit) | C:\\Users\\Public\\Documents\\National Instruments\\TestStand <version> (64-bit) |
| <TestStand Application Data> (Hidden by default) | (Windows 10/8.1/7) C:\\ProgramData\\National Instruments\\TestStand <version> (32-bit) | C:\\ProgramData\\National Instruments\\TestStand <version> (64-bit) |
| <TestStand Local Application Data> (Hidden by default) | (Windows 10/8.1/7) <User Directory>\\AppData\\Local\\National Instruments\\TestStand <version> (32-bit) | <User Directory>\\AppData\\Local\\National Instruments\\TestStand <version> (64-bit) |

TestStand adds the TestStand, TestStandAppData, and TestStandPublic environment variables that reference the <TestStand>, <TestStand Public>, and <TestStand Application Data> directories respectively. You can use the environment variables in development environments to specify paths to files in these TestStand directories. For example, you can use these environment variables to build paths in the Additional Include Directories control in Visual Studio.

Refer to the Defining an Environment topic for more information about using environment variables in side-by-side TestStand environments.

Parent topic:

Extending TestStand

Related concepts:

- TestStand Directory
- TestStand Public Directory
- <TestStand Application Data> Directory
- TestStand Local Application Data Directory
- Defining an Environment
- TestStand Environments

<!--NI_TOPIC bundle=teststand path=teststand-directory.html language=enus -->
## TOPIC 00898: TestStand Directory

- bundle_id: `teststand`
- source_path: `teststand-directory.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/teststand-directory.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following table shows the name and contents of each subdirectory of the <TestStand> directory, which is where you installed TestStand on the computer and contains the read-only program files. 38 Contents of the TestStand Directory Directory Name Contents AdapterSupport Read-only support files fo

### TestStand Directory

The following table shows the name and contents of each subdirectory of the
 <TestStand> directory, which is where you installed
 TestStand on the computer and contains the read-only program files.

| Directory Name | Contents |
| --- | --- |
| AdapterSupport | Read-only support files for the .NET and HTBasic Adapters. |
| API | Read-only TestStand ActiveX Automation server libraries and utility libraries for several programming languages. |
| Bin | Read-only TestStand Sequence Editor executable, TestStand Engine DLLs, and support files. |
| CodeTemplates | Read-only source code templates for step types. |
| Components | Read-only components installed with TestStand, including callback files, converters, icons, language files, process model files, step types, source files, compatibility files, utility files, and sequence analyzer files. |
| Doc | Documentation files. |
| UserInterfaces | Read-only LabVIEW, LabWindows/CVI, Microsoft Visual Basic, C#, and C++ (MFC) user interfaces with source code. |

Parent topic:

TestStand Directory Structure

Related concepts:

- Components Directory

<!--NI_TOPIC bundle=teststand path=teststand-enumerations-reference-guide.html language=enus -->
## TOPIC 00899: TestStand Enumerations Reference Guide

- bundle_id: `teststand`
- source_path: `teststand-enumerations-reference-guide.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/teststand-enumerations-reference-guide.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`

### TestStand Enumerations Reference Guide

- [Enumerations as Numbers](enumerations-as-numbers.html)
- [Enumerations as PropertyObjects](enumerations-as-propertyobjects.html)
- [Enumerations in TestStand Expressions](enumerations-in-teststand-expressions.html)
- [Using Enumerations with the TestStand Adapters](using-enumerations-with-the-teststand-adapter.html)

Parent topic:

Using Enumerations in TestStand

<!--NI_TOPIC bundle=teststand path=teststand-environments.html language=enus -->
## TOPIC 00900: TestStand Environments

- bundle_id: `teststand`
- source_path: `teststand-environments.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/teststand-environments.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: TestStand environments enable two or more TestStand system configurations to exist side-by-sideon a single system. You can specify unique application data directories and public folders for each configuration of TestStand, allowing settings, custom components, and variables normally global to the sy

### TestStand Environments

TestStand environments enable two or more TestStand system configurations to exist side-by-sideon a single system. You can specify unique application data directories and public folders for each configuration of TestStand, allowing settings, custom components, and variables normally global to the system to be maintained separately within each environment. For example, each TestStand environment can independently maintain its own station globals, type palettes, and customized process models.It is important to note some limitations of TestStand environments:

- TestStand environments do not eliminate the requirement to version switch when changing between different versions of TestStand installed on a system.
- Environments do not provide full isolation for simultaneously executing instances of the TestStand engine. While it is possible to run multiple instances of the TestStand engine simultaneously, each in a different environment, some features of TestStand, such as out-of-process synchronization objects, are shared by all running instances.
- The TestStand remote engine does not currently support environments and therefore always runs in the global environment.

Parent topic:

Fundamentals

Related concepts:

- Defining an Environment
- Environment Behavior
- Choosing an Environment
- General Environment Limitations
- Changing Environments

<!--NI_TOPIC bundle=teststand path=teststand-file-diff-and-merge-utility.html language=enus -->
## TOPIC 00901: TestStand File Diff and Merge Utility

- bundle_id: `teststand`
- source_path: `teststand-file-diff-and-merge-utility.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/teststand-file-diff-and-merge-utility.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the TestStand File Diff and Merge utility to compare and merge non-type differences among two or three sequence files and compare type differences among two sequence files or type palette files. You can launch this utility in the following ways: (Windows 8.1) Click the NI Launcher tile on the St

### TestStand File Diff and Merge Utility

Use the TestStand File Diff and Merge utility to compare and merge non-type
 differences among two or three sequence files and compare type differences among two
 sequence files or type palette files.

You can launch this utility in the following ways:

- (Windows 8.1) Click the NI Launcher tile on the Start screen and select TestStand»Tools»TestStand File Diff and Merge Utility .
- (Windows 10 or 7) Select Start»All Programs»National Instruments»TestStand Shared»TestStand File Diff and Merge Utility .
- Run <TestStand>\Bin\FileDiffer.exe .

In the Sequence Editor, you can select the Edit»Diff Sequence File Against and Edit»Diff Against Saved Version menu options to launch the TestStand File Diff and Merge Utility to compare an opened sequence file to a file on disk.

The Select Files dialog box launches when you launch the utility. Use the Diff tab of the Select Files dialog box to specify two sequence files or type palette files you want to compare. Use the Merge tab to specify three sequence files you want to compare—a base file from which modified versions originate and two modified versions—and a fourth sequence file to become the resulting merged file to create.

Click the Options button in the Select Files dialog box to launch the File Differ Options dialog box, in which you can configure settings for the utility, including options for loading and automatically merging types, managing type conflict resolution, and so on.

When you specify files to compare in the Select Files dialog box and click OK, the utility launches the main window, which contains the following information:

- File List—The specified files you are comparing and a count of changes, insertions, and deletions for each file.
- Differences Table—Displays the differences grouped by sequences, file global variables, file properties, and types for each specified file.
- Filters Tab—Hide properties with no differences in the Differences window.

#### Source Code Control

TestStand includes a shared launching application you can use with third-party source
 code control (SCC) providers and Git clients that support launching an external
 application to perform two- and three-way file diff and merge operations. The
 launching application determines the active version of TestStand and launches the
 corresponding TestStand diff application that version of TestStand installs. Using
 the launching application alleviates the requirement to reconfigure the SCC provider
 or Git client each time you activate a different version of TestStand. Launch the
 application by running <National
 Instruments>\Shared\TestStand\FileDifferLauncher.exe.

#### Command-Line Usage

You can also specify files to compare using command-line arguments for the application. You typically use the application to compare files in a source code control system. For example, use the following command-line syntax to specify file paths to a base file, two modified versions, and the resulting merged file to create:

FileDiffer.exe "C:\My Documents\File1.seq" "C:\My Documents\File2.seq" "C:\My Documents\File3.seq" "C:\My Documents\Merged.seq"

Use the following command-line syntax to launch a dialog box that lists all the command-line arguments you can use for the application.

FileDiffer.exe /?

or

FileDiffer.exe /help

To launch the File Diff and Merge Utility in a specific TestStand environment, use the following command line argument:

/env <environment path>

where <environment path> is the location of the .tsenv file that defines the environment.

Note

The following command-line tokens are supported in the help.

- /env <environment path> —Specify the TestStand environment.
- /matchStepsByID:{Y|N} —Require step IDs to match. Provide N for disabling the option.
- /TypeMerging:{Y|N} —Enable or disable automatic type merge.
- /ProcessModelLoading:{Y|N} —Enable or disable process model loading.
- /TypePaletteLoading:{Y|N} —Enable or disable loading type palettes.
- /IgnoreShared:{Y|N} —Enable or disable ignoring differences in variables with the shared property.
- /AutoResolveShared:{N|Base|File1|File2} —Automatically resolve ignored shared conflicts. Requires /IgnoreShared:Y .
- /IgnoredMinorModule:{Y|N} —Enable or disable ignoring minor module differences.
- /AutoResolveMinorModule:{N|Base|File1|File2} —Automatically resolve ignored minor module conflicts. Requires /IgnoreMinorModule:{Base|File1|File2} .
- /GenerateReport <reportPath.xml> —Automatically generate the diff report and then exit. To have this run synchronously from a batch script use the 'start' command with the '/wait' parameter to launch the process.

Parent topic:

TestStand Tools and Utilities

Related concepts:

- Selecting a Source Code Control Provider
- Search Directories
- TestStand Environments

Related information:

- Git Pane
- TestStand File Diff and Merge Utility Environment Reference

<!--NI_TOPIC bundle=teststand path=teststand-file-extensions.html language=enus -->
## TOPIC 00902: TestStand File Extensions

- bundle_id: `teststand`
- source_path: `teststand-file-extensions.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/teststand-file-extensions.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following table includes common file types that TestStand creates and uses to save data. 9 TestStand File Extension Descriptions File Extension Description .c C source file. .dll Dynamic Link Library file. .html HyperText Markup Language file. TestStand can use the HTML file format for test repo

### TestStand File Extensions

The following table includes common file types that TestStand creates and uses to save data.

| File Extension | Description |
| --- | --- |
| .c | C source file. |
| .dll | Dynamic Link Library file. |
| .html | HyperText Markup Language file. TestStand can use the HTML file format for test reports. |
| .ini | Standard Microsoft Windows configuration settings file. Used to store most TestStand configuration information. |
| .llb | LabVIEW library file. |
| .lvclass | LabVIEW class library file. The class library file defines a new data type. |
| .lvlibp | LabVIEW packed project library. LabVIEW packed libraries package multiple files into a single file. |
| .lvproj | LabVIEW project. |
| .seq | Sequence file. Sequence files are the files in which TestStand applications are written. |
| .tsaproj | TestStand Sequence Analyzer project. Specifies the files to analyze and the rules and related settings to use during the analysis. |
| .tpj | TestStand Project file. A project file can store and organize the set of files used in a TestStand application. |
| .tsd | TestStand Deployment Utility deployment file. Contains the information to build a full deployment or a patch deployment. |
| .tso | Workspace options file. TestStand saves information in this file to preserve certain user settings, such as window positions, source code control information, and the expansion state of the Workspace pane. |
| .tsr | TestStand raw results file. Stores results in a compressed format for later processing. |
| .tsw | TestStand workspace file. A workspace file can store TestStand project files. |
| .txt | Text file. |
| .vi | LabVIEW virtual instrument. |
| .xml | Extensible Markup Language file. TestStand can use the XML file format for test reports. |
| .xsl | Extensible Stylesheet Language file. TestStand uses these files to apply formatting to XML test reports. |

Parent topic:

Parts of a TestStand Application

Related concepts:

- Organizing Test Program Files with LabVIEW Projects
- Deploying TestStand Systems
- Patching Deployments
- Generating and Customizing TestStand Reports

<!--NI_TOPIC bundle=teststand path=teststand-licensing-options.html language=enus -->
## TOPIC 00903: Activating and Licensing TestStand

- bundle_id: `teststand`
- source_path: `teststand-licensing-options.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/teststand-licensing-options.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: After you install TestStand, you must use NI License Manager to activate the software or initiate the evaluation period for the software. Activate TestStand using one of the following activation methods: Log in to your NI user account to check for associated licenses Enter the serial number on the C

### Activating and Licensing TestStand

After you install TestStand, you must use NI License Manager to activate the software
 or initiate the evaluation period for the software.

- Log in to your NI user account to check for associated licenses
- Enter the serial number on the Certificate of Ownership included with your TestStand
 software kit
- Enter an activation code
- Connect to a volume license server

- TestStand Development System License
- TestStand Continuous Integration License
- TestStand Custom Sequence Editor License
- TestStand Debug Deployment Environment License
- TestStand Base Deployment Engine License

Use the following descriptions only as a reference for the licensing options. Refer to
 ni.com/activate for more information about activating TestStand licenses. Refer to
 ni.com/teststand to purchase a TestStand license. Contact a local NI representative for more
 information or for questions about specific licensing needs.

Note

<National
 Instruments>\Shared\MDF\EULAs\NIReleased

| License Name | Part Number |
| --- | --- |
| TestStand Development System License | 788372-35 |
| TestStand Continuous Integration License for VLAs | 790410-35 |
| TestStand Custom Sequence Editor License | 777775-35 |
| TestStand Debug Deployment Environment License | 779851-35 |
| TestStand Base Deployment Engine License | 777774-35 |

#### TestStand Evaluation Package

When you run TestStand in Evaluation Mode, the
 software expires after 7 days. The software runs as a fully functional Development System
 during the evaluation period. You can use an ni.com user profile to extend the evaluation
 period for an additional 45 days. You can activate a license at any point during or after
 the evaluation period.

#### TestStand Development System License

- Design, debug, and develop sequences
- Develop a User Interface
- Create a deployment
- Develop a Custom Sequence Editor
- Use TestStand on an additional machine or container within a continuous integration
 (CI) or continuous development (CD) workflow

#### TestStand Continuous Integration License

Use the TestStand Continuous Integration
 license to include TestStand in your CI/CD workflows at no additional
 cost.

Single-Seat License Users

If you have an individual
 TestStand Development System license, you can use TestStand on an additional machine or
 container for CI/CD workflows such as automated software building. Enterprise agreements
 also allow you to use TestStand for CI/CD workflows.

Volume License Agreement
 Users

TestStand Continuous
 Integration for VLAs

790410-35

Note

TestStand Continuous Integration for
 VLAs

#### TestStand Custom Sequence Editor License

Note

- Design, debug, and develop sequences within a Custom Sequence Editor
- Create a deployment

#### TestStand Debug Deployment Environment License

Activate this license to install
 the development versions of TestStand, LabVIEW, LabWindows/CVI, MeasurementStudio, and any
 corresponding add-on toolkits on a single test station so you can debug deployed test
 applications on the test station. This license grants the right to make minor edits to fix
 bugs in deployed test applications but does not grant the right to perform any development
 tasks, such as adding or improving application functionality, using TestStand, LabVIEW,
 LabWindows/CVI, or MeasurementStudio on the test station.

You cannot activate and
 deactivate the TestStand Debug Deployment Environment license and reuse it on multiple
 computers. If you need to use a single debug license across multiple computers, contact NI
 for more information about the Concurrent TestStand Debug Deployment Environment
 license.

- Debug test sequences on a deployed machine

#### TestStand Base Deployment Engine License

Note

- Execute TestStand deployments

| License | Behavior |
| --- | --- |
| TestStand Development System License | The license must be current with the SSP to reactivate a service pack license. |
| TestStand Debug Deployment Environment License | The license must be current with the SSP to reactivate a service pack license. |
| TestStand Custom Sequence Editor License | You can reactivate the license for a service pack upgrade even if the SSP for the original license lapsed. |
| TestStand Base Deployment Engine License | Does not require SSP to reactivate a service pack license. |

#### TestStand Tools That Do Not Require
 Activation

The following tools do not require activation for build or analysis purposes, as defined by
 the license agreement:

- TestStand Deployment Utility
- Update VI Calls Application
- TestStand Sequence Analyzer
- Offline Results Processing Utility
- File Diff and Merge Utility (You can diff, but not save, sequence files)
- XML File Packaging Utility
- Database Viewer

Related concepts:

- TestStand User Manual

Related information:

- License Setup and Activation
- Activating Software
- Purchase a TestStand License

<!--NI_TOPIC bundle=teststand path=teststand-local-application-data-directory.html language=enus -->
## TOPIC 00904: TestStand Local Application Data Directory

- bundle_id: `teststand`
- source_path: `teststand-local-application-data-directory.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/teststand-local-application-data-directory.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The <TestStand Local Application Data> directory is hidden by default and contains configuration files users generally do not edit but an application can edit, as shown in the following table. 40 Contents of the TestStand Local Application Data Directory Directory Name Contents Layout_current.bin di

### TestStand Local Application Data Directory

The <TestStand Local Application Data> directory is hidden by default
 and contains configuration files users generally do not edit but an application can
 edit, as shown in the following table.

| Directory Name | Contents |
| --- | --- |
| Layout_current.bin directory | Layout of the TestStand Sequence Editor the last time it was closed, including window position, size, docked state, and other settings for the panes, menus, and toolbars. |
| SeqEdit.xml | Configuration options for the sequence editor, such as panel size and font settings used on the Insertion Palette pane and the Variables pane. |
| UserInterface.xml | Configuration options for TestStand User Interfaces, such as window and panel sizes, font settings, and sequences to load. You can customize the data stored in this file. |

Parent topic:

TestStand Directory Structure

<!--NI_TOPIC bundle=teststand path=teststand-migration-utility.html language=enus -->
## TOPIC 00905: TestStand Migration Utility

- bundle_id: `teststand`
- source_path: `teststand-migration-utility.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/teststand-migration-utility.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the TestStand Migration Utility to copy settings, configuration, and public component files from the folders of previous versions of TestStand to the current version of TestStand. With TestStand 2014 or later, you can also migrate from 32-bit TestStand to 64-bit TestStand or from 64-bit TestStan

### TestStand Migration Utility

Use the TestStand Migration Utility to copy settings, configuration, and public
 component files from the folders of previous versions of TestStand to the current
 version of TestStand.

With TestStand 2014 or later, you can also migrate from 32-bit TestStand to 64-bit TestStand or
 from 64-bit TestStand to 32-bit TestStand. National Instrument recommends migrating
 between bitnesses only within the same version of TestStand.

You can launch the utility in the following ways:

- (Windows 7) Select Start»All Programs»National Instruments»TestStand»Tools»Compatibility»TestStand Migration Utility .
- (Windows 8.1) Click the NI Launcher tile on the Start screen and select TestStand»Tools»Compatibility»TestStand Migration Utility .
- (Windows 10) Select Start»National Instruments»TestStand Migration Utility .

Use the Files to Copy section to specify the files you want to copy. By default, the migration utility selects files you added or modified in the previous version of TestStand. Expand the directories in the Files to Copy control to view the files you can migrate and determine whether those files have changed since installation. The Conflicts column includes any conflicts that could affect the migration of the files you specify.

The Files to Copy section includes three columns.

- Files to Migrate —Expand the directories to view and select the files to migrate to the current version of TestStand. When you enable a file for migration, the Migration Action column updates to display the necessary action.
- Since Install —Indicates whether a file has changed or has been added since you installed TestStand 2012 or later.
- Migration Action —Indicates whether the Migration Utility copies the files to a folder in the current version of TestStand or overwrites an existing file in a folder in the current version of TestStand. The utility adds the contents of a copied folder to the contents of a folder in the current version of TestStand if a corresponding folder already exists. The Migration Action column displays the following actions:
 
The Migration Action column is empty for files not selected for migration.
  - Copy —The file does not exist in the previous version of TestStand.
  - Overwrite —The file exists in the previous version of TestStand. The migration utility will overwrite the existing file.
  - Overwrite readonly —The file exists in the previous version of TestStand but is read-only. The migration utility will not overwrite the existing file.

Enable the Hide Files not modified since installing TestStand option to show only files modified or created in the version of TestStand you are migrating from.

Use the Location for backup of TestStand public files control to specify the location where the Migration Utility stores the backup copy of the files before performing the copy.

Note

- This utility overwrites any file in the current version of TestStand if the file also exists in the corresponding folder for the previous version of TestStand and if the file is selected in the Files to Copy control. Although the Migration Utility creates a backup copy of all overwritten files, National Instruments recommends that you verify that the utility will not overwrite any files in the current version of TestStand that you intend to keep.
- If the <TestStand Public>\Components directory of the previous version of TestStand includes files installed by an installer other than the TestStand installer, you might need to use that specific installer to move the files for the files to function and uninstall properly from the <TestStand Public>\Components directory of the current version of TestStand. National Instruments recommends that you use an installer that targets the current version of TestStand to install any such components instead of using the migration utility to copy the components. However, some installed components can function properly when copied to another directory and are safe to migrate with the migration utility. The migration utility only moves files and does not update any other information or settings, such as registry keys.
- The utility does not copy files in the <TestStand Public>\Examples , <TestStand Public>\Tutorial , or <TestStand Public>\AdapterSupport directories. These directories do not appear in the Files to Migrate column of the utility.

#### Cross-Bitness Migration

National Instruments recommends upgrading to 64-bit TestStand 2014 in two steps. First upgrade to 32-bit TestStand 2014 and validate that the system works as expected, and then migrate from 32-bit TestStand 2014 to 64-bit TestStand 2014. Performing the upgrade in two steps can help isolate the root cause of issues you might encounter.

Migrating to 64-bit TestStand might require additional manual steps after the Migration Utility completes. You must update bitness-specific files to support the new architecture. For example, if the Migration Utility copies a LabWindows/CVI DLL code module from 32-bit TestStand to 64-bit TestStand, 64-bit TestStand cannot load the 32-bit DLL. You must replace the 32-bit DLL with an equivalent 64-bit DLL. Additionally, code modules you place or install under the <TestStand Public> directory might require additional work depending on the type and implementation of the code module.

- [Process Model Changes in TestStand 2012 or Later and the Migration Utility](process-model-changes-in-teststand-2012-or-la.html)

Parent topic:

TestStand Tools and Utilities

Related concepts:

- Search Directories
- 64-bit TestStand and Migrating from 32-bit TestStand
- Process Model Plug-In Architecture
- TestStand Offline Results Processing Utility

Related tasks:

- Manually Migrating Result Processing Options from Any Version of TestStand

Related information:

- Legacy Model Switcher
- Results Processing Dialog Box
- TestStand Migration Utility Environment Reference

<!--NI_TOPIC bundle=teststand path=teststand-offline-results-processing-utility.html language=enus -->
## TOPIC 00906: TestStand Offline Results Processing Utility

- bundle_id: `teststand`
- source_path: `teststand-offline-results-processing-utility.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/teststand-offline-results-processing-utility.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use this utility to process raw results files into reports and database tables at a time other than when sequence execution occurs, such as overnight, or on a different computer. You can launch the TestStand Offline Results Processing Utility in the following ways: Select Tools»Offline Results Proce

### TestStand Offline Results Processing Utility

Use this utility to process raw results files into reports and database tables at
 a time other than when sequence execution occurs, such as overnight, or on a different
 computer.

You can launch the TestStand Offline Results Processing Utility in the following ways:

- Select Tools»Offline Results Processing Utility in the TestStand Sequence Editor.
- (Windows 8.1) Click the NI Launcher tile on the Start screen and select TestStand»Tools»Offline Results Processing Utility .
- (Windows 10 or 7) Select Start»All Programs»National Instruments»TestStand»Tools»TestStand Offline Results Processing Utility .

Use this utility in situations in which performance is more important than immediately processing
 results. You can use 64-bit TestStand to process files that 32-bit TestStand generates
 and vice versa. If 32-bit TestStand returns out of memory errors while processing a TSR
 file, process the file with 64-bit TestStand, which can use more memory during
 processing.

Select Profile»New or right-click in the Profiles pane and select New Profile from the context menu to create a profile. Use profiles to define a set of raw results files to process, to specify the result processing configuration set to use to process results, to specify the sequence file to use as the callback sequence file when processing the raw results files, and to track the set of files the utility has already processed. Use the inbox of a profile to specify where to store raw results files to process, and use the outbox of a profile to specify where to store raw results files and reports after processing. You can configure the number of files the utility processes simultaneously.

The utility creates a new execution to process raw results files into reports and database tables. This execution calls callbacks for offline results processing in the same manner as normal results processing. Use the Default Callback File option in the TestStand Offline Results Processing Utility Settings dialog box to specify a default callback file for all profiles, or specify a callback file for each profile in the profile grid.

The utility selects the callback file used to process results based on the following criteria:

1. If you specify a callback file for a profile, the utility will use that callback file to process results.
2. If you do not specify a callback file for a profile, the utility will use the default callback file to process results.
3. If you do not specify a callback file for a profile and do not specify a default callback file, the utility will not use any callback file.

When files exist in the inbox of a profile, the utility will load both the specified callback file for the profile and the default callback file, even when the profile is paused. The utility will unload the callback files shortly after the last file is moved out of the inbox.

Note

The Report List pane displays the list of reports the utility generated from the raw results file of the same name. Use the Next Report and Previous Report buttons to show the next or previous unread report. An unread report is one that the utility has not opened during the current session. This pane also uses the same controls as the Report pane in the sequence editor Execution window.

Select File»Settings to launch the TestStand Offline Results Processing Utility Settings dialog box, in which you set utility configuration options. If you are processing TSR files with a large number of results, use the Number of Files Processed Simultaneously option in this dialog box to reduce memory usage.

The status bar of the utility displays the default callback file and the report you selected in the Report List pane.

You can use command-line arguments or a Call Executable step with command-line arguments in a sequence to launch the offline results processing utility.

<TestStand>

\Components\Tools\Offline Results Processing Utility\OfflineResultsProcessingUtility.exe

/quit

Note

Note

Parent topic:

TestStand Tools and Utilities

Related concepts:

- Search Directories

Related information:

- Call Executable Step
- Execution Window
- TestStand Offline Results Processing Utility Environment Reference

<!--NI_TOPIC bundle=teststand path=teststand-process-models.html language=enus -->
## TOPIC 00907: TestStand Process Models

- bundle_id: `teststand`
- source_path: `teststand-process-models.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/teststand-process-models.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Sequential model is the default process model that you use to test one UUT at a time. Use the Parallel and Batch process models to simultaneously run the same test sequence on groups of similar UUTs. Select Configure»Model Options to launch the Model Options dialog box to specify the number of t

### TestStand Process Models

The Sequential model is the default process model that you use to test one UUT at a time. Use the Parallel and Batch process models to simultaneously run the same test sequence on groups of similar UUTs. Select Configure»Model Options to launch the Model Options dialog box to specify the number of test sockets in the test system.

The following table lists the process models and their respective sequence files.

| Process Model | Process Model Sequence File |
| --- | --- |
| Sequential Model | <TestStand>\\Components\\Models\\TestStandModels\\SequentialModel.seq |
| Parallel Model | <TestStand>\\Components\\Models\\TestStandModels\\ParallelModel.seq |
| Batch Model | <TestStand>\\Components\\Models\\TestStandModels\\BatchModel.seq |

You can create a custom process model, or you can modify a copy of a built-in process models.

To modify the installed process model or to create a new process model, copy all the process model files from the <TestStand>\Components\Models\TestStandModels directory to <TestStand Public>\Components\Models and make changes to the copy.

The list of search paths includes the subdirectories in the <TestStand Public>\Components directory.

When you create a custom process model, use the Model tab of the Station Options dialog box to specify the custom process model sequence file as the process model for the station.

Note

<TestStand>\Components\Models\TestStandModels

<TestStand Public>\Components\Models\TestStandModels

<TestStand Public>\Components\Models\TestStandModels

<TestStand Public>\Components\Models\TestStandModels

<TestStand>\Components\Models\TestStandModels

<TestStand>\Components\Models\ModelPlugins

<TestStand Public>\Components\Models\ModelPlugins

Parent topic:

Process Model Architecture

Related concepts:

- Sequential Process Model
- Parallel Process Model
- Batch Process Model
- Copying Read-Only Files to Modify
- TestStand Directory Structure
- Search Directories

<!--NI_TOPIC bundle=teststand path=teststand-public-directory.html language=enus -->
## TOPIC 00908: TestStand Public Directory

- bundle_id: `teststand`
- source_path: `teststand-public-directory.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/teststand-public-directory.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following table lists the name and contents of each subdirectory of the <TestStand Public> directory, which contains modifications, customizations, and other files you can directly edit. Directory Name Contents AdapterSupport Support files for the LabVIEW and LabWindows/CVI Adapters. CodeTemplat

### TestStand Public Directory

The following table lists the name and contents of each subdirectory of the
 <TestStand Public> directory, which contains
 modifications, customizations, and other files you can directly edit.

| Directory Name | Contents |
| --- | --- |
| AdapterSupport | Support files for the LabVIEW and LabWindows/CVI Adapters. |
| CodeTemplates | Empty by default. You can store modified source code templates for step types, or code templates you create. |
| Components | Placeholder subdirectories for modified TestStand components and components you develop, including callback files, language files, process model files, run-time servers, type palette files, and TestStand Sequence Analyzer analysis modules for custom rules you create. TestStand installs the default sequences, executables, project files, and source files for components in the <TestStand>\\Components directory. |
| Examples | Example sequences and tests. Most example sequences that use VIs call subVIs in the <LabVIEW>\\vi.lib directory, which you can access after you install LabVIEW. |
| RuntimeServers | Contains example legacy source code for building a LabVIEW run-time application for executing LabVIEW-based code modules on a computer on which you have not installed the LabVIEW development system. Use the LabVIEW Adapter Configuration dialog box to configure the LabVIEW Adapter to use LabVIEW executables built with an ActiveX server enabled. |
| Setup | Support files for the TestStand installer. |
| Tutorial | Sequences and code modules you use in tutorials the Getting Started with TestStand manual and the NI TestStand Evaluation Guide. This directory also contains a Solution subdirectory that contains completed versions of the tutorial files. |
| UserInterfaces | Copies of the LabVIEW, LabWindows/CVI, Microsoft Visual Basic, C#, and C++ (MFC) user interfaces with source code installed in the <TestStand>\\UserInterfaces directory. |

Parent topic:

TestStand Directory Structure

Related concepts:

- Programming with the TestStand API in LabVIEW
- Programming with the TestStand API in LabWindows/CVI
- Step Types
- Components Directory
- Getting Started with TestStand
- TestStand Directory

<!--NI_TOPIC bundle=teststand path=teststand-sequence-analyzer-application.html language=enus -->
## TOPIC 00909: TestStand Sequence Analyzer Application

- bundle_id: `teststand`
- source_path: `teststand-sequence-analyzer-application.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/teststand-sequence-analyzer-application.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the TestStand Sequence Analyzer application to analyze projects outside of the TestStand Sequence Editor. You can launch the application in the following ways: (Windows 8.1) Click the NI Launcher tile on the Start screen and select TestStand»Tools»TestStand Sequence Analyzer. (Windows 10 or 7) S

### TestStand Sequence Analyzer Application

Use the TestStand Sequence Analyzer application to analyze projects outside of the TestStand Sequence Editor. You can launch the application in the following ways:

- (Windows 8.1) Click the NI Launcher tile on the Start screen and select TestStand»Tools»TestStand Sequence Analyzer .
- (Windows 10 or 7) Select Start»All Programs»National Instruments»TestStand»Tools»TestStand Sequence Analyzer .
- Run <TestStand>\Bin\AnalyzerApp.exe .

The sequence analyzer application window contains the following tabs:

- Files—The files and directories to analyze.
- Rules—The rules to use for analysis. Use this tab to enable, disable, and configure rules for analysis in the current project.
- Options—Contains the project options that control the analysis and determine whether the sequence editor automatically saves the current analyzer project.
- Messages—Contains the list of messages for the most recent analysis of the current project, sequence file, or workspace file. The sequence analyzer overwrites the content of the Messages tab each time you start an analysis session.
- Analysis Summary—Contains a summary of the most recent analysis of the project.

#### Command-Line Usage

Refer to the following table for more information about the commands you can perform in the sequence analyzer application. Commands are listed in order of execution.

| Order | Command | Behavior |
| --- | --- | --- |
| 1 | /minimize | Launches the interface in a minimized state. |
| 2 | /analyze | Analyzes the open project. |
| 3 | /report | Generates a report for the most recently performed analysis. If no analysis has been performed, a dummy report will be generated. If the /analyze command is present, the report will not be generated until the analysis completes. If you specify a file path after the /report command, the report will be placed in that location. If you specify a relative file path, the path will be assumed relative to the open analyzer project directory. If you do not specify a file path, the report will be placed in the analyzer project directory. |
| 4 | /save | Saves the open project. If the /report command is present, the project will not save until the report has been generated. |
| 5 | /clearMessagesOnSave | Deletes analysis messages from the open project on save. |
| 6 | /quit | Closes the interface and quits all associated processes. If the /analyze, /report, or /save commands are present, the application will not quit until these operations are complete. |
| — | /env <environment path> | Launches the application in the environment defined in the .tsenv file located at <environment path>. |
| — | /help | Prints information about command-line syntax usage to the command line. |

You can use the following command-line syntax to open an analyzer project:

AnalyzerApp.exe "C:\My Documents\MyProject.tsaproj"

Use the following command-line syntax to perform commands on an open analyzer project:

AnalyzerApp.exe "C:\My Documents\MyProject.tsaproj" /analyze /report /save /clearMessagesOnSave

#### Sequence Analyzer ExitCodes

The Sequence Analyzer application returns a negative value if there is a problem running the Sequence Analyzer, and returns a positive value if analysis reports one or more rule violations. The following are valid return codes, listed in descending order of precedence:

| Number | Result | Behavior |
| --- | --- | --- |
| -2 | Invalid Paths | An invalid path was passed. |
| -1 | Invalid Flags | An invalid flag was passed. |
| 1 | Analyzer Error | One or more errors were reported when analyzing the project. |
| 2 | Analyzer Warning | One or more warnings were reported when analyzing the project. |
| 0 | Success | No Errors or Warnings were reported. |

Note: If both warnings and errors are reported during the analysis of a project, the return value indicates an error.

Note

Parent topic:

TestStand Sequence Analyzer

Related concepts:

- Search Directories
- Custom Analyzer Rules

Related information:

- TestStand Sequence Analyzer Environment Reference

<!--NI_TOPIC bundle=teststand path=teststand-sequence-analyzer.html language=enus -->
## TOPIC 00910: TestStand Sequence Analyzer

- bundle_id: `teststand`
- source_path: `teststand-sequence-analyzer.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/teststand-sequence-analyzer.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the TestStand Sequence Analyzer in the TestStand Sequence Editor or the stand-alone sequence analyzer application to complete the following tasks for workspace files, sequence files, directories, type palette files, station globals files, template files, and users files during development or bef

### TestStand Sequence Analyzer

Use the TestStand Sequence Analyzer in the TestStand Sequence Editor or the
 stand-alone sequence analyzer application to complete the following tasks for workspace
 files, sequence files, directories, type palette files, station globals files, template
 files, and users files during development or before deployment:

- Find errors
- Enforce custom development guidelines you establish
- Gather statistics

The sequence analyzer uses a built-in set of rules and analysis modules to analyze the files you specify and generate messages that correspond to each issue found during analysis. The built-in rules are designed to detect, at edit time, the most common situations that can cause run-time failures.

Use the Analysis Results pane in the sequence editor or the Messages tab in the sequence analyzer application to view and resolve the messages for the most recent analysis of the current analyzer project, sequence file, or workspace file.

You can create custom rules and analysis modules for the sequence analyzer to use. Refer to the files located in the <TestStand Public>\Examples\TestStand Debugging Features\Custom Analyzer Rules directory for examples of custom rules and analysis modules. You can also distribute custom rules and related supporting files to use in analysis projects or to analyze files on other computers on which TestStand is installed.

In the TestStand Sequence Editor, click the Current Sequence Analyzer Project button on the Sequence Analyzer toolbar or select Debug»Sequence Analyzer»Current Sequence Analyzer Project to open the Current Sequence Analyzer Project window and the most recently opened analyzer project file.

Parent topic:

TestStand Tools and Utilities

Related concepts:

- Search Directories
- Creating Analysis Modules for Custom Rules
- TestStand Sequence Analyzer Rules Descriptions
- Custom Analyzer Rules

Related tasks:

- Creating Custom Rules in the TestStand Sequence Analyzer

Related information:

- Current Sequence Analyzer Project Window
- TestStand Sequence Analyzer Environment Reference
- TestStand Sequence Analyzer API Reference

<!--NI_TOPIC bundle=teststand path=teststand-sequence-editor.html language=enus -->
## TOPIC 00911: TestStand Sequence Editor

- bundle_id: `teststand`
- source_path: `teststand-sequence-editor.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/teststand-sequence-editor.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The TestStand Sequence Editor is a development environment in which you create, edit, execute, and debug sequences and the tests sequences call. Use the sequence editor to access all TestStand features, such as step types and process models. The sequence editor also includes the following debugging

### TestStand Sequence Editor

The TestStand Sequence Editor is a development environment in which you create,
 edit, execute, and debug sequences and the tests sequences call. Use the sequence editor
 to access all TestStand features, such as step types and process models. The sequence
 editor also includes the following debugging tools:

- Setting breakpoints
- Stepping into, out of, or over steps
- Tracing through program executions
- Displaying variables
- Monitoring variables,
 expressions,
 and output messages during executions
- Performing static analysis of sequence files to locate errors and enforce coding
 guidelines

In the sequence editor, you can start multiple concurrent executions, execute multiple
 instances of the same sequence, or execute different sequences at the same time. Each
 execution instance opens an Execution window. In Trace Mode, the Execution window shows
 the steps in the currently executing sequence. If the execution suspends, the Execution
 window shows the next step to execute and provides debugging options.

The sequence editor contains the following advanced editing features:

- Panes you can dock, float, or hide
- Multiple step editing
- Workspace pane to manage sequence files and test source code
- Source code integration
- Type editing
- Undo and redo edits (except for types)
- Graphical sequence call hierarchy display
- Forward and backward navigation among sequences
- Find and replace
- Integrated sequence file differ
- User
 management

You can customize the layout of panes and tabs to optimize development and debugging
 tasks. You can also interactively customize the menus, toolbars, and keyboard shortcuts.

Additionally, you can save custom layouts and reset the layout to the default. TestStand
 does not automatically save the sequence editor layout from a previous session. Click
 the Save Current button on the UI Configuration tab of the
 Sequence Editor Options dialog box to save the sequence editor layout with a name you
 specify.

Parent topic:

TestStand Tools and Utilities

Related concepts:

- Executing a Sequence Directly
- Debugging Executions
- Step Types
- Process Models
- Expressions
- Adding Users and Setting Privileges

<!--NI_TOPIC bundle=teststand path=teststand-tools.html language=enus -->
## TOPIC 00912: TestStand Tools and Utilities

- bundle_id: `teststand`
- source_path: `teststand-tools.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/teststand-tools.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `reference`
- source_description: Refer to the topics in this section for information on TestStand tools and utilities provided by NI, and their usage in TestStand projects.

### TestStand Tools and Utilities

Refer to the topics in this section for information on TestStand tools and utilities
 provided by NI, and their usage in TestStand projects.

- [TestStand Sequence Editor](teststand-sequence-editor.html) The TestStand Sequence Editor is a development environment in which you create, edit, execute, and debug sequences and the tests sequences call. Use the sequence editor to access all TestStand features, such as step types and process models. The sequence editor also includes the following debugging tools:
- [TestStand Deployment Utility](teststand-deployment-utility.html) Use the deployment utility to create a deployable image or a patch deployment of a TestStand system and an optional installer.
- [TestStand File Diff and Merge Utility](teststand-file-diff-and-merge-utility.html) Use the TestStand File Diff and Merge utility to compare and merge non-type differences among two or three sequence files and compare type differences among two sequence files or type palette files.
- [TestStand Offline Results Processing Utility](teststand-offline-results-processing-utility.html) Use this utility to process raw results files into reports and database tables at a time other than when sequence execution occurs, such as overnight, or on a different computer.
- [XML Packaging Utility](xml-packaging-utility.html) Use the XML Packaging Utility to copy local XML and HTML report files you select, including related style sheets, image files, and referenced files, to a destination directory you specify so you can view the XML report on a computer that does not have TestStand installed.
- [TestStand Sequence Analyzer](teststand-sequence-analyzer.html) Use the TestStand Sequence Analyzer in the TestStand Sequence Editor or the stand-alone sequence analyzer application to complete the following tasks for workspace files, sequence files, directories, type palette files, station globals files, template files, and users files during development or before deployment:
- [Execution Profiler](execution-profiler.html) Select the button to launch the Execution Profiler window to view and record duration of steps, code modules, and other resources a multithreaded TestStand system uses over a period of time.
- [Database Viewer Application](database-viewer-application.html) TestStand includes the Database Viewer application for viewing data in a database, editing table information, and executing SQL commands.
- [Instrument Drivers](instrument-drivers.html) Visit the Instrument Driver Network at ni.com/idnet for more information about instrument drivers and for finding and downloading instrument drivers compatible with National Instruments software.
- [Sequence File Converter](sequence-file-converter.html) Use the Sequence File Converter tool to resave sequence files on disk using the current version of TestStand. You can also change the file format to binary, XML, or INI, and you can change the protection setting for the files.
- [TestStand Version Selector](teststand-version-selector.html) The TestStand Version Selector application indicates the active version of TestStand, can activate a different version of TestStand, and can reconfigure the currently active version.
- [Session Manager](session-manager.html) Use Session Manager to obtain instrument sessions.
- [TestStand Migration Utility](teststand-migration-utility.html) Use the TestStand Migration Utility to copy settings, configuration, and public component files from the folders of previous versions of TestStand to the current version of TestStand.
- [NI Nigel AI](nigel-ai.html) NI Nigel AI is an AI which brings a wealth of knowledge about TestStand into your design process. Nigel can offer development advice and test system design information to help you create projects and sequences. Nigel is powered by Microsoft Azure OpenAI.

<!--NI_TOPIC bundle=teststand path=teststand-ui-controls.html language=enus -->
## TOPIC 00913: TestStand UI Controls

- bundle_id: `teststand`
- source_path: `teststand-ui-controls.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/teststand-ui-controls.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: All user interface examples use the TestStand User Interface (UI) Controls, which are a set of ActiveX controls that implement the common functionality for applications to display, execute, edit, save, and debug test sequences. These ActiveX controls greatly reduce the amount of source code a user i

### TestStand UI Controls

All user interface examples use the TestStand User Interface (UI) Controls, which are a set of ActiveX controls that implement the common functionality for applications to display, execute, edit, save, and debug test sequences. These ActiveX controls greatly reduce the amount of source code a user interface application requires.

Note

User interfaces that use the TestStand UI Controls typically perform the following basic operations:

- Configure connections, commands, and other control settings
- Register to handle events the controls generate
- Start TestStand
- Wait in a main event loop until you close the application
- Shut down TestStand

User interfaces can also include a menu bar that contains non-TestStand items and items that invoke TestStand commands.

You can call the TestStand API on objects you create or obtain from the TestStand UI Controls properties, methods, or events. Consider the following guidelines when you call the TestStand API in a user interface that uses the TestStand UI Controls:

- You do not need to create the TestStand Engine. Use the ApplicationMgr.GetEngine method to obtain the Engine object.
- When you call the Engine.NewExecution method to create an execution, the TestStand UI Controls recognize the new execution.
- When you call the Engine.GetSequenceFileEx method to load a sequence file, the TestStand UI Controls do not display the file you load. You must call the ApplicationMgr.OpenSequenceFile method to open and display a file in the user interface.
- You can obtain sequence file and execution references from events or from the SequenceFiles and Executions collections.
- When you hold references to TestStand objects, release them in the handler for the ApplicationMgr.QueryShutdown event when the event handler does not cancel the shut down process.
- The TestStand UI Controls display only the active thread and do not support enabling the ExecMask_TraceAllThreads ExecutionMask constant.
- Do not couple user interfaces to specific sequences.
- Do not use instrumentation code in user interfaces.
- Use UI Messages to communicate information between code modules and user interfaces.

Parent topic:

Creating Custom User Interfaces

Related concepts:

- Getting Started with User Interface Development
- Executions
- Setting the Preferred Execution System of LabVIEW VIs to Prevent Deadlock
- Writing an Application with the TestStand Engine API

<!--NI_TOPIC bundle=teststand path=teststand-utility-functions-library.html language=enus -->
## TOPIC 00914: TestStand Utility Functions Library

- bundle_id: `teststand`
- source_path: `teststand-utility-functions-library.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/teststand-utility-functions-library.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the TestStand Utility (TSUtil) Functions Library to use certain aspects of the TestStand API in particular application development environments (ADEs). Many TestStand Utility (TSUtil) functions operate on environment-specific objects, such as menus, that the environment-neutral TestStand API can

### TestStand Utility Functions Library

Use the TestStand Utility (TSUtil) Functions Library to use certain aspects of the TestStand API in particular application development environments (ADEs). Many TestStand Utility (TSUtil) functions operate on environment-specific objects, such as menus, that the environment-neutral TestStand API cannot access. The functions available in TSUtil vary according to the ADE.

The TSUtil library contains functions to insert menu options that automatically execute commands the TestStand User Interface (UI) Controls API provides. The TSUtil library also provides functions to help localize the strings on a user interface.

The following table describes how to use the TSUtil library in different ADEs. If the table does not include the ADE you use, a version of TSUtil does not exist for the ADE.

| ADE | Help Location | Files | How to Use |
| --- | --- | --- | --- |
| LabVIEW | Context help for each VI and in the NI TestStand VIs and Functions Help, accessible by right-clicking the VI and selecting Help from the shortcut menu or by selecting Help»NI TestStand VIs and Functions | VIs on the Functions»TestStand palette_TSUtility.llb located in <TestStand>\\API\\LabVIEW | Place VIs on the block diagram. |
| LabWindows/CVI | Function panels (TSUtil.fp) | TSUtil.c, TSUtil.h, TSUtil.fp, and TSUtil.obj located in <TestStand>\\API\\CVI | Insert TSUtil.fp into the LabWindows/CVI project. Include TSUtil.h in the source files as needed. The names of TestStand-related functions begin with a TS_ prefix. |
| .NET | In the Object Browser and in the source window using Microsoft IntelliSense | National Instruments.TestStand.Utility.dll located in <TestStand>\\API\\DotNet\\Assemblies\\CurrentVersion | Add a reference to the assembly to the project. The classes in this assembly reside in the National Instruments.TestStand.Utility namespace. |
| C++ (MFC) | Comments in the C++ header file, TSUtilCPP.h | TSUtilCPP.cpp and TSUtilCPP.h located in <TestStand>\\API\\VC | Add TSUtilCPP.cpp to the project once. Include TSUtilCPP.h in the source files as needed. The classes in this library reside in the TSUtil namespace. |

You can use the source code for one of the existing TSUtil libraries as a guide to write your own code that performs similar functionality.

Parent topic:

Advanced User Interface Development

Related concepts:

- TestStand ActiveX API Overview
- Managing Menus and Menu Items
- TestStand UI Controls
- Localizing User Interfaces
- TestStand Directory Structure
- Adding Assembly References in Microsoft Visual Studio
- Using TestStand UI Controls in LabVIEW
- Using TestStand UI Controls in LabWindows/CVI

<!--NI_TOPIC bundle=teststand path=teststand-version-selector.html language=enus -->
## TOPIC 00915: TestStand Version Selector

- bundle_id: `teststand`
- source_path: `teststand-version-selector.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/teststand-version-selector.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The TestStand Version Selector application indicates the active version of TestStand, can activate a different version of TestStand, and can reconfigure the currently active version. Although you can install more than one version of TestStand on a computer, only one version of TestStand can be activ

### TestStand Version Selector

The TestStand Version Selector application indicates the active version of
 TestStand, can activate a different version of TestStand, and can reconfigure the
 currently active version.

Although you can install more than one version of TestStand on a computer, only one version of
 TestStand can be active and can run at a time. You can launch the application in the
 following ways:

- (Windows 10) Click Start»National Instruments»TestStand Version Selector .
- Run C:\<Program Files>\National Instruments\Shared\TestStand Version Selector\TSVerSelect.exe .

- Registers the ActiveX interfaces for the TestStand API.
- Registers the ActiveX interfaces for the TestStand User Interface (UI)
 Controls.
- Registers the TestStand API and UI Controls interop assemblies for Microsoft
 Visual Studio.
- Registers various ActiveX controls, DLLs, and applications located in the
 <TestStand>\Components directories.
- Adds the TestStand VIs and Functions Palette and the TestStand Controls Palette
 to installed versions of LabVIEW.

The TestStand Version Selector also initiates the following actions for specific versions
 of TestStand:

| Version Activated | Actions |
| --- | --- |
| TestStand 2021 SP1 or later | Installs NI TestStand Support for Debugging Python Code, which is an extension for Visual Studio Code. This action occurs only when VS Code is already installed on the computer. When you select TestStand 2021 SP1 or later under Installed TestStand versions, and then click either Activate or Configure, the TestStand Version Selector installs the VS Code extension. If you want to perform step into debugging of Python modules, you must complete this step to install the VS Code extension. |
| TestStand 4.1 or later | Copies API files to <National Instruments>\\Shared\\CVI\\instr\\TestStand\\API for LabWindows/CVI 8.5 or later, or to <CVI>\\instr\\TestStand\\API for LabWindows/CVI 8.1.1 or earlier. Adds environment variables for the <TestStand>, <TestStand>\\Bin, <TestStand Public>, and <TestStand Application Data> directories. You can use the environment variables in development environments to specify paths to files in these TestStand directories. For example, you can use these environment variables to build paths in the Additional Include Directories control in Visual Studio.Note The environment variables for 64-bit TestStand end with a 64 suffix. For example, 32-bit TestStand uses the variables TestStand, TestStandBin, TestStandPublic, and TestStandAppData, and 64-bit TestStand uses the variables TestStand64, TestStandBin64, TestStandPublic64, and TestStandAppData64. In TestStand 4.1 and later, the Current Active Version control shows the currently active version of TestStand. Select a version in the Installed TestStand versions control and click the Activate button to activate a specific version of TestStand. The Path to 32-bit version and Path to 64-bit version controls show the location of the selected version of TestStand. When activation is complete, the TestStand Version Selector indicates success or displays any warnings. Click the Launch 32-bit or Launch 64-bit button to run the sequence editor application for the active version of TestStand. Note The TestStand Version Selector does not normally require administrator privileges to activate a specific version of TestStand on Microsoft Windows 10. To require administrator privileges for using the TestStand Version Selector, add the /reqadmin command-line option to the selector shortcut. |
| TestStand 4.0.1 or earlier | Adds the <TestStand>\\API\\CVI\\ directory to the LabWindows/CVI development environment search directories for include files and instrument drivers. You must exit LabWindows/CVI before activating a new version of TestStand to ensure the changes take effect. |

#### Command-Line Options

The TestStand Version Selector supports the following command-line options:

| Argument | Description |
| --- | --- |
| /? | Displays help for command-line options. |
| /version <versionname> | Activates specified version, where <versionname> is the version of TestStand to activate. |
| /launch <filename> | Launches the executable you specify, where <filename> is the path to the executable to launch. |
| /noprompt | Suppresses prompts while performing activation and launch operations. |
| /reqadmin | Forces the Version Selector to require Administrator access when performing activation. |
| /installing | Displays a status prompt while activating a specified version without displaying errors. You must use this option with the /version and /noprompt options. |
| /donotreactivate | Do not reactivate TestStand if the version of TestStand is already active. |

#### Log File

The TestStand Version Selector creates log files, located at <CommonAppData>\National Instruments\TestStand Version Selector, when you run the version selector to activate a version of TestStand and when you run an application that uses the TestStand Engine because the engine uses the version selector to update external environments. The log files contain details about the changes the version selector made, which might be useful when debugging issues related to changing the active version of TestStand.

Parent topic:

TestStand Tools and Utilities

Related concepts:

- Search Directories
- Activating 32-bit TestStand and 64-bit TestStand

Related information:

- TestStand Version Selector Environment Reference

<!--NI_TOPIC bundle=teststand path=teststand.html language=enus -->
## TOPIC 00916: TestStand

- bundle_id: `teststand`
- source_path: `teststand.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/teststand.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: You implicitly use instrument sessions in TestStand when you use IVI step types. IVI step types can share sessions with code modules written in any language that supports ActiveX. You can also use the ActiveX/COM Adapter to access the complete functionality of the Session Manager server from ActiveX

### TestStand

You implicitly use instrument sessions in TestStand when you use IVI step types. IVI step types can share sessions with code modules written in any language that supports ActiveX.

You can also use the ActiveX/COM Adapter to access the complete functionality of the Session Manager server from ActiveX steps in a sequence. Complete the following steps to call Session Manager from an ActiveX step.

1. Right-click the step and select Specify Module from the context menu.
2. Select NI Session Manager from the Automation Server ring control.

Note

plug&play

Parent topic:

Using Instrument Sessions in a Development Environment

<!--NI_TOPIC bundle=teststand path=thread-concurrency-models.html language=enus -->
## TOPIC 00917: Thread Concurrency Models

- bundle_id: `teststand`
- source_path: `thread-concurrency-models.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/thread-concurrency-models.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: In ActiveX, you can initialize a thread to use the single threaded apartment (STA) concurrency model or the multithreaded apartment (MTA) concurrency model. Before you use a thread with ActiveX, you must initialize the thread to one of these models. Typically, the software development environment yo

### Thread Concurrency Models

In ActiveX, you can initialize a thread to use the single threaded apartment (STA) concurrency model or the multithreaded apartment (MTA) concurrency model. Before you use a thread with ActiveX, you must initialize the thread to one of these models. Typically, the software development environment you are using initializes the threads in the application for you.

When using the TestStand API to implement a user interface or other application program, you can use threads of either concurrency model.

When using ActiveX automation from within a code module, you do not have to initialize the thread concurrency model because the initial thread in an execution is initialized as multithreaded and TestStand initializes new threads in an execution depending on the option you select in the Sequence Call Advanced Settings window.

When using ActiveX controls on a window or dialog box a code module creates, you must ensure that the thread is initialized as STA. If TestStand preloads a code module when an execution starts, the root execution, which is initialized as MTA, typically loads the code module. When a code module is loaded dynamically, the thread that first executes the step loads the code module.

You must complete the following steps to ensure that a code module is loaded by an STA thread.

- Execute the step in an STA thread. Use a Sequence Call step to create a STA thread by enabling the Use Single-Threaded Apartment option for the step in the Thread Settings dialog box.
- Select Load Dynamically for the Load Option option in the Step Properties dialog box.

For LabVIEW VIs that contain ActiveX controls, set the Preferred Execution System option for the VI to user interface to ensure that the VI executes within the user interface thread, which is typically an STA thread.

Note

same as caller

Preferred Execution System

same as caller

Parent topic:

TestStand API Concepts

Related concepts:

- Launching an MFC Dialog with ActiveX Controls

<!--NI_TOPIC bundle=teststand path=thread-safety-of-the-propertyobject-api-and-t.html language=enus -->
## TOPIC 00918: Thread Safety of the PropertyObject API and TestStand Variables

- bundle_id: `teststand`
- source_path: `thread-safety-of-the-propertyobject-api-and-t.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/thread-safety-of-the-propertyobject-api-and-t.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can modify and access the structure, values, and other settings of TestStand variables concurrently from multiple threads without causing crashes, various errors, or data inconsistencies. Use the PropertyObject.GetSubProperties and PropertyObject.GetPropertyObjectElements methods to obtain refer

### Thread Safety of the PropertyObject API and TestStand Variables

You can modify and access the structure, values, and other settings of TestStand variables concurrently from multiple threads without causing crashes, various errors, or data inconsistencies. Use the PropertyObject.GetSubProperties and PropertyObject.GetPropertyObjectElements methods to obtain references to all subproperties or elements of a property in one atomic call to avoid issues with invalid indexes that result when another thread removes or inserts properties or elements while a different thread iterates through the subproperties or elements. Use synchronization primitives, such as locks or semaphores, if you need to maintain atomicity or control editing and data access across multiple edits or PropertyObject API calls.

#### Actions That Are Thread-Safe in TestStand

The following actions are thread-safe in TestStand:

- Using the PropertyObject API or TestStand expressions to access or modify variables from one thread while modifying the structure of such variables in another thread. You can access or modify the parent, the name, and other items that are accessible through the PropertyObject API.
- Serializing variables by using the Engine.SerializeObjects method with the SerializationOption_UseBinary or SerializationOption_UseXml options or by saving a PropertyObjectFile in the XML or Binary format while modifying the structure of such variables in another thread. TestStand maintains the serialized data in a consistent state. However, the timing of the serialization code in regard to the concurrent modifications determines what TestStand actually serializes.

#### Actions That Are Not Thread-Safe in TestStand

The following actions are not thread-safe in TestStand:

- Modifying a type definition in one thread while other threads access the same type definition or its instances.
- Serializing variables using an INI-based format while modifying the structure of such variables in another thread.
- Accessing API properties and methods of a SequenceContext object from a thread other than the thread the object belongs to while the thread the SequenceContext object belongs to runs the TestStand sequence to which the SequenceContext object applies.
- Modifying the structure of built-in properties for steps, sequences, and SequenceContext objects while another thread accesses those objects.

Parent topic:

Writing an Application with the TestStand Engine API

<!--NI_TOPIC bundle=teststand path=thread-usage-per-item-graph.html language=enus -->
## TOPIC 00919: Thread Usage per Item Graph

- bundle_id: `teststand`
- source_path: `thread-usage-per-item-graph.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/thread-usage-per-item-graph.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Thread Usage per Item Graph Use this graph to view the threads that use an item over time. You can view how long threads block waiting to acquire an item and how long they retain or use the item. Along the vertical axis, each row in the graph represents an item. The item name displays in a legend to

### Thread Usage per Item Graph

#### Thread Usage per Item Graph

Use this graph to view the threads that use an item over time. You can view how long threads block waiting to acquire an item and how long they retain or use the item.

Along the vertical axis, each row in the graph represents an item. The item name displays in a legend to the left of the graph time line. After the item name, each row displays rectangles that represent the operations on that item.

The horizontal axis represents time. Operations are positioned along the horizontal axis according to the times at which the operations begin and end. Each operation has a label that indicates the name of the thread that performs the operation. Hovering over an operation displays a tool tip with additional information.

Parent topic:

Profiler Window Graphs

<!--NI_TOPIC bundle=teststand path=top-level-properties.html language=enus -->
## TOPIC 00920: Top-Level Properties

- bundle_id: `teststand`
- source_path: `top-level-properties.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/top-level-properties.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Sequence Context Subproperty Description Locals Contains local variables in the current sequence. Only the current sequence can access these variables. Parameters Contains parameter variables in the current sequence. Only the current sequence or calling sequences can access these variables. FileGlob

### Top-Level Properties

| Sequence Context Subproperty | Description |
| --- | --- |
| Locals | Contains local variables in the current sequence. Only the current sequence can access these variables. |
| Parameters | Contains parameter variables in the current sequence. Only the current sequence or calling sequences can access these variables. |
| FileGlobals | Contains file global variables in the current sequence file. All the sequences in the current sequence file can access these variables. |
| StationGlobals | Contains station global variables on the computer. Any sequence on the current computer can access these variables. Station global variables are stored on disk and the values persist even after you close TestStand. Refer to StationGlobals TS Subproperty for more information about the StationGlobals property. |
| ThisContext | Contains a reference to the current sequence context. You typically use this property to pass the entire sequence context as an argument to a subsequence or a step code module. |
| RunState | Contains properties that describe the current state of execution. Refer to RunState Subproperties for more information about the RunState property. |
| Step | Contains the properties in the currently executing step. The Step property exists only while a step executes. The property does not exist when the execution is between steps, such as at a breakpoint. |

The following properties in the sequence context refer to objects that exist before, and persist after, the current execution:

- StationGlobals
- RunState.InitialSelection
- RunState.SequenceFile
- RunState.ProcessModelClient

Any modifications you make to these objects affect all executions in the current TestStand session. When you save the modifications to disk, they affect future TestStand sessions.

Note

Parent topic:

Sequence Context

Related concepts:

- Station Globals TS Subproperty
- RunState Subproperties

<!--NI_TOPIC bundle=teststand path=tracing-with-the-dett.html language=enus -->
## TOPIC 00921: Tracing with the DETT

- bundle_id: `teststand`
- source_path: `tracing-with-the-dett.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/tracing-with-the-dett.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The LabVIEW Desktop Execution Trace Toolkit (DETT) is a tool that collects various types of trace data from LabVIEW applications. Refer to the LabVIEW Desktop Execution Trace Toolkit Help and the Opening a Trace Connection topic in the LabVIEW Help for more information about using the DETT. Tracing

### Tracing with the DETT

The LabVIEW Desktop Execution Trace Toolkit (DETT) is a tool that collects various types of trace data from LabVIEW applications. Refer to the LabVIEW Desktop Execution Trace Toolkit Help and the Opening a Trace Connection topic in the LabVIEW Help for more information about using the DETT.

Note

#### Configuring the DETT

When you enable debugging and tracing in TestStand, TestStand configures each LabVIEW Runtime loaded by TestStand to open a unique TCP port. Refer to the TCP Ports for the LabVIEW Runtimes topic for more information about TCP ports used.

Complete the following steps to trace and capture events for VIs executed using the LabVIEW Runtime in a TestStand application:

1. Ensure that the Enable Debugging and Tracing option in the LabVIEW Adapter Configuration dialog box is enabled and restart the TestStand Sequence Editor or User Interface if required.
2. Execute your test sequence to ensure all LabVIEW Runtimes and VI code modules are loaded. Note The DETT can only connect to the TestStand Sequence Editor or a User Interface after TestStand loads a supported LabVIEW Runtime. Determine the appropriate port for the runtime you want to trace. Refer to the TCP Ports for the LabVIEW Runtimes topic for more information.
3. In the DETT:
  1. Set the Machine text box in the toolbar to localhost , then set the Port text box to the port number for the LabVIEW Runtime you want to trace.
  2. Refresh the Application Instance drop-down menu to see the context for the TestStand application.
  3. Click the Start button in the DETT to begin a trace session.

Note

- You can only trace one LabVIEW execution/project context at a time.
- The DETT can connect and generate trace and event information for the TestStand Sequence Editor and User Interfaces. The DETT cannot connect to a TestStand application until TestStand loads a supported LabVIEW Runtime.

#### Tracing VIs executing in different LabVIEW projects

If you have a sequence file that executes VIs in one or more project contexts, you must connect to the specific project context you want to trace from the Application Instance drop-down menu.

Parent topic:

Debugging and Tracing of VIs Executed Using the LabVIEW Runtime

Related concepts:

- TCP Ports for the LabVIEW Runtimes

<!--NI_TOPIC bundle=teststand path=transferring-files.html language=enus -->
## TOPIC 00922: Transferring Files

- bundle_id: `teststand`
- source_path: `transferring-files.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/transferring-files.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can transfer files from a development computer to a test station computer by using distribution media, by copying files from a local network, or by using email or FTP, depending on the location of the test station computers and available resources. Consider the following factors when you select

### Transferring Files

[IMAGE alt='image' src='GUID-F326C9C3-FC82-41D6-A23F-8DCC889A1CA3-a5.svg']

You can
 transfer files from a development computer to a test station computer by using
 distribution media, by copying files from a local network, or by using
 email or FTP, depending on the location of the test station computers and available
 resources.

Consider the following factors when you select a transfer
 method:

- Capacity —Determine how large a file you need to transfer.
 For example, a standard CD holds approximately 650 MB, a single-layer DVD holds
 approximately 4700 MB, and a single-layer Blu-Ray holds approximately 25 GB. You
 can use the TestStand Deployment Utility to build an installer that
 spans multiple discs, but this technique requires an operator to
 manually change the discs during the installation process. Internet connections
 might not have strict limits, but you might incur additional charges to transfer
 large amounts of data through email or FTP.
- Speed —Determine the time required to transfer files.
 Consider the total time required to physically move the distribution media to
 the test station computer and read the information from the media to transfer
 the entire test system, which can directly affect manufacturing downtime.

Parent topic:

Deployment Process Overview

Related concepts:

- Network-Based Deployment Mechanisms
- Building a Customized MSI-based Installer

<!--NI_TOPIC bundle=teststand path=transforming-xml-content-to-html-output.html language=enus -->
## TOPIC 00923: Transforming XML Content to HTML Output

- bundle_id: `teststand`
- source_path: `transforming-xml-content-to-html-output.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/transforming-xml-content-to-html-output.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following example XML file associates a style sheet, samplexStylesheet.xsl: <?xml version="1.0" encoding="iso-8859-1" ?> <?xml-stylesheet type="text/xsl" href="C:\samplexStylesheet.xsl "?> <source> <title>XSL tutorial</title> <author>John Smith</author> </source> The following example XSLT code

### Transforming XML Content to HTML Output

The following example XML file associates a style sheet, samplexStylesheet.xsl:

```text
<?xml version="1.0" encoding="iso-8859-1" ?>
<?xml-stylesheet type="text/xsl" href="C:\samplexStylesheet.xsl "?>
<source>
    <title>XSL tutorial</title>
    <author>John Smith</author>
</source>
```

The following example XSLT code transforms XML to HTML. The style sheet uses XPath expressions to add the title and author from the XML file to the generated HTML output. The style sheet also contains required HTML formatting, such as table and border formats, to add to the generated HTML output.

```text
<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version = '1.0' xmlns:xsl='http://www.w3.org/1999/XSL/Transform'>
    <xsl:output method="html"/>
    <xsl:template match="/">
        <head>
            <title>Generated HTML Output</title>
        </head>
        <body>
            <table border="1"> 
                <tr> 
                    <td>Title</td> 
                    <td>Author</td> 
                </tr> 
                <tr> 
                    <td><xsl:value-of select="//title"/></td> 
                    <td><xsl:value-of select="//author"/></td> 
                </tr> 
               </table> 
            </body> 
        </xsl:template> 
<xsl:stylesheet>
```

The previous example XSLT code generates the following HTML:

```text
<head> 
    <title>Generated HTML Output</title> 
</head> 
<body> 
    <table border="1"> 
        <tr> 
            <td><b>Title</b></td> 
            <td><b>Author</b></td> 
        </tr> 
        <tr> 
            <td>XSL Tutorial</td> 
            <td>John Smith</td> 
        </tr> 
    </table> 
</body>
```

The previous HTML code appears as follows when viewed in a browser:

[IMAGE alt='image' src='GUID-875EDB09-E1BB-41A0-9006-A1EBFEAEB66E-a5.png']

Parent topic:

Transforming XML Reports

Related concepts:

- XML Report Style Sheets

<!--NI_TOPIC bundle=teststand path=transforming-xml-reports.html language=enus -->
## TOPIC 00924: Transforming XML Reports

- bundle_id: `teststand`
- source_path: `transforming-xml-reports.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/transforming-xml-reports.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Extensible Stylesheet Language Transformations (XSLT) is an XML-based language that transforms XML documents into other formats, such as a different XML structure, HTML, and text. Use XSLT to separate the formatting of XML data from the actual XML data itself. XSLT does not usually modify the existi

### Transforming XML Reports

Extensible Stylesheet Language Transformations (XSLT) is an XML-based language that transforms XML documents into other formats, such as a different XML structure, HTML, and text. Use XSLT to separate the formatting of XML data from the actual XML data itself. XSLT does not usually modify the existing XML file. Instead, XSLT generates a new output file based on the existing XML file. Therefore, you can apply multiple XSLT transforms to create multiple views for the same XML data. Refer to the World Wide Web Consortium (W3C) web page located at www.w3.org/TR/xslt for more information about XSLT.

XSLT also usually uses JavaScript, VBScript, XPath, and XQuery technologies along with XSL to transform XML documents. Refer to the W3C website, located at www.w3.org, for more information about these technologies.

Parent topic:

XML Reports

<!--NI_TOPIC bundle=teststand path=troubleshooting-labview-code-module-issues.html language=enus -->
## TOPIC 00925: Troubleshooting LabVIEW Code Module Issues

- bundle_id: `teststand`
- source_path: `troubleshooting-labview-code-module-issues.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/troubleshooting-labview-code-module-issues.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Ensure that you prepared the source components as suggested because you can eliminate many issues by following the recommended guidelines and best practices. Use the following suggestions to troubleshoot issues with , , and . Mass Compile Log When you mass compile VIs, enable the Log Results option

### Troubleshooting LabVIEW Code Module Issues

Ensure that you prepared the source components as suggested because you can eliminate many issues by following the recommended guidelines and best practices. Use the following suggestions to troubleshoot issues with , , and .

#### Mass Compile Log

When you mass compile VIs, enable the Log Results option in the Mass Compile dialog box in LabVIEW and specify a destination for the log file. Review the mass compile log for broken VIs or read-only VIs.

Open broken VIs in LabVIEW and click the broken Run button to launch the Error list window, which includes details about the error. If no errors exist in the Error list, press the <Ctrl> key and click the Run button to force LabVIEW to recompile the VI, which updates the error list.

Resolve the reported errors before you include the VI in a deployment and ensure that the deployment also includes other files or drivers the VI requires.

#### Including Dynamically Called VIs

You must explicitly add VIs that code modules call dynamically, such as by using VI Server, to the TestStand workspace or to the directory from which you create the deployment. Additionally, you must manually add to the deployment any VIs or project libraries custom step types or other sequence elements require.

Even if a deployment builds without errors, validation tests on the test station computer can return Error 7 with the similar text "Open VI Reference in <VI Name> VI Path: <Path to VI>" to indicate missing VIs called dynamically. Confirm that you included the dynamically called VIs in the deployment with the correct destination and verify the path of the dynamically called VIs for each dynamic call. Typically, you place dynamically called VIs in the same directory as the calling VIs.

#### Redeploying Previously-Deployed
 VIs

NI does not recommend deploying VIs that were previously deployed
 using the TestStand Deployment Utility. When the deployment utility packages VIs,
 the deployment utility includes all subVIs and creates partial project libraries
 that contain only the required VIs from the project libraries. If possible, use the
 original source files to create the new deployment.

When you attempt to
 redeploy VIs, the build in the deployment utility might fail with the LabVIEW error
 "This VI claims to be part of a library, but that library does not claim to own this
 VI". This error typically occurs due to conflicts between vi.lib VIs, which are
 included by the LabVIEW development system, and the copies of these VIs, which are
 included in the support VIs folder or LLB in the deployment. The deployment utility
 includes these copies so that the deployed files will successfully run on a machine
 without the LabVIEW development system installed. For more details about this error,
 refer to the "Encountering Broken VIs With Partial Project Libraries" section of the
 Partial Project Libraries topic. This issue can also occur when you deploy custom
 LabVIEW-based step types to a development system and then attempt to include the
 step types in a new deployment.

To work around this issue, you must remove the
 duplicate VIs and partial project libraries from the test system and relink any
 callers of the duplicate VIs before you create a new deployment.

Complete the
 following steps to remove duplicate VIs and relink their callers:

1. Create the deployment and review the VIs the deployment utility reports as
 duplicates in the status log.
2. Remove any duplicate VIs and partial project libraries the deployment utility
 reports from the SupportVIs LLB or directory. Do not remove VIs from the vi.lib
 folder of the LabVIEW development system.
3. Load all top-level VIs included in the previously deployed files in the LabVIEW
 development system and re-save the VIs. LabVIEW prompts you to browse for any missing
 subVIs and relinks the VIs to the selected subVI path. In the Sequence Editor, select
 Tools»Update VI Calls to run the Update VI Calls tool to ensure
 that the LabVIEW steps use a valid path for the VI code module, since some steps may point
 to removed duplicate VIs.
4. Rebuild the deployment and verify that no library errors occur. If the errors
 persist, contact NI for support.

To prevent this issue in new deployments, consider enabling the
 Output VIs to a packed project library option to generate
 packed project libraries that contain the VIs the test system requires. All files in
 a packed project library, including project libraries, use qualified names that
 begin with the name of the packed project library to avoid conflicts with filenames
 already in memory, such as partial project libraries.

Parent topic:

Preparing Source Components for Deployment

Related concepts:

- Preparing Source Components for Deployment
- Manually Adding or Removing Files to or from Deployments
- Using a TestStand Workspace File to Create a Deployment
- Using a Directory to Create a Deployment
- Organizing Test Program Files with LabVIEW Project Libraries
- Partial Project Libraries
- Deploying Network-Published Shared Variables
- Deploying Stand-alone VIs
- Deploying VIs in LabVIEW Packed Project Libraries
- Deploying VIs in LabVIEW Projects

<!--NI_TOPIC bundle=teststand path=tsa-rules-description.html language=enus -->
## TOPIC 00926: TestStand Sequence Analyzer Rules Descriptions

- bundle_id: `teststand`
- source_path: `tsa-rules-description.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/tsa-rules-description.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following sections describe the built-in TestStand rules. General Statistics Analysis Errors Performance Best Practices General Rule Severity Description Expressions must evaluate to a value of the expected type Error Each expression property must not include syntax errors and must evaluate to a

### TestStand Sequence Analyzer Rules Descriptions

The following sections describe the built-in TestStand rules.

- General
- Statistics
- Analysis Errors
- Performance
- Best Practices

#### General

| Rule | Severity | Description |
| --- | --- | --- |
| Expressions must evaluate to a value of the expected type | Error | Each expression property must not include syntax errors and must evaluate to a value of the type the property expects. Syntax errors and incorrect value types can cause errors at run time. If you are certain that the expression will evaluate correctly at run time, such as when you dynamically create variables or when you propagate variables, use the #NoValidation directive in the expression to suppress the error. |
| Step properties must have valid values | Error | All step properties must have valid values. Invalid property values can cause errors at run time. Use the Step Settings pane to set the property to a valid value. Ignore this message if the property will be set dynamically to a correct value at run time. |
| Files must be found on disk | Error | File paths must refer to existing files on disk. TestStand can report errors at run time if it cannot find the file the path specifies. Correct the problem by correcting the path or by creating the file on disk. You can safely ignore this message if the file is created dynamically at run time. |
| Files should be found on disk | Warning | File paths should refer to existing files on disk. TestStand does not report errors at run time for these files, but the path specified cannot be found. Correct the problem by changing the path to point to the correct file or by creating the file on disk. Ignore this message if the file is created dynamically at run time. |
| Code modules must be able to load | Error | TestStand must be able to load all code modules without error. TestStand reports errors at run time when it cannot load a code module. Correct this problem by editing the step in the sequence editor. |
| Code modules should load without warnings | Warning | TestStand should be able to load all code modules without warnings. Module load warnings are issues that occur when trying to load a code module that might or might not be fatal or cause unexpected behavior. Correct this problem by editing the step in the sequence editor. |
| Code modules must have expected prototype | Error | The prototype for the code module must match the prototype the step module specifies. TestStand reports errors at run time when it loads a code module with an incompatible prototype. Correct the problem by editing the step module in TestStand to match the code module or by changing the code module prototype to match the step module. |
| Remote computer must be on the network | Error | Step properties that refer to remote computers must specify a valid network computer by IP address or by computer name. Ignore this message if the computer will exist at run time. |
| Steps must have expected block structure | Error | Steps with block structures, such as the Flow Control steps and the Auto Schedule step, must have matching End steps, and End steps must have a matching Begin step. Other block requirements exist for Select/Case and Auto Schedule/Use Auto Scheduled Resource steps. TestStand reports errors at run time for invalid block structures. |
| Variables should be used | Warning | Unused variables and parameters add unnecessary complexity and extraneous information to sequence files. Delete variables if you never access them. You can ignore this rule for variables that you access in code modules or that you access using a lookup string with the TestStand API. |
| Sequences should be used | Warning | Unused sequences add extraneous information to sequence files and needlessly increase the size of the file. Delete sequences if you never use them. You can ignore this error for sequences that you call by expression or if you call the sequence from a sequence file that was not analyzed. |
| Steps should have Normal run mode | Warning | The run mode option for step should be set to Normal instead of Force Pass, Force Fail, or Skip to ensure that tests are performed correctly. Correct the setting on the Run Options Panel of the Step Settings pane in the TestStand Sequence Editor. Ignore this message if a step is intentionally set to this run mode. |
| Sequence calls should match the sequence prototype | Warning | The prototype for the sequence that a sequence call step calls should match the prototype the step specifies. You can ignore this rule for sequence calls in which you intend to pass a different set of parameters and if you check the parameters in the called sequence. |
| Find file paths that expressions specify | Information | Files that path expressions reference might not be included in the set of files to analyze. This rule provides a list of those expressions. You might need to manually add files expressions reference to the workspace for correct deployment. |
| All escape sequences used in expressions must be valid | Error | The sequence analyzer checks expressions for valid escape sequences. Improperly escaping paths usually leads to using invalid escape sequences, which are rarely intended. |
| Expression error caused by missing dynamic property | Warning | Expressions that use dynamic properties, such as RunState, will evaluate with errors at edit time. Ensure that the variable referenced will exist at run time. This message occurs when an expression evaluation error occurs because of a missing variable that starts with RunState or Parameters and the parameter is a container or object reference. If this variable will exist at run time, you can safely ignore this message. |
| Types should have the correct version | Warning | Ensure that all types have versions that will not conflict with the default versions TestStand installs. This message can occur when you have a copy of CommonResults that is less than 3.1.0.100. National Instruments recommends that you set the version of CommonResults to the default of 3.1.0.100 if it contains no subproperties and set the version of CommonResults greater than 3.1.0.100 if it contains subproperties. Failure to change the version might cause type conflicts when loading files. |
| Steps that call LabVIEW modules configured with LabVIEW 7.1.1 or earlier should reload module prototypes | Warning | The prototype information stored on steps that call LabVIEW code modules might not be compatible with LabVIEW 2012 or later. This warning occurs for a step that calls a LabVIEW code module and the step was last configured using LabVIEW 7.1.1 or earlier. The step calls the code module correctly, but TestStand might generate an error when executing the step using LabVIEW 2012 or later. National Instruments recommends that you reload the prototype for the step or select Tools»Update VI Calls to run the Update VI Calls tool on any sequence file that return this warning. |
| Delete subelements of an output array parameter if you intend to log the entire array | Warning | If you enable additional result logging for an output array parameter on a LabVIEW or .NET step and the parameter contains subelements, the step logs only the subelements and not the entire array. An array parameter contains subelements if you added them manually when you specified the code module or if the code module is a LabVIEW VI that defines default element values for the array. To log the entire array, delete all the parameter subelements when you specify the code module. Ignore this message if you intend to log only the parameter subelements. |
| Find expressions that suppress evaluation errors | Information | Expressions that use the #NoValidation directive to suppress semantic evaluation errors might contain actual run-time errors. |
| Disable result recording for all process model sequences except the MainSequence callback | Warning | If you enable result recording for a process model sequence other than the MainSequence callback, On-The-Fly reporting might not work correctly. Disable result recording for all process model sequences except the MainSequence callback. |
| Property Loader source should be proper | Error | Property Loader source should exist. The source should be according to valid format. |
| Enumeration values must be valid | Error | Each instance of an enumeration point must have a value that the type defines as valid. |
| Code modules should be up-to-date | Warning | Code modules should be up-to-date. The Sequence Analyzer checks that the file modification time for the code module is more recent than those of source files specified in the adapter step.Note The Sequence Analyzer only checks source code files, project files, and solution/workspace files specified in the adapter step. It does not perform general dependency checking on included header files, other source files used by the code module, etc. |
| Feature is not supported | Error | Feature is not supported in the current bitness of TestStand that you are using. |

#### Statistics

| Rule | Severity | Description |
| --- | --- | --- |
| Count steps | Information | The total number of steps in all the analyzed files, including count per sequence, count per sequence file, and count per analysis. |
| Count sequences | Information | The total number of sequences in all the analyzed files, including count per sequence file and count per analysis. |
| Count sequence files | Information | The total number of sequence files analyzed. |

#### Analysis Errors

| Rule | Severity | Description |
| --- | --- | --- |
| Internal Error | Error | The sequence analyzer uses this rule to report internal errors that occur during analysis. These messages usually indicate a serious problem with a component of the sequence analyzer. Report the information to the component owner or to National Instruments. You cannot disable this rule. |
| File Open Error | Error | The sequence analyzer uses this rule to report errors that occur when opening files during analysis. You cannot disable this rule. |
| File Locked Error | Warning | The sequence analyzer uses this rule to report errors for files that it could not analyze because the files are locked and not viewable. You cannot disable this rule. |

#### Performance

| Rule | Severity | Description |
| --- | --- | --- |
| Watch expressions are enabled | Warning | Using watch expressions during execution can negatively affect performance and cause slower execution speed. Use watch expressions only when debugging. Select Debug»Breakpoints/Watch Expressions to remove unused watch expressions. |

#### Best Practices

| Rule | Severity | Description |
| --- | --- | --- |
| Avoid using absolute paths | Warning | Absolute paths make moving files among test systems difficult. Use relative paths to specify files. |
| All file paths must have a valid format | Error | All file path variables must contain valid syntax. The sequence analyzer verifies only that the syntax of the path is correct and does not confirm that a file exists at each location. |

Parent topic:

Analyzing Files

Related concepts:

- Expressions
- Code Modules

<!--NI_TOPIC bundle=teststand path=tsdu-deploy-w-env.html language=enus -->
## TOPIC 00927: Deploying with Environments Using the TestStand Deployment Utility

- bundle_id: `teststand`
- source_path: `tsdu-deploy-w-env.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/tsdu-deploy-w-env.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Deploying with Environments The TestStand Deployment Utility supports using an engine environment file (.tsenv) to deploy files from a custom <TestStand Public> directory or <TestStand Application Data> directory. In addition, the TestStand Deployment Utility allows you to specify an environment fil

### Deploying with Environments Using the
 TestStand Deployment Utility

#### Deploying with Environments

The TestStand Deployment Utility supports using an engine environment file
 (.tsenv) to deploy files from a custom <TestStand Public>
 directory or <TestStand Application Data> directory. In addition, the
 TestStand Deployment Utility allows you to specify an environment file for use on
 the deployment machine. If you do, files you deploy to the <TestStand Public>
 directory or <TestStand Application Data> directory will be deployed to the
 custom locations specified in the environment file. For more information about
 creating and using environment files, refer to the TestStand
 Environments
 topic.

#### Using Custom Environment Directories on the Development Machine

To use a custom TestStand Public directory and/or Application Data directory on the
 development machine, specify an environment file in the Engine
 Environment field of the System Source tab. Once you have specified
 an environment file, select the From TestStand Public
 Directories or From TestStand Configuration
 Directory to deploy files from the directory specified in the
 environment file. If you create a deployment with these settings, files will be
 deployed to the default TestStand Public and Application Data directories.

Note

Users.ini

Parent topic:

Choosing a Deployment Mechanism

Related concepts:

- TestStand Environments

Related information:

- TestStand Environment Reference Help

#### Deploying to Custom Environment
 Directories

To deploy files to your custom TestStand Public directory and/or Application Data
 directory on the deployment machine, select the Use Environment File To Determine
 Deployed File Destinations option. After selecting this option, use the
 Destination View in the Distributed Files tab to preview the destinations for files deployed
 to the TestStand Public or Application Data destinations. The custom destination path is
 displayed in parentheses after the destination name.

```text
<destination for environment file> + <custom path specified in environment file>
```

To
 access the custom directories on the deployment machine, your deployed User
 Interface must use the deployed environment file. You can use the command line flag
 /env <Environment File Path> when launching a user
 interface executable to configure the environment file it uses upon launch. Follow
 these steps specify that the deployment utility create a shortcut to a user
 interface with this flag:

1. In the Distributed Files tab, select the user interface
 executable.
2. Click the Shortcuts button to launch the shortcuts
 dialog box.
3. Click Add Shortcut to create a new shortcut.
4. Set the shortcut base path to the same base path you selected for the
 environment file.
5. Set the shortcut relative path to the same relative path of the environment
 file.
6. Set the command line arguments to /env
 <EnvironmentFilename>, where
 <EnvironmentFilename> is the name of the environment
 file you selected on the System Source tab.
7. Ensure that the user interface is deployed to the same destination as the
 environment file.

#### Using a Different Environment File on the
 Deployment Machine

You can configure the TestStand Deployment Utility to use a different environment file to
 determine the custom locations for the TestStand Public directory and/or Application Data
 directory.

Follow these steps to configure an
 environment file for use on the deployment machine:

1. In the Distributed Files tab, select the environment file
 you specified in the Active Engine Environment
 field.
2. Use the browse button for the Replacement Path field to
 select a different environment file.

Once the file is replaced, the custom destination paths
 will update to reflect the paths in the selected file.

<!--NI_TOPIC bundle=teststand path=type-casting-api-classes-labview.html language=enus -->
## TOPIC 00928: Type Casting API Classes - LabVIEW

- bundle_id: `teststand`
- source_path: `type-casting-api-classes-labview.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/type-casting-api-classes-labview.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Purpose This example demonstrates how to type cast TestStand objects in order to access specific API properties and methods. Example File Location <TestStand Public>\Examples\\TestStand API\Type Casting API Classes\LabVIEW\Type Casting API Classes.seq Highlighted Features Built-In Properties Dynamic

### Type Casting API Classes - LabVIEW

#### Purpose

This example demonstrates how to type cast TestStand objects in order to access specific API properties and methods.

#### Example File
 Location

<TestStand
 Public>\Examples\\TestStand API\Type Casting API
 Classes\LabVIEW\Type Casting API Classes.seq

#### Highlighted Features

- Built-In Properties
- Dynamic Properties
- RunState Property
- TestStand API

#### Major API

- PropertyObject.GetPropertyObject
- SequenceFile.AsPropertyObjectFile
- SequenceFile.AsPropertyObject

#### Prerequisites

None

#### How to Use This Example

Complete the following steps to review the code in this example:

1. Open the Cast to More Generic Class sequence from the Sequences pane. Select the Cast to More Generic Class step, then click Edit VI in the Module tab of the Step Settings pane to open the code module. This step casts a sequence file object to the more generic propertyObject and PropertyObjectFile classes to access their properties and methods.
2. Open the Cast to More Specific Class sequence from the Sequences pane. Select the Cast to More Specific Class step, then click Edit VI in the Module tab of the Step Settings pane to open the code module. This step casts a PropertyObject to more specific classes to access their properties and methods.

Complete the following steps to run the example:

1. Select Execute»Run MainSequence to execute the sequence.
2. As the sequence executes, read the message popups for information about the kinds of type casting available in the TestStand API.

Parent topic:

Type Casting API Classes

Related concepts:

- TestStand Directory Structure
- Accessing Built-in Properties
- Accessing Dynamic Properties
- RunState Subproperties

<!--NI_TOPIC bundle=teststand path=type-casting-api-classes-labwindows-cvi.html language=enus -->
## TOPIC 00929: Type Casting API Classes - LabWindows/CVI

- bundle_id: `teststand`
- source_path: `type-casting-api-classes-labwindows-cvi.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/type-casting-api-classes-labwindows-cvi.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Purpose This example demonstrates how to type cast TestStand objects in order to access specific API properties and methods. Example File Location <TestStand Public>\Examples\TestStand API\Type Casting API Classes\CVI\Type Casting API Classes.seq Highlighted Features Built-In Properties Dynamic Prop

### Type Casting API Classes - LabWindows/CVI

#### Purpose

This example demonstrates how to type cast TestStand objects in order to access specific API properties and methods.

#### Example File
 Location

<TestStand
 Public>\Examples\TestStand API\Type Casting API Classes\CVI\Type
 Casting API Classes.seq

#### Highlighted Features

- Built-In Properties
- Dynamic Properties
- RunState Property
- TestStand API

#### Major API

- PropertyObject.GetPropertyObject
- SequenceFile.AsPropertyObjectFile
- SequenceFile.AsPropertyObject

#### Prerequisites

None

#### How to Use This Example

Complete the following steps to review the code in this example:

1. Open the Cast to More Generic Class sequence from the Sequences pane. Select the Cast to More Generic Class step, then click Edit Code in the Module tab of the Step Settings pane to open the code module. This step casts a sequence file object to the more generic propertyObject and PropertyObjectFile classes to access their properties and methods.
2. Open the Cast to More Specific Class sequence from the Sequences pane. Select the Cast to More Specific Class step, then click Edit Code in the Module tab of the Step Settings pane to open the code module. This step casts a PropertyObject to more specific classes to access their properties and methods.

Complete the following steps to run the example:

1. Select Execute»Run MainSequence to execute the sequence.
2. As the sequence executes, read the message popups for information about the kinds of type casting available in the TestStand API.

Parent topic:

Type Casting API Classes

Related concepts:

- TestStand Directory Structure
- Accessing Built-in Properties
- Accessing Dynamic Properties
- RunState Subproperties

<!--NI_TOPIC bundle=teststand path=type-casting-api-classes-net.html language=enus -->
## TOPIC 00930: Type Casting API Classes - .NET

- bundle_id: `teststand`
- source_path: `type-casting-api-classes-net.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/type-casting-api-classes-net.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Purpose This example demonstrates how to type cast TestStand objects in order to access specific API properties and methods. Example File Location <TestStand Public>\Examples\TestStand API\Type Casting API Classes\dotNET\Type Casting API Classes.seq Highlighted Features Built-In Properties Dynamic P

### Type Casting API Classes - .NET

#### Purpose

This example demonstrates how to type cast TestStand objects in order to access specific API properties and methods.

#### Example File
 Location

<TestStand
 Public>\Examples\TestStand API\Type Casting API
 Classes\dotNET\Type Casting API Classes.seq

#### Highlighted Features

- Built-In Properties
- Dynamic Properties
- RunState Property
- TestStand API

#### Major API

- PropertyObject.GetPropertyObject
- SequenceFile.AsPropertyObjectFile
- SequenceFile.AsPropertyObject

#### Prerequisites

None

#### How to Use This Example

Complete the following steps to review the code in this example:

1. Open the Cast to More Generic Class sequence from the Sequences pane. Select the Cast to More Generic Class step, then click Edit in Visual Studio in the Module tab of the Step Settings pane to open the code module. This step casts a sequence file object to the more generic propertyObject and PropertyObjectFile classes to access their properties and methods.
2. Open the Cast to More Specific Class sequence from the Sequences pane. Select the Cast to More Specific Class step, then click Edit in Visual Studio in the Module tab of the Step Settings pane to open the code module. This step casts a PropertyObject to more specific classes to access their properties and methods.

Complete the following steps to run the example:

1. Select Execute»Run MainSequence to execute the sequence.
2. As the sequence executes, read the message popups for information about the kinds of type casting available in the TestStand API.

Parent topic:

Type Casting API Classes

Related concepts:

- TestStand Directory Structure
- Accessing Built-in Properties
- Accessing Dynamic Properties
- RunState Subproperties

<!--NI_TOPIC bundle=teststand path=type-casting-api-classes-teststand-expression.html language=enus -->
## TOPIC 00931: Type Casting API Classes - TestStand Expressions

- bundle_id: `teststand`
- source_path: `type-casting-api-classes-teststand-expression.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/type-casting-api-classes-teststand-expression.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Purpose This example demonstrates how to type cast TestStand objects in order to access specific API properties and methods. Example File Location <TestStand Public>\Examples\TestStand API\Type Casting API Classes\TestStand Expressions\Type Casting API Classes.seq Highlighted Features Built-In Prope

### Type Casting API Classes - TestStand Expressions

#### Purpose

This example demonstrates how to type cast TestStand objects in order to access specific API properties and methods.

#### Example File
 Location

<TestStand
 Public>\Examples\TestStand API\Type Casting API Classes\TestStand
 Expressions\Type Casting API Classes.seq

#### Highlighted Features

- Built-In Properties
- Dynamic Properties
- RunState Property
- TestStand API

#### Major API

- PropertyObject.GetPropertyObject
- SequenceFile.AsPropertyObjectFile
- SequenceFile.AsPropertyObject

#### Prerequisites

None

#### How to Use This Example

Complete the following steps to review the code in this example:

1. Open the Cast an Object Reference sequence from the Sequences pane. Review the statement steps in this sequence. These steps cast a generic object reference to a specific class to access the properties of the specific class.
2. Open the Cast to More Generic Class sequence from the Sequences pane. Review the statement steps in this sequence. These steps cast a sequence file object to the more generic propertyObject and PropertyObjectFile classes to access their properties and methods.
3. Open the Cast to More Specific Class sequence from the Sequences pane. Review the statement steps in this sequence. These steps cast a PropertyObject to more specific classes to access their properties and methods.

Complete the following steps to run the example:

1. Select Execute»Run MainSequence to execute the sequence.
2. As the sequence executes, read the message popups for information about the kinds of type casting available in the TestStand API.

Parent topic:

Type Casting API Classes

Related concepts:

- TestStand Directory Structure
- Accessing Built-in Properties
- Accessing Dynamic Properties
- RunState Subproperties

<!--NI_TOPIC bundle=teststand path=type-casting-api-classes.html language=enus -->
## TOPIC 00932: Type Casting API Classes

- bundle_id: `teststand`
- source_path: `type-casting-api-classes.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/type-casting-api-classes.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The <TestStand Public>\Examples\TestStand API\Type Casting API Classes directory contains the following examples.

### Type Casting API Classes

The <TestStand
 Public>\Examples\TestStand API\Type Casting API Classes
 directory contains the following examples.

- [Type Casting API Classes - LabWindows/CVI](type-casting-api-classes-labwindows-cvi.html)
- [Type Casting API Classes - LabVIEW](type-casting-api-classes-labview.html)
- [Type Casting API Classes - .NET](type-casting-api-classes-net.html)
- [Type Casting API Classes - TestStand Expressions](type-casting-api-classes-teststand-expression.html)

Parent topic:

Examples for the TestStand API

Related concepts:

- TestStand Directory Structure

<!--NI_TOPIC bundle=teststand path=type-concepts.html language=enus -->
## TOPIC 00933: Type Concepts

- bundle_id: `teststand`
- source_path: `type-concepts.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/type-concepts.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: TestStand stores step type and data type definitions in files and in memory. You can modify types and use type version numbers to determine which version of the type to load. Use the Types window to create, modify, and examine step types and data types. You can password-protect types so that other T

### Type Concepts

TestStand stores step type and data type definitions in files and in memory. You can modify types and use type version numbers to determine which version of the type to load. Use the Types window to create, modify, and examine step types and data types. You can password-protect types so that other TestStand users cannot modify the types in the TestStand Sequence Editor.

Parent topic:

Extending TestStand

Related concepts:

- Step Types
- Standard and Custom Data Types
- Modifying Type Instances, Values, and Type Definitions
- Type Versioning
- Password-Protecting Types

<!--NI_TOPIC bundle=teststand path=type-palette-files.html language=enus -->
## TOPIC 00934: Type Palette Files

- bundle_id: `teststand`
- source_path: `type-palette-files.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/type-palette-files.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Type palette files contain step types, standard data types, and custom data types you want available in the TestStand Sequence Editor or in the TestStand User Interfaces at all times. Drag a type to a type palette file in the Types window to ensure that the type is always available, even when the Us

### Type Palette Files

Type palette files contain step types, standard data types, and custom data types you want available in the TestStand Sequence Editor or in the TestStand User Interfaces at all times. Drag a type to a type palette file in the Types window to ensure that the type is always available, even when the User Manager window, station global variables, or any open sequence files do not use the type.

Type palette files are located in the <TestStand>\Components\TypePalettes directory.
 Typically, you create new types in the MyTypes.ini type palette
 file in the <TestStand Public>\Components\TypePalettes
 directory or in a new type palette file you create.

You can distribute step types and data types you create to other computers by copying a type
 palette file to the <TestStand
 Public>\Components\TypePalettes directory. Right-click the
 View Types For pane in the Types window and select
 Customize Type Palettes from the context menu to launch
 the Configure Type Palettes dialog box, in which you can specify which type palette
 files TestStand uses.

#### Adding Type Palette Files

Use one of the following methods to add a type palette file to an existing installation.

- Copy the file to the <TestStand Public>\Components\TypePalettes directory. When you launch the sequence editor or a user interface, TestStand searches this directory for new files and adds those files to the type palette list. Note TestStand will not add a type palette file that you explicitly excluded from the type palette list, even if you add the file to the <TestStand Public>\Components\TypePalettes directory.
- Copy the file to the <TestStand Public>\Components\TypePalettes directory and add the prefix Install_ to the file name. When you launch the sequence editor or a user interface, TestStand identifies files with the Install_ prefix and takes one of the following actions:
  - If TestStand locates a type palette file in the type palette list with the same name, but without the Install_ prefix, TestStand merges the types in the Install_ prefix version of the file with the types in the existing file and then deletes the Install_ prefix version.
  - If TestStand locates a type palette file with the same name, but without the Install_ prefix, that is not included in the type palette list because a user explicitly excluded it, TestStand does not change the contents of either file. Note To ensure that TestStand always installs a type palette file, even when previously excluded from the type palette list, you must first delete the original version of the file—which does not contain the Install_ prefix—before you copy the Install_ prefix version to the <TestStand Public>\Components\TypePalettes directory.
  - If TestStand does not locate a type palette file with the same name, but without the Install_ prefix, TestStand creates a new file with the same name and adds it to the type palettes list. TestStand then adds the types in the Install_ prefix version of the file to the new type palette file and deletes the Install_ prefix version.
- Click Add in the Configure Type Palettes dialog box to manually add the type palette file.

Parent topic:

Type Concepts

Related concepts:

- Station Global Variables
- TestStand Directory Structure
- Deploying Type Palette Files

<!--NI_TOPIC bundle=teststand path=type-versioning.html language=enus -->
## TOPIC 00935: Type Versioning

- bundle_id: `teststand`
- source_path: `type-versioning.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/type-versioning.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use only one version of a type at a time. TestStand uses the version number of a type to determine which version of a type to use when opening a file that has a different version of the type than the version currently in memory. Typically, the version of the type with the latest version numb

### Type Versioning

You can use only one version of a type at a time. TestStand uses the version number of a type to determine which version of a type to use when opening a file that has a different version of the type than the version currently in memory. Typically, the version of the type with the latest version number is the version that TestStand automatically uses.

In versions of TestStand earlier than version 4.1, the propagation of unwanted type versions between files could occur when you open a sequence file with a version of a type later than the version of the type in a type palette file. The automatic type conflict resolution in TestStand updated the type palette file and every file you subsequently opened to use the later version without warning or notification.

In TestStand 4.1 or later, if the type is in a type palette file, the latest version must also be the version in the type palette file and the earlier version must exist in a file other than a type palette file for automatic type conflict resolution to occur. This behavior avoids propagation of unwanted type versions. You can modify the behavior to become more or less strict by changing the value of the Allow Automatic Type Conflict Resolution option on the File tab of the Station Options dialog box.

Use the Set Earliest TestStand Versions that can Use this Type option on the Version tab of the Type Properties dialog box to specify the earliest TestStand version that can use a type to prevent the TestStand Engine from using the type when the version of the engine is earlier than the TestStand version you specify. When you enable this option and an earlier version of the engine attempts to load the type, TestStand ignores the type and loads the file only when an earlier version of the type already exists in memory. If you do not specify the earliest TestStand version that can use a type and you set the Allow Automatic Type Conflict Resolution option on the File tab of the Station Options dialog box to Always, future versions of a type might propagate into type palette files and sequence files that run in the previous TestStand version.

Parent topic:

Type Concepts

Related concepts:

- Avoiding Unwanted Type Version Propagation
- Managing Type Revisions

<!--NI_TOPIC bundle=teststand path=types-of-information-the-profiler-records.html language=enus -->
## TOPIC 00936: Types of Information the Profiler Records

- bundle_id: `teststand`
- source_path: `types-of-information-the-profiler-records.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/types-of-information-the-profiler-records.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Types of Information the Profiler Records Events The Execution Profiler records events that contain information about the following: Step and Step Type Module Execution Times—The duration of code modules that steps call using any adapter, including subsequences called by Sequence Call steps. Step an

### Types of Information the Profiler Records

#### Types of Information the Profiler Records

#### Events

The Execution Profiler records events that contain information about the following:

- Step and Step Type Module Execution Times —The duration of code modules that steps call using any adapter, including subsequences called by Sequence Call steps.
- Step and Step Type Module Load and Unload Times —The time spent loading and unloading LabVIEW VIs, C/C++ dlls, .NET assemblies, and COM servers that steps and step types call.
- Step Execution Times —The complete execution duration for each step. This includes the code modules it calls, step looping, expression evaluation, result recording, post actions, switching, synchronization, and any other actions a step is configured to perform.
- Batch, UUT, and Lot Duration —The time period spent testing each UUT, each Batch, and each Lot.

 Note 

 A Lot is a series of batches tested using the NI TestStand Semiconductor Module.
- Synchronization Operations —The time spent waiting and duration of use for all synchronization operations, including operations on Locks, Notifications, Queues, Semaphores, Batch Synchronization Sections, Auto Schedule Blocks, and explicit Waits.

For each event, the profiler records the time of the event, the TestStand thread and execution in which it occurs, the sequence file, and location in the file from which it initiates. The profiler also records the name of the item for the event. The item name depends on what triggers the event. For example, it could be the name of a TestStand lock for a Lock event, or a description of a code module call for a step module event. The profiler also records other information, such as the index of the test socket from which the event originates.

The Events table displays a list of all the events the Execution Profiler has recorded.

#### Operations

The profiler associates multiple related events for the same item in the same thread with the logical operation that the events record. For example, a Wait operation associates the two events that the profiler records when a thread waits: the Blocked event, which records when the thread begins waiting, and the Completed event, which records when the thread resumes execution.

The Operations table display these operations. You can also view operations in both of the graphs the profiler provides. Typically, you use the profiler primarily to view various operations and how they relate to each other in initiation time, duration, and by thread.

#### Items

Each operation the profiler records originates from a specific item. The item might be a code module, a synchronization object, a UUT, a Batch, a Lot, or a Step. The Items table displays all the items for which the profiler has recorded information. You can view the number of times an item is used and the total time spent using an item. You can also select and navigate to the Operations or Events for selected items.

The Items table contains a list of all code modules, steps, UUTs, batches, lots, and synchronization objects for which the Execution Profiler has recorded events.

#### Threads

The profiler displays a list of every thread in which a profiler event occurs in the Threads table. You can use the Threads table to view the amount of time a thread has been in use by or blocked waiting for profiled operations. You can view the number of operations in and the number of items used by each thread. If a thread is the root thread for a test socket execution, the profiler displays its test socket index. If a profiler event occurs in a thread that is not a TestStand execution thread, the thread name displays Non-Execution Thread. Note that TestStand often uses non-execution threads to load and unload modules.

#### Executions

The profiler displays a list of the executions that contain the threads that the Threads table displays. You can select and navigate to the Threads in each execution. Threads that are not TestStand execution threads appear in the profiler as belonging to an item in the execution table named Not-An-Execution.

The Executions table contains a list of all executions that contain threads for which the Execution Profiler recorded events."

Parent topic:

Execution Profiler

Related information:

- Step Settings Pane
- Lock Step

<!--NI_TOPIC bundle=teststand path=uninstalling-a-teststand-deployment.html language=enus -->
## TOPIC 00937: Uninstalling a TestStand Deployment

- bundle_id: `teststand`
- source_path: `uninstalling-a-teststand-deployment.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/uninstalling-a-teststand-deployment.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: A TestStand deployment that has been installed on a test station computer will appear in the Microsoft Add/Remove Programs utility on the test station computer. Use the Add/Remove Programs utility to uninstall the distribution from the test station computer and remove all installed test system files

### Uninstalling a TestStand Deployment

A TestStand deployment that has been installed on a test station computer will appear in the Microsoft Add/Remove Programs utility on the test station computer. Use the Add/Remove Programs utility to uninstall the distribution from the test station computer and remove all installed test system files.

Note

Parent topic:

Building an Installer with the TestStand Deployment Utility

Related concepts:

- NI MSI-based Installer Architecture

<!--NI_TOPIC bundle=teststand path=update-py-module-debug.html language=enus -->
## TOPIC 00938: Updating Python Modules while Debugging

- bundle_id: `teststand`
- source_path: `update-py-module-debug.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/update-py-module-debug.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `task`
- source_description: You can modify and reload Python modules while debugging a test sequence. The following steps are useful during test development and debugging. However, NI recommends you avoid reloading updated Python modules when running tests in a production environment. Ensure that Reload Modified Modules Before

### Updating Python Modules while
 Debugging

Note

1. Ensure that Reload Modified Modules Before Execution is
 enabled in the Python Adapter Configuration dialog box. 
 Note TestStand prompts you to unload all modules when you modify
 this setting.
2. Execute the sequence and step into a Python code module.
3. While execution is stopped, modify the code module the Python step calls, then
 resume execution. TestStand will use any modifications you make when it executes
 the step.

- Reloading an updated module behaves like importing the module for the first
 time. Global variables are reset to the default value, and any statement at the
 module level is executed.
- TestStand reloads only the module the step executes, but not dependent
 modules.
- If you modify a module that defines a class and another module stores an
 instance of that class, TestStand does not reload the second module when it
 reloads the first one. You must reload the second module to discard any
 instances of the objects and create new instances.
- If any Python object such as a class instance exists, and you modify the object,
 you must recreate the class instance after reloading the module.

Parent topic:

Python Adapter

<!--NI_TOPIC bundle=teststand path=updates-to-default-database-schemas.html language=enus -->
## TOPIC 00939: Updates to Default Database Schemas

- bundle_id: `teststand`
- source_path: `updates-to-default-database-schemas.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/updates-to-default-database-schemas.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: When the default database schema is updated in new versions of TestStand, the old default database schemas remain available as legacy schemas. The following table summarizes changes to the default database schema: 3 Changes to the Default Database Schema Version Default Database Schema Changes TestS

### Updates to Default Database Schemas

When the default database schema is updated in new versions of TestStand, the old default
 database schemas remain available as legacy schemas.

The following table summarizes changes to the default database schema:

| Version | Default Database Schema Changes |
| --- | --- |
| TestStand 2020 | The data types for the following columns in the PROP_NUMERICLIMIT table were changed from Numeric to String to enable TestStand to log INF, -INF, NAN and IND values when you use them as limits of Numeric Limit Test and Multi Numeric Limit Test steps. LOW_LIMITHIGH_LIMITNOMINAL_VALUELOWER_THRESHOLDHIGHER_THRESHOLD |
| TestStand 2016 | The following columns were added to the PROP_NUMERICLIMIT table to log limit values when you use the EQT comparison type in Numeric Limit Test and Multi Numeric Limit Test. THRESHOLD_TYPENOMINAL_VALUELOWER_THRESHOLDHIGHER_THRESHOLD |
| TestStand 2012 | The following columns were added to the UUT_RESULT table to log the part number of the UUT and data from the TestStand Offline Results Processor. PART_NUMBERTSR_FILE_NAMETSR_FILE_IDTSR_FILE_CLOSED |
| TestStand 4.1 | The following changes were made to support logging additional results: The tables listed below are no longer included and this information is logged in the PROP_RESULT table, which includes property result information and simple intrinsic property values. The PROP_RESULT table contains a foreign key that references the STEP_RESULT table. STEP_PASSFAILSTEP_CALLEXESTEP_MSGPOPUPSTEP_PROPERTYLOADERSTEP_STRINGVALUEMEAS_IVI_SINGLEPOINTThe following tables were added, each of which contains a foreign key that references the PROP_RESULT table: PROP_BINARY—logs binary data, such as array values. PROP_ANALOGWAVEFORM—logs analog waveform data, such as the LabVIEWAnalogWaveform, NI_IviWave, and NI_IviWavePair data types. This table replaces the MEAS_IVI_WAVE and MEAS_IVI_WAVEPAIR tables in previous versions of TestStand. PROP_DIGITALWAVEFORM—logs digital waveform data, such as the LabVIEWDigitalWaveform data type. PROP_NUMERICLIMIT—logs numeric limit data. This table replaces the MEAS_NUMERICLIMIT table in previous versions of TestStand. The following new fields were added to the STEP_RESULT table: STEP_ID—specifies the unique step ID.CAUSED_SEQFAIL—specifies whether a step caused a sequence failure. |

Related concepts:

- Using Legacy Database Schemas
- PROP_NUMERICLIMIT Table Schema
- PROP_RESULT Table Schema
- PROP_BINARY Table Schema
- PROP_ANALOGWAVEFORM Table Schema
- PROP_DIGITALWAVEFORM Table Schema
- STEP_RESULT Table Schema
- Default TestStand Table Schemas

<!--NI_TOPIC bundle=teststand path=updating-and-patching-stand-alone-vis.html language=enus -->
## TOPIC 00940: Updating and Patching Stand-alone VIs

- bundle_id: `teststand`
- source_path: `updating-and-patching-stand-alone-vis.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/updating-and-patching-stand-alone-vis.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Consider the following recommendations and requirements for updating and patching VIs when you decide whether to use stand-alone VIs in a TestStand system: Inplaceness allows LabVIEW to reuse memory a caller VI uses in a subVI, thus reducing the memory requirements of the test system. Because of inp

### Updating and Patching Stand-alone VIs

Consider the following recommendations and requirements for updating and patching VIs when you decide whether to use stand-alone VIs in a TestStand system:

- Inplaceness allows LabVIEW to reuse memory a caller VI uses in a subVI, thus reducing the memory
 requirements of the test system. Because of inplaceness changes, a change to a
 subVI can affect all VIs that call the subVI even if the connector pane of the
 subVI remains constant, therefore forcing all calling VIs to recompile. Note NI recommends
 using LabVIEW packed project libraries to modularize a TestStand system. If
 you do not use LabVIEW packed project libraries, the TestStand Deployment
 Utility might take longer to create the deployment because the utility
 rebuilds the source distributions for all the VIs in the test system. The
 deployment utility completes this step to avoid run-time errors that might
 occur when the LabVIEW Run-Time Engine loads VIs that require recompilation
 to account for inplaceness changes.
- Stand-alone VIs do not have version resources. If a file does not have a version resource, installers use a heuristic process to determine whether to upgrade the file. These heuristics might cause confusion when VIs are not upgraded as you expected, such as a test system in which multiple installers update a single set of utility VIs. You can use the Force File to Install option on the Distributed Files tab of the deployment utility to install files regardless of the heuristic to guarantee new files install over the files that exist on the target computer. Note The deployment utility automatically enables the Force File to Install option when you create a patch deployment.

Parent topic:

Organizing Test Program Files with Stand-alone VIs

Related concepts:

- Organizing Test Program Files with Stand-alone VIs
- Organizing Test Program Files with LabVIEW Packed Project Libraries
- Managing Versioned and Non-Versioned Files
- Deploying Stand-alone VIs
- Deploying TestStand Systems
- Editing Stand-alone VIs
- Patching LabVIEW VIs

<!--NI_TOPIC bundle=teststand path=updating-and-patching-vis-in-labview-packed-p.html language=enus -->
## TOPIC 00941: Updating and Patching VIs in LabVIEW Packed Project Libraries

- bundle_id: `teststand`
- source_path: `updating-and-patching-vis-in-labview-packed-p.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/updating-and-patching-vis-in-labview-packed-p.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: LabVIEW packed project libraries are designed to make patching easier. Packed project libraries have an MSI-recognized version resource number, which you can use to more easily make partial updates to the test system. You can replace a packed project library with a newer version without changing the

### Updating and Patching VIs in LabVIEW Packed Project Libraries

LabVIEW packed project libraries are designed to make patching easier. Packed project libraries have an MSI-recognized version resource number, which you can use to more easily make partial updates to the test system. You can replace a packed project library with a newer version without changing the VI or the TestStand steps that call into the packed project library.

By default, the TestStand Deployment Utility automatically includes files that differ from the baseline deployment version of the file. You must compile all LabVIEW packed project libraries before you create a patch deployment to ensure that the deployment utility correctly identifies modified libraries to include in the patch deployment.

Parent topic:

Organizing Test Program Files with LabVIEW Packed Project Libraries

Related concepts:

- Organizing Test Program Files with LabVIEW Packed Project Libraries
- Managing Versioned and Non-Versioned Files
- Patching Deployments
- Deploying TestStand Systems
- Deploying VIs in LabVIEW Packed Project Libraries
- Editing VIs in LabVIEW Packed Project Libraries
- Patching LabVIEW VIs

<!--NI_TOPIC bundle=teststand path=updating-and-patching-vis-in-labview-projects.html language=enus -->
## TOPIC 00942: Updating and Patching VIs in LabVIEW Projects

- bundle_id: `teststand`
- source_path: `updating-and-patching-vis-in-labview-projects.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/updating-and-patching-vis-in-labview-projects.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: NI recommends using LabVIEW packed project libraries to modularize a TestStand system. You can create a patch deployment for a modularized system more quickly by rebuilding only the packed project libraries you modify. If you do not use LabVIEW packed project libraries, the TestStand Deployment Util

### Updating and Patching VIs in LabVIEW Projects

NI recommends using LabVIEW packed project libraries to modularize a TestStand system. You can
 create a patch deployment for a modularized system more quickly by rebuilding only
 the packed project libraries you modify.

If you do not use LabVIEW packed project libraries, the TestStand Deployment Utility might take longer to create the deployment because the utility rebuilds the source distributions for all the VIs in the test system. The deployment utility completes this step to avoid run-time errors that might occur when the LabVIEW Run-Time Engine loads VIs that require recompilation to account for inplaceness changes.

You can use the Force File to Install option on the Distributed Files tab of the deployment utility to install files to guarantee new files install over the files that exist on the target computer.

Note

Parent topic:

Organizing Test Program Files with LabVIEW Projects

Related concepts:

- Organizing Test Program Files with LabVIEW Packed Project Libraries
- Patching Deployments
- Deploying TestStand Systems
- Deploying VIs in LabVIEW Projects
- Editing VIs in LabVIEW Projects
- Patching LabVIEW VIs

<!--NI_TOPIC bundle=teststand path=updating-cluster-elem-mapping.html language=enus -->
## TOPIC 00943: Updating Cluster Element Mapping

- bundle_id: `teststand`
- source_path: `updating-cluster-elem-mapping.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/updating-cluster-elem-mapping.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `task`
- source_description: If the Value column of the VI Parameter Table on the LabVIEW Module tab contains a '??? <Unknown Value>' error for a subproperty of a parameter, TestStand cannot map the subproperty to a cluster element because the cluster item names the TestStand type defines do not match the names in the LabVIEW c

### Updating Cluster Element Mapping

If the Value column of the VI Parameter
 Table on the LabVIEW Module tab contains a '??? <Unknown Value>' error for a
 subproperty of a parameter, TestStand cannot map the subproperty to a cluster element
 because the cluster item names the TestStand type defines do not match the names in the
 LabVIEW cluster definition. Complete the following steps to update the
 subproperty.

1. Select View»Types to launch the Types window.
2. Browse to the definition of the type for the parameter that contains the
 subproperty with the unknown value. Right-click the type and select
 Properties to launch the Type Properties dialog
 box.
3. Click the LabVIEW Cluster Passing tab.
4. In the Property ring control, select the subproperty with the unknown value. If
 the Cluster Item Label control is empty or if the subproperty name is
 misspelled, TestStand cannot map the subproperty to a cluster element.
5. Enter the correct name for the subproperty in the Cluster Item Label control
 and click OK.
6. On the LabVIEW Module tab, click the Apply Cluster Passing
 Changes
 [IMAGE alt='image' src='GUID-6B826889-125C-4657-932D-6D9F8FBCE044-a5.gif']
 button, located in the Type column of the VI Parameter Table for the parameter
 that contains the subproperty.
7. Click Yes in the Update Cluster Mapping dialog box to
 confirm that you want to apply the changes.

Parent topic:

Module Adapters

<!--NI_TOPIC bundle=teststand path=updating-enumeration-parameter-values.html language=enus -->
## TOPIC 00944: Enumeration Parameter Value Update Behavior

- bundle_id: `teststand`
- source_path: `updating-enumeration-parameter-values.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/updating-enumeration-parameter-values.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: If you change the number of items in an enumeration in LabVIEW, you must reload the VI prototype for a VI that uses the enumerated values as parameters in TestStand before you can execute the sequence. When you reload a VI prototype and you specify an expression for the enumeration parameter, TestSt

### Enumeration Parameter Value Update
 Behavior

If you change the number of items in an enumeration in LabVIEW, you must reload the VI prototype for a VI that uses the enumerated values as parameters in TestStand before you can execute the sequence.

When you reload a VI prototype and you specify an expression for the enumeration parameter, TestStand always retains the expression.

When you reload a VI prototype and you do not specify an expression for the enumeration parameter, TestStand updates enumeration parameter values in the following ways depending on the version of LabVIEW you are using:

- (LabVIEW 2011 SP1 or earlier) TestStand retains the numeric value and updates the corresponding string label to match the numeric value. If you delete the numeric value, TestStand updates the string label to use the last enumeration value in the list.
- (LabVIEW 2012 or later) TestStand updates enumeration parameter values in a way similar to how LabVIEW updates enumeration controls. TestStand updates enumeration parameter values differently depending on whether the enumeration is an instance of a LabVIEW type definition, as the following tables describe.

#### When the Enumeration Is an Instance of a LabVIEW Type Definition

The following table describes how TestStand updates enumeration parameter values when you reload the VI prototype, you do not specify an expression for the enumeration parameter, and the enumeration is an instance of a LabVIEW type definition.

| Change You Make to LabVIEW Type Definition | Effect You See in TestStand VI Parameter Table | Effect You See in TestStand Step Properties |
| --- | --- | --- |
| You modify or delete the string label, and the numeric value currently stored in the step property matches another string label. | TestStand retains the numeric value and updates the corresponding string label to match the numeric value. | TestStand retains the numeric value and updates the corresponding string label. |
| You move the string label to a different position in the list of enumeration values. | TestStand retains the string label. | TestStand retains the string label and updates the corresponding numeric value. |
| You delete the string label and the numeric value. | TestStand updates the string label to use the last enumeration value in the list. | TestStand updates the numeric value and updates the string label to use the last enumeration value in the list. |

#### When the Enumeration Is Not an Instance of a LabVIEW Type Definition

The following table describes how TestStand updates enumeration parameter values when you reload the VI prototype, you do not specify an expression for the enumeration parameter, and the enumeration is not an instance of a LabVIEW type definition.

| Change You Make in VI | Effect You See in TestStand VI Parameter Table | Effect You See in TestStand Step Properties |
| --- | --- | --- |
| You delete the numeric value currently stored in the step property. | TestStand updates the string label to use the last enumeration value in the list. | TestStand updates the numeric value and updates the string label to use the last enumeration value in the list. |
| You update the string label but retain the numeric value currently stored in the step property. | TestStand updates the string label. | TestStand retains the numeric value and updates the corresponding string label. |

Parent topic:

LabVIEW Adapter

<!--NI_TOPIC bundle=teststand path=updating-step-properties.html language=enus -->
## TOPIC 00945: Updating Step Properties

- bundle_id: `teststand`
- source_path: `updating-step-properties.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/updating-step-properties.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use the following methods to pass data between the code module and TestStand: Use the tTestData structure Use the sequence context ActiveX reference to call the TestStand ActiveX API functions to set the variables used to store the results of the test, such as Step.Result.PassFail Before cal

### Updating Step Properties

You can use the following methods to pass data between the code module and TestStand:

- Use the tTestData structure
- Use the sequence context ActiveX reference to call the TestStand ActiveX API functions to set the variables used to store the results of the test, such as Step.Result.PassFail

Before calling a code module, the LabWindows/CVI Adapter assigns values from TestStand to input fields of the tTestData structure. After calling the code module, the LabWindows/CVI Adapter copies the values of the output fields of the structures to properties of the step. The LabWindows/CVI Adapter copies a value into a property when the following conditions are true:

- The property exists
- The code module does not change the value of the property directly through the TestStand API

In some cases, the LabWindows/CVI Adapter translates the value of a structure field to a different value in the corresponding property. The following table lists all the properties the LabWindows/CVI Adapter updates and the value translation, if any, the adapter makes.

| Structure Member | Valid Values Tests Can Return | Step.Result Property | Step Property Value |
| --- | --- | --- | --- |
| result | PASS or FAIL | PassFail | True/False |
| outBuffer | string value | ReportText | string value |
| measurement | floating-point value | Numeric | numeric value |
| stringMeasurement | string value | String | string value |
| errorFlag | True or False | Error.Occurred | True/False |
| errorCode | integer value | Error.Code | numeric value |
| errorMessage | string value | Error.Msg | string value |

Note

tTestData

tTestData

tTestData

Step.Result.PassFail

tTestData

Step.Result.ReportText

Parent topic:

Calling Legacy LabWindows/CVI Code Modules

Related concepts:

- Example Legacy LabWindows/CVI Code Module

Related information:

- tTestData Structure
- tTestError Structure

<!--NI_TOPIC bundle=teststand path=updating-the-status-bar-cvil.html language=enus -->
## TOPIC 00946: Updating the Status Bar Using UI Messages - LabWindows/CVI

- bundle_id: `teststand`
- source_path: `updating-the-status-bar-cvil.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/updating-the-status-bar-cvil.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Purpose This example demonstrates how to use LabWindows/CVI to show step execution progress and status in the TestStand Sequence Editor or Execution window. Example File Location <TestStand Public>\Examples\Modifying User Interfaces\Updating the Status Bar Using UI Messages\CVI\Updating the Status B

### Updating the Status Bar Using UI Messages - LabWindows/CVI

#### Purpose

This example demonstrates how to use LabWindows/CVI to show step execution progress and status in the TestStand Sequence Editor or Execution window.

#### Example File
 Location

<TestStand
 Public>\Examples\Modifying User Interfaces\Updating the Status Bar
 Using UI Messages\CVI\Updating the Status Bar Using UI
 Messages.seq

#### Highlighted Features

- LabWindows/CVI Adapter
- Execution

#### Major API

- SequenceContext
- Thread
- Thread.PostUIMessage
- UIMessageCodes Enumeration

#### Prerequisites

None

#### How to Use This Example

Complete the following steps to use this example.

1. Open the DisplayingProgressAndStatus.c source file, located in the <TestStand Public>\Examples\Modifying User Interfaces\Updating the Status Bar Using UI Messages\CVI directory. The source file specifies the following functionality:
  - Lines 29 and 46 —The tsErrChkMsgPopup function uses TS_ThreadPostUIMessage to post a ProgressPercent user interface (UI) message that updates the progress bar the sequence displays in TestStand with the percent complete.
  - Lines 33 and 43 —The tsErrChkMsgPopup function uses TS_ThreadPostUIMessage to post a ProgressText UI message to update the progress text on the status bar with the percent finished.
2. Close the source file. Do not save any changes.
3. In TestStand, select Execute»Single Pass to run the sequence. Review the progress bar and progress status field on the status bar of the sequence editor.

Parent topic:

Updating the Status Bar Using UI Messages

Related concepts:

- TestStand Directory Structure
- Programming with the TestStand API in LabWindows/CVI
- Executions

<!--NI_TOPIC bundle=teststand path=updating-the-status-bar-labview.html language=enus -->
## TOPIC 00947: Updating the Status Bar Using UI Messages - LabVIEW

- bundle_id: `teststand`
- source_path: `updating-the-status-bar-labview.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/updating-the-status-bar-labview.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Purpose This example demonstrates how to use LabVIEW to show step execution progress and status in the TestStand Sequence Editor or Execution window. Example File Location <TestStand Public>\Examples\Modifying User Interfaces\Updating the Status Bar Using UI Messages\LabVIEW\Updating the Status Bar

### Updating the Status Bar Using UI Messages - LabVIEW

#### Purpose

This example demonstrates how to use LabVIEW to show step execution progress and status in the TestStand Sequence Editor or Execution window.

#### Example File
 Location

<TestStand
 Public>\Examples\Modifying User Interfaces\Updating the Status Bar
 Using UI Messages\LabVIEW\Updating the Status Bar Using UI
 Messages.seq

#### Highlighted Features

- LabVIEW Adapter
- Execution

#### Major API

- SequenceContext
- Thread
- Thread.PostUIMessage
- UIMessageCodes Enumeration

#### Prerequisites

You must have the LabVIEW development system installed and you must configure the LabVIEW Adapter to use the LabVIEW development system.

#### How to Use This Example

Complete the following steps to use this example.

1. On the Steps pane, select the Call Long Test step, which is an Action step that uses the LabVIEW Adapter.
2. On the Step Settings pane, click the LabVIEW Module tab.
3. Click the Edit VI button, located to the right of the VI Path control, to open in LabVIEW the VI the Call Long Test step calls.
4. In LabVIEW, switch to the block diagram and select Help»Show Context Help to display the Context Help window for the block diagram. The block diagram specifies the following functionality for the VI:
  - The Sequence Context property node obtains a reference to the Thread object and initializes the termination monitor.
  - The execution enters the Stacked Sequence Structure and executes frame 0. Select frame 0 of the Stacked Sequence Structure. The Start Time is stored in the sequence local variable.
  - Select frame 1 of the Stacked Sequence Structure. The Get Monitor Termination Status VI stops the VI if you terminate or abort the execution. If you do not terminate or abort the execution, the False case of the case structure executes.
  - The VI invokes the Thread.PostUIMessage method and posts a ProgressPercent user interface (UI) message that updates the progress bar the sequence displays in TestStand with the percent complete.
  - The VI posts a ProgressText UI message to update the progress text on the status bar with the percent finished. This behavior continues in the While loop until the time limit expires or you terminate or abort the execution. If the time limit expires, the execution continues to frame 2 of the Stacked Sequence Structure.
  - Select frame 2. In the False case of the case structure, the progress bar updates to 100 percent and the progress text updates to Test Finished.
  - The Thread object reference the terminator monitor close.
5. Close the VI. Do not save any changes.
6. In TestStand, select Execute»Single Pass to run the sequence. Review the progress bar and progress status field on the status bar of the sequence editor.

Parent topic:

Updating the Status Bar Using UI Messages

Related concepts:

- TestStand Directory Structure
- Programming with the TestStand API in LabVIEW
- Executions

<!--NI_TOPIC bundle=teststand path=updating-the-status-bar-net.html language=enus -->
## TOPIC 00948: Updating the Status Bar Using UI Messages - .NET

- bundle_id: `teststand`
- source_path: `updating-the-status-bar-net.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/updating-the-status-bar-net.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Purpose This example demonstrates how to show step execution progress and status in the TestStand Sequence Editor or Execution window. Example File Location <TestStand Public>\Examples\Modifying User Interfaces\Updating the Status Bar Using UI Messages\DotNET\Updating the Status Bar Using UI Message

### Updating the Status Bar Using UI Messages - .NET

#### Purpose

This example demonstrates how to show step execution progress and status in the TestStand Sequence Editor or Execution window.

#### Example File
 Location

<TestStand
 Public>\Examples\Modifying User Interfaces\Updating the Status Bar
 Using UI Messages\DotNET\Updating the Status Bar Using UI
 Messages.seq

#### Highlighted Features

- Execution
- .NET Adapter

#### Major API

- SequenceContext
- Thread
- Thread.PostUIMessage
- UIMessageCodes Enumeration

#### Prerequisites

None

#### How to Use This Example

In TestStand, select Execute»Single Pass to run the sequence. Review the progress bar and progress status field on the status bar of the sequence editor.

Parent topic:

Updating the Status Bar Using UI Messages

Related concepts:

- TestStand Directory Structure
- Executions

<!--NI_TOPIC bundle=teststand path=updating-the-status-bar-using-ui-messages-mfc.html language=enus -->
## TOPIC 00949: Updating the Status Bar Using UI Messages - MFC

- bundle_id: `teststand`
- source_path: `updating-the-status-bar-using-ui-messages-mfc.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/updating-the-status-bar-using-ui-messages-mfc.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Purpose This example demonstrates how to use C++ to show step execution progress and status in the TestStand Sequence Editor or Execution window. Example File Location <TestStand Public>\Examples\Modifying User Interfaces\Updating the Status Bar Using UI Messages\MFC\Updating the Status Bar Using UI

### Updating the Status Bar Using UI Messages - MFC

#### Purpose

This example demonstrates how to use C++ to show step execution progress and status in the TestStand Sequence Editor or Execution window.

#### Example File
 Location

<TestStand
 Public>\Examples\Modifying User Interfaces\Updating the Status Bar
 Using UI Messages\MFC\Updating the Status Bar Using UI
 Messages.seq

#### Highlighted Features

- C/C++ DLL Adapter
- Execution

#### Major API

None

#### Prerequisites

None

#### How to Use This Example

AppWizard creates DisplayingProgressAndStatus.dll, which demonstrates the basics of using the Microsoft Foundation Class (MFC) Library and serves as a starting point for writing a custom DLL.

The following files, located in the <TestStand Public>\Examples\Modifying User Interfaces\Updating the Status Bar Using UI Messages\MFC directory, make up DisplayingProgressAndStatus.dll:

- DisplayingProgressAndStatus.h —The main header file that declares the CDisplayingProgressAndStatusApp class for the DLL.
- DisplayingProgressAndStatus.cpp —The main DLL source file that contains the CDisplayingProgressAndStatusApp class.
- DisplayingProgressAndStatus.rc —A list of all the Microsoft Windows resources the program uses, including icons, bitmaps, and cursors stored in the res subdirectory. You can directly edit this file in Microsoft Developer Studio.
- res\DisplayingProgressAndStatus.rc2 —Contains resources Developer Studio does not edit. Place all resources the resource editor cannot edit in this file.
- DisplayingProgressAndStatus.def —Contains DLL information that must be provided to run with Windows. This file defines parameters such as the name and description of the DLL and exports functions from the DLL.
- DisplayingProgressAndStatus.clw —Contains information ClassWizard uses to edit existing classes, add new classes, and store information required to create and edit message maps and dialog data maps and to create prototype member functions.

Other standard files located in the <TestStand Public>\Examples\Modifying User Interfaces\Updating the Status Bar Using UI Messages\MFC directory include the following:

- StdAfx.h and StdAfx.cpp —Used to build a precompiled header (PCH) file named DisplayingProgressAndStatus.pch and a precompiled types file named StdAfx.obj .
- Resource.h —The standard header file that defines new resource IDs. Developer Studio reads and updates this file.

Note

TODO:

Parent topic:

Updating the Status Bar Using UI Messages

Related concepts:

- TestStand Directory Structure
- Organizing Test Program Files with LabVIEW-Built Shared Libraries
- Executions

<!--NI_TOPIC bundle=teststand path=updating-the-status-bar-using-ui-messages.html language=enus -->
## TOPIC 00950: Updating the Status Bar Using UI Messages

- bundle_id: `teststand`
- source_path: `updating-the-status-bar-using-ui-messages.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/updating-the-status-bar-using-ui-messages.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The <TestStand Public>\Examples\Modifying User Interfaces\Updating the Status Bar Using UI Messages directory contains the following examples.

### Updating the Status Bar Using UI Messages

The <TestStand
 Public>\Examples\Modifying User Interfaces\Updating the Status Bar
 Using UI Messages directory contains the following examples.

- [Updating the Status Bar Using UI Messages - LabWindows/CVI](updating-the-status-bar-cvil.html)
- [Updating the Status Bar Using UI Messages - LabVIEW](updating-the-status-bar-labview.html)
- [Updating the Status Bar Using UI Messages - MFC](updating-the-status-bar-using-ui-messages-mfc.html)
- [Updating the Status Bar Using UI Messages - .NET](updating-the-status-bar-net.html)

Parent topic:

Examples for Modifying User Interfaces

Related concepts:

- TestStand Directory Structure

<!--NI_TOPIC bundle=teststand path=updating-values-sle-file.html language=enus -->
## TOPIC 00951: Updating Values from an SLE Server in TestStand

- bundle_id: `teststand`
- source_path: `updating-values-sle-file.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/updating-values-sle-file.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `task`
- source_description: If product specifications imported from your SLE server or specification file change, you can update your imported specifications and any steps they impact from within TestStand. To update specifications in TestStand with new values from an SLE server or specification file: Retrieve the latest data

### Updating Values from an SLE Server in
 TestStand

If product specifications imported from your SLE server or specification file change, you
 can update your imported specifications and any steps they impact from within
 TestStand.

To update specifications in TestStand with new values from an SLE server or
 specification file:

1. Retrieve the latest data from your SLE server or specification file by clicking
 Check for Updates in the
 Specifications pane. 
 [IMAGE alt='image' src='GUID-219AE38E-1037-44F3-BD10-0ECBB62C7D03-a5.png']
 Note The Check for Updates button
 is only usable if there are differences between the currently loaded
 specifications and the specifications in the linked SLE server or
 specification file.
2. Open the View Differences dialog box by clicking the
 View Changes button.
3. Preview the differences between your current and new data in the View
 Differences dialog box. 
 [IMAGE alt='image' src='GUID-54547A53-2EE4-44AD-9F8F-C31DE75948F9-a5.png']
4. Save the updated values in the active sequence file by clicking
 OK.

Parent topic:

Importing Specifications into TestStand Using the Specifications Pane

Related concepts:

- SLE Attributes, Conditions, and Specifications

<!--NI_TOPIC bundle=teststand path=updating-vi-dependencies.html language=enus -->
## TOPIC 00952: Updating VI Dependencies

- bundle_id: `teststand`
- source_path: `updating-vi-dependencies.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/updating-vi-dependencies.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: To improve performance, the LabVIEW Adapter stores information about VIs it loads. However, if a dependency of a VI is deleted or modified in a way that breaks the main VI, the LabVIEW Module tab does not reflect these changes. You can get the latest information for a VI whose dependencies have chan

### Updating VI Dependencies

To improve performance, the LabVIEW Adapter stores information about VIs it loads.
 However, if a dependency of a VI is deleted or modified in a way that breaks the main VI,
 the LabVIEW Module tab does not reflect these changes. You can get the latest information
 for a VI whose dependencies have changed by unloading all modules.

When a dependency of a VI is modified, unload all modules using one of the following methods:

- In the TestStand Sequence Editor, type <Ctrl+Shift+U> .
- Using the TestStand Engine API, call the Engine.UnloadAllModules method.

Note

Parent topic:

LabVIEW Adapter

Related information:

- LabVIEW Adapter Configuration Dialog Box
- Engine.UnloadAllModules Method

<!--NI_TOPIC bundle=teststand path=upgrade-codes-that-affect-msi-based-installer.html language=enus -->
## TOPIC 00953: Upgrade Codes That Affect MSI-based Installer Behavior

- bundle_id: `teststand`
- source_path: `upgrade-codes-that-affect-msi-based-installer.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/upgrade-codes-that-affect-msi-based-installer.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: MSI-based Installer upgrade codes uniquely identify MSI-based installers. MSI-based Installers that use the same upgrade code are assumed to install the same set of files or product, such as two different versions of the same test system. MSI-based Installers with different upgrade codes are conside

### Upgrade Codes That Affect MSI-based Installer Behavior

MSI-based Installer upgrade codes uniquely identify MSI-based installers. MSI-based Installers that use the same upgrade code are assumed to install the same set of files or product, such as two different versions of the same test system. MSI-based Installers with different upgrade codes are considered independent and can be installed on one computer at the same time.

MSI-based Installers with the same upgrade code use the installer version to determine what action to perform, as shown in the following table.

| Version of New MSI-based Installer | Version of MSI-based Installer on Computer | Action MSI-based Installer Performs |
| --- | --- | --- |
| Later | Earlier | Installs and upgrades the previous version of the MSI-based installer on the computer |
| Earlier | Later | Does not install |

#### MSI-based Installers with Different Upgrade Codes That Install the Same File

Do not include shared files that install to the same path in MSI-based installers that use different upgrade codes because using one of the MSI-based installers to uninstall files removes the shared file, which can negatively affect an installed test system.

To manage shared files correctly with Microsoft Windows Installer technology, the Component ID (GUID) must be the same in each MSI-based installer that shares the file so the MSI Engine can correctly increment the reference count for the shared file and not uninstall the shared file until you uninstall all installers that require the shared file. When multiple installers include shared files with different component IDs, one uninstaller can remove the file from the test station computer, regardless of how many other existing installed test systems on the test station computer require the file. When you use the TestStand Deployment Utility to build MSI-based installers from a single TestStand deployment specification file (.tsd), the MSI-based installers use the same stored component ID for shared files when the destination paths of the files do not change.

If you are using LabVIEW, you can use packed project libraries to work around this issue because for packed project libraries, the MSI-based installer you build with the deployment utility specifies the msidbComponentAttributesSharedDllRefCount attribute, which uses an alternate reference counting mechanism that uses the installation path instead of the component ID. Therefore, MSI-based installers you build with the deployment utility that install a packed project library to the same path increment the same reference count for the file. The packed project libraries uninstall only after you uninstall all MSI-based installers that reference the files.

Parent topic:

Building a Customized MSI-based Installer

Related concepts:

- Choosing Single or Multiple Deployments
- Relationship of NI MSI-based Installer Architecture and Microsoft Windows Installer Technology
- Organizing Test Program Files with LabVIEW Packed Project Libraries

<!--NI_TOPIC bundle=teststand path=use-case-generate-different-types-of-reports.html language=enus -->
## TOPIC 00954: Use Case: Generate Different Types of Reports from the Same Data Set

- bundle_id: `teststand`
- source_path: `use-case-generate-different-types-of-reports.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/use-case-generate-different-types-of-reports.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Scenario Consider a test system in which the report generation functionality must meet the following criteria: Maximize test system throughput Generate and display a summary report immediately after testing the unit under test (UUT) Generate a detailed report a Manufacturing Execution System (MES) c

### Use Case: Generate Different Types of Reports from the Same Data Set

#### Scenario

Consider a test system in which the report generation functionality must meet the following criteria:

- Maximize test system throughput
- Generate and display a summary report immediately after testing the unit under test (UUT)
- Generate a detailed report a Manufacturing Execution System (MES) can post-process

#### Solution

Create one results processing configuration to generate a high-level summary report and different configurations for more detailed reports.

#### Detailed Solution

For the
 summary report, create a result processing configuration that specifies the
 following options in the Report Options dialog box:

| Report Option | Value |
| --- | --- |
| Format | ASCII |
| Asynchronous | False |
| On-the-Fly Report | False |
| Only Display Latest Results | False |

For a more detailed report, create a result processing configuration that
 specifies the following options in the Report Options dialog box:

| Report Option | Value |
| --- | --- |
| Format | ATML |
| Asynchronous | True |
| On-the-Fly Report | False |
| Only Display Latest Results | False |

In some cases, the Manufacturing Execution System (MES) might not
 post-process the detailed report at the time the MES tests the UUT but instead at a
 later time or on a different computer. In this case, create a result processing
 configuration that specifies the following options in the Report Options dialog box
 so you can generate a TSR file and post-process results using the TestStand Offline
 Result Processing Utility, which can generate an ATML report the MES can
 post-process:

| Report Option | Value |
| --- | --- |
| Format | TSR |
| Asynchronous | True |
| On-the-Fly Report | False |
| Only Display Latest Results | False |

Parent topic:

Choosing the Appropriate Report Generation Strategy

Related concepts:

- Process Model Plug-In Architecture
- Choosing the Appropriate Report Generation Strategy
- Use Case: Log Data at One Location but Generate the Report at a Separate Location

<!--NI_TOPIC bundle=teststand path=use-case-log-data-at-one-location-but-generat.html language=enus -->
## TOPIC 00955: Use Case: Log Data at One Location but Generate the Report at a Separate Location

- bundle_id: `teststand`
- source_path: `use-case-log-data-at-one-location-but-generat.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/use-case-log-data-at-one-location-but-generat.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Scenario Consider a test system that runs production tests off-site at a contract manufacturer facility. The report generation functionality must meet the following criteria: Support post-failure information recovery to help diagnose and isolate faults Store the report for each unit under test (UUT)

### Use Case: Log Data at One Location but Generate the Report at a Separate Location

#### Scenario

Consider a test system that runs production tests off-site at a contract manufacturer facility. The report generation functionality must meet the following criteria:

- Support post-failure information recovery to help diagnose and isolate faults
- Store the report for each unit under test (UUT) for traceability or analysis

#### Solution

Generate a compact raw results file at the off-site test system location, transfer the TSR file on-site, and generate the final report using the TestStand Offline Result Processing Utility.

#### Detailed Solution

Create a
 result processing configuration that specifies the following options in the Report
 Options dialog box:

| Report Option | Value |
| --- | --- |
| Format | TSR |
| Asynchronous | True |
| On-the-Fly Report | True |
| Only Display Latest Results | True |

Parent topic:

Choosing the Appropriate Report Generation Strategy

Related concepts:

- Process Model Plug-In Architecture
- Use Case: Generate Different Types of Reports from the Same Data Set

<!--NI_TOPIC bundle=teststand path=use-specs-sle-sm.html language=enus -->
## TOPIC 00956: Using Imported Specifications in TestStand

- bundle_id: `teststand`
- source_path: `use-specs-sle-sm.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/use-specs-sle-sm.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `task`
- source_description: Once you map the parameters of specifications you import, you can use them to create steps in your sequence file. Navigate to the specification you want to map parameters for in the Specifications pane and click Select Measurement. Use the Measurement drop-down list to select the appropriate measure

### Using Imported Specifications in
 TestStand

Once you map the parameters of specifications you import, you can use them to create
 steps in your sequence file.

1. Navigate to the specification you want to map parameters for in the
 Specifications pane and click Select
 Measurement. 
 [IMAGE alt='image' src='GUID-E04231ED-358F-4A78-B922-10EB05750B79-a5.png']
2. Use the Measurement drop-down list to select the
 appropriate measurement plug-in or code module for your measurement. 
 [IMAGE alt='image' src='GUID-A6219C0A-F1F3-4089-8724-E753E66D0394-a5.png']
 Note If you do not have an appropriate code module, you
 can create a VI or Python code module by clicking Create
 new... in the Measurement drop-down
 list.
3. If you are mapping parameters for a measurement plug-in, map your conditions
 and specifications to parameters using the corresponding drop-down lists for
 each condition and specification.
4. If you are mapping parameters for a VI code module, complete the following
 steps.
  1. If you select a LabVIEW project for your measurement, select the VI you
 want to map parameters for using the Select VI
 drop-down list. 
 Note If you select a VI directly for your
 measurement, you do not need to use the Select
 VI drop-down list.Note You can only create new VI code modules through the drop-down list
 if you configured the LabVIEW adapter to use the LabVIEW Development
 Environment.
  2. Map your conditions and specifications to parameters using the
 corresponding drop-down lists for each condition and
 specification.
5. If you are mapping parameters for a Python code module, complete the following
 steps.
  1. Select the function you want to map parameters for using the
 Select Function drop-down list. 
 Note You can only create or load Python code
 modules if the Python adapter is configured.
  2. Map your conditions and specifications to parameters using the
 corresponding drop-down lists for each condition and
 specification.
6. Once you have mapped your parameters, click Back, select
 your mapped specification from the list in the
 Specifications pane, and click Insert
 Step to create a step at the end of
 MainSequence your sequence file for obtaining the selected
 specification. 
 Note If you do not create a step using Insert
 Step and your imported specifications, TestStand will not
 save your imported specifications and parameter mappings.

Parent topic:

Importing Specifications into TestStand Using the Specifications Pane

<!--NI_TOPIC bundle=teststand path=user-components.html language=enus -->
## TOPIC 00957: User Components

- bundle_id: `teststand`
- source_path: `user-components.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/user-components.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can create custom components or modify installed TestStand components to change TestStand behavior on a development computer. You must include the custom components in a deployment for the test station computers to use the same modified TestStand behavior. For example, if you use a custom locali

### User Components

You can create custom components or modify installed TestStand components to change TestStand behavior on a development computer. You must include the custom components in a deployment for the test station computers to use the same modified TestStand behavior. For example, if you use a custom localized string resource file for a user interface on a development computer, you must include that file in the deployment for use on the test station computer.

The following <TestStand>\Components subdirectories contain files you might want to copy to a corresponding <TestStand Public> directory, customize, and include in a deployment:

- Analyzer
- Callbacks
- Icons
- Language
- Models
- StepTypes
- Tools
- TypePalettes

Parent topic:

Customizing Components You Deploy

Related concepts:

- Creating String Resource Files
- Components Directory
- Copying Read-Only Files to Modify

<!--NI_TOPIC bundle=teststand path=user-defined-events.html language=enus -->
## TOPIC 00958: User-Defined Events

- bundle_id: `teststand`
- source_path: `user-defined-events.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/user-defined-events.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can post a custom message in a user-defined event by using an event number greater than or equal to the value of the UIMsg_UserMessageBase constant.

### User-Defined Events

You can post a custom message in a user-defined event by using an event number greater than or equal to the value of the UIMsg_UserMessageBase constant.

Parent topic:

Handling Specific User Interface Messages

Related concepts:

- Posting User Interface Messages

<!--NI_TOPIC bundle=teststand path=user-interface-application-styles.html language=enus -->
## TOPIC 00959: User Interface Application Styles

- bundle_id: `teststand`
- source_path: `user-interface-application-styles.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/user-interface-application-styles.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Although you can use the TestStand User Interface (UI) Controls to create any type of application, the following formats are the most common: Single window Multiple window No visible window Applications of a particular style usually share a similar implementation strategy, particularly with respect

### User Interface Application Styles

Although you can use the TestStand User Interface (UI) Controls to create any type of application, the following formats are the most common:

- Single window
- Multiple window
- No visible window

Applications of a particular style usually share a similar implementation strategy, particularly with respect to the use of the TestStand manager controls.

Parent topic:

User Interface Development Best Practices

Related concepts:

- TestStand UI Controls
- Single Window Applications
- Multiple Window Applications
- No Visible Window Applications
- Manager Controls

<!--NI_TOPIC bundle=teststand path=user-interface-development-best-practices.html language=enus -->
## TOPIC 00960: User Interface Development Best Practices

- bundle_id: `teststand`
- source_path: `user-interface-development-best-practices.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/user-interface-development-best-practices.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Learn the best practices for developing user interfaces.

### User Interface Development Best
 Practices

Learn the best practices for developing user interfaces.

- [Localizing User Interfaces](localizing-user-interfaces.html)
- [Documenting Custom User Interfaces](documenting-custom-user-interfaces.html)
- [User Interface Application Styles](user-interface-application-styles.html)
- [Persisting Application Settings](persisting-application-settings.html)
- [Deploying a User Interface](deploying-a-user-interface.html)

Parent topic:

Creating Custom User Interfaces

<!--NI_TOPIC bundle=teststand path=user-interface-messages-uimessages.html language=enus -->
## TOPIC 00961: User Interface Messages (UIMessages)

- bundle_id: `teststand`
- source_path: `user-interface-messages-uimessages.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/user-interface-messages-uimessages.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: When you write an application that runs TestStand sequence files, you do not handle the details of executing each step. Instead, you call the TestStand Engine to begin executing the sequence file in a new thread. The engine notifies you asynchronously of the state of the execution by sending you mes

### User Interface Messages (UIMessages)

When you write an application that runs TestStand sequence files, you do not handle the details of executing each step. Instead, you call the TestStand Engine to begin executing the sequence file in a new thread. The engine notifies you asynchronously of the state of the execution by sending you messages such as Start, End, Break, and Trace. You can update the application user interface in response to these messages.

You can create an execution directly or indirectly. For example, you create an execution indirectly when you load a sequence file that has a load callback. Before you create an execution directly or indirectly, you must create a user interface message handler. The TestStand Engine uses user interface messages to communicate the execution states and other asynchronous information to the application.

Parent topic:

Writing an Application with the TestStand Engine API

<!--NI_TOPIC bundle=teststand path=user-manual-welcome.html language=enus -->
## TOPIC 00962: TestStand User Manual

- bundle_id: `teststand`
- source_path: `user-manual-welcome.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/user-manual-welcome.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The TestStand User Manual provides detailed descriptions of the product functionality and the step by step processes for use. Looking for Something Else?For information not found in the User Manual for your product, such as specifications and API reference, browse Related Information.

### TestStand
 User Manual

The TestStand User Manual provides detailed
 descriptions of the product functionality and the step by step processes for use.

#### Looking for Something Else?

For information not found in the User Manual
 for your product, such as specifications and API reference, browse *Related
 Information*.

Related concepts:

- Activating and Licensing TestStand

Related tasks:

- Installing TestStand

Related information:

- TestStand Release Notes - Known Issues, Bug Fixes, and
 More
- TestStand API Reference
- Software and Driver Downloads
- Release Notes
- Interactive Activation Guide
- Product Certifications
- Discussion Forums
- NI Learning Center

<!--NI_TOPIC bundle=teststand path=using-a-dedicated-build-computer.html language=enus -->
## TOPIC 00963: Using a Dedicated Build Computer

- bundle_id: `teststand`
- source_path: `using-a-dedicated-build-computer.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/using-a-dedicated-build-computer.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Identifying problems in a deployment as soon as possible can help avoid errors on test station computers. Testing the deployment image on the development computer you use to create the deployment is helpful because the development computer includes the required tools to fix the issue and rebuild the

### Using a Dedicated Build Computer

Identifying problems in a deployment as soon as possible can help avoid errors on test station computers. Testing the deployment image on the development computer you use to create the deployment is helpful because the development computer includes the required tools to fix the issue and rebuild the deployment. You can also use a dedicated build computer on which you only create deployments and avoid any development tasks.

Using the same computer to develop and deploy a test system presents the following disadvantages:

- The deployment might include files in an incomplete state. A common development practice of having multiple versions of a file to test different approaches can result in including one of these files in the deployment by mistake.
- Files that were not submitted to the source code control (SCC) system do not produce errors during deployment because the files exist on the development computer. Additionally, adding new developers or moving to a new development computer might result in lost work.
- The deployment might include files that reference dependencies using absolute paths. If these dependencies are installed to a different path, errors may occur on a deployed system. These errors will not occur on the development system since the dependencies exist at the absolute path.

Using a dedicated build computer offers the following advantages:

- Files synchronized using an SCC system on the build computer can ensure that the files are in the correct state.
- The build process can report as an error files not submitted to the SCC system.
- You can automate the build process to run without negatively affecting developer productivity.

#### Virtual Machine or Image

If you do not have a separate computer available to dedicate to building deployments, you can use a virtual machine or a disk image the same way you use a dedicated build computer.

Parent topic:

Creating Deployments

<!--NI_TOPIC bundle=teststand path=using-a-directory-to-create-a-deployment.html language=enus -->
## TOPIC 00964: Using a Directory to Create a Deployment

- bundle_id: `teststand`
- source_path: `using-a-directory-to-create-a-deployment.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/using-a-directory-to-create-a-deployment.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can create a deployment that contains all the files in a directory. Enable the From Directory option in the Deploy Files section on the System Source tab of the deployment utility and browse to or enter the path to the directory you want to use. Enable the Include Subdirectories option to includ

### Using a Directory to Create a Deployment

You can create a deployment that contains all the files in a directory. Enable the From Directory option in the Deploy Files section on the System Source tab of the deployment utility and browse to or enter the path to the directory you want to use. Enable the Include Subdirectories option to include all files in the subdirectories of the directory you select. The deployment utility automatically includes file dependencies located outside the directory you select.

Note

<TestStand Public>

Parent topic:

Creating Deployments

Related concepts:

- Deploying the TestStand Runtime
- Including Files from the TestStand Public Directory in a Deployment

<!--NI_TOPIC bundle=teststand path=using-a-network-drive-to-deploy-test-systems.html language=enus -->
## TOPIC 00965: Using a Network Drive to Deploy Test Systems

- bundle_id: `teststand`
- source_path: `using-a-network-drive-to-deploy-test-systems.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/using-a-network-drive-to-deploy-test-systems.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can store user interfaces, sequence files, code modules, and other TestStand components on a network drive and configure test station computers to use that network drive. You can use the deployment utility to create a deployable image that you store on the network drive. Using a network drive to

### Using a Network Drive to Deploy Test Systems

You can store user interfaces, sequence files, code modules, and other TestStand components on a network drive and configure test station computers to use that network drive. You can use the deployment utility to create a deployable image that you store on the network drive. Using a network drive to update a test system updates all test station computers that use the network drive.

Consider the following issues before you decide to use a network drive to deploy or update a test system:

- Network access —Developers and test station computers require access to the network drive. If you cannot grant access to the network drive, you can use mirroring techniques to replicate and synchronize the network drive for the required access.
- Network availability —Design a fault-tolerant update process that effectively manages network outages or other situations in which a network drive is unavailable. Network outages can stop production unless the test system can execute successfully without access to the network drive. For example, you can use a temporary directory on the test station computer to store the files you want to update and then transfer those updates to the test system directory at an appropriate time.
- Location of files —If the configuration of all test station computers remain identical, you can deploy and update files from the same network directory. However, test station computers might need variations based on hardware requirements, product revisions, and configuration requirements. Some test station computers might require different sequences, code modules, and driver versions to support different hardware and UUT requirements. You can use directories on the network drive to deploy or update specific versions of the test system based on hardware or UUT requirements. Test station computers also might require different configuration settings for local debugging tasks or for unique reporting requirements. You can use a network drive to distribute code modules, user interfaces, and TestStand components and use locally unique configuration files on each test station computer. Note If you use local configuration files but modify configuration files such as GeneralEngine.cfg, Adapters.cfg, and SearchDirectories.cfg that affect all test station computers, you must edit the local copy of the configuration file on each test station computer. You can design the update process to determine which files on the test station computer to update from the network drive or use update settings files on the test station computers for greater flexibility.
- Timing of changes —Ensure that the update process prevents race conditions that might occur if you do not control when test station computers access files on the network drive.
- Security —Ensure that the network location is secure and that changes cannot be inadvertently made to the files in the test system. Because all test stations share the files, modifying the files in one location could lead to race conditions and invalidate testing.
- Number of inbound connections —Consult the Microsoft Software License Terms to determine the maximum number of computers that can connect to a network drive at the same time.

#### Advantages

Using a network drive offers the following advantages:

- For small updates, you can copy to the network drive only the files that require changes.
- Updating the contents of a network drive updates all the test station computers that use the network drive, which scales well if you use a large number of test station computers. Consult the Microsoft Software License Terms to determine the maximum number of computers that can connect to a network drive at the same time.
- You can create a deployment without having specific knowledge of Microsoft Windows Installer technology.

#### Disadvantages

Using a network drive presents the following disadvantages:

- Designing an update process that manages network outages and avoids race conditions requires additional development time.
- The test station computer site requires a network infrastructure of required hardware and IT resources for maintenance.
- Copying files to a test station computer is not sufficient for the test system to function
 correctly because you must also run installers on the test station computer to
 correctly install the TestStand Runtime, NI components, and required third-party
 components.
- You must be familiar with Microsoft Windows security issues associated with accessing and executing files from shared drive locations.
- Network drives do not keep a history of file changes. When you use the deployment utility to create a deployable image, you can save the generated deployment log to record the list of files included on the network drive.

#### Using a Network Drive to Deploy Patches

You can use the deployment utility to create a patch deployable image that contains all files modified since the previous full or patch deployment and replace the files on the network drive with the files in the patch deployable image folder.

Note

Parent topic:

Network-Based Deployment Mechanisms

Related concepts:

- Network-Based Deployment Mechanisms
- Relationship of NI MSI-based Installer Architecture and Microsoft Windows Installer Technology
- Patching Deployments

<!--NI_TOPIC bundle=teststand path=using-a-source-code-control-system-to-deploy.html language=enus -->
## TOPIC 00966: Using a Source Code Control System to Deploy Test Systems

- bundle_id: `teststand`
- source_path: `using-a-source-code-control-system-to-deploy.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/using-a-source-code-control-system-to-deploy.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Source code control (SCC) systems use a database to store multiple versions of files and can prevent changes from accidentally overwriting other changes. An SCC client application provides a way for users to retrieve files from or submit files to the database. You can also use the SCC client applica

### Using a Source Code Control System to Deploy Test Systems

Source code control (SCC) systems use a database to store multiple versions of files and can prevent changes from accidentally overwriting other changes. An SCC client application provides a way for users to retrieve files from or submit files to the database. You can also use the SCC client application to synchronize a set of files to retrieve the most recent versions of the files or to retrieve previous versions of the files.

In a typical SCC test system deployment architecture, you use the deployment utility to create a deployable image and submit the generated and modified files to the database on the SCC server, and test station computers retrieve the files from the SCC server. You can submit changes at any time without affecting the test system because test station computers do not receive the changes until requested. Because SCC systems use local copies of the files on test station computers, the test system can continue operation during a network outage. However, because network outages can affect SCC-based deployment mechanisms during an update, you can synchronize files to a temporary directory on the test station computer to avoid a partial update of the test system.

Additionally, you must determine when test station computers synchronize to the updated files on the SCC server. For example, a user interface can ensure that the test system has not loaded any sequences and then synchronize files at startup or before loading sequence files to automatically retrieve the most recent versions of the files.

When you use an SCC system to deploy test systems, confirm that you understand the conditions under which the SCC system overwrites files. For example, an SCC system might not automatically overwrite writeable files or files that are checked out by another user. In this case, you might need to revert the changes and force-synchronize writeable files before you update the files to include changes you make.

Note

Included

File Status

You can use the following techniques with an SCC-based deployment mechanism:

- Configure the SCC system to retrieve only the files you modified since the last time you retrieved files on the test station computer, which can increase performance over slower networks.
- Use branching features of the SCC system to concurrently develop multiple versions of a single test system because you can merge changes to large numbers of files between branches. For example, you can use a legacy system branch for bug fixes only and another branch for development tasks.
- Use separate branches for developing test systems and for storing validated test systems you deployed to test station computers, which can be helpful for separating the development and validation processes but can complicate the update process.

#### Advantages

Using an SCC system offers the following advantages:

- Deployment and update tasks scale well if you use a large number of test station computers because each test station computer can retrieve the most recently modified files from a central location.
- Test station computers use local copies of files from the SCC server to ensure test system operation during network outages.
- Submitting modified files does not affect executing test systems because test station computers receive changes only when requested.
- You can synchronize to previous versions of a test system if required.
- You can install files in TestStand directories, such as the <TestStand Application Data> \Cfg directory, the <TestStand Public> directory, and the <TestStand> directory.
- You can create a deployment without having specific knowledge of Microsoft Windows Installer technology.
- You can efficiently perform small updates to the deployment. The size of the files changed determines the size of the update, which does not require a large, fixed, overhead size.

#### Disadvantages

Using an SCC system presents the following disadvantages:

- Designing an update process that manages network outages and avoids race conditions requires additional development time. However, using an SCC system to develop an update process typically is more straightforward than developing an update process based on a network drive.
- The test station computer site requires a network infrastructure of required hardware, IT resources for maintenance, and SCC administration resources.
- Copying files to a test station computer is not sufficient for the test system to function
 correctly because you must also run installers on the test station computer to
 correctly install the SCC client application, the TestStand Runtime, NI
 components, and required third-party components.
- Because the source control system stores a copy of all the versions of all the files in the test system, the disk space the source control server uses could become very large.

#### Using a Source Control System to Deploy Patches

You can use the deployment utility to create a patch deployable image that contains all files modified since the previous full or patch deployment and add the files in the patch deployable image to the source control server, replacing existing files if required. The test station computers can synchronize with the source control server to retrieve the patched version of the deployment.

Note

Parent topic:

Network-Based Deployment Mechanisms

Related concepts:

- Network-Based Deployment Mechanisms
- TestStand Directory Structure
- Relationship of NI MSI-based Installer Architecture and Microsoft Windows Installer Technology
- Patching Deployments

<!--NI_TOPIC bundle=teststand path=using-a-teststand-number-with-representation.html language=enus -->
## TOPIC 00967: Using a TestStand Number with Representation Based on Bitness to Represent Pointer-Sized Numbers in Sequences in 32-bit TestStand and 64-bit TestStand

- bundle_id: `teststand`
- source_path: `using-a-teststand-number-with-representation.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/using-a-teststand-number-with-representation.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use bitness-conditional code to change the representation of a number based on the bitness of TestStand. For example, if Locals.NumVal must be a pointer-sized number, use the following expression to set the representation appropriately based on the bitness of TestStand: Locals.NumVal.Type.Representa

### Using a TestStand Number with Representation Based on Bitness to Represent Pointer-Sized Numbers in Sequences in 32-bit TestStand and 64-bit TestStand

Use bitness-conditional code to change the representation of a number based on the bitness of TestStand. For example, if Locals.NumVal must be a pointer-sized number, use the following expression to set the representation appropriately based on the bitness of TestStand:

Locals.NumVal.Type.Representation = RunState.Engine.Is64Bit ? PropertyRepresentation_Int64 : PropertyRepresentation_Float64

Parent topic:

Representing Pointer-Sized Numbers in Sequences in 32-bit TestStand and 64-bit TestStand

Related concepts:

- Bitness-Conditional Code for 32-bit TestStand or 64-bit TestStand

<!--NI_TOPIC bundle=teststand path=using-a-teststand-workspace-file-to-create-a.html language=enus -->
## TOPIC 00968: Using a TestStand Workspace File to Create a Deployment

- bundle_id: `teststand`
- source_path: `using-a-teststand-workspace-file-to-create-a.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/using-a-teststand-workspace-file-to-create-a.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use the TestStand Deployment Utility to create a deployment that contains all the files you specify in a workspace file. Using workspaces and projects as the source for deployments offers the following advantages: Workspaces can contain files from multiple paths, which is more flexible than

### Using a TestStand Workspace File to Create a Deployment

You can use the TestStand Deployment Utility to create a deployment that contains all the files you specify in a workspace file.

Using workspaces and projects as the source for deployments offers the following advantages:

- Workspaces can contain files from multiple paths, which is more flexible than creating a deployment from a single root directory in the following ways:
  - You can map a directory in a workspace to a directory on the hard drive
  - You can add files from multiple directories to a single workspace directory
  - You can include only specific files from a directory on the hard drive in a workspace directory
- Workspaces contain references to files, not the files themselves. Therefore, deleting files from a workspace does not delete the files from disk.
- You can use projects as reusable, modular components that multiple workspaces can share. Defining projects by functionality can also help you easily add or remove features to or from a deployment by adding or removing the specific project to or from the workspace. For example, you can create a user interface project that includes all the files for the user interface you want to deploy.

Enable the From TestStand Workspace File option in the Deploy Files section on the System Source tab of the TestStand Deployment Utility and browse to or enter the path to the workspace file you want to use. When you add new files to the workspace, the deployment utility includes the new files the next time you create the deployment.

Note

<TestStand Public>

#### Creating a Workspace File for Deployment

Complete the following steps to create a workspace file.

1. Create a list of files to add to the workspace by identifying the components and required files for the test system.
2. Select File»New»Workspace File to create a workspace file. You must add one or more TestStand project files to the workspace.
3. Add individual files or all the files in a directory to the project file.

#### Avoid Inserting Code Modules in a
 Workspace You Use for Deployment

If you are using a workspace only to
 create a deployment, NI does not recommend inserting code modules that sequence
 files use in the workspace for the following reasons:

- Before creating a deployment, the deployment utility analyzes all the files in
 the workspace and includes the files that test sequences statically reference,
 including code modules.
- The list of code modules you insert in the workspace is a static list and does
 not automatically refresh when the sequence file changes. Therefore, you might
 deploy files that the test system no longer requires.

Note

Parent topic:

Creating Deployments

Related concepts:

- Workspaces
- Using a Directory to Create a Deployment
- Distributing Tests from a Workspace
- Deploying the TestStand Runtime
- Including Files from the TestStand Public Directory in a Deployment
- Identifying Components to Deploy
- Adding Dynamically Called Files to a Workspace
- Getting Started with TestStand

<!--NI_TOPIC bundle=teststand path=using-activex-drivers-in-labwindows-cvi.html language=enus -->
## TOPIC 00969: Using ActiveX Drivers in LabWindows/CVI

- bundle_id: `teststand`
- source_path: `using-activex-drivers-in-labwindows-cvi.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/using-activex-drivers-in-labwindows-cvi.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: LabWindows/CVI creates and accesses ActiveX objects using functions in a LabWindows/CVI-generated driver. This driver uses function panels to define C functions for all the methods and properties available for each object. For servers that define events, the driver contains functions for registering

### Using ActiveX Drivers in LabWindows/CVI

LabWindows/CVI creates and accesses ActiveX objects using functions in a LabWindows/CVI-generated driver. This driver uses function panels to define C functions for all the methods and properties available for each object. For servers that define events, the driver contains functions for registering callback sequences for events.

The driver functions you use to invoke methods and properties have the following special naming conventions:

- Function names start with a prefix, such as TS_ .
- Methods are followed by the class name and the method name.
- Properties are followed by Get or Set and the property name.
- In some cases, the class, method, and property names are abbreviated to keep the function name within the constraints of the .fp file format.

The LabWindows/CVI ActiveX Automation Library uses the CAObjHandle data type for handles to ActiveX objects. The TestStand ActiveX drivers also follow this convention, so you can use the CAObjHandle data type for all handles to TestStand objects. However, one drawback of using the same data type for all TestStand objects is that the compiler cannot flag calls to methods in which you pass a handle for the wrong kind of object.

Objects can support more than one interface. For example, a SequenceContext object has a SequenceContext interface and a PropertyObject interface. When using handles in LabWindows/CVI to invoke methods or access properties of an object, you do not have to convert a specific reference for one interface to a specific reference for another interface. The ActiveX driver always queries the handle for the proper interface before invoking the method or accessing the property.

When you receive an object handle as the result of calling a method or obtaining the handle from a property, you must release the handle when you are finished with it.

Some TestStand ActiveX API methods include output parameters that return strings. You must use the CA_FreeMemory function in the LabWindows/CVI ActiveX Automation Library to free these strings when you are done with them.

Parent topic:

Programming with the TestStand API in LabWindows/CVI

Related concepts:

- Adding and Releasing References in LabWindows/CVI

<!--NI_TOPIC bundle=teststand path=using-alias-names-in-property-loader.html language=enus -->
## TOPIC 00970: Using Alias Names in Property Loader

- bundle_id: `teststand`
- source_path: `using-alias-names-in-property-loader.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/using-alias-names-in-property-loader.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Using Alias Names in Property Loader Alias names are alternate names used to represent a property in the property loader source. You need not use property lookup in the property loader source if you use alias names and, therefore, you can create a property loader source that does not contain any Tes

### Using Alias Names in Property Loader

#### Using Alias Names in Property Loader

Alias names are alternate names used to represent a property in the property loader source.
You need not use property lookup in the property loader source if you use alias names and,
therefore, you can create a property loader source that does not contain any TestStand-specific
terminology (i.e. Locals, FileGlobals, etc).

If your property loader source is a file, the mapping between alias names and property lookup
should exist in a file with extension .pla. If your property loader source is a database, the
mapping between alias names and property lookup should exist in a table in the database. You
can provide the filepath or table name to specify where the mapping between alias names and
property lookup exists.

When exporting with the Import/Export Properties tool, you can use the property selector to
specify alias names for the property.

#### Alias Name Restrictions

Alias names cannot contain the following characters:

. < > [ ] { } ' "

#### Storing Alias Names in a File

Mapping between alias names and property lookup must be stored in a file with
extension .pla. Review the example file located at <TestStandPublic>\Examples
\Built-In Step Types\Property Loader Step Type\AliasNames.pla to see
how alias names are stored in a file.

#### Storing Alias Names in a Database

Use a database table to store alias names and property lookup mappings. The Alias table
schema contains the following columns:

ALIAS_NAME — Contains the name of the alias. This is the primary column for the table.
Use the following data types for each database:

- Access – VARCHAR(255)
- MySQL – VARCHAR(255)
- SQLServer – VARCHAR(255)
- Sybase – VARCHAR(255)
- Oracle – VARCHAR2(255)

PROPERTY_LOOKUP — Contains the property lookup mapped to the specified alias name.
Use the following data types for each database:

- Access – LONGTEXT
- MySQL – VARCHAR(8000)
- SQLServer – VARCHAR(8000)
- Sybase – VARCHAR(32767)
- Oracle – VARCHAR2(4000)

Note

Parent topic:

Using the Property Loader Step Type

<!--NI_TOPIC bundle=teststand path=using-an-object-reference-to-represent-pointe.html language=enus -->
## TOPIC 00971: Using an Object Reference to Represent Pointer-Sized Numbers in Sequences in 32-bit TestStand and 64-bit TestStand

- bundle_id: `teststand`
- source_path: `using-an-object-reference-to-represent-pointe.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/using-an-object-reference-to-represent-pointe.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: If TestStand obtains a pointer-sized number from a code module and only holds or passes the value but does not mathematically manipulate the value, use a TestStand Object Reference to store the number. Using this approach avoids the need for bitness-conditional code, but you cannot access and operat

### Using an Object Reference to Represent Pointer-Sized Numbers in Sequences in 32-bit TestStand and 64-bit TestStand

If TestStand obtains a pointer-sized number from a code module and only holds or passes the value but does not mathematically manipulate the value, use a TestStand Object Reference to store the number. Using this approach avoids the need for bitness-conditional code, but you cannot access and operate on the underlying numeric value within TestStand.

Parent topic:

Representing Pointer-Sized Numbers in Sequences in 32-bit TestStand and 64-bit TestStand

Related concepts:

- Representing Pointers in Sequences in 32-bit TestStand and 64-bit TestStand

<!--NI_TOPIC bundle=teststand path=using-callback-sequences-to-modify-process-mo.html language=enus -->
## TOPIC 00972: Using Callback Sequences to Modify Process Models

- bundle_id: `teststand`
- source_path: `using-callback-sequences-to-modify-process-mo.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/using-callback-sequences-to-modify-process-mo.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Model callbacks are sequences entry point sequences call and client sequence files can override. Use Model callbacks to customize the behavior of a process model for each client sequence file that uses the process model. By defining one or more Model callbacks in a process model file, you specify th

### Using Callback Sequences to Modify Process Models

Model callbacks are sequences entry point sequences call and client sequence files can override. Use Model callbacks to customize the behavior of a process model for each client sequence file that uses the process model. By defining one or more Model callbacks in a process model file, you specify the set of process model operations you can customize from a client sequence file.

Complete the following steps to define a Model callback.

1. Add a sequence to the process model file.
2. Select Edit»Sequence Properties to launch the Sequence Properties dialog box.
3. Click the Model tab.
4. Select Callback from the Type ring control.
5. Click OK .
6. Call the new sequence you just created from the process model.

You can override a callback in the process model sequence file by using the Sequence File Callbacks dialog box to create a sequence with the same name but different functionality in the client sequence file. Select Edit»Sequence File Callbacks to launch the Sequence File Callbacks dialog box.

Some Model callbacks, such as the TestReport callback in the default process model, are sufficient for handling specific types of operations. Other Model callbacks are placeholders you override with sequences in the client sequence file. For example, the MainSequence callback in the default process model file is a placeholder for the MainSequence callback you create in the client sequence file.

A primary process model file can directly call model callbacks in a secondary process model file. At run time, if the client sequence file of the primary file implements a callback defined in the secondary process model file, TestStand invokes the callback in the client sequence file, even if the primary process model file does not define the callback. You must add a copy of the callback to the primary model file for the callback to appear in the Sequence File Callbacks dialog box for the client sequence file.

Note

StationCallbacks.seq

StationCallbacks.seq

StationCallbacks.seq

Parent topic:

Modifying Process Model Sequence Files

Related concepts:

- Model Callbacks in the Batch Process Model
- TestStand Directory Structure

<!--NI_TOPIC bundle=teststand path=using-callback-sequences.html language=enus -->
## TOPIC 00973: Using Callback Sequences

- bundle_id: `teststand`
- source_path: `using-callback-sequences.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/using-callback-sequences.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Callbacks are sequences TestStand calls under specific circumstances. You can create new callbacks or you can override existing callbacks to customize the operation of the test station. Completed solution files are located in the <TestStand Public>\Tutorial\Solution directory. Process Model Callback

### Using Callback Sequences

Callbacks are sequences TestStand calls under specific circumstances. You can create new callbacks or you can override existing callbacks to customize the operation of the test station.

Note

<TestStand Public>\Tutorial\Solution

#### Process Model Callbacks

The process models contain sequences that define the operations TestStand performs before and after testing a UUT. You can use an Execution entry point, such as Test UUTs or Single Pass, to invoke sequences within a process model to execute a sequence in a sequence file you create. The process models also contain Model callbacks, which are sequences you can override to customize the behavior of a process model without editing the process model directly.

For example, the process models define a PreUUT callback sequence that prompts the user for a serial number before the test sequence executes. In most cases, this default behavior is sufficient. You can override the default PreUUT callback in a sequence file you create. When you override the default PreUUT callback and you use the Test UUTs or Single Pass Execution entry point to execute a sequence file, the process model calls the custom PreUUT callback in the sequence file instead of the default PreUUT callback in the process model.

The following figure shows the actions the default Sequential process model performs using callback sequences within the Test UUTs and Single Pass Execution entry points.

[IMAGE alt='image' src='GUID-4409553B-174B-4838-96CC-993662F3247B-a5.svg']

You can modify the process models or replace the models entirely to alter the behavior of the process models for all sequences.

Note

<TestStand>\Components\Models\TestStandModels

<TestStand Public>\Components\Models\TestStandModels

- You must rename the files after you modify them if you want to create a separate custom component. You must register any new or renamed ActiveX components.
- You do not have to rename the files after you modify them if you only want to modify the behavior of an existing component.
- If you do not rename the files and you use the files in a future version of TestStand, changes NI makes to the component might not be compatible with the modified version of the component.
- Storing new and customized files in the <TestStand Public> directory ensures that installations of the same version of TestStand do not overwrite the customizations and ensures that uninstalling TestStand does not remove the files you customize.

#### Viewing Process Model Callbacks

Complete the following steps to examine the Model callbacks in the Sequential process model, which is the default process model TestStand uses to execute sequences.

1. Open <TestStand>\Components\Models\TestStandModels\SequentialModel.seq .
2. On the Sequences pane, select Test UUTs , which is the Execution entry point TestStand executes when you select Execute»Test UUTs . The Main step group of the Test UUTs sequence calls several callback sequences, including the following:
  - PreUUTLoop callback
  - PreUUT callback
  - MainSequence callback
  - PostUUT callback
  - PostUUTLoop callback
3. Double-click the PreUUT Callback step, not the PreUUTLoop Callback step, to view the PreUUT callback sequence, which calls the DoPreUUT sequence.
4. On the Sequences pane, select the DoPreUUT sequence. If the DoPreUUT Properties dialog box launches, click OK to close it. The DoPreUUT sequence includes an IdentifyUUT step and a Set Serial Number step. Note If you double-click the Call DoPreUUT step on the Steps pane of the PreUUT Callback sequence to try to open the DoPreUUT sequence, TestStand returns an error that it cannot open the sequence because TestStand evaluates an expression at run time to determine the sequence file path.
5. Right-click the IdentifyUUT step and select Run Selected Steps from the context menu to launch the UUT Information dialog box, which is similar to the dialog box that launches when you execute a sequence using the Test UUTs Execution entry point. You can override the PreUUT callback with a custom callback to change the way TestStand obtains a UUT serial number, such as reading the serial number from a bar code instead.
6. Click OK in the UUT Information dialog box.
7. Close the Execution window.
8. On the Sequences pane, select the Test UUTs sequence.
9. Double-click the PreUUTLoop Callback step to open the PreUUTLoop callback sequence, which is empty because it is a placeholder. If you want to add steps that execute before the UUT loop, you can complete the steps in the section to override this callback.
10. Close SequentialModel.seq and decline any prompts to save the changes.

#### Overriding a Process Model
 Callback

You can customize the functionality of a process model without
 making changes to the model itself. When you override a callback, the process model
 invokes the callback you create in a sequence file instead of the default callback
 in the process model.

Complete the following steps to override the default
 PreUUTLoop callback sequence in the Sequential model by creating a PreUUTLoop
 callback sequence in a client sequence file. Use this technique when you want to
 perform a task only once before operating on multiple UUTs, such as initializing
 hardware.

1. Open <TestStand Public>\Tutorial\Computer4.seq , which you
 created in Using Variables and Properties.
2. Select File»Save <filename> As 
 and save the sequence file as Computer5.seq in the
 <TestStand Public>\Tutorial directory.
3. Select Edit»Sequence File Callbacks to launch the
 Sequence File Callbacks dialog box.
4. Enable the checkbox for the PreUUTLoop callback. Click
 OK to close the Sequence File Callbacks dialog box.
 The sequence editor creates a new empty callback sequence in the sequence file.
 Now, when you start an execution using an Execution entry point, TestStand calls
 the callback in the sequence file instead of the callback sequence in the
 Sequential process model file. The PreUUTLoop callback sequence becomes the
 selected sequence on the Sequences pane and opens in the Sequence File window.
5. Insert a Message Popup step in the Main step group of the PreUUTLoop callback
 sequence and rename the new step Pre UUT Loop Callback
 Message .
6. Enter the literal string "Now in the Pre UUT Loop Callback" in
 the Message Expression control.
7. Save the changes and select Execute»Test UUTs . TestStand
 launches the Pre UUT Loop Callback Message dialog box.
8. Click OK to close the Pre UUT Loop Callback Message
 dialog box. TestStand launches the UUT Information dialog box from the PreUUT
 callback sequence in the Sequential model. Enter a serial number and click
 OK .
9. Run through several iterations of the sequence. TestStand launched the Pre UUT
 Loop Callback Message dialog box only once at the very beginning of the
 execution because the PreUUTLoop callback executes before the loop, and the
 PreUUT callback executes within the loop.
10. Click Stop in the UUT Information dialog box.
11. Close all the windows in the sequence editor.

The Parallel and Batch process models include similar callbacks that you can
 override.

Parent topic:

Getting Started with TestStand

Related concepts:

- Using Variables and Properties

<!--NI_TOPIC bundle=teststand path=using-custom-commands-to-execute-third-party.html language=enus -->
## TOPIC 00974: Using Custom Commands to Execute Third-Party Installers

- bundle_id: `teststand`
- source_path: `using-custom-commands-to-execute-third-party.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/using-custom-commands-to-execute-third-party.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use the TestStand Deployment Utility with custom commands to build a single MSI-based installer that installs all the components of a test system, such as sequences, step types, code modules, support files, user interfaces, NI drivers, run-time engines, and third-party drivers. Use the Custo

### Using Custom Commands to Execute Third-Party Installers

You can use the TestStand Deployment Utility with custom commands to build a single MSI-based
 installer that installs all the components of a test system, such as sequences, step
 types, code modules, support files, user interfaces, NI drivers, run-time engines,
 and third-party drivers.

Use the Custom Commands dialog box to configure commands the MSI-based installer executes after all files have been installed, such as launching an installer you built with LabVIEW or LabWindows/CVI, a third-party installer, or an installer for a user interface.

Requiring users to sequentially run multiple installers for third-party or separate components of the test system forces users to wait for each installer to complete before running the next installer. This process can introduce errors if users do not run the installers in the correct order.

Use custom commands to accomplish the following tasks:

- Run a single installer to install the entire test system and any required third-party installers
- Serialize the execution of multiple installers in the order you configure in the deployment utility
- Request a reboot after all commands execute
- Display a progress window to aid in debugging installation issues
- Use macros in command-line arguments to pass TestStand-specific directories to a third-party installer. For example, the <TESTSTAND> macro corresponds to the <TestStand> directory for the version of TestStand you used to build the installer.

Parent topic:

Building a Customized MSI-based Installer

Related concepts:

- TestStand Directory Structure

<!--NI_TOPIC bundle=teststand path=using-data-step-type.html language=enus -->
## TOPIC 00975: Using the Data Streams Step Type

- bundle_id: `teststand`
- source_path: `using-data-step-type.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/using-data-step-type.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Refer to the following topics for information on using the Data Streams step type.

### Using the Data Streams Step Type

Refer to the following topics for information on using the Data Streams step
 type.

- [Attaching a CSV Output Stream to the Current Execution](attaching-a-csv-output-stream-to-the-current.html)
- [Reading from CSV Files with Data Streams Step Types](reading-from-csv-files-with-data-streams-step.html)
- [Writing to CSV Files with Data Streams Step Types](writing-to-csv-files-with-data-streams-step-t.html)

Parent topic:

Built-In Step Types

<!--NI_TOPIC bundle=teststand path=using-data-streams-labview.html language=enus -->
## TOPIC 00976: Using Data Streams - LabVIEW

- bundle_id: `teststand`
- source_path: `using-data-streams-labview.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/using-data-streams-labview.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Purpose This example uses data streams to read from a comma separated value (csv) file and to create a csv file. Example File Location <TestStand Public>\Examples\Fundamentals\Using Data Streams\LabVIEW\UsingDataStreams.seq Highlighted Features TestStand Data Streams Major API TestStand Data Streams

### Using Data Streams - LabVIEW

#### Purpose

This example uses data streams to read from a comma separated value (csv) file and to create a csv file.

#### Example File
 Location

<TestStand
 Public>\Examples\Fundamentals\Using Data
 Streams\LabVIEW\UsingDataStreams.seq

#### Highlighted Features

- TestStand Data Streams

#### Major API

- TestStand Data Streams API

#### Prerequisites

You must have the LabVIEW Development System installed to execute this example.

#### How to Use This Example

Complete the following steps to run the example:

1. Select Execute»Run MainSequence to execute the sequence.
2. View the resulting CSV in the Report tab.

Parent topic:

Using Data Streams

Related concepts:

- TestStand Directory Structure

<!--NI_TOPIC bundle=teststand path=using-data-streams-net.html language=enus -->
## TOPIC 00977: Using Data Streams - .NET

- bundle_id: `teststand`
- source_path: `using-data-streams-net.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/using-data-streams-net.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Purpose This example uses data streams to read from a comma separated value (csv) file and to create a csv file. Example File Location <TestStand Public>\Examples\Fundamentals\Enumerations\UsingDataStreams.seq Highlighted Features TestStand Data Streams Major API TestStand Data Streams API How to Us

### Using Data Streams - .NET

#### Purpose

This example uses data streams to read from a comma separated value (csv) file and to create a csv file.

#### Example File
 Location

<TestStand
 Public>\Examples\Fundamentals\Enumerations\UsingDataStreams.seq

#### Highlighted Features

- TestStand Data Streams

#### Major API

- TestStand Data Streams API

#### How to Use This Example

Complete the following steps to run the example:

1. Select Execute»Run MainSequence to execute the sequence.
2. View the resulting CSV in the Report tab.

Parent topic:

Using Data Streams

Related concepts:

- TestStand Directory Structure

<!--NI_TOPIC bundle=teststand path=using-data-streams.html language=enus -->
## TOPIC 00978: Using Data Streams

- bundle_id: `teststand`
- source_path: `using-data-streams.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/using-data-streams.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The <TestStand Public>\Examples\Fundamentals\Using Data Streams directory contains the following examples.

### Using Data Streams

The <TestStand
 Public>\Examples\Fundamentals\Using Data Streams
 directory contains the following examples.

- [Using Data Streams - LabVIEW](using-data-streams-labview.html)
- [Using Data Streams - .NET](using-data-streams-net.html)

Parent topic:

Examples for Fundamentals

Related concepts:

- TestStand Directory Structure

<!--NI_TOPIC bundle=teststand path=using-enumerations-in-teststand.html language=enus -->
## TOPIC 00979: Using Enumerations in TestStand

- bundle_id: `teststand`
- source_path: `using-enumerations-in-teststand.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/using-enumerations-in-teststand.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The TestStand enumeration data type provides several advantages over the traditional alternative of using a number to represent an enumerated data type, including range checking, type safety, and the ability to extract the enumerator name as a string. To provide complete backward compatibility, all

### Using Enumerations in TestStand

The TestStand enumeration data type provides several advantages over the traditional alternative of using a number to represent an enumerated data type, including range checking, type safety, and the ability to extract the enumerator name as a string. To provide complete backward compatibility, all TestStand adapters provide full support for passing numbers for enumeration parameters.

TestStand enumerations attempt to provide an experience that as closely as possible mimics
 the behavior of enumerated data types in common modern programming languages. You typically
 interact with enumerated data types using their enumerators at edit time, while operations
 are generally based on the underlying number at run timer. There are subtleties that arise
 from the fact that the distinction between edit time and run time in TestStand is not
 clear-cut. Refer to the TestStand Enumerations Reference Guide for a detailed explanation of
 the behavior of TestStand enumerations.

Parent topic:

Extending TestStand

Related concepts:

- TestStand Enumerations Reference Guide
- Getting Started Creating a TestStand Enumeration

<!--NI_TOPIC bundle=teststand path=using-enumerations-with-the-teststand-adapter.html language=enus -->
## TOPIC 00980: Using Enumerations with the TestStand Adapters

- bundle_id: `teststand`
- source_path: `using-enumerations-with-the-teststand-adapter.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/using-enumerations-with-the-teststand-adapter.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Sequence Call Adapter The type of variable passed for an enumeration parameter must exactly match the parameter type in the sequence being invoked. C/C++ DLL and LabWindows/CVI Adapters There are two ways to pass enumeration parameters to the C/C++ DLL and LabWindows/CVI adapters: Pass a number spec

### Using Enumerations with the TestStand Adapters

#### Sequence Call Adapter

The type of variable passed for an enumeration parameter must exactly match the parameter type in the sequence being invoked.

#### C/C++ DLL and LabWindows/CVI
 Adapters

There are two ways to pass enumeration parameters to the C/C++
 DLL and LabWindows/CVI adapters:

- Pass a number specifying the numeric value of the parameter.
- Pass a TestStand enumeration instance. (Requires TestStand 2016 or later.)

To pass a TestStand enumeration, choose Enumeration for
 the category of the parameter in the module panel. Then select a data type from the
 drop-down menu for the Enum Type control.

When specifying the expression for
 the parameter value, you can select an enumerator in thedrop-down menu, manually
 enter an enumerator constant, or specify an expression that evaluates to the
 required enumeration data type.

#### LabVIEW Adapter

You can
 create an Enum data type that maps to the LabVIEW enumerated parameter from an
 enumeration, ring control, or indicator by clicking on the Create/Update
 Custom Data Typebutton located in the Type column of the VI
 Parameter table next to any LabVIEW enumerated parameter or an enumerated array
 parameter.

This launches the Create/Update Custom Data Type from Enum Dialog
 Box, where you can create a custom Enum data type or update an existing Enum data
 type to match the LabVIEW parameter.

You can create an instance of the Enum
 data type and specify that variable in the Value column of the VI Parameter
 table.

When specifying string or Enum variables as the value of an enumerated
 parameter, the following table describes the behavior:

| TestStand Type | Variable Passed to a LabVIEW Input Parameter | Variable Receiving Data from a LabVIEW Output Parameter |
| --- | --- | --- |
| String | If the variable's value exactly matches any of the LabVIEW enumerated parameter's elements,the numeric value of the element is passed to LabVIEW. If there is no match, you will get a run-time error. Assigning a duplicate (more than one element with the same name) enumerator name will result in an error. | If the numeric value received from LabVIEW matches any of the enumerated parameter's elements, then the matching element's name is stored in the string. If the numeric value does not match any element, its string representation surrounded by angular brackets is stored. Assigning a duplicate enumerator value to the string variable will result in an error. |
| CustomEnum data type | The elements of a TestStand Enum data type should match the LabVIEW parameter's enumerated elements exactly (both name and value). Any mismatch will result in an error. If the type matches,then the numeric value of the selected enum element is passed to LabVIEW. | The elements of a TestStand Enum data type should match the LabVIEW parameter’s enumerated elements exactly(both name and value). Any mismatch will result in an error. If the TestStand Enum data type is Strict, then the numeric value received from LabVIEW must match one of the enumerator elements. If there is no match, you will get a run-time error. |

#### .NET Adapter

There are
 three ways to pass enumeration parameters to the .NET adapter:

- Pass a TestStand string specifying the enumerator.
- Pass a TestStand number specifying the numeric value of the parameter.
- Pass a TestStand enumeration instance. (Requires TestStand 2016 or later.)

If passing a TestStand enumeration for a .NET enumeration parameter, the
 definition of the TestStand enumeration type should match the definition in the .NET
 code module. Specifically, the TestStand enumeration should define the same set of
 enumerators with the same numeric values as the code module. In addition, the
 numeric representation must match with the same requirements that apply to TestStand
 numbers. The name of the type is not important.

At edit time, the module panel
 will indicate if the definition of the TestStand enumeration specified does not
 match the definition in the code module. At run time, limited type checking is
 performed:

- If enumerator information is present in an enumeration instance used as an input
 parameter, the enumerators used by the instance must exist in the code module.
 Furthermore, the numeric value must match the value from the code module. (For
 flags enumerations, only the combined value is checked.)
- For both input and output parameters, the numeric representation of the
 TestStand enumeration must be compatible with the definition in the code
 module.

Note

#### ActiveX/COM Adapter

There
 are two ways to pass enumeration parameters to the ActiveX/COM adapter:

- Pass a number specifying the numeric value of the parameter.
- Pass a TestStand enumeration instance. (Requires TestStand 2016 or later.)

If passing an enumeration for an ActiveX/COM enumeration parameter, the
 definitions of the TestStand enumeration type should match the definition in the
 type library for the code module. Specifically, the TestStand enumeration should
 define the same set of enumerators with the same numeric values as the code module.
 In addition, the numeric representation must be the default. The name of the type is
 not important.

At edit time, the module panel will indicate if the definition
 of the TestStand enumeration specified does not match the definition in the code
 module. At run time, limited type checking is performed:

- If enumerator information is present in an enumeration instance used as an input
 parameter, the enumerators used by the instance must exist in the code module.
 Furthermore, the numeric value must match the value from the code module. (For flags
 enumerations, only the combined value is checked.)
- For both input and output parameters, the numeric representation of the
 TestStand enumeration must be compatible with the definition in the code
 module.

Note

- Use the TestStand Sequence Analyzer to find enumeration type mismatch errors
 in COM/ActiveX adapter steps.
- Many ActiveX/COM APIs expose enumerations in their type libraries, but still
 specify the long data type in method prototypes that expect these
 enumeration parameters. To pass a TestStand enumeration to such a method,
 convert it to a number using the appropriate expression function: Float64(),
 Int64(), or UInt64().

Parent topic:

TestStand Enumerations Reference Guide

<!--NI_TOPIC bundle=teststand path=using-execution-entry-points.html language=enus -->
## TOPIC 00981: Using Execution Entry Points

- bundle_id: `teststand`
- source_path: `using-execution-entry-points.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/using-execution-entry-points.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use an Execution entry point to start an execution only when the MainSequence is the sequence open on the Steps pane. The Execute menu of the sequence editor includes a list of Execution entry points. Each Execution entry point in the menu represents a separate entry point sequence in the pr

### Using Execution Entry Points

You can use an Execution entry point to start an execution only when the MainSequence is the sequence open on the Steps pane. The Execute menu of the sequence editor includes a list of Execution entry points.

Each Execution entry point in the menu represents a separate entry point sequence in the process model that applies to the active sequence file. When you select an Execution entry point from the Execute menu, you actually run an entry point sequence in a process model file. The Execution entry point sequence invokes the Main sequence one time or multiple times.

Execution entry points in a process model provide different ways for the test station operator to invoke a Main sequence. Execution entry points handle common operations, such as unit under test (UUT) identification and report generation. For example, the default Sequential process model provides the Test UUTs and Single Pass Execution entry points. The Test UUTs Execution entry point initiates a loop that repeatedly identifies and tests UUTs. The Single Pass Execution entry point tests a single UUT without identifying it.

Parent topic:

Executing Sequences

Related concepts:

- Main Sequence and Client Sequence File
- Entry Point Sequences
- TestStand Process Models

<!--NI_TOPIC bundle=teststand path=using-instrument-sessions-in-a-development-en.html language=enus -->
## TOPIC 00982: Using Instrument Sessions in a Development Environment

- bundle_id: `teststand`
- source_path: `using-instrument-sessions-in-a-development-en.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/using-instrument-sessions-in-a-development-en.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use instrument sessions in the following ways: Use instrument sessions implicitly by using an ActiveX control, a TestStand step type, or another high-level component that uses instrument sessions to facilitate instrument communication. Call Session Manager to obtain an instrument API handle

### Using Instrument Sessions in a Development Environment

You can use instrument sessions in the following ways:

- Use instrument sessions implicitly by using an ActiveX control, a TestStand step type, or another high-level component that uses instrument sessions to facilitate instrument communication.
- Call Session Manager to obtain an instrument API handle you use in a code module.
- Directly call Session Manager to implement components or utilities that use more advanced Session Manager features, such as enumerating available session names or locking sessions.

You can use an instrument session in the following development environments:

- LabWindows/CVI
- LabVIEW
- Microsoft Visual C++ and Other C++ Environments
- TestStand

Parent topic:

Session Manager

Related concepts:

- LabWindows/CVI
- LabVIEW
- Microsoft Visual C++ and Other C++ Environments
- TestStand

<!--NI_TOPIC bundle=teststand path=using-legacy-database-schemas.html language=enus -->
## TOPIC 00983: Using Legacy Database Schemas

- bundle_id: `teststand`
- source_path: `using-legacy-database-schemas.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/using-legacy-database-schemas.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Configure TestStand to use a legacy database schema when logging results from executions to a database. Click Configure»Result Processing to launch the Result Processing dialog box. In the Database row, click the Options icon to launch the Database Options dialog box Select the Schemas tab, click Re

### Using Legacy Database Schemas

Configure TestStand to use a legacy database schema when logging results from executions to a database.

1. Click Configure»Result Processing to launch the Result Processing dialog box.
2. In the Database row, click the Options icon to launch the Database Options dialog box
3. Select the Schemas tab, click Reload NI Schemas , then select the legacy schema you want to use.

Parent topic:

Default TestStand Table Schemas

Related concepts:

- Updates to Default Database Schemas
- Default TestStand Table Schemas

<!--NI_TOPIC bundle=teststand path=using-multiple-labview-versions-in-a-test-sys.html language=enus -->
## TOPIC 00984: Using Multiple LabVIEW Versions in a Test System

- bundle_id: `teststand`
- source_path: `using-multiple-labview-versions-in-a-test-sys.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/using-multiple-labview-versions-in-a-test-sys.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: NI recommends using a single version of LabVIEW to compile all the VIs for a test system. However, some situations exist that might require a test system to use multiple versions of LabVIEW. For example, you might need to update a validated test system you created in one version of LabVIEW to add a

### Using Multiple LabVIEW Versions in a Test System

NI recommends using a single version of LabVIEW to compile all the VIs for a test system.
 However, some situations exist that might require a test system to use multiple
 versions of LabVIEW. For example, you might need to update a validated test system
 you created in one version of LabVIEW to add a test that requires a feature
 available only in a later version of LabVIEW. In this case, you do not need to
 update and revalidate the entire test system to use the later version of LabVIEW.

You can execute code modules in different versions of LabVIEW in the same test system by using the following techniques:

- If you use the LabVIEW development system to execute code module VIs, you can force TestStand to run specific VIs in a different version of LabVIEW by enabling the Always Run VI in LabVIEW Run-Time Engine option in the LabVIEW Advanced Settings window. When you enable this option, TestStand always runs the VI in the LabVIEW Run-Time Engine (RTE) version that matches the version of LabVIEW in which you last compiled the VI, regardless of the option you select in the Select or Type Which LabVIEW Server to Use section in the LabVIEW Adapter Configuration dialog box.
- If you use the LabVIEW RTE to execute code module VIs, select the Auto detect using VI version option from the Version ring control of the LabVIEW Run-Time Engine option in the Select or Type Which LabVIEW Server to Use section in the LabVIEW Adapter Configuration dialog box. When you enable this option, TestStand always runs the VI in the LabVIEW RTE version that matches the version of LabVIEW in which you last compiled the VI.

NI recommends that you organize VIs specific to a LabVIEW version in separate sequence files and
 store those sequence files and related code modules in a separate directory.

Notice

#### Deploying VIs that Require Multiple Versions of LabVIEW

To run VIs on a test station computer that includes only the LabVIEW RTE, you must include all the VI dependencies in the deployment. The TestStand Deployment Utility analyzes and processes the VIs you include in a deployment to ensure the deployment includes the dependencies. However, the deployment utility can use only a single version of LabVIEW to process the VIs.

To work around this issue, you can create a packed project library that includes all dependent files for the deployment. Alternatively, you can create a source distribution that includes all dependent files for the deployment and enable the Include without Processing Item or Dependencies option in the File Properties section on the Distributed Files tab of the deployment utility for every file created in the source distribution. When you enable this option, the deployment utility does not attempt to find any dependencies of the file during analysis. Therefore, you must manually include all the dependencies in the deployment.

Parent topic:

Preparing Source Components for Deployment

Related concepts:

- Organizing Test Program Files with LabVIEW Packed Project Libraries
- Manually Adding or Removing Files to or from Deployments
- Deploying Network-Published Shared Variables
- Deploying Stand-alone VIs
- Deploying VIs in LabVIEW Packed Project Libraries
- Deploying VIs in LabVIEW Projects

<!--NI_TOPIC bundle=teststand path=using-ni-datafinder-with-teststand.html language=enus -->
## TOPIC 00985: Using NI DataFinder with TestStand

- bundle_id: `teststand`
- source_path: `using-ni-datafinder-with-teststand.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/using-ni-datafinder-with-teststand.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Using NI DataFinder to index TestStand report files in directories to which TestStand writes report files can lead to report generation errors in TestStand because of file access contention issues. To avoid these issues, do not configure DataFinder to index such directories. Instead, copy completed

### Using NI DataFinder with TestStand

Using NI DataFinder to index TestStand report files in directories to which TestStand writes report files can lead to report generation errors in TestStand because of file access contention issues. To avoid these issues, do not configure DataFinder to index such directories. Instead, copy completed report files from the location to which TestStand generates the report files to another directory you have configured DataFinder to index.

For DataFinder 2011 or later and TestStand 2010 SP1 or later, DataFinder no longer indexes the <TestStand Public> directory by default. If TestStand 2010 SP1 is installed on the computer, DataFinder 2011 or later no longer index the <TestStand Public> directory of earlier versions of TestStand installed on the same computer.

If you must generate reports in a directory indexed by NI DataFinder, DataFinder 2012 SP1 introduced a delayed indexing feature which allows you to configure DataFinder to not index files until a specified amount of time has passed since the last modification of the file. This feature is enabled for My DataFinder 2012 SP1 or newer with a default delay of 20 seconds, and disabled for DataFinder Server Edition by default. Complete the following steps to customize the delayed indexing setting:

1. Navigate to the following location in the Windows registry: [HKEY_LOCAL_MACHINE\Software\National Instruments\Common\DataFinder\ConfigItems]
2. Set the DeferredIndexingEnabled key to 0000001 to enable delayed indexing, or 0000000 to disable it. This key is a DWORD value.
3. Set the DeferredIndexingTimeInSeconds key to the number of seconds you would like DataFinder to wait before indexing new files. This key is a DWORD value.

For versions of DataFinder earlier than 2011 and versions of TestStand earlier than 2010 SP1 installed on the computer, DataFinder indexes the <TestStand Public> directory by default. Avoid generating TestStand report files to the <TestStand Public> directory or configure DataFinder not to index the <TestStand Public> directory.

Parent topic:

Generating and Customizing TestStand Reports

<!--NI_TOPIC bundle=teststand path=using-prop-step-type.html language=enus -->
## TOPIC 00986: Using the Property Loader Step Type

- bundle_id: `teststand`
- source_path: `using-prop-step-type.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/using-prop-step-type.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Refer to the following topics for information on using the Property Loader step type.

### Using the Property Loader Step Type

Refer to the following topics for information on using the Property Loader step
 type.

- [Importing and Exporting with a Legacy Source](importing-and-exporting-with-a-legacy-source.html)
- [Importing Data to Non-Existing Properties](importing-data-to-non-existing-properties.html)
- [Validate and Verify Runtime Behavior of Import](validate-and-verify-runtime-behavior-of-impor.html)
- [Using Alias Names in Property Loader](using-alias-names-in-property-loader.html)
- [Property Loader Plugins - Database Table Schemas](property-loader-plugins-database-table-schema.html)
- [Property Loader Plugins - File Formats](property-loader-plugins-file-formats.html)

Parent topic:

Built-In Step Types

<!--NI_TOPIC bundle=teststand path=using-side-by-side-versions-of-the-labwindows.html language=enus -->
## TOPIC 00987: Using Side-by-Side Versions of the LabWindows/CVI Run-Time Engine with TestStand

- bundle_id: `teststand`
- source_path: `using-side-by-side-versions-of-the-labwindows.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/using-side-by-side-versions-of-the-labwindows.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Typically, the default LabWindows/CVI Run-Time Engine (RTE) is appropriate for most DLLs and applications you build in LabWindows/CVI to use with TestStand. However, on occasion, you might want to isolate a test system from upgrades or downgrades to the LabWindows/CVI RTE. With LabWindows/CVI 2012 o

### Using Side-by-Side Versions of the LabWindows/CVI Run-Time Engine with TestStand

Typically, the default LabWindows/CVI Run-Time Engine (RTE) is appropriate for most DLLs and applications you build in LabWindows/CVI to use with TestStand. However, on occasion, you might want to isolate a test system from upgrades or downgrades to the LabWindows/CVI RTE. With LabWindows/CVI 2012 or later you can isolate LabWindows/CVI applications and DLLs from upgrades or downgrades to the LabWindows/CVI RTE by binding an executable or DLL to a specific, side-by-side version of the LabWindows/CVI RTE. Refer to the Binding Executables and DLLs to Side-by-Side Run-Time Engines topic in the LabWindows/CVI Help for more information about binding executables and DLLs to a side-by-side version of the LabWindows/CVI RTE.

#### Calling DLLs that Use a Side-by-Side Version of the LabWindows/CVI RTE in TestStand

You can use the LabWindows/CVI Adapter and the C/C++ DLL Adapter in TestStand to load and call DLL code modules that use a side-by-side LabWindows/CVI RTE or the default LabWindows/CVI RTE within the same sequence file. However, TestStand does not support calling DLLs you create with tools other than LabWindows/CVI, such as Microsoft Visual Studio, to use a side-by-side LabWindows/CVI RTE.

Parent topic:

Calling DLLs from TestStand

Related concepts:

- Programming with the TestStand API in LabWindows/CVI
- Organizing Test Program Files with LabVIEW-Built Shared Libraries
- Binding a TestStand Custom User Interface to a Side-by-Side Version of the LabWindows/CVI RTE
- Choosing Between the Shared or Side-by-Side Version of the LabWindows/CVI Run-Time Engine
- Identifying Components to Deploy

<!--NI_TOPIC bundle=teststand path=using-standard-named-data-types.html language=enus -->
## TOPIC 00988: Using Standard Named Data Types

- bundle_id: `teststand`
- source_path: `using-standard-named-data-types.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/using-standard-named-data-types.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: TestStand defines a set of standard named data types, such as Error, CommonResults, Path, Expression, and NI_TDMSReference. The only standard named data types you can modify are the CommonResults and the NI_UserCustomPrivileges types.

### Using Standard Named Data Types

TestStand defines a set of standard named data types, such as Error, CommonResults, Path, Expression, and NI_TDMSReference. The only standard named data types you can modify are the CommonResults and the NI_UserCustomPrivileges types.

Parent topic:

Data Types

Related concepts:

- Error and CommonResults
- Path
- Expression
- NI_TDMSReference

<!--NI_TOPIC bundle=teststand path=using-substeps.html language=enus -->
## TOPIC 00989: Using Substeps

- bundle_id: `teststand`
- source_path: `using-substeps.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/using-substeps.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Substeps use substep code modules to define standard actions, other than calling the step code module, TestStand performs for all instances of the step type. Use the Substeps tab of the Step Type Properties dialog box to specify Pre-Step, Post-Step, Edit, and Custom substeps for the step type. After

### Using Substeps

Substeps use substep code modules to define standard actions, other than calling the step code module, TestStand performs for all instances of the step type. Use the Substeps tab of the Step Type Properties dialog box to specify Pre-Step, Post-Step, Edit, and Custom substeps for the step type.

After you add a substep to a step type, click the Specify Module button in the Substeps tab to configure the substep module call. For each step that uses the step type, TestStand calls the same substep modules with the same arguments. You cannot add or remove substeps or otherwise alter the substep module call the substep performs when you configure a step instance.

Although you can specify any number of substeps for a step type, the list of substeps is not a sequence, and substeps do not have preconditions, post actions, or other execution options. The order in which Pre- and Post-Step substeps execute is the only execution option you specify.

#### Pre-Step Substep

TestStand calls the Pre-Step substep before calling the step code module. For example, a Pre-Step substep might call a substep code module that retrieves measurement configuration parameters and stores those parameters in step properties the step code module uses.

#### Post-Step Substep

TestStand calls the Post-Step substep after calling the step code module. For example, a Post-Step substep might call a substep code module that compares the values the step code module stored in step properties against limit values the Edit substep stored in other step properties. You can have multiple Post-Step substeps that execute in order.

#### Edit Substep

TestStand calls an Edit substep when you select the substep menu item from the Steps pane context menu. On the Substeps tab, select the Edit substep and click the Rename button to specify the name of the substep menu item and the caption of the button on the Step Type Edit tab of the Step Setting pane. If the Edit substep modifies any step properties, increment the change count of the sequence file by calling the PropertyObjectFile.IncChangeCount method so an editing application can determine that the file changed and refresh itself.

The Edit substep typically calls a substep code module that launches a dialog box in which you can edit the values of the custom step properties. For example, an Edit substep might launch a dialog box in which you specify the high and low limits for a test. The Edit substep might then store the high and low limit values as step properties.

Dialog boxes the Edit substep launches must be modal. Refer to the <TestStand Public>\Examples\Fundamentals\Launching a Modal Dialog directory for LabVIEW and Microsoft Foundation Class (MFC) examples of modal dialog boxes.

Note

Note

#### Custom Substeps

With the exception of substeps named OnNewStep, TestStand does not call custom substeps. Use the TestStand API to invoke a custom substep from a code module or user interface. You can create a custom substep named OnNewStep for TestStand to call each time you create a new step of that type. For example, the built-in If step type uses an OnNewStep substep to insert a matching End step. The OnNewStep substep can cancel the insertion of the step by setting the Step.CancelCurrentExecution property to True.

The <TestStand>\Components\StepTypes directory includes source code for many of the substep modules the built-in step types use. To modify the installed step types or to create a new step type, copy the step type source code from the <TestStand>\Components\StepTypes directory to the <TestStand Public>\Components\StepTypes directory and make changes to the copy of the source code.

Parent topic:

Custom Step Types

Related concepts:

- TestStand Directory Structure
- Launching a Modal Dialog
- TestStand ActiveX API Overview
- Built-In Step Types
- Copying Read-Only Files to Modify

<!--NI_TOPIC bundle=teststand path=using-sweep-loops-labview.html language=enus -->
## TOPIC 00990: Using Sweep Loops - LabVIEW

- bundle_id: `teststand`
- source_path: `using-sweep-loops-labview.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/using-sweep-loops-labview.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Example File Location <TestStand Public>\Examples\Fundamentals\Using Sweep Loops\LabVIEW\Using Sweep Loops.seq Highlighted Features Sweep Loops Data Streams Major API TestStand Data Streams API Prerequisites LabVIEW development system 16.0 or later How to Use This Example Complete the following step

### Using Sweep Loops - LabVIEW

#### Example File
 Location

<TestStand
 Public>\Examples\Fundamentals\Using Sweep Loops\LabVIEW\Using
 Sweep Loops.seq

#### Highlighted Features

- Sweep Loops
- Data Streams

#### Major API

- TestStand Data Streams API

#### Prerequisites

LabVIEW development system 16.0 or later

#### How to Use This Example

Complete the following steps to run the example:

1. Select Execute»Run Mainsequence to execute the sequence.

Parent topic:

Using Sweep Loops

Related concepts:

- TestStand Directory Structure

<!--NI_TOPIC bundle=teststand path=using-sweep-loops-net.html language=enus -->
## TOPIC 00991: Using Sweep Loops - .NET

- bundle_id: `teststand`
- source_path: `using-sweep-loops-net.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/using-sweep-loops-net.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Example File Location <TestStand Public>\Examples\Fundamentals\Using Sweep Loops\dotNet\Using Sweep Loops.seq Highlighted Features Sweep Loops Data Streams Major API TestStand Data Streams API Prerequisites None How to Use This Example Complete the following steps to run the example: Select Execute»

### Using Sweep Loops - .NET

#### Example File
 Location

<TestStand
 Public>\Examples\Fundamentals\Using Sweep Loops\dotNet\Using Sweep
 Loops.seq

#### Highlighted Features

- Sweep Loops
- Data Streams

#### Major API

- TestStand Data Streams API

#### Prerequisites

None

#### How to Use This Example

Complete the following steps to run the example:

1. Select Execute»Run Mainsequence to execute the sequence.

Parent topic:

Using Sweep Loops

Related concepts:

- TestStand Directory Structure

<!--NI_TOPIC bundle=teststand path=using-sweep-loops.html language=enus -->
## TOPIC 00992: Using Sweep Loops

- bundle_id: `teststand`
- source_path: `using-sweep-loops.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/using-sweep-loops.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The <TestStand Public>\Examples\Fundamentals\Using Sweep Loops directory contains the following examples.

### Using Sweep Loops

The <TestStand
 Public>\Examples\Fundamentals\Using Sweep Loops directory
 contains the following examples.

- [Using Sweep Loops - LabVIEW](using-sweep-loops-labview.html)
- [Using Sweep Loops - .NET](using-sweep-loops-net.html)
- [Sweep Loop Strategies](sweep-loop-strategies.html)

Parent topic:

Examples for Fundamentals

Related concepts:

- TestStand Directory Structure

<!--NI_TOPIC bundle=teststand path=using-sync-step-type.html language=enus -->
## TOPIC 00993: Using the Synchronization Step Type

- bundle_id: `teststand`
- source_path: `using-sync-step-type.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/using-sync-step-type.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Refer to the following topics for information on using the Synchronization step type.

### Using the Synchronization Step Type

Refer to the following topics for information on using the Synchronization step
 type.

- [Setting Up TestStand for Accessing Synchronization Objects Remotely](setting-up-teststand-for-accessing-synchroniz.html)
- [Synchronized Sections](synchronized-sections.html)

Parent topic:

Built-In Step Types

<!--NI_TOPIC bundle=teststand path=using-teststand-enumerations-cvi.html language=enus -->
## TOPIC 00994: Using TestStand Enumerations - CVI

- bundle_id: `teststand`
- source_path: `using-teststand-enumerations-cvi.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/using-teststand-enumerations-cvi.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Purpose This example shows how to use TestStand enumerations with CVI code modules. Enumerations are defined as custom types and can be stored in the Sequence File or Type Palettes. Example File Location <TestStand Public>\Examples\Fundamentals\Using TestStand Enumerations\CVI\Using TestStand Enumer

### Using TestStand Enumerations - CVI

#### Purpose

This example shows how to use TestStand enumerations with CVI code modules. Enumerations are defined as custom types and can be stored in the Sequence File or Type Palettes.

#### Example File
 Location

<TestStand
 Public>\Examples\Fundamentals\Using TestStand
 Enumerations\CVI\Using TestStand Enumerations.seq

#### Highlighted Features

- Using Enumerations in TestStand
- Range Checking:Strict and Loose Enumerations
- Flags Enumerations and Bitwise OR Semantics
- Using Enumerations with the TestStand Adapters

#### Major API

- Val Function
- Str Function

#### Prerequisites

None

#### How to Use This Example

Complete the following steps to run the example:

1. Select Execute»Run MainSequence to execute the sequence.
2. As the example executes, follow the prompts and read the message popups for information about Enumerations, Strict Enumerations, and Flag Enumerations.

Complete the following steps to review the enumerations and steps in this example:

1. Open the Enum sequence from the Sequences pane. Select the Enum Behavior step and review the step settings and parameter values for the step. This code module allows the user to select a combination of RGB colors, which are then stored in the Locals.Color Local variable.
2. Select the Display Enum Value step and review the Message Expression. This expression uses the Str() and Val() functions to display the string and formatted numeric representations of an enum value.
3. Repeat steps 1 and 2 for the Strict Enum and Flag Enum sequences.
4. Open the Types Window (Ctrl + t) and select Enums.seq to view the three different enumeration definitions used in this example: Colors , Colors_Strict , and Colors_Flag . Choose Edit Enumerations to view details of each type.

Parent topic:

Using TestStand Enumerations

Related concepts:

- TestStand Directory Structure
- Using Enumerations in TestStand
- Range Checking: Strict and Loose Enumerations
- Flags Enumerations and Bitwise OR Semantics
- Using Enumerations with the TestStand Adapters

<!--NI_TOPIC bundle=teststand path=using-teststand-enumerations-labview.html language=enus -->
## TOPIC 00995: Using TestStand Enumerations - LabVIEW

- bundle_id: `teststand`
- source_path: `using-teststand-enumerations-labview.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/using-teststand-enumerations-labview.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Purpose This example shows how to use TestStand enumerations with LabVIEW code modules. Enumerations are defined as custom types and can be stored in the Sequence File or Type Palettes. Example File Location <TestStand Public>\Examples\Fundamentals\Using TestStand Enumerations\LabVIEW\Using TestStan

### Using TestStand Enumerations - LabVIEW

#### Purpose

This example shows how to use TestStand enumerations with LabVIEW code modules. Enumerations are defined as custom types and can be stored in the Sequence File or Type Palettes.

#### Example File
 Location

<TestStand
 Public>\Examples\Fundamentals\Using TestStand
 Enumerations\LabVIEW\Using TestStand Enumerations.seq

#### Highlighted Features

- Using Enumerations in TestStand
- Range Checking:Strict and Loose Enumerations
- Flags Enumerations and Bitwise OR Semantics
- Using Enumerations with the TestStand Adapters

#### Major API

- PropertyObject.GetPropertyObject
- SequenceFile.AsPropertyObjectFile
- SequenceFile.AsPropertyObject

#### Prerequisites

None

#### How to Use This Example

Complete the following steps to run the example:

1. Select Execute»Run MainSequence to execute the sequence.
2. As the example executes, follow the prompts and read the message popups for information about Enumerations.

Complete the following steps to review the enumerations and steps in this example:

1. Open the Enum sequence from the Sequences pane. Select the Enum Behavior step and review the step settings and parameter values for the step. This code module allows the user to select a combination of RGB colors, which are then stored in the Locals.Color Local variable.
2. Select the Display Enum Value step and review the Message Expression. This expression uses the Str() and Val() functions to display the string and formatted numeric representations of an enum value.
3. Repeat steps 1 and 2 for the Strict Enum and Flag Enum sequences.
4. Open the Types Window (Ctrl + t) and select Enums.seq to view the three different enumeration definitions used in this example: Colors , Colors_Strict , and Colors_Flag . Choose Edit Enumerations to view details of each type.

Parent topic:

Using TestStand Enumerations

Related concepts:

- TestStand Directory Structure
- Using Enumerations in TestStand
- Range Checking: Strict and Loose Enumerations
- Flags Enumerations and Bitwise OR Semantics
- Using Enumerations with the TestStand Adapters

<!--NI_TOPIC bundle=teststand path=using-teststand-enumerations-net.html language=enus -->
## TOPIC 00996: Using TestStand Enumerations - .NET

- bundle_id: `teststand`
- source_path: `using-teststand-enumerations-net.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/using-teststand-enumerations-net.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Purpose This example shows how to use TestStand enumerations with .NET code modules. Enumerations are defined as custom types and can be stored in the Sequence File or Type Palettes. Example File Location <TestStand Public>\Examples\Fundamentals\Using TestStand Enumerations\DotNet\Using TestStand En

### Using TestStand Enumerations - .NET

#### Purpose

This example shows how to use TestStand enumerations with .NET code modules. Enumerations are defined as custom types and can be stored in the Sequence File or Type Palettes.

#### Example File
 Location

<TestStand
 Public>\Examples\Fundamentals\Using TestStand
 Enumerations\DotNet\Using TestStand Enumerations.seq

#### Highlighted Features

- Using Enumerations in TestStand
- Range Checking:Strict and Loose Enumerations
- Flags Enumerations and Bitwise OR Semantics
- Using Enumerations with the TestStand Adapters

#### Major API

- Val Function
- Str Function

#### Prerequisites

None

#### How to Use This Example

Complete the following steps to run the example:

1. Select Execute»Run MainSequence to execute the sequence.
2. As the example executes, follow the prompts and read the message popups for information about Enumerations, Strict Enumerations, and Flag Enumerations.

Complete the following steps to review the enumerations and steps in this example:

1. Open the Enum sequence from the Sequences pane. Select the Enum Behavior step and review the step settings and parameter values for the step. This code module allows the user to select a combination of RGB colors, which are then stored in the Locals.Color Local variable.
2. Select the Display Enum Value step and review the Message Expression. This expression uses the Str() and Val() functions to display the string and formatted numeric representations of an enum value.
3. Repeat steps 1 and 2 for the Strict Enum and Flag Enum sequences.
4. Open the Types Window (Ctrl + t) and select Enums.seq to view the three different enumeration definitions used in this example: Colors , Colors_Strict , and Colors_Flag . Choose Edit Enumerations to view details of each type.

Parent topic:

Using TestStand Enumerations

Related concepts:

- TestStand Directory Structure
- Using Enumerations in TestStand
- Range Checking: Strict and Loose Enumerations
- Flags Enumerations and Bitwise OR Semantics
- Using Enumerations with the TestStand Adapters

<!--NI_TOPIC bundle=teststand path=using-teststand-enumerations.html language=enus -->
## TOPIC 00997: Using TestStand Enumerations

- bundle_id: `teststand`
- source_path: `using-teststand-enumerations.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/using-teststand-enumerations.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: The <TestStand Public>\Examples\Fundamentals\Using TestStand Enumerations directory contains the following examples.

### Using TestStand Enumerations

The <TestStand
 Public>\Examples\Fundamentals\Using TestStand
 Enumerations directory contains the following examples.

- [Using TestStand Enumerations - CVI](using-teststand-enumerations-cvi.html)
- [Using TestStand Enumerations - LabVIEW](using-teststand-enumerations-labview.html)
- [Using TestStand Enumerations - .NET](using-teststand-enumerations-net.html)

Parent topic:

Examples for Fundamentals

Related concepts:

- TestStand Directory Structure

<!--NI_TOPIC bundle=teststand path=using-teststand-on-smp-systems.html language=enus -->
## TOPIC 00998: Using TestStand on SMP Systems

- bundle_id: `teststand`
- source_path: `using-teststand-on-smp-systems.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/using-teststand-on-smp-systems.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: Symmetric multiprocessing (SMP) systems are computers that contain multiple CPUs, where a CPU can be a single core on a multi-core processor or a single-core processor on a multiprocessor computer. Microsoft Windows and other modern operating systems can take advantage of SMP systems to achieve incr

### Using TestStand on SMP Systems

Symmetric multiprocessing (SMP) systems are computers that contain multiple CPUs, where a CPU can be a single core on a multi-core processor or a single-core processor on a multiprocessor computer. Microsoft Windows and other modern operating systems can take advantage of SMP systems to achieve increased performance. SMP systems achieve better performance by executing multiple threads on multiple CPUs concurrently. Performance improvement can come through executing multiple processes concurrently as well as from executing multiple threads within a process concurrently. Generally, when an application is implemented with multiple threads, the operating system attempts to schedule each thread on a separate CPU when possible. In the best-case scenario, an SMP system can execute a multithreaded application n times faster than a non-SMP system, where n is the number of CPUs. An application that exhibits this best-case performance scaling is said to scale linearly with the number of CPUs.

An application scales linearly if the work done in the application is completely divided into an independent part for each CPU, with no data shared between the independent parts. If the parts have to interact with each other or access the same data, the performance increase can be substantially less than linear. In some cases, performance of an application can even be worse on an SMP system than on a non-SMP system. The performance degradation or lack of improvement on SMP systems is caused by a variety of factors. The most typical factors are data sharing, where both reads and writes occur to the same or nearby data in memory, and synchronization interdependencies, where threads must coordinate with each other for the application to execute correctly. The degree to which these factors impact performance is dependent on the particular CPU architecture in the SMP system. For example, on some quad-core CPUs the memory cache is shared among all of the cores while on others the cache is separate for each core. Such a difference can result in performance differences when the threads access a large amount of shared data.

#### General Strategies for Optimizing Performance on SMP Systems

The best way to optimize an application for an SMP system is to break up the application into as many independent, concurrent tasks as possible and run at least n of them at a time, in n separate threads, where n is the number of CPUs on the computer. The application should avoid sharing data among threads and avoid requiring synchronization among threads as much as possible. Unfortunately, it is often difficult or impossible to design application functionality in a way that does not require threads to share data and does not require thread synchronization.

Because the performance impact of sharing data and synchronization depends on the CPU architecture, you can benchmark the application on different computer systems to determine the computer architecture on which the application performs best. You can also optimize the application for a particular computer system. If parts of the application perform worse with multiple CPUs, you can tune the application performance for a particular computer system by limiting the CPUs which certain threads or processes use to a subset of the CPUs on the system. You can then benchmark to determine how such tuning affects performance.

#### Strategies for Optimizing TestStand Performance on SMP Systems

TestStand applications are often multithreaded. You can execute sequences in parallel by using a Sequence Call step to execute a sequence in a new thread or new execution. You can execute code modules in parallel by executing the sequences which contain them in parallel. You can also create threads in code modules using your programming environment.

TestStand sequences that execute in parallel threads, communicate with the engine, share data with other sequences, and synchronize with other sequences might not scale well on SMP systems. Additionally, code modules that sequences call might also perform operations that do not scale well on SMP systems. Therefore, your system might have better performance if you constrain some or all threads to a subset of CPUs. If the TestStand sequences spend significant time in code modules that are completely independent, the system may have the best performance by using all CPUs for such code modules while constraining the CPUs the rest of the system uses.

To allow you to tune your system to achieve the best performance, TestStand provides several features to control how the TestStand process and its threads utilize the CPUs on your computer. In the descriptions of the features below, the CPU affinity of a process refers to the set of CPUs on which the threads in the process may run. The CPU affinity of a thread refers to the subset of those CPUs on which a particular thread may run.

- Station Option: Default CPU Affinity for Threads —Determines the default CPU affinity for new threads of executions and for the user interface thread. The default is to allow all CPUs. This option is located on the Preferences tab of the Station Options dialog box.
- Sequence Call Step: CPU Affinity for New Thread or Execution —The CPU affinity of the new thread in the current execution or the initial thread in a new execution. By default the new thread uses the Default CPU Affinity for Threads station option. This setting allows you to specify that the new thread allows all CPUs, uses the CPU affinity of the calling sequence, or allows specific CPUs that you specify. This option is located on the Sequence Call Advanced Settings window.
- CPU Affinity Step—Enables you to get or set the CPU affinity of the process or the current execution thread. This step gives you low-level control over how your system utilizes CPUs. This step is located in the Advanced subgroup of the Synchronization group on the Insertion Palette or in the Insert Step submenu of the Steps pane context menu.

Note

0b

0b1010

-1

-1

You can use the CPU affinity features together to tune your test system to get the best performance on a particular computer. For example, if you have a quad core computer, you could set the Default CPU Affinity for Threads Station Option to 0b0011 to restrict the test system to use only the first two CPUs and benchmark to determine how the performance of the system is affected. If parts of the test system contain code modules that can be highly parallelized and that do a significant amount of work, you could then use the CPU Affinity settings of a Sequence Call step or a CPU Affinity step to set the execution threads to allow all CPUs for such parts of the system. You may try various CPU affinity configurations to determine what gives the test system the best performance on a particular computer. Since performance results depend on CPU architecture, the best tuning for one computer may be different from the best tuning on another computer.

Parent topic:

Executions

Related concepts:

- Configuring the CPU Affinity for LabVIEW Execution Threads
- Symmetric Multiprocessing in VIs Executed from TestStand

<!--NI_TOPIC bundle=teststand path=using-teststand-search-directories-to-locate.html language=enus -->
## TOPIC 00999: Using TestStand Search Directories to Locate the Correct Code Module in 32-bit TestStand and 64-bit TestStand

- bundle_id: `teststand`
- source_path: `using-teststand-search-directories-to-locate.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/using-teststand-search-directories-to-locate.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: By default, 32-bit TestStand and 64-bit TestStand do not share search directories. You can associate bitness-specific versions of a code module with a sequence or step type by placing the code module in a non-shared TestStand search directory, such as the <TestStand Public> directory. The TestStand

### Using TestStand Search Directories to Locate the Correct Code Module in 32-bit TestStand and 64-bit TestStand

By default, 32-bit TestStand and 64-bit TestStand do not share search directories. You can associate bitness-specific versions of a code module with a sequence or step type by placing the code module in a non-shared TestStand search directory, such as the <TestStand Public> directory. The TestStand <TestStand Public> directories use a (32-bit) or (64-bit) suffix to indicate the bitness of TestStand to which they belong. Search directories located under the <TestStand> installation directory, such as the <TestStand>\Components directory, are naturally separate because Microsoft Windows uses separate Program Files directories for 32-bit applications and 64-bit applications on 64-bit Windows, typically C:\Program Files (x86) for 32-bit applications and C:\Program Files for 64-bit applications.

When you migrate code modules installed in a non-shared search directory, such as the <TestStand Public> directory, from 32-bit TestStand to 64-bit TestStand, complete the following steps.

1. Create a 64-bit search directory structure that matches the existing 32-bit search directory structure.
2. Install the 64-bit compatible versions of each code module in the 64-bit directory in locations that match the 32-bit versions of the code module.

The existing 32-bit code modules and directory structure do not require changes. 32-bit TestStand finds the existing 32-bit code modules in the original locations.

Additionally, 32-bit TestStand and 64-bit TestStand cannot share platform-independent code
 modules, such as AnyCPU .NET DLLs, you reference in a non-shared search directory.
 You need two copies of the code module in this case to simultaneously support 32-bit
 TestStand and 64-bit TestStand. If you need to simultaneously support 32-bit
 TestStand and 64-bit TestStand, NI recommends moving platform-independent code
 modules to a location 32-bit TestStand and 64-bit TestStand share so you can
 maintain a single copy of the code module.

If a Microsoft Visual Studio, LabWindows/CVI, or other development environment project resides in a search directory for which you enabled the Search Subdirectories option in the Edit Search Directories dialog box, ensure that the project does not create intermediate or output files from a 64-bit build in the 32-bit search directory or vice versa. When searching subdirectories, 32-bit TestStand might find the 64-bit version of the DLL code module first. When this happens, the 64-bit version of the DLL hides the 32-bit version of the DLL from 32-bit TestStand, causing steps that use the code module to fail because 32-bit TestStand cannot load the 64-bit DLL. Similarly, when searching subdirectories, 64-bit TestStand might find the 32-bit version of the DLL code module first. When this happens, the 32-bit version of the DLL hides the 64-bit version of the DLL from 64-bit TestStand, causing steps that use the code module to fail because 64-bit TestStand cannot load the 32-bit DLL.

Parent topic:

Locating the Correct Code Module in 32-bit TestStand and 64-bit TestStand

Related concepts:

- TestStand Directory Structure

<!--NI_TOPIC bundle=teststand path=using-teststand-ui-controls-in-different-envi.html language=enus -->
## TOPIC 01000: Using TestStand UI Controls in Different Environments

- bundle_id: `teststand`
- source_path: `using-teststand-ui-controls-in-different-envi.html`
- source_url: https://docs-be.ni.com/bundle/teststand/raw/resource/enus/using-teststand-ui-controls-in-different-envi.html
- document_id: `teststand`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use the TestStand User Interface (UI) Controls in LabVIEW, LabWindows/CVI, Microsoft Visual Studio, and Microsoft Visual C++.

### Using TestStand UI Controls in Different Environments

You can use the TestStand User Interface (UI) Controls in LabVIEW, LabWindows/CVI, Microsoft Visual Studio, and Microsoft Visual C++.

Parent topic:

TestStand UI Controls

Related concepts:

- TestStand UI Controls
- Using TestStand UI Controls in LabVIEW
- Using TestStand UI Controls in LabWindows/CVI
- Using TestStand UI Controls in Microsoft Visual Studio
- Using TestStand UI Controls in Microsoft Visual C++
