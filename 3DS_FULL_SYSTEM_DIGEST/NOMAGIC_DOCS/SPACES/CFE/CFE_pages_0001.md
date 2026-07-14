# NOMAGIC DOCUMENTATION SPACE: CATIA FLXML Exporter

<!--NOMAGIC_SPACE key=CFE chunk=1 -->

<!--NOMAGIC_PAGE id=304014829 space=CFE version=1 -->
## PAGE 00001: (2026x Refresh1) CATIA FLXML Exporter

- page_id: `304014829`
- space_key: `CFE`
- source_url: https://docs.nomagic.com/spaces/CFE/pages/304014829/2026x+Refresh1+CATIA+FLXML+Exporter
- version_number: 1
- version_date: `2026-04-29T17:00:30.431+02:00`
- ancestors: Versions of CATIA FLXML Exporter
- labels: []

### NORMALIZED CONTENT

The CATIA FLXML Exporter plugin allows you to transform a UML/SysML v1/UAF model to functional and logical structures supported in the **3D**EXPERIENCEplatform. The plugin uses the FLXML Generation Engine and the element transformation schema to generate an FLXM file from the selected model elements. The conversion of CATIA Magic data to **3D**EXPERIENCEplatform data with lifecycle management is based on element mapping.

You can later [import the generated FLXML file to the **3D**EXPERIENCE platform](https://help.3ds.com/2024x/English/DSDoc/FleUserMap/fle-t-XMLImport.htm?ContextScope=onpremise) while ensuring the digital continuity and master interfaces of system architecture (with sub-systems developed in **3D**EXPERIENCEPlatform, CATIA Magic, or other tools). The CATIA FLXM Exporter plugin also helps to initiate the transition from the conceptual to the design layer.

#### NOTE: Prerequisites

Prerequisites

To be able to export the selected part of a model to an FLXML file, you need to [CONFLUENCE_PAGE title='Installing modeling tools and plugins' space='IL'] in your modeling tool.

[IMAGE alt='' src='']

###### The schema displaying how the CATIA FLXML Exporter plugin works.

[IMAGE alt='' src='']

###### Using the CATIA FLXML Exporter plugin ensures the digital continuity and master interfaces of the system architecture.

##### Exporting model data to FLXML

To export model data to an FLXML file, follow the steps described below.

To export model data to an FLXML file

1. In the main menu of a modeling tool, go to 3DEXPERIENCE > CATIA FLXML Exporter > Generate FLXML . The CATIA FLXML Exporter dialog opens. [ATTACHMENT filename='CATIA_FLXML_exporter_dialog.png']
2. In the open dialog, click [ATTACHMENT filename='select_scope.png'] next to the Scope elements box and select the scope of elements to be included in the generated FLXML file: [IMAGE alt='' src=''] By default, all elements owned by the selected scope element are included when generating an FLXML file.If the selected scope element is a diagram, the scope of the FLXML file generation will be the elements displayed in the diagram.If a certain element type is not included in the default element mapping schema, the elements of this type are excluded when generating an FLXML file.
  1. In the Tree view of the Select scope elements dialog, select the elements you want to export. (Press and hold the Ctrl key to select multiple elements.)
  2. Click [ATTACHMENT filename='add_scope.png'] to add the elements to the Selected elements list.
  3. Click OK to close the dialog.
3. In the List of available schemas box, select the default SysML to FL schema or a custom schema.
4. Click [ATTACHMENT filename='select_scope.png'] next to the Destination folder box and select the folder where the generated FLXML file should be stored.
5. In the CATIA FLXML Exporter dialog, click OK to start the export.
6. If you get the message saying that some validation errors were found, do one of the following:
  1. Click Yes to ignore the validation errors and generate an FLXML file anyway.
  2. Click No to correct the errors in the open validation results panel. Then try exporting your model to an FLXML file again.

After completing the above steps, an FLXML file is generated and saved in the destination folder. In addition, the **CATIA FLXM Results** window opens, where you can view and filter the export results or fix the validation errors.

##### Exporting FLXML results

Once you , the **CATIA FLXML Results** panel opens, displaying the export results. The results include both transformed and not transformed elements and file generation errors. You can export FLXML results to an MS Excel file as described below.

To export FLXML results to an MS Excel file

1. In the CATIA FLXML Results panel, click [ATTACHMENT filename='export_MSExcel.png'] . [ATTACHMENT filename='exporting_FLXML_results.png']
2. In the Select Destination Directory dialog, select the folder where you want to save the file with FLXML results and click Save .

The MS Excel file with FLXML results is automatically opened and saved in the specified directory.

**Additional resources**

- [ATTACHMENT filename='CATIA FLXML Exporter Plugin.mp4']
- [ATTACHMENT filename='CATIA FLXML Exporter Plugin - Effectivity.mp4']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p>The CATIA FLXML Exporter plugin allows you to transform a UML/SysML v1/UAF model to functional and logical structures supported in the <span style="color:var(--ds-text-accent-purple-bolder,#352c63);"><strong>3D</strong>EXPERIENCE </span>platform. The plugin uses the FLXML Generation Engine and the element transformation schema to generate an FLXM file from the selected model elements. The conversion of CATIA Magic data to <span style="color:var(--ds-text-accent-purple-bolder,#352c63);"><strong>3D</strong>EXPERIENCE </span>platform data with lifecycle management is based on element mapping.</p><p>You can later <a href="https://help.3ds.com/2024x/English/DSDoc/FleUserMap/fle-t-XMLImport.htm?ContextScope=onpremise">import the generated FLXML file to the <strong>3D</strong>EXPERIENCE platform</a> while ensuring the digital continuity and master interfaces of system architecture (with sub-systems developed in <span style="color:var(--ds-text-accent-purple-bolder,#352c63);"><strong>3D</strong>EXPERIENCE </span>Platform, CATIA Magic, or other tools). The CATIA FLXM Exporter plugin also helps to initiate the transition from the conceptual to the design layer.</p><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="e9e33596-f72b-4bba-95d4-5b8d1a8a2ba0"><ac:rich-text-body>For detailed information about the CATIA FLXML Exporter plugin, see <ac:link><ri:attachment ri:filename="CATIA FLXML Exporter Plugin User Guide.pdf"><ri:page ri:content-title="(2026x Refresh1) CATIA FLXML Exporter" /></ri:attachment></ac:link></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="08ec6ff2-aa94-4b92-935a-679517a15172"><ac:parameter ac:name="title">Prerequisites</ac:parameter><ac:rich-text-body><p>To be able to export the selected part of a model to an FLXML file, you need to <ac:link><ri:page ri:space-key="IL" ri:content-title="Installing modeling tools and plugins" /><ac:plain-text-link-body><![CDATA[install the CATIA FLXML Exporter Plugin]]></ac:plain-text-link-body></ac:link> in your modeling tool.</p></ac:rich-text-body></ac:structured-macro><p><br /></p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="flxml_exporter_plugin.png"><ri:page ri:content-title="(2026x Refresh1) CATIA FLXML Exporter" /></ri:attachment></ac:image></p><h6 style="text-align: center;">The schema displaying how the CATIA FLXML Exporter plugin works.</h6><p><ac:image ac:align="center"><ri:attachment ri:filename="importing_flxml_file.png"><ri:page ri:content-title="(2026x Refresh1) CATIA FLXML Exporter" /></ri:attachment></ac:image></p><h6 style="text-align: center;">Using the CATIA FLXML Exporter plugin ensures the digital continuity and master interfaces of the system architecture.</h6><h3><br />Exporting model data to FLXML</h3><p>To export model data to an FLXML file, follow the steps described below.</p><p><br /></p><p>To export model data to an FLXML file</p><hr /><ol><li data-uuid="a48a8e44-44cf-4b6a-8b56-bcfefab966d6">In the main menu of a modeling tool, go to <strong>3DEXPERIENCE</strong> &gt; <strong>CATIA FLXML Exporter</strong> &gt; <strong>Generate FLXML</strong>. The <strong>CATIA FLXML Exporter</strong> dialog opens.<br /><br /><ac:image><ri:attachment ri:filename="CATIA_FLXML_exporter_dialog.png"><ri:page ri:content-title="(2026x Refresh1) CATIA FLXML Exporter" /></ri:attachment></ac:image><br /><br /></li><li data-uuid="319e7254-c634-4d78-8593-8625051fabe3">In the open dialog, click <ac:image ac:thumbnail="true" ac:height="23"><ri:attachment ri:filename="select_scope.png"><ri:page ri:content-title="(2026x Refresh1) CATIA FLXML Exporter" /></ri:attachment></ac:image> next to the <strong>Scope elements</strong> box and select the scope of elements to be included in the generated FLXML file:<ol><li>In the <strong>Tree</strong> view of the <strong>Select scope elements</strong> dialog, select the elements you want to export. (Press and hold the <strong>Ctrl</strong> key to select multiple elements.)</li><li>Click <ac:image><ri:attachment ri:filename="add_scope.png"><ri:page ri:content-title="(2026x Refresh1) CATIA FLXML Exporter" /></ri:attachment></ac:image> to add the elements to the <strong>Selected elements</strong> list.</li><li>Click <strong>OK</strong> to close the dialog.<br /><br /></li></ol><p class="auto-cursor-target"><ac:image><ri:attachment ri:filename="selecting_scope.png"><ri:page ri:content-title="(2026x Refresh1) CATIA FLXML Exporter" /></ri:attachment></ac:image><br /><br /></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="a758e3dc-f4aa-44a5-95e9-0ad14e942469"><ac:rich-text-body><ul><li><p>By default, all elements owned by the selected scope element are included when generating an FLXML file.</p></li><li><p><span>If the selected scope element is a diagram, the scope of the FLXML file generation will be the elements displayed in the diagram.</span></p></li><li><p>If a certain element type is not included in the default element mapping schema, the elements of this type are excluded when generating an FLXML file.<span><br /></span></p></li></ul></ac:rich-text-body></ac:structured-macro></li><li data-uuid="0e0ce91a-a94e-4676-8336-98cd872fa28f">In the <strong>List of available schemas</strong> box, select the default <strong>SysML to FL</strong> schema or a custom schema.</li><li data-uuid="85d307ff-bcc1-4194-bb70-618241efb89b">Click <ac:image ac:thumbnail="true" ac:height="23"><ri:attachment ri:filename="select_scope.png"><ri:page ri:content-title="(2026x Refresh1) CATIA FLXML Exporter" /></ri:attachment></ac:image> next to the <strong>Destination folder</strong> box and select the folder where the generated FLXML file should be stored.</li><li data-uuid="f893effd-673d-42d0-b8bb-4d1dcd14bcb8">In the <strong>CATIA FLXML Exporter</strong> dialog, click <strong>OK</strong> to start the export.</li><li data-uuid="a187afdf-1e50-4536-9c99-cd943067a422">If you get the message saying that some validation errors were found, do one of the following:<ol><li>Click <strong>Yes</strong> to ignore the validation errors and generate an FLXML file anyway.</li><li>Click <strong>No</strong> to correct the errors in the open validation results panel. Then try exporting your model to an FLXML file again.</li></ol></li></ol><p><br />After completing the above steps, an FLXML file is generated and saved in the destination folder. In addition, the <strong>CATIA FLXM Results</strong> window opens, where you can view and filter the export results or fix the validation errors.</p><h3><br />Exporting FLXML results</h3><p>Once you <ac:link ac:anchor="Exporting model data to FLXML"><ac:plain-text-link-body><![CDATA[export model data to an FLXML file]]></ac:plain-text-link-body></ac:link>, the <strong>CATIA FLXML Results</strong> panel opens, displaying the export results. The results include both transformed and not transformed elements and file generation errors. You can export FLXML results to an MS Excel file as described below.</p><p><br /></p><p>To export FLXML results to an MS Excel file</p><hr /><ol><li data-uuid="3bcd02b7-28a5-43fc-af13-8e25358f931e">In the <strong>CATIA FLXML Results</strong> panel, click <ac:image><ri:attachment ri:filename="export_MSExcel.png"><ri:page ri:content-title="(2026x Refresh1) CATIA FLXML Exporter" /></ri:attachment></ac:image>.<br /><br /><ac:image><ri:attachment ri:filename="exporting_FLXML_results.png"><ri:page ri:content-title="(2026x Refresh1) CATIA FLXML Exporter" /></ri:attachment></ac:image><br /><br /></li><li data-uuid="adbfa74a-8329-4295-8bd3-75de146b53a7">In the <strong>Select Destination Directory</strong> dialog, select the folder where you want to save the file with FLXML results and click <strong>Save</strong>.</li></ol><p><br />The MS Excel file with FLXML results is automatically opened and saved in the specified directory.</p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><strong>Additional resources</strong></p><ul><li data-uuid="41edfe68-aa58-4da3-9389-1d239c1952cd"><ac:link><ri:attachment ri:filename="CATIA FLXML Exporter Plugin.mp4"><ri:page ri:content-title="(2026x Refresh1) CATIA FLXML Exporter" /></ri:attachment></ac:link></li><li data-uuid="51410989-ec31-4ad4-bb41-b7c15b9df4ea"><ac:link><ri:attachment ri:filename="CATIA FLXML Exporter Plugin - Effectivity.mp4"><ri:page ri:content-title="(2026x Refresh1) CATIA FLXML Exporter" /></ri:attachment></ac:link></li></ul></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=304014846 space=CFE version=1 -->
## PAGE 00002: (2026x Refresh1) Exporting images of model diagrams

- page_id: `304014846`
- space_key: `CFE`
- source_url: https://docs.nomagic.com/spaces/CFE/pages/304014846/2026x+Refresh1+Exporting+images+of+model+diagrams
- version_number: 1
- version_date: `2026-04-29T17:00:30.694+02:00`
- ancestors: Versions of CATIA FLXML Exporter > (2026x Refresh1) CATIA FLXML Exporter
- labels: ['msosa', 'mcse', 'msa']

### NORMALIZED CONTENT

The CATIA FLXML plugin allows you to export the images of elements if the CustomImageHolder has been set to an element transformed to an FL reference in the **3D**EXPERIENCEplatform. For example, the diagram displayed below can be exported as the following logical view.

[IMAGE alt='' src='']

###### An example of exporting the image of a model diagram.

To export images of model elements

1. In the main menu of a modeling tool, go to Options > Environment .
2. On the left side of the Environment Options dialog, select CATIA FLXML Exporter option group.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>The CATIA FLXML plugin allows you to export the images of elements if the CustomImageHolder has been set to an element transformed to an FL reference in the <span style="color: rgb(55,65,81);"><strong>3D</strong>EXPERIENCE </span>platform. For example, the diagram displayed below can be exported as the following logical view.</p><p><br /></p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="image_export_example.png"><ri:page ri:content-title="(2026x Refresh1) Exporting images of model diagrams" /></ri:attachment></ac:image></p><h6 style="text-align: center;">An example of exporting the image of a model diagram.</h6><p>To export images of model elements</p><hr /><ol><li>In the main menu of a modeling tool, go to <strong>Options</strong> &gt; <strong>Environment</strong>.</li><li>On the left side of the <strong>Environment Options</strong> dialog, select <strong>CATIA FLXML Exporter</strong> option group.</li></ol><p><br /></p>
````

<!--NOMAGIC_PAGE id=304014842 space=CFE version=1 -->
## PAGE 00003: (2026x Refresh1) Running the CATIA FLXML Exporter plugin in command line

- page_id: `304014842`
- space_key: `CFE`
- source_url: https://docs.nomagic.com/spaces/CFE/pages/304014842/2026x+Refresh1+Running+the+CATIA+FLXML+Exporter+plugin+in+command+line
- version_number: 1
- version_date: `2026-04-29T17:00:30.622+02:00`
- ancestors: Versions of CATIA FLXML Exporter > (2026x Refresh1) CATIA FLXML Exporter
- labels: ['msosa', 'mcse', 'msa']

### NORMALIZED CONTENT

You can execute the CATIA FLXML Exporter plugin by using the command line interface both on the server and on the client machine.

#### NOTE: Important

Important

- Before starting, learn how to [CONFLUENCE_PAGE title='Running programs in batch mode' space='DEVG'] .
- When running the CATIA FLFML Exporter plugin in the command line, follow the recommended usage of the plugin described above. Any other usage of the plugin must be avoided
- Before starting, you must study the model and find out what data you want to export to an FLXML file.
- Each client can have a different configuration (e.g., Windows, Linux, etc.), so the execution of the plugin should be adapted to the client configuration.

To run the plugin and export model data to an FLXML file by using the command line

1. Download the [ATTACHMENT filename='generate_flxml.properties'] file.
2. In the generate_flxml.proprties file, specify .
3. Runthe CATIA FLXML Exporter plugin and export model data in one of the following ways:
  - Download and execute the *[ATTACHMENT filename='script_commandline.bat']* script. Executing the script_comandline.bat scriptBefore executing the script, make sure to replace the placeholders between <> with the actual values for the following properties:**%MAGICDRAW_HOME%** - specify the path to the modeling tool installation directory.**properties** - specify the path to the *generate_flxml.properties* file.
  - Implement the *com.nomagic.magicdraw.commandline.CommandLineAction*interface as described in [CONFLUENCE_PAGE title='Running programs in batch mode' space='DEVG'].

##### The CATIA FLXML Exporter plugin options

To export model data to an FLXML file by using the command line interface you have to specify the following properties in the *generate_flxml.properties* file.

| Property | Mandatory | Description |
| --- | --- | --- |
| project | Yes | Specify the path to the project you want to use to generate an FLXML file, e.g., e:\\data\\Aircraft Avionic.mdzip |
| schema | Yes | Specify the RFLP schema used to convert model elements to FL objects during export. You can use the default RFLP schema - SysML to FL or specify a custom schema. |
| destination_folder | Yes | Specify the path to the folder where the FLXML file should be saved. If the folder does not exist, it will be created during file generation. |
| scope_elements | Yes | Specify the list of elements to be exported to an FLXML file. Separate each element by a semicolon (;). Elements can be specified as:Element qualified name.Element ID. When specifying an element ID, use this format: id:<element_ID>Example:White box::Logical architecture::Logical architecture;id:_19_0_1_1a800cf_1559826887570_81532_41786;id:_19_0_1_1a800cf_1559826887379_499848_41443 |
| no_flxml_if_error | No | Set to true (the default value) for the command line execution to stop automatically if an error occurs while generating an FLXML file. In addition, the error text will be displayed in the console.Set to false to generate the FLXM file even if any generation errors occur. |
| log_results | No | Set to true if you want to generate a file with model data export results. The file includes export errors and both converted and not converted objects. It is saved in the same directory as the generated FLXML file. Otherwise, set to false (the default value). |
| log_format | No | The log_format property is only valid if the log_results property is set to true.Specify the file format for the model data export results (the log_results property). The possible values are:xls - an MS Excel file is generated.txt - a text file is generated.xlstxt - both MS Excel and text files are generated. |
| log_info | No | The log_info property is only valid if the log_results property is set to true.Set to true (the default value) if you do not want the annotations of converted and not converted objects to be included in the model data export results (the log_results property). Otherwise, set to false. |
| option_auto_ports | No | Set to true to automatically generate interfaces in the FLXML file if ports or pins do not exist in the UML/SysML v1 model. Otherwise, set to false (the default value). |
| option_escalated_links | No | Set to true to generate and manage the escalated link. Otherwise, set to false (the default option). |
| option_reference_out_of_scope_elements | No | Set to true (the default value) to automatically manage the references to elements located outside of the model data export scope (the scope_elements property). Otherwise, set to false. |
| option_dependecy_relationships | No | Set to true to automatically discover dependency relationships for each element (can be time-consuming). Otherwise, set to false (the default value). |
| option_create_top_refref_implement_links | No | Set to true to automatically create REF-REF implement links for an OCC-OCC link if the REF-REF implement links do not exist. Otherwise, set to false (the default value). |
| option_manage_effectivity | No | Set to true to generate effectivity files and a modified FLXML file to support effectivity. Otherwise, set to false (the default value). |
| option_export_image_for_diagrams | No | Set to true to generate images for symbol diagrams that you can later import to the 3DEXPERIENCE platform. Otherwise, set to false (the default value). |
| option_flxml_preview | No | Set to true (the default value) to generate an RFLXML file to be imported to the CATIA Systems Traceability in the 3DEXPERIENCE platform. Otherwise, set to false. |
| option_export_element_image | No | Set to true to generate images for FL references of the elements with the «CustomImageHolder» stereotype. Otherwise, set to false (the default value). |
| import_xml_file | No | Specify the path to the file that defines the XMLModel used by CATFLEditorImportBatch. This will allow you to modify XmlPath (and ImagePath if required).For more information about the file, see https://dsdoc.dsone.3ds.com/3DEXPERIENCER2021x/en/English/DSDocDSExa.htm?show=SadUserMap/fle-r-BatchForImportExport.htm&XMLToc=DSDocDS.xml&contextscope=onpremise |

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>You can execute the CATIA FLXML Exporter plugin by using the command line interface both on the server and on the client machine.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="a6d812ea-c2c8-43cd-94f9-feb625fa06c6"><ac:parameter ac:name="title">Important</ac:parameter><ac:rich-text-body><ul><li>Before starting, learn how to <ac:link><ri:page ri:space-key="DEVG" ri:content-title="Running programs in batch mode" /><ac:plain-text-link-body><![CDATA[run modeling tools and plugins by using the command line]]></ac:plain-text-link-body></ac:link>.</li><li>When running the CATIA FLFML Exporter plugin in the command line, follow the recommended usage of the plugin described above. Any other usage of the plugin must be avoided</li><li>Before starting, you must study the model and find out what data you want to export to an FLXML file.</li><li><p>Each client can have a different configuration (e.g., Windows, Linux, etc.), so the execution of the plugin should be adapted to the client configuration.</p></li></ul></ac:rich-text-body></ac:structured-macro><p><br /></p><p>To run the plugin and export model data to an FLXML file by using the command line</p><hr /><ol><li>Download the <em><ac:link><ri:attachment ri:filename="generate_flxml.properties"><ri:page ri:content-title="(2026x Refresh1) Running the CATIA FLXML Exporter plugin in command line" /></ri:attachment></ac:link></em><em> </em>file.</li><li>In the <em>generate_flxml.proprties</em> file, specify <ac:link ac:anchor="The CATIA FLXML Exporter plugin options"><ac:plain-text-link-body><![CDATA[project and export-related properties]]></ac:plain-text-link-body></ac:link>.</li><li><p><span style="color:var(--ds-text,#333333);">Run </span><span style="color:var(--ds-text,#333333);">the CATIA FLXML Exporter plugin and export model data in one of the following ways:</span></p><ul><li><p><span style="color:var(--ds-text,#333333);">Download and execute the <em><ac:link><ri:attachment ri:filename="script_commandline.bat"><ri:page ri:content-title="(2026x Refresh1) Running the CATIA FLXML Exporter plugin in command line" /></ri:attachment></ac:link></em> script.</span></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="f57c53e3-0491-465b-8e60-72f3527f2161"><ac:parameter ac:name="title">Executing the script_comandline.bat script</ac:parameter><ac:rich-text-body><p>Before executing the script, make sure to replace the placeholders between &lt;&gt; with the actual values for the following properties:</p><ul><li><strong>%MAGICDRAW_HOME%</strong> - specify the path to the modeling tool installation directory.</li><li><strong>properties</strong> - specify the path to the <em>generate_flxml.properties</em> file.</li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></li><li><p><span style="color:var(--ds-text,#333333);">Implement the <em style="text-align: left;">com.nomagic.magicdraw.commandline.CommandLineAction</em><span> </span>interface as described in <ac:link><ri:page ri:space-key="DEVG" ri:content-title="Running programs in batch mode" /></ac:link>.</span></p></li></ul></li></ol><h3><span style="color:var(--ds-text,#333333);"><br />The CATIA FLXML Exporter plugin options</span></h3><p>To export model data to an FLXML file by using the command line interface you have to specify the following properties in the <em>generate_flxml.properties</em> file.</p><table class="relative-table wrapped" style="width: 63.6314%;"><colgroup><col style="width: 22.2606%;" /><col style="width: 13.201%;" /><col style="width: 64.5384%;" /></colgroup><tbody><tr><th>Property</th><th colspan="1">Mandatory</th><th>Description</th></tr><tr><td><strong>project</strong></td><td colspan="1">Yes</td><td>Specify the path to the project you want to use to generate an FLXML file, e.g., e:\\data\\Aircraft Avionic.mdzip</td></tr><tr><td><strong>schema</strong></td><td colspan="1">Yes</td><td>Specify the RFLP schema used to convert model elements to FL objects during export. You can use the default RFLP schema - SysML to FL or specify a custom schema.</td></tr><tr><td><strong>destination_folder</strong></td><td colspan="1">Yes</td><td>Specify the path to the folder where the FLXML file should be saved. If the folder does not exist, it will be created during file generation.</td></tr><tr><td><strong>scope_elements</strong></td><td colspan="1">Yes</td><td><p>Specify the list of elements to be exported to an FLXML file. Separate each element by a semicolon (;). Elements can be specified as:</p><ul><li>Element qualified name.</li><li>Element ID. When specifying an element ID, use this format: <em>id:&lt;element_ID&gt;</em></li></ul><p>Example:</p><p>White box::Logical architecture::Logical architecture;id:_19_0_1_1a800cf_1559826887570_81532_41786;id:_19_0_1_1a800cf_1559826887379_499848_41443</p></td></tr><tr><td><strong>no_flxml_if_error</strong></td><td colspan="1">No</td><td><p>Set to <em>true</em> (the default value) for the command line execution to stop automatically if an error occurs while generating an FLXML file. In addition, the error text will be displayed in the console.</p><p>Set to <em>false</em> to generate the FLXM file even if any generation errors occur.</p></td></tr><tr><td><strong>log_results</strong></td><td colspan="1">No</td><td><p>Set to <em>true</em> if you want to generate a file with model data export results. The file includes export errors and both converted and not converted objects. It is saved in the same directory as the generated FLXML file. Otherwise, set to <em>false</em> (the default value).</p></td></tr><tr><td><strong>log_format</strong></td><td colspan="1">No</td><td><div class="content-wrapper"><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="988e56d2-ce59-4ff0-88ab-dbb238cb8cf6"><ac:rich-text-body><p>The <strong>log_format</strong> property is only valid if the <strong>log_results</strong> property is set to true.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target">Specify the file format for the model data export results (the <strong>log_results</strong> property). The possible values are:</p><ul><li class="auto-cursor-target"><strong>xls</strong> - an MS Excel file is generated.</li><li class="auto-cursor-target"><strong>txt</strong> - a text file is generated.</li><li class="auto-cursor-target"><strong>xlstxt</strong> - both MS Excel and text files are generated.</li></ul></div></td></tr><tr><td><strong>log_info</strong></td><td colspan="1">No</td><td><div class="content-wrapper"><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="0a8b309a-34fa-427c-b011-edfdd6871454"><ac:rich-text-body><p>The <strong>log_info</strong> property is only valid if the <strong>log_results</strong> property is set to true.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target">Set to <em>true</em> (the default value) if you do not want the annotations of converted and not converted objects to be included in the model data export results (the <strong>log_results</strong> property). Otherwise, set to <em>false</em>.</p></div></td></tr><tr><td colspan="1"><strong>option_auto_ports</strong></td><td colspan="1">No</td><td colspan="1">Set to <em>true</em> to automatically generate interfaces in the FLXML file if ports or pins do not exist in the UML/SysML v1 model. Otherwise, set to <em>false</em> (the default value).</td></tr><tr><td colspan="1"><strong>option_escalated_links</strong></td><td colspan="1">No</td><td colspan="1">Set to <em>true</em> to generate and manage the escalated link. Otherwise, set to <em>false</em> (the default option).</td></tr><tr><td colspan="1"><strong>option_reference_out_of_scope_elements</strong></td><td colspan="1">No</td><td colspan="1">Set to <em>true</em> (the default value) to automatically manage the references to elements located outside of the model data export scope (the <strong>scope_elements</strong> property). Otherwise, set to <em>false</em>.</td></tr><tr><td colspan="1"><strong>option_dependecy_relationships</strong></td><td colspan="1">No</td><td colspan="1">Set to <em>true</em> to automatically discover dependency relationships for each element (can be time-consuming). Otherwise, set to <em>false</em> (the default value).</td></tr><tr><td colspan="1"><strong>option_create_top_refref_implement_links</strong></td><td colspan="1">No</td><td colspan="1">Set to <em>true</em> to automatically create REF-REF implement links for an OCC-OCC link if the REF-REF implement links do not exist. Otherwise, set to <em>false</em> (the default value).</td></tr><tr><td colspan="1"><p><strong>option_manage_effectivity</strong></p></td><td colspan="1">No</td><td colspan="1">Set to <em>true</em> to generate effectivity files and a modified FLXML file to support effectivity. Otherwise, set to <em>false</em> (the default value).</td></tr><tr><td colspan="1"><strong>option_export_image_for_diagrams</strong></td><td colspan="1">No</td><td colspan="1">Set to <em>true</em> to generate images for symbol diagrams that you can later import to the <span style="color:var(--ds-text-accent-purple-bolder,#352c63);"><strong>3D</strong>EXPERIENCE </span>platform. Otherwise, set to <em>false</em> (the default value).</td></tr><tr><td colspan="1"><p><strong>option_flxml_preview</strong></p></td><td colspan="1">No</td><td colspan="1">Set to <em>true</em> (the default value) to generate an RFLXML file to be imported to the CATIA Systems Traceability in the <span style="color:var(--ds-text-accent-purple-bolder,#352c63);"><strong>3D</strong>EXPERIENCE </span>platform. Otherwise, set to <em>false</em>.</td></tr><tr><td colspan="1"><strong>option_export_element_image</strong></td><td colspan="1">No</td><td colspan="1">Set to <em>true</em> to generate images for FL references of the elements with the «CustomImageHolder» stereotype. Otherwise, set to <em>false</em> (the default value).</td></tr><tr><td colspan="1"><strong>import_xml_file</strong></td><td colspan="1">No</td><td colspan="1"><p>Specify the path to the file that defines the XMLModel used by <em>CATFLEditorImportBatch</em>. This will allow you to modify XmlPath (and ImagePath if required).</p><p>For more information about the file, see <a href="https://dsdoc.dsone.3ds.com/3DEXPERIENCER2021x/en/English/DSDocDSExa.htm?show=SadUserMap/fle-r-BatchForImportExport.htm&amp;XMLToc=DSDocDS.xml&amp;contextscope=onpremise">https://dsdoc.dsone.3ds.com/3DEXPERIENCER2021x/en/English/DSDocDSExa.htm?show=SadUserMap/fle-r-BatchForImportExport.htm&amp;XMLToc=DSDocDS.xml&amp;contextscope=onpremise</a></p></td></tr></tbody></table><p class="auto-cursor-target"><br /></p>
````

<!--NOMAGIC_PAGE id=258048960 space=CFE version=1 -->
## PAGE 00004: (2026x) CATIA FLXML Exporter

- page_id: `258048960`
- space_key: `CFE`
- source_url: https://docs.nomagic.com/spaces/CFE/pages/258048960/2026x+CATIA+FLXML+Exporter
- version_number: 1
- version_date: `2025-09-25T13:13:47.799+02:00`
- ancestors: Versions of CATIA FLXML Exporter
- labels: []

### NORMALIZED CONTENT

The CATIA FLXML Exporter plugin allows you to transform a UML/SysML v1/UAF model to functional and logical structures supported in the **3D**EXPERIENCEplatform. The plugin uses the FLXML Generation Engine and the element transformation schema to generate an FLXM file from the selected model elements. The conversion of CATIA Magic data to **3D**EXPERIENCEplatform data with lifecycle management is based on element mapping.

You can later [import the generated FLXML file to the **3D**EXPERIENCE platform](https://help.3ds.com/2024x/English/DSDoc/FleUserMap/fle-t-XMLImport.htm?ContextScope=onpremise) while ensuring the digital continuity and master interfaces of system architecture (with sub-systems developed in **3D**EXPERIENCEPlatform, CATIA Magic, or other tools). The CATIA FLXM Exporter plugin also helps to initiate the transition from the conceptual to the design layer.

#### NOTE: Prerequisites

Prerequisites

To be able to export the selected part of a model to an FLXML file, you need to [CONFLUENCE_PAGE title='Installing modeling tools and plugins' space='IL'] in your modeling tool.

[IMAGE alt='' src='']

###### The schema displaying how the CATIA FLXML Exporter plugin works.

[IMAGE alt='' src='']

###### Using the CATIA FLXML Exporter plugin ensures the digital continuity and master interfaces of the system architecture.

##### Exporting model data to FLXML

To export model data to an FLXML file, follow the steps described below.

To export model data to an FLXML file

1. In the main menu of a modeling tool, go to 3DEXPERIENCE > CATIA FLXML Exporter > Generate FLXML . The CATIA FLXML Exporter dialog opens. [ATTACHMENT filename='CATIA_FLXML_exporter_dialog.png']
2. In the open dialog, click [ATTACHMENT filename='select_scope.png'] next to the Scope elements box and select the scope of elements to be included in the generated FLXML file: [IMAGE alt='' src=''] By default, all elements owned by the selected scope element are included when generating an FLXML file.If the selected scope element is a diagram, the scope of the FLXML file generation will be the elements displayed in the diagram.If a certain element type is not included in the default element mapping schema, the elements of this type are excluded when generating an FLXML file.
  1. In the Tree view of the Select scope elements dialog, select the elements you want to export. (Press and hold the Ctrl key to select multiple elements.)
  2. Click [ATTACHMENT filename='add_scope.png'] to add the elements to the Selected elements list.
  3. Click OK to close the dialog.
3. In the List of available schemas box, select the default SysML to FL schema or a custom schema.
4. Click [ATTACHMENT filename='select_scope.png'] next to the Destination folder box and select the folder where the generated FLXML file should be stored.
5. In the CATIA FLXML Exporter dialog, click OK to start the export.
6. If you get the message saying that some validation errors were found, do one of the following:
  1. Click Yes to ignore the validation errors and generate an FLXML file anyway.
  2. Click No to correct the errors in the open validation results panel. Then try exporting your model to an FLXML file again.

After completing the above steps, an FLXML file is generated and saved in the destination folder. In addition, the **CATIA FLXM Results** window opens, where you can view and filter the export results or fix the validation errors.

##### Exporting FLXML results

Once you , the **CATIA FLXML Results** panel opens, displaying the export results. The results include both transformed and not transformed elements and file generation errors. You can export FLXML results to an MS Excel file as described below.

To export FLXML results to an MS Excel file

1. In the CATIA FLXML Results panel, click [ATTACHMENT filename='export_MSExcel.png'] . [ATTACHMENT filename='exporting_FLXML_results.png']
2. In the Select Destination Directory dialog, select the folder where you want to save the file with FLXML results and click Save .

The MS Excel file with FLXML results is automatically opened and saved in the specified directory.

**Additional resources**

- [ATTACHMENT filename='CATIA FLXML Exporter Plugin.mp4']
- [ATTACHMENT filename='CATIA FLXML Exporter Plugin - Effectivity.mp4']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p>The CATIA FLXML Exporter plugin allows you to transform a UML/SysML v1/UAF model to functional and logical structures supported in the <span style="color:var(--ds-text-accent-purple-bolder,#352c63);"><strong>3D</strong>EXPERIENCE </span>platform. The plugin uses the FLXML Generation Engine and the element transformation schema to generate an FLXM file from the selected model elements. The conversion of CATIA Magic data to <span style="color:var(--ds-text-accent-purple-bolder,#352c63);"><strong>3D</strong>EXPERIENCE </span>platform data with lifecycle management is based on element mapping.</p><p>You can later <a href="https://help.3ds.com/2024x/English/DSDoc/FleUserMap/fle-t-XMLImport.htm?ContextScope=onpremise">import the generated FLXML file to the <strong>3D</strong>EXPERIENCE platform</a> while ensuring the digital continuity and master interfaces of system architecture (with sub-systems developed in <span style="color:var(--ds-text-accent-purple-bolder,#352c63);"><strong>3D</strong>EXPERIENCE </span>Platform, CATIA Magic, or other tools). The CATIA FLXM Exporter plugin also helps to initiate the transition from the conceptual to the design layer.</p><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="e9e33596-f72b-4bba-95d4-5b8d1a8a2ba0"><ac:rich-text-body>For detailed information about the CATIA FLXML Exporter plugin, see <ac:link><ri:attachment ri:filename="CATIA FLXML Exporter Plugin User Guide.pdf"><ri:page ri:content-title="(2026x) CATIA FLXML Exporter" /></ri:attachment></ac:link></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="08ec6ff2-aa94-4b92-935a-679517a15172"><ac:parameter ac:name="title">Prerequisites</ac:parameter><ac:rich-text-body><p>To be able to export the selected part of a model to an FLXML file, you need to <ac:link><ri:page ri:space-key="IL" ri:content-title="Installing modeling tools and plugins" /><ac:plain-text-link-body><![CDATA[install the CATIA FLXML Exporter Plugin]]></ac:plain-text-link-body></ac:link> in your modeling tool.</p></ac:rich-text-body></ac:structured-macro><p><br /></p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="flxml_exporter_plugin.png"><ri:page ri:content-title="(2026x) CATIA FLXML Exporter" /></ri:attachment></ac:image></p><h6 style="text-align: center;">The schema displaying how the CATIA FLXML Exporter plugin works.</h6><p><ac:image ac:align="center"><ri:attachment ri:filename="importing_flxml_file.png"><ri:page ri:content-title="(2026x) CATIA FLXML Exporter" /></ri:attachment></ac:image></p><h6 style="text-align: center;">Using the CATIA FLXML Exporter plugin ensures the digital continuity and master interfaces of the system architecture.</h6><h3><br />Exporting model data to FLXML</h3><p>To export model data to an FLXML file, follow the steps described below.</p><p><br /></p><p>To export model data to an FLXML file</p><hr /><ol><li data-uuid="a48a8e44-44cf-4b6a-8b56-bcfefab966d6">In the main menu of a modeling tool, go to <strong>3DEXPERIENCE</strong> &gt; <strong>CATIA FLXML Exporter</strong> &gt; <strong>Generate FLXML</strong>. The <strong>CATIA FLXML Exporter</strong> dialog opens.<br /><br /><ac:image><ri:attachment ri:filename="CATIA_FLXML_exporter_dialog.png"><ri:page ri:content-title="(2026x) CATIA FLXML Exporter" /></ri:attachment></ac:image><br /><br /></li><li data-uuid="319e7254-c634-4d78-8593-8625051fabe3">In the open dialog, click <ac:image ac:thumbnail="true" ac:height="23"><ri:attachment ri:filename="select_scope.png"><ri:page ri:content-title="(2026x) CATIA FLXML Exporter" /></ri:attachment></ac:image> next to the <strong>Scope elements</strong> box and select the scope of elements to be included in the generated FLXML file:<ol><li>In the <strong>Tree</strong> view of the <strong>Select scope elements</strong> dialog, select the elements you want to export. (Press and hold the <strong>Ctrl</strong> key to select multiple elements.)</li><li>Click <ac:image><ri:attachment ri:filename="add_scope.png"><ri:page ri:content-title="(2026x) CATIA FLXML Exporter" /></ri:attachment></ac:image> to add the elements to the <strong>Selected elements</strong> list.</li><li>Click <strong>OK</strong> to close the dialog.<br /><br /></li></ol><p class="auto-cursor-target"><ac:image><ri:attachment ri:filename="selecting_scope.png"><ri:page ri:content-title="(2026x) CATIA FLXML Exporter" /></ri:attachment></ac:image><br /><br /></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="a758e3dc-f4aa-44a5-95e9-0ad14e942469"><ac:rich-text-body><ul><li><p>By default, all elements owned by the selected scope element are included when generating an FLXML file.</p></li><li><p><span>If the selected scope element is a diagram, the scope of the FLXML file generation will be the elements displayed in the diagram.</span></p></li><li><p>If a certain element type is not included in the default element mapping schema, the elements of this type are excluded when generating an FLXML file.<span><br /></span></p></li></ul></ac:rich-text-body></ac:structured-macro></li><li data-uuid="0e0ce91a-a94e-4676-8336-98cd872fa28f">In the <strong>List of available schemas</strong> box, select the default <strong>SysML to FL</strong> schema or a custom schema.</li><li data-uuid="85d307ff-bcc1-4194-bb70-618241efb89b">Click <ac:image ac:thumbnail="true" ac:height="23"><ri:attachment ri:filename="select_scope.png"><ri:page ri:content-title="(2026x) CATIA FLXML Exporter" /></ri:attachment></ac:image> next to the <strong>Destination folder</strong> box and select the folder where the generated FLXML file should be stored.</li><li data-uuid="f893effd-673d-42d0-b8bb-4d1dcd14bcb8">In the <strong>CATIA FLXML Exporter</strong> dialog, click <strong>OK</strong> to start the export.</li><li data-uuid="a187afdf-1e50-4536-9c99-cd943067a422">If you get the message saying that some validation errors were found, do one of the following:<ol><li>Click <strong>Yes</strong> to ignore the validation errors and generate an FLXML file anyway.</li><li>Click <strong>No</strong> to correct the errors in the open validation results panel. Then try exporting your model to an FLXML file again.</li></ol></li></ol><p><br />After completing the above steps, an FLXML file is generated and saved in the destination folder. In addition, the <strong>CATIA FLXM Results</strong> window opens, where you can view and filter the export results or fix the validation errors.</p><h3><br />Exporting FLXML results</h3><p>Once you <ac:link ac:anchor="Exporting model data to FLXML"><ac:plain-text-link-body><![CDATA[export model data to an FLXML file]]></ac:plain-text-link-body></ac:link>, the <strong>CATIA FLXML Results</strong> panel opens, displaying the export results. The results include both transformed and not transformed elements and file generation errors. You can export FLXML results to an MS Excel file as described below.</p><p><br /></p><p>To export FLXML results to an MS Excel file</p><hr /><ol><li data-uuid="3bcd02b7-28a5-43fc-af13-8e25358f931e">In the <strong>CATIA FLXML Results</strong> panel, click <ac:image><ri:attachment ri:filename="export_MSExcel.png"><ri:page ri:content-title="(2026x) CATIA FLXML Exporter" /></ri:attachment></ac:image>.<br /><br /><ac:image><ri:attachment ri:filename="exporting_FLXML_results.png"><ri:page ri:content-title="(2026x) CATIA FLXML Exporter" /></ri:attachment></ac:image><br /><br /></li><li data-uuid="adbfa74a-8329-4295-8bd3-75de146b53a7">In the <strong>Select Destination Directory</strong> dialog, select the folder where you want to save the file with FLXML results and click <strong>Save</strong>.</li></ol><p><br />The MS Excel file with FLXML results is automatically opened and saved in the specified directory.</p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><strong>Additional resources</strong></p><ul><li data-uuid="41edfe68-aa58-4da3-9389-1d239c1952cd"><ac:link><ri:attachment ri:filename="CATIA FLXML Exporter Plugin.mp4"><ri:page ri:content-title="(2026x) CATIA FLXML Exporter" /></ri:attachment></ac:link></li><li data-uuid="51410989-ec31-4ad4-bb41-b7c15b9df4ea"><ac:link><ri:attachment ri:filename="CATIA FLXML Exporter Plugin - Effectivity.mp4"><ri:page ri:content-title="(2026x) CATIA FLXML Exporter" /></ri:attachment></ac:link></li></ul></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=258048977 space=CFE version=1 -->
## PAGE 00005: (2026x) Exporting images of model diagrams

- page_id: `258048977`
- space_key: `CFE`
- source_url: https://docs.nomagic.com/spaces/CFE/pages/258048977/2026x+Exporting+images+of+model+diagrams
- version_number: 1
- version_date: `2025-09-25T13:13:48.110+02:00`
- ancestors: Versions of CATIA FLXML Exporter > (2026x) CATIA FLXML Exporter
- labels: ['msosa', 'mcse', 'msa']

### NORMALIZED CONTENT

The CATIA FLXML plugin allows you to export the images of elements if the CustomImageHolder has been set to an element transformed to an FL reference in the **3D**EXPERIENCEplatform. For example, the diagram displayed below can be exported as the following logical view.

[IMAGE alt='' src='']

###### An example of exporting the image of a model diagram.

To export images of model elements

1. In the main menu of a modeling tool, go to Options > Environment .
2. On the left side of the Environment Options dialog, select CATIA FLXML Exporter option group.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>The CATIA FLXML plugin allows you to export the images of elements if the CustomImageHolder has been set to an element transformed to an FL reference in the <span style="color: rgb(55,65,81);"><strong>3D</strong>EXPERIENCE </span>platform. For example, the diagram displayed below can be exported as the following logical view.</p><p><br /></p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="image_export_example.png"><ri:page ri:content-title="(2026x) Exporting images of model diagrams" /></ri:attachment></ac:image></p><h6 style="text-align: center;">An example of exporting the image of a model diagram.</h6><p>To export images of model elements</p><hr /><ol><li>In the main menu of a modeling tool, go to <strong>Options</strong> &gt; <strong>Environment</strong>.</li><li>On the left side of the <strong>Environment Options</strong> dialog, select <strong>CATIA FLXML Exporter</strong> option group.</li></ol><p><br /></p>
````

<!--NOMAGIC_PAGE id=258048973 space=CFE version=1 -->
## PAGE 00006: (2026x) Running the CATIA FLXML Exporter plugin in command line

- page_id: `258048973`
- space_key: `CFE`
- source_url: https://docs.nomagic.com/spaces/CFE/pages/258048973/2026x+Running+the+CATIA+FLXML+Exporter+plugin+in+command+line
- version_number: 1
- version_date: `2025-09-25T13:13:48.044+02:00`
- ancestors: Versions of CATIA FLXML Exporter > (2026x) CATIA FLXML Exporter
- labels: ['msosa', 'mcse', 'msa']

### NORMALIZED CONTENT

You can execute the CATIA FLXML Exporter plugin by using the command line interface both on the server and on the client machine.

#### NOTE: Important

Important

- Before starting, learn how to [CONFLUENCE_PAGE title='Running programs in batch mode' space='DEVG'] .
- When running the CATIA FLFML Exporter plugin in the command line, follow the recommended usage of the plugin described above. Any other usage of the plugin must be avoided
- Before starting, you must study the model and find out what data you want to export to an FLXML file.
- Each client can have a different configuration (e.g., Windows, Linux, etc.), so the execution of the plugin should be adapted to the client configuration.

To run the plugin and export model data to an FLXML file by using the command line

1. Download the [ATTACHMENT filename='generate_flxml.properties'] file.
2. In the generate_flxml.proprties file, specify .
3. Runthe CATIA FLXML Exporter plugin and export model data in one of the following ways:
  - Download and execute the *[ATTACHMENT filename='script_commandline.bat']* script. Executing the script_comandline.bat scriptBefore executing the script, make sure to replace the placeholders between <> with the actual values for the following properties:**%MAGICDRAW_HOME%** - specify the path to the modeling tool installation directory.**properties** - specify the path to the *generate_flxml.properties* file.
  - Implement the *com.nomagic.magicdraw.commandline.CommandLineAction*interface as described in [CONFLUENCE_PAGE title='Running programs in batch mode' space='DEVG'].

##### The CATIA FLXML Exporter plugin options

To export model data to an FLXML file by using the command line interface you have to specify the following properties in the *generate_flxml.properties* file.

| Property | Mandatory | Description |
| --- | --- | --- |
| project | Yes | Specify the path to the project you want to use to generate an FLXML file, e.g., e:\\data\\Aircraft Avionic.mdzip |
| schema | Yes | Specify the RFLP schema used to convert model elements to FL objects during export. You can use the default RFLP schema - SysML to FL or specify a custom schema. |
| destination_folder | Yes | Specify the path to the folder where the FLXML file should be saved. If the folder does not exist, it will be created during file generation. |
| scope_elements | Yes | Specify the list of elements to be exported to an FLXML file. Separate each element by a semicolon (;). Elements can be specified as:Element qualified name.Element ID. When specifying an element ID, use this format: id:<element_ID>Example:White box::Logical architecture::Logical architecture;id:_19_0_1_1a800cf_1559826887570_81532_41786;id:_19_0_1_1a800cf_1559826887379_499848_41443 |
| no_flxml_if_error | No | Set to true (the default value) for the command line execution to stop automatically if an error occurs while generating an FLXML file. In addition, the error text will be displayed in the console.Set to false to generate the FLXM file even if any generation errors occur. |
| log_results | No | Set to true if you want to generate a file with model data export results. The file includes export errors and both converted and not converted objects. It is saved in the same directory as the generated FLXML file. Otherwise, set to false (the default value). |
| log_format | No | The log_format property is only valid if the log_results property is set to true.Specify the file format for the model data export results (the log_results property). The possible values are:xls - an MS Excel file is generated.txt - a text file is generated.xlstxt - both MS Excel and text files are generated. |
| log_info | No | The log_info property is only valid if the log_results property is set to true.Set to true (the default value) if you do not want the annotations of converted and not converted objects to be included in the model data export results (the log_results property). Otherwise, set to false. |
| option_auto_ports | No | Set to true to automatically generate interfaces in the FLXML file if ports or pins do not exist in the UML/SysML v1 model. Otherwise, set to false (the default value). |
| option_escalated_links | No | Set to true to generate and manage the escalated link. Otherwise, set to false (the default option). |
| option_reference_out_of_scope_elements | No | Set to true (the default value) to automatically manage the references to elements located outside of the model data export scope (the scope_elements property). Otherwise, set to false. |
| option_dependecy_relationships | No | Set to true to automatically discover dependency relationships for each element (can be time-consuming). Otherwise, set to false (the default value). |
| option_create_top_refref_implement_links | No | Set to true to automatically create REF-REF implement links for an OCC-OCC link if the REF-REF implement links do not exist. Otherwise, set to false (the default value). |
| option_manage_effectivity | No | Set to true to generate effectivity files and a modified FLXML file to support effectivity. Otherwise, set to false (the default value). |
| option_export_image_for_diagrams | No | Set to true to generate images for symbol diagrams that you can later import to the 3DEXPERIENCE platform. Otherwise, set to false (the default value). |
| option_flxml_preview | No | Set to true (the default value) to generate an RFLXML file to be imported to the CATIA Systems Traceability in the 3DEXPERIENCE platform. Otherwise, set to false. |
| option_export_element_image | No | Set to true to generate images for FL references of the elements with the «CustomImageHolder» stereotype. Otherwise, set to false (the default value). |
| import_xml_file | No | Specify the path to the file that defines the XMLModel used by CATFLEditorImportBatch. This will allow you to modify XmlPath (and ImagePath if required).For more information about the file, see https://dsdoc.dsone.3ds.com/3DEXPERIENCER2021x/en/English/DSDocDSExa.htm?show=SadUserMap/fle-r-BatchForImportExport.htm&XMLToc=DSDocDS.xml&contextscope=onpremise |

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>You can execute the CATIA FLXML Exporter plugin by using the command line interface both on the server and on the client machine.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="a6d812ea-c2c8-43cd-94f9-feb625fa06c6"><ac:parameter ac:name="title">Important</ac:parameter><ac:rich-text-body><ul><li>Before starting, learn how to <ac:link><ri:page ri:space-key="DEVG" ri:content-title="Running programs in batch mode" /><ac:plain-text-link-body><![CDATA[run modeling tools and plugins by using the command line]]></ac:plain-text-link-body></ac:link>.</li><li>When running the CATIA FLFML Exporter plugin in the command line, follow the recommended usage of the plugin described above. Any other usage of the plugin must be avoided</li><li>Before starting, you must study the model and find out what data you want to export to an FLXML file.</li><li><p>Each client can have a different configuration (e.g., Windows, Linux, etc.), so the execution of the plugin should be adapted to the client configuration.</p></li></ul></ac:rich-text-body></ac:structured-macro><p><br /></p><p>To run the plugin and export model data to an FLXML file by using the command line</p><hr /><ol><li>Download the <em><ac:link><ri:attachment ri:filename="generate_flxml.properties" /></ac:link></em><em> </em>file.</li><li>In the <em>generate_flxml.proprties</em> file, specify <ac:link ac:anchor="The CATIA FLXML Exporter plugin options"><ac:plain-text-link-body><![CDATA[project and export-related properties]]></ac:plain-text-link-body></ac:link>.</li><li><p><span style="color:var(--ds-text,#333333);">Run </span><span style="color:var(--ds-text,#333333);">the CATIA FLXML Exporter plugin and export model data in one of the following ways:</span></p><ul><li><p><span style="color:var(--ds-text,#333333);">Download and execute the <em><ac:link><ri:attachment ri:filename="script_commandline.bat" /></ac:link></em> script.</span></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="f57c53e3-0491-465b-8e60-72f3527f2161"><ac:parameter ac:name="title">Executing the script_comandline.bat script</ac:parameter><ac:rich-text-body><p>Before executing the script, make sure to replace the placeholders between &lt;&gt; with the actual values for the following properties:</p><ul><li><strong>%MAGICDRAW_HOME%</strong> - specify the path to the modeling tool installation directory.</li><li><strong>properties</strong> - specify the path to the <em>generate_flxml.properties</em> file.</li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></li><li><p><span style="color:var(--ds-text,#333333);">Implement the <em style="text-align: left;">com.nomagic.magicdraw.commandline.CommandLineAction</em><span> </span>interface as described in <ac:link><ri:page ri:space-key="DEVG" ri:content-title="Running programs in batch mode" /></ac:link>.</span></p></li></ul></li></ol><h3><span style="color:var(--ds-text,#333333);"><br />The CATIA FLXML Exporter plugin options</span></h3><p>To export model data to an FLXML file by using the command line interface you have to specify the following properties in the <em>generate_flxml.properties</em> file.</p><table class="relative-table wrapped" style="width: 63.6314%;"><colgroup><col style="width: 22.2606%;" /><col style="width: 13.201%;" /><col style="width: 64.5384%;" /></colgroup><tbody><tr><th>Property</th><th colspan="1">Mandatory</th><th>Description</th></tr><tr><td><strong>project</strong></td><td colspan="1">Yes</td><td>Specify the path to the project you want to use to generate an FLXML file, e.g., e:\\data\\Aircraft Avionic.mdzip</td></tr><tr><td><strong>schema</strong></td><td colspan="1">Yes</td><td>Specify the RFLP schema used to convert model elements to FL objects during export. You can use the default RFLP schema - SysML to FL or specify a custom schema.</td></tr><tr><td><strong>destination_folder</strong></td><td colspan="1">Yes</td><td>Specify the path to the folder where the FLXML file should be saved. If the folder does not exist, it will be created during file generation.</td></tr><tr><td><strong>scope_elements</strong></td><td colspan="1">Yes</td><td><p>Specify the list of elements to be exported to an FLXML file. Separate each element by a semicolon (;). Elements can be specified as:</p><ul><li>Element qualified name.</li><li>Element ID. When specifying an element ID, use this format: <em>id:&lt;element_ID&gt;</em></li></ul><p>Example:</p><p>White box::Logical architecture::Logical architecture;id:_19_0_1_1a800cf_1559826887570_81532_41786;id:_19_0_1_1a800cf_1559826887379_499848_41443</p></td></tr><tr><td><strong>no_flxml_if_error</strong></td><td colspan="1">No</td><td><p>Set to <em>true</em> (the default value) for the command line execution to stop automatically if an error occurs while generating an FLXML file. In addition, the error text will be displayed in the console.</p><p>Set to <em>false</em> to generate the FLXM file even if any generation errors occur.</p></td></tr><tr><td><strong>log_results</strong></td><td colspan="1">No</td><td><p>Set to <em>true</em> if you want to generate a file with model data export results. The file includes export errors and both converted and not converted objects. It is saved in the same directory as the generated FLXML file. Otherwise, set to <em>false</em> (the default value).</p></td></tr><tr><td><strong>log_format</strong></td><td colspan="1">No</td><td><div class="content-wrapper"><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="988e56d2-ce59-4ff0-88ab-dbb238cb8cf6"><ac:rich-text-body><p>The <strong>log_format</strong> property is only valid if the <strong>log_results</strong> property is set to true.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target">Specify the file format for the model data export results (the <strong>log_results</strong> property). The possible values are:</p><ul><li class="auto-cursor-target"><strong>xls</strong> - an MS Excel file is generated.</li><li class="auto-cursor-target"><strong>txt</strong> - a text file is generated.</li><li class="auto-cursor-target"><strong>xlstxt</strong> - both MS Excel and text files are generated.</li></ul></div></td></tr><tr><td><strong>log_info</strong></td><td colspan="1">No</td><td><div class="content-wrapper"><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="0a8b309a-34fa-427c-b011-edfdd6871454"><ac:rich-text-body><p>The <strong>log_info</strong> property is only valid if the <strong>log_results</strong> property is set to true.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target">Set to <em>true</em> (the default value) if you do not want the annotations of converted and not converted objects to be included in the model data export results (the <strong>log_results</strong> property). Otherwise, set to <em>false</em>.</p></div></td></tr><tr><td colspan="1"><strong>option_auto_ports</strong></td><td colspan="1">No</td><td colspan="1">Set to <em>true</em> to automatically generate interfaces in the FLXML file if ports or pins do not exist in the UML/SysML v1 model. Otherwise, set to <em>false</em> (the default value).</td></tr><tr><td colspan="1"><strong>option_escalated_links</strong></td><td colspan="1">No</td><td colspan="1">Set to <em>true</em> to generate and manage the escalated link. Otherwise, set to <em>false</em> (the default option).</td></tr><tr><td colspan="1"><strong>option_reference_out_of_scope_elements</strong></td><td colspan="1">No</td><td colspan="1">Set to <em>true</em> (the default value) to automatically manage the references to elements located outside of the model data export scope (the <strong>scope_elements</strong> property). Otherwise, set to <em>false</em>.</td></tr><tr><td colspan="1"><strong>option_dependecy_relationships</strong></td><td colspan="1">No</td><td colspan="1">Set to <em>true</em> to automatically discover dependency relationships for each element (can be time-consuming). Otherwise, set to <em>false</em> (the default value).</td></tr><tr><td colspan="1"><strong>option_create_top_refref_implement_links</strong></td><td colspan="1">No</td><td colspan="1">Set to <em>true</em> to automatically create REF-REF implement links for an OCC-OCC link if the REF-REF implement links do not exist. Otherwise, set to <em>false</em> (the default value).</td></tr><tr><td colspan="1"><p><strong>option_manage_effectivity</strong></p></td><td colspan="1">No</td><td colspan="1">Set to <em>true</em> to generate effectivity files and a modified FLXML file to support effectivity. Otherwise, set to <em>false</em> (the default value).</td></tr><tr><td colspan="1"><strong>option_export_image_for_diagrams</strong></td><td colspan="1">No</td><td colspan="1">Set to <em>true</em> to generate images for symbol diagrams that you can later import to the <span style="color:var(--ds-text-accent-purple-bolder,#352c63);"><strong>3D</strong>EXPERIENCE </span>platform. Otherwise, set to <em>false</em> (the default value).</td></tr><tr><td colspan="1"><p><strong>option_flxml_preview</strong></p></td><td colspan="1">No</td><td colspan="1">Set to <em>true</em> (the default value) to generate an RFLXML file to be imported to the CATIA Systems Traceability in the <span style="color:var(--ds-text-accent-purple-bolder,#352c63);"><strong>3D</strong>EXPERIENCE </span>platform. Otherwise, set to <em>false</em>.</td></tr><tr><td colspan="1"><strong>option_export_element_image</strong></td><td colspan="1">No</td><td colspan="1">Set to <em>true</em> to generate images for FL references of the elements with the «CustomImageHolder» stereotype. Otherwise, set to <em>false</em> (the default value).</td></tr><tr><td colspan="1"><strong>import_xml_file</strong></td><td colspan="1">No</td><td colspan="1"><p>Specify the path to the file that defines the XMLModel used by <em>CATFLEditorImportBatch</em>. This will allow you to modify XmlPath (and ImagePath if required).</p><p>For more information about the file, see <a href="https://dsdoc.dsone.3ds.com/3DEXPERIENCER2021x/en/English/DSDocDSExa.htm?show=SadUserMap/fle-r-BatchForImportExport.htm&amp;XMLToc=DSDocDS.xml&amp;contextscope=onpremise">https://dsdoc.dsone.3ds.com/3DEXPERIENCER2021x/en/English/DSDocDSExa.htm?show=SadUserMap/fle-r-BatchForImportExport.htm&amp;XMLToc=DSDocDS.xml&amp;contextscope=onpremise</a></p></td></tr></tbody></table><p class="auto-cursor-target"><br /></p>
````

<!--NOMAGIC_PAGE id=258048908 space=CFE version=3 -->
## PAGE 00007: CATIA FLXML Exporter

- page_id: `258048908`
- space_key: `CFE`
- source_url: https://docs.nomagic.com/spaces/CFE/pages/258048908/CATIA+FLXML+Exporter
- version_number: 3
- version_date: `2025-09-25T13:10:34.413+02:00`
- ancestors: 
- labels: []

### NORMALIZED CONTENT

The CATIA FLXML Exporter plugin allows you to transform a UML/SysML v1/UAF model to functional and logical structures supported in the **3D**EXPERIENCEplatform. The plugin uses the FLXML Generation Engine and the element transformation schema to generate an FLXM file from the selected model elements. The conversion of CATIA Magic data to **3D**EXPERIENCEplatform data with lifecycle management is based on element mapping.

You can later [import the generated FLXML file to the **3D**EXPERIENCE platform](https://help.3ds.com/2024x/English/DSDoc/FleUserMap/fle-t-XMLImport.htm?ContextScope=onpremise) while ensuring the digital continuity and master interfaces of system architecture (with sub-systems developed in **3D**EXPERIENCEPlatform, CATIA Magic, or other tools). The CATIA FLXM Exporter plugin also helps to initiate the transition from the conceptual to the design layer.

#### NOTE: Prerequisites

Prerequisites

To be able to export the selected part of a model to an FLXML file, you need to [CONFLUENCE_PAGE title='Installing modeling tools and plugins' space='IL'] in your modeling tool.

[IMAGE alt='' src='']

###### The schema displaying how the CATIA FLXML Exporter plugin works.

[IMAGE alt='' src='']

###### Using the CATIA FLXML Exporter plugin ensures the digital continuity and master interfaces of the system architecture.

##### Exporting model data to FLXML

To export model data to an FLXML file, follow the steps described below.

To export model data to an FLXML file

1. In the main menu of a modeling tool, go to 3DEXPERIENCE > CATIA FLXML Exporter > Generate FLXML . The CATIA FLXML Exporter dialog opens. [ATTACHMENT filename='CATIA_FLXML_exporter_dialog.png']
2. In the open dialog, click [ATTACHMENT filename='select_scope.png'] next to the Scope elements box and select the scope of elements to be included in the generated FLXML file: [IMAGE alt='' src=''] By default, all elements owned by the selected scope element are included when generating an FLXML file.If the selected scope element is a diagram, the scope of the FLXML file generation will be the elements displayed in the diagram.If a certain element type is not included in the default element mapping schema, the elements of this type are excluded when generating an FLXML file.
  1. In the Tree view of the Select scope elements dialog, select the elements you want to export. (Press and hold the Ctrl key to select multiple elements.)
  2. Click [ATTACHMENT filename='add_scope.png'] to add the elements to the Selected elements list.
  3. Click OK to close the dialog.
3. In the List of available schemas box, select the default SysML to FL schema or a custom schema.
4. Click [ATTACHMENT filename='select_scope.png'] next to the Destination folder box and select the folder where the generated FLXML file should be stored.
5. In the CATIA FLXML Exporter dialog, click OK to start the export.
6. If you get the message saying that some validation errors were found, do one of the following:
  1. Click Yes to ignore the validation errors and generate an FLXML file anyway.
  2. Click No to correct the errors in the open validation results panel. Then try exporting your model to an FLXML file again.

After completing the above steps, an FLXML file is generated and saved in the destination folder. In addition, the **CATIA FLXM Results** window opens, where you can view and filter the export results or fix the validation errors.

##### Exporting FLXML results

Once you , the **CATIA FLXML Results** panel opens, displaying the export results. The results include both transformed and not transformed elements and file generation errors. You can export FLXML results to an MS Excel file as described below.

To export FLXML results to an MS Excel file

1. In the CATIA FLXML Results panel, click [ATTACHMENT filename='export_MSExcel.png'] . [ATTACHMENT filename='exporting_FLXML_results.png']
2. In the Select Destination Directory dialog, select the folder where you want to save the file with FLXML results and click Save .

The MS Excel file with FLXML results is automatically opened and saved in the specified directory.

**Additional resources**

- [ATTACHMENT filename='CATIA FLXML Exporter Plugin.mp4']
- [ATTACHMENT filename='CATIA FLXML Exporter Plugin - Effectivity.mp4']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p>The CATIA FLXML Exporter plugin allows you to transform a UML/SysML v1/UAF model to functional and logical structures supported in the <span style="color:var(--ds-text-accent-purple-bolder,#352c63);"><strong>3D</strong>EXPERIENCE </span>platform. The plugin uses the FLXML Generation Engine and the element transformation schema to generate an FLXM file from the selected model elements. The conversion of CATIA Magic data to <span style="color:var(--ds-text-accent-purple-bolder,#352c63);"><strong>3D</strong>EXPERIENCE </span>platform data with lifecycle management is based on element mapping.</p><p>You can later <a href="https://help.3ds.com/2024x/English/DSDoc/FleUserMap/fle-t-XMLImport.htm?ContextScope=onpremise">import the generated FLXML file to the <strong>3D</strong>EXPERIENCE platform</a> while ensuring the digital continuity and master interfaces of system architecture (with sub-systems developed in <span style="color:var(--ds-text-accent-purple-bolder,#352c63);"><strong>3D</strong>EXPERIENCE </span>Platform, CATIA Magic, or other tools). The CATIA FLXM Exporter plugin also helps to initiate the transition from the conceptual to the design layer.</p><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="e9e33596-f72b-4bba-95d4-5b8d1a8a2ba0"><ac:rich-text-body>For detailed information about the CATIA FLXML Exporter plugin, see <ac:link><ri:attachment ri:filename="CATIA FLXML Exporter Plugin User Guide.pdf" /></ac:link></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="08ec6ff2-aa94-4b92-935a-679517a15172"><ac:parameter ac:name="title">Prerequisites</ac:parameter><ac:rich-text-body><p>To be able to export the selected part of a model to an FLXML file, you need to <ac:link><ri:page ri:space-key="IL" ri:content-title="Installing modeling tools and plugins" /><ac:plain-text-link-body><![CDATA[install the CATIA FLXML Exporter Plugin]]></ac:plain-text-link-body></ac:link> in your modeling tool.</p></ac:rich-text-body></ac:structured-macro><p><br /></p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="flxml_exporter_plugin.png" /></ac:image></p><h6 style="text-align: center;">The schema displaying how the CATIA FLXML Exporter plugin works.</h6><p><ac:image ac:align="center"><ri:attachment ri:filename="importing_flxml_file.png" /></ac:image></p><h6 style="text-align: center;">Using the CATIA FLXML Exporter plugin ensures the digital continuity and master interfaces of the system architecture.</h6><h3><br />Exporting model data to FLXML</h3><p>To export model data to an FLXML file, follow the steps described below.</p><p><br /></p><p>To export model data to an FLXML file</p><hr /><ol><li data-uuid="a48a8e44-44cf-4b6a-8b56-bcfefab966d6">In the main menu of a modeling tool, go to <strong>3DEXPERIENCE</strong> &gt; <strong>CATIA FLXML Exporter</strong> &gt; <strong>Generate FLXML</strong>. The <strong>CATIA FLXML Exporter</strong> dialog opens.<br /><br /><ac:image><ri:attachment ri:filename="CATIA_FLXML_exporter_dialog.png" /></ac:image><br /><br /></li><li data-uuid="319e7254-c634-4d78-8593-8625051fabe3">In the open dialog, click <ac:image ac:thumbnail="true" ac:height="23"><ri:attachment ri:filename="select_scope.png" /></ac:image> next to the <strong>Scope elements</strong> box and select the scope of elements to be included in the generated FLXML file:<ol><li>In the <strong>Tree</strong> view of the <strong>Select scope elements</strong> dialog, select the elements you want to export. (Press and hold the <strong>Ctrl</strong> key to select multiple elements.)</li><li>Click <ac:image><ri:attachment ri:filename="add_scope.png" /></ac:image> to add the elements to the <strong>Selected elements</strong> list.</li><li>Click <strong>OK</strong> to close the dialog.<br /><br /></li></ol><p class="auto-cursor-target"><ac:image><ri:attachment ri:filename="selecting_scope.png" /></ac:image><br /><br /></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="a758e3dc-f4aa-44a5-95e9-0ad14e942469"><ac:rich-text-body><ul><li><p>By default, all elements owned by the selected scope element are included when generating an FLXML file.</p></li><li><p><span>If the selected scope element is a diagram, the scope of the FLXML file generation will be the elements displayed in the diagram.</span></p></li><li><p>If a certain element type is not included in the default element mapping schema, the elements of this type are excluded when generating an FLXML file.<span><br /></span></p></li></ul></ac:rich-text-body></ac:structured-macro></li><li data-uuid="0e0ce91a-a94e-4676-8336-98cd872fa28f">In the <strong>List of available schemas</strong> box, select the default <strong>SysML to FL</strong> schema or a custom schema.</li><li data-uuid="85d307ff-bcc1-4194-bb70-618241efb89b">Click <ac:image ac:thumbnail="true" ac:height="23"><ri:attachment ri:filename="select_scope.png" /></ac:image> next to the <strong>Destination folder</strong> box and select the folder where the generated FLXML file should be stored.</li><li data-uuid="f893effd-673d-42d0-b8bb-4d1dcd14bcb8">In the <strong>CATIA FLXML Exporter</strong> dialog, click <strong>OK</strong> to start the export.</li><li data-uuid="a187afdf-1e50-4536-9c99-cd943067a422">If you get the message saying that some validation errors were found, do one of the following:<ol><li>Click <strong>Yes</strong> to ignore the validation errors and generate an FLXML file anyway.</li><li>Click <strong>No</strong> to correct the errors in the open validation results panel. Then try exporting your model to an FLXML file again.</li></ol></li></ol><p><br />After completing the above steps, an FLXML file is generated and saved in the destination folder. In addition, the <strong>CATIA FLXM Results</strong> window opens, where you can view and filter the export results or fix the validation errors.</p><h3><br />Exporting FLXML results</h3><p>Once you <ac:link ac:anchor="Exporting model data to FLXML"><ac:plain-text-link-body><![CDATA[export model data to an FLXML file]]></ac:plain-text-link-body></ac:link>, the <strong>CATIA FLXML Results</strong> panel opens, displaying the export results. The results include both transformed and not transformed elements and file generation errors. You can export FLXML results to an MS Excel file as described below.</p><p><br /></p><p>To export FLXML results to an MS Excel file</p><hr /><ol><li data-uuid="3bcd02b7-28a5-43fc-af13-8e25358f931e">In the <strong>CATIA FLXML Results</strong> panel, click <ac:image><ri:attachment ri:filename="export_MSExcel.png" /></ac:image>.<br /><br /><ac:image><ri:attachment ri:filename="exporting_FLXML_results.png" /></ac:image><br /><br /></li><li data-uuid="adbfa74a-8329-4295-8bd3-75de146b53a7">In the <strong>Select Destination Directory</strong> dialog, select the folder where you want to save the file with FLXML results and click <strong>Save</strong>.</li></ol><p><br />The MS Excel file with FLXML results is automatically opened and saved in the specified directory.</p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><strong>Additional resources</strong></p><ul><li data-uuid="41edfe68-aa58-4da3-9389-1d239c1952cd"><ac:link><ri:attachment ri:filename="CATIA FLXML Exporter Plugin.mp4" /></ac:link></li><li data-uuid="51410989-ec31-4ad4-bb41-b7c15b9df4ea"><ac:link><ri:attachment ri:filename="CATIA FLXML Exporter Plugin - Effectivity.mp4" /></ac:link></li></ul></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=258048936 space=CFE version=1 -->
## PAGE 00008: Exporting images of model diagrams

- page_id: `258048936`
- space_key: `CFE`
- source_url: https://docs.nomagic.com/spaces/CFE/pages/258048936/Exporting+images+of+model+diagrams
- version_number: 1
- version_date: `2025-09-25T13:09:31.736+02:00`
- ancestors: CATIA FLXML Exporter
- labels: ['msosa', 'mcse', 'msa']

### NORMALIZED CONTENT

The CATIA FLXML plugin allows you to export the images of elements if the CustomImageHolder has been set to an element transformed to an FL reference in the **3D**EXPERIENCEplatform. For example, the diagram displayed below can be exported as the following logical view.

[IMAGE alt='' src='']

###### An example of exporting the image of a model diagram.

To export images of model elements

1. In the main menu of a modeling tool, go to Options > Environment .
2. On the left side of the Environment Options dialog, select CATIA FLXML Exporter option group.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>The CATIA FLXML plugin allows you to export the images of elements if the CustomImageHolder has been set to an element transformed to an FL reference in the <span style="color: rgb(55,65,81);"><strong>3D</strong>EXPERIENCE </span>platform. For example, the diagram displayed below can be exported as the following logical view.</p><p><br /></p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="image_export_example.png" /></ac:image></p><h6 style="text-align: center;">An example of exporting the image of a model diagram.</h6><p>To export images of model elements</p><hr /><ol><li>In the main menu of a modeling tool, go to <strong>Options</strong> &gt; <strong>Environment</strong>.</li><li>On the left side of the <strong>Environment Options</strong> dialog, select <strong>CATIA FLXML Exporter</strong> option group.</li></ol><p><br /></p>
````

<!--NOMAGIC_PAGE id=258048939 space=CFE version=3 -->
## PAGE 00009: Running the CATIA FLXML Exporter plugin in command line

- page_id: `258048939`
- space_key: `CFE`
- source_url: https://docs.nomagic.com/spaces/CFE/pages/258048939/Running+the+CATIA+FLXML+Exporter+plugin+in+command+line
- version_number: 3
- version_date: `2025-09-25T13:13:18.877+02:00`
- ancestors: CATIA FLXML Exporter
- labels: ['msosa', 'mcse', 'msa']

### NORMALIZED CONTENT

You can execute the CATIA FLXML Exporter plugin by using the command line interface both on the server and on the client machine.

#### NOTE: Important

Important

- Before starting, learn how to [CONFLUENCE_PAGE title='Running programs in batch mode' space='DEVG'] .
- When running the CATIA FLFML Exporter plugin in the command line, follow the recommended usage of the plugin described above. Any other usage of the plugin must be avoided
- Before starting, you must study the model and find out what data you want to export to an FLXML file.
- Each client can have a different configuration (e.g., Windows, Linux, etc.), so the execution of the plugin should be adapted to the client configuration.

To run the plugin and export model data to an FLXML file by using the command line

1. Download the [ATTACHMENT filename='generate_flxml.properties'] file.
2. In the generate_flxml.proprties file, specify .
3. Runthe CATIA FLXML Exporter plugin and export model data in one of the following ways:
  - Download and execute the *[ATTACHMENT filename='script_commandline.bat']* script. Executing the script_comandline.bat scriptBefore executing the script, make sure to replace the placeholders between <> with the actual values for the following properties:**%MAGICDRAW_HOME%** - specify the path to the modeling tool installation directory.**properties** - specify the path to the *generate_flxml.properties* file.
  - Implement the *com.nomagic.magicdraw.commandline.CommandLineAction*interface as described in [CONFLUENCE_PAGE title='Running programs in batch mode' space='DEVG'].

##### The CATIA FLXML Exporter plugin options

To export model data to an FLXML file by using the command line interface you have to specify the following properties in the *generate_flxml.properties* file.

| Property | Mandatory | Description |
| --- | --- | --- |
| project | Yes | Specify the path to the project you want to use to generate an FLXML file, e.g., e:\\data\\Aircraft Avionic.mdzip |
| schema | Yes | Specify the RFLP schema used to convert model elements to FL objects during export. You can use the default RFLP schema - SysML to FL or specify a custom schema. |
| destination_folder | Yes | Specify the path to the folder where the FLXML file should be saved. If the folder does not exist, it will be created during file generation. |
| scope_elements | Yes | Specify the list of elements to be exported to an FLXML file. Separate each element by a semicolon (;). Elements can be specified as:Element qualified name.Element ID. When specifying an element ID, use this format: id:<element_ID>Example:White box::Logical architecture::Logical architecture;id:_19_0_1_1a800cf_1559826887570_81532_41786;id:_19_0_1_1a800cf_1559826887379_499848_41443 |
| no_flxml_if_error | No | Set to true (the default value) for the command line execution to stop automatically if an error occurs while generating an FLXML file. In addition, the error text will be displayed in the console.Set to false to generate the FLXM file even if any generation errors occur. |
| log_results | No | Set to true if you want to generate a file with model data export results. The file includes export errors and both converted and not converted objects. It is saved in the same directory as the generated FLXML file. Otherwise, set to false (the default value). |
| log_format | No | The log_format property is only valid if the log_results property is set to true.Specify the file format for the model data export results (the log_results property). The possible values are:xls - an MS Excel file is generated.txt - a text file is generated.xlstxt - both MS Excel and text files are generated. |
| log_info | No | The log_info property is only valid if the log_results property is set to true.Set to true (the default value) if you do not want the annotations of converted and not converted objects to be included in the model data export results (the log_results property). Otherwise, set to false. |
| option_auto_ports | No | Set to true to automatically generate interfaces in the FLXML file if ports or pins do not exist in the UML/SysML v1 model. Otherwise, set to false (the default value). |
| option_escalated_links | No | Set to true to generate and manage the escalated link. Otherwise, set to false (the default option). |
| option_reference_out_of_scope_elements | No | Set to true (the default value) to automatically manage the references to elements located outside of the model data export scope (the scope_elements property). Otherwise, set to false. |
| option_dependecy_relationships | No | Set to true to automatically discover dependency relationships for each element (can be time-consuming). Otherwise, set to false (the default value). |
| option_create_top_refref_implement_links | No | Set to true to automatically create REF-REF implement links for an OCC-OCC link if the REF-REF implement links do not exist. Otherwise, set to false (the default value). |
| option_manage_effectivity | No | Set to true to generate effectivity files and a modified FLXML file to support effectivity. Otherwise, set to false (the default value). |
| option_export_image_for_diagrams | No | Set to true to generate images for symbol diagrams that you can later import to the 3DEXPERIENCE platform. Otherwise, set to false (the default value). |
| option_flxml_preview | No | Set to true (the default value) to generate an RFLXML file to be imported to the CATIA Systems Traceability in the 3DEXPERIENCE platform. Otherwise, set to false. |
| option_export_element_image | No | Set to true to generate images for FL references of the elements with the «CustomImageHolder» stereotype. Otherwise, set to false (the default value). |
| import_xml_file | No | Specify the path to the file that defines the XMLModel used by CATFLEditorImportBatch. This will allow you to modify XmlPath (and ImagePath if required).For more information about the file, see https://dsdoc.dsone.3ds.com/3DEXPERIENCER2021x/en/English/DSDocDSExa.htm?show=SadUserMap/fle-r-BatchForImportExport.htm&XMLToc=DSDocDS.xml&contextscope=onpremise |

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>You can execute the CATIA FLXML Exporter plugin by using the command line interface both on the server and on the client machine.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="a6d812ea-c2c8-43cd-94f9-feb625fa06c6"><ac:parameter ac:name="title">Important</ac:parameter><ac:rich-text-body><ul><li>Before starting, learn how to <ac:link><ri:page ri:space-key="DEVG" ri:content-title="Running programs in batch mode" /><ac:plain-text-link-body><![CDATA[run modeling tools and plugins by using the command line]]></ac:plain-text-link-body></ac:link>.</li><li>When running the CATIA FLFML Exporter plugin in the command line, follow the recommended usage of the plugin described above. Any other usage of the plugin must be avoided</li><li>Before starting, you must study the model and find out what data you want to export to an FLXML file.</li><li><p>Each client can have a different configuration (e.g., Windows, Linux, etc.), so the execution of the plugin should be adapted to the client configuration.</p></li></ul></ac:rich-text-body></ac:structured-macro><p><br /></p><p>To run the plugin and export model data to an FLXML file by using the command line</p><hr /><ol><li>Download the <em><ac:link><ri:attachment ri:filename="generate_flxml.properties" /></ac:link></em><em> </em>file.</li><li>In the <em>generate_flxml.proprties</em> file, specify <ac:link ac:anchor="The CATIA FLXML Exporter plugin options"><ac:plain-text-link-body><![CDATA[project and export-related properties]]></ac:plain-text-link-body></ac:link>.</li><li><p><span style="color:var(--ds-text,#333333);">Run </span><span style="color:var(--ds-text,#333333);">the CATIA FLXML Exporter plugin and export model data in one of the following ways:</span></p><ul><li><p><span style="color:var(--ds-text,#333333);">Download and execute the <em><ac:link><ri:attachment ri:filename="script_commandline.bat" /></ac:link></em> script.</span></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="f57c53e3-0491-465b-8e60-72f3527f2161"><ac:parameter ac:name="title">Executing the script_comandline.bat script</ac:parameter><ac:rich-text-body><p>Before executing the script, make sure to replace the placeholders between &lt;&gt; with the actual values for the following properties:</p><ul><li><strong>%MAGICDRAW_HOME%</strong> - specify the path to the modeling tool installation directory.</li><li><strong>properties</strong> - specify the path to the <em>generate_flxml.properties</em> file.</li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></li><li><p><span style="color:var(--ds-text,#333333);">Implement the <em style="text-align: left;">com.nomagic.magicdraw.commandline.CommandLineAction</em><span> </span>interface as described in <ac:link><ri:page ri:space-key="DEVG" ri:content-title="Running programs in batch mode" /></ac:link>.</span></p></li></ul></li></ol><h3><span style="color:var(--ds-text,#333333);"><br />The CATIA FLXML Exporter plugin options</span></h3><p>To export model data to an FLXML file by using the command line interface you have to specify the following properties in the <em>generate_flxml.properties</em> file.</p><table class="relative-table wrapped" style="width: 63.6314%;"><colgroup><col style="width: 22.2606%;" /><col style="width: 13.201%;" /><col style="width: 64.5384%;" /></colgroup><tbody><tr><th>Property</th><th colspan="1">Mandatory</th><th>Description</th></tr><tr><td><strong>project</strong></td><td colspan="1">Yes</td><td>Specify the path to the project you want to use to generate an FLXML file, e.g., e:\\data\\Aircraft Avionic.mdzip</td></tr><tr><td><strong>schema</strong></td><td colspan="1">Yes</td><td>Specify the RFLP schema used to convert model elements to FL objects during export. You can use the default RFLP schema - SysML to FL or specify a custom schema.</td></tr><tr><td><strong>destination_folder</strong></td><td colspan="1">Yes</td><td>Specify the path to the folder where the FLXML file should be saved. If the folder does not exist, it will be created during file generation.</td></tr><tr><td><strong>scope_elements</strong></td><td colspan="1">Yes</td><td><p>Specify the list of elements to be exported to an FLXML file. Separate each element by a semicolon (;). Elements can be specified as:</p><ul><li>Element qualified name.</li><li>Element ID. When specifying an element ID, use this format: <em>id:&lt;element_ID&gt;</em></li></ul><p>Example:</p><p>White box::Logical architecture::Logical architecture;id:_19_0_1_1a800cf_1559826887570_81532_41786;id:_19_0_1_1a800cf_1559826887379_499848_41443</p></td></tr><tr><td><strong>no_flxml_if_error</strong></td><td colspan="1">No</td><td><p>Set to <em>true</em> (the default value) for the command line execution to stop automatically if an error occurs while generating an FLXML file. In addition, the error text will be displayed in the console.</p><p>Set to <em>false</em> to generate the FLXM file even if any generation errors occur.</p></td></tr><tr><td><strong>log_results</strong></td><td colspan="1">No</td><td><p>Set to <em>true</em> if you want to generate a file with model data export results. The file includes export errors and both converted and not converted objects. It is saved in the same directory as the generated FLXML file. Otherwise, set to <em>false</em> (the default value).</p></td></tr><tr><td><strong>log_format</strong></td><td colspan="1">No</td><td><div class="content-wrapper"><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="988e56d2-ce59-4ff0-88ab-dbb238cb8cf6"><ac:rich-text-body><p>The <strong>log_format</strong> property is only valid if the <strong>log_results</strong> property is set to true.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target">Specify the file format for the model data export results (the <strong>log_results</strong> property). The possible values are:</p><ul><li class="auto-cursor-target"><strong>xls</strong> - an MS Excel file is generated.</li><li class="auto-cursor-target"><strong>txt</strong> - a text file is generated.</li><li class="auto-cursor-target"><strong>xlstxt</strong> - both MS Excel and text files are generated.</li></ul></div></td></tr><tr><td><strong>log_info</strong></td><td colspan="1">No</td><td><div class="content-wrapper"><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="0a8b309a-34fa-427c-b011-edfdd6871454"><ac:rich-text-body><p>The <strong>log_info</strong> property is only valid if the <strong>log_results</strong> property is set to true.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target">Set to <em>true</em> (the default value) if you do not want the annotations of converted and not converted objects to be included in the model data export results (the <strong>log_results</strong> property). Otherwise, set to <em>false</em>.</p></div></td></tr><tr><td colspan="1"><strong>option_auto_ports</strong></td><td colspan="1">No</td><td colspan="1">Set to <em>true</em> to automatically generate interfaces in the FLXML file if ports or pins do not exist in the UML/SysML v1 model. Otherwise, set to <em>false</em> (the default value).</td></tr><tr><td colspan="1"><strong>option_escalated_links</strong></td><td colspan="1">No</td><td colspan="1">Set to <em>true</em> to generate and manage the escalated link. Otherwise, set to <em>false</em> (the default option).</td></tr><tr><td colspan="1"><strong>option_reference_out_of_scope_elements</strong></td><td colspan="1">No</td><td colspan="1">Set to <em>true</em> (the default value) to automatically manage the references to elements located outside of the model data export scope (the <strong>scope_elements</strong> property). Otherwise, set to <em>false</em>.</td></tr><tr><td colspan="1"><strong>option_dependecy_relationships</strong></td><td colspan="1">No</td><td colspan="1">Set to <em>true</em> to automatically discover dependency relationships for each element (can be time-consuming). Otherwise, set to <em>false</em> (the default value).</td></tr><tr><td colspan="1"><strong>option_create_top_refref_implement_links</strong></td><td colspan="1">No</td><td colspan="1">Set to <em>true</em> to automatically create REF-REF implement links for an OCC-OCC link if the REF-REF implement links do not exist. Otherwise, set to <em>false</em> (the default value).</td></tr><tr><td colspan="1"><p><strong>option_manage_effectivity</strong></p></td><td colspan="1">No</td><td colspan="1">Set to <em>true</em> to generate effectivity files and a modified FLXML file to support effectivity. Otherwise, set to <em>false</em> (the default value).</td></tr><tr><td colspan="1"><strong>option_export_image_for_diagrams</strong></td><td colspan="1">No</td><td colspan="1">Set to <em>true</em> to generate images for symbol diagrams that you can later import to the <span style="color:var(--ds-text-accent-purple-bolder,#352c63);"><strong>3D</strong>EXPERIENCE </span>platform. Otherwise, set to <em>false</em> (the default value).</td></tr><tr><td colspan="1"><p><strong>option_flxml_preview</strong></p></td><td colspan="1">No</td><td colspan="1">Set to <em>true</em> (the default value) to generate an RFLXML file to be imported to the CATIA Systems Traceability in the <span style="color:var(--ds-text-accent-purple-bolder,#352c63);"><strong>3D</strong>EXPERIENCE </span>platform. Otherwise, set to <em>false</em>.</td></tr><tr><td colspan="1"><strong>option_export_element_image</strong></td><td colspan="1">No</td><td colspan="1">Set to <em>true</em> to generate images for FL references of the elements with the «CustomImageHolder» stereotype. Otherwise, set to <em>false</em> (the default value).</td></tr><tr><td colspan="1"><strong>import_xml_file</strong></td><td colspan="1">No</td><td colspan="1"><p>Specify the path to the file that defines the XMLModel used by <em>CATFLEditorImportBatch</em>. This will allow you to modify XmlPath (and ImagePath if required).</p><p>For more information about the file, see <a href="https://dsdoc.dsone.3ds.com/3DEXPERIENCER2021x/en/English/DSDocDSExa.htm?show=SadUserMap/fle-r-BatchForImportExport.htm&amp;XMLToc=DSDocDS.xml&amp;contextscope=onpremise">https://dsdoc.dsone.3ds.com/3DEXPERIENCER2021x/en/English/DSDocDSExa.htm?show=SadUserMap/fle-r-BatchForImportExport.htm&amp;XMLToc=DSDocDS.xml&amp;contextscope=onpremise</a></p></td></tr></tbody></table><p class="auto-cursor-target"><br /></p>
````

<!--NOMAGIC_PAGE id=258048957 space=CFE version=1 -->
## PAGE 00010: Versions of CATIA FLXML Exporter

- page_id: `258048957`
- space_key: `CFE`
- source_url: https://docs.nomagic.com/spaces/CFE/pages/258048957/Versions+of+CATIA+FLXML+Exporter
- version_number: 1
- version_date: `2025-09-25T13:13:47.258+02:00`
- ancestors: 
- labels: []

### NORMALIZED CONTENT

cfd64d9b43f99e4ec661c2bfef0c7a7e

CATIA FLXML Exporter

documentVersions

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="scroll-document-location" ac:schema-version="1" ac:macro-id="6c75f091-d240-4d64-b719-90f0a5a45e3e"><ac:parameter ac:name="permaId">cfd64d9b43f99e4ec661c2bfef0c7a7e</ac:parameter><ac:parameter ac:name="documentTitle">CATIA FLXML Exporter</ac:parameter><ac:parameter ac:name="key">documentVersions</ac:parameter></ac:structured-macro>
````
