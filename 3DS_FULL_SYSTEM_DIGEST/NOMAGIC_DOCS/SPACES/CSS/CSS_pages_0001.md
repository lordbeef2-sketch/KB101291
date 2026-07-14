# NOMAGIC DOCUMENTATION SPACE: CATIA Systems Synthesis

<!--NOMAGIC_SPACE key=CSS chunk=1 -->

<!--NOMAGIC_PAGE id=304014818 space=CSS version=1 -->
## PAGE 00001: (2026x Refresh1) CATIA Systems Synthesis

- page_id: `304014818`
- space_key: `CSS`
- source_url: https://docs.nomagic.com/spaces/CSS/pages/304014818/2026x+Refresh1+CATIA+Systems+Synthesis
- version_number: 1
- version_date: `2026-04-29T16:56:34.587+02:00`
- ancestors: Versions of CATIA Systems Synthesis
- labels: []

### NORMALIZED CONTENT

An integrated MDZipX plugin helps you improve the display of diagrams on the **3D**EXPERIENCE platform by exporting them to an MDZipX file. You can use different export options for different types of projects as described below.

##### Exporting diagrams to an MDZipX file

You can export diagrams from a local project to an MDZipX file either with or without used project data.

#### NOTE: Prerequisite

Prerequisite

Publishing diagrams to an MDZipX file works only with local projects.

To export diagrams to an MDZipX file

1. Open a local project
2. In the main menu, select 3DEXPERIENCE > CATIA Systems Synthesis Analysis .
3. Select one of the following commands:
  - Export to MDZipX File - exports the .svg file for each diagram.
  - Export to MDZipX File Including Data from Used Projects - exports the .svg file for each diagram and the data from used projects. [ATTACHMENT filename='export_to_mdzipx_file.png']
4. In the open dialog, select the target directory for the exported file.
5. Click the Save button.

The exported MDZipX file is saved in the specified target directory.

##### Publishing MDZipX files to Teamwork Cloud

When working with Teamwork Cloud projects, you can publish all model diagrams to Teamwork Cloud as an MDZipX file. During publishing, each diagram from every project version is saved as an SVG file.

#### NOTE: Prerequisite

Prerequisite

Publishing MDZipX files to Teamwork Cloud works only with Teamwork Cloud projects.

To publish MDZipX to Teamwork Cloud

1. [CONFLUENCE_PAGE title='Opening Teamwork Cloud projects' space='CM'] .
2. In the main menu, click 3DEXPERIENCE > CATIA Systems Synthesis Analysis .
3. Select Publish MDZipX File to Teamwork Cloud . [ATTACHMENT filename='publish_mdzipx_to_teamwork_cloud.png']

##### Publishing diagrams as project assets to the **3D**EXPERIENCE platform

When working with projects stored on the **3D**EXPERIENCE platform, you can export model diagrams to the SVG format and store them as auxiliary resources inside the model. The SVG files are then retrieved from the model and displayed in the CATIA Systems Traceability Application.

#### NOTE: Prerequisites

Prerequisites

- Publishing diagrams as project assets works only with the projects stored on the 3D EXPERIENCE platform.
- Only the [CONFLUENCE_PAGE title='Complete diagrams' space='MT'] are exported to the SVG format and published as project assets.

To publish diagrams as project assets to the **3D**EXPERIENCE platform

1. [CONFLUENCE_PAGE title='Opening projects from 3DEXPERIENCE platform' space='CM']Open a project stored in the **3D**EXPERIENCE platform .
2. In the main menu, select 3DEXPERIENCE > CATIA Systems Synthesis Analysis > Publish Diagrams as Assets . A new Assets package with the SVG package inside it is created under the Model element. All diagrams marked as complete are exported to SVG and stored under the SVG package. [ATTACHMENT filename='assets_package.png']
3. [CONFLUENCE_PAGE title='Committing changes to 3DEXPERIENCE platform' space='CM']Commit changes to the **3D**EXPERIENCE platform .

##### Environment Options

You modify the behavior of the MDZipX plugin by changing the environment options under the CATIA Systems Synthesis Analysis group. For example, you can include diagrams from used projects to exported MDZipX files or choose to publish an MDZipX file to Teamwork Cloud automatically upon every project commit.

You can specify the diagram export options, such as dimensions and building time (the latter applies only to tables and matrices), in the **Project Options** dialog. See the [CONFLUENCE_PAGE title='Diagram image export' space='MT'] page to learn more.

To include diagrams from used projects to an MDZipX file or project assets

1. In the main menu, select Options > Environment .
2. In the left-side panel, select the Collaboration option group.
3. Set the Publish Diagrams from Used Projects option to true .
4. Click OK .

Publish an MDZipX file to Teamwork Cloud automatically upon project commit

1. In the main menu, select Options > Environment .
2. In the left-side panel, select the Collaboration option group.
3. Set the Publish MDZipX Upon Commit option to true .
4. Click OK .

MagicDraw and NoMagic Teamwork Cloud Connectors Configuration

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>An integrated MDZipX plugin helps you improve the display of diagrams on the <strong>3D</strong>EXPERIENCE platform by exporting them to an MDZipX file. You can use different export options for different types of projects as described below.</p><h3>Exporting diagrams to an MDZipX file</h3><p>You can export diagrams from a local project to an MDZipX file either with or without used project data.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="05af13e6-4be0-4497-a1f7-a521aad3e6d0"><ac:parameter ac:name="title">Prerequisite</ac:parameter><ac:rich-text-body><p>Publishing diagrams to an MDZipX file works only with local projects.</p></ac:rich-text-body></ac:structured-macro><p><br /></p><p>To export diagrams to an MDZipX file</p><hr /><ol><li data-uuid="2a9a2eac-f435-407f-b718-41f7d1afa428">Open a local project</li><li data-uuid="f42a42da-1697-4811-8b75-857b778f0ffc">In the main menu, select <strong>3DEXPERIENCE </strong>&gt; <strong>CATIA Systems Synthesis Analysis</strong>.</li><li data-uuid="b4d22813-f5bb-452c-8e20-9abb40685db7">Select one of the following commands:<ul><li><strong>Export to MDZipX File</strong> - exports the .svg file for each diagram.</li><li><strong>Export to MDZipX File Including Data from Used Projects</strong> - exports the .svg file for each diagram and the data from used projects.<br /><br /><ac:image ac:height="114"><ri:attachment ri:filename="export_to_mdzipx_file.png"><ri:page ri:content-title="(2026x Refresh1) CATIA Systems Synthesis" /></ri:attachment></ac:image><br /><br /></li></ul></li><li data-uuid="5297151b-960f-4b04-90ae-3c20b3344db2">In the open dialog, select the target directory for the exported file.</li><li data-uuid="89c21f45-a86d-4099-b404-75338bf4ed44">Click the <strong>Save</strong> button.</li></ol><p><br />The exported MDZipX file is saved in the specified target directory.</p><h3>Publishing MDZipX files to Teamwork Cloud</h3><p>When working with Teamwork Cloud projects, you can publish all model diagrams to Teamwork Cloud as an MDZipX file. During publishing, each diagram from every project version is saved as an SVG file.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="3d9c34ce-fd05-4082-8685-827f0e49ff5f"><ac:parameter ac:name="title">Prerequisite</ac:parameter><ac:rich-text-body><p>Publishing MDZipX files to Teamwork Cloud works only with Teamwork Cloud projects.</p></ac:rich-text-body></ac:structured-macro><p><br /></p><p>To publish MDZipX to Teamwork Cloud</p><hr /><ol><li data-uuid="7d4818d1-281f-44d7-b496-1a2c3e6df155"><ac:link><ri:page ri:space-key="CM" ri:content-title="Opening Teamwork Cloud projects" /><ac:plain-text-link-body><![CDATA[Open a Teamwork Cloud project]]></ac:plain-text-link-body></ac:link>.</li><li data-uuid="737babcb-be90-43b0-a110-dd7314076b05">In the main menu, click <strong>3DEXPERIENCE </strong>&gt; <strong>CATIA Systems Synthesis Analysis</strong>.</li><li data-uuid="9e96a321-b370-4967-b31a-e94c7ef530b9">Select <strong>Publish MDZipX File to Teamwork Cloud</strong>.<br /><br /><ac:image ac:height="114"><ri:attachment ri:filename="publish_mdzipx_to_teamwork_cloud.png"><ri:page ri:content-title="(2026x Refresh1) CATIA Systems Synthesis" /></ri:attachment></ac:image></li></ol><h3>Publishing diagrams as project assets to the <strong>3D</strong>EXPERIENCE platform</h3><p style="text-align: left;">When working with projects stored on the <strong>3D</strong>EXPERIENCE platform, you can export model diagrams to the SVG format and store them as auxiliary resources inside the model. The SVG files are then retrieved from the model and displayed in <span style="color:var(--ds-text,#172b4d);">the CATIA Systems Traceability Application.</span></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="7a6b8a47-a73e-4570-b634-fcc821f25410"><ac:parameter ac:name="title">Prerequisites</ac:parameter><ac:rich-text-body><ul><li data-uuid="dc1397b9-5bcf-41b1-8277-b0e0b34caf9a">Publishing diagrams as project assets works only with the projects stored on the <strong>3D</strong>EXPERIENCE platform.</li><li data-uuid="428da09a-ab60-4a5b-83f7-12a135caf653">Only the <ac:link><ri:page ri:space-key="MT" ri:content-title="Complete diagrams" /><ac:plain-text-link-body><![CDATA[diagrams marked as complete]]></ac:plain-text-link-body></ac:link> are exported to the SVG format and published as project assets.</li></ul></ac:rich-text-body></ac:structured-macro><p style="text-align: left;"><br /></p><p>To publish diagrams as project assets to the <strong>3D</strong>EXPERIENCE platform</p><hr /><ol><li data-uuid="6d4c0cbc-d8d0-403b-8704-4019706bca11"><ac:link><ri:page ri:space-key="CM" ri:content-title="Opening projects from 3DEXPERIENCE platform" /><ac:link-body>Open a project stored in the <strong>3D</strong>EXPERIENCE platform</ac:link-body></ac:link><span>.</span></li><li data-uuid="3e849e8a-0b84-4115-b8bd-f5eaf1d99c8d">In the main menu, select <strong>3DEXPERIENCE </strong>&gt; <strong>CATIA Systems Synthesis Analysis</strong> &gt; <strong>Publish Diagrams as Assets</strong>. A new <em>Assets</em> package with the <em>SVG</em> package inside it is created under the Model element. All diagrams marked as complete are exported to SVG and stored under the <em>SVG</em> package.<br /><br /><ac:image><ri:attachment ri:filename="assets_package.png"><ri:page ri:content-title="(2026x Refresh1) CATIA Systems Synthesis" /></ri:attachment></ac:image><br /><br /></li><li data-uuid="28607262-6d81-44ac-a4ba-fa0c9c8b0e47"><ac:link><ri:page ri:space-key="CM" ri:content-title="Committing changes to 3DEXPERIENCE platform" /><ac:link-body>Commit changes to the <strong>3D</strong>EXPERIENCE platform</ac:link-body></ac:link>.</li></ol><h3><span>Environment Options</span></h3><p>You modify the behavior of the MDZipX plugin by changing the environment options under the CATIA Systems Synthesis Analysis group. For example, you can include diagrams from used projects to exported MDZipX files or choose to publish an MDZipX file to Teamwork Cloud automatically upon every project commit. </p><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="0ae12f24-a4b3-4614-b014-2a939c187bc5"><ac:rich-text-body><p>You can specify the diagram export options, such as dimensions and building time (the latter applies only to tables and matrices), in the <strong>Project Options</strong> dialog. See the <ac:link><ri:page ri:space-key="MT" ri:content-title="Diagram image export" /></ac:link> page to learn more.</p></ac:rich-text-body></ac:structured-macro><p><br /></p><p>To include diagrams from used projects to an MDZipX file or project assets</p><hr /><ol><li data-uuid="63dfba22-e78c-4ba4-93ee-90de52cdf600">In the main menu, select <strong>Options</strong> &gt; <strong>Environment</strong>. </li><li data-uuid="3de2c995-9c2a-45d0-9959-6d96da701c74">In the left-side panel, select the <strong>Collaboration</strong> option group.</li><li data-uuid="43b2f24f-c142-48ca-8ccf-eca3ae0d4692">Set the <strong>Publish Diagrams from Used Projects</strong> option to <em>true</em>.</li><li data-uuid="ac1a1c76-3d62-4f41-81a2-5b130ced8474">Click <strong>OK</strong>.<br /><br /></li></ol><p>Publish an MDZipX file to Teamwork Cloud automatically upon project commit</p><hr /><ol><li data-uuid="120b36f5-e16d-49bc-adc4-2823fbd316d9">In the main menu, select <strong>Options</strong> &gt; <strong>Environment</strong>.</li><li data-uuid="f779d783-d6f7-4e24-b78a-50fe99cad30c">In the left-side panel, select the <strong>Collaboration</strong> option group.</li><li data-uuid="3292a8be-2865-4a67-8ee3-df451a63c34c">Set the <strong>Publish MDZipX Upon Commit</strong> option to <em>true</em>.</li><li data-uuid="63c1d0fc-6440-4fd2-a0e6-ccbeccfa89dc">Click <strong>OK</strong>.</li></ol><p><br /></p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="671a27e2-5851-4cc8-899c-f76020a4f529"><ac:rich-text-body>For more information, please refer to <a href="https://help.3ds.com/2024x/English/DSDoc/TraUserMap/smv-c-ad-NoMagicConfiguration.htm?contextscope=onpremise">MagicDraw and NoMagic Teamwork Cloud Connectors Configuration</a>.</ac:rich-text-body></ac:structured-macro><p><br /></p>
````

<!--NOMAGIC_PAGE id=258048896 space=CSS version=2 -->
## PAGE 00002: (2026x) CATIA Systems Synthesis

- page_id: `258048896`
- space_key: `CSS`
- source_url: https://docs.nomagic.com/spaces/CSS/pages/258048896/2026x+CATIA+Systems+Synthesis
- version_number: 2
- version_date: `2025-09-25T12:58:36.202+02:00`
- ancestors: Versions of CATIA Systems Synthesis
- labels: []

### NORMALIZED CONTENT

An integrated MDZipX plugin helps you improve the display of diagrams on the **3D**EXPERIENCE platform by exporting them to an MDZipX file. You can use different export options for different types of projects as described below.

##### Exporting diagrams to an MDZipX file

You can export diagrams from a local project to an MDZipX file either with or without used project data.

#### NOTE: Prerequisite

Prerequisite

Publishing diagrams to an MDZipX file works only with local projects.

To export diagrams to an MDZipX file

1. Open a local project
2. In the main menu, select 3DEXPERIENCE > CATIA Systems Synthesis Analysis .
3. Select one of the following commands:
  - Export to MDZipX File - exports the .svg file for each diagram.
  - Export to MDZipX File Including Data from Used Projects - exports the .svg file for each diagram and the data from used projects. [ATTACHMENT filename='export_to_mdzipx_file.png']
4. In the open dialog, select the target directory for the exported file.
5. Click the Save button.

The exported MDZipX file is saved in the specified target directory.

##### Publishing MDZipX files to Teamwork Cloud

When working with Teamwork Cloud projects, you can publish all model diagrams to Teamwork Cloud as an MDZipX file. During publishing, each diagram from every project version is saved as an SVG file.

#### NOTE: Prerequisite

Prerequisite

Publishing MDZipX files to Teamwork Cloud works only with Teamwork Cloud projects.

To publish MDZipX to Teamwork Cloud

1. [CONFLUENCE_PAGE title='Opening Teamwork Cloud projects' space='CM'] .
2. In the main menu, click 3DEXPERIENCE > CATIA Systems Synthesis Analysis .
3. Select Publish MDZipX File to Teamwork Cloud . [ATTACHMENT filename='publish_mdzipx_to_teamwork_cloud.png']

##### Publishing diagrams as project assets to the **3D**EXPERIENCE platform

When working with projects stored on the **3D**EXPERIENCE platform, you can export model diagrams to the SVG format and store them as auxiliary resources inside the model. The SVG files are then retrieved from the model and displayed in the CATIA Systems Traceability Application.

#### NOTE: Prerequisites

Prerequisites

- Publishing diagrams as project assets works only with the projects stored on the 3D EXPERIENCE platform.
- Only the [CONFLUENCE_PAGE title='(2026x) Complete diagrams' space='MT'] are exported to the SVG format and published as project assets.

To publish diagrams as project assets to the **3D**EXPERIENCE platform

1. [CONFLUENCE_PAGE title='Opening projects from 3DEXPERIENCE platform' space='CM']Open a project stored in the **3D**EXPERIENCE platform .
2. In the main menu, select 3DEXPERIENCE > CATIA Systems Synthesis Analysis > Publish Diagrams as Assets . A new Assets package with the SVG package inside it is created under the Model element. All diagrams marked as complete are exported to SVG and stored under the SVG package. [ATTACHMENT filename='assets_package.png']
3. [CONFLUENCE_PAGE title='Committing changes to 3DEXPERIENCE platform' space='CM']Commit changes to the **3D**EXPERIENCE platform .

##### Environment Options

You modify the behavior of the MDZipX plugin by changing the environment options under the CATIA Systems Synthesis Analysis group. For example, you can include diagrams from used projects to exported MDZipX files or choose to publish an MDZipX file to Teamwork Cloud automatically upon every project commit.

You can specify the diagram export options, such as dimensions and building time (the latter applies only to tables and matrices), in the **Project Options** dialog. See the [CONFLUENCE_PAGE title='(2026x) Diagram image export' space='MT'] page to learn more.

To include diagrams from used projects to an MDZipX file or project assets

1. In the main menu, select Options > Environment .
2. In the left-side panel, select the Collaboration option group.
3. Set the Publish Diagrams from Used Projects option to true .
4. Click OK .

Publish an MDZipX file to Teamwork Cloud automatically upon project commit

1. In the main menu, select Options > Environment .
2. In the left-side panel, select the Collaboration option group.
3. Set the Publish MDZipX Upon Commit option to true .
4. Click OK .

MagicDraw and NoMagic Teamwork Cloud Connectors Configuration

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>An integrated MDZipX plugin helps you improve the display of diagrams on the <strong>3D</strong>EXPERIENCE platform by exporting them to an MDZipX file. You can use different export options for different types of projects as described below.</p><h3>Exporting diagrams to an MDZipX file</h3><p>You can export diagrams from a local project to an MDZipX file either with or without used project data.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="05af13e6-4be0-4497-a1f7-a521aad3e6d0"><ac:parameter ac:name="title">Prerequisite</ac:parameter><ac:rich-text-body><p>Publishing diagrams to an MDZipX file works only with local projects.</p></ac:rich-text-body></ac:structured-macro><p><br /></p><p>To export diagrams to an MDZipX file</p><hr /><ol><li data-uuid="0ea5c36a-3416-4010-9726-c38f51ec35f5">Open a local project</li><li data-uuid="d8982d30-cfb6-4eb7-a1f2-63b4f8c8eff0">In the main menu, select <strong>3DEXPERIENCE </strong>&gt; <strong>CATIA Systems Synthesis Analysis</strong>.</li><li data-uuid="2f602803-da9d-4c89-bedb-192eceffb540">Select one of the following commands:<ul><li><strong>Export to MDZipX File</strong> - exports the .svg file for each diagram.</li><li><strong>Export to MDZipX File Including Data from Used Projects</strong> - exports the .svg file for each diagram and the data from used projects.<br /><br /><ac:image ac:height="114"><ri:attachment ri:filename="export_to_mdzipx_file.png" /></ac:image><br /><br /></li></ul></li><li data-uuid="d88cdfe5-6fab-4484-be85-f0a94bad9d57">In the open dialog, select the target directory for the exported file.</li><li data-uuid="36909f92-d7c8-49f9-87dc-403b0b58e83d">Click the <strong>Save</strong> button.</li></ol><p><br />The exported MDZipX file is saved in the specified target directory.</p><h3>Publishing MDZipX files to Teamwork Cloud</h3><p>When working with Teamwork Cloud projects, you can publish all model diagrams to Teamwork Cloud as an MDZipX file. During publishing, each diagram from every project version is saved as an SVG file.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="3d9c34ce-fd05-4082-8685-827f0e49ff5f"><ac:parameter ac:name="title">Prerequisite</ac:parameter><ac:rich-text-body><p>Publishing MDZipX files to Teamwork Cloud works only with Teamwork Cloud projects.</p></ac:rich-text-body></ac:structured-macro><p><br /></p><p>To publish MDZipX to Teamwork Cloud</p><hr /><ol><li data-uuid="51b892f4-c982-4753-91c5-832eb60ae6b1"><ac:link><ri:page ri:space-key="CM" ri:content-title="Opening Teamwork Cloud projects" /><ac:plain-text-link-body><![CDATA[Open a Teamwork Cloud project]]></ac:plain-text-link-body></ac:link>.</li><li data-uuid="d02c6200-5981-49dd-b9e4-fa6d03113c04">In the main menu, click <strong>3DEXPERIENCE </strong>&gt; <strong>CATIA Systems Synthesis Analysis</strong>.</li><li data-uuid="0b2e93e4-5203-444e-bd76-c00fa53f65b9">Select <strong>Publish MDZipX File to Teamwork Cloud</strong>.<br /><br /><ac:image ac:height="114"><ri:attachment ri:filename="publish_mdzipx_to_teamwork_cloud.png" /></ac:image></li></ol><h3>Publishing diagrams as project assets to the <strong>3D</strong>EXPERIENCE platform</h3><p style="text-align: left;">When working with projects stored on the <strong>3D</strong>EXPERIENCE platform, you can export model diagrams to the SVG format and store them as auxiliary resources inside the model. The SVG files are then retrieved from the model and displayed in <span style="color:var(--ds-text,#172b4d);">the CATIA Systems Traceability Application.</span></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="7a6b8a47-a73e-4570-b634-fcc821f25410"><ac:parameter ac:name="title">Prerequisites</ac:parameter><ac:rich-text-body><ul><li data-uuid="b1166c35-d9ea-45da-8725-ecb3c780ae28">Publishing diagrams as project assets works only with the projects stored on the <strong>3D</strong>EXPERIENCE platform.</li><li data-uuid="b0e6438d-977a-46a8-b921-aee7782dd1ff">Only the <ac:link><ri:page ri:space-key="MT" ri:content-title="(2026x) Complete diagrams" /><ac:plain-text-link-body><![CDATA[diagrams marked as complete]]></ac:plain-text-link-body></ac:link> are exported to the SVG format and published as project assets.</li></ul></ac:rich-text-body></ac:structured-macro><p style="text-align: left;"><br /></p><p>To publish diagrams as project assets to the <strong>3D</strong>EXPERIENCE platform</p><hr /><ol><li data-uuid="e180ca79-a5c4-4b3c-aa3b-bc62704d78be"><ac:link><ri:page ri:space-key="CM" ri:content-title="Opening projects from 3DEXPERIENCE platform" /><ac:link-body>Open a project stored in the <strong>3D</strong>EXPERIENCE platform</ac:link-body></ac:link><span>.</span></li><li data-uuid="25559ad8-c58e-4832-b46f-8f9a6e7df589">In the main menu, select <strong>3DEXPERIENCE </strong>&gt; <strong>CATIA Systems Synthesis Analysis</strong> &gt; <strong>Publish Diagrams as Assets</strong>. A new <em>Assets</em> package with the <em>SVG</em> package inside it is created under the Model element. All diagrams marked as complete are exported to SVG and stored under the <em>SVG</em> package.<br /><br /><ac:image><ri:attachment ri:filename="assets_package.png" /></ac:image><br /><br /></li><li data-uuid="7a1c9f56-ec08-427a-bfee-6e4510a86816"><ac:link><ri:page ri:space-key="CM" ri:content-title="Committing changes to 3DEXPERIENCE platform" /><ac:link-body>Commit changes to the <strong>3D</strong>EXPERIENCE platform</ac:link-body></ac:link>.</li></ol><h3><span>Environment Options</span></h3><p>You modify the behavior of the MDZipX plugin by changing the environment options under the CATIA Systems Synthesis Analysis group. For example, you can include diagrams from used projects to exported MDZipX files or choose to publish an MDZipX file to Teamwork Cloud automatically upon every project commit. </p><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="0ae12f24-a4b3-4614-b014-2a939c187bc5"><ac:rich-text-body><p>You can specify the diagram export options, such as dimensions and building time (the latter applies only to tables and matrices), in the <strong>Project Options</strong> dialog. See the <ac:link><ri:page ri:space-key="MT" ri:content-title="(2026x) Diagram image export" /></ac:link> page to learn more.</p></ac:rich-text-body></ac:structured-macro><p><br /></p><p>To include diagrams from used projects to an MDZipX file or project assets</p><hr /><ol><li data-uuid="2e4ee859-b2fb-4822-b932-e8c6f803ae84">In the main menu, select <strong>Options</strong> &gt; <strong>Environment</strong>. </li><li data-uuid="d5548964-65af-4e7f-8f9a-594eaf300a21">In the left-side panel, select the <strong>Collaboration</strong> option group.</li><li data-uuid="2e4c9b3f-5df1-4a4c-ab29-56c8a61f6c75">Set the <strong>Publish Diagrams from Used Projects</strong> option to <em>true</em>.</li><li data-uuid="788eafbc-ae1b-42ab-957d-3bfd12e42903">Click <strong>OK</strong>.<br /><br /></li></ol><p>Publish an MDZipX file to Teamwork Cloud automatically upon project commit</p><hr /><ol><li data-uuid="898d98c7-a2ec-420e-8bff-4ae32c857547">In the main menu, select <strong>Options</strong> &gt; <strong>Environment</strong>.</li><li data-uuid="4ac6766a-7d4c-46eb-991c-c4c1601c4c80">In the left-side panel, select the <strong>Collaboration</strong> option group.</li><li data-uuid="9a1b3ba2-6cbc-49ab-affe-2de2a7cb5087">Set the <strong>Publish MDZipX Upon Commit</strong> option to <em>true</em>.</li><li data-uuid="8d6a6b13-30f7-4def-9af3-1599d87a9efd">Click <strong>OK</strong>.</li></ol><p><br /></p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="671a27e2-5851-4cc8-899c-f76020a4f529"><ac:rich-text-body>For more information, please refer to <a href="https://help.3ds.com/2024x/English/DSDoc/TraUserMap/smv-c-ad-NoMagicConfiguration.htm?contextscope=onpremise">MagicDraw and NoMagic Teamwork Cloud Connectors Configuration</a>.</ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=258048882 space=CSS version=2 -->
## PAGE 00003: CATIA Systems Synthesis

- page_id: `258048882`
- space_key: `CSS`
- source_url: https://docs.nomagic.com/spaces/CSS/pages/258048882/CATIA+Systems+Synthesis
- version_number: 2
- version_date: `2025-09-25T12:56:43.370+02:00`
- ancestors: 
- labels: []

### NORMALIZED CONTENT

An integrated MDZipX plugin helps you improve the display of diagrams on the **3D**EXPERIENCE platform by exporting them to an MDZipX file. You can use different export options for different types of projects as described below.

##### Exporting diagrams to an MDZipX file

You can export diagrams from a local project to an MDZipX file either with or without used project data.

#### NOTE: Prerequisite

Prerequisite

Publishing diagrams to an MDZipX file works only with local projects.

To export diagrams to an MDZipX file

1. Open a local project
2. In the main menu, select 3DEXPERIENCE > CATIA Systems Synthesis Analysis .
3. Select one of the following commands:
  - Export to MDZipX File - exports the .svg file for each diagram.
  - Export to MDZipX File Including Data from Used Projects - exports the .svg file for each diagram and the data from used projects. [ATTACHMENT filename='export_to_mdzipx_file.png']
4. In the open dialog, select the target directory for the exported file.
5. Click the Save button.

The exported MDZipX file is saved in the specified target directory.

##### Publishing MDZipX files to Teamwork Cloud

When working with Teamwork Cloud projects, you can publish all model diagrams to Teamwork Cloud as an MDZipX file. During publishing, each diagram from every project version is saved as an SVG file.

#### NOTE: Prerequisite

Prerequisite

Publishing MDZipX files to Teamwork Cloud works only with Teamwork Cloud projects.

To publish MDZipX to Teamwork Cloud

1. [CONFLUENCE_PAGE title='Opening Teamwork Cloud projects' space='CM'] .
2. In the main menu, click 3DEXPERIENCE > CATIA Systems Synthesis Analysis .
3. Select Publish MDZipX File to Teamwork Cloud . [ATTACHMENT filename='publish_mdzipx_to_teamwork_cloud.png']

##### Publishing diagrams as project assets to the **3D**EXPERIENCE platform

When working with projects stored on the **3D**EXPERIENCE platform, you can export model diagrams to the SVG format and store them as auxiliary resources inside the model. The SVG files are then retrieved from the model and displayed in the CATIA Systems Traceability Application.

#### NOTE: Prerequisites

Prerequisites

- Publishing diagrams as project assets works only with the projects stored on the 3D EXPERIENCE platform.
- Only the [CONFLUENCE_PAGE title='Complete diagrams' space='MT'] are exported to the SVG format and published as project assets.

To publish diagrams as project assets to the **3D**EXPERIENCE platform

1. [CONFLUENCE_PAGE title='Opening projects from 3DEXPERIENCE platform' space='CM']Open a project stored in the **3D**EXPERIENCE platform .
2. In the main menu, select 3DEXPERIENCE > CATIA Systems Synthesis Analysis > Publish Diagrams as Assets . A new Assets package with the SVG package inside it is created under the Model element. All diagrams marked as complete are exported to SVG and stored under the SVG package. [ATTACHMENT filename='assets_package.png']
3. [CONFLUENCE_PAGE title='Committing changes to 3DEXPERIENCE platform' space='CM']Commit changes to the **3D**EXPERIENCE platform .

##### Environment Options

You modify the behavior of the MDZipX plugin by changing the environment options under the CATIA Systems Synthesis Analysis group. For example, you can include diagrams from used projects to exported MDZipX files or choose to publish an MDZipX file to Teamwork Cloud automatically upon every project commit.

You can specify the diagram export options, such as dimensions and building time (the latter applies only to tables and matrices), in the **Project Options** dialog. See the [CONFLUENCE_PAGE title='Diagram image export' space='MT'] page to learn more.

To include diagrams from used projects to an MDZipX file or project assets

1. In the main menu, select Options > Environment .
2. In the left-side panel, select the Collaboration option group.
3. Set the Publish Diagrams from Used Projects option to true .
4. Click OK .

Publish an MDZipX file to Teamwork Cloud automatically upon project commit

1. In the main menu, select Options > Environment .
2. In the left-side panel, select the Collaboration option group.
3. Set the Publish MDZipX Upon Commit option to true .
4. Click OK .

MagicDraw and NoMagic Teamwork Cloud Connectors Configuration

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>An integrated MDZipX plugin helps you improve the display of diagrams on the <strong>3D</strong>EXPERIENCE platform by exporting them to an MDZipX file. You can use different export options for different types of projects as described below.</p><h3>Exporting diagrams to an MDZipX file</h3><p>You can export diagrams from a local project to an MDZipX file either with or without used project data.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="05af13e6-4be0-4497-a1f7-a521aad3e6d0"><ac:parameter ac:name="title">Prerequisite</ac:parameter><ac:rich-text-body><p>Publishing diagrams to an MDZipX file works only with local projects.</p></ac:rich-text-body></ac:structured-macro><p><br /></p><p>To export diagrams to an MDZipX file</p><hr /><ol><li data-uuid="2a9a2eac-f435-407f-b718-41f7d1afa428">Open a local project</li><li data-uuid="f42a42da-1697-4811-8b75-857b778f0ffc">In the main menu, select <strong>3DEXPERIENCE </strong>&gt; <strong>CATIA Systems Synthesis Analysis</strong>.</li><li data-uuid="b4d22813-f5bb-452c-8e20-9abb40685db7">Select one of the following commands:<ul><li><strong>Export to MDZipX File</strong> - exports the .svg file for each diagram.</li><li><strong>Export to MDZipX File Including Data from Used Projects</strong> - exports the .svg file for each diagram and the data from used projects.<br /><br /><ac:image ac:height="114"><ri:attachment ri:filename="export_to_mdzipx_file.png" /></ac:image><br /><br /></li></ul></li><li data-uuid="5297151b-960f-4b04-90ae-3c20b3344db2">In the open dialog, select the target directory for the exported file.</li><li data-uuid="89c21f45-a86d-4099-b404-75338bf4ed44">Click the <strong>Save</strong> button.</li></ol><p><br />The exported MDZipX file is saved in the specified target directory.</p><h3>Publishing MDZipX files to Teamwork Cloud</h3><p>When working with Teamwork Cloud projects, you can publish all model diagrams to Teamwork Cloud as an MDZipX file. During publishing, each diagram from every project version is saved as an SVG file.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="3d9c34ce-fd05-4082-8685-827f0e49ff5f"><ac:parameter ac:name="title">Prerequisite</ac:parameter><ac:rich-text-body><p>Publishing MDZipX files to Teamwork Cloud works only with Teamwork Cloud projects.</p></ac:rich-text-body></ac:structured-macro><p><br /></p><p>To publish MDZipX to Teamwork Cloud</p><hr /><ol><li data-uuid="7d4818d1-281f-44d7-b496-1a2c3e6df155"><ac:link><ri:page ri:space-key="CM" ri:content-title="Opening Teamwork Cloud projects" /><ac:plain-text-link-body><![CDATA[Open a Teamwork Cloud project]]></ac:plain-text-link-body></ac:link>.</li><li data-uuid="737babcb-be90-43b0-a110-dd7314076b05">In the main menu, click <strong>3DEXPERIENCE </strong>&gt; <strong>CATIA Systems Synthesis Analysis</strong>.</li><li data-uuid="9e96a321-b370-4967-b31a-e94c7ef530b9">Select <strong>Publish MDZipX File to Teamwork Cloud</strong>.<br /><br /><ac:image ac:height="114"><ri:attachment ri:filename="publish_mdzipx_to_teamwork_cloud.png" /></ac:image></li></ol><h3>Publishing diagrams as project assets to the <strong>3D</strong>EXPERIENCE platform</h3><p style="text-align: left;">When working with projects stored on the <strong>3D</strong>EXPERIENCE platform, you can export model diagrams to the SVG format and store them as auxiliary resources inside the model. The SVG files are then retrieved from the model and displayed in <span style="color:var(--ds-text,#172b4d);">the CATIA Systems Traceability Application.</span></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="7a6b8a47-a73e-4570-b634-fcc821f25410"><ac:parameter ac:name="title">Prerequisites</ac:parameter><ac:rich-text-body><ul><li data-uuid="dc1397b9-5bcf-41b1-8277-b0e0b34caf9a">Publishing diagrams as project assets works only with the projects stored on the <strong>3D</strong>EXPERIENCE platform.</li><li data-uuid="428da09a-ab60-4a5b-83f7-12a135caf653">Only the <ac:link><ri:page ri:space-key="MT" ri:content-title="Complete diagrams" /><ac:plain-text-link-body><![CDATA[diagrams marked as complete]]></ac:plain-text-link-body></ac:link> are exported to the SVG format and published as project assets.</li></ul></ac:rich-text-body></ac:structured-macro><p style="text-align: left;"><br /></p><p>To publish diagrams as project assets to the <strong>3D</strong>EXPERIENCE platform</p><hr /><ol><li data-uuid="6d4c0cbc-d8d0-403b-8704-4019706bca11"><ac:link><ri:page ri:space-key="CM" ri:content-title="Opening projects from 3DEXPERIENCE platform" /><ac:link-body>Open a project stored in the <strong>3D</strong>EXPERIENCE platform</ac:link-body></ac:link><span>.</span></li><li data-uuid="3e849e8a-0b84-4115-b8bd-f5eaf1d99c8d">In the main menu, select <strong>3DEXPERIENCE </strong>&gt; <strong>CATIA Systems Synthesis Analysis</strong> &gt; <strong>Publish Diagrams as Assets</strong>. A new <em>Assets</em> package with the <em>SVG</em> package inside it is created under the Model element. All diagrams marked as complete are exported to SVG and stored under the <em>SVG</em> package.<br /><br /><ac:image><ri:attachment ri:filename="assets_package.png" /></ac:image><br /><br /></li><li data-uuid="28607262-6d81-44ac-a4ba-fa0c9c8b0e47"><ac:link><ri:page ri:space-key="CM" ri:content-title="Committing changes to 3DEXPERIENCE platform" /><ac:link-body>Commit changes to the <strong>3D</strong>EXPERIENCE platform</ac:link-body></ac:link>.</li></ol><h3><span>Environment Options</span></h3><p>You modify the behavior of the MDZipX plugin by changing the environment options under the CATIA Systems Synthesis Analysis group. For example, you can include diagrams from used projects to exported MDZipX files or choose to publish an MDZipX file to Teamwork Cloud automatically upon every project commit. </p><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="0ae12f24-a4b3-4614-b014-2a939c187bc5"><ac:rich-text-body><p>You can specify the diagram export options, such as dimensions and building time (the latter applies only to tables and matrices), in the <strong>Project Options</strong> dialog. See the <ac:link><ri:page ri:space-key="MT" ri:content-title="Diagram image export" /></ac:link> page to learn more.</p></ac:rich-text-body></ac:structured-macro><p><br /></p><p>To include diagrams from used projects to an MDZipX file or project assets</p><hr /><ol><li data-uuid="63dfba22-e78c-4ba4-93ee-90de52cdf600">In the main menu, select <strong>Options</strong> &gt; <strong>Environment</strong>. </li><li data-uuid="3de2c995-9c2a-45d0-9959-6d96da701c74">In the left-side panel, select the <strong>Collaboration</strong> option group.</li><li data-uuid="43b2f24f-c142-48ca-8ccf-eca3ae0d4692">Set the <strong>Publish Diagrams from Used Projects</strong> option to <em>true</em>.</li><li data-uuid="ac1a1c76-3d62-4f41-81a2-5b130ced8474">Click <strong>OK</strong>.<br /><br /></li></ol><p>Publish an MDZipX file to Teamwork Cloud automatically upon project commit</p><hr /><ol><li data-uuid="120b36f5-e16d-49bc-adc4-2823fbd316d9">In the main menu, select <strong>Options</strong> &gt; <strong>Environment</strong>.</li><li data-uuid="f779d783-d6f7-4e24-b78a-50fe99cad30c">In the left-side panel, select the <strong>Collaboration</strong> option group.</li><li data-uuid="3292a8be-2865-4a67-8ee3-df451a63c34c">Set the <strong>Publish MDZipX Upon Commit</strong> option to <em>true</em>.</li><li data-uuid="63c1d0fc-6440-4fd2-a0e6-ccbeccfa89dc">Click <strong>OK</strong>.</li></ol><p><br /></p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="671a27e2-5851-4cc8-899c-f76020a4f529"><ac:rich-text-body>For more information, please refer to <a href="https://help.3ds.com/2024x/English/DSDoc/TraUserMap/smv-c-ad-NoMagicConfiguration.htm?contextscope=onpremise">MagicDraw and NoMagic Teamwork Cloud Connectors Configuration</a>.</ac:rich-text-body></ac:structured-macro><p><br /></p>
````

<!--NOMAGIC_PAGE id=258048893 space=CSS version=1 -->
## PAGE 00004: Versions of CATIA Systems Synthesis

- page_id: `258048893`
- space_key: `CSS`
- source_url: https://docs.nomagic.com/spaces/CSS/pages/258048893/Versions+of+CATIA+Systems+Synthesis
- version_number: 1
- version_date: `2025-09-25T12:57:40.982+02:00`
- ancestors: 
- labels: []

### NORMALIZED CONTENT

6d8afdabf55b8956e5b0758399eb8fe3

CATIA Systems Synthesis

documentVersions

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="scroll-document-location" ac:schema-version="1" ac:macro-id="8b3753b2-098f-415e-a8e9-f3e2838f27f5"><ac:parameter ac:name="permaId">6d8afdabf55b8956e5b0758399eb8fe3</ac:parameter><ac:parameter ac:name="documentTitle">CATIA Systems Synthesis</ac:parameter><ac:parameter ac:name="key">documentVersions</ac:parameter></ac:structured-macro>
````
