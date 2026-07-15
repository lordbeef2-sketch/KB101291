# NI DOCUMENT BUNDLE: g-web-development

<!--NI_BUNDLE_CHUNK bundle=g-web-development start=251 end=377 -->
<!--NI_TOPIC bundle=g-web-development path=palette-taxonomy-api.html language=enus -->
## TOPIC 00251: Palette Taxonomy for Distributed APIs

- bundle_id: `g-web-development`
- source_path: `palette-taxonomy-api.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/palette-taxonomy-api.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Refer to the following table for best practices for palette taxonomy. Guideline Required or Recommended? Details Example(s) Make the root palette easy to browse. Recommended Seven to 10 categories allows for full-size icons in a single-column layout. N/A Design a structure that can expand beyond the

### Palette Taxonomy for Distributed APIs

Refer to the following table for best practices for palette taxonomy.

| Guideline | Required or Recommended? | Details | Example(s) |
| --- | --- | --- | --- |
| Make the root palette easy to browse. | Recommended | Seven to 10 categories allows for full-size icons in a single-column layout. | N/A |
| Design a structure that can expand beyond the original size of the root palette for nodes you may develop in the future. | Recommended | N/A | N/A |
| Make palettes for similar categories consistent. | Recommended | N/A | Across different palettes, such as numeric, string, file, and so on, that have a constants palette, similarly organize all the constants palettes. |
| Add synonyms or keywords to your palettes to improve the findability of your VIs. | Recommended | N/A | Mathematicians commonly refer to the functionality of the Quotient and Remainder node as mod. Make sure mod is a keyword for Quotient and Remainder so that a search for mod returns that node. |

Parent topic:

Best Practices for Designing and Developing an Application Programming Interface (API) in G Web Development Software

Parent topic:

Best Practices for Designing and Developing an Application Programming Interface (API) in G Web Development Software

Related concepts:

- Best Practices for Designing and Developing an Application Programming Interface (API) in G Web Development Software

<!--NI_TOPIC bundle=g-web-development path=panel-container-lvmember.html language=enus -->
## TOPIC 00252: Panel Container

- bundle_id: `g-web-development`
- source_path: `panel-container-lvmember.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/panel-container-lvmember.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Display the panel of a running VI in the panel of the current VI.

### Panel Container

Display the panel of a running VI in the panel of the current VI.

Parent topic:

Creating User Interfaces

<!--NI_TOPIC bundle=g-web-development path=panel-design-lv-projects.html language=enus -->
## TOPIC 00253: Panel Design for G Web Development Software Projects

- bundle_id: `g-web-development`
- source_path: `panel-design-lv-projects.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/panel-design-lv-projects.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Refer to the following table for best practices for designing panels in the G Web Development Software. Guideline Required or Recommended? Details Example(s) Avoid using all capital letters in labels or panel documentation. Recommended Capital letters can make text seem more important than necessary

### Panel Design for G Web Development Software
 Projects

Refer to the following table for best practices for designing panels in the G Web
 Development Software.

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

<!--NI_TOPIC bundle=g-web-development path=parts-manager.html language=enus -->
## TOPIC 00254: Parts Manager

- bundle_id: `g-web-development`
- source_path: `parts-manager.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/parts-manager.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Toggle the plot legend, cursor legend, graph tools, and label on or off.

### Parts Manager

Toggle the plot legend, cursor legend, graph tools, and label on or off.

Parent topic:

Creating User Interfaces

<!--NI_TOPIC bundle=g-web-development path=path-control.html language=enus -->
## TOPIC 00255: Path Control

- bundle_id: `g-web-development`
- source_path: `path-control.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/path-control.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Enter the location of a file or directory.

### Path Control

Enter the location of a file or directory.

Parent topic:

Creating User Interfaces

<!--NI_TOPIC bundle=g-web-development path=path-indicator.html language=enus -->
## TOPIC 00256: Path Indicator

- bundle_id: `g-web-development`
- source_path: `path-indicator.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/path-indicator.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Display the location of a file or directory.

### Path Indicator

Display the location of a file or directory.

Parent topic:

Creating User Interfaces

<!--NI_TOPIC bundle=g-web-development path=path-tool-drawing-controls.html language=enus -->
## TOPIC 00257: Path Tool For Drawing Controls

- bundle_id: `g-web-development`
- source_path: `path-tool-drawing-controls.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/path-tool-drawing-controls.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: A line or shape. When you select this line or shape on the panel, a tool appears that allows you to edit the drawing. Use the tool to add points, remove points, or convert between line segments and Bezier by clicking on an anchor point. This tool is not available for lines and shapes in the icon vie

### Path Tool For Drawing Controls

A line or shape.

When you select this line or shape on the panel, a tool appears that allows you to edit the drawing. Use the tool to add points, remove points, or convert between line segments and Bezier by clicking on an anchor point. This tool is not available for lines and shapes in the icon view.

Parent topic:

Creating User Interfaces

<!--NI_TOPIC bundle=g-web-development path=path.html language=enus -->
## TOPIC 00258: Path

- bundle_id: `g-web-development`
- source_path: `path.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/path.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: A line or shape. Select a line or shape on the panel and use the tool that appears to edit the drawing. Click on anchor points to add points, remove points, or convert between line segments and Bezier. This tool is not available for lines and shapes in the icon view.

### Path

A line or shape. Select a line or shape on the panel and use the tool that appears to edit
 the drawing. Click on anchor points to add points, remove points, or convert between line
 segments and Bezier. This tool is not available for lines and shapes in the icon view.

Parent topic:

Data Types Palette

<!--NI_TOPIC bundle=g-web-development path=paths.html language=enus -->
## TOPIC 00259: Path

- bundle_id: `g-web-development`
- source_path: `paths.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/paths.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Combines two or more shape controls.

### Path

Combines two or more shape controls.

Parent topic:

Creating User Interfaces

<!--NI_TOPIC bundle=g-web-development path=pause-icon-editor.html language=enus -->
## TOPIC 00260: Pause

- bundle_id: `g-web-development`
- source_path: `pause-icon-editor.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/pause-icon-editor.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Add a pause symbol to the icon.

### Pause

Add a pause symbol to the icon.

Parent topic:

Actions Palette

<!--NI_TOPIC bundle=g-web-development path=pen.html language=enus -->
## TOPIC 00261: Pen

- bundle_id: `g-web-development`
- source_path: `pen.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/pen.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Draw a line one point at a time.

### Pen

Draw a line one point at a time.

Parent topic:

Drawing Controls

<!--NI_TOPIC bundle=g-web-development path=pencil.html language=enus -->
## TOPIC 00262: Pencil

- bundle_id: `g-web-development`
- source_path: `pencil.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/pencil.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Draw a freeform line.

### Pencil

Draw a freeform line.

Parent topic:

Drawing Controls

<!--NI_TOPIC bundle=g-web-development path=pentagon-icon-editor.html language=enus -->
## TOPIC 00263: Pentagon

- bundle_id: `g-web-development`
- source_path: `pentagon-icon-editor.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/pentagon-icon-editor.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Create a customizable pentagon.

### Pentagon

Create a customizable pentagon.

Parent topic:

Shapes Palette

<!--NI_TOPIC bundle=g-web-development path=pf-tr.html language=enus -->
## TOPIC 00264: Preview Features

- bundle_id: `g-web-development`
- source_path: `pf-tr.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/pf-tr.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `task`
- source_description: Preview features are new features in G Web Development Software that support specific workflows. They are release-quality features, but they have functionality gaps and are only supported for specific uses. Preview features in G Web Development Software: do not change compilation or execution of exi

### Preview Features

Preview features are new features in G Web Development Software that support
 specific workflows. They are release-quality features, but they have functionality gaps and
 are only supported for specific uses. Preview features in G Web Development
 Software:

- do not change compilation or execution of existing code.
- do not change the persistence of existing files.
- have supporting documentation. You can also request support at ni.com/support.

File

»

Preferences

»

Preview features

Restart software for the changes to take effect.

Parent topic:

Getting Started with G Web Development Software

Related concepts:

- Getting Started with G Web Development Software

Related information:

- NI Support

<!--NI_TOPIC bundle=g-web-development path=picture-display-lvmember.html language=enus -->
## TOPIC 00265: Picture Display

- bundle_id: `g-web-development`
- source_path: `picture-display-lvmember.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/picture-display-lvmember.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Create a list of pictures that you can choose from to display on the user interface.

### Picture Display

Create a list of pictures that you can choose from to display on the user
 interface.

Parent topic:

Drawing Controls

<!--NI_TOPIC bundle=g-web-development path=pitch.html language=enus -->
## TOPIC 00266: Pitch

- bundle_id: `g-web-development`
- source_path: `pitch.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/pitch.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Increase to nose up, decrease to nose down.

### Pitch

Increase to nose up, decrease to nose down.

Parent topic:

Creating User Interfaces

<!--NI_TOPIC bundle=g-web-development path=placeholder-tunnel.html language=enus -->
## TOPIC 00267: Placeholder Tunnel

- bundle_id: `g-web-development`
- source_path: `placeholder-tunnel.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/placeholder-tunnel.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: A placeholder tunnel that replaces a tunnel type not currently supported in this version of the software.

### Placeholder Tunnel

A placeholder tunnel that replaces a tunnel type not currently supported in this version of the software.

Parent topic:

Creating User Interfaces

<!--NI_TOPIC bundle=g-web-development path=plot-legend.html language=enus -->
## TOPIC 00268: Plot Legend

- bundle_id: `g-web-development`
- source_path: `plot-legend.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/plot-legend.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Define the color and style of plots.

### Plot Legend

Define the color and style of plots.

Parent topic:

Creating User Interfaces

<!--NI_TOPIC bundle=g-web-development path=plots.html language=enus -->
## TOPIC 00269: Plots

- bundle_id: `g-web-development`
- source_path: `plots.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/plots.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configure an existing plot or add a new plot.

### Plots

Configure an existing plot or add a new plot.

Parent topic:

Creating User Interfaces

<!--NI_TOPIC bundle=g-web-development path=plus-icon-editor.html language=enus -->
## TOPIC 00270: Plus

- bundle_id: `g-web-development`
- source_path: `plus-icon-editor.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/plus-icon-editor.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Create a customizable plus.

### Plus

Create a customizable plus.

Parent topic:

Shapes Palette

<!--NI_TOPIC bundle=g-web-development path=predefined-cli-operations.html language=enus -->
## TOPIC 00271: Predefined Command Line Operations

- bundle_id: `g-web-development`
- source_path: `predefined-cli-operations.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/predefined-cli-operations.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `concept`
- source_description: The command line interface supports the following operations:

### Predefined Command Line Operations

The command line interface supports the following operations:

- [build-application](build-application.html) Builds the specified application into a binary.
- [build-library](build-library.html) Builds the specified library into a binary.
- [optimize-project](optimize-project.html) Improves the load time and performance of your projects by loading, compiling, and saving project files during the build process.
- [distribution](distribution.html) Builds a distribution(.lvdist) file.
- [applylicensing](applylicensing.html) Applies licensing to a component.

Parent topic:

Developing a Web Application

<!--NI_TOPIC bundle=g-web-development path=prepare-your-js-code.html language=enus -->
## TOPIC 00272: Preparing Your Code For Use With a JavaScript Library Interface

- bundle_id: `g-web-development`
- source_path: `prepare-your-js-code.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/prepare-your-js-code.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `task`
- source_description: Create wrapper code, if necessary, to make your JavaScript functions compatible with the JavaScript Library Interface (JSLI). Before you begin, create a web application and acquire a JavaScript library or find a global, built-in browser function you want to use. Determine if you need to create wrapp

### Preparing Your Code For Use With a JavaScript Library Interface

Create wrapper code, if necessary, to make your JavaScript functions compatible with the JavaScript Library Interface (JSLI).

Before you begin, create a web
 application and acquire a JavaScript library or find a global, built-in browser function you
 want to use.

1. Determine if you need to create wrapper code. 
 When calling JavaScript functions in your web application, you may need to create wrapper code to make your JavaScript code compatible with the JSLI. The following table contains common examples of when to create wrapper code and descriptions of the wrapper code to create. 
 SituationSolutionYou need to call functions that use or return unsupported data types. JSLIs currently support the following data types:booleansstringsnumerics 
 8-bit signed integer16-bit signed integer32-bit signed integer8-bit unsigned integer16-bit unsigned integer32-bit unsigned integerSingle-precision, floating-point numericDouble-precision, floating-point numericJavaScript references1D array of numerics (represented as a TypedArray)1D array of JavaScript references (represented as Array of JavaScript values)Create wrapper functions that convert between unsupported JavaScript types and types supported by the JSLI.You need to use the 
 new operator to create an instance of an object or you need to invoke a method on an instance of an object.Complete the following steps: 
 Create a wrapper function that invokes the 
 new operator and stores a reference to the new object instance.Create a wrapper function that looks up the reference to that object and invokes a method.
2. Create wrapper code for your JavaScript library. NI recommends you create one JavaScript file per JSLI document that contains all the wrapper functions you create. 
 Model the following code as a best practice for creating wrapper code. Customize the following code for your unique programming goals.
 /*1*/
(function () {
 'use strict'; /*2*/

 var counter = 1; /*3*/

 /*4*/
 var logWithCount = function (message){
 console.log(counter + ' > ' + message); /*5*/
 return counter++; /*6*/
 };

 window.logWithCount = logWithCount; /*7*/ 
}());
 
 [IMAGE alt='image' src='GUID-97140CE0-AE0F-45D2-BC12-D22F4BA789B6-a5.svg']
 Wrap the contents of the entire wrapper JavaScript file in an immediately invoked function expression (IIFE). The IIFE creates a new lexical scope which prevents you from unintentionally adding objects to the global scope.
 [IMAGE alt='image' src='GUID-245F4F1B-3FBD-425A-A6D9-4F445ABFE629-a5.svg']
 Configure the IIFE to use JavaScript strict mode. Strict mode improves error handling and allows browsers to make certain optimizations.
 [IMAGE alt='image' src='GUID-EE38CAD4-C25C-4C69-A3B4-5FD829627100-a5.svg']
 Create a private variable by declaring it within the IIFE. In this example, the private variable is named 
 counter. Because this variable is private, it cannot be unintentionally modified by other code. This variable is not accessible to the JSLI because you did not add it to the global scope.
 [IMAGE alt='image' src='GUID-1C2B5505-1271-4422-8DB9-8B9B5154C5C4-a5.svg']
 Create a new function and add the desired parameters to the function. In this example, we create a function named 
 logWithCount that passes a parameter to a built-in browser function named 
 console.log.
 [IMAGE alt='image' src='GUID-1CED6939-5ED1-4388-BEB8-FFF164BED4D0-a5.svg']
 Call the function you are wrapping, in this example, the 
 console.log function.
 [IMAGE alt='image' src='GUID-F2CDD9BB-5D12-4E8D-8D71-2A02539C495D-a5.svg']
 Return a value from your wrapper function. If you configure the return parameter in the JSLI document to be of a type other than void, you must pass a return value of the type you configured in the JSLI document to the return statement.
 [IMAGE alt='image' src='GUID-91842EB6-EE23-4D5B-977F-495F8F2BE07D-a5.svg']
 Add the function you want to call in your web application to the global scope to allow the JSLI document to access the function. In this example, we use the 
 logWithCount function. In a web browser, the name of the global object is 
 window, so the code 
 window.logWithCount = logWithCount; places 
 logWithCount on the global scope.

Parent topic:

Calling JavaScript Functions in a Web Application

Related tasks:

- Defining Calls to JavaScript Functions using a JavaScript Library Interface

Related reference:

- JavaScript Resources

<!--NI_TOPIC bundle=g-web-development path=probes.html language=enus -->
## TOPIC 00273: Using Probes to Check Values on a Wire

- bundle_id: `g-web-development`
- source_path: `probes.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/probes.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `concept`
- source_description: When your WebVI is running in the editor environment, you may want to check the values on the wires to determine if and where any unexpected data occurs. To place a probe on a wire, right-click on the wire and select Add Probe. A probe displays the data from the wire it is on. To view a probe in a t

### Using Probes to Check Values on a Wire

When your WebVI is running in the editor environment, you may want to check the values on the wires to determine if and where any unexpected data occurs.

To place a probe on a wire, right-click on the wire and select Add Probe. 
 A probe displays the data from the wire it is on. To view a probe in a temporary overlay on the diagram, hover over the probe marker on a wire. 
 If desired, you can then click the Pin button to keep this probe visible. From the Options drop-down you can choose the different display styles and also remove the probe, as required.

[IMAGE alt='image' src='GUID-73E4A4B9-F004-4F26-8B5B-047C216429E9-a5.png']

You can also find probes in the Debugging tab on the left side of the editor environment. The order in the list correlates with the numbers in the probe markers on the wires.

Probes display the most recent value carried by a wire. You can hover over the probes in the list and observe the tip strip that specifies when the value was last updated.

The values displayed in the probe list are limited to a line of text. However, you can hover over a probe and click the > button to display an expanded view of the probe and the Options drop-down.

Parent topic:

Testing and Debugging

<!--NI_TOPIC bundle=g-web-development path=programmatically-generated-events.html language=enus -->
## TOPIC 00274: Programmatically Generated Events

- bundle_id: `g-web-development`
- source_path: `programmatically-generated-events.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/programmatically-generated-events.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `concept`
- source_description: Programmatically generated events are events that occur as a result of the execution of diagram code. A user event is a type of programmatically generated event. Unlike user interface events, which require direct user interaction with front panel objects, user events allow you to create an applicati

### Programmatically Generated Events

Programmatically generated events are events that occur as a result of the execution of diagram code.

Unlike user interface events, which require direct user interaction with front panel objects, user events allow you to create an application that responds to programmatic changes on objects.

Event Structure

1. Create the event using the Create User Event node.
2. Register for the event using the Register for Events node.
3. Enable the dynamic event terminals on the Event Structure .

Programmatically generated events communicate among different parts of the program that have no dataflow dependency. For example, one part of an application may run a continuous loop to monitor a temperature sensor and generate a user event when the sensor reaches an alarm level. In a different part of the same application, an Event Structure executes to handle both the user event generated when the sensor reaches the alarm level and a user interface event that the Event Structure handles to notify the user of the alarm condition. Handling both user interface events and programmatically generated events in the same Event Structure allows you to implement more advanced architectures, such as queued state machines using events.

Parent topic:

Event-Driven Programming

<!--NI_TOPIC bundle=g-web-development path=progress-bar.html language=enus -->
## TOPIC 00275: Progress Bar

- bundle_id: `g-web-development`
- source_path: `progress-bar.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/progress-bar.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Display progress in a horizontal bar.

### Progress Bar

Display progress in a horizontal bar.

Parent topic:

Creating User Interfaces

<!--NI_TOPIC bundle=g-web-development path=radial-progress-bar.html language=enus -->
## TOPIC 00276: Radial Progress Bar

- bundle_id: `g-web-development`
- source_path: `radial-progress-bar.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/radial-progress-bar.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Display progress in a circle.

### Radial Progress Bar

Display progress in a circle.

Parent topic:

Creating User Interfaces

<!--NI_TOPIC bundle=g-web-development path=radio-button-group.html language=enus -->
## TOPIC 00277: Radio Button Group

- bundle_id: `g-web-development`
- source_path: `radio-button-group.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/radio-button-group.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Create a list of mutually exclusive options.

### Radio Button Group

Create a list of mutually exclusive options.

Parent topic:

Creating User Interfaces

<!--NI_TOPIC bundle=g-web-development path=read-icon-editor.html language=enus -->
## TOPIC 00278: Read

- bundle_id: `g-web-development`
- source_path: `read-icon-editor.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/read-icon-editor.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Add a read symbol to the icon.

### Read

Add a read symbol to the icon.

Parent topic:

Actions Palette

<!--NI_TOPIC bundle=g-web-development path=recommendations-build-web-app-library.html language=enus -->
## TOPIC 00279: Recommendations for Building a Web Application Library

- bundle_id: `g-web-development`
- source_path: `recommendations-build-web-app-library.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/recommendations-build-web-app-library.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `concept`
- source_description: Consider the following recommendations when building a reusable library for your web application. Use VIs (.gvi) instead of WebVIs (.gviweb)—Use a WebVI as the top-level VI in your web application and VIs with the .gvi file extension for all other VIs and libraries. Using VIs with the .gvi file exte

### Recommendations for Building a Web Application
 Library

Consider the following recommendations when building a reusable library for your web
 application.

[IMAGE alt='image' src='GUID-7F88CA90-94E3-4EE1-A47B-A66D21061DA9-a5.png']

1. Use VIs (.gvi) instead of WebVIs (.gviweb)—Use a WebVI as the top-level VI in your
 web application and VIs with the .gvi file extension for all other VIs and
 libraries. Using VIs with the .gvi file extension enables you to use your libraries
 across targets.
2. Wrap JavaScript Library Interface (JSLI) nodes in VI (.gvi) files and uncheck
 Export for JSLI documents—Rather than exporting nodes
 defined in the JSLI document, wrap the nodes in VI (.gvi) files and ensure they are
 not accessible outside of the library. The wrapper VI isolates the JSLI nodes from
 the library user, giving you the flexibility to add functionality, such as
 supporting additional data types or having multiple outputs.
3. Put JavaScript resources and JSLI in a support namespace—Use a separate namespace
 for JavaScript resources, such as CSS, and JSLI documents to organize web
 application specific resources.

If you want to add custom visual elements to your web application library, refer to
 *Adding a Custom UI Palette to Your Web Application Library*.

Parent topic:

Building Shareable Libraries

Related tasks:

- Adding a Custom UI Palette to Your Web Application Library

<!--NI_TOPIC bundle=g-web-development path=recommendations-for-events.html language=enus -->
## TOPIC 00280: Recommendations for Event-Driven Programming

- bundle_id: `g-web-development`
- source_path: `recommendations-for-events.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/recommendations-for-events.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Because handling events in G Dataflow is different from handling events in other programming languages, follow NI's recommendations for event-driven programming. General Recommendations Recommendation Details Place the Event Structure in a While Loop that terminates when events can no longer occur.

### Recommendations for Event-Driven Programming

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

<!--NI_TOPIC bundle=g-web-development path=rectangle.html language=enus -->
## TOPIC 00281: Rectangle

- bundle_id: `g-web-development`
- source_path: `rectangle.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/rectangle.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Create a customizable rectangle.

### Rectangle

Create a customizable rectangle.

Parent topic:

Drawing Controls

<!--NI_TOPIC bundle=g-web-development path=reference-controls.html language=enus -->
## TOPIC 00282: Control Reference and VI Reference

- bundle_id: `g-web-development`
- source_path: `reference-controls.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/reference-controls.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represent a reference whose behavior and properties you can control and pass to other VIs.

### Control Reference and VI Reference

Represent a reference whose behavior and properties you can control and pass to other VIs.

Parent topic:

Creating User Interfaces

<!--NI_TOPIC bundle=g-web-development path=reference-terminal-tag.html language=enus -->
## TOPIC 00283: Reference Terminal

- bundle_id: `g-web-development`
- source_path: `reference-terminal-tag.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/reference-terminal-tag.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Transfers data between the diagram and other VIs. Use this terminal to add tag reference inputs or outputs to a subVI.

### Reference Terminal

Transfers data between the diagram and other VIs.

Use this terminal to add tag reference inputs or outputs to a subVI.

Parent topic:

Creating User Interfaces

<!--NI_TOPIC bundle=g-web-development path=reorder-tabs-nivs.html language=enus -->
## TOPIC 00284: Edit Tabs

- bundle_id: `g-web-development`
- source_path: `reorder-tabs-nivs.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/reorder-tabs-nivs.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Edit the name and order of the tabs on the selected tab control.

### Edit Tabs

Edit the name and order of the tabs on the selected tab control.

Parent topic:

Creating User Interfaces

<!--NI_TOPIC bundle=g-web-development path=repeating-operations-once-every-element-array.html language=enus -->
## TOPIC 00285: Repeating Operations Once for Every Element in an Array

- bundle_id: `g-web-development`
- source_path: `repeating-operations-once-every-element-array.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/repeating-operations-once-every-element-array.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `task`
- source_description: While working with an array of data, you might want to access individual elements within the array. Although you can use a combination of Array nodes to accomplish this task, the For Loop includes an auto-indexing tunnel that you can use to access the individual elements with minimal additional code

### Repeating Operations Once for Every Element in an Array

While working with an array of data, you might want to access individual elements within the array. Although you can use a combination of Array nodes to accomplish this task, the For Loop includes an auto-indexing tunnel that you can use to access the individual elements with minimal additional code.

Use a For Loop with an auto-indexing input tunnel to process one element of an array during each iteration of the loop. A For Loop with an auto-indexing input tunnel behaves similarly to a 
 for each loop in other programming languages.

#### What to Use

For Loop with an auto-indexing input tunnel

#### What to Do

Create the following diagram to repeat an operation once for every element in an array.

Customize the gray sections for your unique programming goals.

[IMAGE alt='image' src='GUID-81915C7A-852C-4361-9DA5-578078E4AD12-a5.png']

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

Related information:

- For Loop

<!--NI_TOPIC bundle=g-web-development path=repeating-operations-until-condition-occurs.html language=enus -->
## TOPIC 00286: Repeating Operations until a Condition Occurs

- bundle_id: `g-web-development`
- source_path: `repeating-operations-until-condition-occurs.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/repeating-operations-until-condition-occurs.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `task`
- source_description: In some situations, you might know that you want to repeat an operation, but you do not know exactly how many times you want to repeat that operation. Instead, you know only that the operation should repeat until a certain condition occurs. For example, you might have a program you want to run repea

### Repeating Operations until a Condition Occurs

In some situations, you might know that you want to repeat an operation, but you do not know exactly how many times you want to repeat that operation. Instead, you know only that the operation should repeat until a certain condition occurs. For example, you might have a program you want to run repeatedly until a user clicks a stop button or until the code inside the loop produces a particular value.

Use a While Loop to repeat code until a specified condition is met. A While Loop behaves similarly to a 
 do while loop in other programming languages.

#### What to Use

While Loop

#### What to Do

Create the following diagram to repeat an operation until a condition occurs.

Customize the gray sections for your unique programming goals.

[IMAGE alt='image' src='GUID-89659802-CC85-41BC-B657-49415B4A7FCD-a5.png']

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

Related information:

- While Loop

<!--NI_TOPIC bundle=g-web-development path=repeating-operations.html language=enus -->
## TOPIC 00287: Repeating Operations

- bundle_id: `g-web-development`
- source_path: `repeating-operations.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/repeating-operations.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `task`
- source_description: When building an application, you may need to repeat code a set number of times or until a specified condition is met. For example, you may have a section of code that you know you want to run three times. You may want your code to keep running until a user clicks a stop button. You can use loops to

### Repeating Operations

When building an application, you may need to repeat code a set number of times or until a specified condition is met. For example, you may have a section of code that you know you want to run three times. You may want your code to keep running until a user clicks a stop button. You can use loops to do this.

loop

Parent topic:

Programming in G

<!--NI_TOPIC bundle=g-web-development path=request-icon-editor.html language=enus -->
## TOPIC 00288: Request

- bundle_id: `g-web-development`
- source_path: `request-icon-editor.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/request-icon-editor.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Add a request symbol to the icon.

### Request

Add a request symbol to the icon.

Parent topic:

Actions Palette

<!--NI_TOPIC bundle=g-web-development path=reset-icon-editor.html language=enus -->
## TOPIC 00289: Reset

- bundle_id: `g-web-development`
- source_path: `reset-icon-editor.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/reset-icon-editor.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Add a reset symbol to the icon.

### Reset

Add a reset symbol to the icon.

Parent topic:

Actions Palette

<!--NI_TOPIC bundle=g-web-development path=resetting-workspace.html language=enus -->
## TOPIC 00290: Resetting the Workspace

- bundle_id: `g-web-development`
- source_path: `resetting-workspace.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/resetting-workspace.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `task`
- source_description: You can quickly restore the workspace to the default settings after you make adjustments. Click ViewReset Workspace. The Navigation Pane and Configuration Pane are expanded. The Errors and Warnings tab is collapsed on the bottom edge of the workspace.

### Resetting the Workspace

You can quickly restore the workspace to the default settings after you make adjustments.

View

»

Reset Workspace

- The Navigation Pane and Configuration Pane are expanded.
- The 
 Errors and Warnings tab is collapsed on the bottom edge of the workspace.

Parent topic:

Customizing G Web Development Software

<!--NI_TOPIC bundle=g-web-development path=resolve-package-dependencies.html language=enus -->
## TOPIC 00291: Resolving Missing or Mismatched Package Dependencies on a Development System

- bundle_id: `g-web-development`
- source_path: `resolve-package-dependencies.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/resolve-package-dependencies.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `task`
- source_description: Set up a development system by installing packages listed in the Package Dependencies document. Before you can resolve package dependencies on a development system, copy the project folder from the system on which the project was originally developed, then save the folder on the target system. Launc

### Resolving Missing or Mismatched Package Dependencies on a Development System

Set up a development system by installing packages listed in the Package Dependencies document.

Before you can resolve package dependencies on a development system, copy the project folder from the system on which the project was originally developed, then save the folder on the target system.

1. Launch the project, then open the Package Dependencies document. 
 When you open the Package Dependencies document, it searches the system to identify missing or mismatched packages for the project.
2. Click 
 Resolve. 
 The Package Dependencies document displays checkboxes next to the missing or mismatched packages. You can review the packages before installing them with NI Package Manager. By default, the Package Dependencies document selects all missing or mismatched packages. 
 Note NI Package Manager does not support downgrading packages.
3. Click 
 Resolve selected. 
 The Package Dependencies document launches NI Package Manager.
4. Follow the prompts in NI Package Manager to install the packages you selected. 
 Depending on the type of package you install, you may need to restart G Web Development
 Software or the development system.

Parent topic:

Package Dependencies

Parent topic:

Sharing a Project and Including Package Dependencies

Related tasks:

- Sharing a Project and Including Package Dependencies
- Capturing the Package Dependencies of a Project

<!--NI_TOPIC bundle=g-web-development path=retrieve-data-from-web-service.html language=enus -->
## TOPIC 00292: Retrieving Data From a Web Service

- bundle_id: `g-web-development`
- source_path: `retrieve-data-from-web-service.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/retrieve-data-from-web-service.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `task`
- source_description: Before you begin, open or create a web application project. What to Use GET While Loop Wait (Milliseconds) Case Structure What to Do Create the following diagram to retrieve data from a web service and display that data on the panel. Customize the gray sections for your unique programming goals. Com

### Retrieving Data From a Web Service

Before you begin, open or create a web application project.

#### What to Use

- GET
- While Loop
- Wait (Milliseconds)
- Case Structure

#### What to Do

Create the following diagram to retrieve data from a web service and display that data on the panel.

Customize the gray sections for your unique programming goals.

[IMAGE alt='Communicating With a Web Service Diagram' src='GUID-FD2A76BB-B616-444A-BC80-54793501FDDE-a5.png']

|  | If you want your web application to run continuously in a web browser, place your code in a While Loop with a False constant wired to the condition terminal. Otherwise, your web application runs only once in the web browser. Tip You can run your web application again by refreshing the page. |
| --- | --- |
|  | Place the code that calls the web service within a Case Structure. The Case Structure prevents the GET node from making a request to the web service in each iteration of the While Loop. Making a GET request each time the While Loop iterates is unnecessary because the data you're accessing probably doesn't change as quickly as the loop iterates. Most web services also limit how many requests you can make per second and may even ban your IP address if you make too many requests. |
|  | Enter the URL of the web service that you want to call. You can replace this code with a string constant containing the URL of a web service. You can also create code that programmatically creates a URL based on user input. In this example, Minimum Magnitude and Number of Earthquakes to Display determine what values make up the URL. |
|  | The GET node sends a request to the web service and returns data from that web service. In this example, the GET node sends a request to the U.S. Geological Survey web service and returns the latest earthquake data. |
|  | Create a subWebVI that parses the data that the web service returns. The web service in this example returns data in the JSON format, which is what most web services return. Other common data formats are XML, CSV, and YML. If a web service returns data in a format other than JSON, you can use other String nodes to parse that data. |
|  | To reduce load and improve performance when you run your built web application on a web browser, add a Wait node to any WebVI that uses an infinite While Loop. |

#### Troubleshooting

If the GET node doesn't return any data or returns unexpected data,
 verify the following conditions:

- The URL is correct. Test this by navigating to
 the URL in a web browser.
- The website or web server you want to access is
 running. Test this by navigating to the URL in a web browser.
- You have a working internet connection.

If each of these conditions is true, try one of the following:

- To check the status of an HTTP GET request,
 wire an indicator to the status code output of the
 GET node.
- To check detailed information about the HTTP
 GET request, including its status, wire an indicator to the headers 
 output of the GET node.

Refer to the W3C website for more information about HTTP status codes and headers.

#### Examples

Search within the programming environment to access the following installed examples:

- Call a 3rd Party Web Service
- Call LabVIEW Web Service

Parent topic:

Communicating Data with a Web Application

Related concepts:

- Considerations When Accessing Data from Web Services
- Communicating Data with Web Services Using WebVIs

Related information:

- Creating a LabVIEW Web Service
- Hosting a WebVI with the Web Applications Service
- GET
- While Loop
- Wait (Milliseconds)
- Case Structure
- WC3 Site

<!--NI_TOPIC bundle=g-web-development path=ring.html language=enus -->
## TOPIC 00293: Ring

- bundle_id: `g-web-development`
- source_path: `ring.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/ring.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Create a list that a user can cycle through to make selections. The internal output is an integer or a floating-point number.

### Ring

Create a list that a user can cycle through to make selections. The internal output is an integer or a floating-point number.

Parent topic:

Creating User Interfaces

<!--NI_TOPIC bundle=g-web-development path=rise-time.html language=enus -->
## TOPIC 00294: Rise Time

- bundle_id: `g-web-development`
- source_path: `rise-time.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/rise-time.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configure the speed of the bubbles as they rise.

### Rise Time

Configure the speed of the bubbles as they rise.

Parent topic:

Creating User Interfaces

<!--NI_TOPIC bundle=g-web-development path=roll.html language=enus -->
## TOPIC 00295: Roll

- bundle_id: `g-web-development`
- source_path: `roll.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/roll.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Increase to roll right; decrease to roll left.

### Roll

Increase to roll right; decrease to roll left.

Parent topic:

Creating User Interfaces

<!--NI_TOPIC bundle=g-web-development path=rounded-rectangle.html language=enus -->
## TOPIC 00296: Rounded Rectangle

- bundle_id: `g-web-development`
- source_path: `rounded-rectangle.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/rounded-rectangle.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Create a customizable rectangle with rounded corners.

### Rounded Rectangle

Create a customizable rectangle with rounded corners.

Parent topic:

Drawing Controls

<!--NI_TOPIC bundle=g-web-development path=run-operation-using-cli.html language=enus -->
## TOPIC 00297: Running Operations Using the Command Line Interface

- bundle_id: `g-web-development`
- source_path: `run-operation-using-cli.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/run-operation-using-cli.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `task`
- source_description: Run a predefined set of operations in G Web Development Software using the command line interface (CLI). For example, use the CLI to automate the build process of applications you develop. Open a command prompt. Change directories to the location of the CLI. The default location is C:\Program Files\

### Running Operations Using the Command Line Interface

Run a predefined set of operations in G Web
 Development Software using the command line interface (CLI).
 For example, use the CLI to automate the build process of applications you
 develop.

1. Open a command prompt.
2. Change directories to the location of the CLI. 
 Note The default location is
 C:\Program Files\National Instruments\G Web Development
 Software.
3. Execute a command using the following syntax: 
 gwebcli.exe <operation name>
 -<arguments>.Tip To access the built-in help for the CLI, execute the gwebcli.exe
 help command. To learn more about a
 specific operation, execute the gwebcli.exe
 <operation name> --help command.

Parent topic:

Developing a Web Application

<!--NI_TOPIC bundle=g-web-development path=save-icon-editor.html language=enus -->
## TOPIC 00298: Save

- bundle_id: `g-web-development`
- source_path: `save-icon-editor.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/save-icon-editor.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Add a save symbol to the icon.

### Save

Add a save symbol to the icon.

Parent topic:

Actions Palette

<!--NI_TOPIC bundle=g-web-development path=scale-legend.html language=enus -->
## TOPIC 00299: Scale Legend

- bundle_id: `g-web-development`
- source_path: `scale-legend.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/scale-legend.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Define labels for scales and configure scale properties.

### Scale Legend

Define labels for scales and configure scale properties.

Parent topic:

Creating User Interfaces

<!--NI_TOPIC bundle=g-web-development path=scales.html language=enus -->
## TOPIC 00300: Scales

- bundle_id: `g-web-development`
- source_path: `scales.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/scales.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Select the tick style of a numeric control or indicator.

### Scales

Select the tick style of a numeric control or indicator.

Parent topic:

Creating User Interfaces

<!--NI_TOPIC bundle=g-web-development path=scc-merge-resolve.html language=enus -->
## TOPIC 00301: Merging Files and Resolving Conflicts

- bundle_id: `g-web-development`
- source_path: `scc-merge-resolve.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/scc-merge-resolve.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Manually editing and merging files helps you maintain stable source code when merge conflicts occur. Recommendation Details Merge project (.lvproject) files manually. Merge project files manually rather than using the auto-merge utility in your source code control system. One expected merge conflict

### Merging Files and Resolving Conflicts

Manually editing and merging files helps you maintain stable source code when merge conflicts occur.

| Recommendation | Details |
| --- | --- |
| Merge project (.lvproject) files manually. | Merge project files manually rather than using the auto-merge utility in your source code control system. One expected merge conflict in the project file is the checksum, which records the state of the file when it was last loaded. When manually merging the project file, you can select the checksum from either version. G Web Development Software always reloads the project and generates a new checksum. |
| Manually edit a VI to resolve conflicts between two versions. | Avoid performing merge operations on VIs. |

Parent topic:

Recommendations for Developing a Project Stored in a Source Code Control Repository

<!--NI_TOPIC bundle=g-web-development path=scc-models.html language=enus -->
## TOPIC 00302: Source Code Control Models

- bundle_id: `g-web-development`
- source_path: `scc-models.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/scc-models.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `concept`
- source_description: Source code control systems are built using either a centralized or distributed model. Centralized Model In centralized source code control, a project exists in a single central repository, usually on a server. Users create a local repository on a client where they make modifications to the project,

### Source Code Control Models

Source code control systems are built using either a centralized or distributed model.

Centralized Model

In centralized source code control, a project exists in a single central repository, usually on a server. Users create a local repository on a client where they make modifications to the project, then upload their changes directly to the central repository.

Apache Subversion® (SVN) is one
 example of an open-source system using the centralized model.

Distributed Model

In distributed source code control, a project exists in a single central repository. Clients have two local repositories: a clone of the central repository and a working repository where users make modifications. Users submit modifications to the working repository often during development. When users finish development work, they push their changes to the central repository.

Git™ is one example of an open-source system using the distributed model.

Parent topic:

Recommendations for Developing a Project Stored in a Source Code Control Repository

<!--NI_TOPIC bundle=g-web-development path=scc-recommendations.html language=enus -->
## TOPIC 00303: Recommendations for Developing a Project Stored in a Source Code Control Repository

- bundle_id: `g-web-development`
- source_path: `scc-recommendations.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/scc-recommendations.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Because graphical code interacts differently with source code control systems than text-based code does, follow NI's recommendations for developing a project stored in a source code control (SCC) repository. The following information uses examples from Subversion (SVN) and Git. However, you can appl

### Recommendations for Developing a Project Stored in a Source Code Control Repository

Because graphical code interacts differently with source code control systems than text-based code does, follow NI's recommendations for developing a project stored in a source code control (SCC) repository.

Note

| Recommendation | Details |
| --- | --- |
| Create modular code within the project. | Modularity is a software design technique where units of code are collected together into logical and functional groups called modules. Modularity reduces the likelihood that changes to one module of code will introduce unexpected changes to another module of code. To build modularity into your project, create VIs and subVIs that handle specific, limited tasks. Use applications and libraries (.gcomp) when you want to group files together to perform a cohesive set of tasks. In team-based development environments, modular code helps create logical divisions of work between developers. |
| Avoid making simultaneous changes in a VI. | The likelihood of broken code increases when multiple developers modify the same VI simultaneously. Merge conflicts are possible when developers submit conflicting changes in a VI. If you use modular design techniques in the project, you can assign modules to individual developers on your team to reduce the likelihood that multiple developers will modify a VI simultaneously. Some source code control systems allow you to lock files when you check them out. Use this feature to prevent others from modifying a VI while you have it checked out. If you cannot avoid simultaneous development of VIs in a project, use NI Compare to view differences between two versions of a VI, then manually combine the differences between each version. |
| If you make changes to source files in the project, communicate with other developers on your team. | Modifications you make to source files in the project can produce changes to the project file as well as other files. Communicating with your team when you make changes helps other developers to quickly identify conflicts with their work. Using a collaboration tool can help streamline communication on a development team. Some collaboration tools, as well as some source code control systems, can auto-generate emails when changes to the repository occur. |
| Configure the project directory in the centralized repository to ignore submissions to the following project sub-folders: Builds.cache | Changes within these sub-directories do not affect the functionality of source code in the project. In SVN, apply the svn:ignore property to the sub-directories. In Git, list the sub-directories in the .gitignore file. |
| Perform code reviews before submitting code to the central repository. | Code reviews improve the quality of the code in your project and preserve the integrity of your source code as it changes during project development. Consider implementing a tiered review framework on your development team. For example: Peer reviews verify that the submission does not contain defects. Owner reviews verify that the submission adheres to architectural guidelines. As a code reviewer, you can use NI Compare to compare two versions of a project file or VI. |
| Create a Package Dependencies (.sls) document and keep it up to date during project development. | When you include a Package Dependencies (.sls) document in the project, developers can update this file as they create code, then other developers can use it to keep their development systems in sync. |
| For VIs, disable the auto-merge utility in your source code control system. | The underlying source of a VI file is XML-based text. When merging two versions of a VI, the auto-merge utility might combine lines of text from each version in a way that corrupts the VI and prevents the VI from opening. If using the auto-merge utility on a VI breaks code, you may need to revert the VI to an older version to recover your code. |
| Minimize occurrences of renaming and moving files. | When you rename or move a file, SCC systems delete the file and create a new file with the new name or location you provide. This operation erases any version history of the file with its previous name or location. Other developers could introduce a breaking change when they submit files that use the old name. You might encounter this behavior when you move a VI file to an application or library. |

Parent topic:

Collaborating on Web Applications

Related information:

- Using NI Compare with Source Control Providers

<!--NI_TOPIC bundle=g-web-development path=selector-controls.html language=enus -->
## TOPIC 00304: Selector Controls

- bundle_id: `g-web-development`
- source_path: `selector-controls.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/selector-controls.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Create a list that a user can cycle through to make selections. Types of Selector Controls Control Description Ring A ring control is a numeric input that presents a set of choices associated with numeric values. Enumerated type, or Enum The enum control is an object that presents a set of choices a

### Selector Controls

Create a list that a user can cycle through to make selections.

[IMAGE alt='image' src='GUID-8478A9F3-AA87-4ECC-8E3F-D0353E55DBEC-a5.png']

#### Types of Selector Controls

| Control | Description |
| --- | --- |
| Ring | A ring control is a numeric input that presents a set of choices associated with numeric values. |
| Enumerated type, or Enum | The enum control is an object that presents a set of choices associated with an enumerated data type. The enumerated data type consists of a set of named constants. |
| Radio Button Group | The radio button group control is an object that presents a set of mutually exclusive choices associated with an enumerated data type. The enumerated data type consists of a set of named constants. |
| Combo Box | The combo box control is an object that presents a list of names associated with string values. Users may select from items in a predefined list or enter new values directly, at edit time or run time. |
| Listbox | The listbox control is an object that presents a set of items. Users may select single or multiple items at run time. |
| Color Selector | The color selector control is an object that presents a color selection. Each color corresponds to RGBA color values or a hexadecimal value. |

#### Which Selector Control Should I Use?

Selector controls all contain a list of items from which the user can make a selection.

| Control | When to Use | Examples: E-Commerce Application |
| --- | --- | --- |
| Ring | Use a ring when you want to provide a list of choices that represent numeric values. The ring control is a numeric input that allows the user to choose from a list of meaningful, human-readable values instead of numeric values. If the logic of your program prefers numeric values to string values, use a ring. | You want to present users with a list of product names, each of which corresponds to a unique product number. You can specify the products' numbers as their respective numeric values. You can then cross-reference those numeric values to find the prices of the items. |
| Enum and Radio Button Group | Use an enum or a radio button group when you want to provide a list of choices associated with an enumerated data type. If you want your program to deal with a fixed set of constants instead of arbitrary numeric data, use an enum or radio button group. In general, use a radio button group when you have less than five options for the user to select from. A radio button group can help the user quickly scan the options. | You want to present users with a list of shipping speed options for the item they want to order. The numeric values assigned to each of the options are automatically defined. You cannot edit the numeric values. You can use the enumerated data type in the enum control to drive the logic of your program. For example, because the names of the choices are part of the data type, you can use them to populate the cases of a Case Structure. This ensures that only valid states are used in your program. Figure 1. Enum Figure 2. Radio Button Group |
| Combo Box | Use a combo box when you want to provide a list of items for users to cycle through while also providing the option to type new values into the menu at edit time or run time. If the logic of your program requires string values rather than numeric values, use a combo box. | You want to present users with a list of previous shipping addresses, while also allowing them to enter a new shipping address for this purchase. |
| Listbox | Use a listbox when you want to provide a list of items in which users can select items at run time. | You want to present users with a list of products in which they can select one or more items. You can also allow users to select zero items by checking the Allow no selection checkbox. For example, you can allow users to deselect all items. |

#### Assigning Specific Values to Selector Controls

Unlike the strings listed in rings, enums, and radio button groups, the strings listed in a combo box and listbox have no numeric representation. Additionally, enums and radio button groups require these numeric values to be sequential, unsigned integer values, while rings allow for much more freedom in assigning a numeric value.

1. Select the control to which you want to assign specific values.
2. On the 
 Item tab, in the 
 Items group, assign and arrange specific values as desired.

#### Enabling a Combo Box to Accept New Values from the User at Edit Time or Run Time

1. Select the combo box control.
2. On the 
 Item tab, in the 
 Items group, select 
 Allow entry of unlabeled values .

Parent topic:

Creating User Interfaces

Related concepts:

- Enum Data

<!--NI_TOPIC bundle=g-web-development path=sending-credentialed-cross-origin-http-request.html language=enus -->
## TOPIC 00305: Sending a Credentialed Cross-Origin HTTP Request

- bundle_id: `g-web-development`
- source_path: `sending-credentialed-cross-origin-http-request.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/sending-credentialed-cross-origin-http-request.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `task`
- source_description: Enable credentials in your WebVI, such as including and storing HTTP cookies, adding HTTP Authorization headers, or permitting TLS client certificates to interact with a web service. In addition to configuring a web service to support cross-origin credentialed requests, configure the client handle t

### Sending a Credentialed Cross-Origin HTTP Request

Enable credentials in your WebVI, such as including and storing HTTP cookies, adding
 HTTP Authorization headers, or permitting TLS client certificates to interact with a web
 service.

In addition to configuring a web service to support cross-origin credentialed requests,
 configure the client handle to include credentials during a CORS requests.

Note

#### What to Use

- Configure CORS
- Open HTTP Handle
- Close HTTP Handle

#### What to Do

Create the following diagram to send a credentialed cross-origin HTTP request.

Customize the gray sections for your unique programming goals.

[IMAGE alt='image' src='GUID-3371433B-C0FB-4080-B53A-FA9C9324E142-a5.png']

|  | Open HTTP Handle creates a client handle that preserves the headers you want to add to HTTP requests the application sends. |
| --- | --- |
|  | Configure CORS adds configuration information, such as whether credentials should be included in CORS requests, to the client handle. |
|  | Configure the HTTP node to access resources for your application. |
|  | Close HTTP Handle closes the client handle and deletes any authentication credentials and HTTP headers associated with the handle. Note The browser cache independently stores and manages cookies a credentialed CORS request or same-origin request creates. Closing the client handle does not affect the cookies in the browser cache. |

#### Troubleshooting

Some servers may require that your application not include credentials with a cross-origin
 HTTP request. If the server you send requests to responds with the
 Access-Control-Allow-Origin header set to *, the
 wildcard value, the HTTP request fails with a CORS configuration error. To resolve the
 error, set the include credentials during CORS input of
 Configure CORS to False. To enable credentialed access for a LabVIEW
 Web Service, see *Configure a LabVIEW Web Service CORS for Credentialed
 Access*.

Parent topic:

Considerations When Accessing Data from Web Services

Related concepts:

- Configuring CORS for a LabVIEW Web Service

Related tasks:

- Configure a LabVIEW Web Service CORS for Credentialed Access

Related information:

- Configure CORS
- Open HTTP Handle
- Close HTTP Handle

<!--NI_TOPIC bundle=g-web-development path=shape-ribbon-item-array-vs-scalar.html language=enus -->
## TOPIC 00306: Shape ribbon item (scalar vs array)

- bundle_id: `g-web-development`
- source_path: `shape-ribbon-item-array-vs-scalar.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/shape-ribbon-item-array-vs-scalar.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configure the resource as an array or scalar.

### Shape ribbon item (scalar vs array)

Configure the resource as an array or scalar.

Parent topic:

Creating User Interfaces

<!--NI_TOPIC bundle=g-web-development path=shape-ribbon-item-array.html language=enus -->
## TOPIC 00307: Shape

- bundle_id: `g-web-development`
- source_path: `shape-ribbon-item-array.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/shape-ribbon-item-array.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Set array size and dimension.

### Shape

Set array size and dimension.

Parent topic:

Creating User Interfaces

<!--NI_TOPIC bundle=g-web-development path=shape-ribbon-item-fifo.html language=enus -->
## TOPIC 00308: Shape

- bundle_id: `g-web-development`
- source_path: `shape-ribbon-item-fifo.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/shape-ribbon-item-fifo.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configure the FIFO as an array or scalar. This option changes the configuration of the FIFO container on the diagram but does not change the configuration of any FIFO resource in SystemDesigner. If you change this option, you must specify a FIFO resource that meets the new configuration to avoid a t

### Shape

Configure the FIFO as an array or scalar. This option changes the configuration of the FIFO container on the diagram but does not change the configuration of any FIFO resource in SystemDesigner. If you change this option, you must specify a FIFO resource that meets the new configuration to avoid a type mismatch error.

Parent topic:

Creating User Interfaces

<!--NI_TOPIC bundle=g-web-development path=shapes.html language=enus -->
## TOPIC 00309: Shapes Palette

- bundle_id: `g-web-development`
- source_path: `shapes.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/shapes.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Add shapes to the icon.

### Shapes Palette

Add shapes to the icon.

Parent topic:

Creating User Interfaces

<!--NI_TOPIC bundle=g-web-development path=share-package-dependencies.html language=enus -->
## TOPIC 00310: Sharing a Project and Including Package Dependencies

- bundle_id: `g-web-development`
- source_path: `share-package-dependencies.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/share-package-dependencies.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `task`
- source_description: Use the Package Dependencies document to store a list of packages a project uses so you can set up a development system with the required packages. Create a project that uses NI software, drivers, or third-party packages. Identify the packages a project requires and store a list of those packages in

### Sharing a Project and Including Package Dependencies

Use the Package Dependencies document to store a list of packages a project uses so you can set up a development system with the required packages.

1. Create a project that uses NI software, drivers, or third-party packages.
2. Identify the packages a project requires and store a list of those packages in the
 Package Dependencies document. 
 Note When you capture package
 dependencies, you must have the required packages installed on the source system and the
 code in the project must be in working condition.
3. Copy the project folder and save it on the target system.
4. Set up a development system by installing packages listed in the Package Dependencies
 document.

Parent topic:

Package Dependencies

Related tasks:

- Capturing the Package Dependencies of a Project
- Resolving Missing or Mismatched Package Dependencies on a Development System

<!--NI_TOPIC bundle=g-web-development path=show-escape-sequences.html language=enus -->
## TOPIC 00311: Show escape sequences

- bundle_id: `g-web-development`
- source_path: `show-escape-sequences.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/show-escape-sequences.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Display escape sequences or character representations.

### Show escape sequences

Display escape sequences or character representations.

Parent topic:

Creating User Interfaces

<!--NI_TOPIC bundle=g-web-development path=show-escape-string-constant.html language=enus -->
## TOPIC 00312: Show escape sequences

- bundle_id: `g-web-development`
- source_path: `show-escape-string-constant.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/show-escape-string-constant.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Display escape sequences or character representations.

### Show escape sequences

Display escape sequences or character representations.

Parent topic:

Creating User Interfaces

<!--NI_TOPIC bundle=g-web-development path=size.html language=enus -->
## TOPIC 00313: Size button

- bundle_id: `g-web-development`
- source_path: `size.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/size.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Choose a preset display size for selected items on the panel.

### Size button

Choose a preset display size for selected items on the panel.

Parent topic:

Creating User Interfaces

<!--NI_TOPIC bundle=g-web-development path=smart-guides.html language=enus -->
## TOPIC 00314: Aligning Objects on the Panel

- bundle_id: `g-web-development`
- source_path: `smart-guides.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/smart-guides.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `task`
- source_description: When Smart Guides are enabled, the editor displays guide lines to help you align and organize objects as you add them to the panel. Click FilePreferences to display the Preferences dialog box. On the VI tab, in the Panel Editing Defaults section, place a checkmark in the Smart Guides checkbox. As yo

### Aligning Objects on the Panel

When Smart Guides are enabled, the editor displays guide lines to help you align and organize objects as you add them to the panel.

1. Click 
 File»Preferences to display the 
 Preferences dialog box.
2. On the 
 VI tab, in the 
 Panel Editing Defaults section, place a checkmark in the 
 Smart Guides checkbox. 
 As you add objects to the panel, the editor displays guide lines to assist with alignment, as shown in the following image.
 [IMAGE alt='image' src='GUID-3FBA69E2-8EC7-422D-8D1A-B2A2A35C5D97-a5.png']

Parent topic:

Customizing G Web Development Software

<!--NI_TOPIC bundle=g-web-development path=standard-states-when-planning-your-program.html language=enus -->
## TOPIC 00315: Standard States To Consider When Planning Your Program

- bundle_id: `g-web-development`
- source_path: `standard-states-when-planning-your-program.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/standard-states-when-planning-your-program.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `concept`
- source_description: When you design a state machine, create a distinct initialize state for the program. You can also add a specific state to handle user input or provide custom error handling, depending on your program needs. States to Include in Every State Machine You Create Specify one entry point and one exit poin

### Standard States To Consider When Planning Your Program

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

<!--NI_TOPIC bundle=g-web-development path=start-icon-editor.html language=enus -->
## TOPIC 00316: Start

- bundle_id: `g-web-development`
- source_path: `start-icon-editor.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/start-icon-editor.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Add a start symbol to the icon.

### Start

Add a start symbol to the icon.

Parent topic:

Actions Palette

<!--NI_TOPIC bundle=g-web-development path=state-diagrams.html language=enus -->
## TOPIC 00317: State Diagrams

- bundle_id: `g-web-development`
- source_path: `state-diagrams.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/state-diagrams.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `concept`
- source_description: To keep track of every state and interaction in your program, design a state diagram of your state machine before you start programming. A state diagram is an illustration of all the states in a state machine and how these states interact with each other. Each circle represents a state, and each arr

### State Diagrams

To keep track of every state and interaction in your program, design a state diagram of your state machine before you start programming.

A state diagram is an illustration of all the states in a state machine and how these states interact with each other. Each circle represents a state, and each arrow represents a possible state transition. While you create your code, you can follow the diagram flowchart to recall how to structure the state machine and how the states within the machine interact.

The following image shows an example of a basic state diagram for a program that changes the temperature of a room over time.

[IMAGE alt='image' src='GUID-4ECC3348-E0C0-4C39-BE40-084FD315F69A-a5.png']

The state diagram shows all possible state transitions in the program. You can use the state diagram to understand how the states within the program interact before analyzing the code that defines the interactions.

- Each arrow points toward the endpoint of a state transition. For example, the initialize state can only transition to the adjust temperature state. On the other hand, the program can transition back and forth between the adjust temperature state and wait for event state.
- A circular arrow, seen on the adjust temperature and wait for event states, indicates that the state can transition to itself.
- A blue arrow indicates that a transition occurs because of a user action, and a yellow arrow indicates that a transition occurs because of an error in the program.

Parent topic:

State Machine Design Pattern

<!--NI_TOPIC bundle=g-web-development path=state-machine-design-pattern.html language=enus -->
## TOPIC 00318: State Machine Design Pattern

- bundle_id: `g-web-development`
- source_path: `state-machine-design-pattern.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/state-machine-design-pattern.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use the state machine design pattern to implement decision making algorithms where a set of distinguishable states exists. These states, or subdiagrams of code, carry out specific operations within a program. Only one state executes at a time while the machine is active. After all of the cod

### State Machine Design Pattern

You can use the state machine design pattern to implement decision making algorithms where a set of distinguishable states exists.

These states, or subdiagrams of code, carry out specific operations within a program. Only one state executes at a time while the machine is active.

After all of the code within a state executes, the state outputs a transition value and initiates a state transition. This transition advances the program from the finished state to the next state indicated by the transition value.

During a state transition, data from the completed state is sent to the upcoming state. Once the state machine executes its final state, data output by the machine becomes available for other parts of the program to use.

Parent topic:

Programming Design Patterns

<!--NI_TOPIC bundle=g-web-development path=stop-icon-editor.html language=enus -->
## TOPIC 00319: Stop

- bundle_id: `g-web-development`
- source_path: `stop-icon-editor.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/stop-icon-editor.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Add a stop symbol to the icon.

### Stop

Add a stop symbol to the icon.

Parent topic:

Actions Palette

<!--NI_TOPIC bundle=g-web-development path=strategies-for-improving-vi-execution-speed.html language=enus -->
## TOPIC 00320: Strategies for Improving VI Execution Speed

- bundle_id: `g-web-development`
- source_path: `strategies-for-improving-vi-execution-speed.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/strategies-for-improving-vi-execution-speed.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `concept`
- source_description: Factors like inefficient memory use, poorly designed panels, and too many I/O calls can negatively affect the execution speed of your VI. However, there are several strategies you can use to ensure that your VI runs more efficiently. Strategies for Improving Execution Speed through Memory Management

### Strategies for Improving VI Execution Speed

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

[IMAGE alt='image' src='GUID-633AA8AE-1DA2-4DB6-ABF8-2B613359B263-a5.png']

Since all parallel loops share the same processor resources, consider the following practices to make sure other loops do not interrupt the timing or execution of your important tasks:

- Important Operations—Because you want this type of operation to execute as frequently as possible, do not add timing nodes inside the loop to delay its execution.
- Executions Dependent on Dequeue Element node—The Dequeue Element node can halt the execution of a loop until an element is ready in the queue. This node allows more important loops to use more of the processor's time.
- Low-Importance Operations—Because this type of operation is the least important, you can use a Wait node to run the operation less often and yield execution time to the other loops.

The following is an example of a recreated VI using the considerations:

[IMAGE alt='image' src='GUID-0F9586DE-0938-4247-841E-C0151C504258-a5.png']

1. The Read DAQ loop reads data from a DAQ device and sends the data to a queue. Do not add timing nodes because you want this type of operation to execute as frequently as possible.
2. The Write to File loop can execute more slowly as it is logging data points for later analysis. The execution of this loop can be dependent on elements being ready in the queue because it does not need to execute as frequently.
3. The Check Temperature loop displays temperature data to the user and uses a Wait node to run less often and yield execution time to the other loops because it is the least important.

<!--NI_TOPIC bundle=g-web-development path=stretch.html language=enus -->
## TOPIC 00321: Stretch

- bundle_id: `g-web-development`
- source_path: `stretch.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/stretch.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fit one column to width, distribute column widths, or size column widths individually.

### Stretch

Fit one column to width, distribute column widths, or size column widths individually.

Parent topic:

Creating User Interfaces

<!--NI_TOPIC bundle=g-web-development path=string-control.html language=enus -->
## TOPIC 00322: String Control

- bundle_id: `g-web-development`
- source_path: `string-control.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/string-control.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Enter string data.

### String Control

Enter string data.

Parent topic:

Creating User Interfaces

<!--NI_TOPIC bundle=g-web-development path=string-data.html language=enus -->
## TOPIC 00323: String Data

- bundle_id: `g-web-development`
- source_path: `string-data.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/string-data.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `concept`
- source_description: Strings represent text. A string is a sequence of zero or more letters, numbers, and special characters. On the diagram, strings are represented by pink objects and wires. The string data type cannot represent binary data. For binary data, use an array of U8 integers. For text, use a string data typ

### String Data

Strings represent text. A 
 *string* is a sequence of zero or more letters, numbers, and special characters. On the diagram, strings are represented by pink objects and wires.

[IMAGE alt='image' src='GUID-F0800853-DCB1-45E9-A9B1-D6AB854B6906-a5.png']

The string data type cannot represent binary data. For binary data, use an array of U8 integers. For text, use a string data type. Casting any data type to a string may cause unexpected behavior when displaying or manipulating the string.

You can use built-in nodes to format, parse, and manipulate strings.

On the panel, strings appear as tables, text entry boxes, and labels.

Parent topic:

Data Type Reference

<!--NI_TOPIC bundle=g-web-development path=string-indicator.html language=enus -->
## TOPIC 00324: String Indicator

- bundle_id: `g-web-development`
- source_path: `string-indicator.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/string-indicator.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Display string data.

### String Indicator

Display string data.

Parent topic:

Creating User Interfaces

<!--NI_TOPIC bundle=g-web-development path=string.html language=enus -->
## TOPIC 00325: String

- bundle_id: `g-web-development`
- source_path: `string.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/string.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Add a string data type symbol to the icon.

### String

Add a string data type symbol to the icon.

Parent topic:

Data Types Palette

<!--NI_TOPIC bundle=g-web-development path=subvi-from-selection.html language=enus -->
## TOPIC 00326: Creating a SubVI from a Section of Existing Code

- bundle_id: `g-web-development`
- source_path: `subvi-from-selection.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/subvi-from-selection.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `task`
- source_description: Select the section of code you want to reuse. Click EditCreate subVI from selection to generate a new .gvi file in the project. To open this file, double-click the corresponding subVI node that contains the section of code you selected. The subVI diagram and connector pane include inputs and outputs

### Creating a SubVI from a Section of Existing Code

1. Select the section of code you want to reuse.
2. Click 
 Edit»Create subVI from selection to generate a new 
 .gvi file in the project. 
 To open this file, double-click the corresponding subVI node that contains the section of code you selected. The subVI diagram and connector pane include inputs and outputs for every wire that enters and exits the section of code. The panel automatically includes the corresponding controls and indicators. 
 Tip To disable automatically placing items on the panel, click 
 File»Preferences, select the 
 VI tab, and disable 
 Place items on the panel when creating subVI from selection.
3. Rename and save the new 
 .gvi file. 
 Choose a name that describes what function the VI performs so that other users can clearly understand any diagram that uses the VI as a subVI.

To add the new subVI as a node on other diagrams, locate the subVI in the 
 Project Files tab and drag it to the diagram where you want to use it.

Note

Parent topic:

SubVIs

<!--NI_TOPIC bundle=g-web-development path=sweep.html language=enus -->
## TOPIC 00327: Sweep

- bundle_id: `g-web-development`
- source_path: `sweep.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/sweep.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Set the angle of the scale.

### Sweep

Set the angle of the scale.

Parent topic:

Creating User Interfaces

<!--NI_TOPIC bundle=g-web-development path=synchronizing-operations.html language=enus -->
## TOPIC 00328: Synchronizing the Execution of Multiple Loops

- bundle_id: `g-web-development`
- source_path: `synchronizing-operations.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/synchronizing-operations.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `task`
- source_description: By default, each loop iteration executes as quickly as possible based on the code inside the loop. However, consider a program that includes multiple loops that contain code requiring different amounts of time to execute. You might want to control the rate at which those loops execute in order to sy

### Synchronizing the Execution of Multiple Loops

By default, each loop iteration executes as quickly as possible based on the code inside the loop. However, consider a program that includes multiple loops that contain code requiring different amounts of time to execute. You might want to control the rate at which those loops execute in order to synchronize their execution and ensure that the loops begin each iteration at the same time. Use Wait Until Next Multiple to do this.

#### What to Use

- While Loop or For
 Loop
- Wait Until Next
 Multiple

#### What to Do

Create the following diagram to synchronize the execution of multiple loops.

Customize the gray sections for your unique programming goals.

[IMAGE alt='image' src='GUID-120DDA40-708D-4346-8FCA-23959768AB55-a5.png']

|  | Wire the same value to the inputs of the Wait Until Next Multiple nodes placed on the subdiagram of each loop. The loops wait until the value of the system clock becomes a multiple of the specified input before beginning each iteration. Therefore, the loops begin each iteration at exactly the same time. |
| --- | --- |
|  | When specifying a value for the input of Wait Until Next Multiple, ensure that the value is greater than the time required to execute the code inside the loop. If a loop contains code that takes longer to execute than the time specified, Wait Until Next Multiple has no effect on the execution speed of the loop. |

Parent topic:

Repeating Operations

Related information:

- For Loop
- While Loop
- Wait Until Next Multiple

<!--NI_TOPIC bundle=g-web-development path=tab-control.html language=enus -->
## TOPIC 00329: Tab Control

- bundle_id: `g-web-development`
- source_path: `tab-control.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/tab-control.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Organize controls and indicators by overlapping them in a smaller area.

### Tab Control

Organize controls and indicators by overlapping them in a smaller area.

Parent topic:

Creating User Interfaces

<!--NI_TOPIC bundle=g-web-development path=tab-strip-placement.html language=enus -->
## TOPIC 00330: Tab Strip Placement

- bundle_id: `g-web-development`
- source_path: `tab-strip-placement.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/tab-strip-placement.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specify where the tabs appear on the selected tab control.

### Tab Strip Placement

Specify where the tabs appear on the selected tab control.

Parent topic:

Creating User Interfaces

<!--NI_TOPIC bundle=g-web-development path=table.html language=enus -->
## TOPIC 00331: Table

- bundle_id: `g-web-development`
- source_path: `table.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/table.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Group data elements of the string type or numeric type in a 2D array.

### Table

Group data elements of the string type or numeric type in a 2D array.

Parent topic:

Creating User Interfaces

<!--NI_TOPIC bundle=g-web-development path=tag-reference-lvmember.html language=enus -->
## TOPIC 00332: Tag Reference

- bundle_id: `g-web-development`
- source_path: `tag-reference-lvmember.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/tag-reference-lvmember.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Create references to tag resources. You can only use this control as part of a subVI. When you run a subVI that uses this control, the control does not return a valid reference unless a valid reference is passed from a calling VI.

### Tag Reference

Create references to tag resources.

You can only use this control as part of a subVI.

Note

Parent topic:

Creating User Interfaces

<!--NI_TOPIC bundle=g-web-development path=tank.html language=enus -->
## TOPIC 00333: Tank

- bundle_id: `g-web-development`
- source_path: `tank.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/tank.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Display numeric data in a vertical slide that resembles a real tank or thermometer instrument.

### Tank

Display numeric data in a vertical slide that resembles a real tank or thermometer instrument.

Parent topic:

Creating User Interfaces

<!--NI_TOPIC bundle=g-web-development path=terminals-definition.html language=enus -->
## TOPIC 00334: Terminals

- bundle_id: `g-web-development`
- source_path: `terminals-definition.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/terminals-definition.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `concept`
- source_description: Terminals transfer data between the diagram and panel, between the diagram and other nodes, or between duplicates of the same terminal on the diagram. As the following example shows, the color and symbol of each terminal indicate the data type of the terminal.

### Terminals

Terminals transfer data between the diagram and panel, between the diagram and other nodes, or between duplicates of the same terminal on the diagram.

As the following example shows, the color and symbol of each terminal indicate the data type of the terminal.

[IMAGE alt='image' src='GUID-54759EF0-56FC-4CBD-B91B-657624C26E99-a5.png']

Parent topic:

Programming in G

<!--NI_TOPIC bundle=g-web-development path=text-controls-palette.html language=enus -->
## TOPIC 00335: Text Controls

- bundle_id: `g-web-development`
- source_path: `text-controls-palette.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/text-controls-palette.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Create text entry boxes and labels or enter or return the location of a file or directory. Which Text Control Should I Use? Use Control Enter string data. String Control Display string data. String Indicator Create free floating text that you can use as a label or annotation. Text Enter or display a

### Text Controls

Create text entry boxes and labels or enter or return the location of a file or directory.

[IMAGE alt='image' src='GUID-0EA6EEA1-3393-4B2A-BAFD-9A84FFE65F68-a5.png']

#### Which Text Control Should I Use?

| Use | Control |
| --- | --- |
| Enter string data. | String Control |
| Display string data. | String Indicator |
| Create free floating text that you can use as a label or annotation. | Text |
| Enter or display a URL hyperlink. | Hyperlink Control |
| Enter string data in masked display. | Masked Input Control Note This control only masks the text visually. When you read the string data from the diagram, you read the actual data the user entered. Any mechanism that can examine the memory of the program can also read the actual data. |

#### When Does My Entered Text Pass to the Diagram?

By default, new or changed text does not pass to the diagram until you terminate the edit session by clicking elsewhere on the panel or by pressing Ctrl-Enter.

You can change the behavior of the Enter key for a String control by clicking the control on the panel and selecting a new 
 Enter key behavior in the 
 Item tab.

| Option | Behavior |
| --- | --- |
| Commits text | Pressing Enter terminates the edit session. You can also terminate the edit session by clicking elsewhere on the panel. Carriage returns are not allowed. |
| Enters new line (default) | Pressing Enter inserts a carriage return. You can terminate the edit session by clicking elsewhere on the panel or pressing Ctrl-Enter. |

Parent topic:

Creating User Interfaces

<!--NI_TOPIC bundle=g-web-development path=text-controls-webvi.html language=enus -->
## TOPIC 00336: Text

- bundle_id: `g-web-development`
- source_path: `text-controls-webvi.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/text-controls-webvi.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Create free-floating text that you can use as a label or annotation.

### Text

Create free-floating text that you can use as a label or annotation.

Parent topic:

Creating User Interfaces

<!--NI_TOPIC bundle=g-web-development path=text-controls.html language=enus -->
## TOPIC 00337: Text

- bundle_id: `g-web-development`
- source_path: `text-controls.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/text-controls.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Create free-floating text that you can use as a label or annotation.

### Text

Create free-floating text that you can use as a label or annotation.

Parent topic:

Creating User Interfaces

<!--NI_TOPIC bundle=g-web-development path=text.html language=enus -->
## TOPIC 00338: Text Palette

- bundle_id: `g-web-development`
- source_path: `text.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/text.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Add text to the icon.

### Text Palette

Add text to the icon.

Parent topic:

Creating User Interfaces

<!--NI_TOPIC bundle=g-web-development path=timestamp-control.html language=enus -->
## TOPIC 00339: Timestamp Control

- bundle_id: `g-web-development`
- source_path: `timestamp-control.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/timestamp-control.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Enter a time and date value.

### Timestamp Control

Enter a time and date value.

Parent topic:

Creating User Interfaces

<!--NI_TOPIC bundle=g-web-development path=timestamp-indicator.html language=enus -->
## TOPIC 00340: Timestamp Indicator

- bundle_id: `g-web-development`
- source_path: `timestamp-indicator.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/timestamp-indicator.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Display a time and date value.

### Timestamp Indicator

Display a time and date value.

Parent topic:

Creating User Interfaces

<!--NI_TOPIC bundle=g-web-development path=timestamp.html language=enus -->
## TOPIC 00341: TimeStamp

- bundle_id: `g-web-development`
- source_path: `timestamp.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/timestamp.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Add a time stamp data type symbol to the icon.

### TimeStamp

Add a time stamp data type symbol to the icon.

Parent topic:

Data Types Palette

<!--NI_TOPIC bundle=g-web-development path=tips-for-editing-diagram-code.html language=enus -->
## TOPIC 00342: Tips and Tricks for Editing Diagram Code

- bundle_id: `g-web-development`
- source_path: `tips-for-editing-diagram-code.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/tips-for-editing-diagram-code.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: The following time-saving tools can help you edit diagram code more efficiently. Creating Diagram Code Task Tips and Tricks Create constants, controls, and indicators using the shortcut menu. You can save time when adding constants, controls, and indicators by using the shortcut menu to add the obje

### Tips and Tricks for Editing Diagram Code

The following time-saving tools can help you edit diagram code more efficiently.

#### Creating Diagram Code

| Task | Tips and Tricks |
| --- | --- |
| Create constants, controls, and indicators using the shortcut menu. | You can save time when adding constants, controls, and indicators by using the shortcut menu to add the object instead of navigating the palette. Right-click any input or output of a node and select one of the Create options from the shortcut menu. For example, to create a constant, select the Create Constant icon. |
| Create a subVI from existing code. | You can use the Create SubVI from Selection option on the document toolbar to automatically generate a new subVI from a section of existing code. Refer to Creating a SubVI from a Section of Existing Code for more information. |

#### Editing Diagram Code

| Task | Tips and Tricks |
| --- | --- |
| Replace a diagram object with a similar object without using the palette. | You can replace an object on the diagram, such as a node, terminal, or constant, with a different type of the same object without navigating the palette. For example, you can replace an Add node with a Subtract node, a Numeric Terminal with a Boolean Terminal, or a True Constant with a False Constant. Right-click the object, select Replace from the shortcut menu, and select the desired replacement object. |
| Remove a structure without deleting objects in the structure. | You can remove a loop, Case Structure, or Flat Sequence from the diagram without deleting the code it contains. Right-click the border of the structure and select Remove Name of Structure from the shortcut menu. |

#### Organizing Diagram Code

| Task | Tips and Tricks |
| --- | --- |
| Align or distribute diagram objects to improve the organization of the diagram. | On the document toolbar, click Order, Align, or Distribute to organize a set of selected objects. |
| Delete all broken wires at one time. | On the document toolbar, click Remove Broken Wires to delete all broken wires on the diagram. |
| Clean up wires. | You can automatically route a selected wire to decrease the number of bends in the wire and avoid crossing objects on the diagram. Right-click a wire and select Clean Up Wire from the shortcut menu. |
| Move a terminal label to improve diagram readability. | To change the position of a terminal label, select the terminal and update the Label Placement option in the Item tab. |
| Show a node label to improve diagram readability. | To show a node label, select the node and enable the Show Label option in the Item tab. |

Parent topic:

Getting Started with G Web Development Software

Related tasks:

- Creating a SubVI from a Section of Existing Code

<!--NI_TOPIC bundle=g-web-development path=transfer-data-loops.html language=enus -->
## TOPIC 00343: Preventing Data Loss When Transferring Data Between Loops

- bundle_id: `g-web-development`
- source_path: `transfer-data-loops.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/transfer-data-loops.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `task`
- source_description: Prevent data loss and promote efficiency when transferring data between producer and consumer loops by using queue nodes. By creating a queue of data that is ready to be consumed, a consumer loop can process a greater volume of data at more regular intervals without losing data. This is especially u

### Preventing Data Loss When Transferring Data Between Loops

Prevent data loss and promote efficiency when transferring data between producer and consumer loops by using queue nodes.

By creating a queue of data that is ready to be consumed, a consumer loop can process a greater volume of data at more regular intervals without losing data. This is especially useful if data from multiple network channels need to be processed in the order in which they arrive.

Tip

#### What to Use

- Obtain Queue
- Enqueue Element
- Dequeue Element
- Get Queue Status
- Release Queue

#### What to Do

1. Create the following diagram to automate the reading and writing of data without the risk of losing data. 
 
 Customize the gray sections for your unique programming goals. 
 
 [IMAGE alt='image' src='GUID-97140CE0-AE0F-45D2-BC12-D22F4BA789B6-a5.svg']
 Use Obtain Queue to set the data type for the queue and to set the maximum number of elements the queue can hold. In this example, the queue can hold up to 50 pieces of numeric data. 
 Note If you call Obtain Queue inside a loop, this node creates a new reference each time the loop executes, and each new reference uses an additional four bytes of memory. To conserve memory, call Obtain Queue once before the loop executes.
 [IMAGE alt='image' src='GUID-245F4F1B-3FBD-425A-A6D9-4F445ABFE629-a5.svg']
 Use Enqueue Element in the producer loop to add data to the back of the queue. If the queue is full, the producer loop stops adding elements to the queue until Dequeue Element removes data. If the producer loop runs slower than the consumer loop, the queue will empty and result in an underflow. 
 Note If you want to ask a sensor for data at regular intervals instead of as often as possible, use Wait in the producer loop.
 [IMAGE alt='image' src='GUID-EE38CAD4-C25C-4C69-A3B4-5FD829627100-a5.svg']
 Use Dequeue Element in the consumer loop to remove data from the front of the queue so that data processes in the same order that it is added. If the queue is empty, the consumer loop waits to remove elements from the queue until Enqueue Element adds data. If the consumer loop runs slower than the producer loop, the queue will fill up and result in an overflow.
 [IMAGE alt='image' src='GUID-1C2B5505-1271-4422-8DB9-8B9B5154C5C4-a5.svg']
 Use Get Queue Status in the queue status loop to return information about the current state of the queue, such as the number of elements currently in the queue.
 Note Using this node in parallel code can result in race conditions which can cause incorrect logic control and data loss.
 [IMAGE alt='image' src='GUID-1CED6939-5ED1-4388-BEB8-FFF164BED4D0-a5.svg']
 Click the 
 Stop button on the panel. The queue status loop finishes executing and calls Release Queue. This node invalidates the queue reference which causes the producer and consumer loops to error out and finish executing. 
 Note Larger applications typically require a
 more sophisticated mechanism for stopping parallel
 loops. To see an example of such an architecture,
 launch the Queued Message Handler project in G Web
 Development Software.

#### Troubleshooting

- If a consumer loop processes data too slowly and results in an overflow, add a consumer loop to the diagram to raise the rate of data consumption.
- If a producer loop reads data too slowly and results in an underflow, raise the producer loop time if Wait is used. Otherwise add a producer loop to the diagram to raise the rate of data production.
- When multiple loops execute at the same time
 and change the same object, race conditions can occur which can result in data loss.
 Using Get Queue Status as a control mechanism that triggers an event
 between loops in code could result in race conditions if other loops change the contents
 of the queue before the event can be executed. This means that when the event does
 execute, it may do so based on outdated data and overwrite more current data. Improve
 the speed of your VI without the risk of creating race conditions by following the
 practices outlined in the Using Parallel Loops to Increase VI Execution Speed section of
 Strategies for Improving VI Execution Speed . Use an event structure as a
 safer way to trigger your code using event-driven programming.

Parent topic:

Repeating Operations

Related concepts:

- Strategies for Improving VI Execution Speed
- Event-Driven Programming

Related information:

- Obtain Queue
- Enqueue Element
- Dequeue Element
- Get Queue Status
- Release Queue

<!--NI_TOPIC bundle=g-web-development path=transferring-data-between-nodes.html language=enus -->
## TOPIC 00344: Wires: Transferring Data between Nodes

- bundle_id: `g-web-development`
- source_path: `transferring-data-between-nodes.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/transferring-data-between-nodes.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `concept`
- source_description: Wires transfer data between nodes on a diagram by connecting the output terminal of one node to one or more input terminals of another node. Wires have the following properties: A wire has a single data source. A wire can carry data from its single data source to more than one node that reads the da

### Wires: Transferring Data between Nodes

Wires transfer data between nodes on a diagram by connecting the output terminal of one node to one or more input terminals of another node.

Wires have the following properties:

- A wire has a single data source.
- A wire can carry data from its single data source to more than one node that reads the data as an input.
- The color, style, and thickness of a wire represent the type of data passing between nodes.

Parent topic:

Programming in G

<!--NI_TOPIC bundle=g-web-development path=tree-control-event-reference.html language=enus -->
## TOPIC 00345: Tree Control Event Reference

- bundle_id: `g-web-development`
- source_path: `tree-control-event-reference.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/tree-control-event-reference.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: The following events occur when the user performs an action that involves a tree control. Event Description Event Data Fields Item closed Occurs when the user closes an item in a tree control. Time—Value of the millisecond timer when the event occurred. Index—Index of the event source within an indi

### Tree Control Event Reference

The following events occur when the user performs an action that involves a tree control.

| Event | Description | Event Data Fields |
| --- | --- | --- |
| Item closed | Occurs when the user closes an item in a tree control. | Time—Value of the millisecond timer when the event occurred. Index—Index of the event source within an individual event diagram. Control Reference—Reference to the control on which the event occurred. Location—Hierarchical location of the closed item. Data—Data for the closed item, including the hierarchical location and associated data for the columns. |
| Item opened | Occurs when the user expands an item in a tree control. | Time—Value of the millisecond timer when the event occurred. Index—Index of the event source within an individual event diagram. Control Reference—Reference to the control on which the event occurred. Location—Hierarchical location of the expanded item. Data—Data for the expanded item, including the hierarchical location and associated data for the columns. |
| Selection changed | Occurs when the user selects or deselects one or more items in a tree control. | Time—Value of the millisecond timer when the event occurred. Index—Index of the event source within an individual event diagram. Control Reference—Reference to the control on which the event occurred. OldSelection—Hierarchical location of the previously selected item. This event data field can be a string or an array of strings, depending on the selection mode of the tree control. NewSelection—Hierarchical location of the selected item. This event data field can be a string or an array of strings, depending on the selection mode of the tree control. SelectedData—Data for the selected item, including the hierarchical location and associated data for the columns. This event data field can be a cluster or an array of clusters, depending on the selection mode of the tree control. |

Parent topic:

User Interface Events

<!--NI_TOPIC bundle=g-web-development path=tree-control.html language=enus -->
## TOPIC 00346: Tree

- bundle_id: `g-web-development`
- source_path: `tree-control.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/tree-control.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Group string data as a hierarchical list of items in multiple columns. The tree control is a 1D array of clusters. Each row of the tree is one cluster. The first element in the row represents the hierarchical location of the item in the tree, and subsequent elements represent data to display in each

### Tree

Group string data as a hierarchical list of items in multiple columns.

The tree control is a 1D array of clusters. Each row of the tree is one cluster. The first element in the row represents the hierarchical location of the item in the tree, and subsequent elements represent data to display in each column of the tree.

Use tree properties to write the column header or read and write selected items of the tree control.

[IMAGE alt='image' src='GUID-FFBC1FA4-4F9F-48A5-9C84-4ECDE63E95E3-a5.png']

#### How Do I Select Items in a Tree?

You can allow your users to select one or multiple items in the tree by placing a checkmark in the 
 Allow selection checkbox on the 
 Item tab. Use the Selection property to return information about the selected item(s).

#### How Do I Define the Hierarchy of a Tree?

You populate items in a tree using an array of clusters, as shown in the following figure.

[IMAGE alt='image' src='GUID-36550D72-2847-4334-B64D-E2C77411AE0B-a5.png']

The first element of each cluster is the hierarchical location of the item. The hierarchical location is a backslash-delimited string, where each segment of the delimited string denotes a level of hierarchy in the tree. Use the following general syntax to define a hierarchical location:

| Syntax | Definition |
| --- | --- |
| <empty string> or \\ | An empty string or backslash represents the root of the tree. |
| \\parent\\child or parent\\child | A leading backslash is equivalent to a location in the tree without a leading backslash. |
| parent\\child\\ or parent\\child | A trailing backslash is equivalent to a location in the tree without a trailing backslash. |
| Escape sequence or double backslash | Escape sequences for character representations, such as \\s to represent a space character, are not permitted. |

Parent topic:

Array Controls

<!--NI_TOPIC bundle=g-web-development path=triangle.html language=enus -->
## TOPIC 00347: Triangle

- bundle_id: `g-web-development`
- source_path: `triangle.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/triangle.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Create a customizable triangle.

### Triangle

Create a customizable triangle.

Parent topic:

Drawing Controls

<!--NI_TOPIC bundle=g-web-development path=troubleshooting-broken-wires.html language=enus -->
## TOPIC 00348: Troubleshooting Broken Wires

- bundle_id: `g-web-development`
- source_path: `troubleshooting-broken-wires.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/troubleshooting-broken-wires.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `task`
- source_description: A broken wire indicates that dataflow cannot run across the wire. You cannot run code that contains broken wires. Resolve each wire to make dataflow valid and run the code. Broken wires look like the following image. Make sure your code meets the following requirements to resolve each wire: Each wir

### Troubleshooting Broken Wires

A broken wire indicates that dataflow cannot run across the wire. You cannot run code that contains broken wires. Resolve each wire to make dataflow valid and run the code.

Broken wires look like the following image.

[IMAGE alt='image' src='GUID-E0101ADB-BC41-473D-9A17-67A9D283ED82-a5.png']

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
 Note 
 Remove Broken Wires deletes all broken wires, even those you might not see.

Parent topic:

Wires: Transferring Data between Nodes

<!--NI_TOPIC bundle=g-web-development path=two-dimensional-arrays.html language=enus -->
## TOPIC 00349: Two-Dimensional Arrays

- bundle_id: `g-web-development`
- source_path: `two-dimensional-arrays.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/two-dimensional-arrays.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `concept`
- source_description: A two-dimensional (2D) array stores elements in a grid. It requires a column index and a row index to locate an element. 2D array controls and indicators have two index displays to navigate to specific indexes. Top index display—Controls the row index to display in the array control. Bottom index di

### Two-Dimensional Arrays

A two-dimensional (2D) array stores elements in a grid. It requires a column index and a row index to locate an element.

[IMAGE alt='image' src='GUID-A4FFDB53-70C7-42BE-9DE3-0A960631B06B-a5.png']

2D array controls and indicators have two index displays to navigate to specific indexes.

[IMAGE alt='image' src='GUID-AF7CBC79-B871-4A95-B4A9-3BBBBD36F890-a5.png']

1. Top index display—Controls the row index to display in the array control.
2. Bottom index display—Controls the column index to display in the array control.
3. Element display—Values in the 2D array.

Parent topic:

Arrays

<!--NI_TOPIC bundle=g-web-development path=types-of-cors-requests.html language=enus -->
## TOPIC 00350: Types of Cross-Origin HTTP Requests

- bundle_id: `g-web-development`
- source_path: `types-of-cors-requests.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/types-of-cors-requests.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `concept`
- source_description: Cross-origin HTTP requests, either simple or non-simple, determine whether the browser asks the target web service before sending a request. Simple requests are cross-origin HTTP requests that do not require prior approval from the target web service before the request can be sent by the browser. An

### Types of Cross-Origin HTTP Requests

Cross-origin HTTP requests, either simple or non-simple, determine whether the browser
 asks the target web service before sending a request.

*Simple requests* are cross-origin HTTP requests that do not require prior approval from the target web service before the request can be sent by the browser. An HTTP request must meet the following criteria to execute as a simple request:

- Use a GET , HEAD , or POST node to make the request.
- Include only CORS-safelisted request-headers in
 the request.
- Set the Content-Type request header to one of the following values:
  - application/x-www-form-urlencoded
  - multipart/form-data
  - text/plain

*Non-simple requests* are cross-origin HTTP requests that must get approval from the target web service to send the actual HTTP request. The web browser sends a CORS 
 *preflight request* to the target web service to ask for approval. The response to the CORS preflight request determines if the web browser can proceed to send the actual HTTP request. A cross-origin HTTP request executes as a non-simple request if it violates any of the criteria for a simple request.

CORS also enables *credentialed requests*. Credentialed requests may use HTTP
 cookies and HTTP Authentication headers, or allow TLS client certificates. By default,
 browsers do not include credentials with a cross-origin HTTP request. However, you can
 use the Configure CORS node in a WebVI to include credentials with
 a cross-origin request. The Configure CORS node has no effect on
 same-origin HTTP requests.

Parent topic:

Considerations When Accessing Data from Web Services

Related tasks:

- Hosting a Web Application on the NI Application Web Server

Related information:

- Mozilla Developer Network - CORS
- HTTP Nodes
- Configure CORS

<!--NI_TOPIC bundle=g-web-development path=types-of-distributions.html language=enus -->
## TOPIC 00351: Types of Package Outputs

- bundle_id: `g-web-development`
- source_path: `types-of-distributions.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/types-of-distributions.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `concept`
- source_description: With a Package document (.lvdist), you can create a package or package installer to distribute applications and/or add-ons to clients. The following table helps you determine when to use a package or package installer. Output Type Definition File Type Installation Method Configuration Options Packag

### Types of Package Outputs

With a Package document (.lvdist), you can create a package or
 package installer to distribute applications and/or add-ons to clients.

The following table helps you determine when to use a package or package installer.

| Output Type | Definition | File Type | Installation Method | Configuration Options |
| --- | --- | --- | --- | --- |
| Package | A single compressed file containing software intended for installation on a target machine. | .nipkg | NI Package Manager or SystemLink Note In most cases, you must add the package to a feed that also includes the dependencies of the package before installing. | Add the package to a feed—clients of the software can subscribe to the feed and install the package from Package Manager via network access. |
| Package Installer | A folder containing the main software package, package dependencies, and an executable file that extracts the package and installs it on a target machine. Note By default, a package installer includes all of the package dependencies in the output so clients of the software can install the package without network access. | .exe | Run the package installer file. Note Web applications can be hosted and used directly via SystemLink. | Reference package dependencies using feeds instead of including the dependencies in the output—when a package installer that references feeds runs, it retrieves dependencies from the feed locations. Require installation of the exact hierarchy and versions of all the dependencies—when clients of the software install the package, the installer installs the exact versions of the dependencies found on the machine that built the package installer when it was built. Note This is recommended only for installing on a clean machine because it might upgrade or downgrade installed packages on the target machine. |

Parent topic:

Packaging an Application or Library

<!--NI_TOPIC bundle=g-web-development path=types-of-loops.html language=enus -->
## TOPIC 00352: Types of Loops

- bundle_id: `g-web-development`
- source_path: `types-of-loops.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/types-of-loops.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use the following loops to repeat code in G Dataflow: a For Loop and a While Loop. Loop Behavior Example Diagram For Loop Repeats the code inside the loop for a set number of iterations. Generate five random numbers between 1 and 10. While Loop Repeats the code inside the loop until a specif

### Types of Loops

You can use the following loops to repeat code in G Dataflow: a For Loop and a While Loop.

| Loop | Behavior | Example | Diagram |
| --- | --- | --- | --- |
| For Loop | Repeats the code inside the loop for a set number of iterations. | Generate five random numbers between 1 and 10. |  |
| While Loop | Repeats the code inside the loop until a specified condition is met. | Continue rolling a die until the value of the die is 6. |  |

Parent topic:

Repeating Operations

<!--NI_TOPIC bundle=g-web-development path=unflatten-icon-editor.html language=enus -->
## TOPIC 00353: Unflatten

- bundle_id: `g-web-development`
- source_path: `unflatten-icon-editor.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/unflatten-icon-editor.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Add an unflatten symbol to the icon.

### Unflatten

Add an unflatten symbol to the icon.

Parent topic:

Actions Palette

<!--NI_TOPIC bundle=g-web-development path=unlock-icon-editor.html language=enus -->
## TOPIC 00354: Unlock

- bundle_id: `g-web-development`
- source_path: `unlock-icon-editor.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/unlock-icon-editor.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Add an unlock symbol to the icon.

### Unlock

Add an unlock symbol to the icon.

Parent topic:

Actions Palette

<!--NI_TOPIC bundle=g-web-development path=updating-g-type-instances.html language=enus -->
## TOPIC 00355: Updating Custom Data Type Instances Throughout Your Project

- bundle_id: `g-web-development`
- source_path: `updating-g-type-instances.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/updating-g-type-instances.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `task`
- source_description: Modify a G Type document to update all the instances of a custom data type in your project. Open the G Type document that defines the control you want to modify. You can right-click an instance of the type definition control or constant you want to modify and select Open Type Definition to open the

### Updating Custom Data Type Instances Throughout Your Project

Modify a G Type document to update all the instances of a custom data type in your project.

1. Open the G Type document that defines the control you want to modify. 
 Tip You can right-click an instance
 of the type definition control or constant you want to modify and select
 Open Type Definition to open the associated G
 Type document. On the diagram, type definition controls and constants
 display a black marker on the left side to help you identify them.
2. In the G Type document, modify the control to your needs.
3. Save the G Type document to propagate the control updates to all instances of
 the type definition.

Parent topic:

Type Definitions

Related concepts:

- Type Definitions

Related tasks:

- Creating a Custom Data Type Using a G Type Document

<!--NI_TOPIC bundle=g-web-development path=use-vi-hier-doc.html language=enus -->
## TOPIC 00356: Viewing the Hierarchy of VIs in Your Application

- bundle_id: `g-web-development`
- source_path: `use-vi-hier-doc.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/use-vi-hier-doc.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `task`
- source_description: Open the Call Hierarchy document to see the hierarchy of VIs and subVIs and understand the calling relationships between them in your application. For example, you can use the Call Hierarchy document to see all of the VIs that call a specific VI and the subVIs that specific VI calls. This can be hel

### Viewing the Hierarchy of VIs in Your Application

Open the Call Hierarchy document to see the hierarchy of VIs and subVIs and understand the calling relationships between them in your application.

For example, you can use the Call Hierarchy document to see all of the VIs that call a specific VI and the subVIs that specific VI calls. This can be helpful when you need to debug a part of your application and want to see which subVIs are connected to each other.

1. Click 
 View»Call Hierarchy to open a Call Hierarchy document for your project. 
 Note Some callers may be hidden. Toggle the triangle icon below a node to show or hide callers.
2. (Optional) Click 
 Clean up diagram to change the visual arrangement of the hierarchy.
3. (Optional) Select a subVI to highlight its calling connections.
4. (Optional) Double-click a subVI displayed in the Call Hierarchy document to open it.

Parent topic:

Testing and Debugging

<!--NI_TOPIC bundle=g-web-development path=use-waveform-start-time.html language=enus -->
## TOPIC 00357: Use Waveform Start Time

- bundle_id: `g-web-development`
- source_path: `use-waveform-start-time.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/use-waveform-start-time.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the waveform start time as the beginning of the x-scale.

### Use Waveform Start Time

Use the waveform start time as the beginning of the x-scale.

Parent topic:

Creating User Interfaces

<!--NI_TOPIC bundle=g-web-development path=use-web-app-with-crio.html language=enus -->
## TOPIC 00358: Using a Web Application with a CompactRIO Device

- bundle_id: `g-web-development`
- source_path: `use-web-app-with-crio.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/use-web-app-with-crio.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `concept`
- source_description: Leverage the following architectures to use your web application with a CompactRIO device. Access a web application on your CompactRIO. Access a web application on a PC. Access a web application on the cloud. Use the following table to determine the best architecture for your system and web applicat

### Using a Web Application with a CompactRIO
 Device

Leverage the following architectures to use your web application with a
 CompactRIO device.

- Access a web application on your CompactRIO.
- Access a web application on a PC.
- Access a web application on the cloud.

Use the following table to determine the best architecture for your system and web
 application.

| Architecture | Use case | How to access | How to implement |
| --- | --- | --- | --- |
| Access a web application on your CompactRIO.Note You cannot use SystemLink APIs using this architecture. | Light-weight web applications:Browser-based simple configurationsHuman-machine interfaces | Enter the IP address of your CompactRIO in a browser on the same local network as the device. | Create and Access a LabVIEW Web Service on the CompactRIO. Follow the instructions for Hosting a Web Application on the NI Application Web Server. Follow the instructions for Configuring CORS for a LabVIEW Web Service for your LabVIEW Web Service running on a CompactRIO while developing the web application in G Web Development Software. Note NI recommends enabling CORS access to the LabVIEW Web Service only during development and disabling CORS access when deploying the web application to the CompactRIO. |
| Access a web application on a PC. | Use SystemLink Tag and Message APIs Avoid putting the server burden on your CompactRIO | Enter the IP address of the PC in a browser on the same local network as the PC and CompactRIO. | Access the data from your CompactRIO device using one of the following options:Follow the instructions in Communicating Data with Web Services Using WebVIs, such as SystemLink Tag and Message APIs.Follow the instructions in the Tutorial: Creating and Publishing a LabVIEW Web Service to the Application Web Server (Real-Time, Windows) on the PC. Follow the instructions for Hosting a Web Application on the NI Web Server Follow the instructions for Configuring CORS for a LabVIEW Web Service if your development PC and hosting PC are different machines. |
| Access a web application on the cloud. | Use a desktop or mobile device to access the web application over the internet | Enter the URL for the web application in a browser connected to the internet. | Use the NI Web Server and data services included with G Web Development Software to host a public internet accessible web server. Utilize a 3rd party service with public internet accessible web application hosting.Note You may need to configure a 3rd party server to support the application/wasm MIME type for files with the .wasm file extension. |

Parent topic:

Using Hardware with a Web Application

Related concepts:

- Configuring CORS for a LabVIEW Web Service
- Communicating Data with Web Services Using WebVIs

Related tasks:

- Hosting a Web Application on the NI Application Web Server

Related information:

- Tutorial: Creating and Publishing A LabVIEW Web Service to the Application Web
 Server (Real-Time, Windows)
- Tutorial: Creating and Publishing a LabVIEW Web Service to the Application
 Web Server (Real-Time, Windows)

<!--NI_TOPIC bundle=g-web-development path=user-icon-editor.html language=enus -->
## TOPIC 00359: User

- bundle_id: `g-web-development`
- source_path: `user-icon-editor.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/user-icon-editor.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Add a user symbol to the icon.

### User

Add a user symbol to the icon.

Parent topic:

Objects Palette

<!--NI_TOPIC bundle=g-web-development path=user-interface-events.html language=enus -->
## TOPIC 00360: User Interface Events

- bundle_id: `g-web-development`
- source_path: `user-interface-events.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/user-interface-events.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `concept`
- source_description: User interface events are events that occur when a user performs a particular action on the panel. Each time a user interface event occurs, the diagram executes the code you write for the event. Compared with polling the user interface in a loop for interactions, user interface events reduce the CPU

### User Interface Events

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

<!--NI_TOPIC bundle=g-web-development path=userinterface.html language=enus -->
## TOPIC 00361: Creating User Interfaces

- bundle_id: `g-web-development`
- source_path: `userinterface.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/userinterface.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `task`
- source_description: Create a user interface (UI) to allow a user to interact with a program. Use the Panel to design a UI for your program. Build UIs with controls and indicators. A control is an object that allows a user to input information into a program. An indicator is an object that gives the user information abo

### Creating User Interfaces

Create a user interface (UI) to allow a user to interact with a program.

Panel

Build UIs with controls and indicators. A
 *control* is an object that allows a user to input information into a
 program. An *indicator* is an object that gives the user information
 about the program.

1. Create a program in the Diagram.
2. Switch to the Panel.
3. From the Palette, add controls and indicators to the
 Panel. 
 Note Controls and indicators
 have different data types, including numeric, Boolean, and string.
 Right-click the control or indicator to replace it with another control or
 indicator of the same data type.
4. Switch to the Diagram.
5. In the Palette, click Unplaced
 Items to add terminals that correspond to your controls and
 indicators onto the diagram.
6. Wire the new terminals into your program.
7. Click Run.

Configuration
 pane

Parent topic:

Creating a Web Application

<!--NI_TOPIC bundle=g-web-development path=variant-control.html language=enus -->
## TOPIC 00362: Variant Control

- bundle_id: `g-web-development`
- source_path: `variant-control.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/variant-control.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Enter variant data.

### Variant Control

Enter variant data.

Parent topic:

Creating User Interfaces

<!--NI_TOPIC bundle=g-web-development path=variant-indicator.html language=enus -->
## TOPIC 00363: Variant Indicator

- bundle_id: `g-web-development`
- source_path: `variant-indicator.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/variant-indicator.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represent the variant data type.

### Variant Indicator

Represent the variant data type.

Parent topic:

Creating User Interfaces

<!--NI_TOPIC bundle=g-web-development path=variant.html language=enus -->
## TOPIC 00364: Variant

- bundle_id: `g-web-development`
- source_path: `variant.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/variant.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Add a variant data type symbol to the icon.

### Variant

Add a variant data type symbol to the icon.

Parent topic:

Data Types Palette

<!--NI_TOPIC bundle=g-web-development path=vertical-slider.html language=enus -->
## TOPIC 00365: Vertical Slider

- bundle_id: `g-web-development`
- source_path: `vertical-slider.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/vertical-slider.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Enter or display numeric data in a vertical slide.

### Vertical Slider

Enter or display numeric data in a vertical slide.

Parent topic:

Creating User Interfaces

<!--NI_TOPIC bundle=g-web-development path=vi-reentrancy.html language=enus -->
## TOPIC 00366: VI Reentrancy

- bundle_id: `g-web-development`
- source_path: `vi-reentrancy.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/vi-reentrancy.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can choose from three VI reentrancy options that determine how your subVI executes when it is called at more than one point in the dataflow at the same time. Reentrancy is the simultaneous execution of multiple calls for a subVI. By default, each call to the subVI is executed one after another.

### VI Reentrancy

You can choose from three VI reentrancy options that determine how your subVI executes when it is called at more than one point in the dataflow at the same time. Reentrancy is the simultaneous execution of multiple calls for a subVI.

By default, each call to the subVI is executed one after another. This may cause your application to execute slowly or have unexpected behavior. To allow multiple calls to a subVI to execute simultaneously, set a reentrant execution state for the subVI.

Refer to the following table to determine which VI reentrancy option is best for your subVI.

| What your subVI needs | Option(s) to use |
| --- | --- |
| Ability to maintain state | Stateful maintains state for each instance of the subVI. None maintains a single state across all instances of the subVI. |
| Minimize wait time when multiple VIs call your subVI at the same time | Stateful eliminates wait time completely. Stateless results in wait time if there are more calls to the subVI than there are clones. However, the wait time is always within a certain range. |
| Determinism, or the same wait time for each call to the subVI | Stateful guarantees the same exact wait time for each call to the subVI. This minimizes jitter in applications involving time-sensitive data. |
| Minimize memory usage | None uses the least memory. Stateless uses less memory than Stateful if your subVI needs the other features of reentrancy. |
| Minimize call overhead | Stateful is the most efficient for calling a subVI many times, such as within a loop. |

Parent topic:

SubVIs

<!--NI_TOPIC bundle=g-web-development path=vi-reference-lvmember.html language=enus -->
## TOPIC 00367: VI Reference

- bundle_id: `g-web-development`
- source_path: `vi-reference-lvmember.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/vi-reference-lvmember.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represent a reference to a VI whose behavior and properties you can control and pass to other VIs.

### VI Reference

Represent a reference to a VI whose behavior and properties you can control and pass to other VIs.

Parent topic:

Creating User Interfaces

<!--NI_TOPIC bundle=g-web-development path=wait-icon-editor.html language=enus -->
## TOPIC 00368: Wait

- bundle_id: `g-web-development`
- source_path: `wait-icon-editor.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/wait-icon-editor.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Add a wait symbol to the icon.

### Wait

Add a wait symbol to the icon.

Parent topic:

Actions Palette

<!--NI_TOPIC bundle=g-web-development path=waveform.html language=enus -->
## TOPIC 00369: Waveform

- bundle_id: `g-web-development`
- source_path: `waveform.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/waveform.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Group a timestamp, numeric array, and numeric control together to display waveform data.

### Waveform

Group a timestamp, numeric array, and numeric control together to display waveform data.

Parent topic:

Creating User Interfaces

<!--NI_TOPIC bundle=g-web-development path=waveforms.html language=enus -->
## TOPIC 00370: Waveforms

- bundle_id: `g-web-development`
- source_path: `waveforms.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/waveforms.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `concept`
- source_description: One common example of a cluster is the waveform. You might be familiar with the waveform data type if you have used it to collect data from a signal. On the diagram, waveform objects and wires appear brown. A waveform cluster is made up of three data types: a timestamp, an array of numerics, and a n

### Waveforms

One common example of a cluster is the waveform. You might be familiar with the waveform data type if you have used it to collect data from a signal.

On the diagram, waveform objects and wires appear brown.

[IMAGE alt='image' src='GUID-F70FC2E1-3D60-49DA-860C-772587780B72-a5.png']

A waveform cluster is made up of three data types: a timestamp, an array of numerics, and a numeric constant. You can use these three pieces of data to create a signal that you can plot on a chart or graph.

| Item | Details |
| --- | --- |
| t0 | Start time—A timestamp associated with the first measurement point in the waveform. |
| Y | Waveform data—An array of Y values associated with the waveform data. |
| dt | Delta t—The time interval in seconds between any two points in the signal. |

Because this data type is so common, you can access a waveform control from the palette on the panel, and you can access built-in nodes for waveforms from the palette on the diagram.

Parent topic:

Clusters: Building and Interacting with Grouped Data

<!--NI_TOPIC bundle=g-web-development path=what-is-a-subvi.html language=enus -->
## TOPIC 00371: SubVIs

- bundle_id: `g-web-development`
- source_path: `what-is-a-subvi.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/what-is-a-subvi.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `concept`
- source_description: After you build a VI, you can call it from the diagram of another VI within the same project. A VI called from the diagram of another VI is a subVI. SubVIs contain reusable code and simplify the diagrams of calling VIs. SubVIs are analogous to functions or subroutines in other programming languages.

### SubVIs

After you build a VI, you can call it from the diagram of another VI within the same project. 
 A VI called from the diagram of another VI is a 
 *subVI*. SubVIs contain reusable code and simplify the diagrams of calling VIs. SubVIs are analogous to functions or subroutines in other programming languages.

When you add an instance of a subVI to the diagram of another VI, the subVI appears as a single node, similar to a node from the palette. When data in the calling VI reaches the subVI node, the software executes the diagram of the subVI.

The following diagram shows two common situations that benefit from subVIs.

[IMAGE alt='image' src='GUID-4901C208-BA72-45FF-81C7-D511777122AF-a5.png']

1. Users may have difficulty understanding the purpose of this section of code because it performs several operations. The more complex a diagram, the more time it takes to interpret sections of code.
2. The same code appears in two different places. Repeated code increases the likelihood of errors. For example, if you change one section of repeated code, you must remember to make the same change everywhere the code section occurs.

The following diagram shows two solutions that subVIs provide.

[IMAGE alt='image' src='GUID-D10F49F5-A9AF-4187-B639-D13733311C30-a5.png']

1. The Coin Flip subVI represents the highlighted code inside the For Loop of the previous diagram. The subVI simplifies the diagram and communicates the purpose of the code through its label and node icon.
2. The Percentage subVI represents one of the duplicate sections of highlighted code from the previous diagram. The Percentage subVI performs the same function in two places without repeating code. If you change code in the VI called by the Percentage subVI, both instances of the subVI change.

Parent topic:

Programming in G

<!--NI_TOPIC bundle=g-web-development path=when-to-use-a-state-machine.html language=enus -->
## TOPIC 00372: When to Use a State Machine

- bundle_id: `g-web-development`
- source_path: `when-to-use-a-state-machine.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/when-to-use-a-state-machine.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can apply the state machine design pattern to a wide variety of programming tasks. The following tasks are examples of situations for which state machines are well suited: Responding to user interface interactions where the user's action determines which state executes. Process testing where eac

### When to Use a State Machine

You can apply the state machine design pattern to a wide variety of programming tasks.

The following tasks are examples of situations for which state machines are well suited:

- Responding to user interface interactions where the user's action determines which state executes.
- Process testing where each state carries out a step of the process.
- Breaking down difficult to manage applications into smaller, easily maintainable chunks of code.

However, a state machine is not well suited for every programming situation. If your program needs to run parallel processes, you may want to choose a different design pattern.

Parent topic:

State Machine Design Pattern

<!--NI_TOPIC bundle=g-web-development path=wiring-best-practices.html language=enus -->
## TOPIC 00373: Wiring Best Practices

- bundle_id: `g-web-development`
- source_path: `wiring-best-practices.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/wiring-best-practices.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `concept`
- source_description: Poor wire organization might not produce errors, but it can make the diagram difficult to read and debug or make the code appear to do things it does not do. Use these best practices as you develop your diagrams. Use a left-to-right and top-to-bottom layout. Although the positions of diagram element

### Wiring Best Practices

Poor wire organization might not produce errors, but it can make the diagram difficult to read and debug or make the code appear to do things it does not do.
 Use these best practices as you develop your diagrams.

- Use a left-to-right and top-to-bottom layout. Although the positions of diagram elements do not determine execution order, wiring from left to right keeps the diagram organized and easy to understand. Only wires and structures determine execution order.
- Control terminal wires should exit the right side of the terminal, and indicator terminal wires should enter on the left side of the terminal.
- Wire around objects. Do not cover wires with other objects.
- Use as few bends as possible.

Parent topic:

Wires: Transferring Data between Nodes

<!--NI_TOPIC bundle=g-web-development path=wiring-shortcuts.html language=enus -->
## TOPIC 00374: Wiring Shortcuts

- bundle_id: `g-web-development`
- source_path: `wiring-shortcuts.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/wiring-shortcuts.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: You can use the following set of shortcuts to help you create wires more efficiently. Editor Command Shortcut Action Remove Broken Wires Ctrl-B Delete all broken wires from the diagram. — Esc Right-click Ctrl-Z Delete a wire you are in the process of creating. — Single-click wire Select one wire seg

### Wiring Shortcuts

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

<!--NI_TOPIC bundle=g-web-development path=working-with-clusters.html language=enus -->
## TOPIC 00375: Clusters: Building and Interacting with Grouped Data

- bundle_id: `g-web-development`
- source_path: `working-with-clusters.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/working-with-clusters.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `concept`
- source_description: Like elements of arrays, elements of a cluster are ordered. Unlike elements of arrays, the elements of a cluster are not ordered by their positions in the cluster but by the order in which the elements are added to the cluster. The first object you place in the cluster is element 0, the second is el

### Clusters: Building and Interacting with Grouped Data

Like elements of arrays, elements of a cluster are ordered. Unlike elements of arrays, the elements of a cluster are not ordered by their positions in the cluster but by the order in which the elements are added to the cluster. The first object you place in the cluster is element 0, the second is element 1, and so on. You can verify the order of elements in a cluster and reorder them as desired.

A cluster groups data elements of mixed data types. Grouping related data
 elements into clusters allows you to keep them together while you program. For example,
 you can use a cluster to store a person's name, age, and whether the person is a student
 instead of storing this data in three separate controls.

The following images show Name,
 Age, and Student controls as
 individual elements versus the same controls in a single Census
 Cluster control.

| On the panel |  |
| --- | --- |
| On the diagram |  |

Parent topic:

Data Type Reference

<!--NI_TOPIC bundle=g-web-development path=write-icon-editor.html language=enus -->
## TOPIC 00376: Write

- bundle_id: `g-web-development`
- source_path: `write-icon-editor.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/write-icon-editor.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Add a write symbol to the icon.

### Write

Add a write symbol to the icon.

Parent topic:

Actions Palette

<!--NI_TOPIC bundle=g-web-development path=writing-multiple-plots.html language=enus -->
## TOPIC 00377: Writing Multiple Plots to a Graph or Chart

- bundle_id: `g-web-development`
- source_path: `writing-multiple-plots.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/writing-multiple-plots.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `task`
- source_description: Before you write multiple plots to a graph or chart, you must generate all the data sets you want to plot. Make sure each set of data has the same data type. Wire each set of data you want to plot to a Build Array node. Wire the appended array output from Build Array to a graph or chart indicator. I

### Writing Multiple Plots to a Graph or Chart

Before you write multiple plots to a graph or chart, you must generate all the data sets you want to plot. Make sure each set of data has the same data type.

1. Wire each set of data you want to plot to a Build Array node.
2. Wire the appended array output from Build Array to a graph or chart indicator. 
 If your data consists of numeric, complex, or cluster values, appended array is a 2D array. Each row of the array is a separate plot. If your data consists of waveforms, appended array is a 1D array. Each waveform is a separate plot.

Parent topic:

Creating User Interfaces
