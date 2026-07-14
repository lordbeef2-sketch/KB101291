# NOMAGIC DOCUMENTATION SPACE: Magic Systems EE Architect 2024x Refresh1

<!--NOMAGIC_SPACE key=CEAP2024xR1 chunk=1 -->

<!--NOMAGIC_PAGE id=171180816 space=CEAP2024xR1 version=1 -->
## PAGE 00001: Concepts

- page_id: `171180816`
- space_key: `CEAP2024xR1`
- source_url: https://docs.nomagic.com/spaces/CEAP2024xR1/pages/171180816/Concepts
- version_number: 1
- version_date: `2024-03-13T12:29:20.111+01:00`
- ancestors: Magic Systems EE Architect
- labels: []

### NORMALIZED CONTENT

EE Architecture modeling concepts are classified under the following architecture domains:

- Software Architecture
- Hardware Architecture
- Network Communication

These concepts enable you to perform in a System Mapping allocation of Software Architecture on Hardware Architecture given the Communication specifications.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>EE Architecture modeling concepts are classified under the following architecture domains:</p><ul><li>Software Architecture</li><li>Hardware Architecture</li><li>Network Communication</li></ul><p>These concepts enable you to perform in a System Mapping allocation of Software Architecture on Hardware Architecture given the Communication specifications.</p>
````

<!--NOMAGIC_PAGE id=171180815 space=CEAP2024xR1 version=2 -->
## PAGE 00002: Getting Started

- page_id: `171180815`
- space_key: `CEAP2024xR1`
- source_url: https://docs.nomagic.com/spaces/CEAP2024xR1/pages/171180815/Getting+Started
- version_number: 2
- version_date: `2024-05-09T11:36:21.686+02:00`
- ancestors: Magic Systems EE Architect
- labels: []

### NORMALIZED CONTENT

The Magic Systems EE Architect plugin requires the [CONFLUENCE_PAGE title='SysML Plugin Documentation' space='SYSMLP2024xR1'] to be installed in your modeling tool. For the information about how to install the plugin, see [CONFLUENCE_PAGE title='Installing plugins' space='IL2024xR1'].

The following are two ways how you can install the Magic Systems EE Architect plugin.

To download and install a plugin via the **Resource/Plugin Manager** dialog

1. Start your modeling tool.
2. From the modeling tool main menu, select Help > Resource/Plugin Manager . The Resource/Plugin Manager dialog opens and prompts you to check for the latest product updates and resources.
3. Click Check for Updates > Check .
4. Select the check box near the desired plugin and click Download/Install .
5. Restart your modeling tool.

To install a plugin from the downloaded archive file (zip) via the **Resource/Plugin Manager** dialog

1. Start your modeling tool.
2. From the main menu of a modeling tool, select Help > Resource/Plugin Manager .
3. Click the Import button.
4. Specify the downloaded plugin file location. The plugin is extracted and installed automatically.
5. Restart your modeling tool.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>The Magic Systems EE Architect plugin requires the <ac:link><ri:page ri:space-key="SYSMLP2024xR1" ri:content-title="SysML Plugin Documentation" /><ac:plain-text-link-body><![CDATA[SysML plugin]]></ac:plain-text-link-body></ac:link> to be installed in your modeling tool. For the information about how to install the plugin, see <ac:link><ri:page ri:space-key="IL2024xR1" ri:content-title="Installing plugins" /></ac:link>.</p><p><br /></p><p>The following are two ways how you can install the Magic Systems EE Architect plugin.</p><p><br /></p><p>To download and install a plugin via the <strong>Resource/Plugin Manager</strong> dialog</p><hr /><ol><li>Start your modeling tool.</li><li>From the modeling tool main menu, select <strong>Help </strong>&gt; <strong>Resource/Plugin Manager</strong>. The <strong>Resource/Plugin Manager</strong> dialog opens and prompts you to check for the latest product updates and resources.</li><li>Click <strong>Check for Updates</strong> &gt; <strong>Check</strong>.</li><li>Select the check box near the desired plugin and click <strong>Download/Install</strong>.</li><li>Restart your modeling tool.</li></ol><p><br /></p><p>To install a plugin from the downloaded archive file (zip) via the <strong>Resource/Plugin Manager</strong> dialog</p><hr /><ol><li>Start your modeling tool.</li><li>From the main menu of a modeling tool, select <strong>Help </strong>&gt; <strong>Resource/Plugin Manager</strong>.</li><li>Click the <strong>Import </strong>button.</li><li>Specify the downloaded plugin file location. The plugin is extracted and installed automatically.</li><li>Restart your modeling tool.</li></ol>
````

<!--NOMAGIC_PAGE id=171180822 space=CEAP2024xR1 version=2 -->
## PAGE 00003: Hardware Architecture

- page_id: `171180822`
- space_key: `CEAP2024xR1`
- source_url: https://docs.nomagic.com/spaces/CEAP2024xR1/pages/171180822/Hardware+Architecture
- version_number: 2
- version_date: `2024-07-16T08:18:42.354+02:00`
- ancestors: Magic Systems EE Architect
- labels: []

### NORMALIZED CONTENT

**On this page**

##### Modeling concepts

| Modeling Concepts supported | Details |
| --- | --- |
| Topology | Composition of the hardware devices and their interconnections |
| Electronic Control Unit |  |
| Hardware Port | Port typed by hardware interface |
| Hardware Interface | Typed with protocols CAN family, LIN, FlexRay, Ethernet, MOST and wired link. It can be used to ensure consistency of the hardware interfaces |
| High Performance Computer | Hierarchical definition of a High Performance Computer with its internal components. |
| Hypervisor | Part of the internal High Performance Computer definition |
| Runtime | A runtime defines a virtual execution environment |
| Container | A container defines an isolated virtual execution environment for applications |
| MicroController | Hardware part of HPC |
| MicroProcessor | Hardware part of HPC |
| Core | Hardware part of HPC |
| Sensor |  |
| Actuator |  |
| Electrical Device | Can be battery, fuse, relay |
| Device | Openness for any device |
| Communication Bus | Typed with protocols CAN family, LIN, FlexRay, MOST |
| Wired Link | Wire connection between hardware ports |
| Virtual Local Area Network | Definition of Virtual Local Area Network on Ethernet segment for Ethernet communication backbone |
| Ethernet Segment | Ethernet connection between hardware ports |
| Switch | Ethernet switch |

##### Hardware Architecture Project

A template is provided to initiate the modeling of a Hardware Architecture.

The project is structured as follows:

[IMAGE alt='' src='']

##### Hardware Architecture Key Features

The Hardware Architecture Project enables you, at the system level (vehicle) within a Topology to

- Author/edit hardware architectures combining components (Electronic Control Units, Sensors, Actuators, Electrical Devices, High Performance Computers, Communication Bus…)
- Specify Component Interfaces (protocols typed, or wired link) and link them
- Model High Performance Computer internal structure
- Define Ethernet backbone (VLAN, Ethernet segment, switch):
- Configure IP address
- Export the Topology partially or totally in an AUTOSAR format
- Display/Manipulate all the modeling concepts on multiple graphical views (network view, power distribution view)

##### Creating a Hardware Architecture in detail

You can create the Hardware Architecture in the Hardware Architecture package which is shared with the purpose to reuse it in another project (e.g. System Mapping project).

To create E/E Element

1. In the Containment tree, right-click the Hardware Architecture package.
2. From the shortcut menu, select Create E/E Architecture Elements and choose the needed one from the following:
  - Topology
  - Abstract Device
  - High Performance Computer
  - High Performance Computer Part
  - Communication Interface
  - Wired Interface
  - Communication Bus
  - Virtual Local Area Network

You can also create dedicated Hardware Block Definition and Internal Block diagrams. To learn more about how to create diagrams, see [CONFLUENCE_PAGE title='Creating diagrams' space='MD2024x'].

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p><strong>On this page</strong></p><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="959c2417-250e-4bc9-97dd-c13cad07516f" /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><h3>Modeling concepts</h3><table class="wrapped"><tbody class=""><tr class=""><th><p><strong>Modeling Concepts supported</strong></p></th><th><p><strong>Details</strong></p></th></tr><tr class=""><td><p>Topology</p></td><td><p>Composition of the hardware devices and their interconnections</p></td></tr><tr class=""><td><p>Electronic Control Unit</p></td><td><p><br /></p></td></tr><tr class=""><td><p>Hardware Port</p></td><td><p>Port typed by hardware interface</p></td></tr><tr class=""><td><p>Hardware Interface</p></td><td><p>Typed with protocols CAN family, LIN, FlexRay, Ethernet, MOST and wired link. It can be used to ensure consistency of the hardware interfaces</p></td></tr><tr class=""><td><p>High Performance Computer</p></td><td><p>Hierarchical definition of a High Performance Computer with its internal components.</p></td></tr><tr class=""><td><p>Hypervisor</p></td><td><p>Part of the internal High Performance Computer definition</p></td></tr><tr class=""><td><p>Runtime</p></td><td><p>A runtime defines a virtual execution environment</p></td></tr><tr class=""><td><p>Container</p></td><td><p>A container defines an isolated virtual execution environment for applications</p></td></tr><tr class=""><td><p>MicroController</p></td><td><p>Hardware part of HPC</p></td></tr><tr class=""><td><p>MicroProcessor</p></td><td><p>Hardware part of HPC</p></td></tr><tr class=""><td><p>Core</p></td><td><p>Hardware part of HPC</p></td></tr><tr class=""><td><p>Sensor</p></td><td><p><br /></p></td></tr><tr class=""><td><p>Actuator</p></td><td><p><br /></p></td></tr><tr class=""><td><p>Electrical Device</p></td><td><p>Can be battery, fuse, relay</p></td></tr><tr class=""><td><p>Device</p></td><td><p>Openness for any  device</p></td></tr><tr class=""><td><p>Communication Bus</p></td><td><p>Typed with protocols CAN family, LIN, FlexRay, MOST</p></td></tr><tr class=""><td><p>Wired Link</p></td><td><p>Wire connection between hardware ports</p></td></tr><tr class=""><td><p>Virtual Local Area Network</p></td><td><p>Definition of Virtual Local Area Network on Ethernet segment for Ethernet communication backbone</p></td></tr><tr class=""><td><p>Ethernet Segment</p></td><td><p>Ethernet connection between hardware ports</p></td></tr><tr class=""><td><p>Switch</p></td><td><p>Ethernet switch</p></td></tr></tbody></table><h3>Hardware Architecture Project</h3><p>A template is provided to initiate the modeling of a Hardware Architecture.</p><p>The project is structured as follows:</p><p><ac:image><ri:attachment ri:filename="hardvare_architecture.png" /></ac:image></p><h3>Hardware Architecture Key Features</h3><p>The Hardware Architecture Project enables you, at the system level (vehicle) within a Topology to</p><ul><li>Author/edit hardware architectures combining components (Electronic Control Units, Sensors, Actuators, Electrical Devices, High Performance Computers, Communication Bus…)</li><li>Specify Component Interfaces  (protocols typed, or wired link) and link them</li><li>Model High Performance Computer internal structure</li><li>Define Ethernet backbone (VLAN, Ethernet segment, switch):</li><ul><li>VLAN configuration (priority, Id)</li><li>VLAN service discovery configuration</li><li>VLAN allocation on Ethernet segment</li></ul><li>Configure IP address</li><li>Export the Topology partially or totally in an AUTOSAR format</li><li>Display/Manipulate all the modeling concepts on multiple graphical views (network view, power distribution view)</li></ul><h3>Creating a Hardware Architecture in detail</h3><p>You can create the Hardware Architecture in the Hardware Architecture package which is shared with the purpose to reuse it in another project (e.g. System Mapping project).</p><p><br /></p><p>To create E/E Element</p><hr /><ol><li>In the Containment tree, right-click the Hardware Architecture package.</li><li>From the shortcut menu, select <strong>Create E/E Architecture Elements</strong> and choose the needed one from the following:<ul><li>Topology</li><li>Abstract Device</li><li>High Performance Computer</li><li>High Performance Computer Part</li><li>Communication Interface</li><li>Wired Interface</li><li>Communication Bus</li><li>Virtual Local Area Network</li></ul></li></ol><p><br /></p><p>You can also create dedicated Hardware Block Definition and Internal Block diagrams.  To learn more about how to create diagrams, see <ac:link><ri:page ri:space-key="MD2024x" ri:content-title="Creating diagrams" /></ac:link>.</p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=171180814 space=CEAP2024xR1 version=2 -->
## PAGE 00004: Installation, licensing, and system requirements

- page_id: `171180814`
- space_key: `CEAP2024xR1`
- source_url: https://docs.nomagic.com/spaces/CEAP2024xR1/pages/171180814/Installation+licensing+and+system+requirements
- version_number: 2
- version_date: `2024-05-09T11:35:26.027+02:00`
- ancestors: Magic Systems EE Architect
- labels: []

### NORMALIZED CONTENT

**Software requirements**

To install and use the Magic Systems EE Architect plugin, the following plugins must be installed in your modeling tool:

- [CONFLUENCE_PAGE title='SysML Plugin Documentation' space='SYSMLP2024xR1']

For information regarding installation, licensing, and system requirements, visit the [CONFLUENCE_PAGE title='Installation, Licensing, and System Requirements Documentation' space='IL2024xR1'] page.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Software requirements</strong></p><p>To install and use the Magic Systems EE Architect plugin, the following plugins must be installed in your modeling tool:</p><ul><li><ac:link><ri:page ri:space-key="SYSMLP2024xR1" ri:content-title="SysML Plugin Documentation" /><ac:plain-text-link-body><![CDATA[SysML Plugin]]></ac:plain-text-link-body></ac:link></li></ul><p>For information regarding installation, licensing, and system requirements, visit the <ac:link><ri:page ri:space-key="IL2024xR1" ri:content-title="Installation, Licensing, and System Requirements Documentation" /><ac:plain-text-link-body><![CDATA[Installation, licensing, and system requirements]]></ac:plain-text-link-body></ac:link> page.</p>
````

<!--NOMAGIC_PAGE id=171180813 space=CEAP2024xR1 version=1 -->
## PAGE 00005: Magic Systems EE Architect

- page_id: `171180813`
- space_key: `CEAP2024xR1`
- source_url: https://docs.nomagic.com/spaces/CEAP2024xR1/pages/171180813/Magic+Systems+EE+Architect
- version_number: 1
- version_date: `2024-04-18T10:19:25.539+02:00`
- ancestors: 
- labels: []

### NORMALIZED CONTENT

#### WARNING: Technology Preview

Technology Preview

Please note that 2024x Refresh1 is a **technology preview** and should not be used in production environments. The production-ready version is planned for 2024x Refresh2.

##### Introduction

Electrical & Electronics Architecture activities make the bridge between the System Architecture activities (Concept phase) and the Discipline activities such as Electrical, Electronics, Software (Implementation phase).

EE architecture activities are performed at the level of the vehicle system, according to 4 independent scopes of responsibilities:

- Hardware architecture
- Software architecture
- Communication matrices
- and System mapping

This last activity involves making decisions and trade-offs to ensure consistency between hardware and software, taking communication into account.

As a result, EE engineers can deliver optimized architectural proposals to each engineering domain to implement the Hardware (electronics), the Software (Embedded SW), and Electrical (detailed schematics).

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="warning" ac:schema-version="1" ac:macro-id="84836ced-15ec-4455-b591-7c828334f4f2"><ac:parameter ac:name="title">Technology Preview</ac:parameter><ac:rich-text-body><p>Please note that 2024x Refresh1 is a <strong>technology preview</strong> and should not be used in production environments. The production-ready version is planned for 2024x Refresh2.</p></ac:rich-text-body></ac:structured-macro><h3><span style="letter-spacing: 0.0px;">Introduction</span></h3><p><span style="letter-spacing: 0.0px;">Electrical &amp; Electronics Architecture activities make the bridge between the System Architecture activities (Concept phase) and the Discipline activities such as Electrical, Electronics, Software (Implementation phase).</span></p><p>EE architecture activities are performed at the level of the vehicle system, according to 4 independent scopes of responsibilities: </p><ul><li>Hardware architecture </li><li>Software architecture </li><li>Communication matrices </li><li>and System mapping</li></ul><p>This last activity involves making decisions and trade-offs to ensure consistency between hardware and software, taking communication into account.<br /> </p><p>As a result, EE engineers can deliver optimized architectural proposals to each engineering domain to implement the Hardware (electronics), the Software (Embedded SW), and Electrical (detailed schematics).</p><p class="auto-cursor-target"><br /></p>
````

<!--NOMAGIC_PAGE id=171180824 space=CEAP2024xR1 version=2 -->
## PAGE 00006: Network Communication

- page_id: `171180824`
- space_key: `CEAP2024xR1`
- source_url: https://docs.nomagic.com/spaces/CEAP2024xR1/pages/171180824/Network+Communication
- version_number: 2
- version_date: `2024-07-16T08:34:56.970+02:00`
- ancestors: Magic Systems EE Architect
- labels: []

### NORMALIZED CONTENT

**On this page**

##### Modeling concepts

| Modeling Concept supported | Details |
| --- | --- |
| Communication matrix | Typed with protocols CAN family, LIN, FlexRay, Ethernet, MOST |
| Frame |  |
| Protocol Data Unit | Container for data to transmit |
| Bus signal | Bit start, Bit size, Endianness, Signed/Unsigned, Resolution, Offset, Min., Max., Multiplexer, Multiplexed, Multiplexer Value, Consumers, Initial Value |
| Bus Signal Group | Used to transmit hierarchical software data elements |
| System Signal | Used by the System Mapping to define an end-to-end communication in the topology. |
| System Signal Group | Used to transmit hierarchical software data elements |
| Signal Value | Capability to enumerate signal values |
| User Attribute Definition | Additional attributes defined on the matrix |
| User Attribute Value | Value of the user attributes |

##### Network Communication Project

A template is provided to initiate the modeling of Network Communication Matrices.

Project is structured as follow:

[IMAGE alt='' src='']

##### Network Communication Key Features

The Network Communication Project enables you to

- Author/edit communication matrices through tabular editor
- Define the matrix completely: frame, protocol data unit, bus signal, system signal
- Support the CAN family, LIN, FlexRay and Ethernet protocols
- Enable easy extensions for future new protocols
- Enable DBC file import

[IMAGE alt='' src='']

##### Creating Network Communication in detail

You can create communication matrices in the Matrices package which is shared with the purpose to reuse it in another project (e.g. System Mapping project).

To create communication matrix elements from the Matrices package

1. In the Containment tree, right-click the Matrices package.
2. From the shortcut menu, select Create E/E Architecture Elements and choose the needed one from the following:
  - Communication Matrix
  - System Signal
  - System Signal Group

To create communication matrix elements from the Communication Matrices element

1. In the Containment tree, right-click the Matrices package.
2. From the shortcut menu, select Create E/E Architecture Elements and choose the needed one from the following:
  - CAN Matrix
  - Ethernet Matrix
  - FlexRay Matrix
  - LIN Matrix

You can also create dedicated Communication Matrix. To learn more about how to create matrices, see [CONFLUENCE_PAGE title='Creating diagrams' space='MD2024x'].

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p><strong>On this page</strong></p><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="0ab0e05a-dcf8-42b0-993d-a1d0ddb654c5" /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><h3>Modeling concepts</h3><table class="wrapped"><tbody class=""><tr class=""><th><p><strong>Modeling Concept supported</strong></p></th><th><p><strong>Details</strong></p></th></tr><tr class=""><td><p>Communication matrix</p></td><td><p>Typed with protocols CAN family, LIN, FlexRay, Ethernet, MOST</p></td></tr><tr class=""><td><p>Frame</p></td><td><p><br /></p></td></tr><tr class=""><td><p>Protocol Data Unit</p></td><td><p>Container for data to transmit</p></td></tr><tr class=""><td><p>Bus signal</p></td><td><p>Bit start, Bit size, Endianness, Signed/Unsigned, Resolution, Offset, Min., Max., Multiplexer, Multiplexed, Multiplexer Value, Consumers, Initial Value</p></td></tr><tr class=""><td><p>Bus Signal Group</p></td><td><p>Used to transmit hierarchical software data elements</p></td></tr><tr class=""><td><p>System Signal</p></td><td><p>Used by the System Mapping to define an end-to-end communication in the topology.</p></td></tr><tr class=""><td><p>System Signal Group</p></td><td><p>Used to transmit hierarchical software data elements</p></td></tr><tr class=""><td><p>Signal Value</p></td><td><p>Capability to enumerate signal values</p></td></tr><tr class=""><td><p>User Attribute Definition</p></td><td><p>Additional attributes defined on the matrix</p></td></tr><tr class=""><td><p>User Attribute Value</p></td><td><p>Value of the user attributes</p></td></tr></tbody></table><h3>Network Communication Project</h3><p>A template is provided to initiate the modeling of Network Communication Matrices.</p><p>Project is structured as follow:</p><p><ac:image><ri:attachment ri:filename="network_communication.png" /></ac:image></p><h3>Network Communication Key Features</h3><p>The Network Communication Project enables you to</p><ul><li>Author/edit communication matrices through tabular editor</li><li>Define the matrix completely: frame, protocol data unit, bus signal, system signal</li><li>Support the CAN family, LIN, FlexRay and Ethernet protocols</li><li>Enable easy extensions for future new protocols</li><li>Enable DBC file import</li></ul><p><ac:image ac:height="400"><ri:attachment ri:filename="communication_matrix.png" /></ac:image></p><h3>Creating Network Communication in detail</h3><p><span style="letter-spacing: 0.0px;">You can create communication matrices in the Matrices package which is shared with the purpose to reuse it in another project (e.g. System Mapping project).</span></p><p><br /></p><p>To create communication matrix elements from the Matrices package</p><hr /><ol><li>In the Containment tree, right-click the Matrices package.</li><li>From the shortcut menu, select <strong>Create E/E Architecture Elements</strong> and choose the needed one from the following:<ul><li>Communication Matrix</li><li>System Signal</li><li>System Signal Group</li></ul></li></ol><p><br /></p><p>To create communication matrix elements from the <span style="letter-spacing: 0.0px;">Communication Matrices element</span></p><hr /><ol><li>In the Containment tree, right-click the Matrices package.</li><li>From the shortcut menu, select <strong>Create E/E Architecture Elements</strong> and choose the needed one from the following:<ul><li>CAN Matrix</li><li>Ethernet Matrix</li><li>FlexRay Matrix</li><li>LIN Matrix</li></ul></li></ol><p>You can also create dedicated Communication Matrix.  To learn more about how to create matrices, see <ac:link><ri:page ri:space-key="MD2024x" ri:content-title="Creating diagrams" /></ac:link>.</p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=171180817 space=CEAP2024xR1 version=1 -->
## PAGE 00007: Project Templates

- page_id: `171180817`
- space_key: `CEAP2024xR1`
- source_url: https://docs.nomagic.com/spaces/CEAP2024xR1/pages/171180817/Project+Templates
- version_number: 1
- version_date: `2024-03-13T15:47:30.030+01:00`
- ancestors: Magic Systems EE Architect
- labels: []

### NORMALIZED CONTENT

You can use the following pre-defined templates to create projects:

- Hardware Architecture Project : select this template for modeling a hardware topology.
- Software Architecture Project : select this template for modeling signal-based and service-oriented software architectures.
- Network Communication Project : select this template for modeling signals and communication matrices that define bus exchange.
- System Mapping Project: select this template for allocating software architecture on hardware architecture taking into account communication definition.

[IMAGE alt='' src='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>You can use the following pre-defined templates to create projects:</p><ul><li><strong>Hardware Architecture Project</strong>: select this template for modeling a hardware topology.</li><li><strong>Software Architecture Project</strong>: select this template for modeling signal-based and service-oriented software architectures.</li><li><strong>Network Communication Project</strong>: select this template for modeling signals and communication matrices that define bus exchange.</li><li><strong>System Mapping Project:</strong> select this template for allocating software architecture on hardware architecture taking into account communication definition.</li></ul><p><ac:image><ri:attachment ri:filename="templates.png"><ri:page ri:space-key="CEAP2024xR1" ri:content-title="Project Templates" /></ri:attachment></ac:image></p>
````

<!--NOMAGIC_PAGE id=171180819 space=CEAP2024xR1 version=1 -->
## PAGE 00008: Software Architecture

- page_id: `171180819`
- space_key: `CEAP2024xR1`
- source_url: https://docs.nomagic.com/spaces/CEAP2024xR1/pages/171180819/Software+Architecture
- version_number: 1
- version_date: `2024-03-14T14:21:47.594+01:00`
- ancestors: Magic Systems EE Architect
- labels: []

### NORMALIZED CONTENT

**On this page**

Modeling concepts

Below are the modeling concepts for the Software Functional level:

| Modeling Concepts supported | Details |
| --- | --- |
| Software Function | Software Function that can be hierarchical. |
| Software Functional Port | Port typed by a software functional Flow. |
| Software Functional Flow | Software port interface defining flow properties. |

Below are the modeling concepts for the Software Component level:

| Modeling Concepts supported | Details |
| --- | --- |
| Software Component | Software component that can be hierarchical or atomic. |
| Software Port | Port typed by a software interface. |
| Sender/Receiver Interface | Software port interface defining data elements. |
| Software data type support | Supported by UML. |
| Client/Server Interface | Software port interface defining operations. |
| Service interface | Software port interface defining fields, events, operations. |
| SOME/IP Service Interface | Refinement of Service interface for SOME/IP deployment. It defines SOME/IP Fields, SOME/IP Events, SOME/IP Operations. |

##### Software Architecture Project

A project template is provided to initiate the modeling of a Software Architecture.

The project is structured as follows:

[IMAGE alt='' src='']

##### Software Architecture Key Features

The Software Architecture Project enables you, at the system level (vehicle) to

- Author/edit software architectures combining Software components
- Use interfaces either in a signal-based approach or Service Oriented approach, or a mix of approach
- Work with Multiple graphical views

[IMAGE alt='' src='']

##### Creating a Software Architecture in Detail

You can create the Software Architecture in the Software Architecture package which is shared with the purpose to reuse it in another project (e.g. System Mapping project).

To create E/E Element

1. In the Containment tree, right-click the Software Architecture package.
2. From the shortcut menu, select Create E/E Architecture Elements and choose the needed one from the following:
  - Software Atomic Component
  - Software Composition
  - Software Function
  - Abstract Software Interface

You can also create dedicated Software Block Definition and Internal Block diagrams. To learn more about how to create diagrams, see [CONFLUENCE_PAGE title='Creating diagrams' space='MD2024x'].

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p><strong>On this page</strong></p><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="1b9e65ef-5cde-4164-980a-8f1f897516bd" /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><span style="font-size: 16.0px;font-weight: bold;letter-spacing: -0.006em;">Modeling concepts</span><p>Below are the modeling concepts for the Software Functional level:</p><table><tbody class=""><tr class=""><th><p><strong>Modeling Concepts supported</strong></p></th><th><p><strong>Details</strong></p></th></tr><tr class=""><td><p>Software Function</p></td><td><p>Software Function that can be hierarchical.</p></td></tr><tr class=""><td><p>Software Functional Port</p></td><td><p>Port typed by a software functional Flow.</p></td></tr><tr class=""><td><p>Software Functional Flow</p></td><td><p>Software port interface defining flow properties.</p></td></tr></tbody></table><p>Below are the modeling concepts for the Software Component level:</p><table><tbody class=""><tr class=""><th><p><strong>Modeling Concepts supported</strong></p></th><th><p><strong>Details</strong></p></th></tr><tr class=""><td><p>Software Component</p></td><td><p>Software component that can be hierarchical or atomic.</p></td></tr><tr class=""><td><p>Software Port</p></td><td><p>Port typed by a software interface.</p></td></tr><tr class=""><td><p>Sender/Receiver Interface</p></td><td><p>Software port interface defining data elements.</p></td></tr><tr class=""><td><p>Software data type support</p></td><td><p>Supported by UML.</p></td></tr><tr class=""><td><p>Client/Server Interface</p></td><td><p>Software port interface defining operations.</p></td></tr><tr class=""><td><p>Service interface</p></td><td><p>Software port interface defining fields, events, operations.</p></td></tr><tr class=""><td><p>SOME/IP Service Interface</p></td><td><p>Refinement of Service interface for SOME/IP deployment. It defines SOME/IP Fields, SOME/IP Events, SOME/IP Operations.</p></td></tr></tbody></table><h3>Software Architecture Project</h3><p>A project template is provided to initiate the modeling of a Software Architecture.</p><p>The project is structured as follows:</p><p><ac:image><ri:attachment ri:filename="project_structure.png"><ri:page ri:space-key="CEAP2024xR1" ri:content-title="Software Architecture" /></ri:attachment></ac:image></p><h3>Software Architecture Key Features</h3><p>The Software Architecture Project enables you, at the system level (vehicle) to</p><ul><li>Author/edit software architectures combining Software components</li><li>Use interfaces either in a signal-based approach or Service Oriented approach, or a mix of approach</li><li>Work with Multiple graphical views </li></ul><p><ac:image ac:height="400"><ri:attachment ri:filename="key_features_SOA.png"><ri:page ri:space-key="CEAP2024xR1" ri:content-title="Software Architecture" /></ri:attachment></ac:image></p><p><br /></p><h3>Creating a Software Architecture in Detail</h3><p>You can create the Software Architecture in the Software Architecture package which is shared with the purpose to reuse it in another project (e.g. System Mapping project).</p><p>To create E/E Element</p><hr /><ol><li>In the Containment tree, right-click the Software Architecture package.</li><li>From the shortcut menu, select <strong>Create E/E Architecture Elements</strong> and choose the needed one from the following:<ul><li>Software Atomic Component</li><li>Software Composition</li><li>Software Function</li><li>Abstract Software Interface</li></ul></li></ol><p><br /></p><p>You can also create dedicated Software Block Definition and Internal Block diagrams.  To learn more about how to create diagrams, see <ac:link><ri:page ri:space-key="MD2024x" ri:content-title="Creating diagrams" /></ac:link>.</p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=171180827 space=CEAP2024xR1 version=1 -->
## PAGE 00009: System Mapping

- page_id: `171180827`
- space_key: `CEAP2024xR1`
- source_url: https://docs.nomagic.com/spaces/CEAP2024xR1/pages/171180827/System+Mapping
- version_number: 1
- version_date: `2024-03-14T08:37:12.853+01:00`
- ancestors: Magic Systems EE Architect
- labels: []

### NORMALIZED CONTENT

##### Modeling concepts

Allocations rely on SysML allocation links.

##### System Mapping Project

A template is provided to initiate modeling a System Mapping for a given Hardware Architecture, Software Architecture, and Communication Matrices.

The project is structured as follows:

[IMAGE alt='' src='']

##### System Mapping Key Features

The System Mapping Project allows you to make the **consistent synthesis** of the 3 architectures (used projects) through different allocations: Software-to-Hardware, and Software-to-Communication at the system level (vehicle). The outcomes are Interface Control Documents or Service Deployment Manifests.

The key features are:

- Allocate Software components on Hardware
- Allocate Signal-based data exchange on Hardware
- Allocate Service Interface:
- Generate reports of Interface Control Document
- Generate reports of Service Deployment Manifest
- Dedicated diagrams, allocation matrix tables, and tabular views

[IMAGE alt='' src='']

##### Performing System Mappings in detail

Before proceeding with the allocation of software components to the hardware components, it is necessary to initialize the System Mapping project.

The first step is to reference as used projects the following architectures:

- Software Architecture
- Hardware Architecture
- Communication Matrices

The second step involves initializing the System Mapping package with both hardware architecture and software architecture onto which allocations will be performed.

To initialize a System Mapping

1. In the Containment tree, right-click the System Mapping package.
2. In the shortcut menu, click E/E Architecture Tools > Initialize Systems Mapping .
3. Specify **Software Composition/Function** and **Topology**. The top-level components for Hardware Architecture and Software Architecture must be selected.
4. Click OK .

[IMAGE alt='' src='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<h3>Modeling concepts</h3><p>Allocations rely on SysML allocation links.</p><h3>System Mapping Project</h3><p>A template is provided to initiate modeling a System Mapping for a given Hardware Architecture, Software Architecture, and Communication Matrices.</p><p>The project is structured as follows:</p><p><ac:image><ri:attachment ri:filename="system_mapping.png"><ri:page ri:space-key="CEAP2024xR1" ri:content-title="System Mapping" /></ri:attachment></ac:image></p><h3>System Mapping Key Features</h3><p>The System Mapping Project allows you to make the <strong>consistent synthesis</strong> of the 3 architectures (used projects) through different allocations: Software-to-Hardware, and Software-to-Communication at the system level (vehicle). The outcomes are Interface Control Documents or Service Deployment Manifests.</p><p>The key features are:</p><ul><li>Allocate Software components on Hardware</li><li>Allocate Signal-based data exchange on Hardware</li><li>Allocate Service Interface:</li><ul><li>On Hardware Port and middleware (SOME/IP) configuration</li><li>On VLAN</li></ul><li>Generate reports of Interface Control Document</li><li>Generate reports of Service Deployment Manifest</li><li>Dedicated diagrams, allocation matrix tables, and tabular views</li></ul><p><ac:image><ri:attachment ri:filename="1.jpg"><ri:page ri:space-key="CEAP2024xR1" ri:content-title="System Mapping" /></ri:attachment></ac:image></p><h3>Performing System Mappings in detail</h3><p>Before proceeding with the allocation of software components to the hardware components, it is necessary to initialize the System Mapping project.</p><p>The first step is to reference as used projects the following architectures:</p><ul><li>Software Architecture</li><li>Hardware Architecture</li><li>Communication Matrices</li></ul><p>The second step involves initializing the System Mapping package with both hardware architecture and software architecture onto which allocations will be performed.</p><p><br /></p><p>To initialize a System Mapping</p><hr /><ol><li>In the Containment tree, right-click the System Mapping package.</li><li>In the shortcut menu, click <strong>E/E Architecture Tools</strong> &gt; <strong>Initialize Systems Mapping</strong>.</li><li><p class="auto-cursor-target">Specify <strong>Software Composition/Function</strong> and <strong>Topology</strong>.</p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="ee018ac3-b8d4-45a6-8f7a-3bc6f9d689bb"><ac:rich-text-body><p>The top-level components for Hardware Architecture and Software Architecture must be selected.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></li><li>Click <strong>OK</strong>.</li></ol><p><ac:image><ri:attachment ri:filename="system_mapping_initialization.png"><ri:page ri:space-key="CEAP2024xR1" ri:content-title="System Mapping" /></ri:attachment></ac:image></p>
````
