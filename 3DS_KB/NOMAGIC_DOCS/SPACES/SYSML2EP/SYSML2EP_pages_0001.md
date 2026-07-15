# NOMAGIC DOCUMENTATION SPACE: SysML v2 Model Execution

<!--NOMAGIC_SPACE key=SYSML2EP chunk=1 -->

<!--NOMAGIC_PAGE id=304014952 space=SYSML2EP version=1 -->
## PAGE 00001: (2026x Refresh1) Clearing runtime values

- page_id: `304014952`
- space_key: `SYSML2EP`
- source_url: https://docs.nomagic.com/spaces/SYSML2EP/pages/304014952/2026x+Refresh1+Clearing+runtime+values
- version_number: 1
- version_date: `2026-04-29T17:11:15.820+02:00`
- ancestors: Versions of SysML v2 Evaluation Plugin Documentation > (2026x Refresh1) SysML v2 Evaluation Plugin Documentation > (2026x Refresh1) User guide
- labels: []

### NORMALIZED CONTENT

After [CONFLUENCE_PAGE title='(2026x Refresh1) Evaluating model elements' space=''], the runtime values are stored in memory and reused for further evaluations, as shown in the example below.

#### PANEL: Example

Example

attributemyNumber:Real= randomNumberGen();//The script that returns a random number is envoked. 
attributemyNewNumber:Real=myNumber+5;//The generated number is reused. Using the myNumber attribute will not trigger the generation of a new number.

The runtime values stored in memory are cleared when you do the following:

- Modify the model.
- Clear values using the view toolbar.
- Clear values using the SysML v2 Model Evaluation console.

##### Clearing values via the view toolbar

If you evaluated model elements using views, you can use the view toolbar to clear the runtime values.

To clear runtime values via the view toolbar

- In the view toolbar, click the arrow next to [ATTACHMENT filename='evaluate_button.png'] and select Clear Values . [ATTACHMENT filename='clearing_values_via_diagram_toolbar.png']

##### Clearing values via the SysML v2 Model Evaluation console

You can use the **SysML v2 Model Evaluation** console to clear runtime values, regardless of where you initiated model evaluation.

To clear runtime values via the **SysML v2 Model Evaluation** console

- In the SysML v2 Model Evaluation console toolbar, click [ATTACHMENT filename='clear_values_icon.png'] . [ATTACHMENT filename='clearing_values_via_console.png']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p style="text-align: left;">After <ac:link><ri:page ri:content-title="(2026x Refresh1) Evaluating model elements" /><ac:plain-text-link-body><![CDATA[model evaluation]]></ac:plain-text-link-body></ac:link>, the runtime values are stored in memory and reused for further evaluations, as shown in the example below.</p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="ef3e74a2-bf68-44a4-b050-97a1a91a7464"><ac:parameter ac:name="title">Example</ac:parameter><ac:rich-text-body><p><span style="color:var(--ds-text-accent-blue,#0055cc);">attribute</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">myNumber</span><span style="color:var(--ds-text,#000000);"> : </span><span style="color:var(--ds-text-accent-teal,#206a83);">Real</span><span style="color:var(--ds-text,#000000);"> = randomNumberGen(); </span><span style="color:var(--ds-text-accent-green-bolder,#164b35);">//The script that returns a random number is envoked.</span><br /><span style="color:var(--ds-text-accent-blue,#0055cc);">attribute</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">myNewNumber</span><span style="color:var(--ds-text,#000000);"> : </span><span style="color:var(--ds-text-accent-teal,#206a83);">Real</span><span style="color:var(--ds-text,#000000);"> = </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">myNumber</span><span style="color:var(--ds-text,#000000);"> + </span><span style="color:var(--ds-background-accent-green-bolder,#1f845a);">5</span><span style="color:var(--ds-text,#000000);">; </span><span style="color:var(--ds-text-accent-green-bolder,#164b35);">//The generated number is reused. Using the myNumber attribute will not trigger the generation of a new number.</span></p></ac:rich-text-body></ac:structured-macro><p class="code-java"><br />The runtime values stored in memory are cleared when you do the following:</p><ul style="text-align: left;"><li data-uuid="8ff056d2-95cb-44f0-9a0a-054b56c03b03">Modify the model.</li><li data-uuid="35f61a9c-55da-4192-baed-52651842ac88">Clear values using the view toolbar.</li><li data-uuid="44eaa21a-8137-4733-8643-06d60ec5967d">Clear values using the <strong>SysML v2 Model Evaluation</strong> console.</li></ul><h3 style="text-align: left;">Clearing values via the view toolbar</h3><p>If you evaluated model elements using views, you can use the view toolbar to clear the runtime values.</p><p>To clear runtime values via the view toolbar</p><hr /><ul><li data-uuid="1da4ccf3-9a89-40cb-98ec-3f418f12e353">In the view toolbar, click the arrow next to <ac:image ac:thumbnail="true" ac:height="14"><ri:attachment ri:filename="evaluate_button.png"><ri:page ri:content-title="(2026x Refresh1) Clearing runtime values" /></ri:attachment></ac:image> and select <strong>Clear Values</strong>.<br /><ac:image><ri:attachment ri:filename="clearing_values_via_diagram_toolbar.png"><ri:page ri:content-title="(2026x Refresh1) Clearing runtime values" /></ri:attachment></ac:image></li></ul><h3>Clearing values via the SysML v2 Model Evaluation console</h3><p>You can use the <strong>SysML v2 Model Evaluation</strong> console to clear runtime values, regardless of where you initiated model evaluation.</p><p>To clear runtime values via the <strong>SysML v2 Model Evaluation</strong> console</p><hr /><ul><li data-uuid="f13a5e93-689f-49ba-b2e7-8d8b074746c7">In the <strong>SysML v2 Model Evaluation</strong> console toolbar, click <ac:image><ri:attachment ri:filename="clear_values_icon.png"><ri:page ri:content-title="(2026x Refresh1) Clearing runtime values" /></ri:attachment></ac:image>.<br /><ac:image><ri:attachment ri:filename="clearing_values_via_console.png"><ri:page ri:content-title="(2026x Refresh1) Clearing runtime values" /></ri:attachment></ac:image></li></ul>
````

<!--NOMAGIC_PAGE id=304014958 space=SYSML2EP version=1 -->
## PAGE 00002: (2026x Refresh1) Connecting to a running MATLAB session

- page_id: `304014958`
- space_key: `SYSML2EP`
- source_url: https://docs.nomagic.com/spaces/SYSML2EP/pages/304014958/2026x+Refresh1+Connecting+to+a+running+MATLAB+session
- version_number: 1
- version_date: `2026-04-29T17:11:15.927+02:00`
- ancestors: Versions of SysML v2 Evaluation Plugin Documentation > (2026x Refresh1) SysML v2 Evaluation Plugin Documentation > (2026x Refresh1) User guide > (2026x Refresh1) Integration with MATLAB
- labels: ['connecting-to-matlab-session', 'matlab-session']

### NORMALIZED CONTENT

You can connect to a running MATLAB session and use all the variables in the MATLAB workspace.

To connect to a MATLAB session, [CONFLUENCE_PAGE title='(2026x Refresh1) Integration with MATLAB' space=''].

To connect a running MATLAB session

- In the MATLAB command widow, execute the matlab.engine.shareEngine command.

After connecting to a MATLAB session, you can access variables in the MATLAB shared workspace that are not in the SysML v2 model. For example, you can define variables in MATLAB and then use them in calculations in your modeling tool.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>You can connect to a running MATLAB session and use all the variables in the MATLAB workspace.</p><ac:structured-macro ac:macro-id="65f34d32-45d5-43ef-97f4-8ea16e7b1763" ac:name="note" ac:schema-version="1"><ac:rich-text-body><p>To connect to a MATLAB session, <ac:link><ri:page ri:content-title="(2026x Refresh1) Integration with MATLAB" /><ac:plain-text-link-body><![CDATA[MATLAB must be integrated with your modeling tool]]></ac:plain-text-link-body></ac:link>.</p></ac:rich-text-body></ac:structured-macro><p><br /></p><p>To connect <ac:inline-comment-marker ac:ref="c56add26-f5b3-46fc-8fb4-6eef404f8496">a running MATLAB session</ac:inline-comment-marker></p><hr /><ul><li>In the MATLAB command widow, execute the <strong>matlab.engine.shareEngine</strong> command.</li></ul><p class="auto-cursor-target"><br />After connecting to a MATLAB session, you can access variables in the MATLAB shared workspace that are not in the SysML v2 model. For example, you can define variables in MATLAB and then use them in calculations in your modeling tool.</p>
````

<!--NOMAGIC_PAGE id=314180411 space=SYSML2EP version=4 -->
## PAGE 00003: (2026x Refresh1) Displaying evaluation information

- page_id: `314180411`
- space_key: `SYSML2EP`
- source_url: https://docs.nomagic.com/spaces/SYSML2EP/pages/314180411/2026x+Refresh1+Displaying+evaluation+information
- version_number: 4
- version_date: `2026-06-17T09:12:10.149+02:00`
- ancestors: Versions of SysML v2 Evaluation Plugin Documentation > (2026x Refresh1) SysML v2 Evaluation Plugin Documentation > (2026x Refresh1) User guide > (2026x Refresh1) Evaluation information in views
- labels: []

### NORMALIZED CONTENT

##### Displaying runtime values

In views, runtime values are displayed in blue. After evaluation, these runtime values replace the default values and are displayed next to:

- Attributes
- References
- Satisfy requirements

Attributes or references that contain expressions may display calculated values. During the evaluation, views do not display types; only the current runtime values are shown. This reduces visual complexity and improves view readability.

#### INFO: Displaying unit symbols

Displaying unit symbols

When units are assigned directly to literal values, unit symbols are displayed next to runtime values in model views during evaluation. You can assign units using square brackets on literals. For example:

attribute'Mass : MassValue'default:=500[SI::kg];

You can also[CONFLUENCE_PAGE title='(2026x Refresh1) Manipulating runtime values' space='']directly in views and watch as the evaluation results are automatically recalculated.

[IMAGE alt='' src='']

###### A sample view displaying the evaluation results.

INLINE

##### Annotating requirement and constraint verification results

Using views is the quickest way to evaluate multiple requirements and constraints at once. After evaluation, passing and failing values are highlighted in green and red, respectively. In addition, element shapes display specific icons to indicate whether the related requirements and constraints are satisfied.

To evaluate requirements and constraints in views

1. Open the view that displays elements with related requirements and constraints that you want to evaluate.
2. Click [ATTACHMENT filename='evaluate_button.png'] in the view toolbar. To evaluate a single element, select the element shape or an attribute in the shape compartment before completing this step.To evaluate an individual satisfy requirement or assert constraint, select the element shape before completing this step. The evaluation result is *true* or *false*.

The view shapes are highlighted, indicating whether related system requirements and constraints pass or fail.

[IMAGE alt='' src='']

###### A view with annotated requirement verification results. Hovering over a failing value shows the text of the failing requirement.

The following table explains the annotations of requirement and constraint verification results displayed in views.

| Annotation | Description | Tooltip |
| --- | --- | --- |
| ORA shape or its header is colored in green | The annotated elements satisfy related system requirements or constraints. | N/A |
| ORA shape or its header is colored in yellow | The annotated elements indirectly fail related system requirements or constraints. This means that system requirements or constraints are failed by inner parts of the annotated element. | Hover over the icon to see which inner elements fail system requirements or constraints. |
| ORA shape or its header is colored in red | The annotated elements fail related system requirements or constraints. | Hover over the icon to see which requirement or constraint failed. |
|  | The annotated values satisfy related system requirements or constraints. | N/A |
|  | The annotated values fail related system requirements or constraints. | Hover over the value to see the text of the failing requirement. |

###### Customizing the visual representation of verification results

You can customize how requirement and constraint verification results are annotated in views.

To customize the visual representation of the requirement and constraint verification results

1. In the main menu, select Options > Project .
2. In the Project Options dialog, select the Evaluation option group.
3. Specify the following options:
  - Display Verification Results As - Select Display Icons to add icons to shape headers. Select Paint Headers to color shapes or their headers.
  - Propagate Deep Nested Failures - Set to true to indicate nested requirement and constraint failures. Set to false to only highlight the shapes of the elements that directly fail a requirement or constraint.
4. Click OK to close the Project Options dialog.

##### Clearing evaluation results in views

To clear the evaluation results in a view

- In the view toolbar, click an arrow next to [ATTACHMENT filename='evaluate_button.png'] and select Clear Values .

### EXACT CONFLUENCE STORAGE SOURCE

````html
<h3>Displaying runtime values</h3><p style="text-align: left;">In views, runtime values are displayed in blue. After evaluation, these runtime values replace the default values and are displayed next to:</p><ul style="text-align: left;"><li data-uuid="4df9462d-449b-4473-9a1b-66492d2ca634">Attributes</li><li data-uuid="d0c763c8-e720-48d1-832e-627bbb4ba482">References</li><li data-uuid="8bb78bb9-aa0a-4c52-975c-ffb72ab9fdcf">Satisfy requirements</li></ul><p style="text-align: left;">Attributes or references that contain expressions may display calculated values. During the evaluation, views do not display types; only the current runtime values are shown. This reduces visual complexity and improves view readability.</p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="0e991bdb-4fad-4bd9-8d67-a5d3953a41f6"><ac:parameter ac:name="title">Displaying unit symbols</ac:parameter><ac:rich-text-body><p>When units are assigned directly to literal values, unit symbols are displayed next to runtime values in model views during evaluation. You can assign units using square brackets on literals. For example: </p><p><span style="color:var(--ds-text-accent-blue,#0055cc);">attribute</span><span style="color:var(--ds-chart-gray-bold,#8590a2);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">'Mass : MassValue'</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">default</span><span style="color:var(--ds-text,#000000);"> := </span><span style="color:var(--ds-background-accent-green-bolder,#1f845a);">500</span><span style="color:var(--ds-text,#000000);"> [</span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">SI::kg</span><span style="color:var(--ds-text,#000000);">];</span></p></ac:rich-text-body></ac:structured-macro><p style="text-align: left;">You can also<span> </span><ac:link><ri:page ri:content-title="(2026x Refresh1) Manipulating runtime values" /><ac:plain-text-link-body><![CDATA[modify runtime values]]></ac:plain-text-link-body></ac:link><span> </span>directly in views and watch as the <span style="color:var(--ds-text,#172b4d);">evaluation results are automatically recalculated.</span></p><p style="text-align: center;"><span style="color:var(--ds-text,#172b4d);"><ac:image><ri:attachment ri:filename="displaying_runtime_values.png" /></ac:image></span></p><h6 style="text-align: center;"><span style="color:var(--ds-text,#172b4d);">A sample view displaying the evaluation results.</span></h6><ac:structured-macro ac:name="excerpt" ac:schema-version="1" ac:macro-id="14743066-60a6-4d47-833f-6af76e90a237"><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><h3>Annotating requirement and constraint verification results</h3><p>Using views is the quickest way to evaluate multiple requirements and constraints at once. After evaluation, passing and failing values are highlighted in green and red, respectively. In addition, element shapes display specific icons to indicate whether the related requirements and constraints are satisfied.</p><p>To evaluate requirements and constraints in views</p><hr /><ol><li data-uuid="2667b850-9769-42c4-9c9f-d65e35f824aa">Open the view that displays elements with related requirements and constraints that you want to evaluate.</li><li data-uuid="df6ad6d0-d8af-412a-b3e3-e6ac3505c879">Click <ac:image><ri:attachment ri:filename="evaluate_button.png" /></ac:image> in the view toolbar.<br /><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="b4760594-9edc-4ee3-bfd1-320da5a6483f"><ac:rich-text-body><ul><li>To evaluate a single element, select the element shape or an attribute in the shape compartment before completing this step.</li><li>To evaluate an individual satisfy requirement or assert constraint, select the element shape before completing this step. The evaluation result is <em>true</em> or <em>false</em>.</li></ul></ac:rich-text-body></ac:structured-macro></li></ol><p>The view shapes are highlighted, indicating whether related system requirements and constraints pass or fail.</p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="requirement_and_constraint_verification.png" /></ac:image></p><h6 style="text-align: center;">A view with annotated requirement verification results. Hovering over a failing value shows the text of the failing requirement.</h6><p>The following table explains the annotations of requirement and constraint verification results displayed in views.</p><table class="relative-table wrapped" style="width: 85.0804%;"><colgroup><col style="width: 19.8294%;" /><col style="width: 49.12%;" /><col style="width: 31.0506%;" /></colgroup><tbody><tr><th style="text-align: left;">Annotation</th><th>Description</th><th>Tooltip</th></tr><tr><td style="text-align: center;"><div class="content-wrapper"><p><ac:image><ri:attachment ri:filename="pass.png" /></ac:image></p><p>OR</p><p>A shape or its header is colored in green</p></div></td><td>The annotated elements satisfy related system requirements or constraints.</td><td>N/A</td></tr><tr><td style="text-align: center;"><div class="content-wrapper"><p><ac:image><ri:attachment ri:filename="indirect_failure.png" /></ac:image></p><p>OR</p><p>A shape or its header is colored in yellow</p></div></td><td>The annotated elements indirectly fail related system requirements or constraints. This means that system requirements or constraints are failed by inner parts of the annotated element. </td><td>Hover over the icon to see which inner elements fail system requirements or constraints.</td></tr><tr><td style="text-align: center;"><div class="content-wrapper"><p><ac:image><ri:attachment ri:filename="direct_failure.png" /></ac:image></p><p>OR</p><p>A shape or its header is colored in red</p></div></td><td>The annotated elements fail related system requirements or constraints.</td><td>Hover over the icon to see which requirement or constraint failed.</td></tr><tr><td style="text-align: center;"><div class="content-wrapper"><p><ac:image><ri:attachment ri:filename="passing_value.png" /></ac:image></p></div></td><td>The annotated values satisfy related system requirements or constraints.</td><td>N/A</td></tr><tr><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:height="20"><ri:attachment ri:filename="failing_value.png" /></ac:image></p></div></td><td>The annotated values fail related system requirements or constraints.</td><td>Hover over the value to see the text of the failing requirement.</td></tr></tbody></table><h4>Customizing the visual representation of verification results </h4><p><span style="color:var(--ds-text,#172b4d);">You can customize how requirement and constraint verification results are annotated in views.</span></p><p><span style="color:var(--ds-text,#172b4d);">To customize the visual representation of the requirement and constraint verification results</span></p><hr /><ol><li data-uuid="b8d0e243-e5b7-40c0-92ea-cdfe6a4f2283">In the main menu, select <strong>Options</strong> &gt; <strong>Project</strong>.</li><li data-uuid="be670141-33fb-4afe-b4fc-91ea634a6b86">In the <strong>Project Options</strong> dialog, select the <strong>Evaluation</strong> option group.</li><li data-uuid="812485dc-9625-4c7d-99bb-ab108d950f8b">Specify the following options:<ul><li><strong>Display Verification Results As</strong> - Select <strong>Display Icons</strong> to add icons to shape headers. Select <strong>Paint Headers</strong> to color shapes or their headers.</li><li><strong>Propagate Deep Nested Failures</strong> - Set to <em>true</em> to indicate nested requirement and constraint failures. Set to <em>false</em> to only highlight the shapes of the elements that directly fail a requirement or constraint.</li></ul></li><li data-uuid="c32e7d0b-dfbc-4f73-9d14-2fc31c0c1afe">Click <strong>OK</strong> to close the <strong>Project Options</strong> dialog.</li></ol><h3>Clearing evaluation results in views</h3><p>To clear the evaluation results in a view</p><hr /><ul><li data-uuid="ffcc042c-cd58-482b-a79b-9069e9242dce">In the view toolbar, click an arrow next to <ac:image><ri:attachment ri:filename="evaluate_button.png" /></ac:image> and select <strong>Clear Values</strong>.</li></ul></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=304014884 space=SYSML2EP version=4 -->
## PAGE 00004: (2026x Refresh1) Evaluating model elements

- page_id: `304014884`
- space_key: `SYSML2EP`
- source_url: https://docs.nomagic.com/spaces/SYSML2EP/pages/304014884/2026x+Refresh1+Evaluating+model+elements
- version_number: 4
- version_date: `2026-06-17T10:35:41.177+02:00`
- ancestors: Versions of SysML v2 Evaluation Plugin Documentation > (2026x Refresh1) SysML v2 Evaluation Plugin Documentation > (2026x Refresh1) User guide
- labels: []

### NORMALIZED CONTENT

This chapter describes how you can evaluate model elements, e.g., attributes, expressed through general mathematical calculations. When you evaluate a model element, all of its owned and inherited attributes are evaluated as well.

##### Evaluating model elements via the textual notation

To evaluate a model element via the textual notation

1. In the Textual Editor, place the cursor on the element you want to evaluate.
2. In the Textual Editor toolbar, click [ATTACHMENT filename='evaluate_button.png'] . [ATTACHMENT filename='evaluating_element_via_textual_notation.png']

The evaluation results are displayed in the **SysML v2 Model Evaluation** console.

##### Evaluating model elements via the Containment tree

To evaluate a model element via the Containment tree

- Right-click an element in the Containment tree and select Evaluate . [ATTACHMENT filename='evaluating_element_via_containment_tree.png']

The evaluation results are displayed in the **SysML v2 Model Evaluation** console.

##### Evaluating model elements in views

You can use views to evaluate individual model elements or all the elements displayed in a view.

To evaluate a model element in a view

1. Open the view displaying the model elements you want to evaluate.
2. Do one of the following:
  - Select the shapes of the elements you want to evaluate and, in the view toolbar, click [ATTACHMENT filename='evaluate_button.png'] . If you do not select any shapes, all the elements displayed in the view are evaluated. [ATTACHMENT filename='evaluating_from_view_toolbar.png']
  - Right-click an element shape and select Evaluate .
  - Select an element shape and, in the smart manipulator, click [ATTACHMENT filename='evaluate_button.png'] . [ATTACHMENT filename='evaluating_from_smart_manipulator.png']

After evaluation, runtime values are displayed in blue next to attributes, references, and satisfy requirements in a view. In addition, the values that pass or fail requirements and constraints are highlighted in green and red, respectively. To learn more, see [CONFLUENCE_PAGE title='(2026x Refresh1) Displaying evaluation information' space=''].

##### Evaluating elements via the SysML v2 Model Evaluation console

You can evaluate model elements by writing an expression directly in the **SysML v2 Model Evaluation** console. However, you need to call the element you want to evaluate directly, because the console will not display the evaluation results of the owned and inherited elements.

To evaluate an element via the **SysML v2 Model Evaluation** console

1. Select Window > SysML v2 Model Evaluation to open the SysML v2 Model Evaluation console.
2. In the input box of the console, type the qualified name of the element you want to evaluate and press Enter. To save time, click [IMAGE alt='' src=''] in the toolbar of the **SysML v2 Model Evaluation** console to enable context selection in the Containment tree. When context selection is enabled, select the owner of the element you want to evaluate and enter only the element's name to evaluate it. [ATTACHMENT filename='evaluating_attribute_in_console.png']

The evaluation results are displayed in the **SysML v2 Model Evaluation**console as shown in the above figure.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>This chapter describes how you can evaluate model elements, e.g., attributes, expressed through general mathematical calculations. When you evaluate a model element, all of its owned and inherited attributes are evaluated as well.</p><h3>Evaluating model elements via the textual notation</h3><p>To evaluate a model element via the textual notation</p><hr /><ol><li data-uuid="886e8647-70cf-457c-85bd-c66e67cb4b2a">In the Textual Editor, place the cursor on the element you want to evaluate.</li><li data-uuid="93d6493e-b285-4d21-b44b-d75f302ecc96">In the Textual Editor toolbar, click <ac:image><ri:attachment ri:filename="evaluate_button.png" /></ac:image>.<br /><ac:image><ri:attachment ri:filename="evaluating_element_via_textual_notation.png" /></ac:image></li></ol><p>The evaluation results are displayed in the <strong>SysML v2 Model Evaluation</strong> console.</p><h3>Evaluating model elements via the Containment tree</h3><p>To evaluate a model element via the Containment tree</p><hr /><ul><li data-uuid="3cfbec25-79c8-41f3-b73e-df365cbf8aec">Right-click an element in the Containment tree and select <strong>Evaluate</strong>.<br /><ac:image><ri:attachment ri:filename="evaluating_element_via_containment_tree.png" /></ac:image></li></ul><p>The evaluation results are displayed in the <strong>SysML v2 Model Evaluation</strong> console.</p><h3>Evaluating model elements in views</h3><p>You can use views to evaluate individual model elements or all the elements displayed in a view. </p><p>To evaluate a model element in a view</p><hr /><ol><li data-uuid="497cbbe4-aa8e-4208-bd5a-700986b91800">Open the view displaying the model elements you want to evaluate.</li><li data-uuid="947f9f67-eb6c-49c4-9a19-7631846af0f6">Do one of the following:<ul><li>Select the shapes of the elements you want to evaluate and, in the view toolbar, click <ac:image><ri:attachment ri:filename="evaluate_button.png" /></ac:image>.<br /><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="6c510c2a-2148-496b-8784-b03a349ebdf2"><ac:rich-text-body><p>If you do not select any shapes, all the elements displayed in the view are evaluated.</p></ac:rich-text-body></ac:structured-macro><ac:image><ri:attachment ri:filename="evaluating_from_view_toolbar.png" /></ac:image></li><li>Right-click an element shape and select <strong>Evaluate</strong>.</li><li>Select an element shape and, in the smart manipulator, click <ac:image><ri:attachment ri:filename="evaluate_button.png" /></ac:image>.<br /><ac:image><ri:attachment ri:filename="evaluating_from_smart_manipulator.png" /></ac:image></li></ul></li></ol><p>After evaluation, runtime values are displayed in blue next to attributes, references, and satisfy requirements in a view. In addition, the values that pass or fail <span style="color:var(--ds-text,#172b4d);">requirements and constraints are highlighted in green and red, respectively. To learn more, see <ac:link><ri:page ri:content-title="(2026x Refresh1) Displaying evaluation information" /><ac:plain-text-link-body><![CDATA[Displaying evaluation information]]></ac:plain-text-link-body></ac:link>.</span></p><h3>Evaluating elements via the SysML v2 Model Evaluation console</h3><p>You can evaluate model elements by writing an expression directly in the <strong>SysML v2 Model Evaluation</strong> console. However, you need to call the element you want to evaluate directly, because the console will not display the evaluation results of the owned and inherited elements.</p><p>To evaluate an element via the <strong>SysML v2 Model Evaluation</strong> console</p><hr /><ol><li data-uuid="89cd8115-127b-48e8-8a41-e41e7077534e">Select <strong>Window</strong> &gt; <strong>SysML v2 Model Evaluation</strong> to open the <strong>SysML v2 Model Evaluation</strong> console.</li><li data-uuid="f5b982a0-da0c-4481-98da-13f726ac22f0">In the input box of the console, type the qualified name of the element you want to evaluate and press Enter.<br /><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="e7ef7365-c601-472f-a96c-786fb881295e"><ac:rich-text-body><p>To save time, click <ac:image ac:thumbnail="true" ac:height="16"><ri:attachment ri:filename="context_selection_icon.png" /></ac:image> in the toolbar of the <strong>SysML v2 Model Evaluation</strong> console to enable context selection in the Containment tree. When context selection is enabled, select the owner of the element you want to evaluate and enter only the element's name to evaluate it.</p></ac:rich-text-body></ac:structured-macro><ac:image><ri:attachment ri:filename="evaluating_attribute_in_console.png" /></ac:image></li></ol><p>The evaluation results are displayed in the <strong>SysML v2 Model Evaluation</strong><span> console as shown in the above figure.</span></p>
````

<!--NOMAGIC_PAGE id=314180409 space=SYSML2EP version=2 -->
## PAGE 00005: (2026x Refresh1) Evaluation information in views

- page_id: `314180409`
- space_key: `SYSML2EP`
- source_url: https://docs.nomagic.com/spaces/SYSML2EP/pages/314180409/2026x+Refresh1+Evaluation+information+in+views
- version_number: 2
- version_date: `2026-06-16T14:02:51.609+02:00`
- ancestors: Versions of SysML v2 Evaluation Plugin Documentation > (2026x Refresh1) SysML v2 Evaluation Plugin Documentation > (2026x Refresh1) User guide
- labels: []

### NORMALIZED CONTENT

During evaluation, model views display evaluation results, allowing you to analyze variable values and calculated data without leaving the modeling environment. Runtime information can also be modified, with the evaluation results being automatically recalculated.

For more information, see the following topics:

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p style="text-align: left;">During evaluation, model views display evaluation results, allowing you to analyze variable values and calculated data without leaving the modeling environment. Runtime information can also be modified, with the evaluation results being automatically recalculated.</p><p style="text-align: left;">For more information, see the following topics:</p><p style="text-align: left;"><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="629a9984-7ee3-43ea-abd7-c6864e6800c7" /></p>
````

<!--NOMAGIC_PAGE id=304014966 space=SYSML2EP version=1 -->
## PAGE 00006: (2026x Refresh1) Evaluation using Jupyter Notebook

- page_id: `304014966`
- space_key: `SYSML2EP`
- source_url: https://docs.nomagic.com/spaces/SYSML2EP/pages/304014966/2026x+Refresh1+Evaluation+using+Jupyter+Notebook
- version_number: 1
- version_date: `2026-04-29T17:11:16.121+02:00`
- ancestors: Versions of SysML v2 Evaluation Plugin Documentation > (2026x Refresh1) SysML v2 Evaluation Plugin Documentation > (2026x Refresh1) User guide > (2026x Refresh1) Server-side evaluation
- labels: []

### NORMALIZED CONTENT

You can evaluate Teamwork Cloud projects on the server by using Jupyter Notebook. This chapter explains how to set up Jupyter Notebook for server-side evaluation and describes all available requests.

Server-side evaluation is available only with the Teamwork Cloud Enterprise license.

##### Setting up Jupyter Notebook

To set up Jupyter Notebook

- In Jupyter Notebook, run the following command to install a Python package from the < install_root >\plugins\com.nomagic.magicdraw.sysml2.evaluation.plugin/pyEval.zip file:

Use the following requests to evaluate Teamwork Cloud projects on the server:

##### Creating a client/session and authenticating

<server_host>

<server_port>

<TWC_user_name>

<TWC_user_password>

This request starts a work session and provides authentication to Teamwork Cloud.

The following table describes the parameters used in the request:

| Parameter | In | Required or optional | Description |
| --- | --- | --- | --- |
| server_host | path | required | The Teamwork Cloud server host name. |
| server_port | path | required | The Teamwork Cloud server port. |
| TWC_user_name | path | optional | The Teamwork Cloud user name. If you do not specify the user name in the request, an input field will be provided to specify it later. |
| TWC_user_password | path | optional | The Teamwork Cloud password. If you do not specify the password in the request, an input field will be provided to specify it later. |

##### Getting the list of Teamwork Cloud projects

client.get_projects()

This request provides the list of Teamwork Cloud projects accessible to you depending on your permissions. Only projects that you can read (the Read Resources permission) are returned.

```text

```

##### Getting the list of project commits

<projectID>

This request provides the list of commits for the specified Teamwork Cloud project.

| Parameter | In | Required or optional | Description |
| --- | --- | --- | --- |
| projectID | path | required | The Teamwork Cloud project ID. |

```text

```

##### Getting the list of root-level elements

client.get_roots(<projectID>, commit=<commitID>)

This request returns all root-level model elements for the specified project. If there are several namespaces, they are merged into one list.

The following table describes the parameters used in therequest:

| Parameter | In | Required or optional | Description |
| --- | --- | --- | --- |
| projectID | path | required | The Teamwork Cloud project ID. |
| commit | path | optional | The commit ID of the Teamwork Cloud project. If the commit ID is not specified, the latest committed version is used instead. |

```text

```

##### Evaluating a parameter or expression

client.evaluate(<projectID>, commit=<commitID>, context=<contextPath>, data=json.dumps(<parameters>)

This request evaluates the specified Teamwork Cloud project parameter or expression.

The following table describes the parameters used in therequest:

| Parameter | In | Required or optional | Description |
| --- | --- | --- | --- |
| projectID | path | required | The Teamwork Cloud project ID. |
| commit | path | optional | The commit ID of the Teamwork Cloud project. If the commit ID is not specified, the latest committed version is used instead. |
| context | path | optional | The context path of the outputs, inputs, and expressions used to evaluate and retrieve data, e.g., SpacecraftMassRollup::spaceCraft. |
| inputs | body | optional | The set of inputs to be provided for the evaluation. Only inputs with initial values can be modified during evaluation. |
| outputs | body | optional | The set of outputs to be obtained after the evaluation. If no outputs are specified, all values are returned based on the specified context. |
| expressions | body | optional | The parameter or expression you want to evaluate. |

```text

```

##### Displaying an interactive HTML table

open_evaluation_table(self, <projectID>, commit=<commitID>, context=<contextPath>, params=<parmaList>, title=<tableTitle>, verification=<FAIL/ALL/NONE>)

This REST API request returns a JSON object containing the URL to an interactive HTML table that dynamically retrieves data based on the specified context, parameters, and/or expressions.

The following table describes the parameters used in the REST APIrequest:

| Parameter | In | Required or optional | Description |
| --- | --- | --- | --- |
| projectID | path | required | The Teamwork Cloud project ID. |
| commit | path | optional | The commit ID of the Teamwork Cloud project. If the commit ID is not specified, the latest committed version is used instead. |
| context | path | optional | The context path of the table parameters and/or expressions used to evaluate and retrieve data, e.g. SpacecraftMassRollup::spaceCraft. |
| params | path | optional | A comma-separated list of the parameters and/or expressions to display. Use the keyword 'all' to include all available parameters based on the specified context. |
| title | path | optional | The title of the HML table. |
| verification | path | optional | Specify which verification results to display: FAIL - failing values are highlighted in red; ALL - both failing and passing values are highlighted in red and green, respectively; NONE - no verification results are displayed. |

```text

```

```text

```

```text

```

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p style="text-align: left;">You can evaluate Teamwork Cloud projects on the server by using Jupyter Notebook. This chapter explains how to set up Jupyter Notebook for server-side evaluation and describes all available requests.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="69f6901c-8022-42de-a5bd-e06c4d2f1871"><ac:rich-text-body><p>Server-side evaluation is available only with the Teamwork Cloud Enterprise license.</p></ac:rich-text-body></ac:structured-macro><h3>Setting up Jupyter Notebook</h3><p style="text-align: left;">To set up Jupyter Notebook</p><hr /><ul><li data-uuid="9be626c8-3c24-4396-983b-497898a32610">In Jupyter Notebook, run the following command to install a Python package from the &lt;<em>install_root</em><em>&gt;\plugins\com.nomagic.magicdraw.sysml2.evaluation.<span style="color:var(--ds-text,#172b4d);">plugin/pyEval.zip</span></em><span> </span>file:<br /><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="1008cc78-0a4e-476a-9e42-f3eec6d268c4"><ac:plain-text-body><![CDATA[%pip install pyEval.zip]]></ac:plain-text-body></ac:structured-macro></li></ul><p style="text-align: left;">Use the following requests to evaluate Teamwork Cloud projects on the server:</p><h3>Creating a client/session and authenticating</h3><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="9564e4a8-1fa2-40d1-9fa9-4b6076430a22"><ac:rich-text-body>client = EvaluationWebClient('http(s)://<span style="color:var(--ds-background-accent-orange-bolder,#c25100);">&lt;server_host&gt;</span>:<span style="color:var(--ds-background-accent-orange-bolder,#c25100);">&lt;server_port&gt;</span>', '<span style="color:var(--ds-background-accent-orange-bolder,#c25100);">&lt;TWC_user_name&gt;</span>', '<span style="color:var(--ds-background-accent-orange-bolder,#c25100);">&lt;TWC_user_password&gt;</span>', False)</ac:rich-text-body></ac:structured-macro><p>This request starts a work session and provides authentication to Teamwork Cloud.</p><p>The following table describes the parameters used in the request:</p><table class="relative-table wrapped" style="width: 68.7671%;"><colgroup class=""> <col class="" style="width: 12.4396%;" /> <col class="" style="width: 8.85127%;" /> <col class="" style="width: 12.0455%;" /> <col class="" style="width: 66.6636%;" /> </colgroup><tbody class=""><tr class=""><th>Parameter</th><th>In</th><th>Required or optional</th><th colspan="1">Description</th></tr><tr class=""><td><strong>server_host</strong></td><td>path</td><td>required</td><td colspan="1">The Teamwork Cloud server host name.</td></tr><tr class=""><td colspan="1"><strong>server_port</strong></td><td colspan="1">path</td><td colspan="1">required</td><td colspan="1">The Teamwork Cloud server port.</td></tr><tr class=""><td colspan="1"><strong>TWC_user_name</strong></td><td colspan="1">path</td><td colspan="1">optional</td><td colspan="1"><p><span style="color:var(--ds-text,#172b4d);">The Teamwork Cloud user name. </span><span style="color:var(--ds-text,#172b4d);">If you do not specify the user name in the request, an input field will be provided to specify it later.</span></p></td></tr><tr class=""><td colspan="1"><strong>TWC_user_password</strong></td><td colspan="1">path</td><td colspan="1">optional</td><td colspan="1"><span style="color:var(--ds-text,#172b4d);">The Teamwork Cloud password. </span><span style="color:var(--ds-text,#172b4d);">If you do not specify the password in the request, an input field will be provided to specify it later.</span></td></tr></tbody></table><h3 style="text-align: left;">Getting the list of Teamwork Cloud projects</h3><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="6037605c-3e3f-4edb-9b21-86a381d0f6dc"><ac:rich-text-body>client.get_projects()</ac:rich-text-body></ac:structured-macro><p style="text-align: left;"><span style="color:var(--ds-text,#333333);">This request provides the list of Teamwork Cloud projects accessible to you depending on your permissions. Only projects that you can read (the Read Resources permission) are returned.</span></p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="cb1de3dc-c6b6-41d9-86cd-1dee792071ad"><ac:parameter ac:name="title">Request and response example</ac:parameter><ac:plain-text-body><![CDATA[client.get_projects()

[
    {
        'created': '2025-05-27T08:36:26.723Z',
        '@id': '62b072da-22f7-4ee7-9abe-37605571f9b7',
        'description': '',
        '@type': 'Project',
        'defaultBranch': {
            '@id': '7765ea2c-7cc4-4f12-9606-060ae8c8304d'
        },
        'name': "Don't Panic Batmobile"
    },
    {
        'created': '2025-05-27T08:29:52.949Z',
        '@id': 'b906d747-63c2-4d37-a809-49bd07d2eeba',
        'description': '',
        '@type': 'Project',
        'defaultBranch': {
            '@id': 'bbe03735-3093-44d1-bd48-9856b4c00da4'
        },
        'name': 'SysML Customization'
    },
    {
        'created': '2025-05-28T17:03:01.861Z',
        '@id': 'e7b10c6e-ae3c-49e9-af97-42d6384ebc2c',
        'description': '',
        '@type': 'Project',
        'defaultBranch': {
            '@id': 'e6d3df11-3260-4428-bb41-a0a2255e8c69'
        },
        'name': 'Spacecraft Mass Rollup V2'
    },
    {
        'created': '2025-05-28T17:07:08.197Z',
        '@id': '76ac1bae-11c9-434b-9096-3639ab338cf0',
        'description': '',
        '@type': 'Project',
        'defaultBranch': {
            '@id': 'fd07a9b3-8be1-4e6e-90f1-2992d983f8e0'
        },
        'name': 'Hinge Monte Carlo Analysis V2'
    }
]]]></ac:plain-text-body></ac:structured-macro><p style="text-align: left;"><br /></p><h3 style="text-align: left;">Getting the list of project commits</h3><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="2591f19f-8505-45ec-a3ef-9b1a622a1e0e"><ac:rich-text-body>client.get_commits(<span style="color:var(--ds-background-accent-orange-bolder,#c25100);">&lt;projectID&gt;</span>)</ac:rich-text-body></ac:structured-macro><p>This request provides the list of commits for the specified Teamwork Cloud project.</p><table class="relative-table wrapped" style="width: 68.7671%;"><colgroup class=""> <col class="" style="width: 12.4396%;" /> <col class="" style="width: 8.85127%;" /> <col class="" style="width: 12.0455%;" /> <col class="" style="width: 66.6636%;" /> </colgroup><tbody class=""><tr class=""><th>Parameter</th><th>In</th><th>Required or optional</th><th colspan="1">Description</th></tr><tr class=""><td><strong>projectID</strong></td><td>path</td><td>required</td><td colspan="1">The Teamwork Cloud project ID.</td></tr></tbody></table><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="60ce26c7-eac3-49bd-8bc0-68eb9b7c4583"><ac:parameter ac:name="title">Request and response example</ac:parameter><ac:plain-text-body><![CDATA[client.get_commits('62b072da-22f7-4ee7-9abe-37605571f9b7')

[
    {
        'created': '2025-05-27T08:36:26.410Z',
        '@id': '15a995d2-01cf-499b-a2d8-1f943af14320',
        'description': '** no message **',
        'owningProject': {
            '@id': '62b072da-22f7-4ee7-9abe-37605571f9b7'
        },
        'previousCommit': [
            {'@id': None}
        ]
    },
    {
        'created': '2025-05-27T08:39:34.763Z',
        '@id': 'b7a03a50-f42a-495d-9bd1-d87978d7f73f',
        'description': '** no message **',
        'owningProject': {
            '@id': '62b072da-22f7-4ee7-9abe-37605571f9b7'
        },
        'previousCommit': [
            {'@id': '15a995d2-01cf-499b-a2d8-1f943af14320'}
        ]
    }
]]]></ac:plain-text-body></ac:structured-macro><h3 style="text-align: left;">Getting the list of root-level elements</h3><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="c3c70852-5135-4c08-9292-2c88b44ea84b"><ac:rich-text-body><p><span style="color:var(--ds-text,#172b4d);">client.get_roots(<span style="color:var(--ds-background-accent-orange-bolder,#c25100);">&lt;projectID&gt;</span>, commit=<span style="color:var(--ds-background-accent-orange-bolder,#c25100);">&lt;commitID&gt;</span>)</span></p></ac:rich-text-body></ac:structured-macro><p>This request returns all root-level model elements for the specified project. <span style="color:var(--ds-text,#172B4D);">If there are several namespaces, they are merged into one list.</span></p><p><span style="color:var(--ds-text,#172b4d);">The following table describes the parameters used in the </span>request<span style="color:var(--ds-text,#172b4d);">:</span></p><table class="relative-table wrapped" style="width: 68.6413%;"><colgroup class=""><col class="" style="width: 9.82647%;" /><col class="" style="width: 7.84533%;" /><col class="" style="width: 10.4604%;" /><col class="" style="width: 71.8678%;" /></colgroup><tbody class=""><tr class=""><th>Parameter</th><th>In</th><th>Required or optional</th><th>Description</th></tr><tr class=""><td><strong>projectID</strong></td><td>path</td><td>required</td><td>The Teamwork Cloud project ID.</td></tr><tr class=""><td><strong>commit</strong></td><td>path</td><td>optional</td><td>The commit ID of the Teamwork Cloud project. If the commit ID is not specified, the latest committed version is used instead.</td></tr></tbody></table><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="41a398b4-3d38-4b02-bf03-c849ca3bb406"><ac:parameter ac:name="title">Request and response example</ac:parameter><ac:plain-text-body><![CDATA[client.get_roots('62b072da-22f7-4ee7-9abe-37605571f9b7')

[
  {
    "@id": "d6f0eea9-70fd-4ca8-b75f-3c794bd64f2b",
    "@type": "Package",
    "name": "Calculations",
    "elementId": "_G2tFcXD4Ee-huNu5so5rpw"
  },
  {
    "@id": "530d4e51-4f1d-4dfc-aae3-df7ece7dcdea",
    "@type": "Package",
    "name": "Requirements",
    "elementId": "_G2vhsXD4Ee-huNu5so5rpw"
  },
  {
    "@id": "2c5055d8-2899-4727-89c0-51072f20b60f",
    "@type": "Package",
    "name": "Vehicle",
    "elementId": "_G2ylAXD4Ee-huNu5so5rpw"
  },
  {
    "@id": "c1f8cfff-421a-4ab7-ac51-c1ad63899feb",
    "@type": "Package",
    "name": "TradeStudyAnalysis",
    "elementId": "_achG0XQLEe-Dbrd_o2J6Vg"
  }
]]]></ac:plain-text-body></ac:structured-macro><h3 style="text-align: left;">Evaluating a parameter or expression</h3><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="b1cda8f0-a944-47d9-80c8-da8df670be11"><ac:rich-text-body><p>client.evaluate(<span style="color:var(--ds-background-accent-orange-bolder,#c25100);">&lt;projectID&gt;</span>, commit=<span style="color:var(--ds-background-accent-orange-bolder,#c25100);">&lt;commitID&gt;</span>, context=<span style="color:var(--ds-background-accent-orange-bolder,#c25100);">&lt;contextPath&gt;</span>, data=json.dumps(<span style="color:var(--ds-background-accent-orange-bolder,#c25100);">&lt;parameters&gt;</span>)</p></ac:rich-text-body></ac:structured-macro><p style="text-align: left;"><span style="color:var(--ds-text,#172b4d);">This request evaluates the specified Teamwork Cloud project parameter or expression.</span></p><p style="text-align: left;"><span style="color:var(--ds-text,#172b4d);">The following table describes the parameters used in the </span>request<span style="color:var(--ds-text,#172b4d);">:</span></p><table class="relative-table wrapped" style="width: 68.6413%;"><colgroup class=""><col class="" style="width: 9.82647%;" /><col class="" style="width: 7.84533%;" /><col class="" style="width: 10.4604%;" /><col class="" style="width: 71.8678%;" /></colgroup><tbody class=""><tr class=""><th>Parameter</th><th>In</th><th>Required or optional</th><th>Description</th></tr><tr class=""><td><strong>projectID</strong></td><td>path</td><td>required</td><td>The Teamwork Cloud project ID.</td></tr><tr class=""><td><strong>commit</strong></td><td>path</td><td>optional</td><td>The commit ID of the Teamwork Cloud project. If the commit ID is not specified, the latest committed version is used instead.</td></tr><tr class=""><td><strong>context</strong></td><td>path</td><td>optional</td><td><span style="color:var(--ds-text-accent-purple-bolder,#352c63);">The context path of the outputs, inputs, and expressions used to evaluate and retrieve data, e.g., SpacecraftMassRollup::spaceCraft.</span></td></tr><tr class=""><td><strong>inputs</strong></td><td>body</td><td>optional</td><td>The set of inputs to be provided for the evaluation. <span style="color:var(--ds-text-accent-purple-bolder,#352c63);">Only inputs with initial values can be modified during evaluation.</span></td></tr><tr class=""><td><strong>outputs</strong></td><td>body</td><td>optional</td><td>The set of outputs to be obtained after the evaluation. <span style="color:var(--ds-text-accent-purple-bolder,#352c63);">If no outputs are specified, all values are returned based on the specified context.</span></td></tr><tr class=""><td><strong>expressions</strong></td><td>body</td><td>optional</td><td><div class="content-wrapper"><p>The parameter or expression you want to evaluate.</p></div></td></tr></tbody></table><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="9ce7bcd1-f696-4cae-a962-1e39e6de0c3e"><ac:parameter ac:name="title">Request example with a request body</ac:parameter><ac:plain-text-body><![CDATA[parameters = {
 "inputs":
   {
        "propulsion.thruster.me":32,
        "telecom.amplifier.me":15
   },
 "outputs": 
    [ 
        "me",
        "propulsion.mee",
        "propulsion.tank.me",
        "propulsion.thruster.me",
        "telecom.me",
        "telecom.antenna.me",
        "telecom.amplifier.me"
    ]
}

client.evaluate('a9e055de-e288-4b81-81e4-e24bbb32cedd', context='SpacecraftMassRollup::spacecraft', data=json.dumps(parameters))]]></ac:plain-text-body></ac:structured-macro><h3 style="text-align: left;">Displaying an interactive HTML table</h3><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="db3f2dcb-7a12-4b80-9beb-3093dfc154af"><ac:rich-text-body><p>open_evaluation_table(self, <span style="color:var(--ds-background-accent-orange-bolder,#c25100);">&lt;projectID&gt;</span>, commit=<span style="color:var(--ds-background-accent-orange-bolder,#c25100);">&lt;commitID&gt;</span>, context=<span style="color:var(--ds-background-accent-orange-bolder,#c25100);">&lt;contextPath&gt;</span>, params=<span style="color:var(--ds-background-accent-orange-bolder,#c25100);">&lt;parmaList&gt;</span>, title=<span style="color:var(--ds-background-accent-orange-bolder,#c25100);">&lt;tableTitle&gt;</span>, verification=<span style="color:var(--ds-background-accent-orange-bolder,#c25100);">&lt;FAIL/ALL/NONE&gt;</span>)</p></ac:rich-text-body></ac:structured-macro><p style="text-align: left;"><span style="color:var(--ds-text,#172b4d);">This REST API request returns a JSON object containing the URL to an interactive HTML table that dynamically retrieves data based on the specified context, parameters, and/or expressions.</span></p><p style="text-align: left;"><span style="color:var(--ds-text,#172b4d);">The following table describes the parameters used in the REST API<span> </span></span>request<span style="color:var(--ds-text,#172b4d);">:</span></p><table class="relative-table wrapped" style="width: 68.6413%;"><colgroup class=""><col class="" style="width: 9.82647%;" /><col class="" style="width: 7.84533%;" /><col class="" style="width: 10.4604%;" /><col class="" style="width: 71.8678%;" /></colgroup><tbody class=""><tr class=""><th>Parameter</th><th>In</th><th>Required or optional</th><th>Description</th></tr><tr class=""><td><strong>projectID</strong></td><td>path</td><td>required</td><td>The Teamwork Cloud project ID.</td></tr><tr class=""><td><strong>commit</strong></td><td>path</td><td>optional</td><td>The commit ID of the Teamwork Cloud project. If the commit ID is not specified, the latest committed version is used instead.</td></tr><tr class=""><td><strong>context</strong></td><td>path</td><td>optional</td><td><span style="color:var(--ds-text-accent-purple-bolder,#352c63);">The context path of the table parameters and/or expressions used to evaluate and retrieve data, e.g. SpacecraftMassRollup::spaceCraft.</span></td></tr><tr class=""><td><strong>params</strong></td><td>path</td><td>optional</td><td><span style="color:var(--ds-text-accent-purple-bolder,#352c63);">A comma-separated list of the parameters and/or expressions to display. Use the keyword 'all' to include all available parameters based on the specified context.</span></td></tr><tr class=""><td><strong>title</strong></td><td>path</td><td>optional</td><td>The title of the HML table.</td></tr><tr class=""><td><strong>verification </strong></td><td>path</td><td>optional</td><td>Specify which verification results to display: <strong>FAIL</strong> - failing values are highlighted in red; <strong>ALL</strong> - both failing and passing values are highlighted in red and green, respectively; <strong>NONE</strong> - no verification results are displayed.</td></tr></tbody></table><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="8868d21a-0d23-441b-8e6e-fbfba7234301"><ac:parameter ac:name="title">Request example</ac:parameter><ac:plain-text-body><![CDATA[open_evaluation_table(self, dc8b24ee-462d-4874-8b52-b85978f242cc, commit=3fa85f64-5717-4562-b3fc-2c963f66afa6, context=SpacecraftMassRollup::spaceCraft, params=me,propulsion.tank.me,propulsion.thruster.me, title=SpaceCraftMassRollup)]]></ac:plain-text-body></ac:structured-macro><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="7eeb9179-0138-4d81-9713-2a4351d13de4"><ac:parameter ac:name="title">Request example</ac:parameter><ac:plain-text-body><![CDATA[open_evaluation_table(self, dc8b24ee-462d-4874-8b52-b85978f242cc, commit=3fa85f64-5717-4562-b3fc-2c963f66afa6, context=SpacecraftMassRollup::spaceCraft, params=all, title=SpaceCraftMassRollup, verification=fail)]]></ac:plain-text-body></ac:structured-macro><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="8ccc7679-c4d7-4164-aabf-1ac0e533016a"><ac:parameter ac:name="title">Request example</ac:parameter><ac:plain-text-body><![CDATA[open_evaluation_table(self, dc8b24ee-462d-4874-8b52-b85978f242cc, params=SpacecraftMassRollup::spaceCraft.me,SpacecraftMassRollup::spaceCraft.propulsion.tank.me, title=SpaceCraftMassRollup)]]></ac:plain-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=304014964 space=SYSML2EP version=1 -->
## PAGE 00007: (2026x Refresh1) Evaluation using REST API

- page_id: `304014964`
- space_key: `SYSML2EP`
- source_url: https://docs.nomagic.com/spaces/SYSML2EP/pages/304014964/2026x+Refresh1+Evaluation+using+REST+API
- version_number: 1
- version_date: `2026-04-29T17:11:16.044+02:00`
- ancestors: Versions of SysML v2 Evaluation Plugin Documentation > (2026x Refresh1) SysML v2 Evaluation Plugin Documentation > (2026x Refresh1) User guide > (2026x Refresh1) Server-side evaluation
- labels: []

### NORMALIZED CONTENT

You can use the following REST API requests to evaluate Teamwork Cloud projects on the server.

Server-side evaluation is available only with the Teamwork Cloud Enterprise license.

For more information about evaluation-related REST APIs, see *https://<server_IP>:8443/sysmlv2-api/swagger-ui/index.html,* where**<server_IP>**is your Teamwork Cloud server IP.There, you can findREST API descriptions in both machine-readable and human-readable formats.

##### Evaluating a parameter or expression

<projectID>

<commitID>

evaluate?context=

<contextPath>

This REST API request evaluates the specified Teamwork Cloud project parameter or expression.

The following table describes the parameters used in the REST APIrequest:

| Parameter | In | Required or optional | Description |
| --- | --- | --- | --- |
| projects | path | required | The Teamwork Cloud project ID. |
| commits | path | optional | The commit ID of the Teamwork Cloud project. If the commit ID is not specified, the latest committed version is used instead. |
| context | path | optional | The context path of the outputs, inputs, and expressions used to evaluate and retrieve data, e.g., SpacecraftMassRollup::spaceCraft |
| inputs | body | optional | The set of inputs to be provided for the evaluation. Only inputs with initial values can be modified during evaluation. |
| outputs | body | optional | The set of outputs to be obtained after the evaluation. If no outputs are specified, all values are returned based on the specified context. |
| expressions | body | optional | The parameter or expression you want to evaluate. |

```shell

```

```text

```

##### Displaying an interactive HTML table

GET /projects/<projectID>/commits/<commitID>/evaluate/table-view?context=<contextPath>?params=<paramsList>?title=<tableTitle>?verification=<FAIL/ALL/NONE>

This REST API request returns a URL to an interactive HTML table that dynamically retrieves data based on the specified context, parameters and/or expressions.

The following table describes the parameters used in the REST APIrequest:

| Parameter | In | Required or optional | Description |
| --- | --- | --- | --- |
| projects | path | required | The Teamwork Cloud project ID. |
| commits | path | optional | The commit ID of the Teamwork Cloud project. If the commit ID is not specified, the latest committed version is used instead. |
| context | path | optional | The context path of the table parameters and/or expressions used to evaluate and retrieve data, e.g. SpacecraftMassRollup::spaceCraft |
| params | path | optional | A comma-separated list of the parameters and/or expressions to display. Use the keyword 'all' to include all available parameters based on the specified context. |
| title | path | optional | The title of the HML table. |
| verification | path | optional | Specify which verification results to display: FAIL - failing values are highlighted in red; ALL - both failing and passing values are highlighted in red and green, respectively; NONE - no verification results are displayed. |

```text

```

```text

```

```text

```

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p style="text-align: left;">You can use the following REST API requests to evaluate Teamwork Cloud projects on the <ac:inline-comment-marker ac:ref="fe34aa72-4ced-4f7f-8b92-d3cd39200d55">server</ac:inline-comment-marker>.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="06e570ac-6c75-48a3-b433-bd9184d71368"><ac:rich-text-body><p>Server-side evaluation is available only with the Teamwork Cloud Enterprise license.</p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="c44a1752-1253-4e00-abfe-023fcb6c6003"><ac:rich-text-body><p><span style="color:var(--ds-text,#172b4d);"><span style="color:var(--ds-text,#172b4d);">For more information about evaluation-related REST APIs, see <em style="text-align: left;">https://&lt;server_IP&gt;:8443/sysmlv2-api/swagger-ui/index.html,</em> <span style="color:var(--ds-text,#172b4d);">where<span> </span></span><strong style="text-align: left;">&lt;server_IP&gt;</strong><span style="color:var(--ds-text,#172b4d);"><span> </span>is your Teamwork Cloud server IP.</span></span><span style="color:var(--ds-text,#172b4d);"> There, you can find<span> </span></span>REST API descriptions in both machine-readable and human-readable formats.</span></p></ac:rich-text-body></ac:structured-macro><h3 style="text-align: left;">Evaluating a parameter or expression</h3><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="b1cda8f0-a944-47d9-80c8-da8df670be11"><ac:rich-text-body>POST /api/projects/<span style="color:var(--ds-background-accent-orange-bolder,#c25100);">&lt;projectID&gt;</span>/commits/<span style="color:var(--ds-background-accent-orange-bolder,#c25100);">&lt;commitID&gt;</span>/<ac:inline-comment-marker ac:ref="6163968c-91fe-4a1f-b00d-444b5be91736"><span style="color:var(--ds-text,#172b4d);">evaluate?context=</span><span style="color:var(--ds-background-accent-orange-bolder,#c25100);">&lt;contextPath&gt;</span></ac:inline-comment-marker></ac:rich-text-body></ac:structured-macro><p style="text-align: left;"><span style="color:var(--ds-text,#172b4d);">This REST API request evaluates the specified Teamwork Cloud project parameter or expression.</span></p><p style="text-align: left;"><span style="color:var(--ds-text,#172b4d);">The following table describes the parameters used in the REST API<span> </span></span>request<span style="color:var(--ds-text,#172b4d);">:</span></p><table class="wrapped relative-table" style="width: 68.6413%;"><colgroup><col style="width: 9.82647%;" /><col style="width: 7.84533%;" /><col style="width: 10.4604%;" /><col style="width: 71.8678%;" /></colgroup><tbody><tr><th scope="col">Parameter</th><th scope="col">In</th><th scope="col">Required or optional</th><th scope="col">Description</th></tr><tr><td><strong>projects</strong></td><td>path</td><td>required</td><td>The Teamwork Cloud project ID.</td></tr><tr><td><strong><ac:inline-comment-marker ac:ref="c95d1c2f-f8db-4428-8f9e-4434713dff87">commits</ac:inline-comment-marker></strong></td><td>path</td><td>optional</td><td>The commit ID of the Teamwork Cloud project. If the commit ID is not specified, the latest committed version is used instead.</td></tr><tr><td><strong>context</strong></td><td>path</td><td><ac:inline-comment-marker ac:ref="6569328f-546e-4d2d-8496-bc76b93f78ce">optional</ac:inline-comment-marker></td><td><span style="color:var(--ds-text-accent-purple-bolder,#352c63);">The context path of the outputs, inputs, and expressions used to evaluate and retrieve data, e.g., SpacecraftMassRollup::spaceCraft</span></td></tr><tr><td><strong>inputs</strong></td><td>body</td><td><ac:inline-comment-marker ac:ref="6569328f-546e-4d2d-8496-bc76b93f78ce">optional</ac:inline-comment-marker></td><td>The set of inputs to be provided for the evaluation. <span style="color:var(--ds-text-accent-purple-bolder,#352c63);">Only inputs with initial values can be modified during evaluation.</span></td></tr><tr><td><strong>outputs</strong></td><td>body</td><td>optional</td><td>The set of outputs to be obtained after the evaluation. <span style="color:var(--ds-text-accent-purple-bolder,#352c63);">If no outputs are specified, all values are returned based on the specified context.</span></td></tr><tr><td><strong>expressions</strong></td><td>body</td><td><ac:inline-comment-marker ac:ref="af08c97c-2d9e-424e-a7dc-0723880586ca">optional</ac:inline-comment-marker></td><td><div class="content-wrapper"><p>The parameter or expression you want to evaluate.</p></div></td></tr></tbody></table><p><br /></p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="5de60b50-1f5b-47a3-b326-dbcc33d31869"><ac:parameter ac:name="language">shell</ac:parameter><ac:parameter ac:name="title">Request and response example with the request body</ac:parameter><ac:plain-text-body><![CDATA[POST /projects/dc8b24ee-462d-4874-8b52-b85978f242cc/evaluate?context=SpacecraftMassRollup::spaceCraft

{
  "inputs":
   {
        "propulsion.thruster.me":10,
        "telecom.amplifier.me":15
   },
 "outputs": 
    [ 
        "me",
        "propulsion.mee",
        "propulsion.tank.me",
        "propulsion.thruster.me",
        "telecom.me",
        "telecom.antenna.me",
        "telecom.amplifier.me"
    ]
}

Response:

{'outputs': 
 {'me': 144.0,
  'propulsion.tank.me': 100.0,
  'propulsion.thruster.me': 10.0,
  'telecom.me': 34.0,
  'telecom.amplifier.me': 15.0,
  'telecom.antenna.me': 19.0
 }
}]]></ac:plain-text-body></ac:structured-macro><p><br /></p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="457ffbed-3c36-4994-9206-eb01d204ae9c"><ac:parameter ac:name="title">Request and response example with the request body</ac:parameter><ac:plain-text-body><![CDATA[POST /projects/fa6e7f27-f922-4718-aba4-6b909d6d1dcc/evaluate

{
  "inputs":
   {
        "TradeStudyAnalysis::VehicleAlternatives::vehicle_A.grossMass":2000,
        "TradeStudyAnalysis::VehicleAlternatives::vehicle_A.grossMass":1000
   }
 "expressions": 
    [ 
        "TradeStudyAnalysis::VehicleAlternatives::vehicle_A.stoppingDistance-TradeStudyAnalysis::VehicleAlternatives::vehicle_B.stoppingDistance"
    ]
}

=== Response ===

{
'expressions': 
 ['TradeStudyAnalysis::VehicleAlternatives::vehicle_A.stoppingDistance-TradeStudyAnalysis::VehicleAlternatives::vehicle_B.stoppingDistance':56.9344
 ]
}]]></ac:plain-text-body></ac:structured-macro><h3 style="text-align: left;">Displaying an interactive HTML table</h3><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="db3f2dcb-7a12-4b80-9beb-3093dfc154af"><ac:rich-text-body><p><span style="color:var(--ds-text,#172b4d);">GET /projects/<span style="color:var(--ds-background-accent-orange-bolder,#c25100);">&lt;projectID&gt;</span>/commits/<span style="color:var(--ds-background-accent-orange-bolder,#c25100);">&lt;commitID&gt;</span>/evaluate/</span>table-view<span style="color:var(--ds-text,#172b4d);">?</span>context<span style="color:var(--ds-text,#172b4d);">=<span style="color:var(--ds-background-accent-orange-bolder,#c25100);">&lt;contextPath&gt;</span>?</span>params<span style="color:var(--ds-text,#172b4d);">=<span style="color:var(--ds-background-accent-orange-bolder,#c25100);">&lt;paramsList&gt;</span>?</span>title<span style="color:var(--ds-text,#172b4d);">=<span style="color:var(--ds-background-accent-orange-bolder,#c25100);">&lt;tableTitle&gt;<span style="color:var(--ds-text,#172b4d);">?verification=<span style="color:var(--ds-background-accent-orange-bolder,#c25100);">&lt;FAIL/ALL/NONE&gt;</span></span></span></span></p></ac:rich-text-body></ac:structured-macro><p style="text-align: left;"><span style="color:var(--ds-text,#172b4d);">This REST API request returns a URL to an interactive HTML table that dynamically retrieves data based on the specified context, parameters and/or expressions.</span></p><p style="text-align: left;"><span style="color:var(--ds-text,#172b4d);">The following table describes the parameters used in the REST API<span> </span></span>request<span style="color:var(--ds-text,#172b4d);">:</span></p><table class="relative-table wrapped" style="width: 68.6413%;"><colgroup><col style="width: 9.82647%;" /><col style="width: 7.84533%;" /><col style="width: 10.4604%;" /><col style="width: 71.8678%;" /></colgroup><tbody><tr><th>Parameter</th><th>In</th><th>Required or optional</th><th>Description</th></tr><tr><td><strong>projects</strong></td><td>path</td><td>required</td><td>The Teamwork Cloud project ID.</td></tr><tr><td><strong>commits</strong></td><td>path</td><td>optional</td><td>The commit ID of the Teamwork Cloud project. If the commit ID is not specified, the latest committed version is used instead.</td></tr><tr><td><strong>context</strong></td><td>path</td><td>optional</td><td><span style="color:var(--ds-text-accent-purple-bolder,#352c63);">The context path of the table parameters and/or expressions used to evaluate and retrieve data, e.g. SpacecraftMassRollup::spaceCraft</span></td></tr><tr><td><strong>params</strong></td><td>path</td><td>optional</td><td><span style="color:var(--ds-text-accent-purple-bolder,#352c63);">A comma-separated list of the parameters and/or expressions to display. Use the keyword 'all' to include all available parameters based on the specified context.</span></td></tr><tr><td><strong>title</strong></td><td>path</td><td>optional</td><td>The title of the HML table.</td></tr><tr><td><strong>verification</strong></td><td>path</td><td>optional</td><td>Specify which verification results to display: <strong>FAIL</strong> - failing values are highlighted in red; <strong>ALL</strong> - both failing and passing values are highlighted in red and green, respectively; <strong>NONE</strong> - no verification results are displayed.</td></tr></tbody></table><p><br /></p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="8868d21a-0d23-441b-8e6e-fbfba7234301"><ac:parameter ac:name="title">Request example</ac:parameter><ac:plain-text-body><![CDATA[GET /projects/dc8b24ee-462d-4874-8b52-b85978f242cc/commits/3fa85f64-5717-4562-b3fc-2c963f66afa6/evaluate/table-view?context=SpacecraftMassRollup::spaceCraft&params=me,propulsion.tank.me,propulsion.thruster.me&title=SpaceCraftMassRollup]]></ac:plain-text-body></ac:structured-macro><p><br /></p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="7eeb9179-0138-4d81-9713-2a4351d13de4"><ac:parameter ac:name="title">Request example</ac:parameter><ac:plain-text-body><![CDATA[GET /projects/dc8b24ee-462d-4874-8b52-b85978f242cc/commits/3fa85f64-5717-4562-b3fc-2c963f66afa6/evaluate/table-view?context=SpacecraftMassRollup::spaceCraft&params=all&title=SpaceCraftMassRollup?verification=fail]]></ac:plain-text-body></ac:structured-macro><p><br /></p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="8ccc7679-c4d7-4164-aabf-1ac0e533016a"><ac:parameter ac:name="title">Request example</ac:parameter><ac:plain-text-body><![CDATA[GET /projects/dc8b24ee-462d-4874-8b52-b85978f242cc/evaluate/table-view?params=SpacecraftMassRollup::spaceCraft.me,SpacecraftMassRollup::spaceCraft.propulsion.tank.me&title=SpaceCraftMassRollup]]></ac:plain-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=304014916 space=SYSML2EP version=1 -->
## PAGE 00008: (2026x Refresh1) Exporting evaluation results to CSV

- page_id: `304014916`
- space_key: `SYSML2EP`
- source_url: https://docs.nomagic.com/spaces/SYSML2EP/pages/304014916/2026x+Refresh1+Exporting+evaluation+results+to+CSV
- version_number: 1
- version_date: `2026-04-29T17:11:15.327+02:00`
- ancestors: Versions of SysML v2 Evaluation Plugin Documentation > (2026x Refresh1) SysML v2 Evaluation Plugin Documentation > (2026x Refresh1) User guide
- labels: []

### NORMALIZED CONTENT

You can use views to evaluate model elements displayed in a view and export the results to a CSV file.

To export the evaluation results to a CSV file

1. In the view toolbar, click [IMAGE alt='' src=''] to evaluate model elements displayed in the view.
2. In the view toolbar, click the arrow next to [IMAGE alt='' src=''] andselect**Export to CSV**. When the evaluation is performed on selected elements, only the results for those elements are exported. If no elements were selected, the export will include results for all elements displayed in the view. [ATTACHMENT filename='export_to_csv.png']
3. In the**CSV Export Options** dialog, specify the export options. To learn more, see 
[IMAGE alt='' src='']
4. Click **OK** to export the evaluation results.

The CSV file with evaluation results is saved in the specified location. You can open the file by clicking a link in the message saying that the CSV file was generated successfully.

##### CSV Export Options dialog

The following table describes the UI elements of the **CSV Export Options** dialog.

| UI element | Description |
| --- | --- |
| CSV Delimiter | Select the character used to separate values (columns) in a CSV file. The default CSV delimiter is selected according to the machine's locale. |
| Export annotated only | Select the Export annotated only check box to export only annotated results in the view. Clear the check box to export all evaluation results. |
| Attributes as columns | Select the Attributes as columns check box to export attributes to columns and paths to the corresponding rows. Clear the check box to print every value in a separate row. |
| Output | Specify the path to the CSV file. By default, the project directory is selected. |

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><span style="color:var(--ds-text,#172b4d);">You can use views to evaluate model elements displayed in a view and export the results to a CSV file.</span></p><p>To export the evaluation results to a CSV file</p><hr /><ol><li><p>In the <span style="color:var(--ds-text,#172b4d);">view toolbar</span>, click <ac:image ac:thumbnail="true" ac:height="14"><ri:attachment ri:filename="evaluate_button.png" /></ac:image> to evaluate model elements displayed in the view.</p></li><li><p>In the <span style="color:var(--ds-text,#172b4d);">view toolbar</span>, click the arrow next to <ac:image ac:thumbnail="true" ac:height="14"><ri:attachment ri:filename="evaluate_button.png" /></ac:image> and<span style="letter-spacing: 0.0px;"> select </span><strong style="letter-spacing: 0.0px;">Export to CSV</strong><span style="letter-spacing: 0.0px;">.<br /></span></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="bffab1b5-a500-4117-a00a-f37583c604e0"><ac:rich-text-body><p><span style="color:var(--ds-text,#172b4d);">When the evaluation is performed on selected elements, only the results for those elements are exported. If no elements were selected, the export will include results for all elements displayed in the view.</span></p></ac:rich-text-body></ac:structured-macro><ac:image ac:height="224"><ri:attachment ri:filename="export_to_csv.png" /></ac:image></li><li><p>In the<strong> CSV Export Options</strong> dialog, specify the export options. To learn more, see <ac:link ac:anchor="CSV Export Options dialog"><ac:plain-text-link-body><![CDATA[CSV Export Options dialog.]]></ac:plain-text-link-body></ac:link><br /><ac:image><ri:attachment ri:filename="csv_export_options.png" /></ac:image></p></li><li><p>Click <strong>OK</strong> to export the evaluation results.</p></li></ol><p>The CSV file with evaluation results is saved in the specified location. You can open the file by clicking a link in the message saying that the CSV file was generated successfully.</p><h3>CSV Export Options dialog</h3><p>The following table describes the UI elements of the <strong>CSV Export Options</strong> dialog.</p><table class="wrapped relative-table" style="width: 99.1781%;"><colgroup><col style="width: 14.0953%;" /><col style="width: 85.9237%;" /></colgroup><tbody><tr><th scope="col"><p>UI element</p></th><th scope="col"><p>Description</p></th></tr><tr><td><p><strong>CSV Delimiter</strong></p></td><td><p>Select the character used to separate values (columns) in a CSV file. The default CSV delimiter is selected according to the machine's locale. </p></td></tr><tr><td><p><strong>Export annotated only</strong></p></td><td><p>Select the <strong>Export annotated only </strong>check box to export only annotated results in the view. Clear the check box to export all evaluation results.</p></td></tr><tr><td><p><strong>Attributes as columns</strong></p></td><td><div class="content-wrapper"><p>Select the <strong>Attributes as columns </strong>check box to export attributes to columns and paths to the corresponding rows. Clear the check box to print every value in a separate row.</p><p><ac:image ac:height="222"><ri:attachment ri:filename="attributes_as_columns.png" /></ac:image></p></div></td></tr><tr><td><p><strong>Output</strong></p></td><td><p>Specify the path to the CSV file. By default, the project directory is selected. </p></td></tr></tbody></table>
````

<!--NOMAGIC_PAGE id=304014922 space=SYSML2EP version=2 -->
## PAGE 00009: (2026x Refresh1) Integration with MATLAB

- page_id: `304014922`
- space_key: `SYSML2EP`
- source_url: https://docs.nomagic.com/spaces/SYSML2EP/pages/304014922/2026x+Refresh1+Integration+with+MATLAB
- version_number: 2
- version_date: `2026-04-29T17:12:22.515+02:00`
- ancestors: Versions of SysML v2 Evaluation Plugin Documentation > (2026x Refresh1) SysML v2 Evaluation Plugin Documentation > (2026x Refresh1) User guide
- labels: ['matlab-integration']

### NORMALIZED CONTENT

If you install MATLAB and integrate it with your modeling tool, you will be able to evaluate scripts written in MATLAB syntax. For example, you can [use MATLAB as a script language to define the return in calculations](https://docs.nomagic.com/SYSML2EP/?contextKey=invoking-calculations&version=2026x Refresh1).

#### NOTE: Prerequisites

Prerequisites

- MATLAB 2023a and later versions have been tested for compatibility with SysML v2 projects. Support for older versions is not guaranteed.
- You must use the 64-bit version of MATLAB so it will work with the 64-bit version of modeling tools.
- If MATLAB was integrated before installing the SysML v2 Evaluation plugin, you must reintegrate it to ensure compatibility with SysML v2 projects.
- On Windows, the application requires admin rights to complete the integration with MATLAB. If admin rights are not granted or available, you will not be able to use MATLAB with SysML v2 projects.

To integrate a modeling tool with MATLAB

1. In the main menu, select Tools > Integrations .
2. In the Integrations dialog, select MATLAB and click Integrate/Remove Integration . 
[IMAGE alt='' src='']
3. In the open dialog, specify the MATLAB home directory . 
[IMAGE alt='' src=''] The JRE home directory is selected automatically.
4. Click **OK**.
5. If you use Windows, click Yes to grant the application admin rights. Otherwise, go to the next step.
6. When you get a message saying to restart the modeling tool, click OK and restart the modeling tool.

**Related pages**

- [CONFLUENCE_PAGE title='(2026x Refresh1) Connecting to a running MATLAB session' space='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p>If you install MATLAB and integrate it with your modeling tool, you will be able to evaluate scripts written in MATLAB syntax. For example, you can <a href="https://docs.nomagic.com/SYSML2EP/?contextKey=invoking-calculations&amp;version=2026x Refresh1">use MATLAB as a script language to define the return in calculations</a>.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="a62fa631-c814-4636-a48c-c579d65b2775"><ac:parameter ac:name="title">Prerequisites</ac:parameter><ac:rich-text-body><ul><li data-uuid="738f013e-5e85-4df4-9a26-727627077052"><span style="color:var(--ds-text,#172b4d);">MATLAB 2023a and later versions have been tested for compatibility with SysML v2 projects. Support for older versions is not guaranteed.</span></li><li data-uuid="46250bb8-88dc-4535-acde-7796f3e378d0">You must use the 64-bit version of MATLAB so it will work with the 64-bit version of modeling tools.</li><li data-uuid="279c4c89-7045-44bb-b595-a8c3c5204b44">If MATLAB was integrated before installing the SysML v2 Evaluation plugin, you must reintegrate it to ensure compatibility with SysML v2 projects.</li><li data-uuid="b66c7214-9ed4-4451-9a3a-a7afe98a6845"><p style="text-align: left;">On Windows, the application requires admin rights to complete the integration with MATLAB. If admin rights are not granted or available, you will not be able to use MATLAB with SysML v2 projects.</p></li></ul></ac:rich-text-body></ac:structured-macro><p><br /></p><p>To integrate a modeling tool with MATLAB</p><hr /><ol><li class="auto-cursor-target" data-uuid="3094f6a1-7cbb-4c87-8776-c3845c0f0ccb">In the main menu, select <strong>Tools </strong>&gt;<strong> Integrations</strong>.</li><li class="auto-cursor-target" data-uuid="83599c2f-e2f7-4603-b5d1-05b8456461ce">In the <strong>Integrations</strong> dialog, select <strong>MATLAB</strong> and click <strong>Integrate/Remove Integration</strong><span>.<br /><ac:image><ri:attachment ri:filename="integrations_dialog.png"><ri:page ri:content-title="(2026x Refresh1) Integration with MATLAB" /></ri:attachment></ac:image><br /></span></li><li class="auto-cursor-target" data-uuid="78a36882-b376-40a4-a8ee-53cc7bfb4ae0">In the open dialog, specify the <strong>MATLAB home directory</strong><span>.<br /><ac:image><ri:attachment ri:filename="directory_selection_dialog.png"><ri:page ri:content-title="(2026x Refresh1) Integration with MATLAB" /></ri:attachment></ac:image><br /></span><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="a5efb116-d9fe-4aa3-9560-a7b3acea2d26"><ac:rich-text-body><p>The JRE home directory is selected automatically.</p></ac:rich-text-body></ac:structured-macro></li><li class="auto-cursor-target" data-uuid="310fde7e-04cf-4a00-899a-8955c7951976"><p class="auto-cursor-target">Click <strong>OK</strong>.</p></li><li class="auto-cursor-target" data-uuid="a9ce527d-1f37-41ab-8bab-4a626b0b1e98">If you use Windows, click <strong>Yes</strong> to grant the application admin rights. Otherwise, go to the next step.</li><li class="auto-cursor-target" data-uuid="bbd5498b-8e9c-45cc-8d90-34fbb7553f95">When you get a message saying to restart the modeling tool, click <strong>OK</strong> and restart the modeling tool.</li></ol></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><strong>Related pages</strong></p><ul><li><ac:link><ri:page ri:content-title="(2026x Refresh1) Connecting to a running MATLAB session" /></ac:link></li></ul></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=304014949 space=SYSML2EP version=2 -->
## PAGE 00010: (2026x Refresh1) Invoking actions

- page_id: `304014949`
- space_key: `SYSML2EP`
- source_url: https://docs.nomagic.com/spaces/SYSML2EP/pages/304014949/2026x+Refresh1+Invoking+actions
- version_number: 2
- version_date: `2026-04-29T17:12:22.231+02:00`
- ancestors: Versions of SysML v2 Evaluation Plugin Documentation > (2026x Refresh1) SysML v2 Evaluation Plugin Documentation > (2026x Refresh1) User guide
- labels: []

### NORMALIZED CONTENT

An action definition is a type of occurrence definition that specifies what an action is and how it can be performed. An action usage is a type of occurrence usage that represents the**actual use of one or more action definitions within a particular situation or context.

You can invoke action definitions and action usages as described below.

To invoke an action definition or action usage

1. Create and define an action definition or action usage. For instructions, refer to the SysML v2 Plugin documentation .
2. Create an expression that invokes the action, for example, by defining an attribute whose value is computed through the action invocation.
3. Access a specific output of the action invocation in one of the following ways:
  - Use the dot notation in the invocation expression. ExampleactiondefcalculateCircleParameters{ 
inradius:Real; 
outdiameter:Real=radius*2; 
outcircumference:Real=diameter*3.14; 
outarea:Real=radius*radius*3.14; 
} 
partwheel{ 
attributeradius:Real=12; 
attributearea:Real=calculateCircleParameters(radius).area; 
}
  - Create a feature that stores the invocation result, e.g., actionInvoke , and then select specific outputs using dot notation. ExampleactiondefcalculateCircleParameters{ 
inradius:Real; 
outdiameter:Real=radius*2; 
outcircumference:Real=diameter*3.14; 
outarea:Real=radius*radius*3.14; 
} 
partwheel{ 
attributeradius:Real=12; 
actionInvoke=calculateCircleParameters(radius); 
attributearea:Real=actionInvoke.area; 
attributeperimeter:Real=actionInvoke.circumference; 
}
4. Evaluate an element whose value depends on the action invocation (e.g., the area or perimeter attribute in the above examples). For more information, see [CONFLUENCE_PAGE title='(2026x Refresh1) Evaluating model elements' space=''] .

The evaluation results are displayed in the**SysML v2 Model Evaluation**console.

##### Defining calculation return in other script languages

When defining an action using a textual representation element, you can implement its behavior using an external scripting language. Supported languages include JavaScript, Groovy, Beanshell, Python (via Jython), and MATLAB. Only primitive types such as Integer, Real, Boolean, and String are supported as input and output parameters.

#### NOTE: Using MATLAB

Using MATLAB

To evaluate scripts defined in the MATLAB syntax:

- [CONFLUENCE_PAGE title='(2026x Refresh1) Integration with MATLAB' space=''] .
- The language must be specified as "MATLAB" (case sensitive).

#### PANEL: Example

Example

actiondefcounter{ 
inoutcount:Real:=0; 
language"groovy"/* count=count+1 */} 
} 
attributestartCount: Integer = counter().count//The result will be 1 because there is no input 
attributecontinueCount: Integer = counter(startCount).count//The result will be 2. Input overrides the initial value set in the parameter.

Actions also support "ToolExecution", which allows mapping features with different names between the SysML v2 model and MATLAB scripts.

#### PANEL: Example

Example

actioncomputeStoppingDistance { 
privateimportAnalysisTooling::*; 
@ToolExecution { 
:>> toolName ="MATLAB"; 
:>> uri ="run('C:/custom/path/to/StoppingAnalysisExec.m')"; 
} 
inmass : Real = vehicle.grossMass /4{@ToolVariable { name ="m"; }}; 
inspeed : Real = vehicle.speed /3.6{@ToolVariable { name ="v0"; }}; 
outDistance : Real = vehicle.stoppingDistance {@ToolVariable { name ="stoppingDistance"; }}; 
outkineticEnergy : Real = vehicle.kineticEnergy {@ToolVariable { name ="e"; }};

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>An action definition is a type of occurrence definition that specifies what an action is and how it can be performed. An action usage is a type of occurrence usage that represents the<em> </em>actual use of one or more action definitions within a particular situation or context.</p><p>You can invoke action definitions and action usages as described below.</p><p>To invoke an action definition or action usage</p><hr /><ol><li data-uuid="186c59fe-bc20-4821-acfd-955ef255002b">Create and define an action definition or action usage. For instructions, refer to the <a href="https://docs.nomagic.com/SYSML2P/?contextKey=creating-actions&amp;version=2026x Refresh1">SysML v2 Plugin documentation</a>.</li><li data-uuid="01127edb-6d1d-48c6-94c3-4218653fb14c">Create an expression that invokes the action, for example, by defining an attribute whose value is computed through the action invocation.</li><li data-uuid="61815bdb-074f-46db-b970-4f5f00c367cc"><span style="color:var(--ds-text,#172b4d);">Access a specific output of the action invocation in one of the following ways:</span><ul><li data-uuid="d874b0ac-0a93-459e-b58a-feb069b04110"><span style="color:var(--ds-text,#172b4d);">Use the dot notation in the invocation expression.<br /></span><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="fdfd9bdc-4046-4997-a249-ad9e5c74d2de"><ac:parameter ac:name="title">Example</ac:parameter><ac:rich-text-body><p><span style="color:var(--ds-text-accent-blue,#0055cc);">action</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">def</span><span style="color:var(--ds-chart-gray-bold,#8590a2);"> </span><span style="color:var(--ds-text-accent-teal,#206a83);">calculateCircleParameters</span><span style="color:var(--ds-text,#000000);"> {</span><br /><span style="color:var(--ds-text,#000000);">            </span><span style="color:var(--ds-text-accent-blue,#0055cc);">in</span><span style="color:var(--ds-chart-gray-bold,#8590a2);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">radius</span><span style="color:var(--ds-text,#000000);"> : </span><span style="color:var(--ds-text-accent-teal,#206a83);">Real</span><span style="color:var(--ds-text,#000000);">;</span><br /><span style="color:var(--ds-text,#000000);">            </span><span style="color:var(--ds-text-accent-blue,#0055cc);">out</span><span style="color:var(--ds-chart-gray-bold,#8590a2);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">diameter</span><span style="color:var(--ds-text,#000000);"> : </span><span style="color:var(--ds-text-accent-teal,#206a83);">Real</span><span style="color:var(--ds-text,#000000);"> = </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">radius</span><span style="color:var(--ds-text,#000000);"> * </span><span style="color:var(--ds-background-accent-green-bolder,#1f845a);">2</span><span style="color:var(--ds-text,#000000);">;</span><br /><span style="color:var(--ds-text,#000000);">            </span><span style="color:var(--ds-text-accent-blue,#0055cc);">out</span><span style="color:var(--ds-chart-gray-bold,#8590a2);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">circumference</span><span style="color:var(--ds-text,#000000);"> : </span><span style="color:var(--ds-text-accent-teal,#206a83);">Real</span><span style="color:var(--ds-text,#000000);"> = </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">diameter</span><span style="color:var(--ds-text,#000000);"> * </span><span style="color:var(--ds-background-accent-green-bolder,#1f845a);">3.14</span><span style="color:var(--ds-text,#000000);">;</span><br /><span style="color:var(--ds-text,#000000);">            </span><span style="color:var(--ds-text-accent-blue,#0055cc);">out</span><span style="color:var(--ds-chart-gray-bold,#8590a2);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">area</span><span style="color:var(--ds-text,#000000);"> : </span><span style="color:var(--ds-text-accent-teal,#206a83);">Real</span><span style="color:var(--ds-text,#000000);"> = </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">radius</span><span style="color:var(--ds-text,#000000);"> * </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">radius</span><span style="color:var(--ds-text,#000000);"> * </span><span style="color:var(--ds-background-accent-green-bolder,#1f845a);">3.14</span><span style="color:var(--ds-text,#000000);">;</span><br /><span style="color:var(--ds-text,#000000);">        }</span><br /><span style="color:var(--ds-text-accent-blue,#0055cc);">part</span><span style="color:var(--ds-chart-gray-bold,#8590a2);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">wheel</span><span style="color:var(--ds-text,#000000);"> {</span><br /><span style="color:var(--ds-text,#000000);">            </span><span style="color:var(--ds-text-accent-blue,#0055cc);">attribute</span><span style="color:var(--ds-chart-gray-bold,#8590a2);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">radius</span><span style="color:var(--ds-text,#000000);"> : </span><span style="color:var(--ds-text-accent-teal,#206a83);">Real</span><span style="color:var(--ds-text,#000000);"> = </span><span style="color:var(--ds-background-accent-green-bolder,#1f845a);">12</span><span style="color:var(--ds-text,#000000);">;</span><br /><span style="color:var(--ds-text,#000000);">            </span><span style="color:var(--ds-text-accent-blue,#0055cc);">attribute</span><span style="color:var(--ds-chart-gray-bold,#8590a2);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">area</span><span style="color:var(--ds-text,#000000);"> : </span><span style="color:var(--ds-text-accent-teal,#206a83);">Real</span><span style="color:var(--ds-text,#000000);"> = </span><span style="color:var(--ds-text-accent-teal,#206a83);">calculateCircleParameters</span><span style="color:var(--ds-text,#000000);">(</span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">radius</span><span style="color:var(--ds-text,#000000);">).</span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">area</span><span style="color:var(--ds-text,#000000);">;</span><br /><span style="color:var(--ds-text,#000000);">        }</span></p></ac:rich-text-body></ac:structured-macro><span style="color:var(--ds-text,#172b4d);"><br /></span></li><li data-uuid="3e402f5a-7e3d-4a75-8461-7cc760912742"><span style="color:var(--ds-text,#172b4d);">Create a feature that stores the invocation result, e.g., </span><em>actionInvoke</em>, <span style="color:var(--ds-text,#172b4d);">and then select specific outputs using dot notation.<br /></span><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="8fc65334-9f57-4157-9c1b-749899816c3f"><ac:parameter ac:name="title">Example</ac:parameter><ac:rich-text-body><p><span style="color:var(--ds-text-accent-blue,#0055cc);">action</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">def</span><span style="color:var(--ds-chart-gray-bold,#8590a2);"> </span><span style="color:var(--ds-text-accent-teal,#206a83);">calculateCircleParameters</span><span style="color:var(--ds-text,#000000);"> {</span><br /><span style="color:var(--ds-text,#000000);">            </span><span style="color:var(--ds-text-accent-blue,#0055cc);">in</span><span style="color:var(--ds-chart-gray-bold,#8590a2);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">radius</span><span style="color:var(--ds-text,#000000);"> : </span><span style="color:var(--ds-text-accent-teal,#206a83);">Real</span><span style="color:var(--ds-text,#000000);">;</span><br /><span style="color:var(--ds-text,#000000);">            </span><span style="color:var(--ds-text-accent-blue,#0055cc);">out</span><span style="color:var(--ds-chart-gray-bold,#8590a2);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">diameter</span><span style="color:var(--ds-text,#000000);"> : </span><span style="color:var(--ds-text-accent-teal,#206a83);">Real</span><span style="color:var(--ds-text,#000000);"> = </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">radius</span><span style="color:var(--ds-text,#000000);"> * </span><span style="color:var(--ds-background-accent-green-bolder,#1f845a);">2</span><span style="color:var(--ds-text,#000000);">;</span><br /><span style="color:var(--ds-text,#000000);">            </span><span style="color:var(--ds-text-accent-blue,#0055cc);">out</span><span style="color:var(--ds-chart-gray-bold,#8590a2);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">circumference</span><span style="color:var(--ds-text,#000000);"> : </span><span style="color:var(--ds-text-accent-teal,#206a83);">Real</span><span style="color:var(--ds-text,#000000);"> = </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">diameter</span><span style="color:var(--ds-text,#000000);"> * </span><span style="color:var(--ds-background-accent-green-bolder,#1f845a);">3.14</span><span style="color:var(--ds-text,#000000);">;</span><br /><span style="color:var(--ds-text,#000000);">            </span><span style="color:var(--ds-text-accent-blue,#0055cc);">out</span><span style="color:var(--ds-chart-gray-bold,#8590a2);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">area</span><span style="color:var(--ds-text,#000000);"> : </span><span style="color:var(--ds-text-accent-teal,#206a83);">Real</span><span style="color:var(--ds-text,#000000);"> = </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">radius</span><span style="color:var(--ds-text,#000000);"> * </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">radius</span><span style="color:var(--ds-text,#000000);"> * </span><span style="color:var(--ds-background-accent-green-bolder,#1f845a);">3.14</span><span style="color:var(--ds-text,#000000);">;</span><br /><span style="color:var(--ds-text,#000000);">        }</span><br /><span style="color:var(--ds-text-accent-blue,#0055cc);">part</span><span style="color:var(--ds-chart-gray-bold,#8590a2);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">wheel</span><span style="color:var(--ds-text,#000000);"> {</span><br /><span style="color:var(--ds-text,#000000);">            </span><span style="color:var(--ds-text-accent-blue,#0055cc);">attribute</span><span style="color:var(--ds-chart-gray-bold,#8590a2);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">radius</span><span style="color:var(--ds-text,#000000);"> : </span><span style="color:var(--ds-text-accent-teal,#206a83);">Real</span><span style="color:var(--ds-text,#000000);"> = </span><span style="color:var(--ds-background-accent-green-bolder,#1f845a);">12</span><span style="color:var(--ds-text,#000000);">;</span><br /><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">            actionInvoke</span><span style="color:var(--ds-text,#000000);"> = </span><span style="color:var(--ds-text-accent-teal,#206a83);">calculateCircleParameters</span><span style="color:var(--ds-text,#000000);">(</span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">radius</span><span style="color:var(--ds-text,#000000);">);</span><br /><span style="color:var(--ds-text,#000000);">            </span><span style="color:var(--ds-text-accent-blue,#0055cc);">attribute</span><span style="color:var(--ds-chart-gray-bold,#8590a2);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">area</span><span style="color:var(--ds-text,#000000);"> : </span><span style="color:var(--ds-text-accent-teal,#206a83);">Real</span><span style="color:var(--ds-text,#000000);"> = </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">actionInvoke</span><span style="color:var(--ds-text,#000000);">.</span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">area</span><span style="color:var(--ds-text,#000000);">;</span><br /><span style="color:var(--ds-text,#000000);">            </span><span style="color:var(--ds-text-accent-blue,#0055cc);">attribute</span><span style="color:var(--ds-chart-gray-bold,#8590a2);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">perimeter</span><span style="color:var(--ds-text,#000000);"> : </span><span style="color:var(--ds-text-accent-teal,#206a83);">Real</span><span style="color:var(--ds-text,#000000);"> = </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">actionInvoke</span><span style="color:var(--ds-text,#000000);">.</span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">circumference</span><span style="color:var(--ds-text,#000000);">;</span><br /><span style="color:var(--ds-text,#000000);">        }</span></p></ac:rich-text-body></ac:structured-macro><span style="color:var(--ds-text,#172b4d);"><br /></span></li></ul></li><li data-uuid="a234ed53-86bc-4886-8fcd-4930fa75db86">Evaluate an element whose value depends on the action invocation (e.g., the <em>area</em> or <em>perimeter</em> attribute in the above examples). For more information, see <ac:link><ri:page ri:content-title="(2026x Refresh1) Evaluating model elements" /></ac:link>.</li></ol><p><span style="color:var(--ds-text,#172b4d);">The evaluation results are displayed in the </span><strong>SysML v2 Model Evaluation</strong><span style="color:var(--ds-text,#172b4d);"><span> </span>console.</span></p><h3><span style="color:var(--ds-text,#172b4d);">Defining calculation return in other script languages</span></h3><p>When defining an action using a <span style="color:var(--ds-text,#172b4d);">textual representation element</span>, you can implement its behavior using an external scripting language. Supported languages include JavaScript, Groovy, Beanshell, Python (via Jython), and MATLAB. Only primitive types such as Integer, Real, Boolean, and String are supported as input and output parameters.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="7112b935-00f1-4054-b9ef-71f2449b1345"><ac:parameter ac:name="title">Using MATLAB</ac:parameter><ac:rich-text-body><p>To evaluate scripts defined in the MATLAB syntax:</p><ul><li data-uuid="9f0620ea-5fdb-4dca-aab6-0c50f3e23d60"><ac:link><ri:page ri:content-title="(2026x Refresh1) Integration with MATLAB" /><ac:plain-text-link-body><![CDATA[MATLAB must be integrated with your modeling tool]]></ac:plain-text-link-body></ac:link>.</li><li data-uuid="b5ccd0d5-2a5d-499e-b9d5-96029ce985bf">The language must be specified as &quot;MATLAB&quot; (case sensitive).</li></ul></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="c0d6ec98-2f53-4b20-8d8e-4d37f62150b8"><ac:parameter ac:name="title">Example</ac:parameter><ac:rich-text-body><p><span style="color:var(--ds-text-accent-blue,#0055cc);">action</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">def</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-teal,#206a83);">counter</span><span style="color:var(--ds-text,#000000);"> {</span><br /><span style="color:var(--ds-text,#000000);">    </span><span style="color:var(--ds-background-accent-red-bolder,#c9372c);"> </span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-background-accent-red-bolder,#c9372c);"> </span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-background-accent-red-bolder,#c9372c);"> </span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-background-accent-red-bolder,#c9372c);">  </span><span style="color:var(--ds-text-accent-blue,#0055cc);">inout</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">count</span><span style="color:var(--ds-text,#000000);"> : </span><span style="color:var(--ds-text-accent-teal,#206a83);">Real</span><span style="color:var(--ds-text,#000000);"> := </span><span style="color:var(--ds-background-accent-green-bolder,#1f845a);">0</span><span style="color:var(--ds-text,#000000);">;</span><br /><span style="color:var(--ds-text,#000000);">            </span><span style="color:var(--ds-text-accent-blue,#0055cc);">language</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-red,#ae2e24);">&quot;groovy&quot;</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-green-bolder,#164b35);">/* count=count+1 */</span><span style="color:var(--ds-text,#000000);"> } </span><br /><span style="color:var(--ds-text,#000000);">        }</span><br /><span style="color:var(--ds-text-accent-blue,#0055cc);">attribute</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">startCount</span><span style="color:var(--ds-text,#000000);"> : Integer = counter().count </span><span style="color:var(--ds-text-accent-green-bolder,#164b35);">//The result will be 1 because there is no input </span><br /><span style="color:var(--ds-text-accent-blue,#0055cc);">attribute</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">continueCount</span><span style="color:var(--ds-text,#000000);"> : Integer = counter(</span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">startCount</span><span style="color:var(--ds-text,#000000);">).count </span><span style="color:var(--ds-text-accent-green-bolder,#164b35);">//The result will be 2. Input overrides the initial value set in the parameter.</span></p></ac:rich-text-body></ac:structured-macro><p>Actions also support &quot;ToolExecution&quot;, <span data-teams="true">which allows mapping features with different names between the SysML v2 model and MATLAB scripts.</span></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="71f0bc6d-8deb-4cb2-9366-e6f7da3c2ea4"><ac:parameter ac:name="title">Example</ac:parameter><ac:rich-text-body><p><span style="color:var(--ds-text-accent-blue,#0055cc);">action</span><span style="color:var(--ds-text,#000000);"> computeStoppingDistance {</span><br /><span style="color:var(--ds-text,#000000);">            </span><span style="color:var(--ds-text-accent-blue,#0055cc);">private</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">import</span><span style="color:var(--ds-text,#000000);"> AnalysisTooling::*;</span><br /><span style="color:var(--ds-text,#000000);">            @ToolExecution {</span><br /><span style="color:var(--ds-text,#000000);">                :&gt;&gt; toolName = </span><span style="color:var(--ds-text-accent-red,#ae2e24);">&quot;MATLAB&quot;</span><span style="color:var(--ds-text,#000000);">;</span><br /><span style="color:var(--ds-text,#000000);">                :&gt;&gt; uri = </span><span style="color:var(--ds-text-accent-red,#ae2e24);">&quot;run('C:/custom/path/to/StoppingAnalysisExec.m')&quot;</span><span style="color:var(--ds-text,#000000);">;</span><br /><span style="color:var(--ds-text,#000000);">            }</span><br /><span style="color:var(--ds-text,#000000);">            </span><span style="color:var(--ds-text-accent-blue,#0055cc);">in</span><span style="color:var(--ds-text,#000000);"> mass : Real = vehicle.grossMass / </span><span style="color:var(--ds-background-accent-green-bolder,#1f845a);">4</span><span style="color:var(--ds-text,#000000);"> {@ToolVariable { name = </span><span style="color:var(--ds-text-accent-red,#ae2e24);">&quot;m&quot;</span><span style="color:var(--ds-text,#000000);">; }};</span><br /><span style="color:var(--ds-text,#000000);">            </span><span style="color:var(--ds-text-accent-blue,#0055cc);">in</span><span style="color:var(--ds-text,#000000);"> speed : Real = vehicle.speed / </span><span style="color:var(--ds-background-accent-green-bolder,#1f845a);">3.6</span><span style="color:var(--ds-text,#000000);"> {@ToolVariable { name = </span><span style="color:var(--ds-text-accent-red,#ae2e24);">&quot;v0&quot;</span><span style="color:var(--ds-text,#000000);">; }};</span><br /><span style="color:var(--ds-text,#000000);">            </span><span style="color:var(--ds-text-accent-blue,#0055cc);">out</span><span style="color:var(--ds-text,#000000);"> Distance : Real = vehicle.stoppingDistance {@ToolVariable { name = </span><span style="color:var(--ds-text-accent-red,#ae2e24);">&quot;stoppingDistance&quot;</span><span style="color:var(--ds-text,#000000);">; }};</span><br /><span style="color:var(--ds-text,#000000);">            </span><span style="color:var(--ds-text-accent-blue,#0055cc);">out</span><span style="color:var(--ds-text,#000000);"> kineticEnergy : Real = vehicle.kineticEnergy {@ToolVariable { name = </span><span style="color:var(--ds-text-accent-red,#ae2e24);">&quot;e&quot;</span><span style="color:var(--ds-text,#000000);">; }};</span></p></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=304014905 space=SYSML2EP version=2 -->
## PAGE 00011: (2026x Refresh1) Invoking calculations

- page_id: `304014905`
- space_key: `SYSML2EP`
- source_url: https://docs.nomagic.com/spaces/SYSML2EP/pages/304014905/2026x+Refresh1+Invoking+calculations
- version_number: 2
- version_date: `2026-04-29T17:12:22.003+02:00`
- ancestors: Versions of SysML v2 Evaluation Plugin Documentation > (2026x Refresh1) SysML v2 Evaluation Plugin Documentation > (2026x Refresh1) User guide
- labels: []

### NORMALIZED CONTENT

A calculation specifies a reusable computation that returns a result in the result parameter. In addition to its parameters, a calculation may have features that are calculation or action usages, which carry out steps in the computation of the calculation result. A calculation always has a result parameter, which can be declared as an out parameter using the keyword*return*instead of*out*.

You can invoke calculation definitions and calculation usages as described below.

To invoke a calculation definition or calculation usage

1. Create and define a calculation definition or calculation usage. For instructions, refer to the SysML v2 Plugin documentation .
2. Create an invocation expression, e.g., an attribute, whose value is the result of the calculation.
3. Assign the created calculation to the invocation expression and define the calculation inputs. When defining the calculation inputs, keep in mind that they will be taken in the same order as defined in the calculation. ExamplecalcdefArea{ 
inlength:Real; 
inwidth:Real; 
returnresult:Real; 
result=length*width; 
} 
partpad{ 
attributesurfaceArea:Real=Area(centerLength, width); 
}
4. Evaluate the invocation expression (e.g., the surfaceArea attribute in the above example). For more information, see [CONFLUENCE_PAGE title='(2026x Refresh1) Evaluating model elements' space=''] .

The evaluation results are displayed in the**SysML v2 Model Evaluation**console.

##### Defining calculation return in other script languages

When specifying the return of a calculation, you can use a textual representation element to evaluate scripts defined in other script languages. Supported languages include Javascript, Groovy, Beanshell, Python (Python support is based on Jython), and MATLAB.Only primitive input and output types, e.g., String, Real, Boolean, etc., are supported.

#### PANEL: Example

Example

calcdefArea15{ 
inlength:Real; 
inwidth:Real; 
returnresult:Real; 
language"beanshell"/* result=length * width */

}

#### NOTE: Using MATLAB

Using MATLAB

To evaluate scripts defined in the MATLAB syntax:

- [CONFLUENCE_PAGE title='(2026x Refresh1) Integration with MATLAB' space=''] .
- The language must be specified as "MATLAB" (case sensitive).

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><span style="color:var(--ds-text,#172b4d);">A calculation specifies a reusable computation that returns a result in the result parameter. In addition to its parameters, a calculation may have features that are calculation or action usages, which carry out steps in the computation of the calculation result. A calculation always has a result parameter, which can be declared as an out parameter using the keyword<span> </span></span><em style="text-align: left;">return</em><span style="color:var(--ds-text,#172b4d);"><span> </span>instead of<span> </span></span><em style="text-align: left;">out</em><span style="color:var(--ds-text,#172b4d);">.</span></p><p>You can invoke calculation definitions and calculation usages as described below.</p><p>To invoke a calculation definition or calculation usage</p><hr /><ol><li>Create and define a calculation definition or calculation usage. For instructions, refer to the <a href="https://docs.nomagic.com/SYSML2P/?contextKey=calculation&amp;version=2026x Refresh1">SysML v2 Plugin documentation</a>.</li><li>Create an invocation expression, e.g., an attribute, whose value is the result of the calculation.</li><li>Assign the created calculation to the invocation expression and define the calculation inputs.<br /><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="e811507c-c932-4f1e-b7f3-724fd61f8477"><ac:rich-text-body><p>When defining the calculation inputs, keep in mind that they will be taken in the same order as defined in the calculation.</p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="b5afa193-4f21-47eb-bec6-8cf7cb29b5ff"><ac:parameter ac:name="title">Example</ac:parameter><ac:rich-text-body><p><span style="color:var(--ds-text-accent-blue,#0055cc);">calc</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">def</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-teal,#206a83);">Area</span><span style="color:var(--ds-text,#000000);"> {</span><br /><span style="color:var(--ds-text,#000000);">            </span><span style="color:var(--ds-text-accent-blue,#0055cc);">in</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">length</span><span style="color:var(--ds-text,#000000);"> : </span><span style="color:var(--ds-text-accent-teal,#206a83);">Real</span><span style="color:var(--ds-text,#000000);">;</span><br /><span style="color:var(--ds-text,#000000);">            </span><span style="color:var(--ds-text-accent-blue,#0055cc);">in</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">width</span><span style="color:var(--ds-text,#000000);"> : </span><span style="color:var(--ds-text-accent-teal,#206a83);">Real</span><span style="color:var(--ds-text,#000000);">;</span><br /><span style="color:var(--ds-text,#000000);">            </span><span style="color:var(--ds-text-accent-blue,#0055cc);">return</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">result</span><span style="color:var(--ds-text,#000000);"> : </span><span style="color:var(--ds-text-accent-teal,#206a83);">Real</span><span style="color:var(--ds-text,#000000);">;</span><br /><span style="color:var(--ds-text,#000000);">            </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">result</span><span style="color:var(--ds-text,#000000);"> = </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">length</span><span style="color:var(--ds-text,#000000);"> * </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">width</span><span style="color:var(--ds-text,#000000);">;</span><br /><span style="color:var(--ds-text,#000000);"> }       </span><br /><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">part</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">pad</span><span style="color:var(--ds-text,#000000);"> {</span><br /><span style="color:var(--ds-text,#000000);">            </span><span style="color:var(--ds-text-accent-blue,#0055cc);">attribute</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">surfaceArea</span><span style="color:var(--ds-text,#000000);"> : </span><span style="color:var(--ds-text-accent-teal,#206a83);">Real</span><span style="color:var(--ds-text,#000000);"> = </span><span style="color:var(--ds-text-accent-teal,#206a83);">Area</span><span style="color:var(--ds-text,#000000);">(centerLength, width);</span><br /><span style="color:var(--ds-text,#000000);"> }</span></p></ac:rich-text-body></ac:structured-macro></li><li>Evaluate the invocation expression (e.g., the <em>surfaceArea</em> attribute in the above example). For more information, see <ac:link><ri:page ri:content-title="(2026x Refresh1) Evaluating model elements" /></ac:link>.</li></ol><p><span style="color:var(--ds-text,#172b4d);">The evaluation results are displayed in the </span><strong>SysML v2 Model Evaluation</strong><span style="color:var(--ds-text,#172b4d);"><span> </span>console.</span></p><h3><span style="color:var(--ds-text,#172b4d);">Defining calculation return in other script languages</span></h3><p style="text-align: left;">When specifying the return of a calculation, you can use a <span style="color:var(--ds-text,#172b4d);">textual representation element to evaluate scripts defined in other script languages. Supported languages include Javascript, Groovy, Beanshell, Python (Python support is based on Jython), and MATLAB. </span><span>Only</span> primitive input and output types, e.g., String, Real, Boolean, etc., are supported.</p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="c0d6ec98-2f53-4b20-8d8e-4d37f62150b8"><ac:parameter ac:name="title">Example</ac:parameter><ac:rich-text-body><p><span style="color:var(--ds-text-accent-blue,#0055cc);">calc</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">def</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-teal,#206a83);">Area15</span><span style="color:var(--ds-text,#000000);"> {</span><br /><span style="color:var(--ds-text,#000000);">        </span><span style="color:var(--ds-text-accent-blue,#0055cc);">in</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">length</span><span style="color:var(--ds-text,#000000);"> : </span><span style="color:var(--ds-text-accent-teal,#206a83);">Real</span><span style="color:var(--ds-text,#000000);">;</span><br /><span style="color:var(--ds-text,#000000);">        </span><span style="color:var(--ds-text-accent-blue,#0055cc);">in</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">width</span><span style="color:var(--ds-text,#000000);"> : </span><span style="color:var(--ds-text-accent-teal,#206a83);">Real</span><span style="color:var(--ds-text,#000000);">;</span><br /><span style="color:var(--ds-text,#000000);">        </span><span style="color:var(--ds-text-accent-blue,#0055cc);">return</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">result</span><span style="color:var(--ds-text,#000000);"> : </span><span style="color:var(--ds-text-accent-teal,#206a83);">Real</span><span style="color:var(--ds-text,#000000);">;</span><br /><span style="color:var(--ds-text,#000000);">        </span><span style="color:var(--ds-text-accent-blue,#0055cc);">language</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-red,#ae2e24);">&quot;beanshell&quot;</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-green-bolder,#164b35);">/* result=length * width */</span></p><p><span style="color:var(--ds-text,#000000);">}</span></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="7112b935-00f1-4054-b9ef-71f2449b1345"><ac:parameter ac:name="title">Using MATLAB</ac:parameter><ac:rich-text-body><p>To evaluate scripts defined in the MATLAB syntax:</p><ul><li><ac:link><ri:page ri:content-title="(2026x Refresh1) Integration with MATLAB" /><ac:plain-text-link-body><![CDATA[MATLAB must be integrated with your modeling tool]]></ac:plain-text-link-body></ac:link>.</li><li>The language must be specified as &quot;MATLAB&quot; (case sensitive).</li></ul></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=314180424 space=SYSML2EP version=1 -->
## PAGE 00012: (2026x Refresh1) Manipulating runtime values

- page_id: `314180424`
- space_key: `SYSML2EP`
- source_url: https://docs.nomagic.com/spaces/SYSML2EP/pages/314180424/2026x+Refresh1+Manipulating+runtime+values
- version_number: 1
- version_date: `2026-06-16T14:02:16.299+02:00`
- ancestors: Versions of SysML v2 Evaluation Plugin Documentation > (2026x Refresh1) SysML v2 Evaluation Plugin Documentation > (2026x Refresh1) User guide > (2026x Refresh1) Evaluation information in views
- labels: []

### NORMALIZED CONTENT

##### Entering and modifying initial runtime values

You can use views to enter new and modify existing initial runtime values during evaluation. When an initial runtime value is changed or entered, all evaluation results are automatically recalculated and requirements are reverified.

During runtime, you can modify only initial values indicated by the ":=" sign, which means they are not bound and can be adjusted for evaluation purposes.

To enter or modify an initial runtime value

1. Open a view and, in the view toolbar, click [ATTACHMENT filename='evaluate_button.png'] to evaluate it. To evaluate only a specific element in a view, select the element shape (press and hold the Shift key to select multiple shapes), then click [IMAGE alt='' src='']. Only the selected elements will be reevaluated after changing an initial runtime value.
2. Select the shape of the element whose value you want to enter or change and type a new value. Editable attributes are indicated by the ":=" sign. 
[IMAGE alt='' src='']
3. Press Enter or click anywhere in the view to enter the change.

After an initial runtime value is entered or changed, all bound expressions and invocations are automatically recalculated. If an expression or invocation is an initial value, it is only calculated during the first evaluation and will not be recalculated afterwards.

#### PANEL: Example

Example

attributea:=1;//'a' is an initial value that can be changed during runtime. 
attributeb=a*2;//'b' is a bound expression calculated during the initial evaluation (equals 2) and recalculated each time 'a' is changed. 
attributec:=b;//'c' is an initial expression calculated only during the initial evaluation (equals 2) and not recalculated at runtime (even if 'b' changes). However, 'c' can be changed during runtime.

##### Saving runtime values to the model

After using model views to enter or modify initial runtime values, you can save these values to the model as described below.

You can not use model views to save modified values of inherited attributes. Only directly owned or redefined attribute values can be saved to the model.

To save runtime values to the model

1. In the view with new or modified runtime values, do one of the following:
  - To save all modified values, click the arrow next to [ATTACHMENT filename='evaluate_button.png'] in the view toolbar and select Save Modified Values to Model . If you have selected any attribute shapes with modified values in the view, only the selected values are saved. [IMAGE alt='' src='']
  - To save the selected modified values, right-click the selected attribute shapes and select Save Modified Values to Model . You can select multiple shapes by pressing and holding the **Shift** key.
  - To save a single selected modified value, click [ATTACHMENT filename='save_modified_values_to_model.png'] in the smart manipulator of the selected attribute shape. [ATTACHMENT filename='saving_single_modified_value.png']

##### Recalculating bound values manually

When an initial runtime value is entered or changed during evaluation, all bound values are automatically recalculated, and requirements are reverified. However, this behavior can be changed by disabling the automatic bound value recalculation in the Project Options as described below.

To disable or enable bound value recalculation

1. In the main menu, go to Options > Project .
2. In the Project Options dialog, select Evaluation .
3. On the right side of the dialog, set the Auto Recalculate Bound Values option to false or true (default) to disable or enable the automatic bound value recalculation. [ATTACHMENT filename='auto_recalculate_bound_values_option.png']
4. Click OK to close the dialog.

To recalculate the evaluation results manually

- Do one of the following:
  - In the view toolbar, click [ATTACHMENT filename='evaluate_button.png'] .
  - In the view toolbar, click the arrow next to [ATTACHMENT filename='evaluate_button.png'] and select Refresh .
  - Select any shape in the view and, in the smart manipulator, click [ATTACHMENT filename='evaluate_button.png'] .
  - Right-click any shape in the view and select Evaluate .

When invoking recalculation from a specific element shape, all of the evaluation results in the view are recalculated.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<h3><span>Entering and modifying initial runtime values</span></h3><p><span>You can use views to enter new and modify existing initial runtime values during evaluation. When an initial runtime value is changed or entered, all evaluation results are automatically recalculated and requirements are reverified.</span></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="ee2a8342-af11-4191-b472-0599c88c7e22"><ac:rich-text-body><p><span> During runtime, you can modify only initial values indicated by the &quot;:=&quot; sign, which means they are not bound and can be adjusted for evaluation purposes.</span></p></ac:rich-text-body></ac:structured-macro><p>To enter or modify an initial runtime value</p><hr /><ol><li data-uuid="91225f39-b90e-43a0-b687-d36d541707f4">Open a view and, in the view toolbar, click <ac:image ac:thumbnail="true" ac:height="14"><ri:attachment ri:filename="evaluate_button.png"><ri:page ri:space-key="SYSML2EP" ri:content-title="(2026x Refresh1) Manipulating runtime values" /></ri:attachment></ac:image> to evaluate it.<br /><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="5d95554f-2cbb-4aef-9064-73393c7c7eab"><ac:rich-text-body><p>To evaluate only a specific element in a view, select the element shape (press and hold the Shift key to select multiple shapes), then click <ac:image ac:thumbnail="true" ac:height="14"><ri:attachment ri:filename="evaluate_button.png"><ri:page ri:space-key="SYSML2EP" ri:content-title="(2026x Refresh1) Manipulating runtime values" /></ri:attachment></ac:image>. Only the selected elements will be reevaluated after changing an initial runtime value.</p></ac:rich-text-body></ac:structured-macro></li><li data-uuid="4df8633a-4210-48d5-b492-df4ba57cc6f4">Select the shape of the element whose value you want to enter or change and type a new value. Editable <span>attributes are indicated by the &quot;:=&quot; sign.<br /><ac:image><ri:attachment ri:filename="editing_runtime_values.png"><ri:page ri:space-key="SYSML2EP" ri:content-title="(2026x Refresh1) Manipulating runtime values" /></ri:attachment></ac:image></span></li><li data-uuid="33d6cfe6-7227-47fb-a176-39c9e488af01"><span>Press Enter or click anywhere in the view to enter the change.</span></li></ol><p><span>After an initial runtime value is entered or changed, all bound expressions and invocations are automatically recalculated. I<span style="color:var(--ds-text,#172b4d);">f an expression or invocation is an initial value, it is only calculated during the first evaluation and will not be recalculated afterwards.</span></span></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="32cf2c6b-ac6d-4788-af7e-27d09056b017"><ac:parameter ac:name="title">Example</ac:parameter><ac:rich-text-body><p><span style="color:var(--ds-text-accent-blue,#0055cc);">attribute</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">a</span><span style="color:var(--ds-text,#000000);"> := </span><span style="color:var(--ds-background-accent-green-bolder,#1f845a);">1</span><span style="color:var(--ds-text,#000000);">; </span><span style="color:var(--ds-text-accent-green-bolder,#164b35);">//'a' is an initial value that can be changed during runtime.</span><br /><span style="color:var(--ds-text-accent-blue,#0055cc);">attribute</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">b</span><span style="color:var(--ds-text,#000000);"> = </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">a</span><span style="color:var(--ds-text,#000000);"> * </span><span style="color:var(--ds-background-accent-green-bolder,#1f845a);">2</span><span style="color:var(--ds-text,#000000);">; </span><span style="color:var(--ds-text-accent-green-bolder,#164b35);">//'b' is a bound expression calculated during the initial evaluation (equals 2) and recalculated each time 'a' is changed.</span><br /><span style="color:var(--ds-text-accent-blue,#0055cc);">attribute</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">c</span><span style="color:var(--ds-text,#000000);"> := </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">b</span><span style="color:var(--ds-text,#000000);">; </span><span style="color:var(--ds-text-accent-green-bolder,#164b35);">//'c' is an initial expression calculated only during the initial evaluation (equals 2) and not recalculated at runtime (even if 'b' changes). However, 'c' can be changed during runtime.</span></p></ac:rich-text-body></ac:structured-macro><h3>Saving runtime values to the model</h3><p style="text-align: left;">After using model views to enter or modify initial runtime values, you can save these values to the model as described below.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="84dfc085-0aca-4a85-a0dc-2d74d457ff90"><ac:rich-text-body><p><span>You can not use model views to save modified values of inherited attributes. Only directly owned or redefined attribute values can be saved to the model.</span></p></ac:rich-text-body></ac:structured-macro><p style="text-align: left;"><br /></p><p style="text-align: left;">To save runtime values to the model</p><hr /><ol><li style="text-align: left;" data-uuid="347f645e-8f50-4fc7-94e5-da374198013c">In the view with new or modified runtime values, do one of the following:<ul><li style="text-align: left;" data-uuid="989ead07-669a-44f3-9f66-6cc86073992c">To save all modified values, click the arrow next to <ac:image ac:thumbnail="true" ac:height="14"><ri:attachment ri:filename="evaluate_button.png"><ri:page ri:space-key="SYSML2EP" ri:content-title="(2026x Refresh1) Manipulating runtime values" /></ri:attachment></ac:image> in the view toolbar and select <strong>Save Modified Values to Model</strong>.<br /><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="16fabaf7-91ff-48ac-938d-3d28a84d663c"><ac:rich-text-body><p>If you have selected any attribute shapes with modified values in the view, only the selected values are saved.</p></ac:rich-text-body></ac:structured-macro><strong><ac:image><ri:attachment ri:filename="saving_all_modified_values.png"><ri:page ri:space-key="SYSML2EP" ri:content-title="(2026x Refresh1) Manipulating runtime values" /></ri:attachment></ac:image></strong></li><li style="text-align: left;" data-uuid="b6328fe2-20af-45ab-b540-fbff75a5712f">To save the selected modified values, right-click the selected attribute shapes and select <strong>Save Modified Values to Model</strong>.<br /><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="9ae9084d-e7e8-4123-858d-99d972918865"><ac:rich-text-body><p>You can select multiple shapes by pressing and holding the <strong>Shift</strong> key.</p></ac:rich-text-body></ac:structured-macro></li><li style="text-align: left;" data-uuid="a7fdec93-b08f-4c5d-bc7b-ab7a80fb9c55">To save a single selected modified value, click <ac:image><ri:attachment ri:filename="save_modified_values_to_model.png"><ri:page ri:space-key="SYSML2EP" ri:content-title="(2026x Refresh1) Manipulating runtime values" /></ri:attachment></ac:image> in the smart manipulator of the selected attribute shape.<br /><ac:image><ri:attachment ri:filename="saving_single_modified_value.png"><ri:page ri:space-key="SYSML2EP" ri:content-title="(2026x Refresh1) Manipulating runtime values" /></ri:attachment></ac:image></li></ul></li></ol><h3>Recalculating bound values manually</h3><p><span style="color:var(--ds-text,#172b4d);">When an initial runtime value is entered or changed during evaluation, all bound values are automatically recalculated, and requirements are reverified. However, this behavior can be changed by disabling the automatic bound value recalculation in the Project Options as described below.</span></p><p><span style="color:var(--ds-text,#172b4d);">To disable or enable bound value recalculation</span></p><hr /><ol><li data-uuid="38b3bb75-13ff-40e4-8ab9-3df0e523aa3b">In the main menu, go to <strong>Options</strong> &gt; <strong>Project</strong>.</li><li data-uuid="a0e7028b-0d16-4092-bc44-c8cd15ae8aa0">In the <strong>Project Options</strong> dialog, select <strong>Evaluation</strong>.</li><li data-uuid="b3c24023-6bc6-495a-a82c-3f81a81a1faf">On the right side of the dialog, set the <strong>Auto Recalculate Bound Values</strong> option to <em>false</em> or <em>true</em> (default) to disable or enable the automatic bound value recalculation.<br /><ac:image><ri:attachment ri:filename="auto_recalculate_bound_values_option.png"><ri:page ri:space-key="SYSML2EP" ri:content-title="(2026x Refresh1) Manipulating runtime values" /></ri:attachment></ac:image></li><li data-uuid="bbfb2ae5-ae56-4542-aa68-463b0887e512">Click <strong>OK</strong> to close the dialog.</li></ol><p><br />To recalculate the evaluation results manually</p><hr /><ul><li data-uuid="7cc29ad6-1196-4ee0-ad6b-e5ba3b2dccbe">Do one of the following:<ul><li data-uuid="3f7b35a0-4452-4449-a2ce-cfe8909d78e6">In the view toolbar, click <ac:image ac:thumbnail="true" ac:height="14"><ri:attachment ri:filename="evaluate_button.png"><ri:page ri:space-key="SYSML2EP" ri:content-title="(2026x Refresh1) Manipulating runtime values" /></ri:attachment></ac:image>.</li><li data-uuid="66c1ee57-f974-4122-a370-13010b0a69f8">In the view toolbar, click the arrow next to <ac:image ac:thumbnail="true" ac:height="14"><ri:attachment ri:filename="evaluate_button.png"><ri:page ri:space-key="SYSML2EP" ri:content-title="(2026x Refresh1) Manipulating runtime values" /></ri:attachment></ac:image> and select <strong>Refresh</strong>.</li><li data-uuid="51bfcd4c-fdd6-487c-8452-e71f6744e136">Select any shape in the view and, in the smart manipulator, click <ac:image ac:thumbnail="true" ac:height="14"><ri:attachment ri:filename="evaluate_button.png"><ri:page ri:space-key="SYSML2EP" ri:content-title="(2026x Refresh1) Manipulating runtime values" /></ri:attachment></ac:image>.</li><li data-uuid="008568e1-c44d-4140-afbe-d4eac412eebf">Right-click any shape in the view and select <strong>Evaluate</strong>.</li></ul></li></ul><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="39d660b6-3884-4ee5-88da-bdd541a57c75"><ac:rich-text-body><p>When invoking recalculation from a specific element shape, all of the evaluation results in the view are recalculated.</p></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=304014878 space=SYSML2EP version=1 -->
## PAGE 00013: (2026x Refresh1) Prerequisites

- page_id: `304014878`
- space_key: `SYSML2EP`
- source_url: https://docs.nomagic.com/spaces/SYSML2EP/pages/304014878/2026x+Refresh1+Prerequisites
- version_number: 1
- version_date: `2026-04-29T17:11:14.921+02:00`
- ancestors: Versions of SysML v2 Evaluation Plugin Documentation > (2026x Refresh1) SysML v2 Evaluation Plugin Documentation
- labels: []

### NORMALIZED CONTENT

To work with SysML v2 features, including model evaluation, the following software must be installed:

- One of the following CATIA Magic/No Magic modeling tools:
  - Cameo Systems Modeler (Enterprise Edition only)
  - Cameo Enterprise Architecture
  - Magic Cyber Systems Engineer
  - Magic Systems of Systems Architect
- The SysML v1 Plugin.
- Cameo Requirements Modeler.
- Cameo Simulation Toolkit or Magic Model Analyst.
- The SysML v2 Plugin. It provides the majority of the SysML v2 features, including the Textual Editor.
- The SysML v2 Evaluation Plugin. It allows you to conduct static evaluations of SysML v2 models (mathematical calculations, calculation usage evaluation, constraints evaluation, and requirements evaluation).

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>To work with SysML v2 features, including model evaluation, the following software must be installed:</p><ul><li data-uuid="c69be92d-d004-46d5-a2ee-c2ceb367ddc4"><span style="color:var(--ds-text,#172b4d);">One of the following CATIA Magic/No Magic modeling tools:</span><ul><li>Cameo Systems Modeler (Enterprise Edition only)</li><li>Cameo Enterprise Architecture</li><li>Magic Cyber Systems Engineer</li><li>Magic Systems of Systems Architect</li></ul></li><li>The SysML v1 Plugin.</li><li>Cameo Requirements Modeler.</li><li>Cameo Simulation Toolkit or Magic Model Analyst.</li><li>The SysML v2 Plugin. It provides the majority of the SysML v2 features, including the Textual Editor.</li><li><p class="auto-cursor-target"><span>The SysML v2 Evaluation Plugin. It allows you to conduct static evaluations of SysML v2 models (mathematical calculations, calculation usage evaluation, constraints evaluation, and requirements evaluation).</span></p></li></ul>
````

<!--NOMAGIC_PAGE id=304015506 space=SYSML2EP version=1 -->
## PAGE 00014: (2026x Refresh1) Project options

- page_id: `304015506`
- space_key: `SYSML2EP`
- source_url: https://docs.nomagic.com/spaces/SYSML2EP/pages/304015506/2026x+Refresh1+Project+options
- version_number: 1
- version_date: `2026-05-06T14:10:31.274+02:00`
- ancestors: Versions of SysML v2 Evaluation Plugin Documentation > (2026x Refresh1) SysML v2 Evaluation Plugin Documentation
- labels: []

### NORMALIZED CONTENT

Use the**Project Options**dialog to specify project-specific options.Thedialog includes option groups, each designated for specific features. You can find the evaluation-related project options under the **Evaluation** option group.

[IMAGE alt='' src='']

###### The Project Options dialog

##### Modifying evaluation project options

To modify evaluation-related project options

1. In the main menu, select Options > Project .
2. In the Project Options dialog, select the Evaluation option group.
3. In the option list, click the value cell for the option you want to change, then enter or select the new value.
4. Click OK to close the dialog.

##### Evaluation project options

The following table describes evaluation-related project options.

| Option name | Description |
| --- | --- |
| Display Verification Results As | Select the method to visualize requirements and constraint verification results in views. Select Paint Headers to color shape headers. Select Display Icons to add icons to shape headers. |
| Propagate Deep Nested Failures | Set to true to indicate deep nested requirement and constraint failures on part shapes. Set to false if you want shapes to be highlighted only when they directly fail a requirement or constraint. |
| Autorecalculate Bound Values | Set to true to automatically recalculate bound values when an initial value is changed. Set to false to initiate recalculation by clicking Refresh or Evaluate. |
| External Script Engine Libraries | Add the external library files that will be loaded into the script engine. To add a file, select the option value cell, click , click the Add button in the open dialog, and select the file you want to add. |
| Maximum recursion Depth | Specify the maximum number of times a feature can be re-evaluated recursively before the recursion error is triggered. |

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><span style="color:var(--ds-text,#172b4d);">Use the<span> </span></span><strong style="text-align: left;">Project Options</strong><span style="color:var(--ds-text,#172b4d);"><span> </span>dialog to s</span><span style="color:var(--ds-text,#172b4d);">pecify project-specific options.<span> </span></span><span style="color:var(--ds-text,#172b4d);">The </span><span style="color:var(--ds-text,#172b4d);">dialog includes option groups, each designated for specific features. You can find the evaluation-related project options under the <strong>Evaluation</strong> option group.</span></p><p style="text-align: center;"><span style="color:var(--ds-text,#172b4d);"><ac:image><ri:attachment ri:filename="project_options.png" /></ac:image></span></p><h6 style="text-align: center;"><span style="color:var(--ds-text,#172b4d);">The Project Options dialog</span></h6><h3><span style="color:var(--ds-text,#172b4d);">Modifying evaluation project options</span></h3><p><span style="color:var(--ds-text,#172b4d);">To modify evaluation-related project options</span></p><hr /><ol><li data-uuid="8f7725cd-259f-471f-b215-3945d56c7552">In the main menu, select <strong>Options</strong> &gt; <strong>Project</strong>.</li><li data-uuid="d03ea0bd-17a0-46c5-a2e5-6a4d580f6622">In the <strong>Project Options</strong> dialog, select the <strong>Evaluation</strong> option group.</li><li data-uuid="10b81531-bda4-4578-bac9-4870008c5cd6">In the option list, click the value cell for the option you want to change, then enter or select the new value.</li><li data-uuid="bd131ad3-bc72-481a-bedd-323cdbbaf8c9">Click <strong>OK</strong> to close the dialog.</li></ol><h3>Evaluation project options</h3><p>The following table describes evaluation-related project options.</p><table class="wrapped"><colgroup><col /><col /></colgroup><tbody><tr><th scope="col">Option name</th><th scope="col">Description</th></tr><tr><td><strong>Display Verification Results As</strong></td><td>Select the method to visualize requirements and constraint verification results in views. Select <strong>Paint Headers</strong> to color shape headers. Select <strong>Display Icons</strong> to add icons to shape headers. </td></tr><tr><td><strong>Propagate Deep Nested Failures</strong></td><td>Set to <em>true</em> to indicate deep nested requirement and constraint failures on part shapes. Set to <em>false</em> if you want shapes to be highlighted only when they directly fail a requirement or constraint.</td></tr><tr><td><strong>Autorecalculate Bound Values</strong></td><td>Set to <em>true</em> to automatically recalculate bound values when an initial value is changed. Set to <em>false</em> to initiate recalculation by clicking <strong>Refresh</strong> or <strong>Evaluate</strong>.</td></tr><tr><td><strong>External Script Engine Libraries</strong></td><td><div class="content-wrapper"><p>Add the external library files that will be loaded into the script engine. To add a file, select the option value cell, click <ac:image><ri:attachment ri:filename="edit_button.png" /></ac:image>, click the <strong>Add</strong> button in the open dialog, and select the file you want to add.</p></div></td></tr><tr><td><strong>Maximum recursion Depth</strong></td><td>Specify the maximum number of times a feature can be re-evaluated recursively before the recursion error is triggered.</td></tr></tbody></table>
````

<!--NOMAGIC_PAGE id=304014880 space=SYSML2EP version=2 -->
## PAGE 00015: (2026x Refresh1) Samples and libraries

- page_id: `304014880`
- space_key: `SYSML2EP`
- source_url: https://docs.nomagic.com/spaces/SYSML2EP/pages/304014880/2026x+Refresh1+Samples+and+libraries
- version_number: 2
- version_date: `2026-05-06T10:25:09.082+02:00`
- ancestors: Versions of SysML v2 Evaluation Plugin Documentation > (2026x Refresh1) SysML v2 Evaluation Plugin Documentation
- labels: []

### NORMALIZED CONTENT

##### Samples

To get started, review the SysML v2 project samples provided with the installation, found at:

- <modeling tool installation directory>\samples\SysML v2\Evaluation

##### Libraries

Each SysML v2 project is automatically loaded with used projects:

- Standard Libraries. It contains standard SysML v2 libraries.
- 3DS SysML Customization. It contains concepts designed for view creation and symbol styles customization.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<h3>Samples</h3><p>To get started, review the SysML v2 project samples provided with the installation, found at:</p><ul><li><em style="text-align: left;">&lt;modeling tool installation directory&gt;\samples\SysML v2\Evaluation</em><em style="text-align: left;"><br /></em></li></ul><h3>Libraries</h3><p>Each SysML v2 project is automatically loaded with used projects:</p><ul><li><em>Standard Libraries.</em> It contains standard SysML v2 libraries.</li><li><em>3DS SysML Customization. </em>It contains concepts designed for view creation and symbol styles customization.<em><br /></em></li></ul>
````

<!--NOMAGIC_PAGE id=304014947 space=SYSML2EP version=1 -->
## PAGE 00016: (2026x Refresh1) Server-side evaluation

- page_id: `304014947`
- space_key: `SYSML2EP`
- source_url: https://docs.nomagic.com/spaces/SYSML2EP/pages/304014947/2026x+Refresh1+Server-side+evaluation
- version_number: 1
- version_date: `2026-04-29T17:11:15.648+02:00`
- ancestors: Versions of SysML v2 Evaluation Plugin Documentation > (2026x Refresh1) SysML v2 Evaluation Plugin Documentation > (2026x Refresh1) User guide
- labels: []

### NORMALIZED CONTENT

If you work with Teamwork Cloud projects, you can evaluate them on the server byusing the REST API or thePython client (pyEval.zip).

Server-side evaluation is available only with the Teamwork Cloud Enterprise license.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>If you work with Teamwork Cloud projects, you can evaluate them on the server by<span style="letter-spacing: 0.0px;"> using the REST API or the</span><span style="letter-spacing: 0.0px;"> Python client (<ac:inline-comment-marker ac:ref="24822121-cd71-4013-9b75-cf4d77db78fe"><span style="color:var(--ds-text,#172b4d);">pyEval.zip</span></ac:inline-comment-marker>).<br /></span></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="ba65ec8a-8cd1-4d8d-a0d4-0a1b397639ec"><ac:rich-text-body><p>Server-side evaluation is available only with the Teamwork Cloud Enterprise license.</p></ac:rich-text-body></ac:structured-macro><p><span style="color:var(--ds-text,#172b4d);"><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="8a64d399-3fd0-4bfd-9138-4a6175057396" /></span></p>
````

<!--NOMAGIC_PAGE id=304014876 space=SYSML2EP version=2 -->
## PAGE 00017: (2026x Refresh1) SysML v2 Evaluation Plugin Documentation

- page_id: `304014876`
- space_key: `SYSML2EP`
- source_url: https://docs.nomagic.com/spaces/SYSML2EP/pages/304014876/2026x+Refresh1+SysML+v2+Evaluation+Plugin+Documentation
- version_number: 2
- version_date: `2026-06-16T09:20:54.745+02:00`
- ancestors: Versions of SysML v2 Evaluation Plugin Documentation
- labels: []

### NORMALIZED CONTENT

lightgrey

This guide provides documentation for the SysML v2 Evaluation Plugin.

SysML v2 is a next-generation systems modeling language. Compared to SysML v1, SysML v2 aims to offer improved precision, expressiveness, and usability.

To fully take advantage of SysML v2, two primary plugins are available for you:

- The SysML v2 Plugin provides core SysML v2 features and includes the SysML v2 Textual Editor, enabling you to model using both textual and graphical notations.
- The SysML v2 Evaluation Plugin allows you to conduct static evaluations of SysML v2 models.

For more information, please see the [CONFLUENCE_PAGE title='(2026x Refresh1) Prerequisites' space=''] page.

The following topics explain how to install and use the SysML v2 Evaluation Plugin:

2

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="10aa203c-7173-4219-ab58-f6619359c634"><ac:parameter ac:name="bgColor">lightgrey</ac:parameter><ac:rich-text-body><p><span style="color:var(--ds-text,#172b4d);">This guide provides documentation for the SysML v2 Evaluation Plugin.</span></p></ac:rich-text-body></ac:structured-macro><p>SysML v2 is a next-generation systems modeling language. Compared to SysML v1, SysML v2 aims to offer improved precision, expressiveness, and usability.</p><p>To fully take advantage of SysML v2, two primary plugins are available for you:</p><ul><li><a href="https://docs.nomagic.com/SYSML2P/?contextKey=sysml-v2-plugin-documentation&amp;version=2026x%20Refresh1">The SysML v2 Plugin</a> provides core SysML v2 features and includes the SysML v2 Textual Editor, enabling you to model using both textual and graphical notations.</li><li>The SysML v2 Evaluation Plugin allows you to conduct static evaluations of SysML v2 models.</li></ul><p>For more information, please see the <ac:link><ri:page ri:content-title="(2026x Refresh1) Prerequisites" /></ac:link> page.</p><p>The following topics explain how to install and use the SysML v2 Evaluation Plugin:</p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="9a83306a-dc0b-4b64-8374-382275e8d7c5"><ac:parameter ac:name="depth">2</ac:parameter></ac:structured-macro></p><p><br /></p>
````

<!--NOMAGIC_PAGE id=304014882 space=SYSML2EP version=2 -->
## PAGE 00018: (2026x Refresh1) User guide

- page_id: `304014882`
- space_key: `SYSML2EP`
- source_url: https://docs.nomagic.com/spaces/SYSML2EP/pages/304014882/2026x+Refresh1+User+guide
- version_number: 2
- version_date: `2026-04-29T17:12:21.911+02:00`
- ancestors: Versions of SysML v2 Evaluation Plugin Documentation > (2026x Refresh1) SysML v2 Evaluation Plugin Documentation
- labels: []

### NORMALIZED CONTENT

The SysML v2 Evaluation Plugin user guide explains how to conduct static evaluations of SysML v2 models.

For information about generic SysML v2 modeling features, including using the textual notation, see the [SysML v2 Plugin documentation](https://docs.nomagic.com/SYSML2P/?contextKey=sysml-v2-plugin-documentation&version=2026x Refresh1).

To learn more, see the following topics:

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>The SysML v2 Evaluation Plugin user guide explains how to conduct static evaluations of SysML v2 models.</p><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="f0f8e034-bdef-4bad-9db3-36961de8057f"><ac:rich-text-body><p>For information about generic SysML v2 modeling features, including using the textual notation, see the <a href="https://docs.nomagic.com/SYSML2P/?contextKey=sysml-v2-plugin-documentation&amp;version=2026x Refresh1">SysML v2 Plugin documentation</a>.</p></ac:rich-text-body></ac:structured-macro><p> To learn more, see the following topics:</p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="1d052ab0-6a12-44f2-a374-967d5273613b" /></p>
````

<!--NOMAGIC_PAGE id=304014968 space=SYSML2EP version=1 -->
## PAGE 00019: (2026x Refresh1) Using interactive HTML table

- page_id: `304014968`
- space_key: `SYSML2EP`
- source_url: https://docs.nomagic.com/spaces/SYSML2EP/pages/304014968/2026x+Refresh1+Using+interactive+HTML+table
- version_number: 1
- version_date: `2026-04-29T17:11:16.201+02:00`
- ancestors: Versions of SysML v2 Evaluation Plugin Documentation > (2026x Refresh1) SysML v2 Evaluation Plugin Documentation > (2026x Refresh1) User guide > (2026x Refresh1) Server-side evaluation
- labels: []

### NORMALIZED CONTENT

You can use [CONFLUENCE_PAGE title='(2026x Refresh1) Evaluation using REST API' space=''] or [CONFLUENCE_PAGE title='(2026x Refresh1) Evaluation using Jupyter Notebook' space=''] to open and modify an interactive HTML table that dynamically retrieves data based on the specified context, parameters, and/or expressions.

[IMAGE alt='' src='']

###### An interactive HTML table

##### Editing values

In an HTML table, you can edit initial values, as described below.

- Only initial values can be edited.
- Non-editable values are shown in italic font for easier identification.

To edit initial values

1. Click the Value cell you want to edit.
2. Change the value.
3. Click anywhere on the table page to save the value.

##### Adding new rows

To add a new table row

1. In the top right corner of the table page, click [ATTACHMENT filename='add_row.png'] to add a new row at the bottom of the table.
2. Click the Name and Value cells of the new row and enter the desired property name and value.

##### Reordering rows

To change the position of a table row

1. Hover the mouse pointer over a table row to see available action icons.
2. Click and hold [ATTACHMENT filename='drag_to_reorder.png'] .
3. Drag and drop the row to a new position. [ATTACHMENT filename='reordering_rows.png']

##### Deleting rows

To delete a table row

1. Hover the mouse pointer over a table row to see available action icons.
2. Click [ATTACHMENT filename='delete_row.png'] to delete the row.

##### Exporting data

You can export HTML table data to the PNG, CSV, and JSON formats.

To export table data

- In the top right corner of the table page, click [ATTACHMENT filename='export_table.png'] and select the format you want to export to.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><span style="color:var(--ds-text,#172b4d);">You can use <ac:link><ri:page ri:content-title="(2026x Refresh1) Evaluation using REST API" /><ac:plain-text-link-body><![CDATA[REST API]]></ac:plain-text-link-body></ac:link> or <ac:link><ri:page ri:content-title="(2026x Refresh1) Evaluation using Jupyter Notebook" /><ac:plain-text-link-body><![CDATA[Jupyter Notebook]]></ac:plain-text-link-body></ac:link> to open and modify an interactive HTML table that dynamically retrieves data based on the specified context, parameters, and/or expressions.</span></p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="interactive_html_table.png"><ri:page ri:content-title="(2026x Refresh1) Using interactive HTML table" /></ri:attachment></ac:image></p><h6 style="text-align: center;">An interactive HTML table</h6><h3>Editing values</h3><p>In an HTML table, you can edit initial values, as described below.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="76aefc83-3d0f-4ae0-bbe6-162cecceff80"><ac:rich-text-body><ul><li data-uuid="ca56cbae-a2c6-49a4-a951-0ef751c67482">Only initial values can be edited.</li><li data-uuid="5b1e874e-9fbf-4ef8-9f9c-0e3a0c93c4d0">Non-editable values are shown in italic font for easier identification.</li></ul></ac:rich-text-body></ac:structured-macro><p>To edit initial values</p><hr /><ol><li data-uuid="2ea41a37-2bfb-4b11-b578-c67f0f88e8a4">Click the <strong>Value</strong> cell you want to edit.</li><li data-uuid="65d38620-9b60-402c-b8d6-420fff571066">Change the value.</li><li data-uuid="2cd1e1c1-8b20-4169-8de7-a9f28c64950b">Click anywhere on the table page to save the value.</li></ol><h3>Adding new rows</h3><p>To add a new table row</p><hr /><ol><li data-uuid="c936246a-3d08-41d4-b2f6-7194e2826d9c">In the top right corner of the table page, click <ac:image><ri:attachment ri:filename="add_row.png"><ri:page ri:content-title="(2026x Refresh1) Using interactive HTML table" /></ri:attachment></ac:image> to add a new row at the bottom of the table.</li><li data-uuid="559cef5d-7f41-4bfa-9664-0be5ff3f0668">Click the <strong>Name</strong> and <strong>Value</strong> cells of the new row and enter the desired property name and value.</li></ol><h3>Reordering rows</h3><p>To change the position of a table row</p><hr /><ol><li data-uuid="5468d510-837e-4c9c-bfb8-23c6491ee34f">Hover the mouse pointer over a table row to see available action icons.</li><li data-uuid="69c81157-5a1c-4607-ad0f-c45903a9a714">Click and hold <ac:image><ri:attachment ri:filename="drag_to_reorder.png"><ri:page ri:content-title="(2026x Refresh1) Using interactive HTML table" /></ri:attachment></ac:image>.</li><li data-uuid="2a26e1e2-a6ed-427d-8a5e-906fa4efce57">Drag and drop the row to a new position.<br /><ac:image><ri:attachment ri:filename="reordering_rows.png"><ri:page ri:content-title="(2026x Refresh1) Using interactive HTML table" /></ri:attachment></ac:image></li></ol><h3>Deleting rows</h3><p>To delete a table row</p><hr /><ol><li data-uuid="69049473-a60c-4b0d-b5e2-2c225ae4c45e">Hover the mouse pointer over a table row to see available action icons.</li><li data-uuid="23f04ada-7943-4654-ba09-12119b274af1">Click <ac:image ac:thumbnail="true" ac:height="14"><ri:attachment ri:filename="delete_row.png"><ri:page ri:content-title="(2026x Refresh1) Using interactive HTML table" /></ri:attachment></ac:image> to delete the row.</li></ol><h3>Exporting data</h3><p>You can export HTML table data to the PNG, CSV, and JSON formats.</p><p>To export table data</p><hr /><ul><li data-uuid="728ffb95-3107-4839-b29c-93d5577c60b0">In the top right corner of the table page, click <ac:image ac:thumbnail="true" ac:height="22"><ri:attachment ri:filename="export_table.png"><ri:page ri:content-title="(2026x Refresh1) Using interactive HTML table" /></ri:attachment></ac:image> and select the format you want to export to.</li></ul>
````

<!--NOMAGIC_PAGE id=314180455 space=SYSML2EP version=6 -->
## PAGE 00020: (2026x Refresh1) Using textual representation

- page_id: `314180455`
- space_key: `SYSML2EP`
- source_url: https://docs.nomagic.com/spaces/SYSML2EP/pages/314180455/2026x+Refresh1+Using+textual+representation
- version_number: 6
- version_date: `2026-06-18T13:49:56.391+02:00`
- ancestors: Versions of SysML v2 Evaluation Plugin Documentation > (2026x Refresh1) SysML v2 Evaluation Plugin Documentation > (2026x Refresh1) User guide
- labels: []

### NORMALIZED CONTENT

A textual representation element provides a representation of a model element in a specified language. A textual representation identifies the language of the representation and contains the corresponding text body. The language may be a natural language or a machine-readable language.

Textual representations can be used to associate model elements with language-specific content such as scripts, expressions, analysis artifacts, or other textual definitions.

Supported languages include:

- JavaScript
- Groovy
- Beanshell
- Python (via Jython)
- MATLAB

#### NOTE: Using MATLAB

Using MATLAB

To evaluate scripts defined in the MATLAB syntax:

- [CONFLUENCE_PAGE title='(2026x Refresh1) Integration with MATLAB' space=''] .
- The language must be specified as "MATLAB" (case sensitive).

When a textual representation is used for script execution, script inputs and outputs are typically primitive values (Boolean, Integer, Real, and String). Evaluated structured model elements, such as parts, can also be provided as inputs. You can access their feature values by using the get method described below. In Groovy scripts, nested feature values can also be accessed using dot notation.

#### TIP: Printing output from scripts

Printing output from scripts

Evaluated scripts in all supported languages can print messages to the**SysML v2 Model Evaluation**console using the print method. Each call to print outputs a separate line in the console.

calcdefListCalc{ 
/* Calc prints to console and returns null output */ 
innumericalList[*] :Real; 
return:Real; 
repmyScriptlanguage"Python"/* print(numericalList[1]) */

##### Accessing structured model elements in scripts

In addition to primitive values, a script can receive an evaluated structured model element (for example, a part) as input. To access feature values from the structured element, use the get method:

#### PANEL: Example

Example

vehicle.get("grossMass")

The method returns the evaluated value of the specified feature. For example, if *vehicle* is a part and *grossMass* evaluates to a real value, the expression in the above example returns the numerical value of *grossMass*.

#### NOTE: Using Groovy

Using Groovy

When using Groovy, nested feature values can be accessed via dot notation in addition to the get method, for example:

calcdefArea{ 
inmyInput:> Vehicle::pad; 
return:Real;repmyScriptlanguage"Groovy" 
/* myInput.centerLength * myInput.width */

##### Textual representations in calculations

When specifying the return value of a calculation, you can use a textual representation to evaluate a script written in a supported scripting language.

The following example uses a Beanshell script to calculate an area from the supplied inputs:

#### PANEL: Example

Example

calcdefArea15{ 
inlength:Real; 
inwidth:Real; 
returnresult:Real; 
language"beanshell"/* result=length * width */

}

When the calculation is evaluated, the script receives the calculation inputs as variables and assigns the computed value to the return parameter.

##### Textual representations in actions

When defining an action, you can use a textual representation to implement the action's behavior using an external scripting language. Action parameters are exposed to the script and can be read or updated according to their direction (in, out, or inout).

#### PANEL: Example

Example

actiondefcounter{ 
inoutcount:Real:=0; 
language"groovy"/* count=count+1 */} 
} 
attributestartCount: Integer = counter().count//The result will be 1 because there is no input 
attributecontinueCount: Integer = counter(startCount).count//The result will be 2. Input overrides the initial value set in the parameter.

###### Invoking external tools via ToolExecution

Actions support "ToolExecution", which allows SysML v2 features to be mapped to variables used by MATLAB scripts. This is particularly useful when the variable names used in the model differ from those expected by the external script.

The following example executes a MATLAB script and maps model features to MATLAB variables using "ToolVariable"annotations:

#### PANEL: Example

Example

actioncomputeStoppingDistance { 
privateimportAnalysisTooling::*; 
@ToolExecution { 
:>> toolName ="MATLAB"; 
:>> uri ="run('C:/custom/path/to/StoppingAnalysisExec.m')"; 
} 
inmass : Real = vehicle.grossMass{@ToolVariable { name ="m"; }}; 
inspeed : Real = vehicle.speed{@ToolVariable { name ="v0"; }}; 
outDistance : Real = vehicle.stoppingDistance {@ToolVariable { name ="stoppingDistance"; }}; 
outkineticEnergy : Real = vehicle.kineticEnergy {@ToolVariable { name ="e"; }};

##### Textual representations in constraints

You can use a textual representation to define constraint logic in both requirements and standalone constraints using a supported scripting language. When a simple constraint (assert constraint) is evaluated, all attributes of the constraint’s owner are available in the script as variables. You can use them directly without qualification. You can also access nested structures using the get method (and dot notation in Groovy).

###### Standalone constraints

In a standalone constraint, attributes defined within the constraint are directly available in the script.

#### PANEL: Example

Example

assertconstraint{ 
attributemaxValue:Integer=5; 
attributecurrentValue:Integer=3; 
language"Groovy"/* currentValue < maxValue */ 
}

###### Constraints in parts

When a constraint is defined directly under a part, all attributes of the part are available in the script.

#### PANEL: Example

Example

partvehicle{ 
attributemaxSpeed:Integer=100; 
attributecurrentSpeed:Integer=100;satisfyspeedReqbythis; 
 
assertnotconstraint{ 
language"groovy"/* currentSpeed == maxSpeed */ 
} 
}

###### Constraints in requirements

When a constraint is used inside a requirement, the requirement subject is made available to the script engine as the root context for evaluation. This means that the subject and its structure are directly accessible in the script engine.

#### PANEL: Example

Example

requirementspeedReq{ 
subjectvehiclev :>vehicle;requireconstraint{ 
language"groovy"/* v.currentSpeed < vehicle.maxSpeed */ 
} 
}

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="isSelectedEnd"><span>A textual representation element provides a representation of a model element in a specified language. A textual representation identifies the language of the representation and contains the corresponding text body. The language may be a natural language or a machine-readable language.</span></p><p class="isSelectedEnd"><span>Textual representations can be used to associate model elements with language-specific content such as scripts, expressions, analysis artifacts, or other textual definitions.</span></p><p class="isSelectedEnd"><span>Supported languages include:</span></p><ul><li data-uuid="a796e4b9-ceec-4ce0-a91f-bda17b745683"><span>JavaScript</span></li><li data-uuid="6e019d51-0808-4ae5-aeb2-8aa7488f1e98"><span>Groovy</span></li><li data-uuid="8640f526-b03e-4585-87e2-ef16a45c1259"><span>Beanshell</span></li><li data-uuid="0ec18582-6a89-45b0-b189-566f033296bf"><span>Python (via Jython)</span></li><li data-uuid="20af4792-d056-4a64-8cb8-c89b7dbf8351"><span>MATLAB</span></li></ul><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="7112b935-00f1-4054-b9ef-71f2449b1345"><ac:parameter ac:name="title">Using MATLAB</ac:parameter><ac:rich-text-body><p>To evaluate scripts defined in the MATLAB syntax:</p><ul><li data-uuid="09a363ca-55e4-4af8-8339-375cafead37c"><ac:link><ri:page ri:content-title="(2026x Refresh1) Integration with MATLAB" /><ac:plain-text-link-body><![CDATA[MATLAB must be integrated with your modeling tool]]></ac:plain-text-link-body></ac:link>.</li><li data-uuid="43f4a7e1-860d-4895-89cd-6ffd463d7369">The language must be specified as &quot;MATLAB&quot; (case sensitive).</li></ul></ac:rich-text-body></ac:structured-macro><p class="isSelectedEnd">When a textual representation is used for script execution, script inputs and outputs are typically primitive values (Boolean, Integer, Real, and String). Evaluated structured model elements, such as parts, can also be provided as inputs. You can access their feature values by using the get method described below. In Groovy scripts, nested feature values can also be accessed using dot notation.</p><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="6908ea7c-96c6-4375-8d00-9ab56f31c552"><ac:parameter ac:name="title">Printing output from scripts</ac:parameter><ac:rich-text-body><p>Evaluated scripts in all supported languages can print messages to <span style="color:var(--ds-text,#172b4d);">the<span> </span></span><strong style="text-align: left;">SysML v2 Model Evaluation</strong><span style="color:var(--ds-text,#172b4d);"><span> </span>console</span> using the print method. Each call to print outputs a separate line in the console.</p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="a0ce7936-639a-43c2-8b62-35dc10cd8ad9"><ac:rich-text-body><p><span style="color:var(--ds-text-accent-blue,#0055cc);">calc</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">def</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-teal,#206a83);">ListCalc</span><span style="color:var(--ds-text,#000000);"> {</span><br /><span style="color:var(--ds-text,#000000);">    </span><span style="color:var(--ds-text-accent-green-bolder,#164b35);">/* <span style="color:var(--ds-text-accent-lime,#4c6b1f);">Calc prints to console and returns null output</span>  */</span><br /><span style="color:var(--ds-text,#000000);">        </span><span style="color:var(--ds-text-accent-blue,#0055cc);">in</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">numericalList</span><span style="color:var(--ds-text,#000000);"> [*] : </span><span style="color:var(--ds-text-accent-teal,#206a83);">Real</span><span style="color:var(--ds-text,#000000);">;</span><br /><span style="color:var(--ds-text,#000000);">        </span><span style="color:var(--ds-text-accent-blue,#0055cc);">return</span><span style="color:var(--ds-text,#000000);"> : </span><span style="color:var(--ds-text-accent-teal,#206a83);">Real</span><span style="color:var(--ds-text,#000000);">;</span><br /><span style="color:var(--ds-text,#000000);">        </span><span style="color:var(--ds-text-accent-blue,#0055cc);">rep</span><span style="color:var(--ds-text,#000000);"> myScript </span><span style="color:var(--ds-text-accent-blue,#0055cc);">language</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-red,#ae2e24);">&quot;Python&quot;</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-green-bolder,#164b35);">/* print(numericalList[1]) */</span></p></ac:rich-text-body></ac:structured-macro><p><br /></p></ac:rich-text-body></ac:structured-macro><h3>Accessing structured model elements in scripts</h3><p>In addition to primitive values, a script can receive an evaluated structured model element (for example, a part) as input. To access feature values from the structured element, use the get method:</p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="3a7d7d13-8a40-40ef-a3c8-b6519f171ca6"><ac:parameter ac:name="title">Example</ac:parameter><ac:rich-text-body>vehicle.get(&quot;grossMass&quot;)</ac:rich-text-body></ac:structured-macro><p>The method returns the evaluated value of the specified feature. For example, if <em>vehicle</em> is a part and <em>grossMass</em> evaluates to a real value, the expression in the above example returns the numerical value of <em>grossMass</em>.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="08c847c4-2b82-4593-b4ac-261043efde90"><ac:parameter ac:name="title">Using Groovy</ac:parameter><ac:rich-text-body><p>When using Groovy, nested feature values can be accessed via dot notation in addition to the get method, for example:</p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="73760d45-bf16-4944-8ea6-b66a139128db"><ac:rich-text-body><p><span style="color:var(--ds-text-accent-blue,#0055cc);">calc</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">def</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-teal,#206a83);">Area</span><span style="color:var(--ds-text,#000000);"> {</span><br /><span style="color:var(--ds-text,#000000);">        </span><span style="color:var(--ds-text-accent-blue,#0055cc);">in</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">myInput</span><span style="color:var(--ds-text,#000000);"> :&gt; Vehicle::pad;</span><br /><span style="color:var(--ds-text,#000000);">        </span><span style="color:var(--ds-text-accent-blue,#0055cc);">return</span><span style="color:var(--ds-text,#000000);"> : </span><span style="color:var(--ds-text-accent-teal,#206a83);">Real</span><span style="color:var(--ds-text,#000000);">;<br /><br /></span><span style="color:var(--ds-text,#000000);">        </span><span style="color:var(--ds-text-accent-blue,#0055cc);">rep</span><span style="color:var(--ds-text,#000000);"> myScript </span><span style="color:var(--ds-text-accent-blue,#0055cc);">language</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-red,#ae2e24);">&quot;Groovy&quot;</span><br /><span style="color:var(--ds-text,#000000);">        </span><span style="color:var(--ds-text-accent-green-bolder,#164b35);">/* myInput.centerLength * myInput.width */</span></p></ac:rich-text-body></ac:structured-macro><p><br /></p></ac:rich-text-body></ac:structured-macro><h3 class="cm-content q9tKkq_readonly m-0"><span style="color:var(--ds-text,#172b4d);">Textual representations in calculations</span></h3><p class="isSelectedEnd"><span>When specifying the return value of a calculation, you can use a textual representation to evaluate a script written in a supported scripting language.</span></p><p><span>The following example uses a Beanshell script to calculate an area from the supplied inputs:</span></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="c0d6ec98-2f53-4b20-8d8e-4d37f62150b8"><ac:parameter ac:name="title">Example</ac:parameter><ac:rich-text-body><p><span style="color:var(--ds-text-accent-blue,#0055cc);">calc</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">def</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-teal,#206a83);">Area15</span><span style="color:var(--ds-text,#000000);"> {</span><br /><span style="color:var(--ds-text,#000000);">        </span><span style="color:var(--ds-text-accent-blue,#0055cc);">in</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">length</span><span style="color:var(--ds-text,#000000);"> : </span><span style="color:var(--ds-text-accent-teal,#206a83);">Real</span><span style="color:var(--ds-text,#000000);">;</span><br /><span style="color:var(--ds-text,#000000);">        </span><span style="color:var(--ds-text-accent-blue,#0055cc);">in</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">width</span><span style="color:var(--ds-text,#000000);"> : </span><span style="color:var(--ds-text-accent-teal,#206a83);">Real</span><span style="color:var(--ds-text,#000000);">;</span><br /><span style="color:var(--ds-text,#000000);">        </span><span style="color:var(--ds-text-accent-blue,#0055cc);">return</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">result</span><span style="color:var(--ds-text,#000000);"> : </span><span style="color:var(--ds-text-accent-teal,#206a83);">Real</span><span style="color:var(--ds-text,#000000);">;</span><br /><span style="color:var(--ds-text,#000000);">        </span><span style="color:var(--ds-text-accent-blue,#0055cc);">language</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-red,#ae2e24);">&quot;beanshell&quot;</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-green-bolder,#164b35);">/* result=length * width */</span></p><p><span style="color:var(--ds-text,#000000);">}</span></p></ac:rich-text-body></ac:structured-macro><p>When the calculation is evaluated, the script receives the calculation inputs as variables and assigns the computed value to the return parameter.</p><h3><span style="color:var(--ds-text,#172b4d);">Textual representations in actions</span></h3><p><span>When defining an action, you can use a textual representation to implement the action's behavior using an external scripting language. Action parameters are exposed to the script and can be read or updated according to their direction (</span>in, out, or inout<span>).</span></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="24a4616b-d53d-4636-adec-93550d92b4ee"><ac:parameter ac:name="title">Example</ac:parameter><ac:rich-text-body><p><span style="color:var(--ds-text-accent-blue,#0055cc);">action</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">def</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-teal,#206a83);">counter</span><span style="color:var(--ds-text,#000000);"> {</span><br /><span style="color:var(--ds-text,#000000);">    </span><span style="color:var(--ds-background-accent-red-bolder,#c9372c);"> </span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-background-accent-red-bolder,#c9372c);"> </span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-background-accent-red-bolder,#c9372c);"> </span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-background-accent-red-bolder,#c9372c);">  </span><span style="color:var(--ds-text-accent-blue,#0055cc);">inout</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">count</span><span style="color:var(--ds-text,#000000);"> : </span><span style="color:var(--ds-text-accent-teal,#206a83);">Real</span><span style="color:var(--ds-text,#000000);"> := </span><span style="color:var(--ds-background-accent-green-bolder,#1f845a);">0</span><span style="color:var(--ds-text,#000000);">;</span><br /><span style="color:var(--ds-text,#000000);">            </span><span style="color:var(--ds-text-accent-blue,#0055cc);">language</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-red,#ae2e24);">&quot;groovy&quot;</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-green-bolder,#164b35);">/* count=count+1 */</span><span style="color:var(--ds-text,#000000);"> } </span><br /><span style="color:var(--ds-text,#000000);">        }</span><br /><span style="color:var(--ds-text-accent-blue,#0055cc);">attribute</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">startCount</span><span style="color:var(--ds-text,#000000);"> : Integer = counter().count </span><span style="color:var(--ds-text-accent-green-bolder,#164b35);">//The result will be 1 because there is no input </span><br /><span style="color:var(--ds-text-accent-blue,#0055cc);">attribute</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">continueCount</span><span style="color:var(--ds-text,#000000);"> : Integer = counter(</span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">startCount</span><span style="color:var(--ds-text,#000000);">).count </span><span style="color:var(--ds-text-accent-green-bolder,#164b35);">//The result will be 2. Input overrides the initial value set in the parameter.</span></p></ac:rich-text-body></ac:structured-macro><h4 class="isSelectedEnd"><span>Invoking external tools via ToolExecution</span></h4><p class="isSelectedEnd"><span>Actions support &quot;</span>ToolExecution&quot;<span>, which allows SysML v2 features to be mapped to variables used by MATLAB scripts. This is particularly useful when the variable names used in the model differ from those expected by the external script.</span></p><p><span>The following example executes a MATLAB script and maps model features to MATLAB variables using &quot;</span>ToolVariable&quot;<span> annotations:</span></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="71f0bc6d-8deb-4cb2-9366-e6f7da3c2ea4"><ac:parameter ac:name="title">Example</ac:parameter><ac:rich-text-body><p><span style="color:var(--ds-text-accent-blue,#0055cc);">action</span><span style="color:var(--ds-text,#000000);"> computeStoppingDistance {</span><br /><span style="color:var(--ds-text,#000000);">            </span><span style="color:var(--ds-text-accent-blue,#0055cc);">private</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">import</span><span style="color:var(--ds-text,#000000);"> AnalysisTooling::*;</span><br /><span style="color:var(--ds-text,#000000);">            @ToolExecution {</span><br /><span style="color:var(--ds-text,#000000);">                :&gt;&gt; toolName = </span><span style="color:var(--ds-text-accent-red,#ae2e24);">&quot;MATLAB&quot;</span><span style="color:var(--ds-text,#000000);">;</span><br /><span style="color:var(--ds-text,#000000);">                :&gt;&gt; uri = </span><span style="color:var(--ds-text-accent-red,#ae2e24);">&quot;run('C:/custom/path/to/StoppingAnalysisExec.m')&quot;</span><span style="color:var(--ds-text,#000000);">;</span><br /><span style="color:var(--ds-text,#000000);">            }</span><br /><span style="color:var(--ds-text,#000000);">            </span><span style="color:var(--ds-text-accent-blue,#0055cc);">in</span><span style="color:var(--ds-text,#000000);"> mass : Real = vehicle.grossMass </span><span style="color:var(--ds-text,#000000);">{@ToolVariable { name = </span><span style="color:var(--ds-text-accent-red,#ae2e24);">&quot;m&quot;</span><span style="color:var(--ds-text,#000000);">; }};</span><br /><span style="color:var(--ds-text,#000000);">            </span><span style="color:var(--ds-text-accent-blue,#0055cc);">in</span><span style="color:var(--ds-text,#000000);"> speed : Real = vehicle.speed</span><span style="color:var(--ds-text,#000000);"> {@ToolVariable { name = </span><span style="color:var(--ds-text-accent-red,#ae2e24);">&quot;v0&quot;</span><span style="color:var(--ds-text,#000000);">; }};</span><br /><span style="color:var(--ds-text,#000000);">            </span><span style="color:var(--ds-text-accent-blue,#0055cc);">out</span><span style="color:var(--ds-text,#000000);"> Distance : Real = vehicle.stoppingDistance {@ToolVariable { name = </span><span style="color:var(--ds-text-accent-red,#ae2e24);">&quot;stoppingDistance&quot;</span><span style="color:var(--ds-text,#000000);">; }};</span><br /><span style="color:var(--ds-text,#000000);">            </span><span style="color:var(--ds-text-accent-blue,#0055cc);">out</span><span style="color:var(--ds-text,#000000);"> kineticEnergy : Real = vehicle.kineticEnergy {@ToolVariable { name = </span><span style="color:var(--ds-text-accent-red,#ae2e24);">&quot;e&quot;</span><span style="color:var(--ds-text,#000000);">; }};</span></p></ac:rich-text-body></ac:structured-macro><h3>Textual representations in constraints</h3><p>You can use a textual representation to define constraint logic in both requirements and standalone constraints using a supported scripting language. When a simple constraint (assert constraint) is evaluated, all attributes of the constraint’s owner are available in the script as variables. You can use them directly without qualification. You can also access nested structures using the get method (and dot notation in Groovy).</p><h4>Standalone constraints</h4><p>In a standalone constraint, attributes defined within the constraint are directly available in the script.</p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="dd10a11e-b75e-4664-914d-000d06230a76"><ac:parameter ac:name="title">Example</ac:parameter><ac:rich-text-body><p><span style="color:var(--ds-text-accent-blue,#0055cc);">assert</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">constraint</span><span style="color:var(--ds-text,#000000);"> {</span><br /><span style="color:var(--ds-text,#000000);">        </span><span style="color:var(--ds-text-accent-blue,#0055cc);">attribute</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">maxValue</span><span style="color:var(--ds-text,#000000);"> : </span><span style="color:var(--ds-text-accent-teal,#206a83);">Integer</span><span style="color:var(--ds-text,#000000);"> = </span><span style="color:var(--ds-background-accent-green-bolder,#1f845a);">5</span><span style="color:var(--ds-text,#000000);">;</span><br /><span style="color:var(--ds-text,#000000);">        </span><span style="color:var(--ds-text-accent-blue,#0055cc);">attribute</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">currentValue</span><span style="color:var(--ds-text,#000000);"> : </span><span style="color:var(--ds-text-accent-teal,#206a83);">Integer</span><span style="color:var(--ds-text,#000000);"> = </span><span style="color:var(--ds-background-accent-green-bolder,#1f845a);">3</span><span style="color:var(--ds-text,#000000);">;<br /></span><br /><span style="color:var(--ds-text,#000000);">        </span><span style="color:var(--ds-text-accent-blue,#0055cc);">language</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-red,#ae2e24);">&quot;Groovy&quot;</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-green-bolder,#164b35);">/* currentValue &lt; maxValue */</span><br /><span style="color:var(--ds-text,#000000);">}</span></p></ac:rich-text-body></ac:structured-macro><h4 class="cm-content q9tKkq_readonly m-0">Constraints in parts</h4><p>When a constraint is defined directly under a part, all attributes of the part are available in the script.</p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="fdb4d5d7-b99a-4d3c-af75-15ad6ca10e33"><ac:parameter ac:name="title">Example</ac:parameter><ac:rich-text-body><p><span style="color:var(--ds-text-accent-blue,#0055cc);">part</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">vehicle</span><span style="color:var(--ds-text,#000000);"> {</span><br /><span style="color:var(--ds-text,#000000);">    </span><span style="color:var(--ds-text-accent-blue,#0055cc);">attribute</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">maxSpeed</span><span style="color:var(--ds-text,#000000);"> : </span><span style="color:var(--ds-text-accent-teal,#206a83);">Integer</span><span style="color:var(--ds-text,#000000);"> = </span><span style="color:var(--ds-background-accent-green-bolder,#1f845a);">100</span><span style="color:var(--ds-text,#000000);">;</span><br /><span style="color:var(--ds-text,#000000);">    </span><span style="color:var(--ds-text-accent-blue,#0055cc);">attribute</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">currentSpeed</span><span style="color:var(--ds-text,#000000);"> : </span><span style="color:var(--ds-text-accent-teal,#206a83);">Integer</span><span style="color:var(--ds-text,#000000);"> = </span><span style="color:var(--ds-background-accent-green-bolder,#1f845a);">100</span><span style="color:var(--ds-text,#000000);">;<br /></span><span style="color:var(--ds-text,#000000);"><br />    </span><span style="color:var(--ds-text-accent-blue,#0055cc);">satisfy</span><span style="color:var(--ds-text,#000000);"> speedReq </span><span style="color:var(--ds-text-accent-blue,#0055cc);">by</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">this</span><span style="color:var(--ds-text,#000000);">;</span><br /><br /><span style="color:var(--ds-text,#000000);">    </span><span style="color:var(--ds-text-accent-blue,#0055cc);">assert</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">not</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">constraint</span><span style="color:var(--ds-text,#000000);"> {</span><br /><span style="color:var(--ds-text,#000000);">        </span><span style="color:var(--ds-text-accent-blue,#0055cc);">language</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-red,#ae2e24);">&quot;groovy&quot;</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-green-bolder,#164b35);">/* currentSpeed == maxSpeed */</span><br /><span style="color:var(--ds-text,#000000);">    }</span><br /><span style="color:var(--ds-text,#000000);">}</span></p></ac:rich-text-body></ac:structured-macro><h4 class="cm-content q9tKkq_readonly m-0">Constraints in requirements</h4><p>When a constraint is used inside a requirement, the requirement subject is made available to the script engine as the root context for evaluation. This means that the subject and its structure are directly accessible in the script engine.</p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="6ee9d0ad-7196-4304-bfd7-115dc72d4ea5"><ac:parameter ac:name="title">Example</ac:parameter><ac:rich-text-body><p><span style="color:var(--ds-text-accent-blue,#0055cc);">requirement</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">speedReq</span><span style="color:var(--ds-text,#000000);"> {</span><br /><span style="color:var(--ds-text,#000000);">    </span><span style="color:var(--ds-text-accent-blue,#0055cc);">subject</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">vehicle</span><span style="color:var(--ds-text,#000000);"> v :&gt; </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">vehicle</span><span style="color:var(--ds-text,#000000);">;<br /><br /></span><span style="color:var(--ds-text,#000000);">    </span><span style="color:var(--ds-text-accent-blue,#0055cc);">require</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">constraint</span><span style="color:var(--ds-text,#000000);"> {</span><br /><span style="color:var(--ds-text,#000000);">        </span><span style="color:var(--ds-text-accent-blue,#0055cc);">language</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-red,#ae2e24);">&quot;groovy&quot;</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-green-bolder,#164b35);">/* v.currentSpeed &lt; vehicle.maxSpeed */</span><br /><span style="color:var(--ds-text,#000000);">    }</span><br /><span style="color:var(--ds-text,#000000);">}</span></p></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=286557460 space=SYSML2EP version=4 -->
## PAGE 00021: (2026x) Clearing runtime values

- page_id: `286557460`
- space_key: `SYSML2EP`
- source_url: https://docs.nomagic.com/spaces/SYSML2EP/pages/286557460/2026x+Clearing+runtime+values
- version_number: 4
- version_date: `2026-01-30T18:41:30.990+01:00`
- ancestors: Versions of SysML v2 Evaluation Plugin Documentation > (2026x) SysML v2 Evaluation Plugin Documentation > (2026x) User guide
- labels: []

### NORMALIZED CONTENT

After [CONFLUENCE_PAGE title='(2026x) Evaluating model elements' space=''], the runtime values are stored in memory and reused for further evaluations, as shown in the example below.

#### PANEL: Example

Example

attributemyNumber:Real= randomNumberGen();//The script that returns a random number is envoked. 
attributemyNewNumber:Real=myNumber+5;//The generated number is reused. Using the myNumber attribute will not trigger the generation of a new number.

The runtime values stored in memory are cleared when you do the following:

- Modify the model.
- Clear values using the view toolbar.
- Clear values using the SysML v2 Model Evaluation console.

##### Clearing values via the view toolbar

If you evaluated model elements using views, you can use the view toolbar to clear the runtime values.

To clear runtime values via the view toolbar

- In the view toolbar, click the arrow next to [ATTACHMENT filename='evaluate_button.png'] and select Clear Values . [ATTACHMENT filename='clearing_values_via_diagram_toolbar.png']

##### Clearing values via the SysML v2 Model Evaluation console

You can use the **SysML v2 Model Evaluation** console to clear runtime values, regardless of where you initiated model evaluation.

To clear runtime values via the **SysML v2 Model Evaluation** console

- In the SysML v2 Model Evaluation console toolbar, click [ATTACHMENT filename='clear_values_icon.png'] . [ATTACHMENT filename='clearing_values_via_console.png']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p style="text-align: left;">After <ac:link><ri:page ri:content-title="(2026x) Evaluating model elements" /><ac:plain-text-link-body><![CDATA[model evaluation]]></ac:plain-text-link-body></ac:link>, the runtime values are stored in memory and reused for further evaluations, as shown in the example below.</p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="ef3e74a2-bf68-44a4-b050-97a1a91a7464"><ac:parameter ac:name="title">Example</ac:parameter><ac:rich-text-body><p><span style="color:var(--ds-text-accent-blue,#0055cc);">attribute</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">myNumber</span><span style="color:var(--ds-text,#000000);"> : </span><span style="color:var(--ds-text-accent-teal,#206a83);">Real</span><span style="color:var(--ds-text,#000000);"> = randomNumberGen(); </span><span style="color:var(--ds-text-accent-green-bolder,#164b35);">//The script that returns a random number is envoked.</span><br /><span style="color:var(--ds-text-accent-blue,#0055cc);">attribute</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">myNewNumber</span><span style="color:var(--ds-text,#000000);"> : </span><span style="color:var(--ds-text-accent-teal,#206a83);">Real</span><span style="color:var(--ds-text,#000000);"> = </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">myNumber</span><span style="color:var(--ds-text,#000000);"> + </span><span style="color:var(--ds-background-accent-green-bolder,#1f845a);">5</span><span style="color:var(--ds-text,#000000);">; </span><span style="color:var(--ds-text-accent-green-bolder,#164b35);">//The generated number is reused. Using the myNumber attribute will not trigger the generation of a new number.</span></p></ac:rich-text-body></ac:structured-macro><p class="code-java"><br />The runtime values stored in memory are cleared when you do the following:</p><ul style="text-align: left;"><li data-uuid="8ff056d2-95cb-44f0-9a0a-054b56c03b03">Modify the model.</li><li data-uuid="35f61a9c-55da-4192-baed-52651842ac88">Clear values using the view toolbar.</li><li data-uuid="44eaa21a-8137-4733-8643-06d60ec5967d">Clear values using the <strong>SysML v2 Model Evaluation</strong> console.</li></ul><h3 style="text-align: left;">Clearing values via the view toolbar</h3><p>If you evaluated model elements using views, you can use the view toolbar to clear the runtime values.</p><p>To clear runtime values via the view toolbar</p><hr /><ul><li data-uuid="1da4ccf3-9a89-40cb-98ec-3f418f12e353">In the view toolbar, click the arrow next to <ac:image ac:thumbnail="true" ac:height="14"><ri:attachment ri:filename="evaluate_button.png" /></ac:image> and select <strong>Clear Values</strong>.<br /><ac:image><ri:attachment ri:filename="clearing_values_via_diagram_toolbar.png" /></ac:image></li></ul><h3>Clearing values via the SysML v2 Model Evaluation console</h3><p>You can use the <strong>SysML v2 Model Evaluation</strong> console to clear runtime values, regardless of where you initiated model evaluation.</p><p>To clear runtime values via the <strong>SysML v2 Model Evaluation</strong> console</p><hr /><ul><li data-uuid="f13a5e93-689f-49ba-b2e7-8d8b074746c7">In the <strong>SysML v2 Model Evaluation</strong> console toolbar, click <ac:image><ri:attachment ri:filename="clear_values_icon.png" /></ac:image>.<br /><ac:image><ri:attachment ri:filename="clearing_values_via_console.png" /></ac:image></li></ul>
````

<!--NOMAGIC_PAGE id=254423501 space=SYSML2EP version=1 -->
## PAGE 00022: (2026x) Connecting to a running MATLAB session

- page_id: `254423501`
- space_key: `SYSML2EP`
- source_url: https://docs.nomagic.com/spaces/SYSML2EP/pages/254423501/2026x+Connecting+to+a+running+MATLAB+session
- version_number: 1
- version_date: `2025-09-12T14:49:42.310+02:00`
- ancestors: Versions of SysML v2 Evaluation Plugin Documentation > (2026x) SysML v2 Evaluation Plugin Documentation > (2026x) User guide > (2026x) Integration with MATLAB
- labels: ['connecting-to-matlab-session', 'matlab-session']

### NORMALIZED CONTENT

You can connect to a running MATLAB session and use all the variables in the MATLAB workspace.

To connect to a MATLAB session, [CONFLUENCE_PAGE title='(2026x) Integration with MATLAB' space=''].

To connect a running MATLAB session

- In the MATLAB command widow, execute the matlab.engine.shareEngine command.

After connecting to a MATLAB session, you can access variables in the MATLAB shared workspace that are not in the SysML v2 model. For example, you can define variables in MATLAB and then use them in calculations in your modeling tool.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>You can connect to a running MATLAB session and use all the variables in the MATLAB workspace.</p><ac:structured-macro ac:macro-id="65f34d32-45d5-43ef-97f4-8ea16e7b1763" ac:name="note" ac:schema-version="1"><ac:rich-text-body><p>To connect to a MATLAB session, <ac:link><ri:page ri:content-title="(2026x) Integration with MATLAB" /><ac:plain-text-link-body><![CDATA[MATLAB must be integrated with your modeling tool]]></ac:plain-text-link-body></ac:link>.</p></ac:rich-text-body></ac:structured-macro><p><br /></p><p>To connect <ac:inline-comment-marker ac:ref="c56add26-f5b3-46fc-8fb4-6eef404f8496">a running MATLAB session</ac:inline-comment-marker></p><hr /><ul><li>In the MATLAB command widow, execute the <strong>matlab.engine.shareEngine</strong> command.</li></ul><p class="auto-cursor-target"><br />After connecting to a MATLAB session, you can access variables in the MATLAB shared workspace that are not in the SysML v2 model. For example, you can define variables in MATLAB and then use them in calculations in your modeling tool.</p>
````

<!--NOMAGIC_PAGE id=254423438 space=SYSML2EP version=4 -->
## PAGE 00023: (2026x) Evaluating model elements

- page_id: `254423438`
- space_key: `SYSML2EP`
- source_url: https://docs.nomagic.com/spaces/SYSML2EP/pages/254423438/2026x+Evaluating+model+elements
- version_number: 4
- version_date: `2026-06-08T16:07:18.392+02:00`
- ancestors: Versions of SysML v2 Evaluation Plugin Documentation > (2026x) SysML v2 Evaluation Plugin Documentation > (2026x) User guide
- labels: []

### NORMALIZED CONTENT

This chapter describes how you can evaluate model elements, e.g., attributes, expressed through general mathematical calculations. When you evaluate a model element, all of its owned and inherited attributes are evaluated as well.

##### Evaluating model elements via the textual notation

To evaluate a model element via the textual notation

1. In the Textual Editor, place the cursor on the element you want to evaluate.
2. In the Textual Editor toolbar, click [ATTACHMENT filename='evaluate_button.png'] . [ATTACHMENT filename='evaluating_element_via_textual_notation.png']

The evaluation results are displayed in the **SysML v2 Model Evaluation** console.

##### Evaluating model elements via the Containment tree

To evaluate a model element via the Containment tree

- Right-click an element in the Containment tree and select Evaluate . [ATTACHMENT filename='evaluating_element_via_containment_tree.png']

The evaluation results are displayed in the **SysML v2 Model Evaluation** console.

##### Evaluating model elements in views

You can use views to evaluate individual model elements or all the elements displayed in a view.

To evaluate a model element in a view

1. Open the view displaying the model elements you want to evaluate.
2. Do one of the following:
  - Optionally, select the shapes of the elements you want to evaluate and, in the view toolbar, click [ATTACHMENT filename='evaluate_button.png'] . If you do not select any shapes, all the elements displayed in the view are evaluated.
  - Right-click an element shape and select Evaluate .
  - Select an element shape and, in the smart manipulator, click [ATTACHMENT filename='evaluate_button.png'] . [ATTACHMENT filename='evaluating_elements_in_diagram.png']

The evaluation results of the element attributes are displayed on the element shape. The attributes that pass or fail related requirements or constraints are highlighted in green or red. [CONFLUENCE_PAGE title='(2026x) Evaluating requirements and constraints' space=''].

##### Evaluating elements via the SysML v2 Model Evaluation console

You can evaluate model elements by writing an expression directly in the **SysML v2 Model Evaluation** console. However, you need to call the element you want to evaluate directly, because the console will not display the evaluation results of the owned and inherited elements.

To evaluate an element via the **SysML v2 Model Evaluation** console

1. Select Window > SysML v2 Model Evaluation to open the SysML v2 Model Evaluation console.
2. In the input box of the console, type the qualified name of the element you want to evaluate and press Enter. To save time, click [IMAGE alt='' src=''] in the toolbar of the **SysML v2 Model Evaluation** console to enable context selection in the Containment tree. When context selection is enabled, select the owner of the element you want to evaluate and enter only the element's name to evaluate it. [ATTACHMENT filename='evaluating_attribute_in_console.png']

The evaluation results are displayed in the **SysML v2 Model Evaluation**console as shown in the above figure.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>This chapter describes how you can evaluate model elements, e.g., attributes, expressed through general mathematical calculations. When you evaluate a model element, all of its owned and inherited attributes are evaluated as well.</p><h3>Evaluating model elements via the textual notation</h3><p>To evaluate a model element via the textual notation</p><hr /><ol><li>In the Textual Editor, place the cursor on the element you want to evaluate.</li><li>In the Textual Editor toolbar, click <ac:image><ri:attachment ri:filename="evaluate_button.png" /></ac:image>.<br /><ac:image><ri:attachment ri:filename="evaluating_element_via_textual_notation.png" /></ac:image></li></ol><p>The evaluation results are displayed in the <strong>SysML v2 Model Evaluation</strong> console.</p><h3>Evaluating model elements via the Containment tree</h3><p>To evaluate a model element via the Containment tree</p><hr /><ul><li>Right-click an element in the Containment tree and select <strong>Evaluate</strong>.<br /><ac:image><ri:attachment ri:filename="evaluating_element_via_containment_tree.png" /></ac:image></li></ul><p>The evaluation results are displayed in the <strong>SysML v2 Model Evaluation</strong> console.</p><h3>Evaluating model elements in views</h3><p>You can use views to evaluate individual model elements or all the elements displayed in a view. </p><p>To evaluate a model element in a view</p><hr /><ol><li data-uuid="a242c220-a1c1-499d-b7f6-7aec5dcb358b">Open the view displaying the model elements you want to evaluate.</li><li data-uuid="14837aaf-a759-40e6-bb2d-9201d4ddb150">Do one of the following:<ul><li>Optionally, select the shapes of the elements you want to evaluate and, in the view toolbar, click <ac:image><ri:attachment ri:filename="evaluate_button.png" /></ac:image>.<br /><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="6c510c2a-2148-496b-8784-b03a349ebdf2"><ac:rich-text-body><p>If you do not select any shapes, all the elements displayed in the view are evaluated.</p></ac:rich-text-body></ac:structured-macro></li><li>Right-click an element shape and select <strong>Evaluate</strong>.</li><li>Select an element shape and, in the smart manipulator, click <ac:image><ri:attachment ri:filename="evaluate_button.png" /></ac:image>.<br /><ac:image><ri:attachment ri:filename="evaluating_elements_in_diagram.png" /></ac:image></li></ul></li></ol><p>The evaluation results of the element attributes are displayed on the element shape. The attributes that pass or fail related requirements or constraints are highlighted in green or red. <ac:link><ri:page ri:content-title="(2026x) Evaluating requirements and constraints" /><ac:plain-text-link-body><![CDATA[Learn more about requirement and constraint evaluation]]></ac:plain-text-link-body></ac:link>.</p><h3>Evaluating elements via the SysML v2 Model Evaluation console</h3><p>You can evaluate model elements by writing an expression directly in the <strong>SysML v2 Model Evaluation</strong> console. However, you need to call the element you want to evaluate directly, because the console will not display the evaluation results of the owned and inherited elements.</p><p>To evaluate an element via the <strong>SysML v2 Model Evaluation</strong> console</p><hr /><ol><li>Select <strong>Window</strong> &gt; <strong>SysML v2 Model Evaluation</strong> to open the <strong>SysML v2 Model Evaluation</strong> console.</li><li>In the input box of the console, type the qualified name of the element you want to evaluate and press Enter.<br /><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="e7ef7365-c601-472f-a96c-786fb881295e"><ac:rich-text-body><p>To save time, click <ac:image ac:thumbnail="true" ac:height="16"><ri:attachment ri:filename="context_selection_icon.png" /></ac:image> in the toolbar of the <strong>SysML v2 Model Evaluation</strong> console to enable context selection in the Containment tree. When context selection is enabled, select the owner of the element you want to evaluate and enter only the element's name to evaluate it.</p></ac:rich-text-body></ac:structured-macro><ac:image><ri:attachment ri:filename="evaluating_attribute_in_console.png" /></ac:image></li></ol><p>The evaluation results are displayed in the <strong style="letter-spacing: 0.0px;">SysML v2 Model Evaluation</strong><span style="letter-spacing: 0.0px;"> console as shown in the above figure.</span></p>
````

<!--NOMAGIC_PAGE id=254423447 space=SYSML2EP version=3 -->
## PAGE 00024: (2026x) Evaluating requirements and constraints

- page_id: `254423447`
- space_key: `SYSML2EP`
- source_url: https://docs.nomagic.com/spaces/SYSML2EP/pages/254423447/2026x+Evaluating+requirements+and+constraints
- version_number: 3
- version_date: `2026-06-08T18:36:01.619+02:00`
- ancestors: Versions of SysML v2 Evaluation Plugin Documentation > (2026x) SysML v2 Evaluation Plugin Documentation > (2026x) User guide
- labels: []

### NORMALIZED CONTENT

Using views is the quickest way to evaluate multiple requirements and constraints at once. When the evaluation is complete, the view shapes are highlighted with icons or colors to indicate if requirements and constraints are satisfied or not. Failing and passing values are highlighted as well.You can also use the Containment tree,**SysML v2 Model Evaluation**console, or a view toevaluate individual satisfy requirements and assert constraints.

##### Evaluating requirements and constraints in views

To evaluate requirements and constraints in views

1. Open the view displaying the elements that have related requirements and constraints you want to evaluate.
2. Click [ATTACHMENT filename='evaluate_button.png'] in the view toolbar. To evaluate a single element or it's attribute displayed in a view, select the element shape or an attribute in the shape compartment before completing this step.To evaluate an individual satisfy requirement or assert constraint, select the element shape before completing this step. The evaluation result is *true* or *false*.

The view shapes are highlighted, indicating whether related system requirements and constraints pass or fail.

[IMAGE alt='' src='']

###### A view with requirement/constraint evaluation results.

###### Evaluation results in views

The following table explains the requirement and constraint evaluation results displayed on view shapes

| Annotation | Description | Tooltip |
| --- | --- | --- |
| ORA shape or its header is colored in green | The annotated elements satisfy related system requirements or constraints. | N/A |
| ORA shape or its header is colored in yellow | The annotated elements indirectly fail related system requirements or constraints. This means that system requirements or constraints are failed by inner parts of the annotated element. | Hover over the icon to see which inner elements fail system requirements or constraints. |
| ORA shape or its header is colored in red | The annotated elements fail related system requirements or constraints. | Hover over the icon to see which requirement or constraint failed. |
|  | The annotated values satisfy related system requirements or constraints. | N/A |
|  | The annotated values fail related system requirements or constraints. | Hover over the value to see the text of the failing requirement. |

###### Clearing evaluation results in views

To clear evaluation results in a view

- In the view toolbar, click an arrow next to [ATTACHMENT filename='evaluate_button.png'] and select Clear Values .

###### Customizing visual representation of evaluation results

You can customize how requirement and constraint verification results are displayed in views.

To customize visual representation of evaluation results in a view

1. In the main menu, select Options > Project .
2. In the Project Options dialog, select the Evaluation option group.
3. Specify the following options:
  - Display Verification Results As - Select Display Icons to add icons to shape headers. Select Paint Headers to color shapes or their headers.
  - Propagate Deep Nested Failures - Set to true to indicate nested requirement and constraint failures. Set to false to only highlight the shapes of the elements that directly fail a requirement or constraint.
4. Click OK to close the Project Options dialog.

##### Evaluating requirements and constraints via the Containment tree

To evaluate a requirement or constraint via the Containment tree

- In the Containment tree, right-click a satisfy requirement or an assert constraint and select Evaluate . [ATTACHMENT filename='evaluating_requirement_via_containment_tree.png']

The evaluation result (*true* or *false*) is displayed in the**SysML v2 Model Evaluation**console.

##### Evaluating requirements and constraints via the SysML v2 Model Evaluation console

To evaluate a requirement or constraint via the **SysML v2 Model Evaluation** console

1. Select Window > SysML v2 Model Evaluation to open the SysML v2 Model Evaluation console.
2. In the input box of the console, type the qualified name of the satisfy requirement or assert constraint you want to evaluate and press Enter. To save time, click [IMAGE alt='' src=''] in the toolbar of the **SysML v2 Model Evaluation** console to enable context selection in the Containment tree. When context selection is enabled, select the owner the element you want to evaluate and enter only the element's name to evaluate it. [ATTACHMENT filename='evaluating_requirement_via_console.png']

The evaluation result (*true*or*false*) is displayed in the**SysML v2 Model Evaluation**console.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>Using views is the quickest way to evaluate multiple requirements and constraints at once. <span style="letter-spacing: 0.0px;">When the evaluation is complete, the view shapes are highlighted with icons or colors to indicate if requirements and constraints are satisfied or not. Failing and passing values are highlighted as well. </span><span style="letter-spacing: 0.0px;">You can also use <span>the Containment tree, </span><strong>SysML v2 Model Evaluation</strong><span> console, or a view to </span>evaluate individual satisfy requirements and assert constraints.</span></p><h3>Evaluating requirements and constraints in views</h3><p>To evaluate requirements and constraints in views</p><hr /><ol><li>Open the view displaying the elements that have related requirements and constraints you want to evaluate.</li><li>Click <ac:image><ri:attachment ri:filename="evaluate_button.png" /></ac:image> in the view toolbar.<br /><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="e1d82617-d089-49d6-ab13-b70cf6ad59f1"><ac:rich-text-body><ul><li>To evaluate a single element or it's attribute displayed in a view, select the element shape or an attribute in the shape compartment before completing this step.</li><li>To evaluate an individual satisfy requirement or assert constraint, select the element shape before completing this step. The evaluation result is <em>true</em> or <em>false</em>.</li></ul></ac:rich-text-body></ac:structured-macro></li></ol><p><br />The view shapes are highlighted, indicating whether related system requirements and constraints pass or fail.</p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="evaluating_diagrams.png" /></ac:image></p><h6 style="text-align: center;">A view with requirement/constraint evaluation results.</h6><h4>Evaluation results in views</h4><p>The following table explains the requirement and constraint evaluation results displayed on view shapes</p><table class="wrapped relative-table" style="width: 85.0804%;"><colgroup><col style="width: 19.8294%;" /><col style="width: 49.12%;" /><col style="width: 31.0506%;" /></colgroup><tbody><tr><th style="text-align: left;" scope="col">Annotation</th><th scope="col">Description</th><th scope="col">Tooltip</th></tr><tr><td style="text-align: center;"><div class="content-wrapper"><p><ac:image><ri:attachment ri:filename="pass.png" /></ac:image></p><p>OR</p><p>A shape or its header is colored in green</p></div></td><td>The annotated elements satisfy related system requirements or constraints.</td><td>N/A</td></tr><tr><td style="text-align: center;"><div class="content-wrapper"><p><ac:image><ri:attachment ri:filename="indirect_failure.png" /></ac:image></p><p>OR</p><p>A shape or its header is colored in yellow</p></div></td><td>The annotated elements indirectly fail related system requirements or constraints. This means that system requirements or constraints are failed by inner parts of the annotated element. </td><td>Hover over the icon to see which inner elements fail system requirements or constraints.</td></tr><tr><td style="text-align: center;"><div class="content-wrapper"><p><ac:image><ri:attachment ri:filename="direct_failure.png" /></ac:image></p><p>OR</p><p>A shape or its header is colored in red</p></div></td><td>The annotated elements fail related system requirements or constraints.</td><td>Hover over the icon to see which requirement or constraint failed.</td></tr><tr><td style="text-align: center;"><div class="content-wrapper"><p><ac:image><ri:attachment ri:filename="passing_value.png" /></ac:image></p></div></td><td>The annotated values satisfy related system requirements or constraints.</td><td>N/A</td></tr><tr><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:height="20"><ri:attachment ri:filename="failing_value.png" /></ac:image></p></div></td><td>The annotated values fail related system requirements or constraints.</td><td>Hover over the value to see the text of the failing requirement.</td></tr></tbody></table><h4>Clearing evaluation results in views</h4><p>To clear evaluation results in a view</p><hr /><ul><li>In the view toolbar, click an arrow next to <ac:image><ri:attachment ri:filename="evaluate_button.png" /></ac:image> and select <strong>Clear Values</strong>.</li></ul><h4>Customizing visual representation of evaluation results </h4><p><span style="color:var(--ds-text,#172b4d);">You can customize how requirement and constraint verification results are displayed in views.</span></p><p><br /></p><p><span style="color:var(--ds-text,#172b4d);">To customize visual representation of evaluation results in a view</span></p><hr /><ol><li>In the main menu, select <strong>Options</strong> &gt; <strong>Project</strong>.</li><li>In the <strong>Project Options</strong>  dialog, select the <strong>Evaluation</strong> option group.</li><li>Specify the following options:<ul><li><strong>Display Verification Results As</strong> - Select <strong>Display Icons</strong> to add icons to shape headers. Select <strong>Paint Headers</strong> to color shapes or their headers.</li><li><strong>Propagate Deep Nested Failures</strong> - Set to <em>true</em> to indicate nested requirement and constraint failures. Set to <em>false</em> to only highlight the shapes of the elements that directly fail a requirement or constraint.</li></ul></li><li>Click <strong>OK</strong> to close the <strong>Project Options</strong> dialog.</li></ol><h3>Evaluating requirements and constraints via the Containment tree</h3><p>To evaluate a requirement or constraint via the Containment tree</p><hr /><ul><li>In the Containment tree, right-click a satisfy requirement or an assert constraint and select <strong>Evaluate</strong>.<br /><br /><ac:image><ri:attachment ri:filename="evaluating_requirement_via_containment_tree.png" /></ac:image></li></ul><p><br /><span style="color:var(--ds-text,#172b4d);">The evaluation result (<em>true</em> or <em>false</em>) is displayed in the </span><strong>SysML v2 Model Evaluation</strong><span style="color:var(--ds-text,#172b4d);"><span> </span>console.</span></p><h3><span style="letter-spacing: 0.0px;">Evaluating requirements and constraints via the SysML v2 Model Evaluation console</span></h3><p>To evaluate a requirement or constraint via the <strong>SysML v2 Model Evaluation</strong> console</p><hr /><ol><li>Select <strong>Window</strong> &gt; <strong>SysML v2 Model Evaluation</strong> to open the <strong>SysML v2 Model Evaluation</strong> console.</li><li>In the input box of the console, type the qualified name of the satisfy requirement or assert constraint you want to evaluate and press Enter.<br /><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="e7ef7365-c601-472f-a96c-786fb881295e"><ac:rich-text-body><p>To save time, click <ac:image ac:thumbnail="true" ac:height="16"><ri:attachment ri:filename="context_selection_icon.png" /></ac:image> in the toolbar of the <strong>SysML v2 Model Evaluation</strong> console to enable context selection in the Containment tree. When context selection is enabled, select the owner the element you want to evaluate and enter only the element's name to evaluate it.</p></ac:rich-text-body></ac:structured-macro><br /><ac:image ac:height="242"><ri:attachment ri:filename="evaluating_requirement_via_console.png" /></ac:image></li></ol><p><br /><span style="color:var(--ds-text,#172b4d);">The evaluation result (<em>true</em><span> </span>or<span> </span><em>false</em>) is displayed in the<span> </span></span><strong>SysML v2 Model Evaluation</strong><span style="color:var(--ds-text,#172b4d);"><span> </span>console.</span></p>
````

<!--NOMAGIC_PAGE id=254423509 space=SYSML2EP version=16 -->
## PAGE 00025: (2026x) Evaluation using Jupyter Notebook

- page_id: `254423509`
- space_key: `SYSML2EP`
- source_url: https://docs.nomagic.com/spaces/SYSML2EP/pages/254423509/2026x+Evaluation+using+Jupyter+Notebook
- version_number: 16
- version_date: `2026-03-17T14:22:38.100+01:00`
- ancestors: Versions of SysML v2 Evaluation Plugin Documentation > (2026x) SysML v2 Evaluation Plugin Documentation > (2026x) User guide > (2026x) Server-side evaluation
- labels: []

### NORMALIZED CONTENT

You can evaluate Teamwork Cloud projects on the server by using Jupyter Notebook. This chapter explains how to set up Jupyter Notebook for server-side evaluation and describes all available requests.

Server-side evaluation is available only with the Teamwork Cloud Enterprise license.

##### Setting up Jupyter Notebook

To set up Jupyter Notebook

- In Jupyter Notebook, run the following command to install a Python package from the < install_root >\plugins\com.nomagic.magicdraw.sysml2.evaluation.plugin/pyEval.zip file:

Use the following requests to evaluate Teamwork Cloud projects on the server:

##### Creating a client/session and authenticating

<server_host>

<server_port>

<TWC_user_name>

<TWC_user_password>

This request starts a work session and provides authentication to Teamwork Cloud.

The following table describes the parameters used in the request:

| Parameter | In | Required or optional | Description |
| --- | --- | --- | --- |
| server_host | path | required | The Teamwork Cloud server host name. |
| server_port | path | required | The Teamwork Cloud server port. |
| TWC_user_name | path | optional | The Teamwork Cloud user name. If you do not specify the user name in the request, an input field will be provided to specify it later. |
| TWC_user_password | path | optional | The Teamwork Cloud password. If you do not specify the password in the request, an input field will be provided to specify it later. |

##### Getting the list of Teamwork Cloud projects

client.get_projects()

This request provides the list of Teamwork Cloud projects accessible to you depending on your permissions. Only projects that you can read (the Read Resources permission) are returned.

```text

```

##### Getting the list of project commits

<projectID>

This request provides the list of commits for the specified Teamwork Cloud project.

| Parameter | In | Required or optional | Description |
| --- | --- | --- | --- |
| projectID | path | required | The Teamwork Cloud project ID. |

```text

```

##### Getting the list of root-level elements

client.get_roots(<projectID>, commit=<commitID>)

This request returns all root-level model elements for the specified project. If there are several namespaces, they are merged into one list.

The following table describes the parameters used in therequest:

| Parameter | In | Required or optional | Description |
| --- | --- | --- | --- |
| projectID | path | required | The Teamwork Cloud project ID. |
| commit | path | optional | The commit ID of the Teamwork Cloud project. If the commit ID is not specified, the latest committed version is used instead. |

```text

```

##### Evaluating a parameter or expression

client.evaluate(<projectID>, commit=<commitID>, context=<contextPath>, data=json.dumps(<parameters>)

This request evaluates the specified Teamwork Cloud project parameter or expression.

The following table describes the parameters used in therequest:

| Parameter | In | Required or optional | Description |
| --- | --- | --- | --- |
| projectID | path | required | The Teamwork Cloud project ID. |
| commit | path | optional | The commit ID of the Teamwork Cloud project. If the commit ID is not specified, the latest committed version is used instead. |
| context | path | optional | The context path of the outputs, inputs, and expressions used to evaluate and retrieve data, e.g., SpacecraftMassRollup::spaceCraft. |
| inputs | body | optional | The set of inputs to be provided for the evaluation. Only inputs with initial values can be modified during evaluation. |
| outputs | body | optional | The set of outputs to be obtained after the evaluation. If no outputs are specified, all values are returned based on the specified context. |
| expressions | body | optional | The parameter or expression you want to evaluate. |

```text

```

##### Displaying an interactive HTML table

open_evaluation_table(self, <projectID>, commit=<commitID>, context=<contextPath>, params=<parmaList>, title=<tableTitle>, verification=<FAIL/ALL/NONE>)

This REST API request returns a JSON object containing the URL to an interactive HTML table that dynamically retrieves data based on the specified context, parameters, and/or expressions.

The following table describes the parameters used in the REST APIrequest:

| Parameter | In | Required or optional | Description |
| --- | --- | --- | --- |
| projectID | path | required | The Teamwork Cloud project ID. |
| commit | path | optional | The commit ID of the Teamwork Cloud project. If the commit ID is not specified, the latest committed version is used instead. |
| context | path | optional | The context path of the table parameters and/or expressions used to evaluate and retrieve data, e.g. SpacecraftMassRollup::spaceCraft. |
| params | path | optional | A comma-separated list of the parameters and/or expressions to display. Use the keyword 'all' to include all available parameters based on the specified context. |
| title | path | optional | The title of the HML table. |
| verification | path | optional | Specify which verification results to display: FAIL - failing values are highlighted in red; ALL - both failing and passing values are highlighted in red and green, respectively; NONE - no verification results are displayed. |

```text

```

```text

```

```text

```

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p style="text-align: left;">You can evaluate Teamwork Cloud projects on the server by using Jupyter Notebook. This chapter explains how to set up Jupyter Notebook for server-side evaluation and describes all available requests.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="69f6901c-8022-42de-a5bd-e06c4d2f1871"><ac:rich-text-body><p>Server-side evaluation is available only with the Teamwork Cloud Enterprise license.</p></ac:rich-text-body></ac:structured-macro><h3>Setting up Jupyter Notebook</h3><p style="text-align: left;">To set up Jupyter Notebook</p><hr /><ul><li data-uuid="72bc8e7b-32ce-40ea-8b3e-f2dd919ed16e">In Jupyter Notebook, run the following command to install a Python package from the &lt;<em>install_root</em><em>&gt;\plugins\com.nomagic.magicdraw.sysml2.evaluation.<span style="color:var(--ds-text,#172b4d);">plugin/pyEval.zip</span></em><span> </span>file:<br /><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="1008cc78-0a4e-476a-9e42-f3eec6d268c4"><ac:plain-text-body><![CDATA[%pip install pyEval.zip]]></ac:plain-text-body></ac:structured-macro></li></ul><p style="text-align: left;">Use the following requests to evaluate Teamwork Cloud projects on the server:</p><h3>Creating a client/session and authenticating</h3><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="9564e4a8-1fa2-40d1-9fa9-4b6076430a22"><ac:rich-text-body>client = EvaluationWebClient('http(s)://<span style="color:var(--ds-background-accent-orange-bolder,#c25100);">&lt;server_host&gt;</span>:<span style="color:var(--ds-background-accent-orange-bolder,#c25100);">&lt;server_port&gt;</span>', '<span style="color:var(--ds-background-accent-orange-bolder,#c25100);">&lt;TWC_user_name&gt;</span>', '<span style="color:var(--ds-background-accent-orange-bolder,#c25100);">&lt;TWC_user_password&gt;</span>', False)</ac:rich-text-body></ac:structured-macro><p>This request starts a work session and provides authentication to Teamwork Cloud.</p><p>The following table describes the parameters used in the request:</p><table class="relative-table wrapped" style="width: 68.7671%;"><colgroup> <col style="width: 12.4396%;" /> <col style="width: 8.85127%;" /> <col style="width: 12.0455%;" /> <col style="width: 66.6636%;" /> </colgroup><tbody><tr><th>Parameter</th><th>In</th><th>Required or optional</th><th colspan="1">Description</th></tr><tr><td><strong>server_host</strong></td><td>path</td><td>required</td><td colspan="1">The Teamwork Cloud server host name.</td></tr><tr><td colspan="1"><strong>server_port</strong></td><td colspan="1">path</td><td colspan="1">required</td><td colspan="1">The Teamwork Cloud server port.</td></tr><tr><td colspan="1"><strong>TWC_user_name</strong></td><td colspan="1">path</td><td colspan="1">optional</td><td colspan="1"><p><span style="color:var(--ds-text,#172b4d);">The Teamwork Cloud user name. </span><span style="color:var(--ds-text,#172b4d);">If you do not specify the user name in the request, an input field will be provided to specify it later.</span></p></td></tr><tr><td colspan="1"><strong>TWC_user_password</strong></td><td colspan="1">path</td><td colspan="1">optional</td><td colspan="1"><span style="color:var(--ds-text,#172b4d);">The Teamwork Cloud password. </span><span style="color:var(--ds-text,#172b4d);">If you do not specify the password in the request, an input field will be provided to specify it later.</span></td></tr></tbody></table><h3 style="text-align: left;">Getting the list of Teamwork Cloud projects</h3><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="6037605c-3e3f-4edb-9b21-86a381d0f6dc"><ac:rich-text-body>client.get_projects()</ac:rich-text-body></ac:structured-macro><p style="text-align: left;"><span style="color:var(--ds-text,#333333);">This request provides the list of Teamwork Cloud projects accessible to you depending on your permissions. Only projects that you can read (the Read Resources permission) are returned.</span></p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="cb1de3dc-c6b6-41d9-86cd-1dee792071ad"><ac:parameter ac:name="title">Request and response example</ac:parameter><ac:plain-text-body><![CDATA[client.get_projects()

[
    {
        'created': '2025-05-27T08:36:26.723Z',
        '@id': '62b072da-22f7-4ee7-9abe-37605571f9b7',
        'description': '',
        '@type': 'Project',
        'defaultBranch': {
            '@id': '7765ea2c-7cc4-4f12-9606-060ae8c8304d'
        },
        'name': "Don't Panic Batmobile"
    },
    {
        'created': '2025-05-27T08:29:52.949Z',
        '@id': 'b906d747-63c2-4d37-a809-49bd07d2eeba',
        'description': '',
        '@type': 'Project',
        'defaultBranch': {
            '@id': 'bbe03735-3093-44d1-bd48-9856b4c00da4'
        },
        'name': 'SysML Customization'
    },
    {
        'created': '2025-05-28T17:03:01.861Z',
        '@id': 'e7b10c6e-ae3c-49e9-af97-42d6384ebc2c',
        'description': '',
        '@type': 'Project',
        'defaultBranch': {
            '@id': 'e6d3df11-3260-4428-bb41-a0a2255e8c69'
        },
        'name': 'Spacecraft Mass Rollup V2'
    },
    {
        'created': '2025-05-28T17:07:08.197Z',
        '@id': '76ac1bae-11c9-434b-9096-3639ab338cf0',
        'description': '',
        '@type': 'Project',
        'defaultBranch': {
            '@id': 'fd07a9b3-8be1-4e6e-90f1-2992d983f8e0'
        },
        'name': 'Hinge Monte Carlo Analysis V2'
    }
]]]></ac:plain-text-body></ac:structured-macro><p style="text-align: left;"><br /></p><h3 style="text-align: left;">Getting the list of project commits</h3><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="2591f19f-8505-45ec-a3ef-9b1a622a1e0e"><ac:rich-text-body>client.get_commits(<span style="color:var(--ds-background-accent-orange-bolder,#c25100);">&lt;projectID&gt;</span>)</ac:rich-text-body></ac:structured-macro><p>This request provides the list of commits for the specified Teamwork Cloud project.</p><table class="relative-table wrapped" style="width: 68.7671%;"><colgroup> <col style="width: 12.4396%;" /> <col style="width: 8.85127%;" /> <col style="width: 12.0455%;" /> <col style="width: 66.6636%;" /> </colgroup><tbody><tr><th>Parameter</th><th>In</th><th>Required or optional</th><th colspan="1">Description</th></tr><tr><td><strong>projectID</strong></td><td>path</td><td>required</td><td colspan="1">The Teamwork Cloud project ID.</td></tr></tbody></table><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="60ce26c7-eac3-49bd-8bc0-68eb9b7c4583"><ac:parameter ac:name="title">Request and response example</ac:parameter><ac:plain-text-body><![CDATA[client.get_commits('62b072da-22f7-4ee7-9abe-37605571f9b7')

[
    {
        'created': '2025-05-27T08:36:26.410Z',
        '@id': '15a995d2-01cf-499b-a2d8-1f943af14320',
        'description': '** no message **',
        'owningProject': {
            '@id': '62b072da-22f7-4ee7-9abe-37605571f9b7'
        },
        'previousCommit': [
            {'@id': None}
        ]
    },
    {
        'created': '2025-05-27T08:39:34.763Z',
        '@id': 'b7a03a50-f42a-495d-9bd1-d87978d7f73f',
        'description': '** no message **',
        'owningProject': {
            '@id': '62b072da-22f7-4ee7-9abe-37605571f9b7'
        },
        'previousCommit': [
            {'@id': '15a995d2-01cf-499b-a2d8-1f943af14320'}
        ]
    }
]]]></ac:plain-text-body></ac:structured-macro><h3 style="text-align: left;">Getting the list of root-level elements</h3><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="c3c70852-5135-4c08-9292-2c88b44ea84b"><ac:rich-text-body><p><span style="color:var(--ds-text,#172b4d);">client.get_roots(<span style="color:var(--ds-background-accent-orange-bolder,#c25100);">&lt;projectID&gt;</span>, commit=<span style="color:var(--ds-background-accent-orange-bolder,#c25100);">&lt;commitID&gt;</span>)</span></p></ac:rich-text-body></ac:structured-macro><p>This request returns all root-level model elements for the specified project. <span style="color:var(--ds-text,#172B4D);">If there are several namespaces, they are merged into one list.</span></p><p><span style="color:var(--ds-text,#172b4d);">The following table describes the parameters used in the </span>request<span style="color:var(--ds-text,#172b4d);">:</span></p><table class="relative-table wrapped" style="width: 68.6413%;"><colgroup><col style="width: 9.82647%;" /><col style="width: 7.84533%;" /><col style="width: 10.4604%;" /><col style="width: 71.8678%;" /></colgroup><tbody><tr><th>Parameter</th><th>In</th><th>Required or optional</th><th>Description</th></tr><tr><td><strong>projectID</strong></td><td>path</td><td>required</td><td>The Teamwork Cloud project ID.</td></tr><tr><td><strong>commit</strong></td><td>path</td><td>optional</td><td>The commit ID of the Teamwork Cloud project. If the commit ID is not specified, the latest committed version is used instead.</td></tr></tbody></table><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="41a398b4-3d38-4b02-bf03-c849ca3bb406"><ac:parameter ac:name="title">Request and response example</ac:parameter><ac:plain-text-body><![CDATA[client.get_roots('62b072da-22f7-4ee7-9abe-37605571f9b7')

[
  {
    "@id": "d6f0eea9-70fd-4ca8-b75f-3c794bd64f2b",
    "@type": "Package",
    "name": "Calculations",
    "elementId": "_G2tFcXD4Ee-huNu5so5rpw"
  },
  {
    "@id": "530d4e51-4f1d-4dfc-aae3-df7ece7dcdea",
    "@type": "Package",
    "name": "Requirements",
    "elementId": "_G2vhsXD4Ee-huNu5so5rpw"
  },
  {
    "@id": "2c5055d8-2899-4727-89c0-51072f20b60f",
    "@type": "Package",
    "name": "Vehicle",
    "elementId": "_G2ylAXD4Ee-huNu5so5rpw"
  },
  {
    "@id": "c1f8cfff-421a-4ab7-ac51-c1ad63899feb",
    "@type": "Package",
    "name": "TradeStudyAnalysis",
    "elementId": "_achG0XQLEe-Dbrd_o2J6Vg"
  }
]]]></ac:plain-text-body></ac:structured-macro><h3 style="text-align: left;">Evaluating a parameter or expression</h3><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="b1cda8f0-a944-47d9-80c8-da8df670be11"><ac:rich-text-body><p>client.evaluate(<span style="color:var(--ds-background-accent-orange-bolder,#c25100);">&lt;projectID&gt;</span>, commit=<span style="color:var(--ds-background-accent-orange-bolder,#c25100);">&lt;commitID&gt;</span>, context=<span style="color:var(--ds-background-accent-orange-bolder,#c25100);">&lt;contextPath&gt;</span>, data=json.dumps(<span style="color:var(--ds-background-accent-orange-bolder,#c25100);">&lt;parameters&gt;</span>)</p></ac:rich-text-body></ac:structured-macro><p style="text-align: left;"><span style="color:var(--ds-text,#172b4d);">This request evaluates the specified Teamwork Cloud project parameter or expression.</span></p><p style="text-align: left;"><span style="color:var(--ds-text,#172b4d);">The following table describes the parameters used in the </span>request<span style="color:var(--ds-text,#172b4d);">:</span></p><table class="relative-table wrapped" style="width: 68.6413%;"><colgroup><col style="width: 9.82647%;" /><col style="width: 7.84533%;" /><col style="width: 10.4604%;" /><col style="width: 71.8678%;" /></colgroup><tbody><tr><th>Parameter</th><th>In</th><th>Required or optional</th><th>Description</th></tr><tr><td><strong>projectID</strong></td><td>path</td><td>required</td><td>The Teamwork Cloud project ID.</td></tr><tr><td><strong>commit</strong></td><td>path</td><td>optional</td><td>The commit ID of the Teamwork Cloud project. If the commit ID is not specified, the latest committed version is used instead.</td></tr><tr><td><strong>context</strong></td><td>path</td><td>optional</td><td><span style="color:var(--ds-text-accent-purple-bolder,#352c63);">The context path of the outputs, inputs, and expressions used to evaluate and retrieve data, e.g., SpacecraftMassRollup::spaceCraft.</span></td></tr><tr><td><strong>inputs</strong></td><td>body</td><td>optional</td><td>The set of inputs to be provided for the evaluation. <span style="color:var(--ds-text-accent-purple-bolder,#352c63);">Only inputs with initial values can be modified during evaluation.</span></td></tr><tr><td><strong>outputs</strong></td><td>body</td><td>optional</td><td>The set of outputs to be obtained after the evaluation. <span style="color:var(--ds-text-accent-purple-bolder,#352c63);">If no outputs are specified, all values are returned based on the specified context.</span></td></tr><tr><td><strong>expressions</strong></td><td>body</td><td>optional</td><td><div class="content-wrapper"><p>The parameter or expression you want to evaluate.</p></div></td></tr></tbody></table><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="9ce7bcd1-f696-4cae-a962-1e39e6de0c3e"><ac:parameter ac:name="title">Request example with a request body</ac:parameter><ac:plain-text-body><![CDATA[parameters = {
 "inputs":
   {
        "propulsion.thruster.me":32,
        "telecom.amplifier.me":15
   },
 "outputs": 
    [ 
        "me",
        "propulsion.mee",
        "propulsion.tank.me",
        "propulsion.thruster.me",
        "telecom.me",
        "telecom.antenna.me",
        "telecom.amplifier.me"
    ]
}

client.evaluate('a9e055de-e288-4b81-81e4-e24bbb32cedd', context='SpacecraftMassRollup::spacecraft', data=json.dumps(parameters))]]></ac:plain-text-body></ac:structured-macro><h3 style="text-align: left;">Displaying an interactive HTML table</h3><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="db3f2dcb-7a12-4b80-9beb-3093dfc154af"><ac:rich-text-body><p>open_evaluation_table(self, <span style="color:var(--ds-background-accent-orange-bolder,#c25100);">&lt;projectID&gt;</span>, commit=<span style="color:var(--ds-background-accent-orange-bolder,#c25100);">&lt;commitID&gt;</span>, context=<span style="color:var(--ds-background-accent-orange-bolder,#c25100);">&lt;contextPath&gt;</span>, params=<span style="color:var(--ds-background-accent-orange-bolder,#c25100);">&lt;parmaList&gt;</span>, title=<span style="color:var(--ds-background-accent-orange-bolder,#c25100);">&lt;tableTitle&gt;</span>, verification=<span style="color:var(--ds-background-accent-orange-bolder,#c25100);">&lt;FAIL/ALL/NONE&gt;</span>)</p></ac:rich-text-body></ac:structured-macro><p style="text-align: left;"><span style="color:var(--ds-text,#172b4d);">This REST API request returns a JSON object containing the URL to an interactive HTML table that dynamically retrieves data based on the specified context, parameters, and/or expressions.</span></p><p style="text-align: left;"><span style="color:var(--ds-text,#172b4d);">The following table describes the parameters used in the REST API<span> </span></span>request<span style="color:var(--ds-text,#172b4d);">:</span></p><table class="relative-table wrapped" style="width: 68.6413%;"><colgroup><col style="width: 9.82647%;" /><col style="width: 7.84533%;" /><col style="width: 10.4604%;" /><col style="width: 71.8678%;" /></colgroup><tbody><tr><th>Parameter</th><th>In</th><th>Required or optional</th><th>Description</th></tr><tr><td><strong>projectID</strong></td><td>path</td><td>required</td><td>The Teamwork Cloud project ID.</td></tr><tr><td><strong>commit</strong></td><td>path</td><td>optional</td><td>The commit ID of the Teamwork Cloud project. If the commit ID is not specified, the latest committed version is used instead.</td></tr><tr><td><strong>context</strong></td><td>path</td><td>optional</td><td><span style="color:var(--ds-text-accent-purple-bolder,#352c63);">The context path of the table parameters and/or expressions used to evaluate and retrieve data, e.g. SpacecraftMassRollup::spaceCraft.</span></td></tr><tr><td><strong>params</strong></td><td>path</td><td>optional</td><td><span style="color:var(--ds-text-accent-purple-bolder,#352c63);">A comma-separated list of the parameters and/or expressions to display. Use the keyword 'all' to include all available parameters based on the specified context.</span></td></tr><tr><td><strong>title</strong></td><td>path</td><td>optional</td><td>The title of the HML table.</td></tr><tr><td><strong>verification </strong></td><td>path</td><td>optional</td><td>Specify which verification results to display: <strong>FAIL</strong> - failing values are highlighted in red; <strong>ALL</strong> - both failing and passing values are highlighted in red and green, respectively; <strong>NONE</strong> - no verification results are displayed.</td></tr></tbody></table><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="8868d21a-0d23-441b-8e6e-fbfba7234301"><ac:parameter ac:name="title">Request example</ac:parameter><ac:plain-text-body><![CDATA[open_evaluation_table(self, dc8b24ee-462d-4874-8b52-b85978f242cc, commit=3fa85f64-5717-4562-b3fc-2c963f66afa6, context=SpacecraftMassRollup::spaceCraft, params=me,propulsion.tank.me,propulsion.thruster.me, title=SpaceCraftMassRollup)]]></ac:plain-text-body></ac:structured-macro><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="7eeb9179-0138-4d81-9713-2a4351d13de4"><ac:parameter ac:name="title">Request example</ac:parameter><ac:plain-text-body><![CDATA[open_evaluation_table(self, dc8b24ee-462d-4874-8b52-b85978f242cc, commit=3fa85f64-5717-4562-b3fc-2c963f66afa6, context=SpacecraftMassRollup::spaceCraft, params=all, title=SpaceCraftMassRollup, verification=fail)]]></ac:plain-text-body></ac:structured-macro><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="8ccc7679-c4d7-4164-aabf-1ac0e533016a"><ac:parameter ac:name="title">Request example</ac:parameter><ac:plain-text-body><![CDATA[open_evaluation_table(self, dc8b24ee-462d-4874-8b52-b85978f242cc, params=SpacecraftMassRollup::spaceCraft.me,SpacecraftMassRollup::spaceCraft.propulsion.tank.me, title=SpaceCraftMassRollup)]]></ac:plain-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=254423507 space=SYSML2EP version=7 -->
## PAGE 00026: (2026x) Evaluation using REST API

- page_id: `254423507`
- space_key: `SYSML2EP`
- source_url: https://docs.nomagic.com/spaces/SYSML2EP/pages/254423507/2026x+Evaluation+using+REST+API
- version_number: 7
- version_date: `2026-04-28T18:25:31.668+02:00`
- ancestors: Versions of SysML v2 Evaluation Plugin Documentation > (2026x) SysML v2 Evaluation Plugin Documentation > (2026x) User guide > (2026x) Server-side evaluation
- labels: []

### NORMALIZED CONTENT

You can use the following REST API requests to evaluate Teamwork Cloud projects on the server.

Server-side evaluation is available only with the Teamwork Cloud Enterprise license.

For more information about evaluation-related REST APIs, see *https://<server_IP>:8443/sysmlv2-api/swagger-ui/index.html,* where**<server_IP>**is your Teamwork Cloud server IP.There, you can findREST API descriptions in both machine-readable and human-readable formats.

##### Evaluating a parameter or expression

<projectID>

<commitID>

evaluate?context=

<contextPath>

This REST API request evaluates the specified Teamwork Cloud project parameter or expression.

The following table describes the parameters used in the REST APIrequest:

| Parameter | In | Required or optional | Description |
| --- | --- | --- | --- |
| projects | path | required | The Teamwork Cloud project ID. |
| commits | path | optional | The commit ID of the Teamwork Cloud project. If the commit ID is not specified, the latest committed version is used instead. |
| context | path | optional | The context path of the outputs, inputs, and expressions used to evaluate and retrieve data, e.g., SpacecraftMassRollup::spaceCraft |
| inputs | body | optional | The set of inputs to be provided for the evaluation. Only inputs with initial values can be modified during evaluation. |
| outputs | body | optional | The set of outputs to be obtained after the evaluation. If no outputs are specified, all values are returned based on the specified context. |
| expressions | body | optional | The parameter or expression you want to evaluate. |

```shell

```

```text

```

##### Displaying an interactive HTML table

GET /projects/<projectID>/commits/<commitID>/evaluate/table-view?context=<contextPath>?params=<paramsList>?title=<tableTitle>?verification=<FAIL/ALL/NONE>

This REST API request returns a URL to an interactive HTML table that dynamically retrieves data based on the specified context, parameters and/or expressions.

The following table describes the parameters used in the REST APIrequest:

| Parameter | In | Required or optional | Description |
| --- | --- | --- | --- |
| projects | path | required | The Teamwork Cloud project ID. |
| commits | path | optional | The commit ID of the Teamwork Cloud project. If the commit ID is not specified, the latest committed version is used instead. |
| context | path | optional | The context path of the table parameters and/or expressions used to evaluate and retrieve data, e.g. SpacecraftMassRollup::spaceCraft |
| params | path | optional | A comma-separated list of the parameters and/or expressions to display. Use the keyword 'all' to include all available parameters based on the specified context. |
| title | path | optional | The title of the HML table. |
| verification | path | optional | Specify which verification results to display: FAIL - failing values are highlighted in red; ALL - both failing and passing values are highlighted in red and green, respectively; NONE - no verification results are displayed. |

```text

```

```text

```

```text

```

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p style="text-align: left;">You can use the following REST API requests to evaluate Teamwork Cloud projects on the server.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="b15118b5-24d4-4c63-83be-9ddae7e0278a"><ac:rich-text-body><p>Server-side evaluation is available only with the Teamwork Cloud Enterprise license.</p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="2a448455-b7a0-47f3-ab58-4fbcc1877ce2"><ac:rich-text-body><p><span style="color:var(--ds-text,#172b4d);"><span style="color:var(--ds-text,#172b4d);">For more information about evaluation-related REST APIs, see <em style="text-align: left;">https://&lt;server_IP&gt;:8443/sysmlv2-api/swagger-ui/index.html,</em> <span style="color:var(--ds-text,#172b4d);">where<span> </span></span><strong style="text-align: left;">&lt;server_IP&gt;</strong><span style="color:var(--ds-text,#172b4d);"><span> </span>is your Teamwork Cloud server IP.</span></span><span style="color:var(--ds-text,#172b4d);"> There, you can find<span> </span></span>REST API descriptions in both machine-readable and human-readable formats.</span></p></ac:rich-text-body></ac:structured-macro><h3 style="text-align: left;">Evaluating a parameter or expression</h3><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="b1cda8f0-a944-47d9-80c8-da8df670be11"><ac:rich-text-body>POST /api/projects/<span style="color:var(--ds-background-accent-orange-bolder,#c25100);">&lt;projectID&gt;</span>/commits/<span style="color:var(--ds-background-accent-orange-bolder,#c25100);">&lt;commitID&gt;</span>/<span style="color:var(--ds-text,#172b4d);">evaluate?context=</span><span style="color:var(--ds-background-accent-orange-bolder,#c25100);">&lt;contextPath&gt;</span></ac:rich-text-body></ac:structured-macro><p style="text-align: left;"><span style="color:var(--ds-text,#172b4d);">This REST API request evaluates the specified Teamwork Cloud project parameter or expression.</span></p><p style="text-align: left;"><span style="color:var(--ds-text,#172b4d);">The following table describes the parameters used in the REST API<span> </span></span>request<span style="color:var(--ds-text,#172b4d);">:</span></p><table class="relative-table wrapped" style="width: 68.6413%;"><colgroup class=""><col class="" style="width: 9.82647%;" /><col class="" style="width: 7.84533%;" /><col class="" style="width: 10.4604%;" /><col class="" style="width: 71.8678%;" /></colgroup><tbody class=""><tr class=""><th>Parameter</th><th>In</th><th>Required or optional</th><th>Description</th></tr><tr class=""><td><strong>projects</strong></td><td>path</td><td>required</td><td>The Teamwork Cloud project ID.</td></tr><tr class=""><td><strong>commits</strong></td><td>path</td><td>optional</td><td>The commit ID of the Teamwork Cloud project. If the commit ID is not specified, the latest committed version is used instead.</td></tr><tr class=""><td><strong>context</strong></td><td>path</td><td>optional</td><td><span style="color:var(--ds-text-accent-purple-bolder,#352c63);">The context path of the outputs, inputs, and expressions used to evaluate and retrieve data, e.g., SpacecraftMassRollup::spaceCraft</span></td></tr><tr class=""><td><strong>inputs</strong></td><td>body</td><td>optional</td><td>The set of inputs to be provided for the evaluation. <span style="color:var(--ds-text-accent-purple-bolder,#352c63);">Only inputs with initial values can be modified during evaluation.</span></td></tr><tr class=""><td><strong>outputs</strong></td><td>body</td><td>optional</td><td>The set of outputs to be obtained after the evaluation. <span style="color:var(--ds-text-accent-purple-bolder,#352c63);">If no outputs are specified, all values are returned based on the specified context.</span></td></tr><tr class=""><td><strong>expressions</strong></td><td>body</td><td>optional</td><td><div class="content-wrapper"><p>The parameter or expression you want to evaluate.</p></div></td></tr></tbody></table><p><br /></p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="5de60b50-1f5b-47a3-b326-dbcc33d31869"><ac:parameter ac:name="language">shell</ac:parameter><ac:parameter ac:name="title">Request and response example with the request body</ac:parameter><ac:plain-text-body><![CDATA[POST /projects/dc8b24ee-462d-4874-8b52-b85978f242cc/evaluate?context=SpacecraftMassRollup::spaceCraft

{
  "inputs":
   {
        "propulsion.thruster.me":10,
        "telecom.amplifier.me":15
   },
 "outputs": 
    [ 
        "me",
        "propulsion.mee",
        "propulsion.tank.me",
        "propulsion.thruster.me",
        "telecom.me",
        "telecom.antenna.me",
        "telecom.amplifier.me"
    ]
}

Response:

{'outputs': 
 {'me': 144.0,
  'propulsion.tank.me': 100.0,
  'propulsion.thruster.me': 10.0,
  'telecom.me': 34.0,
  'telecom.amplifier.me': 15.0,
  'telecom.antenna.me': 19.0
 }
}]]></ac:plain-text-body></ac:structured-macro><p><br /></p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="457ffbed-3c36-4994-9206-eb01d204ae9c"><ac:parameter ac:name="title">Request and response example with the request body</ac:parameter><ac:plain-text-body><![CDATA[POST /projects/fa6e7f27-f922-4718-aba4-6b909d6d1dcc/evaluate

{
  "inputs":
   {
        "TradeStudyAnalysis::VehicleAlternatives::vehicle_A.grossMass":2000,
        "TradeStudyAnalysis::VehicleAlternatives::vehicle_A.grossMass":1000
   }
 "expressions": 
    [ 
        "TradeStudyAnalysis::VehicleAlternatives::vehicle_A.stoppingDistance-TradeStudyAnalysis::VehicleAlternatives::vehicle_B.stoppingDistance"
    ]
}

=== Response ===

{
'expressions': 
 ['TradeStudyAnalysis::VehicleAlternatives::vehicle_A.stoppingDistance-TradeStudyAnalysis::VehicleAlternatives::vehicle_B.stoppingDistance':56.9344
 ]
}]]></ac:plain-text-body></ac:structured-macro><h3 style="text-align: left;">Displaying an interactive HTML table</h3><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="db3f2dcb-7a12-4b80-9beb-3093dfc154af"><ac:rich-text-body><p><span style="color:var(--ds-text,#172b4d);">GET /projects/<span style="color:var(--ds-background-accent-orange-bolder,#c25100);">&lt;projectID&gt;</span>/commits/<span style="color:var(--ds-background-accent-orange-bolder,#c25100);">&lt;commitID&gt;</span>/evaluate/</span>table-view<span style="color:var(--ds-text,#172b4d);">?</span>context<span style="color:var(--ds-text,#172b4d);">=<span style="color:var(--ds-background-accent-orange-bolder,#c25100);">&lt;contextPath&gt;</span>?</span>params<span style="color:var(--ds-text,#172b4d);">=<span style="color:var(--ds-background-accent-orange-bolder,#c25100);">&lt;paramsList&gt;</span>?</span>title<span style="color:var(--ds-text,#172b4d);">=<span style="color:var(--ds-background-accent-orange-bolder,#c25100);">&lt;tableTitle&gt;<span style="color:var(--ds-text,#172b4d);">?verification=<span style="color:var(--ds-background-accent-orange-bolder,#c25100);">&lt;FAIL/ALL/NONE&gt;</span></span></span></span></p></ac:rich-text-body></ac:structured-macro><p style="text-align: left;"><span style="color:var(--ds-text,#172b4d);">This REST API request returns a URL to an interactive HTML table that dynamically retrieves data based on the specified context, parameters and/or expressions.</span></p><p style="text-align: left;"><span style="color:var(--ds-text,#172b4d);">The following table describes the parameters used in the REST API<span> </span></span>request<span style="color:var(--ds-text,#172b4d);">:</span></p><table class="relative-table wrapped" style="width: 68.6413%;"><colgroup class=""><col class="" style="width: 9.82647%;" /><col class="" style="width: 7.84533%;" /><col class="" style="width: 10.4604%;" /><col class="" style="width: 71.8678%;" /></colgroup><tbody class=""><tr class=""><th>Parameter</th><th>In</th><th>Required or optional</th><th>Description</th></tr><tr class=""><td><strong>projects</strong></td><td>path</td><td>required</td><td>The Teamwork Cloud project ID.</td></tr><tr class=""><td><strong>commits</strong></td><td>path</td><td>optional</td><td>The commit ID of the Teamwork Cloud project. If the commit ID is not specified, the latest committed version is used instead.</td></tr><tr class=""><td><strong>context</strong></td><td>path</td><td>optional</td><td><span style="color:var(--ds-text-accent-purple-bolder,#352c63);">The context path of the table parameters and/or expressions used to evaluate and retrieve data, e.g. SpacecraftMassRollup::spaceCraft</span></td></tr><tr class=""><td><strong>params</strong></td><td>path</td><td>optional</td><td><span style="color:var(--ds-text-accent-purple-bolder,#352c63);">A comma-separated list of the parameters and/or expressions to display. Use the keyword 'all' to include all available parameters based on the specified context.</span></td></tr><tr class=""><td><strong>title</strong></td><td>path</td><td>optional</td><td>The title of the HML table.</td></tr><tr class=""><td><strong>verification</strong></td><td>path</td><td>optional</td><td>Specify which verification results to display: <strong>FAIL</strong> - failing values are highlighted in red; <strong>ALL</strong> - both failing and passing values are highlighted in red and green, respectively; <strong>NONE</strong> - no verification results are displayed.</td></tr></tbody></table><p><br /></p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="8868d21a-0d23-441b-8e6e-fbfba7234301"><ac:parameter ac:name="title">Request example</ac:parameter><ac:plain-text-body><![CDATA[GET /projects/dc8b24ee-462d-4874-8b52-b85978f242cc/commits/3fa85f64-5717-4562-b3fc-2c963f66afa6/evaluate/table-view?context=SpacecraftMassRollup::spaceCraft&params=me,propulsion.tank.me,propulsion.thruster.me&title=SpaceCraftMassRollup]]></ac:plain-text-body></ac:structured-macro><p><br /></p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="7eeb9179-0138-4d81-9713-2a4351d13de4"><ac:parameter ac:name="title">Request example</ac:parameter><ac:plain-text-body><![CDATA[GET /projects/dc8b24ee-462d-4874-8b52-b85978f242cc/commits/3fa85f64-5717-4562-b3fc-2c963f66afa6/evaluate/table-view?context=SpacecraftMassRollup::spaceCraft&params=all&title=SpaceCraftMassRollup?verification=fail]]></ac:plain-text-body></ac:structured-macro><p><br /></p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="8ccc7679-c4d7-4164-aabf-1ac0e533016a"><ac:parameter ac:name="title">Request example</ac:parameter><ac:plain-text-body><![CDATA[GET /projects/dc8b24ee-462d-4874-8b52-b85978f242cc/evaluate/table-view?params=SpacecraftMassRollup::spaceCraft.me,SpacecraftMassRollup::spaceCraft.propulsion.tank.me&title=SpaceCraftMassRollup]]></ac:plain-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=254423466 space=SYSML2EP version=2 -->
## PAGE 00027: (2026x) Exporting evaluation results to CSV

- page_id: `254423466`
- space_key: `SYSML2EP`
- source_url: https://docs.nomagic.com/spaces/SYSML2EP/pages/254423466/2026x+Exporting+evaluation+results+to+CSV
- version_number: 2
- version_date: `2025-11-17T18:29:59.532+01:00`
- ancestors: Versions of SysML v2 Evaluation Plugin Documentation > (2026x) SysML v2 Evaluation Plugin Documentation > (2026x) User guide
- labels: []

### NORMALIZED CONTENT

You can use views to evaluate model elements displayed in a view and export the results to a CSV file.

To export the evaluation results to a CSV file

1. In the view toolbar, click [IMAGE alt='' src=''] to evaluate model elements displayed in the view.
2. In the view toolbar, click the arrow next to [IMAGE alt='' src=''] andselect**Export to CSV**. When the evaluation is performed on selected elements, only the results for those elements are exported. If no elements were selected, the export will include results for all elements displayed in the view. [ATTACHMENT filename='export_to_csv.png']
3. In the**CSV Export Options** dialog, specify the export options. To learn more, see 
[IMAGE alt='' src='']
4. Click **OK** to export the evaluation results.

The CSV file with evaluation results is saved in the specified location. You can open the file by clicking a link in the message saying that the CSV file was generated successfully.

##### CSV Export Options dialog

The following table describes the UI elements of the **CSV Export Options** dialog.

| UI element | Description |
| --- | --- |
| CSV Delimiter | Select the character used to separate values (columns) in a CSV file. The default CSV delimiter is selected according to the machine's locale. |
| Export annotated only | Select the Export annotated only check box to export only annotated results in the view. Clear the check box to export all evaluation results. |
| Attributes as columns | Select the Attributes as columns check box to export attributes to columns and paths to the corresponding rows. Clear the check box to print every value in a separate row. |
| Output | Specify the path to the CSV file. By default, the project directory is selected. |

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><span style="color:var(--ds-text,#172b4d);">You can use views to evaluate model elements displayed in a view and export the results to a CSV file.</span></p><p>To export the evaluation results to a CSV file</p><hr /><ol><li data-uuid="c0cf6758-be65-46d7-91a9-092bfae1a6ca"><p>In the <span style="color:var(--ds-text,#172b4d);">view toolbar</span>, click <ac:image ac:thumbnail="true" ac:height="14"><ri:attachment ri:filename="evaluate_button.png" /></ac:image> to evaluate model elements displayed in the view.</p></li><li data-uuid="a268a305-7057-445f-a5f9-0ff2ec45dbed"><p>In the <span style="color:var(--ds-text,#172b4d);">view toolbar</span>, click the arrow next to <ac:image ac:thumbnail="true" ac:height="14"><ri:attachment ri:filename="evaluate_button.png" /></ac:image> and<span> select </span><strong>Export to CSV</strong><span>.<br /></span></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="bffab1b5-a500-4117-a00a-f37583c604e0"><ac:rich-text-body><p><span style="color:var(--ds-text,#172b4d);">When the evaluation is performed on selected elements, only the results for those elements are exported. If no elements were selected, the export will include results for all elements displayed in the view.</span></p></ac:rich-text-body></ac:structured-macro><ac:image ac:height="224"><ri:attachment ri:filename="export_to_csv.png" /></ac:image></li><li data-uuid="d37d5400-33be-46fb-8296-8c941c24544b"><p>In the<strong> CSV Export Options</strong> dialog, specify the export options. To learn more, see <ac:link ac:anchor="CSV Export Options dialog"><ac:plain-text-link-body><![CDATA[CSV Export Options dialog.]]></ac:plain-text-link-body></ac:link><br /><ac:image><ri:attachment ri:filename="csv_export_options.png" /></ac:image></p></li><li data-uuid="75e03cce-96b8-4580-874d-c9ec39f159ce"><p>Click <strong>OK</strong> to export the evaluation results.</p></li></ol><p>The CSV file with evaluation results is saved in the specified location. You can open the file by clicking a link in the message saying that the CSV file was generated successfully.</p><h3>CSV Export Options dialog</h3><p>The following table describes the UI elements of the <strong>CSV Export Options</strong> dialog.</p><table class="relative-table" style="width: 99.1781%;"><colgroup class=""><col class="" style="width: 14.0953%;" /><col class="" style="width: 85.9237%;" /></colgroup><tbody class=""><tr class=""><th><p>UI element</p></th><th><p>Description</p></th></tr><tr class=""><td><p><strong>CSV Delimiter</strong></p></td><td><p>Select the character used to separate values (columns) in a CSV file. The default CSV delimiter is selected according to the machine's locale. </p></td></tr><tr class=""><td><p><strong>Export annotated only</strong></p></td><td><p>Select the <strong>Export annotated only </strong>check box to export only annotated results in the view. Clear the check box to export all evaluation results.</p></td></tr><tr class=""><td><p><strong>Attributes as columns</strong></p></td><td><div class="content-wrapper"><p>Select the <strong>Attributes as columns </strong>check box to export attributes to columns and paths to the corresponding rows. Clear the check box to print every value in a separate row.</p><p><ac:image ac:height="222"><ri:attachment ri:filename="attributes_as_columns.png" /></ac:image></p></div></td></tr><tr class=""><td><p><strong>Output</strong></p></td><td><p>Specify the path to the CSV file. By default, the project directory is selected. </p></td></tr></tbody></table>
````

<!--NOMAGIC_PAGE id=254423474 space=SYSML2EP version=6 -->
## PAGE 00028: (2026x) Integration with MATLAB

- page_id: `254423474`
- space_key: `SYSML2EP`
- source_url: https://docs.nomagic.com/spaces/SYSML2EP/pages/254423474/2026x+Integration+with+MATLAB
- version_number: 6
- version_date: `2026-01-23T18:09:03.444+01:00`
- ancestors: Versions of SysML v2 Evaluation Plugin Documentation > (2026x) SysML v2 Evaluation Plugin Documentation > (2026x) User guide
- labels: ['matlab-integration']

### NORMALIZED CONTENT

If you install MATLAB and integrate it with your modeling tool, you will be able to evaluate scripts written in MATLAB syntax. For example, you can [use MATLAB as a script language to define the return in calculations](https://docs.nomagic.com/SYSML2EP/?contextKey=invoking-calculations&version=2026x).

#### NOTE: Prerequisites

Prerequisites

- MATLAB 2023a and later versions have been tested for compatibility with SysML v2 projects. Support for older versions is not guaranteed.
- You must use the 64-bit version of MATLAB so it will work with the 64-bit version of modeling tools.
- If MATLAB was integrated before installing the SysML v2 Evaluation plugin, you must reintegrate it to ensure compatibility with SysML v2 projects.
- On Windows, the application requires admin rights to complete the integration with MATLAB. If admin rights are not granted or available, you will not be able to use MATLAB with SysML v2 projects.

To integrate a modeling tool with MATLAB

1. In the main menu, select Tools > Integrations .
2. In the Integrations dialog, select MATLAB and click Integrate/Remove Integration . 
[IMAGE alt='' src='']
3. In the open dialog, specify the MATLAB home directory . 
[IMAGE alt='' src=''] The JRE home directory is selected automatically.
4. Click **OK**.
5. If you use Windows, click Yes to grant the application admin rights. Otherwise, go to the next step.
6. When you get a message saying to restart the modeling tool, click OK and restart the modeling tool.

**Related pages**

- [CONFLUENCE_PAGE title='(2026x) Connecting to a running MATLAB session' space='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p>If you install MATLAB and integrate it with your modeling tool, you will be able to evaluate scripts written in MATLAB syntax. For example, you can <a href="https://docs.nomagic.com/SYSML2EP/?contextKey=invoking-calculations&amp;version=2026x">use MATLAB as a script language to define the return in calculations</a>.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="a62fa631-c814-4636-a48c-c579d65b2775"><ac:parameter ac:name="title">Prerequisites</ac:parameter><ac:rich-text-body><ul><li data-uuid="0f9a499d-d053-4472-894f-e329ec70f8c6"><span style="color:var(--ds-text,#172b4d);">MATLAB 2023a and later versions have been tested for compatibility with SysML v2 projects. Support for older versions is not guaranteed.</span></li><li data-uuid="372bd176-af20-464f-b4ac-bf2be63adef1">You must use the 64-bit version of MATLAB so it will work with the 64-bit version of modeling tools.</li><li data-uuid="c0347e7a-fcd6-45e2-aec5-d7f76c4f209b">If MATLAB was integrated before installing the SysML v2 Evaluation plugin, you must reintegrate it to ensure compatibility with SysML v2 projects.</li><li data-uuid="9bb937c9-74e9-4b15-a63a-a03c32d10ae6"><p style="text-align: left;">On Windows, the application requires admin rights to complete the integration with MATLAB. If admin rights are not granted or available, you will not be able to use MATLAB with SysML v2 projects.</p></li></ul></ac:rich-text-body></ac:structured-macro><p><br /></p><p>To integrate a modeling tool with MATLAB</p><hr /><ol><li class="auto-cursor-target" data-uuid="f1b960de-4a91-471d-a0d2-ce7c391afbb2">In the main menu, select <strong>Tools </strong>&gt;<strong> Integrations</strong>.</li><li class="auto-cursor-target" data-uuid="11bcd78c-702a-4a89-a8ea-2feb4ce06d15">In the <strong>Integrations</strong> dialog, select <strong>MATLAB</strong> and click <strong>Integrate/Remove Integration</strong><span>.<br /><ac:image><ri:attachment ri:filename="integrations_dialog.png" /></ac:image><br /></span></li><li class="auto-cursor-target" data-uuid="ddf9f71a-d4c6-4d94-ad7c-130d290fa335">In the open dialog, specify the <strong style="letter-spacing: 0.0px;">MATLAB home directory</strong><span style="letter-spacing: 0.0px;">.<br /><ac:image><ri:attachment ri:filename="directory_selection_dialog.png" /></ac:image><br /></span><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="a5efb116-d9fe-4aa3-9560-a7b3acea2d26"><ac:rich-text-body><p>The JRE home directory is selected automatically.</p></ac:rich-text-body></ac:structured-macro></li><li class="auto-cursor-target" data-uuid="a93d2697-df55-4441-be7d-1624c7a6a55f"><p class="auto-cursor-target">Click <strong>OK</strong>.</p></li><li class="auto-cursor-target" data-uuid="a2ae8355-7523-45c5-85f1-27e30273afec">If you use Windows, click <strong>Yes</strong> to grant the application admin rights. Otherwise, go to the next step.</li><li class="auto-cursor-target" data-uuid="35d6b7fc-cf73-47fc-a9f1-b9c60ee1f0a8">When you get a message saying to restart the modeling tool, click <strong>OK</strong> and restart the modeling tool.</li></ol></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><strong>Related pages</strong></p><ul><li><ac:link><ri:page ri:content-title="(2026x) Connecting to a running MATLAB session" /></ac:link></li></ul></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=272728839 space=SYSML2EP version=2 -->
## PAGE 00029: (2026x) Invoking actions

- page_id: `272728839`
- space_key: `SYSML2EP`
- source_url: https://docs.nomagic.com/spaces/SYSML2EP/pages/272728839/2026x+Invoking+actions
- version_number: 2
- version_date: `2025-11-25T13:00:27.844+01:00`
- ancestors: Versions of SysML v2 Evaluation Plugin Documentation > (2026x) SysML v2 Evaluation Plugin Documentation > (2026x) User guide
- labels: []

### NORMALIZED CONTENT

An action definition is a type of occurrence definition that specifies what an action is and how it can be performed. An action usage is a type of occurrence usage that represents the**actual use of one or more action definitions within a particular situation or context.

You can invoke action definitions and action usages as described below.

To invoke an action definition or action usage

1. Create and define an action definition or action usage. For instructions, refer to the SysML v2 Plugin documentation .
2. Create an expression that invokes the action, for example, by defining an attribute whose value is computed through the action invocation.
3. Access a specific output of the action invocation in one of the following ways:
  - Use the dot notation in the invocation expression. ExampleactiondefcalculateCircleParameters{ 
inradius:Real; 
outdiameter:Real=radius*2; 
outcircumference:Real=diameter*3.14; 
outarea:Real=radius*radius*3.14; 
} 
partwheel{ 
attributeradius:Real=12; 
attributearea:Real=calculateCircleParameters(radius).area; 
}
  - Create a feature that stores the invocation result, e.g., actionInvoke , and then select specific outputs using dot notation. ExampleactiondefcalculateCircleParameters{ 
inradius:Real; 
outdiameter:Real=radius*2; 
outcircumference:Real=diameter*3.14; 
outarea:Real=radius*radius*3.14; 
} 
partwheel{ 
attributeradius:Real=12; 
actionInvoke=calculateCircleParameters(radius); 
attributearea:Real=actionInvoke.area; 
attributeperimeter:Real=actionInvoke.circumference; 
}
4. Evaluate an element whose value depends on the action invocation (e.g., the area or perimeter attribute in the above examples). For more information, see [CONFLUENCE_PAGE title='(2026x) Evaluating model elements' space=''] .

The evaluation results are displayed in the**SysML v2 Model Evaluation**console.

##### Defining calculation return in other script languages

When defining an action using a textual representation element, you can implement its behavior using an external scripting language. Supported languages include JavaScript, Groovy, Beanshell, Python (via Jython), and MATLAB. Only primitive types such as Integer, Real, Boolean, and String are supported as input and output parameters.

#### NOTE: Using MATLAB

Using MATLAB

To evaluate scripts defined in the MATLAB syntax:

- [CONFLUENCE_PAGE title='(2026x) Integration with MATLAB' space=''] .
- The language must be specified as "MATLAB" (case sensitive).

#### PANEL: Example

Example

actiondefcounter{ 
inoutcount:Real:=0; 
language"groovy"/* count=count+1 */} 
} 
attributestartCount: Integer = counter().count//The result will be 1 because there is no input 
attributecontinueCount: Integer = counter(startCount).count//The result will be 2. Input overrides the initial value set in the parameter.

Actions also support "ToolExecution", which allows mapping features with different names between the SysML v2 model and MATLAB scripts.

#### PANEL: Example

Example

actioncomputeStoppingDistance { 
privateimportAnalysisTooling::*; 
@ToolExecution { 
:>> toolName ="MATLAB"; 
:>> uri ="run('C:/custom/path/to/StoppingAnalysisExec.m')"; 
} 
inmass : Real = vehicle.grossMass /4{@ToolVariable { name ="m"; }}; 
inspeed : Real = vehicle.speed /3.6{@ToolVariable { name ="v0"; }}; 
outDistance : Real = vehicle.stoppingDistance {@ToolVariable { name ="stoppingDistance"; }}; 
outkineticEnergy : Real = vehicle.kineticEnergy {@ToolVariable { name ="e"; }};

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>An action definition is a type of occurrence definition that specifies what an action is and how it can be performed. An action usage is a type of occurrence usage that represents the<em> </em>actual use of one or more action definitions within a particular situation or context.</p><p>You can invoke action definitions and action usages as described below.</p><p>To invoke an action definition or action usage</p><hr /><ol><li data-uuid="186c59fe-bc20-4821-acfd-955ef255002b">Create and define an action definition or action usage. For instructions, refer to the <a href="https://docs.nomagic.com/SYSML2P/?contextKey=creating-actions&amp;version=latest">SysML v2 Plugin documentation</a>.</li><li data-uuid="01127edb-6d1d-48c6-94c3-4218653fb14c">Create an expression that invokes the action, for example, by defining an attribute whose value is computed through the action invocation.</li><li data-uuid="61815bdb-074f-46db-b970-4f5f00c367cc"><span style="color:var(--ds-text,#172b4d);">Access a specific output of the action invocation in one of the following ways:</span><ul><li data-uuid="d874b0ac-0a93-459e-b58a-feb069b04110"><span style="color:var(--ds-text,#172b4d);">Use the dot notation in the invocation expression.<br /></span><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="fdfd9bdc-4046-4997-a249-ad9e5c74d2de"><ac:parameter ac:name="title">Example</ac:parameter><ac:rich-text-body><p><span style="color:var(--ds-text-accent-blue,#0055cc);">action</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">def</span><span style="color:var(--ds-chart-gray-bold,#8590a2);"> </span><span style="color:var(--ds-text-accent-teal,#206a83);">calculateCircleParameters</span><span style="color:var(--ds-text,#000000);"> {</span><br /><span style="color:var(--ds-text,#000000);">            </span><span style="color:var(--ds-text-accent-blue,#0055cc);">in</span><span style="color:var(--ds-chart-gray-bold,#8590a2);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">radius</span><span style="color:var(--ds-text,#000000);"> : </span><span style="color:var(--ds-text-accent-teal,#206a83);">Real</span><span style="color:var(--ds-text,#000000);">;</span><br /><span style="color:var(--ds-text,#000000);">            </span><span style="color:var(--ds-text-accent-blue,#0055cc);">out</span><span style="color:var(--ds-chart-gray-bold,#8590a2);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">diameter</span><span style="color:var(--ds-text,#000000);"> : </span><span style="color:var(--ds-text-accent-teal,#206a83);">Real</span><span style="color:var(--ds-text,#000000);"> = </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">radius</span><span style="color:var(--ds-text,#000000);"> * </span><span style="color:var(--ds-background-accent-green-bolder,#1f845a);">2</span><span style="color:var(--ds-text,#000000);">;</span><br /><span style="color:var(--ds-text,#000000);">            </span><span style="color:var(--ds-text-accent-blue,#0055cc);">out</span><span style="color:var(--ds-chart-gray-bold,#8590a2);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">circumference</span><span style="color:var(--ds-text,#000000);"> : </span><span style="color:var(--ds-text-accent-teal,#206a83);">Real</span><span style="color:var(--ds-text,#000000);"> = </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">diameter</span><span style="color:var(--ds-text,#000000);"> * </span><span style="color:var(--ds-background-accent-green-bolder,#1f845a);">3.14</span><span style="color:var(--ds-text,#000000);">;</span><br /><span style="color:var(--ds-text,#000000);">            </span><span style="color:var(--ds-text-accent-blue,#0055cc);">out</span><span style="color:var(--ds-chart-gray-bold,#8590a2);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">area</span><span style="color:var(--ds-text,#000000);"> : </span><span style="color:var(--ds-text-accent-teal,#206a83);">Real</span><span style="color:var(--ds-text,#000000);"> = </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">radius</span><span style="color:var(--ds-text,#000000);"> * </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">radius</span><span style="color:var(--ds-text,#000000);"> * </span><span style="color:var(--ds-background-accent-green-bolder,#1f845a);">3.14</span><span style="color:var(--ds-text,#000000);">;</span><br /><span style="color:var(--ds-text,#000000);">        }</span><br /><span style="color:var(--ds-text-accent-blue,#0055cc);">part</span><span style="color:var(--ds-chart-gray-bold,#8590a2);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">wheel</span><span style="color:var(--ds-text,#000000);"> {</span><br /><span style="color:var(--ds-text,#000000);">            </span><span style="color:var(--ds-text-accent-blue,#0055cc);">attribute</span><span style="color:var(--ds-chart-gray-bold,#8590a2);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">radius</span><span style="color:var(--ds-text,#000000);"> : </span><span style="color:var(--ds-text-accent-teal,#206a83);">Real</span><span style="color:var(--ds-text,#000000);"> = </span><span style="color:var(--ds-background-accent-green-bolder,#1f845a);">12</span><span style="color:var(--ds-text,#000000);">;</span><br /><span style="color:var(--ds-text,#000000);">            </span><span style="color:var(--ds-text-accent-blue,#0055cc);">attribute</span><span style="color:var(--ds-chart-gray-bold,#8590a2);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">area</span><span style="color:var(--ds-text,#000000);"> : </span><span style="color:var(--ds-text-accent-teal,#206a83);">Real</span><span style="color:var(--ds-text,#000000);"> = </span><span style="color:var(--ds-text-accent-teal,#206a83);">calculateCircleParameters</span><span style="color:var(--ds-text,#000000);">(</span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">radius</span><span style="color:var(--ds-text,#000000);">).</span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">area</span><span style="color:var(--ds-text,#000000);">;</span><br /><span style="color:var(--ds-text,#000000);">        }</span></p></ac:rich-text-body></ac:structured-macro><span style="color:var(--ds-text,#172b4d);"><br /></span></li><li data-uuid="3e402f5a-7e3d-4a75-8461-7cc760912742"><span style="color:var(--ds-text,#172b4d);">Create a feature that stores the invocation result, e.g., </span><em>actionInvoke</em>, <span style="color:var(--ds-text,#172b4d);">and then select specific outputs using dot notation.<br /></span><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="8fc65334-9f57-4157-9c1b-749899816c3f"><ac:parameter ac:name="title">Example</ac:parameter><ac:rich-text-body><p><span style="color:var(--ds-text-accent-blue,#0055cc);">action</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">def</span><span style="color:var(--ds-chart-gray-bold,#8590a2);"> </span><span style="color:var(--ds-text-accent-teal,#206a83);">calculateCircleParameters</span><span style="color:var(--ds-text,#000000);"> {</span><br /><span style="color:var(--ds-text,#000000);">            </span><span style="color:var(--ds-text-accent-blue,#0055cc);">in</span><span style="color:var(--ds-chart-gray-bold,#8590a2);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">radius</span><span style="color:var(--ds-text,#000000);"> : </span><span style="color:var(--ds-text-accent-teal,#206a83);">Real</span><span style="color:var(--ds-text,#000000);">;</span><br /><span style="color:var(--ds-text,#000000);">            </span><span style="color:var(--ds-text-accent-blue,#0055cc);">out</span><span style="color:var(--ds-chart-gray-bold,#8590a2);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">diameter</span><span style="color:var(--ds-text,#000000);"> : </span><span style="color:var(--ds-text-accent-teal,#206a83);">Real</span><span style="color:var(--ds-text,#000000);"> = </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">radius</span><span style="color:var(--ds-text,#000000);"> * </span><span style="color:var(--ds-background-accent-green-bolder,#1f845a);">2</span><span style="color:var(--ds-text,#000000);">;</span><br /><span style="color:var(--ds-text,#000000);">            </span><span style="color:var(--ds-text-accent-blue,#0055cc);">out</span><span style="color:var(--ds-chart-gray-bold,#8590a2);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">circumference</span><span style="color:var(--ds-text,#000000);"> : </span><span style="color:var(--ds-text-accent-teal,#206a83);">Real</span><span style="color:var(--ds-text,#000000);"> = </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">diameter</span><span style="color:var(--ds-text,#000000);"> * </span><span style="color:var(--ds-background-accent-green-bolder,#1f845a);">3.14</span><span style="color:var(--ds-text,#000000);">;</span><br /><span style="color:var(--ds-text,#000000);">            </span><span style="color:var(--ds-text-accent-blue,#0055cc);">out</span><span style="color:var(--ds-chart-gray-bold,#8590a2);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">area</span><span style="color:var(--ds-text,#000000);"> : </span><span style="color:var(--ds-text-accent-teal,#206a83);">Real</span><span style="color:var(--ds-text,#000000);"> = </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">radius</span><span style="color:var(--ds-text,#000000);"> * </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">radius</span><span style="color:var(--ds-text,#000000);"> * </span><span style="color:var(--ds-background-accent-green-bolder,#1f845a);">3.14</span><span style="color:var(--ds-text,#000000);">;</span><br /><span style="color:var(--ds-text,#000000);">        }</span><br /><span style="color:var(--ds-text-accent-blue,#0055cc);">part</span><span style="color:var(--ds-chart-gray-bold,#8590a2);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">wheel</span><span style="color:var(--ds-text,#000000);"> {</span><br /><span style="color:var(--ds-text,#000000);">            </span><span style="color:var(--ds-text-accent-blue,#0055cc);">attribute</span><span style="color:var(--ds-chart-gray-bold,#8590a2);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">radius</span><span style="color:var(--ds-text,#000000);"> : </span><span style="color:var(--ds-text-accent-teal,#206a83);">Real</span><span style="color:var(--ds-text,#000000);"> = </span><span style="color:var(--ds-background-accent-green-bolder,#1f845a);">12</span><span style="color:var(--ds-text,#000000);">;</span><br /><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">            actionInvoke</span><span style="color:var(--ds-text,#000000);"> = </span><span style="color:var(--ds-text-accent-teal,#206a83);">calculateCircleParameters</span><span style="color:var(--ds-text,#000000);">(</span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">radius</span><span style="color:var(--ds-text,#000000);">);</span><br /><span style="color:var(--ds-text,#000000);">            </span><span style="color:var(--ds-text-accent-blue,#0055cc);">attribute</span><span style="color:var(--ds-chart-gray-bold,#8590a2);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">area</span><span style="color:var(--ds-text,#000000);"> : </span><span style="color:var(--ds-text-accent-teal,#206a83);">Real</span><span style="color:var(--ds-text,#000000);"> = </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">actionInvoke</span><span style="color:var(--ds-text,#000000);">.</span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">area</span><span style="color:var(--ds-text,#000000);">;</span><br /><span style="color:var(--ds-text,#000000);">            </span><span style="color:var(--ds-text-accent-blue,#0055cc);">attribute</span><span style="color:var(--ds-chart-gray-bold,#8590a2);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">perimeter</span><span style="color:var(--ds-text,#000000);"> : </span><span style="color:var(--ds-text-accent-teal,#206a83);">Real</span><span style="color:var(--ds-text,#000000);"> = </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">actionInvoke</span><span style="color:var(--ds-text,#000000);">.</span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">circumference</span><span style="color:var(--ds-text,#000000);">;</span><br /><span style="color:var(--ds-text,#000000);">        }</span></p></ac:rich-text-body></ac:structured-macro><span style="color:var(--ds-text,#172b4d);"><br /></span></li></ul></li><li data-uuid="a234ed53-86bc-4886-8fcd-4930fa75db86">Evaluate an element whose value depends on the action invocation (e.g., the <em>area</em> or <em>perimeter</em> attribute in the above examples). For more information, see <ac:link><ri:page ri:content-title="(2026x) Evaluating model elements" /><ac:plain-text-link-body><![CDATA[Evaluating model elements]]></ac:plain-text-link-body></ac:link>.</li></ol><p><span style="color:var(--ds-text,#172b4d);">The evaluation results are displayed in the </span><strong>SysML v2 Model Evaluation</strong><span style="color:var(--ds-text,#172b4d);"><span> </span>console.</span></p><h3><span style="color:var(--ds-text,#172b4d);">Defining calculation return in other script languages</span></h3><p>When defining an action using a <span style="color:var(--ds-text,#172b4d);">textual representation element</span>, you can implement its behavior using an external scripting language. Supported languages include JavaScript, Groovy, Beanshell, Python (via Jython), and MATLAB. Only primitive types such as Integer, Real, Boolean, and String are supported as input and output parameters.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="7112b935-00f1-4054-b9ef-71f2449b1345"><ac:parameter ac:name="title">Using MATLAB</ac:parameter><ac:rich-text-body><p>To evaluate scripts defined in the MATLAB syntax:</p><ul><li data-uuid="9f0620ea-5fdb-4dca-aab6-0c50f3e23d60"><ac:link><ri:page ri:content-title="(2026x) Integration with MATLAB" /><ac:plain-text-link-body><![CDATA[MATLAB must be integrated with your modeling tool]]></ac:plain-text-link-body></ac:link>.</li><li data-uuid="b5ccd0d5-2a5d-499e-b9d5-96029ce985bf">The language must be specified as &quot;MATLAB&quot; (case sensitive).</li></ul></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="c0d6ec98-2f53-4b20-8d8e-4d37f62150b8"><ac:parameter ac:name="title">Example</ac:parameter><ac:rich-text-body><p><span style="color:var(--ds-text-accent-blue,#0055cc);">action</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">def</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-teal,#206a83);">counter</span><span style="color:var(--ds-text,#000000);"> {</span><br /><span style="color:var(--ds-text,#000000);">    </span><span style="color:var(--ds-background-accent-red-bolder,#c9372c);"> </span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-background-accent-red-bolder,#c9372c);"> </span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-background-accent-red-bolder,#c9372c);"> </span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-background-accent-red-bolder,#c9372c);">  </span><span style="color:var(--ds-text-accent-blue,#0055cc);">inout</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">count</span><span style="color:var(--ds-text,#000000);"> : </span><span style="color:var(--ds-text-accent-teal,#206a83);">Real</span><span style="color:var(--ds-text,#000000);"> := </span><span style="color:var(--ds-background-accent-green-bolder,#1f845a);">0</span><span style="color:var(--ds-text,#000000);">;</span><br /><span style="color:var(--ds-text,#000000);">            </span><span style="color:var(--ds-text-accent-blue,#0055cc);">language</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-red,#ae2e24);">&quot;groovy&quot;</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-green-bolder,#164b35);">/* count=count+1 */</span><span style="color:var(--ds-text,#000000);"> } </span><br /><span style="color:var(--ds-text,#000000);">        }</span><br /><span style="color:var(--ds-text-accent-blue,#0055cc);">attribute</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">startCount</span><span style="color:var(--ds-text,#000000);"> : Integer = counter().count </span><span style="color:var(--ds-text-accent-green-bolder,#164b35);">//The result will be 1 because there is no input </span><br /><span style="color:var(--ds-text-accent-blue,#0055cc);">attribute</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">continueCount</span><span style="color:var(--ds-text,#000000);"> : Integer = counter(</span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">startCount</span><span style="color:var(--ds-text,#000000);">).count </span><span style="color:var(--ds-text-accent-green-bolder,#164b35);">//The result will be 2. Input overrides the initial value set in the parameter.</span></p></ac:rich-text-body></ac:structured-macro><p>Actions also support &quot;ToolExecution&quot;, <span data-teams="true">which allows mapping features with different names between the SysML v2 model and MATLAB scripts.</span></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="71f0bc6d-8deb-4cb2-9366-e6f7da3c2ea4"><ac:parameter ac:name="title">Example</ac:parameter><ac:rich-text-body><p><span style="color:var(--ds-text-accent-blue,#0055cc);">action</span><span style="color:var(--ds-text,#000000);"> computeStoppingDistance {</span><br /><span style="color:var(--ds-text,#000000);">            </span><span style="color:var(--ds-text-accent-blue,#0055cc);">private</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">import</span><span style="color:var(--ds-text,#000000);"> AnalysisTooling::*;</span><br /><span style="color:var(--ds-text,#000000);">            @ToolExecution {</span><br /><span style="color:var(--ds-text,#000000);">                :&gt;&gt; toolName = </span><span style="color:var(--ds-text-accent-red,#ae2e24);">&quot;MATLAB&quot;</span><span style="color:var(--ds-text,#000000);">;</span><br /><span style="color:var(--ds-text,#000000);">                :&gt;&gt; uri = </span><span style="color:var(--ds-text-accent-red,#ae2e24);">&quot;run('C:/custom/path/to/StoppingAnalysisExec.m')&quot;</span><span style="color:var(--ds-text,#000000);">;</span><br /><span style="color:var(--ds-text,#000000);">            }</span><br /><span style="color:var(--ds-text,#000000);">            </span><span style="color:var(--ds-text-accent-blue,#0055cc);">in</span><span style="color:var(--ds-text,#000000);"> mass : Real = vehicle.grossMass / </span><span style="color:var(--ds-background-accent-green-bolder,#1f845a);">4</span><span style="color:var(--ds-text,#000000);"> {@ToolVariable { name = </span><span style="color:var(--ds-text-accent-red,#ae2e24);">&quot;m&quot;</span><span style="color:var(--ds-text,#000000);">; }};</span><br /><span style="color:var(--ds-text,#000000);">            </span><span style="color:var(--ds-text-accent-blue,#0055cc);">in</span><span style="color:var(--ds-text,#000000);"> speed : Real = vehicle.speed / </span><span style="color:var(--ds-background-accent-green-bolder,#1f845a);">3.6</span><span style="color:var(--ds-text,#000000);"> {@ToolVariable { name = </span><span style="color:var(--ds-text-accent-red,#ae2e24);">&quot;v0&quot;</span><span style="color:var(--ds-text,#000000);">; }};</span><br /><span style="color:var(--ds-text,#000000);">            </span><span style="color:var(--ds-text-accent-blue,#0055cc);">out</span><span style="color:var(--ds-text,#000000);"> Distance : Real = vehicle.stoppingDistance {@ToolVariable { name = </span><span style="color:var(--ds-text-accent-red,#ae2e24);">&quot;stoppingDistance&quot;</span><span style="color:var(--ds-text,#000000);">; }};</span><br /><span style="color:var(--ds-text,#000000);">            </span><span style="color:var(--ds-text-accent-blue,#0055cc);">out</span><span style="color:var(--ds-text,#000000);"> kineticEnergy : Real = vehicle.kineticEnergy {@ToolVariable { name = </span><span style="color:var(--ds-text-accent-red,#ae2e24);">&quot;e&quot;</span><span style="color:var(--ds-text,#000000);">; }};</span></p></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=254423459 space=SYSML2EP version=8 -->
## PAGE 00030: (2026x) Invoking calculations

- page_id: `254423459`
- space_key: `SYSML2EP`
- source_url: https://docs.nomagic.com/spaces/SYSML2EP/pages/254423459/2026x+Invoking+calculations
- version_number: 8
- version_date: `2025-11-25T13:07:24.557+01:00`
- ancestors: Versions of SysML v2 Evaluation Plugin Documentation > (2026x) SysML v2 Evaluation Plugin Documentation > (2026x) User guide
- labels: []

### NORMALIZED CONTENT

A calculation specifies a reusable computation that returns a result in the result parameter. In addition to its parameters, a calculation may have features that are calculation or action usages, which carry out steps in the computation of the calculation result. A calculation always has a result parameter, which can be declared as an out parameter using the keyword*return*instead of*out*.

You can invoke calculation definitions and calculation usages as described below.

To invoke a calculation definition or calculation usage

1. Create and define a calculation definition or calculation usage. For instructions, refer to the SysML v2 Plugin documentation .
2. Create an invocation expression, e.g., an attribute, whose value is the result of the calculation.
3. Assign the created calculation to the invocation expression and define the calculation inputs. When defining the calculation inputs, keep in mind that they will be taken in the same order as defined in the calculation. ExamplecalcdefArea{ 
inlength:Real; 
inwidth:Real; 
returnresult:Real; 
result=length*width; 
} 
partpad{ 
attributesurfaceArea:Real=Area(centerLength, width); 
}
4. Evaluate the invocation expression (e.g., the surfaceArea attribute in the above example). For more information, see [CONFLUENCE_PAGE title='(2026x) Evaluating model elements' space=''] .

The evaluation results are displayed in the**SysML v2 Model Evaluation**console.

##### Defining calculation return in other script languages

When specifying the return of a calculation, you can use a textual representation element to evaluate scripts defined in other script languages. Supported languages include Javascript, Groovy, Beanshell, Python (Python support is based on Jython), and MATLAB.Only primitive input and output types, e.g., String, Real, Boolean, etc., are supported.

#### PANEL: Example

Example

calcdefArea15{ 
inlength:Real; 
inwidth:Real; 
returnresult:Real; 
language"beanshell"/* result=length * width */

}

#### NOTE: Using MATLAB

Using MATLAB

To evaluate scripts defined in the MATLAB syntax:

- [CONFLUENCE_PAGE title='(2026x) Integration with MATLAB' space=''] .
- The language must be specified as "MATLAB" (case sensitive).

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><span style="color:var(--ds-text,#172b4d);">A calculation specifies a reusable computation that returns a result in the result parameter. In addition to its parameters, a calculation may have features that are calculation or action usages, which carry out steps in the computation of the calculation result. A calculation always has a result parameter, which can be declared as an out parameter using the keyword<span> </span></span><em style="text-align: left;">return</em><span style="color:var(--ds-text,#172b4d);"><span> </span>instead of<span> </span></span><em style="text-align: left;">out</em><span style="color:var(--ds-text,#172b4d);">.</span></p><p>You can invoke calculation definitions and calculation usages as described below.</p><p>To invoke a calculation definition or calculation usage</p><hr /><ol><li data-uuid="505a7004-ed56-44f7-8394-ea7460a923e9">Create and define a calculation definition or calculation usage. For instructions, refer to the <a href="https://docs.nomagic.com/SYSML2P/?contextKey=calculation&amp;version=latest">SysML v2 Plugin documentation</a>.</li><li data-uuid="8c5bf97d-fa0f-48b9-b602-6ac11ea806f7">Create an invocation expression, e.g., an attribute, whose value is the result of the calculation.</li><li data-uuid="c4793d4a-9a0b-45bf-9a73-a62c21904667">Assign the created calculation to the invocation expression and define the calculation inputs.<br /><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="e811507c-c932-4f1e-b7f3-724fd61f8477"><ac:rich-text-body><p>When defining the calculation inputs, keep in mind that they will be taken in the same order as defined in the calculation.</p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="b5afa193-4f21-47eb-bec6-8cf7cb29b5ff"><ac:parameter ac:name="title">Example</ac:parameter><ac:rich-text-body><p><span style="color:var(--ds-text-accent-blue,#0055cc);">calc</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">def</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-teal,#206a83);">Area</span><span style="color:var(--ds-text,#000000);"> {</span><br /><span style="color:var(--ds-text,#000000);">            </span><span style="color:var(--ds-text-accent-blue,#0055cc);">in</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">length</span><span style="color:var(--ds-text,#000000);"> : </span><span style="color:var(--ds-text-accent-teal,#206a83);">Real</span><span style="color:var(--ds-text,#000000);">;</span><br /><span style="color:var(--ds-text,#000000);">            </span><span style="color:var(--ds-text-accent-blue,#0055cc);">in</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">width</span><span style="color:var(--ds-text,#000000);"> : </span><span style="color:var(--ds-text-accent-teal,#206a83);">Real</span><span style="color:var(--ds-text,#000000);">;</span><br /><span style="color:var(--ds-text,#000000);">            </span><span style="color:var(--ds-text-accent-blue,#0055cc);">return</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">result</span><span style="color:var(--ds-text,#000000);"> : </span><span style="color:var(--ds-text-accent-teal,#206a83);">Real</span><span style="color:var(--ds-text,#000000);">;</span><br /><span style="color:var(--ds-text,#000000);">            </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">result</span><span style="color:var(--ds-text,#000000);"> = </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">length</span><span style="color:var(--ds-text,#000000);"> * </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">width</span><span style="color:var(--ds-text,#000000);">;</span><br /><span style="color:var(--ds-text,#000000);"> }       </span><br /><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">part</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">pad</span><span style="color:var(--ds-text,#000000);"> {</span><br /><span style="color:var(--ds-text,#000000);">            </span><span style="color:var(--ds-text-accent-blue,#0055cc);">attribute</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">surfaceArea</span><span style="color:var(--ds-text,#000000);"> : </span><span style="color:var(--ds-text-accent-teal,#206a83);">Real</span><span style="color:var(--ds-text,#000000);"> = </span><span style="color:var(--ds-text-accent-teal,#206a83);">Area</span><span style="color:var(--ds-text,#000000);">(centerLength, width);</span><br /><span style="color:var(--ds-text,#000000);"> }</span></p></ac:rich-text-body></ac:structured-macro></li><li data-uuid="bd93523e-a503-49cc-b9a2-fff63c78c9cf">Evaluate the invocation expression (e.g., the <em>surfaceArea</em> attribute in the above example). For more information, see <ac:link><ri:page ri:content-title="(2026x) Evaluating model elements" /><ac:plain-text-link-body><![CDATA[Evaluating model elements]]></ac:plain-text-link-body></ac:link>.</li></ol><p><span style="color:var(--ds-text,#172b4d);">The evaluation results are displayed in the </span><strong>SysML v2 Model Evaluation</strong><span style="color:var(--ds-text,#172b4d);"><span> </span>console.</span></p><h3><span style="color:var(--ds-text,#172b4d);">Defining calculation return in other script languages</span></h3><p style="text-align: left;">When specifying the return of a calculation, you can use a <span style="color:var(--ds-text,#172b4d);">textual representation element to evaluate scripts defined in other script languages. Supported languages include Javascript, Groovy, Beanshell, Python (Python support is based on Jython), and MATLAB. </span><span>Only</span> primitive input and output types, e.g., String, Real, Boolean, etc., are supported.</p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="c0d6ec98-2f53-4b20-8d8e-4d37f62150b8"><ac:parameter ac:name="title">Example</ac:parameter><ac:rich-text-body><p><span style="color:var(--ds-text-accent-blue,#0055cc);">calc</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">def</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-teal,#206a83);">Area15</span><span style="color:var(--ds-text,#000000);"> {</span><br /><span style="color:var(--ds-text,#000000);">        </span><span style="color:var(--ds-text-accent-blue,#0055cc);">in</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">length</span><span style="color:var(--ds-text,#000000);"> : </span><span style="color:var(--ds-text-accent-teal,#206a83);">Real</span><span style="color:var(--ds-text,#000000);">;</span><br /><span style="color:var(--ds-text,#000000);">        </span><span style="color:var(--ds-text-accent-blue,#0055cc);">in</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">width</span><span style="color:var(--ds-text,#000000);"> : </span><span style="color:var(--ds-text-accent-teal,#206a83);">Real</span><span style="color:var(--ds-text,#000000);">;</span><br /><span style="color:var(--ds-text,#000000);">        </span><span style="color:var(--ds-text-accent-blue,#0055cc);">return</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">result</span><span style="color:var(--ds-text,#000000);"> : </span><span style="color:var(--ds-text-accent-teal,#206a83);">Real</span><span style="color:var(--ds-text,#000000);">;</span><br /><span style="color:var(--ds-text,#000000);">        </span><span style="color:var(--ds-text-accent-blue,#0055cc);">language</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-red,#ae2e24);">&quot;beanshell&quot;</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-green-bolder,#164b35);">/* result=length * width */</span></p><p><span style="color:var(--ds-text,#000000);">}</span></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="7112b935-00f1-4054-b9ef-71f2449b1345"><ac:parameter ac:name="title">Using MATLAB</ac:parameter><ac:rich-text-body><p>To evaluate scripts defined in the MATLAB syntax:</p><ul><li data-uuid="98e7e737-0094-43f6-ae99-0f8ba4c39dde"><ac:link><ri:page ri:content-title="(2026x) Integration with MATLAB" /><ac:plain-text-link-body><![CDATA[MATLAB must be integrated with your modeling tool]]></ac:plain-text-link-body></ac:link>.</li><li data-uuid="f312210c-f07d-490e-ad6b-89425f8b7670">The language must be specified as &quot;MATLAB&quot; (case sensitive).</li></ul></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=254423462 space=SYSML2EP version=6 -->
## PAGE 00031: (2026x) Manipulating runtime values

- page_id: `254423462`
- space_key: `SYSML2EP`
- source_url: https://docs.nomagic.com/spaces/SYSML2EP/pages/254423462/2026x+Manipulating+runtime+values
- version_number: 6
- version_date: `2026-03-25T18:30:30.605+01:00`
- ancestors: Versions of SysML v2 Evaluation Plugin Documentation > (2026x) SysML v2 Evaluation Plugin Documentation > (2026x) User guide
- labels: []

### NORMALIZED CONTENT

##### Modifying initial runtime values

You can use views to modify initial runtime values during evaluation. When an initial runtime value is changed, all evaluation results are automatically recalculated and requirements are reverified.

During runtime, you can modify only initial values indicated by the ":=" sign, which means they are not bound and can be adjusted for evaluation purposes.

To modify an initial runtime value

1. Open a view and, in the view toolbar, click [ATTACHMENT filename='evaluate_button.png'] to evaluate the view elements. To evaluate only a specific element in a view, select the element shape (press and hold the Shift key to select multiple shapes), then click [IMAGE alt='' src='']. Only the selected elements will be reevaluated after changing an initial runtime value.
2. Select an element shape and click the initial runtime value you want to change. Editable values are indicated by the ":=" sign. 
[IMAGE alt='' src='']
3. Modify the selected runtime value and click anywhere in the view to enter the change.

After an initial runtime value is changed, all bound expressions and invocations are automatically recalculated. If an expression or invocation is an initial value, it is only calculated during the first evaluation and will not be recalculated afterwards.

#### PANEL: Example

Example

attributea:=1;//'a' is an initial value that can be changed during runtime. 
attributeb=a*2;//'b' is a bound expression calculated during the initial evaluation (equals 2) and recalculated each time 'a' is changed. 
attributec:=b;//'c' is an initial expression calculated only during the initial evaluation (equals 2) and not recalculated at runtime (even if 'b' changes). However, 'c' can be changed during runtime.

##### Saving modified runtime values to the model

After using model views to modify initial runtime values, you can save the modified values to the model as described below.

You can not use model views to save modified values of inherited attributes. Only directly owned or redefined attribute values can be saved to the model.

To save all modified runtime values to the model

1. In the view with modified runtime values, do one of the following:
  - To save all modified values, click the arrow next to [ATTACHMENT filename='evaluate_button.png'] in the view toolbar and select Save Modified Values to Model . If you have selected any attribute shapes with modified values in the view, only the selected values are saved. [IMAGE alt='' src='']
  - To save selected modified values, right-click the selected attribute shapes and select Save Modified Values to Model . You can select multiple shapes by pressing and holding the **Shift** key.
  - To save a single selected modified value, click [ATTACHMENT filename='save_modified_values_to_model.png'] in the smart manipulator of the selected attribute shape. [ATTACHMENT filename='saving_single_modified_value.png']

##### Recalculating bound values manually

When an initial runtime value is changed during evaluation, all bound values are automatically recalculated, and requirements are reverified. However, this behavior can be changed by disabling the automatic bound value recalculation in the Project Options as described below.

To disable or enable bound value recalculation

1. In the main menu, go to Options > Project .
2. In the Project Options dialog, select Evaluation .
3. On the right side of the dialog, set the Auto Recalculate Bound Values option to false or true (default) to disable or enable the automatic bound value recalculation. [ATTACHMENT filename='auto_recalculate_bound_values_option.png']
4. Click OK to close the dialog.

To recalculate the evaluation results manually

- Do one of the following:
  - In the view toolbar, click [ATTACHMENT filename='evaluate_button.png'] .
  - In the view toolbar, click the arrow next to [ATTACHMENT filename='evaluate_button.png'] and select Refresh .
  - Select any shape in the view and, in the smart manipulator, click [ATTACHMENT filename='evaluate_button.png'] .
  - Right-click any shape in the view and select Evaluate .

When invoking recalculation from a specific element shape, all of the evaluation results in the view are recalculated.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<h3><span>Modifying initial runtime values</span></h3><p><span>You can use views to modify initial runtime values during evaluation. When an initial runtime value is changed, all evaluation results are automatically recalculated and requirements are reverified.</span></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="ee2a8342-af11-4191-b472-0599c88c7e22"><ac:rich-text-body><p><span> During runtime, you can modify only initial values indicated by the &quot;:=&quot; sign, which means they are not bound and can be adjusted for evaluation purposes.</span></p></ac:rich-text-body></ac:structured-macro><p>To modify an initial runtime value</p><hr /><ol><li data-uuid="2007ce79-78cb-437c-a512-5c6b984a8e4d">Open a view and, in the view toolbar, click <ac:image ac:thumbnail="true" ac:height="14"><ri:attachment ri:filename="evaluate_button.png" /></ac:image> to evaluate the view elements.<br /><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="5d95554f-2cbb-4aef-9064-73393c7c7eab"><ac:rich-text-body><p>To evaluate only a specific element in a view, select the element shape (press and hold the Shift key to select multiple shapes), then click <ac:image ac:thumbnail="true" ac:height="14"><ri:attachment ri:filename="evaluate_button.png" /></ac:image>. Only the selected elements will be reevaluated after changing an initial runtime value.</p></ac:rich-text-body></ac:structured-macro></li><li data-uuid="54d2dc4c-e893-4dfe-b1aa-401e07e605de">Select an element shape and click the initial runtime value you want to change. Editable <span>values are indicated by the &quot;:=&quot; sign.<br /><ac:image><ri:attachment ri:filename="editing_runtime_values.png" /></ac:image></span></li><li data-uuid="b52edb50-ad16-45bb-bd43-f17632b1ded3"><span>Modify the selected runtime value and click anywhere in the view to enter the change.</span></li></ol><p><span>After an initial runtime value is changed, all bound expressions and invocations are automatically recalculated. I<span style="color:var(--ds-text,#172b4d);">f an expression or invocation is an initial value, it is only calculated during the first evaluation and will not be recalculated afterwards.</span></span></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="32cf2c6b-ac6d-4788-af7e-27d09056b017"><ac:parameter ac:name="title">Example</ac:parameter><ac:rich-text-body><p><span style="color:var(--ds-text-accent-blue,#0055cc);">attribute</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">a</span><span style="color:var(--ds-text,#000000);"> := </span><span style="color:var(--ds-background-accent-green-bolder,#1f845a);">1</span><span style="color:var(--ds-text,#000000);">; </span><span style="color:var(--ds-text-accent-green-bolder,#164b35);">//'a' is an initial value that can be changed during runtime.</span><br /><span style="color:var(--ds-text-accent-blue,#0055cc);">attribute</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">b</span><span style="color:var(--ds-text,#000000);"> = </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">a</span><span style="color:var(--ds-text,#000000);"> * </span><span style="color:var(--ds-background-accent-green-bolder,#1f845a);">2</span><span style="color:var(--ds-text,#000000);">; </span><span style="color:var(--ds-text-accent-green-bolder,#164b35);">//'b' is a bound expression calculated during the initial evaluation (equals 2) and recalculated each time 'a' is changed.</span><br /><span style="color:var(--ds-text-accent-blue,#0055cc);">attribute</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">c</span><span style="color:var(--ds-text,#000000);"> := </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">b</span><span style="color:var(--ds-text,#000000);">; </span><span style="color:var(--ds-text-accent-green-bolder,#164b35);">//'c' is an initial expression calculated only during the initial evaluation (equals 2) and not recalculated at runtime (even if 'b' changes). However, 'c' can be changed during runtime.</span></p></ac:rich-text-body></ac:structured-macro><h3>Saving modified runtime values to the model</h3><p style="text-align: left;">After using model views to modify initial runtime values, you can save the modified values to the model as described below.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="84dfc085-0aca-4a85-a0dc-2d74d457ff90"><ac:rich-text-body><p><span>You can not use model views to save modified values of inherited attributes. Only directly owned or redefined attribute values can be saved to the model.</span></p></ac:rich-text-body></ac:structured-macro><p style="text-align: left;"><br /></p><p style="text-align: left;">To save all modified runtime values to the model</p><hr /><ol><li data-uuid="82b3e25c-dc54-4625-bde7-1f9d78c1ad32">In the view with modified runtime values, do one of the following:<ul><li>To save all modified values, click the arrow next to <ac:image ac:thumbnail="true" ac:height="14"><ri:attachment ri:filename="evaluate_button.png" /></ac:image> in the view toolbar and select <strong>Save Modified Values to Model</strong>.<br /><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="16fabaf7-91ff-48ac-938d-3d28a84d663c"><ac:rich-text-body><p>If you have selected any attribute shapes with modified values in the view, only the selected values are saved.</p></ac:rich-text-body></ac:structured-macro><strong><ac:image><ri:attachment ri:filename="saving_all_modified_values.png" /></ac:image></strong></li><li>To save selected modified values, right-click the selected attribute shapes and select <strong>Save Modified Values to Model</strong>.<ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="9ae9084d-e7e8-4123-858d-99d972918865"><ac:rich-text-body><p>You can select multiple shapes by pressing and holding the <strong>Shift</strong> key.</p></ac:rich-text-body></ac:structured-macro></li><li data-uuid="9bb2ceb3-6288-45d0-8d55-84c0dd5c7bcb">To save a single selected modified value, click <ac:image><ri:attachment ri:filename="save_modified_values_to_model.png" /></ac:image> in the smart manipulator of the selected attribute shape.<br /><ac:image><ri:attachment ri:filename="saving_single_modified_value.png" /></ac:image></li></ul></li></ol><h3>Recalculating bound values manually</h3><p><span style="color:var(--ds-text,#172b4d);">When an initial runtime value is changed during evaluation, all bound values are automatically recalculated, and requirements are reverified. However, this behavior can be changed by disabling the automatic bound value recalculation in the Project Options as described below.</span></p><p><span style="color:var(--ds-text,#172b4d);">To disable or enable bound value recalculation</span></p><hr /><ol><li data-uuid="e6580572-5d66-4195-8d63-c05f148fc6a4">In the main menu, go to <strong>Options</strong> &gt; <strong>Project</strong>.</li><li data-uuid="222a64e4-83ec-490f-b422-909f352312e7">In the <strong>Project Options</strong> dialog, select <strong>Evaluation</strong>.</li><li data-uuid="359333cb-6e94-45cc-90e6-de612989ce35">On the right side of the dialog, set the <strong>Auto Recalculate Bound Values</strong> option to <em>false</em> or <em>true</em> (default) to disable or enable the automatic bound value recalculation.<br /><ac:image><ri:attachment ri:filename="auto_recalculate_bound_values_option.png" /></ac:image></li><li data-uuid="4d671100-4e21-4502-aebf-b85cbbd3f00d">Click <strong>OK</strong> to close the dialog.</li></ol><p><br />To recalculate the evaluation results manually</p><hr /><ul><li data-uuid="7dec6cff-d718-403f-b824-f06125cc1c18">Do one of the following:<ul><li>In the view toolbar, click <ac:image ac:thumbnail="true" ac:height="14"><ri:attachment ri:filename="evaluate_button.png" /></ac:image>.</li><li>In the view toolbar, click the arrow next to <ac:image ac:thumbnail="true" ac:height="14"><ri:attachment ri:filename="evaluate_button.png" /></ac:image> and select <strong>Refresh</strong>.</li><li>Select any shape in the view and, in the smart manipulator, click <ac:image ac:thumbnail="true" ac:height="14"><ri:attachment ri:filename="evaluate_button.png" /></ac:image>.</li><li>Right-click any shape in the view and select <strong>Evaluate</strong>.</li></ul></li></ul><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="39d660b6-3884-4ee5-88da-bdd541a57c75"><ac:rich-text-body><p>When invoking recalculation from a specific element shape, all of the evaluation results in the view are recalculated.</p></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=254423432 space=SYSML2EP version=4 -->
## PAGE 00032: (2026x) Prerequisites

- page_id: `254423432`
- space_key: `SYSML2EP`
- source_url: https://docs.nomagic.com/spaces/SYSML2EP/pages/254423432/2026x+Prerequisites
- version_number: 4
- version_date: `2026-04-01T12:23:17.883+02:00`
- ancestors: Versions of SysML v2 Evaluation Plugin Documentation > (2026x) SysML v2 Evaluation Plugin Documentation
- labels: []

### NORMALIZED CONTENT

To work with SysML v2 features, including model evaluation, the following software must be installed:

- One of the following CATIA Magic/No Magic modeling tools:
  - Cameo Systems Modeler (Enterprise Edition only)
  - Cameo Enterprise Architecture
  - Magic Cyber Systems Engineer
  - Magic Systems of Systems Architect
- The SysML v1 Plugin.
- Cameo Requirements Modeler.
- Cameo Simulation Toolkit or Magic Model Analyst.
- The SysML v2 Plugin. It provides the majority of the SysML v2 features, including the Textual Editor.
- The SysML v2 Evaluation Plugin. It allows you to conduct static evaluations of SysML v2 models (mathematical calculations, calculation usage evaluation, constraints evaluation, and requirements evaluation).

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>To work with SysML v2 features, including model evaluation, the following software must be installed:</p><ul><li data-uuid="153c93f7-5e0b-4a8b-9c1a-cde852c497c9"><span style="color:var(--ds-text,#172b4d);">One of the following CATIA Magic/No Magic modeling tools:</span><ul><li>Cameo Systems Modeler (Enterprise Edition only)</li><li>Cameo Enterprise Architecture</li><li>Magic Cyber Systems Engineer</li><li>Magic Systems of Systems Architect</li></ul></li><li>The SysML v1 Plugin.</li><li>Cameo Requirements Modeler.</li><li>Cameo Simulation Toolkit or Magic Model Analyst.</li><li>The SysML v2 Plugin. It provides the majority of the SysML v2 features, including the Textual Editor.</li><li><p class="auto-cursor-target"><span>The SysML v2 Evaluation Plugin. It allows you to conduct static evaluations of SysML v2 models (mathematical calculations, calculation usage evaluation, constraints evaluation, and requirements evaluation).</span></p></li></ul>
````

<!--NOMAGIC_PAGE id=254423434 space=SYSML2EP version=3 -->
## PAGE 00033: (2026x) Samples and libraries

- page_id: `254423434`
- space_key: `SYSML2EP`
- source_url: https://docs.nomagic.com/spaces/SYSML2EP/pages/254423434/2026x+Samples+and+libraries
- version_number: 3
- version_date: `2026-05-06T10:24:51.117+02:00`
- ancestors: Versions of SysML v2 Evaluation Plugin Documentation > (2026x) SysML v2 Evaluation Plugin Documentation
- labels: []

### NORMALIZED CONTENT

##### Samples

You can also review the SysML v2 project samples provided with the installation, found at:

- <modeling tool installation directory>\samples\SysML v2\Evaluation

##### Libraries

Each SysML v2 project is automatically loaded with used projects:

- Standard Libraries. It contains standard SysML v2 libraries.
- 3DS SysML Customization. It contains concepts designed for view creation and symbol styles customization.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<h3>Samples</h3><p>You can also review the SysML v2 project samples provided with the installation, found at:</p><ul><li><em style="text-align: left;">&lt;modeling tool installation directory&gt;\samples\SysML v2\Evaluation</em><em style="text-align: left;"><br /></em></li></ul><h3>Libraries</h3><p>Each SysML v2 project is automatically loaded with used projects:</p><ul><li><em>Standard Libraries.</em> It contains standard SysML v2 libraries.</li><li><em>3DS SysML Customization. </em>It contains concepts designed for view creation and symbol styles customization.<em><br /></em></li></ul>
````

<!--NOMAGIC_PAGE id=254423499 space=SYSML2EP version=2 -->
## PAGE 00034: (2026x) Server-side evaluation

- page_id: `254423499`
- space_key: `SYSML2EP`
- source_url: https://docs.nomagic.com/spaces/SYSML2EP/pages/254423499/2026x+Server-side+evaluation
- version_number: 2
- version_date: `2026-01-26T10:53:19.191+01:00`
- ancestors: Versions of SysML v2 Evaluation Plugin Documentation > (2026x) SysML v2 Evaluation Plugin Documentation > (2026x) User guide
- labels: []

### NORMALIZED CONTENT

If you work with Teamwork Cloud projects, you can evaluate them on the server byusing the REST API or thePython client (pyEval.zip).

Server-side evaluation is available only with the Teamwork Cloud Enterprise license.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>If you work with Teamwork Cloud projects, you can evaluate them on the server by<span style="letter-spacing: 0.0px;"> using the REST API or the</span><span style="letter-spacing: 0.0px;"> Python client (<ac:inline-comment-marker ac:ref="24822121-cd71-4013-9b75-cf4d77db78fe"><span style="color:var(--ds-text,#172b4d);">pyEval.zip</span></ac:inline-comment-marker>).</span></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="4b2f9a88-7b0e-4a14-9e82-9407715c4e80"><ac:rich-text-body><p>Server-side evaluation is available only with the Teamwork Cloud Enterprise license.</p></ac:rich-text-body></ac:structured-macro><p><span style="color:var(--ds-text,#172b4d);"><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="8a64d399-3fd0-4bfd-9138-4a6175057396" /></span></p>
````

<!--NOMAGIC_PAGE id=254423430 space=SYSML2EP version=4 -->
## PAGE 00035: (2026x) SysML v2 Evaluation Plugin Documentation

- page_id: `254423430`
- space_key: `SYSML2EP`
- source_url: https://docs.nomagic.com/spaces/SYSML2EP/pages/254423430/2026x+SysML+v2+Evaluation+Plugin+Documentation
- version_number: 4
- version_date: `2026-06-16T09:20:03.707+02:00`
- ancestors: Versions of SysML v2 Evaluation Plugin Documentation
- labels: []

### NORMALIZED CONTENT

lightgrey

This guide provides documentation for the SysML v2 Evaluation Plugin.

SysML v2 is a next-generation systems modeling language. Compared to SysML v1, SysML v2 aims to offer improved precision, expressiveness, and usability.

To fully take advantage of SysML v2, two primary plugins are available for you:

- The SysML v2 Plugin provides core SysML v2 features and includes the SysML v2 Textual Editor, enabling you to model using both textual and graphical notations.
- The SysML v2 Evaluation Plugin allows you to conduct static evaluations of SysML v2 models.

For more information, please see the [CONFLUENCE_PAGE title='(2026x) Prerequisites' space=''] page.

The following topics explain how to install and use the SysML v2 Evaluation Plugin:

2

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="10aa203c-7173-4219-ab58-f6619359c634"><ac:parameter ac:name="bgColor">lightgrey</ac:parameter><ac:rich-text-body><p><span style="color:var(--ds-text,#172b4d);">This guide provides documentation for the SysML v2 Evaluation Plugin.</span></p></ac:rich-text-body></ac:structured-macro><p>SysML v2 is a next-generation systems modeling language. Compared to SysML v1, SysML v2 aims to offer improved precision, expressiveness, and usability.</p><p>To fully take advantage of SysML v2, two primary plugins are available for you:</p><ul><li><a href="https://docs.nomagic.com/SYSML2P/?contextKey=sysml-v2-plugin-documentation&amp;version=2026x">The SysML v2 Plugin</a> provides core SysML v2 features and includes the SysML v2 Textual Editor, enabling you to model using both textual and graphical notations.</li><li>The SysML v2 Evaluation Plugin allows you to conduct static evaluations of SysML v2 models.</li></ul><p>For more information, please see the <ac:link><ri:page ri:content-title="(2026x) Prerequisites" /><ac:plain-text-link-body><![CDATA[Prerequisites]]></ac:plain-text-link-body></ac:link> page.</p><p>The following topics explain how to install and use the SysML v2 Evaluation Plugin:</p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="84f0fb89-da08-4a91-ab07-5ab77e498633"><ac:parameter ac:name="depth">2</ac:parameter></ac:structured-macro></p><p><br /></p>
````

<!--NOMAGIC_PAGE id=254423436 space=SYSML2EP version=4 -->
## PAGE 00036: (2026x) User guide

- page_id: `254423436`
- space_key: `SYSML2EP`
- source_url: https://docs.nomagic.com/spaces/SYSML2EP/pages/254423436/2026x+User+guide
- version_number: 4
- version_date: `2026-04-01T12:40:41.838+02:00`
- ancestors: Versions of SysML v2 Evaluation Plugin Documentation > (2026x) SysML v2 Evaluation Plugin Documentation
- labels: []

### NORMALIZED CONTENT

The SysML v2 Evaluation Plugin user guide explains how to conduct static evaluations of SysML v2 models.

For information about generic SysML v2 modeling features, including using the textual notation, see the [SysML v2 Plugin documentation](https://docs.nomagic.com/SYSML2P/?contextKey=sysml-v2-plugin-documentation&version=2026x).

To learn more, see the following topics:

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>The SysML v2 Evaluation Plugin user guide explains how to conduct static evaluations of SysML v2 models.</p><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="f0f8e034-bdef-4bad-9db3-36961de8057f"><ac:rich-text-body><p>For information about generic SysML v2 modeling features, including using the textual notation, see the <a href="https://docs.nomagic.com/SYSML2P/?contextKey=sysml-v2-plugin-documentation&amp;version=2026x">SysML v2 Plugin documentation</a>.</p></ac:rich-text-body></ac:structured-macro><p> To learn more, see the following topics:</p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="1d052ab0-6a12-44f2-a374-967d5273613b" /></p>
````

<!--NOMAGIC_PAGE id=286097419 space=SYSML2EP version=2 -->
## PAGE 00037: (2026x) Using interactive HTML table

- page_id: `286097419`
- space_key: `SYSML2EP`
- source_url: https://docs.nomagic.com/spaces/SYSML2EP/pages/286097419/2026x+Using+interactive+HTML+table
- version_number: 2
- version_date: `2026-01-19T09:20:11.365+01:00`
- ancestors: Versions of SysML v2 Evaluation Plugin Documentation > (2026x) SysML v2 Evaluation Plugin Documentation > (2026x) User guide > (2026x) Server-side evaluation
- labels: []

### NORMALIZED CONTENT

You can use [CONFLUENCE_PAGE title='Evaluation using REST API' space=''] or [CONFLUENCE_PAGE title='Evaluation using Jupyter Notebook' space=''] to open and modify an interactive HTML table that dynamically retrieves data based on the specified context, parameters, and/or expressions.

[IMAGE alt='' src='']

###### An interactive HTML table

##### Editing values

In an HTML table, you can edit initial values, as described below.

- Only initial values can be edited.
- Non-editable values are shown in italic font for easier identification.

To edit initial values

1. Click the Value cell you want to edit.
2. Change the value.
3. Click anywhere on the table page to save the value.

##### Adding new rows

To add a new table row

1. In the top right corner of the table page, click [ATTACHMENT filename='add_row.png'] to add a new row at the bottom of the table.
2. Click the Name and Value cells of the new row and enter the desired property name and value.

##### Reordering rows

To change the position of a table row

1. Hover the mouse pointer over a table row to see available action icons.
2. Click and hold [ATTACHMENT filename='drag_to_reorder.png'] .
3. Drag and drop the row to a new position. [ATTACHMENT filename='reordering_rows.png']

##### Deleting rows

To delete a table row

1. Hover the mouse pointer over a table row to see available action icons.
2. Click [ATTACHMENT filename='delete_row.png'] to delete the row.

##### Exporting data

You can export HTML table data to the PNG, CSV, and JSON formats.

To export table data

- In the top right corner of the table page, click [ATTACHMENT filename='export_table.png'] and select the format you want to export to.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><span style="color:var(--ds-text,#172b4d);">You can use <ac:link><ri:page ri:content-title="Evaluation using REST API" /><ac:plain-text-link-body><![CDATA[REST API]]></ac:plain-text-link-body></ac:link> or <ac:link><ri:page ri:content-title="Evaluation using Jupyter Notebook" /><ac:plain-text-link-body><![CDATA[Jupyter Notebook]]></ac:plain-text-link-body></ac:link> to open and modify an interactive HTML table that dynamically retrieves data based on the specified context, parameters, and/or expressions.</span></p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="interactive_html_table.png" /></ac:image></p><h6 style="text-align: center;">An interactive HTML table</h6><h3>Editing values</h3><p>In an HTML table, you can edit initial values, as described below.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="76aefc83-3d0f-4ae0-bbe6-162cecceff80"><ac:rich-text-body><ul><li data-uuid="ca56cbae-a2c6-49a4-a951-0ef751c67482">Only initial values can be edited.</li><li data-uuid="5b1e874e-9fbf-4ef8-9f9c-0e3a0c93c4d0">Non-editable values are shown in italic font for easier identification.</li></ul></ac:rich-text-body></ac:structured-macro><p>To edit initial values</p><hr /><ol><li data-uuid="2ea41a37-2bfb-4b11-b578-c67f0f88e8a4">Click the <strong>Value</strong> cell you want to edit.</li><li data-uuid="65d38620-9b60-402c-b8d6-420fff571066">Change the value.</li><li data-uuid="2cd1e1c1-8b20-4169-8de7-a9f28c64950b">Click anywhere on the table page to save the value.</li></ol><h3>Adding new rows</h3><p>To add a new table row</p><hr /><ol><li data-uuid="c936246a-3d08-41d4-b2f6-7194e2826d9c">In the top right corner of the table page, click <ac:image><ri:attachment ri:filename="add_row.png" /></ac:image> to add a new row at the bottom of the table.</li><li data-uuid="559cef5d-7f41-4bfa-9664-0be5ff3f0668">Click the <strong>Name</strong> and <strong>Value</strong> cells of the new row and enter the desired property name and value.</li></ol><h3>Reordering rows</h3><p>To change the position of a table row</p><hr /><ol><li data-uuid="5468d510-837e-4c9c-bfb8-23c6491ee34f">Hover the mouse pointer over a table row to see available action icons.</li><li data-uuid="69c81157-5a1c-4607-ad0f-c45903a9a714">Click and hold <ac:image><ri:attachment ri:filename="drag_to_reorder.png" /></ac:image>.</li><li data-uuid="2a26e1e2-a6ed-427d-8a5e-906fa4efce57">Drag and drop the row to a new position.<br /><ac:image><ri:attachment ri:filename="reordering_rows.png" /></ac:image></li></ol><h3>Deleting rows</h3><p>To delete a table row</p><hr /><ol><li data-uuid="69049473-a60c-4b0d-b5e2-2c225ae4c45e">Hover the mouse pointer over a table row to see available action icons.</li><li data-uuid="23f04ada-7943-4654-ba09-12119b274af1">Click <ac:image ac:thumbnail="true" ac:height="14"><ri:attachment ri:filename="delete_row.png" /></ac:image> to delete the row.</li></ol><h3>Exporting data</h3><p>You can export HTML table data to the PNG, CSV, and JSON formats.</p><p>To export table data</p><hr /><ul><li data-uuid="728ffb95-3107-4839-b29c-93d5577c60b0">In the top right corner of the table page, click <ac:image ac:thumbnail="true" ac:height="22"><ri:attachment ri:filename="export_table.png" /></ac:image> and select the format you want to export to.</li></ul>
````

<!--NOMAGIC_PAGE id=286557445 space=SYSML2EP version=11 -->
## PAGE 00038: Clearing runtime values

- page_id: `286557445`
- space_key: `SYSML2EP`
- source_url: https://docs.nomagic.com/spaces/SYSML2EP/pages/286557445/Clearing+runtime+values
- version_number: 11
- version_date: `2026-01-30T18:42:35.327+01:00`
- ancestors: SysML v2 Evaluation Plugin Documentation > User guide
- labels: []

### NORMALIZED CONTENT

After [CONFLUENCE_PAGE title='Evaluating model elements' space=''], the runtime values are stored in memory and reused for further evaluations, as shown in the example below.

#### PANEL: Example

Example

attributemyNumber:Real= randomNumberGen();//The script that returns a random number is envoked. 
attributemyNewNumber:Real=myNumber+5;//The generated number is reused. Using the myNumber attribute will not trigger the generation of a new number.

The runtime values stored in memory are cleared when you do the following:

- Modify the model.
- Clear values using the view toolbar.
- Clear values using the SysML v2 Model Evaluation console.

##### Clearing values via the view toolbar

If you evaluated model elements using views, you can use the view toolbar to clear the runtime values.

To clear runtime values via the view toolbar

- In the view toolbar, click the arrow next to [ATTACHMENT filename='evaluate_button.png'] and select Clear Values . [ATTACHMENT filename='clearing_values_via_diagram_toolbar.png']

##### Clearing values via the SysML v2 Model Evaluation console

You can use the **SysML v2 Model Evaluation** console to clear runtime values, regardless of where you initiated model evaluation.

To clear runtime values via the **SysML v2 Model Evaluation** console

- In the SysML v2 Model Evaluation console toolbar, click [ATTACHMENT filename='clear_values_icon.png'] . [ATTACHMENT filename='clearing_values_via_console.png']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p style="text-align: left;">After <ac:link><ri:page ri:content-title="Evaluating model elements" /><ac:plain-text-link-body><![CDATA[model evaluation]]></ac:plain-text-link-body></ac:link>, the runtime values are stored in memory and reused for further evaluations, as shown in the example below.</p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="ef3e74a2-bf68-44a4-b050-97a1a91a7464"><ac:parameter ac:name="title">Example</ac:parameter><ac:rich-text-body><p><span style="color:var(--ds-text-accent-blue,#0055cc);">attribute</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">myNumber</span><span style="color:var(--ds-text,#000000);"> : </span><span style="color:var(--ds-text-accent-teal,#206a83);">Real</span><span style="color:var(--ds-text,#000000);"> = randomNumberGen(); </span><span style="color:var(--ds-text-accent-green-bolder,#164b35);">//The script that returns a random number is envoked.</span><br /><span style="color:var(--ds-text-accent-blue,#0055cc);">attribute</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">myNewNumber</span><span style="color:var(--ds-text,#000000);"> : </span><span style="color:var(--ds-text-accent-teal,#206a83);">Real</span><span style="color:var(--ds-text,#000000);"> = </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">myNumber</span><span style="color:var(--ds-text,#000000);"> + </span><span style="color:var(--ds-background-accent-green-bolder,#1f845a);">5</span><span style="color:var(--ds-text,#000000);">; </span><span style="color:var(--ds-text-accent-green-bolder,#164b35);">//The generated number is reused. Using the myNumber attribute will not trigger the generation of a new number.</span></p></ac:rich-text-body></ac:structured-macro><p class="code-java"><br />The runtime values stored in memory are cleared when you do the following:</p><ul style="text-align: left;"><li data-uuid="8ff056d2-95cb-44f0-9a0a-054b56c03b03">Modify the model.</li><li data-uuid="35f61a9c-55da-4192-baed-52651842ac88">Clear values using the view toolbar.</li><li data-uuid="44eaa21a-8137-4733-8643-06d60ec5967d">Clear values using the <strong>SysML v2 Model Evaluation</strong> console.</li></ul><h3 style="text-align: left;">Clearing values via the view toolbar</h3><p>If you evaluated model elements using views, you can use the view toolbar to clear the runtime values.</p><p>To clear runtime values via the view toolbar</p><hr /><ul><li data-uuid="1da4ccf3-9a89-40cb-98ec-3f418f12e353">In the view toolbar, click the arrow next to <ac:image ac:thumbnail="true" ac:height="14"><ri:attachment ri:filename="evaluate_button.png" /></ac:image> and select <strong>Clear Values</strong>.<br /><ac:image><ri:attachment ri:filename="clearing_values_via_diagram_toolbar.png" /></ac:image></li></ul><h3>Clearing values via the SysML v2 Model Evaluation console</h3><p>You can use the <strong>SysML v2 Model Evaluation</strong> console to clear runtime values, regardless of where you initiated model evaluation.</p><p>To clear runtime values via the <strong>SysML v2 Model Evaluation</strong> console</p><hr /><ul><li data-uuid="f13a5e93-689f-49ba-b2e7-8d8b074746c7">In the <strong>SysML v2 Model Evaluation</strong> console toolbar, click <ac:image><ri:attachment ri:filename="clear_values_icon.png" /></ac:image>.<br /><ac:image><ri:attachment ri:filename="clearing_values_via_console.png" /></ac:image></li></ul>
````

<!--NOMAGIC_PAGE id=249578001 space=SYSML2EP version=1 -->
## PAGE 00039: Connecting to a running MATLAB session

- page_id: `249578001`
- space_key: `SYSML2EP`
- source_url: https://docs.nomagic.com/spaces/SYSML2EP/pages/249578001/Connecting+to+a+running+MATLAB+session
- version_number: 1
- version_date: `2025-04-15T10:51:24.386+02:00`
- ancestors: SysML v2 Evaluation Plugin Documentation > User guide > Integration with MATLAB
- labels: ['connecting-to-matlab-session', 'matlab-session']

### NORMALIZED CONTENT

You can connect to a running MATLAB session and use all the variables in the MATLAB workspace.

To connect to a MATLAB session, [CONFLUENCE_PAGE title='Integration with MATLAB' space='SYSML2EP'].

To connect a running MATLAB session

- In the MATLAB command widow, execute the matlab.engine.shareEngine command.

After connecting to a MATLAB session, you can access variables in the MATLAB shared workspace that are not in the SysML v2 model. For example, you can define variables in MATLAB and then use them in calculations in your modeling tool.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>You can connect to a running MATLAB session and use all the variables in the MATLAB workspace.</p><ac:structured-macro ac:macro-id="65f34d32-45d5-43ef-97f4-8ea16e7b1763" ac:name="note" ac:schema-version="1"><ac:rich-text-body><p>To connect to a MATLAB session, <ac:link><ri:page ri:space-key="SYSML2EP" ri:content-title="Integration with MATLAB" /><ac:plain-text-link-body><![CDATA[MATLAB must be integrated with your modeling tool]]></ac:plain-text-link-body></ac:link>.</p></ac:rich-text-body></ac:structured-macro><p><br /></p><p>To connect <ac:inline-comment-marker ac:ref="c56add26-f5b3-46fc-8fb4-6eef404f8496">a running MATLAB session</ac:inline-comment-marker></p><hr /><ul><li>In the MATLAB command widow, execute the <strong>matlab.engine.shareEngine</strong> command.</li></ul><p class="auto-cursor-target"><br />After connecting to a MATLAB session, you can access variables in the MATLAB shared workspace that are not in the SysML v2 model. For example, you can define variables in MATLAB and then use them in calculations in your modeling tool.</p>
````

<!--NOMAGIC_PAGE id=312247610 space=SYSML2EP version=17 -->
## PAGE 00040: Displaying evaluation information

- page_id: `312247610`
- space_key: `SYSML2EP`
- source_url: https://docs.nomagic.com/spaces/SYSML2EP/pages/312247610/Displaying+evaluation+information
- version_number: 17
- version_date: `2026-06-17T09:12:41.550+02:00`
- ancestors: SysML v2 Evaluation Plugin Documentation > User guide > Evaluation information in views
- labels: []

### NORMALIZED CONTENT

##### Displaying runtime values

In views, runtime values are displayed in blue. After evaluation, these runtime values replace the default values and are displayed next to:

- Attributes
- References
- Satisfy requirements

Attributes or references that contain expressions may display calculated values. During the evaluation, views do not display types; only the current runtime values are shown. This reduces visual complexity and improves view readability.

#### INFO: Displaying unit symbols

Displaying unit symbols

When units are assigned directly to literal values, unit symbols are displayed next to runtime values in model views during evaluation. You can assign units using square brackets on literals. For example:

attribute'Mass : MassValue'default:=500[SI::kg];

You can also[CONFLUENCE_PAGE title='Manipulating runtime values' space='']directly in views and watch as the evaluation results are automatically recalculated.

[IMAGE alt='' src='']

###### A sample view displaying the evaluation results.

INLINE

##### Annotating requirement and constraint verification results

Using views is the quickest way to evaluate multiple requirements and constraints at once. After evaluation, passing and failing values are highlighted in green and red, respectively. In addition, element shapes display specific icons to indicate whether the related requirements and constraints are satisfied.

To evaluate requirements and constraints in views

1. Open the view that displays elements with related requirements and constraints that you want to evaluate.
2. Click [ATTACHMENT filename='evaluate_button.png'] in the view toolbar. To evaluate a single element, select the element shape or an attribute in the shape compartment before completing this step.To evaluate an individual satisfy requirement or assert constraint, select the element shape before completing this step. The evaluation result is *true* or *false*.

The view shapes are highlighted, indicating whether related system requirements and constraints pass or fail.

[IMAGE alt='' src='']

###### A view with annotated requirement verification results. Hovering over a failing value shows the text of the failing requirement.

The following table explains the annotations of requirement and constraint verification results displayed in views.

| Annotation | Description | Tooltip |
| --- | --- | --- |
| ORA shape or its header is colored in green | The annotated elements satisfy related system requirements or constraints. | N/A |
| ORA shape or its header is colored in yellow | The annotated elements indirectly fail related system requirements or constraints. This means that system requirements or constraints are failed by inner parts of the annotated element. | Hover over the icon to see which inner elements fail system requirements or constraints. |
| ORA shape or its header is colored in red | The annotated elements fail related system requirements or constraints. | Hover over the icon to see which requirement or constraint failed. |
|  | The annotated values satisfy related system requirements or constraints. | N/A |
|  | The annotated values fail related system requirements or constraints. | Hover over the value to see the text of the failing requirement. |

###### Customizing the visual representation of verification results

You can customize how requirement and constraint verification results are annotated in views.

To customize the visual representation of the requirement and constraint verification results

1. In the main menu, select Options > Project .
2. In the Project Options dialog, select the Evaluation option group.
3. Specify the following options:
  - Display Verification Results As - Select Display Icons to add icons to shape headers. Select Paint Headers to color shapes or their headers.
  - Propagate Deep Nested Failures - Set to true to indicate nested requirement and constraint failures. Set to false to only highlight the shapes of the elements that directly fail a requirement or constraint.
4. Click OK to close the Project Options dialog.

##### Clearing evaluation results in views

To clear the evaluation results in a view

- In the view toolbar, click an arrow next to [ATTACHMENT filename='evaluate_button.png'] and select Clear Values .

### EXACT CONFLUENCE STORAGE SOURCE

````html
<h3>Displaying runtime values</h3><p style="text-align: left;">In views, runtime values are displayed in blue. After evaluation, these runtime values replace the default values and are displayed next to:</p><ul style="text-align: left;"><li data-uuid="4df9462d-449b-4473-9a1b-66492d2ca634">Attributes</li><li data-uuid="d0c763c8-e720-48d1-832e-627bbb4ba482">References</li><li data-uuid="8bb78bb9-aa0a-4c52-975c-ffb72ab9fdcf">Satisfy requirements</li></ul><p style="text-align: left;">Attributes or references that contain expressions may display calculated values. During the evaluation, views do not display types; only the current runtime values are shown. This reduces visual complexity and improves view readability.</p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="0e991bdb-4fad-4bd9-8d67-a5d3953a41f6"><ac:parameter ac:name="title">Displaying unit symbols</ac:parameter><ac:rich-text-body><p>When units are assigned directly to literal values, unit symbols are displayed next to runtime values in model views during evaluation. You can assign units using square brackets on literals. For example: </p><p><span style="color:var(--ds-text-accent-blue,#0055cc);">attribute</span><span style="color:var(--ds-chart-gray-bold,#8590a2);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">'Mass : MassValue'</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">default</span><span style="color:var(--ds-text,#000000);"> := </span><span style="color:var(--ds-background-accent-green-bolder,#1f845a);">500</span><span style="color:var(--ds-text,#000000);"> [</span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">SI::kg</span><span style="color:var(--ds-text,#000000);">];</span></p></ac:rich-text-body></ac:structured-macro><p style="text-align: left;">You can also<span> </span><ac:link><ri:page ri:content-title="Manipulating runtime values" /><ac:plain-text-link-body><![CDATA[modify runtime values]]></ac:plain-text-link-body></ac:link><span> </span>directly in views and watch as the <span style="color:var(--ds-text,#172b4d);">evaluation results are automatically recalculated.</span></p><p style="text-align: center;"><span style="color:var(--ds-text,#172b4d);"><ac:image><ri:attachment ri:filename="displaying_runtime_values.png" /></ac:image></span></p><h6 style="text-align: center;"><span style="color:var(--ds-text,#172b4d);">A sample view displaying the evaluation results.</span></h6><ac:structured-macro ac:name="excerpt" ac:schema-version="1" ac:macro-id="14743066-60a6-4d47-833f-6af76e90a237"><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><h3>Annotating requirement and constraint verification results</h3><p>Using views is the quickest way to evaluate multiple requirements and constraints at once. After evaluation, passing and failing values are highlighted in green and red, respectively. In addition, element shapes display specific icons to indicate whether the related requirements and constraints are satisfied.</p><p>To evaluate requirements and constraints in views</p><hr /><ol><li data-uuid="2667b850-9769-42c4-9c9f-d65e35f824aa">Open the view that displays elements with related requirements and constraints that you want to evaluate.</li><li data-uuid="df6ad6d0-d8af-412a-b3e3-e6ac3505c879">Click <ac:image><ri:attachment ri:filename="evaluate_button.png" /></ac:image> in the view toolbar.<br /><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="b4760594-9edc-4ee3-bfd1-320da5a6483f"><ac:rich-text-body><ul><li>To evaluate a single element, select the element shape or an attribute in the shape compartment before completing this step.</li><li>To evaluate an individual satisfy requirement or assert constraint, select the element shape before completing this step. The evaluation result is <em>true</em> or <em>false</em>.</li></ul></ac:rich-text-body></ac:structured-macro></li></ol><p>The view shapes are highlighted, indicating whether related system requirements and constraints pass or fail.</p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="requirement_and_constraint_verification.png" /></ac:image></p><h6 style="text-align: center;">A view with annotated requirement verification results. Hovering over a failing value shows the text of the failing requirement.</h6><p>The following table explains the annotations of requirement and constraint verification results displayed in views.</p><table class="relative-table wrapped" style="width: 85.0804%;"><colgroup><col style="width: 19.8294%;" /><col style="width: 49.12%;" /><col style="width: 31.0506%;" /></colgroup><tbody><tr><th style="text-align: left;">Annotation</th><th>Description</th><th>Tooltip</th></tr><tr><td style="text-align: center;"><div class="content-wrapper"><p><ac:image><ri:attachment ri:filename="pass.png" /></ac:image></p><p>OR</p><p>A shape or its header is colored in green</p></div></td><td>The annotated elements satisfy related system requirements or constraints.</td><td>N/A</td></tr><tr><td style="text-align: center;"><div class="content-wrapper"><p><ac:image><ri:attachment ri:filename="indirect_failure.png" /></ac:image></p><p>OR</p><p>A shape or its header is colored in yellow</p></div></td><td>The annotated elements indirectly fail related system requirements or constraints. This means that system requirements or constraints are failed by inner parts of the annotated element. </td><td>Hover over the icon to see which inner elements fail system requirements or constraints.</td></tr><tr><td style="text-align: center;"><div class="content-wrapper"><p><ac:image><ri:attachment ri:filename="direct_failure.png" /></ac:image></p><p>OR</p><p>A shape or its header is colored in red</p></div></td><td>The annotated elements fail related system requirements or constraints.</td><td>Hover over the icon to see which requirement or constraint failed.</td></tr><tr><td style="text-align: center;"><div class="content-wrapper"><p><ac:image><ri:attachment ri:filename="passing_value.png" /></ac:image></p></div></td><td>The annotated values satisfy related system requirements or constraints.</td><td>N/A</td></tr><tr><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:height="20"><ri:attachment ri:filename="failing_value.png" /></ac:image></p></div></td><td>The annotated values fail related system requirements or constraints.</td><td>Hover over the value to see the text of the failing requirement.</td></tr></tbody></table><h4>Customizing the visual representation of verification results </h4><p><span style="color:var(--ds-text,#172b4d);">You can customize how requirement and constraint verification results are annotated in views.</span></p><p><span style="color:var(--ds-text,#172b4d);">To customize the visual representation of the requirement and constraint verification results</span></p><hr /><ol><li data-uuid="b8d0e243-e5b7-40c0-92ea-cdfe6a4f2283">In the main menu, select <strong>Options</strong> &gt; <strong>Project</strong>.</li><li data-uuid="be670141-33fb-4afe-b4fc-91ea634a6b86">In the <strong>Project Options</strong> dialog, select the <strong>Evaluation</strong> option group.</li><li data-uuid="812485dc-9625-4c7d-99bb-ab108d950f8b">Specify the following options:<ul><li><strong>Display Verification Results As</strong> - Select <strong>Display Icons</strong> to add icons to shape headers. Select <strong>Paint Headers</strong> to color shapes or their headers.</li><li><strong>Propagate Deep Nested Failures</strong> - Set to <em>true</em> to indicate nested requirement and constraint failures. Set to <em>false</em> to only highlight the shapes of the elements that directly fail a requirement or constraint.</li></ul></li><li data-uuid="c32e7d0b-dfbc-4f73-9d14-2fc31c0c1afe">Click <strong>OK</strong> to close the <strong>Project Options</strong> dialog.</li></ol><h3>Clearing evaluation results in views</h3><p>To clear the evaluation results in a view</p><hr /><ul><li data-uuid="ffcc042c-cd58-482b-a79b-9069e9242dce">In the view toolbar, click an arrow next to <ac:image><ri:attachment ri:filename="evaluate_button.png" /></ac:image> and select <strong>Clear Values</strong>.</li></ul></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=249577941 space=SYSML2EP version=20 -->
## PAGE 00041: Evaluating model elements

- page_id: `249577941`
- space_key: `SYSML2EP`
- source_url: https://docs.nomagic.com/spaces/SYSML2EP/pages/249577941/Evaluating+model+elements
- version_number: 20
- version_date: `2026-06-17T10:33:13.010+02:00`
- ancestors: SysML v2 Evaluation Plugin Documentation > User guide
- labels: []

### NORMALIZED CONTENT

This chapter describes how you can evaluate model elements, e.g., attributes, expressed through general mathematical calculations. When you evaluate a model element, all of its owned and inherited attributes are evaluated as well.

##### Evaluating model elements via the textual notation

To evaluate a model element via the textual notation

1. In the Textual Editor, place the cursor on the element you want to evaluate.
2. In the Textual Editor toolbar, click [ATTACHMENT filename='evaluate_button.png'] . [ATTACHMENT filename='evaluating_element_via_textual_notation.png']

The evaluation results are displayed in the **SysML v2 Model Evaluation** console.

##### Evaluating model elements via the Containment tree

To evaluate a model element via the Containment tree

- Right-click an element in the Containment tree and select Evaluate . [ATTACHMENT filename='evaluating_element_via_containment_tree.png']

The evaluation results are displayed in the **SysML v2 Model Evaluation** console.

##### Evaluating model elements in views

You can use views to evaluate individual model elements or all the elements displayed in a view.

To evaluate a model element in a view

1. Open the view displaying the model elements you want to evaluate.
2. Do one of the following:
  - Select the shapes of the elements you want to evaluate and, in the view toolbar, click [ATTACHMENT filename='evaluate_button.png'] . If you do not select any shapes, all the elements displayed in the view are evaluated. [ATTACHMENT filename='evaluating_from_view_toolbar.png']
  - Right-click an element shape and select Evaluate .
  - Select an element shape and, in the smart manipulator, click [ATTACHMENT filename='evaluate_button.png'] . [ATTACHMENT filename='evaluating_from_smart_manipulator.png']

After evaluation, runtime values are displayed in blue next to attributes, references, and satisfy requirements in a view. In addition, the values that pass or fail requirements and constraints are highlighted in green and red, respectively. To learn more, see [CONFLUENCE_PAGE title='Displaying evaluation information' space=''].

##### Evaluating elements via the SysML v2 Model Evaluation console

You can evaluate model elements by writing an expression directly in the **SysML v2 Model Evaluation** console. However, you need to call the element you want to evaluate directly, because the console will not display the evaluation results of the owned and inherited elements.

To evaluate an element via the **SysML v2 Model Evaluation** console

1. Select Window > SysML v2 Model Evaluation to open the SysML v2 Model Evaluation console.
2. In the input box of the console, type the qualified name of the element you want to evaluate and press Enter. To save time, click [IMAGE alt='' src=''] in the toolbar of the **SysML v2 Model Evaluation** console to enable context selection in the Containment tree. When context selection is enabled, select the owner of the element you want to evaluate and enter only the element's name to evaluate it. [ATTACHMENT filename='evaluating_attribute_in_console.png']

The evaluation results are displayed in the **SysML v2 Model Evaluation**console as shown in the above figure.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>This chapter describes how you can evaluate model elements, e.g., attributes, expressed through general mathematical calculations. When you evaluate a model element, all of its owned and inherited attributes are evaluated as well.</p><h3>Evaluating model elements via the textual notation</h3><p>To evaluate a model element via the textual notation</p><hr /><ol><li>In the Textual Editor, place the cursor on the element you want to evaluate.</li><li>In the Textual Editor toolbar, click <ac:image><ri:attachment ri:filename="evaluate_button.png" /></ac:image>.<br /><ac:image><ri:attachment ri:filename="evaluating_element_via_textual_notation.png" /></ac:image></li></ol><p>The evaluation results are displayed in the <strong>SysML v2 Model Evaluation</strong> console.</p><h3>Evaluating model elements via the Containment tree</h3><p>To evaluate a model element via the Containment tree</p><hr /><ul><li>Right-click an element in the Containment tree and select <strong>Evaluate</strong>.<br /><ac:image><ri:attachment ri:filename="evaluating_element_via_containment_tree.png" /></ac:image></li></ul><p>The evaluation results are displayed in the <strong>SysML v2 Model Evaluation</strong> console.</p><h3>Evaluating model elements in views</h3><p>You can use views to evaluate individual model elements or all the elements displayed in a view. </p><p>To evaluate a model element in a view</p><hr /><ol><li>Open the view displaying the model elements you want to evaluate.</li><li>Do one of the following:<ul><li>Select the shapes of the elements you want to evaluate and, in the view toolbar, click <ac:image><ri:attachment ri:filename="evaluate_button.png" /></ac:image>.<br /><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="6c510c2a-2148-496b-8784-b03a349ebdf2"><ac:rich-text-body><p>If you do not select any shapes, all the elements displayed in the view are evaluated.</p></ac:rich-text-body></ac:structured-macro><ac:image><ri:attachment ri:filename="evaluating_from_view_toolbar.png" /></ac:image></li><li data-uuid="c662988c-e701-447c-a027-58c4886067c6">Right-click an element shape and select <strong>Evaluate</strong>.</li><li>Select an element shape and, in the smart manipulator, click <ac:image><ri:attachment ri:filename="evaluate_button.png" /></ac:image>.<br /><ac:image><ri:attachment ri:filename="evaluating_from_smart_manipulator.png" /></ac:image></li></ul></li></ol><p>After evaluation, runtime values are displayed in blue next to attributes, references, and satisfy requirements in a view. In addition, the values that pass or fail <span style="color:var(--ds-text,#172b4d);">requirements and constraints are highlighted in green and red, respectively. To learn more, see <ac:link><ri:page ri:content-title="Displaying evaluation information" /></ac:link>.</span></p><h3>Evaluating elements via the SysML v2 Model Evaluation console</h3><p>You can evaluate model elements by writing an expression directly in the <strong>SysML v2 Model Evaluation</strong> console. However, you need to call the element you want to evaluate directly, because the console will not display the evaluation results of the owned and inherited elements.</p><p>To evaluate an element via the <strong>SysML v2 Model Evaluation</strong> console</p><hr /><ol><li>Select <strong>Window</strong> &gt; <strong>SysML v2 Model Evaluation</strong> to open the <strong>SysML v2 Model Evaluation</strong> console.</li><li>In the input box of the console, type the qualified name of the element you want to evaluate and press Enter.<br /><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="e7ef7365-c601-472f-a96c-786fb881295e"><ac:rich-text-body><p>To save time, click <ac:image ac:thumbnail="true" ac:height="16"><ri:attachment ri:filename="context_selection_icon.png" /></ac:image> in the toolbar of the <strong>SysML v2 Model Evaluation</strong> console to enable context selection in the Containment tree. When context selection is enabled, select the owner of the element you want to evaluate and enter only the element's name to evaluate it.</p></ac:rich-text-body></ac:structured-macro><ac:image><ri:attachment ri:filename="evaluating_attribute_in_console.png" /></ac:image></li></ol><p>The evaluation results are displayed in the <strong style="letter-spacing: 0.0px;">SysML v2 Model Evaluation</strong><span style="letter-spacing: 0.0px;"> console as shown in the above figure.</span></p><p><br /></p>
````

<!--NOMAGIC_PAGE id=312246334 space=SYSML2EP version=3 -->
## PAGE 00042: Evaluation information in views

- page_id: `312246334`
- space_key: `SYSML2EP`
- source_url: https://docs.nomagic.com/spaces/SYSML2EP/pages/312246334/Evaluation+information+in+views
- version_number: 3
- version_date: `2026-06-10T16:37:54.912+02:00`
- ancestors: SysML v2 Evaluation Plugin Documentation > User guide
- labels: []

### NORMALIZED CONTENT

During evaluation, model views display evaluation results, allowing you to analyze variable values and calculated data without leaving the modeling environment. Runtime information can also be modified, with the evaluation results being automatically recalculated.

For more information, see the following topics:

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p style="text-align: left;">During evaluation, model views display evaluation results, allowing you to analyze <ac:inline-comment-marker ac:ref="bbb77401-49f2-4dc8-ac15-ce978d1217b5">variable</ac:inline-comment-marker> values and calculated data without leaving the modeling environment. Runtime information can also be modified, with the evaluation results being automatically recalculated.</p><p style="text-align: left;">For more information, see the following topics:</p><p style="text-align: left;"><ac:structured-macro ac:macro-id="b027cb9d-9f14-477a-a187-8b230c3195c1" ac:name="children" ac:schema-version="2" /></p>
````

<!--NOMAGIC_PAGE id=249578015 space=SYSML2EP version=15 -->
## PAGE 00043: Evaluation using Jupyter Notebook

- page_id: `249578015`
- space_key: `SYSML2EP`
- source_url: https://docs.nomagic.com/spaces/SYSML2EP/pages/249578015/Evaluation+using+Jupyter+Notebook
- version_number: 15
- version_date: `2026-03-17T14:22:13.500+01:00`
- ancestors: SysML v2 Evaluation Plugin Documentation > User guide > Server-side evaluation
- labels: []

### NORMALIZED CONTENT

You can evaluate Teamwork Cloud projects on the server by using Jupyter Notebook. This chapter explains how to set up Jupyter Notebook for server-side evaluation and describes all available requests.

Server-side evaluation is available only with the Teamwork Cloud Enterprise license.

##### Setting up Jupyter Notebook

To set up Jupyter Notebook

- In Jupyter Notebook, run the following command to install a Python package from the < install_root >\plugins\com.nomagic.magicdraw.sysml2.evaluation.plugin/pyEval.zip file:

Use the following requests to evaluate Teamwork Cloud projects on the server:

##### Creating a client/session and authenticating

<server_host>

<server_port>

<TWC_user_name>

<TWC_user_password>

This request starts a work session and provides authentication to Teamwork Cloud.

The following table describes the parameters used in the request:

| Parameter | In | Required or optional | Description |
| --- | --- | --- | --- |
| server_host | path | required | The Teamwork Cloud server host name. |
| server_port | path | required | The Teamwork Cloud server port. |
| TWC_user_name | path | optional | The Teamwork Cloud user name. If you do not specify the user name in the request, an input field will be provided to specify it later. |
| TWC_user_password | path | optional | The Teamwork Cloud password. If you do not specify the password in the request, an input field will be provided to specify it later. |

##### Getting the list of Teamwork Cloud projects

client.get_projects()

This request provides the list of Teamwork Cloud projects accessible to you depending on your permissions. Only projects that you can read (the Read Resources permission) are returned.

```text

```

##### Getting the list of project commits

<projectID>

This request provides the list of commits for the specified Teamwork Cloud project.

| Parameter | In | Required or optional | Description |
| --- | --- | --- | --- |
| projectID | path | required | The Teamwork Cloud project ID. |

```text

```

##### Getting the list of root-level elements

client.get_roots(<projectID>, commit=<commitID>)

This request returns all root-level model elements for the specified project. If there are several namespaces, they are merged into one list.

The following table describes the parameters used in therequest:

| Parameter | In | Required or optional | Description |
| --- | --- | --- | --- |
| projectID | path | required | The Teamwork Cloud project ID. |
| commit | path | optional | The commit ID of the Teamwork Cloud project. If the commit ID is not specified, the latest committed version is used instead. |

```text

```

##### Evaluating a parameter or expression

client.evaluate(<projectID>, commit=<commitID>, context=<contextPath>, data=json.dumps(<parameters>)

This request evaluates the specified Teamwork Cloud project parameter or expression.

The following table describes the parameters used in therequest:

| Parameter | In | Required or optional | Description |
| --- | --- | --- | --- |
| projectID | path | required | The Teamwork Cloud project ID. |
| commit | path | optional | The commit ID of the Teamwork Cloud project. If the commit ID is not specified, the latest committed version is used instead. |
| context | path | optional | The context path of the outputs, inputs, and expressions used to evaluate and retrieve data, e.g., SpacecraftMassRollup::spaceCraft. |
| inputs | body | optional | The set of inputs to be provided for the evaluation. Only inputs with initial values can be modified during evaluation. |
| outputs | body | optional | The set of outputs to be obtained after the evaluation. If no outputs are specified, all values are returned based on the specified context. |
| expressions | body | optional | The parameter or expression you want to evaluate. |

```text

```

##### Displaying an interactive HTML table

open_evaluation_table(self, <projectID>, commit=<commitID>, context=<contextPath>, params=<parmaList>, title=<tableTitle>, verification=<FAIL/ALL/NONE>)

This REST API request returns a JSON object containing the URL to an interactive HTML table that dynamically retrieves data based on the specified context, parameters, and/or expressions.

The following table describes the parameters used in the REST APIrequest:

| Parameter | In | Required or optional | Description |
| --- | --- | --- | --- |
| projectID | path | required | The Teamwork Cloud project ID. |
| commit | path | optional | The commit ID of the Teamwork Cloud project. If the commit ID is not specified, the latest committed version is used instead. |
| context | path | optional | The context path of the table parameters and/or expressions used to evaluate and retrieve data, e.g. SpacecraftMassRollup::spaceCraft. |
| params | path | optional | A comma-separated list of the parameters and/or expressions to display. Use the keyword 'all' to include all available parameters based on the specified context. |
| title | path | optional | The title of the HML table. |
| verification | path | optional | Specify which verification results to display: FAIL - failing values are highlighted in red; ALL - both failing and passing values are highlighted in red and green, respectively; NONE - no verification results are displayed. |

```text

```

```text

```

```text

```

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p style="text-align: left;">You can evaluate Teamwork Cloud projects on the server by using Jupyter Notebook. This chapter explains how to set up Jupyter Notebook for server-side evaluation and describes all available requests.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="69f6901c-8022-42de-a5bd-e06c4d2f1871"><ac:rich-text-body><p>Server-side evaluation is available only with the Teamwork Cloud Enterprise license.</p></ac:rich-text-body></ac:structured-macro><h3>Setting up Jupyter Notebook</h3><p style="text-align: left;">To set up Jupyter Notebook</p><hr /><ul><li data-uuid="9be626c8-3c24-4396-983b-497898a32610">In Jupyter Notebook, run the following command to install a Python package from the &lt;<em>install_root</em><em>&gt;\plugins\com.nomagic.magicdraw.sysml2.evaluation.<span style="color:var(--ds-text,#172b4d);">plugin/pyEval.zip</span></em><span> </span>file:<br /><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="1008cc78-0a4e-476a-9e42-f3eec6d268c4"><ac:plain-text-body><![CDATA[%pip install pyEval.zip]]></ac:plain-text-body></ac:structured-macro></li></ul><p style="text-align: left;">Use the following requests to evaluate Teamwork Cloud projects on the server:</p><h3>Creating a client/session and authenticating</h3><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="9564e4a8-1fa2-40d1-9fa9-4b6076430a22"><ac:rich-text-body>client = EvaluationWebClient('http(s)://<span style="color:var(--ds-background-accent-orange-bolder,#c25100);">&lt;server_host&gt;</span>:<span style="color:var(--ds-background-accent-orange-bolder,#c25100);">&lt;server_port&gt;</span>', '<span style="color:var(--ds-background-accent-orange-bolder,#c25100);">&lt;TWC_user_name&gt;</span>', '<span style="color:var(--ds-background-accent-orange-bolder,#c25100);">&lt;TWC_user_password&gt;</span>', False)</ac:rich-text-body></ac:structured-macro><p>This request starts a work session and provides authentication to Teamwork Cloud.</p><p>The following table describes the parameters used in the request:</p><table class="relative-table wrapped" style="width: 68.7671%;"><colgroup class=""> <col class="" style="width: 12.4396%;" /> <col class="" style="width: 8.85127%;" /> <col class="" style="width: 12.0455%;" /> <col class="" style="width: 66.6636%;" /> </colgroup><tbody class=""><tr class=""><th>Parameter</th><th>In</th><th>Required or optional</th><th colspan="1">Description</th></tr><tr class=""><td><strong>server_host</strong></td><td>path</td><td>required</td><td colspan="1">The Teamwork Cloud server host name.</td></tr><tr class=""><td colspan="1"><strong>server_port</strong></td><td colspan="1">path</td><td colspan="1">required</td><td colspan="1">The Teamwork Cloud server port.</td></tr><tr class=""><td colspan="1"><strong>TWC_user_name</strong></td><td colspan="1">path</td><td colspan="1">optional</td><td colspan="1"><p><span style="color:var(--ds-text,#172b4d);">The Teamwork Cloud user name. </span><span style="color:var(--ds-text,#172b4d);">If you do not specify the user name in the request, an input field will be provided to specify it later.</span></p></td></tr><tr class=""><td colspan="1"><strong>TWC_user_password</strong></td><td colspan="1">path</td><td colspan="1">optional</td><td colspan="1"><span style="color:var(--ds-text,#172b4d);">The Teamwork Cloud password. </span><span style="color:var(--ds-text,#172b4d);">If you do not specify the password in the request, an input field will be provided to specify it later.</span></td></tr></tbody></table><h3 style="text-align: left;">Getting the list of Teamwork Cloud projects</h3><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="6037605c-3e3f-4edb-9b21-86a381d0f6dc"><ac:rich-text-body>client.get_projects()</ac:rich-text-body></ac:structured-macro><p style="text-align: left;"><span style="color:var(--ds-text,#333333);">This request provides the list of Teamwork Cloud projects accessible to you depending on your permissions. Only projects that you can read (the Read Resources permission) are returned.</span></p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="cb1de3dc-c6b6-41d9-86cd-1dee792071ad"><ac:parameter ac:name="title">Request and response example</ac:parameter><ac:plain-text-body><![CDATA[client.get_projects()

[
    {
        'created': '2025-05-27T08:36:26.723Z',
        '@id': '62b072da-22f7-4ee7-9abe-37605571f9b7',
        'description': '',
        '@type': 'Project',
        'defaultBranch': {
            '@id': '7765ea2c-7cc4-4f12-9606-060ae8c8304d'
        },
        'name': "Don't Panic Batmobile"
    },
    {
        'created': '2025-05-27T08:29:52.949Z',
        '@id': 'b906d747-63c2-4d37-a809-49bd07d2eeba',
        'description': '',
        '@type': 'Project',
        'defaultBranch': {
            '@id': 'bbe03735-3093-44d1-bd48-9856b4c00da4'
        },
        'name': 'SysML Customization'
    },
    {
        'created': '2025-05-28T17:03:01.861Z',
        '@id': 'e7b10c6e-ae3c-49e9-af97-42d6384ebc2c',
        'description': '',
        '@type': 'Project',
        'defaultBranch': {
            '@id': 'e6d3df11-3260-4428-bb41-a0a2255e8c69'
        },
        'name': 'Spacecraft Mass Rollup V2'
    },
    {
        'created': '2025-05-28T17:07:08.197Z',
        '@id': '76ac1bae-11c9-434b-9096-3639ab338cf0',
        'description': '',
        '@type': 'Project',
        'defaultBranch': {
            '@id': 'fd07a9b3-8be1-4e6e-90f1-2992d983f8e0'
        },
        'name': 'Hinge Monte Carlo Analysis V2'
    }
]]]></ac:plain-text-body></ac:structured-macro><p style="text-align: left;"><br /></p><h3 style="text-align: left;">Getting the list of project commits</h3><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="2591f19f-8505-45ec-a3ef-9b1a622a1e0e"><ac:rich-text-body>client.get_commits(<span style="color:var(--ds-background-accent-orange-bolder,#c25100);">&lt;projectID&gt;</span>)</ac:rich-text-body></ac:structured-macro><p>This request provides the list of commits for the specified Teamwork Cloud project.</p><table class="relative-table wrapped" style="width: 68.7671%;"><colgroup class=""> <col class="" style="width: 12.4396%;" /> <col class="" style="width: 8.85127%;" /> <col class="" style="width: 12.0455%;" /> <col class="" style="width: 66.6636%;" /> </colgroup><tbody class=""><tr class=""><th>Parameter</th><th>In</th><th>Required or optional</th><th colspan="1">Description</th></tr><tr class=""><td><strong>projectID</strong></td><td>path</td><td>required</td><td colspan="1">The Teamwork Cloud project ID.</td></tr></tbody></table><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="60ce26c7-eac3-49bd-8bc0-68eb9b7c4583"><ac:parameter ac:name="title">Request and response example</ac:parameter><ac:plain-text-body><![CDATA[client.get_commits('62b072da-22f7-4ee7-9abe-37605571f9b7')

[
    {
        'created': '2025-05-27T08:36:26.410Z',
        '@id': '15a995d2-01cf-499b-a2d8-1f943af14320',
        'description': '** no message **',
        'owningProject': {
            '@id': '62b072da-22f7-4ee7-9abe-37605571f9b7'
        },
        'previousCommit': [
            {'@id': None}
        ]
    },
    {
        'created': '2025-05-27T08:39:34.763Z',
        '@id': 'b7a03a50-f42a-495d-9bd1-d87978d7f73f',
        'description': '** no message **',
        'owningProject': {
            '@id': '62b072da-22f7-4ee7-9abe-37605571f9b7'
        },
        'previousCommit': [
            {'@id': '15a995d2-01cf-499b-a2d8-1f943af14320'}
        ]
    }
]]]></ac:plain-text-body></ac:structured-macro><h3 style="text-align: left;">Getting the list of root-level elements</h3><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="c3c70852-5135-4c08-9292-2c88b44ea84b"><ac:rich-text-body><p><span style="color:var(--ds-text,#172b4d);">client.get_roots(<span style="color:var(--ds-background-accent-orange-bolder,#c25100);">&lt;projectID&gt;</span>, commit=<span style="color:var(--ds-background-accent-orange-bolder,#c25100);">&lt;commitID&gt;</span>)</span></p></ac:rich-text-body></ac:structured-macro><p>This request returns all root-level model elements for the specified project. <span style="color:var(--ds-text,#172B4D);">If there are several namespaces, they are merged into one list.</span></p><p><span style="color:var(--ds-text,#172b4d);">The following table describes the parameters used in the </span>request<span style="color:var(--ds-text,#172b4d);">:</span></p><table class="relative-table wrapped" style="width: 68.6413%;"><colgroup class=""><col class="" style="width: 9.82647%;" /><col class="" style="width: 7.84533%;" /><col class="" style="width: 10.4604%;" /><col class="" style="width: 71.8678%;" /></colgroup><tbody class=""><tr class=""><th>Parameter</th><th>In</th><th>Required or optional</th><th>Description</th></tr><tr class=""><td><strong>projectID</strong></td><td>path</td><td>required</td><td>The Teamwork Cloud project ID.</td></tr><tr class=""><td><strong>commit</strong></td><td>path</td><td>optional</td><td>The commit ID of the Teamwork Cloud project. If the commit ID is not specified, the latest committed version is used instead.</td></tr></tbody></table><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="41a398b4-3d38-4b02-bf03-c849ca3bb406"><ac:parameter ac:name="title">Request and response example</ac:parameter><ac:plain-text-body><![CDATA[client.get_roots('62b072da-22f7-4ee7-9abe-37605571f9b7')

[
  {
    "@id": "d6f0eea9-70fd-4ca8-b75f-3c794bd64f2b",
    "@type": "Package",
    "name": "Calculations",
    "elementId": "_G2tFcXD4Ee-huNu5so5rpw"
  },
  {
    "@id": "530d4e51-4f1d-4dfc-aae3-df7ece7dcdea",
    "@type": "Package",
    "name": "Requirements",
    "elementId": "_G2vhsXD4Ee-huNu5so5rpw"
  },
  {
    "@id": "2c5055d8-2899-4727-89c0-51072f20b60f",
    "@type": "Package",
    "name": "Vehicle",
    "elementId": "_G2ylAXD4Ee-huNu5so5rpw"
  },
  {
    "@id": "c1f8cfff-421a-4ab7-ac51-c1ad63899feb",
    "@type": "Package",
    "name": "TradeStudyAnalysis",
    "elementId": "_achG0XQLEe-Dbrd_o2J6Vg"
  }
]]]></ac:plain-text-body></ac:structured-macro><h3 style="text-align: left;">Evaluating a parameter or expression</h3><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="b1cda8f0-a944-47d9-80c8-da8df670be11"><ac:rich-text-body><p>client.evaluate(<span style="color:var(--ds-background-accent-orange-bolder,#c25100);">&lt;projectID&gt;</span>, commit=<span style="color:var(--ds-background-accent-orange-bolder,#c25100);">&lt;commitID&gt;</span>, context=<span style="color:var(--ds-background-accent-orange-bolder,#c25100);">&lt;contextPath&gt;</span>, data=json.dumps(<span style="color:var(--ds-background-accent-orange-bolder,#c25100);">&lt;parameters&gt;</span>)</p></ac:rich-text-body></ac:structured-macro><p style="text-align: left;"><span style="color:var(--ds-text,#172b4d);">This request evaluates the specified Teamwork Cloud project parameter or expression.</span></p><p style="text-align: left;"><span style="color:var(--ds-text,#172b4d);">The following table describes the parameters used in the </span>request<span style="color:var(--ds-text,#172b4d);">:</span></p><table class="relative-table wrapped" style="width: 68.6413%;"><colgroup class=""><col class="" style="width: 9.82647%;" /><col class="" style="width: 7.84533%;" /><col class="" style="width: 10.4604%;" /><col class="" style="width: 71.8678%;" /></colgroup><tbody class=""><tr class=""><th>Parameter</th><th>In</th><th>Required or optional</th><th>Description</th></tr><tr class=""><td><strong>projectID</strong></td><td>path</td><td>required</td><td>The Teamwork Cloud project ID.</td></tr><tr class=""><td><strong>commit</strong></td><td>path</td><td>optional</td><td>The commit ID of the Teamwork Cloud project. If the commit ID is not specified, the latest committed version is used instead.</td></tr><tr class=""><td><strong>context</strong></td><td>path</td><td>optional</td><td><span style="color:var(--ds-text-accent-purple-bolder,#352c63);">The context path of the outputs, inputs, and expressions used to evaluate and retrieve data, e.g., SpacecraftMassRollup::spaceCraft.</span></td></tr><tr class=""><td><strong>inputs</strong></td><td>body</td><td>optional</td><td>The set of inputs to be provided for the evaluation. <span style="color:var(--ds-text-accent-purple-bolder,#352c63);">Only inputs with initial values can be modified during evaluation.</span></td></tr><tr class=""><td><strong>outputs</strong></td><td>body</td><td>optional</td><td>The set of outputs to be obtained after the evaluation. <span style="color:var(--ds-text-accent-purple-bolder,#352c63);">If no outputs are specified, all values are returned based on the specified context.</span></td></tr><tr class=""><td><strong>expressions</strong></td><td>body</td><td>optional</td><td><div class="content-wrapper"><p>The parameter or expression you want to evaluate.</p></div></td></tr></tbody></table><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="9ce7bcd1-f696-4cae-a962-1e39e6de0c3e"><ac:parameter ac:name="title">Request example with a request body</ac:parameter><ac:plain-text-body><![CDATA[parameters = {
 "inputs":
   {
        "propulsion.thruster.me":32,
        "telecom.amplifier.me":15
   },
 "outputs": 
    [ 
        "me",
        "propulsion.mee",
        "propulsion.tank.me",
        "propulsion.thruster.me",
        "telecom.me",
        "telecom.antenna.me",
        "telecom.amplifier.me"
    ]
}

client.evaluate('a9e055de-e288-4b81-81e4-e24bbb32cedd', context='SpacecraftMassRollup::spacecraft', data=json.dumps(parameters))]]></ac:plain-text-body></ac:structured-macro><h3 style="text-align: left;">Displaying an interactive HTML table</h3><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="db3f2dcb-7a12-4b80-9beb-3093dfc154af"><ac:rich-text-body><p>open_evaluation_table(self, <span style="color:var(--ds-background-accent-orange-bolder,#c25100);">&lt;projectID&gt;</span>, commit=<span style="color:var(--ds-background-accent-orange-bolder,#c25100);">&lt;commitID&gt;</span>, context=<span style="color:var(--ds-background-accent-orange-bolder,#c25100);">&lt;contextPath&gt;</span>, params=<span style="color:var(--ds-background-accent-orange-bolder,#c25100);">&lt;parmaList&gt;</span>, title=<span style="color:var(--ds-background-accent-orange-bolder,#c25100);">&lt;tableTitle&gt;</span>, verification=<span style="color:var(--ds-background-accent-orange-bolder,#c25100);">&lt;FAIL/ALL/NONE&gt;</span>)</p></ac:rich-text-body></ac:structured-macro><p style="text-align: left;"><span style="color:var(--ds-text,#172b4d);">This REST API request returns a JSON object containing the URL to an interactive HTML table that dynamically retrieves data based on the specified context, parameters, and/or expressions.</span></p><p style="text-align: left;"><span style="color:var(--ds-text,#172b4d);">The following table describes the parameters used in the REST API<span> </span></span>request<span style="color:var(--ds-text,#172b4d);">:</span></p><table class="relative-table wrapped" style="width: 68.6413%;"><colgroup class=""><col class="" style="width: 9.82647%;" /><col class="" style="width: 7.84533%;" /><col class="" style="width: 10.4604%;" /><col class="" style="width: 71.8678%;" /></colgroup><tbody class=""><tr class=""><th>Parameter</th><th>In</th><th>Required or optional</th><th>Description</th></tr><tr class=""><td><strong>projectID</strong></td><td>path</td><td>required</td><td>The Teamwork Cloud project ID.</td></tr><tr class=""><td><strong>commit</strong></td><td>path</td><td>optional</td><td>The commit ID of the Teamwork Cloud project. If the commit ID is not specified, the latest committed version is used instead.</td></tr><tr class=""><td><strong>context</strong></td><td>path</td><td>optional</td><td><span style="color:var(--ds-text-accent-purple-bolder,#352c63);">The context path of the table parameters and/or expressions used to evaluate and retrieve data, e.g. SpacecraftMassRollup::spaceCraft.</span></td></tr><tr class=""><td><strong>params</strong></td><td>path</td><td>optional</td><td><span style="color:var(--ds-text-accent-purple-bolder,#352c63);">A comma-separated list of the parameters and/or expressions to display. Use the keyword 'all' to include all available parameters based on the specified context.</span></td></tr><tr class=""><td><strong>title</strong></td><td>path</td><td>optional</td><td>The title of the HML table.</td></tr><tr class=""><td><strong>verification </strong></td><td>path</td><td>optional</td><td>Specify which verification results to display: <strong>FAIL</strong> - failing values are highlighted in red; <strong>ALL</strong> - both failing and passing values are highlighted in red and green, respectively; <strong>NONE</strong> - no verification results are displayed.</td></tr></tbody></table><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="8868d21a-0d23-441b-8e6e-fbfba7234301"><ac:parameter ac:name="title">Request example</ac:parameter><ac:plain-text-body><![CDATA[open_evaluation_table(self, dc8b24ee-462d-4874-8b52-b85978f242cc, commit=3fa85f64-5717-4562-b3fc-2c963f66afa6, context=SpacecraftMassRollup::spaceCraft, params=me,propulsion.tank.me,propulsion.thruster.me, title=SpaceCraftMassRollup)]]></ac:plain-text-body></ac:structured-macro><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="7eeb9179-0138-4d81-9713-2a4351d13de4"><ac:parameter ac:name="title">Request example</ac:parameter><ac:plain-text-body><![CDATA[open_evaluation_table(self, dc8b24ee-462d-4874-8b52-b85978f242cc, commit=3fa85f64-5717-4562-b3fc-2c963f66afa6, context=SpacecraftMassRollup::spaceCraft, params=all, title=SpaceCraftMassRollup, verification=fail)]]></ac:plain-text-body></ac:structured-macro><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="8ccc7679-c4d7-4164-aabf-1ac0e533016a"><ac:parameter ac:name="title">Request example</ac:parameter><ac:plain-text-body><![CDATA[open_evaluation_table(self, dc8b24ee-462d-4874-8b52-b85978f242cc, params=SpacecraftMassRollup::spaceCraft.me,SpacecraftMassRollup::spaceCraft.propulsion.tank.me, title=SpaceCraftMassRollup)]]></ac:plain-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=249578009 space=SYSML2EP version=13 -->
## PAGE 00044: Evaluation using REST API

- page_id: `249578009`
- space_key: `SYSML2EP`
- source_url: https://docs.nomagic.com/spaces/SYSML2EP/pages/249578009/Evaluation+using+REST+API
- version_number: 13
- version_date: `2026-04-28T18:25:47.122+02:00`
- ancestors: SysML v2 Evaluation Plugin Documentation > User guide > Server-side evaluation
- labels: []

### NORMALIZED CONTENT

You can use the following REST API requests to evaluate Teamwork Cloud projects on the server.

Server-side evaluation is available only with the Teamwork Cloud Enterprise license.

For more information about evaluation-related REST APIs, see *https://<server_IP>:8443/sysmlv2-api/swagger-ui/index.html,* where**<server_IP>**is your Teamwork Cloud server IP.There, you can findREST API descriptions in both machine-readable and human-readable formats.

##### Evaluating a parameter or expression

<projectID>

<commitID>

evaluate?context=

<contextPath>

This REST API request evaluates the specified Teamwork Cloud project parameter or expression.

The following table describes the parameters used in the REST APIrequest:

| Parameter | In | Required or optional | Description |
| --- | --- | --- | --- |
| projects | path | required | The Teamwork Cloud project ID. |
| commits | path | optional | The commit ID of the Teamwork Cloud project. If the commit ID is not specified, the latest committed version is used instead. |
| context | path | optional | The context path of the outputs, inputs, and expressions used to evaluate and retrieve data, e.g., SpacecraftMassRollup::spaceCraft |
| inputs | body | optional | The set of inputs to be provided for the evaluation. Only inputs with initial values can be modified during evaluation. |
| outputs | body | optional | The set of outputs to be obtained after the evaluation. If no outputs are specified, all values are returned based on the specified context. |
| expressions | body | optional | The parameter or expression you want to evaluate. |

```shell

```

```text

```

##### Displaying an interactive HTML table

GET /projects/<projectID>/commits/<commitID>/evaluate/table-view?context=<contextPath>?params=<paramsList>?title=<tableTitle>?verification=<FAIL/ALL/NONE>

This REST API request returns a URL to an interactive HTML table that dynamically retrieves data based on the specified context, parameters and/or expressions.

The following table describes the parameters used in the REST APIrequest:

| Parameter | In | Required or optional | Description |
| --- | --- | --- | --- |
| projects | path | required | The Teamwork Cloud project ID. |
| commits | path | optional | The commit ID of the Teamwork Cloud project. If the commit ID is not specified, the latest committed version is used instead. |
| context | path | optional | The context path of the table parameters and/or expressions used to evaluate and retrieve data, e.g. SpacecraftMassRollup::spaceCraft |
| params | path | optional | A comma-separated list of the parameters and/or expressions to display. Use the keyword 'all' to include all available parameters based on the specified context. |
| title | path | optional | The title of the HML table. |
| verification | path | optional | Specify which verification results to display: FAIL - failing values are highlighted in red; ALL - both failing and passing values are highlighted in red and green, respectively; NONE - no verification results are displayed. |

```text

```

```text

```

```text

```

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p style="text-align: left;">You can use the following REST API requests to evaluate Teamwork Cloud projects on the <ac:inline-comment-marker ac:ref="fe34aa72-4ced-4f7f-8b92-d3cd39200d55">server</ac:inline-comment-marker>.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="06e570ac-6c75-48a3-b433-bd9184d71368"><ac:rich-text-body><p>Server-side evaluation is available only with the Teamwork Cloud Enterprise license.</p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="c44a1752-1253-4e00-abfe-023fcb6c6003"><ac:rich-text-body><p><span style="color:var(--ds-text,#172b4d);"><span style="color:var(--ds-text,#172b4d);">For more information about evaluation-related REST APIs, see <em style="text-align: left;">https://&lt;server_IP&gt;:8443/sysmlv2-api/swagger-ui/index.html,</em> <span style="color:var(--ds-text,#172b4d);">where<span> </span></span><strong style="text-align: left;">&lt;server_IP&gt;</strong><span style="color:var(--ds-text,#172b4d);"><span> </span>is your Teamwork Cloud server IP.</span></span><span style="color:var(--ds-text,#172b4d);"> There, you can find<span> </span></span>REST API descriptions in both machine-readable and human-readable formats.</span></p></ac:rich-text-body></ac:structured-macro><h3 style="text-align: left;">Evaluating a parameter or expression</h3><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="b1cda8f0-a944-47d9-80c8-da8df670be11"><ac:rich-text-body>POST /api/projects/<span style="color:var(--ds-background-accent-orange-bolder,#c25100);">&lt;projectID&gt;</span>/commits/<span style="color:var(--ds-background-accent-orange-bolder,#c25100);">&lt;commitID&gt;</span>/<ac:inline-comment-marker ac:ref="6163968c-91fe-4a1f-b00d-444b5be91736"><span style="color:var(--ds-text,#172b4d);">evaluate?context=</span><span style="color:var(--ds-background-accent-orange-bolder,#c25100);">&lt;contextPath&gt;</span></ac:inline-comment-marker></ac:rich-text-body></ac:structured-macro><p style="text-align: left;"><span style="color:var(--ds-text,#172b4d);">This REST API request evaluates the specified Teamwork Cloud project parameter or expression.</span></p><p style="text-align: left;"><span style="color:var(--ds-text,#172b4d);">The following table describes the parameters used in the REST API<span> </span></span>request<span style="color:var(--ds-text,#172b4d);">:</span></p><table class="wrapped relative-table" style="width: 68.6413%;"><colgroup><col style="width: 9.82647%;" /><col style="width: 7.84533%;" /><col style="width: 10.4604%;" /><col style="width: 71.8678%;" /></colgroup><tbody><tr><th scope="col">Parameter</th><th scope="col">In</th><th scope="col">Required or optional</th><th scope="col">Description</th></tr><tr><td><strong>projects</strong></td><td>path</td><td>required</td><td>The Teamwork Cloud project ID.</td></tr><tr><td><strong><ac:inline-comment-marker ac:ref="c95d1c2f-f8db-4428-8f9e-4434713dff87">commits</ac:inline-comment-marker></strong></td><td>path</td><td>optional</td><td>The commit ID of the Teamwork Cloud project. If the commit ID is not specified, the latest committed version is used instead.</td></tr><tr><td><strong>context</strong></td><td>path</td><td><ac:inline-comment-marker ac:ref="6569328f-546e-4d2d-8496-bc76b93f78ce">optional</ac:inline-comment-marker></td><td><span style="color:var(--ds-text-accent-purple-bolder,#352c63);">The context path of the outputs, inputs, and expressions used to evaluate and retrieve data, e.g., SpacecraftMassRollup::spaceCraft</span></td></tr><tr><td><strong>inputs</strong></td><td>body</td><td><ac:inline-comment-marker ac:ref="6569328f-546e-4d2d-8496-bc76b93f78ce">optional</ac:inline-comment-marker></td><td>The set of inputs to be provided for the evaluation. <span style="color:var(--ds-text-accent-purple-bolder,#352c63);">Only inputs with initial values can be modified during evaluation.</span></td></tr><tr><td><strong>outputs</strong></td><td>body</td><td>optional</td><td>The set of outputs to be obtained after the evaluation. <span style="color:var(--ds-text-accent-purple-bolder,#352c63);">If no outputs are specified, all values are returned based on the specified context.</span></td></tr><tr><td><strong>expressions</strong></td><td>body</td><td><ac:inline-comment-marker ac:ref="af08c97c-2d9e-424e-a7dc-0723880586ca">optional</ac:inline-comment-marker></td><td><div class="content-wrapper"><p>The parameter or expression you want to evaluate.</p></div></td></tr></tbody></table><p><br /></p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="5de60b50-1f5b-47a3-b326-dbcc33d31869"><ac:parameter ac:name="language">shell</ac:parameter><ac:parameter ac:name="title">Request and response example with the request body</ac:parameter><ac:plain-text-body><![CDATA[POST /projects/dc8b24ee-462d-4874-8b52-b85978f242cc/evaluate?context=SpacecraftMassRollup::spaceCraft

{
  "inputs":
   {
        "propulsion.thruster.me":10,
        "telecom.amplifier.me":15
   },
 "outputs": 
    [ 
        "me",
        "propulsion.mee",
        "propulsion.tank.me",
        "propulsion.thruster.me",
        "telecom.me",
        "telecom.antenna.me",
        "telecom.amplifier.me"
    ]
}

Response:

{'outputs': 
 {'me': 144.0,
  'propulsion.tank.me': 100.0,
  'propulsion.thruster.me': 10.0,
  'telecom.me': 34.0,
  'telecom.amplifier.me': 15.0,
  'telecom.antenna.me': 19.0
 }
}]]></ac:plain-text-body></ac:structured-macro><p><br /></p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="457ffbed-3c36-4994-9206-eb01d204ae9c"><ac:parameter ac:name="title">Request and response example with the request body</ac:parameter><ac:plain-text-body><![CDATA[POST /projects/fa6e7f27-f922-4718-aba4-6b909d6d1dcc/evaluate

{
  "inputs":
   {
        "TradeStudyAnalysis::VehicleAlternatives::vehicle_A.grossMass":2000,
        "TradeStudyAnalysis::VehicleAlternatives::vehicle_A.grossMass":1000
   }
 "expressions": 
    [ 
        "TradeStudyAnalysis::VehicleAlternatives::vehicle_A.stoppingDistance-TradeStudyAnalysis::VehicleAlternatives::vehicle_B.stoppingDistance"
    ]
}

=== Response ===

{
'expressions': 
 ['TradeStudyAnalysis::VehicleAlternatives::vehicle_A.stoppingDistance-TradeStudyAnalysis::VehicleAlternatives::vehicle_B.stoppingDistance':56.9344
 ]
}]]></ac:plain-text-body></ac:structured-macro><h3 style="text-align: left;">Displaying an interactive HTML table</h3><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="db3f2dcb-7a12-4b80-9beb-3093dfc154af"><ac:rich-text-body><p><span style="color:var(--ds-text,#172b4d);">GET /projects/<span style="color:var(--ds-background-accent-orange-bolder,#c25100);">&lt;projectID&gt;</span>/commits/<span style="color:var(--ds-background-accent-orange-bolder,#c25100);">&lt;commitID&gt;</span>/evaluate/</span>table-view<span style="color:var(--ds-text,#172b4d);">?</span>context<span style="color:var(--ds-text,#172b4d);">=<span style="color:var(--ds-background-accent-orange-bolder,#c25100);">&lt;contextPath&gt;</span>?</span>params<span style="color:var(--ds-text,#172b4d);">=<span style="color:var(--ds-background-accent-orange-bolder,#c25100);">&lt;paramsList&gt;</span>?</span>title<span style="color:var(--ds-text,#172b4d);">=<span style="color:var(--ds-background-accent-orange-bolder,#c25100);">&lt;tableTitle&gt;<span style="color:var(--ds-text,#172b4d);">?verification=<span style="color:var(--ds-background-accent-orange-bolder,#c25100);">&lt;FAIL/ALL/NONE&gt;</span></span></span></span></p></ac:rich-text-body></ac:structured-macro><p style="text-align: left;"><span style="color:var(--ds-text,#172b4d);">This REST API request returns a URL to an interactive HTML table that dynamically retrieves data based on the specified context, parameters and/or expressions.</span></p><p style="text-align: left;"><span style="color:var(--ds-text,#172b4d);">The following table describes the parameters used in the REST API<span> </span></span>request<span style="color:var(--ds-text,#172b4d);">:</span></p><table class="relative-table wrapped" style="width: 68.6413%;"><colgroup><col style="width: 9.82647%;" /><col style="width: 7.84533%;" /><col style="width: 10.4604%;" /><col style="width: 71.8678%;" /></colgroup><tbody><tr><th>Parameter</th><th>In</th><th>Required or optional</th><th>Description</th></tr><tr><td><strong>projects</strong></td><td>path</td><td>required</td><td>The Teamwork Cloud project ID.</td></tr><tr><td><strong>commits</strong></td><td>path</td><td>optional</td><td>The commit ID of the Teamwork Cloud project. If the commit ID is not specified, the latest committed version is used instead.</td></tr><tr><td><strong>context</strong></td><td>path</td><td>optional</td><td><span style="color:var(--ds-text-accent-purple-bolder,#352c63);">The context path of the table parameters and/or expressions used to evaluate and retrieve data, e.g. SpacecraftMassRollup::spaceCraft</span></td></tr><tr><td><strong>params</strong></td><td>path</td><td>optional</td><td><span style="color:var(--ds-text-accent-purple-bolder,#352c63);">A comma-separated list of the parameters and/or expressions to display. Use the keyword 'all' to include all available parameters based on the specified context.</span></td></tr><tr><td><strong>title</strong></td><td>path</td><td>optional</td><td>The title of the HML table.</td></tr><tr><td><strong>verification</strong></td><td>path</td><td>optional</td><td>Specify which verification results to display: <strong>FAIL</strong> - failing values are highlighted in red; <strong>ALL</strong> - both failing and passing values are highlighted in red and green, respectively; <strong>NONE</strong> - no verification results are displayed.</td></tr></tbody></table><p><br /></p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="8868d21a-0d23-441b-8e6e-fbfba7234301"><ac:parameter ac:name="title">Request example</ac:parameter><ac:plain-text-body><![CDATA[GET /projects/dc8b24ee-462d-4874-8b52-b85978f242cc/commits/3fa85f64-5717-4562-b3fc-2c963f66afa6/evaluate/table-view?context=SpacecraftMassRollup::spaceCraft&params=me,propulsion.tank.me,propulsion.thruster.me&title=SpaceCraftMassRollup]]></ac:plain-text-body></ac:structured-macro><p><br /></p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="7eeb9179-0138-4d81-9713-2a4351d13de4"><ac:parameter ac:name="title">Request example</ac:parameter><ac:plain-text-body><![CDATA[GET /projects/dc8b24ee-462d-4874-8b52-b85978f242cc/commits/3fa85f64-5717-4562-b3fc-2c963f66afa6/evaluate/table-view?context=SpacecraftMassRollup::spaceCraft&params=all&title=SpaceCraftMassRollup?verification=fail]]></ac:plain-text-body></ac:structured-macro><p><br /></p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="8ccc7679-c4d7-4164-aabf-1ac0e533016a"><ac:parameter ac:name="title">Request example</ac:parameter><ac:plain-text-body><![CDATA[GET /projects/dc8b24ee-462d-4874-8b52-b85978f242cc/evaluate/table-view?params=SpacecraftMassRollup::spaceCraft.me,SpacecraftMassRollup::spaceCraft.propulsion.tank.me&title=SpaceCraftMassRollup]]></ac:plain-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=249577966 space=SYSML2EP version=21 -->
## PAGE 00045: Exporting evaluation results to CSV

- page_id: `249577966`
- space_key: `SYSML2EP`
- source_url: https://docs.nomagic.com/spaces/SYSML2EP/pages/249577966/Exporting+evaluation+results+to+CSV
- version_number: 21
- version_date: `2025-11-17T18:20:26.185+01:00`
- ancestors: SysML v2 Evaluation Plugin Documentation > User guide
- labels: []

### NORMALIZED CONTENT

You can use views to evaluate model elements displayed in a view and export the results to a CSV file.

To export the evaluation results to a CSV file

1. In the view toolbar, click [IMAGE alt='' src=''] to evaluate model elements displayed in the view.
2. In the view toolbar, click the arrow next to [IMAGE alt='' src=''] andselect**Export to CSV**. When the evaluation is performed on selected elements, only the results for those elements are exported. If no elements were selected, the export will include results for all elements displayed in the view. [ATTACHMENT filename='export_to_csv.png']
3. In the**CSV Export Options** dialog, specify the export options. To learn more, see 
[IMAGE alt='' src='']
4. Click **OK** to export the evaluation results.

The CSV file with evaluation results is saved in the specified location. You can open the file by clicking a link in the message saying that the CSV file was generated successfully.

##### CSV Export Options dialog

The following table describes the UI elements of the **CSV Export Options** dialog.

| UI element | Description |
| --- | --- |
| CSV Delimiter | Select the character used to separate values (columns) in a CSV file. The default CSV delimiter is selected according to the machine's locale. |
| Export annotated only | Select the Export annotated only check box to export only annotated results in the view. Clear the check box to export all evaluation results. |
| Attributes as columns | Select the Attributes as columns check box to export attributes to columns and paths to the corresponding rows. Clear the check box to print every value in a separate row. |
| Output | Specify the path to the CSV file. By default, the project directory is selected. |

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><span style="color:var(--ds-text,#172b4d);">You can use views to evaluate model elements displayed in a view and export the results to a CSV file.</span></p><p>To export the evaluation results to a CSV file</p><hr /><ol><li><p>In the <span style="color:var(--ds-text,#172b4d);">view toolbar</span>, click <ac:image ac:thumbnail="true" ac:height="14"><ri:attachment ri:filename="evaluate_button.png" /></ac:image> to evaluate model elements displayed in the view.</p></li><li><p>In the <span style="color:var(--ds-text,#172b4d);">view toolbar</span>, click the arrow next to <ac:image ac:thumbnail="true" ac:height="14"><ri:attachment ri:filename="evaluate_button.png" /></ac:image> and<span style="letter-spacing: 0.0px;"> select </span><strong style="letter-spacing: 0.0px;">Export to CSV</strong><span style="letter-spacing: 0.0px;">.<br /></span></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="bffab1b5-a500-4117-a00a-f37583c604e0"><ac:rich-text-body><p><span style="color:var(--ds-text,#172b4d);">When the evaluation is performed on selected elements, only the results for those elements are exported. If no elements were selected, the export will include results for all elements displayed in the view.</span></p></ac:rich-text-body></ac:structured-macro><ac:image ac:height="224"><ri:attachment ri:filename="export_to_csv.png" /></ac:image></li><li><p>In the<strong> CSV Export Options</strong> dialog, specify the export options. To learn more, see <ac:link ac:anchor="CSV Export Options dialog"><ac:plain-text-link-body><![CDATA[CSV Export Options dialog.]]></ac:plain-text-link-body></ac:link><br /><ac:image><ri:attachment ri:filename="csv_export_options.png" /></ac:image></p></li><li><p>Click <strong>OK</strong> to export the evaluation results.</p></li></ol><p>The CSV file with evaluation results is saved in the specified location. You can open the file by clicking a link in the message saying that the CSV file was generated successfully.</p><h3>CSV Export Options dialog</h3><p>The following table describes the UI elements of the <strong>CSV Export Options</strong> dialog.</p><table class="wrapped relative-table" style="width: 99.1781%;"><colgroup><col style="width: 14.0953%;" /><col style="width: 85.9237%;" /></colgroup><tbody><tr><th scope="col"><p>UI element</p></th><th scope="col"><p>Description</p></th></tr><tr><td><p><strong>CSV Delimiter</strong></p></td><td><p>Select the character used to separate values (columns) in a CSV file. The default CSV delimiter is selected according to the machine's locale. </p></td></tr><tr><td><p><strong>Export annotated only</strong></p></td><td><p>Select the <strong>Export annotated only </strong>check box to export only annotated results in the view. Clear the check box to export all evaluation results.</p></td></tr><tr><td><p><strong>Attributes as columns</strong></p></td><td><div class="content-wrapper"><p>Select the <strong>Attributes as columns </strong>check box to export attributes to columns and paths to the corresponding rows. Clear the check box to print every value in a separate row.</p><p><ac:image ac:height="222"><ri:attachment ri:filename="attributes_as_columns.png" /></ac:image></p></div></td></tr><tr><td><p><strong>Output</strong></p></td><td><p>Specify the path to the CSV file. By default, the project directory is selected. </p></td></tr></tbody></table>
````

<!--NOMAGIC_PAGE id=249577974 space=SYSML2EP version=7 -->
## PAGE 00046: Integration with MATLAB

- page_id: `249577974`
- space_key: `SYSML2EP`
- source_url: https://docs.nomagic.com/spaces/SYSML2EP/pages/249577974/Integration+with+MATLAB
- version_number: 7
- version_date: `2026-01-23T18:09:29.768+01:00`
- ancestors: SysML v2 Evaluation Plugin Documentation > User guide
- labels: ['matlab-integration']

### NORMALIZED CONTENT

If you install MATLAB and integrate it with your modeling tool, you will be able to evaluate scripts written in MATLAB syntax. For example, you can [use MATLAB as a script language to define the return in calculations](https://docs.nomagic.com/SYSML2EP/?contextKey=invoking-calculations&version=latest).

#### NOTE: Prerequisites

Prerequisites

- MATLAB 2023a and later versions have been tested for compatibility with SysML v2 projects. Support for older versions is not guaranteed.
- You must use the 64-bit version of MATLAB so it will work with the 64-bit version of modeling tools.
- If MATLAB was integrated before installing the SysML v2 Evaluation plugin, you must reintegrate it to ensure compatibility with SysML v2 projects.
- On Windows, the application requires admin rights to complete the integration with MATLAB. If admin rights are not granted or available, you will not be able to use MATLAB with SysML v2 projects.

To integrate a modeling tool with MATLAB

1. In the main menu, select Tools > Integrations .
2. In the Integrations dialog, select MATLAB and click Integrate/Remove Integration . 
[IMAGE alt='' src='']
3. In the open dialog, specify the MATLAB home directory . 
[IMAGE alt='' src=''] The JRE home directory is selected automatically.
4. Click **OK**.
5. If you use Windows, click Yes to grant the application admin rights. Otherwise, go to the next step.
6. When you get a message saying to restart the modeling tool, click OK and restart the modeling tool.

**Related pages**

- [CONFLUENCE_PAGE title='Connecting to a running MATLAB session' space='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p>If you install MATLAB and integrate it with your modeling tool, you will be able to evaluate scripts written in MATLAB syntax. For example, you can <a href="https://docs.nomagic.com/SYSML2EP/?contextKey=invoking-calculations&amp;version=latest">use MATLAB as a script language to define the return in calculations</a>.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="a62fa631-c814-4636-a48c-c579d65b2775"><ac:parameter ac:name="title">Prerequisites</ac:parameter><ac:rich-text-body><ul><li data-uuid="738f013e-5e85-4df4-9a26-727627077052"><span style="color:var(--ds-text,#172b4d);">MATLAB 2023a and later versions have been tested for compatibility with SysML v2 projects. Support for older versions is not guaranteed.</span></li><li data-uuid="46250bb8-88dc-4535-acde-7796f3e378d0">You must use the 64-bit version of MATLAB so it will work with the 64-bit version of modeling tools.</li><li data-uuid="279c4c89-7045-44bb-b595-a8c3c5204b44">If MATLAB was integrated before installing the SysML v2 Evaluation plugin, you must reintegrate it to ensure compatibility with SysML v2 projects.</li><li data-uuid="b66c7214-9ed4-4451-9a3a-a7afe98a6845"><p style="text-align: left;">On Windows, the application requires admin rights to complete the integration with MATLAB. If admin rights are not granted or available, you will not be able to use MATLAB with SysML v2 projects.</p></li></ul></ac:rich-text-body></ac:structured-macro><p><br /></p><p>To integrate a modeling tool with MATLAB</p><hr /><ol><li class="auto-cursor-target" data-uuid="3094f6a1-7cbb-4c87-8776-c3845c0f0ccb">In the main menu, select <strong>Tools </strong>&gt;<strong> Integrations</strong>.</li><li class="auto-cursor-target" data-uuid="83599c2f-e2f7-4603-b5d1-05b8456461ce">In the <strong>Integrations</strong> dialog, select <strong>MATLAB</strong> and click <strong>Integrate/Remove Integration</strong><span>.<br /><ac:image><ri:attachment ri:filename="integrations_dialog.png" /></ac:image><br /></span></li><li class="auto-cursor-target" data-uuid="78a36882-b376-40a4-a8ee-53cc7bfb4ae0">In the open dialog, specify the <strong>MATLAB home directory</strong><span>.<br /><ac:image><ri:attachment ri:filename="directory_selection_dialog.png" /></ac:image><br /></span><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="a5efb116-d9fe-4aa3-9560-a7b3acea2d26"><ac:rich-text-body><p>The JRE home directory is selected automatically.</p></ac:rich-text-body></ac:structured-macro></li><li class="auto-cursor-target" data-uuid="310fde7e-04cf-4a00-899a-8955c7951976"><p class="auto-cursor-target">Click <strong>OK</strong>.</p></li><li class="auto-cursor-target" data-uuid="a9ce527d-1f37-41ab-8bab-4a626b0b1e98">If you use Windows, click <strong>Yes</strong> to grant the application admin rights. Otherwise, go to the next step.</li><li class="auto-cursor-target" data-uuid="bbd5498b-8e9c-45cc-8d90-34fbb7553f95">When you get a message saying to restart the modeling tool, click <strong>OK</strong> and restart the modeling tool.</li></ol></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><strong>Related pages</strong></p><ul><li><ac:link><ri:page ri:content-title="Connecting to a running MATLAB session" /></ac:link></li></ul></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=271516427 space=SYSML2EP version=17 -->
## PAGE 00047: Invoking actions

- page_id: `271516427`
- space_key: `SYSML2EP`
- source_url: https://docs.nomagic.com/spaces/SYSML2EP/pages/271516427/Invoking+actions
- version_number: 17
- version_date: `2026-06-16T14:24:15.874+02:00`
- ancestors: SysML v2 Evaluation Plugin Documentation > User guide
- labels: []

### NORMALIZED CONTENT

An action definition is a type of occurrence definition that specifies what an action is and how it can be performed. An action usage is a type of occurrence usage that represents the**actual use of one or more action definitions within a particular situation or context.

You can invoke action definitions and action usages as described below.

To invoke an action definition or action usage

1. Create and define an action definition or action usage. For instructions, refer to the SysML v2 Plugin documentation .
2. Create an expression that invokes the action, for example, by defining an attribute whose value is computed through the action invocation.
3. Access a specific output of the action invocation in one of the following ways:
  - Use the dot notation in the invocation expression. ExampleactiondefcalculateCircleParameters{ 
inradius:Real; 
outdiameter:Real=radius*2; 
outcircumference:Real=diameter*3.14; 
outarea:Real=radius*radius*3.14; 
} 
partwheel{ 
attributeradius:Real=12; 
attributearea:Real=calculateCircleParameters(radius).area; 
}
  - Create a feature that stores the invocation result, e.g., actionInvoke , and then select specific outputs using dot notation. ExampleactiondefcalculateCircleParameters{ 
inradius:Real; 
outdiameter:Real=radius*2; 
outcircumference:Real=diameter*3.14; 
outarea:Real=radius*radius*3.14; 
} 
partwheel{ 
attributeradius:Real=12; 
actionInvoke=calculateCircleParameters(radius); 
attributearea:Real=actionInvoke.area; 
attributeperimeter:Real=actionInvoke.circumference; 
}
4. Evaluate an element whose value depends on the action invocation (e.g., the area or perimeter attribute in the above examples). For more information, see [CONFLUENCE_PAGE title='Evaluating model elements' space=''] .

The evaluation results are displayed in the**SysML v2 Model Evaluation**console.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>An action definition is a type of occurrence definition that specifies what an action is and how it can be performed. An action usage is a type of occurrence usage that represents the<em> </em>actual use of one or more action definitions within a particular situation or context.</p><p>You can invoke action definitions and action usages as described below.</p><p>To invoke an action definition or action usage</p><hr /><ol><li data-uuid="186c59fe-bc20-4821-acfd-955ef255002b">Create and define an action definition or action usage. For instructions, refer to the <a href="https://docs.nomagic.com/SYSML2P/?contextKey=creating-actions&amp;version=latest">SysML v2 Plugin documentation</a>.</li><li data-uuid="01127edb-6d1d-48c6-94c3-4218653fb14c">Create an expression that invokes the action, for example, by defining an attribute whose value is computed through the action invocation.</li><li data-uuid="61815bdb-074f-46db-b970-4f5f00c367cc"><span style="color:var(--ds-text,#172b4d);">Access a specific output of the action invocation in one of the following ways:</span><ul><li data-uuid="d874b0ac-0a93-459e-b58a-feb069b04110"><span style="color:var(--ds-text,#172b4d);">Use the dot notation in the invocation expression.<br /></span><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="fdfd9bdc-4046-4997-a249-ad9e5c74d2de"><ac:parameter ac:name="title">Example</ac:parameter><ac:rich-text-body><p><span style="color:var(--ds-text-accent-blue,#0055cc);">action</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">def</span><span style="color:var(--ds-chart-gray-bold,#8590a2);"> </span><span style="color:var(--ds-text-accent-teal,#206a83);">calculateCircleParameters</span><span style="color:var(--ds-text,#000000);"> {</span><br /><span style="color:var(--ds-text,#000000);">            </span><span style="color:var(--ds-text-accent-blue,#0055cc);">in</span><span style="color:var(--ds-chart-gray-bold,#8590a2);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">radius</span><span style="color:var(--ds-text,#000000);"> : </span><span style="color:var(--ds-text-accent-teal,#206a83);">Real</span><span style="color:var(--ds-text,#000000);">;</span><br /><span style="color:var(--ds-text,#000000);">            </span><span style="color:var(--ds-text-accent-blue,#0055cc);">out</span><span style="color:var(--ds-chart-gray-bold,#8590a2);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">diameter</span><span style="color:var(--ds-text,#000000);"> : </span><span style="color:var(--ds-text-accent-teal,#206a83);">Real</span><span style="color:var(--ds-text,#000000);"> = </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">radius</span><span style="color:var(--ds-text,#000000);"> * </span><span style="color:var(--ds-background-accent-green-bolder,#1f845a);">2</span><span style="color:var(--ds-text,#000000);">;</span><br /><span style="color:var(--ds-text,#000000);">            </span><span style="color:var(--ds-text-accent-blue,#0055cc);">out</span><span style="color:var(--ds-chart-gray-bold,#8590a2);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">circumference</span><span style="color:var(--ds-text,#000000);"> : </span><span style="color:var(--ds-text-accent-teal,#206a83);">Real</span><span style="color:var(--ds-text,#000000);"> = </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">diameter</span><span style="color:var(--ds-text,#000000);"> * </span><span style="color:var(--ds-background-accent-green-bolder,#1f845a);">3.14</span><span style="color:var(--ds-text,#000000);">;</span><br /><span style="color:var(--ds-text,#000000);">            </span><span style="color:var(--ds-text-accent-blue,#0055cc);">out</span><span style="color:var(--ds-chart-gray-bold,#8590a2);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">area</span><span style="color:var(--ds-text,#000000);"> : </span><span style="color:var(--ds-text-accent-teal,#206a83);">Real</span><span style="color:var(--ds-text,#000000);"> = </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">radius</span><span style="color:var(--ds-text,#000000);"> * </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">radius</span><span style="color:var(--ds-text,#000000);"> * </span><span style="color:var(--ds-background-accent-green-bolder,#1f845a);">3.14</span><span style="color:var(--ds-text,#000000);">;</span><br /><span style="color:var(--ds-text,#000000);">        }</span><br /><span style="color:var(--ds-text-accent-blue,#0055cc);">part</span><span style="color:var(--ds-chart-gray-bold,#8590a2);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">wheel</span><span style="color:var(--ds-text,#000000);"> {</span><br /><span style="color:var(--ds-text,#000000);">            </span><span style="color:var(--ds-text-accent-blue,#0055cc);">attribute</span><span style="color:var(--ds-chart-gray-bold,#8590a2);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">radius</span><span style="color:var(--ds-text,#000000);"> : </span><span style="color:var(--ds-text-accent-teal,#206a83);">Real</span><span style="color:var(--ds-text,#000000);"> = </span><span style="color:var(--ds-background-accent-green-bolder,#1f845a);">12</span><span style="color:var(--ds-text,#000000);">;</span><br /><span style="color:var(--ds-text,#000000);">            </span><span style="color:var(--ds-text-accent-blue,#0055cc);">attribute</span><span style="color:var(--ds-chart-gray-bold,#8590a2);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">area</span><span style="color:var(--ds-text,#000000);"> : </span><span style="color:var(--ds-text-accent-teal,#206a83);">Real</span><span style="color:var(--ds-text,#000000);"> = </span><span style="color:var(--ds-text-accent-teal,#206a83);">calculateCircleParameters</span><span style="color:var(--ds-text,#000000);">(</span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">radius</span><span style="color:var(--ds-text,#000000);">).</span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">area</span><span style="color:var(--ds-text,#000000);">;</span><br /><span style="color:var(--ds-text,#000000);">        }</span></p></ac:rich-text-body></ac:structured-macro><span style="color:var(--ds-text,#172b4d);"><br /></span></li><li data-uuid="3e402f5a-7e3d-4a75-8461-7cc760912742"><span style="color:var(--ds-text,#172b4d);">Create a feature that stores the invocation result, e.g., </span><em>actionInvoke</em>, <span style="color:var(--ds-text,#172b4d);">and then select specific outputs using dot notation.<br /></span><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="8fc65334-9f57-4157-9c1b-749899816c3f"><ac:parameter ac:name="title">Example</ac:parameter><ac:rich-text-body><p><span style="color:var(--ds-text-accent-blue,#0055cc);">action</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">def</span><span style="color:var(--ds-chart-gray-bold,#8590a2);"> </span><span style="color:var(--ds-text-accent-teal,#206a83);">calculateCircleParameters</span><span style="color:var(--ds-text,#000000);"> {</span><br /><span style="color:var(--ds-text,#000000);">            </span><span style="color:var(--ds-text-accent-blue,#0055cc);">in</span><span style="color:var(--ds-chart-gray-bold,#8590a2);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">radius</span><span style="color:var(--ds-text,#000000);"> : </span><span style="color:var(--ds-text-accent-teal,#206a83);">Real</span><span style="color:var(--ds-text,#000000);">;</span><br /><span style="color:var(--ds-text,#000000);">            </span><span style="color:var(--ds-text-accent-blue,#0055cc);">out</span><span style="color:var(--ds-chart-gray-bold,#8590a2);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">diameter</span><span style="color:var(--ds-text,#000000);"> : </span><span style="color:var(--ds-text-accent-teal,#206a83);">Real</span><span style="color:var(--ds-text,#000000);"> = </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">radius</span><span style="color:var(--ds-text,#000000);"> * </span><span style="color:var(--ds-background-accent-green-bolder,#1f845a);">2</span><span style="color:var(--ds-text,#000000);">;</span><br /><span style="color:var(--ds-text,#000000);">            </span><span style="color:var(--ds-text-accent-blue,#0055cc);">out</span><span style="color:var(--ds-chart-gray-bold,#8590a2);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">circumference</span><span style="color:var(--ds-text,#000000);"> : </span><span style="color:var(--ds-text-accent-teal,#206a83);">Real</span><span style="color:var(--ds-text,#000000);"> = </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">diameter</span><span style="color:var(--ds-text,#000000);"> * </span><span style="color:var(--ds-background-accent-green-bolder,#1f845a);">3.14</span><span style="color:var(--ds-text,#000000);">;</span><br /><span style="color:var(--ds-text,#000000);">            </span><span style="color:var(--ds-text-accent-blue,#0055cc);">out</span><span style="color:var(--ds-chart-gray-bold,#8590a2);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">area</span><span style="color:var(--ds-text,#000000);"> : </span><span style="color:var(--ds-text-accent-teal,#206a83);">Real</span><span style="color:var(--ds-text,#000000);"> = </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">radius</span><span style="color:var(--ds-text,#000000);"> * </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">radius</span><span style="color:var(--ds-text,#000000);"> * </span><span style="color:var(--ds-background-accent-green-bolder,#1f845a);">3.14</span><span style="color:var(--ds-text,#000000);">;</span><br /><span style="color:var(--ds-text,#000000);">        }</span><br /><span style="color:var(--ds-text-accent-blue,#0055cc);">part</span><span style="color:var(--ds-chart-gray-bold,#8590a2);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">wheel</span><span style="color:var(--ds-text,#000000);"> {</span><br /><span style="color:var(--ds-text,#000000);">            </span><span style="color:var(--ds-text-accent-blue,#0055cc);">attribute</span><span style="color:var(--ds-chart-gray-bold,#8590a2);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">radius</span><span style="color:var(--ds-text,#000000);"> : </span><span style="color:var(--ds-text-accent-teal,#206a83);">Real</span><span style="color:var(--ds-text,#000000);"> = </span><span style="color:var(--ds-background-accent-green-bolder,#1f845a);">12</span><span style="color:var(--ds-text,#000000);">;</span><br /><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">            actionInvoke</span><span style="color:var(--ds-text,#000000);"> = </span><span style="color:var(--ds-text-accent-teal,#206a83);">calculateCircleParameters</span><span style="color:var(--ds-text,#000000);">(</span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">radius</span><span style="color:var(--ds-text,#000000);">);</span><br /><span style="color:var(--ds-text,#000000);">            </span><span style="color:var(--ds-text-accent-blue,#0055cc);">attribute</span><span style="color:var(--ds-chart-gray-bold,#8590a2);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">area</span><span style="color:var(--ds-text,#000000);"> : </span><span style="color:var(--ds-text-accent-teal,#206a83);">Real</span><span style="color:var(--ds-text,#000000);"> = </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">actionInvoke</span><span style="color:var(--ds-text,#000000);">.</span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">area</span><span style="color:var(--ds-text,#000000);">;</span><br /><span style="color:var(--ds-text,#000000);">            </span><span style="color:var(--ds-text-accent-blue,#0055cc);">attribute</span><span style="color:var(--ds-chart-gray-bold,#8590a2);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">perimeter</span><span style="color:var(--ds-text,#000000);"> : </span><span style="color:var(--ds-text-accent-teal,#206a83);">Real</span><span style="color:var(--ds-text,#000000);"> = </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">actionInvoke</span><span style="color:var(--ds-text,#000000);">.</span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">circumference</span><span style="color:var(--ds-text,#000000);">;</span><br /><span style="color:var(--ds-text,#000000);">        }</span></p></ac:rich-text-body></ac:structured-macro><span style="color:var(--ds-text,#172b4d);"><br /></span></li></ul></li><li data-uuid="a234ed53-86bc-4886-8fcd-4930fa75db86">Evaluate an element whose value depends on the action invocation (e.g., the <em>area</em> or <em>perimeter</em> attribute in the above examples). For more information, see <ac:link><ri:page ri:content-title="Evaluating model elements" /></ac:link>.</li></ol><p><span style="color:var(--ds-text,#172b4d);">The evaluation results are displayed in the </span><strong>SysML v2 Model Evaluation</strong><span style="color:var(--ds-text,#172b4d);"><span> </span>console.</span></p>
````

<!--NOMAGIC_PAGE id=249577960 space=SYSML2EP version=13 -->
## PAGE 00048: Invoking calculations

- page_id: `249577960`
- space_key: `SYSML2EP`
- source_url: https://docs.nomagic.com/spaces/SYSML2EP/pages/249577960/Invoking+calculations
- version_number: 13
- version_date: `2026-06-16T14:23:39.562+02:00`
- ancestors: SysML v2 Evaluation Plugin Documentation > User guide
- labels: []

### NORMALIZED CONTENT

A calculation specifies a reusable computation that returns a result in the result parameter. In addition to its parameters, a calculation may have features that are calculation or action usages, which carry out steps in the computation of the calculation result. A calculation always has a result parameter, which can be declared as an out parameter using the keyword*return*instead of*out*.

You can invoke calculation definitions and calculation usages as described below.

To invoke a calculation definition or calculation usage

1. Create and define a calculation definition or calculation usage. For instructions, refer to the SysML v2 Plugin documentation .
2. Create an invocation expression, e.g., an attribute, whose value is the result of the calculation.
3. Assign the created calculation to the invocation expression and define the calculation inputs. When defining the calculation inputs, keep in mind that they will be taken in the same order as defined in the calculation. ExamplecalcdefArea{ 
inlength:Real; 
inwidth:Real; 
returnresult:Real; 
result=length*width; 
} 
partpad{ 
attributesurfaceArea:Real=Area(centerLength, width); 
}
4. Evaluate the invocation expression (e.g., the surfaceArea attribute in the above example). For more information, see [CONFLUENCE_PAGE title='Evaluating model elements' space=''] .

The evaluation results are displayed in the**SysML v2 Model Evaluation**console.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><span style="color:var(--ds-text,#172b4d);">A calculation specifies a reusable computation that returns a result in the result parameter. In addition to its parameters, a calculation may have features that are calculation or action usages, which carry out steps in the computation of the calculation result. A calculation always has a result parameter, which can be declared as an out parameter using the keyword<span> </span></span><em style="text-align: left;">return</em><span style="color:var(--ds-text,#172b4d);"><span> </span>instead of<span> </span></span><em style="text-align: left;">out</em><span style="color:var(--ds-text,#172b4d);">.</span></p><p>You can invoke calculation definitions and calculation usages as described below.</p><p>To invoke a calculation definition or calculation usage</p><hr /><ol><li>Create and define a calculation definition or calculation usage. For instructions, refer to the <a href="https://docs.nomagic.com/SYSML2P/?contextKey=calculation&amp;version=latest">SysML v2 Plugin documentation</a>.</li><li>Create an invocation expression, e.g., an attribute, whose value is the result of the calculation.</li><li>Assign the created calculation to the invocation expression and define the calculation inputs.<br /><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="e811507c-c932-4f1e-b7f3-724fd61f8477"><ac:rich-text-body><p>When defining the calculation inputs, keep in mind that they will be taken in the same order as defined in the calculation.</p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="b5afa193-4f21-47eb-bec6-8cf7cb29b5ff"><ac:parameter ac:name="title">Example</ac:parameter><ac:rich-text-body><p><span style="color:var(--ds-text-accent-blue,#0055cc);">calc</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">def</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-teal,#206a83);">Area</span><span style="color:var(--ds-text,#000000);"> {</span><br /><span style="color:var(--ds-text,#000000);">            </span><span style="color:var(--ds-text-accent-blue,#0055cc);">in</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">length</span><span style="color:var(--ds-text,#000000);"> : </span><span style="color:var(--ds-text-accent-teal,#206a83);">Real</span><span style="color:var(--ds-text,#000000);">;</span><br /><span style="color:var(--ds-text,#000000);">            </span><span style="color:var(--ds-text-accent-blue,#0055cc);">in</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">width</span><span style="color:var(--ds-text,#000000);"> : </span><span style="color:var(--ds-text-accent-teal,#206a83);">Real</span><span style="color:var(--ds-text,#000000);">;</span><br /><span style="color:var(--ds-text,#000000);">            </span><span style="color:var(--ds-text-accent-blue,#0055cc);">return</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">result</span><span style="color:var(--ds-text,#000000);"> : </span><span style="color:var(--ds-text-accent-teal,#206a83);">Real</span><span style="color:var(--ds-text,#000000);">;</span><br /><span style="color:var(--ds-text,#000000);">            </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">result</span><span style="color:var(--ds-text,#000000);"> = </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">length</span><span style="color:var(--ds-text,#000000);"> * </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">width</span><span style="color:var(--ds-text,#000000);">;</span><br /><span style="color:var(--ds-text,#000000);"> }       </span><br /><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">part</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">pad</span><span style="color:var(--ds-text,#000000);"> {</span><br /><span style="color:var(--ds-text,#000000);">            </span><span style="color:var(--ds-text-accent-blue,#0055cc);">attribute</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">surfaceArea</span><span style="color:var(--ds-text,#000000);"> : </span><span style="color:var(--ds-text-accent-teal,#206a83);">Real</span><span style="color:var(--ds-text,#000000);"> = </span><span style="color:var(--ds-text-accent-teal,#206a83);">Area</span><span style="color:var(--ds-text,#000000);">(centerLength, width);</span><br /><span style="color:var(--ds-text,#000000);"> }</span></p></ac:rich-text-body></ac:structured-macro></li><li>Evaluate the invocation expression (e.g., the <em>surfaceArea</em> attribute in the above example). For more information, see <ac:link><ri:page ri:content-title="Evaluating model elements" /></ac:link>.</li></ol><p><span style="color:var(--ds-text,#172b4d);">The evaluation results are displayed in the </span><strong>SysML v2 Model Evaluation</strong><span style="color:var(--ds-text,#172b4d);"><span> </span>console.</span></p>
````

<!--NOMAGIC_PAGE id=249577962 space=SYSML2EP version=41 -->
## PAGE 00049: Manipulating runtime values

- page_id: `249577962`
- space_key: `SYSML2EP`
- source_url: https://docs.nomagic.com/spaces/SYSML2EP/pages/249577962/Manipulating+runtime+values
- version_number: 41
- version_date: `2026-05-27T10:06:01.254+02:00`
- ancestors: SysML v2 Evaluation Plugin Documentation > User guide > Evaluation information in views
- labels: []

### NORMALIZED CONTENT

##### Entering and modifying initial runtime values

You can use views to enter new and modify existing initial runtime values during evaluation. When an initial runtime value is changed or entered, all evaluation results are automatically recalculated and requirements are reverified.

During runtime, you can modify only initial values indicated by the ":=" sign, which means they are not bound and can be adjusted for evaluation purposes.

To enter or modify an initial runtime value

1. Open a view and, in the view toolbar, click [ATTACHMENT filename='evaluate_button.png'] to evaluate it. To evaluate only a specific element in a view, select the element shape (press and hold the Shift key to select multiple shapes), then click [IMAGE alt='' src='']. Only the selected elements will be reevaluated after changing an initial runtime value.
2. Select the shape of the element whose value you want to enter or change and type a new value. Editable attributes are indicated by the ":=" sign. 
[IMAGE alt='' src='']
3. Press Enter or click anywhere in the view to enter the change.

After an initial runtime value is entered or changed, all bound expressions and invocations are automatically recalculated. If an expression or invocation is an initial value, it is only calculated during the first evaluation and will not be recalculated afterwards.

#### PANEL: Example

Example

attributea:=1;//'a' is an initial value that can be changed during runtime. 
attributeb=a*2;//'b' is a bound expression calculated during the initial evaluation (equals 2) and recalculated each time 'a' is changed. 
attributec:=b;//'c' is an initial expression calculated only during the initial evaluation (equals 2) and not recalculated at runtime (even if 'b' changes). However, 'c' can be changed during runtime.

##### Saving runtime values to the model

After using model views to enter or modify initial runtime values, you can save these values to the model as described below.

You can not use model views to save modified values of inherited attributes. Only directly owned or redefined attribute values can be saved to the model.

To save runtime values to the model

1. In the view with new or modified runtime values, do one of the following:
  - To save all modified values, click the arrow next to [ATTACHMENT filename='evaluate_button.png'] in the view toolbar and select Save Modified Values to Model . If you have selected any attribute shapes with modified values in the view, only the selected values are saved. [IMAGE alt='' src='']
  - To save the selected modified values, right-click the selected attribute shapes and select Save Modified Values to Model . You can select multiple shapes by pressing and holding the **Shift** key.
  - To save a single selected modified value, click [ATTACHMENT filename='save_modified_values_to_model.png'] in the smart manipulator of the selected attribute shape. [ATTACHMENT filename='saving_single_modified_value.png']

##### Recalculating bound values manually

When an initial runtime value is entered or changed during evaluation, all bound values are automatically recalculated, and requirements are reverified. However, this behavior can be changed by disabling the automatic bound value recalculation in the Project Options as described below.

To disable or enable bound value recalculation

1. In the main menu, go to Options > Project .
2. In the Project Options dialog, select Evaluation .
3. On the right side of the dialog, set the Auto Recalculate Bound Values option to false or true (default) to disable or enable the automatic bound value recalculation. [ATTACHMENT filename='auto_recalculate_bound_values_option.png']
4. Click OK to close the dialog.

To recalculate the evaluation results manually

- Do one of the following:
  - In the view toolbar, click [ATTACHMENT filename='evaluate_button.png'] .
  - In the view toolbar, click the arrow next to [ATTACHMENT filename='evaluate_button.png'] and select Refresh .
  - Select any shape in the view and, in the smart manipulator, click [ATTACHMENT filename='evaluate_button.png'] .
  - Right-click any shape in the view and select Evaluate .

When invoking recalculation from a specific element shape, all of the evaluation results in the view are recalculated.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<h3><span>Entering and modifying initial runtime values</span></h3><p><span>You can use views to enter new and modify existing initial runtime values during evaluation. When an initial runtime value is changed or entered, all evaluation results are automatically recalculated and requirements are reverified.</span></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="ee2a8342-af11-4191-b472-0599c88c7e22"><ac:rich-text-body><p><span> During runtime, you can modify only initial values indicated by the &quot;:=&quot; sign, which means they are not bound and can be adjusted for evaluation purposes.</span></p></ac:rich-text-body></ac:structured-macro><p>To enter or modify an initial runtime value</p><hr /><ol><li data-uuid="91225f39-b90e-43a0-b687-d36d541707f4">Open a view and, in the view toolbar, click <ac:image ac:thumbnail="true" ac:height="14"><ri:attachment ri:filename="evaluate_button.png" /></ac:image> to evaluate it.<br /><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="5d95554f-2cbb-4aef-9064-73393c7c7eab"><ac:rich-text-body><p>To evaluate only a specific element in a view, select the element shape (press and hold the Shift key to select multiple shapes), then click <ac:image ac:thumbnail="true" ac:height="14"><ri:attachment ri:filename="evaluate_button.png" /></ac:image>. Only the selected elements will be reevaluated after changing an initial runtime value.</p></ac:rich-text-body></ac:structured-macro></li><li data-uuid="4df8633a-4210-48d5-b492-df4ba57cc6f4">Select the shape of the element whose value you want to enter or change and type a new value. Editable <span>attributes are indicated by the &quot;:=&quot; sign.<br /><ac:image><ri:attachment ri:filename="editing_runtime_values.png" /></ac:image></span></li><li data-uuid="33d6cfe6-7227-47fb-a176-39c9e488af01"><span>Press Enter or click anywhere in the view to enter the change.</span></li></ol><p><span>After an initial runtime value is entered or changed, all bound expressions and invocations are automatically recalculated. I<span style="color:var(--ds-text,#172b4d);">f an expression or invocation is an initial value, it is only calculated during the first evaluation and will not be recalculated afterwards.</span></span></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="32cf2c6b-ac6d-4788-af7e-27d09056b017"><ac:parameter ac:name="title">Example</ac:parameter><ac:rich-text-body><p><span style="color:var(--ds-text-accent-blue,#0055cc);">attribute</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">a</span><span style="color:var(--ds-text,#000000);"> := </span><span style="color:var(--ds-background-accent-green-bolder,#1f845a);">1</span><span style="color:var(--ds-text,#000000);">; </span><span style="color:var(--ds-text-accent-green-bolder,#164b35);">//'a' is an initial value that can be changed during runtime.</span><br /><span style="color:var(--ds-text-accent-blue,#0055cc);">attribute</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">b</span><span style="color:var(--ds-text,#000000);"> = </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">a</span><span style="color:var(--ds-text,#000000);"> * </span><span style="color:var(--ds-background-accent-green-bolder,#1f845a);">2</span><span style="color:var(--ds-text,#000000);">; </span><span style="color:var(--ds-text-accent-green-bolder,#164b35);">//'b' is a bound expression calculated during the initial evaluation (equals 2) and recalculated each time 'a' is changed.</span><br /><span style="color:var(--ds-text-accent-blue,#0055cc);">attribute</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">c</span><span style="color:var(--ds-text,#000000);"> := </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">b</span><span style="color:var(--ds-text,#000000);">; </span><span style="color:var(--ds-text-accent-green-bolder,#164b35);">//'c' is an initial expression calculated only during the initial evaluation (equals 2) and not recalculated at runtime (even if 'b' changes). However, 'c' can be changed during runtime.</span></p></ac:rich-text-body></ac:structured-macro><h3>Saving runtime values to the model</h3><p style="text-align: left;">After using model views to enter or modify initial runtime values, you can save these values to the model as described below.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="84dfc085-0aca-4a85-a0dc-2d74d457ff90"><ac:rich-text-body><p><span>You can not use model views to save modified values of inherited attributes. Only directly owned or redefined attribute values can be saved to the model.</span></p></ac:rich-text-body></ac:structured-macro><p style="text-align: left;"><br /></p><p style="text-align: left;">To save runtime values to the model</p><hr /><ol><li style="text-align: left;" data-uuid="347f645e-8f50-4fc7-94e5-da374198013c">In the view with new or modified runtime values, do one of the following:<ul><li style="text-align: left;" data-uuid="989ead07-669a-44f3-9f66-6cc86073992c">To save all modified values, click the arrow next to <ac:image ac:thumbnail="true" ac:height="14"><ri:attachment ri:filename="evaluate_button.png" /></ac:image> in the view toolbar and select <strong>Save Modified Values to Model</strong>.<br /><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="16fabaf7-91ff-48ac-938d-3d28a84d663c"><ac:rich-text-body><p>If you have selected any attribute shapes with modified values in the view, only the selected values are saved.</p></ac:rich-text-body></ac:structured-macro><strong><ac:image><ri:attachment ri:filename="saving_all_modified_values.png" /></ac:image></strong></li><li style="text-align: left;" data-uuid="b6328fe2-20af-45ab-b540-fbff75a5712f">To save the selected modified values, right-click the selected attribute shapes and select <strong>Save Modified Values to Model</strong>.<br /><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="9ae9084d-e7e8-4123-858d-99d972918865"><ac:rich-text-body><p>You can select multiple shapes by pressing and holding the <strong>Shift</strong> key.</p></ac:rich-text-body></ac:structured-macro></li><li style="text-align: left;" data-uuid="a7fdec93-b08f-4c5d-bc7b-ab7a80fb9c55">To save a single selected modified value, click <ac:image><ri:attachment ri:filename="save_modified_values_to_model.png" /></ac:image> in the smart manipulator of the selected attribute shape.<br /><ac:image><ri:attachment ri:filename="saving_single_modified_value.png" /></ac:image></li></ul></li></ol><h3>Recalculating bound values manually</h3><p><span style="color:var(--ds-text,#172b4d);">When an initial runtime value is entered or changed during evaluation, all bound values are automatically recalculated, and requirements are reverified. However, this behavior can be changed by disabling the automatic bound value recalculation in the Project Options as described below.</span></p><p><span style="color:var(--ds-text,#172b4d);">To disable or enable bound value recalculation</span></p><hr /><ol><li data-uuid="38b3bb75-13ff-40e4-8ab9-3df0e523aa3b">In the main menu, go to <strong>Options</strong> &gt; <strong>Project</strong>.</li><li data-uuid="a0e7028b-0d16-4092-bc44-c8cd15ae8aa0">In the <strong>Project Options</strong> dialog, select <strong>Evaluation</strong>.</li><li data-uuid="b3c24023-6bc6-495a-a82c-3f81a81a1faf">On the right side of the dialog, set the <strong>Auto Recalculate Bound Values</strong> option to <em>false</em> or <em>true</em> (default) to disable or enable the automatic bound value recalculation.<br /><ac:image><ri:attachment ri:filename="auto_recalculate_bound_values_option.png" /></ac:image></li><li data-uuid="bbfb2ae5-ae56-4542-aa68-463b0887e512">Click <strong>OK</strong> to close the dialog.</li></ol><p><br />To recalculate the evaluation results manually</p><hr /><ul><li data-uuid="7cc29ad6-1196-4ee0-ad6b-e5ba3b2dccbe">Do one of the following:<ul><li data-uuid="3f7b35a0-4452-4449-a2ce-cfe8909d78e6">In the view toolbar, click <ac:image ac:thumbnail="true" ac:height="14"><ri:attachment ri:filename="evaluate_button.png" /></ac:image>.</li><li data-uuid="66c1ee57-f974-4122-a370-13010b0a69f8">In the view toolbar, click the arrow next to <ac:image ac:thumbnail="true" ac:height="14"><ri:attachment ri:filename="evaluate_button.png" /></ac:image> and select <strong>Refresh</strong>.</li><li data-uuid="51bfcd4c-fdd6-487c-8452-e71f6744e136">Select any shape in the view and, in the smart manipulator, click <ac:image ac:thumbnail="true" ac:height="14"><ri:attachment ri:filename="evaluate_button.png" /></ac:image>.</li><li data-uuid="008568e1-c44d-4140-afbe-d4eac412eebf">Right-click any shape in the view and select <strong>Evaluate</strong>.</li></ul></li></ul><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="39d660b6-3884-4ee5-88da-bdd541a57c75"><ac:rich-text-body><p>When invoking recalculation from a specific element shape, all of the evaluation results in the view are recalculated.</p></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=249577938 space=SYSML2EP version=5 -->
## PAGE 00050: Prerequisites

- page_id: `249577938`
- space_key: `SYSML2EP`
- source_url: https://docs.nomagic.com/spaces/SYSML2EP/pages/249577938/Prerequisites
- version_number: 5
- version_date: `2026-04-01T12:20:34.813+02:00`
- ancestors: SysML v2 Evaluation Plugin Documentation
- labels: []

### NORMALIZED CONTENT

To work with SysML v2 features, including model evaluation, the following software must be installed:

- One of the following CATIA Magic/No Magic modeling tools:
  - Cameo Systems Modeler (Enterprise Edition only)
  - Cameo Enterprise Architecture
  - Magic Cyber Systems Engineer
  - Magic Systems of Systems Architect
- The SysML v1 Plugin.
- Cameo Requirements Modeler.
- Cameo Simulation Toolkit or Magic Model Analyst.
- The SysML v2 Plugin. It provides the majority of the SysML v2 features, including the Textual Editor.
- The SysML v2 Evaluation Plugin. It allows you to conduct static evaluations of SysML v2 models (mathematical calculations, calculation usage evaluation, constraints evaluation, and requirements evaluation).

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>To work with SysML v2 features, including model evaluation, the following software must be installed:</p><ul><li data-uuid="c69be92d-d004-46d5-a2ee-c2ceb367ddc4"><span style="color:var(--ds-text,#172b4d);">One of the following CATIA Magic/No Magic modeling tools:</span><ul><li>Cameo Systems Modeler (Enterprise Edition only)</li><li>Cameo Enterprise Architecture</li><li>Magic Cyber Systems Engineer</li><li>Magic Systems of Systems Architect</li></ul></li><li>The SysML v1 Plugin.</li><li>Cameo Requirements Modeler.</li><li>Cameo Simulation Toolkit or Magic Model Analyst.</li><li>The SysML v2 Plugin. It provides the majority of the SysML v2 features, including the Textual Editor.</li><li><p class="auto-cursor-target"><span>The SysML v2 Evaluation Plugin. It allows you to conduct static evaluations of SysML v2 models (mathematical calculations, calculation usage evaluation, constraints evaluation, and requirements evaluation).</span></p></li></ul>
````

<!--NOMAGIC_PAGE id=304015464 space=SYSML2EP version=4 -->
## PAGE 00051: Project options

- page_id: `304015464`
- space_key: `SYSML2EP`
- source_url: https://docs.nomagic.com/spaces/SYSML2EP/pages/304015464/Project+options
- version_number: 4
- version_date: `2026-05-06T14:08:09.706+02:00`
- ancestors: SysML v2 Evaluation Plugin Documentation
- labels: []

### NORMALIZED CONTENT

Use the**Project Options**dialog to specify project-specific options.Thedialog includes option groups, each designated for specific features. You can find the evaluation-related project options under the **Evaluation** option group.

[IMAGE alt='' src='']

###### The Project Options dialog

##### Modifying evaluation project options

To modify evaluation-related project options

1. In the main menu, select Options > Project .
2. In the Project Options dialog, select the Evaluation option group.
3. In the option list, click the value cell for the option you want to change, then enter or select the new value.
4. Click OK to close the dialog.

##### Evaluation project options

The following table describes evaluation-related project options.

| Option name | Description |
| --- | --- |
| Display Verification Results As | Select the method to visualize requirements and constraint verification results in views. Select Paint Headers to color shape headers. Select Display Icons to add icons to shape headers. |
| Propagate Deep Nested Failures | Set to true to indicate deep nested requirement and constraint failures on part shapes. Set to false if you want shapes to be highlighted only when they directly fail a requirement or constraint. |
| Autorecalculate Bound Values | Set to true to automatically recalculate bound values when an initial value is changed. Set to false to initiate recalculation by clicking Refresh or Evaluate. |
| External Script Engine Libraries | Add the external library files that will be loaded into the script engine. To add a file, select the option value cell, click , click the Add button in the open dialog, and select the file you want to add. |
| Maximum recursion Depth | Specify the maximum number of times a feature can be re-evaluated recursively before the recursion error is triggered. |

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><span style="color:var(--ds-text,#172b4d);">Use the<span> </span></span><strong style="text-align: left;">Project Options</strong><span style="color:var(--ds-text,#172b4d);"><span> </span>dialog to s</span><span style="color:var(--ds-text,#172b4d);">pecify project-specific options.<span> </span></span><span style="color:var(--ds-text,#172b4d);">The </span><span style="color:var(--ds-text,#172b4d);">dialog includes option groups, each designated for specific features. You can find the evaluation-related project options under the <strong>Evaluation</strong> option group.</span></p><p style="text-align: center;"><span style="color:var(--ds-text,#172b4d);"><ac:image><ri:attachment ri:filename="project_options.png" /></ac:image></span></p><h6 style="text-align: center;"><span style="color:var(--ds-text,#172b4d);">The Project Options dialog</span></h6><h3><span style="color:var(--ds-text,#172b4d);">Modifying evaluation project options</span></h3><p><span style="color:var(--ds-text,#172b4d);">To modify evaluation-related project options</span></p><hr /><ol><li data-uuid="8f7725cd-259f-471f-b215-3945d56c7552">In the main menu, select <strong>Options</strong> &gt; <strong>Project</strong>.</li><li data-uuid="d03ea0bd-17a0-46c5-a2e5-6a4d580f6622">In the <strong>Project Options</strong> dialog, select the <strong>Evaluation</strong> option group.</li><li data-uuid="10b81531-bda4-4578-bac9-4870008c5cd6">In the option list, click the value cell for the option you want to change, then enter or select the new value.</li><li data-uuid="bd131ad3-bc72-481a-bedd-323cdbbaf8c9">Click <strong>OK</strong> to close the dialog.</li></ol><h3>Evaluation project options</h3><p>The following table describes evaluation-related project options.</p><table><colgroup><col /><col /></colgroup><tbody><tr><th scope="col">Option name</th><th scope="col">Description</th></tr><tr><td><strong>Display Verification Results As</strong></td><td>Select the method to visualize requirements and constraint verification results in views. Select <strong>Paint Headers</strong> to color shape headers. Select <strong>Display Icons</strong> to add icons to shape headers. </td></tr><tr><td><strong>Propagate Deep Nested Failures</strong></td><td>Set to <em>true</em> to indicate deep nested requirement and constraint failures on part shapes. Set to <em>false</em> if you want shapes to be highlighted only when they directly fail a requirement or constraint.</td></tr><tr><td><strong>Autorecalculate Bound Values</strong></td><td>Set to <em>true</em> to automatically recalculate bound values when an initial value is changed. Set to <em>false</em> to initiate recalculation by clicking <strong>Refresh</strong> or <strong>Evaluate</strong>.</td></tr><tr><td><strong>External Script Engine Libraries</strong></td><td><div class="content-wrapper"><p>Add the external library files that will be loaded into the script engine. To add a file, select the option value cell, click <ac:image><ri:attachment ri:filename="edit_button.png" /></ac:image>, click the <strong>Add</strong> button in the open dialog, and select the file you want to add.</p></div></td></tr><tr><td><strong>Maximum recursion Depth</strong></td><td>Specify the maximum number of times a feature can be re-evaluated recursively before the recursion error is triggered.</td></tr></tbody></table>
````

<!--NOMAGIC_PAGE id=249577939 space=SYSML2EP version=6 -->
## PAGE 00052: Samples and libraries

- page_id: `249577939`
- space_key: `SYSML2EP`
- source_url: https://docs.nomagic.com/spaces/SYSML2EP/pages/249577939/Samples+and+libraries
- version_number: 6
- version_date: `2026-05-06T10:24:33.311+02:00`
- ancestors: SysML v2 Evaluation Plugin Documentation
- labels: []

### NORMALIZED CONTENT

##### Samples

To get started, review the SysML v2 project samples provided with the installation, found at:

- <modeling tool installation directory>\samples\SysML v2\Evaluation

##### Libraries

Each SysML v2 project is automatically loaded with used projects:

- Standard Libraries. It contains standard SysML v2 libraries.
- 3DS SysML Customization. It contains concepts designed for view creation and symbol styles customization.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<h3>Samples</h3><p>To get started, review the SysML v2 project samples provided with the installation, found at:</p><ul><li><em style="text-align: left;">&lt;modeling tool installation directory&gt;\samples\SysML v2\Evaluation</em><em style="text-align: left;"><br /></em></li></ul><h3>Libraries</h3><p>Each SysML v2 project is automatically loaded with used projects:</p><ul><li><em>Standard Libraries.</em> It contains standard SysML v2 libraries.</li><li><em>3DS SysML Customization. </em>It contains concepts designed for view creation and symbol styles customization.<em><br /></em></li></ul>
````

<!--NOMAGIC_PAGE id=249578007 space=SYSML2EP version=2 -->
## PAGE 00053: Server-side evaluation

- page_id: `249578007`
- space_key: `SYSML2EP`
- source_url: https://docs.nomagic.com/spaces/SYSML2EP/pages/249578007/Server-side+evaluation
- version_number: 2
- version_date: `2026-01-26T10:52:23.938+01:00`
- ancestors: SysML v2 Evaluation Plugin Documentation > User guide
- labels: []

### NORMALIZED CONTENT

If you work with Teamwork Cloud projects, you can evaluate them on the server byusing the REST API or thePython client (pyEval.zip).

Server-side evaluation is available only with the Teamwork Cloud Enterprise license.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>If you work with Teamwork Cloud projects, you can evaluate them on the server by<span style="letter-spacing: 0.0px;"> using the REST API or the</span><span style="letter-spacing: 0.0px;"> Python client (<ac:inline-comment-marker ac:ref="24822121-cd71-4013-9b75-cf4d77db78fe"><span style="color:var(--ds-text,#172b4d);">pyEval.zip</span></ac:inline-comment-marker>).<br /></span></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="ba65ec8a-8cd1-4d8d-a0d4-0a1b397639ec"><ac:rich-text-body><p>Server-side evaluation is available only with the Teamwork Cloud Enterprise license.</p></ac:rich-text-body></ac:structured-macro><p><span style="color:var(--ds-text,#172b4d);"><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="8a64d399-3fd0-4bfd-9138-4a6175057396" /></span></p>
````

<!--NOMAGIC_PAGE id=249577923 space=SYSML2EP version=11 -->
## PAGE 00054: SysML v2 Evaluation Plugin Documentation

- page_id: `249577923`
- space_key: `SYSML2EP`
- source_url: https://docs.nomagic.com/spaces/SYSML2EP/pages/249577923/SysML+v2+Evaluation+Plugin+Documentation
- version_number: 11
- version_date: `2026-06-16T09:19:03.542+02:00`
- ancestors: 
- labels: []

### NORMALIZED CONTENT

lightgrey

This guide provides documentation for the SysML v2 Evaluation Plugin.

SysML v2 is a next-generation systems modeling language. Compared to SysML v1, SysML v2 aims to offer improved precision, expressiveness, and usability.

To fully take advantage of SysML v2, two primary plugins are available for you:

- The SysML v2 Plugin provides core SysML v2 features and includes the SysML v2 Textual Editor, enabling you to model using both textual and graphical notations.
- The SysML v2 Evaluation Plugin allows you to conduct static evaluations of SysML v2 models.

For more information, please see the [CONFLUENCE_PAGE title='Prerequisites' space=''] page.

The following topics explain how to install and use the SysML v2 Evaluation Plugin:

2

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="10aa203c-7173-4219-ab58-f6619359c634"><ac:parameter ac:name="bgColor">lightgrey</ac:parameter><ac:rich-text-body><p><span style="color:var(--ds-text,#172b4d);">This guide provides documentation for the SysML v2 Evaluation Plugin.</span></p></ac:rich-text-body></ac:structured-macro><p>SysML v2 is a next-generation systems modeling language. Compared to SysML v1, SysML v2 aims to offer improved precision, expressiveness, and usability.</p><p>To fully take advantage of SysML v2, two primary plugins are available for you:</p><ul><li><a href="https://docs.nomagic.com/SYSML2P/?contextKey=sysml-v2-plugin-documentation&amp;version=latest">The SysML v2 Plugin</a> provides core SysML v2 features and includes the SysML v2 Textual Editor, enabling you to model using both textual and graphical notations.</li><li>The SysML v2 Evaluation Plugin allows you to conduct static evaluations of SysML v2 models.</li></ul><p>For more information, please see the <ac:link><ri:page ri:content-title="Prerequisites" /></ac:link> page.</p><p>The following topics explain how to install and use the SysML v2 Evaluation Plugin:</p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="9a83306a-dc0b-4b64-8374-382275e8d7c5"><ac:parameter ac:name="depth">2</ac:parameter></ac:structured-macro></p><p><br /></p>
````

<!--NOMAGIC_PAGE id=249577940 space=SYSML2EP version=7 -->
## PAGE 00055: User guide

- page_id: `249577940`
- space_key: `SYSML2EP`
- source_url: https://docs.nomagic.com/spaces/SYSML2EP/pages/249577940/User+guide
- version_number: 7
- version_date: `2026-04-01T12:39:58.418+02:00`
- ancestors: SysML v2 Evaluation Plugin Documentation
- labels: []

### NORMALIZED CONTENT

The SysML v2 Evaluation Plugin user guide explains how to conduct static evaluations of SysML v2 models.

For information about generic SysML v2 modeling features, including using the textual notation, see the [SysML v2 Plugin documentation](https://docs.nomagic.com/SYSML2P/?contextKey=sysml-v2-plugin-documentation&version=latest).

To learn more, see the following topics:

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>The SysML v2 Evaluation Plugin user guide explains how to conduct static evaluations of SysML v2 models.</p><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="f0f8e034-bdef-4bad-9db3-36961de8057f"><ac:rich-text-body><p>For information about generic SysML v2 modeling features, including using the textual notation, see the <a href="https://docs.nomagic.com/SYSML2P/?contextKey=sysml-v2-plugin-documentation&amp;version=latest">SysML v2 Plugin documentation</a>.</p></ac:rich-text-body></ac:structured-macro><p> To learn more, see the following topics:</p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="1d052ab0-6a12-44f2-a374-967d5273613b" /></p>
````

<!--NOMAGIC_PAGE id=285048927 space=SYSML2EP version=8 -->
## PAGE 00056: Using interactive HTML table

- page_id: `285048927`
- space_key: `SYSML2EP`
- source_url: https://docs.nomagic.com/spaces/SYSML2EP/pages/285048927/Using+interactive+HTML+table
- version_number: 8
- version_date: `2026-01-19T09:20:29.902+01:00`
- ancestors: SysML v2 Evaluation Plugin Documentation > User guide > Server-side evaluation
- labels: []

### NORMALIZED CONTENT

You can use [CONFLUENCE_PAGE title='Evaluation using REST API' space=''] or [CONFLUENCE_PAGE title='Evaluation using Jupyter Notebook' space=''] to open and modify an interactive HTML table that dynamically retrieves data based on the specified context, parameters, and/or expressions.

[IMAGE alt='' src='']

###### An interactive HTML table

##### Editing values

In an HTML table, you can edit initial values, as described below.

- Only initial values can be edited.
- Non-editable values are shown in italic font for easier identification.

To edit initial values

1. Click the Value cell you want to edit.
2. Change the value.
3. Click anywhere on the table page to save the value.

##### Adding new rows

To add a new table row

1. In the top right corner of the table page, click [ATTACHMENT filename='add_row.png'] to add a new row at the bottom of the table.
2. Click the Name and Value cells of the new row and enter the desired property name and value.

##### Reordering rows

To change the position of a table row

1. Hover the mouse pointer over a table row to see available action icons.
2. Click and hold [ATTACHMENT filename='drag_to_reorder.png'] .
3. Drag and drop the row to a new position. [ATTACHMENT filename='reordering_rows.png']

##### Deleting rows

To delete a table row

1. Hover the mouse pointer over a table row to see available action icons.
2. Click [ATTACHMENT filename='delete_row.png'] to delete the row.

##### Exporting data

You can export HTML table data to the PNG, CSV, and JSON formats.

To export table data

- In the top right corner of the table page, click [ATTACHMENT filename='export_table.png'] and select the format you want to export to.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><span style="color:var(--ds-text,#172b4d);">You can use <ac:link><ri:page ri:content-title="Evaluation using REST API" /><ac:plain-text-link-body><![CDATA[REST API]]></ac:plain-text-link-body></ac:link> or <ac:link><ri:page ri:content-title="Evaluation using Jupyter Notebook" /><ac:plain-text-link-body><![CDATA[Jupyter Notebook]]></ac:plain-text-link-body></ac:link> to open and modify an interactive HTML table that dynamically retrieves data based on the specified context, parameters, and/or expressions.</span></p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="interactive_html_table.png" /></ac:image></p><h6 style="text-align: center;">An interactive HTML table</h6><h3>Editing values</h3><p>In an HTML table, you can edit initial values, as described below.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="76aefc83-3d0f-4ae0-bbe6-162cecceff80"><ac:rich-text-body><ul><li data-uuid="ca56cbae-a2c6-49a4-a951-0ef751c67482">Only initial values can be edited.</li><li data-uuid="5b1e874e-9fbf-4ef8-9f9c-0e3a0c93c4d0">Non-editable values are shown in italic font for easier identification.</li></ul></ac:rich-text-body></ac:structured-macro><p>To edit initial values</p><hr /><ol><li data-uuid="2ea41a37-2bfb-4b11-b578-c67f0f88e8a4">Click the <strong>Value</strong> cell you want to edit.</li><li data-uuid="65d38620-9b60-402c-b8d6-420fff571066">Change the value.</li><li data-uuid="2cd1e1c1-8b20-4169-8de7-a9f28c64950b">Click anywhere on the table page to save the value.</li></ol><h3>Adding new rows</h3><p>To add a new table row</p><hr /><ol><li data-uuid="c936246a-3d08-41d4-b2f6-7194e2826d9c">In the top right corner of the table page, click <ac:image><ri:attachment ri:filename="add_row.png" /></ac:image> to add a new row at the bottom of the table.</li><li data-uuid="559cef5d-7f41-4bfa-9664-0be5ff3f0668">Click the <strong>Name</strong> and <strong>Value</strong> cells of the new row and enter the desired property name and value.</li></ol><h3>Reordering rows</h3><p>To change the position of a table row</p><hr /><ol><li data-uuid="5468d510-837e-4c9c-bfb8-23c6491ee34f">Hover the mouse pointer over a table row to see available action icons.</li><li data-uuid="69c81157-5a1c-4607-ad0f-c45903a9a714">Click and hold <ac:image><ri:attachment ri:filename="drag_to_reorder.png" /></ac:image>.</li><li data-uuid="2a26e1e2-a6ed-427d-8a5e-906fa4efce57">Drag and drop the row to a new position.<br /><ac:image><ri:attachment ri:filename="reordering_rows.png" /></ac:image></li></ol><h3>Deleting rows</h3><p>To delete a table row</p><hr /><ol><li data-uuid="69049473-a60c-4b0d-b5e2-2c225ae4c45e">Hover the mouse pointer over a table row to see available action icons.</li><li data-uuid="23f04ada-7943-4654-ba09-12119b274af1">Click <ac:image ac:thumbnail="true" ac:height="14"><ri:attachment ri:filename="delete_row.png" /></ac:image> to delete the row.</li></ol><h3>Exporting data</h3><p>You can export HTML table data to the PNG, CSV, and JSON formats.</p><p>To export table data</p><hr /><ul><li data-uuid="728ffb95-3107-4839-b29c-93d5577c60b0">In the top right corner of the table page, click <ac:image ac:thumbnail="true" ac:height="22"><ri:attachment ri:filename="export_table.png" /></ac:image> and select the format you want to export to.</li></ul>
````

<!--NOMAGIC_PAGE id=309365882 space=SYSML2EP version=26 -->
## PAGE 00057: Using textual representation

- page_id: `309365882`
- space_key: `SYSML2EP`
- source_url: https://docs.nomagic.com/spaces/SYSML2EP/pages/309365882/Using+textual+representation
- version_number: 26
- version_date: `2026-06-18T13:50:22.781+02:00`
- ancestors: SysML v2 Evaluation Plugin Documentation > User guide
- labels: []

### NORMALIZED CONTENT

A textual representation element provides a representation of a model element in a specified language. A textual representation identifies the language of the representation and contains the corresponding text body. The language may be a natural language or a machine-readable language.

Textual representations can be used to associate model elements with language-specific content such as scripts, expressions, analysis artifacts, or other textual definitions.

Supported languages include:

- JavaScript
- Groovy
- Beanshell
- Python (via Jython)
- MATLAB

#### NOTE: Using MATLAB

Using MATLAB

To evaluate scripts defined in the MATLAB syntax:

- [CONFLUENCE_PAGE title='Integration with MATLAB' space=''] .
- The language must be specified as "MATLAB" (case sensitive).

When a textual representation is used for script execution, script inputs and outputs are typically primitive values (Boolean, Integer, Real, and String). Evaluated structured model elements, such as parts, can also be provided as inputs. You can access their feature values by using the get method described below. In Groovy scripts, nested feature values can also be accessed using dot notation.

#### TIP: Printing output from scripts

Printing output from scripts

Evaluated scripts in all supported languages can print messages to the**SysML v2 Model Evaluation**console using the print method. Each call to print outputs a separate line in the console.

calcdefListCalc{ 
/* Calc prints to console and returns null output */ 
innumericalList[*] :Real; 
return:Real; 
repmyScriptlanguage"Python"/* print(numericalList[1]) */

##### Accessing structured model elements in scripts

In addition to primitive values, a script can receive an evaluated structured model element (for example, a part) as input. To access feature values from the structured element, use the get method:

#### PANEL: Example

Example

vehicle.get("grossMass")

The method returns the evaluated value of the specified feature. For example, if *vehicle* is a part and *grossMass* evaluates to a real value, the expression in the above example returns the numerical value of *grossMass*.

#### NOTE: Using Groovy

Using Groovy

When using Groovy, nested feature values can be accessed via dot notation in addition to the get method, for example:

calcdefArea{ 
inmyInput:> Vehicle::pad; 
return:Real;repmyScriptlanguage"Groovy" 
/* myInput.centerLength * myInput.width */

##### Textual representations in calculations

When specifying the return value of a calculation, you can use a textual representation to evaluate a script written in a supported scripting language.

The following example uses a Beanshell script to calculate an area from the supplied inputs:

#### PANEL: Example

Example

calcdefArea15{ 
inlength:Real; 
inwidth:Real; 
returnresult:Real; 
language"beanshell"/* result=length * width */

}

When the calculation is evaluated, the script receives the calculation inputs as variables and assigns the computed value to the return parameter.

##### Textual representations in actions

When defining an action, you can use a textual representation to implement the action's behavior using an external scripting language. Action parameters are exposed to the script and can be read or updated according to their direction (in, out, or inout).

#### PANEL: Example

Example

actiondefcounter{ 
inoutcount:Real:=0; 
language"groovy"/* count=count+1 */} 
} 
attributestartCount: Integer = counter().count//The result will be 1 because there is no input 
attributecontinueCount: Integer = counter(startCount).count//The result will be 2. Input overrides the initial value set in the parameter.

###### Invoking external tools via ToolExecution

Actions support "ToolExecution", which allows SysML v2 features to be mapped to variables used by MATLAB scripts. This is particularly useful when the variable names used in the model differ from those expected by the external script.

The following example executes a MATLAB script and maps model features to MATLAB variables using "ToolVariable"annotations:

#### PANEL: Example

Example

actioncomputeStoppingDistance { 
privateimportAnalysisTooling::*; 
@ToolExecution { 
:>> toolName ="MATLAB"; 
:>> uri ="run('C:/custom/path/to/StoppingAnalysisExec.m')"; 
} 
inmass : Real = vehicle.grossMass{@ToolVariable { name ="m"; }}; 
inspeed : Real = vehicle.speed{@ToolVariable { name ="v0"; }}; 
outDistance : Real = vehicle.stoppingDistance {@ToolVariable { name ="stoppingDistance"; }}; 
outkineticEnergy : Real = vehicle.kineticEnergy {@ToolVariable { name ="e"; }};

##### Textual representations in constraints

You can use a textual representation to define constraint logic in both requirements and standalone constraints using a supported scripting language. When a simple constraint (assert constraint) is evaluated, all attributes of the constraint’s owner are available in the script as variables. You can use them directly without qualification. You can also access nested structures using the get method (and dot notation in Groovy).

###### Standalone constraints

In a standalone constraint, attributes defined within the constraint are directly available in the script.

#### PANEL: Example

Example

assertconstraint{ 
attributemaxValue:Integer=5; 
attributecurrentValue:Integer=3; 
language"Groovy"/* currentValue < maxValue */ 
}

###### Constraints in parts

When a constraint is defined directly under a part, all attributes of the part are available in the script.

#### PANEL: Example

Example

partvehicle{ 
attributemaxSpeed:Integer=100; 
attributecurrentSpeed:Integer=100;satisfyspeedReqbythis; 
 
assertnotconstraint{ 
language"groovy"/* currentSpeed == maxSpeed */ 
} 
}

###### Constraints in requirements

When a constraint is used inside a requirement, the requirement subject is made available to the script engine as the root context for evaluation. This means that the subject and its structure are directly accessible in the script engine.

#### PANEL: Example

Example

requirementspeedReq{ 
subjectvehiclev :>vehicle;requireconstraint{ 
language"groovy"/* v.currentSpeed < vehicle.maxSpeed */ 
} 
}

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="isSelectedEnd"><span>A textual representation element provides a representation of a model element in a specified language. A textual representation identifies the language of the representation and contains the corresponding text body. The language may be a natural language or a machine-readable language.</span></p><p class="isSelectedEnd"><span>Textual representations can be used to associate model elements with language-specific content such as scripts, expressions, analysis artifacts, or other textual definitions.</span></p><p class="isSelectedEnd"><span>Supported languages include:</span></p><ul><li data-uuid="07afeeac-0975-49b5-b7ad-556354295e1f"><span>JavaScript</span></li><li data-uuid="9c7f9072-51b4-4e74-b18b-3986b2d4798f"><span>Groovy</span></li><li data-uuid="8873d9f9-af2a-4067-9aa4-80c1f17717e9"><span>Beanshell</span></li><li data-uuid="9ff9a5f8-af23-4637-a4ed-0fac62effa7e"><span>Python (via Jython)</span></li><li data-uuid="6037e39e-a85a-4621-b1a3-e23676064354"><span>MATLAB</span></li></ul><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="7112b935-00f1-4054-b9ef-71f2449b1345"><ac:parameter ac:name="title">Using MATLAB</ac:parameter><ac:rich-text-body><p>To evaluate scripts defined in the MATLAB syntax:</p><ul><li data-uuid="b21fecb0-5721-427d-b186-5eef9af91898"><ac:link><ri:page ri:content-title="Integration with MATLAB" /><ac:plain-text-link-body><![CDATA[MATLAB must be integrated with your modeling tool]]></ac:plain-text-link-body></ac:link>.</li><li data-uuid="4aa43c38-314f-4d3a-b311-5321883c7a39">The language must be specified as &quot;MATLAB&quot; (case sensitive).</li></ul></ac:rich-text-body></ac:structured-macro><p class="isSelectedEnd">When a textual representation is used for script execution, script inputs and outputs are typically primitive values (Boolean, Integer, Real, and String). Evaluated structured model elements, such as parts, can also be provided as inputs. You can access their feature values by using the get method described below. In Groovy scripts, nested feature values can also be accessed using dot notation.</p><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="6908ea7c-96c6-4375-8d00-9ab56f31c552"><ac:parameter ac:name="title">Printing output from scripts</ac:parameter><ac:rich-text-body><p>Evaluated scripts in all supported languages can print messages to <span style="color:var(--ds-text,#172b4d);">the<span> </span></span><strong style="text-align: left;">SysML v2 Model Evaluation</strong><span style="color:var(--ds-text,#172b4d);"><span> </span>console</span> using the print method. Each call to print outputs a separate line in the console.</p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="a0ce7936-639a-43c2-8b62-35dc10cd8ad9"><ac:rich-text-body><p><span style="color:var(--ds-text-accent-blue,#0055cc);">calc</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">def</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-teal,#206a83);">ListCalc</span><span style="color:var(--ds-text,#000000);"> {</span><br /><span style="color:var(--ds-text,#000000);">    </span><span style="color:var(--ds-text-accent-green-bolder,#164b35);"><ac:inline-comment-marker ac:ref="743bbb72-80d7-40ff-84aa-8e308ed61057">/* <span style="color:var(--ds-text-accent-lime,#4c6b1f);">Calc prints to console and returns null output</span>  */</ac:inline-comment-marker></span><br /><span style="color:var(--ds-text,#000000);">        </span><span style="color:var(--ds-text-accent-blue,#0055cc);">in</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">numericalList</span><span style="color:var(--ds-text,#000000);"> [*] : </span><span style="color:var(--ds-text-accent-teal,#206a83);">Real</span><span style="color:var(--ds-text,#000000);">;</span><br /><span style="color:var(--ds-text,#000000);">        </span><span style="color:var(--ds-text-accent-blue,#0055cc);">return</span><span style="color:var(--ds-text,#000000);"> : </span><span style="color:var(--ds-text-accent-teal,#206a83);">Real</span><span style="color:var(--ds-text,#000000);">;</span><br /><span style="color:var(--ds-text,#000000);">        </span><span style="color:var(--ds-text-accent-blue,#0055cc);">rep</span><span style="color:var(--ds-text,#000000);"> myScript </span><span style="color:var(--ds-text-accent-blue,#0055cc);">language</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-red,#ae2e24);">&quot;Python&quot;</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-green-bolder,#164b35);">/* print(numericalList[1]) */</span></p></ac:rich-text-body></ac:structured-macro><p><br /></p></ac:rich-text-body></ac:structured-macro><h3>Accessing structured model elements in scripts</h3><p>In addition to primitive values, a script can receive an evaluated structured model element (for example, a part) as input. To access feature values from the structured element, use the get method:</p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="3a7d7d13-8a40-40ef-a3c8-b6519f171ca6"><ac:parameter ac:name="title">Example</ac:parameter><ac:rich-text-body>vehicle.get(&quot;grossMass&quot;)</ac:rich-text-body></ac:structured-macro><p>The method returns the evaluated value of the specified feature. For example, if <em>vehicle</em> is a part and <em>grossMass</em> evaluates to a real value, the expression in the above example returns the numerical value of <em>grossMass</em>.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="08c847c4-2b82-4593-b4ac-261043efde90"><ac:parameter ac:name="title">Using Groovy</ac:parameter><ac:rich-text-body><p>When using Groovy, nested feature values can be accessed via dot notation in addition to the get method, for example:</p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="73760d45-bf16-4944-8ea6-b66a139128db"><ac:rich-text-body><p><span style="color:var(--ds-text-accent-blue,#0055cc);">calc</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">def</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-teal,#206a83);">Area</span><span style="color:var(--ds-text,#000000);"> {</span><br /><span style="color:var(--ds-text,#000000);">        </span><span style="color:var(--ds-text-accent-blue,#0055cc);">in</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">myInput</span><span style="color:var(--ds-text,#000000);"> :&gt; Vehicle::pad;</span><br /><span style="color:var(--ds-text,#000000);">        </span><span style="color:var(--ds-text-accent-blue,#0055cc);">return</span><span style="color:var(--ds-text,#000000);"> : </span><span style="color:var(--ds-text-accent-teal,#206a83);">Real</span><span style="color:var(--ds-text,#000000);">;<br /><br /></span><span style="color:var(--ds-text,#000000);">        </span><span style="color:var(--ds-text-accent-blue,#0055cc);">rep</span><span style="color:var(--ds-text,#000000);"> myScript </span><span style="color:var(--ds-text-accent-blue,#0055cc);">language</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-red,#ae2e24);">&quot;Groovy&quot;</span><br /><span style="color:var(--ds-text,#000000);">        </span><span style="color:var(--ds-text-accent-green-bolder,#164b35);">/* myInput.centerLength * myInput.width */</span></p></ac:rich-text-body></ac:structured-macro><p><br /></p></ac:rich-text-body></ac:structured-macro><h3 class="cm-content q9tKkq_readonly m-0"><span style="color:var(--ds-text,#172b4d);">Textual representations in calculations</span></h3><p class="isSelectedEnd"><span>When specifying the return value of a calculation, you can use a textual representation to evaluate a script written in a supported scripting language.</span></p><p><span>The following example uses a Beanshell script to calculate an area from the supplied inputs:</span></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="c0d6ec98-2f53-4b20-8d8e-4d37f62150b8"><ac:parameter ac:name="title">Example</ac:parameter><ac:rich-text-body><p><span style="color:var(--ds-text-accent-blue,#0055cc);">calc</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">def</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-teal,#206a83);">Area15</span><span style="color:var(--ds-text,#000000);"> {</span><br /><span style="color:var(--ds-text,#000000);">        </span><span style="color:var(--ds-text-accent-blue,#0055cc);">in</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">length</span><span style="color:var(--ds-text,#000000);"> : </span><span style="color:var(--ds-text-accent-teal,#206a83);">Real</span><span style="color:var(--ds-text,#000000);">;</span><br /><span style="color:var(--ds-text,#000000);">        </span><span style="color:var(--ds-text-accent-blue,#0055cc);">in</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">width</span><span style="color:var(--ds-text,#000000);"> : </span><span style="color:var(--ds-text-accent-teal,#206a83);">Real</span><span style="color:var(--ds-text,#000000);">;</span><br /><span style="color:var(--ds-text,#000000);">        </span><span style="color:var(--ds-text-accent-blue,#0055cc);">return</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">result</span><span style="color:var(--ds-text,#000000);"> : </span><span style="color:var(--ds-text-accent-teal,#206a83);">Real</span><span style="color:var(--ds-text,#000000);">;</span><br /><span style="color:var(--ds-text,#000000);">        </span><span style="color:var(--ds-text-accent-blue,#0055cc);">language</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-red,#ae2e24);">&quot;beanshell&quot;</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-green-bolder,#164b35);">/* result=length * width */</span></p><p><span style="color:var(--ds-text,#000000);">}</span></p></ac:rich-text-body></ac:structured-macro><p>When the calculation is evaluated, the script receives the calculation inputs as variables and assigns the computed value to the return parameter.</p><h3><span style="color:var(--ds-text,#172b4d);">Textual representations in actions</span></h3><p><span>When defining an action, you can use a textual representation to implement the action's behavior using an external scripting language. Action parameters are exposed to the script and can be read or updated according to their direction (</span>in, out, or inout<span>).</span></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="24a4616b-d53d-4636-adec-93550d92b4ee"><ac:parameter ac:name="title">Example</ac:parameter><ac:rich-text-body><p><span style="color:var(--ds-text-accent-blue,#0055cc);">action</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">def</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-teal,#206a83);">counter</span><span style="color:var(--ds-text,#000000);"> {</span><br /><span style="color:var(--ds-text,#000000);">    </span><span style="color:var(--ds-background-accent-red-bolder,#c9372c);"> </span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-background-accent-red-bolder,#c9372c);"> </span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-background-accent-red-bolder,#c9372c);"> </span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-background-accent-red-bolder,#c9372c);">  </span><span style="color:var(--ds-text-accent-blue,#0055cc);">inout</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">count</span><span style="color:var(--ds-text,#000000);"> : </span><span style="color:var(--ds-text-accent-teal,#206a83);">Real</span><span style="color:var(--ds-text,#000000);"> := </span><span style="color:var(--ds-background-accent-green-bolder,#1f845a);">0</span><span style="color:var(--ds-text,#000000);">;</span><br /><span style="color:var(--ds-text,#000000);">            </span><span style="color:var(--ds-text-accent-blue,#0055cc);">language</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-red,#ae2e24);">&quot;groovy&quot;</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-green-bolder,#164b35);">/* count=count+1 */</span><span style="color:var(--ds-text,#000000);"> } </span><br /><span style="color:var(--ds-text,#000000);">        }</span><br /><span style="color:var(--ds-text-accent-blue,#0055cc);">attribute</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">startCount</span><span style="color:var(--ds-text,#000000);"> : Integer = counter().count </span><span style="color:var(--ds-text-accent-green-bolder,#164b35);">//The result will be 1 because there is no input </span><br /><span style="color:var(--ds-text-accent-blue,#0055cc);">attribute</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">continueCount</span><span style="color:var(--ds-text,#000000);"> : Integer = counter(</span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">startCount</span><span style="color:var(--ds-text,#000000);">).count </span><span style="color:var(--ds-text-accent-green-bolder,#164b35);">//The result will be 2. Input overrides the initial value set in the parameter.</span></p></ac:rich-text-body></ac:structured-macro><h4 class="isSelectedEnd"><span>Invoking external tools via ToolExecution</span></h4><p class="isSelectedEnd"><span>Actions support &quot;</span>ToolExecution&quot;<span>, which allows SysML v2 features to be mapped to variables used by MATLAB scripts. This is particularly useful when the variable names used in the model differ from those expected by the external script.</span></p><p><span>The following example executes a MATLAB script and maps model features to MATLAB variables using &quot;</span>ToolVariable&quot;<span> annotations:</span></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="71f0bc6d-8deb-4cb2-9366-e6f7da3c2ea4"><ac:parameter ac:name="title">Example</ac:parameter><ac:rich-text-body><p><span style="color:var(--ds-text-accent-blue,#0055cc);">action</span><span style="color:var(--ds-text,#000000);"> computeStoppingDistance {</span><br /><span style="color:var(--ds-text,#000000);">            </span><span style="color:var(--ds-text-accent-blue,#0055cc);">private</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">import</span><span style="color:var(--ds-text,#000000);"> AnalysisTooling::*;</span><br /><span style="color:var(--ds-text,#000000);">            @ToolExecution {</span><br /><span style="color:var(--ds-text,#000000);">                :&gt;&gt; toolName = </span><span style="color:var(--ds-text-accent-red,#ae2e24);">&quot;MATLAB&quot;</span><span style="color:var(--ds-text,#000000);">;</span><br /><span style="color:var(--ds-text,#000000);">                :&gt;&gt; uri = </span><span style="color:var(--ds-text-accent-red,#ae2e24);">&quot;run('C:/custom/path/to/StoppingAnalysisExec.m')&quot;</span><span style="color:var(--ds-text,#000000);">;</span><br /><span style="color:var(--ds-text,#000000);">            }</span><br /><span style="color:var(--ds-text,#000000);">            </span><span style="color:var(--ds-text-accent-blue,#0055cc);">in</span><span style="color:var(--ds-text,#000000);"> mass : Real = vehicle.grossMass </span><span style="color:var(--ds-text,#000000);">{@ToolVariable { name = </span><span style="color:var(--ds-text-accent-red,#ae2e24);">&quot;m&quot;</span><span style="color:var(--ds-text,#000000);">; }};</span><br /><span style="color:var(--ds-text,#000000);">            </span><span style="color:var(--ds-text-accent-blue,#0055cc);">in</span><span style="color:var(--ds-text,#000000);"> speed : Real = vehicle.speed</span><span style="color:var(--ds-text,#000000);"> {@ToolVariable { name = </span><span style="color:var(--ds-text-accent-red,#ae2e24);">&quot;v0&quot;</span><span style="color:var(--ds-text,#000000);">; }};</span><br /><span style="color:var(--ds-text,#000000);">            </span><span style="color:var(--ds-text-accent-blue,#0055cc);">out</span><span style="color:var(--ds-text,#000000);"> Distance : Real = vehicle.stoppingDistance {@ToolVariable { name = </span><span style="color:var(--ds-text-accent-red,#ae2e24);">&quot;stoppingDistance&quot;</span><span style="color:var(--ds-text,#000000);">; }};</span><br /><span style="color:var(--ds-text,#000000);">            </span><span style="color:var(--ds-text-accent-blue,#0055cc);">out</span><span style="color:var(--ds-text,#000000);"> kineticEnergy : Real = vehicle.kineticEnergy {@ToolVariable { name = </span><span style="color:var(--ds-text-accent-red,#ae2e24);">&quot;e&quot;</span><span style="color:var(--ds-text,#000000);">; }};</span></p></ac:rich-text-body></ac:structured-macro><h3>Textual representations in constraints</h3><p>You can use a textual representation to define constraint logic in both requirements and standalone constraints using a supported scripting language. When a simple constraint (assert constraint) is evaluated, all attributes of the constraint’s owner are available in the script as variables. You can use them directly without qualification. You can also access nested structures using the get method (and dot notation in Groovy).</p><h4>Standalone constraints</h4><p>In a standalone constraint, attributes defined within the constraint are directly available in the script.</p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="dd10a11e-b75e-4664-914d-000d06230a76"><ac:parameter ac:name="title">Example</ac:parameter><ac:rich-text-body><p><span style="color:var(--ds-text-accent-blue,#0055cc);">assert</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">constraint</span><span style="color:var(--ds-text,#000000);"> {</span><br /><span style="color:var(--ds-text,#000000);">        </span><span style="color:var(--ds-text-accent-blue,#0055cc);">attribute</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">maxValue</span><span style="color:var(--ds-text,#000000);"> : </span><span style="color:var(--ds-text-accent-teal,#206a83);">Integer</span><span style="color:var(--ds-text,#000000);"> = </span><span style="color:var(--ds-background-accent-green-bolder,#1f845a);">5</span><span style="color:var(--ds-text,#000000);">;</span><br /><span style="color:var(--ds-text,#000000);">        </span><span style="color:var(--ds-text-accent-blue,#0055cc);">attribute</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">currentValue</span><span style="color:var(--ds-text,#000000);"> : </span><span style="color:var(--ds-text-accent-teal,#206a83);">Integer</span><span style="color:var(--ds-text,#000000);"> = </span><span style="color:var(--ds-background-accent-green-bolder,#1f845a);">3</span><span style="color:var(--ds-text,#000000);">;<br /></span><br /><span style="color:var(--ds-text,#000000);">        </span><span style="color:var(--ds-text-accent-blue,#0055cc);">language</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-red,#ae2e24);">&quot;Groovy&quot;</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-green-bolder,#164b35);">/* currentValue &lt; maxValue */</span><br /><span style="color:var(--ds-text,#000000);">}</span></p></ac:rich-text-body></ac:structured-macro><h4 class="cm-content q9tKkq_readonly m-0">Constraints in parts</h4><p>When a constraint is defined directly under a part, all attributes of the part are available in the script.</p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="fdb4d5d7-b99a-4d3c-af75-15ad6ca10e33"><ac:parameter ac:name="title">Example</ac:parameter><ac:rich-text-body><p><span style="color:var(--ds-text-accent-blue,#0055cc);">part</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">vehicle</span><span style="color:var(--ds-text,#000000);"> {</span><br /><span style="color:var(--ds-text,#000000);">    </span><span style="color:var(--ds-text-accent-blue,#0055cc);">attribute</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">maxSpeed</span><span style="color:var(--ds-text,#000000);"> : </span><span style="color:var(--ds-text-accent-teal,#206a83);">Integer</span><span style="color:var(--ds-text,#000000);"> = </span><span style="color:var(--ds-background-accent-green-bolder,#1f845a);">100</span><span style="color:var(--ds-text,#000000);">;</span><br /><span style="color:var(--ds-text,#000000);">    </span><span style="color:var(--ds-text-accent-blue,#0055cc);">attribute</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">currentSpeed</span><span style="color:var(--ds-text,#000000);"> : </span><span style="color:var(--ds-text-accent-teal,#206a83);">Integer</span><span style="color:var(--ds-text,#000000);"> = </span><span style="color:var(--ds-background-accent-green-bolder,#1f845a);">100</span><span style="color:var(--ds-text,#000000);">;<br /></span><span style="color:var(--ds-text,#000000);"><br />    </span><span style="color:var(--ds-text-accent-blue,#0055cc);">satisfy</span><span style="color:var(--ds-text,#000000);"> speedReq </span><span style="color:var(--ds-text-accent-blue,#0055cc);">by</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">this</span><span style="color:var(--ds-text,#000000);">;</span><br /><br /><span style="color:var(--ds-text,#000000);">    </span><span style="color:var(--ds-text-accent-blue,#0055cc);">assert</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">not</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">constraint</span><span style="color:var(--ds-text,#000000);"> {</span><br /><span style="color:var(--ds-text,#000000);">        </span><span style="color:var(--ds-text-accent-blue,#0055cc);">language</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-red,#ae2e24);">&quot;groovy&quot;</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-green-bolder,#164b35);">/* currentSpeed == maxSpeed */</span><br /><span style="color:var(--ds-text,#000000);">    }</span><br /><span style="color:var(--ds-text,#000000);">}</span></p></ac:rich-text-body></ac:structured-macro><h4 class="cm-content q9tKkq_readonly m-0">Constraints in requirements</h4><p>When a constraint is used inside a requirement, the requirement subject is made available to the script engine as the root context for evaluation. This means that the subject and its structure are directly accessible in the script engine.</p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="6ee9d0ad-7196-4304-bfd7-115dc72d4ea5"><ac:parameter ac:name="title">Example</ac:parameter><ac:rich-text-body><p><span style="color:var(--ds-text-accent-blue,#0055cc);">requirement</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">speedReq</span><span style="color:var(--ds-text,#000000);"> {</span><br /><span style="color:var(--ds-text,#000000);">    </span><span style="color:var(--ds-text-accent-blue,#0055cc);">subject</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);"><ac:inline-comment-marker ac:ref="170302ae-4f59-4d69-8b4f-fa85c8557252">vehicle</ac:inline-comment-marker></span><span style="color:var(--ds-text,#000000);"><ac:inline-comment-marker ac:ref="170302ae-4f59-4d69-8b4f-fa85c8557252"> v :&gt; </ac:inline-comment-marker></span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);"><ac:inline-comment-marker ac:ref="170302ae-4f59-4d69-8b4f-fa85c8557252">vehicle</ac:inline-comment-marker></span><span style="color:var(--ds-text,#000000);"><ac:inline-comment-marker ac:ref="170302ae-4f59-4d69-8b4f-fa85c8557252">;</ac:inline-comment-marker><br /><br /></span><span style="color:var(--ds-text,#000000);">    </span><span style="color:var(--ds-text-accent-blue,#0055cc);">require</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">constraint</span><span style="color:var(--ds-text,#000000);"> {</span><br /><span style="color:var(--ds-text,#000000);">        </span><span style="color:var(--ds-text-accent-blue,#0055cc);">language</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-red,#ae2e24);">&quot;groovy&quot;</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-green-bolder,#164b35);">/* v.currentSpeed &lt; vehicle.maxSpeed */</span><br /><span style="color:var(--ds-text,#000000);">    }</span><br /><span style="color:var(--ds-text,#000000);">}</span></p></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=254423427 space=SYSML2EP version=1 -->
## PAGE 00058: Versions of SysML v2 Evaluation Plugin Documentation

- page_id: `254423427`
- space_key: `SYSML2EP`
- source_url: https://docs.nomagic.com/spaces/SYSML2EP/pages/254423427/Versions+of+SysML+v2+Evaluation+Plugin+Documentation
- version_number: 1
- version_date: `2025-09-12T14:49:40.063+02:00`
- ancestors: 
- labels: []

### NORMALIZED CONTENT

ae5edf3a091d24f1bc7b62973e0464b8

SysML v2 Evaluation Plugin Documentation

documentVersions

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="scroll-document-location" ac:schema-version="1" ac:macro-id="c14eb7df-7045-45a5-849d-482d8a038f17"><ac:parameter ac:name="permaId">ae5edf3a091d24f1bc7b62973e0464b8</ac:parameter><ac:parameter ac:name="documentTitle">SysML v2 Evaluation Plugin Documentation</ac:parameter><ac:parameter ac:name="key">documentVersions</ac:parameter></ac:structured-macro>
````
