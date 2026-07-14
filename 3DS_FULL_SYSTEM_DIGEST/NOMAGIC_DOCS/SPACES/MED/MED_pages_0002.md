# NOMAGIC DOCUMENTATION SPACE: SysML v1/UAF/UML Model Element Descriptions

<!--NOMAGIC_SPACE key=MED chunk=2 -->

<!--NOMAGIC_PAGE id=243967893 space=MED version=1 -->
## PAGE 00327: Pin

- page_id: `243967893`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/243967893/Pin
- version_number: 1
- version_date: `2025-07-31T10:50:43.997+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UML elements
- labels: []

### NORMALIZED CONTENT

835864361

835864365

835948884

**On this page**

43

835864364

##### Description

A Pin represents a connection point for the input and output values of an action. There is one input Pin for each input parameter, and one output pin for each output parameter.

[IMAGE alt='' src='']

You can create the following types of Pins:

- Input Pin. An input pin is a pin that holds input values to be consumed by an action.
- Output Pin.
- Value Pin.
- Action Input Pin.

- When a new action is created that must have mandatory Pins, they are automatically added to that action on the diagram pane, as well as in the Containment tree.
- As of modeling tool 17.0.4 version, the Pins Displaying [CONFLUENCE_PAGE title='Validation' space='MT'] suite has been introduced. It includes the Action Containing Hidden Pins validation rule that detects all hidden pins for the concrete action symbol.
- When deleting the last Pin symbol from the diagram, the Pin element is deleted from the project. This is valid when the Display All Pins in Diagrams option value is true.
- For a send signal action, a Pin is created, but the symbol of the Pin is not represented on the diagram pane.
- You can navigate to the associated parameter from the Pin shortcut menu. From the Pin shortcut menu, select Go To and choose a parameter.

You can format the pin symbol properties in the [CONFLUENCE_PAGE title='Symbol Properties dialog' space='MT'].

You can [CONFLUENCE_PAGE title='Editing property values' space='MT'] in the pin [CONFLUENCE_PAGE title='Specification window' space='MT']. In the [CONFLUENCE_PAGE title='Specification window' space='MT'], you can find the description of each property, which are located in the description area of the [CONFLUENCE_PAGE title='Specification window' space='MT']

##### Assigning Pins

To assign Pins for an action on the diagram pane

1. In the activity diagram, draw an action.
2. In the activity diagram palette, select a Pin you want to create.
3. On the diagram pane, click the action. The Pin for this action is created.

To assign Pins for an action in the action [CONFLUENCE_PAGE title='Specification window' space='MT']

1. In the action [CONFLUENCE_PAGE title='Specification window' space='MT'] , in Pins property group, select one of the following:
  - Input Pin. Select Argument, and, in the property specification cell, click the Add button. Select one of the preferred pins from the list.
  - Output Pin. Select Result, and in the property specification cell, click the Add button.
2. In the opened Pin [CONFLUENCE_PAGE title='Specification window' space='MT'] , type the Pin name.
3. Click Close or Back to return to the action [CONFLUENCE_PAGE title='Specification window' space='MT'] .

##### Specifying Pin type

After the Pin is assigned to an action, you can specify its type. Use one of the following ways:

- Using the **Specify Type** button.
- 

buttonTo specify Pin type by using the **Specify Type** button

1. Select the Pin shape.
2. Click [ATTACHMENT filename='specify_type.png'] on the [CONFLUENCE_PAGE title='Smart manipulator toolbar' space='MT'] .
3. Do one of the following: - Select an existing element from the Select Type menu. - Create new type: a. Type a name. b. Press Enter. c. In the Create <type name> As dialog, select element kind. The type is specified for a Pin.

windowTo specify Pin type by using the Specification window

1. Right-click the Pin and select the Specification command.
2. In the [CONFLUENCE_PAGE title='Specification window' space='MT'] , select the Type property value cell.
3. Do one of the following: - Select an existing element from the list. - Click [ATTACHMENT filename='edit_button_in_specification_window.png'] and in the Select Element dialog do the following: - Select an existing elements from the Tree or List tab. - create new element by switching on the Creation Mode and clicking the Create button.
4. Click Close . The type is specified for a Pin.

##### Displaying Pins

To display Pins on shapes

1. On the diagram pane, select any number of shapes on which you want to display Pins.
2. Open the Select Pins dialog by performing one of the following steps: - From the shortcut menu, select Display > Display Pins . - On the diagram toolbar, click [IMAGE alt='' src=''] and select Display Pins.
3. In the dialog, select the Pins you want to display.
4. In the **Layout options** area, specify the Pins' layout on the shape: 
- **Top/Bottom** - displays Pins on the shape from its top to bottom. 
- **Left/Right** - displays Pins on the shape from its left to right.
5. When you are finished, click OK .

If you want all Pins to be displayed automatically when creating a new Activity diagram, go to **Options** > **Project**on the main menu, and set the **Display All Pins in Diagrams** option to *true.***

If you have an element displayed as an image, you can connect a Pin to that element with no gaps.

[IMAGE alt='' src='']

##### Showing Pin's type

To show the Pin’s type, perform one of the following steps

- From the Pin shortcut menu, select Show Type .
- In the Pin [CONFLUENCE_PAGE title='Symbol Properties dialog' space='MT'] , set the Show Type property to true.

##### Converting a Pin

To convert an input Pin to an output Pin and vice versa

1. From the Pin shortcut menu, select Refactor > Convert To .
2. From the opened list, select one of the following:
  - Input Pin (Output Pin)
  - Action Input Pin
  - Value Pin

To [CONFLUENCE_PAGE title='Converting Elements' space='MT'] to an object node

1. From the Pin shortcut menu, select Refactor > Convert To .
2. From the opened list, select Object Node .

##### Navigating from a Pin to the associated parameter

To navigate from a Pin to the associated parameter

- From the Pin shortcut menu, select Go To, and choose a parameter.

835864360

**Related pages**

- [CONFLUENCE_PAGE title='UML elements' space='']
- [CONFLUENCE_PAGE title='Specification window' space='MT']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="6310d521-111f-4e83-8a18-4f5eb796180d"><ac:parameter ac:name="id">835864361</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="4a45e524-e397-4267-bf8d-9379adf37647"><ac:parameter ac:name="id">835864365</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="9ecbb057-fc3f-4279-8de2-3f939dadc1d8"><ac:parameter ac:name="id">835948884</ac:parameter><ac:rich-text-body><p><strong>On this page</strong></p><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="4419d0e9-a1f8-4e93-9dfe-412e764a8e66"><ac:parameter ac:name="maxLevel">4</ac:parameter><ac:parameter ac:name="minLevel">3</ac:parameter></ac:structured-macro></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="9b38b208-ed34-497b-acd1-2770c0c1f293"><ac:parameter ac:name="id">835864364</ac:parameter><ac:rich-text-body><h3>Description</h3><p>A Pin represents a connection point for the input and output values of an action. There is one input Pin for each input parameter, and one output pin for each output parameter.</p><p><ac:image ac:title="Example of output and input pins" ac:alt="Example of output and input pins"><ri:attachment ri:filename="pin.png" /></ac:image></p><p>You can create the following types of Pins:</p><ul><li>Input Pin. An input pin is a pin that holds input values to be consumed by an action.</li><li>Output Pin. </li><li>Value Pin.</li><li>Action Input Pin.</li></ul><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="3b6bf9d9-e60e-415b-8a59-90960f2bd850"><ac:rich-text-body><ul><li>When a new action is created that must have mandatory Pins, they are automatically added to that action on the diagram pane, as well as in the Containment tree.</li><li>As of modeling tool 17.0.4 version, the <em>Pins Displaying </em><ac:link><ri:page ri:space-key="MT" ri:content-title="Validation" /><ac:plain-text-link-body><![CDATA[validation ]]></ac:plain-text-link-body></ac:link>suite has been introduced. It includes the <em>Action Containing Hidden Pins</em> validation rule that detects all hidden pins for the concrete action symbol.</li><li>When deleting the last Pin symbol from the diagram, the Pin element is deleted from the project. This is valid when the Display All Pins in Diagrams option <span style="line-height: 1.42857;">value is true.</span></li><li>For a send signal action, a Pin is created, but the symbol of the Pin is not represented on the diagram pane.</li><li>You can navigate to the associated parameter from the Pin shortcut menu. From the Pin shortcut menu, select Go To and choose a parameter.</li></ul></ac:rich-text-body></ac:structured-macro><p>You can format the pin symbol properties in the <ac:link><ri:page ri:space-key="MT" ri:content-title="Symbol Properties dialog" /></ac:link>.</p><p>You can <ac:link><ri:page ri:space-key="MT" ri:content-title="Editing property values" /><ac:plain-text-link-body><![CDATA[specify pin properties]]></ac:plain-text-link-body></ac:link> in the pin <ac:link><ri:page ri:space-key="MT" ri:content-title="Specification window" /></ac:link>. In the <ac:link><ri:page ri:space-key="MT" ri:content-title="Specification window" /></ac:link>, you can find the description of each property, which are located in the description area of the <ac:link><ri:page ri:space-key="MT" ri:content-title="Specification window" /><ac:plain-text-link-body><![CDATA[Specification window.]]></ac:plain-text-link-body></ac:link></p><h3>Assigning Pins</h3><p>To assign Pins for an action on the diagram pane</p><hr /><ol><li>In the activity diagram, draw an action.</li><li>In the activity diagram palette, select a Pin you want to create.</li><li>On the diagram pane, click the action. The Pin for this action is created.</li></ol><p><br /></p><p>To assign Pins for an action in the action <ac:link><ri:page ri:space-key="MT" ri:content-title="Specification window" /></ac:link></p><hr /><ol><li>In the action <ac:link><ri:page ri:space-key="MT" ri:content-title="Specification window" /></ac:link>, in <strong>Pins</strong> property group, select one of the following:<ul><li>Input Pin. Select Argument, and, in the property specification cell, click the Add button. Select one of the preferred pins from the list. </li><li>Output Pin. Select Result, and in the property specification cell, click the Add button.</li></ul></li><li>In the opened Pin <ac:link><ri:page ri:space-key="MT" ri:content-title="Specification window" /></ac:link>, type the Pin name.</li><li>Click <strong>Close</strong> or <strong>Back</strong> to return to the action <ac:link><ri:page ri:space-key="MT" ri:content-title="Specification window" /></ac:link>.</li></ol><h3>Specifying Pin type</h3><p>After the Pin is assigned to an action, you can specify its type. Use one of the following ways:</p><ul><li><ac:link ac:anchor="button"><ac:link-body>Using the <strong>Specify Type</strong> button.</ac:link-body></ac:link></li><li><ac:link ac:anchor="window"><ac:plain-text-link-body><![CDATA[Using the Specification window.]]></ac:plain-text-link-body></ac:link></li></ul><p><br /></p><p><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="7c81d126-8932-4b4d-bdd6-6d4f9c332dee"><ac:parameter ac:name="">button</ac:parameter></ac:structured-macro>To specify Pin type by using the <strong>Specify Type</strong> button</p><hr /><ol><li>Select the Pin shape.</li><li>Click <ac:image ac:title="Specify Type" ac:thumbnail="true" ac:alt="Specify Type" ac:height="11"><ri:attachment ri:filename="specify_type.png"><ri:page ri:space-key="MT" ri:content-title="_MD buttons" /></ri:attachment></ac:image> on the <ac:link><ri:page ri:space-key="MT" ri:content-title="Smart manipulator toolbar" /><ac:plain-text-link-body><![CDATA[smart manipulator toolbar]]></ac:plain-text-link-body></ac:link>.</li><li>Do one of the following:<br /> - Select an existing element from the <strong>Select Type</strong> menu.<br /> - Create new type:<br />        a. Type a name.<br />        b. Press Enter.<br />        c. In the <strong>Create &lt;type name&gt; As </strong>dialog, select element kind.<br />The type is specified for a Pin.</li></ol><p><br /></p><p><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="5886f79e-d17a-44ad-bc15-715d5c44e474"><ac:parameter ac:name="">window</ac:parameter></ac:structured-macro>To specify Pin type by using the Specification window</p><hr /><ol><li>Right-click the Pin and select the <strong>Specification</strong> command.</li><li>In the <ac:link><ri:page ri:space-key="MT" ri:content-title="Specification window" /></ac:link>, select the <strong>Type</strong> property value cell.</li><li>Do one of the following:<br /> - Select an existing element from the list.<br /> - Click <ac:image ac:thumbnail="true" ac:height="17"><ri:attachment ri:filename="edit_button_in_specification_window.png"><ri:page ri:space-key="MT" ri:content-title="Composite Structure Diagram context" /></ri:attachment></ac:image> and in the <strong>Select Element</strong> dialog do the following:<br />         - Select an existing elements from the <strong>Tree </strong>or<strong> List</strong> tab.<br />         - create new element by switching on the <strong>Creation Mode</strong> and clicking the <strong>Create</strong> button.</li><li>Click <strong>Close</strong>.<br />The type is specified for a Pin.</li></ol><h3>Displaying Pins</h3><p>To display Pins on shapes</p><hr /><ol><li>On the diagram pane, select any number of shapes on which you want to display Pins.</li><li>Open the <strong>Select Pins</strong> dialog by performing one of the following steps:<br /> - From the shortcut menu, select <strong>Display</strong> &gt; <strong>Display Pins</strong>.<br /> - On the diagram toolbar, click <span class="confluence-embedded-file-wrapper"><ac:image ac:title="Display" ac:alt="Display"><ri:attachment ri:filename="Display.png" /></ac:image></span> and select <strong>Display Pins.</strong></li><li><p>In the dialog, select the Pins you want to display.</p></li><li><p>In the <strong>Layout options</strong> area, specify the Pins' layout on the shape:<br />- <strong>Top/Bottom</strong> - displays Pins on the shape from its top to bottom.<br />- <strong>Left/Right </strong> - displays Pins on the shape from its left to right.</p></li><li>When you are finished, click <strong>OK</strong>.<br /><br /></li></ol><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="dbdb3dc4-ec3d-4573-bfc9-0c8c4f04f7e9"><ac:rich-text-body><p>If you want all Pins to be displayed automatically when creating a new Activity diagram, go to <strong>Options</strong> &gt; <strong>Project </strong>on the main menu, and set the <strong>Display All Pins in Diagrams</strong> option to <em>true.</em><em><br /></em></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="90310ece-d52a-4eed-b831-489c1e216f87"><ac:rich-text-body><p>If you have an element displayed as an image, you can connect a Pin to that element with no gaps.</p><p><ac:image><ri:attachment ri:filename="ports_pins_tip.png" /></ac:image></p></ac:rich-text-body></ac:structured-macro><p><br /></p><h3>Showing Pin's type</h3><p>To show the Pin’s type, perform one of the following steps</p><hr /><ul><li>From the Pin shortcut menu, select <strong>Show Type</strong>.</li><li>In the Pin <ac:link><ri:page ri:space-key="MT" ri:content-title="Symbol Properties dialog" /></ac:link>, set the <strong>Show Type</strong> property to true.</li></ul><p><br /></p><h3>Converting a Pin</h3><p>To convert an input Pin to an output Pin and vice versa</p><hr /><ol><li>From the Pin shortcut menu, select <strong>Refactor</strong> &gt; <strong>Convert To</strong>.</li><li>From the opened list, select one of the following:<ul><li>Input Pin (Output Pin)</li><li>Action Input Pin</li><li>Value Pin</li></ul></li></ol><p><br /></p><p>To <ac:link><ri:page ri:space-key="MT" ri:content-title="Converting Elements" /><ac:plain-text-link-body><![CDATA[convert a Pin]]></ac:plain-text-link-body></ac:link> to an object node</p><hr /><ol><li>From the Pin shortcut menu, select <strong>Refactor</strong> &gt; <strong>Convert To</strong>.</li><li>From the opened list, select <strong>Object Node</strong>.</li></ol><h3>Navigating from a Pin to the associated parameter</h3><p>To navigate from a Pin to the associated parameter</p><hr /><ul><li>From the Pin shortcut menu, select <strong>Go To,</strong> and choose a parameter.</li></ul><p><br /></p><p class="auto-cursor-target"><br /></p><p><br /></p><p class="auto-cursor-target"><br /></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="fb552934-f6e2-4575-963e-1d7fe5ae7a9a"><ac:parameter ac:name="id">835864360</ac:parameter><ac:rich-text-body><p class="auto-cursor-target"><strong>Related pages</strong></p><ul><li><ac:link><ri:page ri:content-title="UML elements" /><ac:plain-text-link-body><![CDATA[Model Elements]]></ac:plain-text-link-body></ac:link></li><li><ac:link><ri:page ri:space-key="MT" ri:content-title="Specification window" /><ac:plain-text-link-body><![CDATA[Specification Window]]></ac:plain-text-link-body></ac:link></li></ul><p class="auto-cursor-target"><br /></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=243967897 space=MED version=1 -->
## PAGE 00328: Port

- page_id: `243967897`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/243967897/Port
- version_number: 1
- version_date: `2025-07-31T10:50:44.453+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UML elements
- labels: []

### NORMALIZED CONTENT

230618172

230618174

230648634

**On this page**

43

230618173

##### Description

A port is a property of a classifier that specifies a distinct interaction point between that classifier and its environment, or between the (behavior of the) classifier and its internal parts. Ports are connected to the properties of the classifier by connectors through which requests can be made to invoke the behavioral features of the classifier.

A Port can specify the services a classifier provides (offers) to its environment as well as the services that a classifier expects (requires) from its environment. It has the ability to specify that any requests arriving at this port are handled.

The Class model element and Component model elements can have any number of Ports.

You can [CONFLUENCE_PAGE title='Editing property values' space='MT'] in the port [CONFLUENCE_PAGE title='Specification window' space='MT']. In the same window, you can find the description of each property. Descriptions are presented in the description area of the [CONFLUENCE_PAGE title='Specification window' space='MT'].

##### Creating Port

To create a port, do one of the following

1. From the diagram palette, select port and on the diagram pane, click the element.
2. Select an element and from the smart manipulator toolbar, choose the Port button.
3. In the element [CONFLUENCE_PAGE title='Specification window' space='MT'] , Port property group, click the Create button.

If you have an element displayed as image, you can connect a port to that element with no gaps.

[IMAGE alt='' src='']

##### Defining Port type

To define a Port type, do one of the following

- On a diagram, select a port and press Ctrl+T (press Cmd+T for MAC OS X). Select a type from the list.
- On a diagram, select a port and in the smart manipulator toolbar, click the Specify Type button. Select a type from the list.
- In the port [CONFLUENCE_PAGE title='Specification window' space='MT'] , Type property specification cell, select a type.

##### Displaying Port type

To show the Port type, do one of the following

- Select a port, and from the shortcut menu, choose Show Type .
- In the port [CONFLUENCE_PAGE title='Symbol Properties dialog' space='MT'] , set the Show Type property to true.

##### Displaying Ports on shapes

To display Ports on shapes

1. Right-click the shape, select Display > Display Parts/Ports . The Display Parts/Ports dialog opens.
2. Select ports you want to display on the shape: 
- On the left side of the dialog, select ports manually. 
- On the right side of the dialog, use the panel to select all or particular types of properties or ports.
3. Click OK when you are done.

- The port type near the port symbol is displayed if port has referenced type, but has no name.
- The port type near the port symbol is not displayed if type is provided or required interface and the interface is displayed on the diagram.
- When a part symbol is created, all its ports are displayed on the diagram.

##### Creating a Port on a composite structure diagram frame

To create a Port on a composite structure diagram frame

1. Select an element and from the smart manipulator toolbar, choose the Connector button.
2. Click the composite structure diagram frame. The port is created and the Select Port list is displayed.
3. Select one of the following:
  - A hidden port or a nested port of the composite structure diagram.
  - New Port - click to create a port on a diagram frame, with the same name, type and multiplicity, as it is set on the source part or port.
  - **Nested Port** - click to create a new nested port. The **Nested Port** is available only when creating a connector from the nested port to the diagram frame.

- You can also quickly create a port on the composite structure diagram frame when drawing a connector straight from a composite structure diagram frame.
- If a connector is created from a port with the defined type, then only compatible hidden ports are listed in the Select Port list.
- If a connector is created from a port that has interfaces, then ports that have compatible interfaces are listed in the Select Port list.

[IMAGE alt='' src='']

[IMAGE alt='' src='']

##### Displaying Port in compartment

To display Ports in the element compartment

1. On the diagram, select a symbol and click the Compartments button.
2. In the list, select Ports . The ports' compartment is displayed on a symbol.

In the **Compartment Edit** dialog, you can select which ports to display in the ports' compartment.

##### Changing position of Port label

To change position of Port label

1. Right-click the Port shape and select the Symbol Properties command.
2. In the [CONFLUENCE_PAGE title='Symbol Properties dialog' space='MT'] , select the All property display mode.
3. Find the **Position of Labels** property and select on of the following value: 
 - **Outside** to show the label outside the Port shape. 
[IMAGE alt='' src=''] 
 - **Inside** to show labels inside the Port shape. 
[IMAGE alt='' src=''] 
 - **Name and Type Labels Inside** to show only the name and type inside the Port shape. 
[IMAGE alt='' src=''] 
 - **Inside Enclosing Shape** to show the label outside the Port shape but inside enclosing shape on which boundary the port is created. Nested ports do not support **Inside Enclosing Shape** value. [IMAGE alt='' src='']

##### Specifying the Provided/Required Interfaces for a Port

To specify the Provided/Required Interfaces for a Port even if the Port type is not specified

1. In the Port [CONFLUENCE_PAGE title='Specification window' space='MT'] , Provided/Required Interfaces property group, click the Add button.
2. Select to either provided or required interface.
3. In the case, when the port type is not specified, the Select Port Type dialog is displayed. Select one of the following options:
  - Set provided interface as a port type (available only when creating a provided interface). The provided interface will be specified as the port type.
  - Create "dummy" port type automatically. Create a “dummy” port type and relations between the type and interface.
  - Select or create a port type manually. The Select Port Type dialog will open, to allow you to select or create a Port.
4. In the element Selection dialog, select or create an interface and click OK .

- Draw a realize relationship from a port to an interface to create a provided interface.
- Draw a usage relationship from a port to an interface to create a required interface.

##### Converting a Port to an Association

To convert a Port to an Association, do one of the following

- From the port's shortcut menu, select Refactor > Convert To > Association .
- In the port's compartment, select a port and drag it out of the shape.

You can convert a port to an association, only if the port type is specified and a port is not a member of any association end.

##### Displaying a Port name in a signature on a shape

To display a Port name in a signature on a shape

- In the [CONFLUENCE_PAGE title='Symbol Properties dialog' space='MT']**Symbol Properties** dialog , click to select the Show Port property.

If you cannot find the **Show Port** property in the [CONFLUENCE_PAGE title='Symbol Properties dialog' space='MT']**Symbol Properties** dialog, change the properties display mode to *Expert* or *All*.

You can display the Port name on the following shapes: 
• Call Operation Action, Call Behavior Action, Send Signal Action, Send Object Action, Broadcast Signal Action, and Start Object Behavior Action. 
For example: via <Port name>.

[IMAGE alt='' src=''] 
• Transition, Protocol Transition, State, and Accept Event Action. 
For example: « from» <Port name>.

##### Hiding the multiplicity

To hide the multiplicity next to the Port's type

1. Right-click the Port shape and select Symbol Properties.
2. In the Symbol Properties dialog, set the Show Multiplicity property value to false .
3. Click Close .

230618171

**Related pages**

- [CONFLUENCE_PAGE title='Displaying parts and ports' space='MT']
- [CONFLUENCE_PAGE title='UML elements' space='']
- [CONFLUENCE_PAGE title='Specification window' space='MT']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="9f5e74a4-8582-4820-89d0-0a91f93b0daf"><ac:parameter ac:name="id">230618172</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="decb9410-696a-4b7e-be19-6a8142930239"><ac:parameter ac:name="id">230618174</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="a142d52d-6f62-4a0b-ae75-1cec2e7ee62d"><ac:parameter ac:name="id">230648634</ac:parameter><ac:rich-text-body><p><strong>On this page</strong></p><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="d37ef7c5-1d4f-4e7e-bdbc-d9ead5d4c09c"><ac:parameter ac:name="maxLevel">4</ac:parameter><ac:parameter ac:name="minLevel">3</ac:parameter></ac:structured-macro></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="0d3fbeee-4814-489c-99ec-09f0f104189d"><ac:parameter ac:name="id">230618173</ac:parameter><ac:rich-text-body><h3>Description</h3><p>A port is a property of a classifier that specifies a distinct interaction point between that classifier and its environment, or between the (behavior of the) classifier and its internal parts. Ports are connected to the properties of the classifier by connectors through which requests can be made to invoke the behavioral features of the classifier.</p><p>A Port can specify the services a classifier provides (offers) to its environment as well as the services that a classifier expects (requires) from its environment. It has the ability to specify that any requests arriving at this port are handled.</p><p>The Class model element and Component model elements can have any number of Ports.</p><p>You can <ac:link><ri:page ri:space-key="MT" ri:content-title="Editing property values" /><ac:plain-text-link-body><![CDATA[specify port properties]]></ac:plain-text-link-body></ac:link> in the port <ac:link><ri:page ri:space-key="MT" ri:content-title="Specification window" /></ac:link>. In the same window, you can find the description of each property. Descriptions are presented in the description area of the <ac:link><ri:page ri:space-key="MT" ri:content-title="Specification window" /></ac:link>.</p><p><br /></p><h3>Creating Port</h3><p>To create a port, do one of the following</p><hr /><ol><li>From the diagram palette, select port and on the diagram pane, click the element.</li><li>Select an element and from the smart manipulator toolbar, choose the Port button.</li><li>In the element <ac:link><ri:page ri:space-key="MT" ri:content-title="Specification window" /></ac:link>, <strong>Port</strong> property group, click the <strong>Create</strong> button.</li></ol><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="6f5f22c0-3040-4e27-9590-427d52887a7d"><ac:rich-text-body><p>If you have an element displayed as image, you can connect a port to that element with no gaps.</p><p><ac:image><ri:attachment ri:filename="ports_pins_tip.png" /></ac:image></p></ac:rich-text-body></ac:structured-macro><h3>Defining Port type</h3><p>To define a Port type, do one of the following</p><hr /><ul><li>On a diagram, select a port and press Ctrl+T (press Cmd+T for MAC OS X). Select a type from the list.</li><li>On a diagram, select a port and in the smart manipulator toolbar, click the Specify Type button. Select a type from the list.</li><li>In the port <ac:link><ri:page ri:space-key="MT" ri:content-title="Specification window" /></ac:link>, <strong>Type</strong> property specification cell, select a type.</li></ul><h3>Displaying Port type</h3><p>To show the Port type, do one of the following</p><hr /><ul><li>Select a port, and from the shortcut menu, choose <strong>Show Type</strong>.</li><li>In the port <ac:link><ri:page ri:space-key="MT" ri:content-title="Symbol Properties dialog" /></ac:link>, set the <strong>Show Type</strong> property to true.</li></ul><h3>Displaying Ports on shapes</h3><p>To display Ports on shapes</p><hr /><ol><li>Right-click the shape, select <strong>Display</strong> &gt;<strong> Display Parts/Ports</strong>. The <strong>Display Parts/Ports</strong> dialog opens.</li><li><p>Select ports you want to display on the shape:<br />- On the left side of the dialog, select ports manually.<br />- On the right side of the dialog, use the panel to select all or particular types of properties or ports.</p></li><li>Click <strong>OK</strong> when you are done.</li></ol><p><br /></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="e835cff2-9a5a-4b26-a0d4-959f0c196afd"><ac:rich-text-body><ul><li>The port type near the port symbol is displayed if port has referenced type, but has no name.</li><li>The port type near the port symbol is not displayed if type is provided or required interface and the interface is displayed on the diagram.</li><li>When a part symbol is created, all its ports are displayed on the diagram.</li></ul></ac:rich-text-body></ac:structured-macro><h3>Creating a Port on a composite structure diagram frame</h3><p>To create a Port on a composite structure diagram frame</p><hr /><ol><li>Select an element and from the smart manipulator toolbar, choose the <strong>Connector</strong> button.</li><li>Click the composite structure diagram frame. The port is created and the Select Port list is displayed.</li><li>Select one of the following:<ul><li>A hidden port or a nested port of the composite structure diagram.</li><li><strong>New Port</strong> - click to create a port on a diagram frame, with the same name, type and multiplicity, as it is set on the source part or port.</li><li><p><strong>Nested Port</strong> - click to create a new nested port.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="87826360-9593-420a-917f-c12457935856"><ac:rich-text-body><p>The <strong>Nested Port</strong> is available only when creating a connector from the nested port to the diagram frame.</p></ac:rich-text-body></ac:structured-macro></li></ul></li></ol><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="37361479-a0d4-489a-b7a2-a8bee53a9d04"><ac:rich-text-body><ul><li>You can also quickly <span>create </span>a port on the composite structure diagram frame when drawing a connector straight from a composite structure diagram frame.</li><li>If a connector is created from a port with the defined type, then only compatible hidden ports are listed in the <strong>Select Port</strong> list.</li><li>If a connector is created from a port that has interfaces, then ports that have compatible interfaces are listed in the <strong>Select Port</strong> list.</li></ul></ac:rich-text-body></ac:structured-macro><p><ac:image ac:title="Example of Port creation on Composite Structure diagram frame" ac:alt="Example of Port creation on Composite Structure diagram frame"><ri:attachment ri:filename="port_on_df.png" /></ac:image></p><p><br /></p><p><br /></p><p><ac:image ac:title="Example of drawing Connector to Composite Structure diagram frame" ac:alt="Example of drawing Connector to Composite Structure diagram frame"><ri:attachment ri:filename="port_on_df2.png" /></ac:image></p><h3>Displaying Port in compartment</h3><p>To display Ports in the element compartment</p><hr /><ol><li>On the diagram, select a symbol and click the Compartments button.</li><li>In the list, select <strong style="line-height: 1.42857;">Ports</strong>. The ports' compartment is displayed on a symbol.</li></ol><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="2e2de1f7-17fb-4761-bca9-d4114439bc17"><ac:rich-text-body><p>In the <strong>Compartment Edit</strong> dialog, you can select which ports to display in the ports' compartment.</p></ac:rich-text-body></ac:structured-macro><h3>Changing position of Port label</h3><p>To change position of Port label</p><hr /><ol><li>Right-click the Port shape and select the <strong>Symbol Properties</strong> command.</li><li>In the <ac:link><ri:page ri:space-key="MT" ri:content-title="Symbol Properties dialog" /></ac:link>, select the <strong>All</strong> property display mode.</li><li><p class="auto-cursor-target">Find the <strong>Position of Labels</strong> property and select on of the following value:<br /> - <strong>Outside</strong> to show the label outside the Port shape.<br /><ac:image><ri:attachment ri:filename="outside_port_label.png" /></ac:image><br /> - <strong>Inside</strong> to show labels inside the Port shape.<br /><ac:image ac:thumbnail="true" ac:height="77"><ri:attachment ri:filename="inside_port_shape.png" /></ac:image><br /> - <strong>Name and Type Labels Inside</strong> to show only the name and type inside the Port shape.<br /><ac:image ac:thumbnail="true" ac:height="77"><ri:attachment ri:filename="inside_port_shape.png" /></ac:image><br /> - <strong>Inside Enclosing Shape</strong> to show the label outside the Port shape but inside enclosing shape on which boundary the port is created.</p><ac:structured-macro ac:name="warning" ac:schema-version="1" ac:macro-id="eb02b1f7-3bbc-4db3-825b-da08343e5250"><ac:rich-text-body><p>Nested ports do not support <strong>Inside Enclosing Shape</strong> value.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /><ac:image><ri:attachment ri:filename="inside_enclosing_shape_port_label.png" /></ac:image><br />  </p></li></ol><h3>Specifying the Provided/Required Interfaces for a Port</h3><p>To specify the Provided/Required Interfaces for a Port even if the Port type is not specified</p><hr /><ol><li>In the Port <ac:link><ri:page ri:space-key="MT" ri:content-title="Specification window" /></ac:link>, <strong>Provided/Required Interfaces</strong> property group, click the <strong>Add</strong> button.</li><li>Select to either provided or required interface.</li><li>In the case, when the port type is not specified, the <strong>Select Port Type</strong> dialog is displayed. Select one of the following options:<ul><li>Set provided interface as a port type (available only when creating a provided interface). The provided interface will be specified as the port type.</li><li>Create &quot;dummy&quot; port type automatically. Create a “dummy” port type and relations between the type and interface.</li><li>Select or create a port type manually. The <strong>Select Port Type</strong> dialog will open, to allow you to select or create a Port.</li></ul></li><li>In the element Selection dialog, select or create an interface and click <strong>OK</strong>.</li></ol><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="4e5352cb-91b3-4955-996a-1b0c0b7e26fb"><ac:rich-text-body><ul><li>Draw a realize relationship from a port to an interface to create a provided interface. </li><li>Draw a usage relationship from a port to an interface to create a required interface.</li></ul></ac:rich-text-body></ac:structured-macro><h3>Converting a Port to an Association</h3><p>To convert a Port to an Association, do one of the following</p><hr /><ul><li>From the port's shortcut menu, select <strong>Refactor </strong>&gt;<strong> Convert To</strong> &gt; <strong>Association</strong>.</li><li>In the port's compartment, select a port and drag it out of the shape.</li></ul><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="194e0e3c-5a02-4666-b3a9-2949ed9f4c94"><ac:rich-text-body><p>You can convert a port to an association, only if the port type is specified and a port is not a member of any <span>association end.</span></p></ac:rich-text-body></ac:structured-macro><h3>Displaying a Port name in a signature on a shape</h3><p>To display a Port name in a signature on a shape</p><hr /><ul><li>In the <ac:link><ri:page ri:space-key="MT" ri:content-title="Symbol Properties dialog" /><ac:link-body><strong>Symbol Properties</strong> dialog</ac:link-body></ac:link>, click to select the <strong>Show Port</strong> property.</li></ul><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="6d0485ea-60c7-4ba9-b086-9c610eba1a3d"><ac:rich-text-body><p>If you cannot find the <strong>Show Port</strong> property in the <ac:link><ri:page ri:space-key="MT" ri:content-title="Symbol Properties dialog" /><ac:link-body><strong>Symbol Properties</strong> dialog</ac:link-body></ac:link>, change the properties display mode to <em>Expert</em> or <em>All</em>.</p></ac:rich-text-body></ac:structured-macro><p><br /></p><p>You can display the Port name on the following shapes: <br />• Call Operation Action, Call Behavior Action, Send Signal Action, Send Object Action, Broadcast Signal Action, and Start Object Behavior Action. <br />For example: via &lt;Port name&gt;.</p><p><ac:image><ri:attachment ri:filename="via_port_name.png" /></ac:image><br />• Transition, Protocol Transition, State, and Accept Event Action.<br />For example: « from» &lt;Port name&gt;.</p><h3>Hiding the multiplicity</h3><p>To hide the multiplicity next to the Port's type</p><hr /><ol><li>Right-click the Port shape and select Symbol Properties.</li><li>In the <strong>Symbol Properties</strong> dialog, set the <strong>Show Multiplicity</strong> property value to <em>false</em>.</li><li>Click <strong>Close</strong>.</li></ol><p class="auto-cursor-target"><br /></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="4fdc35cf-fa2d-4a95-a4ff-fee9971b192e"><ac:parameter ac:name="id">230618171</ac:parameter><ac:rich-text-body><p class="auto-cursor-target"><strong>Related pages</strong></p><ul><li><ac:link><ri:page ri:space-key="MT" ri:content-title="Displaying parts and ports" /></ac:link></li><li><ac:link><ri:page ri:content-title="UML elements" /><ac:plain-text-link-body><![CDATA[Model Elements]]></ac:plain-text-link-body></ac:link></li><li><ac:link><ri:page ri:space-key="MT" ri:content-title="Specification window" /><ac:plain-text-link-body><![CDATA[Specification Window]]></ac:plain-text-link-body></ac:link></li></ul><p class="auto-cursor-target"><br /></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=228986025 space=MED version=2 -->
## PAGE 00329: Post

- page_id: `228986025`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/228986025/Post
- version_number: 2
- version_date: `2025-05-14T10:30:58.511+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UAF 1.3 elements
- labels: []

### NORMALIZED CONTENT

**Description**

Post denote a type of job title or position that a person can fill (e.g. Lawyer, Solution Architect, Machine Operator or Chief Executive Officer).

**Architecture Framework**

UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0

**Extension**

UML Class

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description</strong></p><p>Post denote a type of job title or position that a person can fill (e.g. Lawyer, Solution Architect, Machine Operator or Chief Executive Officer).</p><p><strong>Architecture Framework</strong></p><p><span style="color: rgb(62,63,64);">UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0</span></p><p><strong>Extension</strong></p><p>UML Class</p><p><br /></p>
````

<!--NOMAGIC_PAGE id=228986026 space=MED version=2 -->
## PAGE 00330: Presented By

- page_id: `228986026`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/228986026/Presented+By
- version_number: 2
- version_date: `2025-05-14T10:30:58.902+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UAF 1.3 elements
- labels: []

### NORMALIZED CONTENT

**Description**

A dependency relationship denoting that a Challenge must be overcome for addressing a Driver.

**Architecture Framework**

UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0

**Extensions**

Dependency

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description</strong></p><p class="OMGNormalParagraph">A dependency relationship denoting that a Challenge must be overcome for addressing a Driver.</p><p><strong>Architecture Framework</strong></p><p><span style="color: rgb(62,63,64);">UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0</span></p><p><strong>Extensions</strong></p><p>Dependency</p>
````

<!--NOMAGIC_PAGE id=243967622 space=MED version=1 -->
## PAGE 00331: Primitive

- page_id: `243967622`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/243967622/Primitive
- version_number: 1
- version_date: `2025-07-31T10:50:37.091+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UML elements > Data Type
- labels: []

### NORMALIZED CONTENT

A Primitive defines a predefined [CONFLUENCE_PAGE title='Data Type' space=''] without possessing any relevant UML substructure; that is, it has no UML parts. A Primitive data type can have an algebra as well as operations defined outside of UML (for example, mathematically). The Primitive data types used in UML include Integer, Unlimited Integer, Real, and String.

#### PANEL: Related Pages

Related Pages

- [CONFLUENCE_PAGE title='UML elements' space='']
- [CONFLUENCE_PAGE title='Class diagram' space='MT']
- [CONFLUENCE_PAGE title='Use Case' space='']
- [CONFLUENCE_PAGE title='Use Case diagram' space='MT']
- [CONFLUENCE_PAGE title='Sequence diagram' space='MT']
- [CONFLUENCE_PAGE title='Activity diagram' space='MT']
- [CONFLUENCE_PAGE title='Data Type' space='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p>A Primitive defines a predefined <ac:link><ri:page ri:content-title="Data Type" /></ac:link> without possessing any relevant UML substructure; that is, it has no UML parts. A Primitive data type can have an algebra as well as operations defined outside of UML (for example, mathematically). The Primitive data types used in UML include Integer, Unlimited Integer, Real, and String.</p></ac:layout-cell><ac:layout-cell><p><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="1b2025c5-70c1-47b6-9a1b-4fb242548002"><ac:parameter ac:name="title">Related Pages</ac:parameter><ac:rich-text-body><ul><li><ac:link><ri:page ri:content-title="UML elements" /><ac:plain-text-link-body><![CDATA[Model Elements]]></ac:plain-text-link-body></ac:link></li><li><ac:link><ri:page ri:space-key="MT" ri:content-title="Class diagram" /><ac:plain-text-link-body><![CDATA[Class diagrams]]></ac:plain-text-link-body></ac:link></li><li><ac:link><ri:page ri:content-title="Use Case" /></ac:link></li><li><ac:link><ri:page ri:space-key="MT" ri:content-title="Use Case diagram" /></ac:link></li><li><ac:link><ri:page ri:space-key="MT" ri:content-title="Sequence diagram" /></ac:link></li><li><ac:link><ri:page ri:space-key="MT" ri:content-title="Activity diagram" /></ac:link></li><li><ac:link><ri:page ri:content-title="Data Type" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=228986027 space=MED version=2 -->
## PAGE 00332: Problem Domain

- page_id: `228986027`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/228986027/Problem+Domain
- version_number: 2
- version_date: `2025-05-14T10:30:59.351+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UAF 1.3 elements
- labels: []

### NORMALIZED CONTENT

**Description**

A property associated with a logical architecture, used to specify the scope of the problem.

**Architecture** **Framework**

UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0

**Extension**

UML Property

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="OMGNormalParagraph"><strong>Description</strong></p><p class="OMGNormalParagraph">A property associated with a logical architecture, used to specify the scope of the problem.</p><p class="OMGNormalParagraph"><span class="fontstyle0"><strong>Architecture</strong> <strong>Framework</strong></span></p><p class="OMGNormalParagraph"><span style="color: rgb(62,63,64);">UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0</span></p><p class="OMGNormalParagraph"><strong>Extension</strong></p><p class="OMGNormalParagraph">UML Property</p><p><br /></p>
````

<!--NOMAGIC_PAGE id=243967906 space=MED version=3 -->
## PAGE 00333: Profile

- page_id: `243967906`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/243967906/Profile
- version_number: 3
- version_date: `2025-09-13T12:44:16.691+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UML elements
- labels: []

### NORMALIZED CONTENT

852159285

INLINE

852159288

INLINE

852159287

INLINE

A Profile is a kind of a package that extends a reference metamodel. The primary extension construct is a stereotype. Stereotypes are defined as a part of profiles.

A profile introduces several constraints or restrictions to ordinary metamodeling. Constraints and restrictions are realized using metaclasses defined in the package. It is a restricted form of a metamodel that always must be related to a reference metamodel, such as UML, as it is described below. It cannot be used without its reference metamodel, and it defines a limited capability to extend metaclasses of the reference metamodel. The extensions are defined as stereotypes that apply to the existing metaclasses.

Each profile contains a set of stereotypes. Profiles are defined as separate modules. Profiles are loaded on demand, that is when you start or open your project only profiles used in that project are loaded.

Profiles are defined using the UML extensibility mechanisms that allow modelers to customize UML for specific domains, for example, for software development processes. The mechanism of the profile is similar to the functionality of modules.

The program comes with some predefined profiles: UML Standard Profile, DDL, EDOC, and other. All profiles are stored in *<modeling tool installation directory>\profiles*.

###### Profile Properties

The profile is defined as a [CONFLUENCE_PAGE title='Package' space=''], that is, it has package properties.

You can specify profile properties in the profile's [CONFLUENCE_PAGE title='Specification window' space='MT']. You can also find descriptions of each [CONFLUENCE_PAGE title='Editing property values' space='MT'] in this window. Descriptions are provided in the description area below the property list.

For more information, see the [CONFLUENCE_PAGE title='UML Profiling and DSL Guide' space='MT'] section.

###### Creating Profiles

You can create a profile in one of the following ways:

- 
- 
- 
- 

ShortcutTo create a profile using the package / model / profile shortcut menu

1. In the Containment tree, select a package, a model, or another profile, wherein you want to create the new profile.
2. From the [CONFLUENCE_PAGE title='DH Links panel shortcut menu and Sync Status icons' space='CDH'] of the selected package, model, or profile, select Create Element > Profile . [ATTACHMENT filename='creating_profiles.png'] If the Profile element is not displayed in the **Create Element**menu, enable the **Expert**mode.[IMAGE alt='' src='']

Profile DiagramTo create a profile using the profile diagram palette

1. Either create a new [CONFLUENCE_PAGE title='Profile diagram' space='MT'] or open an existing one.
2. On the diagram palette, click the Profile button.
3. Click a free space on the diagram pane to see the created Profile.

Package DiagramTo create a profile using the package diagram palette

1. Either create a new [CONFLUENCE_PAGE title='Package diagram' space='MT'] or open an existing one.
2. On the diagram palette, click the Package arrow to see more buttons.
3. Click the Profile button.
4. Click a free space of the diagram pane to see the created Profile.

Class DiagramTo create a profile using the class diagram palette

1. Either create a new [CONFLUENCE_PAGE title='Class diagram' space='MT'] or open an existing one.
2. On the Class diagram palette, do one of the following:
  - Expand the Profile Diagram button group and click the Profile button.
  - Expand the Package Diagram button group, click the Package arrow to see more buttons, and then click the Profile button.
3. Click a free space of the diagram pane to see the created Profile.

852159284

INLINE

**Related pages**

- Model Elements
- Stereotype
- Package
- Working with Profiles

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="303a2437-98a0-4690-924e-1046ad9a23f2"><ac:parameter ac:name="id">852159285</ac:parameter><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="a1b04124-c501-4825-9ec5-a9ae72e02ba2"><ac:parameter ac:name="id">852159288</ac:parameter><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="7ef85520-69b2-4d3d-a66c-4beed309df16"><ac:parameter ac:name="id">852159287</ac:parameter><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p>A Profile is a kind of a package that extends a reference metamodel. The primary extension construct is a stereotype. Stereotypes are defined as a part of profiles.</p><p>A profile introduces several constraints or restrictions to ordinary metamodeling. Constraints and restrictions are realized using metaclasses defined in the package. It is a restricted form of a metamodel that always must be related to a reference metamodel, such as UML, as it is described below. It cannot be used without its reference metamodel, and it defines a limited capability to extend metaclasses of the reference metamodel. The extensions are defined as stereotypes that apply to the existing metaclasses.</p><p>Each profile contains a set of stereotypes. Profiles are defined as separate modules. Profiles are loaded on demand, that is when you start or open your project only profiles used in that project are loaded.</p><p>Profiles are defined using the UML extensibility mechanisms that allow modelers to customize UML for specific domains, for example, for software development processes. The mechanism of the profile is similar to the functionality of modules.</p><p>The program comes with some predefined profiles: UML Standard Profile, DDL, EDOC, and other. All profiles are stored in <em>&lt;modeling tool installation directory&gt;\profiles</em>.</p><h4>Profile Properties</h4><p><span>The profile is defined as a <ac:link><ri:page ri:content-title="Package" /><ac:plain-text-link-body><![CDATA[package]]></ac:plain-text-link-body></ac:link>, that is, it has package properties.</span></p><p>You can specify profile properties in the profile's <ac:link><ri:page ri:space-key="MT" ri:content-title="Specification window" /></ac:link>. You can also find descriptions of each <ac:link><ri:page ri:space-key="MT" ri:content-title="Editing property values" /><ac:plain-text-link-body><![CDATA[property]]></ac:plain-text-link-body></ac:link> in this window. Descriptions are provided in the description area below the property list. </p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="bc009266-3691-4340-a5fd-8fbbd7dfa635"><ac:rich-text-body><p>For more information, see the <ac:link><ri:page ri:space-key="MT" ri:content-title="UML Profiling and DSL Guide" /></ac:link> section.</p></ac:rich-text-body></ac:structured-macro><h4>Creating Profiles</h4><p><span>You can create a profile in one of the following ways:</span></p><ul><li><span><ac:link ac:anchor="Shortcut"><ac:plain-text-link-body><![CDATA[Using the package / model / profile shortcut menu]]></ac:plain-text-link-body></ac:link></span></li><li><span><ac:link ac:anchor="Profile Diagram"><ac:plain-text-link-body><![CDATA[Using the profile diagram palette]]></ac:plain-text-link-body></ac:link></span></li><li><ac:link ac:anchor="Package Diagram"><ac:plain-text-link-body><![CDATA[Using the package diagram palette]]></ac:plain-text-link-body></ac:link></li><li><ac:link ac:anchor="Class Diagram"><ac:plain-text-link-body><![CDATA[Using the class diagram palette]]></ac:plain-text-link-body></ac:link></li></ul><p><br /></p><p><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="95bb83e9-c965-41eb-8de8-f02a23720689"><ac:parameter ac:name="">Shortcut</ac:parameter></ac:structured-macro>To create a profile using the package / model / profile shortcut menu</p><hr /><ol><li>In the Containment tree, select a package, a model, or another profile, wherein you want to create the new profile.</li><li>From the <ac:link><ri:page ri:space-key="CDH" ri:content-title="DH Links panel shortcut menu and Sync Status icons" /><ac:plain-text-link-body><![CDATA[shortcut menu]]></ac:plain-text-link-body></ac:link> of the selected package, model, or profile, select <strong>Create Element</strong> &gt; <strong>Profile</strong>.<br /><ac:image><ri:attachment ri:filename="creating_profiles.png" /></ac:image><br /><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="3c49aae6-973c-452c-ba31-74c6653d834d"><ac:rich-text-body><p>If the Profile element is not displayed in the <strong>Create Element </strong>menu, enable the <strong>Expert </strong>mode.</p><p><ac:image><ri:attachment ri:filename="expert_mode.png" /></ac:image></p></ac:rich-text-body></ac:structured-macro></li></ol><p><br /></p><p><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="ce6066c0-81b6-4c04-a709-f78facf6bef0"><ac:parameter ac:name="">Profile Diagram</ac:parameter></ac:structured-macro>To create a profile using the profile diagram palette</p><hr /><ol><li>Either create a new <ac:link><ri:page ri:space-key="MT" ri:content-title="Profile diagram" /></ac:link> or open an existing one.</li><li>On the diagram palette, click the <strong>Profile</strong> button.</li><li>Click a free space on the diagram pane to see the created Profile.</li></ol><p><br /></p><p><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="2255e7cd-a7e4-4794-baf3-8f5f23a927eb"><ac:parameter ac:name="">Package Diagram</ac:parameter></ac:structured-macro>To create a profile using the package diagram palette</p><hr /><ol><li>Either create a new <ac:link><ri:page ri:space-key="MT" ri:content-title="Package diagram" /></ac:link> or open an existing one.</li><li>On the diagram palette, click the <strong>Package</strong> arrow to see more buttons.</li><li>Click the <strong>Profile</strong> button.</li><li>Click a free space of the diagram pane to see the created Profile.</li></ol><p><br /></p><p><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="538cedcb-1ba6-482f-8a71-f2cc5027a5d7"><ac:parameter ac:name="">Class Diagram</ac:parameter></ac:structured-macro>To create a profile using the class diagram palette</p><hr /><ol><li>Either create a new <ac:link><ri:page ri:space-key="MT" ri:content-title="Class diagram" /></ac:link> or open an existing one. </li><li>On the Class diagram palette, do one of the following:<ul><li>Expand the Profile Diagram button group and click the <strong>Profile</strong> button.</li><li>Expand the Package Diagram button group, click the <strong>Package</strong> arrow to see more buttons, and then click the <strong>Profile</strong> button.</li></ul></li><li>Click a free space of the diagram pane to see the created Profile.</li></ol><p><br /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p><br /></p></ac:layout-cell><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section></ac:layout></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="7174b91b-b356-4d3e-8f02-f67e1b7a3eff"><ac:parameter ac:name="id">852159284</ac:parameter><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><p class="ancestor-link parent-link"><strong>Related pages</strong></p><ul><li class="ancestor-link parent-link"><a href="https://docs.nomagic.com/display/MT/Model+elements">Model Elements</a></li><li><a href="https://docs.nomagic.com/display/MT/Stereotype">Stereotype</a></li><li><a href="https://docs.nomagic.com/display/MT/Package">Package</a></li><li><a href="https://docs.nomagic.com/display/MT/Working+with+Profiles">Working with Profiles</a></li></ul></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=243967910 space=MED version=1 -->
## PAGE 00334: Profile Application

- page_id: `243967910`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/243967910/Profile+Application
- version_number: 1
- version_date: `2025-07-31T10:50:45.021+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UML elements
- labels: []

### NORMALIZED CONTENT

A profile application is used to show which profiles have been applied to a package.

Specify the Profile Application element, in the [CONFLUENCE_PAGE title='Specification window' space='MT'] dialog.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><span style="color: rgb(0,0,0);">A profile application is used to show which profiles have been applied to a package.</span></p><p>Specify the Profile Application element, in the <ac:link><ri:page ri:space-key="MT" ri:content-title="Specification window" /><ac:plain-text-link-body><![CDATA[Specification]]></ac:plain-text-link-body></ac:link> dialog.</p>
````

<!--NOMAGIC_PAGE id=228986028 space=MED version=2 -->
## PAGE 00335: Project

- page_id: `228986028`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/228986028/Project
- version_number: 2
- version_date: `2025-05-14T10:30:59.840+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UAF 1.3 elements
- labels: []

### NORMALIZED CONTENT

**Description**

An element that describes types of time-limited endeavors that are required to meet one or more Capability needs.

**Architecture** **Framework**

UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0

**Extensions**

UML Class

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="OMGBoldBulletKeepNextParagraph"><strong>Description</strong></p><p class="OMGNormalParagraph">An element that describes types of time-limited endeavors that are required to meet one or more Capability needs. </p><p class="OMGNormalParagraph"><span class="fontstyle0"><strong>Architecture</strong> <strong>Framework</strong></span></p><p class="OMGNormalParagraph"><span style="color: rgb(62,63,64);">UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0</span></p><p class="OMGNormalParagraph"><strong><span class="fontstyle0">Extensions</span></strong></p><p class="OMGNormalParagraph"><span class="fontstyle2">UML Class</span></p><p><br /></p>
````

<!--NOMAGIC_PAGE id=228986029 space=MED version=2 -->
## PAGE 00336: Project Activity

- page_id: `228986029`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/228986029/Project+Activity
- version_number: 2
- version_date: `2025-05-14T10:31:00.234+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UAF 1.3 elements
- labels: []

### NORMALIZED CONTENT

**Description**

An activity carried out during a project.

**Architecture Framework**

UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0

**Extension**

Activity

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description </strong></p><p>An activity carried out during a project.</p><p><strong>Architecture Framework</strong></p><p><span style="color: rgb(62,63,64);">UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0</span></p><p><strong>Extension</strong></p><p>Activity</p>
````

<!--NOMAGIC_PAGE id=228986030 space=MED version=2 -->
## PAGE 00337: Project Activity Action

- page_id: `228986030`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/228986030/Project+Activity+Action
- version_number: 2
- version_date: `2025-05-14T10:31:00.607+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UAF 1.3 elements
- labels: []

### NORMALIZED CONTENT

**Description**

The ProjectActivityAction is defined as a call behavior action that invokes the activity that needs to be preformed.

**Architecture Framework**

UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0

**Extension**

Call Behavior Action, Activity

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description </strong></p><p>The ProjectActivityAction is defined as a call behavior action that invokes the activity that needs to be preformed.</p><p><strong>Architecture Framework</strong></p><p><span style="color: rgb(62,63,64);">UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0</span></p><p><strong>Extension</strong></p><p>Call Behavior Action, Activity</p>
````

<!--NOMAGIC_PAGE id=228986031 space=MED version=2 -->
## PAGE 00338: Project Kind

- page_id: `228986031`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/228986031/Project+Kind
- version_number: 2
- version_date: `2025-05-14T10:31:01.304+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UAF 1.3 elements
- labels: []

### NORMALIZED CONTENT

**Description**

Enumeration of the possible kinds of project applicable to an ActualProject. Its enumeration literals are:

- Programme - Indicates that the ActualProject associated with the ProjectKind is an undertaking that is a temporary, flexible organization created to co-ordinate, direct and oversee the implementation of a set of related Projects and Tasks in order to deliver outcomes and benefits related to the organization’s strategic objectives. A programme is likely to have a lifespan of several years. During a programme lifecycle, projects are initiated, executed, and closed. Programmes provide an umbrella under which these projects can be co-ordinated. The programme integrates the projects so that it can deliver an outcome greater than the sum of its parts.
- Portfolio - Indicates that the ActualProject associated with the ProjectKind is an undertaking comprised of the Projects and Programmes that are the totality of an organization's investment (or segment thereof) in the changes required to achieve its strategic objectives.
- Project - Indicates that the ActualProject associated with the ProjectKind is an undertaking that is a time-limited endeavor to create a specific set of products or services.
- PersonnelDevelopment - Indicates that the ActualProject associated with the ProjectKind is an undertaking that relates to the training and enablement of personnel to enable them help achieve the organizations objectives.

**Architecture Framework**

UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="OMGBoldBulletKeepNextParagraph"><strong>Description</strong></p><p class="OMGNormalParagraph">Enumeration of the possible kinds of project applicable to an ActualProject. Its enumeration literals are:</p><ul><li>Programme - Indicates that the ActualProject associated with the ProjectKind is an undertaking that is a temporary, flexible organization created to co-ordinate, direct and oversee the implementation of a set of related Projects and Tasks in order to deliver outcomes and benefits related to the organization’s strategic objectives. A programme is likely to have a lifespan of several years. During a programme lifecycle, projects are initiated, executed, and closed. Programmes provide an umbrella under which these projects can be co-ordinated. The programme integrates the projects so that it can deliver an outcome greater than the sum of its parts.</li><li>Portfolio - Indicates that the ActualProject associated with the ProjectKind is an  undertaking comprised of the Projects and Programmes that are the totality of an organization's investment (or segment thereof) in the changes required to achieve its strategic objectives.</li><li>Project - Indicates that the ActualProject associated with the ProjectKind is an undertaking that is a time-limited endeavor to create a specific set of products or services.</li><li>PersonnelDevelopment - Indicates that the ActualProject associated with the ProjectKind is an undertaking that relates to the training and enablement of personnel to enable them help achieve the organizations objectives.</li></ul><p><strong>Architecture Framework</strong></p><p><span style="color: rgb(62,63,64);">UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0</span></p><p><br /></p>
````

<!--NOMAGIC_PAGE id=228986032 space=MED version=2 -->
## PAGE 00339: Project Milestone

- page_id: `228986032`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/228986032/Project+Milestone
- version_number: 2
- version_date: `2025-05-14T10:31:01.754+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UAF 1.3 elements
- labels: []

### NORMALIZED CONTENT

**Description**

A type of event in a Project by which progress is measured.

**Architecture Framework**

UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0

**Extension**

UML Class

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="OMGBoldBulletKeepNextParagraph"><strong>Description</strong></p><p>A type of event in a Project by which progress is measured.</p><p><strong>Architecture Framework</strong></p><p><span style="color: rgb(62,63,64);">UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0</span></p><p><strong>Extension</strong></p><p>UML Class</p><p><br /></p>
````

<!--NOMAGIC_PAGE id=228986033 space=MED version=2 -->
## PAGE 00340: Project Milestone Role

- page_id: `228986033`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/228986033/Project+Milestone+Role
- version_number: 2
- version_date: `2025-05-14T10:31:02.080+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UAF 1.3 elements
- labels: []

### NORMALIZED CONTENT

**Description**

The role played by a Project Milestone in the context of a Project.

**Architecture Framework**

UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0

**Extensions**

UML Property

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong><span class="fontstyle0">Description</span></strong></p><p class="OMGNormalParagraph">The role played by a Project Milestone in the context of a Project. </p><p><strong><span class="fontstyle0">Architecture Framework</span></strong></p><p><span style="color: rgb(62,63,64);">UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0</span></p><p><strong><span class="fontstyle0">Extensions</span></strong></p><p><span class="fontstyle1">UML Property</span></p><p><br /></p>
````

<!--NOMAGIC_PAGE id=228986034 space=MED version=2 -->
## PAGE 00341: Project Role

- page_id: `228986034`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/228986034/Project+Role
- version_number: 2
- version_date: `2025-05-14T10:31:02.314+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UAF 1.3 elements
- labels: []

### NORMALIZED CONTENT

**Description**

Usage of a Project in the context of another Project. Creates a whole-part relationship.

**Architecture Framework**

UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0

**Extension**

UML Property

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="OMGBoldBulletKeepNextParagraph"><strong>Description</strong></p><p class="OMGNormalParagraph">Usage of a Project in the context of another Project. Creates a whole-part relationship.</p><p class="OMGNormalParagraph"><strong><span class="fontstyle0">Architecture Framework</span></strong></p><p class="OMGNormalParagraph"><span style="color: rgb(62,63,64);">UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0</span></p><p class="OMGNormalParagraph"><strong>Extension</strong></p><p class="OMGNormalParagraph">UML Property</p><p><br /></p>
````

<!--NOMAGIC_PAGE id=228986035 space=MED version=2 -->
## PAGE 00342: Project Sequence

- page_id: `228986035`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/228986035/Project+Sequence
- version_number: 2
- version_date: `2025-05-14T10:31:02.695+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UAF 1.3 elements
- labels: []

### NORMALIZED CONTENT

**Description**

A dependency relationship between two Actual Projects that denotes one Actual Project cannot start before the previous Actual Project is finished.

**Architecture Framework**

UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0

**Extension**

UML Dependency

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="OMGNormalParagraph"><strong>Description</strong></p><p class="OMGNormalParagraph">A dependency relationship between two Actual Projects that denotes one Actual Project cannot start before the previous Actual Project is finished. </p><p class="OMGNormalParagraph"><strong><span class="fontstyle0">Architecture Framework</span></strong></p><p class="OMGNormalParagraph"><span style="color: rgb(62,63,64);">UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0</span></p><p class="OMGNormalParagraph"><strong>Extension</strong></p><p class="OMGNormalParagraph">UML Dependency</p><p><br /></p>
````

<!--NOMAGIC_PAGE id=228986036 space=MED version=2 -->
## PAGE 00343: Project Status

- page_id: `228986036`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/228986036/Project+Status
- version_number: 2
- version_date: `2025-05-14T10:31:02.995+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UAF 1.3 elements
- labels: []

### NORMALIZED CONTENT

**Description**

The status (i.e. level of progress) of a Project Theme for an Actual Project at the time of the Actual Project Milestone.

**Architecture Framework**

UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0

**Extension**

UML Slot

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description</strong></p><p class="OMGNormalParagraph">The status (i.e. level of progress) of a Project Theme for an Actual Project at the time of the Actual Project Milestone.</p><p class="OMGNormalParagraph"><strong><span class="fontstyle0">Architecture Framework</span></strong></p><p class="OMGNormalParagraph"><span style="color: rgb(62,63,64);">UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0</span></p><p class="OMGNormalParagraph"><strong>Extension</strong></p><p class="OMGNormalParagraph">UML Slot</p><p><br /></p>
````

<!--NOMAGIC_PAGE id=228986037 space=MED version=2 -->
## PAGE 00344: Project Theme

- page_id: `228986037`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/228986037/Project+Theme
- version_number: 2
- version_date: `2025-05-14T10:31:03.307+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UAF 1.3 elements
- labels: []

### NORMALIZED CONTENT

**Description**

A property of a Project Milestone that captures an aspect by which the progress of Actual Projects may be measured.

**Architecture Framework**

UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0

**Extension**

UML Property

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="OMGNormalParagraph"><strong>Description</strong></p><p>A property of a Project Milestone that captures an aspect by which the progress of Actual Projects may be measured.</p><p><strong><span class="fontstyle0">Architecture Framework</span></strong></p><p><span style="color: rgb(62,63,64);">UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0</span></p><p><strong>Extension</strong></p><p>UML Property</p><p><br /></p>
````

<!--NOMAGIC_PAGE id=228986038 space=MED version=2 -->
## PAGE 00345: Property Set

- page_id: `228986038`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/228986038/Property+Set
- version_number: 2
- version_date: `2025-05-14T10:31:03.650+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UAF 1.3 elements
- labels: []

### NORMALIZED CONTENT

**Description**

An abstract grouping of architectural elements that can own Measurements.

**Architecture** **Framework**

UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0

**Extension**

Element

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="OMGNormalParagraph"><strong>Description</strong></p><p class="OMGNormalParagraph">An abstract grouping of architectural elements that can own Measurements. </p><p class="OMGNormalParagraph"><strong>Architecture</strong> <strong>Framework</strong></p><p class="OMGNormalParagraph"><span style="color: rgb(62,63,64);">UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0</span></p><p class="OMGNormalParagraph"><strong>Extension</strong></p><p class="OMGNormalParagraph">Element</p><p><br /></p>
````

<!--NOMAGIC_PAGE id=228986039 space=MED version=2 -->
## PAGE 00346: Protects

- page_id: `228986039`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/228986039/Protects
- version_number: 2
- version_date: `2025-05-14T10:31:04.866+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UAF 1.3 elements
- labels: []

### NORMALIZED CONTENT

**Description**

A dependency that asserts that a Security Control is required to protect an Asset.

**Architecture Framework**

UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0

**Extension**

UML Dependency

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="OMGNormalParagraph"><strong>Description</strong></p><p class="OMGNormalParagraph">A dependency that asserts that a Security Control is required to protect an Asset.</p><p class="OMGNormalParagraph"><strong>Architecture Framework</strong></p><p class="OMGNormalParagraph"><span style="color: rgb(62,63,64);">UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0</span></p><p class="OMGNormalParagraph"><strong>Extension</strong></p><p class="OMGNormalParagraph">UML Dependency</p><p><br /></p>
````

<!--NOMAGIC_PAGE id=228986040 space=MED version=2 -->
## PAGE 00347: Protects In Context

- page_id: `228986040`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/228986040/Protects+In+Context
- version_number: 2
- version_date: `2025-05-14T10:31:05.096+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UAF 1.3 elements
- labels: []

### NORMALIZED CONTENT

**Description**

A dependency relationship that relates a Security Control Action to a Operational Role, or a Resource Role. It indicates that Security Control is required to protect an Asset in a specific context or configuration.

**Architecture Framework**

UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0

**Extension**

UML Dependency

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="OMGNormalParagraph"><strong>Description</strong></p><p class="OMGNormalParagraph">A dependency relationship that relates a Security Control Action to a Operational Role, or a Resource Role. It indicates that Security Control is required to protect an Asset in a specific context or configuration. </p><p class="OMGNormalParagraph"><strong>Architecture Framework</strong></p><p class="OMGNormalParagraph"><span style="color: rgb(62,63,64);">UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0</span></p><p class="OMGNormalParagraph"><strong>Extension</strong></p><p class="OMGNormalParagraph">UML Dependency</p><p><br /></p>
````

<!--NOMAGIC_PAGE id=228986041 space=MED version=2 -->
## PAGE 00348: Protocol

- page_id: `228986041`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/228986041/Protocol
- version_number: 2
- version_date: `2025-05-14T10:31:05.462+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UAF 1.3 elements
- labels: []

### NORMALIZED CONTENT

**Description**

A Standard for communication over a network. Protocols may be composite, represented as a Protocol Stack made up of Protocol Layers.

**Architecture** **Framework**

UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0

**Extension**

UML Class

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="OMGNormalParagraph"><strong>Description</strong></p><p class="OMGNormalParagraph">A Standard for communication over a network. Protocols may be composite, represented as a Protocol Stack made up of Protocol Layers. </p><p class="OMGNormalParagraph"><strong>Architecture</strong> <strong>Framework</strong></p><p class="OMGNormalParagraph"><span style="color: rgb(62,63,64);">UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0</span></p><p class="OMGNormalParagraph"><strong>Extension</strong></p><p class="OMGNormalParagraph">UML Class</p><p><br /></p>
````

<!--NOMAGIC_PAGE id=228986042 space=MED version=2 -->
## PAGE 00349: Protocol Implementation

- page_id: `228986042`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/228986042/Protocol+Implementation
- version_number: 2
- version_date: `2025-05-14T10:31:05.788+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UAF 1.3 elements
- labels: []

### NORMALIZED CONTENT

**Description**

An abstract grouping of architectural elements that can implement Protocols.

**Architecture** **Framework**

UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0

**Extension**

Element

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="OMGNormalParagraph"><strong>Description</strong></p><p class="OMGNormalParagraph">An abstract grouping of architectural elements that can implement Protocols.</p><p class="OMGNormalParagraph"><strong>Architecture</strong> <strong>Framework</strong></p><p class="OMGNormalParagraph"><span style="color: rgb(62,63,64);">UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0</span></p><p class="OMGNormalParagraph"><strong>Extension</strong></p><p class="OMGNormalParagraph">Element</p><p><br /></p>
````

<!--NOMAGIC_PAGE id=228986043 space=MED version=2 -->
## PAGE 00350: Protocol Layer

- page_id: `228986043`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/228986043/Protocol+Layer
- version_number: 2
- version_date: `2025-05-14T10:31:06.078+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UAF 1.3 elements
- labels: []

### NORMALIZED CONTENT

**Description**

Usage of a Protocol in the context of another Protocol. Creates a whole-part relationship.

**Architecture** **Framework**

UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0

**Extension**

UML Property

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="OMGNormalParagraph"><strong>Description</strong></p><p>Usage of a Protocol in the context of another Protocol. Creates a whole-part relationship.</p><p><strong>Architecture</strong> <strong>Framework</strong></p><p><span style="color: rgb(62,63,64);">UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0</span></p><p><strong>Extension</strong></p><p>UML Property</p><p><br /></p>
````

<!--NOMAGIC_PAGE id=228986044 space=MED version=2 -->
## PAGE 00351: Protocol Stack

- page_id: `228986044`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/228986044/Protocol+Stack
- version_number: 2
- version_date: `2025-05-14T10:31:06.341+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UAF 1.3 elements
- labels: []

### NORMALIZED CONTENT

**Description**

A sub-type of Protocol that contains the Protocol Layers, defining a complete stack.

**Architecture** **Framework**

UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0

**Extension**

UML Class

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="OMGNormalParagraph"><strong>Description</strong></p><p class="OMGNormalParagraph">A sub-type of Protocol that contains the Protocol Layers, defining a complete stack.</p><p class="OMGNormalParagraph"><strong>Architecture</strong> <strong>Framework</strong></p><p class="OMGNormalParagraph"><span style="color: rgb(62,63,64);">UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0</span></p><p class="OMGNormalParagraph"><strong>Extension</strong></p><p class="OMGNormalParagraph">UML Class</p><p><br /></p>
````

<!--NOMAGIC_PAGE id=243967729 space=MED version=1 -->
## PAGE 00352: Provided and Required Interfaces

- page_id: `243967729`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/243967729/Provided+and+Required+Interfaces
- version_number: 1
- version_date: `2025-07-31T10:50:40.122+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UML elements > Interface
- labels: []

### NORMALIZED CONTENT

The set of interfaces realized by a classifier is its provided interfaces, which represent the obligations that instances of that classifier have to their clients. They describe the services that the instances of that classifier offer to their clients.

The interfaces may also be used to specify required interfaces, which are specified by a usage dependency between the classifier and the corresponding interfaces. Required interfaces specify services that a classifier needs in order to perform its function and fulfill its own obligations to its clients.

To draw a Provided Interface

1. In the Class diagram, create a Class.
2. Select the Class shape and in the smart manipulator toolbar, click Interface Realization and then click on the diagram pane. The provided interface is created.
3. Select the interface shape, click the Compartments smart manipulator button, and then select Suppress All . Alternatively, click the Suppress All button in the diagram toolbar.

To draw a Required Interface

1. In the Class diagram, create a Class.
2. Select the Class shape and on the smart manipulator toolbar, click the Usage button and then click on the diagram. The required interface is created.
3. Select the interface shape, click the Compartments smart manipulator button, and then select Suppress All . Alternatively, click the Suppress All button in the diagram toolbar.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>The set of interfaces realized by a classifier is its provided interfaces, which represent the obligations that instances of that classifier have to their clients. They describe the services that the instances of that classifier offer to their clients.</p><p>The interfaces may also be used to specify required interfaces, which are specified by a usage dependency between the classifier and the corresponding interfaces. Required interfaces specify services that a classifier needs in order to perform its function and fulfill its own obligations to its clients.</p><p> </p><p>To draw a Provided Interface</p><hr /><ol><li>In the Class diagram, create a Class.</li><li>Select the Class shape and in the smart manipulator toolbar, click Interface Realization and then click on the diagram pane. The provided interface is created.</li><li>Select the interface shape, click the Compartments smart manipulator button, and then select <strong>Suppress All</strong>. Alternatively, click the <strong>Suppress All</strong> button in the diagram toolbar. <br /><br /></li></ol><p>To draw a Required Interface</p><hr /><ol><li>In the Class diagram, create a Class.</li><li>Select the Class shape and on the smart manipulator toolbar, click the Usage button and then click on the diagram. The required interface is created.</li><li>Select the interface shape, click the Compartments smart manipulator button, and then select <strong>Suppress All</strong>. Alternatively, click the <strong>Suppress All</strong> button in the diagram toolbar. </li></ol>
````

<!--NOMAGIC_PAGE id=243967731 space=MED version=1 -->
## PAGE 00353: Provided and Required Interfaces in the Composite Structure diagram

- page_id: `243967731`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/243967731/Provided+and+Required+Interfaces+in+the+Composite+Structure+diagram
- version_number: 1
- version_date: `2025-07-31T10:50:40.252+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UML elements > Interface
- labels: []

### NORMALIZED CONTENT

Information about provided and required interfaces is crucial in the assembly stage of complex internal structures. It helps to decide where connectors should be attached. 
Provided and required interfaces are valuable parts of the UML Composite Structure Diagram and SysML Internal Block Diagram.

A provided interface is shown using the "lollipop" notation attached to the port, and a required interface is shown using the "fork" notation attached to the port (see the following figure).

[IMAGE alt='' src='']

In the Composite Structure diagram, you cannot draw provided and required interfaces themselves, but, with the new functionality of the modeling tool, you can display a preexisting port with the required and provided interfaces as images.

[IMAGE alt='' src='']

Lollipop and fork symbols in the Composite Structure diagram are implemented as small attachments to a Port symbol similar to name a label. It is not the same as the independent stand alone notation of the interface, it is only part of the port symbol. It is important for Composite Structure diagrams in which real Interfaces (as Classifiers) cannot be used. It is an optional notation as a port does not display provided or required interfaces by default.

To display provided/required interfaces in the Composite Structure diagram

1. Select the port shape that has the provided/required interfaces you want to display.
2. Do one of the following: - From the port shortcut menu, select Display > Display Provided/Required Interfaces . - On the diagram toolbar, click [IMAGE alt='' src=''] and select Display Provided/Required Interfaces.

Ports can provide or require many interfaces, therefore, you can choose which ones to display or hide. Use the **Edit Compartment** dialog to manage the visibility of these interfaces.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>Information about provided and required interfaces is crucial in the assembly stage of complex internal structures. It helps to decide where connectors should be attached.<br />Provided and required interfaces are valuable parts of the UML Composite Structure Diagram and SysML Internal Block Diagram.</p><p>A provided interface is shown using the &quot;lollipop&quot; notation attached to the port, and a required interface is shown using the &quot;fork&quot; notation attached to the port (see the following figure).</p><p><ac:image ac:title="Provided and Required interface" ac:alt="Provided and Required interface"><ri:attachment ri:filename="interface_incomposite_strd1.png" /></ac:image></p><p>In the Composite Structure diagram, you cannot draw provided and required interfaces themselves, but, with the new functionality of the modeling tool, you can display a preexisting port with the required and provided interfaces as images.</p><p><ac:image ac:title="Provided and required interface in the Composite Structure diagram" ac:alt="Provided and required interface in the Composite Structure diagram"><ri:attachment ri:filename="interface_incomposite_strd2.png" /></ac:image></p><p>Lollipop and fork symbols in the Composite Structure diagram are implemented as small attachments to a Port symbol similar to name a label. It is not the same as the independent stand alone notation of the interface, it is only part of the port symbol. It is important for Composite Structure diagrams in which real Interfaces (as Classifiers) cannot be used. It is an optional notation as a port does not display provided or required interfaces by default.</p><p><br /></p><p>To display provided/required interfaces in the Composite Structure diagram</p><hr /><ol><li>Select the port shape that has the provided/required interfaces you want to display.</li><li>Do one of the following:<br />- From the port shortcut menu, select <strong>Display</strong> &gt; <strong>Display Provided/Required Interfaces</strong>.<br />- On the diagram toolbar, click <span class="confluence-embedded-file-wrapper"><ac:image ac:title="Display" ac:alt="Display"><ri:attachment ri:filename="Display.png" /></ac:image></span> and select <strong>Display Provided/Required Interfaces.</strong><br /><br /></li></ol><p>Ports can provide or require many interfaces, therefore, you can choose which ones to display or hide. Use the <strong>Edit Compartment</strong> dialog to manage the visibility of these interfaces.</p><p><br /></p>
````

<!--NOMAGIC_PAGE id=228986045 space=MED version=2 -->
## PAGE 00354: Provided Service Level

- page_id: `228986045`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/228986045/Provided+Service+Level
- version_number: 2
- version_date: `2025-05-14T10:31:06.567+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UAF 1.3 elements
- labels: []

### NORMALIZED CONTENT

**Description**

A sub type of Actual Service that details a specific service level delivered by the provider.

**Architecture** **Framework**

UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0

**Extension**

UML Instance Specification

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="OMGNormalParagraph"><strong>Description</strong></p><p class="OMGNormalParagraph">A sub type of Actual Service that details a specific service level delivered by the provider. </p><p class="OMGNormalParagraph"><strong>Architecture</strong> <strong>Framework</strong></p><p class="OMGNormalParagraph"><span style="color: rgb(62,63,64);">UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0</span></p><p class="OMGNormalParagraph"><strong>Extension</strong></p><p class="OMGNormalParagraph">UML Instance Specification</p><p><br /></p>
````

<!--NOMAGIC_PAGE id=243967735 space=MED version=1 -->
## PAGE 00355: Provided/required interfaces in the Component diagram

- page_id: `243967735`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/243967735/Provided+required+interfaces+in+the+Component+diagram
- version_number: 1
- version_date: `2025-07-31T10:50:40.372+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UML elements > Interface
- labels: []

### NORMALIZED CONTENT

A component specifies a formal contract of the services that it provides to its clients and those that it requires from other components or services in the system in terms of its provided and required interfaces.

The required and provided interfaces may optionally be organized through ports.

To add and manage the provided and required interfaces quickly, in the **Component** Specification window, select the **Provided/Required Interfaces** property group.

[IMAGE alt='' src='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p>A component specifies a formal contract of the services that it provides to its clients and those that it requires from other components or services in the system in terms of its provided and required interfaces. </p><p>The required and provided interfaces may optionally be organized through ports. </p><p>To add and manage the provided and required interfaces quickly, in the <strong>Component</strong> Specification window, select the <strong>Provided/Required Interfaces</strong> property group.</p><p><ac:image><ri:attachment ri:filename="ordering_interfaces.png" /></ac:image></p></ac:layout-cell><ac:layout-cell><p> </p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="two_equal"><ac:layout-cell><p> </p></ac:layout-cell><ac:layout-cell><p> </p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=228986046 space=MED version=2 -->
## PAGE 00356: Provides Competence

- page_id: `228986046`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/228986046/Provides+Competence
- version_number: 2
- version_date: `2025-05-14T10:31:06.841+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UAF 1.3 elements
- labels: []

### NORMALIZED CONTENT

**Description**

A dependency relationship that asserts that an Actual Organizational Resource provides a specific set of Competencies.

**Architecture Framework**

UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0

**Extension**

UML Dependency

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="OMGNormalParagraph"><strong>Description</strong></p><p class="OMGNormalParagraph">A dependency relationship that asserts that an Actual Organizational Resource provides a specific set of Competencies. </p><p class="OMGNormalParagraph"><strong>Architecture Framework</strong></p><p class="OMGNormalParagraph"><span style="color: rgb(62,63,64);">UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0</span></p><p class="OMGNormalParagraph"><strong>Extension</strong></p><p class="OMGNormalParagraph">UML Dependency</p><p><br /></p>
````

<!--NOMAGIC_PAGE id=9919437 space=MED version=10 -->
## PAGE 00357: Proxy Port

- page_id: `9919437`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/9919437/Proxy+Port
- version_number: 10
- version_date: `2025-09-13T12:46:27.226+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > SysML v1 elements
- labels: []

### NORMALIZED CONTENT

314265351

314265353

314265352

A Proxy Port is a port that specifies features of owning [CONFLUENCE_PAGE title='Block' space=''] or [CONFLUENCE_PAGE title='Part Property' space=''] that are available to external blocks through external [CONFLUENCE_PAGE title='Connector' space='MT'] to the ports. It can only be typed by [CONFLUENCE_PAGE title='Interface Block' space=''].

[IMAGE alt='' src='']

314265349

**Related pages**

- [CONFLUENCE_PAGE title='Hiding direction arrow on port shape' space='MT']
- [CONFLUENCE_PAGE title='SysML Internal Block Diagram' space='MT']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="9d15fda4-bdf4-4d04-9b94-d60bc3cad884"><ac:parameter ac:name="id">314265351</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="72e21173-e0f2-4655-9d9c-60dc23286ede"><ac:parameter ac:name="id">314265353</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="1dfb3373-d9dd-464f-8c45-288ea0f9e94d"><ac:parameter ac:name="id">314265352</ac:parameter><ac:rich-text-body><p><span style="color: rgb(0,0,0);">A Proxy Port is a port that specifies features of owning <ac:link><ri:page ri:content-title="Block" /><ac:plain-text-link-body><![CDATA[Blocks]]></ac:plain-text-link-body></ac:link> or <ac:link><ri:page ri:content-title="Part Property" /><ac:plain-text-link-body><![CDATA[Part Properties]]></ac:plain-text-link-body></ac:link> that are available to external blocks through external <ac:link><ri:page ri:space-key="MT" ri:content-title="Connector" /><ac:plain-text-link-body><![CDATA[Connectors]]></ac:plain-text-link-body></ac:link> to the ports. It can only be typed by <ac:link><ri:page ri:content-title="Interface Block" /></ac:link>.</span></p><p><span style="color: rgb(0,0,0);"><ac:image><ri:attachment ri:filename="proxy_ports.png" /></ac:image></span></p><p><br /></p><p class="auto-cursor-target"><br /></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="d51621f2-4dfa-45d1-8d59-f98d298968e3"><ac:parameter ac:name="id">314265349</ac:parameter><ac:rich-text-body><p class="auto-cursor-target"><strong>Related pages</strong></p><ul><li><ac:link><ri:page ri:space-key="MT" ri:content-title="Hiding direction arrow on port shape" /></ac:link></li><li><ac:link><ri:page ri:space-key="MT" ri:content-title="SysML Internal Block Diagram" /></ac:link></li></ul><p class="auto-cursor-target"><br /></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=243967960 space=MED version=1 -->
## PAGE 00358: Pseudo States

- page_id: `243967960`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/243967960/Pseudo+States
- version_number: 1
- version_date: `2025-07-31T10:50:46.090+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UML elements > State Machine
- labels: []

### NORMALIZED CONTENT

The Pseudo state is typically used to connect multiple transitions into more complex state transition's paths. For example, by combining a transition entering a fork pseudo state with a set of transitions exiting the fork pseudo state, we get a compound transition that leads to a set of orthogonal target states.

You can [CONFLUENCE_PAGE title='Editing property values' space='MT'] in the pseudo state [CONFLUENCE_PAGE title='Specification window' space='MT']. In the same window, you can find the description of each property. Descriptions are presented in the description area of the Specification window.

#### PANEL: Related Pages

Related Pages

- [CONFLUENCE_PAGE title='UML elements' space='']
- [CONFLUENCE_PAGE title='Specification window' space='MT']

#### PANEL: Related pages

Related pages

true

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p>The Pseudo state is typically used to connect multiple transitions into more complex state transition's paths. For example, by combining a transition entering a fork pseudo state with a set of transitions exiting the fork pseudo state, we get a compound transition that leads to a set of orthogonal target states.</p><p>You can <ac:link><ri:page ri:space-key="MT" ri:content-title="Editing property values" /><ac:plain-text-link-body><![CDATA[specify pseudo state properties]]></ac:plain-text-link-body></ac:link> in the pseudo state <ac:link><ri:page ri:space-key="MT" ri:content-title="Specification window" /></ac:link>. In the same window, you can find the description of each property. Descriptions are presented in the description area of the Specification window.</p></ac:layout-cell><ac:layout-cell><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="36e20852-22dd-420b-8d4b-52b136b22981"><ac:parameter ac:name="title">Related Pages</ac:parameter><ac:rich-text-body><ul><li><ac:link><ri:page ri:content-title="UML elements" /><ac:plain-text-link-body><![CDATA[Model Elements]]></ac:plain-text-link-body></ac:link></li><li><ac:link><ri:page ri:space-key="MT" ri:content-title="Specification window" /><ac:plain-text-link-body><![CDATA[Specification Window]]></ac:plain-text-link-body></ac:link></li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="f01b84d9-d9d1-4049-8315-15a6a05d850d"><ac:parameter ac:name="title">Related pages</ac:parameter><ac:rich-text-body><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="1672b43d-c66e-4197-af2f-1983c027f143"><ac:parameter ac:name="all">true</ac:parameter></ac:structured-macro></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=9919424 space=MED version=2 -->
## PAGE 00359: Quantity Kind

- page_id: `9919424`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/9919424/Quantity+Kind
- version_number: 2
- version_date: `2025-09-13T12:46:27.644+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > SysML v1 elements
- labels: []

### NORMALIZED CONTENT

A Quantity Kind (in SysML 1.0 and 1.1, called ‘Dimension’) is a kind of quantity that can be measured using defined and unrestricted units of measurement. For example, length, a quantity kind, may be measured by meter, kilometer, or foot units.

The only valid use of a Quantity Kind instance is to be referenced by the **quantity kind** property of a Value Type or Unit stereotype.

[IMAGE alt='' src='']

#### PANEL: Related diagrams

Related diagrams

- [CONFLUENCE_PAGE title='SysML Block Definition Diagram' space='MT']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p>A Quantity Kind (in SysML 1.0 and 1.1, called ‘Dimension’) is a kind of quantity that can be measured using defined and unrestricted units of measurement. For example, length, a quantity kind, may be measured by meter, kilometer, or foot units.</p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="54b3073f-6c12-4bf8-bad7-9be5c849f19a"><ac:rich-text-body><p>The only valid use of a Quantity Kind instance is to be referenced by the <strong>quantity kind</strong> property of a Value Type or Unit stereotype.</p></ac:rich-text-body></ac:structured-macro><p><ac:image ac:alt="Quantity Kind" ac:title="Quantity Kind"><ri:attachment ri:filename="quantity_kind.png" /></ac:image></p><p> </p></ac:layout-cell><ac:layout-cell><p> </p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p> </p><p> </p></ac:layout-cell><ac:layout-cell><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="3db70d55-40ce-4ef2-91cc-1d34c241634d"><ac:parameter ac:name="title">Related diagrams</ac:parameter><ac:rich-text-body><ul><li><ac:link><ri:page ri:space-key="MT" ri:content-title="SysML Block Definition Diagram" /><ac:plain-text-link-body><![CDATA[SysML Block Definition Diagram ]]></ac:plain-text-link-body></ac:link></li></ul></ac:rich-text-body></ac:structured-macro></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=243967911 space=MED version=3 -->
## PAGE 00360: Realization

- page_id: `243967911`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/243967911/Realization
- version_number: 3
- version_date: `2025-09-13T12:44:15.882+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UML elements
- labels: []

### NORMALIZED CONTENT

#### CONTENT-LAYER: Realization Types

852209378

#### CONTENT-COLUMN: Realization Types

852209380

#### CONTENT-BLOCK: Realization Types

852209379

The Realization is a specialized [CONFLUENCE_PAGE title='Navigating between different levels of abstraction' space='MT'] relationship between two sets of Classes, one represents a specification (the supplier), and the other represents an implementation of the latter (the client). The Realization can be used to model stepwise refinement, optimizations, transformations, templates, model synthesis, framework composition, and so forth.

The Realization relationship is drawn as a dashed line with a solid triangular arrowhead (a “dashed generalization symbol”). The client (the one at the tail of the arrow) supports at least all of the operations defined in the supplier (the one at the arrowhead), but not necessarily the data structure of the supplier ([CONFLUENCE_PAGE title='Attribute' space=''] and [CONFLUENCE_PAGE title='Association' space='MT']).

[IMAGE alt='' src='']

#### TIP: More Information

More Information

For more information about working with symbols, see [CONFLUENCE_PAGE title='Diagramming' space='MT'].

The Realization paths can be grouped in a tree. This feature makes the appearance of the diagram more structural and understandable.

#### NOTE: Realization Types

Realization Types

In our modeling tool, you will find three kinds of Realization relationships:

- **Interface Realization.** A dashed line with a solid triangular arrowhead. An Interface Realization is a specialized Realization relationship between a Classifier and an Interface. This relationship signifies that the realizing classifier conforms to the contract specified by the Interface.
- **Realization.** A solid line that represents a relationship between a [CONFLUENCE_PAGE title='Displaying internal structure on structured classifiers' space='MT'] and an [CONFLUENCE_PAGE title='Interface' space=''].
- **Substitution.** A dashed line with an arrowhead and *«substitute»* stereotype. A Substitution is a relationship between two classifiers. It signifies that the Substituting classifier complies with the contract specified by the contract classifier. This implies that instances of the Substituting classifier are runtime substitutable where instances of the contract classifier are expected.

To specify the selected realization path in the Specification window

- Double-click the path.
- Select Specification from the path's shortcut menu.
- Select the path and press Enter .

Creating the realizing classifiers

- The realizing classifiers are a set of Realizations owned by the Component. The Realizations reference the Classifiers of which the [CONFLUENCE_PAGE title='Component' space=''] is an abstraction (i.e., that realize its behavior).

To create a Realization relationship between a component and a classifier:

1. Drag the classifier shape to the [CONFLUENCE_PAGE title='Component' space=''] shape.
2. Select a classifier or Component and select Related Elements from its shortcut menu, then select the Display Paths command.
3. The Realization relationship will be displayed on the diagram pane.

[IMAGE alt='' src='']

852209376

**Related pages**

- Activity diagram
- Class diagram
- Action
- Package
- Associations
- Model Elements

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="846bf270-714e-4c83-ac58-d258863c0753"><ac:parameter ac:name="id">852209378</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="6c629d15-e761-4e99-b3e9-52c26f12117b"><ac:parameter ac:name="id">852209380</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="9650986b-0a7a-4eb0-a6a8-edee363313e7"><ac:parameter ac:name="id">852209379</ac:parameter><ac:rich-text-body><p>The Realization is a specialized <ac:link><ri:page ri:space-key="MT" ri:content-title="Navigating between different levels of abstraction" /><ac:plain-text-link-body><![CDATA[abstraction]]></ac:plain-text-link-body></ac:link> relationship between two sets of Classes, one represents a specification (the supplier), and the other represents an implementation of the latter (the client). The Realization can be used to model stepwise refinement, optimizations, transformations, templates, model synthesis, framework composition, and so forth.</p><p>The Realization relationship is drawn as a dashed line with a solid triangular arrowhead (a “dashed generalization symbol”). The client (the one at the tail of the arrow) supports at least all of the operations defined in the supplier (the one at the arrowhead), but not necessarily the data structure of the supplier (<ac:link><ri:page ri:content-title="Attribute" /><ac:plain-text-link-body><![CDATA[Attributes]]></ac:plain-text-link-body></ac:link> and <ac:link><ri:page ri:space-key="MT" ri:content-title="Association" /><ac:plain-text-link-body><![CDATA[Associations]]></ac:plain-text-link-body></ac:link>).</p><p style="text-align: center;"><ac:image ac:thumbnail="true" ac:height="96"><ri:attachment ri:filename="realization_relationship.png" /></ac:image></p><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="02202a08-01b8-4664-b9d1-3104c6e4ecc5"><ac:parameter ac:name="title">More Information</ac:parameter><ac:rich-text-body><p>For more information about working with symbols, see <ac:link><ri:page ri:space-key="MT" ri:content-title="Diagramming" /></ac:link>.</p></ac:rich-text-body></ac:structured-macro><p>The Realization paths can be grouped in a tree. This feature makes the appearance of the diagram more structural and understandable. </p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="05dbe8c8-0549-4267-bbc6-5daca7dde0a4"><ac:parameter ac:name="title">Realization Types</ac:parameter><ac:rich-text-body><p>In our modeling tool, you will find three kinds of Realization relationships: </p><ul><li><p><strong>Interface Realization.</strong> A dashed line with a solid triangular arrowhead. An Interface Realization is a specialized Realization relationship between a Classifier and an Interface. This relationship signifies that the realizing classifier conforms to the contract specified by the Interface. </p></li><li><p><strong>Realization.</strong> A solid line that represents a relationship between a <ac:link><ri:page ri:space-key="MT" ri:content-title="Displaying internal structure on structured classifiers" /><ac:plain-text-link-body><![CDATA[classifier]]></ac:plain-text-link-body></ac:link> and an <ac:link><ri:page ri:content-title="Interface" /><ac:plain-text-link-body><![CDATA[interface]]></ac:plain-text-link-body></ac:link>. </p></li><li><p><strong>Substitution.</strong> A dashed line with an arrowhead and <em>«substitute»</em> stereotype. A Substitution is a relationship between two classifiers. It signifies that the Substituting classifier complies with the contract specified by the contract classifier. This implies that instances of the Substituting classifier are runtime substitutable where instances of the contract classifier are expected. </p></li></ul></ac:rich-text-body></ac:structured-macro><p><span><br /></span></p><p>To specify the selected realization path in the Specification window</p><hr /><ul><li>Double-click the path.</li><li>Select <strong>Specification</strong> from the path's shortcut menu.</li><li>Select the path and press <strong>Enter</strong>. </li></ul><p><span><br /></span></p><p><span>Creating the realizing classifiers</span></p><hr /><ul><li>The realizing classifiers are a set of Realizations owned by the Component. The Realizations reference the Classifiers of which the <ac:link><ri:page ri:content-title="Component" /></ac:link> is an abstraction (i.e., that realize its behavior).</li></ul><p><br /></p><p>To create a Realization relationship between a component and a classifier: </p><hr /><ol><li>Drag the classifier shape to the <ac:link><ri:page ri:content-title="Component" /></ac:link> shape.</li><li>Select a classifier or Component and select <strong>Related Elements</strong> from its shortcut menu, then select the <strong>Display Paths</strong> command.</li><li>The Realization relationship will be displayed on the diagram pane. </li></ol><p><ac:image ac:thumbnail="true" ac:height="140"><ri:attachment ri:filename="realization_component_classifier.png" /></ac:image></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="ed516806-136c-4456-bee4-294e5784bb83"><ac:parameter ac:name="id">852209376</ac:parameter><ac:rich-text-body><p><strong>Related pages</strong></p><ul><li><a href="https://docs.nomagic.com/display/MT/Activity+diagram">Activity diagram</a></li><li><a href="https://docs.nomagic.com/display/MT/Class+diagram">Class diagram</a></li><li><a href="https://docs.nomagic.com/display/MT/Action">Action</a></li><li><a href="https://docs.nomagic.com/display/MT/Package">Package</a></li><li><a href="https://docs.nomagic.com/display/MT/Association">Associations</a></li><li class="ancestor-link parent-link"><a href="https://docs.nomagic.com/display/MT/Model+elements">Model Elements</a></li></ul></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=243967914 space=MED version=2 -->
## PAGE 00361: Reception

- page_id: `243967914`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/243967914/Reception
- version_number: 2
- version_date: `2025-09-13T12:42:55.780+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UML elements
- labels: []

### NORMALIZED CONTENT

#### CONTENT-LAYER: Signal Reception

847553109

#### CONTENT-COLUMN: Signal Reception

847553112

#### CONTENT-BLOCK: Signal Reception

847553110

Signal Receptions can be specified for [CONFLUENCE_PAGE title='Class' space=''] or [CONFLUENCE_PAGE title='Interface' space=''].

You can specify Reception properties in the Reception [CONFLUENCE_PAGE title='Specification window' space='MT']. You can find the description of each property in the same window. Descriptions are presented in the description area of the Specification window.

To create a new reception

Do one of the following:

- In the Class's Specification window, click the Receptions property group and then click the Create button. Select the signal and click OK . The Reception's Specification window opens.
- In the Containment tree, right-click a Class and from its [CONFLUENCE_PAGE title='DH Links panel shortcut menu and Sync Status icons' space='CDH'] , select Create Element and then Reception . Select the signal and click OK . Type the name for the new signal reception.
- On the diagram pane, click the Class, and then click the [ATTACHMENT filename='create_element.png'] Create Element smart manipulator. At the bottom of the menu, click the arrow to expand the menu and then click the Reception command. Select the signal and click OK.
- On the diagram pane, click the Class, then press the Ctrl+Alt+R shortcut keys. Then, select the signal and click OK .
- On the diagram pane, click the Class shape, and then click the [ATTACHMENT filename='create_signal_reception.png'] Create Reception smart manipulator.

#### NOTE: Signal Reception

Signal Reception

Note that the Reception compartment is suppressed by default.

- Drag the signal from the Containment tree or the diagram to the Class shape on the diagram pane.

To set the signal for a signal reception

Do one of the following:

- Create a Reception. The Select Signal dialog opens. Select an existing or create a new signal for the signal reception.
- In the Reception's Specification window, select a signal in the Signal drop-down menu. You can also click the “..." button. In the Select Element dialog, select a signal or click the Create button to create a new one.

To display signal reception on shape and to customize a displayed list

1. On the diagram pane, click on a symbol, then click the [ATTACHMENT filename='compartments.png'] Compartments button.
2. On the menu, click to select the Receptions check box. The Receptions compartment is displayed on the shape.
3. On the diagram pane, click a shape, then click the [ATTACHMENT filename='compartments.png'] Compartments button. On the menu, click the Edit Compartments command.
4. In the Compartment Edit dialog, click the Receptions tab.
5. Move the receptions from the Hidden to the Selected list or vice versa.

To change the order of the signal receptions

1. On the diagram pane, right-click the shape. From its shortcut menu, select the Symbol Properties command.
2. In the Symbol Properties dialog, under the Receptions group, click to change the Receptions Sort Mode property.

847553108

**Related pages**

- [CONFLUENCE_PAGE title='Class diagram' space='MT']
- [CONFLUENCE_PAGE title='Action' space='']
- [CONFLUENCE_PAGE title='Package' space='']
- [CONFLUENCE_PAGE title='Association' space='']
- [CONFLUENCE_PAGE title='UML elements' space='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="0a393c0c-c696-44e3-8c67-32a4f44c522a"><ac:parameter ac:name="id">847553109</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="b7f98659-3c2a-428a-8bc0-c8fcf452ad4c"><ac:parameter ac:name="id">847553112</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="e9ddf59e-dd10-459a-b2f1-c5cd3b5c72db"><ac:parameter ac:name="id">847553110</ac:parameter><ac:rich-text-body><ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p><span>Signal Receptions can be specified for <ac:link><ri:page ri:content-title="Class" /><ac:plain-text-link-body><![CDATA[classes]]></ac:plain-text-link-body></ac:link> or <ac:link><ri:page ri:content-title="Interface" /><ac:plain-text-link-body><![CDATA[interfaces]]></ac:plain-text-link-body></ac:link>. </span></p><p><span>You can specify Reception properties in the Reception <ac:link><ri:page ri:space-key="MT" ri:content-title="Specification window" /></ac:link>. You can find the description of each property in the same window. Descriptions are presented in the description area of the Specification window. </span></p><p><span><br /></span></p><p><span>To create a new reception</span></p><hr /><p>Do one of the following:</p><ul><li>In the Class's Specification window, click the<strong> Receptions</strong> property group and then click the <strong>Create</strong> button. Select the signal and click <strong>OK</strong>. The Reception's Specification window opens.</li><li>In the Containment tree, right-click a Class and from its <ac:link><ri:page ri:space-key="CDH" ri:content-title="DH Links panel shortcut menu and Sync Status icons" /><ac:plain-text-link-body><![CDATA[shortcut menu]]></ac:plain-text-link-body></ac:link>, select <strong>Create Element</strong> and then<strong> Reception</strong>. Select the signal and click <strong>OK</strong>. Type the name for the new signal reception.</li><li>On the diagram pane, click the Class, and then click the <ac:image ac:thumbnail="true" ac:height="9"><ri:attachment ri:filename="create_element.png" /></ac:image> <em>Create Element</em> smart manipulator. At the bottom of the menu, click the arrow to expand the menu and then click the<strong> Reception</strong> command. Select the signal and click OK.</li><li>On the diagram pane, click the Class, then press the <strong>Ctrl+Alt+R</strong> shortcut keys. Then, select the signal and click <strong>OK</strong>.</li><li>On the diagram pane, click the Class shape, and then click the <ac:image ac:thumbnail="true" ac:height="9"><ri:attachment ri:filename="create_signal_reception.png"><ri:page ri:space-key="MT" ri:content-title="_MD buttons" /></ri:attachment></ac:image> <strong>Create Reception</strong> smart manipulator. </li></ul><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="aca71463-bd5b-446d-9ab4-4f08f5d46896"><ac:parameter ac:name="title">Signal Reception</ac:parameter><ac:rich-text-body><p>Note that the Reception compartment is suppressed by default.</p></ac:rich-text-body></ac:structured-macro><ul><li class="auto-cursor-target">Drag the signal from the Containment tree or the diagram to the Class shape on the diagram pane. </li></ul><p><span><br /></span></p><p><span>To set the signal for a signal reception</span></p><hr /><p>Do one of the following:</p><ul><li>Create a Reception. The Select Signal dialog opens. Select an existing or create a new signal for the signal reception. </li><li>In the Reception's Specification window, select a signal in the <strong>Signal</strong> drop-down menu. You can also click the “...&quot; button. In the Select Element dialog, select a signal or click the <strong>Create</strong> button to create a new one.</li></ul><p><br /></p><p><span>To display signal reception on shape and to customize a displayed list</span></p><hr /><ol><li>On the diagram pane, click on a symbol, then click the <ac:image ac:thumbnail="true" ac:height="9"><ri:attachment ri:filename="compartments.png"><ri:page ri:content-title="Working with dependencies" /></ri:attachment></ac:image>  <em>Compartments</em> button. </li><li>On the menu, click to select the<strong> Receptions</strong> check box. The Receptions compartment is displayed on the shape.</li><li>On the diagram pane, click a shape, then click the <ac:image ac:thumbnail="true" ac:height="9"><ri:attachment ri:filename="compartments.png"><ri:page ri:content-title="Working with dependencies" /></ri:attachment></ac:image> <em>Compartments</em> button. On the menu, click the <strong>Edit Compartments</strong> command.</li><li>In the Compartment Edit dialog, click the<strong> Receptions</strong> tab.</li><li>Move the receptions from the <em>Hidden</em> to the <em>Selected</em> list or vice versa.</li></ol><p><span><br /></span></p><p><span>To change the order of the signal receptions</span></p><hr /><ol><li>On the diagram pane, right-click the shape. From its shortcut menu, select the <strong>Symbol Properties</strong> command. </li><li>In the Symbol Properties dialog, under the<strong> Receptions</strong> group, click to change the<strong> Receptions Sort Mode</strong> property. </li></ol><p><br /></p><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p><br /></p></ac:layout-cell><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section></ac:layout></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="8f660b8c-8c0b-4ed6-9b6d-11e875788866"><ac:parameter ac:name="id">847553108</ac:parameter><ac:rich-text-body><p><strong>Related pages</strong></p><ul><li><ac:link><ri:page ri:space-key="MT" ri:content-title="Class diagram" /></ac:link></li><li><ac:link><ri:page ri:content-title="Action" /></ac:link></li><li><ac:link><ri:page ri:content-title="Package" /></ac:link></li><li><ac:link><ri:page ri:content-title="Association" /><ac:plain-text-link-body><![CDATA[Associations]]></ac:plain-text-link-body></ac:link></li><li><ac:link><ri:page ri:content-title="UML elements" /><ac:plain-text-link-body><![CDATA[Model Elements]]></ac:plain-text-link-body></ac:link></li></ul></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=9919466 space=MED version=2 -->
## PAGE 00362: Reference Property

- page_id: `9919466`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/9919466/Reference+Property
- version_number: 2
- version_date: `2025-09-13T12:46:29.534+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > SysML v1 elements
- labels: []

### NORMALIZED CONTENT

A Reference Property is a property that specifies a reference of its containing Block to another Block. Every Reference Property has ‘none’ AggregationKind and is typed by a block. Reference Properties are displayed in the ‘references’ compartment.

[IMAGE alt='' src='']

#### PANEL: Related diagrams

Related diagrams

- [CONFLUENCE_PAGE title='SysML Internal Block Diagram' space='MT']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p>A Reference Property is a property that specifies a reference of its containing Block to another Block. Every Reference Property has ‘none’ AggregationKind and is typed by a block. Reference Properties are displayed in the ‘references’ compartment.</p><p><ac:image><ri:attachment ri:filename="reference_property.png" /></ac:image></p></ac:layout-cell><ac:layout-cell><p> </p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p> </p><p> </p></ac:layout-cell><ac:layout-cell><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="ad1d2f29-7ddc-4427-be11-2022073a6b8a"><ac:parameter ac:name="title">Related diagrams</ac:parameter><ac:rich-text-body><ul><li><ac:link><ri:page ri:space-key="MT" ri:content-title="SysML Internal Block Diagram" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=249005182 space=MED version=2 -->
## PAGE 00363: Refine

- page_id: `249005182`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/249005182/Refine
- version_number: 2
- version_date: `2025-08-18T17:40:03.368+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > Requirement-related elements
- labels: []

### NORMALIZED CONTENT

A 'Refine' relationship is a dependency that describes how a model element or a set of elements refine a requirement. For example, a use case or activity diagram may be used to refine a text-based functional requirement. Alternatively, it may be used to show how a text-based requirement refines a model element. In this case, some elaborated text could be used to refine a less fine- grained model element.

[IMAGE alt='' src='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>A 'Refine' relationship is a dependency that describes how a model element or a set of elements refine a requirement. For example, a use case or activity diagram may be used to refine a text-based functional requirement. Alternatively, it may be used to show how a text-based requirement refines a model element. In this case, some elaborated text could be used to refine a less fine- grained model element.</p><p><ac:image ac:height="196" ac:width="167"><ri:attachment ri:filename="refine_relationship.png" /></ac:image></p>
````

<!--NOMAGIC_PAGE id=243967916 space=MED version=1 -->
## PAGE 00364: Report Template

- page_id: `243967916`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/243967916/Report+Template
- version_number: 1
- version_date: `2025-07-31T10:50:45.361+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UML elements
- labels: []

### NORMALIZED CONTENT

846411724

846411726

846411725

This is a custom element used to store a report template file (*.mrzip*) attached to the project.

In contrast to the report templates stored in the local report templates folder (*<modeling tool [CONFLUENCE_PAGE title='Configuration files' space='MT']>\data\reports*), a report template attached to the project as this specific type of model element is not lost when you open the project on another computer. It is safely transferred within the project (either local or server).

To attach a report template to the project

1. From the main menu, select Tools > Report Wizard . The [CONFLUENCE_PAGE title='Report Wizard dialog' space='MT']**Report Wizard** dialog opens.
2. Select the report template you want to attach to the project and click the Attach button. The selected report template is duplicated, and the duplicate is attached to the open project. It is visible in the [CONFLUENCE_PAGE title='Containment tab' space='MT'] directly under the root package. As the following figure shows, in the Report Wizard dialog it as marked with the “[Attached to Project]” tag.

[IMAGE alt='' src='']

###### Attached to a project report template in the Report Wizard dialog.

You can generate a report from the attached report template in one of the following ways:

- Right-click the attached report template in the Containment tree. From the shortcut menu select Generate Report . The Report Wizard dialog opens with the attached report template already selected. Proceed to the subsequent steps of the wizard.
- Right-click the namespace (for example, a Package) in the Containment tree. From the shortcut menu select Generate Report . Then select the appropriate report templates category and click the attached report template.

The *“[Attached]”* tag helps to identify attached to project report templates on this menu.

Proceed to the subsequent steps of the wizard.

- From the main menu, select Tools > Report Wizard . In the Report Wizard dialog, select the report template and proceed to the subsequent steps of the wizard.

[IMAGE alt='' src='']

###### Selecting attached to project report template for report generation.

If you no longer need the attached report template, you can simply delete it from the model. Just select it in the Containment tree and press **Delete**.

If you need to modify the attached report template, do the following:

- 
  - Extract it to the local report templates folder.
  - Open the extracted template for edit and make changes in it.
  - After you finish editing, reattach the updated report template to your project.

To extract a report template to the local report templates folder

- 
  - From the main menu, select Tools > Report Wizard. The Report Wizard dialog opens.
  - Select the report template you want to extract to the local report templates folder and click the Extract button.
  - If a message asking to confirm the update of already existing report template appears, click Yes.

The report template appears in the local report templates folder and can be opened for edit. It also remains attached to the open project.

846411723

**Related pages**

- [CONFLUENCE_PAGE title='Report Wizard' space='MT']
- [CONFLUENCE_PAGE title='Containment Tree' space='']
- [CONFLUENCE_PAGE title='UML elements' space='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="83a38efa-6e8b-4fa0-bc79-0da4fa7b2513"><ac:parameter ac:name="id">846411724</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="4a8d51e6-30db-4da8-9796-1660affa4f6f"><ac:parameter ac:name="id">846411726</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="d087491a-9b7c-4add-9e65-7aff201de547"><ac:parameter ac:name="id">846411725</ac:parameter><ac:rich-text-body><ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p>This is a custom element used to store a report template file (<em>.mrzip</em>) attached to the project.</p><p><span>In contrast to the report templates stored in the local report templates folder (</span><em>&lt;modeling tool <ac:link><ri:page ri:space-key="MT" ri:content-title="Configuration files" /><ac:plain-text-link-body><![CDATA[configuration files directory]]></ac:plain-text-link-body></ac:link>&gt;\data\reports</em><span>), a report template attached to the project as this specific type of model element is not lost when you open the project on another computer. It is safely transferred within the project (either local or server). </span></p><p><br /></p><p>To attach a report template to the project</p><hr /><ol><li>From the main menu, select <strong>Tools</strong> &gt; <strong>Report Wizard</strong>. The <ac:link><ri:page ri:space-key="MT" ri:content-title="Report Wizard dialog" /><ac:link-body><strong>Report Wizard</strong> dialog</ac:link-body></ac:link> opens.</li><li>Select the report template you want to attach to the project and click the <strong>Attach</strong> button. The selected report template is duplicated, and the duplicate is attached to the open project. It is visible in the <ac:link><ri:page ri:space-key="MT" ri:content-title="Containment tab" /><ac:plain-text-link-body><![CDATA[Containment tree]]></ac:plain-text-link-body></ac:link> directly under the root package. As the following figure shows, in the <strong>Report Wizard</strong> dialog it as marked with the <em>“[Attached to Project]”</em> tag.</li></ol><p style="text-align: center;"><ac:image><ri:attachment ri:filename="report_template.png" /></ac:image></p><h6 style="text-align: center;">Attached to a project report template in the Report Wizard dialog.</h6><p>You can generate a report from the attached report template in one of the following ways:</p><ul><li>Right-click the attached report template in the Containment tree. From the shortcut menu select <strong>Generate Report</strong>. The <strong>Report Wizard</strong> dialog opens with the attached report template already selected. Proceed to the subsequent steps of the wizard.</li><li class="auto-cursor-target"><span>Right-click the namespace (for example, a Package) in the Containment tree. From the shortcut menu select </span><strong>Generate Report</strong><span>. Then select the appropriate report templates category and click the attached report template.</span></li></ul><p><br /></p><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="79625bc9-2136-4f84-b7fd-680a06bc2552"><ac:rich-text-body><p style="margin-left: 30.0px;">The <em>“[Attached]”</em> tag helps to identify attached to project report templates on this menu.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target" style="margin-left: 30.0px;">Proceed to the subsequent steps of the wizard.</p><ul><li><span>From the main menu, select </span><strong>Tools </strong><span>&gt; </span><strong>Report Wizard</strong><span>. In the </span><strong>Report Wizard </strong><span>dialog, select the report template and proceed to the subsequent steps of the wizard. </span></li></ul><p style="margin-left: 30.0px;"><span><ac:image ac:align="center"><ri:attachment ri:filename="generating_report.png" /></ac:image></span></p><h6 style="margin-left: 30.0px;text-align: center;"><span>Selecting attached to project report template for report generation.</span></h6><p style="margin-left: 30.0px;"><span>If you no longer need the attached report template, you can simply delete it from the model. Just select it in the Containment tree and press <strong>Delete</strong>. </span></p><p style="margin-left: 30.0px;">If you need to modify the attached report template, do the following:</p><ul><li style="list-style-type: none;background-image: none;"><ul><li>Extract it to the local report templates folder.</li><li>Open the extracted template for edit and make changes in it.</li><li>After you finish editing, reattach the updated report template to your project.</li></ul></li></ul><p><br /></p><p style="margin-left: 30.0px;">To extract a report template to the local report templates folder</p><hr /><ul><li style="list-style-type: none;background-image: none;"><ul><li>From the main menu, select <strong>Tools</strong> &gt; <strong>Report Wizard.</strong> The <strong>Report Wizard</strong> dialog opens.</li><li>Select the report template you want to extract to the local report templates folder and click the <strong>Extract</strong> button.</li><li>If a message asking to confirm the update of already existing report template appears, click <strong>Yes.</strong></li></ul></li></ul><p><br /></p><p style="margin-left: 30.0px;">The report template appears in the local report templates folder and can be opened for edit. It also remains attached to the open project. </p><p style="margin-left: 30.0px;"><span><br /></span></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p><br /></p></ac:layout-cell><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section></ac:layout></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="cedf4174-fb8b-4171-8c27-e9a02eef671e"><ac:parameter ac:name="id">846411723</ac:parameter><ac:rich-text-body><p><strong>Related pages</strong></p><ul><li><ac:link><ri:page ri:space-key="MT" ri:content-title="Report Wizard" /></ac:link></li><li><ac:link><ri:page ri:content-title="Containment Tree" /></ac:link></li><li><ac:link><ri:page ri:content-title="UML elements" /><ac:plain-text-link-body><![CDATA[Model Elements]]></ac:plain-text-link-body></ac:link></li></ul></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=243968078 space=MED version=1 -->
## PAGE 00365: Representing Use Case scenarios in Activity diagrams

- page_id: `243968078`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/243968078/Representing+Use+Case+scenarios+in+Activity+diagrams
- version_number: 1
- version_date: `2025-07-31T10:50:49.644+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UML elements > Use Case > Use Case Scenario sketch
- labels: []

### NORMALIZED CONTENT

879905382

879905384

879905383

After you have created a Use Case scenario, you can represent this scenario in an Activity diagram. The following procedure describes how to represent the Use Case scenario in the Activity diagram and how to turn the automatic layout on or off in the Activity diagram when representing the Use Case scenario.

To represent a Use Case scenario in an Activity diagram

1. Open the Use Case Specification window and click the Use Case Scenario Sketch property group.
2. Click the Open Activity Diagram button [ATTACHMENT filename='open_and_update_button.png'] . The Activity diagram opens with the Use Case scenario represented on it.

You need to reopen the Activity diagram each time after you make modifications to the Use Case scenario in the [CONFLUENCE_PAGE title='Specification window' space='MT']. Modifications to the Activity diagram where the Use Case scenario is represented automatically appear in the textual Use Case scenario.

For Use Cases having read-only accessibility, the use Case Scenario cannot be represented on the Activity diagram.

In the Activity diagram, all symbols are laid out automatically every time the diagram is opened.

To leave symbols in the same place while opening the Activity diagram after modifying the Use Case scenario in the [CONFLUENCE_PAGE title='Specification window' space='MT'], change the **Layout use case scenario activity diagram**option value to *false*. This option appears in the **Project Options**dialog, in the **General project options**group.

Your modeling tool might not be able to interpret the Use Case scenario in some cases. These are the most common reasons why:

| There is no merge node or call behavior action after the element. |
| --- |
| There is no initial node in Activity. |
| There is no final node in Activity. |
| There are no outgoing control flows from the element. |
| There is no merge node after the element. |
| There are no outgoing flows from the element. |
| There is no alternative flow step after the element. |
| Cyclic scenario. |

[IMAGE alt='' src='']

###### Use Case Scenario cannot be interpreted

879905381

**Related pages**

- [CONFLUENCE_PAGE title='UML elements' space='']
- [CONFLUENCE_PAGE title='Transition' space='']
- [CONFLUENCE_PAGE title='State Machine diagram' space='MT']
- [CONFLUENCE_PAGE title='Activity diagram' space='MT']
- [CONFLUENCE_PAGE title='Sequence diagram' space='MT']
- [CONFLUENCE_PAGE title='Use Case diagram' space='MT']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="15a3347f-6d63-4e0b-9838-18cf190a5108"><ac:parameter ac:name="id">879905382</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="2311a67c-5aa9-484c-a1cf-433777a2a84a"><ac:parameter ac:name="id">879905384</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="11aa949b-564d-4a3a-bb37-3295684a67a9"><ac:parameter ac:name="id">879905383</ac:parameter><ac:rich-text-body><p>After you have created a Use Case scenario, you can represent this scenario in an Activity diagram. The following procedure describes how to represent the Use Case scenario in the Activity diagram and how to turn the automatic layout on or off in the Activity diagram when representing the Use Case scenario.</p><p><br /></p><p>To represent a Use Case scenario in an Activity diagram </p><hr /><ol><li>Open the Use Case Specification window and click the <strong>Use Case Scenario Sketch </strong>property group.</li><li>Click the <strong style="line-height: 1.4285715;">Open Activity Diagram </strong>button <ac:image ac:thumbnail="true" ac:height="24"><ri:attachment ri:filename="open_and_update_button.png" /></ac:image>. The Activity diagram opens with the Use Case scenario represented on it.</li></ol><p>You need to reopen the Activity diagram each time after you make modifications to the Use Case scenario in the <ac:link><ri:page ri:space-key="MT" ri:content-title="Specification window" /></ac:link>. Modifications to the Activity diagram where the Use Case scenario is represented automatically appear in the textual Use Case scenario.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="3ca74a43-8817-461d-89c5-9d4fbb150532"><ac:rich-text-body><p>For Use Cases having read-only accessibility, the use Case Scenario cannot be represented on the Activity diagram.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><p>In the Activity diagram, all symbols are laid out automatically every time the diagram is opened.</p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="6c60b289-5bbc-4c79-b66b-f350315b2fa0"><ac:rich-text-body><p>To leave symbols in the same place while opening the Activity diagram after modifying the Use Case scenario in the <ac:link><ri:page ri:space-key="MT" ri:content-title="Specification window" /></ac:link>, change the <strong style="line-height: 1.4285715;">Layout use case scenario activity diagram </strong>option value to <em style="line-height: 1.4285715;">false</em>. This option appears in the <strong style="line-height: 1.4285715;">Project Options </strong>dialog, in the <strong style="line-height: 1.4285715;">General project options </strong>group.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><p><br /></p><p>Your modeling tool might not be able to interpret the Use Case scenario in some cases. These are the most common reasons why:</p><table class="relative-table wrapped" style="width: 615.0px;"><colgroup><col style="width: 0.0px;" /></colgroup><tbody><tr><td>There is no merge node or call behavior action after the element.</td></tr><tr><td>There is no initial node in Activity.</td></tr><tr><td>There is no final node in Activity.</td></tr><tr><td colspan="1">There are no outgoing control flows from the element.</td></tr><tr><td colspan="1">There is no merge node after the element.</td></tr><tr><td colspan="1">There are no outgoing flows from the element.</td></tr><tr><td colspan="1">There is no alternative flow step after the element.</td></tr><tr><td colspan="1">Cyclic scenario.</td></tr></tbody></table><p><br /></p><p class="auto-cursor-target"><br /></p><p><ac:image ac:align="center"><ri:attachment ri:filename="unable_to_interpret_use_case_scenario.png" /></ac:image></p><h6 style="text-align: center;"><span style="color: rgb(128,128,128);">Use Case Scenario cannot be interpreted</span></h6></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="b6e4817f-2b94-4433-988e-1dab1c00c80d"><ac:parameter ac:name="id">879905381</ac:parameter><ac:rich-text-body><p><strong>Related pages</strong></p><ul><li><ac:link><ri:page ri:content-title="UML elements" /><ac:plain-text-link-body><![CDATA[Model Elements]]></ac:plain-text-link-body></ac:link></li><li><ac:link><ri:page ri:content-title="Transition" /></ac:link></li><li><ac:link><ri:page ri:space-key="MT" ri:content-title="State Machine diagram" /></ac:link></li><li><ac:link><ri:page ri:space-key="MT" ri:content-title="Activity diagram" /></ac:link></li><li><ac:link><ri:page ri:space-key="MT" ri:content-title="Sequence diagram" /></ac:link></li><li><ac:link><ri:page ri:space-key="MT" ri:content-title="Use Case diagram" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=228986047 space=MED version=2 -->
## PAGE 00366: Required Service Level

- page_id: `228986047`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/228986047/Required+Service+Level
- version_number: 2
- version_date: `2025-05-14T10:31:07.092+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UAF 1.3 elements
- labels: []

### NORMALIZED CONTENT

**Description**

A sub type of Actual Service that details a specific service level required of the provider.

**Architecture** **Framework**

UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0

**Extension**

UML Instance Specification

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="OMGNormalParagraph"><strong>Description</strong></p><p class="OMGNormalParagraph">A sub type of Actual Service that details a specific service level required of the provider.</p><p class="OMGNormalParagraph"><strong>Architecture</strong> <strong>Framework</strong></p><p class="OMGNormalParagraph"><span style="color: rgb(62,63,64);">UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0</span></p><p class="OMGNormalParagraph"><strong>Extension</strong></p><p class="OMGNormalParagraph">UML Instance Specification</p><p><br /></p>
````

<!--NOMAGIC_PAGE id=249005172 space=MED version=2 -->
## PAGE 00367: Requirement

- page_id: `249005172`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/249005172/Requirement
- version_number: 2
- version_date: `2025-08-18T17:37:07.432+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > Requirement-related elements
- labels: []

### NORMALIZED CONTENT

A Requirement specifies a capability or a condition that must (or should) be satisfied. Requirements are used to establish a contract between the customer (or other stakeholders) and those responsible for designing and implementing the system. A requirement can also appear on other diagrams to show its relationship to other modeling elements.

When a requirement nests other requirements, all the nested requirements apply as part of the container requirement (the requirement that contains all the nested requirements). Deleting the container requirement will thus delete all the nested requirements it contains; a functionality inherited from UML.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>A Requirement specifies a capability or a condition that must (or should) be satisfied. Requirements are used to establish a contract between the customer (or other stakeholders) and those responsible for designing and implementing the system. A requirement can also appear on other diagrams to show its relationship to other modeling elements.</p><p>When a requirement nests other requirements, all the nested requirements apply as part of the container requirement (the requirement that contains all the nested requirements). Deleting the container requirement will thus delete all the nested requirements it contains; a functionality inherited from UML.</p>
````

<!--NOMAGIC_PAGE id=249005164 space=MED version=1 -->
## PAGE 00368: Requirement-related elements

- page_id: `249005164`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/249005164/Requirement-related+elements
- version_number: 1
- version_date: `2025-08-14T18:32:06.563+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions
- labels: []

### NORMALIZED CONTENT

This section provides all descriptions of the requirement elements.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p>This section provides all descriptions of the requirement elements.</p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="54827e81-6e19-4d8b-ab2e-d2c80760c18f" /></p></ac:layout-cell><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=228986048 space=MED version=2 -->
## PAGE 00369: Requires Competence

- page_id: `228986048`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/228986048/Requires+Competence
- version_number: 2
- version_date: `2025-05-14T10:31:07.307+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UAF 1.3 elements
- labels: []

### NORMALIZED CONTENT

**Description**

An abstraction relationship that asserts that an Actual Organizational Resource is required to have a specific set of Competencies.

**Architecture Framework**

UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0

**Extension**

UML Abstraction

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="OMGNormalParagraph"><strong>Description</strong></p><p class="OMGNormalParagraph">An abstraction relationship that asserts that an Actual Organizational Resource is required to have a specific set of Competencies. </p><p class="OMGNormalParagraph"><span class="fontstyle0"><strong>Architecture Framework</strong></span></p><p class="OMGNormalParagraph"><span style="color: rgb(62,63,64);">UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0</span></p><p class="OMGNormalParagraph"><strong>Extension</strong></p><p class="OMGNormalParagraph">UML Abstraction</p>
````

<!--NOMAGIC_PAGE id=228986049 space=MED version=2 -->
## PAGE 00370: Resource

- page_id: `228986049`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/228986049/Resource
- version_number: 2
- version_date: `2025-05-14T10:31:07.536+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UAF 1.3 elements
- labels: []

### NORMALIZED CONTENT

**Description**

Abstract element grouping for all elements that can be conveyed by an Exchange.

**Architecture** **Framework**

UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0

**Extension**

Element

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="OMGBoldBulletKeepNextParagraph"><strong>Description</strong></p><p class="OMGNormalParagraph">Abstract element grouping for all elements that can be conveyed by an Exchange.</p><p class="OMGNormalParagraph"><strong>Architecture</strong> <strong>Framework</strong></p><p class="OMGNormalParagraph"><span style="color: rgb(62,63,64);">UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0</span></p><p class="OMGNormalParagraph"><strong>Extension</strong></p><p class="OMGNormalParagraph">Element</p><p><br /></p>
````

<!--NOMAGIC_PAGE id=228986050 space=MED version=2 -->
## PAGE 00371: Resource Architecture

- page_id: `228986050`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/228986050/Resource+Architecture
- version_number: 2
- version_date: `2025-05-14T10:31:07.779+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UAF 1.3 elements
- labels: []

### NORMALIZED CONTENT

**Description**

An element used to denote a model of the Architecture, described from the Resource Performer perspective.

**Architecture** **Framework**

UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0

**Extension**

UML Class

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="OMGNormalParagraph"><strong>Description</strong></p><p class="OMGNormalParagraph">An element used to denote a model of the Architecture, described from the Resource Performer perspective.</p><p class="OMGNormalParagraph"><strong>Architecture</strong> <strong>Framework</strong></p><p class="OMGNormalParagraph"><span style="color: rgb(62,63,64);">UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0</span></p><p class="OMGNormalParagraph"><strong>Extension</strong></p><p class="OMGNormalParagraph">UML Class</p><p><br /></p>
````

<!--NOMAGIC_PAGE id=228986051 space=MED version=2 -->
## PAGE 00372: Resource Artifact

- page_id: `228986051`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/228986051/Resource+Artifact
- version_number: 2
- version_date: `2025-05-14T10:31:08.170+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UAF 1.3 elements
- labels: []

### NORMALIZED CONTENT

**Description**

A type of man-made object that contains no human beings (i.e. satellite, radio, petrol, gasoline, etc.).

**Architecture Framework**

UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0

**Extensions**

UML Class

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="OMGBoldBulletKeepNextParagraph"><strong>Description</strong></p><p class="OMGNormalParagraph">A type of man-made object that contains no human beings (i.e. satellite, radio, petrol, gasoline, etc.). </p><p class="OMGNormalParagraph"><strong><span class="fontstyle0">Architecture Framework</span></strong></p><p class="OMGNormalParagraph"><span style="color: rgb(62,63,64);">UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0</span></p><p class="OMGNormalParagraph"><strong><span class="fontstyle2"><span class="fontstyle0">Extensions</span></span></strong></p><p class="OMGNormalParagraph"><span class="fontstyle2"><span class="fontstyle1">UML Class</span> </span></p><p><br /></p>
````

<!--NOMAGIC_PAGE id=228986052 space=MED version=2 -->
## PAGE 00373: Resource Asset

- page_id: `228986052`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/228986052/Resource+Asset
- version_number: 2
- version_date: `2025-05-14T10:31:08.617+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UAF 1.3 elements
- labels: []

### NORMALIZED CONTENT

**Description**

An abstract element used to group the elements of ResourcePerformer and DataElement allowing them to own DataRoles

**Architecture Framework**

UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0

**Extension**

Class

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description</strong></p><p><span style="color: rgb(62,63,64);">An abstract element used to group the elements of ResourcePerformer and DataElement allowing them to own DataRoles</span></p><p><strong><span style="color: rgb(62,63,64);">Architecture Framework</span></strong></p><p><span style="color: rgb(62,63,64);">UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0</span></p><p><strong><span style="color: rgb(62,63,64);">Extension</span></strong></p><p><span style="color: rgb(62,63,64);">Class</span></p>
````

<!--NOMAGIC_PAGE id=228986053 space=MED version=2 -->
## PAGE 00374: Resource Connector

- page_id: `228986053`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/228986053/Resource+Connector
- version_number: 2
- version_date: `2025-05-14T10:31:08.883+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UAF 1.3 elements
- labels: []

### NORMALIZED CONTENT

**Description**

A channel for exchange between two Resource Roles.

**Architecture** **Framework**

UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0

**Extension**

Connector

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="OMGBoldBulletKeepNextParagraph"><strong>Description</strong></p><p>A channel for exchange between two Resource Roles.</p><p><strong>Architecture</strong> <strong>Framework</strong></p><p><span style="color: rgb(62,63,64);">UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0</span></p><p class="OMGNormalParagraph"><strong>Extension</strong></p><p class="OMGNormalParagraph">Connector</p><p><br /></p>
````

<!--NOMAGIC_PAGE id=228986054 space=MED version=2 -->
## PAGE 00375: Resource Constraint

- page_id: `228986054`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/228986054/Resource+Constraint
- version_number: 2
- version_date: `2025-05-14T10:31:09.308+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UAF 1.3 elements
- labels: []

### NORMALIZED CONTENT

**Description**

A rule governing the structural or functional aspects of an implementation.

**Architecture** **Framework**

UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0

**Extension**

UML Constraint

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="OMGBoldBulletKeepNextParagraph"><strong>Description</strong></p><p class="OMGNormalParagraph">A rule governing the structural or functional aspects of an implementation.</p><p class="OMGNormalParagraph"><strong>Architecture</strong> <strong>Framework</strong></p><p class="OMGNormalParagraph"><span style="color: rgb(62,63,64);">UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0</span></p><p class="OMGNormalParagraph"><strong>Extension</strong></p><p class="OMGNormalParagraph">UML Constraint</p><p><br /></p>
````

<!--NOMAGIC_PAGE id=228986055 space=MED version=2 -->
## PAGE 00376: Resource Exchange

- page_id: `228986055`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/228986055/Resource+Exchange
- version_number: 2
- version_date: `2025-05-14T10:31:09.674+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UAF 1.3 elements
- labels: []

### NORMALIZED CONTENT

**Description**

Asserts that a flow can exist between Resource Performers (i.e. flows of data, people, materiel, or energy).

**Architecture** **Framework**

UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0

**Extension**

UML Information Flow

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="OMGBoldBulletKeepNextParagraph"><strong>Description</strong></p><p>Asserts that a flow can exist between Resource Performers (i.e. flows of data, people, materiel, or energy).</p><p><strong>Architecture</strong> <strong>Framework</strong></p><p><span style="color: rgb(62,63,64);">UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0</span></p><p><strong>Extension</strong></p><p>UML Information Flow</p><p><br /></p>
````

<!--NOMAGIC_PAGE id=228986056 space=MED version=2 -->
## PAGE 00377: Resource Exchange Item

- page_id: `228986056`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/228986056/Resource+Exchange+Item
- version_number: 2
- version_date: `2025-05-14T10:31:10.056+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UAF 1.3 elements
- labels: []

### NORMALIZED CONTENT

**Description**

An abstract grouping for elements that defines the types of elements that can be exchanged between Resource Performers and conveyed by a Resource Exchange.

**Architecture** **Framework**

UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="OMGBoldBulletKeepNextParagraph"><strong>Description</strong></p><p>An abstract grouping for elements that defines the types of elements that can be exchanged between Resource Performers and conveyed by a Resource Exchange.</p><p><strong>Architecture</strong> <strong>Framework</strong></p><p><span style="color: rgb(62,63,64);">UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0</span></p><p><br /></p>
````

<!--NOMAGIC_PAGE id=228986057 space=MED version=2 -->
## PAGE 00378: Resource Exchange Kind

- page_id: `228986057`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/228986057/Resource+Exchange+Kind
- version_number: 2
- version_date: `2025-05-14T10:31:10.360+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UAF 1.3 elements
- labels: []

### NORMALIZED CONTENT

**Description**

Enumeration of the possible kinds of resource exchange applicable to a ResourceExchange. Its enumeration literals are:

- ResourceCommunication - Indicates that the ResourceExchange associated with the ResourceExchangeKind is an implementation of the logical flow of data between Resources.
- ResourceMovement - Indicates that the ResourceExchange associated with the ResourceExchangeKind is an implementation of the logical flow of Resources between Resources.
- ResourceEnergyFlow - Indicates that the ResourceExchange associated with the ResourceExchangeKind is an implementation of the logical flow of natural resources between Resources.
- GeoPoliticalExtentExchange - Indicates that the ResourceExchange associated with the ResourceExchangeKind is an implementation of logical flow where GeoPoliticalExtents (i.e., Borders) flow from one place to another.

**Architecture Framework**

UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="OMGBoldBulletKeepNextParagraph"><strong>Description</strong></p><p class="OMGNormalParagraph">Enumeration of the possible kinds of resource exchange applicable to a ResourceExchange. Its enumeration literals are:</p><ul><li>ResourceCommunication - Indicates that the<span> </span><span style="color: rgb(62,63,64);">ResourceExchange<span> </span></span>associated with the<span> </span><span style="color: rgb(23,43,77);">ResourceExchangeKind<span> </span></span>is an implementation of the logical flow of data between Resources.</li><li>ResourceMovement - Indicates that the<span> </span><span style="color: rgb(62,63,64);">ResourceExchange<span> </span></span>associated with the<span> </span><span style="color: rgb(23,43,77);">ResourceExchangeKind<span> </span></span>is an implementation of the logical flow of Resources between Resources.</li><li>ResourceEnergyFlow - Indicates that the<span> </span><span style="color: rgb(62,63,64);">ResourceExchange<span> </span></span>associated with the<span> </span><span style="color: rgb(23,43,77);">ResourceExchangeKind<span> </span></span>is an implementation of the logical flow of natural resources between Resources.</li><li>GeoPoliticalExtentExchange - Indicates that the<span> </span><span style="color: rgb(62,63,64);">ResourceExchange<span> </span></span>associated with the<span> </span><span style="color: rgb(23,43,77);">ResourceExchangeKind<span> </span></span>is an implementation of logical flow where GeoPoliticalExtents (i.e., Borders) flow from one place to another.</li></ul><p><strong>Architecture Framework</strong></p><p><span style="color: rgb(62,63,64);">UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0</span></p>
````

<!--NOMAGIC_PAGE id=228986058 space=MED version=2 -->
## PAGE 00379: Resource Information

- page_id: `228986058`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/228986058/Resource+Information
- version_number: 2
- version_date: `2025-05-14T10:31:10.595+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UAF 1.3 elements
- labels: []

### NORMALIZED CONTENT

**Description**

A formalized representation of information that is managed by or exchanged between systems.

**Architecture Framework**

UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0

**Extensions**

Class

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description</strong></p><p class="OMGNormalParagraph">A formalized representation of information that is managed by or exchanged between systems.</p><p><span class="fontstyle0"><strong>Architecture Framework</strong></span></p><p><span style="color: rgb(62,63,64);">UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0</span></p><p><span class="fontstyle0"><strong>Extensions</strong></span></p><p><span class="fontstyle2">Class</span></p><p><br /></p>
````

<!--NOMAGIC_PAGE id=228986059 space=MED version=2 -->
## PAGE 00380: Resource Information Role

- page_id: `228986059`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/228986059/Resource+Information+Role
- version_number: 2
- version_date: `2025-05-14T10:31:10.846+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UAF 1.3 elements
- labels: []

### NORMALIZED CONTENT

**Description**

A usage of Resource Information that exists in the context of a Resource Asset. It also allows the representation of the whole-part aggregation of Resource Information elements.

**Architecture Framework**

UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0

**Extension**

Property

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description</strong></p><p class="OMGNormalParagraph">A usage of Resource Information that exists in the context of a Resource Asset. It also allows the representation of the whole-part aggregation of Resource Information elements.</p><p><strong><span style="color: rgb(62,63,64);">Architecture Framework</span></strong></p><p><span style="color: rgb(62,63,64);">UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0</span></p><p><strong><span style="color: rgb(62,63,64);">Extension</span></strong></p><p><span style="color: rgb(62,63,64);">Property</span></p>
````

<!--NOMAGIC_PAGE id=228986060 space=MED version=2 -->
## PAGE 00381: Resource Interface

- page_id: `228986060`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/228986060/Resource+Interface
- version_number: 2
- version_date: `2025-05-14T10:31:11.105+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UAF 1.3 elements
- labels: []

### NORMALIZED CONTENT

**Description**

A declaration that specifies a contract between the Resource Performers it is related to and any other Resource Performers it can interact with. It is also intended to be an implementation of a specification of an Interface in the Business and/or Service layer.

**Architecture Framework**

UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0

**Extension**

UML Class

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="OMGBoldBulletKeepNextParagraph"><strong>Description</strong></p><p class="OMGNormalParagraph">A declaration that specifies a contract between the Resource Performers it is related to and any other Resource Performers it can interact with. It is also intended to be an implementation of a specification of an Interface in the Business and/or Service layer. </p><p class="OMGNormalParagraph"><strong>Architecture Framework</strong></p><p class="OMGNormalParagraph"><span style="color: rgb(62,63,64);">UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0</span></p><p class="OMGNormalParagraph"><strong>Extension</strong></p><p class="OMGNormalParagraph">UML Class</p><p><br /></p>
````

<!--NOMAGIC_PAGE id=228986061 space=MED version=2 -->
## PAGE 00382: Resource Message

- page_id: `228986061`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/228986061/Resource+Message
- version_number: 2
- version_date: `2025-05-14T10:31:11.344+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UAF 1.3 elements
- labels: []

### NORMALIZED CONTENT

**Description**

Message for use in an Resource Event-Trace which carries any of the subtypes of Resource Exchange.

**Architecture** **Framework**

UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0

**Extension**

UML Message

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="OMGBoldBulletKeepNextParagraph"><strong>Description</strong></p><p class="OMGNormalParagraph">Message for use in an Resource Event-Trace which carries any of the subtypes of Resource Exchange. </p><p class="OMGNormalParagraph"><strong>Architecture</strong> <strong>Framework</strong></p><p class="OMGNormalParagraph"><span style="color: rgb(62,63,64);">UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0</span></p><p class="OMGNormalParagraph"><strong>Extension</strong></p><p class="OMGNormalParagraph">UML Message </p><p><br /></p>
````

<!--NOMAGIC_PAGE id=228986062 space=MED version=2 -->
## PAGE 00383: Resource Method

- page_id: `228986062`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/228986062/Resource+Method
- version_number: 2
- version_date: `2025-05-14T10:31:11.622+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UAF 1.3 elements
- labels: []

### NORMALIZED CONTENT

**Description**

A behavioral feature of a Resource Performer whose behavior is specified in a Function.

**Architecture** **Framework**

UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0

**Extension**

UML Operation

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="OMGBoldBulletKeepNextParagraph"><strong>Description</strong></p><p class="OMGNormalParagraph">A behavioral feature of a Resource Performer whose behavior is specified in a Function. </p><p class="OMGNormalParagraph"><strong>Architecture</strong> <strong>Framework</strong></p><p class="OMGNormalParagraph"><span style="color: rgb(62,63,64);">UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0</span></p><p class="OMGNormalParagraph"><strong>Extension</strong></p><p class="OMGNormalParagraph">UML Operation</p><p><br /></p>
````

<!--NOMAGIC_PAGE id=228986063 space=MED version=2 -->
## PAGE 00384: Resource Mitigation

- page_id: `228986063`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/228986063/Resource+Mitigation
- version_number: 2
- version_date: `2025-05-14T10:31:11.865+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UAF 1.3 elements
- labels: []

### NORMALIZED CONTENT

**Description**

A set of security measures intended to address specific cyber risks. Comprises a subset of Tailored Security Controls that are used to protect the asset at resource (Resource Role).

**Architecture** **Framework**

UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0

**Extension**

UML Class

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="OMGBoldBulletKeepNextParagraph"><strong>Description</strong></p><p class="OMGNormalParagraph">A set of security measures intended to address specific cyber risks. Comprises a subset of Tailored Security Controls that are used to protect the asset at resource (Resource Role).</p><p class="OMGNormalParagraph"><strong>Architecture</strong> <strong>Framework</strong></p><p class="OMGNormalParagraph"><span style="color: rgb(62,63,64);">UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0</span></p><p class="OMGNormalParagraph"><strong>Extension</strong></p><p class="OMGNormalParagraph">UML Class</p><p><br /></p>
````

<!--NOMAGIC_PAGE id=228986064 space=MED version=2 -->
## PAGE 00385: Resource Parameter

- page_id: `228986064`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/228986064/Resource+Parameter
- version_number: 2
- version_date: `2025-05-14T10:31:12.123+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UAF 1.3 elements
- labels: []

### NORMALIZED CONTENT

**Description**

An element that represents inputs and outputs of an Function. It is typed by a Resource Exchange Item.

**Architecture** **Framework**

UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0

**Extensions**

UML Parameter

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="OMGBoldBulletKeepNextParagraph"><strong>Description</strong></p><p class="OMGNormalParagraph">An element that represents inputs and outputs of an Function. It is typed by a Resource Exchange Item. </p><p><span class="fontstyle0"><strong>Architecture</strong> <strong>Framework</strong></span></p><p><span style="color: rgb(62,63,64);">UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0</span></p><p><strong><span class="fontstyle0">Extensions</span></strong></p><p><span class="fontstyle2">UML Parameter</span></p><p><br /></p>
````

<!--NOMAGIC_PAGE id=228986065 space=MED version=2 -->
## PAGE 00386: Resource Performer

- page_id: `228986065`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/228986065/Resource+Performer
- version_number: 2
- version_date: `2025-05-14T10:31:12.814+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UAF 1.3 elements
- labels: []

### NORMALIZED CONTENT

**Description**

An abstract grouping of elements that can perform Functions.

**Architecture Framework**

UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0

**Extension**

UML Class

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="OMGNormalParagraph"><strong>Description</strong></p><p class="OMGNormalParagraph">An abstract grouping of elements that can perform Functions.</p><p class="OMGNormalParagraph"><strong>Architecture Framework</strong></p><p class="OMGNormalParagraph"><span style="color: rgb(62,63,64);">UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0</span></p><p class="OMGNormalParagraph"><strong>Extension</strong></p><p class="OMGNormalParagraph">UML Class</p><p><br /></p>
````

<!--NOMAGIC_PAGE id=228986066 space=MED version=2 -->
## PAGE 00387: Resource Port

- page_id: `228986066`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/228986066/Resource+Port
- version_number: 2
- version_date: `2025-05-14T10:31:13.255+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UAF 1.3 elements
- labels: []

### NORMALIZED CONTENT

**Description**

An interaction point for a Resource Performer through which it can interact with the outside environment and which is defined by a Resource Interface.

**Architecture** **Framework**

UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0

**Extension**

UML Port

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="OMGBoldBulletKeepNextParagraph"><strong>Description</strong></p><p class="OMGNormalParagraph">An interaction point for a Resource Performer through which it can interact with the outside environment and which is defined by a Resource Interface.</p><p class="OMGNormalParagraph"><strong>Architecture</strong> <strong>Framework</strong></p><p class="OMGNormalParagraph"><span style="color: rgb(62,63,64);">UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0</span></p><p class="OMGNormalParagraph"><strong>Extension</strong></p><p class="OMGNormalParagraph">UML Port</p><p><br /></p>
````

<!--NOMAGIC_PAGE id=228986067 space=MED version=3 -->
## PAGE 00388: Resource Role

- page_id: `228986067`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/228986067/Resource+Role
- version_number: 3
- version_date: `2025-10-06T10:55:51.835+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UAF 1.3 elements
- labels: []

### NORMALIZED CONTENT

728086762

728086766

728086764

**Description**

Usage of a Resource Performer in the context of another Resource Performer. Creates a whole-part relationship.

**Architecture Framework**

UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0

**Extension**

UML Property

728086761

###### **Resource Role Kind mapping table by OMG specification**

For each Resource Role created under the Resource Performer (which is a context), a type (which is Resource Performer) should be assigned. Depending on a type, an appropriate Role Kind is assigned for each Resource Role according to the rules provided in the following table.

| Role Kind | Type | Context |
| --- | --- | --- |
| Artifact Component | Resource Artifact | Resource Performer |
| Component | Software | Resource Performer |
| Equipment | Physical Resource | Resource Performer |
| Hosted Software | Software | Resource Performer |
| Human Resource | Organizational Resource | Resource Performer |
| Natural Resource Component | Natural Resource | Resource Performer |
| Other | Resource Performer | Resource Performer |
| Part | Resource Performer | Resource Performer |
| Platform | Resource Performer | Resource Performer |
| Post Role | Post | Resource Performer |
| Responsibility Role | Responsibility | Resource Performer |
| System | Resource Performer | Resource Performer |
| Sub Organization | Organization | Resource Performer |
| Sub System Part | Resource Performer | Resource Performer |
| Used Configuration | Capability Configuration | Resource Performer |
| Used Physical Architecture | Resource Architecture | Resource Performer |

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="0ef8ad4f-7d39-4572-aab5-2875490f113d"><ac:parameter ac:name="id">728086762</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="4f57d44c-6389-4e00-979a-b6613c2af0e7"><ac:parameter ac:name="id">728086766</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="0f0ed212-d668-4e10-a226-b6422c010be0"><ac:parameter ac:name="id">728086764</ac:parameter><ac:rich-text-body><p class="OMGBoldBulletKeepNextParagraph"><strong>Description</strong></p><p class="OMGNormalParagraph">Usage of a Resource Performer in the context of another Resource Performer. Creates a whole-part relationship.</p><p class="OMGNormalParagraph"><strong>Architecture Framework</strong></p><p class="OMGNormalParagraph"><span style="color:var(--ds-text,#333333);">UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0</span></p><p class="OMGNormalParagraph"><strong>Extension</strong></p><p class="OMGNormalParagraph">UML Property</p><p><br /></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="d8b5a443-4b88-4085-8ce0-d4dad2adb50a"><ac:parameter ac:name="id">728086761</ac:parameter><ac:rich-text-body><h4><strong>Resource Role Kind mapping table by OMG specification</strong></h4><p>For each Resource Role created under the Resource Performer (which is a context), a type (which is Resource Performer) should be assigned. Depending on a type, an appropriate Role Kind is assigned for each Resource Role according to the rules provided in the following table.</p><table class="relative-table wrapped" style="width: 44.0761%;"><colgroup><col style="width: 33.5802%;" /><col style="width: 35.1852%;" /><col style="width: 31.2346%;" /></colgroup><tbody><tr><th>Role Kind</th><th>Type</th><th>Context</th></tr><tr><td>Artifact Component </td><td>Resource Artifact</td><td>Resource Performer</td></tr><tr><td>Component </td><td>Software </td><td>Resource Performer </td></tr><tr><td>Equipment </td><td>Physical Resource </td><td>Resource Performer</td></tr><tr><td>Hosted Software </td><td>Software </td><td>Resource Performer</td></tr><tr><td>Human Resource</td><td>Organizational Resource</td><td>Resource Performer </td></tr><tr><td>Natural Resource Component </td><td>Natural Resource</td><td>Resource Performer</td></tr><tr><td colspan="1">Other</td><td colspan="1">Resource Performer </td><td colspan="1">Resource Performer </td></tr><tr><td>Part </td><td>Resource Performer </td><td>Resource Performer </td></tr><tr><td>Platform </td><td>Resource Performer </td><td>Resource Performer </td></tr><tr><td>Post Role</td><td>Post</td><td>Resource Performer</td></tr><tr><td>Responsibility Role</td><td>Responsibility </td><td>Resource Performer</td></tr><tr><td>System </td><td>Resource Performer </td><td>Resource Performer </td></tr><tr><td>Sub Organization</td><td>Organization </td><td>Resource Performer </td></tr><tr><td>Sub System Part </td><td>Resource Performer</td><td>Resource Performer</td></tr><tr><td>Used Configuration </td><td>Capability Configuration</td><td>Resource Performer </td></tr><tr><td>Used Physical Architecture </td><td>Resource Architecture </td><td>Resource Performer</td></tr></tbody></table></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=228986068 space=MED version=2 -->
## PAGE 00389: Resource Service

- page_id: `228986068`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/228986068/Resource+Service
- version_number: 2
- version_date: `2025-05-14T10:31:13.826+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UAF 1.3 elements
- labels: []

### NORMALIZED CONTENT

**Description**

A services that a Resource Performer provides to support higher level Services or Operational Activities. Employee provisioning, backup and recovery, storage, self-service help desk are examples of Resource Services.

**Architecture Framework**

UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0

**Extensions**

Class

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description</strong></p><p class="OMGNormalParagraph">A services that a Resource Performer provides to support higher level Services or Operational Activities. Employee provisioning, backup and recovery, storage, self-service help desk are examples of Resource Services.</p><p><strong>Architecture Framework</strong></p><p><span style="color: rgb(62,63,64);">UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0</span></p><p><strong>Extensions</strong></p><p>Class</p>
````

<!--NOMAGIC_PAGE id=228986069 space=MED version=2 -->
## PAGE 00390: Resource Service Interface

- page_id: `228986069`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/228986069/Resource+Service+Interface
- version_number: 2
- version_date: `2025-05-14T10:31:14.409+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UAF 1.3 elements
- labels: []

### NORMALIZED CONTENT

**Description**

A contract that defines the Resource Methods and Resource Signal receptions that the Resource Services realize.

**Architecture Framework**

UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0

**Extensions**

Class

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description</strong></p><p class="OMGNormalParagraph">A contract that defines the Resource Methods and Resource Signal receptions that the Resource Services realize.</p><p class="OMGNormalParagraph"><strong>Architecture Framework</strong></p><p class="OMGNormalParagraph"><span style="color: rgb(62,63,64);">UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0</span></p><p class="OMGNormalParagraph"><strong>Extensions</strong></p><p class="OMGNormalParagraph">Class</p>
````

<!--NOMAGIC_PAGE id=228986070 space=MED version=2 -->
## PAGE 00391: Resource Signal

- page_id: `228986070`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/228986070/Resource+Signal
- version_number: 2
- version_date: `2025-05-14T10:31:14.850+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UAF 1.3 elements
- labels: []

### NORMALIZED CONTENT

**Description**

A ResourceSignal is a specification of a kind of communication between resources (Resource Performers) in which a reaction is asynchronously triggered in the receiver without a reply.

**Architecture Framework**

UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0

**Extension**

Signal

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description </strong></p><p>A ResourceSignal is a specification of a kind of communication between resources (Resource Performers) in which a reaction is asynchronously triggered in the receiver without a reply.</p><p><strong>Architecture Framework</strong></p><p><span style="color: rgb(62,63,64);">UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0</span></p><p><strong>Extension</strong></p><p>Signal</p>
````

<!--NOMAGIC_PAGE id=228986071 space=MED version=2 -->
## PAGE 00392: Resource State Description

- page_id: `228986071`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/228986071/Resource+State+Description
- version_number: 2
- version_date: `2025-05-14T10:31:15.254+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UAF 1.3 elements
- labels: []

### NORMALIZED CONTENT

**Description**

A state machine describing the behavior of a Resource Performer, depicting how the Resource Performer responds to various events and the actions.

**Architecture** **Framework**

UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0

**Extension**

UML StateMachine

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="OMGNormalParagraph"><strong>Description</strong></p><p>A state machine describing the behavior of a Resource Performer, depicting how the Resource Performer responds to various events and the actions.</p><p><strong>Architecture</strong> <strong>Framework</strong></p><p><span style="color: rgb(62,63,64);">UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0</span></p><p><strong>Extension</strong></p><p>UML StateMachine</p><p><br /></p>
````

<!--NOMAGIC_PAGE id=228986072 space=MED version=2 -->
## PAGE 00393: Responsibility

- page_id: `228986072`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/228986072/Responsibility
- version_number: 2
- version_date: `2025-05-14T10:31:15.513+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UAF 1.3 elements
- labels: []

### NORMALIZED CONTENT

**Description**

The type of duty required of a Person or Organization.

**Architecture Framework**

UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0

**Extension**

UML Class

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="OMGBoldBulletKeepNextParagraph"><strong>Description</strong></p><p class="OMGNormalParagraph">The type of duty required of a Person or Organization. </p><p class="OMGNormalParagraph"><strong>Architecture Framework</strong></p><p class="OMGNormalParagraph"><span style="color: rgb(62,63,64);">UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0</span></p><p class="OMGNormalParagraph"><strong>Extension</strong></p><p class="OMGNormalParagraph">UML Class</p><p><br /></p>
````

<!--NOMAGIC_PAGE id=228986073 space=MED version=2 -->
## PAGE 00394: Responsible For

- page_id: `228986073`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/228986073/Responsible+For
- version_number: 2
- version_date: `2025-05-14T10:31:15.777+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UAF 1.3 elements
- labels: []

### NORMALIZED CONTENT

**Description**

An abstraction relationship between an Actual Responsible Resource and an Actual Responsibility or Actual Project. It defines the duties that the Actual Responsible Resource is Responsible For.

**Architecture** **Framework**

UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0

**Extension**

Abstraction

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="OMGNormalParagraph"><strong>Description</strong></p><p class="OMGNormalParagraph">An abstraction relationship between an Actual Responsible Resource and an Actual Responsibility or Actual Project. It defines the duties that the Actual Responsible Resource is Responsible For.</p><p class="OMGNormalParagraph"><strong>Architecture</strong> <strong>Framework</strong></p><p class="OMGNormalParagraph"><span style="color: rgb(62,63,64);">UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0</span></p><p class="OMGNormalParagraph"><strong>Extension</strong></p><p class="OMGNormalParagraph">Abstraction</p><p><br /></p>
````

<!--NOMAGIC_PAGE id=228986074 space=MED version=2 -->
## PAGE 00395: Responsible Role Kind

- page_id: `228986074`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/228986074/Responsible+Role+Kind
- version_number: 2
- version_date: `2025-05-14T10:31:16.031+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UAF 1.3 elements
- labels: []

### NORMALIZED CONTENT

**Description**

Enumeration of the possible kinds of ResponsibleRole. Its enumeration literals are:

- Manager - Indicates that the ResourceExchange associated with the ResourceExchangeKind is an implementation of logical flow.
- ResponsibleOwner - Indicates that the ResourceExchange associated with the ResourceExchangeKind is an implementation of logical flow.

**Architecture Framework**

UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="OMGBoldBulletKeepNextParagraph"><strong>Description</strong></p><p class="OMGNormalParagraph">Enumeration of the possible kinds of ResponsibleRole. Its enumeration literals are:</p><ul><li>Manager - Indicates that the ResourceExchange associated with the ResourceExchangeKind is an implementation of logical flow.</li><li>ResponsibleOwner - Indicates that the ResourceExchange associated with the ResourceExchangeKind is an implementation of logical flow.</li></ul><p><strong>Architecture Framework</strong></p><p><span style="color: rgb(62,63,64);">UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0</span></p>
````

<!--NOMAGIC_PAGE id=228986075 space=MED version=2 -->
## PAGE 00396: Risk

- page_id: `228986075`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/228986075/Risk
- version_number: 2
- version_date: `2025-05-14T10:31:16.299+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UAF 1.3 elements
- labels: []

### NORMALIZED CONTENT

**Description**

A statement of the impact of an event on Assets. It represents a constraint on an Asset in terms of adverse effects, with an associated measure. The measure is used to capture the extent to which an entity is threatened by a potential circumstance or event. Risk is typically a function of:

- the adverse impacts that would arise if the circumstance or event occurs;
- the likelihood of occurrence. Software related security risks are those risks that arise from the loss of confidentiality, integrity, or availability of information or information systems.

**Architecture Framework**

UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description</strong></p><p>A statement of the impact of an event on Assets. It represents a constraint on an Asset in terms of adverse effects, with an associated measure. The measure is used to capture the extent to which an entity is threatened by a potential circumstance or event. Risk is typically a function of:</p><ul><li>the adverse impacts that would arise if the circumstance or event occurs;</li><li>the likelihood of occurrence. Software related security risks are those risks that arise from the loss of confidentiality, integrity, or availability of information or information systems.</li></ul><p><strong>Architecture Framework</strong></p><p><span style="color: rgb(62,63,64);">UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0</span></p>
````

<!--NOMAGIC_PAGE id=228986076 space=MED version=2 -->
## PAGE 00397: Role Kind

- page_id: `228986076`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/228986076/Role+Kind
- version_number: 2
- version_date: `2025-05-14T10:31:16.682+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UAF 1.3 elements
- labels: []

### NORMALIZED CONTENT

**Description**

Enumeration of the possible kinds of roles that a ResourceRole may play in the context of a ResourcePerformer. Its enumeration literals are:

- Part - Indicates that the ResourceRole associated with the ResourceRoleKind is a kind of a ResourcePerformer that is used as a part of another ResourcePerformer.
- Component - Indicates that the ResourceRole associated with the ResourceRoleKind is a kind of Software that is used in the context of a ResourcePerformer.
- UsedConfiguration - Indicates that the ResourceRole associated with the ResourceRoleKind is a kind of existing CapabilityConfiguration that is used in the context of a ResourcePerformer.
- HumanResource - Indicates that the ResourceRole associated with the ResourceRoleKind is a kind of human resource that is used in the context of a ResourcePerformer.
- Platform - Indicates that the ResourceRole associated with the ResourceRoleKind is a kind of a ResourcePerformer that represents a platform (e.g. vessel, aircraft, etc.) that is used in the context of a SystemsResource.
- System - Indicates that the ResourceRole associated with the ResourceRoleKind is a kind of assembly of ResourcePerformers that is used in the context of another ResourcePerformer.
- SubOrganization - Indicates that the ResourceRole associated with the ResourceRoleKind is a kind of Organization that is typically the parent of another - e.g. a squadron may be part of a batallion, that is used in the context of a ResourcePerformer.
- PostRole - Indicates that the ResourceRole associated with the ResourceRoleKind is a kind of Post that is used in the context of a ResourcePerformer.
- ResponsibilityRole - Indicates that the ResourceRole associated with the ResourceRoleKind is a kind of Responsibility associated with a role that is used in the context of a ResourcePerformer.
- Equipment - Indicates that the ResourceRole associated with the ResourceRoleKind is a kind of man made resource that is used to accomplish a task or function in the context of a ResourcePerformer.
- SubSystemPart - Indicates that the ResourceRole associated with the ResourceRoleKind is a kind of subsystem (represented as a ResourcePerformers) is is part of another ResourcePerformer.
- UsedPhysicalArchitecture - Indicates that the ResourceRole associated with the ResourceRoleKind is a kind of existing PhysicalArchitecture that is used in the context of a ResourcePerformer.
- HostedSoftware - Indicates that the ResourceRole associated with the ResourceRoleKind is a kind of software that is used in the context of a ResourcePerformer.
- ArtifactComponent - Indicates that the ResourceRole associated with the ResourceRoleKind is a kind of non human resource that is used as a component in the context of a ResourcePerformer.
- NaturalResourceComponent - Indicates that the ResourceRole associated with the ResourceRoleKind is a kind of natural resource that is used as a component in the context of a ResourcePerformer.
- Other - Indicates that the ResourceRole associated with the ResourceRoleKind is another kind of RoleKind that is not on the enumerated list.

**Architecture** **Framework**

UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="OMGBoldBulletKeepNextParagraph"><strong>Description</strong></p><p class="OMGNormalParagraph">Enumeration of the possible kinds of roles that a ResourceRole may play in the context of a ResourcePerformer. Its enumeration literals are:</p><ul><li>Part - Indicates that the ResourceRole associated with the ResourceRoleKind is a kind of a ResourcePerformer that is used as a part of another ResourcePerformer.</li><li>Component - Indicates that the ResourceRole associated with the ResourceRoleKind is a kind of Software that is used in the context of a ResourcePerformer.</li><li>UsedConfiguration - Indicates that the ResourceRole associated with the ResourceRoleKind is a kind of existing CapabilityConfiguration that is used in the context of a ResourcePerformer.</li><li>HumanResource - Indicates that the ResourceRole associated with the ResourceRoleKind is a kind of human resource that is used in the context of a ResourcePerformer.</li><li>Platform - Indicates that the ResourceRole associated with the ResourceRoleKind is a kind of a ResourcePerformer that represents  a platform (e.g. vessel, aircraft, etc.) that is used in the context of a SystemsResource.</li><li>System - Indicates that the ResourceRole associated with the ResourceRoleKind is a kind of assembly of ResourcePerformers that is used in the context of another ResourcePerformer.</li><li>SubOrganization - Indicates that the ResourceRole associated with the ResourceRoleKind is a kind of  Organization that is typically the parent of another - e.g. a squadron may be part of a batallion, that is used in the context of a ResourcePerformer.</li><li>PostRole - Indicates that the ResourceRole associated with the ResourceRoleKind is a kind of Post that is used in the context of a ResourcePerformer.</li><li>ResponsibilityRole - Indicates that the ResourceRole associated with the ResourceRoleKind is a kind of Responsibility associated with a role that is used in the context of a ResourcePerformer.</li><li>Equipment - Indicates that the ResourceRole associated with the ResourceRoleKind is a kind of man made resource that is used to accomplish a task or function in the context of a ResourcePerformer.</li><li>SubSystemPart - Indicates that the ResourceRole associated with the ResourceRoleKind is a kind of  subsystem (represented as a ResourcePerformers) is is part of another ResourcePerformer.</li><li>UsedPhysicalArchitecture - Indicates that the ResourceRole associated with the ResourceRoleKind is a kind of existing PhysicalArchitecture that is used in the context of a ResourcePerformer.</li><li>HostedSoftware - Indicates that the ResourceRole associated with the ResourceRoleKind is a kind of software that is used in the context of a ResourcePerformer.</li><li>ArtifactComponent - Indicates that the ResourceRole associated with the ResourceRoleKind is a kind of non human resource that is used as a component in the context of a ResourcePerformer.</li><li>NaturalResourceComponent - Indicates that the ResourceRole associated with the ResourceRoleKind is a kind of natural resource that is used as a component in the context of a ResourcePerformer.</li><li>Other - Indicates that the ResourceRole associated with the ResourceRoleKind is another kind of RoleKind that is not on the enumerated list.</li></ul><p><strong>Architecture</strong> <strong>Framework</strong></p><p><span style="color: rgb(62,63,64);">UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0</span></p>
````

<!--NOMAGIC_PAGE id=228986077 space=MED version=2 -->
## PAGE 00398: Rule

- page_id: `228986077`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/228986077/Rule
- version_number: 2
- version_date: `2025-05-14T10:31:16.950+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UAF 1.3 elements
- labels: []

### NORMALIZED CONTENT

**Description**

An abstract grouping for all types of constraint (i.e. an Operational Constraint could detail the rules of accountancy best practice).

**Architecture Framework**

UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0

**Extension**

UML Constraint

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="OMGNormalParagraph"><strong>Description</strong></p><p class="OMGNormalParagraph">An abstract grouping for all types of constraint (i.e. an Operational Constraint could detail the rules of accountancy best practice).</p><p class="OMGNormalParagraph"><strong>Architecture Framework</strong></p><p class="OMGNormalParagraph"><span style="color: rgb(62,63,64);">UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0</span></p><p class="OMGNormalParagraph"><strong>Extension</strong></p><p class="OMGNormalParagraph">UML Constraint</p><p><br /></p>
````

<!--NOMAGIC_PAGE id=236847179 space=MED version=2 -->
## PAGE 00399: Rule Kind

- page_id: `236847179`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/236847179/Rule+Kind
- version_number: 2
- version_date: `2025-06-30T12:34:22.000+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UAF 1.3 elements
- labels: []

### NORMALIZED CONTENT

**Description** 
Enumeration of the possible kinds of Rules applicable to constraints. Its enumeration literals are:

- **StructuralAssertion** – Indicates that the Rule associated with the RuleKind is a statement that details that something of importance either exists as a concept of interest or exists in relationship to another thing of interest.
- **ActionAssertion** – Indicates that the Rule associated with the RuleKind is a statement that concerns some dynamic aspect.
- **Derivation** – Indicates that the Rule associated with the RuleKind is a statement that details a Rule derived from another Rule.
- **Contract** – Indicates that the Rule associated with the RuleKind is a statement that details a consent among parties regarding the terms and conditions of activities that said parties participate in.
- **Constraint** – Indicates that the Rule associated with the RuleKind is a statement that details a limitation, e.g., business rule, restraint, or operational limitation.
- **Guidance** – Indicates that the Rule associated with the RuleKind is a statement that details an authoritative statement intended to lead or steer the execution of actions.
- **SecurityPolicy** – Indicates that the Rule associated with the RuleKind is a statement that details a constraint that specifies policy for information handling, physical security, encryption, etc.
- **Caveat** – Indicates that the Rule associated with the RuleKind is a statement that details alternate conditions under which the rule is not valid.
- **Assumption** – Indicates that the Rule element is accepted as true or as certain to happen, without proof.

**Architecture Framework**

UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description</strong><br />Enumeration of the possible kinds of Rules applicable to constraints. Its enumeration literals are:</p><ul><li data-uuid="a94a9010-6c8d-4710-83cc-142bd671be84"><p><strong>StructuralAssertion</strong> – Indicates that the Rule associated with the RuleKind is a statement that details that something of importance either exists as a concept of interest or exists in relationship to another thing of interest.</p></li><li data-uuid="3ba80f96-8498-4e40-b5ce-1b4978dd2c04"><p><strong>ActionAssertion</strong> – Indicates that the Rule associated with the RuleKind is a statement that concerns some dynamic aspect.</p></li><li data-uuid="f2aaaf98-149f-4657-9098-39caa12d5cb4"><p><strong>Derivation</strong> – Indicates that the Rule associated with the RuleKind is a statement that details a Rule derived from another Rule.</p></li><li data-uuid="46330b3d-1c27-483e-b1ef-ae8dcb022b21"><p><strong>Contract</strong> – Indicates that the Rule associated with the RuleKind is a statement that details a consent among parties regarding the terms and conditions of activities that said parties participate in.</p></li><li data-uuid="9a86f721-d1b4-4e99-b8ff-f15f4a108376"><p><strong>Constraint</strong> – Indicates that the Rule associated with the RuleKind is a statement that details a limitation, e.g., business rule, restraint, or operational limitation.</p></li><li data-uuid="3521d72a-c1cd-437c-aca3-c4de6f2e19b0"><p><strong>Guidance</strong> – Indicates that the Rule associated with the RuleKind is a statement that details an authoritative statement intended to lead or steer the execution of actions.</p></li><li data-uuid="6ec394d1-4a19-469d-a41e-f5422630c670"><p><strong>SecurityPolicy</strong> – Indicates that the Rule associated with the RuleKind is a statement that details a constraint that specifies policy for information handling, physical security, encryption, etc.</p></li><li data-uuid="1642e487-d887-4786-9a80-58d7f81db8b3"><p><strong>Caveat</strong> – Indicates that the Rule associated with the RuleKind is a statement that details alternate conditions under which the rule is not valid.</p></li><li data-uuid="a5177de7-7f8b-410b-a1d8-14fe3373b4ba"><p><strong>Assumption</strong> – Indicates that the Rule element is accepted as true or as certain to happen, without proof.</p></li></ul><p class="OMGNormalParagraph" style="text-align: left;"><strong>Architecture Framework</strong></p><p class="OMGNormalParagraph" style="text-align: left;"><span style="color:var(--ds-text-accent-magenta-bolder,#50253f);">UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0</span></p>
````

<!--NOMAGIC_PAGE id=228986078 space=MED version=2 -->
## PAGE 00400: Same As

- page_id: `228986078`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/228986078/Same+As
- version_number: 2
- version_date: `2025-05-14T10:31:17.216+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UAF 1.3 elements
- labels: []

### NORMALIZED CONTENT

**Description**

Asserts that two elements refer to the same real-world thing.

**Architecture Framework**

UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0

**Extensions**

UML Dependency

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong><span class="fontstyle0">Description</span></strong></p><p><span class="fontstyle0"> </span><span class="fontstyle1">Asserts that two elements refer to the same real-world thing.</span></p><p><span class="fontstyle1"> </span><strong><span class="fontstyle0">Architecture Framework</span></strong></p><p><span style="color: rgb(62,63,64);">UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0</span></p><p><span class="fontstyle1"> </span><strong><span class="fontstyle0">Extensions</span></strong></p><p><span class="fontstyle0"> </span><span class="fontstyle1">UML Dependency</span></p><p><br /></p>
````

<!--NOMAGIC_PAGE id=249005184 space=MED version=2 -->
## PAGE 00401: Satisfy

- page_id: `249005184`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/249005184/Satisfy
- version_number: 2
- version_date: `2025-09-13T12:46:31.485+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > Requirement-related elements
- labels: []

### NORMALIZED CONTENT

946309211

946309223

946309213

INLINE

A 'Satisfy' relationship is a dependency between a requirement and a model element that fulfills that requirement. As with other dependencies, the arrow direction points from the satisfying (client) model element to the (supplier) requirement that is satisfied.

[IMAGE alt='' src='']

946309210

**Related pages**

- [CONFLUENCE_PAGE title='Requirement Diagram' space='']
- [CONFLUENCE_PAGE title='Requirement Table' space='']
- [CONFLUENCE_PAGE title='Requirement matrices1' space='MT']

****

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="d4e223cd-608e-4ee3-9763-62efe11fd252"><ac:parameter ac:name="id">946309211</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="b9b3bf01-dbaa-4a92-8609-f456ebefdd15"><ac:parameter ac:name="id">946309223</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="01ae28f7-9cb1-4e22-b19c-5dc6a0976a82"><ac:parameter ac:name="id">946309213</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="excerpt" ac:schema-version="1" ac:macro-id="7dd48974-36fd-41c1-b1d6-e67d70c23813"><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><p>A 'Satisfy' relationship is a dependency between a requirement and a model element that fulfills that requirement. As with other dependencies, the arrow direction points from the satisfying (client) model element to the (supplier) requirement that is satisfied.</p><p><ac:image><ri:attachment ri:filename="satisfy_relationship.png" /></ac:image></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="90905ab3-3eec-4177-8a9d-b6466ba2309c"><ac:parameter ac:name="id">946309210</ac:parameter><ac:rich-text-body><p class="auto-cursor-target"><strong>Related pages</strong></p><ul><li><span class="confluence-link"><ac:link><ri:page ri:content-title="Requirement Diagram" /></ac:link></span></li><li><span class="confluence-link"><ac:link><ri:page ri:content-title="Requirement Table" /></ac:link></span></li><li><span class="confluence-link"><ac:link><ri:page ri:space-key="MT" ri:content-title="Requirement matrices1" /><ac:plain-text-link-body><![CDATA[Satisfy Requirement Matrix]]></ac:plain-text-link-body></ac:link></span></li></ul><p><strong><br /></strong></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=228986079 space=MED version=2 -->
## PAGE 00402: Security Constraint

- page_id: `228986079`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/228986079/Security+Constraint
- version_number: 2
- version_date: `2025-05-14T10:31:17.515+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UAF 1.3 elements
- labels: []

### NORMALIZED CONTENT

**Description**

A type of rule that captures a formal statement to define security laws, regulations, guidances, and policy.

**Architecture Framework**

UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0

**Extension**

UML Constraint

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="OMGNormalParagraph"><strong>Description</strong></p><p>A type of rule that captures a formal statement to define security laws, regulations, guidances, and policy.</p><p><strong>Architecture Framework</strong></p><p><span style="color: rgb(62,63,64);">UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0</span></p><p><strong>Extension</strong></p><p>UML Constraint</p><p><br /></p>
````

<!--NOMAGIC_PAGE id=228986080 space=MED version=2 -->
## PAGE 00403: Security Control

- page_id: `228986080`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/228986080/Security+Control
- version_number: 2
- version_date: `2025-05-14T10:31:17.819+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UAF 1.3 elements
- labels: []

### NORMALIZED CONTENT

**Description**

The management, operational, and technical control (i.e., safeguard or countermeasure) prescribed for an information system to protect the confidentiality, integrity, and availability of the system and its information.

**Architecture Framework**

UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0

**Extension**

UML Class

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="OMGNormalParagraph"><strong>Description</strong></p><p>The management, operational, and technical control (i.e., safeguard or countermeasure) prescribed for an information system to protect the confidentiality, integrity, and availability of the system and its information.</p><p class="OMGNormalParagraph"><strong>Architecture Framework</strong></p><p class="OMGNormalParagraph"><span style="color: rgb(62,63,64);">UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0</span></p><p class="OMGNormalParagraph"><strong>Extension</strong></p><p class="OMGNormalParagraph">UML Class</p><p><br /></p>
````

<!--NOMAGIC_PAGE id=228986081 space=MED version=2 -->
## PAGE 00404: Security Control Action

- page_id: `228986081`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/228986081/Security+Control+Action
- version_number: 2
- version_date: `2025-05-14T10:31:18.114+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UAF 1.3 elements
- labels: []

### NORMALIZED CONTENT

**Description**

A call of a Security Control in the context of another Security Control. It is used to show how a set of Security Controls can be used to protect an asset in a particular context.

**Architecture Framework**

UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0

**Extension**

UML Call Behavior Action

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="OMGNormalParagraph"><strong>Description</strong></p><p class="OMGNormalParagraph">A call of a Security Control in the context of another Security Control. It is used to show how a set of Security Controls can be used to protect an asset in a particular context. </p><p class="OMGNormalParagraph"><strong>Architecture Framework</strong></p><p class="OMGNormalParagraph"><span style="color: rgb(62,63,64);">UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0</span></p><p class="OMGNormalParagraph"><strong>Extension</strong></p><p class="OMGNormalParagraph">UML Call Behavior Action</p><p><br /></p>
````

<!--NOMAGIC_PAGE id=228986082 space=MED version=2 -->
## PAGE 00405: Security Control Family

- page_id: `228986082`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/228986082/Security+Control+Family
- version_number: 2
- version_date: `2025-05-14T10:31:18.390+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UAF 1.3 elements
- labels: []

### NORMALIZED CONTENT

**Description**

An element that organizes security controls into a family.

**Architecture Framework**

UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0

**Extension**

UML Comment

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="OMGNormalParagraph"><strong>Description</strong></p><p class="OMGNormalParagraph">An element that organizes security controls into a family. </p><p class="OMGNormalParagraph"><strong>Architecture Framework</strong></p><p class="OMGNormalParagraph"><span style="color: rgb(62,63,64);">UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0</span></p><p class="OMGNormalParagraph"><strong>Extension</strong></p><p class="OMGNormalParagraph">UML Comment</p><p><br /></p>
````

<!--NOMAGIC_PAGE id=228986083 space=MED version=2 -->
## PAGE 00406: Security Enclave

- page_id: `228986083`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/228986083/Security+Enclave
- version_number: 2
- version_date: `2025-05-14T10:31:18.656+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UAF 1.3 elements
- labels: []

### NORMALIZED CONTENT

**Description**

Collection of information systems connected by one or more internal networks under the control of a single authority and security policy. The systems may be structured by physical proximity or by function, independent of location.

**Architecture** **Framework**

UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0

**Extension**

UML Class

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="OMGNormalParagraph"><strong>Description</strong></p><p>Collection of information systems connected by one or more internal networks under the control of a single authority and security policy. The systems may be structured by physical proximity or by function, independent of location.</p><p><strong>Architecture</strong> <strong>Framework</strong></p><p><span style="color: rgb(62,63,64);">UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0</span></p><p><strong>Extension</strong></p><p>UML Class</p><p><br /></p>
````

<!--NOMAGIC_PAGE id=228986084 space=MED version=2 -->
## PAGE 00407: Security Process

- page_id: `228986084`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/228986084/Security+Process
- version_number: 2
- version_date: `2025-05-14T10:31:18.924+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UAF 1.3 elements
- labels: []

### NORMALIZED CONTENT

**Description**

The security-related procedure that satisfies the security control requirement.

**Architecture Framework**

UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0

**Extension**

UML Activity

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description </strong></p><p>The security-related procedure that satisfies the security control requirement.</p><p><strong>Architecture Framework</strong></p><p><span style="color: rgb(62,63,64);">UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0</span></p><p><strong>Extension</strong></p><p>UML Activity</p>
````

<!--NOMAGIC_PAGE id=228986085 space=MED version=2 -->
## PAGE 00408: Security Process Action

- page_id: `228986085`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/228986085/Security+Process+Action
- version_number: 2
- version_date: `2025-05-14T10:31:19.325+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UAF 1.3 elements
- labels: []

### NORMALIZED CONTENT

**Description**

A call of a SecurityProcess in the context of another SecurityProcess.

**Architecture Framework**

UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0

**Extension**

Call Behavior Action

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description </strong></p><p>A call of a SecurityProcess in the context of another SecurityProcess.</p><p><strong>Architecture Framework</strong></p><p><span style="color: rgb(62,63,64);">UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0</span></p><p><strong>Extension</strong></p><p>Call Behavior Action</p>
````

<!--NOMAGIC_PAGE id=228986086 space=MED version=2 -->
## PAGE 00409: Security Risk

- page_id: `228986086`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/228986086/Security+Risk
- version_number: 2
- version_date: `2025-05-14T10:31:19.626+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UAF 1.3 elements
- labels: []

### NORMALIZED CONTENT

**Description**

The level of impact on enterprise operations, assets, or individuals resulting from the operation of an information system given the potential impact of a threat and the likelihood of that threat occurring [NIST SP 800-65].

**Architecture Framework**

UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0

**Extensions**

Class

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description</strong></p><p>The level of impact on enterprise operations, assets, or individuals resulting from the operation of an information system given the potential impact of a threat and the likelihood of that threat occurring [NIST SP 800-65].</p><p><strong>Architecture Framework</strong></p><p><span style="color: rgb(62,63,64);">UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0</span></p><p><strong>Extensions</strong></p><p>Class</p>
````

<!--NOMAGIC_PAGE id=243967481 space=MED version=2 -->
## PAGE 00410: Send Signal Action

- page_id: `243967481`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/243967481/Send+Signal+Action
- version_number: 2
- version_date: `2025-09-13T12:42:56.373+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UML elements > Action
- labels: []

### NORMALIZED CONTENT

846228484

846228486

846228485

The Send Signal Action creates a signal instance from its inputs and transmits it to the target object, where it can cause the start of a [CONFLUENCE_PAGE title='State' space=''] transition or the execution of an Activity. The argument values are available to the execution of associated [CONFLUENCE_PAGE title='Behavior' space='']. The requester continues the execution immediately. Any reply [CONFLUENCE_PAGE title='Message' space=''] is ignored and is not transmitted to the requester. If the input is already a Signal instance, use the Send Signal Action.

| Notation | Description |
| --- | --- |
| Send Signal Action | This example describes an order process.First, an order is created (the Create order ).Next, a Signal to fill the order request is sent to the warehouse (the Fill order request Send Signal Action).Finally, an invoice is created (the Create invoice Call Behavior Action). The relationships are represented with Control Flow paths. |

##### Assigning signals

To assign a Signal to a Send Signal Action, you can use any of the following:

- [CONFLUENCE_PAGE title='Specification window' space='MT']
- 
- 
- 

specificationTo assign a Signal via the Send Signal Action’s Specification window

1. Open the [CONFLUENCE_PAGE title='Specification window' space='MT'] for the Send Signal Action.
2. In the Signal property value cell, do any of the following

- 
  - Click the [ATTACHMENT filename='edit_button.png'] button. The Select Signal dialog opens. Select the Signal from the list, or [CONFLUENCE_PAGE title='Creating new elements' space='MT'] .
  - Click the button [ATTACHMENT filename='expand.png'] to open the list of Signals available in the project. Select the Signal from the list. [ATTACHMENT filename='send_signal_action_signal_list.png']
  - Click Close once the Signal is selected.

darg_n_dropTo assign a signal using a drag-and-drop operation

1. Select the Signal in the [CONFLUENCE_PAGE title='Containment tab' space='MT'] .
2. Drag the Signal to the Send Signal Action as shown in the following picture. [ATTACHMENT filename='send_signal_action_drag_signal.png']

shortcutTo assign a signal using the Send Signal Action shortcut menu

1. Right-click the Send Signal Action to open the [CONFLUENCE_PAGE title='DH Links panel shortcut menu and Sync Status icons' space='CDH'] .
2. Click Signal . The list of Signals available in the project opens.
3. Select the Signal from the list, or click **New Signal** and [CONFLUENCE_PAGE title='Creating new elements' space='MT'].

typeTo assign a signal by typing the Send Signal Action name

1. Select the Send Signal Action shape, click on it to activate the name edit mode.
2. Do one of the following: - if you want to use an existing Signal from the model, start typing an appropriate Signal name, and select it from the opened list. - if you want to create a new Signal in the model, type its name and press Enter.

846286589

**Related pages**

- [CONFLUENCE_PAGE title='Action' space='']
- [CONFLUENCE_PAGE title='State Machine diagram' space='MT']
- [CONFLUENCE_PAGE title='Activity diagram' space='MT']
- [CONFLUENCE_PAGE title='UML elements' space='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="28626fb4-7687-466d-9989-db5091046e05"><ac:parameter ac:name="id">846228484</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="f22fd6b9-a643-435c-adf3-e29100bf75dc"><ac:parameter ac:name="id">846228486</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="79f8b413-0c7f-4f1e-a169-991f98f3dabc"><ac:parameter ac:name="id">846228485</ac:parameter><ac:rich-text-body><ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p>The Send Signal Action creates a signal instance from its inputs and transmits it to the target object, where it can cause the start of a <ac:link><ri:page ri:content-title="State" /><ac:plain-text-link-body><![CDATA[State Machine]]></ac:plain-text-link-body></ac:link> transition or the execution of an Activity. The argument values are available to the execution of associated <ac:link><ri:page ri:content-title="Behavior" /><ac:plain-text-link-body><![CDATA[Behaviors]]></ac:plain-text-link-body></ac:link>. The requester continues the execution immediately. Any reply <ac:link><ri:page ri:content-title="Message" /></ac:link> is ignored and is not transmitted to the requester. If the input is already a Signal instance, use the Send Signal Action.</p><table class="wrapped"><colgroup><col /><col /></colgroup><tbody><tr><th>Notation</th><th>Description</th></tr><tr><td><div class="content-wrapper"><p>Send Signal Action</p><p><ac:image><ri:attachment ri:filename="send_signal_action_sample.png" /></ac:image></p></div></td><td><p>This example describes an order process.</p><ol><li>First, an order is created (the <em>Create order</em> <ac:link><ri:page ri:content-title="Call Behavior Action" /></ac:link>).</li><li>Next, a Signal to fill the order request is sent to the warehouse (the <em>Fill order request S</em>end Signal Action).</li><li>Finally, an invoice is created (the <em>Create invoice</em> Call Behavior Action). The relationships are represented with Control Flow paths.</li></ol></td></tr></tbody></table></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><br /></p><h3>Assigning signals</h3><p><br />To assign a Signal to a Send Signal Action, you can use any of the following:</p><ul><li><ac:link ac:anchor="specification"><ac:plain-text-link-body><![CDATA[the Send Signal Action's ]]></ac:plain-text-link-body></ac:link> <ac:link><ri:page ri:space-key="MT" ri:content-title="Specification window" /></ac:link></li><li><ac:link ac:anchor="darg_n_dr"><ac:plain-text-link-body><![CDATA[the drag-and-drop operation]]></ac:plain-text-link-body></ac:link></li><li><ac:link ac:anchor="shortcut"><ac:plain-text-link-body><![CDATA[the Send Signal Action's shortcut menu]]></ac:plain-text-link-body></ac:link></li><li><ac:link ac:anchor="type"><ac:plain-text-link-body><![CDATA[type the Send Signal Action name]]></ac:plain-text-link-body></ac:link></li></ul><p><br /></p><p><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="76a747ba-efae-40a1-bf2c-5491088b56f5"><ac:parameter ac:name="">specification</ac:parameter></ac:structured-macro>To assign a Signal via the Send Signal Action’s Specification window</p><hr /><ol><li>Open the <ac:link><ri:page ri:space-key="MT" ri:content-title="Specification window" /></ac:link> for the Send Signal Action.</li><li>In the <strong>Signal</strong> property value cell, do any of the following</li></ol><ul><li style="list-style-type: none;background-image: none;"><ul><li>Click the <ac:image><ri:attachment ri:filename="edit_button.png"><ri:page ri:space-key="MT" ri:content-title="_MD buttons" /></ri:attachment></ac:image> button. The <strong>Select Signal</strong> dialog opens. Select the Signal from the list, or <ac:link><ri:page ri:space-key="MT" ri:content-title="Creating new elements" /><ac:plain-text-link-body><![CDATA[create a new one]]></ac:plain-text-link-body></ac:link>.</li><li>Click the button <ac:image><ri:attachment ri:filename="expand.png"><ri:page ri:space-key="MT" ri:content-title="_MD buttons" /></ri:attachment></ac:image> to open the list of Signals available in the project. Select the Signal from the list.<br /><ac:image><ri:attachment ri:filename="send_signal_action_signal_list.png" /></ac:image></li><li>Click <strong>Close</strong> once the Signal is selected.</li></ul></li></ul><p><br /></p><p><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="d3f43334-1460-4f2c-9e4e-4afc7884f385"><ac:parameter ac:name="">darg_n_drop</ac:parameter></ac:structured-macro>To assign a signal using a drag-and-drop operation</p><hr /><ol><li>Select the Signal in the <ac:link><ri:page ri:space-key="MT" ri:content-title="Containment tab" /><ac:plain-text-link-body><![CDATA[Containment tree]]></ac:plain-text-link-body></ac:link>.</li><li>Drag the Signal to the Send Signal Action as shown in the following picture.<br /><ac:image ac:title="Signal dragging to Send Signal Action" ac:alt="Signal dragging to Send Signal Action"><ri:attachment ri:filename="send_signal_action_drag_signal.png" /></ac:image></li></ol><p><br /></p><p><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="a0e5ca34-0fef-4704-9300-12c25e62d5b7"><ac:parameter ac:name="">shortcut</ac:parameter></ac:structured-macro>To assign a signal using the Send Signal Action shortcut menu</p><hr /><ol><li>Right-click the Send Signal Action to open the <ac:link><ri:page ri:space-key="CDH" ri:content-title="DH Links panel shortcut menu and Sync Status icons" /><ac:plain-text-link-body><![CDATA[shortcut menu]]></ac:plain-text-link-body></ac:link>.</li><li>Click <strong>Signal</strong>. The list of Signals available in the project opens.</li><li><p>Select the Signal from the list, or click <strong>New Signal</strong> and <ac:link><ri:page ri:space-key="MT" ri:content-title="Creating new elements" /><ac:plain-text-link-body><![CDATA[create a new one]]></ac:plain-text-link-body></ac:link>.</p></li></ol><p><br /></p><p><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="b426e83b-17e8-4be4-8700-2d1836fc5d68"><ac:parameter ac:name="">type</ac:parameter></ac:structured-macro>To assign a signal by typing the Send Signal Action name</p><hr /><ol><li>Select the Send Signal Action shape, click on it to activate the name edit mode.</li><li>Do one of the following:<br /> - if you want to use an existing Signal from the model, start typing an appropriate Signal name, and select it from the opened list.<br /> - if you want to create a new Signal in the model, type its name and press Enter.</li></ol></ac:layout-cell></ac:layout-section></ac:layout></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="c6a49aa6-f7ba-4e6c-aede-737bbe233aaf"><ac:parameter ac:name="id">846286589</ac:parameter><ac:rich-text-body><p><strong>Related pages</strong></p><ul><li><ac:link><ri:page ri:content-title="Action" /></ac:link></li><li><ac:link><ri:page ri:space-key="MT" ri:content-title="State Machine diagram" /></ac:link></li><li><ac:link><ri:page ri:space-key="MT" ri:content-title="Activity diagram" /></ac:link></li><li><ac:link><ri:page ri:content-title="UML elements" /><ac:plain-text-link-body><![CDATA[Model Elements]]></ac:plain-text-link-body></ac:link></li></ul></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=9919457 space=MED version=2 -->
## PAGE 00411: Sensor

- page_id: `9919457`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/9919457/Sensor
- version_number: 2
- version_date: `2025-09-13T12:46:25.171+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > SysML v1 elements
- labels: []

### NORMALIZED CONTENT

A Sensor is a special external system that forwards information from the environment to the system under development.

#### TIP: Example

Example

- Temperature sensor.

#### PANEL: Related diagrams

Related diagrams

- [CONFLUENCE_PAGE title='SysML Use Case Diagram' space='MT']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p>A Sensor is a special external system that forwards information from the environment to the system under development.</p><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="0ca8ebfb-7889-4c69-b967-731d97966708"><ac:parameter ac:name="title">Example</ac:parameter><ac:rich-text-body><ul><li>Temperature sensor.</li></ul></ac:rich-text-body></ac:structured-macro></ac:layout-cell><ac:layout-cell><p> </p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p> </p></ac:layout-cell><ac:layout-cell><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="de9adc89-d387-43d7-a667-124571a795a9"><ac:parameter ac:name="title">Related diagrams</ac:parameter><ac:rich-text-body><ul><li><ac:link><ri:page ri:space-key="MT" ri:content-title="SysML Use Case Diagram" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=228986087 space=MED version=2 -->
## PAGE 00412: Sequence

- page_id: `228986087`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/228986087/Sequence
- version_number: 2
- version_date: `2025-05-14T10:31:19.912+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UAF 1.3 elements
- labels: []

### NORMALIZED CONTENT

**Description**

A dependency relationship that asserts one Individual's temporal extent is completely before the temporal extent of another.

**Architecture Framework**

UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0

**Extensions**

Dependency

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description</strong></p><p>A dependency relationship that asserts one Individual's temporal extent is completely before the temporal extent of another.</p><p><strong>Architecture Framework</strong></p><p><span style="color: rgb(62,63,64);">UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0</span></p><p><strong>Extensions</strong></p><p>Dependency</p>
````

<!--NOMAGIC_PAGE id=228986088 space=MED version=2 -->
## PAGE 00413: Service

- page_id: `228986088`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/228986088/Service
- version_number: 2
- version_date: `2025-05-14T10:31:20.257+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UAF 1.3 elements
- labels: []

### NORMALIZED CONTENT

**Description**

A mechanism to enable access to one or more capabilities, where the access is provided using a prescribed service interface and is exercised consistent with service constraints and policies.

**Architecture** **Framework**

UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0

**Extension**

Class

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="OMGNormalParagraph"><strong>Description</strong></p><p class="OMGNormalParagraph">A mechanism to enable access to one or more capabilities, where the access is provided using a prescribed service interface and is exercised consistent with service constraints and policies.</p><p class="OMGNormalParagraph"><strong>Architecture</strong> <strong>Framework</strong></p><p class="OMGNormalParagraph"><span style="color: rgb(62,63,64);">UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0</span></p><p class="OMGNormalParagraph"><strong>Extension</strong></p><p class="OMGNormalParagraph">Class</p><p><br /></p>
````

<!--NOMAGIC_PAGE id=228986089 space=MED version=2 -->
## PAGE 00414: Service Architecture

- page_id: `228986089`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/228986089/Service+Architecture
- version_number: 2
- version_date: `2025-05-14T10:31:20.509+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UAF 1.3 elements
- labels: []

### NORMALIZED CONTENT

**Description**

An element used to denote a model of the Architecture, described from the Services perspective.

**Architecture Framework**

UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0

**Extensions**

Class

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description</strong></p><p class="OMGNormalParagraph">An element used to denote a model of the Architecture, described from the Services perspective.</p><p><strong>Architecture Framework</strong></p><p><span style="color: rgb(62,63,64);">UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0</span></p><p><strong>Extensions</strong></p><p>Class</p>
````

<!--NOMAGIC_PAGE id=228986090 space=MED version=2 -->
## PAGE 00415: Service Connector

- page_id: `228986090`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/228986090/Service+Connector
- version_number: 2
- version_date: `2025-05-14T10:31:20.750+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UAF 1.3 elements
- labels: []

### NORMALIZED CONTENT

**Description**

A channel for exchange between two Service Specifications. Where one acts as the consumer of the other.

**Architecture** **Framework**

UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0

**Extension**

UML Connector

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="OMGNormalParagraph"><strong>Description</strong></p><p class="OMGNormalParagraph">A channel for exchange between two Service Specifications. Where one acts as the consumer of the other. </p><p class="OMGNormalParagraph"><strong>Architecture</strong> <strong>Framework</strong></p><p class="OMGNormalParagraph"><span style="color: rgb(62,63,64);">UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0</span></p><p class="OMGNormalParagraph"><strong>Extension</strong></p><p class="OMGNormalParagraph">UML Connector</p><p><br /></p>
````

<!--NOMAGIC_PAGE id=228986091 space=MED version=2 -->
## PAGE 00416: Service Contract

- page_id: `228986091`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/228986091/Service+Contract
- version_number: 2
- version_date: `2025-05-14T10:31:21.035+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UAF 1.3 elements
- labels: []

### NORMALIZED CONTENT

**Description**

A constraint governing the use of one or more Services.

**Architecture Framework**

UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0

**Extensions**

Constraint

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description</strong></p><p class="OMGNormalParagraph">A constraint governing the use of one or more Services.</p><p class="OMGNormalParagraph"><strong>Architecture Framework</strong></p><p class="OMGNormalParagraph"><span style="color: rgb(62,63,64);">UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0</span></p><p class="OMGNormalParagraph"><strong>Extensions</strong></p><p class="OMGNormalParagraph">Constraint</p>
````

<!--NOMAGIC_PAGE id=228986092 space=MED version=2 -->
## PAGE 00417: Service Control Flow

- page_id: `228986092`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/228986092/Service+Control+Flow
- version_number: 2
- version_date: `2025-05-14T10:31:21.494+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UAF 1.3 elements
- labels: []

### NORMALIZED CONTENT

**Description**

An Activity Edge that shows the flow of control between Service Function Actions.

**Architecture Framework**

UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0

**Extensions**

Control Flow

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description</strong></p><p class="OMGNormalParagraph">An Activity Edge that shows the flow of control between Service Function Actions.</p><p class="OMGNormalParagraph"><strong>Architecture Framework</strong></p><p class="OMGNormalParagraph"><span style="color: rgb(62,63,64);">UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0</span></p><p class="OMGNormalParagraph"><strong>Extensions</strong></p><p class="OMGNormalParagraph">Control Flow</p>
````

<!--NOMAGIC_PAGE id=228986093 space=MED version=2 -->
## PAGE 00418: Service Exchange

- page_id: `228986093`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/228986093/Service+Exchange
- version_number: 2
- version_date: `2025-05-14T10:31:21.853+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UAF 1.3 elements
- labels: []

### NORMALIZED CONTENT

**Description**

Asserts that a flow can exist between Services (i.e. flows of information, people, materiel, or energy).

**Architecture Framework**

UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0

**Extensions**

Information Flow

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description</strong></p><p>Asserts that a flow can exist between Services (i.e. flows of information, people, materiel, or energy).</p><p><strong>Architecture Framework</strong></p><p><span style="color: rgb(62,63,64);">UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0</span></p><p><strong>Extensions</strong></p><p>Information Flow</p>
````

<!--NOMAGIC_PAGE id=228986094 space=MED version=2 -->
## PAGE 00419: Service Exchange Item

- page_id: `228986094`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/228986094/Service+Exchange+Item
- version_number: 2
- version_date: `2025-05-14T10:31:22.173+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UAF 1.3 elements
- labels: []

### NORMALIZED CONTENT

**Description**

An abstract grouping for elements that defines the types of elements that can be exchanged between Services and conveyed by a Service Exchange.

Service Exchange Item is abstract.

**Architecture Framework**

UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0

**Extensions**

Element

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description</strong></p><p class="OMGNormalParagraph">An abstract grouping for elements that defines the types of elements that can be exchanged between Services and conveyed by a Service Exchange.</p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="a76eb7d7-ba60-4ca9-82c3-d6590dcdb6f6"><ac:rich-text-body>Service Exchange Item is abstract.</ac:rich-text-body></ac:structured-macro><p><strong>Architecture Framework</strong></p><p><span style="color: rgb(62,63,64);">UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0</span></p><p><strong>Extensions</strong></p><p>Element</p>
````

<!--NOMAGIC_PAGE id=228986095 space=MED version=2 -->
## PAGE 00420: Service Exchange Kind

- page_id: `228986095`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/228986095/Service+Exchange+Kind
- version_number: 2
- version_date: `2025-05-14T10:31:22.421+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UAF 1.3 elements
- labels: []

### NORMALIZED CONTENT

**Description**

Enumeration of the possible kinds of Service Exchange.

The following are enumeration literals for Service Exchange Kind:

- Configuration Exchange - Indicates that the Operational Exchange associated with the Operational Exchange Kind is a logical flow where Capability Configurations flow from one Operational Performer to another.
- Energy Exchange - Indicates that the Operational Exchange associated with the Operational Exchange Kind is a logical flow where energy is flowed from one Operational Performer to another.
- Information Exchange - Indicates that the Operational Exchange associated with the Operational Exchange Kind is a logical flow where information is flowed from one Operational Performer to another.
- Materiel Exchange - Indicates that the Operational Exchange associated with the Operational Exchange Kind is a logical flow of materiel (artifacts) between Functions.
- Organizational Exchange - Indicates that the Operational Exchange associated with the Operational Exchange Kind is a logical flow where human resources (Post Types, Role Types) flow between Operational Performers.

**Architecture Framework**

UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0

**Extensions**

Enumeration

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description</strong></p><p class="OMGNormalParagraph">Enumeration of the possible kinds of Service Exchange.</p><p class="OMGNormalParagraph">The following are enumeration literals for Service Exchange Kind:</p><ul><li>Configuration Exchange - Indicates that the Operational Exchange associated with the Operational Exchange Kind is a logical flow where Capability Configurations flow from one Operational Performer to another.</li><li>Energy Exchange - Indicates that the Operational Exchange associated with the Operational Exchange Kind is a logical flow where energy is flowed from one Operational Performer to another.</li><li>Information Exchange - Indicates that the Operational Exchange associated with the Operational Exchange Kind is a logical flow where information is flowed from one Operational Performer to another.</li><li>Materiel Exchange - Indicates that the Operational Exchange associated with the Operational Exchange Kind is a logical flow of materiel (artifacts) between Functions.</li><li>Organizational Exchange - Indicates that the Operational Exchange associated with the Operational Exchange Kind is a logical flow where human resources (Post Types, Role Types) flow between Operational Performers.</li></ul><p><strong>Architecture Framework</strong></p><p><span style="color: rgb(62,63,64);">UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0</span></p><p><strong>Extensions</strong></p><p>Enumeration</p>
````

<!--NOMAGIC_PAGE id=228986096 space=MED version=2 -->
## PAGE 00421: Service Function

- page_id: `228986096`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/228986096/Service+Function
- version_number: 2
- version_date: `2025-05-14T10:31:22.673+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UAF 1.3 elements
- labels: []

### NORMALIZED CONTENT

**Description**

An Activity that describes the abstract behavior of Service Specifications, regardless of the actual implementation.

**Architecture** **Framework**

UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0

**Extension**

UML Activity

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="OMGNormalParagraph"><strong>Description</strong></p><p class="OMGNormalParagraph">An Activity that describes the abstract behavior of Service Specifications, regardless of the actual implementation. </p><p class="OMGNormalParagraph"><span class="fontstyle0"><strong>Architecture</strong> <strong>Framework</strong></span></p><p class="OMGNormalParagraph"><span style="color: rgb(62,63,64);">UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0</span></p><p class="OMGNormalParagraph"><strong>Extension</strong></p><p class="OMGNormalParagraph">UML Activity</p><p><br /></p>
````

<!--NOMAGIC_PAGE id=228986097 space=MED version=2 -->
## PAGE 00422: Service Function Action

- page_id: `228986097`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/228986097/Service+Function+Action
- version_number: 2
- version_date: `2025-05-14T10:31:22.997+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UAF 1.3 elements
- labels: []

### NORMALIZED CONTENT

**Description**

A call of a Service Function in the context of another Service Function.

**Architecture** **Framework**

UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0

**Extension**

UML Call Behavior Action

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="OMGNormalParagraph"><strong>Description</strong></p><p class="OMGNormalParagraph">A call of a Service Function in the context of another Service Function.</p><p class="OMGNormalParagraph"><strong>Architecture</strong> <strong>Framework</strong></p><p class="OMGNormalParagraph"><span style="color: rgb(62,63,64);">UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0</span></p><p class="OMGNormalParagraph"><strong>Extension</strong></p><p class="OMGNormalParagraph">UML Call Behavior Action</p><p><br /></p>
````

<!--NOMAGIC_PAGE id=228986098 space=MED version=2 -->
## PAGE 00423: Service Interface

- page_id: `228986098`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/228986098/Service+Interface
- version_number: 2
- version_date: `2025-05-14T10:31:23.275+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UAF 1.3 elements
- labels: []

### NORMALIZED CONTENT

**Description**

A contract that defines the Service Methods and Service Message Handlers that the Service realizes.

**Architecture** **Framework**

UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0

**Extension**

UML Class

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="OMGNormalParagraph"><strong>Description</strong></p><p class="OMGNormalParagraph">A contract that defines the Service Methods and Service Message Handlers that the Service realizes.</p><p class="OMGNormalParagraph"><strong>Architecture</strong> <strong>Framework</strong></p><p class="OMGNormalParagraph"><span style="color: rgb(62,63,64);">UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0</span></p><p class="OMGNormalParagraph"><strong>Extension</strong></p><p class="OMGNormalParagraph">UML Class</p><p><br /></p>
````

<!--NOMAGIC_PAGE id=228986099 space=MED version=2 -->
## PAGE 00424: Service Message

- page_id: `228986099`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/228986099/Service+Message
- version_number: 2
- version_date: `2025-05-14T10:31:23.657+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UAF 1.3 elements
- labels: []

### NORMALIZED CONTENT

**Description**

Message for use in a Service Event-Trace.

**Architecture Framework**

UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0

**Extension**

UML Message

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description</strong></p><p class="OMGNormalParagraph">Message for use in a Service Event-Trace. </p><p class="OMGNormalParagraph"><strong>Architecture Framework</strong></p><p class="OMGNormalParagraph"><span style="color: rgb(62,63,64);">UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0</span></p><p class="OMGNormalParagraph"><strong>Extension</strong></p><p class="OMGNormalParagraph">UML Message</p><p><br /></p>
````

<!--NOMAGIC_PAGE id=228986100 space=MED version=2 -->
## PAGE 00425: Service Method

- page_id: `228986100`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/228986100/Service+Method
- version_number: 2
- version_date: `2025-05-14T10:31:24.094+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UAF 1.3 elements
- labels: []

### NORMALIZED CONTENT

**Description**

A behavioral feature of a Service Specification whose behavior is specified in a Service Function.

**Architecture** **Framework**

UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0

**Extension**

UML Operation

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="OMGNormalParagraph"><strong>Description</strong></p><p class="OMGNormalParagraph">A behavioral feature of a Service Specification whose behavior is specified in a Service Function. </p><p class="OMGNormalParagraph"><strong>Architecture</strong> <strong>Framework</strong></p><p class="OMGNormalParagraph"><span style="color: rgb(62,63,64);">UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0</span></p><p class="OMGNormalParagraph"><strong>Extension</strong></p><p class="OMGNormalParagraph">UML Operation</p><p><br /></p>
````

<!--NOMAGIC_PAGE id=228986101 space=MED version=2 -->
## PAGE 00426: Service Object Flow

- page_id: `228986101`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/228986101/Service+Object+Flow
- version_number: 2
- version_date: `2025-05-14T10:31:24.481+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UAF 1.3 elements
- labels: []

### NORMALIZED CONTENT

**Description**

An Activity Edge that shows the flow of Resources (objects/information) between Service Function Actions.

**Architecture Framework**

UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0

**Extensions**

Object Flow

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description</strong></p><p class="OMGNormalParagraph">An Activity Edge that shows the flow of Resources (objects/information) between Service Function Actions.</p><p><strong>Architecture Framework</strong></p><p><span style="color: rgb(62,63,64);">UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0</span></p><p><strong>Extensions</strong></p><p>Object Flow</p>
````

<!--NOMAGIC_PAGE id=228986102 space=MED version=2 -->
## PAGE 00427: Service Parameter

- page_id: `228986102`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/228986102/Service+Parameter
- version_number: 2
- version_date: `2025-05-14T10:31:24.794+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UAF 1.3 elements
- labels: []

### NORMALIZED CONTENT

**Description**

An element that represents inputs and outputs of a Service Function, represents inputs and outputs of a Service Specification.

**Architecture Framework**

UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0

**Extension**

UML Parameter

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="OMGNormalParagraph"><strong>Description</strong></p><p>An element that represents inputs and outputs of a Service Function, represents inputs and outputs of a Service Specification.</p><p><strong>Architecture Framework</strong></p><p><span style="color: rgb(62,63,64);">UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0</span></p><p><strong>Extension</strong></p><p>UML Parameter</p><p><br /></p>
````

<!--NOMAGIC_PAGE id=228986103 space=MED version=2 -->
## PAGE 00428: Service Policy

- page_id: `228986103`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/228986103/Service+Policy
- version_number: 2
- version_date: `2025-05-14T10:31:25.044+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UAF 1.3 elements
- labels: []

### NORMALIZED CONTENT

**Description**

A constraint governing the use of one or more Service Specifications.

**Architecture** **Framework**

UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0

**Extension**

UML Constraint

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="OMGNormalParagraph"><strong>Description</strong></p><p>A constraint governing the use of one or more Service Specifications.</p><p><strong>Architecture</strong> <strong>Framework</strong></p><p><span style="color: rgb(62,63,64);">UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0</span></p><p><strong>Extension</strong></p><p>UML Constraint</p><p><br /></p>
````

<!--NOMAGIC_PAGE id=228986104 space=MED version=2 -->
## PAGE 00429: Service Port

- page_id: `228986104`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/228986104/Service+Port
- version_number: 2
- version_date: `2025-05-14T10:31:25.426+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UAF 1.3 elements
- labels: []

### NORMALIZED CONTENT

**Description**

An interaction point for a Service Specification through which it can interact with the outside environment and which is defined by a Service Interface.

**Architecture Framework**

UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0

**Extension**

UML Port

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="OMGNormalParagraph"><strong>Description</strong></p><p class="OMGNormalParagraph">An interaction point for a Service Specification through which it can interact with the outside environment and which is defined by a Service Interface.</p><p class="OMGNormalParagraph"><strong>Architecture Framework</strong></p><p class="OMGNormalParagraph"><span style="color: rgb(62,63,64);">UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0</span></p><p class="OMGNormalParagraph"><strong>Extension</strong></p><p class="OMGNormalParagraph">UML Port</p><p><br /></p>
````

<!--NOMAGIC_PAGE id=228986105 space=MED version=2 -->
## PAGE 00430: Service Role

- page_id: `228986105`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/228986105/Service+Role
- version_number: 2
- version_date: `2025-05-14T10:31:25.703+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UAF 1.3 elements
- labels: []

### NORMALIZED CONTENT

**Description**

Usage of a Service in the context of another Service. Creates a whole-part relationship.

**Architecture** **Framework**

UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0

**Extension**

Property

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="OMGNormalParagraph"><strong>Description</strong></p><p class="OMGNormalParagraph">Usage of a Service in the context of another Service. Creates a whole-part relationship.</p><p class="OMGNormalParagraph"><strong>Architecture</strong> <strong>Framework</strong></p><p class="OMGNormalParagraph"><span style="color: rgb(62,63,64);">UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0</span></p><p class="OMGNormalParagraph"><strong>Extension</strong></p><p class="OMGNormalParagraph">Property</p><p><br /></p>
````

<!--NOMAGIC_PAGE id=228986106 space=MED version=2 -->
## PAGE 00431: Service Signal

- page_id: `228986106`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/228986106/Service+Signal
- version_number: 2
- version_date: `2025-05-14T10:31:25.979+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UAF 1.3 elements
- labels: []

### NORMALIZED CONTENT

**Description**

A specification of a kind of communication between Services in which a reaction is asynchronously triggered in the receiver without a reply.

**Architecture Framework**

UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0

**Extensions**

Signal

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description</strong></p><p class="OMGNormalParagraph">A specification of a kind of communication between Services in which a reaction is asynchronously triggered in the receiver without a reply.</p><p><strong>Architecture Framework</strong></p><p><span style="color: rgb(62,63,64);">UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0</span></p><p><strong>Extensions</strong></p><p>Signal</p>
````

<!--NOMAGIC_PAGE id=228986107 space=MED version=2 -->
## PAGE 00432: Service Signal Property

- page_id: `228986107`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/228986107/Service+Signal+Property
- version_number: 2
- version_date: `2025-05-14T10:31:26.230+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UAF 1.3 elements
- labels: []

### NORMALIZED CONTENT

**Description**

A property of a Service Signal typed by Service Exchange Item. It enables Service Exchange Item e.g. Operational Information to be passed as arguments of the Service Signal.

**Architecture Framework**

UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0

**Extension**

Property

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description</strong></p><p class="OMGNormalParagraph">A property of a Service Signal typed by Service Exchange Item. It enables Service Exchange Item e.g. Operational Information to be passed as arguments of the Service Signal.</p><p><strong>Architecture Framework</strong></p><p><span style="color: rgb(62,63,64);">UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0</span></p><p><strong>Extension</strong></p><p>Property</p>
````

<!--NOMAGIC_PAGE id=228986108 space=MED version=2 -->
## PAGE 00433: Service State Description

- page_id: `228986108`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/228986108/Service+State+Description
- version_number: 2
- version_date: `2025-05-14T10:31:26.566+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UAF 1.3 elements
- labels: []

### NORMALIZED CONTENT

**Description**

A state machine describing the behavior of a Service, depicting how the Service responds to various events and the actions.

**Architecture Framework**

UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0

**Extension**

UML State Machine

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="OMGNormalParagraph"><strong>Description</strong></p><p class="OMGNormalParagraph">A state machine describing the behavior of a Service, depicting how the Service responds to various events and the actions. </p><p class="OMGNormalParagraph"><strong>Architecture Framework</strong></p><p class="OMGNormalParagraph"><span style="color: rgb(62,63,64);">UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0</span></p><p class="OMGNormalParagraph"><strong>Extension</strong></p><p class="OMGNormalParagraph">UML State Machine</p>
````

<!--NOMAGIC_PAGE id=243967967 space=MED version=1 -->
## PAGE 00434: Shallow History

- page_id: `243967967`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/243967967/Shallow+History
- version_number: 1
- version_date: `2025-07-31T10:50:46.633+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UML elements > State Machine > Pseudo States
- labels: []

### NORMALIZED CONTENT

The Shallow History represents the most recent active substate of its containing state (but not the substates of that substate). A composite state can have at most one shallow history vertex. A transition coming to the shallow history vertex is equivalent to a transition coming to the most recent active substate of a state.

#### PANEL: Related Pages

Related Pages

- [CONFLUENCE_PAGE title='UML elements' space='']
- [CONFLUENCE_PAGE title='Specification window' space='MT']

#### PANEL: Related pages

Related pages

[CONFLUENCE_PAGE title='Pseudo States' space='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p>The Shallow History represents the most recent active substate of its containing state (but not the substates of that substate). A composite state can have at most one shallow history vertex. A transition coming to the shallow history vertex is equivalent to a transition coming to the most recent active substate of a state.</p></ac:layout-cell><ac:layout-cell><p> </p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="36e20852-22dd-420b-8d4b-52b136b22981"><ac:parameter ac:name="title">Related Pages</ac:parameter><ac:rich-text-body><ul><li><ac:link><ri:page ri:content-title="UML elements" /><ac:plain-text-link-body><![CDATA[Model Elements]]></ac:plain-text-link-body></ac:link></li><li><ac:link><ri:page ri:space-key="MT" ri:content-title="Specification window" /><ac:plain-text-link-body><![CDATA[Specification Window]]></ac:plain-text-link-body></ac:link></li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="f01b84d9-d9d1-4049-8315-15a6a05d850d"><ac:parameter ac:name="title">Related pages</ac:parameter><ac:rich-text-body><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="7e19d119-2f65-4f2a-b944-60c34f7c4ba8"><ac:parameter ac:name="page"><ac:link><ri:page ri:content-title="Pseudo States" /></ac:link></ac:parameter></ac:structured-macro></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=243967657 space=MED version=1 -->
## PAGE 00435: Signal Event

- page_id: `243967657`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/243967657/Signal+Event
- version_number: 1
- version_date: `2025-07-31T10:50:37.994+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UML elements > Event
- labels: []

### NORMALIZED CONTENT

A signal may be sent as the action of a state in a state machine or as a message in an interaction.

A signal is a named object sent asynchronously by one object and received by another.

In the Signal [CONFLUENCE_PAGE title='Specification window' space='MT'], you can modify the current element and add various specifications to it.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><span style="color: rgb(0,0,0);"><span style="color: rgb(68,68,68);"><span style="color: rgb(68,68,68);">A signal may be sent as the action of a state in a state machine or as a message in an interaction.</span><br /></span></span></p><p><span style="color: rgb(0,0,0);"><span style="color: rgb(68,68,68);">A signal is a named object sent asynchronously by one object and received by another.</span></span></p><p><span style="color: rgb(0,0,0);">In the Signal <ac:link><ri:page ri:space-key="MT" ri:content-title="Specification window" /></ac:link></span><span style="color: rgb(0,0,0);">, you can modify the current element and add various specifications to it. </span></p>
````

<!--NOMAGIC_PAGE id=243967919 space=MED version=1 -->
## PAGE 00436: Slot

- page_id: `243967919`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/243967919/Slot
- version_number: 1
- version_date: `2025-07-31T10:50:45.415+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UML elements
- labels: []

### NORMALIZED CONTENT

A Slot specifies that an entity modeled by an [CONFLUENCE_PAGE title='Instance Specification' space=''] specification has a value or values for a specific structural feature.Values of each [CONFLUENCE_PAGE title='Attribute' space=''] have specific type and are allocated in the slots of the instance or associated with that instance.

You can modify the current element and add various specifications to it in the element dialog box: click onthe property group Tags, select the tag with the assigned value and clickEditValue to open theSlot[CONFLUENCE_PAGE title='Specification window' space='MT'].

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><span style="color: rgb(0,0,0);">A Slot specifies that an entity modeled by an <ac:link><ri:page ri:content-title="Instance Specification" /></ac:link> specification has a value or values for a specific structural feature. </span>Values of each <ac:link><ri:page ri:content-title="Attribute" /></ac:link> have specific type and are allocated in the slots of the instance or associated with that instance. </p><p><span style="color: rgb(0,0,0);">You can modify the current element and add various specifications to it <span style="color: rgb(0,0,0);">in the element dialog box:</span> c</span><span style="color: rgb(0,0,0);">lick on </span><span style="color: rgb(0,0,0);">the property group <span>Tags</span>, select the tag with the assigned value and click </span><span class="hcp1" style="color: rgb(0,0,0);">Edit</span><span style="color: rgb(0,0,0);"> </span><span class="hcp1" style="color: rgb(0,0,0);">Value <span>to open the </span><span class="hcp1">Slot</span><span> <ac:link><ri:page ri:space-key="MT" ri:content-title="Specification window" /></ac:link></span></span><span style="color: rgb(0,0,0);">.  </span></p>
````

<!--NOMAGIC_PAGE id=243967921 space=MED version=2 -->
## PAGE 00437: Smart Package

- page_id: `243967921`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/243967921/Smart+Package
- version_number: 2
- version_date: `2025-09-13T12:44:12.985+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UML elements
- labels: []

### NORMALIZED CONTENT

1342419680

1342419683

1342419682

This feature is available in Standard, Professional, Architect, and Enterprise editions.

Smart package is a special collection of model elements.

There are two ways an element can be included in the smart package:

- *Manually -*the user selects to include the particular element. You can create a smart package named *My Bookmarks*and add frequently used elements to it.

- *Automatically -*the element meets the set of criteria defined by the user. You can create a smart package named *Requirements v5*with the criteria “all elements of type *Requirement*under the package *Business requirements*, having tag *version=5*”.

The membership in the smart package is not the UML ownership; one element can belong to several smart packages.

Smart packages aggregate relevant elements, so that you can:

- Easily browse, navigate, list, and discover these elements in the Containment tree.
- Narrow the scope in both the Find dialog and the element Selection dialog.
- Define dynamic row and column scopes in dependency matrices.

##### Concepts

To better understand this material, please read through the following concepts.

##### Static contents

A collection of manually included elements.

##### Dynamic contents

A collection of elements automatically calculated according to the set of criteria specified by the user.

1342419679

**Related pages**

- [CONFLUENCE_PAGE title='UML elements' space='']
- [CONFLUENCE_PAGE title='Stereotype' space='']
- [CONFLUENCE_PAGE title='Package' space='']
- [CONFLUENCE_PAGE title='Working with Profiles' space='MT']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="7b3290ec-229c-4ed2-ad56-c93a363fff17"><ac:parameter ac:name="id">1342419680</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="d3dad257-c7a9-4267-901b-5efcddcc4610"><ac:parameter ac:name="id">1342419683</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="40c1b770-5752-4e66-b44b-b8a1801a8a7b"><ac:parameter ac:name="id">1342419682</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="dd111539-459a-46d9-8b6c-b00ad9f274a7"><ac:rich-text-body><p>This feature is available in Standard, Professional, Architect, and Enterprise editions.</p></ac:rich-text-body></ac:structured-macro><p>Smart package is a special collection of model elements.</p><p>There are two ways an element can be included in the smart package:</p><ul><li><p> <em>Manually - </em>the user selects to include the particular element.</p><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="4684ce33-c49c-483c-99b2-a93d3a113a41"><ac:rich-text-body><p>You can create a smart package named <em>My Bookmarks </em>and add frequently used elements to it.</p></ac:rich-text-body></ac:structured-macro></li></ul><ul><li><p><em>Automatically - </em>the element meets the set of criteria defined by the user.</p><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="cf0ee22e-e48d-43c1-817e-7447a6424412"><ac:rich-text-body><p>You can create a smart package named <em>Requirements v5 </em>with the criteria “all elements of type <em>Requirement </em>under the package <em>Business requirements</em>, having tag <em>version=5</em>”.</p></ac:rich-text-body></ac:structured-macro></li></ul><p>The membership in the smart package is not the UML ownership; one element can belong to several smart packages.</p><p>Smart packages aggregate relevant elements, so that you can:</p><ul><li>Easily browse, navigate, list, and discover these elements in the Containment tree.</li><li>Narrow the scope in both the <strong>Find </strong>dialog and the element Selection dialog.</li><li>Define dynamic row and column scopes in dependency matrices.</li></ul><h3>Concepts</h3><p>To better understand this material, please read through the following concepts.</p><h3>Static contents</h3><p>A collection of manually included elements.</p><h3>Dynamic contents</h3><p>A collection of elements automatically calculated according to the set of criteria specified by the user.</p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="e59eac7c-23df-47d4-85ac-b782416d0b78"><ac:parameter ac:name="id">1342419679</ac:parameter><ac:rich-text-body><p><strong>Related pages</strong></p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="76d9c65e-a6bf-482b-903b-63419514e323" /></p><ul><li><ac:link><ri:page ri:content-title="UML elements" /><ac:plain-text-link-body><![CDATA[Model Elements]]></ac:plain-text-link-body></ac:link></li><li><ac:link><ri:page ri:content-title="Stereotype" /></ac:link></li><li><ac:link><ri:page ri:content-title="Package" /></ac:link></li><li><ac:link><ri:page ri:space-key="MT" ri:content-title="Working with Profiles" /></ac:link></li></ul><p><br /></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=243967935 space=MED version=2 -->
## PAGE 00438: Smart package properties

- page_id: `243967935`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/243967935/Smart+package+properties
- version_number: 2
- version_date: `2025-09-13T12:44:13.328+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UML elements > Smart Package
- labels: []

### NORMALIZED CONTENT

Every smart package has several properties that allow you to specify the contents of the smart package. These properties are described in the following table.

| Property | Description |
| --- | --- |
| Query | Stores a set of criteria for automatic inclusion of elements into the contents of the smart package.For more information, see . |
| Additional Elements | Stores the list of the elements manually included into the contents of the smart package.For more information, see . |
| Excluded Elements | Stores the list of the elements excluded from the contents of the smart package.For more information, see |

#### PANEL: Related Pages

Related Pages

- [CONFLUENCE_PAGE title='UML elements' space='']
- [CONFLUENCE_PAGE title='Stereotype' space='']
- [CONFLUENCE_PAGE title='Package' space='']
- [CONFLUENCE_PAGE title='Working with Profiles' space='MT']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p>Every smart package has several properties that allow you to specify the contents of the smart package. These properties are described in the following table.</p><table class="wrapped"><colgroup><col /><col /></colgroup><tbody><tr><th>Property</th><th>Description</th></tr><tr><td><strong>Query</strong></td><td><p>Stores a set of criteria for automatic inclusion of elements into the contents of the smart package.</p><p>For more information, see <ac:link ac:anchor="Includingelementsintoasmartpackage"><ri:page ri:content-title="Managing contents of smart package" /><ac:plain-text-link-body><![CDATA[Including elements into a smart package automatically]]></ac:plain-text-link-body></ac:link>.</p></td></tr><tr><td><p><strong>Additional Elements</strong></p></td><td><p>Stores the list of the elements manually included into the contents of the smart package.</p><p>For more information, see <ac:link ac:anchor="Includingelementsintoasmartpackage"><ri:page ri:content-title="Managing contents of smart package" /><ac:plain-text-link-body><![CDATA[Including elements into a smart package manually]]></ac:plain-text-link-body></ac:link>.</p></td></tr><tr><td><p><strong>Excluded Elements</strong></p></td><td><p>Stores the list of the elements excluded from the contents of the smart package.</p><p>For more information, see <ac:link ac:anchor="Removingelementsfromasmartpackage"><ri:page ri:content-title="Managing contents of smart package" /><ac:plain-text-link-body><![CDATA[Removing elements from a smart package.]]></ac:plain-text-link-body></ac:link></p></td></tr></tbody></table><p class="auto-cursor-target"><br /></p></ac:layout-cell><ac:layout-cell><p> </p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="a1cb6614-da6a-4a7b-adf1-3ec18e11a18c"><ac:parameter ac:name="title">Related Pages</ac:parameter><ac:rich-text-body><ul><li><ac:link><ri:page ri:content-title="UML elements" /><ac:plain-text-link-body><![CDATA[Model Elements]]></ac:plain-text-link-body></ac:link></li><li><ac:link><ri:page ri:content-title="Stereotype" /></ac:link></li><li><ac:link><ri:page ri:content-title="Package" /></ac:link></li><li><ac:link><ri:page ri:space-key="MT" ri:content-title="Working with Profiles" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=243967956 space=MED version=2 -->
## PAGE 00439: Smart package-related performance issues

- page_id: `243967956`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/243967956/Smart+package-related+performance+issues
- version_number: 2
- version_date: `2025-09-13T12:44:13.600+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UML elements > Smart Package
- labels: []

### NORMALIZED CONTENT

#### CONTENT-LAYER: Tip

1342803013

#### CONTENT-COLUMN: Tip

1342803015

#### CONTENT-BLOCK: Tip

1342803014

When working with large projects, smart packages can sometimes cause performance issues. They can influence the time of a search, commit, and derived properties-related operations. However, there is a way to identify which smart packages or properties cause the problem by getting notifications about their evaluation time.

To get notifications about the evaluation time of smart package content and derived properties

1. Go to <modeling tool installation directory>/bin and open the properties file of your modeling tool.
2. Enter the *md.expression.evaluation.duration.notification.threshold* Java argument and define the threshold time in seconds for getting notifications, e.g.: -Dmd.expression.evaluation.duration.notification.threshold=30 NoteThe default value of the *md.expression.evaluation.duration.notification.threshold* argument is 60 seconds. If you add the argument to the properties file of your modeling tool but do not define its value, the default value is used.
3. Save and close the file
4. Restart your modeling tool if it's open.

Your modeling tool is now configured to show notifications about the evaluation time of smart package content and derived properties. The notifications are shown in the **Notification Window** area at the bottom of a modeling tool window.

###### [IMAGE alt='' src=''] 
Smart package content and property evaluation notifications - the time threshold applied is 1 second.

To disable notifications

- Click Do not show this message again when a new notification appears on the right side of a modeling tool window.

###### [IMAGE alt='' src=''] 
Disabling notifications from a modeling tool.

This action disables notifications about the evaluation time of both smart package content and derived properties.

#### TIP: Tip

Tip

You can increase the performance of your modeling tool by following these recommendations:

- Avoid using smart packages with Find queries, especially if they are used to find common elements (e.g., Class, Package, Block, etc.).
- Avoid using smart packages with Find queries that have a wide scope.
- Avoid nesting smart packages, i.e., using one smart package as part of another smart package's content.

#### TIP: Tip

Tip

You can prevent a number of performance issues stemming from the use of smart packages by using tables and matrices with the [CONFLUENCE_PAGE title='Specifying scope' space='MT'] instead.

[CONFLUENCE_PAGE title='Smart Package' space='']true

1342803012

**Related pages**

- [CONFLUENCE_PAGE title='UML elements' space='']
- [CONFLUENCE_PAGE title='Stereotype' space='']
- [CONFLUENCE_PAGE title='Package' space='']
- [CONFLUENCE_PAGE title='Working with Profiles' space='MT']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="f195314d-148d-4e33-a980-2d202b58f25c"><ac:parameter ac:name="id">1342803013</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="e5be2337-fe63-4fb7-ada2-c7cc2e5f50eb"><ac:parameter ac:name="id">1342803015</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="df9d3c74-8fcd-4f0c-97fd-62a1f0618f32"><ac:parameter ac:name="id">1342803014</ac:parameter><ac:rich-text-body><p>When working with large projects, smart packages can sometimes cause performance issues. They can influence the time of a search, commit, and derived properties-related operations. However, there is a way to identify which smart packages or properties cause the problem by getting notifications about their evaluation time.</p><p><br /></p><p>To get notifications about the evaluation time of smart package content and derived properties</p><hr /><ol><li>Go to <em>&lt;modeling tool installation directory&gt;/bin</em> and open the properties file of your modeling tool.</li><li><p>Enter the <em>md.expression.evaluation.duration.notification.threshold</em> Java argument and define the threshold time in seconds for getting notifications, e.g.:</p><pre>-Dmd.expression.evaluation.duration.notification.threshold=30<br /> </pre><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="789fe15b-e658-4625-bf75-a9bd84510cf8"><ac:parameter ac:name="title">Note</ac:parameter><ac:rich-text-body><p>The default value of the <em>md.expression.evaluation.duration.notification.threshold</em> argument is 60 seconds. If you add the argument to the properties file of your modeling tool but do not define its value, the default value is used.</p></ac:rich-text-body></ac:structured-macro></li><li>Save and close the file</li><li>Restart your modeling tool if it's open.<br /> </li></ol><p>Your modeling tool is now configured to show notifications about the evaluation time of smart package content and derived properties. The notifications are shown in the <strong>Notification Window</strong> area at the bottom of a modeling tool window.</p><h6 style="margin-left: 30.0px;text-align: center;"><ac:image ac:align="center"><ri:attachment ri:filename="evaluation_time_notifications.png" /></ac:image><br /><span style="color: rgb(128,128,128);">Smart package content and property evaluation notifications - the time threshold applied is 1 second.</span></h6><p>To disable notifications</p><hr /><ul><li>Click <strong>Do not show this message again</strong> when a new notification appears on the right side of a modeling tool window.</li></ul><h6 style="margin-left: 30.0px;"><ac:image><ri:attachment ri:filename="disabling_notifications.png" /></ac:image><br /><span style="color: rgb(128,128,128);">Disabling notifications from a modeling tool.</span></h6><p><br />This action disables notifications about the evaluation time of both smart package content and derived properties.</p><p><br /></p><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="70d699d4-08a7-4a03-aa16-212aad48ca30"><ac:parameter ac:name="title">Tip</ac:parameter><ac:rich-text-body><p>You can increase the performance of your modeling tool by following these recommendations:</p><ul><li>Avoid using smart packages with Find queries, especially if they are used to find common elements (e.g., Class, Package, Block, etc.).</li><li>Avoid using smart packages with Find queries that have a wide scope.</li><li>Avoid nesting smart packages, i.e., using one smart package as part of another smart package's content.</li></ul></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="b45fec35-f992-4abb-be4f-0f1bb4ff0e58"><ac:parameter ac:name="title">Tip</ac:parameter><ac:rich-text-body><p class="auto-cursor-target">You can prevent a number of performance issues stemming from the use of smart packages by using tables and matrices with the <ac:link ac:anchor="specifying row and column query"><ri:page ri:space-key="MT" ri:content-title="Specifying scope" /><ac:plain-text-link-body><![CDATA[specified expression]]></ac:plain-text-link-body></ac:link> instead.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><p><ac:structured-macro ac:name="excerpt-include" ac:schema-version="1" ac:macro-id="3a113683-b932-43f9-9536-f53bf44a61c3"><ac:parameter ac:name=""><ac:link><ri:page ri:content-title="Smart Package" /></ac:link></ac:parameter><ac:parameter ac:name="nopanel">true</ac:parameter></ac:structured-macro></p><p><br /></p><p class="auto-cursor-target"><br /></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="b0f11a5f-b52b-400a-bd7b-49f986eebd89"><ac:parameter ac:name="id">1342803012</ac:parameter><ac:rich-text-body><p><strong>Related pages</strong></p><ul><li><ac:link><ri:page ri:content-title="UML elements" /><ac:plain-text-link-body><![CDATA[Model Elements]]></ac:plain-text-link-body></ac:link></li><li><ac:link><ri:page ri:content-title="Stereotype" /></ac:link></li><li><ac:link><ri:page ri:content-title="Package" /></ac:link></li><li><ac:link><ri:page ri:space-key="MT" ri:content-title="Working with Profiles" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=228986109 space=MED version=2 -->
## PAGE 00440: Software

- page_id: `228986109`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/228986109/Software
- version_number: 2
- version_date: `2025-05-14T10:31:26.962+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UAF 1.3 elements
- labels: []

### NORMALIZED CONTENT

**Description**

A sub-type of ResourceArtifact that specifies an executable computer program.

**Architecture Framework**

UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0

**Extensions**

UML Class

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="OMGBoldBulletKeepNextParagraph"><strong>Description</strong></p><p>A sub-type of ResourceArtifact that specifies an executable computer program.</p><p><span class="fontstyle0"><strong>Architecture Framework</strong></span></p><p><span style="color: rgb(62,63,64);">UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0</span></p><p><span class="fontstyle0"><strong>Extensions</strong></span></p><p><span class="fontstyle2">UML Class</span></p><p><br /></p>
````

<!--NOMAGIC_PAGE id=243967656 space=MED version=1 -->
## PAGE 00441: Specifying a time for a time event

- page_id: `243967656`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/243967656/Specifying+a+time+for+a+time+event
- version_number: 1
- version_date: `2025-07-31T10:50:37.919+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UML elements > Event
- labels: []

### NORMALIZED CONTENT

A time event specifies an instance in time by an expression. The expression might be absolute or it might be relative to some other point in time. Relative time events must always be used in the context of a trigger and the starting point is the time at which the trigger becomes active.

A relative time trigger is specified with the keyword “after” followed by an expression that evaluates to a time value, such as “after (5 seconds).” An absolute time trigger is specified with the keyword “at” followed by an expression that evaluates to a time value, such as “Jan. 1, 2012, Noon.”

You can change the time expression by changing the **Is Relative** property value.

To specify a time for a time event

1. Open the selected [CONFLUENCE_PAGE title='Transition' space=''] [CONFLUENCE_PAGE title='Specification window' space='MT'] or [CONFLUENCE_PAGE title='Accept Event Action' space=''] Specification window having the TimeEvent type assigned.
2. In the **Trigger** category, do one of the following: If you do not see the **Event Type** property, click the button **+** near the **Trigger** category to expand its content.

- 
  - To specify the event occurrence at the absolute time, set **Is Relative** property value to *false*.The time event is specified as absolute, and the command syntax changes from *after()* to *at ()*.
  - To specify the event occurrence at the relative time, set **Is Relative** property value to *true*.The time event is specified as relative, and the command syntax changes from *at ()* to *after ()*.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p>A time event specifies an instance in time by an expression. The expression might be absolute or it might be relative to some other point in time. Relative time events must always be used in the context of a trigger and the starting point is the time at which the trigger becomes active.</p><p>A relative time trigger is specified with the keyword “after” followed by an expression that evaluates to a time value, such as “after (5 seconds).” An absolute time trigger is specified with the keyword “at” followed by an expression that evaluates to a time value, such as “Jan. 1, 2012, Noon.”</p><p>You can change the time expression by changing the <strong>Is Relative</strong> property value.</p><p><br /></p><p>To specify a time for a time event</p><hr /><ol><li>Open the selected <ac:link><ri:page ri:content-title="Transition" /></ac:link><ac:link><ri:page ri:space-key="MT" ri:content-title="Specification window" /></ac:link> or <ac:link><ri:page ri:content-title="Accept Event Action" /><ac:plain-text-link-body><![CDATA[Accept Event Action ]]></ac:plain-text-link-body></ac:link>Specification window having the <strong>TimeEvent</strong> type assigned.</li><li><p>In the <strong>Trigger</strong> category, do one of the following:</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="b1dca04a-933f-4fa0-9df0-4c92c0d1668c"><ac:rich-text-body><p>If you do not see the <strong>Event Type</strong> property, click the button <strong>+</strong> near the <strong>Trigger</strong> category to expand its content.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></li></ol><ul><li style="list-style-type: none;background-image: none;"><ul><li><p>To specify the event occurrence at the absolute time, set <strong>Is Relative</strong> property value to <em>false</em>.The time event is specified as absolute, and the command syntax changes from <em>after()</em> to <em>at ()</em>.</p></li><li><p>To specify the event occurrence at the relative time, set <strong>Is Relative</strong> property value to <em>true</em>.The time event is specified as relative, and the command syntax changes from <em>at ()</em> to <em>after ()</em>.</p></li></ul></li></ul></ac:layout-cell><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=243968043 space=MED version=1 -->
## PAGE 00442: Specifying a Use Case subject

- page_id: `243968043`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/243968043/Specifying+a+Use+Case+subject
- version_number: 1
- version_date: `2025-07-31T10:50:48.873+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UML elements > Use Case
- labels: ['use-case-subject', 'specifying-use-case-subject']

### NORMALIZED CONTENT

21126566

21126568

21126567

INLINE

The subject of a Use Case represents a system under consideration to which that Use Case applies. The subject can be any element that may have a behavior, such as a Component or Class (SysML Block).

To specify the Use Case subject

1. Select the Use Case or its shape.
2. Drag it onto a Class, SysML Block, or Component shape. The Use Case becomes nested in that shape, and the appropriate model element is set as the Use Case subject.

[IMAGE alt='' src='']

Having a Use Case with the subject specified jumpstarts the creation of Swimlanes in the Activity diagram owned by that Use Case. In this case, you can select the subject properties you wish to be represented by the Swimlanes on that diagram.

[IMAGE alt='' src='']

21126565

**Related pages**

[CONFLUENCE_PAGE title='Use Case' space='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="0e16fd3e-c053-4c32-8e1f-1635908b8aa5"><ac:parameter ac:name="id">21126566</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="6b021e86-55a4-4209-9b51-9b67ffdf2821"><ac:parameter ac:name="id">21126568</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="099382e8-4e5c-49a5-b192-c617deca13c6"><ac:parameter ac:name="id">21126567</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="excerpt" ac:schema-version="1" ac:macro-id="c00af183-41b8-469e-bc43-f565aef91275"><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><p>The subject of a Use Case represents a system under consideration to which that Use Case applies. The subject can be any element that may have a behavior, such as a Component or Class (SysML Block).</p><p><br /></p><p>To specify the Use Case subject</p><hr /><ol><li>Select the Use Case or its shape.</li><li>Drag it onto a Class, SysML Block, or Component shape. The Use Case becomes nested in that shape, and the appropriate model element is set as the Use Case subject.</li></ol><p><ac:image><ri:attachment ri:filename="use_case_subject_md.png" /></ac:image></p><p>Having a Use Case with the subject specified jumpstarts the creation of Swimlanes in the Activity diagram owned by that Use Case. In this case, you can select the subject properties you wish to be represented by the Swimlanes on that diagram.</p><p><ac:image><ri:attachment ri:filename="represent_properties.png" /></ac:image></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="fd9f32aa-6ba1-414a-96b8-d6d44df3e931"><ac:parameter ac:name="id">21126565</ac:parameter><ac:rich-text-body><p><strong>Related pages</strong></p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="b6182c6d-bffd-4824-ab67-789a0a46c06d"><ac:parameter ac:name="page"><ac:link><ri:page ri:content-title="Use Case" /></ac:link></ac:parameter></ac:structured-macro></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=228986110 space=MED version=2 -->
## PAGE 00443: Stakeholder

- page_id: `228986110`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/228986110/Stakeholder
- version_number: 2
- version_date: `2025-05-14T10:31:27.216+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UAF 1.3 elements
- labels: []

### NORMALIZED CONTENT

**Description**

Individual, team, organization, or classes thereof, having an interest in an Enterprise Phase.

**Architecture** **Framework**

UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0

**Extension**

Element

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="OMGNormalParagraph"><strong>Description</strong></p><p>Individual, team, organization, or classes thereof, having an interest in an Enterprise Phase.</p><p><strong>Architecture</strong> <strong>Framework</strong></p><p><span style="color: rgb(62,63,64);">UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0</span></p><p><strong>Extension</strong></p><p>Element</p><p><br /></p>
````

<!--NOMAGIC_PAGE id=228986111 space=MED version=2 -->
## PAGE 00444: Standard

- page_id: `228986111`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/228986111/Standard
- version_number: 2
- version_date: `2025-05-14T10:31:27.463+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UAF 1.3 elements
- labels: []

### NORMALIZED CONTENT

**Description**

A ratified and peer-reviewed specification that is used to guide or constrain the architecture. A Standard may be applied to any element in the architecture.

**Architecture Framework**

UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0

**Extension**

UML Class

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="OMGNormalParagraph"><strong>Description</strong></p><p class="OMGNormalParagraph">A ratified and peer-reviewed specification that is used to guide or constrain the architecture. A Standard may be applied to any element in the architecture.</p><p class="OMGNormalParagraph"><strong>Architecture Framework</strong></p><p class="OMGNormalParagraph"><span style="color: rgb(62,63,64);">UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0</span></p><p class="OMGNormalParagraph"><strong>Extension</strong></p><p class="OMGNormalParagraph">UML Class</p><p><br /></p>
````

<!--NOMAGIC_PAGE id=228986112 space=MED version=2 -->
## PAGE 00445: Standard Operational Activity

- page_id: `228986112`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/228986112/Standard+Operational+Activity
- version_number: 2
- version_date: `2025-05-14T10:31:27.749+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UAF 1.3 elements
- labels: []

### NORMALIZED CONTENT

**Description**

A sub-type of Operational Activity that is a standard operating procedure.

**Architecture** **Framework**

UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0

**Extension**

UML Activity

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="OMGNormalParagraph"><strong>Description</strong></p><p>A sub-type of Operational Activity that is a standard operating procedure.</p><p><span class="fontstyle0"><strong>Architecture</strong> <strong>Framework</strong></span></p><p><span style="color: rgb(62,63,64);">UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0</span></p><p><strong>Extension</strong></p><p>UML Activity</p><p><br /></p>
````

<!--NOMAGIC_PAGE id=243967972 space=MED version=1 -->
## PAGE 00446: State

- page_id: `243967972`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/243967972/State
- version_number: 1
- version_date: `2025-07-31T10:50:46.923+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UML elements > State Machine
- labels: ['state', 'simple-state', 'composite-state', 'orthogonal-state', 'submachine-state']

### NORMALIZED CONTENT

A State is a condition during the lifetime of an object or an interaction during which the object meets certain conditions, performs an action, or waits for an event. The State is defined by the concepts of duration and stability. An object can not be in an unknown or undefined State. A State may have two compartments to provide more information about that State:

- The first compartment is the name compartment, it contains the State name, for example: running, going up.
- The second compartment is the activity compartment, it contains the events and actions of the State.

You can specify State properties in the State Specification window. In the same window, you can find the description of each property. Descriptions are presented in the description area of the Specification window

##### Simple State

A simple State is a State without any regions, internal Vertices or Transitions.

##### Composite State

You can create a composite State by [CONFLUENCE_PAGE title='Changing state to composite/submachine/orthogonal state' space=''].

A composite State either contains one region or is decomposed into two or more orthogonal regions. Each region has a set of mutually exclusive disjoint subvertices and a set of transitions. A given State may only be decomposed in one of these two ways.

Any State enclosed within a region of the composite State is called a subState of that composite State. It is called a direct subState when it is not contained by any other State; otherwise it is referred to as an indirect subState.

Each region of the composite State may have an initial pseudoState and a final State. A transition to the enclosing State represents a transition to the initial pseudoState in each region.

You can specify composite State properties in the State Specification window. In the same window, you can find the description of each property. Descriptions are presented in the description area of the Specification window.

##### Orthogonal State

An orthogonal State is a composite State with at least 2 regions.

##### Submachine State

A submachine State specifies the insertion of the specification of a submachine [CONFLUENCE_PAGE title='State Machine' space='']. The State machine that contains the submachine State is called the containing State machine. The same State machine can be a submachine more than once in the context of a single containing State machine.

The submachine State is semantically equivalent to a composite State. The regions of the submachine State machine are the regions of the composite State. The entry, exit, behavior actions, and internal transitions, are defined as part of the State. The submachine State is a decomposition mechanism that allows factoring of the common behaviors and their reuse.

You can specify submachine properties in the State Specification window. In the same window, you can find the description of each property. Descriptions are presented in the description area of the Specification window.

#### PANEL: On this page

On this page

#### PANEL: Related Pages

Related Pages

- [CONFLUENCE_PAGE title='UML elements' space='']
- [CONFLUENCE_PAGE title='Stereotype' space='']
- [CONFLUENCE_PAGE title='State Machine diagram' space='MT']

#### PANEL: Related References

Related References

true

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p>A State is a condition during the lifetime of an object or an interaction during which the object meets certain conditions, performs an action, or waits for an event. The State is defined by the concepts of duration and stability. An object can not be in an unknown or undefined State. A State may have two compartments to provide more information about that State:</p><ul><li>The first compartment is the name compartment, it contains the State name, for example:<br />running, going up.</li><li>The second compartment is the activity compartment, it contains the events and actions of the State.</li></ul><p>You can specify State properties in the State Specification window. In the same window, you can find the description of each property. Descriptions are presented in the description area of the Specification window</p><h3><ac:inline-comment-marker ac:ref="84705cac-792c-4883-baa5-6fbf28e3eb45">Simple State</ac:inline-comment-marker></h3><p><ac:inline-comment-marker ac:ref="84705cac-792c-4883-baa5-6fbf28e3eb45">A simple State is a</ac:inline-comment-marker> State without any regions, internal Vertices or Transitions.</p><h3>Composite State</h3><p>You can create a composite State by <ac:link ac:anchor="simpletocomposite"><ri:page ri:content-title="Changing state to composite/submachine/orthogonal state" /><ac:plain-text-link-body><![CDATA[converting a simple State]]></ac:plain-text-link-body></ac:link>.</p><p>A composite State either contains one region or is decomposed into two or more orthogonal regions. Each region has a set of mutually exclusive disjoint subvertices and a set of transitions. A given State may only be decomposed in one of these two ways.</p><p>Any State enclosed within a region of the composite State is called a subState of that composite State. It is called a direct subState when it is not contained by any other State; otherwise it is referred to as an indirect subState.</p><p>Each region of the composite State may have an initial pseudoState and a final State. A transition to the enclosing State represents a transition to the initial pseudoState in each region.</p><p>You can specify composite State properties in the State Specification window. In the same window, you can find the description of each property. Descriptions are presented in the description area of the Specification window.</p><h3><ac:inline-comment-marker ac:ref="6c2a0fc5-f74a-40ad-8b53-748df1aed10b">Orthogonal State</ac:inline-comment-marker></h3><p><ac:inline-comment-marker ac:ref="6c2a0fc5-f74a-40ad-8b53-748df1aed10b">An orthogonal State is a composite State with at least 2 regions.</ac:inline-comment-marker></p><h3>Submachine State</h3><p>A submachine State specifies the insertion of the specification of a submachine <ac:link><ri:page ri:content-title="State Machine" /></ac:link>. The State machine that contains the submachine State is called the containing State machine. The same State machine can be a submachine more than once in the context of a single containing State machine.</p><p>The submachine State is semantically equivalent to a composite State. The regions of the submachine State machine are the regions of the composite State. The entry, exit, behavior actions, and internal transitions, are defined as part of the State. The submachine State is a decomposition mechanism that allows factoring of the common behaviors and their reuse.</p><p>You can specify submachine properties in the State Specification window. In the same window, you can find the description of each property. Descriptions are presented in the description area of the Specification window.<span style="color: rgb(129,137,156);"><br /></span></p></ac:layout-cell><ac:layout-cell><p><br /></p><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="28e6a99a-36bd-4be7-9dde-88b6c8a12e9d"><ac:parameter ac:name="title">On this page</ac:parameter><ac:rich-text-body><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="b654eb2f-f6b6-46eb-9c95-d2bbcfb10c4b" /></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="a1cb6614-da6a-4a7b-adf1-3ec18e11a18c"><ac:parameter ac:name="title">Related Pages</ac:parameter><ac:rich-text-body><ul><li><ac:link><ri:page ri:content-title="UML elements" /><ac:plain-text-link-body><![CDATA[Model Elements]]></ac:plain-text-link-body></ac:link></li><li><ac:link><ri:page ri:content-title="Stereotype" /></ac:link></li><li><ac:link><ri:page ri:space-key="MT" ri:content-title="State Machine diagram" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro><p><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="58f5fa71-99f8-438f-8820-ad28b7b75547"><ac:parameter ac:name="title">Related References</ac:parameter><ac:rich-text-body><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="111f2a89-0bdf-44f2-8de5-72ca2258a473"><ac:parameter ac:name="all">true</ac:parameter></ac:structured-macro></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="two_equal"><ac:layout-cell><p> </p></ac:layout-cell><ac:layout-cell><p> </p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=243967990 space=MED version=1 -->
## PAGE 00447: State Invariant

- page_id: `243967990`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/243967990/State+Invariant
- version_number: 1
- version_date: `2025-07-31T10:50:47.321+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UML elements > State Machine > State
- labels: []

### NORMALIZED CONTENT

1948643081

1948643101

1948643091

To define a State condition

- Double-click the State to open the State Specification window and in the State Invariant property value cell, type a condition and press Enter.
- Near the State Invariant property value cell, click the ... button. The Edit State Invariant dialog opens. Type the condition and close the dialog.

The State Invariant is displayed in square brackets on the State shape: 
[IMAGE alt='' src='']

1948643080

**Related pages**

- [CONFLUENCE_PAGE title='UML elements' space='']
- [CONFLUENCE_PAGE title='Stereotype' space='']
- [CONFLUENCE_PAGE title='State Machine diagram' space='MT']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="1defd10d-6b4a-4693-a3ca-87c7db5f5da2"><ac:parameter ac:name="id">1948643081</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="5d08ae35-17b9-416f-ab4b-6059cc965c3b"><ac:parameter ac:name="id">1948643101</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="bd80425f-bdba-48c1-a4a4-cc5cfa662509"><ac:parameter ac:name="id">1948643091</ac:parameter><ac:rich-text-body><p>To define a State condition</p><hr /><ul><li>Double-click the State to open the <strong>State</strong> Specification window and in the <strong>State Invariant</strong> property value cell, type a condition and press Enter.</li><li>Near the <strong>State </strong><strong>Invariant</strong> property value cell, click the <strong>...</strong> button. The <strong>Edit</strong><strong> State </strong><strong>Invariant</strong> dialog opens. Type the condition and close the dialog.</li></ul><p>The State Invariant is displayed in square brackets on the State shape: <br class="atl-forced-newline" /><ac:image ac:height="47" ac:width="167"><ri:attachment ri:filename="worddavda695f9d1fd6aff4ea9c66ed29b5da51.png" /></ac:image></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="d755e905-b844-4f61-a4a3-91ca4aa2dc5e"><ac:parameter ac:name="id">1948643080</ac:parameter><ac:rich-text-body><p><strong>Related pages</strong></p><ul><li><ac:link><ri:page ri:content-title="UML elements" /><ac:plain-text-link-body><![CDATA[Model Elements]]></ac:plain-text-link-body></ac:link></li><li><ac:link><ri:page ri:content-title="Stereotype" /></ac:link></li><li><ac:link><ri:page ri:space-key="MT" ri:content-title="State Machine diagram" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=243967959 space=MED version=1 -->
## PAGE 00448: State Machine

- page_id: `243967959`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/243967959/State+Machine
- version_number: 1
- version_date: `2025-07-31T10:50:46.036+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UML elements
- labels: []

### NORMALIZED CONTENT

A State Machine is a type of [CONFLUENCE_PAGE title='Behavior' space=''] that describes how a system or system component (represented by a block) reacts to events or changes in its environment. State machines are typically the classifier behavior of a block; they describe the whole life behavior of the block.

State machines consist of [CONFLUENCE_PAGE title='State' space=''], Transitions and [CONFLUENCE_PAGE title='Pseudo States' space='']. A state represents a significant and persistent condition of a block. A block will remain in a given state until triggered to transition to another state. When the triggering event occurs, the state machine will transition to another state within the region based on the triggers and guard condition specified for the transition. State machines can invoke other behaviors, including activities, interaction and other state machines. These behaviors may be invoked from within the state as entry, do, or exit behaviors or during the transition as an effect behavior. Pseudo states describe the initialization and termination of region and may be used to control the path taken by a given transition. A state machine is created when creating a [CONFLUENCE_PAGE title='State Machine diagram' space='MT'].

Specify the State Machine element in the State Machine [CONFLUENCE_PAGE title='Specification window' space='MT'].

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><span>A State Machine is a type of <ac:link><ri:page ri:content-title="Behavior" /></ac:link> that describes how a system or system component (represented by a block) reacts to events or changes in its environment. State machines are typically the classifier behavior of a block; they describe the whole life behavior of the block.  </span></p><p><span>State machines consist of <ac:link><ri:page ri:content-title="State" /></ac:link>, Transitions and <ac:link><ri:page ri:content-title="Pseudo States" /></ac:link>.  A state represents a significant and persistent condition of a block.  A block will remain in a given state until triggered to transition to another state.  When the triggering event occurs, the state machine will transition to another state within the region based on the triggers and guard condition specified for the transition.  State machines can invoke other behaviors, including activities, interaction and other state machines.  These behaviors may be invoked from within the state as entry, do, or exit behaviors or during the transition as an effect behavior.  Pseudo states describe the initialization and termination of region and may be used to control the path taken by a given transition.  A state machine is created when creating a <ac:link><ri:page ri:space-key="MT" ri:content-title="State Machine diagram" /></ac:link>. </span></p><p>Specify the State Machine element in the State Machine <ac:link><ri:page ri:space-key="MT" ri:content-title="Specification window" /></ac:link>.</p>
````

<!--NOMAGIC_PAGE id=228986113 space=MED version=2 -->
## PAGE 00449: Status Indicators

- page_id: `228986113`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/228986113/Status+Indicators
- version_number: 2
- version_date: `2025-05-14T10:31:28.000+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UAF 1.3 elements
- labels: []

### NORMALIZED CONTENT

**Description**

An enumerated type that specifies a status for a Project Theme.

**Architecture Framework**

UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0

**Extension**

UML Enumeration

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="OMGNormalParagraph"><strong>Description</strong></p><p class="OMGNormalParagraph">An enumerated type that specifies a status for a Project Theme.</p><p class="OMGNormalParagraph"><strong><span class="fontstyle0">Architecture Framework</span></strong></p><p class="OMGNormalParagraph"><span style="color: rgb(62,63,64);">UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0</span></p><p class="OMGNormalParagraph"><strong>Extension</strong></p><p class="OMGNormalParagraph">UML Enumeration</p><p><br /></p>
````

<!--NOMAGIC_PAGE id=243967992 space=MED version=2 -->
## PAGE 00450: Stereotype

- page_id: `243967992`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/243967992/Stereotype
- version_number: 2
- version_date: `2025-09-13T12:44:12.655+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UML elements
- labels: []

### NORMALIZED CONTENT

#### CONTENT-BLOCK: Storing Information

572511468

INLINE

A stereotype defines how an existing metaclass may be extended. It enables the use of a platform, a domain specific terminology, or a notation in place of, or in addition with, the ones used for the extended metaclass. Similar to a class, a stereotype may have properties which may be referred to as tag definitions. When a stereotype is applied to a model element, the values of the properties may be referred to as tagged values. A stereotype can extend any model element from the reference metamodel (any UML model element). For example in UML, States, Transitions, Activities, Use cases, Components, Attributes, Dependencies, etc. can all be extended with the stereotypes. The stereotypes are created as separate model elements and can be drawn in almost all diagrams. You can [CONFLUENCE_PAGE title='Editing property values' space='MT'] in the stereotype [CONFLUENCE_PAGE title='Specification window' space='MT']. In the same window, you can find the description of each property. Descriptions are presented in the description area of the [CONFLUENCE_PAGE title='Specification window' space='MT'].

Stereotype notation in diagrams use the guillemets instead of symbols «» (see the following figure). However, when editing elements in a diagram, you can still enter the stereotype names between the «» symbols.

[IMAGE alt='' src='']

The following procedures describe how to work with stereotypes:

##### Creating a stereotype

To create a stereotype, do one of the following

- Open or create the [CONFLUENCE_PAGE title='Profile diagram' space='MT'] . On the diagram [CONFLUENCE_PAGE title='Understanding the user interface' space='MT'] , click the Stereotype button and place it on the diagram pane.
- In the Containment tree, select a Profile, and from the shortcut menu, select Create Element > Stereotype .

##### Creating stereotype with an image

To create a stereotype with an image

1. In the stereotype's [CONFLUENCE_PAGE title='Specification window' space='MT'] , click the Icon specification cell to edit and select an [CONFLUENCE_PAGE title='Displaying icon or image' space='MT'] for the stereotype by selecting an image form:
  - the image library, click [ATTACHMENT filename='image_library.png'] .
  - the file system, click [ATTACHMENT filename='edit_button.png'] .
  - using URL, click [ATTACHMENT filename='url.png'] .
2. Select an image and click the Open button.
3. Close the Specification window.

##### Applying a stereotype

INLINE

To apply a stereotype, do one of the following:

- In the corresponding element's [CONFLUENCE_PAGE title='Specification window' space='MT'] , click the Applied Stereotype property specification cell, then click [ATTACHMENT filename='edit_button.png'] , and select stereotypes from the open list. After you have selected, click Apply .
- In the element's shortcut menu, select Stereotype and select a stereotype that you wish to apply. Click Apply when you are done.
- On the diagram pane, select an element and in that element's name area, type the stereotype name between brackets « ». The element's name comes after the stereotype. If you want to name the element Books and assign it the «table» stereotype, in the element's name area type the following: «table» Books. The name completion for the stereotypes works in the name editing mode, press Ctrl+Spacebar or Ctrl+Backspace to get a list of available stereotypes.

You can change the order of the stereotypes applied to the element. The symbol style of the last stereotype in the list will be applied to the element.

##### Changing the stereotype’s metaclass

To change the stereotype’s metaclass

1. Do one of the following:
  - On a diagram pane, select the stereotype and from its smart manipulator toolbar, choose the Metaclass button.
  - In the stereotype’s [CONFLUENCE_PAGE title='Specification window' space='MT'] , click the Metaclass specification value cell, and then click [ATTACHMENT filename='edit_button.png'] .
2. In the Select Metaclass list, select the metaclass you want to apply.
3. Click Apply when you are done.

##### Displaying the stereotype icon instead of the shape on the diagram pane

To display the stereotype icon instead of the shape on the diagram pane

1. Select the shape on the diagram and click the [CONFLUENCE_PAGE title='Displaying and suppressing compartments on shapes' space='MT'] .
2. Click [ATTACHMENT filename='expand_sm.png'] to expand the menu and select Suppress All .

##### View assigned image properties

To view assigned image properties

- In the stereotype [CONFLUENCE_PAGE title='Specification window' space='MT'] , right-click the Icon property specification cell and select Open Specification . The Image specification window opens wherein you can see and specify image properties.

##### Changing the order of the stereotypes

If a symbol has several stereotypes applied, you can change the order of stereotypes for visual purposes.

To change the order of the stereotypes

1. Right-click the symbol to open the shortcut menu, click Stereotype . The Select Stereotype dialog opens.
2. Click the Order button. The Order Stereotypes dialog opens.
3. Select a stereotype and click Up or Down buttons to change the order of the stereotypes.

##### Saving the stereotype information in XMI

You can choose the location of the applied stereotypes' information in the XMI file. Information can be saved at the end of the file or inside the element's information. By default, stereotype information is stored at the end of the XMI file.

#### INFO: Storing Information

Storing Information

To store information inside an element

- From the main menu, select Options > Environment .
- The Environment Options dialog opens.
- In the General options group > Save/Load , set the Save Stereotype Information within Element to true .

##### Changing the stereotype display mode

You can change the stereotype name and its icon visibility on an element's shape.

To change the stereotype display mode on the element shape

1. Click the shape, and then, click buttons to [CONFLUENCE_PAGE title='Displaying and suppressing compartments on shapes' space='MT'] .
2. Click the shape and then click the [CONFLUENCE_PAGE title='Displaying and suppressing compartments on shapes' space='MT'] . From the menu, click the Stereotypes and then select a desired display mode that are described in the following table:

| Show Stereotypes Property Value | Shape | Icon of the stereotype on the shape | Name of the stereotype | Image of the stereotype instead of the element shape |
| --- | --- | --- | --- | --- |
| Text and icon |  | displayed | displayed | - |
| Text |  | not displayed | displayed | - |
| Icon |  | displayed | not displayed | - |
| Shape Image and Text |  | - | displayed | displayed* |
| Shape Image |  | - | not displayed | displayed* |
| Do Not Display |  | not displayed | not displayed | - |

* To display the image of a stereotype instead of the element shape, all element compartments should be suppressed.

572511464

INLINE

**Related pages**

- [CONFLUENCE_PAGE title='Profile diagram' space='MT']
- [CONFLUENCE_PAGE title='UML elements' space='']
- [CONFLUENCE_PAGE title='UML Profiling and DSL Guide' space='MT']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="07d13643-5f16-4e30-8e54-e7721a1fe8fa"><ac:parameter ac:name="id">572511468</ac:parameter><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p>A stereotype defines how an existing metaclass may be extended. It enables the use of a platform, a domain specific terminology, or a notation in place of, or in addition with, the ones used for the extended metaclass. Similar to a class, a stereotype may have properties which may be referred to as tag definitions. When a stereotype is applied to a model element, the values of the properties may be referred to as tagged values. A stereotype can extend any model element from the reference metamodel (any UML model element). For example in UML, States, Transitions, Activities, Use cases, Components, Attributes, Dependencies, etc. can all be extended with the stereotypes. The stereotypes are created as separate model elements and can be drawn in almost all diagrams. You can <ac:link><ri:page ri:space-key="MT" ri:content-title="Editing property values" /><ac:plain-text-link-body><![CDATA[specify stereotype properties]]></ac:plain-text-link-body></ac:link> in the stereotype <ac:link><ri:page ri:space-key="MT" ri:content-title="Specification window" /></ac:link>. In the same window, you can find the description of each property. Descriptions are presented in the description area of the <ac:link><ri:page ri:space-key="MT" ri:content-title="Specification window" /></ac:link>.</p><p><span style="color: rgb(51,51,51);">Stereotype notation in diagrams use the guillemets instead of symbols «» (see the following figure).</span> However, when editing elements in a diagram, you can still enter the stereotype names between the «» symbols.</p><p><span class="confluence-embedded-file-wrapper"><ac:image ac:alt="Stereotype Notation"><ri:attachment ri:filename="stereotype_notation.png" /></ac:image></span></p><p><span class="confluence-embedded-file-wrapper"><br /></span></p><p><span class="confluence-embedded-file-wrapper">The following procedures describe how to work with stereotypes:<br /><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="170a4a0f-8cbf-437a-ae77-e0cdb6105d9f" /><br /></span></p><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><br /></p><h3>Creating a stereotype</h3><p>To create a stereotype, do one of the following</p><hr /><ul><li>Open or create the <ac:link><ri:page ri:space-key="MT" ri:content-title="Profile diagram" /><ac:plain-text-link-body><![CDATA[Profile Diagram]]></ac:plain-text-link-body></ac:link>. On the diagram <ac:link><ri:page ri:space-key="MT" ri:content-title="Understanding the user interface" /><ac:plain-text-link-body><![CDATA[pallet]]></ac:plain-text-link-body></ac:link>, click the Stereotype button and place it on the diagram pane.</li><li>In the Containment tree, select a Profile, and from the shortcut menu, select <strong>Create Element</strong> &gt; <strong>Stereotype</strong>.</li></ul><h3>Creating stereotype with an image</h3><p>To create a stereotype with an image</p><hr /><ol><li>In the stereotype's <ac:link><ri:page ri:space-key="MT" ri:content-title="Specification window" /></ac:link>, click the <strong>Icon</strong> specification cell to edit and select an <ac:link><ri:page ri:space-key="MT" ri:content-title="Displaying icon or image" /><ac:plain-text-link-body><![CDATA[image you want to place]]></ac:plain-text-link-body></ac:link> for the stereotype by selecting an image form:<br /><ul><li>the image library, click<ac:image><ri:attachment ri:filename="image_library.png" /></ac:image>.</li><li>the file system, click <ac:image><ri:attachment ri:filename="edit_button.png" /></ac:image>.</li><li>using URL, click <ac:image><ri:attachment ri:filename="url.png" /></ac:image>.</li></ul></li><li>Select an image and click the <strong>Open</strong> button.</li><li>Close the Specification window.</li></ol><h3>Applying a stereotype</h3><p><br /></p><ac:structured-macro ac:name="excerpt" ac:schema-version="1" ac:macro-id="eec8d86a-e1de-40b5-aec2-2417f9bfff50"><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><p>To apply a stereotype, do one of the following:</p><hr /><ul><li>In the corresponding element's <ac:link><ri:page ri:space-key="MT" ri:content-title="Specification window" /></ac:link>, click the <strong>Applied Stereotype</strong> property specification cell, then click <ac:image><ri:attachment ri:filename="edit_button.png" /></ac:image>, and select stereotypes from the open list. After you have selected, click <strong>Apply</strong>.</li><li>In the element's shortcut menu, select <strong>Stereotype</strong> and select a stereotype that you wish to apply. Click <strong>Apply</strong> when you are done.</li><li><p>On the diagram pane, select an element and in that element's name area, type the stereotype name between brackets « ». The element's name comes after the stereotype.</p><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="39a0c9ab-6b1a-4036-865c-135b11c0442c"><ac:rich-text-body><p>If you want to name the element Books and assign it the «table» stereotype, in the element's name area type the following: «table» Books. The name completion for the stereotypes works in the name editing mode, press Ctrl+Spacebar or Ctrl+Backspace to get a list of available stereotypes.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></li></ul><p>You can change the order of the stereotypes applied to the element. The symbol style of the last stereotype in the list will be applied to the element.</p></ac:rich-text-body></ac:structured-macro><h3>Changing the stereotype’s metaclass</h3><p>To change the stereotype’s metaclass</p><hr /><ol><li>Do one of the following:<ul><li>On a diagram pane, select the stereotype and from its smart manipulator toolbar, choose the Metaclass button.</li><li>In the stereotype’s <ac:link><ri:page ri:space-key="MT" ri:content-title="Specification window" /></ac:link>, click the <strong><ac:inline-comment-marker ac:ref="5856f592-79f9-45c4-850b-8254a3af1cec">Metaclass</ac:inline-comment-marker></strong> specification value cell, and then click <ac:image><ri:attachment ri:filename="edit_button.png" /></ac:image>.</li></ul></li><li>In the <strong><ac:inline-comment-marker ac:ref="c98ce2eb-7fe1-4487-a685-d1bcb64924f6">Select Metaclass</ac:inline-comment-marker></strong> list, select the metaclass you want to apply.</li><li>Click <strong>Apply</strong> when you are done.</li></ol><h3>Displaying the stereotype icon instead of the shape on the diagram pane</h3><p>To display the stereotype icon instead of the shape on the diagram pane</p><hr /><ol><li>Select the shape on the diagram and click the <ac:link><ri:page ri:space-key="MT" ri:content-title="Displaying and suppressing compartments on shapes" /><ac:plain-text-link-body><![CDATA[Compartments smart manipulator]]></ac:plain-text-link-body></ac:link>.</li><li>Click <ac:image><ri:attachment ri:filename="expand_sm.png" /></ac:image>to expand the menu and select <strong>Suppress All</strong>.</li></ol><h3>View assigned image properties</h3><p>To view assigned image properties</p><hr /><ul><li>In the stereotype <ac:link><ri:page ri:space-key="MT" ri:content-title="Specification window" /></ac:link>, right-click the <strong>Icon</strong> property specification cell and select <strong>Open Specification</strong>. The Image specification window opens wherein you can see and specify image properties.</li></ul><h3>Changing the order of the stereotypes</h3><p><br /></p><p>If a symbol has several stereotypes applied, you can change the order of stereotypes for visual purposes.</p><p>To change the order of the stereotypes</p><hr /><ol><li>Right-click the symbol to open the shortcut menu, click <strong>Stereotype</strong>. The <strong>Select Stereotype</strong> dialog opens.</li><li>Click the <strong>Order</strong> button. The <strong>Order Stereotypes</strong> dialog opens. </li><li>Select a stereotype and click <strong>Up</strong> or <strong>Down</strong> buttons to change the order of the stereotypes.</li></ol><p><br /></p><h3>Saving the stereotype information in XMI</h3><p>You can choose the location of the applied stereotypes' information in the XMI file. Information can be saved at the end of the file or inside the element's information. By default, stereotype information is stored at the end of the XMI file.</p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="fec924fc-aecb-436c-903a-e593b7178ed5"><ac:parameter ac:name="title">Storing Information </ac:parameter><ac:rich-text-body><p>To store information inside an element</p><hr /><ul><li>From the main menu, select <strong>Options</strong> &gt; <strong>Environment</strong>. </li><li>The <strong>Environment Options</strong> dialog opens.</li><li>In the <strong>General</strong> options group &gt; <strong>Save/Load</strong>, set the <strong>Save Stereotype Information within Element</strong> to <em>true</em>.</li></ul></ac:rich-text-body></ac:structured-macro><h3>Changing the stereotype display mode</h3><p>You can change the stereotype name and its icon visibility on an element's shape.</p><p><br />To change the stereotype display mode on the element shape</p><hr /><ol><li>Click the shape, and then, click buttons to <ac:link><ri:page ri:space-key="MT" ri:content-title="Displaying and suppressing compartments on shapes" /><ac:plain-text-link-body><![CDATA[suppress all the compartments]]></ac:plain-text-link-body></ac:link>.</li><li>Click the shape and then click the <ac:link><ri:page ri:space-key="MT" ri:content-title="Displaying and suppressing compartments on shapes" /><ac:plain-text-link-body><![CDATA[Compartments button]]></ac:plain-text-link-body></ac:link>. From the menu, click the <strong>Stereotypes</strong> and then select a desired display mode that are described in the following table:</li></ol><p><br /></p><table class="wrapped"><tbody><tr><th><p>Show Stereotypes <br />Property Value</p></th><th>Shape</th><th><p>Icon of the <br />stereotype on <br />the shape</p></th><th><p>Name of the <br />stereotype</p></th><th><p>Image of the <br />stereotype <br />instead of the <br />element shape</p></th></tr><tr><td>Text and icon</td><td><div class="content-wrapper"><ac:image><ri:attachment ri:filename="stereotype_mode_1.gif" /></ac:image></div></td><td>displayed</td><td>displayed</td><td>-</td></tr><tr><td><p>Text</p></td><td><div class="content-wrapper"><ac:image><ri:attachment ri:filename="stereotype_mode_2.gif" /></ac:image></div></td><td>not displayed</td><td>displayed</td><td>-</td></tr><tr><td>Icon</td><td><div class="content-wrapper"><ac:image><ri:attachment ri:filename="stereotype_mode_3.gif" /></ac:image></div></td><td>displayed</td><td>not displayed</td><td>-</td></tr><tr><td><p>Shape Image and Text</p></td><td><div class="content-wrapper"><ac:image><ri:attachment ri:filename="stereotype_mode_4.gif" /></ac:image></div></td><td>-</td><td>displayed</td><td>displayed*</td></tr><tr><td>Shape Image</td><td><div class="content-wrapper"><ac:image><ri:attachment ri:filename="stereotype_mode_5.gif" /></ac:image></div></td><td>-</td><td>not displayed</td><td>displayed*</td></tr><tr><td>Do Not Display</td><td><div class="content-wrapper"><ac:image><ri:attachment ri:filename="stereotype_mode_6.gif" /></ac:image></div></td><td>not displayed</td><td>not displayed</td><td>-</td></tr></tbody></table><p>* To display the image of a stereotype instead of the element shape, all element compartments should be suppressed.</p><p><br /></p><p><span style="color: rgb(255,0,0);"><br /></span></p></ac:layout-cell></ac:layout-section></ac:layout></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="432f3828-f870-4c80-ab3c-fb81dda953d6"><ac:parameter ac:name="id">572511464</ac:parameter><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><p><strong>Related pages</strong></p><ul><li><ac:link><ri:page ri:space-key="MT" ri:content-title="Profile diagram" /></ac:link></li><li><ac:link><ri:page ri:content-title="UML elements" /><ac:plain-text-link-body><![CDATA[Model Elements]]></ac:plain-text-link-body></ac:link></li><li><p class="with-breadcrumbs"><ac:link><ri:page ri:space-key="MT" ri:content-title="UML Profiling and DSL Guide" /></ac:link></p></li></ul><p class="auto-cursor-target"><br /></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p>
````

<!--NOMAGIC_PAGE id=228986114 space=MED version=2 -->
## PAGE 00451: Strategic Constraint

- page_id: `228986114`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/228986114/Strategic+Constraint
- version_number: 2
- version_date: `2025-05-14T10:31:28.297+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UAF 1.3 elements
- labels: []

### NORMALIZED CONTENT

**Description**

A Rule governing a Capability.

**Architecture Framework**

UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0

**Extension**

Rule

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description</strong></p><p>A Rule governing a Capability.</p><p><strong>Architecture Framework</strong></p><p><span style="color: rgb(62,63,64);">UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0</span></p><p><strong>Extension</strong></p><p>Rule</p>
````

<!--NOMAGIC_PAGE id=228986115 space=MED version=2 -->
## PAGE 00452: Strategic Exchange

- page_id: `228986115`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/228986115/Strategic+Exchange
- version_number: 2
- version_date: `2025-05-14T10:31:28.554+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UAF 1.3 elements
- labels: []

### NORMALIZED CONTENT

**Description**

Asserts that a flow can exist between Actual Strategic Phases (i.e. flows of information, people, materiel, or energy).

**Architecture Framework**

UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0

**Extensions**

Information Flow

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description</strong></p><p class="OMGNormalParagraph">Asserts that a flow can exist between Actual Strategic Phases (i.e. flows of information, people, materiel, or energy).</p><p class="OMGNormalParagraph"><strong>Architecture Framework</strong></p><p class="OMGNormalParagraph"><span style="color: rgb(62,63,64);">UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0</span></p><p class="OMGNormalParagraph"><strong>Extensions</strong></p><p class="OMGNormalParagraph">Information Flow</p>
````

<!--NOMAGIC_PAGE id=228986116 space=MED version=2 -->
## PAGE 00453: Strategic Information

- page_id: `228986116`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/228986116/Strategic+Information
- version_number: 2
- version_date: `2025-05-14T10:31:28.878+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UAF 1.3 elements
- labels: []

### NORMALIZED CONTENT

**Description**

Knowledge communicated or received concerning a particular fact or circumstance that is strategic in nature that is important or essential in relation to a plan of action.

**Architecture Framework**

UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0

**Extensions**

Class

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description</strong></p><p class="OMGNormalParagraph">Knowledge communicated or received concerning a particular fact or circumstance that is strategic in nature that is important or essential in relation to a plan of action.</p><p><strong>Architecture Framework</strong></p><p><span style="color: rgb(62,63,64);">UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0</span></p><p><strong>Extensions</strong></p><p>Class</p>
````

<!--NOMAGIC_PAGE id=228986117 space=MED version=2 -->
## PAGE 00454: Strategic Phase

- page_id: `228986117`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/228986117/Strategic+Phase
- version_number: 2
- version_date: `2025-05-14T10:31:29.469+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UAF 1.3 elements
- labels: []

### NORMALIZED CONTENT

**Description**

A type of a current or future phase of the enterprise, mission, Value Stream, or Enduring Task.

**Architecture Framework**

UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0

**Extension**

Class

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="OMGNormalParagraph"><strong>Description</strong></p><p class="OMGNormalParagraph">A type of a current or future phase of the enterprise, mission, Value Stream, or Enduring Task.</p><p class="OMGNormalParagraph"><strong>Architecture Framework</strong></p><p class="OMGNormalParagraph"><span style="color: rgb(62,63,64);">UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0</span></p><p class="OMGNormalParagraph"><strong>Extension</strong></p><p class="OMGNormalParagraph">Class</p><p><br /></p>
````

<!--NOMAGIC_PAGE id=228986118 space=MED version=2 -->
## PAGE 00455: Structural Part

- page_id: `228986118`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/228986118/Structural+Part
- version_number: 2
- version_date: `2025-05-14T10:31:29.827+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UAF 1.3 elements
- labels: []

### NORMALIZED CONTENT

**Description**

Usage of an Enterprise Phase in the context of another Enterprise Phase. It asserts that one Enterprise Phase is a spatial part of another. Creates a whole-part relationship that represents the structure of the Enterprise Phase.

**Architecture Framework**

UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0

**Extension**

UML Property

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="OMGNormalParagraph"><strong>Description</strong></p><p class="OMGNormalParagraph">Usage of an Enterprise Phase in the context of another Enterprise Phase. It asserts that one Enterprise Phase is a spatial part of another. Creates a whole-part relationship that represents the structure of the Enterprise Phase. </p><p class="OMGNormalParagraph"><strong><span class="fontstyle0">Architecture Framework</span></strong></p><p class="OMGNormalParagraph"><span style="color: rgb(62,63,64);">UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0</span></p><p class="OMGNormalParagraph"><strong>Extension</strong></p><p class="OMGNormalParagraph">UML Property</p><p><br /></p>
````

<!--NOMAGIC_PAGE id=243967824 space=MED version=1 -->
## PAGE 00456: Structured Activity Node

- page_id: `243967824`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/243967824/Structured+Activity+Node
- version_number: 1
- version_date: `2025-07-31T10:50:42.425+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UML elements > Node
- labels: []

### NORMALIZED CONTENT

A Structured Activity Node is an executable activity node that may have an expansion into subordinate nodes as an activity group. The subordinate nodes must belong to only one Structured Activity Node, although they may be nested.

To create a Structured Activity Node

1. Expand the Activity diagram palette and click the Structured Activity Node icon . [ATTACHMENT filename='select_structured_activity_node.png']
2. Click on the Activity diagram pane. The Structured Activity Node is created.
3. (Optional) To specify the Structured Activity Node, right-click the symbol and open its [CONFLUENCE_PAGE title='Specification window' space='MT'] .

[IMAGE alt='' src='']

###### A variable is defined in the scope of the Structured Activity Node. It has no value and may not be accessed outside the node.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><span>A Structured Activity Node is an executable activity node that may have an expansion into subordinate nodes as an activity group. The subordinate nodes must belong to only one Structured Activity Node, although they may be nested.</span></p><p>To create a <span>Structured Activity Node </span></p><hr /><ol><li>Expand the Activity diagram palette and click the <strong> <span>Structured Activity Node </span> </strong> <span>icon</span>.<br /> <ac:image><ri:attachment ri:filename="select_structured_activity_node.png" /></ac:image></li><li>Click on the Activity diagram pane. The <span>Structured Activity Node</span> is created. </li><li>(Optional) To specify the Structured Activity Node, right-click the symbol and open its <ac:link><ri:page ri:space-key="MT" ri:content-title="Specification window" /></ac:link><span>.  </span></li></ol><p><ac:image ac:align="center"><ri:attachment ri:filename="Structured_activity_in_diagram.png" /></ac:image></p><h6 style="text-align: center;">A variable is defined in the scope of the Structured Activity Node. It has no value and may not be accessed outside the node.</h6>
````

<!--NOMAGIC_PAGE id=228986119 space=MED version=2 -->
## PAGE 00457: Subject Of Forecast

- page_id: `228986119`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/228986119/Subject+Of+Forecast
- version_number: 2
- version_date: `2025-05-14T10:31:30.179+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UAF 1.3 elements
- labels: []

### NORMALIZED CONTENT

**Description**

An abstract grouping of elements that can be the subject of a Forecast.

**Architecture Framework**

UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0

**Extension**

UML Class

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="OMGNormalParagraph"><strong>Description</strong></p><p class="OMGNormalParagraph">An abstract grouping of  elements that can be the subject of a Forecast.</p><p class="OMGNormalParagraph"><strong>Architecture Framework</strong></p><p class="OMGNormalParagraph"><span style="color: rgb(62,63,64);">UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0</span></p><p class="OMGNormalParagraph"><strong>Extension</strong></p><p class="OMGNormalParagraph">UML Class</p><p><br /></p>
````

<!--NOMAGIC_PAGE id=228986120 space=MED version=2 -->
## PAGE 00458: Subject Of Operational Constraint

- page_id: `228986120`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/228986120/Subject+Of+Operational+Constraint
- version_number: 2
- version_date: `2025-05-14T10:31:30.472+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UAF 1.3 elements
- labels: []

### NORMALIZED CONTENT

**Description**

An abstract grouping of elements that can be the subject of an Operational Constraint.

**Architecture Framework**

UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0

**Extension**

Element

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="OMGNormalParagraph"><strong>Description</strong></p><p class="OMGNormalParagraph">An abstract grouping of elements that can be the subject of an Operational Constraint.</p><p class="OMGNormalParagraph"><strong>Architecture Framework</strong></p><p class="OMGNormalParagraph"><span style="color: rgb(62,63,64);">UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0</span></p><p class="OMGNormalParagraph"><strong>Extension</strong></p><p class="OMGNormalParagraph">Element</p><p><br /></p>
````

<!--NOMAGIC_PAGE id=228986121 space=MED version=2 -->
## PAGE 00459: Subject Of Resource Constraint

- page_id: `228986121`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/228986121/Subject+Of+Resource+Constraint
- version_number: 2
- version_date: `2025-05-14T10:31:30.818+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UAF 1.3 elements
- labels: []

### NORMALIZED CONTENT

**Description**

An abstract grouping of elements that can be the subject of a Resource Constraint.

**Architecture** **Framework**

UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0

**Extension**

Element

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="OMGBoldBulletKeepNextParagraph"><strong>Description</strong></p><p class="OMGNormalParagraph">An abstract grouping of elements that can be the subject of a Resource Constraint. </p><p class="OMGNormalParagraph"><strong>Architecture</strong> <strong>Framework</strong></p><p class="OMGNormalParagraph"><span style="color: rgb(62,63,64);">UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0</span></p><p class="OMGNormalParagraph"><strong>Extension</strong></p><p class="OMGNormalParagraph">Element </p><p><br /></p>
````

<!--NOMAGIC_PAGE id=228986122 space=MED version=2 -->
## PAGE 00460: Subject Of Security Constraint

- page_id: `228986122`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/228986122/Subject+Of+Security+Constraint
- version_number: 2
- version_date: `2025-05-14T10:31:31.346+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UAF 1.3 elements
- labels: []

### NORMALIZED CONTENT

**Description**

An abstract grouping of elements that can be the subject of a Security Constraint.

**Architecture Framework**

UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0

**Extension**

Element

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="OMGNormalParagraph"><strong>Description</strong></p><p class="OMGNormalParagraph">An abstract grouping of elements that can be the subject of a Security Constraint.</p><p class="OMGNormalParagraph"><strong>Architecture Framework</strong></p><p class="OMGNormalParagraph"><span style="color: rgb(62,63,64);">UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0</span></p><p class="OMGNormalParagraph"><strong>Extension</strong></p><p class="OMGNormalParagraph">Element</p><p><br /></p>
````

<!--NOMAGIC_PAGE id=243968004 space=MED version=1 -->
## PAGE 00461: Substitution

- page_id: `243968004`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/243968004/Substitution
- version_number: 1
- version_date: `2025-07-31T10:50:47.513+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UML elements
- labels: []

### NORMALIZED CONTENT

A substitution is a relationship between two [CONFLUENCE_PAGE title='Specifying the classifier' space='MT']. In these cases, the substituting Classifier complies with the contract specified by the contract classifier. Instances of the substituting Classifier are runtime substitutable where instances of the contract classifier are expected. 
Specify the Substitution element in the Substitution [CONFLUENCE_PAGE title='Specification window' space='MT'].

You can see which elements the Substitution is drawn between in the Substitution dialog, Source and Target boxes.

You can format the Substitution symbol properties in the [CONFLUENCE_PAGE title='Symbol Properties dialog' space='MT'].

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><span style="color: rgb(0,0,0);">A substitution is a relationship between two <ac:link><ri:page ri:space-key="MT" ri:content-title="Specifying the classifier" /><ac:plain-text-link-body><![CDATA[Classifiers]]></ac:plain-text-link-body></ac:link>. In these cases, the substituting Classifier complies with the contract specified by the contract classifier. Instances of the substituting Classifier are runtime substitutable where instances of the contract classifier are expected.  </span><br /><span style="color: rgb(0,0,0);">Specify the Substitution element in the Substitution <ac:link><ri:page ri:space-key="MT" ri:content-title="Specification window" /></ac:link></span><span style="color: rgb(0,0,0);">. </span></p><p>You can see which elements the Substitution is drawn between in the <span class="hcp1">Substitution</span> dialog, <span class="hcp1">Source</span> and <span class="hcp1">Target</span> boxes.</p><p>You can format the Substitution symbol properties in the <ac:link><ri:page ri:space-key="MT" ri:content-title="Symbol Properties dialog" /></ac:link>.</p>
````

<!--NOMAGIC_PAGE id=243968005 space=MED version=1 -->
## PAGE 00462: Subsystem

- page_id: `243968005`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/243968005/Subsystem
- version_number: 1
- version_date: `2025-07-31T10:50:47.678+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UML elements
- labels: []

### NORMALIZED CONTENT

A subsystem is treated as an abstract single unit. It groups model elements by representing the behavioral unit in a physical system.

To draw a subsystem

- On the Use Case diagram palette, click the Subsystem button, and then click the diagram pane.

#### PANEL: Related Pages

Related Pages

- [CONFLUENCE_PAGE title='UML elements' space='']
- [CONFLUENCE_PAGE title='Stereotype' space='']
- [CONFLUENCE_PAGE title='Use Case diagram' space='MT']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p>A subsystem is treated as an abstract single unit. It groups model elements by representing the behavioral unit in a physical system.</p><p> </p><p>To draw a subsystem</p><hr /><ul><li>On the Use Case diagram palette, click the <strong>Subsystem</strong> button, and then click the diagram pane.</li></ul><p><br /></p></ac:layout-cell><ac:layout-cell><p> </p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="a1cb6614-da6a-4a7b-adf1-3ec18e11a18c"><ac:parameter ac:name="title">Related Pages</ac:parameter><ac:rich-text-body><ul><li><ac:link><ri:page ri:content-title="UML elements" /><ac:plain-text-link-body><![CDATA[Model Elements]]></ac:plain-text-link-body></ac:link></li><li><ac:link><ri:page ri:content-title="Stereotype" /></ac:link></li><li><ac:link><ri:page ri:space-key="MT" ri:content-title="Use Case diagram" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=9919412 space=MED version=12 -->
## PAGE 00463: Subsystem in SysML v1

- page_id: `9919412`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/9919412/Subsystem+in+SysML+v1
- version_number: 12
- version_date: `2025-09-13T12:46:27.106+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > SysML v1 elements
- labels: []

### NORMALIZED CONTENT

A Subsystem is typically a large, encapsulated block within a larger system.

You can convert any Block to a Subsystem if you decide that the appropriate Block is decomposed. It may be called a system (i.e., Power Subsystem, Brake Subsystem, Lightening Subsystem).

[IMAGE alt='' src='']

#### NOTE: Visibility representation

Visibility representation

In SysML, properties and operations of the Block are public. Visibility representation literals, like +, #, ~, -, are not displayed in the Containment tree or in the element symbol on a diagram.

##### Converting a Block to Subsystem

To convert a Block to Subsystem

1. Right-click a Block.
2. Select Refactor > Convert To > More Specific > Subsystem . The Block is converted to a Subsystem.

**Related pages**

- [CONFLUENCE_PAGE title='SysML Block Definition Diagram' space='MT']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p>A Subsystem is typically a large, encapsulated block within a larger system.</p><p>You can convert any Block to a Subsystem <span style="color:var(--ds-text,#333333);">if you decide that the appropriate Block is decomposed. It may be called a system (i.e., Power Subsystem, Brake Subsystem, Lightening Subsystem).</span></p><p><br /></p><p><ac:image ac:title="Subsystem" ac:alt="Subsystem"><ri:attachment ri:filename="subsystem.png" /></ac:image></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="45e244e1-7a14-47d4-88f2-ec499c585171"><ac:parameter ac:name="title">Visibility representation</ac:parameter><ac:rich-text-body><p><span style="color:var(--ds-text,#333333);">In SysML, properties and operations of the Block are public. Visibility representation literals, like +, #, ~, -, are not displayed in the Containment tree or in the element symbol on a diagram.<br /></span></p></ac:rich-text-body></ac:structured-macro><h3>Converting a Block to Subsystem</h3><p>To convert a Block to Subsystem</p><hr /><ol><li data-uuid="7d023fde-ac7d-4315-9e98-d89b6a93fa6b">Right-click a Block.</li><li data-uuid="b6828cbd-25cd-481c-96be-98cf79a6800c">Select <strong>Refactor</strong> &gt; <strong>Convert To</strong> &gt; <strong>More Specific</strong> &gt; <strong>Subsystem</strong>.<br />The Block is converted to a Subsystem.</li></ol></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><strong>Related pages</strong></p><ul><li data-uuid="9a7f142b-da7c-4c27-9855-b6451328ceb3"><ac:link><ri:page ri:space-key="MT" ri:content-title="SysML Block Definition Diagram" /></ac:link></li></ul></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=228986123 space=MED version=2 -->
## PAGE 00464: Supports

- page_id: `228986123`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/228986123/Supports
- version_number: 2
- version_date: `2025-05-14T10:31:31.918+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UAF 1.3 elements
- labels: []

### NORMALIZED CONTENT

**Description**

A abstraction relationship that asserts that a service in someway contributes or assists in the execution of an Operational Activity.

**Architecture Framework**

UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0

**Extension**

Abstraction

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="OMGNormalParagraph"><strong>Description</strong></p><p class="OMGNormalParagraph">A abstraction relationship that asserts that a service in someway contributes or assists in the execution of an Operational Activity.</p><p class="OMGNormalParagraph"><strong>Architecture Framework</strong></p><p class="OMGNormalParagraph"><span style="color: rgb(62,63,64);">UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0</span></p><p class="OMGNormalParagraph"><strong>Extension</strong></p><p class="OMGNormalParagraph">Abstraction</p><p><br /></p>
````

<!--NOMAGIC_PAGE id=243968006 space=MED version=1 -->
## PAGE 00465: Swimlanes

- page_id: `243968006`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/243968006/Swimlanes
- version_number: 1
- version_date: `2025-07-31T10:50:47.729+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UML elements
- labels: []

### NORMALIZED CONTENT

1404690412

1404690415

1404690414

INLINE

Actions and subactivities can be organized into Swimlanes in the Activity diagrams. Swimlanes are used to organize responsibility for actions and subactivities according to class. They often correspond to the organizational units in a business model.

Swimlanes limit and provide a view of the behaviors invoked in the activities. They consist of one or more partitions and can be vertical or horizontal.

An Activity diagram can be visually divided into Swimlanes, each separated from the neighboring Swimlanes by vertical or horizontal solid lines on both sides. Each Swimlane represents a responsibility for part of the overall activity, and may eventually be implemented by one or more objects. The relative ordering of the Swimlanes has no semantic significance, but can indicate some affinity. Each action is assigned to one Swimlane. Transitions can cross lanes. The routing of a transition path is non-essential.

You can customize Swimlane representation by changing its symbol property values. Press Alt + Enter to open the appropriate dialog. Each property is described in the description area on this dialog.

To create a Swimlane

1. On the Activity diagram palette, click the **Vertical Swimlanes** button [IMAGE alt='' src='']and then click an empty space on the diagram pane.
2. If the **Represent Properties** dialog opens, select the properties you want to display as Swimlanes in the diagram (see the following figure) and click **OK**. Otherwise, a few empty Swimlanes are created. The **Represent Properties** dialog opens if:The Activity diagram is owned by a classifier, such as a Class, Component, Use Case.The classifier or its [CONFLUENCE_PAGE title='Specifying a Use Case subject' space=''] has properties.Partitions are created for each property you select to represent as a Swimlane in the Activity diagram. [IMAGE alt='' src='']

You can also create a Swimlane by dragging one or more properties, Actors, Classes, or Instance Specifications from the Containment tree to the Activity diagram pane. Partitions for each element are created as well.

To set representative elements, do one of the following

- Open the Specification window of the Swimlane and click the cell of the Represents property value. Then click [ATTACHMENT filename='3dot_button.png'] and select the element. Click OK when you are done.
- From the Containment tree, drag the representative element to the partition on the diagram.

To add an additional partition, do one of the following

- On the diagram, right-click the Swimlane, select Insert Swimlane and then Insert Vertical Swimlane or Insert Horizontal Swimlane .
- From the Containment tree, drag one or more property, actor, class or instance specification elements to the Swimlane on the diagram.

To draw multidimensional Swimlanes

1. Draw a vertical Swimlane.
2. From the Swimlane shortcut menu, select Insert Horizontal Swimlane .
3. Insert as many horizontal and vertical Swimlanes as you need.

To add model elements to a Swimlane

- If a Swimlane is already drawn in the Activity diagram, drawing an action (or any other element) highlights the Swimlane in blue. This means the action shape depends on the Swimlane symbol. If the model elements depend on a Swimlane symbol, they are deleted if the Swimlane symbol is deleted. [IMAGE alt='' src='']

To rearrange Swimlanes, do one of the following

- Drag any of the Swimlanes in the direction where you want it to be.
- Click the heading of any Swimlane and use the displayed control arrow to move the Swimlane left, right, up or down. [ATTACHMENT filename='move_swimlane_left_button.png']

To delete a single Swimlane entirely, do one of the following

- Click the header of the Swimlane, then press Delete.
- Click the header of the Swimlane, then press Ctrl + D.
- Right-click the header or any empty space on the Swimlane, then select Delete Swimlane .

To delete all Swimlanes and their contents

- Click any empty space on the Swimlanes, then press Ctrl + D.

To delete Swimlanes without deleting contained elements, do one of the following

- Click any empty space on the Swimlanes, then press Delete.
- Right-click the headers or anywhere on the Swimlanes, then select Delete All Swimlanes, Keep Contents .

1404690411

**Rrelated pages**

- [CONFLUENCE_PAGE title='Formatting symbols' space='MT']
- [CONFLUENCE_PAGE title='UML elements' space='']
- [CONFLUENCE_PAGE title='Activity diagram' space='MT']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="8b55eb8c-1c7d-41fd-a310-16a01c7216d9"><ac:parameter ac:name="id">1404690412</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="a38f4c21-39ef-447d-8984-e24914b7625d"><ac:parameter ac:name="id">1404690415</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="78e40bc8-f8fa-4a0a-b407-69473cf417ef"><ac:parameter ac:name="id">1404690414</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="excerpt" ac:schema-version="1" ac:macro-id="8d537487-093a-4301-bce3-914e9ae1198e"><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><p>Actions and subactivities can be organized into Swimlanes in the Activity diagrams. Swimlanes are used to organize responsibility for actions and subactivities according to class. They often correspond to the organizational units in a business model.</p><p>Swimlanes limit and provide a view of the behaviors invoked in the activities. They consist of one or more partitions and can be vertical or horizontal.</p><p>An Activity diagram can be visually divided into Swimlanes, each separated from the neighboring Swimlanes by vertical or horizontal solid lines on both sides. Each Swimlane represents a responsibility for part of the overall activity, and may eventually be implemented by one or more objects. The relative ordering of the Swimlanes has no semantic significance, but can indicate some affinity. Each action is assigned to one Swimlane. Transitions can cross lanes. The routing of a transition path is non-essential.</p><p>You can customize Swimlane representation by changing its symbol property values. Press Alt + Enter to open the appropriate dialog. Each property is described in the description area on this dialog.</p><p><br /></p><p>To create a Swimlane</p><hr /><ol><li><p>On the Activity diagram palette, click the <strong>Vertical Swimlanes</strong> button <ac:image ac:title="Vertical Swimlanes" ac:alt="Vertical Swimlanes" ac:height="16" ac:width="19"><ri:attachment ri:filename="vertical_swimlanes_button.png" /></ac:image>and then click an empty space on the diagram pane.</p></li><li><p>If the <strong>Represent Properties</strong> dialog opens, select the properties you want to display as Swimlanes in the diagram (see the following figure) and click <strong>OK</strong>. Otherwise, a few empty Swimlanes are created.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="1cc1a1a0-eadf-4c9f-9895-8b9eafae3c97"><ac:rich-text-body><p>The <strong>Represent Properties</strong> dialog opens if:</p><ol><li>The Activity diagram is owned by a classifier, such as a Class, Component, Use Case.</li><li class="confluence-link">The classifier or its <ac:link><ri:page ri:content-title="Specifying a Use Case subject" /><ac:plain-text-link-body><![CDATA[subject]]></ac:plain-text-link-body></ac:link> has properties.</li></ol><p class="confluence-link">Partitions are created for each property you select to represent as a Swimlane in the Activity diagram.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><ac:image><ri:attachment ri:filename="represent_proerties_dialog.png" /></ac:image></p></li></ol><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="cf9e5eb3-43c7-44e9-b1d8-fe8d25db6559"><ac:rich-text-body><p>You can also create a Swimlane by dragging one or more properties, Actors, Classes, or Instance Specifications from the Containment tree to the Activity diagram pane. Partitions for each element are created as well.</p></ac:rich-text-body></ac:structured-macro><p><br /></p><p>To set representative elements, do one of the following</p><hr /><ul><li>Open the Specification window of the Swimlane and click the cell of the <strong>Represents</strong> property value. Then click <ac:image><ri:attachment ri:filename="3dot_button.png" /></ac:image> and select the element. Click <strong>OK</strong> when you are done.</li><li>From the Containment tree, drag the representative element to the partition on the diagram.</li></ul><p><br /></p><p>To add an additional partition, do one of the following</p><hr /><ul><li>On the diagram, right-click the Swimlane, select <strong>Insert Swimlane</strong> and then <strong>Insert Vertical Swimlane</strong> or <strong>Insert Horizontal Swimlane</strong>.</li><li>From the Containment tree, drag one or more property, actor, class or instance specification elements to the Swimlane on the diagram.</li></ul><p><br /></p><p>To draw multidimensional Swimlanes</p><hr /><ol><li>Draw a vertical Swimlane.</li><li>From the Swimlane shortcut menu, select <strong>Insert Horizontal Swimlane</strong>.</li><li>Insert as many horizontal and vertical Swimlanes as you need.</li></ol><p><br /></p><p>To add model elements to a Swimlane</p><hr /><ul><li><p>If a Swimlane is already drawn in the Activity diagram, drawing an action (or any other element) highlights the Swimlane in blue. This means the action shape depends on the Swimlane symbol.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="89894628-0c8c-46eb-b11a-2feca4677335"><ac:rich-text-body><p>If the model elements depend on a Swimlane symbol, they are deleted if the Swimlane symbol is deleted.</p></ac:rich-text-body></ac:structured-macro><p><ac:image ac:title="Example of multidimensional swimlane" ac:alt="Example of multidimensional swimlane"><ri:attachment ri:filename="multidimensional_swimlane_example.png" /></ac:image></p></li></ul><p><br /></p><p>To rearrange Swimlanes, do one of the following</p><hr /><ul><li>Drag any of the Swimlanes in the direction where you want it to be.</li><li>Click the heading of any Swimlane and use the displayed control arrow to move the Swimlane left, right, up or down.<br /><ac:image ac:title="Example of 'Move Swimlane Left' Control" ac:alt="Example of 'Move Swimlane Left' Control"><ri:attachment ri:filename="move_swimlane_left_button.png" /></ac:image></li></ul><p><br /></p><p>To delete a single Swimlane entirely, do one of the following</p><hr /><ul><li>Click the header of the Swimlane, then press Delete.</li><li>Click the header of the Swimlane, then press Ctrl + D.</li><li>Right-click the header or any empty space on the Swimlane, then select <strong>Delete Swimlane</strong>.</li></ul><p><br /></p><p>To delete all Swimlanes and their contents</p><hr /><ul><li>Click any empty space on the Swimlanes, then press Ctrl + D.</li></ul><p><br /></p><p>To delete Swimlanes without deleting contained elements, do one of the following</p><hr /><ul><li>Click any empty space on the Swimlanes, then press Delete.</li><li>Right-click the headers or anywhere on the Swimlanes, then select <strong>Delete All Swimlanes, Keep Contents</strong>.</li></ul></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="6b2cf620-7b55-47f4-a0ef-37c858820a97"><ac:parameter ac:name="id">1404690411</ac:parameter><ac:rich-text-body><p><strong>Rrelated pages</strong></p><ul><li><ac:link><ri:page ri:space-key="MT" ri:content-title="Formatting symbols" /></ac:link></li><li><ac:link><ri:page ri:content-title="UML elements" /><ac:plain-text-link-body><![CDATA[Model Elements]]></ac:plain-text-link-body></ac:link></li><li><ac:link><ri:page ri:space-key="MT" ri:content-title="Activity diagram" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=9919400 space=MED version=7 -->
## PAGE 00466: SysML v1 elements

- page_id: `9919400`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/9919400/SysML+v1+elements
- version_number: 7
- version_date: `2025-08-25T12:26:11.640+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions
- labels: []

### NORMALIZED CONTENT



### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="963fdb26-1821-4c72-826f-06bf1ca2c77e" /></p></ac:layout-cell><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=243964901 space=MED version=9 -->
## PAGE 00467: SysML v1/UAF/UML Model Element Descriptions

- page_id: `243964901`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/243964901/SysML+v1+UAF+UML+Model+Element+Descriptions
- version_number: 9
- version_date: `2025-10-30T13:18:22.647+01:00`
- ancestors: 
- labels: []

### NORMALIZED CONTENT

This guide describes model elements defined in UML, SysML v1, and UAF 1.3 language specifications. To learn more, select one of the following topics:

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><span style="color:var(--ds-text,#172b4d);">This guide describes model elements defined in UML, SysML v1, and UAF 1.3 language specifications. To learn more, select one of the following topics:</span></p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="c6f87278-036b-415d-a398-0c3b17faf502" /></p>
````

<!--NOMAGIC_PAGE id=9919407 space=MED version=9 -->
## PAGE 00468: System

- page_id: `9919407`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/9919407/System
- version_number: 9
- version_date: `2025-09-13T12:46:26.487+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > SysML v1 elements
- labels: []

### NORMALIZED CONTENT

#### CONTENT-LAYER: Visibility representation

299125027

#### CONTENT-COLUMN: Visibility representation

299125030

#### CONTENT-BLOCK: Visibility representation

299125029

A System is an artificial artifact consisting of blocks that pursue a common goal which cannot be achieved by the system's individual elements. A block can be software, hardware, a person, or an arbitrary unit.

[IMAGE alt='' src='']

#### NOTE: Visibility representation

Visibility representation

In SysML, properties and operations of the Block are public. Visibility representation literals, like +, #, ~, -, are not displayed in the Containment tree or in the element symbol on a diagram.

299125026

**Related pages**

- [CONFLUENCE_PAGE title='SysML Block Definition Diagram' space='MT']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="d58715bb-5b47-4fd0-9ebd-785e28044f02"><ac:parameter ac:name="id">299125027</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="443e7043-7c26-4edc-8b16-63f86b5a4c25"><ac:parameter ac:name="id">299125030</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="2e3f04e8-4f9d-4f80-8b0d-30595dd8ef5c"><ac:parameter ac:name="id">299125029</ac:parameter><ac:rich-text-body><p>A System is an artificial artifact consisting of blocks that pursue a common goal which cannot be achieved by the system's individual elements. A block can be software, hardware, a person, or an arbitrary unit.</p><p><ac:image ac:title="System" ac:alt="System"><ri:attachment ri:filename="system.png" /></ac:image></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="45e244e1-7a14-47d4-88f2-ec499c585171"><ac:parameter ac:name="title">Visibility representation</ac:parameter><ac:rich-text-body><p><span style="color: rgb(62,63,64);">In SysML, properties and operations of the Block are public. Visibility representation literals, like +, #, ~, -, are not displayed in the Containment tree or in the element symbol on a diagram.</span></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="533769e2-0e4b-4142-bbf0-898a7e7599e6"><ac:parameter ac:name="id">299125026</ac:parameter><ac:rich-text-body><p><strong>Related pages</strong></p><ul><li><ac:link><ri:page ri:space-key="MT" ri:content-title="SysML Block Definition Diagram" /><ac:plain-text-link-body><![CDATA[SysML Block Definition Diagram ]]></ac:plain-text-link-body></ac:link></li></ul></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=9919481 space=MED version=8 -->
## PAGE 00469: System Context

- page_id: `9919481`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/9919481/System+Context
- version_number: 8
- version_date: `2025-09-13T12:46:30.092+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > SysML v1 elements
- labels: []

### NORMALIZED CONTENT

#### CONTENT-LAYER: Visibility representation

299472293

#### CONTENT-COLUMN: Visibility representation

299472356

#### CONTENT-BLOCK: Visibility representation

299472355

A System context element is a virtual container that includes the entire system and its actors.

You can convert any Block to System Contextif you decide that the appropriate Block is decomposed. It may be called a system (i.e., Power Subsystem, Brake Subsystem, Lightening Subsystem).

[IMAGE alt='' src='']

#### NOTE: Visibility representation

Visibility representation

In SysML, properties and operations of the Block are public. Visibility representation literals, like +, #, ~, -, are not displayed in the Containment tree or in the element symbol on a diagram.

##### Converting a Block to System Context

To convert a Block to System Context

1. Right-click a Block.
2. Select Refactor > Convert To > More Specific > System Context . The Block is converted to System Context.

299472292

**Related pages**

- [CONFLUENCE_PAGE title='SysML Block Definition Diagram' space='MT']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="bad3b73e-8c4b-4f7d-bb73-283845098725"><ac:parameter ac:name="id">299472293</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="22094d10-8ce7-459c-ab93-94b3b03fe116"><ac:parameter ac:name="id">299472356</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="6a01ba1e-6af1-45da-be6a-72173d1b142f"><ac:parameter ac:name="id">299472355</ac:parameter><ac:rich-text-body><ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p>A System context element is a virtual container that includes the entire system and its actors.</p><p>You can convert any Block to System Context<span style="color: rgb(51,51,51);"> if you decide that the appropriate Block is decomposed. It may be called a system (i.e., Power Subsystem, Brake Subsystem, Lightening Subsystem).</span></p><p><ac:image ac:title="System Context" ac:alt="System Context" ac:height="250"><ri:attachment ri:filename="system_context.png" /></ac:image></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="45e244e1-7a14-47d4-88f2-ec499c585171"><ac:parameter ac:name="title">Visibility representation</ac:parameter><ac:rich-text-body><p><span style="color: rgb(62,63,64);"><span style="color: rgb(62,63,64);">In SysML, properties and operations of the Block are public. Visibility representation literals, like +, #, ~, -, are not displayed in the Containment tree or in the element symbol on a diagram.</span><br /></span></p></ac:rich-text-body></ac:structured-macro></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><h3>Converting a Block to System Context</h3><p>To convert a Block to System Context</p><hr /><ol><li>Right-click a Block.</li><li>Select <strong>Refactor</strong> &gt; <strong>Convert To</strong> &gt; <strong>More Specific</strong> &gt; <strong>System Context</strong>.<br />The Block is converted to System Context.</li></ol></ac:layout-cell></ac:layout-section></ac:layout></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="51f72765-eb9e-484d-a148-644608de25d4"><ac:parameter ac:name="id">299472292</ac:parameter><ac:rich-text-body><p class="auto-cursor-target"><strong>Related pages</strong></p><ul><li><ac:link><ri:page ri:space-key="MT" ri:content-title="SysML Block Definition Diagram" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=228986124 space=MED version=3 -->
## PAGE 00470: System in UAF

- page_id: `228986124`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/228986124/System+in+UAF
- version_number: 3
- version_date: `2025-08-14T15:07:47.605+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UAF 1.3 elements
- labels: []

### NORMALIZED CONTENT

**Description**

An integrated set of elements, subsystems, or assemblies that accomplish a defined objective. These elements include products (hardware, software, firmware), processes, people, information, techniques, facilities, services, and other support elements.

**Architecture** **Framework**

UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0

**Extension**

UML Class

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="OMGNormalParagraph"><strong>Description</strong></p><p>An integrated set of elements, subsystems, or assemblies that accomplish a defined objective. These elements include products (hardware, software, firmware), processes, people, information, techniques, facilities, services, and other support elements.</p><p><strong>Architecture</strong> <strong>Framework</strong></p><p><span style="color:var(--ds-text,#333333);">UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0</span></p><p><strong>Extension</strong></p><p>UML Class</p><p><br /></p>
````

<!--NOMAGIC_PAGE id=243968014 space=MED version=1 -->
## PAGE 00471: Tag

- page_id: `243968014`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/243968014/Tag
- version_number: 1
- version_date: `2025-07-31T10:50:47.846+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UML elements
- labels: []

### NORMALIZED CONTENT

Just like a class, a [CONFLUENCE_PAGE title='Stereotype' space='']can have properties, which can be referred to as tag definitions. When a [CONFLUENCE_PAGE title='Stereotype' space='']is applied to a model element, the values of the properties may be referred to as tagged values.

The tag definitions are used to define new meta attributes of the extended metaclass, they are used as regular class attributes.

An actual instance of the tag definition is a tagged value (tag).

A tag holds extra information like:

- additional information that does not come with UML, for example Precondition for Use Cases.
- management data about the state and progress of the project such as author, status, and tested.
- language specific data for code generation tools.

A tagged value consists of two parts: name and value (example: Author = Joe).

To create a new tag definition

1. Create a new stereotype.
2. Open the stereotype [CONFLUENCE_PAGE title='Specification window' space='MT'] .
3. In the Tag Definitions property group, click the Create button to add a new tag definition for stereotype.
4. Select the type of this property. Type of the property can be a standard UML data type or another user defined Stereotype. Regular classes should not be used as types of tag definition.

#### PANEL: Related References

Related References

#### PANEL: Related Pages

Related Pages

- [CONFLUENCE_PAGE title='UML elements' space='']
- [CONFLUENCE_PAGE title='Stereotype' space='']
- [CONFLUENCE_PAGE title='State Machine diagram' space='MT']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p>Just like a class, a <ac:link><ri:page ri:content-title="Stereotype" /><ac:plain-text-link-body><![CDATA[stereotype ]]></ac:plain-text-link-body></ac:link>can have properties, which can be referred to as tag definitions. When a <ac:link><ri:page ri:content-title="Stereotype" /><ac:plain-text-link-body><![CDATA[stereotype ]]></ac:plain-text-link-body></ac:link>is applied to a model element, the values of the properties may be referred to as tagged values.</p><p>The tag definitions are used to define new meta attributes of the extended metaclass, they are used as regular class attributes.</p><p>An actual instance of the tag definition is a tagged value (tag).</p><p>A tag holds extra information like:</p><ul><li>additional information that does not come with UML, for example Precondition for Use Cases.</li><li>management data about the state and progress of the project such as author, status, and tested. </li><li>language specific data for code generation tools. </li></ul><p>A tagged value consists of two parts: name and value (example: Author = Joe).</p><p> </p><p>To create a new tag definition</p><hr /><ol><li>Create a new stereotype.</li><li>Open the stereotype <ac:link><ri:page ri:space-key="MT" ri:content-title="Specification window" /></ac:link>.</li><li>In the <strong>Tag Definitions</strong> property group, click the <strong>Create</strong> button to add a new tag definition for stereotype. </li><li><p>Select the type of this property.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="1cde4e12-306c-4688-a2f5-12d58006edfb"><ac:rich-text-body><p>Type of the property can be a standard UML data type or another user defined Stereotype. Regular classes should not be used as types of tag definition.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></li></ol></ac:layout-cell><ac:layout-cell><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="13997e49-fd54-4bdc-89bf-a875a74da3e4"><ac:parameter ac:name="title">Related References</ac:parameter><ac:rich-text-body><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="5b6b0a1e-01ad-40af-8c1e-964b2fc4fd0b" /></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="a1cb6614-da6a-4a7b-adf1-3ec18e11a18c"><ac:parameter ac:name="title">Related Pages</ac:parameter><ac:rich-text-body><ul><li><ac:link><ri:page ri:content-title="UML elements" /><ac:plain-text-link-body><![CDATA[Model Elements]]></ac:plain-text-link-body></ac:link></li><li><ac:link><ri:page ri:content-title="Stereotype" /></ac:link></li><li><ac:link><ri:page ri:space-key="MT" ri:content-title="State Machine diagram" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro><p> </p><p> </p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="two_equal"><ac:layout-cell><p> </p></ac:layout-cell><ac:layout-cell><p> </p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=228986125 space=MED version=2 -->
## PAGE 00472: Technology

- page_id: `228986125`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/228986125/Technology
- version_number: 2
- version_date: `2025-05-14T10:31:32.464+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UAF 1.3 elements
- labels: []

### NORMALIZED CONTENT

**Description**

A sub type of Resource Artifact that indicates a technology domain, i.e. nuclear, mechanical, electronic, mobile telephony etc.

**Architecture** **Framework**

UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0

**Extension**

UML Class

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="OMGNormalParagraph"><strong>Description</strong></p><p class="OMGNormalParagraph">A sub type of Resource Artifact that indicates a technology domain, i.e. nuclear, mechanical, electronic, mobile telephony etc. </p><p class="OMGNormalParagraph"><strong>Architecture</strong> <strong>Framework</strong></p><p class="OMGNormalParagraph"><span style="color: rgb(62,63,64);">UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0</span></p><p class="OMGNormalParagraph"><strong>Extension</strong></p><p class="OMGNormalParagraph">UML Class</p><p><br /></p>
````

<!--NOMAGIC_PAGE id=243968016 space=MED version=2 -->
## PAGE 00473: Template

- page_id: `243968016`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/243968016/Template
- version_number: 2
- version_date: `2025-09-13T12:44:16.882+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UML elements
- labels: []

### NORMALIZED CONTENT

#### CONTENT-LAYER: Working With Templates

502366679

#### CONTENT-COLUMN: Working With Templates

502366682

#### CONTENT-BLOCK: Working With Templates

502366680

Use a Template to define concrete types for elements without concrete types. You can create a template and then use it as many times as you need. Moreover, when you have elements of the same structure (or with the same parameters) but with different values, the template you use can easily define parameters for each element. You can apply template parametrization to classifiers, packages, and operations. Most often. template parametrization is used for classes and interfaces. Templates are often used in code engineering (Java and other programming languages).

The template consists of:

- A parameterized element (an element with defined template parameters). The parameterized element can also be called a template element.
- An actual element (an element for which a template is applied, an element with actual values). The actual element can also be called a templateable element.
- A template binding relationship (a relationship from the actual element to the parameterized element).
- A template parameter substitution (used to define actual parameters of the actual element that substitutes formal template parameters). Template parameter substitutions are created on the template binding relationship.

[IMAGE alt='' src='']

###### Example of Template

In this example, you can see the *GeneralArray*template class, which has the *ArraySize* and *ArrayType* template parameters, represented by the dashed rectangle in the upper-right corner of the class. These parameters represent the size and type of the general array.The attribute *GeneralArray::contents : ArrayType [0..ArraySize]* represents the *ArrayType* and the *ArraySize* template parameters. The *ArraySize* template parameter is of the Integer type, and its default value is 10. The *ArrayType* template parameter is of the Class type (it is not represented in the shape), and its default value is not specified. The default value of the template parameter is used if no actual value is supplied for the parameter in a binding. Typically, the parameter types are classifiers, but they can also be integers or other types.

The *GeneralArray* class and its template parameters create a template of the general array of undefined types. You can use this template in other concrete arrays as many times as you need.

How to use the template and how to create an actual element

To create an array of addresses, you would create the *AddressArray* class. Alone (without a template), the *AddressArray* class would have undefined types. A template binding is created from the *AddressArray* class to the *GeneralArray* class. Now the template binding connection points to the *GeneralArray* template class.

The template binding specifies template parameter substitutions, the actual values of parameters for the address array. In the example, we created the following actual values of the AdressArray class: the array size having the value 3 and the array of the *Address* type.

The output of these definitions results in the *AddressArray* class having the attribute *AddressArray::contents : Address [0..3]*.

Attributes for the actual element classes should be created manually. In the example, the*AddressArray::contents : Address [0..3]*attribute is not created automatically - you must create this attribute manually. Use these optional solutions to create these attributes in your model or not.

#### TIP: Working With Templates

Working With Templates

Step by step instructions for modelling a template in the modeling tool are described in [CONFLUENCE_PAGE title='Working with Template' space=''].

You can format template parameter symbol properties in the [CONFLUENCE_PAGE title='Formatting symbols' space='MT']**Symbol Properties** dialog.

You can specify template parameter properties in the Template Parameter [CONFLUENCE_PAGE title='Specification window' space='MT'] and template binding properties in the Template Binding Specification window. In the specification window, you can find the description of each property. Descriptions are presented in the description area of the Specification window.

502366678

**Related pages**

- Model elements
- Auxiliary Diagram Symbols
- Diagramming

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="714106c9-8378-4c57-9c16-191c0639bf6c"><ac:parameter ac:name="id">502366679</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="ae8ba79e-6ca6-4ac9-a364-25d0cefd136f"><ac:parameter ac:name="id">502366682</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="cf9775cd-ce52-4182-9c1e-6832c322d64d"><ac:parameter ac:name="id">502366680</ac:parameter><ac:rich-text-body><p>Use a Template to define concrete types for elements without concrete types. You can create a template and then use it as many times as you need. Moreover, when you have elements of the same structure (or with the same parameters) but with different values, the template you use can easily define parameters for each element. You can apply template parametrization to classifiers, packages, and operations. Most often. template parametrization is used for classes and interfaces. Templates are often used in code engineering (Java and other programming languages).</p><p>The template consists of:</p><ul><li>A parameterized element (an element with defined template parameters). The parameterized element can also be called a template element.</li><li>An actual element (an element for which a template is applied, an element with actual values). The actual element can also be called a templateable element.</li><li>A template binding relationship (a relationship from the actual element to the parameterized element).</li><li>A template parameter substitution (used to define actual parameters of the actual element that substitutes formal template parameters). Template parameter substitutions are created on the template binding relationship.</li></ul><p style="text-align: center;"><ac:image><ri:attachment ri:filename="template_example.png" /></ac:image></p><h6 style="text-align: center;">Example of Template</h6><p>In this example, you can see the <em>GeneralArray </em>template class, which has the <em>ArraySize</em> and <em>ArrayType</em> template parameters, represented by the dashed rectangle in the upper-right corner of the class. These parameters represent the size and type of the general array.The attribute <em>GeneralArray::contents : ArrayType [0..ArraySize]</em> represents the <em>ArrayType</em> and the <em>ArraySize</em> template parameters. The <em>ArraySize</em> template parameter is of the Integer type, and its default value is 10. The <em>ArrayType</em> template parameter is of the Class type (it is not represented in the shape), and its default value is not specified. The default value of the template parameter is used if no actual value is supplied for the parameter in a binding. Typically, the parameter types are classifiers, but they can also be integers or other types.</p><p>The <em>GeneralArray</em> class and its template parameters create a template of the general array of undefined types. You can use this template in other concrete arrays as many times as you need.</p><p><u>How to use the template and how to create an actual element</u></p><p>To create an array of addresses, you would create the <em>AddressArray</em> class. Alone (without a template), the <em>AddressArray</em> class would have undefined types. A template binding is created from the <em>AddressArray</em> class to the <em>GeneralArray</em> class. Now the template binding connection points to the <em>GeneralArray</em> template class.</p><p>The template binding specifies template parameter substitutions, the actual values of parameters for the address array. In the example, we created the following actual values of the AdressArray class: the array size having the value 3 and the array of the <em>Address</em> type.</p><p>The output of these definitions results in the <em>AddressArray</em> class having the attribute <em>AddressArray::contents : Address [0..3]</em>. </p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="d09d8263-e3ce-42d5-8809-3c30674fc9b6"><ac:rich-text-body><p><span>Attributes for the actual element classes should be created manually. In the example, the </span><em>AddressArray::contents : Address [0..3] </em><span>attribute is not created automatically - you must create this attribute manually. Use these optional solutions to create these attributes in your model or not. </span></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="abc8cd1a-cec0-4421-acda-39dc44cb9904"><ac:parameter ac:name="title">Working With Templates</ac:parameter><ac:rich-text-body><p>Step by step instructions for modelling a template in the modeling tool are described in <ac:link><ri:page ri:content-title="Working with Template" /><ac:plain-text-link-body><![CDATA[Working With Templates]]></ac:plain-text-link-body></ac:link>.</p></ac:rich-text-body></ac:structured-macro><p>You can format template parameter symbol properties in the <ac:link><ri:page ri:space-key="MT" ri:content-title="Formatting symbols" /><ac:link-body><strong>Symbol Properties</strong> dialog</ac:link-body></ac:link>.</p><p><span>You can specify template parameter properties in the Template Parameter <ac:link><ri:page ri:space-key="MT" ri:content-title="Specification window" /></ac:link> and template binding properties in the Template Binding Specification window. In the specification window, you can find the description of each property. Descriptions are presented in the description area of the Specification window.</span></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="f276abb8-02ea-4ad7-bcee-aa487fc86035"><ac:parameter ac:name="id">502366678</ac:parameter><ac:rich-text-body><p><strong>Related pages</strong></p><ul><li class="ancestor-link"><a href="https://docs.nomagic.com/display/MT/Model+elements">Model elements</a></li><li class="ancestor-link parent-link"><a href="https://docs.nomagic.com/display/MT/Auxiliary+diagram+symbols">Auxiliary Diagram Symbols</a></li><li><a href="https://docs.nomagic.com/display/MT/Diagramming">Diagramming</a></li></ul></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=228986126 space=MED version=2 -->
## PAGE 00474: Temporal Part

- page_id: `228986126`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/228986126/Temporal+Part
- version_number: 2
- version_date: `2025-05-14T10:31:32.828+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UAF 1.3 elements
- labels: []

### NORMALIZED CONTENT

**Description**

Usage of an Enterprise Phase in the context of another Enterprise Phase. It asserts that one Enterprise Phase is a spatial part of another. Creates a whole-part relationship that represents the temporal structure of the Enterprise Phase.

**Architecture Framework**

UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0

**Extension**

UML Property

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="OMGNormalParagraph"><strong>Description</strong></p><p class="OMGNormalParagraph">Usage of an Enterprise Phase in the context of another Enterprise Phase. It asserts that one Enterprise Phase is a spatial part of another. Creates a whole-part relationship that represents the temporal structure of the Enterprise Phase.</p><p class="OMGNormalParagraph"><strong><span class="fontstyle0">Architecture Framework</span></strong></p><p class="OMGNormalParagraph"><span style="color: rgb(62,63,64);">UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0</span></p><p><strong>Extension</strong></p><p>UML Property</p><p><br /></p>
````

<!--NOMAGIC_PAGE id=243967963 space=MED version=1 -->
## PAGE 00475: Terminate

- page_id: `243967963`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/243967963/Terminate
- version_number: 1
- version_date: `2025-07-31T10:50:46.293+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UML elements > State Machine > Pseudo States
- labels: []

### NORMALIZED CONTENT

Entering a terminate pseudo state implies that the execution of the state machine by means of its context object is terminated. The state machine does not exit any states nor does it perform any exit actions other than those associated with the transition leading to the terminate pseudo state.

#### PANEL: Related Pages

Related Pages

- [CONFLUENCE_PAGE title='UML elements' space='']
- [CONFLUENCE_PAGE title='Specification window' space='MT']

#### PANEL: Related pages

Related pages

[CONFLUENCE_PAGE title='Pseudo States' space='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p>Entering a terminate pseudo state implies that the execution of the state machine by means of its context object is terminated. The state machine does not exit any states nor does it perform any exit actions other than those associated with the transition leading to the terminate pseudo state.</p></ac:layout-cell><ac:layout-cell><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="36e20852-22dd-420b-8d4b-52b136b22981"><ac:parameter ac:name="title">Related Pages</ac:parameter><ac:rich-text-body><ul><li><ac:link><ri:page ri:content-title="UML elements" /><ac:plain-text-link-body><![CDATA[Model Elements]]></ac:plain-text-link-body></ac:link></li><li><ac:link><ri:page ri:space-key="MT" ri:content-title="Specification window" /><ac:plain-text-link-body><![CDATA[Specification Window]]></ac:plain-text-link-body></ac:link></li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="f01b84d9-d9d1-4049-8315-15a6a05d850d"><ac:parameter ac:name="title">Related pages</ac:parameter><ac:rich-text-body><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="9f0ee894-6ed5-4015-99e4-1d04e579755b"><ac:parameter ac:name="page"><ac:link><ri:page ri:content-title="Pseudo States" /></ac:link></ac:parameter></ac:structured-macro></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=249005179 space=MED version=2 -->
## PAGE 00476: Test Case

- page_id: `249005179`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/249005179/Test+Case
- version_number: 2
- version_date: `2025-08-18T17:38:55.743+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > Requirement-related elements
- labels: []

### NORMALIZED CONTENT

A Test Case (Activity / StateMachine / Interaction) is a method for verifying a requirement.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="auto-cursor-target">A Test Case (Activity / StateMachine / Interaction) is a method for verifying a requirement.</p>
````

<!--NOMAGIC_PAGE id=243967678 space=MED version=1 -->
## PAGE 00477: The formal gate and actual gate usage in the sequence diagram

- page_id: `243967678`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/243967678/The+formal+gate+and+actual+gate+usage+in+the+sequence+diagram
- version_number: 1
- version_date: `2025-07-31T10:50:38.853+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UML elements > Gate
- labels: []

### NORMALIZED CONTENT

See the following figure where the *getBalance* message is drawn from the diagram frame to the *theirBank* lifeline. The *getBalance* message has a gate.

[IMAGE alt='' src='']

See the following figure where the actual gate is presented. The Balance Lookup interaction use refers to the Balance Lookup sequence diagram. The *getBalance* message (see the 2nd message) has selected the formal gate and automatically repeats the data of the *getBalance* message from the Balance Lookup diagram.

[IMAGE alt='' src='']

#### PANEL: Related Pages

Related Pages

- [CONFLUENCE_PAGE title='UML elements' space='']
- [CONFLUENCE_PAGE title='Class diagram' space='MT']
- [CONFLUENCE_PAGE title='Use Case' space='']
- [CONFLUENCE_PAGE title='Use Case diagram' space='MT']
- [CONFLUENCE_PAGE title='Sequence diagram' space='MT']
- [CONFLUENCE_PAGE title='Activity diagram' space='MT']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p>See the following figure where the <em>getBalance</em> message is drawn from the diagram frame to the <em>theirBank</em> lifeline. The <em>getBalance</em> message has a gate.</p><p><ac:image ac:title="Formal gates usage in Sequence diagram" ac:alt="Formal gates usage in Sequence diagram"><ri:attachment ri:filename="gate1.png" /></ac:image></p><p>See the following figure where the actual gate is presented. The Balance Lookup interaction use refers to the Balance Lookup sequence diagram. The <em>getBalance</em> message (see the 2nd message) has selected the formal gate and automatically repeats the data of the <em>getBalance</em> message from the Balance Lookup diagram.</p><p><ac:image ac:title="Actual gates usage in sequence diagram" ac:alt="Actual gates usage in sequence diagram"><ri:attachment ri:filename="gate2.png" /></ac:image></p></ac:layout-cell><ac:layout-cell><p> </p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="1b2025c5-70c1-47b6-9a1b-4fb242548002"><ac:parameter ac:name="title">Related Pages</ac:parameter><ac:rich-text-body><ul><li><ac:link><ri:page ri:content-title="UML elements" /><ac:plain-text-link-body><![CDATA[Model Elements]]></ac:plain-text-link-body></ac:link></li><li><ac:link><ri:page ri:space-key="MT" ri:content-title="Class diagram" /><ac:plain-text-link-body><![CDATA[Class diagrams]]></ac:plain-text-link-body></ac:link></li><li><ac:link><ri:page ri:content-title="Use Case" /></ac:link></li><li><ac:link><ri:page ri:space-key="MT" ri:content-title="Use Case diagram" /></ac:link></li><li><ac:link><ri:page ri:space-key="MT" ri:content-title="Sequence diagram" /></ac:link></li><li><ac:link><ri:page ri:space-key="MT" ri:content-title="Activity diagram" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="two_equal"><ac:layout-cell><p> </p></ac:layout-cell><ac:layout-cell><p> </p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=243968090 space=MED version=1 -->
## PAGE 00478: The Use Case scenario created with version 17.0.1 or earlier

- page_id: `243968090`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/243968090/The+Use+Case+scenario+created+with+version+17.0.1+or+earlier
- version_number: 1
- version_date: `2025-07-31T10:50:49.890+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UML elements > Use Case > Use Case Scenario sketch
- labels: []

### NORMALIZED CONTENT

880408184

880408186

880408185

Beginning with version 17.0.2 of the modeling tool, Use Case scenarios of projects created with earlier versions are stored in the **Use Case Scenario Obsolete**property group in the Use Case [CONFLUENCE_PAGE title='Specification window' space='MT'].

[IMAGE alt='' src='']

- To see the Use Case Scenario Obsolete property group, change the property display mode to Expert .
- The Use Case Scenario Obsolete property group is displayed only if the [CONFLUENCE_PAGE title='Use Case description profile' space=''] is loaded.

880408183

**Related pages**

- [CONFLUENCE_PAGE title='UML elements' space='']
- [CONFLUENCE_PAGE title='Transition' space='']
- [CONFLUENCE_PAGE title='State Machine diagram' space='MT']
- [CONFLUENCE_PAGE title='Activity diagram' space='MT']
- [CONFLUENCE_PAGE title='Sequence diagram' space='MT']
- [CONFLUENCE_PAGE title='Use Case diagram' space='MT']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="031983ed-6e1d-400d-b7b3-c881c7a8a52b"><ac:parameter ac:name="id">880408184</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="3144a562-897b-433e-9d91-1fee7c82d9c8"><ac:parameter ac:name="id">880408186</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="80f391ea-bac7-4d0e-bbec-d2f8f031d72b"><ac:parameter ac:name="id">880408185</ac:parameter><ac:rich-text-body><p>Beginning with version 17.0.2 of the modeling tool, Use Case scenarios of projects created with earlier versions are stored in the <strong>Use Case Scenario Obsolete </strong>property group in the Use Case <ac:link><ri:page ri:space-key="MT" ri:content-title="Specification window" /></ac:link>.</p><p><ac:image ac:title="Example of use case scenario obsolete" ac:alt="Example of use case scenario obsolete"><ri:attachment ri:filename="use_case_scenario_obsolete.png" /></ac:image></p><ac:structured-macro ac:name="warning" ac:schema-version="1" ac:macro-id="a140a788-8f16-4910-950c-f6224de828d5"><ac:rich-text-body><ul><li>To see the <strong style="line-height: 1.4285715;">Use Case Scenario Obsolete </strong>property group, change the property display mode to <strong style="line-height: 1.4285715;">Expert</strong>.</li><li>The <strong style="line-height: 1.4285715;">Use Case Scenario Obsolete </strong>property group is displayed only if the <ac:link><ri:page ri:content-title="Use Case description profile" /><ac:plain-text-link-body><![CDATA[Use Case Description Profile]]></ac:plain-text-link-body></ac:link> is loaded.</li></ul></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="b86c374e-a2cc-479d-be8e-1d1bef9463b6"><ac:parameter ac:name="id">880408183</ac:parameter><ac:rich-text-body><p><strong>Related pages</strong></p><ul><li><ac:link><ri:page ri:content-title="UML elements" /><ac:plain-text-link-body><![CDATA[Model Elements]]></ac:plain-text-link-body></ac:link></li><li><ac:link><ri:page ri:content-title="Transition" /></ac:link></li><li><ac:link><ri:page ri:space-key="MT" ri:content-title="State Machine diagram" /></ac:link></li><li><ac:link><ri:page ri:space-key="MT" ri:content-title="Activity diagram" /></ac:link></li><li><ac:link><ri:page ri:space-key="MT" ri:content-title="Sequence diagram" /></ac:link></li><li><ac:link><ri:page ri:space-key="MT" ri:content-title="Use Case diagram" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=249005180 space=MED version=2 -->
## PAGE 00479: Trace

- page_id: `249005180`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/249005180/Trace
- version_number: 2
- version_date: `2025-08-18T17:39:17.561+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > Requirement-related elements
- labels: []

### NORMALIZED CONTENT

A 'Trace' relationship is a dependency between a requirement and an arbitrary model element traced by this requirement.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="auto-cursor-target">A 'Trace' relationship is a dependency between a requirement and an arbitrary model element traced by this requirement.</p>
````

<!--NOMAGIC_PAGE id=243968028 space=MED version=1 -->
## PAGE 00480: Transition

- page_id: `243968028`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/243968028/Transition
- version_number: 1
- version_date: `2025-07-31T10:50:48.288+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UML elements
- labels: []

### NORMALIZED CONTENT

A transition is a directed relationship between a source vertex and a target vertex. It can be a part of a compound transition, which takes the state machine from one state configuration to another, representing the complete response of the state machine to an occurrence of an event of a particular type. The transition relationship is created between two states. The transition specifies event occurrences and guard conditions.

When these events occur and conditions are satisfied with the object in the source, state will perform the specified effect and will enter the target state. So, in the transition, the main subjects are as follows:

- Event trigger and its parameter
- Guard condition
- Effect

On a transition path the event trigger, guard condition, and effect has the following syntax: 
*< event name> (< parameter >) [<guard condition >] / <effect name>*

An example of the transition.

[IMAGE alt='' src='']

In the preceding example, the transition relationship is created from the Ringing state to the Connected state. The transition has the specified event - phone answered, and the specified effect - enable speech. When the phone answered event occurs, the Ringing state performs the speech effect, and then the Connected state is 
entered.

The event on the transition is specified as event of the concrete type. The event trigger is the event whose reception in the source state makes the transition eligible to fire. That is, the trigger is specified by the event. [CONFLUENCE_PAGE title='Event' space='']types are as follows:

- Any Receive Event
- Call Event
- Change Event
- Signal Event
- Time Event

• You can [CONFLUENCE_PAGE title='Assigning Event Type' space=''] in the Transition Specification window, or there is a quick way to assign an event type straight on the transition from the diagram pane. 
• The effect on the transition is specified as one of the [CONFLUENCE_PAGE title='Assigning Behavior Type' space='']. 
• You can format the transition symbol properties in the [CONFLUENCE_PAGE title='Symbol Properties dialog' space='MT'].

You can [CONFLUENCE_PAGE title='Editing property values' space='MT'] in the Transition [CONFLUENCE_PAGE title='Specification window' space='MT']. In the same window, you can find the description of each property. Descriptions are presented in the description area of the [CONFLUENCE_PAGE title='Specification window' space='MT'].

#### PANEL: Related pages

Related pages

true

#### PANEL: Related Pages

Related Pages

- [CONFLUENCE_PAGE title='UML elements' space='']
- [CONFLUENCE_PAGE title='Event' space='']
- [CONFLUENCE_PAGE title='State Machine diagram' space='MT']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p>A transition is a directed relationship between a source vertex and a target vertex. It can be a part of a compound transition, which takes the state machine from one state configuration to another, representing the complete response of the state machine to an occurrence of an event of a particular type. The transition relationship is created between two states. The transition specifies event occurrences and guard conditions.</p><p>When these events occur and conditions are satisfied with the object in the source, state will perform the specified effect and will enter the target state. So, in the transition, the main subjects are as follows:</p><ul><li>Event trigger and its parameter</li><li>Guard condition</li><li>Effect</li></ul><p>On a transition path the event trigger, guard condition, and effect has the following syntax: <br /><em>&lt; event name&gt; (&lt; parameter &gt;) [&lt;guard condition &gt;] / &lt;effect name&gt;</em></p><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="6f8dbb2b-7038-4657-8f2c-d6188aae14b6"><ac:rich-text-body><p>An example of the transition.</p><p><ac:image><ri:attachment ri:filename="transition.png" /></ac:image></p></ac:rich-text-body></ac:structured-macro><p> </p><p>In the preceding example, the transition relationship is created from the Ringing state to the Connected state. The transition has the specified event - phone answered, and the specified effect - enable speech. When the phone answered event occurs, the Ringing state performs the speech effect, and then the Connected state is <br />entered.</p><p>The event on the transition is specified as event of the concrete type. The event trigger is the event whose reception in the source state makes the transition eligible to fire. That is, the trigger is specified by the event. <ac:link><ri:page ri:content-title="Event" /><ac:plain-text-link-body><![CDATA[Event ]]></ac:plain-text-link-body></ac:link>types are as follows:</p><ul><li>Any Receive Event</li><li>Call Event</li><li>Change Event</li><li>Signal Event</li><li>Time Event</li></ul><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="9ccd54c3-c228-428e-9d86-e56cdf2c997b"><ac:rich-text-body><p>• You can <ac:link><ri:page ri:content-title="Assigning Event Type" /><ac:plain-text-link-body><![CDATA[assign an event type]]></ac:plain-text-link-body></ac:link> in the Transition Specification window, or there is a quick way to assign an event type straight on the transition from the diagram pane. <br />• The effect on the transition is specified as one of the <ac:link><ri:page ri:content-title="Assigning Behavior Type" /><ac:plain-text-link-body><![CDATA[behaviors types]]></ac:plain-text-link-body></ac:link>. <br />• You can format the transition symbol properties in the <ac:link><ri:page ri:space-key="MT" ri:content-title="Symbol Properties dialog" /></ac:link>.</p></ac:rich-text-body></ac:structured-macro><p>You can <ac:link><ri:page ri:space-key="MT" ri:content-title="Editing property values" /><ac:plain-text-link-body><![CDATA[specify transition properties]]></ac:plain-text-link-body></ac:link> in the Transition <ac:link><ri:page ri:space-key="MT" ri:content-title="Specification window" /></ac:link>. In the same window, you can find the description of each property. Descriptions are presented in the description area of the <ac:link><ri:page ri:space-key="MT" ri:content-title="Specification window" /></ac:link>.</p><p> </p></ac:layout-cell><ac:layout-cell><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="e99114da-0b61-4f6c-9bd5-f1072bf9c568"><ac:parameter ac:name="title">Related pages</ac:parameter><ac:rich-text-body><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="7c34deaf-cfb1-4973-ab56-9da678c4314d"><ac:parameter ac:name="all">true</ac:parameter></ac:structured-macro></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="a1cb6614-da6a-4a7b-adf1-3ec18e11a18c"><ac:parameter ac:name="title">Related Pages</ac:parameter><ac:rich-text-body><ul><li><ac:link><ri:page ri:content-title="UML elements" /><ac:plain-text-link-body><![CDATA[Model Elements]]></ac:plain-text-link-body></ac:link></li><li><ac:link><ri:page ri:content-title="Event" /></ac:link></li><li><ac:link><ri:page ri:space-key="MT" ri:content-title="State Machine diagram" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"> </p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=243968035 space=MED version=1 -->
## PAGE 00481: Trigger

- page_id: `243968035`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/243968035/Trigger
- version_number: 1
- version_date: `2025-07-31T10:50:48.609+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UML elements
- labels: []

### NORMALIZED CONTENT

A Trigger used in a [CONFLUENCE_PAGE title='State Machine' space=''] is an extension of the basic definition found within the behavioral and structural portions of the specification. A Trigger defines the types of events that can initiate a transition between states. An event is anything that can happen in a system, such as a signal sent by a [CONFLUENCE_PAGE title='Behavior' space=''], a call to a specific operation, reaching a point in time, or a change in values within the system.

[IMAGE alt='' src='']

To create theTrigger

- For a State element , in the State dialog box, click Add . The Trigger dialog box opens.
- For a Transition relationship , in the Transition dialog box, select the Trigger box, and click Add (note that the Trigger property is hidden by default). The Trigger dialog box opens.

[IMAGE alt='' src='']

Specify the Trigger element in the Trigger [CONFLUENCE_PAGE title='Specification window' space='MT']. 
 
In theTriggerdialog box, near theEventbox, click the **...** button and select existing or create new[CONFLUENCE_PAGE title='Event' space=''].

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>A Trigger used in a <ac:link><ri:page ri:content-title="State Machine" /></ac:link> is an extension of the basic definition found within the behavioral and structural portions of the specification. A Trigger defines the types of events that can initiate a transition between states. An event is anything that can happen in a system, such as a signal sent by a <ac:link><ri:page ri:content-title="Behavior" /></ac:link>, a call to a specific operation, reaching a point in time, or a change in values within the system.</p><p><ac:image><ri:attachment ri:filename="containment_tree_new_trigger_signal_event.png" /></ac:image></p><p><span style="color: rgb(0,0,0);"> To create the </span><span class="hcp1" style="color: rgb(0,0,0);">Trigger</span></p><hr /><ul><li class="kadov-p"><span class="hcp2">For a <a>State</a> element</span>, in the <span class="hcp1">State</span> dialog box, click <span class="hcp1">Add</span>. The <span class="hcp1">Trigger</span> dialog box opens.</li><li class="kadov-p"><span class="hcp2">For a Transition relationship</span>, in the <span class="hcp1">Transition</span> dialog box, select the <span class="hcp1">Trigger</span> box, and click <span class="hcp1">Add</span> (note that the Trigger property is hidden by default). The <span class="hcp1">Trigger</span> dialog box opens.</li></ul><p><ac:image><ri:attachment ri:filename="transition_trigger.png" /></ac:image></p><p><span style="color: rgb(0,0,0);"> Specify the Trigger element in the Trigger <ac:link><ri:page ri:space-key="MT" ri:content-title="Specification window" /></ac:link></span><span style="color: rgb(0,0,0);">.   </span><br /><span style="color: rgb(0,0,0);">  </span><br /><span style="color: rgb(0,0,0);">In the </span><span class="hcp1" style="color: rgb(0,0,0);">Trigger</span><span style="color: rgb(0,0,0);"> dialog box, near the </span><span class="hcp1" style="color: rgb(0,0,0);">Event</span><span style="color: rgb(0,0,0);"> box, click the <strong>...</strong> button and select existing or create new </span><ac:link><ri:page ri:content-title="Event" /></ac:link><span style="color: rgb(0,0,0);">.  </span></p>
````

<!--NOMAGIC_PAGE id=9919405 space=MED version=2 -->
## PAGE 00482: Trigger on Nested Port

- page_id: `9919405`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/9919405/Trigger+on+Nested+Port
- version_number: 2
- version_date: `2025-09-13T12:46:24.005+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > SysML v1 elements
- labels: []

### NORMALIZED CONTENT

A Trigger on Nested Port is a trigger that applies the «TriggerOnNestedPort» stereotype extending the UML’s Port property of the trigger to support nested ports.

#### PANEL: Related diagrams

Related diagrams

- [CONFLUENCE_PAGE title='SysML Activity Diagram' space='MT']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p>A Trigger on Nested Port is a trigger that applies the «TriggerOnNestedPort» stereotype extending the UML’s Port property of the trigger to support nested ports.</p></ac:layout-cell><ac:layout-cell><p> </p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p> </p></ac:layout-cell><ac:layout-cell><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="cce34faa-2f55-4678-b24f-7f27f024c038"><ac:parameter ac:name="title">Related diagrams</ac:parameter><ac:rich-text-body><ul><li><ac:link><ri:page ri:space-key="MT" ri:content-title="SysML Activity Diagram" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=228985870 space=MED version=2 -->
## PAGE 00483: UAF 1.3 elements

- page_id: `228985870`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/228985870/UAF+1.3+elements
- version_number: 2
- version_date: `2025-05-14T10:33:44.184+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions
- labels: []

### NORMALIZED CONTENT



### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="11e6abdb-348b-4922-8030-1452ecc983a1" /></p>
````

<!--NOMAGIC_PAGE id=228986127 space=MED version=2 -->
## PAGE 00484: UAF Element

- page_id: `228986127`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/228986127/UAF+Element
- version_number: 2
- version_date: `2025-05-14T10:31:33.165+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UAF 1.3 elements
- labels: []

### NORMALIZED CONTENT

**Description**

Abstract super type for all of the UAF elements. It provides a way for all of the UAF elements to have a common set of properties.

**Architecture** **Framework**

UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0

**Extension**

Element

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="OMGNormalParagraph"><strong>Description</strong></p><p class="OMGNormalParagraph">Abstract super type for all of the UAF elements. It provides a way for all of the UAF elements to have a common set of properties. </p><p class="OMGNormalParagraph"><strong>Architecture</strong> <strong>Framework</strong></p><p class="OMGNormalParagraph"><span style="color: rgb(62,63,64);">UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0</span></p><p class="OMGNormalParagraph"><strong>Extension</strong></p><p class="OMGNormalParagraph">Element</p><p><br /></p>
````

<!--NOMAGIC_PAGE id=243967461 space=MED version=2 -->
## PAGE 00485: UML elements

- page_id: `243967461`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/243967461/UML+elements
- version_number: 2
- version_date: `2025-08-18T16:44:45.784+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions
- labels: []

### NORMALIZED CONTENT

Our modeling tools fully support the latest UML standard elements. The following pages provide in-depth definitions for each model element used in creating your projects:

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>Our modeling tools fully support the latest UML standard elements. The following pages provide in-depth definitions for each model element used in creating your projects:</p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="f43a9ccc-54ac-444b-98cf-0986eda0f474" /></p>
````

<!--NOMAGIC_PAGE id=17684239 space=MED version=10 -->
## PAGE 00486: Unit

- page_id: `17684239`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/17684239/Unit
- version_number: 10
- version_date: `2025-09-13T12:46:29.005+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > SysML v1 elements
- labels: []

### NORMALIZED CONTENT

157370466

157370468

157370467

INLINE

A Unit represents a standard unit of measure. For example,metre, kilometre, or foot are units of length.Units are used to specify [CONFLUENCE_PAGE title='Value Property' space=''].

157370465

**Related pages**

- [CONFLUENCE_PAGE title='Using Units' space='MT']
- [CONFLUENCE_PAGE title='Customizing Units' space='MT']
- [CONFLUENCE_PAGE title='SysML Block Definition Diagram' space='MT']
- [CONFLUENCE_PAGE title='SysML Internal Block Diagram' space='MT']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="9c98f2a1-b1e4-48fd-bbdb-c92464d2372b"><ac:parameter ac:name="id">157370466</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="81403bac-9c0c-45dc-b2a9-0f1c79584dae"><ac:parameter ac:name="id">157370468</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="d3dfc876-fbcd-43f3-868b-db982ea4642c"><ac:parameter ac:name="id">157370467</ac:parameter><ac:rich-text-body><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="excerpt" ac:schema-version="1" ac:macro-id="4c13a79e-137d-4cbb-ac28-046b2596cc3e"><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><p>A Unit represents a standard <span>unit of measure. For example,<span> metre, kilometre, or foot are units of <span>length.<span> Units are used to specify <ac:link><ri:page ri:content-title="Value Property" /><ac:plain-text-link-body><![CDATA[Value Properties]]></ac:plain-text-link-body></ac:link>.</span></span></span></span></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><p><br /></p><p class="auto-cursor-target"><br /></p><p><br /></p><p class="auto-cursor-target"><br /></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="9fbb91ea-8e6d-4bd4-a3e9-b15f808754d7"><ac:parameter ac:name="id">157370465</ac:parameter><ac:rich-text-body><p class="auto-cursor-target"><strong>Related pages</strong></p><ul><li><ac:link><ri:page ri:space-key="MT" ri:content-title="Using Units" /></ac:link></li><li><ac:link><ri:page ri:space-key="MT" ri:content-title="Customizing Units" /></ac:link></li><li><ac:link><ri:page ri:space-key="MT" ri:content-title="SysML Block Definition Diagram" /></ac:link></li><li><ac:link><ri:page ri:space-key="MT" ri:content-title="SysML Internal Block Diagram" /></ac:link></li></ul><p class="auto-cursor-target"><br /></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=249005173 space=MED version=2 -->
## PAGE 00487: Usability Requirement

- page_id: `249005173`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/249005173/Usability+Requirement
- version_number: 2
- version_date: `2025-08-18T17:37:26.746+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > Requirement-related elements
- labels: []

### NORMALIZED CONTENT

A Usability Requirement specifies the fitness for use of a system for its users and other actors.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="auto-cursor-target">A Usability Requirement specifies the fitness for use of a system for its users and other actors.</p>
````

<!--NOMAGIC_PAGE id=243968038 space=MED version=1 -->
## PAGE 00488: Use Case

- page_id: `243968038`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/243968038/Use+Case
- version_number: 1
- version_date: `2025-07-31T10:50:48.719+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UML elements
- labels: ['use-case', 'use-cases', 'rake-icon', 'actors']

### NORMALIZED CONTENT

19622935

19622937

19622936

INLINE

Use Cases are a means of specifying the required usages of a system. Typically, they are used to capture the requirements of a system, that is, what a system is supposed to do.

In the following figure you can see a fragment of the Library System. The Use Case *Register Return* is associated to the Actor *Librarian*, which means that this Actor initiates that Use Case.

[IMAGE alt='' src='']

Behavior of a Use Case can be specified by an Activity, State Machine, or Sequence. It can also be described by a textual description - a Use Case scenario that can be depicted in an Activity diagram.

A Use Case can be specified by changing its property values in the Use Case [CONFLUENCE_PAGE title='Swimlanes' space='']. Each property is described in the description area on this window.

##### Use Case relationships

A Use Case can be associated with an Actor to specify that the Actor initiates the associated Use Case.

A Use Case can be related to other Use Cases by

- Generalization
- Include
- Extend

##### Use Case shape with rake icon

The rake icon [IMAGE alt='' src=''] is displayed on the shape, if the Use Case is realized by other behavior diagrams, such as Use Case, Activity, State Machine, or Sequence. To hide the rake icon you need to set the **Show Rake Icon** property value to *false* in the **Symbol Property** dialog.

##### Use Case Actors

An Actor can be related to the Use Case by Association.

You can see the Actors that are related to the selected Use Case in [CONFLUENCE_PAGE title='Specification window' space='MT'] of that Use Case, the Actors property group. This group displays a list of Actors that are directly (through the Association relationship) or indirectly (through the Extend, Include, or Generalization relationships) connected to the selected Use Case.

19622934

**Related pages**

- [CONFLUENCE_PAGE title='UML elements' space='']
- [CONFLUENCE_PAGE title='Transition' space='']
- [CONFLUENCE_PAGE title='State Machine diagram' space='MT']
- [CONFLUENCE_PAGE title='Activity diagram' space='MT']
- [CONFLUENCE_PAGE title='Sequence diagram' space='MT']
- [CONFLUENCE_PAGE title='Use Case diagram' space='MT']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="02242262-7518-4e6c-ba62-76139ed4b033"><ac:parameter ac:name="id">19622935</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="4481b73d-b049-485d-a428-059863e328bf"><ac:parameter ac:name="id">19622937</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="bff1fa7d-e6ed-414b-862e-f02d4a9efaa6"><ac:parameter ac:name="id">19622936</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="excerpt" ac:schema-version="1" ac:macro-id="f2fd40bf-7a2d-43b5-abd6-6551e2bfa580"><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><p>Use Cases are a means of specifying the required usages of a system. Typically, they are used to capture the requirements of a system, that is, what a system is supposed to do.</p><p>In the following figure you can see a fragment of the Library System. The Use Case <em>Register Return</em> is associated to the Actor <em>Librarian</em>, which means that this Actor initiates that Use Case.</p><p><ac:image ac:title="Actor and Use Case" ac:alt="Actor and Use Case"><ri:attachment ri:filename="use_case.png" /></ac:image></p><p>Behavior of a Use Case can be specified by an Activity, State Machine, or Sequence. It can also be described by a textual description - a Use Case scenario that can be depicted in an Activity diagram.</p><p>A Use Case can be specified by changing its property values in the Use Case <ac:link><ri:page ri:content-title="Swimlanes" /><ac:plain-text-link-body><![CDATA[Specification window]]></ac:plain-text-link-body></ac:link>. Each property is described in the description area on this window.</p><h3>Use Case relationships</h3><p>A Use Case can be associated with an Actor to specify that the Actor initiates the associated Use Case.</p><p>A Use Case can be related to other Use Cases by</p><ul><li>Generalization</li><li>Include</li><li>Extend<span style="color: rgb(255,0,0);"> </span></li></ul><h3>Use Case shape with rake icon</h3><p>The rake icon <ac:image><ri:attachment ri:filename="rake.png" /></ac:image> is displayed on the shape, if the Use Case is realized by other behavior diagrams, such as Use Case, Activity, State Machine, or Sequence. To hide the rake icon you need to set the <strong>Show Rake Icon</strong> property value to <em>false</em> in the <strong>Symbol Property</strong> dialog.</p><h3><span style="color: rgb(0,0,0);">Use Case Actors</span></h3><p>An Actor can be related to the Use Case by Association.</p><p>You can see the Actors that are related to the selected Use Case in <ac:link><ri:page ri:space-key="MT" ri:content-title="Specification window" /></ac:link> of that Use Case, the <span class="confluence-link">Actors property group</span>. This group displays a list of Actors that are directly (through the Association relationship) or indirectly (through the Extend, Include, or Generalization relationships) connected to the selected Use Case.</p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="a9045261-6e18-46d7-bbeb-e5df5e31fe1e"><ac:parameter ac:name="id">19622934</ac:parameter><ac:rich-text-body><p><strong>Related pages</strong></p><ul><li><ac:link><ri:page ri:content-title="UML elements" /><ac:plain-text-link-body><![CDATA[Model Elements]]></ac:plain-text-link-body></ac:link></li><li><ac:link><ri:page ri:content-title="Transition" /></ac:link></li><li><ac:link><ri:page ri:space-key="MT" ri:content-title="State Machine diagram" /></ac:link></li><li><ac:link><ri:page ri:space-key="MT" ri:content-title="Activity diagram" /></ac:link></li><li><ac:link><ri:page ri:space-key="MT" ri:content-title="Sequence diagram" /></ac:link></li><li><ac:link><ri:page ri:space-key="MT" ri:content-title="Use Case diagram" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=243968048 space=MED version=1 -->
## PAGE 00489: Use Case description profile

- page_id: `243968048`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/243968048/Use+Case+description+profile
- version_number: 1
- version_date: `2025-07-31T10:50:48.938+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UML elements > Use Case
- labels: []

### NORMALIZED CONTENT

21188256

21188259

21188258

INLINE

You can extend the Use Case description with additional Use Case properties, such as Use Case ID, Author, Date, Use Case Complexity, Pre Condition, and others.

To extend the Use Case with additional properties, you must load the Use Case Description Profile manually; in a new project, it is not loaded by default.

To load the Use Case Description Profile

1. Open the Use Case [CONFLUENCE_PAGE title='Specification window' space='MT'] .
2. Click the **Load Profile**button. The Use Case Description Profile is loaded and additional properties are added to the Use Case.

*[IMAGE alt='' src='']*

After the Use Case Description Profile is loaded, the following additional properties appear in the Use Case [CONFLUENCE_PAGE title='Specification window' space='MT']:

- The Use Case ID property in the UseCase general property group. This property is designed to number use cases to correspond to particular sequences.
- The **Use Case Description**property group. In this property group, you can specify properties describing the particular Use Case, such as an Author, Date, Goal, and other.
- The Use Case Scenarios Diagrams property group allows specifying diagrams for basic, alternative, and exceptional Use Case scenarios.
- The **Use Case Scenarios Flows**property group allows specifying flows for basic, alternative, and exceptional Use Case scenarios.

The following figure illustrates an example of the **Use Case** [CONFLUENCE_PAGE title='Specification window' space='MT'] after the Use Case Description Profile is loaded.

[IMAGE alt='' src='']

You can specify the Use Case extension properties in the Use Case [CONFLUENCE_PAGE title='Specification window' space='MT']. Descriptions of each property appear in the description area of the Specification window.

21188255

**Related pages**

[CONFLUENCE_PAGE title='Use Case' space='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="0f0fda88-a777-4766-b70d-9ff4955c72a4"><ac:parameter ac:name="id">21188256</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="b3865aa2-17cc-4703-88bf-a0f3b61b6950"><ac:parameter ac:name="id">21188259</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="9ea8eefa-a93b-4739-a83f-0067a105492a"><ac:parameter ac:name="id">21188258</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="excerpt" ac:schema-version="1" ac:macro-id="1610d0d4-4515-416d-81c5-e370fe84019f"><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><p>You can extend the Use Case description with additional Use Case properties, such as Use Case ID, Author, Date, Use Case Complexity, Pre Condition, and others.</p><p>To extend the Use Case with additional properties, you must load the Use Case Description Profile manually; in a new project, it is not loaded by default.</p><p><br /></p><p>To load the Use Case Description Profile</p><hr /><ol><li>Open the <strong>Use Case </strong> <ac:link><ri:page ri:space-key="MT" ri:content-title="Specification window" /></ac:link>.</li><li><p>Click the <strong>Load Profile </strong>button. The Use Case Description Profile is loaded and additional properties are added to the Use Case.</p></li></ol><p><em><ac:image><ri:attachment ri:filename="specification_of_register_return.png" /></ac:image> <br /></em></p><p>After the Use Case Description Profile is loaded, the following additional properties appear in the Use Case <ac:link><ri:page ri:space-key="MT" ri:content-title="Specification window" /></ac:link>:</p><ul><li>The <strong>Use Case ID </strong>property in the UseCase general property group. This property is designed to number use cases to correspond to particular sequences.</li><li><p>The <strong>Use Case Description </strong>property group. In this property group, you can specify properties describing the particular Use Case, such as an Author, Date, Goal, and other.</p></li><li>The <strong>Use Case Scenarios Diagrams </strong>property group allows specifying diagrams for basic, alternative, and exceptional Use Case scenarios.</li><li><p>The <strong>Use Case Scenarios Flows </strong>property group allows specifying flows for basic, alternative, and exceptional Use Case scenarios. </p></li></ul><p>The following figure illustrates an example of the <strong>Use Case </strong> <ac:link><ri:page ri:space-key="MT" ri:content-title="Specification window" /></ac:link> after the Use Case Description Profile is loaded.</p><p><ac:image><ri:attachment ri:filename="register_return_specification.png" /></ac:image></p><p>You can specify the Use Case extension properties in the Use Case <ac:link><ri:page ri:space-key="MT" ri:content-title="Specification window" /></ac:link>. Descriptions of each property appear in the description area of the Specification window.</p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="e16ee5f8-1a34-463f-9919-40965c6bb05a"><ac:parameter ac:name="id">21188255</ac:parameter><ac:rich-text-body><p><strong>Related pages</strong></p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="7cc04b90-f34f-4407-b03d-1401cec62e61"><ac:parameter ac:name="page"><ac:link><ri:page ri:content-title="Use Case" /></ac:link></ac:parameter></ac:structured-macro></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=243968054 space=MED version=2 -->
## PAGE 00490: Use Case Scenario sketch

- page_id: `243968054`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/243968054/Use+Case+Scenario+sketch
- version_number: 2
- version_date: `2025-09-08T17:32:19.437+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UML elements > Use Case
- labels: ['basic-flow', 'alternative-flow', 'exceptional-flow']

### NORMALIZED CONTENT

This functionality is available in the Standard, Professional, Architect, and Enterprise editions.

Use Case Scenario Sketch is designed for creating the very first Use Case Scenario. After the scenario is created, you may edit it directly in the Activity diagram.

With the help of the Use Case scenario editor, you can:

- Create, review, and edit steps of the Use Case scenario by using the convenient textual values editor.
- Automatically create an Activity diagram representing the textual Use Case scenario flow. This enables you to have the textual numbered action flow and its graphical representation.
- Create the Use Case scenario from the Activity diagram for the particular Use Case and automatically represent this action flow as textual information in the Use Case scenario.

[IMAGE alt='' src='']

###### The Use Case Scenario Sketch creating in the Specification window.

The following figure depicts the same scenario represented in the Activity diagram.

[IMAGE alt='' src='']

A Use Case scenario can have defined , , and flows.

##### **basic**Basic flow

A basic flow represents the sequence of basic steps or actions of the Use Case scenario. You can also add steps from included or extended use cases to the flow. Each basic flow step can have one or more alternative and exceptional paths. The two figures above depict the basic flow, consisting of four steps. Letters and numbers in the brackets next to the basic flow step indicate how many alternative conditions and exceptional types that particular step has. The letter A indicates alternatives flows; the letter E indicates exceptional flows.

In an Activity diagram, the basic flow is the main path down from the initial node to the final node.

****

##### **alternative**Alternative flow

An alternative flow is an alternative path of the basic flow. You can define an alternative flow from a particular step of the basic flow. The alternative flow is an alternative solution, performed after the defined condition is satisfied. The alternative flow contains steps that are executed if one or more conditions occur.

Thus, in the Use Case scenario, the alternative flow is specified by these two parameters: the alternative condition and the alternative flow steps.

The following figure shows the content of the **Alternative Flow**tab of the Use Case Scenario in the Use Case [CONFLUENCE_PAGE title='Specification window' space='MT'].

[IMAGE alt='' src='']

Here, the alternative flow is created for the second step of the basic flow — 2. *Get Loan Details*. The alternative flow has the condition named *2.1 Item is overdue*. The condition contains one alternative flow step named 2.1.1 *Penalize for overdue*.

In the Activity diagram, the alternative flow is created between the decision and merge nodes. The alternative condition is represented as a decision node; the name of the alternative condition in the Activity diagram is the name of the decision node. In the Activity diagram, the alternative flow steps are represented as Call Behavior actions.

The alternative flow representation is shown in the activity diagram in the following figure.

[IMAGE alt='' src='']

In the Activity diagram, you can read the alternative flow as follows: if the item is overdue, then penalize for overdue; if not, continue to the basic flow.

****

##### **exceptional**Exceptional flow

An exceptional flow is an exceptional path from the particular basic flow step, or it can be a quick solution for exit. The exceptional flow contains steps that are executed if something goes wrong, such as an input from the actor that the system cannot handle. An example of this would be if the user clicks the *Cancel*button in the opened dialog.

In the Use Case scenario, the exceptional flow is specified by two parameters: the exception type and the exceptional flow steps.

The type of the exception object indicates the nature of the exception. Any class could be assigned as a type of the exception.

The exceptional flow steps are performed as actions when the execution occurs. The exceptional flow steps are specified for the concrete type. Normally, there is one exceptional flow (in other words, one exception type) assigned for one basic flow step. There can be any number of exceptional flow steps specified for one exception type.

The following figure shows the content of the **Exceptional Flow**tab of the Use Case Scenario in the Use Case Specification window.

[IMAGE alt='' src='']

Here, the exception flow is created for the third step of the basic flow, 3. *Confirm Return*. The exceptional flow has the type named *3.1 Cancel*; that is, the *Cancel*class is assigned as the exception type.The type contains one exceptional flow step named 3.1.1 *Close Item Dialog.*

In the Activity diagram, the exceptional flow is connected using the Exception Handler relationship. The Exception Handler has the type specified, the same as the exception type, in our sample *Cancel*class. Exceptional flow steps in an activity diagram are represented as Call Behavior actions.

You can create a Use Case scenario in the Use Case Specification window using the **Use Case Scenario Sketch**property group, where you can specify the basic, alternative, and exceptional flows, as well as open the Activity diagram.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="59567f37-53a2-4129-be26-ca56159c8e69"><ac:rich-text-body><p>This functionality is available in the Standard, Professional, Architect, and Enterprise editions.</p></ac:rich-text-body></ac:structured-macro><p>Use Case Scenario Sketch is designed for creating the very first Use Case Scenario. After the scenario is created, you may edit it directly in the Activity diagram.</p><p>With the help of the Use Case scenario editor, you can:</p><ul><li data-uuid="8d1032f7-84ad-402b-ae90-0373dc5f6202">Create, review, and edit steps of the Use Case scenario by using the convenient textual values editor.</li><li data-uuid="1fcf1bb2-6cb4-4bf1-8b74-17c2e7efbad3">Automatically create an Activity diagram representing the textual Use Case scenario flow. This enables you to have the textual numbered action flow and its graphical representation.</li><li data-uuid="bc7e5248-2348-4aab-b92f-2d676b405131">Create the Use Case scenario from the Activity diagram for the particular Use Case and automatically represent this action flow as textual information in the Use Case scenario.</li></ul><p><ac:image ac:align="center"><ri:attachment ri:filename="browse_items_sketch.png" /></ac:image></p><h6 style="text-align: center;">The Use Case Scenario Sketch creating in the Specification window.</h6><p><br /></p><p>The following figure depicts the same scenario represented in the Activity diagram.</p><p><ac:image ac:align="center" ac:title="Example of activity diagram with basic, alternative, and exceptional flows" ac:alt="Example of activity diagram with basic, alternative, and exceptional flows"><ri:attachment ri:filename="Example_of_activity_diagram_with_basic_alternative_exceptional_flows.png" /></ac:image></p><p>A Use Case scenario can have defined <ac:link ac:anchor="basic" />, <ac:link ac:anchor="alternative" />, and <ac:link ac:anchor="exceptional" /> flows. </p><h3><strong><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="a0d60a62-0e27-4bbc-ab88-a36369ec8ef0"><ac:parameter ac:name="">basic</ac:parameter></ac:structured-macro></strong>Basic flow</h3><p>A basic flow represents the sequence of basic steps or actions of the Use Case scenario. You can also add steps from included or extended use cases to the flow. Each basic flow step can have one or more alternative and exceptional paths. The two figures above depict the basic flow, consisting of four steps. Letters and numbers in the brackets next to the basic flow step indicate how many alternative conditions and exceptional types that particular step has. The letter A indicates alternatives flows; the letter E indicates exceptional flows.</p><p>In an Activity diagram, the basic flow is the main path down from the initial node to the final node.</p><p><strong> </strong></p><h3><strong><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="0b3ddcb2-c34b-4049-b82c-47c722ba0b3a"><ac:parameter ac:name="">alternative</ac:parameter></ac:structured-macro></strong>Alternative flow</h3><p>An alternative flow is an alternative path of the basic flow. You can define an alternative flow from a particular step of the basic flow. The alternative flow is an alternative solution, performed after the defined condition is satisfied. The alternative flow contains steps that are executed if one or more conditions occur.</p><p>Thus, in the Use Case scenario, the alternative flow is specified by these two parameters: the alternative condition and the alternative flow steps.</p><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="41fbe33a-1826-404f-8b8e-20bede770708"><ac:rich-text-body><p>The following figure shows the content of the <strong>Alternative Flow </strong>tab of the Use Case Scenario in the Use Case <ac:link><ri:page ri:space-key="MT" ri:content-title="Specification window" /></ac:link>.</p><p><ac:image ac:title="Alternative flow in the Specification window" ac:alt="Alternative flow in the Specification window"><ri:attachment ri:filename="Alternative_flow.png" /></ac:image></p><p>Here, the alternative flow is created for the second step of the basic flow — 2. <em>Get Loan Details</em>. The alternative flow has the condition named <em>2.1 Item is overdue</em>. The condition contains one alternative flow step named 2.1.1 <em>Penalize for overdue</em>.</p></ac:rich-text-body></ac:structured-macro><p>In the Activity diagram, the alternative flow is created between the decision and merge nodes. The alternative condition is represented as a decision node; the name of the alternative condition in the Activity diagram is the name of the decision node. In the Activity diagram, the alternative flow steps are represented as Call Behavior actions.</p><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="de58e7f6-c670-412d-990e-e6f61f53c747"><ac:rich-text-body><p>The alternative flow representation is shown in the activity diagram in the following figure.</p><p><ac:image><ri:attachment ri:filename="alternative_flow_in_activity_diagram.png" /></ac:image></p><p>In the Activity diagram, you can read the alternative flow as follows: if the item is overdue, then penalize for overdue; if not, continue to the basic flow.</p></ac:rich-text-body></ac:structured-macro><p><strong> </strong></p><h3><strong><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="a003f981-a8b1-43bc-a563-85a1d04d6240"><ac:parameter ac:name="">exceptional</ac:parameter></ac:structured-macro></strong>Exceptional flow</h3><p>An exceptional flow is an exceptional path from the particular basic flow step, or it can be a quick solution for exit. The exceptional flow contains steps that are executed if something goes wrong, such as an input from the actor that the system cannot handle. An example of this would be if the user clicks the <em>Cancel </em>button in the opened dialog.</p><p>In the Use Case scenario, the exceptional flow is specified by two parameters: the exception type and the exceptional flow steps.</p><p>The type of the exception object indicates the nature of the exception. Any class could be assigned as a type of the exception.</p><p>The exceptional flow steps are performed as actions when the execution occurs. The exceptional flow steps are specified for the concrete type. Normally, there is one exceptional flow (in other words, one exception type) assigned for one basic flow step. There can be any number of exceptional flow steps specified for one exception type.</p><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="9575b0a9-37e9-48dd-847a-717f585e4cfe"><ac:rich-text-body><p>The following figure shows the content of the <strong>Exceptional Flow </strong>tab of the Use Case Scenario in the Use Case Specification window.</p><p><ac:image ac:title="Exceptional flow in Specification window" ac:alt="Exceptional flow in Specification window"><ri:attachment ri:filename="Exceptional_flow.png" /></ac:image></p><p>Here, the exception flow is created for the third step of the basic flow, 3. <em>Confirm Return</em>. The exceptional flow has the type named <em>3.1 Cancel</em>; that is, the <em>Cancel </em>class is assigned as the exception type.The type contains one exceptional flow step named 3.1.1 <em>Close Item Dialog.</em></p></ac:rich-text-body></ac:structured-macro><p>In the Activity diagram, the exceptional flow is connected using the Exception Handler relationship. The Exception Handler has the type specified, the same as the exception type, in our sample <em>Cancel </em>class. Exceptional flow steps in an activity diagram are represented as Call Behavior actions.</p><p>You can create a Use Case scenario in the Use Case Specification window using the <strong>Use Case Scenario Sketch </strong>property group, where you can specify the basic, alternative, and exceptional flows, as well as open the Activity diagram.</p>
````

<!--NOMAGIC_PAGE id=9919456 space=MED version=2 -->
## PAGE 00491: User System

- page_id: `9919456`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/9919456/User+System
- version_number: 2
- version_date: `2025-09-13T12:46:25.023+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > SysML v1 elements
- labels: []

### NORMALIZED CONTENT

An User System is a special external system that serves as medium between a user and the system without having its own interests in the communication.

#### TIP: Example

Example

- Input Device or Display.

#### PANEL: Related diagrams

Related diagrams

- [CONFLUENCE_PAGE title='SysML Use Case Diagram' space='MT']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p>An User System is a special external system that serves as medium between a user and the system without having its own interests in the communication.</p><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="2c988ad5-b38e-44fa-abdb-c86af35e9056"><ac:parameter ac:name="title">Example</ac:parameter><ac:rich-text-body><ul><li>Input Device or Display.</li></ul></ac:rich-text-body></ac:structured-macro></ac:layout-cell><ac:layout-cell><p> </p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p> </p></ac:layout-cell><ac:layout-cell><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="de9adc89-d387-43d7-a667-124571a795a9"><ac:parameter ac:name="title">Related diagrams</ac:parameter><ac:rich-text-body><ul><li><ac:link><ri:page ri:space-key="MT" ri:content-title="SysML Use Case Diagram" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=243967936 space=MED version=3 -->
## PAGE 00492: Using smart packages in your model

- page_id: `243967936`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/243967936/Using+smart+packages+in+your+model
- version_number: 3
- version_date: `2025-09-13T12:44:14.061+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UML elements > Smart Package
- labels: []

### NORMALIZED CONTENT

1701234985

1701234988

1701234987

To better understand the usability of the smart packages, please see the following case studies.

##### Case study #1: Gathering use cases

The case study uses the sample project *use case diagram.mdzip*, which can be found in*<modeling tool installation folder>\samples\diagrams*.

For example, we have a lot of use cases owned by different system boundaries in the project.

We need all these use cases to be in a single package, except for several particular ones. Also, we need all newly created use cases to be automatically included in this package.

In this case, the smart packages feature is very useful. We will create a smart package with dynamic contents to gather all use cases in the model, then demonstrate how it manages further changes in the model. Finally, we will create a snapshot of the smart package to have a static list of use cases as a milestone of the model development.

To accomplish this, do the following:

1. Create a smart package named All Use Cases . [ATTACHMENT filename='smart_package_all_use_cases.png']
2. Define the criteria for gathering the contents of the smart package. Specify the search options to find all use case type elements from the root package Data . [ATTACHMENT filename='specify_search_options.png']
3. Expand the contents of the smart package All Use Cases . [ATTACHMENT filename='expand_contents_of_smart_package.png']
4. Exclude use cases Change password and Change system settings from the contents. See the contents of the smart package shortened.
5. Open the Specification window of the smart package and see the excluded use cases in the cell of the Excluded Elements property value. [ATTACHMENT filename='excluded_elements.png']
6. Drag use cases Change password and Change system settings to the smart package. See them in the contents of the smart package again.
7. Open the Specification window of the smart package again and see these manually included use cases in the cell of the Additional Elements property value. Elements excluded from the contents appear in it after being manually added. [ATTACHMENT filename='additional_elements.png']
8. Create a new use case named Filter by author under the system boundary Item Browser . See the new use case in the smart package All Use Cases . [ATTACHMENT filename='filter_by_author.png']
9. Create a snapshot of the smart package All Use Cases to have a static list of use cases as a milestone of the model development. [ATTACHMENT filename='snapshot_smart_package.png']
10. Expand the contents of the snapshot and see that it equals the contents of the smart package All Use Cases .

##### Case study #2: Performing the requirements coverage analysis

The case study uses the sample project *hybrid sport utility vehicle.mdzip*, which can be found in *<modeling tool installation folder>\samples\SysML v1*, if the SysML plugin is installed.

Here is another case where the smart package feature is very helpful: we need to have all unsatisfied requirements in a separate package. Also, we need requirements to automatically disappear from this package after becoming satisfied.

We will create a smart package with dynamic contents to gather all the unsatisfied requirements in the model and a dependency matrix for performing the requirements coverage analysis. Then we will demonstrate how both the smart package and the dependency matrix reflect the transition of a requirement to satisfy.

Let’s do the following:

1. Create a smart package named Unsatisfied Requirements .
2. To gather the contents of the smart package, add a new script operation (in the **Expert** mode of the **Query** dialog) and define the following OCL 2.0 expression as the criteria: select(r|not r.supplierDependency->exists(d|d.oclIsKindOf(SysML::Satisfy)))]]> [IMAGE alt='' src='']
3. Expand the contents of the smart package Unsatisfied Requirements . [ATTACHMENT filename='smart_package_unsatisfied_requirements.png']
4. Create a dependency matrix and define the following criteria:
  - Specify Requirement as the row element type
  - Specify Block as the column element type
  - Specify the smart package Unsatisfied Requirements as the row scope
  - Specify the package HSUV Structure as the column scope
  - Specify the Satisfy relationship as dependency criteria
  - In the Direction drop-down list, select Column to row. 
[IMAGE alt='' src='']
5. On the dependency matrix, create a Satisfy relationship between the block BrakePedal and the requirement Braking . [ATTACHMENT filename='SP_create_satisfy.png'] The requirement becomes satisfied and thus disappears from the contents of the smart package Unsatisfied Requirements and from the dependency matrix as well.

##### Case Study #3: Configuration management of the complex system - creating dynamic configuration catalogs

*The efficient configuration management process is a challenge in the evolution of any industrial scale product family. Smart packages are a real-life out of the box solution supporting the configuration management approach.*

Now study the case that illustrates the efficient management of complex system configurations with the help of smart packages. We have a library (static package) of system components, which we need to see in several different views of the model, that is, catalogs, according to their characteristics. Using the catalogs will not extend the scope of the model, since they do not require duplication of the elements. 
[IMAGE alt='' src='']

We will create two dynamic system configuration catalogs, that is, smart packages with dynamic contents, to gather the servers from the library *TI Hardware* according to the configuration version defined in a tag value of their specification.

Do the following:

1. Create two packages: TI12 Catalog and TI14 Catalog .
2. In each package, create a smart package named Servers . [ATTACHMENT filename='smart_package_servers.png']
3. Define criteria for gathering the contents of the smart package Servers in TI12 Catalog . Specify search options to find in the package TI Hardware , all block type elements with tag value Used In=TI12. [ATTACHMENT filename='search_smart_package_step3.png']
4. Define criteria for gathering the contents of the smart package Servers in TI14 Catalog. Specify search options to find in the package TI Hardware, all block type elements with tag value Used In=TI14 . [ATTACHMENT filename='search_smart_package_step4.png']
5. Expand the contents of both smart packages. 
[IMAGE alt='' src=''] The block *SUN FIRE T1000* appears in both *TI12 Catalog* and *TI14 Catalog*, since it has both tag values *Used In=TI12* and *Used In=TI14*.
6. Also, you can add a block to a smart package manually. Just drag the block to the smart package.

1701234982

**Related Pages**

- [CONFLUENCE_PAGE title='Specifying criteria for querying model' space='MT']
- Model Elements
- Stereotype
- Package
- Working with Profiles

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="796820fe-b554-43d7-b84d-600b50403ed1"><ac:parameter ac:name="id">1701234985</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="ce508ef7-9ad4-40f1-abe8-9df43271c026"><ac:parameter ac:name="id">1701234988</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="ceffc76e-5c43-4055-a30f-d9639cf452af"><ac:parameter ac:name="id">1701234987</ac:parameter><ac:rich-text-body><p>To better understand the usability of the smart packages, please see the following case studies.</p><h3>Case study #1: Gathering use cases</h3><p><br /></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="69dadb10-94ac-4152-b595-dc8e5553165d"><ac:rich-text-body><p>The case study uses the sample project <em>use case diagram.mdzip</em>, which can be found in<em> &lt;modeling tool installation folder&gt;\samples\diagrams</em>.</p></ac:rich-text-body></ac:structured-macro><p>For example, we have a lot of use cases owned by different system boundaries in the project.</p><p>We need all these use cases to be in a single package, except for several particular ones. Also, we need all newly created use cases to be automatically included in this package.</p><p>In this case, the smart packages feature is very useful. We will create a smart package with dynamic contents to gather all use cases in the model, then demonstrate how it manages further changes in the model. Finally, we will create a snapshot of the smart package to have a static list of use cases as a milestone of the model development.</p><p>To accomplish this, do the following:</p><ol><li>Create a smart package named <em>All Use Cases</em>.<br /><ac:image><ri:attachment ri:filename="smart_package_all_use_cases.png" /></ac:image></li><li>Define the criteria for gathering the contents of the smart package. Specify the search options to find all use case type elements from the root package <em>Data</em>.<br /><ac:image ac:height="175" ac:width="340"><ri:attachment ri:filename="specify_search_options.png" /></ac:image></li><li>Expand the contents of the smart package <em>All Use Cases</em>.<br /><ac:image><ri:attachment ri:filename="expand_contents_of_smart_package.png" /></ac:image></li><li>Exclude use cases <em>Change password</em> and <em>Change system settings</em> from the contents. See the contents of the smart package shortened.</li><li>Open the Specification window of the smart package and see the excluded use cases in the cell of the <strong>Excluded Elements</strong> property value.<br /><ac:image><ri:attachment ri:filename="excluded_elements.png" /></ac:image></li><li>Drag use cases <em>Change password</em> and <em>Change system settings</em> to the smart package. See them in the contents of the smart package again.</li><li>Open the Specification window of the smart package again and see these manually included use cases in the cell of the <strong>Additional Elements</strong> property value. Elements excluded from the contents appear in it after being manually added.<br /><ac:image><ri:attachment ri:filename="additional_elements.png" /></ac:image></li><li>Create a new use case named <em>Filter</em> <em>by author</em> under the system boundary<em> Item Browser</em>. See the new use case in the smart package <em>All Use Cases</em>.<br /><ac:image><ri:attachment ri:filename="filter_by_author.png" /></ac:image></li><li>Create a snapshot of the smart package <em>All Use Cases</em> to have a static list of use cases as a milestone of the model development.<br /><ac:image><ri:attachment ri:filename="snapshot_smart_package.png" /></ac:image></li><li>Expand the contents of the snapshot and see that it equals the contents of the smart package <em>All Use Cases</em>.</li></ol><h3>Case study #2: Performing the requirements coverage analysis</h3><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="379e59dc-a2ea-4122-b14b-8d486ebd70d0"><ac:rich-text-body><p>The case study uses the sample project <em>hybrid sport utility vehicle.mdzip</em>, which can be found in <em>&lt;modeling tool installation folder&gt;\samples\SysML v1</em>, if the SysML plugin is installed.</p></ac:rich-text-body></ac:structured-macro><p>Here is another case where the smart package feature is very helpful: we need to have all unsatisfied requirements in a separate package. Also, we need requirements to automatically disappear from this package after becoming satisfied.</p><p>We will create a smart package with dynamic contents to gather all the unsatisfied requirements in the model and a dependency matrix for performing the requirements coverage analysis. Then we will demonstrate how both the smart package and the dependency matrix reflect the transition of a requirement to satisfy.</p><p>Let’s do the following:</p><ol><li>Create a smart package named <em>Unsatisfied Requirements</em>.</li><li><p>To gather the contents of the smart package, add a new script operation (in the <strong>Expert</strong> mode of the <strong>Query</strong> dialog) and define the following OCL 2.0 expression as the criteria:</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="ee5655e3-7fc5-4541-acfe-620580602288"><ac:plain-text-body><![CDATA[SysML::Requirements::Requirement::allInstances()->select(r|not r.supplierDependency->exists(d|d.oclIsKindOf(SysML::Satisfy)))]]></ac:plain-text-body></ac:structured-macro><p><ac:image><ri:attachment ri:filename="ocl_expression.png" /></ac:image></p></li><li>Expand the contents of the smart package <em>Unsatisfied Requirements</em>.<br /><ac:image><ri:attachment ri:filename="smart_package_unsatisfied_requirements.png" /></ac:image></li><li>Create a dependency matrix and define the following criteria:<br /><ul><li>Specify Requirement as the row element type</li><li>Specify Block as the column element type</li><li>Specify the smart package <em>Unsatisfied Requirements</em> as the row scope</li><li>Specify the package <em>HSUV Structure</em> as the column scope</li><li>Specify the Satisfy relationship as dependency criteria</li><li>In the <strong>Direction</strong> drop-down list, select <strong>Column to row.<br /><ac:image><ri:attachment ri:filename="specify_smart_package_criteria.png" /></ac:image><br /></strong></li></ul></li><li>On the dependency matrix, create a Satisfy relationship between the block <em>BrakePedal</em> and the requirement <em>Braking</em>.<br /><ac:image><ri:attachment ri:filename="SP_create_satisfy.png" /></ac:image><br />The requirement becomes satisfied and thus disappears from the contents of the smart package <em>Unsatisfied Requirements</em> and from the dependency matrix as well.</li></ol><h3>Case Study #3: Configuration management of the complex system - creating dynamic configuration catalogs</h3><p><em>The efficient configuration management process is a challenge in the evolution of any industrial scale product family. Smart packages are a real-life out of the box solution supporting the configuration management approach.</em></p><p>Now study the case that illustrates the efficient management of complex system configurations with the help of smart packages. We have a library (static package) of system components, which we need to see in several different views of the model, that is, catalogs, according to their characteristics. Using the catalogs will not extend the scope of the model, since they do not require duplication of the elements.<br /><ac:image><ri:attachment ri:filename="library_of_system_components.png" /></ac:image></p><p>We will create two dynamic system configuration catalogs, that is, smart packages with dynamic contents, to gather the servers from the library <em>TI Hardware</em> according to the configuration version defined in a tag value of their specification.</p><p>Do the following:</p><ol><li>Create two packages: <em>TI12 Catalog</em> and <em>TI14 Catalog</em>.</li><li>In each package, create a smart package named <em>Servers</em>.<br /><ac:image><ri:attachment ri:filename="smart_package_servers.png" /></ac:image></li><li>Define criteria for gathering the contents of the smart package <em>Servers</em> in <em>TI12 Catalog</em>. Specify search options to find in the package <em>TI Hardware</em>, all block type elements with tag value Used In=TI12.<br /><ac:image><ri:attachment ri:filename="search_smart_package_step3.png" /></ac:image></li><li>Define criteria for gathering the contents of the smart package Servers in TI14 Catalog. Specify search options to find in the package TI Hardware, all block type elements with tag value <em>Used In=TI14</em>.<br /><ac:image><ri:attachment ri:filename="search_smart_package_step4.png" /></ac:image></li><li><p>Expand the contents of both smart packages.<br /><ac:image><ri:attachment ri:filename="expand_both.png" /></ac:image></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="0ff462f5-0e43-43ae-88a5-b3ab900aa6c2"><ac:rich-text-body><p>The block <em>SUN FIRE T1000</em> appears in both <em>TI12 Catalog</em> and <em>TI14 Catalog</em>, since it has both tag values <em>Used In=TI12</em> and <em>Used In=TI14</em>.</p></ac:rich-text-body></ac:structured-macro></li><li><p>Also, you can add a block to a smart package manually. Just drag the block to the smart package.</p></li></ol></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="f06f5575-e600-4043-89f8-5bdf0e064d70"><ac:parameter ac:name="id">1701234982</ac:parameter><ac:rich-text-body><p><strong>Related Pages</strong></p><ul><li class="ancestor-link"><ac:link><ri:page ri:space-key="MT" ri:content-title="Specifying criteria for querying model" /></ac:link></li><li class="ancestor-link"><a href="https://docs.nomagic.com/display/MT/UML+elements">Model Elements</a></li><li><a href="https://docs.nomagic.com/display/MT/Stereotype">Stereotype</a></li><li><a href="https://docs.nomagic.com/display/MT/Package">Package</a></li><li><a href="https://docs.nomagic.com/display/MT/Working+with+Profiles">Working with Profiles</a></li></ul><p><br /></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=228986128 space=MED version=2 -->
## PAGE 00493: Value Item

- page_id: `228986128`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/228986128/Value+Item
- version_number: 2
- version_date: `2025-05-14T10:31:33.584+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UAF 1.3 elements
- labels: []

### NORMALIZED CONTENT

**Description**

An ideal, custom, or institution that an enterprise promotes or agrees with. It may be positive or negative, depending on point of view.

**Architecture Framework**

UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0

**Extensions**

Data Type

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description</strong></p><p class="OMGNormalParagraph">An ideal, custom, or institution that an enterprise promotes or agrees with. It may be positive or negative, depending on point of view.</p><p><strong>Architecture Framework</strong></p><p><span style="color: rgb(62,63,64);">UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0</span></p><p><strong>Extensions</strong></p><p>Data Type</p>
````

<!--NOMAGIC_PAGE id=228986129 space=MED version=2 -->
## PAGE 00494: Value Item Kind

- page_id: `228986129`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/228986129/Value+Item+Kind
- version_number: 2
- version_date: `2025-05-14T10:31:33.891+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UAF 1.3 elements
- labels: []

### NORMALIZED CONTENT

**Description**

Enumeration of the possible kinds of Value Item.

The following are enumeration literals for Value Item Kind:

- Benefit
- Cost
- KPI
- Loss
- Other
- Quality
- Revenue
- Time

**Architecture Framework**

UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0

**Extensions**

Enumeration

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description</strong></p><p class="OMGNormalParagraph">Enumeration of the possible kinds of Value Item.</p><p class="OMGNormalParagraph">The following are enumeration literals for Value Item Kind:</p><ul><li>Benefit</li><li>Cost</li><li>KPI</li><li>Loss</li><li>Other</li><li>Quality</li><li>Revenue</li><li>Time</li></ul><p><strong>Architecture Framework</strong></p><p><span style="color: rgb(62,63,64);">UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0</span></p><p><strong>Extensions</strong></p><p>Enumeration</p>
````

<!--NOMAGIC_PAGE id=9919459 space=MED version=8 -->
## PAGE 00495: Value Property

- page_id: `9919459`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/9919459/Value+Property
- version_number: 8
- version_date: `2025-09-13T12:46:28.784+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > SysML v1 elements
- labels: []

### NORMALIZED CONTENT

230681161

230681163

230681162

A Value Property is a property that specifies the quantitative property of its containing Block. Every Value Property has composite AggregationKind and is typed by a SysML Value Type. Value Properties are displayed in the **values** compartment.

[IMAGE alt='' src='']

The name of the Value Property must be without space. Otherwise, the [CONFLUENCE_PAGE title='SysML Parametric Diagram' space='MT'] will not calculate results correctly.

230681160

**Related diagrams**

- [CONFLUENCE_PAGE title='SysML Internal Block Diagram' space='MT']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="8b3d4113-3f5b-434c-93d6-8b4de01e665d"><ac:parameter ac:name="id">230681161</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="4572af5d-42c0-4f16-afa6-6d486ce349d7"><ac:parameter ac:name="id">230681163</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="cd91460d-415c-40bb-9343-ddb1680bf187"><ac:parameter ac:name="id">230681162</ac:parameter><ac:rich-text-body><p>A Value Property is a property that specifies the quantitative property of its containing Block. Every Value Property has composite AggregationKind and is typed by a SysML Value Type. Value Properties are displayed in the <strong>values</strong> compartment.</p><p><ac:image ac:title="Value Property" ac:alt="Value Property"><ri:attachment ri:filename="value_property.png" /></ac:image></p><ac:structured-macro ac:name="warning" ac:schema-version="1" ac:macro-id="f26a2d68-717d-4d57-9e80-6696c24ebff9"><ac:rich-text-body><p>The name of the Value Property must be without space. Otherwise, the <ac:link><ri:page ri:space-key="MT" ri:content-title="SysML Parametric Diagram" /></ac:link> will not calculate results correctly.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><p><br /></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="d4b78eda-b93a-4f10-ab43-64242e53cde1"><ac:parameter ac:name="id">230681160</ac:parameter><ac:rich-text-body><p class="auto-cursor-target"><strong>Related diagrams</strong></p><ul><li class="auto-cursor-target"><ac:link><ri:page ri:space-key="MT" ri:content-title="SysML Internal Block Diagram" /></ac:link></li></ul><p class="auto-cursor-target"><br /></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=243968092 space=MED version=1 -->
## PAGE 00496: Value Specification

- page_id: `243968092`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/243968092/Value+Specification
- version_number: 1
- version_date: `2025-07-31T10:50:49.989+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UML elements
- labels: []

### NORMALIZED CONTENT

You can create a standalone value specification in a model from the appropriate element's shortcut menu.

You can use any of the following ways to create a value specification:

- Via the element’s shortcut menu.
- Via the element’s Specification window.
- By defining a default value to an element.

You can also change an assigned value specification after it has been created.

To create a value specification from the element’s shortcut menu

1. In the Containment tree, select an appropriate element.
2. From the selected element's shortcut menu, select **Create Element** > **Value Specification** and choose a suitable value specification.

To assign a value specification in the element’s [CONFLUENCE_PAGE title='Specification window' space='MT']

1. In the Specification window of the selected element, choose an appropriate property value cell and click the Show Shortcut Menu button (the black arrow).
2. In the shortcut menu, click Value Specification and select a value specification.

To create a value specification automatically

1. Assign a default value to a property for which you want to create a value specification.
2. The value specification of the corresponding type will be assigned automatically according to the assigned default value in your model.

To change an assigned value specification

1. In the Specification window of the selected element, choose an appropriate property value cell and click the Show Shortcut Menu button (the black arrow).
2. From the shortcut menu, select Value Specification > Delete <value specification>.
3. Assign a new value specification.

#### PANEL: Related Pages

Related Pages

- [CONFLUENCE_PAGE title='UML elements' space='']
- [CONFLUENCE_PAGE title='Specification window' space='MT']
- [CONFLUENCE_PAGE title='Transition' space='']
- [CONFLUENCE_PAGE title='State Machine diagram' space='MT']
- [CONFLUENCE_PAGE title='Activity diagram' space='MT']
- [CONFLUENCE_PAGE title='Sequence diagram' space='MT']
- [CONFLUENCE_PAGE title='Use Case diagram' space='MT']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p>You can create a standalone value specification in a model from the appropriate element's shortcut menu.</p><p>You can use any of the following ways to create a value specification:</p><ul><li>Via the element’s shortcut menu.</li><li>Via the element’s Specification window.</li><li>By defining a default value to an element.</li></ul><p>You can also change an assigned value specification after it has been created.</p><p> </p><p>To create a value specification from the element’s shortcut menu</p><hr /><ol><li>In the Containment tree, select an appropriate element.</li><li><p>From the selected element's shortcut menu, select <strong>Create Element</strong> &gt; <strong>Value Specification</strong> and choose a suitable value specification.</p></li></ol><p> </p><p>To assign a value specification in the element’s <ac:link><ri:page ri:space-key="MT" ri:content-title="Specification window" /></ac:link></p><hr /><ol><li>In the Specification window of the selected element, choose an appropriate property value cell and click the <strong>Show Shortcut Menu</strong> button (the black arrow).</li><li>In the shortcut menu, click <strong>Value Specification</strong> and select a value specification.</li></ol><p> </p><p>To create a value specification automatically</p><hr /><ol><li>Assign a default value to a property for which you want to create a value specification.</li><li>The value specification of the corresponding type will be assigned automatically according to the assigned default value in your model.</li></ol><p> </p><p>To change an assigned value specification</p><hr /><ol><li>In the Specification window of the selected element, choose an appropriate property value cell and click the <strong>Show Shortcut Menu</strong> button (the black arrow).</li><li>From the shortcut menu, select <strong style="line-height: 1.42857;">Value Specification</strong> &gt; <strong style="line-height: 1.42857;">Delete</strong> &lt;value specification&gt;.</li><li>Assign a new value specification.</li></ol></ac:layout-cell><ac:layout-cell><p> </p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="a1cb6614-da6a-4a7b-adf1-3ec18e11a18c"><ac:parameter ac:name="title">Related Pages</ac:parameter><ac:rich-text-body><ul><li><ac:link><ri:page ri:content-title="UML elements" /><ac:plain-text-link-body><![CDATA[Model Elements]]></ac:plain-text-link-body></ac:link></li><li><ac:link><ri:page ri:space-key="MT" ri:content-title="Specification window" /></ac:link></li><li><ac:link><ri:page ri:content-title="Transition" /></ac:link></li><li><ac:link><ri:page ri:space-key="MT" ri:content-title="State Machine diagram" /></ac:link></li><li><ac:link><ri:page ri:space-key="MT" ri:content-title="Activity diagram" /></ac:link></li><li><ac:link><ri:page ri:space-key="MT" ri:content-title="Sequence diagram" /></ac:link></li><li><ac:link><ri:page ri:space-key="MT" ri:content-title="Use Case diagram" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=228986130 space=MED version=2 -->
## PAGE 00497: Value Stream

- page_id: `228986130`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/228986130/Value+Stream
- version_number: 2
- version_date: `2025-05-14T10:31:34.247+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UAF 1.3 elements
- labels: []

### NORMALIZED CONTENT

**Description**

An end-to-end collection of activities that create a result for a customer, who may be the ultimate customer or an internal end-user of the value stream. Value stream nested within another value stream may represent Value Stream Stage - a distinct, identifiable phase or step within a value stream [The Business Architecture Metamodel Guide, 2020].

**Architecture Framework**

UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0

**Extensions**

Instance Specification

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description</strong></p><p class="OMGNormalParagraph">An end-to-end collection of activities that create a result for a customer, who may be the ultimate customer or an internal end-user of the value stream. Value stream nested within another value stream may represent Value Stream Stage - a distinct, identifiable phase or step within a value stream [The Business Architecture Metamodel Guide, 2020].</p><p><strong>Architecture Framework</strong></p><p><span style="color: rgb(62,63,64);">UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0</span></p><p><strong>Extensions</strong></p><p>Instance Specification</p>
````

<!--NOMAGIC_PAGE id=9919422 space=MED version=19 -->
## PAGE 00498: Value Type

- page_id: `9919422`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/9919422/Value+Type
- version_number: 19
- version_date: `2025-09-13T12:46:27.344+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > SysML v1 elements
- labels: []

### NORMALIZED CONTENT

133530759

133530762

133530760

A Value Type is defined as a stereotype of UML Data Type to establish a more neutral term for system values that may never be given a concrete data representation. A Value Type adds an ability to carry a [CONFLUENCE_PAGE title='Unit' space='']unitsof measure of a [CONFLUENCE_PAGE title='Quantity Kind' space=''] associated with the value.

Use the [CONFLUENCE_PAGE title='Using QUDV model library' space='MT'] to find all standard value types.

[IMAGE alt='' src='']

When specifying the Value Type for a [CONFLUENCE_PAGE title='Value Property' space=''], you can select one of the following:

- Unitless Value Type.
- Value Type with specified [CONFLUENCE_PAGE title='Unit' space='']unit.

Look at the table below to see the differences.

- If you cannot find the Value Type you need, you can create a custom Value Type. [CONFLUENCE_PAGE title='Customizing Units' space='MT']>]]>
- If you cannot find the [CONFLUENCE_PAGE title='Unit' space='']you need, you can create a custom Unit. [CONFLUENCE_PAGE title='Customizing Units' space='MT']>]]>

If you want to specify the Value Type for a Value Property, follow the procedures in the [CONFLUENCE_PAGE title='Using Units' space='MT'] page.

| Value Type | Name construction | Purpose | Example |
| --- | --- | --- | --- |
| Unitless | Quantity name, e.g. distance. | Use this to create a general-purpose model. and its Slots can contain different units of the same . |  |
| With specified | Quantity and unit names, e.g. distance[metre]. | Use this to create a specific-purpose model. Instance Specifications and its Slots can contain the same units of the same . |  |

133530758

**Related diagrams**

- [CONFLUENCE_PAGE title='SysML Block Definition Diagram' space='MT']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="1431c954-eda6-40c5-855a-a9d134e7fbd3"><ac:parameter ac:name="id">133530759</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="fb6184c2-4af3-4814-8aef-b0710e62d312"><ac:parameter ac:name="id">133530762</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="1a981aee-d3a0-4969-a755-fe720ed2fe50"><ac:parameter ac:name="id">133530760</ac:parameter><ac:rich-text-body><p>A Value Type is defined as a stereotype of UML Data Type to establish a more neutral term for system values that may never be given a concrete data representation. A Value Type adds an ability to carry a <ac:link><ri:page ri:content-title="Unit" /><ac:link-body><span class="confluence-link">units</span> </ac:link-body></ac:link>of measure of a <ac:link><ri:page ri:content-title="Quantity Kind" /></ac:link> associated with the value.</p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="19c0e762-25f2-442f-969a-966776a30389"><ac:rich-text-body><p>Use the <span class="confluence-link"><ac:link><ri:page ri:space-key="MT" ri:content-title="Using QUDV model library" /><ac:plain-text-link-body><![CDATA[QUDV model library]]></ac:plain-text-link-body></ac:link></span> to find all standard value types.</p></ac:rich-text-body></ac:structured-macro><p><ac:image><ri:attachment ri:filename="unitless_value_type.png" /></ac:image></p><p><br /></p><p><span> When specifying the Value Type for a <ac:link><ri:page ri:content-title="Value Property" /></ac:link>, you can select one of the following:</span></p><ul><li><span>Unitless Value Type.</span></li><li><span>Value Type with specified <ac:link><ri:page ri:content-title="Unit" /><ac:link-body><span class="confluence-link">unit</span></ac:link-body></ac:link>.</span></li></ul><p><span>Look at the table below to see the differences.</span></p><ac:structured-macro ac:name="warning" ac:schema-version="1" ac:macro-id="645b475e-5a16-4534-a281-1695f2eb7e92"><ac:rich-text-body><ul><li><span>If you cannot find the Value Type you need, you can create a custom Value Type. <ac:link ac:anchor="Creating custom Value Type"><ri:page ri:space-key="MT" ri:content-title="Customizing Units" /><ac:plain-text-link-body><![CDATA[Learn how to create a custom Value Type >>]]></ac:plain-text-link-body></ac:link></span></li><li><span>If you cannot find the <ac:link><ri:page ri:content-title="Unit" /><ac:plain-text-link-body><![CDATA[unit ]]></ac:plain-text-link-body></ac:link>you need, you can create a custom Unit. <ac:link ac:anchor="Creating custom Unit"><ri:page ri:space-key="MT" ri:content-title="Customizing Units" /><ac:plain-text-link-body><![CDATA[Learn how to create a custom units >>]]></ac:plain-text-link-body></ac:link></span></li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><span>If you want to specify the Value Type for a Value Property, follow the procedures in the <ac:link><ri:page ri:space-key="MT" ri:content-title="Using Units" /></ac:link> page.</span></p><table class="relative-table wrapped"><colgroup><col style="width: 116.0px;" /><col style="width: 226.0px;" /><col style="width: 410.0px;" /><col style="width: 349.0px;" /></colgroup><tbody><tr><th>Value Type</th><th>Name construction</th><th>Purpose</th><th>Example</th></tr><tr><td>Unitless</td><td><span><span>Quantity name, e.g. distance.</span></span></td><td><span><span>Use this <span><span>to create a general-purpose model</span></span>. <ac:link><ri:page ri:space-key="MT" ri:content-title="Instance Specification" /><ac:plain-text-link-body><![CDATA[Instance Specifications]]></ac:plain-text-link-body></ac:link> and its <span class="confluence-link">Slots</span> can contain different units of the same <ac:link><ri:page ri:content-title="Block" /></ac:link>.</span></span></td><td><div class="content-wrapper"><p><ac:image><ri:attachment ri:filename="unitless_value_type_1.png" /></ac:image></p></div></td></tr><tr><td>With <span>specified <span class="confluence-link"><ac:link><ri:page ri:content-title="Unit" /><ac:plain-text-link-body><![CDATA[units]]></ac:plain-text-link-body></ac:link></span></span></td><td><span>Quantity and unit names, e.g. distance[metre].</span></td><td><span>Use this to create a specific-purpose model. <ac:link><ri:page ri:space-key="MT" ri:content-title="Instance Specification" /><ac:link-body>I<span><span>nstance Specifications</span></span></ac:link-body></ac:link><span><span> and its Slots can contain the same units of the same <ac:link><ri:page ri:content-title="Block" /></ac:link>.</span></span></span></td><td><div class="content-wrapper"><p><ac:image><ri:attachment ri:filename="value_type_with_unit.png" /></ac:image></p></div></td></tr></tbody></table></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="ed7ecf3a-999b-4742-b0cb-c84182483660"><ac:parameter ac:name="id">133530758</ac:parameter><ac:rich-text-body><p class="auto-cursor-target"><strong>Related diagrams</strong></p><ul><li class="auto-cursor-target"><ac:link><ri:page ri:space-key="MT" ri:content-title="SysML Block Definition Diagram" /><ac:plain-text-link-body><![CDATA[SysML Block Definition Diagram ]]></ac:plain-text-link-body></ac:link></li></ul><p class="auto-cursor-target"><br /></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=243967493 space=MED version=2 -->
## PAGE 00499: Variables

- page_id: `243967493`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/243967493/Variables
- version_number: 2
- version_date: `2025-09-13T12:44:14.523+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UML elements > Activity
- labels: []

### NORMALIZED CONTENT

Variables are elements that indirectly pass data between [CONFLUENCE_PAGE title='Action' space='']. A local variable stores values shared by the actions in a structured [CONFLUENCE_PAGE title='Activity' space=''] group, but not accessible outside the group. The output of an action can be written to a variable and read for the input to a subsequent action, which is effectively an indirect data flow path. Because there is no predefined relationship between actions that read and write variables, these actions must be sequenced by control flows to prevent race conditions that may occur between actions that read or write the same variable.

To create a Variable

1. Open Activity Specification window .
2. ChooseVariables from the property group list.
3. To create a new Variable click **Create**.
4. Specify the Variable in the Specification of Variable window.

[IMAGE alt='' src='']

###### Creating variables in the Specification of Activity dialog

[IMAGE alt='' src='']

###### Specification dialog for a Variable

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>Variables are elements that indirectly pass data between <ac:link><ri:page ri:content-title="Action" /><ac:plain-text-link-body><![CDATA[Actions]]></ac:plain-text-link-body></ac:link>. A local variable stores values shared by the actions in a structured <ac:link><ri:page ri:content-title="Activity" /></ac:link> group, but not accessible outside the group. The output of an action can be written to a variable and read for the input to a subsequent action, which is effectively an indirect data flow path. Because there is no predefined relationship between actions that read and write variables, these actions must be sequenced by control flows to prevent race conditions that may occur between actions that read or write the same variable.</p><p><br /></p><p>To create a Variable</p><hr /><ol><li>Open Activity <a href="https://docs.nomagic.com/display/MT/Specification+window" rel="nofollow">Specification window</a>. </li><li><span style="color: rgb(0,0,0);"><span style="color: rgb(0,0,0);">Choose </span>Variables from the property group list.</span></li><li><span style="color: rgb(0,0,0);">To create a new Variable click <strong>Create</strong>.</span></li><li><span style="color: rgb(0,0,0);">Specify the Variable in the Specification of Variable window.</span></li></ol><p><ac:image ac:align="center"><ri:attachment ri:filename="Specification_of_activity_variables.png" /></ac:image></p><h6 style="text-align: center;">Creating variables in the Specification of Activity dialog</h6><p><ac:image ac:align="center"><ri:attachment ri:filename="Specification_of_variables.png" /></ac:image></p><h6 style="text-align: center;">Specification dialog for a Variable</h6>
````

<!--NOMAGIC_PAGE id=249005181 space=MED version=2 -->
## PAGE 00500: Verify

- page_id: `249005181`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/249005181/Verify
- version_number: 2
- version_date: `2025-08-18T17:39:38.365+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > Requirement-related elements
- labels: []

### NORMALIZED CONTENT

A 'Verify' relationship is a dependency between a requirement and a test case or a model element that can determine whether the system fulfills the requirement. As with other dependencies, the arrow direction points from the (client) test case to the (supplier) requirement.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="auto-cursor-target">A 'Verify' relationship is a dependency between a requirement and a test case or a model element that can determine whether the system fulfills the requirement. As with other dependencies, the arrow direction points from the (client) test case to the (supplier) requirement.</p>
````

<!--NOMAGIC_PAGE id=228986132 space=MED version=2 -->
## PAGE 00501: Version Of Configuration

- page_id: `228986132`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/228986132/Version+Of+Configuration
- version_number: 2
- version_date: `2025-05-14T10:31:35.135+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UAF 1.3 elements
- labels: []

### NORMALIZED CONTENT

**Description**

A property of a Whole Life Configuration, used in version control of a Versioned Element. It asserts that a Versioned Element is a version of a Whole Life Configuration.

**Architecture** **Framework**

UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0

**Extension**

UML Property

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="OMGNormalParagraph"><strong>Description</strong></p><p class="OMGNormalParagraph">A property of a Whole Life Configuration, used in version control of a Versioned Element. It asserts that a Versioned Element is a version of a Whole Life Configuration.</p><p class="OMGNormalParagraph"><strong>Architecture</strong> <strong>Framework</strong></p><p class="OMGNormalParagraph"><span style="color: rgb(62,63,64);">UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0</span></p><p><strong>Extension</strong></p><p>UML Property </p><p><br /></p>
````

<!--NOMAGIC_PAGE id=228986133 space=MED version=2 -->
## PAGE 00502: Version Succession

- page_id: `228986133`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/228986133/Version+Succession
- version_number: 2
- version_date: `2025-05-14T10:31:35.515+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UAF 1.3 elements
- labels: []

### NORMALIZED CONTENT

**Description**

A dependency relationship between two Version Of Configurations that denotes that one Version Of Configuration follows from another.

**Architecture Framework**

UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0

**Extension**

UML Dependency

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="OMGNormalParagraph"><strong>Description</strong></p><p class="OMGNormalParagraph">A dependency relationship between two  Version Of Configurations that denotes that one Version Of Configuration follows from another.</p><p class="OMGNormalParagraph"><strong>Architecture Framework</strong></p><p class="OMGNormalParagraph"><span style="color: rgb(62,63,64);">UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0</span></p><p class="OMGNormalParagraph"><strong>Extension</strong></p><p class="OMGNormalParagraph">UML Dependency</p><p><br /></p>
````

<!--NOMAGIC_PAGE id=228986131 space=MED version=2 -->
## PAGE 00503: Versioned Element

- page_id: `228986131`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/228986131/Versioned+Element
- version_number: 2
- version_date: `2025-05-14T10:31:34.688+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UAF 1.3 elements
- labels: []

### NORMALIZED CONTENT

**Description**

An abstract grouping of ResourcePerformer and ServiceSpecification that allows VersionOfConfiguration to be related to ActualProjectMilestones.

**Architecture** **Framework**

UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0

**Extension**

UML Class

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="OMGNormalParagraph"><strong>Description</strong></p><p class="OMGNormalParagraph">An abstract grouping of ResourcePerformer and ServiceSpecification that allows VersionOfConfiguration to be related to ActualProjectMilestones.</p><p class="OMGNormalParagraph"><strong>Architecture</strong> <strong>Framework</strong></p><p class="OMGNormalParagraph"><span style="color: rgb(62,63,64);">UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0</span></p><p class="OMGNormalParagraph"><strong>Extension</strong></p><p class="OMGNormalParagraph">UML Class</p><p><br /></p>
````

<!--NOMAGIC_PAGE id=9919489 space=MED version=2 -->
## PAGE 00504: View

- page_id: `9919489`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/9919489/View
- version_number: 2
- version_date: `2025-09-13T12:46:30.907+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > SysML v1 elements
- labels: []

### NORMALIZED CONTENT

A View is a representation of a whole system from the perspective of a single [CONFLUENCE_PAGE title='Viewpoint' space='']. A view can only own element import, package import, comment, and constraint elements.

[IMAGE alt='' src='']

#### PANEL: Related diagram

Related diagram

- [CONFLUENCE_PAGE title='Views and Viewpoints Diagram' space='MT']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p>A View is a representation of a whole system from the perspective of a single <ac:link><ri:page ri:content-title="Viewpoint" /></ac:link>. A view can only own element import, package import, comment, and constraint elements.</p><p><ac:image ac:alt="View" ac:title="View"><ri:attachment ri:filename="view.png" /></ac:image></p></ac:layout-cell><ac:layout-cell><p> </p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p> </p></ac:layout-cell><ac:layout-cell><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="945c9ebe-05c7-4a1c-b7c9-5fdadbc65f5c"><ac:parameter ac:name="title">Related diagram</ac:parameter><ac:rich-text-body><ul><li><ac:link><ri:page ri:space-key="MT" ri:content-title="Views and Viewpoints Diagram" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=228986134 space=MED version=3 -->
## PAGE 00505: View in UAF

- page_id: `228986134`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/228986134/View+in+UAF
- version_number: 3
- version_date: `2025-08-14T15:08:04.549+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UAF 1.3 elements
- labels: []

### NORMALIZED CONTENT

**Description**

An architecture view expresses the architecture of the system-of-interest in accordance with an architecture viewpoint (or simply, viewpoint).

**Architecture** **Framework**

UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0

**Extension**

UML Class

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="OMGNormalParagraph"><strong>Description</strong></p><p>An architecture view expresses the architecture of the system-of-interest in accordance with an architecture viewpoint (or simply, viewpoint).</p><p><strong>Architecture</strong> <strong>Framework</strong></p><p><span style="color:var(--ds-text,#333333);">UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0</span></p><p><strong>Extension</strong></p><p>UML Class</p><p><br /></p>
````

<!--NOMAGIC_PAGE id=9919491 space=MED version=5 -->
## PAGE 00506: Viewpoint

- page_id: `9919491`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/9919491/Viewpoint
- version_number: 5
- version_date: `2025-09-13T12:46:31.088+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > SysML v1 elements
- labels: []

### NORMALIZED CONTENT

A Viewpoint is a specification of the conventions and rules for constructing and using a view for the purpose of addressing a set of stakeholder concerns. The languages and methods for specifying a View can reference methods and languages in another Viewpoint. They specify the elements expected to be represented in the view that may be formally or informally defined.

[IMAGE alt='' src='']

A Viewpoint has a Method property which describes the expectation of what stakeholder(s) wish to see exposed from the model, how the stakeholder wishes the information to be structured and presented, and in what kind of artifact the stakeholder wants to consume the information. It is the set of rules that describe how the view should express the information from the model to address the stakeholder concerns. The methods are used to construct the [CONFLUENCE_PAGE title='View' space=''] for the Viewpoint.

#### PANEL: Related diagram

Related diagram

- [CONFLUENCE_PAGE title='Views and Viewpoints Diagram' space='MT']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>A Viewpoint is a specification of the conventions and rules for constructing and using a view for the purpose of addressing a set of stakeholder concerns. The languages and methods for specifying a View can reference methods and languages in another Viewpoint. They specify the elements expected to be represented in the view that may be formally or informally defined.</p><p><ac:image ac:title="Viewpoint" ac:alt="Viewpoint"><ri:attachment ri:filename="viewpoint.png" /></ac:image></p><p>A Viewpoint has a Method property which describes the expectation of what stakeholder(s) wish to see exposed from the model, how the stakeholder wishes the information to be structured and presented, and in what kind of artifact the stakeholder wants to consume the information. It is the set of rules that describe how the view should express the information from the model to address the stakeholder concerns. The methods are used to construct the <ac:link><ri:page ri:content-title="View" /><ac:plain-text-link-body><![CDATA[Views]]></ac:plain-text-link-body></ac:link> for the Viewpoint.</p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="945c9ebe-05c7-4a1c-b7c9-5fdadbc65f5c"><ac:parameter ac:name="title">Related diagram</ac:parameter><ac:rich-text-body><ul><li><ac:link><ri:page ri:space-key="MT" ri:content-title="Views and Viewpoints Diagram" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=228986135 space=MED version=3 -->
## PAGE 00507: Viewpoint in UAF

- page_id: `228986135`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/228986135/Viewpoint+in+UAF
- version_number: 3
- version_date: `2025-08-14T15:09:34.773+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UAF 1.3 elements
- labels: []

### NORMALIZED CONTENT

**Description**

An architecture viewpoint frames (to formulate or construct in a particular style or language) one or more concerns. A concern can be framed by more than one viewpoint.

**Architecture** **Framework**

UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0

**Extension**

UML Class

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="OMGNormalParagraph"><strong>Description</strong></p><p>An architecture viewpoint frames (to formulate or construct in a particular style or language) one or more concerns. A concern can be framed by more than one viewpoint. </p><p><strong>Architecture</strong> <strong>Framework</strong></p><p><span style="color:var(--ds-text,#333333);">UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0</span></p><p><strong>Extension</strong></p><p>UML Class</p><p><br /></p>
````

<!--NOMAGIC_PAGE id=228986136 space=MED version=2 -->
## PAGE 00508: Vision Statement

- page_id: `228986136`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/228986136/Vision+Statement
- version_number: 2
- version_date: `2025-05-14T10:31:36.961+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UAF 1.3 elements
- labels: []

### NORMALIZED CONTENT

**Description**

A type of comment that describes the future state of the enterprise, without regard to how it is to be achieved.

**Architecture Framework**

UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0

**Extension**

UML Comment

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="OMGNormalParagraph"><strong>Description</strong></p><p>A type of comment that describes the future state of the enterprise, without regard to how it is to be achieved.</p><p><strong><span class="fontstyle0">Architecture Framework</span></strong></p><p><span style="color: rgb(62,63,64);">UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0</span></p><p><strong>Extension</strong></p><p>UML Comment</p><p><br /></p>
````

<!--NOMAGIC_PAGE id=228986137 space=MED version=2 -->
## PAGE 00509: Whole Life Configuration

- page_id: `228986137`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/228986137/Whole+Life+Configuration
- version_number: 2
- version_date: `2025-05-14T10:31:37.232+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UAF 1.3 elements
- labels: []

### NORMALIZED CONTENT

**Description**

A set of Versioned Elements.

**Architecture** **Framework**

UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0

**Extension**

UML Class

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="OMGNormalParagraph"><strong>Description</strong></p><p class="OMGNormalParagraph">A set of Versioned Elements. </p><p class="OMGNormalParagraph"><strong>Architecture</strong> <strong>Framework</strong></p><p class="OMGNormalParagraph"><span style="color: rgb(62,63,64);">UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0</span></p><p class="OMGNormalParagraph"><strong>Extension</strong></p><p class="OMGNormalParagraph">UML Class</p><p><br /></p>
````

<!--NOMAGIC_PAGE id=228986138 space=MED version=2 -->
## PAGE 00510: Whole Life Configuration Kind

- page_id: `228986138`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/228986138/Whole+Life+Configuration+Kind
- version_number: 2
- version_date: `2025-05-14T10:31:37.500+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UAF 1.3 elements
- labels: []

### NORMALIZED CONTENT

**Description**

Enumeration of the possible kinds of Whole Life Configuration. Its enumeration literals are:

- Service - Indicates that the WholeLifeConfiguration associated with the WholeLifeConfigurationKind is the master specification from which Services are versioned.
- ResourcePerformer - Indicates that the WholeLifeConfiguration associated with the WholeLifeConfigurationKind is the master specification from which ResourcePerformers are versioned.
- Organizational Resource - Indicates that the Whole Life Configuration associated with the Whole Life Configuration Kind is the master specification from which Organizational Resources are versioned.

**Architecture** **Framework**

UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="OMGBoldBulletKeepNextParagraph"><strong>Description</strong></p><p class="OMGNormalParagraph">Enumeration of the possible kinds of Whole Life Configuration. Its enumeration literals are:</p><ul><li>Service - Indicates that the WholeLifeConfiguration associated with the WholeLifeConfigurationKind is the master specification from which Services are versioned.</li><li>ResourcePerformer - Indicates that the WholeLifeConfiguration associated with the WholeLifeConfigurationKind is the master specification from which ResourcePerformers are versioned.</li><li>Organizational Resource - Indicates that the Whole Life Configuration associated with the Whole Life Configuration Kind is the master specification from which Organizational Resources are versioned.</li></ul><p><strong>Architecture</strong> <strong>Framework</strong></p><p><span style="color: rgb(62,63,64);">UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0</span></p><p><br /></p>
````

<!--NOMAGIC_PAGE id=228986139 space=MED version=2 -->
## PAGE 00511: Whole Life Enterprise

- page_id: `228986139`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/228986139/Whole+Life+Enterprise
- version_number: 2
- version_date: `2025-05-14T10:31:37.749+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UAF 1.3 elements
- labels: []

### NORMALIZED CONTENT

**Description**

A Whole Life Enterprise is a purposeful endeavor of any size involving people, organizations and supporting systems. It is made up of Temporal Parts and Structural Parts.

**Architecture** **Framework**

UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0

**Extension**

UML Class

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="OMGNormalParagraph"><strong>Description</strong></p><p class="OMGNormalParagraph">A Whole Life Enterprise is a purposeful endeavor of any size involving people, organizations and supporting systems. It is made up of Temporal Parts and Structural Parts. </p><p class="OMGNormalParagraph"><strong>Architecture</strong> <strong>Framework</strong></p><p class="OMGNormalParagraph"><span style="color: rgb(62,63,64);">UAF 1.3, DoDAF 2.0, MODAF, NAF, NAF 4.0</span></p><p class="OMGNormalParagraph"><strong>Extension</strong></p><p class="OMGNormalParagraph">UML Class</p><p><br /></p>
````

<!--NOMAGIC_PAGE id=243967485 space=MED version=1 -->
## PAGE 00512: Working with Actions

- page_id: `243967485`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/243967485/Working+with+Actions
- version_number: 1
- version_date: `2025-07-31T10:50:33.129+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UML elements > Action
- labels: []

### NORMALIZED CONTENT

907190545

907190548

907190547

To create any action quickly

1. In the Activity diagram toolbar , right-click or expand the Action button. The menu opens. [ATTACHMENT filename='action_toolbar.png']
2. Select the Any Action command. The Select Action Metaclass dialog opens. [ATTACHMENT filename='select_action_metaclass.png']
3. Select an Action metaclass from the list, or type the first letter of the metaclass in the [CONFLUENCE_PAGE title='Quick filter' space='MT']. Click **OK**. The Action is created.
4. Click the diagram pane. An action symbol is drawn.

##### Applying duration constraint on the Action

You can create and apply a duration constraint on an Action that states that the output must occur after delay from the input.

To create and apply a duration constraint

1. Select an Action and create the input and output [CONFLUENCE_PAGE title='Pin' space=''] to specify the [CONFLUENCE_PAGE title='Event' space=''] .
2. Create a duration constraint for the Action using one of the following way:
  - From the diagram palette:
    1. In the diagram palette, under the Common category, expand the Constraint command, and select the Duration Constraint, Time Constraint, or Constraint button, and create it directly on the action shape.
  - In the Specification window: 
 a. In the [CONFLUENCE_PAGE title='Call Behavior Action' space=''] [CONFLUENCE_PAGE title='Specification window' space='MT'], click the **Constraints** group. 
 b. Click the **Apply** button. The **Select Constraint** dialog opens. 
 c. Select the constraint storage place, and click the **Create** button. In the opened menu, select the **Duration Constraint** command. The **Duration Constraint** Specification window opens.
3. Specify a duration interval. Type the minimum and maximum duration to hold the Activity in the Min and Max property specification cells, e.g., 0 sec and 30 sec.
4. Assign the Events for the input and output pins:
  1. In the opened **Duration Constraint** Specification window, click the **Specification** property specification cell, and click the Show Shortcut Menu button [IMAGE alt='' src='']. The following shortcut menu opens: [IMAGE alt='' src='']
  2. Select the **Open Specification** command. The **Duration Interval** Specification window opens.
  3. Click the **Min** property specification cell, and and click the Show Shortcut Menu button [IMAGE alt='' src='']. In the shortcut menu, select the **Open Specification** command. The **Duration** Specification window opens.
  4. In the Event field, click the “...” button. The **Select Element** dialog opens. Select the activity input pin.
  5. Repeat steps c and d for the Max property - select the action output pin as an event.
5. Apply the created duration constraint on the action.

The following sample depicts a fragment of the [CONFLUENCE_PAGE title='Activity diagram' space='MT'] with a duration constraint applied on the Action.

[IMAGE alt='' src='']

907190544

**Related pages**

- [CONFLUENCE_PAGE title='UML elements' space='']
- [CONFLUENCE_PAGE title='Behavior' space='']
- [CONFLUENCE_PAGE title='Action' space='']
- [CONFLUENCE_PAGE title='Activity diagram' space='MT']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="4ba5610a-1806-450e-96d9-e09c0ef8155d"><ac:parameter ac:name="id">907190545</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="5d818015-8974-4bdb-a26e-a849634ae778"><ac:parameter ac:name="id">907190548</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="448a359e-ec88-438e-8443-bbb3b8b77062"><ac:parameter ac:name="id">907190547</ac:parameter><ac:rich-text-body><ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p>To create any action quickly </p><hr /><ol><li>In the <span class="confluence-link">Activity diagram toolbar</span>, right-click or expand the <strong>Action</strong> button. The menu opens.<br /><br /><ac:image><ri:attachment ri:filename="action_toolbar.png" /></ac:image><br /><br /></li><li>Select the <strong>Any Action</strong> command. The <strong>Select Action Metaclass</strong> dialog opens.<br /><br /><ac:image><ri:attachment ri:filename="select_action_metaclass.png" /></ac:image><br /><br /></li><li><p>Select an Action metaclass from the list, or type the first letter of the metaclass in the <ac:link><ri:page ri:space-key="MT" ri:content-title="Quick filter" /><ac:plain-text-link-body><![CDATA[Quick filter box]]></ac:plain-text-link-body></ac:link>. Click <strong>OK</strong>. The Action is created.</p></li><li><p>Click the diagram pane. An action symbol is drawn.</p></li></ol></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><h3>Applying duration constraint on the Action</h3><p><br />You can create and apply a duration constraint on an Action that states that the output must occur after delay from the input.</p><p><br />To create and apply a duration constraint</p><hr /><ol><li>Select an Action and create the input and output <ac:link><ri:page ri:content-title="Pin" /><ac:plain-text-link-body><![CDATA[Pins]]></ac:plain-text-link-body></ac:link> to specify the <ac:link><ri:page ri:content-title="Event" /><ac:plain-text-link-body><![CDATA[Events]]></ac:plain-text-link-body></ac:link>.</li><li>Create a duration constraint for the Action using one of the following way:<br /><ul><li>From the diagram palette:<br /><ol><li>In the diagram palette, under the Common category, expand the <strong>Constraint</strong> command, and select the Duration Constraint, Time Constraint, or Constraint button, and create it directly on the action shape.</li></ol></li><li><p>In the Specification window:<br />      a. In the <ac:link><ri:page ri:content-title="Call Behavior Action" /></ac:link> <ac:link><ri:page ri:space-key="MT" ri:content-title="Specification window" /></ac:link>, click the <strong>Constraints</strong> group.<br />      b. Click the <strong>Apply</strong> button. The <strong>Select Constraint</strong> dialog opens.<br />      c. Select the constraint storage place, and click the <strong>Create</strong> button. In the opened menu, select the <strong>Duration Constraint</strong> command. The <strong>Duration Constraint</strong> Specification window opens.</p></li></ul></li><li>Specify a duration interval. Type the minimum and maximum duration to hold the Activity in the <strong>Min</strong> and <strong>Max</strong> property specification cells, e.g., 0 sec and 30 sec.</li><li>Assign the Events for the input and output pins:<br /><ol><li><p>In the opened <strong>Duration Constraint</strong> Specification window, click the <strong>Specification</strong> property specification cell, and click the Show Shortcut Menu button <ac:image><ri:attachment ri:filename="show_shortcut_menu.png"><ri:page ri:space-key="MT" ri:content-title="_MD buttons" /></ri:attachment></ac:image>. The following shortcut menu opens:</p><p><ac:image><ri:attachment ri:filename="open_specification_command.png" /></ac:image></p></li><li><p>Select the <strong>Open Specification</strong> command. The <strong>Duration Interval</strong> Specification window opens.</p></li><li><p>Click the <strong>Min</strong> property specification cell, and and click the Show Shortcut Menu button <ac:image><ri:attachment ri:filename="show_shortcut_menu.png"><ri:page ri:space-key="MT" ri:content-title="_MD buttons" /></ri:attachment></ac:image>. In the shortcut menu, select the <strong>Open Specification</strong> command. The <strong>Duration</strong> Specification window opens.</p></li><li><p>In the Event field, click the “...” button. The <strong>Select Element</strong> dialog opens. Select the activity input pin.</p></li><li><p>Repeat steps c and d for the Max property - select the action output pin as an event.</p></li></ol></li><li><p>Apply the created duration constraint on the action.</p></li></ol><p>The following sample depicts a fragment of the <ac:link><ri:page ri:space-key="MT" ri:content-title="Activity diagram" /></ac:link> with a duration constraint applied on the Action.</p><p><ac:image><ri:attachment ri:filename="duration_constraint2.png" /></ac:image></p></ac:layout-cell><ac:layout-cell><p> </p></ac:layout-cell></ac:layout-section></ac:layout></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="69c42a84-10af-404f-b04e-0fdea78e9786"><ac:parameter ac:name="id">907190544</ac:parameter><ac:rich-text-body><p><strong>Related pages</strong></p><ul><li><ac:link><ri:page ri:content-title="UML elements" /><ac:plain-text-link-body><![CDATA[Model Elements]]></ac:plain-text-link-body></ac:link></li><li><ac:link><ri:page ri:content-title="Behavior" /></ac:link></li><li><ac:link><ri:page ri:content-title="Action" /></ac:link></li><li><ac:link><ri:page ri:space-key="MT" ri:content-title="Activity diagram" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=243967512 space=MED version=1 -->
## PAGE 00513: Working with Associations

- page_id: `243967512`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/243967512/Working+with+Associations
- version_number: 1
- version_date: `2025-07-31T10:50:33.820+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UML elements > Association
- labels: ['reflective-association', 'association-class']

### NORMALIZED CONTENT

1018698642

1018698644

1018698643

An [CONFLUENCE_PAGE title='Association' space=''] is a relationship between two classes. It is represented by a solid line. Though associations are bi-directional by default, they can also be unidirectional, where one class knows about the other class and the relationship but the other class does not. Sometimes an association links a class to itself. This association is called a recursive (reflexive) association. One example of this association is an employee who is managed by a manager who is also himself an employee.

To draw a recursive (reflexive) association

1. Select Association .
2. Click a class ( Employee in this example) and hover over the class until you see a rectangle shape. Click the class again to create a recursive association. [ATTACHMENT filename='recursiveAssociation.png']

##### Association Properties

You can specify association properties in the association [CONFLUENCE_PAGE title='Specification window' space='MT']. The description of each property appears in the same window. The description area of the Specification window presents the descriptions.

To show the direction arrow near the association name

1. Do one of the following:
  - Right-click the association, and from the shortcut menu, select Show Direction Arrow .
  - Open the association [CONFLUENCE_PAGE title='Symbol Properties dialog' space='MT'] dialog and set the Show Direction Arrow property to true .

The default Direction Arrow direction is displayed according to the path creation direction.

To change the **Direction Arrow** direction

1. Right-click the association.
2. From the shortcut menu, select Reverse Direction Arrow .

The Direction Arrow is a graphical representation most often used in top-level domain class diagrams. It helps to read a diagram and explains diagram semantics, and has no meaning in a model.

Usually, you would use the Direction Arrow on a diagram where navigability is not yet defined. Direction Arrows are usually displayed for named associations. When you create more detailed diagrams with specified navigability, direction arrows and association names are not usually displayed in these types of diagrams.

As shown in the following figure, *User* and *Account* Classes are connected with the Association. A navigation arrow can be displayed on either side depending on the Association name. If the association name is *belongs to*, the Direction Arrow should point from the *Account* to the *User*. If the Association name is *has*, the Direction Arrow should point from the *User* to the *Account*.

[IMAGE alt='' src='']

###### Examples of Direction Arrows

In the [CONFLUENCE_PAGE title='Class diagram' space='MT'], you can add [CONFLUENCE_PAGE title='Attribute' space=''] to an Association using an [CONFLUENCE_PAGE title='Association Class' space='']. The Association Class is a simple [CONFLUENCE_PAGE title='Class' space='']with a dashed line connected to the Association.

##### Adding Association between Read-Only Classifiers

Adding a new Association always creates two roles or properties at both ends. They are owned by the attached Classifier by default. However, when one or both ends of the Association are not editable (for example, locked in a server project or stored in a read-only profile or used project), the properties will be ownedby the Association itself. In this case, a warning appears informing you about any unexpected issue in model creation.

1018698641

**Related pages**

- [CONFLUENCE_PAGE title='Editing property values' space='MT'] [CONFLUENCE_PAGE title='Editing property values' space='MT']
- [CONFLUENCE_PAGE title='Specification window' space='MT']
- [CONFLUENCE_PAGE title='Customizing and Selecting Perspective' space='MT']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="0079a582-0880-4a71-952d-bd6ffeac94ed"><ac:parameter ac:name="id">1018698642</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="83f8aed7-4ed4-4309-b0ca-073a1316d6de"><ac:parameter ac:name="id">1018698644</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="23a89a27-5199-4e16-be1b-89f6fab69039"><ac:parameter ac:name="id">1018698643</ac:parameter><ac:rich-text-body><p>An <ac:link><ri:page ri:content-title="Association" /><ac:plain-text-link-body><![CDATA[association]]></ac:plain-text-link-body></ac:link> is a relationship between two classes. It is represented by a solid line. Though associations are bi-directional by default, they can also be unidirectional, where one class knows about the other class and the relationship but the other class does not. Sometimes an association links a class to itself. This association is called a recursive (reflexive) association. One example of this association is an employee who is managed by a manager who is also himself an employee.</p><p>To draw a recursive (reflexive) association</p><hr /><ol><li>Select <strong>Association</strong>.</li><li>Click a class (<strong>Employee</strong> in this example) and hover over the class until you see a rectangle shape. Click the class again to create a recursive association.<br /><br /><ac:image><ri:attachment ri:filename="recursiveAssociation.png" /></ac:image></li></ol><h3>Association Properties</h3><p><span>You can specify association properties in the association <ac:link><ri:page ri:space-key="MT" ri:content-title="Specification window" /></ac:link>. T<span>he description of each property</span> appears in the same window. The description area of the Specification window presents the descriptions.</span></p><p><br /></p><p>To show the direction arrow near the association name</p><hr /><ol><li>Do one of the following:<ul><li>Right-click the association, and from the shortcut menu, select <strong>Show Direction Arrow</strong>.</li><li>Open the association <strong><ac:link><ri:page ri:space-key="MT" ri:content-title="Symbol Properties dialog" /><ac:plain-text-link-body><![CDATA[Symbol properties]]></ac:plain-text-link-body></ac:link> </strong>dialog and set the <strong>Show Direction Arrow </strong>property to <em>true</em>.</li></ul></li></ol><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="69cdb323-0d34-4a45-9e71-cee15d846a51"><ac:rich-text-body>This command is available in the Full Featured <ac:link><ri:page ri:space-key="MT" ri:content-title="Customizing and Selecting Perspective" /><ac:plain-text-link-body><![CDATA[perspective]]></ac:plain-text-link-body></ac:link>.</ac:rich-text-body></ac:structured-macro><p>The default Direction Arrow direction is displayed according to the path creation direction.</p><p><br /></p><p>To change the <strong>Direction Arrow</strong> direction</p><hr /><ol><li>Right-click the association.</li><li>From the shortcut menu, select <strong>Reverse Direction Arrow</strong>.</li></ol><p><br /></p><p>The Direction Arrow is a graphical representation most often used in top-level domain class diagrams. It helps to read a diagram and explains diagram semantics, and has no meaning in a model.</p><p>Usually, you would use the Direction Arrow on a diagram where navigability is not yet defined. Direction Arrows are usually displayed for named associations. When you create more detailed diagrams with specified navigability, direction arrows and association names are not usually displayed in these types of diagrams.</p><p>As shown in the following figure, <em>User</em> and <em>Account</em> Classes are connected with the Association. A navigation arrow can be displayed on either side depending on the Association name. If the association name is <em>belongs to</em>, the Direction Arrow should point from the <em>Account</em> to the <em>User</em>. If the Association name is <em>has</em>, the Direction Arrow should point from the <em>User</em> to the <em>Account</em>.</p><p><ac:image ac:align="center" ac:thumbnail="true" ac:height="121"><ri:attachment ri:filename="examples_of_direction_arrows.png" /></ac:image></p><h6 style="text-align: center;">Examples of Direction Arrows</h6><p><br /></p><p>In the <ac:link><ri:page ri:space-key="MT" ri:content-title="Class diagram" /></ac:link>, you can add <ac:link><ri:page ri:content-title="Attribute" /><ac:plain-text-link-body><![CDATA[Attributes]]></ac:plain-text-link-body></ac:link> to an Association using an <ac:link><ri:page ri:content-title="Association Class" /></ac:link>. The Association Class is a simple <ac:link><ri:page ri:content-title="Class" /><ac:plain-text-link-body><![CDATA[Class ]]></ac:plain-text-link-body></ac:link>with a dashed line connected to the Association.</p><h3>Adding Association between Read-Only Classifiers</h3><p><span>Adding a new Association always creates two roles or properties at both ends. They are owned by the attached Classifier by default. However, when one or both ends of the Association are not editable (for example, locked in a server project or stored in a read-only profile or used project), the properties will be owned </span>by the Association itself. In this case, a warning appears informing you about any unexpected issue in model creation.</p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="fc7af625-a400-4730-a5a3-697bcd6a94f8"><ac:parameter ac:name="id">1018698641</ac:parameter><ac:rich-text-body><p><strong>Related pages</strong></p><ul><li><ac:link><ri:page ri:space-key="MT" ri:content-title="Editing property values" /><ac:plain-text-link-body><![CDATA[Editing]]></ac:plain-text-link-body></ac:link><ac:link><ri:page ri:space-key="MT" ri:content-title="Editing property values" /><ac:plain-text-link-body><![CDATA[ Property Values]]></ac:plain-text-link-body></ac:link></li><li><ac:link><ri:page ri:space-key="MT" ri:content-title="Specification window" /></ac:link></li><li><ac:link><ri:page ri:space-key="MT" ri:content-title="Customizing and Selecting Perspective" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=243967533 space=MED version=2 -->
## PAGE 00514: Working with Classes

- page_id: `243967533`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/243967533/Working+with+Classes
- version_number: 2
- version_date: `2025-09-13T12:42:26.029+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UML elements > Class
- labels: []

### NORMALIZED CONTENT

#### CONTENT-LAYER: More Information

1408655808

#### CONTENT-COLUMN: More Information

1408655819

#### CONTENT-BLOCK: More Information

1408655809

A [CONFLUENCE_PAGE title='Class' space=''] can be defined as active (a border to the Class shape is added). An active Class specifies whether an object of the Class maintains its own thread of control.

General information about working with shapes is provided in [CONFLUENCE_PAGE title='Diagramming' space='MT'].

You can specify Class properties in the Class's Specification window. In the same window, you can find the description of each property. Descriptions are presented in the description area at the bottom of the Specification window.

#### TIP: More information

More information

- For more information about the Specification window, see the page [CONFLUENCE_PAGE title='Specification window' space='MT'] .
- For more information about specifying property values, see the page [CONFLUENCE_PAGE title='Editing property values' space='MT'] .

To insert an inner element in the selected class

1. Double-click the selected Class or select Specification from the Class's [CONFLUENCE_PAGE title='Shortcut menu' space='CDH'] . The Class's Specification window opens.
2. Click the Inner Elements tab and then click the Create button or press Insert .
3. Select the element you wish to add from the list. Click the selected element.
4. The corresponding Specification window opens. Define the Class, Use Case, or Interface, and click OK . [ATTACHMENT filename='Screen Shot 2017-06-09 at 12.30.14 AM.png']

To generate operations for setting or getting private data to the selected class

- From the Class's shortcut menu, select Tools and then Create Setters/Getters . [ATTACHMENT filename='Screen Shot 2017-06-09 at 12.32.54 AM.png']

#### TIP: More Information

More Information

For a detailed description, read [CONFLUENCE_PAGE title='Creating Setters and Getters' space='MT'].

To control a list of operations and attributes that are visible on a diagram

1. Select Edit Compartmen t from the Class's shortcut menu.
2. The Compartment Edit dialog opens. [ATTACHMENT filename='Screen Shot 2017-06-09 at 12.39.07 AM.png']

To define a class as abstract and/or active

1. Open the Class's Specification window.
2. In the General tab, select the Is Abstract , and/or Is Active check box to true .

To show members (attributes and operations) on the classifier shape according to the visibility

1. On the diagram pane, right-click the Class shape and then from the class's shortcut menu, select the Symbol Properties .
2. In the Symbol Properties dialog, change the Show Members property; the options are All, Only Public, or Not Private.

1408655807

**Related references**

true[CONFLUENCE_PAGE title='Class' space='']

**Related pages**

- [CONFLUENCE_PAGE title='Class diagram' space='MT']
- [CONFLUENCE_PAGE title='Class Diagram Wizard' space='MT']
- [CONFLUENCE_PAGE title='Behavior' space='']
- [CONFLUENCE_PAGE title='Package' space='']
- [CONFLUENCE_PAGE title='Editing property values' space='MT']
- [CONFLUENCE_PAGE title='UML elements' space='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="07ecaa37-da83-49b3-a403-3169d801b0d7"><ac:parameter ac:name="id">1408655808</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="cba10225-82d2-4a21-9f1c-507066be9bd4"><ac:parameter ac:name="id">1408655819</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="b4d1d2b6-4f45-4140-969e-d03edc6f14b6"><ac:parameter ac:name="id">1408655809</ac:parameter><ac:rich-text-body><p>A <ac:link><ri:page ri:content-title="Class" /></ac:link> can be defined as active (a border to the Class shape is added). An active Class specifies whether an object of the Class maintains its own thread of control.</p><p>General information about working with shapes is provided in <ac:link><ri:page ri:space-key="MT" ri:content-title="Diagramming" /></ac:link>.</p><p>You can specify Class properties in the Class's Specification window. In the same window, you can find the description of each property. Descriptions are presented in the description area at the bottom of the Specification window.</p><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="353a5c3b-3ae7-4c37-bd98-dac321d8c9cf"><ac:parameter ac:name="title">More information </ac:parameter><ac:rich-text-body><ul><li>For more information about the Specification window, see the page <ac:link><ri:page ri:space-key="MT" ri:content-title="Specification window" /></ac:link>.</li><li>For more information about specifying property values, see the page <ac:link><ri:page ri:space-key="MT" ri:content-title="Editing property values" /><ac:plain-text-link-body><![CDATA[Editing Property Values]]></ac:plain-text-link-body></ac:link>.</li></ul></ac:rich-text-body></ac:structured-macro><p><span><br /></span></p><p><span>To insert an inner element in the selected class</span></p><hr /><ol><li>Double-click the selected Class or select Specification from the Class's <ac:link><ri:page ri:space-key="CDH" ri:content-title="Shortcut menu" /><ac:plain-text-link-body><![CDATA[shortcut menu]]></ac:plain-text-link-body></ac:link>. The Class's Specification window opens.</li><li>Click the <strong>Inner Elements</strong> tab and then click the <strong>Create</strong> button or press <strong>Insert</strong>. </li><li>Select the element you wish to add from the list. Click the selected element.</li><li>The corresponding Specification window opens. Define the Class, Use Case, or Interface, and click <strong>OK</strong>.<br /><ac:image ac:align="center" ac:thumbnail="true" ac:width="300"><ri:attachment ri:filename="Screen Shot 2017-06-09 at 12.30.14 AM.png" /></ac:image></li></ol><p><span><br /></span></p><p><span>To generate operations for setting or getting private data to the selected class</span></p><hr /><ul><li>From the Class's shortcut menu, select <strong>Tools</strong> and then <strong>Create Setters/Getters</strong>. <br /><ac:image ac:align="center" ac:width="400"><ri:attachment ri:filename="Screen Shot 2017-06-09 at 12.32.54 AM.png" /></ac:image><br /><br /></li></ul><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="5a3dcb59-5c0e-4c58-afab-08cb5af73efa"><ac:parameter ac:name="title">More Information</ac:parameter><ac:rich-text-body><p>For a detailed description, read <ac:link><ri:page ri:space-key="MT" ri:content-title="Creating Setters and Getters" /></ac:link>. </p></ac:rich-text-body></ac:structured-macro><p><br /></p><p>To control a list of operations and attributes that are visible on a diagram</p><hr /><ol><li>Select <strong>Edit Compartmen</strong>t from the Class's shortcut menu.</li><li>The <strong>Compartment Edit</strong> dialog opens.<br /><ac:image ac:align="center" ac:width="400"><ri:attachment ri:filename="Screen Shot 2017-06-09 at 12.39.07 AM.png" /></ac:image></li></ol><p><br /></p><p>To define a class as abstract and/or active</p><hr /><ol><li>Open the Class's Specification window.</li><li>In the <strong>General</strong> tab, select the <strong>Is Abstract</strong>, and/or <strong>Is Active</strong> check box to <em>true</em>.</li></ol><p><br /></p><p>To show members (attributes and operations) on the classifier shape according to the visibility</p><hr /><ol><li>On the diagram pane, right-click the Class shape and then from the class's shortcut menu, select the <strong>Symbol Properties</strong>.</li><li>In the <strong>Symbol Properties</strong> dialog, change the <strong>Show Members</strong> property; the options are All, Only Public, or Not Private.</li></ol></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="243a1b17-5ccd-4efc-b8a1-da0d207c6cfd"><ac:parameter ac:name="id">1408655807</ac:parameter><ac:rich-text-body><p class="auto-cursor-target"><strong>Related references</strong></p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="7118b710-f736-4180-b8b7-c6a5f641c293"><ac:parameter ac:name="all">true</ac:parameter><ac:parameter ac:name="page"><ac:link><ri:page ri:content-title="Class" /></ac:link></ac:parameter></ac:structured-macro></p><p><br /></p><p><strong>Related pages</strong></p><ul><li><ac:link><ri:page ri:space-key="MT" ri:content-title="Class diagram" /></ac:link></li><li><ac:link><ri:page ri:space-key="MT" ri:content-title="Class Diagram Wizard" /></ac:link></li><li><ac:link><ri:page ri:content-title="Behavior" /></ac:link></li><li><ac:link><ri:page ri:content-title="Package" /></ac:link></li><li><ac:link><ri:page ri:space-key="MT" ri:content-title="Editing property values" /><ac:plain-text-link-body><![CDATA[Editing Property Values]]></ac:plain-text-link-body></ac:link></li><li><ac:link><ri:page ri:content-title="UML elements" /><ac:plain-text-link-body><![CDATA[Model Elements]]></ac:plain-text-link-body></ac:link></li></ul><p class="auto-cursor-target"><br /></p><p><br /></p><p class="auto-cursor-target"><br /></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=243967600 space=MED version=1 -->
## PAGE 00515: Working with Constraints

- page_id: `243967600`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/243967600/Working+with+Constraints
- version_number: 1
- version_date: `2025-07-31T10:50:36.435+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UML elements > Constraint
- labels: []

### NORMALIZED CONTENT

You can edit constraints in the **Constraints** property group of the containing element Specification window, in the constraint’s Specification window, or double click the selected constraint and edit it on the diagram pane directly.

To see the constraint expression, make sure the **Show Constraint** value is set to true, in the [CONFLUENCE_PAGE title='Symbol Properties dialog' space='MT']**Symbol Properties** dialog.

In this section, see the following procedures:

##### Defining a new constraint

To define a new constraint, do one of the following

- In the Containment Tree, from the element shortcut menu, select Create Element > Constraint .
- In the [CONFLUENCE_PAGE title='Specification window' space='MT'] , select the Inner Elements property group and click the Create button (select Constraint from the list, if needed). Specify the constraint in the constraint [CONFLUENCE_PAGE title='Specification window' space='MT'] .
- In the [CONFLUENCE_PAGE title='Specification window' space='MT'], select the **Constraints** property group and click the **Create** button. In the menu, select a duration, interaction, time, or simple constraint. The constraint [CONFLUENCE_PAGE title='Specification window' space='MT'] is displayed.
- In the diagram palette, under the Common category, expand the Constraint command and select the Duration Constraint, Time Constraint, or Constraint button and create it directly on the action shape.

If a constraint is displayed in the **Constraints** property group of the element [CONFLUENCE_PAGE title='Specification window' space='MT'], it means this constraint is applied for the element. If it is displayed in the **Inner Elements** list, this constraint is only owned by the element.

##### Editing a duration interval of the constraint

To edit the duration interval of the constraint

1. Right-click the element shape and select Specification.
2. In the Specification window, select the Constraints property group.
3. Edit the duration interval on the left side of the Specification window in the Specification column.

##### Applying an existing constraint

To apply a constraint to an element

1. In the chosen element's [CONFLUENCE_PAGE title='Specification window' space='MT'] , select the Constraints property group and click the Apply button. The Select Constraint dialog opens.
2. Select a constraint or create a new one.
3. Click OK when you are done.

#### PANEL: Related Pages

Related Pages

- [CONFLUENCE_PAGE title='UML elements' space='']
- [CONFLUENCE_PAGE title='Class diagram' space='MT']
- [CONFLUENCE_PAGE title='Use Case' space='']
- [CONFLUENCE_PAGE title='Use Case diagram' space='MT']
- [CONFLUENCE_PAGE title='Sequence diagram' space='MT']
- [CONFLUENCE_PAGE title='Activity diagram' space='MT']
- [CONFLUENCE_PAGE title='Working with Actions' space='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p>You can edit constraints in the <strong>Constraints</strong> property group of the containing element Specification window, in the constraint’s Specification window, or double click the selected constraint and edit it on the diagram pane directly.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="5cd4774f-d718-4558-a0be-70f3582fef06"><ac:rich-text-body><p>To see the constraint expression, make sure the <strong>Show Constraint</strong> value is set to true, in the <ac:link><ri:page ri:space-key="MT" ri:content-title="Symbol Properties dialog" /><ac:link-body><strong>Symbol Properties</strong> dialog</ac:link-body></ac:link>.</p></ac:rich-text-body></ac:structured-macro><p>In this section, see the following procedures:</p><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="f4b1ab44-7973-4607-ae6a-29a971acd416" /></p><h3>Defining a new constraint</h3><p>To define a new constraint, do one of the following</p><hr /><ul><li>In the Containment Tree, from the element shortcut menu, select <strong>Create Element</strong> &gt; <strong>Constraint</strong>.</li><li>In the <ac:link><ri:page ri:space-key="MT" ri:content-title="Specification window" /></ac:link>, select the <strong>Inner Elements</strong> property group and click the <strong>Create</strong> button (select Constraint from the list, if needed). Specify the constraint in the constraint <ac:link><ri:page ri:space-key="MT" ri:content-title="Specification window" /></ac:link>. </li><li><p>In the <ac:link><ri:page ri:space-key="MT" ri:content-title="Specification window" /></ac:link>, select the <strong>Constraints</strong> property group and click the <strong>Create</strong> button. In the menu, select a duration, interaction, time, or simple constraint. The constraint <ac:link><ri:page ri:space-key="MT" ri:content-title="Specification window" /></ac:link> is displayed.</p></li><li>In the diagram palette, under the Common category, expand the <strong>Constraint</strong> command and select the Duration Constraint, Time Constraint, or Constraint button and create it directly on the action shape.</li></ul><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="31f555b2-4db8-4d2c-bd5b-0e398e433712"><ac:rich-text-body><p>If a constraint is displayed in the <strong>Constraints</strong> property group of the element <ac:link><ri:page ri:space-key="MT" ri:content-title="Specification window" /></ac:link>, it means this constraint is applied for the element. If it is displayed in the <strong>Inner Elements</strong> list, this constraint is only owned by the element.</p></ac:rich-text-body></ac:structured-macro><h3>Editing a duration interval of the constraint</h3><p>To edit the duration interval of the constraint</p><hr /><ol><li>Right-click the element shape and select Specification.</li><li>In the Specification window, select the <strong>Constraints</strong> property group.</li><li>Edit the duration interval on the left side of the Specification window in the Specification column.</li></ol><h3>Applying an existing constraint</h3><p>To apply a constraint to an element</p><hr /><ol><li>In the chosen element's <ac:link><ri:page ri:space-key="MT" ri:content-title="Specification window" /></ac:link>, select the <strong>Constraints</strong> property group and click the <strong>Apply</strong> button. The <strong>Select Constraint</strong> dialog opens. </li><li>Select a constraint or create a new one.</li><li>Click <strong>OK</strong> when you are done.</li></ol></ac:layout-cell><ac:layout-cell><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="1b2025c5-70c1-47b6-9a1b-4fb242548002"><ac:parameter ac:name="title">Related Pages</ac:parameter><ac:rich-text-body><ul><li><ac:link><ri:page ri:content-title="UML elements" /><ac:plain-text-link-body><![CDATA[Model Elements]]></ac:plain-text-link-body></ac:link></li><li><ac:link><ri:page ri:space-key="MT" ri:content-title="Class diagram" /><ac:plain-text-link-body><![CDATA[Class diagrams]]></ac:plain-text-link-body></ac:link></li><li><ac:link><ri:page ri:content-title="Use Case" /></ac:link></li><li><ac:link><ri:page ri:space-key="MT" ri:content-title="Use Case diagram" /></ac:link></li><li><ac:link><ri:page ri:space-key="MT" ri:content-title="Sequence diagram" /></ac:link></li><li><ac:link><ri:page ri:space-key="MT" ri:content-title="Activity diagram" /></ac:link></li><li><ac:link><ri:page ri:content-title="Working with Actions" /><ac:plain-text-link-body><![CDATA[Applying duration constraint on the Action]]></ac:plain-text-link-body></ac:link></li></ul></ac:rich-text-body></ac:structured-macro><br /><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=243967630 space=MED version=2 -->
## PAGE 00516: Working with dependencies

- page_id: `243967630`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/243967630/Working+with+dependencies
- version_number: 2
- version_date: `2025-09-13T12:41:54.028+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UML elements > Dependency
- labels: []

### NORMALIZED CONTENT

###### Element Import

To draw the Element Import dependency

1. Open or create the [CONFLUENCE_PAGE title='Package diagram' space='MT'] .
2. In the diagram, select or create at least two packages. When using created packages, simply drag and drop the packages onto your diagram pane and name them as you wish.
3. On the Package diagram palette, expand the Package Merge button [ATTACHMENT filename='Screen Shot 2017-06-13 at 9.17.43 PM.png'] and select the Element Import button [ATTACHMENT filename='Screen Shot 2017-06-13 at 9.17.54 PM.png'] . [ATTACHMENT filename='Screen Shot 2017-06-13 at 9.33.08 PM.png']

###### Access

An Access relationship shows that elements can only be accessed from a package, and it cannot be referenced.

To draw the Access dependency

1. Open or create the Package diagram.
2. On the Package diagram palette, expand the Package Merge button [ATTACHMENT filename='Screen Shot 2017-06-13 at 9.17.43 PM.png'] and select the Package Import button [ATTACHMENT filename='Screen Shot 2017-06-13 at 9.28.54 PM.png'] .
3. Draw the dependency on your diagram pane between two packages.
4. Select the Package Import dependency, open its [CONFLUENCE_PAGE title='Specification window' space='MT'] , and set the Visibility property to private . [ATTACHMENT filename='Screen Shot 2017-06-13 at 9.31.03 PM.png']

###### Deployment

To draw a deployment relationship

1. Create a [CONFLUENCE_PAGE title='Deployment diagram' space='MT'] .
2. On the Deployment diagram pane, create a [CONFLUENCE_PAGE title='Node' space=''] and an [CONFLUENCE_PAGE title='Artifacts' space='MT'] by dragging and dropping each one onto the diagram pane.
3. Click the Deployment button [ATTACHMENT filename='Screen Shot 2017-06-13 at 9.42.33 PM.png'] and draw a deployment link from the node to the artifact. [ATTACHMENT filename='Screen Shot 2017-06-13 at 9.43.10 PM.png']

To display the deployed artifacts on the node instance shape

Do one of the following:

- On the diagram pane, select the node instance symbol, then click the Compartments button [ATTACHMENT filename='compartments.png'] (usually it is displayed on the top left corner of the symbol). In the opened menu, select the Deployed Elements .
- On the diagram pane, right-click the node instance and from the shortcut menu, select Symbol Properties . Then in the Symbol Properties dialog, set the Suppress Deployed Elements property value to false .

#### PANEL: On this page

On this page

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><h4>Element Import</h4><p><br /></p><p>To draw the Element Import dependency</p><hr /><ol><li>Open or create the <ac:link><ri:page ri:space-key="MT" ri:content-title="Package diagram" /></ac:link>.</li><li>In the diagram, select or create at least two packages. When using created packages, simply drag and drop the packages onto your diagram pane and name them as you wish.</li><li>On the Package diagram palette, expand the <strong>Package Merge</strong> button <ac:image ac:thumbnail="true" ac:width="120"><ri:attachment ri:filename="Screen Shot 2017-06-13 at 9.17.43 PM.png" /></ac:image> and select the <strong>Element Import</strong> button <ac:image ac:thumbnail="true" ac:width="120"><ri:attachment ri:filename="Screen Shot 2017-06-13 at 9.17.54 PM.png" /></ac:image>.<br /><ac:image ac:width="350"><ri:attachment ri:filename="Screen Shot 2017-06-13 at 9.33.08 PM.png" /></ac:image></li></ol><h4>Access</h4><p><span>An Access relationship shows that elements can only be accessed from a package, and it cannot be referenced. </span></p><p><span><br /></span></p><p>To draw the Access dependency</p><hr /><ol><li>Open or create the Package diagram.</li><li>On the Package diagram palette, expand the <strong>Package Merge</strong> button <ac:image ac:thumbnail="true" ac:width="120"><ri:attachment ri:filename="Screen Shot 2017-06-13 at 9.17.43 PM.png" /></ac:image>and select the <strong>Package Import</strong> button <ac:image ac:thumbnail="true" ac:width="120"><ri:attachment ri:filename="Screen Shot 2017-06-13 at 9.28.54 PM.png" /></ac:image>.</li><li>Draw the dependency on your diagram pane between two packages.</li><li>Select the <strong>Package Import</strong> dependency, open its <ac:link><ri:page ri:space-key="MT" ri:content-title="Specification window" /></ac:link>, and set the <strong>Visibility</strong> property to <em>private</em>.<br /><ac:image ac:width="350"><ri:attachment ri:filename="Screen Shot 2017-06-13 at 9.31.03 PM.png" /></ac:image></li></ol><p><br /></p><h4>Deployment</h4><p><br /></p><p>To draw a deployment relationship</p><hr /><ol><li>Create a <ac:link><ri:page ri:space-key="MT" ri:content-title="Deployment diagram" /></ac:link>.</li><li>On the Deployment diagram pane, create a <ac:link><ri:page ri:content-title="Node" /></ac:link><strong> </strong>and an <ac:link><ri:page ri:space-key="MT" ri:content-title="Artifacts" /><ac:plain-text-link-body><![CDATA[Artifact]]></ac:plain-text-link-body></ac:link> by dragging and dropping each one onto the diagram pane. </li><li>Click the <strong>Deployment</strong> button <ac:image ac:thumbnail="true" ac:width="120"><ri:attachment ri:filename="Screen Shot 2017-06-13 at 9.42.33 PM.png" /></ac:image> and draw a deployment link from the node to the artifact.<br /><ac:image ac:width="350"><ri:attachment ri:filename="Screen Shot 2017-06-13 at 9.43.10 PM.png" /></ac:image></li></ol><p><br /></p><p>To display the deployed artifacts on the <ac:inline-comment-marker ac:ref="65fa8750-165e-49f5-bdc7-d0c0694679fc">node instance shape</ac:inline-comment-marker></p><hr /><p>Do one of the following:</p><ul><li>On the diagram pane, select the node instance symbol, then click the <strong>Compartments</strong> button <ac:image><ri:attachment ri:filename="compartments.png" /></ac:image> (usually it is displayed on the top left corner of the symbol). In the opened menu, select the <strong>Deployed Elements</strong>.</li><li>On the diagram pane, right-click the node instance and from the shortcut menu, select <strong>Symbol Properties</strong>. Then in the <strong>Symbol Properties</strong> dialog, set the <strong>Suppress Deployed Elements</strong> property value to <em>false</em>.</li></ul><p><br /></p><p><br /></p></ac:layout-cell><ac:layout-cell><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="99babe36-ca57-40b6-9425-3ffa650eccbc"><ac:parameter ac:name="title">On this page</ac:parameter><ac:rich-text-body><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="26815ca3-4409-4c48-96c1-2451caaf398b" /></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=243967755 space=MED version=2 -->
## PAGE 00517: Working with Links

- page_id: `243967755`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/243967755/Working+with+Links
- version_number: 2
- version_date: `2025-09-13T12:42:26.701+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UML elements > Link
- labels: []

### NORMALIZED CONTENT

To create a link

1. Create an [CONFLUENCE_PAGE title='Object diagram' space='MT'] .
2. In the diagram pane, create two Instance shapes by dragging and dropping the element onto the diagram pane. Select any Classifier you would like.
3. Draw a Link between the two Instance shapes.
4. The Select Association dialog opens. Select Association dialogThe Select Association dialog displays associations that are created between the classifiers of the Link.
5. Select the appropriate association and click OK .
6. The Create Slots dialog opens. Select the appropriate slots and click OK .

[IMAGE alt='' src='']

###### Example of a link between two Instance shapes.

To create slots on a link

1. In the Object diagram's diagram pane, create two Instance shapes by dragging and dropping the element onto the diagram pane. Select any Classifier you would like.
2. Draw a Link between the two Instance shapes. The Select Associations dialog opens.
3. In the Select Association dialog, select the appropriate associations then click OK .
4. The Create Slots dialog opens. [ATTACHMENT filename='Screen Shot 2017-06-20 at 12.43.56 PM.png']
5. Select the slots. Create Slots dialogThe Create Slots dialog displays the roles of the association that is created between the classifiers of the Link.[IMAGE alt='' src='']
6. Click OK. [IMAGE alt='' src='']

#### NOTE: Automatic Creation of Slots on Links

Automatic Creation of Slots on Links

- The slots on the Link are created automatically only if the Automatically Create Slots of Link option is set to true . For more information, read the instructions on how to turn on automatic creation of slots in Links further on in this page.
- The slots on a Link are created automatically only when the Link references the association. For more information read on how to create a Link at the top of this page.

To turn on automatic creation of slots in links

1. In the window, click Options > Environment . The Environment Options dialog opens.
2. In the General options group, under the Editing subgroup, set the Automatically Create Slots in Link option value to true .

To display slot values on a link

1. Right-click on a Link. Select Symbol Properties . The Symbol Properties dialog opens.
2. Deselect the Suppress Slots check box, so it says false .
3. The result should look something like the figure below. [ATTACHMENT filename='Screen Shot 2017-06-20 at 1.21.41 PM.png']

#### NOTE: Suppress Slots Default Value

Suppress Slots Default Value

- The default value of the Suppress Slots option is true , that is, slots are not displayed on a Link.
- Slots on a Link are displayed in the following form: {< slot1 name > = < slot values >, < slot2 name > = <slot values> , ... }

#### TIP: Edit Compartment

Edit Compartment

You can select to display or hide an individual slot in the Compartment Edit dialog.

To open the Compartment Edit dialog

- Select the link on a diagram pane and on its [CONFLUENCE_PAGE title='Shortcut menu' space='CDH'] , click Edit Compartment > Slots.

To change a link end

1. On a diagram pane, select an end of a Link and move it to the other target.
2. The Link is connected to the other target.

#### PANEL: Related Pages

Related Pages

- [CONFLUENCE_PAGE title='UML elements' space='']
- [CONFLUENCE_PAGE title='Displaying internal structure on structured classifiers' space='MT']
- [CONFLUENCE_PAGE title='Specification window' space='MT']
- [CONFLUENCE_PAGE title='Link' space='']

#### PANEL: Related References

Related References

- [CONFLUENCE_PAGE title='Object diagram' space='MT']
- [CONFLUENCE_PAGE title='Active Validation Rules for Links' space='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p>To create a link</p><hr /><ol><li>Create an <ac:link><ri:page ri:space-key="MT" ri:content-title="Object diagram" /></ac:link>.</li><li>In the diagram pane, create two Instance shapes by dragging and dropping the element onto the diagram pane. Select any Classifier you would like.</li><li>Draw a <strong>Link</strong> between the two Instance shapes.</li><li><p class="auto-cursor-target">The Select Association dialog opens. </p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="6960344b-ab37-4e96-8380-fe363a2b9a50"><ac:parameter ac:name="title">Select Association dialog</ac:parameter><ac:rich-text-body><p>The Select Association dialog displays associations that are created between the classifiers of the Link. </p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></li><li>Select the appropriate association and click <strong>OK</strong>. </li><li>The Create Slots dialog opens. Select the appropriate slots and click <strong>OK</strong>.</li></ol><p><ac:image ac:width="600"><ri:attachment ri:filename="Screen Shot 2017-06-19 at 9.55.58 PM.png" /></ac:image></p><h6>Example of a link between two Instance shapes.</h6><p><span style="color: rgb(51,51,51);font-size: 14.0px;">To create slots on a link</span></p><hr /><ol><li>In the Object diagram's diagram pane, create two Instance shapes by dragging and dropping the element onto the diagram pane. Select any Classifier you would like.</li><li>Draw a <strong>Link</strong> between the two Instance shapes. The Select Associations dialog opens. </li><li>In the Select Association dialog, select the appropriate associations then click <strong>OK</strong>.</li><li>The Create Slots dialog opens. <br /><ac:image ac:height="250"><ri:attachment ri:filename="Screen Shot 2017-06-20 at 12.43.56 PM.png" /></ac:image></li><li><p class="auto-cursor-target">Select the slots. </p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="1c57e8b9-1020-42fa-b484-9d1e906b444d"><ac:parameter ac:name="title">Create Slots dialog</ac:parameter><ac:rich-text-body><p>The Create Slots dialog displays the roles of the association that is created between the classifiers of the Link.</p><p><ac:image ac:height="250"><ri:attachment ri:filename="Screen Shot 2017-07-07 at 3.15.09 PM.png" /></ac:image></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></li><li>Click <strong>OK. </strong><br /><strong><ac:image ac:width="600"><ri:attachment ri:filename="Screen Shot 2017-07-07 at 3.15.16 PM.png" /></ac:image></strong></li></ol><p><br /></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="7b20f00d-4291-4220-95b9-0e632c7b603d"><ac:parameter ac:name="title">Automatic Creation of Slots on Links</ac:parameter><ac:rich-text-body><ul><li><span style="color: rgb(0,0,0);">The slots on the Link are created automatically only if the </span><strong style="color: rgb(0,0,0);">Automatically Create Slots of Link</strong><span style="color: rgb(0,0,0);"> option is set to </span><em style="color: rgb(0,0,0);">true</em><span style="color: rgb(0,0,0);">. For more information, read the instructions on how to turn on automatic creation of slots in Links further on in this page.</span></li><li><span style="color: rgb(0,0,0);">The slots on a Link are created automatically only when the Link references the association. For more information read on how to create a Link at the top of this page. </span></li></ul></ac:rich-text-body></ac:structured-macro><p><br /></p><p>To turn on automatic creation of slots in links</p><hr /><ol><li>In the window, click <strong>Options</strong> &gt; <strong>Environment</strong>. The Environment Options dialog opens.</li><li>In the <strong>General</strong> options group, under the <strong>Editing</strong> subgroup, set the <strong>Automatically Create Slots in Link </strong>option value to <em>true</em>.</li></ol><p><br /></p><p>To display slot values on a link</p><hr /><ol><li>Right-click on a Link. Select <strong>Symbol Properties</strong>. The Symbol Properties dialog opens. </li><li>Deselect the <strong>Suppress Slots</strong> check box, so it says <em>false</em>.</li><li>The result should look something like the figure below. <br /><ac:image ac:width="600"><ri:attachment ri:filename="Screen Shot 2017-06-20 at 1.21.41 PM.png" /></ac:image></li></ol><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="b6ff085a-ef35-4c6a-9668-d058739a65a3"><ac:parameter ac:name="title">Suppress Slots Default Value</ac:parameter><ac:rich-text-body><ul><li>The default value of the <strong>Suppress Slots</strong> option is <em>true</em>, that is, slots are not displayed on a Link. </li><li>Slots on a Link are displayed in the following form: <em>{&lt; slot1 name &gt; = &lt; slot values &gt;, &lt; slot2 name &gt; = &lt;slot values&gt; , ... }</em></li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="44bb3319-3172-48a0-8adf-dd49b105ec82"><ac:parameter ac:name="title">Edit Compartment</ac:parameter><ac:rich-text-body><p>You can select to display or hide an individual slot in the Compartment Edit dialog.</p><p>To open the Compartment Edit dialog</p><hr /><ul><li>Select the link on a diagram pane and on its <ac:link><ri:page ri:space-key="CDH" ri:content-title="Shortcut menu" /><ac:plain-text-link-body><![CDATA[shortcut menu]]></ac:plain-text-link-body></ac:link>, click<strong> Edit Compartment </strong>&gt; <strong>Slots.</strong></li></ul></ac:rich-text-body></ac:structured-macro><p><br /></p><p>To change a link end</p><hr /><ol><li>On a diagram pane, select an end of a Link and move it to the other target. </li><li>The Link is connected to the other target.</li></ol><p><br /></p><p><br /></p></ac:layout-cell><ac:layout-cell><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="36e20852-22dd-420b-8d4b-52b136b22981"><ac:parameter ac:name="title">Related Pages</ac:parameter><ac:rich-text-body><ul><li><ac:link><ri:page ri:content-title="UML elements" /><ac:plain-text-link-body><![CDATA[Model Elements]]></ac:plain-text-link-body></ac:link></li><li><ac:link><ri:page ri:space-key="MT" ri:content-title="Displaying internal structure on structured classifiers" /><ac:plain-text-link-body><![CDATA[Classifiers]]></ac:plain-text-link-body></ac:link></li><li><ac:link><ri:page ri:space-key="MT" ri:content-title="Specification window" /><ac:plain-text-link-body><![CDATA[Specification Window]]></ac:plain-text-link-body></ac:link></li><li><ac:link><ri:page ri:content-title="Link" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="de005802-81ee-4fe1-96ef-d8e38b1ee55a"><ac:parameter ac:name="title">Related References</ac:parameter><ac:rich-text-body><ul><li><ac:link><ri:page ri:space-key="MT" ri:content-title="Object diagram" /><ac:plain-text-link-body><![CDATA[Object Diagram]]></ac:plain-text-link-body></ac:link></li><li><ac:link><ri:page ri:content-title="Active Validation Rules for Links" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=243967883 space=MED version=1 -->
## PAGE 00518: Working with packages

- page_id: `243967883`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/243967883/Working+with+packages
- version_number: 1
- version_date: `2025-07-31T10:50:43.544+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UML elements > Package
- labels: []

### NORMALIZED CONTENT

You can [CONFLUENCE_PAGE title='Editing property values' space='MT'] in the package [CONFLUENCE_PAGE title='Specification window' space='MT']. In the same window, you can find the description of each property. Descriptions are displayed in the description area of the Specification window.

You can conveniently [CONFLUENCE_PAGE title='Package import' space=''] to find the elements you're looking for in the type selection list.

The procedures below illustrate how to work with packages:

##### Adding inner elements

To add inner elements to the selected package

1. In the Package Specification window, select the Inner Elements property group.
2. Click the Create button, and select an element you wish to add. The selected element Specification window will open.
3. Define the properties you need.
4. Click Back to return to Package Specification window.

##### Changing the package header position

To change the package header position

- In the Symbol Properties dialog, set the Header Position property to:
  - Top to place a package header at the top of a package shape.
  - In Tab to place a package header in a package tab.

[IMAGE alt='' src='']

##### Showing the list of elements assigned to a package on its shape

To show the list of elements assigned to a package on the package shape

- From the selected package shortcut menu, choose Show Inner Elements List .

[IMAGE alt='' src='']

##### Displaying inner elements inside package shape

To display the inner elements of a package in a diagram

1. Select a single package shape on the diagram pane.
2. Open the Select Inner Elements dialog by doing one of the following: - From its shortcut menu, select Display > Display Inner Elements . - On the diagram toolbar, click [IMAGE alt='' src=''] and select Display Inner Elements.
3. In the dialog, select the elements that you want to display inside the package shape. [ATTACHMENT filename='select_inner_elements.png']
4. Click **OK**. 
The selected elements are displayed on the shape of the selected package. 
[IMAGE alt='' src='']

The rake icon [IMAGE alt='' src=''] is displayed on the shape if the package refers to another package diagrams. The rake icon isn’t shown by default, therefore, you need to set the **[CONFLUENCE_PAGE title='Displaying rake icon' space='MT']** property value to *true* in the **[CONFLUENCE_PAGE title='Symbol Properties dialog' space='MT']** dialog.

#### PANEL: Related Pages

Related Pages

- [CONFLUENCE_PAGE title='UML elements' space='']
- [CONFLUENCE_PAGE title='Specification window' space='MT']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p>You can <ac:link><ri:page ri:space-key="MT" ri:content-title="Editing property values" /><ac:plain-text-link-body><![CDATA[specify package properties]]></ac:plain-text-link-body></ac:link> in the package <ac:link><ri:page ri:space-key="MT" ri:content-title="Specification window" /></ac:link>. In the same window, you can find the description of each property. Descriptions are displayed in the description area of the Specification window.<br /><br /></p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="d23ac1bc-c3de-4ded-840a-6aa6cb74cd77"><ac:rich-text-body><p>You can conveniently <ac:link><ri:page ri:content-title="Package import" /><ac:plain-text-link-body><![CDATA[import packages]]></ac:plain-text-link-body></ac:link> to find the elements you're looking for in the type selection list.</p></ac:rich-text-body></ac:structured-macro><p> The procedures below illustrate how to work with packages:</p><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="ba85dbb9-5381-4bfb-bb67-b12d3c15f85b" /></p><h3>Adding inner elements</h3><p>To add inner elements to the selected package</p><hr /><ol><li>In the <strong>Package </strong>Specification window, select the<strong style="line-height: 1.42857;"> Inner Elements</strong> property group.</li><li>Click the <strong>Create</strong> button, and select an element you wish to add. The selected element Specification window will open.</li><li>Define the properties you need.</li><li>Click <strong>Back</strong> to return to <strong>Package </strong>Specification window.</li></ol><p> </p><h3>Changing the package header position</h3><p>To change the package header position</p><hr /><ul><li>In the <strong>Symbol Properties</strong> dialog, set the Header Position property to:<ul><li><strong>Top</strong> to place a package header at the top of a package shape.</li><li><strong>In Tab</strong> to place a package header in a package tab.</li></ul></li></ul><p><ac:image ac:title="Position of a package header" ac:alt="Position of a package header"><ri:attachment ri:filename="package_header_top_in_tab.png" /></ac:image></p><h3>Showing the list of elements assigned to a package on its shape</h3><p>To show the list of elements assigned to a package on the package shape</p><hr /><ul><li>From the selected package shortcut menu, choose <strong style="line-height: 1.42857;">Show Inner Elements List</strong>.</li></ul><p><ac:image ac:title="Package inner elements displayed in a package shape" ac:alt="Package inner elements displayed in a package shape"><ri:attachment ri:filename="package_inner_elements.png" /></ac:image></p><p> </p><h3>Displaying inner elements inside package shape</h3><p>To display the inner elements of a package in a diagram</p><hr /><ol><li>Select a single package shape on the diagram pane.</li><li>Open the <strong>Select Inner Elements</strong> dialog by doing one of the following:<br />- From its shortcut menu, select <strong>Display</strong> &gt; <strong>Display Inner Elements</strong>.<br />- On the diagram toolbar, click <span class="confluence-embedded-file-wrapper"><span class="confluence-embedded-file-wrapper"><ac:image ac:title="Display" ac:alt="Display"><ri:attachment ri:filename="Display.png" /></ac:image></span></span> and select <strong>Display Inner Elements.</strong></li><li><p>In the dialog, select the elements that you want to display inside the package shape.</p><ac:image ac:title="Select Inner Elements dialog" ac:alt="Select Inner Elements dialog"><ri:attachment ri:filename="select_inner_elements.png" /></ac:image></li><li><p>Click <strong>OK</strong>. <br />The selected elements are displayed on the shape of the selected package.<br /><ac:image ac:title="Package with inner elements displayed" ac:alt="Package with inner elements displayed"><ri:attachment ri:filename="package_with_inner_structure.png" /></ac:image></p></li></ol><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="62616252-0566-459a-b5a3-deedc795e33c"><ac:rich-text-body><p>The rake icon <ac:image><ri:attachment ri:filename="rake.png" /></ac:image> is displayed on the shape if the package refers to another package diagrams. The rake icon isn’t shown by default, therefore, you need to set the <strong><ac:link><ri:page ri:space-key="MT" ri:content-title="Displaying rake icon" /><ac:plain-text-link-body><![CDATA[Show Rake Icon]]></ac:plain-text-link-body></ac:link></strong> property value to <em>true</em> in the <strong><ac:link><ri:page ri:space-key="MT" ri:content-title="Symbol Properties dialog" /><ac:plain-text-link-body><![CDATA[Symbol Properties]]></ac:plain-text-link-body></ac:link></strong> dialog.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell><ac:layout-cell><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="36e20852-22dd-420b-8d4b-52b136b22981"><ac:parameter ac:name="title">Related Pages</ac:parameter><ac:rich-text-body><ul><li><ac:link><ri:page ri:content-title="UML elements" /><ac:plain-text-link-body><![CDATA[Model Elements]]></ac:plain-text-link-body></ac:link></li><li><ac:link><ri:page ri:space-key="MT" ri:content-title="Specification window" /><ac:plain-text-link-body><![CDATA[Specification Window]]></ac:plain-text-link-body></ac:link></li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=243968019 space=MED version=2 -->
## PAGE 00519: Working with Template

- page_id: `243968019`
- space_key: `MED`
- source_url: https://docs.nomagic.com/spaces/MED/pages/243968019/Working+with+Template
- version_number: 2
- version_date: `2025-09-13T12:44:17.071+02:00`
- ancestors: SysML v1/UAF/UML Model Element Descriptions > UML elements > Template
- labels: []

### NORMALIZED CONTENT

#### CONTENT-LAYER: Value Specification

502685492

#### CONTENT-COLUMN: Value Specification

502685495

#### CONTENT-BLOCK: Value Specification

502685494

This section demonstrates how to create a template and how to use it.

Follow these instructions from the first step consistently. If you do not, and if you do not define the template parameter, you will not be able to draw a template binding relationship. You can omit optional procedures only.

#### INFO: Precondition

Precondition

Let’s assume you already have an element to which you want to apply a template. This element is an actual element. The actual element can be a classifier, package, or operation.

To create and apply a template to an actual element, see the following procedures:

- 
- 

In the following procedures, we will show you how to create a template with parameters and how to define these parameters.

TemplateTo create a template

1. Create or select a template element for which you will create template parameters.
2. Open the element's [CONFLUENCE_PAGE title='Specification window' space='MT'].
3. Change the property display mode to**All**,if it is not changed already. The**Template Parameters** property group appears in the property group list.
4. Click the Template Parameters property group.
5. To add a new template parameter, click the Create button. The Select Template Parameter Type dialog opens. [ATTACHMENT filename='template_select_element.png']
6. In the Model tree, select an existing or create a new type of the template parameter. Template ParameterIf you do not want to specify the concrete template parameter type, you can select the*Class*type (the*Class*from the UML metamodel). When the*Class*type is specified, type is not displayed on the diagram pane. Only the name of the template parameter is represented.If you need to select one of the UML metamodel elements, such as *Class*, be sure to clear the **Hide Uncommon Elements** and **Exclude Used Projects** commands (as in the preceding figure). For more information, read [CONFLUENCE_PAGE title='Selecting elements' space='MT'].
7. Click OK . The template parameter is created. The name of the template parameter is defined automatically by compounding the T letter and the name of the template parameter type - T<type name> . For example, TInteger . You can change the name of the template parameter if you need to. [ATTACHMENT filename='template_parameter.png']
8. (Optional) Assign the default value to the created template parameter. More InformationFor more information about symbol representation properties, see [CONFLUENCE_PAGE title='Formatting symbols' space='MT']. Value SpecificationTo assign a particular value of the value specification, you must specify a Value Specification first and then type its particular value in the Actual value cell. For more information about Value Specification, read [CONFLUENCE_PAGE title='Value Specification' space=''].

After the template is created, you can apply it to the actual element. The following procedures describe how to apply the template to the actual element.

ApplyTo apply a template to an actual element

1. Bind the actual element to the template element. In the diagram palette, click the **Template Binding** button in the Class diagram group or click the **B** shortcut key and draw a template binding relationship from the actual element to the template element. If the **Template Binding** button is not visible, change the the modeling tool's perspective to Full Featured or Software Architect. See the [CONFLUENCE_PAGE title='Customizing and Selecting Perspective' space='MT'] page on how to change the perspective.
2. Define a template parameter substitution. Open the Template Binding Specification window and click the Template Parameter Substitutions property group.
3. To add a new template parameter substitution, click the Create button. The Select Template Parameter dialog opens, listing the template parameters of the element to which the template binding relationship is connected. [ATTACHMENT filename='select_template_parameter.png']
4. Select one or more template parameters to add as template parameter substitutions. Click OK to return to the Template Binding Specification window. [ATTACHMENT filename='template_binding_specification_window.png']
5. (Optional) Assign the actual value for each template parameter substitution. More InformationFor more information about specifying property values, see [CONFLUENCE_PAGE title='Editing property values' space='MT']. Value SpecificationTo assign a particular value of the value specification, you must specify a Value Specification first and then type its particular value in the Actual value cell. For more information about Value Specification, read [CONFLUENCE_PAGE title='Value Specification' space=''].

502685491

**Related pages**

- Model elements
- Auxiliary Diagram Symbols
- Diagramming

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="381d5bd2-a4e0-4331-a9e6-f4b632bd6804"><ac:parameter ac:name="id">502685492</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="5435861c-9233-4416-9a2a-6b18a75489c4"><ac:parameter ac:name="id">502685495</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="c08be011-88c7-4de5-a3c7-2d60a106ca16"><ac:parameter ac:name="id">502685494</ac:parameter><ac:rich-text-body><ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p><span>This section demonstrates how to create a template and how to use it. </span></p><p><span>Follow these instructions from the first step consistently. If you do not, and if you do not define the template parameter, you will not be able to draw a template binding relationship. You can omit optional procedures only. </span></p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="8ebfea3f-5c09-4bf3-b02d-5ea5a92a9871"><ac:parameter ac:name="title">Precondition</ac:parameter><ac:rich-text-body><p>Let’s assume you already have an element to which you want to apply a template. This element is an actual element. The actual element can be a classifier, package, or operation.</p></ac:rich-text-body></ac:structured-macro><p>To create and apply a template to an actual element, see the following procedures:</p><ul><li><ac:link ac:anchor="Templat"><ac:plain-text-link-body><![CDATA[To create a template]]></ac:plain-text-link-body></ac:link></li><li><ac:link ac:anchor="Appl"><ac:plain-text-link-body><![CDATA[To apply a template to an actual element]]></ac:plain-text-link-body></ac:link></li></ul><p>In the following procedures, we will show you how to create a template with parameters and how to define these parameters. </p><p><span><br /></span></p><p><span><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="9663d288-04f5-47d5-b742-5988d8046286"><ac:parameter ac:name="">Template</ac:parameter></ac:structured-macro>To create a template</span></p><hr /><ol><li><span>Create or select a template element for which you will create template parameters.</span></li><li><span>Open the element's <ac:link><ri:page ri:space-key="MT" ri:content-title="Specification window" /></ac:link>.</span></li><li><p class="auto-cursor-target"><span>Change the property display mode to </span><span><strong>All</strong>, </span><span>if it is not changed already. The </span><strong>Template Parameters</strong> property group appears in the property group list.</p></li><li>Click the <strong>Template Parameters </strong>property group. </li><li>To add a new template parameter, click the <strong>Create</strong> button. The <strong>Select Template Parameter Type</strong> dialog opens. <br /><ac:image><ri:attachment ri:filename="template_select_element.png" /></ac:image></li><li><p class="auto-cursor-target">In the Model tree, select an existing or create a new type of the template parameter.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="0b3e0567-f715-4b59-8a74-c2b665cce15b"><ac:parameter ac:name="title">Template Parameter </ac:parameter><ac:rich-text-body><p><span>If you do not want to specify the concrete template parameter type, you can select the </span><em>Class </em><span>type (the </span><em>Class </em><span>from the UML metamodel). When the </span><em>Class </em><span>type is specified, type is not displayed on the diagram pane. Only the name of the template parameter is represented. </span></p><p>If you need to select one of the UML metamodel elements, such as <em>Class</em>, be sure to clear the <strong>Hide Uncommon Elements</strong> and <strong>Exclude Used Projects</strong> commands (as in the preceding figure). For more information, read <ac:link><ri:page ri:space-key="MT" ri:content-title="Selecting elements" /><ac:plain-text-link-body><![CDATA[Searching for elements in the Element Selection dialog]]></ac:plain-text-link-body></ac:link>.</p></ac:rich-text-body></ac:structured-macro></li><li>Click <strong>OK</strong>. The template parameter is created. The name of the template parameter is defined automatically by compounding the <em>T</em> letter and the name of the template parameter type - <em>T&lt;type name&gt;</em>. For example, <em>TInteger</em>. You can change the name of the template parameter if you need to. <br /><ac:image><ri:attachment ri:filename="template_parameter.png" /></ac:image></li><li><p class="auto-cursor-target">(Optional) Assign the default value to the created template parameter.</p><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="296c0e33-4fa7-44ce-a622-df6e1ea25d0b"><ac:parameter ac:name="title">More Information</ac:parameter><ac:rich-text-body><p>For more information about symbol representation properties, see <ac:link><ri:page ri:space-key="MT" ri:content-title="Formatting symbols" /><ac:plain-text-link-body><![CDATA[Formatting Symbols]]></ac:plain-text-link-body></ac:link>.</p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="c5f793e9-95cf-4e1e-9064-692a0c8311e2"><ac:parameter ac:name="title">Value Specification</ac:parameter><ac:rich-text-body><p>To assign a particular value of the value specification, you must specify a Value Specification first and then type its particular value in the Actual value cell. For more information about Value Specification, read <ac:link><ri:page ri:content-title="Value Specification" /></ac:link>.</p></ac:rich-text-body></ac:structured-macro></li></ol><p>After the template is created, you can apply it to the actual element. The following procedures describe how to apply the template to the actual element. </p><p><br /></p><p><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="f5215c6d-e8b1-4969-bcf0-58024c898108"><ac:parameter ac:name="">Apply</ac:parameter></ac:structured-macro>To apply a template to an actual element</p><hr /><ol><li><p>Bind the actual element to the template element. In the diagram palette, click the <strong>Template Binding</strong> button in the Class diagram group or click the <strong>B</strong> shortcut key and draw a template binding relationship from the actual element to the template element.<span style="color: rgb(114,126,148);"> <br /></span></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="1911d033-9528-4b79-81e9-eb694eb33b34"><ac:rich-text-body><p>If the <strong>Template Binding</strong> button is not visible, change the the modeling tool's perspective to Full Featured or Software Architect. See the <ac:link><ri:page ri:space-key="MT" ri:content-title="Customizing and Selecting Perspective" /></ac:link> page on how to change the perspective.</p></ac:rich-text-body></ac:structured-macro></li><li>Define a template parameter substitution. Open the Template Binding Specification window and click the <strong>Template Parameter Substitutions</strong> property group.</li><li>To add a new template parameter substitution, click the <strong>Create</strong> button. The Select Template Parameter dialog opens, listing the template parameters of the element to which the template binding relationship is connected.<br /><ac:image><ri:attachment ri:filename="select_template_parameter.png" /></ac:image></li><li>Select one or more template parameters to add as template parameter substitutions. Click <strong>OK</strong> to return to the Template Binding Specification window.<br /><ac:image><ri:attachment ri:filename="template_binding_specification_window.png" /></ac:image></li><li><p class="auto-cursor-target">(Optional) Assign the actual value for each template parameter substitution.</p><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="02202a08-01b8-4664-b9d1-3104c6e4ecc5"><ac:parameter ac:name="title">More Information</ac:parameter><ac:rich-text-body><p><span style="color: rgb(0,0,0);">For more information about specifying property values, see <ac:link><ri:page ri:space-key="MT" ri:content-title="Editing property values" /></ac:link>.</span></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="ea14beb8-bd7a-4b70-96bd-40c90f9add51"><ac:parameter ac:name="title">Value Specification</ac:parameter><ac:rich-text-body><p>To assign a particular value of the value specification, you must specify a Value Specification first and then type its particular value in the Actual value cell. For more information about Value Specification, read <ac:link><ri:page ri:content-title="Value Specification" /></ac:link>.</p></ac:rich-text-body></ac:structured-macro></li></ol></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p><br /></p></ac:layout-cell><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section></ac:layout></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="a6f97ff2-7bdf-46e0-b57f-7a0c9cbe2196"><ac:parameter ac:name="id">502685491</ac:parameter><ac:rich-text-body><p><strong>Related pages</strong></p><ul><li class="ancestor-link"><a href="https://docs.nomagic.com/display/MT/Model+elements" rel="nofollow">Model elements</a></li><li class="ancestor-link parent-link"><a href="https://docs.nomagic.com/display/MT/Auxiliary+diagram+symbols" rel="nofollow">Auxiliary Diagram Symbols</a></li><li><a href="https://docs.nomagic.com/display/MT/Diagramming" rel="nofollow">Diagramming</a></li></ul></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````
