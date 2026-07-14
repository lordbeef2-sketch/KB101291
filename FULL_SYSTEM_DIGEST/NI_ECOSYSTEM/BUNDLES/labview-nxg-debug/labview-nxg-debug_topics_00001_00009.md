# NI DOCUMENT BUNDLE: labview-nxg-debug

<!--NI_BUNDLE_CHUNK bundle=labview-nxg-debug start=1 end=9 -->
<!--NI_TOPIC bundle=labview-nxg-debug path=breakpoints.html language=enus -->
## TOPIC 00001: Pausing Execution with Breakpoints

- bundle_id: `labview-nxg-debug`
- source_path: `breakpoints.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-debug/raw/resource/enus/breakpoints.html
- document_id: `labview-nxg-debug`
- page_type: `leaf`
- content_type: `concept`
- source_description: When looking for a problem in your code, you may have an idea of the general area where the problem exists. To help focus on this area, you can use a breakpoint to pause the VI at a specified point in the program. When the VI reaches a breakpoint during execution, you can take the following actions:

Pausing Execution with Breakpoints

When looking for a problem in your code, you may have an idea of the general area where the problem exists. To help focus on this area, you can use a breakpoint to pause the VI at a specified point in the program.

When the VI reaches a breakpoint during execution, you can take the following actions:

- Single-step through execution using the single-stepping buttons.
- Check intermediate values on probes that you placed on wires prior to running the VI.
- Change values of panel controls.
- Click the 
 Resume button to continue running to the next breakpoint or until the VI finishes running.

[IMAGE alt='1378' src='GUID-4F3C782C-A392-45AF-8298-23FAC59ECF29-a5.png']

You can add a breakpoint to any wire or node in the code, or in a row of a
 text-based programming node. Add a breakpoint by right-clicking the wire, node, or row
 and selecting Add breakpoint.

You can add conditional logic to a breakpoint to pause execution if a condition is met.
 Add a condition by right clicking the breakpoint and selecting Pause on
 condition. Configure the conditions of the breakpoint in the
 Debugging pane.

Parent topic:

Testing and Debugging

<!--NI_TOPIC bundle=labview-nxg-debug path=debugging-tools.html language=enus -->
## TOPIC 00002: Testing and Debugging

- bundle_id: `labview-nxg-debug`
- source_path: `debugging-tools.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-debug/raw/resource/enus/debugging-tools.html
- document_id: `labview-nxg-debug`
- page_type: `leaf`
- content_type: `concept`
- source_description: When the results of your application are not what you expect, use a set of tools to determine where errors occur within your code. Although errors are often detected automatically, sometimes your code can run successfully but not as intended. When this happens, you need to identify the source of the

Testing and Debugging

When the results of your application are not what you expect, use a
 set of tools to determine where errors occur within your code.

Although errors are often detected automatically, sometimes your code can run successfully but not as intended. When this happens, you need to identify the source of the unintended behaviors.

The following debugging tools can help you in this process:

- Probes
- Breakpoints

<!--NI_TOPIC bundle=labview-nxg-debug path=execution-logs.html language=enus -->
## TOPIC 00003: Improve Applications with Execution Logs

- bundle_id: `labview-nxg-debug`
- source_path: `execution-logs.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-debug/raw/resource/enus/execution-logs.html
- document_id: `labview-nxg-debug`
- page_type: `leaf`
- content_type: `concept`
- source_description: Well-written applications use execution logs for both activity audit and monitoring. An execution log makes it easy for a developer or user to track and identify issues that occur throughout the application without excessive effort.Maintaining an execution log allows you to review all activity and m

Improve Applications with Execution Logs

Well-written applications use execution logs for both activity audit and monitoring. An execution log makes it easy for a developer or user to track and identify issues that occur throughout the application without excessive effort.Maintaining an execution log allows you to review all activity and make improvements to your application accordingly.

An application should record data from multiple execution points throughout an application—errors, exceptions, successful execution, and so on. An execution log can help you recreate a certain behavior and improve your application effectively. For example, you can use the log to do one or more of the following:

- Modify the code to be able to handle a situation that caused an error
- Modify the code based on the most common use case
- Update the documentation for the application so that users interact with the application in a more predictable way
- Validate successful execution

The execution log should include as much information as you need to understand the state of the product at the time the data was collected.

- The current time and date
- A pre-defined category for the activity
- A running count of the specific type of activity
- A description of the activity
- The value of data that was generated during or prior to the activity
- The location of the activity within the application
- The type and severity of the problem, if there is one

Parent topic:

Testing and Debugging

<!--NI_TOPIC bundle=labview-nxg-debug path=highlight-execution.html language=enus -->
## TOPIC 00004: Highlighting Execution of the Diagram

- bundle_id: `labview-nxg-debug`
- source_path: `highlight-execution.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-debug/raw/resource/enus/highlight-execution.html
- document_id: `labview-nxg-debug`
- page_type: `leaf`
- content_type: `concept`
- source_description: Execution highlighting reduces the speed of execution and displays data bubbles that move along the wires, revealing the data that each node receives when it executes. When you begin debugging a program, you may not be able to identify which part of the code introduces the incorrect behavior. To gai

Highlighting Execution of the Diagram

*Execution highlighting* reduces the speed of execution and displays data bubbles that move along the wires, revealing the data that each node receives when it executes.

When you begin debugging a program, you may not be able to identify which part of the code introduces the incorrect behavior. To gain a better idea of how data progresses and changes as it flows through the code, you can use execution highlighting.

Execution highlighting helps you detect the following kinds of unintended behavior:

- While Loops that never terminate
- Case Structures that execute an unexpected case
- Data values that do not match the expected value

You can turn on execution highlighting by clicking the 
 Highlight execution button on the document toolbar.

Parent topic:

Testing and Debugging

<!--NI_TOPIC bundle=labview-nxg-debug path=identifying-errors.html language=enus -->
## TOPIC 00005: Identifying Errors That Prevent You from Running Code

- bundle_id: `labview-nxg-debug`
- source_path: `identifying-errors.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-debug/raw/resource/enus/identifying-errors.html
- document_id: `labview-nxg-debug`
- page_type: `leaf`
- content_type: `concept`
- source_description: As you create code, a broken Run button communicates that the code contains errors that prevent it from running. You can use the provided error and warning messages to help fix these problems. Errors break the code. You must resolve any errors before you can run the program. Warnings do not prevent

Identifying Errors That Prevent You from Running Code

As you create code, a broken 
 Run button 
 [IMAGE alt='1378' src='GUID-EDAB8A33-591F-407B-99DB-B44A700348E7-a5.png'] communicates that the code contains errors that prevent it from running.

You can use the provided error and warning messages to help fix these problems. 
 *Errors* break the code. You must resolve any errors before you can run the program. 
 *Warnings* do not prevent you from running the code. They are designed to help you avoid potential problems in the program.

To identify the specific errors, click the broken 
 Run button to display the 
 Errors and Warnings tab. The following image highlights sections of the 
 Errors and Warnings tab that define detected errors and warnings.

[IMAGE alt='1378' src='GUID-0FEF9A0D-6D1D-4755-B12B-E669CF569F1B-a5.png']

|  | Severity—Denotes whether an issue is an error or a warning. |
| --- | --- |
|  | Source—Identifies the object that is causing the error or warning. |
|  | Message—Provides more detail about why the error or warning exists. |

Parent topic:

Testing and Debugging

<!--NI_TOPIC bundle=labview-nxg-debug path=probe-prev-exec.html language=enus -->
## TOPIC 00006: Viewing Wire Data from the Previous VI Execution

- bundle_id: `labview-nxg-debug`
- source_path: `probe-prev-exec.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-debug/raw/resource/enus/probe-prev-exec.html
- document_id: `labview-nxg-debug`
- page_type: `leaf`
- content_type: `task`
- source_description: You can configure a VI to retain wire values on the diagram so that when you create a probe, the probe displays the most recent data that flowed through the wire at the last VI execution. Retaining wire values can help you debug a VI when a diagram is complex and you need to view specific wire data

Viewing Wire Data from the Previous VI Execution

You can configure a VI to retain wire values on the diagram so that when you create a probe, the probe displays the most recent data that flowed through the wire at the last VI execution.

Retaining wire values can help you debug a VI when a diagram is complex and you need to view specific wire data after a VI finishes executing to determine where an error occurred.

1. Click the 
 Retain wire values button on the document toolbar to start retaining all wire values on the diagram.
2. Run the VI at least once so that wire values are immediately available to any probes you create.
3. Place a probe on a specific wire by right-clicking the wire and selecting
 Add probe. 
 To see the most recent value of the data that passed through the wire,
 either hover over the wire or click the probe.

Parent topic:

Testing and Debugging

<!--NI_TOPIC bundle=labview-nxg-debug path=probes.html language=enus -->
## TOPIC 00007: Using Probes to Check Values on a Wire

- bundle_id: `labview-nxg-debug`
- source_path: `probes.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-debug/raw/resource/enus/probes.html
- document_id: `labview-nxg-debug`
- page_type: `leaf`
- content_type: `concept`
- source_description: When your WebVI is running in the editor environment, you may want to check the values on the wires to determine if and where any unexpected data occurs. To place a probe on a wire, right-click on the wire and select Add Probe. A probe displays the data from the wire it is on. To view a probe in a t

Using Probes to Check Values on a Wire

When your WebVI is running in the editor environment, you may want to check the values on the wires to determine if and where any unexpected data occurs.

To place a probe on a wire, right-click on the wire and select Add Probe. 
 A probe displays the data from the wire it is on. To view a probe in a temporary overlay on the diagram, hover over the probe marker on a wire. 
 If desired, you can then click the Pin button to keep this probe visible. From the Options drop-down you can choose the different display styles and also remove the probe, as required.

[IMAGE alt='1378' src='GUID-73E4A4B9-F004-4F26-8B5B-047C216429E9-a5.png']

You can also find probes in the Debugging tab on the left side of the editor environment. The order in the list correlates with the numbers in the probe markers on the wires.

Probes display the most recent value carried by a wire. You can hover over the probes in the list and observe the tip strip that specifies when the value was last updated.

The values displayed in the probe list are limited to a line of text. However, you can hover over a probe and click the > button to display an expanded view of the probe and the Options drop-down.

Parent topic:

Testing and Debugging

<!--NI_TOPIC bundle=labview-nxg-debug path=single-step.html language=enus -->
## TOPIC 00008: Single-Stepping through VIs

- bundle_id: `labview-nxg-debug`
- source_path: `single-step.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-debug/raw/resource/enus/single-step.html
- document_id: `labview-nxg-debug`
- page_type: `leaf`
- content_type: `concept`
- source_description: While execution highlighting slows the execution of your code, single-stepping allows you to have more control of viewing individual actions of the program. With execution highlighting, execution slows down, and the code executes until completion. With single-stepping, you can execute a single node

Single-Stepping through VIs

While execution highlighting slows the execution of your code, single-stepping allows you to have more control of viewing individual actions of the program.

With execution highlighting, execution slows down, and the code executes until completion. With single-stepping, you can execute a single node at a time, causing the program to pause after the node completes.

You can use single-stepping in three ways: 
 Step In, 
 Step Out, and 
 Step Over. You can find these options in the 
 Debugging tab.

|  | Step In—Display the code and pause execution if a node is a subVI and represents more code. For a node that you cannot open, use this option to highlight the node and pause its execution. For text-based programming nodes, Step-In processes the code row-wise. |
| --- | --- |
|  | Step Out— Complete the execution of the current diagram or subdiagram and pause. |
|  | Step Over—Execute a node without stepping into the node and pause at the next node. |

While single-stepping, you will notice the following behaviors:

- When you single-step through code, nodes are highlighted to indicate they are ready to execute.
- Gray lines appear in a loop or a diagram to indicate that the section of code has finished executing but the program is still running. 
 [IMAGE alt='1378' src='GUID-D6C9DB44-B9BF-4A0A-9BBC-7980C9C46F92-a5.png']

Parent topic:

Testing and Debugging

<!--NI_TOPIC bundle=labview-nxg-debug path=use-vi-hier-doc.html language=enus -->
## TOPIC 00009: Viewing the Hierarchy of VIs in Your Application

- bundle_id: `labview-nxg-debug`
- source_path: `use-vi-hier-doc.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-debug/raw/resource/enus/use-vi-hier-doc.html
- document_id: `labview-nxg-debug`
- page_type: `leaf`
- content_type: `task`
- source_description: Open the Call Hierarchy document to see the hierarchy of VIs and subVIs and understand the calling relationships between them in your application. For example, you can use the Call Hierarchy document to see all of the VIs that call a specific VI and the subVIs that specific VI calls. This can be hel

Viewing the Hierarchy of VIs in Your Application

Open the Call Hierarchy document to see the hierarchy of VIs and subVIs and understand the calling relationships between them in your application.

For example, you can use the Call Hierarchy document to see all of the VIs that call a specific VI and the subVIs that specific VI calls. This can be helpful when you need to debug a part of your application and want to see which subVIs are connected to each other.

1. Click 
 View»Call Hierarchy to open a Call Hierarchy document for your project. 
 org.dita.html5/xsl/topic.xsl 455Note Some callers may be hidden. Toggle the triangle icon below a node to show or hide callers.
2. (Optional) Click 
 Clean up diagram to change the visual arrangement of the hierarchy.
3. (Optional) Select a subVI to highlight its calling connections.
4. (Optional) Double-click a subVI displayed in the Call Hierarchy document to open it.

Parent topic:

Testing and Debugging
