# NI DOCUMENT BUNDLE: g-web-development

<!--NI_BUNDLE_CHUNK bundle=g-web-development start=1 end=250 -->
<!--NI_TOPIC bundle=g-web-development path=5-point-star.html language=enus -->
## TOPIC 00001: 5 Point Star

- bundle_id: `g-web-development`
- source_path: `5-point-star.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/5-point-star.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Create a customizable star.

### 5 Point Star

Create a customizable star.

Parent topic:

Drawing Controls

<!--NI_TOPIC bundle=g-web-development path=abort-icon-editor.html language=enus -->
## TOPIC 00002: Abort

- bundle_id: `g-web-development`
- source_path: `abort-icon-editor.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/abort-icon-editor.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Add an abort symbol to the icon.

### Abort

Add an abort symbol to the icon.

Parent topic:

Actions Palette

<!--NI_TOPIC bundle=g-web-development path=accessing-data-from-previous-loop-iteration.html language=enus -->
## TOPIC 00003: Accessing Data from the Previous Loop Iteration

- bundle_id: `g-web-development`
- source_path: `accessing-data-from-previous-loop-iteration.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/accessing-data-from-previous-loop-iteration.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `task`
- source_description: After a loop completes a single iteration, sometimes you want to use the value of one of its calculations in the next loop iteration. You can use a shift register to pass data from the most recent iteration to the next iteration. What to Use For Loop or While Loop Shift register What to Do Create th

### Accessing Data from the Previous Loop Iteration

After a loop completes a single iteration, sometimes you want to use the value of one of its calculations in the next loop iteration. You can use a shift register to pass data from the most recent iteration to the next iteration.

#### What to Use

- For Loop or While
 Loop
- Shift register

#### What to Do

Create the following diagram to pass data from the most recent loop iteration to the next iteration.

Customize the gray sections for your unique programming goals.

[IMAGE alt='image' src='GUID-FE5D4487-4136-40C2-B219-84990BFF4478-a5.png']

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

Related information:

- For Loop
- While Loop

<!--NI_TOPIC bundle=g-web-development path=accessing-resource-files-webvi.html language=enus -->
## TOPIC 00004: Accessing Resource Files from a WebVI

- bundle_id: `g-web-development`
- source_path: `accessing-resource-files-webvi.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/accessing-resource-files-webvi.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `task`
- source_description: You can include CSS, JavaScript, images, and other types of files in your web application and access them from a WebVI. For information about including JavaScript files for a JavaScript Library Interface document, refer to the Integrating a JavaScript File Into a Web Application help topic. Before y

### Accessing Resource Files from a WebVI

You can include CSS, JavaScript, images, and other types of files in your web application and access them from a WebVI.

Note

Before you begin, create or open a web application project.

1. In the 
 Project Files tab, right-click the application document file (.gcomp) and select 
 Import files. 
 Note You must save the application document before you can import files.
2. Navigate to the file you want to add and click 
 Open.
3. Open the WebVI you want to reference the resource file from, and choose one of the following options based on file type. 
 Type of fileHow to reference the file from your WebVICSS
 In the <head></head> tags, add the following lines of code:
 <link rel="stylesheet" href="my-style-sheet.css" />
 Refer to the Mozilla Developer Network for more information on using CSS to
 customize the appearance of your UI.JavaScript
 In the <head></head> tags, add the
 following lines of code:
 <script src="my-script.js"></script>
 Refer to the Mozilla Developer Network for more information on using JavaScript to
 add custom functionality to your web application.Image
 For images that are hosted externally, complete the following steps: 
 Switch to the panel and add a URL Image control to the panel.On the 
 Item tab, enter the path to your image file in the 
 Source URL field.
 For images on disk, complete the following steps: 
 Import the image into your application document file (.gcomp).Switch to the panel and drag the image from the 
 Project Files tab onto the Panel.

Parent topic:

Communicating Data with a Web Application

Related tasks:

- Integrating a JavaScript File Into a Web Application

Related information:

- Mozilla Developer Network

<!--NI_TOPIC bundle=g-web-development path=actions.html language=enus -->
## TOPIC 00005: Actions Palette

- bundle_id: `g-web-development`
- source_path: `actions.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/actions.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Add images related to actions to the icon.

### Actions Palette

Add images related to actions to the icon.

Parent topic:

Creating User Interfaces

<!--NI_TOPIC bundle=g-web-development path=add-custom-ui-palette-to-web-app-library.html language=enus -->
## TOPIC 00006: Adding a Custom UI Palette to Your Web Application Library

- bundle_id: `g-web-development`
- source_path: `add-custom-ui-palette-to-web-app-library.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/add-custom-ui-palette-to-web-app-library.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `task`
- source_description: Add custom UI elements you created with the Placeholder HTML Container to a palette in your web application library. Before you create a palette for your custom UI elements, complete the following tasks:Enable the preview feature—Navigate to File Preferences Preview Features and in the WebVI section

### Adding a Custom UI Palette to Your Web
 Application Library

Add custom UI elements you created with the Placeholder HTML Container to a palette in
 your web application library.

- Enable the preview feature—Navigate to File»Preferences»Preview Features and in the WebVI section, select Enable Placeholder HTML
 Containers in WebVI library palettes to enable this feature. Refer to
 Preview Features to learn more about G Web Development Software preview
 features.
- Use the Placeholder HTML Container and Obtain JavaScript Reference node to
 create custom UI elements for your web application.

Use a control definition file to make the
 custom UI elements you create available in the palette when someone installs
 your web application add-on.

1. Create or open a library in your web application project. 
 Tip Make
 sure this library has an extension of
 .gcomp and has a Web Server
 target.
2. Create a control definition file and add it to the
 library.
3. Add your Placeholder HTML Container to the control definition
 file and configure how you want it to appear when placed on
 the front panel. 
 Note If you
 use the Image URL option, you cannot use an image
 file in the library at deployment. You must use an
 image URL from the public internet or a
 self-contained data URL. If you try to reference an
 image file in the library component, it may not
 resolve in the correct location once
 deployed.
4. In the library with the control definition file selected, click
 Create palette file from the
 configuration pane.
5. Select G HTML panel palette for the
 palette type.
6. (Optional) Use the configuration pane to configure your
 palette.

Parent topic:

Building Shareable Libraries

Related concepts:

- Creating UI Elements with JavaScript

Related tasks:

- Preview Features

<!--NI_TOPIC bundle=g-web-development path=add-icon-editor.html language=enus -->
## TOPIC 00007: Add

- bundle_id: `g-web-development`
- source_path: `add-icon-editor.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/add-icon-editor.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Add an addition symbol to the icon.

### Add

Add an addition symbol to the icon.

Parent topic:

Actions Palette

<!--NI_TOPIC bundle=g-web-development path=adding-a-code-snippet-to-the-diagram.html language=enus -->
## TOPIC 00008: Adding a Code Snippet to the Diagram

- bundle_id: `g-web-development`
- source_path: `adding-a-code-snippet-to-the-diagram.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/adding-a-code-snippet-to-the-diagram.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `task`
- source_description: Use code snippets to drag sections of code onto your diagram. Before you begin, make sure you have any subVIs included in the code snippet in your project. Save the snippet to your machine. If you edit a snippet in an image editor, the editor will remove the VI information from the file and you will

### Adding a Code Snippet to the Diagram

Use code snippets to drag sections of code onto your diagram.

Before you begin, make sure you have any
 subVIs included in the code snippet in your project.

1. Save the snippet to your machine. 
 Note If you edit a snippet in an image editor, the editor will
 remove the VI information from the file and you will not be able to drop the
 snippet onto the diagram.
2. Open your project and navigate to the diagram of the VI you want to add the
 snippet to.
3. Drag the snippet from its location on your machine to the diagram. 
 The code depicted in the snippet appears on the diagram.

Parent topic:

Code Snippets

<!--NI_TOPIC bundle=g-web-development path=addressing-issues-with-numeric-conversions.html language=enus -->
## TOPIC 00009: Addressing Issues with Numeric Conversions

- bundle_id: `g-web-development`
- source_path: `addressing-issues-with-numeric-conversions.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/addressing-issues-with-numeric-conversions.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `task`
- source_description: When you wire numeric data to a node that expects a different numeric data type, the node coerces the data to the most precise type. A red coercion dot appears where the coercion takes place. Because numeric coercions can affect memory usage, performance of a VI, or cause a VI to generate inaccurate

### Addressing Issues with Numeric Conversions

When you wire numeric data to a node that expects a different numeric data type, the node coerces the data to the most precise type. A red coercion dot appears where the coercion takes place. Because numeric coercions can affect memory usage, performance of a VI, or cause a VI to generate inaccurate results, use one of the strategies in the following table to eliminate or reduce the impact of a problematic coercion.

| Strategy | Details | Action | Example |
| --- | --- | --- | --- |
| Match input data types. | Create an object that matches the data type the node expects. If you wire data from a G type to a node or subVI that does not accept the data type of the G type, your VI may break or generate inaccurate data. Replace the node or subVI with one that matches the data type used in the G type, or replace the G type with a constant of the matching data type. | Right-click the coerced control, constant, or indicator on the diagram, select Representation from the shortcut menu, and select the matching data type. | In the following diagram, the red coercion dot on the top input of the Add node indicates that the node is coercing I16 (x), a signed integer, to an unsigned integer to match the data type of U16 (y). This causes Add to return a sum of 65,531 instead of -5. If you change the data type representation of I16 (x) so that both inputs are signed integers, no coercion is necessary, and the node performs an accurate computation, as you can see in the following diagram. |
| Use a conversion node. | Conversion nodes convert one data type to another. Conversion nodes have the same effect as the automatic coercions that occur when you wire numeric data to a node that expects a different numeric data type. However, when you use a conversion node you can control where in your VI the conversion takes place, which can improve VI performance in certain cases. | To add a conversion node from the diagram palette, navigate to Data Types » Numeric » Conversion and select the desired conversion node. | You may want to use a conversion node inside a loop that generates an array so the conversion is performed before the VI generates the array. This allows you to avoid a large data buffer. In the following diagram, To Single Precision Float converts the Random Number output to a single-precision number inside the For Loop to prevent the Add node from converting a large amount of data. |

Parent topic:

Numeric Data

Related concepts:

- Numeric Conversions

<!--NI_TOPIC bundle=g-web-development path=adjusting-execution-speed.html language=enus -->
## TOPIC 00010: Adjusting the Execution Speed of a Loop

- bundle_id: `g-web-development`
- source_path: `adjusting-execution-speed.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/adjusting-execution-speed.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `task`
- source_description: By default, each loop iteration executes as quickly as possible based on the code inside the loop. However, you might want to control the rate at which a loop executes in order to specify a fixed time interval for each iteration, reduce the speed at which an indicator changes value, or conserve proc

### Adjusting the Execution Speed of a Loop

By default, each loop iteration executes as quickly as possible based on the code inside the loop.

#### What to Use

- While Loop or For
 Loop
- Wait

#### What to Do

Create the following diagram to adjust the execution speed of a loop.

Customize the gray sections for your unique programming goals.

[IMAGE alt='image' src='GUID-7C24DA22-841F-43AD-A7DC-B54E3F3AFA81-a5.png']

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

Related information:

- For Loop
- While Loop
- Wait

<!--NI_TOPIC bundle=g-web-development path=administrator-icon-editor.html language=enus -->
## TOPIC 00011: Administrator

- bundle_id: `g-web-development`
- source_path: `administrator-icon-editor.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/administrator-icon-editor.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Add an administrator symbol to the icon.

### Administrator

Add an administrator symbol to the icon.

Parent topic:

Objects Palette

<!--NI_TOPIC bundle=g-web-development path=advanced-icon-editor.html language=enus -->
## TOPIC 00012: Advanced

- bundle_id: `g-web-development`
- source_path: `advanced-icon-editor.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/advanced-icon-editor.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Add an advanced symbol to the icon.

### Advanced

Add an advanced symbol to the icon.

Parent topic:

Objects Palette

<!--NI_TOPIC bundle=g-web-development path=allow-no-selection-ni.listboxcommands.html language=enus -->
## TOPIC 00013: Allow no selection

- bundle_id: `g-web-development`
- source_path: `allow-no-selection-ni.listboxcommands.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/allow-no-selection-ni.listboxcommands.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Allow users to select zero items at run time.

### Allow no selection

Allow users to select zero items at run time.

Parent topic:

Creating User Interfaces

<!--NI_TOPIC bundle=g-web-development path=allow-no-selection.html language=enus -->
## TOPIC 00014: Allow no selection

- bundle_id: `g-web-development`
- source_path: `allow-no-selection.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/allow-no-selection.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Allow users to select zero items at run time.

### Allow no selection

Allow users to select zero items at run time.

Parent topic:

Creating User Interfaces

<!--NI_TOPIC bundle=g-web-development path=allow-selection-tree.html language=enus -->
## TOPIC 00015: Allow selection

- bundle_id: `g-web-development`
- source_path: `allow-selection-tree.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/allow-selection-tree.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Allow users to select a single row or multiple rows at run time.

### Allow selection

Allow users to select a single row or multiple rows at run time.

Parent topic:

Creating User Interfaces

<!--NI_TOPIC bundle=g-web-development path=analog-waveform.html language=enus -->
## TOPIC 00016: Analog Waveform

- bundle_id: `g-web-development`
- source_path: `analog-waveform.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/analog-waveform.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Add an analog waveform data type symbol to the icon.

### Analog Waveform

Add an analog waveform data type symbol to the icon.

Parent topic:

Data Types Palette

<!--NI_TOPIC bundle=g-web-development path=anti-aliased.html language=enus -->
## TOPIC 00017: Anti-aliased

- bundle_id: `g-web-development`
- source_path: `anti-aliased.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/anti-aliased.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Make line plots appear smoother. Anti-aliased drawing may not be visible over remote desktop.

### Anti-aliased

Make line plots appear smoother. Anti-aliased drawing may not be visible over remote desktop.

Parent topic:

Creating User Interfaces

<!--NI_TOPIC bundle=g-web-development path=api-design.html language=enus -->
## TOPIC 00018: API Design for Distributed APIs

- bundle_id: `g-web-development`
- source_path: `api-design.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/api-design.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Refer to the following table for best practices for designing VIs. Guideline Required or Recommended? Details Example(s) Include every public VI in your API in the API palette. Required Users may not look on disk to find advanced VIs. If a VI is not ready or intended for public consumption, make the

### API Design for Distributed APIs

Refer to the following table for best practices for designing VIs.

| Guideline | Required or Recommended? | Details | Example(s) |
| --- | --- | --- | --- |
| Include every public VI in your API in the API palette. | Required | Users may not look on disk to find advanced VIs. If a VI is not ready or intended for public consumption, make the VI private in the API component. | N/A |
| Do not use a VI in your API to open a dialog box unless that is the stated intent of the VI. | Required | N/A | N/A |
| If you expect multiple calls of your API VI to run in parallel, consider making the VI reentrant. | Recommended | If the VI stores any internal state in feedback nodes or uninitialized shift registers, make the VI reentrant and stateful, such as a preallocated clone. If the VI doesn't store any internal state, make it stateless, as a shared clone. | N/A |

Parent topic:

Best Practices for Designing and Developing an Application Programming Interface (API) in G Web Development Software

Parent topic:

Best Practices for Designing and Developing an Application Programming Interface (API) in G Web Development Software

Related concepts:

- Best Practices for Designing and Developing an Application Programming Interface (API) in G Web Development Software

<!--NI_TOPIC bundle=g-web-development path=applications.html language=enus -->
## TOPIC 00019: Applications

- bundle_id: `g-web-development`
- source_path: `applications.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/applications.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `concept`
- source_description: An application is a program designed to perform a group of coordinated functions or tasks. A web application is an application that is capable of running in web browsers. Use an Application document (.gcomp) to create an application from scratch or from existing code. The Application document contai

### Applications

An *application* is a program designed to
 perform a group of coordinated functions or tasks. A web application is an application that is
 capable of running in web browsers.

Use an *Application* document (.gcomp) to
 create an application from scratch or from existing code. The Application document
 contains your source files, such as VIs, text files, and other types of files.

You can build your application into HTML, JavaScript, and CSS that you share on web servers
 and run in web browsers outside the development environment.

Parent topic:

Creating a Web Application

<!--NI_TOPIC bundle=g-web-development path=applylicensing.html language=enus -->
## TOPIC 00020: applylicensing

- bundle_id: `g-web-development`
- source_path: `applylicensing.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/applylicensing.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Applies licensing to a component. To apply licensing to a component from the CLI, use the following syntax: gwebcli.exe applylicensing -c=<relative path to the component file> --ln=<license feature name> --lv=<version> For example: gwebcli.exe applylicensing -c="C:\Desktop\Web Application Project\We

### applylicensing

Applies licensing to a component.

To apply licensing to a component from the CLI, use the following syntax:

```text
        
          gwebcli.exe applylicensing -c=<relative path to the component file> --ln=<license feature name> --lv=<version>
      
```

For example:

```text
        
          gwebcli.exe applylicensing -c="C:\Desktop\Web Application Project\WebApp.gcomp\WebApp.gcomp" --ln="License" --lv="2" 
      
```

| Argument | Required | Description | Example |
| --- | --- | --- | --- |
| -c --cpath --compPath | Yes | This path must point directly to the component to be licensed. | -c="C:\\Desktop\\Web Application Project\\WebApp.gcomp\\WebApp.gcomp" --cpath="C:\\Desktop\\Web Application Project\\WebApp.gcomp\\WebApp.gcomp" --compPath="C:\\Desktop\\Web Application Project\\WebApp.gcomp\\WebApp.gcomp" |
| --ln --licenseFeatureName=VALUE | Yes | Specifies the component license in the corresponding license file (.lc). | --ln="License" --licenseFeatureName="License" |
| --lv --licenseVersion=VALUE | Yes | Specifies the version of the license in the license file (.lc) that corresponds to the component. | --lv="2" --licenseVersion="2" |
| --dp --dontProtectFiles | No | Specifies that we do not want to protect the source files under a component when we license it. By default, all the source files are protected when licensed. | — |

Parent topic:

Predefined Command Line Operations

<!--NI_TOPIC bundle=g-web-development path=arc.html language=enus -->
## TOPIC 00021: Arc

- bundle_id: `g-web-development`
- source_path: `arc.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/arc.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Draw a curved line.

### Arc

Draw a curved line.

Parent topic:

Drawing Controls

<!--NI_TOPIC bundle=g-web-development path=arrange.html language=enus -->
## TOPIC 00022: Arrange

- bundle_id: `g-web-development`
- source_path: `arrange.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/arrange.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Changes the dimensions of the cluster control.

### Arrange

Changes the dimensions of the cluster control.

Parent topic:

Creating User Interfaces

<!--NI_TOPIC bundle=g-web-development path=array-control.html language=enus -->
## TOPIC 00023: Array Controls

- bundle_id: `g-web-development`
- source_path: `array-control.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/array-control.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Group data elements of the same type. Examples An example of a simple array is a 1D text array that lists the eight planets of our solar system in order. Array elements are ordered. An array uses an index so you can readily access any particular element. The index is zero-based, which means it is in

### Array Controls

Group data elements of the same type.

[IMAGE alt='image' src='GUID-AFB17239-0E71-4021-A375-8676CEE39DD2-a5.png']

#### Examples

An example of a simple array is a 1D text array that lists the eight planets of our solar
 system in order.

Array elements are ordered. An array uses an index so you can readily access any particular
 element. The index is zero-based, which means it is in the range 0 to n -
 1, where n is the number of elements in the array. For example,
 n = 8 for the eight planets, so the index ranges from 0 to 7. Earth is
 the third planet, so it has an index of 2.

#### What Is an Array?

An array consists of elements and dimensions. Elements are the data that make up the array.
 A dimension is the length, height, or depth of an array. An array can have one to 32
 dimensions and as many as (2<sup>31</sup>) - 1 elements per dimension, memory permitting.
 You can build arrays of numeric, Boolean, path, string, waveform, and cluster data types.
 Input arrays are classified as controls by default and allow users to input data into the
 control. Output arrays are classified as indicators by default and display data on the
 panel.

#### When Should I Use an Array?

Consider using arrays when you work with a collection of similar data and when you perform
 repetitive computations. Arrays are ideal for storing data you collect from waveforms or
 data generated in loops, where each iteration of a loop produces one element of the array.

#### How Do I Find an Array Element?

To locate a particular element in an array, you must use indexes. Each dimension in the
 array has an index. Indexes let you navigate through an array and retrieve elements, rows,
 columns, and pages from an array on the diagram.

Note

#### How Do I Create a Multidimensional
 Array?

Specify Dimensions on the Item tab to define
 the dimension or size of the array.

#### How Do I Manipulate Array Data?

- Extracting individual data elements from an
 array.
- Inserting, deleting, or replacing data
 elements in an array.
- Splitting arrays.

You can use the Build Array node or a loop to build an array
 programmatically.

Parent topic:

Creating User Interfaces

<!--NI_TOPIC bundle=g-web-development path=array-controls.html language=enus -->
## TOPIC 00024: Array Controls

- bundle_id: `g-web-development`
- source_path: `array-controls.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/array-controls.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following image is an example of a one-dimensional numeric array control. Index display—Determines which element to display at the top of the array control. An array index is zero-based. Element display—Value in the array.

### Array Controls

The following image is an example of a one-dimensional numeric array control.

[IMAGE alt='image' src='GUID-D61DFC01-601A-43FC-9F5B-553B20AF380A-a5.png']

1. Index display—Determines which element to display at the top of the array control. An array index is zero-based.
2. Element display—Value in the array.

Parent topic:

Arrays

<!--NI_TOPIC bundle=g-web-development path=array.html language=enus -->
## TOPIC 00025: Array

- bundle_id: `g-web-development`
- source_path: `array.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/array.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Add an array data type symbol to the icon.

### Array

Add an array data type symbol to the icon.

Parent topic:

Data Types Palette

<!--NI_TOPIC bundle=g-web-development path=arrays.html language=enus -->
## TOPIC 00026: Arrays

- bundle_id: `g-web-development`
- source_path: `arrays.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/arrays.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `concept`
- source_description: An array combines data of the same data type into one data structure. An array consists of elements and dimensions. Elements are the data that make up the array. Dimensions represent the length, height, or depth of an array. Consider using arrays when you work with a collection of similar data and w

### Arrays

An 
 *array* combines data of the same data type into one data structure. An array consists of elements and dimensions. Elements are the data that make up the array. Dimensions represent the length, height, or depth of an array.

Consider using arrays when you work with a collection of similar data and when you perform repetitive computations. You can build arrays of numeric, Boolean, path, string, waveform, and cluster data types. You cannot create arrays of arrays. However, you can use a multidimensional array or create an array of clusters where each cluster contains one or more arrays.

[IMAGE alt='image' src='GUID-F3583466-6AA3-436B-AC52-878EDF6F47B7-a5.png']

Parent topic:

Data Type Reference

<!--NI_TOPIC bundle=g-web-development path=arrow.html language=enus -->
## TOPIC 00027: Arrow

- bundle_id: `g-web-development`
- source_path: `arrow.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/arrow.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Create a customizable arrow.

### Arrow

Create a customizable arrow.

Parent topic:

Drawing Controls

<!--NI_TOPIC bundle=g-web-development path=ask-icon-editor.html language=enus -->
## TOPIC 00028: Ask

- bundle_id: `g-web-development`
- source_path: `ask-icon-editor.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/ask-icon-editor.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Add an ask symbol to the icon.

### Ask

Add an ask symbol to the icon.

Parent topic:

Actions Palette

<!--NI_TOPIC bundle=g-web-development path=autoscale.html language=enus -->
## TOPIC 00029: Autoscale

- bundle_id: `g-web-development`
- source_path: `autoscale.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/autoscale.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adjust the scale automatically to reflect the data.

### Autoscale

Adjust the scale automatically to reflect the data.

Parent topic:

Creating User Interfaces

<!--NI_TOPIC bundle=g-web-development path=axes.html language=enus -->
## TOPIC 00030: Axes Ribbon Item

- bundle_id: `g-web-development`
- source_path: `axes.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/axes.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configure the axis or add a new axis.

### Axes Ribbon Item

Configure the axis or add a new axis.

Parent topic:

Creating User Interfaces

<!--NI_TOPIC bundle=g-web-development path=best-practices-api.html language=enus -->
## TOPIC 00031: Best Practices for Designing and Developing an Application Programming Interface (API) in G Web Development Software

- bundle_id: `g-web-development`
- source_path: `best-practices-api.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/best-practices-api.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `concept`
- source_description: To develop an API to distribute to other users that is consistent with NI style recommendations for G content, refer to the following best practice guidelines. You also need to follow best practices for designing projects in G Web Development Software if you want your API to be consistent with NI be

### Best Practices for Designing and Developing
 an Application Programming Interface (API) in G Web Development Software

To develop an API to distribute to other users that is consistent with NI style
 recommendations for G content, refer to the following best practice guidelines.

You also need to follow best practices for designing projects in G Web Development Software
 if you want your API to be consistent with NI best practice recommendations for G content.

Note

required

recommended

- [File Organization and Node Naming for Distributed APIs](file-organization-api.html) Refer to the following table for best practices for organizing files and naming nodes.
- [Component Organization for Distributed APIs](component-organization-api.html) Refer to the following table for best practices for organizing components.
- [Icons and Connector Panes for Distributed APIs](icons-connector-panes-api.html) Refer to the following table for best practices for creating icons and connector panes.
- [Data Type Selection for Distributed APIs](data-type-selection-api.html) Refer to the following table for best practices for selecting data types.
- [Palette Taxonomy for Distributed APIs](palette-taxonomy-api.html) Refer to the following table for best practices for palette taxonomy.
- [Documentation for Distributed APIs](documentation-api.html) Refer to the following table for best practices for documenting an API.
- [Error Message Design for Distributed APIs](error-messages-api.html) Refer to the following table for best practices for designing error messages.
- [API Design for Distributed APIs](api-design.html) Refer to the following table for best practices for designing VIs.

Parent topic:

Programming in G

Related concepts:

- Best Practices for Creating Projects in G Web Development Software

Related reference:

- Panel Design for G Web Development Software Projects

<!--NI_TOPIC bundle=g-web-development path=best-practices-customizing-controls-in-webvi.html language=enus -->
## TOPIC 00032: Best Practices for Customizing the Appearance of Controls in a WebVI

- bundle_id: `g-web-development`
- source_path: `best-practices-customizing-controls-in-webvi.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/best-practices-customizing-controls-in-webvi.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use a combination of configuration options in G Web Development Software, NI-defined custom properties, and browser-defined Cascading Style Sheet (CSS) properties to customize the controls in your WebVI. By following these best practices, you can create, edit, and maintain the appearance of your con

### Best Practices for Customizing the Appearance
 of Controls in a WebVI

Use a combination of configuration options in G Web Development Software,
 NI-defined custom properties, and browser-defined Cascading Style Sheet (CSS) properties
 to customize the controls in your WebVI. By following these best practices,
 you can create, edit, and maintain the appearance of your controls more easily.

Note

#### When to Use CSS Properties

- If the control supports the Configuration Pane UI to accomplish the same effect.
- If the control supports Property Node configuration to accomplish the same
 effect.

When G Web Development Software defines custom CSS properties, such as
 --ni-fill-background, you should use these over other browser-defined CSS
 properties whenever possible. You can use browser-defined CSS properties, such as
 font or margin, to format your controls if G Web
 Development Software configuration options are not available.

#### Styling
 Guidelines

Use the following guidelines to style your WebVI
 controls.

| Goal | How to implement |
| --- | --- |
| Style the entire page. | Select body |
| Style the panel canvas. | Select ni-front-panel |
| Style a specific control in my WebVI. | Set an HTML class attribute in the IDE and use that class selector in the CSS:.your_class_selector { --ni-true-background: yellow; --ni-true-foreground-color: #067bc2; }Note To use an HTML class attribute as a CSS class selector, you must prefix the class attribute with a period in the CSS. In the example above, the HTML class attribute referenced is your_class_selector. See MDN CSS Selectors for more information. |
| Style a group of controls in my WebVI. | Set multiple HTML class attributes in the IDE and apply the styles to those classes in the CSS:.activation-progress { font-weight: bold; } .activation-progress.warning { --ni-fill-background: yellow; } .activation-progress.danger { --ni-fill-background: red; }Note When specifying multiple HTML class attributes in the IDE, the list of classes must be space-delimited. In the example above, the HTML class attribute for the control is activation-progress. To make the control bold and yellow, you would use the HTML class attribute of activation-progress warning. Notice the class is not prefixed with a period and the class names are separated with a space. |

For recommendations on how to style specific controls, such as setting border styles on a
 button or configuring font styles in text boxes, see the *How do I customize a specific
 control on my WebVI Panel?* section of CSS Frequently Asked Questions.

Parent topic:

Customizing the Appearance of Controls in a WebVI

Related information:

- MDN CSS Selectors
- CSS Frequently Asked Questions

<!--NI_TOPIC bundle=g-web-development path=boolean-data.html language=enus -->
## TOPIC 00033: Boolean Data

- bundle_id: `g-web-development`
- source_path: `boolean-data.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/boolean-data.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `concept`
- source_description: Boolean data represents True and False values. On the diagram, Boolean values are represented by green objects and wires. On the panel, Boolean data is represented as switches or buttons with mechanical actions that represent physical switches and buttons.

### Boolean Data

Boolean data represents True and False values.

On the diagram, Boolean values are represented by green objects and wires.

[IMAGE alt='image' src='GUID-DE0DFD50-C59B-4038-8BE5-22A8FEAEF60D-a5.png']

On the panel, Boolean data is represented as switches or buttons with mechanical actions that represent physical switches and buttons.

Parent topic:

Data Type Reference

<!--NI_TOPIC bundle=g-web-development path=build-application.html language=enus -->
## TOPIC 00034: build-application

- bundle_id: `g-web-development`
- source_path: `build-application.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/build-application.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Builds the specified application into a binary. To build an application from the CLI, use the following syntax: gwebcli.exe build-application -p=<relative or absolute location of the project> -n=<name of the application> -t=<Web Server target containing the application> -s For example: gwebcli.exe b

### build-application

Builds the specified application into a binary.

To build an application from the CLI, use the following syntax:

```text
        
          gwebcli.exe build-application -p=<relative or absolute location of the project> -n=<name of the application> -t=<Web Server target containing the application> -s
      
```

For example:

```text
        
          gwebcli.exe build-application -p="C:\G Web Projects\Project.gwebproject" -n="Application.gcomp" -t="Default Web Server" -s
      
```

| Argument | Required | Description | Example |
| --- | --- | --- | --- |
| -p --path=VALUE | Yes | Specifies the relative or absolute path of the project containing the application to build. | -p="C:\\G Web Projects\\Project.gwebproject" --path="C:\\G Web Projects\\Project.gwebproject" |
| -n --name=VALUE | Yes | Specifies the name of the application to build. | -n="Application.gcomp" --name="Application.gcomp" |
| -t --target=VALUE | This argument is required if the project contains SystemDesigner targets. | The target that contains the application to build. This option is only required if the project contains SystemDesigner targets. | -t="Default Web Server" --target="Default Web Server" |
| -s --save | No | Saves the application and project file after building. Use this argument when you select Auto-increment version on build in the application. | — |

Parent topic:

Predefined Command Line Operations

<!--NI_TOPIC bundle=g-web-development path=build-library.html language=enus -->
## TOPIC 00035: build-library

- bundle_id: `g-web-development`
- source_path: `build-library.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/build-library.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Builds the specified library into a binary. To build a library from the CLI, use the following syntax: gwebcli.exe build-library -p=<relative or absolute location of the project> -n=<name of the library> -t For example: gwebcli.exe build-library -p="C:\G Web Projects\Project.gwebproject" -n="Library

### build-library

Builds the specified library into a binary.

To build a library from the CLI, use the following syntax:

```text
        
          gwebcli.exe build-library -p=<relative or absolute location of the project> -n=<name of the library> -t
      
```

For example:

```text
        
          gwebcli.exe build-library -p="C:\G Web Projects\Project.gwebproject" -n="Library.gcomp" -t
      
```

Note

build-library

| Argument | Required | Description | Example |
| --- | --- | --- | --- |
| -p --path=VALUE | Yes | Specifies the relative or absolute path of the project containing the library to build. | -p="C:\\G Web Projects\\Project.gwebproject" --path="C:\\G Web Projects\\Project.gwebproject" |
| -n --name=VALUE | Yes | Specifies the name of the library to build. | -n="Library.gcomp" --name="Library.gcomp" |
| -t --target=VALUE | This argument is required if the project contains SystemDesigner Web Server targets. | Specifies the SystemDesigner Web Server target that contains the library to build. | -t="Default Web Server" --target="Default Web Server" |
| -s --save | No | Saves the library and project file after building. Use this argument when you select Auto-increment version on build in the library. | — |

Parent topic:

Predefined Command Line Operations

<!--NI_TOPIC bundle=g-web-development path=build-shareable-library.html language=enus -->
## TOPIC 00036: Building Shareable Libraries

- bundle_id: `g-web-development`
- source_path: `build-shareable-library.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/build-shareable-library.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `task`
- source_description: Use your web application library to share reusable code. You can create an add-on for your web application and distribute it in a package using the following steps. Add all of the source files for your web application to the library. Ensure you create the library on the web server target. Add a HTML

### Building Shareable Libraries

Use your web application library to share reusable code.

You can create an add-on for your web
 application and distribute it in a package using the following steps.

1. Add all of the source files for your web application to the library. 
 Note Ensure you create the library on the
 web server target.
2. Add a HTML panel palette and all supporting functions to the web application
 library.
3. Add a palette with your custom UI elements to the web application
 library.
4. Build the web application library into a package or package installer.

Parent topic:

Libraries

Related tasks:

- Creating a Library
- Creating a Custom Palette
- Adding a Custom UI Palette to Your Web Application Library
- Packaging a Library

<!--NI_TOPIC bundle=g-web-development path=building-a-web-application.html language=enus -->
## TOPIC 00037: Building a Web Application as a Web Page

- bundle_id: `g-web-development`
- source_path: `building-a-web-application.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/building-a-web-application.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `task`
- source_description: To view your completed web application in a web browser, build your application to generate HTML, CSS, JavaScript, and other files that are included in your application. Open or create a web application project. On the Project Files tab, double-click the application document to open it. In the appli

### Building a Web Application as a Web
 Page

To view your completed web application in a web browser, build your application to generate HTML, CSS, JavaScript, and other files that are included in your application.

Open or create a web application
 project.

1. On the 
 Project Files tab, double-click the application document to open it.
2. In the application document, enable the 
 Top-level VI checkbox for each WebVI you want to output as a separate web page. 
 Each top-level WebVI in an application document generates one HTML file, which corresponds to one web page.
3. On the 
 Document tab, click 
 Build. 
 Monitor the status of your build in the 
 Build Queue tab.
4. On the Document tab click Run to view your
 top level VIs in a web browser.

To make your web application available to other users, host your build output on a web server that is accessible to other users.

Parent topic:

Creating a Web Application

Related tasks:

- Creating a Web Application
- Hosting a Web Application on a Server

<!--NI_TOPIC bundle=g-web-development path=button-controls-lv-member.html language=enus -->
## TOPIC 00038: Buttons Controls

- bundle_id: `g-web-development`
- source_path: `button-controls-lv-member.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/button-controls-lv-member.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Enter or display true and false data.

### Buttons Controls

Enter or display true and false data.

Parent topic:

Creating User Interfaces

<!--NI_TOPIC bundle=g-web-development path=button-controls.html language=enus -->
## TOPIC 00039: Button Controls

- bundle_id: `g-web-development`
- source_path: `button-controls.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/button-controls.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Enter or display true and false data. Which Button Should I Use? Button Type Use Default Mechanical Action Buttons Enter true or false input. Latch when released Checkbox Select an item or items from a list. Switch when released only Switches Enter true or false input in an application. Latch when r

### Button Controls

Enter or display true and false data.

[IMAGE alt='image' src='GUID-67CB3772-DD70-433F-ABD3-1FF5B137E804-a5.png']

#### Which Button Should I Use?

| Button Type | Use | Default Mechanical Action |
| --- | --- | --- |
| Buttons | Enter true or false input. | Latch when released |
| Checkbox | Select an item or items from a list. | Switch when released only |
| Switches | Enter true or false input in an application. | Latch when released |
| LEDs | Indicate true or false data. You must select Show values on the Item tab for content to appear on the LED. | Switch when released |

#### Which Mechanical Action Should I Use?

The mechanical action of the control determines how the control behaves. You classify mechanical actions as either switch actions or latch actions:

| I want my control to behave like a... | Mechanical Action | What This Mechanical Action Does | Caveats |
| --- | --- | --- | --- |
| Power button | Switch when pressed | Changes as soon as you click down on the control without waiting for you to release the mouse. |  |
| On/off switch | Switch when released | Changes the control value only after you release the mouse button within the graphical boundary of the control. | The mechanical action for radio buttons and checkboxes is not configurable; it is always switch when released. |
| Door buzzer | Switch until released | Changes the control value when you press it and retains the new value until you release the mouse button. | The frequency with which the program reads the control does not affect this behavior. You cannot select this behavior for a radio button control or a checkbox control. |
| Circuit breaker | Latch when pressed | Changes the control value when you press it and retains the new value until the program reads it once. | This behavior is useful for getting the program to perform an action only once each time you set the control. You cannot select this behavior for a radio button control or a checkbox control. |
| Dialog box button | Latch when released | Changes the control value only after you press and then release the mouse button within the graphical boundary of the control and retains the new value until the program reads it once. | This behavior is useful for stopping a While Loop. When the program reads the control once, the control reverts to its default value. You cannot select this behavior for a radio button control or a checkbox control. |

Parent topic:

Creating User Interfaces

<!--NI_TOPIC bundle=g-web-development path=calculate-icon-editor.html language=enus -->
## TOPIC 00040: Calculate

- bundle_id: `g-web-development`
- source_path: `calculate-icon-editor.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/calculate-icon-editor.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Add a calculate symbol to the icon.

### Calculate

Add a calculate symbol to the icon.

Parent topic:

Actions Palette

<!--NI_TOPIC bundle=g-web-development path=calibrate-icon-editor.html language=enus -->
## TOPIC 00041: Calibrate

- bundle_id: `g-web-development`
- source_path: `calibrate-icon-editor.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/calibrate-icon-editor.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Add a calibrate symbol to the icon.

### Calibrate

Add a calibrate symbol to the icon.

Parent topic:

Actions Palette

<!--NI_TOPIC bundle=g-web-development path=calling-js-functions-web-app.html language=enus -->
## TOPIC 00042: Calling JavaScript Functions in a Web Application

- bundle_id: `g-web-development`
- source_path: `calling-js-functions-web-app.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/calling-js-functions-web-app.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `task`
- source_description: Use a JavaScript Library Interface (JSLI) to call globally accessible JavaScript functions in your web application. A JSLI is a document in which you create entry points, or defined calls, to JavaScript functions. When you create a new entry point, a visual representation of the entry point appears

### Calling JavaScript Functions in a Web Application

Use a JavaScript Library Interface (JSLI) to call globally accessible JavaScript functions in your web application.

A JSLI is a document in which you create 
 *entry points*, or defined calls, to JavaScript functions.

When you create a new entry point, a visual representation of the entry point appears on the software palette of the diagram. You can place and wire entry points like nodes.

As the web application executes, the entry point calls the JavaScript function. Input data passes from the diagram to the JavaScript function, and output data returns from the JavaScript function to the diagram.

Complete the following tasks to call JavaScript functions in your web application:

1. (Optional): Create wrapper code for the JavaScript file you want
 to use.
2. Define the JavaScript functions you want to call in your web application.
3. Connect the JavaScript file to your web application and create calls to the JavaScript
 functions you defined in the JSLI.
4. (Optional): Add code to your JavaScript file to use asynchronous
 JavaScript calls in your WebVI.

#### Examples

Search within the programming environment to access the following installed example:

- *Call JavaScript From a WebVI*

If you encounter issues after you create a JSLI and add entry points to your web
 application, debug the interface to address common issues with JSLIs.

1. Preparing Your Code For Use With a JavaScript Library Interface Create wrapper code, if necessary, to make your JavaScript functions compatible with the JavaScript Library Interface (JSLI).
2. Defining Calls to JavaScript Functions using a JavaScript Library Interface To call JavaScript functions in your web application, define calls to the JavaScript functions using a JavaScript Library Interface (JSLI) document.
3. Integrating a JavaScript File Into a Web Application Connect a JavaScript file to your web application and call functions you defined in a JavaScript Library Interface (JSLI) in your web application.
4. Waiting for Asynchronous JavaScript Operations to Complete in a Web Application Use asynchronous JavaScript code to wait on tasks or requests while the rest of the code in your WebVI continues to execute.
5. Debugging JavaScript Library Interfaces Solve common problems that may occur when configuring and using JavaScript Library Interfaces (JSLIs).

Parent topic:

Using JavaScript with a Web Application

<!--NI_TOPIC bundle=g-web-development path=callout-icon-editor.html language=enus -->
## TOPIC 00043: Callout

- bundle_id: `g-web-development`
- source_path: `callout-icon-editor.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/callout-icon-editor.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Create a customizable callout.

### Callout

Create a customizable callout.

Parent topic:

Shapes Palette

<!--NI_TOPIC bundle=g-web-development path=capture-package-dependencies.html language=enus -->
## TOPIC 00044: Capturing the Package Dependencies of a Project

- bundle_id: `g-web-development`
- source_path: `capture-package-dependencies.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/capture-package-dependencies.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `task`
- source_description: Identify the packages a project requires and store a list of those packages in the Package Dependencies document. On the Project Files tab, right-click the project and select Capture package dependencies. The Package Dependencies document opens, scans the project, and displays a list of packages the

### Capturing the Package Dependencies of a Project

Identify the packages a project requires and store a list of those packages in the Package Dependencies document.

1. On the 
 Project Files tab, right-click the project and select 
 Capture package dependencies. 
 The Package Dependencies document opens, scans the project, and displays a list of packages the project requires.
2. (Optional) Make changes to the project, return to the Package Dependencies document, and click 
 Recapture dependencies.
3. Click 
 File»Save all.

After you capture the package dependencies of a project, copy the project folder, save it on another development system, and use the Package Dependencies document to resolve package dependencies on that system.

Parent topic:

Package Dependencies

Parent topic:

Sharing a Project and Including Package Dependencies

Related tasks:

- Sharing a Project and Including Package Dependencies
- Resolving Missing or Mismatched Package Dependencies on a Development System

<!--NI_TOPIC bundle=g-web-development path=centering-cursor.html language=enus -->
## TOPIC 00045: Centering a Cursor on a Graph or Chart

- bundle_id: `g-web-development`
- source_path: `centering-cursor.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/centering-cursor.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `task`
- source_description: If you cannot locate a cursor that you added to your graph or chart, you can reset the cursor position to the center of your graph or chart. Use the cursor legend to center a cursor. Cursors are not available for intensity graphs. If you do not see the cursor legend, select Cursor Legend in the Part

### Centering a Cursor on a Graph or Chart

If you cannot locate a cursor that you added to your graph or chart, you can reset the cursor position to the center of your graph or chart. 
 Use the cursor legend to center a cursor.

Note

1. If you do not see the cursor legend, select 
 Cursor Legend in the 
 Parts section on the 
 Item tab for the graph or chart.
2. On the 
 Cursor Legend, navigate to the cursor you want to center.
3. Ensure the 
 Visible? button 
 [IMAGE alt='image' src='GUID-84751343-7EE6-486F-A777-F1C856AEF72C-a5.png'] is selected.
4. Click the 
 Center Cursor button 
 [IMAGE alt='image' src='GUID-411CDB0C-8C52-4E4D-A260-7A6E5EB3C478-a5.png'] to center the cursor.

Parent topic:

Creating User Interfaces

<!--NI_TOPIC bundle=g-web-development path=centralized-scc-recommendations.html language=enus -->
## TOPIC 00046: Recommendations for Interacting with a Centralized Source Code Control System while Developing a Project

- bundle_id: `g-web-development`
- source_path: `centralized-scc-recommendations.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/centralized-scc-recommendations.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Learn how to interact with a centralized source code control provider while developing a project. You can apply these concepts when interacting with any centralized source code control provider. Checking Out Files and Making Modifications Recommendation Details Lock webVI files to prevent other deve

### Recommendations for Interacting with a Centralized Source Code Control System while Developing a Project

Learn how to interact with a centralized source code control provider while developing a project.

Note

#### Checking Out Files and Making Modifications

| Recommendation | Details |
| --- | --- |
| Lock webVI files to prevent other developers from making simultaneous changes. | Locking webVI files when you check them out reduces the chances of code-breaking merge conflicts. |
| Update your local copy of the project regularly during development. | Keeping your local copy of the project in sync with the central repository ensures you are developing code against the most recent version of the project. Use the <centralized source control provider> update command, where <centralized source control provider> is, replace with the name of your provider. |
| Exit G Web Development Software before updating your remote copy. | If you leave G Web Development Software open when you update your local copy, it is possible to corrupt files in the project. |

#### Checking In Files

| Recommendation | Details |
| --- | --- |
| Check in all files within the project folder that have changes. | You may notice that some files have changes even if you did not modify them. In particular, the project file will frequently change due to changes in other files. Your source code control provider should scan the project folder for changes. Use this feature to identify all files with modifications. |
| Ignore the following directories when you submit to the central repository: Builds.cache | Changes within these sub-directories do not affect the functionality of source code in the project. The project directory in the central repository may already be configured to ignore the folders. If not, use commands to configure your source code control provider to ignore the folders. |
| Add a descriptive comment to your commit. | Descriptive comments help you and other developers interpret changes you submit to the repository. |
| After you commit files to the repository, notify other team members. | Other developers may need to change their code based on changes you make. Some collaboration tools, as well as some source code control systems, can auto-generate emails when changes to the repository occur. |

Parent topic:

Recommendations for Developing a Project Stored in a Source Code Control Repository

<!--NI_TOPIC bundle=g-web-development path=certificate-icon-editor.html language=enus -->
## TOPIC 00047: Certificate

- bundle_id: `g-web-development`
- source_path: `certificate-icon-editor.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/certificate-icon-editor.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Add a certificate symbol to the icon.

### Certificate

Add a certificate symbol to the icon.

Parent topic:

Objects Palette

<!--NI_TOPIC bundle=g-web-development path=chart-control.html language=enus -->
## TOPIC 00048: Chart Control

- bundle_id: `g-web-development`
- source_path: `chart-control.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/chart-control.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Chart numeric data by displaying a history of values. How is Charting Different Than Plotting? Graphs and charts differ in the way they display and update data. VIs with a graph usually collect the data in an array and then plot the data to the graph. This process is similar to a spreadsheet that fi

### Chart Control

Chart numeric data by displaying a history of values.

[IMAGE alt='image' src='GUID-998D1272-BA2D-4196-9653-B8E6CDFC9EF7-a5.png']

#### How is Charting Different Than Plotting?

Graphs and charts differ in the way they display and update data. VIs with a graph usually collect the data in an array and then plot the data to the graph. This process is similar to a spreadsheet that first stores the data then generates a plot of it. When the data is plotted, the graph discards the previously plotted data and displays only the new data.

In contrast, a chart appends new data points to those points already in the display to create a history or a buffer. On a chart, you can see the current reading or measurement in context with data previously acquired. When more data points are added than can be displayed on the chart, the chart scrolls so that new points are added to the right side of the chart while old points disappear to the left.

#### What Types of Data Can I Chart?

You can chart numeric data contained in arrays and analog waveforms. By default, the chart data type is an array of doubles. You can change the data type on the diagram.

The waveform data type carries the start time (t0), delta t (dt), and y-values (Y) of a waveform. When you wire waveform data to a chart, the chart automatically plots a waveform based on the start time, delta t, and y-values of the waveform. A waveform that specifies 
 t0 and a single-element 
 Y array is useful for plotting data that is not evenly sampled because each data point has its own time stamp.

For data contained in arrays, the chart displays a general-purpose Cartesian graph that charts any set of points, evenly sampled or not.

The following table describes how different types of array data are charted.

| Data Type | Plot Behavior |
| --- | --- |
| Scalar numeric value | The chart displays a single plot using the scaler numeric value as the most recent value and previous values up to the history length. |
| 1D array of numeric values | The array is a single plot. X-value: Array index Y-value: Array element |
| Cluster of numeric values | Each element of the cluster is a single plot which uses the numeric value as the most recent value and previous values up to the history length. |
| 1D array of clusters of numeric values | Each element of the cluster is a single plot which uses the numeric value as the most recent value and previous values up to the history length. The array represents an aggregated set of samples. |
| 1D array of waveforms | Each waveform is a separate plot. This data type is not supported. |
| 2D array of numeric values | Each column of the array is a separate plot. |

#### How Do I Define the Chart History Length?

On the 
 Item tab, in the 
 Behavior section, specify 
 History length to configure the size of the buffer. For waveforms, the history length is the number of individual waveforms the buffer can hold. The waveforms can be of various sample sizes. For numeric data, the history length is the number of samples the buffer can hold.

Parent topic:

Charts and Graphs

<!--NI_TOPIC bundle=g-web-development path=charts-and-graphs.html language=enus -->
## TOPIC 00049: Charts and Graphs

- bundle_id: `g-web-development`
- source_path: `charts-and-graphs.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/charts-and-graphs.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Chart and plot data. What Is the Difference between Graphs and Charts? You can collect data, usually in an array, and then plot the data to a graph. This process is similar to a spreadsheet that first stores the data and then generates a plot of it. A chart appends new data points to those points al

### Charts and Graphs

Chart and plot data.

[IMAGE alt='image' src='GUID-8410F478-BE1A-457B-A198-A4EA7CB22028-a5.png']

#### What Is the Difference between Graphs
 and Charts?

You can collect data, usually in an array, and then plot the data to a graph. This
 process is similar to a spreadsheet that first stores the data and then generates a plot
 of it.

A chart appends new data points to those points already in the display to create a
 history. On a chart, you can see the current reading or measurement in context with data
 previously acquired.

#### Deciding Which Graph or Chart to Use

Knowing what type of data you need to display determines the type of graph or chart you should use.

| Control | Accepted Data Types | Display Examples | When to Use |
| --- | --- | --- | --- |
| Graph | Numeric, complex, X/Y, or point sample data contained in arrays and analog waveforms | Analog waveform data acquired at a constant rate | Use a graph for fast processes that acquire data continuously. |
| Chart | Numeric data contained in arrays and analog waveforms | Analog waveform data acquired at a constant rate with a history, or buffer, of the data from previous updates | Use a chart for processes that require a cumulative history of incremental updates to be maintained. |
| Intensity Graph | 3D data on a 2D plot by using color to display the values of the third dimension | Patterned data, such as frequency of sound intensity | Use an intensity graph for 3D data. |

#### Autoscaling

You can enable autoscaling for graphs and charts, which means they adjust their horizontal or vertical scales to fit the data you wire to them. Graphs and charts support the following types of autoscaling:

- Fit exactly —Fits the end markers to the exact minimum and maximum values of the data.
- Fit loosely —Rounds the end markers to a multiple of the increment used for the scale.
- Grow only —Fits the end markers to the minimum and maximum values of the data at run time. This type of autoscaling is available only for the vertical axis of graph, chart, and intensity graph.

Parent topic:

Creating User Interfaces

Related tasks:

- Clearing Indicator Display Data in a Chart, Graph, or Array

<!--NI_TOPIC bundle=g-web-development path=check-mark-icon-editor.html language=enus -->
## TOPIC 00050: Check Mark

- bundle_id: `g-web-development`
- source_path: `check-mark-icon-editor.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/check-mark-icon-editor.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Add a check mark to the icon.

### Check Mark

Add a check mark to the icon.

Parent topic:

Objects Palette

<!--NI_TOPIC bundle=g-web-development path=choose-right-vi-reentrancy.html language=enus -->
## TOPIC 00051: Choosing the Right VI Reentrancy Option for a SubVI

- bundle_id: `g-web-development`
- source_path: `choose-right-vi-reentrancy.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/choose-right-vi-reentrancy.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `task`
- source_description: On the Document tab, in the Behavior section, click Properties to access VI Reentrancy options for your subVI. In the resulting dialog box, select the Execution tab. Choose one of the following options: Option Description None Allocates a single data space for use by all instances of the subVI. Ther

### Choosing the Right VI Reentrancy Option for a SubVI

1. On the 
 Document tab, in the 
 Behavior section, click 
 Properties to access VI Reentrancy options for your subVI.
2. In the resulting dialog box, select the 
 Execution tab.
3. Choose one of the following options: 
 OptionDescriptionNone
 Allocates a single data space for use by all instances of the subVI. Therefore, the software executes multiple, simultaneous calls to a subVI one at a time in an indeterminate order. Because every instance of the subVI shares the same data space, all calls to the subVI also share a single state, which preserves the values of controls and uninitialized shift registers among calls.Stateless
 Allocates one copy, or clone, of the subVI for each processor on your machine. Each call to the subVI can then access one of these shared clones instead of waiting on the main subVI. If there are not enough shared clones for each call to the subVI, additional clones are allocated on demand. Each instance of the subVI may access a different clone each time it is called.Stateful
 Allocates a separate clone for each instance of the subVI. Each instance of the subVI stores data in its own pre-allocated clone.

Parent topic:

SubVIs

<!--NI_TOPIC bundle=g-web-development path=circle.html language=enus -->
## TOPIC 00052: Circle

- bundle_id: `g-web-development`
- source_path: `circle.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/circle.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Create a customizable circle.

### Circle

Create a customizable circle.

Parent topic:

Drawing Controls

<!--NI_TOPIC bundle=g-web-development path=classobjcont.html language=enus -->
## TOPIC 00053: Class Object Control

- bundle_id: `g-web-development`
- source_path: `classobjcont.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/classobjcont.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: A control or indicator of a user-defined class type.

### Class Object Control

A control or indicator of a user-defined class type.

Parent topic:

Creating User Interfaces

<!--NI_TOPIC bundle=g-web-development path=clear-data.html language=enus -->
## TOPIC 00054: Clearing Indicator Display Data in a Chart, Graph, or Array

- bundle_id: `g-web-development`
- source_path: `clear-data.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/clear-data.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `task`
- source_description: Right-click the chart, graph, or array and select Clear Data to remove all data from the indicator displays.

### Clearing Indicator Display Data in a Chart, Graph, or Array

Clear Data

Parent topic:

Creating User Interfaces

<!--NI_TOPIC bundle=g-web-development path=cli-global-arguments.html language=enus -->
## TOPIC 00055: Global Arguments

- bundle_id: `g-web-development`
- source_path: `cli-global-arguments.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/cli-global-arguments.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Refer to the table below for a list of arguments you can use when executing an operation with the command line interface. All arguments are case-sensitive. Argument Description Example -v --verbose Increases the detail of the output log. gwebcli.exe build-application -p "C:\G Web Projects\Project.gw

### Global Arguments

Refer to the table below for a list of arguments you can use when executing an operation with the command line interface.

Note

| Argument | Description | Example |
| --- | --- | --- |
| -v --verbose | Increases the detail of the output log. | gwebcli.exe build-application -p "C:\\G Web Projects\\Project.gwebproject" -n "Application.gcomp" -v |

Parent topic:

Running Operations Using the Command Line Interface

<!--NI_TOPIC bundle=g-web-development path=clock-icon-editor.html language=enus -->
## TOPIC 00056: Clock

- bundle_id: `g-web-development`
- source_path: `clock-icon-editor.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/clock-icon-editor.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Add a clock symbol to the icon.

### Clock

Add a clock symbol to the icon.

Parent topic:

Objects Palette

<!--NI_TOPIC bundle=g-web-development path=clockwise.html language=enus -->
## TOPIC 00057: Clockwise

- bundle_id: `g-web-development`
- source_path: `clockwise.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/clockwise.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Increase angles in a clockwise direction.

### Clockwise

Increase angles in a clockwise direction.

Parent topic:

Creating User Interfaces

<!--NI_TOPIC bundle=g-web-development path=close-icon-editor.html language=enus -->
## TOPIC 00058: Close

- bundle_id: `g-web-development`
- source_path: `close-icon-editor.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/close-icon-editor.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Add a close symbol to the icon.

### Close

Add a close symbol to the icon.

Parent topic:

Actions Palette

<!--NI_TOPIC bundle=g-web-development path=cluster-controls-error-in.html language=enus -->
## TOPIC 00059: Error In

- bundle_id: `g-web-development`
- source_path: `cluster-controls-error-in.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/cluster-controls-error-in.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Group a checkbox, numeric indicator, and textbox to input error information.

### Error In

Group a checkbox, numeric indicator, and textbox to input error information.

Parent topic:

Creating User Interfaces

<!--NI_TOPIC bundle=g-web-development path=cluster-controls-error-out.html language=enus -->
## TOPIC 00060: Error Out

- bundle_id: `g-web-development`
- source_path: `cluster-controls-error-out.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/cluster-controls-error-out.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Group a checkbox, numeric indicator, and textbox to display error information.

### Error Out

Group a checkbox, numeric indicator, and textbox to display error information.

Parent topic:

Creating User Interfaces

<!--NI_TOPIC bundle=g-web-development path=cluster.html language=enus -->
## TOPIC 00061: Cluster

- bundle_id: `g-web-development`
- source_path: `cluster.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/cluster.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Add a cluster data type symbol to the icon.

### Cluster

Add a cluster data type symbol to the icon.

Parent topic:

Data Types Palette

<!--NI_TOPIC bundle=g-web-development path=clusters.html language=enus -->
## TOPIC 00062: Cluster Controls

- bundle_id: `g-web-development`
- source_path: `clusters.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/clusters.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Group data elements of a mixed type that logically belong together. What Is a Cluster? Clusters group data elements of mixed types. A cluster is similar to a record or a struct in text-based programming languages. Which Cluster Should I Use? You can choose from the following cluster types, and clust

### Cluster Controls

Group data elements of a mixed type that logically belong together.

[IMAGE alt='image' src='GUID-90EA61A3-0E2B-4ED4-8E71-BBD98C7C9C18-a5.png']

#### What Is a Cluster?

Clusters group data elements of mixed types. A cluster is similar to a record or a struct in text-based programming languages.

#### Which Cluster Should I Use?

You can choose from the following cluster types, and clusters can be nested:

| Use | Type |
| --- | --- |
| Groups a checkbox, numeric control, and string control together to input error information. | Error In |
| Groups a checkbox, numeric indicator, and string control together to display error information. | Error Out |
| Groups a timestamp, numeric array, and numeric control together to display waveform data. | Waveform |
| Create a custom group by dragging and dropping controls, such as buttons, graphs, arrays, and so on, into the cluster shell. | Empty Cluster |

#### How Do I Reorder Cluster Elements?

You can reorder cluster elements by using the 
 Data items section on the 
 Item tab or by moving controls inside or outside the cluster. The order of the controls within the cluster is determined by the order in which you add them to the cluster.

Parent topic:

Creating User Interfaces

<!--NI_TOPIC bundle=g-web-development path=code-snippets.html language=enus -->
## TOPIC 00063: Code Snippets

- bundle_id: `g-web-development`
- source_path: `code-snippets.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/code-snippets.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `concept`
- source_description: A code snippet is a PNG image of code that includes the functionality of a VI file. You can drag a snippet directly onto the diagram and G Web Development Software populates the code depicted in the snippet. You can embed snippets in documents, forum posts, and emails to quickly share and collaborat

### Code Snippets

A *code snippet* is a PNG image of code that includes the functionality of a
 VI file.

You can drag a snippet directly onto the diagram and G Web Development Software populates the
 code depicted in the snippet. You can embed snippets in documents, forum
 posts, and emails to quickly share and collaborate on code. Snippets are
 also useful for keeping sections of code that you use frequently handy.

Parent topic:

Collaborating on Web Applications

<!--NI_TOPIC bundle=g-web-development path=coefficient-icon-editor.html language=enus -->
## TOPIC 00064: Coefficient

- bundle_id: `g-web-development`
- source_path: `coefficient-icon-editor.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/coefficient-icon-editor.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Add a coefficient symbol to the icon.

### Coefficient

Add a coefficient symbol to the icon.

Parent topic:

Objects Palette

<!--NI_TOPIC bundle=g-web-development path=coerce-interval.html language=enus -->
## TOPIC 00065: Coerce to Interval.

- bundle_id: `g-web-development`
- source_path: `coerce-interval.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/coerce-interval.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configure a control to snap to the defined interval.

### Coerce to Interval.

Configure a control to snap to the defined interval.

Parent topic:

Creating User Interfaces

<!--NI_TOPIC bundle=g-web-development path=collab-on-apps.html language=enus -->
## TOPIC 00066: Collaborating on Web Applications

- bundle_id: `g-web-development`
- source_path: `collab-on-apps.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/collab-on-apps.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `task`
- source_description: Learn about tools that help your team streamline interactions with project files during software development. Consider using one of the following tools when working on a project with a team of developers. These tools are designed to support developer efficiency and preserve the integrity of your cod

### Collaborating on Web Applications

Learn about tools that help your team streamline interactions with project files during
 software development.

Consider using one of the following tools when working on a project with a team
 of developers.

These tools are designed to support developer efficiency and preserve the
 integrity of your code base.

- Package Dependencies Document—Store a list of packages a project uses so you can
 set up a development system.
- Source Code Control—Back up and manage versions of your source files.

Parent topic:

G Web Development Software

Related tasks:

- Sharing a Project and Including Package Dependencies

Related reference:

- Recommendations for Developing a Project Stored in a Source Code Control Repository

<!--NI_TOPIC bundle=g-web-development path=color-scale.html language=enus -->
## TOPIC 00067: Color Scale

- bundle_id: `g-web-development`
- source_path: `color-scale.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/color-scale.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configure the colors that represent the third dimension of an intensity graph.

### Color Scale

Configure the colors that represent the third dimension of an intensity graph.

Parent topic:

Creating User Interfaces

<!--NI_TOPIC bundle=g-web-development path=color-selector.html language=enus -->
## TOPIC 00068: Color Selector

- bundle_id: `g-web-development`
- source_path: `color-selector.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/color-selector.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Display a color selector whose color corresponds to RGBA color values or a hexadecimal value.

### Color Selector

Display a color selector whose color corresponds to RGBA color values or a hexadecimal value.

Parent topic:

Creating User Interfaces

<!--NI_TOPIC bundle=g-web-development path=combo-box.html language=enus -->
## TOPIC 00069: Combo Box

- bundle_id: `g-web-development`
- source_path: `combo-box.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/combo-box.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Create a drop-down listbox that a user can cycle through to make selections. Users can also type values into the list at edit time or run time.

### Combo Box

Create a drop-down listbox that a user can cycle through to make selections. Users can also type values into the list at edit time or run time.

Parent topic:

Creating User Interfaces

<!--NI_TOPIC bundle=g-web-development path=common-state-machine-transitions.html language=enus -->
## TOPIC 00070: Common State Machine Transition Code

- bundle_id: `g-web-development`
- source_path: `common-state-machine-transitions.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/common-state-machine-transitions.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Transition code determines which case to execute in the next While Loop iteration. You can use the transitions detailed below as a starting point for the transition code in your program. 2 One State Transition Value State Transition Example Image Use an Enum constant transition when you always want

### Common State Machine Transition Code

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

<!--NI_TOPIC bundle=g-web-development path=communicate-data-web-application.html language=enus -->
## TOPIC 00071: Communicating Data with a Web Application

- bundle_id: `g-web-development`
- source_path: `communicate-data-web-application.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/communicate-data-web-application.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `concept`
- source_description: Send and receive data from files and web services with your web application. Use WebVIs to include CSS, JavaScript, and other files in your web application. Learn more about sending requests to and receiving responses from a web service, including same-origin and cross-origin requests, and configuri

### Communicating Data with a Web
 Application

Send and receive data from files and web services with your web application.

- Use WebVIs to include CSS, JavaScript, and other files in your web application.
- Learn more about sending requests to and receiving responses from a web service,
 including same-origin and cross-origin requests, and configuring the LabVIEW Web Service
 for access to your web application resources.
- Use WebVIs to communicate with web services, such as SystemLink Tags and Messages, on
 the same network as your web application or cloud web services.

Parent topic:

G Web Development Software

Related concepts:

- Communicating Data with Web Services Using WebVIs

Related tasks:

- Accessing Resource Files from a WebVI
- Retrieving Data From a Web Service

<!--NI_TOPIC bundle=g-web-development path=communicating-data-with-webvi.html language=enus -->
## TOPIC 00072: Communicating Data with Web Services Using WebVIs

- bundle_id: `g-web-development`
- source_path: `communicating-data-with-webvi.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/communicating-data-with-webvi.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can communicate with web services on the same network using WebVIs. Use the following table to choose the best communication option for your needs. 1 Communicating with Web Services on the Same Network Goal Web service to use How to implement Track a piece of data, such as a hardware measurement

### Communicating Data with Web Services Using
 WebVIs

You can communicate with web services on the same network using WebVIs.

Use the following table to choose the best communication option for your needs.

| Goal | Web service to use | How to implement |
| --- | --- | --- |
| Track a piece of data, such as a hardware measurement. | Tags Service | Refer to Transferring Data Using Tags |
| Send commands, status updates, and data between web applications and servers. | Messages Service | Refer to Sending Messages Between Systems |
| Share waveform data stored in a TDMS file. | TDM Reader API Service | Refer to Reading Measurement Data from TDMS Files |
| Host a WebVI to make it accessible from web browsers. | NI Web Server | Refer to Hosting a WebVI with the Web Applications Service |
| Create a custom HTTP REST API to interface with an existing system, such as a database. | LabVIEW Web Service | Refer to Creating and Publishing a LabVIEW Web Service to the NI Web Server (Windows)Note Download the latest LabVIEW Help for the most up-to-date content. |
| Refer to Configuring CORS for a LabVIEW Web Service |  |  |
| Refer to Hosting a Web Application on the NI Application Web Server |  |  |
| Stream data with low latency. | 3rd party WebSocket service | Refer to WebSocket G APIs |

Parent topic:

Communicating Data with a Web Application

Related concepts:

- Considerations When Accessing Data from Web Services
- Configuring CORS for a LabVIEW Web Service

Related tasks:

- Retrieving Data From a Web Service
- Hosting a Web Application on a Server
- Hosting a WebVI with the Web Applications Service
- Hosting a Web Application on the NI Application Web Server

Related information:

- Transferring Data Using Tags
- Sending Messages Between Systems
- Reading Measurement Data from TDMS Files
- Tutorial: Creating and Publishing a LabVIEW Web Service to the NI Web Server
 (Windows)
- Tutorial: Creating and Publishing a LabVIEW Web Service to the Application Web
 Server (Real-Time, Windows)
- WebSocket G APIs

<!--NI_TOPIC bundle=g-web-development path=comparison-modes.html language=enus -->
## TOPIC 00073: Comparison Modes for Array and Cluster Data

- bundle_id: `g-web-development`
- source_path: `comparison-modes.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/comparison-modes.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `concept`
- source_description: When using certain Comparison nodes to compare data contained in arrays or clusters, you can select from two comparison modes. Compare elements when you want to compare the individual corresponding elements of the input arrays or clusters. Compare aggregates when you want to compare the input arrays

### Comparison Modes for Array and Cluster Data

When using certain Comparison nodes to compare data contained in arrays or clusters, you can select from two comparison modes.

Compare elements when you want to compare the individual corresponding elements of the input arrays or clusters.

Compare aggregates when you want to compare the input arrays or clusters in their entirety.

Note

Greater?

Equal?

Less or Equal?

Greater Than 0?

#### Example

The following table describes the behavior of Greater? in each of the two comparison modes.

| Comparison Mode | Input Array 1 (x) | Input Array 2 (y) | Result (x > y?) | Comments |
| --- | --- | --- | --- | --- |
| Elements | [1,2,3,4] | [2,1,4,3] | [False, True, False, True] | Greater? compares the individual corresponding elements and returns an array of Boolean values that represent the result of each comparison. |
| Aggregates | [1,2,3,4] | [2,1,4,3] | False | In Aggregates mode, a Comparison node processes corresponding elements sequentially, checking for inequalities. The node stops as soon as it encounters corresponding elements that are not equal or reaches the end of one of the input arrays or clusters and performs the comparison on those elements. The first elements in the input arrays are not equal, so Greater? stops and returns a single Boolean value representing the result of 1 > 2? |

You can change the comparison mode for a selected Comparison node by selecting 
 Elements or 
 Aggregates on the 
 Item tab in the 
 Compare section.

Parent topic:

Data Type Reference

Related information:

- Comparison Nodes

<!--NI_TOPIC bundle=g-web-development path=component-organization-api.html language=enus -->
## TOPIC 00074: Component Organization for Distributed APIs

- bundle_id: `g-web-development`
- source_path: `component-organization-api.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/component-organization-api.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Refer to the following table for best practices for organizing components. Guideline Required or Recommended? Details Set the Exported or Non-exported designation of the VIs in your API appropriately. Required The Exported designation indicates to users which VIs are guaranteed to have a consistent

### Component Organization for Distributed APIs

Refer to the following table for best practices for organizing components.

| Guideline | Required or Recommended? | Details |
| --- | --- | --- |
| Set the Exported or Non-exported designation of the VIs in your API appropriately. | Required | The Exported designation indicates to users which VIs are guaranteed to have a consistent interface. |
| Mark a VI as Exported only if it is a public member of your API. | Required | Mark a VI as Exported. |
| If a G Type is on the connector pane of an exported VI in your API, also mark that G Type Exported. | Required | N/A |
| Follow the namespacing guideline [Company].[Product].[Component].gcomp for your API component. | Required | For example, NI.G Core.Data Type.gcomp is a component NI owns, part of the G Core product (in other words, the core libraries that compose the G language), and these VIs pertain to parsing Data Types. |

Parent topic:

Best Practices for Designing and Developing an Application Programming Interface (API) in G Web Development Software

Parent topic:

Best Practices for Designing and Developing an Application Programming Interface (API) in G Web Development Software

Related concepts:

- Best Practices for Designing and Developing an Application Programming Interface (API) in G Web Development Software

<!--NI_TOPIC bundle=g-web-development path=componentize-application.html language=enus -->
## TOPIC 00075: Componentizing Applications

- bundle_id: `g-web-development`
- source_path: `componentize-application.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/componentize-application.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `concept`
- source_description: Componentizing an application helps you organize code into logical groups, save time from creating duplicate code, and enhance software stability. Use Application and Library documents to create component-based applications, in which you compose loosely coupled code into modular and cohesive project

### Componentizing Applications

Componentizing an application helps you organize code into logical groups, save time from
 creating duplicate code, and enhance software stability. Use Application and
 Library documents to create component-based applications, in which you compose loosely
 coupled code into modular and cohesive projects.

The following figure demonstrates how to convert a project with loosely coupled code into a component-based project.

[IMAGE alt='image' src='GUID-073E4D0F-B796-4939-848D-E1BFF3CF58E5-a5.svg']

When you build the application, each top-level VI is built into a separate HTML page with
 required support files.

#### Best Practices for Componentizing
 Applications

Consider the following guidelines when componentizing an
 application:

- Keep application components small and
 self-contained.
- Store code that you might reuse in a separate
 Library document.
- Create namespaces to organize files into
 logical groups.
- Avoid creating circular dependencies between
 libraries, which cause problems such as build failures.
- Analyze your application composition frequently for
 opportunities to refactor code. Refer to Code Dependency Guidelines when
 refactoring code.

#### Code Dependency Guidelines

A VI in an
 Application or Library document can call only VIs within the same component or in a
 dependency library.

[IMAGE alt='image' src='GUID-F0955503-5949-42F0-8132-B5EDBE39185B-a5.svg']

Parent topic:

Applications

Related tasks:

- Organizing Code to Avoid Name Collisions

<!--NI_TOPIC bundle=g-web-development path=computational-units.html language=enus -->
## TOPIC 00076: Nodes: Computational Units

- bundle_id: `g-web-development`
- source_path: `computational-units.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/computational-units.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `concept`
- source_description: Nodes are objects on the diagram that accept inputs, return outputs, and perform operations when a program runs. They are analogous to statements, operators, functions, and subroutines in text-based programming languages.

### Nodes: Computational Units

Nodes are objects on the diagram that accept inputs, return outputs, and perform operations when a program runs.

They are analogous to statements, operators, functions, and subroutines in text-based programming languages.

[IMAGE alt='image' src='GUID-DD0CDE2C-C5AA-409D-A4A7-82C707F350BC-a5.png']

Parent topic:

Programming in G

<!--NI_TOPIC bundle=g-web-development path=config-lv-web-service-cors-cred-access.html language=enus -->
## TOPIC 00077: Configure a LabVIEW Web Service CORS for Credentialed Access

- bundle_id: `g-web-development`
- source_path: `config-lv-web-service-cors-cred-access.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/config-lv-web-service-cors-cred-access.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `task`
- source_description: Configure CORS to allow specific origins you define, well-known origins, and origins with credentials access to your WebVI resources. The following content only applies to LabVIEW Web Services deployed to the LabVIEW Application Web Server. NI recommends deploying LabVIEW Web Services to the NI Web

### Configure a LabVIEW Web Service CORS for
 Credentialed Access

Configure CORS to allow specific origins you define, well-known origins, and origins
 with credentials access to your WebVI resources.

Note

#### What to Use

- LabVIEW Web Service Request
- Read Request Variable
- Set HTTP Header

#### What to Do

Create the following
 diagram in a Web Resources VI to configure a LabVIEW Web Service to allow CORS with specific
 or well-known origins and origins with credentials.

Customize the gray sections for
 your unique programming goals.

[IMAGE alt='image' src='GUID-20DC0C54-1DB0-4E83-A86F-4B8A0CEF8FD5-a5.png']

|  | A new Web Resources VI automatically adds the LabVIEW Web Service Request class to the block diagram and terminal pane. |
| --- | --- |
|  | Read Request Variable checks the request for the variable you define. To check the origin of the request, enter Origin for the value of variable. Use a Case Structure to create two cases: a case to continue if an origin is found in the request and a case to do nothing if an origin is not found in the request. Note Web browsers in a same-origin configuration and HTTP clients outside of web browsers may not have an Origin header in the request. These should be handled by the web resource. |
|  | Define how to filter the origins you want to access your web resources. Some common implementations include the following:Have a strict list of origins to check againstCheck for a prefix on the origin, such as http://localhostUse the LabVIEW Web Service Request and Read Request Variable to check for additional information, such as Remote Address Use a Case Structure to create two cases: a case continue if the origin passes the filter you implement and a case to do nothing if the origin does not pass the filter. |
|  | Set HTTP Header sets the HTTP header value in response to a request. Use the headerAccess-Control-Allow-Origin to indicate if the origin making the request can access the response of your Web Service VI. The header value populates with the origin the filter approves.Note The wildcard (*) value is not valid for credentialed cross-origin requests. You must choose a filtered origin. |
|  | Set HTTP Header sets the HTTP header value in response to a request. Use the headerAccess-Control-Allow-Credentials to indicate if the origin making the request can access the response of your Web Service VI and accept credentialed information, such as cookies. Use the header valuetrue to allow the filtered origin to access your Web Service VI. You must make a corresponding change in the Configure CORS node in your WebVI. See Sending a Credentialed Cross-Origin HTTP Request for more information. |
|  | Add code that only functions if the origin has supported credentials defined in the request. The code above uses session VIs that require browser cookies to function. |

#### Troubleshooting

- Check the implementation of your filter for errors.
- Verify the header is correct for each Set HTTP Header.
- Check the implementation of the Configure CORS node in your WebVI.

Parent topic:

Configuring CORS for a LabVIEW Web Service

Related tasks:

- Sending a Credentialed Cross-Origin HTTP Request

Related information:

- NI Web Server Manual

<!--NI_TOPIC bundle=g-web-development path=config-lv-web-service-cors-filter-access.html language=enus -->
## TOPIC 00078: Configure a LabVIEW Web Service CORS for Filtered Access

- bundle_id: `g-web-development`
- source_path: `config-lv-web-service-cors-filter-access.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/config-lv-web-service-cors-filter-access.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `task`
- source_description: Configure CORS to allow specific origins you define or well-known origins access to your WebVI resources. The following content only applies to LabVIEW Web Services deployed to the LabVIEW Application Web Server. NI recommends deploying LabVIEW Web Services to the NI Web Server instead. What to Use

### Configure a LabVIEW Web Service CORS for
 Filtered Access

Configure CORS to allow specific origins you define or well-known origins access to
 your WebVI resources.

Note

#### What to Use

- LabVIEW Web Service Request
- Read Request Variable
- Set HTTP Header

#### What to Do

Create the following
 diagram in a Web Resources VI to configure a LabVIEW Web Service to allow CORS with specific
 or well-known origins.

Customize the gray sections for your unique programming
 goals.

[IMAGE alt='image' src='GUID-41210DB6-7EA7-4575-BE1C-6535673CC61C-a5.png']

|  | A new Web Resources VI automatically adds the LabVIEW Web Service Request class to the block diagram and terminal pane. |
| --- | --- |
|  | Read Request Variable checks the request for the variable you define. To check the origin of the request, enter Origin for the value of variable. Use a Case Structure to create two cases: a case to continue if an origin is found in the request and a case to do nothing if an origin is not found in the request. Note Web browsers in a same-origin configuration and HTTP clients outside of web browsers may not have an Origin header in the request. These should be handled by the web resource. |
|  | Define how to filter the origins you want to access your web resources. Some common implementations include the following:Have a strict list of origins to check againstCheck for a prefix on the origin, such as http://localhostUse the LabVIEW Web Service Request and Read Request Variable to check for additional information, such as Remote Address Use a Case Structure to create two cases: a case to continue if the origin passes the filter you implement and a case to do nothing if the origin does not pass the filter. |
|  | Set HTTP Header sets the HTTP header value in response to a request. Use the headerAccess-Control-Allow-Origin to indicate if the origin making the request can access the response of your Web Service VI. The header value populates with the origin the filter approves. |

#### Troubleshooting

- Check the implementation of your filter for errors.
- Verify the header is correct.

Parent topic:

Configuring CORS for a LabVIEW Web Service

Related information:

- NI Web Server Manual

<!--NI_TOPIC bundle=g-web-development path=config-lv-web-service-cors-open-access.html language=enus -->
## TOPIC 00079: Configure a LabVIEW Web Service CORS for Open Access

- bundle_id: `g-web-development`
- source_path: `config-lv-web-service-cors-open-access.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/config-lv-web-service-cors-open-access.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `task`
- source_description: Configure CORS to allow any origin access to your WebVI resources. This CORS configuration is the least secure configuration. Any origin can access your web service and application resources. For example, any web page the browser visits could run scripts that make requests to the web service. The fo

### Configure a LabVIEW Web Service CORS for Open
 Access

Configure CORS to allow any origin access to your WebVI resources.

This CORS configuration is the least secure configuration. Any origin can access your web
 service and application resources. For example, any web page the browser visits could run
 scripts that make requests to the web service.

Note

#### What to Use

- LabVIEW Web Service Request
- Set HTTP Header

#### What to Do

Create the following
 diagram in a Web Resources VI to configure a LabVIEW Web Service to allow CORS from any
 origin.

[IMAGE alt='image' src='GUID-F377F974-8848-4D47-B04F-F7E80EF3C3E4-a5.png']

|  | A new Web Resources VI automatically adds the LabVIEW Web Service Request class to the block diagram and terminal pane. |
| --- | --- |
|  | Set HTTP Header sets the HTTP header value in response to a request. Use the headerAccess-Control-Allow-Origin to indicate if the origin making the request can access the response of your Web Service VI. Use wildcard (*) as the header value to allow any origin to access your WebVI resource. |

#### Troubleshooting

- Verify the header and header value 
 are correct.

Parent topic:

Configuring CORS for a LabVIEW Web Service

Related information:

- NI Web Server Manual

<!--NI_TOPIC bundle=g-web-development path=configure-cors-for-labview-web-service.html language=enus -->
## TOPIC 00080: Configuring CORS for a LabVIEW Web Service

- bundle_id: `g-web-development`
- source_path: `configure-cors-for-labview-web-service.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/configure-cors-for-labview-web-service.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `concept`
- source_description: You may need different CORS configurations for each LabVIEW Web Service in your application during development and deployment. The following content only applies to LabVIEW Web Services deployed to the LabVIEW Application Web Server. NI recommends deploying LabVIEW Web Services to the NI Web Server

### Configuring CORS for a LabVIEW Web
 Service

You may need different CORS configurations for each LabVIEW Web Service in your
 application during development and deployment.

Note

To determine the origin of a web application executing in the development environment, refer
 to *Hosting a Web Application During Development*. During development using a
 LabVIEW Web Service, configure CORS to test your application in the LabVIEW editor.

Note

| Goal | CORS Configuration | Configuration Instructions |
| --- | --- | --- |
| Share your web application resources publicly and receive requests from any origin.Note This configuration is the least secure. Any origin could access your web service. | No credentials Unfiltered Origins | Refer to Configure a LabVIEW Web Service CORS for Open Access. |
| Allow specific origins you define or well-known origins to access your web application resources that do not require credentials. | No credentials Filtered Origins | Refer to Configure a LabVIEW Web Service CORS for Filtered Access. |
| Allow specific origins you define or well-known origins to access your web application resources and you want to enable sharing credentials, such as cookies. | Credentials Filtered Origins | Refer to Configure a LabVIEW Web Service CORS for Credentialed Access. |

Parent topic:

Considerations When Accessing Data from Web Services

Related concepts:

- Hosting a Web Application During Development

Related tasks:

- Configure a LabVIEW Web Service CORS for Open Access
- Configure a LabVIEW Web Service CORS for Filtered Access
- Configure a LabVIEW Web Service CORS for Credentialed Access

Related information:

- NI Web Server Manual

<!--NI_TOPIC bundle=g-web-development path=configure-icon-editor.html language=enus -->
## TOPIC 00081: Configure

- bundle_id: `g-web-development`
- source_path: `configure-icon-editor.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/configure-icon-editor.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Add a configure symbol to the icon.

### Configure

Add a configure symbol to the icon.

Parent topic:

Actions Palette

<!--NI_TOPIC bundle=g-web-development path=configuring-flex-ui.html language=enus -->
## TOPIC 00082: Aligning and Arranging Objects in a Responsive User Interface

- bundle_id: `g-web-development`
- source_path: `configuring-flex-ui.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/configuring-flex-ui.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `task`
- source_description: A container groups together controls and indicators and determines their arrangement on the panel. If the screen size on which you view your application changes, the objects in a container rearrange according to the layout settings of the container. Containers exist only on panels whose layout type

### Aligning and Arranging Objects in a Responsive User Interface

A 
 *container* groups together controls and indicators and determines their arrangement on the panel. If the screen size on which you view your application changes, the objects in a container rearrange according to the layout settings of the container.
 Containers exist only on panels whose layout type is flexible.

Flexible

Layout

Item

1. Set the 
 Direction to one of the following options: 
 OptionDescriptionRow
 Arranges objects in a single row as the screen width allows. As the screen width decreases, objects rearrange into multiple rows.Column
 Arranges objects in a single column.
2. Set the Horizontal alignment to one of the following
 options: 
 OptionDescriptionLeft
 Aligns objects to the left of the container.Center
 Aligns objects to the center of the container.Right
 Aligns objects to the right of the container.Space between
 Arranges objects with space between the left and right of objects.Space around
 Arranges objects with space before, between, and after
 objects.
3. Set the Vertical alignment to one of the following
 options: 
 OptionDescriptionTop
 Aligns objects to the top of the container.Center
 Aligns objects to the center of the container.Bottom
 Aligns objects to the bottom of the container.Space between
 Arranges objects with space between the top and bottom of objects.Space around
 Arranges objects with space above, between, and, below
 objects.

Layout

Item

1. Set the Width and Height of the
 object.
2. Set 
 Flexible resize to one of the following options: 
 OptionDescriptionDo not resize
 Does not resize the object.Resize height and width
 Resizes the height and width of the object while maintaining aspect ratio.Resize width
 Resizes only the width of the object. 
 Note The flexible resize options are not
 available for all objects, as some objects have fixed width and/or height.
 For example, text objects do not support flexible resize options. You must
 enable the Auto size property for text objects to
 resize to the container or disable the Auto size
 property to prevent text objects from resizing.
3. Optional: 
 Set Minimum height and Minimum
 width of the objects. This prevents the objects from becoming
 too small to read or use when the screen size decreases.
4. Click 
 File»Save all to save all files.
5. Select Run»Run in browser to view your application in a web browser. 
 Resize the web browser and ensure the controls and indicators
 resize appropriately.

Parent topic:

Designing a Responsive User Interface

Related tasks:

- Designing a Responsive User Interface

<!--NI_TOPIC bundle=g-web-development path=consideration-create-ui-js.html language=enus -->
## TOPIC 00083: Considerations When Creating UI Elements with JavaScript

- bundle_id: `g-web-development`
- source_path: `consideration-create-ui-js.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/consideration-create-ui-js.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `concept`
- source_description: JavaScript UI elements may require special sizing considerations to ensure they appear correctly after you deploy your web application or share the UI element in a library. The size of the UI element you create can change if your web application has a flexible layout or if your user configures the e

### Considerations When Creating UI Elements with
 JavaScript

JavaScript UI elements may require special sizing considerations to ensure they appear
 correctly after you deploy your web application or share the UI element in a
 library.

- Configure with CSS—Use a style sheet to set the size of the UI
 element.
- Configure with the ResizeObserver API—Use the browser-based ResizeObserver API to make
 adjustments programmatically. Note The
 ResizeObserver API is supported in most browsers. Ensure your browser supports this API
 before implementing it in your code. Refer to the Mozilla Developer Network
 documentation for more information about the ResizeObserver API.

Parent topic:

Creating UI Elements with JavaScript

Related information:

- Mozilla Developer Network

<!--NI_TOPIC bundle=g-web-development path=considerations-package-web-app.html language=enus -->
## TOPIC 00084: Considerations for Packaging a Web Application

- bundle_id: `g-web-development`
- source_path: `considerations-package-web-app.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/considerations-package-web-app.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `concept`
- source_description: Web applications have unique deployment factors and dependencies you need to know before configuring a package or package installer. You can package web applications using the distribution document in software. However, you must deploy web applications to a web server. After you add your web applica

### Considerations for Packaging a Web
 Application

Web applications have unique deployment factors and dependencies you need to know before
 configuring a package or package installer.

Note

NI Web
 Server

File

Preferences

Web Server

<web
 application name>

- Right-click the component in the project tree and choose
 Create Package/Installer with
 item .
- Open a distribution document and choose Add
 Files... .

For web applications that use SystemLink APIs, such as Tags and Messages, add
 those dependencies to the package manually.

Parent topic:

Packaging an Application or Library

Related tasks:

- Packaging an Application
- Packaging a Library

<!--NI_TOPIC bundle=g-web-development path=constants.html language=enus -->
## TOPIC 00085: Constants

- bundle_id: `g-web-development`
- source_path: `constants.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/constants.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `concept`
- source_description: A constant is a fixed piece of data that exists only on the diagram. Use a constant instead of a control when you know that a certain piece of data should always be the same regardless of other parts of your code. You can use the following types of constants in graphical programming: Universal const

### Constants

A constant is a fixed piece of data that exists only on the diagram. Use a constant instead of a control when you know that a certain piece of data should always be the same regardless of other parts of your code.

You can use the following types of constants in graphical programming:

Universal constant

User-defined constant

Parent topic:

Programming in G

<!--NI_TOPIC bundle=g-web-development path=content-font-family.html language=enus -->
## TOPIC 00086: Content Font Family

- bundle_id: `g-web-development`
- source_path: `content-font-family.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/content-font-family.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Select the font face.

### Content Font Family

Select the font face.

Parent topic:

Creating User Interfaces

<!--NI_TOPIC bundle=g-web-development path=content-font-size.html language=enus -->
## TOPIC 00087: Content Font Size

- bundle_id: `g-web-development`
- source_path: `content-font-size.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/content-font-size.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Set the font size.

### Content Font Size

Set the font size.

Parent topic:

Creating User Interfaces

<!--NI_TOPIC bundle=g-web-development path=content.html language=enus -->
## TOPIC 00088: Content

- bundle_id: `g-web-development`
- source_path: `content.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/content.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Toggle the content within the control on or off.

### Content

Toggle the content within the control on or off.

Parent topic:

Creating User Interfaces

<!--NI_TOPIC bundle=g-web-development path=control-reference-lvmember.html language=enus -->
## TOPIC 00089: Control Reference

- bundle_id: `g-web-development`
- source_path: `control-reference-lvmember.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/control-reference-lvmember.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represent a reference to a control, indicator, or panel item whose behavior and properties you can control and pass to other VIs.

### Control Reference

Represent a reference to a control, indicator, or panel item whose behavior and properties you can control and pass to other VIs.

Parent topic:

Creating User Interfaces

<!--NI_TOPIC bundle=g-web-development path=control-reference-type.html language=enus -->
## TOPIC 00090: Control reference type

- bundle_id: `g-web-development`
- source_path: `control-reference-type.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/control-reference-type.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reference is generic and does not include value data type.

### Control reference type

Reference is generic and does not include value data type.

Parent topic:

Creating User Interfaces

<!--NI_TOPIC bundle=g-web-development path=control-zoom-mouse-wheel.html language=enus -->
## TOPIC 00091: Customizing Mouse Wheel Behavior

- bundle_id: `g-web-development`
- source_path: `control-zoom-mouse-wheel.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/control-zoom-mouse-wheel.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `task`
- source_description: You can change the action the mouse wheel performs within the workspace. Click FilePreferences to display the Preferences dialog box. On the Editor tab, select the desired setting for Zoom Control. Setting Description Zoom with Mouse Wheel Scroll with the mouse wheel to zoom in and out within the wo

### Customizing Mouse Wheel Behavior

You can change the action the mouse wheel performs within the workspace.

1. Click 
 File»Preferences to display the 
 Preferences dialog box.
2. On the 
 Editor tab, select the desired setting for Zoom Control. 
 SettingDescriptionZoom with Mouse Wheel
 Scroll with the mouse wheel to zoom in and out within the workspace.
 To scroll vertically within the workspace, hold down the <Ctrl> key while scrolling with the mouse wheel.Zoom with Ctrl + Mouse Wheel (Default)
 Hold down the <Ctrl> key while scrolling with the mouse wheel to zoom in and out within the workspace.
 To scroll vertically within the workspace, scroll with the mouse wheel.
3. Click 
 OK.

Parent topic:

Customizing G Web Development Software

<!--NI_TOPIC bundle=g-web-development path=control.html language=enus -->
## TOPIC 00092: Control button

- bundle_id: `g-web-development`
- source_path: `control.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/control.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Change the selected indicator to a control.

### Control button

Change the selected indicator to a control.

Parent topic:

Creating User Interfaces

<!--NI_TOPIC bundle=g-web-development path=controlling-panel-objects.html language=enus -->
## TOPIC 00093: Controlling Panel Objects Programmatically

- bundle_id: `g-web-development`
- source_path: `controlling-panel-objects.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/controlling-panel-objects.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `concept`
- source_description: Control a panel object, such as a control, indicator, or the panel itself, by creating a control reference to the object. Control references are either strictly typed or general. Use control references with the Panel Manipulation nodes to control panel objects programmatically. The Chart class does

### Controlling Panel Objects
 Programmatically

Control a panel object, such as a control, indicator, or the panel itself, by creating a
 control reference to the object. Control references are either strictly typed or
 general. Use control references with the Panel Manipulation
 nodes to control panel objects programmatically.

Note

Chart

Value

Parent topic:

Creating User Interfaces

#### Strictly Typed Control References

*Strictly typed control references* include data type information and accept
 only references of the same data type. For example, if a subVI accepts a strictly
 typed control reference that contains a 32-bit integer data type, you can wire only
 a reference that also contains a 32-bit integer data type to the subVI.

Complete the following steps to create a strictly
 typed control reference:

1. Place a control or indicator on the panel.
2. Right-click a panel object and select Create
 reference.
3. On the diagram, place the Static Control
 Reference of the panel object from the
 Unplaced Items tray and
 right-click the reference to create a control, indicator, or
 constant.

#### General Control References

*General control references* are flexible in the type of data they accept. For
 example, if a subVI accepts a general slide reference, you can wire a reference to a
 32-bit integer slide, single-precision slide, or a cluster of 32-bit integer slides
 to the slide reference terminal of the subVI.

Behavior

Item

```text
Reference does not include value data type
```

Note

Value

1. Place a Control Reference on the panel.
2. On the diagram, place the Control
 Reference from the Unplaced
 Items tray and click the
 Select reference type button
 next to the Reference type option on
 the Item tab to select a type.

<!--NI_TOPIC bundle=g-web-development path=conversion-behavior.html language=enus -->
## TOPIC 00094: Conversion Behaviors

- bundle_id: `g-web-development`
- source_path: `conversion-behavior.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/conversion-behavior.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `concept`
- source_description: By default, a data type with fewer bits changes to match the data type with more bits. If the number of bits is the same, unsigned data types are chosen over signed data types to retain as much precision as possible. Conversion behaviors depend on the data types you are converting between or the nod

### Conversion Behaviors

By default, a data type with fewer bits changes to match the data
 type with more bits. If the number of bits is the same, unsigned data types are chosen
 over signed data types to retain as much precision as possible.

Conversion behaviors depend on the data types you are converting between or the node accepting the data. For example, if you wire two different data types to a node that expects matching data types, one of the inputs is converted to match the other.

| Original Type | Converted Type | Conversion Behavior | Behavior Details |
| --- | --- | --- | --- |
| Signed or unsigned integer | Floating-point number | Data is coerced to the nearest value possible. | This conversion is exact when the floating-point number is more precise than the integer. If the integer is more precise than the floating-point number, the floating-point data type maintains as much precision as possible in the conversion. |
| Floating-point number | Signed or unsigned integer | In-range values are coerced to a signed or unsigned integer. Out-of-range values are coerced to the minimum or maximum value of the integer. | This conversion is less precise if the floating-point number is an out-of-range value. For example, unsigned integers represent only non-negative integers. If you convert a negative floating-point number to an unsigned integer, the result is 0. |
| Integer | Integer | If the source is smaller than the destination, the sign of a signed source is extended and zeros are placed in the extra bits of an unsigned source. If the source is larger than the destination, the destination retains only the least significant bits of the source value. | Out-of-range values are not coerced to the minimum or maximum value of an integer. The software attempts to retain as much precision as possible when converting between integer types. |

Note

Parent topic:

Numeric Data

<!--NI_TOPIC bundle=g-web-development path=convert-nxg-to-g-web.html language=enus -->
## TOPIC 00095: Converting LabVIEW NXG Web Module Projects to G Web Development Software Projects

- bundle_id: `g-web-development`
- source_path: `convert-nxg-to-g-web.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/convert-nxg-to-g-web.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `task`
- source_description: Convert your LabVIEW NXG Web Module project (.lvproject) to a G Web Development Software project (.gwebproject). Before you begin, ensure that all files are unlocked and sourced within the project you want to convert. If your files are locked or cannot be found, your project will not convert. Launch

### Converting LabVIEW NXG Web Module Projects to
 G Web Development Software Projects

Convert your LabVIEW NXG Web Module project (.lvproject) to a G Web
 Development Software project (.gwebproject).

Before you begin, ensure that all
 files are unlocked and sourced within the project you want to convert. If your files are
 locked or cannot be found, your project will not convert.

1. Launch G Web Development Software.
2. Click File»Open Project»Browse.
3. In the Open Project dialog box, filter the available files
 by selecting LabVIEW NXG Project in the file type
 pull-down.
4. Select the project you want to convert and click
 Open.
5. Click Continue when prompted. 
 Note G Web Development Software
 removes unsupported files to successfully complete conversion. The
 conversion report lists any changes made to your code.
6. Click Close and your converted project automatically
 opens.

Parent topic:

G Web Development Software

Parent topic:

G Web Development Software Manual

<!--NI_TOPIC bundle=g-web-development path=cors-considerations.html language=enus -->
## TOPIC 00096: Considerations When Accessing Data from Web Services

- bundle_id: `g-web-development`
- source_path: `cors-considerations.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/cors-considerations.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `concept`
- source_description: If you want to create a web application that sends requests to and receives responses from a web service, you need to know the origin of the web service that hosts the web application as well as the origin of the target web service. For example, a web application hosted at http://localhost:8080/Demo

### Considerations When Accessing Data from Web Services

If you want to create a web application that sends requests to and receives responses
 from a web service, you need to know the origin of the web service that hosts the web
 application as well as the origin of the target web service.

For example, a web application hosted at http://localhost:8080/Demo/MyExample.html has the origin http://localhost:8080. A server origin contains three parts:

| Part | Definition | Example |
| --- | --- | --- |
| Scheme | Protocol the web service uses. | http:// |
| Host | Domain name or IP address of the service. | localhost |
| Port | TCP port of the web service. If you don't specify a port, the web service uses the default port. | 8080 |

Once you know the origin of the host web service and the target web service, determine whether requests from the web application to the target web service will be same-origin requests or cross-origin requests. If both origins are identical, requests from the web application to the web service are same-origin requests. If there is any difference between the two origins, requests from the web application to the web service are cross-origin requests.

Browsers running web applications do not impose restrictions on same-origin requests. Web applications that perform cross-origin requests are subject to the 
 *Cross-Origin Resource Sharing* (CORS) mechanism. By default, a web browser blocks all cross-origin requests made to a target web service that is not configured to support CORS.

Parent topic:

Communicating Data with a Web Application

Related concepts:

- Types of Cross-Origin HTTP Requests
- Configuring CORS for a LabVIEW Web Service
- Hosting a Web Application During Development

Related tasks:

- Enabling CORS for a Web Service
- Sending a Credentialed Cross-Origin HTTP Request

<!--NI_TOPIC bundle=g-web-development path=create-async-js-calls.html language=enus -->
## TOPIC 00097: Waiting for Asynchronous JavaScript Operations to Complete in a Web Application

- bundle_id: `g-web-development`
- source_path: `create-async-js-calls.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/create-async-js-calls.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `task`
- source_description: Use asynchronous JavaScript code to wait on tasks or requests while the rest of the code in your WebVI continues to execute. Synchronous code means that your code executes in order. Asynchronous code means that a portion of your code waits for a task to complete while the rest of your code continues

### Waiting for Asynchronous JavaScript Operations to Complete in a Web Application

Use asynchronous JavaScript code to wait on tasks or requests while the rest of the code in your WebVI continues to execute.

Synchronous code means that your code executes in order. Asynchronous code means that a
 portion of your code waits for a task to complete while the rest of your code continues to
 execute.

#### What to Use

- External JavaScript file
- JavaScript Library Interface (JSLI) document

#### What to Do

1. Create the following code in a JavaScript (.js) file to use an asynchronous JavaScript
 function in your web application to run two loops in parallel. Customize the
 following code for your unique programming goals. 
 (function () {
 'use strict';

 /*1*/
 const synchronousDivide = function (numerator, denominator) {
 if (denominator === 0) {
 throw new Error('Cannot divide by zero');
 } else {
 return numerator / denominator;
 }
 };

 const sleep = function (time) {
 return new Promise(function (resolve) {
 setTimeout(resolve, time);
 });
 };

 /*2*/
 const asynchronousDivide = async function (numerator, denominator) {
 await sleep(1000); /*3*/

 /*4*/
 if (denominator === 0) {
 throw new Error('Cannot divide by zero');
 } else {
 return numerator / denominator;
 }
 };

 /*5*/
 window.synchronousDivide = synchronousDivide;
 window.asynchronousDivide = asynchronousDivide;
}()); 
 [IMAGE alt='image' src='GUID-97140CE0-AE0F-45D2-BC12-D22F4BA789B6-a5.svg']
 Create a JavaScript function that completes synchronously named
 synchronousDivide. Note To
 notify G Web Development Software that a
 JavaScript error has occurred in a synchronous
 function, you must throw an error in your
 JavaScript code. In your diagram code, the
 error out output on the
 JSLI node returns an error.
 [IMAGE alt='image' src='GUID-245F4F1B-3FBD-425A-A6D9-4F445ABFE629-a5.svg']
 Create an async JavaScript function named 
 asynchronousDivide.
 An async JavaScript function results in a JavaScript Promise that notifies G Web
 Development Software that the function will run
 asynchronously.
 [IMAGE alt='image' src='GUID-EE38CAD4-C25C-4C69-A3B4-5FD829627100-a5.svg']
 Add code that runs asynchronously. This example uses the sleep function which asynchronously pauses execution for 1000 milliseconds.
 [IMAGE alt='image' src='GUID-1C2B5505-1271-4422-8DB9-8B9B5154C5C4-a5.svg']
 Return a value or throw an error from the async function. When using an async JavaScript
 function for asynchronous programming, returning a
 value or throwing an error uses syntax similar to
 synchronous programming.
 [IMAGE alt='image' src='GUID-1CED6939-5ED1-4388-BEB8-FFF164BED4D0-a5.svg']
 Add the functions you want to call in your web application to the global scope to make the functions accessible to the JSLI document. In this example, we place both the 
 synchronousDivide and 
 asynchronousDivide functions on the global scope.
2. Create and configure a JSLI document.
3. Integrate the JavaScript file into your web
 application.
4. Create the following diagram to use the asynchronous JavaScript function to execute two loops in parallel in your WebVI. 
 
 [IMAGE alt='image' src='GUID-97140CE0-AE0F-45D2-BC12-D22F4BA789B6-a5.svg']
 Run the WebVI. The Sync Divide JSLI node executes continuously without waiting.
 [IMAGE alt='image' src='GUID-245F4F1B-3FBD-425A-A6D9-4F445ABFE629-a5.svg']
 The Async Divide JSLI node waits 1000 milliseconds before continuing execution. Because the 
 asynchronousDivide function executes asynchronously in your JavaScript code, the second loop doesn't block execution of the first loop. The Async Divide JSLI node behaves synchronously in your diagram code, so you do not need to wait on the asynchronously executing JavaScript code manually in your diagram code.

Parent topic:

Calling JavaScript Functions in a Web Application

Related tasks:

- Defining Calls to JavaScript Functions using a JavaScript Library Interface
- Integrating a JavaScript File Into a Web Application
- Debugging JavaScript Library Interfaces

Related reference:

- JavaScript Resources

<!--NI_TOPIC bundle=g-web-development path=create-icon-editor.html language=enus -->
## TOPIC 00098: Create

- bundle_id: `g-web-development`
- source_path: `create-icon-editor.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/create-icon-editor.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Add a create symbol to the icon.

### Create

Add a create symbol to the icon.

Parent topic:

Actions Palette

<!--NI_TOPIC bundle=g-web-development path=create-ui-elements-with-javascript.html language=enus -->
## TOPIC 00099: Creating UI Elements with JavaScript

- bundle_id: `g-web-development`
- source_path: `create-ui-elements-with-javascript.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/create-ui-elements-with-javascript.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `concept`
- source_description: Create UI elements to place on the panel of your web application using the Placeholder HTML Container and JavaScript Library Interface document (JSLI). You can add custom UI elements, such as controls, to your web application by creating a placeholder on the panel. Using the placeholder, you can set

### Creating UI Elements with JavaScript

Create UI elements to place on the panel of your web application using the Placeholder
 HTML Container and JavaScript Library Interface document (JSLI).

You can add custom UI elements, such as controls, to your web application by creating a
 placeholder on the panel. Using the placeholder, you can set the dimensions and other
 properties of the element that work for both flexible and absolute layouts. You then
 create a control reference and wire the reference into a JSLI, directly exposing the
 underlying HTML for the control to your JavaScript code.

Before you begin, create or open a web application.

#### What to Use

- Placeholder HTML Container
- Obtain JavaScript Reference

#### What
 to Do

1. Open or create a JSLI and add the JavaScript function you want to call from your
 web application. Add the parameters with one input having a data type of
 JS Reference . Note In order to directly access
 your HTML element, your function must have an input with a matching data
 type of JS Reference. You can also include an array of JS
 references. In the following example, the JavaScript function is
 Reflect.set, a function available in most
 browsers, with the name Property Set. In addition to
 the JavaScript Reference input, there are two additional inputs for the
 function. 
[IMAGE alt='image' src='GUID-649C6046-BEFE-412C-AE38-CAB25322D45C-a5.png'] 
Note You can rename the
 function and properties, however the JavaScript Global function name
 must be the name of the function you are referencing.
2. Open or create a WebVI ( .gviweb ) and on the panel, select Decorations»Placeholder HTML Container and place it on the panel.
3. Use the Configuration pane on the right to configure the
 container. Note Use
 the Configuration pane or property nodes to configure the HTML container
 instead of injecting HTML to configure the placement and
 sizing.The container is empty by default and you can populate it with
 a control at runtime. If you use the Configuration pane to add a placeholder
 image, the placeholder image is visible in the container at edit time.
 Select Image visible at runtime to make the
 placeholder image also visible at runtime until the contents of the
 container are available.
4. With the HTML Container selected, click Create
 reference in the Configuration pane. The HTML
 Container does not have a terminal, so you must create a
 reference to interact with it on the diagram.
5. Create the following diagram to populate the HTML container on the panel with
 the JavaScript function you defined in the JSLI. Customize the gray sections
 for your unique programming goals. [IMAGE alt='image' src='GUID-E307443C-552D-4016-8D22-6B6DF81A0E22-a5.png'] [IMAGE alt='image' src='GUID-97140CE0-AE0F-45D2-BC12-D22F4BA789B6-a5.svg']The Static Control Reference
 represents the HTML Container you
 placed on the panel.Tip You
 can wire the HTML container to a property node to
 configure the size and position of your
 control.Obtain JavaScript Reference creates
 a JavaScript reference with a value of the HTML element
 within the container.Note The
 references do not have controls and are only visible
 on the diagram. You can wire references to terminals
 on a connector pane.[IMAGE alt='image' src='GUID-245F4F1B-3FBD-425A-A6D9-4F445ABFE629-a5.svg']If you want your web application to run continuously in a
 web browser until it encounters an error, place your
 code in a While Loop with the
 conditional terminal wired to the error
 out parameter of your JavaScript
 function.In this example, the Property Set JavaScript function is
 wired to the conditional terminal. If Property Set
 returns an error, the conditional terminal will stop the
 loop from executing.[IMAGE alt='image' src='GUID-EE38CAD4-C25C-4C69-A3B4-5FD829627100-a5.svg']The JavaScript function uses the JavaScript reference
 from Obtain JavaScript reference. You can configure the
 function using the properties you defined in the JSLI
 document along with any other supporting code.In this example, the Property Set
 function outputs the number of loop iterations by
 converting the iteration counter output into a string
 using the HTML <b> tag.[IMAGE alt='image' src='GUID-1C2B5505-1271-4422-8DB9-8B9B5154C5C4-a5.svg']To reduce loading time and improve performance when you
 run your built web application on a web browser, add a
 Wait node to any WebVI that uses an
 infinite While Loop.

#### Troubleshooting

Ensure you properly define the JavaScript calls you make in the JSLI.

Parent topic:

Using JavaScript with a Web Application

Related concepts:

- Considerations When Creating UI Elements with JavaScript
- JavaScript Reference Functionality

Related tasks:

- Defining Calls to JavaScript Functions using a JavaScript Library Interface

Related reference:

- JavaScript Resources

Related information:

- Decorations Palette
- Obtain JavaScript Reference

<!--NI_TOPIC bundle=g-web-development path=create-vi.html language=enus -->
## TOPIC 00100: Creating a WebVI

- bundle_id: `g-web-development`
- source_path: `create-vi.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/create-vi.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `task`
- source_description: Create a webVI (.gviweb) in which you can write a program. In the Navigation pane, right click on a component document and select New WebVI . Top-level VIs must be WebVIs. Complete any of the following tasks to accomplish your programming goals: On the diagram, write code that performs your desired

### Creating a WebVI

Create a webVI (.gviweb) in which you can write a program.

1. In the Navigation pane, right click on a component document and select New»WebVI. 
 Note Top-level VIs must be WebVIs.
2. Complete any of the following tasks to accomplish your programming goals:
  - On the diagram, write code that performs your desired task when the program
 executes.
  - On the panel, build a user interface.
  - On the icon editor, add inputs and outputs to configure a WebVI or a VI as a
 SubVI. After you save the SubVI, you can add it to the diagram of other VIs.

After you create a WebVI, run the WebVI in the development
 environment or build the WebVI into a web page to execute the code.

Parent topic:

Applications

Related tasks:

- Creating User Interfaces
- Creating a SubVI from a Section of Existing Code
- Building a Web Application as a Web Page

<!--NI_TOPIC bundle=g-web-development path=creating-a-code-snippet.html language=enus -->
## TOPIC 00101: Creating a Code Snippet

- bundle_id: `g-web-development`
- source_path: `creating-a-code-snippet.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/creating-a-code-snippet.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `task`
- source_description: Use code snippets to store and share G Web Development Software code as PNG files that become graphical code when you drag them onto the diagram. Open a project. On the diagram, highlight the code you want to capture as a snippet. Click EditCreate snippet from selection. Choose where to save the sni

### Creating a Code Snippet

Use code snippets to store and share G Web Development Software code as PNG files that
 become graphical code when you drag them onto the diagram.

1. Open a project.
2. On the diagram, highlight the code you want to capture as a snippet.
3. Click Edit»Create snippet from selection.
4. Choose where to save the snippet, give it a descriptive name, and click
 Save. 
 Note If you edit a snippet in an image editor, the editor will
 remove the VI information from the file and you will not be able to drop the
 snippet onto the diagram.
 Tip Sharing snippets
 is most useful for simple code. If your snippet includes dependencies, such
 as subVIs or classes, anyone who uses your snippet must have those
 dependencies in their project or they will see a missing dependency
 error.

Parent topic:

Code Snippets

<!--NI_TOPIC bundle=g-web-development path=creating-a-web-application.html language=enus -->
## TOPIC 00102: Creating a Web Application

- bundle_id: `g-web-development`
- source_path: `creating-a-web-application.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/creating-a-web-application.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `task`
- source_description: Use the web application project template to create an application that can run in a web browser. In the Projects tab, click Web Application Project, name your project, and click Create. A web application project includes the following parts: Web application document (.gcomp) - The container for all

### Creating a Web Application

Use the web application project template to create an application that can run in a web browser.

1. In the 
 Projects tab, click 
 Web Application Project, name your project, and click 
 Create. 
 A web application project includes the following parts:
 Web application document (.gcomp) - The container for all the files in your
 application.
 
 
 WebVI (.gviweb) - A specialized VI that generates HTML, JavaScript, and CSS files
 after you build a web application. Each WebVI marked as top-level in your application
 generates one HTML file, which corresponds to one web page after you build your web
 application.
 
 
 Other files (Optional) - Any other files you want to include in your web
 application, such as CSS, JavaScript, and image files.
2. Open or create a WebVI within the application document and customize the WebVI for your unique programming goals.
3. Optional: If you want to customize the appearance of your WebVI
 or add interactive functionality, create CSS and JavaScript files and include them in your
 application.
4. Test and debug your code. 
 Select Run»Run in browser to test your WebVI in a browser.
5. Repeat steps 2–4 to create additional WebVIs.

Once you finish creating and testing your application, build it into a web application that can run in a web browser.

Parent topic:

Developing a Web Application

Related concepts:

- Testing and Debugging

Related tasks:

- Building a Web Application as a Web Page
- Debugging a WebVI

Related information:

- NI Package Manager User Manual
- LabVIEW Application Builder Module
- TestStand Licensing Information

<!--NI_TOPIC bundle=g-web-development path=creating-custom-data-type-using-g-type-document.html language=enus -->
## TOPIC 00103: Creating a Custom Data Type Using a G Type Document

- bundle_id: `g-web-development`
- source_path: `creating-custom-data-type-using-g-type-document.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/creating-custom-data-type-using-g-type-document.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `task`
- source_description: Create a type definition, or custom data type, to reuse a control or constant throughout your project. You define the type definition with the control you add to the panel of a G Type document. An example of when a type definition would be useful is keeping state enums of a state machine in sync. Be

### Creating a Custom Data Type Using a G Type Document

Create a type definition, or custom data type, to reuse a control or constant
 throughout your project. You define the type definition with the control you
 add to the panel of a G Type document.

An example of when a type definition would be useful is keeping state enums of a state machine
 in sync. Because instances of a type definition share a source file, you can update
 the source enum, the type definition, with additional states as needed and propagate
 the changes to all instances rather than having to update each copy individually.

1. From the Project Files tab, expand the
 New menu and select Type
 Definition to create a G Type document.
2. In the G Type document, add a single control, array of controls, or cluster of controls that you want to reuse throughout your application. 
 The data type of the control you add to the G Type document panel defines the data type of
 the type definition. Note Adding
 more than one control outside of an array or cluster or more than one array
 or cluster of controls to a G Type document makes the type definition
 unusable.
3. In the Item tab, configure the control with the settings
 you want to persist to each instance of the type definition.
4. Save the G Type document.

Project Files

Parent topic:

Type Definitions

Related concepts:

- Type Definitions

Related tasks:

- Updating Custom Data Type Instances Throughout Your Project

<!--NI_TOPIC bundle=g-web-development path=creating-custom-palette.html language=enus -->
## TOPIC 00104: Creating a Custom Palette

- bundle_id: `g-web-development`
- source_path: `creating-custom-palette.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/creating-custom-palette.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `task`
- source_description: The palette provides an organized hierarchy of all the objects you can add to the diagram or panel. Create a palette file (.gpal), or an add-on library, to customize a palette category with the objects in your library. By default, custom categories are added to the Add-ons palette category. On the D

### Creating a Custom Palette

The palette provides an organized hierarchy of all the objects you can add to the
 diagram or panel. Create a palette file
 (.gpal), or an add-on library, to customize a palette category
 with the objects in your library. By default, custom categories are added to the
 Add-ons palette category.

1. On the 
 Document tab of a Library document, click 
 Create palette file.
2. In the 
 Palette Options dialog box, select the type of palette you want to create.
  - G diagram palette —Create a palette containing objects you can drop on the diagram.
  - G panel palette —Create a palette containing objects you can drop on the panel.
3. Click OK.
4. In the palette file, use the options on the 
 Item tab to customize each palette item.

Now that you have created your custom palette, consider
 creating localized string dictionaries for and optimizing your add-on library before creating
 a web application to demonstrate the use of your add-on library.

Parent topic:

Libraries

Related tasks:

- Creating a Web Application

Related reference:

- optimize-project

Related information:

- Create Localized String Directories

<!--NI_TOPIC bundle=g-web-development path=creating-library-from-existing-files.html language=enus -->
## TOPIC 00105: Creating a Library from Existing Files

- bundle_id: `g-web-development`
- source_path: `creating-library-from-existing-files.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/creating-library-from-existing-files.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `task`
- source_description: Use a Library document (.gcomp) to create a library from existing files. Before you begin, create a project that contains the files you want to include in your library. On the Project Files tab, right-click the VI(s) you want to include in your library and select Create Application/Library from item

### Creating a Library from Existing Files

Use a Library document (.gcomp) to create a library from existing files.

Before you begin, create a project that contains the files you want to include in your library.

1. On the 
 Project Files tab, right-click the VI(s) you want to include in your library and select 
 Create Application/Library from item.
2. In the Create Application or Library
 dialog box, set Type to
 Library.
3. Enter values in 
 Library name and 
 Namespace.
4. Determine whether to enable the Include
 dependencies not in an Application or Library checkbox. If you
 enable the Include dependencies not in an Application or
 Library checkbox, the Application or Library document you create
 includes any dependencies one or more of your VIs require that are not already
 in an Application or Library document.
5. Click OK.

The Library document appears in the project and contains the files you selected to include in the library.

Parent topic:

Libraries

<!--NI_TOPIC bundle=g-web-development path=creating-library.html language=enus -->
## TOPIC 00106: Creating a Library

- bundle_id: `g-web-development`
- source_path: `creating-library.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/creating-library.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `task`
- source_description: To create a library, create a Library document (.gcomp) and add source files to the document. Create a new Library document. Click FileNewLibrary. In the Create Library dialog box, enter values in Library name and Namespace. Click OK. Save the Library document. Add source files to the Library docume

### Creating a Library

To create a library, create a Library document (.gcomp) and add source files to the document.

1. Create a new Library document.
  1. Click 
 File»New»Library.
  2. In the 
 Create Library dialog box, enter values in 
 Library name and 
 Namespace.
  3. Click OK.
  4. Save the Library document.
2. Add source files to the Library document in one of the following ways:
  - Create files under the project and drag the files from the 
 Project Files tab to the Library document.
  - In the Library document, click 
 New on the document toolbar and select the type of file to create.
  - In the Library document, click 
 New»Import files on the document toolbar and select files on disk to copy to the Library document.
3. For each item in the Library document, configure the build options as needed.
  - Enable Export if you
 want to allow a source file to be called from other applications or
 libraries. Disable Export for internal source
 files.
  - Enable Always
 include if you want to include a support file, such as a
 text, image, or audio file or source files, such as .gvis or .gtypes, when
 you share the library.
4. On the Document tab, enter information about your library
 in the Details section.
5. Click File»Save all.

Now that you have created a library, consider optimizing your
 library before you package it.

Parent topic:

Libraries

Related tasks:

- Packaging a Library

Related reference:

- optimize-project

<!--NI_TOPIC bundle=g-web-development path=cursor-legend.html language=enus -->
## TOPIC 00107: Cursor Legend

- bundle_id: `g-web-development`
- source_path: `cursor-legend.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/cursor-legend.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Display a marker at a defined point coordinate. You can display multiple cursors on a graph.

### Cursor Legend

Display a marker at a defined point coordinate. You can display multiple cursors on a graph.

Parent topic:

Creating User Interfaces

<!--NI_TOPIC bundle=g-web-development path=cursors.html language=enus -->
## TOPIC 00108: Cursors

- bundle_id: `g-web-development`
- source_path: `cursors.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/cursors.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Add or configure a cursor.

### Cursors

Add or configure a cursor.

Parent topic:

Creating User Interfaces

<!--NI_TOPIC bundle=g-web-development path=customizing-appearance-controls-webvi.html language=enus -->
## TOPIC 00109: Customizing the Appearance of Controls in a WebVI

- bundle_id: `g-web-development`
- source_path: `customizing-appearance-controls-webvi.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/customizing-appearance-controls-webvi.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `task`
- source_description: Use Cascading Style Sheets (CSS) to customize the appearance of controls in a WebVI. You can modify properties such as the font, color, shape, or layout of a control. Before you begin, complete the following: Familiarize yourself with CSS on the Mozilla Developer Network Open or create a web applica

### Customizing the Appearance of Controls in a WebVI

Use 
 *Cascading Style Sheets* (CSS) to customize the appearance of controls in a WebVI. You can modify properties such as the font, color, shape, or layout of a control.

Before you begin, complete the following:

- Familiarize yourself with CSS on the Mozilla
 Developer Network
- Open or create a web application project

Note

1. Open the panel of a WebVI and click Edit HTML Source
 ([IMAGE alt='image' src='GUID-6B081D95-21C2-42EC-95DA-E5868B1FD666-a5.png']).
2. In the <head></head> tags, add the following lines
 of code after the <style
 ni-autogenerated-style-id=""></style> tags. 
 <style>
 selector {
 property 1: value 1;
 property 2: value 2;
 ...
 property n: value n;
 }
</style>
 CSS Item
 Descriptionselector
 The element you want to customize. You can select an
 element by its tag name, ID, class, or attribute.
 Example: ni-string-control
 property:
 value
 The property of the element that you want to customize
 and the value you want to change it to. Example:
 --ni-control-background-color: orange; 
 For example, you can use the following code to change the background color of
 a string control from the default white to orange.
 
[IMAGE alt='image' src='GUID-FD8C998C-AD2E-45D5-B626-C1044D81FCEB-a5.png'] 

 <style>
 ni-string-control {
 --ni-control-background-color: orange;
 }
</style>
 CSS Item
 Descriptionni-string-control
 This selector targets every string control in a WebVI.
 --ni-control-background-color: orange;
 This sets the CSS Custom Property named
 --ni-control-background-color to the
 color orange. The
 --ni-control-background-color CSS
 Custom Property targets the background color of string
 controls.
3. Click 
 OK and verify your changes.

Search within the programming environment to access the following installed example:

*Customize with CSS*

Parent topic:

Creating User Interfaces

Related reference:

- Best Practices for Customizing the Appearance of Controls in a WebVI

Related information:

- Mozilla Developer Network

<!--NI_TOPIC bundle=g-web-development path=customizing-labview-nxg.html language=enus -->
## TOPIC 00110: Customizing G Web Development Software

- bundle_id: `g-web-development`
- source_path: `customizing-labview-nxg.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/customizing-labview-nxg.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `task`
- source_description: Customize the G Web Development Software environment by changing the mouse wheel behavior, displaying tabs in the editor, and adding guide lines to the panel and diagram.

### Customizing G Web Development Software

Customize the G Web Development Software environment by changing the mouse wheel
 behavior, displaying tabs in the editor, and adding guide lines to the panel and
 diagram.

- [Customizing Mouse Wheel Behavior](control-zoom-mouse-wheel.html) You can change the action the mouse wheel performs within the workspace.
- [Displaying Tabs in the Editor](display-tabs.html) Display tabs in the editor to access different types of information about your project as well as to complete project-related tasks, such as troubleshooting or resource management.
- [Aligning Objects on the Panel](smart-guides.html) When Smart Guides are enabled, the editor displays guide lines to help you align and organize objects as you add them to the panel.
- [Displaying the Diagram Grid](diagram-grid.html) As you place objects on the diagram, they automatically align to a grid. Making this grid visible can help you keep the diagram organized as you add and arrange objects.
- [Resetting the Workspace](resetting-workspace.html) You can quickly restore the workspace to the default settings after you make adjustments.

Parent topic:

Getting Started with G Web Development Software

<!--NI_TOPIC bundle=g-web-development path=data-grid.html language=enus -->
## TOPIC 00111: Data Grid

- bundle_id: `g-web-development`
- source_path: `data-grid.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/data-grid.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Group elements of various data types as rows on a table. The data grid control is a 1D array of clusters. Each row of the table is one cluster, and each element in a cluster represents one column. You can use the data grid control to configure hardware or to display data in a table.

### Data Grid

Group elements of various data types as rows on a table.

The data grid control is a 1D array of clusters. Each row of the table is one cluster, and each element in a cluster represents one column.

You can use the data grid control to configure hardware or to display data in a table.

[IMAGE alt='image' src='GUID-E5B69C4B-B03D-40B0-98F3-75EC3F3FDF99-a5.png']

Parent topic:

Array Controls

<!--NI_TOPIC bundle=g-web-development path=data-items-cluster-tab-controls.html language=enus -->
## TOPIC 00112: Data items

- bundle_id: `g-web-development`
- source_path: `data-items-cluster-tab-controls.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/data-items-cluster-tab-controls.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Edit the name and order of the items on the control.

### Data items

Edit the name and order of the items on the control.

Parent topic:

Creating User Interfaces

<!--NI_TOPIC bundle=g-web-development path=data-type-selection-api.html language=enus -->
## TOPIC 00113: Data Type Selection for Distributed APIs

- bundle_id: `g-web-development`
- source_path: `data-type-selection-api.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/data-type-selection-api.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Refer to the following table for best practices for selecting data types. Guideline Required or Recommended? Details Example(s) For numeric input or output values, use double-precision for floating-point values and I32 for integer values unless there is a specific reason to use another type. Require

### Data Type Selection for Distributed APIs

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

Parent topic:

Best Practices for Designing and Developing an Application Programming Interface (API) in G Web Development Software

Related concepts:

- Best Practices for Designing and Developing an Application Programming Interface (API) in G Web Development Software

<!--NI_TOPIC bundle=g-web-development path=data-types-ni.platformframework.html language=enus -->
## TOPIC 00114: Data Types Palette

- bundle_id: `g-web-development`
- source_path: `data-types-ni.platformframework.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/data-types-ni.platformframework.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Add images related to data types to the icon.

### Data Types Palette

Add images related to data types to the icon.

Parent topic:

Creating User Interfaces

<!--NI_TOPIC bundle=g-web-development path=data-types.html language=enus -->
## TOPIC 00115: Data Type Reference

- bundle_id: `g-web-development`
- source_path: `data-types.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/data-types.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: You can use the following data types for controls and indicators, diagram terminals, wires, and node terminals. Icon Data Type Details Single-precision, floating-point numeric (SGL) Minimum positive number: 1.40e-45 Maximum positive number: 3.40e+38 Minimum negative number: -3.40e+38 Maximum negativ

### Data Type Reference

You can use the following data types for controls and indicators, diagram terminals, wires, and node terminals.

| Icon | Data Type | Details |
| --- | --- | --- |
|  | Single-precision, floating-point numeric (SGL) | Minimum positive number: 1.40e-45 Maximum positive number: 3.40e+38 Minimum negative number: -3.40e+38 Maximum negative number: -1.40e-45 |
|  | Double-precision, floating-point numeric (DBL) | Minimum positive number: 4.94e-324 Maximum positive number: 1.79e+308 Minimum negative number: -1.79e+308 Maximum negative number: -4.94e-324 |
|  | Complex single-precision, floating-point numeric (CSG) | Same as single-precision, floating-point, with a real and an imaginary part. |
|  | Complex double-precision, floating-point numeric (CDB) | Same as double-precision, floating-point, with a real and an imaginary part. |
|  | 8-bit signed integer numeric (I8) | A positive or negative integer stored using 8 bits, or a single byte. Range: -128 to 127 |
|  | 16-bit signed integer numeric (I16) | A positive or negative integer stored using 16 bits, or two bytes. Range: -32,768 to 32,767 |
|  | 32-bit signed integer numeric (I32) | A positive or negative integer stored using 32 bits, or four bytes. Range: -2,147,483,648 to 2,147,483,647 |
|  | 64-bit signed integer numeric (I64) | A positive or negative integer stored using 64 bits, or eight bytes. Approximate Range: -1e19 to 1e19 |
|  | 8-bit unsigned integer numeric (U8) | A positive integer stored using 8 bits, or a single byte. Range: 0 to 255 |
|  | 16-bit unsigned integer numeric (U16) | A positive integer stored using 16 bits, or two bytes. Range: 0 to 65,535 |
|  | 32-bit unsigned integer numeric (U32) | A positive integer stored using 32 bits, or four bytes. Range: 0 to 4,294,967,295 |
|  | 64-bit unsigned integer numeric (U64) | A positive integer stored using 64 bits, or eight bytes. Approximate Range: 0 to 2e19 |
|  | timestamp | A time and date. Minimum time: 01/01/1600 00:00:00 UTC maximum time: 01/01/3001 00:00:00 UTC |
|  | enumerated type | A list of items from which to select. |
|  | Boolean | A TRUE/FALSE value. |
|  | string | A series of text characters. |
|  | array | A collection of multiple pieces of data, each of which must be the same data type. The array icon shows the data type of the array's elements in square brackets and takes the color of that data type. As you add dimensions to the array, the thickness of the output wire increases. |
|  | cluster | A collection of multiple pieces of data, each of which can be a different data type. Cluster data types appear brown if all elements in the cluster are numeric or pink if any elements in the cluster are of non-numeric types. |
|  | error cluster | A cluster of information that specifies error conditions returned by a node. |
|  | waveform | A cluster of information that specifies an array of data, the start time at which the data was collected, and the change in time between each measurement. |
|  | reference number (refnum) | A unique identifier for an object, such as a task. |
|  | variant | A generic container for all other types of data. |

Parent topic:

Programming in G

<!--NI_TOPIC bundle=g-web-development path=dataflow-duplicates.html language=enus -->
## TOPIC 00116: Dataflow between Duplicates of the Same Terminal

- bundle_id: `g-web-development`
- source_path: `dataflow-duplicates.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/dataflow-duplicates.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use a duplicated output terminal to write to an indicator at multiple places on the diagram. You can also use a duplicated input terminal to read from a control at multiple places on the diagram. Terminals are duplicates of one another if they have the exact same label. You can duplicate a t

### Dataflow between Duplicates of the Same Terminal

You can use a duplicated output terminal to write to an indicator at multiple places on the diagram. You can also use a duplicated input terminal to read from a control at multiple places on the diagram.

Note

Create Duplicate Terminal

In the following example, the 
 String indicator displays a different message depending on which While Loop is executing. This example also uses a duplicate of the 
 Run button to control the execution of both While Loops.

Figure 3.

[IMAGE alt='image' src='GUID-02DB5688-C953-4D32-8246-7202DBA72A8B-a5.png']

Figure 4.

[IMAGE alt='image' src='GUID-921D89F7-8B3D-40CF-88A1-111CA3B3F846-a5.png']

Parent topic:

Terminals

Related concepts:

- Terminals
- Dataflow between the Diagram and Another VI
- Data Transfer between the Panel and the Diagram

<!--NI_TOPIC bundle=g-web-development path=dataflow-panel.html language=enus -->
## TOPIC 00117: Data Transfer between the Panel and the Diagram

- bundle_id: `g-web-development`
- source_path: `dataflow-panel.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/dataflow-panel.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `concept`
- source_description: Data in a control flows from the panel to the diagram through a corresponding input terminal. Data in an output terminal flows from the diagram to the panel through a corresponding indicator. The following image shows the flow of data between the panel and diagram of a VI.

### Data Transfer between the Panel and the Diagram

Data in a control flows from the panel to the diagram through a corresponding input terminal. Data in an output terminal flows from the diagram to the panel through a corresponding indicator.

The following image shows the flow of data between the panel and diagram of a VI.

[IMAGE alt='image' src='GUID-6F4B0B8A-8083-4D00-B7EA-5B1A33AC67DC-a5.png']

Parent topic:

Terminals

<!--NI_TOPIC bundle=g-web-development path=dataflow-subvi.html language=enus -->
## TOPIC 00118: Dataflow between the Diagram and Another VI

- bundle_id: `g-web-development`
- source_path: `dataflow-subvi.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/dataflow-subvi.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `concept`
- source_description: Terminals transfer data between the diagram and other VIs via subVIs. The following image shows the flow of data between terminals of the calling VI and a subVI. The calling VI passes data to the Percentage subVI through the input terminals of the subVI node. Data from the calling VI flows through t

### Dataflow between the Diagram and Another VI

Terminals transfer data between the diagram and other VIs via subVIs.
 The following image shows the flow of data between terminals of the calling VI and a subVI.

[IMAGE alt='image' src='GUID-A98B399D-70E2-4F90-B26F-1391933C335F-a5.png']

1. The calling VI passes data to the Percentage subVI through the input terminals of the subVI node.
2. Data from the calling VI flows through the input terminals on the diagram of the subVI.
3. As the subVI executes, data flows to the output terminal of the subVI diagram.
4. Data flows from the output terminal of the subVI diagram to the output terminal of the subVI node in the calling VI.

Parent topic:

Terminals

<!--NI_TOPIC bundle=g-web-development path=dataflow.html language=enus -->
## TOPIC 00119: Programming in G

- bundle_id: `g-web-development`
- source_path: `dataflow.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/dataflow.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `concept`
- source_description: G Dataflow (G) is a graphical programming language in which nodes on a diagram execute when data is available for all required inputs. A node in G Dataflow executes only when it receives data for all wired inputs. When a node finishes executing, it passes data along the wire to the next node in the

### Programming in G

*G Dataflow* (G) is a graphical programming language in which nodes on a diagram execute when data is available for all required inputs.

A node in G Dataflow executes only when it receives data for all wired
 inputs. When a node finishes executing, it passes data along the wire to the next node in
 the dataflow path. The movement of data along the wires and through the nodes is called
 dataflow and determines the execution order of nodes on the diagram.

Because a node executes only when all of the inputs receive data, the Subtract node in the following G diagram cannot execute until Add finishes executing and passes the data to Subtract.

[IMAGE alt='image' src='GUID-AF97D482-CA7E-40B3-99C5-6403310D8C5F-a5.png']

However, in the following G diagram, the Add, Random Number, and Divide nodes all meet the dataflow requirement of having the required input data they need to execute. Nodes not connected to each other by wires can execute in any order because the nodes do not depend on data from another node. You cannot determine which node executes first.

[IMAGE alt='image' src='GUID-06651DCB-2B39-43AD-8C2D-ACB35E394490-a5.png']

Because the flow of data, rather than the sequential order of commands, determines the execution order of nodes in G, you can create diagrams that have simultaneous operations. The image above illustrates operations that run simultaneously.

Parent topic:

G Web Development Software

<!--NI_TOPIC bundle=g-web-development path=debugging-a-webvi.html language=enus -->
## TOPIC 00120: Debugging a WebVI

- bundle_id: `g-web-development`
- source_path: `debugging-a-webvi.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/debugging-a-webvi.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `task`
- source_description: WebVIs support a subset of the debugging techniques available in an editor like LabVIEW. You can debug WebVIs using the following strategies. Choose between the following debugging options. Use Case Instructions You want to probe the value of a wire while running in the editor. See the Using Probes

### Debugging a WebVI

WebVIs support a subset of the debugging techniques available in an editor like
 LabVIEW. You can debug WebVIs using the following strategies.

Choose between the following debugging options.

| Use Case | Instructions |
| --- | --- |
| You want to probe the value of a wire while running in the editor. | See the Using Probes to Check Values on a Wire topic.Note G Web does not support highlight execution or breakpoints. |
| You want to see the error output of diagram objects. | WebVIs support an alternative to automatic error management that logs unhandled errors to the Output tab or browser development console. Because this does not provide the full capabilities of automatic error management, make sure you follow the guidelines for programmatic error management. Note To view your error output, create an error indicator and place it on the panel. |
| Use this debugging strategy in either of the following cases. You need to debug a subVI in your web application. You want to log error information to the console of your web browser. | To write log error information to the console of your web browser or G Web Development Software output window, go to the diagram palette and select Interoperability » Operating System » Write to System Log. To view the information output by Write to System Log within the editor, on the Navigation pane, open the Output tab by clicking Tool Launcher » All » Output. To view the information output by Write to System Log in a web browser, use the console of the web browser development tools. |
| You need to debug your top-level WebVI. | Wire extra indicators at any point in your WebVI code to imitate probes and display the data that flows through a wire. Note WebVIs do not currently support G types as controls or indicators on the panel. If you create an indicator from a G type on the diagram, no corresponding indicator is available on the panel. |

Parent topic:

Creating a Web Application

Related concepts:

- Using Probes to Check Values on a Wire

Related tasks:

- Building a Web Application as a Web Page

Related information:

- Error Management

<!--NI_TOPIC bundle=g-web-development path=debugging-jsli.html language=enus -->
## TOPIC 00121: Debugging JavaScript Library Interfaces

- bundle_id: `g-web-development`
- source_path: `debugging-jsli.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/debugging-jsli.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `task`
- source_description: Solve common problems that may occur when configuring and using JavaScript Library Interfaces (JSLIs). Most errors occur due to mismatches between the JSLI configuration and the functions in the JavaScript library. Mismatch errors may not occur at the exact time the JavaScript function call executes

### Debugging JavaScript Library Interfaces

Solve common problems that may occur when configuring and using JavaScript Library Interfaces (JSLIs).

Note

Use the following table to resolve common errors.

| Issue | Solution |
| --- | --- |
| You receive a Function not found error. | Verify the JSLI uses the correct spelling and case sensitivity for the entry points you defined. |
| The JSLI node does not appear in the software palette on the diagram. | Check the Project Files tab and ensure that the JSLI document is in a web application document. |
| The changes you make to the HTML source panel do not take affect. | Verify your HTML is valid. |
| You do not get the results you expected from your entry point. | Verify that the parameters are in the correct order in the JSLI document. |
| Your function does not appear to be called. | Add temporary calls to console.log('my custom message') to your JavaScript code to print a custom message to the console when it is called.Note To view messages printed to the console, see Debugging a WebVI. |

Parent topic:

Calling JavaScript Functions in a Web Application

<!--NI_TOPIC bundle=g-web-development path=debugging-tools.html language=enus -->
## TOPIC 00122: Testing and Debugging

- bundle_id: `g-web-development`
- source_path: `debugging-tools.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/debugging-tools.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `concept`
- source_description: When the results of your application are not what you expect, use a set of tools to determine where errors occur within your code. Although errors are often detected automatically, sometimes your code can run successfully but not as intended. When this happens, you need to identify the source of the

### Testing and Debugging

When the results of your application are not what you expect, use a
 set of tools to determine where errors occur within your code.

Although errors are often detected automatically, sometimes your code can run successfully but not as intended. When this happens, you need to identify the source of the unintended behaviors.

The Probes debugging tool can help you in this process.

Parent topic:

G Web Development Software

<!--NI_TOPIC bundle=g-web-development path=default.html language=enus -->
## TOPIC 00123: Default button

- bundle_id: `g-web-development`
- source_path: `default.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/default.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Set the value when the VI loads or when you reinitialize the data of the control to default.

### Default button

Set the value when the VI loads or when you reinitialize the data of the control to
 default.

Parent topic:

Creating User Interfaces

<!--NI_TOPIC bundle=g-web-development path=define-calls-using-jsli.html language=enus -->
## TOPIC 00124: Defining Calls to JavaScript Functions using a JavaScript Library Interface

- bundle_id: `g-web-development`
- source_path: `define-calls-using-jsli.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/define-calls-using-jsli.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `task`
- source_description: To call JavaScript functions in your web application, define calls to the JavaScript functions using a JavaScript Library Interface (JSLI) document. Before you begin, create or open a web application project and prepare your JavaScript code for use with the JSLI.For the JSLI to access a JavaScript f

### Defining Calls to JavaScript Functions using a JavaScript Library Interface

To call JavaScript functions in your web application, define calls to the JavaScript functions using a JavaScript Library Interface (JSLI) document.

Note

To create and configure a JSLI document, complete the following steps:

1. On the 
 Project Files tab, add a JSLI to a web application component or library component in your project. 
 A JSLI document appears in your web application.
2. Define the prototype for the JavaScript function you want to call. A defined call to a JavaScript function in a JSLI is called an 
 *entry point*.
  1. In the JavaScript global form field, enter the name of the JavaScript function you want to call. The name you enter must exactly match the function name in the JavaScript code. You must specify all functions relative to the global scope. Use dot notation to refer to nested objects. For example, if you want to call the absolute function abs in the object Math, you must specify 
 Math.abs in the JavaScript global form field. 
 Note The JavaScript global form field is case sensitive.
  2. Click 
 Add function to create an entry point. The default entry point name is created from the JavaScript global.
  3. Click 
 Add parameter.
  4. On the 
 Item tab, specify the parameter name, data type, and JavaScript representation. 
 Consider the following information when you add parameters to your prototype: 
 You can choose any name for the parameters you add to a JSLI document, but you must add them in the same order as they appear in the JavaScript function.The parameter and return data types you specify in the JSLI document must match the parameter and return data types in the JavaScript function.The parameter in the top position in the JSLI document is always the return type.
3. Repeat step 2 to create as many entry points as you need for your project.

Parent topic:

Calling JavaScript Functions in a Web Application

Related tasks:

- Waiting for Asynchronous JavaScript Operations to Complete in a Web Application
- Debugging JavaScript Library Interfaces
- Preparing Your Code For Use With a JavaScript Library Interface

Related reference:

- JavaScript Resources

<!--NI_TOPIC bundle=g-web-development path=delete-icon-editor.html language=enus -->
## TOPIC 00125: Delete

- bundle_id: `g-web-development`
- source_path: `delete-icon-editor.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/delete-icon-editor.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Add a delete symbol to the icon.

### Delete

Add a delete symbol to the icon.

Parent topic:

Actions Palette

<!--NI_TOPIC bundle=g-web-development path=design-develop-projects-g.html language=enus -->
## TOPIC 00126: Best Practices for Creating Projects in G Web Development Software

- bundle_id: `g-web-development`
- source_path: `design-develop-projects-g.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/design-develop-projects-g.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `concept`
- source_description: To develop projects that successfully serve your needs and the needs of your end users, refer to the following best practice guidelines:

### Best Practices for Creating Projects in G
 Web Development Software

To develop projects that successfully serve your needs and the needs of your end users, refer to the following best practice guidelines:

- [File and Project Organization in G Web Development Software](file-prog-org-lv.html) Refer to the following table for best practices for organizing files and projects in G Web Development Software.
- [Icons and Connector Panes for G Web Development Software Projects](icons-connector-panes-lv-proj.html) Refer to the following table for best practices for creating icons and connector panes in G Web Development Software.
- [Panel Design for G Web Development Software Projects](panel-design-lv-projects.html) Refer to the following table for best practices for designing panels in the G Web Development Software.
- [Diagram Design for G Web Development Software Projects](diagram-design-lv-projects.html) Refer to the following table for best practices for designing diagrams in G Web Development Software.

Parent topic:

Programming in G

<!--NI_TOPIC bundle=g-web-development path=design-patterns.html language=enus -->
## TOPIC 00127: Programming Design Patterns

- bundle_id: `g-web-development`
- source_path: `design-patterns.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/design-patterns.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `concept`
- source_description: A design pattern is a code structure or practice that solves common programming problems. Here are a few examples of design patterns and the problems they solve. Event-driven programming allows your code to respond to events during execution. The state machine design pattern allows you to execute di

### Programming Design Patterns

A design pattern is a code structure or practice that solves common programming
 problems.

Here are a few examples of design patterns and the problems they solve.

- Event-driven programming allows your code to respond to events during
 execution.
- The state machine design pattern allows you to execute different parts of your code
 based on the state of your application.

Parent topic:

Programming in G

<!--NI_TOPIC bundle=g-web-development path=designing-flex-ui.html language=enus -->
## TOPIC 00128: Designing a Responsive User Interface

- bundle_id: `g-web-development`
- source_path: `designing-flex-ui.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/designing-flex-ui.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `task`
- source_description: You can design the user interface of a WebVI to respond to different screen sizes. Suppose you want your WebVI to run on both a computer monitor and a tablet device; or you want the WebVI to run on a mobile phone that users expect to scroll only vertically. Instead of creating a user interface for e

### Designing a Responsive User Interface

You can design the user interface of a WebVI to respond to different screen sizes.

Suppose you want your WebVI to run on both a computer monitor and a tablet device; or you want the WebVI to run on a mobile phone that users expect to scroll only vertically. Instead of creating a user interface for each use case, you can design a single user interface that adapts the panel and its contents to the screen size.

1. Create a WebVI within your application document.
2. On the 
 Panel tab, set 
 Panel layout to 
 Flexible.
3. Create containers by placing objects on the panel. 
 
 A container appears as a border when you hover over objects on the panel.
  - On an empty panel, place a control or indicator anywhere on the panel to create a container.
  - Place a control or indicator outside an existing container to create a new container. You can create multiple containers in a column or in a row.
4. Select a container and configure the layout options in the 
 Layout section of the 
 Item tab to determine how objects in the container arrange and align when the screen size changes.
5. Select an object and configure the layout options in the 
 Layout section of the 
 Item tab to set the object size and whether the object resizes when the screen size changes.
6. Click 
 File»Save all to save all files.
7. Select Run»Run in browser to view your application in a web browser. 
 Resize the web browser and ensure the controls and indicators
 resize appropriately.

To make your web application available to other users, host your build output on a web server that is accessible to other users.

Parent topic:

Creating User Interfaces

Related tasks:

- Aligning and Arranging Objects in a Responsive User Interface
- Building a Web Application as a Web Page
- Hosting a Web Application on a Server

<!--NI_TOPIC bundle=g-web-development path=develop-web-application.html language=enus -->
## TOPIC 00129: Developing a Web Application

- bundle_id: `g-web-development`
- source_path: `develop-web-application.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/develop-web-application.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `concept`
- source_description: Learn about the different tasks you complete to develop a web application using G Web Development Software. Write a program to run in a web browser. Create responsive interfaces and customize controls for your web application. Learn about strategies to debug your WebVIs. Build and view your applicat

### Developing a Web Application

Learn about the different tasks you complete to develop a web application using G Web
 Development Software.

- Write a program to run in a web browser.
- Create responsive interfaces and customize controls for your web application.
- Learn about strategies to debug your WebVIs.
- Build and view your application in a web browser
- Link multiple WebVIs to create multiple web pages.
- Learn how to configure a package or package installer for your web application.

Parent topic:

G Web Development Software

Related tasks:

- Creating a Web Application
- Designing a Responsive User Interface
- Debugging a WebVI
- Building a Web Application as a Web Page
- Linking WebVIs in a Web Application
- Packaging an Application or Library

<!--NI_TOPIC bundle=g-web-development path=diagram-components-state-machine.html language=enus -->
## TOPIC 00130: Diagram Components of a State Machine

- bundle_id: `g-web-development`
- source_path: `diagram-components-state-machine.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/diagram-components-state-machine.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `concept`
- source_description: A state machine has four components on the diagram: a While Loop, a Case Structure, an Enum constant, and a shift register. While Loop—Sets the outer boundary for the state machine code and facilitates state transitions. Case Structure—Contains a subdiagram for each state in the state machine. Shift

### Diagram Components of a State Machine

A state machine has four components on the diagram: a While Loop, a Case Structure, an Enum constant, and a shift register.

[IMAGE alt='image' src='GUID-963C1926-B50A-4314-A03B-BE6F12BDECBA-a5.png']

1. While Loop—Sets the outer boundary for the state machine code and facilitates state transitions.
2. Case Structure—Contains a subdiagram for each state in the state machine.
3. Shift register—Passes data from a completed state to the upcoming state.
4. Enum constant—Contains a list of every state in the state machine. The state machine uses this constant to update the current state transition value as the program executes.

Note

Enum constant

Enum constant

Parent topic:

State Machine Design Pattern

<!--NI_TOPIC bundle=g-web-development path=diagram-design-lv-projects.html language=enus -->
## TOPIC 00131: Diagram Design for G Web Development Software Projects

- bundle_id: `g-web-development`
- source_path: `diagram-design-lv-projects.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/diagram-design-lv-projects.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Refer to the following table for best practices for designing diagrams in G Web Development Software. Guideline Required or Recommended? Details Example(s) Use a type definition when you use the same unique control in more than one location or when your project includes a large data structure that p

### Diagram Design for G Web Development
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

[IMAGE alt='image' src='GUID-C6D26EFF-2DAD-42EC-8DD6-E98842DBA1BD-a5.png']

Parent topic:

Best Practices for Creating Projects in G Web Development Software

<!--NI_TOPIC bundle=g-web-development path=diagram-grid.html language=enus -->
## TOPIC 00132: Displaying the Diagram Grid

- bundle_id: `g-web-development`
- source_path: `diagram-grid.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/diagram-grid.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `task`
- source_description: As you place objects on the diagram, they automatically align to a grid. Making this grid visible can help you keep the diagram organized as you add and arrange objects. Click FilePreferences to display the Preferences dialog box. On the VI tab, in the Diagram Editing Defaults section, place a check

### Displaying the Diagram Grid

As you place objects on the diagram, they automatically align to a grid. Making this grid visible can help you keep the diagram organized as you add and arrange objects.

1. Click 
 File»Preferences to display the 
 Preferences dialog box.
2. On the 
 VI tab, in the 
 Diagram Editing Defaults section, place a checkmark in the 
 Always Show Grid checkbox. 
 [IMAGE alt='image' src='GUID-836825A2-3C61-453D-A514-0D65D385612D-a5.png']

Parent topic:

Customizing G Web Development Software

<!--NI_TOPIC bundle=g-web-development path=dialog-type.html language=enus -->
## TOPIC 00133: Dialog Type

- bundle_id: `g-web-development`
- source_path: `dialog-type.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/dialog-type.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Set whether you can select a file or a directory with the path control.

### Dialog Type

Set whether you can select a file or a directory with the path control.

Parent topic:

Creating User Interfaces

<!--NI_TOPIC bundle=g-web-development path=differences-labview-labviewnxg.html language=enus -->
## TOPIC 00134: Differences between LabVIEW and G Web Development Software

- bundle_id: `g-web-development`
- source_path: `differences-labview-labviewnxg.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/differences-labview-labviewnxg.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Learn the differences between LabVIEW and G Web Development Software so that you can identify the areas in your application that may change during conversion. The following table lists terminology differences between LabVIEW and G Web Development Software. This table is not an exhaustive list of all

### Differences between LabVIEW and G Web
 Development Software

Learn the differences between LabVIEW and G Web Development Software so that you can
 identify the areas in your application that may change during conversion.

The following table lists terminology differences between LabVIEW and G Web
 Development Software.

Note

| LabVIEW | G Web Development Software |
| --- | --- |
| Application Directory | Relative Paths |
| Unbundle By Name/Bundle By Name (Clusters) | Cluster Properties |
| CTL (Strict Typedef) | Type Definitions |
| Formula Node | No equivalent behavior. |
| Global Variable | No equivalent behavior. |
| LabVIEW Class | No equivalent behavior. |
| Local Variable | Duplicate Terminal |
| Get Waveform Components | Waveform Properties |
| VI Server | Panel Manipulation |

The following table lists behaviors in G Web Development Software that differ from
 LabVIEW.

Note

| LabVIEW | G Web Development Software |
| --- | --- |
| Build Specification - Installer | Package or Package Installer |
| Call Library Function Node | JavaScript Library Interface |
| CTL (Control Definition) | No equivalent behavior. |
| CTL (Typedef) | Type Definition |
| Creating Actors and Messages with Actor Framework | No equivalent behavior. |
| DataSocket API | No equivalent behavior. See Communicating Data with a Web Application for more information about other networking APIs. |
| Express VIs | SubVIs |
| Flattening and Unflattening to Binary | No equivalent behavior. Consider using To Variant and Variant to Data VIs for compatible use cases. |
| Invoke Nodes | Invoke nodes are replaced with VIs that have corresponding behavior. |
| MathScript | No equivalent behavior. |
| Merge Errors | Retain First Error behaves similarly. Consider using Multiplex Errors for handling multiple errors on the same wire. |
| .NET Constructor Nodes and Invoke Nodes | No equivalent behavior. See JavaScript Library Interface for more information about calling JavaScript libraries. |
| Packed Project Libraries | No equivalent behavior. |
| Polymorphic VIs | An overload VI or a multi-mode element. |
| Sub-panels | No equivalent behavior. |
| String Encoding | The string data type is UTF-8.Note Casting other data types, such as binary, to a string may cause unexpected behavior when displaying or manipulating the string. |
| Tree Control | Tree Control |
| VI Package Manager | Use NI Package Manager for distributing and updating both source code and deployed applications. |
| XControls | No equivalent behavior. |

The following table lists common keyboard shortcuts that differ between LabVIEW and G Web
 Development Software.

Note

| Command | LabVIEW | G Web Development Software |
| --- | --- | --- |
| Create branch from wire | Click near a wire | Hold Ctrl to change to the wiring cursor while hovering over a wire (Default preference setting, which you can change.) |
| Create constants for all unwired inputs | <Ctrl-Space> then <Ctrl-Shift-D> | <Ctrl-M> |
| Create constants for required unwired inputs | No equivalent behavior. | <Ctrl-Shift-M> |
| Go through case/event structures on diagram | <Ctrl-Scroll Wheel> | <Ctrl-Shift-Scroll Wheel> |
| Insert on wire | <Ctrl-Space> then <Ctrl-I> | Right-click on wire and select or search for new VI. Error wires automatically connected if applicable. |
| Pan on canvas | <Ctrl-Shift-Drag> | <Space-Drag> |
| Remove wire and rewire | <Ctrl-Space> then <Ctrl-R> | <Ctrl-Del> |
| Replace object | <Ctrl-Space> then <Ctrl-P> | Right-click on VI and select a new VI. |
| Show Panel and Diagram in separate windows | Default | Right-click on Panel/Diagram switcher or document tab and select Float in new window. |
| Show/hide panes | <Ctrl-\\> | <Ctrl-T> |
| Wire objects | <Ctrl-Space> then <Ctrl-W> | <Ctrl-J> |

Parent topic:

Converting LabVIEW NXG Web Module Projects to G Web Development Software Projects

Related concepts:

- Dataflow between Duplicates of the Same Terminal
- Type Definitions
- Communicating Data with a Web Application
- String Data

Related tasks:

- Packaging an Application or Library
- Calling JavaScript Functions in a Web Application
- Accessing Resource Files from a WebVI

Related reference:

- Text Controls
- Tree

Related information:

- Cluster Properties
- Waveform Properties
- Panel Manipulation Nodes
- Retain First Error
- Multiplex Errors
- NI Package Manager User Manual

<!--NI_TOPIC bundle=g-web-development path=digital-table.html language=enus -->
## TOPIC 00135: Digital Table

- bundle_id: `g-web-development`
- source_path: `digital-table.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/digital-table.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents data in up to six digital data states. Value Digital Data State Description 0 0 (Drive Low) Forces logic low. Drives to the low voltage level (V[OL]). 1 1 (Drive High) Forces logic high. Drives to the high voltage level (V[OH]). 2 Z (Force Off) Forces logic high impedance. Turns the drive

### Digital Table

Represents data in up to six digital data states.

| Value | Digital Data State | Description |
| --- | --- | --- |
| 0 | 0 (Drive Low) | Forces logic low. Drives to the low voltage level (VOL). |
| 1 | 1 (Drive High) | Forces logic high. Drives to the high voltage level (VOH). |
| 2 | Z (Force Off) | Forces logic high impedance. Turns the driver off. |
| 3 | L (Compare Low) | Compares logic low (edge). Compares a voltage level lower than the low voltage threshold. |
| 4 | H (Compare High) | Compares logic high (edge). Compares a voltage level higher than the high voltage threshold. |
| 5 | X (Compare Unknown) | Compares logic unknown. Does not compare. |

Parent topic:

Creating User Interfaces

<!--NI_TOPIC bundle=g-web-development path=digital-waveform.html language=enus -->
## TOPIC 00136: Digital Waveform

- bundle_id: `g-web-development`
- source_path: `digital-waveform.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/digital-waveform.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specify start time, delta t, input data, and attributes of a digital waveform.

### Digital Waveform

Specify start time, delta t, input data, and attributes of a digital waveform.

Parent topic:

Creating User Interfaces

<!--NI_TOPIC bundle=g-web-development path=digital-waveforms.html language=enus -->
## TOPIC 00137: Digital Waveform

- bundle_id: `g-web-development`
- source_path: `digital-waveforms.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/digital-waveforms.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Add a digital waveform data type symbol to the icon.

### Digital Waveform

Add a digital waveform data type symbol to the icon.

Parent topic:

Data Types Palette

<!--NI_TOPIC bundle=g-web-development path=disable-mapping-changes.html language=enus -->
## TOPIC 00138: Disable mapping changes

- bundle_id: `g-web-development`
- source_path: `disable-mapping-changes.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/disable-mapping-changes.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Prevent users from changing the scale mapping mode at run-time.

### Disable mapping changes

Prevent users from changing the scale mapping mode at run-time.

Parent topic:

Creating User Interfaces

<!--NI_TOPIC bundle=g-web-development path=display-digits.html language=enus -->
## TOPIC 00139: Display Digits

- bundle_id: `g-web-development`
- source_path: `display-digits.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/display-digits.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Set the precision of a numeric control or indicator.

### Display Digits

Set the precision of a numeric control or indicator.

Parent topic:

Creating User Interfaces

<!--NI_TOPIC bundle=g-web-development path=display-tabs.html language=enus -->
## TOPIC 00140: Displaying Tabs in the Editor

- bundle_id: `g-web-development`
- source_path: `display-tabs.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/display-tabs.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `task`
- source_description: Display tabs in the editor to access different types of information about your project as well as to complete project-related tasks, such as troubleshooting or resource management. Click View and select the tab(s) you want to display from the pull-down menu.

### Displaying Tabs in the Editor

Display tabs in the editor to access different types of information about your project as well as to complete project-related tasks, such as troubleshooting or resource management.

View

Parent topic:

Customizing G Web Development Software

<!--NI_TOPIC bundle=g-web-development path=display-type.html language=enus -->
## TOPIC 00141: Display Type

- bundle_id: `g-web-development`
- source_path: `display-type.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/display-type.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Set the numeric format of the control or indicator.

### Display Type

Set the numeric format of the control or indicator.

Parent topic:

Creating User Interfaces

<!--NI_TOPIC bundle=g-web-development path=distribute-apps-libs.html language=enus -->
## TOPIC 00142: Packaging an Application or Library

- bundle_id: `g-web-development`
- source_path: `distribute-apps-libs.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/distribute-apps-libs.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `task`
- source_description: Package your application or library for distribution. Before you begin, create an application or a library before completing the following tasks: Package an Application—Use a Package document (.lvdist) to build an application into a package. Package a Library—Use a Package document (.lvdist) to buil

### Packaging an Application or Library

Package your application or library for distribution.

Before you begin, create an application
 or a library before completing the following tasks:

- Package an Application—Use a Package document (.lvdist) to
 build an application into a package.
- Package a Library—Use a Package document (.lvdist) to build a
 library into a package or package installer.

Parent topic:

G Web Development Software

Related tasks:

- Creating a WebVI
- Creating a Library
- Packaging an Application
- Packaging a Library

<!--NI_TOPIC bundle=g-web-development path=distributed-scc-recommendations.html language=enus -->
## TOPIC 00143: Recommendations for Developing a Project in a Distributed Source Code Control System

- bundle_id: `g-web-development`
- source_path: `distributed-scc-recommendations.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/distributed-scc-recommendations.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Learn how to interact with a distributed source code control provider while developing a project. The following information uses terminology and commands from Git. However, you can apply these concepts when interacting with any distributed source code control provider. Obtaining a Working Copy of a

### Recommendations for Developing a Project in a Distributed Source Code Control System

Learn how to interact with a distributed source code control provider while developing a project.

Note

#### Obtaining a Working Copy of a File and Making Modifications

| Recommendation | Details |
| --- | --- |
| Merge from the central repository regularly during development. | Keeping your local copy of the project in sync with the central repository ensures you are developing code against the most recent version of the project. Fetch and merge to update code in your local repository. |
| Commit files to your local repository often. | Commit to your local repository as often as you want. It is common to commit locally many times per day. |

#### Committing and Pushing Files

| Recommendation | Details |
| --- | --- |
| Push all files with changes in the project folder. | Push any files with changes. Most source code control providers scan for changes to the project folder to help you identify changed files. |
| Ignore the following directories when you submit to the central repository: Builds.cache | Changes within these sub-directories do not affect the functionality of source code in the project. The project directory in the central repository may already be configured to ignore the folders. If not, include the directories in a .gitignore file. Refer to Git documentation for more information. |
| Add descriptive comments when you commit to your local repository or push to the central repository. | Descriptive comments help you and other developers interpret changes you submit to the repository. |

Parent topic:

Recommendations for Developing a Project Stored in a Source Code Control Repository

<!--NI_TOPIC bundle=g-web-development path=distributing-app-lib.html language=enus -->
## TOPIC 00144: Packaging an Application

- bundle_id: `g-web-development`
- source_path: `distributing-app-lib.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/distributing-app-lib.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `task`
- source_description: Use a Package document (.lvdist) to build an application into a package. The Package document contains the build configuration and metadata for your package, such as version, maintainer, and display name. Click FileNewPackage/Installer. The Package document opens in the project. Drag the files you w

### Packaging an Application

Use a Package document (.lvdist) to
 build an application into a package.
 The Package document contains the build configuration and metadata for your
 package, such as version, maintainer, and display name.

1. Click 
 File»New»Package/Installer. 
 The Package document opens in the project.
2. Drag the files you want to distribute from the 
 Project Files tab to the 
 Files section. 
 You can include applications and other support files. 
 The Package document automatically calculates the package dependencies that your application requires.
3. Review the contents of the 
 Package Dependencies section, which displays package dependencies your application requires. 
 You can include additional dependencies by clicking 
 Dependencies and selecting packages under 
 Add Dependencies.
4. In the 
 Information section, confirm that the Package document filled the text boxes with information you want. 
 The Package document automatically gathers information from the project and your NI User Account to complete the 
 Information section. The values in the text boxes become metadata in the package. NI Package Manager reads the metadata of packages to sort them and display information about them to users.
5. On the 
 Document tab, choose the target on which to build the package contents in 
 Build target.
6. Select the package output type from 
 Output type.
7. In 
 Output directory, specify the location to save the package output.
8. Click File»Save all.
9. Click 
 Build. 
 The Build Queue tab shows the status of the
 build process.

Right-click the package and click Locate directory in Windows Explorer
 to locate the package in the output directory. You can distribute your software
 content using NI Package Manager or other distribution channels.

Parent topic:

Packaging an Application or Library

<!--NI_TOPIC bundle=g-web-development path=distribution.html language=enus -->
## TOPIC 00145: distribution

- bundle_id: `g-web-development`
- source_path: `distribution.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/distribution.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Builds a distribution(.lvdist) file. To build a distribution from the CLI, use the following syntax: gwebcli.exe distribution -p=<relative or absolute path of the project> --dn=<name of the .lvdist file> For example: gwebcli.exe distribution -p="C:\G Web Projects\Project.gwebproject" --dn="Applicati

### distribution

Builds a distribution(.lvdist) file.

To build a distribution from the CLI, use the following syntax:

```text
        
          gwebcli.exe distribution -p=<relative or absolute path of the project> --dn=<name of the .lvdist file>
      
```

For example:

```text
        
          gwebcli.exe distribution -p="C:\G Web Projects\Project.gwebproject" --dn="Application.lvdist" 
      
```

| Argument | Required | Description | Example |
| --- | --- | --- | --- |
| -p --ppath=VALUE | Yes | Specifies the source path. This is a path to the .gwebproject containing the .lvdist to build. | -p="C:\\G Web Projects\\Project.gwebproject" --ppath="C:\\G Web Projects\\Project.gwebproject" |
| --dn --distributionDocumentName=VALUE | Yes | Specifies the name of the distribution document to build. | -dn="Application.lvdist" --distributionDocumentName="Application.lvdist" |
| -d --outputDirectory=VALUE | No | Specifies a custom output directory for the distribution. | — |
| --version=VALUE | No | Specifies the version for the distribution. The distribution build version does not automatically increment when you use this parameter. | — |
| --addonDirectory=VALUE | No | Specifies the custom addon installation location. By default, it is set to the "Addons" directory in the .exe directory. | — |
| --autoAddDependencies | No | Specifies whether to automatically calculate and add dependencies. | — |
| --retainIntermediaryOutputDirectory=VALUE | No | Specifies whether to retain intermediary output directory upon building a package. | — |
| --save | No | Specifies whether to save the distribution when finished. The default value is False. | — |
| --do --distributionOutputType=VALUE | No | Specifies the output type of the distribution to build. The default is the output type set in the distribution. Supported output types: nipackage and nipackageinstaller. | — |

Parent topic:

Predefined Command Line Operations

<!--NI_TOPIC bundle=g-web-development path=documentation-api.html language=enus -->
## TOPIC 00146: Documentation for Distributed APIs

- bundle_id: `g-web-development`
- source_path: `documentation-api.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/documentation-api.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Refer to the following table for best practices for documenting an API. Guideline Required or Recommended? Details Review the VI description and parameter descriptions of all public VIs in your API for correct meaning for what the VI does, usability by third parties who are unfamiliar with your API,

### Documentation for Distributed APIs

Refer to the following table for best practices for documenting an API.

| Guideline | Required or Recommended? | Details |
| --- | --- | --- |
| Review the VI description and parameter descriptions of all public VIs in your API for correct meaning for what the VI does, usability by third parties who are unfamiliar with your API, spelling, grammar, and naming conventions for G Web Development Software. | Required | N/A |

Parent topic:

Best Practices for Designing and Developing an Application Programming Interface (API) in G Web Development Software

Parent topic:

Best Practices for Designing and Developing an Application Programming Interface (API) in G Web Development Software

Related concepts:

- Best Practices for Designing and Developing an Application Programming Interface (API) in G Web Development Software

<!--NI_TOPIC bundle=g-web-development path=drawings-controls.html language=enus -->
## TOPIC 00147: Drawing Controls

- bundle_id: `g-web-development`
- source_path: `drawings-controls.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/drawings-controls.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Decorate the user interface with lines or shapes.

### Drawing Controls

Decorate the user interface with lines or shapes.

Parent topic:

Creating User Interfaces

<!--NI_TOPIC bundle=g-web-development path=edit-items.html language=enus -->
## TOPIC 00148: Edit Items

- bundle_id: `g-web-development`
- source_path: `edit-items.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/edit-items.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Add, delete, and configure the items within a selector control list.

### Edit Items

Add, delete, and configure the items within a selector control list.

Parent topic:

Creating User Interfaces

<!--NI_TOPIC bundle=g-web-development path=ellipse.html language=enus -->
## TOPIC 00149: Ellipse

- bundle_id: `g-web-development`
- source_path: `ellipse.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/ellipse.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Create a customizable ellipse.

### Ellipse

Create a customizable ellipse.

Parent topic:

Drawing Controls

<!--NI_TOPIC bundle=g-web-development path=empty-cluster.html language=enus -->
## TOPIC 00150: Empty Cluster

- bundle_id: `g-web-development`
- source_path: `empty-cluster.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/empty-cluster.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Create an empty group you can customize by dragging and dropping controls, such as buttons, graphs, arrays, and so on, on the cluster shell.

### Empty Cluster

Create an empty group you can customize by dragging and dropping controls, such as buttons, graphs, arrays, and so on, on the cluster shell.

Parent topic:

Creating User Interfaces

<!--NI_TOPIC bundle=g-web-development path=enable-sd.html language=enus -->
## TOPIC 00151: Enabling SystemDesigner Visibility

- bundle_id: `g-web-development`
- source_path: `enable-sd.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/enable-sd.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `task`
- source_description: Update your preferences to see a visual representation of web targets in SystemDesigner. SystemDesigner is not necessary for most G Web Development Software applications. If you have a project migrated to G Web that relied on SystemDesigner specific features such as Target-Defined symbols, see the f

### Enabling SystemDesigner Visibility

Update your preferences to see a visual representation of web targets in
 SystemDesigner.

Note

1. Click File»Preferences.
2. Select Web Server and enable Show
 SystemDesigner.
3. Reopen the project to apply the update.

Parent topic:

Getting Started with G Web Development Software

Parent topic:

Getting Started with G Web Development Software

Parent topic:

Creating a Web Application

<!--NI_TOPIC bundle=g-web-development path=enabling-cors-for-a-web-service.html language=enus -->
## TOPIC 00152: Enabling CORS for a Web Service

- bundle_id: `g-web-development`
- source_path: `enabling-cors-for-a-web-service.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/enabling-cors-for-a-web-service.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `task`
- source_description: To incorporate resources from a different origin into your web application, configure CORS for the server hosting those resources. Refer to the web service documentation or contact the web service administrator to verify if the web service allows cross-origin requests using CORS. The target web serv

### Enabling CORS for a Web Service

To incorporate resources from a different origin into your web application, configure
 CORS for the server hosting those resources.

1. Refer to the web service documentation or contact the web service administrator
 to verify if the web service allows cross-origin requests using CORS. 
 Note The target web service must enable
 cross-origin requests to allow HTTP requests from a WebVI executing in the development
 environment. Refer to *Hosting a Web Application During Development* for more
 information.
2. Determine whether the web service requires credentialed CORS requests. 
 If the web service requires credentialed requests, refer to
 *Sending a Credentialed Cross-Origin HTTP Request* to configure
 your application to send credentialed requests.
3. Ensure the web service administrator includes an
 Access-Control-Allow-Origin header in HTTP responses
 to enable cross-origin HTTP requests to the web service.
  - For non-credentialed simple CORS requests, set the Access-Control-Allow-Origin header to one of the
 following values:
    - The wildcard value (*) that allows any origin to
 access a resource. NI recommends using this value only during the
 development of your application.
    - The origin of the web
 application performing the HTTP request.
  - For credentialed simple requests, ensure the web service includes the
 following header values in responses to the web application:
    - Access-Control-Allow-Origin header set
 to the origin of the web application performing the HTTP request.
    - Access-Control-Allow-Credentials header
 set to True.

- Responding to a CORS preflight request during a non-simple CORS request
- Handling headers for browser caches
- Accepting additional request headers from a browser
- Allowing the browser to have access to additional response headers

Parent topic:

Considerations When Accessing Data from Web Services

Related concepts:

- Configuring CORS for a LabVIEW Web Service
- Hosting a Web Application During Development

Related tasks:

- Sending a Credentialed Cross-Origin HTTP Request

Related information:

- Mozilla Developer Network - Cross-Origin Resource Sharing (CORS)

<!--NI_TOPIC bundle=g-web-development path=enter-key-behavior-string-control.html language=enus -->
## TOPIC 00153: Enter key behavior

- bundle_id: `g-web-development`
- source_path: `enter-key-behavior-string-control.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/enter-key-behavior-string-control.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Choose the behavior of the Enter key. If you select Commits text, carriage returns are not allowed and pressing Enter terminates the edit session. If you select Enters new line, pressing Enter inserts a carriage return and pressing Ctrl-Enter terminates the session. You can always terminate the edit

### Enter key behavior

Choose the behavior of the Enter key. If you select 
Commits text, carriage returns are not allowed and pressing Enter terminates the edit session. If you select 
Enters new line, pressing Enter inserts a carriage return and pressing Ctrl-Enter terminates the session. You can always terminate the edit session by clicking elsewhere on the panel.

Parent topic:

Creating User Interfaces

<!--NI_TOPIC bundle=g-web-development path=enum-data.html language=enus -->
## TOPIC 00154: Enum Data

- bundle_id: `g-web-development`
- source_path: `enum-data.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/enum-data.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `concept`
- source_description: The enumerated type, or enum, is a container for a finite set of user-named values. Each item in the set has both a string and a numeric value. On the diagram, an enum appears as a pull-down list of names represented as numeric data. You can use the named values to drive the logic of your program. F

### Enum Data

The enumerated type, or enum, is a container for a finite set of user-named values. Each item in the set has both a string and a numeric value.

On the diagram, an enum appears as a pull-down list of names represented as numeric data.

You can use the named values to drive the logic of your program. For example, you can wire an enum constant or control to the selector of a Case Structure to create cases that correspond to each item in the enum.

[IMAGE alt='image' src='GUID-480CCAEC-EEC7-4817-9025-D0FA36C8609B-a5.png']

You can use the numeric values within the enum for numeric calculations or comparisons. If you wire an enum control to a numeric node or indicator, the enum value is coerced to a numeric value. All arithmetic functions except Increment and Decrement treat enum data the same as an unsigned integer.

Parent topic:

Data Type Reference

<!--NI_TOPIC bundle=g-web-development path=enum.html language=enus -->
## TOPIC 00155: Enum

- bundle_id: `g-web-development`
- source_path: `enum.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/enum.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Create a list that a user can cycle through to make selections. Enum values are pre-defined and do not change at run time.

### Enum

Create a list that a user can cycle through to make selections. Enum values are pre-defined and do not change at run time.

Parent topic:

Creating User Interfaces

<!--NI_TOPIC bundle=g-web-development path=error-codes.html language=enus -->
## TOPIC 00156: Error Codes

- bundle_id: `g-web-development`
- source_path: `error-codes.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/error-codes.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Find and read the description for an error code you encounter in software. Error Code Description Recommended Solution 2147467259 Unspecified error. N/A 1967345152 Invalid refnum. A specified refnum was not valid. Specify a valid refnum. 1967345151 Invalid property code. The specified property code

### Error Codes

Find and read the description for an error code you encounter in software.

| Error Code | Description | Recommended Solution |
| --- | --- | --- |
| 2147467259 | Unspecified error. | N/A |
| 1967345152 | Invalid refnum. A specified refnum was not valid. | Specify a valid refnum. |
| 1967345151 | Invalid property code. The specified property code is not valid for this refnum. | Specify a valid property for the refnum. |
| 1967345148 | Invalid argument. One of the specified arguments is invalid. | Specify a valid argument. |
| 1967345147 | Entry not found. The requested entry could not be found. | N/A |
| 375012 | A JSON numeric value is out of the range of a G Web Development Software numeric type. | N/A |
| 375011 | G Web Development Software failed to read or write a -Infinity or +Infinity floating-point value. | Enable G Web Development Software JSON extensions to allow support for a value of Infinity. |
| 375010 | G Web Development Software failed to read or write a NaN floating-point value. | Enable G Web Development Software JSON extensions to allow support for a value of NaN. |
| 375009 | The JSON string contains an invalid multi-dimensional array. | N/A |
| 375008 | The array has an invalid number of dimensions. | N/A |
| 375007 | The cluster or JSON string contains an invalid number of elements. Note When strict validation is enabled, the number of elements in the JSON string must match the number of elements in the input cluster. | N/A |
| 375005 | Type mismatch between JSON and G Web Development Software. | N/A |
| 375004 | The path cannot be found in the JSON string. | N/A |
| 375003 | The JSON string is invalid. Note JSON strings must be encoded in UTF-8 and must conform to the JSON grammar. | N/A |
| 375002 | The cluster element name is invalid.Note Each element of the cluster must have either a unique name or no name, such as an empty string. | N/A |
| 375001 | The JSON root container must be an array or cluster. | N/A |
| 375000 | The data type cannot be converted to or from JSON. Supported data types include arrays and clusters of booleans, numerics, strings, and other arrays and clusters. | N/A |
| 4824 | Clipped Floating-point data to fit the range [-1.0, 1.0]. | N/A |
| 4820 | A buffer underflow has occurred because the application is not writing data quickly enough. | N/A |
| 1 | An input parameter is invalid.For example if the input is a path, the path might contain a character not allowed by the OS such as ? or @. If you receive this error while developing a large application or storing large sets of data in G Web Development Software, refer to the KnowledgeBase at ni.com for more information. | N/A |
| 2 | Memory is full.If you receive this error while developing a large application or storing large sets of data in G Web Development Software, refer to the KnowledgeBase at ni.com for more information. | N/A |
| 4 | End of file encountered. | N/A |
| 5 | File already open. | N/A |
| 6 | Generic file I/O error.A possible cause for this error is the disk or hard drive to which you are trying to save might be full. Another possible cause for this error is there might be a bad network connection. For example, the network connection is down or a network cable is unplugged. | (If applicable) Free up disk space or saving to a different disk or drive. |
| 7 | File not found. The file might be in a different location or deleted. Another possible cause for this error is there might be a bad network connection. For example, the network connection is down or a network cable is unplugged. | (If applicable) Use the command prompt or the file explorer to verify that the path is correct. |
| 8 | File permission error. You do not have the correct permissions for the file. | Verify that the file is not in use by another application and that file permissions are set correctly. On Windows, navigate to the file, right-click the file, select Properties, and set the Read-only option in the dialog box. On Linux or Mac OS X, use chmod to set file permissions. If you only need read access, you can use the Open/Create/Replace File function with the access input set to Read-only. |
| 9 | Disk full. The disk or hard drive does not have enough free space to complete the operation. | Free up disk space or saving to a different disk or drive. |
| 10 | Duplicate path.If you receive this error while building an application in G Web Development Software, refer to the KnowledgeBase at ni.com for more information.If you receive this error while using a File I/O function or VI, you may be attempting to overwrite a file or folder that already exists. | Refer to the specific function or VI reference topic in the G Web Development Software API Manual for information about overwriting files or folders. |
| 11 | Too many files open. | N/A |
| 50 | Message out of range. | N/A |
| 51 | Null method. | N/A |
| 52 | Unknown message. | N/A |
| 67 | Interapplication Manager initialization error. | N/A |
| 68 | Bad occurrence. | N/A |
| 69 | Handler does not know what occurrence to wait for. | N/A |
| 70 | Occurrence queue overflow. | N/A |
| 71 | File datalog type conflict. | N/A |
| 72 | Semaphore not signaled. | N/A |
| 73 | Interapplication Manager unrecognized type error. | N/A |
| 74 | Memory or data structure corrupt. | N/A |
| 81 | Format specifier type mismatch. A format specifier does not match the data type of its corresponding argument in a Format Into String or Scan From String function. | N/A |
| 82 | Unknown format specifier. A bad format specifier was found in the Format String input to a Format Into String or Scan From String function. | N/A |
| 83 | Too few format specifiers. There are not enough format specifiers to match all of the arguments of a Format Into String or Scan From String function. | N/A |
| 84 | Too many format specifiers. There are more format specifiers than the number of arguments of a Format Into String or Scan From String function. | N/A |
| 85 | Scan failed.The input string does not contain data in the expected format. The Scan From String function was unable to scan its input because the data was not in the expected format.Another possible cause for this error is if the Scan From File or Scan From String functions reach the end of the file. | Right-click the Scan From String function and select Edit Format String to configure the format string to match the input data.Refer to the KnowledgeBase at ni.com for more information about this use case. |
| 87 | Error converting to variant. An error occurred converting from G Web Development Software type to OLE variant type. | N/A |
| 100 | File contains erroneous data. This normally is a user data file. | N/A |
| 116 | Unflatten or byte stream read operation failed due to corrupt, unexpected, or truncated data. | N/A |
| 117 | Directory path supplied where a file path is required. | Provide a file path where required. |
| 118 | The supplied folder path does not exist. | N/A |
| 122 | The resource you are attempting to open was created in a more recent version of G Web Development Software and is incompatible with this version. | N/A |
| 123 | A timeout occurred. | N/A |
| 124 | A string contained an unexpected null character. | N/A |
| 125 | A stack overflow occurred. | Restart G Web Development Software and review your code for recursive data structures. |
| 1000 | The VI is not in a state compatible with this operation. This error can occur for several reasons.This error can occur if you attempt to edit a VI that is running or reserved for running.This error also can occur if you attempt to open a reference to a VI that is running or reserved for running. A VI is reserved for running when you open a reference to the VI by wiring a type specifier VI Refnum to the Open VI Reference function, or when you have a Static VI Reference linked to the VI within a running VI.This error also can occur if you try to run a VI using the run method while the target VI is running or reserved for running.This error also can occur if you attempt to obtain a VI's image while the VI is being modified programmatically. | (If applicable) To correct this error, ensure the target VI is idle or reentrant. If the VI is reentrant: Use the Open VI Reference function with the options input set to 0x08 to prepare the VI for reentrant run. Use the Open VI Reference function with the type specifier VI Refnum wired to a strictly typed VI reference. (If applicable) Wait until the VI is not being modified to get the image of a panel or diagram. |
| 1001 | The VI front panel is not open. | Use the Window Appearance page to configure if the front panel is shown when the VI is run or loaded. Use the Front Panel:Open method to open the front panel programmatically. |
| 1002 | The VI cannot run because it has a front panel control in an error state. | N/A |
| 1003 | The VI is not executable. This error may occur because the VI is either broken or contains a subVI that G Web Development Software cannot locate. | Select File » Open to open the VI and verify that you can run it.Refer to the KnowledgeBase at ni.com if you receive this error in one of the following situations: while using the VI Server to call a VI dynamically or while building an application. |
| 1004 | The VI is not in memory. | N/A |
| 1005 | VI execution has been disabled in the VI Properties dialog box. | Open the Execution page of the VI Properties dialog box to change the settings for the VI execution. |
| 1006 | FPDCO on connector pane thinks it is constant. | N/A |
| 1008 | Cannot load connector pane. | N/A |
| 1009 | Variant tag out of range. | N/A |
| 1010 | No default or operate data. | N/A |
| 1012 | Cannot load block diagram. | N/A |
| 1013 | Cannot load front panel. | Ensure you included the front panel of the VI when building a stand-alone application. |
| 1016 | Cannot load History. | N/A |
| 1017 | VI has been modified on disk since it was last loaded or saved. | N/A |
| 1018 | Unspecified error occurred. | N/A |
| 1019 | One or more untitled subVIs exist. This file cannot be saved until all dependent files have been named. | N/A |
| 1026 | VI Reference is invalid. | N/A |
| 1027 | The reference cannot be reserved as requested because it is in an improper reservation mode or the execution state must be set to running or reserved. | N/A |
| 1028 | Attribute selector is invalid. | N/A |
| 1039 | VI was aborted. | N/A |
| 1042 | Attempted recursive call. | N/A |
| 1043 | The property or method is not supported in this version of G Web Development Software.This error can occur if you use a property or method that is not supported in the G Web Development Software Run-Time Engine. | N/A |
| 1102 | The string wired to the xml string input is empty. | N/A |
| 1103 | The XML tag describing the type of data is not recognized. | N/A |
| 1104 | No end tag was found for an XML start/end tag pair. | N/A |
| 1105 | An unknown or unexpected XML tag was discovered. | N/A |
| 1106 | The XML tag describing the type of data does not match the wired type. | N/A |
| 1107 | The XML enumerated type choice(s) does not match the wired type. | N/A |
| 1108 | XML value text is illegal or out of range for type and/or format. | N/A |
| 1109 | Unsupported data type. | N/A |
| 1110 | No longer used. | N/A |
| 1122 | Refnum became invalid while node waited for it. | N/A |
| 1124 | VI is not loadable.In a built application, this error might occur because the VI being loaded was last compiled for a different OS or with CPU features, such as SSE, that this target does not support.This error also might occur if the VI is a polymorphic VI that cannot be loaded in the G Web Development Software Run-Time Engine. | (If applicable) Rebuild the application for the target OS and make sure SSE compiler settings in the build specifications match the target platform.(If applicable) Load an instance of the polymorphic VI instead of the polymorphic VI itself. |
| 1129 | You cannot assign the same numeric value to two or more strings in a ring control. You also cannot assign the same string value to two or more strings in a combo box control. | If you receive this error while trying to write to the Strings and Values property of a control, refer to the KnowledgeBase at ni.com for more information. |
| 1135 | The tree control's active item is not valid for this property. | N/A |
| 1136 | You wired an invalid item tag to a tree control property or method. | N/A |
| 1137 | Tree control's internal data is corrupt. | N/A |
| 1146 | You attempted an operation that would change a child-only item into a parent item. | N/A |
| 1147 | Cannot insert a remote VI in a subpanel control. | N/A |
| 1148 | This property is read only while the VI is in a subpanel. | N/A |
| 1149 | Cannot close or set the state of a closed front panel. The front panel must already be open before you close it or set its state. | N/A |
| 1150 | Cannot open a front panel that is already open. Set the state of the open front panel by using the Front Panel Window:State property. | N/A |
| 1151 | Invalid input for front panel state. | N/A |
| 1156 | Memory full error, possibly due to a data format not matching expected data type. This is caused by trying to allocate a buffer that is too large for memory. Although normal allocation might run the system out of memory, frequently an out of memory error is caused by interpreting the data incorrectly and treating something that is data as the size of the data. | Before assuming that the system needs more memory to complete the operation, make sure the read format you are requesting is valid for the data being read. |
| 1157 | You cannot use this property with a numeric indicator. | N/A |
| 1186 | Cannot show or hide the label on its own. Label visibility is controlled by the label owner. | N/A |
| 1192 | No data range set for digital displays. | N/A |
| 1301 | The dimension of the array passed in does not match the expected dimension for the operation. | N/A |
| 1303 | The elements of the array are not unique. There are duplicated items in the array. | N/A |
| 1304 | The array index is outside of the array bounds. | N/A |
| 1313 | You cannot use this property on a control in a radio buttons control. | N/A |
| 1321 | NI License Manager is not initialized. | Verify that NI License Manager is installed on the computer. Select Start » All Programs » National Instruments » NI License Manager. |
| 1322 | Invalid project build reference. | N/A |
| 1359 | A drag cannot start because a previous drag transaction is still pending. | N/A |
| 1360 | Cannot provide the type of data requested for this drag and drop operation. | Ensure that a drag and drop operation is in progress when you call this function and that the data type and drag data name match what is currently available during the drag and drop operation. |
| 1362 | Cannot use this property with this string display mode or if word wrapping is enabled. | Change the display mode to 0 (normal) and/or disable word wrapping to use this property. |
| 1366 | You cannot hide or show the scroll bars of a subpanel control when a VI containing multiple panels is inserted. | N/A |
| 1370 | The selected build failed to complete. | N/A |
| 1376 | A Diagram Disable structure cannot have a default frame. This error occurs when you try to use the Default Frame property with a Diagram Disable structure. You can use this property only with the Conditional Disable structure. | N/A |
| 1377 | A Diagram Disable Structure cannot have conditions. You can use the Conditions property and the Get Frame Index method only with the Conditional Disable structure. | N/A |
| 1378 | Cannot set the Active Frame property on a Conditional Disable structure. This error occurs when you try to use the Active Frame property with a Conditional Disable structure. You cannot use this property with a Conditional Disable structure because conditions determine the active frame. You can use this property only with a Diagram Disable structure. | N/A |
| 1380 | License checkout failure. Unable to checkout the requested license feature because the license is invalid or does not exist. | N/A |
| 1397 | You have not wired a required input on this subVI. | Wire the required input. |
| 1430 | The path is empty or relative. You must use an absolute path. | N/A |
| 1432 | The specified format cannot be used with floating point data. For example, hexadecimal notation is not a valid format for floating point numbers. | N/A |
| 1434 | The precision is greater than the maximum allowed value for this format. | N/A |
| 1436 | Numeric precision cannot be negative. | N/A |
| 1449 | Arrays must have at least one dimension and a maximum of 63 dimensions. | N/A |
| 1452 | This library was saved in an earlier version of G Web Development Software. | Load and save the library in the latest version of G Web Development Software. |
| 1453 | You may only set the vertical arrangement on a label, caption or free label. | N/A |
| 1470 | Specified folder is outside the library. You cannot add library items to folders that do not belong to the library. | N/A |
| 1483 | Cannot change width of the plot legend when you configure the plot legend to automatically resize, or if the legend has more than one entry and you arrange the plot legend horizontally. | Right-click the graph or chart and deselect Autosize Plot Legend in the shortcut menu to disable automatic resizing and make sure you arrange the plot legend vertically. |
| 1546 | The VI must be in a project to use this property. | N/A |
| 1548 | Queue refnum cannot be obtained with a size of zero. Size input must be a positive number or -1 for unlimited size. | N/A |
| 1556 | The reference is invalid. This error might occur because the reference has been deleted. | N/A |
| 1557 | G Web Development Software tried to access duplicate references at the same time. | N/A |
| 1558 | There is a type mismatch between the wire type and the internal data type of the reference. This problem might occur due to a type cast error. | N/A |
| 1586 | Compiled code is out of date. | N/A |
| 1588 | Compiled object cache is corrupt. | N/A |
| 1599 | An empty string is not a valid method name. | N/A |
| 1627 | The control index at position %d is invalid. | N/A |
| 1628 | G Web Development Software cannot convert the input data type at position %d to the control data type. | N/A |
| 1629 | The control must have a terminal on the block diagram. | N/A |

Parent topic:

Testing and Debugging

<!--NI_TOPIC bundle=g-web-development path=error-messages-api.html language=enus -->
## TOPIC 00157: Error Message Design for Distributed APIs

- bundle_id: `g-web-development`
- source_path: `error-messages-api.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/error-messages-api.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Refer to the following table for best practices for designing error messages. Guideline Required or Recommended? Details Reserve a range of error codes for your API and use those codes for error conditions specific to your API. Required Pick a range for error codes between -8999 through -8000, 5000

### Error Message Design for Distributed APIs

Refer to the following table for best practices for designing error messages.

| Guideline | Required or Recommended? | Details |
| --- | --- | --- |
| Reserve a range of error codes for your API and use those codes for error conditions specific to your API. | Required | Pick a range for error codes between -8999 through -8000, 5000 through 9999, and 500,000 through 599,999, which are reserved for external users. |
| When generating or manipulating errors on the diagram of your API VIs, make sure you use the Error API to construct and manipulate error clusters. | Required | Never bundle or unbundle error cluster elements directly in G Web Development Software. |
| If the VI has no way to generate errors, consider excluding error inputs and outputs. | Recommended | If a VI does not generate errors, users of the VI can take advantage of parallelism in G Web Development Software. |
| If you exclude error inputs and outputs on a VI in your API, leave the error input and output locations on the connector pane empty. | Recommended | When unused error inputs and outputs on a VI are left empty, you can add error handling to the VI later. |

Parent topic:

Best Practices for Designing and Developing an Application Programming Interface (API) in G Web Development Software

Parent topic:

Best Practices for Designing and Developing an Application Programming Interface (API) in G Web Development Software

Related concepts:

- Best Practices for Designing and Developing an Application Programming Interface (API) in G Web Development Software

<!--NI_TOPIC bundle=g-web-development path=error.html language=enus -->
## TOPIC 00158: Error

- bundle_id: `g-web-development`
- source_path: `error.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/error.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Add an error data type symbol to the icon.

### Error

Add an error data type symbol to the icon.

Parent topic:

Data Types Palette

<!--NI_TOPIC bundle=g-web-development path=escape-sequences.html language=enus -->
## TOPIC 00159: Escape Sequences

- bundle_id: `g-web-development`
- source_path: `escape-sequences.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/escape-sequences.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: The following table lists allowable escape sequences for character representations. Escaping characters using hex codes is not supported. Escape Sequence Character Represented \b Backspace \f Form feed \n Newline or line feed \r Carriage return \s Space \t Tab \\ Backslash Use escape sequences to su

### Escape Sequences

The following table lists allowable escape sequences for character representations. Escaping characters using hex codes is not supported.

| Escape Sequence | Character Represented |
| --- | --- |
| \\b | Backspace |
| \\f | Form feed |
| \\n | Newline or line feed |
| \\r | Carriage return |
| \\s | Space |
| \\t | Tab |
| \\\\ | Backslash |

Use escape sequences to substitute for reserved characters in string terminals and string constants. On the 
 Item tab, toggle the 
 Show escape sequences checkbox to display escape sequences or character representations.

Parent topic:

Text Controls

Parent topic:

Text Controls

<!--NI_TOPIC bundle=g-web-development path=event-driven-programming.html language=enus -->
## TOPIC 00160: Event-Driven Programming

- bundle_id: `g-web-development`
- source_path: `event-driven-programming.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/event-driven-programming.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `concept`
- source_description: Event-driven programming is a programming pattern in which you create diagram code that executes outside the dataflow structure as a result of an event occurring. Use event-driven programming when you want diagram code to execute in response to an event. An event is anything that happens to the user

### Event-Driven Programming

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

<!--NI_TOPIC bundle=g-web-development path=event-sources.html language=enus -->
## TOPIC 00161: Event Sources

- bundle_id: `g-web-development`
- source_path: `event-sources.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/event-sources.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can configure the Event Structure to handle events from any supported source. User Interface—mouse clicks, key presses, and so on. Programmatically generated events—events triggered by diagram code, without any user interaction. Each event is associated with a control on the panel of the VI, the

### Event Sources

You can configure the Event Structure to handle events from any supported source.

- User Interface—mouse clicks, key presses, and so on.
- Programmatically generated events—events triggered by diagram code, without any user interaction.

Note

Parent topic:

Event-Driven Programming

<!--NI_TOPIC bundle=g-web-development path=execute-code-based-on-event.html language=enus -->
## TOPIC 00162: Executing Code Based on an Event

- bundle_id: `g-web-development`
- source_path: `execute-code-based-on-event.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/execute-code-based-on-event.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `task`
- source_description: To execute code based on an event, you must configure the Event Structure to handle events. Before you configure events for the Event Structure to handle, review Recommendations for Event-Driven Programming. Complete the following steps to configure an Event Structure case to handle events. (Optiona

### Executing Code Based on an Event

To execute code based on an event, you must configure the Event Structure to handle events.

Event Structure

Recommendations for Event-Driven
 Programming

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

Related reference:

- Recommendations for Event-Driven Programming

<!--NI_TOPIC bundle=g-web-development path=execute-code-based-on-user-event.html language=enus -->
## TOPIC 00163: Executing Code Based on a User Event

- bundle_id: `g-web-development`
- source_path: `execute-code-based-on-user-event.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/execute-code-based-on-user-event.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `task`
- source_description: User events are defined on the diagram and triggered by the execution of diagram code. Unlike user interface events, which require direct user interaction with front panel objects, user events allow you to create an application that responds to programmatic changes on objects. Additionally, you can

### Executing Code Based on a User Event

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

[IMAGE alt='image' src='GUID-E57D381F-69AB-4633-86F5-8FA2F454E088-a5.png']

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

Related information:

- Create User Event
- Register for Events
- Event Loop
- Generate User Event
- Unregister for Events
- Destroy User Event

<!--NI_TOPIC bundle=g-web-development path=executing-code-based-condition.html language=enus -->
## TOPIC 00164: Executing Code Based on a Condition

- bundle_id: `g-web-development`
- source_path: `executing-code-based-condition.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/executing-code-based-condition.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `task`
- source_description: Use a Case Structure to incorporate decision logic into your program. A Case Structure contains one or more subdiagrams, or cases, exactly one of which executes when the structure executes.Case Structures behave similarly to switch statements or if-then-else statements in other programming languages

### Executing
 Code Based on a Condition

Case Structure

Case Structure

Case Structures

switch

if-then-else

#### What to Use

- Case Structure Tip If you are choosing
 between only two values based on a Boolean input, you can use the
 Select node instead of a Case Structure with a
 Boolean selector.

#### What to Do

Create the following diagram to execute different code based on a given condition.

Customize the gray sections for your unique programming goals.

[IMAGE alt='image' src='GUID-2C5E960D-D338-48FF-949E-254D93136D34-a5.png']

[IMAGE alt='image' src='GUID-B2DAE4FD-3F00-4CC7-BAEB-2561341C11DF-a5.png']

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

Related information:

- Case Structure
- Select

<!--NI_TOPIC bundle=g-web-development path=execution-logs.html language=enus -->
## TOPIC 00165: Improve Applications with Execution Logs

- bundle_id: `g-web-development`
- source_path: `execution-logs.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/execution-logs.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `concept`
- source_description: Well-written applications use execution logs for both activity audit and monitoring. An execution log makes it easy for a developer or user to track and identify issues that occur throughout the application without excessive effort.Maintaining an execution log allows you to review all activity and m

### Improve Applications with Execution Logs

Well-written applications use execution logs for both activity audit and monitoring. An execution log makes it easy for a developer or user to track and identify issues that occur throughout the application without excessive effort.Maintaining an execution log allows you to review all activity and make improvements to your application accordingly.

An application should record data from multiple execution points throughout
 an application—errors, exceptions, successful execution, and so on. An execution log can
 help you recreate a certain behavior and improve your application effectively. For example,
 you can use the log to do one or more of the following:

- Modify the code to be able to handle a
 situation that caused an error
- Modify the code based on the most common use
 case
- Update the documentation for the application so
 that users interact with the application in a more predictable way
- Validate successful execution

The execution log should include as much information as you need to understand
 the state of the product at the time the data was collected.

- The current time and date
- A pre-defined category for the activity
- A running count of the specific type of
 activity
- A description of the activity
- The value of data that was generated during or
 prior to the activity
- The location of the activity within the
 application
- The type and severity of the problem, if there
 is one

Parent topic:

Testing and Debugging

<!--NI_TOPIC bundle=g-web-development path=file-organization-api.html language=enus -->
## TOPIC 00166: File Organization and Node Naming for Distributed APIs

- bundle_id: `g-web-development`
- source_path: `file-organization-api.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/file-organization-api.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Refer to the following table for best practices for organizing files and naming nodes. Guideline Required or Recommended? Details Example(s) Use title case. Required Capitalize the following in subVI names: The first and the last word All nouns, pronouns, adjectives, verbs, adverbs, and subordinate

### File Organization and Node Naming for Distributed APIs

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
| Make sure none of the nodes or VIs in your API share the same name with a node or VI that is already in the G Web Development Software palettes. | Required | Unique node and VI names in an API make unique palette object names for Quick Drop users. | N/A |
| Do not use the forbidden word, Example, in the names of your API nodes or VIs. | Required | N/A | N/A |

Parent topic:

Best Practices for Designing and Developing an Application Programming Interface (API) in G Web Development Software

<!--NI_TOPIC bundle=g-web-development path=file-prog-org-lv.html language=enus -->
## TOPIC 00167: File and Project Organization in G Web Development Software

- bundle_id: `g-web-development`
- source_path: `file-prog-org-lv.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/file-prog-org-lv.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Refer to the following table for best practices for organizing files and projects in G Web Development Software. Guideline Required or Recommended? Details Example(s) Avoid using special characters in file names. Recommended Using special characters in file names can cause compatibility concerns acr

### File and Project Organization in G Web
 Development Software

Refer to the following table for best practices for organizing files and projects in G
 Web Development Software.

| Guideline | Required or Recommended? | Details | Example(s) |
| --- | --- | --- | --- |
| Avoid using special characters in file names. | Recommended | Using special characters in file names can cause compatibility concerns across platforms. | Avoid the following: File separators such as colons, forward slashes, and backward slashes Non-alphabetical and non-numerical symbols, such as the trademark symbol Punctuation marks, such as parentheses, quotation marks, brackets, and operators White space characters, such as tabs and new lines Note You can use spaces for most applications, but avoid using spaces in a top-level .gviweb to create a human-readable URL. |
| Make sure your project organization is logical and easy to use. | Recommended | Create a hierarchical structure with easily accessible top-level VIs. Place support VIs in folders within the project and group them to reflect modular components, such as instrument drivers, other drivers, and configuration utilities. Limit the number and the levels of directories you use in a project. | N/A |

Parent topic:

Best Practices for Creating Projects in G Web Development Software

<!--NI_TOPIC bundle=g-web-development path=file-type.html language=enus -->
## TOPIC 00168: File Type

- bundle_id: `g-web-development`
- source_path: `file-type.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/file-type.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Set the file type(s) you can select with the path control.

### File Type

Set the file type(s) you can select with the path control.

Parent topic:

Creating User Interfaces

<!--NI_TOPIC bundle=g-web-development path=filename.html language=enus -->
## TOPIC 00169: Filename

- bundle_id: `g-web-development`
- source_path: `filename.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/filename.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates standard text to represent a filename.

### Filename

Creates standard text to represent a filename.

Parent topic:

Creating User Interfaces

<!--NI_TOPIC bundle=g-web-development path=filter-icon-editor.html language=enus -->
## TOPIC 00170: Filter

- bundle_id: `g-web-development`
- source_path: `filter-icon-editor.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/filter-icon-editor.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Add a filter symbol to the icon.

### Filter

Add a filter symbol to the icon.

Parent topic:

Objects Palette

<!--NI_TOPIC bundle=g-web-development path=flatten-icon-editor.html language=enus -->
## TOPIC 00171: Flatten

- bundle_id: `g-web-development`
- source_path: `flatten-icon-editor.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/flatten-icon-editor.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Add a flatten symbol to the icon.

### Flatten

Add a flatten symbol to the icon.

Parent topic:

Actions Palette

<!--NI_TOPIC bundle=g-web-development path=font-size.html language=enus -->
## TOPIC 00172: Font Size

- bundle_id: `g-web-development`
- source_path: `font-size.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/font-size.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Set the font size.

### Font Size

Set the font size.

Parent topic:

Creating User Interfaces

<!--NI_TOPIC bundle=g-web-development path=font.html language=enus -->
## TOPIC 00173: Font Family

- bundle_id: `g-web-development`
- source_path: `font.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/font.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Select the font face.

### Font Family

Select the font face.

Parent topic:

Creating User Interfaces

<!--NI_TOPIC bundle=g-web-development path=for-loops-repeating-operations-set-number-of-times.html language=enus -->
## TOPIC 00174: Repeating Operations a Set Number of Times

- bundle_id: `g-web-development`
- source_path: `for-loops-repeating-operations-set-number-of-times.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/for-loops-repeating-operations-set-number-of-times.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `task`
- source_description: Instead of creating the same code on a diagram multiple times, you can write code in a single location and use a For Loop to programmatically repeat it. For example, you might want to read a specific number of measurement samples from a device. You can place the code that performs the measurement op

### Repeating Operations a Set Number of Times

Instead of creating the same code on a diagram multiple times, you can write code in a single location and use a For Loop to programmatically repeat it. For example, you might want to read a specific number of measurement samples from a device. You can place the code that performs the measurement operation on the subdiagram of a For Loop and configure the loop to repeat the operation as many times as your application requires.

#### What to Use

- For Loop
- Count terminal of the For
 Loop

#### What to Do

Create the following diagram to repeat an operation a set number of times.

Customize the gray sections for your unique programming goals.

[IMAGE alt='image' src='GUID-5104BCE3-FA5B-4A67-AA56-BAB601CBE542-a5.png']

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

Related information:

- For Loop

<!--NI_TOPIC bundle=g-web-development path=fpga-large-icon-editor.html language=enus -->
## TOPIC 00175: FPGA (large)

- bundle_id: `g-web-development`
- source_path: `fpga-large-icon-editor.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/fpga-large-icon-editor.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Add a large FPGA symbol to the icon.

### FPGA (large)

Add a large FPGA symbol to the icon.

Parent topic:

Objects Palette

<!--NI_TOPIC bundle=g-web-development path=fpga-small-icon-editor.html language=enus -->
## TOPIC 00176: FPGA (small)

- bundle_id: `g-web-development`
- source_path: `fpga-small-icon-editor.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/fpga-small-icon-editor.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Add a small FPGA symbol to the icon.

### FPGA (small)

Add a small FPGA symbol to the icon.

Parent topic:

Objects Palette

<!--NI_TOPIC bundle=g-web-development path=fractional-digits.html language=enus -->
## TOPIC 00177: Fractional Digits

- bundle_id: `g-web-development`
- source_path: `fractional-digits.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/fractional-digits.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Set the number of digits to the right of the decimal point; sets the precision of the control display.

### Fractional Digits

Set the number of digits to the right of the decimal point; sets the precision of the control display.

Parent topic:

Creating User Interfaces

<!--NI_TOPIC bundle=g-web-development path=g-object-control.html language=enus -->
## TOPIC 00178: G Object Control

- bundle_id: `g-web-development`
- source_path: `g-object-control.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/g-object-control.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: A control or indicator of the common parent of all classes in the G Dataflow inheritance hierarchy.

### G Object Control

A control or indicator of the common parent of all classes in the G Dataflow inheritance hierarchy.

Parent topic:

Creating User Interfaces

<!--NI_TOPIC bundle=g-web-development path=g-types.html language=enus -->
## TOPIC 00179: Type Definitions

- bundle_id: `g-web-development`
- source_path: `g-types.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/g-types.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `concept`
- source_description: Type definitions are custom data types that you define using the G language and can reuse throughout your project. You define a type definition in a G Type document.

### Type Definitions

*Type definitions* are custom data types that you define using the G
 language and can reuse throughout your project.

You define a type definition in a G Type document.

Parent topic:

Data Type Reference

Related tasks:

- Creating a Custom Data Type Using a G Type Document
- Updating Custom Data Type Instances Throughout Your Project

<!--NI_TOPIC bundle=g-web-development path=gauge.html language=enus -->
## TOPIC 00180: Gauge

- bundle_id: `g-web-development`
- source_path: `gauge.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/gauge.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Enter or display numeric data in a rotary scale.

### Gauge

Enter or display numeric data in a rotary scale.

Parent topic:

Creating User Interfaces

<!--NI_TOPIC bundle=g-web-development path=general-user-interface-event-reference.html language=enus -->
## TOPIC 00181: General User Interface Event Reference

- bundle_id: `g-web-development`
- source_path: `general-user-interface-event-reference.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/general-user-interface-event-reference.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: The following events occur when the user performs an action that involves the panel or any control on the panel. Event Description Event Data Fields Value Changed Generated when the user changes the value of a control. You must read the terminal of a latched Boolean control in its Value Change event

### General User Interface Event
 Reference

The following events occur when the user performs an action that involves the panel or any control on the panel.

| Event | Description | Event Data Fields |
| --- | --- | --- |
| Value Changed | Generated when the user changes the value of a control. You must read the terminal of a latched Boolean control in its Value Change event case. | Index—Index of the event source within an individual event diagram. Time—Value of the millisecond timer when the event occurred. Control Reference—Reference to the control on which the event occurred. Old Value—Value of the control before the data change. New Value—Value of the control after the data change. |

Parent topic:

User Interface Events

<!--NI_TOPIC bundle=g-web-development path=generate-icon-editor.html language=enus -->
## TOPIC 00182: Generate

- bundle_id: `g-web-development`
- source_path: `generate-icon-editor.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/generate-icon-editor.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Add a generate symbol to the icon.

### Generate

Add a generate symbol to the icon.

Parent topic:

Actions Palette

<!--NI_TOPIC bundle=g-web-development path=graph-control.html language=enus -->
## TOPIC 00183: Graph Control

- bundle_id: `g-web-development`
- source_path: `graph-control.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/graph-control.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Plot numeric, complex, X/Y, or point sample data contained in arrays and analog waveforms. What Types of Data Can I Plot? You can plot numeric, complex, or point sample data contained in arrays and analog waveforms. By default, the graph data type is an array of doubles. You can change the data type

### Graph Control

Plot numeric, complex, X/Y, or point sample data contained in arrays and analog waveforms.

[IMAGE alt='image' src='GUID-CF2EAC4E-EA4D-4A61-B7BB-E209E72CF813-a5.png']

#### What Types of Data Can I Plot?

You can plot numeric, complex, or point sample data contained in arrays and analog waveforms. By default, the graph data type is an array of doubles. You can change the data type on the diagram.

The waveform data type carries the start time (t0), delta t (dt), and y-values (Y) of a waveform. When you wire waveform data to a graph, the graph automatically plots a waveform based on the start time, delta t, and y-values of the waveform.

For data contained in arrays, the graph displays a general-purpose Cartesian graph that plots any set of points, evenly sampled or not.

The following table describes how graphs plot different types of array data.

| Data Type | Plot Behavior |
| --- | --- |
| 1D array of numeric values | The array is a single plot. X-value: Array index Y-value: Array element |
| 1D array of complex or cluster values | The array is a single plot. The cluster must be a two-element cluster. X-value: First element of the complex number or cluster Y-value: Second element of the complex number or cluster |
| Cluster of two 1D arrays of numeric values | The cluster is a single plot. X-value: Elements of the first array Y-value: Elements of the second array |
| 1D array of waveforms | Each waveform is a separate plot. |
| 2D array of numeric values | Each row of the array is a separate plot. |
| 2D array of complex or cluster values | Each row of the array is a separate plot. The cluster must be a two-element cluster.X-value: First element of the complex number or clusterY-value: Second element of the complex number or cluster |
| 1D array of clusters of 1D arrays | Each cluster of arrays is a separate plot. Arrays within a cluster must be the same size, but arrays in different clusters can be different sizes. |
| Cluster of two numeric values and a 1D array | The cluster is a single plot.X-value: An initial x value incremented by a delta x. The first numeric value represents the initial x value, and the second numeric value represents the delta x valueY-value: Elements of the arrayThis data type is not supported. |

Parent topic:

Charts and Graphs

<!--NI_TOPIC bundle=g-web-development path=graph-tools.html language=enus -->
## TOPIC 00184: Graph Tools

- bundle_id: `g-web-development`
- source_path: `graph-tools.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/graph-tools.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Move the cursor and zoom and pan the graph or chart while a VI runs.

### Graph Tools

Move the cursor and zoom and pan the graph or chart while a VI runs.

Parent topic:

Creating User Interfaces

<!--NI_TOPIC bundle=g-web-development path=grow-time.html language=enus -->
## TOPIC 00185: Grow Time

- bundle_id: `g-web-development`
- source_path: `grow-time.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/grow-time.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configure the rate at which the bubbles grow.

### Grow Time

Configure the rate at which the bubbles grow.

Parent topic:

Creating User Interfaces

<!--NI_TOPIC bundle=g-web-development path=gslv.html language=enus -->
## TOPIC 00186: Getting Started with G Web Development Software

- bundle_id: `g-web-development`
- source_path: `gslv.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/gslv.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use G Web Development Software to create browser-based user interfaces to visualize data from distributed systems. The Projects tab appears when you launch G Web Development Software. Select either the Projects or Learning tab to get started. From the Projects tab you can: Create a new blank web app

### Getting Started with G Web Development
 Software

Use G Web Development Software to create browser-based user interfaces to visualize
 data from distributed systems. The Projects tab appears when you launch G
 Web Development Software. Select either the Projects or
 Learning tab to get started.

Projects

- Create a new blank web application project.
- Create a new web application project based on a template.
- Open a recent project.
- Access help documentation from the right panel to learn more
 about G Web Development Software.

The Projects tab will close once you make your selection. You can
 access it again by clicking Home in the upper-left corner of the
 document.

Parent topic:

G Web Development Software

<!--NI_TOPIC bundle=g-web-development path=handshake-icon-editor.html language=enus -->
## TOPIC 00187: Handshake

- bundle_id: `g-web-development`
- source_path: `handshake-icon-editor.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/handshake-icon-editor.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Add a handshake symbol to the icon.

### Handshake

Add a handshake symbol to the icon.

Parent topic:

Objects Palette

<!--NI_TOPIC bundle=g-web-development path=hardware-web-application.html language=enus -->
## TOPIC 00188: Using Hardware with a Web Application

- bundle_id: `g-web-development`
- source_path: `hardware-web-application.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/hardware-web-application.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use a web application to share measurement data and interact with hardware. The following diagrams show three architectures for how to use your hardware with a web application. Use the diagrams to choose the best architecture for your application.You can use both real-time and non-real-time hardware

### Using Hardware with a Web Application

Use a web application to share measurement data and interact with hardware.

Note

#### Access a Web Application on Your Hardware

[IMAGE alt='image' src='GUID-F4A13401-4187-4341-A5CF-09BECC1D767B-a5.png']

Note

#### Access a Web Application on a PC

[IMAGE alt='image' src='GUID-B5D454A2-29DB-4B6F-93C4-F77F926E6AD3-a5.png']

In this architecture, the web service runs and web application is stored on a PC on the
 same network as your hardware. This architecture keeps the server burden off of your
 hardware and works best for sharing measurement data in web applications using SystemLink
 Tag and Message APIs.

#### Access a Web Application on the Cloud

[IMAGE alt='image' src='GUID-5E451FC2-45CC-4DE3-9EA6-6CD97D172086-a5.png']

In this architecture, your hardware shares data with the web application hosted in the
 cloud. This architecture works best for accessing the web application from a desktop or
 mobile device over the internet to securely share your measurement data.

Parent topic:

G Web Development Software

Parent topic:

G Web Development Software Manual

<!--NI_TOPIC bundle=g-web-development path=hexagon-icon-editor.html language=enus -->
## TOPIC 00189: Hexagon

- bundle_id: `g-web-development`
- source_path: `hexagon-icon-editor.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/hexagon-icon-editor.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Create a customizable hexagon.

### Hexagon

Create a customizable hexagon.

Parent topic:

Shapes Palette

<!--NI_TOPIC bundle=g-web-development path=history.html language=enus -->
## TOPIC 00190: History

- bundle_id: `g-web-development`
- source_path: `history.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/history.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configure the size of the chart history buffer.

### History

Configure the size of the chart history buffer.

Parent topic:

Creating User Interfaces

<!--NI_TOPIC bundle=g-web-development path=horizontal-slider.html language=enus -->
## TOPIC 00191: Horizontal Slider

- bundle_id: `g-web-development`
- source_path: `horizontal-slider.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/horizontal-slider.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Enter or display numeric data in a horizontal slider.

### Horizontal Slider

Enter or display numeric data in a horizontal slider.

Parent topic:

Creating User Interfaces

<!--NI_TOPIC bundle=g-web-development path=host-web-app-during-dev.html language=enus -->
## TOPIC 00192: Hosting a Web Application During Development

- bundle_id: `g-web-development`
- source_path: `host-web-app-during-dev.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/host-web-app-during-dev.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `concept`
- source_description: Host WebVIs running in the G Web Development Software editor with NI Web Server or the G Web Development Software embedded web server. NI recommends hosting your WebVI with NI Web Server. NI Web Server helps you avoid additional configurations when you use other APIs NI Web Server hosts, such as Sys

### Hosting a Web Application During
 Development

Host WebVIs running in the G Web Development Software editor with NI Web Server or
 the G Web Development Software embedded web server.

NI recommends hosting your WebVI with NI Web Server. NI Web Server helps you avoid additional
 configurations when you use other APIs NI Web Server hosts, such as SystemLink Tags and
 Messages. Refer to the NI Web Server Manual for more information.

Use the G Web Development Software embedded web server if you are unable to configure NI Web
 Server on your development PC. If you choose the embedded web server, you cannot connect to
 APIs hosted on the NI Web Server, such as the SystemLink APIs, unless you configure NI Web
 Server to support the cross-origin resource sharing (CORS) mechanism. Refer to *Choosing
 Remote Settings* to learn more about enabling CORS for NI Web Server.

Note

<port>

To set your hosting preference in G Web Development Software, select File»Preferences»Web Server.

Parent topic:

Hosting a Web Application on a Server

Related concepts:

- Considerations When Accessing Data from Web Services

Related information:

- NI Web Server Manual
- Choosing Remote Settings

<!--NI_TOPIC bundle=g-web-development path=hosting-a-web-vi.html language=enus -->
## TOPIC 00193: Hosting a WebVI with the Web Applications Service

- bundle_id: `g-web-development`
- source_path: `hosting-a-web-vi.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/hosting-a-web-vi.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `task`
- source_description: Host a WebVI on the NI Web Server with the Web Applications Service to securely share it with users on the server. Before hosting a WebVI with the Web Applications Service, create a package (.nipkg) in G Web Development Software that contains the WebVI.To host a web application on an NI web server,

### Hosting a WebVI with the Web Applications
 Service

Host a WebVI on the NI Web Server with the Web Applications Service to
 securely share it with users on the server.

Note

- Index.htm
- Index.html
- Main.htm
- Main.html
- Function.htm
- Function.html

1. In the NI Web Server web application, open the navigation menu, and click
 Web Applications.
2. Click IMPORT.
3. Select the package you want to upload from your local machine.
4. Click UPLOAD. 
 Note In G Web Development Software all WebVIs are uploaded to the Default
 workspace.
5. Click the WebVI to run it.
6. To update an existing WebVI, select the WebVI and click
 Update.

Users who have WebVI permissions can
 interact with the WebVI you uploaded.

Parent topic:

Hosting a Web Application on a Server

<!--NI_TOPIC bundle=g-web-development path=hosting-g-web-server.html language=enus -->
## TOPIC 00194: Hosting a Web Application on the NI Application Web Server

- bundle_id: `g-web-development`
- source_path: `hosting-g-web-server.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/hosting-g-web-server.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `task`
- source_description: To make your web application available to other users, host your build output on a web server that is accessible to other users. Before you begin, you must complete the following tasks. Install a version of LabVIEW from 2013 or later. Build your web application. To host your web application on the A

### Hosting a Web Application on the NI
 Application Web Server

To make your web application available to other users, host your build output on a web server that is accessible to other users.

- Install a version of LabVIEW from 2013 or later.
- Build your web application.

To host your web application on the Application Web Server, choose from the following options.

| Option | Description |
| --- | --- |
| Host your web application on the Application Web Server through LabVIEW Web Services. | In your LabVIEW Web Service, create a public content folder. For more information, refer to Integrating Static Content into a Web Service. Copy your entire web application output directory into the public content folder you created. Publish your LabVIEW Web Service. Note Download the latest LabVIEW Help for the most up-to-date content. |
| Manually host your web application files on the Application Web Server. | Navigate to the Application web server document root. Example if the 32-bit Application Web Server is enabled: C:\\Program Files (x86)\\National Instruments\\Shared\\NI WebServer\\wwwExample if hosting on a CompactRIO:/var/local/natinst/www Copy your entire web application output directory into the Application web server document root. To navigate to your web application output on your machine, open your web application component and on the Document tab click the path shown under Build Information » Output directory. Open a web browser and navigate to http://localhost:8080/WebApp_Web%20Server/Main.html, where Main.html is the file name of the top-level WebVI in your web application. Note You can update the port in the URL, if necessary, to match the Application Web Server HTTP port. |

Parent topic:

Hosting a Web Application on a Server

Related information:

- Integrating Static Content into a Web Service (Real-Time, Windows)
- Publishing Web Services (Real-Time, Windows)

<!--NI_TOPIC bundle=g-web-development path=hosting-ni-web-server.html language=enus -->
## TOPIC 00195: Hosting a Web Application on the NI Web Server

- bundle_id: `g-web-development`
- source_path: `hosting-ni-web-server.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/hosting-ni-web-server.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `task`
- source_description: To make your application available to other users, host your build output on a web server that is accessible to other users. This topic demonstrates hosting WebVIs as simple static files with limited access control options. Instead it is recommended to leverage the Web Applications service for permi

### Hosting a Web Application on the NI Web
 Server

To make your application available to other users, host your build output on a web
 server that is accessible to other users.

Note

- Remove the URL, username, and password from the
 panel and the diagram to maximize the security of your web application. Refer to the
 Hosting Authentication Credentials Securely section of Security in NI Web
 Technology for more information.

NI SystemLink and G Web Development Software both use NI Web Server. Complete the
 following steps to host your web application on NI Web Server.

1. Open your web application project (.gwebproject).
2. Locate the NI Web Server root directory. 
 Open File»Preferences on the Web Server tab of the NI Web Server option
 note the root directory path. 
 Here is an example of a root directory path: C:\Program Files\National
 Instruments\Shared\Web Server\htdocs\.
3. Copy your entire web application output directory into the root directory. 
 To navigate to your web application output on your machine, open your web application
 component and on the Document tab click the path shown under Build Information»Output directory.
4. Open a web browser and navigate to
 http://localhost/WebApp_Web%20Server/Main.html,
 localhost is the IP address of the server and
 Main.html is the file name of the top-level
 WebVI in your web application.

Parent topic:

Hosting a Web Application on a Server

Related tasks:

- Hosting a WebVI with the Web Applications Service

Related information:

- Choosing Remote Settings

<!--NI_TOPIC bundle=g-web-development path=hosting-web-application-on-server.html language=enus -->
## TOPIC 00196: Hosting a Web Application on a Server

- bundle_id: `g-web-development`
- source_path: `hosting-web-application-on-server.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/hosting-web-application-on-server.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `task`
- source_description: To make your web application available to other users, host your build output on a web server that is accessible to other users. You can host your web application on any server you choose. This includes local servers and servers in the cloud. Use the following table to choose and set up a server for

### Hosting a Web Application on a Server

To make your web application available to other users, host your build output on a web server that is accessible to other users.

You can host your web application on any server you choose. This includes local servers and servers in the cloud. Use the following table to choose and set up a server for hosting your web application.

#### Options for Hosting a Web Application

| Required Products | Use Case | Hosting Server | Hosting Instructions |
| --- | --- | --- | --- |
| G Web Development Software or NI SystemLink | Choose this server in either of the following cases: You want to manage your own server from within your network, either through G Web Development Software or NI SystemLink. You want to avoid placing the server burden on your measurement hardware, such as when using real-time hardware. | NI Web Server | NI SystemLink and the G Web Development Software both use the NI Web Server. To host a WebVI on the NI Web Server with permissioned access and configurable security settings, follow the instructions for Hosting a WebVI with the Web Applications Service. To host a WebVI on the NI Web Server as simple static files without access control settings, follow the instructions for Hosting a Web Application on the NI Web Server. |
| LabVIEW 2013 or later | Choose this server in either of the following cases: You want to host a web application directly on a LabVIEW real-time target, such as a CompactRIO. You want to use the security features provided by LabVIEW Web services. | LabVIEW Application Web Server | Follow the instructions for Hosting a Web Application on the NI Application Web Server. |
| 3rd party software | You need functionality that is not included in the NI server options. | 3rd party server | Before you begin, you must build a web application. Follow the instructions for Building a Web Application as a Web Page. Copy your entire web application build output to the server directory. To navigate to your web application output on your machine, click Locate directory in Windows Explorer on the Document tab of your web application component document. Note You may need to configure a 3rd party server to support the application/wasm MIME type for files with the .wasm file extension. |

Parent topic:

Creating a Web Application

Related tasks:

- Hosting a WebVI with the Web Applications Service
- Hosting a Web Application on the NI Web Server
- Hosting a Web Application on the NI Application Web Server
- Building a Web Application as a Web Page

<!--NI_TOPIC bundle=g-web-development path=hyperlink-control.html language=enus -->
## TOPIC 00197: Hyperlink Control

- bundle_id: `g-web-development`
- source_path: `hyperlink-control.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/hyperlink-control.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Enter or display a URL hyperlink.

### Hyperlink Control

Enter or display a URL hyperlink.

Parent topic:

Creating User Interfaces

<!--NI_TOPIC bundle=g-web-development path=icons-connector-panes-api.html language=enus -->
## TOPIC 00198: Icons and Connector Panes for Distributed APIs

- bundle_id: `g-web-development`
- source_path: `icons-connector-panes-api.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/icons-connector-panes-api.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Refer to the following table for best practices for creating icons and connector panes. 5 Guidelines for SubVI Size Guideline Required or Recommended? Details Make all VIs or as many VIs as possible the same size. Required The icon size is determined by the connector pane pattern that the subVI requ

### Icons and Connector Panes for Distributed APIs

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

[IMAGE alt='image' src='GUID-BD123550-6F61-4DED-A0D6-8E41874FDBDF-a5.png']

#### Locate Inputs and Outputs Consistently

[IMAGE alt='image' src='GUID-523EF860-01DA-465E-902F-5D246FC2A224-a5.png']

Parent topic:

Best Practices for Designing and Developing an Application Programming Interface (API) in G Web Development Software

Parent topic:

Best Practices for Designing and Developing an Application Programming Interface (API) in G Web Development Software

Related concepts:

- Best Practices for Designing and Developing an Application Programming Interface (API) in G Web Development Software

Related reference:

- Icons and Connector Panes for G Web Development Software Projects

<!--NI_TOPIC bundle=g-web-development path=icons-connector-panes-lv-proj.html language=enus -->
## TOPIC 00199: Icons and Connector Panes for G Web Development Software Projects

- bundle_id: `g-web-development`
- source_path: `icons-connector-panes-lv-proj.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/icons-connector-panes-lv-proj.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Refer to the following table for best practices for creating icons and connector panes in G Web Development Software. Guideline Required or Recommended? Details Example(s) Consider using the well-designed icons in the G Web Development Software libraries as prototypes for your icon. Recommended If y

### Icons and Connector Panes for G Web
 Development Software Projects

Refer to the following table for best practices for creating icons and connector panes
 in G Web Development Software.

| Guideline | Required or Recommended? | Details | Example(s) |
| --- | --- | --- | --- |
| Consider using the well-designed icons in the G Web Development Software libraries as prototypes for your icon. | Recommended | If you cannot find or create a picture to use for an icon, you can use text. | N/A |
| Create a uniform icon style for all related VIs. | Recommended | A uniform style helps users visually determine which subVIs are associated with a top-level VI. | N/A |
| Avoid using colloquialisms when making icons. | Recommended | Colloquialisms, even in pictures, are difficult to translate. Users that speak languages other than English may not understand a picture that relies on cultural background knowledge. | If you represent a data logging VI with a picture of a lumberjack, some users may not know the cultural reference to understand how a lumberjack can represent data logging. |
| Create a meaningful icon for every VI. | Recommended | The icon represents the VI on a palette and diagram. Well-designed icons help users gain a better understanding of the subVI without the need for excess documentation. | N/A |
| Consider common node sizes in the G Web Development Software when designing an icon. | Recommended | Refer to the following common node sizes: 30x30 for small nodes. This size supports the 3-1-1-3 connector pane pattern. 40x40 for the default VI size. This size supports the 4-2-2-4 connector pane pattern. 50x50 for the default size used by NI hardware driver and Advanced Analysis Library APIs. This size supports the 5-3-3-5 connector pane pattern. | N/A |
| Make sure to set inputs and outputs for each subVI as required, recommended, or optional in the connector pane for that subVI, and make sure the settings make sense for your project. | Recommended | Use the Usage settings on the Item tab for the connector panes of all subVIs to specify the input and output settings for each subVI. The Usage setting for connector pane terminals affects the appearance of the inputs and outputs in the Context Help and reminds users to wire subVI connections. Use the required setting for inputs that users must wire for the subVI to run properly. Use the optional setting for inputs that have default values that are appropriate for the subVI the majority of the time. Use the recommended setting for all other inputs. | N/A |
| Assign inputs and outputs according to the way a user will eventually wire VIs together. | Recommended | Wire inputs on the left and outputs on the right of the connector pane because standard data flow moves from the left to the right. Consistency between the location you assign inputs and outputs in the connector pane and their location in the actual data flow promotes ease of use and reuse. | If you create a group of subVIs that you often use together, give the subVIs a consistent connector pane with common inputs in the same location to help you remember where to locate each input. If you create a subVI that produces an output that another subVI uses as an input, such as references, task IDs, and error clusters, align the input and output connections to simplify the wiring patterns. Assign two inputs of a VI to the left two terminals of the corresponding connector pane and two outputs of that VI to the right two terminals of the corresponding connector pane. |
| Reserve the bottom left and right connector pane terminals for the error input and error output. | Recommended | Session-based APIs are the only exception to this recommendation. For session-based APIs, you can place error inputs and outputs directly beneath session and reference inputs and outputs. | N/A |
| Avoid creating connector panes with more than 16 terminals. | Recommended | Including too many terminals can make a subVI difficult to understand. You can consider either splitting the functionality of the subVI into multiple subVIs or using clusters to create logical groupings of the inputs to the subVI, depending on which solution makes sense for your project. | N/A |
| If your subVI includes a pass-through input and output pair, add an in suffix to the control and an out suffix to the indicator. | Recommended | Adding these suffixes to pairs of inputs and outputs indicates a relationship between the inputs and outputs. | If you name an input reference in, name the related output reference out. |
| If your subVI includes a pass-through input and output pair, and you wire the control directly to the indicator on the diagram to prevent the value from changing, remove the indicator from the connector pane. | Recommended | You can exclude references from this guideline. | N/A |

Parent topic:

Best Practices for Creating Projects in G Web Development Software

<!--NI_TOPIC bundle=g-web-development path=identifying-errors.html language=enus -->
## TOPIC 00200: Identifying Errors That Prevent You from Running Code

- bundle_id: `g-web-development`
- source_path: `identifying-errors.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/identifying-errors.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `concept`
- source_description: As you create code, a broken Run button communicates that the code contains errors that prevent it from running. You can use the provided error and warning messages to help fix these problems. Errors break the code. You must resolve any errors before you can run the program. Warnings do not prevent

### Identifying Errors That Prevent You from Running Code

As you create code, a broken 
 Run button 
 [IMAGE alt='image' src='GUID-EDAB8A33-591F-407B-99DB-B44A700348E7-a5.png'] communicates that the code contains errors that prevent it from running.

You can use the provided error and warning messages to help fix these problems. 
 *Errors* break the code. You must resolve any errors before you can run the program. 
 *Warnings* do not prevent you from running the code. They are designed to help you avoid potential problems in the program.

To identify the specific errors, click the broken 
 Run button to display the 
 Errors and Warnings tab. The following image highlights sections of the 
 Errors and Warnings tab that define detected errors and warnings.

[IMAGE alt='image' src='GUID-0FEF9A0D-6D1D-4755-B12B-E669CF569F1B-a5.png']

|  | Severity—Denotes whether an issue is an error or a warning. |
| --- | --- |
|  | Source—Identifies the object that is causing the error or warning. |
|  | Message—Provides more detail about why the error or warning exists. |

Parent topic:

Testing and Debugging

<!--NI_TOPIC bundle=g-web-development path=image-control.html language=enus -->
## TOPIC 00201: Image

- bundle_id: `g-web-development`
- source_path: `image-control.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/image-control.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Decorate the user interface with bitmap or vector graphics.

### Image

Decorate the user interface with bitmap or vector graphics.

Parent topic:

Drawing Controls

<!--NI_TOPIC bundle=g-web-development path=indeterminate-progress.html language=enus -->
## TOPIC 00202: Indeterminate Progress

- bundle_id: `g-web-development`
- source_path: `indeterminate-progress.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/indeterminate-progress.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Displays unknown progress

### Indeterminate Progress

Displays unknown progress

Parent topic:

Creating User Interfaces

<!--NI_TOPIC bundle=g-web-development path=indicator.html language=enus -->
## TOPIC 00203: Indicator

- bundle_id: `g-web-development`
- source_path: `indicator.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/indicator.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Change the selected control to an indicator.

### Indicator

Change the selected control to an indicator.

Parent topic:

Creating User Interfaces

<!--NI_TOPIC bundle=g-web-development path=integer-digits.html language=enus -->
## TOPIC 00204: Integer Digits

- bundle_id: `g-web-development`
- source_path: `integer-digits.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/integer-digits.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Set the number of whole number digits to display.

### Integer Digits

Set the number of whole number digits to display.

Parent topic:

Creating User Interfaces

<!--NI_TOPIC bundle=g-web-development path=integrate-js-library.html language=enus -->
## TOPIC 00205: Integrating a JavaScript File Into a Web Application

- bundle_id: `g-web-development`
- source_path: `integrate-js-library.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/integrate-js-library.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `task`
- source_description: Connect a JavaScript file to your web application and call functions you defined in a JavaScript Library Interface (JSLI) in your web application. Before you begin, create and configure a JLI. Import the JavaScript file(s) you want to use into your web application. Save your project. On the Project

### Integrating a JavaScript File Into a Web Application

Connect a JavaScript file to your web application and call functions you defined in a JavaScript Library Interface (JSLI) in your web application.

Before you begin, create and configure a JLI.

1. Import the JavaScript file(s) you want to use into your web application.
  1. Save your project.
  2. On the 
 Project Files tab, right-click a web application document or library component document (.gcomp) and select 
 Import files.
  3. Navigate to the JavaScript file(s) you want to add and click 
 Open. Click 
 Copy to close the 
 Copy existing file(s) dialog box.
2. Integrate the JavaScript file into your web application.
  1. Open the JSLI document associated with the JavaScript file and enter the relative path to the JavaScript file in the HTML script and link dependencies form field. 
 Example: 
 <script src="library.js"></script> 
 Note The JavaScript file must be in the same component as the JSLI document and must be marked as 
 Always include in the component document.
  2. Click 
 Apply Changes.
3. Add the entry points you defined in the JSLI to any web application in your project.
  1. Open the WebVI in which you want to call the JavaScript function.
  2. On the diagram palette, click Project Items»Software»<YourWebAppName>. Click the folder with the name of your JSLI
 document to show each entry point you defined in that JSLI.
  3. Drop the entry points you want to use on the diagram.
  4. Wire the entry points and complete the diagram.
  5. Run the WebVI. Input data passes from the diagram to the JavaScript code, and output data returns from the JavaScript code to the diagram.

Parent topic:

Calling JavaScript Functions in a Web Application

Related tasks:

- Defining Calls to JavaScript Functions using a JavaScript Library Interface

<!--NI_TOPIC bundle=g-web-development path=intensity-graph-control.html language=enus -->
## TOPIC 00206: Intensity Graph Control

- bundle_id: `g-web-development`
- source_path: `intensity-graph-control.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/intensity-graph-control.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Plot 3D data on a 2D plot by using color to display the values of the third dimension. For example, you can use an intensity graph to display patterned data, such as terrain, where the magnitude represents altitude. What Types of Data Can I Plot? Intensity graphs accept 2D arrays of numeric values.

### Intensity Graph Control

Plot 3D data on a 2D plot by using color to display the values of the third dimension. For example, you can use an intensity graph to display patterned data, such as terrain, where the magnitude represents altitude.

[IMAGE alt='image' src='GUID-95977A16-0963-4A2A-9D95-DF05B3E9702B-a5.png']

#### What Types of Data Can I Plot?

Intensity graphs accept 2D arrays of numeric values. Each number in the array represents a specific color. The array indexes correspond to the center of the color block. The row index of the array is the x-value, and the column index of the array is the y-value. The color block has a unit area, which is the area between the two points, as defined by the array indexes.

Rows of the array appear as columns on the graph and vice-versa. If you want rows to appear as rows on the graph, use Transpose 2D Array before wiring the array to the graph.

#### Configuring the Color Scale

When you set the color mapping for an intensity graph, you configure the color scale of the graph. The color scale consists of at least two markers, each with a numeric value and a corresponding display color. The colors displayed on an intensity graph correspond to the numeric values associated with the specified colors. Color mapping is useful for visually indicating data ranges, such as when plot data exceeds a threshold value.

Click 
 Color scale on the 
 Item tab to set the color mapping. Lower and upper out-of-range colors are specified as 
 High color and 
 Low color and are displayed on the graph.

Parent topic:

Charts and Graphs

<!--NI_TOPIC bundle=g-web-development path=interval.html language=enus -->
## TOPIC 00207: Interval

- bundle_id: `g-web-development`
- source_path: `interval.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/interval.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Set the amount by which the increment and decrement buttons increase or decrease the value of the numeric control.

### Interval

Set the amount by which the increment and decrement buttons increase or decrease the value of the numeric control.

Parent topic:

Creating User Interfaces

<!--NI_TOPIC bundle=g-web-development path=inverted-graph.html language=enus -->
## TOPIC 00208: Inverted

- bundle_id: `g-web-development`
- source_path: `inverted-graph.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/inverted-graph.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reverse the positions of the minimum and maximum values on the scale.

### Inverted

Reverse the positions of the minimum and maximum values on the scale.

Parent topic:

Creating User Interfaces

<!--NI_TOPIC bundle=g-web-development path=inverted-numeric-pointers.html language=enus -->
## TOPIC 00209: Inverted

- bundle_id: `g-web-development`
- source_path: `inverted-numeric-pointers.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/inverted-numeric-pointers.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reverse the positions of the minimum and maximum values on the scale.

### Inverted

Reverse the positions of the minimum and maximum values on the scale.

Parent topic:

Creating User Interfaces

<!--NI_TOPIC bundle=g-web-development path=javascript-web-application.html language=enus -->
## TOPIC 00210: Using JavaScript with a Web Application

- bundle_id: `g-web-development`
- source_path: `javascript-web-application.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/javascript-web-application.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `concept`
- source_description: Call JavaScript functions in your web application and use JavaScript to create UI elements.

### Using JavaScript with a Web
 Application

Call JavaScript functions in your web application and use JavaScript to create UI
 elements.

- [Calling JavaScript Functions in a Web Application](calling-js-functions-web-app.html) Use a JavaScript Library Interface (JSLI) to call globally accessible JavaScript functions in your web application.
- [Creating UI Elements with JavaScript](create-ui-elements-with-javascript.html) Create UI elements to place on the panel of your web application using the Placeholder HTML Container and JavaScript Library Interface document (JSLI).
- [JavaScript Resources](js-resources.html) Research JavaScript concepts using NI-recommended resources.

Parent topic:

Creating a Web Application

<!--NI_TOPIC bundle=g-web-development path=js-resources.html language=enus -->
## TOPIC 00211: JavaScript Resources

- bundle_id: `g-web-development`
- source_path: `js-resources.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/js-resources.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Research JavaScript concepts using NI-recommended resources. The items are some concepts you may want to research when using JavaScript Library Interfaces (JSLIs) and calling JavaScript functions in your web application. If the JavaScript concept you want to learn about is not listed, NI recommends

### JavaScript Resources

Research JavaScript concepts using NI-recommended resources.

- Asynchronous JavaScript
- Built-in Objects
- Callback Function
- Global Scope
- Immediately Invoked Function Expression (IIFE)
- Objects
- Strict Mode
- TypedArray Object

Parent topic:

Using JavaScript with a Web Application

Related information:

- Mozilla Developer Network JavaScript Documentation

<!--NI_TOPIC bundle=g-web-development path=jsref-function.html language=enus -->
## TOPIC 00212: JavaScript Reference Functionality

- bundle_id: `g-web-development`
- source_path: `jsref-function.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/jsref-function.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `concept`
- source_description: JavaScript references behave similarly to references for other data types, but have some unique functionality. When using JavaScript references in your web application, you need to consider the following:Primitive values null and undefined—JavaScript references treat primitive values null and undefi

### JavaScript Reference Functionality

JavaScript references behave similarly to references for other data types, but have some
 unique functionality.

- Primitive values null and
 undefined —JavaScript references treat primitive
 values null and undefined the same
 as other primitives, such as strings, booleans, numbers, etc. If a value of null
 or undefined is returned, it generates a new JavaScript reference that you need
 to clean up to prevent memory leaks.
- Not a Number/Path/Refnum? behavior—The node tells you if
 the value is valid, but it does not tell you if the JavaScript reference value
 is null or undefined. There is not an existing node to check for values of null
 or undefined.
- JavaScript values—JavaScript references can hold any JavaScript value, including
 primitives and objects, such as JavaScript functions, HTML elements, and class
 instances.
- Type definitions containing a JavaScript reference—JavaScript references do not
 have front panel representations, so you will need to use the following process
 to create a type definition containing a JavaScript reference:
  1. Create a VI (.gvi) with a web server target in your web application
 project.
  2. Add your JavaScript reference to the diagram.
  3. In the Configuration pane, click Change to Type
 Definition .

Parent topic:

Creating UI Elements with JavaScript

Related concepts:

- Creating UI Elements with JavaScript

<!--NI_TOPIC bundle=g-web-development path=keyboard-shortcuts.html language=enus -->
## TOPIC 00213: Keyboard Shortcuts

- bundle_id: `g-web-development`
- source_path: `keyboard-shortcuts.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/keyboard-shortcuts.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: The following tables list keyboard shortcuts in the environment. File Operations Shortcut Action Ctrl-N Open a new document and add it to the existing project. Ctrl-Shift-N Open a new project. Ctrl-O Open an existing project. Ctrl-W Close the current document. Ctrl-S Save the current file. Ctrl-Shif

### Keyboard Shortcuts

The following tables list keyboard shortcuts in the environment.

Parent topic:

Getting Started with G Web Development Software

#### File Operations

| Shortcut | Action |
| --- | --- |
| Ctrl-N | Open a new document and add it to the existing project. |
| Ctrl-Shift-N | Open a new project. |
| Ctrl-O | Open an existing project. |
| Ctrl-W | Close the current document. |
| Ctrl-S | Save the current file. |
| Ctrl-Shift-S | Save all open files. |
| Ctrl-P | Print the current document. |
| Alt-F4 | Quit. |

#### Basic Editing

| Shortcut | Action |
| --- | --- |
| Ctrl-X Shift-Delete | Cut. |
| Ctrl-C Ctrl-Insert | Copy. |
| Ctrl-V Shift-Insert | Paste. |
| Ctrl-Z Alt-Backspace | Undo. |
| Ctrl-Y Alt-Shift-Backspace | Redo. |
| Shift-F10 Application Key | Open shortcut menu for selected item. |
| Delete | Delete. |
| Ctrl-Delete | Delete and rewire. |

#### Selecting and Moving Objects

| Shortcut | Action |
| --- | --- |
| Shift-Click | Select multiple objects. Add object to the current selection. |
| Ctrl-A | Select all objects. |
| Arrow keys | Move selected objects in grid-sized increments. |
| Shift-Arrow keys | Move selected objects four grid units. |
| Ctrl-Drag | Copy and drag selected object. |
| Ctrl-Shift-Drag | Copy selected object and move it along one axis. |
| Shift-Resize | Resize selected object while maintaining aspect ratio. |
| Ctrl-Resize | Resize selected object while maintaining center point. |
| Shift-Ctrl-Resize | Resize selected object while maintaining both aspect ratio and center point. |
| Ctrl-Drag open area | Create additional blank space along the axis you drag the mouse. |
| Double-click open area | Add free label or comment to panel or diagram. |
| Spacebar-Drag | Pan across panel or diagram. |

#### Navigating the Environment

| Shortcut | Action |
| --- | --- |
| Ctrl-F | Find and replace text or objects within a document. |
| Ctrl-Shift-F | Find and replace text or objects within a project. |
| Enter F3 Ctrl-G | Search document for next instance of text or an object. This command is only available when in Find mode. |
| Shift-Enter Shift-F3 Shift-Ctrl-G | Search document for previous instance of text or an object. This command is only available when in Find mode. |
| Ctrl-Tab | Cycle through document tabs in the order in which they appear onscreen. |
| Ctrl-Shift-Tab | Cycle through document tabs in the opposite order in which they appear onscreen. |
| Ctrl-Shift-Spacebar | Shift focus to the application-wide search bar. |
| Ctrl-\\ | Hide and show all tabs. Hide and show all panes. |

#### Navigating the Panel and Diagram

| Editor Command | Shortcut | Action |
| --- | --- | --- |
| Panel and diagram selectors | Ctrl-E | Toggle between the panel and diagram view. If the icon view is active, switch to the panel view. |
| Search | Ctrl-Spacebar (Chinese keyboards) Ctrl-Alt-Spacebar | Shift focus to the palette search bar. |
| — | Ctrl-' | Toggle the diagram grid on/off. |
| — | Shift-Ctrl-; | Toggle Smart Guides on/off. Smart Guides help you align objects on the panel. |
| Vertical scroll bar | Mouse wheel | Scroll the document vertically. |
| Horizontal scroll bar | Shift-Mouse wheel | Scroll the document horizontally. |
| — | Tab | Shift focus from one control to another in tabbing order while the code is running. |
| — | Shift-Tab | Shift focus from one control to another in reverse tabbing order while the code is running. |
| — | Ctrl-Alt-I | Open and close the icon editor. |

#### Help Commands

| Shortcut | Action |
| --- | --- |
| Ctrl-H | Display the Context Help. |
| F1 | Access additional information on ni.com. |

#### Running Code

| Editor Command | Shortcut | Action |
| --- | --- | --- |
| Run | Ctrl-R | Execute this code. |
| Abort | Ctrl-. | Stop the code immediately, before it finishes executing. |
|  | Ctrl-Run button | Recompile the code in the current document. |
|  | Ctrl-Shift-Run button | Recompile the code in all documents in memory. |

#### Wiring

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

#### Editing Text

| Shortcut | Action |
| --- | --- |
| Double-click text | Select a single word in a string. |
| Triple-click text | Select the entire string. |
| Ctrl-Right arrow Ctrl-Left arrow | Move the cursor within a string by one word in the direction of the arrow. |
| Home | Move the cursor to the beginning of the current line. |
| End | Move the cursor to the end of the current line. |
| Ctrl-Home | Move the cursor to the beginning of the string. |
| Ctrl-End | Move the cursor to the end of the string. |
| Esc | Cancel text entry. |
| Ctrl-Enter | Submit text entry. |

#### Navigating the Project Files and Captured Data Tabs

| Shortcut | Action |
| --- | --- |
| * (Numeric keypad) | Expand everything under the selected folder. |
| + (Numeric keypad) | Expand the selected folder. |
| - (Numeric keypad) | Collapse the selected folder. |
| Right arrow | Expand the selected folder if it is closed. Otherwise, this keyboard shortcut selects the first child. |
| Left arrow | Collapse the selected folder if it is open. Otherwise, this keyboard shortcut selects the parent. |
| Ctrl-up arrow Ctrl-down arrow | Scroll through the pane without changing the current selection. |
| Any printable key(s) | Select the item beginning with the entered letter(s). |
| Enter | Open the selected document. |
| F2 | Rename the selected item. |
| Page Up Home | Move the selection to the first item in the tree. |
| Page Down End | Moves the selection to the last item in the tree. |

#### Zooming

| Shortcut | Action |
| --- | --- |
| Ctrl-Mouse wheel | Zoom. |
| Ctrl-+ | Zoom in. |
| Ctrl-- | Zoom out. |
| Ctrl-0 | Zoom to fit. |
| Ctrl-9 | Zoom to fit the selection. |

<!--NI_TOPIC bundle=g-web-development path=knob.html language=enus -->
## TOPIC 00214: Knob

- bundle_id: `g-web-development`
- source_path: `knob.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/knob.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Enter or display numeric data in a rotary scale.

### Knob

Enter or display numeric data in a rotary scale.

Parent topic:

Creating User Interfaces

<!--NI_TOPIC bundle=g-web-development path=label-placement.html language=enus -->
## TOPIC 00215: Label Placement

- bundle_id: `g-web-development`
- source_path: `label-placement.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/label-placement.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Set the label location for selected items on the panel.

### Label Placement

Set the label location for selected items on the panel.

Parent topic:

Creating User Interfaces

<!--NI_TOPIC bundle=g-web-development path=label-text-linked-control-name.html language=enus -->
## TOPIC 00216: Label text linked to control name

- bundle_id: `g-web-development`
- source_path: `label-text-linked-control-name.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/label-text-linked-control-name.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Toggle whether the label and name of the control are set independent of each other.

### Label text linked to control
 name

Toggle whether the label and name of the control are set independent of each
 other.

Parent topic:

Creating User Interfaces

<!--NI_TOPIC bundle=g-web-development path=label.html language=enus -->
## TOPIC 00217: Label

- bundle_id: `g-web-development`
- source_path: `label.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/label.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Toggle the control label on or off.

### Label

Toggle the control label on or off.

Parent topic:

Creating User Interfaces

<!--NI_TOPIC bundle=g-web-development path=labview-standard-error-behavior.html language=enus -->
## TOPIC 00218: Standard Error Behavior

- bundle_id: `g-web-development`
- source_path: `labview-standard-error-behavior.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/labview-standard-error-behavior.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `concept`
- source_description: Many nodes provide error in and an error out parameters so that the node can respond to and communicate errors that occur while code is running. When you create an application, wire all error inputs and outputs of each node on the diagram so that error information moves through the application in th

### Standard Error Behavior

Many nodes provide error in and an error out parameters so that the node can respond to and communicate errors that occur while code is running. When you create an application, wire all error inputs and outputs of each node on the diagram so that error information moves through the application in the same way as data values. As your VI runs, each node with error-checking capabilities monitors for error information that is passed to the error input from the previous node. Since each node with error inputs and outputs does the same thing, allowing only valid data or error information to flow through the diagram.

The value of error in specifies whether an error occurred before the node runs. Most nodes respond to values of error in in a standard, predictable way:

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

Note

error in

error in

If you enable error information to flow through the diagram by wiring all error inputs and outputs, you can also use Error nodes to process information provided by the error, access additional information about the error, and use that information to make run-time decisions based on the error conditions in the application.

Parent topic:

Testing and Debugging

<!--NI_TOPIC bundle=g-web-development path=layouts.html language=enus -->
## TOPIC 00219: Layouts

- bundle_id: `g-web-development`
- source_path: `layouts.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/layouts.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Organize the appearance of controls and indicators or display the panel of other VIs. When Should I Use a Tab Control? Tab controls are useful when you have several panel objects that are used together or during a specific phase of operation. For example, you might have a VI that requires the user t

### Layouts

Organize the appearance of controls and indicators or display the panel of other VIs.

[IMAGE alt='image' src='GUID-9D41F51E-FCED-456C-8903-04447CF531FE-a5.png']

#### When Should I Use a Tab Control?

Tab controls are useful when you have several panel objects that are used together or
 during a specific phase of operation. For example, you might have a VI that requires the
 user to first configure several settings before a test can start, then allows the user to
 modify aspects of the test as it progresses, and finally allows the user to display and
 store only pertinent data.

Parent topic:

Creating User Interfaces

<!--NI_TOPIC bundle=g-web-development path=libraries.html language=enus -->
## TOPIC 00220: Libraries

- bundle_id: `g-web-development`
- source_path: `libraries.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/libraries.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `concept`
- source_description: A library is a collection of source files, such as VIs, type definitions, classes, and other support files. You can use a library to organize source​ files into a single hierarchy of items. A library allows you to reuse code across multiple applications without having to implement the same functiona

### Libraries

A *library* is a collection of source files, such
 as VIs, type definitions, classes, and other support files. You can use a library
 to organize source​ files into a single hierarchy of items.

A library allows you to reuse code across multiple applications without having to implement the same functionality in each application.​ Your code must be part of a library before you can reuse it across ​applications.

Use a *Library* document (.gcomp) to create a library. The
 Library​ document allows you to perform the following actions: ​

- Organize files using namespaces to avoid name
 collisions.​
- Customize the organization of files on the
 palette.
- Enable source files to be called from other
 applications and libraries​.

Parent topic:

Creating a Web Application

Related tasks:

- Organizing Code to Avoid Name Collisions

<!--NI_TOPIC bundle=g-web-development path=line-arrows.html language=enus -->
## TOPIC 00221: Line with Arrows

- bundle_id: `g-web-development`
- source_path: `line-arrows.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/line-arrows.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Draw a straight line with an arrow on one end.

### Line with Arrows

Draw a straight line with an arrow on one end.

Parent topic:

Drawing Controls

<!--NI_TOPIC bundle=g-web-development path=line.html language=enus -->
## TOPIC 00222: Line

- bundle_id: `g-web-development`
- source_path: `line.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/line.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Draw a straight line.

### Line

Draw a straight line.

Parent topic:

Drawing Controls

<!--NI_TOPIC bundle=g-web-development path=lines.html language=enus -->
## TOPIC 00223: Lines Palette

- bundle_id: `g-web-development`
- source_path: `lines.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/lines.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Add lines to the icon.

### Lines Palette

Add lines to the icon.

Parent topic:

Creating User Interfaces

<!--NI_TOPIC bundle=g-web-development path=linking-webvis.html language=enus -->
## TOPIC 00224: Linking WebVIs in a Web Application

- bundle_id: `g-web-development`
- source_path: `linking-webvis.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/linking-webvis.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `task`
- source_description: Before you begin, open or create a web application project with multiple top-level WebVIs. Each WebVI that you mark as top-level outputs as a separate web page. On the Project Files tab, double-click the web application document to open it. In the web application document, select the top-level WebVI

### Linking WebVIs in a Web Application

Before you begin, open or create a web application project with multiple top-level WebVIs. Each WebVI that you mark as top-level outputs as a separate web page.

1. On the 
 Project Files tab, double-click the web application document to open it.
2. In the web application document, select the top-level WebVI you want to link to. On the 
 Item tab, copy the 
 Relative URL.
3. Open the top-level WebVI you want to link from.
4. Switch to the panel and add a Hyperlink Control.
5. Select the Hyperlink Control. On the 
 Item tab, in the 
 URL field, paste the relative URL of the WebVI that you want to link to. 
 You may need to modify the relative URL depending on how your files are organized. Consider the following file structure.
 Application
|
|———One.gviweb
|
|———Two.gviweb
|
|———Namespace_A
| |
| |———Three.gviweb
|
|———Namespace_B
 |
 |———Four.gviweb
 |
 |———Namespace_C
 |
 |———Five.gviweb
 Link from
 Link to
 Relative URLOne.gviweb
 Two.gviweb
 Two.html
 One.gviweb
 Three.gviweb
 Namespace_A/Three.html
 Three.gviweb
 One.gviweb
 ../One.html
 Three.gviweb
 Four.gviweb
 ../Namespace_B/Four.html
 Five.gviweb
 One.gviweb
 ../../One.html
 Five.gviweb
 Three.gviweb
 ../../Namespace_A/Three.html
6. Build your application and open the HTML output in a web browser to test the link you created.

Search within the programming environment to access the following installed example:

*Multiple Top-Level WebVIs*

Parent topic:

Creating a Web Application

<!--NI_TOPIC bundle=g-web-development path=listbox.html language=enus -->
## TOPIC 00225: Listbox

- bundle_id: `g-web-development`
- source_path: `listbox.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/listbox.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Create a list of items in which a user can select single or multiple items.

### Listbox

Create a list of items in which a user can select single or multiple items.

Parent topic:

Creating User Interfaces

<!--NI_TOPIC bundle=g-web-development path=lock-icon-editor.html language=enus -->
## TOPIC 00226: Lock

- bundle_id: `g-web-development`
- source_path: `lock-icon-editor.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/lock-icon-editor.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Add a lock symbol to the icon.

### Lock

Add a lock symbol to the icon.

Parent topic:

Actions Palette

<!--NI_TOPIC bundle=g-web-development path=lock-label.html language=enus -->
## TOPIC 00227: Lock Label

- bundle_id: `g-web-development`
- source_path: `lock-label.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/lock-label.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Keep the label with the control.

### Lock Label

Keep the label with the control.

Parent topic:

Creating User Interfaces

<!--NI_TOPIC bundle=g-web-development path=manual-overview.html language=enus -->
## TOPIC 00228: G Web Development Software

- bundle_id: `g-web-development`
- source_path: `manual-overview.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/manual-overview.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use G Web Development Software to create browser-based user interfaces to visualize data from distributed systems. This manual contains step-by-step instructions for working with WebVIs and creating web applications. Create a web application, design responsive UIs and controls, and debug, build, and

### G Web Development Software

Use G Web Development Software to create browser-based user interfaces to visualize
 data from distributed systems. This manual contains step-by-step instructions for
 working with WebVIs and creating web applications.

[IMAGE alt='image' src='GUID-685643D3-0D11-4CD0-89E3-59E98773AC5B-a5.png']

- Create a web application, design responsive UIs and controls, and debug, build, and
 package your WebVIs.
- Access WebVI resource files, web service data, and use web services like SystemLink
 Tag and Message in your web application.
- Add JavaScript functions to your web application using a JavaScript Library Interface
 (JSLI) document and create custom UI elements.
- Learn about your hosting options during development and how to host your web
 application to share with users.
- Build a library and add custom palettes to share code and create add-ons.

Tip

Learning

Examples

»

Programming WebVIs

Related concepts:

- Developing a Web Application
- Communicating Data with a Web Application
- Using JavaScript with a Web Application

Related tasks:

- Hosting a Web Application on a Server
- Building Shareable Libraries

Related information:

- NI Web Server User Manual
- SystemLink Server User Manual

<!--NI_TOPIC bundle=g-web-development path=masked-input-control.html language=enus -->
## TOPIC 00229: Masked Input Control

- bundle_id: `g-web-development`
- source_path: `masked-input-control.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/masked-input-control.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Enter string data in masked display.

### Masked Input Control

Enter string data in masked display.

Parent topic:

Creating User Interfaces

<!--NI_TOPIC bundle=g-web-development path=max.html language=enus -->
## TOPIC 00230: Max

- bundle_id: `g-web-development`
- source_path: `max.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/max.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Set the maximum value for the data range.

### Max

Set the maximum value for the data range.

Parent topic:

Creating User Interfaces

<!--NI_TOPIC bundle=g-web-development path=measure-icon-editor.html language=enus -->
## TOPIC 00231: Measure

- bundle_id: `g-web-development`
- source_path: `measure-icon-editor.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/measure-icon-editor.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Add a measure symbol to the icon.

### Measure

Add a measure symbol to the icon.

Parent topic:

Actions Palette

<!--NI_TOPIC bundle=g-web-development path=mechanical-action.html language=enus -->
## TOPIC 00232: Mechanical Action

- bundle_id: `g-web-development`
- source_path: `mechanical-action.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/mechanical-action.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configure button behavior.

### Mechanical Action

Configure button behavior.

Parent topic:

Creating User Interfaces

<!--NI_TOPIC bundle=g-web-development path=meter.html language=enus -->
## TOPIC 00233: Meter

- bundle_id: `g-web-development`
- source_path: `meter.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/meter.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Enter or display numeric data in a rotary scale.

### Meter

Enter or display numeric data in a rotary scale.

Parent topic:

Creating User Interfaces

<!--NI_TOPIC bundle=g-web-development path=min.html language=enus -->
## TOPIC 00234: Min

- bundle_id: `g-web-development`
- source_path: `min.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/min.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Set the minimum value for the data range.

### Min

Set the minimum value for the data range.

Parent topic:

Creating User Interfaces

<!--NI_TOPIC bundle=g-web-development path=minimize-subvi-overhead.html language=enus -->
## TOPIC 00235: Minimizing SubVI Overhead

- bundle_id: `g-web-development`
- source_path: `minimize-subvi-overhead.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/minimize-subvi-overhead.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `task`
- source_description: Inlining a subVI into its calling VIs helps minimize the overhead associated with calling the subVI. When you inline a subVI, G Web Development Software inserts the compiled code of the subVI into the compiled code of the calling VI. If you then make changes to the subVI, G Web Development Software

### Minimizing SubVI Overhead

Inlining a subVI into its calling VIs helps minimize the overhead associated with calling
 the subVI.

When you inline a subVI, G Web Development Software
 inserts the compiled code of the subVI into the compiled code of the
 calling VI. If you then make changes to the subVI, G Web Development Software
 recompiles all calling VIs of that subVI to include those changes.
 Essentially, inlining a subVI removes the need to call the subVI at
 run time. Instead, the subVI code executes inside the compiled code
 of the calling VI.

A subVI that you want to inline cannot have any of the following
 characteristics:

- Contains recursion
- Contains certain diagram nodes, such as control references.
 These nodes generate edit-time error messages if you enable
 subVI inlining.

Complete the following steps to inline a
 subVI.

1. On the Document tab, in the
 Behavior section, click
 Properties to access the
 property settings for the subVI.
2. Place a checkmark in the Inline subVI into calling
 VIs checkbox.
3. Set VI Reentrancy to
 Stateless or
 Stateful to configure
 reentrant execution.
4. Click OK.

Parent topic:

SubVIs

<!--NI_TOPIC bundle=g-web-development path=moon-icon-editor.html language=enus -->
## TOPIC 00236: Moon

- bundle_id: `g-web-development`
- source_path: `moon-icon-editor.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/moon-icon-editor.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Create a customizable moon.

### Moon

Create a customizable moon.

Parent topic:

Shapes Palette

<!--NI_TOPIC bundle=g-web-development path=name.html language=enus -->
## TOPIC 00237: Name

- bundle_id: `g-web-development`
- source_path: `name.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/name.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Set a unique name to identify the control on the diagram.

### Name

Set a unique name to identify the control on the diagram.

Parent topic:

Creating User Interfaces

<!--NI_TOPIC bundle=g-web-development path=network-icon-editor.html language=enus -->
## TOPIC 00238: Network

- bundle_id: `g-web-development`
- source_path: `network-icon-editor.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/network-icon-editor.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Add a network symbol to the icon.

### Network

Add a network symbol to the icon.

Parent topic:

Objects Palette

<!--NI_TOPIC bundle=g-web-development path=no-coercion.html language=enus -->
## TOPIC 00239: No Coercion

- bundle_id: `g-web-development`
- source_path: `no-coercion.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/no-coercion.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Allow the control interval to move freely.

### No Coercion

Allow the control interval to move freely.

Parent topic:

Creating User Interfaces

<!--NI_TOPIC bundle=g-web-development path=numeric-control.html language=enus -->
## TOPIC 00240: Numeric Control

- bundle_id: `g-web-development`
- source_path: `numeric-control.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/numeric-control.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Enter numeric data.

### Numeric Control

Enter numeric data.

Parent topic:

Creating User Interfaces

<!--NI_TOPIC bundle=g-web-development path=numeric-conversion.html language=enus -->
## TOPIC 00241: Numeric Conversions

- bundle_id: `g-web-development`
- source_path: `numeric-conversion.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/numeric-conversion.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `concept`
- source_description: When you wire numeric data to a node that expects a different numeric data type, the node coerces the data to the most precise type. A red coercion dot appears on the node input where the coercion takes place. In the following diagram, a red coercion dot appears on the Add node because the node expe

### Numeric Conversions

When you wire numeric data to a node that expects a different numeric data type, the node coerces the data to the most precise type.

A red coercion dot appears on the node input where the coercion takes place.

In the following diagram, a red coercion dot appears on the Add node because the node expects two inputs of matching numeric data types but receives a double-precision, floating-point number and an integer. Because input 0 (a double-precision, floating-point number) is more precise than input 1 (an unsigned, 32-bit integer), the node coerces input 1 to a double-precision, floating-point number.

[IMAGE alt='image' src='GUID-2F0C60CB-5DCA-4733-9701-AEB3A56CE4C7-a5.png']

Parent topic:

Numeric Data

Related tasks:

- Addressing Issues with Numeric Conversions

<!--NI_TOPIC bundle=g-web-development path=numeric-data.html language=enus -->
## TOPIC 00242: Numeric Data

- bundle_id: `g-web-development`
- source_path: `numeric-data.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/numeric-data.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can program using a variety of numeric data types, each with different qualities and ranges. The differences among the numeric data types are the number of bits they use to store data and the data values they represent. The following table describes the differences among the numeric data types.

### Numeric Data

You can program using a variety of numeric data types, each with different qualities and ranges. 
 The differences among the numeric data types are the number of bits they use to store data and the data values they represent.

The following table describes the differences among the numeric data types.

| Type | Description | Representation on the Diagram |
| --- | --- | --- |
| Integers | Represent whole numbers. Signed integers can be positive or negative. Use unsigned integers when you know the integer is always zero or positive. |  |
| Floating-Point Numbers | Represent fractional numbers. Double-precision floating-point numbers store more digits than single-precision floating-point numbers. |  |
| Complex Numbers | Represent a point in the complex numeric plane. Each value is comprised of two floating-point numbers, one representing the real part and the other representing the imaginary part. |  |

On the panel, you can use many types of controls and indicators to represent numeric values.

Parent topic:

Data Type Reference

<!--NI_TOPIC bundle=g-web-development path=numeric-indicator.html language=enus -->
## TOPIC 00243: Numeric Indicator

- bundle_id: `g-web-development`
- source_path: `numeric-indicator.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/numeric-indicator.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Display numeric data.

### Numeric Indicator

Display numeric data.

Parent topic:

Creating User Interfaces

<!--NI_TOPIC bundle=g-web-development path=numerics.html language=enus -->
## TOPIC 00244: Numeric Controls

- bundle_id: `g-web-development`
- source_path: `numerics.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/numerics.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Enter and display numeric data. Which Numeric Should I Use? Control Use Numeric control and indicator Enter or display numeric data. Slider Display numeric data in a vertical or horizontal slide with a customizable scale and a pointer that helps you see the exact value. Gauge Enter or display numeri

### Numeric Controls

Enter and display numeric data.

[IMAGE alt='image' src='GUID-74555973-64B7-4E3F-BEB9-6C5F34CC6707-a5.png']

#### Which Numeric Should I Use?

| Control | Use |
| --- | --- |
| Numeric control and indicator | Enter or display numeric data. |
| Slider | Display numeric data in a vertical or horizontal slide with a customizable scale and a pointer that helps you see the exact value. |
| Gauge | Enter or display numeric data in a rotary scale. |
| Tank | Display numeric data in a vertical slide that resembles a real tank or thermometer instrument. |
| Timestamp | Enter or display a time and date value. |
| Progress bars | Show progress in a vertical bar or circle. |

#### What Is the Difference between Significant Digits and Digits of Precision?

Significant digits specifies the number of significant digits to display in the numeric control.

Digits of precision specifies how many digits to display after the decimal mark.

#### How Do I Use, View, and Store Absolute Time?

Use the timestamp control to use, view, and store absolute time with high precision. This data type can accurately store 18 digits of precision in whole seconds and 19 digits of precision in fractions of a second. The timestamp control displays values in local time. However, the timestamp wire data type stores values in UTC.

Although you can use a numeric control to display timestamp values, the numeric control holds a relative quantity. The timestamp control holds an absolute quantity.

#### What Characters Do Numeric Controls Accept?

| Character(s) | Description |
| --- | --- |
| Hexadecimal digits | 0 through F |
| Octal digits | 0 through 7 |
| Binary digits | 0 and 1 |
| Decimal digits | 1, 1.0, 2, 3.5, and so on |
| . | Decimal point |
| , | Decimal comma |
| + | Positive symbol |
| - | Negative symbol |
| E or e | For scientific or engineering notation format |
| Infinity | Infinity |
| NaN | Not a number |
| / | For use in absolute time format |
| : | For use in absolute time format |
| AM, am, PM, pm | For use in absolute time format |
| SI prefixes |  |
| y | yocto (10 -24 ) |
| z | zepto (10 -21 ) |
| a | atto (10 -18 ) |
| f | femto (10 -15 ) |
| p | pico (10 -12 ) |
| n | nano (10 -9 ) |
| u | micro (10 -6 ) |
| m | milli (10 -3 ) |
| c | centi (10 -2 ) |
| d | deci (10 -1 ) |
| da | deka (10 1 ) |
| h | hecto (10 2 ) |
| k | kilo (10 3 ) |
| M | mega (10 6 ) |
| G | giga (10 9 ) |
| T | tera (10 12 ) |
| P | peta (10 15 ) |
| E | exa (10 18 ) |
| Z | zetta (10 21 ) |
| Y | yotta (10 24 ) |

Parent topic:

Creating User Interfaces

<!--NI_TOPIC bundle=g-web-development path=objects.html language=enus -->
## TOPIC 00245: Objects Palette

- bundle_id: `g-web-development`
- source_path: `objects.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/objects.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Add images related to objects to the icon.

### Objects Palette

Add images related to objects to the icon.

Parent topic:

Creating User Interfaces

<!--NI_TOPIC bundle=g-web-development path=on-connector-pane.html language=enus -->
## TOPIC 00246: On Connector Pane button duplicated

- bundle_id: `g-web-development`
- source_path: `on-connector-pane.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/on-connector-pane.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Add the terminal to or remove the terminal from the connector pane.

### On Connector Pane button duplicated

Add the terminal to or remove the terminal from the connector pane.

Parent topic:

Creating User Interfaces

<!--NI_TOPIC bundle=g-web-development path=optimize-project.html language=enus -->
## TOPIC 00247: optimize-project

- bundle_id: `g-web-development`
- source_path: `optimize-project.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/optimize-project.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `reference`
- source_description: Improves the load time and performance of your projects by loading, compiling, and saving project files during the build process. Similar to mass compiling in LabVIEW, the optimize-project command: Verifies the existence of subVIs and links them to the main VI. Updates files to the current G Web Dev

### optimize-project

Improves the load time and performance of your projects by loading,
 compiling, and saving project files during the build process.

optimize-project

- Verifies the existence of subVIs and links them to the main VI.
- Updates files to the current G Web Development Software version.
- Reports corrupt files which can prevent your project from loading correctly.

```text
gwebcli.exe optimize-project -p=<relative or absolute location of the project> -t=<time in seconds> -s=<name of target to exclude>
```

```text
gwebcli.exe optimize-project -p="C:\G Web Projects\Project.gwebproject" -t=60 -s="Default Web Server"
```

| Argument | Required | Description | Example |
| --- | --- | --- | --- |
| -p --path=VALUE | Yes | Specifies the relative or absolute path of the project to optimize.Note You can reference multiple paths in a comma-separated list. | -p="C:\\G Web Projects\\Project.gwebproject" --path=".\\Add\\Add.gwebproject, .\\Subtract\\Subtract.gwebproject" |
| -s --skipTargets=VALUE | No | Specifies which targets to exclude in the optimization process. | -s="Default Web Server" --skipTarget="Default Web Server" |
| -t --timeout=VALUE | No | Specifies the amount of time in seconds before the operation exits. | -t=10 --timeout=10 |

Parent topic:

Predefined Command Line Operations

Related information:

- Mass Compiling VIs

<!--NI_TOPIC bundle=g-web-development path=organizing-code-to-avoid-name-collisions.html language=enus -->
## TOPIC 00248: Organizing Code to Avoid Name Collisions

- bundle_id: `g-web-development`
- source_path: `organizing-code-to-avoid-name-collisions.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/organizing-code-to-avoid-name-collisions.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `task`
- source_description: A namespace is a container used to organize files into logical groups. Items in the same namespace must have a unique name. Namespaces help to prevent name collisions. Open an Application or Library document. On the document toolbar, click NewAdd namespace. Rename the namespace. Give your namespace

### Organizing Code to Avoid Name Collisions

A 
 *namespace* is a container used to organize files into logical groups. Items in the same namespace must have a unique name. Namespaces help to prevent name collisions.

1. Open an Application or Library document.
2. On the document toolbar, click 
 New»Add namespace.
3. Rename the namespace. 
 Tip Give your namespace a meaningful name to indicate that the namespace contains files of the same logical group.
4. Drag files from the project to the namespace.
5. Optional: 
 Rename the files as necessary. 
 Different namespaces can contain files that have the same name. For example, the 
 Main VI namespace and the 
 SubVI namespace in the same Application or Library document can each contain a file named 
 Function.gvi.
6. Click File»Save all.

After you build an application, each namespace corresponds to a folder in the output directory.

Parent topic:

Applications

Parent topic:

Componentizing Applications

<!--NI_TOPIC bundle=g-web-development path=package-dependencies.html language=enus -->
## TOPIC 00249: Package Dependencies

- bundle_id: `g-web-development`
- source_path: `package-dependencies.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/package-dependencies.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `concept`
- source_description: In projects, a package dependency is a package installed on the development system and used in the project. The Package Dependencies document (.sls) stores a list of packages a project uses so you can set up a development system with the required packages. With the Package Dependencies document, you

### Package Dependencies

In projects, a 
 *package dependency* is a package installed on the development system and used in the project.

Package Dependencies

.sls

- Share a project that allows a recipient to easily set up their development system with the package dependencies of the project.
- Create a project that serves as a template. Other developers can use the template project to set up their development system and begin development of the project.
- Update the list of package dependencies any time you add a package dependency to the project. Share the updated list with other developers so they can see new package dependencies you add to the project.

The Package Dependencies document is a Salt State file (.sls). For more information about Salt States, visit the SaltStack Documentation website and search for the SALT.STATE.PKG state module.

Parent topic:

Collaborating on Web Applications

Related tasks:

- Sharing a Project and Including Package Dependencies

<!--NI_TOPIC bundle=g-web-development path=package-libraries.html language=enus -->
## TOPIC 00250: Packaging a Library

- bundle_id: `g-web-development`
- source_path: `package-libraries.html`
- source_url: https://docs-be.ni.com/bundle/g-web-development/raw/resource/enus/package-libraries.html
- document_id: `g-web-development`
- page_type: `leaf`
- content_type: `task`
- source_description: Use a Package document (.lvdist) to build a library into a package or package installer. The Package document contains the build configuration and metadata, such as version, maintainer, and display name, for your package. Before you begin, create a library of source files using a Library document (.

### Packaging a Library

Use a Package document (.lvdist) to
 build a library into a package or package installer.

The Package document contains the build configuration and metadata, such as version,
 maintainer, and display name, for your package.

.gcomp

1. Click 
 File»New»Package/Installer. 
 The Package document opens in the project.
2. Drag the library or libraries you want to distribute from the Project
 Files tab to the Files section. 
 You can include applications and other support files.Note Make sure that the Destination is set to
 Public Add-ons and that the company information is filled in.
 Your libraries will be installed in G Web Development Software/addons/[company
 name]/[product name]. 
 The Package document automatically calculates the package dependencies that your
 library requires.
3. In the right rail, click Create palette
 file.
4. Use the pull-down to choose whether you will create a
 G diagram palette or a G panel palette
 library.
5. Review the contents of the Package Dependencies section, which
 displays package dependencies your library requires. 
 You can include additional dependencies by clicking Add
 dependencies and selecting packages.
6. In the Information section, confirm that the values in the
 Package document are correct. 
 The Package document automatically gathers information from the project and your NI
 User Account to complete the Information section. The values in the
 text boxes become metadata in the package. NI Package Manager reads the metadata of
 packages to sort them and display information about them to users.
7. In Output type on the Document tab,
 select Package for the output type. Select Package
 Installer if you want to create an installer that includes all of your
 packages.
8. In 
 Output directory, specify the location to save the package output.
9. Click File»Save all.
10. Click 
 Build. 
 The Build Queue tab shows the status of the
 build process.

Locate directory in File Explorer

Parent topic:

Packaging an Application or Library

Related tasks:

- Creating a Library
