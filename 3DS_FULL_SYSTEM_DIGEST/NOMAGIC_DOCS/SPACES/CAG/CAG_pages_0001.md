# NOMAGIC DOCUMENTATION SPACE: CATIA Agile Governance

<!--NOMAGIC_SPACE key=CAG chunk=1 -->

<!--NOMAGIC_PAGE id=304014858 space=CAG version=1 -->
## PAGE 00001: (2026x Refresh1) CATIA Agile Governance

- page_id: `304014858`
- space_key: `CAG`
- source_url: https://docs.nomagic.com/spaces/CAG/pages/304014858/2026x+Refresh1+CATIA+Agile+Governance
- version_number: 1
- version_date: `2026-04-29T17:05:00.810+02:00`
- ancestors: Versions of CATIA Agile Governance
- labels: []

### NORMALIZED CONTENT

##### Description

The CATIA Agile Governance plugin allows the generation of the work breakdown structure, initializing the Agile development plans according to a protocol collecting traceability through all phases of software development.

##### Prerequisites

- Create a new SysML v1 Project.
- Use profile AgileGovernance.
- Options > Environment > Agile Governance set values: Server URL and API key : [ATTACHMENT filename='Environment options.PNG']
- Connect to Cloud **3D**EXPERIENCEPlatform (**3DEXPERIENCE**> **Login**): [ATTACHMENT filename='Connect to platform.PNG']

Now, you have access to the contextual menu of the plugin.

##### Working with Agile Governance Plugin

The following operations can be realized with single or multiple selections:

- 
- 

###### Item association

You can now associate the ALM Project with the Model.

To associate the ALM Project with the model

1. In the Containment tree, right-click the Model.
2. In the shortcut menu, click Agile Governance and select Associate Project .

As a result, the «AgileProject» stereotype is applied to the Model.

[IMAGE alt='' src=''][IMAGE alt='' src='']

Attributes are filled with information to link with the Semantic Graph Index.

Once the project is associated, you can associate MBSE elements with ALM items:

- Capabilities
- Stories
- Epics
- Features

A wizard allows you to choose among several items in your lifecycle management system application.

[IMAGE alt='' src='']

###### Item creation

You can also create ALM items directly from the contextual menu and associate them with the MBSE element. Stereotypes appear. On your lifecycle management system application, a new item is created.

A wizard allows you to edit the name of the new item and shows you the context project.

[IMAGE alt='' src='']

###### Diagrams

There are two tables to see the association with a tree model and all the stories associated with their ALM.

- Agile Governance Status Table . A table of the MBSE elements associated with a tree model and columns for their type, title, and status.

[IMAGE alt='' src='']

- Agile Governance Story Table . A table of all the stories associated with their ALM title and reference, description, status, acceptance criteria, and test cases.

[IMAGE alt='' src='']

###### Column "Title" is a URL reference to the ALM item in your lifecycle management system application.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<h3>Description</h3><p>The CATIA Agile Governance plugin allows the generation of the work breakdown structure, initializing the Agile development plans according to a protocol collecting traceability through all phases of software development.</p><h3>Prerequisites</h3><ul><li data-uuid="57d7fbd9-9f4a-4cc5-8386-2d97f8699590">Create a new SysML v1 Project.</li><li data-uuid="6ae8690f-846a-4154-bbd4-8692b73319ce">Use profile <em>AgileGovernance.</em></li><li data-uuid="de74e73b-9da9-40f9-a27d-a6c83081c464"><strong>Options </strong>&gt; <strong>Environment </strong>&gt; <strong>Agile Governance</strong> set values: <strong>Server URL</strong> and <strong>API key</strong>:<br /><ac:image><ri:attachment ri:filename="Environment options.PNG"><ri:page ri:content-title="(2026x Refresh1) CATIA Agile Governance" /></ri:attachment></ac:image></li><li data-uuid="fdb2e291-a0e3-4854-8185-c42bddef13fa"><span>Connect to Cloud <span style="color:var(--ds-text-accent-purple-bolder,#352c63);"><strong>3D</strong>EXPERIENCE </span>Platform (<strong>3DEXPERIENCE </strong>&gt; <strong>Login</strong>):<br /></span><ac:image><ri:attachment ri:filename="Connect to platform.PNG"><ri:page ri:content-title="(2026x Refresh1) CATIA Agile Governance" /></ri:attachment></ac:image></li></ul><p>Now, you have access to the contextual menu of the plugin.</p><h3>Working with Agile Governance Plugin</h3><p>The following operations can be realized with single or multiple selections:</p><ul><li data-uuid="55e665d5-7ce7-4a8f-ad6d-6bb317879592"><ac:link ac:anchor="Item association" /></li><li data-uuid="fea22d14-e9f6-4b17-adcc-f56e96bec41d"><ac:link ac:anchor="Item creation" /></li></ul><h4>Item association</h4><p>You can now associate the ALM Project with the Model.</p><p><br /></p><p>To associate the ALM Project with the model</p><hr /><ol><li data-uuid="41461437-6b74-4925-993e-c7741dd4903c">In the Containment tree, right-click the Model.</li><li data-uuid="53791f1f-6a0c-446d-be56-4f15483fa1e1">In the shortcut menu, click <strong>Agile Governance</strong> and select <strong>Associate Project</strong>.</li></ol><p>As a result, the «AgileProject» stereotype is applied to the Model. </p><p><ac:image><ri:attachment ri:filename="Associate project.png"><ri:page ri:content-title="(2026x Refresh1) CATIA Agile Governance" /></ri:attachment></ac:image><ac:image><ri:attachment ri:filename="Stereotype.png"><ri:page ri:content-title="(2026x Refresh1) CATIA Agile Governance" /></ri:attachment></ac:image></p><p>Attributes are filled with information to link with the Semantic Graph Index.</p><p>Once the project is associated, you can associate MBSE elements with ALM items:</p><ul><li data-uuid="0abc33bb-3aa6-421f-ba74-5729639adbf6">Capabilities</li><li data-uuid="5bb96057-52c2-459a-a69e-9f20096e0b7d">Stories</li><li data-uuid="0df9bba7-510b-45d0-ad67-6def8b69f485">Epics</li><li data-uuid="ae9a9b4c-4bb2-41e6-b11c-bf9d93e0a23e">Features</li></ul><p>A wizard allows you to choose among several items in your lifecycle management system application.</p><p><ac:image><ri:attachment ri:filename="Associate Wizard.png"><ri:page ri:content-title="(2026x Refresh1) CATIA Agile Governance" /></ri:attachment></ac:image></p><h4>Item creation</h4><p>You can also create ALM items directly from the contextual menu and associate them with the MBSE element. Stereotypes appear. On your lifecycle management system application, a new item is created.</p><p>A wizard allows you to edit the name of the new item and shows you the context project.</p><p><ac:image><ri:attachment ri:filename="Creation Wizard.png"><ri:page ri:content-title="(2026x Refresh1) CATIA Agile Governance" /></ri:attachment></ac:image></p><h4>Diagrams</h4><p>There are two tables to see the association with a tree model and all the stories associated with their ALM.</p><ul><li data-uuid="bf07a27a-2550-4745-8b96-b67a904f238f"><strong>Agile Governance Status Table</strong>. A table of the MBSE elements associated with a tree model and columns for their type, title, and status.</li></ul><p><ac:image><ri:attachment ri:filename="Status table.png"><ri:page ri:content-title="(2026x Refresh1) CATIA Agile Governance" /></ri:attachment></ac:image></p><ul><li data-uuid="35e5aed8-a6dc-4c74-b8fe-a787959bf0df"><strong>Agile Governance Story Table</strong>. A table of all the stories associated with their ALM title and reference, description, status, acceptance criteria, and test cases.</li></ul><p><ac:image><ri:attachment ri:filename="Story Table.png"><ri:page ri:content-title="(2026x Refresh1) CATIA Agile Governance" /></ri:attachment></ac:image></p><h6 style="text-align: center;">Column &quot;Title&quot; is a URL reference to the ALM item in your lifecycle management system application.</h6><p><br /></p>
````

<!--NOMAGIC_PAGE id=258049077 space=CAG version=2 -->
## PAGE 00002: (2026x) CATIA Agile Governance

- page_id: `258049077`
- space_key: `CAG`
- source_url: https://docs.nomagic.com/spaces/CAG/pages/258049077/2026x+CATIA+Agile+Governance
- version_number: 2
- version_date: `2025-09-25T13:43:28.706+02:00`
- ancestors: Versions of CATIA Agile Governance
- labels: []

### NORMALIZED CONTENT

##### Description

The CATIA Agile Governance plugin allows the generation of the work breakdown structure, initializing the Agile development plans according to a protocol collecting traceability through all phases of software development.

##### Prerequisites

- Create a new SysML v1 Project.
- Use profile AgileGovernance.
- Options > Environment > Agile Governance set values: Server URL and API key : [ATTACHMENT filename='Environment options.PNG']
- Connect to Cloud **3D**EXPERIENCEPlatform (**3DEXPERIENCE**> **Login**): [ATTACHMENT filename='Connect to platform.PNG']

Now, you have access to the contextual menu of the plugin.

##### Working with Agile Governance Plugin

The following operations can be realized with single or multiple selections:

- 
- 

###### Item association

You can now associate the ALM Project with the Model.

To associate the ALM Project with the model

1. In the Containment tree, right-click the Model.
2. In the shortcut menu, click Agile Governance and select Associate Project .

As a result, the «AgileProject» stereotype is applied to the Model.

[IMAGE alt='' src=''][IMAGE alt='' src='']

Attributes are filled with information to link with the Semantic Graph Index.

Once the project is associated, you can associate MBSE elements with ALM items:

- Capabilities
- Stories
- Epics
- Features

A wizard allows you to choose among several items in your lifecycle management system application.

[IMAGE alt='' src='']

###### Item creation

You can also create ALM items directly from the contextual menu and associate them with the MBSE element. Stereotypes appear. On your lifecycle management system application, a new item is created.

A wizard allows you to edit the name of the new item and shows you the context project.

[IMAGE alt='' src='']

###### Diagrams

There are two tables to see the association with a tree model and all the stories associated with their ALM.

- Agile Governance Status Table . A table of the MBSE elements associated with a tree model and columns for their type, title, and status.

[IMAGE alt='' src='']

- Agile Governance Story Table . A table of all the stories associated with their ALM title and reference, description, status, acceptance criteria, and test cases.

[IMAGE alt='' src='']

###### Column "Title" is a URL reference to the ALM item in your lifecycle management system application.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<h3>Description</h3><p>The CATIA Agile Governance plugin allows the generation of the work breakdown structure, initializing the Agile development plans according to a protocol collecting traceability through all phases of software development.</p><h3>Prerequisites</h3><ul><li data-uuid="57d7fbd9-9f4a-4cc5-8386-2d97f8699590">Create a new SysML v1 Project.</li><li data-uuid="6ae8690f-846a-4154-bbd4-8692b73319ce">Use profile <em>AgileGovernance.</em></li><li data-uuid="de74e73b-9da9-40f9-a27d-a6c83081c464"><strong>Options </strong>&gt; <strong>Environment </strong>&gt; <strong>Agile Governance</strong> set values: <strong>Server URL</strong> and <strong>API key</strong>:<br /><ac:image><ri:attachment ri:filename="Environment options.PNG" /></ac:image></li><li data-uuid="fdb2e291-a0e3-4854-8185-c42bddef13fa"><span>Connect to Cloud <span style="color:var(--ds-text-accent-purple-bolder,#352c63);"><strong>3D</strong>EXPERIENCE </span>Platform (<strong>3DEXPERIENCE </strong>&gt; <strong>Login</strong>):<br /></span><ac:image><ri:attachment ri:filename="Connect to platform.PNG" /></ac:image></li></ul><p>Now, you have access to the contextual menu of the plugin.</p><h3>Working with Agile Governance Plugin</h3><p>The following operations can be realized with single or multiple selections:</p><ul><li data-uuid="55e665d5-7ce7-4a8f-ad6d-6bb317879592"><ac:link ac:anchor="Item association" /></li><li data-uuid="fea22d14-e9f6-4b17-adcc-f56e96bec41d"><ac:link ac:anchor="Item creation" /></li></ul><h4>Item association</h4><p>You can now associate the ALM Project with the Model.</p><p><br /></p><p>To associate the ALM Project with the model</p><hr /><ol><li data-uuid="41461437-6b74-4925-993e-c7741dd4903c">In the Containment tree, right-click the Model.</li><li data-uuid="53791f1f-6a0c-446d-be56-4f15483fa1e1">In the shortcut menu, click <strong>Agile Governance</strong> and select <strong>Associate Project</strong>.</li></ol><p>As a result, the «AgileProject» stereotype is applied to the Model. </p><p><ac:image><ri:attachment ri:filename="Associate project.png" /></ac:image><ac:image><ri:attachment ri:filename="Stereotype.png" /></ac:image></p><p>Attributes are filled with information to link with the Semantic Graph Index.</p><p>Once the project is associated, you can associate MBSE elements with ALM items:</p><ul><li data-uuid="0abc33bb-3aa6-421f-ba74-5729639adbf6">Capabilities</li><li data-uuid="5bb96057-52c2-459a-a69e-9f20096e0b7d">Stories</li><li data-uuid="0df9bba7-510b-45d0-ad67-6def8b69f485">Epics</li><li data-uuid="ae9a9b4c-4bb2-41e6-b11c-bf9d93e0a23e">Features</li></ul><p>A wizard allows you to choose among several items in your lifecycle management system application.</p><p><ac:image><ri:attachment ri:filename="Associate Wizard.png" /></ac:image></p><h4>Item creation</h4><p>You can also create ALM items directly from the contextual menu and associate them with the MBSE element. Stereotypes appear. On your lifecycle management system application, a new item is created.</p><p>A wizard allows you to edit the name of the new item and shows you the context project.</p><p><ac:image><ri:attachment ri:filename="Creation Wizard.png" /></ac:image></p><h4>Diagrams</h4><p>There are two tables to see the association with a tree model and all the stories associated with their ALM.</p><ul><li data-uuid="bf07a27a-2550-4745-8b96-b67a904f238f"><strong>Agile Governance Status Table</strong>. A table of the MBSE elements associated with a tree model and columns for their type, title, and status.</li></ul><p><ac:image><ri:attachment ri:filename="Status table.png" /></ac:image></p><ul><li data-uuid="35e5aed8-a6dc-4c74-b8fe-a787959bf0df"><strong>Agile Governance Story Table</strong>. A table of all the stories associated with their ALM title and reference, description, status, acceptance criteria, and test cases.</li></ul><p><ac:image><ri:attachment ri:filename="Story Table.png" /></ac:image></p><h6 style="text-align: center;">Column &quot;Title&quot; is a URL reference to the ALM item in your lifecycle management system application.</h6><p><br /></p>
````

<!--NOMAGIC_PAGE id=258049058 space=CAG version=3 -->
## PAGE 00003: CATIA Agile Governance

- page_id: `258049058`
- space_key: `CAG`
- source_url: https://docs.nomagic.com/spaces/CAG/pages/258049058/CATIA+Agile+Governance
- version_number: 3
- version_date: `2025-09-25T13:43:07.185+02:00`
- ancestors: 
- labels: []

### NORMALIZED CONTENT

##### Description

The CATIA Agile Governance plugin allows the generation of the work breakdown structure, initializing the Agile development plans according to a protocol collecting traceability through all phases of software development.

##### Prerequisites

- Create a new SysML v1 Project.
- Use profile AgileGovernance.
- Options > Environment > Agile Governance set values: Server URL and API key : [ATTACHMENT filename='Environment options.PNG']
- Connect to Cloud **3D**EXPERIENCEPlatform (**3DEXPERIENCE**> **Login**): [ATTACHMENT filename='Connect to platform.PNG']

Now, you have access to the contextual menu of the plugin.

##### Working with Agile Governance Plugin

The following operations can be realized with single or multiple selections:

- 
- 

###### Item association

You can now associate the ALM Project with the Model.

To associate the ALM Project with the model

1. In the Containment tree, right-click the Model.
2. In the shortcut menu, click Agile Governance and select Associate Project .

As a result, the «AgileProject» stereotype is applied to the Model.

[IMAGE alt='' src=''][IMAGE alt='' src='']

Attributes are filled with information to link with the Semantic Graph Index.

Once the project is associated, you can associate MBSE elements with ALM items:

- Capabilities
- Stories
- Epics
- Features

A wizard allows you to choose among several items in your lifecycle management system application.

[IMAGE alt='' src='']

###### Item creation

You can also create ALM items directly from the contextual menu and associate them with the MBSE element. Stereotypes appear. On your lifecycle management system application, a new item is created.

A wizard allows you to edit the name of the new item and shows you the context project.

[IMAGE alt='' src='']

###### Diagrams

There are two tables to see the association with a tree model and all the stories associated with their ALM.

- Agile Governance Status Table . A table of the MBSE elements associated with a tree model and columns for their type, title, and status.

[IMAGE alt='' src='']

- Agile Governance Story Table . A table of all the stories associated with their ALM title and reference, description, status, acceptance criteria, and test cases.

[IMAGE alt='' src='']

###### Column "Title" is a URL reference to the ALM item in your lifecycle management system application.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<h3>Description</h3><p>The CATIA Agile Governance plugin allows the generation of the work breakdown structure, initializing the Agile development plans according to a protocol collecting traceability through all phases of software development.</p><h3>Prerequisites</h3><ul><li data-uuid="57d7fbd9-9f4a-4cc5-8386-2d97f8699590">Create a new SysML v1 Project.</li><li data-uuid="6ae8690f-846a-4154-bbd4-8692b73319ce">Use profile <em>AgileGovernance.</em></li><li data-uuid="de74e73b-9da9-40f9-a27d-a6c83081c464"><strong>Options </strong>&gt; <strong>Environment </strong>&gt; <strong>Agile Governance</strong> set values: <strong>Server URL</strong> and <strong>API key</strong>:<br /><ac:image><ri:attachment ri:filename="Environment options.PNG" /></ac:image></li><li data-uuid="fdb2e291-a0e3-4854-8185-c42bddef13fa"><span>Connect to Cloud <span style="color:var(--ds-text-accent-purple-bolder,#352c63);"><strong>3D</strong>EXPERIENCE </span>Platform (<strong>3DEXPERIENCE </strong>&gt; <strong>Login</strong>):<br /></span><ac:image><ri:attachment ri:filename="Connect to platform.PNG" /></ac:image></li></ul><p>Now, you have access to the contextual menu of the plugin.</p><h3>Working with Agile Governance Plugin</h3><p>The following operations can be realized with single or multiple selections:</p><ul><li data-uuid="55e665d5-7ce7-4a8f-ad6d-6bb317879592"><ac:link ac:anchor="Item association" /></li><li data-uuid="fea22d14-e9f6-4b17-adcc-f56e96bec41d"><ac:link ac:anchor="Item creation" /></li></ul><h4>Item association</h4><p>You can now associate the ALM Project with the Model.</p><p><br /></p><p>To associate the ALM Project with the model</p><hr /><ol><li data-uuid="41461437-6b74-4925-993e-c7741dd4903c">In the Containment tree, right-click the Model.</li><li data-uuid="53791f1f-6a0c-446d-be56-4f15483fa1e1">In the shortcut menu, click <strong>Agile Governance</strong> and select <strong>Associate Project</strong>.</li></ol><p>As a result, the «AgileProject» stereotype is applied to the Model. </p><p><ac:image><ri:attachment ri:filename="Associate project.png" /></ac:image><ac:image><ri:attachment ri:filename="Stereotype.png" /></ac:image></p><p>Attributes are filled with information to link with the Semantic Graph Index.</p><p>Once the project is associated, you can associate MBSE elements with ALM items:</p><ul><li data-uuid="0abc33bb-3aa6-421f-ba74-5729639adbf6">Capabilities</li><li data-uuid="5bb96057-52c2-459a-a69e-9f20096e0b7d">Stories</li><li data-uuid="0df9bba7-510b-45d0-ad67-6def8b69f485">Epics</li><li data-uuid="ae9a9b4c-4bb2-41e6-b11c-bf9d93e0a23e">Features</li></ul><p>A wizard allows you to choose among several items in your lifecycle management system application.</p><p><ac:image><ri:attachment ri:filename="Associate Wizard.png" /></ac:image></p><h4>Item creation</h4><p>You can also create ALM items directly from the contextual menu and associate them with the MBSE element. Stereotypes appear. On your lifecycle management system application, a new item is created.</p><p>A wizard allows you to edit the name of the new item and shows you the context project.</p><p><ac:image><ri:attachment ri:filename="Creation Wizard.png" /></ac:image></p><h4>Diagrams</h4><p>There are two tables to see the association with a tree model and all the stories associated with their ALM.</p><ul><li data-uuid="bf07a27a-2550-4745-8b96-b67a904f238f"><strong>Agile Governance Status Table</strong>. A table of the MBSE elements associated with a tree model and columns for their type, title, and status.</li></ul><p><ac:image><ri:attachment ri:filename="Status table.png" /></ac:image></p><ul><li data-uuid="35e5aed8-a6dc-4c74-b8fe-a787959bf0df"><strong>Agile Governance Story Table</strong>. A table of all the stories associated with their ALM title and reference, description, status, acceptance criteria, and test cases.</li></ul><p><ac:image><ri:attachment ri:filename="Story Table.png" /></ac:image></p><h6 style="text-align: center;">Column &quot;Title&quot; is a URL reference to the ALM item in your lifecycle management system application.</h6><p><br /></p>
````

<!--NOMAGIC_PAGE id=258049074 space=CAG version=1 -->
## PAGE 00004: Versions of CATIA Agile Governance

- page_id: `258049074`
- space_key: `CAG`
- source_url: https://docs.nomagic.com/spaces/CAG/pages/258049074/Versions+of+CATIA+Agile+Governance
- version_number: 1
- version_date: `2025-09-25T13:39:07.499+02:00`
- ancestors: 
- labels: []

### NORMALIZED CONTENT

eb9662872c27431841048dddbff71911

CATIA Agile Governance

documentVersions

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="scroll-document-location" ac:schema-version="1" ac:macro-id="6fe7d892-b522-4f85-a105-ca295a5a6a4d"><ac:parameter ac:name="permaId">eb9662872c27431841048dddbff71911</ac:parameter><ac:parameter ac:name="documentTitle">CATIA Agile Governance</ac:parameter><ac:parameter ac:name="key">documentVersions</ac:parameter></ac:structured-macro>
````
