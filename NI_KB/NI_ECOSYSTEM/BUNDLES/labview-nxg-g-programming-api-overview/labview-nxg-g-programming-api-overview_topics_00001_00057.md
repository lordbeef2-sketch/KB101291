# NI DOCUMENT BUNDLE: labview-nxg-g-programming-api-overview

<!--NI_BUNDLE_CHUNK bundle=labview-nxg-g-programming-api-overview start=1 end=57 -->
<!--NI_TOPIC bundle=labview-nxg-g-programming-api-overview path=accessing-data-from-previous-loop-iteration.html language=enus -->
## TOPIC 00001: Accessing Data from the Previous Loop Iteration

- bundle_id: `labview-nxg-g-programming-api-overview`
- source_path: `accessing-data-from-previous-loop-iteration.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-g-programming-api-overview/raw/resource/enus/accessing-data-from-previous-loop-iteration.html
- document_id: `labview-nxg-g-programming-api-overview`
- page_type: `leaf`
- content_type: `task`
- source_description: After a loop completes a single iteration, sometimes you want to use the value of one of its calculations in the next loop iteration. You can use a shift register to pass data from the most recent iteration to the next iteration. What to Use For Loop or While Loop Shift register What to Do Create th

Accessing Data from the Previous Loop Iteration

After a loop completes a single iteration, sometimes you want to use the value of one of its calculations in the next loop iteration. You can use a shift register to pass data from the most recent iteration to the next iteration.

#### What to Use

- For Loop or While Loop
- Shift register

#### What to Do

Create the following diagram to pass data from the most recent loop iteration to the next iteration.

Customize the gray sections for your unique programming goals.

[IMAGE alt='1378' src='GUID-FE5D4487-4136-40C2-B219-84990BFF4478-a5.png']

|  | To share data with the next loop iteration, pass the data into a shift register on the right border of the loop. This right shift register passes that data to a corresponding left shift register. To create a pair of shift registers, right-click the loop border and select Create Shift Register. |
| --- | --- |
|  | The left shift register contains data passed from the right shift register. Access this data by wiring the output of the left shift register to the code inside the loop. |
|  | For the first loop iteration, an initialized shift register returns the value wired to its input. If you do not initialize the shift register, it shares the data it held the last time the loop executed, even if that data is from a previous execution of the VI containing the loop. |
|  | After the loop executes, access the data from the last iteration by wiring the output of the right shift register to the rest of the program. Only values from the last iteration exit the loop through the output of the right shift register. |

#### Examples

In the previous example, the value the left shift register passes into the loop changes after each iteration. The following table records the data each shift register contains after each loop iteration if the 
 initial value wired to the left shift register is 10 and the 
 loop count is 3.

| Shift Register | Value after First Iteration | Value after Second Iteration | Value after Third Iteration |
| --- | --- | --- | --- |
| Left shift register | 10 | 15 | 20 |
| Right shift register | 15 | 20 | 25 |

Parent topic:

Repeating Operations

Related tasks:

- Accessing Data from Multiple Past Loop Iterations

<!--NI_TOPIC bundle=labview-nxg-g-programming-api-overview path=adjusting-execution-speed.html language=enus -->
## TOPIC 00002: Adjusting the Execution Speed of a Loop

- bundle_id: `labview-nxg-g-programming-api-overview`
- source_path: `adjusting-execution-speed.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-g-programming-api-overview/raw/resource/enus/adjusting-execution-speed.html
- document_id: `labview-nxg-g-programming-api-overview`
- page_type: `leaf`
- content_type: `task`
- source_description: By default, each loop iteration executes as quickly as possible based on the code inside the loop. However, you might want to control the rate at which a loop executes in order to specify a fixed time interval for each iteration, reduce the speed at which an indicator changes value, or conserve proc

Adjusting the Execution Speed of a Loop

By default, each loop iteration executes as quickly as possible based on the code inside the loop.

#### What to Use

- While Loop or For Loop
- Wait

#### What to Do

Create the following diagram to adjust the execution speed of a loop.

Customize the gray sections for your unique programming goals.

[IMAGE alt='1378' src='GUID-7C24DA22-841F-43AD-A7DC-B54E3F3AFA81-a5.png']

|  | Place the code you want to repeat on the subdiagram of a While Loop or For Loop. |
| --- | --- |
|  | To specify the amount of time to wait between loop iterations, wire the desired time duration to the input of the Wait node. The Wait node waits until the value of the operating system's counter increases by an amount equal to the input you specify. The total running time of the loop is equal to the greater of the time it takes to run the code inside the loop and the wait time you specify. |
|  | Pressing the stop button does not interrupt the Wait node. For example, if the user presses the stop button in the middle of a loop iteration, the While Loop stops only after the specified wait period has elapsed and the code inside the loop has finished executing. |

#### Troubleshooting

If a loop does not execute at the desired rate, verify that you have specified the input of the Wait node correctly. Consider the following common mistakes:

- If you are converting from another unit of time, verify that your conversion calculation is correct.
- If your code takes longer than expected to execute, note that the total running time of the loop is equal to the greater of the time it takes to run the code inside the loop and the wait time you specify.

Parent topic:

Repeating Operations

Related concepts:

- Loop Timing

<!--NI_TOPIC bundle=labview-nxg-g-programming-api-overview path=api-design.html language=enus -->
## TOPIC 00003: API Design for Distributed APIs

- bundle_id: `labview-nxg-g-programming-api-overview`
- source_path: `api-design.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-g-programming-api-overview/raw/resource/enus/api-design.html
- document_id: `labview-nxg-g-programming-api-overview`
- page_type: `leaf`
- content_type: `reference`
- source_description: Refer to the following table for best practices for designing VIs. Guideline Required or Recommended? Details Example(s) Include every public VI in your API in the API palette. Required Users may not look on disk to find advanced VIs. If a VI is not ready or intended for public consumption, make the

API Design for Distributed APIs

Refer to the following table for best practices for designing VIs.

| Guideline | Required or Recommended? | Details | Example(s) |
| --- | --- | --- | --- |
| Include every public VI in your API in the API palette. | Required | Users may not look on disk to find advanced VIs. If a VI is not ready or intended for public consumption, make the VI private in the API component. | N/A |
| Do not use a VI in your API to open a dialog box unless that is the stated intent of the VI. | Required | N/A | N/A |
| If you expect multiple calls of your API VI to run in parallel, consider making the VI reentrant. | Recommended | If the VI stores any internal state in feedback nodes or uninitialized shift registers, make the VI reentrant and stateful, such as a preallocated clone. If the VI doesn't store any internal state, make it stateless, as a shared clone. | N/A |

Parent topic:

Best Practices for Designing and Developing an Application Programming Interface (API) in G Web Development Software

Related concepts:

- Best Practices for Designing and Developing an Application Programming Interface (API) in G Web Development Software

Related reference:

- File Organization and Node Naming for Distributed APIs
- Component Organization for Distributed APIs
- Icons and Connector Panes for Distributed APIs
- Panel Design for Distributed APIs
- Data Type Selection for Distributed APIs
- Palette Taxonomy for Distributed APIs
- Documentation for Distributed APIs
- Error Message Design for Distributed APIs

<!--NI_TOPIC bundle=labview-nxg-g-programming-api-overview path=best-practices-api.html language=enus -->
## TOPIC 00004: Best Practices for Designing and Developing an Application Programming Interface (API) in G Web Development Software

- bundle_id: `labview-nxg-g-programming-api-overview`
- source_path: `best-practices-api.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-g-programming-api-overview/raw/resource/enus/best-practices-api.html
- document_id: `labview-nxg-g-programming-api-overview`
- page_type: `leaf`
- content_type: `concept`
- source_description: To develop an API to distribute to other users that is consistent with NI style recommendations for G content, refer to the following best practice guidelines: File Organization and Node Naming Component Organization Icons and Connector Panes Panel Design Data Type Selection Palette Taxonomy Documen

Best Practices for Designing and Developing
 an Application Programming Interface (API) in G Web Development Software

To develop an API to distribute to other users that is consistent with NI style recommendations for G content, refer to the following best practice guidelines:

- File
 Organization and Node Naming
- Component
 Organization
- Icons and
 Connector Panes
- Panel Design
- Data Type
 Selection
- Palette Taxonomy
- Documentation
- Error Message Design
- API Design

You also need to follow the [Best Practices for Designing and Developing Projects in G Web Development
 Software](design-develop-projects-g.html#GUID-F4891E5A-257C-40E4-9C2B-F15FE31BAD62) if you want your API to be consistent with NI best practice
 recommendations for G content.

Throughout this section, the term 
 *required* refers to a guideline that NI requires when designing an API. The term 
 *recommended* refers to a guideline that NI suggests when designing an API.

Parent topic:

Programming in G

Related reference:

- File Organization and Node Naming for Distributed APIs
- Component Organization for Distributed APIs
- Icons and Connector Panes for Distributed APIs
- Panel Design for Distributed APIs
- Data Type Selection for Distributed APIs
- Palette Taxonomy for Distributed APIs
- Documentation for Distributed APIs
- Error Message Design for Distributed APIs
- API Design for Distributed APIs

<!--NI_TOPIC bundle=labview-nxg-g-programming-api-overview path=component-organization-api.html language=enus -->
## TOPIC 00005: Component Organization for Distributed APIs

- bundle_id: `labview-nxg-g-programming-api-overview`
- source_path: `component-organization-api.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-g-programming-api-overview/raw/resource/enus/component-organization-api.html
- document_id: `labview-nxg-g-programming-api-overview`
- page_type: `leaf`
- content_type: `reference`
- source_description: Refer to the following table for best practices for organizing components. Guideline Required or Recommended? Details Set the Exported or Non-exported designation of the VIs in your API appropriately. Required The Exported designation indicates to users which VIs are guaranteed to have a consistent

Component Organization for Distributed APIs

Refer to the following table for best practices for organizing components.

| Guideline | Required or Recommended? | Details |
| --- | --- | --- |
| Set the Exported or Non-exported designation of the VIs in your API appropriately. | Required | The Exported designation indicates to users which VIs are guaranteed to have a consistent interface. |
| Mark a VI as Exported only if it is a public member of your API. | Required | Mark a VI as Exported. |
| If a G Type is on the connector pane of an exported VI in your API, also mark that G Type Exported. | Required | N/A |
| Follow the namespacing guideline [Company].[Product].[Component].gcomp for your API component. | Required | For example, NI.G Core.Data Type.gcomp is a component NI owns, part of the G Core product (in other words, the core libraries that compose the G language), and these VIs pertain to parsing Data Types. |

Parent topic:

Best Practices for Designing and Developing an Application Programming Interface (API) in G Web Development Software

Related concepts:

- Best Practices for Designing and Developing an Application Programming Interface (API) in G Web Development Software

Related reference:

- File Organization and Node Naming for Distributed APIs
- Icons and Connector Panes for Distributed APIs
- Panel Design for Distributed APIs
- Data Type Selection for Distributed APIs
- Palette Taxonomy for Distributed APIs
- Documentation for Distributed APIs
- Error Message Design for Distributed APIs
- API Design for Distributed APIs

<!--NI_TOPIC bundle=labview-nxg-g-programming-api-overview path=computational-units.html language=enus -->
## TOPIC 00006: Nodes: Computational Units

- bundle_id: `labview-nxg-g-programming-api-overview`
- source_path: `computational-units.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-g-programming-api-overview/raw/resource/enus/computational-units.html
- document_id: `labview-nxg-g-programming-api-overview`
- page_type: `leaf`
- content_type: `concept`
- source_description: Nodes are objects on the diagram that accept inputs, return outputs, and perform operations when a program runs. They are analogous to statements, operators, functions, and subroutines in text-based programming languages.

Nodes: Computational Units

Nodes are objects on the diagram that accept inputs, return outputs, and perform operations when a program runs.

They are analogous to statements, operators, functions, and subroutines in text-based programming languages.

[IMAGE alt='1378' src='GUID-DD0CDE2C-C5AA-409D-A4A7-82C707F350BC-a5.png']

Parent topic:

Programming in G

<!--NI_TOPIC bundle=labview-nxg-g-programming-api-overview path=connecting-to-a-database-using-dsns.html language=enus -->
## TOPIC 00007: Connecting to a Database Using Data Source Names

- bundle_id: `labview-nxg-g-programming-api-overview`
- source_path: `connecting-to-a-database-using-dsns.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-g-programming-api-overview/raw/resource/enus/connecting-to-a-database-using-dsns.html
- document_id: `labview-nxg-g-programming-api-overview`
- page_type: `leaf`
- content_type: `task`
- source_description: Establish a connection with a database using Open Database Connectivity (ODBC) protocols. Use the ODBC Data Source Administrator dialog box to register and configure drivers to make them available as data sources. In the Windows Control Panel, select Administrative ToolsODBC Data Sources to configur

Connecting to a Database Using Data Source
 Names

Establish a connection with a database using Open Database Connectivity (ODBC)
 protocols.

1. Use the ODBC Data Source Administrator dialog box to register and
 configure drivers to make them available as data sources. In the Windows Control Panel,
 select Administrative Tools»ODBC Data Sources to configure a data source name connection.
2. Place an Open Connection node in your code.
3. Use a string or a path to specify the DSN you created, and wire it to the
 connection information input.

- Verify the requested server is running.
- Verify the network is running.
- Verify there are available server connections.
- Verify with your administrator whether the maximum number of user licenses has been
 reached.
- Check whether you have permission to access the specified database.
- Check whether the specified DSN exists.
- Select the correct provider for a database. You must create a DSN to connect to a
 database that uses ODBC, while you must use a UDL to connect to databases that use ADO
 and OLE DB.

Note

Parent topic:

Database Connectivity

<!--NI_TOPIC bundle=labview-nxg-g-programming-api-overview path=connecting-to-a-database-with-a-udl.html language=enus -->
## TOPIC 00008: Connecting to a Database with a Universal Data Link

- bundle_id: `labview-nxg-g-programming-api-overview`
- source_path: `connecting-to-a-database-with-a-udl.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-g-programming-api-overview/raw/resource/enus/connecting-to-a-database-with-a-udl.html
- document_id: `labview-nxg-g-programming-api-overview`
- page_type: `leaf`
- content_type: `task`
- source_description: Establish a connection with a database using Microsoft ActiveX Data Object (ADO) protocols. Connect a True constant to the prompt? input of the Open Connection node. The prompt? input displays the Data Link Properties dialog box when you run your code. Configure your data connection by selecting the

Connecting to a Database with a Universal Data
 Link

Establish a connection with a database using Microsoft ActiveX Data Object (ADO)
 protocols.

1. Connect a True constant to the
 prompt? input of the Open
 Connection node. The prompt? input
 displays the Data Link Properties dialog box when you run
 your code. Configure your data connection by selecting the available options in
 the dialog box.
2. In Windows Explorer, right-click an empty location in a folder and select New»Text Document from the short-cut menu. Change the file extension of this
 document from .txt to .udl.
3. Use a path control to specify the path to your UDL file.
 Use the path created in step 2.

- Verify the requested server is running.
- Verify the network is running.
- Verify there are available server connections.
- Verify with your administrator whether the maximum number of user licenses
 has been reached.
- Check whether you have permission to access the specified database.
- Check whether the specified UDL exists.
- Select the correct provider for a database. You must create a DSN to connect
 to a database that uses ODBC, while you must use a UDL to connect to
 databases that use ADO and OLE DB.

Parent topic:

Database Connectivity

<!--NI_TOPIC bundle=labview-nxg-g-programming-api-overview path=constants.html language=enus -->
## TOPIC 00009: Constants

- bundle_id: `labview-nxg-g-programming-api-overview`
- source_path: `constants.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-g-programming-api-overview/raw/resource/enus/constants.html
- document_id: `labview-nxg-g-programming-api-overview`
- page_type: `leaf`
- content_type: `concept`
- source_description: A constant is a fixed piece of data that exists only on the diagram. Use a constant instead of a control when you know that a certain piece of data should always be the same regardless of other parts of your code. You can use the following types of constants in graphical programming: Universal const

Constants

A constant is a fixed piece of data that exists only on the diagram. Use a constant instead of a control when you know that a certain piece of data should always be the same regardless of other parts of your code.

You can use the following types of constants in graphical programming:

Universal constant

User-defined constant

Parent topic:

Programming in G

<!--NI_TOPIC bundle=labview-nxg-g-programming-api-overview path=controlling-timing-in-a-loop.html language=enus -->
## TOPIC 00010: Loop Timing

- bundle_id: `labview-nxg-g-programming-api-overview`
- source_path: `controlling-timing-in-a-loop.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-g-programming-api-overview/raw/resource/enus/controlling-timing-in-a-loop.html
- document_id: `labview-nxg-g-programming-api-overview`
- page_type: `leaf`
- content_type: `concept`
- source_description: Loop timing refers to how long a loop takes to execute a single iteration. The amount and type of code a loop contains affects its execution speed. By default, each loop iteration executes as quickly as possible based on the code inside the loop. However, you might want to change the execution speed

Loop Timing

Loop timing refers to how long a loop takes to execute a single iteration. The amount and type of code a loop contains affects its execution speed.

By default, each loop iteration executes as quickly as possible based on the code inside the loop.
 However, you might want to change the execution speed of a loop for one or more of the following reasons.

| Reason to Control Loop Timing | Example Application | Procedure |
| --- | --- | --- |
| You want to repeat the code inside a loop and specify a fixed time interval for each iteration. | Take a temperature measurement every 10 minutes. | Adjusting the Execution Speed of a Loop |
| You want to reduce the execution speed of a loop to make the result of each iteration more easily visible, as seen through indicators on the panel. | Control the rate at which data values are plotted to a chart. |  |
| Instead of allowing a loop to execute at full speed, potentially taking full control of all of the CPU's resources, you want to conserve processing resources for other tasks. | Yield control of the CPU to allow other threads, such as serial or VISA calls, access to processor resources while the loop waits. |  |
| You want to synchronize the execution of multiple loops. | Two loops contain sections of code that take different amounts of time to run. Synchronize these loops to the system clock so that they begin each iteration at the same time. | Synchronizing the Execution of Multiple Loops |

Parent topic:

Repeating Operations

Related tasks:

- Adjusting the Execution Speed of a Loop
- Synchronizing the Execution of Multiple Loops

Related information:

- nihelp://node-ref/for-loop/
- nihelp://node-ref/while-loop/
- nihelp://node-ref/wait/
- nihelp://node-ref/wait-until-next-multiple/

<!--NI_TOPIC bundle=labview-nxg-g-programming-api-overview path=create-plugin-test-app.html language=enus -->
## TOPIC 00011: Creating a Plugin-Based Test Application

- bundle_id: `labview-nxg-g-programming-api-overview`
- source_path: `create-plugin-test-app.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-g-programming-api-overview/raw/resource/enus/create-plugin-test-app.html
- document_id: `labview-nxg-g-programming-api-overview`
- page_type: `leaf`
- content_type: `task`
- source_description: Use Execution Control nodes to create an extensible application. Extend your application so you can add components, such as plugins, to it after you build it. A plugin is a library component that has Identify library as a plugin enabled in its metadata. What to Use Open Component Reference Component

Creating a Plugin-Based Test
 Application

Use [Execution Control](/csh?topicname=execution-control-nodes.html) nodes to create an extensible application. Extend your
 application so you can add components, such as plugins, to it after you build
 it.

Note

Identify library as a plugin

#### What to Use

- Open Component Reference
- Component Reference
 Properties
- Open VI Reference
- Call By Reference
- Close Reference

#### What to Do

Create the following diagram to make a plugin-based test application.

Customize the gray sections for your unique programming goals.

[IMAGE alt='1378' src='GUID-2EC6A660-6B09-44DE-8F76-EAFC3E9E4269-a5.png']

|  | Open Component Reference returns a reference to a library component (or GLL) you specify with a name string. Note Do not include the file extension in the component name string. |
| --- | --- |
|  | Component Reference properties reads the properties of a component reference you open with Open Component Reference. Wire the appropriate data type terminals to Component Information and Plugin? to review component metadata and determine whether the component is a plugin. Wire the Exports terminal to vi name in Open VI Reference to iterate over and run the exported VIs in the plugin. |
|  | Open VI Reference returns a reference to a VI you specify with a name string. Wire component reference to open a VI from a specific library. Note You must wire a strictly typed VI reference to type specifier VI reference. The connector pane of the VI specified by vi name must match the connector pane of the VI wired to type specifier VI reference. |
|  | Close Reference closes a reference to an open VI. |
|  | Close Reference closes a reference to an open component. |

#### Troubleshooting

- Make sure the connector pane of each exported VI in
 your component matches the connector pane of the type specifier VI
 reference . Refer to the Details tab of the Open VI Reference node for criteria for
 opening strictly typed reference.
- Make sure the expected plugins have
 Identify library as a plugin enabled in the metadata.
 To identify library component as a plugin, open the Library document and enable
 the Identify library as a plugin option from the
 Document tab.

Parent topic:

Programming in G

<!--NI_TOPIC bundle=labview-nxg-g-programming-api-overview path=creating-a-multi-mode-element.html language=enus -->
## TOPIC 00012: Creating a Multi-Mode Element

- bundle_id: `labview-nxg-g-programming-api-overview`
- source_path: `creating-a-multi-mode-element.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-g-programming-api-overview/raw/resource/enus/creating-a-multi-mode-element.html
- document_id: `labview-nxg-g-programming-api-overview`
- page_type: `leaf`
- content_type: `task`
- source_description: Create a Multi-Mode Element to manually determine how a node should behave on your diagram. In an open project, select FilePreferences and click Preview features. Check the Enable Multi-Mode Elements and overload groups and click OK. Click Yes to restart LabVIEW NXG. When LabVIEW NXG launches, open

Creating a Multi-Mode Element

Create a Multi-Mode Element to manually determine how a node should behave on your
 diagram.

1. In an open project, select File»Preferences and click Preview features.
2. Check the Enable Multi-Mode Elements and overload groups
 and click OK.
3. Click Yes to restart LabVIEW NXG.
4. When LabVIEW NXG launches, open your project.
5. To create a Multi-Mode Element, select File»New»Multi-Mode Element. 
 A Multi-Mode Element document (.gmme) opens in your
 project.
6. Create categories within the document by clicking the New
 Category button. If you need to remove a category, select that
 category, and click Delete.
7. From the palette, select Project Items»Software and select the VI you want to add to a category. 
 org.dita.html5/xsl/topic.xsl 455Note To add multiple VIs to a category, press and hold Ctrl as you select the
 VIs from the Software palette.Furthermore, if
 the Project Items palette doesn't appear, you
 need to add VIs to your project.
8. Enter names for the categories and modes in the Configuration pane.
9. Open a new VI and place one of the VIs you added to your Multi-Mode Element
 document on the diagram. 
 A drop-down appears and allows you to select which category and node to
 use from the Multi-Mode Element.

Parent topic:

Multi-Mode Element and Overload Group Behavior

Related tasks:

- Preview Features

<!--NI_TOPIC bundle=labview-nxg-g-programming-api-overview path=creating-an-overload-group.html language=enus -->
## TOPIC 00013: Creating an Overload Group

- bundle_id: `labview-nxg-g-programming-api-overview`
- source_path: `creating-an-overload-group.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-g-programming-api-overview/raw/resource/enus/creating-an-overload-group.html
- document_id: `labview-nxg-g-programming-api-overview`
- page_type: `leaf`
- content_type: `task`
- source_description: Overload groups determine how a node should automatically behave based on how you connect different data types to it in your diagram. In an open project, select FilePreferences and click Preview features. Check the Enable Multi-Mode Elements and overload groups and click OK. Click Yes to restart Lab

Creating an Overload Group

Overload groups determine how a node should automatically behave based on how you
 connect different data types to it in your diagram.

1. In an open project, select File»Preferences and click Preview features.
2. Check the Enable Multi-Mode Elements and overload groups
 and click OK.
3. Click Yes to restart LabVIEW NXG.
4. When LabVIEW NXG launches, open your project.
5. Select a node you want to add to the overload group.
6. In the Document tab, expand
 Behavior and enter a name for the overload
 group. 
 org.dita.html5/xsl/topic.xsl 455Note Overload groups work best when the individual nodes included have all but
 one parameter in common. If the node parameter configurations are
 significantly different, the algorithm which evaluates the overload group
 may not behave the way you expect.
7. Repeat this for all nodes you want to add to the overload group.
8. Connect a wire to a node on your diagram that belongs to an overload group,
 LabVIEW NXG evaluates whether the node on the diagram is the best match for the
 wired connection. 
 org.dita.html5/xsl/topic.xsl 455Note If LabVIEW determines that
 another node in the overload group is a better match, it will automatically
 switch the node in the diagram to that node.

Parent topic:

Multi-Mode Element and Overload Group Behavior

Related tasks:

- Preview Features

<!--NI_TOPIC bundle=labview-nxg-g-programming-api-overview path=creating-timing-source.html language=enus -->
## TOPIC 00014: Creating a Timing Source for a Timed Loop

- bundle_id: `labview-nxg-g-programming-api-overview`
- source_path: `creating-timing-source.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-g-programming-api-overview/raw/resource/enus/creating-timing-source.html
- document_id: `labview-nxg-g-programming-api-overview`
- page_type: `leaf`
- content_type: `task`
- source_description: A timing source controls the execution of a Timed Loop. Open or create a VI that includes at least one Timed Loop on the diagram. Add Create Timing Source to the diagram. Configure the type and rate of the timing source using the pull-down menus that appear. Type Description Built-In A timing source

Creating a Timing Source for a Timed Loop

A timing source controls the execution of a Timed Loop.

1. Open or create a VI that includes at least one Timed Loop on the diagram.
2. Add Create Timing Source to the diagram. Configure the type and rate of the timing source using the pull-down menus that appear. 
 TypeDescriptionBuilt-In
 A timing source that controls a Timed Loop using an internal clock. You can choose from the following built-in timing sources:
 **1 kHz Clock**—A clock that allows you to schedule a Timed Loop with millisecond resolution. By default, a Timed Loop uses the 1 kHz clock of the operating system as a timing source.
 **1 MHz Clock**—A clock that allows you to schedule a Timed Loop with microsecond resolution. If the controller does not support microsecond resolution due to processor or operating system limitations, the 1 MHz clock is not available.
 
 org.dita.html5/xsl/topic.xsl 455Note You can also select a built-in timing source by selecting the Timing Source border node on the Timed Loop and choosing a timing source in the 
 Item tab.Software-Triggered
 A timing source that triggers the start of a timed structure based on a software-defined event. You can use a software-triggered timing source for the following applications:
 As a real-time-compatible event handler.
 To notify a consumer Timed Loop when new data becomes available within a producer-consumer application.
 For discrete event simulation.
 org.dita.html5/xsl/topic.xsl 455Note Use Fire Software-Triggered Timing Source to specify the number of ticks that elapse between each event.
3. Wire timing source name of Create Timing Source to source in on the Timing Source border node of any Timed Loop that you want to control with the timing source you created.

Parent topic:

Repeating Operations

<!--NI_TOPIC bundle=labview-nxg-g-programming-api-overview path=data-type-selection-api.html language=enus -->
## TOPIC 00015: Data Type Selection for Distributed APIs

- bundle_id: `labview-nxg-g-programming-api-overview`
- source_path: `data-type-selection-api.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-g-programming-api-overview/raw/resource/enus/data-type-selection-api.html
- document_id: `labview-nxg-g-programming-api-overview`
- page_type: `leaf`
- content_type: `reference`
- source_description: Refer to the following table for best practices for selecting data types. Guideline Required or Recommended? Details Example(s) For numeric input or output values, use double-precision for floating-point values and I32 for integer values unless there is a specific reason to use another type. Require

Data Type Selection for Distributed APIs

Refer to the following table for best practices for selecting data types.

| Guideline | Required or Recommended? | Details | Example(s) |
| --- | --- | --- | --- |
| For numeric input or output values, use double-precision for floating-point values and I32 for integer values unless there is a specific reason to use another type. | Required | N/A | N/A |
| Always use an error cluster for reporting error conditions. Never use an error code or error Boolean output by itself. | Required | G Web Development Software has a single Error API for error handling. If API VIs do not use the error cluster to convey error information, you cannot use the Error API for handling errors. | N/A |
| Use a text ring only for parameters that have a natural association to several discrete possibilities and no numeric content. | Recommended | An exception for numeric content is if the set of valid values is sufficiently small. | Examples of discrete possibilities without numeric content are days of the week, months of the year, make and model of car. An example of numeric content that would be an exception is the number of connected devices within a finite number of connections. It's better for a user to pick a value of 0, 1, 2, 3 from a ring control than to instead have a numeric control and need to make sure the specified value is in range. |
| If you use text rings for numeric content, do not create an item with text that represents a different numeric value. | Recommended | N/A | For example, a selection of 2 assigned to the value 0 could confuse the user. |
| Use the timestamp data type for time values in your API. | Recommended | N/A | N/A |
| Use a double-precision value to specify the number of seconds for timeout values in your API. Use -1 to indicate that the diagram object has no timeout limit. | Recommended | N/A | N/A |
| Use the waveform data type when your VI acquires or generates analog waveforms. | Recommended | N/A | N/A |
| If your VI has a string input or output, consider whether another data type, such as an enum, might make your API easier to use. | Recommended | N/A | If the user needs to pick a day of the week, an enum with the seven days in it is easier to use than typing the name of the day as a string, because of possible problems with the case, spelling, and abbreviation. |
| If you use a cluster as an input or output of your VI, make sure the cluster logically groups parameters. | Recommended | Do not use clusters only to reduce the number of inputs and outputs on your VI, because clustering things unnecessarily to reduce the number of inputs to the VI is not a logical organization. | N/A |

Parent topic:

Best Practices for Designing and Developing an Application Programming Interface (API) in G Web Development Software

Related concepts:

- Best Practices for Designing and Developing an Application Programming Interface (API) in G Web Development Software

Related reference:

- File Organization and Node Naming for Distributed APIs
- Component Organization for Distributed APIs
- Icons and Connector Panes for Distributed APIs
- Panel Design for Distributed APIs
- Palette Taxonomy for Distributed APIs
- Documentation for Distributed APIs
- Error Message Design for Distributed APIs
- API Design for Distributed APIs

<!--NI_TOPIC bundle=labview-nxg-g-programming-api-overview path=database-connectivity-toolkit.html language=enus -->
## TOPIC 00016: Database Connectivity

- bundle_id: `labview-nxg-g-programming-api-overview`
- source_path: `database-connectivity-toolkit.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-g-programming-api-overview/raw/resource/enus/database-connectivity-toolkit.html
- document_id: `labview-nxg-g-programming-api-overview`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Database Connectivity API contains a set of nodes with which you can perform both common database tasks and advanced customized tasks. Works with any provider that adheres to the Microsoft ActiveX Data Object (ADO) standard. Works with any database driver that complies with Open Database Connect

Database Connectivity

The Database Connectivity API contains a set of nodes with which you can perform both
 common database tasks and advanced customized tasks.

- Works with any provider that adheres to the Microsoft ActiveX Data Object (ADO)
 standard.
- Works with any database driver that complies with Open Database Connectivity (ODBC) or
 Object Linking and Embedding Database (OLE DB) protocols.
- Maintains a high level of portability. In many cases, you can port an application to
 another database by changing the connection information you pass to the Open
 Connection node.
- Converts database column values from native data types to standard LabVIEW NXG data
 types, further enhancing portability.
- Permits the use of SQL statements with all supported database systems, even non-SQL
 systems.
- Creates tables and selects, inserts, updates, and deletes records without using SQL
 statements.

Parent topic:

Programming in G

<!--NI_TOPIC bundle=labview-nxg-g-programming-api-overview path=dataflow-duplicates.html language=enus -->
## TOPIC 00017: Dataflow between Duplicates of the Same Terminal

- bundle_id: `labview-nxg-g-programming-api-overview`
- source_path: `dataflow-duplicates.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-g-programming-api-overview/raw/resource/enus/dataflow-duplicates.html
- document_id: `labview-nxg-g-programming-api-overview`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use a duplicated output terminal to write to an indicator at multiple places on the diagram. You can also use a duplicated input terminal to read from a control at multiple places on the diagram. Terminals are duplicates of one another if they have the exact same label. You can duplicate a t

Dataflow between Duplicates of the Same Terminal

You can use a duplicated output terminal to write to an indicator at multiple places on the diagram. You can also use a duplicated input terminal to read from a control at multiple places on the diagram.

Note

Create Duplicate Terminal

In the following example, the 
 String indicator displays a different message depending on which While Loop is executing. This example also uses a duplicate of the 
 Run button to control the execution of both While Loops.

Figure 1.

[IMAGE alt='1378' src='GUID-02DB5688-C953-4D32-8246-7202DBA72A8B-a5.png']

Figure 2.

[IMAGE alt='1378' src='GUID-921D89F7-8B3D-40CF-88A1-111CA3B3F846-a5.png']

Parent topic:

Terminals

Related concepts:

- Terminals
- Dataflow between the Diagram and Another VI
- Data Transfer between the Panel and the Diagram

<!--NI_TOPIC bundle=labview-nxg-g-programming-api-overview path=dataflow-panel.html language=enus -->
## TOPIC 00018: Data Transfer between the Panel and the Diagram

- bundle_id: `labview-nxg-g-programming-api-overview`
- source_path: `dataflow-panel.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-g-programming-api-overview/raw/resource/enus/dataflow-panel.html
- document_id: `labview-nxg-g-programming-api-overview`
- page_type: `leaf`
- content_type: `concept`
- source_description: Data in a control flows from the panel to the diagram through a corresponding input terminal. Data in an output terminal flows from the diagram to the panel through a corresponding indicator. The following image shows the flow of data between the panel and diagram of a VI.

Data Transfer between the Panel and the Diagram

Data in a control flows from the panel to the diagram through a corresponding input terminal. Data in an output terminal flows from the diagram to the panel through a corresponding indicator.

The following image shows the flow of data between the panel and diagram of a VI.

[IMAGE alt='1378' src='GUID-6F4B0B8A-8083-4D00-B7EA-5B1A33AC67DC-a5.png']

Parent topic:

Terminals

<!--NI_TOPIC bundle=labview-nxg-g-programming-api-overview path=dataflow-subvi.html language=enus -->
## TOPIC 00019: Dataflow between the Diagram and Another VI

- bundle_id: `labview-nxg-g-programming-api-overview`
- source_path: `dataflow-subvi.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-g-programming-api-overview/raw/resource/enus/dataflow-subvi.html
- document_id: `labview-nxg-g-programming-api-overview`
- page_type: `leaf`
- content_type: `concept`
- source_description: Terminals transfer data between the diagram and other VIs via subVIs. The following image shows the flow of data between terminals of the calling VI and a subVI. The calling VI passes data to the Percentage subVI through the input terminals of the subVI node. Data from the calling VI flows through t

Dataflow between the Diagram and Another VI

Terminals transfer data between the diagram and other VIs via subVIs.
 The following image shows the flow of data between terminals of the calling VI and a subVI.

[IMAGE alt='1378' src='GUID-A98B399D-70E2-4F90-B26F-1391933C335F-a5.png']

1. The calling VI passes data to the Percentage subVI through the input terminals of the subVI node.
2. Data from the calling VI flows through the input terminals on the diagram of the subVI.
3. As the subVI executes, data flows to the output terminal of the subVI diagram.
4. Data flows from the output terminal of the subVI diagram to the output terminal of the subVI node in the calling VI.

Parent topic:

Terminals

<!--NI_TOPIC bundle=labview-nxg-g-programming-api-overview path=dataflow.html language=enus -->
## TOPIC 00020: Programming in G

- bundle_id: `labview-nxg-g-programming-api-overview`
- source_path: `dataflow.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-g-programming-api-overview/raw/resource/enus/dataflow.html
- document_id: `labview-nxg-g-programming-api-overview`
- page_type: `leaf`
- content_type: `concept`
- source_description: G Dataflow (G) is a graphical programming language in which nodes on a diagram execute when data is available for all required inputs. A node in G Dataflow executes only when it receives data for all wired inputs. When a node finishes executing, it passes data along the wire to the next node in the

Programming in G

*G Dataflow* (G) is a graphical programming language in which nodes on a diagram execute when data is available for all required inputs.

A node in G Dataflow executes only when it receives data for all wired
 inputs. When a node finishes executing, it passes data along the wire to the next node in
 the dataflow path. The movement of data along the wires and through the nodes is called
 dataflow and determines the execution order of nodes on the diagram.

Because a node executes only when all of the inputs receive data, the Subtract node in the following G diagram cannot execute until Add finishes executing and passes the data to Subtract.

[IMAGE alt='1378' src='GUID-AF97D482-CA7E-40B3-99C5-6403310D8C5F-a5.png']

However, in the following G diagram, the Add, Random Number, and Divide nodes all meet the dataflow requirement of having the required input data they need to execute. Nodes not connected to each other by wires can execute in any order because the nodes do not depend on data from another node. You cannot determine which node executes first.

[IMAGE alt='1378' src='GUID-06651DCB-2B39-43AD-8C2D-ACB35E394490-a5.png']

Because the flow of data, rather than the sequential order of commands, determines the execution order of nodes in G, you can create diagrams that have simultaneous operations. The image above illustrates operations that run simultaneously.

<!--NI_TOPIC bundle=labview-nxg-g-programming-api-overview path=design-develop-projects-g.html language=enus -->
## TOPIC 00021: Best Practices for Creating Projects in G Web Development Software

- bundle_id: `labview-nxg-g-programming-api-overview`
- source_path: `design-develop-projects-g.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-g-programming-api-overview/raw/resource/enus/design-develop-projects-g.html
- document_id: `labview-nxg-g-programming-api-overview`
- page_type: `leaf`
- content_type: `concept`
- source_description: To develop projects that successfully serve your needs and the needs of your end users, refer to the following best practice guidelines: File and Project Organization for Projects in G Web Development Software Icons and Connector Panes for Projects in G Web Development Software Panel Design for Proj

Best Practices for Creating Projects in G
 Web Development Software

To develop projects that successfully serve your needs and the needs of your end users, refer to the following best practice guidelines:

- File and Project Organization for
 Projects in G Web Development Software
- Icons and Connector Panes
 for Projects in G Web Development Software
- Panel Design for Projects in G
 Web Development Software
- Diagram Design for Projects
 in G Web Development Software
- Other Best Practices for Projects
 in G Web Development Software

Parent topic:

Programming in G

Related reference:

- File and Project Organization in G Web Development Software
- Icons and Connector Panes for Distributed APIs
- Panel Design for G Web Development Software Projects
- Diagram Design for G Web Development Software Projects
- Localization for LabVIEW NXG Projects

<!--NI_TOPIC bundle=labview-nxg-g-programming-api-overview path=diagram-design-lv-projects.html language=enus -->
## TOPIC 00022: Diagram Design for G Web Development Software Projects

- bundle_id: `labview-nxg-g-programming-api-overview`
- source_path: `diagram-design-lv-projects.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-g-programming-api-overview/raw/resource/enus/diagram-design-lv-projects.html
- document_id: `labview-nxg-g-programming-api-overview`
- page_type: `leaf`
- content_type: `reference`
- source_description: Refer to the following table for best practices for designing diagrams in G Web Development Software. Guideline Required or Recommended? Details Example(s) Use a type definition when you use the same unique control in more than one location or when your project includes a large data structure that p

Diagram Design for G Web Development
 Software Projects

Refer to the following table for best practices for designing diagrams in G Web
 Development Software.

| Guideline | Required or Recommended? | Details | Example(s) |
| --- | --- | --- | --- |
| Use a type definition when you use the same unique control in more than one location or when your project includes a large data structure that passes between several subVIs. | Required | A type definition automatically propagates changes to the control or data structure throughout all relevant VIs and subVIs. | N/A |
| Select Autosize list view in the Item tab for any properties nodes, such as Cluster Properties or Waveform Properties. | Required | The Autosize list view option ensures that all element names are fully visible. | N/A |
| Make sure that data flows from left to right and that wires enter the diagram from the left and exit to the right. | Recommended | Although the positions of program elements do not determine execution order, avoiding right-to-left wiring helps users read and comprehend the diagram. Note Only wires and structures determine execution order. | N/A |
| Avoid creating any backwards wires. | Recommended | Wires that cause data to flow from right to left contradict style best practices. | N/A |
| For subVIs and top-level VIs that do not contain loops, place controls on the far left and indicators on the far right. | Recommended | Placing controls and indicators in these positions increases readability and usability by giving users a familiar and expected location to look for the controls and indicators. | N/A |
| For non-user interface subVIs, make sure all controls and indicators that are on the connector pane also reside on the top-level diagram. | Recommended | N/A | N/A |
| When you use enumerated type constants, always create G Types of those constants. | Recommended | Enumerated type constants are useful for making diagram code easier to read. When you wire an enumerated type constant to a Case Structure, the string labels appear in the selector label of the Case Structure. G Types prevent you from needing to rewrite code each time you add or remove an item from an enumerated type constant. | N/A |
| Use a docked constant if the only purpose of the constant is to define a data type and the value is unimportant. | Recommended | Docked constants that contain meaningful values can inhibit the readability of the diagram. If a docked constant is set to the default value, it will appear hollow. If any other value is used, it will be a solid color. | N/A |
| If you display the list view of a node, make sure the entire name of the longest item in the node is visible. | Recommended | Also, resize the node for shorter names to reduce any extra space. | N/A |
| Use list view for all nodes imported with the Jenkins Shared Library Interface (JSLI) document type, and show the node label. | Recommended | List view helps users distinguish between JSLI nodes and subVI nodes and also improves readability. | N/A |
| If you wire an enum to a Case Structure, make sure none of the cases are marked as the default case. | Recommended | One exception to this guideline is if the Case Structure only operates on one or a small number of the overall number of items in the enum. | N/A |
| If you wire a ring, string, or numeric to a Case Structure, remove any additional values from the string in the Case Selector Label. | Recommended | Removing additional values increases clarity. | See the Case Values of a Case Structure section following this table for a visual example. |
| If possible, avoid using ellipsis notation for enum values. | Recommended | Enumerate all the values so that if you add a new value later, the diagram breaks and you can consciously handle the new enum value. Use range notation sparingly. | N/A |
| If your VI includes its own clusters or enums on the diagram, define them with type definitions. | Recommended | Type definitions allow you to manage these data types in one place and ensure that any changes you make to a data type propagate across all relevant VIs and subVIs. | N/A |
| Use comments to document the functionality of your code. | Recommended | N/A | N/A |
| Reference applicable VIs in comments instead of showing the labels on all subVIs in a diagram. | Recommended | When you display object labels, you cannot reposition them, so your diagram width must increase unnecessarily. | N/A |
| Consider whether or not your VI needs an error Case Structure surrounding its contents. | Recommended | If the error Case Structure is not handling critical running code, consider simply passing the error wire through all diagram nodes without creating a case around the whole diagram. You may want to use an error case if your VI is manipulating the error cluster at all. Using an error case allows you to case out the relevant diagram so that your error manipulation code does not modify any error entering the VI. | High iteration loops and modal dialogs are examples of critical running code. |
| Arrange diagrams so that the primary wire travels in a straight line between nodes. | Recommended | The primary wire is typically a reference or error wire. | N/A |
| Keep approximately 20 pixels of white space between objects. | Recommended | An overcrowded diagram without adequate white space is difficult to read. | N/A |
| Expand array constants to display all array elements, plus one empty element at the end. | Recommended | Displaying all array elements with an empty space at the end helps users see the entirety of the array. If you do not have enough space for a large array constant, display the scrollbar. | N/A |
| Use a comment to label long wires and identify their use. | Recommended | Wire comments are useful for identifying and describing wires that come from shift registers and long wires that span the entire diagram. | N/A |
| Avoid bending wires when possible, and keep wires short. | Recommended | Wires with long, complicated paths are difficult to follow. Note Avoid replacing long wires with local or global variables. | N/A |
| Align and distribute nodes, terminals, and constants. | Recommended | When you align and distribute objects evenly, you can use straight wires to connect objects and create readable diagrams. | N/A |
| Avoid placing diagram objects, such as subVIs or structures, on top of wires, and avoid placing any wires under diagram objects because the software can hide certain segments of the resulting wire. | Recommended | Draw wires so that you can clearly see if a wire connects to a terminal. Avoid wiring through structures if the structure does not use the data in a wire. | N/A |
| Make sure control and indicator terminals on the connector pane do not reside inside structures on the diagram. | Recommended | The development environment can optimize subVI execution time when all controls and indicators on the connector pane reside on the top-level diagram of the VI. | N/A |
| Save the VI with the most important frame of multi-framed structures, such as a Case Structure, displayed. | Recommended | Saving the VI with the most important case displayed increases readability because the user does not have to switch cases immediately. | If you open a diagram and the error case that wraps the entire diagram is displayed first, you must switch to the no error case to see the actual diagram code. |
| Maximize the performance of code on the diagram. | Recommended | When a program has large arrays or critical timing problems, you can use the following guidelines to maximize the performance of the VI: If possible, avoid building arrays using Build Array within a loop because the node makes repetitive calls to the memory manager. Instead, use auto-indexing or pre-size the array and use Replace Array Subset to place values in the array. Also avoid using Concatenate Strings with strings because, in memory, the software handles strings as arrays of characters. Choose the proper array data type to control the memory usage of the application. Display only necessary information on the panel. Send data to indicators only if the data is different from what the indicator already displays. Frequently updating panel indicators with new data can affect the performance of the VI, especially if you display large amounts of data in graphs or charts. | Array data types can affect the memory usage of an application. For example, if your double-precision, floating-point array of 100,000 values is actually storing single-precision, floating-point values, you are using memory inefficiently. In this case, use an array of single-precision, floating-point values to match the data type stored in the array and reduce the memory usage. |
| If your VI includes several I/O name controls, such as Waveform and Digital Waveform, that are stacked vertically, configure them to not show type. | Recommended | If you set I/O name controls to not show their type, you can maximize information density and avoid overlapping the controls. | N/A |

#### Case Values of a Case Structure

[IMAGE alt='1378' src='GUID-C6D26EFF-2DAD-42EC-8DD6-E98842DBA1BD-a5.png']

Parent topic:

Best Practices for Creating Projects in G Web Development Software

Related concepts:

- Best Practices for Creating Projects in G Web Development Software

Related reference:

- File and Project Organization in G Web Development Software
- Icons and Connector Panes for Distributed APIs
- Panel Design for G Web Development Software Projects
- Localization for LabVIEW NXG Projects

<!--NI_TOPIC bundle=labview-nxg-g-programming-api-overview path=documentation-api.html language=enus -->
## TOPIC 00023: Documentation for Distributed APIs

- bundle_id: `labview-nxg-g-programming-api-overview`
- source_path: `documentation-api.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-g-programming-api-overview/raw/resource/enus/documentation-api.html
- document_id: `labview-nxg-g-programming-api-overview`
- page_type: `leaf`
- content_type: `reference`
- source_description: Refer to the following table for best practices for documenting an API. Guideline Required or Recommended? Details Review the VI description and parameter descriptions of all public VIs in your API for correct meaning for what the VI does, usability by third parties who are unfamiliar with your API,

Documentation for Distributed APIs

Refer to the following table for best practices for documenting an API.

| Guideline | Required or Recommended? | Details |
| --- | --- | --- |
| Review the VI description and parameter descriptions of all public VIs in your API for correct meaning for what the VI does, usability by third parties who are unfamiliar with your API, spelling, grammar, and naming conventions for G Web Development Software. | Required | N/A |

Parent topic:

Best Practices for Designing and Developing an Application Programming Interface (API) in G Web Development Software

Related concepts:

- Best Practices for Designing and Developing an Application Programming Interface (API) in G Web Development Software

Related reference:

- File Organization and Node Naming for Distributed APIs
- Component Organization for Distributed APIs
- Icons and Connector Panes for Distributed APIs
- Panel Design for Distributed APIs
- Data Type Selection for Distributed APIs
- Palette Taxonomy for Distributed APIs
- Error Message Design for Distributed APIs
- API Design for Distributed APIs

<!--NI_TOPIC bundle=labview-nxg-g-programming-api-overview path=enable-multi-mode-elements-and-overload-groups.html language=enus -->
## TOPIC 00024: Multi-Mode Element and Overload Group Behavior

- bundle_id: `labview-nxg-g-programming-api-overview`
- source_path: `enable-multi-mode-elements-and-overload-groups.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-g-programming-api-overview/raw/resource/enus/enable-multi-mode-elements-and-overload-groups.html
- document_id: `labview-nxg-g-programming-api-overview`
- page_type: `leaf`
- content_type: `concept`
- source_description: Multi-Mode Elements and overload groups allow you to expand and customize the way you interact with nodes on a diagram. These features are only supported for use within an add-on library. To update Multi-Mode Elements and overload groups, place them in an add-on library and update the add-on library

Multi-Mode Element and Overload Group
 Behavior

Multi-Mode Elements and overload groups allow you to expand and customize the way
 you interact with nodes on a diagram.

These features are only supported for use within an add-on library. To update
 Multi-Mode Elements and overload groups, place them in an add-on library and
 update the add-on library.

Parent topic:

Programming in G

Related tasks:

- Preview Features

<!--NI_TOPIC bundle=labview-nxg-g-programming-api-overview path=error-management.html language=enus -->
## TOPIC 00025: Error Management

- bundle_id: `labview-nxg-g-programming-api-overview`
- source_path: `error-management.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-g-programming-api-overview/raw/resource/enus/error-management.html
- document_id: `labview-nxg-g-programming-api-overview`
- page_type: `leaf`
- content_type: `concept`
- source_description: When an error occurs in your code, the error is logged in the console. You can manage errors programmatically.

Error Management

When an error occurs in your code, the error is logged in the console. You can manage
 errors programmatically.

Parent topic:

Programming in G

<!--NI_TOPIC bundle=labview-nxg-g-programming-api-overview path=error-messages-api.html language=enus -->
## TOPIC 00026: Error Message Design for Distributed APIs

- bundle_id: `labview-nxg-g-programming-api-overview`
- source_path: `error-messages-api.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-g-programming-api-overview/raw/resource/enus/error-messages-api.html
- document_id: `labview-nxg-g-programming-api-overview`
- page_type: `leaf`
- content_type: `reference`
- source_description: Refer to the following table for best practices for designing error messages. Guideline Required or Recommended? Details Reserve a range of error codes for your API and use those codes for error conditions specific to your API. Required Pick a range for error codes between -8999 through -8000, 5000

Error Message Design for Distributed APIs

Refer to the following table for best practices for designing error messages.

| Guideline | Required or Recommended? | Details |
| --- | --- | --- |
| Reserve a range of error codes for your API and use those codes for error conditions specific to your API. | Required | Pick a range for error codes between -8999 through -8000, 5000 through 9999, and 500,000 through 599,999, which are reserved for external users. |
| When generating or manipulating errors on the diagram of your API VIs, make sure you use the Error API to construct and manipulate error clusters. | Required | Never bundle or unbundle error cluster elements directly in G Web Development Software. |
| If the VI has no way to generate errors, consider excluding error inputs and outputs. | Recommended | If a VI does not generate errors, users of the VI can take advantage of parallelism in G Web Development Software. |
| If you exclude error inputs and outputs on a VI in your API, leave the error input and output locations on the connector pane empty. | Recommended | When unused error inputs and outputs on a VI are left empty, you can add error handling to the VI later. |

Parent topic:

Best Practices for Designing and Developing an Application Programming Interface (API) in G Web Development Software

Related concepts:

- Best Practices for Designing and Developing an Application Programming Interface (API) in G Web Development Software

Related reference:

- File Organization and Node Naming for Distributed APIs
- Component Organization for Distributed APIs
- Icons and Connector Panes for Distributed APIs
- Panel Design for Distributed APIs
- Data Type Selection for Distributed APIs
- Palette Taxonomy for Distributed APIs
- Documentation for Distributed APIs
- API Design for Distributed APIs

<!--NI_TOPIC bundle=labview-nxg-g-programming-api-overview path=executing-code-based-condition.html language=enus -->
## TOPIC 00027: Executing Code Based on a Condition

- bundle_id: `labview-nxg-g-programming-api-overview`
- source_path: `executing-code-based-condition.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-g-programming-api-overview/raw/resource/enus/executing-code-based-condition.html
- document_id: `labview-nxg-g-programming-api-overview`
- page_type: `leaf`
- content_type: `task`
- source_description: Use a Case Structure to incorporate decision logic into your program. A Case Structure contains one or more subdiagrams, or cases, exactly one of which executes when the structure executes.Case Structures behave similarly to switch statements or if-then-else statements in other programming languages

Executing Code Based on a Condition

Case Structure

Case Structure

Case Structures

switch

if-then-else

#### What to Use

- Case Structure 
 org.dita.html5/xsl/topic.xsl 455Tip If you are choosing between only two values based on a Boolean input, you can use the [Select](/csh?topicname=select.html) node instead of a Case Structure with a Boolean selector.

#### What to Do

Create the following diagram to execute different code based on a given condition.

Customize the gray sections for your unique programming goals.

[IMAGE alt='1378' src='GUID-2C5E960D-D338-48FF-949E-254D93136D34-a5.png']

[IMAGE alt='1378' src='GUID-B2DAE4FD-3F00-4CC7-BAEB-2561341C11DF-a5.png']

|  | Wire the data that you want to use to make a decision to the selector terminal. The data type of the value you wire to the selector terminal defines the various cases that are available in the Case Structure. The selector terminal accepts Boolean, string, integer, floating point, enumerated type, and error cluster data. |
| --- | --- |
|  | Use the case selector label to define the various cases in which different code executes. The case name displayed in the case selector label matches the selector terminal value(s) for which the corresponding subdiagram executes. You can define each case using a single value or a range of values. You can also use the case selector label to specify a default case. |
|  | Place the code you want to execute in each case on the corresponding subdiagram of the Case Structure. |
|  | To add, duplicate, or delete cases, right-click the border of the Case Structure and select the desired option from the Cases shortcut menu. |
|  | To view the different subdiagrams in the Case Structure, click the down arrow on the case selector label and select the desired case. |
|  | Every case must provide data to all output tunnels in order for the Case Structure to execute. If any case does not provide data to an output tunnel, an error occurs, and the output tunnel appears as a white box with a colored border. To resolve this error and allow the Case Structure to execute without explicitly wiring all cases, right-click the unwired output tunnel and select Default If Unwired. The output tunnel returns the default value for its data type if the subdiagram that executes does not provide that output tunnel with data. When set to Default If Unwired, the output tunnel appears as a white box with a colored border and a dash in the center. When all cases provide data to a particular output tunnel, that output tunnel appears as a solid box. |

#### Troubleshooting

- If the default case executes unexpectedly, verify that the input values wired to the selector terminal match the values in the case selector label exactly.
- An edit-time error occurs when there are values of the selector data type that do not correspond to any subdiagram in the Case Structure. You must either define a default case to handle out-of-range values or create a case for every possible input value. For example, if the selector is an integer data type and you specify cases for 1, 2, and 3, you must specify a default case to execute if the input value is 4 or any other unspecified integer value.

Parent topic:

Repeating Operations

<!--NI_TOPIC bundle=labview-nxg-g-programming-api-overview path=file-io.html language=enus -->
## TOPIC 00028: Opening, Processing, and Closing Files

- bundle_id: `labview-nxg-g-programming-api-overview`
- source_path: `file-io.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-g-programming-api-overview/raw/resource/enus/file-io.html
- document_id: `labview-nxg-g-programming-api-overview`
- page_type: `leaf`
- content_type: `task`
- source_description: What to Use Open/Create/Replace File A read or write node from the Storage palette category Close File What to Do Create the following diagram to programmatically open, write to, and close a text file. Customize the gray sections for your unique programming goals. Open, create, or replace a file by

Opening, Processing, and Closing Files

#### What to Use

- Open/Create/Replace File
- A read or write node from the Storage palette category
- Close File

#### What to Do

Create the following diagram to programmatically open, write to, and close a text file.

Customize the gray sections for your unique programming goals.

[IMAGE alt='1378' src='GUID-E41CE97C-C4C6-43AC-A02F-D4F70514ABE9-a5.png']

|  | Open, create, or replace a file by using the Open/Create/Replace File node and specifying its precise behavior. To access the enumerated list of possible behaviors, create a constant from the operation input of the node. |
| --- | --- |
|  | After the file opens, a unique identifier called a refnum represents the file. A file refnum is required for most nodes that process files. |
|  | Process the file by using a file I/O node from the Storage palette category. You can interact with binary or text files. In this example, Write to Text File writes Hello world to the file represented by the file refnum. |
|  | Close the file to release the object from memory and avoid potential errors. If you do not close a file, the reference cannot be closed until the VI that opened the file finishes executing. |

#### Troubleshooting

- Some file I/O nodes are considered high-level nodes and perform all three steps of a file I/O process—open, read/write, and close. Avoid placing high-level file I/O nodes, such as Read from Spreadsheet File and Write to Spreadsheet File , in loops because these nodes perform open and close operations each time they run.

Parent topic:

Programming in G

<!--NI_TOPIC bundle=labview-nxg-g-programming-api-overview path=file-organization-api.html language=enus -->
## TOPIC 00029: File Organization and Node Naming for Distributed APIs

- bundle_id: `labview-nxg-g-programming-api-overview`
- source_path: `file-organization-api.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-g-programming-api-overview/raw/resource/enus/file-organization-api.html
- document_id: `labview-nxg-g-programming-api-overview`
- page_type: `leaf`
- content_type: `reference`
- source_description: Refer to the following table for best practices for organizing files and naming nodes. Guideline Required or Recommended? Details Example(s) Use title case. Required Capitalize the following in subVI names: The first and the last word All nouns, pronouns, adjectives, verbs, adverbs, and subordinate

File Organization and Node Naming for Distributed APIs

Refer to the following table for best practices for organizing files and naming nodes.

| Guideline | Required or Recommended? | Details | Example(s) |
| --- | --- | --- | --- |
| Use title case. | Required | Capitalize the following in subVI names: The first and the last word All nouns, pronouns, adjectives, verbs, adverbs, and subordinate conjunctions (as, because, although) | General Error Handler, not General error handler |
| Capitalize the second part of a hyphenated compound. | Required | N/A | Fixed-Point, not Fixed-point |
| Do not capitalize articles (a, an, the), coordinate conjunctions (and, or, nor), or prepositions regardless of length, unless they are the first or last word. | Required | Boolean operators are an exception. Write Boolean operators, such as AND and OR, in all capital letters. | Search and Replace, not Search And Replace |
| Do not capitalize to in an infinitive phrase unless to is the first word node name. | Required | N/A | Path to String, not Path To String; To String, not to String. |
| Use industry-standard capitalization for an engineering or scientific term. | Required | N/A | PolyBezier, not Polybezier |
| Write acronyms in all capital letters. | Required | N/A | FIFO, not Fifo, URL, not Url |
| Use spaces between words. | Required | N/A | Feedback Node, not FeedbackNode |
| Do not use special characters. | Required | Boolean operators are an exception. Use a question mark (?) for node names when the primary output is Boolean, such as Equal?, not Is Equal. | Search and Replace, not Search & Replace |
| Make sure none of the nodes or VIs in your API share the same name with a node or VI that is already in the LabVIEW NXG palettes. | Required | Unique node and VI names in an API make unique palette object names for Quick Drop users. | N/A |
| Do not use the forbidden word, Example, in the names of your API nodes or VIs. | Required | N/A | N/A |

Parent topic:

Best Practices for Designing and Developing an Application Programming Interface (API) in G Web Development Software

Related concepts:

- Best Practices for Designing and Developing an Application Programming Interface (API) in G Web Development Software

Related reference:

- Component Organization for Distributed APIs
- Icons and Connector Panes for Distributed APIs
- Panel Design for Distributed APIs
- Data Type Selection for Distributed APIs
- Palette Taxonomy for Distributed APIs
- Documentation for Distributed APIs
- Error Message Design for Distributed APIs
- API Design for Distributed APIs

<!--NI_TOPIC bundle=labview-nxg-g-programming-api-overview path=file-prog-org-lv.html language=enus -->
## TOPIC 00030: File and Project Organization in G Web Development Software

- bundle_id: `labview-nxg-g-programming-api-overview`
- source_path: `file-prog-org-lv.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-g-programming-api-overview/raw/resource/enus/file-prog-org-lv.html
- document_id: `labview-nxg-g-programming-api-overview`
- page_type: `leaf`
- content_type: `reference`
- source_description: Refer to the following table for best practices for organizing files and projects in G Web Development Software. Guideline Required or Recommended? Details Example(s) Avoid using special characters in file names. Recommended Using special characters in file names can cause compatibility concerns acr

File and Project Organization in G Web
 Development Software

Refer to the following table for best practices for organizing files and projects in G
 Web Development Software.

| Guideline | Required or Recommended? | Details | Example(s) |
| --- | --- | --- | --- |
| Avoid using special characters in file names. | Recommended | Using special characters in file names can cause compatibility concerns across platforms. | Avoid the following: File separators such as colons, forward slashes, and backward slashes Non-alphabetical and non-numerical symbols, such as the trademark symbol Punctuation marks, such as parentheses, quotation marks, brackets, and operators White space characters, such as tabs and new lines Note You can use spaces for most applications, but avoid using spaces in a top-level .gviweb to create a human-readable URL. |
| Make sure your project organization is logical and easy to use. | Recommended | Create a hierarchical structure with easily accessible top-level VIs. Place support VIs in folders within the project and group them to reflect modular components, such as instrument drivers, other drivers, and configuration utilities. Limit the number and the levels of directories you use in a project. | N/A |

Parent topic:

Best Practices for Creating Projects in G Web Development Software

Related concepts:

- Best Practices for Creating Projects in G Web Development Software

Related reference:

- Icons and Connector Panes for Distributed APIs
- Panel Design for G Web Development Software Projects
- Diagram Design for G Web Development Software Projects
- Localization for LabVIEW NXG Projects

<!--NI_TOPIC bundle=labview-nxg-g-programming-api-overview path=for-loops-repeating-operations-set-number-of-times.html language=enus -->
## TOPIC 00031: Repeating Operations a Set Number of Times

- bundle_id: `labview-nxg-g-programming-api-overview`
- source_path: `for-loops-repeating-operations-set-number-of-times.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-g-programming-api-overview/raw/resource/enus/for-loops-repeating-operations-set-number-of-times.html
- document_id: `labview-nxg-g-programming-api-overview`
- page_type: `leaf`
- content_type: `task`
- source_description: Instead of creating the same code on a diagram multiple times, you can write code in a single location and use a For Loop to programmatically repeat it. For example, you might want to read a specific number of measurement samples from a device. You can place the code that performs the measurement op

Repeating Operations a Set Number of Times

Instead of creating the same code on a diagram multiple times, you can write code in a single location and use a For Loop to programmatically repeat it. For example, you might want to read a specific number of measurement samples from a device. You can place the code that performs the measurement operation on the subdiagram of a For Loop and configure the loop to repeat the operation as many times as your application requires.

#### What to Use

- For Loop
- Count terminal of the For Loop

#### What to Do

Create the following diagram to repeat an operation a set number of times.

Customize the gray sections for your unique programming goals.

[IMAGE alt='1378' src='GUID-5104BCE3-FA5B-4A67-AA56-BAB601CBE542-a5.png']

|  | Place the code you want to repeat on the subdiagram of a For Loop. |
| --- | --- |
|  | Specify how many times the For Loop repeats its subdiagram by wiring the desired value to the count terminal. Tip If you want the loop to execute once for each element in an array, wire the array to the loop using an auto-indexing tunnel instead of wiring a value to the count terminal. |
|  | If you want to know which loop iteration is currently executing, use the iteration terminal to return the current loop iteration count. The iteration terminal is zero-indexed, meaning it ranges from 0 to n -1. Use Increment to obtain the true number of loop iterations. |
|  | If you want to collect the result of each loop iteration in an array, use an auto-indexing output tunnel to pass values out of the loop. To enable auto-indexing for an output tunnel, right-click the tunnel and select Append Mode » Auto Index Values. If you do not enable auto-indexing, the loop returns only the value from the last loop iteration. |

#### Troubleshooting

- If the For Loop 
 unexpectedly fails to execute, verify that the value wired to the count terminal
 is greater than zero.
- If the execution
 speed of the loop is too fast, place a Wait node on the
 subdiagram of the loop to specify a wait period.

Parent topic:

Repeating Operations

Related concepts:

- Loop Timing

Related tasks:

- Repeating Operations
- Repeating Operations Once for Every Element in an Array
- Repeating Operations until a Condition Occurs

<!--NI_TOPIC bundle=labview-nxg-g-programming-api-overview path=icons-connector-panes-api.html language=enus -->
## TOPIC 00032: Icons and Connector Panes for Distributed APIs

- bundle_id: `labview-nxg-g-programming-api-overview`
- source_path: `icons-connector-panes-api.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-g-programming-api-overview/raw/resource/enus/icons-connector-panes-api.html
- document_id: `labview-nxg-g-programming-api-overview`
- page_type: `leaf`
- content_type: `reference`
- source_description: Refer to the following table for best practices for creating icons and connector panes. Guidelines for SubVI Size Guideline Required or Recommended? Details Make all VIs or as many VIs as possible the same size. Required The icon size is determined by the connector pane pattern that the subVI requir

Icons and Connector Panes for Distributed APIs

Refer to the following table for best practices for creating icons and connector panes.

| Guideline | Required or Recommended? | Details |
| --- | --- | --- |
| Make all VIs or as many VIs as possible the same size. | Required | The icon size is determined by the connector pane pattern that the subVI requires. Refer to the icon and connector pane guidelines in Icons and Connector Panes for G Web Development Software Projects for more information. |
| When resizing a VI, expand it in one direction. | Required | The direction a VI can stretch depends on error input and output location on the connector pane. If the error input and output are beneath the instrument handles, as with driver APIs, vertically expand the VI. If the error input and output are on the lower-left or lower-right of the node, horizontally expand the VI. Increase the size of the entire API to be more consistent, if necessary. |

| Guideline | Required or Recommended? | Details | Example(s) |
| --- | --- | --- | --- |
| Make the node size big enough to communicate its functionality through an icon. | Required | The icon should communicate node behavior. | N/A |
| Make consistent iconography for all the VIs in your API. | Required | Default glyphs are in the G Web Development Software project on the Icon tab. You can use the default glyphs as a starting point in your VIs. | N/A |

| Guideline | Required or Recommended? | Details | Example(s) |
| --- | --- | --- | --- |
| Include pass-through wires in the upper corners of a VI only if it is part of a reference-based API. | Required | A reference value is not modified during execution, so passing it through VIs in an API is convenient. A VI could potentially modify a data value, in other words, any wire that is not a reference or a cluster/class of references, if it is passing through. Pass data values through VIs only if the VI might modify the value of the wire. | Reference-based APIs in G Web Development Software include queue and HTTP. |
| Either coerce numeric inputs into a range that your code expects, or handle out-of-range values with an error condition or warning. | Required | Do not configure data limits for numeric controls. | If you specify the speed of a motor, and the motor can go only 0-100 mph, make sure you are either coercing the input value with an In Range and Coerce function to be within 0-100, or return an error if you specify a value outside that range. |
| Use lower case for input and output names. | Required | N/A | Use: exported waveform Do not use: Exported Waveform |
| Use input and output names that are easy to understand. | Required | N/A | Use: remainder Do not use: x-y*floor(x/y) |
| Name inputs and outputs consistently. | Required | N/A | For three inputs that have the same data type and source type, use: task in, task in, task in. Do not use: task in, myDAQ task in, myDAQ resource in |
| Use simple words, not symbols. | Required | N/A | Use: number of samples Do not use: # of samples |
| Use a question mark (?) for input and output names when the data type is Boolean with an implied question. | Required | N/A | Use: UTC? Do not use: is UTC |
| Do not use a question mark (?) for Boolean inputs and outputs that are commands. | Required | N/A | Use: reset Do not use: reset? |
| Do not include default values in parentheses. | Required | Set default values in the configuration panel. G Web Development Software automatically appends the default values to the label. | Use: max characters per row Do not use: max characters/row (no limit:0) |
| Do not include units of measure in parentheses. | Required | Set units in the configuration panel. G Web Development Software automatically appends the units to the label. | Use: delay time Do not use: delay time (s) |
| Make sure the names of inputs and outputs of your VIs use complete English words, unless users worldwide know an abbreviation. | Required | N/A | N/A |
| If you use the top or bottom inputs and outputs on the connector pane, make sure their wires never cross each other. | Required | N/A | See the Avoid Crossing Wires section at the end of this table for a visual example. |
| Assign the input and output terminals on the connector pane in a way that simplifies the wiring diagram. | Required | Consider how users might wire the VIs together when you assign terminals. Align the output terminals with the corresponding input terminals. | N/A |
| If multiple VIs in your API have the same input or output, place all similar inputs and outputs in the same location on the connector pane of all VIs. | Required | N/A | See the Locate Inputs and Outputs Consistently section at the end of this table for a visual example. |
| Do not leave any terminals of your public API VIs in the unplaced items tray. | Recommended | When all controls/indicators are on the panel, the user can open the panel of your VI and see input and output values during debugging. | N/A |
| Set the display format of numeric controls and indicators to produce reasonable format settings for controls and indicators that users create from them. | Recommended | The display format settings of a source numeric control or indicator are passed on to any controls and indicators created from them. | N/A |

#### Avoid Crossing Wires

[IMAGE alt='1378' src='GUID-BD123550-6F61-4DED-A0D6-8E41874FDBDF-a5.png']

#### Locate Inputs and Outputs Consistently

[IMAGE alt='1378' src='GUID-523EF860-01DA-465E-902F-5D246FC2A224-a5.png']

Parent topic:

Best Practices for Designing and Developing an Application Programming Interface (API) in G Web Development Software

Related concepts:

- Best Practices for Creating Projects in G Web Development Software
- Best Practices for Designing and Developing an Application Programming Interface (API) in G Web Development Software

Related reference:

- Localization for LabVIEW NXG Projects
- File and Project Organization in G Web Development Software
- Panel Design for G Web Development Software Projects
- Diagram Design for G Web Development Software Projects
- File Organization and Node Naming for Distributed APIs
- Component Organization for Distributed APIs
- Panel Design for Distributed APIs
- Data Type Selection for Distributed APIs
- Palette Taxonomy for Distributed APIs
- Documentation for Distributed APIs
- Error Message Design for Distributed APIs
- API Design for Distributed APIs
- Icons and Connector Panes for G Web Development Software Projects

<!--NI_TOPIC bundle=labview-nxg-g-programming-api-overview path=icons-connector-panes-lv-proj.html language=enus -->
## TOPIC 00033: Icons and Connector Panes for G Web Development Software Projects

- bundle_id: `labview-nxg-g-programming-api-overview`
- source_path: `icons-connector-panes-lv-proj.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-g-programming-api-overview/raw/resource/enus/icons-connector-panes-lv-proj.html
- document_id: `labview-nxg-g-programming-api-overview`
- page_type: `leaf`
- content_type: `reference`
- source_description: Refer to the following table for best practices for creating icons and connector panes in G Web Development Software. Guideline Required or Recommended? Details Example(s) Consider using the well-designed icons in the G Web Development Software libraries as prototypes for your icon. Recommended If y

Icons and Connector Panes for G Web
 Development Software Projects

Refer to the following table for best practices for creating icons and connector panes
 in G Web Development Software.

| Guideline | Required or Recommended? | Details | Example(s) |
| --- | --- | --- | --- |
| Consider using the well-designed icons in the G Web Development Software libraries as prototypes for your icon. | Recommended | If you cannot find or create a picture to use for an icon, you can use text. | N/A |
| Create a uniform icon style for all related VIs. | Recommended | A uniform style helps users visually determine which subVIs are associated with a top-level VI. | N/A |
| Avoid using colloquialisms when making icons. | Recommended | Colloquialisms, even in pictures, are difficult to translate. Users that speak languages other than English may not understand a picture that relies on cultural background knowledge. | If you represent a data logging VI with a picture of a lumberjack, some users may not know the cultural reference to understand how a lumberjack can represent data logging. |
| Create a meaningful icon for every VI. | Recommended | The icon represents the VI on a palette and diagram. Well-designed icons help users gain a better understanding of the subVI without the need for excess documentation. | N/A |
| Consider common node sizes in LabVIEW NXG when designing an icon. | Recommended | Refer to the following common node sizes: 30x30 for small nodes. This size supports the 3-1-1-3 connector pane pattern. 40x40 for the default VI size. This size supports the 4-2-2-4 connector pane pattern. 50x50 for the default size used by NI hardware driver and Advanced Analysis Library APIs. This size supports the 5-3-3-5 connector pane pattern. | N/A |
| Make sure to set inputs and outputs for each subVI as required, recommended, or optional in the connector pane for that subVI, and make sure the settings make sense for your project. | Recommended | Use the Usage settings on the Item tab for the connector panes of all subVIs to specify the input and output settings for each subVI. The Usage setting for connector pane terminals affects the appearance of the inputs and outputs in the Context Help and reminds users to wire subVI connections. Use the required setting for inputs that users must wire for the subVI to run properly. Use the optional setting for inputs that have default values that are appropriate for the subVI the majority of the time. Use the recommended setting for all other inputs. | N/A |
| Assign inputs and outputs according to the way a user will eventually wire VIs together. | Recommended | Wire inputs on the left and outputs on the right of the connector pane because standard data flow moves from the left to the right. Consistency between the location you assign inputs and outputs in the connector pane and their location in the actual data flow promotes ease of use and reuse. | If you create a group of subVIs that you often use together, give the subVIs a consistent connector pane with common inputs in the same location to help you remember where to locate each input. If you create a subVI that produces an output that another subVI uses as an input, such as references, task IDs, and error clusters, align the input and output connections to simplify the wiring patterns. Assign two inputs of a VI to the left two terminals of the corresponding connector pane and two outputs of that VI to the right two terminals of the corresponding connector pane. |
| Reserve the bottom left and right connector pane terminals for the error input and error output. | Recommended | Session-based APIs are the only exception to this recommendation. For session-based APIs, you can place error inputs and outputs directly beneath session and reference inputs and outputs. | N/A |
| Avoid creating connector panes with more than 16 terminals. | Recommended | Including too many terminals can make a subVI difficult to understand. You can consider either splitting the functionality of the subVI into multiple subVIs or using clusters to create logical groupings of the inputs to the subVI, depending on which solution makes sense for your project. | N/A |
| If your subVI includes a pass-through input and output pair, add an in suffix to the control and an out suffix to the indicator. | Recommended | Adding these suffixes to pairs of inputs and outputs indicates a relationship between the inputs and outputs. | If you name an input reference in, name the related output reference out. |
| If your subVI includes a pass-through input and output pair, and you wire the control directly to the indicator on the diagram to prevent the value from changing, remove the indicator from the connector pane. | Recommended | You can exclude references from this guideline. | N/A |

Parent topic:

Best Practices for Creating Projects in G Web Development Software

<!--NI_TOPIC bundle=labview-nxg-g-programming-api-overview path=localization-lv-proj.html language=enus -->
## TOPIC 00034: Localization for LabVIEW NXG Projects

- bundle_id: `labview-nxg-g-programming-api-overview`
- source_path: `localization-lv-proj.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-g-programming-api-overview/raw/resource/enus/localization-lv-proj.html
- document_id: `labview-nxg-g-programming-api-overview`
- page_type: `leaf`
- content_type: `reference`
- source_description: Refer to the following table for best practices for localization in LabVIEW NXG. Guideline Required or Recommended? Details Example(s) Position plot legends to avoid any potential overlaps. Required Plot legends expand to the right when plot names grow due to larger system fonts or longer localized

Localization for LabVIEW NXG Projects

Refer to the following table for best practices for localization in LabVIEW NXG.

| Guideline | Required or Recommended? | Details | Example(s) |
| --- | --- | --- | --- |
| Position plot legends to avoid any potential overlaps. | Required | Plot legends expand to the right when plot names grow due to larger system fonts or longer localized text. | N/A |
| On the panel, check for consistent placement of control labels, and allow for extra space between controls to prevent labels from overlapping objects due to localization concerns. | Required | N/A | If you place a label on the left of an object, make sure to justify the label to the right and create some space to the left of the text. If you center a label over or under an object, make sure to center the text of that label as well. |
| On the diagram, create extra space inside free labels to account for longer or larger strings due to font differences and localization. | Required | N/A | N/A |
| If you localize a project or library that contains icons with text, make sure you also localize the text on the icon. | Required | N/A | N/A |
| Create extra space in areas of a panel or diagram where text may grow due to larger system fonts or localized text. | Required | N/A | You can leave extra white space for control and indicator labels to potentially grow in size. See the Spacing for Panels and Diagrams section following this table for a visual example. |
| Avoid using enums in shipping content if possible. | Required | Although enum labels on the panel and diagram are localized, individual enum items are not. | N/A |

#### Spacing for Panels and Diagrams

[IMAGE alt='1378' src='GUID-6840797A-E087-43D2-B8E4-03606583E119-a5.png']

Parent topic:

Best Practices for Creating Projects in G Web Development Software

Related concepts:

- Best Practices for Creating Projects in G Web Development Software

Related reference:

- File and Project Organization in G Web Development Software
- Icons and Connector Panes for Distributed APIs
- Panel Design for G Web Development Software Projects
- Diagram Design for G Web Development Software Projects

<!--NI_TOPIC bundle=labview-nxg-g-programming-api-overview path=misc-best-prac-lv-proj.html language=enus -->
## TOPIC 00035: Other Best Practices for LabVIEW NXG Projects

- bundle_id: `labview-nxg-g-programming-api-overview`
- source_path: `misc-best-prac-lv-proj.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-g-programming-api-overview/raw/resource/enus/misc-best-prac-lv-proj.html
- document_id: `labview-nxg-g-programming-api-overview`
- page_type: `leaf`
- content_type: `reference`
- source_description: Refer to the following table for LabVIEW NXG best practices. Guideline Required or Recommended? Details Example(s) Avoid using absolute paths in VIs. Required Absolute paths may cause problems when you build an application or run the VI on a different computer. If you must use an absolute path, make

Other Best Practices for LabVIEW NXG Projects

Refer to the following table for LabVIEW NXG best practices.

| Guideline | Required or Recommended? | Details | Example(s) |
| --- | --- | --- | --- |
| Avoid using absolute paths in VIs. | Required | Absolute paths may cause problems when you build an application or run the VI on a different computer. If you must use an absolute path, make sure that you include code to test that the path exists and to create the path if it does not exist. | N/A |

Parent topic:

Best Practices for Creating Projects in G Web Development Software

<!--NI_TOPIC bundle=labview-nxg-g-programming-api-overview path=palette-taxonomy-api.html language=enus -->
## TOPIC 00036: Palette Taxonomy for Distributed APIs

- bundle_id: `labview-nxg-g-programming-api-overview`
- source_path: `palette-taxonomy-api.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-g-programming-api-overview/raw/resource/enus/palette-taxonomy-api.html
- document_id: `labview-nxg-g-programming-api-overview`
- page_type: `leaf`
- content_type: `reference`
- source_description: Refer to the following table for best practices for palette taxonomy. Guideline Required or Recommended? Details Example(s) Make the root palette easy to browse. Recommended Seven to 10 categories allows for full-size icons in a single-column layout. N/A Design a structure that can expand beyond the

Palette Taxonomy for Distributed APIs

Refer to the following table for best practices for palette taxonomy.

| Guideline | Required or Recommended? | Details | Example(s) |
| --- | --- | --- | --- |
| Make the root palette easy to browse. | Recommended | Seven to 10 categories allows for full-size icons in a single-column layout. | N/A |
| Design a structure that can expand beyond the original size of the root palette for nodes you may develop in the future. | Recommended | N/A | N/A |
| Make palettes for similar categories consistent. | Recommended | N/A | Across different palettes, such as numeric, string, file, and so on, that have a constants palette, similarly organize all the constants palettes. |
| Add synonyms or keywords to your palettes to improve the findability of your VIs. | Recommended | N/A | Mathematicians commonly refer to the functionality of the Quotient and Remainder node as mod. Make sure mod is a keyword for Quotient and Remainder so that a search for mod returns that node. |

Parent topic:

Best Practices for Designing and Developing an Application Programming Interface (API) in G Web Development Software

Related concepts:

- Best Practices for Designing and Developing an Application Programming Interface (API) in G Web Development Software

Related reference:

- File Organization and Node Naming for Distributed APIs
- Component Organization for Distributed APIs
- Icons and Connector Panes for Distributed APIs
- Panel Design for Distributed APIs
- Data Type Selection for Distributed APIs
- Documentation for Distributed APIs
- Error Message Design for Distributed APIs
- API Design for Distributed APIs

<!--NI_TOPIC bundle=labview-nxg-g-programming-api-overview path=panel-api.html language=enus -->
## TOPIC 00037: Panel Design for Distributed APIs

- bundle_id: `labview-nxg-g-programming-api-overview`
- source_path: `panel-api.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-g-programming-api-overview/raw/resource/enus/panel-api.html
- document_id: `labview-nxg-g-programming-api-overview`
- page_type: `leaf`
- content_type: `reference`
- source_description: Refer to the following table for best practices for designing panels. Guideline Required or Recommended? Details Use the flat style without shadows for controls and indicators on the panels of your public API VIs. Required Create a consistent style for users when they create controls and indicators

Panel Design for Distributed APIs

Refer to the following table for best practices for designing panels.

| Guideline | Required or Recommended? | Details |
| --- | --- | --- |
| Use the flat style without shadows for controls and indicators on the panels of your public API VIs. | Required | Create a consistent style for users when they create controls and indicators from the inputs and outputs of your VIs. |

Parent topic:

Best Practices for Designing and Developing an Application Programming Interface (API) in G Web Development Software

Related concepts:

- Best Practices for Designing and Developing an Application Programming Interface (API) in G Web Development Software

Related reference:

- File Organization and Node Naming for Distributed APIs
- Component Organization for Distributed APIs
- Icons and Connector Panes for Distributed APIs
- Data Type Selection for Distributed APIs
- Palette Taxonomy for Distributed APIs
- Documentation for Distributed APIs
- Error Message Design for Distributed APIs
- API Design for Distributed APIs

<!--NI_TOPIC bundle=labview-nxg-g-programming-api-overview path=panel-design-lv-projects.html language=enus -->
## TOPIC 00038: Panel Design for G Web Development Software Projects

- bundle_id: `labview-nxg-g-programming-api-overview`
- source_path: `panel-design-lv-projects.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-g-programming-api-overview/raw/resource/enus/panel-design-lv-projects.html
- document_id: `labview-nxg-g-programming-api-overview`
- page_type: `leaf`
- content_type: `reference`
- source_description: Refer to the following table for best practices for designing panels in LabVIEW NXG Guideline Required or Recommended? Details Example(s) Avoid using all capital letters in labels or panel documentation. Recommended Capital letters can make text seem more important than necessary. N/A Position the p

Panel Design for G Web Development Software
 Projects

Refer to the following table for best practices for designing panels in LabVIEW NXG

| Guideline | Required or Recommended? | Details | Example(s) |
| --- | --- | --- | --- |
| Avoid using all capital letters in labels or panel documentation. | Recommended | Capital letters can make text seem more important than necessary. | N/A |
| Position the panel in the top left, spatially even with the controls palette. | Recommended | If you position the panel in the top left, you can prevent the user from opening the panel to a position that is potentially off the screen or otherwise difficult to see and read. | N/A |
| Display the labels of all controls and indicators on the panel. | Recommended | Make sure the labels of all controls are meaningful to increase clarity and ease of use for users. | N/A |
| Set reasonable default values for controls. Note Default values you set for controls automatically append to the terminal name. The Context Help displays the default value when you hover over the control. | Recommended | Make sure the default values you set do not generate errors when you run the top-level VI. Note When possible, avoid setting default values for indicators such as graphs, arrays, and strings. Setting default values for those types of indicators wastes disk space when you save the VI. | N/A |
| Use default values strategically and logically. | Recommended | Planning the use of default values can save space and simplify code. | N/A |
| Avoid displaying labels on the panel for buttons that display Boolean text. | Recommended | Only display the Boolean text for these buttons. Note If you click the boolean text of a checkbox, the value of that checkbox toggles. The value of that checkbox does not toggle if you click the label. | N/A |
| Format any text on your panel appropriately. | Recommended | Use default fonts when possible. When the alignment of characters is critical, use monospace fonts for string controls and indicators, and space the characters equally. For free labels, only use carriage returns to separate paragraphs. Resize labels to enable word wrapping. Include extra space in free labels to allow for longer or larger strings due to font differences in localized languages. | N/A |
| Group and arrange controls logically and aesthetically. | Recommended | Consider the arrangement of controls on panels, and keep panels simple to avoid confusing users. For top-level VIs that users can see, place the most important controls in the most prominent positions. For subVI panels, place controls and indicators of the subVI to correspond with the connector pane pattern. Note Regardless of the location of the error cluster connector pane connection, place error cluster controls and indicators at the bottom of the panel. | N/A |
| Use the Align and Distribute options in the Layout pull-down menu to create a uniform layout. | Recommended | N/A | N/A |
| Visually group objects with related functions. | Recommended | Use decorations from the Drawings palette. Use clusters to group related data. Avoid using clusters for only aesthetic purposes. | N/A |
| Configure path inputs and outputs appropriately. | Recommended | Use path controls instead of string controls to specify the location of files or directories. Path controls and indicators work similarly to strings, but the software formats paths using the standard syntax for the platform you are using. Avoid hiding the Browse button on path controls. Set the browse action correctly for the Browse button on path controls in the Item tab. | If you set a browse action in which a user needs to select a directory, select Select Folder from the Action drop-down menu in the Item tab. |
| Determine whether an enum or ring is more effective than a Boolean. | Recommended | An enum may be more efficient in cases where two states may increase to more states. | N/A |
| Arrange items in a cluster vertically. | Recommended | To arrange items vertically, select Vertical from the Arrange drop-down menu in the Item tab. | N/A |
| Use imported graphics to enhance the panel. Note This guideline is specific to user interfaces. | Recommended | Import graphics and text objects to use as panel backgrounds by dropping URL Image from the Decorations palette and navigating to the image on the Item tab. | N/A |
| Use color logically, sparingly, and consistently, if at all. Note This guideline is specific to user interfaces. | Recommended | Never use color as the sole indicator of device state. Use a minimal number of colors, emphasizing black, white, and gray. Color can be difficult to discern or distract the user from important information. Use light gray, white, or pastel colors for backgrounds. Use bright, highlighting colors only when a term is important, such as an error notification. Because multi-plot graphs and charts can lose meaning when displayed in black and white, use different plot styles, such as dots, and dashes, in addition to color to further differentiate multiple plots. | A yellow, green, or bright orange background makes it difficult to see a red danger light. People with some degree of color-blindness can struggle to detect certain color changes. You can upload an image of your panel to an online color blindness simulator to test your panel under various degrees of color blindness. |

Parent topic:

Best Practices for Creating Projects in G Web Development Software

Related concepts:

- Best Practices for Creating Projects in G Web Development Software

Related reference:

- File and Project Organization in G Web Development Software
- Icons and Connector Panes for Distributed APIs
- Diagram Design for G Web Development Software Projects
- Localization for LabVIEW NXG Projects

<!--NI_TOPIC bundle=labview-nxg-g-programming-api-overview path=place-diagram-contents.html language=enus -->
## TOPIC 00039: Adding Code Snippets to a Custom Palette

- bundle_id: `labview-nxg-g-programming-api-overview`
- source_path: `place-diagram-contents.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-g-programming-api-overview/raw/resource/enus/place-diagram-contents.html
- document_id: `labview-nxg-g-programming-api-overview`
- page_type: `leaf`
- content_type: `task`
- source_description: Add items to a palette file (.gpal) that include chunks of code from your diagram. Before you begin, complete the following prerequisite tasks: Enable .gpal option to place diagram contents when dropped.Enable preview features.Relaunch G Web Development Software. Create a VI within your project. Cre

Adding Code Snippets to a Custom
 Palette

Add items to a palette file (.gpal) that include chunks of code from
 your diagram.

- Enable .gpal option to place diagram contents when
 dropped.
- Enable preview features .
- Relaunch G Web Development Software.

1. [Create a VI within your project.](/csh?topicname=create-vi.html)
2. [Create a library.](/csh?topicname=creating-library.html)
3. Add the VI to the library.
4. On the 
 Document tab of a Library document, click 
 Create palette file.
5. Select G diagram palette from the palette type drop-down
 menu.
6. Open your palette file (.gpal). Select your VI.
7. In the Item tab, under Behavior,
 select Place diagram contents. 
 The block of diagram code from the VI will appear on the diagram in
 projects that include your custom .gpal. org.dita.html5/xsl/topic.xsl 455Note You
 cannot include a VI in an application if any of the exported VIs in the
 library are broken. If a VI in your library containing a snippet is broken,
 disable the VI's Export box before building the
 package.

Parent topic:

Programming in G

<!--NI_TOPIC bundle=labview-nxg-g-programming-api-overview path=reading-data-from-a-database.html language=enus -->
## TOPIC 00040: Reading Data from a Database

- bundle_id: `labview-nxg-g-programming-api-overview`
- source_path: `reading-data-from-a-database.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-g-programming-api-overview/raw/resource/enus/reading-data-from-a-database.html
- document_id: `labview-nxg-g-programming-api-overview`
- page_type: `leaf`
- content_type: `task`
- source_description: Read data from a connected database for use in your code. Connect to a database using the Open Connection node. Insert a Select Data node. To limit the amount of data read from a large database, connect a string control to the columns input and select the columns you want to read. Customize the gray

Reading Data from a Database

Read data from a connected database for use in your code.

1. Connect to a database using the Open Connection
 node.
2. Insert a Select Datanode. To limit the amount of data
 read from a large database, connect a string control to the
 columns input and select the columns you want to
 read. Customize the gray sections for your unique programming goals.
3. Connect a variant array constant to the
 data output to read and interact with the returned
 data. Microsoft ActiveX Data Objects (ADO) use variants as data types. Use
 Variant to Data to convert variant data for use in
 graphs, charts, or LEDs. Customize the gray sections for your unique
 programming goals.
4. Use a Close Connection node to close the connection with a
 database.

[IMAGE alt='1378' src='GUID-91E30A44-9623-4AEF-9576-0A8ACEE2FB73-a5.png']

Parent topic:

Database Connectivity

<!--NI_TOPIC bundle=labview-nxg-g-programming-api-overview path=repeating-operations-once-every-element-array.html language=enus -->
## TOPIC 00041: Repeating Operations Once for Every Element in an Array

- bundle_id: `labview-nxg-g-programming-api-overview`
- source_path: `repeating-operations-once-every-element-array.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-g-programming-api-overview/raw/resource/enus/repeating-operations-once-every-element-array.html
- document_id: `labview-nxg-g-programming-api-overview`
- page_type: `leaf`
- content_type: `task`
- source_description: While working with an array of data, you might want to access individual elements within the array. Although you can use a combination of Array nodes to accomplish this task, the For Loop includes an auto-indexing tunnel that you can use to access the individual elements with minimal additional code

Repeating Operations Once for Every Element in an Array

While working with an array of data, you might want to access individual elements within the array. Although you can use a combination of Array nodes to accomplish this task, the For Loop includes an auto-indexing tunnel that you can use to access the individual elements with minimal additional code.

Use a For Loop with an auto-indexing input tunnel to process one element of an array during each iteration of the loop. A For Loop with an auto-indexing input tunnel behaves similarly to a 
 for each loop in other programming languages.

#### What to Use

[For Loop](/csh?topicname=for-loop.html) with an auto-indexing input tunnel

#### What to Do

Create the following diagram to repeat an operation once for every element in an array.

Customize the gray sections for your unique programming goals.

[IMAGE alt='1378' src='GUID-81915C7A-852C-4361-9DA5-578078E4AD12-a5.png']

|  | Place the code you want to repeat on the subdiagram of a For Loop. |
| --- | --- |
|  | When you wire an array to a For Loop, the For Loop processes one element of the array at a time. This configuration, known as auto-indexing, occurs by default. The input tunnel appears as a white box with brackets to indicate that it is an auto-indexing tunnel. Note A For Loop can process multiple arrays one element at a time using multiple auto-indexing input tunnels. In this situation, the loop uses the smallest array size to determine the number of loop iterations. For example, if two auto-indexed arrays enter the loop with 10 and 20 elements respectively, the loop executes 10 times, processing all elements of the first array but only the first 10 elements of the second array. |
|  | You can access each individual element of the input array by wiring the auto-indexing tunnel to the code on the subdiagram of the loop. The wire entering the auto-indexing tunnel carries 1D array data, whereas the wire leaving the auto-indexing tunnel carries scalar data. Note For multidimensional input arrays, the wire leaving the auto-indexing tunnel carries array data that is one dimension smaller than the input array. For example, if the input array terminal passes a 2D array to the auto-indexing tunnel, the wire leaving the auto-indexing tunnel carries 1D array data. |
|  | By not wiring a value to the count terminal when auto-indexing is enabled, the loop automatically iterates once for each element in the array. Note Wiring a value to the count terminal while auto-indexing is enabled causes the For Loop to use the smallest of the choices between the count terminal and the input array size to determine the number of loop iterations. For example, if an auto-indexed array enters the loop with 10 elements and you wire a value of 15 to the count terminal, the loop executes 10 times. |
|  | If you want to collect the result of each loop iteration in an array, use an auto-indexing output tunnel to pass values out of the loop. To enable auto-indexing for an output tunnel, right-click the tunnel and select Append Mode » Auto Index Values. If you do not enable auto-indexing, the loop returns only the value from the last loop iteration. |

#### Troubleshooting

- If the For Loop 
 iterates an unexpected number of times, note that if you enable auto-indexing
 for more than one input tunnel or if you wire a value to the count terminal, the
 actual number of loop iterations becomes the smallest of the choices.
- If the For Loop 
 processes the entire input array in a single loop iteration instead of one
 element per iteration, verify that the input tunnel is auto-indexing the array.
 An auto-indexing tunnel appears as a white box with brackets, whereas a
 non-indexing tunnel appears as a solid box.
- If the execution
 speed of the loop is too fast, place a Wait node on the
 subdiagram of the loop to specify a wait period.

Parent topic:

Repeating Operations

Related concepts:

- Loop Timing

Related tasks:

- Repeating Operations
- Repeating Operations a Set Number of Times
- Repeating Operations until a Condition Occurs

<!--NI_TOPIC bundle=labview-nxg-g-programming-api-overview path=repeating-operations-until-condition-occurs.html language=enus -->
## TOPIC 00042: Repeating Operations until a Condition Occurs

- bundle_id: `labview-nxg-g-programming-api-overview`
- source_path: `repeating-operations-until-condition-occurs.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-g-programming-api-overview/raw/resource/enus/repeating-operations-until-condition-occurs.html
- document_id: `labview-nxg-g-programming-api-overview`
- page_type: `leaf`
- content_type: `task`
- source_description: In some situations, you might know that you want to repeat an operation, but you do not know exactly how many times you want to repeat that operation. Instead, you know only that the operation should repeat until a certain condition occurs. For example, you might have a program you want to run repea

Repeating Operations until a Condition Occurs

In some situations, you might know that you want to repeat an operation, but you do not know exactly how many times you want to repeat that operation. Instead, you know only that the operation should repeat until a certain condition occurs. For example, you might have a program you want to run repeatedly until a user clicks a stop button or until the code inside the loop produces a particular value.

Use a While Loop to repeat code until a specified condition is met. A While Loop behaves similarly to a 
 do while loop in other programming languages.

#### What to Use

[While Loop](/csh?topicname=while-loop.html)

#### What to Do

Create the following diagram to repeat an operation until a condition occurs.

Customize the gray sections for your unique programming goals.

[IMAGE alt='1378' src='GUID-89659802-CC85-41BC-B657-49415B4A7FCD-a5.png']

|  | Place the code you want to repeat on the subdiagram of a While Loop. |
| --- | --- |
|  | To specify the condition under which the loop stops, create code that produces a True Boolean value when the desired stop condition occurs and wire that Boolean value to the condition terminal. By default, the condition terminal is configured to Stop if True. To stop the loop for a False Boolean value instead of a True value, right-click the condition terminal and select Continue if True. You can also specify when the loop stops by wiring an error cluster to the condition terminal. In this situation, the Boolean value of the status of the error is used to determine when the loop stops. |
|  | If you want to know how many loop iterations executed before the stop condition occurred, use the iteration terminal to return the current loop iteration count. The iteration terminal is zero-indexed, meaning it ranges from 0 to n -1. Use Increment to obtain the true number of loop iterations. Note A While Loop always executes at least one time. |
|  | If you want to collect the result of each loop iteration in an array, use an auto-indexing output tunnel to pass values out of the loop. To enable auto-indexing for an output tunnel, right-click the tunnel and select Append Mode » Auto Index Values. If you do not enable auto-indexing, the loop returns only the value from the last loop iteration. |

#### Troubleshooting

If the execution
 speed of the loop is too fast, place a Wait node on the
 subdiagram of the loop to specify a wait period.

Parent topic:

Repeating Operations

Related concepts:

- Loop Timing

Related tasks:

- Repeating Operations
- Repeating Operations a Set Number of Times
- Repeating Operations Once for Every Element in an Array

<!--NI_TOPIC bundle=labview-nxg-g-programming-api-overview path=repeating-operations.html language=enus -->
## TOPIC 00043: Repeating Operations

- bundle_id: `labview-nxg-g-programming-api-overview`
- source_path: `repeating-operations.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-g-programming-api-overview/raw/resource/enus/repeating-operations.html
- document_id: `labview-nxg-g-programming-api-overview`
- page_type: `leaf`
- content_type: `task`
- source_description: When building an application, you may need to repeat code a set number of times or until a specified condition is met. For example, you may have a section of code that you know you want to run three times. You may want your code to keep running until a user clicks a stop button. You can use loops to

Repeating Operations

When building an application, you may need to repeat code a set number of times or until a specified condition is met. For example, you may have a section of code that you know you want to run three times. You may want your code to keep running until a user clicks a stop button. You can use loops to do this.

loop

Parent topic:

Programming in G

Related tasks:

- Repeating Operations until a Condition Occurs
- Repeating Operations a Set Number of Times
- Repeating Operations Once for Every Element in an Array

<!--NI_TOPIC bundle=labview-nxg-g-programming-api-overview path=stacked-shift-register.html language=enus -->
## TOPIC 00044: Accessing Data from Multiple Past Loop Iterations

- bundle_id: `labview-nxg-g-programming-api-overview`
- source_path: `stacked-shift-register.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-g-programming-api-overview/raw/resource/enus/stacked-shift-register.html
- document_id: `labview-nxg-g-programming-api-overview`
- page_type: `leaf`
- content_type: `task`
- source_description: A shift register passes values from one loop iteration to the next, but sometimes you need to access values from more than just the previous iteration. What to Use For Loop or While Loop What to Do Create the following diagram to pass data from the two most recent loop iterations to the current iter

Accessing Data from Multiple Past Loop Iterations

A shift register passes values from one
 loop iteration to the next, but sometimes you need to access values from more than just
 the previous iteration.

#### What to Use

- For Loop 
 or While
 Loop

#### What to Do

Create the following diagram to pass data from the two most recent loop iterations to the current iteration.

Customize the gray sections for your unique programming goals.

[IMAGE alt='1378' src='GUID-FE546E59-5BC4-44A8-AB25-850D366C5A46-a5.png']

|  | A right shift register always passes data to the next loop iteration, regardless of whether you want to share data among one or multiple loop iterations. To create a pair of shift registers, right-click the loop border and select Create Shift Register. |
| --- | --- |
|  | After each iteration, the first left shift register contains the data passed from the right shift register. Access this data by wiring the output of the first left shift register to the code inside the loop. |
|  | The second left shift register contains the data from the second most recent iteration. |
|  | Just like for single shift registers, specify an initial value for each stacked shift register to ensure that each one has a predictable value for the first loop iteration. Each left shift register that lacks an initial value uses the most recent value it contained, even if that value is from a previous loop execution. |
|  | After the loop executes, access the data from the last iteration by wiring the output of the right shift register to the rest of the program. Only values from the last iteration exit the loop through the output of the right shift register. |

#### Examples

In the previous example, the value contained in each shift register changed after each loop iteration. The following table records the data each shift register contains after each loop iteration, assuming the following conditions:

- The 
 loop count is 3.
- The 
 initial value wired to the first left shift register is 5.
- The 
 initial value 2 wired to the second left shift register is 2.

| Shift Register | Note | First Iteration Value | Second Iteration Value | Third Iteration Value |
| --- | --- | --- | --- | --- |
| First left shift register | The first left shift register receives new values from the right shift register. | 5 | 7 | 12 |
| Second left shift register | The second left shift register receives new values from first left shift register. | 2 | 5 | 7 |
| Right shift register | The right shift register receives values from the subdiagram of the loop. | 7 | 12 | 19 |

Parent topic:

Repeating Operations

Related tasks:

- Accessing Data from the Previous Loop Iteration

<!--NI_TOPIC bundle=labview-nxg-g-programming-api-overview path=storing-data-with-dvr.html language=enus -->
## TOPIC 00045: Storing Data with Data Value References to Manage Memory

- bundle_id: `labview-nxg-g-programming-api-overview`
- source_path: `storing-data-with-dvr.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-g-programming-api-overview/raw/resource/enus/storing-data-with-dvr.html
- document_id: `labview-nxg-g-programming-api-overview`
- page_type: `leaf`
- content_type: `task`
- source_description: Create a data value reference to store a single copy of a set of data. You can help manage memory and avoid frequent data copies that cause slower performance and out-of-memory errors by using data value references to store large data sets. What to Use New Data Value Reference DVR Read/Write Element

Storing Data with Data Value References to Manage Memory

Create a data value reference to store a single copy of a set of data. You can help manage memory and avoid frequent data copies that cause slower performance and out-of-memory errors by using data value references to store large data sets.

#### What to Use

- New Data Value Reference
- DVR Read/Write Elements of the In Place Element Structure
- Delete Data Value Reference

#### What to Do

Create the following diagram to store, access, and operate on data using a data value reference.

Customize the gray sections for your unique programming goals.

[IMAGE alt='1378' src='GUID-CC632801-E42C-44FD-8B80-F32B91AEE46D-a5.png']

|  | Store any type of data in memory and return a reference to that data with a data value reference. Because the reference points to the data stored in memory, you can access the reference inside In Place Element Structures. The In Place Element Structure allows you to access and update the data without creating and maintaining multiple copies of the data in memory. |
| --- | --- |
|  | Add read and write elements to the In Place Element Structure using the Create DVR Read/Write Elements button in the Item tab and wire the data value reference to the Read Data Value Reference Element. |
|  | Use any nodes available in the context of the In Place Element Structure to operate on the data. The resulting data set must be the same data type as the data set that you originally stored in the data value reference. |
|  | The Write Data Value Reference Element places the resulting data set in the original memory space. Note The data value reference does not save or maintain previous copies of the data anywhere in memory. If you want to maintain a log or history of your data, implement another data storage strategy. |
|  | Remove access to the data stored in the reference to prevent memory leakage. Delete Data Value Reference deletes the reference but leaves the stored data intact. |

Parent topic:

Programming in G

<!--NI_TOPIC bundle=labview-nxg-g-programming-api-overview path=strategies-for-improving-vi-execution-speed.html language=enus -->
## TOPIC 00046: Strategies for Improving VI Execution Speed

- bundle_id: `labview-nxg-g-programming-api-overview`
- source_path: `strategies-for-improving-vi-execution-speed.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-g-programming-api-overview/raw/resource/enus/strategies-for-improving-vi-execution-speed.html
- document_id: `labview-nxg-g-programming-api-overview`
- page_type: `leaf`
- content_type: `concept`
- source_description: Factors like inefficient memory use, poorly designed panels, and too many I/O calls can negatively affect the execution speed of your VI. However, there are several strategies you can use to ensure that your VI runs more efficiently. Strategies for Improving Execution Speed through Memory Management

Strategies for Improving VI Execution Speed

Factors like inefficient memory use, poorly designed panels, and too many I/O calls can negatively affect the execution speed of your VI.
 However, there are several strategies you can use to ensure that your VI runs more efficiently.

Parent topic:

Programming in G

#### Strategies for Improving Execution Speed through Memory Management

Effective memory management can improve the execution speed of your VI. By minimizing memory usage, you can help alleviate slow VI execution speeds, which are affected by allocation and deallocation operations. 
 Execution speed is indirectly affected by the allocation of more space in memory because operations slow down if they reach the memory's capacity.

The more you allocate, deallocate, or move data in memory, the more memory the VI uses. Memory can also indirectly affect execution speed because allocating more space in memory leaves less memory for other operations, causing them to slow down if they reach the memory's capacity.

When creating a VI, consider the following guidelines:

- Use consistent data types and watch for coercion dots when passing data to subVIs.
- Avoid using hierarchical data types such as arrays of clusters containing large arrays or strings.
- Reduce the use of nested subVIs inside of other VIs, as these can cause an exponential increase in the number of VI clones needed to maintain separate data spaces for each call to a subVI.

Avoid the following, which can create additional and unnecessary copies of data:

- Repeatedly resizing data—Clearing space in memory or adding and removing data from memory creates overhead and can take time.
- Overusing duplicated array and string terminals—Creating more than one corresponding object on the diagram can increase memory usage.
- Unintentionally coercing data—Coercion dots appear on nodes when data types are coerced. Data type coercion can decrease execution speed and increase memory usage, especially when you use complex data types or large arrays because they can increase memory usage.
- Displaying large arrays and strings on panels—Displaying the smallest array or string on the panel will ensure that copies of data remain small. The larger the array or string, the larger the copy of contained data.

#### Strategies for Improving Execution Speed by
 Minimizing I/O Calls

I/O calls can incur a significant amount of overhead and take more time than a computational operation because I/O calls have to wait on external resources. 
 You can improve VI execution speed by using various strategies to troubleshoot or optimize I/O calls.

The following example diagram shows an inefficiently structured loop. The loop is inefficient because the I/O functions within the loop run multiple times unnecessarily and are structured to write a small amount of data each iteration.

[IMAGE alt='1378' src='GUID-255D555A-FE99-4CEF-87F6-D3848960AA47-a5.png']

When troubleshooting or optimizing your I/O calls, examine the following items to ensure your loop runs efficiently:

- I/O calls—You can reduce excessive overhead by reducing the number of I/O Write or Read calls. Limit the use of nodes within your loop that interact with external resources. Nodes like Write to Text File and TCP Write can incur the overhead of the external resource they interact with, like a network card, an OS, or file system.
- Data transfer quantities—Instead of making multiple I/O calls with smaller quantities of data, structure the VI to transfer large amounts of data with each call. Consolidate data into large chunks by using arrays and concatenated strings whenever possible.
- Unnecessary nodes outside of loops—Avoid putting a node in a loop if the node produces the same value for every iteration. Instead, move the node out of the loop and pass the result into the loop. Also, keep nodes that open or close references such as TCP Open Connection and Close File outside of loops to avoid repetitive overhead delays when interacting with external resources.

The following example diagram shows the loop restructured for efficiency:

[IMAGE alt='1378' src='GUID-1C860F4A-A87F-42FC-8955-E1BF9B93BB31-a5.png']

1. The loop is efficient because it minimizes the number of I/O calls.
2. The loop is structured to transfer significant amounts of data with each call.
3. The loop does not contain unnecessary computations.

#### Guidelines for Designing Efficient Panels

Optimizing your panel can improve the execution speed of your VI. 
 Design and configure your panel according to the following guidelines:

- Remove unnecessary panel objects and avoid adding objects to the panel that aren't necessary for controlling input to the diagram or observing output data.
- Avoid transparent and overlapped panel objects unless necessary.
- When using charts, reducing Chart History Length in the Configuration pane will set the maximum number of data points drawn to your chart.
- When using graphs and charts, turn off auto-scaling, axis labels, anti-aliased line drawing, and axis grids to prevent drawing more elements. A graph with fewer elements takes less time to redraw every time the graph updates.

#### Using Parallel Loops to Increase VI Execution Speed

When multiple loops run in parallel, the VI switches between them periodically. 
 Parallel loops can help decrease execution time by simultaneously running independent tasks within individual loops. 
 In the following example diagram, a single loop contains multiple independent tasks. This loop is inefficient because execution speeds can vary due to the lack of loop timing. In this example, the DAQ operation must wait for the slower I/O function and a status check to complete each iteration.

[IMAGE alt='1378' src='GUID-633AA8AE-1DA2-4DB6-ABF8-2B613359B263-a5.png']

Since all parallel loops share the same processor resources, consider the following practices to make sure other loops do not interrupt the timing or execution of your important tasks:

- Important Operations—Because you want this type of operation to execute as frequently as possible, do not add timing nodes inside the loop to delay its execution.
- Executions Dependent on Dequeue Element node—The Dequeue Element node can halt the execution of a loop until an element is ready in the queue. This node allows more important loops to use more of the processor's time.
- Low-Importance Operations—Because this type of operation is the least important, you can use a Wait node to run the operation less often and yield execution time to the other loops.

The following is an example of a recreated VI using the considerations:

[IMAGE alt='1378' src='GUID-0F9586DE-0938-4247-841E-C0151C504258-a5.png']

1. The Read DAQ loop reads data from a DAQ device and sends the data to a queue. Do not add timing nodes because you want this type of operation to execute as frequently as possible.
2. The Write to File loop can execute more slowly as it is logging data points for later analysis. The execution of this loop can be dependent on elements being ready in the queue because it does not need to execute as frequently.
3. The Check Temperature loop displays temperature data to the user and uses a Wait node to run less often and yield execution time to the other loops because it is the least important.

<!--NI_TOPIC bundle=labview-nxg-g-programming-api-overview path=supported-data-types-and-portability-issues.html language=enus -->
## TOPIC 00047: Supported Data Types and Portability Issues with Database Connectivity

- bundle_id: `labview-nxg-g-programming-api-overview`
- source_path: `supported-data-types-and-portability-issues.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-g-programming-api-overview/raw/resource/enus/supported-data-types-and-portability-issues.html
- document_id: `labview-nxg-g-programming-api-overview`
- page_type: `leaf`
- content_type: `reference`
- source_description: Because the Database Connectivity API works with a wide range of databases, you may encounter portability issues due to different data types or table elements in the databases you work with. Consider the following issues when choosing your database system: Type of Support Issue What To Do Flat-file

Supported Data Types and Portability Issues
 with Database Connectivity

Because the Database Connectivity API works with a wide range of databases, you may
 encounter portability issues due to different data types or table elements in the databases
 you work with. Consider the following issues when choosing your database system:

| Type of Support Issue | What To Do |
| --- | --- |
| Flat-file databases do not support floating-point numbers. | Database Connectivity nodes will automatically convert floating-point numbers to the nearest equivalent- usually a binary-coded decimal (BCD) before storing them in the database. |
| Microsoft Open Database Connectivity (ODBC) drivers for Oracle and the Microsoft Object Linking and Embedding Database Provider (OLE DB) for Oracle do not support binary large object (BLOB) data types. You cannot use Oracle with LabVIEW NXG for binary data with these drivers. | Use the OLE DB Provider and ODBC driver that Oracle provides. Refer to the Oracle website for more information. |
| Restrictions on column names and column name length vary among database systems. | Limit column names to ten uppercase characters without spaces for maximum portability. To access longer column or field names, or names that contain spaces, try enclosing the names in double quotation marks. |
| Some database systems do not support date, time, or datetime data types. | Format this data into another compatible data type, such as string or number data. Use a different database type if storing date, time, or datetime data is necessary. |

Parent topic:

Database Connectivity

<!--NI_TOPIC bundle=labview-nxg-g-programming-api-overview path=synch-timed-loops-single.html language=enus -->
## TOPIC 00048: Synchronizing Timed Loops on a Single Device

- bundle_id: `labview-nxg-g-programming-api-overview`
- source_path: `synch-timed-loops-single.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-g-programming-api-overview/raw/resource/enus/synch-timed-loops-single.html
- document_id: `labview-nxg-g-programming-api-overview`
- page_type: `leaf`
- content_type: `task`
- source_description: If you have two Timed Loops on the diagram, you can ensure that they execute on the same schedule relative to each other. For example, you can configure loop A to execute first and generate data. You then can configure loop B to process that data when an iteration of loop A finishes. To ensure that

Synchronizing Timed Loops on a Single Device

Timed Loops

For example, you can configure loop A to execute first and generate data. You then can configure loop B to process that data when an iteration of loop A finishes. To ensure that both loops use the same start time as the basis for their execution, you can synchronize the start time of the Timed Loops.

#### What to Use

- Synchronize Timed Structure Starts
- Two or more Timed Loops

#### What to Do

Create the following diagram to synchronize the start of two or more Timed Loops that are executing on a single device.

Customize the gray sections for your unique programming goals.

[IMAGE alt='1378' src='GUID-79B95D7E-7EB6-430F-81EE-5678082CCF1C-a5.png']

|  | Each Timed Loop that you want to synchronize must have a unique name. |
| --- | --- |
|  | Creating a synchronization group using Synchronize Timed Structure Starts specifies which Timed Loops on the diagram you want to synchronize. The synchronization group name can be any string that you want to use to identify a specific group. A synchronization group remains active until the VI completes execution. Note A Timed Loop cannot belong to more than one synchronization group. |
|  | Configuring one loop to start a set amount of time after the previous loop ensures that the first loop executes and generates data before the second loop executes. |

#### Troubleshooting

If the start times of your Timed Loops do not align, verify that you did not add one Timed Loop to more than one synchronization group. By default, Synchronize Timed Structure Starts deletes a Timed Loop from its current group and adds it to the group you specify in synchronization group name on the node that executes last. If you set replace to False and a Timed Loop you specify in timed structure names is already a member of another group, the node returns an error to indicate that it could not add the Timed Loop to the synchronization group.

Parent topic:

Repeating Operations

<!--NI_TOPIC bundle=labview-nxg-g-programming-api-overview path=synchronizing-operations.html language=enus -->
## TOPIC 00049: Synchronizing the Execution of Multiple Loops

- bundle_id: `labview-nxg-g-programming-api-overview`
- source_path: `synchronizing-operations.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-g-programming-api-overview/raw/resource/enus/synchronizing-operations.html
- document_id: `labview-nxg-g-programming-api-overview`
- page_type: `leaf`
- content_type: `task`
- source_description: By default, each loop iteration executes as quickly as possible based on the code inside the loop. However, consider a program that includes multiple loops that contain code requiring different amounts of time to execute. You might want to control the rate at which those loops execute in order to sy

Synchronizing the Execution of Multiple Loops

By default, each loop iteration executes as quickly as possible based on the code inside the loop. However, consider a program that includes multiple loops that contain code requiring different amounts of time to execute. You might want to control the rate at which those loops execute in order to synchronize their execution and ensure that the loops begin each iteration at the same time. Use Wait Until Next Multiple to do this.

#### What to Use

- While Loop or For Loop
- Wait Until Next Multiple

#### What to Do

Create the following diagram to synchronize the execution of multiple loops.

Customize the gray sections for your unique programming goals.

[IMAGE alt='1378' src='GUID-120DDA40-708D-4346-8FCA-23959768AB55-a5.png']

|  | Wire the same value to the inputs of the Wait Until Next Multiple nodes placed on the subdiagram of each loop. The loops wait until the value of the system clock becomes a multiple of the specified input before beginning each iteration. Therefore, the loops begin each iteration at exactly the same time. |
| --- | --- |
|  | When specifying a value for the input of Wait Until Next Multiple, ensure that the value is greater than the time required to execute the code inside the loop. If a loop contains code that takes longer to execute than the time specified, Wait Until Next Multiple has no effect on the execution speed of the loop. |

Parent topic:

Repeating Operations

Related concepts:

- Loop Timing

<!--NI_TOPIC bundle=labview-nxg-g-programming-api-overview path=terminals-definition.html language=enus -->
## TOPIC 00050: Terminals

- bundle_id: `labview-nxg-g-programming-api-overview`
- source_path: `terminals-definition.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-g-programming-api-overview/raw/resource/enus/terminals-definition.html
- document_id: `labview-nxg-g-programming-api-overview`
- page_type: `leaf`
- content_type: `concept`
- source_description: Terminals transfer data between the diagram and panel, between the diagram and other nodes, or between duplicates of the same terminal on the diagram. As the following example shows, the color and symbol of each terminal indicate the data type of the terminal.

Terminals

Terminals transfer data between the diagram and panel, between the diagram and other nodes, or between duplicates of the same terminal on the diagram.

As the following example shows, the color and symbol of each terminal indicate the data type of the terminal.

[IMAGE alt='1378' src='GUID-54759EF0-56FC-4CBD-B91B-657624C26E99-a5.png']

Parent topic:

Programming in G

<!--NI_TOPIC bundle=labview-nxg-g-programming-api-overview path=transfer-data-loops.html language=enus -->
## TOPIC 00051: Preventing Data Loss When Transferring Data Between Loops

- bundle_id: `labview-nxg-g-programming-api-overview`
- source_path: `transfer-data-loops.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-g-programming-api-overview/raw/resource/enus/transfer-data-loops.html
- document_id: `labview-nxg-g-programming-api-overview`
- page_type: `leaf`
- content_type: `task`
- source_description: Prevent data loss and promote efficiency when transferring data between producer and consumer loops by using queue nodes. By creating a queue of data that is ready to be consumed, a consumer loop can process a greater volume of data at more regular intervals without losing data. This is especially u

Preventing Data Loss When Transferring Data Between Loops

Prevent data loss and promote efficiency when transferring data between producer and consumer loops by using queue nodes.

By creating a queue of data that is ready to be consumed, a consumer loop can process a greater volume of data at more regular intervals without losing data. This is especially useful if data from multiple network channels need to be processed in the order in which they arrive.

#### What to Use

Tip

- Obtain Queue
- Enqueue Element
- Dequeue Element
- Get Queue Status
- Release Queue

#### What to Do

1. Create the following diagram to automate the reading and writing of data without the risk of losing data. 
 
 Customize the gray sections for your unique programming goals. 
 
 [IMAGE alt='1378' src='GUID-97140CE0-AE0F-45D2-BC12-D22F4BA789B6-a5.svg']
 Use Obtain Queue to set the data type for the queue and to set the maximum number of elements the queue can hold. In this example, the queue can hold up to 50 pieces of numeric data. 
 org.dita.html5/xsl/topic.xsl 455Note If you call Obtain Queue inside a loop, this node creates a new reference each time the loop executes, and each new reference uses an additional four bytes of memory. To conserve memory, call Obtain Queue once before the loop executes.
 [IMAGE alt='1378' src='GUID-245F4F1B-3FBD-425A-A6D9-4F445ABFE629-a5.svg']
 Use Enqueue Element in the producer loop to add data to the back of the queue. If the queue is full, the producer loop stops adding elements to the queue until Dequeue Element removes data. If the producer loop runs slower than the consumer loop, the queue will empty and result in an underflow. 
 org.dita.html5/xsl/topic.xsl 455Note If you want to ask a sensor for data at regular intervals instead of as often as possible, use Wait in the producer loop.
 [IMAGE alt='1378' src='GUID-EE38CAD4-C25C-4C69-A3B4-5FD829627100-a5.svg']
 Use Dequeue Element in the consumer loop to remove data from the front of the queue so that data processes in the same order that it is added. If the queue is empty, the consumer loop waits to remove elements from the queue until Enqueue Element adds data. If the consumer loop runs slower than the producer loop, the queue will fill up and result in an overflow.
 [IMAGE alt='1378' src='GUID-1C2B5505-1271-4422-8DB9-8B9B5154C5C4-a5.svg']
 Use Get Queue Status in the queue status loop to return information about the current state of the queue, such as the number of elements currently in the queue.
 org.dita.html5/xsl/topic.xsl 455Note Using this node in parallel code can result in race conditions which can cause incorrect logic control and data loss.
 [IMAGE alt='1378' src='GUID-1CED6939-5ED1-4388-BEB8-FFF164BED4D0-a5.svg']
 Click the 
 Stop button on the panel. The queue status loop finishes executing and calls Release Queue. This node invalidates the queue reference which causes the producer and consumer loops to error out and finish executing. 
 org.dita.html5/xsl/topic.xsl 455Note Larger applications typically require a
 more sophisticated mechanism for stopping parallel
 loops. To see an example of such an architecture,
 launch the Queued Message Handler project in G Web
 Development Software.

#### Troubleshooting

- If a consumer loop processes data too slowly and results in an overflow, add a consumer loop to the diagram to raise the rate of data consumption.
- If a producer loop reads data too slowly and results in an underflow, raise the producer loop time if Wait is used. Otherwise add a producer loop to the diagram to raise the rate of data production.
- When multiple loops execute at the same time and
 change the same object, race conditions can occur which can result in data
 loss. Using Get Queue Status as a control mechanism
 that triggers an event between loops in code could result in race conditions
 if other loops change the contents of the queue before the event can be
 executed. This means that when the event does execute, it may do so based on
 outdated data and overwrite more current data. Improve the speed of your VI
 without the risk of creating race conditions by following the practices
 outlined in the Using Parallel Loops to Increase VI Execution Speed section
 of Strategies for Improving VI Execution Speed . Use
 an event structure as a safer way to trigger your code using event-driven programming .

Parent topic:

Repeating Operations

<!--NI_TOPIC bundle=labview-nxg-g-programming-api-overview path=transferring-data-between-nodes.html language=enus -->
## TOPIC 00052: Wires: Transferring Data between Nodes

- bundle_id: `labview-nxg-g-programming-api-overview`
- source_path: `transferring-data-between-nodes.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-g-programming-api-overview/raw/resource/enus/transferring-data-between-nodes.html
- document_id: `labview-nxg-g-programming-api-overview`
- page_type: `leaf`
- content_type: `concept`
- source_description: Wires transfer data between nodes on a diagram by connecting the output terminal of one node to one or more input terminals of another node. Wires have the following properties: A wire has a single data source. A wire can carry data from its single data source to more than one node that reads the da

Wires: Transferring Data between Nodes

Wires transfer data between nodes on a diagram by connecting the output terminal of one node to one or more input terminals of another node.

Wires have the following properties:

- A wire has a single data source.
- A wire can carry data from its single data source to more than one node that reads the data as an input.
- The color, style, and thickness of a wire represent the type of data passing between nodes.

Parent topic:

Programming in G

<!--NI_TOPIC bundle=labview-nxg-g-programming-api-overview path=troubleshooting-broken-wires.html language=enus -->
## TOPIC 00053: Troubleshooting Broken Wires

- bundle_id: `labview-nxg-g-programming-api-overview`
- source_path: `troubleshooting-broken-wires.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-g-programming-api-overview/raw/resource/enus/troubleshooting-broken-wires.html
- document_id: `labview-nxg-g-programming-api-overview`
- page_type: `leaf`
- content_type: `task`
- source_description: A broken wire indicates that dataflow cannot run across the wire. You cannot run code that contains broken wires. Resolve each wire to make dataflow valid and run the code. Broken wires look like the following image. Make sure your code meets the following requirements to resolve each wire: Each wir

Troubleshooting Broken Wires

A broken wire indicates that dataflow cannot run across the wire. You cannot run code that contains broken wires. Resolve each wire to make dataflow valid and run the code.

Broken wires look like the following image.

[IMAGE alt='1378' src='GUID-E0101ADB-BC41-473D-9A17-67A9D283ED82-a5.png']

Make sure your code meets the following requirements to resolve each wire:

- Each wire has a single data source.
- There are no unwired or overlapping tunnels when wiring through structures.
- All wires are connected to a node.
- Every data source is wired to at least one output. 
 For example, you cannot wire two indicators together.
- The output and input of the same node are not wired together.
- Wire compatible data types together. 
 For example, you cannot wire a Boolean output to a string input.
- Triple-click the wire to select the entire wire. 
 You might see hidden wire segments that help you identify one of the causes listed above.
- Use the error list to find broken wires and an explanation.
- If you still cannot identify the cause of the broken wire, click 
 Remove Broken Wires on the Document toolbar. 
 org.dita.html5/xsl/topic.xsl 455Note 
 Remove Broken Wires deletes all broken wires, even those you might not see.

Parent topic:

Wires: Transferring Data between Nodes

<!--NI_TOPIC bundle=labview-nxg-g-programming-api-overview path=types-of-loops.html language=enus -->
## TOPIC 00054: Types of Loops

- bundle_id: `labview-nxg-g-programming-api-overview`
- source_path: `types-of-loops.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-g-programming-api-overview/raw/resource/enus/types-of-loops.html
- document_id: `labview-nxg-g-programming-api-overview`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use the following loops to repeat code in G Dataflow: a For Loop and a While Loop. Loop Behavior Example Diagram For Loop Repeats the code inside the loop for a set number of iterations. Generate five random numbers between 1 and 10. While Loop Repeats the code inside the loop until a specif

Types of Loops

You can use the following loops to repeat code in G Dataflow: a For Loop and a While Loop.

| Loop | Behavior | Example | Diagram |
| --- | --- | --- | --- |
| For Loop | Repeats the code inside the loop for a set number of iterations. | Generate five random numbers between 1 and 10. |  |
| While Loop | Repeats the code inside the loop until a specified condition is met. | Continue rolling a die until the value of the die is 6. |  |

Parent topic:

Repeating Operations

Related concepts:

- Loop Timing

Related information:

- nihelp://node-ref/while-loop/
- nihelp://node-ref/for-loop/

<!--NI_TOPIC bundle=labview-nxg-g-programming-api-overview path=wiring-best-practices.html language=enus -->
## TOPIC 00055: Wiring Best Practices

- bundle_id: `labview-nxg-g-programming-api-overview`
- source_path: `wiring-best-practices.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-g-programming-api-overview/raw/resource/enus/wiring-best-practices.html
- document_id: `labview-nxg-g-programming-api-overview`
- page_type: `leaf`
- content_type: `concept`
- source_description: Poor wire organization might not produce errors, but it can make the diagram difficult to read and debug or make the code appear to do things it does not do. Use these best practices as you develop your diagrams. Use a left-to-right and top-to-bottom layout. Although the positions of diagram element

Wiring Best Practices

Poor wire organization might not produce errors, but it can make the diagram difficult to read and debug or make the code appear to do things it does not do.
 Use these best practices as you develop your diagrams.

- Use a left-to-right and top-to-bottom layout. Although the positions of diagram elements do not determine execution order, wiring from left to right keeps the diagram organized and easy to understand. Only wires and structures determine execution order.
- Control terminal wires should exit the right side of the terminal, and indicator terminal wires should enter on the left side of the terminal.
- Wire around objects. Do not cover wires with other objects.
- Use as few bends as possible.

Parent topic:

Wires: Transferring Data between Nodes

<!--NI_TOPIC bundle=labview-nxg-g-programming-api-overview path=wiring-shortcuts.html language=enus -->
## TOPIC 00056: Wiring Shortcuts

- bundle_id: `labview-nxg-g-programming-api-overview`
- source_path: `wiring-shortcuts.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-g-programming-api-overview/raw/resource/enus/wiring-shortcuts.html
- document_id: `labview-nxg-g-programming-api-overview`
- page_type: `leaf`
- content_type: `reference`
- source_description: You can use the following set of shortcuts to help you create wires more efficiently. Editor Command Shortcut Action Remove Broken Wires Ctrl-B Delete all broken wires from the diagram. — Esc Right-click Ctrl-Z Delete a wire you are in the process of creating. — Single-click wire Select one wire seg

Wiring Shortcuts

You can use the following set of shortcuts to help you create wires more efficiently.

| Editor Command | Shortcut | Action |
| --- | --- | --- |
| Remove Broken Wires | Ctrl-B | Delete all broken wires from the diagram. |
| — | Esc Right-click Ctrl-Z | Delete a wire you are in the process of creating. |
| — | Single-click wire | Select one wire segment. |
| — | Double-click wire | Select a wire branch. |
| — | Triple-click wire | Select the entire wire. |
| — | Ctrl-click wire | Create a new wire branch from an existing wire. |
| — | Single-click while wiring | Tack down the wire segment and start a new wire segment. |
| — | Double-click while wiring | End the wire without connecting it to a node. |
| — | Tap spacebar while wiring | Switch the direction of a wire between horizontal and vertical. |
| Clean Up Diagram Clean Up Selection | Ctrl-U | Organize the diagram or the selected code to make it easier to understand. |
| Clean Up Wire | Select Clean Up Wire from the shortcut menu | Route a selected wire to decrease the number of bends in the wire and avoid crossing objects on the diagram. |

Parent topic:

Wires: Transferring Data between Nodes

<!--NI_TOPIC bundle=labview-nxg-g-programming-api-overview path=writing-data-to-a-database.html language=enus -->
## TOPIC 00057: Writing Data to a Database

- bundle_id: `labview-nxg-g-programming-api-overview`
- source_path: `writing-data-to-a-database.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-g-programming-api-overview/raw/resource/enus/writing-data-to-a-database.html
- document_id: `labview-nxg-g-programming-api-overview`
- page_type: `leaf`
- content_type: `task`
- source_description: Write data to a connected database. Connect to a database using the Open Connection node. Insert an Insert Data node. To create a new table, connect a True constant to the create table? input. To add data to existing tables and columns, connect string or string array constants representing table and

Writing Data to a Database

Write data to a connected database.

1. Connect to a database using the Open Connection
 node.
2. Insert an Insert Data node. To create a new table, connect
 a True constant to the create
 table? input. To add data to existing tables and columns,
 connect string or string array
 constants representing table and column names to the
 table and columns
 inputs.Customize the gray sections for your
 unique programming goals.
3. Connect a variant or variant array to
 the data input. This data will be written to the
 database,
4. Place a Close Connection node to close the connection with
 a database.

[IMAGE alt='1378' src='GUID-625D62E1-3510-414B-BAD7-85832451796A-a5.png']

Parent topic:

Database Connectivity
