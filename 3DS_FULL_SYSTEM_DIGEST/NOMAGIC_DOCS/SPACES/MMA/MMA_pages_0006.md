# NOMAGIC DOCUMENTATION SPACE: Simulation

<!--NOMAGIC_SPACE key=MMA chunk=6 -->

<!--NOMAGIC_PAGE id=249570356 space=MMA version=1 -->
## PAGE 00705: Signal properties mapping to Behavior parameters

- page_id: `249570356`
- space_key: `MMA`
- source_url: https://docs.nomagic.com/spaces/MMA/pages/249570356/Signal+properties+mapping+to+Behavior+parameters
- version_number: 1
- version_date: `2017-09-29T03:59:32.948+02:00`
- ancestors: Magic Model Analyst / Cameo Simulation Toolkit Documentation > User Guide > State Machine simulation > Adapting models for State Machine simulation
- labels: ['signal-property-mapping', 'mapping-signal-properties-to-behavior-parameters']

### NORMALIZED CONTENT

119117224

119117227

119117225

Once the Activities Entry, Exit, and Do Activity of a State have been specified with a Behavior that has input parameters, a signal, which triggers objects to change the State, can carry values to the input parameters.

In order to send the signal to the target object, an instance of the signal will be created. The signal instance can contain the values of its structural features. These values will be propagated to the parameters of the Behavior specified at the Entry, Exit, and Do Activity when the two following conditions are met

- The number and order of properties of the signal must be the same as the number and order of parameters in the Behavior.
- The type, the order (isOrdered), and the multiplicity of each property of the signal must be the same as the corresponding parameter of the Behavior. If the type of signal properties are Subtype of the parameter type, it is considered a match.

If one of the two conditions is not satisfied, a warning will appear once the model is validated by pre-simulation constraints before the simulation starts.

A send signal Action in an Activity can create a signal instance with the values of its structural features. For example, the signal **MySignal** shown in the following figure. It contains three properties: attrib1, attrib2, and attrib3. They are created with Real, String, and Boolean respectively.

###### [IMAGE alt='' src=''] 
A Signal with three properties.

The following figure shows the order of the three signal attributes

###### [IMAGE alt='' src=''] 
The arguments of MySignal signal.

To create the signal Instance of MySignal that contains the values of attrib1, attrib2 and attrib3, a send signal Action must be created with three argument pins as shown in the following figure. The order and types of the pins must match the order and type of the signal properties, therefore the first pin must be typed by Real, the second by String, and the third by Boolean.

###### [IMAGE alt='' src=''] 
Send signal Actions with three arguments.

Now that the pins of the send signal Action have been created, you can specify the values of the signal Instance through them (see the following figure). The figure shows the value specification Actions that are used to create the values and add them to the pins of the send signal Action.

###### [IMAGE alt='' src=''] 
Creating values for argument and parameters of MySignal.

At this point, the signal Instance created by the send signal Action in the **Send Signal Actions with three arguments** figure, will be sent to the context object of Activity A. The signal Instance contains **12.34**, **Hello** **World**, and **true** as the values of attrib1, attrib2, and attrib3 respectively. You can get more information on State Machine simulation and Activity simulation in sections [CONFLUENCE_PAGE title='State Machine simulation' space=''] and [CONFLUENCE_PAGE title='Activity simulation' space=''] respectively.

###### [IMAGE alt='' src=''] 
Details of the State Machine diagram.

In a State-Machine simulation, the state of an object will change if it receives a send signal instance. Behaviors that are specified at the entry, do Activity, and exit of the State will be invoked in the State transition. The values that come with the signal instance will be delivered to the parameters of the behaviors. For example, prior to receiving a signal, an object is in State1, however, it will move to State2 once it has accepted the signal. The Behaviors to which the values of the signal Instance will be delivered, are the Behaviors specified at Exit of State1, Entry and Do Activity of State2.

In the following figure, the object has accepted the signal Instance, that is MySignal, and it will move from State1 to State2. A performOnEntry activity, which is the entry Activity of State 2 will be simulated. The performOnEntry Activity contains three parameters which are param1, param2, and param3. They are typed by Real, String, and Boolean respectively.

###### [IMAGE alt='' src=''] 
Details of the performOnEntry Activity.

You can see the order of the parameters. The values that come with the signal Instance of MySignal will be delivered to these parameters. In this example, the value of attrib1 will be propagated to param1, the value of attrib2 will be propagated to param2, and the value of attrib3 will be propagated to param3. The values of param1, param2, and param3 are "12.34", "Hello World", and "true" respectively. 
 
[IMAGE alt='' src='']

###### Arguments of the performOnEntry Activity.

119117223

**Related pages**

- [CONFLUENCE_PAGE title='State Machine simulation' space='']
- [CONFLUENCE_PAGE title='Activity simulation' space='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="5dc1e7ef-e486-4fef-85a2-4cfcd8d0987a"><ac:parameter ac:name="id">119117224</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="3abaca81-437d-4028-ab38-14f31f0a70d9"><ac:parameter ac:name="id">119117227</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="0b3f5c44-97a6-4ffe-9df8-8e271eb5b1a4"><ac:parameter ac:name="id">119117225</ac:parameter><ac:rich-text-body><p>Once the Activities Entry, Exit, and Do Activity of a State have been specified with a Behavior that has input parameters, a signal, which triggers objects to change the State, can carry values to the input parameters. </p><p>In order to send the signal to the target object, an instance of the signal will be created. The signal instance can contain the values of its structural features. These values will be propagated to the parameters of the Behavior specified at the Entry, Exit, and Do Activity when the two following conditions are met</p><ul><li>The number and order of properties of the signal must be the same as the number and order of parameters in the Behavior. </li><li>The type, the order (isOrdered), and the multiplicity of each property of the signal must be the same as the corresponding parameter of the Behavior. If the type of signal properties are Subtype of the parameter type, it is considered a match. </li></ul><p>If one of the two conditions is not satisfied, a warning will appear once the model is validated by pre-simulation constraints before the simulation starts. </p><p>A send signal Action in an Activity can create a signal instance with the values of its structural features. For example, the signal <strong>MySignal</strong> shown in the following figure. It contains three properties: attrib1, attrib2, and attrib3. They are created with Real, String, and Boolean respectively. <br class="atl-forced-newline" /><br class="atl-forced-newline" /></p><h6 style="text-align: center;"><ac:image ac:align="center" ac:title="A Signal with Three Properties" ac:alt="A Signal with Three Properties"><ri:attachment ri:filename="Signal with 3 properties.png" /></ac:image><br />A Signal with three properties.</h6><p>The following figure shows the order of the three signal attributes</p><h6 style="text-align: center;"><br class="atl-forced-newline" /><ac:image ac:align="center" ac:title="Arguments of MySignal Signal" ac:alt="Arguments of MySignal Signal"><ri:attachment ri:filename="specification-of-signal.png" /></ac:image><br />The arguments of MySignal signal.</h6><p>To create the signal Instance of MySignal that contains the values of attrib1, attrib2 and attrib3, a send signal Action must be created with three argument pins as shown in the following figure. The order and types of the pins must match the order and type of the signal properties, therefore the first pin must be typed by Real, the second by String, and the third by Boolean. </p><h6 style="text-align: center;"><ac:image ac:align="center" ac:title="Send Signal Actions with Three Arguments" ac:alt="Send Signal Actions with Three Arguments"><ri:attachment ri:filename="Sending Signal Action with Arguments.png" /></ac:image><br />Send signal Actions with three arguments.<br class="atl-forced-newline" /> </h6><p>Now that the pins of the send signal Action have been created, you can specify the values of the signal Instance through them (see the following figure). The figure shows the value specification Actions that are used to create the values and add them to the pins of the send signal Action. <br class="atl-forced-newline" /><br class="atl-forced-newline" /></p><h6 style="text-align: center;"><ac:image ac:align="center" ac:title="Creating Values for Argument and Parameters of MySignal" ac:alt="Creating Values for Argument and Parameters of MySignal"><ri:attachment ri:filename="Creating Values for Arguments and Parameters of MySignal.png" /></ac:image><br />Creating values for argument and parameters of MySignal.</h6><p>At this point, the signal Instance created by the send signal Action in the <strong>Send Signal Actions with three arguments</strong> figure, will be sent to the context object of Activity A. The signal Instance contains <strong>12.34</strong>, <strong>Hello</strong> <strong>World</strong>, and <strong>true</strong> as the values of attrib1, attrib2, and attrib3 respectively. You can get more information on State Machine simulation and Activity simulation in sections <ac:link><ri:page ri:content-title="State Machine simulation" /></ac:link> and <ac:link><ri:page ri:content-title="Activity simulation" /></ac:link> respectively. <br class="atl-forced-newline" /><br class="atl-forced-newline" /></p><h6 style="text-align: center;"><ac:image ac:align="center" ac:title="Details of Untitled1 Statemachine" ac:alt="Details of Untitled1 Statemachine"><ri:attachment ri:filename="Details of State Machine named Entitled1.png" /></ac:image> <br />Details of the State Machine diagram.</h6><p>In a State-Machine simulation, the state of an object will change if it receives a send signal instance. Behaviors that are specified at the entry, do Activity, and exit of the State will be invoked in the State transition. The values that come with the signal instance will be delivered to the parameters of the behaviors. For example, prior to receiving a signal, an object is in State1, however, it will move to State2 once it has accepted the signal. The Behaviors to which the values of the signal Instance will be delivered, are the Behaviors specified at Exit of State1, Entry and Do Activity of State2. </p><p>In the following figure, the object has accepted the signal Instance, that is MySignal, and it will move from State1 to State2. A performOnEntry activity, which is the entry Activity of State 2 will be simulated. The performOnEntry Activity contains three parameters which are param1, param2, and param3. They are typed by Real, String, and Boolean respectively. <br class="atl-forced-newline" /><br class="atl-forced-newline" /></p><h6 style="text-align: center;"><ac:image ac:align="center" ac:title="Details of performOnEntry Activity" ac:alt="Details of performOnEntry Activity"><ri:attachment ri:filename="Details of PerformOnEntry Activity.png" /></ac:image><br />Details of the performOnEntry Activity.</h6><p style="text-align: left;">You can see the order of the parameters. The values that come with the signal Instance of MySignal will be delivered to these parameters. In this example, the value of attrib1 will be propagated to param1, the value of attrib2 will be propagated to param2, and the value of attrib3 will be propagated to param3. The values of param1, param2, and param3 are &quot;12.34&quot;, &quot;Hello World&quot;, and &quot;true&quot; respectively. <br class="atl-forced-newline" /><br class="atl-forced-newline" /><ac:image ac:align="center" ac:title="Arguments of performOnEntry Activity" ac:alt="Arguments of performOnEntry Activity"><ri:attachment ri:filename="specification-of-activity-on-entry.png" /></ac:image></p><h6 style="text-align: center;">Arguments of the performOnEntry Activity.</h6></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="dd50a514-9b64-48ab-b96f-1111729d4aa4"><ac:parameter ac:name="id">119117223</ac:parameter><ac:rich-text-body><p><strong>Related pages</strong></p><ul><li><ac:link><ri:page ri:content-title="State Machine simulation" /></ac:link></li><li><ac:link><ri:page ri:content-title="Activity simulation" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=249569655 space=MMA version=2 -->
## PAGE 00706: Simulation Configuration and UI modeling

- page_id: `249569655`
- space_key: `MMA`
- source_url: https://docs.nomagic.com/spaces/MMA/pages/249569655/Simulation+Configuration+and+UI+modeling
- version_number: 2
- version_date: `2025-08-19T14:56:05.809+02:00`
- ancestors: Magic Model Analyst / Cameo Simulation Toolkit Documentation > User Guide
- labels: ['simulation-configuration', 'ui-modeling', 'modeling-ui', 'user-interface']

### NORMALIZED CONTENT

This chapter discusses the components as follows

- [CONFLUENCE_PAGE title='Project options' space=''] Setting options for a Simulation project, e.g., animation, simulation framework, and Simulation engines.
- [CONFLUENCE_PAGE title='SimulationConfig stereotype' space=''] «SimulationConfig» and the SimulationConfig stereotypes as a model-based execution configuration through the «stereotype» SimulationConfig .
- [CONFLUENCE_PAGE title='Simulation log' space=''] Recording all event occurrences during simulation of a Simulation Configuration.
- [CONFLUENCE_PAGE title='Simulation time and simulation clock' space=''] Enabling Magic Model Analyst / Cameo Simulation Toolkit to obtain the amount of time spent on simulating a model from a simulation clock.
- [CONFLUENCE_PAGE title='Automatic start of active objects' space=''] An active object whose Classifier is an active Class.
- [CONFLUENCE_PAGE title='UI modeling diagram simulation' space=''] UI components supporting the UI modeling diagram simulation.
- [CONFLUENCE_PAGE title='ImageSwitcher and ActiveImage' space=''] ImageSwitcher as a powerful animation tool and «ActiveImage» attributes.
- [CONFLUENCE_PAGE title='Time Series Chart' space=''] Displaying plots of runtime values with respect to simulation time and its properties.
- [CONFLUENCE_PAGE title='Timeline chart' space=''] Allowing you to see the active States of an object or a property during simulation or the Activities simulated in an object.
- [CONFLUENCE_PAGE title='Histogram' space=''] Displaying the density of the underlying distribution of data and estimating the probability density function of underlying variables.
- [CONFLUENCE_PAGE title='Nested UI Configuration stereotype' space=''] Creating complex UI mockup consisting of multiple UI Configs.
- [CONFLUENCE_PAGE title='Reusable UI Mockup' space=''] Improving the flexibility in user interface modeling from typing the property using the UI component.
- [CONFLUENCE_PAGE title='CSV export' space=''] Exporting simulation results to a CSV file.
- [CONFLUENCE_PAGE title='Nested property selection for configurations' space=''] Supporting nested property selection for configurations, e.g., Time series charts, Timelines, Sequence diagram generator, and CSV export.
- [CONFLUENCE_PAGE title='Attached files supported' space=''] Accessing files as «AttachedFile» by using only file names without paths in case of references to files by names.
- [CONFLUENCE_PAGE title='HTML UI' space=''] Exporting, opening, and using HTML UI mockups and control model simulations within an embedded browser.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>This chapter discusses the components as follows</p><p><br /></p><ul><li data-uuid="e9d65e41-61d2-40be-9372-d98e49ee9e34"><ac:link><ri:page ri:content-title="Project options" /></ac:link><br />Setting options for a Simulation project, e.g., animation, simulation framework, and Simulation engines.<br /><br /></li><li data-uuid="95f51d8c-07dc-42a2-8f25-20feab8cb6ee"><ac:link><ri:page ri:content-title="SimulationConfig stereotype" /></ac:link><br />«SimulationConfig» and the SimulationConfig stereotypes as a model-based execution configuration through the <em>«stereotype» SimulationConfig</em>.<br /><br /></li><li data-uuid="f06cf5d9-442f-45c4-b1f3-8318fad66ce7"><ac:link><ri:page ri:content-title="Simulation log" /></ac:link><br />Recording all event occurrences during simulation of a Simulation Configuration.<br /><br /></li><li data-uuid="eb3f0c8c-ee46-46c3-a399-b018e63523c6"><ac:link><ri:page ri:content-title="Simulation time and simulation clock" /></ac:link><br />Enabling Magic Model Analyst / Cameo Simulation Toolkit to obtain the amount of time spent on simulating a model from a simulation clock.<br /><br /></li><li data-uuid="7358c70a-4834-4a90-b410-56b8e7383de2"><ac:link><ri:page ri:content-title="Automatic start of active objects" /></ac:link><br />An active object whose Classifier is an active Class.<br /><br /></li><li data-uuid="bcdbc607-df27-4ae1-819b-29f439d32dfb"><ac:link><ri:page ri:content-title="UI modeling diagram simulation" /></ac:link><br />UI components supporting the UI modeling diagram simulation.<br /><br /></li><li data-uuid="42cac9d3-85c7-43cc-9244-58f63ffa9c8c"><ac:link><ri:page ri:content-title="ImageSwitcher and ActiveImage" /></ac:link><br />ImageSwitcher as a powerful animation tool and «ActiveImage» attributes.<br /><br /></li><li data-uuid="c159d5e7-4e36-4ad8-ab2a-2d2301717822"><ac:link><ri:page ri:content-title="Time Series Chart" /></ac:link><br /><span style="color:var(--ds-text,#333333);">Displaying plots of runtime values with respect to simulation time and its properties.</span><br /><br /></li><li data-uuid="a4d7193d-425a-4fcd-b903-e99f18689a24"><ac:link><ri:page ri:content-title="Timeline chart" /></ac:link><br />Allowing you to see the active States of an object or a property during simulation or the Activities simulated in an object.<br /><br /></li><li data-uuid="a5c9695b-0e79-42e1-b8df-65f0c35eb1ac"><ac:link><ri:page ri:content-title="Histogram" /></ac:link><br />Displaying the density of the underlying distribution of data and estimating the probability density function of underlying variables.<br /><br /></li><li data-uuid="540cee23-e40b-4a4b-8f49-3059645b323d"><ac:link><ri:page ri:content-title="Nested UI Configuration stereotype" /></ac:link><br />Creating complex UI mockup consisting of multiple UI Configs.<br /><br /></li><li data-uuid="b000f708-717a-4e50-90f4-544dab257995"><ac:link><ri:page ri:content-title="Reusable UI Mockup" /></ac:link><br />Improving the flexibility in user interface modeling from typing the property using the UI component.<br /><br /></li><li data-uuid="87bb4f68-3ca3-4f0e-bb60-729e9d35c181"><ac:link><ri:page ri:content-title="CSV export" /></ac:link><br />Exporting simulation results to a CSV file.<br /><br /></li><li data-uuid="f1cb4f36-ebd7-47b2-bdb0-20c1cc6fa6bc"><ac:link><ri:page ri:content-title="Nested property selection for configurations" /></ac:link><br /><span style="color:var(--ds-text,#333333);">Supporting nested property selection for configurations, e.g., Time series charts, Timelines<span style="color:var(--ds-text,#333333);">, Sequence diagram generator, and CSV export.<br /><br /></span></span></li><li data-uuid="6caaa55e-c20f-4240-bdc3-13b0006cc6a0"><ac:link><ri:page ri:content-title="Attached files supported" /></ac:link> <br />Accessing files as «AttachedFile» by using only file names without paths in case of references to files by names.<br /><br /></li><li data-uuid="943c854f-7233-4505-9911-a3bc9f9dbf87"><ac:link><ri:page ri:content-title="HTML UI" /></ac:link><br /><span style="color:var(--ds-text,#172b4d);">Exporting, opening, and using HTML UI mockups and control model simulations within an embedded browser.</span></li></ul>
````

<!--NOMAGIC_PAGE id=249570152 space=MMA version=1 -->
## PAGE 00707: Simulation console

- page_id: `249570152`
- space_key: `MMA`
- source_url: https://docs.nomagic.com/spaces/MMA/pages/249570152/Simulation+console
- version_number: 1
- version_date: `2018-02-22T05:12:47.931+01:00`
- ancestors: Magic Model Analyst / Cameo Simulation Toolkit Documentation > User Guide > Simulation debugging
- labels: ['simulation-pane']

### NORMALIZED CONTENT

30385878

30385880

30385879

This chapter explains the fundamental concept and functions of buttons in the Simulation **Console** pane and its displayed levels of information, log files as records of all simulation details displayed in the **Console** pane during simulation, log's filter options, and constraint failures shown in the **Console** pane.

30385877

**Related pages**

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="02e9b27e-b4ad-4575-bbe9-22c60bfe6275"><ac:parameter ac:name="id">30385878</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="87e4dce7-4726-4373-8d7c-75c679d50fd9"><ac:parameter ac:name="id">30385880</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="b4109919-f056-4455-851c-2b6d9ac1bfcf"><ac:parameter ac:name="id">30385879</ac:parameter><ac:rich-text-body><p>This chapter explains the fundamental concept and functions of buttons in the Simulation <strong>Console</strong> pane and its displayed levels of information, log files as records of all simulation details displayed in the <strong>Console</strong> pane during simulation, log's filter options, and constraint failures shown in the <strong>Console</strong> pane.</p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="e9f19056-23a4-4561-9075-9d9f88bfdafe"><ac:parameter ac:name="id">30385877</ac:parameter><ac:rich-text-body><p><strong>Related pages</strong></p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="04b42275-4836-4495-b115-0eb9a2feaac6" /></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=249570138 space=MMA version=1 -->
## PAGE 00708: Simulation debugging

- page_id: `249570138`
- space_key: `MMA`
- source_url: https://docs.nomagic.com/spaces/MMA/pages/249570138/Simulation+debugging
- version_number: 1
- version_date: `2018-03-05T14:33:07.812+01:00`
- ancestors: Magic Model Analyst / Cameo Simulation Toolkit Documentation > User Guide
- labels: ['simulation-debugging', 'debugging']

### NORMALIZED CONTENT

28891594

28891596

28891595

This section presents an overview of simulation sessions, debugging process, components of simulation console and log files, monitoring runtime values, updating default values from an Instance Specification, adding and removing breakpoints, and the settings for automatic updates during simulation sessions in the **Simulation** pane.

28891593

**Related pages**

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="cbf34e50-41b9-4263-a5f7-d4849055490b"><ac:parameter ac:name="id">28891594</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="511039be-3944-4e42-bfd9-59efc724d4a3"><ac:parameter ac:name="id">28891596</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="a5a85f22-6924-46ec-924f-b7ed2a7145ba"><ac:parameter ac:name="id">28891595</ac:parameter><ac:rich-text-body><p>This section presents an overview of simulation sessions, debugging process, components of simulation console and log files, monitoring runtime values, updating default values from an Instance Specification, adding and removing breakpoints, and the settings for automatic updates during simulation sessions in the <strong>Simulation</strong> pane.</p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="e917dac8-9754-4c67-b1c7-7800b3169aef"><ac:parameter ac:name="id">28891593</ac:parameter><ac:rich-text-body><p><strong>Related pages</strong></p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="d9ee3349-7c91-47e1-9861-598a23eb6d40" /></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=249571207 space=MMA version=5 -->
## PAGE 00709: Simulation in Cameo Collaborator for Teamwork Cloud

- page_id: `249571207`
- space_key: `MMA`
- source_url: https://docs.nomagic.com/spaces/MMA/pages/249571207/Simulation+in+Cameo+Collaborator+for+Teamwork+Cloud
- version_number: 5
- version_date: `2025-12-03T09:48:50.171+01:00`
- ancestors: Magic Model Analyst / Cameo Simulation Toolkit Documentation > User Guide > Server-side simulation
- labels: []

### NORMALIZED CONTENT

[CONFLUENCE_PAGE title='Cameo Collaborator for Teamwork Cloud' space='MCS'] has a user interface that allows you to simulate a project directly in the Cameo Collaborator document published from that project.

##### Preparing projects for simulation in Cameo Collaborator for Teamwork Cloud

To simulate a project in Cameo Collaborator for Teamwork Cloud, prepare it as described below.

To prepare a project for simulation in Cameo Collaborator for Teamwork Cloud

1. In a modeling tool, open the project that you want to simulate.
2. Create a Simulation Configuration and specify its properties if you haven't already done so. In Cameo Collaborator for Teamwork Cloud, you can only simulate the projects that have a Simulation Configuration.
3. Make sure you specify the Execution Target property of the Simulation Configuration.
4. If you want the simulation results to be saved and displayed in a Cameo Collaborator document after every simulation, specify the**Result Location** property of the Simulation Configuration. The value of the**Result Location** property should be the Instance Specification in which you want to save simulation results. [IMAGE alt='' src='']
5. Commit project changes to the server or save and add the project to Teamwork Cloud (if the project is local).
6. [CONFLUENCE_PAGE title='Publishing from graphical user interface' space='MCS'] .

Now you can open the Cameo Collaborator document and simulate the model on the web.

##### Simulating projects in Cameo Collaborator for Teamwork Cloud

Once you publish your project to Cameo Collaborator for Teamwork Cloud, you can simulate it in a Cameo Collaborator document, as described below.

To simulate a project in Cameo Collaborator for Teamwork Cloud

1. [CONFLUENCE_PAGE title='Opening Cameo Collaborator for Teamwork Cloud' space='MCS'] published from the project you want to simulate.
2. Click [IMAGE alt='' src=''] on the bottom right corner of the screen.
3. Navigate to the element you want to execute (the execution target of a Simulation Configuration) and select it.
4. When the Select configuration and run pane opens on the right side of the screen, select the Simulation Configuration you want to run.
5. Click [IMAGE alt='' src=''] on the top right corner of the pane. [IMAGE alt='' src=''] Requirement or Constraint verification in an Instance TableIn the example above, the execution target is an Instance Specification in an Instance table. As you can see, the Instance Table cells are highlighted in green or red according to Requirement or Constraint verification results. To see the tooltip with Requirement or Constraint text, hover the mouse pointer over a highlighted cell.
6. Wait for the notifications informing you about the simulation's place in the queue and its status. You can use these notifications to do one of the following:
  - When the simulation is complete, click Refresh to refresh the page and see the simulation results.
  - When the simulation is complete, click Navigate to go to the document section where the simulation was initiated and see the simulation results.
  - When the simulation with UI is started, click Open to open the UI window.

After simulating a project in Cameo Collaborator for Teamwork Cloud, a new project version is created with the following commit message: Simulation WebApp: '<Simulation Config Name>' execution results.If the simulation runs longer than 1 min, the right-side panel is closed, and you can work with the document as usual while the simulation continues to run in the background. When the simulation is completed, you get a notification with the link to the document location where the simulated instance was selected.

##### Displaying charts with the simulation results

Server-side simulation supports Timeline and Time Series Charts, which areupdated in real-time during simulation. When displayed in a Cameo Collaborator document, Timeline and Time Series Charts are automatically updated with the latest simulation results every time you simulate the model.

To display a Timeline or Time Series Chart in a Cameo Collaborator document

1. In a modeling tool, open the project that you want to simulate.
2. Open the Specification window of the Simulation Configuration you want to run.
3. Set the value of the Result Location property to the Instance Specification in which you want to save simulation results.
4. Set the value of the UI property to the Timeline or Time Series Chart you want to display in a Cameo Collaborator document.
5. Open the Specification window of the Timeline or Time Series Chart you specified as the value of the UI property in the previous step.
6. Set the value of the Record Plot Data As property to HTML .
7. Commit project changes to the server or save and add the project to Teamwork Cloud (if the project is local).
8. [CONFLUENCE_PAGE title='Publishing from graphical user interface' space='MCS']
9. .

Once the simulation is finished, a Timeline or Time Series Chart will be displayed in the HTML format as the **Documentation** property of the Instance Specification set as the location result (see step 3).

[IMAGE alt='' src='']

###### A Timeline Chart displayed in a Cameo Collaborator document.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><ac:link><ri:page ri:space-key="MCS" ri:content-title="Cameo Collaborator for Teamwork Cloud" /></ac:link> has a user interface that allows you to simulate a project directly in the Cameo Collaborator document published from that project.</p><h3>Preparing projects for simulation in Cameo Collaborator for Teamwork Cloud</h3><p>To simulate a project in Cameo Collaborator for Teamwork Cloud, prepare it as described below.</p><p><br /></p><p>To prepare a project for simulation in Cameo Collaborator for Teamwork Cloud</p><hr /><ol><li data-uuid="018dab3c-77ee-4567-8d49-89283e3d0f88">In a modeling tool, open the project that you want to simulate.</li><li data-uuid="33e49a77-12cf-48ce-9ae3-597b0406513c"><p>Create a Simulation Configuration and specify its properties if you haven't already done so.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="868e1f60-b49f-4772-9d46-cb73abab9b8d"><ac:rich-text-body><p>In Cameo Collaborator for Teamwork Cloud, you can only simulate the projects that have a Simulation Configuration.</p></ac:rich-text-body></ac:structured-macro></li><li data-uuid="1a8288c2-c55c-403f-a3d6-51f615299f40">Make sure you specify the <strong>Execution Target</strong> property of the Simulation Configuration.</li><li data-uuid="d87af0bc-5320-4127-861d-437968c4d21a"><p><span style="color:var(--ds-text,#333333);">If you want the simulation results to be saved and displayed in a Cameo Collaborator document after every simulation, specify the </span><strong>Result Location</strong> property of the Simulation Configuration.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="02cad1fd-887b-4848-ba6e-814cfb4fd3d2"><ac:rich-text-body>The value of the<span style="color:var(--ds-text,#333333);"> </span><strong>Result Location</strong> property should be the Instance Specification in which you want to save simulation results.</ac:rich-text-body></ac:structured-macro><p><br /><ac:image><ri:attachment ri:filename="result_location.png" /></ac:image> <br /><br /></p></li><li data-uuid="0369a1d3-e766-4e8a-8d70-425508e7d985">Commit project changes to the server or save and <a href="https://docs.nomagic.com/CM/?contextKey=adding-projects-to-teamwork-cloud&amp;version=latest">add the project to Teamwork Cloud</a> (if the project is local).</li><li data-uuid="8ecab479-57ad-4b4d-8bab-2102fcd9eb89"><ac:link><ri:page ri:space-key="MCS" ri:content-title="Publishing from graphical user interface" /><ac:plain-text-link-body><![CDATA[Publish the project to Cameo Collaborator for Teamwork Cloud]]></ac:plain-text-link-body></ac:link>.</li></ol><p><br />Now you can open the Cameo Collaborator document and simulate the model on the web.</p><h3><br />Simulating projects in Cameo Collaborator for Teamwork Cloud</h3><p>Once you publish your project to Cameo Collaborator for Teamwork Cloud, you can simulate it in a Cameo Collaborator document, as described below.</p><p><br /></p><p>To simulate a project in Cameo Collaborator for Teamwork Cloud</p><hr /><ol><li data-uuid="9b9292c4-ce11-41ab-8f58-cb22ab4798d6"><ac:link><ri:page ri:space-key="MCS" ri:content-title="Opening Cameo Collaborator for Teamwork Cloud" /><ac:plain-text-link-body><![CDATA[Open the Cameo Collaborator document]]></ac:plain-text-link-body></ac:link> published from the project you want to simulate.</li><li data-uuid="cc4ff849-4339-4cbe-9649-4782c990b45d"><p class="auto-cursor-target">Click <ac:image ac:thumbnail="true" ac:width="25"><ri:attachment ri:filename="run_icon.png" /></ac:image> on the bottom right corner of the screen.</p></li><li data-uuid="6606810a-933d-4d99-a1c3-ef3e6a28b2be">Navigate to the element you want to execute (the execution target of a Simulation Configuration) and select it.</li><li data-uuid="2dcfa8b4-fd32-4186-8f1f-19c433ba7289">When the <strong>Select configuration and run</strong> pane opens on the right side of the screen, select the Simulation Configuration you want to run.</li><li data-uuid="f2f8f0a2-f46f-4c53-b3fb-52aff2cf587a"><p class="auto-cursor-target">Click <ac:image ac:thumbnail="true" ac:width="25"><ri:attachment ri:filename="run_icon.png" /></ac:image> on the top right corner of the pane.<br /><br /></p><p><ac:image><ri:attachment ri:filename="running_simulation.png" /></ac:image><br /><br /></p><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="4d579d80-745a-4e4b-9c8c-1a4eba92adb5"><ac:parameter ac:name="title">Requirement or Constraint verification in an Instance Table</ac:parameter><ac:rich-text-body><p><span style="color:var(--ds-text,#333333);">In the example above, the execution target is an Instance Specification in an Instance table. As you can see, the Instance Table cells are highlighted in green or red according to Requirement or Constraint verification results. To see the tooltip with Requirement or Constraint text, hover the mouse pointer over a highlighted cell.</span></p></ac:rich-text-body></ac:structured-macro></li><li data-uuid="defa9229-1d30-4137-a842-6e657fb16b71"><p class="auto-cursor-target"><span style="color:var(--ds-text,#333333);">Wait for the notifications informing you about the simulation's place in the queue and its status. Y</span>ou can use these notifications to do one of the following:</p><ul><li>When the simulation is complete, click <strong>Refresh</strong> to refresh the page and see the simulation results.</li><li>When the simulation is complete, click <strong>Navigate</strong> to go to the document section where the simulation was initiated and see the simulation results.</li><li>When the simulation with UI is started, click <strong>Open</strong> to open the UI window.</li></ul><p><br /></p></li></ol><p><span style="color:var(--ds-text,#333333);">After simulating a project in Cameo Collaborator for Teamwork Cloud, a new project version is created with the following commit message: Simulation WebApp: '&lt;S</span><span class="error" style="color:var(--ds-text,#333333);">imulation Config Name&gt;</span><span style="color:var(--ds-text,#333333);">' execution results. </span>If the simulation runs longer than 1 min, the right-side panel is closed, and you can work with the document as usual while the simulation continues to run in the background. When the simulation is completed, you get a notification with the link to the document location where the simulated instance was selected.</p><h3><br />Displaying charts with the simulation results</h3><p>Server-side simulation supports Timeline and Time Series Charts, <span style="color:var(--ds-text,#333333);">which are<span> </span></span><span style="color:var(--ds-text,#172b4d);">updated in real-time during simulation. When displayed</span> in a Cameo Collaborator document, Timeline and Time Series Charts are automatically updated with the latest simulation results every time you simulate the model.</p><p><br /></p><p>To display a Timeline or Time Series Chart in a Cameo Collaborator document</p><hr /><ol><li data-uuid="a74cc2a0-1139-4ba4-b65e-399caa323ab5">In a modeling tool, open the project that you want to simulate.</li><li data-uuid="00fed3e0-3429-4919-99bc-aa523d476697">Open the Specification window of the Simulation Configuration you want to run.</li><li data-uuid="2ec31d2b-b126-426a-86af-ee4f614777ad">Set the value of the <strong>Result Location</strong> property to the Instance Specification in which you want to save simulation results.</li><li data-uuid="3a6eed80-cea7-4252-8f39-877bb4181609">Set the value of the <strong>UI</strong> property to the Timeline or Time Series Chart you want to display in a Cameo Collaborator document.</li><li data-uuid="b70f6b1b-d798-44b6-bfef-949b5bbeb1e3">Open the Specification window of the Timeline or Time Series Chart you specified as the value of the <strong>UI</strong> property in the previous step.</li><li data-uuid="722fda98-dcf7-4c4d-b2c3-876c84d2528c">Set the value of the <strong>Record Plot Data As</strong> property to <strong>HTML</strong>.</li><li data-uuid="2b6f819c-e9db-4533-be17-5a76777768a5">Commit project changes to the server or save and <a href="https://docs.nomagic.com/CM/?contextKey=adding-projects-to-teamwork-cloud&amp;version=latest">add the project to Teamwork Cloud</a> (if the project is local).</li><li data-uuid="40697965-a335-45de-bc25-230db282ff8a"><ac:link><ri:page ri:space-key="MCS" ri:content-title="Publishing from graphical user interface" /><ac:plain-text-link-body><![CDATA[Publish the project to Cameo Collaborator for Teamwork Cloud.]]></ac:plain-text-link-body></ac:link></li><li data-uuid="f919a402-8ce1-4fc1-a675-7d6f1aafbe0f"><ac:link ac:anchor="Simulating projects in Cameo Collaborator for Teamwork Cloud"><ac:plain-text-link-body><![CDATA[Simulate the project in Cameo Collaborator for Teamwork Cloud]]></ac:plain-text-link-body></ac:link>.</li></ol><p><br /><span style="color:var(--ds-text,#333333);">Once the simulation is finished, a Timeline or Time Series Chart will be displayed in the HTML format as the <strong>Documentation</strong> property of the Instance Specification set as the location result (see step 3).</span></p><p><br /></p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="live_timeline_chart_in_CC_document.png" /></ac:image></p><h6 style="text-align: center;">A Timeline Chart displayed in a Cameo Collaborator document.</h6>
````

<!--NOMAGIC_PAGE id=249571199 space=MMA version=3 -->
## PAGE 00710: Simulation in the Resources application

- page_id: `249571199`
- space_key: `MMA`
- source_url: https://docs.nomagic.com/spaces/MMA/pages/249571199/Simulation+in+the+Resources+application
- version_number: 3
- version_date: `2025-12-03T09:48:28.676+01:00`
- ancestors: Magic Model Analyst / Cameo Simulation Toolkit Documentation > User Guide > Server-side simulation
- labels: []

### NORMALIZED CONTENT

You can simulate server projects with specified UI in the Resources application of Teamwork Cloud.

To simulate a project in the Resources application

1. Open the [CONFLUENCE_PAGE title='Resources application' space='MCS'] and navigate to the project you want to simulate.
2. Click [IMAGE alt='' src=''] on the right side of the project line and select **Run simulation**. You can only run a project with a UI mockup, Time Series Chart, or Timeline Chart. If the project has no specified UI, the **Run simulation** menu item is not available. For more information on how to prepare projects with UI for simulation, refer to [CONFLUENCE_PAGE title='Simulation with UI' space='']. [IMAGE alt='' src='']
3. On the right-side pane select the Simulation Configuration you want to run and click [IMAGE alt='' src='']. [IMAGE alt='' src=''] If the name of a Simulation Configuration is greyed out and you cannot select it, it means that the project has a UI but it is not generated and attached to the project. In this case, [CONFLUENCE_PAGE title='Simulation with UI' space=''].[IMAGE alt='' src='']
4. Wait for the notifications informing you about the simulation's place in the queue and its status. You can use these notifications to do one of the following:
  - When the simulation is complete, click Refresh to refresh the page and see the simulation results.
  - When the simulation is complete, click Navigate to go to the document section where the simulation was initiated and see the simulation results.
  - When the simulation with UI is started, click Open to open the UI window.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>You can simulate server projects with <span style="color:var(--ds-text,#333333);">specified UI in the Resources application of Teamwork Cloud.</span></p><p><br /></p><p><span style="color:var(--ds-text,#333333);">To simulate a project in the Resources application</span></p><hr /><ol><li data-uuid="0f218ccf-a406-4569-b6b7-1c30920824af">Open the <ac:link><ri:page ri:space-key="MCS" ri:content-title="Resources application" /></ac:link> and navigate to the project you want to simulate.</li><li data-uuid="b0770531-2e18-493a-8405-c97b13ec1956"><p class="auto-cursor-target">Click <ac:image ac:thumbnail="true" ac:height="18"><ri:attachment ri:filename="menu.png" /></ac:image> on the right side of the project line and select <strong>Run simulation</strong>.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="3a48640d-fae6-4c78-9975-b3dec51d2c3e"><ac:rich-text-body><p>You can only run a project with a <span style="color:var(--ds-text,#333333);">UI mockup, Time Series Chart, or Timeline Chart. If the project has no specified UI, the <strong>Run simulation</strong> menu item is not available. For more information on how to prepare projects with UI for simulation, refer to <ac:link><ri:page ri:content-title="Simulation with UI" /></ac:link>.</span></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><ac:image><ri:attachment ri:filename="simulation_from_resources_app.png" /></ac:image></p><p class="auto-cursor-target"><br /></p></li><li data-uuid="b7e3958d-588c-468f-a42b-8c20c5e5044a"><p class="auto-cursor-target">On the right-side pane select the Simulation Configuration you want to run and click <ac:image ac:thumbnail="true" ac:width="25"><ri:attachment ri:filename="run.png" /></ac:image>.<br /><br /></p><p class="auto-cursor-target"><ac:image><ri:attachment ri:filename="selecting_simConfig.png" /></ac:image><br /><br /></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="2a5d86e6-f074-4c40-b454-c8407000557e"><ac:rich-text-body><p>If the name of a Simulation Configuration is greyed out and you cannot select it, it means that the project has a UI but it is not generated and attached to the project. In this case, <ac:link><ri:page ri:content-title="Simulation with UI" /><ac:plain-text-link-body><![CDATA[generate and attach HTML to the Teamwork Cloud project]]></ac:plain-text-link-body></ac:link>.</p><p><ac:image ac:align="center"><ri:attachment ri:filename="ui_not_attached.png" /></ac:image></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></li><li data-uuid="b886cf72-fdb5-42ac-a181-149d9a03f792"><p class="auto-cursor-target"><span style="color:var(--ds-text,#333333);">Wait for the notifications informing you about the simulation's place in the queue and its status. Y</span>ou can use these notifications to do one of the following:</p><ul><li>When the simulation is complete, click <strong>Refresh</strong> to refresh the page and see the simulation results.</li><li>When the simulation is complete, click <strong>Navigate</strong> to go to the document section where the simulation was initiated and see the simulation results.</li><li>When the simulation with UI is started, click <strong>Open</strong> to open the UI window.</li></ul></li></ol>
````

<!--NOMAGIC_PAGE id=249570164 space=MMA version=1 -->
## PAGE 00711: Simulation information

- page_id: `249570164`
- space_key: `MMA`
- source_url: https://docs.nomagic.com/spaces/MMA/pages/249570164/Simulation+information
- version_number: 1
- version_date: `2021-10-11T10:46:46.151+02:00`
- ancestors: Magic Model Analyst / Cameo Simulation Toolkit Documentation > User Guide > Simulation debugging > Simulation console
- labels: ['simulation-information-in-console']

### NORMALIZED CONTENT

32929692

32929695

32929693

The **Console** pane can display four levels of information (sorted in ascending order by priority) as follows

| Option | Description |
| --- | --- |
| DEBUG | Displays debugging information. |
| INFO | Displays normal information. |
| WARN | Displays warnings. |
| ERROR | Displays errors. |

By default, only information with a priority equivalent to INFO or higher (WARN and ERROR) will be displayed in the **Console** pane. You can customize the way information is displayed by editing the *simulation.properties* file in the **data** directory in the MagicDraw installation directory. You can use a text editor to edit this file.

To change the priority level, e.g., open *log4j.category.SIM_CONSOLE*.

| log4j.category.SIM_CONSOLE=INFO,SimConsoleApp,SimXMLApp |
| --- |

Change the first parameter's priority level from **INFO** (default value) to **DEBUG** to display all levels of simulation information in the **Console** tab.

| log4j.category.SIM_CONSOLE=DEBUG,SimConsoleApp,SimXMLApp |
| --- |

You can see more information about customizing the information displayed in the **Console** pane from the comment in the *simulation.properties* file.

32929691

**Related page**

- [CONFLUENCE_PAGE title='Console pane' space='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="115253fb-c1f7-4452-9331-51bef64bfbf3"><ac:parameter ac:name="id">32929692</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="8f9449e1-4bcd-4bb3-a57c-054f2fe8cdf4"><ac:parameter ac:name="id">32929695</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="80164846-36e2-4d66-86df-40e7526f85f7"><ac:parameter ac:name="id">32929693</ac:parameter><ac:rich-text-body><p>The <strong>Console</strong> pane can display four levels of information (sorted in ascending order by priority) as follows</p><p class="auto-cursor-target"><br /></p><table class="wrapped relative-table" style="width: 33.2436%;"><colgroup><col style="width: 26.741%;" /><col style="width: 73.2691%;" /></colgroup><tbody><tr><th colspan="1">Option</th><th colspan="1">Description</th></tr><tr><td><strong>DEBUG</strong> </td><td>Displays debugging information.</td></tr><tr><td><strong>INFO</strong> </td><td>Displays normal information.</td></tr><tr><td><strong>WARN</strong> </td><td>Displays warnings.</td></tr><tr><td><strong>ERROR</strong> </td><td>Displays errors.</td></tr></tbody></table><p class="auto-cursor-target"><br /></p><p>By default, only information with a priority equivalent to INFO or higher (WARN and ERROR) will be displayed in the <strong>Console</strong> pane. You can customize the way information is displayed by editing the <em>simulation.properties</em> file in the <strong>data</strong> directory in the MagicDraw installation directory. You can use a text editor to edit this file. </p><p>To change the priority level, e.g., open <em>log4j.category.SIM_CONSOLE</em>. </p><table class="wrapped"><colgroup><col /></colgroup><tbody><tr><td>log4j.category.SIM_CONSOLE=<strong>INFO</strong>,SimConsoleApp,SimXMLApp</td></tr></tbody></table><p>Change the first parameter's priority level from <strong style="line-height: 1.42857;">INFO</strong> (default value) to <strong style="line-height: 1.42857;">DEBUG</strong> to display all levels of simulation information in the <strong style="line-height: 1.42857;">Console</strong> tab. </p><table class="wrapped"><colgroup><col /></colgroup><tbody><tr><td>log4j.category.SIM_CONSOLE=<strong>DEBUG</strong>,SimConsoleApp,SimXMLApp</td></tr></tbody></table><p><br class="atl-forced-newline" />You can see more information about customizing the information displayed in the <strong>Console</strong> pane from the comment in the <em>simulation.properties</em> file. </p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="d0022ac9-7687-4e42-8d80-d11ae69c9478"><ac:parameter ac:name="id">32929691</ac:parameter><ac:rich-text-body><p><strong>Related page</strong></p><ul><li><ac:link><ri:page ri:content-title="Console pane" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=249570057 space=MMA version=1 -->
## PAGE 00712: Simulation information in diagrams

- page_id: `249570057`
- space_key: `MMA`
- source_url: https://docs.nomagic.com/spaces/MMA/pages/249570057/Simulation+information+in+diagrams
- version_number: 1
- version_date: `2024-01-30T09:23:24.945+01:00`
- ancestors: Magic Model Analyst / Cameo Simulation Toolkit Documentation > User Guide > Animation
- labels: ['simulation-information-in-diagrams', 'simulation-dashboard']

### NORMALIZED CONTENT

#### CONTENT-LAYER: Types of diagrams

591998423

#### CONTENT-COLUMN: Types of diagrams

591998437

#### CONTENT-BLOCK: Types of diagrams

591998427

When simulating a model, you can display and manipulate simulation information in diagrams a similar way you do it in the Simulation window. For example, you can see and edit runtime values directly on Part shapes or send a trigger and see a flowing item with its name on a path.

In diagrams, the following simulation information can be displayed:

- [CONFLUENCE_PAGE title='Displaying simulation information' space='']
- [CONFLUENCE_PAGE title='Displaying simulation information' space='']
- [CONFLUENCE_PAGE title='Displaying simulation information' space='']
- [CONFLUENCE_PAGE title='Displaying simulation information' space='']

In addition, you can manipulate simulation information the following way:

- [CONFLUENCE_PAGE title='Manipulating simulation information' space='']
- [CONFLUENCE_PAGE title='Manipulating simulation information' space='']

#### NOTE: Types of diagrams

Types of diagrams

You can display and manipulate simulation information only in diagrams that are based on a Composite Structure Diagram. However, the flowing information on paths can be displayed both in diagrams based on a Composite Structure Diagram and an Activity Diagram.

[IMAGE alt='' src='']

###### This sample model simulation demonstrates how you can use diagrams to view and manipulate the same simulation information as in the Simulation window.

1768204143

**Related pages**

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="6bf017af-e7d8-4502-86e9-d7c3a81dfb48"><ac:parameter ac:name="id">591998423</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="a73f232d-7f22-471b-bd43-955e51c1b87d"><ac:parameter ac:name="id">591998437</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="1805d11d-5c27-4884-8703-66e8a532e58f"><ac:parameter ac:name="id">591998427</ac:parameter><ac:rich-text-body><p>When simulating a model, you can display and manipulate <ac:inline-comment-marker ac:ref="ef7357aa-9c4b-4fb2-b9d9-c1c9b1ef1a27">simulation information</ac:inline-comment-marker> in diagrams a similar way you do it in the Simulation window. For example, you can see and edit runtime values directly on Part shapes or send a trigger and see a flowing item with its name on a path.</p><p>In diagrams, the following simulation information can be displayed:</p><ul><li><ac:link ac:anchor="Displaying active States"><ri:page ri:content-title="Displaying simulation information" /><ac:plain-text-link-body><![CDATA[Active state of the represented element]]></ac:plain-text-link-body></ac:link></li><li><ac:inline-comment-marker ac:ref="63b7736a-6739-4837-9bcf-48f88908a863"><ac:link ac:anchor="Displaying active State images"><ri:page ri:content-title="Displaying simulation information" /><ac:plain-text-link-body><![CDATA[Active state image]]></ac:plain-text-link-body></ac:link></ac:inline-comment-marker></li><li><ac:link ac:anchor="Displaying runtime values"><ri:page ri:content-title="Displaying simulation information" /><ac:plain-text-link-body><![CDATA[Runtime values on Part shapes]]></ac:plain-text-link-body></ac:link></li><li><ac:inline-comment-marker ac:ref="d3003d78-d52a-44d6-b4bd-67a5a81a1a05"><ac:link ac:anchor="Displaying flowing information"><ri:page ri:content-title="Displaying simulation information" /><ac:plain-text-link-body><![CDATA[Flowing information on paths]]></ac:plain-text-link-body></ac:link></ac:inline-comment-marker></li></ul><p><ac:inline-comment-marker ac:ref="fd214bd5-2efa-4e63-8ce8-694ce8e01591">In addition, you can manipulate simulation information the following way:</ac:inline-comment-marker></p><ul><li><ac:inline-comment-marker ac:ref="e39bf967-00e1-4abd-9dd5-fdfad72e26c8"><ac:link ac:anchor="Changing runtime values"><ri:page ri:content-title="Manipulating simulation information" /><ac:plain-text-link-body><![CDATA[Enter or change runtime values]]></ac:plain-text-link-body></ac:link></ac:inline-comment-marker></li><li><ac:inline-comment-marker ac:ref="f44af93d-1a6e-4673-be41-5e7026f8c6fb"><ac:link ac:anchor="Sending a trigger"><ri:page ri:content-title="Manipulating simulation information" /><ac:plain-text-link-body><![CDATA[Send a trigger]]></ac:plain-text-link-body></ac:link><br /><br /></ac:inline-comment-marker></li></ul><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="096310cf-d7e9-4611-b89d-dfb5df048f9c"><ac:parameter ac:name="title">Types of diagrams</ac:parameter><ac:rich-text-body><p>You can display and manipulate simulation information only in diagrams that are based on a Composite Structure Diagram. However, the flowing information on paths can be displayed both in diagrams based on a Composite Structure Diagram and an Activity Diagram.</p></ac:rich-text-body></ac:structured-macro><p><br /></p><p><ac:image ac:align="center"><ri:attachment ri:filename="simulation_dashboard.png" /></ac:image></p><h6 style="text-align: center;">This sample model simulation demonstrates how you <ac:inline-comment-marker ac:ref="0005294c-3b94-46b3-837e-89473b8da3f6">can use diagrams</ac:inline-comment-marker> to view and <ac:inline-comment-marker ac:ref="2e21e01c-5ae3-4e9f-844a-dd32e9996bcc">manipulate</ac:inline-comment-marker> the same simulatio<ac:inline-comment-marker ac:ref="b1566d8f-9c51-4020-8792-6e3008037c47">n information</ac:inline-comment-marker> as in the Simulation window.</h6></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="75b390af-06fa-4672-9de1-54003da1b4ec"><ac:parameter ac:name="id">1768204143</ac:parameter><ac:rich-text-body><p><strong>Related pages</strong></p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="ed921279-7c2d-480c-aaaa-ee071c678e2d" /></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=249569676 space=MMA version=2 -->
## PAGE 00713: Simulation log

- page_id: `249569676`
- space_key: `MMA`
- source_url: https://docs.nomagic.com/spaces/MMA/pages/249569676/Simulation+log
- version_number: 2
- version_date: `2025-08-19T14:56:06.091+02:00`
- ancestors: Magic Model Analyst / Cameo Simulation Toolkit Documentation > User Guide > Simulation Configuration and UI modeling
- labels: ['simulation-log', 'log']

### NORMALIZED CONTENT

Magic Model Analyst / Cameo Simulation Toolkit provides a simulation log, which is an element to record all event occurrences during simulation of a Simulation Configuration. It is a Class element applied with a «SimulationLog» stereotype. The «SimulationLog» stereotype comes with tag definitions as the options for selecting information that you want to record.

[IMAGE alt='' src='']

###### Simulation log.

The tag definitions of the «SimulationLog» stereotype are as follows

- recordedValues To specify the property whose value will be recorded to the simulation log.
- recordSignals To specify whether the simulation log will record signals that are sent during simulation. If the value is true , all of the sent signals will be recorded.
- recordActivation To specify whether the simulation log will record elements that are activated during simulation. If the value is true , all of the activated elements will be recorded.
- recordCalls To specify whether the simulation log will record Operations/Behaviors that are called during simulation. If the value is true , all of the called Operations/Behaviors will be recorded.
- recordConstraintFailures To specify whether the simulation log will record elements whose runtime values or objects fail the constraints applied on them. If the value is true , the elements that cause constraint failures will be recorded.

You can create a new simulation log element and set it as a tagged value of the log tag definition of the Simulation Configuration as shown in the following figure

[IMAGE alt='' src='']

###### Simulation Config.

A model-based simulation log or trace has many benefits including

- The source of various customized reports and analysis using the MagicDraw validation mechanism (as both are model-based).
- The capability to import simulation data into any other UML compliant tools.

You can record multiple simulation sessions or test results in the same «SimulationLog» element. The session's start time can be seen as an attribute's name. You can also record the following runtime data (see the following figure)

**Signal****Instance** 
(when recordSignals = true) under the "Signal Instances" node: timestamp (that is the relative occurrence time in milliseconds: '0' when the simulation starts), signal type, and target (see the following figure).

**Sequence****of****Activation** and **Sequence****of****Deactivation** 
(when recordActivation = true) under the "Activation Sequence" node: timestamp and types of the element being activated or deactivated.

**Behavior Call** and **Operation****Call** 
(when recordCalls = true) under the "Behavior Calls" and "Operation Calls" nodes respectively: timestamp, type, target, and value(s).

**Runtime Value** 
(when the recordedValues attribute has at least one Property selected) under the "Value Changes" node: timestamp and the Property and value(s) of a selected Property.

**Constraint Failure** 
(when recordedConstraintFailures = true) under the "Constraint Failures" node: timestamp, element, target, and value(s).

[IMAGE alt='' src='']

###### Recorded runtime information from the Stopwatch sample.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>Magic Model Analyst / Cameo Simulation Toolkit provides a simulation log, which is an element to record all event occurrences during simulation of a Simulation Configuration. It is a Class element applied with a «SimulationLog» stereotype. The «SimulationLog» stereotype comes with tag definitions as the options for selecting information that you want to record. </p><p><ac:image ac:align="center"><ri:attachment ri:filename="Figure_0016.png" /></ac:image></p><h6 style="text-align: center;">Simulation log.</h6><p>The tag definitions of the «SimulationLog» stereotype are as follows</p><ul><li><strong>recordedValues</strong><span> <br />To specify the property whose value will be recorded to the simulation log.<br /></span></li><li><strong>recordSignals</strong> <br />To specify whether the simulation log will record signals that are sent during simulation. If the value is <strong>true</strong>, all of the sent signals will be recorded. </li><li><strong>recordActivation</strong> <br />To specify whether the simulation log will record elements that are activated during simulation. If the value is <strong>true</strong>, all of the activated elements will be recorded.</li><li><strong>recordCalls</strong> <br />To specify whether the simulation log will record Operations/Behaviors that are called during simulation. If the value is <strong>true</strong>, all of the called Operations/Behaviors will be recorded.</li><li><strong>recordConstraintFailures</strong> <br />To specify whether the simulation log will record elements whose runtime values or objects fail the constraints applied on them. If the value is <strong>true</strong>, the elements that cause constraint failures will be recorded.</li></ul><p>You can create a new simulation log element and set it as a tagged value of the log tag definition of the Simulation Configuration as shown in the following figure</p><p><ac:image ac:align="center" ac:title="A Simulation Log as a Simulation Configuration Log" ac:alt="A Simulation Log as a Simulation Configuration Log"><ri:attachment ri:filename="simulationConfig_log.png" /></ac:image></p><h6 style="text-align: center;">Simulation Config.<br class="atl-forced-newline" /> </h6><p>A model-based simulation log or trace has many benefits including</p><ul><li>The source of various customized reports and analysis using the MagicDraw validation mechanism (as both are model-based).</li><li>The capability to import simulation data into any other UML compliant tools. <br /><br /></li></ul><p>You can record multiple simulation sessions or test results in the same «SimulationLog» element. The session's start time can be seen as an attribute's name. You can also record the following runtime data (see the following figure)</p><p><strong>Signal </strong><strong>Instance</strong> <br />(when recordSignals = true) under the &quot;Signal Instances&quot; node: timestamp (that is the relative occurrence time in milliseconds: '0' when the simulation starts), signal type, and target (see the following figure).</p><p><strong>Sequence </strong><strong>of </strong><strong>Activation</strong> and <strong>Sequence </strong><strong>of </strong><strong>Deactivation</strong> <br />(when recordActivation = true) under the &quot;Activation Sequence&quot; node: timestamp and types of the element being activated or deactivated.</p><p><strong>Behavior Call</strong> and <strong>Operation </strong><strong>Call</strong> <br />(when recordCalls = true) under the &quot;Behavior Calls&quot; and &quot;Operation Calls&quot; nodes respectively: timestamp, type, target, and value(s). </p><p><strong>Runtime Value</strong> <br />(when the recordedValues attribute has at least one Property selected) under the &quot;Value Changes&quot; node: timestamp and the Property and value(s) of a selected Property.</p><p><strong>Constraint Failure</strong> <br />(when recordedConstraintFailures = true) under the &quot;Constraint Failures&quot; node: timestamp, element, target, and value(s). </p><p> </p><p><ac:image ac:align="center" ac:title="Recorded Runtime Information from the Stopwatch Sample" ac:alt="Recorded Runtime Information from the Stopwatch Sample"><ri:attachment ri:filename="spec-of-exec-sess.png" /></ac:image></p><h6 style="text-align: center;">Recorded runtime information from the Stopwatch sample.</h6>
````

<!--NOMAGIC_PAGE id=249571292 space=MMA version=3 -->
## PAGE 00714: Simulation modeling: Do's and Don't's

- page_id: `249571292`
- space_key: `MMA`
- source_url: https://docs.nomagic.com/spaces/MMA/pages/249571292/Simulation+modeling+Do+s+and+Don+t+s
- version_number: 3
- version_date: `2025-09-15T15:37:45.632+02:00`
- ancestors: Magic Model Analyst / Cameo Simulation Toolkit Documentation > User Guide
- labels: ['simulation-modeling']

### NORMALIZED CONTENT

##### Don’t: Create an fUML loop without any Action Activation

When the fUML model has a loop without any Action Activation in the loop as shown in the figure below, the code stack continually increases until **StackOverflowError** occurs, causing the execution to be unexpectedly terminated. You can see **StackOverflowError** in the **magicdraw.log** file.

[IMAGE alt='' src='']

###### The model runs an infinite loop until StackOverflowError occurs, and the execution is terminated.

##### Do: Add an Action Activation in the loop

To avoid **StackOverflowError**, you must add at least an Action Activation, e.g., **CallBehaviorAction** in the loop as shown in the figure below. The code stack will not increase continually without **StackOverflowError** because Simulation has code to cut the stack loop and recall the Action at **ActivityNodeActivation.receiveOffer()** and **ActionActivation.fire()** according to fUML v1.3 specification. The execution will be continuously run without unexpected termination.

[IMAGE alt='' src='']

###### The model runs an infinite loop without StackOverflowError, and the execution is not terminated.

##### Don't: Send multiple signals and multiple AcceptEventActions at the same time without synchronization at all

When the fUML model has multiple threads of sending signal and multiple threads of PREPARING TO READ the signal at the same time, with no synchronization at all, it may send a signal before other thread starts AcceptEventAction to listen for it in the event pool.

According to fUML semantics, an event is lost and removed if such is a case: According to fUML semantics, once an event occurrence is selected for dispatch, it is matched against the list of waiting event accepters for the active object. If a match is found, the event occurrence is passed to the event accepter using its accept operation. If no matching event acceptor is found, the event occurrence is not returned to the event pool and is lost.

###### [IMAGE alt='' src='']AcceptEventAction did not receive the Signal from the SendSignalAction

##### Do: Send signals only when all AcceptEventActions are activated

To avoid off-synchronization, you must synchronize sending and receiving activities, to make sure that you start sending only when all AcceptEventActions are activated. For example, you may send "Ready" signals after they are all activated to the sender.

###### [IMAGE alt='' src='']All AcceptEventActions are activated for receiving the Signal from the SendSignalAction

##### Don't: Create fUML loops with Fork nodes

When the fUML model has loops with Fork nodes as shown in the figure below, execution threads continually increase until the internal error occurs, causing the execution to be unexpectedly terminated.

[IMAGE alt='' src='']

###### The model has loops with Fork nodes

##### Do: Use a CallBehaviorAction to encapsulate Fork nodes

To avoid the internal error, you must add an activity with CallBehaviorAction to encapsulate Fork nodes in the loops as shown in the figure below. The thread will not increase continually because Simulation can clear the memory after finishing the activity that contains the CallBehaviorAction.

[IMAGE alt='' src='']

###### The model uses an activity to encapsulate a fork node

**Related pages**

- [CONFLUENCE_PAGE title='Action' space='MED']
- [CONFLUENCE_PAGE title='Execution' space='DEVG']
- [CONFLUENCE_PAGE title='Behavior' space='']
- [CONFLUENCE_PAGE title='Call Behavior Action' space='MED']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><h3>Don’t: Create an fUML loop without any Action Activation</h3><p>When the fUML model has a loop without any Action Activation in the loop as shown in the figure below, the code stack continually increases until <strong>StackOverflowError</strong> occurs, causing the execution to be unexpectedly terminated. You can see <strong>StackOverflowError</strong> in the <strong>magicdraw.log</strong> file.</p><p><br /></p><p><ac:image ac:align="center"><ri:attachment ri:filename="Loop without Action Activation.png" /></ac:image></p><h6 style="text-align: center;">The model runs an infinite loop until StackOverflowError occurs, and the execution is terminated.</h6><h3>Do: Add an Action Activation in the loop</h3><p>To avoid <strong>StackOverflowError</strong>, you must a<span style="color:var(--ds-text-accent-blue-bolder,#09326c);">dd at leas</span>t an Action Activation, e.g., <strong>CallBehaviorAction</strong> in the loop as shown in the figure below. The code stack will not increase continually without <strong>StackOverflowError</strong> because Simulation has code to cut the stack loop and recall the Action at <strong>ActivityNodeActivation.receiveOffer()</strong> and <strong>ActionActivation.fire()</strong> according to fUML v1.3 specification. The execution will be continuously run without unexpected termination.</p><p><br /></p><p><ac:image ac:align="center"><ri:attachment ri:filename="Loop with Action Activation.png" /></ac:image></p><h6 style="text-align: center;">The model runs an infinite loop without StackOverflowError, and the execution is not terminated.</h6><h3>Don't: Send multiple signals and multiple AcceptEventActions at the same time without synchronization at all</h3><p>When the fUML model has multiple threads of sending signal and multiple threads of PREPARING TO READ the signal at the same time, with no synchronization at all, it may send a signal before other thread starts AcceptEventAction to listen for it in the event pool. </p><p>According to fUML semantics, an event is lost and removed if such is a case: According to fUML semantics, once an event occurrence is selected for dispatch, it is matched against the list of waiting event accepters for the active object. If a match is found, the event occurrence is passed to the event accepter using its accept operation. If no matching event acceptor is found, the event occurrence is not returned to the event pool and is lost.</p><p><br /></p><h6 style="text-align: center;"><ac:image ac:align="center" ac:width="1100"><ri:attachment ri:filename="Don't multiple Send signals and multiple AcceptEventActions at the same time without synchronization at all.PNG" /></ac:image><span style="color:var(--ds-background-accent-gray-bolder,#626f86);">AcceptEventAction did not receive the Signal from the SendSignalAction</span></h6><h3>Do: Send signals only when all AcceptEventActions are activated</h3><p>To avoid off-synchronization, you must synchronize sending and receiving activities, to make sure that you start sending only when all AcceptEventActions are activated.  For example, you may send &quot;Ready&quot; signals after they are all activated to the sender.</p><p><br /></p><h6 style="text-align: center;"><ac:image ac:align="center" ac:width="1100"><ri:attachment ri:filename="Do Send signals only when all AcceptEventActions are activated.PNG" /></ac:image><span style="color:var(--ds-background-accent-gray-bolder,#626f86);">All AcceptEventActions are activated for receiving the Signal from the SendSignalAction</span></h6><h3>Don't: Create fUML loops with Fork nodes</h3><p>When the fUML model has loops with Fork nodes as shown in the figure below, execution threads continually increase until the internal error occurs, causing the execution to be unexpectedly terminated.</p><p><br /></p><p><ac:image ac:align="center"><ri:attachment ri:filename="Don't Create fUML loops with Fork nodes.PNG" /></ac:image></p><h6 style="text-align: center;"><span>The model has loops with Fork nodes</span></h6><h3>Do: Use a CallBehaviorAction to encapsulate Fork nodes</h3><p>To avoid the internal error, you must add an activity with CallBehaviorAction to encapsulate Fork nodes in the loops as shown in the figure below. The thread will not increase continually because Simulation can clear the memory after finishing the activity that contains the CallBehaviorAction.</p><p><br /></p><p><ac:image ac:align="center" ac:width="1100"><ri:attachment ri:filename="Do Use a CallBehaviorAction to encapsulate Fork nodes.PNG" /></ac:image></p><h6 style="text-align: center;"><span>The model uses an activity to encapsulate a fork node</span></h6></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><strong>Related pages</strong></p><ul><li data-uuid="5e74d978-2be6-401a-9ad4-325308b85959"><ac:link><ri:page ri:space-key="MED" ri:content-title="Action" /></ac:link></li><li data-uuid="b49d4809-9214-409c-a91b-5a9ea63fea53"><ac:link><ri:page ri:space-key="DEVG" ri:content-title="Execution" /></ac:link></li><li data-uuid="5977e923-e83b-43d6-a3fb-1df7993d6041"><ac:link><ri:page ri:content-title="Behavior" /></ac:link></li><li data-uuid="b1204a46-2619-451d-aafb-22f0e05790fc"><ac:link><ri:page ri:space-key="MED" ri:content-title="Call Behavior Action" /></ac:link></li></ul></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=249570850 space=MMA version=2 -->
## PAGE 00715: Simulation of SysML models

- page_id: `249570850`
- space_key: `MMA`
- source_url: https://docs.nomagic.com/spaces/MMA/pages/249570850/Simulation+of+SysML+models
- version_number: 2
- version_date: `2025-08-19T14:56:16.962+02:00`
- ancestors: Magic Model Analyst / Cameo Simulation Toolkit Documentation > User Guide
- labels: ['sysml-model-simulation']

### NORMALIZED CONTENT

- [CONFLUENCE_PAGE title='FMI 2.0 co-simulation' space=''] The Magic Model Analyst / Cameo Simulation Toolkit supports Functional Mockup Interface (FMI) Version 1.0 and 2.0. A component that implements FMI is called FMU (Functional Mockup Unit). The procedure to co-simulate FMU is outlined.
- [CONFLUENCE_PAGE title='Supported SysML elements' space=''] The Magic Model Analyst / Cameo Simulation Toolkit supports multiple SysML elements. All the supported SysML elements are outlined.
- [CONFLUENCE_PAGE title='Requirements traceability from the Variables pane' space=''] The Magic Model Analyst / Cameo Simulation Toolkit allows you to navigate from the runtime value or object to the SysML requirement during the model simulation. Tracing SysML requirements with the help of runtime value or object is outlined.
- [CONFLUENCE_PAGE title='Distribution Extensions' space=''] A Distributed Property is a property of a Block or a Value Type used to apply a probability distribution to the values of the property.The procedure to set a distributed property is outlined.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ul><li><ac:link><ri:page ri:content-title="FMI 2.0 co-simulation" /></ac:link><br /><span style="color: rgb(23,43,77);">The Magic Model Analyst / Cameo Simulation Toolkit supports Functional Mockup Interface (FMI) Version 1.0 and 2.0. A component that implements FMI is called FMU (Functional Mockup Unit). The procedure to co-simulate FMU is outlined.<br /><br /></span></li><li><ac:link><ri:page ri:content-title="Supported SysML elements" /></ac:link><br />The Magic Model Analyst / Cameo Simulation Toolkit supports multiple SysML elements. All the supported SysML elements are outlined.<br /><br /></li><li><ac:link><ri:page ri:content-title="Requirements traceability from the Variables pane" /></ac:link><br />The <span style="color: rgb(23,43,77);">Magic Model Analyst / Cameo Simulation Toolkit allows you to navigate from the runtime value or object to the SysML requirement during the model simulation. Tracing SysML requirements with the help of runtime value or object is outlined.<br /><br /></span></li><li><ac:link><ri:page ri:content-title="Distribution Extensions" /></ac:link><br /><span style="color: rgb(23,43,77);">A Distributed Property is a property of a Block or a Value Type used to apply a probability distribution to the values of the property.<span> The procedure to set a distributed property is outlined.</span></span></li></ul>
````

<!--NOMAGIC_PAGE id=249569549 space=MMA version=2 -->
## PAGE 00716: Simulation project template

- page_id: `249569549`
- space_key: `MMA`
- source_url: https://docs.nomagic.com/spaces/MMA/pages/249569549/Simulation+project+template
- version_number: 2
- version_date: `2025-09-12T15:08:39.495+02:00`
- ancestors: Magic Model Analyst / Cameo Simulation Toolkit Documentation > User Guide > Getting started
- labels: ['project-template']

### NORMALIZED CONTENT

1328636027

1328636029

1328636028

**Simulation** **Project** is a useful template that consists of fundamental diagrams and elements basically required for the user to work on a simulation project. The template significantly reduces time spent on working on the preparation of making simulation from scratch. The template is available in the **Simulation** project category in the **New Project** dialog.

To open a template

1. Click File > New Project on the MagicDraw main menu.
2. Select Simulation > Simulation Project in the New Project dialog.
3. Name your project, select its location, create a directory for the project, and click OK .

[IMAGE alt='' src='']

The Simulation Project template arranges basic and necessary diagrams represented by Class and Package diagrams including State Machine diagrams. The project template additionally encompasses Simulation Configuration to which a Simulation Target is set.

[IMAGE alt='' src='']

###### Simulation project template with the class and package diagrams.

1328636026

**Related pages**

- [CONFLUENCE_PAGE title='Class diagram' space='MT']
- [CONFLUENCE_PAGE title='Package diagram' space='MT']
- [CONFLUENCE_PAGE title='State Machine diagram' space='MT']
- [CONFLUENCE_PAGE title='Simulation Configuration and UI modeling' space='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="9c7aedea-da5d-47f2-8c6d-54702c106bbf"><ac:parameter ac:name="id">1328636027</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="8452fc2b-a795-414c-91b7-e1b5ae0ca361"><ac:parameter ac:name="id">1328636029</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="4a318e00-e591-49f9-9deb-d84b07bb4cc7"><ac:parameter ac:name="id">1328636028</ac:parameter><ac:rich-text-body><ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p><strong style="line-height: 1.42857;">Simulation</strong> <strong style="line-height: 1.42857;">Project</strong> is a useful template that consists of fundamental diagrams and elements basically required for the user to work on a simulation project. The template significantly reduces time spent on working on the preparation of making simulation from scratch. The template is available in the <strong style="line-height: 1.42857;">Simulation</strong> project category in the <strong style="line-height: 1.42857;">New Project</strong> dialog. </p><p><span style="color: rgb(0,0,0);">To open a template </span></p><hr /><ol><li>Click <strong>File</strong> &gt; <strong>New Project</strong> on the MagicDraw main menu.</li><li>Select <strong>Simulation</strong> &gt; <strong>Simulation Project </strong>in the <strong>New Project</strong> dialog. </li><li>Name your project, select its location, create a directory for the project, and click <strong>OK</strong>.</li></ol><p style="margin-left: 30.0px;"><br class="atl-forced-newline" /><ac:image ac:title=" The Simulation Project Template in the New Project Dialog " ac:alt=" The Simulation Project Template in the New Project Dialog "><ri:attachment ri:filename="cst-new-proj.png" /></ac:image></p><p>The Simulation Project template arranges basic and necessary diagrams represented by Class and Package diagrams including State Machine diagrams. The project template additionally encompasses Simulation Configuration to which a Simulation Target is set.<br /><span class="confluence-embedded-file-wrapper confluence-embedded-manual-size"><br /></span></p><p><span class="confluence-embedded-file-wrapper confluence-embedded-manual-size"> </span><ac:image ac:align="center" ac:title="The Simulation Project Template with the Class and Package Diagrams" ac:alt="The Simulation Project Template with the Class and Package Diagrams"><ri:attachment ri:filename="Simulation Project Template.PNG" /></ac:image></p><h6 style="text-align: center;">Simulation project template with the class and package diagrams.</h6></ac:layout-cell><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section></ac:layout></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="bf7e620f-0a2e-48d4-8bd5-7d0fad0a6591"><ac:parameter ac:name="id">1328636026</ac:parameter><ac:rich-text-body><p><strong>Related pages</strong></p><ul><li><ac:link><ri:page ri:space-key="MT" ri:content-title="Class diagram" /></ac:link></li><li><ac:link><ri:page ri:space-key="MT" ri:content-title="Package diagram" /></ac:link></li><li><ac:link><ri:page ri:space-key="MT" ri:content-title="State Machine diagram" /></ac:link></li><li><ac:link><ri:page ri:content-title="Simulation Configuration and UI modeling" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=249569681 space=MMA version=3 -->
## PAGE 00717: Simulation time and simulation clock

- page_id: `249569681`
- space_key: `MMA`
- source_url: https://docs.nomagic.com/spaces/MMA/pages/249569681/Simulation+time+and+simulation+clock
- version_number: 3
- version_date: `2025-08-19T14:56:06.170+02:00`
- ancestors: Magic Model Analyst / Cameo Simulation Toolkit Documentation > User Guide > Simulation Configuration and UI modeling
- labels: ['simulation-time', 'simulation-clock']

### NORMALIZED CONTENT

#### CONTENT-LAYER: Note

1348792145

#### CONTENT-COLUMN: Note

1348792147

#### CONTENT-BLOCK: Note

1348792146

When you simulate a model related to time (such as a transition with a time trigger), Magic Model Analyst / Cameo Simulation Toolkit will obtain the simulation time from a simulation clock. The simulation time is the amount of time spent simulating a model. Magic Model Analyst / Cameo Simulation Toolkit also uses the simulation time in the timestamp of a signal instance in a SimulationLog (see [CONFLUENCE_PAGE title='Simulation log' space='']), in a time series chart (see [CONFLUENCE_PAGE title='Time Series Chart' space='']), and on messages of a generated Sequence diagram.

There are three types of simulation clocks in Magic Model Analyst / Cameo Simulation Toolkit:

- Built-in clock. This is the default simulation clock.
- Internal simulation clock. This clock is designed to precisely control the simulation time. Its implementation is based on UML run-to-completion semantics and internal completion events.
- Model-based clock. You can select the model-based clock by making a property as the time value tag definition of a Simulation Config. See [CONFLUENCE_PAGE title='Model-based clock' space=''] for further details on the model-based clock.

#### NOTE: Note

Note

Nanosecond and microsecond are only supported in the internal simulation clock and model-based clock.

To open the Simulation Clock

- Right-click a sessionin the [Simulation Sessions](https://docs.nomagic.com/display/MMA/Understanding+simulation+sessions) pane and select Show Simulation Clock . [ATTACHMENT filename='Simulation_Clock.png']

[IMAGE alt='' src='']

###### The Simulation Clock dialog with the Step button.

#### NOTE: Note

Note

The **Step** button in the **Simulation Clock** dialog is available only for the internal simulation clock to allow manually increasing and ticking the internal simulation clock.

To show or****hide the Simulation Time

- Click [ATTACHMENT filename='Simulation Time_Icon.png'] in the toolbar of the Simulation window . [ATTACHMENT filename='Simulation Window showing Simulation Time.png']

By default, the Simulation time is always displayed.

36004161

**Related pages**

- Built-in clock
- Internal simulation clock
- Model-based clock
- [CONFLUENCE_PAGE title='Understanding simulation sessions' space='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="9b4118a7-68e0-48ad-ac1a-1af5cbe4509f"><ac:parameter ac:name="id">1348792145</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="fa0a9ca3-282c-410c-b72a-209cef6864cb"><ac:parameter ac:name="id">1348792147</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="d01da5e9-a85a-40cf-987d-25908b6d62c3"><ac:parameter ac:name="id">1348792146</ac:parameter><ac:rich-text-body><p>When you simulate a model related to time (such as a transition with a time trigger), Magic Model Analyst / Cameo Simulation Toolkit will obtain the simulation time from a simulation clock. The simulation time is the amount of time spent simulating a model. Magic Model Analyst / Cameo Simulation Toolkit also uses the simulation time in the timestamp of a signal instance in a SimulationLog (see <ac:link><ri:page ri:content-title="Simulation log" /></ac:link>), in a time series chart (see <ac:link><ri:page ri:content-title="Time Series Chart" /></ac:link>), and on messages of a generated Sequence diagram. </p><p>There are three types of simulation clocks in Magic Model Analyst / Cameo Simulation Toolkit:</p><ul><li><p class="auto-cursor-target">Built-in clock. This is the default simulation clock.</p></li><li>Internal simulation clock. This clock is designed to precisely control the simulation time. Its implementation is based on UML run-to-completion semantics and internal completion events.</li><li>Model-based clock. You can select the model-based clock by making a property as the time value tag definition of a Simulation Config. See <ac:link><ri:page ri:content-title="Model-based clock" /><ac:plain-text-link-body><![CDATA[Model-based Clock]]></ac:plain-text-link-body></ac:link> for further details on the model-based clock.<br /><br /></li></ul><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="bc333e82-f65d-4235-8203-1466d1b0e4ee"><ac:parameter ac:name="title">Note</ac:parameter><ac:rich-text-body><p>Nanosecond and microsecond are only supported in the internal simulation clock and model-based clock.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><ac:inline-comment-marker ac:ref="09040418-9426-4d2f-b7a5-9727dc253c7f">To open the Simulation Clock</ac:inline-comment-marker></p><hr /><ul><li class="auto-cursor-target"><ac:inline-comment-marker ac:ref="a4dc57a8-67b7-403e-8ab1-c86b0621378c">Right-click a <span style="color: rgb(62,63,64);">session </span>in the </ac:inline-comment-marker><strong><a href="https://docs.nomagic.com/display/MMA/Understanding+simulation+sessions"><ac:inline-comment-marker ac:ref="a4dc57a8-67b7-403e-8ab1-c86b0621378c">Simulation Sessions</ac:inline-comment-marker></a></strong><ac:inline-comment-marker ac:ref="a4dc57a8-67b7-403e-8ab1-c86b0621378c"> pane</ac:inline-comment-marker> and select<strong> Show Simulation Clock</strong>.<br /><br /><ac:image ac:height="93"><ri:attachment ri:filename="Simulation_Clock.png" /></ac:image></li></ul><p><br /></p><p><ac:image ac:align="center"><ri:attachment ri:filename="Simulation clock.PNG" /></ac:image></p><h6 style="text-align: center;"><ac:inline-comment-marker ac:ref="47e61e8a-57a7-4630-b86f-f9516673cdff">The Simulation Clock dialog with the Step button.</ac:inline-comment-marker></h6><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="01c00e13-d9b9-401c-b742-298bde8659a1"><ac:parameter ac:name="title">Note</ac:parameter><ac:rich-text-body><p>The <strong>Step</strong> button in the <strong>Simulation Clock</strong> dialog is available only for the internal simulation clock to allow manually increasing and ticking the internal simulation clock.</p></ac:rich-text-body></ac:structured-macro><p><br /></p><p><ac:inline-comment-marker ac:ref="a6aecb99-82af-4153-b2ea-88de21adb66e">To show or</ac:inline-comment-marker><strong><ac:inline-comment-marker ac:ref="a6aecb99-82af-4153-b2ea-88de21adb66e"> </ac:inline-comment-marker></strong><ac:inline-comment-marker ac:ref="a6aecb99-82af-4153-b2ea-88de21adb66e">hide the Simulation Time</ac:inline-comment-marker></p><hr /><ul><li>Click <ac:image ac:thumbnail="true" ac:height="32"><ri:attachment ri:filename="Simulation Time_Icon.png" /></ac:image> <ac:inline-comment-marker ac:ref="c0697a16-356c-4a0e-a125-19d5ad1dae05">in the <span style="color: rgb(62,63,64);">toolbar of the </span></ac:inline-comment-marker><strong><ac:inline-comment-marker ac:ref="c0697a16-356c-4a0e-a125-19d5ad1dae05">Simulation </ac:inline-comment-marker></strong><ac:inline-comment-marker ac:ref="c0697a16-356c-4a0e-a125-19d5ad1dae05">window</ac:inline-comment-marker>.<br /><br /><ac:image><ri:attachment ri:filename="Simulation Window showing Simulation Time.png" /></ac:image><br /><br /></li></ul><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="3b00bcf3-aca6-427c-8717-8de99838d4b7"><ac:rich-text-body><p>By default, the Simulation time is always displayed.</p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="005a81c7-035e-4f47-8b0f-43fae89168e8"><ac:parameter ac:name="id">36004161</ac:parameter><ac:rich-text-body><p><strong>Related pages</strong></p><ul class="childpages-macro"><li><a href="https://docs.nomagic.com/display/MMA/Built-in+clock">Built-in clock</a></li><li><a href="https://docs.nomagic.com/display/MMA/Internal+simulation+clock">Internal simulation clock</a></li><li><a href="https://docs.nomagic.com/display/MMA/Model-based+clock">Model-based clock</a></li><li><ac:link><ri:page ri:content-title="Understanding simulation sessions" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=249571165 space=MMA version=3 -->
## PAGE 00718: Simulation using Jupyter Notebook

- page_id: `249571165`
- space_key: `MMA`
- source_url: https://docs.nomagic.com/spaces/MMA/pages/249571165/Simulation+using+Jupyter+Notebook
- version_number: 3
- version_date: `2025-12-03T10:07:52.254+01:00`
- ancestors: Magic Model Analyst / Cameo Simulation Toolkit Documentation > User Guide > Server-side simulation
- labels: []

### NORMALIZED CONTENT

You can simulate Teamwork Cloud projects on the server by using Jupyter Notebook. This chapter explains how to set up Jupyter Notebook for server-side simulation and lists all available commands with examples.

#### NOTE: Prerequisites

Prerequisites

Before starting the simulation, make sure you have [CONFLUENCE_PAGE title='Server-side simulation' space=''].

##### Setting up Jupyter Notebook

To set up Jupyter Notebook

- In Jupyter Notebook, run the following command to install a Python package from the <*install_root**>\plugins\com.nomagic.magicdraw.simulation\**pyST.zip*file:

##### Create client/session and authenticate

lightgrey

1

solid

client = SimulationWebClient('http(s)://<server_host>:<server_port>','<username>', '<password>', '<token>', False)

This request starts a work session and provides authentication to Teamwork Cloud.

The following table describes the parameters used in the request:

| Parameter | In | Required or optional | Description |
| --- | --- | --- | --- |
| server_host | path | required | The Teamwork Cloud server host name. |
| server_port | path | required | The Teamwork Cloud server port. |
| username | path | optional | The Teamwork Cloud user name. If you do not specify the user name in the request, an input field will be provided to specify it later. |
| password | path | optional | The Teamwork Cloud password. If you do not specify the password in the request, an input field will be provided to specify it later. |
| token | path | optional | The Teamwork Cloud token. You can either provide a username/password or a token. To learn more about generating a token, click . |

For instructions on how to run server-side simulation using SSL, refer to [CONFLUENCE_PAGE title='Running server-side simulation with SSL' space='']

##### Get the list of Teamwork Cloud projects

lightgrey

1

solid

client.get_projects()

This request provides the list of Teamwork Cloud projects accessible to you depending on your permissions. Only projects that you can read (the Read Resources permission) are returned.

```text

```

##### Run simulation

lightgrey

1

solid

client.run(<project>, version=<version>, branch=<branch>, element=<element>, config=<config>, started_from=<starting location>, commit_results=<True/False>, verification=<All/None/Fail>, data=json.dumps(<param> ),****timeout=<timeout duration>, sync=<True/False>)

This request initiates the execution of the specified Simulation Configuration in a particular project. It connects to Teamwork Cloud, finds the element to execute, and initiates the execution if the element exists. After the execution is complete, the request constructs and returns a unique ID (per application) for the given execution.

The following table describes the parameters used in the request:

| Parameter | In | Required or optional | Description | Options |
| --- | --- | --- | --- | --- |
| project | path | required | The Teamwork Cloud project name or ID. | NA |
| version | path | optional | The Teamwork Cloud project version. | NA |
| branch | path | optional | The project branch name or ID. If the branch is omitted, the trunk is used instead. | NA |
| element | path | optional | The qualified name or server ID of the element to be executed. | NA |
| config | path | optional | The Simulation Configuration name or server ID. | NA |
| started_from | path | optional | Allows specifying the starting location of the simulation. The value of the started_from parameter is provided in the status endpoint response. | NA |
| commit_results | path | optional | Commits a new project version with the simulation results. Available values are True or False (default). | NA |
| verification | path | optional | Returns the selected verification results. Available values are:All - all verification results are returned.None - no verification results are returned.Fail (default) - verification results with the fail status are returned. | NA |
| data | path | optional | A set of output parameters, which will be obtained after the simulation is complete. | NA |
| timeout | path | optional | Allows specifying the timeout duration in minutes. If the timeout parameter is not provided, the sim.timeout.min property will be taken from the webappplatform.properties instead. | NA |
| sync | path | optional | Initiates a synchronous API call. If the sync is set to 'True', the call will return when it is completed. Available values are True or False (default). | NA |
| simconfig | body | optional | The set of simulation configuration properties along with their corresponding values. The simulation configuration options you specify will take precedence over the initial configuration option from a model. | "ALLOW_CONCURRENT_ALLOCATED_ACTIVITIES": true,"AUTOMATIC_PARAMETRIC_RECALCULATION": true,"AUTO_CONVERT_UNITS": true,"AUTO_CREATE_FUML_OBJECT_OF_OUTPUT_PIN": true,"AUTO_START": true,"AUTO_START_ACTIVE_OPTIONS": true,"AUTO_TERMINATE": true,"CLOCK_RATIO": 1,"CLONE_REFERENCES": true,"COMPLETION_EVENTS_AND_TRANSITIONS": true,"CONSTRAINT_FAILURE_AS_BREAKPOINT": true,"DECIMAL_PLACES": 4,"DEFAULT_LANGUAGE": "JavaScript Rhino","DURATION_SIMULATION_MODE": "MIN", // possible values: MIN, MAX, AVERAGE, RANDOM"ENDTIME": 0,"ENGINES_PRIORITY": "[on] fUML Engine\n[on] Interaction Engine\n[on] SCXML Engine","INITIALIZE_NUMERICAL_VALUE": false,"INITIALIZE_REFERENCES": true,"NUMBER_OF_RUNS": 0,"NUMBER_OF_STEPS": 0,"PASS_CALLER_CONTEXT": true,"RECORD_TIMESTAMP": false,"REMEMBER_FAILURE_STATUS": true,"RESULT_LOCATION": "Results","RUN_FORKS_IN_PARALLEL": true,"SOLVE_AFTER_INITIALIZATION": true,"START_TIME": 0,"STATE_ACTIVATION_SEMANTICS": "BEFORE_ENTRY", // possible values: "BEFORE_ENTRY", "AFTER_ENTRY""STEP_DELAY": 0,"STEP_SIZE": 0,"TERMINATE_BEHAVIOR_ON_EXCEPTION_THROWN": true,"TERMINATE_NESTED_BEHAVIORS": true,"TERMINATE_STREAMING_BEHAVIORS_BY_OUTPUT_PARAMETER_MULTIPLICITY": false,"TIME_UNIT": "MILLISECOND","TIME_VALUE": "Model-based Clock Test::Clock::time","TIME_VARIABLE_NAME": "simtime","TREAT_ALL_CLASSIFIERS_AS_ACTIVE": true,"USE_FUML_DECISION_SEMANTICS": false |

```text

```

```text

```

To enable the autocompletion option for specifying the simulation in Jupyter, use**from pyST import simconfig**

**[IMAGE alt='' src='']**

##### Perform a time step

lightgrey

1

client.step(<simulation_id>, sync=<True/False>)

This request performs a single time step of the specified simulation. To run the simulation by step, it should be run with the **AUTO_START**option of the simconfig parameter set to*false*.

The following table describes the parameters used in the request:

| Parameter | In | Required or optional | Description |
| --- | --- | --- | --- |
| simulation_id | path | optional | The ID of a specific simulation.If the simulation_id is not specified, the pyST client will use the simulation_id of the last simulation run. |
| sync | path | optional | Initiates a synchronous API call. If the sync is set to 'True', the call will return when it is completed. Available values are True or False (default). |

##### Start simulation

lightgrey

1

client.start(<simulation_id>)

This request starts the execution of the specified simulation. If the initialization phase is still in progress, the start endpoint is memorized and sent when the initialization phase is completed.

The following table describes the parameters used in the request:

| Parameter | In | Required or optional | Description |
| --- | --- | --- | --- |
| simulation_id | path | optional | The ID of a specific simulation.If the simulation_id is not specified, the pyST client will use the simulation_id of the last simulation run. |

##### Start simulation and get results

lightgrey

1

solid

client.simulate(<project>, version=<version>, branch=<branch>, element=<element>, config=<config>, commit_results=<True/False>, verification=<All/None/Fail>, data=json.dumps(<param>))

This request starts a simulation and returns its results.

The following table describes the parameters used in the request:

| Parameter | In | Required or optional | Description | Options |
| --- | --- | --- | --- | --- |
| project | path | required | The Teamwork Cloud project name or ID. | NA |
| version | path | optional | The Teamwork Cloud project version. | NA |
| branch | path | optional | The project branch name or ID. If the branch is omitted, the trunk is used instead. | NA |
| element | path | optional | The qualified name or server ID of the element to be executed. | NA |
| config | path | optional | The Simulation Configuration name or server ID. | NA |
| commit_results | path | optional | A new project version is committed with the simulation results. Available values are True or False (default). | NA |
| verification | path | optional | Returns the selected verification results. Available values are:All - all verification results are returned.None - no verification results are returned.Fail - verification results with the fail status are returned including the main status and the status of requirements and constraints.If the verification value is not specified, only the verification results with the fail status are returned when the get_results endpoint is called. | NA |
| data | path | optional | A set of output parameters, which will be obtained after the simulation is complete. | NA |
| simconfig | body | optional | The set of simulation configuration properties along with their corresponding values. The simulation configuration options you specify will take precedence over the initial configuration option from a model. | "ALLOW_CONCURRENT_ALLOCATED_ACTIVITIES": true,"ANIMATION_SPEED": 95,"AUTOMATIC_PARAMETRIC_RECALCULATION": true,"AUTO_CONVERT_UNITS": true,"AUTO_CREATE_FUML_OBJECT_OF_OUTPUT_PIN": true,"AUTO_START": true,"AUTO_START_ACTIVE_OPTIONS": true,"AUTO_TERMINATE": true,"CAPTURE_TIMESTAMP": false,"CLOCK_RATIO": 1,"CLONE_REFERENCES": true,"COMPLETION_EVENTS_AND_TRANSITIONS": true,"CONSTRAINT_FAILURE_AS_BREAKPOINT": true,"DECIMAL_PLACES": 4,"DEFAULT_LANGUAGE": "JavaScript Rhino","DURATION_SIMULATION_MODE": "MIN", // possible values: MIN, MAX, AVERAGE, RANDOM"ENDTIME": 0,"ENGINES_PRIORITY": "[on] fUML Engine\n[on] Interaction Engine\n[on] SCXML Engine","INITIALIZE_NUMERICAL_VALUE": false,"INITIALIZE_REFERENCES": true,"NUMBER_OF_RUNS": 0,"NUMBER_OF_STEPS": 0,"PASS_CALLER_CONTEXT": true,"RECORD_TIMESTAMP": false,"REMEMBER_FAILURE_STATUS": true,"RESULT_LOCATION": "Results","RUN_FORKS_IN_PARALLEL": true,"SHOW_ANNOTATIONS": false,"SOLVE_AFTER_INITIALIZATION": true,"START_TIME": 0,"STATE_ACTIVATION_SEMANTICS": "BEFORE_ENTRY", // possible values: "BEFORE_ENTRY", "AFTER_ENTRY""STEP_DELAY": 0,"STEP_SIZE": 0,"TERMINATE_BEHAVIOR_ON_EXCEPTION_THROWN": true,"TERMINATE_NESTED_BEHAVIORS": true,"TERMINATE_STREAMING_BEHAVIORS_BY_OUTPUT_PARAMETER_MULTIPLICITY": false,"TIME_UNIT": "MILLISECOND","TIME_VALUE": "Model-based Clock Test::Clock::time","TIME_VARIABLE_NAME": "simtime","TREAT_ALL_CLASSIFIERS_AS_ACTIVE": true,"USE_FUML_DECISION_SEMANTICS": false |

```text

```

```text

```

To enable the autocompletion option for specifying the simulation in Jupyter, use**from pyST import simconfig**

**[IMAGE alt='' src='']**

##### Get simulation status

lightgrey

1

client.get_status(<simulation_id>)

This request gets the status of a specific simulation. If the model has aUI mockup, Time Series Chart, Timeline Chart, or HTML Table, you can use the URL provided in the 'ui' or indexUI' key to open the specified UI.

The following table describes the parameters used in the request:

| Parameter | In | Required or optional | Description |
| --- | --- | --- | --- |
| simulation_id | path | optional | The ID of a specific simulation.If the simulation_id is not specified, the pyST client will use the simulation_id of the last simulation run. |

```text

```

##### Get simulation variables

lightgrey

1

solid

client.get_variables(<simulation_id>, variables=json.dumps(<parameters>))

This request returns a list of simulation variables during simulation.

The following table describes the parameters used in the request:

| Parameter | In | Required or optional | Description |
| --- | --- | --- | --- |
| simulation_id | path | optional | The ID of the running simulation.If the simulation_id is not specified, the pyST client will use the simulation_id of the last simulation run. |
| variables | path | optional | The set of simulation variables that should be obtained. If no variables are specified, the values of all simulation variables are returned. |

##### Set simulation variables

lightgrey

1

solid

client.set_variables(<simulation_id>, variables=json.dumps(<parameters>), context=<context ID>, property_path=<property path>)

This request provides a list of simulation variables with values.

The following table describes the parameters used in the request:

| Parameter | In | Required or optional | Description |
| --- | --- | --- | --- |
| simulation_id | path | optional | The ID of the running simulation.If the simulation_id is not specified, the pyST client will use the simulation_id of the last simulation run. |
| variables | path | required | The set of simulation variables with values that should be used during the current simulation. |
| context | path | optional | The context ID. |
| property_path | path | optional | The property path of the context specified using property names or IDs. |

```text

```

#### NOTE: Alternative method to set a single simulation variable

Alternative method to set a single simulation variable

A simplified **Set Simulation Variable** method can be used when setting a single value, which does not require constructing a JSON.

client.set_variable(<name>, <value>, <simulation_id> (optional), <context> (optional), <propertyPath> (optional)).

For example, set_variable(name="mass", value=100, propertyPath = "car.engine").

You can also omit parameter names if the parameters are in the correct sequence, for example, client.set_variable("mass", 100).

##### Pause simulation

lightgrey

1

solid

client.pause(<simulation_id>)

This request pauses the execution of the specified simulation.

The following table describes the parameters used in the REST API request:

| Parameter | In | Required or optional | Description |
| --- | --- | --- | --- |
| simulation_id | path | optional | The ID of the running simulation.If the simulation_id is not specified, the pyST client will use the simulation_id of the last simulation run. |

##### Resume simulation

lightgrey

1

solid

client.resume(<simulation_id>)

This request resumes the execution of the specified simulation.

The following table describes the parameters used in the REST API request:

| Parameter | In | Required or optional | Description |
| --- | --- | --- | --- |
| simulation_id | path | optional | The ID of the running simulation.If the simulation_id is not specified, the pyST client will use the simulation_id of the last simulation run. |

##### Get simulation results

lightgrey

1

solid

client.get_result(<simulation_id>)

This request returns the results of the specified simulation. If the **OutputParameters** tag of the executed Simulation Configuration is specified, the results are provided according to the **OutputParameters** tag value. If a Time Series or Timeline chart is specified for the Simulation Configuration, the chart data is returned in the JSON format.

The figure below demonstrates how to specify input and output parameters.

[IMAGE alt='' src='']

###### Specifying input and output parameters.

The following table describes the parameters used in the request:

| Parameter | In | Required or optional | Description |
| --- | --- | --- | --- |
| simulation_id | path | optional | The ID of the running simulation.If the simulation_id is not specified, the pyST client will use the simulation_id of the last simulation run. |

##### Get the list of running simulations

lightgrey

1

solid

```text
client.get_running()
```

This REST API request gets the list of all currently running simulations including the queued simulations that are placed in a waiting line.

##### Terminate simulation

lightgrey

1

solid

client.terminate(<simulation_id>, sync=<True/False>)

This request terminates the specified simulation.

The following table describes the parameters used in the request:

| Parameter | In | Required or optional | Description |
| --- | --- | --- | --- |
| simulation_id | path | optional | The ID of a specific simulation.If the simulation_id is not specified, the pyST client will use the simulation_id of the last simulation run. |
| sync | path | optional | Initiates a synchronous API call. If the sync is set to 'True', the call will return when it is completed. Available values are True or False (default). |

##### Check for Simulation Configurations

lightgrey

1

solid

client.has_configurations(<project>, version=<version>, branch=<branch>)

This request checks if the project has any Simulation Configurations.

The following table describes the parameters used in the request:

| Parameter | In | Required or optional | Description |
| --- | --- | --- | --- |
| project | path | required | The Teamwork Cloud project name or ID. |
| version | path | optional | The Teamwork Cloud project version. |
| branch | path | optional | The project branch name or ID. If the branch is omitted, the trunk is used instead. |

##### Get Simulation Configurations

lightgrey

1

solid

client.get_configurations(<project>, version=<version>, branch=<branch>, element=<element>, filter=<ui>)

This request retrieves the names and descriptions of the Simulation Configurations available for the given project.

The following table describes the parameters used in the request:

| Parameter | In | Required or optional | Description |
| --- | --- | --- | --- |
| project | path | required | The Teamwork Cloud project name or ID. |
| version | path | optional | The Teamwork Cloud project version. |
| branch | path | optional | The project branch name or ID. If the branch is omitted, the trunk is used instead. |
| element | path | optional | The qualified name or server ID of the element to be executed. |
| filter | path | optional | Returns Simulations Configurations with a specified UI tag for a particular project. The only possible value for the filter parameter is ui.Only Simulations Configurations having at least one of the following UI elements are returned:FrameTableTimeSeries chartTimeline chart |

##### Get Simulation Configuration descriptor

lightgrey

1

solid

client.get_descriptor(<project>, version=<version>, branch=<branch>, config=<config>)

This REST API request retrieves Simulation Configuration data (description, execution target,time step,input and output parameters) from the specified project. The set of input and output parameters is specified using the **Input Parameters** and **Output Parameters** properties of a Simulation Configuration.The figure below demonstrates how to specify input and output parameters.

[IMAGE alt='' src='']

###### Specifying input and output parameters.

The following table describes the parameters used in the request:

| Parameter | In | Required or optional | Description |
| --- | --- | --- | --- |
| project | path | required | The Teamwork Cloud project name or ID. |
| version | path | optional | The Teamwork Cloud project version. |
| branch | path | optional | The project branch name or ID. If the branch is omitted, the trunk is used instead. |
| config | path | optional | The Simulation Configuration name or server ID. |

```text

```

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>You can simulate Teamwork Cloud projects on the server by using Jupyter Notebook. This chapter explains how to set up Jupyter Notebook for server-side simulation and lists all available commands with examples.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="4b2c6a4e-9f6c-43f4-a634-89475a2b7d2a"><ac:parameter ac:name="title">Prerequisites</ac:parameter><ac:rich-text-body><p>Before starting the simulation, make sure you have <ac:link ac:anchor="Preparing projects for server-side simulation"><ri:page ri:content-title="Server-side simulation" /><ac:plain-text-link-body><![CDATA[prepared your projects for server-side simulation]]></ac:plain-text-link-body></ac:link>.</p></ac:rich-text-body></ac:structured-macro><h3>Setting up Jupyter Notebook</h3><p>To set up Jupyter Notebook</p><hr /><ul><li><p class="auto-cursor-target">In Jupyter Notebook, run the following command to install a Python package from the &lt;<em style="text-align: left;">install_root</em><em>&gt;\plugins\com.nomagic.magicdraw.simulation\</em><em><span style="color:var(--ds-text,#333333);">pyST.zip</span> </em>file:</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="16870fe8-2f0b-48f1-a7d3-8b3dad3a29f1"><ac:plain-text-body><![CDATA[%pip install pyST.zip]]></ac:plain-text-body></ac:structured-macro></li></ul><h3>Create client/session and authenticate</h3><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="dc1c47b0-74c6-4d38-ae40-35a93e8d3633"><ac:parameter ac:name="borderColor">lightgrey</ac:parameter><ac:parameter ac:name="borderWidth">1</ac:parameter><ac:parameter ac:name="borderStyle">solid</ac:parameter><ac:rich-text-body><p><span style="color:var(--ds-text,#172b4d);">client = SimulationWebClient('http(s)://<span style="color:var(--ds-background-accent-orange-bolder,#c25100);">&lt;server_host&gt;</span>:<span style="color:var(--ds-background-accent-orange-bolder,#c25100);">&lt;server_port&gt;</span>',<span> </span></span><span style="color:var(--ds-text,#172b4d);">'<span style="color:var(--ds-background-accent-orange-bolder,#c25100);">&lt;username&gt;</span>', '<span style="color:var(--ds-background-accent-orange-bolder,#c25100);">&lt;password&gt;</span>', <span style="color:var(--ds-text,#172b4d);">'<span style="color:var(--ds-background-accent-orange-bolder,#c25100);">&lt;token&gt;</span>',</span> False)</span></p></ac:rich-text-body></ac:structured-macro><p>This request starts a work session and provides authentication to Teamwork Cloud.</p><p>The following table describes the parameters used in the request:</p><table class="wrapped"><colgroup><col /><col /><col /><col /></colgroup><tbody><tr><th>Parameter</th><th>In</th><th>Required or optional</th><th>Description</th></tr><tr><td><strong>server_host</strong></td><td>path</td><td>required</td><td>The Teamwork Cloud server host name.</td></tr><tr><td><strong>server_port</strong></td><td>path</td><td>required</td><td>The Teamwork Cloud server port.</td></tr><tr><td><strong>username</strong></td><td>path</td><td>optional</td><td><p><span style="color:var(--ds-text,#172b4d);">The Teamwork Cloud user name. </span><span style="color:var(--ds-text,#172b4d);">If you do not specify the user name in the request, an input field will be provided to specify it later.</span></p></td></tr><tr><td><p><strong>password</strong></p></td><td>path</td><td>optional</td><td><span style="color:var(--ds-text,#172b4d);">The Teamwork Cloud password. </span><span style="color:var(--ds-text,#172b4d);">If you do not specify the password in the request, an input field will be provided to specify it later.</span></td></tr><tr><td><p><strong>token</strong></p></td><td>path</td><td>optional</td><td><span style="color:var(--ds-text,#172b4d);">The Teamwork Cloud token. You can either <span style="color:var(--ds-text,#172b4d);">provide a username/password or a token. To learn more about generating a token, click <ac:link><ri:page ri:space-key="MCS" ri:content-title="Generating a personal access token" /><ac:plain-text-link-body><![CDATA[here]]></ac:plain-text-link-body></ac:link>.</span></span></td></tr></tbody></table><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="6a412d3a-f998-48f0-994d-7c7f6b068a35"><ac:rich-text-body><p>For instructions on how to run server-side simulation using SSL, refer to <ac:link><ri:page ri:content-title="Running server-side simulation with SSL" /></ac:link></p></ac:rich-text-body></ac:structured-macro><h3>Get the list of Teamwork Cloud projects</h3><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="aba79bdf-8e47-412b-8fcf-9fde0f8e51fa"><ac:parameter ac:name="borderColor">lightgrey</ac:parameter><ac:parameter ac:name="borderWidth">1</ac:parameter><ac:parameter ac:name="borderStyle">solid</ac:parameter><ac:rich-text-body><p>client.get_projects()</p></ac:rich-text-body></ac:structured-macro><p><span style="color:var(--ds-text,#333333);">This request provides the list of Teamwork Cloud projects accessible to you depending on your permissions. Only projects that you can read (the Read Resources permission) are returned.<br /></span></p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="61c559d6-d351-4fb8-833d-76f36b1b42e9"><ac:parameter ac:name="title">Request and response examples</ac:parameter><ac:plain-text-body><![CDATA[client.get_projects()


[{'id': '1f9fd988-620b-4b3c-8414-7ab96dc53a48',
  'name': 'SpacecraftMassRollup',
  'description': ''},
 {'id': 'c125b91e-7d31-4015-b659-6fd98059b8c7',
  'name': 'BouncingBall',
  'description': 'This project demonstrates the execution of the BouncingBall, including fmu.'},
 {'id': '485dfc82-7b08-43cd-86b1-953b3725e5b1',
  'name': 'CarBrakingAnalysis',
  'description': 'This project calculates the stopping distance based on car speed and mass.'}]]]></ac:plain-text-body></ac:structured-macro><h3>Run simulation</h3><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="cffa5aa1-1a65-49db-90e6-71d6ab2d17c5"><ac:parameter ac:name="borderColor">lightgrey</ac:parameter><ac:parameter ac:name="borderWidth">1</ac:parameter><ac:parameter ac:name="borderStyle">solid</ac:parameter><ac:rich-text-body><p>client.run(<span style="color:var(--ds-background-accent-orange-bolder,#c25100);">&lt;project&gt;</span>, version=<span style="color:var(--ds-background-accent-orange-bolder,#c25100);">&lt;version&gt;</span>, branch=<span style="color:var(--ds-background-accent-orange-bolder,#c25100);">&lt;branch&gt;</span>, element=<span style="color:var(--ds-background-accent-orange-bolder,#c25100);">&lt;element&gt;</span>, config=<span style="color:var(--ds-background-accent-orange-bolder,#c25100);">&lt;config&gt;</span>, started_from=<span style="color:var(--ds-background-accent-orange-bolder,#c25100);">&lt;starting location&gt;</span>, commit_results=<span style="color:var(--ds-background-accent-orange-bolder,#c25100);">&lt;True/False&gt;</span>, verification=<span style="color:var(--ds-background-accent-orange-bolder,#c25100);">&lt;All/None/Fail&gt;</span>, data=json.dumps(<span style="color:var(--ds-background-accent-orange-bolder,#c25100);">&lt;param&gt;</span> ),<strong> </strong>timeout=<span style="color:var(--ds-background-accent-orange-bolder,#c25100);">&lt;timeout duration&gt;</span>, sync=<span style="color:var(--ds-background-accent-orange-bolder,#c25100);">&lt;True/False&gt;</span>)</p></ac:rich-text-body></ac:structured-macro><p>This request initiates the execution of the specified Simulation Configuration in a particular project. It connects to Teamwork Cloud, finds the element to execute, and initiates the execution if the element exists. After the execution is complete, the request constructs and returns a unique ID (per application) for the given execution.</p><p>The following table describes the parameters used in the request:</p><table class="relative-table wrapped" style="width: 100.0%;"><colgroup><col style="width: 6.64105%;" /><col style="width: 5.26894%;" /><col style="width: 4.39078%;" /><col style="width: 54.0066%;" /><col style="width: 29.6378%;" /></colgroup><tbody><tr><th>Parameter</th><th>In</th><th>Required or optional</th><th>Description</th><th>Options</th></tr><tr><td><strong>project</strong></td><td>path</td><td>required</td><td>The Teamwork Cloud project name or ID.</td><td>NA</td></tr><tr><td><strong>version</strong></td><td>path</td><td>optional</td><td>The Teamwork Cloud project version.</td><td>NA</td></tr><tr><td><strong>branch</strong></td><td>path</td><td>optional</td><td>The project branch name or ID. If the branch is omitted, the trunk is used instead.</td><td>NA</td></tr><tr><td><strong>element</strong></td><td>path</td><td>optional</td><td><span style="color:var(--ds-text,#172b4d);">The qualified name or server ID of the element to be executed.</span></td><td>NA</td></tr><tr><td><strong>config</strong></td><td>path</td><td>optional</td><td>The Simulation Configuration name or server ID.</td><td>NA</td></tr><tr><td><strong>started_from</strong></td><td>path</td><td>optional</td><td><span style="color:var(--ds-text,#172b4d);">Allows specifying the starting location of the simulation. The value of the<span> </span></span><strong style="text-align: left;">started_from</strong><span style="color:var(--ds-text,#172b4d);"> parameter is provided in the status endpoint response.</span></td><td>NA</td></tr><tr><td><strong> <span style="color:var(--ds-text,#333333);">commit_results</span> </strong></td><td>path</td><td>optional</td><td><p>Commits a new project version with the simulation results. Available values are <em>True</em> or <em>False</em> (default).</p></td><td>NA</td></tr><tr><td><strong>verification</strong></td><td>path</td><td>optional</td><td><p>Returns the selected verification results. Available values are:</p><ul><li style="list-style-type: none;background-image: none;"><ul><li><strong>All</strong> - all verification results are returned.</li><li><strong>None</strong> - no verification results are returned.</li><li><strong>Fail</strong> (default) - verification results with the fail status are returned.</li></ul></li></ul></td><td>NA</td></tr><tr><td><strong>data</strong></td><td>path</td><td>optional</td><td>A set of output parameters, which will be obtained after the simulation is complete.</td><td>NA</td></tr><tr><td><p><strong style="text-align: left;">timeout</strong></p></td><td>path</td><td>optional</td><td><p>Allows specifying the timeout duration in minutes. If the <strong>timeout</strong> parameter is not provided, the <strong>sim.timeout.min</strong> property will be taken from the webappplatform.properties instead.</p></td><td>NA</td></tr><tr><td><p><strong style="text-align: left;">sync</strong></p></td><td>path</td><td>optional</td><td><p>Initiates a synchronous API call. If the <strong>sync</strong> is set to 'True', the call will return when it is completed. Available values are <em>True</em> or <em>False</em> (default).</p></td><td>NA</td></tr><tr><td><strong style="text-align: left;">simconfig</strong><span style="color:var(--ds-text,#172b4d);"><span> </span></span></td><td>body</td><td>optional</td><td><span style="color:var(--ds-text,#172b4d);">The set of simulation configuration properties along with their corresponding values. The simulation configuration options you specify will take precedence over the initial configuration option from a model.</span></td><td><ul style="text-align: left;"><li>&quot;ALLOW_CONCURRENT_ALLOCATED_ACTIVITIES&quot;: true,</li><li>&quot;AUTOMATIC_PARAMETRIC_RECALCULATION&quot;: true,</li><li>&quot;AUTO_CONVERT_UNITS&quot;: true,</li><li>&quot;AUTO_CREATE_FUML_OBJECT_OF_OUTPUT_PIN&quot;: true,</li><li>&quot;AUTO_START&quot;: true,</li><li>&quot;AUTO_START_ACTIVE_OPTIONS&quot;: true,</li><li>&quot;AUTO_TERMINATE&quot;: true,</li><li>&quot;CLOCK_RATIO&quot;: 1,</li><li>&quot;CLONE_REFERENCES&quot;: true,</li><li>&quot;COMPLETION_EVENTS_AND_TRANSITIONS&quot;: true,</li><li>&quot;CONSTRAINT_FAILURE_AS_BREAKPOINT&quot;: true,</li><li>&quot;DECIMAL_PLACES&quot;: 4,</li><li>&quot;DEFAULT_LANGUAGE&quot;: &quot;JavaScript Rhino&quot;,</li><li>&quot;DURATION_SIMULATION_MODE&quot;: &quot;MIN&quot;, // possible values: MIN, MAX, AVERAGE, RANDOM</li><li>&quot;ENDTIME&quot;: 0,</li><li>&quot;ENGINES_PRIORITY&quot;: &quot;<span class="error">[on]</span><span> </span>fUML Engine\n<span class="error">[on]</span><span> </span>Interaction Engine\n<span class="error">[on]</span><span> </span>SCXML Engine&quot;,</li><li>&quot;INITIALIZE_NUMERICAL_VALUE&quot;: false,</li><li>&quot;INITIALIZE_REFERENCES&quot;: true,</li><li>&quot;NUMBER_OF_RUNS&quot;: 0,</li><li>&quot;NUMBER_OF_STEPS&quot;: 0,</li><li>&quot;PASS_CALLER_CONTEXT&quot;: true,</li><li>&quot;RECORD_TIMESTAMP&quot;: false,</li><li>&quot;REMEMBER_FAILURE_STATUS&quot;: true,</li><li>&quot;RESULT_LOCATION&quot;: &quot;Results&quot;,</li><li>&quot;RUN_FORKS_IN_PARALLEL&quot;: true,</li><li>&quot;SOLVE_AFTER_INITIALIZATION&quot;: true,</li><li>&quot;START_TIME&quot;: 0,</li><li>&quot;STATE_ACTIVATION_SEMANTICS&quot;: &quot;BEFORE_ENTRY&quot;, // possible values: &quot;BEFORE_ENTRY&quot;, &quot;AFTER_ENTRY&quot;</li><li>&quot;STEP_DELAY&quot;: 0,</li><li>&quot;STEP_SIZE&quot;: 0,</li><li>&quot;TERMINATE_BEHAVIOR_ON_EXCEPTION_THROWN&quot;: true,</li><li>&quot;TERMINATE_NESTED_BEHAVIORS&quot;: true,</li><li>&quot;TERMINATE_STREAMING_BEHAVIORS_BY_OUTPUT_PARAMETER_MULTIPLICITY&quot;: false,</li><li>&quot;TIME_UNIT&quot;: &quot;MILLISECOND&quot;,</li><li>&quot;TIME_VALUE&quot;: &quot;Model-based Clock Test::Clock::time&quot;,</li><li>&quot;TIME_VARIABLE_NAME&quot;: &quot;simtime&quot;,</li><li>&quot;TREAT_ALL_CLASSIFIERS_AS_ACTIVE&quot;: true,</li><li>&quot;USE_FUML_DECISION_SEMANTICS&quot;: false</li></ul></td></tr></tbody></table><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="4844b2ed-f359-4509-8a87-f8ea12cd7d42"><ac:parameter ac:name="title">Request and response examples</ac:parameter><ac:plain-text-body><![CDATA[ # SpaceCraftMassRollup sample

parameters = {
    "inputs":
   {
       "telecom.antenna.me":10,
        "telecom.amplifier.me":20
   },
 "outputs": 
    [ 
        "me",
        "propulsion.me",
        "propulsion.tank.me",
        "propulsion.thruster.me",
        "telecom.me",
        "telecom.antenna.me",
        "telecom.amplifier.me"
    ] 
}
        
client.run('SpacecraftMassRollup_SimWeb', config='spacecraft mass analysis', commit_results=False, data=json.dumps(parameters))]]></ac:plain-text-body></ac:structured-macro><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="4c20dc01-0688-45ef-9fe7-6b70ecbe62ed"><ac:parameter ac:name="title">Request example with simulation options specified in a request body</ac:parameter><ac:plain-text-body><![CDATA[from pyST import simconfig   // imports simulation configuration class that allows using autocompletion to specify simulation options

simOptions = {
"simconfig":
   {
        simconfig.AUTO_START: True,
        simconfig.DURATION_SIMULATION_MODE: "MIN",
        simconfig.ENDTIME: 50,
        simconfig.TERMINATE_NESTED_BEHAVIORS: False
   }
}
 

client.run('OntologicalBehaviorModeling', config='Ontological Configurable', data=json.dumps(simOptions))]]></ac:plain-text-body></ac:structured-macro><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="a4ef8f60-dabf-4101-8449-f8b533102bba"><ac:rich-text-body><p><span style="color:var(--ds-text,#172b4d);">To enable the autocompletion option for specifying the simulation in Jupyter, use </span><strong>from pyST import simconfig</strong></p><p><strong><ac:image><ri:attachment ri:filename="Jupyter.png" /></ac:image></strong></p></ac:rich-text-body></ac:structured-macro><h3 class="auto-cursor-target">Perform a time step</h3><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="cfd4167a-0def-4f2a-864e-dfbf9f97a8e6"><ac:parameter ac:name="borderColor">lightgrey</ac:parameter><ac:parameter ac:name="borderWidth">1</ac:parameter><ac:rich-text-body><p>client.step(<span style="color:var(--ds-background-accent-orange-bolder,#c25100);">&lt;simulation_id&gt;<span style="color:var(--ds-text,#333333);">, sync=</span>&lt;True/False&gt;</span>)</p></ac:rich-text-body></ac:structured-macro><p><span style="color:var(--ds-text,#333333);">This request performs a single time step of the specified simulation. To run the simulation by step, it should be run with the</span> <strong>AUTO_START</strong><span style="color:var(--ds-text,#333333);"><span> </span>option of the simconfig parameter set to<span> </span></span><em>false</em><span style="color:var(--ds-text,#333333);">.</span></p><p>The following table describes the parameters used in the request:</p><table class="relative-table wrapped" style="width: 78.113%;"><colgroup><col style="width: 15.6711%;" /><col style="width: 9.27618%;" /><col style="width: 15.9522%;" /><col style="width: 59.1005%;" /></colgroup><tbody><tr><th>Parameter</th><th>In</th><th>Required or optional</th><th>Description</th></tr><tr><td><strong>simulation_id</strong></td><td>path</td><td><span style="color:var(--ds-text,#172b4d);">optional</span></td><td><div class="content-wrapper"><p class="auto-cursor-target">The ID of a specific simulation.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="5b29eb73-8bdc-4d04-a515-daa4ac7127a7"><ac:rich-text-body><p>If the<span> </span><strong>simulation_id</strong><span> </span>is not specified, the pyST client will use the<span> </span><strong>simulation_id</strong><span> </span>of the last simulation run.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></div></td></tr><tr><td><strong>sync</strong></td><td>path</td><td>optional</td><td><p>Initiates a synchronous API call. If the <strong>sync</strong> is set to 'True', the call will return when it is completed. Available values are <em>True</em> or <em>False</em> (default).</p></td></tr></tbody></table><h3>Start simulation</h3><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="0a954e32-9014-48ec-a77b-091e69e3ff85"><ac:parameter ac:name="borderColor">lightgrey</ac:parameter><ac:parameter ac:name="borderWidth">1</ac:parameter><ac:rich-text-body><p>client.start(<span style="color:var(--ds-background-accent-orange-bolder,#c25100);">&lt;simulation_id&gt;</span>)</p></ac:rich-text-body></ac:structured-macro><p><span style="color:var(--ds-text,#333333);">This request starts the execution of the specified simulation. </span> <span style="color:var(--ds-text,#333333);">If the initialization phase is still in progress, the start </span> <span style="color:var(--ds-text,#333333);">endpoint is memorized and sent when the initialization phase is completed.</span></p><p>The following table describes the parameters used in the request:</p><table class="relative-table wrapped" style="width: 77.7839%;"><colgroup> <col style="width: 15.808%;" /> <col style="width: 9.31546%;" /> <col style="width: 16.0198%;" /> <col style="width: 58.8567%;" /> </colgroup><tbody><tr><th>Parameter</th><th>In</th><th>Required or optional</th><th colspan="1">Description</th></tr><tr><td><strong>simulation_id</strong></td><td>path</td><td><span style="color:var(--ds-text,#172b4d);">optional</span></td><td colspan="1"><div class="content-wrapper"><p class="auto-cursor-target">The ID of a specific simulation.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="67cdf141-6393-4b3e-9cb1-fa9c4e10a711"><ac:rich-text-body><p>If the<span> </span><strong>simulation_id</strong><span> </span>is not specified, the pyST client will use the<span> </span><strong>simulation_id</strong><span> </span>of the last simulation run.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></div></td></tr></tbody></table><h3>Start simulation and get results</h3><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="c0fe21ad-1e85-458b-944d-51225d4e9ec6"><ac:parameter ac:name="borderColor">lightgrey</ac:parameter><ac:parameter ac:name="borderWidth">1</ac:parameter><ac:parameter ac:name="borderStyle">solid</ac:parameter><ac:rich-text-body><p>client.simulate(<span style="color:var(--ds-background-accent-orange-bolder,#c25100);">&lt;project&gt;</span>, version=<span style="color:var(--ds-background-accent-orange-bolder,#c25100);">&lt;version&gt;</span>, branch=<span style="color:var(--ds-background-accent-orange-bolder,#c25100);">&lt;branch&gt;</span>, element=<span style="color:var(--ds-background-accent-orange-bolder,#c25100);">&lt;element&gt;</span>, config=<span style="color:var(--ds-background-accent-orange-bolder,#c25100);">&lt;config&gt;</span>, commit_results=<span style="color:var(--ds-background-accent-orange-bolder,#c25100);">&lt;True/False&gt;</span>, verification=<span style="color:var(--ds-background-accent-orange-bolder,#c25100);">&lt;All/None/Fail&gt;</span>, data=json.dumps(<span style="color:var(--ds-background-accent-orange-bolder,#c25100);">&lt;param&gt;</span>))</p></ac:rich-text-body></ac:structured-macro><p>This request starts a simulation and returns its results.</p><p>The following table describes the parameters used in the request:</p><table class="relative-table wrapped" style="width: 100.0%;"><colgroup><col style="width: 6.64105%;" /><col style="width: 5.32382%;" /><col style="width: 7.35456%;" /><col style="width: 51.0428%;" /><col style="width: 29.6378%;" /></colgroup><tbody><tr><th>Parameter</th><th>In</th><th>Required or optional</th><th colspan="1">Description</th><th colspan="1">Options</th></tr><tr><td><strong>project</strong></td><td>path</td><td>required</td><td colspan="1">The Teamwork Cloud project name or ID.</td><td colspan="1">NA</td></tr><tr><td colspan="1"><strong>version</strong></td><td colspan="1">path</td><td colspan="1">optional</td><td colspan="1">The Teamwork Cloud project version.</td><td colspan="1">NA</td></tr><tr><td><strong>branch</strong></td><td>path</td><td>optional</td><td colspan="1">The project branch name or ID. If the branch is omitted, the trunk is used instead.</td><td colspan="1">NA</td></tr><tr><td><strong>element</strong></td><td>path</td><td>optional</td><td colspan="1"><span style="color:var(--ds-text,#172b4d);">The qualified name or server ID of the element to be executed.</span></td><td colspan="1">NA</td></tr><tr><td><strong>config</strong></td><td>path</td><td>optional</td><td colspan="1">The Simulation Configuration name or server ID.</td><td colspan="1">NA</td></tr><tr><td colspan="1"><strong> <span style="color:var(--ds-text,#333333);">commit_results</span> </strong></td><td colspan="1">path</td><td colspan="1">optional</td><td colspan="1"><p>A new project version is committed with the simulation results. Available values are <em>True</em> or <em>False</em> (default).</p></td><td colspan="1">NA</td></tr><tr><td colspan="1"><strong>verification</strong></td><td colspan="1">path</td><td colspan="1">optional</td><td colspan="1"><p>Returns the selected verification results. Available values are:</p><ul><li style="list-style-type: none;background-image: none;"><ul><li><strong>All</strong> - all verification results are returned.</li><li><strong>None</strong> - no verification results are returned.</li><li><strong>Fail</strong> - verification results with the fail status are returned including the main status and the status of requirements and constraints.</li></ul></li></ul><p>If the <strong>verification</strong> value is not specified, only the verification results with the fail status are returned when the get_results endpoint is called.</p></td><td colspan="1">NA</td></tr><tr><td colspan="1"><strong>data</strong></td><td colspan="1">path</td><td colspan="1">optional</td><td colspan="1">A set of output parameters, which will be obtained after the simulation is complete.</td><td colspan="1">NA</td></tr><tr><td colspan="1"><strong style="text-align: left;">simconfig</strong><span style="color:var(--ds-text,#172b4d);"><span> </span></span></td><td colspan="1">body</td><td colspan="1">optional</td><td colspan="1"><span style="color:var(--ds-text,#172b4d);">The set of simulation configuration properties along with their corresponding values. The simulation configuration options you specify will take precedence over the initial configuration option from a model.</span></td><td colspan="1"><ul><li>&quot;ALLOW_CONCURRENT_ALLOCATED_ACTIVITIES&quot;: true,</li><li data-uuid="31367d9c-c243-4c30-832c-5aa758ae6dd7"><span style="color:var(--ds-text,#172b4d);">&quot;ANIMATION_SPEED&quot;: 95,</span></li><li>&quot;AUTOMATIC_PARAMETRIC_RECALCULATION&quot;: true,</li><li>&quot;AUTO_CONVERT_UNITS&quot;: true,</li><li>&quot;AUTO_CREATE_FUML_OBJECT_OF_OUTPUT_PIN&quot;: true,</li><li>&quot;AUTO_START&quot;: true,</li><li>&quot;AUTO_START_ACTIVE_OPTIONS&quot;: true,</li><li>&quot;AUTO_TERMINATE&quot;: true,</li><li data-uuid="361f752d-86f8-4bbc-84e2-7601cee29f85">&quot;<span style="color:var(--ds-text,#172b4d);">CAPTURE_TIMESTAMP</span>&quot;: false,</li><li>&quot;CLOCK_RATIO&quot;: 1,</li><li>&quot;CLONE_REFERENCES&quot;: true,</li><li>&quot;COMPLETION_EVENTS_AND_TRANSITIONS&quot;: true,</li><li>&quot;CONSTRAINT_FAILURE_AS_BREAKPOINT&quot;: true,</li><li>&quot;DECIMAL_PLACES&quot;: 4,</li><li>&quot;DEFAULT_LANGUAGE&quot;: &quot;JavaScript Rhino&quot;,</li><li>&quot;DURATION_SIMULATION_MODE&quot;: &quot;MIN&quot;, // possible values: MIN, MAX, AVERAGE, RANDOM</li><li>&quot;ENDTIME&quot;: 0,</li><li>&quot;ENGINES_PRIORITY&quot;: &quot;<span class="error">[on]</span><span> </span>fUML Engine\n<span class="error">[on]</span><span> </span>Interaction Engine\n<span class="error">[on]</span><span> </span>SCXML Engine&quot;,</li><li>&quot;INITIALIZE_NUMERICAL_VALUE&quot;: false,</li><li>&quot;INITIALIZE_REFERENCES&quot;: true,</li><li>&quot;NUMBER_OF_RUNS&quot;: 0,</li><li>&quot;NUMBER_OF_STEPS&quot;: 0,</li><li>&quot;PASS_CALLER_CONTEXT&quot;: true,</li><li>&quot;RECORD_TIMESTAMP&quot;: false,</li><li>&quot;REMEMBER_FAILURE_STATUS&quot;: true,</li><li>&quot;RESULT_LOCATION&quot;: &quot;Results&quot;,</li><li>&quot;RUN_FORKS_IN_PARALLEL&quot;: true,</li><li data-uuid="c8d255fa-aa51-4abe-b05d-239ac0de9cf6">&quot;<span style="color:var(--ds-text,#172b4d);">SHOW_ANNOTATIONS</span>&quot;: false,</li><li>&quot;SOLVE_AFTER_INITIALIZATION&quot;: true,</li><li>&quot;START_TIME&quot;: 0,</li><li>&quot;STATE_ACTIVATION_SEMANTICS&quot;: &quot;BEFORE_ENTRY&quot;, // possible values: &quot;BEFORE_ENTRY&quot;, &quot;AFTER_ENTRY&quot;</li><li>&quot;STEP_DELAY&quot;: 0,</li><li>&quot;STEP_SIZE&quot;: 0,</li><li>&quot;TERMINATE_BEHAVIOR_ON_EXCEPTION_THROWN&quot;: true,</li><li>&quot;TERMINATE_NESTED_BEHAVIORS&quot;: true,</li><li>&quot;TERMINATE_STREAMING_BEHAVIORS_BY_OUTPUT_PARAMETER_MULTIPLICITY&quot;: false,</li><li>&quot;TIME_UNIT&quot;: &quot;MILLISECOND&quot;,</li><li>&quot;TIME_VALUE&quot;: &quot;Model-based Clock Test::Clock::time&quot;,</li><li>&quot;TIME_VARIABLE_NAME&quot;: &quot;simtime&quot;,</li><li>&quot;TREAT_ALL_CLASSIFIERS_AS_ACTIVE&quot;: true,</li><li>&quot;USE_FUML_DECISION_SEMANTICS&quot;: false</li></ul></td></tr></tbody></table><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="91c406ec-2b16-4dd4-861d-e75499fb21b1"><ac:parameter ac:name="title">Request and response examples</ac:parameter><ac:plain-text-body><![CDATA[ # SpaceCraftMassRollup sample

parameters = {
    "inputs":
   {
       "telecom.antenna.me":10,
        "telecom.amplifier.me":20
   },
 "outputs": 
    [ 
        "me",
        "propulsion.me",
        "propulsion.tank.me",
        "propulsion.thruster.me",
        "telecom.me",
        "telecom.antenna.me",
        "telecom.amplifier.me"
    ] 
}
        
client.simulate('SpacecraftMassRollup_SimWeb', config='spacecraft mass analysis', commit_results=False, data=json.dumps(parameters))]]></ac:plain-text-body></ac:structured-macro><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="e81b05c7-7a17-40a5-acf0-6212a5cc8e0a"><ac:parameter ac:name="title">Request example with simulation options specified in a request body</ac:parameter><ac:plain-text-body><![CDATA[from pyST import simconfig   // imports simulation configuration class that allows using autocompletion to specify simulation options

simOptions = {
"simconfig":
   {
        option.AUTO_START: true,
        option.DURATION_SIMULATION_MODE: "MIN",
        option.ENDTIME: 50,
        option.TERMINATE_NESTED_BEHAVIORS: false
   }
}
 

client.run('OntologicalBehaviorModeling', config='Ontological Configurable', data=json.dumps(simOptions))]]></ac:plain-text-body></ac:structured-macro><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="b8d34ae7-43db-45a9-a7ce-add9d9bd8b25"><ac:rich-text-body><p><span style="color:var(--ds-text,#172b4d);">To enable the autocompletion option for specifying the simulation in Jupyter, use </span><strong>from pyST import simconfig</strong></p><p><strong><ac:image><ri:attachment ri:filename="Jupyter.png" /></ac:image></strong></p></ac:rich-text-body></ac:structured-macro><h3>Get simulation status</h3><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="60fd529d-5ba2-4c29-b67a-e38b01bebef9"><ac:parameter ac:name="borderColor">lightgrey</ac:parameter><ac:parameter ac:name="borderWidth">1</ac:parameter><ac:rich-text-body><p>client.get_status(<span style="color:var(--ds-background-accent-orange-bolder,#c25100);">&lt;simulation_id&gt;</span>)</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target">This request gets the status of a specific simulation. <span style="color:var(--ds-text,#172b4d);">If the model has a<span> </span></span><span style="color:var(--ds-text,#333333);">UI mockup, Time Series Chart</span><span style="color:var(--ds-text,#172b4d);">, Timeline Chart, or HTML Table, you can use the URL provided in the 'ui' or indexUI' key to open the specified UI.</span></p><p>The following table describes the parameters used in the request:</p><table class="relative-table wrapped" style="width: 81.1849%;"><colgroup> <col style="width: 15.1454%;" /> <col style="width: 8.92495%;" /> <col style="width: 15.4158%;" /> <col style="width: 60.5139%;" /> </colgroup><tbody><tr><th>Parameter</th><th>In</th><th>Required or optional</th><th colspan="1">Description</th></tr><tr><td><strong>simulation_id</strong></td><td>path</td><td>optional</td><td colspan="1"><div class="content-wrapper"><p class="auto-cursor-target">The ID of a specific simulation.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="ea04cdf5-ccb1-437f-b399-d8059e8b2284"><ac:rich-text-body><p>If the<span> </span><strong>simulation_id</strong><span> </span>is not specified, the pyST client will use the<span> </span><strong>simulation_id</strong><span> </span>of the last simulation run.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></div></td></tr></tbody></table><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="88359719-df30-4206-abc5-e6153bc5ee1f"><ac:parameter ac:name="title">Request and response examples</ac:parameter><ac:plain-text-body><![CDATA[client.get_status('77d0c496-c1e2-42cd-8ba4-04e4c7f359d3')
 
{'state': 'RUNNING',
 'simulationId': '77d0c496-c1e2-42cd-8ba4-04e4c7f359d3',
 'simulationTime': '0 ms',
 'indexUI': 'http://nm-simulation.dsone.3ds.com/simulation/api/ui/index/77d0c496-c1e2-42cd-8ba4-04e4c7f359d3?pages=Coffee%20Machine.html&pages=Water%20Heating%20Element.html&pages=Wallet.html',
 'project': 'CoffeeMachine',
 'config': 'Coffee Machine',
 'elapsedTime': 0,
 'podName': 'simulation-deployment-6989d5dfc9-r6llk',
 'ui': ['http://nm-simulation.dsone.3ds.com/simulation/api/ui/77d0c496-c1e2-42cd-8ba4-04e4c7f359d3/Coffee%20Machine.html',
  'http://nm-simulation.dsone.3ds.com/simulation/api/ui/77d0c496-c1e2-42cd-8ba4-04e4c7f359d3/Water%20Heating%20Element.html',
  'http://nm-simulation.dsone.3ds.com/simulation/api/ui/77d0c496-c1e2-42cd-8ba4-04e4c7f359d3/Wallet.html']}


client.get_status('ce8c8215-0515-43fd-9d34-92d1d7a95d87')
 
{'state': 'COMPLETED',
 'simulationId': 'ce8c8215-0515-43fd-9d34-92d1d7a95d87',
 'simulationTime': '3000 ms',
 'project': 'SpacecraftMassRollup',
 'config': 'spacecraft mass analysis',
 'elapsedTime': 6598}
 
 
client.get_status('b7bdf933-f58d-4e7e-b73b-8370c60485cd')
 
{'state': 'QUEUED',
 'queueNumber': 3,
 'simulationId': 'b7bdf933-f58d-4e7e-b73b-8370c60485cd',
 'simulationTime': '0 ms',
 'project': 'CarBrakingAnalysis',
 'elapsedTime': 52}]]></ac:plain-text-body></ac:structured-macro><h3 class="auto-cursor-target">Get simulation variables</h3><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="5f054114-792f-40ff-b9a1-0b9bcdbb2b96"><ac:parameter ac:name="borderColor">lightgrey</ac:parameter><ac:parameter ac:name="borderWidth">1</ac:parameter><ac:parameter ac:name="borderStyle">solid</ac:parameter><ac:rich-text-body><p>client.get_variables(<span style="color:var(--ds-background-accent-orange-bolder,#c25100);">&lt;simulation_id&gt;</span>, variables=json.dumps(<span style="color:var(--ds-background-accent-orange-bolder,#c25100);">&lt;parameters&gt;</span>))</p></ac:rich-text-body></ac:structured-macro><p><span style="color:var(--ds-text,#333333);">This request returns a list of simulation variables during simulation.</span></p><p>The following table describes the parameters used in the request:</p><table class="relative-table wrapped" style="width: 80.746%;"><colgroup> <col style="width: 15.8396%;" /> <col style="width: 9.10945%;" /> <col style="width: 15.2277%;" /> <col style="width: 59.8232%;" /> </colgroup><tbody><tr><th>Parameter</th><th>In</th><th>Required or optional</th><th colspan="1">Description</th></tr><tr><td><strong>simulation_id</strong></td><td>path</td><td>optional</td><td colspan="1"><div class="content-wrapper"><p class="auto-cursor-target">The ID of the running simulation.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="4ef1f222-ab95-4769-89f0-5a0476e15384"><ac:rich-text-body><p>If the<span> </span><strong>simulation_id</strong><span> </span>is not specified, the pyST client will use the<span> </span><strong>simulation_id</strong><span> </span>of the last simulation run.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></div></td></tr><tr><td colspan="1"><strong>variables</strong></td><td colspan="1">path</td><td colspan="1">optional</td><td colspan="1"><span style="color:var(--ds-text,#333333);">The set of simulation variables that should be obtained. If no variables are specified, the values of all simulation variables are returned.</span></td></tr></tbody></table><h3>Set simulation variables</h3><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="ae5fd73e-2a0b-41cc-845a-00eefefe93b5"><ac:parameter ac:name="borderColor">lightgrey</ac:parameter><ac:parameter ac:name="borderWidth">1</ac:parameter><ac:parameter ac:name="borderStyle">solid</ac:parameter><ac:rich-text-body><p><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">client.set_variables(&lt;simulation_id&gt;, variables=json.dumps(&lt;parameters&gt;),</span> context=<span style="color:var(--ds-background-accent-orange-bolder,#c25100);">&lt;context ID&gt;, <span style="color:var(--ds-text,#333333);">property_path=</span>&lt;property path&gt;</span>)</p></ac:rich-text-body></ac:structured-macro><p><span style="color:var(--ds-text,#333333);">This request provides a list of simulation variables with values. </span></p><p>The following table describes the parameters used in the request:</p><table class="relative-table wrapped" style="width: 80.6912%;"><colgroup> <col style="width: 15.8503%;" /> <col style="width: 9.11565%;" /> <col style="width: 15.2381%;" /> <col style="width: 59.7959%;" /> </colgroup><tbody><tr><th>Parameter</th><th>In</th><th>Required or optional</th><th colspan="1">Description</th></tr><tr><td><strong>simulation_id</strong></td><td>path</td><td>optional</td><td colspan="1"><div class="content-wrapper"><p class="auto-cursor-target">The ID of the running simulation.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="74b8afa8-5cfa-40a8-b963-4e6562b3f8b0"><ac:rich-text-body><p>If the<span> </span><strong>simulation_id</strong><span> </span>is not specified, the pyST client will use the<span> </span><strong>simulation_id</strong><span> </span>of the last simulation run.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></div></td></tr><tr><td colspan="1"><strong>variables</strong></td><td colspan="1">path</td><td colspan="1">required</td><td colspan="1"><span style="color:var(--ds-text,#333333);">The set of simulation variables with values that should be used during the current simulation.</span></td></tr><tr><td colspan="1"><strong>context</strong></td><td colspan="1">path</td><td colspan="1">optional</td><td colspan="1">The context ID.</td></tr><tr><td colspan="1"><strong>property_path</strong></td><td colspan="1">path</td><td colspan="1">optional</td><td colspan="1">The property path of the context specified using property names or IDs.</td></tr></tbody></table><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="5e9885bd-f52e-4c43-9823-737554959864"><ac:parameter ac:name="title">Request and response examples</ac:parameter><ac:plain-text-body><![CDATA[var = {
 "variables":
 {
 "position": 40
 }
}

client.set_variables('23ceff24-28fa-47e4-b29f-b6b60b4b12e3', variables=json.dumps(var))]]></ac:plain-text-body></ac:structured-macro><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="1459c7ec-4583-4b9b-90ab-bb923d14ffb6"><ac:parameter ac:name="title">Alternative method to set a single simulation variable</ac:parameter><ac:rich-text-body><p><br />A simplified <strong>Set Simulation Variable</strong> method can be used when setting a single value, which does not require constructing a JSON.</p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="43c7fd4a-e8f0-4ef0-8425-0d1afe4974cf"><ac:rich-text-body><p>client.set_variable(&lt;name&gt;, &lt;value&gt;, &lt;simulation_id&gt; (optional), &lt;context&gt; (optional), &lt;propertyPath&gt; (optional)). </p></ac:rich-text-body></ac:structured-macro><p>For example, set_variable(name=&quot;mass&quot;, value=100, propertyPath = &quot;car.engine&quot;).</p><p>You can also omit parameter names if the parameters are in the correct sequence, for example, client.set_variable(&quot;mass&quot;, 100).</p></ac:rich-text-body></ac:structured-macro><h3>Pause simulation</h3><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="78ce9449-914a-4df6-8285-dbfc5220448b"><ac:parameter ac:name="borderColor">lightgrey</ac:parameter><ac:parameter ac:name="borderWidth">1</ac:parameter><ac:parameter ac:name="borderStyle">solid</ac:parameter><ac:rich-text-body><p>client.pause(<span style="color:var(--ds-background-accent-orange-bolder,#c25100);">&lt;simulation_id&gt;</span>)</p></ac:rich-text-body></ac:structured-macro><p>This request <span style="color:var(--ds-text,#172b4d);">pauses the execution of the specified simulation.</span></p><p>The following table describes the parameters used in the REST API request:</p><table class="relative-table wrapped" style="width: 80.362%;"><colgroup><col style="width: 15.9836%;" /><col style="width: 9.15301%;" /><col style="width: 15.3005%;" /><col style="width: 59.5628%;" /></colgroup><tbody><tr><th>Parameter</th><th>In</th><th>Required or optional</th><th colspan="1">Description</th></tr><tr><td><strong>simulation_id</strong></td><td>path</td><td>optional</td><td colspan="1"><div class="content-wrapper"><p class="auto-cursor-target">The ID of the running simulation.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="9a2ae5ab-ab7c-4952-bc53-2b0126d648df"><ac:rich-text-body><p>If the<span> </span><strong>simulation_id</strong><span> </span>is not specified, the pyST client will use the<span> </span><strong>simulation_id</strong><span> </span>of the last simulation run.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></div></td></tr></tbody></table><h3>Resume simulation</h3><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="0f2007e1-18da-427c-a387-aac78989a3c3"><ac:parameter ac:name="borderColor">lightgrey</ac:parameter><ac:parameter ac:name="borderWidth">1</ac:parameter><ac:parameter ac:name="borderStyle">solid</ac:parameter><ac:rich-text-body><p>client.resume(<span style="color:var(--ds-background-accent-orange-bolder,#c25100);">&lt;simulation_id&gt;</span>)</p></ac:rich-text-body></ac:structured-macro><p><span style="color:var(--ds-text,#172b4d);">This request resumes the execution of the specified simulation.</span></p><p>The following table describes the parameters used in the REST API request:</p><table class="relative-table wrapped" style="width: 80.362%;"><colgroup><col style="width: 15.9836%;" /><col style="width: 9.15301%;" /><col style="width: 15.3005%;" /><col style="width: 59.5628%;" /></colgroup><tbody><tr><th>Parameter</th><th>In</th><th>Required or optional</th><th colspan="1">Description</th></tr><tr><td><strong>simulation_id</strong></td><td>path</td><td>optional</td><td colspan="1"><div class="content-wrapper"><p class="auto-cursor-target">The ID of the running simulation.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="da282b0b-da54-49e4-9fa3-a89eae177b20"><ac:rich-text-body><p>If the<span> </span><strong>simulation_id</strong><span> </span>is not specified, the pyST client will use the<span> </span><strong>simulation_id</strong><span> </span>of the last simulation run.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></div></td></tr></tbody></table><h3>Get simulation results</h3><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="834c8512-af83-4faa-b0d9-06c1d29b5050"><ac:parameter ac:name="borderColor">lightgrey</ac:parameter><ac:parameter ac:name="borderWidth">1</ac:parameter><ac:parameter ac:name="borderStyle">solid</ac:parameter><ac:rich-text-body><p>client.get_result(<span style="color:var(--ds-background-accent-orange-bolder,#c25100);">&lt;simulation_id&gt;</span>)</p></ac:rich-text-body></ac:structured-macro><p>This request returns the results of the specified simulation. If the <strong>OutputParameters</strong> tag of the executed Simulation Configuration is specified, the results are provided according to the <strong>OutputParameters</strong> tag value. I<span style="color:var(--ds-text,#172b4d);">f a Time Series or Timeline chart is specified for the Simulation Configuration, the chart data is returned in the JSON format.</span></p><p><span style="color:var(--ds-text,#333333);">The figure below demonstrates how to specify input and output parameters.</span></p><p><br /></p><p><ac:image ac:align="center"><ri:attachment ri:filename="specifying_input_output_parameters.png" /></ac:image></p><h6 style="text-align: center;">Specifying input and output parameters.</h6><p>The following table describes the parameters used in the request:</p><table class="relative-table wrapped" style="width: 80.362%;"><colgroup> <col style="width: 15.9836%;" /> <col style="width: 9.15301%;" /> <col style="width: 15.3005%;" /> <col style="width: 59.5628%;" /> </colgroup><tbody><tr><th>Parameter</th><th><strong>In</strong></th><th><strong>Required or optional</strong></th><th colspan="1"><strong>Description</strong></th></tr><tr><td><strong>simulation_id</strong></td><td>path</td><td>optional</td><td colspan="1"><div class="content-wrapper"><p class="auto-cursor-target">The ID of the running simulation.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="7d02c713-4503-4d5a-8fdf-41bb8b14f3a6"><ac:rich-text-body><p>If the<span> </span><strong>simulation_id</strong><span> </span>is not specified, the pyST client will use the<span> </span><strong>simulation_id</strong><span> </span>of the last simulation run.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></div></td></tr></tbody></table><h3>Get the list of running simulations</h3><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="f48fd9b2-c2cd-4a77-9269-fa90bc0ce769"><ac:parameter ac:name="borderColor">lightgrey</ac:parameter><ac:parameter ac:name="borderWidth">1</ac:parameter><ac:parameter ac:name="borderStyle">solid</ac:parameter><ac:rich-text-body><pre>client.get_running()</pre></ac:rich-text-body></ac:structured-macro><p>This REST API request gets the list of all currently running simulations including the queued simulations that are placed in a waiting line.</p><h3>Terminate simulation</h3><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="10d35be0-4043-4f1c-b234-fa9e02269345"><ac:parameter ac:name="borderColor">lightgrey</ac:parameter><ac:parameter ac:name="borderWidth">1</ac:parameter><ac:parameter ac:name="borderStyle">solid</ac:parameter><ac:rich-text-body><p>client.terminate(<span style="color:var(--ds-background-accent-orange-bolder,#c25100);">&lt;simulation_id&gt;<span style="color:var(--ds-text,#333333);">, sync=</span>&lt;True/False&gt;</span>)</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target">This request terminates the specified simulation.</p><p>The following table describes the parameters used in the request:</p><table class="relative-table wrapped" style="width: 78.4421%;"><colgroup><col style="width: 17.4248%;" /><col style="width: 9.30721%;" /><col style="width: 16.795%;" /><col style="width: 56.4731%;" /></colgroup><tbody><tr><th>Parameter</th><th>In</th><th>Required or optional</th><th>Description</th></tr><tr><td><strong>simulation_id</strong></td><td>path</td><td>optional</td><td><div class="content-wrapper"><p class="auto-cursor-target">The ID of a specific simulation.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="5cb7e33e-75e9-4e84-901a-6723d387b192"><ac:rich-text-body><p>If the<span> </span><strong>simulation_id</strong><span> </span>is not specified, the pyST client will use the<span> </span><strong>simulation_id</strong><span> </span>of the last simulation run.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></div></td></tr><tr><td><strong>sync</strong></td><td>path</td><td>optional</td><td><p>Initiates a synchronous API call. If the <strong>sync</strong> is set to 'True', the call will return when it is completed. Available values are <em>True</em> or <em>False</em> (default).</p></td></tr></tbody></table><h3>Check for Simulation Configurations</h3><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="be5a29fe-f5e9-4026-ac0e-b3ceb34d836f"><ac:parameter ac:name="borderColor">lightgrey</ac:parameter><ac:parameter ac:name="borderWidth">1</ac:parameter><ac:parameter ac:name="borderStyle">solid</ac:parameter><ac:rich-text-body><p>client.has_configurations(<span style="color:var(--ds-background-accent-orange-bolder,#c25100);">&lt;project&gt;</span>, version=<span style="color:var(--ds-background-accent-orange-bolder,#c25100);">&lt;version&gt;</span>, branch=<span style="color:var(--ds-background-accent-orange-bolder,#c25100);">&lt;branch&gt;</span>)</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target">This request checks if the project has any Simulation Configurations.</p><p>The following table describes the parameters used in the request:</p><table class="relative-table wrapped" style="width: 78.2227%;"><colgroup> <col style="width: 17.7544%;" /> <col style="width: 8.07018%;" /> <col style="width: 17.4035%;" /> <col style="width: 56.7719%;" /> </colgroup><tbody><tr><th>Parameter</th><th>In</th><th>Required or optional</th><th colspan="1">Description</th></tr><tr><td><strong>project</strong></td><td>path</td><td>required</td><td colspan="1">The Teamwork Cloud project name or ID.</td></tr><tr><td colspan="1"><strong>version</strong></td><td colspan="1">path</td><td colspan="1">optional</td><td colspan="1">The Teamwork Cloud project version.</td></tr><tr><td><strong>branch</strong></td><td>path</td><td>optional</td><td colspan="1">The project branch name or ID. If the branch is omitted, the trunk is used instead.</td></tr></tbody></table><h3>Get Simulation Configurations</h3><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="6976f825-9a6a-4be0-9d1f-826331173230"><ac:parameter ac:name="borderColor">lightgrey</ac:parameter><ac:parameter ac:name="borderWidth">1</ac:parameter><ac:parameter ac:name="borderStyle">solid</ac:parameter><ac:rich-text-body><p>client.get_configurations(<span style="color:var(--ds-background-accent-orange-bolder,#c25100);">&lt;project&gt;</span>, version=<span style="color:var(--ds-background-accent-orange-bolder,#c25100);">&lt;version&gt;</span>, branch=<span style="color:var(--ds-background-accent-orange-bolder,#c25100);">&lt;branch&gt;</span>, element=<span style="color:var(--ds-background-accent-orange-bolder,#c25100);">&lt;element&gt;<span style="color:var(--ds-text,#333333);">, filter=</span>&lt;ui&gt;</span>)</p></ac:rich-text-body></ac:structured-macro><p>This request retrieves the names and descriptions of the Simulation Configurations available for the given project.</p><p>The following table describes the parameters used in the request:</p><table class="relative-table wrapped" style="width: 77.3999%;"><colgroup> <col style="width: 17.6596%;" /> <col style="width: 9.57447%;" /> <col style="width: 17.305%;" /> <col style="width: 55.461%;" /> </colgroup><tbody><tr><th>Parameter</th><th>In</th><th>Required or optional</th><th colspan="1">Description</th></tr><tr><td><strong>project</strong></td><td>path</td><td>required</td><td colspan="1">The Teamwork Cloud project name or ID.</td></tr><tr><td colspan="1"><strong>version</strong></td><td colspan="1">path</td><td colspan="1">optional</td><td colspan="1">The Teamwork Cloud project version.</td></tr><tr><td><strong>branch</strong></td><td>path</td><td>optional</td><td colspan="1">The project branch name or ID. If the branch is omitted, the trunk is used instead.</td></tr><tr><td colspan="1"><strong>element</strong></td><td colspan="1">path</td><td colspan="1">optional</td><td colspan="1"><span style="color:var(--ds-text,#172b4d);">The qualified name or server ID of the element to be executed.</span></td></tr><tr><td colspan="1"><strong>filter</strong></td><td colspan="1">path</td><td colspan="1">optional</td><td colspan="1"><p><span style="color:var(--ds-text,#172b4d);">Returns Simulations Configurations with a specified UI tag for a particular project. The only possible value for the<span> </span><strong>filter</strong><span> </span>parameter is<span> </span><strong>ui</strong>.</span></p><p><span style="color:var(--ds-text,#172b4d);">Only Simulations Configurations having at least one of the following UI elements are returned:</span></p><ul><li><span style="color:var(--ds-text,#172b4d);">Frame</span></li><li><span style="color:var(--ds-text,#172b4d);">Table</span></li><li><span style="color:var(--ds-text,#172b4d);">TimeSeries chart</span></li><li><span style="color:var(--ds-text,#172b4d);">Timeline chart</span></li></ul></td></tr></tbody></table><h3 class="auto-cursor-target">Get Simulation Configuration descriptor</h3><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="1749b4f0-e46b-4e24-8e97-5a687cc81b9d"><ac:parameter ac:name="borderColor">lightgrey</ac:parameter><ac:parameter ac:name="borderWidth">1</ac:parameter><ac:parameter ac:name="borderStyle">solid</ac:parameter><ac:rich-text-body><p>client.get_descriptor(<span style="color:var(--ds-background-accent-orange-bolder,#c25100);">&lt;project&gt;</span>, version=<span style="color:var(--ds-background-accent-orange-bolder,#c25100);">&lt;version&gt;</span>, branch=<span style="color:var(--ds-background-accent-orange-bolder,#c25100);">&lt;branch&gt;</span>, config=<span style="color:var(--ds-background-accent-orange-bolder,#c25100);">&lt;config&gt;</span>)</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><span style="color:var(--ds-text,#333333);"><span style="color:var(--ds-text,#172b4d);">This REST API request retrieves Simulation Configuration data (description, execution target,<span> </span></span>time step,<span style="color:var(--ds-text,#172b4d);"><span> </span>input and output parameters) from the specified project.</span> The</span> <span style="color:var(--ds-text,#333333);">set of input and output parameters is specified using the <strong>Input Parameters</strong> and <strong>Output Parameters</strong> properties of a Simulation Configuration. </span><span style="color:var(--ds-text,#333333);">The figure below demonstrates how to specify input and output parameters.</span></p><p><br /></p><p><ac:image ac:align="center"><ri:attachment ri:filename="specifying_input_output_parameters.png" /></ac:image></p><h6 style="text-align: center;">Specifying input and output parameters.</h6><p>The following table describes the parameters used in the request:</p><table class="relative-table wrapped" style="width: 77.345%;"><colgroup> <col style="width: 17.6721%;" /> <col style="width: 9.58126%;" /> <col style="width: 17.3172%;" /> <col style="width: 55.4294%;" /> </colgroup><tbody><tr><th>Parameter</th><th>In</th><th>Required or optional</th><th colspan="1">Description</th></tr><tr><td><strong>project</strong></td><td>path</td><td>required</td><td colspan="1">The Teamwork Cloud project name or ID.</td></tr><tr><td colspan="1"><strong>version</strong></td><td colspan="1">path</td><td colspan="1">optional</td><td colspan="1">The Teamwork Cloud project version.</td></tr><tr><td><strong>branch</strong></td><td>path</td><td>optional</td><td colspan="1">The project branch name or ID. If the branch is omitted, the trunk is used instead.</td></tr><tr><td colspan="1"><strong>config</strong></td><td colspan="1">path</td><td colspan="1">optional</td><td colspan="1">The Simulation Configuration name or server ID.</td></tr></tbody></table><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="9c2e8ff5-194d-497f-b377-3bb49a089737"><ac:parameter ac:name="title">Request and response examples</ac:parameter><ac:plain-text-body><![CDATA[ client.get_descriptor('SpacecraftMassPollup_SimWeb', config='spacecraft mass analysis')

{'config': 'spacecraft mass analysis',
 'description': 'Simulation Config that is dedicated to run spacecraft mass rollup.',
 'model': 'spacecraft',
 'parameters': {'inputs': [{'parameter': 'telecom.amplifier.me',
    'value': 32.0,
    'type': 'mass[kilogram]',
    'unit': 'kilogram',
    'requirements': [{'id': '1',
      'text': 'Estimated mass shall be less than allocated mass'}]},
   {'parameter': 'telecom.antenna.me',
    'value': 32.0,
    'type': 'mass[kilogram]',
    'unit': 'kilogram',
    'requirements': [{'id': '1',
      'text': 'Estimated mass shall be less than allocated mass'}]},
   {'parameter': 'propulsion.tank.me',
    'value': 68.0,
    'type': 'mass[kilogram]',
    'unit': 'kilogram',
    'requirements': [{'id': '1',
      'text': 'Estimated mass shall be less than allocated mass'}]},
   {'parameter': 'propulsion.thruster.me',
    'value': 68.0,
    'type': 'mass[kilogram]',
    'unit': 'kilogram',
    'requirements': [{'id': '1',
      'text': 'Estimated mass shall be less than allocated mass'}]}],
  'outputs': [{'parameter': 'telecom.me',
    'value': 32.0,
    'type': 'mass[kilogram]',
    'unit': 'kilogram',
    'requirements': [{'id': '1',
      'text': 'Estimated mass shall be less than allocated mass'}]},
   {'parameter': 'propulsion.me',
    'value': 68.0,
    'type': 'mass[kilogram]',
    'unit': 'kilogram',
    'requirements': [{'id': '1',
      'text': 'Estimated mass shall be less than allocated mass'}]},
   {'parameter': 'me',
    'value': 95.0,
    'type': 'mass[kilogram]',
    'unit': 'kilogram',
    'requirements': [{'id': '1',
      'text': 'Estimated mass shall be less than allocated mass'}]}]}}


client.get_descriptor('BouncingBall', config='Run BouncingBall')


{'config': 'Run BouncingBall',
 'description': 'Simulation Config dedicated to run simulation with bouncingBall.fmu.',
 'model': 'bouncingBall',
 'timeStep': '10 ms' 
 }]]></ac:plain-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=249571113 space=MMA version=5 -->
## PAGE 00719: Simulation using REST API

- page_id: `249571113`
- space_key: `MMA`
- source_url: https://docs.nomagic.com/spaces/MMA/pages/249571113/Simulation+using+REST+API
- version_number: 5
- version_date: `2025-12-03T09:37:29.181+01:00`
- ancestors: Magic Model Analyst / Cameo Simulation Toolkit Documentation > User Guide > Server-side simulation
- labels: []

### NORMALIZED CONTENT

It is possible to simulate Teamwork Cloud projects on the server by using REST API. The topics below describe all available REST API requests and provide examples of how to use them.

#### NOTE: Prerequisites

Prerequisites

Before starting the simulation, make sure you have [CONFLUENCE_PAGE title='Server-side simulation' space=''].

#### TIP: REST API documentation

REST API documentation

For more information about simulation-related REST APIs, see our [REST API documentation](https://osmc.nomagic.com/simulation/2026x/swagger/index.html) in Swagger. There you can find REST API descriptions in both machine-readable and human-readable formats.

REST API documentation is also provided with the installation of Magic Model Analyst / Cameo Simulation Toolkit with server-side simulation functionality. You can find it at *http://<IP>:<Port>/simulation/swagger/index.html*.

You can use the following REST API requests to simulate Teamwork Cloud projects on the server:

- 
- /version//branch//element//config/]]>
- ]]>
- ]]>
- ]]>
- ]]>
- ]]>
- ]]>
- ]]>
- ]]>
- GET /simulation/api/running
- ]]>
- /version//branch/]]>
- /version//branch//element/]]>
- /version//branch//config/]]>

##### Get the list of Teamwork Cloud projects

lightgrey

1

solid

GET /simulation/api/projects

This REST API endpoint provides the list of Teamwork Cloud projects accessible to you depending on your permissions. Only projects that you can read (the Read Resources permission) are returned.

```text

```

##### Run simulation

lightgrey

1

solid

POST /simulation/api/run/project/<project>/version/<version>/branch/<branch>/element/<element>/config/<config>

This REST API request initiates the execution of the specified Simulation Configuration in a particular project. It connects to Teamwork Cloud, finds the element to execute, and initiates the execution if the element exists. After the execution is complete, the request constructs and returns a unique ID (per application) for the given execution.

The following table describes the parameters used in the REST API request:

| Parameter | In | Required or optional | Description | Options |
| --- | --- | --- | --- | --- |
| project | path | required | The Teamwork Cloud project name or ID. | NA |
| version | path | optional | The Teamwork Cloud project version. | NA |
| branch | path | optional | The project branch name or ID. If the branch is omitted, the trunk is used instead. | NA |
| element | path | optional | The qualified name or server ID of the element to be executed. | NA |
| config | path | optional | The Simulation Configuration name or server ID. | NA |
| ?commitResults | query | optional | Commits a new project version with the simulation results. Available values are true or false (default). | NA |
| ?verification | query | optional | Returns the selected verification results. Available values are:all - all verification results are returned.none - no verification results are returned.fail (default) - verification results with the fail status are returned. | NA |
| ?startedFrom | query | optional | Allows specifying the starting location of the simulation. The value of the startedFrom query parameter is provided in the status endpoint response. | NA |
| ?timeout | query | optional | Allows specifying the timeout duration in minutes. If the timeout parameter is not provided, the sim.timeout.min property will be taken from the webappplatform.properties instead. | NA |
| inputs | body | optional | The set of input parameters with values that should be provided for the simulation.Input parameters can be the parameters with the data type, primitive type, or enumeration type. | NA |
| outputs | body | optional | The set of output parameters that should be obtained after the simulation is complete. If no output parameters are specified, all initialized values are returned.Output parameters can be the parameters with the data type, primitive type, or enumeration type. | NA |
| simconfig | body | optional | The set of simulation configuration properties along with their corresponding values. The simulation configuration options you specify will take precedence over the initial configuration option from a model. | "ALLOW_CONCURRENT_ALLOCATED_ACTIVITIES": true,"AUTOMATIC_PARAMETRIC_RECALCULATION": true,"AUTO_CONVERT_UNITS": true,"AUTO_CREATE_FUML_OBJECT_OF_OUTPUT_PIN": true,"AUTO_START": true,"AUTO_START_ACTIVE_OPTIONS": true,"AUTO_TERMINATE": true,"CLOCK_RATIO": 1,"CLONE_REFERENCES": true,"COMPLETION_EVENTS_AND_TRANSITIONS": true,"CONSTRAINT_FAILURE_AS_BREAKPOINT": true,"DECIMAL_PLACES": 4,"DEFAULT_LANGUAGE": "JavaScript Rhino","DURATION_SIMULATION_MODE": "MIN", // possible values: MIN, MAX, AVERAGE, RANDOM"ENDTIME": 0,"ENGINES_PRIORITY": "[on] fUML Engine\n[on] Interaction Engine\n[on] SCXML Engine","INITIALIZE_NUMERICAL_VALUE": false,"INITIALIZE_REFERENCES": true,"NUMBER_OF_RUNS": 0,"NUMBER_OF_STEPS": 0,"PASS_CALLER_CONTEXT": true,"RECORD_TIMESTAMP": false,"REMEMBER_FAILURE_STATUS": true,"RESULT_LOCATION": "Results","RUN_FORKS_IN_PARALLEL": true,"SOLVE_AFTER_INITIALIZATION": true,"START_TIME": 0,"STATE_ACTIVATION_SEMANTICS": "BEFORE_ENTRY", // possible values: "BEFORE_ENTRY", "AFTER_ENTRY""STEP_DELAY": 0,"STEP_SIZE": 0,"TERMINATE_BEHAVIOR_ON_EXCEPTION_THROWN": true,"TERMINATE_NESTED_BEHAVIORS": true,"TERMINATE_STREAMING_BEHAVIORS_BY_OUTPUT_PARAMETER_MULTIPLICITY": false,"TIME_UNIT": "MILLISECOND","TIME_VALUE": "Model-based Clock Test::Clock::time","TIME_VARIABLE_NAME": "simtime","TREAT_ALL_CLASSIFIERS_AS_ACTIVE": true,"USE_FUML_DECISION_SEMANTICS": false |

```text

```

```text

```

```text

```

##### Perform a time step

lightgrey

1

POST simulation/api/step/<simulation_id>

This REST API request performs a single time step of the specified simulation. To run the simulation by step, it should be run with the **AUTO_START** option of the simconfig parameter set to *false*.

The following table describes the parameters used in the REST API request:

| Parameter | In | Required or optional | Description |
| --- | --- | --- | --- |
| simulation_id | path | required | The ID of a specific simulation. |

##### Start simulation

lightgrey

1

POST /simulation/api/start/<simulation_id>

This REST API request starts the execution of the specified simulation. If the initialization phase is still in progress, the startendpoint is memorized and sent when the initialization phase is completed.

The following table describes the parameters used in the REST API request:

| Parameter | In | Required or optional | Description |
| --- | --- | --- | --- |
| simulation_id | path | required | The ID of a specific simulation. |

##### Get simulation status

lightgrey

1

GET /simulation/api/status/<simulation_id>

This REST API request gets the status, simulation time, and elapsed time of a specific simulation. It returns the actual elapsed time of the simulation thread and the simulation state (INITIALIZED, INITIALIZING, READY, QUEUED, RUNNING, COMPLETED, TERMINATING, TERMINATED, ERROR). For iterative executions (e.g., TradeStudy and MonteCarlo), the request also returns the total number of iteration runs and the number of the currently running iteration. If the simulation is placed in a waiting line, the QUEUED state and queued number are provided. If the model has aUI mockup, Time Series Chart, Timeline Chart, or HTML Table, you can use the URL provided in the 'ui' or indexUI' key to open the specified UI. If a user has the administrator role, the user ID is also returned.

The following table describes the parameters used in the REST API request:

| Parameter | In | Required or optional | Description |
| --- | --- | --- | --- |
| simulation_id | path | required | The ID of a specific simulation. |

```text

```

##### Get simulation variables

lightgrey

1

solid

POST simulation/api/get/<simulation_id>

This REST API request returns a list of simulation variables during simulation.

The following table describes the parameters used in the REST API request:

| Parameter | In | Required or optional | Description |
| --- | --- | --- | --- |
| simulation_id | path | required | The ID of the running simulation. |
| variables | body | optional | The set of simulation variables that should be obtained. If no variables are specified, the values of all simulation variables are returned. |

```text

```

##### Set simulation variables

lightgrey

1

solid

POST simulation/api/set/<simulation_id>

This REST API request specifies values for a provided list of simulation variables during simulation.

The following table describes the parameters used in the REST API request:

| Parameter | In | Required or optional | Description |
| --- | --- | --- | --- |
| simulation_id | path | required | The ID of the running simulation. |
| variables | body | required | The set of simulation variables with values that should be used during the current simulation. |
| context | body | optional | The context ID. |
| propertyPath | body | optional | The property path of the context specified using property names or IDs. |

```text

```

##### Pause simulation

lightgrey

1

solid

POST /simulation/api/pause/<simulation_id>

This REST API request pauses the execution of the specified simulation.

The following table describes the parameters used in the REST API request:

| Parameter | In | Required or optional | Description |
| --- | --- | --- | --- |
| simulation_id | path | required | The ID of the running simulation. |

##### Resume simulation

lightgrey

1

solid

POST /simulation/api/resume/<simulation_id>

This REST API request resumes the execution of the specified simulation.

The following table describes the parameters used in the REST API request:

| Parameter | In | Required or optional | Description |
| --- | --- | --- | --- |
| simulation_id | path | required | The ID of the running simulation. |

##### Get simulation results

lightgrey

1

solid

GET /simulation/api/result/<simulation_id>

This REST API request returns the results of the specified simulation. You can specify what output parameters should be returned in the run REST API body. If output parameters are not specified, all output parameters are obtained. The verification results are returned based on the value of theverificationparameter of the Run Simulation endpoint.If the CSV export is specified for the Simulation Configuration, the CSV export results are returned in JSON format. If a Time Series or Timeline chart is specified for the Simulation Configuration, the chart data is returned in JSON format as well.

The figure below demonstrates how to specify input and output parameters.

[IMAGE alt='' src='']

###### Specifying input and output parameters.

- Output parameters can be the parameters with the data type, primitive type, or enumeration type.
- If the OutputParameters tag of the executed Simulation Configuration is specified, the results are provided according to the OutputParameters tag value.

The following table describes the parameters used in the REST API request:

| Parameter | In | Required or optional | Description |
| --- | --- | --- | --- |
| simulation_id | path | required | The ID of the running simulation. |

```text
=57500',
     'status': 'fail',
     'margin': -1086.92089241422,
     'timestamp': 0}]},
  {'property': 'wheel.brake.rotor.outerDiameter',
   'status': 'fail',
   'value': 0.25,
   'requirements': [{'id': '6',
     'text': 'The brake rotors shall have a 0.28 meter diameter.',
     'constraint': 'outerDiameter==0.28',
     'status': 'fail',
     'margin': -0.03,
     'timestamp': 0}]}]}]]>
```

##### ****Get the list of running simulations

lightgrey

1

solid

GET /simulation/api/running

This REST API request gets the list of all currently running simulations including the queued simulations that are placed in a waiting line.

```text

```

##### ****Terminate simulation

lightgrey

1

solid

POST /simulation/api/terminate/<simulation_id>

This REST API request terminates the specified simulation.

The following table describes the parameters used in the REST API request:

| Parameter | In | Required or optional | Description |
| --- | --- | --- | --- |
| simulation_id | path | required | The ID of a specific simulation. |

```text

```

##### ****Check for Simulation Configurations

lightgrey

1

solid

GET /simulation/api/hasConfigs/project/<project>/version/<version>/branch/<branch>

This REST API request checks if the project has any Simulation Configurations.

The following table describes the parameters used in the REST API request:

| Parameter | In | Required or optional | Description |
| --- | --- | --- | --- |
| project | path | required | The Teamwork Cloud project name or ID. |
| version | path | optional | The Teamwork Cloud project version. |
| branch | path | optional | The project branch name or ID. If the branch is omitted, the trunk is used instead. |

```text

```

##### Get Simulation Configurations

lightgrey

1

solid

GET /simulation/api/configs/project/<project>/version/<version>/branch/<branch>/element/<element>

This REST API request retrieves element IDs, names, and descriptions of the Simulation Configurations available for the given executable element.

If the executable element is an Instance Specification, the method returns the following Simulation Configurations:

- Whose execution target is the classifier of the executable element.
- Whose execution target is the Instance Specification having at least one classifier matching those of the executable element.

The following table describes the parameters used in the REST API request:

| Parameter | In | Required or optional | Description |
| --- | --- | --- | --- |
| project | path | required | The Teamwork Cloud project name or ID. |
| version | path | optional | The Teamwork Cloud project version. |
| branch | path | optional | The project branch name or ID. If the branch is omitted, the trunk is used instead. |
| element | path | optional | The qualified name or server ID of the element to be executed. |
| ?filter | query | optional | Returns Simulations Configurations with a specified UI tag for a particular project. The only possible value for the filter parameter is ui.Only Simulations Configurations having at least one of the following UI elements are returned:FrameTableTimeSeries chartTimeline chart |

```text

```

##### Get Simulation Configuration descriptor

lightgrey

1

solid

GET simulation/api/descriptor/project/<project>/version/<version>/branch/<branch>/config/<config>

This REST API request retrieves Simulation Configuration data (description, execution target,time step,input and output parameters) from the specified project. Theset of input and output parameters is specified using the **Input Parameters** and **Output Parameters** properties of a Simulation Configuration.The figure below demonstrates how to specify input and output parameters.

[IMAGE alt='' src='']

###### Specifying input and output parameters.

The following table describes the parameters used in the REST API request:

| Parameter | In | Required or optional | Description |
| --- | --- | --- | --- |
| project | path | required | The Teamwork Cloud project name or ID. |
| version | path | optional | The Teamwork Cloud project version. |
| branch | path | optional | The project branch name or ID. If the branch is omitted, the trunk is used instead. |
| config | path | optional | The Simulation Configuration name or server ID. |

```text

```

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>It is possible to simulate Teamwork Cloud projects on the server by using REST API. The topics below describe all available REST API requests and provide examples of how to use them.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="4b2c6a4e-9f6c-43f4-a634-89475a2b7d2a"><ac:parameter ac:name="title">Prerequisites</ac:parameter><ac:rich-text-body><p>Before starting the simulation, make sure you have <ac:link ac:anchor="Preparing projects for server-side simulation"><ri:page ri:content-title="Server-side simulation" /><ac:plain-text-link-body><![CDATA[prepared your projects for server-side simulation]]></ac:plain-text-link-body></ac:link>.</p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="8a23eb57-6263-4713-84ef-95a9f0401df1"><ac:parameter ac:name="title">REST API documentation</ac:parameter><ac:rich-text-body><p>For more information about simulation-related REST APIs, see our <a href="https://osmc.nomagic.com/simulation/2026x/swagger/index.html">REST API documentation</a> in Swagger. There you can find <span>REST API descriptions in both machine-readable and human-readable formats.</span></p><p><span>REST API documentation is also provided with the installation of Magic Model Analyst / Cameo Simulation Toolkit with server-side simulation functionality. You can find it at <em>http://&lt;IP&gt;:&lt;Port&gt;/simulation/swagger/index.html</em>.</span></p></ac:rich-text-body></ac:structured-macro><p><br />You can use the following REST API requests to simulate Teamwork Cloud projects on the server:</p><ul><li data-uuid="a4da7332-f346-47a5-9ccc-e3ece04c6b1a"><span><ac:link ac:anchor="Get the list of Teamwork Cloud projects"><ac:plain-text-link-body><![CDATA[GET /simulation/api/projects]]></ac:plain-text-link-body></ac:link></span></li><li data-uuid="c270e361-be63-45ae-8bbc-a0c2d2b3a52a"><ac:link ac:anchor="Run simulation"><ac:plain-text-link-body><![CDATA[ POST /simulation/api/run/project/<project>/version/<version>/branch/<branch>/element/<element>/config/<config>]]></ac:plain-text-link-body></ac:link></li><li data-uuid="c76a6aae-38bd-4354-a23e-689184cdaebc"><ac:link ac:anchor="Perform a time step"><ac:plain-text-link-body><![CDATA[POST simulation/api/step/<simulation_id>]]></ac:plain-text-link-body></ac:link></li><li data-uuid="a69da4a1-3172-4a91-83ac-8c6f24ae4f0e"><ac:link ac:anchor="Start simulation"><ac:plain-text-link-body><![CDATA[POST /simulation/api/start/<simulation_id>]]></ac:plain-text-link-body></ac:link></li><li data-uuid="6ff12a8f-493b-49d1-be7d-bb03faadb1d6"><ac:link ac:anchor="Get simulation status"><ac:plain-text-link-body><![CDATA[GET /simulation/api/status/<simulation_id>]]></ac:plain-text-link-body></ac:link></li><li data-uuid="a85cae63-6977-489d-b2b1-1c2fc67564e8"><ac:link ac:anchor="Get simulation variables"><ac:plain-text-link-body><![CDATA[POST simulation/api/get/<simulation_id>]]></ac:plain-text-link-body></ac:link></li><li data-uuid="384d8203-31cf-4ea0-8b2f-4e0817bb7fa1"><ac:link ac:anchor="Set simulation variables"><ac:plain-text-link-body><![CDATA[POST simulation/api/set/<simulation_id>]]></ac:plain-text-link-body></ac:link></li><li data-uuid="f86da416-8670-4f55-9a21-0cd1021370e8"><ac:link ac:anchor="Pause simulation"><ac:plain-text-link-body><![CDATA[POST /simulation/api/pause/<simulation_id>]]></ac:plain-text-link-body></ac:link></li><li data-uuid="e538646a-d321-47d4-a3fc-ec730bc7d6cd"><ac:link ac:anchor="Resume simulation"><ac:plain-text-link-body><![CDATA[POST /simulation/api/resume/<simulation_id>]]></ac:plain-text-link-body></ac:link></li><li data-uuid="bb35f50f-10ea-470d-bb7a-1f25ee2e76a8"><ac:link ac:anchor="Get simulation results"><ac:plain-text-link-body><![CDATA[GET /simulation/api/result/<simulation_id>]]></ac:plain-text-link-body></ac:link></li><li data-uuid="32d6efb5-4544-411b-b731-22653d46b4f5"><ac:link ac:anchor="Get the list of running simulations"><ac:link-body><span>GET /simulation/api/running</span></ac:link-body></ac:link></li><li data-uuid="6cde9330-e4ed-4f5f-94e7-3f2cd36207ba"><ac:link ac:anchor="Terminate simulation"><ac:plain-text-link-body><![CDATA[POST /simulation/api/terminate/<simulation_id>]]></ac:plain-text-link-body></ac:link></li><li data-uuid="4c8715cb-d55a-4fb7-a47f-a9b4d7ab9752"><ac:link ac:anchor="Check for Simulation Configurations"><ac:plain-text-link-body><![CDATA[GET /simulation/api/hasConfigs/project/<project>/version/<version>/branch/<branch>]]></ac:plain-text-link-body></ac:link></li><li data-uuid="0c8d3199-e6d6-48a2-95ff-65b63f2deb31"><ac:link ac:anchor="Get Simulation Configurations"><ac:plain-text-link-body><![CDATA[GET /simulation/api/configs/project/<project>/version/<version>/branch/<branch>/element/<element>]]></ac:plain-text-link-body></ac:link></li><li data-uuid="e777cd1a-64a7-4173-a4c5-eb84f03f773d"><ac:link ac:anchor="Get Simulation Configuration descriptor"><ac:plain-text-link-body><![CDATA[GET simulation/api/descriptor/project/<project>/version/<version>/branch/<branch>/config/<config>]]></ac:plain-text-link-body></ac:link></li></ul><h3><br />Get the list of Teamwork Cloud projects</h3><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="c5bf2928-f37d-45e7-89be-3ae280c0c649"><ac:parameter ac:name="borderColor">lightgrey</ac:parameter><ac:parameter ac:name="borderWidth">1</ac:parameter><ac:parameter ac:name="borderStyle">solid</ac:parameter><ac:rich-text-body><p>GET /simulation/api/projects</p></ac:rich-text-body></ac:structured-macro><p><br />This REST API endpoint provides the list of Teamwork Cloud projects accessible to you depending on your permissions. Only projects that you can read (the Read Resources permission) are returned.<br /><br /></p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="61c559d6-d351-4fb8-833d-76f36b1b42e9"><ac:parameter ac:name="title">Request and response examples</ac:parameter><ac:plain-text-body><![CDATA[/simulation/api/projects


[{'id': '1f9fd988-620b-4b3c-8414-7ab96dc53a48',
  'name': 'SpacecraftMassRollup',
  'description': ''},
 {'id': 'c125b91e-7d31-4015-b659-6fd98059b8c7',
  'name': 'BouncingBall',
  'description': 'This project demonstrates the execution of the BouncingBall, including fmu.'},
 {'id': '485dfc82-7b08-43cd-86b1-953b3725e5b1',
  'name': 'CarBrakingAnalysis',
  'description': 'This project calculates the stopping distance based on car speed and mass.'}]]]></ac:plain-text-body></ac:structured-macro><h3><br />Run simulation</h3><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="ce30b831-4d54-4cd1-ac96-ff0f4acc4ab0"><ac:parameter ac:name="borderColor">lightgrey</ac:parameter><ac:parameter ac:name="borderWidth">1</ac:parameter><ac:parameter ac:name="borderStyle">solid</ac:parameter><ac:rich-text-body><p>POST /simulation/api/run/project/<span style="color:var(--ds-background-accent-orange-bolder,#c25100);">&lt;project&gt;</span>/version/<span style="color:var(--ds-background-accent-orange-bolder,#c25100);">&lt;version&gt;</span>/branch/<span style="color:var(--ds-background-accent-orange-bolder,#c25100);">&lt;branch&gt;</span>/element/<span style="color:var(--ds-background-accent-orange-bolder,#c25100);">&lt;element&gt;</span>/config/<span style="color:var(--ds-background-accent-orange-bolder,#c25100);">&lt;config&gt;</span></p></ac:rich-text-body></ac:structured-macro><p><br />This REST API request initiates the execution of the specified Simulation Configuration in a particular project. It connects to Teamwork Cloud, finds the element to execute, and initiates the execution if the element exists. After the execution is complete, the request constructs and returns a unique ID (per application) for the given execution.</p><p>The following table describes the parameters used in the REST API request:</p><table class="relative-table" style="width: 100.0%;"><colgroup class=""><col class="" style="width: 7.35456%;" /><col class="" style="width: 5.26894%;" /><col class="" style="width: 7.9034%;" /><col class="" style="width: 49.8353%;" /><col class="" style="width: 29.6378%;" /></colgroup><tbody class=""><tr class=""><th>Parameter</th><th>In</th><th>Required or optional</th><th>Description</th><th>Options</th></tr><tr class=""><td><strong>project</strong></td><td>path</td><td>required</td><td>The Teamwork Cloud project name or ID.</td><td>NA</td></tr><tr class=""><td><strong>version</strong></td><td>path</td><td>optional</td><td>The Teamwork Cloud project version.</td><td>NA</td></tr><tr class=""><td><strong>branch</strong></td><td>path</td><td>optional</td><td>The project branch name or ID. If the branch is omitted, the trunk is used instead.</td><td>NA</td></tr><tr class=""><td><strong>element</strong></td><td>path</td><td>optional</td><td>The qualified name or server ID of the element to be executed.</td><td>NA</td></tr><tr class=""><td><strong>config</strong></td><td>path</td><td>optional</td><td>The Simulation Configuration name or server ID.</td><td>NA</td></tr><tr class=""><td><strong><span style="color:var(--ds-text,#333333);">?commitResults</span></strong></td><td>query</td><td>optional</td><td><p>Commits a new project version with the simulation results. Available values are <em>true</em> or <em>false</em> (default).</p></td><td>NA</td></tr><tr class=""><td><strong>?verification</strong></td><td>query</td><td>optional</td><td><p>Returns the selected verification results. Available values are:</p><ul><li style="list-style-type: none;background-image: none;" data-uuid="67df4cc6-293a-4262-a21b-618d7bcfb76e"><ul><li><strong>all</strong> - all verification results are returned.</li><li><strong>none</strong> - no verification results are returned.</li><li><strong>fail</strong> (default) - verification results with the fail status are returned.</li></ul></li></ul></td><td>NA</td></tr><tr class=""><td><strong>?startedFrom</strong></td><td>query</td><td>optional</td><td><span style="color:var(--ds-text,#172b4d);">Allows specifying the starting location of the simulation. The value of the <strong>startedFrom</strong> query parameter is provided in the status endpoint response.</span></td><td>NA</td></tr><tr class=""><td><p><strong><span style="color:var(--ds-text,#172b4d);">?timeout</span></strong></p></td><td><span style="color:var(--ds-text,#172b4d);">query</span></td><td><span style="color:var(--ds-text,#172b4d);">optional</span></td><td><span style="color:var(--ds-text,#172b4d);">Allows specifying the timeout duration in minutes. If the<span> </span></span><strong style="text-align: left;">timeout</strong><span style="color:var(--ds-text,#172b4d);"><span> </span>parameter is not provided, the<span> </span></span><strong style="text-align: left;">sim.timeout.min</strong><span style="color:var(--ds-text,#172b4d);"><span> </span>property will be taken from the webappplatform.properties instead.</span></td><td>NA</td></tr><tr class=""><td><strong>inputs</strong></td><td>body</td><td>optional</td><td><div class="content-wrapper"><p class="auto-cursor-target">The set of input parameters with values that should be provided for the simulation.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="a0e1cbfa-cfd0-4c0c-93a1-d06e429f65fe"><ac:rich-text-body><p>Input parameters can be the parameters with the data type, primitive type, or enumeration type.</p></ac:rich-text-body></ac:structured-macro></div></td><td>NA</td></tr><tr class=""><td><strong>outputs</strong></td><td>body</td><td>optional</td><td><div class="content-wrapper"><p class="auto-cursor-target"><span>The set of output parameters that should be obtained after the simulation is complete. </span><span>If</span><span style="color:var(--ds-text,#333333);"> no output parameters are specified, all initialized values are returned.<br /></span></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="2db5d4a0-c6ec-401d-9628-3c86d97a61d5"><ac:rich-text-body><p>Output parameters can be the parameters with the data type, primitive type, or enumeration type.</p></ac:rich-text-body></ac:structured-macro></div></td><td>NA</td></tr><tr class=""><td><p><strong>simconfig</strong></p></td><td>body</td><td>optional</td><td>The set of simulation configuration properties along with their corresponding values. The simulation configuration options you specify will take precedence over the initial configuration option from a model.</td><td><ul><li data-uuid="b67fe33c-6f72-41dc-bc83-0042adce75e2">&quot;ALLOW_CONCURRENT_ALLOCATED_ACTIVITIES&quot;: true,</li><li data-uuid="7ae59820-ce5f-47ff-8afd-4063fa94c21c">&quot;AUTOMATIC_PARAMETRIC_RECALCULATION&quot;: true,</li><li data-uuid="946e5642-66ea-45dd-93e1-b9ae982504a7">&quot;AUTO_CONVERT_UNITS&quot;: true,</li><li data-uuid="c0e4d748-418e-4205-81c7-7307592b3fe7">&quot;AUTO_CREATE_FUML_OBJECT_OF_OUTPUT_PIN&quot;: true,</li><li data-uuid="54ba8d10-9838-4254-88e1-615aaaaa2849">&quot;AUTO_START&quot;: true,</li><li data-uuid="42f99c4a-a468-4286-a4dc-d37c8ca7b311">&quot;AUTO_START_ACTIVE_OPTIONS&quot;: true,</li><li data-uuid="3e2f43a9-52f1-4c15-a7e0-762365d986ff">&quot;AUTO_TERMINATE&quot;: true,</li><li data-uuid="7b957d7a-9c00-4f06-a49f-bccc87f7c1c7">&quot;CLOCK_RATIO&quot;: 1,</li><li data-uuid="201b0a97-e441-4947-ba43-c074bab3b467">&quot;CLONE_REFERENCES&quot;: true,</li><li data-uuid="13d5a9fa-6111-479a-bb8a-09d6a71d8bbc">&quot;COMPLETION_EVENTS_AND_TRANSITIONS&quot;: true,</li><li data-uuid="da144ac4-1767-48f5-8aff-a890c70e896b">&quot;CONSTRAINT_FAILURE_AS_BREAKPOINT&quot;: true,</li><li data-uuid="689252cb-ba3b-4666-bd65-fd28f0053a49">&quot;DECIMAL_PLACES&quot;: 4,</li><li data-uuid="93d68854-bdc9-496f-999c-4c163e2a8cda">&quot;DEFAULT_LANGUAGE&quot;: &quot;JavaScript Rhino&quot;,</li><li data-uuid="0e47d6ed-061a-463b-9a10-aa63c0fa31da">&quot;DURATION_SIMULATION_MODE&quot;: &quot;MIN&quot;, // possible values: MIN, MAX, AVERAGE, RANDOM</li><li data-uuid="dbc6276b-6a5c-47c4-ab76-3f51a923f653">&quot;ENDTIME&quot;: 0,</li><li data-uuid="32e6b6cf-e153-4798-a372-7fd4e3ebee68">&quot;ENGINES_PRIORITY&quot;: &quot;<span class="error">[on]</span> fUML Engine\n<span class="error">[on]</span> Interaction Engine\n<span class="error">[on]</span> SCXML Engine&quot;,</li><li data-uuid="7abad799-134a-44ca-b319-3fefc7518ee8">&quot;INITIALIZE_NUMERICAL_VALUE&quot;: false,</li><li data-uuid="961de3fe-764c-4d55-8ca1-e6dc36e5ab0a">&quot;INITIALIZE_REFERENCES&quot;: true,</li><li data-uuid="a071b1ce-730e-4e67-bfe6-6db3402e9fd5">&quot;NUMBER_OF_RUNS&quot;: 0,</li><li data-uuid="16397386-89b7-4bd4-af50-062b538bbb06">&quot;NUMBER_OF_STEPS&quot;: 0,</li><li data-uuid="41a99d8c-e688-4b74-87d2-dfd156850d4a">&quot;PASS_CALLER_CONTEXT&quot;: true,</li><li data-uuid="82d86af9-4b1b-4165-a249-ab2d77b6e03a">&quot;RECORD_TIMESTAMP&quot;: false,</li><li data-uuid="3e3be90b-a15c-4ca1-9e97-98e8fa656279">&quot;REMEMBER_FAILURE_STATUS&quot;: true,</li><li data-uuid="882f92a3-2c83-4a3c-9aa0-b4c04f325fbb">&quot;RESULT_LOCATION&quot;: &quot;Results&quot;,</li><li data-uuid="e23b2ea7-26e1-4309-9078-1e799373b30e">&quot;RUN_FORKS_IN_PARALLEL&quot;: true,</li><li data-uuid="5856fd2e-2a16-4783-9c8a-33b6e11fd586">&quot;SOLVE_AFTER_INITIALIZATION&quot;: true,</li><li data-uuid="25a220fd-d9c6-4bc3-a517-5bfcf82d062b">&quot;START_TIME&quot;: 0,</li><li data-uuid="63f000be-1ed7-4c48-bc8f-e9ff91084ae7">&quot;STATE_ACTIVATION_SEMANTICS&quot;: &quot;BEFORE_ENTRY&quot;, // possible values: &quot;BEFORE_ENTRY&quot;, &quot;AFTER_ENTRY&quot;</li><li data-uuid="67f10a6e-8431-45c7-adda-dcd7d279d8e2">&quot;STEP_DELAY&quot;: 0,</li><li data-uuid="b620c55a-4aeb-44c1-a054-015f14324492">&quot;STEP_SIZE&quot;: 0,</li><li data-uuid="4668976a-f02b-40a5-aeb9-f23d2be2e361">&quot;TERMINATE_BEHAVIOR_ON_EXCEPTION_THROWN&quot;: true,</li><li data-uuid="3a460810-30bb-4535-85eb-28b464819465">&quot;TERMINATE_NESTED_BEHAVIORS&quot;: true,</li><li data-uuid="cbca75f9-6873-4076-9219-8d5485896ec8">&quot;TERMINATE_STREAMING_BEHAVIORS_BY_OUTPUT_PARAMETER_MULTIPLICITY&quot;: false,</li><li data-uuid="ff85ef32-4924-49ec-a5ca-e3e9b3a4243b">&quot;TIME_UNIT&quot;: &quot;MILLISECOND&quot;,</li><li data-uuid="a4939a1f-2966-41b2-8e3a-be43081e4d8a">&quot;TIME_VALUE&quot;: &quot;Model-based Clock Test::Clock::time&quot;,</li><li data-uuid="197ea15f-aec7-47df-8810-9248c3a56138">&quot;TIME_VARIABLE_NAME&quot;: &quot;simtime&quot;,</li><li data-uuid="d1286507-2729-4783-a264-e9ff33190cab">&quot;TREAT_ALL_CLASSIFIERS_AS_ACTIVE&quot;: true,</li><li data-uuid="1da019e0-c42b-45aa-bc7d-fc74db0f3aa6">&quot;USE_FUML_DECISION_SEMANTICS&quot;: false</li></ul></td></tr></tbody></table><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="996864bc-50eb-48b6-8b8b-80d1d925c84d"><ac:parameter ac:name="title">Request and response examples</ac:parameter><ac:plain-text-body><![CDATA[/simulation/api/run/project/SpacecraftMassRollup/branch/2/element/519701b0-bec8-4f51-aad5-152a5411d60b/config/spacecraft mass analysis?resultAsJson=true

{"state": "INITIALIZING",
"simulationId": "c7944233-a1cb-4310-a62f-48bce07dd71c",
"elapsedTime": 1591}


/simulation/api/run/project/CarBrakingAnalysis/config/Vehicle Analysis no Matlab

{"state": "RUNNING",
 "simulationId": "cf83877b-86cc-466c-89a1-af97619a9a86",
 "elapsedTime": 1821}


/simulation/api/run/project/8715fcfa-fd34-4928-8480-13f4439cec3d/element/519701b0-bec8-4f51-aad5-152a5411d60b/config/7915fcfa-fd88-4910-8560-13f4439cec3d

{"state": "QUEUED",
 "simulationId": "b7bdf933-f58d-4e7e-b73b-8370c60485cd",
 "queueNumber": 1,
 "elapsedTime": 0}]]></ac:plain-text-body></ac:structured-macro><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="e7a52d3d-49d6-4156-b499-2a1e1fe4d14b"><ac:parameter ac:name="title">Request example with a request body</ac:parameter><ac:plain-text-body><![CDATA[/simulation/api/run/project/SpacecraftMassRollup/config/spacecraft mass analysis

Request body:
{
"inputs":
   {
        "propulsion.tank.me": 38,
        "propulsion.thruster.me": 30,
        "telecom.antena.me": 19,
        "telecom.amplifier.me": 8
   },
 "outputs": 
    [ 
        "propulsion.me", 
        "telecom.me" 
    ] 
}

Response:
{"state": "RUNNING",
 "simulationId": "b7bdf933-f58d-4e7e-b73b-8370c60485cd",
 "elapsedTime": 1480}
]]></ac:plain-text-body></ac:structured-macro><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="e6f5d0e3-e46e-48f8-9033-94c9ee1d75a2"><ac:parameter ac:name="title">Request example with simulation options specified in a request body</ac:parameter><ac:plain-text-body><![CDATA[/simulation/api/run/project/OntologicalBehaviorModeling/config/Ontological Configurable

Request body:
{
"simconfig":
   {
        "AUTO_START": true,
        "DURATION_SIMULATION_MODE": "MIN",
        "ENDTIME": 50,
        "TERMINATE_NESTED_BEHAVIORS": false
   }
}
 
Response:
{"state": "RUNNING",
 "simulationId": "37f51022-d164-4077-bfa9-0414e02a7b52",
 "elapsedTime": 1016}]]></ac:plain-text-body></ac:structured-macro><h3>Perform a time step</h3><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="cfd4167a-0def-4f2a-864e-dfbf9f97a8e6"><ac:parameter ac:name="borderColor">lightgrey</ac:parameter><ac:parameter ac:name="borderWidth">1</ac:parameter><ac:rich-text-body><p>POST simulation/api/step/<span style="color:var(--ds-background-accent-orange-bolder,#c25100);">&lt;simulation_id&gt;</span></p></ac:rich-text-body></ac:structured-macro><p><br />This REST API request performs a single time step of the specified simulation. To run the simulation by step, it should be run with the <strong>AUTO_START</strong> option of the simconfig parameter set to <em>false</em>.</p><p>The following table describes the parameters used in the REST API request:</p><table class="relative-table" style="width: 81.1849%;"><colgroup class=""><col class="" style="width: 15.1454%;" /><col class="" style="width: 8.92495%;" /><col class="" style="width: 15.4158%;" /><col class="" style="width: 60.5139%;" /></colgroup><tbody class=""><tr class=""><th>Parameter</th><th>In</th><th>Required or optional</th><th colspan="1">Description</th></tr><tr class=""><td><strong>simulation_id</strong></td><td>path</td><td>required</td><td colspan="1">The ID of a specific simulation.</td></tr></tbody></table><h3><br />Start simulation</h3><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="9ce096eb-8e29-4767-aab5-9c71e6a97708"><ac:parameter ac:name="borderColor">lightgrey</ac:parameter><ac:parameter ac:name="borderWidth">1</ac:parameter><ac:rich-text-body><p>POST /simulation/api/start/<span style="color:var(--ds-background-accent-orange-bolder,#c25100);">&lt;simulation_id&gt;</span></p></ac:rich-text-body></ac:structured-macro><p><br />This REST API request starts the execution of the specified simulation. <span>If the initialization phase is still in progress, the start </span><span>endpoint is memorized and sent when the initialization phase is completed.</span></p><p>The following table describes the parameters used in the REST API request:</p><table class="relative-table" style="width: 81.1849%;"><colgroup class=""><col class="" style="width: 15.1454%;" /><col class="" style="width: 8.92495%;" /><col class="" style="width: 15.4158%;" /><col class="" style="width: 60.5139%;" /></colgroup><tbody class=""><tr class=""><th>Parameter</th><th>In</th><th>Required or optional</th><th colspan="1">Description</th></tr><tr class=""><td><strong>simulation_id</strong></td><td>path</td><td>required</td><td colspan="1">The ID of a specific simulation.</td></tr></tbody></table><h3><br />Get simulation status</h3><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="ab17a96c-7c5d-4a7a-ba19-0b4156430fd8"><ac:parameter ac:name="borderColor">lightgrey</ac:parameter><ac:parameter ac:name="borderWidth">1</ac:parameter><ac:rich-text-body><p>GET /simulation/api/status/<span style="color:var(--ds-background-accent-orange-bolder,#c25100);">&lt;simulation_id&gt;</span></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br />This REST API request <span style="color:var(--ds-text,#333333);">gets the status, simulation time, and elapsed time</span> of a specific simulation. It returns the actual elapsed time of the simulation thread and the simulation state (INITIALIZED, INITIALIZING, READY, QUEUED, RUNNING, COMPLETED, TERMINATING, TERMINATED, ERROR). For iterative executions (e.g., TradeStudy and MonteCarlo), the request also returns <span style="color:var(--ds-text,#172b4d);">the total number of iteration runs and the number of the currently running iteration.</span> <span style="color:var(--ds-text,#333333);">If the simulation is placed in a waiting line, the QUEUED state and queued number are provided. <span style="color:var(--ds-text,#172b4d);">If the model has a<span> </span></span>UI mockup, Time Series Chart<span style="color:var(--ds-text,#172b4d);">, Timeline Chart, or HTML Table, you can use the URL provided in the 'ui' or indexUI' key to open the specified UI.</span></span> If a user has the administrator role, the user ID is also returned. </p><p>The following table describes the parameters used in the REST API request:</p><table class="relative-table" style="width: 81.1849%;"><colgroup class=""><col class="" style="width: 15.1454%;" /><col class="" style="width: 8.92495%;" /><col class="" style="width: 15.4158%;" /><col class="" style="width: 60.5139%;" /></colgroup><tbody class=""><tr class=""><th>Parameter</th><th>In</th><th>Required or optional</th><th colspan="1">Description</th></tr><tr class=""><td><strong>simulation_id</strong></td><td>path</td><td>required</td><td colspan="1">The ID of a specific simulation.</td></tr></tbody></table><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="9c366d62-dbb3-4f8f-b234-c438727b7d85"><ac:parameter ac:name="title">Request and response examples</ac:parameter><ac:plain-text-body><![CDATA[/simulation/api/status/77d0c496-c1e2-42cd-8ba4-04e4c7f359d3

{'state': 'RUNNING',
 'simulationId': '77d0c496-c1e2-42cd-8ba4-04e4c7f359d3',
 'simulationTime': '0 ms',
 'indexUI': 'http://nm-simulation.dsone.3ds.com/simulation/api/ui/index/77d0c496-c1e2-42cd-8ba4-04e4c7f359d3?pages=Coffee%20Machine.html&pages=Water%20Heating%20Element.html&pages=Wallet.html',
 'project': 'CoffeeMachine',
 'config': 'Coffee Machine',
 'elapsedTime': 0,
 'podName': 'simulation-deployment-6989d5dfc9-r6llk',
 'ui': ['http://nm-simulation.dsone.3ds.com/simulation/api/ui/77d0c496-c1e2-42cd-8ba4-04e4c7f359d3/Coffee%20Machine.html',
  'http://nm-simulation.dsone.3ds.com/simulation/api/ui/77d0c496-c1e2-42cd-8ba4-04e4c7f359d3/Water%20Heating%20Element.html',
  'http://nm-simulation.dsone.3ds.com/simulation/api/ui/77d0c496-c1e2-42cd-8ba4-04e4c7f359d3/Wallet.html']}


/simulation/api/status/ce8c8215-0515-43fd-9d34-92d1d7a95d87
 
{'state': 'COMPLETED',
 'simulationId': 'ce8c8215-0515-43fd-9d34-92d1d7a95d87',
 'simulationTime': '3000 ms',
 'project': 'SpacecraftMassRollup',
 'config': 'spacecraft mass analysis',
 'elapsedTime': 6598}
 
 
/simulation/api/status/b7bdf933-f58d-4e7e-b73b-8370c60485cd
 
{'state': 'QUEUED',
 'queueNumber': 3,
 'simulationId': 'b7bdf933-f58d-4e7e-b73b-8370c60485cd',
 'simulationTime': '0 ms',
 'project': 'CarBrakingAnalysis',
 'elapsedTime': 52}]]></ac:plain-text-body></ac:structured-macro><h3><br />Get simulation variables</h3><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="c0fe21ad-1e85-458b-944d-51225d4e9ec6"><ac:parameter ac:name="borderColor">lightgrey</ac:parameter><ac:parameter ac:name="borderWidth">1</ac:parameter><ac:parameter ac:name="borderStyle">solid</ac:parameter><ac:rich-text-body><p>POST simulation/api/get/<span style="color:var(--ds-background-accent-orange-bolder,#c25100);">&lt;simulation_id&gt;</span></p></ac:rich-text-body></ac:structured-macro><p><br />This REST API request returns a list of simulation variables during simulation.</p><p>The following table describes the parameters used in the REST API request:</p><table class="relative-table" style="width: 80.362%;"><colgroup class=""><col class="" style="width: 15.9836%;" /><col class="" style="width: 9.15301%;" /><col class="" style="width: 15.3005%;" /><col class="" style="width: 59.5628%;" /></colgroup><tbody class=""><tr class=""><th>Parameter</th><th>In</th><th>Required or optional</th><th colspan="1">Description</th></tr><tr class=""><td><strong>simulation_id</strong></td><td>path</td><td>required</td><td colspan="1">The ID of the running simulation.</td></tr><tr class=""><td colspan="1"><strong>variables</strong></td><td colspan="1">body</td><td colspan="1">optional</td><td colspan="1">The set of simulation variables that should be obtained. If no variables are specified, the values of all simulation variables are returned.</td></tr></tbody></table><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="91c406ec-2b16-4dd4-861d-e75499fb21b1"><ac:parameter ac:name="title">Request and response examples</ac:parameter><ac:plain-text-body><![CDATA[/simulation/api/get/ce8c8215-0515-43fd-9d34-92d1d7a95d87

{
"variables":
   [
        "propulsion.tank.me",
        "propulsion.thruster.me",
        "telecom.antena.me",
        "telecom.amplifier.me"
   ]
}]]></ac:plain-text-body></ac:structured-macro><h3>Set simulation variables</h3><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="3d635b51-55d8-43d0-a14c-6362f25d9e87"><ac:parameter ac:name="borderColor">lightgrey</ac:parameter><ac:parameter ac:name="borderWidth">1</ac:parameter><ac:parameter ac:name="borderStyle">solid</ac:parameter><ac:rich-text-body><p>POST simulation/api/set/<span style="color:var(--ds-background-accent-orange-bolder,#c25100);">&lt;simulation_id&gt;</span></p></ac:rich-text-body></ac:structured-macro><p><span style="color:var(--ds-text,#333333);">This REST API request specifies values for a provided list of simulation variables during simulation.</span></p><p>The following table describes the parameters used in the REST API request:</p><table class="relative-table" style="width: 80.362%;"><colgroup class=""><col class="" style="width: 15.9836%;" /><col class="" style="width: 9.15301%;" /><col class="" style="width: 15.3005%;" /><col class="" style="width: 59.5628%;" /></colgroup><tbody class=""><tr class=""><th>Parameter</th><th>In</th><th>Required or optional</th><th colspan="1">Description</th></tr><tr class=""><td><strong>simulation_id</strong></td><td>path</td><td>required</td><td colspan="1">The ID of the running simulation.</td></tr><tr class=""><td colspan="1"><strong>variables</strong></td><td colspan="1">body</td><td colspan="1">required</td><td colspan="1">The set of simulation variables with values that should be used during the current simulation.</td></tr><tr class=""><td colspan="1"><strong>context</strong></td><td colspan="1">body</td><td colspan="1">optional</td><td colspan="1">The context ID.</td></tr><tr class=""><td colspan="1"><strong>propertyPath</strong></td><td colspan="1">body</td><td colspan="1">optional</td><td colspan="1">The property path of the context specified using property names or IDs.</td></tr></tbody></table><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="712965be-4275-43b3-9bf2-3a8ac204cf29"><ac:parameter ac:name="title">Request and response examples</ac:parameter><ac:plain-text-body><![CDATA[/simulation/api/set/ce8c8215-0515-43fd-9d34-92d1d7a95d87
 
Request body:
{
"variables":
   {
        "propulsion.tank.me": 38,
        "propulsion.thruster.me": 30,
        "telecom.antena.me": 19,
        "telecom.amplifier.me": 8
   }
}]]></ac:plain-text-body></ac:structured-macro><h3><br />Pause simulation</h3><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="78ce9449-914a-4df6-8285-dbfc5220448b"><ac:parameter ac:name="borderColor">lightgrey</ac:parameter><ac:parameter ac:name="borderWidth">1</ac:parameter><ac:parameter ac:name="borderStyle">solid</ac:parameter><ac:rich-text-body><p><span style="color:var(--ds-text,#172b4d);">POST /simulation/api/pause/<span style="color:var(--ds-background-accent-orange-bolder,#c25100);">&lt;simulation_id&gt;</span></span></p></ac:rich-text-body></ac:structured-macro><p><br />This REST API request <span style="color:var(--ds-text,#172b4d);">pauses the execution of the specified simulation.</span></p><p>The following table describes the parameters used in the REST API request:</p><table class="relative-table" style="width: 80.362%;"><colgroup class=""><col class="" style="width: 15.9836%;" /><col class="" style="width: 9.15301%;" /><col class="" style="width: 15.3005%;" /><col class="" style="width: 59.5628%;" /></colgroup><tbody class=""><tr class=""><th>Parameter</th><th>In</th><th>Required or optional</th><th colspan="1">Description</th></tr><tr class=""><td><strong>simulation_id</strong></td><td>path</td><td>required</td><td colspan="1">The ID of the running simulation.</td></tr></tbody></table><h3><br />Resume simulation</h3><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="0f2007e1-18da-427c-a387-aac78989a3c3"><ac:parameter ac:name="borderColor">lightgrey</ac:parameter><ac:parameter ac:name="borderWidth">1</ac:parameter><ac:parameter ac:name="borderStyle">solid</ac:parameter><ac:rich-text-body><p>POST /simulation/api/resume/<span style="color:var(--ds-background-accent-orange-bolder,#c25100);">&lt;simulation_id&gt;</span></p></ac:rich-text-body></ac:structured-macro><p><span style="color:var(--ds-text,#172b4d);"><br />This REST API request resumes the execution of the specified simulation.</span></p><p>The following table describes the parameters used in the REST API request:</p><table class="relative-table" style="width: 80.362%;"><colgroup class=""><col class="" style="width: 15.9836%;" /><col class="" style="width: 9.15301%;" /><col class="" style="width: 15.3005%;" /><col class="" style="width: 59.5628%;" /></colgroup><tbody class=""><tr class=""><th>Parameter</th><th>In</th><th>Required or optional</th><th colspan="1">Description</th></tr><tr class=""><td><strong>simulation_id</strong></td><td>path</td><td>required</td><td colspan="1">The ID of the running simulation.</td></tr></tbody></table><h3><br />Get simulation results</h3><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="5fa89bd5-1cca-464f-aed2-98bc012e3f27"><ac:parameter ac:name="borderColor">lightgrey</ac:parameter><ac:parameter ac:name="borderWidth">1</ac:parameter><ac:parameter ac:name="borderStyle">solid</ac:parameter><ac:rich-text-body><p>GET /simulation/api/result/<span style="color:var(--ds-background-accent-orange-bolder,#c25100);">&lt;simulation_id&gt;</span></p></ac:rich-text-body></ac:structured-macro><p><br />This REST API request returns the results of the specified simulation. You can specify what output parameters should be returned in the run REST API body. If output parameters are not specified, all output parameters are obtained. T<span style="color:var(--ds-text,#172b4d);">he verification results are returned based on the value of the<span> </span></span>verification<span style="color:var(--ds-text,#172b4d);"> parameter of the Run Simulation endpoint. </span>I<span style="color:var(--ds-text,#333333);">f the CSV export is specified for the Simulation Configuration, the CSV export results are returned in JSON format. I<span style="color:var(--ds-text,#172b4d);">f a Time Series or Timeline chart is specified for the Simulation Configuration, the chart data is returned in JSON format as well.</span></span></p><p><span style="color:var(--ds-text,#333333);">The figure below demonstrates how to specify input and output parameters.</span></p><p><br /></p><p><ac:image ac:align="center"><ri:attachment ri:filename="specifying_input_output_parameters.png" /></ac:image></p><h6 style="text-align: center;">Specifying input and output parameters.</h6><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="9a790cef-87af-44d5-995a-875e60cba61f"><ac:rich-text-body><ul><li data-uuid="05747173-c645-48c0-8abd-0810fe2e40f2">Output parameters can be the parameters with the data type, primitive type, or enumeration type.</li><li data-uuid="ffd8c764-95ab-4cb2-89d2-07544b7b508b">If the OutputParameters tag of the executed Simulation Configuration is specified, the results are provided according to the OutputParameters tag value.</li></ul></ac:rich-text-body></ac:structured-macro><p><br />The following table describes the parameters used in the REST API request:</p><table class="relative-table" style="width: 80.362%;"><colgroup class=""><col class="" style="width: 15.9836%;" /><col class="" style="width: 9.15301%;" /><col class="" style="width: 15.3005%;" /><col class="" style="width: 59.5628%;" /></colgroup><tbody class=""><tr class=""><th>Parameter</th><th>In</th><th>Required or optional</th><th colspan="1">Description</th></tr><tr class=""><td><strong>simulation_id</strong></td><td>path</td><td>required</td><td colspan="1">The ID of the running simulation.</td></tr></tbody></table><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="2e11d3cc-8453-4f28-9fc1-c0b01d0ccf03"><ac:parameter ac:name="title">Request and response examples</ac:parameter><ac:plain-text-body><![CDATA[/simulation/api/results/ce8c8215-0515-43fd-9d34-92d1d7a95d87

{
 "outputs": {
 "me": 98.0,
 "propulsion.me": 68.0,
 "propulsion.tank.me": 38.0,
 "propulsion.thruster.me": 30.0,
 "telecom.me": 30.0,
 "telecom.antenna.me": 10.0,
 "telecom.amplifier.me": 20.0
 },
 "csv exports": {
 "'SpaceCraftResults'": "me,propulsion.me,propulsion.tank.me,propulsion.thruster.me,telecom.me,telecom.amplifier.me,telecom.antenna.me\n98.0000,68.0000,38.0000,30.0000,30.0000,20.0000,10.0000\n98.0000,68.0000,38.0000,30.0000,30.0000,20.0000,10.0000\n98.0000,68.0000,38.0000,30.0000,30.0000,20.0000,10.0000\n"
 }
}

/simulation/api/results/309c8e47-4bdc-49be-b10a-aeacd9697584
 
{'outputs': {'requiredStoppingDistance': 49.09927575033121,
  'stoppingDistance': 36.32807361129315},
 'verification': [{'property': 'brakeLifeExpectancy',
   'status': 'fail',
   'value': 56413.07910758578,
   'requirements': [{'id': '3',
     'text': 'Brake pads shall have a projected life of at least 57500 kilometers under normal driving conditions, as per industry standard assumptions.',
     'constraint': 'brakeLifeExpectancy>=57500',
     'status': 'fail',
     'margin': -1086.92089241422,
     'timestamp': 0}]},
  {'property': 'wheel.brake.rotor.outerDiameter',
   'status': 'fail',
   'value': 0.25,
   'requirements': [{'id': '6',
     'text': 'The brake rotors shall have a 0.28 meter diameter.',
     'constraint': 'outerDiameter==0.28',
     'status': 'fail',
     'margin': -0.03,
     'timestamp': 0}]}]}]]></ac:plain-text-body></ac:structured-macro><h3><strong><br /></strong>Get the list of running simulations</h3><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="f48fd9b2-c2cd-4a77-9269-fa90bc0ce769"><ac:parameter ac:name="borderColor">lightgrey</ac:parameter><ac:parameter ac:name="borderWidth">1</ac:parameter><ac:parameter ac:name="borderStyle">solid</ac:parameter><ac:rich-text-body><p>GET /simulation/api/running</p></ac:rich-text-body></ac:structured-macro><p><br />This REST API request gets the list of all currently running simulations including the queued simulations that are placed in a waiting line.<br /><br /></p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="fbe59115-f65b-4839-a181-4c2da22ec377"><ac:parameter ac:name="title">Request and response examples</ac:parameter><ac:plain-text-body><![CDATA[/simulation/api/running

{
  "running": [
    "f5c574a8-cd9c-4dbd-aae4-b1d18f048721",
    "ac1afe0a-c093-4eb1-865e-081c381d7f9f"
  ],
  "queued": [
    "ee99c51f-a8e8-40a4-a109-8f97aa579a33",
    "7c92a019-08b5-49bd-8c67-874613dcc1ae",
    "67840dbf-2071-4408-be76-8027e8a7aa48"
  ]
}]]></ac:plain-text-body></ac:structured-macro><h3><strong><br /></strong>Terminate simulation</h3><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="10d35be0-4043-4f1c-b234-fa9e02269345"><ac:parameter ac:name="borderColor">lightgrey</ac:parameter><ac:parameter ac:name="borderWidth">1</ac:parameter><ac:parameter ac:name="borderStyle">solid</ac:parameter><ac:rich-text-body><p>POST /simulation/api/terminate/<span style="color:var(--ds-background-accent-orange-bolder,#c25100);">&lt;simulation_id&gt;</span></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br />This REST API request terminates the specified simulation.</p><p>The following table describes the parameters used in the REST API request:</p><table class="relative-table" style="width: 78.4421%;"><colgroup class=""><col class="" style="width: 17.4248%;" /><col class="" style="width: 9.30721%;" /><col class="" style="width: 16.795%;" /><col class="" style="width: 56.4731%;" /></colgroup><tbody class=""><tr class=""><th>Parameter</th><th>In</th><th>Required or optional</th><th colspan="1">Description</th></tr><tr class=""><td><strong>simulation_id</strong></td><td>path</td><td>required</td><td colspan="1">The ID of a specific simulation.</td></tr></tbody></table><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="d94aaf10-bede-4bb1-8f1e-0a912c229c3a"><ac:parameter ac:name="title">Request and response examples</ac:parameter><ac:plain-text-body><![CDATA[/simulation/api/terminate/4e35bc60-2c66-48e8-96e2-80f5270c08cf

/simulation/api/status/4e35bc60-2c66-48e8-96e2-80f5270c08cf

{
 "state": "TERMINATED",
 "elapsedTime": 11702
}]]></ac:plain-text-body></ac:structured-macro><h3><strong><br /></strong>Check for Simulation Configurations</h3><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="6976f825-9a6a-4be0-9d1f-826331173230"><ac:parameter ac:name="borderColor">lightgrey</ac:parameter><ac:parameter ac:name="borderWidth">1</ac:parameter><ac:parameter ac:name="borderStyle">solid</ac:parameter><ac:rich-text-body><p>GET /simulation/api/hasConfigs/project/<span style="color:var(--ds-background-accent-orange-bolder,#c25100);">&lt;project&gt;</span>/version/<span style="color:var(--ds-background-accent-orange-bolder,#c25100);">&lt;version&gt;</span>/branch/<span style="color:var(--ds-background-accent-orange-bolder,#c25100);">&lt;branch&gt;</span></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br />This REST API request checks if the project has any Simulation Configurations.</p><p>The following table describes the parameters used in the REST API request:</p><table class="relative-table" style="width: 78.2227%;"><colgroup class=""><col class="" style="width: 17.7544%;" /><col class="" style="width: 8.07018%;" /><col class="" style="width: 17.4035%;" /><col class="" style="width: 56.7719%;" /></colgroup><tbody class=""><tr class=""><th>Parameter</th><th>In</th><th>Required or optional</th><th>Description</th></tr><tr class=""><td><strong>project</strong></td><td>path</td><td>required</td><td>The Teamwork Cloud project name or ID.</td></tr><tr class=""><td><strong>version</strong></td><td>path</td><td>optional</td><td>The Teamwork Cloud project version.</td></tr><tr class=""><td><strong>branch</strong></td><td>path</td><td>optional</td><td>The project branch name or ID. If the branch is omitted, the trunk is used instead.</td></tr></tbody></table><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="b93a6dcd-9313-4e7f-9bc3-efbfc694747e"><ac:parameter ac:name="title">Request and response examples</ac:parameter><ac:plain-text-body><![CDATA[/simulation/api/hasConfigs/project/SpacecraftMassRollup

{
 "hasConfigs": true
}]]></ac:plain-text-body></ac:structured-macro><h3><br />Get Simulation Configurations</h3><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="be5a29fe-f5e9-4026-ac0e-b3ceb34d836f"><ac:parameter ac:name="borderColor">lightgrey</ac:parameter><ac:parameter ac:name="borderWidth">1</ac:parameter><ac:parameter ac:name="borderStyle">solid</ac:parameter><ac:rich-text-body><p>GET /simulation/api/configs/project/<span style="color:var(--ds-background-accent-orange-bolder,#c25100);">&lt;project&gt;</span>/version/<span style="color:var(--ds-background-accent-orange-bolder,#c25100);">&lt;version&gt;</span>/branch/<span style="color:var(--ds-background-accent-orange-bolder,#c25100);">&lt;branch&gt;</span>/element/<span style="color:var(--ds-background-accent-orange-bolder,#c25100);">&lt;element&gt;</span></p></ac:rich-text-body></ac:structured-macro><p><br />This REST API request retrieves element IDs, names, and descriptions of the Simulation Configurations available for the given executable element.</p><p>If the executable element is an Instance Specification, the method returns the following Simulation Configurations:</p><ul><li data-uuid="177f56da-8682-423a-9faa-eea7420924cb">Whose execution target is the classifier of the executable element.</li><li data-uuid="49a9a874-a7e8-4e98-9b18-9060d24245b7">Whose execution target is the Instance Specification having at least one classifier matching those of the executable element.</li></ul><p>The following table describes the parameters used in the REST API request:</p><table class="relative-table" style="width: 77.3999%;"><colgroup class=""><col class="" style="width: 17.6596%;" /><col class="" style="width: 9.57447%;" /><col class="" style="width: 17.305%;" /><col class="" style="width: 55.461%;" /></colgroup><tbody class=""><tr class=""><th>Parameter</th><th>In</th><th>Required or optional</th><th colspan="1">Description</th></tr><tr class=""><td><strong>project</strong></td><td>path</td><td>required</td><td colspan="1">The Teamwork Cloud project name or ID.</td></tr><tr class=""><td colspan="1"><strong>version</strong></td><td colspan="1">path</td><td colspan="1">optional</td><td colspan="1">The Teamwork Cloud project version.</td></tr><tr class=""><td><strong>branch</strong></td><td>path</td><td>optional</td><td colspan="1">The project branch name or ID. If the branch is omitted, the trunk is used instead.</td></tr><tr class=""><td><strong>element</strong></td><td>path</td><td>optional</td><td colspan="1">The qualified name or server ID of the element to be executed.</td></tr><tr class=""><td colspan="1"><strong>?filter</strong></td><td colspan="1">query</td><td colspan="1">optional</td><td colspan="1"><p><span style="color:var(--ds-text,#172b4d);">Returns Simulations Configurations with a specified UI tag for a particular project. The only possible value for the <strong>filter</strong> parameter is <strong>ui</strong>.</span></p><p><span style="color:var(--ds-text,#172b4d);">Only Simulations Configurations having at least one of the following UI elements are returned:</span></p><ul><li data-uuid="3f4838e1-0bfc-4ba4-964f-730f3e0dd185"><span style="color:var(--ds-text,#172b4d);">Frame</span></li><li data-uuid="e0ca7463-47ed-46da-877e-59458fb98baa"><span style="color:var(--ds-text,#172b4d);">Table</span></li><li data-uuid="3e27220c-0c58-466d-9e49-3f354cc8d6aa"><span style="color:var(--ds-text,#172b4d);">TimeSeries chart</span></li><li data-uuid="de0dd4bb-50ef-485c-a5fe-5f5401f37cbd"><span style="color:var(--ds-text,#172b4d);">Timeline chart</span></li></ul></td></tr></tbody></table><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="2e91bf46-3ed3-466d-8916-2d86db4a7f99"><ac:parameter ac:name="title">Request and response examples</ac:parameter><ac:plain-text-body><![CDATA[/simulation/api/configs/project/SpacecraftMassRollup

{
 "id": "7915fcfa-fd88-4910-8560-13f4439cec3d",
 "name": "spacecraft mass analysis",
 "description": ""
 }]]></ac:plain-text-body></ac:structured-macro><h3><br />Get Simulation Configuration descriptor</h3><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="ef91ca01-06a7-498f-b1e4-190dbde5f595"><ac:parameter ac:name="borderColor">lightgrey</ac:parameter><ac:parameter ac:name="borderWidth">1</ac:parameter><ac:parameter ac:name="borderStyle">solid</ac:parameter><ac:rich-text-body><p>GET simulation/api/descriptor/project/<span style="color:var(--ds-background-accent-orange-bolder,#c25100);">&lt;project&gt;</span>/version/<span style="color:var(--ds-background-accent-orange-bolder,#c25100);">&lt;version&gt;</span>/branch/<span style="color:var(--ds-background-accent-orange-bolder,#c25100);">&lt;branch&gt;</span>/config/<span style="color:var(--ds-background-accent-orange-bolder,#c25100);">&lt;config&gt;</span></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /><span style="color:var(--ds-text,#333333);"><span style="color:var(--ds-text,#172b4d);">This REST API request retrieves Simulation Configuration data (description, execution target,<span> </span></span>time step,<span style="color:var(--ds-text,#172b4d);"><span> </span>input and output parameters) from the specified project.</span> The</span><span style="color:var(--ds-text,#333333);"> set of input and output parameters is specified using the <strong>Input Parameters</strong> and <strong>Output Parameters</strong> properties of a Simulation Configuration. </span><span style="color:var(--ds-text,#333333);">The figure below demonstrates how to specify input and output parameters.</span></p><p><br /></p><p><ac:image ac:align="center"><ri:attachment ri:filename="specifying_input_output_parameters.png" /></ac:image></p><h6 style="text-align: center;">Specifying input and output parameters.</h6><p>The following table describes the parameters used in the REST API request:</p><table class="relative-table" style="width: 77.3999%;"><colgroup class=""><col class="" style="width: 17.6596%;" /><col class="" style="width: 9.57447%;" /><col class="" style="width: 17.305%;" /><col class="" style="width: 55.461%;" /></colgroup><tbody class=""><tr class=""><th>Parameter</th><th>In</th><th>Required or optional</th><th colspan="1">Description</th></tr><tr class=""><td><strong>project</strong></td><td>path</td><td>required</td><td colspan="1">The Teamwork Cloud project name or ID.</td></tr><tr class=""><td colspan="1"><strong>version</strong></td><td colspan="1">path</td><td colspan="1">optional</td><td colspan="1">The Teamwork Cloud project version.</td></tr><tr class=""><td><strong>branch</strong></td><td>path</td><td>optional</td><td colspan="1">The project branch name or ID. If the branch is omitted, the trunk is used instead.</td></tr><tr class=""><td><strong>config</strong></td><td>path</td><td>optional</td><td colspan="1">The Simulation Configuration name or server ID.</td></tr></tbody></table><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="ad182cfe-3321-4b09-8c7a-a8b71cc17c34"><ac:parameter ac:name="title">Request and response examples</ac:parameter><ac:plain-text-body><![CDATA[simulation/api/descriptor/project/SpacecraftMassRollup/config/spacecraft mass analysis


{'config': 'spacecraft mass analysis',
 'description': 'Simulation Config that is dedicated to run spacecraft mass rollup.',
 'model': 'spacecraft',
 'parameters': {'inputs': [{'parameter': 'telecom.amplifier.me',
    'value': 32.0,
    'type': 'mass[kilogram]',
    'unit': 'kilogram',
    'requirements': [{'id': '1',
      'text': 'Estimated mass shall be less than allocated mass'}]},
   {'parameter': 'telecom.antenna.me',
    'value': 32.0,
    'type': 'mass[kilogram]',
    'unit': 'kilogram',
    'requirements': [{'id': '1',
      'text': 'Estimated mass shall be less than allocated mass'}]},
   {'parameter': 'propulsion.tank.me',
    'value': 68.0,
    'type': 'mass[kilogram]',
    'unit': 'kilogram',
    'requirements': [{'id': '1',
      'text': 'Estimated mass shall be less than allocated mass'}]},
   {'parameter': 'propulsion.thruster.me',
    'value': 68.0,
    'type': 'mass[kilogram]',
    'unit': 'kilogram',
    'requirements': [{'id': '1',
      'text': 'Estimated mass shall be less than allocated mass'}]}],
  'outputs': [{'parameter': 'telecom.me',
    'value': 32.0,
    'type': 'mass[kilogram]',
    'unit': 'kilogram',
    'requirements': [{'id': '1',
      'text': 'Estimated mass shall be less than allocated mass'}]},
   {'parameter': 'propulsion.me',
    'value': 68.0,
    'type': 'mass[kilogram]',
    'unit': 'kilogram',
    'requirements': [{'id': '1',
      'text': 'Estimated mass shall be less than allocated mass'}]},
   {'parameter': 'me',
    'value': 95.0,
    'type': 'mass[kilogram]',
    'unit': 'kilogram',
    'requirements': [{'id': '1',
      'text': 'Estimated mass shall be less than allocated mass'}]}]}}


simulation/api/descriptor/project/BouncingBall/config/Run BouncingBall


{'config': 'Run BouncingBall',
 'description': 'Simulation Config dedicated to run simulation with bouncingBall.fmu.',
 'model': 'bouncingBall',
 'timeStep': '10 ms' 
 }]]></ac:plain-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=249571231 space=MMA version=3 -->
## PAGE 00720: Simulation with UI

- page_id: `249571231`
- space_key: `MMA`
- source_url: https://docs.nomagic.com/spaces/MMA/pages/249571231/Simulation+with+UI
- version_number: 3
- version_date: `2025-09-15T15:45:29.351+02:00`
- ancestors: Magic Model Analyst / Cameo Simulation Toolkit Documentation > User Guide > Server-side simulation
- labels: []

### NORMALIZED CONTENT

When simulating a model with aUI mockup, Time Series Chart, Timeline Chart, or HTML Table, you can open a UI or index UI window during model execution. These windows display all UI elements of the executed Simulation Configuration and have a control panel allowing you to start, pause, resume, or terminate the simulation. The benefit of using an index UI window is that it allows you to reorder and resize each individual UI since they are displayed in separate boxes, as shown below.

[IMAGE alt='' src='']

###### A UI index window where you can reorder and resize all existing UIs.

To run the server-side simulation with UI

1. In your modeling tool, open the User Interface Modeling Diagram where the relevant UI elements are displayed.
2. In the diagram toolbar, click [ATTACHMENT filename='generate_HTML_button.png'] and select Generate and Attach HTML . For more information see [CONFLUENCE_PAGE title='Auto-generating HTML files' space=''] .
3. Commit the changes to Teamwork Cloud .
4. Run the simulation on the server in one of the following ways:
  - Run the simulation using [CONFLUENCE_PAGE title='Simulation using REST API' space=''] or [CONFLUENCE_PAGE title='Simulation using Jupyter Notebook' space=''] , then open the index UI window by doing the following:
    1. Check the simulation status.
    2. Go to the URL given as the 'indexUI' in the response of the status request to open the index UI window containing all UI elements of the executed Simulation Configuration. To open each UI element of the executed Simulation Configuration separately, go to the URLs given under 'ui' in the response of the status request.
  - [CONFLUENCE_PAGE title='Simulation in the Resources application' space=''] , then open the index UI window by clicking Open in the pop-up message or using the [CONFLUENCE_PAGE title='Managing active simulations' space=''] .
  - [CONFLUENCE_PAGE title='Simulation in Cameo Collaborator for Teamwork Cloud' space=''], then open the index UI window by clicking **Open** in the pop-up message or using the [CONFLUENCE_PAGE title='Managing active simulations' space=''].

#### NOTE: Saving Time Series and Time Line Chart data

Saving Time Series and Time Line Chart data

Time Series and Timeline Chart data is exported to HTML/CSV and stored in the **Documentation** property of the result Instance Specification when all of these conditions are met:

- Simulation Configuration has an assigned Time Series or Timeline Chart, in which the [CONFLUENCE_PAGE title='Saving plot results to the model' space='']**recordPlotDataAs** tag is set to HTML/CSV, and the resultFile tag is empty.
- Simulation Configuration has a specified [CONFLUENCE_PAGE title='Saving plot results to the model' space='']**resultLocation** tag .
- Server-side simulation is run with the [CONFLUENCE_PAGE title='Simulation using REST API' space='']**?commitResults** parameter set to True .

##### Supported UI types

During server-side simulation, you can open the following UI types:

- UI Mockups including Frame, embedded Widgets, and Image Switcher. [ATTACHMENT filename='ui_with_widgets.png']
- **Timeline Charts**displaying Activity and State plots. Numeric, boolean, and enumeration value plots cannot be displayed. In addition, Requirements and Constraint failures are not annotated. Timeline Charts do not need to be generated and attached to a Teamwork Cloud project. [IMAGE alt='' src='']
- **Time Series Charts**which areupdated in real-time during simulation. Note that Requirements and Constraint failures are not annotated in Time Series Charts. Timeseries Charts do not need to be generated and attached to a Teamwork Cloud project. [IMAGE alt='' src='']
- Tables created in a User Interface Modeling Diagram. [CONFLUENCE_PAGE title='Generating an HTML table from a UI table, Time series chart, and CSV export configuration' space='']. [IMAGE alt='' src='']
- **Animated Diagrams**which are updated in real-time during simulation. [CONFLUENCE_PAGE title='Diagram Animation on HTML UI' space=''] 
 
[IMAGE alt='' src=''] Structured diagrams with nested property paths are not supported.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><span style="color:var(--ds-text,#172b4d);">When simulating a model with a<span> </span></span><span style="color:var(--ds-text,#333333);">UI mockup, Time Series Chart</span><span style="color:var(--ds-text,#172b4d);">, Timeline Chart, or HTML Table, you can open a UI or index UI window during model execution. These windows display all UI elements of the executed Simulation Configuration and have a control panel allowing you to start, pause, resume, or terminate the simulation. The benefit of using an index UI window is that it allows you to reorder and resize each individual UI since they are displayed in separate boxes, as shown below.</span></p><p><br /></p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="Coffee Machine.png" /></ac:image></p><h6 style="text-align: center;">A UI index window where you can reorder and resize all existing UIs.</h6><p><br /></p><p>To run the server-side simulation with UI</p><hr /><ol><li>In your modeling tool, open the User Interface Modeling Diagram where the relevant UI elements are displayed.</li><li>In the diagram toolbar, click <ac:image ac:thumbnail="true" ac:height="20"><ri:attachment ri:filename="generate_HTML_button.png" /></ac:image> and select <strong>Generate and Attach HTML</strong>. For more information see <ac:link ac:anchor="Generating and attaching HTML files to Teamwork Cloud projects"><ri:page ri:content-title="Auto-generating HTML files" /><ac:plain-text-link-body><![CDATA[Auto-generating HTML files]]></ac:plain-text-link-body></ac:link>.</li><li><a href="https://docs.nomagic.com/CM/?contextKey=committing-changes-to-teamwork-cloud&amp;version=latest">Commit the changes to Teamwork Cloud</a>.</li><li>Run the simulation on the server in one of the following ways:<ul><li>Run the simulation using <ac:link><ri:page ri:content-title="Simulation using REST API" /><ac:plain-text-link-body><![CDATA[REST API]]></ac:plain-text-link-body></ac:link> or <ac:link><ri:page ri:content-title="Simulation using Jupyter Notebook" /><ac:plain-text-link-body><![CDATA[Jupiter Notebook]]></ac:plain-text-link-body></ac:link>, then open the index UI window by doing the following:<ol><li>Check the simulation status.</li><li><p class="auto-cursor-target">Go to the URL given as the 'indexUI' in the response of the status request to open the index UI window containing <span style="color:var(--ds-text,#172b4d);">all UI elements of the executed Simulation Configuration</span>.</p><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="4b94e1f8-ecfb-4319-926a-9b2c5bd5993f"><ac:rich-text-body><p>To open each UI element of the executed Simulation Configuration separately, go to the URLs given under 'ui' in the response of the status request.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></li></ol></li><li><ac:link><ri:page ri:content-title="Simulation in the Resources application" /><ac:plain-text-link-body><![CDATA[Run the simulation in the Resources application]]></ac:plain-text-link-body></ac:link>, then open the index UI window by clicking <strong>Open</strong> in the pop-up message or using the <ac:link><ri:page ri:content-title="Managing active simulations" /><ac:plain-text-link-body><![CDATA[Task Manager]]></ac:plain-text-link-body></ac:link>. </li><li><p><ac:link><ri:page ri:content-title="Simulation in Cameo Collaborator for Teamwork Cloud" /><ac:plain-text-link-body><![CDATA[Run the simulation in Cameo Collaborator for Teamwork Cloud]]></ac:plain-text-link-body></ac:link>, then open the index UI window by clicking <strong>Open</strong> in the pop-up message or using the <ac:link><ri:page ri:content-title="Managing active simulations" /><ac:plain-text-link-body><![CDATA[Task Manager]]></ac:plain-text-link-body></ac:link>. </p><p class="auto-cursor-target"><br /></p></li></ul></li></ol><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="9ab4c44e-0237-46a0-87fc-078ea7aebea5"><ac:parameter ac:name="title">Saving Time Series and Time Line Chart data</ac:parameter><ac:rich-text-body><p style="text-align: left;">Time Series and Timeline Chart data is exported to HTML/CSV and stored in the <strong>Documentation</strong> property of the result Instance Specification when all of these conditions are met: </p><ul style="text-align: left;"><li>Simulation Configuration has an assigned Time Series or Timeline Chart, in which the <ac:link><ri:page ri:content-title="Saving plot results to the model" /><ac:link-body><strong>recordPlotDataAs</strong> tag</ac:link-body></ac:link> is set to HTML/CSV, and the <strong>resultFile</strong> tag is empty.</li><li>Simulation Configuration has a specified <ac:link><ri:page ri:content-title="Saving plot results to the model" /><ac:link-body><strong>resultLocation</strong> tag</ac:link-body></ac:link>. </li><li>Server-side simulation is run with the <ac:link ac:anchor="Run simulation"><ri:page ri:content-title="Simulation using REST API" /><ac:link-body><strong>?commitResults</strong> parameter</ac:link-body></ac:link> set to <em>True</em>.</li></ul></ac:rich-text-body></ac:structured-macro><p><br /></p><h3>Supported UI types</h3><p>During server-side simulation, you can open the following UI types:</p><ul><li><strong>UI Mockups</strong> including Frame, embedded Widgets, and Image Switcher.<br /><br /><ac:image><ri:attachment ri:filename="ui_with_widgets.png" /></ac:image><br /><br /></li><li><p><strong>Timeline Charts </strong>displaying Activity and State plots. Numeric, boolean, and enumeration value plots cannot be displayed. In addition, Requirements and Constraint failures are not annotated. </p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="445de28a-364c-46fd-bc94-8d71e6dd1196"><ac:rich-text-body><p>Timeline Charts do not need to be generated and attached to a Teamwork Cloud project.</p></ac:rich-text-body></ac:structured-macro><p><ac:image><ri:attachment ri:filename="timeline_chart.png" /></ac:image><br /><br /></p></li><li><p><strong>Time Series Charts</strong><span> which are </span><span style="color:var(--ds-text,#172b4d);">updated in real-time during simulation. Note that Requirements and Constraint failures are not annotated in Time Series Charts.<br /></span></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="603926f3-3f26-4c55-bae4-9433dabeda1b"><ac:rich-text-body><p>Timeseries Charts do not need to be generated and attached to a Teamwork Cloud project.</p></ac:rich-text-body></ac:structured-macro><p><ac:image><ri:attachment ri:filename="time_series_chart.png" /></ac:image><br /><br /></p></li><li><strong>Tables</strong> created in a <span style="color:var(--ds-text,#333333);">User Interface Modeling Diagram. <ac:link><ri:page ri:content-title="Generating an HTML table from a UI table, Time series chart, and CSV export configuration" /><ac:plain-text-link-body><![CDATA[Learn how to Create UI tables that can be viewed as HTML in an internet browser]]></ac:plain-text-link-body></ac:link>.</span><br /><strong><br /><ac:image><ri:attachment ri:filename="html_table.png" /></ac:image><br /><br /></strong></li><li><p class="auto-cursor-target"><strong>Animated Diagrams </strong>which are updated in real-time during simulation. <ac:link><ri:page ri:content-title="Diagram Animation on HTML UI" /><ac:plain-text-link-body><![CDATA[Learn which diagram types are supported and how to create a UI Mockup with a diagram.]]></ac:plain-text-link-body></ac:link><br /><br /><ac:image><ri:attachment ri:filename="Server side.png" /></ac:image><br /><br /></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="cda16d9e-15b7-40ce-9318-79bc6f1f6598"><ac:rich-text-body><p>Structured diagrams with nested property paths are not supported.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></li></ul>
````

<!--NOMAGIC_PAGE id=249569663 space=MMA version=10 -->
## PAGE 00721: SimulationConfig stereotype

- page_id: `249569663`
- space_key: `MMA`
- source_url: https://docs.nomagic.com/spaces/MMA/pages/249569663/SimulationConfig+stereotype
- version_number: 10
- version_date: `2026-01-20T07:55:53.102+01:00`
- ancestors: Magic Model Analyst / Cameo Simulation Toolkit Documentation > User Guide > Simulation Configuration and UI modeling
- labels: ['simulationconfig-stereotype', 'initializing-references']

### NORMALIZED CONTENT

**On this page**

33

Magic Model Analyst / Cameo Simulation Toolkit provides a model-based execution configuration through the *«stereotype» SimulationConfig*. You can configure the stereotypes in the Specification window of «SimulationConfig». The following figure shows the «SimulationConfig» and the SimulationConfig stereotypes

To show up the «SimulationConfig» and the SimulationConfig stereotype

1. Right-click a Package in the Containment tree in a simulation project and select Create Diagram > Simulation Configuration Diagram, which is the SimulationProfile stereotype applied.
2. Right-click the SimulationProfile [SimulationProfile.mdzip] stereotype in the Containment tree and select Config > SimulationConfig [Class] and drag the Class to the diagram pane.

[IMAGE alt='' src='']

###### The «SimulationConfig» and its «stereotype».

The *SimulationConfig «stereotype»* contains tag definitions. You can sort these tag definitions alphabetically by right-clicking them and selecting **Symbol Properties** > **Attributes Sort Mode** > **By Name**. Click the *«SimulationConfig»* to open its Specification window and see all of the tag definitions.

| Tag definition | Description |  |
| --- | --- | --- |
| UI | A user interface for configuration mockups that will start with a model simulation. |  |
| silent | If the value is true, the simulation will run without animation or idle time. |  |
| executionTarget | An element from which the simulation should start. NoteYou can drag any element that can be simulated to a Simulation Configuration to set the executionTarget for the dragged element. |  |
| excludedElement | A list of elements that will be excluded and not instantiated if not ready to be used or not needed, e.g., Class, Package, Use Case, Actor, Behavior, Connector, Port, and State. See also in . |  |
| log | An element in which the execution trace will be recorded. |  |
| resultLocation | A Package, a Model, InstanceSpecification, or an InstanceTable in which a context object will be stored after simulation.If the resultLocation is specified by an InstanceSpecification, the values of the context object will be saved as slot values of the specified InstanceSpecification. Not applicable when executionTarget is a table.If the resultLocation is specified by a Package or a Model, Magic Model Analyst / Cameo Simulation Toolkit will create a new InstanceSpecification owned by the Package or the Model after the simulation. The values of the context object will then be saved as slot values of the created InstanceSpecification. If the resultLocation is specified by an InstanceTable, a new result instance will be created and added as a new row with only the visible columns of the table. However, if the executionTarget and the resultLocation are the same InstanceTable, the result instance will be updated instead (only visible columns of the table). See also the Instance Table in the modeling tool User Guide.NoteThe following elements will not be savedInstanceTable without the Classifier set.Nested instances inside slots.If the resultLocation is not specified, the simulation results will not be saved, except if executionTarget is a table, then instances will be updated in the same table. |  |
| enginesPriority | Allows specifying execution engine priority and availability for a particular execution. The first engine on the list has the highest priority. If the Simulation Configuration does not have a tagged value for this tag definition, Magic Model Analyst / Cameo Simulation Toolkit will use the values that are defined in the registered Simulation Engine Priority in the dialog. |  |
| allowConcurrentAllocatedActivities | If set to true, Activities can be executed in parallel even if the allocated resource is busy. If set to false, only one allocated Activity is executed for an object represented in an Activity Partition. |  |
| autoStart | If true, a model simulation starts running automatically once it has been initialized. Otherwise, you must click the Start button in the Simulation pane to run the simulation.NoteFor Monte Carlo Simulation and Table Simulation, the conditions are as follows:If true, the simulation will be initialized, solve parametric, start Behaviors, wait for Behaviors terminated or when endTime is reached, and terminate. Those Behaviors are Blocks with Classifier Behaviors and/or Part Property with Behaviors. If endTime is less than the time of part Behaviors, e.g., duration constraints are applied, the time of each iteration will be endTime. However, when endTime is more than the time of part Behaviors, all part Behaviors will be completed just once.If false, the simulation will be initialized, solve parametric, and terminate. Behaviors will not be started. |  |
| clock ratio | A ratio between a simulation clock and a real-time clock (1:10). For example, if the clock ratio is 10, it means that one second on the simulation clock is equal to 10 seconds on the real-time clock. |  |
| autostartActiveObjects | If the value is true, the runtime objects whose classifier is active will start their behavior automatically in an asynchronous mode. Otherwise, their behavior will start using a startObjectBehaviorAction. |  |
| executionListeners | A list of execution listeners that will receive events from a model simulation. An execution listener can be a SequenceDiagramGeneratorConfig. |  |
| decimalPlaces | Decimal places of all displayed numerical values in a model simulation, for example, in the Variables pane, Tooltip, and the SimulationConsole pane. Their values must be integers. If the precision of displayed numerical values is greater than or equal to 10% of the absolute value, the numerical values will be displayed in exponential form. |  |
| fireValueChangeEvent | If this value is true, a parametric simulation will be repeated immediately whenever the value of any structural feature changes. Repeating simulation will give an impact on both values carried over by binding connectors and specified in a constraint. |  |
| timeValue | A property that will be used in a model-based clock. If the tagged value is specified, the run-time value specified by the property will be used as the simulation time. |  |
| timeUnit | A unit of a runtime value that specifies the simulation time. If the tagged value is unspecified, the millisecond will be used by default. |  |
| constraintFailureAsBreakpoint | A flag that indicates a simulation will pause at the constraint element where the failure occurs. |  |
| rememberFailureStatus | If true, the failure status will be remembered until the termination, and the first failure status will be recorded with its timestamp as fail, even though it passes at the end. |  |
| durationSimulationMode | Specifies a duration mode of simulation in min, max, average, or random. Magic Model Analyst / Cameo Simulation Toolkit uses the duration mode to calculate the duration of an Action simulation to which a duration constraint is applied. |  |
| treatAllClassifiersAsActive | This option (true by default) runs all Behaviors, including the ones in the subsystems. Even though the isActive property is false, if TreatAllClassifiersAsActive is true, Magic Model Analyst / Cameo Simulation Toolkit will run all of the Behaviors of non-active Classifiers. |  |
| initializeReferences | If true, references will be initialized by creating new objects, instead of referencing the existing parts of the system. See also in . |  |
| startTime | Specifies when simulation will initiate (in integer). |  |
| endTime | The time simulation terminates (in integer). |  |
| stepSize | Increases together with the simulation time (in real numbers or decimal places). |  |
| numberOfSteps | Specifies the number of steps through which the simulation will run. |  |
| numberOfRuns | A number of runs of a particular configuration, especially for the sample size in Monte Carlo simulation. The value must be greater than or equal to 1. Not applicable when executionTarget is a table. |  |
| timeVariableName | This property returns time from the simulation clock (the default value is "simtime"). It returns the time on the simulation clock. |  |
| stepDelay | Specifies how long the delay will be, if any, for each step. |  |
| runForksInParallel | If the value is true or undefined, all outgoing edges from the fork will run in parallel. |  |
| cloneReferences | If true, creates new instances for all objects recursively. Otherwise, it creates instances only for the first level and others remain in their original locations (the default is false). |  |
| Show UI as HTML | If set to true, the HTML UI shall be generated and automatically opened in an embedded browser.If set to false, the Java-based UI shall be automatically opened in an embedded browser. |  |
| terminateStreamingBehaviorsByOutputParameterMultiplicity | If set to true, a streaming Activity terminates when each of its output parameters receives a cumulative number of values equal to the upper bound of the parameter multiplicity. If set to false, a streaming Activity terminates only when forced by the Activity final node or the termination by the Activity that invoked it. |  |
| solveAfterInitialization | If true, automatically starts initial solving. If false, the manual start is required via Refresh in the Variables pane, or press Start (F8). |  |
| animationSpeed | Specifies the animation speed of a particular configuration in percentage. The default value is 95, but you can enter your preferred value from 1 to 100. |  |
| recordTimestamp | If true, the timestamp is recorded into a result instance name.NoteThe naming of the newly created instance will not follow MagicDraw instance naming criteria.If false (by default), MagicDraw instance naming will be used instead, and the timestamp will not be recorded and appended to the instance name. |  |
| autoConvertUnits | If true, values connected via Binding Connector will be recalculated if they have compatible types defined by the QUDV library. |  |
| autoTerminate | If true, the simulation terminates when it is completed or after the initialization phase, if autoStart is set to false. If false, the simulation continues without termination, hanging at the end or after the initialization phase, if autoStart is set to false.The default setting for this property is undefined, allowing the simulation to conclude under normal circumstances. Normal circumstances mean, when the specified end time is reached or when the main behavior finishes.To learn more about how autoStart and autoTerminate tags work in combination, refer to the table below:autoStartautoTerminateResultTrueTrueThe simulation will automatically start and will terminate under normal conditions, such as reaching the specified end time or when the main behavior terminates. Note: A simulation with no main behavior will run until the user manually terminates it.TrueFalseThe simulation will automatically start, but it will not be terminated upon reaching the end time or the conclusion of the main behavior. Instead, the simulation will hang at the end.FalseTrueAfter the initialization phase, the simulation will be terminated.FalseFalseAfter the initialization phase, the simulation will not be terminated. Instead, it will remain in the initialized phase, hanging in that state. However, once the simulation is started, the simulation will hang at the end. |  |
| autoStart | autoTerminate | Result |
| True | True | The simulation will automatically start and will terminate under normal conditions, such as reaching the specified end time or when the main behavior terminates. Note: A simulation with no main behavior will run until the user manually terminates it. |
| True | False | The simulation will automatically start, but it will not be terminated upon reaching the end time or the conclusion of the main behavior. Instead, the simulation will hang at the end. |
| False | True | After the initialization phase, the simulation will be terminated. |
| False | False | After the initialization phase, the simulation will not be terminated. Instead, it will remain in the initialized phase, hanging in that state. However, once the simulation is started, the simulation will hang at the end. |
| showAnnotations | If true, the simulation annotations in the diagrams are enabled. If showAnnotations is set to false, then the following animation features will be affected accordingly:Flowing information will also be disabled.Animation delay will be disabled, thus the animation will run at full speed.The annotation tooltips will be gone since they relate to annotations.On a breakpoint, the annotation will be shown as it is now with silent animation. |  |
| showRuntimeValuesOnPartShapes | If true, the runtime values on Part shapes are displayed instead of the default values. |  |
| showRuntimeValuesOnPortLabels | If true, the runtime values on the Port and Constraint Parameters labels are displayed. |  |
| showFlowingInformation | If true, the label of the flowing item on the path is displayed. If false, only the flow path is highlighted. |  |
| showUnits | If true, unit symbols for runtime values in diagrams and UI mockups are displayed. |  |

##### Initialize References property

The property Initialize References in the Specification window of *«*SimulationConfig» allows Magic Model Analyst / Cameo Simulation Toolkit to initialize all references between objects owned in a composite owner. The following is the Specification window of *«*SimulationConfig» from the [CoffeeMachine.mdzip](https://docs.nomagic.com/display/MT/_sample+models?preview=%2F17664205%2F17664212%2FCoffeeMachine.mdzip) sample.

[IMAGE alt='' src='']

###### Initialize references in the Specification window of «SimulationConfig» Coffee Machine.

#### NOTE: Note

Note

Initialize References appears if you open the Specification window in the **All** or **Expert** Properties mode.

The following are two types of references that you can initialize using the Initialize References option in SimulationConfig

- References between objects created inside a system

This type of reference occurs when you create a project similar to the following example. The following figure shows ***«*block» c** as a root context, **a** is a Part Property, and **b** is both the part and reference properties. The ***«*block c»** contains an Internal Block diagram with a connector line (the type of the connector is association named **a-b**) that connects two part properties **a:a** to**b:b**. The connector specifies that reference property **b**will get the run time object value from Part Property **b**. If there is no connector, an auto-generated value will be given to reference property **b**.

[IMAGE alt='' src='']

###### Initialization of Property.

- References to external objects

If you run a block, for example, the **Variables** pane will show the classifiers of the references. When the InitializeReferences is false, the reference property in the block will not be initialized. When it is true, the reference property will be initialized at run time.

##### Instantiation scope with excluded elements

To control what part of the model is used in simulation, you can use **excludedElement** to exclude and not to instantiate any elements that are not ready to be used or not needed. When any Classifiers, e.g., Classes, Packages, Use Cases, Actors, Behaviors, Connectors, Ports, or States are selected, they will not be instantiated by default instantiation. Excluded Classifiers will not be displayed in the list of types in the **Variables** pane when clicked or right-clicked to select **Add value**. For example, a Part property is set in **excludedElement**, so it will not be instantiated when running a simulation as shown in the figure below. See also in [Automatic instantiation of the implementation Class](https://docs.nomagic.com/display/MMA/Class#Class-AutomaticinstantiationoftheimplementationClass).

[IMAGE alt='' src='']

###### Part property, CPU2, is not instantiated in the Variables pane, since it has been set in excludedElement.

For nested Part properties, **excludedElement** can be set through «SelectPropertiesConfig» as shown in the figure below. You can find the **«SelectPropertiesConfig»** control in the **Simulation Configuration Diagram** toolbar.

[IMAGE alt='' src='']

###### Nested Part property, cache of CPU2, is not instantiated in the Variables pane, since it has been set in excludedElement through «SelectPropertiesConfig».

**Related pages**

- 
- [CONFLUENCE_PAGE title='Simulation log' space='']
- [CONFLUENCE_PAGE title='Simulation time and simulation clock' space='']
- [CONFLUENCE_PAGE title='Automatic start of active objects' space='']
- [CONFLUENCE_PAGE title='UI modeling diagram simulation' space='']
- [CONFLUENCE_PAGE title='ImageSwitcher and ActiveImage' space='']
- [CONFLUENCE_PAGE title='Time Series Chart' space='']
- [CONFLUENCE_PAGE title='Timeline chart' space='']
- [CONFLUENCE_PAGE title='Histogram' space='']
- [CONFLUENCE_PAGE title='Nested UI Configuration stereotype' space='']
- [CONFLUENCE_PAGE title='Reusable UI Mockup' space='']
- 
- [CONFLUENCE_PAGE title='CSV export' space='']
- [CONFLUENCE_PAGE title='Nested property selection for configurations' space='']
- [CONFLUENCE_PAGE title='Instance table' space='MT']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p><strong>On this page</strong></p><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="54a291f8-bb66-42e0-9216-d9b94f4bf6ae"><ac:parameter ac:name="maxLevel">3</ac:parameter><ac:parameter ac:name="minLevel">3</ac:parameter></ac:structured-macro></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p>Magic Model Analyst / Cameo Simulation Toolkit provides a model-based execution configuration through the <em>«stereotype» SimulationConfig</em>. You can configure the stereotypes in the Specification window of «SimulationConfig». The following figure shows the «SimulationConfig» and the SimulationConfig stereotypes</p><p>To show up the «SimulationConfig» and the SimulationConfig stereotype</p><hr /><ol><li data-uuid="b6f3b906-c4e2-4dfe-91f2-fa2008a23a30">Right-click a Package in the Containment tree in a simulation project and select <strong>Create Diagram</strong> &gt; <strong>Simulation Configuration Diagram, </strong>which is the SimulationProfile stereotype applied.</li><li data-uuid="af16b98c-f558-4122-840a-e0b88d3ae92d">Right-click the<em> SimulationProfile [SimulationProfile.mdzip]</em> stereotype in the Containment tree and select <strong>Config &gt; SimulationConfig [Class]</strong> and drag the Class to the diagram pane.</li></ol><p style="text-align: center;"><ac:image><ri:attachment ri:filename="Sim_Config.png" /></ac:image></p><h6 style="text-align: center;">The «SimulationConfig» and its «stereotype».</h6><p>The <em>SimulationConfig «stereotype»</em> contains tag definitions. You can sort these tag definitions alphabetically by right-clicking them and selecting <strong>Symbol Properties</strong> &gt; <strong>Attributes Sort Mode</strong> &gt; <strong>By Name</strong>. Click the <em>«SimulationConfig»</em> to open its Specification window and see all of the tag definitions. </p><table class="wrapped"><colgroup><col style="width: 235.0px;" /><col style="width: 1022.0px;" /></colgroup><tbody><tr><th>Tag definition</th><th>Description</th></tr><tr><td><strong>UI</strong></td><td>A user interface for configuration mockups that will start with a model simulation. </td></tr><tr><td><strong>silent</strong> </td><td>If the value is <em>true</em>, the simulation will run without animation or idle time. </td></tr><tr><td><strong>executionTarget</strong></td><td><div class="content-wrapper"><p>An element from which the simulation should start. </p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="f443eb90-9b6c-4c5e-8b80-f95471b01c88"><ac:parameter ac:name="title">Note</ac:parameter><ac:rich-text-body><p>You can drag any element that can be simulated to a Simulation Configuration to set the <strong>executionTarget</strong> for the dragged element.</p></ac:rich-text-body></ac:structured-macro></div></td></tr><tr><td><strong>excludedElement</strong></td><td>A list of elements that will be excluded and not instantiated if not ready to be used or not needed, e.g., Class, Package, Use Case, Actor, Behavior, Connector, Port, and State. See also in <ac:link ac:anchor="Instantiationscopewithexcludedelements"><ac:plain-text-link-body><![CDATA[Instantiation scope with excluded elements]]></ac:plain-text-link-body></ac:link>.</td></tr><tr><td><strong>log</strong> </td><td>An element in which the execution trace will be recorded.</td></tr><tr><td><strong>resultLocation</strong></td><td><div class="content-wrapper"><p>A <a href="https://docs.nomagic.com/MT/?contextKey=package&amp;version=latest&amp;variant=default">Package</a>, a Model, InstanceSpecification, or an <a href="https://docs.nomagic.com/MT/?contextKey=instance-table&amp;version=latest&amp;variant=default">InstanceTable</a> in which a context object will be stored after simulation.</p><ul><li data-uuid="8c5fed51-a739-44a6-8881-a0a675d0a939">If the <strong>resultLocation</strong> is specified by an<span> </span>InstanceSpecification, the values of the context object will be saved as slot values of the specified InstanceSpecification. <span style="color:var(--ds-text,#172b4d);">Not applicable when executionTarget is a table.</span></li><li data-uuid="8dd3e0f1-0ad1-4926-94ad-7780aa0e7549">If the <strong>resultLocation</strong> is specified by a Package or a Model, Magic Model Analyst / Cameo Simulation Toolkit will create a new InstanceSpecification owned by the Package or the Model after the simulation. The values of the context object will then be saved as slot values of the created InstanceSpecification. </li><li data-uuid="ae080bcc-31bc-49d5-b4d7-b4332500826c">If the <strong>resultLocation</strong> is specified by an InstanceTable, a new result instance will be created and added as a new row with only the visible columns of the table. However, if the <strong>executionTarget</strong> and the <strong>resultLocation</strong> are the same InstanceTable, the result instance will be updated instead (only visible columns of the table). See also the Instance Table in the modeling tool User Guide.</li></ul><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="48e56ff3-91e5-4f0c-b99b-4d0038894ca0"><ac:parameter ac:name="title">Note</ac:parameter><ac:rich-text-body><p>The following elements will not be saved</p><ul><li data-uuid="89f21f3e-dea3-46b7-9bd8-94ddd59d0e86">InstanceTable without the Classifier set.</li><li data-uuid="e0c988c2-f202-4d76-b64d-8e7685e78d72">Nested instances inside slots.</li></ul></ac:rich-text-body></ac:structured-macro><ul><li data-uuid="688b864d-d264-459f-8d2f-2ac1493b94e0">If the resultLocation is not specified, the simulation results will not be saved, except if executionTarget is a table, then instances will be updated in the same table.</li></ul></div></td></tr><tr><td><strong>enginesPriority</strong></td><td>Allows specifying execution engine priority and availability for a particular execution. The first engine on the list has the highest priority. If the Simulation Configuration does not have a tagged value for this tag definition, Magic Model Analyst / Cameo Simulation Toolkit will use the values that are defined in the registered Simulation Engine Priority in the <strong><ac:link><ri:page ri:content-title="Project options" /><ac:plain-text-link-body><![CDATA[Project Options]]></ac:plain-text-link-body></ac:link></strong> dialog.</td></tr><tr><td><strong>allowConcurrentAllocatedActivities</strong></td><td><p>If set to <em>true</em>, Activities can be executed in parallel even if the allocated resource is busy. If set to <em>false</em>, only one allocated Activity is executed for an object represented in an Activity Partition.</p></td></tr><tr><td><strong>autoStart</strong></td><td><div class="content-wrapper"><p>If <em>true</em>, a model simulation starts running automatically once it has been initialized. Otherwise, you must click the <strong>Start </strong>button in the <strong>Simulation</strong> pane to run the simulation.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="7537bdc6-3498-42de-82c6-ef8fde45c03b"><ac:parameter ac:name="title">Note</ac:parameter><ac:rich-text-body><p>For <a href="https://docs.nomagic.com/display/MMA/Monte+Carlo+simulation">Monte Carlo Simulation</a> and <a href="https://docs.nomagic.com/display/MMA/Table">Table Simulation</a>, the conditions are as follows:</p><ul><li data-uuid="f2739639-0cf9-42f9-aa5a-8b9c61d30852">If <em>true</em>, the simulation will be initialized, solve parametric, start Behaviors, wait for Behaviors terminated or when <strong>endTime</strong> is reached, and terminate. Those Behaviors are Blocks with Classifier Behaviors and/or Part Property with Behaviors. If <strong>endTime</strong> is less than the time of part Behaviors, e.g., duration constraints are applied, the time of each iteration will be <strong>endTime</strong>. However, when <strong>endTime</strong> is more than the time of part Behaviors, all part Behaviors will be completed just once.</li><li data-uuid="28706768-3e4a-452d-8760-9ac2e8792b84">If false, the simulation will be initialized, solve parametric, and terminate. Behaviors will not be started.</li></ul></ac:rich-text-body></ac:structured-macro></div></td></tr><tr><td><strong>clock </strong><strong>ratio</strong></td><td>A ratio between a simulation clock and a real-time clock (1:10). For example, if the clock ratio is 10, it means that one second on the simulation clock is equal to 10 seconds on the real-time clock.  </td></tr><tr><td><strong>autostartActiveObjects</strong> </td><td>If the value is <em>true</em>, the runtime objects whose classifier is active will start their behavior automatically in an asynchronous mode. Otherwise, their behavior will start using a startObjectBehaviorAction. </td></tr><tr><td><strong>executionListeners</strong> </td><td>A list of execution listeners that will receive events from a model simulation. An execution listener can be a SequenceDiagramGeneratorConfig.</td></tr><tr><td><strong>decimalPlaces</strong></td><td>Decimal places of all displayed numerical values in a model simulation, for example, in the <strong>Variables</strong> pane, Tooltip, and the <strong>Simulation</strong><strong>Console</strong> pane. Their values must be integers. If the precision of displayed numerical values is greater than or equal to 10% of the absolute value, the numerical values will be displayed in exponential form.</td></tr><tr><td><strong>fireValueChangeEvent</strong></td><td>If this value is <em>true</em>, a parametric simulation will be repeated immediately whenever the value of any structural feature changes. Repeating simulation will give an impact on both values carried over by binding connectors and specified in a constraint.</td></tr><tr><td><strong>timeValue</strong> </td><td>A property that will be used in a model-based clock. If the tagged value is specified, the run-time value specified by the property will be used as the simulation time.</td></tr><tr><td><strong>timeUnit</strong> </td><td>A unit of a runtime value that specifies the simulation time. If the tagged value is unspecified, the millisecond will be used by default. </td></tr><tr><td><strong>constraintFailureAsBreakpoint</strong> </td><td>A flag that indicates a simulation will pause at the constraint element where the failure occurs. </td></tr><tr><td><strong>rememberFailureStatus</strong></td><td>If <em>true</em>, the failure status will be remembered until the termination, and the first failure status will be recorded with its timestamp as fail, even though it passes at the end.</td></tr><tr><td><strong>durationSimulationMode</strong> </td><td>Specifies a duration mode of simulation in min, max, average, or random. Magic Model Analyst / Cameo Simulation Toolkit uses the duration mode to calculate the duration of an Action simulation to which a duration constraint is applied. </td></tr><tr><td><strong>treatAllClassifiersAsActive</strong> </td><td>This option (<em>true</em> by default) runs all Behaviors, including the ones in the subsystems. Even though the isActive property is <em>false</em>, if TreatAllClassifiersAsActive is true, Magic Model Analyst / Cameo Simulation Toolkit will run all of the Behaviors of non-active Classifiers. </td></tr><tr><td><strong>initializeReferences</strong></td><td><p>If <em>true</em>, references will be initialized by creating new objects, instead of referencing the existing parts of the system. See also in <ac:link ac:anchor="InitializeReferencesproperty"><ac:plain-text-link-body><![CDATA[Initialize References property]]></ac:plain-text-link-body></ac:link>.</p></td></tr><tr><td><strong>startTime</strong></td><td>Specifies when simulation will initiate (in integer).</td></tr><tr><td><strong>endTime</strong></td><td>The time simulation terminates (in integer).</td></tr><tr><td><strong>stepSize</strong></td><td>Increases together with the simulation time (in real numbers or decimal places).</td></tr><tr><td><strong>numberOfSteps <br /></strong></td><td>Specifies the number of steps through which the simulation will run.</td></tr><tr><td><strong>numberOfRuns</strong></td><td>A number of runs of a particular configuration, especially for the sample size in Monte Carlo simulation. The value must be greater than or equal to 1. <span style="color:var(--ds-text,#172b4d);">Not applicable when executionTarget is a table.</span></td></tr><tr><td><strong>timeVariableName</strong></td><td>This property returns time from the simulation clock (the default value is &quot;simtime&quot;). It returns the time on the simulation clock.</td></tr><tr><td><strong>stepDelay</strong></td><td>Specifies how long the delay will be, if any, for each step.</td></tr><tr><td><strong>runForksInParallel</strong></td><td>If the value is <em>true</em> or undefined, all outgoing edges from the fork will run in parallel.</td></tr><tr><td><strong>cloneReferences</strong></td><td>If <em>true</em>, creates new instances for all objects recursively. Otherwise, it creates instances only for the first level and others remain in their original locations (the default is false).</td></tr><tr><td><strong style="text-align: left;">Show UI as HTML</strong></td><td><p>If set to <em>true</em>, the HTML UI shall be generated and automatically opened in an embedded browser.</p><p>If set to <em>false</em>, the Java-based UI shall be automatically opened in an embedded browser.</p></td></tr><tr><td><strong>terminateStreamingBehaviorsByOutputParameterMultiplicity</strong></td><td>If set to <em>true</em>, a streaming Activity terminates when each of its output parameters receives a cumulative number of values equal to the upper bound of the parameter multiplicity. If set to <em>false</em>, a streaming Activity terminates only when forced by the Activity final node or the termination by the Activity that invoked it.</td></tr><tr><td><strong>solveAfterInitialization</strong></td><td>If <em>true</em>, automatically starts initial solving. If false, the manual start is required via Refresh in the <strong>Variables</strong> pane, or press <strong>Start</strong> (<strong>F8</strong>).</td></tr><tr><td><strong>animationSpeed</strong></td><td>Specifies the animation speed of a particular configuration in percentage. The default value is 95, but you can enter your preferred value from 1 to 100.</td></tr><tr><td><strong>recordTimestamp</strong></td><td><div class="content-wrapper"><p>If <em>true</em>, the timestamp is recorded into a result instance name.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="f7594e5f-648b-4919-904e-1dcb40dc7f05"><ac:parameter ac:name="title">Note</ac:parameter><ac:rich-text-body><p>The naming of the newly created instance will not follow MagicDraw instance naming criteria.</p></ac:rich-text-body></ac:structured-macro><p>If <em>false</em> (by default), MagicDraw instance naming will be used instead, and the timestamp will not be recorded and appended to the instance name.</p></div></td></tr><tr><td><strong><span style="color:var(--ds-text,#172b4d);">autoConvertUnits</span></strong></td><td>If <em>true</em>, values connected via Binding Connector will be recalculated if they have compatible types defined by the QUDV library.</td></tr><tr><td><div class="content-wrapper"><p><strong style="text-align: left;">autoTerminate<br /></strong></p></div></td><td><div class="content-wrapper"><p>If <em>true</em>, <span style="color:var(--ds-text,#172b4d);">the simulation terminates when it is completed or after the initialization phase, if autoStart is set to false. </span></p><p><span style="color:var(--ds-text,#172b4d);">If <em>false</em>, the simulation continues without termination, hanging at the end or after the initialization phase, if autoStart is set to false.</span></p><p>The default setting for this property is<span> </span>undefined, allowing the simulation to conclude under normal circumstances. Normal circumstances mean, when the specified end time is reached or when the main behavior finishes.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="db275681-0f0f-48e3-8d1c-b75c237383f3"><ac:rich-text-body><p>To learn more about how <strong>autoStart </strong>and <strong>autoTerminate </strong>tags work in combination, refer to the table below:</p><table class="wrapped" data-mce-resize="false"><tbody><tr><th>autoStart</th><th>autoTerminate</th><th>Result</th></tr><tr><td>True</td><td>True</td><td>The simulation will automatically start and will terminate under normal conditions, such as reaching the specified end time or when the main behavior terminates. <br /><em>Note</em>: <span style="color:var(--ds-text,#172b4d);">A simulation with no main behavior will run until the user manually terminates it.</span></td></tr><tr><td>True</td><td>False</td><td>The simulation will automatically start, but it will not be terminated upon reaching the end time or the conclusion of the main behavior. Instead, the simulation will hang at the end.</td></tr><tr><td>False</td><td>True</td><td>After the initialization phase, the simulation will be terminated.</td></tr><tr><td>False</td><td>False</td><td>After the initialization phase, the simulation will not be terminated. Instead, it will remain in the initialized phase, hanging in that state. <br />However, once the simulation is started, the simulation will hang at the end.</td></tr></tbody></table></ac:rich-text-body></ac:structured-macro></div></td></tr><tr><td><strong>showAnnotations</strong></td><td><div class="content-wrapper"><p>If <em>true,</em> the simulation annotations in the diagrams are enabled.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="05dae2e4-361f-4d93-9226-1379eba718bc"><ac:rich-text-body><p style="text-align: left;"><span> </span>If <strong>showAnnotations</strong> is set to <em>false</em>, then the following animation features will be affected accordingly:</p><ul style="text-align: left;"><li data-uuid="21318a1c-c67e-4e88-8c76-3773ca14a012">Flowing information will also be disabled.</li><li data-uuid="1d5996ec-42b4-4e37-b370-36b024593fd1">Animation delay will be disabled, thus the animation will run at full speed.</li><li data-uuid="9b0d78f7-d7fb-4eeb-b894-f2a0fc7a39bf">The annotation tooltips will be gone since they relate to annotations.</li><li data-uuid="6b4ef8e0-84e2-4be0-96bf-1b26c89ffa57">On a breakpoint, the annotation will be shown as it is now with <strong>silent </strong>animation.</li></ul></ac:rich-text-body></ac:structured-macro></div></td></tr><tr><td><strong>showRuntimeValuesOnPartShapes</strong></td><td><p>If <em>true,</em> the runtime values on Part shapes are displayed instead of the default values.</p></td></tr><tr><td><strong>showRuntimeValuesOnPortLabels</strong></td><td><p>If <em>true,</em> the runtime values on the Port and Constraint Parameters labels are displayed.</p></td></tr><tr><td><strong>showFlowingInformation</strong></td><td><p>If <em>true, </em>the label of the flowing item on the path is displayed. If <em>false, </em>only the flow path is highlighted.</p></td></tr><tr><td><strong>showUnits</strong></td><td><p>If <em>true</em>, <span style="color:var(--ds-text,#172B4D);">unit symbols for runtime values in diagrams and UI mockups are displayed.</span></p></td></tr></tbody></table><h3>Initialize References property</h3><p>The property Initialize References in the Specification window of <em>«</em>SimulationConfig» allows Magic Model Analyst / Cameo Simulation Toolkit to initialize all references between objects owned in a composite owner. The following is the Specification window of <em>«</em>SimulationConfig» from the <a href="https://docs.nomagic.com/display/MT/_sample+models?preview=%2F17664205%2F17664212%2FCoffeeMachine.mdzip">CoffeeMachine.mdzip</a> sample.</p><p><br /></p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="InitializeReferences.png" /></ac:image></p><h6 style="text-align: center;">Initialize references in the Specification window of «SimulationC<span>onfig» Coffee Machine.</span></h6><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="534c7cab-2e13-4440-af82-b359ab0db868"><ac:parameter ac:name="title">Note</ac:parameter><ac:rich-text-body><p>Initialize References appears if you open the Specification window in the <strong>All</strong> or <strong>Expert</strong> Properties mode.</p></ac:rich-text-body></ac:structured-macro><p>The following are two types of references that you can initialize using the Initialize References option in SimulationConfig</p><ul><li data-uuid="3b221ef8-f859-4747-bb25-e8495043d7a4"><strong>References between objects created inside a system</strong></li></ul><p style="margin-left: 30.0px;">This type of reference occurs when you create a project similar to the following example. The following figure shows <strong><em>«</em>block» c</strong> as a root context, <strong>a</strong> is a Part Property, and <strong>b</strong> is both the part and reference properties. The <strong><em>«</em>block c»</strong> contains an Internal Block diagram with a connector line (the type of the connector is association named <strong>a-b</strong>) that connects two part properties <strong>a:a</strong> to<strong> b:b</strong>. The connector specifies that reference property <strong>b </strong>will get the run time object value from Part Property <strong>b</strong>. If there is no connector, an auto-generated value will be given to reference property <strong>b</strong>.</p><p><ac:image ac:align="center" ac:title="Initialization of Property" ac:alt="Initialization of Property"><ri:attachment ri:filename="initialization+of+references.png" /></ac:image></p><h6 style="text-align: center;">Initialization of Property.</h6><ul><li data-uuid="197258d7-c4c8-4fa2-986f-72d9d66c971f"><strong>References to external objects</strong></li></ul><p style="margin-left: 30.0px;"><span>If you run a block, for example, the <strong>Variables</strong> pane will show the classifiers of the references. When the InitializeReferences is false, the reference property in the block will not be initialized. When it is true, the reference property will be initialized at run time.</span></p><h3>Instantiation scope with excluded elements</h3><p>To control what part of the model is used in simulation, you can use <strong>excludedElement</strong> to exclude and not to instantiate any elements that are not ready to be used or not needed. When any Classifiers, e.g., Classes, Packages, Use Cases, Actors, Behaviors, Connectors, Ports, or States are selected, they will not be instantiated by default instantiation. Excluded Classifiers will not be displayed in the list of types in the <strong>Variables</strong> pane when clicked or right-clicked to select <strong>Add value</strong>. For example, a Part property is set in <strong>excludedElement</strong>, so it will not be instantiated when running a simulation as shown in the figure below. See also in <a href="https://docs.nomagic.com/display/MMA/Class#Class-AutomaticinstantiationoftheimplementationClass">Automatic instantiation of the implementation Class</a>.</p><p><ac:image ac:align="center"><ri:attachment ri:filename="Part Property Not Instantiated in the Variables Pane.PNG" /></ac:image></p><h6 style="text-align: center;">Part property, CPU2, is not instantiated in the Variables pane, since it has been set in excludedElement.</h6><p>For nested Part properties, <strong>excludedElement</strong> can be set through «SelectPropertiesConfig» as shown in the figure below. You can find the <strong>«SelectPropertiesConfig»</strong> control in the <strong>Simulation Configuration Diagram</strong> toolbar.</p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="Nested Part Property Not Instantiated in the Variables Pane.PNG" /></ac:image></p><h6 style="text-align: center;">Nested Part property, cache of CPU2, is not instantiated in the Variables pane, since it has been set in excludedElement through «SelectPropertiesConfig».</h6></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><strong>Related pages</strong></p><ul><li data-uuid="1d9571cb-56be-4d4e-b094-5a7cab7d456d"><ac:link /></li><li data-uuid="cc3ac24f-7b3a-4af9-ad12-ab825ce49097"><ac:link><ri:page ri:content-title="Simulation log" /></ac:link></li><li data-uuid="22f0f26c-2af1-40ca-a028-be3e1b2a7388"><ac:link><ri:page ri:content-title="Simulation time and simulation clock" /></ac:link></li><li data-uuid="c2e63170-b8e9-4354-9c03-21b0451ed67e"><ac:link><ri:page ri:content-title="Automatic start of active objects" /></ac:link></li><li data-uuid="45a55ad1-c9b8-4fe7-affc-9f3ed6e4cde0"><ac:link><ri:page ri:content-title="UI modeling diagram simulation" /></ac:link></li><li data-uuid="864aa790-013b-45cd-af8e-3221cb690941"><ac:link><ri:page ri:content-title="ImageSwitcher and ActiveImage" /></ac:link></li><li data-uuid="317fe824-5e9a-4fe9-a758-0df03ec8b315"><ac:link><ri:page ri:content-title="Time Series Chart" /></ac:link></li><li data-uuid="c65ff463-7497-4e7f-a176-0f75886158d8"><ac:link><ri:page ri:content-title="Timeline chart" /></ac:link></li><li data-uuid="982e0fa2-31d6-49d3-9bfd-439d9051163c"><ac:link><ri:page ri:content-title="Histogram" /></ac:link></li><li data-uuid="e5dc1ce8-4ee7-4113-b327-d7800046d035"><ac:link><ri:page ri:content-title="Nested UI Configuration stereotype" /></ac:link></li><li data-uuid="3b5ba8ab-1bf7-4600-88f8-65a4efdc05fd"><ac:link><ri:page ri:content-title="Reusable UI Mockup" /></ac:link></li><li data-uuid="8692be1c-fdd0-4231-9b8b-2bfc3bd89032"><ac:link /></li><li data-uuid="abdf4dbf-ae5b-4ed9-a3ea-c563348f876c"><ac:link><ri:page ri:content-title="CSV export" /></ac:link></li><li data-uuid="33c36aa2-018c-4154-915d-b741a1f9f418"><ac:link><ri:page ri:content-title="Nested property selection for configurations" /></ac:link></li><li data-uuid="bcbf1217-6447-4365-84b4-ddc583c0e1e1"><ac:link><ri:page ri:space-key="MT" ri:content-title="Instance table" /></ac:link></li></ul></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=249571275 space=MMA version=4 -->
## PAGE 00722: SIMULIA Process Composer Integration

- page_id: `249571275`
- space_key: `MMA`
- source_url: https://docs.nomagic.com/spaces/MMA/pages/249571275/SIMULIA+Process+Composer+Integration
- version_number: 4
- version_date: `2025-12-03T09:50:02.983+01:00`
- ancestors: Magic Model Analyst / Cameo Simulation Toolkit Documentation > User Guide
- labels: []

### NORMALIZED CONTENT

In today’s complex product development and manufacturing environment, designers and engineers use various software tools to design and simulate their products. Often, chained simulation process flows are required in which the parameters and results of one system are needed as inputs to another system. The manual process of entering the required data can reduce efficiency, slow product development, and introduce errors in modelling and simulation assumptions. Additionally, the decreasing time-to-market phases and the increasing complexity of advanced systems make it difficult for engineers to properly test the performance of systems, implement changes, and optimize the system architecture.

MBSE in****SIMULIA and****Magic Model Analyst / Cameo Simulation Toolkit enables a system model to be simulated and integrated with multidisciplinary engineering tools, providing a high level of fidelity to MBSE/digital engineering.

[IMAGE alt='' src='']

###### The process of simulation using a Simulation Template from SIMULIA.

To execute a model using a Simulation Template and get the results in a modeling tool follow these steps:

1. .
2. .
3. .

##### Creating and sharing a Simulation Template

When you create the Simulation Process in SIMULIA Process Composer and save it as a template to be used in a modeling tool, make sure that the following criteria are met:

- The simulation Process must expose at least one input and/or output parameter.
- Defined parameters must be scalar: Real, Integer, String, Boolean. Array parameters are supported.
- The Simulation Template must be shared on the 3DEXPERIENCE platform.

The created workflows must have associated affinities which tell where the simulation job is executed. If specified station is not available (for example if private station is not started), then simulation process can hang without any result. For more information, please refer to[SIMULIA documentation](https://help.3ds.com/2024/english/dssimulia_established/ihrseetomeemap/x1e-c-Interfaces-Station-AboutAffin.htm).

##### Dragging a Simulation Template to a modeling tool

You can use a Simulation Template in a modeling tool by dragging it to one of the following diagrams:

- An Activity Diagram - in this case, an Activity with a hyperlink to the Simulation Template in SIMULIA is created. In addition, a Call Behavior Action with exposed input and/or output pins is created and displayed in the Activity Diagram.
- A Parametric Diagram - in this case, a Constraint Block with a hyperlink to the Simulation Template in SIMULIA is created. In addition, a Constraint with exposed input and/or output Constraint Parameters is created and displayed in the Parametric Diagram.

To drag a Simulation Template to a diagram in a modeling tool

1. In the main menu of a modeling tool, select 3DEXPERIENCE > Login and [CONFLUENCE_PAGE title='Authentication with 3DEXPERIENCE platform' space='MT'] .
2. Use an internet browser to open the 3DEXPERIENCE platform and find the Simulation Template from SIMULIA that you want to use.
3. Drag the Simulation Template from the 3DEXPERIENCE platform on the web to an Activity or Parametric Diagram in your modeling tool.

[IMAGE alt='' src='']

###### Dragging a Simulation Template from SIMULIA to an Activity or Parametric Diagram.

##### Connecting a model with SIMULIA Process Composer and launching the simulation

After dragging a Simulation Template to an Activity or Parametric Diagram, connect the SysML model with the SIMULIA Process Composer. This means you need to define what SysML parameters should be provided to the Simulation Template as inputs and what parameters should be retrieved as outputs back to the SysML model. Once you connect the parameters, you can launch the simulation in a modeling tool.

#### NOTE: SIMULIA Process Composer Project Options

SIMULIA Process Composer Project Options

You can modify the SIMULIA Process Composer project options from the Project Options dialog under Simulation section. To learn more about Project Options dialog, refer to [CONFLUENCE_PAGE title='Project options' space=''].

- Execution License : Specifies which license type is used for job execution. If the selected execution license is not available on the server, the next available license is used.

To connect input and output parameters and run the simulation using a Simulation Template

1. Connect the exposed parameters of a Simulation Template:
  - If you work with an Activity Diagram, connect the Pins of the created Call Behavior Action to the required input and/or output parameters.
  - If you work with a Parametric Diagram, connect the Constraint Parameters of the created Constraint with the required input and/or output parameters.
2. Run the simulation using a Simulation Configuration.

[IMAGE alt='' src='']

###### The sample diagrams illustrate how to connect the input and output parameters of a Simulation Template.

#### NOTE: Storing simulation results

Storing simulation results

Results Location

- The simulation results are stored in an Instance Specification.
- A hyperlink to the simulation process stored on the 3DEXPERIENCE platform is added tothe Instance Specification with the simulation results.
- If t he Instance Specification with the simulation results already has a hyperlink(s), it is removed and a new hyperlink to the simulation process is added and marked as active.
- Hyperlinks to the simulation process are stored on the root Instance Specification with the simulation results .

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>In today’s complex product development and manufacturing environment, designers and engineers use various software tools to design and simulate their products. Often, chained simulation process flows are required in which the parameters and results of one system are needed as inputs to another system. The manual process of entering the required data can reduce efficiency, slow product development, and introduce errors in modelling and simulation assumptions. Additionally, the decreasing time-to-market phases and the increasing complexity of advanced systems make it difficult for engineers to properly test the performance of systems, implement changes, and optimize the system architecture.</p><p>MBSE in<strong> </strong>SIMULIA and<strong> </strong>Magic Model Analyst / Cameo Simulation Toolkit enables a system model to be simulated and integrated with multidisciplinary engineering tools, providing a high level of fidelity to MBSE/digital engineering.</p><p><br /></p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="integration.png" /></ac:image></p><h6 style="text-align: center;">The process of simulation using a Simulation Template from SIMULIA.</h6><p>To execute a model using a Simulation Template and get the results in a modeling tool follow these steps:</p><ol><li><p><ac:link ac:anchor="Creating and sharing a Simulation Template"><ac:plain-text-link-body><![CDATA[Create the Simulation Process in SIMULIA Process Composer and share it as a Simulation Template on the 3DEXPERIENCE platform]]></ac:plain-text-link-body></ac:link>.</p></li><li><p><ac:link ac:anchor="Dragging a Simulation Template to a modeling tool"><ac:plain-text-link-body><![CDATA[Drag the Simulation Template from SIMULIA to the modeling tool and expose its inputs and outputs]]></ac:plain-text-link-body></ac:link>.</p></li><li><p><ac:link ac:anchor="Connecting a model with SIMULIA Process Composer and launching the simulation"><ac:plain-text-link-body><![CDATA[Connect a SysML model with SIMULIA Process Composer and launch the simulation in the modeling tool]]></ac:plain-text-link-body></ac:link>.</p></li></ol><h3><br />Creating and sharing a Simulation Template</h3><p>When you create the Simulation Process in SIMULIA Process Composer and save it as a template to be used in a modeling tool, make sure that the following criteria are met:</p><ul><li>The simulation Process must expose at least one input and/or output parameter.</li><li>Defined parameters must be scalar: Real, Integer, String, Boolean. <span style="color:var(--ds-text,#172b4d);">Array parameters are supported.</span></li><li>The Simulation Template must be shared on the 3DEXPERIENCE platform.</li></ul><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="a79c0f51-20ec-463c-bb09-3e7f2f710f84"><ac:rich-text-body><p><span style="color:var(--ds-text,#172b4d);">The created workflows must have associated affinities which tell where the simulation job is executed. If specified station is not available (for example if private station is not started), then simulation process can hang without any result. For more information, please refer to<span> </span></span><a class="external-link" style="text-align: left;" href="https://help.3ds.com/2024/english/dssimulia_established/ihrseetomeemap/x1e-c-Interfaces-Station-AboutAffin.htm" title="Follow link">SIMULIA documentation</a>.</p></ac:rich-text-body></ac:structured-macro><h3>Dragging a Simulation Template to a modeling tool</h3><p>You can use a Simulation Template in a modeling tool by dragging it to one of the following diagrams:</p><ul><li>An Activity Diagram - in this case, an Activity with a hyperlink to the Simulation Template in SIMULIA is created. In addition, a Call Behavior Action with exposed input and/or output pins is created and displayed in the Activity Diagram.</li><li>A Parametric Diagram - in this case, a Constraint Block with a hyperlink to the Simulation Template in SIMULIA is created. In addition, a Constraint with exposed input and/or output Constraint Parameters is created and displayed in the Parametric Diagram.</li></ul><p><br /></p><p>To drag a Simulation Template to a diagram in a modeling tool</p><hr /><ol><li>In the main menu of a modeling tool, select <strong>3DEXPERIENCE</strong> &gt; <strong>Login</strong> and <ac:link><ri:page ri:space-key="MT" ri:content-title="Authentication with 3DEXPERIENCE platform" /><ac:plain-text-link-body><![CDATA[log into the 3DEXPERIENCE platform]]></ac:plain-text-link-body></ac:link>.</li><li>Use an internet browser to open the 3DEXPERIENCE platform and find the Simulation Template from SIMULIA that you want to use.</li><li>Drag the Simulation Template from the 3DEXPERIENCE platform on the web to an Activity or Parametric Diagram in your modeling tool.</li></ol><p><br /></p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="dragging_simulation_template.png" /></ac:image></p><h6 style="text-align: center;">Dragging a Simulation Template from SIMULIA to an Activity or Parametric Diagram.</h6><h3>Connecting a model with SIMULIA Process Composer and launching the simulation</h3><p>After dragging a Simulation Template to an Activity or Parametric Diagram, connect the SysML model with the SIMULIA Process Composer. This means you need to define what SysML parameters should be provided to the Simulation Template as inputs and what parameters should be retrieved as outputs back to the SysML model. Once you connect the parameters, you can launch the simulation in a modeling tool.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="15fef393-faca-4780-8296-ab7f7355ad94"><ac:parameter ac:name="title">SIMULIA Process Composer Project Options</ac:parameter><ac:rich-text-body><p>You can modify the SIMULIA Process Composer project options from the Project Options <ac:inline-comment-marker ac:ref="1d27fa2c-1f1f-428a-9491-8e06ad004cd6">dialog <span style="color:var(--ds-text,#333333);">under Simulation section</span></ac:inline-comment-marker>. To learn more about Project Options dialog, refer to <ac:link><ri:page ri:content-title="Project options" /><ac:plain-text-link-body><![CDATA[Project Options]]></ac:plain-text-link-body></ac:link>.</p><ul><li><strong>Execution License</strong>: <span style="color:var(--ds-text,#172b4d);">Specifies which license type is used for job execution. </span><ac:inline-comment-marker ac:ref="cacc62ba-4785-4f78-8a85-7ccfe6464a1e">If the selected execution license is not available on the server, the next available license is used.</ac:inline-comment-marker></li></ul></ac:rich-text-body></ac:structured-macro><p><br /></p><p>To connect input and output parameters and run the simulation using a Simulation Template</p><hr /><ol><li>Connect the exposed parameters of a Simulation Template:<ul><li>If you work with an Activity Diagram, connect the Pins of the created Call Behavior Action to the required input and/or output parameters.</li><li>If you work with a Parametric Diagram, connect the Constraint Parameters of the created Constraint with the required input and/or output parameters.</li></ul></li><li>Run the simulation using a Simulation Configuration.</li></ol><p style="text-align: center;"><br /><ac:image><ri:attachment ri:filename="connecting_parameters.png" /></ac:image></p><h6 style="text-align: center;">The sample diagrams illustrate how to connect the input and output parameters of a Simulation Template.</h6><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="5c378e2a-8b4d-403b-a725-69ea9856d996"><ac:parameter ac:name="title">Storing simulation results</ac:parameter><ac:rich-text-body><span style="color:var(--ds-text,#333333);">If the <strong>Results Location</strong> property of a Simulation Configuration is specified:<br /></span><ul><li><span style="color:var(--ds-text,#333333);">The simulation results are stored in an Instance Specification.</span></li><li><span style="color:var(--ds-text,#333333);"><span>A hyperlink to the simulation process stored on the 3DEXPERIENCE platform is added to </span>the Instance Specification with the simulation results.</span></li><li>If t<span style="color:var(--ds-text,#333333);">he Instance Specification with the simulation results</span> already has a hyperlink(s), it is removed and a new hyperlink to the simulation process is added and marked as active.</li><li>Hyperlinks to the simulation process are stored on the root <span style="color:var(--ds-text,#333333);">Instance Specification with the simulation results</span>.</li></ul></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=249570806 space=MMA version=5 -->
## PAGE 00723: Simulink co-simulation

- page_id: `249570806`
- space_key: `MMA`
- source_url: https://docs.nomagic.com/spaces/MMA/pages/249570806/Simulink+co-simulation
- version_number: 5
- version_date: `2025-09-15T18:05:26.321+02:00`
- ancestors: Magic Model Analyst / Cameo Simulation Toolkit Documentation > User Guide > Parametric evaluator > Integration with external Evaluators > Integration with MATLAB
- labels: ['simulink-co-simulation']

### NORMALIZED CONTENT

Magic Model Analyst / Cameo Simulation Toolkit supports Simulink (MATLAB) co-simulation. Simulation executes the entire Simulink model (*.slx) on all steps, if there are any value changes in the input, which is similar to FMI. Simulation works with Simulink models as attached files and Simulink models located in the same directory of the project.

#### WARNING: Warning

Warning

- You must successfully integrate MATLAB Version 2016b or later before using Simulink co-simulation. See Integration with MATLAB .
- Any duplicated Simulink model is not allowed in the project.

#### NOTE: Note

Note

- Simulink models without input/output Ports are not executed because there is no connectivity, and value change is not propagated to the Block.
- This type of Simulink integration is for atomic calculations. When any input changes, outputs such as the parametric diagram are calculated, e.g. In1 → Gain5 → Out1. It occurs as one step of Simulation time, the same as FMU.
- If the simulink file (.slx) is updated or modified, Simulation needs to restart the MATLAB session by calling the kill matlab command in the Simulation console.

##### Using Simulink in an Internal Block/Parametric diagram

1. To import a Simulink model from the main menu, select **File** > **Import From** > **Simulink File** > **Import** > ***.slx**. You can also drag the Simulink file into the Block Definition diagram, Internal Block diagram, or Parametric diagram of the project. The **Simulink Import Options** dialog opens as shown below. [IMAGE alt='' src=''] The Simulink Import Options dialog opens after importing a Simulink model into the project.
2. All Input/Output Ports of the Simulink model are selected by default. However, you can select Proxy Port, Flow Port, or both of them in the same Block for the simulation, e.g., In1 and In2 Proxy Ports and Out1 Flow Port. The following scenarios apply:
  1. If you select the Proxy Port, you can select an existing Interface Block or <NEW> to automatically create a new Interface Block for each Port with «SimulinkBlock» applied as the model name with the Proxy Port. The automatically created Interface Block will have the default settings with In / Out In1 / Out1 : Real «FlowProperty» according to I/O Ports of the Simulink model.
  2. If you select the Flow Port, a Block with «SimulinkBlock» applied as the model name and the Flow Port with *In*/*Out In1*/*Out1 : Real «FlowPort»* according to I/O Ports of the Simulink model will be automatically created. [IMAGE alt='' src=''] The Simulink model is created as Blocks with Proxy/Flow Ports. WarningThe Interface Block of a Proxy Port must have only a Flow Property.The names of the Proxy Port and Simulink I/O Port must be the same, e.g., *In1*-*In1* and *Out1*-*Out1*.Otherwise, an error message will be printed in the **Simulation** console, and the result will be invalid.
3. Connect those Proxy/Flow ports through [CONFLUENCE_PAGE title='Binding Connector' space='MED'] in the Internal Block/Parametric diagram.
4. Run the simulation. When inputs are available for initialization (e.g., passed via binding), «SimulinkBlock» will be run at the first time and on every input change. You can also see animation of Flow Ports and set breakpoints for debugging.

From the figure below, a system is with two Simulink models: *GainAdd* and *Gain5*. *GainAdd* will multiply Port *In1* by 10, multiply Port *In2* by 2, and add the two results to Port *Out1*. *Gain5* will multiply Port *m* by 5. Therefore, *result* will be [(2 * 10) + (2 * 2)] * 5 = 120.

[IMAGE alt='' src='']

###### The Simulink co-simulation result from the system which has two Simulink models (GainAdd.slx and Gain5.slx) connected via Flow Ports.

##### Using Simulink in an Activity diagram

A Simulink model can be used in the Activity diagram through drag-and-drop operation. The dropped Simulink file is presented as an Activity in the Containment tree with the same name as the Simulink model name, and «SimulinkBlock» is automatically applied. Parameters and directions are the same as the Simulink In/Out ports and can be used as a CallBehaviorAction on demand as shown in the figure below.

[IMAGE alt='' src='']

###### A Simulink model, sumInport1, is presented as an Activity and used as a CallBehaviorAction in the Activity diagram.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>Magic Model Analyst / Cameo Simulation Toolkit supports Simulink (MATLAB) co-simulation. Simulation executes the entire Simulink model (*.slx) on all steps, if there are any value changes in the input, which is similar to FMI. Simulation works with Simulink models as attached files and Simulink models located in the same directory of the project.</p><ac:structured-macro ac:name="warning" ac:schema-version="1" ac:macro-id="5b952094-0c9f-4efa-8d95-17cff21e6ef1"><ac:parameter ac:name="title">Warning</ac:parameter><ac:rich-text-body><ul><li data-uuid="88238fa0-1855-4ee4-8133-29d963ab1f4d">You must successfully integrate MATLAB Version 2016b or later before using Simulink co-simulation. See <a href="https://docs.nomagic.com/display/MMA/Integration+with+MATLAB">Integration with MATLAB</a>.</li><li data-uuid="097fc3e7-1367-4ff6-b7f7-afaeb18e74e4">Any duplicated Simulink model is not allowed in the project.</li></ul></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="cd6084f1-b65c-4f64-92d5-6f363c476ee2"><ac:parameter ac:name="title">Note</ac:parameter><ac:rich-text-body><ul><li data-uuid="f8a72b19-dbea-49ad-ab77-f197c0302dbc">Simulink models without input/output Ports are not executed because there is no connectivity, and value change is not propagated to the Block.</li><li data-uuid="a8f61bcf-1316-486a-a02d-8ae6a71e8318">This type of Simulink integration is for atomic calculations. When any input changes, outputs such as the parametric diagram are calculated, e.g. In1 → Gain5 → Out1. It occurs as one step of Simulation time, the same as FMU.</li><li data-uuid="b42a7380-4c35-4f14-92b8-19538a673d68">If the simulink file (.slx) is updated or modified, Simulation needs to restart the MATLAB session by calling the <code>kill matlab</code> command in the <strong>Simulation</strong> console.</li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><h3>Using Simulink in an Internal Block/Parametric diagram</h3><ol><li data-uuid="56837f8b-8683-41e2-a271-b2bbdca4b4c3"><p class="auto-cursor-target">To import a Simulink model from the main menu, select <strong>File</strong> &gt; <strong>Import From</strong> &gt; <strong>Simulink File</strong> &gt; <strong>Import</strong> &gt; <strong>*.slx</strong>. You can also drag the Simulink file into the Block Definition diagram, Internal Block diagram, or Parametric diagram of the project. The <strong>Simulink Import Options</strong> dialog opens as shown below.</p><p><ac:image ac:width="800"><ri:attachment ri:filename="Simulink Import Options dialog.png" /></ac:image></p><h6>The Simulink Import Options dialog opens after importing a Simulink model into the project.</h6></li><li data-uuid="e75e28a2-b61e-410e-a150-36ee3331ea9e">All Input/Output Ports of the Simulink model are selected by default. However, you can select Proxy Port, Flow Port, or both of them in the same Block for the simulation, e.g., <em>In1</em> and <em>In2</em> Proxy Ports and Out1 Flow Port. The following scenarios apply:<br /><ol><li>If you select the Proxy Port, you can select an existing Interface Block or <strong>&lt;NEW&gt;</strong> to automatically create a new Interface Block for each Port with «SimulinkBlock» applied as the model name with the Proxy Port. The automatically created Interface Block will have the default settings with <em>In</em>/<em>Out In1</em>/<em>Out1 : Real «FlowProperty»</em> according to I/O Ports of the Simulink model.</li><li><p class="auto-cursor-target">If you select the Flow Port, a Block with «SimulinkBlock» applied as the model name and the Flow Port with <em>In</em>/<em>Out In1</em>/<em>Out1 : Real «FlowPort»</em> according to I/O Ports of the Simulink model will be automatically created.</p><p style="text-align: left;"><ac:image ac:width="700"><ri:attachment ri:filename="Simulink Model Created as Blocks.PNG" /></ac:image></p><h6 style="text-align: left;">The Simulink model is created as Blocks with Proxy/Flow Ports.</h6><ac:structured-macro ac:name="warning" ac:schema-version="1" ac:macro-id="0119e5e5-b2ad-4365-9a3c-41568e35c668"><ac:parameter ac:name="title">Warning</ac:parameter><ac:rich-text-body><ul><li>The Interface Block of a Proxy Port must have only a Flow Property.</li><li>The names of the Proxy Port and Simulink I/O Port must be the same, e.g., <em>In1</em>-<em>In1</em> and <em>Out1</em>-<em>Out1</em>.</li></ul><p>Otherwise, an error message will be printed in the <strong>Simulation</strong> console, and the result will be invalid.</p></ac:rich-text-body></ac:structured-macro></li></ol></li><li data-uuid="aea189bd-18cb-4d54-8289-49e76a568701">Connect those Proxy/Flow ports through <ac:link><ri:page ri:space-key="MED" ri:content-title="Binding Connector" /><ac:plain-text-link-body><![CDATA[binding Connectors]]></ac:plain-text-link-body></ac:link> in the Internal Block/Parametric diagram.</li><li data-uuid="8bedd778-905a-48db-a15a-dffa42308953">Run the simulation. When inputs are available for initialization (e.g., passed via binding), «SimulinkBlock» will be run at the first time and on every input change. You can also see animation of Flow Ports and set breakpoints for debugging.</li></ol><p>From the figure below, a system is with two Simulink models: <em>GainAdd</em> and <em>Gain5</em>. <em>GainAdd</em> will multiply Port <em>In1</em> by 10, multiply Port <em>In2</em> by 2, and add the two results to Port <em>Out1</em>. <em>Gain5</em> will multiply Port <em>m</em> by 5. Therefore, <em>result</em> will be [(2 * 10) + (2 * 2)] * 5 = 120.</p><p><ac:image ac:align="center"><ri:attachment ri:filename="Simulink co-simulation Result.png" /></ac:image></p><h6 style="text-align: center;">The Simulink co-simulation result from the system which has two Simulink models (GainAdd.slx and Gain5.slx) connected via Flow Ports.</h6><h3>Using Simulink in an Activity diagram</h3><p>A Simulink model can be used in the Activity diagram through drag-and-drop operation. The dropped Simulink file is presented as an Activity in the Containment tree with the same name as the Simulink model name, and «SimulinkBlock» is automatically applied. Parameters and directions are the same as the Simulink In/Out ports and can be used as a CallBehaviorAction on demand as shown in the figure below.</p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="Simulink Model as Activity and CallBehaviorAction.PNG" /></ac:image></p><h6 style="text-align: center;">A Simulink model, sumInport1, is presented as an Activity and used as a CallBehaviorAction in the Activity diagram.</h6>
````

<!--NOMAGIC_PAGE id=249570680 space=MMA version=3 -->
## PAGE 00724: Specifying the language for the expression

- page_id: `249570680`
- space_key: `MMA`
- source_url: https://docs.nomagic.com/spaces/MMA/pages/249570680/Specifying+the+language+for+the+expression
- version_number: 3
- version_date: `2026-04-13T10:13:33.415+02:00`
- ancestors: Magic Model Analyst / Cameo Simulation Toolkit Documentation > User Guide > Parametric evaluator
- labels: ['expression-language']

### NORMALIZED CONTENT

The parametric evaluator only evaluates expressions that are written in the syntax it supports. By default, the parametric evaluator uses the built-in math to solve expressions. The built-in math uses a syntax that is similar to the Octave syntax (see [CONFLUENCE_PAGE title='Built-in Math' space=''] for more information about built-in math). You can also write an expression using a scripting language that is supported by MagicDraw.

You can specify a scripting language to evaluate an expression through the **Specification** dialog of the opaque expression, which is the specification of the constraint.

To specify the language to evaluate an expression in the **Specification** dialog

1. Right-click an opaque expression in the Containment tree and select **Specification**. The **Specification** dialog of the opaque expression will open (see the following figure). [IMAGE alt='' src='']
2. Click the row next to the Language option to open the text box and enter the name of the language you want.
3. Click Close to close the dialog.

You can also select the language for constraints on a SysML constraint block through the context menu on the constraint block or a constraint property typed by the constraint block (see the following figure).

To select the language for the constraint of a SysML constraint block

1. Right-click a SysML constraint block or a constraint property typed by the constraint block on the diagram.
2. Click **Language** and select any supported language to evaluate constraint blocks from the list. [IMAGE alt='' src='']

The language of the **Default Parametric Evaluator** in Magic Model Analyst / Cameo Simulation Toolkit is Built-in Math. Therefore, it will use Built-in Math to evaluate an opaque expression whose language is not specified. You can see the **Default Parametric Evaluator** language option in the **Parametric Evaluator** group in the **[CONFLUENCE_PAGE title='Project options' space='']** dialog.

[IMAGE alt='' src='']

###### The Default Parametric Evaluator option in the Parametric Evaluator group in the Project Options dialog.

You can also specify the duration you want to wait for the parametric evaluator to evaluate an expression. The timeout value is specified in second. If, for example, the timeout value is 15, the parametric evaluator has 15 seconds to evaluate a given expression. If it cannot give you the result within 15 seconds, it will stop evaluating the expression.

**Related pages**

- [CONFLUENCE_PAGE title='Value binding' space='']
- [CONFLUENCE_PAGE title='Evaluating expressions' space='']
- [CONFLUENCE_PAGE title='Dynamic constraint' space='']
- [CONFLUENCE_PAGE title='Manual value updates using the Parametric Evaluator' space='']
- [CONFLUENCE_PAGE title='Communicating with evaluators through simulation console' space='']
- [CONFLUENCE_PAGE title='Built-in Math' space='']
- [CONFLUENCE_PAGE title='Integration with external Evaluators' space='']
- [CONFLUENCE_PAGE title='Trade study analysis' space='']
- [CONFLUENCE_PAGE title='Sample project' space='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p>The parametric evaluator only evaluates expressions that are written in the syntax it supports. By default, the parametric evaluator uses the built-in math to solve expressions. The built-in math uses a syntax that is similar to the Octave syntax (see <ac:link><ri:page ri:content-title="Built-in Math" /></ac:link> for more information about built-in math). You can also write an expression using a scripting language that is supported by MagicDraw. </p><p>You can specify a scripting language to evaluate an expression through the <strong>Specification</strong> dialog of the opaque expression, which is the specification of the constraint. <br class="atl-forced-newline" /><br class="atl-forced-newline" /></p><p>To specify the language to evaluate an expression in the <strong>Specification</strong> dialog </p><hr /><ol><li data-uuid="a7cc2c12-127c-482e-b470-5f129f061d85"><p>Right-click an opaque expression in the Containment tree and select <strong>Specification</strong>. The <strong>Specification</strong> dialog of the opaque expression will open (see the following figure).<br /><br /></p><p><ac:image ac:title="Selecting the Language of the Opaque Expression in the Specification Dialog" ac:alt="Selecting the Language of the Opaque Expression in the Specification Dialog"><ri:attachment ri:filename="spec-of-opaque-expression.png" /></ac:image><br /><br /></p></li><li data-uuid="9539ac32-f02e-44ca-8c84-6058a7c8304c">Click the row next to the <strong>Language</strong> option to open the text box and enter the name of the language you want.</li><li data-uuid="31729f52-95a7-4951-bbbb-7346e0631eb3">Click <strong>Close</strong> to close the dialog. </li></ol><p>You can also select the language for constraints on a SysML constraint block through the context menu on the constraint block or a constraint property typed by the constraint block (see the following figure). </p><p>To select the language for the constraint of a SysML constraint block </p><hr /><ol><li data-uuid="7849e9cb-4a65-4098-bd38-68c2b15d0bdc">Right-click a SysML constraint block or a constraint property typed by the constraint block on the diagram.</li><li data-uuid="5cd80209-855e-4712-97c6-9bb081efef06"><p>Click <strong>Language</strong> and select any supported language to evaluate constraint blocks from the list. </p><p><ac:image ac:title="Selecting the Language for Expressions in the Context Menu" ac:alt="Selecting the Language for Expressions in the Context Menu"><ri:attachment ri:filename="expressionLang_context.png" /></ac:image></p></li></ol><p>The language of the <strong>Default Parametric Evaluator</strong> in Magic Model Analyst / Cameo Simulation Toolkit is Built-in Math. Therefore, it will use Built-in Math to evaluate an opaque expression whose language is not specified. You can see the <strong>Default Parametric Evaluator</strong> language option in the <strong>Parametric Evaluator</strong> group in the <strong><ac:link><ri:page ri:content-title="Project options" /><ac:plain-text-link-body><![CDATA[Project Options]]></ac:plain-text-link-body></ac:link></strong> dialog. </p><p><ac:image ac:align="center"><ri:attachment ri:filename="Default Parametric Evaluator.png" /></ac:image></p><h6 style="text-align: center;">The Default Parametric Evaluator option in the Parametric Evaluator group in the Project Options dialog.</h6><p>You can also specify the duration you want to wait for the parametric evaluator to evaluate an expression. The timeout value is specified in second. If, for example, the timeout value is 15, the parametric evaluator has 15 seconds to evaluate a given expression. If it cannot give you the result within 15 seconds, it will stop evaluating the expression.</p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><strong>Related pages</strong></p><ul><li data-uuid="cdeef821-b33e-4431-92ea-ad787441b065"><ac:link><ri:page ri:content-title="Value binding" /></ac:link></li><li data-uuid="4fb18198-ff25-47b5-8748-1627cd5b45c2"><ac:link><ri:page ri:content-title="Evaluating expressions" /></ac:link></li><li data-uuid="006ac01e-df45-4124-aaf4-efaf2af9c781"><ac:link><ri:page ri:content-title="Dynamic constraint" /></ac:link></li><li data-uuid="3c7a1b3a-f848-459d-829b-29881166a6c8"><ac:link><ri:page ri:content-title="Manual value updates using the Parametric Evaluator" /></ac:link></li><li data-uuid="01b7dabe-1c89-4bad-a0d2-ffa04d8ef077"><ac:link><ri:page ri:content-title="Communicating with evaluators through simulation console" /></ac:link></li><li data-uuid="19a45594-e3b8-4574-a1fd-a9b6ec0f6590"><ac:link><ri:page ri:content-title="Built-in Math" /></ac:link></li><li data-uuid="e6309dcd-1a54-4c98-8700-92cdfccd40a5"><ac:link><ri:page ri:content-title="Integration with external Evaluators" /></ac:link></li><li data-uuid="611346d8-ae50-431d-bd0d-4ba8dbc165de"><ac:link><ri:page ri:content-title="Trade study analysis" /></ac:link></li><li data-uuid="3fd849a8-9f24-4976-8102-dac3bbaae93c"><ac:link><ri:page ri:content-title="Sample project" /></ac:link></li></ul></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=249569748 space=MMA version=8 -->
## PAGE 00725: Specifying time axis' range in a Time series chart

- page_id: `249569748`
- space_key: `MMA`
- source_url: https://docs.nomagic.com/spaces/MMA/pages/249569748/Specifying+time+axis+range+in+a+Time+series+chart
- version_number: 8
- version_date: `2026-02-26T09:33:39.501+01:00`
- ancestors: Magic Model Analyst / Cameo Simulation Toolkit Documentation > User Guide > Simulation Configuration and UI modeling > Time Series Chart
- labels: ['time-axis-range']

### NORMALIZED CONTENT

You can specify the range of the time axis (horizontal axis) in a Time series chart by providing the values of **fixedTimeLength** and **fixedTimeLocation**. If you specify a value for the Fixed Time Length but leave the Fixed Time Location value empty, the Time Series chart will work like an oscilloscope, and the plot(s) will move to the left. If the Fixed Time Location value is not specified, the chart uses the **Start Time**defined in the Simulation Configuration Timing properties (if set). Negative time values are supported. The fixedTimeLength and fixedTimeLocation units are specified by **timeUnit** when a model-based clock is used (For more information about the model-based clock, see [CONFLUENCE_PAGE title='Model-based clock' space='']). If you do not specify the time unit, Magic Model Analyst will use milliseconds as the default unit.

You can use the **fixedTimeLength** property to specify the range of the time axis. If you do not define the value of **fixedTimeLength**, the time axis will expand as long as the maximum duration a simulation will run. The following figure shows a Time series chart when the **fixedTimeLength** value is 100 seconds

[IMAGE alt='' src='']

###### A Time series chart when the **fixedTimeLength** value is 100 seconds.

You can also change the minimum value of the time axis in a Time series chart by specifying the value for **fixedTimeLocation**. The following figure shows a Time series chart when the **fixedTimeLength** value is 100 seconds, and the **fixedTimeLocation** value is 50 seconds.

If the Fixed Time Location value is not specified, the chart uses the Start Time defined in the Simulation Configuration Timing properties (if set). Negative time values are supported.

[IMAGE alt='' src='']

###### A Time series chart when the fixedTimeLength value is 100 seconds, and the fixedTimeLocation value is 50 seconds.

If the value you define only that of the **fixedTimeLength** value, the minimum value of the time axis will change automatically to adjust to the total length of time that you have defined as the value of **fixedTimeLength**. This situation will occur when the simulation time is greater than **fixedTimeLength**. If this happens, the maximum time axis value will be the actual simulation time and the minimum time axis value will increase to preserve the current value of **fixedTimeLength**.

If **fixedTimeLength** is 100 seconds, the range of the time axis will be [0, 100] (If you do not specify **fixedTimeLocation**, the minimum time axis value will be 0). However, if your simulation model runs longer than the simulation time or more than 100 seconds, e.g., 115 seconds, the range of the time axis will be [15, 115]. This particular Behavior of Magic Model Analyst / Cameo Simulation Toolkit's Time series chart is similar to that of Oscilloscope when **fixedTimeLocation** is unspecified.

[IMAGE alt='' src='']

###### A Time series chart with fixedTimeLength 100 seconds and fixedTimeLocation unspecified running longer than the simulation time.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>You can specify the range of the time axis (horizontal axis) in a Time series chart by providing the values of <strong>fixedTimeLength</strong> and <strong>fixedTimeLocation</strong>. If you specify a value for the Fixed Time Length but leave the Fixed Time Location value empty, the Time Series chart will work like an oscilloscope, and the plot(s) will move to the left. If the Fixed Time Location value is not specified, the chart uses the <strong>Start Time </strong>defined in the Simulation Configuration Timing properties (if set). Negative time values are supported. The fixedTimeLength and fixedTimeLocation units are specified by <strong>timeUnit</strong> when a model-based clock is used (For more information about the model-based clock, see <ac:link><ri:page ri:content-title="Model-based clock" /><ac:plain-text-link-body><![CDATA[Model-based Clock]]></ac:plain-text-link-body></ac:link>). If you do not specify the time unit, Magic Model Analyst will use milliseconds as the default unit.</p><p>You can use the <strong>fixedTimeLength</strong> property to specify the range of the time axis. If you do not define the value of <strong>fixedTimeLength</strong>, the time axis will expand as long as the maximum duration a simulation will run. The following figure shows a Time series chart when the <strong>fixedTimeLength</strong> value is 100 seconds</p><p style="margin-left: 30.0px;"><ac:image ac:align="center" ac:alt="Time Series Chart with 100 Seconds fixedTimeLength Value"><ri:attachment ri:filename="Time Series Chart with fixedTimeLength value 100.png" /></ac:image></p><h6 style="margin-left: 30.0px;text-align: center;">A Time series chart when the <strong>fixedTimeLength</strong> value is 100 seconds.</h6><p>You can also change the minimum value of the time axis in a Time series chart by specifying the value for <strong style="line-height: 1.42857;">fixedTimeLocation</strong>. The following figure shows a Time series chart when the <strong style="line-height: 1.42857;">fixedTimeLength</strong> value is 100 seconds, and the <strong style="line-height: 1.42857;">fixedTimeLocation</strong> value is 50 seconds.</p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="c2a45695-b05f-4a7b-8c4b-832699c1b949"><ac:rich-text-body><p>If the Fixed Time Location value is not specified, the chart uses the Start Time defined in the Simulation Configuration Timing properties (if set). Negative time values are supported.</p></ac:rich-text-body></ac:structured-macro><p><br /></p><p style="margin-left: 30.0px;"><br class="atl-forced-newline" /><ac:image ac:align="center" ac:alt="Time Series Chart with 50 Seconds fixedTimeLocation Value" ac:height="250"><ri:attachment ri:filename="Time Series Chart with fixedTimeLocation 50.png" /></ac:image></p><h6 style="text-align: center;">A Time series chart when the fixedTimeLength value is 100 seconds, and the fixedTimeLocation value is 50 seconds.</h6><p>If the value you define only that of the <strong>fixedTimeLength</strong> value, the minimum value of the time axis will change automatically to adjust to the total length of time that you have defined as the value of <strong>fixedTimeLength</strong>. This situation will occur when the simulation time is greater than <strong>fixedTimeLength</strong>. If this happens, the maximum time axis value will be the actual simulation time and the minimum time axis value will increase to preserve the current value of <strong>fixedTimeLength</strong>. </p><p>If <strong>fixedTimeLength</strong> is 100 seconds, the range of the time axis will be [0, 100] (If you do not specify <strong>fixedTimeLocation</strong>, the minimum time axis value will be 0). However, if your simulation model runs longer than the simulation time or more than 100 seconds, e.g., 115 seconds, the range of the time axis will be [15, 115]. This particular Behavior of Magic Model Analyst / Cameo Simulation Toolkit's Time series chart is similar to that of Oscilloscope when <strong>fixedTimeLocation</strong> is unspecified. <br class="atl-forced-newline" /><br class="atl-forced-newline" /></p><p style="margin-left: 30.0px;"><ac:image ac:align="center" ac:title="Time Series Chart with 100 Seconds fixedTimeLength Value and Undefined fixedTimeLocation Value" ac:alt="Time Series Chart with 100 Seconds fixedTimeLength Value and Undefined fixedTimeLocation Value"><ri:attachment ri:filename="Time Series Chart with fixedTimeLocation undefined.png" /></ac:image></p><h6 style="text-align: center;">A Time series chart with fixedTimeLength 100 seconds and fixedTimeLocation unspecified running longer than the simulation time.</h6>
````

<!--NOMAGIC_PAGE id=249570984 space=MMA version=4 -->
## PAGE 00726: SSP Export - Technology Preview

- page_id: `249570984`
- space_key: `MMA`
- source_url: https://docs.nomagic.com/spaces/MMA/pages/249570984/SSP+Export+-+Technology+Preview
- version_number: 4
- version_date: `2025-12-15T10:02:43.786+01:00`
- ancestors: Magic Model Analyst / Cameo Simulation Toolkit Documentation > User Guide > Simulation of SysML models
- labels: []

### NORMALIZED CONTENT

To import the SSP file in Dymola

[System Structure and Parametrization (SSP)](https://ssp-standard.org/) is a tool-independent standard used to define complete systems consisting of one or more [CONFLUENCE_PAGE title='FMU import' space='MT'] (FMUs). The FMUs generated by various third-party suppliers can be exported from the modeling tool. The exported SSP file can then be imported to various simulation tools (such as Dymola), enhancing the interoperability. For systems without FMUs, SSP can still be used to export the internal system structure, providing a standardized way to share and reuse system architectures. SSP export works only on instances.

[IMAGE alt='' src='']

###### System structure in the SysML and Modelica.

##### Automatically simulating in Dymola

You can automatically simulate the SSP file in Dymola and export the CSV file to the Results Player in just one click. This method saves you the time and efforts of manually exporting the SSP file in the modeling tool, launching Dymola, Importing and simulating the SSP file, exporting the CSV file and importing the CSV file again into the Results Player.

#### NOTE: Prerequisites

Prerequisites

- You must have the Windows Operating System.
- You must integrate the Dymola application with your modeling tool with help of the Integrations dialog. To open Integrations dialog, click Tools> Integrations .
- You must use the Dymola version 2024x or later.

To automaticallyexport model data to SSP, simulate it inDymola, andthen load the results to the Results Player

1. Right- click the **FMUControl_FMUTank : RequirementsVerification> Simulation**and from the contextual menu select the desired simulation configuration to be simulated in Dymola.**[IMAGE alt='' src='']**

Once simulation is done, results are automatically loaded into the results player.

- You can choose the solver in the project options, click Options> Project> General> Simulation> Dymola Engine.
- The timing properties required for the simulation are used from the simulation configuration.

##### Manually exporting the SSP file from the modeling tool

To export the SSP file

1. In the Containment tree, right-click the instance, and select the Export to SSP command. [ATTACHMENT filename='SSP Export command.png']
2. In the Select Destination Directory, select the location to save the SSP file. [ATTACHMENT filename='Select Destinantion.png']

##### Manually importing and simulating the SSP file in the Dymola

1. Click File>Open>Import SSP. 
 
[IMAGE alt='' src='']
2. In the Import SSP dialog, select the imported SSP file. [ATTACHMENT filename='Import SSP_Dialog.png']
3. I n the Save package FMUControl_FMUTank as Modelica File dialog, save the Modelica file. [ATTACHMENT filename='Save package FMUControl_FMUTank as Modelica File.png']
4. Select the **FMUControl_FMUTank** model in the tree.
5. In the Simulation pane, specify the Stop time for the simulation, and click **Simulate** in the Simulation tab.. The compiler must be set up for the simulation to work. To learn more about setting up the compiler, refer to **Help Documents**in the Tool tab of the Dymola application. [ATTACHMENT filename='Simulation pane.png']
6. Select the required variables from the simulation results in the Variables Browser. The graph for the selected variables is available in the simulation pane. 
 
[IMAGE alt='' src='']

##### Manually exporting the CSV file from the Dymola

To export the CSV file from Dymola

1. In the Variable Browser, right-click the required results and select Export Result>All . [ATTACHMENT filename='Export Results.png']
2. In the Export Result-All dialog, select the location to export the CSV file. [ATTACHMENT filename='Export Results_Dialog.png']

This exported CSV file can be loaded into the [CONFLUENCE_PAGE title='Results Player' space=''] to display numerical values from a CSV file directly in composite structure diagrams.

##### Sample model

The model used in the figures is the WaterTankFMI.mdzip sample, bundled with the modeling tool.

To open the sample

- Find the sample in the modeling tool <install_root>\samples\simulation\fmi\WaterTankFMI.mdzip

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>To import the SSP file in Dymola</p><p><a href="https://ssp-standard.org/">System Structure and Parametrization (SSP)</a> is a tool-independent standard used to define complete systems consisting of one or more <ac:link><ri:page ri:space-key="MT" ri:content-title="FMU import" /><ac:plain-text-link-body><![CDATA[Functional Mock-up Units]]></ac:plain-text-link-body></ac:link> (FMUs). The FMUs generated by various third-party suppliers can be exported from the modeling tool. The exported SSP file can then be imported to various simulation tools (such as Dymola), enhancing the interoperability. For systems without FMUs, SSP can still be used to export the internal system structure, providing a standardized way to share and reuse system architectures. SSP export works only on instances.</p><p><br /></p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="System Structure_Comparison.png" /></ac:image></p><h6 style="text-align: center;"><span style="font-size: 12.0px;font-weight: 600;letter-spacing: 0.0px;color:var(--ds-background-accent-gray-bolder,#626f86);"><ac:inline-comment-marker ac:ref="dc4bf636-049a-4a07-8cc9-df729214f45c">System structure in the SysML and Modelica.</ac:inline-comment-marker></span></h6><h3>Automatically simulating in Dymola</h3><p><span style="color:var(--ds-text,#172b4d);">You can automatically simulate the SSP file in Dymola and export the CSV file to the Results Player in just one click. This method saves you the time and efforts of manually exporting the SSP file in the modeling tool, launching Dymola, Importing and simulating the SSP file, exporting the CSV file and importing the CSV file again into the Results Player.<br /><br /></span></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="41e8c30b-8799-42b5-8a8e-8c08663b6cf8"><ac:parameter ac:name="title">Prerequisites</ac:parameter><ac:rich-text-body><ul><li>You must have the Windows Operating System.</li><li>You must integrate the Dymola application with your modeling tool with help of the Integrations dialog. To open Integrations dialog, click <strong>Tools&gt; Integrations</strong>.</li><li>You must use the Dymola version 2024x or later.</li></ul></ac:rich-text-body></ac:structured-macro><p><br />T<span style="letter-spacing: 0.0px;">o automatically </span><span style="letter-spacing: 0.0px;">export model data to SSP, simulate it in </span><span style="letter-spacing: 0.0px;">Dymola, and</span><span style="letter-spacing: 0.0px;"> </span><span style="letter-spacing: 0.0px;">then load the results to the Results Player</span></p><hr /><ol><li><span style="color:var(--ds-text,#172b4d);">Right- click the <strong>FMUControl_FMUTank : RequirementsVerification&gt; Simulation </strong>and from the contextual menu select the desired simulation configuration to be simulated in Dymola.<strong><br /><br /><ac:image><ri:attachment ri:filename="Automated_simulation_in_dymola.png" /></ac:image><br /><br /></strong></span></li></ol><p><span>Once simulation is done, results are automatically loaded into the results player.</span></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="b7a2d823-09c5-4bed-a557-506c0f18f5f9"><ac:rich-text-body><ul><li>You can choose the solver in the project options, click <strong>Options&gt; Project&gt; General&gt; Simulation&gt; Dymola Engine. </strong></li><li>The timing properties required for the simulation are used from the simulation configuration.</li></ul></ac:rich-text-body></ac:structured-macro><h3>Manually exporting the SSP file from the modeling tool</h3><p>To export the SSP file</p><hr /><ol><li>In the Containment tree, right-click the instance, and select the <strong>Export to SSP</strong> command.<br /><br /><ac:image><ri:attachment ri:filename="SSP Export command.png" /></ac:image><br /><br /></li><li>In the Select Destination Directory, select the location to save the SSP file.<br /><br /><ac:image><ri:attachment ri:filename="Select Destinantion.png" /></ac:image></li></ol><h3>Manually importing and simulating the SSP file in the Dymola</h3><p><br /></p><hr /><ol><li>Click <strong>File&gt;Open&gt;Import SSP.<br /><br /><ac:image><ri:attachment ri:filename="Import SSP.png" /></ac:image><br /><br /></strong></li><li><ac:inline-comment-marker ac:ref="1b1ca785-65e0-46e4-b49a-7ba0e3c3a1fa">In the Import SSP dialog, select the imported SSP file.</ac:inline-comment-marker><br /><br /><ac:image><ri:attachment ri:filename="Import SSP_Dialog.png" /></ac:image><br /><br /></li><li>I<ac:inline-comment-marker ac:ref="40007223-33cc-498a-ae94-75e6796faf29">n the Save package FMUControl_FMUTank as Modelica File dialog, save the Modelica file.</ac:inline-comment-marker><br /><br /><ac:image><ri:attachment ri:filename="Save package FMUControl_FMUTank as Modelica File.png" /></ac:image><br /><br /></li><li><span style="color:var(--ds-text,#172b4d);">Select the <strong>FMUControl_FMUTank</strong> model in the tree.</span></li><li><span style="color:var(--ds-text,#172b4d);">In the Simulation pane, specify the Stop time for the simulation, and click <strong>Simulate</strong> in the Simulation tab..<br /></span><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="3c14fc4f-f5fe-43c4-94d2-631d43d928ba"><ac:rich-text-body><p><span style="color:var(--ds-text,#172b4d);">The compiler must be set up for the simulation to work. To learn more about setting up the compiler, refer to <strong>Help Documents </strong>in the Tool tab of the Dymola application.</span></p></ac:rich-text-body></ac:structured-macro><ac:image><ri:attachment ri:filename="Simulation pane.png" /></ac:image><br /><br /></li><li>Select the required variables from the simulation results in the Variables Browser. The graph <span style="color:var(--ds-text,#172b4d);">for the selected variables </span><span style="letter-spacing: 0.0px;">is available in the simulation pane.<br /><br /><ac:image><ri:attachment ri:filename="Result plot and variables.png" /></ac:image><br /></span></li></ol><h3>Manually exporting the CSV file from the Dymola</h3><p>To export the CSV file from Dymola</p><hr /><ol><li>In the Variable Browser, right-click the required results and select <strong>Export Result&gt;All</strong>.<br /><br /><ac:image><ri:attachment ri:filename="Export Results.png" /></ac:image><br /><br /><br /></li><li>In the Export Result-All dialog, select the location to export the CSV file.<br /><br /><ac:image><ri:attachment ri:filename="Export Results_Dialog.png" /></ac:image><br /><br /></li></ol><p>This exported CSV file can be loaded into the <ac:link><ri:page ri:content-title="Results Player" /></ac:link> to <span style="color:var(--ds-text,#172b4d);">display numerical values from a CSV file directly in composite structure diagrams.</span></p><h3><span style="color:var(--ds-text,#172b4d);">Sample model</span></h3><p><span style="color:var(--ds-text,#172b4d);"><span style="color:var(--ds-text,#172b4d);">The model used in the figures is the WaterTankFMI.mdzip sample, bundled with the modeling tool. </span></span></p><p><span style="color:var(--ds-text,#172b4d);"><span style="color:var(--ds-text,#172b4d);">To open the sample</span></span></p><hr /><ul><li><span style="letter-spacing: 0.0px;">Find the sample in the modeling tool</span><span style="letter-spacing: 0.0px;"> </span><em style="letter-spacing: 0.0px;">&lt;install_root&gt;\samples\simulation\fmi\<span style="color:var(--ds-text,#172b4d);">WaterTankFMI.mdzip</span></em></li></ul>
````

<!--NOMAGIC_PAGE id=249570366 space=MMA version=2 -->
## PAGE 00727: State activation semantics

- page_id: `249570366`
- space_key: `MMA`
- source_url: https://docs.nomagic.com/spaces/MMA/pages/249570366/State+activation+semantics
- version_number: 2
- version_date: `2025-08-19T14:56:11.453+02:00`
- ancestors: Magic Model Analyst / Cameo Simulation Toolkit Documentation > User Guide > State Machine simulation > Adapting models for State Machine simulation
- labels: ['state-activation-semantics']

### NORMALIZED CONTENT

121081268

121081270

121081269

Magic Model Analyst / Cameo Simulation Toolkit provides **State** **Activation** **Semantics** as one of the simulation options. This option allows you to determine whether Magic Model Analyst / Cameo Simulation Toolkit activates an Entry Behavior before or after activating an entry of State. You can select one of the options: **After entry** and **Before entry**. The **After** **entry** option allows activating the entry of State after the Entry Behavior is completely activated. The **Before entry** option allows entering the entry of State before executing the Entry Behavior. 
 
To set the **State Activation** **Semantics** option

1. Open the **[CONFLUENCE_PAGE title='Project options' space='']** dialog.
2. In the **SCXML Engine** group, select **State Activation Semantics**.
3. From the drop-down list, select **After entry** or **Before entry**.
4. Click **OK**. 
 
[IMAGE alt='' src='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="25d15856-43a8-4162-9d5b-14c6e5e5d40e"><ac:parameter ac:name="id">121081268</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="444ec1e3-096c-479c-a3b4-36137663be9a"><ac:parameter ac:name="id">121081270</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="92f1f699-c5cf-47c0-bde9-19244ec60492"><ac:parameter ac:name="id">121081269</ac:parameter><ac:rich-text-body><p>Magic Model Analyst / Cameo Simulation Toolkit provides <strong>State</strong> <strong>Activation</strong> <strong>Semantics</strong> as one of the simulation options. This option allows you to determine whether Magic Model Analyst / Cameo Simulation Toolkit activates an Entry Behavior before or after activating an entry of State. You can select one of the options: <strong>After entry</strong> and <strong>Before entry</strong>. The <strong>After</strong> <strong>entry</strong> option allows activating the entry of State after the Entry Behavior is completely activated. The <strong>Before entry</strong> option allows entering the entry of State before executing the Entry Behavior.<br class="atl-forced-newline" /><br class="atl-forced-newline" />To set the <strong>State Activation</strong> <strong>Semantics</strong> option</p><hr /><ol><li><p>Open the <strong><ac:link><ri:page ri:content-title="Project options" /></ac:link></strong> dialog.</p></li><li><p>In the <strong>SCXML Engine</strong> group, select <strong>State Activation Semantics</strong>.</p></li><li><p>From the drop-down list, select <strong>After entry</strong> or <strong>Before entry</strong>.</p></li><li><p>Click <strong>OK</strong>.<br /><br /><ac:image><ri:attachment ri:filename="State Activation Semantics option.png" /></ac:image></p></li></ol></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=249570580 space=MMA version=3 -->
## PAGE 00728: State invariant

- page_id: `249570580`
- space_key: `MMA`
- source_url: https://docs.nomagic.com/spaces/MMA/pages/249570580/State+invariant
- version_number: 3
- version_date: `2025-09-12T15:08:40.031+02:00`
- ancestors: Magic Model Analyst / Cameo Simulation Toolkit Documentation > User Guide > Interaction simulation > Supported elements in interaction simulation
- labels: ['state-invariant']

### NORMALIZED CONTENT

381703861

381703863

381703862

A State Invariant is one of the UML elements. It is a runtime constraint applied to a lifeline in a Sequence diagram to specify conditions that are always true when a State is a current State. It is used to validate States. You may also specify State Invariants in the States directly. State Invariants on lifelines resolves variables in the same order as it does in message arguments.

When Magic Model Analyst / Cameo Simulation Toolkit runs a State Invariant in a model, it also evaluates its constraints. If the constraints are not satisfied, the evaluation will fail or return false and Magic Model Analyst / Cameo Simulation Toolkit will stop simulation (if "ConstraintAsBreakpoint" is set to true) at that invalid constraint or point. However, you can still continue the simulation to the next point. You can define constraints using any of the supported languages in Magic Model Analyst / Cameo Simulation Toolkit. State Invariants are used mostly in Interactions, but you can also use them in a State Machine diagram.

[IMAGE alt='' src='']

###### A State Invariant containing constraints being evaluated during execution.

Magic Model Analyst / Cameo Simulation Toolkit supports duration constraints between State invariants. The following figure shows the duration constraint, e.g., from *playing* to *playing* takes 5,000 ms of the total simulation time.

[IMAGE alt='' src='']

###### Duration constraints between State invariants are supported.

Time constraints of State invariants will be checked if right States are activated at the right time. When States change, Magic Model Analyst / Cameo Simulation Toolkit will check if active States contain required States, and time is exactly as specified in the constraints. If failed, an error message of the time constraints will be printed in the **Console** pane with the value, time unit, and State invariant name with hyperlinks accordingly, as shown in the figure below.

[IMAGE alt='' src='']

###### The time constraint of the State invariant is checked against the simulation time.

381703860

**Related pages**

- [CONFLUENCE_PAGE title='Lifeline' space='']
- Sequence diagram

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="2a2f2806-d0c2-4249-b0a1-e35a3d5bda0e"><ac:parameter ac:name="id">381703861</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="05f0dc1b-d598-4d05-9373-1ff95b648497"><ac:parameter ac:name="id">381703863</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="fe5e174b-954e-4651-a2c4-5bd5d765d96d"><ac:parameter ac:name="id">381703862</ac:parameter><ac:rich-text-body><p>A State Invariant is one of the UML elements. It is a runtime constraint applied to a lifeline in a Sequence diagram to specify conditions that are always true when a State is a current State. It is used to validate States. You may also specify State Invariants in the States directly. State Invariants on lifelines resolves variables in the same order as it does in message arguments. </p><p>When Magic Model Analyst / Cameo Simulation Toolkit runs a State Invariant in a model, it also evaluates its constraints. If the constraints are not satisfied, the evaluation will fail or return false and Magic Model Analyst / Cameo Simulation Toolkit will stop simulation (if &quot;ConstraintAsBreakpoint&quot; is set to true) at that invalid constraint or point. However, you can still continue the simulation to the next point. You can define constraints using any of the supported languages in Magic Model Analyst / Cameo Simulation Toolkit. State Invariants are used mostly in Interactions, but you can also use them in a State Machine diagram. </p><p style="text-align: center;"><br class="atl-forced-newline" /><ac:image ac:align="center"><ri:attachment ri:filename="State Invariant Containing Constraints.PNG" /></ac:image></p><h6 style="text-align: center;">A State Invariant containing constraints being evaluated during execution.</h6><p class="Textbody">Magic Model Analyst / Cameo Simulation Toolkit supports duration constraints between State invariants. The following figure shows the duration constraint, e.g., from <em>playing</em> to <em>playing</em> takes 5,000 ms of the total simulation time.</p><p class="Textbody" style="text-align: center;"><br /></p><p><ac:image ac:align="center"><ri:attachment ri:filename="State Invariant with Time Constraint.PNG" /></ac:image></p><h6 class="Textbody" style="text-align: center;">Duration constraints between State invariants are supported.</h6><p>Time constraints of State invariants will be checked if right States are activated at the right time. When States change, Magic Model Analyst / Cameo Simulation Toolkit will check if active States contain required States, and time is exactly as specified in the constraints. If failed, an error message of the time constraints will be printed in the <strong>Console</strong> pane with the value, time unit, and State invariant name with hyperlinks accordingly, as shown in the figure below.</p><p><ac:image ac:align="center"><ri:attachment ri:filename="State Invariant.PNG" /></ac:image></p><h6 style="text-align: center;">The time constraint of the State invariant is checked against the simulation time.</h6></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="49a0a486-dcc4-4673-b84d-fc236d69b872"><ac:parameter ac:name="id">381703860</ac:parameter><ac:rich-text-body><p><strong>Related pages</strong></p><ul><li><ac:link><ri:page ri:content-title="Lifeline" /></ac:link></li><li><a href="https://docs.nomagic.com/display/MT/Sequence+diagram">Sequence diagram</a></li></ul></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=249569581 space=MMA version=2 -->
## PAGE 00729: State Machine

- page_id: `249569581`
- space_key: `MMA`
- source_url: https://docs.nomagic.com/spaces/MMA/pages/249569581/State+Machine
- version_number: 2
- version_date: `2025-08-19T14:56:05.257+02:00`
- ancestors: Magic Model Analyst / Cameo Simulation Toolkit Documentation > User Guide > Model simulation > Elements simulation > Behavior
- labels: ['state-machine-simulation', 'simulating-state-machines']

### NORMALIZED CONTENT

1356819412

1356819415

1356819413

Similar to the Activity simulation, when you run a State Machine, Magic Model Analyst / Cameo Simulation Toolkit will create a new session for a State Machine simulation. If there is a State Machine diagram that represents the State Machine, animation effect on the diagram will begin playing at the start of non-silent mode simulation.

###### [IMAGE alt='' src=''] 
Running a State Machine. 
 
[IMAGE alt='' src='']

###### Animation of the State Machine simulation.

1356819411

**Related pages**

- [CONFLUENCE_PAGE title='Activity' space='']
- [CONFLUENCE_PAGE title='Interaction' space='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:macro-id="3e2d7db3-5122-440b-b147-9e7b1013fc6f" ac:name="content-layer" ac:schema-version="1"><ac:parameter ac:name="id">1356819412</ac:parameter><ac:rich-text-body><ac:structured-macro ac:macro-id="7f4cbac4-f04d-4fa3-b138-37fc229e6698" ac:name="content-column" ac:schema-version="1"><ac:parameter ac:name="id">1356819415</ac:parameter><ac:rich-text-body><ac:structured-macro ac:macro-id="398a4d6d-ab46-4cc9-be91-255fafe94546" ac:name="content-block" ac:schema-version="1"><ac:parameter ac:name="id">1356819413</ac:parameter><ac:rich-text-body><p style="text-align: left;"><ac:inline-comment-marker ac:ref="0380d2b7-73cc-498d-ac57-61c6d1e95edd">Similar</ac:inline-comment-marker> to the Activity simulation, when you run a State Machine, Magic Model Analyst / Cameo Simulation Toolkit will create a new session for a State Machine simulation. If there is a State Machine diagram that represents the State Machine, animation effect on the diagram will begin playing at the start of non-silent mode simulation. </p><h6 style="text-align: center;"><br class="atl-forced-newline" /><ac:image ac:alt="Running a State Machine " ac:title="Running a State Machine "><ri:attachment ri:filename="Figure_0006.png" /></ac:image><br class="atl-forced-newline" />Running a State Machine. <br class="atl-forced-newline" /><br class="atl-forced-newline" /><span class="confluence-embedded-file-wrapper confluence-embedded-manual-size"><ac:image ac:alt="Animation of a State Machine Simulation" ac:title="Animation of a State Machine Simulation"><ri:attachment ri:filename="Figure_0007.png"><ri:page ri:content-title="Behavior" /></ri:attachment></ac:image></span></h6><h6 style="text-align: center;"><span class="confluence-embedded-file-wrapper confluence-embedded-manual-size">Animation of the State Machine simulation.</span></h6><p style="text-align: center;"><br /></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:macro-id="d5648e44-508b-4fc8-ab0c-d2385aa2661d" ac:name="content-block" ac:schema-version="1"><ac:parameter ac:name="id">1356819411</ac:parameter><ac:rich-text-body><p><strong>Related pages</strong></p><ul><li><ac:link><ri:page ri:content-title="Activity" /></ac:link></li><li><ac:link><ri:page ri:content-title="Interaction" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=249570391 space=MMA version=4 -->
## PAGE 00730: State Machine duration simulation

- page_id: `249570391`
- space_key: `MMA`
- source_url: https://docs.nomagic.com/spaces/MMA/pages/249570391/State+Machine+duration+simulation
- version_number: 4
- version_date: `2025-09-12T15:08:37.042+02:00`
- ancestors: Magic Model Analyst / Cameo Simulation Toolkit Documentation > User Guide > State Machine simulation
- labels: ['state-duration-in-state-machines']

### NORMALIZED CONTENT

123846598

123846601

123846597

**On this page**

123846599

You can specify a duration constraint on any State in a State Machine. The minimum and maximum duration spent by the State can be provided through **min** and **max** of the duration constraints.

You can use one of the four different modes: min, max, average, and random, to simulate a State that has a duration constraint. You can select a duration mode through the value of the **durationSimulationMode** tag of the «SimulationConfig» stereotype.

Magic Model Analyst / Cameo Simulation Toolkit supports the following time suffixes: ms (millisecond), s (second), m or min (minute), h (hour), and d (day). You can parse the time unit that is specified as a suffix after a number or at the end of an expression string. If you do not specify a suffix, the millisecond will be used by default. The examples are as follows

- 100 m or 100min is 100 minutes.
- xs is the value of the property x in seconds.
- 200 is 200 milliseconds.

#### Min

When you select min as the duration simulation mode, Magic Model Analyst / Cameo Simulation Toolkit will increase the time spent on a State Machine by the min duration specified on the duration constraint when the element, to which a duration constraint is applied, is activated.

#### Max

If you select max as the duration simulation mode, Magic Model Analyst / Cameo Simulation Toolkit will increase the time spent on a State Machine by the max duration specified on the duration constraint when the element, to which a duration constraint is applied, is activated.

#### Average

When Magic Model Analyst / Cameo Simulation Toolkit simulates your model with the average duration simulation mode, it will use the average value between the max and min duration of the duration constraint as the duration of time spent on simulating the element, to which the duration constraint applied.

#### Random

The random mode allows Magic Model Analyst / Cameo Simulation Toolkit to obtain the duration of time spent on simulating an element, to which a duration constraint applied, from a uniformly distributed random number between the min and max duration of the duration constraint.

If you simulate a model without specifying any duration simulation mode, Magic Model Analyst / Cameo Simulation Toolkit will ignore duration constraints and obtain the time spent on simulating the States and State Machines from the simulation clock.

If you simulation a State that has a duration constraint with a duration simulation mode and the time spent on Entry, Exit, and DoActivity Behaviors are beyond the range of the duration constraint specified on the State, the State will be considered as a broken constraint element, and Magic Model Analyst / Cameo Simulation Toolkit will pause the model simulation at the State.

124223797

**Related pages**

- State Machine
- State Machine diagram

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="73f9432c-6331-4b09-aaae-893ddf1caca9"><ac:parameter ac:name="id">123846598</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="4800d69a-5703-464e-a1ad-ba9e31f82bd5"><ac:parameter ac:name="id">123846601</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="f7214356-0eb5-4a63-942f-d2116331bc89"><ac:parameter ac:name="id">123846597</ac:parameter><ac:rich-text-body><p><strong>On this page</strong></p><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="f920e41a-5967-4fef-a8eb-5db339ee4523" /></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="449c9a8f-ac10-484c-86be-c63eef42439f"><ac:parameter ac:name="id">123846599</ac:parameter><ac:rich-text-body><p class="western">You can specify a duration constraint on any State in a State Machine. The minimum and maximum duration spent by the State can be provided through <strong><span>min</span></strong> and <strong><span>max</span></strong> of the duration constraints.</p><p class="western">You can use one of the four different modes: min, max, average, and random, to simulate a State that has a duration constraint. You can select a duration mode through the value of the <strong><span>durationSimulationMode</span></strong> tag of the «SimulationConfig» stereotype. </p><p class="western">Magic Model Analyst / Cameo Simulation Toolkit supports the following time suffixes: ms (millisecond), s (second), m or min (minute), h (hour), and d (day). You can parse the time unit that is specified as a suffix after a number or at the end of an expression string. If you do not specify a suffix, the millisecond will be used by default. The examples are as follows</p><ul><li class="western">100 m or 100min is 100 minutes. </li><li class="western">xs is the value of the property x in seconds. </li><li class="western">200 is 200 milliseconds. </li></ul><h2 class="western">Min</h2><p class="western">When you select min as the duration simulation mode, Magic Model Analyst / Cameo Simulation Toolkit will increase the time spent on a State Machine by the min duration specified on the duration constraint when the element, to which a duration constraint is applied, is activated. </p><h2 class="western">Max</h2><p class="western">If you select max as the duration simulation mode, Magic Model Analyst / Cameo Simulation Toolkit will increase the time spent on a State Machine by the max duration specified on the duration constraint when the element, to which a duration constraint is applied, is activated. </p><h2 class="western">Average</h2><p class="western">When Magic Model Analyst / Cameo Simulation Toolkit simulates your model with the average duration simulation mode, it will use the average value between the max and min duration of the duration constraint as the duration of time spent on simulating the element, to which the duration constraint applied. </p><h2 class="western">Random</h2><p class="western">The random mode allows Magic Model Analyst / Cameo Simulation Toolkit to obtain the duration of time spent on simulating an element, to which a duration constraint applied, from a uniformly distributed random number between the min and max duration of the duration constraint. </p><p class="western">If you simulate a model without specifying any duration simulation mode, Magic Model Analyst / Cameo Simulation Toolkit will ignore duration constraints and obtain the time spent on simulating the States and State Machines from the simulation clock.</p><p class="western">If you simulation a State that has a duration constraint with a duration simulation mode and the time spent on Entry, Exit, and DoActivity Behaviors are beyond the range of the duration constraint specified on the State, the State will be considered as a broken constraint element, and Magic Model Analyst / Cameo Simulation Toolkit will pause the model simulation at the State.</p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="bfa18c8c-69e8-468e-abcb-2ec99b8c2888"><ac:parameter ac:name="id">124223797</ac:parameter><ac:rich-text-body><p><strong>Related pages</strong></p><ul><li><a href="https://docs.nomagic.com/display/MMA/State+Machine">State Machine</a></li><li><a href="https://docs.nomagic.com/display/MT/State+Machine+diagram">State Machine diagram</a></li></ul></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=249570336 space=MMA version=2 -->
## PAGE 00731: State Machine simulation

- page_id: `249570336`
- space_key: `MMA`
- source_url: https://docs.nomagic.com/spaces/MMA/pages/249570336/State+Machine+simulation
- version_number: 2
- version_date: `2025-08-19T14:56:11.024+02:00`
- ancestors: Magic Model Analyst / Cameo Simulation Toolkit Documentation > User Guide
- labels: ['state-machine']

### NORMALIZED CONTENT

115319798

115319801

115319799

Magic Model Analyst / Cameo Simulation Toolkit allows you to perform a State Machine Simulation (State Chart Simulation) on existing State Machine diagrams, based on the W3C SCXML standard. This kind of simulation is frequently used in the early stage of software development by designers or analysts to test the flow of the software to be developed.

The W3C SCXML standard provides a generic State machine-based simulation environment based on the Harel Statechart. SCXML is capable of describing complex State machines, including Substates, concurrency, history, time events, and many more. Most of the things that can be represented as UML statecharts, e.g., business process flows, views on navigation bits, interaction or dialog management, and many more, can leverage the SCXML engine. When executing a State Machine, the SCXML engine is capable of finding an initial state automatically even if the initial node is not defined. This feature is also applicable to composite States and orthogonal States.

In addition to simulating an executable model as a demonstration tool to validate and verify the system Behavior at key milestone reviews, the State Machine simulation supports exporting the UML State Machine to standard SCXML files for further analyses or transformations.

To export the UML State Machine to an SCXML file

1. Open a Simulation project with the State Machine diagram.
2. From the main menu, select File > Export To > SCXML File . The SCXML File dialog opens to select the State Machine diagram exported to an SCXML file. [ATTACHMENT filename='SCXML File Dialog.PNG']
3. Locate the State Machine diagram by doing one of the following:
  - In the Search by Name box, type the name of the State Machine diagram.
  - Click the Tree tab and select the State Machine diagram appearing in the tree.
  - Click the List tab and select the State Machine diagram appearing in the list.
  - At the File Location box, select [ATTACHMENT filename='Ellipsis.png'] to browse the State Machine diagram.
4. Click **OK**. The exported file, e.g., *class.scxml*, will be as follows. texthttp://commons.apache.org/scxml
 
 
 
 
]]>

115319797

**Related pages**

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="a8a01366-546a-44c7-87b2-80d12a646c48"><ac:parameter ac:name="id">115319798</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="fb303175-a858-4f29-b713-c8fdf47d1456"><ac:parameter ac:name="id">115319801</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="a36291e3-87d2-432c-8bf4-c08866c43110"><ac:parameter ac:name="id">115319799</ac:parameter><ac:rich-text-body><p>Magic Model Analyst / Cameo Simulation Toolkit allows you to perform a State Machine Simulation (State Chart Simulation) on existing State Machine diagrams, based on the W3C SCXML standard. This kind of simulation is frequently used in the early stage of software development by designers or analysts to test the flow of the software to be developed. </p><p>The W3C SCXML standard provides a generic State machine-based simulation environment based on the Harel Statechart. SCXML is capable of describing complex State machines, including Substates, concurrency, history, time events, and many more. Most of the things that can be represented as UML statecharts, e.g., business process flows, views on navigation bits, interaction or dialog management, and many more, can leverage the SCXML engine. When executing a State Machine, the SCXML engine is capable of finding an initial state automatically even if the initial node is not defined. This feature is also applicable to composite States and orthogonal States. </p><p>In addition to simulating an executable model as a demonstration tool to validate and verify the system Behavior at key milestone reviews, the State Machine simulation supports exporting the UML State Machine to standard SCXML files for further analyses or transformations.</p><p><br /></p><p>To export the UML State Machine to an SCXML file</p><hr /><ol><li>Open a Simulation project with the State Machine diagram.</li><li>From the main menu, select <strong>File </strong>&gt;<strong> Export To </strong>&gt;<strong> SCXML File</strong>. The <strong>SCXML File</strong> dialog opens to select the State Machine diagram exported to an SCXML file.<br /><br /><ac:image><ri:attachment ri:filename="SCXML File Dialog.PNG" /></ac:image><br /><br /></li><li>Locate the State Machine diagram by doing one of the following:<ul><li>In the <em>Search by Name</em> box, type the name of the State Machine diagram.</li><li>Click the <strong>Tree</strong> tab and select the State Machine diagram appearing in the tree.</li><li>Click the <strong> List </strong> tab and select the State Machine diagram appearing in the list.</li><li>At the <strong> File Location </strong> box, select <ac:image><ri:attachment ri:filename="Ellipsis.png" /></ac:image> to browse the State Machine diagram.</li></ul></li><li><p class="auto-cursor-target">Click <strong>OK</strong>. The exported file, e.g., <em>class.scxml</em>, will be as follows.</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="31124e23-1981-49d6-bc7c-259a7aadf0f8"><ac:parameter ac:name="language">text</ac:parameter><ac:plain-text-body><![CDATA[<scxml xmlns="http://www.w3.org/2005/07/scxml" version="null" initial="initial__20_0_5630196_1596545104923_661917_23868">
	<!-- http://commons.apache.org/scxml -->
	<state id="initial__20_0_5630196_1596545104923_661917_23868">
		<transition target="State_Tests::Do_Activity_in_State::class::class::_20_0_5630196_1596545104918_849035_23846::state">
		</transition>
	</state>
	<state id="State_Tests::Do_Activity_in_State::class::class::_20_0_5630196_1596545104918_849035_23846::state">
		<transition event="s2" target="State_Tests::Do_Activity_in_State::class::class::_20_0_5630196_1596545104918_849035_23846::state2">
		</transition>
		<invoke targettype="doactivity" src="_20_0_5630196_1596545104909_691815_23820">
		</invoke>
	</state>
	<state id="final_State_Tests::Do_Activity_in_State::class::class::_20_0_5630196_1596545104918_849035_23846::final" final="true">
	</state>
	<state id="State_Tests::Do_Activity_in_State::class::class::_20_0_5630196_1596545104918_849035_23846::state2">
		<transition event="COMPLETION_EVENT__20_0_5630196_1596545104923_763628_23871" target="final_State_Tests::Do_Activity_in_State::class::class::_20_0_5630196_1596545104918_849035_23846::final">
		</transition>
	</state>
</scxml>]]></ac:plain-text-body></ac:structured-macro></li></ol></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="8e653b73-74de-4af7-bb97-51cc257d2a4b"><ac:parameter ac:name="id">115319797</ac:parameter><ac:rich-text-body><p><strong>Related pages</strong></p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="abb940b5-6c34-43da-9c4f-736c14c2fcd5" /></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=249571307 space=MMA version=3 -->
## PAGE 00732: Stopwatch model sample

- page_id: `249571307`
- space_key: `MMA`
- source_url: https://docs.nomagic.com/spaces/MMA/pages/249571307/Stopwatch+model+sample
- version_number: 3
- version_date: `2025-09-12T15:08:47.430+02:00`
- ancestors: Magic Model Analyst / Cameo Simulation Toolkit Documentation > Tutorial
- labels: []

### NORMALIZED CONTENT

1779042397

1779042418

1779042408

This tutorial is intended to demonstrate how to create a UML model in MagicDraw that can be executed by Magic Model Analyst / Cameo Simulation Toolkit. The model used in this tutorial is a simple stopwatch whose timer will increment by 1 every second.

This tutorials provides the instructions to create a stopwatch model with MagicDraw and execute the stopwatch model step-by-step. You will also learn how to create a mock-up user interface to use with the stopwatch execution.

Before modeling a stopwatch, you will need to know the stopwatch structure and the stopwatch Behavior.

##### Stopwatch structure

The structure of the stopwatch model in this tutorial is very simple. It only contains a time property, which is typed by an integer. The time property will record the elapsed time when the stopwatch receives a starting Signal. Therefore, the structure of the stopwatch system contains a StopWatch class that has the time property.

##### Stopwatch Behavior

This tutorial uses the State Machine diagram to describe the main Behavior of the stopwatch. The stopwatch has two stages: Initial and final.

A stage consists of four States as follows:

- Ready The State where the stopwatch is ready to start.

- Running When it receives the start Signal, the stopwatch will run, and the timer will start. In this State, the stopwatch will be triggered by a time Event to increment the time value by 1 per second.

- Paused The State where the stopwatch is paused and waiting for the user to restart it.

- Stopped The State where the stopwatch stops running.

1779042396

**Related pages**

- [CONFLUENCE_PAGE title='Executing the StopWatch class' space='']
- [CONFLUENCE_PAGE title='State Machine diagram' space='MT']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="ba5b93a3-9b9f-453a-91db-147755284698"><ac:parameter ac:name="id">1779042397</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="a7e4c1da-1757-414c-8286-524e4ada718e"><ac:parameter ac:name="id">1779042418</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="6666db8f-43e6-4575-9e59-ed4fab50f905"><ac:parameter ac:name="id">1779042408</ac:parameter><ac:rich-text-body><p>This tutorial is intended to demonstrate how to create a UML model in MagicDraw that can be executed by Magic Model Analyst / Cameo Simulation Toolkit. The model used in this tutorial is a simple stopwatch whose timer will increment by 1 every second.</p><p>This tutorials provides the instructions to create a stopwatch model with MagicDraw and execute the stopwatch model step-by-step. You will also learn how to create a mock-up user interface to use with the stopwatch execution.</p><p>Before modeling a stopwatch, you will need to know <span>the stopwatch structure</span> and <span>the stopwatch Behavior</span>.</p><h3>Stopwatch structure</h3><p>The structure of the stopwatch model in this tutorial is very simple. It only contains a time property, which is typed by an integer. The time property will record the elapsed time when the stopwatch receives a starting Signal. Therefore, the structure of the stopwatch system contains a StopWatch class that has the time property.</p><h3>Stopwatch Behavior</h3><p>This tutorial uses the State Machine diagram to describe the main Behavior of the stopwatch. The stopwatch has two stages: Initial and final.</p><p>A stage consists of four States as follows:</p><ul><li>Ready<br />The State where the stopwatch is ready to start. </li></ul><ul><li>Running<br />When it receives the start Signal, the stopwatch will run, and the timer will start. In this State, the stopwatch will be triggered by a time Event to increment the time value by 1 per second. </li></ul><ul><li>Paused<br />The State where the stopwatch is paused and waiting for the user to restart it. </li></ul><ul><li>Stopped<br />The State where the stopwatch stops running.</li></ul></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="58651a98-9f7b-4b52-a9ad-a7bd0b58ec6e"><ac:parameter ac:name="id">1779042396</ac:parameter><ac:rich-text-body><p><strong>Related pages</strong></p><ul><li><ac:link><ri:page ri:content-title="Executing the StopWatch class" /></ac:link></li><li><ac:link><ri:page ri:space-key="MT" ri:content-title="State Machine diagram" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=249570533 space=MMA version=1 -->
## PAGE 00733: Streaming Activity simulation

- page_id: `249570533`
- space_key: `MMA`
- source_url: https://docs.nomagic.com/spaces/MMA/pages/249570533/Streaming+Activity+simulation
- version_number: 1
- version_date: `2021-04-09T06:32:38.431+02:00`
- ancestors: Magic Model Analyst / Cameo Simulation Toolkit Documentation > User Guide > Activity simulation
- labels: ['streaming-activity-simulation', 'streaming-parameters']

### NORMALIZED CONTENT

#### CONTENT-LAYER: To display streaming rate in a diagram

1609640788

#### CONTENT-COLUMN: To display streaming rate in a diagram

1609640799

1609640787

**On this page**

4

#### CONTENT-BLOCK: To display streaming rate in a diagram

1609640789

You can model either *non-streaming* or *streaming* behaviors. Non-streaming behaviors consume their input object tokens at the moment they begin executing and deliver their output object tokens when they finish executing. If a system receives inputs and produces outputs even while behaviors continue to execute, this is referred to as a *streaming* behavior.

An Activity with streaming parameters is terminated in the following cases:

- An Activity whose only streaming parameters are output parameters is terminated once all of its actions finish executing.
- An Activity with streaming input parameters is terminated by an Activity final node or if the execution is explicitly terminated by the Activity that invoked it.
- If the **Terminate Streaming Behaviors by Output Parameter Multiplicity** project option (or Simulation Configuration property), is set to *true*, an Activity with streaming output parameters terminates when each of its output parameters receives a cumulative number of values equal to the upper bound of the parameter multiplicity.

[IMAGE alt='' src='']

###### Non-streaming vs streaming behavior.

You can model a streaming behavior by setting the parameter of a Pin or Activity Parameter Node as streaming.

To set a parameter as streaming

- In the Specification window of a Parameter of a Pin or Activity Parameter Node, set the Is Stream property to true .

[IMAGE alt='' src='']

###### Setting a parameter as streaming.

#### NOTE: Streaming parameter multiplicity

Streaming parameter multiplicity

We recommend specifying the multiplicity of [1..*], [*], or [0..*] if you want to get an unlimited number of tokens. Otherwise, the streaming input parameter stops receiving tokens when it reaches the upper bound of multiplicity.

##### Specifying parameter streaming rate

Streaming rate is the number of objects or values that flow in or out of the parameter per time interval while the behavior or operation is executing. You define input or output parameter streaming rate by specifying the **Rate** property which determines the expected rate at which tokens can arrive at or leave a Pin or Activity Parameter Node.

To specify streaming rate

1. Create an Instance Specification and name, e.g., 3 per min .
2. Open the Specification window of the Instance Specification and set the Specification property to the number of objects or values that flow in or out of the parameter per time interval, e.g., 3.
3. Set the Instance Specification (created in step 1) as the value of the Rate property both for a Pin (or Activity Parameter Node) and for the parameter of that Pin (or Activity Parameter Node).
4. Open the Specification window of the Simulation Configuration and specify the Time Unit property by selecting the time interval per which the selected number of objects or values flow in or out of the parameter. If the Time Unit is not specified, a second is used as the default time interval.

Once you define parameter streaming rate, object tokens flow at fixed time intervals. This means that the specified time interval (step 4) is divided by a specified number of tokens (step 2). For example, if streaming rate is 3/min, object tokens are passed at fixed time intervals of 20s. If a token does not arrive at the specified time, then that time interval is skipped and object token is passed only after the next fixed time interval.If there are more object tokens than an Action can accept, they wait in a corresponding Pin and are passed after the next fixed time interval.

[IMAGE alt='' src='']

#### TIP: To display streaming rate in a diagram

To display streaming rate in a diagram

1. Right-click a Pin or Activity Parameter Node and select Symbol Properties .
2. In the Symbol Properties dialog, set the Show Tagged Values property to true .

##### Streaming Activity animation

The Activity Diagram below shows an example of a streaming Activity where the *Manufacture*, *Paint*, and *Dry* Actions can be executed simultaneously. In this example, the *Manufacture* action has already finished executing and is annotated in green (visited element). The *Dry* and *Paint* Actions are executing simultaneously and are annotated in red (active elements). Note that you can control the held token display (annotated as red bubbles with the number of waiting tokens) in the **Project Options** dialog or Simulation Configuration properties.

The execution of this Activity will not terminate even when all the Actions finish executing.

[IMAGE alt='' src='']

###### An example of a streaming Activity

The following chart displays the timeline of the fully executed streaming Activity displayed above.

[IMAGE alt='' src='']

###### The timeline chart of a streaming Activity Diagram.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="ec69425e-06d8-40c0-9a17-67beb018de4b"><ac:parameter ac:name="id">1609640788</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="c18cc8b1-e8e4-4dfa-82e6-709bd689e6f6"><ac:parameter ac:name="id">1609640799</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="b06c6d2f-5e3f-44bf-842c-442c1b08fa2e"><ac:parameter ac:name="id">1609640787</ac:parameter><ac:rich-text-body><p><strong>On this page</strong></p><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="8fc70071-6949-413b-904f-4ba55318471f"><ac:parameter ac:name="maxLevel">4</ac:parameter></ac:structured-macro></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="7ac3fb55-f192-4dc0-bf08-0804a1728f0f"><ac:parameter ac:name="id">1609640789</ac:parameter><ac:rich-text-body><p>You can model either <em>non-streaming</em> or <em>streaming</em> <ac:inline-comment-marker ac:ref="50c15936-4c5a-4ec7-96f1-e0b24b574d3d">behaviors</ac:inline-comment-marker>. Non-streaming behaviors consume their input object tokens at the moment they begin executing and deliver their output object tokens when they finish executing. If a system receives inputs and produces outputs even while behaviors continue to execute, this is referred to as a <em>streaming</em> behavior.</p><p><ac:inline-comment-marker ac:ref="2ca9a777-eaf5-46f6-bc77-311aed89a64d">An Activity with streaming parameters is terminated in the following cases:</ac:inline-comment-marker></p><ul><li><span style="color: rgb(62,63,64);">An Activity whose only streaming parameters are output parameters is terminated once all of its actions finish executing.</span></li><li>An Activity with streaming input parameters is terminated by an Activity final node or if the execution is explicitly terminated <ac:inline-comment-marker ac:ref="ea815464-05dd-4a33-b619-a5dcbc07ff35">by the Activity that invoked it.</ac:inline-comment-marker></li><li><ac:inline-comment-marker ac:ref="ea815464-05dd-4a33-b619-a5dcbc07ff35">If the <strong>Terminate Streaming Behaviors by Output Parameter Multiplicity</strong> project option (or Simulation Configuration property), is set to <em>true</em>, an Activity with streaming output parameters terminates when each of its output parameters receives a cumulative number of values equal to the upper bound of the parameter multiplicity.</ac:inline-comment-marker></li></ul><p style="text-align: center;"><ac:image><ri:attachment ri:filename="streaming_vs_non-streaming.png" /></ac:image></p><h6 style="text-align: center;"><ac:inline-comment-marker ac:ref="aae594a1-53c3-4194-b95b-e283c4ee2aa9">Non-streaming vs streaming behavior.</ac:inline-comment-marker></h6><p>You can model a streaming behavior by setting the parameter of a Pin or Activity Parameter Node as streaming.</p><p><br /></p><p><ac:inline-comment-marker ac:ref="d6c6b077-1f42-4dca-872d-276ca8c52813">To set a parameter as streaming</ac:inline-comment-marker></p><hr /><ul><li>In the Specification window of a Parameter of a Pin or Activity Parameter Node, set the <strong>Is Stream</strong> property to <em>true</em>.</li></ul><p><br /></p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="setting_parameter_as_streaming.png" /></ac:image></p><h6 style="text-align: center;">Setting a parameter as streaming.</h6><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="d62fa3ec-ed48-40df-af37-c13d86f5db7c"><ac:parameter ac:name="title">Streaming parameter multiplicity</ac:parameter><ac:rich-text-body><p><span style="color: rgb(0,0,0);">We recommend specifying the multiplicity of [1..*], [*], or [0..*] if you want to get an unlimited number of tokens. Otherwise, the streaming input parameter stops receiving tokens when it reaches the upper bound of multiplicity.</span></p></ac:rich-text-body></ac:structured-macro><h3><br />Specifying parameter streaming rate</h3><p>Streaming rate is the number of objects or values that flow in or out of the parameter per time interval while the behavior or operation is executing. You define input or output parameter streaming rate by specifying the <strong>Rate</strong> property which determines the expected rate at which tokens can arrive at or leave a Pin or Activity Parameter Node.</p><p><br /></p><p>To specify streaming rate</p><hr /><ol><li>Create an Instance Specification and name, e.g., <em>3 per min</em>.</li><li>Open the Specification window of the Instance Specification and set the <strong>Specification</strong> property to the number of objects or values that flow in or out of the parameter per time interval, e.g., 3.</li><li>Set the Instance Specification (created in step 1) as the value of the <strong>Rate</strong> property both for a Pin (or Activity Parameter Node) and for the parameter of that Pin (or Activity Parameter Node).</li><li>Open the Specification window of the Simulation Configuration and specify the <strong>Time Unit</strong> property by selecting the time interval per which the selected number of objects or values flow in or out of the parameter. If the <strong>Time Unit</strong> is not specified, a second is used as the default time interval.</li></ol><p><br />Once you define parameter streaming rate, object tokens flow at fixed time intervals. This means that the specified time interval (step 4) is divided by a specified number of tokens (step 2). For example, if streaming rate is 3/min, object tokens are passed at fixed time intervals of 20<ac:inline-comment-marker ac:ref="9feb0d19-ab05-4498-822c-5a2710e5fa11"> s</ac:inline-comment-marker>. <span>If a token does not arrive at the specified time, then that time interval is skipped and object token is passed only after the next fixed time interval. </span>If there are more object tokens than an Action can accept, they wait in a corresponding Pin and are passed after the next fixed time interval.</p><p><br /></p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="displaying_streaming_rate.png" /></ac:image></p><p><br /></p><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="89719cfb-b635-4cf1-8fc1-46d8dcaf6d31"><ac:parameter ac:name="title">To display streaming rate in a diagram</ac:parameter><ac:rich-text-body><ol><li>Right-click <ac:inline-comment-marker ac:ref="84bcbd11-2043-4b45-82a2-1192964a49e2">a Pin or Activity Parameter Node and</ac:inline-comment-marker> select <strong>Symbol Properties</strong>.</li><li>In the <strong>Symbol Properties</strong> dialog, set the <strong>Show Tagged Values</strong> property to <em>true</em>.</li></ol></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><h3>Streaming Activity animation</h3><p>The Activity Diagram below shows an example of a streaming Activity where the <em>Manufacture</em>, <em>Paint</em>, and <em>Dry</em> Actions can be executed simultaneously. In this example, the <em>Manufacture</em> action has already finished executing and is annotated in green (visited element). The <em>Dry</em> and <em>Paint</em> Actions are executing simultaneously and are annotated in red (active elements). <span style="color: rgb(62,63,64);">Note that you can control the held token display (annotated as red bubbles with the number of waiting tokens) in the <strong>Project Options</strong> dialog or Simulation Configuration properties</span>.</p><p>The execution of this Activity will not terminate even when all the Actions finish executing.</p><p><br /></p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="streaming_activity_simulation.png" /></ac:image></p><h6 style="text-align: center;"><ac:inline-comment-marker ac:ref="70694756-6fed-4957-8140-3a54dbb8a96c">An example of a streaming Activity</ac:inline-comment-marker></h6><p><br /></p><p><ac:inline-comment-marker ac:ref="98526b6f-3b5a-400b-b853-4226f7c3b0c7">The following chart displays the timeline of the fully executed streaming Activity displayed above.</ac:inline-comment-marker></p><p><ac:inline-comment-marker ac:ref="98526b6f-3b5a-400b-b853-4226f7c3b0c7"><br /></ac:inline-comment-marker></p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="timeline_chart.png" /></ac:image></p><h6 style="text-align: center;">The timeline chart of a streaming Activity Diagram.</h6></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=249569651 space=MMA version=2 -->
## PAGE 00734: Subset property

- page_id: `249569651`
- space_key: `MMA`
- source_url: https://docs.nomagic.com/spaces/MMA/pages/249569651/Subset+property
- version_number: 2
- version_date: `2025-08-19T14:56:05.722+02:00`
- ancestors: Magic Model Analyst / Cameo Simulation Toolkit Documentation > User Guide > Model simulation
- labels: ['subset-properties']

### NORMALIZED CONTENT

Magic Model Analyst / Cameo Simulation Toolkit supports and includes Subset properties in a simulation. It initializes subsets at the beginning of simulation and also updates their values during simulation. The following figure demonstrates a model with subsets

[IMAGE alt='' src='']

###### A Model with Subsets.

When the Magic Model Analyst / Cameo Simulation Toolkit starts running the model, it will add all runtime values of the subsetting properties to the subsetted properties as illustrated in the following figure

[IMAGE alt='' src='']

###### Subsets after being initialized.

You can update or add a value in the subsetting or subsetted properties. Removing or changing a value in the set of values of a subsetting property will cause the value to disappear or will cause a change in the set of values in the subsetted property, and vice versa. Adding a value to the set of values in the subsetted property causes it to appear in the set of values in the subsetting property.

##### Sample model

The model used in the figures on this page is the **SpacecraftMassRollup**sample model that comes with your modeling tool.

To open this sample, do either of the following

- Download ** [ATTACHMENT filename='SpacecraftMassRollup.mdzip'] .
- Find it in the modeling tool <**install_root**>\samples\simulation\SpacecraftMassRollup.mdzip.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>Magic Model Analyst / Cameo Simulation Toolkit supports and includes Subset properties in a simulation. It initializes subsets at the beginning of simulation and also updates their values during simulation. The following figure demonstrates a model with subsets</p><p><ac:image ac:align="center" ac:title="A Model with Subsets" ac:alt="A Model with Subsets"><ri:attachment ri:filename="subsetProperties.png" /></ac:image></p><h6 style="text-align: center;">A Model with Subsets.</h6><p>When the Magic Model Analyst / Cameo Simulation Toolkit starts running the model, it will add all runtime values of the subsetting properties to the subsetted properties as illustrated in the following figure <br class="atl-forced-newline" /><br class="atl-forced-newline" /></p><p><ac:image ac:align="center" ac:title="Subsets after Being Initialized" ac:alt="Subsets after Being Initialized"><ri:attachment ri:filename="initializedSubset.png" /></ac:image></p><h6 style="text-align: center;">Subsets after being initialized.<br class="atl-forced-newline" /> </h6><p>You can update or add a value in the subsetting or subsetted properties. Removing or changing a value in the set of values of a subsetting property will cause the value to disappear or will cause a change in the set of values in the subsetted property, and vice versa. Adding a value to the set of values in the subsetted property causes it to appear in the set of values in the subsetting property.</p><h3>Sample model</h3><p>The model used in the figures on this page is the <strong>SpacecraftMassRollup </strong>sample model that comes with your modeling tool.</p><p><br /></p><p>To open this sample, do either of the following</p><hr /><ul><li>Download<span class="confluence-link"><em> </em></span><ac:link><ri:attachment ri:filename="SpacecraftMassRollup.mdzip" /></ac:link>.</li><li>Find it in the modeling tool <em>&lt;<em style=""><em style="text-align: left;">install_root</em></em>&gt;\samples\simulation\SpacecraftMassRollup.mdzip.</em></li></ul>
````

<!--NOMAGIC_PAGE id=249571572 space=MMA version=2 -->
## PAGE 00735: Support

- page_id: `249571572`
- space_key: `MMA`
- source_url: https://docs.nomagic.com/spaces/MMA/pages/249571572/Support
- version_number: 2
- version_date: `2025-09-12T15:11:11.533+02:00`
- ancestors: Magic Model Analyst / Cameo Simulation Toolkit Documentation
- labels: []

### NORMALIZED CONTENT

[CONFLUENCE_PAGE title='Support' space='SUP']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><ac:structured-macro ac:name="include" ac:schema-version="1" ac:macro-id="95d7f34d-fd75-4318-8072-426556c368e4"><ac:parameter ac:name=""><ac:link><ri:page ri:space-key="SUP" ri:content-title="Support" /></ac:link></ac:parameter></ac:structured-macro></p>
````

<!--NOMAGIC_PAGE id=249570339 space=MMA version=1 -->
## PAGE 00736: Supported elements

- page_id: `249570339`
- space_key: `MMA`
- source_url: https://docs.nomagic.com/spaces/MMA/pages/249570339/Supported+elements
- version_number: 1
- version_date: `2024-01-10T11:17:20.379+01:00`
- ancestors: Magic Model Analyst / Cameo Simulation Toolkit Documentation > User Guide > State Machine simulation
- labels: ['supported-elements-on-state-machine-diagram']

### NORMALIZED CONTENT

Most of the elements on a State Machine diagram are supported as follows

| Element Type | Executable (Yes/No) | Exportable to SCXML (Yes/No) |
| --- | --- | --- |
| state | Yes | Yes |
| composite state | Yes | Yes |
| orthogonal state | Yes | Yes |
| submachine state | Yes | Yes |
| initial state | Yes | Yes |
| final state | Yes | Yes |
| onEntry (entry behavior) | Yes | Yes |
| onExit (exit behavior) | Yes | Yes |
| onTransition | Yes | Yes |
| doActivity | Yes | Yes |
| time event | Yes | Yes |
| deep history | Yes | Yes |
| shallow history | Yes | Yes |
| transition | Yes | Yes |
| transition-to-self | Yes | Yes |
| choice | Yes | Yes |
| junction | Yes | Yes |

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>Most of the elements on a State Machine diagram are supported as follows</p><table class="wrapped relative-table" style="margin-left: 30.0px;width: 66.6142%;"><colgroup><col style="width: 27.574%;" /><col style="width: 26.2722%;" /><col style="width: 46.1538%;" /></colgroup><tbody style="margin-left: 30.0px;"><tr style="margin-left: 30.0px;"><th style="margin-left: 30.0px;"><p>Element Type</p></th><th style="margin-left: 30.0px;"><p>Executable (Yes/No)</p></th><th style="margin-left: 30.0px;"><p>Exportable to SCXML (Yes/No)</p></th></tr><tr style="margin-left: 30.0px;"><td style="margin-left: 30.0px;"><p style="margin-left: 30.0px;">state</p></td><td style="margin-left: 30.0px;"><p style="margin-left: 30.0px;">Yes</p></td><td style="margin-left: 30.0px;"><p style="margin-left: 30.0px;">Yes</p></td></tr><tr style="margin-left: 30.0px;"><td style="margin-left: 30.0px;"><p style="margin-left: 30.0px;">composite state</p></td><td style="margin-left: 30.0px;"><p style="margin-left: 30.0px;">Yes</p></td><td style="margin-left: 30.0px;"><p style="margin-left: 30.0px;">Yes</p></td></tr><tr style="margin-left: 30.0px;"><td style="margin-left: 30.0px;"><p style="margin-left: 30.0px;">orthogonal state</p></td><td style="margin-left: 30.0px;"><p style="margin-left: 30.0px;">Yes</p></td><td style="margin-left: 30.0px;"><p style="margin-left: 30.0px;">Yes</p></td></tr><tr style="margin-left: 30.0px;"><td style="margin-left: 30.0px;"><p style="margin-left: 30.0px;">submachine state</p></td><td style="margin-left: 30.0px;"><p style="margin-left: 30.0px;">Yes</p></td><td style="margin-left: 30.0px;"><p style="margin-left: 30.0px;">Yes</p></td></tr><tr style="margin-left: 30.0px;"><td style="margin-left: 30.0px;"><p style="margin-left: 30.0px;">initial state</p></td><td style="margin-left: 30.0px;"><p style="margin-left: 30.0px;">Yes</p></td><td style="margin-left: 30.0px;"><p style="margin-left: 30.0px;">Yes</p></td></tr><tr style="margin-left: 30.0px;"><td style="margin-left: 30.0px;"><p style="margin-left: 30.0px;">final state</p></td><td style="margin-left: 30.0px;"><p style="margin-left: 30.0px;">Yes</p></td><td style="margin-left: 30.0px;"><p style="margin-left: 30.0px;">Yes</p></td></tr><tr style="margin-left: 30.0px;"><td style="margin-left: 30.0px;"><p style="margin-left: 30.0px;">onEntry <span style="color: rgb(62,63,64);">(entry behavior)</span></p></td><td style="margin-left: 30.0px;"><p style="margin-left: 30.0px;">Yes</p></td><td style="margin-left: 30.0px;"><p style="margin-left: 30.0px;">Yes</p></td></tr><tr style="margin-left: 30.0px;"><td style="margin-left: 30.0px;"><p style="margin-left: 30.0px;">onExit <span style="color: rgb(62,63,64);">(exit behavior)</span></p></td><td style="margin-left: 30.0px;"><p style="margin-left: 30.0px;">Yes</p></td><td style="margin-left: 30.0px;"><p style="margin-left: 30.0px;">Yes</p></td></tr><tr style="margin-left: 30.0px;"><td style="margin-left: 30.0px;"><p style="margin-left: 30.0px;">onTransition</p></td><td style="margin-left: 30.0px;"><p style="margin-left: 30.0px;">Yes</p></td><td style="margin-left: 30.0px;"><p style="margin-left: 30.0px;">Yes</p></td></tr><tr style="margin-left: 30.0px;"><td style="margin-left: 30.0px;"><p style="margin-left: 30.0px;">doActivity</p></td><td style="margin-left: 30.0px;"><p style="margin-left: 30.0px;">Yes</p></td><td style="margin-left: 30.0px;"><p style="margin-left: 30.0px;">Yes</p></td></tr><tr style="margin-left: 30.0px;"><td style="margin-left: 30.0px;"><p style="margin-left: 30.0px;">time event</p></td><td style="margin-left: 30.0px;"><p style="margin-left: 30.0px;">Yes</p></td><td style="margin-left: 30.0px;"><p style="margin-left: 30.0px;">Yes</p></td></tr><tr style="margin-left: 30.0px;"><td style="margin-left: 30.0px;"><p style="margin-left: 30.0px;">deep history</p></td><td style="margin-left: 30.0px;"><p style="margin-left: 30.0px;">Yes</p></td><td style="margin-left: 30.0px;"><p style="margin-left: 30.0px;">Yes</p></td></tr><tr style="margin-left: 30.0px;"><td style="margin-left: 30.0px;"><p style="margin-left: 30.0px;">shallow history</p></td><td style="margin-left: 30.0px;"><p style="margin-left: 30.0px;">Yes</p></td><td style="margin-left: 30.0px;"><p style="margin-left: 30.0px;">Yes</p></td></tr><tr style="margin-left: 30.0px;"><td style="margin-left: 30.0px;"><p style="margin-left: 30.0px;">transition</p></td><td style="margin-left: 30.0px;"><p style="margin-left: 30.0px;">Yes</p></td><td style="margin-left: 30.0px;"><p style="margin-left: 30.0px;">Yes</p></td></tr><tr style="margin-left: 30.0px;"><td style="margin-left: 30.0px;"><p style="margin-left: 30.0px;">transition-to-self</p></td><td style="margin-left: 30.0px;"><p style="margin-left: 30.0px;">Yes</p></td><td style="margin-left: 30.0px;"><p style="margin-left: 30.0px;">Yes</p></td></tr><tr style="margin-left: 30.0px;"><td style="margin-left: 30.0px;"><p style="margin-left: 30.0px;">choice</p></td><td style="margin-left: 30.0px;"><p style="margin-left: 30.0px;">Yes</p></td><td style="margin-left: 30.0px;"><p style="margin-left: 30.0px;">Yes</p></td></tr><tr style="margin-left: 30.0px;"><td style="text-align: left;margin-left: 30.0px;" colspan="1"><p style="margin-left: 30.0px;"><span>junction</span></p></td><td style="margin-left: 90.0px;" colspan="1"><p style="margin-left: 30.0px;"><span>Yes</span></p></td><td style="margin-left: 60.0px;" colspan="1"><p style="margin-left: 30.0px;"><span>Yes</span></p></td></tr></tbody></table><p class="auto-cursor-target"><br /></p>
````

<!--NOMAGIC_PAGE id=249570559 space=MMA version=2 -->
## PAGE 00737: Supported elements in interaction simulation

- page_id: `249570559`
- space_key: `MMA`
- source_url: https://docs.nomagic.com/spaces/MMA/pages/249570559/Supported+elements+in+interaction+simulation
- version_number: 2
- version_date: `2025-08-19T14:50:59.245+02:00`
- ancestors: Magic Model Analyst / Cameo Simulation Toolkit Documentation > User Guide > Interaction simulation
- labels: ['interaction-simulation-elements']

### NORMALIZED CONTENT

272464035

272464037

272464036

Elements supported in interaction simulation include the following items:

- Lifeline Locating the sources and targets of Messages.
- Message Signal, Call, and Reply Messages indicating communication between Lifelines of Interaction.
- CallEvent Used when Operations are called without Methods.
- Duration constraint. Delaying delivery of two Messages run consecutively.
- Time constraint As timestamps when recording simulation.
- State invariant Validating whether current States are true.
- Test case verdict As generated values in the Behavior return parameter.
- Combined fragment A combination of Interaction fragments as choices of Behaviors and loops.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="ddefae23-a147-46ed-9c3c-56db63aa1f0e"><ac:parameter ac:name="id">272464035</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="8aa6cffa-3a9b-4f87-8785-ce123e202aa9"><ac:parameter ac:name="id">272464037</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="11b74978-a1b7-4ca5-bdd3-55f5deed8c4b"><ac:parameter ac:name="id">272464036</ac:parameter><ac:rich-text-body><p>Elements supported in interaction simulation include the following items:</p><p><br /></p><ul class="childpages-macro"><li><a href="https://docs.nomagic.com/display/MMA/Lifeline">Lifeline<br /></a>Locating the sources and targets of Messages.<br /><br /></li><li><a href="https://docs.nomagic.com/display/MMA/Message">Message<br /></a>Signal, Call, and Reply Messages indicating communication between Lifelines of Interaction.<br /><br /></li><li><a href="https://docs.nomagic.com/display/MMA/CallEvent">CallEvent<br /></a>Used when Operations are called without Methods.<br /><br /></li><li><a href="https://docs.nomagic.com/display/MMA/Duration+constraint">Duration constraint.<br /></a>Delaying delivery of two Messages run consecutively.<br /><br /></li><li><a href="https://docs.nomagic.com/display/MMA/Time+constraint">Time constraint<br /></a>As timestamps when recording simulation.<br /><br /></li><li><a href="https://docs.nomagic.com/display/MMA/State+invariant">State invariant<br /></a>Validating whether current States are true.<br /><br /></li><li><a href="https://docs.nomagic.com/display/MMA/Test+case+verdict">Test case verdict<br /></a>As generated values in the Behavior return parameter.<br /><br /></li><li><a href="https://docs.nomagic.com/display/MMA/Combined+fragment">Combined fragment</a><br />A combination of Interaction fragments as choices of Behaviors and loops.</li></ul></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=249571006 space=MMA version=3 -->
## PAGE 00738: Supported scripting languages

- page_id: `249571006`
- space_key: `MMA`
- source_url: https://docs.nomagic.com/spaces/MMA/pages/249571006/Supported+scripting+languages
- version_number: 3
- version_date: `2026-01-05T10:19:10.795+01:00`
- ancestors: Magic Model Analyst / Cameo Simulation Toolkit Documentation > User Guide > Action languages
- labels: ['scripting-languages']

### NORMALIZED CONTENT

Magic Model Analyst / Cameo Simulation Toolkit includes several scripting languages out of the box :

- BeanShell
- [CONFLUENCE_PAGE title='Built-in Math' space='']
- Groovy
- JavaScript Rhino (default)
- Python (Jython): you can call an external Python library (*.py), e.g., from lib1 import fc1, fc2 , in two ways:
  - Use import sys and sys.path commands to get the working directory of Python. Then copy the *.py file to the returned directory prior to calling the library.
  - Use **import sys** and **sys.path.append(pathOfFile)** prior to calling the library. text

These languages can be used as the language of any OpaqueExpression or OpaqueAction anywhere in the model.

When CST is integrated with external Math engines (e.g. MATLAB or Mathematica), corresponding languages are also added into the supported language list.

Additionally, you can download and install any other JSR-223 standard compatible language.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>Magic Model Analyst / Cameo Simulation Toolkit includes several scripting languages out of the box :</p><ul><li>BeanShell</li><li><ac:link><ri:page ri:content-title="Built-in Math" /></ac:link></li><li>Groovy</li><li>JavaScript Rhino (default)</li><li>Python (Jython): you can call an external Python library (*.py), e.g., <em>from lib1 import fc1, fc2</em>, in two ways:<ul><li>Use <strong>import sys</strong> and <strong>sys.path</strong> commands to get the working directory of Python. Then copy the <strong>*.py</strong> file to the returned directory prior to calling the library.</li><li><p class="auto-cursor-target">Use <strong>import sys</strong> and <strong>sys.path.append(pathOfFile)</strong> prior to calling the library.</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="2c2e527f-f011-4476-a297-4f2d7e5d564f"><ac:parameter ac:name="language">text</ac:parameter><ac:plain-text-body><![CDATA[import sys
sys.path.append(pathOfFile) // e.g. "C:\Python\Test"
from lib1 import fc1, fc2]]></ac:plain-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></li></ul></li></ul><p>These languages can be used as the language of any OpaqueExpression or OpaqueAction anywhere in the model.</p><p>When CST is integrated with external Math engines (e.g. MATLAB or Mathematica), corresponding languages are also added into the supported language list.</p><p>Additionally, you can download and install any other JSR-223 standard compatible language.</p>
````

<!--NOMAGIC_PAGE id=249570859 space=MMA version=2 -->
## PAGE 00739: Supported SysML elements

- page_id: `249570859`
- space_key: `MMA`
- source_url: https://docs.nomagic.com/spaces/MMA/pages/249570859/Supported+SysML+elements
- version_number: 2
- version_date: `2025-08-19T14:56:17.269+02:00`
- ancestors: Magic Model Analyst / Cameo Simulation Toolkit Documentation > User Guide > Simulation of SysML models
- labels: ['supported-sysml-elements']

### NORMALIZED CONTENT

710319658

710319660

710319659

The SysML elements that Magic Model Analyst / Cameo Simulation Toolkit supports are outlined below:

- [CONFLUENCE_PAGE title='Accept Change Structural Feature Event Action' space=''] An accept event action that waits for a Change Structural Feature Event.
- [CONFLUENCE_PAGE title='Adjunct property' space=''] A property to which the «AdjunctProperty» stereotype is applied.
- [CONFLUENCE_PAGE title='Binding Connector' space=''] A Connector that the «BindingConnector» stereotype is applied to and specifying that properties at both ends of a connector have equal values.
- [CONFLUENCE_PAGE title='Block' space=''] A UML Class stereotyped with «Block».
- [CONFLUENCE_PAGE title='Association Block' space=''] A Block containing an instance that can link instances of the end Classifiers of the Association together.
- [CONFLUENCE_PAGE title='BoundReference' space=''] A property applying the «BoundReference» stereotype that requires a binding Connector to a property or nested property of an owning Block.
- [CONFLUENCE_PAGE title='Change Structural Feature Event' space=''] An Event that occurs when a value of a specified structural feature on the Event changes.
- [CONFLUENCE_PAGE title='Classifier Behavior property' space=''] A property to which the stereotype «ClassifierBehaviorProperty» is applied that the value of a classifier Behavior property is a Behavior simulation of the classifier Behavior of an object.
- [CONFLUENCE_PAGE title='Constraint Block' space=''] A class stereotyped with «ConstraintBlock» that has a constraint with an expression to constrain the values of its constraint parameters.
- [CONFLUENCE_PAGE title='Flow property' space=''] A property to which the stereotype «FlowProperty» is applied and has a flow direction.
- [CONFLUENCE_PAGE title='Full Port' space=''] A port stereotyped with «FullPort» that specifies a separate element of an owning block.
- [CONFLUENCE_PAGE title='Invocation on nested Port Action' space=''] Magic Model Analyst / Cameo Simulation Toolkit uses the tagged value onNestedPort to send a signal if a send signal Action is stereotyped with «InvocationOnNestedPortAction».
- [CONFLUENCE_PAGE title='Nested Connector end' space=''] If the ends of a connector that connects properties are stereotyped with «NestedConnectorEnd», Magic Model Analyst / Cameo Simulation Toolkit uses the information from the propertyPath of the nested connector end to find the right objects that specify the properties at both ends of the connector.
- [CONFLUENCE_PAGE title='Probability' space=''] A stereotype in SysML applied to outgoing edges of decision nodes and object nodes that Magic Model Analyst / Cameo Simulation Toolkit uses its probability value to select one outgoing edge from other outgoing edges to go to.
- [CONFLUENCE_PAGE title='Proxy Port' space=''] A port stereotyped with «ProxyPort» that the value specifying the proxy port is the reference of the object that is the target of the flow.
- [CONFLUENCE_PAGE title='Trigger on nested Port' space=''] A trigger stereotyped with «TriggerOnNestedPort» that Magic Model Analyst / Cameo Simulation Toolkit uses the tagged value onNestedPort to check the port and find which object receives the triggering Events.
- [CONFLUENCE_PAGE title='Value type' space=''] A data type stereotyped with «ValueType» that allows you to define a value type for typing value properties in a model.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="cd64937a-223c-41f1-9290-12935e98c766"><ac:parameter ac:name="id">710319658</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="f3505a08-5ada-442f-ab58-90eb3835cd6b"><ac:parameter ac:name="id">710319660</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="b517a9c3-b43c-4e72-bb67-d6bac4e4a928"><ac:parameter ac:name="id">710319659</ac:parameter><ac:rich-text-body><p>The SysML elements that Magic Model Analyst / Cameo Simulation Toolkit supports are outlined below:</p><p><br /></p><ul><li><ac:link><ri:page ri:content-title="Accept Change Structural Feature Event Action" /></ac:link><br />An accept event action that waits for a Change Structural Feature Event.<br /><br /></li><li><ac:link><ri:page ri:content-title="Adjunct property" /></ac:link><br />A property to which the «AdjunctProperty» stereotype is applied.<br /><br /></li><li><ac:link><ri:page ri:content-title="Binding Connector" /></ac:link><br />A Connector that the «BindingConnector» stereotype is applied to and specifying that properties at both ends of a connector have equal values.<br /><br /></li><li><ac:link><ri:page ri:content-title="Block" /></ac:link><br />A UML Class stereotyped with «Block».<br /><br /></li><li><ac:link><ri:page ri:content-title="Association Block" /></ac:link><br />A Block containing an instance that can link instances of the end Classifiers of the Association together.<br /><br /></li><li><ac:link><ri:page ri:content-title="BoundReference" /></ac:link><br />A property applying the «BoundReference» stereotype that requires a binding Connector to a property or nested property of an owning Block.<br /><br /></li><li><ac:link><ri:page ri:content-title="Change Structural Feature Event" /></ac:link><br />An Event that occurs when a value of a specified structural feature on the Event changes. <br /><br /></li><li><ac:link><ri:page ri:content-title="Classifier Behavior property" /></ac:link><br />A property to which the stereotype «ClassifierBehaviorProperty» is applied that the value of a classifier Behavior property is a Behavior simulation of the classifier Behavior of an object.<br /><br /></li><li><ac:link><ri:page ri:content-title="Constraint Block" /></ac:link><br />A class stereotyped with «ConstraintBlock» that has a constraint with an expression to constrain the values of its constraint parameters.<br /><br /></li><li><ac:link><ri:page ri:content-title="Flow property" /></ac:link><br />A property to which the stereotype «FlowProperty» is applied and has a flow direction.<br /><br /></li><li><ac:link><ri:page ri:content-title="Full Port" /></ac:link><br />A port stereotyped with «FullPort» that specifies a separate element of an owning block.<br /><br /></li><li><ac:link><ri:page ri:content-title="Invocation on nested Port Action" /></ac:link><br /><p>Magic Model Analyst / Cameo Simulation Toolkit uses the tagged value onNestedPort to send a signal if a send signal Action is stereotyped with «InvocationOnNestedPortAction».</p><p><br /></p></li><li><ac:link><ri:page ri:content-title="Nested Connector end" /></ac:link><br /><p>If the ends of a connector that connects properties are stereotyped with «NestedConnectorEnd», Magic Model Analyst / Cameo Simulation Toolkit uses the information from the propertyPath of the nested connector end to find the right objects that specify the properties at both ends of the connector.<br /><br /></p></li><li><ac:link><ri:page ri:content-title="Probability" /></ac:link><br />A stereotype in SysML applied to outgoing edges of decision nodes and object nodes that Magic Model Analyst / Cameo Simulation Toolkit uses its probability value to select one outgoing edge from other outgoing edges to go to.<br /><br /></li><li><ac:link><ri:page ri:content-title="Proxy Port" /></ac:link><br />A port stereotyped with «ProxyPort» that the value specifying the proxy port is the reference of the object that is the target of the flow.<br /><br /></li><li><ac:link><ri:page ri:content-title="Trigger on nested Port" /></ac:link><br /><p>A trigger stereotyped with «TriggerOnNestedPort» that Magic Model Analyst / Cameo Simulation Toolkit uses the tagged value onNestedPort to check the port and find which object receives the triggering Events.</p><p><br /></p></li><li><ac:link><ri:page ri:content-title="Value type" /></ac:link><br />A data type stereotyped with «ValueType» that allows you to define a value type for typing value properties in a model.</li></ul></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=249569614 space=MMA version=3 -->
## PAGE 00740: Table

- page_id: `249569614`
- space_key: `MMA`
- source_url: https://docs.nomagic.com/spaces/MMA/pages/249569614/Table
- version_number: 3
- version_date: `2025-08-19T14:56:05.635+02:00`
- ancestors: Magic Model Analyst / Cameo Simulation Toolkit Documentation > User Guide > Model simulation > Elements simulation
- labels: ['simulating-tables', 'table-simulation', 'generic-table-simulation', 'instance-table-simulation']

### NORMALIZED CONTENT

#### CONTENT-LAYER: Note

1965719714

#### CONTENT-COLUMN: Note

1965719719

1965719713

**On this page**

33

#### CONTENT-BLOCK: Note

1965719717

Magic Model Analyst / Cameo Simulation Toolkit provides the means to simulate a set of elements iteratively using a Generic Table or an Instance Table. Each element in the table will be simulated one-by-one from the first to the last row.

You can run the table by specifying it as a target of a Simulation Configuration and then run the Simulation Configuration. You can also run an Instance or Generic Table using the toolbar button. The toolbar button is dynamic. If you do not select any rows in the table, the toolbar button is **Evaluate**. However, if you select a row in the table, the toolbar button will change to **Evaluate Selected Rows**.

To run a Generic Table or an Instance Table

- Open the table you want to run and do one of the following: [IMAGE alt='' src=''] NoteFor a model that has Behaviors (Classifier Behavior and/or Part Property with Behaviors), see the **autoStart** tag in [SimulationConfig](https://docs.nomagic.com/display/MMA/SimulationConfig+stereotype).
  - If you want to run the entire table, click the Evaluate button in the table toolbar.
  - If you want to run just the selected rows, select the rows you want to run and click the Evaluate Selected Rows button .

##### Running Instance Tables using Simulation Configurations

You can run an entire Instance Table or the selected rows in it by using a compatible Simulation Configuration. The Simulation Configuration compatibility depends on the compatibility of its execution target and the Instance Table classifier. The list of compatible Simulation Configurations is displayed in the table toolbar after clicking the **Evaluate** button. When you select the Simulation Configuration you want to run, its Execution Target is temporarily replaced with the Instance Specifications of the Instance Table. Other settings of the Simulation Configuration, e.g., clock, charts, or UI, stay the same.

To run an Instance Table using a Simulation Configuration

- In the toolbar, click the drop-down arrow next to the Evaluate button and select the Simulation Configuration you want to use. [ATTACHMENT filename='running_instance_table_with_simconfig.png']

To run the selected Instance Specifications of an Instance Table using a Simulation Configuration

1. In an Instance Table, select the rows with the Instance Specifications you want to run.
2. In the table toolbar, click the drop-down arrow next to the Evaluate button and select the Simulation Configuration you want to use. [ATTACHMENT filename='running_instance_specifications.png']

If the Simulation Configuration does not have a specified **resultLocation**, all or selected Instance Specifications of an Instance Table are executed and the results are displayed in the same table as shown below.

[IMAGE alt='' src='']

###### Instance Table simulation results.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:macro-id="4a9a687a-c547-48e6-b75d-474b9811fbd1" ac:name="content-layer" ac:schema-version="1"><ac:parameter ac:name="id">1965719714</ac:parameter><ac:rich-text-body><ac:structured-macro ac:macro-id="d2508a2e-5153-4eb3-84cc-d0e5233fdb73" ac:name="content-column" ac:schema-version="1"><ac:parameter ac:name="id">1965719719</ac:parameter><ac:rich-text-body><ac:structured-macro ac:macro-id="281991a3-7499-487a-b138-e4f00a4b7315" ac:name="content-block" ac:schema-version="1"><ac:parameter ac:name="id">1965719713</ac:parameter><ac:rich-text-body><p><strong>On this page</strong></p><p><ac:structured-macro ac:macro-id="59073de5-ccae-43a5-bb31-e6dffef9590b" ac:name="toc" ac:schema-version="1"><ac:parameter ac:name="maxLevel">3</ac:parameter><ac:parameter ac:name="minLevel">3</ac:parameter></ac:structured-macro></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:macro-id="bfc7cf7e-ac2d-463d-baf5-6e875c8a5408" ac:name="content-block" ac:schema-version="1"><ac:parameter ac:name="id">1965719717</ac:parameter><ac:rich-text-body><p>Magic Model Analyst / Cameo Simulation Toolkit provides the means to simulate a set of elements iteratively using a Generic Table or an Instance Table. Each element in the table will be simulated one-by-one from the first to the last row. </p><p>You can run the table by specifying it as a target of a Simulation Configuration and then run the Simulation Configuration. You can also run an Instance or Generic Table using the toolbar button. The toolbar button is dynamic. If you do not select any rows in the table, the toolbar button is <strong>Evaluate</strong>. However, if you select a row in the table, the toolbar button will change to <strong>Evaluate Selected Rows</strong>. </p><p><br /></p><p><ac:inline-comment-marker ac:ref="d1a88a82-7fa8-484c-8426-6332c4770add">To</ac:inline-comment-marker> run a Generic Table or an Instance Table</p><hr /><ul><li>Open the table you want to run and do one of the following:<ul><li>If you want to run the entire table, click the <strong>Evaluate</strong> button in the table toolbar.</li><li>If you want to run just the selected rows, select the rows you want to run and click the <strong>Evaluate Selected Rows</strong> <ac:inline-comment-marker ac:ref="8f35276e-0bea-4889-b573-cacb1a448a66">button</ac:inline-comment-marker>.</li></ul><p class="auto-cursor-target"><br /><ac:image><ri:attachment ri:filename="running_instance_table.png" /></ac:image></p><ac:structured-macro ac:macro-id="7a639dec-c9c7-42a7-961a-488c112eba6a" ac:name="note" ac:schema-version="1"><ac:parameter ac:name="title">Note</ac:parameter><ac:rich-text-body><p><span>For a model that has Behaviors (Classifier Behavior and/or Part Property with Behaviors),</span> see the <strong>autoStart</strong> tag in <a href="https://docs.nomagic.com/display/MMA/SimulationConfig+stereotype">SimulationConfig</a>.</p></ac:rich-text-body></ac:structured-macro></li></ul><h3><br />Running Instance Tables using Simulation Configurations</h3><p>You can run an entire Instance Table or the selected rows in it by using a compatible Simulation Configuration. The Simulation Configuration compatibility depends on the compatibility of its execution target and the Instance Table classifier. The list of compatible Simulation Configurations is displayed in the table toolbar after clicking the <strong>Evaluate</strong> button. When you select the Simulation Configuration you want to run, its Execution Target is temporarily replaced with the Instance Specifications of the Instance Table. Other settings of the Simulation Configuration, e.g., clock, charts, or UI, stay the same.</p><p><br /></p><p>To run an Instance Table using a Simulation Configuration</p><hr /><ul><li>In the toolbar, click the drop-down arrow next to the <strong>Evaluate</strong> button and select the Simulation Configuration you want to use.<br /><br /><ac:image><ri:attachment ri:filename="running_instance_table_with_simconfig.png" /></ac:image></li></ul><p><br /></p><p>To run the selected Instance Specifications of an Instance Table using a Simulation Configuration</p><hr /><ol><li>In an Instance Table, select the rows with the Instance Specifications you want to run.</li><li>In the table toolbar, click the drop-down arrow next to the <strong>Evaluate</strong> button and select the Simulation Configuration you want to use.<br /><br /><ac:image><ri:attachment ri:filename="running_instance_specifications.png" /></ac:image></li></ol><p><ac:inline-comment-marker ac:ref="0dec7eb3-e6f7-4316-a1fd-a3ba50eb5d71"><br />If the Simulation Configuration does not have a specified <strong>resultLocation</strong>, all or selected Instance Specifications of an Instance Table are executed and the results are displayed in the same table as shown below.</ac:inline-comment-marker></p><p><br /></p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="instance_table_simulation_results.png" /></ac:image></p><h6 style="text-align: center;">Instance Table simulation results.</h6></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=249570588 space=MMA version=2 -->
## PAGE 00741: Test case verdict

- page_id: `249570588`
- space_key: `MMA`
- source_url: https://docs.nomagic.com/spaces/MMA/pages/249570588/Test+case+verdict
- version_number: 2
- version_date: `2025-08-19T14:56:13.929+02:00`
- ancestors: Magic Model Analyst / Cameo Simulation Toolkit Documentation > User Guide > Interaction simulation > Supported elements in interaction simulation
- labels: ['test-case-verdict']

### NORMALIZED CONTENT

382013818

382013821

382013820

A testcase is one kind of Behavior Classifier. It can be a class, Behavior, activity, or operation. Since a test case is a SysML element, you need to load a SysML profile into your model to run it. Magic Model Analyst / Cameo Simulation Toolkit supports testcase verdicts.

A verdict kind is an Enumeration value in SysML. It can be error, inconclusive, pass, or fail. Magic Model Analyst / Cameo Simulation Toolkit automatically assigns either **Pass** or **Fail** as the verdict value to a Testcase. If a constraint in the test case (pre/post conditions, state invariants) is not satisfied in a model execution, Magic Model Analyst / Cameo Simulation Toolkit will automatically generate a fail verdict value for the Behavior return parameter, terminate the Behavior simulation, and return the value.

If the "constraint as a breakpoint" option is used in the simulation, whenever the constraint fails, evaluation will stop and will be highlighted in the model, and you will see the message in red in the **Variables** pane. The requirement will be highlighted as well so that you can see what is wrong and navigate to the requirement.

Magic Model Analyst / Cameo Simulation Toolkit will generate a Pass verdict value after the simulation terminates if there is no constraint fails. If a constraint fails, the simulation will pause, and you will get a Fail verdict value in the **Console** pane, but you can always resume the simulation afterwards.

[IMAGE alt='' src='']

###### Simulation console showing constraints that have been evaluated.

382013817

**Related page**

- [CONFLUENCE_PAGE title='Supported SysML elements' space='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="76f254fe-c03c-4b98-a37a-45748e023cd7"><ac:parameter ac:name="id">382013818</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="70858b37-96e6-49ec-b273-784a1cb7814b"><ac:parameter ac:name="id">382013821</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="7d1075b6-cac6-40fa-bb35-7b1736c0ccef"><ac:parameter ac:name="id">382013820</ac:parameter><ac:rich-text-body><p>A testcase is one kind of Behavior Classifier. It can be a class, Behavior, activity, or operation. Since a test case is a SysML element, you need to load a SysML profile into your model to run it. Magic Model Analyst / Cameo Simulation Toolkit supports testcase verdicts. </p><p>A verdict kind is an Enumeration value in SysML. It can be error, inconclusive, pass, or fail. Magic Model Analyst / Cameo Simulation Toolkit automatically assigns either <strong>Pass</strong> or <strong>Fail</strong> as the verdict value to a Testcase. If a constraint in the test case (pre/post conditions, state invariants) is not satisfied in a model execution, Magic Model Analyst / Cameo Simulation Toolkit will automatically generate a fail verdict value for the Behavior return parameter, terminate the Behavior simulation, and return the value. </p><p>If the &quot;constraint as a breakpoint&quot; option is used in the simulation, whenever the constraint fails, evaluation will stop and will be highlighted in the model, and you will see the message in red in the <strong>Variables</strong> pane. The requirement will be highlighted as well so that you can see what is wrong and navigate to the requirement. </p><p>Magic Model Analyst / Cameo Simulation Toolkit will generate a Pass verdict value after the simulation terminates if there is no constraint fails. If a constraint fails, the simulation will pause, and you will get a Fail verdict value in the <strong>Console</strong> pane, but you can always resume the simulation afterwards.</p><p style="margin-left: 30.0px;"><br class="atl-forced-newline" /> <ac:image ac:align="center" ac:title="Pass and Fail Verdict Values in the Console Pane" ac:alt="Pass and Fail Verdict Values in the Console Pane"><ri:attachment ri:filename="passfail_verdict.png" /></ac:image></p><h6 style="text-align: center;">Simulation console showing constraints that have been evaluated.<br class="atl-forced-newline" /><br class="atl-forced-newline" /></h6></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="372b1973-0833-4fda-8a69-fadc4d60138b"><ac:parameter ac:name="id">382013817</ac:parameter><ac:rich-text-body><p><strong>Related page</strong></p><ul><li><ac:link><ri:page ri:content-title="Supported SysML elements" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=249570233 space=MMA version=2 -->
## PAGE 00742: The Time series chart

- page_id: `249570233`
- space_key: `MMA`
- source_url: https://docs.nomagic.com/spaces/MMA/pages/249570233/The+Time+series+chart
- version_number: 2
- version_date: `2025-08-19T14:56:09.426+02:00`
- ancestors: Magic Model Analyst / Cameo Simulation Toolkit Documentation > User Guide > Simulation debugging > Runtime Value Monitoring
- labels: ['time-series-chart']

### NORMALIZED CONTENT

39142533

39142535

39142534

Magic Model Analyst / Cameo Simulation Toolkit allows you to show the plot between runtime values, which are the numerical value and simulation time. This plot is called Time series chart. To view this chart during a model simulation, right-click the row of a runtime value in the **Variables** pane and select **Show** **in** **time series chart**.

###### [IMAGE alt='' src=''] 
The context menu showing the runtime value in the Time series chart.

The **Time series chart** shows the runtime value with respect to simulation time shown as follows

###### [IMAGE alt='' src=''] 
The Time series chart of runtime value of Property x.

39142532

**Related page**

- [CONFLUENCE_PAGE title='Time Series Chart' space='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="91cb5a0b-b491-4139-a906-c12c595d7da1"><ac:parameter ac:name="id">39142533</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="210648f3-4220-400b-b843-8651e4563fb4"><ac:parameter ac:name="id">39142535</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="dba7dabd-3133-444e-ae1a-4787a3ba8c24"><ac:parameter ac:name="id">39142534</ac:parameter><ac:rich-text-body><p>Magic Model Analyst / Cameo Simulation Toolkit allows you to show the plot between runtime values, which are the numerical value and simulation time. This plot is called Time series chart. To view this chart during a model simulation, right-click the row of a runtime value in the <strong>Variables</strong> pane and select <strong>Show</strong> <strong>in</strong> <strong>time series chart</strong>. <br class="atl-forced-newline" /><br class="atl-forced-newline" /></p><h6 style="text-align: center;"><ac:image ac:align="center" ac:title="The Context Menu Showing the Runtime Value in Time Series Chart" ac:alt="The Context Menu Showing the Runtime Value in Time Series Chart"><ri:attachment ri:filename="ShowInTimeSeriesChartMenu.png" /></ac:image><br />The context menu showing the runtime value in the Time series chart.</h6><p>The <strong>Time series chart</strong> shows the runtime value with respect to simulation time shown as follows <br class="atl-forced-newline" /><br class="atl-forced-newline" /></p><h6 style="text-align: center;"><ac:image ac:align="center" ac:title="The Time Series Chart of Runtime Value of Property x" ac:alt="The Time Series Chart of Runtime Value of Property x"><ri:attachment ri:filename="LoadDataButton (1).png" /></ac:image><br />The Time series chart of runtime value of Property x.</h6><p> </p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="e317b4d3-3bff-41c0-b8dd-96102347a9f4"><ac:parameter ac:name="id">39142532</ac:parameter><ac:rich-text-body><p><strong>Related page</strong></p><ul><li><ac:link><ri:page ri:content-title="Time Series Chart" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=249570579 space=MMA version=3 -->
## PAGE 00743: Time constraint

- page_id: `249570579`
- space_key: `MMA`
- source_url: https://docs.nomagic.com/spaces/MMA/pages/249570579/Time+constraint
- version_number: 3
- version_date: `2025-09-12T15:08:39.898+02:00`
- ancestors: Magic Model Analyst / Cameo Simulation Toolkit Documentation > User Guide > Interaction simulation > Supported elements in interaction simulation
- labels: ['time-constraint']

### NORMALIZED CONTENT

381279036

381279038

381279037

You can specify a time constraint in Messages in the Sequence diagram. During simulating an interaction, Simulation Toolkit checks if the active State contains the required State ([**State Invariant**](https://docs.nomagic.com/display/MMA/State+invariant)), and the time is exactly as specified (**Time constraint**). However, the time constraint is not used as the delay time.

381279035

**Related pages**

- [CONFLUENCE_PAGE title='Duration constraint' space='']
- [CONFLUENCE_PAGE title='Sequence diagram' space='MT']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="c01a04e5-2af1-4963-b372-e38d0a8ca546"><ac:parameter ac:name="id">381279036</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="dc9fb3ae-98be-4ddc-a583-bf7b39cd5e60"><ac:parameter ac:name="id">381279038</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="6e646e3b-30b5-4ff0-8447-20d76bdbc24f"><ac:parameter ac:name="id">381279037</ac:parameter><ac:rich-text-body><p><span style="color: rgb(62,63,64);">You can specify a time constraint in Messages in the Sequence diagram. During simulating an interaction, Simulation Toolkit checks if the active State contains the required State (<a href="https://docs.nomagic.com/display/MMA/State+invariant"><strong>State Invariant</strong></a>), and the time is exactly as specified (<strong>Time constraint</strong>). However, the time constraint is not used as the delay time.<br /></span></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="34ea5485-e2ab-4a39-be4f-5ada6655e745"><ac:parameter ac:name="id">381279035</ac:parameter><ac:rich-text-body><p><strong>Related pages</strong></p><ul><li><ac:link><ri:page ri:content-title="Duration constraint" /></ac:link></li><li><ac:link><ri:page ri:space-key="MT" ri:content-title="Sequence diagram" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=249569732 space=MMA version=8 -->
## PAGE 00744: Time Series Chart

- page_id: `249569732`
- space_key: `MMA`
- source_url: https://docs.nomagic.com/spaces/MMA/pages/249569732/Time+Series+Chart
- version_number: 8
- version_date: `2026-02-26T07:52:33.388+01:00`
- ancestors: Magic Model Analyst / Cameo Simulation Toolkit Documentation > User Guide > Simulation Configuration and UI modeling
- labels: ['time-series-chart', 'showing-requirements', 'showing-constraint-violations', 'constraint-violations']

### NORMALIZED CONTENT

**On this page**

**4**

In Magic Model Analyst, a Time series chart displays plots of runtime values with respect to simulation time. You can show a Time series chart of any runtime values during model simulation. The Time series chart measures time on the X-axis (horizontal axis) and runtime values on the Y-axis (vertical axis). The graph of the time series chart simulates the movement of the values or data over time. It allows you to evaluate trend or monitor behavior in the selected values within a specific period of time. You can use a time series chart to display real-time plotting of runtime values on the Y-axis, along with simulation time on the X-axis (as in the simulation time and clock settings). You can also customize most of the chart properties according to your preferences, including title, plot color, min and max value, and external CSV. For further information, see the built-in sample MotionAnalysis.mdzip, used throughout this page to demonstrate how to use the Time series chart in your model.

##### Properties of Time Series Charts

The Specification window of a Time series chart contains the properties you can select or modify to change the display of the Time series chart. The following figure shows the Specification dialog of the Time series chart:

[IMAGE alt='' src='']

###### The properties of Time series chart in its Specification window.

The following table describes the function of each property of the Specification dialog of Time series chart:

| Property | Function |
| --- | --- |
| Annotate Failures | To annotate a Requirement and constraint failures as the chart plot area in red (true by default). |
| Load CSV File | A load CSV file is a file that the Time Series chart will load as a curved line graph. You can import multiple CSV files into the Time series chart and load them as curved line graphs. They will be represented with different colors and legend names (same as the filename extension) so you can compare the differences between the actual results and the desired line graphs. |
| Record Plot Data As | To specify the selected format of the file to be saved if Result File is specified. |
| Result File | To specify the file name to be saved from the results in the selected file format specified in the Record Plot Data As property. Otherwise, the results will be saved into model elements. |
| Fixed Time Length | To specify a fixed range of the time axis in a Time series chart. If you specify a value, the time axis range will be fixed to that particular value. If you do not specify the value of Fixed Time Location, the plot(s) will move to the left if the time range is greater than the maximum value of the time axis. A fixed time length unit is specified by a time unit tag definition of the simulation config. If you do not specify the time unit, Magic Model Analyst will use milliseconds as the default unit. |
| Fixed Time Location | To specify the start time of the time axis in a Time Series chart. If you specify a value for the Fixed Time Length but leave the Fixed Time Location value empty, the Time Series chart will work like an oscilloscope, and the plot(s) will move to the left. If the Fixed Time Location value is not specified, the chart uses the Start Time defined in the Simulation Configuration Timing properties (if set). Negative time values are supported. A fixed time location unit is specified by a time unit tag definition of the Simulation Configuration. If you do not specify the time unit, Magic Model Analyst will use milliseconds as the default unit. |
| Y Label | To specify the label of the y-axis of the Time series chart. |
| Title | To specify the title of a Time series chart. |
| Fixed Range | To specify whether a Time series chart will automatically adjust the range on the Y-axis. If the value is true, the range of the Y-axis will be fixed; otherwise, the range will automatically change. |
| Grid X | To show or hide a vertical grid line |
| Grid Y | To show or hide a horizontal grid line. |
| Keep Open After Termination | To keep the Time series chart open after the termination of the simulation. |
| Max Value | To specify an upper bound value of the Y-axis. |
| Min Value | To specify a lower bound value of the Y-axis. |
| Plot Color | To specify a plot color. |
| Refresh Rate | To specify the time intervals at which the Time Series Chart should be refreshed. The unit of the refresh rate is the same as the Time Unit property value of the Simulation Configuration. If the time unit is not specified, the refresh rate is measured in milliseconds. If the refresh rate is not specified, the value of 1000 is used. Specify 0 to refresh the chart every time the value is changed. |
| Linear Interpolation | If true, a curvilinear graph will be displayed. If false, a linear graph will be displayed. |

The following figure shows the configuration settings of both Time series chart and Simulation Config of the MotionAnalysis.mdzip sample project. The Time series chart has been set as the "Represents" field to the Motion Analysis block together with the "Values" field to the required properties (x, v, and a), along with other properties as needed. Also, the Simulation Config "UI" field has been set to the Time Series Chart (x-v-a plot).

###### [IMAGE alt='' src=''] 
The configuration settings of both Time series chart and Simulation Config of the MotionAnalysis.mdzip sample project.

Once the simulation begins, the Time series chart displays real-time plotting of the x, v, and a properties with time(s), as shown in the MotionAnalysis.mdzip sample.

###### [IMAGE alt='' src=''] 
Real-time plotting of the x, v, and a property with time(s) in the MotionAnalysis.mdzip sample.

##### Using Time Series Charts

To display a Time series chart

1. Open the context menu of the Variables pane.
2. Right-click the row of a runtime value, which must be shown on the Time series chart. Select Show in time series chart (see [CONFLUENCE_PAGE title='The Time series chart' space=''] for more information).

The Magic Model Analyst Time series chart can also serve as a predefined subtype of UI config. You can use it as a UI mockup of the SimulationConfig element, just like an ImageSwitcher.

To use a Time series chart

1. Create a TimeSeriesChart element to represent a Classifier.
2. In the Specification window, specify the **value** tag definition and properties whose values will be monitored in the Time series chart. These properties must be members of the Classifier represented by the Time series chart element. [ATTACHMENT filename='Time Series Chart Property Dialog.png']

##### Reordering Time Series Chart Values

You can reorder the values monitored on a Time Series Chart as described below.

To reorder Time Series Chart values

1. Open the Specification window of a Time Series Chart.
2. Click the property specification cell of the Value property and click [ATTACHMENT filename='order_button.png'] . [ATTACHMENT filename='reordering_time_series_values.png']
3. In the Order Value dialog, select the value whose position you want to change.
4. Click the Up button to move the value up or the Down button - to move the value down.
5. When you are done, click OK and close the Specification window.

##### Showing Requirements or constraint violations

When the Magic Model Analyst annotates a failure property in red (as the selected property to be represented in the chart) on the **Variables** pane, the chart plot area during that period of failure will also be rendered in red. There will be a tooltip shown in the red area with the full information, exactly the same as other tooltips, e.g., in the Instance table and **Variables** pane, when failure is shown in red.

Labels will be printed in red above the chart and at the center. The label format of a failed constraint is shown as *“<Name of the constraint property typed by the constraint Block>* fails”, and the label format of a failed Requirement is shown as “req <ID> fails”. However, if the name of the constraint property is blank, the label will not be printed. You can also manually disable this option via the **Annotate Failures** property in the Time series chart Specification window for some reasons, e.g., too many failures with overlapped labels in the chart.

[IMAGE alt='' src='']

###### Time series chart shows constraint violations with multiple labels.

You can zoom in the chart to see start time and end time points marked with big dots. You can also display the time unit of each point by hovering the mouse over it as shown in the figure below. Labels of failed validation will be included in the exported image (by setting **Record Plot Data As** PNG and specifying **Result File**in the Time series chart Specification window). This feature also applies to [Representing Time series charts in a Timeline chart](https://docs.nomagic.com/display/MMA/Timeline+chart#Timelinechart-RepresentingTimeserieschartsinaTimelinechart).

[IMAGE alt='' src='']

###### Tooltip of the Time series chart shows the full information of failure, start time, and end time points.

##### Glossary

- CSV A CSV is a comma-separated values file that stores tabular data (text and number) in plain text. Each line in the file is a record; each record consists of one or more fields, separated by commas.

- Runtime value A runtime value refers to the value of the structural features contained in the created object during model simulation.

- Time series chart A Time series chart is a graph that can simulate runtime values over a specific period of time.

##### Sample projects

To find the *Motion Analysis* sample project used in this chapter, go to *<modeling_tool_install_dir>/samples/simulation/Parametrics/MotionAnalysis.mdzip.*

##### Related pages

- [CONFLUENCE_PAGE title="Specifying time axis' range in a Time series chart" space='']
- [CONFLUENCE_PAGE title='Exporting plots data' space='']
- [CONFLUENCE_PAGE title='Representing data from a CSV file in a line chart' space='']
- [CONFLUENCE_PAGE title='The Time series chart' space='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p><strong>On this page</strong></p><p><strong><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="9603c432-2df4-44ab-8f1e-8bb87cf37929"><ac:parameter ac:name="maxLevel">4</ac:parameter></ac:structured-macro></strong></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><span style="color:var(--ds-text,#333333);">In Magic Model Analyst, a Time series chart displays plots of runtime values with respect to simulation time. You can show a Time series chart of any runtime values during model simulation. The Time series chart measures time on the X-axis (horizontal axis) and runtime values on the Y-axis (vertical axis). The graph of the time series chart simulates the movement of the values or data over time. It allows you to evaluate trend or monitor behavior in the selected values within a specific period of time. You can use a time series chart to display real-time plotting of runtime values on the Y-axis, along with simulation time on the X-axis (as in the simulation time and clock settings). You can also customize most of the chart properties according to your preferences, including title, plot color, min and max value, and external CSV. For further information, see the built-in sample MotionAnalysis.mdzip, used throughout this page to demonstrate how to use the Time series chart in your model.</span></p><h3><br />Properties of Time Series Charts</h3><p>The Specification window of a Time series chart contains the properties you can select or modify to change the display of the Time series chart. The following figure shows the Specification dialog of the Time series chart:</p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="First Time Series Chart Property Dialog.png" /></ac:image></p><h6 style="text-align: center;">The properties of Time series chart in its Specification window.</h6><p>The following table describes the function of each property of the Specification dialog of Time series chart:</p><table class="relative-table wrapped" style="width: 99.9436%;"><colgroup class=""><col class="" style="width: 20.5351%;" /><col class="" style="width: 79.4563%;" /></colgroup><tbody class=""><tr class=""><th>Property</th><th colspan="1">Function</th></tr><tr class=""><td colspan="1"><strong>Annotate Failures</strong></td><td colspan="1">To annotate a Requirement and constraint failures as the chart plot area in red (true by default).</td></tr><tr class=""><td colspan="1"><strong>Load CSV File</strong></td><td colspan="1"><strong><span>A load CSV</span></strong><span> file is a file that the Time Series chart will load as a curved line graph. You can import multiple CSV files into the Time series chart and load them as curved line graphs. They will be represented with different colors and legend names (same as the filename extension) so you can compare the differences between the actual results and the desired line graphs.</span></td></tr><tr class=""><td colspan="1"><strong>Record Plot Data As</strong></td><td colspan="1"><span>To specify the selected format of the file to be saved if <strong>Result File</strong> is specified.</span></td></tr><tr class=""><td colspan="1"><strong>Result File</strong></td><td colspan="1"><span>To specify the file name to be saved from the results in the selected file format specified in the <strong>Record Plot Data As</strong> property. Otherwise, the results will be saved into model elements.</span></td></tr><tr class=""><td><strong>Fixed Time Length</strong></td><td colspan="1">To specify a fixed range of the time axis in a Time series chart. If you specify a value, the time axis range will be fixed to that particular value. If you do not specify the value of Fixed Time Location, the plot(s) will move to the left if the time range is greater than the maximum value of the time axis. A fixed time length unit is specified by a time unit tag definition of the simulation config. If you do not specify the time unit, Magic Model Analyst will use milliseconds as the default unit. </td></tr><tr class=""><td><strong>Fixed Time Location</strong></td><td colspan="1">To specify the start time of the time axis in a Time Series chart. If you specify a value for the Fixed Time Length but leave the Fixed Time Location value empty, the Time Series chart will work like an oscilloscope, and the plot(s) will move to the left. If the Fixed Time Location value is not specified, the chart uses the <strong>Start Time </strong>defined in the Simulation Configuration Timing properties (if set). Negative time values are supported. A fixed time location unit is specified by a time unit tag definition of the Simulation Configuration. If you do not specify the time unit, Magic Model Analyst will use milliseconds as the default unit.</td></tr><tr class=""><td colspan="1"><strong>Y Label</strong></td><td colspan="1"><span>To specify the label of the y-axis of the Time series chart.</span></td></tr><tr class=""><td colspan="1"><strong>Title</strong></td><td colspan="1"><span>To specify the title of a Time series chart.</span></td></tr><tr class=""><td><strong>Fixed Range</strong></td><td colspan="1">To specify whether a Time series chart will automatically adjust the range on the Y-axis. If the value is true, the range of the Y-axis will be fixed; otherwise, the range will automatically change. </td></tr><tr class=""><td><strong>Grid X</strong></td><td colspan="1">To show or hide a vertical grid line</td></tr><tr class=""><td><strong>Grid Y</strong></td><td colspan="1">To show or hide a horizontal grid line.</td></tr><tr class=""><td colspan="1"><div class="content-wrapper"><p><strong>Keep Open After Termination</strong></p></div></td><td colspan="1">To keep the Time series chart open after the termination of the simulation.</td></tr><tr class=""><td><strong>Max Value</strong></td><td colspan="1">To specify an upper bound value of the Y-axis.</td></tr><tr class=""><td><strong>Min Value</strong> </td><td colspan="1">To specify a lower bound value of the Y-axis.</td></tr><tr class=""><td><strong>Plot Color</strong></td><td colspan="1">To specify a plot color.</td></tr><tr class=""><td><strong>Refresh Rate</strong></td><td colspan="1">To specify the <span style="color:var(--ds-text,#333333);">time intervals at which the Time Series Chart should be refreshed. </span>The unit of the refresh rate is the same as the Time Unit property value of the Simulation Configuration. If the time unit is not specified, the refresh rate is measured in milliseconds. If the refresh rate is not specified, the value of 1000 is used. Specify 0 to refresh the chart every time the value is changed.</td></tr><tr class=""><td colspan="1"><strong>Linear Interpolation</strong></td><td colspan="1"><span style="color:var(--ds-text,#172b4d);">If true, a curvilinear graph will be displayed. If false, a linear graph will be displayed.</span></td></tr></tbody></table><p>The following figure shows the configuration settings of both Time series chart and Simulation Config of the MotionAnalysis.mdzip sample project. The Time series chart has been set as the &quot;Represents&quot; field to the Motion Analysis block together with the &quot;Values&quot; field to the required properties (x, v, and a), along with other properties as needed. Also, the Simulation Config &quot;UI&quot; field has been set to the Time Series Chart (x-v-a plot).</p><h6 style="text-align: center;"><ac:image ac:align="center" ac:title="TimeSeriesChart in the MotionAnalysis.mdzip Sample Project" ac:alt="TimeSeriesChart in the MotionAnalysis.mdzip Sample Project"><ri:attachment ri:filename="TimeSeriesChart_2.png" /></ac:image><br />The configuration settings of both Time series chart and Simulation Config of the MotionAnalysis.mdzip sample project.</h6><p>Once the simulation begins, the Time series chart displays real-time plotting of the x, v, and a properties with time(s), as shown in the MotionAnalysis.mdzip sample.</p><h6 style="text-align: center;"><ac:image ac:align="center" ac:title="Time Series Chart during the Simulation of Run Analysis x-v-a Simulation Configuration in the MotionAnalysis Sample" ac:alt="Time Series Chart during the Simulation of Run Analysis x-v-a Simulation Configuration in the MotionAnalysis Sample"><ri:attachment ri:filename="TimeSeriesChart_3.png" /></ac:image><br />Real-time plotting of the x, v, and a property with time(s) in the MotionAnalysis.mdzip sample.</h6><h3>Using  Time Series Charts</h3><p>To display a Time series chart</p><hr /><ol><li data-uuid="7a5047e7-8534-4f14-8f72-55ba66256904">Open the context menu of the <strong>Variables</strong> pane.</li><li data-uuid="1a6a2c79-ed43-43ca-b681-b5669154cffd">Right-click the row of a runtime value, which must be shown on the Time series chart. Select <strong>Show</strong> <strong>in</strong> <strong>time series chart</strong> (see <ac:link><ri:page ri:content-title="The Time series chart" /><ac:plain-text-link-body><![CDATA[the Time series chart]]></ac:plain-text-link-body></ac:link> for more information). </li></ol><p>The Magic Model Analyst Time series chart can also serve as a predefined subtype of UI config. You can use it as a UI mockup of the SimulationConfig element, just like an ImageSwitcher. </p><p><br /></p><p class="auto-cursor-target">To use a Time series chart</p><hr /><ol><li data-uuid="1968cb90-a992-4ee5-b177-c7120601a4cb">Create a TimeSeriesChart element to represent a Classifier.</li><li data-uuid="642a250a-d810-48e2-abcc-6e779d032203"><p style="text-align: left;">In the Specification window, specify the <strong>value</strong> tag definition and properties whose values will be monitored in the Time series chart. These properties must be members of the Classifier represented by the Time series chart element.<br /><br /></p><ac:image><ri:attachment ri:filename="Time Series Chart Property Dialog.png" /></ac:image></li></ol><h3><br />Reordering Time Series Chart Values</h3><p>You can reorder the values monitored on a Time Series Chart as described below.</p><p><br /></p><p>To reorder Time Series Chart values</p><hr /><ol><li data-uuid="7a25d339-a1ea-44fd-b14b-aa6c894b7a2d">Open the Specification window of a Time Series Chart.</li><li data-uuid="d59c1bec-bcc3-434b-8c32-231cd704cb30">Click the property specification cell of the <strong>Value</strong> property and click <ac:image ac:thumbnail="true" ac:height="17"><ri:attachment ri:filename="order_button.png" /></ac:image>.<br /><br /><ac:image><ri:attachment ri:filename="reordering_time_series_values.png" /></ac:image><br /><br /></li><li data-uuid="dab3bb04-d642-4e3d-b639-7e83115667b3">In the <strong>Order Value</strong> dialog, select the value whose position you want to change.</li><li data-uuid="47d06426-668d-4d94-a3ce-f5c176dcdeaa">Click the <strong>Up</strong> button to move the value up or the <strong>Down</strong> button - to move the value down.</li><li data-uuid="d4ef4a34-e076-42bb-a573-616318347bd7">When you are done, click <strong>OK</strong> and close the Specification window.</li></ol><h3><br />Showing Requirements or constraint violations</h3><p>When the Magic Model Analyst annotates a failure property in red (as the selected property to be represented in the chart) on the <strong>Variables</strong> pane, the chart plot area during that period of failure will also be rendered in red. There will be a tooltip shown in the red area with the full information, exactly the same as other tooltips, e.g., in the Instance table and <strong>Variables</strong> pane, when failure is shown in red.</p><p>Labels will be printed in red above the chart and at the center. The label format of a failed constraint is shown as <em>“&lt;Name of the constraint property typed by the constraint Block&gt;</em> fails”, and the label format of a failed Requirement is shown as “req &lt;ID&gt; fails”. However, if the name of the constraint property is blank, the label will not be printed. You can also manually disable this option via the <strong>Annotate Failures</strong> property in the Time series chart Specification window for some reasons, e.g., too many failures with overlapped labels in the chart.</p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="Time Series Chart with Constraint Violations and Multiple Labels.png" /></ac:image></p><h6 style="text-align: center;">Time series chart shows constraint violations with multiple labels.</h6><p>You can zoom in the chart to see start time and end time points marked with big dots. You can also display the time unit of each point by hovering the mouse over it as shown in the figure below. Labels of failed validation will be included in the exported image (by setting <strong>Record Plot Data As</strong> PNG and specifying <strong>Result File </strong>in the Time series chart Specification window). This feature also applies to <a href="https://docs.nomagic.com/display/MMA/Timeline+chart#Timelinechart-RepresentingTimeserieschartsinaTimelinechart">Representing Time series charts in a Timeline chart</a>.</p><p><ac:image ac:align="center"><ri:attachment ri:filename="Tooltip of Time Series Chart.png" /></ac:image></p><h6 style="text-align: center;">Tooltip of the Time series chart shows the full information of failure, start time, and end time points.</h6><h3>Glossary</h3><ul><li data-uuid="d45c7656-058d-4449-8c80-12d878a046db"><strong>CSV</strong><br />A CSV is a comma-separated values file that stores tabular data (text and number) in plain text. Each line in the file is a record; each record consists of one or more fields, separated by commas.</li></ul><ul><li class="auto-cursor-target" data-uuid="62e0193d-75d5-473b-82fe-45c213145f5b"><strong>Runtime value</strong><br />A runtime value refers to the value of the structural features contained in the created object during model simulation.</li></ul><ul><li class="auto-cursor-target" data-uuid="fde2c12a-ea6b-43c8-b41c-013b2d2b9d1e"><strong>Time series chart</strong><br />A Time series chart is a graph that can simulate runtime values over a specific period of time.</li></ul><h3>Sample projects</h3><p>To find the <em>Motion Analysis</em> sample project used in this chapter, go to <em>&lt;modeling_tool_install_dir&gt;<span style="color:var(--ds-text,#172b4d);">/samples/simulation/Parametrics/MotionAnalysis.mdzip.<br /></span></em></p><h3>Related pages</h3><ul><li data-uuid="eb1e61d9-9627-4562-a4af-5c136d42015f"><ac:link><ri:page ri:content-title="Specifying time axis' range in a Time series chart" /></ac:link></li><li data-uuid="7606a880-d55a-4f31-be93-d9321057c0f1"><ac:link><ri:page ri:content-title="Exporting plots data" /></ac:link></li><li data-uuid="9c1c1f27-205b-449c-a8a7-81fde1133ab0"><ac:link><ri:page ri:content-title="Representing data from a CSV file in a line chart" /></ac:link></li><li data-uuid="2135f44f-83f4-48ea-aee6-9c51b35f0ec8"><ac:link><ri:page ri:content-title="The Time series chart" /></ac:link></li></ul></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=249569785 space=MMA version=7 -->
## PAGE 00745: Timeline chart

- page_id: `249569785`
- space_key: `MMA`
- source_url: https://docs.nomagic.com/spaces/MMA/pages/249569785/Timeline+chart
- version_number: 7
- version_date: `2026-02-26T09:59:07.724+01:00`
- ancestors: Magic Model Analyst / Cameo Simulation Toolkit Documentation > User Guide > Simulation Configuration and UI modeling
- labels: ['timeline-chart', 'exporting-timeline-chart', 'showing-time-series-chart-in-timeline-chart', 'time-series-chart-in-timeline-chart']

### NORMALIZED CONTENT

**On this page**

4

Unlike a [CONFLUENCE_PAGE title='Time Series Chart' space=''], a Timeline chart allows you to see the active States of an object or a property during simulation or the Activities simulated in an object. The Timeline plot allows you to see the animation of all active States while a model simulation is running, as well as which objects are active in each State or when a State starts and ends.

Similar to the Time series chart, the Timeline chart also shows the x-axis and y-axis. If a Timeline chart represents an Activity, the x-axis of the chart shows time, and the y-axis shows Call Behavior Action, Activity, Call Operation Action, and Operation names. If a Timeline chart represents a State, the x-axis of the chart shows time, and the y-axis shows object State names in different values.Timeline charts identify the changes in object States or executed Activities and plot them along a timeline. The States are grouped by region. Magic Model Analyst / Cameo Simulation Toolkit records changes in the active States or Activities and allows you to export them to a CSV or TSV file. You can then import the CSV file into an Excel file and analyze the exported Timeline chart, e.g., calculate the simulation duration, see what object is in a particular State, and how long it is busy or idle.

We use the sample project *[ATTACHMENT filename='FlashingLight.mdzip']* throughout this section to demonstrate how to use a Timeline chart in your model.

##### Properties of the Timeline Chart

The Magic Model Analyst / Cameo Simulation Toolkit's Timeline chart can also serve as a predefined subtype of a [CONFLUENCE_PAGE title='Simulation Configuration and UI modeling' space='']. You can use it as a UI mockup of the SimulationConfig element just like an ImageSwitcher. The Specification window of the Timeline chart is shown below:

[IMAGE alt='' src='']

###### The properties of Timeline chart in the Specification window.

You can change the Timeline chart's display by modifying its properties, as shown in the following table.

| Property | Function |
| --- | --- |
| Annotate Failures | To annotate a Requirement and constraint failures as the chart plot area in red (true by default). |
| Context Plot | To show or hide a context plot. |
| Dynamic | If true, the chart shows only States or Actions actually used and sorted by occurrence. Otherwise, the list of static Behaviors is shown, and the chart contains information when open. |
| Fixed Time Length | To specify a fixed range of the time axis in a Timeline chart in milliseconds. If you specify a value, the time axis range will be fixed to that particular value. If you do not specify the value of the Fixed Time Location, the plot(s) will move to the left if the time range is greater than the maximum value of the time axis. A fixed time length unit is specified by a time unit tag definition of the Simulation Config. If you do not specify the time unit, Magic Model Analyst / Cameo Simulation Toolkit uses 20,000 milliseconds as the default unit. |
| Fixed Time Location | To specify the start time of the time axis in a Timeline chart. If you specify a value for the Fixed Time Length but leave the Fixed Time Location value empty, the Timeline chart will work like an oscilloscope, and the plot(s) will move to the left. If the Fixed Time Location value is not specified, the chart uses the Start Time defined in the Simulation Configuration Timing properties (if set). Negative time values are supported. A fixed time location unit is specified by a time unit tag definition of the Simulation Configuration. If you do not specify the time unit, Magic Model Analyst uses milliseconds as the default unit. |
| Ignored Elements | A list of elements (States, Actions, and Activities) that will be ignored and not displayed in the Timeline chart. This list takes priority over the Value list. |
| Keep Open After Termination | To keep the Timeline chart open after the termination of the simulation. |
| Linear Interpolation | If true, the plot will connect 2 dots in a non-rectangular line at a time.e |
| Plot Color | To specify a plot color. |
| Record Plot Data As | To specify the selected format of the file to be saved if Result File is specified. |
| Result File | To specify the file name to be saved from the results in the selected file format specified in the Record Plot Data As property. Otherwise, the results will be saved into model elements. |
| Timeline Mode | To select whether to show the Timeline of a State or an Activity. |
| Title | To specify the title of a Timeline Chart. |

##### Using a Timeline Chart

To display a Timeline chart

1. Open the shortcut menu of the Variables pane in the Simulation window.
2. Right-click the row of a runtime value you want to show on the Timeline chart and select Show in Timeline Chart > State or Activity . This example uses State .

[IMAGE alt='' src='']

To use a Timeline chart

1. Create a Timeline chart element to represent a Classifier.
2. Open its Specification window and click [ATTACHMENT filename='browse_button.png'] next to the Value property to select the elements/values to be monitored in the Timeline Chart. The Select Nested Properties dialog opens. [IMAGE alt='' src='']
3. Select the values and click [IMAGE alt='' src='']. The selected values of the Timeline chartappear in the **Value** tag property of the Specification window. 
 
[IMAGE alt='' src='']
4. Double-click Simulation Config Flashlight on the diagram pane to open its Specification window.
5. Click [IMAGE alt='' src=''] next to the UI property field. The**Select UI** dialog opens.
6. Select the **Timeline** component and click [IMAGE alt='' src=''] to add it to the UI of the Simulation Config. [IMAGE alt='' src='']
7. Click [IMAGE alt='' src='']. The added Timeline component appears as one of the Simulation Config UI properties in the Specification window. [IMAGE alt='' src='']
8. Once you specify all of the values, t he Simulation Config in the diagram pane shows the Timeline chart, along with the values that represent systems . [ATTACHMENT filename='ConfigTimelineSystem.png']
9. Run the Timeline Chart. You can see the animation of the active States in the Timeline Chart when the Context Plot option is set to False and True . The following figure shows the Timeline chart output when the **Context Plot** option in the Specification window is set to **False.**

[IMAGE alt='' src='']

The following figure shows the Timeline chart output when the **Context Plot** option in the Specification window is set to **True**.

[IMAGE alt='' src='']

10. Optionally, you can specify in the **Ignored Elements** property what State will be ignored and not be recorded in the Timeline chart if the user does not want to see them. The following figure shows the Timeline chart output when the Ignored Elements property is set to ignore the ticking State and the off State of the timer, and the on State of the system.

###### [IMAGE alt='' src='']

###### The Ignored Elements property set to ignore the ticking State and the off State of timer, and the on State of system.

#### WARNING: Important

Important

A Timeline chart shows only States and Actions that are actually used, e.g., Actions with duration constraints and signaled States. The used elements will be displayed in the chart and sorted in time order.

##### Reordering Timeline Chart values

You can reorder the values monitored on a Timeline Chart as described below.

To reorder Timeline Chart values

1. Open the Specification window of a Timeline Chart.
2. Click the property specification cell of the Value property and click [ATTACHMENT filename='order_button.png'] . [ATTACHMENT filename='reordering_timeline_values.png']
3. In the Order Value dialog, select the value whose position you want to change.
4. Click the Up button to move the value up or the Down button to move the value down.
5. When you are done, click OK and close the Specification window.

##### Showing the duration of empty/dummy Actions as duration constraints

To show the duration of empty/dummy Actions as duration constraints

- The Timeline Chart can show empty or dummy actions with duration constraints. The dummy action can be either an empty call Behavior Action with no behavior assigned or an Opaque Action with duration constraints, as shown in the following example.

[IMAGE alt='' src='']

The Timeline Chart shows the Action names on the left-hand side and the duration simulation performed on the Actions (not the Activities) on the right-hand side. The same thing applies to an Action that has Behaviors assigned, but it is empty and has no diagram. The following figure shows the Timeline chart of the empty/dummy actions from the above example.

[IMAGE alt='' src='']

###### The Timeline chart of the empty/dummy actions.

##### Exporting a Timeline Chart

To export a Timeline chart

1. On the Timeline chart pane (e.g., System), click the **Export** **Data** button on the **Timeline Chart** dialog. [IMAGE alt='' src='']
2. The Timeline chart will be exported as a CSV format file. The exported Timeline chart in an Excel file is shown in the figure below.

[IMAGE alt='' src='']

##### Representing Time Series Charts in a Timeline Chart

To represent value properties as separated Time series charts in a Timeline chart

1. Open the Specification window of a Timeline chart and click the **Value** tag. Boolean, Enumeration, and Numeric primitive value types (e.g., Number, Real, or Integer), are supported as shown in the following figure. [IMAGE alt='' src=''] Selecting numeric primitive value types in Value of a Timeline chart.
2. Run the simulation with the Timeline chart. The selected value properties will be included in the Timeline chart and represented as the Time series chart with fixed height, as separate bars for individual properties (shown in the figure below). [IMAGE alt='' src=''] The selected jobsDoneIn value property is represented as the Time series chart in form of separated bars in the Timeline chart.

##### Glossary

- Context plot A Context plot is a Timeline chart property that enables the plot of the context. It appears on top of the chart as a horizontal line.

- CSV A CSV is a comma-separated values file that stores tabular data (text and number) in plain text. Each line in the file is a record and each record consists of one or more fields, separated by commas.

- Oscilloscope A piece of equipment showing oscillations in an electric current as waves on the screen.

- Timeline chart A Timeline chart is used to describe the Behaviors of both individual Classifiers and Interactions of the Classifiers, focusing attention on the time of events triggering a State change.

- TSV A TSV is a tab-separated values file that stores data in a tabular structure (e.g., database or spreadsheet data). Each line in the file is a record and each record consists of one or more fields, separated by tabs.

##### Sample model

The models used in the figures on this page are the **FlashingLight** and **OntologicalBehaviorModeling**sample models that come with your modeling tool.

To open the sample, do either of the following

- Download [ATTACHMENT filename='FlashingLight.mdzip'] or *[ATTACHMENT filename='OntologicalBehaviorModeling.mdzip']* .
- Find it in the modeling tool <*install_root*>\samples\simulation\.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p><strong>On this page</strong></p><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="6da069c5-5af8-4e76-be6f-f483ad3b4715"><ac:parameter ac:name="maxLevel">4</ac:parameter></ac:structured-macro></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p>Unlike a <ac:link><ri:page ri:content-title="Time Series Chart" /><ac:plain-text-link-body><![CDATA[Time Series chart]]></ac:plain-text-link-body></ac:link>, a Timeline chart allows you to see the active States of an object or a property during simulation or the Activities simulated in an object. The Timeline plot allows you to see the animation of all active States while a model simulation is running, as well as which objects are active in each State or when a State starts and ends. </p><p>Similar to the Time series chart, the Timeline chart also shows the x-axis and y-axis. <span style="color:var(--ds-text,#333333);">If a Timeline chart represents an Activity, the x-axis of the chart shows time, and the y-axis shows Call Behavior Action, Activity, Call Operation Action, and Operation names. If a Timeline chart represents a State, the x-axis of the chart shows time, and the y-axis shows object State names in different values. </span><span style="color:var(--ds-text,#333333);">Timeline charts identify the changes in object States or executed Activities and plot them along a timeline. The States are grouped by region. Magic Model Analyst / Cameo Simulation Toolkit records changes in the active States or Activities and allows you to export them to a CSV or TSV file. You can then import the CSV file into an Excel file and analyze the exported Timeline chart, e.g., calculate the simulation duration, see what object is in a particular State, and how long it is busy or idle.</span></p><p>We use the sample project <em><ac:link><ri:attachment ri:filename="FlashingLight.mdzip" /></ac:link></em> throughout this section to demonstrate how to use a Timeline chart in your model.</p><h3><br />Properties of the Timeline Chart</h3><p>The Magic Model Analyst / Cameo Simulation Toolkit's Timeline chart can also serve as a predefined subtype of a <ac:link><ri:page ri:content-title="Simulation Configuration and UI modeling" /><ac:plain-text-link-body><![CDATA[UI Config]]></ac:plain-text-link-body></ac:link>. You can use it as a UI mockup of the SimulationConfig element just like an ImageSwitcher. The Specification window of the Timeline chart is shown below:</p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="Timeline Specification - All.png" /></ac:image></p><h6 style="text-align: center;">The properties of Timeline chart in the Specification window.</h6><p>You can change the Timeline chart's display by modifying its properties, as shown in the following table.</p><table class="relative-table wrapped" style="width: 99.9436%;"><colgroup class=""><col class="" style="width: 19.4318%;" /><col class="" style="width: 80.5597%;" /></colgroup><tbody class=""><tr class=""><th>Property</th><th>Function</th></tr><tr class=""><td colspan="1"><strong>Annotate Failures</strong></td><td colspan="1">To annotate a Requirement and constraint failures as the chart plot area in red (true by default).</td></tr><tr class=""><td><strong>Context Plot</strong></td><td><p>To show or hide a context plot.</p></td></tr><tr class=""><td colspan="1"><div class="content-wrapper"><p><strong>Dynamic</strong></p></div></td><td colspan="1">If true, the chart shows only States or Actions actually used and sorted by occurrence. Otherwise, the list of static Behaviors is shown, and the chart contains information when open.</td></tr><tr class=""><td><strong>Fixed</strong><strong> Time </strong><strong>Length</strong></td><td>To specify a fixed range of the time axis in a Timeline chart in milliseconds. If you specify a value, the time axis range will be fixed to that particular value. If you do not specify the value of the Fixed Time Location, the plot(s) will move to the left if the time range is greater than the maximum value of the time axis. A fixed time length unit is specified by a time unit tag definition of the Simulation Config. If you do not specify the time unit, Magic Model Analyst / Cameo Simulation Toolkit uses 20,000 milliseconds as the default unit.</td></tr><tr class=""><td colspan="1"><strong>Fixed</strong> <strong>Time </strong><strong>Location</strong></td><td colspan="1">To specify the start time of the time axis in a Timeline chart. If you specify a value for the Fixed Time Length but leave the Fixed Time Location value empty, the Timeline chart will work like an oscilloscope, and the plot(s) will move to the left. If the Fixed Time Location value is not specified, the chart uses the <strong>Start Time </strong>defined in the Simulation Configuration Timing properties (if set). Negative time values are supported. A fixed time location unit is specified by a time unit tag definition of the Simulation Configuration. If you do not specify the time unit, Magic Model Analyst uses milliseconds as the default unit.</td></tr><tr class=""><td><strong>Ignored Elements</strong></td><td>A list of elements (States, Actions, and Activities) that will be ignored and not displayed in the Timeline chart. This list takes priority over the <strong>Value</strong> list.</td></tr><tr class=""><td colspan="1"><div class="content-wrapper"><p><strong>Keep Open After Termination</strong></p></div></td><td colspan="1">To keep the Timeline chart open after the termination of the simulation.</td></tr><tr class=""><td colspan="1"><strong>Linear Interpolation</strong></td><td colspan="1">If true, the plot will connect 2 dots in a non-rectangular line at a time.e</td></tr><tr class=""><td><strong>Plot Color</strong></td><td>To specify a plot color.</td></tr><tr class=""><td colspan="1"><strong>Record Plot Data As</strong></td><td colspan="1">To specify the selected format of the file to be saved if <strong>Result File</strong> is specified.</td></tr><tr class=""><td colspan="1"><strong>Result File</strong></td><td colspan="1"><div class="content-wrapper"><p>To specify the file name to be saved from the results in the selected file format specified in the <strong>Record Plot Data As</strong> property. Otherwise, the results will be saved into model elements.</p></div></td></tr><tr class=""><td colspan="1"><strong>Timeline Mode</strong></td><td colspan="1"><div class="content-wrapper"><p>To select whether to show the Timeline of a State or an Activity.</p></div></td></tr><tr class=""><td colspan="1"><strong>Title</strong></td><td colspan="1">To specify the title of a Timeline Chart.</td></tr></tbody></table><p><br /></p><h3>Using a Timeline Chart</h3><p>To display a Timeline chart</p><hr /><ol><li>Open the shortcut menu of the <strong>Variables</strong> pane in the Simulation window.</li><li>Right-click the row of a runtime value you want to show on the Timeline chart and select <strong>Show</strong> <strong>in</strong> <strong>Timeline</strong> <strong>Chart</strong> &gt; <strong>State</strong> or <strong>Activity</strong>. This example uses <strong>State</strong>.</li></ol><p style="margin-left: 30.0px;"><br class="atl-forced-newline" /><ac:image><ri:attachment ri:filename="show_in_timelinechart.png" /></ac:image></p><p class="auto-cursor-target"><br /></p><p>To use a Timeline chart</p><hr /><ol><li><p>Create a Timeline chart element to represent a Classifier.</p></li><li>Open its Specification window and click <ac:image><ri:attachment ri:filename="browse_button.png" /></ac:image> next to the <strong>Value</strong> property to select the elements/values to be monitored in the Timeline Chart. The <strong>Select Nested Properties</strong> dialog opens.<br /><br /><p><ac:image><ri:attachment ri:filename="Select Property dialog.png" /></ac:image></p></li><li><p>Select the values and click <ac:image><ri:attachment ri:filename="OK_button.png" /></ac:image>. The selected values <span style="color:var(--ds-text-accent-blue-bolder,#09326c);">of the Timeline chart </span>appear in the <strong>Value</strong> tag property of <span style="color:var(--ds-text-accent-blue-bolder,#09326c);">the Specification window</span>.<br /><br /><ac:image><ri:attachment ri:filename="Timeline chart values.png" /></ac:image></p><p><br /></p></li><li>Double-click <strong>Simulation Config Flashlight</strong> on the diagram pane to open its Specification window.</li><li><p>Click <ac:image><ri:attachment ri:filename="browse_button.png" /></ac:image> next to the UI property field. The<strong> Select UI</strong> dialog opens.<span style="color:var(--ds-text-accent-blue-bolder,#09326c);"><br /></span></p></li><li><p>Select the <strong>Timeline</strong> component and click <ac:image><ri:attachment ri:filename="plus_sign.png" /></ac:image> to add it to the UI of the Simulation Config.</p><p><br /></p><p><ac:image><ri:attachment ri:filename="SelectUI_dialog.png" /></ac:image></p><p><br /></p></li><li><p>Click <ac:image><ri:attachment ri:filename="OK_button.png" /></ac:image>. The added Timeline component appears as one of the Simulation Config UI properties in the Specification window.<br /><br /></p><p><ac:image><ri:attachment ri:filename="Simulation Config  UI Properties - Timeline.png" /></ac:image></p><p><br /></p></li><li>Once you specify all of the values, t<span style="color:var(--ds-text-accent-blue-bolder,#09326c);">he Simulation Config in the diagram pane shows the Timeline chart, along with the values </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">that represent systems</span>.<br /><br /><ac:image><ri:attachment ri:filename="ConfigTimelineSystem.png" /></ac:image><br /><span style="color:var(--ds-text-accent-blue-bolder,#09326c);"> </span><br /><span style="color:var(--ds-text-accent-blue-bolder,#09326c);"><br /></span></li><li>Run the Timeline Chart. You can see the animation of the active States in the Timeline Chart when the <strong>Context Plot</strong> option is set to <strong>False</strong> and <strong>True</strong>. <span style="color:var(--ds-text-accent-blue-bolder,#09326c);">The following figure shows the Timeline chart output when the <strong>Context Plot</strong> option in the Specification window is set to <strong>False.</strong></span></li></ol><p style="margin-left: 30.0px;"><br class="atl-forced-newline" /><span style="color:var(--ds-chart-gray-bold,#8590a2);"> <ac:image><ri:attachment ri:filename="Timeline_contextFalse.png" /></ac:image><br /><br /></span></p><p style="margin-left: 30.0px;"><span style="color:var(--ds-chart-gray-bold,#8590a2);"><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">The following figure shows the Timeline chart output when the <strong>Context Plot</strong> option in the Specification window is set to <strong>True</strong>.</span></span></p><p style="margin-left: 30.0px;"><span style="color:var(--ds-chart-gray-bold,#8590a2);"><ac:image><ri:attachment ri:filename="timeline_contextTrue.png" /></ac:image></span></p><p><br /></p><p style="margin-left: 30.0px;">10. Optionally, you can specify in the <strong>Ignored Elements</strong> property what State will be ignored and not be recorded in the Timeline chart if the user does not want to see them. The following figure shows the Timeline chart output when the Ignored Elements property is set to ignore the ticking State and the off State of the timer, and the on State of the system.</p><h6 style="text-align: center;margin-left: 30.0px;"><ac:image ac:align="left"><ri:attachment ri:filename="7460+7708-2 Ignored Elements Option.PNG" /></ac:image></h6><p><br /></p><p><br /></p><p><br /></p><p><br /></p><p><br /></p><p><br /></p><p><br /></p><p><br /></p><p><br /></p><p><br /></p><p><br /></p><p><br /></p><h6 style="margin-left: 30.0px;">The Ignored Elements property set to ignore the ticking State and the off State of timer, and the on State of system.</h6><ac:structured-macro ac:name="warning" ac:schema-version="1" ac:macro-id="655eebad-5cec-4dc8-91f7-c40188dc6cb9"><ac:parameter ac:name="title">Important</ac:parameter><ac:rich-text-body><p>A Timeline chart shows only States and Actions that are actually used, e.g., Actions with duration constraints and signaled States. The used elements will be displayed in the chart and sorted in time order.</p></ac:rich-text-body></ac:structured-macro><h3><br />Reordering Timeline Chart values</h3><p>You can reorder the values monitored on a Timeline Chart as described below.</p><p><br /></p><p>To reorder Timeline Chart values</p><hr /><ol><li>Open the Specification window of a Timeline Chart.</li><li>Click the property specification cell of the <strong>Value</strong> property and click <ac:image ac:thumbnail="true" ac:height="17"><ri:attachment ri:filename="order_button.png" /></ac:image>.<br /><br /><ac:image><ri:attachment ri:filename="reordering_timeline_values.png" /></ac:image><br /><br /></li><li>In the <strong>Order Value</strong> dialog, select the value whose position you want to change.</li><li>Click the <strong>Up</strong> button to move the value up or the <strong>Down</strong> button to move the value down.</li><li>When you are done, click <strong>OK</strong> and close the Specification window.</li></ol><h3><br />Showing the duration of empty/dummy Actions as duration constraints</h3><p>To show the duration of empty/dummy Actions as duration constraints</p><hr /><ul><li class="auto-cursor-target">The Timeline Chart can show empty or dummy actions with duration constraints. The dummy action can be either an empty call Behavior Action with no behavior assigned or an Opaque Action with duration constraints, as shown in the following example.</li></ul><p class="Standard"> <ac:image ac:title="The empty/dummy actions with duration constraints"><ri:attachment ri:filename="1.PNG" /></ac:image></p><p class="Standard"><br /></p><p class="Standard">The Timeline Chart shows the Action names on the left-hand side and the duration simulation performed on the Actions (not the Activities) on the right-hand side. The same thing applies to an Action that has Behaviors assigned, but it is empty and has no diagram. The following figure shows the Timeline chart of the empty/dummy actions from the above example.</p><p class="Standard"> <ac:image ac:align="center" ac:title="The action names of the empty/dummy actions"><ri:attachment ri:filename="2.PNG" /></ac:image></p><h6 class="auto-cursor-target" style="text-align: center;">The Timeline chart of the empty/dummy actions.</h6><h3>Exporting a Timeline Chart</h3><p>To export a Timeline chart</p><hr /><ol><li><p>On the Timeline chart pane (e.g., System), click the <strong>Export</strong> <strong>Data</strong> button on the <strong>Timeline Chart</strong> dialog.<br /><br /></p><h6><ac:image ac:title="The Export Data Button of the Timeline Chart" ac:alt="The Export Data Button of the Timeline Chart"><ri:attachment ri:filename="export_button.png" /></ac:image></h6><p><br /></p></li><li>The Timeline chart will be exported as a CSV format file. The exported Timeline chart in an Excel file is shown in the figure below.</li></ol><p style="margin-left: 30.0px;"><ac:image><ri:attachment ri:filename="Exported CSV (Plain and Excel).png" /></ac:image></p><h3><br />Representing Time Series Charts in a Timeline Chart</h3><p>To represent value properties as separated Time series charts in a Timeline chart</p><hr /><ol><li><p>Open the Specification window of a Timeline chart and click the <strong>Value</strong> tag. Boolean, Enumeration, and Numeric primitive value types (e.g., Number, Real, or Integer), are supported as shown in the following figure.</p><p><ac:image><ri:attachment ri:filename="Numeric Primitive Value Types.PNG" /></ac:image></p><h6>Selecting numeric primitive value types in Value of a Timeline chart.</h6></li><li><p>Run the simulation with the Timeline chart. The selected value properties will be included in the Timeline chart and represented as the Time series chart with fixed height, as separate bars for individual properties (shown in the figure below).</p><p><ac:image><ri:attachment ri:filename="Separated Time Series Chart.PNG" /></ac:image></p><h6>The selected jobsDoneIn value property is represented as the Time series chart in form of separated bars in the Timeline chart.</h6></li></ol><h3>Glossary</h3><ul><li><strong>Context plot</strong><br />A Context plot is a Timeline chart property that enables the plot of the context. It appears on top of the chart as a horizontal line.</li></ul><ul><li><strong>CSV</strong><br />A CSV is a comma-separated values file that stores tabular data (text and number) in plain text. Each line in the file is a record and each record consists of one or more fields, separated by commas.</li></ul><ul><li><strong>Oscilloscope</strong><br />A piece<span style="color:var(--ds-text,#000000);"> of </span>equipment<span style="color:var(--ds-text,#000000);"> showing</span><span style="color:var(--ds-text,#000000);"> </span><span class="NDV" style="color:var(--ds-text,#000000);">oscillations</span><span style="color:var(--ds-text,#000000);"> in an </span>electric<span style="color:var(--ds-text,#000000);"> </span>current<span style="color:var(--ds-text,#000000);"> as </span>waves<span style="color:var(--ds-text,#000000);"> on the </span>screen.</li></ul><ul><li><strong>Timeline chart</strong><br />A Timeline chart is used to describe the Behaviors of both individual Classifiers and Interactions of the Classifiers, focusing attention on the time of events triggering a State change.</li></ul><ul><li><strong>TSV</strong><br />A TSV is a tab-separated values file that stores data in a tabular structure (e.g., database or spreadsheet data). Each line in the file is a record and each record consists of one or more fields, separated by tabs.</li></ul><h3 class="auto-cursor-target">Sample model</h3><p>The models used in the figures on this page are the <strong>FlashingLight</strong> and <strong>OntologicalBehaviorModeling </strong>sample models that come with your modeling tool.</p><p>To open the sample, do either of the following</p><hr /><ul><li>Download <em><ac:link><ri:attachment ri:filename="FlashingLight.mdzip" /></ac:link></em> or<span class="confluence-link"><em> <ac:link><ri:attachment ri:filename="OntologicalBehaviorModeling.mdzip" /></ac:link></em></span>.</li><li>Find it in the modeling tool <em>&lt;<em style="text-align: left;">install_root</em>&gt;\samples\simulation\.</em></li></ul></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=249571512 space=MMA version=4 -->
## PAGE 00746: Trade study analysis

- page_id: `249571512`
- space_key: `MMA`
- source_url: https://docs.nomagic.com/spaces/MMA/pages/249571512/Trade+study+analysis
- version_number: 4
- version_date: `2025-09-12T15:08:46.980+02:00`
- ancestors: Magic Model Analyst / Cameo Simulation Toolkit Documentation > Tutorial > Analysis pattern
- labels: []

### NORMALIZED CONTENT

**On this page:**

33

A trade study or trade-off study is the activity of a multidisciplinary team to identify the most balanced technical solutions among a set of proposed viable solutions (System Engineering Manual, Federal Aviation Administration, 2006).

A trade study is used to compare with a number of alternative solutions to see whether and how well they satisfy a particular set of criteria. Each solution is characterized by a set of measures of effectiveness (often abbreviated “moe’s”) that corresponds to evaluation criteria and has a calculated value or value distribution. The moe’s for a given solution is then evaluated using an objective function (often called a cost function or utility function), and the results for each alternative are compared to select a preferred solution.

Magic Model Analyst / Cameo Simulation Toolkit has built-in support for trade study analysis. The **TradeStudyExamples** sample model is used as a demonstration for trade study analysis through the following steps.

##### Creating a Trade Study Analysis Block

1. Create a new Analysis Block in a Block Definition diagram (BDD), e.g., TradeStudyInstances.
2. Add the main Block of the simulation context as the Part Property of the newly created Analysis Block, e.g., v : VehicleAnalysis .
3. Create a constraint Block containing a constant expression for determining the best weighted value and related constraint parameters, e.g., Criteria .
4. Add the newly created constraint Block as a Constraint Property in the Analysis Block then right-click the Constraint Property and select Stereotype**objectiveFunction**. «objectiveFunction» is a special type of a constraint Block for determining all values of weighted alternatives in terms of weighted criteria.The specification of the constraint must be an equation with LHS = RHS, where LHS contains only one parameter to bind with *TradeAnalysis::^score*, and RHS can contain multiple parameters (bound with corresponding value properties) to evaluate as **winner** criteria.The output of **«objectiveFunction»** will be compared with previous weighted results. If an alternative is greater, it will be set as the **winner** (maximum value by default). However, if you want the minimum value, use a negative value, e.g., *value = -distance*.
5. Create alternatives by creating references properties typed by a Block of alternatives and apply «alternatives» to the newly created references properties, e.g., *C : Caliper*,*R : Rotor*, and*P : Pad* as shown in the figure below. If you intend to use the Parameter Sweep functionality to automatically generate alternatives based on the specified ranges, skip this step.

[IMAGE alt='' src='']

###### The structure of the Trade Study Analysis Block.

##### Inheriting the Analysis Block from the Trade Study Analysis Block

1. From the Containment tree under the **MD Customization for****SysML::analysis patterns::trade study** package, drag **TradeStudy «Block» «Analysis»** into the Block Definition diagram (BDD) created in the previous section. NoteThe **TradeStudy** package is available in all SysML projects. If the **MD Customization for SysML** package is not visible, click [IMAGE alt='' src=''] in the Containment tree pane and select **Show Auxiliary Resources**.
2. To inherit the TradeStudy «block» «Analysis», create a Generalization Relation from the TradeStudyInstances Block to TradeStudy «block» «Analysis» as shown in the figure below.

[IMAGE alt='' src='']

###### Inheriting the Analysis Block from the TradeStudy Block.

##### Creating an Internal Block diagram for alternatives kind = Instance Table

1. Create an Internal Block diagram (IBD) of the TradeAnalysis Block. You must select Parts which have been set as «objectiveFunction» and «alternatives» to display. You must also display ^score (inherited property) in the diagram.
2. Bind ^score with a Binding Connector to the LHS parameter of «objectiveFunction» , e.g., ^score – value . You must also bind a value property of the main simulation context with a Binding Connector to the RHS parameter of «objectiveFunction» , e.g., stoppingDistance – distance .
3. Bind each «alternatives» with a Binding Connector to each Part property.
4. For each «alternatives», source depends on kind through the Tags settings. If kind = TABLE , source must be an instance table which must be the same Classifier as the alternative property, as shown in the two figures below. However, sorting of rows in the table is not necessary.

[IMAGE alt='' src='']

###### TABLE, kind of «alternatives», must be the same Classifier as the alternative property.

[IMAGE alt='' src='']

###### Binding of the TradeAnalysis Block in the Internal Block diagram (kind = TABLE).

##### Creating an Internal Block diagram for alternatives kind = Subtypes

1. Refer to Step 1-3 about .
2. For each «alternatives», source depends on kind through the Tags settings. If kind = SUBTYPES , source must be a parent Block of subtypes which must be the same type as the alternative property, as shown in the two figures below. Also, the parent Block will not be evaluated as well as any Blocks which have Is Abstract = true.

[IMAGE alt='' src='']

###### SUBTYPES, kind of «alternatives», must be the same type as the alternative property.

[IMAGE alt='' src='']

###### Binding of the TradeAnalysis Block in the Internal Block diagram (kind = SUBTYPES).

##### Creating an Internal Block diagram for alternatives kind = Excel

1. Refer to Step 1-3 about .
2. For each «alternatives», source depends on kind through the Tags settings. If kind = EXCEL , source must be either an Instance table linked to an Excel file («DiagramTableMapToDataSource» applied) or using an «ImportMap» . Table columns or element properties must be correctly mapped to Excel/CSV columns as shown in the two figures below (see also Sync with Excel or CSV files ). However, you do not need to use the Read from File command from the Publish Excel toolbar to load data into the table.

[IMAGE alt='' src='']

###### EXCEL, kind of «alternatives» with an Instance table linked to Excel file («DiagramTableMapToDataSource» applied) settings.

[IMAGE alt='' src='']

###### EXCEL, kind of «alternatives» with Import Map settings.

[IMAGE alt='' src='']

###### Binding of the TradeAnalysis Block in the Internal Block diagram (kind = EXCEL, source = Import Map).

##### Creating an Internal Block diagram for alternatives kind = Parameter Sweep

Parameter Sweep generates alternatives automatically based on the specified parameters. Once you , follow the steps below to model an Internal Block Diagram for using Parameter Sweep.

TradeStudyExamples

install_root

To create an Internal Block Diagram for using Parameter Sweep

1. Create an Internal Block diagram (IBD) for the Analysis Block (e.g, TradeStudyParameterSweep ).
2. In the diagram, display the Constraint Property of the Analysis Block with the «objectiveFunction» stereotype.
3. In the diagram, display the ^score Value Property (inherited from the TradeStudy Block in the MD Customization for SysML profile).
4. Connect the ^score Value Property to the LHS parameter of the Constraint Property (e.g., value ) using a Binding Connector.
5. Connect a Value Property of the main simulation context (e.g., stoppingDistance ) to the RHS parameter of the Constraint Property (e.g., distance ) using a Binding Connector.
6. Create Bound References and use Binding Connectors to connect them to specific properties whose alternatives you want to generate in the specified ranges, e.g., outerDiameter : diameter[meter] , thickness : length[meter], etc.
7. Apply the «designVariable» stereotype to the newly created Bound References.
8. Specify ranges for design variables using any of the four methods described in [CONFLUENCE_PAGE title='Parameter sweep' space=''] .

[IMAGE alt='' src='']

###### The Internal Block Diagram for the Analysis Block illustrating how to use different methods of Parameter Sweep.

##### Creating a Simulation Configuration diagram and configuring other settings

Create a Simulation Configuration diagram, add a [SimulationConfig](https://docs.nomagic.com/display/MMA/SimulationConfig+stereotype) to the newly created diagram, and set the following tags:

- executionTarget : set to the TradeAnalysis Block, e.g., BrakeTradeStudy in the sample. executionTarget can be an instance of the TradeAnalysis Block so that the instance can be reconfigured.
- **resultLocation**: a package/instance table must be specified so an instance with related information will be saved after running the simulation. The information includes **N**,****OutOfSpec**, **score**,****winner**, and other elements. NoteIf you do not create a SimulationConfig and run the *TradeAnalysis* Block directly, **TradeStudy** will not be triggered, but the *TradeAnalysis* Block will be run as normal .If the **executionTarget** of a SimulationConfig is the *TradeAnalysis* Block, **TradeStudy** execution will override other executions, so Monte Carlo simulation will not be triggered even if **numberOfRuns** is more than 1.
- silent : set the silent tag accordingly to see the animation.
- rememberFailureStatus : use rememberFailureStatus when evaluating those weighted alternatives. Any alternatives violating any of the attached constraints/Requirements will not be considered as the winner , but they will be used in the calculation of OutOfSpec .
- **Tags neglected**: to neglect **animationSpeed***,***constraintFailureAsBreakpoint***,***UI**, and **autoStart**.

[IMAGE alt='' src='']

###### SimulationConfig created for other settings, e.g., executionTarget and resultLocation.

##### Running the SimulationConfig and reviewing results

1. Run the SimulationConfig created in the previous section.
2. When running the SimulationConfig, the information of TradeStudy will be printed in the Console pane. The Simulation pane will be disabled, but all warning/errors will be printed.
3. There is a progress bar shown with the description of Executing alternative [n] of [total iterations] (Time elapsed: [time]) , and the Cancel button that allows canceling Trade Study as shown in the figure below.
4. Simulation automatically iterates all variants and instantiates all possible configurations in memory. For example, Brake which contains the combinations of Pad (26 instances), Caliper (20 instances), and Rotor (4 instances) will have 26 x 20 x 4 = 2,080 configurations.
5. The **winner** value on each iteration will be compared directly with the **score** value property. NoteThe **Starting Math Engine** progress bar will be shown in this sample because MATLAB is used as the external evaluator. See also [Integration with MATLAB](https://docs.nomagic.com/display/MMA/Integration+with+MATLAB).Any alternatives violating any of the attached constraints/Requirements will not be considered as the **winner**. They will be used in the calculation of **OutOfSpec**.The**rememberFailureStatus** of a SimulationConfig will be used when evaluating those alternatives.When more than one alternative has the same winning score of a Trade Study, a warning message is printed.In some cases, you can click **Unlock** in the **Simulation** pane to see execution details during the execution. [IMAGE alt='' src=''] 
A progress bar shown with description and the Cancel button during the simulation.
6. When the simulation is either completed or canceled, **winning** information will be printed on the **Console** pane in the following three lines as shown in the figure below. The result instance will be saved at the location as specified in **resultLocation** of SimulationConfig. You can create an instance table, set a Classifier to the *TradeAnalysis* Block, and set *Scope* to the package of the results. [IMAGE alt='' src=''] The TradeAnalysis result (in the last 3 lines) is printed on the Console pane, and the result instance is saved into a package and presented in the instance table.
  - The first line shows the number of iterations (completed/canceled) of all alternatives for ***executionTarget*** with elapsed time.
  - The second line displays the *winning* configuration from the **winner** string.
  - The third line is the **winning****score** from the*^score*. NoteThe **winner** string is printed with the formats as follows:*AlternativeProperty.Name1 : StringKind [, AlternativeProperty.Name2 : StringKind, AlternativeProperty.Name3 : StringKind, …]*where *StringKind* will apply the following rules, depending on **kind** of alternative:*kind=TABLE*: then *StringKind*=InstanceName, e.g., P : Saphire 66, C : Alphine K7, R : Rotus 30.*kind=SUBTYPES*: then *StringKind*=subtypesName, e.g., power : Diesel, support : Wheels, stopping : Brakes.*kind=EXCEL*: then *StringKind*=#Row, e.g., R : #5, P : #21, C : #21, where *Row* is the number of Excel rows.*kind=Parameter Sweep:*then*StringKind=*GeneratedValue,**e.g., brakeMU : 0.66, centerLength : 0.12, outerDiameter : 0.29, thickness : 0.04, width : 0.038.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p><strong>On this page:</strong></p><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="a3e228c1-de26-4c37-aaa9-fb6a34ddbe62"><ac:parameter ac:name="maxLevel">3</ac:parameter><ac:parameter ac:name="minLevel">3</ac:parameter></ac:structured-macro></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p>A trade study or trade-off study is the activity of a multidisciplinary team to identify the most balanced technical solutions among a set of proposed viable solutions (System Engineering Manual, Federal Aviation Administration, 2006).</p><p>A trade study is used to compare with a number of alternative solutions to see whether and how well they satisfy a particular set of criteria. Each solution is characterized by a set of measures of effectiveness (often abbreviated “moe’s”) that corresponds to evaluation criteria and has a calculated value or value distribution. The moe’s for a given solution is then evaluated using an objective function (often called a cost function or utility function), and the results for each alternative are compared to select a preferred solution.</p><p>Magic Model Analyst / Cameo Simulation Toolkit has built-in support for trade study analysis. The <strong>TradeStudyExamples</strong> sample model is used as a demonstration for trade study analysis through the following steps.</p><h3>Creating a Trade Study Analysis Block</h3><ol><li>Create a new Analysis Block in a Block Definition diagram (BDD), e.g., <em>TradeStudyInstances.</em></li><li>Add the main Block of the simulation context as the Part Property of the newly created Analysis Block, e.g., <em>v : VehicleAnalysis</em>.</li><li>Create a constraint Block containing a constant expression for determining the best weighted value and related constraint parameters, e.g., <em>Criteria</em>.</li><li><p class="auto-cursor-target">Add the newly created constraint Block as a Constraint Property in the Analysis Block then right-click the Constraint Property and select Stereotype<strong> objectiveFunction</strong>.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="1292f7a8-abed-458b-ada5-296bc6d664cf"><ac:rich-text-body><ul><li>«objectiveFunction» is a special type of a constraint Block for determining all values of weighted alternatives in terms of weighted criteria.</li><li>The specification of the constraint must be an equation with LHS = RHS, where LHS contains only one parameter to bind with <em>TradeAnalysis::^score</em>, and RHS can contain multiple parameters (bound with corresponding value properties) to evaluate as <strong>winner</strong> criteria.</li><li>The output of <strong>«objectiveFunction»</strong> will be compared with previous weighted results. If an alternative is greater, it will be set as the <strong>winner</strong> (maximum value by default). However, if you want the minimum value, use a negative value, e.g., <em>value = -distance</em>.</li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></li><li><p class="auto-cursor-target">Create alternatives by creating references properties typed by a Block of alternatives and apply «alternatives» to the newly created references properties, e.g., <em>C : Caliper</em>,<em> R : Rotor</em>, and<em> P : Pad</em> as shown in the figure below.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="1f012ee3-10f5-4a81-b50b-07383ba5f6cc"><ac:rich-text-body><p><span style="color: rgb(62,63,64);">If you intend to use the Parameter Sweep functionality to automatically generate alternatives based on the specified ranges, skip this step.</span></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></li></ol><p><br /></p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="trade_study_analysis_block.png" /></ac:image></p><h6 style="text-align: center;">The structure of the Trade Study Analysis Block.</h6><h3 class="auto-cursor-target">Inheriting the Analysis Block from the Trade Study Analysis Block</h3><ol><li><p class="auto-cursor-target">From the Containment tree under the <strong>MD Customization for</strong><strong>SysML::analysis patterns::trade study</strong> package, drag <strong>TradeStudy «Block» «Analysis»</strong> into the Block Definition diagram (BDD) created in the previous section.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="dad767c9-aa47-4578-8260-094d18945302"><ac:parameter ac:name="title">Note</ac:parameter><ac:rich-text-body><p>The <strong>TradeStudy</strong> package is available in all SysML projects. If the <strong>MD Customization for SysML</strong> package is not visible, click <ac:image><ri:attachment ri:filename="Filter Icon.png" /></ac:image> in the Containment tree pane and select <strong>Show Auxiliary Resources</strong>.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></li><li>To inherit the TradeStudy «block» «Analysis», create a Generalization Relation from the <strong>TradeStudyInstances</strong> Block to <strong>TradeStudy</strong> «block» «Analysis» as shown in the figure below.</li></ol><p><br /></p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="inheriting_analysis_block.png" /></ac:image></p><h6 style="text-align: center;">Inheriting the Analysis Block from the TradeStudy Block.</h6><h3>Creating an Internal Block diagram for alternatives kind = Instance Table</h3><ol><li>Create an Internal Block diagram (IBD) of the <em>TradeAnalysis</em> Block. You must select Parts which have been set as <strong>«objectiveFunction»</strong> and <strong>«alternatives»</strong> to display. You must also display <em>^score</em> (inherited property) in the diagram.</li><li>Bind<em> ^score</em><strong> </strong>with a Binding Connector to the LHS parameter of <strong>«objectiveFunction»</strong>, e.g., <em>^score – value</em>. You must also bind a value property of the main simulation context with a Binding Connector to the RHS parameter of <strong>«objectiveFunction»</strong>, e.g., <em>stoppingDistance – distance</em>.</li><li>Bind each <strong>«alternatives»</strong> with a Binding Connector to each Part property.</li><li>For each «alternatives», <strong>source</strong> depends on <strong>kind</strong> through the <strong>Tags</strong> settings. If <strong>kind = TABLE</strong>, <strong>source</strong> must be an instance table which must be the same Classifier as the alternative property, as shown in the two figures below. However, sorting of rows in the table is not necessary.</li></ol><p><br /></p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="instance_tables.png" /></ac:image></p><h6 style="text-align: center;">TABLE, kind of «alternatives», must be the same Classifier as the alternative property.</h6><p><ac:image ac:align="center"><ri:attachment ri:filename="7205-3.PNG" /></ac:image></p><h6 style="text-align: center;">Binding of the TradeAnalysis Block in the Internal Block diagram (kind = TABLE).</h6><h3>Creating an Internal Block diagram for alternatives kind = Subtypes</h3><ol><li>Refer to Step 1-3 about <ac:link ac:anchor="CreatinganInternalBlockdiagramforalternativeskind=InstanceTable"><ac:plain-text-link-body><![CDATA[creating an Internal Block diagram for alternatives kind = Instance Table]]></ac:plain-text-link-body></ac:link>.</li><li>For each «alternatives», <strong>source</strong> depends on <strong>kind</strong> through the <strong>Tags</strong> settings. If <strong>kind = SUBTYPES</strong>, <strong>source</strong> must be a parent Block of subtypes which must be the same type as the alternative property, as shown in the two figures below. Also, the parent Block will not be evaluated as well as any Blocks which have <em>Is Abstract</em> = true.</li></ol><p><ac:image ac:align="center"><ri:attachment ri:filename="7205-4.PNG" /></ac:image></p><h6 style="text-align: center;">SUBTYPES, kind of «alternatives», must be the same type as the alternative property.</h6><p><ac:image ac:align="center"><ri:attachment ri:filename="7205-5.PNG" /></ac:image></p><h6 style="text-align: center;">Binding of the TradeAnalysis Block in the Internal Block diagram (kind = SUBTYPES).</h6><h3>Creating an Internal Block diagram for alternatives kind = Excel</h3><ol><li>Refer to Step 1-3 about <ac:link ac:anchor="CreatinganInternalBlockdiagramforalternativeskind=InstanceTable"><ac:plain-text-link-body><![CDATA[creating an Internal Block diagram for alternatives kind = Instance Table]]></ac:plain-text-link-body></ac:link>.</li><li>For each «alternatives», <strong>source</strong> depends on <strong>kind</strong> through the <strong>Tags</strong> settings. If <strong>kind = EXCEL</strong>, <strong>source</strong> must be either an Instance table linked to an Excel file («DiagramTableMapToDataSource» applied) or using an <a href="https://docs.nomagic.com/display/MT/Saving+an+Import+Map">«ImportMap»</a>. Table columns or element properties must be correctly mapped to Excel/CSV columns as shown in the two figures below (see also <a href="https://docs.nomagic.com/display/MT/Sync+with+Excel+or+CSV+files">Sync with Excel or CSV files</a>). However, you do not need to use the <strong>Read from File</strong> command from the <strong>Publish</strong> Excel toolbar to load data into the table.</li></ol><p><br /></p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="alternatives_with_instance_table.png" /></ac:image></p><h6 style="text-align: center;">EXCEL, kind of «alternatives» with an Instance table linked to Excel file («DiagramTableMapToDataSource» applied) settings.</h6><p style="text-align: center;"><ac:image><ri:attachment ri:filename="alternatives_with_import_map_settings.png" /></ac:image></p><h6 style="text-align: center;">EXCEL, kind of «alternatives» with Import Map settings.</h6><p style="text-align: center;"><ac:image><ri:attachment ri:filename="binding_trade_analysis_block.png" /></ac:image></p><h6 style="text-align: center;">Binding of the TradeAnalysis Block in the Internal Block diagram (kind = EXCEL, source = Import Map).</h6><h3>Creating an Internal Block diagram for alternatives kind = Parameter Sweep</h3><p>Parameter Sweep generates alternatives automatically based on the specified parameters. Once you <ac:link ac:anchor="Creating a Trade Study Analysis Block"><ac:plain-text-link-body><![CDATA[create the Analysis Block]]></ac:plain-text-link-body></ac:link>, follow the steps below to model an Internal Block Diagram for using Parameter Sweep.</p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="b6ecefca-c1aa-46b8-b273-33b1daac8b21"><ac:rich-text-body>In this workflow, the <em>TradeStudyExamples</em> model is used as an example. You can find it in the <em>&lt;<em style="text-align: left;">install_root</em>&gt;\samples\simulation</em> directory.</ac:rich-text-body></ac:structured-macro><p><br /></p><p>To create an Internal Block Diagram for using Parameter Sweep</p><hr /><ol><li>Create an Internal Block diagram (IBD) for the Analysis Block (e.g, <em>TradeStudyParameterSweep</em>).</li><li>In the diagram, display the Constraint Property of the Analysis Block with the «objectiveFunction» stereotype.</li><li>In the diagram, display the <em>^score</em> Value Property (inherited from the <em>TradeStudy</em> Block in the <em>MD Customization for SysML</em> profile).</li><li>Connect the<em> ^score</em> Value Property to the LHS parameter of the Constraint Property (e.g.,<em> value</em>) using a Binding Connector.</li><li>Connect a Value Property of the main simulation context (e.g., <em>stoppingDistance</em>) to the RHS parameter of the Constraint Property (e.g., <em>distance</em>) using a Binding Connector.</li><li>Create Bound References and use Binding Connectors to connect them to specific properties whose alternatives you want to generate in the specified ranges, e.g., <em>outerDiameter : diameter[meter]</em>,<em> thickness : length[meter], etc.</em></li><li>Apply the «designVariable» stereotype to the newly created Bound References.</li><li>Specify ranges for design variables using any of the four methods described in <ac:link><ri:page ri:content-title="Parameter sweep" /></ac:link>.</li></ol><p><br /></p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="trade_study_parameter_sweep.png" /></ac:image></p><h6 style="text-align: center;">The Internal Block Diagram for the Analysis Block illustrating how to use different methods of Parameter Sweep.</h6><h3>Creating a Simulation Configuration diagram and configuring other settings</h3><p>Create a Simulation Configuration diagram, add a <a href="https://docs.nomagic.com/display/MMA/SimulationConfig+stereotype">SimulationConfig</a> to the newly created diagram, and set the following tags:</p><ul><li><strong>executionTarget</strong>: set to the <em>TradeAnalysis</em> Block, e.g., <em>BrakeTradeStudy</em> in the sample. <em>executionTarget</em> can be an instance of the <em>TradeAnalysis</em> Block so that the instance can be reconfigured.</li><li><p class="auto-cursor-target"><strong>resultLocation</strong>: a package/instance table must be specified so an instance with related information will be saved after running the simulation. The information includes <strong>N</strong>,<em> </em><strong>OutOfSpec</strong>, <strong>score</strong>,<em> </em><strong>winner</strong>, and other elements.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="a9042770-b92c-4da9-9a78-85871de6b979"><ac:parameter ac:name="title">Note</ac:parameter><ac:rich-text-body><ul><li>If you do not create a SimulationConfig and run the <em>TradeAnalysis</em> Block directly, <strong>TradeStudy</strong> will not be triggered, but the <em>TradeAnalysis</em> Block will be run as normal .</li><li>If the <strong>executionTarget</strong> of a SimulationConfig is the <em>TradeAnalysis</em> Block, <strong>TradeStudy</strong> execution will override other executions, so Monte Carlo simulation will not be triggered even if <strong>numberOfRuns</strong> is more than 1.</li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></li><li><strong>silent</strong>: set the <strong>silent</strong> tag accordingly to see the animation.</li><li><strong>rememberFailureStatus</strong>: use <em>rememberFailureStatus</em> when evaluating those weighted alternatives. Any alternatives violating any of the attached constraints/Requirements will not be considered as the <strong>winner</strong>, but they will be used in the calculation of <strong>OutOfSpec</strong>.</li><li><p><strong>Tags neglected</strong>: to neglect <strong>animationSpeed</strong><em>, </em><strong>constraintFailureAsBreakpoint</strong><em>, </em><strong>UI</strong>, and <strong>autoStart</strong>.</p></li></ul><p><ac:image ac:align="center"><ri:attachment ri:filename="7205-8.PNG" /></ac:image></p><h6 style="text-align: center;">SimulationConfig created for other settings, e.g., executionTarget and resultLocation.</h6><h3>Running the SimulationConfig and reviewing results</h3><ol><li>Run the SimulationConfig created in the previous section.</li><li>When running the SimulationConfig, the information of TradeStudy will be printed in the <strong>Console</strong> pane. The Simulation pane will be disabled, but all warning/errors will be printed.</li><li>There is a progress bar shown with the description of <strong>Executing alternative [n] of [total iterations] (Time elapsed: [time])</strong>, and the <strong>Cancel</strong> button that allows canceling Trade Study as shown in the figure below.</li><li>Simulation automatically iterates all variants and instantiates all possible configurations in memory. For example, <em>Brake</em> which contains the combinations of <em>Pad</em> (26 instances), <em>Caliper</em> (20 instances), and <em>Rotor</em> (4 instances) will have 26 x 20 x 4 = 2,080 configurations.</li><li><p class="auto-cursor-target">The <strong>winner</strong> value on each iteration will be compared directly with the <strong>score</strong> value property.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="06c40a1f-9d62-4a08-9fed-1fe8e8bdaa04"><ac:parameter ac:name="title">Note</ac:parameter><ac:rich-text-body><ul><li>The <strong>Starting Math Engine</strong> progress bar will be shown in this sample because MATLAB is used as the external evaluator. See also <a href="https://docs.nomagic.com/display/MMA/Integration+with+MATLAB">Integration with MATLAB</a>.</li><li>Any alternatives violating any of the attached constraints/Requirements will not be considered as the <strong>winner</strong>. They will be used in the calculation of <strong>OutOfSpec</strong>.</li><li>The<strong> rememberFailureStatus</strong> of a SimulationConfig will be used when evaluating those alternatives.</li><li>When more than one alternative has the same winning score of a Trade Study, a <span>warning message is printed.</span></li><li>In some cases, you can click <strong>Unlock</strong> in the <strong>Simulation</strong> pane to see execution details during the execution.</li></ul></ac:rich-text-body></ac:structured-macro><h6 class="auto-cursor-target"><ac:image><ri:attachment ri:filename="7205-9.PNG" /></ac:image><br />A progress bar shown with description and the Cancel button during the simulation.</h6></li><li><p>When the simulation is either completed or canceled, <strong>winning</strong> information will be printed on the <strong>Console</strong> pane in the following three lines as shown in the figure below.</p><ul><li><p>The first line shows the number of iterations (completed/canceled) of all alternatives for <strong><em>executionTarget</em></strong> with elapsed time.</p></li><li><p>The second line displays the <em>winning</em> configuration from the <strong>winner</strong> string.</p></li><li><p class="auto-cursor-target">The third line is the <strong>winning</strong><strong>score</strong> from the<em> ^score</em>.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="3c1d4f53-3cf4-41da-a371-fabf5080ef6f"><ac:parameter ac:name="title">Note</ac:parameter><ac:rich-text-body><p>The <strong>winner</strong> string is printed with the formats as follows:<em><br />AlternativeProperty.Name1 : StringKind [, AlternativeProperty.Name2 : StringKind, AlternativeProperty.Name3 : StringKind, …]</em></p><p>where <em>StringKind</em> will apply the following rules, depending on <strong>kind</strong> of alternative:</p><ul><li><p><em>kind=TABLE</em>: then <em>StringKind</em>=InstanceName, e.g., P : Saphire 66, C : Alphine K7, R : Rotus 30.</p></li><li><p><em>kind=SUBTYPES</em>: then <em>StringKind</em>=subtypesName, e.g., power : Diesel, support : Wheels, stopping : Brakes.</p></li><li><p><em>kind=EXCEL</em>: then <em>StringKind</em>=#Row, e.g., R : #5, P : #21, C : #21, where <em>Row</em> is the number of Excel rows.</p></li><li><em>kind=Parameter Sweep: </em>then<em> StringKind=</em>GeneratedValue,<em> </em>e.g., brakeMU : 0.66, centerLength : 0.12, outerDiameter : 0.29, thickness : 0.04, width : 0.038.</li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></li></ul><p>The result instance will be saved at the location as specified in <strong>resultLocation</strong> of SimulationConfig. You can create an instance table, set a Classifier to the <em>TradeAnalysis</em> Block, and set <em>Scope</em> to the package of the results.</p><p><ac:image ac:align="center"><ri:attachment ri:filename="7205-10.PNG" /></ac:image></p><h6 style="text-align: center;">The TradeAnalysis result (in the last 3 lines) is printed on the Console pane, and the result instance is saved into a package and presented in the instance table.</h6></li></ol></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=249570898 space=MMA version=2 -->
## PAGE 00747: Trigger on nested Port

- page_id: `249570898`
- space_key: `MMA`
- source_url: https://docs.nomagic.com/spaces/MMA/pages/249570898/Trigger+on+nested+Port
- version_number: 2
- version_date: `2025-08-19T14:56:19.305+02:00`
- ancestors: Magic Model Analyst / Cameo Simulation Toolkit Documentation > User Guide > Simulation of SysML models > Supported SysML elements
- labels: ['trigger-on-nested-port']

### NORMALIZED CONTENT

When you model a State Machine in your system whose Transition has a Trigger stereotyped with «TriggerOnNestedPort», Magic Model Analyst / Cameo Simulation Toolkit will use the tagged value onNestedPort to check the Port and find which object receives the triggering Events.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>When you model a State Machine in your system whose Transition has a Trigger stereotyped with «TriggerOnNestedPort», Magic Model Analyst / Cameo Simulation Toolkit will use the tagged value onNestedPort to check the Port and find which object receives the triggering Events. </p>
````

<!--NOMAGIC_PAGE id=249571305 space=MMA version=1 -->
## PAGE 00748: Tutorial

- page_id: `249571305`
- space_key: `MMA`
- source_url: https://docs.nomagic.com/spaces/MMA/pages/249571305/Tutorial
- version_number: 1
- version_date: `2022-03-24T12:13:14.858+01:00`
- ancestors: Magic Model Analyst / Cameo Simulation Toolkit Documentation
- labels: []

### NORMALIZED CONTENT

h4

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="73f0886b-8e32-4e8b-855a-c28308717024"><ac:parameter ac:name="style">h4</ac:parameter></ac:structured-macro></p>
````

<!--NOMAGIC_PAGE id=249569709 space=MMA version=2 -->
## PAGE 00749: UI modeling diagram simulation

- page_id: `249569709`
- space_key: `MMA`
- source_url: https://docs.nomagic.com/spaces/MMA/pages/249569709/UI+modeling+diagram+simulation
- version_number: 2
- version_date: `2025-08-19T14:56:06.644+02:00`
- ancestors: Magic Model Analyst / Cameo Simulation Toolkit Documentation > User Guide > Simulation Configuration and UI modeling
- labels: ['ui-modeling-diagram-simulation', 'simulating-ui-modeling-diagram']

### NORMALIZED CONTENT

**On this page**

33

The MagicDraw User Interface Modeling diagram becomes even more powerful and valuable when used with Magic Model Analyst / Cameo Simulation Toolkit. Supported UI components are as follows

##### Frames

You need to drag a Classifier to a UI Frame to bind them together (Magic Model Analyst / Cameo Simulation Toolkit will automatically apply a «UI» stereotype and set its **represents** tag to the Classifier). Once bound, the UI Frame can represent the Classifier. The **source** tag of the applied «UI» stereotype will also be set as *com.nomagic.magicdraw.simulation.uiprototype.UIDiagramFrame* by default.

#### NOTE: Note

Note

- The represents and source tag values are necessary to run a simulation with UI.
- If you use the User Interface Configuration element on the diagram toolbars, you need to manually specify the represents and source tag values accordingly.

##### Panels

A UI Panel can hold any supported UI components, such as buttons, labels, sliders, check boxes, text fields, combo boxes, spinners, radio buttons, and even panels themselves.

- If a UI Panel resides in a UI Frame, drag the Property of a Classifier that the UI Frame represents to the UI Panel to bind that Property to the UI Panel. The «NestedUIConfig» stereotype will be automatically applied; its "feature" tag will then be set to the Property and its "Text" tag will also be set to the name of that Property. In this case, the UI Panel represents the Property.
- If a UI Panel (child) resides in another UI Panel (parent), drag the Property of a Classifier that types the Property and the parent UI Panel it represents to the child UI Panel to bind that Property to the UI Panel. The «NestedUIConfig» stereotype will be automatically applied; its "feature" tag will then be set to the Property and its "Text" tag will also be set to the name of that Property. This functionality allows you to bind the nested parts (properties) of a Classifier to its correspondent nested UI Panels in a UI Frame representing the Classifier.
- Y ou can also reuse existing UI components (all supported ones, except the frame) in an existing UI Frame in another UI Panel. To reuse existing components, drag the UI Frame model in the Containment tree to that UI Panel. The «NestedUIConfig» stereotype will be automatically applied if it has not been and its "config" tag will then be set to the UI Frame.

During runtime, UI components in the UI Panel can also display their documentation as a tooltip.

[IMAGE alt='' src='']

###### Runtime documentation of User Interface components displayed as a tooltip.

##### Group boxes

Group boxes have similar usages to Panels.

##### TextFields, checkboxes, and sliders

Drag a Property to one of these three UI components to bind the Property with that particular UI component. The «RuntimeValue» stereotype will be automatically applied, its "element" tag will be set to the Property, and its "Text" tag will also be set to the name of that Property. In this case, the UI component represents the Property. Once represented, the UI component will reflect the value of the represented Property in the **Variables** pane during simulation, and vice versa.

##### Labels

Drag a Property to a UI Label to bind the Property with that particular UI Label. The «RuntimeValue» stereotype will be automatically applied, its "element" tag will be set to the Property, and its "Text" tag will also be set to the name of that Property. In this case, the UI Label represents the Property. Once represented, the UI Label will display the value of the represented Property in the **Variables** pane during simulation.

##### Buttons

You can use a UI button to send Signal(s), call Operation(s), or call Behavior(s).

To use a UI button to send a Signal

- Drag a Signal to a UI button to associate it with the button. The «SignalInstance» stereotype will be automatically applied, its "element" ("signal") tag will then be set to the Signal, and its "Text" tag will also be set as the name of that Signal.

In addition, runtime values will be automatically created for all of the attributes and placed under the UI button if the signal has attributes. You can specify the values to be used at runtime in the "value" tag of these runtime values. If you click this UI button during simulation, it will send the associated Signal along with its runtime values.

To use a UI button to call an operation

- Drag an Operation to a UI button to associate the Operation with the UI button. The «OperationCall» stereotype will be automatically applied, its "element" tag will then be set to the Operation, and its "Text" tag will also be set to the name of that Operation.

If you click this UI button is during simulation, it will call the associated Operation.

To use a UI button to call a behavior

- Drag a Behavior, such as an Activity, to a UI button to associate it with the button. The «BehaviorCall» stereotype will be automatically applied, its "element" tag will then be set to the Behavior, and its "Text" tag will also be set to the name of that Behavior.

If you click this UI button during simulation, it will call the associated Behavior.

##### Combo boxes and spinners

Drag a Property typed by Enumeration to one of these two UI components (ComboBoxes and Spinners) to bind the Property to that particular UI component. The «RuntimeValue» stereotype will be automatically applied, its "element" tag will then be set to the Property, and its "Text" tag will also be set to the name of that Property. In this case, the UI component will represent the Property typed by Enumeration. Once represented, the UI component will reflect the value (the selected Enumeration Literal) of the represented Property in the **Variables** pane during simulation, and vice versa.

##### Radio buttons

Drag a Property typed by Enumeration to a UI Panel or GroupBox to bind the Property to that particular UI panel or GroupBox. The «RuntimeValue» stereotype will be automatically applied, its "element" tag will then be set to the Property, and its "Text" tag will also be set to the name of that Property. All Enumeration Literals of the Property type will be automatically created as a vertical list of UI RadioButtons. Each UI RadioButton will represent Enumeration Literal of the Property type accordingly. Once represented, the UI RadioButton will display the value of the represented Property in the **Variables** pane during simulation.

In addition, you can assign or re-assign other Enumeration Literals to an existing UI RadioButton by dragging other Enumeration Literals of the same Property type to the existing UI RadioButton. Also, you can create a single UI RadioButton to represent a particular Enumeration Literal by dragging the Enumeration Literal to a UI Panel or GroupBox. The «RuntimeValue» stereotype will be automatically applied, its "element" tag will then be set to Enumeration Literal, and its "Text" tag will also be set to the name of the Enumeration Literal. 
 
The following figure demonstrates an example of using MagicDraw's User Interface Modeling Diagram with Magic Model Analyst / Cameo Simulation Toolkit.

[IMAGE alt='' src='']

###### Using the MagicDraw User Interface modeling diagram with Magic Model Analyst / Cameo Simulation Toolkit.

The steps in this example are as follows

1. Drag a Classifier to a UI frame.
2. Drag each Signal to each UI button to associate it with the button.
3. Specify a value for each UI button's runtime value (the runtime value is located under each UI button).
4. Drag any Classifier's property to a UI label to be represented.
5. Reference the frame in the "UI" tag of the SimulationConfig.

See the *Calculator.mdzip* sample for detailed instructions.When you drag any GUI elements to a diagram, click **Run** to simulate the animation.

#### NOTE: Note

Note

- The current version of Magic Model Analyst / Cameo Simulation Toolkit supports frames, panels, group boxes, labels, buttons, check boxes, text fields, sliders, combo boxes, spinners, and radio buttons only.
- Do not drag any model elements of an existing UI Frame (from the Containment tree) to a diagram to create one more ComponentView/Frame symbol on the diagram. Magic Model Analyst / Cameo Simulation Toolkit does not support two UI symbols of the same model element.
- Other samples include: SmallTestSamples.mdzip , StopWatch_advanced.mdzip , and SimpleUI_labelUpdate.mdzip .

###### Sample models

The models used on this page are the **CarBrakingAnalysis** and **Calculator** sample models that come with MagicDraw. To open a sample, do either of the following

- Download [ATTACHMENT filename='CarBrakingAnalysis.mdzip'] or [ATTACHMENT filename='Calculator.mdzip'].
- Find it in the modeling tool <*install_root*>\samples\simulation.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p><strong>On this page</strong></p><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="3551dcde-85c3-4f4a-b73f-5980bee9e295"><ac:parameter ac:name="maxLevel">3</ac:parameter><ac:parameter ac:name="minLevel">3</ac:parameter></ac:structured-macro></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p>The MagicDraw User Interface Modeling diagram becomes even more powerful and valuable when used with Magic Model Analyst / Cameo Simulation Toolkit. Supported UI components are as follows</p><h3>Frames</h3><p>You need to drag a Classifier to a UI Frame to bind them together (Magic Model Analyst / Cameo Simulation Toolkit will automatically apply a «UI» stereotype and set its <strong>represents</strong> tag to the Classifier). Once bound, the UI Frame can represent the Classifier. The <strong>source</strong> tag of the applied «UI» stereotype will also be set as <em>com.nomagic.magicdraw.simulation.uiprototype.UIDiagramFrame</em> by default. <br class="atl-forced-newline" /><br class="atl-forced-newline" /></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="ba141db8-e6d3-42d2-ab40-38d591f1991d"><ac:parameter ac:name="title">Note</ac:parameter><ac:rich-text-body><ul><li>The <strong>represents</strong> and <strong>source</strong> tag values are necessary to run a simulation with UI.</li><li><span>If you use the </span><strong>User Interface Configuration</strong><span> element on the diagram toolbars, you need to manually specify the </span><strong>represents</strong><span> and </span><strong>source</strong><span> tag values accordingly. </span></li></ul></ac:rich-text-body></ac:structured-macro><h3>Panels</h3><p>A UI Panel can hold any supported UI components, such as buttons, labels, sliders, check boxes, text fields, combo boxes, spinners, radio buttons, and even panels themselves. </p><ul><li><span>If a UI Panel resides in a UI Frame, drag the Property of a Classifier that the UI Frame represents to the UI Panel to bind that Property to the UI Panel. The «NestedUIConfig» stereotype will be automatically applied; its &quot;feature&quot; tag will then be set to the Property and its &quot;Text&quot; tag will also be set to the name of that Property. In this case, the UI Panel represents the Property.</span></li><li><span> </span><span>If a UI Panel (child) resides in another UI Panel (parent), drag the Property of a Classifier that types the Property and the parent UI Panel it represents to the child UI Panel to bind that Property to the UI Panel. The «NestedUIConfig» stereotype will be automatically applied; its &quot;feature&quot; tag will then be set to the Property and its &quot;Text&quot; tag will also be set to the name of that Property. This functionality allows you to bind the nested parts (properties) of a Classifier to its correspondent nested UI Panels in a UI Frame representing the Classifier.</span></li><li><span>Y</span>ou can also reuse existing UI components (all supported ones, except the frame) in an existing UI Frame in another UI Panel. To reuse existing components, drag the UI Frame model in the Containment tree to that UI Panel. The «NestedUIConfig» stereotype will be automatically applied if it has not been and its &quot;config&quot; tag will then be set to the UI Frame. </li></ul><p>During runtime, UI components in the UI Panel can also display their documentation as a tooltip. <br class="atl-forced-newline" /><br class="atl-forced-newline" /></p><p><ac:image ac:align="center" ac:title="Run-Time Documentation ofUser Interface Components Displayed as Tooltip" ac:alt="Run-Time Documentation ofUser Interface Components Displayed as Tooltip"><ri:attachment ri:filename="specfication-of-simulation-cruise-control.png" /></ac:image></p><h6 style="text-align: center;">Runtime documentation of User Interface components displayed as a tooltip.<br class="atl-forced-newline" /><br class="atl-forced-newline" /></h6><h3>Group boxes</h3><p>Group boxes have similar usages to Panels.</p><h3>TextFields, checkboxes, and sliders</h3><p>Drag a Property to one of these three UI components to bind the Property with that particular UI component. The «RuntimeValue» stereotype will be automatically applied, its &quot;element&quot; tag will be set to the Property, and its &quot;Text&quot; tag will also be set to the name of that Property. In this case, the UI component represents the Property. Once represented, the UI component will reflect the value of the represented Property in the <strong>Variables</strong> pane during simulation, and vice versa. </p><h3>Labels</h3><p>Drag a Property to a UI Label to bind the Property with that particular UI Label. The «RuntimeValue» stereotype will be automatically applied, its &quot;element&quot; tag will be set to the Property, and its &quot;Text&quot; tag will also be set to the name of that Property. In this case, the UI Label represents the Property. Once represented, the UI Label will display the value of the represented Property in the <strong>Variables</strong> pane during simulation. </p><h3>Buttons</h3><p>You can use a UI button to send Signal(s), call Operation(s), or call Behavior(s).</p><p>To use a UI button to send a Signal</p><hr /><ul><li>Drag a Signal to a UI button to associate it with the button. The «SignalInstance» stereotype will be automatically applied, its &quot;element&quot; (&quot;signal&quot;) tag will then be set to the Signal, and its &quot;Text&quot; tag will also be set as the name of that Signal. </li></ul><p><br class="atl-forced-newline _mce_tagged_br" />In addition, runtime values will be automatically created for all of the attributes and placed under the UI button if the signal has attributes. You can specify the values to be used at runtime in the &quot;value&quot; tag of these runtime values. If you click this UI button during simulation, it will send the associated Signal along with its runtime values. </p><p>To use a UI button to call an operation</p><hr /><ul><li>Drag an Operation to a UI button to associate the Operation with the UI button. The «OperationCall» stereotype will be automatically applied, its &quot;element&quot; tag will then be set to the Operation, and its &quot;Text&quot; tag will also be set to the name of that Operation.</li></ul><p>If you click this UI button is during simulation, it will call the associated Operation. </p><p>To use a UI button to call a behavior </p><hr /><ul><li>Drag a Behavior, such as an Activity, to a UI button to associate it with the button. The «BehaviorCall» stereotype will be automatically applied, its &quot;element&quot; tag will then be set to the Behavior, and its &quot;Text&quot; tag will also be set to the name of that Behavior.<br /><br /></li></ul><p>If you click this UI button during simulation, it will call the associated Behavior. </p><h3>Combo boxes and spinners</h3><p>Drag a Property typed by Enumeration to one of these two UI components (ComboBoxes and Spinners) to bind the Property to that particular UI component. The «RuntimeValue» stereotype will be automatically applied, its &quot;element&quot; tag will then be set to the Property, and its &quot;Text&quot; tag will also be set to the name of that Property. In this case, the UI component will represent the Property typed by Enumeration. Once represented, the UI component will reflect the value (the selected Enumeration Literal) of the represented Property in the <strong>Variables</strong> pane during simulation, and vice versa. </p><h3>Radio buttons</h3><p>Drag a Property typed by Enumeration to a UI Panel or GroupBox to bind the Property to that particular UI panel or GroupBox. The «RuntimeValue» stereotype will be automatically applied, its &quot;element&quot; tag will then be set to the Property, and its &quot;Text&quot; tag will also be set to the name of that Property. All Enumeration Literals of the Property type will be automatically created as a vertical list of UI RadioButtons. Each UI RadioButton will represent Enumeration Literal of the Property type accordingly. Once represented, the UI RadioButton will display the value of the represented Property in the <strong>Variables</strong> pane during simulation. </p><p>In addition, you can assign or re-assign other Enumeration Literals to an existing UI RadioButton by dragging other Enumeration Literals of the same Property type to the existing UI RadioButton. Also, you can create a single UI RadioButton to represent a particular Enumeration Literal by dragging the Enumeration Literal to a UI Panel or GroupBox. The «RuntimeValue» stereotype will be automatically applied, its &quot;element&quot; tag will then be set to Enumeration Literal, and its &quot;Text&quot; tag will also be set to the name of the Enumeration Literal. <br class="atl-forced-newline" /><br class="atl-forced-newline" />The following figure demonstrates an example of using MagicDraw's User Interface Modeling Diagram with Magic Model Analyst / Cameo Simulation Toolkit. </p><p><br class="atl-forced-newline" /><ac:image ac:align="center" ac:title="Using the MagicDraw User Interface Modeling Diagram with Magic Model Analyst / Cameo Simulation Toolkit" ac:alt="Using the MagicDraw User Interface Modeling Diagram with Magic Model Analyst / Cameo Simulation Toolkit"><ri:attachment ri:filename="Figure 24.png" /></ac:image></p><h6 style="text-align: center;">Using the MagicDraw User Interface modeling diagram with Magic Model Analyst / Cameo Simulation Toolkit.<br class="atl-forced-newline" /><br /></h6><p>The steps in this example are as follows</p><ol><li>Drag a Classifier to a UI frame.</li><li>Drag each Signal to each UI button to associate it with the button.</li><li>Specify a value for each UI button's runtime value (the runtime value is located under each UI button).</li><li>Drag any Classifier's property to a UI label to be represented.</li><li><span>Reference the frame in the &quot;UI&quot; tag of the SimulationConfig. </span></li></ol><p><span>See the <em>Calculator.mdzip</em> sample for detailed instructions. </span>When you drag any GUI elements to a diagram, click <strong>Run</strong> to simulate the animation. </p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="b84aab4a-0802-4cf6-af81-2844f38f4f17"><ac:parameter ac:name="title">Note</ac:parameter><ac:rich-text-body><ul><li>The current version of Magic Model Analyst / Cameo Simulation Toolkit supports frames, panels, group boxes, labels, buttons, check boxes, text fields, sliders, combo boxes, spinners, and radio buttons only.</li><li>Do not drag any model elements of an existing UI Frame (from the Containment tree) to a diagram to create one more ComponentView/Frame symbol on the diagram. Magic Model Analyst / Cameo Simulation Toolkit does not support two UI symbols of the same model element.</li><li>Other samples include: <em>SmallTestSamples.mdzip</em>, <em>StopWatch_advanced.mdzip</em>, and <em>SimpleUI_labelUpdate.mdzip</em>. </li></ul></ac:rich-text-body></ac:structured-macro><h4 class="auto-cursor-target">Sample models</h4><p>The models used on this page are the <strong>CarBrakingAnalysis</strong> and <strong>Calculator</strong> sample models that come with MagicDraw. To open a sample, do either of the following</p><hr /><ul><li>Download <ac:link><ri:attachment ri:filename="CarBrakingAnalysis.mdzip" /></ac:link><span class="confluence-link"> or <ac:link><ri:attachment ri:filename="Calculator.mdzip"><ri:page ri:content-title="Auto-generating HTML files" /></ri:attachment></ac:link>.</span></li><li>Find it in the modeling tool <em>&lt;<em style="text-align: left;">install_root</em>&gt;\samples\simulation.</em></li></ul></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=249570139 space=MMA version=3 -->
## PAGE 00750: Understanding simulation sessions

- page_id: `249570139`
- space_key: `MMA`
- source_url: https://docs.nomagic.com/spaces/MMA/pages/249570139/Understanding+simulation+sessions
- version_number: 3
- version_date: `2025-08-19T14:56:08.586+02:00`
- ancestors: Magic Model Analyst / Cameo Simulation Toolkit Documentation > User Guide > Simulation debugging
- labels: ['simulation-sessions']

### NORMALIZED CONTENT

1130427757

1130427759

1130427758

Magic Model Analyst / Cameo Simulation Toolkit creates a simulation session(s) while a model is being simulated. A simulation session contains a context with a specified runtime value. The context of the simulation session is the executing UML element that can be either a Class element or a sub-type of a Class. When the context element is simulated, a runtime object will be created to store the simulated values.

You can create multiple simulation sessions during a single simulation, such as an Activity simulation. If the simulated Activity contains any callBehaviorAction, a new simulation session will be created to simulate each callBehaviorAction. The **Sessions** pane will display all simulation sessions during simulation and order them by context elements in a tree node, as shown below.

[IMAGE alt='' src='']

###### The Simulation Sessions pane.

You can open the **[CONFLUENCE_PAGE title='Simulation time and simulation clock' space='']** dialog to see the simulation clock in real time by right-clicking any context elements in the **Simulation Sessions** pane and selecting**Show Simulation Clock**.

While executing a model, you can double-click a running session to open a diagram of that particular session containing the progress of the simulation as shown below.

[IMAGE alt='' src='']

###### Double-clicking a running session to show the diagram at runtime.

1130427756

**Related page**

- Simulation time and simulation clock

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="24bb362e-c1fe-46ec-8743-163336383e39"><ac:parameter ac:name="id">1130427757</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="c0ad1fac-5225-4fbb-aefa-06fc89b88759"><ac:parameter ac:name="id">1130427759</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="beb24355-e0f6-473f-94bc-8139785083c9"><ac:parameter ac:name="id">1130427758</ac:parameter><ac:rich-text-body><p>Magic Model Analyst / Cameo Simulation Toolkit creates a simulation session(s) while a model is being simulated. A simulation session contains a context with a specified runtime value. The context of the simulation session is the executing UML element that can be either a Class element or a sub-type of a Class. When the context element is simulated, a runtime object will be created to store the simulated values. </p><p>You can create multiple simulation sessions during a single simulation, such as an Activity simulation. If the simulated Activity contains any callBehaviorAction, a new simulation session will be created to simulate each callBehaviorAction. The <strong>Sessions</strong> pane will display all simulation sessions during simulation and order them by context elements in a tree node, as shown below.</p><p><br /></p><p><ac:image ac:align="center"><ri:attachment ri:filename="Sessions Window.PNG" /></ac:image></p><h6 style="text-align: center;">The Simulation Sessions pane.</h6><p>You can open the <strong><ac:link><ri:page ri:content-title="Simulation time and simulation clock" /><ac:plain-text-link-body><![CDATA[Simulation clock]]></ac:plain-text-link-body></ac:link></strong> dialog to see the simulation clock in real time by right-clicking any context elements in the <strong>Simulation Sessions</strong> pane and selecting<strong> Show Simulation Clock</strong>.</p><p>While executing a model, you can double-click a running session to open a diagram of that particular session containing the progress of the simulation as shown below.</p><p><ac:image ac:align="center" ac:title="Double-Clicking a Running Session to Show the Diagram at Runtime" ac:alt="Double-Clicking a Running Session to Show the Diagram at Runtime" ac:width="900"><ri:attachment ri:filename="sim-console-d.png" /></ac:image></p><h6 style="text-align: center;">Double-clicking a running session to show the diagram at runtime.</h6></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="4822e0da-817a-4643-8494-1486b205a325"><ac:parameter ac:name="id">1130427756</ac:parameter><ac:rich-text-body><p><strong>Related page</strong></p><ul><li><a href="https://docs.nomagic.com/display/MMA/Simulation+time+and+simulation+clock">Simulation time and simulation clock</a></li></ul></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=249570832 space=MMA version=2 -->
## PAGE 00751: Unit Conversion

- page_id: `249570832`
- space_key: `MMA`
- source_url: https://docs.nomagic.com/spaces/MMA/pages/249570832/Unit+Conversion
- version_number: 2
- version_date: `2025-09-12T15:11:52.838+02:00`
- ancestors: Magic Model Analyst / Cameo Simulation Toolkit Documentation > User Guide > Parametric evaluator
- labels: []

### NORMALIZED CONTENT

The units of structural features (such as Value Properties, Flow Properties, Constraint Parameters, etc.) that are connected through a Binding Connector can be automatically converted. The units are converted only if both sides have a compatible set of units of the same quantity kind. If the conversion fails due toincompatible units, the values are mirrored the same as with the Auto Convert Units option disabled.

800450

The units can be loaded through the ISO 80000 library and ISO 80000 extension. To learn more about how to load and apply units, refer to [CONFLUENCE_PAGE title='Using Units' space='MT'].

Unit conversion is performed according to the SysML extension QUDV. You can also create your own units or whole library based on the QUDV standard. To learn more about the QUDV library, refer to [CONFLUENCE_PAGE title='Using QUDV model library' space='MT'].

The supported unit types in the QUDV library include:

- PrefixedUnit (e.g., kilogram)
- LinearConversionUnit (e.g., inch)
- AffineConversionUnit (e.g., Fahrenheit)
- DerivedUnit (e.g., km/h)
- SimpleUnit (base unit, eg., gram)

You can use different kinds of units for different structural features based on the usage and domain. The following example shows that basic SI units are set on Constraint Parameters and imperial units are set on Value Properties.

###### [IMAGE alt='' src=''] 
SI units and imperial units used in one Parametric Diagram

Units are converted according to the definitions (or values) set in the Unit element. For linear conversion units, the most important aspects are **factor**and **referenceUnit**.

###### [IMAGE alt='' src=''] 
Unit pound Specification dialog

##### Enabling or disabling the Auto Convert Units option

To enable or disable the **Auto Convert Units** option in the Project Options dialog

- In the [CONFLUENCE_PAGE title='Project options' space=''] dialog, set the Auto Convert Units property value to true to enable the functionality or false to disable the functionality. [ATTACHMENT filename='Auto Convert Unit _Project Option.png']

To enable or disable the **Auto Convert Units** option in the Simulation Configuration Specification dialog

- In the Simulation Configuration Specification dialog, set the Auto Convert Units property value to true to enable the functionality or false to disable the functionality. [ATTACHMENT filename='Auto Convert Unit _Specification Dialog.png']

- The Auto Convert Units op tion is enabled by default for the project. The Auto Convert Units option is disabled by default for the projects saved with versions previous to the 2024x version.
- The Auto Convert Units option in the Simulation Configuration Specification dialog is only visible with the Expert mode.
- The simulation properties set in the Simulation Configuration supersede the ones set in the Project Options dialog.

The Transmission sample uses unit conversion in its Parametric Diagram.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>The units of structural features (such as Value Properties, Flow Properties, Constraint Parameters, etc.) that are connected through a Binding Connector can be automatically converted. The units are converted only if both sides have a compatible set of units of the same quantity kind. <span style="color: rgb(23,43,77);">If the conversion fails due to<span> </span></span><span style="color: rgb(23,43,77);">incompatible units, the values are mirrored the same as with the Auto Convert Units option disabled.</span></p><p><br /></p><p style="text-align: center;"><ac:structured-macro ac:name="widget" ac:schema-version="1" ac:macro-id="99660f72-e540-48c2-9a9c-987109f39306"><ac:parameter ac:name="width">800</ac:parameter><ac:parameter ac:name="url"><ri:url ri:value="https://www.youtube.com/watch?v=-seC3_leZxI" /></ac:parameter><ac:parameter ac:name="height">450</ac:parameter></ac:structured-macro></p><p style="text-align: center;"><br /></p><p>The units can be loaded through the ISO 80000 library and ISO 80000 extension. To learn more about how to load and apply units, refer to <ac:link><ri:page ri:space-key="MT" ri:content-title="Using Units" /></ac:link>.</p><p>Unit conversion is performed according to the SysML extension QUDV. You can also create your own units or whole library based on the QUDV standard. To learn more about the QUDV library, refer to <ac:link><ri:page ri:space-key="MT" ri:content-title="Using QUDV model library" /><ac:plain-text-link-body><![CDATA[QUDV library]]></ac:plain-text-link-body></ac:link>. </p><p>The supported unit types in the QUDV library <ac:inline-comment-marker ac:ref="1b748246-8604-4cfe-b416-3423f720ab53">include:</ac:inline-comment-marker></p><ul><li>PrefixedUnit (e.g., kilogram)</li><li>LinearConversionUnit (e.g., inch)</li><li>AffineConversionUnit (e.g., Fahrenheit)</li><li>DerivedUnit (e.g., km/h)</li><li><p>SimpleUnit (base unit, eg., gram)</p></li></ul><p><span style="color: rgb(23,43,77);">You can use different kinds of units for different structural features based on the usage and domain. The following example shows that basic SI units are set on Constraint Parameters and imperial units are set on Value Properties.</span></p><h6 style="text-align: center;"><ac:image><ri:attachment ri:filename="Conversion.PNG" /></ac:image><br />SI units and imperial units used in one Parametric Diagram</h6><p>Units are converted according to the definitions (or values) set in the Unit element. For linear conversion units, the most important aspects are <strong>factor </strong>and <strong>referenceUnit</strong>.<br /><br /></p><h6 style="text-align: center;"><ac:image><ri:attachment ri:filename="Unit Pound Specification dialog.png" /></ac:image><br />Unit pound Specification dialog</h6><h3>Enabling or disabling the Auto Convert Units option</h3><p>To enable or disable the <strong>Auto Convert Units</strong> option in the Project Options dialog</p><hr /><ul><li>In the <ac:link><ri:page ri:content-title="Project options" /><ac:plain-text-link-body><![CDATA[Project Options]]></ac:plain-text-link-body></ac:link> dialog, set the <strong>Auto Convert Units</strong> property value to <em>true </em>to <span style="color: rgb(62,63,64);">enable the functionality</span> or <em>false </em>to <span style="color: rgb(62,63,64);">disable the functionality.</span><br /><br /><ac:image><ri:attachment ri:filename="Auto Convert Unit _Project Option.png" /></ac:image><br /><br /></li></ul><p>To enable or disable the <strong>Auto Convert Units</strong> option in the Simulation Configuration Specification dialog</p><hr /><ul><li>In the Simulation Configuration Specification dialog, set the <strong>Auto Convert Units</strong> property value to <em>true </em>to <span style="color: rgb(62,63,64);">enable the functionality</span> or <em>false </em>to <span style="color: rgb(62,63,64);">disable the functionality.</span><br /><br /><ac:image><ri:attachment ri:filename="Auto Convert Unit _Specification Dialog.png" /></ac:image><br /><br /></li></ul><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="8761d078-650f-4837-aa57-37908b10d109"><ac:rich-text-body><ul><li><ac:inline-comment-marker ac:ref="2d4daac9-da28-4498-b33d-a587ad0577ff">The</ac:inline-comment-marker><strong><ac:inline-comment-marker ac:ref="2d4daac9-da28-4498-b33d-a587ad0577ff"> Auto Convert Units</ac:inline-comment-marker></strong><ac:inline-comment-marker ac:ref="2d4daac9-da28-4498-b33d-a587ad0577ff"> op</ac:inline-comment-marker>tion is enabled by default for the project. The <strong>Auto Convert Units</strong> option is disabled by default for the projects saved with versions previous to the 2024x version.</li><li>The <strong>Auto Convert Units</strong> option in the <span style="color: rgb(62,63,64);">Simulation Configuration </span>Specification dialog is only visible with the <strong>Expert </strong>mode.</li><li>The simulation properties set in the Simulation Configuration supersede the ones set in the Project Options dialog.</li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="c6584506-3635-4654-a4e8-4c006b8a2623"><ac:rich-text-body><p>The Transmission sample uses unit conversion in its Parametric Diagram.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p>
````

<!--NOMAGIC_PAGE id=249570301 space=MMA version=3 -->
## PAGE 00752: Updating default values

- page_id: `249570301`
- space_key: `MMA`
- source_url: https://docs.nomagic.com/spaces/MMA/pages/249570301/Updating+default+values
- version_number: 3
- version_date: `2025-09-12T15:05:18.564+02:00`
- ancestors: Magic Model Analyst / Cameo Simulation Toolkit Documentation > User Guide > Simulation debugging
- labels: ['updating-values-from-instance-specification']

### NORMALIZED CONTENT

53678191

53678193

53678192

When an object acquires the properties of another, there is an inheritance relationship between them. The object that inherits the properties is called Subtype or Subclass (child) and the inheriting object is called Supertype or Class (parent). This inheritance relationship allows the child and the parent to have identical properties. If the property has a value, the Subclass will also inherits the value. Magic Model Analyst / Cameo Simulation Toolkit allows you to change the default value of an object or a Subtype whose property is defined in the Supertype or a read-only property. You can override this existing value in the subtype without changing the default value of the property of the Supertype by creating a redefine property of the subtype that represents the default values. The value of the property can be integer, real, or string.

When you change the inherited value in the subtype, e.g., from 2 to 3, in the **Variables** pane, the simulation will initiate at 3.

This example uses the model depicted in to show you how to update default values to an inherited and/or read-only property by creating redefined properties as follows

###### [IMAGE alt='' src=''] 
Inherited and read-only Properties of a Subtype.

To update default value(s) from an Instance Specification

1. Run a simulation on your model as follows [IMAGE alt='' src='']

2. A **Question** dialog will open asking if you want to redefine the values in the Subtype. Click **Yes**.

###### [IMAGE alt='' src='']

Magic Model Analyst / Cameo Simulation Toolkit will create new redefined properties for the ExternalSubSystem (i, r, and s), and save the default values (i = 0, r = 0.0000, and s = null) to the new properties.

###### [IMAGE alt='' src='']

3. On the **Variables** pane, change the default value of property i, r, and s of ExternalSubSystem.

###### [IMAGE alt='' src='']

4. Each time you finish updating the value, right-click the property in the **Variables** pane and select **Save To****Default Value(s)**.

###### [IMAGE alt='' src='']

If Magic Model Analyst / Cameo Simulation Toolkit cannot create redefined properties, a warning message will appear.

###### [IMAGE alt='' src='']

53678190

**Related page**

- [CONFLUENCE_PAGE title='Redefine' space='MT']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="4b31d74f-4ede-411d-8b34-43c2eb9431c3"><ac:parameter ac:name="id">53678191</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="7425009a-44bf-4058-80b1-faba76b4ea40"><ac:parameter ac:name="id">53678193</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="c4ad9f6a-9c7c-44c5-851a-ed724ac7cfad"><ac:parameter ac:name="id">53678192</ac:parameter><ac:rich-text-body><p>When an object acquires the properties of another, there is an inheritance relationship between them. The object that inherits the properties is called Subtype or Subclass (child) and the inheriting object is called Supertype or Class (parent). This inheritance relationship allows the child and the parent to have identical properties. If the property has a value, the Subclass will also inherits the value. Magic Model Analyst / Cameo Simulation Toolkit allows you to change the default value of an object or a Subtype whose property is defined in the Supertype or a read-only property. You can override this existing value in the subtype without changing the default value of the property of the Supertype by creating a redefine property of the subtype that represents the default values. The value of the property can be integer, real, or string. </p><p>When you change the inherited value in the subtype, e.g., from 2 to 3, in the <strong>Variables</strong> pane, the simulation will initiate at 3. </p><p>This example uses the model depicted in to show you how to update default values to an inherited and/or read-only property by creating redefined properties as follows</p><h6 style="text-align: center;"><ac:image ac:align="center" ac:title="Inherited and Read Only Properties of a Subtype" ac:alt="Inherited and Read Only Properties of a Subtype"><ri:attachment ri:filename="1_systemDefine.png" /></ac:image><br />Inherited and read-only Properties of a Subtype.</h6><p>To update default value(s) from an Instance Specification </p><hr /><ol><li><p>Run a simulation on your model as follows</p><h6><ac:image ac:title="Running a Model Simulation" ac:alt="Running a Model Simulation"><ri:attachment ri:filename="2.1.1_SaveTodefaultMenu.png" /></ac:image></h6></li></ol><p style="margin-left: 30.0px;">2. A <strong>Question</strong> dialog will open asking if you want to redefine the values in the Subtype. Click <strong>Yes</strong>. </p><h6 style="margin-left: 30.0px;"><ac:image ac:title="The Question Dialog" ac:alt="The Question Dialog"><ri:attachment ri:filename="3_RedefinePropertiesQuestion.png" /></ac:image></h6><p style="margin-left: 30.0px;">Magic Model Analyst / Cameo Simulation Toolkit will create new redefined properties for the ExternalSubSystem (i, r, and s), and save the default values (i = 0, r = 0.0000, and s = null) to the new properties.</p><h6 style="margin-left: 30.0px;"><ac:image ac:title="The Redefining Properties of a Subtype" ac:alt="The Redefining Properties of a Subtype"><ri:attachment ri:filename="4_SaveToDefaultValueResult.png" /></ac:image></h6><p style="margin-left: 30.0px;">3. On the <strong>Variables</strong> pane, change the default value of property i, r, and s of ExternalSubSystem.</p><h6 style="margin-left: 30.0px;"><ac:image ac:title="Updating Default Values in the Variables Pane" ac:alt="Updating Default Values in the Variables Pane"><ri:attachment ri:filename="updatesavedefvalue.png" /></ac:image></h6><p style="margin-left: 30.0px;">4. Each time you finish updating the value, right-click the property in the <strong>Variables</strong> pane and select <strong>Save To</strong><strong>Default Value(s)</strong>.</p><h6 style="margin-left: 30.0px;"><ac:image ac:title="Saving the Updated Default Value in the Variables Pane" ac:alt="Saving the Updated Default Value in the Variables Pane"><ri:attachment ri:filename="updatesavedefvalue2.png" /></ac:image></h6><p style="margin-left: 30.0px;">If Magic Model Analyst / Cameo Simulation Toolkit cannot create redefined properties, a warning message will appear.</p><h6 style="margin-left: 30.0px;"><ac:image ac:title="A Warning Message" ac:alt="A Warning Message"><ri:attachment ri:filename="110174_SaveToDafaultWarning.png" /></ac:image></h6></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="138028e4-6b4d-49c5-ab42-ce69fc8c8d8c"><ac:parameter ac:name="id">53678190</ac:parameter><ac:rich-text-body><p><strong>Related page</strong></p><ul><li><ac:link><ri:page ri:space-key="MT" ri:content-title="Redefine" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=249571086 space=MMA version=1 -->
## PAGE 00753: Updating fUML runtime value with value from a spreadsheet

- page_id: `249571086`
- space_key: `MMA`
- source_url: https://docs.nomagic.com/spaces/MMA/pages/249571086/Updating+fUML+runtime+value+with+value+from+a+spreadsheet
- version_number: 1
- version_date: `2022-09-08T09:30:03.072+02:00`
- ancestors: Magic Model Analyst / Cameo Simulation Toolkit Documentation > User Guide > Action languages > Action scripts APIs > Excel Helper APIs
- labels: []

### NORMALIZED CONTENT

You can assign a value from a specific row in a spreadsheet in an Excel file to an fUML runtime value by using the following API

```text

```

The APIs can ignore the sheetName and use the first sheet of the selected spreadsheet instead.

```text

```

The mappingElement parameter can be String or Element for represent the mapping Class name or mapping Class Element. The APIs can ignore the mappingElement then update the runtime object of the file schema element that is matched with file name.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>You can assign a value from a specific row in a spreadsheet in an Excel file to an fUML runtime value by using the following API <br class="atl-forced-newline" /><span style="color: rgb(127,0,85);"> </span></p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="60ee8308-40e8-481f-85c5-894133b73679"><ac:parameter ac:name="language">text</ac:parameter><ac:plain-text-body><![CDATA[public void updatefUMLValueFromSpreadSheet(StructuredValue value, String fileName, String sheetName, Number rowIndex, Object mappingElement) {
...
}]]></ac:plain-text-body></ac:structured-macro><p><br /></p><p>The APIs can ignore the sheetName and use the first sheet of the selected spreadsheet instead. <br class="atl-forced-newline" /><span style="color: rgb(127,0,85);"> </span></p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="50453455-2687-4cd9-ac9e-0dfd944719dc"><ac:parameter ac:name="language">text</ac:parameter><ac:plain-text-body><![CDATA[public void updatefUMLValueFromSpreadSheet(StructuredValue value, String fileName, Number rowIndex, Object mappingElement) {
...
}]]></ac:plain-text-body></ac:structured-macro><p>The mappingElement parameter can be String or Element for represent the mapping Class name or mapping Class Element. The APIs can ignore the mappingElement then update the runtime object of the file schema element that is matched with file name.</p>
````

<!--NOMAGIC_PAGE id=249570672 space=MMA version=3 -->
## PAGE 00754: Use Case simulation

- page_id: `249570672`
- space_key: `MMA`
- source_url: https://docs.nomagic.com/spaces/MMA/pages/249570672/Use+Case+simulation
- version_number: 3
- version_date: `2025-09-12T15:08:38.241+02:00`
- ancestors: Magic Model Analyst / Cameo Simulation Toolkit Documentation > User Guide
- labels: ['use-case-simulation']

### NORMALIZED CONTENT

You can use Magic Model Analyst / Cameo Simulation Toolkit to simulate a Use Case model or diagram. This section illustrates the steps to simulate the Use Case model.

To simulate a use case model

1. Create a use case diagram. See the following example of a Use Case diagram. The figure shows the Use Case diagram in a block (a subject can be either a block or a class). [IMAGE alt='' src='']
2. Either right-click the Use Case diagram in the Containment tree and select **Simulation** > **Run** or click [IMAGE alt='' src=''] on the diagram toolbar to run the model. The classifier behaviors in the Use Case diagram are run during simulation. Magic Model Analyst / Cameo Simulation Toolkit creates a window to represent each Actor in the diagram (the preceding figure shows four actors: Worker1, Worker2, Worker3, and Worker4.
3. You can click the button, which represents what Use Case the Actor can perform, in each window to simulate it (the following figure shows the buttons **Change Color** and **Paint**). NoteThe Block connected by the Association with a Use Case is shown as an Actor, e.g. Worker3, so any Use Cases connected are shown as buttons in the GUI window of the Actor. Also, the image of the Block is shown according to the selected **Image** above the list of Use Case buttons. The following figure shows the Actor's name and title, and the buttons (**Change Color**, **Paint**) representing the Use Cases the actors can perform. Once you click the button, Magic Model Analyst / Cameo Simulation Toolkit uses the subject (Worker1, Worker2, Worker3, and Worker4) as the context to access the Classifier Behaviors of the Use Case diagram or read the values of the properties. If the Use Case has no subject, Magic Model Analyst / Cameo Simulation Toolkit will run the Classifier Behavior of the Use Case. You can change the values of the properties in the **Variables** pane. You can import an image to represent an Actor through the Actor [CONFLUENCE_PAGE title='Specification window' space='MT']. [IMAGE alt='' src=''] Actions associated with actors within a Use Case diagram.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>You can use Magic Model Analyst / Cameo Simulation Toolkit to simulate a Use Case model or diagram. This section illustrates the steps to simulate the Use Case model.</p><p><br /></p><p>To simulate a use case model</p><hr /><ol><li><p><span style="color: rgb(112,112,112);"><span style="color: rgb(0,0,0);">Create a use case diagram. See the following example of a Use Case diagram. The figure shows the Use Case diagram in a block (a subject can be either a block or a class). </span><br /></span></p><p><ac:image><ri:attachment ri:filename="UseCase.png" /></ac:image></p><p><br /></p></li><li><span style="line-height: 1.42857;">Either </span><span style="line-height: 1.42857;">right-click the Use Case diagram in the Containment tree and select <strong>Simulation</strong> &gt; <strong>Run</strong> or </span><span style="line-height: 1.42857;">click <ac:image><ri:attachment ri:filename="run button.png" /></ac:image> on the diagram toolbar to run the model. The classifier behaviors in the Use Case diagram are run during simulation. Magic Model Analyst / Cameo Simulation Toolkit creates a window to represent each Actor in the diagram (the preceding figure shows four actors: Worker1, Worker2, <ac:inline-comment-marker ac:ref="71c263ca-c6c5-4eb8-a98c-9de23516b540">Worker3</ac:inline-comment-marker>, and Worker4.</span></li><li><p><span style="line-height: 1.42857;">You can click the button, which represents what Use Case the Actor can perform, in each window to simulate it (the following figure shows the buttons <strong>Change Color</strong> and <strong>Paint</strong>).</span></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="7cf85f04-c61d-4c84-ad93-28bb900a5496"><ac:parameter ac:name="title">Note</ac:parameter><ac:rich-text-body><p>The Block connected by the Association with a Use Case is shown as an Actor, e.g. Worker3, so any Use Cases connected are shown as buttons in the GUI window of the Actor. Also, the image of the Block is shown according to the selected <strong>Image</strong> above the list of Use Case buttons.</p></ac:rich-text-body></ac:structured-macro><p><span style="line-height: 1.42857;"><br /></span></p><p>The following figure shows the Actor's name and title, and the buttons (<strong>Change Color</strong>, <strong>Paint</strong>) representing the Use Cases the actors can perform. Once you click the button, Magic Model Analyst / Cameo Simulation Toolkit uses the subject (Worker1, Worker2, Worker3, and Worker4) as the context to access the Classifier Behaviors of the Use Case diagram or read the values of the properties. If the Use Case has no subject, Magic Model Analyst / Cameo Simulation Toolkit will run the Classifier Behavior of the Use Case. You can change the values of the properties in the <strong>Variables</strong> pane. You can import an image to represent an Actor through the Actor <ac:link><ri:page ri:space-key="MT" ri:content-title="Specification window" /><ac:plain-text-link-body><![CDATA[Specification window]]></ac:plain-text-link-body></ac:link>.</p><p><span style="line-height: 1.42857;"><ac:image><ri:attachment ri:filename="UseCase_withActions.png" /></ac:image></span><span style="line-height: 1.42857;"><br /></span></p><h6><span style="line-height: 1.42857;"><span style="color: rgb(112,112,112);">Actions associated with actors within a Use Case diagram.</span></span></h6></li></ol><p> </p>
````

<!--NOMAGIC_PAGE id=249569546 space=MMA version=2 -->
## PAGE 00755: User Guide

- page_id: `249569546`
- space_key: `MMA`
- source_url: https://docs.nomagic.com/spaces/MMA/pages/249569546/User+Guide
- version_number: 2
- version_date: `2025-08-19T14:56:04.728+02:00`
- ancestors: Magic Model Analyst / Cameo Simulation Toolkit Documentation
- labels: ['user-guide']

### NORMALIZED CONTENT

**Welcome!** This user guide will walk you through the basics of using Magic Model Analyst / Cameo Simulation Toolkit.

Use the search box to find a specific topic or select one from the list below:

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Welcome!</strong> This user guide will walk you through the basics of using Magic Model Analyst / Cameo Simulation Toolkit.</p><p>Use the search box to find a specific topic or select one from the list below<span class="confluence-link">:</span></p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="f78f0a5d-7918-4a2d-a4f6-69e777fae41a" /></p>
````

<!--NOMAGIC_PAGE id=249570346 space=MMA version=1 -->
## PAGE 00756: Using Guards on Transitions

- page_id: `249570346`
- space_key: `MMA`
- source_url: https://docs.nomagic.com/spaces/MMA/pages/249570346/Using+Guards+on+Transitions
- version_number: 1
- version_date: `2020-12-29T08:31:48.294+01:00`
- ancestors: Magic Model Analyst / Cameo Simulation Toolkit Documentation > User Guide > State Machine simulation > Adapting models for State Machine simulation
- labels: ['guards-on-transitions']

### NORMALIZED CONTENT

#### CONTENT-LAYER: Note

117029420

#### CONTENT-COLUMN: Note

117029422

#### CONTENT-BLOCK: Note

117029421

You can specify Guard conditions on Transitions using any action language. Open the *SmallTestSamples.mdzip* to see an example of how to specify Guards on Transitions.

You can use the properties of a context Classifier (the Classifier that is the context of a State Machine diagram) in Guard expressions as variable names. The real values of the variables will be resolved at runtime. In the example in *SmallTestSamples.mdzip*, the values come from the slots of the instance of the context Classifier (see the Instance diagram in the sample project).

###### [IMAGE alt='' src=''] 
The Test_guard diagram sample.

During the simulation, any Guard that is not Boolean expression evaluation (the*state 2 or state 3* body of the Guard in this case) will show the **Question** dialog box displaying the body of the Guard as shown in the figure below. You can click **Yes** to set the evaluation result **true** with the Transition according to the Path or **No** to set the evaluation result **false** without the Transition.

[IMAGE alt='' src='']

###### The Question dialog box appears for any Guard not Boolean expression evaluation during the simulation.

#### NOTE: Note

Note

If you use a Choice with Transitions, the name of the Choice will be also shown in the **Question** dialog box with the body of the Guard.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="1d2eaf0b-c538-499b-8d70-eb436c9df431"><ac:parameter ac:name="id">117029420</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="efbe52f4-8d04-4fbf-b856-44fec08e7508"><ac:parameter ac:name="id">117029422</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="49be1025-8222-46be-81ae-1313e1496039"><ac:parameter ac:name="id">117029421</ac:parameter><ac:rich-text-body><p>You can specify Guard conditions on Transitions using any action language. Open the <em>SmallTestSamples.mdzip</em> to see an example of how to specify Guards on Transitions. </p><p>You can use the properties of a context Classifier (the Classifier that is the context of a State Machine diagram) in Guard expressions as variable names. The real values of the variables will be resolved at runtime. In the example in <em>SmallTestSamples.mdzip</em>, the values come from the slots of the instance of the context Classifier (see the Instance diagram in the sample project). </p><p><br /></p><h6 style="text-align: center;"><ac:image ac:align="center" ac:title="Test_guard Example" ac:alt="Test_guard Example"><ri:attachment ri:filename="Figure_0038.png" /></ac:image><br />The Test_guard diagram sample.</h6><p>During the simulation, any Guard that is not Boolean expression evaluation (the<em> state 2 or state 3</em> body of the Guard in this case) will show the <strong>Question</strong> dialog box displaying the body of the Guard as shown in the figure below. You can click <strong>Yes</strong> to set the evaluation result <strong>true</strong> with the Transition according to the Path or <strong>No</strong> to set the evaluation result <strong>false</strong> without the Transition.</p><p style="text-align: center;"><ac:image ac:align="center"><ri:attachment ri:filename="Question Dialog for Evaluation Result.PNG" /></ac:image></p><h6 style="text-align: center;">The Question dialog box appears for any Guard not Boolean expression evaluation during the simulation.</h6><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="b103c6a4-12b7-4e65-bc74-686d73f4cc57"><ac:parameter ac:name="title">Note</ac:parameter><ac:rich-text-body><p>If you use a Choice with Transitions, the name of the Choice will be also shown in the <strong>Question</strong> dialog box with the body of the Guard.</p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=249571478 space=MMA version=10 -->
## PAGE 00757: Using simulation command line and showing test results through Jenkins

- page_id: `249571478`
- space_key: `MMA`
- source_url: https://docs.nomagic.com/spaces/MMA/pages/249571478/Using+simulation+command+line+and+showing+test+results+through+Jenkins
- version_number: 10
- version_date: `2025-09-15T14:13:51.399+02:00`
- ancestors: Magic Model Analyst / Cameo Simulation Toolkit Documentation > Tutorial
- labels: []

### NORMALIZED CONTENT

#### NOTE: Note

Note

In these scenarios, all related items on this page to be used are in the [ATTACHMENT filename='TestSimulationCommandLine.zip'] sample.

Preparing a simulation project and Configs in MagicDraw

To prepare a simulation project and Configs in MagicDraw

1. Create a simulation model with Behaviors, e.g., TestVerdictKind.mdzip .
2. Apply «TestCase» to the Behaviors so the pass/fail status will be returned to the VerdictKind Activity parameters.
3. Create Simulation Configs and set those Behaviors as **executionTarget** of those Simulation Configs. NoteAll required resources must be available for the Simulation Configs, e.g., loadCSV and fmu. All features preventing simulation from the start/terminate, e.g., false autoStart, context without Classifier Behavior, chart windows at the end of execution, or output parameters at the end of execution (running Activity) will also be automatically started/terminated.
4. Run each Simulation Config to verify that an expected result, either pass or fail, must be returned. [IMAGE alt='' src='']

##### Running a project through simulate command line

To run a project through simulate command line

1. Run the command line console, e.g., cmd on Windows.
2. In the console, type any commands to go to the local installation of MagicDraw.
3. Go to the plugins\com.nomagic.magicdraw.simulation folder.
4. Use the following syntax: *simulate -project “[Path of an MDZIP project]” -config “[Config]”*. 
 
In this case, the following commands are used: text
5. At the last line of the command prompt, **pass** or **fail**appears. You can also see the details of execution through the [Simulation Log File](https://docs.nomagic.com/display/MMA/Simulation+log+file). [IMAGE alt='' src='']

##### Creating a JUnit test case and configuration file

To create a JUnit test case and configuration file

1. Include the JUnit library in the Java project by creating a new Java project and adding the JUnit 4 library in current location using the Eclipse's JUnit.
2. Create a new JUnit test case, e.g., .
3. Compile the test case and create a JAR file, e.g., TestSimulationCommandLine.JAR from the test case.
4. Create properties file, e.g., TestGeneratePassResult.properties and TestGenerateFailResult.properties .
5. Create an , e.g., run_junit.xml .

##### Configuring Jenkins for the Automated testing

To configure Jenkins for the Automated testing

1. Create a new Jenkins project.
2. Specify a Project Name , e.g., Test Simulation Command Line .
3. Go to Advanced Project Options , click Advanced , and select Use custom workspace . [ATTACHMENT filename='2018-09-21 15_48_04-Window.png']
4. In the Directory box, specify a path to the directory that contains run_junit.xml .
5. Go to Build and click Add build step . Select Invoke Ant .
6. In the Targets box, type build . [ATTACHMENT filename='2018-09-21 15_55_55-Window.png']
7. Select Advanced . In the Build File box, type run_junit.xml .
8. In the **Properties** box, specify *md.root=[MagicDraw installation directory]*and *properties.files.dir=[Path containing the properties files]*, as shown in the example above. TipThe path containing the property files can be either an absolute (full) path, e.g., *C:\Users\User\Desktop\TestSimulationCommandLine\tests* or relative path, e.g., *tests*.
9. Go to Post-build Actions and click Add post-build action . Select Publish JUnit test result report .
10. In the Test report XMLs box, specify a path to JUnit XML files, e.g., test-reports/**TEST*.xml . [ATTACHMENT filename='2018-09-21 15_39_46-Window.png']
11. Run the build. Test Result will be shown and allows you to view more details for those test cases. [IMAGE alt='' src='']

##### Simulate command arguments and parameters

Examples of the **simulate** command lines are as follows:

- On Windows: simulate.bat -project "../../samples/simulation/HingeMonteCarloAnalysis.mdzip" -config "Monte Carlo Analysis"
- On Mac OS: sh simulate.sh -project "../../samples/simulation/HingeMonteCarloAnalysis.mdzip" -config "Monte Carlo Analysis"

| Type of argument | Parameter | Description |
| --- | --- | --- |
| Mandatory arguments | -project | Specify the file name with the path to the project. Both relative and absolute paths are supported. |
| -config | Specify the Simulation Configuration without a qualified name to run.NoteIf there are multiple Simulation Configurations with the same name (e.g., in different Packages), a warning message will be displayed in the Simulation log, and the first Simulation Configuration will be used. |  |
| -properties propertiesFileName | Specify the name of the properties file to use, e.g., in the TestSimulationCommandLine.zip sample.NoteIf the -properties option is specified, the argument is the name of a properties file, and the mandatory argument is no longer required.A properties file contains -project and -config, along with the specified data of each parameter. |  |
| Optional arguments | -inputs elementNameListWithValue | Specify one or more properties with values that will be provided to the Simulation Configuration. |
| -inputsFile propertiesFileName | Specify the name of the properties file containing the parameters with values that will be provided to the Simulation Configuration.NoteIf you provide both -inputs and -inputFile arguments, parameters are collected from both arguments. |  |
| -outputs elementNameList | Specify one or more properties whose values should be obtained during the simulation. |  |
| -outputsTemplate propertiesFileName | Specify the properties file that contains the parameters whose values should be obtained during the simulation.NoteIf you provide both -outputs and -outputTemplate arguments, parameters are collected from both arguments. |  |
| -outputsFile propertiesFileName | Specify the properties file which will contain the output parameters with values after the simulation. The specified file will contain the parameters provided in the -outputTemplate and/or -outputs argument. |  |
| -element | Specify the qualified name or element ID of the element to be executed. |  |
| Optional (server) arguments | -server | Specify the name or IP address (and port) of the server. |
| -leaveprojectopen | Set to true to leave the project open per property file after simulating the project in a series of project simulations. The default value is false. |  |
| -login | Specify the login name to log in to the server. |  |
| -password | Specify the password to log in to the server. |  |
| -spassword | Specify the encrypted password to log in on to the server.NoteTo generate an encrypted password for this option, use the following command line (the characters of the encrypted password will be returned, e.g., 49034c0439….):generate -generatepassword “Administrator” |  |
| -ssl | Set to true to use and enable Secured Connection (SSL). The default value is false. |  |
| -pversion | Specify the version of the server project. |  |
| -tag | Specify the tag name of the server project.Note-tag can't be used with -pversion.If multiple projects are returned, only the latest version will be run. |  |
| -readonly | Set to true (the default value) to open the project as historical in the latest version without specifying -pversion.Specify other values to open the latest version normally. |  |
| Teamwork Cloud arguments | -branch | Specify the branch of the Teamwork Cloud project.Note-branch and -pversion cannot be specified in the same command.If -pversion and -tag are not specified, the latest version of the specified branch will be returned. |
| -updatemodule | Set to true to update used projects. The default value is false.Setting this argument to true will update only those project usages that have enabled notifications for Any New Version. |  |
| -projectpassword | Specify the project password. |  |

##### Simulate command arguments with projects in Teamwork Cloud

To use simulate command arguments with projects in [Teamwork Cloud](https://docs.nomagic.com/CM/?contextKey=using-teamwork-cloud&version=latest), the projects must be added to Teamwork Cloud. The following examples demonstrate how to use the simulate command to run a model from Teamwork Cloud.

| Scenario | Command argument |
| --- | --- |
| Simulate a project with an encrypted password and enable a secured connection (-spassword, -ssl). | simulate -project "HingeMonteCarloAnalysis" -config "Monte Carlo Analysis" -servertype "twcloud" -server "localhost:1234" -login "Administrator" -spassword "49034c0439…" -ssl "true" |
| Simulate a project by specifying a project version and project password (-pversion, -projectpassword). | simulate -project "HingeMonteCarloAnalysis" -config "Monte Carlo Analysis" -servertype "twcloud" -server "localhost" -login "Administrator" -password "Administrator" -pversion "5" -projectpassword "Administrator" |
| Simulate a project by specifying a tag name and branch (-tag, -branch).NoteIf there are any duplicated tags in the branch, the latest version will be run. | simulate -project "HingeMonteCarloAnalysis" -config "Monte Carlo Analysis" -servertype "twcloud" -server "localhost" -login "Administrator" -spassword "49034c0439…" -tag "duplicatedTag" -branch "19.0 SP2" |
| Simulate a command with three property files having different parameters. See . | simulate -properties "D:\\Simulation\\Project-Config1.properties" "D:\\Simulation\\Project-Config2.properties" "D:\\Simulation\\Project-Config3.properties" |
| Simulate a project in Teamwork Server by specifying a project version (-pversion). | simulate -project "HingeMonteCarloAnalysis" -config "Monte Carlo Analysis" -servertype "tw" -server "localhost" -login "Administrator" -password "Administrator" -pversion "2" |
| Simulate a project in Teamwork Server by specifying an encrypted password and tag name (-spassword, -tag). | simulate -project "HingeMonteCarloAnalysis" -config "Monte Carlo Analysis" -servertype "tw" -server "localhost" -login "Administrator" -spassword "49034c0439…" -tag "run2000" |
| Simulate multiple projects in a single command with better performance (-leaveprojectopen).TipWhen large-size projects need to be loaded and closed for many property files, it takes longer time to simulate projects. In this case, you can use -leaveprojectopen as an option to reduce memory for loading each project. | simulate -leaveprojectopen true -properties "Properties1_Undefined.properties" "Properties2_Undefined.properties" "Properties3_Undefined.properties" |
| Simulate a project in Teamwork Cloud while specifying several input parameters that will be provided for the Simulation Configuration (-inputs). | simulate -project "SpacecraftMassRollup" -config "spacecraft mass analysis" -inputs telecom.amplifier.me=8 telecom.antenna.me=29 -outputsFile “SimResults” -servertype "twcloud" -server "localhost” -login “Administrator" -spassword "49034c0439…" |
| Simulate a project in Teamwork Cloud while specifying the properties file that will be provided to the Simulation Configuration (-inputsFile), the properties file containing the parameters whose values should be obtained (-outputsTemplate), and the properties file that will contain output parameters with their values after the simulation (-outputsFile). | simulate -project "SpacecraftMassRollup" -config "spacecraft mass analysis" -inputsFile “D:\\Simulation\\InputsParams.properties” -outputsTemplate “D:\\Simulation\\OutputParams.properties” -outputsFile "D:\\Simulation\\SimResults.properties" -servertype "twcloud" -server "localhost” -login “Administrator" -spassword "49034c0439…" |

##### Property file sampleProperty file sample: Project-Config1.properties

```text

```

##### JUnit test sampleJUnit test sample: TestSimulationCommandLine.java

```text
not found.");
			} else {
				absPropPath = path.toAbsolutePath().toString();
			}
		}
		String cmd = propFilePath == null || propFilePath.isEmpty() ? SIMULATION_COMMAND_LINE : SIMULATION_COMMAND_LINE + " -properties \"" + absPropPath + "\"";
        return execute(cmd);
	}
}]]>
```

##### Ant configuration file sampleAnt configuration file sample: run_junit.xml

```text
]]>
```

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="04101a36-5f99-4101-a494-182f8798bcc5"><ac:parameter ac:name="title">Note</ac:parameter><ac:rich-text-body><p>In these scenarios, all related items on this page to be used are in the <ac:link><ri:attachment ri:filename="TestSimulationCommandLine.zip" /></ac:link> sample.</p></ac:rich-text-body></ac:structured-macro><p><span style="font-size: 16.0px;font-weight: bold;letter-spacing: -0.006em;">Preparing a simulation project and Configs in MagicDraw</span></p><p>To prepare a simulation project and Configs in MagicDraw</p><hr /><ol><li>Create a simulation model with Behaviors, e.g., <em>TestVerdictKind.mdzip</em>.</li><li>Apply «TestCase» to the Behaviors so the pass/fail status will be returned to the VerdictKind Activity parameters.</li><li><p class="auto-cursor-target">Create Simulation Configs and set those Behaviors as <strong>executionTarget</strong> of those Simulation Configs.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="cdf69c7b-3a62-4163-8aa7-600421838100"><ac:parameter ac:name="title">Note</ac:parameter><ac:rich-text-body><p>All required resources must be available for the Simulation Configs, e.g., loadCSV and fmu. All features preventing simulation from the start/terminate, e.g., false autoStart, context without Classifier Behavior, chart windows at the end of execution, or output parameters at the end of execution (running Activity) will also be automatically started/terminated.</p></ac:rich-text-body></ac:structured-macro></li><li><p>Run each Simulation Config to verify that an expected result, either pass or fail, must be returned.</p><p><ac:image><ri:attachment ri:filename="8114-1.PNG" /></ac:image></p></li></ol><h3>Running a project through simulate command line</h3><p>To run a project through simulate command line</p><hr /><ol><li>Run the command line console, e.g., cmd on Windows.</li><li>In the console, type any commands to go to the local installation of MagicDraw.</li><li>Go to the <strong>plugins\com.nomagic.magicdraw.simulation</strong> folder.</li><li><p class="auto-cursor-target">Use the following <ac:link ac:anchor="Simulate command arguments and parameters"><ac:plain-text-link-body><![CDATA[simulate command ]]></ac:plain-text-link-body></ac:link>syntax: <em>simulate -project “[Path of an MDZIP project]” -config “[Config]”</em>.<br /><br />In this case, the following commands are used:</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="46aacd9a-a4c8-4f65-a21c-5f50d1e471ad"><ac:parameter ac:name="language">text</ac:parameter><ac:plain-text-body><![CDATA[simulate -project “D:\\Simulation\\API\\TestVerdictKind.mdzip” -config “Run GeneratePassResult”
simulate -project “D:\\Simulation\\API\\TestVerdictKind.mdzip” -config “Run GenerateFailResult”]]></ac:plain-text-body></ac:structured-macro></li><li><p>At the last line of the command prompt, <strong>pass</strong> or <strong>fail </strong>appears. You can also see the details of execution through the <a href="https://docs.nomagic.com/display/MMA/Simulation+log+file">Simulation Log File</a>.<br /><br /></p><p><ac:image><ri:attachment ri:filename="8114-2.PNG" /></ac:image></p></li></ol><h3>Creating a JUnit test case and configuration file</h3><p>To create a JUnit test case and configuration file</p><hr /><ol><li>Include the JUnit library in the Java project by creating a new Java project and adding the <strong>JUnit 4</strong> library in <strong>current location</strong> using the Eclipse's JUnit.</li><li>Create a new JUnit test case, e.g., <ac:link ac:anchor="JUnit test sample"><ac:plain-text-link-body><![CDATA[Test Simulation Command Line.java]]></ac:plain-text-link-body></ac:link>.</li><li>Compile the test case and create a JAR file, e.g., <strong>TestSimulationCommandLine.JAR</strong> from the test case.</li><li>Create properties file, e.g., <strong>TestGeneratePassResult.properties</strong> and <strong>TestGenerateFailResult.properties</strong>.</li><li class="confluence-link">Create an <ac:link ac:anchor="Ant configuration file sample"><ac:plain-text-link-body><![CDATA[Ant configuration file]]></ac:plain-text-link-body></ac:link>, e.g., <strong>run_junit.xml</strong>.</li></ol><h3 class="confluence-link">Configuring Jenkins for the Automated testing</h3><p>To configure Jenkins for the Automated testing</p><hr /><ol><li>Create a new Jenkins project.</li><li>Specify a <strong>Project Name</strong>, e.g., <em>Test Simulation Command Line</em>.</li><li>Go to <strong>Advanced Project Options</strong>, click <strong>Advanced</strong>, and select<strong> Use custom workspace</strong>.<br /><br /><ac:image><ri:attachment ri:filename="2018-09-21 15_48_04-Window.png" /></ac:image><br /><br /></li><li>In the <strong>Directory</strong> box, specify a path to the directory that contains <strong>run_junit.xml</strong>.</li><li>Go to <strong>Build </strong>and click <strong>Add build step</strong>. Select <strong>Invoke Ant</strong>.</li><li>In the <strong>Targets</strong> box, type <strong>build</strong>.<br /><br /><ac:image><ri:attachment ri:filename="2018-09-21 15_55_55-Window.png" /></ac:image><br /><br /></li><li>Select <strong>Advanced</strong>. In the <strong>Build File</strong> box, type <strong>run_junit.xml</strong>.</li><li><p class="auto-cursor-target">In the <strong>Properties</strong> box, specify <em>md.root=[MagicDraw installation directory] </em>and <em>properties.files.dir=[Path containing the properties files]</em>, as shown in the example above.</p><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="036c046a-8461-4541-a9e4-27e749469742"><ac:parameter ac:name="title">Tip</ac:parameter><ac:rich-text-body><p>The path containing the property files can be either an absolute (full) path, e.g., <em>C:\Users\User\Desktop\TestSimulationCommandLine\tests</em> or relative path, e.g., <em>tests</em>.</p></ac:rich-text-body></ac:structured-macro></li><li>Go to <strong>Post-build Actions</strong> and click <strong>Add post-build action</strong>. Select <strong>Publish JUnit test result report</strong>.</li><li>In the <strong>Test report XMLs</strong> box, specify a path to JUnit XML files, e.g., <em>test-reports/**TEST*.xml</em>.<br /><br /><ac:image><ri:attachment ri:filename="2018-09-21 15_39_46-Window.png" /></ac:image><br /><br /></li><li><p>Run the build. Test Result will be shown and allows you to view more details for those test cases.<br /><br /></p><p><ac:image><ri:attachment ri:filename="8114-4.PNG" /></ac:image></p></li></ol><h3>Simulate command arguments and parameters</h3><p>Examples of the <strong>simulate</strong> command lines are as follows:</p><ul><li>On Windows: <em>simulate.bat -project &quot;../../samples/simulation/HingeMonteCarloAnalysis.mdzip&quot; -config &quot;Monte Carlo Analysis&quot;</em></li><li>On Mac OS: <em>sh simulate.sh -project &quot;../../samples/simulation/HingeMonteCarloAnalysis.mdzip&quot; -config &quot;Monte Carlo Analysis&quot;</em></li></ul><table class="wrapped"><colgroup><col /><col /><col /></colgroup><tbody><tr><td><p>Type of argument<strong><br /></strong></p></td><td>Parameter</td><td><p>Description</p></td></tr><tr><td rowspan="3"><p><strong>Mandatory arguments</strong></p></td><td>-project</td><td><p>Specify the file name with the path to the project. Both relative and absolute paths are supported.</p></td></tr><tr><td>-config</td><td><div class="content-wrapper"><p>Specify the Simulation Configuration without a qualified name to run.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="c51705b5-07c6-4c95-b36b-81d7bc2a4883"><ac:parameter ac:name="title">Note</ac:parameter><ac:rich-text-body><p>If there are multiple Simulation Configurations with the same name (e.g., in different Packages), a warning message will be displayed in the Simulation log, and the first Simulation Configuration will be used.</p></ac:rich-text-body></ac:structured-macro></div></td></tr><tr><td>-properties propertiesFileName</td><td><div class="content-wrapper"><p class="auto-cursor-target">Specify the name of the properties file to use, e.g., in the <a class="external-link" href="https://docs.nomagic.com/download/attachments/33212749/TestSimulationCommandLine.zip?version=2&amp;modificationDate=1537518855106&amp;api=v2" rel="nofollow">TestSimulationCommandLine.zip</a> sample.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="4f3b695a-75c9-41d3-9d6e-0ac423a5a198"><ac:parameter ac:name="title">Note</ac:parameter><ac:rich-text-body><ul><li>If the <strong>-properties</strong> option is specified, the argument is the name of a properties file, and the mandatory argument is no longer required.</li><li>A properties file contains <strong>-project</strong> and <strong>-config</strong>, along with the specified data of each parameter.</li></ul></ac:rich-text-body></ac:structured-macro></div></td></tr><tr><td rowspan="6"><strong>Optional arguments</strong></td><td>-inputs elementNameListWithValue</td><td><div class="content-wrapper"><p class="auto-cursor-target">Specify one or more properties with values that will be provided to the Simulation Configuration.</p></div></td></tr><tr><td>-inputsFile propertiesFileName</td><td><div class="content-wrapper"><p><span>Specify the name of the properties file containing the parameters with values that will be provided to the Simulation Configuration.</span></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="dcafa05c-e4e8-49be-a52b-9026cccc6530"><ac:parameter ac:name="title">Note</ac:parameter><ac:rich-text-body>If you provide both <strong>-inputs</strong> and <strong>-inputFile</strong> arguments, parameters are collected from both arguments.</ac:rich-text-body></ac:structured-macro></div></td></tr><tr><td>-outputs elementNameList</td><td>Specify one or more properties whose values should be obtained during the simulation.</td></tr><tr><td><span>-outputsTemplate </span>propertiesFileName</td><td><div class="content-wrapper"><p class="auto-cursor-target"><span>Specify the properties file that contains the parameters whose values should be obtained during the simulation.</span></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="2a0fded6-d358-42d7-a253-a3bde0bcd692"><ac:parameter ac:name="title">Note</ac:parameter><ac:rich-text-body><p>If you provide both <strong>-outputs</strong> and <strong>-outputTemplate</strong> arguments, parameters are collected from both arguments.</p></ac:rich-text-body></ac:structured-macro></div></td></tr><tr><td>-outputsFile propertiesFileName</td><td><div class="content-wrapper"><p>Specify the properties file which will contain the output parameters with values after the simulation. The specified file will contain the parameters provided in the -<strong>outputTemplate</strong> and/or -<strong>outputs</strong> argument.</p></div></td></tr><tr><td>-element</td><td><div class="content-wrapper"><p><span style="color:var(--ds-text,#172b4d);">Specify the qualified name or element ID of the element to be executed.</span></p></div></td></tr><tr><td rowspan="9"><strong>Optional (server) arguments</strong><div class="content-wrapper"><p><br /></p></div></td><td>-server</td><td>Specify the name or IP address (and port) of the server.</td></tr><tr><td>-leaveprojectopen</td><td><p>Set to <em>true</em> to leave the project open per property file after simulating the project in a series of project simulations. The default value is <em>false</em>.</p></td></tr><tr><td>-login</td><td><p>Specify the login name to log in to the server.</p></td></tr><tr><td>-password</td><td><p>Specify the password to log in to the server.</p></td></tr><tr><td><div class="content-wrapper"><p>-spassword</p></div></td><td><div class="content-wrapper"><p>Specify the encrypted password to log in on to the server.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="95c8def1-bf7b-432b-bcdc-304d14368d27"><ac:parameter ac:name="title">Note</ac:parameter><ac:rich-text-body><p>To generate an encrypted password for this option, use the following command line (the characters of the encrypted password will be returned, e.g., <em>49034c0439</em>….):</p><strong>generate -generatepassword “Administrator”</strong></ac:rich-text-body></ac:structured-macro></div></td></tr><tr><td>-ssl</td><td><p>Set to <em>true</em> to use and enable Secured Connection (SSL). The default value is <em>false</em>.</p></td></tr><tr><td>-pversion</td><td><p>Specify the version of the server project.</p></td></tr><tr><td>-tag</td><td><div class="content-wrapper"><p>Specify the tag name of the server project.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="5224386c-8243-4270-a754-803c850ea5a3"><ac:parameter ac:name="title">Note</ac:parameter><ac:rich-text-body><ul><li><strong>-tag</strong> can't be used with <strong>-pversion</strong>.</li><li>If multiple projects are returned, only the latest version will be run.</li></ul></ac:rich-text-body></ac:structured-macro></div></td></tr><tr><td>-readonly</td><td><p>Set to <em>true</em> (the default value) to open the project as historical in the latest version without specifying <strong>-pversion</strong>.</p><p>Specify other values to open the latest version normally.</p></td></tr><tr><td rowspan="3"><p><strong>Teamwork Cloud arguments</strong></p><p><br /></p><p><br /></p></td><td>-branch</td><td><div class="content-wrapper"><p>Specify the branch of the Teamwork Cloud project.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="472a032d-bbf4-497a-8a42-d9d9c743563a"><ac:parameter ac:name="title">Note</ac:parameter><ac:rich-text-body><ul><li><strong>-branch</strong> and <strong>-pversion</strong> cannot be specified in the same command.</li><li>If <strong>-pversion</strong> and <strong>-tag</strong> are not specified, the latest version of the specified branch will be returned.</li></ul></ac:rich-text-body></ac:structured-macro></div></td></tr><tr><td>-updatemodule</td><td><div class="content-wrapper"><p>Set to <em>true</em> to update used projects. The default value is <em>false</em>.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="7752f059-57af-416a-b68c-3e9226e9f070"><ac:rich-text-body><p>Setting this argument to true will update only those project usages that have enabled <a href="https://docs.nomagic.com/CM/?contextKey=changing-used-project-versions&amp;version=latest">notifications for Any New Version</a>.</p></ac:rich-text-body></ac:structured-macro></div></td></tr><tr><td>-projectpassword</td><td><p>Specify the project password.</p></td></tr></tbody></table><h3 class="auto-cursor-target">Simulate command arguments with projects in Teamwork Cloud</h3><p>To use simulate command arguments with projects in <a href="https://docs.nomagic.com/CM/?contextKey=using-teamwork-cloud&amp;version=latest">Teamwork Cloud</a>, the projects must be added to Teamwork Cloud. The following examples demonstrate how to use the simulate command to run a model from Teamwork Cloud.</p><table class="relative-table wrapped" style="width: 99.9444%;"><colgroup><col style="width: 38.8393%;" /><col style="width: 61.1922%;" /></colgroup><tbody><tr><td>Scenario</td><td>Command argument</td></tr><tr><td>Simulate a project with an encrypted password and enable a secured connection (<em>-spassword, -ssl</em>).</td><td><em>simulate -project &quot;HingeMonteCarloAnalysis&quot; -config &quot;Monte Carlo Analysis&quot; -servertype &quot;twcloud&quot; -server &quot;localhost:1234&quot; -login &quot;Administrator&quot; -spassword &quot;49034c0439…&quot; -ssl &quot;true&quot;</em></td></tr><tr><td><div class="content-wrapper">Simulate a project by specifying a project version and project password (<em>-pversion, -projectpassword</em>).</div></td><td><em>simulate -project &quot;HingeMonteCarloAnalysis&quot; -config &quot;Monte Carlo Analysis&quot; -servertype &quot;twcloud&quot; -server &quot;localhost&quot; -login &quot;Administrator&quot; -password &quot;Administrator&quot; -pversion &quot;5&quot; -projectpassword &quot;Administrator&quot;</em></td></tr><tr><td><div class="content-wrapper"><p>Simulate a project by specifying a tag name and branch (<em>-tag, -branch</em>).</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="bf421104-27bf-439c-a63b-a575f60421bf"><ac:parameter ac:name="title">Note</ac:parameter><ac:rich-text-body><p>If there are any duplicated tags in the branch, the latest version will be run.</p></ac:rich-text-body></ac:structured-macro></div></td><td><em>simulate -project &quot;HingeMonteCarloAnalysis&quot; -config &quot;Monte Carlo Analysis&quot; -servertype &quot;twcloud&quot; -server &quot;localhost&quot; -login &quot;Administrator&quot; -spassword &quot;49034c0439…&quot; -tag &quot;duplicatedTag&quot; -branch &quot;19.0 SP2&quot;</em></td></tr><tr><td><div class="content-wrapper"><p>Simulate a command with three property files having different parameters. See <ac:link ac:anchor="Property file sample"><ac:plain-text-link-body><![CDATA[Property file sample: Project-Config1.properties]]></ac:plain-text-link-body></ac:link>.</p></div></td><td><em>simulate -properties &quot;D:\\Simulation\\Project-Config1.properties&quot; &quot;D:\\Simulation\\Project-Config2.properties&quot; &quot;D:\\Simulation\\Project-Config3.properties&quot;</em></td></tr><tr><td>Simulate a project in Teamwork Server by specifying a project version (<em>-pversion</em>).</td><td><em>simulate -project &quot;HingeMonteCarloAnalysis&quot; -config &quot;Monte Carlo Analysis&quot; -servertype &quot;tw&quot; -server &quot;localhost&quot; -login &quot;Administrator&quot; -password &quot;Administrator&quot; -pversion &quot;2&quot; <br /></em></td></tr><tr><td>Simulate a project in Teamwork Server by specifying an encrypted password and tag name (<em>-spassword, -tag</em>).</td><td><em>simulate -project &quot;HingeMonteCarloAnalysis&quot; -config &quot;Monte Carlo Analysis&quot; -servertype &quot;tw&quot; -server &quot;localhost&quot; -login &quot;Administrator&quot; -spassword &quot;49034c0439…&quot; -tag &quot;run2000&quot; <br /></em></td></tr><tr><td colspan="1"><div class="content-wrapper"><p>Simulate multiple projects in a single command with better performance (<em>-leaveprojectopen</em>).</p><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="9805cf76-c1ce-451d-8be2-bf793925083f"><ac:parameter ac:name="title">Tip</ac:parameter><ac:rich-text-body><p>When large-size projects need to be loaded and closed for many property files, it takes longer time to simulate projects. In this case, you can use <strong>-leaveprojectopen</strong> as an option to reduce memory for loading each project.</p></ac:rich-text-body></ac:structured-macro></div></td><td colspan="1"><em>simulate -leaveprojectopen true -properties &quot;Properties1_Undefined.properties&quot; &quot;Properties2_Undefined.properties&quot; &quot;Properties3_Undefined.properties&quot;</em></td></tr><tr><td colspan="1">Simulate a project in Teamwork Cloud while specifying several input parameters that will be provided for the Simulation Configuration (<span>-inputs</span>).</td><td colspan="1"><span style="color:var(--ds-text,#333333);">simulate -project &quot;SpacecraftMassRollup&quot; -config &quot;spacecraft mass analysis&quot; -inputs telecom.amplifier.me=8 telecom.antenna.me=29 -outputsFile “SimResults” -servertype &quot;twcloud&quot; -server &quot;localhost” -login “Administrator&quot; -spassword &quot;</span><em>49034c0439…</em><span style="color:var(--ds-text,#333333);">&quot;</span></td></tr><tr><td colspan="1">Simulate a project in Teamwork Cloud while specifying the properties file that will be provided to the Simulation Configuration (<span>-</span>inputsFile<span>), the properties file containing the parameters whose values should be obtained (-outputsTemplate), and the properties file that will contain output parameters with their values after the simulation (-outputsFile).</span></td><td colspan="1"><span style="color:var(--ds-text,#333333);">simulate -project &quot;SpacecraftMassRollup&quot; -config &quot;spacecraft mass analysis&quot; -inputsFile “</span>D:\\Simulation\\<span style="color:var(--ds-text,#333333);">InputsParams.properties” -outputsTemplate “</span>D:\\Simulation\\<span style="color:var(--ds-text,#333333);">OutputParams.properties”  -outputsFile &quot;</span>D:\\Simulation\\<span style="color:var(--ds-text,#333333);">SimResults.properties&quot; -servertype &quot;twcloud&quot; -server &quot;localhost” -login “Administrator&quot; -spassword &quot;</span><em>49034c0439…</em><span style="color:var(--ds-text,#333333);">&quot;</span></td></tr></tbody></table><h3><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="4ed3d50e-1b5d-48f4-8ac9-34b89c08999b"><ac:parameter ac:name="">Property file sample</ac:parameter></ac:structured-macro>Property file sample: Project-Config1.properties</h3><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="9149d338-80b2-4fea-ad75-43f36a0a68c1"><ac:parameter ac:name="language">text</ac:parameter><ac:plain-text-body><![CDATA[project=Project1
config=Config1
servertype=twcloud
server=localhost
login=Administrator
spassword=49034c0439d3d1acc8d212adc289670c6224af46f2ec597eea1f25071740d5615a82d82d4460d5b95747f1e369ed26cdb5bb70fe6f50ff095cf978f1743
e5fbae6c4f2eef98abbca482133e4ca045c3ce407134e9c42966d2f245aed349d39fecd6a49f67b5019d5668e09cfd7f10a9363c5657a01addb9829052ffc26c49364]]></ac:plain-text-body></ac:structured-macro><h3><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="0a99484f-d5d1-497b-99b7-cb4698e1cd7e"><ac:parameter ac:name="">JUnit test sample</ac:parameter></ac:structured-macro>JUnit test sample: TestSimulationCommandLine.java</h3><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="271741dc-0f65-4cbd-85d0-bf9aee72108e"><ac:parameter ac:name="language">text</ac:parameter><ac:plain-text-body><![CDATA[package com.nomagic.magicdraw.simulation;

import static org.junit.Assert.assertNotNull;
import static org.junit.Assert.assertTrue;
import static org.junit.Assert.fail;

import java.io.BufferedReader;
import java.io.File;
import java.io.IOException;
import java.io.InputStreamReader;
import java.nio.file.Files;
import java.nio.file.Path;

import org.junit.Before;
import org.junit.Test;

/**
 * A test class for running the simulation command line and checking for the pass/fail result.
 * @author Chanon S.
 */

public class TestSimulationCommandLine {
	private static final String MD_ROOT_PROPERTY = "md.root";
	private static final String PROPERTIES_FILES_PROPERTY = "properties.files.dir";
	private static final String MD_DIR = System.getProperty(MD_ROOT_PROPERTY);
	private static final String SIMULATION_COMMAND_LINE = MD_DIR + "/plugins/com.nomagic.magicdraw.simulation/simulate.sh";
	private static final String PROPERTIES_FILES_DIR = System.getProperty(PROPERTIES_FILES_PROPERTY);
	private static final String PASS_PROPERTIES = "TestGeneratePassResult.properties";
	private static final String FAIL_PROPERTIES = "TestGenerateFailResult.properties";
	private static final String SYSTEM_NEW_LINE = System.getProperty("line.separator");

	@Before
	public void assertBuildExist() {
		System.out.println(MD_ROOT_PROPERTY + "=" + MD_DIR);
		System.out.println(PROPERTIES_FILES_PROPERTY + "=" + PROPERTIES_FILES_DIR);

		assertNotNull(MD_ROOT_PROPERTY + " is not specified.", MD_DIR);
		assertNotNull(PROPERTIES_FILES_PROPERTY + " is not specified.", PROPERTIES_FILES_DIR);

		assertTrue("MagicDraw directory does not exist, MD_DIR=" + MD_DIR, new File(MD_DIR).exists());
		assertTrue("Properties files directory does not exist,PROPERTIES_FILES_DIR=" + PROPERTIES_FILES_DIR, new File(PROPERTIES_FILES_DIR).exists());
		assertTrue("Could not find simulate.sh file, SIMULATION_COMMAND_LINE=", new File(SIMULATION_COMMAND_LINE).exists());
	}

	@Test(timeout = 120000)
	public void testGeneratePassResult() {
		// This project and Simulation Config generate "pass" as the result of TestCase.
		String propertyFilePath = PROPERTIES_FILES_DIR + "/" + PASS_PROPERTIES;
		String consoleOutput = runWithProperties(propertyFilePath);
		System.out.println("Console output=" + consoleOutput);		
		boolean result = consoleOutput.contains(SYSTEM_NEW_LINE + "pass" + SYSTEM_NEW_LINE);
		assertTrue(consoleOutput, result);
	}

	@Test(timeout = 120000)
	public void testGenerateFailResult() {
		// This project and Simulation Config generate "fail" as the result of TestCase.
		String propertyFilePath = PROPERTIES_FILES_DIR + "/" + FAIL_PROPERTIES;
		String consoleOutput = runWithProperties(propertyFilePath);
		boolean result = consoleOutput.contains(SYSTEM_NEW_LINE + "pass" + SYSTEM_NEW_LINE);
		assertTrue(consoleOutput, result);
	}

	private String execute(String command) {
		System.out.println("Executing, command=" + command);

		StringBuilder result = new StringBuilder();
		try {
			Process p = Runtime.getRuntime().exec(command);
			BufferedReader input = new BufferedReader(new InputStreamReader(p.getInputStream()));
		
			String line;
			while ((line = input.readLine()) != null) {
				result.append(line);
				result.append(SYSTEM_NEW_LINE);
			}
		} catch (IOException e) {
			e.printStackTrace();
		}
		return result.toString();
	}

	private String runWithProperties(String propFilePath) {
		String absPropPath = propFilePath;
		if (propFilePath != null) {
			Path path = new File(propFilePath).toPath();
			if (!Files.exists(path)) {
				fail("Properties file <" + propFilePath + "> not found.");
			} else {
				absPropPath = path.toAbsolutePath().toString();
			}
		}
		String cmd = propFilePath == null || propFilePath.isEmpty() ? SIMULATION_COMMAND_LINE : SIMULATION_COMMAND_LINE + " -properties \"" + absPropPath + "\"";
        return execute(cmd);
	}
}]]></ac:plain-text-body></ac:structured-macro><h3><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="3461d703-4748-456e-9b7d-1227c3493a62"><ac:parameter ac:name="">Ant configuration file sample</ac:parameter></ac:structured-macro>Ant configuration file sample: run_junit.xml</h3><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="84943f6e-153f-4464-b66c-6ed91265fa61"><ac:parameter ac:name="language">text</ac:parameter><ac:plain-text-body><![CDATA[<project name="Run JUnit and Generate Reports" default="build" basedir=".">
	<target name="build" depends="set.properties, prepare, run.junit" />    
	<target name="set.properties">
		<property name="md.root" location="${md.root}" />
		<property name="properties.files.dir" location="${properties.files.dir}" />
		<property name="test.reports.dir" location="test-reports"/>
	</target>   
	<target name="prepare">
		<delete dir="${test.reports.dir}" />
		<mkdir dir="${test.reports.dir}" />
	</target>   
	<target name="run.junit">
		<junit printsummary="yes" fork="yes">
			<classpath>
				<pathelement location="lib/TestSimulationCommandLine.jar"/>
				<pathelement location="lib/junit-4.12.jar"/>
				<pathelement location="lib/hamcrest-core-1.3.jar"/>
			</classpath>
			<jvmarg value="-Xmx1200m" />
			<jvmarg value="-Xms256m" />
			<jvmarg value="-XX:PermSize=128M" />
			<jvmarg value="-XX:MaxPermSize=256M" />
			<jvmarg value="-XX:-UseSplitVerifier" />
			<jvmarg value="-noverify" />

			<sysproperty key="md.root" value="${md.root}" />
			<sysproperty key="properties.files.dir" value="${properties.files.dir}" />

			<batchtest todir="${test.reports.dir}">
				<zipfileset src="lib/TestSimulationCommandLine.jar">
					<include name="**/*.class"/>
				</zipfileset>
			</batchtest>
			<formatter type="xml" />
		</junit>
	</target>
</project>]]></ac:plain-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=249570525 space=MMA version=2 -->
## PAGE 00758: Using utility functions of Simulation

- page_id: `249570525`
- space_key: `MMA`
- source_url: https://docs.nomagic.com/spaces/MMA/pages/249570525/Using+utility+functions+of+Simulation
- version_number: 2
- version_date: `2025-09-12T15:08:46.737+02:00`
- ancestors: Magic Model Analyst / Cameo Simulation Toolkit Documentation > User Guide > Activity simulation
- labels: ['utility-functions']

### NORMALIZED CONTENT

Simulation provides some utility functions to facilitate common tasks, e.g., running command line and text file replacement. Those utility functions are encapsulated in Opaque Behaviors under **SimulationProfile::library::utils**as shown in the figure below.

#### NOTE: Note

Note

If the **SimulationProfile** package is not visible, click [IMAGE alt='' src=''] in the Containment tree pane and select **Show Auxiliary Resources**.

[IMAGE alt='' src='']

###### CommandLine, one of the utility functions of Simulation, is used through Opaque Behaviors in SimulationProfile::library::utils (shown in the circled area).

You can use those Opaque Behaviors by dragging them to the Activity diagram and setting parameters as described in the [CONFLUENCE_PAGE title='Opaque Behavior' space='MT'] section. Simulation also provides a few samples using the Activity diagram in the **utils** package. As displayed in the figure below, you can use **WindowsCommandLine** to open **Notepad** on Windows.

[IMAGE alt='' src='']

###### Using WindowsCommandLine to open Notepad on Windows.

From the following figure, you can use **TextFileReplace** to open the **build_me_a_HAB.ses** file and replace **$press_tunnel_len$** with **2.0**. See also the **UsingCommandLine.mdzip** built-in sample in **Simulation** on the **Welcome** page.

[IMAGE alt='' src='']

###### Using TextFileReplace to open the build_me_a_HAB.ses file and replace $press_tunnel_len$ with 2.0.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>Simulation provides some utility functions to facilitate common tasks, e.g., running command line and text file replacement. Those utility functions are encapsulated in Opaque Behaviors under <strong>SimulationProfile::library::utils </strong>as shown in the figure below.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="13350e42-5f75-43ff-944a-e711aba12385"><ac:parameter ac:name="title">Note</ac:parameter><ac:rich-text-body><p>If the <strong>SimulationProfile</strong> package is not visible, click <ac:image><ri:attachment ri:filename="Filter Icon.png" /></ac:image> in the Containment tree pane and select <strong>Show Auxiliary Resources</strong>.</p></ac:rich-text-body></ac:structured-macro><p><ac:image ac:align="center"><ri:attachment ri:filename="8716-1.PNG" /></ac:image></p><h6 style="text-align: center;">CommandLine, one of the utility functions of Simulation, is used through Opaque Behaviors in SimulationProfile::library::utils (shown in the circled area).</h6><p>You can use those Opaque Behaviors by dragging them to the Activity diagram and setting parameters as described in the <ac:link><ri:page ri:space-key="MT" ri:content-title="Opaque Behavior" /></ac:link> section. Simulation also provides a few samples using the Activity diagram in the <strong>utils</strong> package. As displayed in the figure below, you can use <strong>WindowsCommandLine</strong> to open <strong>Notepad</strong> on Windows.</p><p><ac:image ac:align="center"><ri:attachment ri:filename="8716-2.PNG" /></ac:image></p><h6 style="text-align: center;">Using WindowsCommandLine to open Notepad on Windows.</h6><p>From the following figure, you can use <strong>TextFileReplace</strong> to open the <strong>build_me_a_HAB.ses</strong> file and replace <strong>$press_tunnel_len$</strong> with <strong>2.0</strong>. See also the <strong>UsingCommandLine.mdzip</strong> built-in sample in <strong>Simulation</strong> on the <strong>Welcome</strong> page.</p><p><ac:image ac:align="center"><ri:attachment ri:filename="8716-3.PNG" /></ac:image></p><h6 style="text-align: center;">Using TextFileReplace to open the build_me_a_HAB.ses file and replace $press_tunnel_len$ with 2.0.</h6>
````

<!--NOMAGIC_PAGE id=249570330 space=MMA version=2 -->
## PAGE 00759: Validation and verification

- page_id: `249570330`
- space_key: `MMA`
- source_url: https://docs.nomagic.com/spaces/MMA/pages/249570330/Validation+and+verification
- version_number: 2
- version_date: `2025-08-19T14:56:10.888+02:00`
- ancestors: Magic Model Analyst / Cameo Simulation Toolkit Documentation > User Guide
- labels: ['validating-model']

### NORMALIZED CONTENT

55687136

55687138

55687137

INLINE

Before executing UML or SysML model, you need to make sure that it has been correctly modeled, or you can use the Magic Model Analyst / Cameo Simulation Toolkit's validation feature to help you validate the model against a set of validation rules before executing it.

To validate a model

1. From the main menu, click **Project**>**Options** to open the model validation option in the **[CONFLUENCE_PAGE title='Project options' space='']** dialog.
2. On the left pane, click General > Simulation .
3. In the Simulation Framework group, select the Check Model Before Execution option. [ATTACHMENT filename='Check Model Before Execution.png']
4. Click OK .
5. Simulate your model. A dialog will open, asking whether you want to load the required profiles that contain the validation rules to validate your model (if your project does not contain the required validation rules). [ATTACHMENT filename='question.png']
6. Click Yes to load the validation rules and validate the model before the simulation or No to simulate the model without validating it.

55687135

**Related page**

- [CONFLUENCE_PAGE title='Project options' space='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="b2467895-707a-46eb-befa-d302f67feb67"><ac:parameter ac:name="id">55687136</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="3d0084cd-98c6-4439-a3aa-66fd3caeea72"><ac:parameter ac:name="id">55687138</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="8bddd550-4853-437a-8612-48022fb1763e"><ac:parameter ac:name="id">55687137</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="excerpt" ac:schema-version="1" ac:macro-id="62402e3a-eaf1-41d2-93bc-c043662a37b5"><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><p>Before executing UML or SysML model, you need to make sure that it has been correctly modeled, or you can use the Magic Model Analyst / Cameo Simulation Toolkit's validation feature to help you validate the model against a set of validation rules before executing it. </p><p>To validate a model</p><hr /><ol><li><p>From the main menu, click <strong>Project </strong>&gt;<strong> Options</strong> to open the model validation option in the <strong><ac:link><ri:page ri:content-title="Project options" /><ac:plain-text-link-body><![CDATA[Project Options]]></ac:plain-text-link-body></ac:link></strong> dialog. </p></li><li>On the left pane, click <strong>General</strong> &gt; <strong>Simulation</strong>.</li><li>In the <strong>Simulation Framework</strong> group, select the <strong>Check Model</strong><strong> Before </strong><strong>Execution</strong> option.<br /><br /><ac:image><ri:attachment ri:filename="Check Model Before Execution.png" /></ac:image></li><li>Click <strong>OK</strong>.</li><li>Simulate your model. A dialog will open, asking whether you want to load the required profiles that contain the validation rules to validate your model (if your project does not contain the required validation rules).<br /><br /><ac:image ac:title="A Dialog Prompting the Validation Rules" ac:alt="A Dialog Prompting the Validation Rules"><ri:attachment ri:filename="question.png" /></ac:image></li><li>Click <strong>Yes</strong> to load the validation rules and validate the model before the simulation or <strong>No</strong> to simulate the model without validating it.</li></ol></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="bac42502-1870-4d14-88a2-f8d757b13deb"><ac:parameter ac:name="id">55687135</ac:parameter><ac:rich-text-body><p><strong>Related page</strong></p><ul><li><ac:link><ri:page ri:content-title="Project options" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=249571014 space=MMA version=4 -->
## PAGE 00760: Value access and references by tags

- page_id: `249571014`
- space_key: `MMA`
- source_url: https://docs.nomagic.com/spaces/MMA/pages/249571014/Value+access+and+references+by+tags
- version_number: 4
- version_date: `2025-09-15T17:58:41.918+02:00`
- ancestors: Magic Model Analyst / Cameo Simulation Toolkit Documentation > User Guide > Action languages
- labels: []

### NORMALIZED CONTENT

Magic Model Analyst / Cameo Simulation Toolkit supports accessing [CONFLUENCE_PAGE title='Tag' space='MED'] elements by names in script evaluated from that model element. All tags will be added as variables to that model element where the script is evaluated through an Opaque expression (default language). Other variables with the same name referred to by tags will be overwritten with the values of the Tags, e.g., the default value of a Distributed property can be initialized from calculating the *min* and *max* variables as shown in the figure below.

###### [IMAGE alt='' src='']Default values are calculated from the min and max tags as variables.

You can get any tag values by using names through console with the following command:

```text

```

You can also run the command without the runtime object even if no runtime object is provided, e.g., *ALH.getTagValue(String tagName)*, as shown in the following figure.

[IMAGE alt='' src='']

###### Running ALH.setValue() and ALH.getTagValue() without runtime objects.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>Magic Model Analyst / Cameo Simulation Toolkit supports accessing <ac:link><ri:page ri:space-key="MED" ri:content-title="Tag" /><ac:plain-text-link-body><![CDATA[tag]]></ac:plain-text-link-body></ac:link> elements by names in script evaluated from that model element. All tags will be added as variables to that model element where the script is evaluated through an Opaque expression (default language). Other variables with the same name referred to by tags will be overwritten with the values of the Tags, e.g., the default value of a Distributed property can be initialized from calculating the <em>min</em> and <em>max</em> variables as shown in the figure below.</p><p><br /></p><h6 style="text-align: center;"><ac:image ac:align="center"><ri:attachment ri:filename="Values from Min and Max Variables.PNG" /></ac:image>Default values are calculated from the min and max tags as variables.</h6><p class="Textbody">You can get any tag values by using names through console with the following command:</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="e499257a-4128-4c25-b9bd-a7d76ed92c55"><ac:plain-text-body><![CDATA[ALH.getTagValue(StructuredValue runtimeObject, String tagName)]]></ac:plain-text-body></ac:structured-macro><p><br /></p><p>You can also run the command without the runtime object even if no runtime object is provided, e.g., <em>ALH.getTagValue(String tagName)</em>, as shown in the following figure.</p><p><br /></p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="Running without Runtime Objects.PNG" /></ac:image></p><h6 style="text-align: center;">Running ALH.setValue() and ALH.getTagValue() without runtime objects.</h6>
````

<!--NOMAGIC_PAGE id=249570695 space=MMA version=2 -->
## PAGE 00761: Value binding

- page_id: `249570695`
- space_key: `MMA`
- source_url: https://docs.nomagic.com/spaces/MMA/pages/249570695/Value+binding
- version_number: 2
- version_date: `2026-04-13T12:34:17.774+02:00`
- ancestors: Magic Model Analyst / Cameo Simulation Toolkit Documentation > User Guide > Parametric evaluator
- labels: ['value-binding']

### NORMALIZED CONTENT

Value binding is the method to maintain values of properties, which are bound together, to be the same. The properties whose values are bound, must be connected together with a connector. The type of the properties which are bound together must be the same or one is a subtype of another. If the type of the properties is a primitive type, you can bind them with either a UML connector that does not have a type, or a SysML binding connector with a «BindingConnector» stereotype applied. If the type of the properties is a class or a block, you can only use a SysML binding connector to tie them.

**Related pages**

- [CONFLUENCE_PAGE title='Specifying the language for the expression' space='']
- [CONFLUENCE_PAGE title='Evaluating expressions' space='']
- [CONFLUENCE_PAGE title='Dynamic constraint' space='']
- [CONFLUENCE_PAGE title='Manual value updates using the Parametric Evaluator' space='']
- [CONFLUENCE_PAGE title='Communicating with evaluators through simulation console' space='']
- [CONFLUENCE_PAGE title='Built-in Math' space='']
- [CONFLUENCE_PAGE title='Integration with external Evaluators' space='']
- [CONFLUENCE_PAGE title='Trade study analysis' space='']
- [CONFLUENCE_PAGE title='Sample project' space='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p>Value binding is the method to maintain values of properties, which are bound together, to be the same. The properties whose values are bound, must be connected together with a connector. The type of the properties which are bound together must be the same or one is a subtype of another. If the type of the properties is a primitive type, you can bind them with either a UML connector that does not have a type, or a SysML binding connector with a «BindingConnector» stereotype applied. If the type of the properties is a class or a block, you can only use a SysML binding connector to tie them.</p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><strong>Related pages</strong></p><ul><li data-uuid="31a70c60-1ad6-4000-8da0-bb7ea325f0ac"><ac:link><ri:page ri:content-title="Specifying the language for the expression" /></ac:link></li><li data-uuid="86224795-9c27-459a-ad55-abc329400616"><ac:link><ri:page ri:content-title="Evaluating expressions" /></ac:link></li><li data-uuid="c1d4c3f8-2237-4551-aeef-ce7eecb43ea7"><ac:link><ri:page ri:content-title="Dynamic constraint" /></ac:link></li><li data-uuid="0b4ad396-fffb-482d-b18a-71c8e929a572"><ac:link><ri:page ri:content-title="Manual value updates using the Parametric Evaluator" /></ac:link></li><li data-uuid="99018ed1-da76-430f-8f7d-02c4de7b433b"><ac:link><ri:page ri:content-title="Communicating with evaluators through simulation console" /></ac:link></li><li data-uuid="6400168f-a898-44f5-9dca-876806d3b53c"><ac:link><ri:page ri:content-title="Built-in Math" /></ac:link></li><li data-uuid="3206a107-f9ca-4fc7-830d-f27a7d463154"><ac:link><ri:page ri:content-title="Integration with external Evaluators" /></ac:link></li><li data-uuid="8d8e16c8-ebe7-409d-afb5-8c6ad4726819"><ac:link><ri:page ri:content-title="Trade study analysis" /></ac:link></li><li data-uuid="23e5cb78-36f3-4c82-a329-6d0f2cae5eb0"><ac:link><ri:page ri:content-title="Sample project" /></ac:link></li></ul></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=249570899 space=MMA version=2 -->
## PAGE 00762: Value type

- page_id: `249570899`
- space_key: `MMA`
- source_url: https://docs.nomagic.com/spaces/MMA/pages/249570899/Value+type
- version_number: 2
- version_date: `2025-08-19T14:56:19.481+02:00`
- ancestors: Magic Model Analyst / Cameo Simulation Toolkit Documentation > User Guide > Simulation of SysML models > Supported SysML elements
- labels: ['value-type']

### NORMALIZED CONTENT

726567156

726567158

726567154

**On this page**

22

726567157

A value type is a data type stereotyped with «ValueType». SysML allows you to define a value type for typing value properties in your model. You can specify the quantity kind and the unit of the value type with the quantity kinds and units defined in the QUDV library.

###### [IMAGE alt='' src=''] 
Value Types Inherited from Real. 
 
 
[IMAGE alt='' src=''] 
A SysML Model Using the SysML Value Types Defined.

#### Interpreting ValueType as Real

Magic Model Analyst / Cameo Simulation Toolkit interprets all ValueTypes that are not inherited from any UML or SysML primitive types as Real primitive numbers. For example, if the value property is typed by complex (not a primitive type), it will be interpreted as real.

###### [IMAGE alt='' src=''] 
Non-Primitive Value Types Interpreted as Real.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="2d4208e6-de9f-4c1e-b0b3-dca6050a3ef4"><ac:parameter ac:name="id">726567156</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="e6d82edd-f99e-48bb-93a1-4b1b64a0408f"><ac:parameter ac:name="id">726567158</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="0035aa4e-469e-4441-9b22-95087c3ed7f9"><ac:parameter ac:name="id">726567154</ac:parameter><ac:rich-text-body><p><strong>On this page</strong></p><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="beceeb4b-a581-4306-9806-d34eadef8956"><ac:parameter ac:name="maxLevel">2</ac:parameter><ac:parameter ac:name="minLevel">2</ac:parameter></ac:structured-macro></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="e5dc8f67-52a3-40a4-88e5-9ee9099b8df8"><ac:parameter ac:name="id">726567157</ac:parameter><ac:rich-text-body><p>A value type is a data type stereotyped with «ValueType». SysML allows you to define a value type for typing value properties in your model. You can specify the quantity kind and the unit of the value type with the quantity kinds and units defined in the QUDV library.</p><h6 style="text-align: center;"><ac:image ac:align="center" ac:title="Value Types Inherited from Real " ac:alt="Value Types Inherited from Real "><ri:attachment ri:filename="valuetypes_fromReal.png" /></ac:image><br />Value Types Inherited from Real.<br class="atl-forced-newline" /><br class="atl-forced-newline" /><br class="atl-forced-newline" /><ac:image ac:title="A SysML Model Using the SysML Value Types Defined" ac:alt="A SysML Model Using the SysML Value Types Defined"><ri:attachment ri:filename="sysmodel_withvalueTypes.png" /></ac:image><br />A SysML Model Using the SysML Value Types Defined.</h6><h2>Interpreting ValueType as Real </h2><p>Magic Model Analyst / Cameo Simulation Toolkit interprets all ValueTypes that are not inherited from any UML or SysML primitive types as Real primitive numbers. For example, if the value property is typed by complex (not a primitive type), it will be interpreted as real. </p><h6 style="text-align: center;"><ac:image ac:align="center" ac:title="Non-Primitive Value Types Interpreted as Real" ac:alt="Non-Primitive Value Types Interpreted as Real"><ri:attachment ri:filename="value_asReal.png" /></ac:image><br />Non-Primitive Value Types Interpreted as Real.</h6></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=249570766 space=MMA version=1 -->
## PAGE 00763: Values

- page_id: `249570766`
- space_key: `MMA`
- source_url: https://docs.nomagic.com/spaces/MMA/pages/249570766/Values
- version_number: 1
- version_date: `2017-10-03T05:18:28.068+02:00`
- ancestors: Magic Model Analyst / Cameo Simulation Toolkit Documentation > User Guide > Parametric evaluator > Built-in Math
- labels: ['values-in-expressions']

### NORMALIZED CONTENT

The valid values that you can use in an expression are as follows

- Real Number

- Complex Number

- Boolean

- Matrix

##### Real Number

x = 3.14159

y = 2

##### Complex Number

c = 3 + 4i 
d = 1.25 + 0.25i

#### NOTE: Note

Note

An 'i' character in an expression can be parsed as either an imaginary unit or a character of a variable name. If the character 'i' is placed after a number, and the next character is neither an alphabet nor number, it will be parsed as an imaginary unit. Otherwise, it will be parsed as a variable. The examples are as follows 
**•** ca = 1i 'i' is parsed as an imaginary unit. 
**•** cb = i 'i' is parsed as a variable. 
**•** cx = 3.25i 'i' is parsed as an imaginary unit. 
**•** cy = 4i4 'i' is parsed as the first character of a variable name 'i4'

##### Boolean

a = true 
b = false

##### Matrix

U = [1.0, 2.0, 3.0; 4.0, 5.0, 6.0; 7.0, 8.0, 9.0]

A = [true; false; false; true]

You can add a matrix to the built-in Math Solver by using the following syntax (a semicolon is used as a row separator and comma or space is used as a comma separator). The examples are as follows

U = [1.0, 2.0, 3.0; 4.0, 5.0, 6.0; 7.0, 8.0, 9.0]

[IMAGE alt='' src='']

A = [true; false; false; true]

[IMAGE alt='' src='']

You can refer to a matrix element with the row and column index specified in round brackets after a matrix name. The examples are as follows (see U above)

U(1, 1) is 1.0 
U(2, 3) is 6.0

You can also refer to a matrix element with only one index specified in round brackets after a matrix name. In this case, the matrix will be considered as a column-major order matrix. The elements on the given column-major order index will be returned. The examples are as follows (see U above)

U(2) is 4.0 
U(6) is 8.0

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>The valid values that you can use in an expression are as follows</p><ul><li>Real Number</li></ul><ul><li>Complex Number </li></ul><ul><li>Boolean </li></ul><ul><li>Matrix </li></ul><h3>Real Number</h3><p style="margin-left: 30.0px;">x = 3.14159</p><p style="margin-left: 30.0px;">y = 2 </p><h3>Complex Number</h3><p style="margin-left: 30.0px;">c = 3 + 4i<br />d = 1.25 + 0.25i </p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="dbb37653-8d49-46b8-a792-88f61505807d"><ac:parameter ac:name="title">Note</ac:parameter><ac:rich-text-body><p>An 'i' character in an expression can be parsed as either an imaginary unit or a character of a variable name. If the character 'i' is placed after a number, and the next character is neither an alphabet nor number, it will be parsed as an imaginary unit. Otherwise, it will be parsed as a variable. The examples are as follows<br /><span style="color: rgb(125,133,154);"><strong>•</strong></span> ca = 1i 'i' is parsed as an imaginary unit.<br /><span style="color: rgb(125,133,154);"><strong>•</strong></span> cb = i 'i' is parsed as a variable.<br /><span style="color: rgb(125,133,154);"><strong>•</strong></span> cx = 3.25i 'i' is parsed as an imaginary unit.<br /><span style="color: rgb(125,133,154);"><strong>•</strong></span> cy = 4i4 'i' is parsed as the first character of a variable name 'i4' </p></ac:rich-text-body></ac:structured-macro><h3>Boolean</h3><p style="margin-left: 30.0px;">a = true<br />b = false </p><h3>Matrix</h3><p style="margin-left: 30.0px;">U = [1.0, 2.0, 3.0; 4.0, 5.0, 6.0; 7.0, 8.0, 9.0]</p><p style="margin-left: 30.0px;">A = [true; false; false; true]</p><p>You can add a matrix to the built-in Math Solver by using the following syntax (a semicolon is used as a row separator and comma or space is used as a comma separator). The examples are as follows</p><p style="margin-left: 30.0px;">U = [1.0, 2.0, 3.0; 4.0, 5.0, 6.0; 7.0, 8.0, 9.0] </p><p style="margin-left: 30.0px;"><ac:image><ri:attachment ri:filename="matrixU.png" /></ac:image></p><p style="margin-left: 30.0px;"><br class="atl-forced-newline" />A = [true; false; false; true] </p><p style="margin-left: 30.0px;"><ac:image><ri:attachment ri:filename="matrixA.png" /></ac:image></p><p>You can refer to a matrix element with the row and column index specified in round brackets after a matrix name. The examples are as follows (see U above)</p><p style="margin-left: 30.0px;">U(1, 1) is 1.0<br />U(2, 3) is 6.0 </p><p>You can also refer to a matrix element with only one index specified in round brackets after a matrix name. In this case, the matrix will be considered as a column-major order matrix. The elements on the given column-major order index will be returned. The examples are as follows (see U above) </p><p style="margin-left: 30.0px;">U(2) is 4.0<br />U(6) is 8.0 </p><p> </p>
````

<!--NOMAGIC_PAGE id=249570765 space=MMA version=1 -->
## PAGE 00764: Variables

- page_id: `249570765`
- space_key: `MMA`
- source_url: https://docs.nomagic.com/spaces/MMA/pages/249570765/Variables
- version_number: 1
- version_date: `2023-12-01T12:05:29.281+01:00`
- ancestors: Magic Model Analyst / Cameo Simulation Toolkit Documentation > User Guide > Parametric evaluator > Built-in Math
- labels: ['variables-in-math-solver']

### NORMALIZED CONTENT

You can use variables (operands) in the built-in Math Solver if they conform to the naming conventions as follows

**•** The characters in a variable name must be **a-z**, **A-Z**, or **0-9**. 
**•** The first character must **not** be a **number**. 
**•** Variable names must **not** be **Constants** ("**E**" or "**PI**") 
**•** Variable names must **not** be **Operators** ("**+**", "**-**", "*****", "/").

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>You can use variables (operands) in the built-in Math Solver if they conform to the naming conventions as follows</p><p style="margin-left: 30.0px;"><span style="color: rgb(125,133,154);"><strong>•</strong></span> The characters in a variable name must be <strong>a-z</strong>, <strong>A-Z</strong>, or <strong>0-9</strong>. <br class="atl-forced-newline" /><span style="color: rgb(125,133,154);"><strong>•</strong></span> The first character must <strong>not</strong> be a <strong>number</strong>. <br class="atl-forced-newline" /><span style="color: rgb(125,133,154);"><strong>•</strong></span> Variable names must <strong>not</strong> be <strong>Constants</strong> (&quot;<strong>E</strong>&quot; or &quot;<strong>PI</strong>&quot;) <br class="atl-forced-newline" /><span style="color: rgb(125,133,154);"><strong>•</strong></span> Variable names must <strong>not</strong> be <strong>Operators</strong> (&quot;<strong>+</strong>&quot;, &quot;<strong>-</strong>&quot;, &quot;<strong>*</strong>&quot;, &quot;/&quot;). </p><p><br /></p>
````

<!--NOMAGIC_PAGE id=249570176 space=MMA version=4 -->
## PAGE 00765: Variables pane

- page_id: `249570176`
- space_key: `MMA`
- source_url: https://docs.nomagic.com/spaces/MMA/pages/249570176/Variables+pane
- version_number: 4
- version_date: `2026-04-13T12:29:53.876+02:00`
- ancestors: Magic Model Analyst / Cameo Simulation Toolkit Documentation > User Guide > Simulation debugging > Runtime Value Monitoring
- labels: ['variables-tab']

### NORMALIZED CONTENT

The **Variables** pane displays the structure of a model being executed, as well as runtime values during model simulation. This pane contains two primary columns: **Name** and **Value**, and are outlined below.

- Name : represents the context and structural features of a model being simulated. The [] and {} notations are automatically shown after the structural feature as follows:
  - [] : the current State and number of Events of a State Machine and multiplicities.
  - {} : constraint expressions with parameters and subsets.
- Value : represents runtime values of structural features from the Name column. A runtime value can be the input or output of a simulation. You can directly edit runtime values in the Value column if they are Boolean, Integer, Real, and String.

[IMAGE alt='' src='']

###### The Variables pane of a simulation model session.

You can also display the **Show Requirement** and **Show Margin** columns and configure the filtering by clicking [IMAGE alt='' src=''] at the top-right corner. Also, you can select a session in the [**Sessions** pane](https://docs.nomagic.com/display/MMA/Understanding+simulation+sessions) to display its runtime objects and values that will be shown in the **Variables** pane accordingly.

The following table lists the toolbar buttons and options of the **Variables**pane.

| Button | Name | Function |
| --- | --- | --- |
|  | Refresh | To refresh the tree and values in the Variables pane. |
|  | Export to New Instance | To create a new InstanceSpecification and export a selected runtime object to a newly created InstanceSpecification. |
|  | Export to Instance | To export a selected runtime object to an InstanceSpecification, which is used to create the runtime object, or to an existing InstanceSpecification (see ). All of the slot values of the InstanceSpecification will be replaced by the runtime values of the runtime object. |
|  | Options: | To allow displaying and filtering elements in the Variables pane. Each option will be available only when the simulating model contains the kind of element to be filtered. |
|  | Show Requirement | To display the Requirement column. The value is shown only for properties that have Satisfy Relations with the Requirements in req IDs (req text format). |
|  | Show Margin | To display the Margin column. The value is calculated from value properties and the Requirement boundary with a Satisfy Relation. |
|  | Show Derived Unions | To display derived unions. |
|  | Show Redefined Properties | To display redefined properties. |
|  | Show Reference Properties | To display reference properties. |
|  | Show Adjunct Properties | To display SysML adjunct properties. |
|  | Show Constraint Properties | To display SysML constraint properties. |
|  | Show Ports | To display Ports. |

[IMAGE alt='' src='']

###### The options for displaying and filtering elements in the Variables pane.

[IMAGE alt='' src='']

###### The result of selecting Show Requirement and Show Margin options of the Variables pane.

**Related page**

- [CONFLUENCE_PAGE title='Exporting runtime objects to InstanceSpecifications' space='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p>The <strong>Variables</strong> pane displays the structure of a model being executed, as well as runtime values during model simulation. This pane contains two primary columns: <strong>Name</strong> and <strong>Value</strong>, and are outlined below.</p><ul><li data-uuid="45344c60-7faf-477e-953c-0361fa02fdce"><strong>Name</strong>: represents the context and structural features of a model being simulated. The <strong>[]</strong> and <strong>{}</strong> notations are automatically shown after the structural feature as follows:<ul><li><strong>[]</strong>: the current State and number of Events of a State Machine and multiplicities.</li><li><strong>{}</strong>: constraint expressions with parameters and subsets.</li></ul></li><li data-uuid="201bc345-0a81-4420-8f3e-24d5518075c1"><strong>Value</strong>: represents runtime values of structural features from the <strong>Name</strong> column. A runtime value can be the input or output of a simulation. You can directly edit runtime values in the <strong>Value</strong> column if they are Boolean, Integer, Real, and String.</li></ul><p><br /></p><p><ac:image ac:align="center"><ri:attachment ri:filename="The Variables pane of a simulation model session.png" /></ac:image></p><h6 style="text-align: center;">The Variables pane of a simulation model session.</h6><p>You can also display the <strong>Show Requirement</strong> and <strong>Show Margin</strong> columns and configure the filtering by clicking <ac:image><ri:attachment ri:filename="varPaneOptButton.png" /></ac:image> at the top-right corner. Also, you can select a session in the <a href="https://docs.nomagic.com/display/MMA/Understanding+simulation+sessions"><strong>Sessions</strong> pane</a> to display its runtime objects and values that will be shown in the <strong>Variables</strong> pane accordingly. </p><p style="text-align: left;">The following table lists the toolbar buttons and options of the <strong>Variables </strong>pane.</p><table class="relative-table wrapped" style="width: 98.9305%;"><colgroup><col style="width: 5.41087%;" /><col style="width: 21.5649%;" /><col style="width: 73.0397%;" /></colgroup><tbody><tr><th>Button</th><th>Name</th><th>Function</th></tr><tr><td><div class="content-wrapper"><ac:image><ri:attachment ri:filename="RefreshButton.png" /></ac:image></div></td><td>Refresh</td><td>To refresh the tree and values in the <strong>Variables</strong> pane.</td></tr><tr><td><div class="content-wrapper"><ac:image><ri:attachment ri:filename="ExportToNewInstanceButton.png" /></ac:image></div></td><td>Export to New Instance</td><td>To create a new InstanceSpecification and export a selected runtime object to a newly created InstanceSpecification. </td></tr><tr><td><div class="content-wrapper"><ac:image><ri:attachment ri:filename="ExportToInstanceButton.png" /></ac:image></div></td><td><span>Export to Instance</span></td><td>To export a selected runtime object to an InstanceSpecification, which is used to create the runtime object, or to an existing InstanceSpecification (see <ac:link><ri:page ri:content-title="Exporting runtime objects to InstanceSpecifications" /><ac:plain-text-link-body><![CDATA[Exporting Runtime Objects to InstanceSpecifications]]></ac:plain-text-link-body></ac:link>). All of the slot values of the InstanceSpecification will be replaced by the runtime values of the runtime object. </td></tr><tr><td><div class="content-wrapper"><ac:image><ri:attachment ri:filename="varPaneOptButton.png" /></ac:image></div></td><td>Options:</td><td><p>To allow displaying and filtering elements in the <strong>Variables</strong> pane. Each option will be available only when the simulating model contains the kind of element to be filtered.</p></td></tr><tr><td><br /></td><td><ul><li data-uuid="deaf5a19-d832-4659-8099-b28b37a3786a"><strong>Show Requirement</strong></li></ul></td><td>To display the <strong>Requirement</strong> column. The value is shown only for properties that have Satisfy Relations with the Requirements in req IDs (req text format).</td></tr><tr><td><br /></td><td><ul><li data-uuid="bb81fd9f-4bd1-439d-8f33-2e43a27df1d7"><strong>Show Margin</strong></li></ul></td><td>To display the <strong>Margin</strong> column. The value is calculated from value properties and the Requirement boundary with a Satisfy Relation.</td></tr><tr><td><br /></td><td><ul><li data-uuid="d1e5363e-07e2-4e9b-95cc-257060021356"><strong>Show Derived Unions</strong></li></ul></td><td>To display derived unions.</td></tr><tr><td><br /></td><td><ul><li data-uuid="0ec71c18-d694-4b3e-b741-43bcf1df9904"><strong>Show Redefined Properties</strong></li></ul></td><td>To display redefined properties.</td></tr><tr><td><br /></td><td><ul><li data-uuid="6d31de16-9001-47c5-bbc4-72b099156ad1"><strong>Show Reference Properties</strong></li></ul></td><td>To display reference properties.</td></tr><tr><td><br /></td><td><ul><li data-uuid="4c0cc0d3-2216-4660-a952-7ef10cfea040"><strong>Show Adjunct Properties</strong></li></ul></td><td>To display SysML adjunct properties.</td></tr><tr><td><br /></td><td><ul><li data-uuid="96220a96-650a-4e2a-b5d4-576925619c27"><strong>Show Constraint Properties</strong></li></ul></td><td>To display SysML constraint properties.</td></tr><tr><td><br /></td><td><ul><li data-uuid="945b7971-59c3-40f0-aa09-ef0b56f4a495"><strong>Show Ports</strong></li></ul></td><td>To display Ports.</td></tr></tbody></table><p style="text-align: center;"><ac:image><ri:attachment ri:filename="variables_pane_options.png" /></ac:image></p><h6 style="text-align: center;">The options for displaying and filtering elements in the Variables pane.</h6><p style="text-align: center;"><ac:image><ri:attachment ri:filename="selecting_options_in_variables_pane.png" /></ac:image></p><h6 style="text-align: center;">The result of selecting Show Requirement and Show Margin options of the Variables pane.</h6></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><strong>Related page</strong></p><ul><li data-uuid="f0344415-c91b-4389-8573-55683345dbee"><ac:link><ri:page ri:content-title="Exporting runtime objects to InstanceSpecifications" /></ac:link></li></ul></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=254415282 space=MMA version=1 -->
## PAGE 00766: Versions of Magic Model Analyst / Cameo Simulation Toolkit

- page_id: `254415282`
- space_key: `MMA`
- source_url: https://docs.nomagic.com/spaces/MMA/pages/254415282/Versions+of+Magic+Model+Analyst+Cameo+Simulation+Toolkit
- version_number: 1
- version_date: `2025-09-11T15:48:31.999+02:00`
- ancestors: 
- labels: []

### NORMALIZED CONTENT

69ff9259447cf5bc5907170a8f82f3ea

Magic Model Analyst / Cameo Simulation Toolkit

documentVersions

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="scroll-document-location" ac:schema-version="1" ac:macro-id="493ae90f-4875-4d2c-adaf-66c722fdfbd7"><ac:parameter ac:name="permaId">69ff9259447cf5bc5907170a8f82f3ea</ac:parameter><ac:parameter ac:name="documentTitle">Magic Model Analyst / Cameo Simulation Toolkit</ac:parameter><ac:parameter ac:name="key">documentVersions</ac:parameter></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=249570192 space=MMA version=1 -->
## PAGE 00767: Watch pane

- page_id: `249570192`
- space_key: `MMA`
- source_url: https://docs.nomagic.com/spaces/MMA/pages/249570192/Watch+pane
- version_number: 1
- version_date: `2023-08-29T07:54:36.334+02:00`
- ancestors: Magic Model Analyst / Cameo Simulation Toolkit Documentation > User Guide > Simulation debugging > Runtime Value Monitoring
- labels: []

### NORMALIZED CONTENT

#### CONTENT-LAYER: Note

1592676366

#### CONTENT-COLUMN: Note

1592676386

1592676364

**On this page**

4

#### CONTENT-BLOCK: Note

1592676376

In the **Watch** pane, you can easily monitor selected properties and their expressions with runtime values while debugging. The **Watch** pane displays a flat list of selected runtime values during model simulation.

[IMAGE alt='' src='']

###### The **Watch**pane with expressions and their selected runtime values during model simulation.

For any projects with the default Simulation window settings, the **Watch** pane will be opened by default in the same group as the **Variables** and **Breakpoints** as the last pane. If you save the project, the **Watch** pane properties will be kept according to the most recent settings, the same as the **Variables**and **Breakpoints**panes. Also, you can manually open it by clicking [IMAGE alt='' src=''] in the **Simulation** toolbar. This pane contains two columns:

- Name/Expression : When you add a Watch item, it will be shown in this column. Names and expressions can be edited in this column.
- Value : When you add a Watch item, its value will be displayed in this column. The Value can be edited if it represents a value property. It cannot be edited if it represents the result of an expression. The Value column will be highlighted in red or green the same as in the Variables.

You can also display the **Show Requirement**and **Show Margin** columns and configure filtering by clicking [IMAGE alt='' src=''] at the top-right corner.

[IMAGE alt='' src='']

###### The Watch pane with Requirement and Margin columns.

#### NOTE: Note

Note

- If the Simulation toolbar is locked (i.e., in the Monte-Carlo and Trade Study simulation), the Watch pane will be disabled to maximize performance.
- When adding items at runtime, the value is evaluated and updated for all property changes and state changes on each clock tick. However, if you add properties before runtime, the value is not be evaluated until the simulation runs.
- If the added item is not found, the value is displayed as "Not found!" in red unless you correct or remove the selected property.
- If the added item has no value, the value is displayed as <blank>.
- If the added item has multiplicity with <blank>/0 value, the value is displayed as []/ [0] .

You can add Watch items to the **Watch** pane using the following:

- 
- 
- 
- 
- 

##### Adding Watch items using the Variables pane

To add Watch items using the **Variables**pane

- In the Variables pane, right-click the property you want to add and select Add Watch . [ATTACHMENT filename='adding_items_to_watch_pane.png']

##### Adding Watch items using the Console pane

To add Watch items using the **Console**pane

1. In the input box (>>) of the Console ****pane , type the properties and expressions you want to add to the Watch pane.
2. In the Console pane toolbar click [ATTACHMENT filename='add_to_watch.png'] . The properties and expressions in the input box (>>) are added to the Watch pane. Also, the simulation automatically saves the selected language in the list box. [ATTACHMENT filename='using_console_pane.png']

##### Adding Watch items using the Watch pane

To add Watch items using the **Watch**pane

1. Do one of the following:
  - In the Watch pane toolbar, click [ATTACHMENT filename='add_to_watch.png'] .
  - In the Watch pane, click the first blank row.
2. Type the property or expression you want to add. [ATTACHMENT filename='using_watch_pane.png']

#### NOTE: Note

Note

- You can add the name of a property without using the root object because the context of the Watch pane is the main root context.
- You can also use Type if the name of a property does not exist (e.g., [spacecraft.telecom.ma](http://spacecraft.telecom.ma) = 35 ).
- Multiplicity will be shown as a flat list of an array of strings (e.g., Trade-Study.MaxEfficiency.x = [0.4761, 0.4761,…, 0.4237] ).
- You can specify an index of Multiplicity starting at 1 (e.g., Trade-Study.MaxEfficiency.x[1] = 0.4761 ).

##### Adding Watch items using the Select Properties Config

To use the Select Properties Configas a predefined list of properties and add it to a [CONFLUENCE_PAGE title='SimulationConfig stereotype' space='']

1. Create a Simulation Configuration diagram.
2. Add a Select Properties Config and Simulation Config to the diagram.
3. Set Name, Represents, and Value of the Select Properties Config.
4. Set Watch Properties of the Select Properties Config. NoteThe *Watch Properties* will be shown in the **Expert & All** view mode.
5. When running the Simulation Config, the **Watch** pane will append the properties populated from Select Properties Config. If there are existing properties, they will not be added to the **Watch** pane. [IMAGE alt='' src='']

##### Adding Watch items using an Internal Block or Parametric Diagram

You can add many properties (value, part, constraint), constraint parameters, and ports to the **Watch**pane directly from an Internal Block or Parametric Diagram.

You can only use this method if

Internal Block or Parametric Diagram

To add Watch items using an Internal Block or Parametric Diagram

1. Run the simulation.
2. In an Internal Block or Parametric Diagram, right-click a property, constraint parameter, or port, and select Simulation > Add to Watch . [ATTACHMENT filename='add_to_watch_from_ibd_or_par.png']

##### Editing and removing Watch items

You can edit and remove any items by selecting the **Name/Expression** column on the **Watch** pane.

To edit a Watch item

- Click an item to edit and press ENTER.

To remove Watch****items from the **Watch**pane

- Do one of the following:
  - To remove a single Watch item, select the item you want to remove and click [IMAGE alt='' src=''].
  - To remove all Watch items, click [ATTACHMENT filename='remove_all.png'] .

##### Adding watch items to a new Select Properties Configusing the Watch Pane

To add the watch items to a new Select Properties Configusing the Watch Pane

1. In the watch pane toolbar, click [ATTACHMENT filename='new.png'] [ATTACHMENT filename='Watch_Pane_New.png']
2. From the Select Owner dialog, choose the package where you want to save the new Select Properties Config with exported properties from a watch pane and click OK. [ATTACHMENT filename='Select Owner_Dialog.png']

You can find the exported watch list in the Containment Tree under the selected package.

[IMAGE alt='' src='']

##### Adding new watch items to the existing Select Properties Configusing the Watch Pane

To add the new watch items to the existing Select Properties Configusing the Watch Pane

- Run the simulation using the Simulation Configwith specified Watch Properties and then click [IMAGE alt='' src='']to update the Select Properties Config specified in the Simulation Config. If there is no specified Select Properties Config as Watch Properties, a dialog is displayed prompting you to select an existing Select Properties Config. This selection will then overwrite the chosen Select Properties Config. [IMAGE alt='' src='']

The Select Properties Config displays the added properties from the watch list.

[IMAGE alt='' src='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="efc5bcb3-049f-45c0-94c8-90183d995cf0"><ac:parameter ac:name="id">1592676366</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="42bb50e9-7c84-4d83-80f3-82b54d067a35"><ac:parameter ac:name="id">1592676386</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="87ad80fb-d9cb-41b1-8ba0-e91e4fbb95bd"><ac:parameter ac:name="id">1592676364</ac:parameter><ac:rich-text-body><p><strong>On this page</strong></p><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="52ba46b1-0ac6-4d06-9914-8ed1e38eec72"><ac:parameter ac:name="maxLevel">4</ac:parameter></ac:structured-macro></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="05c44161-02e4-4583-a25d-a0669c8fe81d"><ac:parameter ac:name="id">1592676376</ac:parameter><ac:rich-text-body><p>In the <strong>Watch</strong> pane, you can easily monitor selected properties and their expressions with runtime values while debugging. The <strong>Watch</strong> pane displays a flat list of selected runtime values during model simulation.</p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="Watch_Pane.jpg" /></ac:image></p><h6 style="text-align: center;">The <strong>Watch </strong>pane with expressions and their selected runtime values during model simulation.</h6><p>For any projects with the default Simulation window settings, the <strong>Watch</strong> pane will be opened by default in the same group as the <strong>Variables</strong> and <strong>Breakpoints</strong> as the last pane. If you save the project, the <strong>Watch</strong> pane properties will be kept according to the most recent settings, the same as the <strong>Variables </strong>and <strong>Breakpoints </strong>panes. Also, you can manually open it by clicking <ac:image><ri:attachment ri:filename="watch_button.png" /></ac:image> in the <strong>Simulation</strong> toolbar. This pane contains two columns:</p><ul><li><strong>Name/Expression</strong>: When you<span> </span>add a Watch item, it will be shown in this column.<span> </span>Names and expressions can be edited in this column.</li><li><strong>Value</strong>:  When you add a Watch item, its value will be displayed in this column. The Value can be edited if it represents a value property.  It cannot be edited if it represents the result of an expression. The<span> </span><strong>Value</strong><span> </span>column will be highlighted in red or green the same as in the<span> </span><strong>Variables.</strong></li></ul><p><span style="color: rgb(62,63,64);">You can also display the </span> <strong>Show Requirement </strong><span style="color: rgb(62,63,64);">and<span> </span> </span> <strong>Show Margin</strong> <span style="color: rgb(62,63,64);"> <span> </span>columns and configure filtering by clicking<span> </span> </span> <span class="confluence-embedded-file-wrapper" style="color: rgb(62,63,64);"> <ac:image><ri:attachment ri:filename="varPaneOptButton.png" /></ac:image> <span style="color: rgb(62,63,64);">at the top-right corner.</span> </span></p><p><br /></p><p style="text-align: center;"><span class="confluence-embedded-file-wrapper" style="color: rgb(62,63,64);"> <span style="color: rgb(62,63,64);"> <ac:image><ri:attachment ri:filename="Watch_Pane_With_Options.jpg" /></ac:image> </span> </span></p><h6 style="text-align: center;">The Watch pane with Requirement and Margin columns.</h6><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="7edb1775-6a50-48d7-a657-d8a238180414"><ac:parameter ac:name="title">Note</ac:parameter><ac:rich-text-body><ul><li>If the <strong>Simulation</strong> toolbar is locked (i.e., in the Monte-Carlo and Trade Study simulation), the <strong>Watch</strong> pane will be disabled to maximize performance.</li><li>When adding items at runtime, the value is evaluated and updated for all property changes and state changes on each clock tick. However, if you add properties before runtime, the value is not be evaluated until the simulation runs.</li><li>If the added item is not found, the value is displayed as &quot;Not found!&quot; in red unless you correct or remove the selected property.</li><li>If the added item has no value, the value is displayed as &lt;blank&gt;.</li><li>If the added item has multiplicity with &lt;blank&gt;/0 value, the value is displayed as []/<span class="error">[0]</span>.</li></ul></ac:rich-text-body></ac:structured-macro><p>You can add Watch items to the <strong>Watch</strong> pane using the following:</p><ul><li><ac:link ac:anchor="Adding Watch items using the Variables pane"><ac:plain-text-link-body><![CDATA[Variables pane]]></ac:plain-text-link-body></ac:link></li><li><ac:link ac:anchor="Adding Watch items using the Console pane"><ac:plain-text-link-body><![CDATA[Console pane]]></ac:plain-text-link-body></ac:link></li><li><ac:link ac:anchor="Adding Watch items using the Watch pane" /></li><li><ac:link ac:anchor="Adding Watch items using the Select Properties Config"><ac:plain-text-link-body><![CDATA[Select Properties Config stereotype]]></ac:plain-text-link-body></ac:link></li><li><ac:link ac:anchor="Adding Watch items using an Internal Block or Parametric Diagram"><ac:plain-text-link-body><![CDATA[Internal Block or Parametric Diagram]]></ac:plain-text-link-body></ac:link></li></ul><h3><br />Adding Watch items using the Variables pane</h3><p><br /></p><p>To add Watch items using the <strong>Variables </strong>pane</p><hr /><ul><li>In the <strong>Variables </strong>pane, right-click the property you want to add and select <strong>Add Watch</strong>.<br /><br /><ac:image><ri:attachment ri:filename="adding_items_to_watch_pane.png" /></ac:image></li></ul><h3><br />Adding Watch items using the Console pane</h3><p style="text-align: left;"><br /></p><p style="text-align: left;">To add Watch items using the <strong>Console </strong>pane</p><hr /><ol><li>In the input box (&gt;&gt;) of the <strong>Console</strong> <span> <strong> </strong>pane</span>, type the properties and expressions you want to add to the <strong>Watch </strong>pane.</li><li>In the <strong>Console </strong>pane toolbar click <ac:image ac:thumbnail="true" ac:height="22"><ri:attachment ri:filename="add_to_watch.png" /></ac:image>. The properties and expressions in the input box (&gt;&gt;) are added to the <strong>Watch </strong>pane. Also, the simulation automatically saves the selected language in the list box.<br /><br /><ac:image><ri:attachment ri:filename="using_console_pane.png" /></ac:image></li></ol><h3><br />Adding Watch items using the Watch pane</h3><p style="text-align: left;"><br /></p><p style="text-align: left;">To add Watch items using the <strong>Watch </strong>pane</p><hr /><ol><li>Do one of the following:<ul><li>In the <strong>Watch </strong>pane toolbar, click <ac:image><ri:attachment ri:filename="add_to_watch.png" /></ac:image>.</li><li>In the <strong>Watch </strong>pane, click the first blank row.</li></ul></li><li>Type the property or expression you want to add.<br /><br /><ac:image><ri:attachment ri:filename="using_watch_pane.png" /></ac:image><br /><br /></li></ol><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="c4f185b5-722c-4739-b688-a42b40d31b7c"><ac:parameter ac:name="title">Note</ac:parameter><ac:rich-text-body><ul><li>You can add the name of a property without using the root object because the context of the <strong>Watch</strong> pane is the main root context.</li><li>You can also use <em>Type</em> if the name of a property does not exist (e.g., <em><a href="http://spacecraft.telecom.ma">spacecraft.telecom.ma</a> = 35</em>).</li><li><em>Multiplicity</em> will be shown as a flat list of an array of strings (e.g., <em>Trade-Study.MaxEfficiency.x = [0.4761, 0.4761,…, 0.4237]</em>).</li><li>You can specify an index of <em>Multiplicity</em> starting at 1 (e.g., <em>Trade-Study.MaxEfficiency.x[1] = 0.4761</em>).</li></ul></ac:rich-text-body></ac:structured-macro><h3><br />Adding Watch items using the <span style="color: rgb(62,63,64);">Select Properties Config </span></h3><p><br /></p><p>To use the <span style="color: rgb(62,63,64);">Select Properties Config </span>as a predefined list of properties and add it to a <ac:link><ri:page ri:content-title="SimulationConfig stereotype" /><ac:plain-text-link-body><![CDATA[Simulation Configuration]]></ac:plain-text-link-body></ac:link></p><hr /><ol><li>Create a Simulation Configuration diagram.</li><li>Add a <span style="color: rgb(62,63,64);">Select Properties Config</span> and <span style="color: rgb(62,63,64);">Simulation Config</span> to the diagram.</li><li><span style="color: rgb(62,63,64);">Set Name, Represents, and Value of the Select Properties Config.</span></li><li><p class="auto-cursor-target"><ac:inline-comment-marker ac:ref="0472d5ed-cb6f-470f-b9d3-576d596c4df2"><span style="color: rgb(62,63,64);">Set Watch Properties of the Select Properties Config</span>.</ac:inline-comment-marker></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="9cf4544e-baae-479d-ae01-0e9558796bcb"><ac:parameter ac:name="title">Note</ac:parameter><ac:rich-text-body>The <em>Watch Properties</em> will be shown in the <strong>Expert &amp; All</strong> view mode.</ac:rich-text-body></ac:structured-macro></li><li><p class="auto-cursor-target">When running the <span style="color: rgb(62,63,64);">Simulation Config</span>, the <strong>Watch</strong> pane will append the properties populated from <span style="color: rgb(62,63,64);">Select Properties Config</span>. If there are existing properties, they will not be added to the <strong>Watch</strong> pane.<br /><br /></p><p><ac:image><ri:attachment ri:filename="using_SelectPropertiesConfig.png" /></ac:image></p></li></ol><h3><br />Adding Watch items using an Internal Block or Parametric Diagram</h3><p><span style="color: rgb(62,63,64);">You can add many properties (value, part, constraint), constraint parameters, and ports to the <strong>Watch </strong>pane directly from an Internal Block or Parametric Diagram.</span></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="e7580e9f-0266-486b-b89d-d07b45fc882a"><ac:rich-text-body><span style="color: rgb(62,63,64);">You can only use this method if </span>the <span style="color: rgb(62,63,64);">Internal Block or Parametric Diagram </span>context is the same as the simulation context, or if the diagram context is the first level of the simulation context structure.</ac:rich-text-body></ac:structured-macro><p><br /></p><p>To add Watch items using an Internal Block or Parametric Diagram</p><hr /><ol><li>Run the simulation.</li><li>In an Internal Block or Parametric Diagram, right-click a property, constraint parameter, or port, and select <strong>Simulation</strong> &gt; <strong>Add to Watch</strong>.<br /><br /><ac:image><ri:attachment ri:filename="add_to_watch_from_ibd_or_par.png" /></ac:image></li></ol><h3><br />Editing and removing Watch items</h3><p>You can edit and remove any items by selecting the <strong>Name/Expression</strong> column on the <strong>Watch</strong> pane.</p><p><br /></p><p>To edit a Watch item</p><hr /><ul><li>Click an item to edit and press ENTER.</li></ul><p><br /></p><p>To remove Watch<strong> </strong>items from the <strong>Watch </strong>pane</p><hr /><ul><li><p>Do one of the following:</p><ul><li><p>To remove a single Watch item, select the item you want to remove and click <ac:image><ri:attachment ri:filename="remove_button.png" /></ac:image>.</p></li><li>To remove all Watch items, click <ac:image><ri:attachment ri:filename="remove_all.png" /></ac:image>.</li></ul></li></ul><h3>Adding watch items to a new <span style="color: rgb(62,63,64);">Select Properties Config</span><ac:inline-comment-marker ac:ref="0fb9dafb-55af-4e0e-b21b-e7877ef84005"> </ac:inline-comment-marker>using the Watch Pane</h3><p><br /></p><p>To add the watch items to a new <span style="color: rgb(62,63,64);">Select Properties Config</span><ac:inline-comment-marker ac:ref="05823b95-ae6f-4807-a6ff-114cf3d05384"> </ac:inline-comment-marker>using the Watch Pane</p><hr /><ol><li> In the watch pane toolbar, click <ac:image ac:thumbnail="true" ac:height="16"><ri:attachment ri:filename="new.png" /></ac:image><br /><br /><ac:image><ri:attachment ri:filename="Watch_Pane_New.png" /></ac:image><br /><br /></li><li>From the Select Owner dialog, choose the package where you want to save the new Select Properties Config with exported properties from a watch pane and click<strong> OK.</strong><br /><br /><ac:image><ri:attachment ri:filename="Select Owner_Dialog.png" /></ac:image></li></ol><p>You can find the exported watch list in the Containment Tree under the selected package.</p><p><ac:image><ri:attachment ri:filename="Exported_Select Properties Config_.png" /></ac:image></p><h3>Adding new watch items to the existing <span style="color: rgb(62,63,64);">Select Properties Config</span><ac:inline-comment-marker ac:ref="befef167-0272-4dbb-9a89-0d998debd33a"> </ac:inline-comment-marker>using the Watch Pane</h3><p><br /></p><p>To add the new watch items to the existing <span style="color: rgb(62,63,64);">Select Properties Config</span><ac:inline-comment-marker ac:ref="b9183ac2-868b-45a5-b0a2-a41ee4277fbe"> </ac:inline-comment-marker>using the Watch Pane</p><hr /><ul><li><p><span style="color: rgb(55,65,81);text-decoration: none;">Run the simulation using the <span style="color: rgb(62,63,64);">Simulation Config </span>with specified Watch Properties and then click <ac:image ac:thumbnail="true" ac:height="16"><ri:attachment ri:filename="save.png" /></ac:image> </span>to <span style="color: rgb(55,65,81);"><span style="color: rgb(55,65,81);">update the Select Properties Config specified in the <span style="color: rgb(62,63,64);">Simulation Config</span>.<br /></span></span></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="dbe85581-481c-4094-8a82-df47b56a94e7"><ac:rich-text-body><p>If there is no specified Select Properties Config as Watch Properties, a dialog is displayed prompting you to select an existing Select Properties Config. This selection will then overwrite the chosen Select Properties Config.</p></ac:rich-text-body></ac:structured-macro><p><span style="color: rgb(55,65,81);"><br /><ac:image><ri:attachment ri:filename="Watch_Pane_Save.png" /></ac:image><br /><br /></span></p></li></ul><p>The Select Properties Config displays the added properties from the watch list.</p><p><ac:image><ri:attachment ri:filename="Updated_Select Properties Config.png" /></ac:image></p><p><br /></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=249570008 space=MMA version=2 -->
## PAGE 00768: Widgets

- page_id: `249570008`
- space_key: `MMA`
- source_url: https://docs.nomagic.com/spaces/MMA/pages/249570008/Widgets
- version_number: 2
- version_date: `2025-08-19T14:50:57.579+02:00`
- ancestors: Magic Model Analyst / Cameo Simulation Toolkit Documentation > User Guide > Simulation Configuration and UI modeling
- labels: ['html-widgets', 'custom-html-widgets', 'widget-integration']

### NORMALIZED CONTENT

Simulation supports the integration of custom HTML widgets through the build-in model library named **UI Widgets Library.mdzip**. It is used in the **WebUIWidgets** sample present under **Simulation**on the Welcome screen. For further technical details, refer to the [CONFLUENCE_PAGE title='Integrating widgets for simulation' space=''] page.

##### Using the HTML widgets model library

To use the HTML widgets model library

1. From the main menu, click File > Use Project > Use Local Project . The Use Project dialog opens.
2. In the Use Project dialog, do the following:
  - Click the From predefined location option.
  - Choose <install.root>\modelLibraries .
  - Select UI Widgets Library.mdzip . [ATTACHMENT filename='Use Project Dialog.png']
3. Click Next . UI Widgets Library will be shown as the shared Package.
4. Click Finish . A question dialog about auxiliary resources will appear.
5. Click Yes . UI Widgets Library.mdzip will be shown in the Containment tree. There are build-in widgets in the Package, e.g., JQueryKnob , LED , and KumaGuage . Those widgets are ready to be customized and used as user interfaces. [ATTACHMENT filename='UI Widget Library Package.PNG']

#### NOTE: Note

Note

- HTML widgets are self-containing owned properties (not references to any model elements except themselves).
- To further customize «Widget», open the UI Widgets Library.mdzip library and modify, save, and reattach the zip file of «Widget».

##### Integrating HTML widgets in projects

You can use widgets in the diagrams based on a Composite Structure diagram as described below.

Widgets are not supported in iterative simulations like Monte Carlo.

1. Drag the widget from the **UI Widgets Library** and drop it into the IBD/Composite Structure diagram of the simulation context. Then use a Binding Connector to connect between the value property of the system and the Port of the widget with the same Type. The widget can be resized as needed. [IMAGE alt='' src='']
2. You can customize the properties of any widgets, e.g., changing the colors of the *cursorKnob*, through the following steps:
  1. Create an Instance Specification of the widget by right-clicking the widget and selecting Tools > Create Instance . Then select a Part and Package to save.
  2. Open the Specification window of the created Instance Specification. In the left pane of the window, click **Slots** and choose either **Create Value** or **Edit Value**.
  3. Use the modified Instance Specifications as the Default Value of the Part properties in the simulation context, as shown in the following figure . [ATTACHMENT filename='Customizing Values through Creating Instance Specification of the Widget.PNG']
3. When running from a «SimulationConfig», you must set the executionTarget of the «SimulationConfig» to the simulation context, and the following Events will occur as shown in the next figure below:
  1. «Widget» Parts in the executionTarget, found at any Package levels, will be automatically generated as HTML files. All generated HTML files will be stored in the project's working directory with the same name as the project.
  2. The Console pane will print all generated HTML files and the generated folder. [ATTACHMENT filename='Running Simulation with HTML Widgets from a Simulation Config (1).PNG']
4. You can also run the simulation directly from the IBD/Composite Structure diagram that contains widgets either from the right-click menu of the diagram or the Containment tree, or the **Simulation** toolbar of the diagram. Then the simulation will automatically generate HTML files, similar to Step 3.
5. Depending on the circumstances, you can manually regenerate HTML files for further customization of the web UI. To learn more about generating HTML files, refer to [CONFLUENCE_PAGE title='Auto-generating HTML files' space='']. NoteThe **Generate HTML** command is available only when there is «Widget» as Part (either Class or Block) in the *executionTarget* of a «SimulationConfig».
6. However, if the HTML files already exist, a question dialog will be shown to prevent you from accidentally overwriting them, as shown in the figure below. 
 
[IMAGE alt='' src=''] You can select one of the following buttons for a proper action: NoteThe *<project>_index*.html file is always regenerated at the end of the process.
  - Yes : overwrite the existing <widget> .html file.
  - Yes To All : overwrite all <widget> .html files.
  - No : keep the existing <widget> .html file.
  - No To All : keep all existing <widget> .html files.

##### Widgets in nested Parts supported

You can use widgets in nested Parts. Simulation uses the name (or the element ID if the name does not exist) of the property to construct the full path name for each generated HTML file name, e.g., a nested widget, *ld-m1:LED*, of *Monitor* is generated **m1_ld-m1.html**, **m2_ld-m1.html**, and ***<Element ID>*_ld-m1.html**.

[IMAGE alt='' src='']

###### Widgets in nested Parts and generated HTML file names**.**

#### NOTE: Note

Note

When using widgets, you must define your Parts with distinctive names to shorten generated widget file names that cannot normally be longer than 255 characters, as limited by operating systems.

##### Widgets in UI mockups

You can reuse widgets in UI mockups when running a [SimulationConfig](https://docs.nomagic.com/display/MMA/SimulationConfig+stereotype) with *ShowUIAsHTML*= *true* and *UI*=*«Frame» «UI» hosted widgets*.

To reuse widgets in UI mockups

1. Create an IBD and connect the Ports of the widgets with value properties to work with runtime values.
2. Drag a property-typed widget to a «Frame» «UI». Simulation will automatically set the *config* according to the *feature*. *The image* of the widget will automatically be shown, and «NestedUIConfig» will be automatically set. You can use either a group box (by default) or a panel as a placeholder, shown below. 
 
[IMAGE alt='' src='']
3. Run a SimulationConfig with *ShowUIAsHTML= true* and *UI = «Frame» «UI» hosted widgets*. Then, HTML files of the widgets will be generated, and the HTML UI of the widgets will be displayed in the embedded browser. [IMAGE alt='' src='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>Simulation supports the integration of custom HTML widgets through the build-in model library named <strong>UI Widgets Library.mdzip</strong>. It is used in the <strong>WebUIWidgets</strong> sample present under <strong>Simulation </strong>on the Welcome screen. For further technical details, refer to the <ac:link><ri:page ri:content-title="Integrating widgets for simulation" /><ac:plain-text-link-body><![CDATA[the tutorial for integrating widgets for simulation]]></ac:plain-text-link-body></ac:link> page.</p><h3>Using the HTML widgets model library</h3><p>To use the HTML widgets model library</p><hr /><ol><li>From the main menu, click <strong>File</strong><em> &gt; </em><strong>Use Project</strong><em> &gt; </em><strong>Use Local Project</strong>. The <strong>Use Project</strong> dialog opens.</li><li>In the <strong>Use Project</strong> dialog, do the following:<br /><ul><li>Click the <strong>From predefined location</strong> option.</li><li>Choose <strong>&lt;install.root&gt;\modelLibraries</strong>.</li><li>Select <strong>UI Widgets Library.mdzip</strong>.<br /><br /><ac:image><ri:attachment ri:filename="Use Project Dialog.png" /></ac:image><br /><br /></li></ul></li><li>Click <strong>Next</strong>. <strong>UI Widgets Library</strong><em> </em>will be shown as the shared Package.</li><li>Click <strong>Finish</strong>. A question dialog about auxiliary resources will appear.</li><li>Click <strong>Yes</strong>. <strong>UI Widgets Library.mdzip</strong> will be shown in the Containment tree. There are build-in widgets in the Package, e.g., <em>JQueryKnob</em>, <em>LED</em>, and <em>KumaGuage</em>. Those widgets are ready to be customized and used as user interfaces.<br /><br /><ac:image><ri:attachment ri:filename="UI Widget Library Package.PNG" /></ac:image></li></ol><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="9c725858-b55e-47fb-a55d-9b315eb91376"><ac:parameter ac:name="title">Note</ac:parameter><ac:rich-text-body><ul><li>HTML widgets are self-containing owned properties (not references to any model elements except themselves).</li><li>To further customize «Widget», open the <strong>UI Widgets Library.mdzip</strong> library and modify, save, and reattach the zip file of «Widget».</li></ul></ac:rich-text-body></ac:structured-macro><h3>Integrating HTML widgets in projects</h3><p>You can use widgets in the diagrams based on a Composite Structure diagram as described below.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="2893dff8-40d4-47cb-ad86-8adb0396a922"><ac:rich-text-body><p>Widgets are not supported in iterative simulations like Monte Carlo.</p></ac:rich-text-body></ac:structured-macro><ol><li><p>Drag the widget from the <strong>UI Widgets Library</strong> and drop it into the IBD/Composite Structure diagram of the simulation context. Then use a Binding Connector to connect between the value property of the system and the Port of the widget with the same Type. The widget can be resized as <ac:inline-comment-marker ac:ref="7eec1533-2299-4ec8-9630-14d276560e5c">needed</ac:inline-comment-marker>.</p><p><br /><ac:image><ri:attachment ri:filename="HTML Widgets Used as Type of Property.PNG" /></ac:image><br /><br /></p></li><li><p>You can customize the properties of any widgets, e.g., changing the colors of the <em>cursorKnob</em>, through the following steps:</p><ol><li>Create an Instance Specification of the widget by right-clicking the widget and selecting <strong>Tools</strong> &gt; <strong>Create Instance</strong>. Then select a Part and Package to save.</li><li><p>Open the Specification window of the created Instance Specification. In the left pane of the window, click <strong>Slots</strong> and choose either <strong>Create Value</strong> or <strong>Edit Value</strong>.</p></li><li>Use the modified Instance Specifications as<strong> </strong>the <strong>Default Value</strong> of the Part properties in the simulation context, as shown in the following <ac:inline-comment-marker ac:ref="7b5f8428-891a-44bb-9e65-e422cee07cb2">figure</ac:inline-comment-marker>.<br /><br /><ac:image><ri:attachment ri:filename="Customizing Values through Creating Instance Specification of the Widget.PNG" /></ac:image></li></ol><p style="text-align: left;"><br /></p></li><li>When running from a «SimulationConfig», you must set the executionTarget of the «SimulationConfig» to the simulation context, and the following Events will occur as shown in the next figure below:<br /><ol><li>«Widget» Parts in the executionTarget, found at any Package levels, will be automatically generated as HTML files. All generated HTML files will be stored in the project's working directory with the same name as the project.</li><li>The <strong>Console</strong> pane will print all generated HTML files and the generated folder.<br /><br /><ac:image><ri:attachment ri:filename="Running Simulation with HTML Widgets from a Simulation Config (1).PNG" /></ac:image><br /><br /></li></ol></li><li><p>You can also run the simulation directly from the IBD/Composite Structure diagram that contains widgets either from the right-click menu of the diagram or the Containment tree, or the <strong>Simulation</strong> toolbar of the diagram. Then the simulation will automatically generate HTML files, similar to Step 3.</p></li><li><p class="auto-cursor-target">Depending on the circumstances, you can manually regenerate HTML files for further customization of the web UI. To learn more about generating HTML files, refer to <ac:link><ri:page ri:content-title="Auto-generating HTML files" /></ac:link><span style="letter-spacing: 0.0px;">.</span></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="bb77d830-106d-4245-8c3b-2fec7e495197"><ac:parameter ac:name="title">Note</ac:parameter><ac:rich-text-body><p>The <strong>Generate HTML</strong> command is available only when there is «Widget» as Part (either Class or Block) in the <em>executionTarget</em> of a «SimulationConfig».</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></li><li><p>However, if the HTML files already exist, a question dialog will be shown to prevent you from accidentally overwriting them, as shown in the figure below.<br /><br /><ac:image><ri:attachment ri:filename="Question Dialog.png" /></ac:image></p><p>You can select one of the following buttons for a proper action:</p><ul><li><strong>Yes</strong>: overwrite the existing <em>&lt;widget&gt;</em>.html file.</li><li><strong>Yes To All</strong>: overwrite all <em>&lt;widget&gt;</em>.html files.</li><li><strong>No</strong>: keep the existing <em>&lt;widget&gt;</em>.html file.</li><li><strong>No To All</strong>: keep all existing <em>&lt;widget&gt;</em>.html files.</li></ul><p><br /></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="f9667f90-290e-4835-8f4d-9b7675ae9d8a"><ac:parameter ac:name="title">Note</ac:parameter><ac:rich-text-body><p>The <em>&lt;project&gt;_index</em>.html file is always regenerated at the end of the process.</p></ac:rich-text-body></ac:structured-macro></li></ol><h3>Widgets in nested Parts supported</h3><p>You can use widgets in nested Parts. Simulation uses the name (or the element ID if the name does not exist) of the property to construct the full path name for each generated HTML file name, e.g., a nested widget, <em>ld-m1:LED</em>, of <em>Monitor</em> is generated <strong>m1_ld-m1.html</strong>, <strong>m2_ld-m1.html</strong>, and <strong><em>&lt;Element ID&gt;</em>_ld-m1.html</strong>.</p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="Widgets in Nested Parts.PNG" /></ac:image></p><h6 style="text-align: center;">Widgets in nested Parts and generated HTML file names<strong>.</strong></h6><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="9846b804-8469-45ec-a9b1-f26ba9711b5f"><ac:parameter ac:name="title">Note</ac:parameter><ac:rich-text-body><p>When using widgets, you must define your Parts with distinctive names to shorten generated widget file names that cannot normally be longer than 255 characters, as limited by operating systems.</p></ac:rich-text-body></ac:structured-macro><h3>Widgets in UI mockups</h3><p>You can reuse widgets in UI mockups when running a <a href="https://docs.nomagic.com/display/MMA/SimulationConfig+stereotype">SimulationConfig</a> with <em>ShowUIAsHTML </em>= <em>true</em> and <em>UI </em>=<em> «Frame» «UI» hosted widgets</em>.</p><p>To reuse widgets in UI mockups</p><hr /><ol><li>Create an IBD and connect the Ports of the widgets with value properties to work with runtime values.</li><li><p>Drag a property-typed widget to a «Frame» «UI». Simulation will automatically set the <em>config</em> according to the <em>feature</em>. <em>The image</em> of the widget will automatically be shown, and «NestedUIConfig» will be automatically set. You can use either a group box (by default) or a panel as a placeholder, shown <ac:inline-comment-marker ac:ref="e7976afb-4107-42b3-8939-b90c73c44a61">below</ac:inline-comment-marker>.<br /><br /><ac:image><ri:attachment ri:filename="UI_Cruise Control.png" /></ac:image><br /><br /></p></li><li><p>Run a SimulationConfig with <em><span>ShowUIAsHTML=</span> true</em> and <em>UI = «Frame» «UI» hosted widgets</em>. Then, HTML files of the widgets will be generated, and the HTML UI of the widgets will be displayed in the embedded browser.</p><p><ac:image ac:align="left"><ri:attachment ri:filename="CruiseControl with Widgets.png" /></ac:image></p></li></ol>
````

<!--NOMAGIC_PAGE id=249571082 space=MMA version=2 -->
## PAGE 00769: Writing runtime values to an Excel spreadsheet

- page_id: `249571082`
- space_key: `MMA`
- source_url: https://docs.nomagic.com/spaces/MMA/pages/249571082/Writing+runtime+values+to+an+Excel+spreadsheet
- version_number: 2
- version_date: `2025-08-19T14:51:01.983+02:00`
- ancestors: Magic Model Analyst / Cameo Simulation Toolkit Documentation > User Guide > Action languages > Action scripts APIs > Excel Helper APIs
- labels: []

### NORMALIZED CONTENT

The following API helps you write fUML runtime values to an Excel file.

```text

```

The APIs can ignore the sheetName and use the first sheet of the selected spreadsheet instead.

```text

```

The mappingElement parameter can be String or Element for represent the mapping Class name or mapping Class Element. The APIs can write the runtime objects of the file schema element to spreadsheet that is matched the file name by ignore the mapping class.

```text

```

#### INFO: Information

Information

You can also write runtime values to an Excel file (.xlsx) as [an attached file supported](https://docs.nomagic.com/display/MMA/Attached+files+supported).

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>The following API helps you write fUML runtime values to an Excel file.<br class="atl-forced-newline" /><span style="color: rgb(127,0,85);"> </span></p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="ea6130bb-0bca-437f-89ed-58e9799c3e62"><ac:parameter ac:name="language">text</ac:parameter><ac:plain-text-body><![CDATA[public void writeObjectsToSpreadSheet(Object object, String fileName, String sheetName, Number atRow, boolean isReplace, Object mappingElement) {
...
} ]]></ac:plain-text-body></ac:structured-macro><p><br class="atl-forced-newline" />The APIs can ignore the sheetName and use the first sheet of the selected spreadsheet instead. <br class="atl-forced-newline" /><span style="color: rgb(127,0,85);"> </span></p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="846e280b-1a09-428d-83ff-3d961707c8c4"><ac:parameter ac:name="language">text</ac:parameter><ac:plain-text-body><![CDATA[public void writeObjectsToSpreadSheet(Object object, String fileName, Number atRow, boolean isReplace, Object mappingElement) {
...
} ]]></ac:plain-text-body></ac:structured-macro><p><br class="atl-forced-newline" />The mappingElement parameter can be String or Element for represent the mapping Class name or mapping Class Element. The APIs can write the runtime objects of the file schema element to spreadsheet that is matched the file name by ignore the mapping class. <br class="atl-forced-newline" /><span style="color: rgb(127,0,85);"> </span></p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="e52b7cf0-cfbf-4428-86e8-ef48f1e293da"><ac:parameter ac:name="language">text</ac:parameter><ac:plain-text-body><![CDATA[public void writeObjectsToSpreadSheet(Object object, String fileName, String sheetName, Number atRow, boolean isReplace) {
...
} 
public void writeObjectsToSpreadSheet(Object object, String fileName, Number atRow, boolean isReplace) {
...
}]]></ac:plain-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><p><br /></p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="2ff7dad2-9cbd-4bef-9c22-be7c84e8415a"><ac:parameter ac:name="title">Information</ac:parameter><ac:rich-text-body><p>You can also write runtime values to an Excel file (.xlsx) as <a href="https://docs.nomagic.com/display/MMA/Attached+files+supported">an attached file supported</a>.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p>
````
