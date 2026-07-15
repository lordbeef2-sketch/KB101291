# NI DOCUMENT BUNDLE: labview-nxg-g-programming-patterns

<!--NI_BUNDLE_CHUNK bundle=labview-nxg-g-programming-patterns start=1 end=16 -->
<!--NI_TOPIC bundle=labview-nxg-g-programming-patterns path=common-state-machine-transitions.html language=enus -->
## TOPIC 00001: Common State Machine Transition Code

- bundle_id: `labview-nxg-g-programming-patterns`
- source_path: `common-state-machine-transitions.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-g-programming-patterns/raw/resource/enus/common-state-machine-transitions.html
- document_id: `labview-nxg-g-programming-patterns`
- page_type: `leaf`
- content_type: `reference`
- source_description: Transition code determines which case to execute in the next While Loop iteration. You can use the transitions detailed below as a starting point for the transition code in your program. One State Transition Value State Transition Example Image Use an Enum constant transition when you always want to

Common State Machine Transition Code

Transition code determines which case to execute in the next While Loop iteration. You can use the transitions detailed below as a starting point for the transition code in your program.

| State Transition | Example Image |
| --- | --- |
| Use an Enum constant transition when you always want to transition to a specific state after the code in the current state executes. For example, the Initialize and Exit states in a state machine often use an Enum constant transition. |  |

| State Transition | Example Image |
| --- | --- |
| Use a Select node and a Boolean value to choose between one of two transition values. |  |

| State Transition | Example Image |
| --- | --- |
| Use a Case Structure transition when you need to handle a variety of situations. Add a case for each transition you need to program and create transition code in each case to adjust the transition value when the case executes. Each case in the Case Structure can include a single transition value or multiple values that the program must choose between. |  |
| Use a transition array when you need to choose between more than two transition values at one time. At run time, an Index Array node selects a transition value from an array constant containing each possible state transition value. |  |
| Use an Event Structure when you need to change states in response to a user action in your program. The Event Structure monitors the program for events and executes a subdiagram of code when a specific event occurs. Each event in the Event Structure can include a single transition value or multiple values that the program must choose between. For example, the Wait for Event state in the simple state machine template uses an Event Structure. Note If you need to perform an action periodically in the Wait for Event state, such as updating a timer, you can include an application timeout event in the Event Structure. |  |

Parent topic:

State Machine Design Pattern

<!--NI_TOPIC bundle=labview-nxg-g-programming-patterns path=design-patterns.html language=enus -->
## TOPIC 00002: Programming Design Patterns

- bundle_id: `labview-nxg-g-programming-patterns`
- source_path: `design-patterns.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-g-programming-patterns/raw/resource/enus/design-patterns.html
- document_id: `labview-nxg-g-programming-patterns`
- page_type: `leaf`
- content_type: `concept`
- source_description: A design pattern is a code structure or practice that solves common programming problems. Here are a few examples of design patterns and the problems they solve. Event-driven programming allows your code to respond to events during execution. The state machine design pattern allows you to execute di

Programming Design Patterns

A design pattern is a code structure or practice that solves common programming
 problems.

Here are a few examples of design patterns and the problems they solve.

- Event-driven programming allows your code to respond to events during
 execution.
- The state machine design pattern allows you to execute different parts of your code
 based on the state of your application.

<!--NI_TOPIC bundle=labview-nxg-g-programming-patterns path=diagram-components-state-machine.html language=enus -->
## TOPIC 00003: Diagram Components of a State Machine

- bundle_id: `labview-nxg-g-programming-patterns`
- source_path: `diagram-components-state-machine.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-g-programming-patterns/raw/resource/enus/diagram-components-state-machine.html
- document_id: `labview-nxg-g-programming-patterns`
- page_type: `leaf`
- content_type: `concept`
- source_description: A state machine has four components on the diagram: a While Loop, a Case Structure, an Enum constant, and a shift register. While Loop—Sets the outer boundary for the state machine code and facilitates state transitions. Case Structure—Contains a subdiagram for each state in the state machine. Shift

Diagram Components of a State Machine

A state machine has four components on the diagram: a While Loop, a Case Structure, an Enum constant, and a shift register.

[IMAGE alt='1378' src='GUID-963C1926-B50A-4314-A03B-BE6F12BDECBA-a5.png']

1. While Loop—Sets the outer boundary for the state machine code and facilitates state transitions.
2. Case Structure—Contains a subdiagram for each state in the state machine.
3. Shift register—Passes data from a completed state to the upcoming state.
4. Enum constant—Contains a list of every state in the state machine. The state machine uses this constant to update the current state transition value as the program executes.

Note

Enum constant

Enum constant

Parent topic:

State Machine Design Pattern

<!--NI_TOPIC bundle=labview-nxg-g-programming-patterns path=event-driven-programming.html language=enus -->
## TOPIC 00004: Event-Driven Programming

- bundle_id: `labview-nxg-g-programming-patterns`
- source_path: `event-driven-programming.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-g-programming-patterns/raw/resource/enus/event-driven-programming.html
- document_id: `labview-nxg-g-programming-patterns`
- page_type: `leaf`
- content_type: `concept`
- source_description: Event-driven programming is a programming pattern in which you create diagram code that executes outside the dataflow structure as a result of an event occurring. Use event-driven programming when you want diagram code to execute in response to an event. An event is anything that happens to the user

Event-Driven Programming

*Event-driven programming* is a programming pattern in which you create diagram code that executes outside the dataflow structure as a result of an event occurring.

Use event-driven programming when you want diagram code to execute in response to an event. An *event* is anything that happens to the user interface during
 run time that provides a notification to other parts of a program.

Events are handled by the Event Structure. An
 Event Loop, which consists of an Event Structure
 within a While Loop waits for events, responds to those events, then
 returns to waiting for the next event. Place the code that handles the event in the
 appropriate event case of the Event Structure.

For example, if you want an event to occur when the user presses a specific key on the panel, you can design an application to include a loop that waits until the key press event occurs, handles the event, and returns to wait for the next event. While the loop waits for the event to occur, other parts of the application can continue to run. How the application handles each event depends on the code written for that specific event. Some sections of the program may execute frequently because the events those sections handle occur frequently, and other sections of the program may not execute at all because the events never occur.

Parent topic:

Programming Design Patterns

<!--NI_TOPIC bundle=labview-nxg-g-programming-patterns path=event-sources.html language=enus -->
## TOPIC 00005: Event Sources

- bundle_id: `labview-nxg-g-programming-patterns`
- source_path: `event-sources.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-g-programming-patterns/raw/resource/enus/event-sources.html
- document_id: `labview-nxg-g-programming-patterns`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can configure the Event Structure to handle events from any supported source. User Interface—mouse clicks, key presses, and so on. Programmatically generated events—events triggered by diagram code, without any user interaction. Each event is associated with a control on the panel of the VI, the

Event Sources

You can configure the Event Structure to handle events from any supported source.

- User Interface—mouse clicks, key presses, and so on.
- Programmatically generated events—events triggered by diagram code, without any user interaction.

Note

Parent topic:

Event-Driven Programming

<!--NI_TOPIC bundle=labview-nxg-g-programming-patterns path=execute-code-based-on-event.html language=enus -->
## TOPIC 00006: Executing Code Based on an Event

- bundle_id: `labview-nxg-g-programming-patterns`
- source_path: `execute-code-based-on-event.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-g-programming-patterns/raw/resource/enus/execute-code-based-on-event.html
- document_id: `labview-nxg-g-programming-patterns`
- page_type: `leaf`
- content_type: `task`
- source_description: To execute code based on an event, you must configure the Event Structure to handle events. Before you configure events for the Event Structure to handle, review the Recommendations for Event-Driven Programming. Complete the following steps to configure an Event Structure case to handle events. (Opt

Executing Code Based on an Event

To execute code based on an event, you must configure the Event Structure to handle events.

Event Structure

Recommendations for Event-Driven Programming

Event Structure

1. (Optional) If you want to configure the Event Structure to handle an external I/O event or a programmatically generated event, you first must dynamically register that event.
  1. Select the Event Structure. On the 
 Item tab, click 
 Use dynamic events to enable the Dynamic Event Terminals.
  2. Place a Register for Events node on the diagram and wire the output to the input of the Dynamic Event Terminal.
  3. Create diagram code for your event source and wire it to the inputs of Register for Events.
2. Click the event selector label at the top of the Event Structure, to view the list of available event sources from which you can choose.
3. Select one or more event sources for which you want to respond. Then select an event type for each event source. 
 The event case you configure appears as a selection option in the event selector label at the top of the Event Structure, and the Event Data Node displays the data common to all events handled in that case.
4. Create the code you want the Event Structure to execute when the event occurs. 
 Place this code inside the Event Structure.
5. (Optional) Use a Timeout event to configure an Event Structure to wait a specified amount of time for an event to occur. 
 If no event occurs before the specified amount of time passes, the Event Structure stops handling events.
6. Add additional event cases as required by your application.
  1. Select the Event Structure and click 
 + on the 
 Item tab to add additional event cases.
  2. Repeat steps 2 through 4 for each event case you want to configure.

Parent topic:

Event-Driven Programming

<!--NI_TOPIC bundle=labview-nxg-g-programming-patterns path=execute-code-based-on-user-event.html language=enus -->
## TOPIC 00007: Executing Code Based on a User Event

- bundle_id: `labview-nxg-g-programming-patterns`
- source_path: `execute-code-based-on-user-event.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-g-programming-patterns/raw/resource/enus/execute-code-based-on-user-event.html
- document_id: `labview-nxg-g-programming-patterns`
- page_type: `leaf`
- content_type: `task`
- source_description: User events are defined on the diagram and triggered by the execution of diagram code. Unlike user interface events, which require direct user interaction with front panel objects, user events allow you to create an application that responds to programmatic changes on objects. Additionally, you can

Executing Code Based on a User Event

Unlike user interface events, which require direct user interaction with front panel objects, user events allow you to create an application that responds to programmatic changes on objects.

Event Structure

#### What to Use

- Create User Event
- Register for Events
- Event Loop
- Generate User Event
- Unregister for Events
- Destroy User Event

#### What to Do

Create the following diagram to build a user event that notifies the Event Structure to handle the event and any associated data.

Customize the gray sections for your unique programming goals.

[IMAGE alt='1378' src='GUID-E57D381F-69AB-4633-86F5-8FA2F454E088-a5.png']

|  | To define a user event, wire a constant of the same data type as the event to Create User Event. The input for Create User Event is an individual element or a cluster whose data type defines the data type for the event. |
| --- | --- |
|  | Create User Event returns a reference to the user event that you create. Use this reference to register for events and generate a user event. To give a unique name to the user event you create, select Create User Event and edit the Event name field on the Item tab. In this diagram, the name of the user event is My User Event. |
|  | Use Register For Events to dynamically register the user event. You must dynamically register the user event so that the Event Structure can handle it when it occurs. |
|  | To display the Dynamic Event Terminal, click the Event Structure and select Use dynamic events on the Item tab. Wire the event registration refnum output of Register For Events to the Dynamic Event Terminal on the left side of the Event Structure. After you select an event, the user event data items appear in the Event Data Node on the left border of the Event Structure. |
|  | Click the event selector label at the top of the Event Structure to select one or more event sources for which you want to respond. Then select an event type for each event source. The name of the user event appears under the Event type drop-down list when you select Dynamic as the event source. |
|  | Use the Event Data Node to access data elements associated with a particular event. To add more data items to the Event Data Node, vertically resize the node. |
|  | Use Generate User Event to broadcast the user event you wire to this node and the associated event data to each Event Structure registered to handle the event. The data value that you wire to this node must match the data type of the user event. Note If the user event is not registered, Generate User Event has no effect. If the user event is registered but no Event Structure is waiting on it, the VI queues the user event and data until an Event Structure executes to handle the event. |
|  | To conserve memory resources, use Unregister For Events and Destroy User Event to release the associated events and the user event reference. |
|  | Create code that executes whenever this user event occurs. |

Parent topic:

Event-Driven Programming

<!--NI_TOPIC bundle=labview-nxg-g-programming-patterns path=general-user-interface-event-reference.html language=enus -->
## TOPIC 00008: General User Interface Event Reference

- bundle_id: `labview-nxg-g-programming-patterns`
- source_path: `general-user-interface-event-reference.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-g-programming-patterns/raw/resource/enus/general-user-interface-event-reference.html
- document_id: `labview-nxg-g-programming-patterns`
- page_type: `leaf`
- content_type: `reference`
- source_description: The following events occur when the user performs an action that involves the panel or any control on the panel. Event Description Event Data Fields Value Changed Generated when the user changes the value of a control. You must read the terminal of a latched Boolean control in its Value Change event

General User Interface Event
 Reference

The following events occur when the user performs an action that involves the panel or any control on the panel.

| Event | Description | Event Data Fields |
| --- | --- | --- |
| Value Changed | Generated when the user changes the value of a control. You must read the terminal of a latched Boolean control in its Value Change event case. | Index—Index of the event source within an individual event diagram. Time—Value of the millisecond timer when the event occurred. Control Reference—Reference to the control on which the event occurred. Old Value—Value of the control before the data change. New Value—Value of the control after the data change. |

Parent topic:

User Interface Events

<!--NI_TOPIC bundle=labview-nxg-g-programming-patterns path=programmatically-generated-events.html language=enus -->
## TOPIC 00009: Programmatically Generated Events

- bundle_id: `labview-nxg-g-programming-patterns`
- source_path: `programmatically-generated-events.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-g-programming-patterns/raw/resource/enus/programmatically-generated-events.html
- document_id: `labview-nxg-g-programming-patterns`
- page_type: `leaf`
- content_type: `concept`
- source_description: Programmatically generated events are events that occur as a result of the execution of diagram code. A user event is a type of programmatically generated event. Unlike user interface events, which require direct user interaction with front panel objects, user events allow you to create an applicati

Programmatically Generated Events

Programmatically generated events are events that occur as a result of the execution of diagram code.

Unlike user interface events, which require direct user interaction with front panel objects, user events allow you to create an application that responds to programmatic changes on objects.

Event Structure

1. Create the event using the Create User Event node.
2. Register for the event using the Register for Events node.
3. Enable the dynamic event terminals on the Event Structure .

Programmatically generated events communicate among different parts of the program that have no dataflow dependency. For example, one part of an application may run a continuous loop to monitor a temperature sensor and generate a user event when the sensor reaches an alarm level. In a different part of the same application, an Event Structure executes to handle both the user event generated when the sensor reaches the alarm level and a user interface event that the Event Structure handles to notify the user of the alarm condition. Handling both user interface events and programmatically generated events in the same Event Structure allows you to implement more advanced architectures, such as queued state machines using events.

Parent topic:

Event-Driven Programming

<!--NI_TOPIC bundle=labview-nxg-g-programming-patterns path=recommendations-for-events.html language=enus -->
## TOPIC 00010: Recommendations for Event-Driven Programming

- bundle_id: `labview-nxg-g-programming-patterns`
- source_path: `recommendations-for-events.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-g-programming-patterns/raw/resource/enus/recommendations-for-events.html
- document_id: `labview-nxg-g-programming-patterns`
- page_type: `leaf`
- content_type: `reference`
- source_description: Because handling events in G Dataflow is different from handling events in other programming languages, follow NI's recommendations for event-driven programming. General Recommendations Recommendation Details Place the Event Structure in a While Loop that terminates when events can no longer occur.

Recommendations for Event-Driven Programming

Because handling events in G Dataflow is different from handling events in other programming languages, follow NI's recommendations for event-driven programming.

Parent topic:

Event-Driven Programming

#### General Recommendations

| Recommendation | Details |
| --- | --- |
| Place the Event Structure in a While Loop that terminates when events can no longer occur. | Using a While Loop ensures that the Event Structure can handle events whenever events occur. Without a While Loop, the Event Structure handles only the first event it receives. If the VI queues events after the Event Structure finishes executing, the Event Structure cannot handle those events. |
| To ensure that every queued event is handled, design the VI to finish running soon after the Event Structure stops executing. | The VI uses an event queue to store events and handle them in the order in which they occur. Because the VI queues events for the entire time that it is running, the VI can queue events after dataflow causes an Event Structure to finish executing. |
| Use caution when placing an Event Structure within a Case Structure. | If a Case Structure prevents an Event Structure from executing to handle events, the Event Structure cannot handle events when they occur. If you have enabled panel event pausing, the user interface of the VI can become unresponsive. For example, if an event case launches an application that requires text entry from the user, the user might begin typing before the application appears on the panel. If panel event pausing is enabled, once the application launches and appears on the panel, it processes the key presses in the order in which they occurred. If panel event pausing is disabled, the key presses might be processed elsewhere on the panel. To enable or disable panel event pausing, use the Pause panel event processing until complete checkbox on the Item tab of the Event Structure. |
| Wire each Event Structure that handles dynamic events to a unique Register for Events node. | Branching the wire from a Register for Events node allows multiple Event Structures to pull events from one queue, resulting in a race condition that may cause unpredictable behavior. |
| When you use multiple Event Structures in the same VI, observe the following guidelines: Place each Event Structure in its own While Loop. Wire your diagram code so that the Event Structures execute simultaneously. Wire your diagram code so that the Event Structures stop handling events simultaneously. | You can use multiple Event Structures in the same VI, especially if you register for events dynamically. For example, you can place two Event Structures within two separate While Loops that are subject to different stop conditions. |
| Use Unregister for Events and Destroy User Event to unregister and destroy user events. | The VI unregisters all events and destroys existing user events automatically when the top-level VI finishes running. However, to conserve memory resources, unregister and destroy user events explicitly, especially in an application that runs for a long period of time. |

#### Notify Events

| Recommendation | Details |
| --- | --- |
| Avoid configuring one Event Structure case to handle multiple notify events of different data types. | A single case in an Event Structure can handle multiple notify events. However, if the events are not the same type, only the event data fields common to all events that the case handles appear on the Event Data Node. |
| Do not use the Panel Close notify event for shutdown code. | Including shutdown code in your VI allows you to stop the VI in a controlled manner and protect data. If you use the Panel Close notify event to execute shutdown code, the VI can abort before the shutdown code executes. |

#### Events and Loops

| Recommendation | Details |
| --- | --- |
| Avoid placing code that takes a long time to execute within the Event Structure because the UI will not be able to respond to additional user input until the operation finishes. | If no Event Structure executes promptly to handle an event and panel event pausing is enabled, the user interface of the VI may become unresponsive. If you have enabled panel event pausing, the user interface of the VI can become unresponsive. For example, if an event case launches an application that requires text entry from the user, the user might begin typing before the application appears on the panel. If panel event pausing is enabled, once the application launches and appears on the panel, it processes the key presses in the order in which they occurred. If panel event pausing is disabled, the key presses might be processed elsewhere on the panel. To enable or disable panel event pausing, use the Pause panel event processing until complete checkbox on the Item tab of the Event Structure. |
| Avoid placing two Event Structures in one loop. | If you place two Event Structures in a single loop, the loop cannot iterate until both Event Structures handle an event. For example, if you place two Event Structures in a single While Loop and configure the first Event Structure to handle a Mouse Down event and configure the second Event Structure to handle a Key Down event, if the user clicks the mouse button twice with no intervening Key Down event, the user interface will not respond to the second until the user presses a key. |

#### Events and Latched Boolean Controls

| Recommendation | Details |
| --- | --- |
| When using events with latched Boolean controls, place the control inside the event case so that the mechanical action of a latched Boolean control behaves correctly. | When you trigger an event on a Boolean control with a latched mechanical action, the Boolean control does not reset to its default value until the diagram reads the Boolean control. For example, if you wire a latched stop Boolean control to the condition terminal of a While Loop, create an event case that handles the latched stop Boolean control in the Event Structure. |
| When you wire a latched Boolean control, place the Boolean control in its Value Change event case. |  |
| Use a Case Structure within the event case to handle undo operations for a latched Boolean control. | When you perform an undo operation on a Boolean control with a latching mechanical action, the Event Structure handles the undo operation as a Value Change event, which might return unexpected results. Use the True case of the Case Structure to specify how you want to handle the Boolean control and the False case to specify how you want to handle the undo operation. |

<!--NI_TOPIC bundle=labview-nxg-g-programming-patterns path=standard-states-when-planning-your-program.html language=enus -->
## TOPIC 00011: Standard States To Consider When Planning Your Program

- bundle_id: `labview-nxg-g-programming-patterns`
- source_path: `standard-states-when-planning-your-program.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-g-programming-patterns/raw/resource/enus/standard-states-when-planning-your-program.html
- document_id: `labview-nxg-g-programming-patterns`
- page_type: `leaf`
- content_type: `concept`
- source_description: When you design a state machine, create a distinct initialize state for the program. You can also add a specific state to handle user input or provide custom error handling, depending on your program needs. States to Include in Every State Machine You Create Specify one entry point and one exit poin

Standard States To Consider When Planning Your Program

When you design a state machine, create a distinct initialize state for the program.
 You can also add a specific state to handle user input or provide custom error handling,
 depending on your program needs.

#### States to Include in Every State
 Machine You Create

Specify one entry point and one exit point for a state machine to control the code
 that executes each time the state machine starts up and shuts down.

Initialize state

Note

A state machine runs continuously until the condition terminal
 on the While Loop receives the stop value determined by the
 user. Directing your state machine toward a single exit rather than accounting for
 multiple exit points allows you to control the shutdown code that executes each time
 the machine stops. Using a single exit state also helps prevent accidental,
 premature, or partial state machine shutdowns.

#### States to Consider Depending on Your Program Needs

If you are designing a program that implements user interface actions or contains specialized error handling, consider including these states in your state machine.

Wait for event state

Error handling state

Parent topic:

State Machine Design Pattern

<!--NI_TOPIC bundle=labview-nxg-g-programming-patterns path=state-diagrams.html language=enus -->
## TOPIC 00012: State Diagrams

- bundle_id: `labview-nxg-g-programming-patterns`
- source_path: `state-diagrams.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-g-programming-patterns/raw/resource/enus/state-diagrams.html
- document_id: `labview-nxg-g-programming-patterns`
- page_type: `leaf`
- content_type: `concept`
- source_description: To keep track of every state and interaction in your program, design a state diagram of your state machine before you start programming. A state diagram is an illustration of all the states in a state machine and how these states interact with each other. Each circle represents a state, and each arr

State Diagrams

To keep track of every state and interaction in your program, design a state diagram of your state machine before you start programming.

A state diagram is an illustration of all the states in a state machine and how these states interact with each other. Each circle represents a state, and each arrow represents a possible state transition. While you create your code, you can follow the diagram flowchart to recall how to structure the state machine and how the states within the machine interact.

The following image shows an example of a basic state diagram for a program that changes the temperature of a room over time.

[IMAGE alt='1378' src='GUID-4ECC3348-E0C0-4C39-BE40-084FD315F69A-a5.png']

The state diagram shows all possible state transitions in the program. You can use the state diagram to understand how the states within the program interact before analyzing the code that defines the interactions.

- Each arrow points toward the endpoint of a state transition. For example, the initialize state can only transition to the adjust temperature state. On the other hand, the program can transition back and forth between the adjust temperature state and wait for event state.
- A circular arrow, seen on the adjust temperature and wait for event states, indicates that the state can transition to itself.
- A blue arrow indicates that a transition occurs because of a user action, and a yellow arrow indicates that a transition occurs because of an error in the program.

Parent topic:

State Machine Design Pattern

<!--NI_TOPIC bundle=labview-nxg-g-programming-patterns path=state-machine-design-pattern.html language=enus -->
## TOPIC 00013: State Machine Design Pattern

- bundle_id: `labview-nxg-g-programming-patterns`
- source_path: `state-machine-design-pattern.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-g-programming-patterns/raw/resource/enus/state-machine-design-pattern.html
- document_id: `labview-nxg-g-programming-patterns`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use the state machine design pattern to implement decision making algorithms where a set of distinguishable states exists. These states, or subdiagrams of code, carry out specific operations within a program. Only one state executes at a time while the machine is active. After all of the cod

State Machine Design Pattern

You can use the state machine design pattern to implement decision making algorithms where a set of distinguishable states exists.

These states, or subdiagrams of code, carry out specific operations within a program. Only one state executes at a time while the machine is active.

After all of the code within a state executes, the state outputs a transition value and initiates a state transition. This transition advances the program from the finished state to the next state indicated by the transition value.

During a state transition, data from the completed state is sent to the upcoming state. Once the state machine executes its final state, data output by the machine becomes available for other parts of the program to use.

Parent topic:

Programming Design Patterns

<!--NI_TOPIC bundle=labview-nxg-g-programming-patterns path=tree-control-event-reference.html language=enus -->
## TOPIC 00014: Tree Control Event Reference

- bundle_id: `labview-nxg-g-programming-patterns`
- source_path: `tree-control-event-reference.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-g-programming-patterns/raw/resource/enus/tree-control-event-reference.html
- document_id: `labview-nxg-g-programming-patterns`
- page_type: `leaf`
- content_type: `reference`
- source_description: The following events occur when the user performs an action that involves a tree control. Event Description Event Data Fields Item closed Occurs when the user closes an item in a tree control. Time—Value of the millisecond timer when the event occurred. Index—Index of the event source within an indi

Tree Control Event Reference

The following events occur when the user performs an action that involves a tree control.

| Event | Description | Event Data Fields |
| --- | --- | --- |
| Item closed | Occurs when the user closes an item in a tree control. | Time—Value of the millisecond timer when the event occurred. Index—Index of the event source within an individual event diagram. Control Reference—Reference to the control on which the event occurred. Location—Hierarchical location of the closed item. Data—Data for the closed item, including the hierarchical location and associated data for the columns. |
| Item opened | Occurs when the user expands an item in a tree control. | Time—Value of the millisecond timer when the event occurred. Index—Index of the event source within an individual event diagram. Control Reference—Reference to the control on which the event occurred. Location—Hierarchical location of the expanded item. Data—Data for the expanded item, including the hierarchical location and associated data for the columns. |
| Selection changed | Occurs when the user selects or deselects one or more items in a tree control. | Time—Value of the millisecond timer when the event occurred. Index—Index of the event source within an individual event diagram. Control Reference—Reference to the control on which the event occurred. OldSelection—Hierarchical location of the previously selected item. This event data field can be a string or an array of strings, depending on the selection mode of the tree control. NewSelection—Hierarchical location of the selected item. This event data field can be a string or an array of strings, depending on the selection mode of the tree control. SelectedData—Data for the selected item, including the hierarchical location and associated data for the columns. This event data field can be a cluster or an array of clusters, depending on the selection mode of the tree control. |

Parent topic:

User Interface Events

<!--NI_TOPIC bundle=labview-nxg-g-programming-patterns path=user-interface-events.html language=enus -->
## TOPIC 00015: User Interface Events

- bundle_id: `labview-nxg-g-programming-patterns`
- source_path: `user-interface-events.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-g-programming-patterns/raw/resource/enus/user-interface-events.html
- document_id: `labview-nxg-g-programming-patterns`
- page_type: `leaf`
- content_type: `concept`
- source_description: User interface events are events that occur when a user performs a particular action on the panel. Each time a user interface event occurs, the diagram executes the code you write for the event. Compared with polling the user interface in a loop for interactions, user interface events reduce the CPU

User Interface Events

User interface events are events that occur when a user performs a particular action on the panel.

Each time a user interface event occurs, the diagram executes the code you
 write for the event. Compared with polling the user interface in a loop for
 interactions, user interface events reduce the CPU requirements of your program,
 simplify the diagram code, and ensure that the diagram can respond to all user actions.

You can select from two categories of user interface events: notify and filter.

| Event Type | Description | Example | Use Case |
| --- | --- | --- | --- |
| Notify | Informs you that a user action occurred. | Configure an Event structure to execute in order to handle a Value Change event when the user changes the value of a control. | Use notify events only if you want to know the user performed a specific action. |
| Filter | Allows you to validate or change the event data before the software performs the default action associated with that event. You can also discard the event to prevent the change. | Configure an Event structure to discard a Key down? event, which prevents a user from clicking the mouse to select or change behavior on the panel. | Use filter events if you want to influence how the software handles certain user actions. |

Note

Filter event names include a question mark to help you distinguish them from notify
 events. The software generates an associated notify event after most filter events if no event case discarded the event. The
 notify event has the same name as the filter event but without the question mark.

Parent topic:

Event-Driven Programming

<!--NI_TOPIC bundle=labview-nxg-g-programming-patterns path=when-to-use-a-state-machine.html language=enus -->
## TOPIC 00016: When to Use a State Machine

- bundle_id: `labview-nxg-g-programming-patterns`
- source_path: `when-to-use-a-state-machine.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-g-programming-patterns/raw/resource/enus/when-to-use-a-state-machine.html
- document_id: `labview-nxg-g-programming-patterns`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can apply the state machine design pattern to a wide variety of programming tasks. The following tasks are examples of situations for which state machines are well suited: Responding to user interface interactions where the user's action determines which state executes. Process testing where eac

When to Use a State Machine

You can apply the state machine design pattern to a wide variety of programming tasks.

The following tasks are examples of situations for which state machines are well suited:

- Responding to user interface interactions where the user's action determines which state executes.
- Process testing where each state carries out a step of the process.
- Breaking down difficult to manage applications into smaller, easily maintainable chunks of code.

However, a state machine is not well suited for every programming situation. If your program needs to run parallel processes, you may want to choose a different design pattern.

Parent topic:

State Machine Design Pattern
