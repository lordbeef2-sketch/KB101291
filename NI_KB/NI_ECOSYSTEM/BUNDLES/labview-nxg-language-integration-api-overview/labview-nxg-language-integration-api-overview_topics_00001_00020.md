# NI DOCUMENT BUNDLE: labview-nxg-language-integration-api-overview

<!--NI_BUNDLE_CHUNK bundle=labview-nxg-language-integration-api-overview start=1 end=20 -->
<!--NI_TOPIC bundle=labview-nxg-language-integration-api-overview path=call-net-lv-app.html language=enus -->
## TOPIC 00001: Calling .NET Code from Your Application

- bundle_id: `labview-nxg-language-integration-api-overview`
- source_path: `call-net-lv-app.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-language-integration-api-overview/raw/resource/enus/call-net-lv-app.html
- document_id: `labview-nxg-language-integration-api-overview`
- page_type: `leaf`
- content_type: `task`
- source_description: Integrate existing .NET code into your application by calling a .NET assembly from the Global Assembly Cache (GAC). To call a .NET assembly, you must create a .NET document, or interface. Select FileNew.NET Interface to add a .NET document to your project. Click Select Assembly to open, search, and

Calling .NET Code from Your Application

Integrate existing .NET code into your application by calling a .NET assembly from the Global Assembly Cache (GAC).

To call a .NET assembly, you must create a .NET document, or interface.

1. Select 
 File»New».NET Interface to add a .NET document to your project.
2. Click 
 Select Assembly to open, search, and select from the list of available .NET items.
3. In the .NET document, select the .NET namespaces and classes you want to use in your application. 
 In the Project Items palette, LabVIEW NXG creates new palettes for all of the namespaces and classes you select. These new palettes contain properties and methods that are entry points to the .NET assemblies. You can use these entry points in any project in your application. 
 org.dita.html5/xsl/topic.xsl 455Note You must save the document to make the newly selected items available in your project.
4. Open the VI in which you want to call the .NET code.
5. On the diagram, select 
 Project Items»Software. Then click the .NET folder to show every entry point you selected in the .NET document.
6. Drop the entry points you want to use on the diagram.
7. Wire the entry points like nodes and complete the diagram.
8. Execute the VI. 
 As the VI executes, input and output data passes between the .NET assembly and the diagram through the .NET entry points you specify.

Parent topic:

Language Integration in G

<!--NI_TOPIC bundle=labview-nxg-language-integration-api-overview path=callback-vis.html language=enus -->
## TOPIC 00002: Callback VIs

- bundle_id: `labview-nxg-language-integration-api-overview`
- source_path: `callback-vis.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-language-integration-api-overview/raw/resource/enus/callback-vis.html
- document_id: `labview-nxg-language-integration-api-overview`
- page_type: `leaf`
- content_type: `concept`
- source_description: A callback VI contains code to handle a .NET event you specify. You must create a callback VI to handle events from .NET objects when the objects generate the registered events. The callback VI runs when the event occurs. When you create a callback VI, LabVIEW NXG creates a reentrant VI that you can

Callback VIs

A callback VI contains code to handle a .NET event you specify.

- Event Common Data
  - Event Source—Specifies the source of the event, such as LabVIEW NXG or
 .NET. A value of 2 indicates a .NET event.
  - Event Type—Specifies which event occurred. This is an enumerated type
 for user interface events and a 32-bit unsigned integer type for .NET
 and other event sources.
  - Time Stamp—Specifies the time, in milliseconds, that the event was
 generated.
- Control Reference—Specifies a reference to the .NET object on which the event
 occurred.
- Event Data—Specifies the parameters specific to the event the callback VI
 handles. LabVIEW NXG determines the appropriate Event Data when you select an
 event from the Register Event Callback node. If an event
 does not have data associated with it, LabVIEW NXG does not create this control
 in the callback VI.
- Event Data Out—Specifies the modifiable parameters specific to the event the
 callback VI handles. This element is available only if the .NET event has output
 parameters.
- user parameter—Specifies data that you want to pass to the
 callback VI when the .NET object generates the event.

Note

Parent topic:

Calling .NET Code from Your Application

Related concepts:

- Callback VIs
- .NET Events

Related tasks:

- Registering and Handling .NET Events

Related information:

- Register Event Callback

<!--NI_TOPIC bundle=labview-nxg-language-integration-api-overview path=calling-matlab-functions-scripts.html language=enus -->
## TOPIC 00003: Calling MATLAB Functions and Scripts

- bundle_id: `labview-nxg-language-integration-api-overview`
- source_path: `calling-matlab-functions-scripts.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-language-integration-api-overview/raw/resource/enus/calling-matlab-functions-scripts.html
- document_id: `labview-nxg-language-integration-api-overview`
- page_type: `leaf`
- content_type: `task`
- source_description: Create an Interface for MATLAB to define calls to a MATLAB function or script. On the Project Files tab, select NewInterface for MATLAB. In the Interface for MATLAB, use one of the following options to specify a function or script you want to call: Click the ... button and select a MATLAB file on di

Calling MATLAB Functions and Scripts

Create an Interface for MATLAB to define calls to a MATLAB function or script.

1. On the 
 Project Files tab, select 
 New»Interface for 
 MATLAB®.
2. In the Interface for MATLAB, use one of the following options to specify a function or script you want to call:
  - Click the 
 ... button and select a MATLAB file on disk.
  - Enter the name of a MATLAB function or the filename of a MATLAB file on the MATLAB search path. Use this option to build your G dataflow application into an executable ( .exe ).
3. On the 
 Document tab, choose the 
 File type of the MATLAB file you want to call. 
 NI recommends that you format MATLAB programs into functions because functions perform better than scripts and offer a clean programming model.
4. Define the 
 *interface node* that maps to the arguments in the function or variables in the script.
  1. Click 
 Add interface node.
  2. On the 
 Item tab, enter a name for the interface node. 
 The name will show up in the node icon.
  3. Click 
 Add parameter.
  4. On the 
 Item tab, specify the parameter name, data type, and behavior.
  5. Add more parameters as necessary. 
 The number of parameters in the interface node must match the number of arguments in the function or the number of variables in the script.
5. Save the Interface for MATLAB.
6. Open the VI in which you want to call the MATLAB function or script.
7. On the diagram palette, click 
 Project Items»Software to find the interface node you defined in the Interface for MATLAB.
8. Drop the interface node on the diagram.
9. Wire the interface node and complete the diagram.
10. Run the VI. 
 The 
 MATLAB Command Window automatically launches. Input data passes from the diagram to MATLAB, and data returns from MATLAB to the diagram.
 org.dita.html5/xsl/topic.xsl 455Note If you have multiple versions of MATLAB installed, by default the Interface for MATLAB invokes the version of MATLAB you most recently installed.

Parent topic:

Interfaces for MATLAB

<!--NI_TOPIC bundle=labview-nxg-language-integration-api-overview path=calling-shared-libraries.html language=enus -->
## TOPIC 00004: Calling Shared Libraries

- bundle_id: `labview-nxg-language-integration-api-overview`
- source_path: `calling-shared-libraries.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-language-integration-api-overview/raw/resource/enus/calling-shared-libraries.html
- document_id: `labview-nxg-language-integration-api-overview`
- page_type: `leaf`
- content_type: `task`
- source_description: Define calls to a shared library to integrate external code into your application. A shared library is a file containing executable program modules that different programs can use. To call these shared library functions in your application, use a Shared Library Interface (SLI) document. Use one SLI

Calling Shared Libraries

Define calls to a shared library to integrate external code into your application.

A shared library is a file containing executable program modules that different programs can use. To call these shared library functions in your application, use a Shared Library Interface (SLI) document. Use one SLI per shared library. To call functions from another shared library, create a new SLI to access those functions.

Create an SLI.

1. On the 
 Project Files tab, add an SLI to your project. 
 An SLI document appears in your project.
2. In the SLI, click the 
 ... button and select the shared library on disk.
3. Define the prototype for a function you want to call from the shared library. 
 A defined call to a function in an SLI is called an 
 *entry point*.
  1. Click 
 Add function.
  2. On the 
 Item tab, select the function prototype symbol. 
 The entry point's name reflects the symbol you select.
  3. Click 
 Add parameter.
  4. On the 
 Item tab, specify the parameter name, data type, and behavior.
4. Repeat step 3 to create as many entry points as you need for your project.
5. Save the SLI.

Use the entry points in any application in your project.

1. Open the VI in which you want to call the shared library.
2. On the diagram palette, click Project Items >> Software. 
 Click the SLI folder to show every entry point you defined in that SLI.
3. Drop the entry points you want to use on the diagram.
4. Wire the entry points and complete the diagram.
5. Run the VI. 
 Input data passes from the diagram to the external code, and data returns from the external code to the diagram.

Parent topic:

Shared Library Interfaces

<!--NI_TOPIC bundle=labview-nxg-language-integration-api-overview path=consid-net-lv.html language=enus -->
## TOPIC 00005: Considerations for Including .NET Code in a LabVIEW NXG Application

- bundle_id: `labview-nxg-language-integration-api-overview`
- source_path: `consid-net-lv.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-language-integration-api-overview/raw/resource/enus/consid-net-lv.html
- document_id: `labview-nxg-language-integration-api-overview`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can call .NET code from your LabVIEW NXG application. However, some .NET features and functionality either work differently or do not have direct counterparts in LabVIEW NXG. To successfully include .NET code in your application, learn which differences may affect your existing .NET code. Generi

Considerations for Including .NET Code in a LabVIEW NXG Application

You can call .NET code from your LabVIEW NXG application. However, some .NET features and functionality either work differently or do not have direct counterparts in LabVIEW NXG.

To successfully include .NET code in your application, learn which differences may affect your existing .NET code.

#### Generic .NET Classes and Methods

LabVIEW NXG cannot create generic .NET classes or call generic .NET methods. However, you can call .NET methods that use generic classes or methods internally.

#### Static .NET Properties and Methods

You can use static .NET properties and methods in LabVIEW NXG. Static .NET methods do not include an input for a .NET class reference and display a different icon from non-static methods. Static .NET property nodes do include an input for a .NET class reference, but they only use the type information at run time. You can combine static and non-static properties on the same property node.

#### Dynamic Keywords

LabVIEW NXG requires .NET objects to have a defined type in order to display available methods. Therefore, although you can call .NET methods that return a dynamic data type, you cannot use the returned data to call other methods.

Note

#### Default Values for Optional Parameters

.NET assemblies may include methods that allow optional parameters, which have default values that the method uses if the caller does not specify a value for the parameter. However, when you call a method with an optional parameter from LabVIEW NXG, LabVIEW NXG always passes the default value for the data type of the parameter instead of letting the method use its own pre-configured defaults.

Parent topic:

Calling .NET Code from Your Application

<!--NI_TOPIC bundle=labview-nxg-language-integration-api-overview path=conv-net-lv-types.html language=enus -->
## TOPIC 00006: Conversion of .NET Data Types to LabVIEW NXG Data Types

- bundle_id: `labview-nxg-language-integration-api-overview`
- source_path: `conv-net-lv-types.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-language-integration-api-overview/raw/resource/enus/conv-net-lv-types.html
- document_id: `labview-nxg-language-integration-api-overview`
- page_type: `leaf`
- content_type: `reference`
- source_description: LabVIEW NXG converts the data types of .NET property, method, and constructor parameters into LabVIEW NXG data types so LabVIEW NXG can read and interpret the data. LabVIEW NXG displays data types it cannot convert as .NET references. Refer to the following table to compare .NET data types and their

Conversion of .NET Data Types to LabVIEW NXG Data Types

LabVIEW NXG converts the data types of .NET property, method, and constructor parameters into LabVIEW NXG data types so LabVIEW NXG can read and interpret the data.

LabVIEW NXG displays data types it cannot convert as .NET references. Refer to the following table to compare .NET data types and their corresponding LabVIEW NXG data types.

| .NET Data Types | LabVIEW Data Types |
| --- | --- |
| System .Int64, System .UInt64, System Int32, System UInt32, System .Int16, System .UInt16 |  |
| System.String |  |
| System.Boolean |  |
| System.Byte, System.UByte |  |
| System.Char |  |
| System.Single, System.Double, System.Decimal |  |
| System.Array | An array of the corresponding type. |
| Enumeration | A ring with an integer value of a corresponding type. |
| DateTime |  |
| Any other .NET object |  |

Parent topic:

Calling .NET Code from Your Application

<!--NI_TOPIC bundle=labview-nxg-language-integration-api-overview path=debug-matlab-functions-scripts.html language=enus -->
## TOPIC 00007: Debugging MATLAB Functions and Scripts

- bundle_id: `labview-nxg-language-integration-api-overview`
- source_path: `debug-matlab-functions-scripts.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-language-integration-api-overview/raw/resource/enus/debug-matlab-functions-scripts.html
- document_id: `labview-nxg-language-integration-api-overview`
- page_type: `leaf`
- content_type: `task`
- source_description: You can debug MATLAB functions and scripts when you use an Interface for MATLAB to call them in your G dataflow application. Complete the following steps to debug a function or script. In an Interface for MATLAB, ensure that you specify the correct file path to a MATLAB function or script. Click Ope

Debugging MATLAB Functions and Scripts

You can debug MATLAB functions and scripts when you use an Interface for MATLAB to call them in your G dataflow application.

Complete the following steps to debug a function or script.

1. In an Interface for MATLAB, ensure that you specify the correct file path to a MATLAB function or script.
2. Click 
 Open in 
 MATLAB® to open the function or script in the MATLAB 
 Editor.
3. In the MATLAB Editor that launches, add a breakpoint on
 the line of code where you think the problem could be.
4. Run your G dataflow application. 
 The execution of the MATLAB function or script pauses at the specific line where you
 add the breakpoint.
5. While the function or script is paused, you can view the value of each argument in the MATLAB 
 Editor.
6. Click 
 Continue in the MATLAB 
 Editor. 
 The G dataflow application finishes executing the remaining code.
7. Change the values of arguments or modify the script or function to produce expected results by using standard MATLAB functionality.

Parent topic:

Interfaces for MATLAB

<!--NI_TOPIC bundle=labview-nxg-language-integration-api-overview path=debugging-shared-library-interfaces.html language=enus -->
## TOPIC 00008: Debugging Shared Library Interfaces

- bundle_id: `labview-nxg-language-integration-api-overview`
- source_path: `debugging-shared-library-interfaces.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-language-integration-api-overview/raw/resource/enus/debugging-shared-library-interfaces.html
- document_id: `labview-nxg-language-integration-api-overview`
- page_type: `leaf`
- content_type: `task`
- source_description: Find solutions to common problems that may occur when configuring and using Shared Library Interfaces (SLIs). Most errors occur due to mismatches between the SLI configuration and the functions in the shared library. These kinds of crashes might not occur at the time the shared library call actually

Debugging Shared Library Interfaces

Find solutions to common problems that may occur when configuring and using Shared Library Interfaces (SLIs).

Note

Most errors occur due to mismatches between the SLI configuration and the functions in the shared library. These kinds of crashes might not occur at the time the shared library call actually executes on the diagram. Refer to 
 [Shared Library Best Practices](shared-library-best-practices.html#GUID-FAC5AAA5-663E-4AEF-A98A-ECA742899611) for tips on how to avoid errors in the code of the shared library.

Use the following table to resolve an error.

| Issue | Solution |
| --- | --- |
| You receive a Function not found in library error. | Verify the SLI uses the correct spelling and case sensitivity for the entrypoints you defined. Verify the C++ compiler has not decorated the function name. For details on this issue, refer to Shared Library Best Practices. |
| You receive an error message that a secondary shared library cannot be found. | The primary shared library needs additional functions from one or more other shared libraries. Find the other shared libraries and place them in the same directory as the shared library that needs them or in a directory that is in the search path. |
| VI crashes or behaves incorrectly. | Verify the return data types and parameter settings of your entrypoints exactly match the data types the function in the shared library uses. Verify the SLI is passing arguments in the correct order. |
| LabVIEW hangs and requires you to restart. | In the Item tab, verify your SLI is configured to Run in any thread. Note This solution applies only to DLLs built from LabVIEW. |

Shared Library Best Practices

Shared Library Interface Best Practices

Parent topic:

Shared Library Interfaces

<!--NI_TOPIC bundle=labview-nxg-language-integration-api-overview path=dni-outside-gac.html language=enus -->
## TOPIC 00009: Adding a .NET Assembly Outside the GAC to a Project

- bundle_id: `labview-nxg-language-integration-api-overview`
- source_path: `dni-outside-gac.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-language-integration-api-overview/raw/resource/enus/dni-outside-gac.html
- document_id: `labview-nxg-language-integration-api-overview`
- page_type: `leaf`
- content_type: `task`
- source_description: Add a .NET assembly outside of the Global Assembly Cache (GAC) to your LabVIEW NXG project. Create a .NET interface document (DNI) within your project. Add the desired .NET assembly to your DNI by opening your DNI document and clicking Select Assembly. Within the Select Assembly dialog, select Impor

Adding a .NET Assembly Outside the GAC
 to a Project

Add a .NET assembly outside of the Global Assembly Cache (GAC) to your LabVIEW
 NXG project.

.NET interface document

1. Add the desired .NET assembly to your DNI by opening your DNI
 document and clicking Select
 Assembly. Within the Select
 Assembly dialog, select
 Import and navigate to the
 .DLL assembly you wish to add to the project. Click
 OK to import the selected
 assembly.
2. After LabVIEW NXG recognizes your assembly and locates all
 dependencies within the selected directory, a Copy
 Existing File(s)? dialog prompts you to
 copy the files to your project. Select
 Copy to proceed.
3. Select Project in the left pane of the
 Select Assembly dialog. The
 imported assembly appears there.
4. Select the assembly and click OK. 
 The selected assembly appears within your DNI
 document.

Configure the imported
 assembly for use in your project.

Parent topic:

Calling .NET Code from Your Application

<!--NI_TOPIC bundle=labview-nxg-language-integration-api-overview path=dotnet-events.html language=enus -->
## TOPIC 00010: .NET Events

- bundle_id: `labview-nxg-language-integration-api-overview`
- source_path: `dotnet-events.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-language-integration-api-overview/raw/resource/enus/dotnet-events.html
- document_id: `labview-nxg-language-integration-api-overview`
- page_type: `leaf`
- content_type: `concept`
- source_description: .NET events are actions that affect a .NET object, such as clicking a mouse, pressing a key, or receiving notifications about running out of memory or tasks completing. When a .NET action occurs, the .NET object sends an event and event-specific data to alert the .NET container. The .NET object defi

.NET Events

.NET events are actions that affect a .NET object, such as clicking a
 mouse, pressing a key, or receiving notifications about running out of memory or tasks
 completing. When a .NET action occurs, the .NET object sends an event and
 event-specific data to alert the .NET container. The .NET object defines the events
 available to itself.

- .NET object you want to generate an event for.
- Register Event Callback node to specify and register for
 the type of event you want to generate.
- Callback VI that contains code to handle the .NET event you specify.

To register a .NET object for an event, wire the .NET object to the Register
 Event Callback node and specify the event you want to generate for that
 object. After you register for the event, create a callback VI that contains code to
 handle the event. If you change the event after you create a callback VI, consider that
 different events might have different event data formats and check for broken wires on
 the diagram.

Parent topic:

Calling .NET Code from Your Application

Related concepts:

- Callback VIs
- .NET Events

Related tasks:

- Registering and Handling .NET Events

Related information:

- Register Event Callback

<!--NI_TOPIC bundle=labview-nxg-language-integration-api-overview path=handle-dotnet-events.html language=enus -->
## TOPIC 00011: Registering and Handling .NET Events

- bundle_id: `labview-nxg-language-integration-api-overview`
- source_path: `handle-dotnet-events.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-language-integration-api-overview/raw/resource/enus/handle-dotnet-events.html
- document_id: `labview-nxg-language-integration-api-overview`
- page_type: `leaf`
- content_type: `task`
- source_description: To handle a .NET event, you must register for the event and create a callback VI to handle that event. Before you begin, complete the following prerequisite tasks: Enable .gpal option to place diagram contents when dropped.Enable preview features.Relaunch G Web Development Software. Complete the fol

Registering and Handling .NET Events

To handle a .NET event, you must register for the event and create a callback VI to
 handle that event.

- Enable .gpal option to place diagram contents when
 dropped.
- Enable preview features .
- Relaunch G Web Development Software.

Complete the following steps to register and
 handle .NET events.

1. Use a .NET Interface document to create a .NET object from LabVIEW NXG.
2. Add the Register Event Callback node to the diagram.
3. Wire the reference or object to Event on the
 Register Event Callback node.
4. Expand Event on the Register Event
 Callback node and select an event.
5. (Optional) Wire the data that you want to pass to the callback VI to
 user parameter.
6. Right-click VI Ref and select Create
 Callback VI to generate a VI based on the event you select and
 the data you wire to user parameter. LabVIEW NXG wires
 the callback VI to VI Ref. 
 org.dita.html5/xsl/topic.xsl 455Note You can use an existing VI as a
 callback VI as long as the connector pane of that VI matches the connector pane of the
 event data. The callback VI must be reentrant and the reference to the callback VI must
 be strictly typed.
7. Open the callback VI and edit the diagram to handle the event. 
 org.dita.html5/xsl/topic.xsl 455Note If you want to pass any
 part of event data through the callback VI, you must wire event
 data to event data out.

Until you unregister for events, LabVIEW NXG continues to
 generate and queue the events as long as the VI runs, even if no Event
 Structure is waiting to handle them. This behavior consumes memory
 and can hang the VI if you enable front panel locking for the events. To avoid this,
 unregister for events when you no longer need to handle them using the
 Unregister For Events node.

Parent topic:

Calling .NET Code from Your Application

Related concepts:

- Callback VIs
- .NET Events

Related tasks:

- Registering and Handling .NET Events

Related information:

- Register Event Callback

<!--NI_TOPIC bundle=labview-nxg-language-integration-api-overview path=import-export-matlab-data.html language=enus -->
## TOPIC 00012: Importing and Exporting MATLAB Data

- bundle_id: `labview-nxg-language-integration-api-overview`
- source_path: `import-export-matlab-data.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-language-integration-api-overview/raw/resource/enus/import-export-matlab-data.html
- document_id: `labview-nxg-language-integration-api-overview`
- page_type: `leaf`
- content_type: `task`
- source_description: In a G dataflow application, you can import data from or export data to MATLAB using MATLAB formatted binary files (.mat). To import data from MATLAB, click the Import button in the Captured Data tab and select a .mat file. You can use the data in your G dataflow application. To export data to MATLA

Importing and Exporting MATLAB Data

In a G dataflow application, you can import data from or export data to MATLAB® using MATLAB formatted binary files (.mat).

To import data from MATLAB, click the 
 Import button in the 
 Captured Data tab and select a 
 .mat file. You can use the data in your G dataflow application.

To export data to MATLAB, right-click a data item in the 
 Captured Data tab and select 
 Export to export to a 
 .mat file. You can then load the data file in MATLAB to analyze the data.

Parent topic:

Interfaces for MATLAB

<!--NI_TOPIC bundle=labview-nxg-language-integration-api-overview path=integrationg.html language=enus -->
## TOPIC 00013: Language Integration in G

- bundle_id: `labview-nxg-language-integration-api-overview`
- source_path: `integrationg.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-language-integration-api-overview/raw/resource/enus/integrationg.html
- document_id: `labview-nxg-language-integration-api-overview`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use other languages in addition to G when creating an application. The following table displays the ways you can integrate your existing code in another language into G. Language How to Integrate C Use a C node. Shared Library Add a Shared Library Interface (SLI) document. .NET Code Create a

Language Integration in G

You can use other languages in addition to G when creating an application.

The following table displays the ways you can integrate your existing code in another language into G.

| Language | How to Integrate |
| --- | --- |
| C | Use a C node. |
| Shared Library | Add a Shared Library Interface (SLI) document. |
| .NET Code | Create a .NET Interface. |
| MATLAB Functions and Scripts | Create a MATLAB Interface. |

<!--NI_TOPIC bundle=labview-nxg-language-integration-api-overview path=interfaces-for-matlab.html language=enus -->
## TOPIC 00014: Interfaces for MATLAB

- bundle_id: `labview-nxg-language-integration-api-overview`
- source_path: `interfaces-for-matlab.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-language-integration-api-overview/raw/resource/enus/interfaces-for-matlab.html
- document_id: `labview-nxg-language-integration-api-overview`
- page_type: `leaf`
- content_type: `concept`
- source_description: An Interface for MATLAB (.mli) is a document in which you define calls to a MATLAB file (.m or .mlx) in your G dataflow application. MATLAB files can be either functions or scripts. NI recommends that you format MATLAB programs into functions because functions perform better than scripts and offer a

Interfaces for MATLAB

An 
 *Interface for MATLAB* (.mli) is a document in which you define calls to a MATLAB file (.m or 
 .mlx) in your G dataflow application.

MATLAB files can be either 
 *functions* or 
 *scripts*. NI recommends that you format MATLAB programs into functions because functions perform better than scripts and offer a clean programming model.

In an Interface for MATLAB, you create 
 *interface nodes* that map to arguments in a MATLAB function or variables in a MATLAB script. Visual representations of interface nodes appear on the 
 Project Item»Software palette on the diagram. You can place and wire interface nodes in your application.

When you execute the application, the Interface for MATLAB invokes MATLAB, which calls the MATLAB file. Input data passes from the diagram to MATLAB, and data returns from MATLAB to the diagram.

The Interface for MATLAB supports Windows targets only.

#### Examples

Search within the programming environment to access the following installed examples:

- Interface for MATLAB Fundamentals
- Interface for MATLAB Working with nD Arrays
- Interface for MATLAB Working with Structures
- MATLAB User Defined Function
- MATLAB Monte Carlo Calculation
- Prime Number Calculation

MATLAB<sup>®</sup> is a registered trademark of The MathWorks, Inc.

Parent topic:

Language Integration in G

<!--NI_TOPIC bundle=labview-nxg-language-integration-api-overview path=mathscript-vs-matlab-function.html language=enus -->
## TOPIC 00015: Migrating MathScript Functions to MathWorks Functions

- bundle_id: `labview-nxg-language-integration-api-overview`
- source_path: `mathscript-vs-matlab-function.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-language-integration-api-overview/raw/resource/enus/mathscript-vs-matlab-function.html
- document_id: `labview-nxg-language-integration-api-overview`
- page_type: `leaf`
- content_type: `reference`
- source_description: The following table lists MathScript function names and their corresponding function names in MathWorks products. Review the usage of these functions when you migrate from MathScript Node to Interface for MATLAB. MathScript Function Name MathWorks Function Name MathWorks Product ac_to_poly ac2poly S

Migrating MathScript Functions to MathWorks Functions

The following table lists MathScript function names and their corresponding function names in MathWorks products. Review the usage of these functions when you migrate from MathScript Node to Interface for MATLAB.

| MathScript Function Name | MathWorks Function Name | MathWorks Product |
| --- | --- | --- |
| ac_to_poly | ac2poly | Signal Processing Toolbox™ |
| ac_to_rc | ac2rc | Signal Processing Toolbox™ |
| ac_to_rcschur | schurrc | Signal Processing Toolbox™ |
| accumproducts | cumprod | MATLAB® |
| accumsums | cumsum | MATLAB® |
| accumtrapint | cumtrapz | MATLAB® |
| ackermann | acker | Control System Toolbox™ |
| add_noise | imnoise | Image Processing Toolbox™ |
| algriccati | care | Control System Toolbox™ |
| ar_burg | arburg | Signal Processing Toolbox™ |
| ar_covar | arcov | Signal Processing Toolbox™ |
| ar_mcovar | armcov | Signal Processing Toolbox™ |
| ar_yule | aryule | Signal Processing Toolbox™ |
| arginchk | narginchk | MATLAB® |
| arginnum | nargin | MATLAB® |
| argoutchk | nargoutchk | MATLAB® |
| argoutnum | nargout | MATLAB® |
| augmentstate | augstate | Control System Toolbox™ |
| balance_diag | ssbal | Control System Toolbox™ |
| balance_grammian | balreal | Control System Toolbox™ |
| barhoriz | barh | MATLAB® |
| base_to_dec | base2dec | MATLAB® |
| bessel_h | besselh | MATLAB® |
| bessel_i | besseli | MATLAB® |
| bessel_j | besselj | MATLAB® |
| bessel_k | besselk | MATLAB® |
| bessel_y | bessely | MATLAB® |
| beta_incomplete | betainc | MATLAB® |
| beta_ln | betaln | MATLAB® |
| bin_to_dec | bin2dec | MATLAB® |
| bitnot | bitcmp | MATLAB® |
| bitreverseorder | bitrevorder | Signal Processing Toolbox™ |
| blockdiag | blkdiag | MATLAB® |
| buffermx | buffer | Signal Processing Toolbox™ |
| c_to_d | c2d | Control System Toolbox™ |
| canonical | canon | Control System Toolbox™ |
| cart_to_polar | cart2pol | MATLAB® |
| cart_to_sphere | cart2sph | MATLAB® |
| ccepstrum | cceps | Signal Processing Toolbox™ |
| cctranspose | ctranspose | MATLAB® |
| char | setstr | MATLAB® |
| chirpzt | czt | Signal Processing Toolbox™ |
| circularshift | circshift | MATLAB® |
| clfig | clf | MATLAB® |
| clgraph | clf | MATLAB® |
| clout | clc | MATLAB® |
| coherence | cohere | Signal Processing Toolbox™ |
| coherence_ms | mscohere | Signal Processing Toolbox™ |
| colormapplot | rgbplot | MATLAB® |
| companion | compan | MATLAB® |
| condeign | condeig | MATLAB® |
| condestimate | condest | MATLAB® |
| condrecip | rcond | MATLAB® |
| conjugate | conj | MATLAB® |
| contouris | contourf | MATLAB® |
| contours | contourc | MATLAB® |
| conv2d | conv2 | MATLAB® |
| convcirc | cconv | Signal Processing Toolbox™ |
| convexhull | convhull | MATLAB® |
| convmx | convmtx | Signal Processing Toolbox™ |
| corrcoeff | corrcoef | MATLAB® |
| corrmx | corrmtx | Signal Processing Toolbox™ |
| covarmx | cov | MATLAB® |
| crosscorr | xcorr | Signal Processing Toolbox™ |
| crosscorr2d | xcorr2 | Signal Processing Toolbox™ |
| crosscovar | xcov | Signal Processing Toolbox™ |
| crosspsd | cpsd | Signal Processing Toolbox™ |
| crosssd | csd | Signal Processing Toolbox™ |
| ctrbmx | ctrb | Control System Toolbox™ |
| ctrbstairs | ctrbf | Control System Toolbox™ |
| d_to_c | d2c | Control System Toolbox™ |
| d_to_d | d2d | Control System Toolbox™ |
| dalgriccati | dare | Control System Toolbox™ |
| datatype | class | MATLAB® |
| date_to_num | datenum | MATLAB® |
| date_to_str | datestr | MATLAB® |
| date_to_vector | datevec | MATLAB® |
| datescale | datetick | MATLAB® |
| dec_to_base | dec2base | MATLAB® |
| dec_to_bin | dec2bin | MATLAB® |
| dec_to_hex | dec2hex | MATLAB® |
| deflate | squeeze | MATLAB® |
| deg_to_rad | deg2rad | MATLAB® |
| delay_to_z | delay2z | Control System Toolbox™ |
| density_kernel | ksdensity | Statistics and Machine Learning Toolbox™ |
| dftmx | dftmtx | Signal Processing Toolbox™ |
| difference | diff | MATLAB® |
| digitreverseorder | digitrevorder | Signal Processing Toolbox™ |
| dirichlet | diric | Signal Processing Toolbox™ |
| dlaplacian | del2 | MATLAB® |
| dlqr_y | dlqry | Control System Toolbox™ |
| dlyapunov | dlyap | Control System Toolbox™ |
| drandss | drss | Control System Toolbox™ |
| drandtf | tf | Control System Toolbox™ |
| drandzpk | zpk | Control System Toolbox™ |
| duplicate | deal | MATLAB® |
| eigsort | eigs | MATLAB® |
| elliptic_int | ellipke | MATLAB® |
| elliptic_j | ellipj | MATLAB® |
| eqtflen | eqtflength | Signal Processing Toolbox™ |
| erf_inv | erfinv | MATLAB® |
| erfc_inv | erfcinv | MATLAB® |
| erfc_scale | erfcx | MATLAB® |
| estimator | estim | Control System Toolbox™ |
| evalfreq | evalfr | Control System Toolbox™ |
| exp_int | expint | MATLAB® |
| expmx | expm | MATLAB® |
| expmx_eign | expmdemo3 | MATLAB® |
| expmx_pade | expmdemo1 | MATLAB® |
| expmx_taylor | expmdemo2 | MATLAB® |
| eyediagram | eyediagram | Communications Toolbox™ |
| fft2d | fft2 | MATLAB® |
| filter_2d | filter2 | MATLAB® |
| filter_fft | fftfilt | Signal Processing Toolbox™ |
| filter_impulse | impinvar | Signal Processing Toolbox™ |
| filter_lattice | latcfilt | Signal Processing Toolbox™ |
| filter_median | medfilt1 | Signal Processing Toolbox™ |
| filter_rcos | rcosflt | Communications Toolbox™ |
| filter_sg | sgolayfilt | Signal Processing Toolbox™ |
| filter_sos | sosfilt | Signal Processing Toolbox™ |
| filter_zerophase | filtfilt | Signal Processing Toolbox™ |
| filteric | filtic | Signal Processing Toolbox™ |
| findnz | find | MATLAB® |
| fir_fs | fir2 | Signal Processing Toolbox™ |
| fir_gauss | firgauss | Signal Processing Toolbox™ |
| fir_gaussps | gaussfir | Signal Processing Toolbox™ |
| fir_interp | intfilt | Signal Processing Toolbox™ |
| fir_lsq | firls | Signal Processing Toolbox™ |
| fir_pm | firpm | Signal Processing Toolbox™ |
| fir_pmord | firpmord | Signal Processing Toolbox™ |
| fir_rcos | firrcos | Signal Processing Toolbox™ |
| fir_remez | remez | Signal Processing Toolbox™ |
| fir_remezord | remezord | Signal Processing Toolbox™ |
| fir_sgsmooth | sgolay | Signal Processing Toolbox™ |
| fir_win | fir1 | Signal Processing Toolbox™ |
| flatindex | sub2ind | MATLAB® |
| fmin_bracket | fminbnd | MATLAB® |
| fmin_lp | linprog | Optimization Toolbox™ |
| fmin_qp | quadprog | Optimization Toolbox™ |
| fread_audio | audioread | MATLAB® |
| freq_space | freqspace | MATLAB® |
| freqsd | freqs | Signal Processing Toolbox™ |
| freqzd | freqz | Signal Processing Toolbox™ |
| funmx | funm | MATLAB® |
| gamma_incomplete | gammainc | MATLAB® |
| gamma_ln | gammaln | MATLAB® |
| gaussmonopulse | gmonopuls | Signal Processing Toolbox™ |
| gausspulse | gauspuls | Signal Processing Toolbox™ |
| gensignal | gensig | Control System Toolbox™ |
| grammian | gram | Control System Toolbox™ |
| hconcatmx | horzcat | MATLAB® |
| hessenberg | hess | MATLAB® |
| hex_to_dec | hex2dec | MATLAB® |
| hex_to_num | hex2num | MATLAB® |
| hilbertmx | hilb | MATLAB® |
| histogram | hist | MATLAB® |
| histogramc | histc | MATLAB® |
| iccepstrum | icceps | Signal Processing Toolbox™ |
| ifft2d | ifft2 | MATLAB® |
| ifft_shift | ifftshift | MATLAB® |
| iir_bessel | besself | Signal Processing Toolbox™ |
| iir_besselzpk | besselap | Signal Processing Toolbox™ |
| iir_butter | butter | Signal Processing Toolbox™ |
| iir_butterord | buttord | Signal Processing Toolbox™ |
| iir_butterzpk | buttap | Signal Processing Toolbox™ |
| iir_cheby1 | cheby1 | Signal Processing Toolbox™ |
| iir_cheby1ord | cheb1ord | Signal Processing Toolbox™ |
| iir_cheby1zpk | cheb1ap | Signal Processing Toolbox™ |
| iir_cheby2 | cheby2 | Signal Processing Toolbox™ |
| iir_cheby2ord | cheb2ord | Signal Processing Toolbox™ |
| iir_cheby2zpk | cheb2ap | Signal Processing Toolbox™ |
| iir_elliptic | ellip | Signal Processing Toolbox™ |
| iir_ellipticord | ellipord | Signal Processing Toolbox™ |
| iir_ellipticzpk | ellipap | Signal Processing Toolbox™ |
| iir_maxflat | maxflat | Signal Processing Toolbox™ |
| iir_steigmcbride | stmcb | Signal Processing Toolbox™ |
| iir_yulewalker | yulewalk | Signal Processing Toolbox™ |
| imagescaled | imagesc | MATLAB® |
| impzd | impz | Signal Processing Toolbox™ |
| ind_to_sub | ind2sub | MATLAB® |
| int_to_str | int2str | MATLAB® |
| interpolate | interp | Control System Toolbox™ |
| interpolate1d | interp1 | MATLAB® |
| interpolate2d | interp2 | MATLAB® |
| interpolateft | interpft | MATLAB® |
| intrp2d_uneven | griddata | MATLAB® |
| invfreqsd | invfreqs | Signal Processing Toolbox™ |
| invfreqzd | invfreqz | Signal Processing Toolbox™ |
| invhilbertmx | invhilb | MATLAB® |
| iopzgraph | iopzmap | Control System Toolbox™ |
| is_char | ischar | MATLAB® |
| is_dir | isdir | MATLAB® |
| is_empty | isempty | MATLAB® |
| is_equal | isequal | MATLAB® |
| is_equalnan | isequalwithequalnans | MATLAB® |
| is_field | isfield | MATLAB® |
| is_finite | isfinite | MATLAB® |
| is_hold | ishold | MATLAB® |
| is_inf | isinf | MATLAB® |
| is_inpolygon | inpolygon | MATLAB® |
| is_keyword | iskeyword | MATLAB® |
| is_letter | isletter | MATLAB® |
| is_logical | islogical | MATLAB® |
| is_membermx | ismember | MATLAB® |
| is_nan | isnan | MATLAB® |
| is_numeric | isnumeric | MATLAB® |
| is_prime | isprime | MATLAB® |
| is_real | isreal | MATLAB® |
| is_scalar | isscalar | MATLAB® |
| is_sorted | issorted | MATLAB® |
| is_space | isspace | MATLAB® |
| is_string | isstr | MATLAB® |
| is_struct | isstruct | MATLAB® |
| is_student | isstudent | MATLAB® |
| is_to_rc | is2rc | Signal Processing Toolbox™ |
| is_validvarname | isvarname | MATLAB® |
| kaiserwinord | kaiserord | Signal Processing Toolbox™ |
| kalman_d | kalmd | Control System Toolbox™ |
| lar_to_rc | lar2rc | Signal Processing Toolbox™ |
| lattice_to_tf | latc2tf | Signal Processing Toolbox™ |
| leftdiv | ldivide | MATLAB® |
| leftdivmx | mldivide | MATLAB® |
| lib_call | calllib | MATLAB® |
| lib_funclist | libfunctionsview | MATLAB® |
| lib_isloaded | libisloaded | MATLAB® |
| lib_load | loadlibrary | MATLAB® |
| lib_unload | unloadlibrary | MATLAB® |
| linearsolve | linsolve | MATLAB® |
| linramp | linspace | MATLAB® |
| logmx | logm | MATLAB® |
| logramp | logspace | MATLAB® |
| lowercase | lower | MATLAB® |
| lp_to_bp | lp2bp | Signal Processing Toolbox™ |
| lp_to_bs | lp2bs | Signal Processing Toolbox™ |
| lp_to_hp | lp2hp | Signal Processing Toolbox™ |
| lp_to_lp | lp2lp | Signal Processing Toolbox™ |
| lqr_d | lqrd | Control System Toolbox™ |
| lqr_dy | ss | Control System Toolbox™ |
| lqr_y | lqry | Control System Toolbox™ |
| lsf_to_poly | lsf2poly | Signal Processing Toolbox™ |
| lyapunov | lyap | Control System Toolbox™ |
| margins | allmargin | Control System Toolbox™ |
| maxfloat | realmax | MATLAB® |
| maxfloatint | flintmax | MATLAB® |
| maxnamelen | namelengthmax | MATLAB® |
| meshgrid2d | meshgrid | MATLAB® |
| minfloat | realmin | MATLAB® |
| minimal | minreal | Control System Toolbox™ |
| minimal_state | sminreal | Control System Toolbox™ |
| minrepseq | seqperiod | Signal Processing Toolbox™ |
| minus1 | uminus | MATLAB® |
| mirror | flipdim | MATLAB® |
| mirrorh | fliplr | MATLAB® |
| mirrorv | flipud | MATLAB® |
| moment_central | moment | Statistics and Machine Learning Toolbox™ |
| mreduce | modred | Control System Toolbox™ |
| multmx | mtimes | MATLAB® |
| mx_to_str | mat2str | MATLAB® |
| nextpowerof2 | nextpow2 | MATLAB® |
| normestimate | normest | MATLAB® |
| num_to_str | num2str | MATLAB® |
| numdays | eomday | MATLAB® |
| numdims | ndims | MATLAB® |
| numelements | numel | MATLAB® |
| numnz | nnz | MATLAB® |
| nz | nonzeros | MATLAB® |
| obsvmx | obsv | Control System Toolbox™ |
| obsvstair | obsvf | Control System Toolbox™ |
| ode_adams | ode113 | MATLAB® |
| ode_bdf15 | ode15s | MATLAB® |
| ode_bdf23 | ode23tb | MATLAB® |
| ode_rk23 | ode23 | MATLAB® |
| ode_rk45 | ode45 | MATLAB® |
| ode_rosen | ode23s | MATLAB® |
| odepset | odeset | MATLAB® |
| padm | pamdemod | Communications Toolbox™ |
| pam | pammod | Communications Toolbox™ |
| peakfcn1d | humps | MATLAB® |
| peakfcn2d | peaks | MATLAB® |
| phasezd | phasez | Signal Processing Toolbox™ |
| plotcoord | gplot | MATLAB® |
| plottext | gtext | MATLAB® |
| plus1 | uplus | MATLAB® |
| polar_to_cart | pol2cart | MATLAB® |
| poleplace | place | Control System Toolbox™ |
| poles | pole | Control System Toolbox™ |
| poly_pw | mkpp | MATLAB® |
| poly_pwhermite | pchip | MATLAB® |
| poly_scale | polyscale | Signal Processing Toolbox™ |
| poly_stable | polystab | Signal Processing Toolbox™ |
| poly_to_ac | poly2ac | Signal Processing Toolbox™ |
| poly_to_lsf | poly2lsf | Signal Processing Toolbox™ |
| poly_to_rc | poly2rc | Signal Processing Toolbox™ |
| polyderivative | polyder | MATLAB® |
| polyeign | polyeig | MATLAB® |
| polygonarea | polyarea | MATLAB® |
| polyintegral | polyint | MATLAB® |
| polyvalmx | polyvalm | MATLAB® |
| powermx | mpower | MATLAB® |
| powerof2 | pow2 | MATLAB® |
| powerofreal | realpow | MATLAB® |
| psd_burg | pburg | Signal Processing Toolbox™ |
| psd_covar | pcov | Signal Processing Toolbox™ |
| psd_mcovar | pmcov | Signal Processing Toolbox™ |
| psd_periodogram | periodogram | Signal Processing Toolbox™ |
| psd_welch | pwelch | Signal Processing Toolbox™ |
| psd_yule | pyulear | Signal Processing Toolbox™ |
| pspec_eign | peig | Signal Processing Toolbox™ |
| pspec_music | pmusic | Signal Processing Toolbox™ |
| pulsetrain | pulstran | Signal Processing Toolbox™ |
| pzgraph | pzmap | Control System Toolbox™ |
| qadm | qamdemod | Communications Toolbox™ |
| qam | qammod | Communications Toolbox™ |
| quadn_trap | trapz | MATLAB® |
| quantdecode | udecode | Signal Processing Toolbox™ |
| quantencode | uencode | Signal Processing Toolbox™ |
| rad_to_deg | rad2deg | MATLAB® |
| randnormal | randn | MATLAB® |
| randpermutation | randperm | MATLAB® |
| randss | rss | Control System Toolbox™ |
| randtf | tf | Control System Toolbox™ |
| randzpk | zpk | Control System Toolbox™ |
| rc_to_ac | rc2ac | Signal Processing Toolbox™ |
| rc_to_is | rc2is | Signal Processing Toolbox™ |
| rc_to_lar | rc2lar | Signal Processing Toolbox™ |
| rc_to_poly | rc2poly | Signal Processing Toolbox™ |
| rcepstrum | rceps | Signal Processing Toolbox™ |
| rcos | rcosine | Communications Toolbox™ |
| rectintarea | rectint | MATLAB® |
| rectpulse | rectpuls | Signal Processing Toolbox™ |
| ref_plotarea | gca | MATLAB® |
| ref_plotwin | gcf | MATLAB® |
| regex | regexp | MATLAB® |
| regex_convert | regexptranslate | MATLAB® |
| regex_i | regexpi | MATLAB® |
| regex_replace | regexprep | MATLAB® |
| regulator | reg | Control System Toolbox™ |
| remove_field | rmfield | MATLAB® |
| reorderdim | permute | MATLAB® |
| reorderdiminv | ipermute | MATLAB® |
| repeatmx | repmat | MATLAB® |
| resample_fir | upfirdn | Signal Processing Toolbox™ |
| reshapemx | reshape | MATLAB® |
| residuezd | residuez | Signal Processing Toolbox™ |
| reverse_vector | flip | MATLAB® |
| revlevinson | rlevinson | Signal Processing Toolbox™ |
| rgb_to_grayscale | rgb2gray | MATLAB® |
| rightdiv | rdivide | MATLAB® |
| rightdivmx | mrdivide | MATLAB® |
| rlocusfind | rlocfind | Control System Toolbox™ |
| root_eign | rooteig | Signal Processing Toolbox™ |
| root_music | rootmusic | Signal Processing Toolbox™ |
| rotate90 | rot90 | MATLAB® |
| rotateplane | planerot | MATLAB® |
| scatter3d | scatter3 | MATLAB® |
| selectdata | ginput | MATLAB® |
| semilog_x | semilogx | MATLAB® |
| semilog_y | semilogy | MATLAB® |
| sets_diff | setdiff | MATLAB® |
| sets_intersect | intersect | MATLAB® |
| sets_union | union | MATLAB® |
| sets_unique | unique | MATLAB® |
| sets_xor | setxor | MATLAB® |
| showplot | shg | MATLAB® |
| singularvalues | sigma | Control System Toolbox™ |
| sortconjugate | cplxpair | MATLAB® |
| sortdown | dsort | Control System Toolbox™ |
| sortdownreal | esort | Control System Toolbox™ |
| sos_to_ss | sos2ss | Signal Processing Toolbox™ |
| sos_to_tf | sos2tf | Signal Processing Toolbox™ |
| sos_to_zpk | sos2zp | Signal Processing Toolbox™ |
| soundscaled | soundsc | MATLAB® |
| spectrogram | specgram | Signal Processing Toolbox™ |
| sphere_to_cart | sph2cart | MATLAB® |
| splinefit | spline | MATLAB® |
| sqrtmx | sqrtm | MATLAB® |
| sqrtofreal | realsqrt | MATLAB® |
| ss_to_sos | ss2sos | Signal Processing Toolbox™ |
| ss_to_ss | ss2ss | Control System Toolbox™ |
| ss_to_tf | ss2tf | Control System Toolbox™ |
| ss_to_zpk | ss2zp | Control System Toolbox™ |
| stem3d | stem3 | MATLAB® |
| stepsignal | stepfun | Control System Toolbox™ |
| stepzd | stepz | Signal Processing Toolbox™ |
| str_to_double | str2double | MATLAB® |
| str_to_mx | str2mat | MATLAB® |
| str_to_num | str2num | MATLAB® |
| strcmp_i | strcmpi | MATLAB® |
| strcmp_n | strncmp | MATLAB® |
| strcmp_ni | strncmpi | MATLAB® |
| strconcat | strcat | MATLAB® |
| strfindall | strfind | MATLAB® |
| stripplot | strips | Signal Processing Toolbox™ |
| strjustify | strjust | MATLAB® |
| strmatchall | strmatch | MATLAB® |
| strreplace | strrep | MATLAB® |
| strtoken | strtok | MATLAB® |
| strtrimwhite | strtrim | MATLAB® |
| strvconcat | strvcat | MATLAB® |
| strvectorize | vectorize | MATLAB® |
| subspaceangle | subspace | MATLAB® |
| surface | surf | MATLAB® |
| surfacecontour | surfc | MATLAB® |
| surfacenorm | surfnorm | MATLAB® |
| sys_filter | filt | Control System Toolbox™ |
| sys_order1 | rss | Control System Toolbox™ |
| sys_order2 | rss | Control System Toolbox™ |
| tf_estimate | tfe | Signal Processing Toolbox™ |
| tf_estimateplot | tfestimate | Signal Processing Toolbox™ |
| tf_to_lattice | tf2latc | Signal Processing Toolbox™ |
| tf_to_sos | tf2sos | Signal Processing Toolbox™ |
| tf_to_ss | tf2ss | Control System Toolbox™ |
| tf_to_zpk | tf2zp | Control System Toolbox™ |
| tf_to_zpk_eqlen | tf2zpk | Signal Processing Toolbox™ |
| timerstart | tic | MATLAB® |
| timerstop | toc | MATLAB® |
| titles | title | MATLAB® |
| triangsearch | isinterior | MATLAB® |
| tripulse | tripuls | Signal Processing Toolbox™ |
| unwrapphase | unwrap | MATLAB® |
| updatechol | cholupdate | MATLAB® |
| uppercase | upper | MATLAB® |
| vandermonde | vander | MATLAB® |
| vconcatmx | vertcat | MATLAB® |
| view_image | imshow | MATLAB® |
| who_all | whos | MATLAB® |
| win_bartlett | bartlett | Signal Processing Toolbox™ |
| win_bartletthann | barthannwin | Signal Processing Toolbox™ |
| win_blackman | blackman | Signal Processing Toolbox™ |
| win_blackmanharris | blackmanharris | Signal Processing Toolbox™ |
| win_bohman | bohmanwin | Signal Processing Toolbox™ |
| win_cheby | chebwin | Signal Processing Toolbox™ |
| win_flattop | flattopwin | Signal Processing Toolbox™ |
| win_gauss | gausswin | Signal Processing Toolbox™ |
| win_hamming | hamming | Signal Processing Toolbox™ |
| win_hann | hann | Signal Processing Toolbox™ |
| win_hann2 | hanning | Signal Processing Toolbox™ |
| win_kaiser | kaiser | Signal Processing Toolbox™ |
| win_nuttall | nuttallwin | Signal Processing Toolbox™ |
| win_parzen | parzenwin | Signal Processing Toolbox™ |
| win_rect | rectwin | Signal Processing Toolbox™ |
| win_taylor | taylorwin | Signal Processing Toolbox™ |
| win_triangular | triang | Signal Processing Toolbox™ |
| win_tukey | tukeywin | Signal Processing Toolbox™ |
| xlabels | xlabel | MATLAB® |
| xlimit | xlim | MATLAB® |
| ylabels | ylabel | MATLAB® |
| ylimit | ylim | MATLAB® |
| zlimit | zlim | MATLAB® |
| zpk_to_sos | zp2sos | Signal Processing Toolbox™ |
| zpk_to_ss | zp2ss | Control System Toolbox™ |
| zpk_to_tf | zp2tf | Control System Toolbox™ |

Parent topic:

Interfaces for MATLAB

<!--NI_TOPIC bundle=labview-nxg-language-integration-api-overview path=migrate-to-interface-for-matlab.html language=enus -->
## TOPIC 00016: Migrating from MathScript Node to Interface for MATLAB

- bundle_id: `labview-nxg-language-integration-api-overview`
- source_path: `migrate-to-interface-for-matlab.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-language-integration-api-overview/raw/resource/enus/migrate-to-interface-for-matlab.html
- document_id: `labview-nxg-language-integration-api-overview`
- page_type: `leaf`
- content_type: `task`
- source_description: Use an Interface for MATLAB to migrate source code that contains a MathScript Node. When you open a VI containing a MathScript Node, the MathScript Node is replaced with a Sequence Structure and the original MathScript code is converted to a MATLAB file (.m). The VI is broken and you must modify the

Migrating from MathScript Node to Interface for MATLAB

Use an 
 *Interface for MATLAB* to migrate source code that contains a MathScript Node.

When you open a VI containing a MathScript Node, the MathScript Node is replaced with a Sequence Structure and the original MathScript code is converted to a MATLAB file (.m). The VI is broken and you must modify the code to replicate the behavior of the original code.

Complete the following steps to migrate your code:

1. Ensure that the generated MATLAB file works in MATLAB. 
 Refer to the comments in the Sequence Structure to locate the MATLAB file on disk. If the MATLAB file contains MathScript-specific function names, you must modify the file to use MATLAB function names. Refer to [Migrating MathScript Functions to MathWorks® Functions](/csh?topicname=mathscript-vs-matlab-function.html) for more information about mapping MathScript function names and their corresponding function names in MathWorks products.
2. [Create an Interface for MATLAB to call the MATLAB file](/csh?topicname=calling-matlab-functions-scripts.html). 
 org.dita.html5/xsl/topic.xsl 455Note 
 You must choose 
 Function as the 
 File type on the 
 Document tab because the generated MATLAB file is a function.
 You must configure parameters of the interface node using consistent input/output arguments in the MATLAB file. Find input/output arguments of the MATLAB file from comments in the Sequence Structure.
3. Return to the VI diagram and rewire controls and indicators to the interface node.
  1. Click 
 Project Files»Software, select the interface node, and drop the interface node on the diagram.
  2. Wire controls and indicators to the interface node by replicating wire connections to the Sequence Structure.
  3. Remove the Sequence Structure and clean up the diagram.
  4. Save the VI.

Notice that the VI is no longer broken. The modified code has the same behavior as the original code.

Parent topic:

Interfaces for MATLAB

<!--NI_TOPIC bundle=labview-nxg-language-integration-api-overview path=migrating-to-a-shared-library-interface.html language=enus -->
## TOPIC 00017: Migrating to a Shared Library Interface

- bundle_id: `labview-nxg-language-integration-api-overview`
- source_path: `migrating-to-a-shared-library-interface.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-language-integration-api-overview/raw/resource/enus/migrating-to-a-shared-library-interface.html
- document_id: `labview-nxg-language-integration-api-overview`
- page_type: `leaf`
- content_type: `task`
- source_description: Use the Code Conversion Utility to convert Call Library Function Node (CLFN) configurations to a Shared Library Interface. For more information on migrating LabVIEW source code to LabVIEW NXG, refer to the migration help. Run the Code Conversion Utility to migrate the entire project. The utility aut

Migrating to a Shared Library Interface

Use the 
 **Code Conversion Utility** to convert Call Library Function Node (CLFN) configurations to a Shared Library Interface.

Note

1. Run the 
 Code Conversion Utility to migrate the entire project. 
 The utility automatically converts your CLFNs into an SLI document. The Code Conversion utility will combine CLFNs that reference the same Shared Library into a single SLI. A reference to an SLI replaces each CLFN on the diagram.
2. Locate the new SLI document in the 
 Project Files tab and ensure all functions converted correctly.

#### Example

Search within the programming environment to access the following installed example:
 *External Code (DLL) Execution*.

Parent topic:

Shared Library Interfaces

<!--NI_TOPIC bundle=labview-nxg-language-integration-api-overview path=shared-library-best-practices.html language=enus -->
## TOPIC 00018: Shared Library Best Practices

- bundle_id: `labview-nxg-language-integration-api-overview`
- source_path: `shared-library-best-practices.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-language-integration-api-overview/raw/resource/enus/shared-library-best-practices.html
- document_id: `labview-nxg-language-integration-api-overview`
- page_type: `leaf`
- content_type: `concept`
- source_description: Prepare your shared library to minimize errors when using a Shared Library Interface (SLI). When implementing an SLI, ensure the following: Your entry point is exported from the shared library. For example, in a C++ library, declare the functions you want to use with the _declspec (dllexport) keywor

Shared Library Best Practices

Prepare your shared library to minimize errors when using a Shared Library Interface (SLI).

- Your entry point is exported from the
 shared library. For example, in a C++ library, declare the functions you want to
 use with the _declspec (dllexport) keyword in the header file
 and the source code, or define them in the EXPORTS section of
 the module definition file.
- The C++ compiler has not decorated the
 function name. Name decoration doesn't cause any technical problems, but can
 make your code less clear to read. Use the C++ compiler function export
 directive, extern "C"{} , in your header file, as shown in the
 following example code:
 extern "C" {
/* your function prototypes here */
}
- All applications that use the shared
 library are unloaded from memory before recompiling the shared library. This
 ensures the shared library itself is not loaded into memory when recompiling.
 For example, if you are using a shared library in your VI, you must close the
 entire project before recompiling your shared library.

Note

Parent topic:

Shared Library Interfaces

<!--NI_TOPIC bundle=labview-nxg-language-integration-api-overview path=shared-library-interface-best-practices.html language=enus -->
## TOPIC 00019: Shared Library Interface Best Practices

- bundle_id: `labview-nxg-language-integration-api-overview`
- source_path: `shared-library-interface-best-practices.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-language-integration-api-overview/raw/resource/enus/shared-library-interface-best-practices.html
- document_id: `labview-nxg-language-integration-api-overview`
- page_type: `leaf`
- content_type: `concept`
- source_description: Prepare your Shared Library Interface (SLI) to minimize errors when calling external code. When implementing an SLI, ensure the following: The SLI has the correct name or path for the shared library. If you specify a shared library using a path, the path is absolute. If you specify a shared library

Shared Library Interface Best Practices

Prepare your Shared Library Interface (SLI) to minimize errors when calling external code.

- The SLI has the correct name or path for the shared library.
- If you specify a shared library using a path, the path is absolute.
- If you specify a shared library using a name, the library is located in the system search path.
- All parameters are defined to be passed by the correct method, such as value or pointer.
- The SLI passes arguments to the function in the correct order.
- If you are moving a VI that uses an SLI to another platform, you have updated the SLI to specify the version of the shared library that is compiled for the new platform.

If your SLI handles arrays or strings of data, ensure the following:

- You pass a buffer or array that is large enough to hold any results that the function places in the buffer.
- If you are passing arrays or strings as LabVIEW NXG handles, you use Manager functions to resize them under Visual C++ or Xcode compilers.
- Pascal strings do not exceed 255 characters in length.

Note

Parent topic:

Shared Library Interfaces

<!--NI_TOPIC bundle=labview-nxg-language-integration-api-overview path=shared-library-interfaces.html language=enus -->
## TOPIC 00020: Shared Library Interfaces

- bundle_id: `labview-nxg-language-integration-api-overview`
- source_path: `shared-library-interfaces.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-language-integration-api-overview/raw/resource/enus/shared-library-interfaces.html
- document_id: `labview-nxg-language-integration-api-overview`
- page_type: `leaf`
- content_type: `concept`
- source_description: When you want to use code from another programming language, such as C, in your G Dataflow application, you use a Shared Library Interface (SLI). An SLI is a file in which you define calls to a shared library. An SLI connects your G Dataflow application to a shared library which contains executable

Shared Library Interfaces

When you want to use code from another programming language, such as C, in your G Dataflow application, you use a 
 *Shared Library Interface (SLI)*. An SLI is a file in which you define calls to a shared library.

An SLI connects your G Dataflow application to a shared library which contains executable programming modules written in another programming language. Use an SLI in your application to create 
 *entry points*, or defined calls, to these portions of external code.

Visual representations of entry points appear on the software palette on the diagram. You can place and wire entry points like nodes.

As the application executes, the SLI calls the function in the external code. Input data passes from the diagram to the external code, and data returns from the external code to the diagram.

#### Shared Library Terminology on Different Operating Systems

Use the following table to determine what a shared library is called on your operating system.

| Operating System | Terminology |
| --- | --- |
| Windows | DLL |
| Linux | Shared library |
| OS X | Dynamic library |

#### Example

Search within the programming environment to access the following installed example:
 *External Code (DLL) Execution*.

Parent topic:

Language Integration in G
