# NOMAGIC DOCUMENTATION SPACE: Developer Guides

<!--NOMAGIC_SPACE key=DEVG chunk=5 -->

<!--NOMAGIC_PAGE id=309365437 space=DEVG version=12 -->
## PAGE 00809: Working with Compartments

- page_id: `309365437`
- space_key: `DEVG`
- source_url: https://docs.nomagic.com/spaces/DEVG/pages/309365437/Working+with+Compartments
- version_number: 12
- version_date: `2026-06-04T20:24:02.672+02:00`
- ancestors: Developer Guides Home > Modeling Tools Developer Guide > SysML v2 > Working With Model > Managing Presentation Elements
- labels: []

### NORMALIZED CONTENT

#### Overview

The [**CompartmentManager**](https://jdocs.nomagic.com/2026xRefresh2/com/dassault_systemes/modeler/sysml/diagram/compartments/CompartmentManager.html)class provides utility methods for controlling the visibility of elements displayed inside symbol compartments in diagrams.

Compartments are presentation-level areas of a symbol that display related model information, such as attributes, ports, values, parts, constraints, requirements, or other owned / related elements. The [**CompartmentManager**](https://jdocs.nomagic.com/2026xRefresh2/com/dassault_systemes/modeler/sysml/diagram/compartments/CompartmentManager.html)does not create or delete model elements. It controls whether existing model elements are shown or hidden in a diagram presentation.

Use this API when you need to programmatically:

- Show selected elements in a symbol compartment.
- Hide selected elements from a symbol compartment.
- Show or hide multiple compartment entries at once.
- Manage payload visibility on connector paths.

#### When to Use CompartmentManager

Use [**CompartmentManager**](https://jdocs.nomagic.com/2026xRefresh2/com/dassault_systemes/modeler/sysml/diagram/compartments/CompartmentManager.html)when the model element already exists, but the diagram must display or suppress that element inside a specific compartment.

Typical examples include:

- Showing selected part usages in a SysML v2 part definition symbol.
- Hiding inherited, derived, or generated values from a compartment.

#### Important Concepts

##### Compartment ID

A[**compartment ID**](https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/sysml/diagram/compartments/descriptors/CompartmentDescriptorID.html)[https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/sysml/diagram/compartments/descriptors/CompartmentDescriptorID.html](https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/sysml/diagram/compartments/descriptors/CompartmentDescriptorID.html)identifies the compartment that contains the displayed entries. Use constants provided by the platform where available, such as **CompartmentID** values, instead of hard-coded strings.

##### Element

An[**Element**](https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/kerml/model/kerml/Element.html)[https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/kerml/model/kerml/Element.html](https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/kerml/model/kerml/Element.html)is the model element that should be shown or hidden inside the compartment.

##### Connector Path

A[**ConnectorPath**](https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/kerml/diagram/ConnectorPath.html)[https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/kerml/diagram/ConnectorPath.html](https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/kerml/diagram/ConnectorPath.html)is the presentation element for a connector or relationship path on a diagram. Payload-related methods operate on connector-path presentation data.

#### Method Details

##### showCompartmentElement

Displays a single model element inside a specified compartment of a presentation element.

Use this method when one specific SysML v2 model element should become visible in a diagram symbol compartment.

```java
;
Element element = ...;

Editing.getInstance(project).execute("compartment operation", ()-> CompartmentManager.showCompartmentElement(presentationElement, compartmentId, element));
]]>
```

##### showCompartmentElements

Displays multiple model elements inside a specified compartment of a presentation element.

Use this method when applying display rules to a group of elements, such as showing all selected ports, features, requirements, or value properties.

```java
;
Collection elements = ...;

Editing.getInstance(project).execute("compartment operation", ()-> CompartmentManager.showCompartmentElements(presentationElement, compartmentId, elements));
]]>
```

##### hideCompartmentElement

Hides a single model element from a specified compartment of a presentation element.

Use this method when only one compartment entry should be suppressed from the diagram view.

```java
;
Element element = ...;

Editing.getInstance(project).execute("compartment operation", ()-> CompartmentManager.hideCompartmentElement(presentationElement, compartmentId, element));
]]>
```

##### hideCompartmentElements

Hides multiple model elements from a specified compartment of a presentation element.

Use this method when simplifying a symbol by hiding a group of compartment entries.

```java
;
Collection elements = ...;

Editing.getInstance(project).execute("compartment operation", ()-> CompartmentManager.hideCompartmentElements(presentationElement, compartmentId, elements));
]]>
```

#### Showing or Hiding an Entire Compartment

In addition to showing or hiding individual elements inside a compartment, SysML v2 diagram compartments can also be shown or hidden as a complete compartment area. This is done by changing the compartment style applied to the target **[PresentationElement](https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/magicdraw/uml/symbols/PresentationElement.html)**. The[PresentationElementsManager](https://jdocs.nomagic.com/2026xRefresh2/com/dassault_systemes/modeler/sysml/diagram/PresentationElementsManager.html)[https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/sysml/diagram/PresentationElementsManager.html](https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/sysml/diagram/PresentationElementsManager.html)provides the **changeStyle** method, which allows updating a specific **CompartmentStyle**. To show the compartment, set **showCompartment** to **true**. To hide the entire compartment, set **showCompartment** to **false**.

```java
compartmentStyleClass = ...;

// Show the entire compartment.
manager.changeStyle(
    presentationElement,
    compartmentStyleClass,
    style -> style.setShowCompartment(true)
);

// Hide the entire compartment.
manager.changeStyle(
    presentationElement,
    compartmentStyleClass,
    style -> style.setShowCompartment(false)
);
]]>
```

#### NOTE: Usage Note

Usage Note

Use **CompartmentManager** when you need to show or hide specific elements inside a compartment. Use **PresentationElementsManager.changeStyle** with **CompartmentStyle** when you need to show or hide the entire compartment itself.

#### Showing or hiding Payloads on ConnectorPath

The payload displayed on a**`[ConnectorPath](https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/kerml/diagram/ConnectorPath.html)`**is stored in the [payload feature](https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/kerml/model/kerml/PayloadFeature.html) of the underlying [flow usage](https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/sysml/model/sysml/FlowUsage.html). Hiding or showing the payload changes only the symbol presentation; it does not remove or modify the payload feature in the semantic model.

To hide or show the payload item on the connector path, the corresponding payload feature must be found from the underlying flow usage

```java
;
List itemDefinitions =...
Collection payloadFeatures = Payloads.getPayloadFeaturesOfTypes((Type) presentationElement.getModelElement(), itemDefinitions);

Editing.getInstance(project).execute("compartment operation", () -> CompartmentManager.hideCompartmentElements(presentationElement, compartmentId, payloadFeatures));

]]>
```

#### Best Practices

- Use compartment ID constants where available.
- Do not hard-code compartment IDs unless no constant exists.
- Always perform diagram presentation changes inside a session.
- Validate that the presentation element belongs to an active, loaded project.
- Check that the element belongs to the model context represented by the symbol.
- Use bulk methods when showing or hiding multiple elements.
- Keep diagram visibility logic separate from model-creation logic.
- Do not use this API to create or delete SysML v2 elements.
- Refresh or repaint the diagram after large visibility updates if required by your plugin workflow.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<h2>Overview</h2><p>The <a href="https://jdocs.nomagic.com/2026xRefresh2/com/dassault_systemes/modeler/sysml/diagram/compartments/CompartmentManager.html"><strong>CompartmentManager</strong> </a>class provides utility methods for controlling the visibility of elements displayed inside symbol compartments in diagrams.</p><p>Compartments are presentation-level areas of a symbol that display related model information, such as attributes, ports, values, parts, constraints, requirements, or other owned / related elements. The <a href="https://jdocs.nomagic.com/2026xRefresh2/com/dassault_systemes/modeler/sysml/diagram/compartments/CompartmentManager.html"><strong>CompartmentManager</strong> </a>does not create or delete model elements. It controls whether existing model elements are shown or hidden in a diagram presentation.</p><p>Use this API when you need to programmatically:</p><ul><li>Show selected elements in a symbol compartment.</li><li>Hide selected elements from a symbol compartment.</li><li>Show or hide multiple compartment entries at once.</li><li data-uuid="b5ea8474-3fbb-4a97-85f8-8aa2a9099b7c">Manage payload visibility on connector paths.</li></ul><h2>When to Use CompartmentManager</h2><p>Use <a href="https://jdocs.nomagic.com/2026xRefresh2/com/dassault_systemes/modeler/sysml/diagram/compartments/CompartmentManager.html"><strong>CompartmentManager</strong> </a>when the model element already exists, but the diagram must display or suppress that element inside a specific compartment.</p><p>Typical examples include:</p><ul><li>Showing selected part usages in a SysML v2 part definition symbol.</li><li>Hiding inherited, derived, or generated values from a compartment.</li></ul><h2>Important Concepts</h2><h3>Compartment ID</h3><p><span style="letter-spacing: 0.0px;">A</span><a style="letter-spacing: 0.0px;" href="https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/sysml/diagram/compartments/descriptors/CompartmentDescriptorID.html"><strong> compartment ID</strong></a><a href="https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/sysml/diagram/compartments/descriptors/CompartmentDescriptorID.html"> </a>identifies the compartment that contains the displayed entries. Use constants provided by the platform where available, such as <strong>CompartmentID</strong> values, instead of hard-coded strings.</p><h3>Element</h3><p><span style="letter-spacing: 0.0px;">An</span><a style="letter-spacing: 0.0px;" href="https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/kerml/model/kerml/Element.html"><strong> Element</strong></a><a href="https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/kerml/model/kerml/Element.html"> </a>is the model element that should be shown or hidden inside the compartment.</p><h3 style="text-align: left;">Connector Path</h3><p style="text-align: left;"><span>A</span><a class="external-link" href="https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/kerml/diagram/ConnectorPath.html"><strong><span> </span>ConnectorPath</strong></a><a class="external-link" href="https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/kerml/diagram/ConnectorPath.html"> </a>is the presentation element for a connector or relationship path on a diagram. Payload-related methods operate on connector-path presentation data.</p><h2>Method Details</h2><h3>showCompartmentElement</h3><p>Displays a single model element inside a specified compartment of a presentation element.</p><p>Use this method when one specific SysML v2 model element should become visible in a diagram symbol compartment.</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="e9668b6b-4bd6-4303-a25d-48b3b095f86e"><ac:parameter ac:name="language">java</ac:parameter><ac:plain-text-body><![CDATA[import com.dassault_systemes.modeler.foundation.editing.Editing;
import com.dassault_systemes.modeler.kerml.diagram.ConnectorPath;
import com.dassault_systemes.modeler.kerml.model.kerml.Element;
import com.dassault_systemes.modeler.sysml.diagram.compartments.CompartmentManager;
import com.dassault_systemes.modeler.sysml.diagram.compartments.descriptors.CompartmentDescriptorID;
import com.nomagic.magicdraw.core.Application;
import com.nomagic.magicdraw.core.Project;
import com.nomagic.magicdraw.uml.symbols.PresentationElement;

Project project = Application.getInstance().getProject();

PresentationElement presentationElement = ...;
String compartmentId = CompartmentDescriptorID.<....>;
Element element = ...;

Editing.getInstance(project).execute("compartment operation", ()-> CompartmentManager.showCompartmentElement(presentationElement, compartmentId, element));
]]></ac:plain-text-body></ac:structured-macro><h3>showCompartmentElements</h3><p>Displays multiple model elements inside a specified compartment of a presentation element.</p><p>Use this method when applying display rules to a group of elements, such as showing all selected ports, features, requirements, or value properties.</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="4c2b5e64-840f-436f-a768-2f4d3fde6b6c"><ac:parameter ac:name="language">java</ac:parameter><ac:plain-text-body><![CDATA[import com.dassault_systemes.modeler.foundation.editing.Editing;
import com.dassault_systemes.modeler.kerml.diagram.ConnectorPath;
import com.dassault_systemes.modeler.kerml.model.kerml.Element;
import com.dassault_systemes.modeler.sysml.diagram.compartments.CompartmentManager;
import com.dassault_systemes.modeler.sysml.diagram.compartments.descriptors.CompartmentDescriptorID;
import com.nomagic.magicdraw.core.Application;
import com.nomagic.magicdraw.core.Project;
import com.nomagic.magicdraw.uml.symbols.PresentationElement;

import java.util.Collection;

Project project = Application.getInstance().getProject();

PresentationElement presentationElement = ...;
String compartmentId = CompartmentDescriptorID.<....>;
Collection<Element> elements = ...;

Editing.getInstance(project).execute("compartment operation", ()-> CompartmentManager.showCompartmentElements(presentationElement, compartmentId, elements));
]]></ac:plain-text-body></ac:structured-macro><h3>hideCompartmentElement</h3><p>Hides a single model element from a specified compartment of a presentation element.</p><p>Use this method when only one compartment entry should be suppressed from the diagram view.</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="6e547fc3-6c41-460b-8054-3aaf14fd3092"><ac:parameter ac:name="language">java</ac:parameter><ac:plain-text-body><![CDATA[import com.dassault_systemes.modeler.foundation.editing.Editing;
import com.dassault_systemes.modeler.kerml.diagram.ConnectorPath;
import com.dassault_systemes.modeler.kerml.model.kerml.Element;
import com.dassault_systemes.modeler.sysml.diagram.compartments.CompartmentManager;
import com.dassault_systemes.modeler.sysml.diagram.compartments.descriptors.CompartmentDescriptorID;
import com.nomagic.magicdraw.core.Application;
import com.nomagic.magicdraw.core.Project;
import com.nomagic.magicdraw.uml.symbols.PresentationElement;

Project project = Application.getInstance().getProject();

PresentationElement presentationElement = ...;
String compartmentId = CompartmentDescriptorID.<....>;
Element element = ...;

Editing.getInstance(project).execute("compartment operation", ()-> CompartmentManager.hideCompartmentElement(presentationElement, compartmentId, element));
]]></ac:plain-text-body></ac:structured-macro><h3>hideCompartmentElements</h3><p>Hides multiple model elements from a specified compartment of a presentation element.</p><p>Use this method when simplifying a symbol by hiding a group of compartment entries.</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="6a9285e1-4968-4f72-9953-4797dde4542e"><ac:parameter ac:name="language">java</ac:parameter><ac:plain-text-body><![CDATA[import com.dassault_systemes.modeler.foundation.editing.Editing;
import com.dassault_systemes.modeler.kerml.model.kerml.Element;
import com.dassault_systemes.modeler.sysml.diagram.compartments.CompartmentManager;
import com.dassault_systemes.modeler.sysml.diagram.compartments.descriptors.CompartmentDescriptorID;
import com.nomagic.magicdraw.core.Application;
import com.nomagic.magicdraw.core.Project;
import com.nomagic.magicdraw.uml.symbols.PresentationElement;

import java.util.Collection;

Project project = Application.getInstance().getProject();

PresentationElement presentationElement = ...;
String compartmentId = CompartmentDescriptorID.<....>;
Collection<Element> elements = ...;

Editing.getInstance(project).execute("compartment operation", ()-> CompartmentManager.hideCompartmentElements(presentationElement, compartmentId, elements));
]]></ac:plain-text-body></ac:structured-macro><h2>Showing or Hiding an Entire Compartment</h2><p>In addition to showing or hiding individual elements inside a compartment, SysML v2 diagram compartments can also be shown or hidden as a complete compartment area. This is done by changing the compartment style applied to the target <strong><a href="https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/magicdraw/uml/symbols/PresentationElement.html">PresentationElement</a></strong>. <span>The<a href="https://jdocs.nomagic.com/2026xRefresh2/com/dassault_systemes/modeler/sysml/diagram/PresentationElementsManager.html"> PresentationElementsManager</a></span><a href="https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/sysml/diagram/PresentationElementsManager.html"> </a>provides the <strong>changeStyle</strong> method, which allows updating a specific <strong>CompartmentStyle</strong>. To show the compartment, set <strong>showCompartment</strong> to <strong>true</strong>. To hide the entire compartment, set <strong>showCompartment</strong> to <strong>false</strong>. </p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="c6d270d8-5607-409d-b81c-ec49bd12e7fc"><ac:parameter ac:name="language">java</ac:parameter><ac:plain-text-body><![CDATA[import com.dassault_systemes.modeler.kerml.view.style.kermlstyles.CompartmentStyle;
import com.dassault_systemes.modeler.sysml.diagram.PresentationElementsManager;
import com.nomagic.magicdraw.core.Project;
import com.nomagic.magicdraw.uml.symbols.PresentationElement;

PresentationElement presentationElement = ...;

PresentationElementsManager manager = PresentationElementsManager.getInstance();
Class<? extends CompartmentStyle> compartmentStyleClass = ...;

// Show the entire compartment.
manager.changeStyle(
    presentationElement,
    compartmentStyleClass,
    style -> style.setShowCompartment(true)
);

// Hide the entire compartment.
manager.changeStyle(
    presentationElement,
    compartmentStyleClass,
    style -> style.setShowCompartment(false)
);
]]></ac:plain-text-body></ac:structured-macro><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="37cd7790-0a4f-495d-9ef7-fdc5affb70b5"><ac:parameter ac:name="title">Usage Note</ac:parameter><ac:rich-text-body><p>Use <strong>CompartmentManager</strong> when you need to show or hide specific elements inside a compartment. Use <strong>PresentationElementsManager.changeStyle</strong> with <strong>CompartmentStyle</strong> when you need to show or hide the entire compartment itself.</p></ac:rich-text-body></ac:structured-macro><h2>Showing or hiding Payloads on ConnectorPath</h2><p class="isSelectedEnd"><span>The payload displayed on a </span><strong><code><a href="https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/kerml/diagram/ConnectorPath.html">ConnectorPath</a></code></strong><span> is stored in the <a href="https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/kerml/model/kerml/PayloadFeature.html">payload feature</a> of the underlying <a href="https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/sysml/model/sysml/FlowUsage.html">flow usage</a>. Hiding or showing the payload changes only the symbol presentation; it does not remove or modify the payload feature in the semantic model.</span></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="3e10c375-ef78-45d0-833e-b50a4ebf1120"><ac:rich-text-body><p><span>To hide or show the payload item on the connector path, the corresponding payload feature must be found from the underlying flow usage</span></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="45bc08d1-d955-492a-a732-dcadd22d23e3"><ac:parameter ac:name="language">java</ac:parameter><ac:plain-text-body><![CDATA[import com.dassault_systemes.modeler.foundation.editing.Editing;
import com.dassault_systemes.modeler.kerml.model.Payloads;
import com.dassault_systemes.modeler.kerml.model.kerml.Element;
import com.dassault_systemes.modeler.kerml.model.kerml.Type;
import com.dassault_systemes.modeler.sysml.diagram.compartments.CompartmentManager;
import com.dassault_systemes.modeler.sysml.diagram.compartments.descriptors.CompartmentDescriptorID;
import com.dassault_systemes.modeler.sysml.model.sysml.ItemDefinition;
import com.nomagic.magicdraw.core.Application;
import com.nomagic.magicdraw.core.Project;
import com.nomagic.magicdraw.uml.symbols.PresentationElement;

import java.util.Collection;
import java.util.List;

Project project = Application.getInstance().getProject();

PresentationElement presentationElement = ...;
String compartmentId = CompartmentDescriptorID.<....>;
List<ItemDefinition> itemDefinitions =...
Collection<Element> payloadFeatures = Payloads.getPayloadFeaturesOfTypes((Type) presentationElement.getModelElement(), itemDefinitions);

Editing.getInstance(project).execute("compartment operation", () -> CompartmentManager.hideCompartmentElements(presentationElement, compartmentId, payloadFeatures));

]]></ac:plain-text-body></ac:structured-macro><h2>Best Practices</h2><ul><li>Use <a href="https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/sysml/diagram/compartments/descriptors/CompartmentDescriptorID.html">compartment ID</a> constants where available.</li><li>Do not hard-code <a href="https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/sysml/diagram/compartments/descriptors/CompartmentDescriptorID.html">compartment IDs</a> unless no constant exists.</li><li>Always perform diagram presentation changes inside a session.</li><li>Validate that the presentation element belongs to an active, loaded project.</li><li>Check that the element belongs to the model context represented by the symbol.</li><li>Use bulk methods when showing or hiding multiple elements.</li><li>Keep diagram visibility logic separate from model-creation logic.</li><li>Do not use this API to create or delete SysML v2 elements.</li><li>Refresh or repaint the diagram after large visibility updates if required by your plugin workflow.</li></ul>
````

<!--NOMAGIC_PAGE id=249573514 space=DEVG version=2 -->
## PAGE 00810: Working with Dependency Matrix

- page_id: `249573514`
- space_key: `DEVG`
- source_url: https://docs.nomagic.com/spaces/DEVG/pages/249573514/Working+with+Dependency+Matrix
- version_number: 2
- version_date: `2025-09-12T15:43:38.874+02:00`
- ancestors: Developer Guides Home > Modeling Tools Developer Guide > UML-based > Working with diagrams
- labels: []

### NORMALIZED CONTENT

[CONFLUENCE_PAGE title='Dependency Matrix' space='MT'] is a special type of diagram, that is, a diagram with a specific stereotype applied. Our modeling tools provide an API to:

- Create custom types of the Dependency Matrix.
- Customize a Dependency Matrix as follows:
  - Configure the command bar, shortcut menus of the row or column header element, cell, and filter panel.
  - Assign shortcut keys for commands.
  - Define custom dependencies that can be created in the matrix.
  - Specify the appearance of the matrix, that is, change the default colors of the cell and both row and column headers, assign custom icons to represent dependencies, and so forth.
  - Define cases when specific dependencies should be updated without rebuilding the whole matrix.
  - Export the data of a Dependency Matrix to any format.

****You can find the code examples in

- <installation_directory>\openapi\examples\dependencymatrix

#### PANEL: Related pages

Related pages

true

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p><ac:link><ri:page ri:content-title="Dependency Matrix" ri:space-key="MT" /></ac:link> is a special type of diagram, that is, a diagram with a specific stereotype applied. Our modeling tools provide an API to:</p><ul><li>Create custom types of the Dependency Matrix.</li><li>Customize a Dependency Matrix as follows:<ul><li>Configure the command bar, shortcut menus of the row or column header element, cell, and filter panel.</li><li>Assign shortcut keys for commands.</li><li>Define custom dependencies that can be created in the matrix.</li><li>Specify the appearance of the matrix, that is, change the default colors of the cell and both row and column headers, assign custom icons to represent dependencies, and so forth.</li><li>Define cases when specific dependencies should be updated without rebuilding the whole matrix.</li><li>Export the data of a Dependency Matrix to any format.</li></ul></li></ul><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="149c6619-33cd-40ac-aa63-ffaeb054ed5d"><ac:rich-text-body><p><strong> </strong>You can find the code examples in</p><ul><li><em>&lt;installation_directory&gt;\openapi\examples\dependencymatrix</em></li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell><ac:layout-cell><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="2ec81986-1195-4a33-b3e7-c53171711e90"><ac:parameter ac:name="title">Related pages</ac:parameter><ac:rich-text-body><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="020d5294-9339-4f3e-ac93-82cb86709a4c"><ac:parameter ac:name="all">true</ac:parameter></ac:structured-macro></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=249573456 space=DEVG version=1 -->
## PAGE 00811: Working with diagrams

- page_id: `249573456`
- space_key: `DEVG`
- source_url: https://docs.nomagic.com/spaces/DEVG/pages/249573456/Working+with+diagrams
- version_number: 1
- version_date: `2023-12-08T15:23:59.782+01:00`
- ancestors: Developer Guides Home > Modeling Tools Developer Guide > UML-based
- labels: []

### NORMALIZED CONTENT

Diagrams are not a part of UML metamodel, but we extended it and introduced a new Diagram element. Diagram element extends a standard UML NamedElement.

#### PANEL: Related pages

Related pages

true

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p>Diagrams are not a part of UML metamodel, but we extended it and introduced a new Diagram element. Diagram element extends a standard UML NamedElement.</p><p> </p></ac:layout-cell><ac:layout-cell><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="a074d2fc-ee1f-4fc4-aaae-f2073920d554"><ac:parameter ac:name="title">Related pages</ac:parameter><ac:rich-text-body><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="5f33f1b4-4842-4f30-9938-416ac1254e80"><ac:parameter ac:name="all">true</ac:parameter></ac:structured-macro></p></ac:rich-text-body></ac:structured-macro></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=296125236 space=DEVG version=20 -->
## PAGE 00812: Working with Element Properties

- page_id: `296125236`
- space_key: `DEVG`
- source_url: https://docs.nomagic.com/spaces/DEVG/pages/296125236/Working+with+Element+Properties
- version_number: 20
- version_date: `2026-04-15T20:50:49.978+02:00`
- ancestors: Developer Guides Home > Modeling Tools Developer Guide > SysML v2 > Working With Model
- labels: []

### NORMALIZED CONTENT

Element properties are accessed and modified using the metamodel’s standard getter and setter methods, which provide a consistent way to read and update model data.These methods ensure that changes are properly reflected in the underlying model while maintaining its integrity. Below are a few examples of setting and getting commonly used element properties:

###### Name

The declaredName property represents the user-defined name of a *[com.dassault_systemes.modeler.kerml.model.kerml.Element](https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/kerml/model/kerml/Element.html)*. It is used to identify and display the element within the model. *[getDeclaredName()](https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/kerml/model/kerml/Element.html#getDeclaredName())* returns the name explicitly assigned to the element and *[setDeclaredName](https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/kerml/model/kerml/Element.html#setDeclaredName(java.lang.String))(String)* updates the element’s name. You can retrieve and update this property using the provided getter and setter methods:

```java

```

###### ShortName

The declaredShortName property provides an optional, concise identifier for an element. It is typically used as a shorter or more readable alternative to the primary declaredName, especially in diagrams or contexts where space is limited. *[getDeclaredShortName()](https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/kerml/model/kerml/Element.html#getDeclaredShortName())*retrieves the short name of the element. *[setDeclaredShortName](https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/kerml/model/kerml/Element.html#setDeclaredShortName(java.lang.String))(String)*assigns a short, alternative name.

```java

```

###### Multiplicity

[Multiplicity](https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/kerml/model/kerml/Multiplicity.html) defines the allowable number of instances for a type. It is expressed as a range *(e.g., 1, 0..1, 1..*)*. 
The [Multiplicities](https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/kerml/model/Multiplicities.html) utility class provides methods to both set and retrieve multiplicity values.

```java

```

###### Direction

The direction of a feature defines how data flows through it. For elements such as [PortUsage](https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/sysml/model/sysml/PortUsage.html), the direction can be specified using the *[FeatureDirectionKind](https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/kerml/model/kerml/FeatureDirectionKind.html)* enum. Use *[setDirection](https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/kerml/model/kerml/Feature.html#getDirection())()*to assign the feature direction and use *[getDirection](https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/kerml/model/kerml/Feature.html#getDirection())()* to retrieve the current direction. 
Supported direction values :**[IN](https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/kerml/model/kerml/FeatureDirectionKind.html#IN), [OUT](https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/kerml/model/kerml/FeatureDirectionKind.html#OUT), [INOUT](https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/kerml/model/kerml/FeatureDirectionKind.html#INOUT).

```java

```

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><span style="color:var(--ds-background-accent-red-bolder,#c9372c);"><span style="color:var(--ds-text,#172b4d);">Element properties are accessed and modified using the metamodel’s standard getter and setter methods, which provide a consistent way to read and update model data. </span></span><span style="letter-spacing: 0.0px;color:var(--ds-text,#172b4d);">These methods ensure that changes are properly reflected in the underlying model while maintaining its integrity. Below are a few examples of setting and getting commonly used element properties:</span></p><h5>Name</h5><p>The declaredName property represents the user-defined name of a <em><a href="https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/kerml/model/kerml/Element.html">com.dassault_systemes.modeler.kerml.model.kerml.Element</a></em>. It is used to identify and display the element within the model. <em><a href="https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/kerml/model/kerml/Element.html#getDeclaredName()">getDeclaredName()</a></em> returns the name explicitly assigned to the element and <em><a href="https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/kerml/model/kerml/Element.html#setDeclaredName(java.lang.String)">setDeclaredName</a>(String)</em> updates the element’s name. You can retrieve and update this property using the provided getter and setter methods:<br /><br /></p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="bf538163-3380-42a1-854d-fd032795b386"><ac:parameter ac:name="language">java</ac:parameter><ac:plain-text-body><![CDATA[com.dassault_systemes.modeler.kerml.model.kerml.Element element = ...; 
String name = element.getDeclaredName();
element.setDeclaredName("name");]]></ac:plain-text-body></ac:structured-macro><h5>ShortName</h5><p>The declaredShortName property provides an optional, concise identifier for an element. It is typically used as a shorter or more readable alternative to the primary declaredName, especially in diagrams or contexts where space is limited. <em><a href="https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/kerml/model/kerml/Element.html#getDeclaredShortName()">getDeclaredShortName()</a> </em>retrieves the short name of the element. <em><a href="https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/kerml/model/kerml/Element.html#setDeclaredShortName(java.lang.String)">setDeclaredShortName</a>(String) </em>assigns a short, alternative name.<br /><br /></p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="cc9559e1-d2f6-4eeb-a9f1-9b200288375a"><ac:parameter ac:name="language">java</ac:parameter><ac:plain-text-body><![CDATA[com.dassault_systemes.modeler.kerml.model.kerml.Element element = ...;
element.setDeclaredShortName("drn");
String shortName = element.getDeclaredShortName();

]]></ac:plain-text-body></ac:structured-macro><h5>Multiplicity</h5><p><a href="https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/kerml/model/kerml/Multiplicity.html">Multiplicity</a> defines the allowable number of instances for a type. It is expressed as a range <em>(e.g., 1, 0..1, 1..*)</em>.<br />The <a href="https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/kerml/model/Multiplicities.html">Multiplicities</a> utility class provides methods to both set and retrieve multiplicity values.<br /><br /></p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="4a09ae1d-a0d3-4eb8-ab28-90f93f054259"><ac:parameter ac:name="language">java</ac:parameter><ac:plain-text-body><![CDATA[com.dassault_systemes.modeler.kerml.model.kerml.Type type = ...;
Multiplicity multiplicity = Multiplicities.getOwnedOrInheritedMultiplicity(drone);
Multiplicities.setMultiplicity(type, "1..*");]]></ac:plain-text-body></ac:structured-macro><h5>Direction</h5><p>The direction of a feature defines how data flows through it. For elements such as <a href="https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/sysml/model/sysml/PortUsage.html">PortUsage</a>, the direction can be specified using the <em><a href="https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/kerml/model/kerml/FeatureDirectionKind.html">FeatureDirectionKind</a></em> enum. Use <em><a href="https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/kerml/model/kerml/Feature.html#getDirection()">setDirection</a>() </em>to assign the feature direction and use <em><a href="https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/kerml/model/kerml/Feature.html#getDirection()">getDirection</a>()</em> to retrieve the current direction.<br />Supported direction values :<em> </em><a href="https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/kerml/model/kerml/FeatureDirectionKind.html#IN">IN</a>, <a href="https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/kerml/model/kerml/FeatureDirectionKind.html#OUT">OUT</a>, <a href="https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/kerml/model/kerml/FeatureDirectionKind.html#INOUT">INOUT</a>.</p><p><br /></p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="145a8dba-0521-4a99-911d-1391c748401c"><ac:parameter ac:name="language">java</ac:parameter><ac:plain-text-body><![CDATA[com.dassault_systemes.modeler.kerml.model.kerml.Feature feature = ...;
feature.setDirection(FeatureDirectionKind.IN);
FeatureDirectionKind direction = feature.getDirection();]]></ac:plain-text-body></ac:structured-macro><p><br /></p>
````

<!--NOMAGIC_PAGE id=249573527 space=DEVG version=1 -->
## PAGE 00813: Working with Gantt Chart

- page_id: `249573527`
- space_key: `DEVG`
- source_url: https://docs.nomagic.com/spaces/DEVG/pages/249573527/Working+with+Gantt+Chart
- version_number: 1
- version_date: `2023-12-08T15:24:05.386+01:00`
- ancestors: Developer Guides Home > Modeling Tools Developer Guide > UML-based > Working with diagrams
- labels: []

### NORMALIZED CONTENT

**Refreshing Gantt Chart**

To refresh the gantt chart, use the GanttChartUtilities.refreshChart(diagram) method:

```text

```

```text

```

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="auto-cursor-target"><span><strong>Refreshing Gantt Chart<br /></strong></span></p><p>To refresh the gantt chart, use the GanttChartUtilities.refreshChart(diagram) method:</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="c4e582fc-94ba-4db7-83d9-bbf0bf654cc0"><ac:plain-text-body><![CDATA[GanttChartUtilities.refreshChart(Diagram)]]></ac:plain-text-body></ac:structured-macro><p><br /></p><pre><br /></pre>
````

<!--NOMAGIC_PAGE id=249573512 space=DEVG version=2 -->
## PAGE 00814: Working with Generic tables

- page_id: `249573512`
- space_key: `DEVG`
- source_url: https://docs.nomagic.com/spaces/DEVG/pages/249573512/Working+with+Generic+tables
- version_number: 2
- version_date: `2025-09-12T15:43:38.697+02:00`
- ancestors: Developer Guides Home > Modeling Tools Developer Guide > UML-based > Working with diagrams
- labels: []

### NORMALIZED CONTENT

A generic table is a diagram with a specific stereotype. It is used to represent the element properties in a table form. It can represent different element types in one table and show all their properties. Table rows represent elements, and columns represent element properties. For more information about generic tables and their managing, see [CONFLUENCE_PAGE title='Generic table' space='MT'].

The Open API of modeling tools provides the***com.nomagic.generictable.GenericTableManager* class for creating and manipulating generic tables.

This API is used for creating a generic table, adding, editing, and removing table columns and rows, as well as getting cell values.

Find the Generic Table Manager Example Plugin in <*MagicDraw_installation_directory>\openapi\examples\generictablemanager*.

###### **Creatin****g generic table**

To create a generic table, use the *GenericTableManager.createGenericTable(**Project**, java.lang.String)* method.

```java

```

```text

```

###### **Settin****g generic table filter**

To set a generic table element types, use the *GenericTableManager.setTableElementTypes(**Diagram**, java.util.List<java.lang.Object>)***method. The type of the element types list could be the Class or the Stereotype. See an example of the table element types:

```java
set = new HashSet();
List tableElementTypes = new ArrayList();
 
//Get all row elements
rowElements = GenericTableManager.getRowElements(createdDiagram);
for (int i = 0; i < rowElements.size(); i++)
{
	set.add(rowElements.get(i).getClassType());
}
tableElementTypes.addAll(set);]]>
```

###### **Gettin****g generic table element types**

To get the generic table element types, use the *GenericTableManager.getTableElementTypes(**Diagram)***method:

```java
setElementTypes = GenericTableManager.getTableElementTypes(createdDiagram);]]>
```

###### **Adding/gettin****g columns**

To add columns to the generic table, use the *GenericTableManager.addColumnsById(Diagram, java.util.List<java.lang.String>)*method.

To get all possible columns from the generic table, use the *GenericTableManager.getPossibleColumnIDs(**Element)***method. To get set columns for the generic table, use the *GenericTableManager.getColumnIds(**Diagram)***method.

```java
columnIDs = GenericTableManager.getPossibleColumnIDs(elementType);]]>
```

*getColumnIds(**Diagram)* returns columns from the generic table:

```java
columnIDs = GenericTableManager.getColumnIds(createdDiagram); 
GenericTableManager.addColumnsById(createdDiagram, columnIDs);]]>
```

How to get *columnIDs*, please look at the *com.nomagic.magicdraw.examples.generictablemanager.GenericTableManagerExamplePlugin.GenericTableManagerAction* class in the *GenericTableManagerExamplePlugin.java*file. The file can be found in *<program_installation_directory>\openapi\examples\generictablemanager*.

###### **Gettin****g cell value**

To get a value of the generic table call, use the *GenericTableManager.getCellValue(Diagram[,](http://jdocs.nomagic.com/2024x/com/nomagic/generictable/GenericTableManager.html#getCellValue-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element-java.lang.String-)Element, java.lang.String)*method:

```java

```

###### **Gettin****g column names**

To get column names from the generic table, use the *GenericTableManager.getColumnNames(Diagram[)](http://jdocs.nomagic.com/2024x/com/nomagic/generictable/GenericTableManager.html#getColumnNames-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram-)*method.

To get a single column name from the generic table, use the *GenericTableManager.getColumnNameById(**Diagram**, java.lang.String)***method.

```java
columnNames = GenericTableManager.getColumnNames(createdDiagram);
String columnName = GenericTableManager.getColumnNameById(createdDiagram, columnID);]]>
```

###### **Gettin****g row elements**

To get row elements from the generic table, use the *GenericTableManager.getRowElements(**Diagram)***method:

```java
rows = GenericTableManager.getRowElements(createdDiagram);]]>
```

******Gettin****g visible row elements**

To get visible row elements from the generic table, use the *GenericTableManager.getVisibleRowElements(**Diagram)***method:

```java
rows = GenericTableManager.getVisibleRowElements(createdDiagram);]]>
```

###### **Addin****g row element**

To add a new row for the model element to the generic table, use the *GenericTableManager.addRowElement(Diagram[,](http://jdocs.nomagic.com/2024x/com/nomagic/generictable/GenericTableManager.html#addRowElement-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element-)Element[)](http://jdocs.nomagic.com/2024x/com/nomagic/generictable/GenericTableManager.html#addRowElement-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element-)*method:

```java

```

The element you want to add must be of the same type as one of generic table filter types.

###### **Removin****g row element**

To remove a row from the generic table, use the *GenericTableManager.removeRowElement(**Diagram, Element)***method:

```java

```

**Setting table scope**

To set a scope for the generic table, use the *GenericTableManager.removeRowElement(**Diagram, Element)***method:

```java

```

**Refreshing table**

To refresh the table, use the GenericTableManager.refreshTable(Diagram) method:

```java

```

#### PANEL: On this page

On this page

#### PANEL: Related pages

Related pages

- [CONFLUENCE_PAGE title='SessionManager API' space='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p>A generic table is a diagram with a specific stereotype. It is used to represent the element properties in a table form. It can represent different element types in one table and show all their properties. Table rows represent elements, and columns represent element properties. For more information about generic tables and their manag<span style="color: rgb(0,0,0);">ing, see <ac:link><ri:page ri:space-key="MT" ri:content-title="Generic table" /><ac:plain-text-link-body><![CDATA[Generic Table]]></ac:plain-text-link-body></ac:link>.</span></p><p>The Open API of modeling tools provides the<em> </em><em>com.nomagic.generictable.GenericTableManager</em> class for creating and manipulating generic tables.</p><div class="WordSection1"><p>This API is used for creating a generic table, adding, editing, and removing table columns and rows, as well as getting cell values.</p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="1b944d37-d25a-4e2b-af42-bd6490c10121"><ac:rich-text-body><p>Find the Generic Table Manager Example Plugin in &lt;<em style="line-height: 1.4285715;">MagicDraw_installation_directory&gt;\openapi\examples\generictablemanager</em>.</p></ac:rich-text-body></ac:structured-macro><h4><strong style="color: rgb(0,0,0);line-height: 1.4285715;">Creatin</strong><strong style="color: rgb(0,0,0);line-height: 1.4285715;">g generic table</strong></h4><p>To create a generic table, use the <em>GenericTableManager.createGenericTable(</em><em>Project</em><em>, java.lang.String)</em> method.</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="3c092b5b-12cf-4a75-92a0-fb1862597c7d"><ac:parameter ac:name="language">java</ac:parameter><ac:plain-text-body><![CDATA[Diagram createdDiagram = GenericTableManager.createGenericTable(project, "Generic table name");]]></ac:plain-text-body></ac:structured-macro><pre><br /></pre><h4><strong>Settin</strong><strong>g generic table filter</strong></h4><p>To set a generic table element types, use the <em>GenericTableManager.setTableElementTypes(</em><em>Diagram</em><em>, java.util.List&lt;java.lang.Object&gt;)</em><em> </em>method. The type of the element types list could be the Class or the Stereotype. See an example of the table element types:</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="42d3b258-b3cd-4227-995f-95557f7cd731"><ac:parameter ac:name="language">java</ac:parameter><ac:plain-text-body><![CDATA[//The table element types list
Set<Class> set = new HashSet<Class>();
List<Object> tableElementTypes = new ArrayList<Object>();
 
//Get all row elements
rowElements = GenericTableManager.getRowElements(createdDiagram);
for (int i = 0; i < rowElements.size(); i++)
{
	set.add(rowElements.get(i).getClassType());
}
tableElementTypes.addAll(set);]]></ac:plain-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></div><div class="WordSection2"><h4><strong>Gettin</strong><strong>g generic table element types</strong></h4><p>To get the generic table element types, use the <em style="line-height: 1.4285715;">GenericTableManager.getTableElementTypes(</em><em style="line-height: 1.4285715;">Diagram)</em><em style="line-height: 1.4285715;"> </em>method:</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="685db55f-3f2e-400e-83a3-435e3dd89cca"><ac:parameter ac:name="language">java</ac:parameter><ac:plain-text-body><![CDATA[List<Object> setElementTypes = GenericTableManager.getTableElementTypes(createdDiagram);]]></ac:plain-text-body></ac:structured-macro><h4><strong>Adding/gettin</strong><strong>g columns</strong></h4><p>To add columns to the generic table, use the <em>GenericTableManager.addColumnsById(Diagram, java.util.List&lt;java.lang.String&gt;) </em>method.</p><p>To get all possible columns from the generic table, use the <em>GenericTableManager.getPossibleColumnIDs(</em><em>Element)</em><em> </em>method. To get set columns for the generic table, use the <em>GenericTableManager.getColumnIds(</em><em>Diagram)</em><em> </em>method.</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="7db69c7c-fa56-479b-a51d-ef5e68761182"><ac:parameter ac:name="language">java</ac:parameter><ac:plain-text-body><![CDATA[List<String> columnIDs = GenericTableManager.getPossibleColumnIDs(elementType);]]></ac:plain-text-body></ac:structured-macro><p><em>getColumnIds(</em><em>Diagram)</em> returns columns from the generic table:</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="017b2a32-14ba-4359-9ae0-530a9f42c2bd"><ac:parameter ac:name="language">java</ac:parameter><ac:plain-text-body><![CDATA[List<String> columnIDs = GenericTableManager.getColumnIds(createdDiagram); 
GenericTableManager.addColumnsById(createdDiagram, columnIDs);]]></ac:plain-text-body></ac:structured-macro><br /><p>How to get <em>columnIDs</em>, please look at the <em>com.nomagic.magicdraw.examples.generictablemanager.GenericTableManagerExamplePlugin.GenericTableManagerAction</em> class in the <em>GenericTableManagerExamplePlugin.java </em>file. The file can be found in <em>&lt;program_installation_directory&gt;\openapi\examples\generictablemanager</em>.</p><p><br /></p><h4><strong>Gettin</strong><strong>g cell value</strong></h4><p>To get a value of the generic table call, use the <em>GenericTableManager.getCellValue(Diagram<a href="http://jdocs.nomagic.com/2024x/com/nomagic/generictable/GenericTableManager.html#getCellValue-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element-java.lang.String-">, </a>Element, java.lang.String) </em>method:</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="13ffc60b-1f89-4985-bb39-9f0f8f088edb"><ac:parameter ac:name="language">java</ac:parameter><ac:plain-text-body><![CDATA[Property mdProperty = GenericTableManager.getCellValue(createdDiagram, element, columnId);]]></ac:plain-text-body></ac:structured-macro><br /><h4><strong>Gettin</strong><strong>g column names</strong></h4><p>To get column names from the generic table, use the <em>GenericTableManager.getColumnNames(Diagram<a href="http://jdocs.nomagic.com/2024x/com/nomagic/generictable/GenericTableManager.html#getColumnNames-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram-">)</a> </em>method.</p><p>To get a single column name from the generic table, use the <em>GenericTableManager.getColumnNameById(</em><em>Diagram</em><em>, java.lang.String)</em><em> </em>method.</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="9a55642b-51f3-4569-99f5-42c37f05b311"><ac:parameter ac:name="language">java</ac:parameter><ac:plain-text-body><![CDATA[List<String> columnNames = GenericTableManager.getColumnNames(createdDiagram);
String columnName = GenericTableManager.getColumnNameById(createdDiagram, columnID);]]></ac:plain-text-body></ac:structured-macro><br /><h4><strong>Gettin</strong><strong>g row elements</strong></h4><p>To get row elements from the generic table, use the <em>GenericTableManager.getRowElements(</em><em>Diagram)</em><em> </em>method:</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="205ace80-6605-4aed-a640-2ef86c8f1e51"><ac:parameter ac:name="language">java</ac:parameter><ac:plain-text-body><![CDATA[List<Element> rows = GenericTableManager.getRowElements(createdDiagram);]]></ac:plain-text-body></ac:structured-macro><p><strong style="color: rgb(0,0,0);line-height: 1.42857;"><br /></strong><strong style="color: rgb(0,0,0);line-height: 1.42857;">Gettin</strong><strong style="color: rgb(0,0,0);line-height: 1.42857;">g visible row elements</strong></p><p>To get visible row elements from the generic table, use the <em>GenericTableManager.getVisibleRowElements(</em><em>Diagram)</em><em> </em>method:</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="f47b5ee1-f6bc-4f76-9454-49f77f37e812"><ac:parameter ac:name="language">java</ac:parameter><ac:plain-text-body><![CDATA[List<Element> rows = GenericTableManager.getVisibleRowElements(createdDiagram);]]></ac:plain-text-body></ac:structured-macro><br /><h4><strong>Addin</strong><strong>g row element</strong></h4><p>To add a new row for the model element to the generic table, use the <em>GenericTableManager.addRowElement(Diagram<a href="http://jdocs.nomagic.com/2024x/com/nomagic/generictable/GenericTableManager.html#addRowElement-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element-">, </a>Element<a href="http://jdocs.nomagic.com/2024x/com/nomagic/generictable/GenericTableManager.html#addRowElement-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element-">)</a> </em>method:</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="ef82abee-a4a6-4134-923d-067125559f06"><ac:parameter ac:name="language">java</ac:parameter><ac:plain-text-body><![CDATA[GenericTableManager.addRowElement(createdDiagram, element);]]></ac:plain-text-body></ac:structured-macro><p>The element you want to add must be of the same type as one of generic table filter types.</p></div><h4><strong>Removin</strong><strong>g row element</strong></h4><p>To remove a row from the generic table, use the <em>GenericTableManager.removeRowElement(</em><em>Diagram, Element)</em><em> </em>method:</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="499d517d-469b-46e7-be89-f50dcfb26dc5"><ac:parameter ac:name="language">java</ac:parameter><ac:plain-text-body><![CDATA[GenericTableManager.removeRowElement(createdDiagram, element);]]></ac:plain-text-body></ac:structured-macro><p class="auto-cursor-target"><span style="letter-spacing: -0.042px;"><strong>Setting table scope</strong></span></p><p>To set a scope for  the generic table, use the <em>GenericTableManager.removeRowElement(</em><em>Diagram, Element)</em><em> </em>method:</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="8b9a558c-c187-42b8-b1b4-1ec07ade738f"><ac:parameter ac:name="language">java</ac:parameter><ac:plain-text-body><![CDATA[GenericTableManager.removeRowElement(createdDiagram, element);]]></ac:plain-text-body></ac:structured-macro><p class="auto-cursor-target"><span><strong>Refreshing table<br /></strong></span></p><p>To refresh the table, use the GenericTableManager.refreshTable(Diagram) method:</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="d0465c4b-41d4-413a-8088-961710f0f49a"><ac:parameter ac:name="language">java</ac:parameter><ac:plain-text-body><![CDATA[GenericTableManager.refreshTable(diagram)]]></ac:plain-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell><ac:layout-cell><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="84ace198-a24b-457d-a46e-cc18a8db8595"><ac:parameter ac:name="title">On this page</ac:parameter><ac:rich-text-body><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="f616bdf8-03b9-420a-b222-ef83b9be7c5f" /></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="becf631e-811b-484c-90d3-30aaa50ab94c"><ac:parameter ac:name="title">Related pages</ac:parameter><ac:rich-text-body><ul><li><ac:link><ri:page ri:content-title="SessionManager API" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=249573384 space=DEVG version=1 -->
## PAGE 00815: Working with icons

- page_id: `249573384`
- space_key: `DEVG`
- source_url: https://docs.nomagic.com/spaces/DEVG/pages/249573384/Working+with+icons
- version_number: 1
- version_date: `2024-02-13T09:37:24.955+01:00`
- ancestors: Developer Guides Home > Modeling Tools Developer Guide > General > Adding new functionality
- labels: []

### NORMALIZED CONTENT

Use *com.nomagic.magicdraw.icons.IconsFactory*to load the icons.

As of version 18.2, modeling tools support HiDPI/Retina monitors and chooses dynamically which icon to load - a lower or higher resolution. All this logic is encapsulated in *com.nomagic.ui.ScalableImageIcon*. *IconsFactory*adds additional caching and ensures that icon from the same URL will be loaded just once.

The HiDPI/Retina compatibility requires two images - for a normal resolution and for a high resolution. Use the SVG format for a high resolution image. Put both icons with the same name (but a different extension) at the same location. Use a normal icon URL to load the icon, but the SVG icon will be loaded on the high resolution monitor.

##### Icon classes

| Class | Description |
| --- | --- |
| com.nomagic.ui.ResizableIcon | The extended version of javax.swing.Icon. It can be scaled (resized) during the painting. |
| com.nomagic.ui.ResizableIconAdapter | An adapter of a simple javax.swing.Icon to a com.nomagic.ui.ResizableIcon. |
| com.nomagic.ui.SquareIcon | An icon which fits another icon into a square of a given size. |
| com.nomagic.ui.ScalableImageIcon | The HiDPI (Retina) friendly javax.swing.ImageIcon implementation. This class dynamically chooses a right image by the current screen dpi and/or the scaling factor defined in the system (Retina and etc). If scaling is needed and the SVG icon with the same name is available at the given location, the SVG icon will be used instead of a bitmap icon. Dynamic choosing will work only if two icons are provided at the same location. For example, /com/product/icons/a.png and /com/product/icons/a.svg. ScalableImageIcon(Product.class, "/com/product/icons/a.png") will load a.png on a regular dpi monitor, but a.svg will be loaded on the HiDPI monitor. Keep in mind that the SVG icon size can be any. The SVG icon will be resized according to the size of the a.png icon and a scaling factor. For example, if a size of a.png is 16x16 and a scaling factor is 2, the loaded SVG icon will be resized to 32x32 if needed. The original icon will be loaded and scaled if the SVG icon is not provided, but HiDPI with scaling is used. |

##### Utility classes

| Class | Description |
| --- | --- |
| com.nomagic.magicdraw.icons.IconsFactory | A utility class to load icons from the MagicDraw icons package or other locations. |
| com.nomagic.ui.IconUtilities | A utility class to work with Icons. |

```text

```

##### Advanced icons classes

| Class | Description |
| --- | --- |
| com.nomagic.ui.AlphaCompositeIcon | Paints a wrapped icon with an alpha composite. |
| com.nomagic.ui.BorderIcon | An icon for adding a border around a wrapped icon. |
| com.nomagic.ui.DoubleIcon | An Icon for painting two wrapped icons on a top of each other. |
| com.nomagic.ui.RetinaImageIcon | A retina friendly image icon implementation. The icon (and the image returned by this icon) is twice smaller then the wrapped icon itself.A wrapped icon is used for painting. On painting, Graphics is scaled down by a retina scale factor and the wrapped icon is painted. |
| com.nomagic.ui.DoubleSizeImageIcon | An icon combines two other icons and chooses which one to paint depending on the graphics scaling. |
| com.nomagic.ui.ResizableIconImageIcon | An image icon which wraps other icon and provides an image for a wrapped icon. The provided image is HiDPI/Retina friendly. On Mac, a special instance of java.awt.Image (sun.awt.image.MultiResolutionToolkitImage) is returned which supports multi-resolution. |

#### PANEL: On this page

On this page

#### PANEL: Related pages

Related pages

true

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p>Use <em>com.nomagic.magicdraw.icons.IconsFactory </em>to load the icons. </p><p>As of version 18.2, modeling tools support HiDPI/Retina monitors and chooses dynamically which icon to load - a lower or higher resolution. All this logic is encapsulated in <em>com.nomagic.ui.ScalableImageIcon</em>. <em>IconsFactory </em>adds additional caching and ensures that icon from the same URL will be loaded just once.</p><p><span style="color: rgb(0,0,0);">The HiDPI/Retina compatibility requires two images - for a normal resolution and for a high resolution. Use the SVG format for a high resolution image. Put both icons with the same name (but a different extension) at the same location. Use a normal icon URL to load the icon, but the SVG icon will be loaded on the high resolution monitor.</span></p><h3><span>Icon classes</span></h3><table><colgroup><col /><col /></colgroup><tbody><tr><th>Class</th><th>Description</th></tr><tr><td colspan="1"><em><span style="color: rgb(0,0,0);">com.nomagic.ui.ResizableIcon</span></em></td><td colspan="1">The extended version of <em>javax.swing.Icon.</em> It can be scaled (resized) during the painting.</td></tr><tr><td colspan="1"><em><span style="color: rgb(0,0,0);">com.nomagic.ui.ResizableIconAdapter</span></em></td><td colspan="1"><p><span style="color: rgb(0,0,0);">An adapter of a simple <em>javax.swing.Icon</em> to a <em>com.nomagic.ui.ResizableIcon</em><em>.</em></span></p></td></tr><tr><td colspan="1"><em><span style="color: rgb(0,0,0);">com.nomagic.ui.SquareIcon</span></em></td><td colspan="1"><p>An icon which fits another icon into a square of a given size.</p></td></tr><tr><td colspan="1"><em><span style="color: rgb(0,0,0);">com.nomagic.ui.ScalableImageIcon</span></em></td><td colspan="1"><p><span style="color: rgb(0,0,0);">The HiDPI (Retina) friendly <em>javax.swing.ImageIcon</em> implementation. This class dynamically chooses a right image by the current screen dpi and/or the scaling factor defined in the system (Retina and etc). If scaling is needed and the SVG icon with the same name is available at the given location, the SVG icon will be used instead of a bitmap icon. Dynamic choosing will work only if two icons are provided at the same location. </span></p><p><span style="color: rgb(0,0,0);">For example, </span><em><span style="color: rgb(0,0,0);">/com/product/icons/a.png </span></em><span style="color: rgb(0,0,0);">and </span><em><span style="color: rgb(0,0,0);">/com/product/icons/a.svg. </span>ScalableImageIcon</em><span style="color: rgb(0,0,0);"><em>(Product.class, &quot;/com/product/icons/a.png&quot;)</em> will load <em>a.png</em> on a regular dpi monitor, but <em>a.svg</em> will be loaded on the HiDPI monitor. </span><span style="color: rgb(0,0,0);">Keep in mind that the SVG icon size can be any. The SVG icon will be resized according to the size of the<em> a.png</em> icon and a scaling factor. </span><span style="color: rgb(0,0,0);">For example, if a size of <em>a.png</em> is 16x16 and a scaling factor is 2, the loaded SVG icon will be resized to 32x32 if needed. </span><span style="color: rgb(0,0,0);">The original icon will be loaded and scaled if the SVG</span><span> </span><span style="color: rgb(0,0,0);">icon is not provided, but HiDPI with scaling is used.</span></p><div><span style="color: rgb(0,0,0);"><br /></span></div></td></tr></tbody></table><h3>Utility classes</h3><table><colgroup><col /><col /></colgroup><tbody><tr><th>Class</th><th>Description</th></tr><tr><td><em>com.nomagic.magicdraw.icons.IconsFactory</em></td><td><span style="color: rgb(0,0,0);">A utility class to load icons from the MagicDraw icons package or other locations.</span></td></tr><tr><td><em>com.nomagic.ui.IconUtilities</em></td><td><span style="color: rgb(0,0,0);">A u</span><span style="color: rgb(0,0,0);">tility class to work with Icons.</span></td></tr></tbody></table><pre><br /></pre><h3><span style="color: rgb(0,0,0);">Advanced icons classes</span></h3><table><colgroup><col /><col /></colgroup><tbody><tr><th>Class</th><th>Description</th></tr><tr><td><em><span style="color: rgb(0,0,0);">com.nomagic.ui.AlphaCompositeIcon</span></em></td><td><p><span style="color: rgb(0,0,0);">Paints a wrapped icon with an alpha composite.</span></p></td></tr><tr><td><em><span style="color: rgb(0,0,0);">com.nomagic.ui.BorderIcon</span></em></td><td><p><span style="color: rgb(0,0,0);">An icon for adding a border around a wrapped icon.</span></p></td></tr><tr><td><em><span style="color: rgb(0,0,0);">com.nomagic.ui.DoubleIcon</span></em></td><td><p><span style="color: rgb(0,0,0);">An Icon for painting two wrapped icons on a top of each other.</span></p></td></tr><tr><td colspan="1"><em><span style="color: rgb(0,0,0);">com.nomagic.ui.RetinaImageIcon</span></em></td><td colspan="1"><p><span style="color: rgb(0,0,0);">A retina friendly image icon implementation. The icon (and the image returned by this icon) is twice smaller then the wrapped icon itself.</span></p><p><span style="color: rgb(0,0,0);">A wrapped icon is used for painting. On painting, Graphics is scaled down by a retina scale factor and the wrapped icon is painted.</span></p></td></tr><tr><td colspan="1"><em><span style="color: rgb(0,0,0);">com.nomagic.ui.DoubleSizeImageIcon</span></em></td><td colspan="1"><p><span style="color: rgb(0,0,0);">An icon combines two other icons and chooses which one to paint depending on the graphics scaling.</span></p></td></tr><tr><td colspan="1"><em>com.nomagic.ui.ResizableIconImageIcon</em></td><td colspan="1"><span style="color: rgb(0,0,0);"><span>An image icon which wraps other icon and provides an image for a wrapped icon. The p</span></span><span style="color: rgb(0,0,0);">rovided image is HiDPI/Retina friendly. On Mac, a special instance of <em>java.awt.Image</em> (<em>sun.awt.image.MultiResolutionToolkitImage</em>) is returned which supports multi-resolution.</span></td></tr></tbody></table><p class="auto-cursor-target"><br /></p></ac:layout-cell><ac:layout-cell><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="83e819a2-cb1b-43fb-9c59-c36f9667233d"><ac:parameter ac:name="title">On this page</ac:parameter><ac:rich-text-body><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="7fded546-72ea-40a4-b103-845a3fa165dc" /></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="36954480-067d-430e-bdb9-742c68a9a8c1"><ac:parameter ac:name="title">Related pages</ac:parameter><ac:rich-text-body><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="6c4cedb7-d96b-477c-924e-b34dc831c71a"><ac:parameter ac:name="all">true</ac:parameter></ac:structured-macro></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=296124600 space=DEVG version=5 -->
## PAGE 00816: Working With Model

- page_id: `296124600`
- space_key: `DEVG`
- source_url: https://docs.nomagic.com/spaces/DEVG/pages/296124600/Working+With+Model
- version_number: 5
- version_date: `2026-04-17T18:49:50.013+02:00`
- ancestors: Developer Guides Home > Modeling Tools Developer Guide > SysML v2
- labels: []

### NORMALIZED CONTENT

This section covers the core operations for interacting with a SysML v2 model using the Open API—creating elements, defining relationships, modifying structure, and querying the model.

SysML v2 is **relationship-driven**, meaning most API calls do not just set values but create or update underlying relationships (such as ownership, typing, or connections). The Open API ensures these changes keep the model valid and consistent.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p data-start="62" data-end="246">This section covers the core operations for interacting with a SysML v2 model using the Open API—creating elements, defining relationships, modifying structure, and querying the model.</p><p data-start="248" data-end="493">SysML v2 is <strong data-start="260" data-end="283">relationship-driven</strong>, meaning most API calls do not just set values but create or update underlying relationships (such as ownership, typing, or connections). The Open API ensures these changes keep the model valid and consistent.</p>
````

<!--NOMAGIC_PAGE id=249573477 space=DEVG version=1 -->
## PAGE 00817: Working with presentation elements

- page_id: `249573477`
- space_key: `DEVG`
- source_url: https://docs.nomagic.com/spaces/DEVG/pages/249573477/Working+with+presentation+elements
- version_number: 1
- version_date: `2024-02-13T09:38:50.110+01:00`
- ancestors: Developer Guides Home > Modeling Tools Developer Guide > UML-based > Working with diagrams > Presentation elements (symbols)
- labels: []

### NORMALIZED CONTENT

706297666

INLINE

706297668

INLINE

706297667

INLINE

Use only getter in Presentation elements’ classes even if setters are available. Setters are not part of OpenAPI and in most cases should not be called directly.

Majority of functions for manipulating/creating/deleting the symbols is available in utility class *com.nomagic.magicdraw.openapi.uml.PresentationElementsManager**.*

*PresentationElementManager* can be used only inside the created session with *com.nomagic.magicdraw.openapi.uml.SessionManager*. If a session is not created, *java.lang.IllegalStateException* is thrown.

*PresentationElementManager* can be used only in already loaded and active project. In other cases, results can be unpredictable.

*PresentationElementManager* is implemented as a singleton. Use method *PresentationElementManager.getInstance()*to get a shared instance of this manager.

706297665

INLINE

**Related pages**

- [CONFLUENCE_PAGE title='SessionManager API' space='']

true

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="c938f53a-5c7c-4427-822b-ba6db3822b35"><ac:parameter ac:name="id">706297666</ac:parameter><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="cdfae3ad-ea5f-484a-a06e-075f454d6ee3"><ac:parameter ac:name="id">706297668</ac:parameter><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="6a993cf2-94d7-4484-9117-d034054a7650"><ac:parameter ac:name="id">706297667</ac:parameter><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><div class="WordSection1"><p>Use only getter in Presentation elements’ classes even if setters are available. Setters are not part of OpenAPI and in most cases should not be called directly.</p><p><br /></p><p>Majority of functions for manipulating/creating/deleting the symbols is available in utility class <em>com.nomagic.magicdraw.openapi.uml.PresentationElementsManager</em><em>. </em></p><p><em>PresentationElementManager</em> can be used only inside the created session with <em>com.nomagic.magicdraw.openapi.uml.SessionManager</em>. If a session is not created, <em>java.lang.IllegalStateException</em> is thrown.</p></div><p><em>PresentationElementManager</em> can be used only in already loaded and active project. In other cases, results can be unpredictable.</p><p><em>PresentationElementManager</em> is implemented as a singleton. Use method <em>PresentationElementManager.getInstance() </em>to get a shared instance of this manager.</p><p><br /></p></ac:layout-cell><ac:layout-cell><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section></ac:layout></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="aaa930a4-864a-4f26-9658-07bcc0ce2e04"><ac:parameter ac:name="id">706297665</ac:parameter><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><p class="auto-cursor-target"><strong>Related pages</strong></p><ul><li><ac:link><ri:page ri:content-title="SessionManager API" /></ac:link></li></ul><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="7c7ab909-e217-4362-9dd2-78168dfe4f57"><ac:parameter ac:name="all">true</ac:parameter></ac:structured-macro></p><p><br /></p><p class="auto-cursor-target"><br /></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p>
````

<!--NOMAGIC_PAGE id=249573387 space=DEVG version=1 -->
## PAGE 00818: Working with project

- page_id: `249573387`
- space_key: `DEVG`
- source_url: https://docs.nomagic.com/spaces/DEVG/pages/249573387/Working+with+project
- version_number: 1
- version_date: `2024-01-31T16:09:05.261+01:00`
- ancestors: Developer Guides Home > Modeling Tools Developer Guide > General
- labels: []

### NORMALIZED CONTENT



### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="a8251faf-7ec9-4e57-8f64-a886115f67a2" /></p></ac:layout-cell><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=249573400 space=DEVG version=2 -->
## PAGE 00819: Working with projects from Teamwork Cloud server

- page_id: `249573400`
- space_key: `DEVG`
- source_url: https://docs.nomagic.com/spaces/DEVG/pages/249573400/Working+with+projects+from+Teamwork+Cloud+server
- version_number: 2
- version_date: `2025-09-12T15:43:38.376+02:00`
- ancestors: Developer Guides Home > Modeling Tools Developer Guide > General > Working with project
- labels: []

### NORMALIZED CONTENT

Use the *com.nomagic.magicdraw.esi.EsiUtils* utility class to work with projects from [CONFLUENCE_PAGE title='Using Teamwork Cloud' space='MT'].

Check javadoc for more details.

****You can find the code examples in <*modeling tool**installation direc**tory>\openapi\examples\teamworkcloud*

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p>Use the <em>com.nomagic.magicdraw.esi.EsiUtils</em> utility class to work with projects from <ac:link><ri:page ri:space-key="MT" ri:content-title="Using Teamwork Cloud" /><ac:plain-text-link-body><![CDATA[Teamwork Cloud]]></ac:plain-text-link-body></ac:link>. </p><p>Check javadoc for more details.</p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="149c6619-33cd-40ac-aa63-ffaeb054ed5d"><ac:rich-text-body><p><strong> </strong>You can find the code examples in <span style="line-height: 1.4285715;">&lt;<em>modeling tool</em> </span><em style="line-height: 1.4285715;">installation direc</em><em style="line-height: 1.4285715;">tory&gt;\openapi\examples\teamworkcloud</em></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=249573526 space=DEVG version=1 -->
## PAGE 00820: Working with Relation Map

- page_id: `249573526`
- space_key: `DEVG`
- source_url: https://docs.nomagic.com/spaces/DEVG/pages/249573526/Working+with+Relation+Map
- version_number: 1
- version_date: `2023-12-08T15:24:05.277+01:00`
- ancestors: Developer Guides Home > Modeling Tools Developer Guide > UML-based > Working with diagrams
- labels: []

### NORMALIZED CONTENT

A relation map is a diagram with a specific stereotype. It is used to represent the element properties in a relation based form.It can represent elements connected via various relation criteria

The Open API of our modeling tools provides the**com.nomagic.magicdraw.visualization.relationshipmap.RelationshipMapUtilities****to work with Relation maps.

**Refreshing relation map**

To refresh the relation map, use the RelationshipMapUtilities.refreshMap(Diagram) method:

```java

```

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><span>A relation map is a diagram with a specific stereotype. It is used to represent the element properties in a relation based form.It can represent elements connected via various relation criteria</span></p><p><span>The Open API of our modeling tools provides the<em> </em>com.nomagic.magicdraw.visualization.relationshipmap.RelationshipMapUtilities<strong>  </strong>to work with Relation maps.</span></p><p class="auto-cursor-target"><br /></p><p><br /></p><p><span><strong>Refreshing relation map<br /></strong></span></p><p>To refresh the relation map, use the RelationshipMapUtilities.refreshMap(Diagram) method:</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="d0465c4b-41d4-413a-8088-961710f0f49a"><ac:parameter ac:name="language">java</ac:parameter><ac:plain-text-body><![CDATA[RelationshipMapUtilities.refreshMap(diagram)]]></ac:plain-text-body></ac:structured-macro><p class="auto-cursor-target"><br /><br /></p>
````

<!--NOMAGIC_PAGE id=249573447 space=DEVG version=1 -->
## PAGE 00821: Working with stereotypes and tagged values

- page_id: `249573447`
- space_key: `DEVG`
- source_url: https://docs.nomagic.com/spaces/DEVG/pages/249573447/Working+with+stereotypes+and+tagged+values
- version_number: 1
- version_date: `2024-02-13T09:40:20.796+01:00`
- ancestors: Developer Guides Home > Modeling Tools Developer Guide > UML-based
- labels: ['stereotypes-helper', 'helper-class']

### NORMALIZED CONTENT

Standard UML metamodel is extended with additional meta-classes and meta-properties to support stereotypes applications.

[IMAGE alt='' src='']

There are two ways to work with stereotypes applications

- We provide a com.nomagic.uml2.ext.jmi.helpers.StereotypesHelper helper class for hiding this mapping complexity. It has set of useful methods for assigning or unassigning stereotypes, creating TaggedValues
- Use profile implementation classes

#### PANEL: Related pages

Related pages

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p> Standard UML metamodel is extended with additional meta-classes and meta-properties to support stereotypes applications.</p><p><ac:image ac:height="400"><ri:attachment ri:filename="image2020-3-12_9-29-28.png" /></ac:image></p><p>There are two ways to work with stereotypes applications</p><ul><li>We provide a <em>com.nomagic.uml2.ext.jmi.helpers.StereotypesHelper</em> helper class  for hiding this mapping complexity. It has set of useful methods for assigning or unassigning stereotypes, creating <em style="line-height: 1.4285715;">TaggedValues</em></li><li>Use profile implementation classes</li></ul><p><br /></p></ac:layout-cell><ac:layout-cell><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="c8695294-59d4-411e-80f7-18d01b1e07b6"><ac:parameter ac:name="title">Related pages</ac:parameter><ac:rich-text-body><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="428cfc7e-97da-4269-aec3-ce828becf8cb" /></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=301367378 space=DEVG version=11 -->
## PAGE 00822: Working with SysML v2 Projects

- page_id: `301367378`
- space_key: `DEVG`
- source_url: https://docs.nomagic.com/spaces/DEVG/pages/301367378/Working+with+SysML+v2+Projects
- version_number: 11
- version_date: `2026-04-17T07:41:56.933+02:00`
- ancestors: Developer Guides Home > Modeling Tools Developer Guide > SysML v2
- labels: []

### NORMALIZED CONTENT

This section describes how to use the Open API to manage SysML v2 projects:

- Create a local repository project (UPS)
- Create a Teamwork Cloud (TWC) project
- Open an existing TWC project
- Open the locally stored project in the local repository (UPS)

#### Overview

SysML v2 project workflows typically involve two environments:

- [CONFLUENCE_PAGE title='Local Repository' space=''] — used for working with projects locally
- [CONFLUENCE_PAGE title='Teamwork Cloud' space=''] — used for collaborative project storage and access

#### Best Practices

- Validate project existence before opening
- Handle exceptions related to TWC connectivity and authentication
- Keep local repository (UPS) and collaborative (TWC) workflows clearly separated

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>This section describes how to use the Open API to manage SysML v2 projects:</p><ul><li>Create a local repository project (UPS)</li><li>Create a Teamwork Cloud (TWC) project</li><li>Open an existing TWC project</li><li>Open the locally stored project in the local repository (UPS)</li></ul><h2>Overview</h2><p>SysML v2 project workflows typically involve two environments:</p><ul><li><strong><ac:link><ri:page ri:content-title="Local Repository" /></ac:link></strong> — used for working with projects locally</li><li><strong><ac:link><ri:page ri:content-title="Teamwork Cloud" /><ac:plain-text-link-body><![CDATA[Teamwork Cloud (TWC)]]></ac:plain-text-link-body></ac:link></strong> — used for collaborative project storage and access</li></ul><h2>Best Practices</h2><ul><li>Validate project existence before opening</li><li>Handle exceptions related to TWC connectivity and authentication</li><li>Keep local repository (UPS) and collaborative (TWC) workflows clearly separated</li></ul>
````

<!--NOMAGIC_PAGE id=249573349 space=DEVG version=1 -->
## PAGE 00823: Working with test resources

- page_id: `249573349`
- space_key: `DEVG`
- source_url: https://docs.nomagic.com/spaces/DEVG/pages/249573349/Working+with+test+resources
- version_number: 1
- version_date: `2024-02-13T09:57:27.813+01:00`
- ancestors: Developer Guides Home > Modeling Tools Developer Guide > General > Plugins > Creating test cases
- labels: []

### NORMALIZED CONTENT

Test cases may use external resources such as configuration files and projects for testing purposes. It is recommended to keep external test resources apart from test case implementation class files. The test framework provides methods for retrieving test resources from the one specific resource directory.

Resource directory can be accessed by calling the *com.nomagic.magicdraw.tests.common.TestEnvironment.getResourceDir()* method. This method obtains the directory specified by the *tests.resources* system property. For information about specifying the *tests.resources* system property see [CONFLUENCE_PAGE title='Configure test environment' space='']. The test framework also provides methods for collecting projects from the resource directory. Developers may use *TestEnvironment.getProjects(java.io.File)* for collecting projects recursively from a specific directory. Unnecessary projects can be filtered out by specifying their names in *skip.txt* files that are placed in the same directory as project files.

Test cases may produce some resources as a test output. The output directory for a specific test case can be created using *TestEnvironment.getOutputDir(java.lang.Class)*. The class here specifies a class of the test case which output directory should be accessed.

There are also methods for working with output files. An output file for a specific project can be simply created by changing the project file extension (*TestEnvironment.getFileWithExtension(java.io.File, java.lang.String)*) or adding a special prefix to its name (*TestEnvironment.createFileNameWithPrefix(**java.io.File, java.lang.String)* ).

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><div class="WordSection1"><p>Test cases may use external resources such as configuration files and projects for testing purposes. It is recommended to keep external test resources apart from test case implementation class files. The test framework provides methods for retrieving test resources from the one specific resource directory.</p><p>Resource directory can be accessed by calling the <em>com.nomagic.magicdraw.tests.common.TestEnvironment.getResourceDir()</em> method. This method obtains the directory specified by the <em>tests.resources</em> system property. For information about specifying the <em>tests.resources</em> system property see <ac:link><ri:page ri:content-title="Configure test environment" /></ac:link>. The test framework also provides methods for collecting projects from the resource directory. Developers may use <em>TestEnvironment.getProjects(java.io.File)</em> for collecting projects recursively from a specific directory. Unnecessary projects can be filtered out by specifying their names in <em>skip.txt</em> files that are placed in the same directory as project files.</p><p>Test cases may produce some resources as a test output. The output directory for a specific test case can be created using <em>TestEnvironment.getOutputDir(java.lang.Class)</em>. The class here specifies a class of the test case which output directory should be accessed.</p><p>There are also methods for working with output files. An output file for a specific project can be simply created by changing the project file extension (<em>TestEnvironment.getFileWithExtension(java.io.File, java.lang.String)</em>) or adding a special prefix to its name (<em>TestEnvironment.createFileNameWithPrefix(</em><em>java.io.File, java.lang.String)</em> ).</p></div></ac:layout-cell><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=314182067 space=DEVG version=11 -->
## PAGE 00824: Working with Textual Editor Content

- page_id: `314182067`
- space_key: `DEVG`
- source_url: https://docs.nomagic.com/spaces/DEVG/pages/314182067/Working+with+Textual+Editor+Content
- version_number: 11
- version_date: `2026-06-30T22:36:27.269+02:00`
- ancestors: Developer Guides Home > Modeling Tools Developer Guide > SysML v2 > SysML v2 Textual Support
- labels: []

### NORMALIZED CONTENT

#### Overview

This guide explains how to interact with the **SysML textual editor** using the [**SysMLTextualNotationUtils**](https://jdocs.nomagic.com/2026xRefresh2/com/dassault_systemes/modeler/magic/sysml/textual/texteditor/ui/SysMLTextualNotationUtils.html)API.

#### Preconditions

The textual editor must be opened before accessing content

```text

```

#### Reading Editor Content

Retrieves the current textual content from the active editor associated with a given model element.

- Returns the editor content as a String
- Returns null if the editor is not open

```java

```

#### Updating Editor Content

Updates the textual content in the active editor for a given model element.

- Replaces the existing editor content with the provided text
- Works only when an editor instance is active
- Does not automatically persist changes to the model

```java

```

#### End-to-End Example

```text

```

#### Common Pitfalls

- Attempting to read content without opening the editor
- Overwriting content without reading existing text
- Assuming changes are automatically persisted

### EXACT CONFLUENCE STORAGE SOURCE

````html
<h2>Overview</h2><p>This guide explains how to interact with the <strong>SysML textual editor</strong> using the <a href="https://jdocs.nomagic.com/2026xRefresh2/com/dassault_systemes/modeler/magic/sysml/textual/texteditor/ui/SysMLTextualNotationUtils.html"><strong>SysMLTextualNotationUtils</strong> </a>API.</p><h2>Preconditions</h2><p>The textual editor must be opened before accessing content</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="f2e8da5c-6754-4cfa-9f73-38ef2a02cff4"><ac:plain-text-body><![CDATA[import com.dassault_systemes.modeler.kerml.model.kerml.Element;
import com.dassault_systemes.modeler.magic.sysml.textual.texteditor.ui.SysMLTextualNotationUtils;

Element element = ...; // model element
SysMLTextualNotationUtils.openTextualEditor(element);
]]></ac:plain-text-body></ac:structured-macro><h2>Reading Editor Content</h2><p>Retrieves the current textual content from the active editor associated with a given model element.</p><ul><li>Returns the editor content as a <strong>String</strong></li><li>Returns <strong>null</strong> if the editor is not open</li></ul><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="91681f12-e535-439f-aaf7-f329a6030497"><ac:parameter ac:name="language">java</ac:parameter><ac:plain-text-body><![CDATA[import com.dassault_systemes.modeler.kerml.model.kerml.Element;
import com.dassault_systemes.modeler.magic.sysml.textual.texteditor.ui.SysMLTextualNotationUtils;

Element element = ...; // model element
String content = SysMLTextualNotationUtils.getEditorContent(element);]]></ac:plain-text-body></ac:structured-macro><h2>Updating Editor Content</h2><p>Updates the textual content in the active editor for a given model element.</p><ul><li>Replaces the existing editor content with the provided text</li><li>Works only when an editor instance is active</li><li>Does not automatically persist changes to the model</li></ul><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="5d1da7b6-fa07-4daa-985c-878d7214151f"><ac:parameter ac:name="language">java</ac:parameter><ac:plain-text-body><![CDATA[import com.dassault_systemes.modeler.kerml.model.kerml.Element;
import com.dassault_systemes.modeler.magic.sysml.textual.texteditor.ui.SysMLTextualNotationUtils;

String updatedContent = ...; // new content
SysMLTextualNotationUtils.setEditorContent(element, updatedContent);]]></ac:plain-text-body></ac:structured-macro><h2>End-to-End Example</h2><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="89fcbac8-9cbd-4062-bba6-66ac8b3a377b"><ac:parameter ac:name="">java</ac:parameter><ac:plain-text-body><![CDATA[import com.dassault_systemes.modeler.kerml.model.kerml.Element;
import com.dassault_systemes.modeler.magic.sysml.textual.texteditor.ui.SysMLTextualNotationUtils;

Element element = ...; // obtain model element

// Open the textual editor
SysMLTextualNotationUtils.openTextualEditor(element);

// Read current editor content
String content = SysMLTextualNotationUtils.getEditorContent(element);

if (content != null) 
{
	// Modify the content
	String updatedContent =
        content +
        "\n\n// --- Updated via API ---\n" +
        "part def PartType;\n" +
        "block SampleBlock {\n" +
        "   part p1 : PartType;\n" +
        "}";

	// Update the editor content
	SysMLTextualNotationUtils.setEditorContent(element, updatedContent);

	System.out.println("Editor content successfully updated.");
}
]]></ac:plain-text-body></ac:structured-macro><h2>Common Pitfalls</h2><ul><li>Attempting to read content without opening the editor</li><li>Overwriting content without reading existing text</li><li>Assuming changes are automatically persisted</li></ul>
````

<!--NOMAGIC_PAGE id=304015669 space=DEVG version=11 -->
## PAGE 00825: Working with the Presentation Element Styles

- page_id: `304015669`
- space_key: `DEVG`
- source_url: https://docs.nomagic.com/spaces/DEVG/pages/304015669/Working+with+the+Presentation+Element+Styles
- version_number: 11
- version_date: `2026-05-14T22:52:05.712+02:00`
- ancestors: Developer Guides Home > Modeling Tools Developer Guide > SysML v2 > Working With Model > Managing Presentation Elements
- labels: []

### NORMALIZED CONTENT

#### Overview

Use presentation element styles to customize the visual appearance of diagram symbols programmatically, such as colors, fonts, compartments, visibility, or rendering-specific behavior.

In SysML v2 diagrams, the visual appearance of a symbol is controlled by style elements associated with it.

The**[PresentationElementsManager](https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/sysml/diagram/PresentationElementsManager.html)**provides the standard API entry point for modifying style attributes of presentation elements.

Typical use cases include:

- changing fill color
- changing line color
- changing font settings
- changing element-specific appearance
- changing compartment-specific appearance

StyleElements should only be modified using the **[PresentationElementsManager](https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/sysml/diagram/PresentationElementsManager.html)**class.

The call [PresentationElementsManager.changeStyle(...)](https://jdocs.nomagic.com/2026xRefresh2/com/dassault_systemes/modeler/sysml/diagram/PresentationElementsManager.html#changeStyle(com.nomagic.magicdraw.uml.symbols.PresentationElement,java.lang.Class,java.util.function.Consumer)) modifies the 'explicitly set attribute values' of the style element.

This ensures that style updates are applied at the correct layer and remain fully consistent with the internal style resolution model.

#### Presentation element style structure:

A single presentation element is made up of 3 style elements.

Each style element controls a specific aspect of the symbol’s visual appearance. Because of this, style changes should target the most appropriate style type instead of always modifying only the general symbol style.

Typical examples include:

- `SymbolStyle` — general visual properties of the symbol(e.g. fill color, pen color etc.)
- ElementStyle — specific properties to an element (e.g. an element that uses ElementStyle can show a name, or an element that uses a FeatureStyle(more specific ElementStyle class) can show values or inherited sign)
- CompartmentStyle — specific properties to a particular compartment

A single symbol may therefore contain several style objects, each representing a different visual concern.

##### Selecting the Correct Style Type

Use the style type that owns the property you want to change.

- If you want to modify a general symbol-level property such as fill color or line color, use SymbolStyle .
- If you want to modify an element-specific property , use the corresponding [ElementStyle](https://jdocs.nomagic.com/2026xRefresh2/com/dassault_systemes/modeler/kerml/view/style/kermlstyles/ElementStyle.html) style class
- If you want to modify a compartment-specific property , use the corresponding compartment style class.

Using the most specific style type keeps updates precise and avoids unintended changes to unrelated visual properties.

#### Changing the explicit Style attribute values of a Presentation Element

The primary API entry point is: [PresentationElementsManager.changeStyle](https://jdocs.nomagic.com/2026xRefresh2/com/dassault_systemes/modeler/sysml/diagram/PresentationElementsManager.html#changeStyle(com.nomagic.magicdraw.uml.symbols.PresentationElement,java.lang.Class,java.util.function.Consumer))

This method:

1. locates the requested style type on the presentation element
2. retrieves the StyleElement instance
3. applies the requested modification

##### Basic Example

```text
style.setFillColor(Color.RED));
]]>
```

In this example:

- symbol is the target presentation element
- [SymbolStyle.class](https://jdocs.nomagic.com/2026xRefresh2/com/dassault_systemes/modeler/kerml/view/style/kermlstyles/SymbolStyle.html) specifies which StyleElement type should be modified
- The lambda applies the style update

##### Example: General Symbol Style

```text
style.setFillColor(Color.RED));
]]>
```

##### Example: Feature-Specific Style

```text
{
            // feature-specific style changes
        });
]]>
```

##### Example: Compartment-Specific Style

```text
{
			style.setShowFullText(true);
			style.setShowInheritedSign(true);
		});
]]>
```

##### Recommended Practice

When working with presentation elements, first identify which style element owns the property you want to modify.

As a general rule:

- use [SymbolStyle](https://jdocs.nomagic.com/2026xRefresh2/com/dassault_systemes/modeler/kerml/view/style/kermlstyles/SymbolStyle.html) for symbol-wide appearance
- use ElementStyle for element-related appearance
- use the corresponding compartment style class for compartment-related appearance

### EXACT CONFLUENCE STORAGE SOURCE

````html
<h2>Overview</h2><p>Use presentation element styles to customize the visual appearance of diagram symbols programmatically, such as colors, fonts, compartments, visibility, or rendering-specific behavior.</p><p>In SysML v2 diagrams, the visual appearance of a symbol is controlled by style elements associated with it.</p><p><span style="color:var(--ds-text,#333333);">The </span><strong style="text-align: left;"><a class="external-link" href="https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/sysml/diagram/PresentationElementsManager.html" style="">PresentationElementsManager</a></strong><span style="color:var(--ds-text,#333333);"><span> </span></span>provides the standard API entry point for modifying style attributes of presentation elements.</p><p>Typical use cases include:</p><ul><li>changing fill color</li><li>changing line color</li><li>changing font settings</li><li>changing element-specific appearance</li><li>changing compartment-specific appearance</li></ul><p>StyleElements should only be modified using the <strong style="text-align: left;"><a class="external-link" href="https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/sysml/diagram/PresentationElementsManager.html" style="">PresentationElementsManager</a></strong><span style="color:var(--ds-text,#333333);"><span> </span></span>class. </p><p>The call <a href="https://jdocs.nomagic.com/2026xRefresh2/com/dassault_systemes/modeler/sysml/diagram/PresentationElementsManager.html#changeStyle(com.nomagic.magicdraw.uml.symbols.PresentationElement,java.lang.Class,java.util.function.Consumer)">PresentationElementsManager.changeStyle(...)</a> modifies the 'explicitly set attribute values' of the style element.</p><p>This ensures that style updates are applied at the correct layer and remain fully consistent with the internal style resolution model.</p><h2>Presentation element style structure:</h2><p>A single presentation element is made up of 3 style elements.</p><p>Each style element controls a specific aspect of the symbol’s visual appearance. Because of this, style changes should target the most appropriate style type instead of always modifying only the general symbol style.</p><p>Typical examples include:</p><ul><li data-uuid="2f9ed3f0-82fd-4c5d-81f8-f3b5ff030ac8"><a href="https://jdocs.nomagic.com/2026xRefresh2/com/dassault_systemes/modeler/kerml/view/style/kermlstyles/SymbolStyle.html"><code>SymbolStyle</code> </a>— general visual properties of the symbol(e.g. fill color, pen color etc.)</li><li data-uuid="c783d23f-23ca-4726-975b-4f541a48231c"><a href="https://jdocs.nomagic.com/2026xRefresh2/com/dassault_systemes/modeler/kerml/view/style/kermlstyles/ElementStyle.html">ElementStyle</a>— specific properties to an element (e.g. an element that uses ElementStyle can show a name, or an element that uses a FeatureStyle(more specific ElementStyle class) can show values or inherited sign)</li><li data-uuid="f769d2b9-cd1d-477b-866b-944c501d278b"><a href="https://jdocs.nomagic.com/2026xRefresh2/com/dassault_systemes/modeler/kerml/view/style/kermlstyles/CompartmentStyle.html">CompartmentStyle </a>— specific properties to a particular compartment</li></ul><p>A single symbol may therefore contain several style objects, each representing a different visual concern.</p><h3>Selecting the Correct Style Type</h3><p>Use the style type that owns the property you want to change.</p><ul><li data-uuid="37e979fe-2416-4b16-9bfe-b611f2941ef2">If you want to modify a <strong>general symbol-level property</strong> such as fill color or line color, use <code>SymbolStyle</code>.</li><li data-uuid="08152683-6a67-407d-b186-679c40e6b523">If you want to modify an <strong>element-specific property</strong>, use the corresponding <strong><a href="https://jdocs.nomagic.com/2026xRefresh2/com/dassault_systemes/modeler/kerml/view/style/kermlstyles/ElementStyle.html">ElementStyle</a> style class</strong></li><li data-uuid="c0c219f5-729d-4555-ba8a-5a8b6250b2e3">If you want to modify a <strong>compartment-specific property</strong>, use the corresponding compartment style class.</li></ul><p>Using the most specific style type keeps updates precise and avoids unintended changes to unrelated visual properties.</p><h2>Changing the explicit Style attribute values of a Presentation Element</h2><p>The primary API entry point is: <a href="https://jdocs.nomagic.com/2026xRefresh2/com/dassault_systemes/modeler/sysml/diagram/PresentationElementsManager.html#changeStyle(com.nomagic.magicdraw.uml.symbols.PresentationElement,java.lang.Class,java.util.function.Consumer)">PresentationElementsManager.changeStyle</a></p><p>This method:</p><ol><li>locates the requested style type on the presentation element</li><li>retrieves the StyleElement instance</li><li>applies the requested modification</li></ol><h3>Basic Example</h3><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="60a3e40a-db04-43fb-b5b5-157ce198d407"><ac:parameter ac:name="">java</ac:parameter><ac:plain-text-body><![CDATA[import com.dassault_systemes.modeler.kerml.view.style.kermlstyles.SymbolStyle;
import com.dassault_systemes.modeler.sysml.diagram.PresentationElementsManager;
import java.awt.*;

PresentationElementsManager manager = PresentationElementsManager.getInstance();

manager.changeStyle(symbol, SymbolStyle.class, style -> style.setFillColor(Color.RED));
]]></ac:plain-text-body></ac:structured-macro><p>In this example:</p><ul><li><code>symbol</code> is the target presentation element</li><li><code><a href="https://jdocs.nomagic.com/2026xRefresh2/com/dassault_systemes/modeler/kerml/view/style/kermlstyles/SymbolStyle.html">SymbolStyle.class</a></code> specifies which StyleElement type should be modified</li><li>The lambda applies the style update</li></ul><h3>Example: General Symbol Style</h3><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="098a564a-c206-44c3-aed6-e24a85fefa03"><ac:parameter ac:name="">java</ac:parameter><ac:plain-text-body><![CDATA[import com.dassault_systemes.modeler.kerml.view.style.kermlstyles.SymbolStyle;
import com.dassault_systemes.modeler.sysml.diagram.PresentationElementsManager;
import java.awt.*;

PresentationElementsManager manager = PresentationElementsManager.getInstance();

manager.changeStyle(symbol, SymbolStyle.class, style -> style.setFillColor(Color.RED));
]]></ac:plain-text-body></ac:structured-macro><h3>Example: Feature-Specific Style</h3><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="11e9b44b-16e3-400f-97cc-8a6d787eaa06"><ac:parameter ac:name="">java</ac:parameter><ac:plain-text-body><![CDATA[import com.dassault_systemes.modeler.kerml.view.style.kermlstyles.FeatureStyle;
import com.dassault_systemes.modeler.sysml.diagram.PresentationElementsManager;


PresentationElementsManager manager = PresentationElementsManager.getInstance();

 manager.changeStyle(symbol, FeatureStyle.class,
        style -> {
            // feature-specific style changes
        });
]]></ac:plain-text-body></ac:structured-macro><h3>Example: Compartment-Specific Style</h3><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="fd40dbfc-7e0c-4af3-8c92-f3701606901b"><ac:parameter ac:name="">java</ac:parameter><ac:plain-text-body><![CDATA[import com.dassault_systemes.modeler.sysml.view.style.sysmlstyles.AttributesCompartmentStyle;
import com.dassault_systemes.modeler.sysml.diagram.PresentationElementsManager;

PresentationElementsManager manager = PresentationElementsManager.getInstance();

manager.changeStyle(operatorShape, AttributesCompartmentStyle.class, style -> {
			style.setShowFullText(true);
			style.setShowInheritedSign(true);
		});
]]></ac:plain-text-body></ac:structured-macro><h3>Recommended Practice</h3><p>When working with presentation elements, first identify which style element owns the property you want to modify.</p><p>As a general rule:</p><ul><li>use <code><a href="https://jdocs.nomagic.com/2026xRefresh2/com/dassault_systemes/modeler/kerml/view/style/kermlstyles/SymbolStyle.html">SymbolStyle</a></code> for symbol-wide appearance</li><li>use <a href="https://jdocs.nomagic.com/2026xRefresh2/com/dassault_systemes/modeler/kerml/view/style/kermlstyles/ElementStyle.html">ElementStyle</a> for element-related appearance</li><li>use the corresponding <a href="https://jdocs.nomagic.com/2026xRefresh2/com/dassault_systemes/modeler/kerml/view/style/kermlstyles/CompartmentStyle.html">compartment style</a> class for compartment-related appearance</li></ul>
````

<!--NOMAGIC_PAGE id=249573409 space=DEVG version=1 -->
## PAGE 00826: Working with UML model

- page_id: `249573409`
- space_key: `DEVG`
- source_url: https://docs.nomagic.com/spaces/DEVG/pages/249573409/Working+with+UML+model
- version_number: 1
- version_date: `2023-12-08T15:23:57.477+01:00`
- ancestors: Developer Guides Home > Modeling Tools Developer Guide > UML-based
- labels: []

### NORMALIZED CONTENT

trueh4

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="3a046f2e-f011-496e-a6b9-12c2589ee797"><ac:parameter ac:name="all">true</ac:parameter><ac:parameter ac:name="style">h4</ac:parameter></ac:structured-macro></p></ac:layout-cell><ac:layout-cell><p> </p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=249573325 space=DEVG version=1 -->
## PAGE 00827: Writing plugins

- page_id: `249573325`
- space_key: `DEVG`
- source_url: https://docs.nomagic.com/spaces/DEVG/pages/249573325/Writing+plugins
- version_number: 1
- version_date: `2024-02-13T10:16:18.698+01:00`
- ancestors: Developer Guides Home > Modeling Tools Developer Guide > General > Plugins
- labels: []

### NORMALIZED CONTENT

With this example, we will create a plugin that displays a message on the program startup. To create the plugin, you need to write a plugin descriptor.

###### **Step** **#1:** **Create** **your** **plugin** **folder** **in** **a** *plugins* **folder**

Create a *myplugin* folder in the *plugins* folder in the installation directory of the modeling tool.

###### **Step** **#2:** **Write** **a plugin** **code**

The plugin must contain at least one class derived from the *com.nomagic.magicdraw.plugins.Plugin* class.

```java

```

This plugin shows the one message when it is initialized, and another message when it is closed.

###### **Step #3: Compile and pack the plugin to a *.jar* file**

For more information on the classpath specification details, see [CONFLUENCE_PAGE title='Compilation classpath' space=''].

The compiled code must be packed to a *.jar* file.

To create a .jar file, use a jar command in the plugins directory:

```bash

```

###### **Step #4: Write a plugin descriptor**

The plugin descriptor is a file named*plugin.xml*. This file should be placed in the *myplugin* folder.

```xml
]]>
```

For detailed information about the plugin descriptor, see [CONFLUENCE_PAGE title='Plugin descriptor' space=''].

#### PANEL: Related pages

Related pages

- [CONFLUENCE_PAGE title='Compilation classpath' space='']
- [CONFLUENCE_PAGE title='Plugin descriptor' space='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p>With this example, we will create a plugin that displays a message on the program startup. To create the plugin, you need to write a plugin descriptor.</p><h4><br /><strong>Step</strong> <strong>#1:</strong> <strong>Create</strong> <strong>your</strong> <strong>plugin</strong> <strong>folder</strong> <strong>in</strong> <strong>a</strong> <em>plugins</em> <strong>folder</strong></h4><p>Create a <em>myplugin</em> folder in the <em>plugins</em> folder in the installation directory of the modeling tool.</p><h4><br class="atl-forced-newline" /><strong>Step</strong> <strong>#2:</strong> <strong>Write</strong> <strong>a plugin</strong> <strong>code</strong></h4><p>The plugin must contain at least one class derived from the <em>com.nomagic.magicdraw.plugins.Plugin</em> class.</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="c123c8e2-6dac-4853-90a4-0c0609196328"><ac:parameter ac:name="language">java</ac:parameter><ac:plain-text-body><![CDATA[package myplugin;
import com.nomagic.magicdraw.plugins.Plugin;
import javax.swing.*;
public class MyPlugin extends Plugin
{
    @Override
    public void init()
    {
        JOptionPane.showMessageDialog(null, "My Plugin init");
    }
    @Override
    public boolean close()
    {
        JOptionPane.showMessageDialog( null, "My Plugin close"); 
        return true;
    }
    @Override
    public boolean isSupported()
    {
        //plugin can check here for specific conditions
        //if false is returned plugin is not loaded.
        return true;
    }
}

]]></ac:plain-text-body></ac:structured-macro><p>This plugin shows the one message when it is initialized, and another message when it is closed.</p><h4><strong>Step #3: Compile and pack the plugin to a <em>.jar</em> file </strong></h4><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="385a8e42-7013-49ba-a45a-6987c7292678"><ac:rich-text-body><p><span>For more information on the classpath specification details, see <ac:link><ri:page ri:content-title="Compilation classpath" /><ac:plain-text-link-body><![CDATA[Classpath]]></ac:plain-text-link-body></ac:link>.</span></p></ac:rich-text-body></ac:structured-macro><p>The compiled code must be packed to a <em>.jar</em> file.</p><p>To create a .jar file, use a jar command in the plugins directory:</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="88154e09-3d7e-4879-8b3d-0aa3d34d8672"><ac:parameter ac:name="language">bash</ac:parameter><ac:plain-text-body><![CDATA[ jar -cf myplugin.jar myplugin/*.class]]></ac:plain-text-body></ac:structured-macro><h4><strong>Step #4: Write a plugin descriptor</strong></h4><p>The plugin descriptor is a file named<em> plugin.xml</em>. This file should be placed in the <em>myplugin</em> folder.</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="8026d05b-3932-4e9a-800e-4ac970f3f541"><ac:parameter ac:name="language">xml</ac:parameter><ac:plain-text-body><![CDATA[<?xml version="1.0" encoding="UTF-8"?>
<plugin id="my.first.plugin" name="My First Plugin" version="1.0" provider-name="Coder" class="myplugin.MyPlugin"> 
    <requires>
        <api version="1.0"/>
    </requires> 
    <runtime>
        <library name="myplugin.jar"/>
    </runtime>
</plugin>]]></ac:plain-text-body></ac:structured-macro><p>For detailed information about the plugin descriptor, see <ac:link><ri:page ri:content-title="Plugin descriptor" /></ac:link>.</p></ac:layout-cell><ac:layout-cell><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="8f28f0cc-f589-4636-9cbc-3542147b42a9"><ac:parameter ac:name="title">Related pages</ac:parameter><ac:rich-text-body><ul><li><ac:link><ri:page ri:content-title="Compilation classpath" /></ac:link></li><li><ac:link><ri:page ri:content-title="Plugin descriptor" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````
