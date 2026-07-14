# NI DOCUMENT BUNDLE: teststand-atml-toolkit

<!--NI_BUNDLE_CHUNK bundle=teststand-atml-toolkit start=1 end=52 -->
<!--NI_TOPIC bundle=teststand-atml-toolkit path=atml-td-schema-file-data-types-using-teststan.html language=enus -->
## TOPIC 00001: ATML TD Schema File Data Types - Using TestStand Type Palette Files with the TD Translator

- bundle_id: `teststand-atml-toolkit`
- source_path: `atml-td-schema-file-data-types-using-teststan.html`
- source_url: https://docs-be.ni.com/bundle/teststand-atml-toolkit/raw/resource/enus/atml-td-schema-file-data-types-using-teststan.html
- document_id: `teststand-atml-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: ATML TD Schema File Data TypesThe ATMLTDTypes type palette, located at <TestStand Public>\Components\TypePalettes\ATMLTDTypes.ini, contains the TestStand data type equivalents for the types the TestDescription.xsd, Common.xsd, DatumTypes.xsd, Operations.xsd, IeeeStd1641.xsd, and HardwareCommon.xsd A

### ATML TD Schema File Data Types - Using
 TestStand Type Palette Files with the TD Translator

#### ATML TD Schema File Data Types

The
 ATMLTDTypes type palette, located at
 <TestStand Public>\Components\TypePalettes\ATMLTDTypes.ini,
 contains the TestStand data type equivalents for the types the
 TestDescription.xsd, Common.xsd,
 DatumTypes.xsd, Operations.xsd,
 IeeeStd1641.xsd, and
 HardwareCommon.xsd ATML TD schema files
 define.

TestStand always loads the ATMLTDTypes.ini type
 palette when you launch the TestStand Sequence Editor.

ATMLTDTypes.ini

NI_ATML

Note

Parent topic:

Using TestStand Type Palette Files with the TD Translator

Related concepts:

- IEEE 1641 Specification Data Types - Using TestStand Type Palette Files with the TD Translator

<!--NI_TOPIC bundle=teststand-atml-toolkit path=atml-td-standards-146.html language=enus -->
## TOPIC 00002: ATML TD Standards

- bundle_id: `teststand-atml-toolkit`
- source_path: `atml-td-standards-146.html`
- source_url: https://docs-be.ni.com/bundle/teststand-atml-toolkit/raw/resource/enus/atml-td-standards-146.html
- document_id: `teststand-atml-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The IEEE Standards Coordinating Committee 20 (SCC20) directs the development of ATML standards for exchanging the following Unit Under Test (UUT) test and diagnostic information among components of a test system: Design data Test strategies Test requirements Test procedures Test results management T

### ATML TD Standards

The IEEE Standards Coordinating Committee 20 (SCC20) directs the development of ATML standards
 for exchanging the following Unit Under Test (UUT) test and diagnostic information among
 components of a test system:

- Design data
- Test strategies
- Test requirements
- Test procedures
- Test results management
- Test system implementations

The IEEE Std 1671 standard defines the ATML framework and specifies a set of common XML formats.
 Related standards specify XML formats for exchanging various categories of UUT test and
 diagnostic information. The ATML Test Description (TD) standard, IEEE Std 1671.1,
 specifies the XML format for exchanging the TD information.

Use the ATML TD standard and its associated standards to identify and document the descriptions
 of tests that can be used to implement a test program to test a UUT.

#### Schema Files

The ATML standards use XML
 schemas to specify formats. The
 <TestStand>\Components\Translators\ATMLTDTranslator\Schemas
 directory contains the following XML schemas the IEEE Std 1671 and IEEE Std 1671.1
 (1.01 and 3.0) standards define:

- TestDescription.xsd
- Common.xsd
- HardwareCommon.xsd
- DatumTypes.xsd
- Operations.xsd
- IeeeStd1641.xsd

ATML TD instance documents can also refer to the following XML schemas related
 to the IEEE Std 1641 standard and also located in the
 <TestStand>\Components\Translators\ATMLTDTranslator\Schemas
 directory:

- STDBSC.xsd
- STDTSF.xsd
- STDTSFLib.xsd

Refer to the IEEE standards listed below for more information about the
 definition and use of elements these schemas define.

#### For More Information

Refer to the
 following documents on the IEEE Website for more information about the ATML TD
 standard:

- IEEE Std 1671 —IEEE Standard for Automatic Test Markup
 Language (ATML) for Exchanging Automatic Test Equipment and Test Information via
 XML
- IEEE Std 1671.1 —IEEE Standard for Automatic Test Markup
 Language (ATML) for Exchanging Automatic Test Equipment and Test Information via
 XML: Exchanging Test Descriptions
- IEEE Std 1671.3 —IEEE Standard for Automatic Test Markup
 Language (ATML) for Exchanging Automatic Test Information via XML (eXtensible
 Markup Language): Exchanging UUT (Unit-Under-Test) Description Information
- IEEE Std 1641 —IEEE Standard for Signal and Test
 Definition

Parent topic:

TestStand ATML Toolkit Help

<!--NI_TOPIC bundle=teststand-atml-toolkit path=calling-a-labwindows-cvi-custom-code-generato.html language=enus -->
## TOPIC 00003: Calling a LabWindows/CVI Custom Code Generator dll during an Incremental Update

- bundle_id: `teststand-atml-toolkit`
- source_path: `calling-a-labwindows-cvi-custom-code-generato.html`
- source_url: https://docs-be.ni.com/bundle/teststand-atml-toolkit/raw/resource/enus/calling-a-labwindows-cvi-custom-code-generato.html
- document_id: `teststand-atml-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The example located in the <TestStand Public>\Examples\Toolkits\ATMLTDTranslator\Code Generator\CVI directory demonstrates how the ATML TD translator uses a custom code generator dll to incrementally update LabWindows/CVI code modules.Complete the following steps to use the example: Complete the ste

### Calling a LabWindows/CVI Custom Code Generator
 dll during an Incremental Update

The example located in the
 <TestStand Public>\Examples\Toolkits\ATMLTDTranslator\Code
 Generator\CVIdirectory demonstrates how the ATML TD translator uses a
 custom code generator dll to incrementally update LabWindows/CVI
 code modules.

Complete the following steps to use the example:

1. Complete the steps in the Recommended LabWindows/CVI Function Prototypes tutorial
 to translate
 <TestStand Public>\Examples\Toolkits\ATMLTDTranslator\Translator\Test
 Description 1.0\Computer 1.0.xml , which is an ATML TD instance
 document, to a TestStand sequence file and a set of LabWindows/CVI code modules
 using a LabWindows/CVI custom code generator dll .
2. In LabWindows/CVI, open
 <TestStand Public>\Examples\Toolkits\ATMLTDTranslator\Code
 Generator\CVI\CVICodeGenerator.prj .
3. Build the project to generate the dll .
4. In TestStand, select Tools»Configure ATML TD Translator to launch the ATML Test Description Translator
 Configuration dialog box.
5. Click the General Settings tab and enable the Update Sequence
 File option.
6. Click the Code Module Settings tab and enable the
 LabWindows/CVI option.
7. Click the Browse button next to the Path to the Custom Code
 Generator DLL control and browse to the path of the
 dll you built in Step 3.
8. Click OK to close the ATML Test Description Translator
 Configuration dialog box.
9. Close all open sequence files.
10. Select File»Open File to launch the File Open dialog box.
11. Browse to <TestStand Public>\Examples\Toolkits\ATMLTDTranslator\Translator\Test
 Description 1.0\Computer 1.0 - Update.xml .
12. Click Open . The Update Options dialog box
 launches.
13. Enable the Use the Selected File to Update option and click the
 Browse button to select the
 Computer.seq sequence file you created in the
 Recommended LabWindows/CVI Function Prototypes section. The
 translator updates the existing sequence file and the LabWindows/CVI code modules it
 had previously created.

Parent topic:

Implementing a LabWindows/CVI Custom Code Generator

Related concepts:

- Incrementally Updating a Translated Sequence File
- Recommended LabWindows/CVI Function Prototypes

<!--NI_TOPIC bundle=teststand-atml-toolkit path=calling-labview-custom-code-generator-vis-dur.html language=enus -->
## TOPIC 00004: Calling LabVIEW Custom Code Generator VIs during an Incremental Update

- bundle_id: `teststand-atml-toolkit`
- source_path: `calling-labview-custom-code-generator-vis-dur.html`
- source_url: https://docs-be.ni.com/bundle/teststand-atml-toolkit/raw/resource/enus/calling-labview-custom-code-generator-vis-dur.html
- document_id: `teststand-atml-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The example located in the <TestStand Public>\Examples\Toolkits\ATMLTDTranslator\Code Generator\LabVIEW directory demonstrates how the ATML TD translator uses custom code generator VIs to incrementally update LabVIEW code modules.Complete the following steps to use the example: Complete the steps in

### Calling LabVIEW Custom Code Generator VIs
 during an Incremental Update

The example located in the
 <TestStand Public>\Examples\Toolkits\ATMLTDTranslator\Code
 Generator\LabVIEW directory demonstrates how the ATML TD translator uses
 custom code generator VIs to incrementally update LabVIEW code modules.

Complete the following steps to use the example:

1. Complete the steps in the Example LabVIEW Custom Code Generator VIs tutorial to translate
 <TestStand Public>\Examples\Toolkits\ATMLTDTranslator\Translator\Test
 Description 1.0\Computer 1.0.xml , which is an ATML TD instance
 document, to a TestStand sequence file and a set of LabVIEW code modules using the
 LabVIEW custom code generator VIs.
2. Select Tools»Configure ATML TD Translator to launch the ATML
 Test Description Translator Configuration dialog box.
3. Click the General Settings tab and enable the Update Sequence
 File option.
4. Click the Code Module Settings tab and enable the
 LabVIEW option.
5. Click the Browse button next to the Directory that Contains
 the Custom Code Generator VIs control and browse to
 <TestStand Public>\Examples\Toolkits\ATMLTDTranslator\Code
 Generator\LabVIEW .
6. Click OK to close the ATML Test Description Translator
 Configuration dialog box.
7. Close all open sequence files.
8. Select File»Open File to launch the File Open dialog box.
9. Browse to <TestStand Public>\Examples\Toolkits\ATMLTDTranslator\Translator\Test
 Description 1.0\Computer 1.0.xml .
10. Click Open . The Update Options dialog box launches.
11. Enable the Use the Selected File to Update option and click the
 Browse button to select the
 Computer.seq sequence file you created in the Example
 LabVIEW Custom Code Generator VIs tutorial. The translator updates the existing
 sequence file and the LabVIEW code modules it had previously created.

Parent topic:

Implementing a LabVIEW Custom Code Generator

Related concepts:

- Incrementally Updating a Translated Sequence File
- Example LabVIEW Custom Code Generator VIs

<!--NI_TOPIC bundle=teststand-atml-toolkit path=completing-the-partial-test-program-188.html language=enus -->
## TOPIC 00005: Completing the Partial Test Program

- bundle_id: `teststand-atml-toolkit`
- source_path: `completing-the-partial-test-program-188.html`
- source_url: https://docs-be.ni.com/bundle/teststand-atml-toolkit/raw/resource/enus/completing-the-partial-test-program-188.html
- document_id: `teststand-atml-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The ATML TD schema defines a number of elements that the ATML TD translator cannot directly translate to constructs in TestStand or logic in LabVIEW or LabWindows/CVI code modules. By default, the translator stores the elements it cannot directly translate as comments or TestStand attributes in vari

### Completing the Partial Test Program

The ATML TD schema defines a number of elements that the ATML TD translator cannot directly
 translate to constructs in TestStand or logic in LabVIEW or LabWindows/CVI code modules.
 By default, the translator stores the elements it cannot directly translate as comments
 or TestStand attributes in various places in the translated sequence file and code
 modules.

The collection of a commented sequence file and code modules is a partial test program.

The post-translation recommended actions section of the log file lists the elements the
 translator translates but cannot implement and describes how you must implement the
 required functionality to complete the test program the source TD instance document
 originally described.

You can manually implement the operations and logic the comments in the sequence file and code
 modules describe. Because the elements translated as attribute containers or comments do
 not correspond to specific TestStand constructs, you can use a custom solution, such as
 a custom step type in TestStand, to implement the missing operations and logic.

Alternatively, you can use the custom code generator callbacks during translation to
 programatically translate the code module comments to code that implements the logic
 required to complete the test program.

Sections that contain the Completing the Partial Test
 Program icon ([IMAGE alt='image' src='GUID-5D8EF323-6138-4253-8059-68EE3E52E461-a5.gif']) describe how the
 translator stores information for elements that it cannot
 translate. It also provides information on how you can manually
 implement the logic that these untranslatable elements
 describe.

Parent topic:

Translating a TD Instance Document to a TestStand Sequence File

Related concepts:

- Creating LabVIEW Code Modules for Behavior Elements
- Creating LabWindows/CVI Code Modules for Behavior Elements
- Post-Translation Recommended Actions Section - Logging Translation Information
- Logging Translation Information
- Generating Complete Code Modules Using a Custom Code Generator

<!--NI_TOPIC bundle=teststand-atml-toolkit path=creating-a-dll-for-a-labwindows-cvi-custom-co.html language=enus -->
## TOPIC 00006: Creating a dll for a LabWindows/CVI Custom Code Generator

- bundle_id: `teststand-atml-toolkit`
- source_path: `creating-a-dll-for-a-labwindows-cvi-custom-co.html`
- source_url: https://docs-be.ni.com/bundle/teststand-atml-toolkit/raw/resource/enus/creating-a-dll-for-a-labwindows-cvi-custom-co.html
- document_id: `teststand-atml-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can create a dll that contains the functions for a LabWindows/CVI custom code generator and use the dll you create as a starting point for customizing the code generator behavior. When you create a function in a C file to implement a custom code generator callback, the function must use the same

### Creating a dll for a LabWindows/CVI Custom
 Code Generator

dll

dll

Note

CodeGenerator_PreTranslateAction()

dll

dll

Note

<TestStand Public>\Examples\Toolkits\ATMLTDTranslator\Code
 Generator\LabVIEW

1. Select Project from Template in the New section of
 the LabWindows/CVI welcome page, or select File»New»Project From Template in LabWindows/CVI to launch the New Project From
 Template dialog box.
2. In the template type control, select Dynamic-Link Library .
3. Specify a name, directory, and path for the LabWindows/CVI project in the Project name , Project folder , and Project path controls, respectively.
4. Click OK to create the project and source files and close the
 New Project From Template dialog box. A new
 Workspace window opens in LabWindows/CVI.
5. Use the recommended LabWindows/CVI function prototype or Visual C++ function prototype to
 implement the body of the function for the callback. Refer to the LabWindows/CVI
 project and source files located in the
 <TestStand Public>\Examples\Toolkits\ATMLTDTranslator\Code
 Generator\CVI directory for examples of how to implement callbacks in
 a LabWindows/CVI dll . Note You must expose the prototype of
 each callback as __stdcall in the
 dll.
6. Select Build»Create Debuggable Dynamic Link Library to build the LabWindows/CVI project.
7. Complete the following steps to configure the ATML TD translator to call the
 dll you created as a LabWindows/CVI custom code generator:
  1. In TestStand, select Tools»Configure ATML TD Translator to launch the ATML Test Description Translator
 Configuration dialog box.
  2. Click the Code Module Settings tab and enable the
 LabWindows/CVI option.
  3. In the Path to Custom Code Generator DLL control,
 enter or browse to the complete path for the path you specified in Step
 3.

Parent topic:

Implementing a LabWindows/CVI Custom Code Generator

Related concepts:

- Implementing a LabWindows/CVI Custom Code Generator
- Recommended LabWindows/CVI Function Prototypes
- Recommended Microsoft Visual C++ Function Prototypes

<!--NI_TOPIC bundle=teststand-atml-toolkit path=creating-a-vi-for-a-labview-custom-code-gener.html language=enus -->
## TOPIC 00007: Creating a VI for a LabVIEW Custom Code Generator

- bundle_id: `teststand-atml-toolkit`
- source_path: `creating-a-vi-for-a-labview-custom-code-gener.html`
- source_url: https://docs-be.ni.com/bundle/teststand-atml-toolkit/raw/resource/enus/creating-a-vi-for-a-labview-custom-code-gener.html
- document_id: `teststand-atml-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can recreate an example VI for a LabVIEW custom code generator and use the VI you create as a starting point for customizing the code generator behavior. When you create a VI to implement a custom code generator callback, the VI must use the same filename as the example VI that implements the sa

### Creating a VI for a LabVIEW Custom Code
 Generator

Note

CodeGenerator_PreTranslateAction.vi

Note

<TestStand Public>\Examples\Toolkits\ATMLTDTranslator\Code
 Generator\LabVIEW

1. Create a directory.
2. In LabVIEW, create a new VI and save it in the directory you created in step 1. Ensure the VI
 name matches the name of an example custom code generator VI. For example, if you
 want to implement and customize the PreTranslateAction callback, save the VI as
 CodeGenerator_PreTranslateAction.vi
3. Create controls to match the example VI for the callback you want to implement. For example, if
 you are recreating the PreTranslateAction callback, you must connect the following
 controls:
4. TranslatorCodeGenerator —Automation Refnum control that uses the TranslatorCodeGenerator
 interface.
5. CodeGenerator —Automation Refnum control that uses the LVCodeGenerator interface.
6. DOMNode —Automation Refnum control that uses the MSXML DOM Node of the
 <Action> element.
7. Implement the code required to call the corresponding callback and generate the code modules.
 Refer to the VIs located in the
 <TestStand Public>\Examples\Toolkits\ATMLTDTranslator\Code
 Generator\LabVIEW directory for examples of how to implement
 callbacks in VIs.
8. Save the VI.
9. Complete the following steps to configure the ATML TD translator to call the VI you created as a LabVIEW custom code generator.
  1. In TestStand, select Tools»Configure ATML TD Translator to launch the
 ATML Test Description Translator Configuration 
 dialog box.
  2. Click the Code Module Settings tab and enable the
 LabVIEW option.
  3. In the Directory that Contains the Custom Code Generator VIs control,
 enter or browse to the complete path for the directory you created in step
 1.

Parent topic:

Implementing a LabVIEW Custom Code Generator

Related concepts:

- Example LabVIEW Custom Code Generator VIs
- Implementing a LabVIEW Custom Code Generator

<!--NI_TOPIC bundle=teststand-atml-toolkit path=creating-labview-code-modules-for-behavior-el.html language=enus -->
## TOPIC 00008: Creating LabVIEW Code Modules for Behavior Elements

- bundle_id: `teststand-atml-toolkit`
- source_path: `creating-labview-code-modules-for-behavior-el.html`
- source_url: https://docs-be.ni.com/bundle/teststand-atml-toolkit/raw/resource/enus/creating-labview-code-modules-for-behavior-el.html
- document_id: `teststand-atml-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The ATML TD translator creates a LabVIEW VI using the path you specified in the LabVIEW VI Path control on the Code Module Settings tab of the ATML Test Description Translator Configuration dialog box and creates block diagram labels that begin with the string <ATMLTranslatorComment> for the <Automa

### Creating LabVIEW Code Modules for Behavior
 Elements

The ATML TD translator creates a LabVIEW VI using the path you specified in the LabVIEW VI Path
 control on the Code Module Settings tab of the ATML
 Test Description Translator Configuration dialog box and creates block
 diagram labels that begin with the string <ATMLTranslatorComment>
 for the <AutomaticGeneration>,
 <Description>, <Extension>,
 <IeeeStd1641>, and <Operations> child
 elements of the <Behavior> element.

#### Completing the Partial Test
 Program
 [IMAGE alt='image' src='GUID-5D8EF323-6138-4253-8059-68EE3E52E461-a5.gif']

You must manually implement the
 logic that the <AutomaticGeneration>,
 <Description>, <Extension>,
 <IeeeStd1641>, and <Operations>
 elements describe. Refer to the *Post-Translation Recommended Actions*
 section of the log file for more information about the elements you must
 implement.

If a VI already exists at the path you specified and the VI has a
 name that matches the value of the name attribute of the parent
 <Action> element, the translator updates existing block
 diagram labels in the VI. If the VI does not exist, the translator creates a new
 VI.

The translator configures the VI as the code module for the step and names
 the VI using the same name as the name attribute of the parent
 <Action> element. The translator configures the path of
 the VI to be relative to the sequence file.

The translator passes parameters
 as local variables or as a single container to the LabVIEW code
 module.

#### Incremental Update
 [IMAGE alt='image' src='GUID-10242244-39C8-44B3-AAC3-6C5701803D28-a5.gif']

The translator incrementally updates
 existing block diagram labels that correspond to the
 <AutomaticGeneration>,
 <Description>, <Extension>,
 <IeeeStd1641>, and <Operations>
 child elements of the <Behavior> element, as the following
 table describes.

Note

| Change in Source TD Instance Document | Change in VI |
| --- | --- |
| You modify the <AutomaticGeneration>, <Description>, <Extension>, or <IeeeStd1641> child element of the <Behavior> element. | The translator updates the block diagram label that corresponds to the element you modified to use the new XML from the source TD instance document. |
| You delete a child element of the <Behavior> element in the source TD instance document and insert a different child element of the <Behavior> element. For example, you delete a <Description> child element and insert an <Operations> child element. | The translator deletes the block diagram label that corresponds to the element you deleted and creates a new block diagram label for the element you created. |
| You add or modify a <Behavior>/<Operations>/<Operation> element. | The translator adds or modifies the block diagram label that corresponds to the <Operation> element you added or modified. |
| You delete any <Behavior>/<Operations>/<Operation> element. | The translator deletes the block diagram label that corresponds to the <Operation> element you deleted from the source TD instance document. |

Note

<ATMLTranslatorComment>

Delete
 Previously Generated Sequence File and Code Module Constructs

General Settings

ATML Test
 Description Translator Configuration

Parent topic:

TestStand ATML Toolkit Help

Related concepts:

- Post-Translation Recommended Actions Section - Logging Translation Information
- Logging Translation Information
- Passing Parameters to LabVIEW Code Modules

<!--NI_TOPIC bundle=teststand-atml-toolkit path=creating-labview-code-modules-for-behavior-el2.html language=enus -->
## TOPIC 00009: Creating LabVIEW Code Modules for Behavior Elements

- bundle_id: `teststand-atml-toolkit`
- source_path: `creating-labview-code-modules-for-behavior-el2.html`
- source_url: https://docs-be.ni.com/bundle/teststand-atml-toolkit/raw/resource/enus/creating-labview-code-modules-for-behavior-el2.html
- document_id: `teststand-atml-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The ATML TD translator creates a LabVIEW VI using the path you specified in the LabVIEW VI Path control on the Code Module Settings tab of the ATML Test Description Translator Configuration dialog box and creates block diagram labels that begin with the string <ATMLTranslatorComment> for the <Automa

### Creating LabVIEW Code Modules for Behavior
 Elements

The ATML TD translator creates a LabVIEW VI using the path you specified in the LabVIEW VI Path
 control on the Code Module Settings tab of the ATML
 Test Description Translator Configuration dialog box and creates block
 diagram labels that begin with the string <ATMLTranslatorComment>
 for the <AutomaticGeneration>,
 <Description>, <Extension>,
 <IeeeStd1641>, and <Operations> child
 elements of the <Behavior> element.

#### Completing the Partial Test
 Program
 [IMAGE alt='image' src='GUID-5D8EF323-6138-4253-8059-68EE3E52E461-a5.gif']

You must manually implement the
 logic that the <AutomaticGeneration>,
 <Description>, <Extension>,
 <IeeeStd1641>, and <Operations>
 elements describe. Refer to the *Post-Translation Recommended Tests*
 section of the log file for more information about the elements you must
 implement.

If a VI already exists at the path you specified and the VI has a
 name that matches the value of the name attribute of the parent
 <Test> element, the translator updates existing block
 diagram labels in the VI. If the VI does not exist, the translator creates a new
 VI.

The translator configures the VI as the code module for the step and names
 the VI using the same name as the name attribute of the parent
 <Test> element. The translator configures the path of the
 VI to be relative to the sequence file.

The translator passes parameters as
 local variables or as a single container to the LabVIEW code module.

#### Incremental Update
 [IMAGE alt='image' src='GUID-10242244-39C8-44B3-AAC3-6C5701803D28-a5.gif']

The translator incrementally updates
 existing block diagram labels that correspond to the
 <AutomaticGeneration>,
 <Description>, <Extension>,
 <IeeeStd1641>, and <Operations>
 child elements of the <Behavior> element, as the following
 table describes.

Note

| Change in Source TD Instance Document | Change in VI |
| --- | --- |
| You modify the <AutomaticGeneration>, <Description>, <Extension>, or <IeeeStd1641> child element of the <Behavior> element. | The translator updates the block diagram label that corresponds to the element you modified to use the new XML from the source TD instance document. |
| You delete a child element of the <Behavior> element in the source TD instance document and insert a different child element of the <Behavior> element. For example, you delete a <Description> child element and insert an <Operations> child element. | The translator deletes the block diagram label that corresponds to the element you deleted and creates a new block diagram label for the element you created. |
| You add or modify a <Behavior>/<Operations>/<Operation> element. | The translator adds or modifies the block diagram label that corresponds to the <Operation> element you added or modified. |
| You delete any <Behavior>/<Operations>/<Operation> element. | The translator deletes the block diagram label that corresponds to the <Operation> element you deleted from the source TD instance document. |

Note

<ATMLTranslatorComment>

Delete
 Previously Generated Sequence File and Code Module Constructs

General Settings

ATML Test
 Description Translator Configuration

Parent topic:

TestStand ATML Toolkit Help

Related concepts:

- Post-Translation Recommended Actions Section - Logging Translation Information
- Logging Translation Information
- Passing Parameters to LabVIEW Code Modules

<!--NI_TOPIC bundle=teststand-atml-toolkit path=creating-labwindows-cvi-code-modules-for-beha.html language=enus -->
## TOPIC 00010: Creating LabWindows/CVI Code Modules for Behavior Elements

- bundle_id: `teststand-atml-toolkit`
- source_path: `creating-labwindows-cvi-code-modules-for-beha.html`
- source_url: https://docs-be.ni.com/bundle/teststand-atml-toolkit/raw/resource/enus/creating-labwindows-cvi-code-modules-for-beha.html
- document_id: `teststand-atml-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The ATML TD translator creates a LabWindows/CVI project using the path you specified in the LabWindows/CVI Project File Path control on the Code Module Settings tab of the ATML Test Description Translator Configuration dialog box and adds the generated source file, header file, and default TestStand

### Creating LabWindows/CVI Code Modules for
 Behavior Elements

The ATML TD translator creates a LabWindows/CVI project using the path you specified in the
 LabWindows/CVI Project File Path control on the Code Module
 Settings tab of the ATML Test Description Translator
 Configuration dialog box and adds the generated source file, header
 file, and default TestStand instrument files to the project. The translator configures
 the paths of the LabWindows/CVI project file, source file, and the DLL as relative paths
 in the generated TestStand step.

The translator creates a LabWindows/CVI source file, creates a function for each
 <Test> parent element, names the function using the
 name attribute of the <Test> element, and
 inserts the function in the LabWindows/CVI code module. The translator then creates
 comments that begin with the string <ATMLTranslatorComment> for
 the <AutomaticGeneration>, <Description>,
 <Extension>, <IeeeStd1641>, or
 <Operations> child elements of the
 <Behavior> element and adds the comments to the function.

#### Completing the Partial Test
 Program
 [IMAGE alt='image' src='GUID-5D8EF323-6138-4253-8059-68EE3E52E461-a5.gif']

You must manually implement the
 logic that the <AutomaticGeneration>,
 <Description>, <Extension>,
 <IeeeStd1641>, and <Operations>
 elements describe. Refer to the *Post-Translation Recommended Tests*
 section of the log file for more information about the elements you must
 implement.

The translator configures the path of the DLL project to be
 relative to the sequence file. The translator passes all the
 <Parameters>, and <TestResults>
 elements of the corresponding <Test> element to the
 function.

Caution

If a source file already exists at the path you specified and the file contains a
 function with a name that matches the value of the name attribute
 of the parent <Test> element, the translator updates existing
 comments in the function. If the function does not exist, the translator creates a
 new source file.

#### Incremental Update
 [IMAGE alt='image' src='GUID-10242244-39C8-44B3-AAC3-6C5701803D28-a5.gif']

The translator incrementally updates
 existing comments that correspond to the
 <AutomaticGeneration>,
 <Description>, <Extension>,
 <IeeeStd1641>, and <Operations>
 child elements of the <Behavior> element, as the following
 table describes.

Note

| Change in Source TD Instance Document | Incremental Update Behavior |
| --- | --- |
| You modify the <AutomaticGeneration>, <Description>, <Extension>, or <IeeeStd1641> child element of the <Behavior> element. | The translator updates the function comment that corresponds to the element you modified to use the new XML from the source TD instance document. |
| You delete a child element of the <Behavior> element in the source TD instance document and insert a different child element of the <Behavior> element. For example, you delete a <Description> child element and insert an <Operations> child element. | The translator deletes the function comment that corresponds to the element you deleted and creates a new function comment for the element you created. |
| You add or modify a <Behavior>/<Operations>/<Operation> element. | The translator adds or modifies the function comment that corresponds to the <Operation> element you added or modified. |
| You delete any <Behavior>/<Operations>/<Operation> element. | The translator deletes the function comment that corresponds to the <Operation> element you deleted from the source TD instance document. |

Note

<ATMLTranslatorComment>

Delete Previously Generated
 Sequence File and Code Module Constructs

General Settings

ATML Test
 Description Translator Configuration

Parent topic:

TestStand ATML Toolkit Help

Related concepts:

- Post-Translation Recommended Actions Section - Logging Translation Information
- Logging Translation Information
- Passing Parameters to LabWindows/CVI Code Modules

<!--NI_TOPIC bundle=teststand-atml-toolkit path=creating-labwindows-cvi-code-modules-for-beha2.html language=enus -->
## TOPIC 00011: Creating LabWindows/CVI Code Modules for Behavior Elements

- bundle_id: `teststand-atml-toolkit`
- source_path: `creating-labwindows-cvi-code-modules-for-beha2.html`
- source_url: https://docs-be.ni.com/bundle/teststand-atml-toolkit/raw/resource/enus/creating-labwindows-cvi-code-modules-for-beha2.html
- document_id: `teststand-atml-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The ATML TD translator creates a LabWindows/CVI project using the path you specified in the LabWindows/CVI Project File Path control on the Code Module Settings tab of the ATML Test Description Translator Configuration dialog box and adds the generated source file, header file, and default TestStand

### Creating LabWindows/CVI Code Modules for
 Behavior Elements

The ATML TD translator creates a LabWindows/CVI project using the path you specified in the
 LabWindows/CVI Project File Path control on the
 Code Module Settings tab of the ATML Test
 Description Translator Configuration dialog box and adds the generated
 source file, header file, and default TestStand instrument files to the project. The
 translator configures the paths of the LabWindows/CVI project file, source file, and the
 DLL as relative paths in the generated TestStand step.

The translator creates a LabWindows/CVI source file, creates a function for each
 <Action> parent element, names the function using the
 name attribute of the <Action> element, and
 inserts the function in the LabWindows/CVI code module. The translator then creates
 comments that begin with the string <ATMLTranslatorComment> for
 the <AutomaticGeneration>, <Description>,
 <Extension>, <IeeeStd1641>, or
 <Operations> child elements of the
 <Behavior> element and adds the comments to the function.

#### Completing the Partial Test
 Program
 [IMAGE alt='image' src='GUID-5D8EF323-6138-4253-8059-68EE3E52E461-a5.gif']

You must manually implement the
 logic that the <AutomaticGeneration>,
 <Description>, <Extension>,
 <IeeeStd1641>, and <Operations>
 elements describe. Refer to the *Post-Translation Recommended Actions*
 section of the log file for more information about the elements you must
 implement.

The translator configures the path of the DLL project to be
 relative to the sequence file. The translator passes all the
 <Parameters>, <TestResults>, and
 <SessionData> elements of the corresponding
 <Action> element to the function.

Caution

If a source file already exists at the path you specified and the file contains a
 function with a name that matches the value of the name attribute
 of the parent <Action> element, the translator updates
 existing comments in the function. If the function does not exist, the translator
 creates a new source file.

#### Incremental Update
 [IMAGE alt='image' src='GUID-10242244-39C8-44B3-AAC3-6C5701803D28-a5.gif']

The translator incrementally updates
 existing comments that correspond to the
 <AutomaticGeneration>,
 <Description>, <Extension>,
 <IeeeStd1641>, and <Operations>
 child elements of the <Behavior> element, as the following
 table describes.

Note

| Change in Source TD Instance Document | Incremental Update Behavior |
| --- | --- |
| You modify the <AutomaticGeneration>, <Description>, <Extension>, or <IeeeStd1641> child element of the <Behavior> element. | The translator updates the function comment that corresponds to the element you modified to use the new XML from the source TD instance document. |
| You delete a child element of the <Behavior> element in the source TD instance document and insert a different child element of the <Behavior> element. For example, you delete a <Description> child element and insert an <Operations> child element. | The translator deletes the function comment that corresponds to the element you deleted and creates a new function comment for the element you created. |
| You add or modify a <Behavior>/<Operations>/<Operation> element. | The translator adds or modifies the function comment that corresponds to the <Operation> element you added or modified. |
| You delete any <Behavior>/<Operations>/<Operation> element. | The translator deletes the function comment that corresponds to the <Operation> element you deleted from the source TD instance document. |

Note

<ATMLTranslatorComment>

Delete Previously Generated
 Sequence File and Code Module Constructs

General Settings

ATML Test
 Description Translator Configuration

Parent topic:

TestStand ATML Toolkit Help

Related concepts:

- Post-Translation Recommended Actions Section - Logging Translation Information
- Logging Translation Information
- Passing Parameters to LabWindows/CVI Code Modules

<!--NI_TOPIC bundle=teststand-atml-toolkit path=custom-code-generator-api-38.html language=enus -->
## TOPIC 00012: Custom Code Generator API

- bundle_id: `teststand-atml-toolkit`
- source_path: `custom-code-generator-api-38.html`
- source_url: https://docs-be.ni.com/bundle/teststand-atml-toolkit/raw/resource/enus/custom-code-generator-api-38.html
- document_id: `teststand-atml-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The ATML Toolkit includes custom code generator API classes, properties, methods, and enumerations that you can use when implementing the code generator functionality.For example, if you want to implement the PreTranslateAction callback in LabVIEW and you want to obtain the path of the code module t

### Custom Code Generator API

The ATML Toolkit includes custom code generator API classes, properties, methods, and
 enumerations that you can use when implementing the code generator functionality.

For example, if you want to implement the PreTranslateAction callback in LabVIEW and you want to
 obtain the path of the code module the translator generates so that you can modify the
 code module, you can use the CodeGenerator_PreTranslateAction VI,
 which requires a CodeGenerator control connected to the connector pane. The
 CodeGenerator control is an Automation Refnum control that uses the LVCodeGenerator
 interface of the custom code generator API. You can use the
 LVCodeGenerator.CodeModulePath property to obtain the absolute file path of the
 generated code module.

Parent topic:

Generating Complete Code Modules Using a Custom Code Generator

Related concepts:

- Example LabVIEW Custom Code Generator VIs
- Generating Complete Code Modules Using a Custom Code Generator

<!--NI_TOPIC bundle=teststand-atml-toolkit path=deleting-sequence-file-and-code-module-constr.html language=enus -->
## TOPIC 00013: Deleting Sequence File and Code Module Constructs when Incrementally Updating a Sequence File

- bundle_id: `teststand-atml-toolkit`
- source_path: `deleting-sequence-file-and-code-module-constr.html`
- source_url: https://docs-be.ni.com/bundle/teststand-atml-toolkit/raw/resource/enus/deleting-sequence-file-and-code-module-constr.html
- document_id: `teststand-atml-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: In some cases when incrementally updating a sequence file and code modules, you might want to retain customizations you made to sequence file constructs created during the previous translation. This way you can copy the customizations from the previous construct to the updated construct, such as: st

### Deleting Sequence File and Code Module
 Constructs when Incrementally Updating a Sequence File

In some cases when incrementally updating a sequence file and code modules, you might want to
 retain customizations you made to sequence file constructs created during the previous
 translation. This way you can copy the customizations from the previous construct to the
 updated construct, such as:

- steps
- sequences
- local variables
- code module constructs:
  - comments
  - parameters
  - controls
  - indicators

Use the Delete Previously Generated Sequence File and Code Module
 Constructs option on the General Settings tab of
 the ATML Test Description Translator Configuration dialog box to
 specify whether the translator retains or deletes previously created constructs.

When you enable this option, the ATML TD translator deletes TestStand steps, sequences, and local
 variables and block diagram labels in LabVIEW code modules or function comments in
 LabWindows/CVI code modules created during the previous translation. The translator
 deletes these items when incrementally updating a sequence file if you have deleted the
 corresponding elements from the source TD instance document, as shown in the following
 table.

When you disable this option, the translator retains TestStand steps, sequences, local variables,
 block diagram labels and function comments in LabWindows/CVI code modules when
 incrementally updating a sequence file. It retains the constructs even if you have
 deleted the corresponding elements from the source TD instance document. The translator
 deletes in the retained TestStand constructs the attributes previously created for the
 attributes of translated elements in the source TD instance document.

For comments in retained code modules, the translator deletes from the comments the
 <ATMLTranslatorComment> and
 </ATMLTranslatorComment> tags previously created for some
 child elements of the <Action> and
 <Behavior> elements.

| Change in Source TD Instance Document | Constructs Deleted in Sequence File |
| --- | --- |
| You delete a <Step> child element of a <TestGroup> element of the TestGroupSequence type, or child element of a <Sequence> element. | The TestStand step that corresponds to the deleted <Step> element and the local variables TestStand passes to the code module for the step. |
| You delete an <ActionReference> or a <Step> child element of a <TestGroup> element of the TestGroupSerial, TestGroupUnspecifiedOrder, or TestGroupDiagnosticModel type, or a child element of a <Serial>, Parallel, UnspecifiedOrder, or Diagnostoc element. | The TestStand step that corresponds to the deleted <ActionReference> element and the local variables TestStand passes to the code module for the step. |
| You delete an <ActionReference> or a <Step> child element of a <TestGroup> element of the TestGroupParallel type or a child element of a <Parallel> element. | The Sequence Call step that corresponds to the deleted <ActionReference> element, the local variables TestStand passes to the code module for the step, and the sequence the Sequence Call step calls. |
| You delete a <TestGroup> element. | The sequence that corresponds to the deleted <TestGroup> element. |
| You delete an <AutomaticGeneration>, <Description>, <Extension>, <IeeeStd1641>, or <Operations> child element of the <Action>/<Behavior> element. | The comments in the code module that correspond to the deleted <AutomaticGeneration>, <Description>, <Extension>, <IeeeStd1641>, or <Operations> element. |
| You delete an <AutomaticGeneration>, <FailureFaultData>, <TsfLibraries>, <Tools>, or <UUT> child element of the <TestDescription> root element. | The file global variables that correspond to the deleted <AutomaticGeneration>, <FailureFaultData>, <TsfLibraries>, <Tools>, or <UUT> element. |

Parent topic:

Incrementally Updating a Translated Sequence File

Related concepts:

- Incrementally Updating a Translated Sequence File
- Storing TD Instance Document Attributes in a Translated Sequence

<!--NI_TOPIC bundle=teststand-atml-toolkit path=deriving-atml-test-results-elements-from-tran.html language=enus -->
## TOPIC 00014: Deriving ATML Test Results Elements from Translated TD Elements

- bundle_id: `teststand-atml-toolkit`
- source_path: `deriving-atml-test-results-elements-from-tran.html`
- source_url: https://docs-be.ni.com/bundle/teststand-atml-toolkit/raw/resource/enus/deriving-atml-test-results-elements-from-tran.html
- document_id: `teststand-atml-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following table shows the relationship between ATML Test Results (TR) elements and the TestStand constructs in a sequence file the ATML TD translator translates from a source TD instance document: TR Element Sequence File Equivalent <References> FileGlobals.UUT.Documentation file global variable

### Deriving ATML Test Results Elements from
 Translated TD Elements

The following table shows the relationship between ATML Test Results (TR) elements and the
 TestStand constructs in a sequence file the ATML TD translator translates from a source
 TD instance document:

| TR Element | Sequence File Equivalent |
| --- | --- |
| <References> | FileGlobals.UUT.Documentation file global variable |
| <TestDescription>/<DescriptionDocumentReference> element | FileGlobals.TestDescriptionAttributes.uuid file global variable |
| securityClassification attribute of the TestResults root element | FileGlobals.TestDescriptionAttributes.securityClassification file global variable |
| <Events> child element of the <SessionAction>, <Test>, or <TestGroup> element | Step.Result.Error property |
| <Outcome> child element of the <Test> or <TestGroup> element, or the <ActionOutcome> child element of the <SessionAction> element | Step.Result.Status property |
| <Description> child element of the <SessionAction>, <Test>, or <TestGroup> element | NI.ATML.TDTranslator.StepDescription attribute of Step.Result.ReportText property |
| ID attribute of the <SessionAction>, <Test>, or <TestGroup> element | NI.ATML.TDTranslator.StepID attribute of Step.Result.ReportText property |
| <Parameter>/<Description> element | NI.ATML.TDTranslator.Description attribute of an [In] parameter PropertyObject |
| <TestResult>/<Description> element | NI.ATML.TDTranslator.Description attribute of an [Out] parameter PropertyObject or an additional results PropertyObject |
| <Parameters>/<Parameter> element under an <SessionAction>, <Test>, or <TestGroup> element | Step [In] parameters |
| <TestResult> child element of the <Test> or <TestGroup> element | Step [Out] parameters and step additional results |
| <Data> child element of the <Test> or <TestGroup> element | Attributes of step [In] and [Out] parameters and attributes of additional results |
| <SessionAction>/<Data> element | Step [In] and [Out] parameters. Step additional results. Attributes of step [In] and [Out] parameters. Attributes of additional results. |
| <TestResult>/<TestLimits> child element of the <Test> or <TestGroup> element | Step limit values and comparison types |
| <Test> element | A step that does not use the Sequence Adapter and that specifies limits but no post action sequence call. A step that does not use the Sequence Adapter and that specifies limits and a post action sequence call that does not specify any results to record. A step that uses the Sequence Adapter and that does not specify a post action sequence call. The sequence the step calls does not specify any results to record, and the step is not an Action step. A step that uses the Sequence Adapter and that specifies a post action sequence call that does not specify any results to record. The sequence the step calls does not specify any results to record, and the step is not an Action step. |
| <SessionAction> element | A step that does not use the Sequence Adapter and that does not specify limits or a post action sequence call. A step that does not use the Sequence Adapter and that does not specify limits but specifies a post action sequence call that does not specify any results to record. A step that uses the Sequence Adapter and that does not specify a post action sequence call. The sequence the step calls does not specify any results to record and the step is an Action step. A step that uses the Sequence Adapter and that specifies a post action sequence call that does not specify any results to record. The sequence the step calls does not specify any results to record and the step is an Action step. |
| <TestGroup> element | A step that uses the Sequence Adapter that specifies results to record. A step that does not use the Sequence Adapter and that specifies a post action sequence call that specifies results to record. |

Note

TestStand adds error messages and codes to the report as events with a severity
 value of 4. According to the ATML Test Results and Session
 Information schema, a severity value of 4 indicates a critical
 event.

The ATML Test Results and Session Information schema does not support reporting
 the Case Insensitive string limit comparison type in TestStand. The report
 instead displays IgnoreCase for the Comparison Type field even when the
 comparison type is Case Insensitive in the sequence.

TestStand supports arrays that begin with a negative index, but the ATML Test
 Results and Session Information schema supports only zero-based indexing for
 arrays. Therefore, an ATML TR report generated for arrays that begin with a
 negative index do not validate against the ATML Test Results and Session
 Information schema.

Parent topic:

TestStand ATML Toolkit Help

Related concepts:

- Translating a TD Instance Document to a TestStand Sequence File

<!--NI_TOPIC bundle=teststand-atml-toolkit path=determining-the-step-type-to-create-for-a-tes.html language=enus -->
## TOPIC 00015: Determining the Step Type to Create for a Test Element

- bundle_id: `teststand-atml-toolkit`
- source_path: `determining-the-step-type-to-create-for-a-tes.html`
- source_url: https://docs-be.ni.com/bundle/teststand-atml-toolkit/raw/resource/enus/determining-the-step-type-to-create-for-a-tes.html
- document_id: `teststand-atml-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following table describes how the ATML TD translator determines which TestStand step type to create for each <Test> element based on its child elements <TestLimits>/<Limit>: Structure of Source TD Instance Document Translator Behavior Additional Test Required The <Limit> element contains a <Mask

### Determining the Step Type to Create for a Test
 Element

The following table describes how the ATML TD translator determines which TestStand step type to
 create for each <Test> element based on its child elements
 <TestLimits>/<Limit>:

| Structure of Source TD Instance Document | Translator Behavior | Additional Test Required |
| --- | --- | --- |
| The <Limit> element contains a <Mask> child element. | Creates a Pass/Fail Test step. | You must apply the specified mask and return the pass/fail status. |
| The value of the xsi:type attribute of the <Behavior>/<Operations>/<Operation> element is OperationCompare. | Creates a Pass/Fail Test step and adds the content of the <Limit> element as a comment to the code module that implements the parent <Test> element. | You must implement the limit comparison logic in the code module. |
| The <Test> element contains a customType attribute. | The customType attribute takes precedence over the limit processing. Therefore, the translator creates a step the customType attribute defines and adds comments for the <Limit> element to the code module. | You must implement the limit comparison logic in the code module. |
| The <Test> element includes a single numeric type <TestResult> element and the <TestResult>/<TestLimits> element contains only one numeric type <Limit> child element. | Creates a Numeric Limit Test step. | — |
| The <Test> element includes multiple numeric type <TestResult> elements and each <TestResult>/<TestLimits> element contains a numeric type <Limit> element. | Creates a Multiple Numeric Limit Test step. | — |
| The <Test> element includes a single <TestResult> element with multiple numeric type <Limit> elements. | Creates a Multiple Numeric Limit Test step. | — |
| The <Test> element contains a single string type <TestResult> element, the <TestResult> element contains a string type <Limit> element, and the <Limit> element contains an <Expected> child element with a comparator attribute that specifies a value of EQ. | Creates a String Value Test step. String Value Test steps support only EQ types of comparison, and the translator supports only case-sensitive comparison. | — |
| The <Test> element specifies an xsi:type attribute with a value of SessionTest. | Creates a Test step. | — |

For all other cases, the translator generates a Pass/Fail Test step and copies the XML content of
 the <TestLimits> element as a comment in the LabVIEW or
 LabWindows/CVI code module that implements the parent <Test>
 element.

#### Completing the Partial Test
 Program
 [IMAGE alt='image' src='GUID-5D8EF323-6138-4253-8059-68EE3E52E461-a5.gif']

You must implement in the code
 module the limit comparison that the
 <TestLimits>/<Limit> element
 describes, and return the comparison results to TestStand. Refer to the
 *Post-Translation Recommended Tests* section of the log file for more
 information about how you can implement the logic the <Limit>
 element describes.

Parent topic:

TestStand ATML Toolkit Help

Related concepts:

- Translating an Action Element with a customType Attribute
- Creating LabVIEW Code Modules for Behavior Elements
- Creating LabWindows/CVI Code Modules for Behavior Elements
- Post-Translation Recommended Actions Section - Logging Translation Information
- Logging Translation Information

<!--NI_TOPIC bundle=teststand-atml-toolkit path=determining-the-step-type-to-create-for-an-ac.html language=enus -->
## TOPIC 00016: Determining the Step Type to Create for an Action Element

- bundle_id: `teststand-atml-toolkit`
- source_path: `determining-the-step-type-to-create-for-an-ac.html`
- source_url: https://docs-be.ni.com/bundle/teststand-atml-toolkit/raw/resource/enus/determining-the-step-type-to-create-for-an-ac.html
- document_id: `teststand-atml-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following table describes how the ATML TD translator determines which TestStand step type to create for each <Action> element based on its child elements <TestLimits>/<Limit>: Structure of Source TD Instance Document Translator Behavior Additional Action Required The <Limit> element contains a <

### Determining the Step Type to Create for an
 Action Element

The following table describes how the ATML TD translator determines which TestStand step type to
 create for each <Action> element based on its child elements
 <TestLimits>/<Limit>:

| Structure of Source TD Instance Document | Translator Behavior | Additional Action Required |
| --- | --- | --- |
| The <Limit> element contains a <Mask> child element. | Creates a Pass/Fail Test step. | You must apply the specified mask and return the pass/fail status. |
| The value of the xsi:type attribute of the <Behavior>/<Operations>/<Operation> element is OperationCompare. | Creates a Pass/Fail Test step and adds the content of the <Limit> element as a comment to the code module that implements the parent <Action> element. | You must implement the limit comparison logic in the code module. |
| The <Action> element contains a customType attribute. | The customType attribute takes precedence over the limit processing. Therefore, the translator creates a step the customType attribute defines and adds comments for the <Limit> element to the code module. | You must implement the limit comparison logic in the code module. |
| The <Action> element includes a single numeric type <TestResult> element and the <TestResult>/<TestLimits> element contains only one numeric type <Limit> child element. | Creates a Numeric Limit Test step. | — |
| The <Action> element includes multiple numeric type <TestResult> elements and each <TestResult>/<TestLimits> element contains a numeric type <Limit> element. | Creates a Multiple Numeric Limit Test step. | — |
| The <Action> element includes a single <TestResult> element with multiple numeric type <Limit> elements. | Creates a Multiple Numeric Limit Test step. | — |
| The <Action> element contains a single string type <TestResult> element, the <TestResult> element contains a string type <Limit> element, and the <Limit> element contains an <Expected> child element with a comparator attribute that specifies a value of EQ. | Creates a String Value Test step. String Value Test steps support only EQ types of comparison, and the translator supports only case-sensitive comparison. | — |
| The <Action> element specifies an xsi:type attribute with a value of SessionAction. | Creates an Action step. | — |

For all other cases, the translator generates a Pass/Fail Test step and copies the XML content of
 the <TestLimits> element as a comment in the LabVIEW or
 LabWindows/CVI code module that implements the parent <Action>
 element.

#### Completing the Partial Test Program[IMAGE alt='image' src='GUID-5D8EF323-6138-4253-8059-68EE3E52E461-a5.gif']

You must implement in the code module the limit comparison
 that the <TestLimits>/<Limit> element
 describes, and return the comparison results to TestStand. Refer to the
 *Post-Translation Recommended Actions* section of the log file for
 more information about how you can implement the logic the
 <Limit> element describes.

Parent topic:

TestStand ATML Toolkit Help

Related concepts:

- Translating an Action Element with a customType Attribute
- Creating LabVIEW Code Modules for Behavior Elements
- Creating LabWindows/CVI Code Modules for Behavior Elements
- Post-Translation Recommended Actions Section - Logging Translation Information
- Logging Translation Information

<!--NI_TOPIC bundle=teststand-atml-toolkit path=example-labview-custom-code-generator-vis-67.html language=enus -->
## TOPIC 00017: Example LabVIEW Custom Code Generator VIs

- bundle_id: `teststand-atml-toolkit`
- source_path: `example-labview-custom-code-generator-vis-67.html`
- source_url: https://docs-be.ni.com/bundle/teststand-atml-toolkit/raw/resource/enus/example-labview-custom-code-generator-vis-67.html
- document_id: `teststand-atml-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the example VIs located in the <TestStand Public>\Examples\Toolkits\ATMLTDTranslator\Code Generator\LabVIEW directory as a starting point for implementing a VI that calls a specific code generator callback. Refer to the individual callback topics for more information about the example VI for eac

### Example LabVIEW Custom Code Generator
 VIs

Use the example VIs located in the
 <TestStand Public>\Examples\Toolkits\ATMLTDTranslator\Code
 Generator\LabVIEW directory as a starting point for implementing a VI
 that calls a specific code generator callback. Refer to the individual callback topics
 for more information about the example VI for each callback, including the controls and
 indicators you must connect to the VI connector pane.

Complete the following steps to use the example VIs to generate complete LabVIEW code modules for
 the translated sequence:

1. In TestStand, select Tools»Configure ATML TD Translator to launch the
 ATML Test Description Translator Configuration dialog
 box.
2. Click the Code Module Settings tab and enable the
 LabVIEW option.
3. Click the Browse button next to the Directory that Contains
 the Custom Code Generator VIs control and browse to
 <TestStand Public>\Examples\Toolkits\ATMLTDTranslator\Code
 Generator\LabVIEW .
4. Click OK to close the ATML Test Description Translator
 Configuration dialog box.
5. Close all open sequence files.
6. In TestStand, select File»Open File to launch the File Open dialog box.
7. Browse to <TestStand Public>\Examples\Toolkits\ATMLTDTranslator\Translator\Test
 Description 1.0\Computer 1.0.xml .
8. Click Open to translate the TD instance document to a TestStand sequence file and a set of LabVIEW code modules.
9. Review the translated sequence file and the generated code modules. Note If an
 <Action> element contains a child element of the
 OperationConnect, OperationRead, or
 OperationDisconnect type, the custom code generator adds
 subVI calls to the VI reference the VIFileUpdater.VIReference
 property returns to implement the operation. The example demonstrates how to
 insert a new parameter named UUID, which TestStand passes to
 code modules, and how to change the flags of the step and sequence constructs to
 non-editable and non-deletable, respectively.

#### Incremental Update
 [IMAGE alt='image' src='GUID-10242244-39C8-44B3-AAC3-6C5701803D28-a5.gif']

Complete the steps in the
 *Calling LabVIEW Custom Code Generator VIs during an Incremental
 Update* section for information about using LabVIEW custom code generator
 VIs when you incrementally update a previously translated sequence
 file.

Parent topic:

Implementing a LabVIEW Custom Code Generator

Related concepts:

- Calling LabVIEW Custom Code Generator VIs during an Incremental Update
- Creating a VI for a LabVIEW Custom Code Generator
- Creating LabVIEW Code Modules for Behavior Elements
- Custom Code Generator API

<!--NI_TOPIC bundle=teststand-atml-toolkit path=extended-support-changes.html language=enus -->
## TOPIC 00018: Updates and Changes for TestStand ATML Toolkit Extended Support Versions

- bundle_id: `teststand-atml-toolkit`
- source_path: `extended-support-changes.html`
- source_url: https://docs-be.ni.com/bundle/teststand-atml-toolkit/raw/resource/enus/extended-support-changes.html
- document_id: `teststand-atml-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Browse updates and changes made in TestStand ATML Toolkit versions on extended support. If you cannot find changes for your version, it might be a more recent version, documented as a new feature. Or, your version might not have included user-facing updates. You can find more information about non-v

### Updates and Changes for TestStand ATML Toolkit Extended Support Versions

Browse updates and changes made in TestStand ATML Toolkit versions
 on extended support.

Note

Release Notes

<!--NI_TOPIC bundle=teststand-atml-toolkit path=generating-complete-code-modules-using-a-cust.html language=enus -->
## TOPIC 00019: Generating Complete Code Modules Using a Custom Code Generator

- bundle_id: `teststand-atml-toolkit`
- source_path: `generating-complete-code-modules-using-a-cust.html`
- source_url: https://docs-be.ni.com/bundle/teststand-atml-toolkit/raw/resource/enus/generating-complete-code-modules-using-a-cust.html
- document_id: `teststand-atml-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The ATML TD translator translates an <Action> or <Test> element to a step in the translated TestStand sequence and translates the <Action>, <Test>or <Behavior> element as a LabVIEW or LabWindows/CVI code module for the step. Because the translator cannot translate all elements in a TD source file to

### Generating Complete Code Modules Using a
 Custom Code Generator

The ATML TD translator translates an <Action> or
 <Test> element to a step in the translated TestStand sequence
 and translates the <Action>, <Test>or
 <Behavior> element as a LabVIEW or LabWindows/CVI code module
 for the step. Because the translator cannot translate all elements in a TD source file
 to constructs in TestStand or logic in code modules, the translator creates comments
 that describe the operations and logic you must implement to create a complete test
 program.

You can manually implement the operations and logic the comments in the code modules describe, or
 you can use the custom code generator callbacks during translation to programatically
 translate the code module comments to code that implements the logic required to
 complete the test program. The translator calls the callbacks when *translating an
 <Action>* or *translating a <TestGroup>* element. Use a
 custom code generator when you want to implement code only once in callbacks, which you
 can reuse when translating multiple TD instance documents, to avoid manually
 implementing the missing code for each TD instance document you translate. You can
 implement one or more callbacks in a custom code generator.

dll

Note

#### API

The ATML Toolkit includes custom code
 generator API classes, properties, methods, and enumerations you can use when
 implementing the code generator functionality.

Parent topic:

TestStand ATML Toolkit Help

Related concepts:

- Creating LabVIEW Code Modules for Behavior Elements
- Creating LabWindows/CVI Code Modules for Behavior Elements
- Completing the Partial Test Program
- Incrementally Updating a Translated Sequence File
- Implementing a LabVIEW Custom Code Generator
- Implementing a LabWindows/CVI Custom Code Generator
- Logging Translation Information
- Custom Code Generator API

<!--NI_TOPIC bundle=teststand-atml-toolkit path=getting-started-with-the-atml-td-translator-1.html language=enus -->
## TOPIC 00020: Getting Started with the ATML TD Translator

- bundle_id: `teststand-atml-toolkit`
- source_path: `getting-started-with-the-atml-td-translator-1.html`
- source_url: https://docs-be.ni.com/bundle/teststand-atml-toolkit/raw/resource/enus/getting-started-with-the-atml-td-translator-1.html
- document_id: `teststand-atml-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use the Open File dialog box in TestStand to browse for files with XML extensions, including valid ATML TD instance documents. When you open a TD instance document, the ATML TD translator translates the TD instance document to a partial test program, which includes a translated TestStand seq

### Getting Started with the ATML TD
 Translator

You can use the Open File dialog box in TestStand to browse for files with
 XML extensions, including valid ATML TD instance documents. When you open a TD instance
 document, the ATML TD translator translates the TD instance document to a partial test
 program, which includes a translated TestStand sequence file and a set of LabVIEW or
 LabWindows/CVI code modules.

Use the ATML Test Description Translator Configuration dialog box to
 configure the Application Development Environment (ADE) to use for generating the code
 modules. The translator creates VIs for LabVIEW code modules and creates a project file
 and a source file for LabWindows/CVI code modules.

The ATML Toolkit includes an example, located in the
 <TestStand Public>\Examples\Toolkits\ATMLTDTranslator\Translator
 directory, to help you begin using the TD translator.

Complete the following steps to translate the example to a partial test program.

1. Create a directory named Examples on the desktop.
2. Copy all files located in the
 <TestStand Public>\Examples\Toolkits\ATMLTDTranslator\Translator 
 directory to the <Desktop>\Examples directory. You will
 use the copy of the files in the <Desktop>\Examples 
 directory so that you do not modify the example in the
 <TestStand Public> directory.
3. In TestStand, select Tools»Configure ATML TD Translator to launch the ATML Test Description Translator
 Configuration dialog box.
4. Click the Code Module Settings tab and enable the
 LabVIEW or LabWindows/CVI option,
 depending on the ADE for which you want the translator to generate code modules. You
 can also use the controls available on the Code Module
 Settings tab to specify the file paths for saving the generated
 LabVIEW VIs or the file paths and names for saving the generated LabWindows/CVI
 project file, C source file, and DLL. In addition, you can use the controls on the
 Code Module Settings tab to specify a path to a directory
 that contains VIs or a path to a DLL that implements a LabVIEW or LabWindows/CVI
 custom code generator, respectively. Click OK to close the
 ATML Test Description Translator Configuration dialog
 box.
5. Close all open sequence files.
6. Select File»Open File to launch the Open File dialog box. Browse to
 <Desktop>\Examples\Translator\Computer.xml , which is
 an ATML TD instance document. Note If you attempt to open an XML
 file that is not formatted as an ATML TD instance document in TestStand, the
 translator returns an error that specifies that it does not support the file and
 TestStand returns an error that it does not have a sequence file translator that
 supports the file format.
7. Click Open . The TD translator translates the TD instance document to a
 partial test program, which includes a TestStand sequence file and a set of LabVIEW
 or LabWindows/CVI code modules, depending on the ADE you selected in step 4. The
 translated sequence file contains a sequence named MainSequence that contains
 multiple steps.

<Desktop>\Examples\Translator\CodeModules_Computer

<Desktop>\Examples\Translator\CVI

<Desktop>\Examples\Translator\LabVIEW

Note

Add Date and Time to File Name

Generated Sequence File Settings

ATML Test Description Translator Configuration

#### Incrementally Updating a Previously Translated Test
 Program

If you make changes to the source TD instance document and you
 want to reflect the changes in the translated sequence file and code modules, you
 can incrementally update the sequence file and code modules instead of creating an
 entirely new test program.

Complete the following steps to incrementally
 update a previously translated partial test program.

1. Select Tools»Configure ATML TD Translator to launch the ATML Test Description Translator
 Configuration dialog box.
2. Click the General Settings tab and enable the
 Update Sequence File option. Click
 OK to close the ATML Test Description
 Translator Configuration dialog box.
3. Close all open sequence files.
4. Select File»Open File to launch the Open File dialog box. Browse to
 <Desktop>\Examples\Translator\Computer - Update.xml ,
 which is an ATML TD instance document.
5. Click Open . The Update Options 
 dialog box launches.
6. Enable the Use the Selected File to Update option and
 click the Browse button to select the
 Computer.seq sequence file you created in the
 previous tutorial. The translator updates the existing sequence file and the
 LabVIEW or LabWindows/CVI code modules it had previously created.

Parent topic:

Translating a TD Instance Document to a TestStand Sequence File

Related concepts:

- Completing the Partial Test Program
- Creating LabVIEW Code Modules for Behavior Elements
- Creating LabWindows/CVI Code Modules for Behavior Elements
- Generating Complete Code Modules Using a Custom Code Generator
- Incrementally Updating a Translated Sequence File
- Translation Process Overview

<!--NI_TOPIC bundle=teststand-atml-toolkit path=header-section-logging-translation-informatio.html language=enus -->
## TOPIC 00021: Header Section - Logging Translation Information

- bundle_id: `teststand-atml-toolkit`
- source_path: `header-section-logging-translation-informatio.html`
- source_url: https://docs-be.ni.com/bundle/teststand-atml-toolkit/raw/resource/enus/header-section-logging-translation-informatio.html
- document_id: `teststand-atml-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The header section of the log file includes the following items: Translation status ATML TD instance document path Location of the schema used to validate the TD instance document TD namespace Uniform Resource Identifier (URI), such as urn:IEEE-1671.1:2009:TestDescription or urn:IEEE-1671:2009.02:Co

### Header Section - Logging Translation
 Information

The header section of the log file includes the following items:

- Translation status
- ATML TD instance document path
- Location of the schema used to validate the TD instance document
- TD namespace Uniform Resource Identifier (URI), such as
 urn:IEEE-1671.1:2009:TestDescription or
 urn:IEEE-1671:2009.02:Common , used to validate the TD instance
 document against the schema the URI specifies, such as
 TestDescription.xsd or Common.xsd
- Start and end date and time of the translation
- Total time required for the translation
- Total number of errors and warnings

Parent topic:

Logging Translation Information

<!--NI_TOPIC bundle=teststand-atml-toolkit path=ieee-1641-specification-data-types-using-test.html language=enus -->
## TOPIC 00022: IEEE 1641 Specification Data Types - Using TestStand Type Palette Files with the TD Translator

- bundle_id: `teststand-atml-toolkit`
- source_path: `ieee-1641-specification-data-types-using-test.html`
- source_url: https://docs-be.ni.com/bundle/teststand-atml-toolkit/raw/resource/enus/ieee-1641-specification-data-types-using-test.html
- document_id: `teststand-atml-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: IEEE 1641 Specification Data TypesThe ATMLTD_IEEE1641_Types type palette contains types from the STDTSF.xsd, STDBSC.xsd, and STDTSFLib.xsd ATML TD schema files.By default, the ATML TD translator does not load this type palette file when you launch TestStand. To load this type palette file, enable th

### IEEE 1641 Specification Data Types - Using
 TestStand Type Palette Files with the TD Translator

#### IEEE 1641 Specification Data Types

The
 ATMLTD_IEEE1641_Types type palette contains types from the
 STDTSF.xsd, STDBSC.xsd, and
 STDTSFLib.xsd ATML TD schema files.

By default, the
 ATML TD translator does not load this type palette file when you launch TestStand.
 To load this type palette file, enable the Use IEEE 1641 Data Types in
 TestStand option on the General Settings tab
 of the ATML Test Description Translator Configuration dialog
 box.

The types defined in the ATMLTD_IEEE1641_Types.ini
 type palette file include an NI_ATMLSTD prefix on the type
 names.

Parent topic:

Using TestStand Type Palette Files with the TD Translator

Related concepts:

- ATML TD Schema File Data Types - Using TestStand Type Palette Files with the TD Translator

<!--NI_TOPIC bundle=teststand-atml-toolkit path=implementing-a-labview-custom-code-generator.html language=enus -->
## TOPIC 00023: Implementing a LabVIEW Custom Code Generator

- bundle_id: `teststand-atml-toolkit`
- source_path: `implementing-a-labview-custom-code-generator.html`
- source_url: https://docs-be.ni.com/bundle/teststand-atml-toolkit/raw/resource/enus/implementing-a-labview-custom-code-generator.html
- document_id: `teststand-atml-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can create a VI to implement a custom code generator callback for a LabVIEW code module. The translator validates the order and types of controls and indicators connected to the connector pane. You can store all the callback VIs in a single directory that the translator references when creating

### Implementing a LabVIEW Custom Code
 Generator

You can create a VI to implement a custom code generator callback for a LabVIEW code module. The
 translator validates the order and types of controls and indicators connected to the
 connector pane. You can store all the callback VIs in a single directory that the
 translator references when creating the code modules. You can implement one or more
 callbacks in a custom code generator.

Enable the LabVIEW option on the Code Module
 Settings tab of the ATML Test Description Translator
 Configuration dialog box and use the Directory Containing
 Custom Code Generator VIs control to specify the directory that contains
 the callback VIs.

The ATML Toolkit includes an example that demonstrates how the translator uses custom code
 generator VIs to create complete LabVIEW code modules. The translator calls custom code
 generator VIs during translation or during an incremental update.

<TestStand Public>\Examples\Toolkits\ATMLTDTranslator\Code
 Generator\LabVIEW

Note

CodeGenerator_PreTranslateAction.vi

Parent topic:

Generating Complete Code Modules Using a Custom Code Generator

Related concepts:

- Generating Complete Code Modules Using a Custom Code Generator
- Example LabVIEW Custom Code Generator VIs
- Calling LabVIEW Custom Code Generator VIs during an Incremental Update
- Creating a VI for a LabVIEW Custom Code Generator

<!--NI_TOPIC bundle=teststand-atml-toolkit path=implementing-a-labwindows-cvi-custom-code-gen.html language=enus -->
## TOPIC 00024: Implementing a LabWindows/CVI Custom Code Generator

- bundle_id: `teststand-atml-toolkit`
- source_path: `implementing-a-labwindows-cvi-custom-code-gen.html`
- source_url: https://docs-be.ni.com/bundle/teststand-atml-toolkit/raw/resource/enus/implementing-a-labwindows-cvi-custom-code-gen.html
- document_id: `teststand-atml-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can build a dll that exports all the custom code generator callback functions the translator references when creating the code modules. You can implement one or more callbacks in a custom code generator.Enable the LabWindows/CVI option on the Code Module Settings tab of the ATML Test Description

### Implementing a LabWindows/CVI Custom Code
 Generator

You can build a dll that exports all the custom code generator callback
 functions the translator references when creating the code modules. You can implement
 one or more callbacks in a custom code generator.

Enable the LabWindows/CVI option on the Code Module
 Settings tab of the ATML Test Description Translator
 Configuration dialog box and use the Path to Custom Code
 Generator DLL control to specify the file path to the
 dll that contains all the callback functions.

The ATML Toolkit includes an example that demonstrates how the translator uses the custom code
 generator dll to create complete LabWindows/CVI code modules. The
 translator calls a custom code generator dll during translation or
 during an incremental update.

dll

Note

PreTranslateAction

CodeGenerator_PreTranslateAction()

Parent topic:

Generating Complete Code Modules Using a Custom Code Generator

Related concepts:

- Generating Complete Code Modules Using a Custom Code Generator
- Recommended LabWindows/CVI Function Prototypes
- Calling a LabWindows/CVI Custom Code Generator dll during an Incremental Update
- Recommended Microsoft Visual C++ Function Prototypes
- Creating a dll for a LabWindows/CVI Custom Code Generator

<!--NI_TOPIC bundle=teststand-atml-toolkit path=incrementally-updating-a-translated-sequence.html language=enus -->
## TOPIC 00025: Incrementally Updating a Translated Sequence File

- bundle_id: `teststand-atml-toolkit`
- source_path: `incrementally-updating-a-translated-sequence.html`
- source_url: https://docs-be.ni.com/bundle/teststand-atml-toolkit/raw/resource/enus/incrementally-updating-a-translated-sequence.html
- document_id: `teststand-atml-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: If you modify a TD instance document after translating it to a TestStand sequence file and a set of LabVIEW or LabWindows/CVI code modules, you can run the translator again. Choose to incrementally update the previously generated sequence file and code modules instead of generating new files. The tr

### Incrementally Updating a Translated Sequence
 File

If you modify a TD instance document after translating it to a TestStand sequence file and a set
 of LabVIEW or LabWindows/CVI code modules, you can run the translator again. Choose to
 incrementally update the previously generated sequence file and code modules instead of
 generating new files.

The translator updates the existing sequence file and code module constructs previously
 translated from the TD instance document. The translator creates a log file for the
 incremental update, and you can use the log file to examine changes made to the sequence
 file.

1. Enable the Update Sequence File option on the
 General Settings tab of the ATML Test
 Description Translator Configuration dialog box to update the
 sequence file incrementally.
2. Enable the Launch TestStand File Diff/Merge Application to Show
 Differences option on the General Settings 
 tab to use the TestStand File Diff/Merge application to view the differences between
 the original sequence file and the updated sequence file.
3. Enable the Preview Only option on the General
 Settings tab to view only the updates using the log files or the
 TestStand File Diff/Merge application but not apply them.

When you open a modified TD instance document to retranslate, TestStand launches the
 Update Options dialog box, in which you can specify to update
 a previously translated sequence file or to translate the modified TD instance document
 to a new sequence file.

You can also use the LabVIEW custom code generator VIs or a LabWindows/CVI
 custom code generator DLL to update existing code modules during an incremental
 update.

Individual TD element topics that contain the Incremental Update
 icon ([IMAGE alt='image' src='GUID-10242244-39C8-44B3-AAC3-6C5701803D28-a5.gif']) provide information about how the translator
 incrementally updates the existing TestStand constructs the translator previously
 created for that element.

Parent topic:

Translating a TD Instance Document to a TestStand Sequence File

Related concepts:

- Logging Translation Information
- Calling LabVIEW Custom Code Generator VIs during an Incremental Update
- Calling a LabWindows/CVI Custom Code Generator dll during an Incremental Update
- Generating Complete Code Modules Using a Custom Code Generator

<!--NI_TOPIC bundle=teststand-atml-toolkit path=localization-support-93.html language=enus -->
## TOPIC 00026: Localization Support 93

- bundle_id: `teststand-atml-toolkit`
- source_path: `localization-support-93.html`
- source_url: https://docs-be.ni.com/bundle/teststand-atml-toolkit/raw/resource/enus/localization-support-93.html
- document_id: `teststand-atml-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The ATML Toolkit includes an ATMLTDString.ini string resource file, located in the <TestStand>\Components\Language\English directory.You can modify the strings in the resource file to localize the following information: Dialog box messages when an error occurs during translation or an incremental up

### Localization Support 93

The ATML Toolkit includes an ATMLTDString.ini string resource file, located in
 the <TestStand>\Components\Language\English directory.

You can modify the strings in the resource file to localize the following information:

- Dialog box messages when an error occurs during translation or an incremental update
- Log file entries the translator generates for each translation or incremental update
- String labels that display in the ATML Test Description Translator
 Configuration dialog box and the Update
 Options dialog box

To support error and log messages for multiple languages, copy the resource file and place it in
 the required language directory in the <TestStand
 Public>\Components\Language directory.

Parent topic:

Translating a TD Instance Document to a TestStand Sequence File

Related concepts:

- Translating a TD Instance Document to a TestStand Sequence File
- Incrementally Updating a Translated Sequence File
- Logging Translation Information

<!--NI_TOPIC bundle=teststand-atml-toolkit path=logging-translation-information-94.html language=enus -->
## TOPIC 00027: Logging Translation Information

- bundle_id: `teststand-atml-toolkit`
- source_path: `logging-translation-information-94.html`
- source_url: https://docs-be.ni.com/bundle/teststand-atml-toolkit/raw/resource/enus/logging-translation-information-94.html
- document_id: `teststand-atml-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The ATML TD translator generates a log file for each translation of a TD instance document in the same directory as the generated TestStand sequence file. The log file contains the following sections: Header Validation Translation Post-Translation Recommended Actions In TestStand, select Tools»Confi

### Logging Translation Information

The ATML TD translator generates a log file for each translation of a TD instance document in the
 same directory as the generated TestStand sequence file. The log file contains the
 following sections:

- Header
- Validation
- Translation
- Post-Translation Recommended Actions

In TestStand, select Tools»Configure ATML TD Translator to launch the
 ATML Test Description Translator Configuration dialog box, in
 which you can use the Log Level option on the General Settings
 tab to configure filtering options for information the log file includes.

The translator bases the name of the log file on the name of the TD instance document and adds
 the following items to the filename:

- ATMLLog_ prefix
- Date suffix
- Start time of translation suffix
- Successful or failed status suffix

IEEE 1671.1 - Example3

ATMLLog_IEEE 1671.1 - Example3_Successful[07 08
 2009][15 22 07].xml

Note

Parent topic:

Translating a TD Instance Document to a TestStand Sequence File

Related concepts:

- Header Section - Logging Translation Information
- Validation Section - Logging Translation Information
- Translation Section - Logging Translation Information
- Post-Translation Recommended Actions Section - Logging Translation Information

<!--NI_TOPIC bundle=teststand-atml-toolkit path=new-features-and-changes.html language=enus -->
## TOPIC 00028: TestStand ATML Toolkit New Features and Changes

- bundle_id: `teststand-atml-toolkit`
- source_path: `new-features-and-changes.html`
- source_url: https://docs-be.ni.com/bundle/teststand-atml-toolkit/raw/resource/enus/new-features-and-changes.html
- document_id: `teststand-atml-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Learn about updates—including new features and behavior changes—introduced in each version of TestStand ATML Toolkit. Discover what's new in the latest releases of TestStand ATML Toolkit.If you cannot find new features and changes for your version, it might not include user-facing updates. However,

### TestStand ATML Toolkit
 New Features and Changes

Learn about updates—including new features and behavior changes—introduced in each
 version of TestStand ATML Toolkit.

TestStand ATML Toolkit

Note

Release Notes

Related information:

- Software and Driver Downloads

#### ATML Toolkit 2017 New Features

The following list describes the new features in the ATML Toolkit 2017 and other changes since
 the ATML Toolkit 2013.

- Compliance with ATML TD 1.01 and 3.0
- Version-agnostic installation
  - The ATML Toolkit 2017 installer can install with future versions of TestStand. The installer installs files to a separate non-TestStand location, and uses the TestStand Version Selector to copy files to supported versions of TestStand.
  - The ATML Toolkit example files are now located in the <TestStand
 Public>\Examples\Toolkits\ATMLTDTranslator directory and
 the language resource files are located in the
 <TestStand>\Components\Language\English
 directory .
- Support for TestStand 64-bit
  - ATML Toolkit 2013 and earlier were only compatible with TestStand 32-bit.
- Ability to disable automatic code generation
  - Creates steps from an ATML TD file using the None adapter.
  - Supports the custom code generator to generate custom code modules.
- Improvements for the ATML Test Description Translator Configuration 
 dialog, including support for pointing to a specific schema location.
  - Schema files are located in a separate tab with information about the
 schema's location and namespace.

#### ATML Toolkit 2013 New Features

The following list describes the new features in the ATML Toolkit 2013 and other changes since
 the ATML Toolkit 2012.

- You can now generate XML reports that validate against the approved version 6.01 of the ATML
 Test Results and Session Information schema that the ATML standard defines. You can
 also continue to generate reports that validate against the non-finalized version
 5.0 or approved version 2.02 of the schema. Select ATML 6.01 Standards Report
 Document from the Report Format ring control on the Contents tab of the Report
 Options dialog box to generate an ATML report that validates against version 6.01 of
 the schema. TestStand provides the following style sheets, located in the
 <TestStand>\Components\Models\TestStandModels\ATML\Stylesheets 
 directory, for generating an ATML Test Results 6.01 report. You can customize the
 style sheets directly.
- TR6_Expand.xsl —Displays reports similar to TR6_report.xsl , with
 expandable and collapsible sections for each step or for the entire
 report.
- TR6_Horizontal.xls —Displays reports in a horizontal, tabular, indented, format with data
 for each step in one or more rows.
- TR6_report.xls —Displays reports in a vertical, tabular, indented format with data for
 each step in multiple rows. Customizable, color-coded rows visually
 separate relevant information, such as step group, status, and so
 on.
- The ATML Test Results report generator extension DLL can implement the following new functions to modify the content of the ATML TR report.
  - Event_Extension
  - Parameter_Extension
  - TestResults_TestResult_Extension

#### ATML Toolkit 2012 New Features

The following list describes the new features in the ATML Toolkit 2012 and other changes since the ATML Toolkit 2010.

- The ATML Test Results (TR) report generator supports the non-finalized version 5.0 of the ATML Test Results and Session Information schema.
- In addition to using the Locals.Atml_Rpt_Options.ExtDLLAbsPath property in the
 GetATMLReport sequence of the reportgen_atml.seq sequence file
 to provide the path of an extension DLL when you generate an ATML TR 2.02 report,
 you can also now use the
 Parameters.ReportOptions.Atml_Rpt_Options.ExtensionDLLAbsolutePath 
 property in the ReportOptions callback to complete the same task.
- You can use the Parameters.ReportOptions.Atml_Rpt_Options.ExtensionDLLAbsolutePath property in the ReportOptions callback to provide the path of an extension DLL when you generate an ATML TR 5.0 report.
- The ATML Toolkit 2012 includes the following new exported TR report generator extension functions:
  - ResultSet_EnvironmentalData
  - ResultSet_Events_All
  - SessionAction_EnvironmentalData
  - Test_EnvironmentalData
  - TestGroup_EnvironmentalData
  - TestResults_Site
  - TestResults_TestProgram_All
- The ATML Toolkit 2012 includes the following new TR report generator functions:
  - Get_Atml_ReportBody
  - Get_Atml_ReportFooter
  - Get_Atml_ReportHeader

#### ATML Toolkit 2012 Compatibility and Known
 Issues

The ATML Toolkit includes the following behavior changes between version 2010 and version
 2012.

| Behavior | ATML Toolkit 2010 Behavior | ATML Toolkit 2012 Behavior |
| --- | --- | --- |
| Directory structure of TR schemas | <TestStandModels>\\ATML\\Schemas | <TestStandModels>\\ATML\\Schemas\\ATML 2.02 and <TestStandModels>\\ATML\\Schemas\\ATML 5 |

#### ATML Toolkit 2010 New Features

The following list describes the new features in the ATML Toolkit 2010 and other changes since
 the ATML Toolkit 1.0. This list only summarizes each new feature. Refer to the
 documentation listed for a particular feature for more information about that
 feature.

- Enhanced ATML Test Description Translator
  - Translating Limits Associated with Steps Translated from <TestGroupCall> 
 Elements
  - Localization Support
- Improved Incremental Update Support
- Instructions for Completing the Test Program
- Deleting Sequence File and Code Module Constructs
- New ATML Test Results Report Style Sheet
- Sequence File Updater Application

##### Enhanced ATML Test Description
 Translator

The ATML Test Description (TD) translator now supports
 translating limits associated with steps translated from
 <TestGroupCall> elements and localizing error and log
 messages.

##### Translating Limits Associated with
 Steps Translated from <TestGroupCall> Elements

In the case in which a TD instance document contains an
 <Action> element with a <Behavior>
 child element that contains a <TestGroupCall> child element,
 the translator in the ATML Toolkit 2010 uses the <TestLimits>
 element to determine the appropriate type of step to generate in the translated
 sequence file. Depending on the content of the <TestLimits>
 element, the translator generates a Pass/Fail Test, Numeric Limit Test, Multiple
 Numeric Limit Test, or String Value Test step. The translator in the ATML
 Toolkit 1.0 always generated a Pass/Fail Test step in this case.

Refer to the *Determining Test Steps to Create for <Limit> Elements*
 topic for more information about how the translator determines step types.

##### Localization Support

The ATML Toolkit 2010 adds support for localizing user interface strings. The
 following toolkit features contain strings you might want to localize:

- Dialog box messages when an error occurs during translation or an incremental
 update
- Log file entries the translator generates for each translation or incremental
 update
- The string labels that display in the ATML Test Description
 Translator Configuration dialog box and the Update
 Options dialog box

The ATML Toolkit 2010 includes an ATMLTDString.ini string
 resource file, located in the
 <TestStand Public>\Components\Language\English
 directory. You can modify the strings in the resource file to modify the error or
 log messages. To support error and log messages for multiple languages, copy the
 resource file and place it in the required language directory in the
 <TestStand Public>\Components\Language directory.

##### Improved Incremental Update Support

The
 ATML Toolkit 2010 adds support for updating existing LabVIEW or LabWindows/CVI code
 modules the translator created for a previously translated sequence file.

- LabVIEW Code Modules —When incrementally updating a
 previously translated sequence file, the translator determines whether a VI
 already exists at the path you specify in the LabVIEW VI Path control on the
 Code Module Settings tab of the ATML Test Description
 Translator Configuration dialog box. If the VI exists at the path you specified
 and the VI has a name that is the same as the value of the name 
 attribute of the parent <Action> element, the translator
 updates in the VI connector pane the existing block diagram labels that
 correspond to the <AutomaticGeneration> ,
 <Description> , <Extension> ,
 <IeeeStd1641> , and
 <Operations> child elements of the
 <Behavior> element. If the VI does not exist, the
 translator creates a new VI.
- LabWindows/CVI Code Modules —When incrementally updating a
 previously translated sequence file, the translator determines whether a
 function already exists in the C source file at the path you specify in the
 LabWindows/CVI Source File Path control on the Code Module
 Settings tab of the ATML Test Description Translator
 Configuration dialog box. If the source file already exists at
 the path you specified and the file contains a function with a name that is the
 same as the value of the name attribute of the parent
 <Action> element, the translator updates the comments
 in the function definition that correspond to the
 <AutomaticGeneration> ,
 <Description> , <Extension> ,
 <IeeeStd1641> , and
 <Operations> child elements of the
 <Behavior> element. If the function does not exist,
 the translator creates a new function in the source file.

The translator also updates block diagram labels or function comments that
 correspond to the <LocalSignal>,
 <TestLimit>, <Parameter>,
 <SessionDatum>, and <TestResult>
 child elements of the parent <Action> element.

In
 addition, the ATML Toolkit 2010 adds support for incrementally updating TestStand
 steps, attributes, and variables created from the child elements of a
 <TestGroup> element of the TestGroupParallel
 type.

##### Instructions for Completing the Test
 Program

The translator cannot translate all elements in a source TD
 instance document to TestStand constructs, such as steps, sequences, or code
 modules. The translator stores these elements in TestStand variables, attributes, or
 comments, but the generated sequence file does not use the variables, attributes, or
 comments.

The ATML Toolkit 2010 translation log file lists the elements the
 translator translated but cannot implement and describes how you must implement the
 required functionality to complete the test program. The log file uses subsections
 for the sequences and steps that contain the information you must implement. The
 translator generates the log file in the same directory that it generates the
 translated sequence file.

##### Deleting Sequence File and Code Module
 Constructs

The General Settings tab of the
 ATML Test Description Translator Configuration dialog box
 now includes a Delete Previously Generated Sequence File and Code Module
 Constructs option, which is enabled by default.

When you
 enable this option, the translator deletes TestStand steps, sequences, and local
 variables and block diagram labels in LabVIEW code modules or function comments in
 LabWindows/CVI code modules created during the previous translation. The translator
 deletes these items when incrementally updating a sequence file if you have deleted
 the corresponding elements from the source TD instance document.

When you
 disable this option, the translator retains TestStand steps, sequences, and local
 variables and block diagram labels in LabVIEW code modules or function comments in
 LabWindows/CVI code modules when incrementally updating a sequence file, even if you
 have deleted the corresponding elements from the source TD instance document. The
 translator deletes in the retained TestStand constructs the attributes previously
 created for the attributes of translated elements in the source TD instance
 document. For comments in retained code modules, the translator deletes from the
 comments the <ATMLTranslatorComment> and
 </ATMLTranslatorComment> tags previously created for some
 elements in the source TD instance document.

##### New ATML Test Results Report Style
 Sheet

The ATML Toolkit 2010 includes a new ATML Test Results report style
 sheet, TR_horizontal.xsl, located in the
 <TestStand>\Components\Models\TestStandModels\ATML\StyleSheets
 directory. The style sheet displays an ATML Test Results report in a concise tabular
 format with expand and collapse sections.

Select Configure»Report
 Options to launch the Report Options dialog
 box. Click the Contents tab, select ATML Report Document from
 the Report Format ring control, and select TR_horizontal.xsl
 from the Stylesheet ring control to select the new style sheet when you generate an
 ATML Test Results report.

##### Sequence File Updater Application

The
 ATML Toolkit 2010 changes the prefixes of the types contained in the
 ATMLTDTypes.ini and
 ATMLTD_IEEE1641_Types.ini type palette files and also
 renames the Attributes subproperty of the types as ATMLAttributes. As a result of
 these naming changes, the ATML Toolkit 2010 does not correctly incrementally update
 sequence files you originally translated using the ATML Toolkit 1.0. Refer to
 *ATML Toolkit 2010 Compatibility and Known Issues* for more
 information about these naming changes.

You can use the Sequence File
 Updater application to convert sequence files you originally
 translated using the ATML Toolkit 1.0 to a sequence file you can use for an
 incremental update using the ATML Toolkit 2010. Complete the following steps to
 install and launch the Sequence File Updater application.

1. Copy the ATMLSequenceFileConverter directory from the ATML
 Toolkit installer directory, located on the ATML Toolkit 2010 media, to a
 directory on the computer.
2. Double-click SequenceFileConverter.exe , located in the
 ATMLSequenceFileConverter directory, to launch the
 Update Sequence Files Translated with the ATML
 Toolkit 1.0 dialog box.
3. Use the Path of Sequence File to be Updated control to
 specify the path of the sequence file translated using the ATML
 Toolkit 1.0.
4. Optionally, use the Path of Test Description File
 (Optional) control to specify the path of the source TD instance
 document used to generate the sequence file, if the source TD instance document
 is available.
5. Click OK to update the sequence file for the ATML
 Toolkit 2010.

Related concepts:

- Determining the Step Type to Create for an Action Element
- Localization Support 93
- Logging Translation Information
- Post-Translation Recommended Actions Section - Logging Translation Information
- Completing the Partial Test Program
- Deleting Sequence File and Code Module Constructs when Incrementally Updating a Sequence File
- ATML TD Schema File Data Types - Using TestStand Type Palette Files with the TD Translator
- IEEE 1641 Specification Data Types - Using TestStand Type Palette Files with the TD Translator
- ATML Toolkit 2010 Compatibility and Known Issues

#### ATML Toolkit 2010 Compatibility and Known
 Issues

The ATML Toolkit includes the following behavior changes between version 1.0 and version 2010.
 Refer to the list of *ATML Toolkit 2010 Known Issues* on the manufacturer's
 web site for a list of known issues in the ATML Toolkit 2010. You can also view this
 list by date.

| Behavior | ATML Toolkit 1.0 Behavior | ATML Toolkit 2010 Behavior |
| --- | --- | --- |
| When translating the <Datum> child element of a <Parameter> element. | The translator translates the parent <Action> element as a TestStand step, the <Parameter> element as a parameter of the step, and the <Datum> element as a local variable of the sequence that contains the step created for the <Action> element. The value expression for the parameter contains the lookup string for the local variable created for the <Datum> element. | The translator translates the parent <Action> element as a TestStand step and the <Parameter> element as a parameter of the step but no longer creates a local variable when translating <Datum> elements of the following types: binary boolean double hexadecimal integer octal string unsigned integer Instead, the value expression for the parameter contains the value of the <Parameter> element. |
| When translating the <EntryPoints>/<ActionEntryPoints> element. | The translator completes the following steps to translate the <ActionEntryPoints> element. Identifies the <Action> element that the actionID attribute of the first <ActionEntryPoints>/<ActionEntryPoint> element references. Identifies the sequence that corresponds to the first <TestGroup> element that contains a reference to the <Action> element identified in step 1. Inserts a Goto step in the Setup step group of the sequence identified in step 2. Specifies that the destination step for the Goto step is the step that corresponds to the <Action> element identified in step 1. Translates the <EntryPoints> parent element as a Sequence Call step and inserts the step into the MainSequence. | The translator completes the following additional steps to add new functionality when translating the <ActionEntryPoints> element. Adds a Boolean parameter to the sequence that contains the Goto step. Specifies the value of the parameter as False. Specifies that the lookup string of the parameter is the precondition of the Goto step. Specifies that the Sequence Call step the translator created for the <EntryPoints> parent element passes a value of True for the Boolean parameter created in step 1. As a result, other Sequence Call steps that call the sequence in which the Goto step exists pass a default value of False for the Boolean parameter, and the Goto step executes only once. |
| When translating the <EntryPoints> child element of a <TestGroup> element of the TestGroupSequence type. | The translator creates an EntryPoints container local variable in the translated sequence and translates individual <EntryPoint> elements as child containers of the EntryPoints container. The translator also stores all attributes of an <EntryPoint> element under an Attributes container local variable. You must specify that the first step in the translated sequence is the primary entry point because the translator does not support any other option. | For an EntryPoint element with an ID attribute value that matches the value of the primaryEntryPointID attribute of the parent <EntryPoints> element, the translator inserts a Goto step as the first step of the Main step group in the translated sequence. The destination for the Goto step is the step the translator creates for a <Step> element with an ID attribute value that is the same as the value of the stepID attribute of the <EntryPoint> element. |
| The ATMLTDTypes.ini type palette file, located in the <TestStand Public>\\Components\\TypePalettes directory, contains data types from the TestDescription.xsd, Common.xsd, and HardwareCommon.xsd ATML TD schema files. The ATMLTD_IEEE1641_Types.ini type palette file, located in the same directory, contains data types from the STDTSF.xsd, STDBSC.xsd, and STDTSFLib.xsd IEEE Std 1641 standard schema files. | The types defined in both type palette files include an ATML prefix on the type names. The translator translates attributes defined in the ATML and IEEE 1641 schemas as a subproperty, named Attributes, in the types defined in TestStand. The translator translates XML elements and attributes with the name Value as a local variable, named ATML_Value, in the translated sequence. | The types defined in the ATMLTDTypes.ini type palette file include an NI_ATML prefix on the type names. The types defined in the ATMLTD_IEEE1641_Types.ini type palette file include an NI_ATMLSTD prefix on the type names. The translator translates attributes defined in the ATML and IEEE 1641 schemas as a subproperty, named ATMLAttributes, in the types defined in TestStand. The translator translates XML elements and attributes with the name Value as a local variable, named NI_ATMLValue, in the translated sequence. Note The ATML Toolkit 2010 does not correctly incrementally update sequence files you originally translated using the ATML Toolkit 1.0. The ATML Toolkit 2010 includes a Sequence File Updater application to convert sequence files you originally translated using the ATML Toolkit 1.0. |

Related concepts:

- ATML TD Schema File Data Types - Using TestStand Type Palette Files with the TD Translator
- IEEE 1641 Specification Data Types - Using TestStand Type Palette Files with the TD Translator

#### ATML Toolkit 2010 Bug Fixes

The following items are changes from the ATML Toolkit 1.0 to the ATML Toolkit 2010, unless
 otherwise specified.

[IMAGE alt='image' src='GUID-AF76D01C-C04D-4B25-B02A-9FE81B652CD3-a5.gif']

Toggle Expansion

Allow Blocked Content

[IMAGE alt='image' src='GUID-1B8F8764-5847-4A20-97A4-D2CB62944995-a5.gif']

| ID | Fixed Issue | Issue Details |
| --- | --- | --- |
| 215986 | Including the ATML Test Results report generator in a TestStand deployment installs the report generator to both TestStand 4.1.1 and TestStand 4.2 directories | If you install the ATML Test Results report generator component of the TestStand ATML Toolkit 1.0 for both TestStand 4.1.1 and TestStand 4.2, build a deployment, and run the deployment installer on a different computer, the installer installs the ATML Test Results report generator component in both the TestStand 4.1.1 and TestStand 4.2 directories, even if one of those versions of TestStand does not exist on the computer. |
| 255867 | The ATML Toolkit is not compatible with TestStand 2010 | TestStand 2010 introduces a restriction that prevents the translator from creating a subproperty named Attributes when the property also contains attributes. If the translator in the ATML Toolkit 1.0 encounters this restriction, the translator returns an error during translation. |

[IMAGE alt='image' src='GUID-1B8F8764-5847-4A20-97A4-D2CB62944995-a5.gif']

| ID | Fixed Issue | Issue Details |
| --- | --- | --- |
| 188737 | The ATML Toolkit 1.0 uninstaller does not remove the ATMLTD_IEEE1641_Types.ini type file from the <TestStand Public>\\Components\\TypePalettes directory | If you enable the Use IEEE 1641 Data Types in TestStand option on the General Settings tab of the ATML Test Description Translator Configuration dialog box, the translator adds the ATMLTD_IEEE1641_Types.ini file to the <TestStand Public>\\Components\\TypePalettes directory. Uninstalling the ATML Toolkit does not remove the ATMLTD_IEEE1641_Types.ini type file from the <TestStand Public>\\Components\\TypePalettes directory. |
| 201735 | The toolkit installs the TestStand ATML Toolkit Help in the default <TestStand>\\Doc\\Help directory when TestStand is not installed in the default installation directory | The toolkit installs the TestStand ATML Toolkit Help in the default <TestStand>\\Doc\\Help directory when TestStand is not installed in the default installation directory. |
| 218266 | The ATML Toolkit autorun.exe dialog box does not display correctly | The ATML Toolkit autorun.exe dialog box might not display correctly if you make a different window active after you launch the autorun.exe but before the autorun.exe dialog box displays. |
| 245573 | Reinstalling the ATML Toolkit creates duplicate Configure ATML TD Translator menu items in the Tools menu | If you repair the existing ATML Toolkit installation or uninstall and then reinstall the toolkit, the TestStand Tools menu includes a duplicate entry for the Configure ATML TD Translator menu item for each time you repaired or installed the toolkit. |

[IMAGE alt='image' src='GUID-1B8F8764-5847-4A20-97A4-D2CB62944995-a5.gif']

| ID | Fixed Issue | Issue Details |
| --- | --- | --- |
| 183549 | The translator does not recognize the installation of LabVIEW 2009 (64-bit) | The translator runs as a Windows 32-bit On Windows 64-bit (WoW64) process on 64-bit operating systems, which causes registry queries from the translator to be redirected to the Wow6432Node registry node and prevents the translator from recognizing the installation of 64-bit versions of LabVIEW in the 64-bit registry. |
| 186711 | Limit values for a custom step type that is similar to Numeric Limit Test, Multiple Numeric Limit Test, or String Value Test step types do not update during an incremental update | If the translator uses the customType attribute of an <Action> element to specify a custom step type and the custom step type definition is similar to the definition of the Numeric Limit Test, Multiple Numeric Limit Test, or String Value Test step types, the translator does not update the limit values of the step during an incremental update. |
| 186913 | The ATML Test Description Translator Configuration dialog box takes longer to load when the computer is connected to a network but not connected to the internet | The ATML Test Description Translator Configuration dialog box DLL contains a Microsoft Authenticode signature that causes the dialog box to take longer to load when the computer is connected to a network but not connected to the Internet. Refer to the Microsoft KnowledgeBase article 936707, located at support.microsoft.com/kb/936707, for more information about how Authenticode signatures affect application load times. |
| 198055 | Incremental update skips any <TestGroup> element of the TestGroupParallel type | The translator does not incrementally update a TestStand sequence the translator previously created for a <TestGroup> element of the TestGroupParallel type. |
| 201786 | The translator does not enable additional results for parameters of Sequence Call steps the translator creates for <Action> elements | The translator does not enable additional results for parameters of Sequence Call steps the translator creates for <Action> elements. |
| 208443 | The translator does not properly incrementally update <TestGroup> elements | If you remove a <TestGroup> element from a previously translated TD instance document, the translator does not properly remove the sequence the translator previously created for the <TestGroup> element during an incremental update. If you change the name of a <TestGroup> element in a previously translated TD instance document, translator does not properly update the name of the sequence the translator previously created for the <TestGroup> element during an incremental update. If two Sequence Call steps call into the same sequence, and during an incremental update the translator changes one of the Sequence Call steps to no longer call into the sequence, the translator incorrectly deletes the sequence from the sequence file even though a Sequence Call step that calls into the sequence still exists. |
| 209833 | The translator does not use the <NominalValue> child elements of <TestResult> elements to specify the default values for VI indicators | If an <Action> element contains <TestResult> elements, the translator uses the <TestResult> elements to store the output parameters of the <Action> element. If the LabVIEW code module the translator creates for such an <Action> element does not actually wire data to one of these output parameters, the indicator should default to the value that the <NominalValue> child element of the respective <TestResult> element specifies. When generating LabVIEW VIs, the translator does not specify the default values of indicators to match the values that the <NominalValue> elements of the respective <TestResult> elements specify. |
| 219534 | The translator does not properly recognize year-based versions of LabVIEW and LabWindows/CVI | The translator incorrectly evaluates year-based versions of LabVIEW and LabWindows/CVI as versions earlier than LabVIEW 8.2.1 and LabWindows/CVI 8.1.1. |
| 234677 | The translator incorrectly populates parameter values for a Sequence Call step that calls a sequence created for a <Step> element that exists under a <TestGroup> element of the TestGroupParallel type | The translator incorrectly populates parameter values for a Sequence Call step that calls a sequence created for a <Step> element that exists under a <TestGroup> element of the TestGroupParallel type and references an <Action> element that contains a <Behavior>/<TestGroupCall> child element. |
| 234678 | The translator hangs when you execute it in a LabVIEW-built user interface | The translator hangs when you execute it in a TestStand User Interface built with LabVIEW. |
| 243363 | The translator does not update the data source for Multiple Numeric Limit Test steps when the number of parameters exceeds the number of limits | The translator does not update the data source for Multiple Numeric Limit Test steps when the number of parameters exceeds the number of limits. |
| 286139 | The translator incorrectly skips some custom code generator callbacks during an incremental update | When performing an incremental update, the translator skips the TranslateTestGroup custom code generator callback for <TestGroup> elements and the PreTranslateStep and PostTranslateStep custom code generator callbacks for <Step> and <ActionReference> elements. |
| 289410 | The translator incorrectly specifies the Load Option and Step Failure Causes Sequence Failure run options for a step translated from an <ActionReference> element | The translator incorrectly specifies the Load Option and Step Failure Causes Sequence Failure run options for a step the translator creates for an <ActionReference> child element of a <TestGroup> element of the TestGroupParallel, TestGroupDiagnosticModel, TestGroupSerial, or TestGroupUnspecifiedOrder type. The translator incorrectly specifies Load dynamically for the Load Option run option and True for the Step Failure Causes Sequence Failure run option when the translator should specify Preload when execution begins and False, respectively. |
| 294302 | The translator returns the error 'Item is locked, protected, or in use and cannot be deleted.' when you use the example custom code generator VIs | The translator returns the error 'Item is locked, protected, or in use and cannot be deleted.' when you configure the translator to use the LabVIEW custom code generator VIs, located in the <TestStand Public>\\Components\\Translators\\ATMLTDTranslator\\Examples\\Code Generator\\LabVIEW directory. |
| 297288 | The translator does not properly call the LabVIEWParameter.UpdateClusterMapping method for container parameters of LabVIEW steps created for <ActionReference> child elements of <TestGroup> elements of the TestGroupParallel type | The translator does not properly call the LabVIEWParameter.UpdateClusterMapping method for container parameters of LabVIEW steps created for <ActionReference> child elements of <TestGroup> elements of the TestGroupParallel type. |
| 98211 | The translator hangs if you close the LabWindows/CVI environment during translation | Closing the LabWindows/CVI environment while the translator is generating LabWindows/CVI code modules causes the translator to hang. |

[IMAGE alt='image' src='GUID-1B8F8764-5847-4A20-97A4-D2CB62944995-a5.gif']

| ID | Fixed Issue | Issue Details |
| --- | --- | --- |
| 165526 | The ATML Test Results report generator does not correctly process the Default Numeric Format setting | The ATML Test Results report generator does not correctly process the setting you specify in the Default Numeric Format control on the Contents tab of the Report Options dialog box. When you select ATML Report Document from the Report Format ring control on the Contents tab of the Report Options dialog box, the Default Numeric Format control and Edit Format button are disabled. |
| 209830 | The ATML Test Results report generator does not process and include descriptions for Sequence Call steps in the ATML report | The ATML Test Results report generator does not process and include descriptions for Sequence Call steps in the ATML report. |
| 220888 | The ATML Test Results report generator does not process and include the results of step post actions in the ATML report | The ATML Test Results report generator does not process and include the results of step post actions in the ATML report. |
| 221937 | The ATML Test Results report generator omits Sequence Call step names from the ATML report | The ATML Test Results report generator omits Sequence Call step names from the ATML report and instead uses the generic name TestGroup to record Sequence Call steps. |
| 228564 | The ATML Test Results report generator does not include <Event>, <Data>, or <Description> elements under <TestGroup> elements in the ATML report | The ATML Test Results report generator does not include <Event>, <Data>, or <Description> elements under <TestGroup> elements in the ATML report. |
| 231930 | The ATML Test Results report generator does not include additional results when you enable the Is Limit option but do not enable the Is Measurement option | If you configure an additional result for a step and enable the Include in Report option, the generated ATML Test Results report displays the additional result. However, if you also enable the Is Limit option but do not enable the Is Measurement option, the report does not display the additional result. The report does correctly display the additional result if you enable the Include in Report and Is Measurement options but you do not enable the Is Limit option. |

Related concepts:

- Translating an Action Element with a customType Attribute
- Deriving ATML Test Results Elements from Translated TD Elements

<!--NI_TOPIC bundle=teststand-atml-toolkit path=ni-teststand-atml-toolkit-2018-help-42.html language=enus -->
## TOPIC 00029: TestStand ATML Toolkit Help

- bundle_id: `teststand-atml-toolkit`
- source_path: `ni-teststand-atml-toolkit-2018-help-42.html`
- source_url: https://docs-be.ni.com/bundle/teststand-atml-toolkit/raw/resource/enus/ni-teststand-atml-toolkit-2018-help-42.html
- document_id: `teststand-atml-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The ATML Toolkit documentation refers to XML concepts and assumes that you have a working knowledge of ATML, the ATML TD standard, XML, XML Path Language (XPath), XML Schema Document (XSD), and XQuery. Refer to the World Wide Web Consortium (W3C) website, located at www.w3.org, for more information

### TestStand ATML Toolkit Help

The ATML Toolkit documentation refers to XML concepts and assumes that you have a working
 knowledge of ATML, the ATML TD standard, XML, XML Path Language
 (XPath), XML Schema Document (XSD), and XQuery. Refer to the
 *World Wide Web Consortium (W3C)*
 website, located at www.w3.org, for more
 information about these technologies. You can find additional
 resources and tutorials online to help you learn these
 technologies.

<!--NI_TOPIC bundle=teststand-atml-toolkit path=overview.html language=enus -->
## TOPIC 00030: TestStand ATML Toolkit Overview

- bundle_id: `teststand-atml-toolkit`
- source_path: `overview.html`
- source_url: https://docs-be.ni.com/bundle/teststand-atml-toolkit/raw/resource/enus/overview.html
- document_id: `teststand-atml-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The TestStand ATML Toolkit helps you implement Automatic Test Markup Language (ATML) into TestStand applications. You can save development time by creating custom code generators that extend the code autogeneration to implement specific test code module functionality. The TestStand ATML Toolkit tran

### TestStand ATML Toolkit
 Overview

The TestStand ATML Toolkit helps you implement Automatic Test Markup Language (ATML) into
 TestStand applications. You can save development time by creating custom code generators
 that extend the code autogeneration to implement specific test code module
 functionality.

The TestStand ATML Toolkit translates ATML Test Description documents into TestStand
 sequences and code modules written in LabVIEW or LabWindows/CVI.

<!--NI_TOPIC bundle=teststand-atml-toolkit path=passing-parameters-to-labview-code-modules-10.html language=enus -->
## TOPIC 00031: Passing Parameters to LabVIEW Code Modules

- bundle_id: `teststand-atml-toolkit`
- source_path: `passing-parameters-to-labview-code-modules-10.html`
- source_url: https://docs-be.ni.com/bundle/teststand-atml-toolkit/raw/resource/enus/passing-parameters-to-labview-code-modules-10.html
- document_id: `teststand-atml-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following table lists the parameters the ATML TD translator always passes to a LabVIEW code module: Parameter Name Value Description Comments Sequence Context RunState.ThisContext Object reference The translator passes the Sequence Context parameter so you can access any variable in TestStand fr

### Passing Parameters to LabVIEW
 Code Modules

The following table lists the parameters the ATML TD translator always passes to a LabVIEW code
 module:

| Parameter Name | Value | Description | Comments |
| --- | --- | --- | --- |
| Sequence Context | RunState.ThisContext | Object reference | The translator passes the Sequence Context parameter so you can access any variable in TestStand from the generated VI. |
| <Parameter> element | — | — | <Parameter> elements are [In] parameters. |
| <TestResult> element | — | — | The <TestResult> element is an [Out] parameter. |
| PASS/FAIL Flag | Step.Result.PassFail | Boolean | A return value that indicates if the test passed or failed. The translator passes the PASS/FAIL Flag parameter to the code modules only if the translated step is a Pass/Fail Test step. |
| Error Out | Step.Result.Error | Container | A return value that contains the error state. LabVIEW passes the Error Out parameter back to TestStand. |

If the total number of [In] and [Out] parameters to pass to the VI is 28 or fewer, the translator
 places the local variable it creates for <Parameter>, The
 <TestResult> element under the Locals for the sequence. If the total
 number of parameters exceeds 28, the translator creates a container under the Locals for
 the sequence, names the container
 TestName_Parameters,
 TestName_TestResults, or
 TestName_SessionData, respectively, and
 passes the container to the LabVIEW code module as an object reference. The
 TestName is the value of the name attribute of
 the parent <Test> element.

The following table shows how the translator translates simple types for
 <Parameter> and <TestResult> elements
 that the TestDescription.xsd and Common.xsd
 ATML TD schema files define into TestStand and LabVIEW types.

| TestDescription.xsd Type | Common.xsd Type | TestStand Type | LabVIEW Type |
| --- | --- | --- | --- |
| unsignedInteger | unsignedInteger | Number with unsigned integer format | Numeric |
| string | String | String | String |
| octal | Octal | Number with octal format | Numeric |
| integer | Integer | Number | Numeric |
| hexadecimal | Hexadecimal | Number with hexadecimal format | Numeric |
| double | Double | Number with double numeric format | Numeric |
| binary | Binary | Number with binary format | Numeric |
| boolean | Boolean | Boolean | Boolean |

For the strict ATML TD types the ATMLTDTypes and ATMLTD_IEEE1641_Types type palette files define,
 the translator passes each type as a container to the code module. The translator passes
 all other types as object references.

Parent topic:

Creating LabVIEW Code Modules for Behavior Elements

Related concepts:

- Creating LabVIEW Code Modules for Behavior Elements
- ATML TD Standards
- ATML TD Schema File Data Types - Using TestStand Type Palette Files with the TD Translator
- IEEE 1641 Specification Data Types - Using TestStand Type Palette Files with the TD Translator
- Using TestStand Type Palette Files with the TD Translator

<!--NI_TOPIC bundle=teststand-atml-toolkit path=passing-parameters-to-labview-code-modules-11.html language=enus -->
## TOPIC 00032: Passing Parameters to LabVIEW Code Modules

- bundle_id: `teststand-atml-toolkit`
- source_path: `passing-parameters-to-labview-code-modules-11.html`
- source_url: https://docs-be.ni.com/bundle/teststand-atml-toolkit/raw/resource/enus/passing-parameters-to-labview-code-modules-11.html
- document_id: `teststand-atml-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following table lists the parameters the ATML TD translator always passes to a LabVIEW code module: Parameter Name Value Description Comments Sequence Context RunState.ThisContext Object reference The translator passes the Sequence Context parameter so you can access any variable in TestStand fr

### Passing Parameters to LabVIEW
 Code Modules

The following table lists the parameters the ATML TD translator always passes to a LabVIEW code
 module:

| Parameter Name | Value | Description | Comments |
| --- | --- | --- | --- |
| Sequence Context | RunState.ThisContext | Object reference | The translator passes the Sequence Context parameter so you can access any variable in TestStand from the generated VI. |
| <Parameter> element | — | — | <Parameter> elements are [In] parameters. |
| <TestResult> or <SessionDatum> element | — | — | <TestResult> and <SessionDatum> elements are [Out] parameters. |
| PASS/FAIL Flag | Step.Result.PassFail | Boolean | A return value that indicates if the test passed or failed. The translator passes the PASS/FAIL Flag parameter to the code modules only if the translated step is a Pass/Fail Test step. |
| Error Out | Step.Result.Error | Container | A return value that contains the error state. LabVIEW passes the Error Out parameter back to TestStand. |

If the total number of [In] and [Out] parameters to pass to the VI is 28 or fewer, the translator
 places the local variable it creates for <Parameter>,
 <TestResult>, and <SessionDatum>
 elements under the Locals for the sequence. If the total number of parameters exceeds
 28, the translator creates a container under the Locals for the sequence, names the
 container actionName_Parameters,
 actionName_TestResults, or
 actionName_SessionData, respectively, and
 passes the container to the LabVIEW code module as an object reference. The
 actionName is the value of the name attribute
 of the parent <Action> element.

ATML TD schema files define into TestStand and LabVIEW types. The following table shows how the
 translator translates simple types for <Parameter> and
 <TestResult> elements that the
 TestDescription.xsd and Common.xsd:

| TestDescription.xsd Type | Common.xsd Type | TestStand Type | LabVIEW Type |
| --- | --- | --- | --- |
| unsignedInteger | unsignedInteger | Number with unsigned integer format | Numeric |
| string | String | String | String |
| octal | Octal | Number with octal format | Numeric |
| integer | Integer | Number | Numeric |
| hexadecimal | Hexadecimal | Number with hexadecimal format | Numeric |
| double | Double | Number with double numeric format | Numeric |
| binary | Binary | Number with binary format | Numeric |
| boolean | Boolean | Boolean | Boolean |

For the strict ATML TD types the ATMLTDTypes and ATMLTD_IEEE1641_Types type palette files define,
 the translator passes each type as a container to the code module. The translator passes
 all other types as object references.

Parent topic:

Creating LabVIEW Code Modules for Behavior Elements

Related concepts:

- Creating LabVIEW Code Modules for Behavior Elements
- ATML TD Standards
- ATML TD Schema File Data Types - Using TestStand Type Palette Files with the TD Translator
- IEEE 1641 Specification Data Types - Using TestStand Type Palette Files with the TD Translator
- Using TestStand Type Palette Files with the TD Translator

<!--NI_TOPIC bundle=teststand-atml-toolkit path=passing-parameters-to-labwindows-cvi-code-mod.html language=enus -->
## TOPIC 00033: Passing Parameters to LabWindows/CVI Code Modules

- bundle_id: `teststand-atml-toolkit`
- source_path: `passing-parameters-to-labwindows-cvi-code-mod.html`
- source_url: https://docs-be.ni.com/bundle/teststand-atml-toolkit/raw/resource/enus/passing-parameters-to-labwindows-cvi-code-mod.html
- document_id: `teststand-atml-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following table lists the variables the ATML TD translator passes to a LabWindows/CVI code module: Variable Name Value Description Comments seqContextCVI RunState.ThisContext CAObjHandle The translator passes the SeqContextCVI parameter so you can access any variable in TestStand from the genera

### Passing Parameters to LabWindows/CVI
 Code Modules

The following table lists the variables the ATML TD translator passes to a LabWindows/CVI code
 module:

| Variable Name | Value | Description | Comments |
| --- | --- | --- | --- |
| seqContextCVI | RunState.ThisContext | CAObjHandle | The translator passes the SeqContextCVI parameter so you can access any variable in TestStand from the generated LabWindows/CVI code module. |
| <Parameter> element | — | — | <Parameter> elements are [In] parameters. |
| <TestResult> or <SessionDatum> element | — | — | <TestResult> and <SessionDatum> elements are [In/Out] parameters. |
| PassFailResult | Step.Result.PassFail | long* | A Boolean that indicates if the test passed or failed. The translator passes the PassFailResult parameter to the code modules only if the translated step is a Pass/Fail Test step. |
| errorOccurred | Step.Result.Error.Occurred | long* | Boolean variable to set if an error occurs in the code module. |
| errorCode | Step.Result.Error.Code | long* | Number that indicates the code of the error that occurred. |
| errorMsg | Step.Result.Error.Msg | char[1024] | String that indicates the error message. |

The translator passes the following parameters of the step created for an
 <Action> element to the code modules by value:

- The translator passes each string type parameter as a const char * .
- The translator passes <TestResult> and <SessionDatum> elements to code modules as pointers so you can set and return the value to TestStand.
- If the <TestResult> or <SessionDatum> element
 contains a <DatumDescription> child element with an
 xsi:type attribute value of stringDescription ,
 the translator passes the parent <TestResult> or
 <SessionDatum> element as char
 [1024] .
- The translator passes each Boolean value as long .
- Some types, such as dateTime and complex, have strict type definitions and are available in
 ATMLCVITypes.h , which is located in the
 <TestStand>\Components\Translators\ATMLTDTranslator\CodeModule Templates\CVI 
 directory. The translator passes these types to the code modules as structures.
- The translator passes any other type that does not have a strict type definition as a CAObjHandle.

If the total number of [In] and [Out] parameters to pass to the LabWindows/CVI function is 32 or
 fewer, the translator places the local variable it creates for
 <Parameter>, <TestResult>, and
 <SessionDatum> elements under the Locals for the sequence. If
 the total number of parameters exceeds 32, the translator creates a container under the
 Locals for the sequence, names the container
 actionName_Parameters,
 actionName_TestResults, or
 actionName_SessionData, respectively, and
 passes the container to the function as an object reference. The
 actionName is the value of the name attribute
 of the parent <Action> element.

Parent topic:

Creating LabWindows/CVI Code Modules for Behavior Elements

Related concepts:

- Creating LabWindows/CVI Code Modules for Behavior Elements

<!--NI_TOPIC bundle=teststand-atml-toolkit path=passing-parameters-to-labwindows-cvi-code-mod2.html language=enus -->
## TOPIC 00034: Passing Parameters to LabWindows/CVI Code Modules

- bundle_id: `teststand-atml-toolkit`
- source_path: `passing-parameters-to-labwindows-cvi-code-mod2.html`
- source_url: https://docs-be.ni.com/bundle/teststand-atml-toolkit/raw/resource/enus/passing-parameters-to-labwindows-cvi-code-mod2.html
- document_id: `teststand-atml-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following table lists the variables the ATML TD translator passes to a LabWindows/CVI code module: Variable Name Value Description Comments seqContextCVI RunState.ThisContext CAObjHandle The translator passes the SeqContextCVI parameter so you can access any variable in TestStand from the genera

### Passing Parameters to LabWindows/CVI
 Code Modules

The following table lists the variables the ATML TD translator passes to a LabWindows/CVI code
 module:

| Variable Name | Value | Description | Comments |
| --- | --- | --- | --- |
| seqContextCVI | RunState.ThisContext | CAObjHandle | The translator passes the SeqContextCVI parameter so you can access any variable in TestStand from the generated LabWindows/CVI code module. |
| <Parameter> element | — | — | <Parameter> elements are [In] parameters. |
| <TestResult> element | — | — | <TestResult> elements are [In/Out] parameters. |
| PassFailResult | Step.Result.PassFail | long* | A Boolean that indicates if the test passed or failed. The translator passes the PassFailResult parameter to the code modules only if the translated step is a Pass/Fail Test step. |
| errorOccurred | Step.Result.Error.Occurred | long* | Boolean variable to set if an error occurs in the code module. |
| errorCode | Step.Result.Error.Code | long* | Number that indicates the code of the error that occurred. |
| errorMsg | Step.Result.Error.Msg | char[1024] | String that indicates the error message. |

The translator passes the following parameters of the step created for an
 <Test> element to the code modules by value:

- The translator passes each string type parameter as a const char * .
- The translator passes <TestResult> elements to code modules as pointers so you can set and return the value to TestStand.
- If the <TestResult> element contains a
 <DatumDescription> child element with an
 xsi:type attribute value of stringDescription ,
 the translator passes the parent <TestResult> element as
 char [1024] .
- The translator passes each Boolean value as long .
- Some types, such as dateTime and complex, have strict type definitions and are available in
 ATMLCVITypes.h , which is located in the
 <TestStand>\Components\Translators\ATMLTDTranslator\CodeModule Templates\CVI 
 directory. The translator passes these types to the code modules as structures.
- The translator passes any other type that does not have a strict type definition as a CAObjHandle.

If the total number of [In] and [Out] parameters to pass to the LabWindows/CVI function is 32 or fewer, the translator places the local variable it creates for <Parameter>, and <TestResult> elements under the Locals for the sequence. If the total number of parameters exceeds 32, the translator creates a container under the Locals for the sequence, names the container TestName_Parameters, or TestName_TestResults, respectively, and passes the container to the function as an object reference. The TestName is the value of the name attribute of the parent <Test> element.

Parent topic:

Creating LabWindows/CVI Code Modules for Behavior Elements

Related concepts:

- Creating LabWindows/CVI Code Modules for Behavior Elements

<!--NI_TOPIC bundle=teststand-atml-toolkit path=post-translation-recommended-actions-section.html language=enus -->
## TOPIC 00035: Post-Translation Recommended Actions Section - Logging Translation Information

- bundle_id: `teststand-atml-toolkit`
- source_path: `post-translation-recommended-actions-section.html`
- source_url: https://docs-be.ni.com/bundle/teststand-atml-toolkit/raw/resource/enus/post-translation-recommended-actions-section.html
- document_id: `teststand-atml-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The ATML TD translator cannot translate all elements in a source TD instance document to TestStand constructs, such as sequences, steps, or code modules. The translator stores these elements in TestStand variables, attributes, or comments, but the generated sequence file does not use the variables,

### Post-Translation Recommended Actions Section -
 Logging Translation Information

The ATML TD translator cannot translate all elements in a source TD instance document to
 TestStand constructs, such as sequences, steps, or code modules. The translator stores
 these elements in TestStand variables, attributes, or comments, but the generated
 sequence file does not use the variables, attributes, or comments.

The post-translation recommended actions section of the log file lists the elements the
 translator translated but cannot implement. It also describes how you must implement the
 required functionality to complete the test program the source TD instance document
 originally described.

The log file uses subsections for the sequences and steps that contain the information you must
 implement.

Parent topic:

Logging Translation Information

Related concepts:

- Completing the Partial Test Program

<!--NI_TOPIC bundle=teststand-atml-toolkit path=recommended-labwindows-cvi-function-prototype.html language=enus -->
## TOPIC 00036: Recommended LabWindows/CVI Function Prototypes

- bundle_id: `teststand-atml-toolkit`
- source_path: `recommended-labwindows-cvi-function-prototype.html`
- source_url: https://docs-be.ni.com/bundle/teststand-atml-toolkit/raw/resource/enus/recommended-labwindows-cvi-function-prototype.html
- document_id: `teststand-atml-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the example project and source files located in the <TestStand Public>\Examples\Toolkits\ATMLTDTranslator\Code Generator\CVI directory as a starting point for implementing a LabWindows/CVI function that calls a specific code generator callback.Use a function prototype for each callback the LabWi

### Recommended LabWindows/CVI Function
 Prototypes

Use the example project and source files located in the
 <TestStand Public>\Examples\Toolkits\ATMLTDTranslator\Code
 Generator\CVI directory as a starting point for implementing a
 LabWindows/CVI function that calls a specific code generator callback.

Use a function prototype for each callback the LabWindows/CVI custom code generator uses. Refer
 to the individual callback topics for more information about the LabWindows/CVI function
 prototype for each callback.

Complete the following steps to use the example project and source files to generate complete
 LabWindows/CVI code modules:

1. In LabWindows/CVI, open
 <TestStand Public>\Examples\Toolkits\ATMLTDTranslator\Code
 Generator\CVI\CVICodeGenerator.prj .
2. Build the project to generate the dll .
3. In TestStand, select Tools»Configure ATML TD Translator to launch the ATML Test Description Translator
 Configuration dialog box.
4. Click the Code Module Settings tab and enable the LabWindows/CVI option.
5. Click the Browse button next to the Path to Custom Code
 Generator DLL control and browse to the path of the
 dll you built in step 2.
6. Click OK to close the ATML Test Description Translator
 Configuration dialog box.
7. Close all open sequence files.
8. In TestStand, select File»Open File to launch the File Open dialog box.
9. Browse to <TestStand Public>\Examples\Toolkits\ATMLTDTranslator\Translator\Test
 Description 1.0\Computer 1.0.xml .
10. Click Open to translate the TD instance document to a TestStand sequence file and a set of LabWindows/CVI code modules.
11. Review the translated sequence file and the generated code modules. Note If an
 <Action> or <Test> element
 contains a child element of the OperationConnect,
 OperationRead, or OperationDisconnect
 type, the translator creates new Connect,
 Read, or Disconnect functions and precedes
 each function name with the name of the source <Action>
 or <Test> element. For each element of the
 OperationConnect, OperationRead, or
 OperationDisconnect type that exists under a parent
 <Action> or <Test> element,
 the translator updates the function body with a call to the newly created
 functions. The example demonstrates how to insert a new parameter named
 UUID, which TestStand passes to the code module, and how to
 change the flags of the Step and Sequence elements to non-editable and
 non-deletable, respectively.

#### Incremental Update
 [IMAGE alt='image' src='GUID-10242244-39C8-44B3-AAC3-6C5701803D28-a5.gif']

Complete the steps in the
 *Calling a LabWindows/CVI Custom Code Generator DLL during an Incremental
 Update* section for information about using a LabWindows/CVI custom code
 generator dll when you incrementally update a previously
 translated sequence file.

Parent topic:

Implementing a LabWindows/CVI Custom Code Generator

Related concepts:

- Calling a LabWindows/CVI Custom Code Generator dll during an Incremental Update
- Creating a dll for a LabWindows/CVI Custom Code Generator
- Creating LabWindows/CVI Code Modules for Behavior Elements

<!--NI_TOPIC bundle=teststand-atml-toolkit path=recommended-microsoft-visual-c-function-proto.html language=enus -->
## TOPIC 00037: Recommended Microsoft Visual C++ Function Prototypes

- bundle_id: `teststand-atml-toolkit`
- source_path: `recommended-microsoft-visual-c-function-proto.html`
- source_url: https://docs-be.ni.com/bundle/teststand-atml-toolkit/raw/resource/enus/recommended-microsoft-visual-c-function-proto.html
- document_id: `teststand-atml-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: When you use Microsoft Visual C++ to create a function to implement a LabWindows/CVI custom code generator, the manufacturer recommends a function prototype for each callback the LabWindows/CVI custom code generator uses.Refer to the individual callback topics for more information about the Visual C

### Recommended Microsoft Visual C++ Function
 Prototypes

When you use Microsoft Visual C++ to create a function to implement a LabWindows/CVI custom code
 generator, the manufacturer recommends a function prototype for each callback the
 LabWindows/CVI custom code generator uses.

Refer to the individual callback topics for more information about the Visual C++ function prototype for each callback.

LabWindows/CVI Custom Code Generator

Note

CodeGenerator_PreTranslateAction()

Note

stdcall

.def

dll

Parent topic:

Implementing a LabWindows/CVI Custom Code Generator

Related concepts:

- Creating a dll for a LabWindows/CVI Custom Code Generator

<!--NI_TOPIC bundle=teststand-atml-toolkit path=restrictions-in-a-td-instance-document-145.html language=enus -->
## TOPIC 00038: Restrictions in a TD Instance Document

- bundle_id: `teststand-atml-toolkit`
- source_path: `restrictions-in-a-td-instance-document-145.html`
- source_url: https://docs-be.ni.com/bundle/teststand-atml-toolkit/raw/resource/enus/restrictions-in-a-td-instance-document-145.html
- document_id: `teststand-atml-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: If a TD instance document violates a restriction, the log file records the violation as an error. TestStand has the following restrictions when translating a TD instance document to a sequence file: The number of dimensions in an array must be less than 17. The number of elements in each dimension o

### Restrictions in a TD Instance Document

If a TD instance document violates a restriction, the log file records the violation as an error.
 TestStand has the following restrictions when translating a TD instance document to a
 sequence file:

- The number of dimensions in an array must be less than 17.
- The number of elements in each dimension of the array must be a positive number.
- Invalid characters must not be present in the name attribute of the
 <TestGroup> , <Action> ,
 <Parameters> , <TestResults> or
 <SessionData> elements. Invalid characters include ~ ! @
 # $ % ^ & * = + ` " : ' ; ? > < , . / [ ] \ \ | } {
- All steps translated from <Action> elements with a parameter value of the
 ValueFromTestGroupParameter type that refers to a <TestGroup> 
 parameter, or translated from <Action> elements with a
 <TestResults> / <TestResult> child
 element that contains a <ValueToTestResult> child element
 that refers to the <Step> / <Result> 
 child element of the <TestGroup> element, must exist in the
 test group.
- <Parameter> child elements of the <Action> element
 cannot be of the ValueFromActionParameter type.
- The value of all attributes in the elements of an array must be the same.
- <Parameter> elements of the <Collection> type must
 contain at least one <Item> child element.

Parent topic:

Translating a TD Instance Document to a TestStand Sequence File

<!--NI_TOPIC bundle=teststand-atml-toolkit path=specifying-default-values-for-indicators-in-v.html language=enus -->
## TOPIC 00039: Specifying Default Values for Indicators in VIs

- bundle_id: `teststand-atml-toolkit`
- source_path: `specifying-default-values-for-indicators-in-v.html`
- source_url: https://docs-be.ni.com/bundle/teststand-atml-toolkit/raw/resource/enus/specifying-default-values-for-indicators-in-v.html
- document_id: `teststand-atml-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: If a <Test> element contains one or more <TestResult> child elements, the ATML TD translator inserts an indicator in the VI for each <TestResult> element. If the <DatumDescription> and <IndexedArrayDescription> child elements of a <TestResult> element contain <NominalValue> or <NominalElementValue>

### Specifying Default Values for Indicators in
 VIs

If a <Test> element contains one or more
 <TestResult> child elements, the ATML TD translator inserts
 an indicator in the VI for each <TestResult> element.

If the <DatumDescription> and
 <IndexedArrayDescription> child elements of a
 <TestResult> element contain
 <NominalValue> or
 <NominalElementValue> child elements, respectively, the
 translator specifies the default value for the indicator.

The default value for the indicator is the value of the local variable the translator creates for
 the <TestResult> element in the sequence file so that the
 indicator returns the default value the translator specifies when you run the VI.
 However, if you wire or modify the indicator with any other value in the VI, the
 indicator returns the value you wire or modify.

#### Incremental Update
 [IMAGE alt='image' src='GUID-10242244-39C8-44B3-AAC3-6C5701803D28-a5.gif']

If in the source TD instance
 document you add or modify any of the following elements and you incrementally
 update the sequence file, the translator adds or modifies the default value for the
 indicator that corresponds to the parent <TestResult>
 element:

- <NominalValue>
- <NominalElementValue> child element of the
 <DatumDescription>
- <IndexedArrayDescription>

If in the source TD instance document you delete any of the elements listed
 above and you incrementally update the sequence file, the translator does not modify
 the default value for the indicator that corresponds to the parent
 <TestResult> element.

Parent topic:

TestStand ATML Toolkit Help

<!--NI_TOPIC bundle=teststand-atml-toolkit path=specifying-default-values-for-indicators-in-v2.html language=enus -->
## TOPIC 00040: Specifying Default Values for Indicators in VIs

- bundle_id: `teststand-atml-toolkit`
- source_path: `specifying-default-values-for-indicators-in-v2.html`
- source_url: https://docs-be.ni.com/bundle/teststand-atml-toolkit/raw/resource/enus/specifying-default-values-for-indicators-in-v2.html
- document_id: `teststand-atml-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: If an <Action> element contains one or more <TestResult> child elements, the ATML TD translator inserts an indicator in the VI for each <TestResult> element.If the <DatumDescription>, <IndexedArrayDescription>, and <CollectionDescription> child elements of a <TestResult> element contain <NominalValu

### Specifying Default Values for Indicators in
 VIs

If an <Action> element contains one or more
 <TestResult> child elements, the ATML TD translator inserts
 an indicator in the VI for each <TestResult> element.

If the <DatumDescription>,
 <IndexedArrayDescription>, and
 <CollectionDescription> child elements of a
 <TestResult> element contain
 <NominalValue> or
 <NominalElementValue> child elements, respectively, the
 translator specifies the default value for the indicator.

The default value for the indicator is the value of the local variable the translator creates for
 the <TestResult> element in the sequence file so that the
 indicator returns the default value the translator specifies when you run the VI.
 However, if you wire or modify the indicator with any other value in the VI, the
 indicator returns the value you wire or modify.

#### Incremental Update
 [IMAGE alt='image' src='GUID-10242244-39C8-44B3-AAC3-6C5701803D28-a5.gif']

If in the source TD instance document you add or modify any of
 the following elements and you incrementally update the sequence file, the
 translator adds or modifies the default value for the indicator that corresponds to
 the parent <TestResult> element:

- <NominalValue>
- <NominalElementValue> child element of the
 <DatumDescription>
- <IndexedArrayDescription>

If in the source TD instance document you delete any of the elements listed
 above and you incrementally update the sequence file, the translator does not modify
 the default value for the indicator that corresponds to the parent
 <TestResult> element.

Parent topic:

TestStand ATML Toolkit Help

<!--NI_TOPIC bundle=teststand-atml-toolkit path=storing-td-instance-document-attributes-in-a.html language=enus -->
## TOPIC 00041: Storing TD Instance Document Attributes in a Translated Sequence

- bundle_id: `teststand-atml-toolkit`
- source_path: `storing-td-instance-document-attributes-in-a.html`
- source_url: https://docs-be.ni.com/bundle/teststand-atml-toolkit/raw/resource/enus/storing-td-instance-document-attributes-in-a.html
- document_id: `teststand-atml-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: ATML TD instance documents define attributes for most elements.TestStand uses the NI.ATML.TDTranslator.ATMLAttributes namespace to store ATML TD attributes in the attributes of the TestStand construct, such as: step variable sequence sequence file Use the Attributes dialog box in TestStand to view t

### Storing TD Instance Document Attributes in a
 Translated Sequence

ATML TD instance documents define attributes for most elements.

TestStand uses the NI.ATML.TDTranslator.ATMLAttributes namespace to store ATML
 TD attributes in the attributes of the TestStand construct, such as:

- step
- variable
- sequence
- sequence file

Attributes

PropertyObject

Note

TS.SData.ActualArgs

Parent topic:

TestStand ATML Toolkit Help

<!--NI_TOPIC bundle=teststand-atml-toolkit path=storing-td-instance-document-attributes-in-a_2.html language=enus -->
## TOPIC 00042: Storing TD Instance Document Attributes in a Translated Sequence

- bundle_id: `teststand-atml-toolkit`
- source_path: `storing-td-instance-document-attributes-in-a_2.html`
- source_url: https://docs-be.ni.com/bundle/teststand-atml-toolkit/raw/resource/enus/storing-td-instance-document-attributes-in-a_2.html
- document_id: `teststand-atml-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: ATML TD instance documents define attributes for most elements.TestStand uses the NI.ATML.TDTranslator.ATMLAttributes namespace to store ATML TD attributes in the attributes of the TestStand construct, such as: step variable sequence sequence file Use the Attributes dialog box in TestStand to view t

### Storing TD Instance Document Attributes in a
 Translated Sequence

ATML TD instance documents define attributes for most elements.

TestStand uses the NI.ATML.TDTranslator.ATMLAttributes namespace to store ATML
 TD attributes in the attributes of the TestStand construct, such as:

- step
- variable
- sequence
- sequence file

Attributes

PropertyObject

Note

TS.SData.ActualArgs

Parent topic:

TestStand ATML Toolkit Help

<!--NI_TOPIC bundle=teststand-atml-toolkit path=translating-a-td-instance-document-to-a-tests.html language=enus -->
## TOPIC 00043: Translating a TD Instance Document to a TestStand Sequence File

- bundle_id: `teststand-atml-toolkit`
- source_path: `translating-a-td-instance-document-to-a-tests.html`
- source_url: https://docs-be.ni.com/bundle/teststand-atml-toolkit/raw/resource/enus/translating-a-td-instance-document-to-a-tests.html
- document_id: `teststand-atml-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: An ATML Test Description (TD) instance document is a document that validates against the ATML TD schema. The ATML TD translator uses the translator framework included in TestStand 4.0 or later to translate a TD instance document into a TestStand sequence file.The translator translates some elements

### Translating a TD Instance Document to a
 TestStand Sequence File

An ATML Test Description (TD) instance document is a document that validates against the ATML TD
 schema. The ATML TD translator uses the translator framework included in TestStand 4.0
 or later to translate a TD instance document into a TestStand sequence file.

Note

Note

The ATML Toolkit includes an example ATML TD instance document that you can use to learn how to
 get started with translating a TD instance document to a partial test program.

If you modify the information in the source TD instance document after you have already
 translated the TD instance document to a sequence file, you can incrementally update the
 existing sequence file and code modules to reflect the changes in the source TD instance
 document.

Refer to the individual TD element topics in this help file for more information about how the translator translates each element in the TD instance document to a TestStand construct and for more information to complete the partial test program.

Parent topic:

TestStand ATML Toolkit Help

Related concepts:

- ATML TD Standards
- Completing the Partial Test Program
- Getting Started with the ATML TD Translator
- Incrementally Updating a Translated Sequence File
- Translation Process Overview

<!--NI_TOPIC bundle=teststand-atml-toolkit path=translating-a-test-element-with-a-customtype.html language=enus -->
## TOPIC 00044: Translating a Test Element with a customType Attribute

- bundle_id: `teststand-atml-toolkit`
- source_path: `translating-a-test-element-with-a-customtype.html`
- source_url: https://docs-be.ni.com/bundle/teststand-atml-toolkit/raw/resource/enus/translating-a-test-element-with-a-customtype.html
- document_id: `teststand-atml-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: When you specify the customType attribute for a <Test> element, the ATML TD translator creates a custom step type for the translated Test using the type that the value of the customType attribute specifies.If the value of the customType attribute specifies a step type with a default adapter that req

### Translating a Test Element with a customType
 Attribute

When you specify the customType attribute for a <Test>
 element, the ATML TD translator creates a custom step type for the translated Test using
 the type that the value of the customType attribute specifies.

If the value of the customType attribute specifies a step type with a default
 adapter that requires code modules, the translator does not create code modules for the
 step.

customType

name

name

<Parameter>

<TestResult>

Note

Parent topic:

TestStand ATML Toolkit Help

<!--NI_TOPIC bundle=teststand-atml-toolkit path=translating-an-action-element-with-a-customty.html language=enus -->
## TOPIC 00045: Translating an Action Element with a customType Attribute

- bundle_id: `teststand-atml-toolkit`
- source_path: `translating-an-action-element-with-a-customty.html`
- source_url: https://docs-be.ni.com/bundle/teststand-atml-toolkit/raw/resource/enus/translating-an-action-element-with-a-customty.html
- document_id: `teststand-atml-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: When you specify the customType attribute for an <Action> element, the ATML TD translator creates a custom step type for the translated action using the type that the value of the customType attribute specifies.If the value of the customType attribute specifies a step type with a default adapter tha

### Translating an Action Element with a
 customType Attribute

When you specify the customType attribute for an <Action>
 element, the ATML TD translator creates a custom step type for the translated action
 using the type that the value of the customType attribute
 specifies.

If the value of the customType attribute specifies a step type with a default
 adapter that requires code modules, the translator does not create code modules for the
 step.

customType

name

name

<Parameter>

<TestResult>

<SessionDatum>

Note

Parent topic:

TestStand ATML Toolkit Help

<!--NI_TOPIC bundle=teststand-atml-toolkit path=translating-elements-and-types-with-no-strict.html language=enus -->
## TOPIC 00046: Translating Elements and Types with No Strict Type Definitions

- bundle_id: `teststand-atml-toolkit`
- source_path: `translating-elements-and-types-with-no-strict.html`
- source_url: https://docs-be.ni.com/bundle/teststand-atml-toolkit/raw/resource/enus/translating-elements-and-types-with-no-strict.html
- document_id: `teststand-atml-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The translator creates some ATML TD elements and types as equivalent TestStand data types.The translator uses the following guidelines to create a PropertyObject variable in TestStand for every element or type in the TD instance document with the limitations specified above. The created variable mai

### Translating Elements and Types with No Strict
 Type Definitions

The translator creates some ATML TD elements and types as equivalent TestStand data types.

The translator uses the following guidelines to create a PropertyObject
 variable in TestStand for every element or type in the TD instance document with the
 limitations specified above. The created variable maintains the parent-child
 relationship and stores the attributes specified for each element.

- If an element contains child elements and attributes, the translator creates a
 PropertyObject container, with the same name as the
 element, to contain all the PropertyObject created for the
 child elements. If an element contains two or more child elements with the same
 name, the translator appends _1 , _2 , and so on to
 the names.
- Incremental Update
 [IMAGE alt='image' src='GUID-10242244-39C8-44B3-AAC3-6C5701803D28-a5.gif'] —If an element contains child elements, the translator updates the
 PropertyObject containers created for each
 child element according to the following rules:
  - If the child element includes an ID attribute,
 the translator uses the ID to uniquely identify the child
 element. If the element does not define an ID 
 attribute, the translator uses all attributes to uniquely
 identify the child element.
  - If the translator locates a PropertyObject 
 for the child element in the translated sequence file, the
 translator recursively updates the child element. If the
 translator cannot locate a PropertyObject 
 for the child element, the translator creates a new
 PropertyObject for the child element
 and records the change in the log file.
  - If additional child elements exist in the translated sequence
 file after the translator completes adding or updating all child
 elements from the source TD instance document, the translator
 deletes the extra elements from the sequence file and records
 the change in the log file.
- If an element contains only attributes, the translator creates a
 PropertyObject container named ATMLAttributes under the
 PropertyObject created for the element to contain all the
 attributes as strings. The translator sets the name of the string variable to the
 name of the attribute and sets the value of the string to the value of the
 attribute.
  - Incremental Update 
 [IMAGE alt='image' src='GUID-10242244-39C8-44B3-AAC3-6C5701803D28-a5.gif'] - If an element contains attributes
 the ATMLAttributes container of a PropertyObject 
 created, the translator updates the element according to the attributes
 defined for the element.
- If an element is a text element with no attributes, the translator creates a string variable
 with the same name as the element. The translator sets the value of the string to
 the value of the element.
  - Incremental Update 
 [IMAGE alt='image' src='GUID-10242244-39C8-44B3-AAC3-6C5701803D28-a5.gif'] - If an XML element is a text element
 with no attributes, the translator updates the value of the string variable
 with the same name as the element.

If the translator encounters an element or attribute with the name Value in the
 TD instance document, the translator creates a corresponding TestStand variable named
 NI_ATMLValue because Value is a reserved keyword
 in TestStand.

Parent topic:

TestStand ATML Toolkit Help

Related concepts:

- Using TestStand Type Palette Files with the TD Translator
- Logging Translation Information

<!--NI_TOPIC bundle=teststand-atml-toolkit path=translation-process-overview-194.html language=enus -->
## TOPIC 00047: Translation Process Overview

- bundle_id: `teststand-atml-toolkit`
- source_path: `translation-process-overview-194.html`
- source_url: https://docs-be.ni.com/bundle/teststand-atml-toolkit/raw/resource/enus/translation-process-overview-194.html
- document_id: `teststand-atml-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following diagram shows the flow of steps the ATML TD translator completes when translating a source TD instance document. Matching colors indicate corresponding begin/end or Setup/Cleanup steps. Elements are based on XML order.

### Translation Process Overview

Note

[IMAGE alt='image' src='GUID-0F1E38B7-DDAD-4C36-8118-FA5C1C0E7AB5-a5.gif']

Parent topic:

Translating a TD Instance Document to a TestStand Sequence File

<!--NI_TOPIC bundle=teststand-atml-toolkit path=translation-section-logging-translation-infor.html language=enus -->
## TOPIC 00048: Translation Section - Logging Translation Information

- bundle_id: `teststand-atml-toolkit`
- source_path: `translation-section-logging-translation-infor.html`
- source_url: https://docs-be.ni.com/bundle/teststand-atml-toolkit/raw/resource/enus/translation-section-logging-translation-infor.html
- document_id: `teststand-atml-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The translation section of the log file includes a table that contains all the actions performed during translation. This table might contain additional warnings. You must resolve these warnings before you can run the TestStand sequence file and code module is generated.If a TD instance document vio

### Translation Section - Logging Translation
 Information

The translation section of the log file includes a table that contains all the actions performed
 during translation. This table might contain additional warnings. You must resolve these
 warnings before you can run the TestStand sequence file and code module is
 generated.

If a TD instance document violates a TestStand-imposed restriction, the log file records the
 restriction as an error.

Parent topic:

Logging Translation Information

Related concepts:

- Restrictions in a TD Instance Document

<!--NI_TOPIC bundle=teststand-atml-toolkit path=user-manual-welcome.html language=enus -->
## TOPIC 00049: TestStand ATML Toolkit User Manual

- bundle_id: `teststand-atml-toolkit`
- source_path: `user-manual-welcome.html`
- source_url: https://docs-be.ni.com/bundle/teststand-atml-toolkit/raw/resource/enus/user-manual-welcome.html
- document_id: `teststand-atml-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The TestStand ATML Toolkit User Manual provides detailed descriptions of the product functionality and the step by step processes for use. Looking for Something Else?For information not found in the User Manual for your product, such as specifications and API reference, browse Related Information.

### TestStand ATML Toolkit
 User Manual

The TestStand ATML Toolkit User Manual provides detailed
 descriptions of the product functionality and the step by step processes for use.

#### Looking for Something Else?

For information not found in the User Manual
 for your product, such as specifications and API reference, browse *Related
 Information*.

Related information:

- Hardware and Software Operating System
 Compatibility
- License Setup and Activation

<!--NI_TOPIC bundle=teststand-atml-toolkit path=using-teststand-type-palette-files-with-the-t.html language=enus -->
## TOPIC 00050: Using TestStand Type Palette Files with the TD Translator

- bundle_id: `teststand-atml-toolkit`
- source_path: `using-teststand-type-palette-files-with-the-t.html`
- source_url: https://docs-be.ni.com/bundle/teststand-atml-toolkit/raw/resource/enus/using-teststand-type-palette-files-with-the-t.html
- document_id: `teststand-atml-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The ATMLTDTypes.ini and ATMLTD_IEEE1641_Types.ini TestStand type palette files contain TestStand data type equivalents of simple and strict TD elements and types, which the ATML schemas define. The type palette files also specify the format for passing the data types to LabVIEW and LabWindows/CVI co

### Using TestStand Type Palette Files with the
 TD Translator

The ATMLTDTypes.ini and ATMLTD_IEEE1641_Types.ini
 TestStand type palette files contain TestStand data type equivalents of simple and
 strict TD elements and types, which the ATML schemas define. The type palette files also
 specify the format for passing the data types to LabVIEW and LabWindows/CVI code
 modules. The ATML TD translator also provides a C-style header file for all types the
 type palette files define.

When translating the following elements, the translator uses the type palette files to create in
 the sequence file instances of data types equivalent to the TD types:

- <Parameter> , <TestResult> , and
 <SessionDatum> child elements of the
 <Action> element
- <ParameterDescription> and <TestResultDescription> 
 child elements of the <TestGroup> element

For each <xs:SimpleType> and <xs:ComplexType>
 element that exists in a schema that the source TD instance document references, the
 translator creates a corresponding data type in TestStand. The name of the TestStand
 data type is the same as the value of the name attribute of the
 <xs:SimpleType> or <xs:ComplexType>
 element. The names of the TestStand data types the ATMLTDTypes.ini
 type palette file contains include an NI_ATML prefix, and the names of
 the TestStand data types the ATMLTD_IEEE1641_Types.ini type palette
 file contains include an NI_ATMLSTD prefix.

However, the type palette files do not contain the data type equivalents for the following
 <xs:ComplexType> elements:

- <xs:ComplexType> elements that recursively use the type or element
- <xs:ComplexType> elements that contain <xs:any> , <xs:anyAttribute> , or <xs:choice> child elements

The translator creates in TestStand a container named ATMLAttributes that contains string
 variables for the XML attributes of <xs:SimpleType> or
 <xs:ComplexType> elements. The name of each string variable
 is the same as the name of the XML attribute. The translator translates XML elements and
 attributes with the name Value as a local variable named
 NI_ATMLValue in the translated sequence.

Parent topic:

Translating a TD Instance Document to a TestStand Sequence File

Related concepts:

- ATML TD Schema File Data Types - Using TestStand Type Palette Files with the TD Translator
- IEEE 1641 Specification Data Types - Using TestStand Type Palette Files with the TD Translator
- ATML TD Standards
- Translating Elements and Types with No Strict Type Definitions

<!--NI_TOPIC bundle=teststand-atml-toolkit path=validation-section-logging-translation-inform.html language=enus -->
## TOPIC 00051: Validation Section - Logging Translation Information

- bundle_id: `teststand-atml-toolkit`
- source_path: `validation-section-logging-translation-inform.html`
- source_url: https://docs-be.ni.com/bundle/teststand-atml-toolkit/raw/resource/enus/validation-section-logging-translation-inform.html
- document_id: `teststand-atml-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: The validation section of the log file includes a table that contains all the errors and warnings the ATML TD translator finds when translating the TD instance document.When you enable the Stop Translation if Validation Fails option on the General Settings tab of the ATML Test Description Translator

### Validation Section - Logging Translation
 Information

The validation section of the log file includes a table that contains all the errors and warnings
 the ATML TD translator finds when translating the TD instance document.

When you enable the Stop Translation if Validation Fails option on the General
 Settings tab of the ATML Test Description Translator
 Configuration dialog box, the ATML TD translator returns errors if the
 TD instance document does not validate against the ATML TD schema or if the TD instance
 document violates constraints the ATML TD standard defines. The translator uses the
 following schema files located in the directory you specify in the ATML Test
 Description Schema Location control on the General
 Settings tab of the ATML Test Description Translator
 Configuration dialog box to validate the TD instance document before
 translating it:

- TestDescription.xsd
- Common.xsd
- HardwareCommon.xsd
- STDBSC.xsd
- STDTSF.xsd
- STDTSFLib.xsd
- DatumTypes.xsd
- Operations.xsd
- IeeeStd1641.xsd

You must resolve all errors to complete a successful translation. Warnings usually relate to
 tasks to complete, and you might need to resolve the warnings before you can completely
 execute the generated TestStand sequence file and code module.

In most cases, if any errors occur when translating a TD instance document or incrementally
 updating a translated sequence file, the translator does not generate any files but
 continues translating to locate all errors.

Parent topic:

Logging Translation Information

Related concepts:

- ATML TD Standards
- Incrementally Updating a Translated Sequence File

<!--NI_TOPIC bundle=teststand-atml-toolkit path=year-based-and-major-minor-version-equivalent.html language=enus -->
## TOPIC 00052: Year-Based and Major.Minor Version Equivalents

- bundle_id: `teststand-atml-toolkit`
- source_path: `year-based-and-major-minor-version-equivalent.html`
- source_url: https://docs-be.ni.com/bundle/teststand-atml-toolkit/raw/resource/enus/year-based-and-major-minor-version-equivalent.html
- document_id: `teststand-atml-toolkit`
- page_type: `leaf`
- content_type: `concept`
- source_description: Versions of the TestStand ATML Toolkit that follow year-based versioning continue to use major.minor notation for some features. The following table lists year-based TestStand ATML Toolkit versions and the equivalent major.minor notation. Year-Based Version Major.Minor Version TestStand ATML Toolkit

### Year-Based and Major.Minor Version
 Equivalents

Versions of the TestStand ATML Toolkit that follow year-based versioning continue to use
 major.minor notation for some features. The following table lists
 year-based TestStand ATML Toolkit versions and the equivalent
 major.minor notation.

| Year-Based Version | Major.Minor Version |
| --- | --- |
| TestStand ATML Toolkit 2017 | 5.0 |
| TestStand ATML Toolkit 2013 | 4.0 |
| TestStand ATML Toolkit 2012 | 3.0 |
| TestStand ATML Toolkit 2010 | 2.0 |
