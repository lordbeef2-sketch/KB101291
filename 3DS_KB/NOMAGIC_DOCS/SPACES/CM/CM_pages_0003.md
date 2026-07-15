# NOMAGIC DOCUMENTATION SPACE: Client-Side Collaboration

<!--NOMAGIC_SPACE key=CM chunk=3 -->

<!--NOMAGIC_PAGE id=243970309 space=CM version=1 -->
## PAGE 00265: Lock-Free Editing mode

- page_id: `243970309`
- space_key: `CM`
- source_url: https://docs.nomagic.com/spaces/CM/pages/243970309/Lock-Free+Editing+mode
- version_number: 1
- version_date: `2025-07-31T10:51:48.048+02:00`
- ancestors: Client-Side Collaborative Modeling Documentation > Collaboration powered by 3DEXPERIENCE platform > Locking models in 3DEXPERIENCE platform
- labels: []

### NORMALIZED CONTENT

#### CONTENT-LAYER: Example #2

833100474

#### CONTENT-COLUMN: Example #2

833100476

833100473

**On this page**

**5**

#### CONTENT-BLOCK: Example #2

833100475

The Lock-Free Editing mode, the default mode for the **3D**EXPERIENCEplatform, enables you to work with model elements without needing to lock them. Keep in mind that this is applicable to model elements only. Locks for diagrams, project options, and used projects will persist; you will still have to lock them before editing.

#### TIP: Recommendation

Recommendation

Assigning differentscopesof the model to various users is the recommended way to work in the Lock-Free Editing mode to prevent conflicts that may occur when users' changes interfere with each other.

Even though users usually work on different parts of the model, occasionally when they edit the same model elements conflicting changes may occur. In that case, you will be asked to review these conflicts in the**Conflicting Changes** panel and then take action, such as confirming the update result or discarding local changes.

#### TIP: Example #1

Example #1

*User 1 and User 2 are working on the same model iteration: [1] A.1. The model contains Class A.*

*User 1 deletes Class A from the model and commits the project to the server. Model iteration [1] A.2 is created.*

*User 2 renames Class A to Class B and commits/updates the project to the server. Conflicting changes occur.*

#### TIP: Example #2

Example #2

*User 1 and User 2 are working on the same model iteration: [1] A.1. The model contains Class A.*

*User 1 renames Class A to Class B and commits the project to the server. Model iteration [1] A.2 is created.*

*User 2 renames Class A to Class C and commits the project to the server. Conflicting changes occur.*

##### Conflicting Changes panel

To open the panel

1. In the main menu, click Window .
2. Select Conflicting Changes from the drop-down menu. The Conflicting Changes panel opens.
3. [ATTACHMENT filename='conflicting_changes_panel.png'] The Conflicting Changes panel.

Alternatively, you can open it by clicking the **Review Conflicts**button directly on the warning that appears when conflicting changes are detected.

[IMAGE alt='' src='']

###### The Conflicting Changes warning.

Please note that conflicting changes are checked upon a project update or a commit that requires an update.

##### Composition of the Conflicting Changes panel

The **Conflicting Changes** panel consists of three smaller panels that provide the following pieces of information to the user:

- Conflicting Local Changes : shows locally modified elements whose changes conflict with the changes already committed to the server.
- Upcoming Changes : shows the upcoming changes that conflict with the selected local change.
- Preview Update Result : shows the changes that will be applied after the project update.

[IMAGE alt='' src='']

###### Conflicting Changes panel informs users about the changes that conflict in the project.

##### Symbols used in the Conflicting Changes panel

| Icon | Description |
| --- | --- |
|  | Checks the presence of the conflicting changes in the model. |
|  | Selects the previous conflicting change on the list. |
|  | Selects the next conflicting change on the list. |
|  | Expands elements in the Conflicting Local Changes panel. |
|  | Collapses elements in the Conflicting Local changes panel. |
|  | Confirms the update result affecting the selected element. |
|  | Confirms all update results of the conflicting changes at once. |
|  | Filters confirmed/unconfirmed conflicting changes. |
|  | Shows that the conflicting change has been confirmed by the user. |

##### Resolving conflicting changes

**Confirming update results**

Once you have reviewed the conflicting changes, you can confirm the update result that will be applied after the project update. It should be emphasized that remote deletions always take precedence over local changes.

To confirm an update result

1. In the Conflicting Changes panel, do one of the following:
  - select the specific conflicting element and click [ATTACHMENT filename='confirm.png'] in the toolbar at the top.
  - click [ATTACHMENT filename='confirm_all_update_results.png'] in the toolbar to confirm all conflicting changes at once.

Right-click the conflicting element and select **Confirm Update Result**in the shortcut menu. The acknowledged change is marked with a green tick[IMAGE alt='' src='']. 
 
[IMAGE alt='' src='']

###### Confirming the conflicting changes via the shortcut menu.

The following outlines another group of actions you can perform to handle detected conflicting changes:

- Select in Containment Tree : click to select the element in Containment tree.
- Quick Diff : select to inspect the conflicting changes in a compact form.
- Full Diff : select to inspect the conflicting changes in a detailed form.
- Compare Projects : select to compare the modified projects.
- Discard Changes : select to discard the local changes.

Please note that you cannot undo the discarded changes.

Depending on the action you have performed prior to the detection of conflicting changes in your model, you will see either the **Commit** or the **Update** button in the **Conflicting Changes** panel after confirming the conflicting changes in your project.

[IMAGE alt='' src='']

###### Update or Commit button in the Conflicting Changes panel.

##### Disabling the Lock-Free Editing mode

To lock all lockable elements and work in a lock-required mode, disable lock-free editing.

To disable the Lock-Free Editing mode

1. In the main menu, click Options > Project .
2. In the panel on the left, select General > Collaboration .
3. Under the Locking options, disable Lock-Free Editing by setting the value to false , and click OK . [ATTACHMENT filename='disabling_lock_free_editing.png']
4. In the **Question** dialog asking whether you want to commit the changes to the server, select **Continue**. 
[IMAGE alt='' src='']
5. In the Information dialog, click OK . The Lock-Free Editing mode is now disabled. [ATTACHMENT filename='information_panel_lock_required_mode.jpg']

If the Lock-Free Mode is disabled in the project, users who worked without locks will not be able to commit their changes to the server. We recommend making sure that all users working on the model do not have uncommitted changes before switching modes.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="3a3657fb-450b-4168-af5e-a612afc0bdc7"><ac:parameter ac:name="id">833100474</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="2e5064b4-c442-4607-9874-d00aaa9d1906"><ac:parameter ac:name="id">833100476</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="f9a53328-f498-4496-b7ef-e3767e676379"><ac:parameter ac:name="id">833100473</ac:parameter><ac:rich-text-body><p><strong>On this page</strong></p><p><strong><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="81eb5a28-aae2-4815-98f4-f076cf0192dd"><ac:parameter ac:name="maxLevel">5</ac:parameter></ac:structured-macro></strong></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="3a62ebf0-5853-4217-ad87-c5c5431034ec"><ac:parameter ac:name="id">833100475</ac:parameter><ac:rich-text-body><p>The Lock-Free Editing mode, the default mode for the <span style="color: rgb(55,65,81);"><strong>3D</strong>EXPERIENCE </span>platform, enables you to work with model elements <ac:inline-comment-marker ac:ref="3bbcc18f-73e9-4648-a496-8a8f4baf9de1">without needing</ac:inline-comment-marker> to lock them. Keep in mind that this is applicable to model elements only. Locks for diagrams, project options, and used projects will persist; <ac:inline-comment-marker ac:ref="f9b76e18-7d85-46d1-a229-1196821965cb">you will still have to lock them before editing</ac:inline-comment-marker>.</p><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="09f91519-1edc-43e4-8d5c-e3d25d948aee"><ac:parameter ac:name="title">Recommendation</ac:parameter><ac:rich-text-body><p><span>Assigning different </span>scopes<span> of the model to various users is the recommended way to work in the Lock-Free Editing mode to prevent conflicts that may occur when users' changes interfere with each other.</span></p></ac:rich-text-body></ac:structured-macro><p><br /></p><p class="auto-cursor-target" style="text-align: center;"><ac:structured-macro ac:name="widget" ac:schema-version="1" ac:macro-id="5f6a5a4d-5969-42c3-b75e-e6fc6a4595d0"><ac:parameter ac:name="url"><ri:url ri:value="https://www.youtube.com/watch?v=aMgoxSg4-Rw" /></ac:parameter></ac:structured-macro></p><p>Even though users usually work on different parts of the model, occasionally when they edit the same model elements conflicting changes may occur. In that case, you will be asked to review these conflicts in the<strong> Conflicting Changes</strong> panel and then take action, such as confirming the update result or discarding local changes.</p><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="53ba45fe-db2b-4e03-8b59-21f919bcd807"><ac:parameter ac:name="title">Example #1</ac:parameter><ac:rich-text-body><p style="margin-left: 0.0in;"><em> <span style="color: rgb(62,63,64);">User 1 and User 2 are working on the same model iteration: [1] A.1. The model contains Class A.</span> </em></p><p style="margin-left: 0.0in;"><em> <span style="color: rgb(62,63,64);">User 1 deletes Class A from the model and commits the project to the server. Model iteration [1] A.2 is created.</span> </em></p><p style="margin-left: 0.0in;"><em> <span style="color: rgb(62,63,64);">User 2 renames Class A to Class B and commits/updates the project to the server. Conflicting changes occur.</span> </em></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="3750b2a9-b602-4880-ae5c-7d8ace07ea34"><ac:parameter ac:name="title">Example #2</ac:parameter><ac:rich-text-body><p style="margin-left: 0.0in;"><em> <span style="color: rgb(62,63,64);">User 1 and User 2 are working on the same model iteration: [1] A.1. The model contains Class A.</span> </em></p><p style="margin-left: 0.0in;"><em> <span style="color: rgb(62,63,64);">User 1 renames Class A to Class B and commits the project to the server. Model iteration [1] A.2 is created.</span> </em></p><p style="margin-left: 0.0in;"><em> <span style="color: rgb(62,63,64);">User 2 renames Class A to Class C and commits the project to the server. Conflicting changes occur.</span> </em></p></ac:rich-text-body></ac:structured-macro><h3 class="auto-cursor-target">Conflicting Changes panel</h3><p>To open the panel</p><hr /><ol><li>In the main menu, click <strong>Window</strong>.</li><li>Select <strong>Conflicting Changes</strong> from the drop-down menu. The <strong>Conflicting Changes</strong> panel opens.</li><li><ac:image ac:align="center"><ri:attachment ri:filename="conflicting_changes_panel.png" /></ac:image><h6 style="text-align: center;">The Conflicting Changes panel.</h6></li></ol><p>Alternatively, you can open it by clicking the <strong>Review Conflicts </strong>button directly on the warning that appears when conflicting changes are detected. </p><p><ac:image ac:align="center"><ri:attachment ri:filename="review_conflicts_dialog.png" /></ac:image></p><h6 style="text-align: center;">The Conflicting Changes warning.</h6><p><br /></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="8375b7f6-33d7-4cc8-ad88-9d7a70e2bee1"><ac:rich-text-body><p>Please note that conflicting changes are checked upon a project update <span style="color: rgb(62,63,64);">or a commit that requires an update.</span></p></ac:rich-text-body></ac:structured-macro><h3>Composition of the Conflicting Changes panel</h3><p>The <strong>Conflicting Changes</strong> panel consists of three smaller panels that provide the following pieces of information to the user: </p><ul><li><strong>Conflicting Local Changes</strong>: shows locally modified elements whose changes conflict with the changes already committed to the server. </li><li><strong>Upcoming Changes</strong>: shows the upcoming changes that conflict with the selected local change. </li><li><strong>Preview Update Result</strong>: shows the changes that will be applied after the project update. </li></ul><p><ac:image ac:align="center"><ri:attachment ri:filename="preview_conflicting_changes.png" /></ac:image></p><h6 style="text-align: center;">Conflicting Changes panel informs users about the changes that conflict in the project.</h6><h3>Symbols used in the Conflicting Changes panel</h3><table class="relative-table wrapped" style="width: 35.2715%;"><colgroup> <col style="width: 7.78816%;" /> <col style="width: 92.2118%;" /> </colgroup><tbody><tr><th>Icon</th><th>Description</th></tr><tr><td><div class="content-wrapper"><p><ac:image><ri:attachment ri:filename="refresh_buttonpng.png" /></ac:image></p></div></td><td>Checks the presence of the conflicting changes in the model.</td></tr><tr><td><div class="content-wrapper"><p><ac:image><ri:attachment ri:filename="moving_up.png" /></ac:image></p></div></td><td>Selects the previous conflicting change on the list.</td></tr><tr><td><div class="content-wrapper"><p><ac:image><ri:attachment ri:filename="moving_down.png" /></ac:image></p></div></td><td>Selects the next conflicting change on the list.</td></tr><tr><td><div class="content-wrapper"><p><ac:image><ri:attachment ri:filename="expand_all.png" /></ac:image></p></div></td><td>Expands elements in the <strong>Conflicting</strong> <strong>Local Changes</strong> panel.</td></tr><tr><td colspan="1"><div class="content-wrapper"><p><ac:image><ri:attachment ri:filename="collapse_all.png" /></ac:image></p></div></td><td colspan="1">Collapses elements in the <strong>Conflicting Local changes</strong> panel.</td></tr><tr><td colspan="1"><div class="content-wrapper"><p><ac:image><ri:attachment ri:filename="confirm.png" /></ac:image></p></div></td><td colspan="1">Confirms the update result affecting the selected element.</td></tr><tr><td colspan="1"><div class="content-wrapper"><p><ac:image><ri:attachment ri:filename="confirm_all_update_results.png" /></ac:image></p></div></td><td colspan="1">Confirms all update results of the conflicting changes at once.</td></tr><tr><td colspan="1"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:height="10"><ri:attachment ri:filename="filter_icon.jpg" /></ac:image></p></div></td><td colspan="1"><div class="content-wrapper"><p>Filters confirmed/unconfirmed conflicting changes.</p><p><ac:image ac:thumbnail="true" ac:height="72"><ri:attachment ri:filename="filter_options.jpg" /></ac:image></p></div></td></tr><tr><td colspan="1"><div class="content-wrapper"><p><ac:image><ri:attachment ri:filename="green_tick.png" /></ac:image></p></div></td><td colspan="1"><div class="content-wrapper"><p>Shows that the conflicting change has been confirmed by the user.</p><p><ac:image><ri:attachment ri:filename="confirmed_change_symbol.png" /></ac:image></p></div></td></tr></tbody></table><p><br /></p><h3>Resolving conflicting changes</h3><p><strong>Confirming update results</strong></p><p>Once you have reviewed the conflicting changes, you can confirm the update result that will be applied after the project update. It should be emphasized that remote deletions always take precedence over local changes. </p><p>To confirm an update result</p><hr /><ol><li>In the <strong>Conflicting Changes</strong> panel, do one of the following:<ul><li>select the specific conflicting element and click <ac:image><ri:attachment ri:filename="confirm.png" /></ac:image> in the toolbar at the top.</li><li>click <ac:image><ri:attachment ri:filename="confirm_all_update_results.png" /></ac:image> in the toolbar to confirm all conflicting changes at once.</li></ul></li></ol><p>Right-click the conflicting element and select <strong>Confirm Update Result </strong>in the shortcut menu. The acknowledged change is marked with a green tick<ac:image><ri:attachment ri:filename="green_tick.png" /></ac:image>.<br /><br /><ac:image ac:align="center"><ri:attachment ri:filename="confirming_update_result.png" /></ac:image></p><h6 style="text-align: center;">Confirming the conflicting changes via the shortcut menu.</h6><p>The following outlines another group of actions you can perform to handle detected conflicting changes:</p><ul><li><strong>Select in Containment Tree</strong>: click to select the element in Containment tree.</li><li><strong>Quick Diff</strong>: select to inspect the conflicting changes in a compact form.</li><li><strong>Full Diff</strong>: select to inspect the conflicting changes in a detailed form.</li><li><strong>Compare Projects</strong>: select to compare the modified projects.</li><li><strong>Discard Changes</strong>: select to discard the local changes.</li></ul><ac:structured-macro ac:name="warning" ac:schema-version="1" ac:macro-id="0a7dbecd-ccf3-4b0c-a051-86a08e39231a"><ac:rich-text-body><p>Please note that you cannot undo the discarded changes.</p></ac:rich-text-body></ac:structured-macro><p><br /></p><p>Depending on the action you have performed prior to the detection of conflicting changes in your model, you will see either the <strong>Commit</strong> or the <strong>Update</strong> button in the <strong>Conflicting Changes</strong> panel after confirming the conflicting changes in your project. </p><p><ac:image ac:align="center"><ri:attachment ri:filename="conflicting_changes_buttons.png" /></ac:image></p><h6 style="text-align: center;"><span style="color: rgb(94,108,132);">Update or Commit button in the Conflicting Changes panel.</span></h6><h3>Disabling the Lock-Free Editing mode</h3><p>To lock all lockable elements and work in a lock-required mode, disable lock-free editing.</p><p>To disable the Lock-Free Editing mode</p><hr /><ol><li>In the main menu, click <strong>Options</strong> &gt; <strong>Project</strong>.</li><li>In the panel on the left, select <strong>General</strong> &gt; <strong>Collaboration</strong>.</li><li>Under the <strong>Locking</strong> options, disable <strong>Lock-Free Editing </strong>by setting the value to <em>false</em>, and click <strong>OK</strong>. <br /><ac:image ac:width="742"><ri:attachment ri:filename="disabling_lock_free_editing.png" /></ac:image></li><li><p class="auto-cursor-target">In the <strong>Question</strong> dialog asking whether you want to commit the changes to the server, select <strong>Continue</strong>. <br /><ac:image ac:height="227"><ri:attachment ri:filename="question_dialog.jpg" /></ac:image></p></li><li>In the <strong>Information</strong> dialog, click <strong>OK</strong>. The <strong>Lock-Free Editing</strong> mode is now disabled. <br /><ac:image ac:height="154"><ri:attachment ri:filename="information_panel_lock_required_mode.jpg" /></ac:image></li></ol><ac:structured-macro ac:name="warning" ac:schema-version="1" ac:macro-id="bab8d01c-9b27-4158-a504-20ea5d28d6f6"><ac:rich-text-body><p><span style="color: rgb(62,63,64);">If the Lock-Free Mode is disabled</span> in the project, users who worked without locks will not be able to commit their changes to the server. We recommend making sure that all users working on the model do not have uncommitted changes before switching modes.</p></ac:rich-text-body></ac:structured-macro><p><br /></p><p><br /></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=243969837 space=CM version=2 -->
## PAGE 00266: Locking model for edit

- page_id: `243969837`
- space_key: `CM`
- source_url: https://docs.nomagic.com/spaces/CM/pages/243969837/Locking+model+for+edit
- version_number: 2
- version_date: `2026-06-08T12:18:07.523+02:00`
- ancestors: Client-Side Collaborative Modeling Documentation > Using Teamwork Cloud > Using lock-based editing mode
- labels: []

### NORMALIZED CONTENT

You must lock the part of the model you are going to edit to prevent other users from editing it at the same time. Locking is allowed if that part of the model is not locked by another user, because the same item can only be locked by one user at a time.

The following table explains what you can edit after you lock a single element, single diagram, diagram with elements, and so on.

| When you lock... | You can... |
| --- | --- |
| Element | Edit element specification properties (in the Specification window) |
| Diagram | Edit:Diagram specification properties (in the Specification window)Diagram properties (in the Diagram Properties dialog)Symbol layout on the diagram paneSymbol properties (in the Symbol Properties dialog) |
| Diagram with elements | Edit:Diagram specification properties (in the Specification window)Element specification properties (in the Specification window and on the diagram pane)Diagram properties (in the Symbol Properties dialog)Symbol properties (in the Symbol Properties dialog)Symbol layout on the diagram pane |
| Symbol styles | Edit properties of symbol styles (in the Project Options dialog) |
| Project usages | Import used projects as packages into the main projectStop using projectsChange versions of used projects |

##### Locking without forced project update

You can lock elements without forcing an update of a project to the latest version if the selected elements are not locked or do not have changes in a newer version on the server.

This feature can be disabled/enabled in the **Environment Options** dialog.

To disable/enable locking without updating

1. Select Options > Environment > Collaboration node.
2. Find Enable Locking Without Forced Project Update option. Do one of the following:
  - Set value to true, to enable locking without updating;
  - Set value to false, to disable locking without updating .

#### NOTE: An example

There is a 60-second threshold; iflocking takes longer than 60 seconds, a project update will be required.

#### TIP: An example

An example

You are trying to lock package B, which contains many elements, recursively. The modeling tool cannot check all contained elements' status in the later versions of the project in 60 seconds. After 60 seconds, a project update will be requiredto lock the package.

##### representRepresentation of locked elements

In the Containment tree, element names are represented in two colors:

- Unlocked elements are represented in black, meaning they are editable.
- Locked elements are represented in gray, meaning they are not editable.

[IMAGE alt='' src='']

##### Locking elements and diagrams

Elements and diagrams can be locked by using the commands from their shortcut menu.

[IMAGE alt='' src='']

Elements can also be locked by clicking the Lock element for the Edit button [IMAGE alt='' src=''] on their Specification window.

[IMAGE alt='' src='']

The following table provides suggestions on which locking commands to use for different purposes.

| If you need to edit... | Do the following |
| --- | --- |
| Specification properties of a single element | Right-click either:This element in the Model Browser.A symbol of this element on a diagram pane.From the shortcut menu, select Lock > Lock Element for Edit.ORDouble-click either:This element in the Model Browser.A symbol of this element on a diagram pane.In the Specification window, click the Lock element for Edit button . |
| Specification properties of both an element and the elements it contains (owns)For example, a project has a Package Analysis, containing two inner Packages- Design and Implementation. Each inner Package also contains elements.Lock the Package Analysis recursively to edit all the elements in this Package. | Right-click either:This element in the Model Browser.A symbol of this element on a diagram pane.From the shortcut menu, select Lock > Lock Elements for Edit Recursively |
| At least one of the following:Diagram representation properties (including diagram layout)Symbol properties of elements represented on that diagram pane | Right-click this diagram in the Model Browser.From the shortcut menu, select Lock > Lock Diagram for Edit.ORRight-click a free space on this diagram pane.From the shortcut menu, select Lock Diagram > Lock Diagram for Edit. |
| At least one of the following:Diagram specification propertiesDiagram representation properties (including diagram layout)Properties of elements represented on that diagram paneSymbol properties of elements represented on that diagram pane | Right-click this diagram in the Model Browser.From the shortcut menu, select Lock > Lock Diagram Content for Edit.ORRight-click a free space on this diagram pane.From the shortcut menu, select Lock Diagram > Lock Diagram Content for Edit. |
| At least one of the following:Symbol properties of a single element represented on a diagram panePosition of the symbol on the diagram pane | Right-click the symbol of that element on a diagram pane.From the shortcut menu, select Lock > Lock Element for Edit in Diagram. |

##### Locking symbol styles

You can lock symbol styles via the **Lock View** tab or the **Project Options** dialog.

To lock symbol styles via the **Lock View** tab

1. In the **Lock View** tab on the Model Browser, expand *Project Options*. Where is the Lock View tab?It is the last tab on the Model Browser. If the tab is closed, you can simply open it by selecting **Collaborate** > **View Locked Elements**.
2. Right-click Symbol Styles and from the shortcut menu select Lock Symbol Styles for Edit .

To lock symbol styles via the**Project Options** dialog

1. Do either:
  - Select Options > Project .
  - In the **Lock View** tab on the Model Browser, right-click *Project Options* and from the shortcut menu, select **Symbol Styles**. Where is the Lock View tab?It is the last tab on the Model Browser. If the tab is closed, you can simply open it by selecting **Collaborate** > **View Locked Elements**.
2. In the Project Options dialog, click the Lock Symbol Styles for Edit button.

[IMAGE alt='' src='']

As a result, symbol styles become editable. Additionally, the **Make Default** button (1) in all **Symbol Properties** dialogs and the**Set Selected Symbol Style as Default** button (2) on all the diagram toolbars become available.

[IMAGE alt='' src='']

##### Locking project usages

To lock a used project

1. From the Options menu, select Project Usages . The Project Usages dialog opens.
2. Select a used project on the left side of the dialog.
3. Click the [ATTACHMENT filename='lock_in_spec.png'] button to lock the used project.

#### TIP: Shortcut menu

Shortcut menu

This step can be done via shortcut menu. Right-click project and then select **Lock**.****

You can then import this used project as a package to the main project, stop using it, or change its version.

**Related pages**

- [CONFLUENCE_PAGE title='Unlocking model' space='']
- [CONFLUENCE_PAGE title='Committing changes to Teamwork Cloud' space='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>You must lock the part of the model you are going to edit to prevent other users from editing it at the same time. Locking is allowed if that part of the model is not locked by another user, because the same item can only be locked by  one user at a time. </p><p>The following table explains what you can edit after you lock a single element, single diagram, diagram with elements, and so on.</p><table><colgroup class=""><col class="" /><col class="" /></colgroup><tbody class=""><tr class=""><th>When you lock...</th><th>You can...</th></tr><tr class=""><td>Element</td><td>Edit element specification properties (in the Specification window)</td></tr><tr class=""><td>Diagram</td><td><p>Edit:</p><ul><li data-uuid="fbbaf0b1-1cb6-407d-80c1-5f1267c9cf23">Diagram specification properties (in the Specification window)</li><li data-uuid="35770cc7-10eb-42aa-b520-cc0c90686f9a">Diagram properties (in the <strong>Diagram Properties</strong> dialog)</li><li data-uuid="b4107f5a-2fc3-404c-b29d-326108495432">Symbol layout on the diagram pane</li><li data-uuid="abb57d17-d848-494a-a72b-d0a86a836eb8">Symbol properties (in the <strong>Symbol Properties</strong> dialog)</li></ul></td></tr><tr class=""><td>Diagram with elements</td><td><p>Edit:</p><ul><li data-uuid="759fcb30-c83e-4385-85b2-347312734646">Diagram specification properties (in the Specification window)</li><li data-uuid="769efbfe-93e5-40b5-bdd1-a988978d922c">Element specification properties (in the Specification window and on the diagram pane)</li><li data-uuid="bba27241-6622-48ec-a7e9-09034eff8e53">Diagram properties (in the <strong>Symbol Properties</strong> dialog)</li><li data-uuid="7c7031f6-7ceb-411f-ab5e-c93893e37b45">Symbol properties (in the <strong>Symbol Properties</strong> dialog)</li><li data-uuid="cf830766-6b02-4f50-b84f-df27b2362ea3">Symbol layout on the diagram pane</li></ul></td></tr><tr class=""><td colspan="1">Symbol styles</td><td colspan="1"><p>Edit properties of symbol styles (in the <strong>Project Options</strong> dialog)</p></td></tr><tr class=""><td colspan="1">Project usages</td><td colspan="1"><ul><li data-uuid="1bdf41e4-8fb2-4bd5-b23f-5f00d8a808bc">Import used projects as packages into the main project</li><li data-uuid="615a6543-91f9-4426-a166-419a2221b68d">Stop using projects</li><li data-uuid="6e8aad00-0870-404e-9eca-7ebca4981db7">Change versions of used projects</li></ul></td></tr></tbody></table><p class="auto-cursor-target"><br /></p><h3>Locking without forced project update</h3><p>You can lock elements without forcing an update of a project to the latest version if the selected <span style="color:var(--ds-text,#333333);">elements are not locked or do not have changes in a newer version on the server. </span></p><p><span style="color:var(--ds-text,#333333);">This feature can be</span> disabled/enabled in the <strong>Environment Options</strong> dialog.</p><p>To disable/enable locking without updating</p><hr /><ol><li data-uuid="d59ada7f-9d81-48dd-9809-9ed6bf141c76">Select <strong>Options</strong> &gt; <strong>Environment </strong>&gt; <strong>Collaboration </strong>node.</li><li data-uuid="c1c88523-43d3-4d9f-94b3-3ac9ce83c56e">Find <strong>Enable Locking Without Forced Project Update </strong>option. Do one of the following: <ul><li>Set value to <em>true, </em>to enable <span style="color:var(--ds-text,#333333);">locking without updating;</span></li><li>Set value to<em> false, </em>to disable <span style="color:var(--ds-text,#333333);">locking without updating</span>. </li></ul></li></ol><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="6cc4ef97-4cde-4bc9-907e-89f11ac34a94"><ac:rich-text-body><p>There is a 60-second threshold; if<span style="color:var(--ds-text,#333333);"> locking takes longer than 60 seconds, a project update will be required.</span></p><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="85b7cfd4-f4c0-484d-a506-1b41e27ef468"><ac:parameter ac:name="title">An example</ac:parameter><ac:rich-text-body><p><span>You are trying to lock package B, which contains many elements, recursively. The modeling tool cannot check all contained elements' status in the later versions of the project in 60 seconds. After 60 seconds, a project update will be required </span><span>to lock the package.</span></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro><p><br /></p><h3><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="ed9519ee-5388-48a8-a877-3827fd18e096"><ac:parameter ac:name="">represent</ac:parameter></ac:structured-macro>Representation of locked elements</h3><p>In the Containment tree, element names are represented in two colors:</p><ul><li data-uuid="66d8a161-830e-496c-84c5-567e7248551c">Unlocked elements are represented in black, meaning they are editable.</li><li data-uuid="081e4d64-8578-40d3-a51a-40ffb3c01e19">Locked elements are represented in gray, meaning they are not editable.</li></ul><p><ac:image ac:title="Locked and unlocked elements in the Containment tree" ac:alt="Locked and unlocked elements in the Containment tree"><ri:attachment ri:filename="locked_and_unlocked_elems.png" /></ac:image></p><h3>Locking elements and diagrams</h3><p>Elements and diagrams can be locked by using the commands from their shortcut menu.</p><p><ac:image ac:title="Locking commands on the shortcut menu of the Package" ac:alt="Locking commands on the shortcut menu of the Package"><ri:attachment ri:filename="locking_commands_on_shortcut_menu.png" /></ac:image></p><p><br /></p><p>Elements can also be locked by clicking the Lock element for the Edit button <ac:image><ri:attachment ri:filename="lock_in_spec.png" /></ac:image> on their Specification window.</p><p><ac:image ac:title="Locking command in the element's Specification window" ac:alt="Locking command in the element's Specification window"><ri:attachment ri:filename="locking_command_in_spec_window.png" /></ac:image></p><p><br /></p><p>The following table provides suggestions on which locking commands to use for different purposes.</p><table><colgroup class=""><col class="" /><col class="" /></colgroup><tbody class=""><tr class=""><th>If you need to edit...</th><th>Do the following</th></tr><tr class=""><td><p>Specification properties of a single element</p></td><td><div class="content-wrapper"><ol><li data-uuid="c8f18058-3882-4992-ad2e-5e403cfc7d85">Right-click either:<ul><li>This element in the Model Browser.</li><li>A symbol of this element on a diagram pane.</li></ul></li><li data-uuid="438c6eee-e8ca-4186-8f21-05ab7362d8b8">From the shortcut menu, select <strong>Lock</strong> &gt; <strong>Lock Element for Edit</strong>.</li></ol><p>OR</p><ol><li data-uuid="533bf7eb-8614-4997-81d5-ab7bfaac6ee0">Double-click either:<ul><li>This element in the Model Browser.</li><li>A symbol of this element on a diagram pane.</li></ul></li><li data-uuid="aced825e-d960-4783-bd36-b160b5ddd4ff">In the Specification window, click the Lock element for Edit button <ac:image ac:title="Lock element for Edit" ac:alt="Lock element for Edit"><ri:attachment ri:filename="lock_in_spec.png" /></ac:image>.</li></ol></div></td></tr><tr class=""><td><div class="content-wrapper"><p><span>Specification properties of both an element and the elements it contains (owns)</span></p><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="35433209-e864-4b2f-b359-b9ca1dc4348b"><ac:rich-text-body><p>For example, a project has a Package <em>Analysis</em>, containing two inner Packages<br />- <em>Design</em> and <em>Implementation</em>. Each inner Package also contains elements.</p><p>Lock the Package <em>Analysis </em>recursively to edit all the elements in this Package.</p></ac:rich-text-body></ac:structured-macro><p><span> </span></p></div></td><td><ol><li data-uuid="6f0f212b-3f9c-4e5c-83be-b6985313aca5">Right-click either:<ul><li>This element in the Model Browser.</li><li>A symbol of this element on a diagram pane.</li></ul></li><li data-uuid="2a644265-c99f-413f-a500-3c007eb8bcc8">From the shortcut menu, select <strong>Lock</strong> &gt; <strong>Lock Elements for Edit Recursively</strong></li></ol></td></tr><tr class=""><td colspan="1"><p>At least one of the following:</p><ul><li data-uuid="133c63b1-4e19-4e25-957a-db25f6296531">Diagram representation properties (including diagram layout)</li><li data-uuid="793ce1df-c3f7-4eda-81af-1dd6005c6397">Symbol properties of elements represented on that diagram pane</li></ul></td><td colspan="1"><ol><li data-uuid="2e7d7f41-933c-4c80-8d7a-524be47503de">Right-click this diagram in the Model Browser.</li><li data-uuid="dc60328b-df7a-4b8d-a8c2-eee53bb8be90">From the shortcut menu, select <strong>Lock</strong> &gt; <strong>Lock Diagram for Edit</strong>.</li></ol><p>OR</p><ol><li data-uuid="532bd150-85bb-4698-ab85-b426d7bad68c">Right-click a free space on this diagram pane.</li><li data-uuid="c84b1c00-2766-46a4-a11d-92e2b5d93f3b">From the shortcut menu, select <strong>Lock Diagram</strong> &gt; <strong>Lock Diagram for Edit</strong>.</li></ol></td></tr><tr class=""><td colspan="1"><p>At least one of the following:</p><ul><li data-uuid="0c40e1ca-495c-4787-9aa8-38d72fe9fde3">Diagram specification properties</li><li data-uuid="b2d21366-2427-476a-a822-338bfcba31e5">Diagram representation properties (including diagram layout)</li><li data-uuid="b43a8636-51f5-4118-972d-55479a8ce02b">Properties of elements represented on that diagram pane</li><li data-uuid="0065d028-cd2c-449a-a8a2-48930a016858">Symbol properties of elements represented on that diagram pane</li></ul></td><td colspan="1"><ol><li data-uuid="c1e8cf93-8c6b-48f5-a916-0179c42df021">Right-click this diagram in the Model Browser.</li><li data-uuid="516dedb5-56d0-41d6-a069-55f88afcf5a6">From the shortcut menu, select <strong>Lock</strong> &gt; <strong>Lock Diagram Content for Edit</strong>.</li></ol><p>OR</p><ol><li data-uuid="b77ae993-21f0-465e-98bc-e80c29fddc07">Right-click a free space on this diagram pane.</li><li data-uuid="235cf01d-53e0-47f3-9b89-3ddc4f02d195">From the shortcut menu, select <strong>Lock Diagram</strong> &gt; <strong>Lock Diagram Content for Edit</strong>.</li></ol></td></tr><tr class=""><td colspan="1"><p>At least one of the following:</p><ul><li data-uuid="d01ddbb6-f7d0-44d4-9841-a1fb7c8614cf"><p>Symbol properties of a single element represented on a diagram pane</p></li><li data-uuid="9689df9d-165e-49d0-a88b-a9f2ea1a064c">Position of the symbol on the diagram pane</li></ul></td><td colspan="1"><ol><li data-uuid="775722d8-b7a1-4915-a27d-8169115d4242">Right-click the symbol of that element on a diagram pane.</li><li data-uuid="df8a1bca-7c39-4b12-aaf7-d82a5ad51224">From the shortcut menu, select <strong>Lock</strong> &gt; <strong>Lock Element for Edit in Diagram</strong>.</li></ol></td></tr></tbody></table><h3><span style="color:var(--ds-text,#000000);">Locking symbol styles</span></h3><p>You can lock symbol styles via the <strong>Lock View</strong> tab or the <strong>Project Options</strong> dialog.</p><p><br /></p><p>To lock symbol styles via the <strong>Lock View</strong> tab</p><hr /><ol><li data-uuid="368c73aa-bd96-4636-b163-b75059fc6325"><p>In the <strong>Lock View</strong> tab on the Model Browser, expand <em>Project Options</em>.<br /><br /></p><ac:structured-macro ac:name="expand" ac:schema-version="1" ac:macro-id="92907ee3-184d-4f2b-a91e-cfe471e306c6"><ac:parameter ac:name="title">Where is the Lock View tab?</ac:parameter><ac:rich-text-body>It is the last tab on the Model Browser. If the tab is closed, you can simply open it by selecting <strong>Collaborate</strong> &gt; <strong>View Locked Elements</strong>.</ac:rich-text-body></ac:structured-macro></li><li data-uuid="80a7ed68-fc84-47d8-b7a7-831c25512793">Right-click <em>Symbol Styles</em> and from the shortcut menu select <strong>Lock Symbol Styles for Edit</strong>.</li></ol><p><br /></p><p>To lock symbol styles via the<strong> Project Options</strong> dialog</p><hr /><ol><li data-uuid="2d5ad2b2-6a4f-4b6d-9627-48e2f3443f27">Do either:<ul><li>Select <strong>Options</strong> &gt; <strong>Project</strong>.</li><li><p>In the <strong>Lock View</strong> tab on the Model Browser, right-click <em>Project Options</em> and from the shortcut menu, select <strong>Symbol Styles</strong>.<br /><br /></p><ac:structured-macro ac:name="expand" ac:schema-version="1" ac:macro-id="21d002dc-1495-4aad-a35a-12301dc0896d"><ac:parameter ac:name="title">Where is the Lock View tab?</ac:parameter><ac:rich-text-body>It is the last tab on the Model Browser. If the tab is closed, you can simply open it by selecting <strong>Collaborate</strong> &gt; <strong>View Locked Elements</strong>.</ac:rich-text-body></ac:structured-macro></li></ul></li><li data-uuid="8f16b5ee-ad5c-451f-b4ce-b46f9ad21858">In the <strong>Project Options</strong> dialog, click the<strong> Lock Symbol Styles for Edit</strong> button.</li></ol><p><br /></p><p><ac:image ac:title="Locking symbol styles via the Project Options dialog" ac:alt="Locking symbol styles via the Project Options dialog"><ri:attachment ri:filename="Locking_symbol_styles_for_edit.png" /></ac:image></p><p><br /></p><p>As a result, symbol styles become editable. Additionally, the <strong>Make Default</strong> button (1) in all <strong>Symbol Properties</strong> dialogs and the<strong> Set Selected Symbol Style as Default</strong> button (2) on all the diagram toolbars become available.</p><p><ac:image ac:title="Symbol style manipulation buttons" ac:alt="Symbol style manipulation buttons"><ri:attachment ri:filename="available_buttons.png" /></ac:image></p><h3>Locking project usages</h3><p>To lock a used project</p><hr /><ol><li data-uuid="fa5a762d-70aa-4d0e-a51d-af91e527ac25">From the <strong>Options</strong> menu, select <strong>Project Usages</strong>. The <strong>Project Usages </strong>dialog opens.</li><li data-uuid="e16c8792-22ec-43f5-827b-04534bd13833"><p>Select a used project on the left side of the dialog.</p></li><li data-uuid="344f52d2-4f0c-48ce-bdef-77b371decfdb">Click the <ac:image ac:thumbnail="true" ac:height="12"><ri:attachment ri:filename="lock_in_spec.png" /></ac:image> button <span style="color:var(--ds-text,#333333);">to lock the used project.</span></li></ol><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="ac0e76a5-8ae3-4829-8bdb-a3a08b2944bf"><ac:parameter ac:name="title">Shortcut menu</ac:parameter><ac:rich-text-body><p>This step can be done via shortcut menu. Right-click project and then select <strong>Lock</strong>.<strong> </strong></p></ac:rich-text-body></ac:structured-macro><p>You can then import this used project as a package to the main project, stop using it, or change its version.</p><p><br /></p><p class="auto-cursor-target"><strong>Related pages</strong></p><ul><li data-uuid="092c553f-4e6e-4069-879e-f35b402da697"><ac:link><ri:page ri:content-title="Unlocking model" /></ac:link></li><li data-uuid="c899836f-b824-45d4-a834-4b9021d3f7ea"><ac:link><ri:page ri:content-title="Committing changes to Teamwork Cloud" /></ac:link></li></ul><p class="auto-cursor-target"><br /></p>
````

<!--NOMAGIC_PAGE id=243970342 space=CM version=1 -->
## PAGE 00267: Locking model for editing

- page_id: `243970342`
- space_key: `CM`
- source_url: https://docs.nomagic.com/spaces/CM/pages/243970342/Locking+model+for+editing
- version_number: 1
- version_date: `2025-07-31T10:51:48.349+02:00`
- ancestors: Client-Side Collaborative Modeling Documentation > Collaboration powered by 3DEXPERIENCE platform > Locking models in 3DEXPERIENCE platform
- labels: []

### NORMALIZED CONTENT

#### CONTENT-LAYER: Shortcut menu

1217182917

INLINE

#### CONTENT-COLUMN: Shortcut menu

1217182920

INLINE

1217182914

INLINE

**On this page**

#### CONTENT-BLOCK: Shortcut menu

1217182919

INLINE

You must lock the part of the model you are going to edit to prevent other users from editing it at the same time. Locking is allowed if that part of the model is not locked by another user, because an item can only be locked by one user at a time.

The following table outlines what you can edit after you lock a single element, single diagram, diagram with elements, and so on:

| When you lock... | You can... |
| --- | --- |
| Element | Edit element specification properties (in the Specification window) |
| Diagram | Edit:Diagram specification properties (in the Specification window)Diagram properties (in the Diagram Properties dialog)Symbol layout on the diagram paneSymbol properties (in the Symbol Properties dialog) |
| Diagram with elements | Edit:Diagram specification properties (in the Specification window)Element specification properties (in the Specification window and on the diagram pane)Diagram properties (in the Symbol Properties dialog)Symbol properties (in the Symbol Properties dialog)Symbol layout on the diagram pane |
| Symbol styles | Edit properties of symbol styles (in the Project Options dialog) |
| Project usages | Import used projects as packages into the main projectStop using projectsChange versions of used projects |

##### Locking without forced project update

You can lock elements without forcing an update of a project to the latest versionif the selectedelements are not locked or do not have changes in a newer version on the server.

This feature can be enabled/disabled in the **Environment Options** dialog.

To enable/disable locking without updating

1. Select Options > Environment > Collaboration node.
2. Find Enable Locking Without Forced Project Update . Do one of the following:
  - Set to true, to enable locking without updating;
  - Set to false, to disable locking without updating .

#### NOTE: An example

There is a 60-second threshold; iflocking takes longer than 60 seconds, a project update will be required.

#### TIP: An example

An example

You are trying to lock package B, which contains many elements, recursively. The modeling tool cannot check all contained elements' status in later versions of the project in 60 seconds. After 60 seconds, a project update will be requiredto lock the package.

##### representRepresentation of locked elements

In the Containment tree, element names are represented in two colors:

- Unlocked elements are represented in black, meaning they are editable.
- Locked elements are represented in gray, meaning they are not editable.

[IMAGE alt='' src='']

##### Locking elements and diagrams

If you want to lock all lockable elements, [CONFLUENCE_PAGE title='Lock-Free Editing mode' space=''] to work in a lock-required mode.

Elements and diagrams can be locked by using the commands from their shortcut menu.

[IMAGE alt='' src='']

Elements can also be locked by clicking the Lock element for the Edit button [IMAGE alt='' src=''] on their Specification window.

[IMAGE alt='' src='']

The following table provides suggestions on which locking commands to use for different purposes.

| If you need to edit... | Do the following |
| --- | --- |
| Specification properties of a single element | Right-click either:The element in the Model Browser.A symbol of the element on a diagram pane.From the shortcut menu, select Lock > Lock Element for Edit.ORDouble-click either:The element in the Model Browser.A symbol of the element on a diagram pane.In the Specification window, click Lock Element for Edit. |
| Specification properties of both an element and the elements it contains (owns)For example, a project has a Package Analysis, containing two inner Packages- Design and Implementation. Each inner Package also contains elements.Lock the Package Analysis recursively to edit all the elements in this Package. | Right-click either:This element in the Model Browser.A symbol of this element on a diagram pane.From the shortcut menu, select Lock > Lock Elements for Edit Recursively |
| At least one of the following:Diagram representation properties (including diagram layout)Symbol properties of elements represented on that diagram pane | Right-click this diagram in the Model Browser.From the shortcut menu, select Lock > Lock Diagram for Edit.ORRight-click a free space on this diagram pane.From the shortcut menu, select Lock Diagram > Lock Diagram for Edit. |
| At least one of the following:Diagram specification propertiesDiagram representation properties (including diagram layout)Properties of elements represented on that diagram paneSymbol properties of elements represented on that diagram pane | Right-click this diagram in the Model Browser.From the shortcut menu, select Lock > Lock Diagram Content for Edit.ORRight-click a free space on this diagram pane.From the shortcut menu, select Lock Diagram > Lock Diagram Content for Edit. |
| At least one of the following:Symbol properties of a single element represented on a diagram panePosition of the symbol on the diagram pane | Right-click the symbol of that element on a diagram pane.From the shortcut menu, select Lock > Lock Element for Edit in Diagram. |

##### Locking symbol styles

You can lock symbol styles via the **Lock View** tab or the **Project Options** dialog.

To lock symbol styles via the **Lock View** tab

1. In the **Lock View** tab on the Model Browser, expand *Project Options*. Where is the Lock View tab?It is the last tab on the Model Browser. If the tab is closed, you can simply open it by selecting **Collaborate** > **View Locked Elements**.
2. Right-click Symbol Styles and from the shortcut menu select Lock Symbol Styles for Edit .

To lock symbol styles via the**Project Options** dialog

1. Do either:
  - Select Options > Project .
  - In the **Lock View** tab on the Model Browser, right-click *Project Options* and from the shortcut menu, select **Symbol Styles**. Where is the Lock View tab?It is the last tab on the Model Browser. If the tab is closed, you can simply open it by selecting **Collaborate** > **View Locked Elements**.
2. In the Project Options dialog, click Lock Symbol Styles for Edit .

[IMAGE alt='' src='']

As a result, symbol styles become editable. Additionally, the **Make Default** button (1) in all **Symbol Properties** dialogs and the**Set Selected Symbol Style as Default** button (2) on all the diagram toolbars become available, as shown below.

[IMAGE alt='' src='']

##### Locking project usages

To lock a used project

1. From the Options menu, select Project Usages . The Project Usages dialog opens.
2. Select a used project on the left side of the dialog.
3. Click the [ATTACHMENT filename='lock_in_spec.png'] button to lock the used project.

#### TIP: Shortcut menu

Shortcut menu

You can use a shortcut menu for this step. Right-click the project and then select **Lock**.****

You can then import the used project as a package to the main project, stop using it, or change its version.

1217187869

INLINE

**Related pages**

- [CONFLUENCE_PAGE title='Unlocking model' space='']
- [CONFLUENCE_PAGE title='Committing changes to Teamwork Cloud' space='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="5bb4f2d9-5ce1-40ab-9971-0503911ba9de"><ac:parameter ac:name="id">1217182917</ac:parameter><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="9dcf7b61-8883-4420-b237-ee66e7bfaf6e"><ac:parameter ac:name="id">1217182920</ac:parameter><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="3aa68d28-dc9a-43d7-abed-1b92cba1eb5a"><ac:parameter ac:name="id">1217182914</ac:parameter><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><p class="auto-cursor-target"><strong>On this page</strong></p><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="307e8173-eb92-4008-a7df-b26929fbd8ed" /></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="4b12672b-6b6a-4a75-88c3-1bf071db3115"><ac:parameter ac:name="id">1217182919</ac:parameter><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p>You must lock the part of the model you are going to edit to prevent other users from editing it at the same time. Locking is allowed if that part of the model is not locked by another user, because an item can only be locked by one user at a time. </p><p>The following table outlines what you can edit after you lock a single element, single diagram, diagram with elements, and so on:</p><table class="wrapped"><colgroup><col /><col /></colgroup><tbody><tr><th>When you lock...</th><th>You can...</th></tr><tr><td>Element</td><td>Edit element specification properties (in the Specification window)</td></tr><tr><td>Diagram</td><td><p>Edit:</p><ul><li>Diagram specification properties (in the Specification window)</li><li>Diagram properties (in the <strong>Diagram Properties</strong> dialog)</li><li>Symbol layout on the diagram pane</li><li>Symbol properties (in the <strong>Symbol Properties</strong> dialog)</li></ul></td></tr><tr><td>Diagram with elements</td><td><p>Edit:</p><ul><li>Diagram specification properties (in the Specification window)</li><li>Element specification properties (in the Specification window and on the diagram pane)</li><li>Diagram properties (in the <strong>Symbol Properties</strong> dialog)</li><li>Symbol properties (in the <strong>Symbol Properties</strong> dialog)</li><li>Symbol layout on the diagram pane</li></ul></td></tr><tr><td colspan="1">Symbol styles</td><td colspan="1"><p>Edit properties of symbol styles (in the <strong>Project Options</strong> dialog)</p></td></tr><tr><td colspan="1">Project usages</td><td colspan="1"><ul><li>Import used projects as packages into the main project</li><li>Stop using projects</li><li>Change versions of used projects</li></ul></td></tr></tbody></table><p class="auto-cursor-target"><br /></p><h3>Locking without forced project update</h3><p>You can lock elements without forcing an update of a project to the latest version<ac:inline-comment-marker ac:ref="230f6a8c-602d-4b0c-920c-6e1138948405"> if the selected </ac:inline-comment-marker><span style="color: rgb(62,63,64);">elements are not locked or do not have changes in a newer version on the server. </span></p><p><span style="color: rgb(62,63,64);">This feature can be</span> enabled/disabled in the <strong>Environment Options</strong> dialog.</p><p>To enable/disable locking without updating</p><hr /><ol><li>Select <strong>Options</strong> &gt; <strong><ac:inline-comment-marker ac:ref="8d4988b6-6639-49d9-9791-dc38b54d5da4">Environment </ac:inline-comment-marker></strong><ac:inline-comment-marker ac:ref="8d4988b6-6639-49d9-9791-dc38b54d5da4">&gt;</ac:inline-comment-marker> <strong>Collaboration </strong>node.</li><li><ac:inline-comment-marker ac:ref="336aeb9d-5598-4131-a86e-46599ec84269">Find</ac:inline-comment-marker> <strong>Enable Locking Without Forced Project Update</strong>. Do one of the following: <ul><li>Set to <em>true, </em>to enable <span style="color: rgb(62,63,64);">locking without updating;</span></li><li>Set to<em> false, </em>to disable <span style="color: rgb(62,63,64);">locking without updating</span>. </li></ul></li></ol><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="6cc4ef97-4cde-4bc9-907e-89f11ac34a94"><ac:rich-text-body><p>There is a 60-second <ac:inline-comment-marker ac:ref="2bb7464b-a64f-4c04-aee6-71e61191f08e">threshold; if</ac:inline-comment-marker><span style="color: rgb(62,63,64);"> locking takes longer than 60 seconds, a project update will be required.</span></p><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="85b7cfd4-f4c0-484d-a506-1b41e27ef468"><ac:parameter ac:name="title">An example</ac:parameter><ac:rich-text-body><p><span>You are trying to lock package B, which contains many elements, recursively. The modeling tool cannot check all contained elements' status in later versions of the project in 60 seconds. After 60 seconds, a project update will be required </span><span>to lock the package.</span></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><h3><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="ed9519ee-5388-48a8-a877-3827fd18e096"><ac:parameter ac:name="">represent</ac:parameter></ac:structured-macro>Representation of locked elements</h3><p>In the Containment tree, element names are represented in two colors:</p><ul><li>Unlocked elements are represented in black, meaning they are editable.</li><li>Locked elements are represented in gray, meaning they are not editable.</li></ul><p><ac:image ac:title="Locked and unlocked elements in the Containment tree" ac:alt="Locked and unlocked elements in the Containment tree"><ri:attachment ri:filename="locked_and_unlocked_elems.png" /></ac:image></p><h3>Locking <ac:inline-comment-marker ac:ref="01a040cf-2090-4700-a28e-5123efd07ec4">elements</ac:inline-comment-marker> and diagrams</h3><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="f21153a2-c92b-49ca-bf2e-a8346fd6c859"><ac:rich-text-body><p>If you want to lock all lockable elements, <ac:link ac:anchor="Disabling the Lock-Free Editing mode"><ri:page ri:content-title="Lock-Free Editing mode" /><ac:plain-text-link-body><![CDATA[disable lock-free editing]]></ac:plain-text-link-body></ac:link> to work in a lock-required mode.</p></ac:rich-text-body></ac:structured-macro><p><span style="letter-spacing: 0.0px;">Elements and diagrams can be locked by using the commands from their shortcut menu.</span></p><p><ac:image ac:title="Locking commands on the shortcut menu of the Package" ac:alt="Locking commands on the shortcut menu of the Package"><ri:attachment ri:filename="locking_commands_on_shortcut_menu.png" /></ac:image></p><p><br /></p><p>Elements can also be locked by clicking the Lock element for the Edit button <ac:image><ri:attachment ri:filename="lock_in_spec.png"><ri:page ri:space-key="MT" ri:content-title="_MD buttons" /></ri:attachment></ac:image> on their Specification window.</p><p><ac:image ac:title="Locking command in the element's Specification window" ac:alt="Locking command in the element's Specification window"><ri:attachment ri:filename="locking_command_in_spec_window.png" /></ac:image></p><p><br /></p><p>The following table provides suggestions on which locking commands to use for different purposes.</p><table class="wrapped"><colgroup><col /><col /></colgroup><tbody><tr><th>If you need to edit...</th><th>Do the following</th></tr><tr><td><p>Specification properties of a single element</p></td><td><div class="content-wrapper"><ol><li>Right-click either:<ul><li>The element in the Model Browser.</li><li>A symbol of the element on a diagram pane.</li></ul></li><li>From the shortcut menu, select <strong>Lock</strong> &gt; <strong>Lock Element for Edit</strong>.</li></ol><p>OR</p><ol><li>Double-click either:<ul><li>The element in the Model Browser.</li><li>A symbol of the element on a diagram pane.</li></ul></li><li>In the Specification window, click <strong>Lock Element for Edit</strong>.</li></ol></div></td></tr><tr><td><div class="content-wrapper"><p><span>Specification properties of both an element and the elements it contains (owns)</span></p><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="35433209-e864-4b2f-b359-b9ca1dc4348b"><ac:rich-text-body><p>For example, a project has a Package <em>Analysis</em>, containing two inner Packages<br />- <em>Design</em> and <em>Implementation</em>. Each inner Package also contains elements.</p><p>Lock the Package <em>Analysis </em>recursively to edit all the elements in this Package.</p></ac:rich-text-body></ac:structured-macro><p><span><br /></span></p></div></td><td><ol><li>Right-click either:<ul><li>This element in the Model Browser.</li><li>A symbol of this element on a diagram pane.</li></ul></li><li>From the shortcut menu, select <strong>Lock</strong> &gt; <strong style="line-height: 1.4285715;">Lock Elements for Edit Recursively</strong></li></ol></td></tr><tr><td colspan="1"><p>At least one of the following:</p><ul><li>Diagram representation properties (including diagram layout)</li><li>Symbol properties of elements represented on that diagram pane</li></ul></td><td colspan="1"><ol><li>Right-click this diagram in the Model Browser.</li><li>From the shortcut menu, select <strong>Lock</strong> &gt; <strong>Lock Diagram for Edit</strong>.</li></ol><p>OR</p><ol><li>Right-click a free space on this diagram pane.</li><li>From the shortcut menu, select <strong>Lock Diagram</strong> &gt; <strong>Lock Diagram for Edit</strong>.</li></ol></td></tr><tr><td colspan="1"><p>At least one of the following:</p><ul><li>Diagram specification properties</li><li>Diagram representation properties (including diagram layout)</li><li>Properties of elements represented on that diagram pane</li><li>Symbol properties of elements represented on that diagram pane</li></ul></td><td colspan="1"><ol><li>Right-click this diagram in the Model Browser.</li><li>From the shortcut menu, select <strong>Lock</strong> &gt; <strong>Lock Diagram Content for Edit</strong>.</li></ol><p>OR</p><ol><li>Right-click a free space on this diagram pane.</li><li>From the shortcut menu, select <strong>Lock Diagram</strong> &gt; <strong>Lock Diagram Content for Edit</strong>.</li></ol></td></tr><tr><td colspan="1"><p>At least one of the following:</p><ul><li><p>Symbol properties of a single element represented on a diagram pane</p></li><li>Position of the symbol on the diagram pane</li></ul></td><td colspan="1"><ol><li>Right-click the symbol of that element on a diagram pane.</li><li>From the shortcut menu, select <strong>Lock</strong> &gt; <strong>Lock Element for Edit in Diagram</strong>.</li></ol></td></tr></tbody></table><h3><span style="color: rgb(0,0,0);">Locking symbol styles</span></h3><p>You can lock symbol styles via the <strong>Lock View</strong> tab or the <strong>Project Options</strong> dialog.</p><p><br /></p><p>To lock symbol styles via the <strong>Lock View</strong> tab</p><hr /><ol><li><p>In the <strong>Lock View</strong> tab on the Model Browser, expand <em>Project Options</em>.<br /><br /></p><ac:structured-macro ac:name="expand" ac:schema-version="1" ac:macro-id="92907ee3-184d-4f2b-a91e-cfe471e306c6"><ac:parameter ac:name="title">Where is the Lock View tab?</ac:parameter><ac:rich-text-body>It is the last tab on the Model Browser. If the tab is closed, you can simply open it by selecting <strong>Collaborate</strong> &gt; <strong>View Locked Elements</strong>.</ac:rich-text-body></ac:structured-macro></li><li>Right-click <em>Symbol Styles</em> and from the shortcut menu select <strong>Lock Symbol Styles for Edit</strong>.</li></ol><p><br /></p><p>To lock symbol styles via the<strong> Project Options</strong> dialog</p><hr /><ol><li>Do either:<ul><li>Select <strong>Options</strong> &gt; <strong>Project</strong>.</li><li><p>In the <strong>Lock View</strong> tab on the Model Browser, right-click <em>Project Options</em> and from the shortcut menu, select <strong>Symbol Styles</strong>.<br /><br /></p><ac:structured-macro ac:name="expand" ac:schema-version="1" ac:macro-id="21d002dc-1495-4aad-a35a-12301dc0896d"><ac:parameter ac:name="title">Where is the Lock View tab?</ac:parameter><ac:rich-text-body>It is the last tab on the Model Browser. If the tab is closed, you can simply open it by selecting <strong>Collaborate</strong> &gt; <strong>View Locked Elements</strong>.</ac:rich-text-body></ac:structured-macro></li></ul></li><li>In the <strong>Project Options</strong> dialog, click<strong> Lock Symbol Styles for Edit</strong>.</li></ol><p><br /></p><p><ac:image ac:title="Locking symbol styles via the Project Options dialog" ac:alt="Locking symbol styles via the Project Options dialog"><ri:attachment ri:filename="Locking_symbol_styles_for_edit.png" /></ac:image></p><p><br /></p><p>As a result, symbol styles become editable. Additionally, the <strong>Make Default</strong> button (1) in all <strong>Symbol Properties</strong> dialogs and the<strong> Set Selected Symbol Style as Default</strong> button (2) on all the diagram toolbars become available, as shown below.</p><p><ac:image ac:title="Symbol style manipulation buttons" ac:alt="Symbol style manipulation buttons"><ri:attachment ri:filename="available_buttons.png" /></ac:image></p><h3>Locking project usages</h3><p>To lock a used project</p><hr /><ol><li>From the <strong>Options</strong> menu, select <strong>Project Usages</strong>. The <strong>Project Usages </strong>dialog opens.</li><li><p>Select a used project on the left side of the dialog.</p></li><li>Click the <ac:image ac:thumbnail="true" ac:height="12"><ri:attachment ri:filename="lock_in_spec.png"><ri:page ri:space-key="MT" ri:content-title="_MD buttons" /></ri:attachment></ac:image> button <span style="color: rgb(62,63,64);">to lock the used project.</span></li></ol><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="ac0e76a5-8ae3-4829-8bdb-a3a08b2944bf"><ac:parameter ac:name="title">Shortcut menu</ac:parameter><ac:rich-text-body><p>You can use a shortcut menu for this step. Right-click the project and then select <strong>Lock</strong>.<strong> </strong></p></ac:rich-text-body></ac:structured-macro><p>You can then import the used project as a package to the main project, stop using it, or change its version.</p></ac:layout-cell></ac:layout-section></ac:layout></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="d3f1cf83-12fa-438d-9af5-153ec2353304"><ac:parameter ac:name="id">1217187869</ac:parameter><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><p class="auto-cursor-target"><strong>Related pages</strong></p><ul><li><ac:link><ri:page ri:content-title="Unlocking model" /></ac:link></li><li><ac:link><ri:page ri:content-title="Committing changes to Teamwork Cloud" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p>
````

<!--NOMAGIC_PAGE id=243970308 space=CM version=1 -->
## PAGE 00268: Locking models in 3DEXPERIENCE platform

- page_id: `243970308`
- space_key: `CM`
- source_url: https://docs.nomagic.com/spaces/CM/pages/243970308/Locking+models+in+3DEXPERIENCE+platform
- version_number: 1
- version_date: `2025-07-31T10:51:47.957+02:00`
- ancestors: Client-Side Collaborative Modeling Documentation > Collaboration powered by 3DEXPERIENCE platform
- labels: []

### NORMALIZED CONTENT

Lock-Free Editing is the default mode for **3D**EXPERIENCEprojects; only diagrams, used projects, and symbol styles can have locks.

If you want to start locking all the lockable elements, you can [CONFLUENCE_PAGE title='Lock-Free Editing mode' space=''] and work in a lock-required mode.

Read about project locking in the following topics:

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>Lock-Free Editing is the default mode for <span style="color: rgb(55,65,81);"><strong>3D</strong>EXPERIENCE </span>projects; <span style="color: rgb(23,43,77);">only diagrams, used projects, and symbol styles can have locks.</span></p><p>If you want to start locking all the lockable elements, you can <ac:link ac:anchor="Disabling the Lock-Free Editing mode"><ri:page ri:content-title="Lock-Free Editing mode" /><ac:plain-text-link-body><![CDATA[disable lock-free editing]]></ac:plain-text-link-body></ac:link> and work in a lock-required mode.</p><p>Read about project locking in the following topics:</p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="64c33836-2d0d-4862-a939-e63d91ab1c44" /></p>
````

<!--NOMAGIC_PAGE id=243970164 space=CM version=2 -->
## PAGE 00269: Logging in to 3DEXPERIENCE platform

- page_id: `243970164`
- space_key: `CM`
- source_url: https://docs.nomagic.com/spaces/CM/pages/243970164/Logging+in+to+3DEXPERIENCE+platform
- version_number: 2
- version_date: `2025-09-11T12:09:50.621+02:00`
- ancestors: Client-Side Collaborative Modeling Documentation > Collaboration powered by 3DEXPERIENCE platform
- labels: []

### NORMALIZED CONTENT

The**3D**EXPERIENCE menu groups all available integrations with the **3D**EXPERIENCE platform. For some functionalities to work, you need to log in to the **3D**EXPERIENCE platform as described below. You can log in to the platform either on-premises or on the cloud server.

- To avoid connection issues related to certificates that are not trusted, we recommend installing a self-signed certificate to JRE.
- If you are launching a modeling tool from the 3D EXPERIENCE platform, you are logged in automatically.
- To avoid issues when launching the modeling tool, set it as the default app for .mdzip files: select Windows Settings > Apps > Default apps > Choose default apps by file type > choose your modeling tool as the default app for .mdzip files.

##### Logging in to the 3DEXPERIENCE platform

To log in to the **3D**EXPERIENCE platform from the modeling tool

1. In the main menu, select 3DEXPERIENCE > Login . If the **Login** command is not available, make sure to [CONFLUENCE_PAGE title='Enabling 3DEXPERIENCE collaboration' space='']enable collaboration powered by the **3D**EXPEREINCE platform.
2. In the **Server** box of the open dialog, enter the server address.
3. If the **3D**EXPERIENCE****platform is deployed on the cloud, select **The 3DEXPERIENCE platform is hosted on the cloud** check box. 
 
[IMAGE alt='' src='']
4. Click OK .
5. In the open dialog, enter your 3D EXPERIENCE username and click Continue .
6. In the password box enter your 3D EXPERIENCE password.
7. Click Log in . [ATTACHMENT filename='logging_in_to_platform.png']

Once you log in to the **3D**EXPERIENCE platform, you can use all functionalities of the installed plugins without canceling the session.

3D

##### Switching platform/credentials

Once you log in to the **3D**EXPERIENCE platform, you can switch to a different platform, the platform's collaborative space, or a different access role without terminating your session.

To switch to a different **3D**EXPERIENCE platform/credentials

1. In the main menu, select 3DEXPERIENCE > Switch Platform/Credentials .
2. In the **Switch Platform/Credentials**dialog, select the platform and/or credentials you want to switch to and click**OK**. 
 
[IMAGE alt='' src=''] The **Switch Platform/Credentials** dialog lists only the platforms, collaborative spaces, and roles you can access. Platforms are displayed in the first drop-down list. Collaborative spaces and credentials in the second drop-down list are displayed in the following format: Collaborative Space• Access Role.

##### Logging out of the 3DEXPERIENCE platform

When you finish working on a project in the **3D**EXPERIENCE platform, you can terminate your session by logging out of the platform.

To log out of the **3D**EXPERIENCE platform

- In the main menu, select 3DEXPERIENCE > Logout .

##### Launching a modeling tool from the 3DEXPERIENCE platform

To launch a modeling tool from the **3D**EXPERIENCE platform

1. Log in to the 3D EXPERIENCE platform with your 3D EXPERIENCE username and password.
2. Click the Compass icon [ATTACHMENT filename='compass.png'] in the upper left corner.
3. Select Design with CATIA Magic.

The tool launches and you are automatically logged in to the platform.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>The<strong> 3D</strong>EXPERIENCE menu groups all available integrations with the <strong>3D</strong>EXPERIENCE platform. For some functionalities to work, you need to log in to the <strong>3D</strong>EXPERIENCE platform as described below. You can log in to the platform either on-premises or on the cloud server.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="8e84cb98-e792-43e8-9d2a-1e898ce62ec9"><ac:rich-text-body><ul><li>To avoid connection issues related to certificates that are not trusted, we recommend installing a self-signed certificate to JRE.</li><li>If you are launching a modeling tool from the <strong>3D</strong>EXPERIENCE platform, you are logged in automatically.</li><li>To avoid issues when launching the modeling tool, set it as the default app for .mdzip files: select <strong>Windows Settings &gt; Apps &gt; Default apps &gt; Choose default apps by file type &gt; </strong>choose your modeling tool as the default app for .mdzip files.</li></ul></ac:rich-text-body></ac:structured-macro><h3>Logging in to the 3DEXPERIENCE platform</h3><p>To log in to the <strong>3D</strong>EXPERIENCE platform from the modeling tool</p><hr /><ol><li>In the main menu, select <strong>3DEXPERIENCE</strong> &gt;<strong> Login</strong>.<br /><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="eb1f5103-8a11-471e-b2e7-8b25eed3d678"><ac:rich-text-body><p>If the <strong>Login</strong> command is not available, make sure to <ac:link><ri:page ri:content-title="Enabling 3DEXPERIENCE collaboration" /><ac:link-body>enable collaboration powered by the <strong>3D</strong>EXPEREINCE platform</ac:link-body></ac:link>. </p></ac:rich-text-body></ac:structured-macro></li><li><p class="auto-cursor-target">In the <strong>Server</strong> box of the open dialog, enter the server address.</p></li><li><p class="auto-cursor-target">If the <strong>3D</strong>EXPERIENCE<strong> </strong>platform is deployed on the cloud, select <strong>The 3DEXPERIENCE platform is hosted on the cloud</strong> check box.<br /><br /><ac:image><ri:attachment ri:filename="login_dialog.png" /></ac:image><br /><br /></p></li><li>Click <strong>OK</strong>.</li><li>In the open dialog, enter your<strong> 3D</strong>EXPERIENCE username and click <strong>Continue</strong>.</li><li>In the password box enter your <strong style="letter-spacing: 0.0px;">3D</strong><span style="letter-spacing: 0.0px;">EXPERIENCE password.</span></li><li>Click <strong>Log in</strong>.<br /><br /><ac:image><ri:attachment ri:filename="logging_in_to_platform.png" /></ac:image></li></ol><p><br />Once you log in to the <strong>3D</strong>EXPERIENCE platform, you can use all functionalities of the installed plugins without canceling the session.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="b5840a66-10ef-410a-91bc-6979d67e6dab"><ac:rich-text-body>When logging in to the cloud-based<strong> 3D</strong>EXPERIENCE platform, ensure you have all the required roles and/or licenses to use the platform and its applications. If you do not have the necessary roles and/or licenses, you will receive a notification suggesting that you choose a different platform. If you still encounter login issues, contact the person responsible for the role and license configuration.</ac:rich-text-body></ac:structured-macro><h3><br />Switching platform/credentials</h3><p>Once you log in to the <strong>3D</strong>EXPERIENCE platform, you can switch to a different platform, the platform's collaborative space, or a different access role without terminating your session.</p><p><br /></p><p>To switch to a different <strong>3D</strong>EXPERIENCE platform/credentials</p><hr /><ol><li>In the main menu, select <strong>3DEXPERIENCE</strong> &gt; <strong>Switch Platform/Credentials</strong>.</li><li><p class="auto-cursor-target">In the <strong>Switch Platform/Credentials</strong><span> dialog, select the platform and/or credentials you want to switch to and click </span><strong>OK</strong><span>.</span><br /><br /><ac:image><ri:attachment ri:filename="switch_platform_credentials.png" /></ac:image></p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="78dece3c-4435-4da9-9ee2-deccb7eeb478"><ac:rich-text-body><p>The <strong>Switch Platform/Credentials</strong> dialog lists only the platforms, collaborative spaces, and roles you can access. Platforms are displayed in the first drop-down list. Collaborative spaces and credentials in the second drop-down list are displayed in the following format: Collaborative Space<span> • Access Role.</span></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></li></ol><h3>Logging out of the 3DEXPERIENCE platform</h3><p>When you finish working on a project in the <strong>3D</strong>EXPERIENCE platform, you can terminate your session by logging out of the platform.</p><p><br /></p><p>To log out of the <strong>3D</strong>EXPERIENCE platform</p><hr /><ul><li>In the main menu, select <strong>3DEXPERIENCE</strong> &gt; <strong>Logout</strong>.</li></ul><h3>Launching a modeling tool from the 3DEXPERIENCE platform</h3><p>To launch a modeling tool from the <strong>3D</strong>EXPERIENCE platform</p><hr /><ol><li>Log in to the <strong>3D</strong>EXPERIENCE platform with your <strong>3D</strong>EXPERIENCE username and password.</li><li>Click the <strong>Compass </strong>icon <ac:image ac:thumbnail="true" ac:width="26"><ri:attachment ri:filename="compass.png" /></ac:image> in the upper left corner.</li><li>Select <strong>Design with CATIA Magic.</strong></li></ol><p><br />The tool launches and you are automatically logged in to the platform.</p>
````

<!--NOMAGIC_PAGE id=286556221 space=CM version=8 -->
## PAGE 00270: Manage Profiles

- page_id: `286556221`
- space_key: `CM`
- source_url: https://docs.nomagic.com/spaces/CM/pages/286556221/Manage+Profiles
- version_number: 8
- version_date: `2026-02-18T08:17:06.397+01:00`
- ancestors: Client-Side Collaborative Modeling Documentation > Collaboration powered by 3DEXPERIENCE platform > Technical practices
- labels: []

### NORMALIZED CONTENT

This Technical Practice highlights the importance of managing profiles on the**3D**EXPERIENCE platform. It describes how to upload and maintain them on the**3D**EXPERIENCE platform.

#### Why

Every CATIA Magic systems model requires profiles. All profiles and libraries that are bundled with the modeling tool are considered as standard profiles, non-modifiable and essential for the proper performance of the tool. Accessing these standard profiles is mandatory to open a CATIA Magic system model stored in the**3D**EXPERIENCE platform. Since profiles are essential for working with CATIA Magic, a profile administrator is necessary to manage profiles and avoid their modification by other users.

#### What

This technical practice highlights the importance of managing profiles on the**3D**EXPERIENCE platform. It describes how to upload and maintain them on the**3D**EXPERIENCE platform.

#### Target Audience

Profile Administrator

#### Knowledge

##### Standard Profiles

A standard profile is a CATIA Magic model essential for proper functioning of the tool. It contains packages that extend a reference metamodel, such as UML. Standard profiles come with the modeling tool and its plugins. To enable the CATIA Magic Power'By, they must be added to the platform and be accessible to all CATIA Magic users.

##### Collaborative Spaces

Collaborative spaces are digital workspaces, where teams and stakeholders can collaborate on various aspects of product design, development and project management.

##### Access for Collaborative Spaces

Collaborative spaces can have different levels of visibility: public, protected or private. Content in public or protected collaborative spaces is either private or public, depending on the current maturity level of the content. Content in private collaborative spaces is always private. Public collaborative spaces are typically used to store standard content. Use protected or private collaborative spaces to collaborate with other organizations. Members control who can access the content based on their role in the collaborative space and the maturity level of the objects.

The following table defines whether the content is public or private based on the type of collaborative space and the maturity state of the content.

| Collaborative Space Visibility | Maturity State |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Draft | In Work | Frozen | Released | Obsolete |  |
| Public | Private | Public | Public | Public | Public |
| Protected | Private | Private | Private | Public | Public |
| Private | Private | Private | Private | Private | Private |

##### Maturities of System Models

[IMAGE alt='' src='']

In the**3D**EXPERIENCE platform, the maturity states of a physical product help manage its lifecycle by defining distinct stages. Here is an explanation of each state:

| Private | Description: This is the initial state where a physical product is only visible to its creator or a restricted group.Purpose: This state allows early development work and iterations without broader visibility. It is useful for preliminary drafts and experimental designs that are not yet ready for a team review. |
| --- | --- |
| In Work | Description: This state indicates that the product is under active development and can be accessed and modified by designated team members.Purpose: This state facilitates collaboration among team members, enabling collective development, editing and refinement of the product. This state is crucial for iterative development and incorporating feedback. |
| Frozen | Description: The product is in a state where no further changes can be made except by an authorized personnel.Purpose: This state ensures stability before the final review and release. It allows thorough validation, testing and quality assurance without the risk of unapproved changes. This state acts as a checkpoint for critical reviews. |
| Released | Description: In this state the product is finalized, fully validated and approved for use or production.Purpose: This state marks the product as complete and ready for deployment, manufacturing, or customer use. This state signifies that the product has passed all necessary checks and meets all required standards and specifications. |
| Obsolete | Description: In this state the product is no longer in use and is retired from active development or production.Purpose: This state helps manage and archive older versions or products that are replaced by newer models. This state ensures that obsolete products are clearly marked, preventing their use in current projects and maintaining an organized product catalog. |

Each of these maturity states serves a specific role in managing the product development process, ensuring that products are developed systematically, reviewed thoroughly and transitioned smoothly from concept to completion and eventual retirement. The structured approach of the**3D**EXPERIENCE platformfor maturity states helps maintain high standards of quality, compliance and efficiency throughout the product lifecycle.

#### Use Cases

##### Use Case: Manage Profiles on the 3DEXPERIENCE Platform

###### Scenario

A Profile Administrator adds profiles to the**3D**EXPERIENCE platformfor team members to access the profile for opening a systems model.

###### Actors/personas

Jack Profile Administrator: Jack is responsible for managing the CATIA Magic Profiles on the**3D**EXPERIENCE platform.

##### Workflow

[IMAGE alt='' src='']

#### How

##### Prerequisite Roles

3DSwymer (IFW-OC), Collaborative Industry Innovator (CSV-OC), Collaborative Designer for CATIA Magic (SSY-OC), Magic Systems of Systems Architect (MYH)

##### Step 1: Upload CATIA Magic Profiles on 3DEXPERIENCE Platform

600400

##### Step 2: Change the Maturity of CATIA Magic Profiles

600400

##### Step 3: Update Profiles on 3DEXPERIENCE Platform

600400

#### Recommandation

- Ensure, you are on the right **3D**EXPERIENCE platform server and Collaborative Spaces.
  - Navigate to the **3D**EXPERIENCE menu in the CATIA Magic application.
  - Select the Switch Platform/Credentials option.
  - Select the desired platform and credentials. [ATTACHMENT filename='techPract_ManageProfile_Reco.gif']
- Ensure standard profiles are stored in a protected collaborative space, as this allows visibility to all CATIA Magic users while ensuring a good security level. However, it is also possible to use a public collaborative space.
- While migrating profiles and projects, it is recommended to have the profiles in the Released state.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="title topictitle2" style="text-align: left;"><span style="color:var(--ds-text,#000000);">This Technical Practice highlights the importance of managing profiles on the<span> </span></span><span class="ph" style="color:var(--ds-text,#000000);"><strong><span class="tm-3D">3D</span></strong>EXPERIENCE platform</span><span style="color:var(--ds-text,#000000);">. It describes how to upload and maintain them on the<span> </span></span><span class="ph" style="color:var(--ds-text,#000000);"><strong><span class="tm-3D">3D</span></strong>EXPERIENCE platform</span><span style="color:var(--ds-text,#000000);">.</span></p><h2 class="title topictitle2" style="text-align: left;">Why</h2><p>Every CATIA Magic systems model requires profiles. All profiles and libraries that are bundled with the modeling tool are considered as standard profiles, non-modifiable and essential for the proper performance of the tool. Accessing these standard profiles is mandatory to open a CATIA Magic system model stored in the<span> </span><span class="ph"><strong><span class="tm-3D">3D</span></strong>EXPERIENCE platform</span>. Since profiles are essential for working with CATIA Magic, a profile administrator is necessary to manage profiles and avoid their modification by other users.</p><h2 class="title topictitle2" style="text-align: left;">What</h2><p>This technical practice highlights the importance of managing profiles on the<span> </span><span class="ph"><strong><span class="tm-3D">3D</span></strong>EXPERIENCE platform</span>. It describes how to upload and maintain them on the<span> </span><span class="ph"><strong><span class="tm-3D">3D</span></strong>EXPERIENCE platform</span>.</p><h2 class="title topictitle2" style="text-align: left;">Target Audience</h2><p>Profile Administrator</p><h2 class="title topictitle2" style="text-align: left;">Knowledge</h2><h3 class="title topictitle3" style="text-align: left;margin-left: 0.0px;">Standard Profiles</h3><p>A standard profile is a CATIA Magic model essential for proper functioning of the tool. It contains packages that extend a reference metamodel, such as UML. Standard profiles come with the modeling tool and its plugins. To enable the CATIA Magic Power'By, they must be added to the platform and be accessible to all CATIA Magic users.</p><h3 class="title topictitle3" style="text-align: left;margin-left: 0.0px;">Collaborative Spaces</h3><p>Collaborative spaces are digital workspaces, where teams and stakeholders can collaborate on various aspects of product design, development and project management.</p><h3 class="title topictitle3" style="text-align: left;margin-left: 0.0px;">Access for Collaborative Spaces</h3><p>Collaborative spaces can have different levels of visibility: public, protected or private. Content in public or protected collaborative spaces is either private or public, depending on the current maturity level of the content. Content in private collaborative spaces is always private. Public collaborative spaces are typically used to store standard content. Use protected or private collaborative spaces to collaborate with other organizations. Members control who can access the content based on their role in the collaborative space and the maturity level of the objects.</p><p>The following table defines whether the content is public or private based on the type of collaborative space and the maturity state of the content.</p><table class="wrapped" style="margin-left: 0.0px;"><tbody><tr><td rowspan="2">Collaborative Space Visibility</td><td colspan="5">Maturity State</td></tr><tr><th scope="col"><span class="ph uicontrol" style="color:var(--ds-text,#333333);">Draft</span></th><th scope="col"><span class="ph uicontrol" style="color:var(--ds-text,#333333);">In Work</span></th><th scope="col"><span class="ph uicontrol" style="color:var(--ds-text,#333333);">Frozen</span></th><th scope="col"><span class="ph uicontrol" style="color:var(--ds-text,#333333);">Released</span></th><th scope="col"><span class="ph uicontrol" style="color:var(--ds-text,#333333);">Obsolete</span></th></tr><tr><td>Public</td><td>Private</td><td>Public</td><td>Public</td><td>Public</td><td>Public</td></tr><tr><td>Protected</td><td>Private</td><td>Private</td><td>Private</td><td>Public</td><td>Public</td></tr><tr><td>Private</td><td>Private</td><td>Private</td><td>Private</td><td>Private</td><td>Private</td></tr></tbody></table><h3 class="title topictitle3" style="text-align: left;margin-left: 0.0px;">Maturities of System Models</h3><p><ac:image><ri:attachment ri:filename="techPract_ManageProfile_Maturities.png" /></ac:image><br /><br /></p><p>In the<span> </span><span class="ph"><strong><span class="tm-3D">3D</span></strong>EXPERIENCE platform</span>, the maturity states of a physical product help manage its lifecycle by defining distinct stages. Here is an explanation of each state:</p><table class="wrapped" style="margin-left: 0.0px;"><tbody><tr><td>Private</td><td><p>Description: This is the initial state where a physical product is only visible to its creator or a restricted group.</p><p>Purpose: This state allows early development work and iterations without broader visibility. It is useful for preliminary drafts and experimental designs that are not yet ready for a team review.</p></td></tr><tr><td>In Work</td><td><p>Description: This state indicates that the product is under active development and can be accessed and modified by designated team members.</p><p>Purpose: This state facilitates collaboration among team members, enabling collective development, editing and refinement of the product. This state is crucial for iterative development and incorporating feedback.</p></td></tr><tr><td>Frozen</td><td><p>Description: The product is in a state where no further changes can be made except by an authorized personnel.</p><p>Purpose: This state ensures stability before the final review and release. It allows thorough validation, testing and quality assurance without the risk of unapproved changes. This state acts as a checkpoint for critical reviews.</p></td></tr><tr><td>Released</td><td><p>Description: In this state the product is finalized, fully validated and approved for use or production.</p><p>Purpose: This state marks the product as complete and ready for deployment, manufacturing, or customer use. This state signifies that the product has passed all necessary checks and meets all required standards and specifications.</p></td></tr><tr><td>Obsolete</td><td><p>Description: In this state the product is no longer in use and is retired from active development or production.</p><p>Purpose: This state helps manage and archive older versions or products that are replaced by newer models. This state ensures that obsolete products are clearly marked, preventing their use in current projects and maintaining an organized product catalog.</p></td></tr></tbody></table><p>Each of these maturity states serves a specific role in managing the product development process, ensuring that products are developed systematically, reviewed thoroughly and transitioned smoothly from concept to completion and eventual retirement. The structured approach of the<span> </span><span class="ph"><strong><span class="tm-3D">3D</span></strong>EXPERIENCE platform</span><span> </span>for maturity states helps maintain high standards of quality, compliance and efficiency throughout the product lifecycle.</p><h2 class="title topictitle2" style="text-align: left;">Use Cases</h2><h3 class="title topictitle3" style="text-align: left;margin-left: 0.0px;">Use Case: Manage Profiles on the 3DEXPERIENCE Platform</h3><h4 class="title topictitle4" style="text-align: left;margin-left: 0.0px;">Scenario</h4><p>A Profile Administrator adds profiles to the<span> </span><span class="ph"><strong><span class="tm-3D">3D</span></strong>EXPERIENCE platform</span><span> </span>for team members to access the profile for opening a systems model.</p><h4 class="title topictitle4" style="text-align: left;margin-left: 0.0px;">Actors/personas</h4><p>Jack Profile Administrator: Jack is responsible for managing the CATIA Magic Profiles on the<span> </span><span class="ph"><strong><span class="tm-3D">3D</span></strong>EXPERIENCE platform</span>.</p><h3 class="title topictitle3" style="text-align: left;margin-left: 0.0px;">Workflow</h3><p><ac:image ac:height="400"><ri:attachment ri:filename="techPract_ManageProfile_Workflow.png" /></ac:image><br /><br /><br /></p><h2 class="title topictitle2" style="text-align: left;">How</h2><h3 class="title topictitle3" style="text-align: left;margin-left: 0.0px;">Prerequisite Roles</h3><p>3DSwymer (IFW-OC), Collaborative Industry Innovator (CSV-OC), Collaborative Designer for CATIA Magic (SSY-OC), Magic Systems of Systems Architect (MYH)</p><h3 class="title topictitle3" style="text-align: left;margin-left: 0.0px;">Step 1: Upload CATIA Magic Profiles on 3DEXPERIENCE Platform</h3><p><ac:structured-macro ac:name="widget" ac:schema-version="1" ac:macro-id="8d985949-f858-4863-bd79-7f9838f0494b"><ac:parameter ac:name="width">600</ac:parameter><ac:parameter ac:name="url"><ri:url ri:value="https://www.youtube.com/watch?v=6eMjLbUR7Tc&amp;list=PLlvXsDYdI5UMPvWYNEF0F4Rq0w18dsMJz&amp;index=10" /></ac:parameter><ac:parameter ac:name="height">400</ac:parameter></ac:structured-macro></p><h3 class="title topictitle3" style="text-align: left;margin-left: 0.0px;">Step 2: Change the Maturity of CATIA Magic Profiles</h3><p><ac:structured-macro ac:name="widget" ac:schema-version="1" ac:macro-id="2b878a44-7aaf-4e1c-82aa-eaa593cea6b1"><ac:parameter ac:name="width">600</ac:parameter><ac:parameter ac:name="url"><ri:url ri:value="https://www.youtube.com/watch?v=HUs_Bxp4uAs&amp;list=PLlvXsDYdI5UMPvWYNEF0F4Rq0w18dsMJz&amp;index=7" /></ac:parameter><ac:parameter ac:name="height">400</ac:parameter></ac:structured-macro></p><h3 class="title topictitle3" style="text-align: left;margin-left: 0.0px;">Step 3: Update Profiles on 3DEXPERIENCE Platform</h3><p><ac:structured-macro ac:name="widget" ac:schema-version="1" ac:macro-id="f42c14f5-0d9d-4093-86c4-6a41458623b9"><ac:parameter ac:name="width">600</ac:parameter><ac:parameter ac:name="url"><ri:url ri:value="https://www.youtube.com/watch?v=NPyhmEB2x-M&amp;list=PLlvXsDYdI5UMPvWYNEF0F4Rq0w18dsMJz&amp;index=14" /></ac:parameter><ac:parameter ac:name="height">400</ac:parameter></ac:structured-macro></p><h2 class="title topictitle2" style="text-align: left;">Recommandation</h2><ul class="ul"><li class="li" data-uuid="88281015-220b-428e-ab69-c4b838d6e335">Ensure, you are on the right<span> </span><span class="ph"><strong><span class="tm-3D">3D</span></strong>EXPERIENCE platform</span><span> </span>server and Collaborative Spaces.<ul class="ul"><li class="li">Navigate to the<span> </span><span class="ph"><strong><span class="tm-3D">3D</span></strong>EXPERIENCE</span><span> </span>menu in the CATIA Magic application.</li><li class="li">Select the<span> </span><strong><span class="ph uicontrol" style="color:var(--ds-text,#333333);">Switch Platform/Credentials</span></strong><span> </span>option.</li><li class="li">Select the desired platform and credentials.<br /><ac:image ac:width="1111"><ri:attachment ri:filename="techPract_ManageProfile_Reco.gif" /></ac:image><br /> </li></ul></li><li class="li" data-uuid="a36fc17b-d9ed-4391-8c2e-c592df3fcb2d">Ensure standard profiles are stored in a protected collaborative space, as this allows visibility to all CATIA Magic users while ensuring a good security level. However, it is also possible to use a public collaborative space.</li><li class="li" data-uuid="8fa5df69-0e07-4625-a00e-5059b833d9de">While migrating profiles and projects, it is recommended to have the profiles in the Released state.</li></ul>
````

<!--NOMAGIC_PAGE id=291832024 space=CM version=1 -->
## PAGE 00271: Manage Project Usage

- page_id: `291832024`
- space_key: `CM`
- source_url: https://docs.nomagic.com/spaces/CM/pages/291832024/Manage+Project+Usage
- version_number: 1
- version_date: `2026-02-18T13:28:15.840+01:00`
- ancestors: Client-Side Collaborative Modeling Documentation > Collaboration powered by 3DEXPERIENCE platform > Technical practices
- labels: []

### NORMALIZED CONTENT

#### Why

A CATIA Magic project consists of many elements that can be used multiple times across different projects. Creating a standard library for reusable elements can help reduce manual work of creating same elements for different projects.

#### What

This technical practice highlights the use of Project Usages with the**3D**EXPERIENCE platform. It will help users create a new library by using the Project Usages option to split the CATIA MAGIC project. The library can then be used in multiple CATIA Magic projects. This technical practice also highlights the management of the library.

#### Targer Audience

Systems Engineer, Systems Architect

#### Knowledge

##### Manage Project Usages

Large CATIA Magic projects are built from smaller parts, diagrams or elements. Users can move a part of the model to a separate project. The split projects can then be referred as a**Project Usage**or**Used Project**.

#### Use Cases

##### Use Case: Reusing Elements of CATIA Magic Project in Other Projects

**Scenario:**

A systems engineer wants to reuse elements from a CATIA Magic project to other CATIA Magic projects. He adds the project in the Project Usages to create a library and reduce the manual work of creating the same elements repetitively.

**Actors/Personas:**

**Mark Systems Engineer**: Mark is responsible for creating a library of elements that are required to be added in other CATIA Magic projects.

**John Systems Engineer**: John is responsible for updating the CATIA Magic project using the CATIA Magic library.

**Workflow:**

**[IMAGE alt='' src='']**

#### How

##### Prerequisite Roles

3DSwymer (IFW-OC), Collaborative Industry Innovator (CSV-OC), Collaborative Designer for CATIA Magic (SSY-OC)

##### Step 1: Create CATIA Magic Library

600400

##### Step 2: Use Library in CATIA Magic Project

600400

##### Step 3: Update CATIA Magic Library

600400

##### Step 4: Update Revision of CATIA Magic Library

600400

#### Recommendation

Ensure that the used projects are in the right Collaborative Spaces for them to be accessible to all the users.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<h2>Why</h2><p>A CATIA Magic project consists of many elements that can be used multiple times across different projects. Creating a standard library for reusable elements can help reduce manual work of creating same elements for different projects.</p><h2>What</h2><p>This technical practice highlights the use of Project Usages with the<span> </span><strong>3D</strong>EXPERIENCE platform. It will help users create a new library by using the Project Usages option to split the CATIA MAGIC project. The library can then be used in multiple CATIA Magic projects. This technical practice also highlights the management of the library.</p><h2>Targer Audience</h2><p>Systems Engineer, Systems Architect</p><h2>Knowledge</h2><h3>Manage Project Usages</h3><p>Large CATIA Magic projects are built from smaller parts, diagrams or elements. Users can move a part of the model to a separate project. The split projects can then be referred as a<span> </span><strong>Project Usage</strong><span> </span>or<span> </span><strong>Used Project</strong>.</p><h2>Use Cases</h2><h3>Use Case: Reusing Elements of CATIA Magic Project in Other Projects</h3><p><strong>Scenario: </strong></p><p>A systems engineer wants to reuse elements from a CATIA Magic project to other CATIA Magic projects. He adds the project in the Project Usages to create a library and reduce the manual work of creating the same elements repetitively.<br /></p><p><strong>Actors/Personas:</strong></p><p><strong>Mark Systems Engineer</strong>: Mark is responsible for creating a library of elements that are required to be added in other CATIA Magic projects.</p><p><strong>John Systems Engineer</strong>: John is responsible for updating the CATIA Magic project using the CATIA Magic library.<br /></p><p><strong>Workflow:</strong></p><p><strong><ac:image ac:height="400"><ri:attachment ri:filename="Workflow 3_19_2025.png" /></ac:image></strong></p><h2>How</h2><h3>Prerequisite Roles</h3><p>3DSwymer (IFW-OC), Collaborative Industry Innovator (CSV-OC), Collaborative Designer for CATIA Magic (SSY-OC)</p><h3>Step 1: Create CATIA Magic Library</h3><p><ac:structured-macro ac:name="widget" ac:schema-version="1" ac:macro-id="a084c3f3-fcdf-45b3-b80e-a338b22bc402"><ac:parameter ac:name="width">600</ac:parameter><ac:parameter ac:name="url"><ri:url ri:value="https://www.youtube.com/watch?v=7YxVhIEl94Y&amp;list=PLlvXsDYdI5UMPvWYNEF0F4Rq0w18dsMJz" /></ac:parameter><ac:parameter ac:name="height">400</ac:parameter></ac:structured-macro></p><h3>Step 2: Use Library in CATIA Magic Project</h3><p><ac:structured-macro ac:name="widget" ac:schema-version="1" ac:macro-id="b4c2bca3-0f23-431c-8d92-4329588e44cf"><ac:parameter ac:name="width">600</ac:parameter><ac:parameter ac:name="url"><ri:url ri:value="https://www.youtube.com/watch?v=Qb2EnkAfYQw&amp;list=PLlvXsDYdI5UMPvWYNEF0F4Rq0w18dsMJz" /></ac:parameter><ac:parameter ac:name="height">400</ac:parameter></ac:structured-macro></p><h3>Step 3: Update CATIA Magic Library</h3><p><ac:structured-macro ac:name="widget" ac:schema-version="1" ac:macro-id="e026d87b-8b9b-435f-887b-de87e12c1c54"><ac:parameter ac:name="width">600</ac:parameter><ac:parameter ac:name="url"><ri:url ri:value="https://www.youtube.com/watch?v=paZfJ-Dca2w&amp;list=PLlvXsDYdI5UMPvWYNEF0F4Rq0w18dsMJz" /></ac:parameter><ac:parameter ac:name="height">400</ac:parameter></ac:structured-macro></p><h3>Step 4: Update Revision of CATIA Magic Library</h3><p><ac:structured-macro ac:name="widget" ac:schema-version="1" ac:macro-id="a93d2e38-c466-4fa2-8406-56f8749d807b"><ac:parameter ac:name="width">600</ac:parameter><ac:parameter ac:name="url"><ri:url ri:value="https://www.youtube.com/watch?v=bqVvgnzaAj4&amp;list=PLlvXsDYdI5UMPvWYNEF0F4Rq0w18dsMJz" /></ac:parameter><ac:parameter ac:name="height">400</ac:parameter></ac:structured-macro></p><h2>Recommendation</h2><p>Ensure that the used projects are in the right Collaborative Spaces for them to be accessible to all the users.</p>
````

<!--NOMAGIC_PAGE id=243969977 space=CM version=4 -->
## PAGE 00272: Managing project usages

- page_id: `243969977`
- space_key: `CM`
- source_url: https://docs.nomagic.com/spaces/CM/pages/243969977/Managing+project+usages
- version_number: 4
- version_date: `2026-07-01T14:59:46.606+02:00`
- ancestors: Client-Side Collaborative Modeling Documentation > Using Teamwork Cloud
- labels: []

### NORMALIZED CONTENT

To manage project usages, you must have the [**Administer Resources** permission](https://docs.nomagic.com/MCS/?contextKey=permissions&version=latest&variant=default).

Large Teamwork Cloud projects are built from smaller parts.

We recommend project partitioning when the model has weakly dependent parts, such as type libraries, models of different phases of software/system development, etc. A part of the model that has been moved to a separate project can be used in many projects. From the perspective of the project using elements from another project, we refer to the other project as a****project usage** or **used project**.

You can easily detach a selected part of the model by [CONFLUENCE_PAGE title='Exporting a package to a new server project' space=''] it to a separate Teamwork Cloud project and [CONFLUENCE_PAGE title='Using server projects' space=''] it in other server projects. Since projects are used as *read-only*, you cannot modify their contents directly from the main project. To [CONFLUENCE_PAGE title='Editing the content of a used project' space='']a used project, you should open it as a standalone project. You can also [CONFLUENCE_PAGE title='Changing used project versions' space=''] to a different used project version if needed.

If you no longer need a part of the model as a separate project, you can [CONFLUENCE_PAGE title='Importing the content of a used project into your project' space='']the project into the main project. Additionally, you can [CONFLUENCE_PAGE title='Stop using the project in your project' space='']using the project.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="660e2072-9c67-4bfd-a314-4d8ce037351b"><ac:rich-text-body><p>To manage project usages, you must have the <a href="https://docs.nomagic.com/MCS/?contextKey=permissions&amp;version=latest&amp;variant=default"><strong>Administer Resources</strong> permission</a>.</p></ac:rich-text-body></ac:structured-macro><p>Large Teamwork Cloud projects are built from smaller parts.</p><p>We recommend project partitioning when the model has weakly dependent parts, such as type libraries, models of different phases of software/system development, etc. A part of the model that has been moved to a separate project can be used in many projects. From the perspective of the project using elements from another project, we refer to the other project as a<em> </em><strong>project usage</strong> or <strong>used project</strong>.</p><p>You can easily detach a selected part of the model by <ac:link><ri:page ri:content-title="Exporting a package to a new server project" /><ac:plain-text-link-body><![CDATA[exporting]]></ac:plain-text-link-body></ac:link> it to a separate Teamwork Cloud project and <ac:link><ri:page ri:content-title="Using server projects" /><ac:plain-text-link-body><![CDATA[reusing]]></ac:plain-text-link-body></ac:link> it in other server projects. Since projects are used as <em>read-only</em>, you cannot modify their contents directly from the main project. To <ac:link><ri:page ri:content-title="Editing the content of a used project" /><ac:plain-text-link-body><![CDATA[modify ]]></ac:plain-text-link-body></ac:link>a used project, you should open it as a standalone project. You can also <ac:link><ri:page ri:content-title="Changing used project versions" /><ac:plain-text-link-body><![CDATA[switch]]></ac:plain-text-link-body></ac:link> to a different used project version if needed.</p><p>If you no longer need a part of the model as a separate project, you can <ac:link><ri:page ri:content-title="Importing the content of a used project into your project" /><ac:plain-text-link-body><![CDATA[import ]]></ac:plain-text-link-body></ac:link>the project into the main project. Additionally, you can <ac:link><ri:page ri:content-title="Stop using the project in your project" /><ac:plain-text-link-body><![CDATA[stop ]]></ac:plain-text-link-body></ac:link>using the project.</p>
````

<!--NOMAGIC_PAGE id=243970229 space=CM version=1 -->
## PAGE 00273: Managing project usages in 3DEXPERIENCE platform

- page_id: `243970229`
- space_key: `CM`
- source_url: https://docs.nomagic.com/spaces/CM/pages/243970229/Managing+project+usages+in+3DEXPERIENCE+platform
- version_number: 1
- version_date: `2025-07-31T10:51:46.795+02:00`
- ancestors: Client-Side Collaborative Modeling Documentation > Collaboration powered by 3DEXPERIENCE platform
- labels: []

### NORMALIZED CONTENT

Large projects are built from smaller parts. From the perspective of the project using elements from another project, we refer to the other project as a*usage* or *used project*. To learn how to use projects and manage them, see the following topics:

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>Large projects are built from smaller parts. From the perspective of the project using elements from another project, we refer to the other project as a<em> usage</em> or <em>used project</em>. To learn how to use projects and manage them, see the following topics:</p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="ac87287b-9310-4f69-838e-f7da71e93f84" /></p>
````

<!--NOMAGIC_PAGE id=243969709 space=CM version=2 -->
## PAGE 00274: Managing server projects

- page_id: `243969709`
- space_key: `CM`
- source_url: https://docs.nomagic.com/spaces/CM/pages/243969709/Managing+server+projects
- version_number: 2
- version_date: `2025-09-12T12:50:39.340+02:00`
- ancestors: Client-Side Collaborative Modeling Documentation > Using Teamwork Cloud
- labels: []

### NORMALIZED CONTENT

You can manage your server projects, as well as locally saved server projects (known as [CONFLUENCE_PAGE title='Offline modeling' space='']), in the **Manage Projects** dialog.

Currently open project is automatically selected in the**Manage Projects**dialog, making it easier to findit in the project list.

To open the **Manage Projects**dialog

1. [CONFLUENCE_PAGE title='Starting a collaboration session' space='']
2. On the main menu, click Collaborate > Projects .

[IMAGE alt='' src='']

You can use the search tab to quickly filter used projects by name.

In the **Manage Projects** dialog, you can:

- For server projects:
  - [CONFLUENCE_PAGE title='Adding projects to Teamwork Cloud' space='']
  - [CONFLUENCE_PAGE title='Opening Teamwork Cloud projects' space='']
  - Rename a server project
  - Remove a server project
  - [CONFLUENCE_PAGE title='Cloning projects' space='']
  - [CONFLUENCE_PAGE title='Reviewing historical versions of the project' space='']
  - [CONFLUENCE_PAGE title='Creating and managing categories' space='']
  - [CONFLUENCE_PAGE title='Branching projects' space='']
  - [CONFLUENCE_PAGE title='Password-protected projects' space='']
  - [CONFLUENCE_PAGE title='Viewing Version Properties' space='']
- For offline server projects:
  - [CONFLUENCE_PAGE title='Offline modeling' space='']
  - [CONFLUENCE_PAGE title='Offline modeling' space='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>You can manage your server projects, as well as locally saved server projects (known as <ac:link><ri:page ri:content-title="Offline modeling" /><ac:plain-text-link-body><![CDATA[offline server projects]]></ac:plain-text-link-body></ac:link>), in the <strong>Manage Projects</strong> dialog.</p><p><span style="color: rgb(23,43,77);"><span style="color: rgb(23,43,77);">Currently open project is automatically selected in the </span><strong>Manage Projects </strong><span style="color: rgb(23,43,77);">dialog, making it easier to <ac:inline-comment-marker ac:ref="eeedddf5-dcf6-4b1b-983d-29dd503609b9">find </ac:inline-comment-marker>it in the project list.</span></span></p><p><br /></p><p>To open the <strong>Manage Projects </strong>dialog</p><hr /><ol><li><ac:link><ri:page ri:content-title="Starting a collaboration session" /><ac:plain-text-link-body><![CDATA[Log on to the Teamwork Cloud server.]]></ac:plain-text-link-body></ac:link></li><li>On the main menu, click <strong>Collaborate</strong> &gt; <strong>Projects</strong>.</li></ol><p style="margin-left: 30.0px;"><ac:image><ri:attachment ri:filename="manage_projects_dialog.png" /></ac:image></p><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="e2474492-efba-4e80-a068-d3843bc29301"><ac:rich-text-body><p><span style="color: rgb(0,0,0);"><span style="color: rgb(0,0,0);"><span style="color: rgb(0,0,0);">You can use the search tab to quickly filter used projects by name.</span><br /></span></span></p></ac:rich-text-body></ac:structured-macro><p>In the <strong>Manage Projects</strong> dialog, you can:</p><ul><li>For server projects:<ul><li><ac:link><ri:page ri:content-title="Adding projects to Teamwork Cloud" /><ac:plain-text-link-body><![CDATA[Add a new server project]]></ac:plain-text-link-body></ac:link></li><li><ac:link><ri:page ri:content-title="Opening Teamwork Cloud projects" /><ac:plain-text-link-body><![CDATA[Open a server project]]></ac:plain-text-link-body></ac:link></li><li><a href="https://docs.nomagic.com/display/MT/Renaming+projects">Rename a server project</a></li><li><a href="https://docs.nomagic.com/display/MT/Removing+projects">Remove a server project</a></li><li><ac:link><ri:page ri:content-title="Cloning projects" /><ac:plain-text-link-body><![CDATA[Clone a server project]]></ac:plain-text-link-body></ac:link></li><li><ac:link><ri:page ri:content-title="Reviewing historical versions of the project" /><ac:plain-text-link-body><![CDATA[Review and change project versions]]></ac:plain-text-link-body></ac:link></li><li><ac:link><ri:page ri:content-title="Creating and managing categories" /><ac:plain-text-link-body><![CDATA[Manage server project categories]]></ac:plain-text-link-body></ac:link></li><li><ac:link><ri:page ri:content-title="Branching projects" /><ac:plain-text-link-body><![CDATA[Manage server project branches]]></ac:plain-text-link-body></ac:link></li><li><ac:link><ri:page ri:content-title="Password-protected projects" /><ac:plain-text-link-body><![CDATA[Set a password for a server project]]></ac:plain-text-link-body></ac:link></li><li><ac:link><ri:page ri:content-title="Viewing Version Properties" /><ac:plain-text-link-body><![CDATA[View Version Properties]]></ac:plain-text-link-body></ac:link></li></ul></li><li>For offline server projects:<ul><li><ac:link><ri:page ri:content-title="Offline modeling" /><ac:plain-text-link-body><![CDATA[Open a server project]]></ac:plain-text-link-body></ac:link></li><li><ac:link ac:anchor="Remove offline project"><ri:page ri:content-title="Offline modeling" /><ac:plain-text-link-body><![CDATA[Remove a server project]]></ac:plain-text-link-body></ac:link></li></ul></li></ul>
````

<!--NOMAGIC_PAGE id=243970065 space=CM version=2 -->
## PAGE 00275: Managing Teamwork Cloud users

- page_id: `243970065`
- space_key: `CM`
- source_url: https://docs.nomagic.com/spaces/CM/pages/243970065/Managing+Teamwork+Cloud+users
- version_number: 2
- version_date: `2025-09-12T12:45:41.734+02:00`
- ancestors: Client-Side Collaborative Modeling Documentation > Using Teamwork Cloud
- labels: []

### NORMALIZED CONTENT

Managing Teamwork Cloud users includes:

- Creating and modifying user accounts
- Creating roles and assigning them to the users
- Assigning the users to projects

These tasks can be performed only in the [CONFLUENCE_PAGE title='Users application' space='MCS'] and [CONFLUENCE_PAGE title='Resources application' space='MCS'] of Teamwork Cloud Admin.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>Managing Teamwork Cloud users includes:</p><ul><li>Creating and modifying user accounts</li><li>Creating roles and assigning them to the users</li><li>Assigning the users to projects</li></ul><p><br /></p><p>These tasks can be performed only in the <ac:link><ri:page ri:space-key="MCS" ri:content-title="Users application" /></ac:link> and <ac:link><ri:page ri:space-key="MCS" ri:content-title="Resources application" /><ac:plain-text-link-body><![CDATA[Roles Application]]></ac:plain-text-link-body></ac:link> of Teamwork Cloud Admin.</p>
````

<!--NOMAGIC_PAGE id=243970121 space=CM version=2 -->
## PAGE 00276: Manually configuring properties file

- page_id: `243970121`
- space_key: `CM`
- source_url: https://docs.nomagic.com/spaces/CM/pages/243970121/Manually+configuring+properties+file
- version_number: 2
- version_date: `2025-09-12T12:45:42.366+02:00`
- ancestors: Client-Side Collaborative Modeling Documentation > Using Teamwork Cloud > Used Projects Auto Updater Plugin
- labels: []

### NORMALIZED CONTENT

This section explains how to correctly configure a Used Projects Auto Update Plugin properties file.

To configure the properties file for updating used projects

- In the <modeling tool installation directory>/plugins/com.nomagic.magicdraw.twcusageupdater directory, open the sample.properties file (or any generated properties file) through a wizard.
- Specify the properties values listed below in the table (or leave the default values if they do not need to be changed).

| Properties | Description |
| --- | --- |
| twc.server | TWCloud server hostname or IP (with port if it is not default) |
| twc.user.name | TWCloud username |
| twc.user.password | TWCloud user hashed password (the only way to get a hashed password is to generate it through first) |
| twc.project | TWCloud main project URI* |
| twc.project.password | Project hashed password if there is password protection (the only way to get a hashed password is to generate it through first) |
| twc.used.projects | List of used projects URI (with hashed passwords if project is password protected. Pattern <URI>,<URI>#<password>,<URI>.The only way to get a hashed password is to generate it through first) |
| twc.use.ssl | Use SSL flag |
| twc.personal.access.token | The personal access token generated using the My account application in the Teamwork Cloud web UI. To learn more, see . |

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>This section explains how to correctly configure a Used Projects Auto Update Plugin <ac:inline-comment-marker ac:ref="673df12e-e0fe-4a61-9a15-de980f2193be">properties</ac:inline-comment-marker> file. </p><p><br /></p><p>To configure the properties file for updating used projects</p><hr /><ul><li>In the <em>&lt;modeling tool installation directory&gt;/plugins/com.nomagic.magicdraw.twcusageupdater</em> directory, open the <em><ac:inline-comment-marker ac:ref="f14e4879-635b-4b52-8a9f-0082b669b5c5">sample.properties</ac:inline-comment-marker></em><ac:inline-comment-marker ac:ref="f14e4879-635b-4b52-8a9f-0082b669b5c5"> file (or any generated properties file) through a wizard.</ac:inline-comment-marker></li><li>Specify the properties values listed below in the table (or leave the default values if they do not need to be changed). </li></ul><table class="wrapped"><colgroup><col /><col /></colgroup><tbody><tr><th>Properties</th><th>Description</th></tr><tr><td><em>twc.server</em></td><td>TWCloud server hostname or IP (with port if it is not default)</td></tr><tr><td><em>twc.user.name</em></td><td>TWCloud username</td></tr><tr><td><em>twc.user.password</em></td><td>TWCloud user hashed <ac:inline-comment-marker ac:ref="a90fb439-006e-4312-8476-7c2fef0f8f1b">password (t<span style="color: rgb(62,63,64);">he only way to get a hashed password is to generate it through <ac:link><ri:page ri:content-title="Using Used Projects Auto Update Wizard" /><ac:plain-text-link-body><![CDATA[Used Projects Auto Update Wizard]]></ac:plain-text-link-body></ac:link> first)</span></ac:inline-comment-marker></td></tr><tr><td><em>twc.project</em></td><td>TWCloud main project URI*</td></tr><tr><td><em>twc.project.password</em></td><td><span>Project <span>hashed </span>password if there is password protection <span>(t</span><span style="color: rgb(62,63,64);">he only way to get a hashed password is to generate it through <ac:link><ri:page ri:content-title="Using Used Projects Auto Update Wizard" /><ac:plain-text-link-body><![CDATA[Used Projects Auto Update Wizard]]></ac:plain-text-link-body></ac:link> first)</span></span></td></tr><tr><td><em>twc.used.projects</em></td><td><p>List of used projects URI (with <ac:inline-comment-marker ac:ref="64ea3a97-200d-48a9-ab8d-3be608cd4a12">hashed </ac:inline-comment-marker><ac:inline-comment-marker ac:ref="36343f8c-1181-464d-a027-2f31515f7f0f"><ac:inline-comment-marker ac:ref="64ea3a97-200d-48a9-ab8d-3be608cd4a12">password</ac:inline-comment-marker>s</ac:inline-comment-marker> if project is password protected. Pattern &lt;URI&gt;,&lt;URI&gt;#&lt;password&gt;,&lt;URI&gt;.</p><p>T<span style="color: rgb(62,63,64);">he only way to get a hashed password is to generate it through <ac:link><ri:page ri:content-title="Using Used Projects Auto Update Wizard" /><ac:plain-text-link-body><![CDATA[Used Projects Auto Update Wizard]]></ac:plain-text-link-body></ac:link> first)</span></p></td></tr><tr><td><em>twc.use.ssl</em></td><td>Use SSL flag</td></tr><tr><td><em>twc.personal.access.token</em></td><td>The personal access token generated using the My account application in the Teamwork Cloud web UI. To learn more, see <ac:link><ri:page ri:space-key="MCS" ri:content-title="Generating a personal access token" /></ac:link>.</td></tr></tbody></table><p class="auto-cursor-target"><br /></p>
````

<!--NOMAGIC_PAGE id=243969919 space=CM version=4 -->
## PAGE 00277: Migrating projects

- page_id: `243969919`
- space_key: `CM`
- source_url: https://docs.nomagic.com/spaces/CM/pages/243969919/Migrating+projects
- version_number: 4
- version_date: `2025-09-12T12:51:44.641+02:00`
- ancestors: Client-Side Collaborative Modeling Documentation > Using Teamwork Cloud
- labels: []

### NORMALIZED CONTENT

Once you have successfully[CONFLUENCE_PAGE title='Upgrade and data migration' space='MCS']to a new version of Teamwork Cloud, you should also migrate the projects if you want to be able to edit them with a new version of a modeling tool. Migrating projects updates their standard/system profiles. Projects that are not migrated can only be opened in the read-only mode.

- To migrate a project, you need to have the Administer Resources, Edit Resources, Edit Resource Properties, and Read Resources permissions for that project.
- While a project is being migrated, other users are prevented from modifying it. Therefore, we highly recommend that the same person migrates all projects.

##### Migrating server projects automatically

Automatic project migration allows you to migrate a large number of projects at the same time and is the recommended approach after upgrading the Teamwork Cloud server.

To migrate server projects automatically

1. Start the modeling tool and [CONFLUENCE_PAGE title='Starting a collaboration session' space=''] .
2. In the main menu, go to Collaborate > Migrate Projects to Version X .
3. In the Migrate Projects to Version X dialog, select the projects you want to migrate. In the dialog toolbar, click [IMAGE alt='' src='']to select all server projects.Select a category (or categories) to migrate all projects inside it. [ATTACHMENT filename='migrating_projects.png']
4. Optionally, select one or several of the following check boxes:
  - Speed up model-history related operations - Migrates the cache of the earlier project versions to speed up model history-related operations after migration. However, selecting this check box may slow down the migration.
  - Enable migration of password-protected projects - Allows you to select password-protected projects. You will be prompted to enter the password for each password-protected project in the selected scope. If you do not select this check box, password-protected projects will be excluded from the migration scope.
  - Skip archived branches - Excludes archived project branches from the migration scope. Selecting this check box may speed up the migration.
5. Click OK .

Note that it may take a while to migrate a large number of projects. Once you receive a message saying that Teamwork Cloud projects were migrated successfully, the migration is complete. If you get the list of projects that were not migrated, it means that migration was only partially successful and you have to migrate these projects manually.

#### WARNING: Migrating UAF and UPDM projects

Migrating UAF and UPDM projects

- UPDM projects cannot be migrated from the modeling tool with the UAF environment. If you want to migrate UPDM projects to UAF, open the <install_root>\bin\<modeling_tool>.properties file and change the value of the -Dmigrate.project.from.updm2.to.uaf\=false property to true . By default, the value of this property is false , which means, that UPDM projects will not be migrated.
- For more information about UAF project migration issues, see [CONFLUENCE_PAGE title='Project migration issues on Teamwork Cloud' space='MT'] .

##### Migrating server projects manually

If you do not want to migrate multiple projects with their branches at once, you can migrate these projects manually. You can also use this approach ifautomatic project migration was only partially successful and some projects were not migrated.

To migrate server projects manually

1. Start the modeling tool and [CONFLUENCE_PAGE title='Starting a collaboration session' space=''] .
2. [CONFLUENCE_PAGE title='Opening Teamwork Cloud projects' space=''] that was not migrated.
3. When the Incompatible Standard/System Profiles dialog opens, click Continue to update the profiles and commit the changes to the server. [ATTACHMENT filename='incompatible_system_profiles.png']

When you get the message that the profiles were successfully updated, you can continue working with the project as usual.

##### Migrating used projects

This section explains if you need to migrate used projects depending on your situation.

To begin with, it is important to understand how project usages work. Every time you use a project, a copy of that project is embedded into the main project. When you migrate the main project, the embedded copies of used projects start using the same updated standard/system profiles that the main project uses. The same thing happens if you use a non-migrated project (committed with an earlier version of a modeling tool) in a migrated project. In other words, project usages (embedded copies) become migrated in the context of the main project, even if the used projects themselves are not migrated. This behavior helps to avoid version conflicts inside the main project and enables you to keep working with the historical versions of used projects without migrating them.

To sum up, even if used projects are not migrated, you can still do the following:

- Work with the main project as usual.
- Change the versions of used projects in the main project.
- Continue to modify used projects using an earlier version of a modeling tool (as long as it is compatible with the version of the upgraded server).

However, if you do not migrate used projects, you will not be able to modify them with a new version of a modeling tool. They can only be opened in the read-only mode.

###### Frequently asked questions

**Q: Do I need to migrate all of the used projects?**

**A:** No, in most cases you do not need to migrate your used projects. You will be able to work with the main project as usual and even change the versions of the usages if needed.

**Q: Do I need to change used projects to their latest versions after migration?**

**A:**No, you do not need to change the versions of used projects after migration. Even if you migrate a used project and a new version of that project becomes available on the server, the project content stays the same.

**Q: What happens during migration if the main project uses a historical used project version?**

**A:** When you migrate the main project, used projects are migrated automatically but only in the context of the main project. (The embedded copies of the used projects start using the same updated standard/system profiles as the main project.)

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><span style="letter-spacing: 0.0px;">Once you have successfully </span><ac:link><ri:page ri:space-key="MCS" ri:content-title="Upgrade and data migration" /><ac:plain-text-link-body><![CDATA[migrated your data]]></ac:plain-text-link-body></ac:link><span style="letter-spacing: 0.0px;"> to a new version of Teamwork Cloud, you <ac:inline-comment-marker ac:ref="f5f77abc-896c-4fc3-9421-de543e379a9d">should</ac:inline-comment-marker> also migrate the projects if you want to be able to edit them with a new version of a modeling tool. Migrating projects updates their standard/system profiles. Projects that are not migrated can only be opened in the read-only mode.</span></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="cfbe2848-ae23-42b3-b69e-6e916ec569ce"><ac:rich-text-body><ul><li>To migrate a project, you need to have the <a href="https://docs.nomagic.com/MCS/?contextKey=permissions&amp;version=latest&amp;variant=default">Administer Resources, Edit Resources, Edit Resource Properties, and Read Resources permissions</a> for that project.</li><li>While a project is being migrated, other users are prevented from modifying it. Therefore, we highly recommend that the same person migrates all projects.</li></ul></ac:rich-text-body></ac:structured-macro><h3>Migrating server projects automatically</h3><p>Automatic project migration allows you to migrate a large number of projects at the same time and is the recommended approach after upgrading the Teamwork Cloud server.</p><p><br /></p><p>To migrate server projects automatically</p><hr /><ol><li>Start the modeling tool and <ac:link><ri:page ri:content-title="Starting a collaboration session" /><ac:plain-text-link-body><![CDATA[log in to Teamwork Cloud]]></ac:plain-text-link-body></ac:link>.</li><li>In the main menu, go to <strong>Collaborate</strong> &gt; <strong>Migrate Projects to Version X</strong>.</li><li>In the <strong>Migrate Projects to Version X</strong> dialog, select the projects you want to migrate.<br /><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="0453d608-7b36-4dc7-be05-8e298ec24419"><ac:rich-text-body><ul><li><p><span>In the dialog toolbar, click <ac:image><ri:attachment ri:filename="select_all.png" /></ac:image></span><span> to select all server projects.</span></p></li><li><p><span>Select a category (or categories) to migrate all projects inside it.</span></p></li></ul></ac:rich-text-body></ac:structured-macro><br /><ac:image><ri:attachment ri:filename="migrating_projects.png" /></ac:image><br /><br /></li><li><p>Optionally, select one or several of the following check boxes:</p><ul><li><strong>Speed up model-history related operations</strong> - Migrates the cache of the earlier project versions to speed up model history-related operations after migration. However, selecting this check box may slow down the migration.</li><li><strong>Enable migration of password-protected projects</strong> - Allows you to select password-protected projects. You will be prompted to enter the password for each password-protected project in the selected scope. If you do not select this check box, password-protected projects will be excluded from the migration scope.</li><li><strong>Skip archived branches</strong> - Excludes archived project branches from the migration scope. Selecting this check box may speed up the migration.</li></ul></li><li>Click <strong>OK</strong>.</li></ol><p><br />Note that it may take a while to migrate a large number of projects. Once you receive a message saying that Teamwork Cloud projects were migrated successfully, the migration is complete. If you get the list of projects that were not migrated, it means that migration was only partially successful and you have to migrate these projects manually. </p><ac:structured-macro ac:name="warning" ac:schema-version="1" ac:macro-id="6025377b-5cc4-4105-8d2d-9b8c88ce051b"><ac:parameter ac:name="title">Migrating UAF and UPDM projects</ac:parameter><ac:rich-text-body><ul><li>UPDM projects cannot be migrated from the modeling tool with the UAF environment. If you want to migrate UPDM projects to UAF, open the <em>&lt;install_root&gt;\bin\&lt;modeling_tool&gt;.properties</em> file and change the value of the <strong>-Dmigrate.project.from.updm2.to.uaf\=false</strong> property to <em>true</em>. By default, the value of this property is <em>false</em>, which means, that UPDM projects will not be migrated.</li><li>For more information about UAF project migration issues, see <ac:link><ri:page ri:space-key="MT" ri:content-title="Project migration issues on Teamwork Cloud" /></ac:link>.</li></ul></ac:rich-text-body></ac:structured-macro><h3>Migrating server projects manually</h3><p><ac:inline-comment-marker ac:ref="41886b96-2c0d-446f-b63c-b21c620b15dd">If <span style="color:var(--ds-text,#172b4d);">you do not want to migrate multiple projects with their branches at once, you can migrate these projects manually. You can also use this approach if </span>automatic project migration was only partially successful and some projects were not migrated.</ac:inline-comment-marker></p><p><br /></p><p><span style="color:var(--ds-background-accent-red-bolder,#c9372c);"><span style="color:var(--ds-text,#000000);">To migrate server projects manually</span></span></p><hr /><ol><li>Start the modeling tool and <ac:link><ri:page ri:content-title="Starting a collaboration session" /><ac:plain-text-link-body><![CDATA[log in to Teamwork Cloud]]></ac:plain-text-link-body></ac:link>.</li><li><ac:link><ri:page ri:content-title="Opening Teamwork Cloud projects" /><ac:plain-text-link-body><![CDATA[Open the server project]]></ac:plain-text-link-body></ac:link> that was not migrated.</li><li>When the <strong>Incompatible Standard/System Profiles</strong> dialog opens, click <strong>Continue</strong> to update the profiles and commit the changes to the server.<br /><br /><ac:image><ri:attachment ri:filename="incompatible_system_profiles.png" /></ac:image><br /><br /></li></ol><p><br />When you get the message that the profiles were successfully updated, you can continue working with the project as usual.</p><h3><ac:inline-comment-marker ac:ref="481f6ac7-a851-4344-bf41-8f58bd03ad73">Migrating used projects</ac:inline-comment-marker></h3><p>This section explains if you need to migrate used projects depending on your situation.</p><p>To begin with, it is important to understand how project usages work. Every time you use a project, a copy of that project is embedded into the main project. <ac:inline-comment-marker ac:ref="2c1e05f2-8a92-44d1-a221-80ec9e2a1819">When you migrate the main project, the embedded copies of used projects start using the same updated standard/system profiles that the main project uses.</ac:inline-comment-marker> The same thing happens <ac:inline-comment-marker ac:ref="12aaa8be-848d-4145-8224-8dc23e1ddc9b">if you use</ac:inline-comment-marker> a non-migrated project (committed with an earlier version of a modeling tool) in a migrated project. In other words, project usages (embedded copies) become migrated in the context of the main project, even if the used projects themselves are not migrated. This behavior helps to avoid version <ac:inline-comment-marker ac:ref="b1d9ee2a-8f47-48b9-bf50-ff4cc6d85006">conflicts</ac:inline-comment-marker> inside the main project and enables you to keep working with the historical versions of used projects without migrating them.</p><p><span style="color:var(--ds-text,#000000);">To sum up, even if used projects are not migrated, you can still do the following:</span></p><ul><li><span style="letter-spacing: 0.0px;">Work with the main project as usual.</span></li><li><span style="letter-spacing: 0.0px;">Change the versions of used projects in the main project.</span></li><li><span style="letter-spacing: 0.0px;">Continue to modify used projects using an earlier version of a modeling tool (as long as it is compatible with the version of the upgraded server).</span></li></ul><p><span style="letter-spacing: 0.0px;"><span>However, if you do not migrate used projects, <ac:inline-comment-marker ac:ref="15ac273d-2360-4c7e-8bab-754185413b0f">you will not be able to modify them with a new version of a modeling tool</ac:inline-comment-marker>. They can only be opened in the read-only mode.</span></span></p><h4><br />Frequently asked questions</h4><p><strong>Q: Do I need to migrate all of the used projects?</strong></p><p><strong>A:</strong> No, in most cases you do not need to migrate your used projects. You will be able to work with the main project as usual and even change the versions of the usages if needed.</p><p><strong>Q: Do I need to change used projects to their latest versions after migration?</strong></p><p><strong><ac:inline-comment-marker ac:ref="42ee16c3-db7e-4ad7-bee9-12c4b31c9a88">A:</ac:inline-comment-marker></strong><ac:inline-comment-marker ac:ref="42ee16c3-db7e-4ad7-bee9-12c4b31c9a88"> No, you do not need to change the versions of used projects after migration. Even if you migrate a used project and a new version of that project becomes available on the server, the project content stays the same.</ac:inline-comment-marker></p><p><strong>Q: What happens during migration if the main project uses a historical used project version?</strong></p><p><strong>A:</strong> When you migrate the main project, used projects are migrated automatically but only in the context of the main project. (The embedded copies of the used projects start using the same updated standard/system profiles as the main project.)</p>
````

<!--NOMAGIC_PAGE id=243970194 space=CM version=6 -->
## PAGE 00278: Migrating projects and standard profiles

- page_id: `243970194`
- space_key: `CM`
- source_url: https://docs.nomagic.com/spaces/CM/pages/243970194/Migrating+projects+and+standard+profiles
- version_number: 6
- version_date: `2026-01-26T15:14:55.681+01:00`
- ancestors: Client-Side Collaborative Modeling Documentation > Collaboration powered by 3DEXPERIENCE platform
- labels: []

### NORMALIZED CONTENT

After upgrading your modeling tool, you need to migrate the projects and standard profiles stored in the **3D**EXPERIENCE platform to the new version as well. You can do this in several different methods which are described below.

#### NOTE: Prerequisites

Prerequisites

- To migrate standard profiles, you need to have write permissions in the collaborative space where profiles are stored.
- To migrate a project, you need to have write permissions on its branch/revision and maturity to allow iterations to be created.

- When migrating standard profiles, a revision is created for each profile that is migrated.
- When migrating standard profiles, an intermediate profile version can be committed in certain cases. This is a normal part of the migration process and is not a cause for concern. For example, when migrating from UAF 1.2 to 1.3, you may see an intermediate version such as *1.B (1) (UAF 1.2 -> 1.3)*.
- When migrating projects, an iteration is created for each branch/revision of a migrated project.
- If the 3D EXPERIENCE platform is upgraded, but you still use the same version of a modeling tool, standard profiles do not change, and you do not need to migrate them.
- You can only migrate projects to the version of your modeling tool.
- You can migrate projects partially to allow users to work on both an earlier version and the version you are migrating to. However, if you start working and creating projects on a later version, you cannot migrate or add projects to an earlier version.

##### Migrating all projects and standard profiles at once

You can migrate projects and standard profiles all at once.

To migrate all projects and standard profiles at once

1. In the main menu, select Collaborate > Migrate Projects to Version <version number> .
2. In the **Show** drop-down menu of the open dialog, select **All Projects**. It will display all projects and standard profiles on the server.****
3. Click [ATTACHMENT filename='select_all_button.png'] on the left side of the dialog to select all projects and standard profiles. [ATTACHMENT filename='migrate_all_projects.png']
4. Click OK.

##### Migrating standard profiles

To migrate projects separately from standard profiles, you must first migrate the standard profiles.

To migrate standard profiles

1. [CONFLUENCE_PAGE title='Logging in to 3DEXPERIENCE platform' space='']Log in to the **3D**EXPERIENCE platform .
2. Select the collaborative space dedicated for standard profiles: It is highly recommended to store standard profiles in a public collaborative space. To learn how to create a collaborative space, see [CONFLUENCE_PAGE title='Adding standard profiles to 3DEXPERIENCE platform' space=''].
  1. In the main menu, select 3DEXPERIENCE > Switch Platform/Credentials .
  2. In the Credentials drop-down box of the open dialog, select the collaborative space. [ATTACHMENT filename='switching_to_public_space.png']
  3. Click OK.
3. In the main menu, select Collaborate > Migrate Projects to Version <version number> .
4. In the **Show** drop-down menu of the open dialog, select **Standard Profiles**. It will display all standard profiles on the server.****
5. Select the standard profiles you want to migrate or click [ATTACHMENT filename='select_all_button.png'] on the left side of the dialog to select all standard profiles. [ATTACHMENT filename='migrating_standard_profiles.png']
6. Click OK .

##### Migrating projects

You can migrate projects either automatically through the dedicated dialog or manually by opening a project that has not yet been migrated. Please note that for either of these methods to work you have to beforehand.

###### Migrating projects automatically

If you migrate projects automatically through the dedicated dialog, all branches of the projects are migrated as well.

To migrate projects automatically

1. In the main menu, select Collaborate > Migrate Projects to Version <version number> .
2. In the **Show** drop-down menu of the open dialog, select **Projects**. It will display all projects on the server.****
3. Select the projects you want to migrate or click [ATTACHMENT filename='select_all_button.png'] on the left side of the dialog to select all projects. [ATTACHMENT filename='migrating_projects_automatically.png']
4. Click OK .

###### Migrating projects manually

If you choose to migrate a project that you are opening, only the branch that you are opening will be migrated.

To migrate a project manually

1. On the main menu, click Collaborate > Projects .
2. In the Manage projects dialog, s elect a project and click Open . A dialog opens telling you to update the System/Standard Profiles in the project. 
 
[IMAGE alt='' src='']
3. Click Continue .

After the System/Standard Profiles are updated, you get a notification saying that the model was successfully updated.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>After upgrading your modeling tool, you need to migrate the projects and standard profiles stored in the <strong>3D</strong>EXPERIENCE platform to the new version as well. You can do this in several different methods which are described below.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="ea2e0dc3-66d6-485c-b8c8-31e6b33d7d2e"><ac:parameter ac:name="title">Prerequisites</ac:parameter><ac:rich-text-body><ul><li>To migrate standard profiles, you need to have write permissions in the collaborative space where profiles are stored.</li><li>To migrate a project, <span>you need to have write permissions on its branch/revision and maturity to allow iterations to be created.</span></li></ul></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="1a967a4b-f62e-43a0-8f12-440c57e5d97b"><ac:rich-text-body><ul><li><p>When migrating standard profiles, a revision is created for each profile that is migrated.</p></li><li data-uuid="89a500b7-a21d-4e61-8c27-5b1e452037c2"><span style="color:var(--ds-text,#172b4d);">When migrating standard profiles, an intermediate profile version can be committed in certain cases. This is a normal part of the migration process and is not a cause for concern. For example, when migrating from UAF 1.2 to 1.3, you may see an intermediate version such as <em>1.B (1) (UAF 1.2 -&gt; 1.3)</em>.</span></li><li><p><span style="letter-spacing: 0.0px;">When migrating projects, an iteration is created for each branch/revision of a migrated project.</span></p></li><li>If the <strong>3D</strong>EXPERIENCE platform is upgraded, but you still use the same version of a modeling tool, standard profiles do not change, and you do not need to migrate them.</li><li>You can only migrate projects to the version of your modeling tool.</li><li>You can migrate projects partially to allow users to work on both an earlier version and the version you are migrating to. However, if you start working and creating projects on a later version, you cannot migrate or add projects to an earlier version.</li></ul></ac:rich-text-body></ac:structured-macro><h3>Migrating all projects and standard profiles at once</h3><p>You can migrate projects and standard profiles all at once.</p><p><br /></p><p>To migrate all projects and standard profiles at once</p><hr /><ol><li><span style="letter-spacing: 0.0px;">In the main menu, select </span><strong style="letter-spacing: 0.0px;">Collaborate &gt; Migrate Projects to Version &lt;version number&gt;</strong>.</li><li><p class="auto-cursor-target">In the <strong>Show</strong> drop-down menu of the open dialog, select <strong>All Projects</strong>. It will display all projects and standard profiles on the server.<strong><br /></strong></p></li><li>Click <ac:image ac:thumbnail="true" ac:height="14"><ri:attachment ri:filename="select_all_button.png" /></ac:image> on the left side of the dialog to select all projects and standard profiles.<br /><br /><ac:image><ri:attachment ri:filename="migrate_all_projects.png" /></ac:image><br /><br /></li><li>Click <strong>OK.</strong></li></ol><h3>Migrating standard profiles</h3><p>To migrate projects separately from standard profiles, you must first migrate the standard profiles.</p><p><br /></p><p>To migrate standard profiles</p><hr /><ol><li><ac:link><ri:page ri:content-title="Logging in to 3DEXPERIENCE platform" /><ac:link-body>Log in to the <strong>3D</strong>EXPERIENCE platform</ac:link-body></ac:link>.</li><li>Select the collaborative space dedicated for standard profiles:<br /><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="520a7b61-9400-4409-ba3f-3baad1057ad8"><ac:rich-text-body><p>It is highly recommended to store standard profiles in a public collaborative space. <span>To learn how to create a collaborative space, see <ac:link><ri:page ri:content-title="Adding standard profiles to 3DEXPERIENCE platform" /><ac:plain-text-link-body><![CDATA[Creating public collaborative spaces]]></ac:plain-text-link-body></ac:link>.</span></p></ac:rich-text-body></ac:structured-macro><ol><li>In the main menu, select <strong>3DEXPERIENCE</strong> &gt; <strong>Switch Platform/Credentials</strong>.</li><li>In the Credentials drop-down box of the open dialog, select the collaborative space.<br /><br /><ac:image><ri:attachment ri:filename="switching_to_public_space.png" /></ac:image><br /><br /></li><li>Click <strong>OK.</strong></li></ol></li><li><span>In the main menu, select </span><strong>Collaborate &gt; Migrate Projects to Version &lt;version number&gt;</strong>.</li><li><p class="auto-cursor-target">In the <strong>Show</strong> drop-down menu of the open dialog, select <strong>Standard Profiles</strong>. It will display all standard profiles on the server.<strong><br /></strong></p></li><li>Select the standard profiles you want to migrate or click <ac:image ac:thumbnail="true" ac:height="14"><ri:attachment ri:filename="select_all_button.png" /></ac:image> on the left side of the dialog to select all standard profiles.<br /><br /><ac:image><ri:attachment ri:filename="migrating_standard_profiles.png" /></ac:image><br /><br /></li><li>Click <strong>OK</strong>.</li></ol><h3>Migrating projects</h3><p>You can migrate projects either automatically through the dedicated dialog or manually by opening a project that has not yet been migrated. Please note that for either of these methods to work you have to <ac:link ac:anchor="Migrating standard profiles"><ac:plain-text-link-body><![CDATA[migrate standard profiles]]></ac:plain-text-link-body></ac:link> beforehand.</p><h4>Migrating projects automatically</h4><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="6aa46382-fdcd-42b5-af3f-b886fb9dd0e5"><ac:rich-text-body><p>If you migrate projects automatically through the dedicated dialog, all branches of the projects are migrated as well.</p></ac:rich-text-body></ac:structured-macro><p><br /></p><p>To migrate projects automatically</p><hr /><ol><li><span>In the main menu, select </span><strong>Collaborate &gt; Migrate Projects to Version &lt;version number&gt;</strong>.</li><li><p class="auto-cursor-target">In the <strong>Show</strong> drop-down menu of the open dialog, select <strong>Projects</strong>. It will display all projects on the server.<strong><br /></strong></p></li><li>Select the projects you want to migrate or click <ac:image ac:thumbnail="true" ac:height="14"><ri:attachment ri:filename="select_all_button.png" /></ac:image> on the left side of the dialog to select all projects.<br /><br /><ac:image><ri:attachment ri:filename="migrating_projects_automatically.png" /></ac:image><br /><br /></li><li>Click <strong>OK</strong>.</li></ol><h4>Migrating projects manually</h4><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="f5253671-1c28-4d83-a085-9cff791ad7cb"><ac:rich-text-body>If you choose to migrate a project that you are opening, only the branch that you are opening will be migrated.</ac:rich-text-body></ac:structured-macro><p><br /></p><p>To migrate a project manually</p><hr /><ol><li><span style="letter-spacing: 0.0px;">On the main menu, click </span><strong style="letter-spacing: 0.0px;">Collaborate</strong><span style="letter-spacing: 0.0px;"> &gt; </span><strong style="letter-spacing: 0.0px;">Projects</strong><span style="letter-spacing: 0.0px;">.</span></li><li>In the <strong style="letter-spacing: 0.0px;">Manage projects</strong><span> dialog, s</span>elect a project and click <strong style="letter-spacing: 0.0px;">Open</strong><span style="letter-spacing: 0.0px;">. A dialog opens telling you to update the System/Standard Profiles in the project.<br /><br /><ac:image><ri:attachment ri:filename="incompatible_system_profiles.png" /></ac:image><br /><br /></span></li><li>Click <strong>Continue</strong>.</li></ol><p><span style="letter-spacing: 0.0px;"><br />After the System/Standard Profiles are updated, you get a notification saying that the model was successfully updated.</span></p>
````

<!--NOMAGIC_PAGE id=243970123 space=CM version=3 -->
## PAGE 00279: Model merge in Teamwork Cloud

- page_id: `243970123`
- space_key: `CM`
- source_url: https://docs.nomagic.com/spaces/CM/pages/243970123/Model+merge+in+Teamwork+Cloud
- version_number: 3
- version_date: `2025-12-15T14:22:51.622+01:00`
- ancestors: Client-Side Collaborative Modeling Documentation > Using Teamwork Cloud
- labels: []

### NORMALIZED CONTENT

You need to have the Project Merge plugin installed to use the merge functionality.

700400

##### Starting model merge

Start the merge using either of the following:

- From Collaborate > Merge From :

You can apply this method of starting a merge exclusively to Teamwork Cloud projects. For Teamwork Cloud projects, you do not need to specify the ancestor; it will be instantly identified after the source is selected. By default, the lowest common parent of two branches is considered a common ancestor.

- From Tools > Project Merge .

You can apply this method of starting a merge to both local and Teamwork Cloud projects, although used projects can be included in a merge only for server projects. You must specify both the source and the ancestor, and manually choose the 3-way or 2-way merge.

- For Teamwork Cloud projects, the modeling tool automatically applies the 3-way merge, as a merge is only available between project versions from different branches.
- Partial locking of a project occurs when merging changes of a project in the Teamwork Cloud. Only changed/updated and merging elements are locked in the project, not the whole project. Thus, actions with other server project elements are not interrupted for other users by locking and merging activities.
- While merging with lock is in progress in a server project on the Teamwork Cloud server, other users cannot commit the changes to the server.

Conflicting changes detected during merge are automatically resolved by accepting changes either from the Source or the Target version. To specify a contributor, go to **Options** > **Environment** > **General** > **Merge and Compare** and then next to **Automatically Resolve Conflicts by Choosing**, select either **Target** or **Source**.

##### Model merge in Teamwork Cloud

To start a merge of the from **Collaborate** > **Merge From**

1. Open a server project that will be the [CONFLUENCE_PAGE title='(2026x) Model Merge' space='MT'] .
2. From the Collaborate menu, select Merge From .
3. In the opened dialog, select a server project that will be the [CONFLUENCE_PAGE title='(2026x) Model Merge' space='MT'].
4. Click the **OK** button. The question message illustrated below appears. [IMAGE alt='' src='']
5. Do one of the following:
  - Click **Merge with Lock**to lock the server project before merging. Other users cannot commit the changes.
  - Click **Merge without Lock** to perform the merge operation without locking the server project. We recommend that you select**Merge with Lock** to merge the project changes. To review the Merge Result, choose**Merge without Lock**.
  - Click Cancel merge process and close the dialog.
6. The project merge will start. If changes are found, the **Merge** window will open.
7. Proceed to [CONFLUENCE_PAGE title='(2026x) Analyzing and managing merge results' space='MT'].

In this case, **[CONFLUENCE_PAGE title='Understanding merge types in Teamwork Cloud' space='']** is considered a common ancestor by default.

To start merge from **Tools** > **Project Merge**

1. Open a project that will be the [CONFLUENCE_PAGE title='(2026x) Model Merge' space='MT'] .
2. From the Tools menu, select Project Merge . The Merge Projects dialog will open within the active project selected as the target.
3. Select a project that will be the [CONFLUENCE_PAGE title='(2026x) Model Merge' space='MT'].
4. Click the [ATTACHMENT filename='advanced_button.png'] Advanced button to see more merge options. Otherwise, go to .
5. In the Ancestor drop-down list, select either:
  - Lowest Common Parent to select the lowest common ancestor according to graph logic during the project merge.
  - Branch Point to select the version the branch was created from during the project merge.
6. In the Optimize for drop-down list, select either:
  - Speed , to merge the projects faster. This will require more memory.
  - **Memory,** to decrease memory usage while merging the projects if your computer does not have enough memory. This will use less memory but at the same time will slow down the merge procedure when the project has many changes in diagrams. It will not include the differing diagrams/elements count. If you need that information, select optimize for **Speed**. You can also specify the **Optimize for** option in the **Environment Options** dialog. Find this option under the **Merge and Compare** category in the **General** options group. If the **Low memory** notification keeps popping up during merge, we recommend that you do one of the following:increase the amount of memory allocated for the modeling tooloptimize Merge and Compare for **Memory** [IMAGE alt='' src='']
7. step7 Click the Merge button. The question message illustrated in the previous section will appear.
8. Do one of the following:
  - Click **Continue** to lock the server project and continue the merge process. Other users will not be able to commit changes.
  - Click **Show Merge Results**to proceed directly to the Merge Results.
9. The project merge will start. If changes are found, the **Merge** window will open. Proceed to [CONFLUENCE_PAGE title='(2026x) Analyzing and managing merge results' space='MT'].

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="warning" ac:schema-version="1" ac:macro-id="30548dd4-a918-4e75-9af9-01843c2bd473"><ac:rich-text-body>You need to have the Project Merge plugin installed to use the merge functionality. </ac:rich-text-body></ac:structured-macro><p style="text-align: center;"><ac:structured-macro ac:name="widget" ac:schema-version="1" ac:macro-id="47879fc4-996b-443a-b1e2-ae01f6af2d61"><ac:parameter ac:name="width">700</ac:parameter><ac:parameter ac:name="url"><ri:url ri:value="https://www.youtube.com/watch?v=nP5sqRlz3o8" /></ac:parameter><ac:parameter ac:name="height">400</ac:parameter></ac:structured-macro></p><h3>Starting model merge</h3><p>Start the merge using either of the following:</p><ul><li data-uuid="a304d414-8dfa-4109-af7e-2d1d33fa4d09">From <strong>Collaborate</strong> &gt; <strong>Merge From</strong>:</li></ul><p style="margin-left: 30.0px;">You can apply this method of starting a merge exclusively to Teamwork Cloud projects. For Teamwork Cloud projects, you do not need to specify the ancestor; it will be instantly identified after the s<span style="color:var(--ds-text,#333333);">ource is selected. By default, the lowest common parent of two branches is considered a common ancestor. </span></p><ul><li data-uuid="e414470b-0f88-4761-94a2-c0ee3ad8c8d0">From <strong>Tools</strong> &gt; <strong>Project Merge</strong>.</li></ul><p style="margin-left: 30.0px;">You can apply this method of starting a merge to both local and Teamwork Cloud projects, although used projects can be included in a merge only for server projects. You must specify both the source and the ancestor, and manually choose the 3-way or 2-way merge.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="2a5b6f6c-3f31-4a0a-b49c-79a67e74d9b3"><ac:rich-text-body><ul><li data-uuid="3e5b0285-8eae-47ab-979c-5520a8dff5e3">For Teamwork Cloud projects, the modeling tool automatically applies the 3-way merge, as a merge is only available between project versions from different branches. </li><li data-uuid="c66798c1-a47d-4df3-9c05-b75067851288">Partial locking of a project occurs when merging changes of a project in the Teamwork Cloud. Only changed/updated and merging elements are locked in the project, not the whole project. Thus, actions with other server project elements are not interrupted for other users by locking and merging activities.</li><li data-uuid="75246c90-2f9b-46c7-9f76-45eace1b3d21">While merging with lock is in progress in a server project on the Teamwork Cloud server, other users cannot commit the changes to the server.</li></ul></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="7913be13-1342-491a-8bdc-d24361cdc14d"><ac:rich-text-body><p>Conflicting changes detected during merge are automatically resolved by accepting changes either from the Source or the Target version. To specify a contributor, go to <strong>Options</strong> &gt; <strong>Environment</strong> &gt; <strong>General</strong> &gt; <strong>Merge and Compare</strong> and then next to <strong>Automatically Resolve Conflicts by Choosing</strong>, select either <strong>Target</strong> or <strong>Source</strong>.</p></ac:rich-text-body></ac:structured-macro><h3>Model merge in Teamwork Cloud</h3><p>To start a merge of the from <strong>Collaborate</strong> &gt; <strong>Merge From </strong></p><hr /><ol><li data-uuid="8b3371e2-4f83-4553-af50-14da9f4c2eed">Open a server project that will be the <ac:link ac:anchor="Target"><ri:page ri:space-key="MT" ri:content-title="(2026x) Model Merge" /><ac:plain-text-link-body><![CDATA[target]]></ac:plain-text-link-body></ac:link>.</li><li data-uuid="ae85d5f9-ceaa-48b4-b766-79604c0ff393">From the <strong>Collaborate</strong> menu, select <strong>Merge From</strong>.</li><li data-uuid="e39ffb02-d667-4fcf-a780-7b5fe4c6eacb">In the opened dialog, select a server project that will be the<span style="color:var(--ds-text,#000000);"> <ac:link ac:anchor="Source"><ri:page ri:space-key="MT" ri:content-title="(2026x) Model Merge" /><ac:plain-text-link-body><![CDATA[source]]></ac:plain-text-link-body></ac:link>.</span></li><li data-uuid="ba3f6ec7-0ac5-4f20-b946-f24172a51b02"><span style="color:var(--ds-text,#000000);">Click the <strong>OK</strong> button. The question message illustrated below appears.</span><br /><span style="color:var(--ds-text,#000000);"><ac:image><ri:attachment ri:filename="do_you_want_to_merge_the_project.png" /></ac:image> </span></li><li data-uuid="5c021501-8e5b-4118-9853-2d64e26af40d"><p>Do one of the following:</p><ul><li><p>Click <strong>Merge with Lock </strong>to lock the server project before merging. Other users cannot commit the changes.</p></li><li><p>Click <strong>Merge without Lock</strong> to perform the merge operation without locking the server project.</p><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="9d1f5671-8bd6-41d5-bcae-b6ed8dd21d51"><ac:rich-text-body>We recommend that you select<strong> Merge with Lock</strong> to merge the project changes. To review the Merge Result, choose<strong> Merge without Lock</strong>.</ac:rich-text-body></ac:structured-macro></li><li>Click<strong> Cancel</strong> merge process and close the dialog.</li></ul></li><li data-uuid="0e3ea61c-53b9-4097-8590-6f08a7d1169f"><span style="color:var(--ds-text,#000000);">The project merge will start. If changes are found, the <strong>Merge</strong> window will open. </span></li><li data-uuid="0d8ae2cb-1d3f-4bc8-b7b8-145c7495bfd8"><span style="color:var(--ds-text,#000000);">Proceed to <ac:link><ri:page ri:space-key="MT" ri:content-title="(2026x) Analyzing and managing merge results" /></ac:link>.</span></li></ol><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="d6de2283-e0e9-43fe-bbe9-285d1da28529"><ac:rich-text-body><p>In this case, <strong><ac:link><ri:page ri:content-title="Understanding merge types in Teamwork Cloud" /><ac:plain-text-link-body><![CDATA[Lowest Common Parent]]></ac:plain-text-link-body></ac:link></strong> is considered a common ancestor by default.</p></ac:rich-text-body></ac:structured-macro><p><br /></p><p>To start merge from <strong>Tools</strong> &gt; <strong>Project Merge</strong></p><hr /><ol><li data-uuid="6d5212aa-ca4c-4b36-9159-e458f451f734">Open a project that will be the <ac:link ac:anchor="Target"><ri:page ri:space-key="MT" ri:content-title="(2026x) Model Merge" /><ac:plain-text-link-body><![CDATA[target]]></ac:plain-text-link-body></ac:link> <span style="color:var(--ds-text,#000000);">.</span></li><li data-uuid="d9dea293-403e-4876-8dc4-609efbbe1479">From the <strong>Tools</strong> menu, select <strong>Project </strong> <strong>Merge</strong>. The <strong>Merge </strong> <strong>Projects</strong> dialog will open within the active project selected as the target.</li><li data-uuid="f00defbe-4772-4bcf-baf6-becfec9b9d34"><p>Select a project that will be the <ac:link ac:anchor="Source"><ri:page ri:space-key="MT" ri:content-title="(2026x) Model Merge" /><ac:plain-text-link-body><![CDATA[source]]></ac:plain-text-link-body></ac:link>.</p></li><li data-uuid="cc8e9e9b-b061-4cb8-9df4-6ac17e9aa1bc">Click the <ac:image ac:thumbnail="true" ac:height="16"><ri:attachment ri:filename="advanced_button.png" /></ac:image> <strong>Advanced</strong> button to see more merge options. Otherwise, go to<span style="color:var(--ds-text,#000000);"> <ac:link ac:anchor="step7"><ac:plain-text-link-body><![CDATA[step #7]]></ac:plain-text-link-body></ac:link> </span>.</li><li data-uuid="f3421c9c-756f-44f3-8488-c86f51001cf5">In the <strong>Ancestor</strong> drop-down list, select either:<ul><li><strong>Lowest Common Parent</strong> to select the lowest common ancestor according to graph logic during the project merge.</li><li><strong>Branch Point</strong> to select the version the branch was created from during the project merge.</li></ul></li><li data-uuid="a59d13e4-d230-4d03-8ecd-e752aa3b921a">In the <strong>Optimize for</strong> drop-down list, select either:<br /><ul><li><strong>Speed</strong>, to merge the projects faster. This will require more memory.</li><li><p><strong>Memory,</strong> to decrease memory usage while merging the projects if your computer does not have enough memory. This will use less memory but at the same time will slow down the merge procedure when the project has many changes in diagrams. It <span style="color:var(--ds-text,#000000);">will not include the differing diagrams/elements count. If you need that information, select optimize for <strong>Speed</strong>.</span></p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="ce850a66-b7f2-448c-89de-82dae8495005"><ac:rich-text-body><p>You can also specify the <strong>Optimize for</strong> option in the <strong>Environment Options</strong> dialog. Find this option under the <strong>Merge and Compare</strong> category in the <strong>General</strong> options group.</p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="cfcb70d8-2d48-4075-9e5e-4fc634774900"><ac:rich-text-body><p>If the <strong>Low memory</strong> notification keeps popping up during merge, we recommend that you do one of the following:</p><ul><li>increase the amount of memory allocated for the modeling tool</li><li>optimize Merge and Compare for <strong>Memory</strong></li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><ac:image><ri:attachment ri:filename="merge_projects_dialog_updated.png" /></ac:image></p></li></ul></li><li data-uuid="ca2fc857-a03c-4447-adcc-69d29e596b73"><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="61ef5e02-6b0a-46a9-b651-5adfd886a7ab"><ac:parameter ac:name="">step7</ac:parameter></ac:structured-macro>Click the <strong>Merge</strong> button. <span style="color:var(--ds-text,#000000);">The question message illustrated in the previous section will appear.</span></li><li data-uuid="b90bab0c-7249-483f-bad1-6ff8a6d90a89"><p>Do one of the following:</p><ul><li><p>Click <strong>Continue</strong> to lock the server project and continue the merge process. Other users will not be able to commit changes.</p></li><li><p>Click <strong>Show Merge Results </strong>to proceed directly to the Merge Results.</p></li></ul></li><li data-uuid="a87eba64-13c2-4d18-b8a6-c1cd2c0d5137"><p>The project merge will start. If changes are found, the <strong>Merge</strong> window will open. Proceed to <span style="color:var(--ds-text,#000000);"><ac:link><ri:page ri:space-key="MT" ri:content-title="(2026x) Analyzing and managing merge results" /></ac:link>.</span></p></li></ol>
````

<!--NOMAGIC_PAGE id=243970218 space=CM version=1 -->
## PAGE 00280: Modeling offline

- page_id: `243970218`
- space_key: `CM`
- source_url: https://docs.nomagic.com/spaces/CM/pages/243970218/Modeling+offline
- version_number: 1
- version_date: `2025-07-31T10:51:46.170+02:00`
- ancestors: Client-Side Collaborative Modeling Documentation > Collaboration powered by 3DEXPERIENCE platform
- labels: []

### NORMALIZED CONTENT

CATIA Magic and No Magic modeling tools allow working on server projects when the connection to the **3D**EXPERIENCEplatform is lost. You can make projects available offline, save changes locally, and commit them to the **3D**EXPERIENCEplatform when connection becomes available.

When modeling offline follow this workflow:

1. .
2. Work on the project as usual and save changes locally.
3. To resume your work, .
4. When you want to stop working on the project offline, [CONFLUENCE_PAGE title='Committing changes to 3DEXPERIENCE platform' space=''] and .

##### Making projects available offline

To start working on a project offline you have to save it locally as described below.

To make a project available offline

1. [CONFLUENCE_PAGE title='Opening projects from 3DEXPERIENCE platform' space=''] .
2. Do one of the following:
  - In the main menu, select Collaborate > Save Changes Locally / Make Available Offline .
  - In the main menu, select File > Save Project .

After making a project available offline, you can work on it as usual. When you want to save project changes locally, perform the second step in the above workflow.

#### NOTE: Offline project location

Offline project location

Offline projects are saved in the restricted folder of the user home directory, e.g. *<disk_name>\Users\<user_name>\AppData\Local\.<modeling_tool_name>\<modeling_tool_version>\restricted*. These projects are saved as multiple files in different folders, unlike the regular .mdzip files. You can only open offline projects from a modeling tool.

##### Opening offline projects

When you want to resume work on an offline project, you can open it either without updating, or open the project and automatically update it from the server.

To open an offline project

1. Do one of the following:
  - In the main menu of a modeling tool, select Collaborate > Open Server Project .
  - In the main menu of a modeling tool, select Collaborate > Projects .
2. In the open dialog, select the Offline Projects tab.
3. If you want to update a project after loading it, right-click the project and select **Update project After Load**. If you do not want to update the project, proceed to the next step. 
 
[IMAGE alt='' src=''] Keep in mind that if you select to update the project after loading, this option remains selected even after reloading the project.
4. Select the project you want to open and click the Open button.

##### Removing offline projects

If you want to stop working on a project offline, you need to [CONFLUENCE_PAGE title='Logging in to 3DEXPERIENCE platform' space=''], [CONFLUENCE_PAGE title='Committing changes to 3DEXPERIENCE platform' space=''], and remove the offline project version.

#### TIP: Force-opening server projects

Force-opening server projects

Keep in mind that in order to open a project from the server, you need to remove its offline version first. If you do not remove the offline project, the modeling tool will always load the locally saved project version even if you open the project from the **Online Projects** tab. However, if do not want to remove the offline project for some reason, you can force-open the project from the server by doing the following:

1. Do one of the following:
  - In the main menu of a modeling tool, select Collaborate > Open Server Project .
  - In the main menu of a modeling tool, select Collaborate > Projects .
2. In the Online Projects tab of the open dialog, right-click a project and select Open From Server .

To remove an offline project

1. In the main menu of a modeling tool, select Collaborate > Projects .
2. In the open dialog, select the Offline Projects tab.
3. Select the offline project you want to remove and click the Remove button.
4. When you are asked if you want to remove the offline version of the project, click Yes .

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>CATIA Magic and No Magic modeling tools allow working on server projects when the connection to the <span style="color: rgb(55,65,81);"><strong>3D</strong>EXPERIENCE </span>platform is lost. You can make projects available offline, save changes locally, and commit them to the <span style="color: rgb(55,65,81);"><strong>3D</strong>EXPERIENCE </span>platform when connection becomes available.</p><p>When modeling offline follow this workflow:</p><ol><li><ac:link ac:anchor="Making projects available offline"><ac:plain-text-link-body><![CDATA[Make a project available offline]]></ac:plain-text-link-body></ac:link>.</li><li>Work on the project as usual and save changes locally.</li><li>To resume your work, <ac:link ac:anchor="Opening offline projects"><ac:plain-text-link-body><![CDATA[open the offline project]]></ac:plain-text-link-body></ac:link>.</li><li>When you want to stop working on the project offline, <ac:link><ri:page ri:content-title="Committing changes to 3DEXPERIENCE platform" /><ac:plain-text-link-body><![CDATA[commit changes to the server]]></ac:plain-text-link-body></ac:link> and <ac:link ac:anchor="Removing offline projects"><ac:plain-text-link-body><![CDATA[remove the offline project version]]></ac:plain-text-link-body></ac:link>.</li></ol><h3><br />Making projects available offline</h3><p>To start working on a project offline you have to save it locally as described below.</p><p><br /></p><p>To make a project available offline</p><hr /><ol><li><ac:link><ri:page ri:content-title="Opening projects from 3DEXPERIENCE platform" /><ac:plain-text-link-body><![CDATA[Open a server project]]></ac:plain-text-link-body></ac:link>.</li><li>Do one of the following:<ul><li>In the main menu, select <strong>Collaborate</strong> &gt; <strong>Save Changes Locally / Make Available Offline</strong>.</li><li>In the main menu, select <strong>File</strong> &gt; <strong>Save Project</strong>.</li></ul></li></ol><p><br />After making a project available offline, you can work on it as usual. When you want to save project changes locally, perform the second step in the above workflow.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="717a0cef-7699-430b-b437-1d9e6e60ffee"><ac:parameter ac:name="title">Offline project location</ac:parameter><ac:rich-text-body><p>Offline projects are saved in the restricted folder of the user home directory, e.g. <em>&lt;disk_name&gt;\Users\&lt;user_name&gt;\AppData\Local\.&lt;modeling_tool_name&gt;\&lt;modeling_tool_version&gt;\restricted</em>. These projects are saved as multiple files in different folders, unlike the <span>regular .mdzip files</span>. You can only open offline projects from a modeling tool.</p></ac:rich-text-body></ac:structured-macro><h3 class="auto-cursor-target"><br />Opening offline projects</h3><p>When you want to resume work on an offline project, you can open it either without updating, or open the project and automatically update it from the server.</p><p><br /></p><p>To open an offline project</p><hr /><ol><li>Do one of the following:<ul><li>In the main menu of a modeling tool, select <strong>Collaborate</strong> &gt; <strong>Open Server Project</strong>.</li><li>In the main menu of a modeling tool, select <strong>Collaborate</strong> &gt; <strong>Projects</strong>.</li></ul></li><li>In the open dialog, select the <strong>Offline Projects</strong> tab.</li><li><p class="auto-cursor-target">If you want to update a project after loading it, right-click the project and select <strong>Update project After Load</strong>. If you do not want to update the project, proceed to the next step.<br /><br /><ac:image><ri:attachment ri:filename="updating_project_after_load.png" /></ac:image></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="95d24323-2fda-4bc6-8ca7-9cab2698edd0"><ac:rich-text-body><p><span style="color: rgb(62,63,64);">Keep in mind that if you select to update the project after loading, this option remains selected even after reloading the project.</span></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></li><li>Select the project you want to open and click the <strong>Open</strong> button.</li></ol><h3><br />Removing offline projects</h3><p>If you want to stop working on a project offline, you need to <ac:link><ri:page ri:content-title="Logging in to 3DEXPERIENCE platform" /><ac:plain-text-link-body><![CDATA[log in to the DEXPERIENCE platform]]></ac:plain-text-link-body></ac:link>, <ac:link><ri:page ri:content-title="Committing changes to 3DEXPERIENCE platform" /><ac:plain-text-link-body><![CDATA[commit the local project changes to the server]]></ac:plain-text-link-body></ac:link>, and remove the offline project version.</p><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="69b6ce28-3afc-42ed-aa96-83f78f574761"><ac:parameter ac:name="title">Force-opening server projects</ac:parameter><ac:rich-text-body><p>Keep in mind that in order to open a project from the server, you need to remove its offline version first. If you do not remove the offline project, the modeling tool will always load the locally saved project version even if you open the project from the <strong>Online Projects</strong> tab. However, if do not want to remove the offline project for some reason, you can force-open the project from the server by doing the following:</p><ol><li>Do one of the following:<ul><li>In the main menu of a modeling tool, select <strong>Collaborate</strong> &gt; <strong>Open Server Project</strong>.</li><li>In the main menu of a modeling tool, select <strong>Collaborate</strong> &gt; <strong>Projects</strong>.</li></ul></li><li>In the <strong>Online Projects</strong> tab of the open dialog, right-click a project and select <strong>Open From Server</strong>.</li></ol></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><p><br /></p><p>To remove an offline project</p><hr /><ol><li>In the main menu of a modeling tool, select <strong>Collaborate</strong> &gt; <strong>Projects</strong>.</li><li>In the open dialog, select the <strong>Offline Projects</strong> tab.</li><li>Select the offline project you want to remove and click the <strong>Remove</strong> button.</li><li>When you are asked if you want to remove the offline version of the project, click <strong>Yes</strong>.</li></ol>
````

<!--NOMAGIC_PAGE id=243970287 space=CM version=1 -->
## PAGE 00281: Moving elements to other 3DEXPERIENCE projects

- page_id: `243970287`
- space_key: `CM`
- source_url: https://docs.nomagic.com/spaces/CM/pages/243970287/Moving+elements+to+other+3DEXPERIENCE+projects
- version_number: 1
- version_date: `2025-07-31T10:51:47.580+02:00`
- ancestors: Client-Side Collaborative Modeling Documentation > Collaboration powered by 3DEXPERIENCE platform > Managing project usages in 3DEXPERIENCE platform
- labels: []

### NORMALIZED CONTENT

You can move selected elements from the main server project to a [CONFLUENCE_PAGE title='Managing project usages in 3DEXPERIENCE platform' space='']. The relations are also moved with the element(s).

#### WARNING: Moving cannot be undone

Moving cannot be undone

This action cannot be undone as a new version is automatically created and committed to the server after the selected elements are moved to a new location.

##### Moving elements to/from used projects

To move elements from the main server project to a used one

1. In the Model Browser, select one or more elements.
2. Right-click the selected elements. From the shortcut menu, choose **Refactor** > **Move Element(s) to Other Project**. You must commit the project to the server before moving elements.
3. The **Move Elements** dialog opens. Select a package or a classifier in the target project where you want to move the elements. You will see the classifier as a possible destination if only the****classifier elements are selected to move. Otherwise, only packages will be shown. Drag the selectionYou can drag and drop the selected elements to the target project package or classifier instead of using the shortcut menu. This action can be performed if the following conditions are met:if the selected elements to move contain at least one non-classifier element, it is restricted to drop to other targets than packages.if the selected elements to move contain only classifiers, moving is allowed to either packages or classifiers.
4. Do one of the following:
  1. 
    - Click Move to start moving elements or
    - Click Select More to specify your selection. The Select Elements dialog opens, in which you can:
      - add or remove some elements from a selection or
      - change the destination (click [ATTACHMENT filename='edit_button.png'] at the end of the row). The Select destination dialog will list destination targets by the type of the element selected to move (i.e. if it is a classifier element, classifiers will be listed in the Tree and List tabs). Otherwise only packages will be listed.
    - Click OK when you are done.
5. After you move the elements, new source project and target project versions are created and automatically committed to the server. Additionally , the used project is switched to the latest version .

**Related pages**

- [CONFLUENCE_PAGE title='Identifying Package Dependencies' space='MT']
- [CONFLUENCE_PAGE title='Using server projects' space='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p>You can move selected elements from the main server project to a <ac:link><ri:page ri:content-title="Managing project usages in 3DEXPERIENCE platform" /><ac:plain-text-link-body><![CDATA[directly used project]]></ac:plain-text-link-body></ac:link>. The relations are also moved with the element(s).</p><ac:structured-macro ac:name="warning" ac:schema-version="1" ac:macro-id="89025004-c1be-4198-bd1a-f967f8771a34"><ac:parameter ac:name="title">Moving cannot be undone</ac:parameter><ac:rich-text-body><p>This action cannot be undone as a new version is automatically created and committed to the server after the selected elements are moved to a new location.</p></ac:rich-text-body></ac:structured-macro><h3>Moving elements to/from used projects</h3><p>To move elements from the main server project to a used one</p><hr /><ol><li>In the Model Browser, select one or more elements.</li><li><p>Right-click the selected elements. From the shortcut menu, choose <strong>Refactor</strong> &gt; <strong>Move Element(s) to Other Project</strong>.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="9f84af1e-ec8b-4c75-b04d-50f03db92f98"><ac:rich-text-body><p>You must commit the project to the server before moving elements.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></li><li><p class="auto-cursor-target">The <strong>Move Elements</strong> dialog opens. Select a package or a classifier in the target project where you want to move the elements. You will see the classifier as a possible destination if <u>only</u> the<strong> </strong>classifier elements are selected to move. Otherwise, only packages will be shown.</p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="ce3366a9-1ded-4a81-bca6-ad16fca1eb55"><ac:parameter ac:name="title">Drag the selection</ac:parameter><ac:rich-text-body><p>You can drag and drop the selected elements to the target project package or classifier instead of using the shortcut menu. This action can be performed if the following conditions are met:</p><ul><li>if the selected elements to move contain at least one non-classifier element, it is restricted to drop to other targets than packages.</li><li>if the selected elements to move contain only classifiers, moving is allowed to either packages or classifiers.</li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></li><li>Do one of the following:<br /><ol><li style="list-style-type: none;background-image: none;"><ul><li>Click <strong>Move</strong> to start moving elements or </li><li>Click <strong>Select More</strong> to specify your selection. The <strong>Select Elements</strong> dialog opens, in which you can:<ul><li>add or remove some elements from a selection or</li><li>change the destination (click <ac:image ac:thumbnail="true" ac:height="20"><ri:attachment ri:filename="edit_button.png" /></ac:image> at the end of the row). The <strong>Select </strong><strong>destination</strong> dialog will list destination targets by the type of the element selected to move (i.e. if it is a classifier element, classifiers will be listed in the Tree and List tabs). Otherwise only packages will be listed.</li></ul></li><li>Click <strong>OK </strong>when you are done.</li></ul></li></ol></li><li>After you move the elements, <ac:inline-comment-marker ac:ref="3bcbfbad-bf0c-41ae-bea9-ebefad9b2871">new source project and target project versions are created and automatically committed to the server. Additionally</ac:inline-comment-marker><ac:inline-comment-marker ac:ref="ae0ed0f0-5aff-4cd6-a165-4372d3238912">, the <ac:inline-comment-marker ac:ref="adc14006-f02e-4428-b958-434a90a6ba5f">used</ac:inline-comment-marker> project is switched to the latest version</ac:inline-comment-marker>.</li></ol></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p style="margin-top: 10.0px;"><strong>Related pages</strong></p><ul style="margin-top: 0.0px;"><li><ac:link><ri:page ri:space-key="MT" ri:content-title="Identifying Package Dependencies" /></ac:link></li><li><ac:link><ri:page ri:content-title="Using server projects" /></ac:link></li></ul></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=243970043 space=CM version=2 -->
## PAGE 00282: Moving elements to other projects

- page_id: `243970043`
- space_key: `CM`
- source_url: https://docs.nomagic.com/spaces/CM/pages/243970043/Moving+elements+to+other+projects
- version_number: 2
- version_date: `2025-09-11T15:24:49.055+02:00`
- ancestors: Client-Side Collaborative Modeling Documentation > Using Teamwork Cloud
- labels: []

### NORMALIZED CONTENT

You can move selected elements from the main server project to a [CONFLUENCE_PAGE title='Managing used projects' space='MT']. The relations are also moved with the element(s).

#### WARNING: Moving cannot be undone

Moving cannot be undone

This action cannot be undone as a new version is automatically created and committed to the Teamwork Cloud server after the selected elements are moved to a new location.

#### WARNING: Permissions

Permissions

To move the elements to other projects, you must have:

- Read Resources, Edit Resources, Edit Resource Properties, and Administer Resources [permissions](https://docs.nomagic.com/MCS/?contextKey=permissions&version=latest&variant=default) on both source and target projects.
- You must have the read-write permission for the project branch you move elements to.

##### Moving elements to/from used projects

To move elements from the main server project to a used one

1. In the Model Browser, select one or more elements.
2. Right-click the selected elements. From the shortcut menu, choose Refactor > Move Element(s) to Other Project .
3. The **Move Elements** dialog opens. Select a package or a classifier in the target project where you want to move the elements. You will see the classifier as a possible destination **if**only classifier elements are selected to move. Otherwise, only packages will be shown. Drag the selectionYou can drag and drop the selected elements to the target project package or classifier instead of using the shortcut menu. This action can be performed if the following conditions are met:if the selected elements to move contain at least one non-classifier element, it is restricted to drop to other targets than packages.if the selected elements to move contain only classifiers, moving is allowed to either packages or classifiers.
4. Do one of the following:
  1. 
    - Click Move to start moving elements or
    - Click Select More to specify your selection. The Select Elements dialog opens, in which you can:
      - add or remove some elements from a selection or
      - change the destination (click [ATTACHMENT filename='edit_button.png'] at the end of the row). The Select destination dialog will list destination targets by the type of the element selected to move (i.e. if it is a classifier element, classifiers will be listed in the Tree and List tabs). Otherwise only packages will be listed.
    - Click OK when you are done.
5. A notification appears, asking if you want to [CONFLUENCE_PAGE title='Identifying Package Dependencies' space='MT']. Select **Yes**/**No** to continue moving elements. If elements being moved from the source project to the target project are dependent on other elements that are NOT moved together, the necessary usages to used projects are created in the project these elements are moved to. This is being done with the intention of keeping all the dependencies valid.
6. After you move the elements, new source project and target project versions are created and automatically committed to the server. Additionally, the used project is switched to the latest version.

To move elements from a used project to the main one

1. Open the used project and create a new package.
2. In the Model Browser, select the elements you want to move and drag them to the newly created package.
3. [CONFLUENCE_PAGE title='Exporting a package to a new server project' space='']to a new temporary project. If the elements you want to export have dependencies in the project you want to export them from, a dependency warning will be prompted in the**Package Dependencies**panel.
4. [CONFLUENCE_PAGE title='Stop using the project in your project' space=''], which is displayed under the package*Project Usages*in the Model Browser. Commit the changes.
5. Open the main project and [CONFLUENCE_PAGE title='Changing used project versions' space=''] containing the elements to its latest version (or remove it keeping references), in which the used project no longer contains the elements that were moved.
6. [CONFLUENCE_PAGE title='Using server projects' space=''] in the main project.
7. [CONFLUENCE_PAGE title='Importing the content of a used project into your project' space=''] to the project. Once you click the button, the Import dialog opens.
8. In the Import dialog, you can select to import the elements either with the new element IDs or with the old ones. It is recommended to delete the temporary project from the server repository once its data is imported to the main project, especially if the data is imported with the old IDs, to make sure there are no duplicate elements with the same element IDs.
  1. Selecting**Import with New IDs** creates new IDs for the imported elements in the main project. This way, element IDs are not duplicated, ensuring that the main project remains intact. However, if the elements of the used project are used in other projects, choosing **Import with****New IDs** may break those references. It is highly recommended to import elements with new IDs as it is the safest option regarding project consistency.
  2. Selecting **Import with Old IDs** imports the elements with their existing IDs, which can be useful if the elements are used in multiple other projects. However, this may cause duplicate element IDs, resulting in the main project being corrupted. To proceed with the import using the old IDs, click **Yes**in the **Question**dialog, acknowledging that the procedure might corrupt the data of the main project.
  3. **Question** dialog opens, click **Yes** to save and commit the changes.

##### Fixing element references in other projects

If the elements that were moved from a used project to a new one were used in other projects prior to the move, validation issues may occur in those projects once the elements are moved from their original project to a new one. The procedure for resolving such issues depends on whether the elements were imported with the old element IDs or the new ones during the element move procedure from a used project to a new one.

To fix references in other projects after the import

1. Validation issues will appear in the main project as the elements that were used from the used project no longer exist in the newest version of the used project. These elements will be displayed:
  - In a diagram - the element symbol is displayed with a red border and a letter*R* on its corner. 
[IMAGE alt='' src='']
  - In the Model Browser - the element is displayed with a red *X* mark and a letter *R*. 
[IMAGE alt='' src='']
  - In the **Active Validation Results**panel on the bottom right of the modeling tool. 
[IMAGE alt='' src='']
2. In the other project using the elements that are no longer contained in the used project, [CONFLUENCE_PAGE title='Using server projects' space=''] to which the elements were moved. If the elements were imported with the **old IDs**, Step 4 resolves the validation issues, as the newly used project contains the moved elements with the same old IDs that were initially used in this project.
3. If the elements were imported with the **new IDs**, validation issues will still remain after Step 4 as the element in the newly used project has a new ID, while the opened project used the element with the old ID. To resolve the issue:
  1. Double click on the element or its symbol, select Validation > Change Usages To . Select Element dialog opens.
  2. In the model tree, you can see both the previously used element with the old ID, displayed with a letter R on it and the newly used element with the new ID. Double-click on the newly used element to replace the used element with the old ID with the one with the new ID. [ATTACHMENT filename='validation_element_usage.png']

**An example**

Say you have three projects: Car Project, Library and Van. Car Project has element Doors. Project Van uses the Car Project and its element Doors in a diagram.

You decide to place the element Doors into a package *temp* and move it from the Car Project to the Library, by first using *temp* in the Library and then importing the data of the project *temp* to the Library (either with the old IDs or with the new ones).

You would then need to remove the used project *temp* from the Car Project and commit the changes. This removes the element Doors from the Car Project completely.

Now you would need to open the project Van, which uses the element Doors through the used project Car Project. The CarProject version would need to be updated to the latest one. This latest version no longer contains the element Doors, as it was moved to the Library. This will cause a validation issue in the project Van, as the element Doors is no longer to be found in the used project Car Project.

To resolve the validation issue, you would need to use the project Library, as it is the one containing the element Doors. If the data of the project *temp* was imported to the Library with the old IDs, the validation issue would be resolved. If the data was imported using the new IDs, the validation issue would remain, as the Van project would still have the instance of element Doors with the old ID. You would need to resolve the issue by selecting the element with the new ID (located in the newly used Library project) as described in Step 3.

**Related pages**

- [CONFLUENCE_PAGE title='Identifying Package Dependencies' space='MT']
- [CONFLUENCE_PAGE title='Using server projects' space='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p>You can move selected elements from the main server project to a <ac:link><ri:page ri:space-key="MT" ri:content-title="Managing used projects" /><ac:plain-text-link-body><![CDATA[directly used project]]></ac:plain-text-link-body></ac:link>. The relations are also moved with the element(s).</p><ac:structured-macro ac:name="warning" ac:schema-version="1" ac:macro-id="89025004-c1be-4198-bd1a-f967f8771a34"><ac:parameter ac:name="title">Moving cannot be undone</ac:parameter><ac:rich-text-body><p>This action cannot be undone as a new version is automatically created and committed to the Teamwork Cloud server after the selected elements are moved to a new location.</p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="warning" ac:schema-version="1" ac:macro-id="188523c3-85dc-470e-a29a-2d6e920233d6"><ac:parameter ac:name="title">Permissions</ac:parameter><ac:rich-text-body><p>To move the elements to other projects, you must have:</p><ul><li data-uuid="581bcad8-0275-4540-a50c-b02dbfa9b621"><p class="auto-cursor-target"><span style="color:var(--ds-text,#333333);">Read Resources, Edit Resources, Edit Resource Properties,</span> and Administer Resources <a href="https://docs.nomagic.com/MCS/?contextKey=permissions&amp;version=latest&amp;variant=default">permissions</a> on both source and target projects.</p></li><li data-uuid="dc661cfb-1246-4d3f-aaf4-94ae11173778">You must have the read-write permission for the project branch you move elements to.</li></ul></ac:rich-text-body></ac:structured-macro><h3>Moving elements to/from used projects</h3><p><br /></p><p>To move elements from the main server project to a used one</p><hr /><ol><li data-uuid="73becadc-779b-4114-9cac-f0312c352ff0">In the Model Browser, select one or more elements.</li><li data-uuid="94ea7082-b45e-4e15-89d8-2656cfac9930">Right-click the selected elements. From the shortcut menu, choose <strong>Refactor</strong> &gt; <strong>Move Element(s) to Other Project</strong>. </li><li data-uuid="1009fe28-450f-4e1a-8608-30267b7515bb"><p class="auto-cursor-target">The <strong>Move Elements</strong> dialog opens. Select a package or a classifier in the target project where you want to move the elements. You will see the classifier as a possible destination <strong>if </strong>only classifier elements are selected to move. Otherwise, only packages will be shown.</p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="ce3366a9-1ded-4a81-bca6-ad16fca1eb55"><ac:parameter ac:name="title">Drag the selection</ac:parameter><ac:rich-text-body><p>You can drag and drop the selected elements to the target project package or classifier instead of using the shortcut menu. This action can be performed if the following conditions are met:</p><ul><li>if the selected elements to move contain at least one non-classifier element, it is restricted to drop to other targets than packages.</li><li>if the selected elements to move contain only classifiers, moving is allowed to either packages or classifiers.</li></ul></ac:rich-text-body></ac:structured-macro></li><li data-uuid="ebff1452-b147-4370-8195-ff495a283e9f">Do one of the following:<br /><ol><li style="list-style-type: none;background-image: none;"><ul><li>Click <strong>Move</strong> to start moving elements or </li><li>Click <strong>Select More</strong> to specify your selection. The <strong>Select Elements</strong> dialog opens, in which you can:<ul><li>add or remove some elements from a selection or</li><li>change the destination (click <ac:image ac:thumbnail="true" ac:height="20"><ri:attachment ri:filename="edit_button.png" /></ac:image> at the end of the row). The <strong>Select </strong><strong>destination</strong> dialog will list destination targets by the type of the element selected to move (i.e. if it is a classifier element, classifiers will be listed in the Tree and List tabs). Otherwise only packages will be listed.</li></ul></li><li>Click <strong>OK </strong>when you are done.</li></ul></li></ol></li><li data-uuid="1f99919b-8c6b-4621-9290-cdb9c582d010"><p class="auto-cursor-target">A notification appears, asking if you want to <ac:link><ri:page ri:space-key="MT" ri:content-title="Identifying Package Dependencies" /><ac:plain-text-link-body><![CDATA[check dependencies among projects]]></ac:plain-text-link-body></ac:link>. Select <strong>Yes</strong>/<strong>No</strong> to continue moving elements. </p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="724fb065-179d-4572-9b0d-09372c2075bf"><ac:rich-text-body><p>If elements being moved from the source project to the target project are dependent on other elements that are NOT moved together, the necessary usages to used projects are created in the project these elements are moved to. This is being done with the intention of keeping all the dependencies valid.</p></ac:rich-text-body></ac:structured-macro></li><li data-uuid="6b168d05-a66a-46a8-b212-9174dd2f87e5">After you move the elements, new source project and target project versions are created and automatically committed to the server. Additionally, the used project is switched to the latest version.</li></ol><p><br /></p><p>To move elements from a used project to the main one</p><hr /><ol><li data-uuid="e6e83dba-d65e-4a3c-95ed-9ff7d4863e74">Open the used project and create a new package. </li><li data-uuid="00306e8e-e25a-4e19-99ba-c906d0cdb6de">In the Model Browser, select the elements you want to move and drag them to the newly created package.</li><li data-uuid="560bd4e7-09bb-45fa-844b-8acd63724b77"><p class="auto-cursor-target"><ac:link><ri:page ri:content-title="Exporting a package to a new server project" /><ac:plain-text-link-body><![CDATA[Export the package]]></ac:plain-text-link-body></ac:link><span> to a new temporary project.</span></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="1f34be04-e5b1-40f1-bfb4-5172313f2d16"><ac:rich-text-body><p><span>If the elements you want to export have dependencies in the project you want to export them from, a dependency warning will be prompted in the </span><strong>Package Dependencies </strong><span>panel</span><span>.</span></p></ac:rich-text-body></ac:structured-macro></li><li data-uuid="37151865-46da-4082-b9a9-e86156968f7e"><p><ac:link><ri:page ri:content-title="Stop using the project in your project" /><ac:plain-text-link-body><![CDATA[Remove the used temporary project]]></ac:plain-text-link-body></ac:link>, which is displayed <span style="color:var(--ds-text,#333333);">under the package </span><em>Project Usages</em><span style="color:var(--ds-text,#333333);"> in the Model Browser. Commit the changes.</span></p></li><li data-uuid="459eb299-d0fe-4bef-99e5-4e6acbebf298">Open the main project and <ac:link><ri:page ri:content-title="Changing used project versions" /><ac:plain-text-link-body><![CDATA[update the used project]]></ac:plain-text-link-body></ac:link> containing the elements to its latest version (or remove it keeping references), in which the used project no longer contains the elements that were moved.</li><li data-uuid="079c4754-f9c7-4608-ae9c-6f75c7f8bf7d"><p><ac:link><ri:page ri:content-title="Using server projects" /><ac:plain-text-link-body><![CDATA[Use the new temporary project]]></ac:plain-text-link-body></ac:link> in the main project.</p></li><li data-uuid="c3ae075c-a77a-440f-8374-2d352c3dc575"><ac:link><ri:page ri:content-title="Importing the content of a used project into your project" /><ac:plain-text-link-body><![CDATA[Import the content of the used temporary project]]></ac:plain-text-link-body></ac:link> to the project. Once you click the <ac:image><ri:url ri:value="https://docs.nomagic.com/download/thumbnails/9918725/import_button.png?version=1&amp;modificationDate=1505898528100&amp;api=v2" /></ac:image> button, the <strong>Import</strong> dialog opens. </li><li data-uuid="5b3dff94-f5a2-4b45-b73f-e6c11c41bd31">In the <strong>Import</strong> dialog, you can select to import the elements either with the new element IDs or with the old ones.<ol><li><p class="auto-cursor-target">Selecting<strong> Import with New IDs</strong> creates new IDs for the imported elements in the main project. This way, element IDs are not duplicated, ensuring that the main project remains intact. However, if the elements of the used project are used in other projects, choosing <strong>Import with </strong><strong>New IDs</strong> may break those references.</p><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="f73d9e1f-6144-49a9-b69c-3c28a0861585"><ac:rich-text-body><p>It is highly recommended to import elements with new IDs as it is the safest option regarding project consistency.</p></ac:rich-text-body></ac:structured-macro></li><li><p class="auto-cursor-target">Selecting <strong>Import with Old IDs</strong> imports the elements with their existing IDs, which can be useful if the elements are used in multiple other projects. However, this may cause duplicate element IDs, resulting in the main project being corrupted. To proceed with the import using the old IDs, click <strong>Yes </strong>in the <strong>Question </strong>dialog, acknowledging that the procedure might corrupt the data of the main project.</p></li><li><p><strong>Question</strong> dialog opens, click <strong>Yes</strong> to save and commit the changes.</p></li></ol><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="cfd4b919-4a1c-45f1-aa3c-6b4eed802ddf"><ac:rich-text-body><p>It is recommended to delete the temporary project from the server repository once its data is imported to the main project, especially if the data is imported with the old IDs, to make sure there are no duplicate elements with the same element IDs.</p></ac:rich-text-body></ac:structured-macro></li></ol><h3>Fixing element references in other projects</h3><p>If the elements that were moved from a used project to a new one were used in other projects prior to the move, validation issues may occur in those projects once the elements are moved from their original project to a new one. The procedure for resolving such issues depends on whether the elements were imported with the old element IDs or the new ones during the element move procedure from a used project to a new one. </p><p><br /></p><p>To fix references in other projects after the import</p><hr /><ol><li data-uuid="bfbcb4d9-fb02-46f3-90f3-92866d145c63"><p>Validation issues will appear in the main project as the elements that were used from the used project no longer exist in the newest version of the used project. These elements will be displayed:</p><ul><li><p>In a diagram - the element symbol is displayed with a red border and a letter<em> R</em> on its corner.<br /><ac:image><ri:attachment ri:filename="validation_issues.png" /></ac:image></p></li><li><p>In the Model Browser - the element is displayed with a red <em>X</em> mark and a letter <em>R</em>.<br /><ac:image><ri:attachment ri:filename="validation_issues2.png" /></ac:image></p></li><li><p>In the <strong>Active Validation Results </strong>panel on the bottom right of the modeling tool.<br /><ac:image ac:thumbnail="true" ac:height="23"><ri:attachment ri:filename="validation_issues3.png" /></ac:image></p></li></ul></li><li data-uuid="51c16dc3-7314-4400-b199-97f2be742461"><p>In the other project using the elements that are no longer contained in the used project, <ac:link><ri:page ri:content-title="Using server projects" /><ac:plain-text-link-body><![CDATA[use the new project]]></ac:plain-text-link-body></ac:link> to which the elements were moved.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="2ced5b4e-2e03-403e-8725-9ab781a3ad43"><ac:rich-text-body><p>If the elements were imported with the <strong>old IDs</strong>, Step 4 resolves the validation issues, as the newly used project contains the moved elements with the same old IDs that were initially used in this project.</p></ac:rich-text-body></ac:structured-macro></li><li data-uuid="d12d6d01-3b6d-443b-a219-b67f9ac311c5"><p>If the elements were imported with the <strong>new IDs</strong>, v<span>alidation issues will still remain after Step 4 as the element in the newly used project has a new ID, while the opened project used the element with the old ID. To resolve the issue:</span></p><ol><li>Double click on the element or its symbol, select <strong>Validation</strong> &gt; <strong>Change Usages To</strong>. <strong>Select Element </strong>dialog opens. </li><li>In the model tree, you can see both the previously used element with the old ID, displayed with a letter <em>R</em> on it and the newly used element with the new ID. Double-click on the newly used element to replace the used element with the old ID with the one with the new ID.<br /><ac:image><ri:attachment ri:filename="validation_element_usage.png" /></ac:image><br /><br /></li></ol></li></ol><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="dc64272a-f3a2-4c32-bb43-a79e893a018a"><ac:rich-text-body><p><strong>An example</strong></p><p>Say you have three projects: Car Project, Library and Van. <span>Car Project has element Doors. Project Van uses the Car Project and its element Doors in a diagram. </span></p><p><span>You decide to place the element Doors into a package <em>temp</em> and move it from the Car Project to the <span>Library, by first using <span><em>temp</em> in the Library and then</span> importing the data of the project <em>temp</em> to the Library (either with the old IDs or with the new ones). </span></span></p><p><span>You would then need to remove the used project <em>temp</em> from the <span>Car Project and commit the changes. This removes the element Doors from the Car Project completely.</span></span></p><p><span>Now you would need to open the project Van, which uses the element Doors through the used project <span>Car Project. The Car<span> Project version would need to be updated to the latest one. This latest version no longer contains the element Doors, as it was moved to the <span>Library. This will cause a validation issue in the <span>project Van, as the element Doors is no longer to be found in the used project Car Project.</span></span></span></span></span></p><p><span>To resolve the validation issue, you would need to use the project <span>Library, as it is the one containing the element Doors. If the data of the project <em>temp</em> was imported to the <span>Library with the old IDs, the validation issue would be resolved. If the data was imported using the new IDs, the validation issue would remain, as the Van project would still have the instance of element Doors with the old ID. You would need to resolve the issue by selecting the element with the new ID (located in the newly used Library project) as described in Step 3. </span></span></span></p></ac:rich-text-body></ac:structured-macro></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><strong>Related pages</strong></p><ul><li data-uuid="52bdcbe7-8275-48c3-89e4-3bb6036853db"><ac:link><ri:page ri:space-key="MT" ri:content-title="Identifying Package Dependencies" /></ac:link></li><li data-uuid="2e6dd9b2-16f5-4011-b639-3859fd77597e"><ac:link><ri:page ri:content-title="Using server projects" /></ac:link></li></ul></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=243969825 space=CM version=1 -->
## PAGE 00283: Offline modeling

- page_id: `243969825`
- space_key: `CM`
- source_url: https://docs.nomagic.com/spaces/CM/pages/243969825/Offline+modeling
- version_number: 1
- version_date: `2025-07-31T10:51:38.024+02:00`
- ancestors: Client-Side Collaborative Modeling Documentation > Using Teamwork Cloud
- labels: ['offline-project', 'offline-projects', 'update-offline-project']

### NORMALIZED CONTENT

#### CONTENT-LAYER: The selection to update is persistent

745137283

#### CONTENT-COLUMN: The selection to update is persistent

745137285

#### CONTENT-BLOCK: The selection to update is persistent

745137284

The Teamwork Cloud server supports offline modeling by allowing you to:

- Work with the project (read/edit) when a connection to the server is not available.
- Save intermediate changes locally (privately), and commit changes to the server when required.
- Save time by saving changes locally, which is much faster than committing directly to the server.

In an offline project, you can:

- Edit elements locked by a current user.
- Edit element symbols of elements locked by a current user.
- Create new elements/diagrams in the model.
- Review a project structure (used projects), project options, and styles.
- Save changes locally.
- Use a local project (if permissions allow).

When a connection is established, you can commit and/or update project changes, and lock or unlock project elements.

##### Make project available offline

To make an online project available offline

1. Open a server project.
2. From the main menu, select one of the following:

- 
  - Collaborate > Saves Changes Locally / Make available offline .
  - File > Save Project .

#### NOTE: Not a local copy of a server project

Not a local copy of a server project

This is **not** a local copy of a server project! All user locks and changes are saved within the project, so the offline project can be committed to the server later.

#### NOTE: Offline project location

Offline project location

Offline projects are saved in the restricted folder of the user home directory, e.g. *<disk_name>\Users\<user_name>\AppData\Local\.<modeling_tool_name>\<modeling_tool_version>\restricted*. These projects are saved as multiple files in different folders, unlike the regular .mdzip files. You can only open offline projects through the modeling tool.

##### Open offline project

To open an offline project

1. From the Collaborate menu, select either Open Server Project (or press Ctrl+Shift+O), or Projects .
2. In the open dialog, click the Offline Projects tab and select the offline project to open.

In the title bar, you can see information about a project opened from TWCloud. This information allows you to distinguish Online from Offline projects:

If you open the Online project, the title bar will show:

- Modeling tool name and version,
- Project name,
- Project trunk or branch,
- Project version,
- Server name.

[IMAGE alt='' src='']

If you open the Offline project, the title bar will show:

- Project name,
- Project trunk or branch,
- Project version,
- Server name,
- Last user who saved the project,
- Available Offline.

[IMAGE alt='' src='']

##### Update project after load

You can open the project as it is saved locally (without checking for the latest updates) or open the project and update it automatically from the server, if a connection is available.

To include updates, right-click the selected project and select **Update Project After Load** for each project you want to update when loading.

[IMAGE alt='' src='']

#### NOTE: The selection to update is persistent

The selection to update is persistent

Keep in mind that if you select to update the project after loading it is persistent and remains selected after reloading the project.

****

##### **Remove offline project**

To stop using the offline project version you need to remove it. This action does not remove a project from the server; it only removes the offline copy from the actual local machine. However, if you do not want that offline project would be removed, you can [CONFLUENCE_PAGE title='Opening Teamwork Cloud projects' space='']. In this case, changes made to the offline project and not committed will be lost.

To remove an offline project

1. From the Collaborate main menu, select Projects... . The Manage Projects dialog opens.
2. In the Manage Projects dialog open Offline Projects tab.
3. Select an offline project and click the Remove button.

745137282

**Related pages**

- [CONFLUENCE_PAGE title='Committing changes to Teamwork Cloud' space='']
- [CONFLUENCE_PAGE title='Locking model for edit' space='']
- [CONFLUENCE_PAGE title='Unlocking model' space='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="db9a57d6-1dec-4686-b3b0-515c950824de"><ac:parameter ac:name="id">745137283</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="02a13b6d-5e8b-4eda-a440-cea22d96cd7a"><ac:parameter ac:name="id">745137285</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="dfa854fb-bf22-4d88-9c67-b0d4d03e4e44"><ac:parameter ac:name="id">745137284</ac:parameter><ac:rich-text-body><p>The Teamwork Cloud server supports offline modeling by allowing you to:</p><ul><li>Work with the project (read/edit) when a connection to the server is not available.</li><li>Save intermediate changes locally (privately), and commit changes to the server when required.</li><li>Save time by saving changes locally, which is much faster than committing directly to the server.</li></ul><p>In an offline project, you can:</p><ul><li>Edit elements locked by a current user.</li><li>Edit element symbols of elements locked by a current user.</li><li>Create new elements/diagrams in the model.</li><li>Review a project structure (used projects), project options, and styles.</li><li>Save changes locally.</li><li>Use a local project (if permissions allow).</li></ul><p>When a connection is established, you can commit and/or update project changes, and lock or unlock project elements.</p><p><br /></p><h3>Make project available offline</h3><p>To make an online project available offline</p><hr /><ol><li>Open a server project.</li><li>From the main menu, select one of the following:</li></ol><ul><li style="list-style-type: none;background-image: none;"><ul><li><strong>Collaborate</strong> &gt; <strong>Saves Changes Locally / Make available offline</strong>.</li><li><strong>File</strong> &gt; <strong>Save Project</strong>.</li></ul></li></ul><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="caa679bb-7c95-4af0-b78b-584129db734e"><ac:parameter ac:name="title">Not a local copy of a server project</ac:parameter><ac:rich-text-body><p>This is <strong>not</strong> a local copy of a server project! All user locks and changes are saved within the project, so the offline project can be committed to the server later.</p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="717a0cef-7699-430b-b437-1d9e6e60ffee"><ac:parameter ac:name="title">Offline project location</ac:parameter><ac:rich-text-body><p>Offline projects are saved in the restricted folder of the user home directory, e.g. <em>&lt;disk_name&gt;\Users\&lt;user_name&gt;\AppData\Local\.&lt;modeling_tool_name&gt;\&lt;modeling_tool_version&gt;\restricted</em>. These projects are saved as multiple files in different folders, unlike the <span style="letter-spacing: 0.0px;">regular .mdzip files</span>. You can only open offline projects through the modeling tool.</p></ac:rich-text-body></ac:structured-macro><h3><br />Open offline project</h3><p>To open an offline project</p><hr /><ol><li>From the <strong>Collaborate</strong> menu, select either <strong>Open Server Project </strong>(or press Ctrl+Shift+O), or <strong>Projects</strong>.</li><li>In the open dialog, click the <strong>Offline Projects</strong> tab and select the offline project to open.</li></ol><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="78d8afde-e9d2-4c5b-9968-3cef65be42d2"><ac:rich-text-body><p><span>In the title bar, you can see information about a project opened from TWCloud. This information allows you to distinguish Online from Offline projects: </span></p><p>If you open the Online project, the title bar will show: </p><ul><li>Modeling tool name and version,</li><li>Project name,</li><li>Project trunk or branch,</li><li>Project version,</li><li>Server name.</li></ul><p><ac:image><ri:attachment ri:filename="Title bar information.PNG" /></ac:image></p><p>If you open the Offline project, <span>the title bar will show:</span></p><ul><li>Project name,</li><li>Project trunk or branch,</li><li>Project version,</li><li>Server name,</li><li><span>Last user who saved the project,</span></li><li>Available Offline.</li></ul><p><ac:image><ri:attachment ri:filename="Title bar information offline.PNG" /></ac:image></p></ac:rich-text-body></ac:structured-macro><p><br /></p><h3>Update project after load</h3><p>You can open the project as it is saved locally (without checking for the latest updates) or open the project and update it automatically from the server, if a connection is available.</p><p>To include updates, right-click the selected project and select <strong>Update Project After Load</strong> for each project you want to update when loading.</p><p class="auto-cursor-target"><ac:image ac:align="center"><ri:attachment ri:filename="update_project_after_load.png" /></ac:image></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="08e4f77b-768a-4a8a-923c-2287c37e83f4"><ac:parameter ac:name="title">The selection to update is persistent</ac:parameter><ac:rich-text-body><p>Keep in mind that if you select to update the project after loading it is persistent and remains selected after reloading the project.</p></ac:rich-text-body></ac:structured-macro><p><strong style="letter-spacing: 0.0px;"> <br /></strong></p><h3><strong style="letter-spacing: 0.0px;">Remove offline project</strong></h3><p>To stop using the offline project version you need to remove it. <span>This action does not remove a project from the server; it only removes the offline copy from the actual local machine. However, if you do not want that offline project would be removed, you can <ac:link><ri:page ri:content-title="Opening Teamwork Cloud projects" /><ac:plain-text-link-body><![CDATA[force open server project]]></ac:plain-text-link-body></ac:link>. In this case, changes made to the offline project and not committed will be lost. </span></p><p><span> <br /></span></p><p>To remove an offline project</p><hr /><ol><li>From the <strong>Collaborate</strong> main menu, select <strong>Projects...</strong>. The <strong>Manage Projects</strong> dialog opens.</li><li>In the <strong>Manage Projects</strong> dialog open <strong>Offline Projects</strong> tab. </li><li>Select an offline project and click the <strong>Remove</strong> button.</li></ol></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="464ebe22-ee41-4d79-98d8-f18cd77a327c"><ac:parameter ac:name="id">745137282</ac:parameter><ac:rich-text-body><p><strong>Related pages</strong></p><ul><li><ac:link><ri:page ri:content-title="Committing changes to Teamwork Cloud" /></ac:link></li><li><ac:link><ri:page ri:content-title="Locking model for edit" /></ac:link></li><li><ac:link><ri:page ri:content-title="Unlocking model" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=243970182 space=CM version=1 -->
## PAGE 00284: Opening projects from 3DEXPERIENCE platform

- page_id: `243970182`
- space_key: `CM`
- source_url: https://docs.nomagic.com/spaces/CM/pages/243970182/Opening+projects+from+3DEXPERIENCE+platform
- version_number: 1
- version_date: `2025-07-31T10:51:45.513+02:00`
- ancestors: Client-Side Collaborative Modeling Documentation > Collaboration powered by 3DEXPERIENCE platform
- labels: []

### NORMALIZED CONTENT

In this chapter you can learn how to open a server project from the **3D**EXPERIENCEplatform.

To open server projects from the **3D**EXPERIENCEplatform, you must [CONFLUENCE_PAGE title='Logging in to 3DEXPERIENCE platform' space=''] first.

To open a project from the **3D**EXPERIENCEplatform

1. Do one of the following:
  - In the main menu of a modeling tool, select Collaborate > Open Server Project .
  - In the main menu of a modeling tool, select Collaborate > Projects .
2. In the open dialog, select the project you want to open and click the Open button. [ATTACHMENT filename='opening_server_projects.png']

When a project opens, you can start working on it immediately in parallel with other users (if there are any users working on the same project). Make sure to [CONFLUENCE_PAGE title='Committing changes to 3DEXPERIENCE platform' space='']commit changes to the **3D**EXPERIENCE platform after you finish working on the project.

#### NOTE: Modeling offline

Modeling offline

If you worked on a server project offline and there is an offline project version available (displayed in the**Offline****Projects** tab of the **Open Server Project** dialog), the offline project will be opened even if you choose to open the project from the**Online Projects**tab. This mechanism ensures that the changes made to the offline project version are not lost.

For more information about working with server projects offline, see [CONFLUENCE_PAGE title='Modeling offline' space=''].

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>In this chapter you can learn how to open a server project from the <span style="color: rgb(55,65,81);"><strong>3D</strong>EXPERIENCE </span>platform.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="97820265-56fc-4fa5-96fb-340b982db553"><ac:rich-text-body><p>To open server projects from the <span style="color: rgb(55,65,81);"><strong>3D</strong>EXPERIENCE </span>platform, you must <ac:link><ri:page ri:content-title="Logging in to 3DEXPERIENCE platform" /><ac:plain-text-link-body><![CDATA[log in to the platform]]></ac:plain-text-link-body></ac:link> first.</p></ac:rich-text-body></ac:structured-macro><p><br /></p><p>To open a project from the <span style="color: rgb(55,65,81);"><strong>3D</strong>EXPERIENCE </span>platform</p><hr /><ol><li>Do one of the following:<ul><li>In the main menu of a modeling tool, select <strong>Collaborate</strong> &gt; <strong>Open Server Project</strong>.</li><li>In the main menu of a modeling tool, select <strong>Collaborate</strong> &gt; <strong>Projects</strong>.</li></ul></li><li>In the open dialog, select the project you want to open and click the <strong>Open</strong> button.<br /><br /><ac:image><ri:attachment ri:filename="opening_server_projects.png" /></ac:image></li></ol><p><br />When a project opens, you can start working on it immediately in parallel with other users (if there are any users working on the same project). Make sure to <ac:link><ri:page ri:content-title="Committing changes to 3DEXPERIENCE platform" /><ac:link-body>commit changes to the <strong>3D</strong>EXPERIENCE platform</ac:link-body></ac:link> after you finish working on the project.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="5511b6b2-8415-4d4f-9d62-5edf2572a0cf"><ac:parameter ac:name="title">Modeling offline</ac:parameter><ac:rich-text-body><p><span style="color: rgb(62,63,64);"><span style="color: rgb(62,63,64);">If you worked on a server project offline and there is an offline project version available (displayed in the </span><strong style="color: rgb(62,63,64);">Offline </strong><span style="color: rgb(62,63,64);"><strong>Projects</strong> tab of the <strong>Open Server Project</strong> dialog), the offline project will be opened even if you choose to open the project from the </span></span><strong>Online Projects</strong><span style="color: rgb(62,63,64);"> tab. This mechanism ensures that the changes made to the offline project version are not lost.</span></p><p>For more information about working with server projects offline, see <ac:link><ri:page ri:content-title="Modeling offline" /></ac:link>.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p>
````

<!--NOMAGIC_PAGE id=243970227 space=CM version=1 -->
## PAGE 00285: Opening projects in Collaborative Lifecycle app

- page_id: `243970227`
- space_key: `CM`
- source_url: https://docs.nomagic.com/spaces/CM/pages/243970227/Opening+projects+in+Collaborative+Lifecycle+app
- version_number: 1
- version_date: `2025-07-31T10:51:46.693+02:00`
- ancestors: Client-Side Collaborative Modeling Documentation > Collaboration powered by 3DEXPERIENCE platform
- labels: []

### NORMALIZED CONTENT

You can use a modeling tool to open a server project in the Collaborative Lifecycle app on the **3D**EXPERIENCEPlatform.

To open a project in the Collaborative Lifecycle app

1. [CONFLUENCE_PAGE title='Opening projects from 3DEXPERIENCE platform' space=''].
2. In the main menu, select **3DEXPERIENCE** > **Open in Collaborative Lifecycle App**.

After completing the steps above, the project is opened in the Collaborative Lifecycle app whichprovides the commands to manage thelifecycle of a project (from creation to deletion).

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>You can use a modeling tool to open a server project in the Collaborative Lifecycle app on the <span style="color: rgb(55,65,81);"><strong>3D</strong>EXPERIENCE </span>Platform.</p><p><span style="color: rgb(0,0,0);"><br /></span></p><p><span style="color: rgb(0,0,0);">To open a project in the Collaborative Lifecycle app</span></p><hr /><ol><li><span style="color: rgb(0,0,0);"><ac:link><ri:page ri:content-title="Opening projects from 3DEXPERIENCE platform" /><ac:plain-text-link-body><![CDATA[Open a server project]]></ac:plain-text-link-body></ac:link>.</span></li><li><span style="color: rgb(0,0,0);">In the main menu, select <strong>3DEXPERIENCE</strong> &gt; <strong>Open in Collaborative Lifecycle App</strong>.</span></li></ol><p><br /><span style="color: rgb(0,0,0);">After completing the steps above, the project is opened in t<span style="color: rgb(62,63,64);">he Collaborative Lifecycle app which </span></span><span>provides the commands to manage the </span><span>lifecycle of a project (from creation to deletion).</span></p>
````

<!--NOMAGIC_PAGE id=243970144 space=CM version=2 -->
## PAGE 00286: Opening Resource Usage Map

- page_id: `243970144`
- space_key: `CM`
- source_url: https://docs.nomagic.com/spaces/CM/pages/243970144/Opening+Resource+Usage+Map
- version_number: 2
- version_date: `2025-09-12T12:45:42.584+02:00`
- ancestors: Client-Side Collaborative Modeling Documentation > Using Teamwork Cloud
- labels: []

### NORMALIZED CONTENT

[CONFLUENCE_PAGE title='Resource Usage Map' space='MCS'] is a web application that comes with Teamwork. Resource Usage Map allows you to create graphical representations of Teamwork Cloud project usages, analyze dependencies among projects in the Teamwork Cloud repository, and identify potentially problematic usage areas.

You can open Resource Usage Map right from your modeling tool as described below.

To open Resource Usage Map

1. Open a server project.
2. In the main menu, select Collaborate > Open in Resource Usage Map .

After completing the steps above, the project usage map is opened in a web browser.

[IMAGE alt='' src='']

###### Example of a resource usage map.

If you work with a server that is of an earlier version than your modeling tool, you may need to specify the Web Application Platform URL for the Resource Usage Map functionality to work.

To specify Web Application Platform URL

1. In the main menu, select Options > Environment .
2. On the left side of the Environment Options dialog, select the Collaboration option group.
3. Specify the value of the Web Application Platform URL option.

**Related pages**

[CONFLUENCE_PAGE title='Resource Usage Map' space='MCS']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p><span style="color: rgb(62,63,64);"><ac:link><ri:page ri:space-key="MCS" ri:content-title="Resource Usage Map" /></ac:link> is a web application that comes with Teamwork. Resource Usage Map allows you to create graphical representations of Teamwork Cloud project usages, analyze dependencies among projects in the Teamwork Cloud repository, and identify potentially problematic usage areas.</span></p><p><span style="color: rgb(62,63,64);">You can open Resource Usage Map right from your modeling tool as described below.</span></p><p><br /></p><p>To open Resource Usage Map</p><hr /><ol><li>Open a server project.</li><li>In the main menu, select <strong>Collaborate</strong> &gt; <strong>Open in Resource Usage Map</strong>.</li></ol><p><br />After completing the steps above, the project usage map is opened in a web browser.</p><p><br /></p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="resource_usage_map.png" /></ac:image></p><h6 style="text-align: center;">Example of a resource usage map.</h6><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="3c83fcc2-332c-46c6-b7da-428a9fe5d686"><ac:rich-text-body><p>If you work with a server that is of an earlier version than your modeling tool, you may need to specify the Web Application Platform URL for the Resource Usage Map functionality to work.</p><p><br /></p><p>To specify Web Application Platform URL</p><hr /><ol><li>In the main menu, select <strong>Options</strong> &gt; <strong>Environment</strong>.</li><li>On the left side of the <strong>Environment Options</strong> dialog, select the <strong>Collaboration</strong> option group.</li><li>Specify the value of the <strong>Web Application Platform URL</strong> option.</li></ol></ac:rich-text-body></ac:structured-macro></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><strong>Related pages</strong></p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="61dac04b-ecc8-4531-95ec-0dc8e6f50965"><ac:parameter ac:name="page"><ac:link><ri:page ri:space-key="MCS" ri:content-title="Resource Usage Map" /></ac:link></ac:parameter></ac:structured-macro></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=243969751 space=CM version=4 -->
## PAGE 00287: Opening Teamwork Cloud projects

- page_id: `243969751`
- space_key: `CM`
- source_url: https://docs.nomagic.com/spaces/CM/pages/243969751/Opening+Teamwork+Cloud+projects
- version_number: 4
- version_date: `2025-12-08T16:06:13.149+01:00`
- ancestors: Client-Side Collaborative Modeling Documentation > Using Teamwork Cloud
- labels: []

### NORMALIZED CONTENT

The **Open Server Project** dialog is used for opening and managing projects from Teamwork Cloud.

To open the Open Server Project dialog

- From the Collaborate menu, select Open Server Project or Projects... .
- On the Collaboration toolbar, click the [ATTACHMENT filename='open_serverproject.png'] button.
- Press Ctrl+Shift+O.

[IMAGE alt='' src='']

###### The Open Server Project dialog.

In the dialog, do one of the following:

- Select a project and click **Open**. This does one of two things:
  1. 
    1. If an online project has an offline project version, the offline version opens to ensure a faster project load. This also ensures that you do not lose the changes that you made offline but have not yet committed.
    2. If you do not have an offline version saved, the project is opened from the server.
- Choose to Open Server Project (i.e. an online project from the server; ). Y ou can force open the online project , but, in this case, all changes made and not committed in the offline project will be lost.

Open project from serverTo open the project from the server

1. From the Collaborate menu, select Open Server Project or **Projects...**. .
2. In the new dialog, open the Online Projects tab.
3. Right-click the project you want to open.
4. From the shortcut menu, select **Open From Server**.
5. In the question dialog, click Yes . The server project will be opened shortly. [ATTACHMENT filename='message_to_open_project.png']

#### NOTE: Password-protected projects

Password-protected projects

- You may be prompted to enter a password if the selected project is [CONFLUENCE_PAGE title='Password-protected projects' space=''] .

- You can use the search bar to filter used projects by name.
- Currently, an open project is automatically selected in the **Open Server Project**dialog, making it easier to find it in the project list.

| Button | Description |
| --- | --- |
| Show empty categories | When selected, shows empty categories. Cancel the selection if you do not want empty categories to be displayed. |
| Version Properties | Opens the Version Properties dialog.In this dialog, you can see project information, such as comments, tags, modules, and meta information. You can find out the author, version number, and date including time zone.The button is available only when the project is selected.In the Tags tab, the Major version checkbox was added, to easily add tag Major. |
| Project History | Opens the History dialog.In this dialog, you can find the project change history. You can find out who made the changes, what and when has been changed. Also, you can open earlier versions of the project or even restore your project if any changes have corrupted your project.The button is available only when the project is selected. |
| Select Branches | Opens the Select Branch dialog.In this dialog, you can see if the project has branches. If the project has branches, you can select them. Furthermore, you can create and manage project branches.Click in a project line to select a particular project branch. |

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>The <strong>Open Server Project</strong> dialog is used for opening and managing projects from Teamwork Cloud.</p><p><br /></p><p>To open the Open Server Project dialog</p><hr /><ul><li>From the <strong>Collaborate</strong> menu, select <strong>Open Server Project </strong>or<strong> Projects...</strong>.</li><li>On the <strong>Collaboration</strong> toolbar, click the <ac:image><ri:attachment ri:filename="open_serverproject.png" /></ac:image> button.</li><li data-uuid="c1d651ed-d645-48c9-a70d-b376309f29cc">Press Ctrl+Shift+O.</li></ul><p><ac:image ac:align="center"><ri:attachment ri:filename="open_server_project.png" /></ac:image></p><h6 style="text-align: center;line-height: 1.66667;letter-spacing: normal;">The Open Server Project dialog.</h6><p>In the dialog, do one of the following:</p><ul><li><ac:inline-comment-marker ac:ref="91081e01-b0ea-4fda-a453-c5d84cbb95c6">Select a project and click </ac:inline-comment-marker><ac:inline-comment-marker ac:ref="91081e01-b0ea-4fda-a453-c5d84cbb95c6"><strong>Open</strong>. This does one of two things:</ac:inline-comment-marker><ol><li style="list-style-type: none;"><ol><li><span style="color:var(--ds-text,#172b4d);">If an online project has an offline project version, the offline version opens to<span> </span></span><span style="color:var(--ds-text,#172b4d);">ensure a faster project load.</span><span style="letter-spacing: 0.0px;"> This also ensures that you do not lose the changes that you made offline but have not yet committed.</span></li><li><span style="letter-spacing: 0.0px;"><span style="color:var(--ds-text,#172b4d);">If you do not have an offline version saved, the project is opened from the server.</span></span></li></ol></li></ol></li><li>Choose to <strong>Open Server Project </strong>(i.e. an online project from the server; <ac:link ac:anchor="Open project from server"><ac:plain-text-link-body><![CDATA[see full instructions below]]></ac:plain-text-link-body></ac:link>). Y<ac:inline-comment-marker ac:ref="d87fbac2-0c5a-4fef-b370-181427ed5c41">ou can force open the online project</ac:inline-comment-marker>, but, in this case, all changes made and not committed in the offline project will be lost. </li></ul><p><br /></p><p><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="14f980ec-4a72-438c-a44b-7dc9362a1d8a"><ac:parameter ac:name="">Open project from server</ac:parameter></ac:structured-macro>To open the project from the server</p><hr /><ol><li>From the <strong>Collaborate</strong> menu, select <strong>Open Server Project </strong><span style="color:var(--ds-text,#333333);">or</span><strong><strong> Projects...</strong><span style="color:var(--ds-text,#333333);">.</span></strong>.</li><li>In the new dialog, open the <strong>Online Projects</strong> tab. </li><li>Right-click the project you want to open.</li><li>From the <span style="color:var(--ds-text,#333333);">shortcut menu, select <strong>Open From Server</strong>. </span></li><li>In the question dialog, click <strong>Yes</strong>. The server project will be opened shortly.<br /><ac:image><ri:attachment ri:filename="message_to_open_project.png" /></ac:image></li></ol><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="0cc17b06-25d7-4322-ae04-4ef6fe174f5a"><ac:parameter ac:name="title">Password-protected projects</ac:parameter><ac:rich-text-body><ul><li>You may be prompted to enter a password if the selected project is <ac:link><ri:page ri:content-title="Password-protected projects" /><ac:plain-text-link-body><![CDATA[password-protected]]></ac:plain-text-link-body></ac:link>.</li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="3ef4e086-93c5-4c08-88ae-ed336fb357ea"><ac:rich-text-body><ul><li><span style="color:var(--ds-text,#000000);">You can use the search bar to filter used projects by name.</span></li><li><span style="color:var(--ds-text,#000000);">Currently, an open project is automatically selected in the <strong>Open Server Project </strong>dialog, making it easier to find it in the project list.<br class="_mce_tagged_br" /></span></li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p><table class="wrapped relative-table" style="width: 1091.33px;"><colgroup><col style="width: 141.354px;" /><col style="width: 949.312px;" /></colgroup><tbody><tr><th>Button</th><th>Description</th></tr><tr><td><div class="content-wrapper"><p><strong>Show empty categories</strong></p><p><strong><ac:image ac:title="Show empty categories" ac:alt="Show empty categories"><ri:attachment ri:filename="show_empty_categories.png" /></ac:image><br /></strong></p></div></td><td>When selected, shows empty categories. Cancel the selection if you do not want empty categories to be displayed.</td></tr><tr><td><div class="content-wrapper"><p><strong>Version Properties</strong></p><p><ac:image ac:title="Version Properties" ac:alt="Version Properties"><ri:attachment ri:filename="version_properties.png" /></ac:image></p></div></td><td><div class="content-wrapper"><p>Opens the <strong>Version Properties</strong> dialog.</p><p>In this dialog, you can see project information, such as comments, tags, modules, and meta information. You can find out the author, version number, and date including time zone.</p><p>The button is available only when the project is selected.</p><p>In the Tags tab, the <strong>Major version </strong>checkbox was <ac:inline-comment-marker ac:ref="3fbbf173-2464-41ac-be10-24083e01f8fd">added, to easily add tag <em>Major.</em></ac:inline-comment-marker></p><p><ac:image><ri:attachment ri:filename="Version_properties_Tags_tab.PNG" /></ac:image></p></div></td></tr><tr><td><div class="content-wrapper"><p><strong>Project History</strong></p><p><ac:image ac:title="Project History" ac:alt="Project History"><ri:attachment ri:filename="project_history.png" /></ac:image></p></div></td><td><p>Opens the <strong>History</strong> dialog.</p><p>In this dialog, you can find the project change history. You can find out who made the changes, what and when has been changed. Also, you can open earlier versions of the project or even restore your project if any changes have corrupted your project.</p><p>The button is available only when the project is selected.</p></td></tr><tr><td colspan="1"><div class="content-wrapper"><p><strong>Select Branches</strong></p><p><ac:image ac:title="Select Branches" ac:alt="Select Branches"><ri:attachment ri:filename="select_branches.png" /></ac:image></p></div></td><td colspan="1"><div class="content-wrapper"><p>Opens the <strong>Select Branch</strong> dialog.</p><p>In this dialog, you can see if the project has branches. If the project has branches, you can select them. Furthermore, you can create and manage project branches.</p><p>Click <ac:image ac:thumbnail="true" ac:height="22"><ri:attachment ri:filename="3dot_button.png"><ri:page ri:space-key="MT" ri:content-title="Project Properties dialog" /></ri:attachment></ac:image> in a project line to select a particular project branch.</p></div></td></tr></tbody></table><p class="auto-cursor-target"><br /></p>
````

<!--NOMAGIC_PAGE id=243969830 space=CM version=4 -->
## PAGE 00288: Package permissions

- page_id: `243969830`
- space_key: `CM`
- source_url: https://docs.nomagic.com/spaces/CM/pages/243969830/Package+permissions
- version_number: 4
- version_date: `2026-07-01T14:40:50.478+02:00`
- ancestors: Client-Side Collaborative Modeling Documentation > Using Teamwork Cloud
- labels: []

### NORMALIZED CONTENT

By default, all packages in the project can be reviewed and modified by any Teamwork Cloud user.

There are two levels of permissions:

- The Global permission specifies which permission is applied for all project packages for all users: Global permissions can be overridden by package permissions:Read-Only global permission can be overridden by a package with Read-Write permission. This allows the user/group to edit the package, whereas editing the rest of the model is restricted.Read-Write global permission can be overridden by a package with Read-Only permission. This restricts the user/group from editing the package, whereas editing the rest of the model is allowed.
  - Select Read-Write as the Global permission to allow editing of the entire model.
  - Select Read-Only as the Global permission to restrict editing of the entire model.
- **Package permissions** specify the permissions applied to a particular package for a particular user. If no permission is specified for the package, the global permission is valid.

If you want to restrict editing of a package for a specific user or user group, you can easily do this by [CONFLUENCE_PAGE title='Setting package permissions' space='']. You can modify package permissions if you have the [**Manage model permissions** permission](https://docs.nomagic.com/MCS/?contextKey=permissions&version=latest&variant=default) on that project. Select:

- Read-Only to restrict editing of the package for the selected user.
- Read-Write to allow editing of the package for the selected user.

By default, **Read-Write** as the **Global permission** is assigned to the project and the **Read-Only** permission is assigned to the package.

#### NOTE: Project-level and package-level permissions

Project-level and package-level permissions

The Teamwork Cloud project-level **Read-Write** permissions can be overridden by package permissions. For example, if a user was granted project-level **Read-Write**permissions, but was assigned **Read-Only** permissions for a particular package, that user will not be allowed to make changes to the elements owned by the package and the package itself.

If a user has project-level **Read-Only**permissions, package permissions cannot override them.

##### Permissions conflict logic

There are some cases when permissions for users or user group might be conflicting, these cases and the final outcome are described below:

1. If the user belongs to two groups and one group is granted Read-Only permission, while another group - Read-Write permission. In this permission conflict, the user will be granted with higher permission, which is Read-Write**permission.
2. User is granted different permissions through the Users and Groups tabs, if permissions are different, User permission wins.
3. If permission is granted simultaneously for both users and groups, then this permission will be granted for standalone users and for users within the selected groups.
4. In case of nested packages with each having different permissions (Read-Only/Read-Write), owned element modification mode is decided from the closest root package permissions in the tree.

**Related pages**

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p>By default, all packages in the project can be reviewed and modified by any Teamwork Cloud user.</p><p>There are two levels of permissions:</p><ul><li><ac:inline-comment-marker ac:ref="d4a15d37-3203-48e0-8d50-ce18ba56adbd">The</ac:inline-comment-marker><strong><ac:inline-comment-marker ac:ref="d4a15d37-3203-48e0-8d50-ce18ba56adbd"> Global permission</ac:inline-comment-marker></strong> specifies which permission is applied for all project packages for all users:<ul><li>Select <strong>Read-Write</strong> as the <strong>Global permission</strong> to allow editing of the entire model.</li><li>Select <strong>Read-Only</strong> as the <strong>Global permission</strong> to restrict editing of the entire model.</li></ul><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="afaaa1d8-38fb-48c1-836a-c5b1e355cf34"><ac:rich-text-body><p>Global permissions can be overridden by package permissions:</p><p>Read-Only global permission can be overridden by a package with Read-Write permission. This allows the user/group to edit the package, whereas editing the rest of the model is restricted.</p><p>Read-Write global permission can be overridden by a package with Read-Only permission. This restricts the user/group from editing the package, whereas editing the rest of the model is allowed.</p></ac:rich-text-body></ac:structured-macro></li><li><span style="line-height: 1.42857;"><strong>Package permissions</strong> specify the permissions applied to a particular package for a particular user. If no permission is specified for the package, the global permission is valid.<br /></span></li></ul><p>If you want to restrict editing of a package for a specific user or user group, you can easily do this by <ac:link><ri:page ri:content-title="Setting package permissions" /><ac:plain-text-link-body><![CDATA[modifying the package permissions]]></ac:plain-text-link-body></ac:link>. You can modify package permissions if you have the <a href="https://docs.nomagic.com/MCS/?contextKey=permissions&amp;version=latest&amp;variant=default"><strong>Manage model permissions</strong> permission</a> on that project. Select:</p><ul><li><strong>Read-Only</strong> to restrict editing of the package for the selected user.<strong><br /></strong></li><li><strong>Read-Write</strong> to allow editing of the package for the selected user.</li></ul><p>By default, <strong>Read-Write</strong> as the <strong>Global permission</strong> is assigned to the project and the <strong>Read-Only</strong> permission is assigned to the package.</p><p><br /></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="4cd33a02-0ead-4e97-9716-82f48fdc27b9"><ac:parameter ac:name="title">Project-level and package-level permissions</ac:parameter><ac:rich-text-body><p>The Teamwork Cloud project-level <strong>Read-Write</strong> permissions can be overridden by package permissions. For example, if a user was granted project-level <strong>Read-Write </strong>permissions, but was assigned <strong>Read-Only</strong> permissions for a particular package, that user will not be allowed to make changes to the elements owned by the package and the package itself. </p><p>If a user has project-level <strong>Read-Only </strong>permissions, package permissions cannot override them.</p></ac:rich-text-body></ac:structured-macro><h3><span style="color:var(--ds-text,#333333);">Permissions conflict logic</span></h3><p><span style="color:var(--ds-text,#333333);">There are some cases when permissions for users or user group might be conflicting, these cases and the final outcome are described below: </span></p><ol><li><span style="color:var(--ds-text,#333333);">If the user belongs to two groups and one group is granted Read-Only permission, while another group - Read-Write permission. In this permission conflict, the user will be granted with higher permission, which is Read-Write<em> </em>permission.</span></li><li><span style="color:var(--ds-text,#333333);">User is granted different permissions through the Users and Groups tabs, if permissions are different, User permission wins.</span></li><li><span style="color:var(--ds-text,#333333);">If permission is granted simultaneously for both users and groups, then this permission will be granted for standalone users and for users within the selected groups.</span></li><li><span style="color:var(--ds-text,#333333);">In case of nested packages with each having different permissions (Read-Only/Read-Write), owned element modification mode is decided from the closest root package permissions in the tree.</span></li></ol></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><strong>Related pages</strong></p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="8c78e8c3-386d-4403-be20-ada8fd84c0f2" /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=243969734 space=CM version=4 -->
## PAGE 00289: Password-protected projects

- page_id: `243969734`
- space_key: `CM`
- source_url: https://docs.nomagic.com/spaces/CM/pages/243969734/Password-protected+projects
- version_number: 4
- version_date: `2025-09-12T12:41:47.146+02:00`
- ancestors: Client-Side Collaborative Modeling Documentation > Using Teamwork Cloud > Managing server projects
- labels: []

### NORMALIZED CONTENT

- To set, update, and remove project password, you need the **Administer Resources**permission .
- The icon [IMAGE alt='' src=''] indicates password-protected projects.

You can protect your server projects with a password. The password covers all project versions, and can be set or removed by a project owner or a user having

You must be logged to a server to set a password for a particular project.

##### Setting project password

To set a password for a project

1. On the main menu, click Collaborate > Projects . The Manage Projects dialog opens.
2. In the Online project tab , select a project you want to protect by a password and do one of the following: You can use the search bar to faster filter used projects by name.
  - On the dialog toolbar, click the Set Password button.
  - Right-click the selected project and click Set Password . [ATTACHMENT filename='setting_password.png']
3. The Set Password dialog opens. [ATTACHMENT filename='Enter password.png'] Enter and confirm your password and click OK .

##### Updating project password

To update a password for Teamwork Cloud project

1. On the main menu, click Collaborate > Projects . The Manage Projects dialog opens.
2. In the Online project tab, select a password-protected project (indicated by [ATTACHMENT filename='indication_of_password_protected_project.PNG'] icon) and do one of the following:
  - On the dialog toolbar, click the Set Password button.
  - Right-click the selected project and click Set Password .
3. The Update Password dialog opens. [ATTACHMENT filename='update_password.png']

Enter your old password, then enter and confirm your new password and click **OK**.

##### Removing project password

To remove a password for Teamwork Cloud project

1. On the main menu, click Collaborate > Projects . The Manage Projects dialog opens.
2. In the Online project tab, select a password-protected project (indicated by [ATTACHMENT filename='indication_of_password_protected_project.PNG'] icon) and do one of the following:
  - On the dialog toolbar, click the Set Password button.
  - Right-click the selected project and click Set Password .
3. The Update Password dialog opens. Enter your old password and leave the **New Password**and **Confirm New Password**boxes empty . Click OK . Password is removed.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="c4b2b017-415c-4c8a-8979-0ef6309883e4"><ac:rich-text-body><ul><li>To set, update, and remove project password, you need the <a href="https://docs.nomagic.com/MCS/?contextKey=permissions&amp;version=latest&amp;variant=default"><strong style="letter-spacing: 0.0px;">Administer Resources</strong><span style="letter-spacing: 0.0px;"> </span>permission</a><span style="letter-spacing: 0.0px;">.</span></li><li><span style="letter-spacing: 0.0px;">The icon <ac:image ac:thumbnail="true" ac:height="12"><ri:attachment ri:filename="indication_of_password_protected_project.PNG" /></ac:image> indicates password-protected projects.</span></li></ul></ac:rich-text-body></ac:structured-macro><p><br /></p><p><span style="letter-spacing: 0.0px;">You can protect your server projects with a password. The password covers all project versions, and can be set or removed by a project owner or a user having </span></p><p>You must be logged to a server to set a password for a particular project.</p><h3>Setting project password</h3><p>To set a password for a project</p><hr /><ol><li>On the main menu, click <strong>Collaborate </strong>&gt; <strong>Projects</strong>. The <strong>Manage Projects</strong> dialog opens.</li><li>In the <strong>O<ac:inline-comment-marker ac:ref="e27231ec-d1d7-41e5-b3b7-5590567a4784">nline project </ac:inline-comment-marker></strong><ac:inline-comment-marker ac:ref="7ecffbb7-77c0-4752-865c-d9874240222e">tab</ac:inline-comment-marker>, select a project you want to protect by a password and do one of the following:<ul><li><ac:inline-comment-marker ac:ref="70686892-49df-4c33-bb8b-e523c6b0275c">On the dialog</ac:inline-comment-marker> toolbar, click the <strong>Set Password</strong> button.</li><li>Right-click the selected project and click <strong>Set Password</strong>.<br /><br /><ac:image><ri:attachment ri:filename="setting_password.png" /></ac:image></li></ul><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="e2474492-efba-4e80-a068-d3843bc29301"><ac:rich-text-body><p><span style="color:var(--ds-text,#000000);">You can use the search bar to faster filter used projects by name.<br /></span></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></li><li>The <strong>Set Password</strong> dialog opens.<br /><br /><ac:image ac:thumbnail="true" ac:height="160"><ri:attachment ri:filename="Enter password.png" /></ac:image><br /><br />Enter and confirm your password and click <strong>OK</strong>.</li></ol><h3 class="auto-cursor-target">Updating project password</h3><p class="auto-cursor-target"><span style="color:var(--ds-text,#000000);">To update a password for Teamwork Cloud project</span></p><hr /><ol><li class="auto-cursor-target"><span style="letter-spacing: 0.0px;">On the main menu, click </span><strong style="letter-spacing: 0.0px;">Collaborate </strong><span style="letter-spacing: 0.0px;">&gt; </span><strong style="letter-spacing: 0.0px;">Projects</strong><span style="letter-spacing: 0.0px;">. The </span><strong style="letter-spacing: 0.0px;">Manage Projects</strong><span style="letter-spacing: 0.0px;"> dialog opens.</span></li><li>In the <strong>Online project </strong>tab, select a password-protected project (indicated by <ac:image ac:thumbnail="true" ac:height="12"><ri:attachment ri:filename="indication_of_password_protected_project.PNG"><ri:page ri:space-key="MT" ri:content-title="Password-protected projects" /></ri:attachment></ac:image> icon) and do one of the following:<ul><li>On the dialog toolbar, click the <strong>Set Password</strong> button.</li><li>Right-click the selected project and click <strong>Set Password</strong>.</li></ul></li><li>The <strong>Update Password</strong> dialog opens.<br /><br /><ac:image ac:height="200"><ri:attachment ri:filename="update_password.png" /></ac:image></li></ol><p style="margin-left: 40.0px;">Enter your old password, then enter and confirm your new password and click <strong>OK</strong>.</p><h3 class="auto-cursor-target">Removing project password</h3><p class="auto-cursor-target"><span style="color:var(--ds-text,#000000);">To remove a password for Teamwork Cloud project</span></p><hr /><ol><li class="auto-cursor-target"><span>On the main menu, click </span><strong>Collaborate </strong><span>&gt; </span><strong>Projects</strong><span>. The </span><strong>Manage Projects</strong><span> dialog opens.</span></li><li>In the <strong>Online project </strong>tab, select a password-protected project (indicated by <ac:image ac:thumbnail="true" ac:height="12"><ri:attachment ri:filename="indication_of_password_protected_project.PNG" /></ac:image> icon) and do one of the following:<ul><li>On the dialog toolbar, click the <strong>Set Password</strong> button.</li><li>Right-click the selected project and click <strong>Set Password</strong>.</li></ul></li><li>The <strong>Update Password</strong> dialog opens. Enter your old password and <u>leave the <strong>New Password </strong>and <strong>Confirm New Password </strong>boxes empty</u>. Click <strong>OK</strong>. Password is removed.</li></ol>
````

<!--NOMAGIC_PAGE id=243970137 space=CM version=3 -->
## PAGE 00290: Pre-merge check

- page_id: `243970137`
- space_key: `CM`
- source_url: https://docs.nomagic.com/spaces/CM/pages/243970137/Pre-merge+check
- version_number: 3
- version_date: `2025-09-12T12:43:45.762+02:00`
- ancestors: Client-Side Collaborative Modeling Documentation > Using Teamwork Cloud > Model merge in Teamwork Cloud
- labels: []

### NORMALIZED CONTENT

Use the optional pre-merge check functionality to check permissions and prepare for branch merging.

How to perform the pre-merge check

1. Open the project that will be the [CONFLUENCE_PAGE title='Model Merge' space='MT'] .
2. Select Tools > Project Merge.
3. Select the project that will be the [CONFLUENCE_PAGE title='Model Merge' space='MT'] .
4. Click the Pre-merge check refresh icon: [ATTACHMENT filename='per_merge_check.png']

This checks if you can execute this merge, i.e., if you have sufficient permissions and a valid model structure.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p style="text-align: left;">Use the optional pre-merge check functionality to check permissions and prepare for branch merging.</p><p style="text-align: left;">How to perform the pre-merge check</p><hr /><ol><li>Open the project that will be the <ac:link ac:anchor="Target"><ri:page ri:space-key="MT" ri:content-title="Model Merge" /><ac:plain-text-link-body><![CDATA[target]]></ac:plain-text-link-body></ac:link><span style="color: rgb(0,0,0);">.</span></li><li>Select <strong>Tools &gt; Project Merge.</strong></li><li>Select the project that will be the <ac:link ac:anchor="Source"><ri:page ri:space-key="MT" ri:content-title="Model Merge" /><ac:plain-text-link-body><![CDATA[source]]></ac:plain-text-link-body></ac:link><span class="confluence-link">.</span></li><li>Click the <strong>Pre-merge check</strong> refresh icon:<br /><ac:image><ri:attachment ri:filename="per_merge_check.png" /></ac:image></li></ol><p style="text-align: left;">This checks if you can execute this merge, i.e., if you have sufficient permissions and a valid model structure.</p>
````

<!--NOMAGIC_PAGE id=243970356 space=CM version=2 -->
## PAGE 00291: Publishing Cameo Collaborator documents

- page_id: `243970356`
- space_key: `CM`
- source_url: https://docs.nomagic.com/spaces/CM/pages/243970356/Publishing+Cameo+Collaborator+documents
- version_number: 2
- version_date: `2025-08-25T12:52:41.064+02:00`
- ancestors: Client-Side Collaborative Modeling Documentation > Collaboration powered by 3DEXPERIENCE platform > Using Cameo Collaborator
- labels: []

### NORMALIZED CONTENT

Publishing Cameo Collaborator documents to the **3D**EXPERIENCE platformallows you to present them in a simplified form for users who do not know modeling languages, such as UML or SysML v1.

#### NOTE: Prerequisites

Prerequisites

- To publish Cameo Collaborator documents, [CONFLUENCE_PAGE title='Installing Cameo Collaborator Publisher plugin' space=''] in your modeling tool.
- Publishing is only supported on a cloud-hosted 3D EXPERIENCE platform.

To learn more, see:

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><span style="color:var(--ds-text,#333333);"><span style="color:var(--ds-text,#000000);">Publishing Cameo Collaborator documents to the <strong>3D</strong>EXPERIENCE platform </span><span style="color:var(--ds-text,#000000);">allows you to present them in a simplified form for users who do not know modeling languages, such as UML or SysML v1.</span><br /></span></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="dd518cb5-3be9-4ff7-9fc3-911d561a6cfb"><ac:parameter ac:name="title">Prerequisites</ac:parameter><ac:rich-text-body><ul><li>To publish Cameo Collaborator documents, <ac:link><ri:page ri:content-title="Installing Cameo Collaborator Publisher plugin" /><ac:plain-text-link-body><![CDATA[the Cameo Collaborator Publisher plugin must be installed]]></ac:plain-text-link-body></ac:link> in your modeling tool.</li><li>Publishing is only supported on a cloud-hosted <strong>3D</strong>EXPERIENCE platform.</li></ul></ac:rich-text-body></ac:structured-macro><p style="text-align: left;">To learn more, see:</p><p style="text-align: left;"><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="e88aa385-269f-42d4-b07e-a3fd167b9987" /></p>
````

<!--NOMAGIC_PAGE id=243970367 space=CM version=1 -->
## PAGE 00292: Publishing from command line

- page_id: `243970367`
- space_key: `CM`
- source_url: https://docs.nomagic.com/spaces/CM/pages/243970367/Publishing+from+command+line
- version_number: 1
- version_date: `2025-07-31T10:51:49.400+02:00`
- ancestors: Client-Side Collaborative Modeling Documentation > Collaboration powered by 3DEXPERIENCE platform > Using Cameo Collaborator > Publishing Cameo Collaborator documents
- labels: []

### NORMALIZED CONTENT

Publishing Cameo Collaborator documents is the simplest way to present models tostakeholders, sponsors, customers, and engineering teams. This chapter explains how to publish documents from the command line, which is useful if you want to publish them periodically, e.g., once a day or during non-business hours to save time.

#### NOTE: Prerequisites

Prerequisites

- [CONFLUENCE_PAGE title='Installing Cameo Collaborator Publisher plugin' space=''] .
- Cameo Collaborator works only with projects stored on a cloud-hosted 3D EXPERIENCE platform. If you want to publish a local model, first [CONFLUENCE_PAGE title='Adding projects to 3DEXPERIENCE platform' space='']add it to the **3D**EXPERIENCE platform .

#### TIP: Recommendations

Recommendations

- If you intend to publish a large model, increase the default JVM heap size of the Cameo Collaborator Publisher plugin as follows:
  1. Go to the *<modeling tool installationdirectory>/plugins/com.nomagic.collaborator.publisher*directory and open the *publish.properties* file.
  2. Increase the *-Xmx*value, e.g.,*-Xmx4000M*. It is recommended to set a larger heap size value than the one defined foryour modeling tool.
  3. Save and close the file.
- Depending on the size of the model you intend to publish, [CONFLUENCE_PAGE title='Memory allocation' space='MT'] to your modeling tool:
  - 2 million element model - 24 GB of RAM
  - 1 million element model - 15 GB of RAM
  - 500k element model - 7 GB of RAM

#### TIP: Publishing tips

Publishing tips

- To change the number of decimals displayed in Cameo Collaborator documents, in the main menu, go to Options > Project Options and specify the Decimal Places option. The setting is remembered and used for other documents published from the project.
- You can specify the diagram export options, such as dimensions and building time (the latter applies only to tables and matrices). To learn more, refer to [CONFLUENCE_PAGE title='Diagram image export' space='MT'] .

To publish a Cameo Collaborator document from the command line interface

1. Open the <modeling tool installation directory>/plugins/com.nomagic.collaborator.publisher/PowerBy_template .properties file.
2. Read the comments in the file and specify the publishing options.
3. Open the command line interface.
4. Go to the *<modeling tool installationdirectory>/plugins/com.nomagic.collaborator.publisher*directory containing the executive file for model publishing.
5. Execute the following command:
  - On Windows \plugins\com.nomagic.collaborator.publisher\PowerBy_template.properties]]>
  - On OS X or Linux /plugins/com.nomagic.collaborator.publisher/PowerBy_template.properties]]>

After completing the steps above, your model is published to Cameo Collaborator. If you want to publish the same model frequently, you do not need to do it manually every time. Instead, schedule publishing as a background task to save time.

##### Scheduling to publish a document

If you need to publish your models periodically and/or during non-business hours, you can schedule them to be published automatically. The following procedures describe the scheduling process on Windows and Linux operating systems.

To schedule a publishing task on Windows

1. Open the Task Scheduler from the Start menu of your Windows computer and select the option to create a basic task.
2. Type the task name, an optional description, and click Next .
3. Select how often you want the task to reoccur and click Next .
4. Specify when you want the task to start and click Next .
5. To schedule the publishing to start automatically, select the **Start a program** radio button and click **Next**.
6. Click the **Browse** button, go to the *<modeling tool installationdirectory>/plugins/com.nomagic.collaborator.publisher*directory, and open the *publish.exe* file.
7. In the **Add Arguments (optional)** box, type *properties=<modeling_tool_installation_directory>\plugins\com.nomagic.collaborator.publisher\template.properties* and click **Next**. 
 
[IMAGE alt='' src='']
8. Click Finish .

To schedule a publishing task on Linux

1. Connect to the remote server using SSH, or open the terminal directly.
2. Type the following command to open the *crontab*file with the default text editor: DJango
3. Using the Cron syntax create a cronjob to run the model publishing task once a day at midnight: DJango/plugins/com.nomagic.collaborator.publisher/publish.sh -properties PowerBy_template.properties]]>
4. Save the crontab file.

```text

```

After completing the steps described above, your model is published automatically on a regular basis at a specified time.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><span style="color: rgb(62,63,64);">Publishing Cameo Collaborator documents is the simplest way to present models to </span>stakeholders, sponsors, customers, and engineering teams. This chapter explains how to publish documents from the command line, which is useful if you want to publish them periodically, e.g., once a day or during non-business hours to save time.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="61942541-1e20-48ba-86a6-a6971994dce5"><ac:parameter ac:name="title">Prerequisites</ac:parameter><ac:rich-text-body><ul><li><ac:link><ri:page ri:content-title="Installing Cameo Collaborator Publisher plugin" /><ac:plain-text-link-body><![CDATA[The Cameo Collaborator Publisher plugin must be installed in your modeling tool]]></ac:plain-text-link-body></ac:link>.</li><li>Cameo Collaborator works only with projects stored on a cloud-hosted <strong>3D</strong>EXPERIENCE platform. If you want to publish a local model, first <ac:link><ri:page ri:content-title="Adding projects to 3DEXPERIENCE platform" /><ac:link-body>add it to the <strong>3D</strong>EXPERIENCE platform</ac:link-body></ac:link>.</li></ul></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="174b72be-2c84-421a-87ac-d4a5e8905adf"><ac:parameter ac:name="title">Recommendations</ac:parameter><ac:rich-text-body><ul><li>If you intend to publish a large model, increase the default JVM heap size of the Cameo Collaborator Publisher plugin as follows:<ol><li><p>Go to the <em><span style="color: rgb(0,0,0);">&lt;modeling tool installa</span><span style="color: rgb(0,0,0);">tion</span><span style="color: rgb(0,0,0);"> directory&gt;/plugins/com.nomagic.collaborator.publisher </span></em>directory and open the <em>publish.properties</em> file.</p></li><li><p>Increase the <em>-Xmx</em><span style="color: rgb(0,0,0);"> value, e.g., </span><em>-Xmx4000M</em>. It is recommended to set a larger <span style="color: rgb(0,0,0);">heap size value than the one defined for</span><span style="color: rgb(0,0,0);"> your modeling tool.</span></p></li><li><p>Save and close the file.</p></li></ol></li><li>Depending on the size of the model you intend to publish, <ac:link><ri:page ri:space-key="MT" ri:content-title="Memory allocation" /><ac:plain-text-link-body><![CDATA[allocate a sufficient amount of memory]]></ac:plain-text-link-body></ac:link> to your modeling tool:<ul><li><p>2 million element model - 24 GB of RAM</p></li><li><p>1 million element model - 15 GB of RAM</p></li><li><p>500k element model - 7 GB of RAM</p></li></ul></li></ul></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="dd769109-cbb1-4d6f-9581-3a50ef4eb4f8"><ac:parameter ac:name="title">Publishing tips</ac:parameter><ac:rich-text-body><ul><li>To change the number of decimals displayed in Cameo Collaborator documents, in the main menu, go to <strong>Options</strong> &gt; <strong>Project Options</strong> and specify the <strong>Decimal Places</strong> option. The setting is remembered and used for other documents published from the project.</li><li>You can specify the diagram export options, such as dimensions and building time (the latter applies only to tables and matrices). To learn more, refer to <ac:link><ri:page ri:space-key="MT" ri:content-title="Diagram image export" /></ac:link>.</li></ul></ac:rich-text-body></ac:structured-macro><p><br /></p><p>To publish a Cameo Collaborator document from the command line interface</p><hr /><ol><li>Open the <em>&lt;modeling tool installation directory&gt;/plugins/com.nomagic.collaborator.publisher/PowerBy_template</em><em>.properties</em> file.</li><li><p class="auto-cursor-target">Read the comments in the file and specify the publishing options.</p></li><li>Open the command line interface.</li><li><p>Go to the <em><span style="color: rgb(0,0,0);">&lt;modeling tool installa</span><span style="color: rgb(0,0,0);">tion </span><span style="color: rgb(0,0,0);">directory&gt;/plugins/com.nomagic.collaborator.publisher </span></em>directory containing the executive file for model publishing.</p></li><li><p>Execute the following command:</p><ul><li><p>On Windows</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="16283a09-a9e5-419d-b702-1102e6505938"><ac:plain-text-body><![CDATA[publish.exe properties=<modeling_tool_installation_directory>\plugins\com.nomagic.collaborator.publisher\PowerBy_template.properties]]></ac:plain-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></li><li><p class="auto-cursor-target">On OS X or Linux</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="ceab7baa-ff77-457d-a86a-ae6f4adf8ffe"><ac:plain-text-body><![CDATA[./publish properties=<modeling_tool_installation_directory>/plugins/com.nomagic.collaborator.publisher/PowerBy_template.properties]]></ac:plain-text-body></ac:structured-macro></li></ul></li></ol><p><span style="color: rgb(51,51,51);"><br />After completing the steps above, yo</span>ur model is published to Cameo Collaborator. If you want to publish the same model frequently, you do not need to do it manually every time. Instead, schedule publishing as a background task to save time.</p><h3>Scheduling to publish a document</h3><p>If you need to publish your models periodically and/or during non-business hours, you can schedule them to be published automatically. The following procedures describe the scheduling process on Windows and Linux operating systems.<br /> </p><p>To schedule a publishing task on Windows</p><hr /><ol><li>Open the <strong>Task Scheduler</strong> from the<strong> Start</strong> menu of your Windows computer and select the option to create a basic task.</li><li>Type the task name, an optional description, and click <strong>Next</strong>.</li><li>Select how often you want the task to reoccur and click <strong>Next</strong>.</li><li>Specify when you want the task to start and click <strong>Next</strong>.</li><li><p>To schedule the publishing to start automatically, select the <strong>Start a program</strong> radio button and click <strong>Next</strong>.</p></li><li><p>Click the <strong>Browse</strong> button, go to the <em><span style="color: rgb(0,0,0);">&lt;modeling tool installa</span><span style="color: rgb(0,0,0);">tion </span><span style="color: rgb(0,0,0);">directory&gt;/plugins/com.nomagic.collaborator.publisher </span></em>directory, and open the <em>publish.exe</em> file.</p></li><li><p>In the <strong>Add Arguments (optional)</strong> box, type <em><span style="color: rgb(23,43,77);">properties=&lt;modeling_tool_installation_directory&gt;\plugins\com.nomagic.collaborator.publisher\template.properties</span></em> and click <strong>Next</strong>.<br /><br /><ac:image><ri:attachment ri:filename="basic_task_creation_wizard.png" /></ac:image><br /><br /></p></li><li>Click <strong>Finish</strong>.</li></ol><p><br /></p><p>To schedule a publishing task on Linux</p><hr /><ol><li>Connect to the remote server using SSH, or open the terminal directly.</li><li><p>Type the following command to open the <em>crontab </em>file with the default text editor:</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="76b83299-bcf9-4b5c-9085-3013fe2b64b8"><ac:parameter ac:name="theme">DJango</ac:parameter><ac:plain-text-body><![CDATA[# crontab -e]]></ac:plain-text-body></ac:structured-macro></li><li>Using the Cron syntax create a <em>cronjob</em> to run the model publishing task once a day at midnight:<br /><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="8df24ec5-7b0f-43a9-b3a0-4fca8a01f01d"><ac:parameter ac:name="theme">DJango</ac:parameter><ac:plain-text-body><![CDATA[0 0 * * * <modeling tool installation directory>/plugins/com.nomagic.collaborator.publisher/publish.sh -properties PowerBy_template.properties]]></ac:plain-text-body></ac:structured-macro></li><li>Save the <em>crontab</em> file.</li></ol><pre><br /></pre><p><br />After completing the steps described above, your model is published automatically on a regular basis at a specified time.</p>
````

<!--NOMAGIC_PAGE id=243970357 space=CM version=1 -->
## PAGE 00293: Publishing from graphical user interface

- page_id: `243970357`
- space_key: `CM`
- source_url: https://docs.nomagic.com/spaces/CM/pages/243970357/Publishing+from+graphical+user+interface
- version_number: 1
- version_date: `2025-07-31T10:51:49.113+02:00`
- ancestors: Client-Side Collaborative Modeling Documentation > Collaboration powered by 3DEXPERIENCE platform > Using Cameo Collaborator > Publishing Cameo Collaborator documents
- labels: []

### NORMALIZED CONTENT

Publishing documents from the graphical user interface is the simplest way to present models tostakeholders, sponsors, customers, and engineering teams.

#### NOTE: Prerequisites

Prerequisites

- [CONFLUENCE_PAGE title='Installing Cameo Collaborator Publisher plugin' space=''] .
- You can publish Cameo Collaborator documents only on a cloud-hosted**3D**EXPERIENCE platform. Make sure youselect the relevant check box when logging in. 
 
[IMAGE alt='' src='']
- If you want to publish a local model, first [CONFLUENCE_PAGE title='Adding projects to 3DEXPERIENCE platform' space='']add it to the **3D**EXPERIENCE platform .

#### TIP: Recommendations

Recommendations

- If you intend to publish a large model, increase the default JVM heap size of the Cameo Collaborator Publisher plugin as follows:
  1. Open the *<modeling_tool_installation_directory>/bin/**<modeling_tool_name>.properties* file.
  2. Increase the *-Xmx*value, e.g.,*-Xmx4000M*.
  3. Save and close the file.
- Depending on the size of the model you intend to publish, [CONFLUENCE_PAGE title='Memory allocation' space='MT'] to your modeling tool:
  - 2 million element model - 24 GB of RAM
  - 1 million element model - 15 GB of RAM
  - 500k element model - 7 GB of RAM

#### TIP: Publishing tips

Publishing tips

- To change the number of decimals displayed in Cameo Collaborator documents, in the main menu, go to **Options** > **Project Options** and specify the Decimal Places option. The setting is remembered and used for other documents published from the project.
- You can specify the diagram export options, such as dimensions and building time (the latter applies only to tables and matrices). To learn more, refer to [CONFLUENCE_PAGE title='Diagram image export' space='MT'] .

To publish a Cameo Collaborator document

1. [CONFLUENCE_PAGE title='Logging in to 3DEXPERIENCE platform' space=''] and [CONFLUENCE_PAGE title='Opening projects from 3DEXPERIENCE platform' space=''] you want to publish.
2. [CONFLUENCE_PAGE title='Using a server project in 3DEXPERIENCE platform' space=''] if you have not already done so. If document templates are not listed in the **Use Server Project** dialog, add the **-Desi.allow.usage.all.types=true** property to the *<modeling_tool_installation_directory>/bin/**<modeling_tool_name>.properties* file and restart the modeling tool.
3. [CONFLUENCE_PAGE title='Committing changes to 3DEXPERIENCE platform' space=''] .
4. In the main menu, select Tools > Cameo Collaborator > Publish .
5. In the Cameo Collaborator Publisher dialog, specify the publishing options:
  - In the Document box, enter the document name.
  - Click [ATTACHMENT filename='select_button2.png'] next to the Scope box and select one or several Packages containing the data you want to publish.
  - Click the Template drop-down box and select the document template you want to use for publishing.
  - If you want to update a previously published document, click the Options button and select the Update previously published document check box. [ATTACHMENT filename='cameo_collaborator_publisher.png']
6. Click the **Publish** button.
7. Wait until you get the message that the document is successfully published.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><span style="color: rgb(62,63,64);">Publishing documents from the graphical user interface is the simplest way to present models to </span>stakeholders, sponsors, customers, and engineering teams.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="61942541-1e20-48ba-86a6-a6971994dce5"><ac:parameter ac:name="title">Prerequisites</ac:parameter><ac:rich-text-body><ul><li><ac:link><ri:page ri:content-title="Installing Cameo Collaborator Publisher plugin" /><ac:plain-text-link-body><![CDATA[The Cameo Collaborator Publisher plugin must be installed in your modeling tool]]></ac:plain-text-link-body></ac:link>.</li><li><span style="color: rgb(23,43,77);"><span style="color: rgb(51,51,51);">You can publish Cameo Collaborator documents only on a cloud-hosted<span> </span></span><strong style="text-align: left;">3D</strong><span style="color: rgb(51,51,51);">EXPERIENCE platform. Make sure you<span> </span></span>select the relevant check box when logging in.<br /><br /><ac:image><ri:attachment ri:filename="platform_login_dialog.png" /></ac:image><br /><br /></span></li><li>If you want to publish a local model, first <ac:link><ri:page ri:content-title="Adding projects to 3DEXPERIENCE platform" /><ac:link-body>add it to the <strong>3D</strong>EXPERIENCE platform</ac:link-body></ac:link>.</li></ul></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="174b72be-2c84-421a-87ac-d4a5e8905adf"><ac:parameter ac:name="title">Recommendations</ac:parameter><ac:rich-text-body><ul><li>If you intend to publish a large model, increase the default JVM heap size of the Cameo Collaborator Publisher plugin as follows:<ol><li><p>Open the <em><span style="color: rgb(0,0,0);">&lt;modeling_tool_installa</span><span style="color: rgb(0,0,0);">tion_</span><span style="color: rgb(0,0,0);">directory&gt;/bin/</span></em><em>&lt;modeling_tool_name&gt;.properties</em> file.</p></li><li><p>Increase the <em>-Xmx</em><span style="color: rgb(0,0,0);"> value, e.g., </span><em>-Xmx4000M</em>.</p></li><li><p>Save and close the file.</p></li></ol></li><li>Depending on the size of the model you intend to publish, <ac:link><ri:page ri:space-key="MT" ri:content-title="Memory allocation" /><ac:plain-text-link-body><![CDATA[allocate a sufficient amount of memory]]></ac:plain-text-link-body></ac:link> to your modeling tool:<ul><li><p>2 million element model - 24 GB of RAM</p></li><li><p>1 million element model - 15 GB of RAM</p></li><li><p>500k element model - 7 GB of RAM</p></li></ul></li></ul></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="fb8c52e5-ffb0-485e-bec1-a6c3149cbf73"><ac:parameter ac:name="title">Publishing tips</ac:parameter><ac:rich-text-body><ul><li><span>To change the number of decimals displayed in Cameo Collaborator documents, in the main menu, go to <strong>Options</strong> &gt; <strong>Project Options</strong> and specify the </span><strong>Decimal Places</strong><span> option. The setting is remembered and used for other documents published from the project.</span></li><li>You can specify the diagram export options, such as dimensions and building time (the latter applies only to tables and matrices). To learn more, refer to <ac:link><ri:page ri:space-key="MT" ri:content-title="Diagram image export" /></ac:link>.</li></ul></ac:rich-text-body></ac:structured-macro><p><br /></p><p>To publish a Cameo Collaborator document</p><hr /><ol><li><p class="auto-cursor-target"><ac:link><ri:page ri:content-title="Logging in to 3DEXPERIENCE platform" /><ac:plain-text-link-body><![CDATA[Log in to the 3DEXPERIENCE platform]]></ac:plain-text-link-body></ac:link> and <ac:link><ri:page ri:content-title="Opening projects from 3DEXPERIENCE platform" /><ac:plain-text-link-body><![CDATA[open the server project]]></ac:plain-text-link-body></ac:link> you want to publish.</p></li><li><ac:link><ri:page ri:content-title="Using a server project in 3DEXPERIENCE platform" /><ac:plain-text-link-body><![CDATA[Use the document template you want to utilize for publishing in the model]]></ac:plain-text-link-body></ac:link> if you have not already done so.<br /><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="77dd927b-d6bb-46fd-810d-6b94b24c500c"><ac:rich-text-body><p>If document templates are not listed in the <strong>Use Server Project</strong> dialog, add the <span style="color: rgb(23,43,77);"><strong>-Desi.allow.usage.all.types=true</strong> property to the <em><span style="color: rgb(0,0,0);">&lt;modeling_tool_installa</span><span style="color: rgb(0,0,0);">tion_</span><span style="color: rgb(0,0,0);">directory&gt;/bin/</span></em><em>&lt;modeling_tool_name&gt;.properties</em> file and restart the modeling tool.</span></p></ac:rich-text-body></ac:structured-macro></li><li><ac:link><ri:page ri:content-title="Committing changes to 3DEXPERIENCE platform" /><ac:plain-text-link-body><![CDATA[Commit project changes to the server]]></ac:plain-text-link-body></ac:link>.</li><li>In the main menu, select <strong>Tools</strong> &gt; <strong>Cameo Collaborator</strong> &gt; <strong>Publish</strong>.</li><li>In the <strong>Cameo Collaborator Publisher</strong> dialog, specify the publishing options:<ul><li>In the <strong>Document</strong> box, enter the document name.</li><li>Click <ac:image ac:thumbnail="true" ac:height="18"><ri:attachment ri:filename="select_button2.png" /></ac:image> next to the <strong>Scope</strong> box and select one or several Packages containing the data you want to publish.</li><li>Click the <strong>Template</strong> drop-down box and select the document template you want to use for publishing.</li><li>If you want to update a previously published document, click the <strong>Options</strong> button and select the <strong>Update previously published document</strong> check box.<br /><br /><ac:image><ri:attachment ri:filename="cameo_collaborator_publisher.png" /></ac:image><br /><br /></li></ul></li><li><p>Click the <strong>Publish</strong> button.</p></li><li><p>Wait until you get the message that the document is successfully published.</p></li></ol>
````

<!--NOMAGIC_PAGE id=243969744 space=CM version=2 -->
## PAGE 00294: Removing projects

- page_id: `243969744`
- space_key: `CM`
- source_url: https://docs.nomagic.com/spaces/CM/pages/243969744/Removing+projects
- version_number: 2
- version_date: `2025-09-12T12:45:41.046+02:00`
- ancestors: Client-Side Collaborative Modeling Documentation > Using Teamwork Cloud > Managing server projects
- labels: []

### NORMALIZED CONTENT

To remove a project

1. From the main menu, select Collaborate > Projects . The Manage Projects dialog opens.
2. Select the project you want to remove.
3. Click **Remove**. 
 
[IMAGE alt='' src='']

4. In the dialog that opens, select **Yes**. The project will be removed from Teamwork Cloud.

Data Manager

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>To remove a project</p><hr /><ol><li>From the main menu, select <strong>Collaborate </strong>&gt; <strong>Projects</strong>. The<span> </span><strong>Manage Projects </strong>dialog opens.</li><li>Select the project you want to remove.</li><li><p>Click <strong>Remove</strong>. <br /><br /><ac:image><ri:attachment ri:filename="removing_project.png" /></ac:image></p></li></ol><p><span style="letter-spacing: 0.0px;">       4. In the dialog that opens, select </span> <span style="letter-spacing: 0.0px;"> </span> <strong style="letter-spacing: 0.0px;">Yes</strong><span style="letter-spacing: 0.0px;">. </span> <span style="letter-spacing: 0.0px;"> </span> <span style="letter-spacing: 0.0px;"> </span> <span style="letter-spacing: 0.0px;"> </span> <span style="letter-spacing: 0.0px;">The project will be removed from Teamwork Cloud.</span></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="a32fe1f2-e685-4ab7-96ba-8155e9178b41"><ac:rich-text-body>Removed projects are not deleted from the Teamwork Cloud database. To permanently delete resources from the database, use the <a href="https://docs.nomagic.com/display/MCS/Data+Manager">Data Manager</a> tool.</ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p>
````

<!--NOMAGIC_PAGE id=243970271 space=CM version=2 -->
## PAGE 00295: Removing server project usages in 3DEXPERIENCE platform

- page_id: `243970271`
- space_key: `CM`
- source_url: https://docs.nomagic.com/spaces/CM/pages/243970271/Removing+server+project+usages+in+3DEXPERIENCE+platform
- version_number: 2
- version_date: `2025-09-12T12:42:30.091+02:00`
- ancestors: Client-Side Collaborative Modeling Documentation > Collaboration powered by 3DEXPERIENCE platform > Managing project usages in 3DEXPERIENCE platform
- labels: []

### NORMALIZED CONTENT

If you no longer need to use a project, you can easily remove the usage from the main project. Project usages are removed with all references to the elements stored in the used project.

To remove a project usage

1. [CONFLUENCE_PAGE title='Locking model for edit' space='MT'] you want to stop using.
2. In the main menu, click Collaborate > Project Usages > Project Usages .
3. In the **Project Usages** dialog, do one of the following:
  - Select a used project, click [IMAGE alt='' src=''], and select **Remove with References**.
  - Right-click a used project and select Remove > Remove with References . [ATTACHMENT filename='removing_project_usages.png']
4. In the question dialog, click Yes to confirm that you want to remove the used project.
5. When the used project is removed, click OK to close the Project Usages dialog.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>If you no longer need to use a project, you can easily remove the usage from the main project. Project usages are removed with <span style="letter-spacing: 0.0px;">all references to the elements stored in the used project.</span></p><p><br /></p><p>To remove a project usage</p><hr /><ol><li><ac:link><ri:page ri:space-key="MT" ri:content-title="Locking model for edit" /><ac:plain-text-link-body><![CDATA[Lock the used project]]></ac:plain-text-link-body></ac:link> you want to stop using.</li><li>In the main menu, click <strong> Collaborate</strong> &gt; <strong>Project Usages</strong> &gt; <strong>Project Usages</strong>.</li><li><p class="auto-cursor-target">In the <strong>Project Usages</strong> dialog, do one of the following:</p><ul><li><p class="auto-cursor-target">Select a used project, click <ac:image ac:thumbnail="true" ac:height="17"><ri:attachment ri:filename="remove_button.png"><ri:page ri:space-key="MT" ri:content-title="_buttons" /></ri:attachment></ac:image>, and select <strong>Remove with References</strong>.</p></li><li>Right-click a used project and select <strong>Remove</strong> &gt; <strong>Remove with References</strong>.<br /><br /><ac:image><ri:attachment ri:filename="removing_project_usages.png" /></ac:image><br /><br /></li></ul></li><li>In the question dialog, click <strong>Yes</strong> to confirm that you want to remove the used project.</li><li>When the used project is removed, click <strong>OK</strong> to close the <strong>Project Usages</strong> dialog.</li></ol>
````

<!--NOMAGIC_PAGE id=243969741 space=CM version=1 -->
## PAGE 00296: Renaming projects

- page_id: `243969741`
- space_key: `CM`
- source_url: https://docs.nomagic.com/spaces/CM/pages/243969741/Renaming+projects
- version_number: 1
- version_date: `2025-07-31T10:51:36.579+02:00`
- ancestors: Client-Side Collaborative Modeling Documentation > Using Teamwork Cloud > Managing server projects
- labels: []

### NORMALIZED CONTENT

To rename a project

1. From the main menu, select Collaborate > Projects . The Manage Projects dialog opens.
2. Select the project you want to rename.
3. Click Rename .
4. In the dialog that opens, type a new name for the project in the **Name:** field: [ATTACHMENT filename='renaming_project.png']

5. In this dialog, you can also change the project category by clicking the three dots menu [IMAGE alt='' src=''] and selecting the desired category.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>To rename a project</p><hr /><ol><li>From the main menu, select<span> </span> <strong>Collaborate</strong> <span> </span>&gt;<span> </span> <strong>Projects</strong>. The<span> </span> <strong>Manage Projects</strong> <span> </span>dialog opens.</li><li>Select the project you want to rename.</li><li>Click <strong>Rename</strong>.</li><li><p class="auto-cursor-target">In the dialog that opens, type a new name for the project in the <strong>Name:</strong> field:</p><ac:image><ri:attachment ri:filename="renaming_project.png" /></ac:image></li></ol><p>       5. In this dialog, you can also change the project category by clicking the three dots menu <ac:image ac:thumbnail="true" ac:height="16"><ri:attachment ri:filename="3_dots.png" /></ac:image> and selecting the desired category.</p>
````

<!--NOMAGIC_PAGE id=243970066 space=CM version=2 -->
## PAGE 00297: Representation of Teamwork Cloud users

- page_id: `243970066`
- space_key: `CM`
- source_url: https://docs.nomagic.com/spaces/CM/pages/243970066/Representation+of+Teamwork+Cloud+users
- version_number: 2
- version_date: `2025-09-11T15:25:53.830+02:00`
- ancestors: Client-Side Collaborative Modeling Documentation > Using Teamwork Cloud
- labels: []

### NORMALIZED CONTENT

You need to have the [**List All Users** permission](https://docs.nomagic.com/MCS/?contextKey=permissions&version=latest&variant=default) assigned to change the user representation.

You can customize how users are represented when, for example, they lock model elements by changing the value of the**Representation of Users**environment option.

[IMAGE alt='' src='']

###### Changing the user representation in the Teamwork Cloud project.

A *User Name* is shown by default in the following cases:

- the corresponding fields (e.g., Full name) are not filled in the Web Application Platform.
- the List All Users permission is not assigned to the user.

To choose how to represent users

1. In the main menu, click Options > Environment .
2. In the panel on the left, select Collaboration .
3. Under General , click Representation of Users . [ATTACHMENT filename='representation_of_users_environment_option.png']
4. Select to represent users by displaying one of the following:
  - User Name
  - Full Name
  - Email
5. When you are done, click OK .
6. Reload an open server project.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="warning" ac:schema-version="1" ac:macro-id="d54b005c-9d28-482b-b1b5-610b7d06084f"><ac:rich-text-body><p>You need to have the <a href="https://docs.nomagic.com/MCS/?contextKey=permissions&amp;version=latest&amp;variant=default"><strong>List All Users</strong> permission</a> assigned to change the user representation.</p></ac:rich-text-body></ac:structured-macro><p>You can <ac:inline-comment-marker ac:ref="727d6f66-a4ae-4f97-b8bd-c2f0c8e06225">customize</ac:inline-comment-marker> how users are represented when, <ac:inline-comment-marker ac:ref="e147007c-5efc-458d-a703-8e4a286136ed">for example, they lock model elements by changing the value of the </ac:inline-comment-marker><strong><ac:inline-comment-marker ac:ref="e147007c-5efc-458d-a703-8e4a286136ed">Representation of Users</ac:inline-comment-marker></strong><ac:inline-comment-marker ac:ref="e147007c-5efc-458d-a703-8e4a286136ed"> environment option.</ac:inline-comment-marker></p><p><ac:image ac:align="center"><ri:attachment ri:filename="representation_of_users.png" /></ac:image></p><h6 style="text-align: center;">Changing the user representation in the Teamwork Cloud project.</h6><p>A <em>User Name</em> is shown by default in the following cases:</p><ul><li>the corresponding fields (e.g., Full name) are not filled in the Web Application Platform. </li><li>the <strong>List All Users</strong> permission is not assigned to the user.<br /><br /></li></ul><p>To choose how to represent users </p><hr /><ol><li>In the main menu, click <strong>Options</strong> &gt; <strong>Environment</strong>.</li><li>In the panel on the left, select <strong>Collaboration</strong>.</li><li>Under <strong>General</strong>, click <strong>Representation of Users</strong>.<br /><ac:image><ri:attachment ri:filename="representation_of_users_environment_option.png" /></ac:image></li><li>Select to represent users by displaying one of the following:<ul><li>User Name </li><li>Full Name</li><li>Email</li></ul></li><li>When you are done, click <strong>OK</strong>.</li><li><ac:inline-comment-marker ac:ref="3e47549c-9a73-4665-9f16-79a42f4344d8">Reload an open server project.</ac:inline-comment-marker> </li></ol>
````

<!--NOMAGIC_PAGE id=243970139 space=CM version=1 -->
## PAGE 00298: Returning to Merge dialog

- page_id: `243970139`
- space_key: `CM`
- source_url: https://docs.nomagic.com/spaces/CM/pages/243970139/Returning+to+Merge+dialog
- version_number: 1
- version_date: `2025-07-31T10:51:44.692+02:00`
- ancestors: Client-Side Collaborative Modeling Documentation > Using Teamwork Cloud > Model merge in Teamwork Cloud
- labels: []

### NORMALIZED CONTENT

You can return to the previously performed merge operation if you notice that you have accepted or rejected the changes, e.g., rejected the element creation, by mistake and need to change your merge decisions.

Returning to the **Merge** dialog is only possible if you have not committed the changes to the server or reloaded the server project yet.

Also, you need to discard the changes you have already introduced to the project before you can return to the **Merge** dialog.

[IMAGE alt='' src='']

To return to the Merge dialog

- Click Return to Merge in the notification window that appears after clicking Finish Merging in the Merged Result panel. [ATTACHMENT filename='model_successfully_merged.png']

Alternatively, you can return to the **Merge** dialog by performing the merge operation again. This works only if the project has not been reloaded or committed to the server yet.

To initiate the merge operation

1. Do one of the following:
  - In the main menu, go to Collaborate > Merge From . [ATTACHMENT filename='collaborate_merge_from.png']

- 
  - In the main menu, go to Tools > Project Merge . [ATTACHMENT filename='tools_project_merge.png']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="auto-cursor-target">You can return to the previously performed merge operation if you notice that you have accepted or rejected the changes, e.g., rejected the element creation, by mistake and need to change your merge decisions.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="e4a65075-8897-4973-b77d-b2caf4cdac41"><ac:rich-text-body><p>Returning to the <strong>Merge</strong> dialog is only possible if you have not committed the changes to the server or reloaded the server project yet.</p><p>Also, you need to discard the changes you have already introduced to the project before you can return to the <strong>Merge</strong> dialog.</p><p><ac:image><ri:attachment ri:filename="discard_changes_to_return_to_merge_dialog.png" /></ac:image></p></ac:rich-text-body></ac:structured-macro><p><br /></p><p>To return to the Merge dialog</p><hr /><ul><li><span style="letter-spacing: 0.0px;">Click </span><strong style="letter-spacing: 0.0px;">Return to Merge</strong><span style="letter-spacing: 0.0px;"> in the notification window that appears after clicking </span><strong style="letter-spacing: 0.0px;">Finish Merging</strong><span style="letter-spacing: 0.0px;"> in the </span><strong style="letter-spacing: 0.0px;">Merged Result</strong><span style="letter-spacing: 0.0px;"> panel.</span><br /><ac:image><ri:attachment ri:filename="model_successfully_merged.png" /></ac:image><br /><br /></li></ul><p>Alternatively, you can return to the <strong>Merge</strong> dialog by performing the merge operation again. This works only if the project has not been reloaded or committed to the server yet.</p><p>To initiate the merge operation</p><hr /><ol><li>Do one of the following:<ul><li>In the main menu, go to<strong> Collaborate</strong> &gt;<strong> Merge From</strong>.<br /><ac:image><ri:attachment ri:filename="collaborate_merge_from.png" /></ac:image></li></ul></li></ol><ul><li style="list-style-type: none;background-image: none;"><ul><li>In the main menu, go to <strong>Tools</strong> &gt; <strong>Project Merge</strong>. <br /><ac:image><ri:attachment ri:filename="tools_project_merge.png" /></ac:image></li></ul></li></ul>
````

<!--NOMAGIC_PAGE id=243969855 space=CM version=1 -->
## PAGE 00299: Reviewing conflicting changes

- page_id: `243969855`
- space_key: `CM`
- source_url: https://docs.nomagic.com/spaces/CM/pages/243969855/Reviewing+conflicting+changes
- version_number: 1
- version_date: `2025-07-31T10:51:38.816+02:00`
- ancestors: Client-Side Collaborative Modeling Documentation > Using Teamwork Cloud > Using lock-free editing mode
- labels: []

### NORMALIZED CONTENT

#### CONTENT-LAYER: Example #2

1866845014

#### CONTENT-COLUMN: Example #2

1866845026

1866845012

**On this page**

**33**

#### CONTENT-BLOCK: Example #2

1866845016

Even though users usually work on different parts of the model, situations when they start editing the same model elements and, as a result, conflicting changes are detected may occur. In such a case, you will be asked to review these conflicts in the**Conflicting Changes** panel and then take certain action, for instance, confirm the update result or discard the local changes.

#### TIP: Example #1

Example #1

*User 1 and User 2 are working on the same model version: #24. The model contains Class A.*

*User 1 deletes Class A from the model and commits the project to the server. The model version #25 is created.*

*User 2 renames Class A to Class B and commits/updates the project to the server. The conflicting changes occur.*

#### TIP: Example #2

Example #2

*User 1 and User 2 are working on the same model version: #24. The model contains Class A.*

*User 1 renames Class A to Class B and commits the project to the server. The model version #25 is created.*

*User 2 renames Class A to Class C and commits the project to the server. The conflicting changes occur.*

##### Conflicting Changes panel

To open the panel

1. In the main menu, click Window .
2. Select Conflicting Changes from the drop-down menu. The Conflicting Changes panel opens. [ATTACHMENT filename='conflicting_changes_panel.png'] The Conflicting Changes panel.

Alternatively, you can open it by clicking the **Review Conflicts**button directly on the warning that appears when conflicting changes are detected.

[IMAGE alt='' src='']

###### The Conflicting Changes warning.

Please note that the possible occurrence of conflicting changes is being checked upon the project update or a commit that requires an update.

##### Composition of the Conflicting Changes panel

The **Conflicting Changes** panel consists of three smaller panels that provide different pieces of information to the user:

- Conflicting Local Changes : shows locally modified elements whose changes conflict with the changes already committed to the server.
- Upcoming Changes : shows the upcoming changes that c onflict with the selected local change.
- Preview Update Result : informs about the changes tha t will be applied after the project update.

[IMAGE alt='' src='']

###### Conflicting Changes panels that inform users about the changes that conflict in the project.

##### Symbols used in the Conflicting Changes panel

| Icon | Description |
| --- | --- |
|  | Checks the presence of the conflicting changes in the model. |
|  | Selects the previous conflicting change on the list. |
|  | Selects the next conflicting change on the list. |
|  | Expands elements in the Conflicting Local Changes panel. |
|  | Collapses elements in the Conflicting Local changes panel. |
|  | Confirms the update result affecting the selected element. |
|  | Confirms all update results of the conflicting changes at once. |
|  | Filters confirmed/unconfirmed conflicting changes. |
|  | Shows that the conflicting change has been confirmed by the user. |

##### Resolving conflicting changesResolving conflicting changes

**Confirming update results**

Once you have reviewed the conflicting changes, you can confirm the update result that will be appliedafter the project update. It should be emphasized that remote deletions always take precedence over the local changes.

To confirm the update result

1. In the Conflicting Changes panel, do one of the following:
  - select the specific conflicting element and click [ATTACHMENT filename='confirm.png'] in the toolbar at the top.
  - click [ATTACHMENT filename='confirm_all_update_results.png'] in the toolbar to confirm all conflicting changes at once.
  - right-click the conflicting element and select Confirm Update Result in the shortcut menu. The acknowledged change is marked with a green tick [ATTACHMENT filename='green_tick.png'] . [ATTACHMENT filename='confirming_update_result.png']

###### Confirming the conflicting changes via the shortcut menu.

There is another group of actions you can perform to handle the detected conflicting changes:

- Select in Containment Tree : click to select the element in Containment tree.
- Quick Diff : select to inspect the conflicting changes in a compact form.
- Full Diff : select to inspect the conflicting changes in a detailed form.
- Compare Projects : select to compare the modified projects.
- Discard Changes : select to discard the local changes.

Please note that the discarded changes cannot be undone.

Depending on the action you have performed prior to the detection of conflicting changes in your model, you will see either the **Commit** or the **Update** button in the **Conflicting Changes** panel after confirming the conflicting changes in your project.

[IMAGE alt='' src='']

###### Update or Commit button in the Conflicting Changes panel.

1875700929

**Related pages**

- [CONFLUENCE_PAGE title='Reviewing element history and inspecting changes' space='']
- [CONFLUENCE_PAGE title='Change Sets' space='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="b57928ec-c8e1-400e-be2b-32afd038dea2"><ac:parameter ac:name="id">1866845014</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="98fb5e86-003b-4a61-8b6c-d1fbf7825404"><ac:parameter ac:name="id">1866845026</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="01346cce-bd7a-4ec2-bedc-1414712aa0b9"><ac:parameter ac:name="id">1866845012</ac:parameter><ac:rich-text-body><p><strong>On this page</strong></p><p><strong><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="700dd3ec-eb66-4717-a923-cd5c228c578f"><ac:parameter ac:name="maxLevel">3</ac:parameter><ac:parameter ac:name="minLevel">3</ac:parameter></ac:structured-macro><br /></strong></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="000a36de-4bd8-49f7-84ae-9bd9f5958103"><ac:parameter ac:name="id">1866845016</ac:parameter><ac:rich-text-body><p>Even though users usually work on different parts of the model, situations when they start editing the same model elements and, as a result, conflicting changes are detected may occur. In such a case, you will be asked to review these conflicts in the<strong style="letter-spacing: 0.0px;"> Conflicting Changes</strong> panel and then take certain action, for instance, <ac:inline-comment-marker ac:ref="cba6988a-7872-4b76-adc1-15e38127cf92">confirm the update result or discard the local changes.</ac:inline-comment-marker></p><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="53ba45fe-db2b-4e03-8b59-21f919bcd807"><ac:parameter ac:name="title">Example #1</ac:parameter><ac:rich-text-body><p style="margin-left: 0.0in;"><em><span style="color: rgb(62,63,64);">User 1 and User 2 are working on the same model version: #24. The model contains Class A.</span></em></p><p style="margin-left: 0.0in;"><em><span style="color: rgb(62,63,64);">User 1 deletes Class A from the model and commits the project to the server. The model version #25 is created.</span></em></p><p style="margin-left: 0.0in;"><em><span style="color: rgb(62,63,64);">User 2 renames Class A to Class B and commits/updates the project to the server. The conflicting changes occur.</span></em></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="3750b2a9-b602-4880-ae5c-7d8ace07ea34"><ac:parameter ac:name="title">Example #2</ac:parameter><ac:rich-text-body><p style="margin-left: 0.0in;"><em><span style="color: rgb(62,63,64);">User 1 and User 2 are working on the same model version: #24. The model contains Class A.</span></em></p><p style="margin-left: 0.0in;"><em><span style="color: rgb(62,63,64);">User 1 renames Class A to Class B and commits the project to the server. The model version #25 is created.</span></em></p><p style="margin-left: 0.0in;"><em><span style="color: rgb(62,63,64);">User 2 renames Class A to Class C and commits the project to the server. The conflicting changes occur.</span></em></p></ac:rich-text-body></ac:structured-macro><h3 class="auto-cursor-target">Conflicting Changes panel</h3><p>To open the panel</p><hr /><ol><li>In the main menu, click <strong>Window</strong>.</li><li style="text-align: left;">Select <strong>Conflicting Changes</strong> from the drop-down menu. The <strong>Conflicting Changes</strong> panel opens.<br /><br /><ac:image ac:align="center"><ri:attachment ri:filename="conflicting_changes_panel.png" /></ac:image><h6 style="text-align: center;">The Conflicting Changes panel.</h6></li></ol><p>Alternatively, you can open it by clicking the <strong>Review Conflicts </strong>button directly <ac:inline-comment-marker ac:ref="85dd7eb7-2717-45cf-8d48-96ce0d5c405d">on the warning that appears when conflicting changes are detected.</ac:inline-comment-marker> </p><p><ac:image ac:align="center"><ri:attachment ri:filename="review_conflicts_dialog.png" /></ac:image></p><h6 style="text-align: center;">The Conflicting Changes warning.</h6><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="8375b7f6-33d7-4cc8-ad88-9d7a70e2bee1"><ac:rich-text-body><p>Please note that the possible occurrence of conflicting changes is being checked upon the project update <span style="color: rgb(62,63,64);">or a commit that requires an update.</span></p></ac:rich-text-body></ac:structured-macro><h3>Composition of the Conflicting Changes panel</h3><p>The <strong>Conflicting Changes</strong> panel consists of three smaller panels that provide different pieces of information to the user: </p><ul><li><strong>Conflicting Local Changes</strong>: shows locally modified elements whose changes conflict with the changes already committed to the server. </li><li><strong>Upcoming Changes</strong>: shows the upcoming changes that c<ac:inline-comment-marker ac:ref="b5f6ed0e-2033-4605-bcd4-4bc67e07f22e">onflict with the selected local change.</ac:inline-comment-marker> </li><li><strong>Preview Update Result</strong>: informs about the changes tha<ac:inline-comment-marker ac:ref="a2c2ea3b-039e-4138-acf6-30b65c880301">t will be applied after the project update.</ac:inline-comment-marker> </li></ul><p><ac:image ac:align="center"><ri:attachment ri:filename="preview_conflicting_changes.png" /></ac:image></p><h6 style="text-align: center;">Conflicting Changes panels that inform users about the changes that conflict in the project.</h6><h3>Symbols used in the Conflicting Changes panel</h3><table class="wrapped relative-table" style="width: 35.2715%;"><colgroup><col style="width: 7.78816%;" /><col style="width: 92.2118%;" /></colgroup><tbody><tr><th>Icon</th><th>Description</th></tr><tr><td><div class="content-wrapper"><p><ac:image><ri:attachment ri:filename="refresh_buttonpng.png" /></ac:image></p></div></td><td>Checks the presence of the conflicting changes in the model.</td></tr><tr><td><div class="content-wrapper"><p><ac:image><ri:attachment ri:filename="moving_up.png" /></ac:image></p></div></td><td>Selects the previous conflicting change on the list.</td></tr><tr><td><div class="content-wrapper"><p><ac:image><ri:attachment ri:filename="moving_down.png" /></ac:image></p></div></td><td>Selects the next conflicting change on the list.</td></tr><tr><td><div class="content-wrapper"><p><ac:image><ri:attachment ri:filename="expand_all.png" /></ac:image></p></div></td><td><ac:inline-comment-marker ac:ref="ed6f5822-dbae-4879-93ef-a29032315cc9">Expands</ac:inline-comment-marker> elements in the <strong>Conflicting</strong> <strong><ac:inline-comment-marker ac:ref="05f1e36f-bb17-4562-9c73-6930f970a8c2"><ac:inline-comment-marker ac:ref="f82b96ee-51ed-46f7-837b-6159e79b8b83">Local Changes</ac:inline-comment-marker></ac:inline-comment-marker></strong> <ac:inline-comment-marker ac:ref="1531460a-4b8c-488f-8a38-424d1cc82e5b">panel.</ac:inline-comment-marker></td></tr><tr><td colspan="1"><div class="content-wrapper"><p><ac:image><ri:attachment ri:filename="collapse_all.png" /></ac:image></p></div></td><td colspan="1">Collapses elements in the <strong>Conflicting <ac:inline-comment-marker ac:ref="e82e3de2-d80e-4ae3-acdd-3dbad88f9e39">Local changes</ac:inline-comment-marker></strong> panel.</td></tr><tr><td colspan="1"><div class="content-wrapper"><p><ac:image><ri:attachment ri:filename="confirm.png" /></ac:image></p></div></td><td colspan="1"><ac:inline-comment-marker ac:ref="d113a533-3149-4f1b-9eda-42e716ecc14b"><ac:inline-comment-marker ac:ref="0246411d-e4a6-475b-aaf3-c6fe7d274127">Confirms the update result</ac:inline-comment-marker> affecting the selected element.</ac:inline-comment-marker></td></tr><tr><td colspan="1"><div class="content-wrapper"><p><ac:image><ri:attachment ri:filename="confirm_all_update_results.png" /></ac:image></p></div></td><td colspan="1"><ac:inline-comment-marker ac:ref="d8b76525-61c7-4d13-b1be-d54f5e58ef85"><ac:inline-comment-marker ac:ref="bd7d6ae7-8977-47c0-af2a-f3dabc75e981">Confirms all update results</ac:inline-comment-marker> of the conflicting changes at once.</ac:inline-comment-marker></td></tr><tr><td colspan="1"><div class="content-wrapper"><p><ac:image><ri:attachment ri:filename="filter_icon.png" /></ac:image></p></div></td><td colspan="1"><div class="content-wrapper"><p>Filters confirmed/unconfirmed conflicting changes.</p><p><ac:image><ri:attachment ri:filename="filtering.png" /></ac:image></p></div></td></tr><tr><td colspan="1"><div class="content-wrapper"><p><ac:image><ri:attachment ri:filename="green_tick.png" /></ac:image></p></div></td><td colspan="1"><div class="content-wrapper"><p>Shows that the conflicting change has been confirmed by the user.</p><p><ac:image><ri:attachment ri:filename="confirmed_change_symbol.png" /></ac:image></p></div></td></tr></tbody></table><p><br /></p><h3><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="921ca35d-3665-490d-90d7-fba543635af8"><ac:parameter ac:name="">Resolving conflicting changes</ac:parameter></ac:structured-macro>Resolving conflicting changes</h3><p><strong>Confirming update results</strong></p><p><ac:inline-comment-marker ac:ref="72835d65-4dd1-4d8f-acec-918228c7133d">Once</ac:inline-comment-marker> you have reviewed the conflicting changes, <ac:inline-comment-marker ac:ref="6171d08e-f65f-4279-9744-072b9e8da18f">you can confirm <ac:inline-comment-marker ac:ref="ddaf69d2-6aed-443d-9062-b2de0d80d707">the update result that will be applied </ac:inline-comment-marker></ac:inline-comment-marker>after the project update. It should be emphasized that remote <ac:inline-comment-marker ac:ref="cdd25caf-bbb9-4325-b041-490d89a81311">deletions</ac:inline-comment-marker> always take precedence over the local changes. </p><p>To confirm the update result</p><hr /><ol><li>In the <strong>Conflicting Changes</strong> panel, do one of the following:<ul><li>select the specific conflicting element and click <ac:image><ri:attachment ri:filename="confirm.png" /></ac:image> in the toolbar at the top.</li><li>click <ac:image><ri:attachment ri:filename="confirm_all_update_results.png" /></ac:image> in the toolbar to confirm <ac:inline-comment-marker ac:ref="9a303e5c-df13-4729-8b43-0ca97e7a46c2">all conflicting changes</ac:inline-comment-marker> at once.</li><li>right-click the conflicting element and select <strong>Confirm Update Result </strong>in the shortcut menu.<br />The <ac:inline-comment-marker ac:ref="8a968258-2f6c-434b-b3c2-65a0a5fba4ea">acknowledged change is </ac:inline-comment-marker>marked with a green tick<ac:image><ri:attachment ri:filename="green_tick.png" /></ac:image>.<br /><ac:image ac:align="center"><ri:attachment ri:filename="confirming_update_result.png" /></ac:image></li></ul></li></ol><h6 style="text-align: center;">Confirming the conflicting changes via the shortcut menu.</h6><p>There is another group of actions you can perform to handle the detected conflicting changes:</p><ul><li><strong><ac:inline-comment-marker ac:ref="36bfaaf5-2ae5-4734-8501-c00f42310ec5">Select in Containment Tree</ac:inline-comment-marker></strong><ac:inline-comment-marker ac:ref="36bfaaf5-2ae5-4734-8501-c00f42310ec5">: click to select the element in Containment tree.</ac:inline-comment-marker></li><li><strong><ac:inline-comment-marker ac:ref="36bfaaf5-2ae5-4734-8501-c00f42310ec5">Quick Diff</ac:inline-comment-marker></strong><ac:inline-comment-marker ac:ref="36bfaaf5-2ae5-4734-8501-c00f42310ec5">: select to inspect the conflicting changes in a compact form.</ac:inline-comment-marker></li><li><strong><ac:inline-comment-marker ac:ref="36bfaaf5-2ae5-4734-8501-c00f42310ec5">Full Diff</ac:inline-comment-marker></strong><ac:inline-comment-marker ac:ref="36bfaaf5-2ae5-4734-8501-c00f42310ec5">: select to inspect the conflicting changes in a detailed form.</ac:inline-comment-marker></li><li><strong><ac:inline-comment-marker ac:ref="36bfaaf5-2ae5-4734-8501-c00f42310ec5">Compare Projects</ac:inline-comment-marker></strong><ac:inline-comment-marker ac:ref="36bfaaf5-2ae5-4734-8501-c00f42310ec5">: select to compare the modified projects.</ac:inline-comment-marker></li><li><strong><ac:inline-comment-marker ac:ref="36bfaaf5-2ae5-4734-8501-c00f42310ec5">Discard Changes</ac:inline-comment-marker></strong><ac:inline-comment-marker ac:ref="36bfaaf5-2ae5-4734-8501-c00f42310ec5">: select to discard the local changes.</ac:inline-comment-marker></li></ul><ac:structured-macro ac:name="warning" ac:schema-version="1" ac:macro-id="0a7dbecd-ccf3-4b0c-a051-86a08e39231a"><ac:rich-text-body><p>Please note that the discarded changes cannot be undone.</p></ac:rich-text-body></ac:structured-macro><p><br /></p><p>Depending on the action you have performed prior to the detection of conflicting changes in your model, you will see either the <strong>Commit</strong> or the <strong>Update</strong> button in the <strong>Conflicting Changes</strong> panel after confirming the conflicting changes in your project. </p><p><ac:image ac:align="center"><ri:attachment ri:filename="conflicting_changes_buttons.png" /></ac:image></p><h6 style="text-align: center;"><span style="color: rgb(94,108,132);">Update or Commit button in the Conflicting Changes panel.</span></h6><p /><p><br /></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="32e03022-2fe5-400e-ab81-22410c0e0bda"><ac:parameter ac:name="id">1875700929</ac:parameter><ac:rich-text-body><p><strong>Related pages</strong></p><ul><li><ac:link><ri:page ri:content-title="Reviewing element history and inspecting changes" /></ac:link><strong><br class="_mce_tagged_br" /></strong></li><li><ac:link><ri:page ri:content-title="Change Sets" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=243969964 space=CM version=3 -->
## PAGE 00300: Reviewing content history

- page_id: `243969964`
- space_key: `CM`
- source_url: https://docs.nomagic.com/spaces/CM/pages/243969964/Reviewing+content+history
- version_number: 3
- version_date: `2025-09-11T08:38:12.799+02:00`
- ancestors: Client-Side Collaborative Modeling Documentation > Using Teamwork Cloud > Reviewing project history
- labels: ['scope-history', 'history']

### NORMALIZED CONTENT

You can view changes in the model in a particular scope at the element level; that is, a selected package or a classifier element (a composed element). The ability to see the history of a selected [CONFLUENCE_PAGE title='Block' space='MED'], [CONFLUENCE_PAGE title='Requirement' space='MED'], or another composed element is a big benefit for system engineers.

[IMAGE alt='' src='']

###### History of element changes in the scope of a *Book*package.

In the history review panel, you can see various details about the changes between selected versions, such as the list of elements that was changed, when changes were made, and who made changes. Different colors describe if a particular model element is added, deleted or modified. You can also export the content history of changes to a report in a *docx* format.

To view the changes of a particular project scope

1. Select a composed element in the [CONFLUENCE_PAGE title='Containment tab' space='MT'] or diagram pane and right click it.
2. From the shortcut menu, select Content History . The history review panel opens, where you can analyze changes between selected server project versions.
3. To see differences between server project versions:
  - Double click the project version to see differences between the selected version and the earlier one.
  - Select the list of versions and click the [ATTACHMENT filename='display_changes.png'] button.

#### INFO: Stopping collecting changes

Stopping collecting changes

If retrieving the content history takes too much time, you can click the **Stop**button to complete reviewing changes through versions of the selected composed element.

[IMAGE alt='' src='']

To display version properties

1. Open the Content History panel as described above.
2. Select the project version.
3. In the panel's toolbar, click the [ATTACHMENT filename='4.png'] button or right-click the selected version and select the Version Properties command.

The button is disabled if either no version or multiple versions are selected.

To generate the content history report

1. Open the Content History panel.
2. On the Content History toolbar, click the Generate Report button. [ATTACHMENT filename='generate_report_toolbar_button.png']
3. The Save As dialog opens to specify the location of a report file.

To generate a project Comparison report (Differences report)

1. Open the Content History panel.
2. In the project versions comparison area, click the Generate Report button. [ATTACHMENT filename='changes_between_versions_generate_report.png']
3. The Save As dialog opens to specify the location of a report file.

In a Differences report you can find project scope and element scope:

- Project scope – name, version, the number of elements and diagrams in the compared project versions.
- Element scope – name, path and element type of the particular model element that was chosen as a content history scope .

This Differences report compared to the [CONFLUENCE_PAGE title='Reviewing element history and inspecting changes' space='']report only includes changes from the chosen model element scope and not the entire model. These changes are included inthe sections **Diagram Differences**, **Model Differences**,and**Changes by Type**of the report.

**Related pages**

- [CONFLUENCE_PAGE title='Analyzing comparison results' space='MT']
- [CONFLUENCE_PAGE title='Reviewing project history' space='']
- [CONFLUENCE_PAGE title='Reviewing historical versions of the project' space='']
- [CONFLUENCE_PAGE title='Reviewing element history and inspecting changes' space='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p>You can view changes in the model in a particular scope at the element level; that is, a selected package or a classifier element (a composed element). The ability to see the history of a selected <ac:link><ri:page ri:space-key="MED" ri:content-title="Block" /></ac:link>, <ac:link><ri:page ri:space-key="MED" ri:content-title="Requirement" /></ac:link>, or another composed element is a big benefit for system engineers.</p><p><ac:image ac:align="center"><ri:attachment ri:filename="Content_history.png" /></ac:image></p><h6 style="text-align: center;">History of element changes in the scope of a <em>Book </em>package.</h6><p>In the history review panel, you can see various details about the changes between selected versions, such as the list of elements that was changed, when changes were made, and who made changes. Different colors describe if a particular model element is added, deleted or modified. You can also export the content history of changes to a report in a <em>docx</em> format.</p><p><br /></p><p>To view the changes of a particular project scope</p><hr /><ol><li data-uuid="42382f8e-820c-431d-92ca-e565f4c33f3a">Select a composed element in the <ac:link><ri:page ri:space-key="MT" ri:content-title="Containment tab" /><ac:plain-text-link-body><![CDATA[Containment tree]]></ac:plain-text-link-body></ac:link> or diagram pane and right click it.</li><li data-uuid="ba43f206-be1b-4ca9-b827-fb7f990496c3">From the shortcut menu, select <strong>Content History</strong>. The history review panel opens, where you can analyze changes between selected server project versions. </li><li data-uuid="dfb61afb-34d0-4a85-84d0-0f826fdaf329">To see differences between server project versions:<ul><li>Double click the project version to see differences between the selected version and the earlier one.</li><li>Select the list of versions and click the <ac:image ac:thumbnail="true" ac:height="16"><ri:attachment ri:filename="display_changes.png" /></ac:image> button.</li></ul></li></ol><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="ef837b2e-9e13-49de-9bd8-7160a060cb6e"><ac:parameter ac:name="title">Stopping collecting changes</ac:parameter><ac:rich-text-body><p>If retrieving the content history takes too much time, you can click the <strong>Stop </strong>button to complete reviewing changes through versions of the selected composed element.</p><p><ac:image><ri:attachment ri:filename="collecting_changes_in_versions.png" /></ac:image></p></ac:rich-text-body></ac:structured-macro><p><br /></p><p>To display version properties</p><hr /><ol><li data-uuid="8b7b7f08-dc3c-403f-95b3-647ea4774a82">Open the <strong>Content History</strong> panel as described above.</li><li data-uuid="71993407-d54e-41f6-8bc9-ea88115d0480">Select the project version.</li><li data-uuid="992b00b0-3666-4030-a0ff-b0d123771bdc">In the panel's toolbar, click the<ac:image ac:thumbnail="true" ac:width="23"><ri:attachment ri:filename="4.png" /></ac:image> button or right-click the selected version and select the <strong>Version Properties</strong> command.</li></ol><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="4c6c8b71-38db-4909-9433-ad73eff8b1ce"><ac:rich-text-body><p>The button is disabled if either no version or multiple versions are selected.</p></ac:rich-text-body></ac:structured-macro><p><br /></p><p>To generate the content history report</p><hr /><ol><li data-uuid="28fcf19d-22ff-4146-8d9b-1bbc53449fed">Open the <strong>Content History</strong> panel.</li><li data-uuid="94f734aa-d02e-4194-831e-acdbdb43f28d">On the Content History toolbar, click the<strong> </strong>Generate Report button.<br /><ac:image><ri:attachment ri:filename="generate_report_toolbar_button.png" /></ac:image></li><li data-uuid="3bef6d3c-9107-4ca5-84c6-407ea4204f11">The <strong>Save As </strong>dialog opens to specify the location of a report file.</li></ol><p><br /></p><p>To generate a project Comparison report (Differences report)</p><hr /><ol><li data-uuid="d652e2b5-d9b4-4e1e-b10e-2bf2019ee98e">Open the <strong>Content History</strong> panel.</li><li data-uuid="b788542e-0714-4b5f-93b4-3cda5eae7cf5">In the project versions comparison area, click the Generate Report button.<br /><ac:image><ri:attachment ri:filename="changes_between_versions_generate_report.png" /></ac:image></li><li data-uuid="330ab663-0773-4df5-8552-593b408bb4cf">The <strong>Save As </strong>dialog opens to specify the location of a report file.</li></ol><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="d8c5edff-5fd7-4813-90d9-24873d249c2e"><ac:rich-text-body><p><span style="color:var(--ds-text,#000000);">In a Differences report you can find project scope and element scope</span><span style="color:var(--ds-text,#000000);">:</span></p><ul><li data-uuid="c38b9672-105c-43c9-9a43-049c55b012ed">Project scope – name, version, the number of elements and diagrams in the compared project versions.</li><li data-uuid="7b7c1729-16d6-4cea-a48f-73a49e6b305b">Element scope – <span style="color:var(--ds-text,#333333);">name, path and element type of the particular model element that was chosen as a content history scope</span>.</li></ul><p><span style="color:var(--ds-text,#333333);">This Differences report compared to the <ac:link><ri:page ri:content-title="Reviewing element history and inspecting changes" /><ac:plain-text-link-body><![CDATA[Full Diff ]]></ac:plain-text-link-body></ac:link>report <span style="color:var(--ds-text,#333333);">only includes changes from the chosen model element scope and not the entire model. These changes are included in<span style="color:var(--ds-text,#333333);"> the sections <strong>Diagram Differences</strong>, <strong>Model Differences</strong>, </span>and<strong> Changes by Type </strong>of the report</span>.</span></p></ac:rich-text-body></ac:structured-macro></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><strong>Related pages</strong></p><ul><li data-uuid="81e2374e-4893-437d-86d6-2280accccc4a"><ac:link><ri:page ri:space-key="MT" ri:content-title="Analyzing comparison results" /></ac:link></li><li data-uuid="92950f2f-dd52-4b10-83a6-9c9401d4ca53"><ac:link><ri:page ri:content-title="Reviewing project history" /></ac:link></li><li data-uuid="8f2d072f-7e9c-465c-8f49-5a8a9683dccf"><ac:link><ri:page ri:content-title="Reviewing historical versions of the project" /></ac:link></li><li data-uuid="da254fb9-2a1e-48ca-89f8-b0e8e4575b5c"><ac:link><ri:page ri:content-title="Reviewing element history and inspecting changes" /></ac:link></li></ul></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=243969939 space=CM version=2 -->
## PAGE 00301: Reviewing element history and inspecting changes

- page_id: `243969939`
- space_key: `CM`
- source_url: https://docs.nomagic.com/spaces/CM/pages/243969939/Reviewing+element+history+and+inspecting+changes
- version_number: 2
- version_date: `2025-09-11T15:18:04.486+02:00`
- ancestors: Client-Side Collaborative Modeling Documentation > Using Teamwork Cloud > Reviewing project history
- labels: ['differences', 'element-diff', 'diagram_diff', 'element-differences', 'diagram_diffrerences']

### NORMALIZED CONTENT

##### Displaying element history

To display the history of an element, do one of the following

- Right-click the element or its symbol. From the shortcut menu, select History . [ATTACHMENT filename='image2018-3-16_11-33-0.png']
- Select the element or its symbol and press Ctrl + H.
- Open the [CONFLUENCE_PAGE title='Specification window' space='MT'] of the element and click the History button [ATTACHMENT filename='history_in_spec.png'] .
- If it is a diagram, right-click an empty space on the diagram pane. From the shortcut menu, select History .

#### INFO: Stopping collecting changes

Stopping collecting changes

If retrieving the element history takes too much time, you can click the **Stop**button to complete reviewing changes through different versions of the selected element.

[IMAGE alt='' src='']

The **History** panel of the selected element then opens at the bottom of the client application window. If you select an element in a used project, the corresponding panel title is **Usage History**. The highlighted row indicates current changes that are not yet committed. To refresh the list of versions, click the [IMAGE alt='' src=''] button in the panel's toolbar or perform the same actions as for opening the panel.

[IMAGE alt='' src='']

###### A list of project versions in the History panel.

You can compare any two versions of an element to see the differences between them.

To display element version properties

1. Open the element's History panel as described above.
2. Select the project version.
3. In the panel's toolbar, click the [ATTACHMENT filename='4.png'] button or right-click the selected version and select the Version Properties command.

The button is disabled if either no version or multiple versions are selected.

To display the history of an element in a used project

1. Open the element's Usage History panel as described above.
2. Select the project version.
3. In the panel's toolbar, click the [ATTACHMENT filename='display_changes.png'] button or right-click the selected version and select the Show History in Used Project command.

##### Comparing element versionsComparing element versions

To compare project versions in the Teamwork Cloud environment, you are required to have the [**Read Resources**permission](https://docs.nomagic.com/MCS/?contextKey=permissions&version=latest&variant=default) for every used project in compared versions.

To compare element versions

1. Hold down Ctrl and select the versions you want to compare. You can only compare two versions. Please note that if you select more than two items, only two (the latest and the earliest versions) will be compared. If you want to compare subsequent versions, you only need to select the later one.
2. On the panel's toolbar, click the [ATTACHMENT filename='quick_diff_button.png'] button or right-click the selection and choose either: [IMAGE alt='' src=''] You can also choose the same commands from the toolbar of the **History** panel.
  - quickdiffQuick Diff – to inspect changes of element property values (such as documentation, type, or multiplicity) in a compact form .
  - Full Diff – to inspect changes of diagrams or element property values in a detailed form, as well as look at the properties of new relationships and directly related elements (such as new or modified attributes and operations).

After you select the **Quick Diff** command, a dialog opens that shows changes in element property values (see the following figure). Different colors help identify new, modified, and deleted values. You can analyze exact changes in the textual value of the selected property in the **Text Diff** box. If you want to see the original texts of both versions, click the Compare property values button [IMAGE alt='' src=''] on the toolbar of the dialog to open the **Compare property** dialog and then click **Original Texts**.

[IMAGE alt='' src='']

###### An example of the Quick Diff dialog of an element (class).

FullDiffAfter you select the **Full Diff** command for an element, the **Difference Viewer** dialog opens, showing changes in element property values, as well as detailed information for directly related elements and new relationships (see the figure below). For more information about using this dialog, see [CONFLUENCE_PAGE title='Analyzing comparison results' space='MT'].

[IMAGE alt='' src='']

###### An example of the Difference Viewer dialog of an element.

After you select the **Full Diff** command for a diagram, the **Difference Viewer** dialog opens, showing all changes in the diagram (see the figure below). For more information about using this dialog, see [CONFLUENCE_PAGE title='Viewing and analyzing differences of modified diagrams' space='MT'].

[IMAGE alt='' src='']

###### An example of the Difference Viewer dialog of a diagram.

Be aware that Quick Diff is not available for displaying diagram changes. Diagram changes (as diagram layout changes) can be displayed only in the **Full Diff**mode. To see these changes you must initiate the comparison of entire project versions. For this, select a couple of project versions in the **History** panel and on the shortcut menu click**Compare Projects**. For more information, see [CONFLUENCE_PAGE title='Analyzing comparison results' space='MT'].

##### Generating reports

To generate an element history report

1. Perform element history as described above.
2. On the History toolbar, click the Generate Report button. [ATTACHMENT filename='Element_history.png']
3. The Save As dialog opens to specify the location of the report file.

**Related pages**

- [CONFLUENCE_PAGE title='Reviewing project history' space='']
- [CONFLUENCE_PAGE title='Analyzing comparison results' space='MT']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><h3>Displaying element history </h3><p>To display the history of an element, do one of the following</p><hr /><ul><li data-uuid="5dc0c978-f773-4078-aa67-ed396c312306">Right-click the element or its symbol. From the shortcut menu, select <strong>History</strong>.<br /><ac:image ac:title="Element_short_cut_menu" ac:alt="Element_short_cut_menu"><ri:attachment ri:filename="image2018-3-16_11-33-0.png" /></ac:image></li><li data-uuid="e875ce3d-cfd5-41b9-9c0d-478e941c845b">Select the element or its symbol and press Ctrl + H.</li><li data-uuid="375d52a7-297a-49f0-a759-8eadc98910c8">Open the <ac:link><ri:page ri:space-key="MT" ri:content-title="Specification window" /></ac:link> of the element and click the History button <ac:image ac:title="History" ac:alt="History"><ri:attachment ri:filename="history_in_spec.png" /></ac:image>.</li><li data-uuid="07f62a57-d0cb-439c-9cde-c7db8e224de4">If it is a diagram, right-click an empty space on the diagram pane. From the shortcut menu, select <strong>History</strong>.</li></ul><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="ae3634f2-20b8-4c26-8431-6f1979836140"><ac:parameter ac:name="title">Stopping collecting changes</ac:parameter><ac:rich-text-body><p>If retrieving the element history takes too much time, you can click the <strong>Stop </strong>button to complete reviewing changes through different versions of the selected element.</p><p><ac:image><ri:attachment ri:filename="collecting_changes_in_versions.png" /></ac:image></p></ac:rich-text-body></ac:structured-macro><p><br /></p><p>The <strong>History</strong> panel of the selected element then opens at the bottom of the client application window. If you select an element in a used project, the corresponding panel title is <strong>Usage History</strong>. The highlighted row indicates current changes that are not yet committed. To refresh the list of versions, click the <ac:image ac:thumbnail="true" ac:height="20"><ri:attachment ri:filename="Refresh.png" /></ac:image> button in the panel's toolbar or perform the same actions as for opening the panel.</p><p><ac:image ac:align="center"><ri:attachment ri:filename="element_history_panel..png" /></ac:image></p><h6 style="text-align: center;">A list of project versions in the History panel.</h6><p class="auto-cursor-target">You can compare any two versions of an element to see the differences between them.</p><p>To display element version properties</p><hr /><ol><li data-uuid="7d532bb2-355f-44a0-a8c8-21b8bd7aa6c2">Open the element's <strong>History</strong> panel as described above.</li><li data-uuid="a505017d-501e-4ee1-9bbe-bb3aea79fb6b">Select the project version.</li><li data-uuid="0fd0ddac-fb26-4721-9932-d517bb495fcf">In the panel's toolbar, click the <ac:image ac:thumbnail="true" ac:width="24"><ri:attachment ri:filename="4.png" /></ac:image> button or right-click the selected version and select the <strong>Version Properties</strong> command.</li></ol><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="5ed6f645-7ee0-49a5-bcd1-ccde8f2ed9b4"><ac:rich-text-body><p><span>The button is disabled if either no version or multiple versions are selected.</span></p></ac:rich-text-body></ac:structured-macro><p>To display the history of an element in a used project</p><hr /><ol><li data-uuid="38a11e2b-7064-4ca8-8afc-64b82bd6d01d">Open the element's <strong>Usage History </strong>panel <span>as described above.</span></li><li data-uuid="00871325-7a29-45f6-896b-7b9047f0e373">Select the project version.</li><li data-uuid="dc31d14d-b73c-499d-b19f-463f64b22b41">In the panel's toolbar, click the <ac:image ac:thumbnail="true" ac:height="16"><ri:attachment ri:filename="display_changes.png" /></ac:image> button or right-click the selected version and select the <strong>Show History in Used Project</strong> command.</li></ol><h3><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="02b2532b-3d2c-4259-bc56-a1aeac9a95ba"><ac:parameter ac:name="">Comparing element versions</ac:parameter></ac:structured-macro>Comparing element versions</h3><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="4a73b4d1-6afc-4c40-a06b-26cf4a0706d8"><ac:rich-text-body><p>To compare project versions in the Teamwork Cloud environment, you are required to have the <a href="https://docs.nomagic.com/MCS/?contextKey=permissions&amp;version=latest&amp;variant=default"><strong>Read Resources </strong>permission</a> for every used project in compared versions.</p></ac:rich-text-body></ac:structured-macro><p>To compare element versions</p><hr /><ol><li data-uuid="32e29b14-6756-4afc-b327-387a035317ad"><p>Hold down Ctrl and select the versions you want to compare.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="a3488855-6fcc-4e60-bec8-34598df48e83"><ac:rich-text-body><p>You can only compare two versions. Please note that if you select more than two items, only two (the latest and the earliest versions) will be compared.</p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="b0a18123-e197-4a8f-ab43-dfcf36508614"><ac:rich-text-body><p>If you want to compare subsequent versions, you only need to select the later one.</p></ac:rich-text-body></ac:structured-macro></li><li data-uuid="08585e01-4e2c-49be-897d-ab09cb722cf6">On the panel's toolbar, click the <ac:image ac:thumbnail="true" ac:height="16"><ri:attachment ri:filename="quick_diff_button.png" /></ac:image> button or right-click the selection and choose either:<br /><br /><ul><li><strong><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="3ca12485-300f-4670-91aa-91cd828ba35e"><ac:parameter ac:name="">quickdiff</ac:parameter></ac:structured-macro>Quick Diff</strong> – to inspect changes of element property values (such as documentation, type, or multiplicity) in <em>a compact form</em>. </li><li><strong>Full Diff</strong> – to inspect changes of diagrams or element property values in <em>a detailed form,</em> as well as look at the properties of new relationships and directly related elements (such as new or modified attributes and operations).</li></ul><p><ac:image><ri:attachment ri:filename="compare_element_versions.png" /></ac:image></p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="15d5df0b-b443-40f9-8f0e-bb0f93760e25"><ac:rich-text-body><p> You can also choose the same commands from the toolbar of the <strong>History</strong> panel.</p></ac:rich-text-body></ac:structured-macro></li></ol><p>After you select the <strong>Quick Diff</strong> command, a dialog opens that shows changes in element property values (see the following figure). Different colors help identify new, modified, and deleted values. You can analyze exact changes in the textual value of the selected property in the <strong>Text Diff</strong> box. If you want to see the original texts of both versions, click the Compare property values button <ac:image ac:title="Compare property values" ac:alt="Compare property values"><ri:attachment ri:filename="compare_property_values_button.png" /></ac:image> on the toolbar of the dialog to open the <strong>Compare property</strong> dialog and then click <strong>Original Texts</strong>.</p><p><br /><ac:image ac:align="center"><ri:attachment ri:filename="quick_diff_dialog.png" /></ac:image></p><h6 style="text-align: center;">An example of the Quick Diff dialog of an element (class).</h6><p><br /></p><p><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="2828fb39-eb48-4699-8915-a9572fffd161"><ac:parameter ac:name="">FullDiff</ac:parameter></ac:structured-macro>After you select the <strong>Full Diff</strong> command for an element, the <strong>Difference Viewer</strong> dialog opens, showing changes in element property values, as well as detailed information for directly related elements and new relationships (see the figure below). For more information about using this dialog, see <ac:link><ri:page ri:space-key="MT" ri:content-title="Analyzing comparison results" /></ac:link>.</p><p><ac:image ac:align="center"><ri:attachment ri:filename="full_diff_viewer_dialog.png" /></ac:image></p><h6 style="text-align: center;">An example of the Difference Viewer dialog of an element.</h6><p>After you select the <strong>Full Diff</strong> command for a diagram, the <strong>Difference Viewer</strong> dialog opens, showing all changes in the diagram (see the figure below). For more information about using this dialog, see <ac:link><ri:page ri:space-key="MT" ri:content-title="Viewing and analyzing differences of modified diagrams" /></ac:link>.</p><p><br /></p><p><ac:image ac:align="center"><ri:attachment ri:filename="diagram_differences.png" /></ac:image></p><h6 style="text-align: center;"><span style="color:var(--ds-text,#707070);">An example of the Difference Viewer dialog of a diagram.</span> </h6><p>Be aware that Quick Diff is not available for displaying diagram changes. Diagram changes (as diagram layout changes) can be displayed only in the <strong>Full Diff </strong>mode. To see these changes you must initiate the comparison of entire project versions. For this, select a couple of project versions in the <strong>History</strong> panel and on the shortcut menu click<strong> Compare Projects</strong>. For more information, see <ac:link><ri:page ri:space-key="MT" ri:content-title="Analyzing comparison results" /></ac:link>.</p><h3>Generating reports</h3><p>To generate an element history report</p><hr /><ol><li data-uuid="58f3f794-8687-4cc6-a842-d96f3d16b5e0">Perform element history as described above.</li><li data-uuid="c544f2c3-a2bc-4d35-b02d-f47d65c6947e">On the <strong>History</strong> toolbar, click the<strong> </strong>Generate Report button.<br /><ac:image><ri:attachment ri:filename="Element_history.png" /></ac:image></li><li data-uuid="53cc90ff-dfc5-481d-b8f9-2f82b3ad2b85">The <strong>Save As </strong>dialog opens to specify the location of the report file.</li></ol></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><strong>Related pages</strong></p><ul><li data-uuid="371effdb-c5b8-44fe-ba3a-3596f5a48796"><ac:link><ri:page ri:content-title="Reviewing project history" /></ac:link></li><li data-uuid="d0ce5aef-ab27-4ec6-9b18-5e6aed981f34"><ac:link><ri:page ri:space-key="MT" ri:content-title="Analyzing comparison results" /></ac:link></li></ul></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=243969932 space=CM version=12 -->
## PAGE 00302: Reviewing historical versions of the project

- page_id: `243969932`
- space_key: `CM`
- source_url: https://docs.nomagic.com/spaces/CM/pages/243969932/Reviewing+historical+versions+of+the+project
- version_number: 12
- version_date: `2025-11-13T17:13:14.050+01:00`
- ancestors: Client-Side Collaborative Modeling Documentation > Using Teamwork Cloud > Reviewing project history
- labels: ['history-dialog', 'out-of-sync', 'set-as-latest']

### NORMALIZED CONTENT

Historical project versions are all versions of a project that were committed before the latest version. These versions are also referred to as project history. You can review the history of a project or its branch in one of the following ways:

- The **History** dialog - displays all historical versions of a project or project branch, including details such as the commit date, author, comment, and version tags.
- The **Project History** panel - displays all historical versions of the open project and its branch structure. The panel also includes details such as the commit date, author, message, and version tags.

##### Using the History dialog

To review the history of the selected project

1. In the main menu, select Collaborate > Projects or Open Server Project .
2. In the open dialog, select the project whose historical versions you want to review.
3. Do one of the following:
  - In the dialog toolbar, click [ATTACHMENT filename='project_history_button.png'] .
  - Right-click the selected project and select Project History .
4. In the **History** dialog, review all versions of the selected project. If a version has tags, they are displayed next to the version number.

[IMAGE alt='' src='']

###### Opening the **History** dialog.

Use the search bar to filter project versions according to:

- Project version (together with the commit tags)
- Author
- Comment

The following table describes the user interface elements of the **History** dialog.

| Column name | Description |
| --- | --- |
| Project version | The version number of a project. |
| Author | The name of the user who created the project version. |
| Date | The date and time when the project version was created. |
| Comment | The description of changes in the version. You can make a version comment when committing a project. |
| Button | Description |
| Set As Latest | Sets the selected project version as the latest version of the project or project branch.You must have the read-write permission for the branch in which you set the selected project version as the latest version. |
| Set As Latest > Select Branch | Sets the selected version as the latest in a specific branch.To use this feature, click the drop-down arrow next to the Set As Latest button, click Select Branch, then select a branch and click OK. |
| Compare | Compares two selected project versions. The differences between the selected versions are displayed in the Difference Viewer dialog. The button is available only when two project versions are selected (use the SHIFT or CTRL keys). |
| Properties | Opens the Version Properties dialog. |
| Open | Opens the selected version of the project. You can make changes only to the latest version of the project. Historical versions are read-only. |
| Cancel | Closes the dialog. |
| Help | Opens the related documentation page. |

The History dialig allows you to review the properties of the selected project version and add version tags. 
 
To review the properties of a project version

1. In the History dialog, select a project version whose properties you want to review.
2. Click the Properties button.
3. In the Version Properties dialog, do the following:
  - In the Comments tab, review the comment of the selected project version.
  - In the Tags tab, you can:
    - Review the tags of the selected version.
    - Edit a tag by selecting it and clicking the Edit button.
    - Add a new tag by clicking the Add button.
    - Mark the version as major by selecting the Major version check box.
  - In the Used Projects tab, review the projects used by the selected project version.
  - In the Meta information tab, review the metadata of the selected project version.

##### Using the Project History panel

To review the history and branch structure of the open project

1. In the main menu, select Window > Project History .
2. In the open Project History panel, review all versions of the open project, its branch structure, and other details, such as the author, commit date, commit message, and version tags.

[IMAGE alt='' src='']

###### The **Project History** panel displaying all project versions and its branch structure.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><span style="color:var(--ds-text,#172b4d);">Historical project versions are all versions of a project that were committed before the latest version. These versions are also referred to as project history. You can review the history of a project or its branch in one of the following ways:</span></p><ul><li><span style="color:var(--ds-text,#172b4d);">The <strong>History</strong> dialog - displays all historical versions of a project or project branch, including details such as the commit date, author, comment, and version tags.</span></li><li data-uuid="b7919a91-e5f7-4d9d-b512-47d852f013db"><span style="color:var(--ds-text,#172b4d);">The <strong>Project History</strong> panel - displays all historical versions of the open project and its branch structure. The panel also includes details such as the commit date, author, message, and version tags.</span></li></ul><h3>Using the History dialog</h3><p>To review the history of the selected project</p><hr /><ol><li data-uuid="6df2d4b9-e328-46b1-913e-1e627c06e842">In the main menu, select <strong>Collaborate</strong> &gt; <strong>Projects</strong> or <strong>Open Server Project</strong>.</li><li>In the open dialog, select the project whose historical versions you want to review.</li><li>Do one of the following:<br /><ul><li>In the dialog toolbar, click <ac:image ac:thumbnail="true" ac:height="14"><ri:attachment ri:filename="project_history_button.png" /></ac:image>.</li><li>Right-click the selected project and select <strong>Project</strong><strong> History</strong>.</li></ul></li><li><p>In the <strong>History</strong> dialog, review all versions of the selected project. If a version has tags, they are displayed next to the version number.</p></li></ol><p style="text-align: center;"><ac:image><ri:attachment ri:filename="history_dialog.png" /></ac:image></p><h6 style="text-align: center;">Opening the <strong>History</strong> dialog.</h6><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="82ec3531-1954-443c-9837-e54adc1fa2ce"><ac:rich-text-body><p>Use the search bar to filter project versions according to:</p><ul><li>Project version (together with the commit tags)</li><li>Author</li><li>Comment</li></ul></ac:rich-text-body></ac:structured-macro><p>The following table describes the user interface elements of the <strong>History</strong> dialog.</p><table class="relative-table wrapped" style="width: 80.8767%;"><colgroup><col style="width: 20.7367%;" /><col style="width: 79.2633%;" /></colgroup><thead><tr><th><p>Column name</p></th><th><p>Description</p></th></tr></thead><tbody><tr><td colspan="1"><strong>Project version</strong></td><td colspan="1">The version number of a project.</td></tr><tr><td><strong>Author</strong></td><td><p>The name of the user who created the project version.</p></td></tr><tr><td colspan="1"><strong>Date</strong></td><td colspan="1"><span>The date and time when the project version was created.</span></td></tr><tr><td><strong>Comment</strong></td><td><p>The description of changes in the version. You can make a version comment when committing a project.</p></td></tr><tr><th>Button</th><th><p>Description</p></th></tr><tr><td colspan="1"><strong>Set As Latest</strong></td><td colspan="1"><div class="content-wrapper"><p><span>Sets the selected project version as the latest version <span>of the project or project branch.</span></span></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="54de5397-1248-4fbc-af5a-241183042f4f"><ac:rich-text-body><p>You must have the read-write permission for<span> the branch in which </span>you set the selected project version as the latest version.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></div></td></tr><tr><td colspan="1"><strong>Set As Latest &gt; Select Branch</strong></td><td colspan="1"><div class="content-wrapper"><p><span style="color:var(--ds-text,#000000);">Sets the selected version as the latest in a specific <ac:inline-comment-marker ac:ref="f77c1d77-4985-4df0-b5e8-b8109a866d8f">branch</ac:inline-comment-marker>.</span></p><p><span style="color:var(--ds-text,#000000);">To use this feature, click the drop-down arrow next to the <strong>Set As Latest </strong>button, click <strong>Select Branch</strong>, then select a branch and click <strong>OK</strong>.</span></p></div></td></tr><tr><td><strong>Compare</strong></td><td><p>Compares two selected project versions. The differences between the selected versions are displayed in the <strong>Difference Viewer</strong> dialog. The button is available only when two project versions are selected (use the SHIFT or CTRL keys).</p></td></tr><tr><td><strong>Properties</strong></td><td>Opens the <strong>Version Properties</strong> dialog.</td></tr><tr><td><strong>Open</strong></td><td><p>Opens the selected version of the project. You can make changes only to the latest version of the project. Historical versions are read-only.</p></td></tr><tr><td><strong>Cancel</strong></td><td>Closes the dialog.</td></tr><tr><td colspan="1"><strong>Help</strong></td><td colspan="1"><p>Opens the related documentation page<strong>.</strong></p></td></tr></tbody></table><p><br />The History dialig allows you to review the properties of the selected project version and add version tags.<br /><br />To review the properties of a project version</p><hr /><ol><li>In the <strong>History</strong> dialog, select a project version whose properties you want to review.</li><li>Click the <strong>Properties</strong> button.</li><li data-uuid="34295ad8-13c6-45d6-95da-761a6216f4ea">In the <strong>Version Properties</strong> dialog, do the following:<ul><li data-uuid="bf23255e-e39a-46a3-addb-de5a5396cd67">In the <strong>Comments</strong> tab, review the comment of the selected project version.</li><li data-uuid="c8a5817a-0460-4e71-9f0b-0694178996a3">In the <strong>Tags</strong> tab, you can:<ul><li data-uuid="cfa4961f-baa5-4f73-b629-349587afeac5">Review the tags of the selected version.</li><li data-uuid="e1ecdd68-93a8-432e-8e44-727c9407b278">Edit a tag by selecting it and clicking the <strong>Edit</strong> button.</li><li data-uuid="a0c38032-a994-4f88-ad83-b44cd31dd33e">Add a new tag by clicking the <strong>Add</strong> button.</li><li data-uuid="3292a49f-4eaf-4b25-8a4a-bbda1e5eab7d">Mark the version as major by selecting the <strong>Major version</strong> check box.</li></ul></li><li data-uuid="538067d8-c84f-449f-8922-9187d6f8f72e">In the <strong>Used Projects</strong> tab, review the projects used by the selected project version.</li><li data-uuid="e40c6213-abd0-4ef2-beac-54cb813d0e8f">In the <strong>Meta information</strong> tab, review the metadata of the selected project version.</li></ul></li></ol><h3>Using the Project History panel</h3><p>To review the history and branch structure of the open project</p><hr /><ol><li data-uuid="f08590ed-092a-44db-a1ac-8b191e792e66">In the main menu, select <strong>Window</strong> &gt; <strong>Project History</strong>.</li><li data-uuid="7d557b11-34c7-4eb3-9eb9-16ec56eb6700">In the open <strong>Project History</strong> panel, review all versions of the open project, its branch structure, and other details, such as the author, commit date, commit message, and version tags.</li></ol><p style="text-align: center;"><ac:image><ri:attachment ri:filename="project_history_panel.png" /></ac:image></p><h6 style="text-align: center;">The <strong>Project History</strong> panel displaying all project versions and its branch structure.</h6>
````

<!--NOMAGIC_PAGE id=243969930 space=CM version=7 -->
## PAGE 00303: Reviewing project history

- page_id: `243969930`
- space_key: `CM`
- source_url: https://docs.nomagic.com/spaces/CM/pages/243969930/Reviewing+project+history
- version_number: 7
- version_date: `2025-11-13T17:15:13.424+01:00`
- ancestors: Client-Side Collaborative Modeling Documentation > Using Teamwork Cloud
- labels: []

### NORMALIZED CONTENT

Every time a [CONFLUENCE_PAGE title='Committing changes to Teamwork Cloud' space=''], a new version of that project is created. Over time, projects accumulate multiple versions. All project versions committed before the latest version are referred to as [CONFLUENCE_PAGE title='Reviewing historical versions of the project' space=''].

Every element in the model — including diagrams — maintains its own version history, which can be [CONFLUENCE_PAGE title='Reviewing element history and inspecting changes' space=''] in any open project. A new version of an element is created whenever its properties are modified. This includes updates such as editing documentation, changing multiplicity or type, or adding new attributes or operations. Similarly, a new version of a diagram is created whenever you modify its layout or properties.

You can at the element level — for example, within a selected package or classifier element. This capability is especially valuable for system engineers, as it allows you to trace the history of composed elements such as Blocks, Requirements.

To learn more, see

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>Every time a <ac:link><ri:page ri:content-title="Committing changes to Teamwork Cloud" /><ac:plain-text-link-body><![CDATA[project is committed]]></ac:plain-text-link-body></ac:link>, a new version of that project is created. Over time, projects accumulate multiple versions. All project versions committed before the latest version are referred to as <ac:link><ri:page ri:content-title="Reviewing historical versions of the project" /><ac:plain-text-link-body><![CDATA[historical versions]]></ac:plain-text-link-body></ac:link>.</p><p>Every element in the model — including diagrams — maintains its own version history, which can be <ac:link><ri:page ri:content-title="Reviewing element history and inspecting changes" /><ac:plain-text-link-body><![CDATA[reviewed]]></ac:plain-text-link-body></ac:link> in any open project. A new version of an element is created whenever its properties are modified. This includes updates such as editing documentation, changing multiplicity or type, or adding new attributes or operations. Similarly, a new version of a diagram is created whenever you modify its layout or properties.</p><p><span style="color:var(--ds-text,#333333);">You can <ac:link><ac:plain-text-link-body><![CDATA[review model changes within a specific scope]]></ac:plain-text-link-body></ac:link> at the element level — for example, within a selected package or classifier element. This capability is especially valuable for system engineers, as it allows you to trace the history of composed elements such as Blocks, Requirements.</span></p><p><span style="color:var(--ds-text,#333333);">To learn more, see</span></p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="d40f8338-4e2c-42e3-ae78-b7b3ffcab65b" /></p>
````

<!--NOMAGIC_PAGE id=243969781 space=CM version=2 -->
## PAGE 00304: Saving a local copy of Teamwork Cloud project

- page_id: `243969781`
- space_key: `CM`
- source_url: https://docs.nomagic.com/spaces/CM/pages/243969781/Saving+a+local+copy+of+Teamwork+Cloud+project
- version_number: 2
- version_date: `2026-03-09T12:21:35.151+01:00`
- ancestors: Client-Side Collaborative Modeling Documentation > Using Teamwork Cloud > Collaboration between disconnected teams > Using local project file format
- labels: []

### NORMALIZED CONTENT

To assign a Teamwork Cloud project to a user who cannot access the project on the server, or to move the project to another server, you can save a local copy on your computer. This enables you to send the local copy by email or add it to another server.

#### NOTE: Note

Note

The local copy of the project will not have locking and project version information. You will not be able to commit local project changes to the server.

To save a local copy of a Teamwork Cloud project

1. From the File menu, select Save Project As .
2. The question box appears. If you are sure you want to save a local copy of the server project, click Save .
3. Specify a name and location to save the project.
4. Wait while the local copy is saved to your computer.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>To assign a Teamwork Cloud project to a user who cannot access the project on the server, or to move the project to another server, you can save a local copy on your computer. This enables you to send the local copy by email or add it to another server.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="02f9916c-8699-44fc-9f68-1bc80a8f08b6"><ac:parameter ac:name="title">Note</ac:parameter><ac:rich-text-body><p>The local copy of the project will not have locking and project version information. You will not be able to commit local project changes to the server.</p></ac:rich-text-body></ac:structured-macro><p><br /></p><p>To save a local copy of a Teamwork Cloud project</p><hr /><ol><li data-uuid="52bbe5a8-e93a-465c-8d9e-1b9f354bdc27">From the <strong>File</strong> menu, select <strong>Save Project As</strong>.</li><li data-uuid="4a9bd4d3-5220-487c-82b7-2f41b6715a5c">The question box appears. If you are sure you want to save a local copy of the server project, click<strong> Save</strong>. </li><li data-uuid="4409d781-3bcf-49b9-a706-0233552fbd57">Specify a name and location to save the project.</li><li data-uuid="af2b8f03-141f-4cf9-9649-a5d944ca67f2">Wait while the local copy is saved to your computer.</li></ol>
````

<!--NOMAGIC_PAGE id=243969763 space=CM version=1 -->
## PAGE 00305: Saving server project to exchange format

- page_id: `243969763`
- space_key: `CM`
- source_url: https://docs.nomagic.com/spaces/CM/pages/243969763/Saving+server+project+to+exchange+format
- version_number: 1
- version_date: `2025-07-31T10:51:37.053+02:00`
- ancestors: Client-Side Collaborative Modeling Documentation > Using Teamwork Cloud > Collaboration between disconnected teams > Using server project file format
- labels: []

### NORMALIZED CONTENT

To save a server project to an exchange format

1. From the File menu, select Export To > Server Project File and one of the following options:
  - Without Used Projects: export the main project without used projects. All of the content from used projects will still be embedded into the main project, but importing or updating used projects will not be available;
  - With Used Projects: export the full project with used projects.
2. Specify a name and location to save the project.
3. Wait while the local copy is saved to your computer.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>To save a server project to an exchange format</p><hr /><ol><li>From the <strong>File</strong> menu, select <strong>Export To &gt; Server Project File </strong>and one of the following options:<br /><ul><li><strong><ac:inline-comment-marker ac:ref="8312fec2-2efb-4681-8e36-2b188b6d56eb">Without Used Projects: </ac:inline-comment-marker></strong>export the main project without used projects. All of the content from used projects will still be embedded into the main project, but importing or updating used projects will not be available;</li><li><strong>With Used Projects: </strong>export the full project with used projects.</li></ul></li><li>Specify a name and location to save the project.</li><li>Wait while the local copy is saved to your computer.</li></ol>
````

<!--NOMAGIC_PAGE id=291831904 space=CM version=5 -->
## PAGE 00306: Seamless Collaboration

- page_id: `291831904`
- space_key: `CM`
- source_url: https://docs.nomagic.com/spaces/CM/pages/291831904/Seamless+Collaboration
- version_number: 5
- version_date: `2026-02-18T13:15:28.355+01:00`
- ancestors: Client-Side Collaborative Modeling Documentation > Collaboration powered by 3DEXPERIENCE platform > Technical practices
- labels: []

### NORMALIZED CONTENT

#### Why

Working in a team with multiple users at the same time on a single CATIA Magic project can create conflicts in managing the data. To prevent such cumbersome conflict management, it is important to organize work packages.

#### What

This technical practice focuses on achieving seamless collaboration for users, either by utilizing the Lock/Unlock feature or by managing the work packages through branches of the CATIA Magic project.

#### Target Audience

Systems Engineer, Systems Architect

#### Knowledge

##### Lock and Unlock a Project

###### Lock Elements and Diagrams

You must lock the part of the model you are going to edit to prevent other users from editing it at the same time. An element can only be locked by one user at a time. Once it is locked, other users can only access it but not edit it.

The following table outlines what you can edit after you lock a single element, single diagram, diagram with elements, symbol styles and project usages.

| When you lock... | You can... |
| --- | --- |
| Element | Edit element specification properties (in the Specification window) |
| Diagram | Edit:Diagram specification properties (in the Specification window)Diagram properties (in the Diagram Properties dialog)Symbol layout on the diagram paneSymbol properties (in the Symbol Properties dialog) |
| Diagram with elements | Edit:Diagram specification properties (in the Specification window)Element specification properties (in the Specification window and on the diagram pane)Diagram properties (in the Symbol Properties dialog)Symbol properties (in the Symbol Properties dialog)Symbol layout on the diagram pane |
| Symbol styles | Edit properties of symbol styles (in the Project Options dialog) |
| Project usages | Import used projects as packages into the main projectStop using projectsChange versions of used projects |

###### Unlock Elements and Diagrams

You can use commands from the shortcut menu to unlock elements and diagrams. Unlocking modified elements will trigger to commit the project.

[IMAGE alt='' src='']

##### Project Branching

Project branching enables multiple users to work on the same model at the same time. For this, you need to create a project branch, which is a copy of the project. You can modify the branch as required, independent of other branches. Branches can be merged back when required. Conflicts between the branches are resolved during the merge process.

#### Use Cases

##### Locking and Managing Branches

**Scenario:**

A system engineer is assigned to make edits to a CATIA Magic project. He uses locking and unlocking to prevent other users from making changes at the same time. He is also responsible for moving a branch to a different collaborative space for other teams to make edits to the CATIA Magic project.

**Actors/Personas:**

**Dave, Systems Engineer**: Dave, is responsible for making changes in the Cool Down Air Cabin diagram for the cooling system. He is also assigned the task of sharing a branch of the project with the traceability team to make their changes in the Cooling System project.

**Workflow:**

**[IMAGE alt='' src='']**

#### How

##### Prerequisite Roles

3DSwymer (IFW-OC), Collaborative Industry Innovator (CSV-OC), Collaborative Designer for CATIA Magic (SSY-OC)

##### Step 1: Lock Model

600400

##### Step 2: Share Branch

600400

##### Step 3: Merge Branches

600400

#### Recommendarion

##### Unlocking Elements Locked by Other Users

Forced unlocking is helpful when elements are left locked by a user who is currently unavailable. This functionality is only available to the Leader role on**3D**EXPERIENCE platform. As a result, all the locks made by another user are released and any changes the user made are lost forever.

To unlock elements locked by another user:

1. From the Collaborate menu, select Unlock All .
2. If a message opens asking you to choose what to unlock, click**Unlock All**. The**Commit Project to the Server**dialog opens. 
[IMAGE alt='' src='']
3. In the dialog, do the following:
  1. Type a comment (if needed).
  2. Click Commit .

### EXACT CONFLUENCE STORAGE SOURCE

````html
<h2>Why</h2><p>Working in a team with multiple users at the same time on a single CATIA Magic project can create conflicts in managing the data. To prevent such cumbersome conflict management, it is important to organize work packages.</p><h2>What</h2><p>This technical practice focuses on achieving seamless collaboration for users, either by utilizing the Lock/Unlock feature or by managing the work packages through branches of the CATIA Magic project.</p><h2>Target Audience</h2><p>Systems Engineer, Systems Architect</p><h2>Knowledge</h2><h3>Lock and Unlock a Project</h3><h4>Lock Elements and Diagrams</h4><p>You must lock the part of the model you are going to edit to prevent other users from editing it at the same time. An element can only be locked by one user at a time. Once it is locked, other users can only access it but not edit it.</p><p>The following table outlines what you can edit after you lock a single element, single diagram, diagram with elements, symbol styles and project usages. </p><table class="wrapped" data-mce-resize="false"><colgroup class=""><col class="" style="width: 325.781px;" /><col class="" style="width: 623.219px;" /></colgroup><thead class=""><tr class=""><th style="text-align: center;vertical-align: top;"><p><strong>When you lock...</strong></p></th><th style="text-align: center;vertical-align: top;"><p><strong>You can...</strong></p></th></tr></thead><tbody class=""><tr class=""><td style="text-align: center;">Element</td><td style="vertical-align: top;">Edit element specification properties (in the Specification window)</td></tr><tr class=""><td style="text-align: center;">Diagram</td><td style="vertical-align: top;"><p>Edit:</p><ul><li data-uuid="6fb0c92d-ee5f-478b-b671-203df82cc822">Diagram specification properties (in the Specification window)</li><li data-uuid="1d321e69-0267-49dd-8517-2273e6a98629">Diagram properties (in the<span> </span><strong>Diagram Properties</strong><span> </span>dialog)</li><li data-uuid="f0e01035-cca2-4321-bf00-de98182c6a50">Symbol layout on the diagram pane</li><li data-uuid="97414198-5d21-4466-a690-d1a11f287c05">Symbol properties (in the<span> </span><strong>Symbol Properties</strong><span> </span>dialog)</li></ul></td></tr><tr class=""><td style="text-align: center;">Diagram with elements</td><td style="vertical-align: top;"><p>Edit:</p><ul><li data-uuid="1ec0b8bc-eb12-4d49-8d93-659cd6e29872">Diagram specification properties (in the Specification window)</li><li data-uuid="1767b0d2-5322-4027-a696-d234e32a9051">Element specification properties (in the Specification window and on the diagram pane)</li><li data-uuid="02542e7a-5548-4e13-8bb1-370512ccc1e3">Diagram properties (in the<span> </span><strong>Symbol Properties</strong><span> </span>dialog)</li><li data-uuid="f35c27de-1c75-42f8-80a6-0a09ca145d22">Symbol properties (in the<span> </span><strong>Symbol Properties</strong><span> </span>dialog)</li><li data-uuid="8ee853d3-dc42-407f-9492-aab7c447139c">Symbol layout on the diagram pane</li></ul></td></tr><tr class=""><td style="text-align: center;" colspan="1">Symbol styles</td><td style="vertical-align: top;" colspan="1"><p>Edit properties of symbol styles (in the<span> </span><strong>Project Options</strong><span> </span>dialog)</p></td></tr><tr class=""><td style="text-align: center;" colspan="1">Project usages</td><td style="vertical-align: top;" colspan="1"><ul><li data-uuid="da7c1105-8376-40f1-8f71-8c71fa693de4">Import used projects as packages into the main project</li><li data-uuid="c19f9194-b8cc-4aab-abae-69f22c4aa509">Stop using projects</li><li data-uuid="20f85db6-215d-491a-9666-08797bcfa869">Change versions of used projects</li></ul></td></tr></tbody></table><h4>Unlock Elements and Diagrams</h4><p>You can use commands from the shortcut menu to unlock elements and diagrams. Unlocking modified elements will trigger to commit the project.</p><p><ac:image><ri:attachment ri:filename="Unlock Elements and Diagrams.png" /></ac:image></p><h3>Project Branching</h3><p>Project branching enables multiple users to work on the same model at the same time. For this, you need to create a project branch, which is a copy of the project. You can modify the branch as required, independent of other branches. Branches can be merged back when required. Conflicts between the branches are resolved during the merge process.</p><h2>Use Cases</h2><h3>Locking and Managing Branches</h3><p><strong>Scenario: </strong></p><p>A system engineer is assigned to make edits to a CATIA Magic project. He uses locking and unlocking to prevent other users from making changes at the same time. He is also responsible for moving a branch to a different collaborative space for other teams to make edits to the CATIA Magic project.</p><p><strong>Actors/Personas:</strong></p><p><strong>Dave, Systems Engineer</strong>: Dave, is responsible for making changes in the Cool Down Air Cabin diagram for the cooling system. He is also assigned the task of sharing a branch of the project with the traceability team to make their changes in the Cooling System project.</p><p><strong>Workflow:</strong></p><p><strong><ac:image ac:width="910"><ri:attachment ri:filename="Workflow 3_6_2025.png" /></ac:image></strong></p><h2>How</h2><h3>Prerequisite Roles</h3><p>3DSwymer (IFW-OC), Collaborative Industry Innovator (CSV-OC), Collaborative Designer for CATIA Magic (SSY-OC)</p><h3>Step 1: Lock Model </h3><p><ac:structured-macro ac:name="widget" ac:schema-version="1" ac:macro-id="6cfd0c9e-be11-463f-8ced-87ba2b5c4021"><ac:parameter ac:name="width">600</ac:parameter><ac:parameter ac:name="url"><ri:url ri:value="https://www.youtube.com/watch?v=8d7mVvDn-Mw&amp;list=PLlvXsDYdI5UMPvWYNEF0F4Rq0w18dsMJz" /></ac:parameter><ac:parameter ac:name="height">400</ac:parameter></ac:structured-macro></p><h3>Step 2: Share Branch</h3><p><ac:structured-macro ac:name="widget" ac:schema-version="1" ac:macro-id="4602c918-73e5-4252-83da-fb3ea5440a1e"><ac:parameter ac:name="width">600</ac:parameter><ac:parameter ac:name="url"><ri:url ri:value="https://www.youtube.com/watch?v=6CveqbmIdtM&amp;list=PLlvXsDYdI5UMPvWYNEF0F4Rq0w18dsMJz" /></ac:parameter><ac:parameter ac:name="height">400</ac:parameter></ac:structured-macro></p><h3>Step 3: Merge Branches</h3><p><ac:structured-macro ac:name="widget" ac:schema-version="1" ac:macro-id="21515d0a-631d-49de-a047-348d6dc72e37"><ac:parameter ac:name="width">600</ac:parameter><ac:parameter ac:name="url"><ri:url ri:value="https://www.youtube.com/watch?v=nreEukjK50A&amp;list=PLlvXsDYdI5UMPvWYNEF0F4Rq0w18dsMJz" /></ac:parameter><ac:parameter ac:name="height">400</ac:parameter></ac:structured-macro></p><h2>Recommendarion</h2><h3>Unlocking Elements Locked by Other Users</h3><p>Forced unlocking is helpful when elements are left locked by a user who is currently unavailable. This functionality is only available to the Leader role on<span> </span><strong>3D</strong>EXPERIENCE platform. As a result, all the locks made by another user are released and any changes the user made are lost forever.</p><p>To unlock elements locked by another user:</p><ol><li data-uuid="560150b2-5374-4255-b14e-2a5a7c741590">From the<span> </span><strong>Collaborate</strong><span> </span>menu, select<span> </span><strong>Unlock All</strong>.</li><li data-uuid="45899f8f-1219-4a31-9b25-45de9a6643cf"><p>If a message opens asking you to choose what to unlock, click<span> </span><strong>Unlock All</strong>. The<span> </span><strong>Commit Project to the Server</strong><span> </span>dialog opens.<br /><ac:image><ri:attachment ri:filename="1739235406948-title 3_6_2025.png" /></ac:image></p></li><li data-uuid="d23fcf92-8d84-4185-b216-fbaf2e4bcaa0">In the dialog, do the following:<ol><li>Type a comment (if needed).</li><li>Click<span> </span><strong>Commit</strong>.</li></ol></li></ol>
````

<!--NOMAGIC_PAGE id=291831892 space=CM version=5 -->
## PAGE 00307: Search with Predefined Queries and 6WTags

- page_id: `291831892`
- space_key: `CM`
- source_url: https://docs.nomagic.com/spaces/CM/pages/291831892/Search+with+Predefined+Queries+and+6WTags
- version_number: 5
- version_date: `2026-02-18T13:17:50.585+01:00`
- ancestors: Client-Side Collaborative Modeling Documentation > Collaboration powered by 3DEXPERIENCE platform > Technical practices
- labels: []

### NORMALIZED CONTENT

#### Why

A team working on CATIA Magic may need to create numerous revisions and branches, making it crucial for users to select the correct project or data to work on. While many CATIA Magic users are familiar with the tree structures, they may not be aware of the advanced search features available on the**3D**EXPERIENCE platform.

#### What

This Technical Practice emphasizes the importance of knowing the project's location. Clients are familiar with the CATIA Magic tree structure but not server storage of the**3D**EXPERIENCE platform. Optimizing search helps to open the correct project with the right dependencies.

#### Target Audience

Systems Architect, Systems Engineer, Profile Administrator

#### Knowledge

**6WTags**

6WTags help filter the desired data in the**3D**EXPERIENCE platform by organizing information into six key categories:

[IMAGE alt='' src='']

#### Use Cases

##### Search for CATIA Magic Project on the 3DEXPERIENCE Platform

**Scenario:**

A system architect wants to open a CATIA Magic Project available on the**3D**EXPERIENCE platform. He uses the keywords and 6WTags to navigate to the desired CATIA Magic Project.

**Actors/Personas:**

**John System Architect**: John, is searching for CATIA Magic data on the**3D**EXPERIENCE platform.

**Workflow:**

[IMAGE alt='' src='']

#### How

##### Prerequisite Roles

3DSwymer (IFW-OC), Collaborative Industry Innovator (CSV-OC), Collaborative Designer for CATIA Magic (SSY-OC)

##### Step 1: Search with Predefined Queries

600400

##### Step 2: Use 6WTags to Navigate on the 3DEXPERIENCE Platform

600400

#### Recommendation

- The**3D**EXPERIENCE platform creates different entries for each revision and branch. Ensure that you are selecting the correct branch and revisions while working on the CATIA Magic project from the search results.

[IMAGE alt='' src='']

- For each W category, search results are grouped by subcategories. Click the arrow next to each W to focus the view on a specific subcategory.

| For example, in the What tab, you can focus on a specific category of document. |  |
| --- | --- |
| In the Where tab, you can also focus the content specific to a continent or a country, by clicking the pinpoints on the Map view. |  |

In the**Who**,**When**, and**What**tabs, when a category returns a large number of results, you can click**View all Content**to display a pagination and browse all the results from this category.

- Refer to the following User Assistance document on the Predefined Queries for CATIA Magic.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<h2>Why</h2><p>A team working on CATIA Magic may need to create numerous revisions and branches, making it crucial for users to select the correct project or data to work on. While many CATIA Magic users are familiar with the tree structures, they may not be aware of the advanced search features available on the<span> </span><strong>3D</strong>EXPERIENCE platform.</p><h2>What</h2><p>This Technical Practice emphasizes the importance of knowing the project's location. Clients are familiar with the CATIA Magic tree structure but not server storage of the<span> </span><strong>3D</strong>EXPERIENCE platform. Optimizing search helps to open the correct project with the right dependencies.</p><h2>Target Audience</h2><p>Systems Architect, Systems Engineer, Profile Administrator</p><h2>Knowledge</h2><p><strong>6WTags</strong></p><p>6WTags help filter the desired data in the<span> </span><strong>3D</strong>EXPERIENCE platform by organizing information into six key categories:</p><p><ac:image ac:width="664"><ri:attachment ri:filename="image 3_19_2025.png" /></ac:image></p><h2>Use Cases</h2><h3>Search for CATIA Magic Project on the 3DEXPERIENCE Platform</h3><p><strong>Scenario: </strong></p><p>A system architect wants to open a CATIA Magic Project available on the<span> </span><strong>3D</strong>EXPERIENCE platform. He uses the keywords and 6WTags to navigate to the desired CATIA Magic Project.</p><p><strong>Actors/Personas:</strong></p><p><strong>John System Architect</strong>: John, is searching for CATIA Magic data on the<span> </span><strong>3D</strong>EXPERIENCE platform.</p><p><strong>Workflow:</strong></p><p><ac:image ac:height="250"><ri:attachment ri:filename="image 3_19_2025 (1).png" /></ac:image></p><h2>How</h2><h3>Prerequisite Roles</h3><p>3DSwymer (IFW-OC), Collaborative Industry Innovator (CSV-OC), Collaborative Designer for CATIA Magic (SSY-OC)</p><h3>Step 1: Search with Predefined Queries</h3><p><ac:structured-macro ac:name="widget" ac:schema-version="1" ac:macro-id="5107ab0c-73e2-4d28-9e62-758b67fa459c"><ac:parameter ac:name="width">600</ac:parameter><ac:parameter ac:name="url"><ri:url ri:value="https://www.youtube.com/watch?v=mVzLX-HmlTA&amp;list=PLlvXsDYdI5UMPvWYNEF0F4Rq0w18dsMJz" /></ac:parameter><ac:parameter ac:name="height">400</ac:parameter></ac:structured-macro></p><h3>Step 2: Use 6WTags to Navigate on the 3DEXPERIENCE Platform</h3><p><ac:structured-macro ac:name="widget" ac:schema-version="1" ac:macro-id="b6ceed65-11ed-4721-968b-0396b65fd941"><ac:parameter ac:name="width">600</ac:parameter><ac:parameter ac:name="url"><ri:url ri:value="https://www.youtube.com/watch?v=lM77VBK4rPE&amp;list=PLlvXsDYdI5UMPvWYNEF0F4Rq0w18dsMJz" /></ac:parameter><ac:parameter ac:name="height">400</ac:parameter></ac:structured-macro></p><h2>Recommendation</h2><ul><li data-uuid="077bf3fc-afa8-43e6-8148-2fd0fc488acb"><p>The<span> </span><strong>3D</strong>EXPERIENCE platform creates different entries for each revision and branch. Ensure that you are selecting the correct branch and revisions while working on the CATIA Magic project from the search results.</p></li></ul><p><br /><ac:image ac:align="center"><ri:attachment ri:filename="2Revisions 3_19_2025.png" /></ac:image></p><ul><li data-uuid="00672485-6a37-41de-b488-78788b7d5d22">For each<span> </span><strong>W</strong><span> </span>category, search results are grouped by subcategories. Click the arrow next to each<span> </span><strong>W</strong><span> </span>to focus the view on a specific subcategory.</li></ul><table class="wrapped" data-mce-resize="false"><colgroup class=""><col class="" style="width: 483.5px;" /><col class="" style="width: 264.375px;" /></colgroup><tbody class=""><tr class=""><td>For example, in the<span> </span><strong>What</strong><span> </span>tab, you can focus on a specific category of document.</td><td><div class="content-wrapper"><ac:image><ri:attachment ri:filename="2025-02-05_17-35-57 3_19_2025.png" /></ac:image><br /><br /></div></td></tr><tr class=""><td>In the<span> </span><strong>Where</strong><span> </span>tab, you can also focus the content specific to a continent or a country, by clicking the pinpoints on the Map view.</td><td><div class="content-wrapper"><p><ac:image><ri:attachment ri:filename="1737950251487-title_o1 3_19_2025.jpg" /></ac:image></p></div></td></tr></tbody></table><p style="margin-left: 40.0px;">In the<span> </span><strong>Who</strong>,<span> </span><strong>When</strong>, and<span> </span><strong>What</strong><span> </span>tabs, when a category returns a large number of results, you can click<span> </span><strong>View all Content</strong><span> </span>to display a pagination and browse all the results from this category.</p><ul><li data-uuid="d845cb7e-d1ba-4bf7-89da-6fb6d979a844">Refer to the following<span> </span><a style="text-decoration: none;" href="https://docservices/doc427/English/?show=CATMagcUserMap/CATMagc-c-PredefinedQueries.htm&amp;contextscope=all">User Assistance document</a><span> </span>on the Predefined Queries for CATIA Magic.</li></ul>
````

<!--NOMAGIC_PAGE id=243969831 space=CM version=1 -->
## PAGE 00308: Setting package permissions

- page_id: `243969831`
- space_key: `CM`
- source_url: https://docs.nomagic.com/spaces/CM/pages/243969831/Setting+package+permissions
- version_number: 1
- version_date: `2025-07-31T10:51:38.340+02:00`
- ancestors: Client-Side Collaborative Modeling Documentation > Using Teamwork Cloud > Package permissions
- labels: []

### NORMALIZED CONTENT

1282481725

1282481727

1282481724

**On this page**

**3**

1282481726

##### Modify package permissions

To modify the permissions of the package

1. Right-click the package or its shape and select **Permissions**. The **Permissions of Package** dialog opens. The full name of the dialog depends on the selected package name. Thus, if you select to modify the permissions of the package *domain*, the **Permissions of Package domain** dialog opens.
2. Add new package permission:
  1. Click the Add button under the Package permissions table. The Select User/Group dialog opens.
  2. Use the search bar to filter users or groups, then click to select the check box near the user or group name. [IMAGE alt='' src='']
  3. Click OK and see the new row appeared in the Package permissions table.
  4. Click the Permission cell and select:
    - Read-Only to restrict editing of the package for the selected user/group.
    - Read-Write to allow editing of the package for the selected user/group.
  5. If you don't want to apply the same permission on the subpackages of this package, click the Apply To cell and select This package only .
3. Add as many permissions as you need by repeating step 3.
4. Close the Permissions of Package dialog.

###### Inheritable permissions

The **Permissions of Package** dialog includes a few options for handling inheritable permissions. The following table provides their descriptions.

| Option | Description |
| --- | --- |
| Include inheritable permissions from the parent | Inheritable permissions of the package are those that apply to its subpackages as well.By default, these permissions are displayed together with individual permissions of every subpackage, but cannot be modified or deleted there. If you want to hide them, click to clear the check box.Let's say you have a package Model and a subpackage Requirements.If you set on the package Model the Read-Only permission for a certain user and leave the default setting to apply this permission on subpackages as well, the Permissions of Package dialog also displays the permission, if the relevant check box is selected. The Inherited From cell value of the inherited permission is Model. |
| Replace all subpackages permissions with inheritable permissions from this package | Inheritable permissions of the package are those that apply to its subpackages as well.If the package, whose permissions you modify, has subpackages, you can choose to replace their individual permissions with those of the parent package. Make sure the appropriate permissions are set as inheritable and click to select the check box. |

##### Modify global permissions and review package permissions

You can use the**Package permissions**dialog to review the permissions set on all packages in a project. This dialog allows you to change the global permissions affecting all users for a project.You can also change or remove the user permission for a selected package.

To review package permissions

- From the Options main menu, select Package permissions . Package permissions dialog opens.

To modify package permissions

1. Open the Package permissions dialog as described above.
2. Click the value in the Permission cell of the Package permissions table set for the user/group and select:
  - Read-Only to restrict editing of the package for the selected user/group.
  - Read-Write to allow editing of the package for the selected user/group.
3. If you don't want to apply the same permission on the subpackages of this package, click the Apply To cell and select This package only . [ATTACHMENT filename='modify_package_permissions_2.png']

To modify global permissions

1. Open the Package permissions dialog as described above.
2. In the upper-right corner of the dialog, select the appropriate Global permission:

- 
  - To allow editing of the entire model, select **Read-Write**.
  - To restrict editing of the entire model, select **Read-Only**. Global permissions can be overridden by package permissions, e.g. Read-Only global permission can be overridden by a package with Read-Write permission. This allows the user/group to edit the package, whereas editing the rest of the model is restricted. [IMAGE alt='' src='']

To copy permissions

1. Open the Package permissions dialog as described above.
2. Select the permission you want to copy.
  - To select multiple permissions, hold down the Ctrl key and select the permissions.
  - To select all permissions, click Ctrl+A .
3. Copy the selected permissions using Ctrl+C .
4. Paste the permissions (e.g., to an Excel document.)

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="e4285057-09a6-4c94-a28f-0b2110c01478"><ac:parameter ac:name="id">1282481725</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="b18f25a3-b9e9-4303-b68f-3fdf49477140"><ac:parameter ac:name="id">1282481727</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="16b9344c-1019-44d6-921a-d2c500193040"><ac:parameter ac:name="id">1282481724</ac:parameter><ac:rich-text-body><p><strong>On this page</strong></p><p><strong><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="e98a7c99-8ff3-449d-880a-f727983f7885"><ac:parameter ac:name="minLevel">3</ac:parameter></ac:structured-macro><br /></strong></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="d40552c3-4caf-4c1d-aba2-7a68cbc3bc72"><ac:parameter ac:name="id">1282481726</ac:parameter><ac:rich-text-body><h3>Modify package permissions</h3><p>To modify the permissions of the package</p><hr /><ol><li><p>Right-click the package or its shape and select <strong>Permissions</strong>. The <strong>Permissions of Package</strong> dialog opens.</p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="01d23a2e-2a46-40a0-a29e-ce83a0a2ddc1"><ac:rich-text-body><p>The full name of the dialog depends on the selected package name. Thus, if you select to modify the permissions of the package <em>domain</em>, the <strong>Permissions of Package <ac:inline-comment-marker ac:ref="761c8cf7-22c7-4bdf-b1f4-a1997aa8ef03">domain</ac:inline-comment-marker></strong> dialog opens.</p></ac:rich-text-body></ac:structured-macro></li><li>Add new package permission:<br /><br /><ol><li>Click the <strong>Add</strong> button under the <strong>Package permissions</strong> table. The <strong>Select User/Group</strong> dialog opens.</li><li><p>Use the search bar to filter users or groups, then click to select the check box near the user or group name.</p><p><ac:image><ri:attachment ri:filename="selecting_a_user.png" /></ac:image><br /><br /></p></li><li>Click <strong>OK</strong> and see the new row appeared in the <strong>Package permissions</strong> table.</li><li>Click the <strong>Permission</strong> cell and select:<br /><br /><ul><li><strong>Read-Only</strong> to restrict editing of the package for the selected user/group.<strong><br /></strong></li><li><strong>Read-Write</strong> to allow editing of the package for the selected user/group.<br /><br /></li></ul></li><li>If you don't want to apply the same permission on the subpackages of this package, click the <strong>Apply To</strong> cell and select <strong>This package only</strong>.<br /><br /></li></ol></li><li>Add as many permissions as you need by repeating step 3.</li><li>Close the <strong>Permissions of Package</strong> dialog.</li></ol><h4>Inheritable permissions</h4><p>The <strong>Permissions of Package</strong> dialog includes a few options for handling inheritable permissions. The following table provides their descriptions.</p><table class="wrapped"><colgroup><col /><col /></colgroup><tbody><tr><th>Option</th><th>Description</th></tr><tr><td><p>Include inheritable permissions from the parent</p></td><td><div class="content-wrapper"><p><em>Inheritable permissions</em> of the package are those that apply to its subpackages as well.</p><p>By default, these permissions are displayed together with individual permissions of every subpackage, but cannot be <span>modified or deleted there</span>. If you want to hide them, click to clear the check box.</p><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="8eac208f-d6a3-4c7b-a6dd-e90474f33e2c"><ac:rich-text-body><p>Let's say you have a package <em>Model</em> and a subpackage <em>Requirements</em>.</p><p><span>If you set on the package <em>Model</em></span><span> the Read-Only permission for a certain user and leave the default setting to apply this permission on subpackages as well, the <strong>Permissions of Package </strong>dialog also displays the permission, if the relevant check box is selected. The</span><strong style="line-height: 1.42857;"> Inherited From</strong> cell value of the inherited permission is <em style="line-height: 1.42857;">Model</em>.</p><p><ac:image ac:title="Showing inheritable permissions of the parent package" ac:alt="Showing inheritable permissions of the parent package"><ri:attachment ri:filename="showing_inheritable_permissions.png" /></ac:image></p></ac:rich-text-body></ac:structured-macro></div></td></tr><tr><td>Replace all subpackages permissions with inheritable permissions from this package</td><td><p><em>Inheritable permissions</em><span> of the package are those that apply to its subpackages as well.</span></p><p><span>If the package, whose permissions you modify, has subpackages, you can choose to replace their individual permissions with those of the parent package. Make sure the appropriate permissions are set as inheritable and click to select the check box.<br /></span></p></td></tr></tbody></table><h3><span style="color: rgb(51,51,51);">Modify global permissions and r</span>eview package permissions</h3><p><span>You can use the </span><strong>Package permissions</strong><span> dialog to review the permissions set on all packages in a project. This dialog allows you to change the global permissions affecting all users for a project. </span>You can also change or remove the user permission for a selected package.</p><p><br /></p><p>To review package permissions</p><hr /><ul><li>From the <strong>Options</strong> main menu, select <strong>Package permissions</strong>. <strong>Package permissions</strong> dialog opens.</li></ul><p><br /></p><p>To modify package permissions</p><hr /><ol><li>Open the <strong>Package permissions</strong> dialog as described above.</li><li>Click the value in the <strong>Permission</strong> cell of the <strong>Package permissions</strong> table set for the user/group and select:<br /><br /><ul><li><strong>Read-Only</strong> to restrict editing of the package for the selected user/group.<strong><br /></strong></li><li><strong>Read-Write</strong> to allow editing of the package for the selected user/group.<br /><br /></li></ul></li><li>If you don't want to apply the same permission on the subpackages of this package, click the <strong>Apply To</strong> cell and select <strong>This package only</strong>.<ac:image ac:width="450"><ri:attachment ri:filename="modify_package_permissions_2.png" /></ac:image></li></ol><p><br /></p><p>To modify global permissions</p><hr /><ol><li>Open the <strong>Package permissions</strong> dialog as described above.</li><li>In the upper-right corner of the dialog, select the appropriate Global permission:</li></ol><ul><li style="list-style-type: none;background-image: none;"><ul><li><p>To allow editing of the entire model, select <strong>Read-Write</strong>.</p></li><li><p>To restrict editing of the entire model, select <strong>Read-Only</strong>.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="afaaa1d8-38fb-48c1-836a-c5b1e355cf34"><ac:rich-text-body><p>Global permissions can be overridden by package permissions, e.g. Read-Only global permission can be overridden by a package with Read-Write permission. This allows the user/group to edit the package, whereas editing the rest of the model is restricted.</p></ac:rich-text-body></ac:structured-macro><p><ac:image ac:width="450"><ri:attachment ri:filename="setting_global_permission_2.png" /></ac:image></p></li></ul></li></ul><p>To copy permissions</p><hr /><ol><li>Open the <strong>Package permissions</strong> dialog as described above.</li><li>Select the permission you want to copy.<ul><li>To select multiple permissions, hold down the <strong>Ctrl</strong> key and select the permissions.</li><li>To select all permissions, click <strong>Ctrl+A</strong>.</li></ul></li><li>Copy the selected permissions using <strong>Ctrl+C</strong>.</li><li>Paste the permissions (e.g., to an Excel document.)</li></ol></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=243969687 space=CM version=2 -->
## PAGE 00309: Single Sign-On Authentication

- page_id: `243969687`
- space_key: `CM`
- source_url: https://docs.nomagic.com/spaces/CM/pages/243969687/Single+Sign-On+Authentication
- version_number: 2
- version_date: `2025-09-12T12:45:40.515+02:00`
- ancestors: Client-Side Collaborative Modeling Documentation > Using Teamwork Cloud > Starting a collaboration session
- labels: []

### NORMALIZED CONTENT

854241299

854241301

854241300

The Single Sign-On (SSO) property is available to log on to a Teamwork Cloud server. For now, you can log using SAML authentication (e.g., ForgeRock, Ping, WSO2). And for you it means:

- No need to remember and type credentials each time you logging to a server.
- No issues about weak passwords and updating it.

[IMAGE alt='' src='']

###### Logging to Teamwork Cloud using SSO.

SSO implementation is based on the [JxBrowser platform](https://www.teamdev.com/jxbrowser), andis supported by following OS:

- Windows (32-bit & 64-bit)
  - Windows 10
  - Windows 8 & 8.1
  - Windows 7
  - Windows Server 2008 R2
  - Windows Server 2012
  - Windows Server 2016
- Linux (32-bit & 64-bit)
  - Ubuntu 12.04+
  - Debian 7.7+
  - Fedora 20
  - openSUSE 13.1
  - RedHat Enterprise Linux 7

- macOS (64-bit)
  - macOS 10.9.x - 10.12.x

For more information about supported OS, please refer to [JxBrowser](https://www.teamdev.com/jxbrowser)[system requirements](https://jxbrowser-support.teamdev.com/docs/guides/introduction/requirements.html).

854241298

**Related pages**

- [CONFLUENCE_PAGE title='Authentication server' space='MCS']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="9646be3e-9113-415f-b631-8ca713353516"><ac:parameter ac:name="id">854241299</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="41dce372-43bd-40e3-b4f0-41e98eee99f9"><ac:parameter ac:name="id">854241301</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="02bde3c1-1e6b-4614-916c-3c135f4df1cc"><ac:parameter ac:name="id">854241300</ac:parameter><ac:rich-text-body><p>The Single Sign-On (SSO) property is available to log on to a Teamwork Cloud server. For now, you can log using SAML authentication (e.g., ForgeRock, Ping, WSO2). And for you it means:</p><ul><li>No need to remember and type credentials each time you logging to a server.</li><li>No issues about weak passwords and updating it.</li></ul><p><br /></p><p><ac:image ac:align="center"><ri:attachment ri:filename="login_TWC.png" /></ac:image></p><h6 style="text-align: center;">Logging to Teamwork Cloud using SSO.</h6><p>SSO implementation is based on the <span><a href="https://www.teamdev.com/jxbrowser">JxBrowser platform</a>, and </span>is supported by following OS:</p><ul><li><strong>Windows (32-bit &amp; 64-bit)</strong><ul><li><span>Windows 10</span></li><li>Windows 8 &amp; 8.1</li><li>Windows 7</li><li>Windows Server 2008 R2</li><li>Windows Server 2012</li><li><p class="auto-cursor-target">Windows Server 2016</p></li></ul></li><li><strong>Linux (32-bit &amp; 64-bit)</strong><ul><li>Ubuntu 12.04+</li><li>Debian 7.7+</li><li>Fedora 20</li><li>openSUSE 13.1</li><li>RedHat Enterprise Linux 7<br /><br /></li></ul></li></ul><ul><li><strong>macOS (64-bit)</strong><ul><li>macOS 10.9.x - 10.12.x</li></ul></li></ul><p>For more information about supported OS, please refer to <a href="https://www.teamdev.com/jxbrowser">JxBrowser</a><a href="https://jxbrowser-support.teamdev.com/docs/guides/introduction/requirements.html"> system requirements</a>.</p><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="3e2ec0f8-1104-400f-b46f-4a0381b6a0f6"><ac:parameter ac:name="id">854241298</ac:parameter><ac:rich-text-body><p class="auto-cursor-target"><strong>Related pages</strong></p><ul><li><ac:link><ri:page ri:space-key="MCS" ri:content-title="Authentication server" /><ac:plain-text-link-body><![CDATA[Administrating the authentication server]]></ac:plain-text-link-body></ac:link></li></ul><p class="auto-cursor-target"><br /></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=243969680 space=CM version=4 -->
## PAGE 00310: Starting a collaboration session

- page_id: `243969680`
- space_key: `CM`
- source_url: https://docs.nomagic.com/spaces/CM/pages/243969680/Starting+a+collaboration+session
- version_number: 4
- version_date: `2025-09-12T13:19:34.120+02:00`
- ancestors: Client-Side Collaborative Modeling Documentation > Using Teamwork Cloud
- labels: []

### NORMALIZED CONTENT

Before logging in to any server, you must:

- Have a user account on the server.
- Be sure the server is running.

To log in to a server

1. From the Collaborate menu, select Login . The Login dialog opens.
2. Log in to a server. If you have [CONFLUENCE_PAGE title='Managing LDAP servers' space='MCS'] and imported users from LDAP using Teamwork Cloud Admin, you can use either internal or imported users to log in to Teamwork Cloud.
  - To login using "username/password" authentication:
  1. 
    1. Click the Login tab.
    2. Type your user name and password. 
[IMAGE alt='' src='']
  - For users having a single ID and password for multiple software systems (valid only for Teamwork Cloud Server):
  1. 
    1. Click the [CONFLUENCE_PAGE title='Single Sign-On Authentication' space=''] tab. [ATTACHMENT filename='SSO_login.png']
3. Provide the server name (address). If you need to specify a server port, type < *server* name> : *<port number>* , for example *10.2.2.47:3579* . If you prefer to have only a Single Sign On login option, you can enable it by adding an argument to the properties file of the modeling tool:Go to *<modeling tool installation directory>/bin* and open the properties file of your modeling tool.In the *JAVA_ARGS* line, add the *-Dhide.login.tab=true*argument. 
[IMAGE alt='' src='']
4. If you want the client application to remember your credentials and automatically log in to the server next time upon starting the client application, select the Auto Login to Server check box.
5. If you need to connect to the server using the SSL connection, select the **Use Secured Connection (SSL)** check box. The SSL connection must be established on both the server and the client side.
6. Click **OK**.
7. Wait while you are connected to the server, and then you can start performing collaborative tasks.

To log out of the server

- From the Collaborate menu, select Logout .

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="e67a8f13-9562-4c07-850c-f655e23f0fd5"><ac:rich-text-body><p>Before logging in to any server, you must:</p><ul><li>Have a user account on the server.</li><li>Be sure the server is running.</li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><span>To log in to a server </span></p><hr /><ol><li>From the <strong>Collaborate</strong> menu, select <strong>Login</strong>. The <strong>Login</strong> dialog opens.</li><li><p class="auto-cursor-target"><span style="letter-spacing: 0.0px;">Log in to a server.</span></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="73015aac-0e32-452f-889a-f6f2567a63f5"><ac:rich-text-body><p>If you have <ac:link><ri:page ri:space-key="MCS" ri:content-title="Managing LDAP servers" /><ac:plain-text-link-body><![CDATA[set up an LDAP connection]]></ac:plain-text-link-body></ac:link> and imported users from LDAP using Teamwork Cloud Admin, you can use either internal or imported users to log in to Teamwork Cloud<span style="color:var(--ds-text,#172b4d);">.</span></p></ac:rich-text-body></ac:structured-macro><ul><li>To login using &quot;username/password&quot; authentication:</li></ul><ol><li style="list-style-type: none;background-image: none;"><br /><ol><li>Click the <strong>Login </strong>tab.</li><li><p class="auto-cursor-target">Type your user name and password.<br /><ac:image><ri:attachment ri:filename="login_dialog.png" /></ac:image><br /><br /></p><p class="auto-cursor-target"><br /></p></li></ol></li></ol><ul><li>For users having a <span style="color:var(--ds-text,#333333);">single ID and password for multiple software systems (valid only for Teamwork Cloud Server):</span></li></ul><ol><li style="list-style-type: none;background-image: none;"><br /><ol><li><span style="letter-spacing: 0.0px;color:var(--ds-text,#333333);">Click the </span><strong style="letter-spacing: 0.0px;color:var(--ds-text,#333333);"> <ac:link><ri:page ri:content-title="Single Sign-On Authentication" /><ac:plain-text-link-body><![CDATA[Single Sign On]]></ac:plain-text-link-body></ac:link> </strong><span style="letter-spacing: 0.0px;color:var(--ds-text,#333333);">tab.<br /></span><ac:image><ri:attachment ri:filename="SSO_login.png" /></ac:image><br /><br /><br /></li></ol></li></ol></li><li><p class="auto-cursor-target"><span>Provide the server name (address). If you need to specify a server port, type &lt;</span> <em>server </em> <span>name&gt; :</span> <em> &lt;port number&gt;</em> <span>, for example </span> <em>10.2.2.47:3579</em> <span>.</span></p><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="12355897-be7d-49eb-a3ec-358f9cc2c80f"><ac:rich-text-body><p>If you prefer to have only a Single Sign On login option, you can enable it by <span style="color:var(--ds-text,#333333);">adding an argument to the properties file of the modeling tool:</span></p><ol><li><span>Go to </span> <em>&lt;modeling tool installation directory&gt;/bin</em> <span> and open the properties file of your modeling tool.</span></li><li><span>In the <em>JAVA_ARGS</em> line, add the <em>-Dhide.login.tab=true </em>argument.</span> <br /><span> <ac:image><ri:attachment ri:filename="single_sign_on_properties.png" /></ac:image> </span> <span> <br /></span></li></ol></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></li><li>If you want the client application to remember your credentials and automatically log in to the server next time upon starting the client application, select the <strong>Auto Login to Server</strong> check box.</li><li><p>If you need to connect to the server using the SSL connection, select the <strong>Use Secured Connection (SSL)</strong> check box.</p><ac:structured-macro ac:name="warning" ac:schema-version="1" ac:macro-id="30e5d2b8-300e-4478-bcde-657ac7931eb6"><ac:rich-text-body><p>The SSL connection must be established on both the server and the client side.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></li><li><p class="auto-cursor-target">Click <strong>OK</strong>.</p></li><li><p>Wait while you are connected to the server, and then you can start performing collaborative tasks.</p></li></ol><p><br /></p><p>To log out of the server</p><hr /><ul><li>From the <strong>Collaborate</strong> menu, select <strong>Logout</strong>.</li></ul></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=243970024 space=CM version=2 -->
## PAGE 00311: Stop using the project in your project

- page_id: `243970024`
- space_key: `CM`
- source_url: https://docs.nomagic.com/spaces/CM/pages/243970024/Stop+using+the+project+in+your+project
- version_number: 2
- version_date: `2025-09-11T15:22:52.624+02:00`
- ancestors: Client-Side Collaborative Modeling Documentation > Using Teamwork Cloud > Managing project usages
- labels: []

### NORMALIZED CONTENT

To stop using the project in your project, you must have the [**Administer Resources** permission](https://docs.nomagic.com/MCS/?contextKey=permissions&version=latest&variant=default).

If you no longer need to use a project, you can easily remove it from your project usages.

Removal can be:

- Complete, after which all references to the elements stored in the used project are eliminated.
- Incomplete, after which all references are preserved. Choose this method when you need to replace the used project with an equivalent project containing the same elements with slightly different content.

Before you attempt to stop using a project, make sure other users are not currently creating usages to this project.

To stop using a project in your project

1. [CONFLUENCE_PAGE title='Locking model for edit' space=''] you want to stop using.
2. On the main menu, click Collaborate > Project Usages > Project Usages .
3. Select the used project and click the [IMAGE alt='' src=''] button. Shortcut menuThis step can be done via shortcut menu. Right-click project and then select **Remove**.**** [IMAGE alt='' src='']
4. Wait while the removal completes.
5. Click OK .

The project is no longer used in your project. It will disappear from the Model Browser of your project.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="660e2072-9c67-4bfd-a314-4d8ce037351b"><ac:rich-text-body><p>To stop using the project in your project, you must have the <a href="https://docs.nomagic.com/MCS/?contextKey=permissions&amp;version=latest&amp;variant=default"><strong>Administer Resources</strong> permission</a>.</p></ac:rich-text-body></ac:structured-macro><p>If you no longer need to use a project, you can easily remove it from your project usages.</p><p>Removal can be:</p><ul><li>Complete, after which all references to the elements stored in the used project are eliminated.</li><li>Incomplete, after which all references are preserved. Choose this method when you need to replace the used project with an equivalent project containing the same elements with slightly different content.</li></ul><p><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="1bc44b2c-e21f-4931-96fe-ba85a84166b3"><ac:rich-text-body><p>Before you attempt to stop using a project, make sure other users are not currently creating usages to this project.</p></ac:rich-text-body></ac:structured-macro><p><br /></p><p>To stop using a project in your project</p><hr /><ol><li><ac:link><ri:page ri:content-title="Locking model for edit" /><ac:plain-text-link-body><![CDATA[Lock the used project]]></ac:plain-text-link-body></ac:link> you want to stop using.</li><li>On the main menu, click <strong> Collaborate</strong> &gt; <strong>Project Usages</strong> &gt; <strong>Project Usages</strong>.</li><li><p class="auto-cursor-target">Select the used project and click the <ac:image ac:thumbnail="true" ac:height="17"><ri:attachment ri:filename="remove_button.png"><ri:page ri:space-key="MT" ri:content-title="_MD buttons" /></ri:attachment></ac:image> button.</p><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="ac0e76a5-8ae3-4829-8bdb-a3a08b2944bf"><ac:parameter ac:name="title">Shortcut menu</ac:parameter><ac:rich-text-body><p>This step can be done via shortcut menu. Right-click project and then select <strong>Remove</strong>.<strong> </strong></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /><ac:image><ri:attachment ri:filename="project_usages_remove.png" /></ac:image></p></li><li>Wait while the removal completes.</li><li>Click <strong>OK</strong>.</li></ol><p>The project is no longer used in your project. It will disappear from the Model Browser of your project.</p>
````

<!--NOMAGIC_PAGE id=243970151 space=CM version=2 -->
## PAGE 00312: Teamwork Cloud data markings

- page_id: `243970151`
- space_key: `CM`
- source_url: https://docs.nomagic.com/spaces/CM/pages/243970151/Teamwork+Cloud+data+markings
- version_number: 2
- version_date: `2025-09-12T12:45:42.752+02:00`
- ancestors: Client-Side Collaborative Modeling Documentation > Using Teamwork Cloud
- labels: []

### NORMALIZED CONTENT

Teamwork Cloud data markings help to classify resources with custom-defined access levels. They are shown if they were [CONFLUENCE_PAGE title='Managing data markings in Teamwork Cloud Admin' space='MCS'].

You may see Teamwork Cloud data markings when you:

- try to [CONFLUENCE_PAGE title='Opening Teamwork Cloud projects' space=''] ,
- want to [CONFLUENCE_PAGE title='Managing server projects' space=''] , or
- need to [CONFLUENCE_PAGE title='Managing project usages' space=''] in your project.

If set, Teamwork Cloud data markings are displayed in an appropriate column of a dialog:

###### [IMAGE alt='' src='']

###### Open Server Project dialog with Teamwork Cloud data markings.

If there is an access level set on a project and you want to use that project in your project, your project must have the same or more strict access level rights. Otherwise, you see a warning:

[IMAGE alt='' src='']

If you decide to use a used project with a stricter access level in your project, users must also have the same or stricter access level rights to be able to open your project.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>Teamwork Cloud data markings help to classify resources with custom-defined access levels. They are shown if they were <ac:link><ri:page ri:space-key="MCS" ri:content-title="Managing data markings in Teamwork Cloud Admin" /><ac:plain-text-link-body><![CDATA[enabled and created in Teamwork Cloud Admin]]></ac:plain-text-link-body></ac:link>.</p><p>You may see Teamwork Cloud data markings when you:</p><ul><li>try to <ac:link><ri:page ri:content-title="Opening Teamwork Cloud projects" /><ac:plain-text-link-body><![CDATA[open a server project from Teamwork Cloud]]></ac:plain-text-link-body></ac:link>,</li><li>want to <ac:link><ri:page ri:content-title="Managing server projects" /><ac:plain-text-link-body><![CDATA[manage a server project]]></ac:plain-text-link-body></ac:link>, or</li><li>need to <ac:link><ri:page ri:content-title="Managing project usages" /><ac:plain-text-link-body><![CDATA[ use a project ]]></ac:plain-text-link-body></ac:link>in your project.</li></ul><p>If set, Teamwork Cloud data markings are displayed in an appropriate column of a dialog:</p><h6><ac:image ac:align="center"><ri:attachment ri:filename="twc_data_markings.png" /></ac:image></h6><h6 style="text-align: center;">Open Server Project dialog with Teamwork Cloud data markings.</h6><p>If there is an access level set on a project and you want to use that project in your project, <ac:inline-comment-marker ac:ref="55676b24-9d82-4260-b1db-87d21b28b79a">your project</ac:inline-comment-marker> must have the same or more strict access level rights. Otherwise, you see a <ac:inline-comment-marker ac:ref="ad51715f-9f21-4817-b4be-692f914795d7">warning</ac:inline-comment-marker>:</p><p><ac:image ac:border="true" ac:height="156" ac:width="639"><ri:attachment ri:filename="data_markings_warning.png" /></ac:image></p><p><span style="color: rgb(62,63,64);">If you decide to use a used project with a stricter access level in your project, users must also have the same or stricter access level rights to be able to open your project.</span></p>
````

<!--NOMAGIC_PAGE id=286556218 space=CM version=1 -->
## PAGE 00313: Technical practices

- page_id: `286556218`
- space_key: `CM`
- source_url: https://docs.nomagic.com/spaces/CM/pages/286556218/Technical+practices
- version_number: 1
- version_date: `2026-01-21T06:57:42.803+01:00`
- ancestors: Client-Side Collaborative Modeling Documentation > Collaboration powered by 3DEXPERIENCE platform
- labels: []

### NORMALIZED CONTENT

In this section, you will find technical practices and recommendations for working with CATIA Magic Power'By.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><span style="color:var(--ds-text,#000000);">In this section, you will find technical practices and recommendations for working with CATIA Magic Power'By.</span></p><p><span style="color:var(--ds-text,#000000);"><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="7f6b0f4d-5460-4928-a8af-d29a464aaf6c" /></span></p>
````

<!--NOMAGIC_PAGE id=243970154 space=CM version=1 -->
## PAGE 00314: Troubleshooting

- page_id: `243970154`
- space_key: `CM`
- source_url: https://docs.nomagic.com/spaces/CM/pages/243970154/Troubleshooting
- version_number: 1
- version_date: `2025-07-31T10:51:45.075+02:00`
- ancestors: Client-Side Collaborative Modeling Documentation > Using Teamwork Cloud
- labels: []

### NORMALIZED CONTENT

**On this page**

4

##### Recovered Database Detected

If the current project version conflicts with the project version committed to the server earlier, and a recovered database is detected, then the following error message appears. Follow the instructions in the message or contact your system administrator to solve the issue.

[IMAGE alt='' src='']

###### *Recovered Database Detected*error message.

##### Waiting for Response

If the response from the server is taking too long due to time-consuming server-side tasks or client-server connectivity issues, then the following notification appears. Check your server status and network connectivity if the notification keeps popping up.

[IMAGE alt='' src='']

###### *Waiting For Response*notification.

##### Client-server communication

If the operation that requires a remote call to Teamwork Cloud is taking too long, you can analyze a .log file to learn how much time was spent processing the operation in the client and server side.

#### INFO: Where do I find a .log file?

Where do I find a .log file?

1. Open your modeling tool.
2. In the main menu, go to Help > About <modeling tool name> .
3. In the Environment tab, click the file path next to Log File to open a .log file.

##### **Measuring Network Latency**

*INFO NetworkPerformance - <operation name> latency <latency time>*

**Description**

The latency (i.e., the time it takes for the ping signal sent from the tool to the server to return) is measured for the following operations:

- Login
- Committing project to server
- Updating project
- Opening project

#### TIP: Example

Example

INFO NetworkPerformance - Login latency 1 ms

##### **Remote Operations Duration Statistics**

*INFO RemoteCallsAnalyzer - <operation name> all operations time <total operation time>*

*INFO RemoteCallsAnalyzer - <operation name> calls total time: <total time, spent in remote calls>, start count: <remote calls count>, failed count: <failed remote calls count>*

**Description**

The remote and local operations duration statistics are collected for the following operations:

- Updating from local project
- Opening Manage Projects dialog
- Opening Open Server Project dialog
- Updating project
- Committing changes to a server project
- Setting selected version as latest
- Cloning project
- Managing version properties
- Opening Teamwork Cloud project
- Renaming project
- Removing project
- Adding project to server
- Viewing element history
- Comparing projects
- Using server project
- Discarding changes
- Locking and unlocking elements/diagrams
- Changing used project version

#### TIP: Example

Example

- INFO RemoteCallsAnalyzer - Manage projects all operations time 9797 ms
- INFO RemoteCallsAnalyzer - Manage projects calls total time: 2293 ms, start count: 47, failed count: 0

##### Your locked elements were unlocked by another user

The following warning appears if project elements you locked were unlocked by another user:

[IMAGE alt='' src='']

###### Warning that your locked elements were unlocked by another user.

In such case, select **Cancel**in the warning and do the following:

1. [CONFLUENCE_PAGE title='Saving a local copy of Teamwork Cloud project' space=''] .
2. [CONFLUENCE_PAGE title='Updating a server project with local changes' space=''] with changes from the local .mdzip project you saved. During this process, choose to create a new branch from the locally exported version by selecting **Yes**in this dialog: [ATTACHMENT filename='new_branch.png'] This is necessary to ensure a successful merge of local and server changes that you have to perform in the next step.
3. [CONFLUENCE_PAGE title='Model Merge' space='MT'] from the new branch to the working branch.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p><strong>On this page</strong></p><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="d769dd04-55e2-45cb-b636-b5c880eb9990"><ac:parameter ac:name="maxLevel">4</ac:parameter></ac:structured-macro></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><h3>Recovered Database Detected</h3><p>If the current project version conflicts with the project version committed to the server earlier, and a recovered database is detected, then the following error message appears. Follow the instructions in the message or contact your system administrator to solve the issue.</p><p><ac:image ac:align="center"><ri:attachment ri:filename="recovered_database_detected_error_message.png" /></ac:image></p><h6 style="text-align: center;"><span style="color: rgb(128,128,128);"><em>Recovered Database Detected </em>error message.</span></h6><h3>Waiting for Response</h3><p>If the response from the server is taking too long due to time-consuming server-side tasks or client-server connectivity issues, then the following notification appears. Check your server status and network connectivity if the notification keeps popping up.</p><p><ac:image ac:align="center"><ri:attachment ri:filename="waiting_for_response_notification.png" /></ac:image></p><h6 style="text-align: center;"><em>Waiting For Response </em>notification.</h6><h3>Client-server communication</h3><p>If the operation that requires a remote call to Teamwork Cloud is taking too long, you can analyze a .log file to learn how much time was spent processing the operation in the client and server side.</p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="b5ed1840-62f0-4f20-bb47-ed1bf74175d5"><ac:parameter ac:name="title">Where do I find a .log file?</ac:parameter><ac:rich-text-body><ol><li><span style="color: rgb(62,63,64);">Open your modeling tool.</span></li><li><span style="color: rgb(62,63,64);">In the main menu, go to </span><strong>Help</strong><span style="color: rgb(62,63,64);"> &gt; </span><strong>About &lt;modeling tool name&gt;</strong><span style="color: rgb(62,63,64);">. </span></li><li><span style="color: rgb(62,63,64);">In the </span><strong>Environment</strong><span style="color: rgb(62,63,64);"> tab, click the file path next to </span><strong>Log File </strong><span style="color: rgb(62,63,64);">to open a .log file.</span></li></ol></ac:rich-text-body></ac:structured-macro><h3><strong style="font-size: 16.0px;letter-spacing: -0.006em;">Measuring Network Latency</strong></h3><p><em>INFO  NetworkPerformance - &lt;operation name&gt; latency &lt;latency time&gt; </em></p><p><strong>Description</strong></p><p>The latency (i.e., the time it takes for the ping signal sent from the tool to the server to return) is measured for the following operations:</p><ul><li>Login</li><li>Committing project to server</li><li>Updating project</li><li>Opening project<br /><br /></li></ul><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="d03b1a64-de21-4176-a03c-8d524734cafc"><ac:parameter ac:name="title">Example</ac:parameter><ac:rich-text-body><p><span>INFO  NetworkPerformance - Login latency 1 ms</span></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><h3><strong>Remote Operations Duration Statistics</strong></h3><p><em>INFO  RemoteCallsAnalyzer - &lt;operation name&gt; all operations time &lt;total operation time&gt;</em></p><p><em>INFO  RemoteCallsAnalyzer - &lt;operation name&gt; calls total time: &lt;total time, spent in remote calls&gt;, start count: &lt;remote calls count&gt;, failed count: &lt;failed remote calls count&gt;</em></p><p><strong>Description</strong></p><p>The remote and local operations duration statistics are collected for the following operations:</p><ul><li>Updating from local project</li><li>Opening<strong> Manage Projects</strong> dialog</li><li>Opening <strong>Open Server Project</strong> dialog</li><li>Updating project</li><li>Committing changes to a server project</li><li>Setting selected version as latest</li><li>Cloning project</li><li>Managing version properties</li><li>Opening Teamwork Cloud project</li><li>Renaming project</li><li>Removing project</li><li>Adding project to server</li><li>Viewing element history</li><li>Comparing projects</li><li>Using server project</li><li>Discarding changes</li><li>Locking and unlocking elements/diagrams</li><li>Changing used project version<br /><br /></li></ul><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="9da75f01-2dd6-410b-9c6d-e1823fae7e91"><ac:parameter ac:name="title">Example</ac:parameter><ac:rich-text-body><ul><li>INFO  RemoteCallsAnalyzer - Manage projects all operations time 9797 ms</li><li>INFO  RemoteCallsAnalyzer - Manage projects calls total time: 2293 ms, start count: 47, failed count: 0</li></ul></ac:rich-text-body></ac:structured-macro><h3 class="auto-cursor-target">Your locked elements were unlocked by another user</h3><p>The following warning appears if project elements you locked were unlocked by another user:</p><p style="text-align: left;"><ac:image ac:align="center" ac:height="150"><ri:attachment ri:filename="elements_unlocked_by_another_user.png" /></ac:image></p><h6 style="text-align: center;"> Warning that your locked elements were unlocked by another user.</h6><p>In such case, select <strong>Cancel </strong>in the warning and do the following:</p><ol><li><ac:link><ri:page ri:content-title="Saving a local copy of Teamwork Cloud project" /><ac:plain-text-link-body><![CDATA[Save your project locally to .mdzip file]]></ac:plain-text-link-body></ac:link>.</li><li><ac:link><ri:page ri:content-title="Updating a server project with local changes" /><ac:plain-text-link-body><![CDATA[Update the project on the server]]></ac:plain-text-link-body></ac:link> with changes from the local .mdzip project you saved. During this process, choose to <span style="color: rgb(51,51,51);">create a new branch from the locally exported version by selecting <strong>Yes </strong>in this dialog:<br /></span><ac:image ac:height="152"><ri:attachment ri:filename="new_branch.png" /></ac:image><br />This is necessary to ensure a successful merge of local and server changes that you have to perform in the next step.</li><li><ac:link><ri:page ri:space-key="MT" ri:content-title="Model Merge" /><ac:plain-text-link-body><![CDATA[Merge the changes]]></ac:plain-text-link-body></ac:link> from the new branch to the working branch.</li></ol></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=243970226 space=CM version=2 -->
## PAGE 00315: Troubleshooting server project file import issues

- page_id: `243970226`
- space_key: `CM`
- source_url: https://docs.nomagic.com/spaces/CM/pages/243970226/Troubleshooting+server+project+file+import+issues
- version_number: 2
- version_date: `2025-09-12T12:45:43.018+02:00`
- ancestors: Client-Side Collaborative Modeling Documentation > Collaboration powered by 3DEXPERIENCE platform > Disconnected team collaboration
- labels: []

### NORMALIZED CONTENT

##### Cannot import projects from one 3DEXPERIENCE platform to another 3DEXPERIENCE platform

If you cannot import a server project file from one **3D**EXPERIENCE platform to another, ensure that the target server already has the same version of the standard profiles used by the source project. If you receive a message about missing standard profiles during the import, add the required profiles to the target server and try again.

You can only add standard profiles to the **3D**EXPERIENCE platform if one of the following conditions are met:

- No standard profiles exist in the platform, and you can add them as new projects.
- The standard profiles you want to add are of a later version than the profiles already stored in the platform. In this case, you can migrate the existing profiles to a later version (to match the version of the project you want to import).

If the standard profiles you want to add are of an earlier version than those already stored in the platform, you must upgrade your modeling tool and the project to match the profile version stored in the target platform before the import.

##### Cannot import projects from Teamwork Cloud to the 3DEXPERIENCE platform

If you cannot import a server project file from Teamwork Cloud to the **3D**EXPERIENCE platform, make sure the exported projects meet the following criteria:

- Exported projects cannot have cyclic project usages. A cyclic project usage is the kind of usage where a project uses itself through other used projects and forms a usage loop. You can use the [CONFLUENCE_PAGE title='Resource Usage Map' space='MCS'] application to [CONFLUENCE_PAGE title='Identifying suspicious usages' space='MCS'] .
- Exported projects cannot have version conflicts in project usages. A version conflict occurs when a project uses different versions of the same project directly and through other used projects. [CONFLUENCE_PAGE title='Troubleshooting used project version conflicts' space=''].
- Exported projects cannot have recovered elements. A recovered element is an indication of a dangling reference. It means that a project has a reference to the element in a used project that can no longer be found. In this case, a modeling tool recovers the missing element to maintain model integrity. [CONFLUENCE_PAGE title='Managing unresolved references' space='MT'].
- Standard/system profiles used by exported projects (including used projects) must be imported to the 3D EXPERIENCE platform. [CONFLUENCE_PAGE title='Adding standard profiles to 3DEXPERIENCE platform' space='']Learn to add standard/system profiles to the **3D**EXPERIENCE platform .
- If you want to import a Teamwork Cloud project exported without used projects, all of these used projects must be already imported to the 3D EXPERIENCE platform (the versions of all used projects must match the used project versions on the platform).

### EXACT CONFLUENCE STORAGE SOURCE

````html
<h3><span>Cannot import projects from one 3DEXPERIENCE platform to another 3DEXPERIENCE platform</span></h3><p>If you cannot import a server project file from one <strong>3D</strong>EXPERIENCE platform to another, ensure that the target server already has the same version of the standard profiles used by the source project. If you receive a message about missing standard profiles during the import, <ac:inline-comment-marker ac:ref="45b85bb9-ebdd-4475-a6ed-532020015f4f">add the required profiles to the target server</ac:inline-comment-marker> and try again.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="005d8765-e3e7-44c4-93ef-5bf830429b77"><ac:rich-text-body><p>You can only add standard profiles to the <strong>3D</strong>EXPERIENCE platform if one of the following conditions are met:</p><ul><li>No standard profiles exist in the platform, and you can add them as new projects.</li><li>The standard profiles you want to add are of a later version than the profiles already stored in the platform. In this case, you can migrate the existing profiles to a later version (to match the version of the project you want to import).</li></ul><p>If the standard profiles you want to add are of an earlier version than those already stored in the platform, you must upgrade your modeling tool and the project to match the profile version stored in the target platform before the import.</p></ac:rich-text-body></ac:structured-macro><h3>Cannot import projects from Teamwork Cloud to the 3DEXPERIENCE platform</h3><p style="text-align: left;">If you cannot import a <ac:inline-comment-marker ac:ref="78ebb26c-4de7-4605-9d02-491e71aad4f7">server</ac:inline-comment-marker> project file from Teamwork Cloud to the <strong>3D</strong>EXPERIENCE platform, make sure the exported projects meet the following criteria: </p><ul style="text-align: left;"><li>Exported projects cannot have cyclic project usages.<br />A cyclic project usage is the kind of usage where a project <span style="color: rgb(62,63,64);">uses itself through other used projects and forms a usage loop.</span> You can use the <ac:link><ri:page ri:space-key="MCS" ri:content-title="Resource Usage Map" /></ac:link> application to <ac:link ac:anchor="Cyclic usages"><ri:page ri:space-key="MCS" ri:content-title="Identifying suspicious usages" /><ac:plain-text-link-body><![CDATA[identify cyclic project usages]]></ac:plain-text-link-body></ac:link>.<br /><br /></li><li>Exported projects<strong> </strong>cannot have version conflicts in project usages.<br />A version conflict occurs when a project <span style="color: rgb(62,63,64);">uses different versions of the same project directly and through other used projects. <ac:link><ri:page ri:content-title="Troubleshooting used project version conflicts" /><ac:plain-text-link-body><![CDATA[Learn to troubleshoot used project version conflicts]]></ac:plain-text-link-body></ac:link>.<br /><br /></span></li><li>Exported projects cannot have recovered elements.<br />A recovered element is an indication of a dangling reference. It means that a project has a reference to the element <span style="color: rgb(23,43,77);">in a used project that can no longer be found. In this case, a modeling tool recovers the missing element to maintain model integrity. <ac:link><ri:page ri:space-key="MT" ri:content-title="Managing unresolved references" /><ac:plain-text-link-body><![CDATA[Learn to resolve dangling references]]></ac:plain-text-link-body></ac:link>.<br /><br /></span></li><li>Standard/system profiles used by exported projects (including used projects) must be imported to the <strong>3D</strong>EXPERIENCE platform. <ac:link><ri:page ri:content-title="Adding standard profiles to 3DEXPERIENCE platform" /><ac:link-body>Learn to add standard/system profiles to the <strong>3D</strong>EXPERIENCE platform</ac:link-body></ac:link>.<br /><br /></li><li>If you want to import a Teamwork Cloud project exported without used projects, all of these used projects must be already imported to the <strong>3D</strong>EXPERIENCE platform (the versions of all used projects must match the used project versions on the platform).</li></ul>
````

<!--NOMAGIC_PAGE id=243970035 space=CM version=1 -->
## PAGE 00316: Troubleshooting used project version conflicts

- page_id: `243970035`
- space_key: `CM`
- source_url: https://docs.nomagic.com/spaces/CM/pages/243970035/Troubleshooting+used+project+version+conflicts
- version_number: 1
- version_date: `2025-07-31T10:51:42.724+02:00`
- ancestors: Client-Side Collaborative Modeling Documentation > Using Teamwork Cloud > Managing project usages
- labels: []

### NORMALIZED CONTENT

When the same used project is used multiple times in the same project, either directly or through another used project, inconsistencies may happen. Version conflicts are detected if a project uses multiple versions of the same used project.

**An example**

You have projects: A, B and C. Project A uses both project B andversion #1 of project C. However, project B also uses project C, only the version #3. This means that project A uses version #1 and version #3 (through project B) of project C, causing inconsistencies between the used versions of project C.

To check used project version inconsistencies

1. From the main menu, select Collaborate > Project Usages > Project Usages .
2. Select a used project on the left pane.
3. On the right side of the dialog, Version line displays the version of the used project.
4. When there are version inconsistencies, [IMAGE alt='' src=''] icon is displayed. Hover over it to see the used project version inconsistencies warning.

[IMAGE alt='' src='']

In the example above, you can see project Car version #1 used directly in Project Vehicle and project Car version #3 used in Project Vehicle through project Wheel.

The term #1/3 denotes that 1 is the used version and 3 is the latest version.

##### Used project version selection

When an inconsistency is detected, the tool selects one single version of the same used project to be used and displayed in the main project according to the following rules:

- The shortest usage path to the used project.

**Usage path**

When the same used project A is used multiple times in the main project, it can be done either by using the used project A directly in the main project, or by using other used projects (e.g. B, C, D, etc.) that use the used project A themselves. This determines the usage path to the used project A. The version of a used project that is used directly has the shortest usage path in comparison to a version of a used project used through another project. To review usage paths of used project's versions:

1. Open [CONFLUENCE_PAGE title='Configure used projects' space=''] dialog.
2. Click the [ATTACHMENT filename='project_usage_information.png'] button. Project Usage Information dialog opens.

[IMAGE alt='' src='']

Here you can see that the project Car is used twice in the Project Vehicle. The first usage of project Car is nested within Project Vehicle directly, while the second usage is nested within project Wheel. This means that the version of project Car that is nested the least of all the other usages is the one with the shortest usage path. Consequently, the more nested the used project, the longer the usage path to it is.

- If there are multiple shortest usage paths to the used project, the one that was used first will be the one selected for usage.

##### Resolving used project version inconsistencies

Used project version needs to be [CONFLUENCE_PAGE title='Configure used projects' space=''] in order to resolve used project version inconsistencies.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>When the same used project is used multiple times in the same project, either directly or through another used project, inconsistencies may happen. <ac:inline-comment-marker ac:ref="c433a4c8-ef1b-46e8-b0bb-4f2f494bb775">Version conflicts are detected if a project uses multiple versions of the same used project.</ac:inline-comment-marker></p><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="e3a0dcfb-6ad3-49d2-83fe-42e304edc48c"><ac:rich-text-body><p><strong>An example</strong></p><p>You have projects: A, B and C. Project A uses both <span>project B and </span>version #1 of project C. However, project B also uses project C, only the version #3. This means that project A uses version #1 and version #3 (through project B) of project C, causing inconsistencies between the used versions of project C.</p></ac:rich-text-body></ac:structured-macro><p>To check used project version inconsistencies</p><hr /><ol><li><span style="color: rgb(51,51,51);">From the main menu, select </span><strong style="color: rgb(51,51,51);letter-spacing: 0.0px;">Collaborate</strong><span style="color: rgb(51,51,51);"> &gt; </span><strong style="color: rgb(51,51,51);letter-spacing: 0.0px;">Project Usages</strong><span style="color: rgb(51,51,51);"> &gt; </span><strong style="color: rgb(51,51,51);letter-spacing: 0.0px;">Project Usages</strong><span style="color: rgb(51,51,51);">.</span></li><li>Select a used project on the left pane. </li><li>On the right side of the dialog, <strong>Version</strong> line displays the version of the used project.</li><li><span>When there are version inconsistencies, <ac:image><ri:attachment ri:filename="used_project_inconsistencies_alert_icon.png" /></ac:image> icon is displayed. Hover over it </span><span>to see the used project version inconsistencies warning.</span></li></ol><p><ac:image><ri:attachment ri:filename="used_project_inconsistencies.png" /></ac:image></p><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="2697b4ef-c299-452f-a059-2895b57d804d"><ac:rich-text-body><p>In the example above, you can see project Car version #1 used directly in Project Vehicle and project Car version #3 used in Project Vehicle through project Wheel.</p><p>The term #1/3 denotes that 1 is the used version and 3 is the latest version.</p></ac:rich-text-body></ac:structured-macro><h3>Used project version selection</h3><p><span style="letter-spacing: 0.0px;">When an inconsistency is detected, the tool selects one single version of the same used project to be used and displayed in the main project according to the following rules:</span></p><ul><li>The <ac:inline-comment-marker ac:ref="67c00151-aad0-4507-9569-f9743792da6f">shortest usage path</ac:inline-comment-marker> to the used project. </li></ul><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="70f1cc20-af3c-4f16-8755-b3d5c0794238"><ac:rich-text-body><p><strong>Usage path</strong></p><p>When the same used project A is used multiple times in the main project, it can be done either by using the used project A directly in the main project, or by using other used projects (e.g. B, C, D, etc.) that use the used project A themselves. This determines the usage path to the used project A. The version of a used project that is used directly has the shortest usage path in comparison to a version of a used project used through another project. To review usage paths of used project's versions:</p><ol><li>Open <ac:link><ri:page ri:content-title="Configure used projects" /><ac:plain-text-link-body><![CDATA[Advanced Project Usages Configuration]]></ac:plain-text-link-body></ac:link><span style="color: rgb(62,63,64);"> dialog.</span></li><li>Click the <ac:image ac:thumbnail="true" ac:height="20"><ri:attachment ri:filename="project_usage_information.png" /></ac:image><span style="color: rgb(62,63,64);"> button. </span><strong style="color: rgb(62,63,64);letter-spacing: 0.0px;">Project Usage Information </strong><span style="color: rgb(62,63,64);">dialog opens.</span></li></ol><p><span style="color: rgb(62,63,64);"><ac:image><ri:attachment ri:filename="Project_Usage_Information_details.png" /></ac:image><br /></span></p><p><span style="color: rgb(62,63,64);">Here you can see that the project Car is used twice in the Project Vehicle. The first usage of project Car is nested within Project Vehicle directly, while the second usage is nested within project Wheel. This means that the version of project Car that is nested the least of all the other usages is the one with the shortest usage path. Consequently, the more nested the used project, the longer the usage path to it is.</span></p></ac:rich-text-body></ac:structured-macro><ul><li>If there are multiple shortest usage paths to the used project, the one that was used first will be the one selected for usage.</li></ul><h3>Resolving used project version inconsistencies</h3><p>Used project version needs to be <ac:link><ri:page ri:content-title="Configure used projects" /><ac:plain-text-link-body><![CDATA[changed manually]]></ac:plain-text-link-body></ac:link> in order to resolve used project version inconsistencies.</p><p class="auto-cursor-target"><br /></p>
````

<!--NOMAGIC_PAGE id=243970094 space=CM version=1 -->
## PAGE 00317: Understanding changes

- page_id: `243970094`
- space_key: `CM`
- source_url: https://docs.nomagic.com/spaces/CM/pages/243970094/Understanding+changes
- version_number: 1
- version_date: `2025-07-31T10:51:43.487+02:00`
- ancestors: Client-Side Collaborative Modeling Documentation > Using Teamwork Cloud > Used Project Switch Impact Analysis
- labels: []

### NORMALIZED CONTENT

The following definitions show the different change types.

**Addition change** 
In the context of used project impact analysis, an addition change is treated to be the one when an element is restored from a recovered state to a normal one. Such element change is represented in the green rectanglein the **Affected elements** panel.

**Deletion change** 
If an element has been removed, a deletion change occurs. The deletion change usually results in composition integrity errors, i.e., it causes the appearance of recovered elements, since the deleted element is still used in the main project.

**Modification change** 
If an element property has been modified, a modification change occurs.

**Understanding element marking**

When a change occurs on a single element, the element marking indicates the state of the change which can be either accepted or rejected.

| Marking | Change state | Example |
| --- | --- | --- |
| (green tick before the element icon) | Accepted | A new element had been created in one of the contributors and its addition was accepted. |
| (red cross before the element icon) | Rejected | A new element had been created in one of the contributors and its addition was rejected. |

To understand the concept of change states, refer to [CONFLUENCE_PAGE title='Understanding change concept' space='MT'].

Elements with resolved conflicting changes are decorated as shown in the following table. Owners of these elements are also decorated.

| Marking | Change applied by | Example |
| --- | --- | --- |
| (red diamond on the lower-left corner of the element icon) | System | The element had a conflicting modification change which was resolved automatically. |
| (yellow diamond on the lower-left corner of the element icon) | User | The element had a conflicting modification change which was resolved by the user. |

**Recognizing addition changes**

For the addition change description, refer to [CONFLUENCE_PAGE title='Understanding change concept' space='MT'].

Added elements are highlighted in green background. 
 
[IMAGE alt='' src='']

**Recognizing deletion changes**

For the deletion change description, refer to [CONFLUENCE_PAGE title='Understanding change concept' space='MT'].

Deleted elements are highlighted in red background.

[IMAGE alt='' src='']

****

**Recognizing modification changes**

For the modification change description, refer to [CONFLUENCE_PAGE title='Understanding change concept' space='MT'].

Elements whose properties have been changed are highlighted in blue. 
[IMAGE alt='' src=''] 
 
To see what properties have been modified, click the element and see changes in the **Specification** panel.

For more information about using the Specification panel, see [CONFLUENCE_PAGE title='Inspecting changes in the Change details panel' space='MT'].

**Recognizing movement changes**

For the movement change description, refer to [CONFLUENCE_PAGE title='Understanding change concept' space='MT'].

Elements with movement changes are highlighted in the same blue background that is used to highlight modification changes. Since movement changes are some kind of modification changes. Icon of an element with movement changes is represented with an arrow symbol on the left.

The following figure illustrates a movement change, when element X has been moved from package A to package B. The movement change had been accepted and element X became owned by package B.

[IMAGE alt='' src='']

You can navigate from the element original location to the new one (and vice versa) using the commands on the element shortcut menu.

**Recognizing order changes**

For the order change description, refer to [CONFLUENCE_PAGE title='Understanding change concept' space='MT'].

Elements with order changes are highlighted in the same blue background that is used to highlight modification changes, since order changes are some kind of modification changes. 
After accepting the change, all the elements in the collection are reordered so that it would be the same as in one of the contributors.

[IMAGE alt='' src='']

You can turn off the order changes detection. For more about it, see [CONFLUENCE_PAGE title='Finishing and canceling merge' space='MT']

**Recognizing elements with changed owned elements** 
Elements whose owned elements (in any nesting level) have changes are highlighted using red diagonals.

[IMAGE alt='' src='']

Modified elements with changed owned elements are highlighted in blue with red diagonals.

[IMAGE alt='' src='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><span style="color: rgb(51,51,51);">The following definitions show the different change types. </span></p><p><span style="color: rgb(51,51,51);"><strong>Addition change</strong></span><br /><span style="color: rgb(51,51,51);">In the context of used project impact analysis, an addition change is treated to be the one when an element is restored from a recovered state to a normal one. Such element change is represented in the green rectangle</span><span style="color: rgb(51,51,51);"> in the <strong>Affected elements</strong> panel.<br /></span></p><p><span style="color: rgb(51,51,51);"><strong>Deletion change</strong></span><br /><span style="color: rgb(51,51,51);">If an element has been removed, a deletion change occurs. The deletion change <span style="color: rgb(62,63,64);">usually results in composition integrity errors, i.e., it causes the appearance of recovered elements, since the deleted element is still used in the main project.</span><br /></span></p><p><span style="color: rgb(51,51,51);"><strong>Modification change</strong></span><br /><span style="color: rgb(51,51,51);">If an element property has been modified, a modification change occurs.</span></p><p><br /></p><p><span style="color: rgb(51,51,51);"><strong>Understanding element marking</strong></span></p><p>When a change occurs on a single element, the element marking indicates the state of the change which can be either accepted or rejected.</p><table><colgroup><col /><col /><col /></colgroup><tbody><tr><th><p>Marking</p></th><th><p><strong>Change state</strong></p></th><th><p><strong>Example</strong></p></th></tr><tr><td><div class="content-wrapper"><p><ac:image><ri:attachment ri:filename="green_tick.png" /></ac:image> <br class="atl-forced-newline" /> (green tick before the element icon)</p></div></td><td><p>Accepted</p></td><td><div class="content-wrapper"><p><ac:image><ri:attachment ri:filename="accepted_change.png" /></ac:image> <br class="atl-forced-newline" /> A new element had been created in one of the contributors and its addition was accepted.</p></div></td></tr><tr><td><div class="content-wrapper"><p><ac:image><ri:attachment ri:filename="red_cross.png" /></ac:image> <br class="atl-forced-newline" /> (red cross before the element icon)</p></div></td><td><p>Rejected</p></td><td><div class="content-wrapper"><p><ac:image><ri:attachment ri:filename="rejected_change.png" /></ac:image> <br class="atl-forced-newline" /> A new element had been created in one of the contributors and its addition was rejected.</p></div></td></tr></tbody></table><p><br />To understand the concept of change states, refer to <ac:link ac:anchor="changestates"><ri:page ri:space-key="MT" ri:content-title="Understanding change concept" /><ac:plain-text-link-body><![CDATA[Change states]]></ac:plain-text-link-body></ac:link>.</p><p>Elements with resolved conflicting changes are decorated as shown in the following table. Owners of these elements are also decorated.</p><table><colgroup><col /><col /><col /></colgroup><tbody><tr><th><p><strong>Marking</strong></p></th><th><p><strong>Change applied by</strong></p></th><th><p><strong>Example</strong></p></th></tr><tr><td><div class="content-wrapper"><p><ac:image><ri:attachment ri:filename="red_diamond.png" /></ac:image> <br class="atl-forced-newline" /> (red diamond on the lower-left corner of the element icon)</p></div></td><td><p>System</p></td><td><div class="content-wrapper"><p><ac:image><ri:attachment ri:filename="change_owner_system.png" /></ac:image> <br class="atl-forced-newline" /> The element had a conflicting modification change which was resolved automatically.</p></div></td></tr><tr><td><div class="content-wrapper"><p><ac:image><ri:attachment ri:filename="yellow_diamond.png" /></ac:image> <br class="atl-forced-newline" /> (yellow diamond on the lower-left corner of the element icon)</p></div></td><td><p>User</p></td><td><div class="content-wrapper"><ac:image><ri:attachment ri:filename="change_owner_user.png" /></ac:image> <span> </span><p>The element had a conflicting modification change which was resolved by the user.</p></div></td></tr></tbody></table><p><br /></p><p><span style="color: rgb(51,51,51);"><strong>Recognizing addition changes</strong></span></p><p>For the addition change description, refer to <ac:link ac:anchor="additionchange"><ri:page ri:space-key="MT" ri:content-title="Understanding change concept" /><ac:plain-text-link-body><![CDATA[Addition change]]></ac:plain-text-link-body></ac:link>.</p><p>Added elements are highlighted in green background.<br /><br class="atl-forced-newline" /><ac:image ac:title="Example of accepted addition change" ac:alt="Example of accepted addition change"><ri:attachment ri:filename="accepted_addition.png" /></ac:image></p><p><br class="atl-forced-newline" /><span style="color: rgb(51,51,51);"><strong>Recognizing deletion changes</strong></span></p><p>For the deletion change description, refer to <ac:link ac:anchor="deletionchange"><ri:page ri:space-key="MT" ri:content-title="Understanding change concept" /><ac:plain-text-link-body><![CDATA[Deletion change]]></ac:plain-text-link-body></ac:link>.</p><p><span style="color: rgb(129,137,156);"><span style="color: rgb(51,51,51);">Deleted elements are highlighted in red background.</span></span></p><p><span style="color: rgb(129,137,156);"><span style="color: rgb(51,51,51);"><ac:image ac:title="Example of deletion change" ac:alt="Example of deletion change"><ri:attachment ri:filename="deletion_change.png" /></ac:image><br /></span></span></p><p><span style="color: rgb(129,137,156);"><strong><br /></strong></span></p><p><span style="color: rgb(51,51,51);"><strong>Recognizing modification changes</strong></span></p><p>For the modification change description, refer to <ac:link ac:anchor="modificationchange"><ri:page ri:space-key="MT" ri:content-title="Understanding change concept" /><ac:plain-text-link-body><![CDATA[Modification change]]></ac:plain-text-link-body></ac:link>.</p><p>Elements whose properties have been changed are highlighted in blue. <br class="atl-forced-newline" /><ac:image><ri:attachment ri:filename="element_modified_properties.png" /></ac:image> <br /><br />To see what properties have been modified, click the element and see changes in the <strong>Specification</strong> panel.</p><p>For more information about using the Specification panel, see <ac:link><ri:page ri:space-key="MT" ri:content-title="Inspecting changes in the Change details panel" /></ac:link>.</p><p><br class="atl-forced-newline" /><span style="color: rgb(51,51,51);"><strong>Recognizing movement changes</strong></span></p><p>For the movement change description, refer to <ac:link ac:anchor="movementchange"><ri:page ri:space-key="MT" ri:content-title="Understanding change concept" /><ac:plain-text-link-body><![CDATA[Movement change]]></ac:plain-text-link-body></ac:link>.</p><p>Elements with movement changes are highlighted in the same blue background that is used to highlight modification changes. Since movement changes are some kind of modification changes. Icon of an element with movement changes is represented with an arrow symbol on the left.</p><p>The following figure illustrates a movement change, when element X has been moved from package A to package B. The movement change had been accepted and element X became owned by package B.</p><p><ac:image ac:title="Example of accepted movement change" ac:alt="Example of accepted movement change"><ri:attachment ri:filename="accepted_movement_change.png" /></ac:image></p><p>You can navigate from the element original location to the new one (and vice versa) using the commands on the element shortcut menu.</p><p><br class="atl-forced-newline" /><br class="atl-forced-newline" /><span style="color: rgb(51,51,51);"><strong>Recognizing order changes</strong></span></p><p>For the order change description, refer to <ac:link ac:anchor="orderc"><ri:page ri:space-key="MT" ri:content-title="Understanding change concept" /><ac:plain-text-link-body><![CDATA[Order change]]></ac:plain-text-link-body></ac:link>.</p><p>Elements with order changes are highlighted in the same blue background that is used to highlight modification changes, since order changes are some kind of modification changes. <br class="atl-forced-newline" />After accepting the change, all the elements in the collection are reordered so that it would be the same as in one of the contributors.</p><p><ac:image ac:title="Example of accepted order change" ac:alt="Example of accepted order change"><ri:attachment ri:filename="example_order_change.png" /></ac:image></p><p>You can turn off the order changes detection. For more about it, see <ac:link ac:anchor="diagramannotationson"><ri:page ri:space-key="MT" ri:content-title="Finishing and canceling merge" /><ac:plain-text-link-body><![CDATA[Turning on showing merged diagram annotations.]]></ac:plain-text-link-body></ac:link></p><p><br class="atl-forced-newline" /><span style="color: rgb(51,51,51);"><strong>Recognizing elements with changed owned elements</strong> </span><br class="atl-forced-newline" />Elements whose owned elements (in any nesting level) have changes are highlighted using red diagonals.</p><p><ac:image ac:title="Element with owned elements added" ac:alt="Element with owned elements added"><ri:attachment ri:filename="owned-elements-added.png" /></ac:image></p><p><br class="atl-forced-newline" />Modified elements with changed owned elements are highlighted in blue with red diagonals.</p><p><ac:image ac:title="Element with owned elements added and modification change" ac:alt="Element with owned elements added and modification change"><ri:attachment ri:filename="modified-owned-elements.png" /></ac:image></p><p><br /></p>
````

<!--NOMAGIC_PAGE id=243969802 space=CM version=3 -->
## PAGE 00318: Understanding differences in local and server project structure

- page_id: `243969802`
- space_key: `CM`
- source_url: https://docs.nomagic.com/spaces/CM/pages/243969802/Understanding+differences+in+local+and+server+project+structure
- version_number: 3
- version_date: `2025-09-12T12:41:17.858+02:00`
- ancestors: Client-Side Collaborative Modeling Documentation > Using Teamwork Cloud > Collaboration between disconnected teams > Using local project file format
- labels: []

### NORMALIZED CONTENT

The structure of your model may change when switching back and forth between local and server projects. Usually, this happens when the local project is added to the server, the server project is saved locally, or the server project is updated with local changes.

##### From Teamwork Cloud to local project****

- When the Teamwork Cloud project containing used projects is saved locally, packages from used projects are mounted under the model root ( [ATTACHMENT filename='model_root.png'] ) and marked with the [ATTACHMENT filename='shared_package_icon.png'] (shared package) symbol. The original model structure (as it is in the server project) cannot be maintained due to model architecture limitations, i.e., the absence of the dedicated root node for used projects.

[IMAGE alt='' src='']

- In the local environment, only shared packages will be visible in the used project. Therefore, if the used project contains elements under the model root, a new package **<userProjectName>_shared** is created when you save the project to make it possible to share those elements.

[IMAGE alt='' src='']

##### From local project to Teamwork Cloud

##### Mount relationshipMount relationship

- The Mount relationship may be created when the server project containing used projects is saved locally, modified, and then added back to the server.

It is used to recreate the same structure of the Containment tree as it was originally in the local project. This may be important for features that use a defined scope of the model. Only elements from used projects that are mounted under the Model root ([IMAGE alt='' src='']) or any of its packages are considered part of the model scope (when no used projects are set as the scope).

In general, the Mount relationship enables you to create a visual copy/representation of the chosen package in any place in the model.

[IMAGE alt='' src='']

- You can delete Mount relationships from your project if, for example, you do not want to have duplicate packages in the Containment tree of your server project.

Deleting Mount relationships may affect diagrams, elements or other options that require specifying the scope since packages from used projects will no longer be under the main project model root (they will still be available under**Project Usages**).

If you do not want Mount relationships to be created by default, remove the tick from the **Maintain Mount Points of Used Projects** check box in the **Update from Local Project** (**Collaborate** >**Update from Local Project**) dialog.

[IMAGE alt='' src='']

Packages from used projects mounted under the model root or any of its packages via the [CONFLUENCE_PAGE title='Managing used projects' space='MT'] dialog are kept in their original locations by using Mount relationships. They are automatically created once the project is added to the server.

##### Project Usages

The root node **Project Usages** is created in the Containment tree in Teamwork Cloud projects to list all used projects. The entire used project version is visible in the project. 
[IMAGE alt='' src='']

##### Symbols used

| Symbol | Description |
| --- | --- |
|  | Indicates that a package belonging to the used project is shared. |
|  | Indicates that a shared package belongs to the opened project. |
| // | Indicates that there is a package/profile/model from the used project in the Teamwork Cloud project. |
|  | Packages from used projects have the project name they come from written in brackets. |

For additional markings that can be displayed in used projects, refer to pages[CONFLUENCE_PAGE title='Moving elements to other projects' space='']and[CONFLUENCE_PAGE title='Working with partially loaded projects' space='MT'].

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>The structure of your model may change when switching back and forth between local and server projects. Usually, this happens when the local project is added to the server, the server project is saved locally, or the server project is updated with local changes. </p><h3>From Teamwork Cloud to local project<strong> </strong></h3><ul><li data-uuid="33e0854c-1f66-4a48-a9db-b46d57aa7ac5">When the Teamwork Cloud project containing used projects is saved locally, packages from used projects are mounted under the model root (<ac:image ac:thumbnail="true" ac:height="14"><ri:attachment ri:filename="model_root.png" /></ac:image>) and marked with the<ac:image ac:thumbnail="true" ac:height="16"><ri:attachment ri:filename="shared_package_icon.png" /></ac:image>(shared package) symbol. The original model structure (as it is in the server project) cannot be maintained due to model architecture limitations, i.e., the absence of the dedicated root node for used projects. </li></ul><p style="margin-left: 30.0px;"><ac:image><ri:attachment ri:filename="projects_saved_from_TWC.png" /></ac:image></p><ul><li data-uuid="7e9b1ac1-33a8-45c6-9133-ccc47200555f"><span style="color:var(--ds-text,#333333);">In the local environment, only shared packages will be visible in the used project. Therefore, if the used project contains elements under the model root, a new package <strong>&lt;userProjectName&gt;_shared</strong> is created when you save the project to make it possible to share those elements.</span></li></ul><p style="margin-left: 30.0px;"><ac:image><ri:attachment ri:filename="shared_package_local_project.png" /></ac:image></p><h3>From local project to Teamwork Cloud</h3><h3><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="76d4a847-02b7-4dc5-907a-75b1d70be9f7"><ac:parameter ac:name="">Mount relationship</ac:parameter></ac:structured-macro>Mount relationship</h3><ul><li class="auto-cursor-target" data-uuid="e07d2dc1-a8da-4dc8-b4b9-10738dccca14">The<strong> Mount </strong>relationship may be created when the server project containing used projects is saved locally, modified, and then added back to the server.</li></ul><p class="auto-cursor-target" style="margin-left: 30.0px;">It is used to recreate the same structure of the Containment tree as it was originally in the local project. This may be important for features that use a defined scope of the model. Only elements from used projects that are mounted under the Model root (<ac:image><ri:attachment ri:filename="model_root.png" /></ac:image>) or any of its packages are considered part of the model scope (when no used projects are set as the scope).</p><p class="auto-cursor-target" style="margin-left: 30.0px;">In general, the Mount relationship enables <span style="color:var(--ds-text,#333333);">you to create a visual copy/representation of the chosen package in any place in the model.</span></p><p class="auto-cursor-target"><ac:image><ri:attachment ri:filename="mount_relationship.png" /></ac:image></p><ul><li data-uuid="81ed02b5-1b27-4f07-8cba-34d038941890">You can delete <strong>Mount</strong> relationships from your project if, for example, you do not want to have duplicate packages in the Containment tree of your server project.</li></ul><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="a69c4c22-8dbd-4c8e-bce7-93fa1c38a819"><ac:rich-text-body><p><span style="color:var(--ds-text,#333333);">Deleting Mount relationships may affect diagrams, elements or other options that require specifying the scope since packages from used projects will no longer be under the main project model root (they will still be available under<strong> Project Usages</strong>).</span></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="5a49365a-6ab0-4377-9adc-ccf5eb9f5f70"><ac:rich-text-body><p>If you do not want Mount relationships to be created by default, remove the tick from the <strong>Maintain Mount Points of Used Projects</strong> check box in the <strong>Update from Local Project</strong> (<strong>Collaborate</strong> &gt;<strong> Update from Local Project</strong>) dialog.</p><p><ac:image ac:align="center"><ri:attachment ri:filename="update_from_local_project_dialog_structure_drift.png" /></ac:image></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="13f56158-dbd8-4c87-99ac-f99ed1985c54"><ac:rich-text-body><p>Packages from used projects mounted under the model root or any of its packages via the <ac:link><ri:page ri:space-key="MT" ri:content-title="Managing used projects" /><ac:plain-text-link-body><![CDATA[Used Projects]]></ac:plain-text-link-body></ac:link> dialog are kept in their original locations by using Mount relationships. They are automatically created once the project is added to the server.</p></ac:rich-text-body></ac:structured-macro><h3>Project Usages</h3><p>The root node <strong>Project Usages</strong> is created in the Containment tree in Teamwork Cloud projects to list all used projects. The entire used project version is visible in the project.<br /><ac:image><ri:attachment ri:filename="project_usages_package_TWC.png" /></ac:image></p><h3>Symbols used</h3><table class="relative-table" style="width: 840.0px;"><colgroup class=""><col class="" style="width: 0.0px;" /><col class="" style="width: 0.0px;" /></colgroup><tbody class=""><tr class=""><th>Symbol</th><th>Description</th></tr><tr class=""><td><div class="content-wrapper"><p><ac:image><ri:attachment ri:filename="shared_project_symbol.png" /></ac:image></p></div></td><td>Indicates that a package belonging to the used project is shared.</td></tr><tr class=""><td colspan="1"><div class="content-wrapper"><p><ac:image><ri:attachment ri:filename="shared_package_yellow_hand.png" /></ac:image></p></div></td><td colspan="1">Indicates that a shared package belongs to the opened project.</td></tr><tr class=""><td><div class="content-wrapper"><p><ac:image><ri:attachment ri:filename="used_project_icon_TWC.png" /></ac:image>/<ac:image><ri:attachment ri:filename="shared_model_TWC.png" /></ac:image>/<ac:image><ri:attachment ri:filename="shared_model_.png" /></ac:image></p></div></td><td>Indicates that there is a package/profile/model from the used project in the Teamwork Cloud project.</td></tr><tr class=""><td><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:height="18"><ri:attachment ri:filename="brackets_next_to_project_name_TWC.png" /></ac:image></p></div></td><td>Packages from used projects have the project name they come from written in brackets.</td></tr></tbody></table><p><span><span style="color:var(--ds-text,#000000);">For additional markings that can be displayed in used projects, refer to pages </span><span style="color:var(--ds-text,#000000);"><ac:link><ri:page ri:content-title="Moving elements to other projects" /></ac:link></span><span style="color:var(--ds-text,#000000);"> and </span><span style="color:var(--ds-text,#000000);"><ac:link><ri:page ri:space-key="MT" ri:content-title="Working with partially loaded projects" /></ac:link></span><span style="color:var(--ds-text,#000000);">.</span></span></p>
````

<!--NOMAGIC_PAGE id=243970124 space=CM version=1 -->
## PAGE 00319: Understanding merge types in Teamwork Cloud

- page_id: `243970124`
- space_key: `CM`
- source_url: https://docs.nomagic.com/spaces/CM/pages/243970124/Understanding+merge+types+in+Teamwork+Cloud
- version_number: 1
- version_date: `2025-07-31T10:51:44.353+02:00`
- ancestors: Client-Side Collaborative Modeling Documentation > Using Teamwork Cloud > Model merge in Teamwork Cloud
- labels: []

### NORMALIZED CONTENT

#### CONTENT-LAYER: Example #5

651419100

#### CONTENT-COLUMN: Example #5

651419114

651419095

**On this page**

**4**

#### CONTENT-BLOCK: Example #5

651419104

The 3-way merge is the default method used to merge selected Teamwork Cloud projects; the ancestor version is calculated automatically depending on the selected ancestor calculation algorithm. Once the correct ancestor for the two selected project versions is calculated, the **[CONFLUENCE_PAGE title='Analyzing and managing merge results' space='MT']** dialog opens.

You need to [CONFLUENCE_PAGE title='Model merge in Teamwork Cloud' space=''] from the **Tools** (**Tools** > **Project Merge**) menu to be able to change the ancestor selection (**Lowest Common Parent** or**Branch Point**) for the model merge. By default, **Lowest Common Parent**is considered an ancestor of the selected project versions.

##### Lowest Common Parent (Default)

If **Lowest Common Parent** is selected, the lowest common version for both the Target and Source is considered an ancestor. The lowest common parent of two revisions of the Source and Target in a directed acyclic graph is the nearest revision that has both the Target and Source as descendants. The algorithm considers both the direct parent path and the merged path when traversing and searching for the lowest common parent. In other words, during the repeated merge, the Contributor from the Source that was participating in the last merge is considered to be the common ancestor.

As shown in the image below, version #1 is considered to be a common parent during the first merge between versions #4 and #5. During the second merge between version #7 and #8, we traverse graphs back until we find the common parent for #7 and #8, which, in this case, is #4.

[IMAGE alt='' src='']

###### Visual representation of the model merge when Lowest Common Parent is considered an ancestor

##### Branch Point

If **Branch Point** is selected, the version from which the branches separate is considered an ancestor. As shown in the image below, version #1 is considered an ancestor in the first (version #4 is merged with version #3) and subsequent merges (version #6 is merged with version #5).

[IMAGE alt='' src='']

###### Visual representation of the model merge when Branch Point is considered an ancestor

Both ancestor calculation algorithms work in an identical way during the very first merge of the selected branches because the same ancestor is taken during the very first merge, no matter if the Branch Point or the Lowest Common Parent is specified. However, it is crucial to understand the importance of the ancestor selection during subsequent merges because the changes may differ greatly from those you expect to see (see examples below).

##### Repetitive merge

###### Lowest Common Parent

During the repeated merge, the Lowest Common Parent algorithm always chooses the latest merged Source version as the ancestor. Consequently, you do not need to review historical decisions made during previous merges.

#### TIP: Example #1

Example #1

You create a Class *Machine* in the Source branch and merge it with the Target (merge version #3 with version #4). Then continue your development process in the Source and rename *Machine* to *Washing Machine*. When you merge these two branches for the second time (merge version #6 with version #5), the algorithm recognizes that *Machine* was already created in the Target and Source, and, therefore, the only change that needs to be merged is renaming the Class *Machine* to *Washing Machine*.

[IMAGE alt='' src='']

On the other hand, the **Lowest Common Parent** calculation algorithm may cause confusion, since rejections from the Source branch are considered to be the inverted changes in the Target branch. For example, the created Class that was previously rejected in the Source will appear as a deletion in the Target. As a result, it may seem that some changes that are shown have never been made in the project.

#### TIP: Example #2

Example #2

You create two packages *Requirements* and *Design* in your**development branch (Source). You decide to do the merge but you know that the *Design* package is incomplete. Therefore, you reject the addition of this particular package and continue your merge with just the *Requirements* package. You continue your work with the *Design* of your system in the Source branch. When you are done, you decide to merge this package into the Target branch (merge version #6 with version #5). However, during the merge, you may notice that this *Design* package is shown as deleted in the Target (because it does not exist in the Target but exists in the selected ancestor). **In this case, you have to go through the Target changes and reject the deletion of this package to be able to add it.**

[IMAGE alt='' src='']

###### Branch Point

During the repeated merge, the branch point always compares the two branches as if they were developed completely separately and were never merged before. As a consequence, you can easily understand what changes have been made in the Source and Target since the branch creation. This eliminates any confusion that may occur in the case of the Lowest Common Parent algorithm and the rejected changes (see above).

#### TIP: Example #3

Example #3

You create two packages *(Requirements* and *Design)* in your development branch (Source). You decide to do the merge but you know that the *Design* package is incomplete. Therefore, you reject the addition of that particular package and continue your merge with just the *Requirements* package. Then you continue your work with the *Design* of your system in the Source branch. When you are done, you decide to merge this package into the Target branch. During the merge, you will see that the*Design* package is added and you will just carry on to merge it.

[IMAGE alt='' src='']

The default filter hides all the equivalent changes from Target and Source. Therefore, the creation of the *Requirements* package is hidden by default.

However, this algorithm has other drawbacks that can emerge if the elements that were already merged are edited.

#### TIP: Example #4

Example #4

You create a class *Machine* in the Source and merge it to the Target. Then you continue your work in the Source branch and decide to rename it to *Washing Machine*. If the Branch Point is specified as an ancestor, you have to solve the conflict of whether you want to keep the addition of a Class *Washing Machine* or *Machine,* because neither of these Classes existed in the branch point (the version from which the branch was created). This may require a lot of manual work since you will have to make sure that the conflicting changes are resolved in the desired direction.

[IMAGE alt='' src='']

##### Set as Latest

###### Lowest Common Parent

If an earlier version of the project is set to the latest version in the Target branch, e.g., version #8 is reverted to version #7 (version #9 is created), the ancestor is calculated taking the version that was set as the latest (version #7). If there is a preceding merge (version #3 is merged with version #4), the Source version from the last merge (version #3) is considered the ancestor; however, if no merges precede the version that was set as the latest, the version where the branch splits off the trunk (version #1) is considered the ancestor.

#### TIP: Example #5

Example #5

[IMAGE alt='' src='']

###### Branch Point

If an earlier version of the project is set to the latest version in the Target branch, e.g., version #8 is reverted to version #7 (version #9 was created), and then the merge of the two selected project versions occurs, the version from which the branches separate (i.e., a branch point) is considered an ancestor (version #1 in the image above).

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="3d2c546e-2c68-4e67-83fc-94ff4ecedee8"><ac:parameter ac:name="id">651419100</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="5530dd98-0290-4a21-9c1f-7dbe24fa6426"><ac:parameter ac:name="id">651419114</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="d5858a8f-fa92-4ec5-b5d7-5cf520618fda"><ac:parameter ac:name="id">651419095</ac:parameter><ac:rich-text-body><p><strong>On this page</strong></p><p><strong><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="02e21f4b-373d-4984-9fed-37d76d1b88bb"><ac:parameter ac:name="maxLevel">4</ac:parameter></ac:structured-macro><br class="_mce_tagged_br" /></strong></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="b16676d4-522c-4f33-ad5c-ff6a8c97be92"><ac:parameter ac:name="id">651419104</ac:parameter><ac:rich-text-body><p>The 3-way merge is the default method used to merge selected Teamwork Cloud projects; <span>the ancestor version is calculated automatically depending on the selected ancestor calculation algorithm</span>. Once the correct ancestor for the two selected project versions is calculated, the <strong><ac:link><ri:page ri:space-key="MT" ri:content-title="Analyzing and managing merge results" /><ac:plain-text-link-body><![CDATA[Merge]]></ac:plain-text-link-body></ac:link></strong> dialog opens.</p><ac:structured-macro ac:name="warning" ac:schema-version="1" ac:macro-id="8356b88c-b487-4918-914d-0498c165fa9a"><ac:rich-text-body><p>You need to <ac:link><ri:page ri:content-title="Model merge in Teamwork Cloud" /><ac:plain-text-link-body><![CDATA[start the model merge]]></ac:plain-text-link-body></ac:link> from the <strong>Tools</strong> (<strong>Tools</strong> &gt; <strong>Project Merge</strong>) menu to be able to change the ancestor selection (<strong>Lowest Common Parent</strong> or<strong> Branch Point</strong>) for the model merge. By default, <strong>Lowest Common Parent </strong>is considered an ancestor of the selected project versions.</p></ac:rich-text-body></ac:structured-macro><h3>Lowest Common Parent (Default)</h3><p>If <strong>Lowest Common Parent</strong> is selected, the lowest common version for both the Target and Source is considered an ancestor. The lowest common parent of two revisions of the Source and Target in a directed acyclic graph is the nearest revision that has both the Target and Source as descendants. The algorithm considers both the direct parent path and the merged path when traversing and searching for the lowest common parent. In other words, during the repeated merge, the Contributor from the Source that was participating in the last merge is considered to be the common ancestor.</p><p>As shown in the image below, version #1 is considered to be a common parent during the first merge between versions #4 and #5. During the second merge between version #7 and #8, we traverse graphs back until we find the common parent for #7 and #8, which, in this case, is #4.</p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="lowest_common_parent_default.png" /></ac:image></p><h6 style="text-align: center;">Visual representation of the model merge when Lowest Common Parent is considered an ancestor</h6><h3>Branch Point</h3><p>If <strong>Branch Point</strong> is selected, the version from which the branches separate is considered an ancestor. As shown in the image below, version #1 is considered an ancestor in the first (version #4 is merged with version #3) and subsequent merges (version #6 is merged with version #5).  </p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="branch_point_calculation.png" /></ac:image></p><h6 style="text-align: center;">Visual representation of the model merge when Branch Point is considered an ancestor</h6><p>Both ancestor calculation algorithms work in an identical way during the very first merge of the selected branches because the same ancestor is taken during the very first merge, no matter if the Branch Point or the Lowest Common Parent is specified. However, it is crucial to understand the importance of the ancestor selection during subsequent merges because the changes may differ greatly from those you expect to see (see examples below).</p><p><br /></p><h3>Repetitive merge</h3><h4>Lowest Common Parent</h4><p>During the repeated merge, the Lowest Common Parent algorithm always chooses the latest merged Source version as the ancestor. Consequently, you do not need to review historical decisions made during previous merges.</p><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="d33ca22c-d9ad-46e9-875f-360497959b7f"><ac:parameter ac:name="title">Example #1</ac:parameter><ac:rich-text-body><p>You create a Class <em>Machine</em> in the Source branch and merge it with the Target (merge version #3 with version #4). Then continue your development process in the Source and rename <em>Machine</em> to <em>Washing Machine</em>. When you merge these two branches for the second time (merge version #6 with version #5), the algorithm recognizes that <em>Machine</em> was already created in the Target and Source, and, therefore, the only change that needs to be merged is renaming the Class <em>Machine</em> to <em>Washing Machine</em>. </p><p><ac:image ac:align="center"><ri:attachment ri:filename="lowest_common_parent_calculation_visualization.png" /></ac:image></p></ac:rich-text-body></ac:structured-macro><p>On the other hand, the <strong>Lowest Common Parent</strong> calculation algorithm may cause confusion, since rejections from the Source branch are considered to be the inverted changes in the Target branch. For example, the created Class that was previously rejected in the Source will appear as a deletion in the Target. As a result, it may seem that some changes that are shown have never been made in the project.</p><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="452b4ebc-4f6b-4650-8341-cac359924166"><ac:parameter ac:name="title">Example #2</ac:parameter><ac:rich-text-body><p>You create two packages <em>Requirements</em> and <em>Design</em> in your<em> </em><span>development branch (Source)</span>. You decide to do the merge but you know that the <em>Design</em> package is incomplete. Therefore, you reject the addition of this particular package and continue your merge with just the <em>Requirements</em> package. You continue your work with the <em>Design</em> of your system in the Source branch. When you are done, you decide to merge this package into the Target branch (merge version #6 with version #5). However, during the merge, you may notice that this <em>Design</em> package is shown as deleted in the Target (because it does not exist in the Target but exists in the selected ancestor). <strong>In this case, you have to <ac:inline-comment-marker ac:ref="bbc68dbb-7dea-4b87-a8a2-cbfbfb2d2356">go through the Target changes</ac:inline-comment-marker> and reject the deletion of this package to be able to add it.</strong></p><p><ac:image ac:align="center"><ri:attachment ri:filename="lowest_common_parent_calculation_drawback_during_repetitive_merge.png" /></ac:image></p></ac:rich-text-body></ac:structured-macro><h4>Branch Point</h4><p>During the repeated merge, the branch point always compares the two branches as if they were developed completely separately and were never merged before. As a consequence, you can easily understand what changes have been made in the Source and Target since the branch creation. This eliminates any confusion that may occur in the case of the Lowest Common Parent algorithm and the rejected changes (see above).</p><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="ebc74f75-8181-4314-8b85-738a253caeeb"><ac:parameter ac:name="title">Example #3</ac:parameter><ac:rich-text-body><p>You create two packages <em>(Requirements</em> and <em>Design)</em> in your development branch (Source). You decide to do the merge but you know that the <em>Design</em> package is incomplete. Therefore, you reject the addition of that particular package and continue your merge with just the <em>Requirements</em> package. Then you continue your work with the <em>Design</em> of your system in the Source branch. When you are done, you decide to merge this package into the Target branch. During the merge, you will see that the<em> Design</em> package is added and you will just carry on to merge it.</p><p><ac:image ac:align="center"><ri:attachment ri:filename="branch_point_calculation_during_repetitive_merge.png" /></ac:image></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="39baed23-6c4d-41b6-9331-fa4af0516162"><ac:rich-text-body><p>The default filter hides all the equivalent changes from Target and Source. Therefore, the creation of the <em>Requirements</em> package is hidden by default. </p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro><p>However, this algorithm has other drawbacks that can emerge if the elements that were already merged are edited.</p><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="1cd8d182-66cb-4799-9ee8-376a3d5a8203"><ac:parameter ac:name="title">Example #4</ac:parameter><ac:rich-text-body><p>You create a class <em>Machine</em> in the Source and merge it to the Target. Then you continue your work in the Source branch and decide to rename it to <em>Washing Machine</em>. If the Branch Point is specified as an ancestor, you have to solve the conflict of whether you want to keep the addition of a Class <em>Washing Machine</em> or <em>Machine,</em> because neither of these Classes existed in the branch point (the version from which the branch was created). This may require a lot of manual work since you will have to make sure that the conflicting changes are resolved in the desired direction.</p><p><ac:image ac:align="center"><ri:attachment ri:filename="branch_point_drawback_visualization.png" /></ac:image></p></ac:rich-text-body></ac:structured-macro><h3 class="auto-cursor-target">Set as Latest</h3><h4>Lowest Common Parent</h4><p><span style="color: rgb(62,63,64);">If an earlier version of the project is set to the latest version in the Target branch, e.g., version #8 is reverted to version #7 (version #9 is created), the ancestor is calculated taking the version that was set as the latest (version #7). If there is a preceding merge (version #3 is merged with version #4), the Source version from the last merge (version #3) is considered the ancestor; however, if no merges precede the version that was set as the latest, the version where the branch splits off the trunk (version #1) is considered the ancestor. </span></p><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="aa60f179-6ba0-46d1-996b-93d1a913e47a"><ac:parameter ac:name="title">Example #5</ac:parameter><ac:rich-text-body><p><ac:image ac:align="center"><ri:attachment ri:filename="set_as_latest_lowest_common_parent.png" /></ac:image></p></ac:rich-text-body></ac:structured-macro><h4>Branch Point</h4><p><span style="color: rgb(62,63,64);">If an earlier version of the project is set to the latest version in the Target branch, e.g., version #8 is reverted to version #7 (version #9 was created), and then the merge of the two selected project versions occurs, the version from which the branches separate (i.e., a branch point) is considered an ancestor (version #1 in the image above). </span></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=243969888 space=CM version=1 -->
## PAGE 00320: Unlocking model

- page_id: `243969888`
- space_key: `CM`
- source_url: https://docs.nomagic.com/spaces/CM/pages/243969888/Unlocking+model
- version_number: 1
- version_date: `2025-07-31T10:51:39.017+02:00`
- ancestors: Client-Side Collaborative Modeling Documentation > Using Teamwork Cloud > Using lock-based editing mode
- labels: []

### NORMALIZED CONTENT

Unlocking the model is useful in one of the following cases:

- After you choose to keep locks, when [CONFLUENCE_PAGE title='Committing changes to Teamwork Cloud' space=''] .
- If you [CONFLUENCE_PAGE title='Locking model for edit' space=''] , but haven't made any changes in the model.
- When you want to clean other user locks. To unlock other users' locks, you must have the **Project Locks Administrator** permission.

#### PANEL: On this page

On this page

##### Unlocking elements and diagrams

Elements and diagrams can be unlocked by using the commands from their shortcut menu. 
[IMAGE alt='' src='']

Elements can also be locked by clicking the Lock element for Edit button [IMAGE alt='' src=''] on their Specification window. 
[IMAGE alt='' src='']

The following table provides suggestions on what unlocking commands to use for different purposes.

| If you finished editing... | Do the following |
| --- | --- |
| Specification properties of a single element | Right-click either:This element in the Containment tree of Lock View tree on the Model Browser.A symbol of this element on a diagram pane.From the shortcut menu, select Lock > Unlock Element.ORDouble-click either:This element in the Containment tree of Lock View tree on the Model Browser.A symbol of this element on a diagram pane.In the Specification window, click the Unlock element button . |
| Specification properties of both an element and all the elements it contains (owns) | Right-click either:This element in the Containment tree of Lock View tree on the Model Browser.A symbol of this element on a diagram pane.From the shortcut menu, select Lock > Unlock Elements Recursively. |
| At least one of the following:Diagram representation properties (including diagram layout)Symbol properties of elements represented on that diagram pane | Right-click this diagram in the Containment tree of Lock View tree on the Model Browser.From the shortcut menu, select Lock > Unlock Diagram.ORRight-click a free space on this diagram pane.From the shortcut menu, select Lock Diagram > Unlock Diagram.Use this command after you have finished editing the diagram representation, but you still need to change the specification properties of the elements represented on that diagram pane. |
| At least one of the following:Diagram specification propertiesDiagram representation properties (including diagram layout)Properties of elements represented on that diagram paneSymbol properties of elements represented on that diagram pane | Right-click this diagram in the Containment tree of Lock View tree on the Model Browser.From the shortcut menu, select Lock > Unlock Diagram Content.ORRight-click a free space on this diagram pane.From the shortcut menu, select Lock Diagram > Unlock Diagram Content. |
| At least one of the following:Symbol properties of a single element represented on a diagram panePosition of the symbol on the diagram pane | Right-click the symbol of that element on a diagram pane.From the shortcut menu, select Lock > Unlock Element in Diagram. |

##### Unlocking elements locked by other users

Forced unlocking is helpful, when elements are left locked by the user who is currently unavailable.

For this you must have the **Project Locks Administrator** permission.

To unlock the elements locked by another user

1. From the Collaborate menu, select Unlock All .
2. If the message opens asking you to choose what to unlock, click Unlock All . The Commit Project to the Server dialog opens. [ATTACHMENT filename='unlock_elements_msg.png']
3. In the dialog, do the following:
  1. If there is a need, type a comment.
  2. Click Commit .

As a result, all the locks made by another user are released, and the changes he/she made are lost forever.

##### Unlocking symbol styles

Symbol styles can be unlocked via the **Lock View** tab or the **Project Options** dialog.

To unlock symbol styles via the **Lock View** tab

1. In the **Lock View** tab on the Model Browser, expand *Project Options*. Where is the Lock View tab?It is the last tab on the Model Browser. If the tab is closed, you can simply open. For this, select **Collaborate** > **View Locked Elements**.
2. Right-click Symbol Styles by <user name> and from the shortcut menu select Unlock > Commit . [ATTACHMENT filename='unlocking_symbol_styles.png']
3. In the Commit Project to the Server dialog do the following:
  1. If there is a need, type a comment.
  2. Click to clear the Keep Locks check box.
  3. Click Commit .

To unlock symbol styles via the**Project Options** dialog

1. Do either:
  - Select Options > Project .
  - In the **Lock View** tab on the Model Browser, right-click *Project Options* and from the shortcut menu, select **Symbol Styles**. Where is the Lock View tab?It is the last tab on the Model Browser. If the tab is closed, you can simply open. For this, select **Collaborate** > **View Locked Elements**.
2. In the Project Options dialog, click the Unlock button and then select Commit .
3. In the Commit Project to the Server dialog do the following:
  1. If there is a need, type a comment.
  2. Click to clear the Keep Locks check box.
  3. Click Commit .

##### Unlocking project usages

To unlock a used project

1. From the Options menu, select Project Usages . The Project Usages dialog opens.
2. Select a locked used project on the left side of the dialog.
3. Click the Edit button and then select Unlock > Commit . The Commit Project to the Server dialog opens.
4. In the dialog:
  1. Type a comment, if there is a need.
  2. Click to clear the Keep Locks check box.
  3. Click Commit .

##### Unlocking project structure

Project structure becomes locked during the [CONFLUENCE_PAGE title='Model Merge' space='MT'] operation. The lock is automatically released after the merged project is committed to the server.

However, the user who started the merge operation can release the lock manually as well.

To unlock the project structure manually

1. From the **File** menu, select **Project Properties**. The **Project Properties** dialog opens.
2. Click the **Unlock (locked by <user name>)** button, for example, **Unlock (locked by billybob)**. The **Commit Project to the Server** dialog opens.
3. In the dialog:
  1. Type a comment, if there is a need.
  2. Click to clear the Keep Locks check box.
  3. Click Commit .

Other users cannot unlock the project structure manually.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p>Unlocking the model is useful in one of the following cases:</p><ul><li>After you choose to keep locks, when <ac:link><ri:page ri:content-title="Committing changes to Teamwork Cloud" /><ac:plain-text-link-body><![CDATA[committing changes]]></ac:plain-text-link-body></ac:link>.</li><li>If you <ac:link><ri:page ri:content-title="Locking model for edit" /><ac:plain-text-link-body><![CDATA[locked the model]]></ac:plain-text-link-body></ac:link>, but haven't made any changes in the model.</li><li><p>When you want to clean other user locks.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="92b705bf-088c-4dbd-947d-e844199f5484"><ac:rich-text-body><p>To unlock other users' locks, you must have the <strong>Project Locks Administrator</strong> permission.</p></ac:rich-text-body></ac:structured-macro></li></ul></ac:layout-cell><ac:layout-cell><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="c9597455-0f2e-43b0-adc6-f617116cf911"><ac:parameter ac:name="title">On this page</ac:parameter><ac:rich-text-body><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="c87c5cc1-a73f-43d9-9872-c997ec56540b" /></p></ac:rich-text-body></ac:structured-macro></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><h3>Unlocking elements and diagrams</h3><p>Elements and diagrams can be unlocked by using the commands from their shortcut menu.<br /><ac:image ac:alt="Unlocking commands on the shortcut menu of the Package" ac:title="Unlocking commands on the shortcut menu of the Package"><ri:attachment ri:filename="unlocking_commands_on_shortcut_menu.png" /></ac:image></p><p> </p><p>Elements can also be locked by clicking the Lock element for Edit button <ac:image><ri:attachment ri:filename="lock_in_spec.png"><ri:page ri:space-key="MT" ri:content-title="_MD buttons" /></ri:attachment></ac:image> on their Specification window.<br /><ac:image ac:alt="Unlocking command in the element's Specification window" ac:title="Unlocking command in the element's Specification window"><ri:attachment ri:filename="unlocking_command_in_spec_window.png" /></ac:image></p><p> </p><p>The following table provides suggestions on what unlocking commands to use for different purposes.</p><table><tbody><tr><th>If you finished editing...</th><th>Do the following</th></tr><tr><td>Specification properties of a single element</td><td><ol><li>Right-click either:<ul><li>This element in the Containment tree of Lock View tree on the Model Browser.</li><li>A symbol of this element on a diagram pane.</li></ul></li><li>From the shortcut menu, select <strong>Lock</strong> &gt; <strong>Unlock Element</strong>.</li></ol><p>OR</p><ol><li>Double-click either:<ul><li>This element in the Containment tree of Lock View tree on the Model Browser.</li><li>A symbol of this element on a diagram pane.</li></ul></li><li>In the Specification window, click the Unlock element button <ac:image ac:alt="Unlock element" ac:title="Unlock element"><ri:attachment ri:filename="lock_in_spec.png"><ri:page ri:space-key="MT" ri:content-title="_MD buttons" /></ri:attachment></ac:image>.</li></ol></td></tr><tr><td>Specification properties of both an element and all the elements it contains (owns)</td><td><ol><li>Right-click either:<ul><li>This element in the Containment tree of Lock View tree on the Model Browser.</li><li>A symbol of this element on a diagram pane.</li></ul></li><li>From the shortcut menu, select <strong>Lock</strong> &gt; <strong>Unlock Elements Recursively</strong>.</li></ol></td></tr><tr><td><p>At least one of the following:</p><ul><li>Diagram representation properties (including diagram layout)</li><li>Symbol properties of elements represented on that diagram pane</li></ul></td><td><ol><li>Right-click this diagram in the Containment tree of Lock View tree on the Model Browser.</li><li>From the shortcut menu, select <strong>Lock</strong> &gt; <strong>Unlock Diagram</strong>.</li></ol><p>OR</p><ol><li>Right-click a free space on this diagram pane.</li><li>From the shortcut menu, select <strong>Lock Diagram</strong> &gt; <strong>Unlock Diagram</strong>.</li></ol><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="4e8dc0cf-95bd-41a3-b99b-83d125262e7b"><ac:rich-text-body><p>Use this command after you have finished editing the diagram representation, but you still need to change the specification properties of the elements represented on that diagram pane.</p></ac:rich-text-body></ac:structured-macro></td></tr><tr><td colspan="1"><p>At least one of the following:</p><ul><li>Diagram specification properties</li><li>Diagram representation properties (including diagram layout)</li><li>Properties of elements represented on that diagram pane</li><li>Symbol properties of elements represented on that diagram pane</li></ul></td><td colspan="1"><ol><li>Right-click this diagram in the Containment tree of Lock View tree on the Model Browser.</li><li>From the shortcut menu, select <strong>Lock</strong> &gt; <strong>Unlock Diagram Content</strong>.</li></ol><p>OR</p><ol><li>Right-click a free space on this diagram pane.</li><li>From the shortcut menu, select <strong>Lock Diagram</strong> &gt; <strong>Unlock Diagram Content</strong>.</li></ol></td></tr><tr><td colspan="1"><p>At least one of the following:</p><ul><li><p>Symbol properties of a single element represented on a diagram pane</p></li><li>Position of the symbol on the diagram pane</li></ul></td><td colspan="1"><ol><li>Right-click the symbol of that element on a diagram pane.</li><li>From the shortcut menu, select <strong>Lock</strong> &gt; <strong>Unlock Element in Diagram</strong>.</li></ol></td></tr></tbody></table><h3><span style="color: rgb(0,0,0);">Unlocking elements locked by other users</span></h3><p>Forced unlocking is helpful, when elements are left locked by the user who is currently unavailable.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="3e3057c2-4af6-4afd-b2e2-923e2d30ae20"><ac:rich-text-body><p>For this you must have the <strong>Project Locks Administrator</strong> permission.</p></ac:rich-text-body></ac:structured-macro><p> </p><p>To unlock the elements locked by another user</p><hr /><ol><li>From the <strong>Collaborate</strong> menu, select <strong>Unlock All</strong>.</li><li>If the message opens asking you to choose what to unlock, click <strong>Unlock All</strong>. The <strong>Commit Project to the Server</strong> dialog opens.<br /><ac:image><ri:attachment ri:filename="unlock_elements_msg.png" /></ac:image><br /><br /></li><li>In the dialog, do the following:<ol><li>If there is a need, type a comment.</li><li>Click <strong>Commit</strong>.</li></ol></li></ol><p> </p><p>As a result, all the locks made by another user are released, and the changes he/she made are lost forever.</p><h3>Unlocking symbol styles</h3><p><ac:inline-comment-marker ac:ref="c9dddc31-704b-48bb-915a-dadafc3457d9">Symbol styles</ac:inline-comment-marker> can be unlocked via the <strong>Lock View</strong> tab or the <strong>Project Options</strong> dialog.</p><p> </p><p>To unlock symbol styles via the <strong>Lock View</strong> tab</p><hr /><ol><li><p>In the <strong>Lock View</strong> tab on the Model Browser, expand <em>Project Options</em>.<br /><br /></p><ac:structured-macro ac:name="expand" ac:schema-version="1" ac:macro-id="2a1f27ae-38df-4c83-9f2e-16c086e23d9e"><ac:parameter ac:name="title">Where is the Lock View tab?</ac:parameter><ac:rich-text-body>It is the last tab on the Model Browser. If the tab is closed, you can simply open. For this, select <strong>Collaborate</strong> &gt; <strong>View Locked Elements</strong>.</ac:rich-text-body></ac:structured-macro></li><li>Right-click <em>Symbol Styles by &lt;user name&gt;</em> and from the shortcut menu select <strong>Unlock</strong> &gt;<strong> Commit</strong>.<br /><ac:image ac:alt="Locking symbol styles via the Lock View tab" ac:title="Locking symbol styles via the Lock View tab"><ri:attachment ri:filename="unlocking_symbol_styles.png" /></ac:image><br /><br /></li><li>In the <strong>Commit Project to the Server</strong> dialog do the following:<ol><li>If there is a need, type a comment.</li><li>Click to clear the <strong>Keep Locks</strong> check box.</li><li>Click <strong>Commit</strong>.</li></ol></li></ol><p> </p><p>To unlock symbol styles via the<strong> Project Options</strong> dialog</p><hr /><ol><li>Do either:<ul><li>Select <strong>Options</strong> &gt; <strong>Project</strong>.</li><li><p>In the <strong>Lock View</strong> tab on the Model Browser, right-click <em>Project Options</em> and from the shortcut menu, select <strong>Symbol Styles</strong>.<br /><br /></p><ac:structured-macro ac:name="expand" ac:schema-version="1" ac:macro-id="ddc66f3a-945f-4672-99bb-71a7b35764fe"><ac:parameter ac:name="title">Where is the Lock View tab?</ac:parameter><ac:rich-text-body>It is the last tab on the Model Browser. If the tab is closed, you can simply open. For this, select <strong>Collaborate</strong> &gt; <strong>View Locked Elements</strong>.</ac:rich-text-body></ac:structured-macro></li></ul></li><li>In the <strong>Project Options</strong> dialog, click the<strong> Unlock</strong> button and then select <strong>Commit</strong>.</li><li>In the <strong>Commit Project to the Server</strong> dialog do the following:<ol><li>If there is a need, type a comment.</li><li>Click to clear the <strong>Keep Locks</strong> check box.</li><li>Click <strong>Commit</strong>.</li></ol></li></ol><p> </p><h3>Unlocking project usages</h3><p> </p><p><ac:inline-comment-marker ac:ref="5f95ad3a-6831-40be-b69c-9a40c53761c6">To unlock</ac:inline-comment-marker> a used project</p><hr /><ol><li>From the <strong>Options</strong> menu, select <strong>Project Usages</strong>. The <strong>Project Usages </strong>dialog opens.</li><li><p>Select a locked used project on the left side of the dialog.</p></li><li>Click the <strong>Edit</strong> button and then select <strong>Unlock</strong> &gt; <strong>Commit</strong>. The <strong>Commit Project to the Server</strong> dialog opens.</li><li>In the dialog:<ol><li>Type a comment, if there is a need.</li><li>Click to clear the <strong>Keep Locks</strong> check box.</li><li>Click <strong>Commit</strong>.</li></ol></li></ol><h3>Unlocking project structure</h3><p>Project structure becomes locked during the <ac:link><ri:page ri:space-key="MT" ri:content-title="Model Merge" /><ac:plain-text-link-body><![CDATA[merge]]></ac:plain-text-link-body></ac:link> operation. The lock is automatically released after the merged project is committed to the server.</p><p>However, the user who started the merge operation can release the lock manually as well.</p><p> </p><p>To unlock the project structure manually</p><hr /><ol><li><p>From the <strong>File</strong> menu, select <strong>Project Properties</strong>. The <strong>Project Properties</strong> dialog opens.</p></li><li><p>Click the <strong>Unlock (locked by &lt;user name&gt;)</strong> button, for example, <strong>Unlock (locked by billybob)</strong>. The <strong>Commit Project to the Server</strong> dialog opens.</p></li><li>In the dialog:<ol><li>Type a comment, if there is a need.</li><li>Click to clear the <strong>Keep Locks</strong> check box.</li><li>Click <strong>Commit</strong>.</li></ol></li></ol><p> </p><p>Other users cannot unlock the project structure manually.</p></ac:layout-cell><ac:layout-cell><p> </p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=243970349 space=CM version=1 -->
## PAGE 00321: Unlocking models

- page_id: `243970349`
- space_key: `CM`
- source_url: https://docs.nomagic.com/spaces/CM/pages/243970349/Unlocking+models
- version_number: 1
- version_date: `2025-07-31T10:51:48.539+02:00`
- ancestors: Client-Side Collaborative Modeling Documentation > Collaboration powered by 3DEXPERIENCE platform > Locking models in 3DEXPERIENCE platform
- labels: []

### NORMALIZED CONTENT

#### CONTENT-LAYER: Where is the Lock View tab?

724915896

#### CONTENT-COLUMN: Where is the Lock View tab?

724915917

724915894

**On this page**

****

#### CONTENT-BLOCK: Where is the Lock View tab?

724915907

Unlocking the model is useful in any of the following cases:

- After you choose to keep locks, when [CONFLUENCE_PAGE title='Committing changes to Teamwork Cloud' space=''] .
- If you [CONFLUENCE_PAGE title='Locking model for edit' space=''] , but haven't made any changes in the model.
- When you want to clean up other user locks.

##### Unlocking elements and diagrams

If you want to start locking all the lockable elements, [CONFLUENCE_PAGE title='Lock-Free Editing mode' space=''] to work in a lock-required mode.

Elements and diagrams can be unlocked by using the commands from their shortcut menu. 
[IMAGE alt='' src='']

Elements can also be locked by clicking the Lock Element for Edit button [IMAGE alt='' src=''] on their Specification window. 
[IMAGE alt='' src='']

The following table provides suggestions on what unlocking commands to use for different purposes.

| If you finished editing... | Do the following |
| --- | --- |
| Specification properties of a single element | Right-click either:The element in the Containment tree of Lock View tree on the Model Browser.A symbol of the element on a diagram pane.From the shortcut menu, select Lock > Unlock Element.ORDouble-click either:The element in the Containment tree of Lock View tree on the Model Browser.A symbol of the element on a diagram pane.In the Specification window, click the Unlock Element button . |
| Specification properties of both an element and all the elements it contains (owns) | Right-click either:The element in the Containment tree of Lock View tree on the Model Browser.A symbol of the element on a diagram pane.From the shortcut menu, select Lock > Unlock Elements Recursively. |
| At least one of the following:Diagram representation properties (including diagram layout)Symbol properties of elements represented on the diagram pane | Right-click the diagram in the Containment tree of Lock View tree on the Model Browser.From the shortcut menu, select Lock > Unlock Diagram.ORRight-click a free space on the diagram pane.From the shortcut menu, select Lock Diagram > Unlock Diagram.Use this command after you have finished editing the diagram representation. However, you still need to change the specification properties of the elements represented on that diagram pane. |
| At least one of the following:Diagram specification propertiesDiagram representation properties (including diagram layout)Properties of elements represented on the diagram paneSymbol properties of elements represented on the diagram pane | Right-click the diagram in the Containment tree of Lock View tree on the Model Browser.From the shortcut menu, select Lock > Unlock Diagram Content.ORRight-click a free space on the diagram pane.From the shortcut menu, select Lock Diagram > Unlock Diagram Content. |
| At least one of the following:Symbol properties of a single element represented on a diagram panePosition of the symbol on the diagram pane | Right-click the element's symbol on a diagram pane.From the shortcut menu, select Lock > Unlock Element in Diagram. |

##### Unlocking elements locked by other users

Forced unlocking is helpful when elements are left locked by a user who is currently unavailable.

For this you must have the **Project Locks Administrator** permission.

To unlock elements locked by another user

1. From the Collaborate menu, select Unlock All .
2. If a message opens asking you to choose what to unlock, click Unlock All . The Commit Project to the Server dialog opens. [ATTACHMENT filename='unlock_elements_msg.png']
3. In the dialog, do the following:
  1. Type a comment (if needed).
  2. Click Commit .

As a result, all the locks made by another user are released, and any changes the user made are lost forever.

##### Unlocking symbol styles

Symbol styles can be unlocked via the **Lock View** tab or the **Project Options** dialog.

To unlock symbol styles via the **Lock View** tab

1. In the **Lock View** tab on the Model Browser, expand *Project Options*. Where is the Lock View tab?It is the last tab on the Model Browser. If the tab is closed, simply select **Collaborate** > **View Locked Elements**.
2. Right-click Symbol Styles by <user name> and from the shortcut menu select Unlock > Commit . [ATTACHMENT filename='unlocking_symbol_styles.png']
3. In the Commit Project to the Server dialog do the following:
  1. Type a comment (if needed).
  2. Click to clear the Keep Locks check box.
  3. Click Commit .

To unlock symbol styles via the**Project Options** dialog

1. Do either:
  - Select Options > Project .
  - In the **Lock View** tab on the Model Browser, right-click *Project Options* and from the shortcut menu, select **Symbol Styles**. Where is the Lock View tab?It is the last tab on the Model Browser. If the tab is closed, simply select **Collaborate** > **View Locked Elements**.
2. In the Project Options dialog, click the Unlock button and then select Commit .
3. In the Commit Project to the Server dialog do the following:
  1. Type a comment (if needed).
  2. Click to clear the Keep Locks check box.
  3. Click Commit .

##### Unlocking project usages

To unlock a used project

1. From the Options menu, select Project Usages . The Project Usages dialog opens.
2. Select a locked used project on the left side of the dialog.
3. Click the Edit button and then select Unlock > Commit . The Commit Project to the Server dialog opens.
4. In the dialog:
  1. Type a comment (if needed).
  2. Click to clear the Keep Locks check box.
  3. Click Commit .

##### Unlocking project structure

Project structure becomes locked during the [CONFLUENCE_PAGE title='Model Merge' space='MT'] operation. The lock is automatically released after the merged project is committed to the server.

However, the user who started the merge operation can release the lock manually as well.

To unlock the project structure manually

1. From the **File** menu, select **Project Properties**. The **Project Properties** dialog opens.
2. Click the **Unlock (locked by <user name>)** button (for example, **Unlock (locked by billybob)**). The **Commit Project to the Server** dialog opens.
3. In the dialog:
  1. Type a comment (if needed).
  2. Click to clear the Keep Locks check box.
  3. Click Commit .

Other users cannot unlock the project structure manually.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="ccd0ddc8-b3a9-40f4-b097-95be3d09932b"><ac:parameter ac:name="id">724915896</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="60908a8b-ce18-41d5-85b7-25772d5fd970"><ac:parameter ac:name="id">724915917</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="04e43b75-f61b-4b02-b735-a2a9e5320771"><ac:parameter ac:name="id">724915894</ac:parameter><ac:rich-text-body><p><strong>On this page</strong></p><p><strong><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="edcd45dd-92f5-4222-aa23-2e5529614ce5" /></strong></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="bed3747a-0d4d-4cd3-95d9-53bd9f49b704"><ac:parameter ac:name="id">724915907</ac:parameter><ac:rich-text-body><ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p>Unlocking the model is useful in any of the following cases:</p><ul><li>After you choose to keep locks, when <ac:link><ri:page ri:content-title="Committing changes to Teamwork Cloud" /><ac:plain-text-link-body><![CDATA[committing changes]]></ac:plain-text-link-body></ac:link>.</li><li>If you <ac:link><ri:page ri:content-title="Locking model for edit" /><ac:plain-text-link-body><![CDATA[locked the model]]></ac:plain-text-link-body></ac:link>, but haven't made any changes in the model.</li><li><p>When you want to clean up other user locks.</p></li></ul></ac:layout-cell><ac:layout-cell><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><h3>Unlocking <ac:inline-comment-marker ac:ref="2a1e8ffd-1053-446b-8745-3b9e01566dc1">elements</ac:inline-comment-marker> and diagrams</h3><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="8183d317-d270-42b1-9cb3-49bdb46b5d53"><ac:rich-text-body><p>If you want to start locking all the lockable elements, <ac:link ac:anchor="Disabling the Lock-Free Editing mode"><ri:page ri:content-title="Lock-Free Editing mode" /><ac:plain-text-link-body><![CDATA[disable lock-free editing]]></ac:plain-text-link-body></ac:link> to work in a lock-required mode.</p></ac:rich-text-body></ac:structured-macro><p>Elements and diagrams can be unlocked by using the commands from their shortcut menu.<br /><ac:image ac:title="Unlocking commands on the shortcut menu of the Package" ac:alt="Unlocking commands on the shortcut menu of the Package"><ri:attachment ri:filename="unlocking_commands_on_shortcut_menu.png" /></ac:image></p><p><br /></p><p>Elements can also be locked by clicking the Lock Element for Edit button <ac:image><ri:attachment ri:filename="lock_in_spec.png"><ri:page ri:space-key="MT" ri:content-title="_MD buttons" /></ri:attachment></ac:image> on their Specification window.<br /><ac:image ac:title="Unlocking command in the element's Specification window" ac:alt="Unlocking command in the element's Specification window"><ri:attachment ri:filename="unlocking_command_in_spec_window.png" /></ac:image></p><p><br /></p><p>The following table provides suggestions on what unlocking commands to use for different purposes.</p><table class="wrapped"><colgroup><col /><col /></colgroup><tbody><tr><th>If you finished editing...</th><th>Do the following</th></tr><tr><td>Specification properties of a single element</td><td><div class="content-wrapper"><ol><li>Right-click either:<ul><li>The element in the Containment tree of Lock View tree on the Model Browser.</li><li>A symbol of the element on a diagram pane.</li></ul></li><li>From the shortcut menu, select <strong>Lock</strong> &gt; <strong>Unlock Element</strong>.</li></ol><p>OR</p><ol><li>Double-click either:<ul><li>The element in the Containment tree of Lock View tree on the Model Browser.</li><li>A symbol of the element on a diagram pane.</li></ul></li><li>In the Specification window, click the Unlock Element button <ac:image ac:title="Unlock element" ac:alt="Unlock element"><ri:attachment ri:filename="lock_in_spec.png"><ri:page ri:space-key="MT" ri:content-title="_MD buttons" /></ri:attachment></ac:image>.</li></ol></div></td></tr><tr><td>Specification properties of both an element and all the elements it contains (owns)</td><td><ol><li>Right-click either:<ul><li>The element in the Containment tree of Lock View tree on the Model Browser.</li><li>A symbol of the element on a diagram pane.</li></ul></li><li>From the shortcut menu, select <strong>Lock</strong> &gt; <strong>Unlock Elements Recursively</strong>.</li></ol></td></tr><tr><td><p>At least one of the following:</p><ul><li>Diagram representation properties (including diagram layout)</li><li>Symbol properties of elements represented on the diagram pane</li></ul></td><td><div class="content-wrapper"><ol><li>Right-click the diagram in the Containment tree of Lock View tree on the Model Browser.</li><li>From the shortcut menu, select <strong>Lock</strong> &gt; <strong>Unlock Diagram</strong>.</li></ol><p>OR</p><ol><li>Right-click a free space on the diagram pane.</li><li>From the shortcut menu, select <strong>Lock Diagram</strong> &gt; <strong>Unlock Diagram</strong>.</li></ol><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="4e8dc0cf-95bd-41a3-b99b-83d125262e7b"><ac:rich-text-body><p>Use this command after you have finished editing the diagram representation. However, you still need to change the specification properties of the elements represented on that diagram pane.</p></ac:rich-text-body></ac:structured-macro></div></td></tr><tr><td colspan="1"><p>At least one of the following:</p><ul><li>Diagram specification properties</li><li>Diagram representation properties (including diagram layout)</li><li>Properties of elements represented on the diagram pane</li><li>Symbol properties of elements represented on the diagram pane</li></ul></td><td colspan="1"><ol><li>Right-click the diagram in the Containment tree of Lock View tree on the Model Browser.</li><li>From the shortcut menu, select <strong>Lock</strong> &gt; <strong>Unlock Diagram Content</strong>.</li></ol><p>OR</p><ol><li>Right-click a free space on the diagram pane.</li><li>From the shortcut menu, select <strong>Lock Diagram</strong> &gt; <strong>Unlock Diagram Content</strong>.</li></ol></td></tr><tr><td colspan="1"><p>At least one of the following:</p><ul><li><p>Symbol properties of a single element represented on a diagram pane</p></li><li>Position of the symbol on the diagram pane</li></ul></td><td colspan="1"><ol><li>Right-click the element's symbol on a diagram pane.</li><li>From the shortcut menu, select <strong>Lock</strong> &gt; <strong>Unlock Element in Diagram</strong>.</li></ol></td></tr></tbody></table><h3><span style="color: rgb(0,0,0);">Unlocking elements locked by other users</span></h3><p>Forced unlocking is helpful when elements are left locked by a user who is currently unavailable.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="3e3057c2-4af6-4afd-b2e2-923e2d30ae20"><ac:rich-text-body><p>For this you must have the <strong>Project Locks Administrator</strong> permission.</p></ac:rich-text-body></ac:structured-macro><p><br /></p><p>To unlock elements locked by another user</p><hr /><ol><li>From the <strong>Collaborate</strong> menu, select <strong>Unlock All</strong>.</li><li>If a message opens asking you to choose what to unlock, click <strong>Unlock All</strong>. The <strong>Commit Project to the Server</strong> dialog opens.<br /><ac:image><ri:attachment ri:filename="unlock_elements_msg.png" /></ac:image><br /><br /></li><li>In the dialog, do the following:<ol><li>Type a comment (if needed).</li><li>Click <strong>Commit</strong>.</li></ol></li></ol><p><br /></p><p>As a result, all the locks made by another user are released, and any changes the user made are lost forever.</p><h3>Unlocking symbol styles</h3><p><ac:inline-comment-marker ac:ref="c9dddc31-704b-48bb-915a-dadafc3457d9">Symbol styles</ac:inline-comment-marker> can be unlocked via the <strong>Lock View</strong> tab or the <strong>Project Options</strong> dialog.</p><p><br /></p><p>To unlock symbol styles via the <strong>Lock View</strong> tab</p><hr /><ol><li><p>In the <strong>Lock View</strong> tab on the Model Browser, expand <em>Project Options</em>.<br /><br /></p><ac:structured-macro ac:name="expand" ac:schema-version="1" ac:macro-id="2a1f27ae-38df-4c83-9f2e-16c086e23d9e"><ac:parameter ac:name="title">Where is the Lock View tab?</ac:parameter><ac:rich-text-body>It is the last tab on the Model Browser. If the tab is closed, simply select <strong>Collaborate</strong> &gt; <strong>View Locked Elements</strong>.</ac:rich-text-body></ac:structured-macro></li><li>Right-click <em>Symbol Styles by &lt;user name&gt;</em> and from the shortcut menu select <strong>Unlock</strong> &gt;<strong> Commit</strong>.<br /><ac:image ac:title="Locking symbol styles via the Lock View tab" ac:alt="Locking symbol styles via the Lock View tab"><ri:attachment ri:filename="unlocking_symbol_styles.png" /></ac:image><br /><br /></li><li>In the <strong>Commit Project to the Server</strong> dialog do the following:<ol><li>Type a comment (if needed).</li><li>Click to clear the <strong>Keep Locks</strong> check box.</li><li>Click <strong>Commit</strong>.</li></ol></li></ol><p><br /></p><p>To unlock symbol styles via the<strong> Project Options</strong> dialog</p><hr /><ol><li>Do either:<ul><li>Select <strong>Options</strong> &gt; <strong>Project</strong>.</li><li><p>In the <strong>Lock View</strong> tab on the Model Browser, right-click <em>Project Options</em> and from the shortcut menu, select <strong>Symbol Styles</strong>.<br /><br /></p><ac:structured-macro ac:name="expand" ac:schema-version="1" ac:macro-id="ddc66f3a-945f-4672-99bb-71a7b35764fe"><ac:parameter ac:name="title">Where is the Lock View tab?</ac:parameter><ac:rich-text-body>It is the last tab on the Model Browser. If the tab is closed, simply select <strong>Collaborate</strong> &gt; <strong>View Locked Elements</strong>.</ac:rich-text-body></ac:structured-macro></li></ul></li><li>In the <strong>Project Options</strong> dialog, click the<strong> Unlock</strong> button and then select <strong>Commit</strong>.</li><li>In the <strong>Commit Project to the Server</strong> dialog do the following:<ol><li>Type a comment (if needed).</li><li>Click to clear the <strong>Keep Locks</strong> check box.</li><li>Click <strong>Commit</strong>.</li></ol></li></ol><p><br /></p><h3>Unlocking project usages</h3><p><br /></p><p><ac:inline-comment-marker ac:ref="5f95ad3a-6831-40be-b69c-9a40c53761c6">To unlock</ac:inline-comment-marker> a used project</p><hr /><ol><li>From the <strong>Options</strong> menu, select <strong>Project Usages</strong>. The <strong>Project Usages </strong>dialog opens.</li><li><p>Select a locked used project on the left side of the dialog.</p></li><li>Click the <strong>Edit</strong> button and then select <strong>Unlock</strong> &gt; <strong>Commit</strong>. The <strong>Commit Project to the Server</strong> dialog opens.</li><li>In the dialog:<ol><li>Type a comment (if needed).</li><li>Click to clear the <strong>Keep Locks</strong> check box.</li><li>Click <strong>Commit</strong>.</li></ol></li></ol><h3>Unlocking project structure</h3><p>Project structure becomes locked during the <ac:link><ri:page ri:space-key="MT" ri:content-title="Model Merge" /><ac:plain-text-link-body><![CDATA[merge]]></ac:plain-text-link-body></ac:link> operation. The lock is automatically released after the merged project is committed to the server.</p><p>However, the user who started the merge operation can release the lock manually as well.</p><p><br /></p><p>To unlock the project structure manually</p><hr /><ol><li><p>From the <strong>File</strong> menu, select <strong>Project Properties</strong>. The <strong>Project Properties</strong> dialog opens.</p></li><li><p>Click the <strong>Unlock (locked by &lt;user name&gt;)</strong> button (for example, <strong>Unlock (locked by billybob)</strong>). The <strong>Commit Project to the Server</strong> dialog opens.</p></li><li>In the dialog:<ol><li>Type a comment (if needed).</li><li>Click to clear the <strong>Keep Locks</strong> check box.</li><li>Click <strong>Commit</strong>.</li></ol></li></ol><p><br /></p><p>Other users cannot unlock the project structure manually.</p></ac:layout-cell><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section></ac:layout></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=243969784 space=CM version=2 -->
## PAGE 00322: Updating a server project with local changes

- page_id: `243969784`
- space_key: `CM`
- source_url: https://docs.nomagic.com/spaces/CM/pages/243969784/Updating+a+server+project+with+local+changes
- version_number: 2
- version_date: `2025-09-11T15:12:56.074+02:00`
- ancestors: Client-Side Collaborative Modeling Documentation > Using Teamwork Cloud > Collaboration between disconnected teams > Using local project file format
- labels: []

### NORMALIZED CONTENT

Once a third-party has modified the locally saved project and sent it back to you, you can update your server project with local changes. To update your project, you need to import the received file back to the Teamwork Cloud server as a new version of the project.

#### WARNING: Permissions

Permissions

- To update a server project from a local project, you need to have the **Administer Resources** permission .
- To update a main project and used projects with local changes, you must have the read-write permission for all the branches that require update.

The branch selected for update cannot contain any locks. They must be released before updating the project.

To update a server project with local changes of the same project

1. Do one of the following:
  - Open the server project. In the main menu, click Collaborate > Update from Local Project . [ATTACHMENT filename='collaborate_main_menu_update_from_local_project.png']
  - In the main menu, click Collaborate > Projects. The Manage Projects dialog opens. Right-click the project you need to update under the Online Projects tab, and then select Update from Local Project . [ATTACHMENT filename='update_from_local_project.png']
  - In the main menu, click Collaborate > Projects. The Manage Projects dialog opens. Select the project you need to update and then click . [ATTACHMENT filename='update_from_local_project_with_button.png']
2. When the **Update from Local Project** dialog opens:
  - select a local file exported from the server project you are working on
  - specify the branch to update It is highly recommended that you create a new branch from the locally exported version of the server project. This will ensure that the changes made in Teamwork Cloud can be [CONFLUENCE_PAGE title='Model Merge' space='MT'] with local changes by using a correct common ancestor.If the **Question** dialog appears, click**Yes** to automatically create a new branch from the locally exported version.It will automatically create new branches for the project and each of its used projects if they need an update.If you click **No**, the branch that is opened or selected in the **Manage Projects** dialog is specified automatically.[IMAGE alt='' src='']
  - Disable the **Maintain Mount Points of Used Projects** option if you do not want [CONFLUENCE_PAGE title='Understanding differences in local and server project structure' space='']**Mount** relationships to be automatically created upon the project update. [ATTACHMENT filename='update_from_local_project_dialog_.png']
3. Click **Update** when you are done. An updated version of the project with the contents of the local project is created in the selected branch.

The server project will not be updated if the tool recognizes that the local project is the same version as the server project. The same rule goes for used projects.

****

**Used projects**

If the exported version of the server project contains used projects, their status can be reviewed in the **Update from Local Project dialog** when the project updates. To review updates, click **More** in the bottom-left corner of the dialog.

[IMAGE alt='' src='']

Depending on the changes made in the used project, the following actions can be automatically chosen when the project updates:

- Keep Version #<number> : if the used project version is the same as the one on the server (for example, it has not been modified locally), the same version of that used project is kept when the main project updates.
- Use Version #<number> : if the used project version on the server differs from the one in the local file, the version that is available on the server and matches the local file contents is used.
- Add to server : if a new used project is added to the local file and it does not exist in the server project yet, it is added to the server upon the main project update.
- **Update**: if the local file contains used project-related changes, the changes are applied to the server project upon the main project update. [IMAGE alt='' src='']

During a server project update from a local project, commits to branches being updated are not allowed, meaning other users working on the same project branch cannot commit the changes they have made.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="auto-cursor-target">Once a third-party has modified the locally saved project and sent it back to you, you can update your server project with local changes. To update your project, you need to import the received file back to the Teamwork Cloud server as a new version of the project.</p><ac:structured-macro ac:name="warning" ac:schema-version="1" ac:macro-id="3d64b792-c533-4201-8415-7a1f059ad8da"><ac:parameter ac:name="title">Permissions</ac:parameter><ac:rich-text-body><ul><li><span>To update a server project from a local project, you need to have the </span><a href="https://docs.nomagic.com/MCS/?contextKey=permissions&amp;version=latest&amp;variant=default"><strong>Administer Resources</strong> permission</a><span>.</span></li><li><span><span>To update a main project and used projects with local changes, you must have the read-write permission for all the branches that require update.</span></span></li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="7ca81348-287d-4ccf-bac3-b38cf84b8b75"><ac:rich-text-body><p>The branch selected for update cannot contain any locks. They must be released before updating the project.</p></ac:rich-text-body></ac:structured-macro><p><br />To update a server project with local changes of the same project</p><hr /><ol><li>Do one of the following:<ul><li>Open the server project. In the main menu, click <strong>Collaborate</strong> &gt; <strong>Update from Local Project</strong>.<br /><ac:image><ri:attachment ri:filename="collaborate_main_menu_update_from_local_project.png" /></ac:image></li><li>In the main menu, click <strong>Collaborate</strong> &gt; <strong>Projects. </strong>The<strong> Manage Projects </strong>dialog opens. Right-click the project you need to update under the<strong> Online Projects</strong> tab, and then select <strong>Update from Local Project</strong>.<br /><ac:image><ri:attachment ri:filename="update_from_local_project.png" /></ac:image></li><li>In the main menu, click <strong>Collaborate</strong> &gt; <strong>Projects. </strong>The<strong> Manage Projects</strong> dialog opens. Select the project you need to update and then click .<br /><ac:image><ri:attachment ri:filename="update_from_local_project_with_button.png" /></ac:image></li></ul></li><li><p class="auto-cursor-target">When the <strong>Update from Local Project</strong> dialog opens:</p><ul><li><p class="auto-cursor-target">select a local file exported from the server project you are working on</p></li><li><p class="auto-cursor-target">specify the branch to update</p><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="b3a2ff40-95c1-4cc7-9758-64a51a4e24a3"><ac:rich-text-body><p>It is highly recommended that you create a new branch from the locally exported version of the server project. This will ensure that the changes made in Teamwork Cloud can be <ac:link><ri:page ri:space-key="MT" ri:content-title="Model Merge" /><ac:plain-text-link-body><![CDATA[merged]]></ac:plain-text-link-body></ac:link> with local changes by using a correct common ancestor.</p><p>If the <strong>Question</strong> dialog appears, click<strong> Yes</strong> to automatically create a new branch from the locally exported version.<span> It will automatically create new branches for the project and each of its used projects if they need an update.</span></p><p>If you click <strong>No</strong>, the branch that is opened or selected in the <strong>Manage Projects</strong> dialog is specified automatically.</p><p><ac:image ac:align="center"><ri:attachment ri:filename="2019-11-15 13_33_10-Question.png" /></ac:image></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></li><li><p class="auto-cursor-target">Disable the <strong>Maintain Mount Points of Used Projects</strong> option if you do not want <ac:link><ri:page ri:content-title="Understanding differences in local and server project structure" /><ac:link-body><strong>Mount</strong> relationships</ac:link-body></ac:link> to be automatically created upon the project update. </p><ac:image><ri:attachment ri:filename="update_from_local_project_dialog_.png" /></ac:image></li></ul></li><li><p class="auto-cursor-target">Click <strong>Update</strong> when you are done. An updated version of the project with the contents of the local project is created in the selected branch.</p></li></ol><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="d251a63a-8cb3-4bf8-93ec-69b5ff89d9a7"><ac:rich-text-body><p>The server project will not be updated if the tool recognizes that the local project is the same version as the server project. The same rule goes for used projects. </p></ac:rich-text-body></ac:structured-macro><p><strong> </strong></p><p><strong>Used projects</strong></p><p>If the exported version of the server project contains used projects, their status can be reviewed in the <strong>Update from Local Project dialog</strong> when the project updates. To review updates, click <strong>More</strong> in the bottom-left corner of the dialog. </p><p style="margin-left: 30.0px;"><ac:image ac:align="left"><ri:attachment ri:filename="more_button_managing_used_projects.png" /></ac:image></p><p><br /></p><p><br /></p><p><br /></p><p><br /></p><p><br /></p><p><br /></p><p><br /></p><p><br /></p><p><br /></p><p><br /></p><p><br /></p><p>Depending on the changes made in the used project, the following actions can be automatically chosen when the project updates: </p><ul><li><strong>Keep Version #&lt;number&gt;</strong>: if the used project version is the same as the one on the server (for example, it has not been modified locally), the same version of that used project is kept when the main project updates. </li><li><strong>Use Version #&lt;number&gt;</strong>: if the used project version on the server differs from the one in the local file, the version that is available on the server and matches the local file contents is used.</li><li><strong>Add to server</strong>: if a new used project is added to the local file and it does not exist in the server project yet, it is added to the server upon the main project update.</li><li><p class="auto-cursor-target _mce_tagged_br"><strong>Update</strong>: if the local file contains used project-related changes, the changes are applied to the server project upon the main project update.</p><p class="auto-cursor-target _mce_tagged_br"><ac:image><ri:attachment ri:filename="disconnected_team_collaboration_used_projects.png" /></ac:image></p></li></ul><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="97198b50-8611-4150-8a31-f50c1f86a726"><ac:rich-text-body><p>During a server project update from a local project, commits to branches being updated are not allowed, meaning other users working on the same project branch cannot commit the changes they have made.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p>
````

<!--NOMAGIC_PAGE id=243970122 space=CM version=2 -->
## PAGE 00323: Updating a used project with a command line

- page_id: `243970122`
- space_key: `CM`
- source_url: https://docs.nomagic.com/spaces/CM/pages/243970122/Updating+a+used+project+with+a+command+line
- version_number: 2
- version_date: `2026-02-03T14:08:55.480+01:00`
- ancestors: Client-Side Collaborative Modeling Documentation > Using Teamwork Cloud > Used Projects Auto Updater Plugin
- labels: []

### NORMALIZED CONTENT

This section explains how to update a used project using a command line.

To update a used project from the command-line interface

1. Move the properties file to the plugin director y <modeling tool installation directory>/plugins/com.nomagic.magicdraw.twcusageupdater.
2. Open the command-line interface.
3. Go to the <modeling tool installation directory>/plugins/com.nomagic.magicdraw.twcusageupdater directory containing the executable file for the used project update.

#### NOTE: Executable file

Executable file

Depending on your operating system, the executable file is the .sh or .bat file.

To update a used project using a single properties file

Type the following command in the command line:

- On Windows:
- On OS X or Linux:

To update a used project using multiple properties files

Type the following command in the command line:

- On Windows:
- On OS X or Linux:

```text

```

##### Project configuration directory

If you use a non-default configuration directory (e.g. change it by using special properties in the *<modeling tool>.properties* file), you need to update the plugin as well. Otherwise, the plugin searches for settings in the default directory instead of the configuration directory that is actually in use. This results in unexpected failures.

To avoid failures, add identical properties for changing the configuration directory in the update script:

- On Windows:

1. Go to the update.bat file.
2. Change the command line at the end of the file to the following:

"%fullPath%/bin/java" -Xmx4000M -Xss1024K -Dlocalconfig.location=userhome -cp %CLASS_PATH% %*

- On OS X or Linux:

1. Go to the update.sh file.
2. Change the VM_OPTIONS line to the following:

VM_OPTIONS="-Xmx1900M -Xss1024K -Dlocalconfig.location=userhome"

This example is applicable if the modeling tool uses the property "-Dlocalconfig.location=userhome".

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>This section explains how to update a used project using a command line. </p><p><br /></p><p>To update a used project from the command-line interface</p><hr /><ol><li>Move the <ac:inline-comment-marker ac:ref="2c8537ef-4686-40b2-aadb-2637904d8f39">properties</ac:inline-comment-marker> file to the plugin director<ac:inline-comment-marker ac:ref="698a52f9-90e7-4735-8ae1-d6e226b1bb37">y </ac:inline-comment-marker><em><ac:inline-comment-marker ac:ref="698a52f9-90e7-4735-8ae1-d6e226b1bb37">&lt;</ac:inline-comment-marker>modeling tool installation directory&gt;/plugins/com.nomagic.magicdraw.twcusageupdater.</em></li><li>Open the command-line interface.</li><li>Go to the <em>&lt;modeling tool installation directory&gt;/plugins/com.nomagic.magicdraw.twcusageupdater</em> directory containing the executable file for the used project update.<br /><br /></li></ol><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="ef895669-0c57-46b4-8534-8d12933711a3"><ac:parameter ac:name="title">Executable file</ac:parameter><ac:rich-text-body><p>Depending on your operating system, t<span>he executable file is the .sh or .bat file</span><ac:inline-comment-marker ac:ref="343775b0-b011-4d49-8e49-632c4714d342">.</ac:inline-comment-marker></p></ac:rich-text-body></ac:structured-macro><p><br /></p><p><span style="color:var(--ds-text,#333333);">To update a used project using a single properties file</span></p><hr /><p><span style="color:var(--ds-text,#333333);">Type the following command in the command line:</span></p><ul><li data-uuid="3373e01a-57b8-4840-bff6-cde490650fe6">On Windows:<ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="ecf06397-3c8c-4625-88aa-b45edc33f447"><ac:plain-text-body><![CDATA[update.bat -properties sample.properties]]></ac:plain-text-body></ac:structured-macro></li><li data-uuid="7f3fd1aa-3b22-463e-8c12-ad2112d50557">On OS X or Linux:<br /><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="8f22d098-a6ba-4eaf-bf55-99df04813f04"><ac:plain-text-body><![CDATA[./update.sh -properties sample.properties]]></ac:plain-text-body></ac:structured-macro></li></ul><p><br /></p><p><span style="color:var(--ds-text,#333333);">To update a used project using multiple properties files</span></p><hr /><p><span style="color:var(--ds-text,#333333);">Type the following command in the command line:</span></p><ul><li data-uuid="cb7df70c-4796-42bd-a374-f86541e18bb4">On Windows:<br /><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="36f9b4bd-1de2-47da-a332-7f4bb7da417f"><ac:plain-text-body><![CDATA[update.bat -properties first.properties second.properties third.properties]]></ac:plain-text-body></ac:structured-macro></li><li data-uuid="866c5896-e81f-475c-b207-0e8db5a84adc"><p>On OS X or Linux:</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="59bb2a6d-8cc9-4ed1-b808-888fd30c9fd9"><ac:plain-text-body><![CDATA[./update.sh -properties first.properties second.properties third.properties]]></ac:plain-text-body></ac:structured-macro></li></ul><pre><br /></pre><h3>Project configuration directory</h3><p>If you use a non-default configuration directory (e.g. change it by using special properties in the <em>&lt;modeling tool&gt;.properties</em> file), you need to update the plugin as well. Otherwise, the plugin searches for settings in the default directory instead of the configuration directory that is actually in use. This results in unexpected failures.</p><p>To avoid failures, add identical properties for changing the configuration directory in the update script:</p><ul><li>On Windows:</li></ul><ol><li>Go to the update.bat file.</li><li>Change the command line at the end of the file to the following:</li></ol><p>&quot;%fullPath%/bin/java&quot; -Xmx4000M -Xss1024K -Dlocalconfig.location=userhome -cp %CLASS_PATH% %*</p><ul><li>On OS X or Linux:</li></ul><ol><li>Go to the update.sh file.</li><li>Change the VM_OPTIONS line to the following:</li></ol><p>VM_OPTIONS=&quot;-Xmx1900M -Xss1024K -Dlocalconfig.location=userhome&quot;</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="4a36f4af-6839-4b02-900b-3243ba84e4e6"><ac:rich-text-body><p>This example is applicable if the modeling tool uses the property &quot;-Dlocalconfig.location=userhome&quot;.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p>
````

<!--NOMAGIC_PAGE id=243969908 space=CM version=1 -->
## PAGE 00324: Updating changes from Teamwork Cloud

- page_id: `243969908`
- space_key: `CM`
- source_url: https://docs.nomagic.com/spaces/CM/pages/243969908/Updating+changes+from+Teamwork+Cloud
- version_number: 1
- version_date: `2025-07-31T10:51:39.285+02:00`
- ancestors: Client-Side Collaborative Modeling Documentation > Using Teamwork Cloud
- labels: []

### NORMALIZED CONTENT

547926333

547926335

537822470

**On this page**

**3**

547926334

##### Notifications about new versions

NotifyAboutNewWhen several users work on the same project simultaneously, you will be notified if new changes are committed to the server project you are working on.

To turn notifications about new versions on/off

1. On the main menu, click Options > Environment . The Environment Options dialog opens.
2. In the options list, select Collaboration and then the property Notify About New Project Versions on the Server. Do one of the following:

- 
  - Set to true to get notifications.
  - Set to false to turn the notification window off.

You can specify the interval you want the tool to check for new committed project versions on the server; by default, this time interval is two minutes.

To specify a time interval for checking new versions

1. On the main menu, click Options > Environment . The Environment Options dialog opens.
2. In the options list, select Collaboration.
3. Specify Interval to Check For New Project Version (in seconds) property value.

Any changes to theinterval will be applied to newly opened projects only.

After notifications are turned on and/or a time interval is specified, the tool will automatically check to see if there is a new project version available on the server. When a new version is detected, the following notification will appear:

[IMAGE alt='' src='']

You can choose these actions from this notification: or in the **Upcoming Changes**panel.

##### Update the project from the server

UpdatingAn update is the process of refreshing your current project version by merging changes other team members have made and [CONFLUENCE_PAGE title='Committing changes to Teamwork Cloud' space='']. You should update a project when you know that a new project version is available on the server.

To update the project with changes from Teamwork Cloud

- From the **Collaborate** menu, select **Update Project**, or press Ctrl+U. Locked items cannot be updated.

Updating lock information is a special case of the update feature. Use it to refresh the list of elements locked by other users*.*

**

To update the lock information on elements locked by other users

- From the Collaborate menu, select Update Lock Information , or press Ctrl+Shift+U.

##### Display upcoming changes

UpcomingChanges

If you want to see the latest changes, open the **Upcoming Changes** panel**,**whichshows the changes committed to the server project while you were working on it.

To open the **Upcoming Changes** panel

- On the main menu, click Window > Upcoming Changes . The Upcoming Changes panel opens.

[IMAGE alt='' src='']

This toolbar allows you to manage project changes. Its commands are described in the following table.

| Button icon | Button name | Description |
| --- | --- | --- |
|  | Refresh | Refresh the view to check for changes in the latest project version. |
|  | Update project | Update the project to the latest version (or press Ctrl+U). |
|  | Show description | Select a changed element and click Show description. The latest changes committed for that element are displayed, including project version, date, author, and commit comment. |
|  | Difference checker | element history and inspecting changes. |
|  | Legend | - Green indicates that the element was added. - Red indicates that the element was deleted. - Blue indicates that the element was modified or moved. |

##### Granularity level of project options

Every project option and its value under **General** and **Default Model Properties** nodes are treated as separate changes. However, options under the**Diagram Info**node are treated as single changes.After every update, project options get merged (or overwritten). When more than one user works on the same project version and changes different options, these options will be merged after updating. However, if all users changed the same options, the last user to commit will overwrite the option value and only that option will be seen in the last update. The user will be notified before overwriting the option value.

547926332

**Related pages**

- [CONFLUENCE_PAGE title='Reviewing element history and inspecting changes' space='']
- [CONFLUENCE_PAGE title='Committing changes to Teamwork Cloud' space='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="cc08eef6-3027-44ad-b8f8-23e19683d225"><ac:parameter ac:name="id">547926333</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="99ab85a3-60d2-496b-b5a7-a31d5aaca6d1"><ac:parameter ac:name="id">547926335</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="30339f13-f5e1-486d-9b09-7a50b9870e75"><ac:parameter ac:name="id">537822470</ac:parameter><ac:rich-text-body><p><strong>On this page</strong></p><p><strong><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="1f23db09-61cc-4803-9409-ca7989eed709"><ac:parameter ac:name="minLevel">3</ac:parameter></ac:structured-macro><br /></strong></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="d05a6a04-f462-4807-882f-fe9b695f0d9c"><ac:parameter ac:name="id">547926334</ac:parameter><ac:rich-text-body><ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><h3>Notifications about new versions</h3><p><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="86b686e3-7190-4759-b72d-985eabb9cb9b"><ac:parameter ac:name="">NotifyAboutNew</ac:parameter></ac:structured-macro>When several users work on the same project simultaneously, you will be notified if new changes are committed to the server project you are working on. </p><p><br /></p><p>To turn notifications about new versions on/off</p><hr /><ol><li>On the main menu, click <strong>Options</strong> &gt; <strong>Environment</strong>. The <strong>Environment Options </strong>dialog opens.</li><li> In the options list, select <strong>Collaboration </strong>and then the property <strong>Notify About New Project Versions on the Server.</strong> Do one of the following: </li></ol><ul><li style="list-style-type: none;background-image: none;"><ul><li>Set to <em>true</em> to get notifications.</li><li>Set to <em>false</em> to turn the notification window off.</li></ul></li></ul><p><br /></p><p>You can specify the interval you want the tool to check for new committed project versions on the server; by default, this time interval is two minutes. </p><p><br /></p><p>To specify a time interval for checking new versions</p><hr /><ol><li>On the main menu, click <strong>Options</strong> &gt; <strong>Environment</strong>. The <strong>Environment Options </strong>dialog opens.</li><li> In the options list, select <strong>Collaboration.</strong></li><li>Specify <strong>Interval to Check For New Project Version (in seconds) </strong>property value.   <br /><br /></li></ol><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="fa9f1995-91e4-45f2-9111-d0e895d37910"><ac:rich-text-body><p>Any changes to the<span> </span>interval will be applied to newly opened projects only.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><p>After notifications are turned on and/or a time interval is specified, the tool will automatically check to see if there is a new project version available on the server. When a new version is detected, the following notification will appear:</p><p><ac:image ac:align="center"><ri:attachment ri:filename="Changes_on_server.png" /></ac:image></p><p>You can choose these actions from this notification:  <ac:link ac:anchor="Updating"><ac:plain-text-link-body><![CDATA[Update the project from the server]]></ac:plain-text-link-body></ac:link> or <ac:link ac:anchor="UpcomingChanges"><ac:plain-text-link-body><![CDATA[display upcoming changes]]></ac:plain-text-link-body></ac:link> in the  <strong>Upcoming Changes</strong><span style="color: rgb(62,63,64);"> panel.</span></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><br /></p><h3><span style="color: rgb(64,64,64);">Update the project from the server</span></h3><p><span style="color: rgb(64,64,64);"><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="14c7bc38-121b-4a67-90f3-8764df694c15"><ac:parameter ac:name="">Updating</ac:parameter></ac:structured-macro>An update is the process of refreshing your current project version by merging changes other team members have made and <ac:link><ri:page ri:content-title="Committing changes to Teamwork Cloud" /><ac:plain-text-link-body><![CDATA[committed to the server]]></ac:plain-text-link-body></ac:link>. You should update a project when you know that a new project version is available on the server.</span></p><p><span style="color: rgb(64,64,64);"><br /></span></p><p><span style="color: rgb(64,64,64);">To update the project with changes from Teamwork Cloud</span></p><hr /><ul><li><p><span style="color: rgb(64,64,64);">From the <strong>Collaborate</strong> menu, select <strong>Update Project</strong>, or press Ctrl+U.<br /></span></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="a0e80935-0520-42ee-bfcd-46512c5f1c15"><ac:rich-text-body><p>Locked items cannot be updated.</p></ac:rich-text-body></ac:structured-macro></li></ul><p>Updating lock information is a special case of the update feature. Use it to refresh the list of elements locked by other users<em>.</em></p><p><em><br /></em></p><p>To update the lock information on elements locked by other users</p><hr /><ul><li>From the <strong>Collaborate</strong> menu, select <strong>Update Lock Information</strong>, or press Ctrl+Shift+U.</li></ul><p><br /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><h3><span style="color: rgb(62,63,64);">Display upcoming changes</span></h3><p><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="e7dce9cf-2cb7-46fb-8068-aea84e39abaa"><ac:parameter ac:name="">UpcomingChanges</ac:parameter></ac:structured-macro></p><p><span style="color: rgb(62,63,64);">If you want to see the latest changes, open the <strong>Upcoming Changes</strong> panel<strong>, </strong>which</span><span style="color: rgb(62,63,64);"> shows the changes committed to the server project while you were working on it.</span></p><p><br /></p><p>To open the <strong>Upcoming Changes</strong> panel </p><hr /><ul><li>On the main menu, click <strong>Window</strong> &gt; <strong>Upcoming Changes</strong>. The <strong>Upcoming Changes</strong> panel opens.</li></ul><p><ac:image><ri:attachment ri:filename="Upcaming_changes_panel.png" /></ac:image></p><p>This toolbar allows you to manage project changes. Its commands are described in the following table.</p><table class="relative-table wrapped" style="width: 89.4277%;"><colgroup><col style="width: 8.80783%;" /><col style="width: 12.3665%;" /><col style="width: 78.8256%;" /></colgroup><tbody><tr><th>Button icon</th><th>Button name</th><th colspan="1">Description</th></tr><tr><td><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:height="20"><ri:attachment ri:filename="Refresh.png" /></ac:image></p></div></td><td><strong>Refresh</strong></td><td colspan="1">Refresh the view to check for changes in the latest project version.</td></tr><tr><td><div class="content-wrapper"><p><ac:image><ri:attachment ri:filename="Update_project_Upcoming_chages_panel.PNG" /></ac:image></p></div></td><td><strong>Update project</strong></td><td colspan="1"><p>Update the project to the latest version (<span style="color: rgb(64,64,64);">or press Ctrl+U</span>).</p></td></tr><tr><td><div class="content-wrapper"><p><ac:image><ri:attachment ri:filename="show_description.png" /></ac:image></p></div></td><td><strong>Show description</strong></td><td colspan="1"><p>Select a changed element and click <strong>Show description</strong>. The latest changes committed for that element are displayed, including project version, date, author, and commit comment.</p></td></tr><tr><td colspan="1"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:height="16"><ri:attachment ri:filename="quick_diff_button.png" /></ac:image></p></div></td><td colspan="1"><strong>Difference checker</strong></td><td colspan="1"><ac:link><ri:page ri:content-title="Reviewing element history and inspecting changes" /><ac:plain-text-link-body><![CDATA[Reviewing]]></ac:plain-text-link-body></ac:link> element history and inspecting changes.</td></tr><tr><td colspan="1"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:height="20"><ri:attachment ri:filename="Legend_Upcoming_changes_panel.PNG" /></ac:image></p></div></td><td colspan="1"><strong>Legend</strong></td><td colspan="1"><div class="content-wrapper"><p><ac:image><ri:attachment ri:filename="Added.png" /></ac:image> - Green indicates that the element was added.</p><p><ac:image ac:thumbnail="true" ac:height="16"><ri:attachment ri:filename="Deleted.png" /></ac:image> - Red indicates that the element was deleted.</p><p><ac:image><ri:attachment ri:filename="Modified.png" /></ac:image> - Blue indicates that the element was modified or moved.</p></div></td></tr></tbody></table><p class="auto-cursor-target"><br /></p><h3>Granularity level of project options</h3><p>Every project option and its value under <strong>General</strong> and <strong>Default Model Properties</strong> nodes are treated as separate changes. However, o<span>ptions under the </span><strong>Diagram Info</strong><span> node are treated as single changes. </span>After every update, project options get merged (or overwritten). When more than one user works on the same project version and changes different options, these options will be merged after updating. However, if all users changed the same options, the last user to commit will overwrite the option value and only that option will be seen in the last update. The user will be notified before overwriting the option value.</p><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section></ac:layout></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="93de4311-7cd7-4c83-aa9c-69753cd3d594"><ac:parameter ac:name="id">547926332</ac:parameter><ac:rich-text-body><p><strong>Related pages</strong></p><ul><li><ac:link><ri:page ri:content-title="Reviewing element history and inspecting changes" /></ac:link></li><li><ac:link><ri:page ri:content-title="Committing changes to Teamwork Cloud" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=243969769 space=CM version=3 -->
## PAGE 00325: Updating project on server from server project file

- page_id: `243969769`
- space_key: `CM`
- source_url: https://docs.nomagic.com/spaces/CM/pages/243969769/Updating+project+on+server+from+server+project+file
- version_number: 3
- version_date: `2025-09-12T12:50:19.666+02:00`
- ancestors: Client-Side Collaborative Modeling Documentation > Using Teamwork Cloud > Collaboration between disconnected teams > Using server project file format
- labels: []

### NORMALIZED CONTENT

Once a third-party has modified the server project and sent it back to you, you can update a project on the server using the server project file that you received. To update your project, you need to import the received file to the Teamwork Cloud server as a new version of the project.

#### WARNING: Permissions

Permissions

- To update a server project from a server project file, you need the **Administer Resources** permission .
- To update a main project and used projects with changes from the server project file, you must have read-write permission for all branches requiring updates.

The branch selected for update cannot contain any locks. Locks must be released before updating the project.

To update a server project with changes from a server project file

1. Do one of the following :
  - Open the server project. In the main menu, click Collaborate > Update from Local Project . 
[IMAGE alt='' src='']
  - In the main menu, click Collaborate > Projects. The Manage Projects dialog opens. Right-click the project you need to update under the Online Projects tab. Then select Update from Local Project . [ATTACHMENT filename='update_from_local_project.png']
  - In the main menu, click Collaborate > Projects. The Manage Projects dialog opens. Select the project you need to update and then click [ATTACHMENT filename='update_from_local_project_button.png'] . [ATTACHMENT filename='update_from_local_project_with_button.png']
2. When the **Update from Local Project** dialog opens:
  - select the *.szip* file you want to use to update the server project;
  - specify the branch to update: [IMAGE alt='' src=''] It is strongly recommended that you create a new branch from the locally exported version of the server project. This will ensure that changes made in Teamwork Cloud can be [CONFLUENCE_PAGE title='Model Merge' space='MT'] with local changes by using a correct common ancestor.If the **Question** dialog appears, click**Yes** to automatically create a new branch from the locally exported version.It will automatically create new branches for the project and each of its used projects if they need an update.If you click **No**, the branch that is opened or selected in the **Manage Projects** dialog is specified automatically.[IMAGE alt='' src='']
3. Click **Update** when you are done. An updated version of the project with the contents of the local project is created in the selected branch.

The server project will not be updated if the tool recognizes that the local project is the same version as the server project. The same rule applies to used projects.

****

**Used projects**

If the *.szip*version of the project contains used projects, their status can be reviewed in the **Update from Local Project dialog** when the project updates. To review updates, click **More** in the bottom-left corner of the dialog.

[IMAGE alt='' src='']

Depending on the changes made in the used project, the following actions can be chosen automatically when the project updates:

- Keep Version #<number> : if the used project version is the same as the one on the server (for example, it has not been modified locally), the same version of that used project is kept when the main project updates.
- Use Version #<number> : if the used project version on the server differs from the one in the local file, the version that is both available on the server and matches the local file contents is used.
- Add to server : if a new used project is added to the local file and it does not yet exist in the server project, it is added to the server upon the main project update.
- **Update**: if the local file contains used project-related changes, the changes are applied to the server project upon the main project update. [IMAGE alt='' src='']

During a server project update from a local project, commits to branches being updated are not allowed, meaning other users working on the same project branch cannot commit the changes they have made.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="auto-cursor-target">Once a third-party has modified the server project and sent it back to you, you can update a project on the server using the server project file that you received. To update your project, you need to import the received file to the Teamwork Cloud server as a new version of the project.</p><ac:structured-macro ac:name="warning" ac:schema-version="1" ac:macro-id="3d64b792-c533-4201-8415-7a1f059ad8da"><ac:parameter ac:name="title">Permissions</ac:parameter><ac:rich-text-body><ul><li><span>To update a server project from a server project file, you need the </span><a href="https://docs.nomagic.com/MCS/?contextKey=permissions&amp;version=latest&amp;variant=default"><strong>Administer Resources</strong> permission</a><strong>.</strong></li><li><span>To update a main project and used projects with changes from the server project file, you must have read-write permission for all branches requiring updates.</span></li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="7ca81348-287d-4ccf-bac3-b38cf84b8b75"><ac:rich-text-body><p>The branch selected for update cannot contain any locks. Locks must be released before updating the project.</p></ac:rich-text-body></ac:structured-macro><p><br />To update a server project with changes from a server project file</p><hr /><ol><li>Do one of the <ac:inline-comment-marker ac:ref="fb9c03b7-d1ab-4a37-8832-acbf36defc81">following</ac:inline-comment-marker>:<ul><li><span style="color:var(--ds-text,#333333);">Open the server project. In the main menu, click </span><strong style="text-align: left;">Collaborate</strong><span style="color:var(--ds-text,#333333);"> &gt; </span><strong style="text-align: left;">Update from Local Project</strong><span style="color:var(--ds-text,#333333);">.<br /><ac:image><ri:attachment ri:filename="collaborate_main_menu_update_from_local_project.png" /></ac:image></span></li><li>In the main menu, click <strong>Collaborate</strong> &gt; <strong>Projects. </strong>The<strong> Manage Projects </strong>dialog opens. Right-click the project you need to update under the<strong> Online Projects</strong> tab. Then select <strong>Update from Local Project</strong>.<br /><ac:image><ri:attachment ri:filename="update_from_local_project.png" /></ac:image></li><li>In the main menu, click <strong>Collaborate</strong> &gt; <strong>Projects. </strong>The<strong> Manage Projects</strong> dialog opens. Select the project you need to update and then click <ac:image ac:thumbnail="true" ac:width="18"><ri:attachment ri:filename="update_from_local_project_button.png"><ri:page ri:space-key="MT" ri:content-title="Updating a server project with local changes" /></ri:attachment></ac:image>.<br /><ac:image><ri:attachment ri:filename="update_from_local_project_with_button.png" /></ac:image></li></ul></li><li><p class="auto-cursor-target">When the <strong>Update from Local Project</strong> dialog opens:</p><ul><li><p class="auto-cursor-target">select the <em>.szip</em> file you want to use to update the server project;</p></li><li><p class="auto-cursor-target">specify the branch to update:</p><p class="auto-cursor-target"><ac:image><ri:attachment ri:filename="update_from_server_project_file.png" /></ac:image></p><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="b3a2ff40-95c1-4cc7-9758-64a51a4e24a3"><ac:rich-text-body><p>It is strongly recommended that you create a new branch from the locally exported version of the server project. This will ensure that changes made in Teamwork Cloud can be <ac:link><ri:page ri:space-key="MT" ri:content-title="Model Merge" /><ac:plain-text-link-body><![CDATA[merged]]></ac:plain-text-link-body></ac:link> with local changes by using a correct common ancestor.</p><p>If the <strong>Question</strong> dialog appears, click<strong> Yes</strong> to automatically create a new branch from the locally exported version.<span> It will automatically create new branches for the project and each of its used projects if they need an update.</span></p><p>If you click <strong>No</strong>, the branch that is opened or selected in the <strong>Manage Projects</strong> dialog is specified automatically.</p><p><ac:image ac:align="center"><ri:attachment ri:filename="2019-11-15 13_33_10-Question.png" /></ac:image></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></li></ul></li><li><p class="auto-cursor-target">Click <strong>Update</strong> when you are done. An updated version of the project with the contents of the local project is created in the selected branch.</p></li></ol><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="d251a63a-8cb3-4bf8-93ec-69b5ff89d9a7"><ac:rich-text-body><p>The server project will not be updated if the tool recognizes that the local project is the same version as the server project. The same rule applies to used projects. </p></ac:rich-text-body></ac:structured-macro><p><strong> </strong></p><p><strong>Used projects</strong></p><p>If the <em>.szip </em>version of the project contains used projects, their status can be reviewed in the <strong>Update from Local Project dialog</strong> when the project updates. To review updates, click <strong>More</strong> in the bottom-left corner of the dialog. </p><p style="margin-left: 30.0px;"><ac:image><ri:attachment ri:filename="update_from_server_project_file_more.png" /></ac:image></p><p>Depending on the changes made in the used project, the following actions can be chosen automatically when the project updates: </p><ul><li><strong>Keep Version #&lt;number&gt;</strong>: if the used project version is the same as the one on the server (for example, it has not been modified locally), the same version of that used project is kept when the main project updates. </li><li><strong>Use Version #&lt;number&gt;</strong>: if the used project version on the server differs from the one in the local file, the version that is both available on the server and matches the local file contents is used.</li><li><strong>Add to server</strong>: if a new used project is added to the local file and it does not yet exist in the server project, it is added to the server upon the main project update.</li><li><p class="auto-cursor-target _mce_tagged_br"><strong>Update</strong>: if the local file contains used project-related changes, the changes are applied to the server project upon the main project update.</p><p class="auto-cursor-target _mce_tagged_br"><ac:image><ri:attachment ri:filename="Update_server_project_used_projects.png" /></ac:image></p></li></ul><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="97198b50-8611-4150-8a31-f50c1f86a726"><ac:rich-text-body><p>During a server project update from a local project, commits to branches being updated are not allowed, meaning other users working on the same project branch cannot commit the changes they have made.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p>
````

<!--NOMAGIC_PAGE id=243970188 space=CM version=1 -->
## PAGE 00326: Updating projects from 3DEXPERIENCE platform

- page_id: `243970188`
- space_key: `CM`
- source_url: https://docs.nomagic.com/spaces/CM/pages/243970188/Updating+projects+from+3DEXPERIENCE+platform
- version_number: 1
- version_date: `2025-07-31T10:51:45.664+02:00`
- ancestors: Client-Side Collaborative Modeling Documentation > Collaboration powered by 3DEXPERIENCE platform
- labels: []

### NORMALIZED CONTENT

When you work on a server project in parallel with other users, you do not see the changes that other users have committed until you update the project from the **3D**EXPERIENCEplatform. By default, a modeling tool regularly checks if there are new project iterations on the server and displays a notification prompting you to update the project once a new iteration is detected.

This chapter explains how to update a project from the server and when a new project iteration becomes available.

To update a project from the **3D**EXPERIENCEplatform

- In the main menu of a modeling tool, select Collaborate > Update Project .

When you update a project, your current project iteration is merged with the changes of the latest project iteration available on the server.

##### Viewing upcoming project changes

Before updating a project from the **3D**EXPERIENCEplatform you can view the changes of the latest project iteration stored on the server.

To view the upcoming project changes

The **Upcoming Changes** tab displays the project changes committed to the server after the last time you updated the project in your modeling tool. These changes will be merged with your current project iteration when you update the project.

##### Enabling notifications about new project iterations

The option to get notifications about new project iterations committed to the server is enabled by default. However, you can change this setting in the **Environment Options** dialog.

To enable or disable notifications about new project iterations

1. In the main menu of a modeling tool, select Options > Environment .
2. On the left side of the Environment Options dialog, select the Collaboration option group.
3. Do one of the following:
  - To enable notifications about new project iterations, set the Notify About New Project Versions on the Server option to true .
  - To disable notifications about new project iterations, set the Notify About New Project Versions on the Server option to false .

In addition to enabling notifications, you can also specify how often your modeling tool checks for new project iterations on the server.

To specify the time interval determining how often a modeling tool checks for new project iterations

1. In the main menu of a modeling tool, select Options > Environment .
2. On the left side of the Environment Options dialog, select the Collaboration option group.
3. Select the desired value of the Interval to Check For New Project Version (in seconds) option.

[IMAGE alt='' src='']

###### The environment options related to notifications about new project iterations on the server.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>When you work on a server project in parallel with other users, you do not see the changes that other users have committed until you update the project from the <span style="color: rgb(55,65,81);"><strong>3D</strong>EXPERIENCE </span>platform. By default, a modeling tool regularly checks if there are new project iterations on the server and displays a notification prompting you to update the project once a new iteration is detected.</p><p>This chapter explains how to update a project from the server and <ac:link ac:anchor="Viewing upcoming project changes"><ac:plain-text-link-body><![CDATA[view the upcoming changes]]></ac:plain-text-link-body></ac:link> when a new project iteration becomes available.</p><p><br /></p><p>To update a project from the <span style="color: rgb(55,65,81);"><strong>3D</strong>EXPERIENCE </span>platform</p><hr /><ul><li>In the main menu of a modeling tool, select <strong>Collaborate</strong> &gt; <strong>Update Project</strong>.</li></ul><p><br />When you update a project, your current project iteration is merged with the changes of the latest project iteration available on the server. </p><h3><br />Viewing upcoming project changes</h3><p>Before updating a project from the <span style="color: rgb(55,65,81);"><strong>3D</strong>EXPERIENCE </span>platform you can view the changes of the latest project iteration stored on the server.</p><p><br /></p><p>To view the upcoming project changes</p><hr /><ul><ul><li><p class="auto-cursor-target">In the main menu of a modeling tool, select <strong>Window</strong> &gt; <strong>Upcoming Changes</strong>. The <strong>Upcoming Changes</strong> tab is opened on the Quick properties panel.<br /><br /><ac:image><ri:attachment ri:filename="upcoming_changes.png" /></ac:image></p><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="128258f8-3ec1-4e01-ac63-e5bd161f04b0"><ac:rich-text-body><p>You can use the <strong>Upcoming Changes</strong> tab to do the following:</p><ul><li>Click <ac:image><ri:attachment ri:filename="refresh_button.png" /></ac:image> to check for a new project iteration and refresh the <strong>Upcoming Changes</strong> tab.</li><li>Click <ac:image><ri:attachment ri:filename="update_project_button.png" /></ac:image> to update the project to the latest iteration.</li></ul></ac:rich-text-body></ac:structured-macro></li></ul></ul><p>The <strong>Upcoming Changes</strong> tab displays the project changes committed to the server after the last time you updated the project in your modeling tool. These changes will be merged with your current project iteration when you update the project.</p><h3><br />Enabling notifications about new project iterations</h3><p>The option to get notifications about new project iterations committed to the server is enabled by default. However, you can change this setting in the <strong>Environment Options</strong> dialog.</p><p><br /></p><p>To enable or disable notifications about new project iterations</p><hr /><ol><li>In the main menu of a modeling tool, select <strong>Options</strong> &gt; <strong>Environment</strong>.</li><li>On the left side of the <strong>Environment Options</strong> dialog, select the <strong>Collaboration</strong> option group.</li><li>Do one of the following:<ul><li>To enable notifications about new project iterations, set the <strong>Notify About New Project Versions on the Server</strong> option to <em>true</em>.</li><li>To disable notifications about new project iterations, set the <strong>Notify About New Project Versions on the Server</strong> option to <em>false</em>.</li></ul></li></ol><p><br />In addition to enabling notifications, you can also specify how often your modeling tool checks for new project iterations on the server.</p><p><br /></p><p>To specify the time interval determining how often a modeling tool checks for new project iterations</p><hr /><ol><li>In the main menu of a modeling tool, select <strong>Options</strong> &gt; <strong>Environment</strong>.</li><li>On the left side of the <strong>Environment Options</strong> dialog, select the <strong>Collaboration</strong> option group.</li><li>Select the desired value of the <strong>Interval to Check For New Project Version (in seconds)</strong> option.</li></ol><p><br /><ac:image ac:align="center"><ri:attachment ri:filename="environment_options.png" /></ac:image></p><h6 style="text-align: center;">The environment options related to notifications about new project iterations on the server.</h6>
````

<!--NOMAGIC_PAGE id=243970069 space=CM version=1 -->
## PAGE 00327: Used Project Switch Impact Analysis

- page_id: `243970069`
- space_key: `CM`
- source_url: https://docs.nomagic.com/spaces/CM/pages/243970069/Used+Project+Switch+Impact+Analysis
- version_number: 1
- version_date: `2025-07-31T10:51:43.207+02:00`
- ancestors: Client-Side Collaborative Modeling Documentation > Using Teamwork Cloud
- labels: []

### NORMALIZED CONTENT

The used project switch impact analysis enables you to review impacting changes before switching a used project version.In other words, this tool enables early insights over version changes that would have an impact on the main project once the switch is complete.You can use the analysisto inspect impacting changes at different granularity levels, allowing you to see the impact on element-to-element usages or to dive deeper into specific affecting/affected element properties.

To invoke the used project switch impact analysis

1. Right-click the used project version you want to change. The shortcut menu appears.
2. Click **Project usages > Change version**. The **Edit branches** dialog opens.
3. Select the **Show impact of changes before changing versions**check box, as shown below. [IMAGE alt='' src='']
4. Choose the used project version and click **OK**. The Impact analysis window opens shortly.

You can also invoke the used project impact analysis window using the following method:

1. Go to the **Project usages**dialog, reached either from the context menu by choosing **Project usages >** **Project Usage Options...**or from the main menu **Options > Project usages**.
2. The **Edit Branches**dialog opens. Select **Show impact of changes before changing versions**check box.
3. Select the used project version and click **OK**. The Impact analysis window opens.

When the tool finds any impacting changes to be caused by a used project version switch the**Impact analysis**window shows up. Otherwise, you will get a notification that there are no impacting changes and used project version will be changed without invoking the dialog.

##### Used project switch impact analysis window

The**Impact analysis**window consists of three panels:

- Affecting Element Changes - the first panel, showing the changes in used project elements between the current used project version and the one that is to-be-switched to. Next to the panel title there are a number of elements that affect the main (using) project. This panel is separated into two columns:
  - The first column shows used project elements. It can be displayed as a tree or in list form.
  - The second column is named **Affecting**. Thiscolumn shows how many elements are affected by the changed element and what kind of impact it might have (composition integrity errors or no errors).

[IMAGE alt='' src='']

The **Affecting Element Changes**panel****covers both direct and indirect usages, that is, if affecting change comes from an indirectly used project, it will be taken into account as well.

- **Affected Elements** - the second panel, which shows elements from the main project that are directly affected by element change(s) from the **Affecting Element Changes**panel. Next to the panel title are a number of elements that are affected in the main project by the selected element in the first panel. [ATTACHMENT filename='Affected_elements.png']

- **Element specification** - the third panel, showing the properties of selected element either from the **Affecting Element Changes**(changed element properties are shown) or**Affected Elements**(directly affected element properties are shown) panel. This panel works similarly to[CONFLUENCE_PAGE title='Reviewing element history and inspecting changes' space=''] and is separated into three columns:

[IMAGE alt='' src='']

###### Impact analysis window for the *Alarm system* used project.

false

Derived properties are not considered in the impact analysis.

There are certain cases when element selection either in **Affecting Element Changes** or **Affected Elements** panels are not followed by a quick diff in the **Element Specification** panel:

- Whenever an element is deleted in the **Affecting elements** panel, its properties will no longer exist. Following this logic, the **Element Specification** panel will only show a notification indicating that the element is deleted and there are no properties to show.
- Whenever an affecting /affected element is selected in either of the first two panels against which a quick diff does not work, such as a diagram. In this case, you will be notified that there are no property changes for this type of element.

###### Toolbar

All three panels have toolbars to ease navigation through changes.

| Icon | Name | Functionality |
| --- | --- | --- |
|  | Expand All | Click to expand all the elements in the tree. |
|  | Collapse All | Click to collapse all the elements in the tree. |
| Specific for Element specification panel toolbar |  |  |
|  | Categorized view | Click to show all property names in a category. |
|  | Alphabetical view | Click to show all property names in alphabetical order. |
|  | Compare values | Click to compare property values. |
|  | Strip Multiline Text | Click to strip multiline text. If the text in the property cell (e.g., ToDo) covers more than five rows, it is finished with ... showing only those five rows. The complete text is available in the tooltip or in the cell edit mode. |

**Affecting Element Changes**and****Affected Elements**** panels have a List view tab. Use this to list all changed elements. You can search for a specific element in these List views.

###### Summary/Legend

The Summary/Legend section introduces change types, the number of different affecting changes and the number of affected elements.It also includes marking composition integrity errors and a green tick to notify you that changes will not invoke any new composition integrity errors.

[IMAGE alt='' src='']

##### **Understanding changes**

The following definitions show the different change types.

**Addition change** 
In the context of used project impact analysis, an addition change is treated to be the one when an element is restored from a recovered state to a normal one. Such element change is represented in the green rectanglein the **Affected elements** panel.

**Deletion change** 
If an element has been removed, a deletion change occurs. The deletion change usually results in composition integrity errors, i.e., it causes the appearance of recovered elements, since the deleted element is still used in the main project.

**Modification change** 
If an element property has been modified, a modification change occurs.

##### **Accept Changes** or **Reject Changes**

The **Accept****Changes** button switches the used project version to the selected one. You will be warned if the selected version will cause or leave unresolved references.

**Reject Changes** restores the project to the state before invoking the Impact analysis with all of the local changes you had as well. The same appliesfor**X** (closing the dialog).

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><span style="color: rgb(51,51,51);"><span class="_mh6 _wsc">The used project switch impact analysis enables you to <ac:inline-comment-marker ac:ref="d9ca9f96-aaf8-4ba0-98ef-9617a3b5d87f">review impacting changes</ac:inline-comment-marker> before <ac:inline-comment-marker ac:ref="8f5a3675-a973-4ce7-a2e1-bbd91f2b76bc">switching</ac:inline-comment-marker> a used project version. </span></span><ac:inline-comment-marker ac:ref="51354296-f5f8-4f30-9a99-989a42ce63ac">In other words, <span style="color: rgb(62,63,64);">this tool enables early insights over version changes that would have an impact on the main project once the switch is complete.</span></ac:inline-comment-marker><span style="color: rgb(51,51,51);"> <ac:inline-comment-marker ac:ref="ae04f5f5-6d92-4a0b-addf-12b8d20c1f90">You can use the analysis</ac:inline-comment-marker><ac:inline-comment-marker ac:ref="8d69b60c-9c62-48a2-ad69-346706b34a28"><ac:inline-comment-marker ac:ref="ae04f5f5-6d92-4a0b-addf-12b8d20c1f90"> to inspect impacting changes <span style="color: rgb(62,63,64);">at different granularity levels, allowing you to see the impact on element-to-element usages or to dive deeper into specific affecting/affected element properties</span></ac:inline-comment-marker></ac:inline-comment-marker><ac:inline-comment-marker ac:ref="ae04f5f5-6d92-4a0b-addf-12b8d20c1f90">.</ac:inline-comment-marker> </span></p><p class="toggle-title"><br /></p><p class="toggle-title"><span style="color: rgb(51,51,51);">To <ac:inline-comment-marker ac:ref="2aed1746-1c30-4771-a8fe-2fe2824e0d90">invoke</ac:inline-comment-marker> the used project switch <ac:inline-comment-marker ac:ref="254099ab-98eb-45e1-8c89-e67f883ad5f8">impact analysis</ac:inline-comment-marker></span></p><hr /><ol><li><span style="color: rgb(51,51,51);">Right-click the used project version you want to change. The <ac:inline-comment-marker ac:ref="136fcd42-729d-4c2d-8eca-54d285a18d3f">shortcut</ac:inline-comment-marker> menu appears. </span></li><li><span style="color: rgb(51,51,51);">Click <strong>Project usages &gt; Change version</strong>. The <strong>Edit branches</strong> dialog opens. </span></li><li><span style="color: rgb(51,51,51);">Select the <strong>Show impact of changes before changing versions </strong>check box, as shown below. </span><br /><br /><span style="color: rgb(51,51,51);"><ac:image><ri:attachment ri:filename="Edit Branches.png" /></ac:image></span></li><li class="auto-cursor-target"><span style="color: rgb(51,51,51);">Choose the used project version and click <strong>OK</strong>. The Impact analysis window opens shortly.</span></li></ol><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="5f41cf45-7ece-459c-bbe9-a727fe9a6958"><ac:rich-text-body><p><span style="color: rgb(51,51,51);">You can also invoke the used project impact analysis window using the following method:<br /></span></p><ol><li><span style="color: rgb(51,51,51);">Go to the <strong>Project usages </strong>dialog, reached either from the context menu by choosing <strong>Project usages &gt;</strong> <strong>Project Usage Options... </strong>or from the main menu <strong>Options &gt; Project usages</strong>.</span></li><li><span style="color: rgb(51,51,51);">The <strong>Edit Branches </strong>dialog opens. Select <strong>Show impact of changes before changing versions </strong>check box.</span></li><li><span style="color: rgb(51,51,51);">Select the used project version and click <strong>OK</strong>. The Impact analysis window opens.</span></li></ol></ac:rich-text-body></ac:structured-macro><p><span style="color: rgb(51,51,51);">When the tool finds <span style="color: rgb(62,63,64);">any impacting changes to be caused by a used project version switch</span> the </span><strong style="letter-spacing: 0.0px;">Impact analysis </strong><span style="color: rgb(51,51,51);">window shows up. Otherwise, you will get a notification that there are no impacting changes and used project version will be <ac:inline-comment-marker ac:ref="29eae8db-0142-4b46-8188-7adb2c4ce956">changed <span style="color: rgb(62,63,64);">without invoking the dialog</span></ac:inline-comment-marker>. </span></p><h3><span style="color: rgb(51,51,51);">Used project switch impact analysis window</span></h3><p><span style="color: rgb(51,51,51);">The<strong> Impact analysis </strong>window consists of three panels:</span></p><ul><li><strong style="color: rgb(51,51,51);"><ac:inline-comment-marker ac:ref="b5df661d-9e41-4d7f-9ba5-c296be8ed88d">Affecting Element Changes</ac:inline-comment-marker></strong><span style="color: rgb(51,51,51);"> - the first panel, showing the <span style="color: rgb(62,63,64);">changes in used project elements between the current used project version and the one that is to-be-switched to</span>. Next to the panel title there are a number of elements that <span style="color: rgb(62,63,64);">affect the main (using) project</span>. This panel is separated into two columns: </span><br /><ul><li><span style="color: rgb(51,51,51);">The first column shows used project <ac:inline-comment-marker ac:ref="0b1f9cfd-ba16-450b-9ac0-c453627bb589">elements</ac:inline-comment-marker>. It can be displayed as a tree or in list form.</span></li><li><span style="color: rgb(51,51,51);">The second column is named <strong>Affecting</strong>.  This<span style="color: rgb(62,63,64);"> column shows how many elements are affected by the changed element and what kind of impact it might have (composition integrity errors or no errors).</span></span></li></ul></li></ul><p class="auto-cursor-target" style="margin-left: 30.0px;"><ac:image><ri:attachment ri:filename="Affecting_element_changes.png" /></ac:image></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="e03983e0-3464-49d1-9ad4-30771cb5074d"><ac:rich-text-body><p><span style="color: rgb(62,63,64);">The <strong>Affecting Element Changes </strong>panel<strong> </strong>covers both direct and indirect usages, that is, if affecting change comes from an indirectly used project, it will be taken into account as well.</span></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ul><li><span style="color: rgb(51,51,51);"><strong>Affected Elements</strong> - the second panel, which shows elements from the main project that are directly affected by element change(s) from the <strong>Affecting Element Changes </strong>panel. Next to the panel title are a number of elements that are affected in the main project by the selected element in the first panel.</span><br /><ac:image><ri:attachment ri:filename="Affected_elements.png" /></ac:image></li></ul><ul><li><p class="auto-cursor-target"><span style="color: rgb(51,51,51);"><strong>Element specification</strong> - the third panel, showing the properties of selected <ac:inline-comment-marker ac:ref="09f13536-7822-466f-9804-fe9c8d0c898e">element either from</ac:inline-comment-marker> the <span style="color: rgb(62,63,64);"><strong><ac:inline-comment-marker ac:ref="6a94efe1-dae5-418d-b3e4-80e44180d4e0">Affecting Element Changes </ac:inline-comment-marker></strong><ac:inline-comment-marker ac:ref="6a94efe1-dae5-418d-b3e4-80e44180d4e0">(</ac:inline-comment-marker><ac:inline-comment-marker ac:ref="6a94efe1-dae5-418d-b3e4-80e44180d4e0"><span style="color: rgb(62,63,64);">changed element properties are shown)</span></ac:inline-comment-marker> or </span><strong><ac:inline-comment-marker ac:ref="c7710872-f09a-42f9-a432-023823200936"><ac:inline-comment-marker ac:ref="f5812f7a-0f7e-4e1a-8047-47ecca87ff25">Affected Elements </ac:inline-comment-marker></ac:inline-comment-marker></strong><ac:inline-comment-marker ac:ref="c7710872-f09a-42f9-a432-023823200936"><ac:inline-comment-marker ac:ref="f5812f7a-0f7e-4e1a-8047-47ecca87ff25">(<span style="color: rgb(62,63,64);">directly affected element properties are shown)</span></ac:inline-comment-marker></ac:inline-comment-marker> panel. This panel <ac:inline-comment-marker ac:ref="dd5b93ba-78f2-4709-a502-ecf8bc635332">works similarly to</ac:inline-comment-marker></span><ac:inline-comment-marker ac:ref="dd5b93ba-78f2-4709-a502-ecf8bc635332"> </ac:inline-comment-marker><ac:link ac:anchor="quickdiff"><ri:page ri:content-title="Reviewing element history and inspecting changes" /><ac:plain-text-link-body><![CDATA[quick diff ]]></ac:plain-text-link-body></ac:link> and is separated into three columns:</p></li><ul><li><p class="auto-cursor-target"><span style="color: rgb(51,51,51);">The first column shows the properties name.</span></p></li><li><p class="auto-cursor-target"><ac:inline-comment-marker ac:ref="85fc514a-3551-4b40-8cd4-14becf827d8e"><span style="color: rgb(51,51,51);">The second column shows <ac:inline-comment-marker ac:ref="95d22714-13f0-4f82-8a03-049a4138508c">the properties</ac:inline-comment-marker> value from the current used project version when an element is selected in </span><strong style="color: rgb(51,51,51);">Affecting Element Changes</strong><span style="color: rgb(51,51,51);">. </span><span style="color: rgb(62,63,64);"><span style="color: rgb(62,63,64);">When an element is selected from </span><strong style="color: rgb(62,63,64);">Affected Elements</strong><span style="color: rgb(62,63,64);">, <span style="color: rgb(62,63,64);">this column will show the current property value before the used project version switch.</span></span></span></ac:inline-comment-marker></p></li><li><p class="auto-cursor-target"><span style="color: rgb(51,51,51);"><ac:inline-comment-marker ac:ref="85fc514a-3551-4b40-8cd4-14becf827d8e">The third column shows <ac:inline-comment-marker ac:ref="1a5ca889-dc72-4d79-9c07-682417c2e8b6">properties value</ac:inline-comment-marker> changes in the new used project version <span style="color: rgb(51,51,51);">when an element is selected in </span><strong>Affecting Element Changes</strong>. When an element is selected from <strong>Affected Elements</strong>, <span style="color: rgb(62,63,64);">this column will show the to-be property value after the used project version switch.</span></ac:inline-comment-marker></span></p></li></ul></ul><div><span style="color: rgb(51,51,51);"><br /></span></div><div><p><span style="color: rgb(51,51,51);"><ac:image ac:align="center"><ri:attachment ri:filename="impact analysis window.png" /></ac:image></span></p><h6 style="text-align: center;"><span style="color: rgb(51,51,51);">Impact analysis window for the <em>Alarm system</em> used project.</span></h6></div><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="26a4c340-fc77-4384-97e8-e00659731eb4"><ac:parameter ac:name="icon">false</ac:parameter><ac:rich-text-body><p><span style="color: rgb(51,51,51);">Derived properties are not considered in the impact analysis.</span></p><p><span style="color: rgb(51,51,51);">There are certain cases when element selection either in <strong>Affecting Element Changes</strong> or <strong>Affected Elements</strong> panels are not followed by a quick diff in the <strong>Element Specification</strong> panel:</span></p><ul><li><span style="color: rgb(51,51,51);">Whenever an element is deleted in the <strong>Affecting elements</strong> panel, its properties will no longer exist. Following this logic, the <strong>Element Specification</strong> panel will only show a notification indicating that the element is deleted and there are no properties to show. </span></li><li><span style="color: rgb(51,51,51);">Whenever </span>an affecting<span style="color: rgb(51,51,51);">/affected element is selected in either of the first two panels against which a quick diff does not work, such as a diagram. In this case, you will be notified that there are no property changes for this type of element. </span></li></ul></ac:rich-text-body></ac:structured-macro><h4><span style="color: rgb(51,51,51);">Toolbar</span></h4><p><span style="color: rgb(51,51,51);">All three panels have toolbars to ease navigation through changes. </span></p><table class="wrapped"><colgroup><col /><col /><col /></colgroup><tbody><tr><th><span style="color: rgb(51,51,51);">Icon</span></th><th colspan="1"><span style="color: rgb(51,51,51);">Name</span></th><th><span style="color: rgb(51,51,51);">Functionality</span></th></tr><tr><td><div class="content-wrapper"><p><span style="color: rgb(51,51,51);"><ac:image ac:thumbnail="true" ac:height="23"><ri:attachment ri:filename="Expand.png" /></ac:image></span></p></div></td><td colspan="1"><span style="color: rgb(51,51,51);">Expand All</span></td><td><span style="color: rgb(51,51,51);">Click to expand all the elements in the tree.</span></td></tr><tr><td><div class="content-wrapper"><p><span style="color: rgb(51,51,51);"><ac:image ac:thumbnail="true" ac:height="20"><ri:attachment ri:filename="Collapse.png" /></ac:image></span></p></div></td><td colspan="1"><span style="color: rgb(51,51,51);">Collapse All</span></td><td><span style="color: rgb(51,51,51);">Click to collapse all the elements in the tree.</span></td></tr><tr><th colspan="3"><span style="color: rgb(51,51,51);">Specific for Element specification panel toolbar</span></th></tr><tr><td><div class="content-wrapper"><p><span style="color: rgb(51,51,51);"><ac:image ac:thumbnail="true" ac:height="20"><ri:attachment ri:filename="Categorized_view.png" /></ac:image></span></p></div></td><td colspan="1"><span style="color: rgb(51,51,51);">Categorized view</span></td><td><span style="color: rgb(51,51,51);">Click to show all property names in a category.</span></td></tr><tr><td colspan="1"><div class="content-wrapper"><p><span style="color: rgb(51,51,51);"><ac:image ac:thumbnail="true" ac:height="22"><ri:attachment ri:filename="Alphabetical_view.png" /></ac:image></span></p></div></td><td colspan="1"><span style="color: rgb(51,51,51);">Alphabetical view</span></td><td colspan="1"><span style="color: rgb(51,51,51);">Click to show all property names in alphabetical order.</span></td></tr><tr><td colspan="1"><div class="content-wrapper"><p><span style="color: rgb(51,51,51);"><ac:image ac:thumbnail="true" ac:height="20"><ri:attachment ri:filename="compare_property_values_button.png" /></ac:image></span></p></div></td><td colspan="1"><span style="color: rgb(51,51,51);">Compare values</span></td><td colspan="1"><span style="color: rgb(51,51,51);">Click to compare property values.</span></td></tr><tr><td colspan="1"><div class="content-wrapper"><p><span style="color: rgb(51,51,51);"><ac:image ac:thumbnail="true" ac:height="22"><ri:attachment ri:filename="Strip_multiline_text.png" /></ac:image></span></p></div></td><td colspan="1"><span style="color: rgb(51,51,51);">Strip Multiline Text</span></td><td colspan="1"><span style="color: rgb(51,51,51);">Click to strip multiline text. If the text in the property cell (e.g., ToDo)  covers more than five rows, it is finished with <strong>... </strong>showing only those five rows. The complete text is available in the tooltip or in the cell edit mode. </span></td></tr></tbody></table><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="e8ee5da0-c3a2-4cd9-ac07-f75aa9980a4c"><ac:rich-text-body><p><span style="color: rgb(51,51,51);"><strong>Affecting Element Changes </strong>and<strong> <strong>Affected Elements</strong></strong> panels have a List view tab. Use this to list all changed elements. You can search for a specific element in these List views.</span></p></ac:rich-text-body></ac:structured-macro><h4><span style="color: rgb(51,51,51);">Summary/Legend</span></h4><p><span style="color: rgb(51,51,51);">The Summary/Legend section introduces change types, the number of different affecting changes and the number of affected elements. </span>It also includes marking composition integrity errors and a green tick to notify you <span style="color: rgb(62,63,64);">that changes will not invoke any new composition integrity errors.</span></p><p><span style="color: rgb(51,51,51);"><ac:image ac:height="103"><ri:attachment ri:filename="Impact_analysis_summary_legend.png" /></ac:image></span></p><h3><strong style="color: rgb(51,51,51);font-size: 16.0px;letter-spacing: -0.006em;">Understanding changes</strong></h3><p><span style="color: rgb(51,51,51);">The following definitions show the different change types. </span></p><p><span style="color: rgb(51,51,51);"><strong>Addition change</strong></span><br /><span style="color: rgb(51,51,51);">In the context of used project impact analysis, an addition change is treated to be the one when an element is restored from a recovered state to a normal one. Such element change is represented in the green rectangle</span><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);"> in the <strong>Affected elements</strong> panel.</span><br /></span></p><p><span style="color: rgb(51,51,51);"><strong>Deletion change</strong></span><br /><span style="color: rgb(51,51,51);">If an element has been removed, a deletion change occurs. The deletion change <span style="color: rgb(62,63,64);">usually results in composition integrity errors, i.e., it causes the <span style="color: rgb(62,63,64);">appearance of</span> recovered elements, since the deleted element is still used in the main project.</span><br /></span></p><p><span style="color: rgb(51,51,51);"><strong>Modification change</strong></span><br /><span style="color: rgb(51,51,51);">If an element property has been modified, a modification change occurs.</span></p><h3><span style="color: rgb(51,51,51);"><strong style="font-size: 16.0px;letter-spacing: -0.006em;">Accept Changes</strong> or <strong style="font-size: 16.0px;letter-spacing: -0.006em;">Reject Changes</strong></span></h3><p><span style="color: rgb(51,51,51);">The <strong>Accept</strong><strong style="letter-spacing: 0.0px;"> Changes</strong> button switches the used project version to the selected one. You will be warned if the selected version will cause or leave unresolved references. </span></p><p><span style="color: rgb(51,51,51);"><strong>Reject Changes</strong> restores the project to the state before invoking the Impact analysis <span>with all of the local changes you had as well</span>. The same applies </span>for<span style="color: rgb(51,51,51);"> <strong>X</strong> (closing the dialog).</span></p>
````

<!--NOMAGIC_PAGE id=243970083 space=CM version=1 -->
## PAGE 00328: Used project switch impact analysis window

- page_id: `243970083`
- space_key: `CM`
- source_url: https://docs.nomagic.com/spaces/CM/pages/243970083/Used+project+switch+impact+analysis+window
- version_number: 1
- version_date: `2025-07-31T10:51:43.348+02:00`
- ancestors: Client-Side Collaborative Modeling Documentation > Using Teamwork Cloud > Used Project Switch Impact Analysis
- labels: []

### NORMALIZED CONTENT

The**Impact analysis**window consists of three panels:

- Affecting Element Changes - the first panel, showing the changes in used project elements between the current used project version and the one that is to-be-switched to. Next to the panel title there are a number of elements that affect the main (using) project. This panel is separated into two columns:
  - The first column shows used project elements. It can be displayed as a tree or in list form.
  - The second column is named **Affecting**. Thiscolumn shows how many elements are affected by the changed element and what kind of impact it might have (composition integrity errors or no errors).

[IMAGE alt='' src='']

The **Affecting Element Changes**panel****covers both direct and indirect usages, that is, if affecting change comes from an indirectly used project, it will be taken into account as well.

- **Affected Elements** - the second panel, which shows elements from the main project that are directly affected by element change(s) from the **Affecting Element Changes**panel. Next to the panel title are a number of elements that are affected in the main project by the selected element in the first panel. [ATTACHMENT filename='Affected_elements.png']

- **Element specification** - the third panel, showing the properties of selected element either from the **Affecting Element Changes**(changed element properties are shown) or**Affected Elements**(directly affected element properties are shown) panel. This panel works similarly to [CONFLUENCE_PAGE title='Reviewing element history and inspecting changes' space=''] and is separated into three columns:

[IMAGE alt='' src='']

###### Impact analysis window for the *Alarm system* used project.

false

Derived properties are not considered in the impact analysis.

There are certain cases when element selection either in **Affecting Element Changes** or **Affected Elements** panels are not followed by a quick diff in the **Element Specification** panel:

- Whenever an element is deleted in the **Affecting elements** panel, its properties will no longer exist. Following this logic, the **Element Specification** panel will only show a notification indicating that the element is deleted and there are no properties to show.
- Whenever an affecting /affected element is selected in either of the first two panels against which a quick diff does not work, such as a diagram. In this case, you will be notified that there are no property changes for this type of element.

###### Toolbar

All three panels have toolbars to ease navigation through changes.

| Icon | Name | Functionality |
| --- | --- | --- |
|  | Expand All | Click to expand all the elements in the tree. |
|  | Collapse All | Click to collapse all the elements in the tree. |
| Specific for Element specification panel toolbar |  |  |
|  | Categorized view | Click to show all property names in a category. |
|  | Alphabetical view | Click to show all property names in alphabetical order. |
|  | Compare values | Click to compare property values. |
|  | Strip Multiline Text | Click to strip multiline text. If the text in the property cell (e.g., ToDo) covers more than five rows, it is finished with ... showing only those five rows. The complete text is available in the tooltip or in the cell edit mode. |

**Affecting Element Changes**and****Affected Elements**** panels have a List view tab. Use this to list all changed elements. You can search for a specific element in these List views.

###### Summary/Legend

The Summary/Legend section introduces change types, the number of different affecting changes and the number of affected elements.It also includes marking composition integrity errors and a green tick to notify you that changes will not invoke any new composition integrity errors.

[IMAGE alt='' src='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><span style="color: rgb(51,51,51);">The<strong> Impact analysis </strong>window consists of three panels:</span></p><ul><li><strong>Affecting Element Changes</strong><span style="color: rgb(51,51,51);"> - the first panel, showing the <span style="color: rgb(62,63,64);">changes in used project elements between the current used project version and the one that is to-be-switched to</span>. Next to the panel title there are a number of elements that <span style="color: rgb(62,63,64);">affect the main (using) project</span>. This panel is separated into two columns: </span><br /><ul><li><span style="color: rgb(51,51,51);">The first column shows used project elements. It can be displayed as a tree or in list form.</span></li><li><span style="color: rgb(51,51,51);">The second column is named <strong>Affecting</strong>.  This<span style="color: rgb(62,63,64);"> column shows how many elements are affected by the changed element and what kind of impact it might have (composition integrity errors or no errors).</span></span></li></ul></li></ul><p class="auto-cursor-target" style="margin-left: 30.0px;"><ac:image><ri:attachment ri:filename="Affecting_element_changes.png" /></ac:image></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="e03983e0-3464-49d1-9ad4-30771cb5074d"><ac:rich-text-body><p><span style="color: rgb(62,63,64);">The <strong>Affecting Element Changes </strong>panel<strong> </strong>covers both direct and indirect usages, that is, if affecting change comes from an indirectly used project, it will be taken into account as well.</span></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ul><li><span style="color: rgb(51,51,51);"><strong>Affected Elements</strong> - the second panel, which shows elements from the main project that are directly affected by element change(s) from the <strong>Affecting Element Changes </strong>panel. Next to the panel title are a number of elements that are affected in the main project by the selected element in the first panel.</span><br /><ac:image><ri:attachment ri:filename="Affected_elements.png" /></ac:image></li></ul><ul><li><p class="auto-cursor-target"><span style="color: rgb(51,51,51);"><strong>Element specification</strong> - the third panel, showing the properties of selected element either from the <span style="color: rgb(62,63,64);"><strong>Affecting Element Changes </strong>(changed element properties are shown) or </span><strong>Affected Elements </strong>(<span style="color: rgb(62,63,64);">directly affected element properties are shown)</span> panel. This panel works similarly to</span> <ac:link ac:anchor="quickdiff"><ri:page ri:content-title="Reviewing element history and inspecting changes" /><ac:plain-text-link-body><![CDATA[quick diff]]></ac:plain-text-link-body></ac:link> and is separated into three columns:</p></li><ul><li><p class="auto-cursor-target"><span style="color: rgb(51,51,51);">The first column shows the properties name.</span></p></li><li><p class="auto-cursor-target"><span style="color: rgb(51,51,51);">The second column shows the properties value from the current used project version when an element is selected in </span><strong>Affecting Element Changes</strong><span style="color: rgb(51,51,51);">. </span><span style="color: rgb(62,63,64);">When an element is selected from <strong>Affected Elements</strong>, this column will show the current property value before the used project version switch.</span></p></li><li><p class="auto-cursor-target"><span style="color: rgb(51,51,51);">The third column shows properties value changes in the new used project version when an element is selected in <strong>Affecting Element Changes</strong>. When an element is selected from <strong>Affected Elements</strong>, <span style="color: rgb(62,63,64);">this column will show the to-be property value after the used project version switch.</span></span></p></li></ul></ul><p><span style="color: rgb(51,51,51);"><ac:image ac:align="center"><ri:attachment ri:filename="impact analysis window.png" /></ac:image></span></p><h6 style="text-align: center;"><span style="color: rgb(51,51,51);">Impact analysis window for the <em>Alarm system</em> used project.</span></h6><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="26a4c340-fc77-4384-97e8-e00659731eb4"><ac:parameter ac:name="icon">false</ac:parameter><ac:rich-text-body><p><span style="color: rgb(51,51,51);">Derived properties are not considered in the impact analysis.</span></p><p><span style="color: rgb(51,51,51);">There are certain cases when element selection either in <strong>Affecting Element Changes</strong> or <strong>Affected Elements</strong> panels are not followed by a quick diff in the <strong>Element Specification</strong> panel:</span></p><ul><li><span style="color: rgb(51,51,51);">Whenever an element is deleted in the <strong>Affecting elements</strong> panel, its properties will no longer exist. Following this logic, the <strong>Element Specification</strong> panel will only show a notification indicating that the element is deleted and there are no properties to show. </span></li><li><span style="color: rgb(51,51,51);">Whenever </span>an affecting<span style="color: rgb(51,51,51);">/affected element is selected in either of the first two panels against which a quick diff does not work, such as a diagram. In this case, you will be notified that there are no property changes for this type of element. </span></li></ul></ac:rich-text-body></ac:structured-macro><h4><span style="color: rgb(51,51,51);">Toolbar</span></h4><p><span style="color: rgb(51,51,51);">All three panels have toolbars to ease navigation through changes. </span></p><table><colgroup><col /><col /><col /></colgroup><tbody><tr><th><span style="color: rgb(51,51,51);">Icon</span></th><th colspan="1"><span style="color: rgb(51,51,51);">Name</span></th><th><span style="color: rgb(51,51,51);">Functionality</span></th></tr><tr><td><div class="content-wrapper"><p><span style="color: rgb(51,51,51);"><ac:image ac:thumbnail="true" ac:height="23"><ri:attachment ri:filename="Expand.png" /></ac:image></span></p></div></td><td colspan="1"><span style="color: rgb(51,51,51);">Expand All</span></td><td><span style="color: rgb(51,51,51);">Click to expand all the elements in the tree.</span></td></tr><tr><td><div class="content-wrapper"><p><span style="color: rgb(51,51,51);"><ac:image ac:thumbnail="true" ac:height="20"><ri:attachment ri:filename="Collapse.png" /></ac:image></span></p></div></td><td colspan="1"><span style="color: rgb(51,51,51);">Collapse All</span></td><td><span style="color: rgb(51,51,51);">Click to collapse all the elements in the tree.</span></td></tr><tr><th colspan="3"><span style="color: rgb(51,51,51);">Specific for Element specification panel toolbar</span></th></tr><tr><td><div class="content-wrapper"><p><span style="color: rgb(51,51,51);"><ac:image ac:thumbnail="true" ac:height="20"><ri:attachment ri:filename="Categorized_view.png" /></ac:image></span></p></div></td><td colspan="1"><span style="color: rgb(51,51,51);">Categorized view</span></td><td><span style="color: rgb(51,51,51);">Click to show all property names in a category.</span></td></tr><tr><td colspan="1"><div class="content-wrapper"><p><span style="color: rgb(51,51,51);"><ac:image ac:thumbnail="true" ac:height="22"><ri:attachment ri:filename="Alphabetical_view.png" /></ac:image></span></p></div></td><td colspan="1"><span style="color: rgb(51,51,51);">Alphabetical view</span></td><td colspan="1"><span style="color: rgb(51,51,51);">Click to show all property names in alphabetical order.</span></td></tr><tr><td colspan="1"><div class="content-wrapper"><p><span style="color: rgb(51,51,51);"><ac:image ac:thumbnail="true" ac:height="20"><ri:attachment ri:filename="compare_property_values_button.png" /></ac:image></span></p></div></td><td colspan="1"><span style="color: rgb(51,51,51);">Compare values</span></td><td colspan="1"><span style="color: rgb(51,51,51);">Click to compare property values.</span></td></tr><tr><td colspan="1"><div class="content-wrapper"><p><span style="color: rgb(51,51,51);"><ac:image ac:thumbnail="true" ac:height="22"><ri:attachment ri:filename="Strip_multiline_text.png" /></ac:image></span></p></div></td><td colspan="1"><span style="color: rgb(51,51,51);">Strip Multiline Text</span></td><td colspan="1"><span style="color: rgb(51,51,51);">Click to strip multiline text. If the text in the property cell (e.g., ToDo)  covers more than five rows, it is finished with <strong>... </strong>showing only those five rows. The complete text is available in the tooltip or in the cell edit mode. </span></td></tr></tbody></table><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="e8ee5da0-c3a2-4cd9-ac07-f75aa9980a4c"><ac:rich-text-body><p><span style="color: rgb(51,51,51);"><strong>Affecting Element Changes </strong>and<strong> <strong>Affected Elements</strong></strong> panels have a List view tab. Use this to list all changed elements. You can search for a specific element in these List views.</span></p></ac:rich-text-body></ac:structured-macro><h4><span style="color: rgb(51,51,51);">Summary/Legend</span></h4><p><span style="color: rgb(51,51,51);">The Summary/Legend section introduces change types, the number of different affecting changes and the number of affected elements. </span>It also includes marking composition integrity errors and a green tick to notify you <span style="color: rgb(62,63,64);">that changes will not invoke any new composition integrity errors.</span></p><p><span style="color: rgb(51,51,51);"><ac:image ac:height="103"><ri:attachment ri:filename="Impact_analysis_summary_legend.png" /></ac:image></span></p>
````

<!--NOMAGIC_PAGE id=243970112 space=CM version=1 -->
## PAGE 00329: Used Projects Auto Updater Plugin

- page_id: `243970112`
- space_key: `CM`
- source_url: https://docs.nomagic.com/spaces/CM/pages/243970112/Used+Projects+Auto+Updater+Plugin
- version_number: 1
- version_date: `2025-07-31T10:51:43.750+02:00`
- ancestors: Client-Side Collaborative Modeling Documentation > Using Teamwork Cloud
- labels: []

### NORMALIZED CONTENT

The Teamwork Cloud Used Project Updater plugin is an internal modeling tool plugin. Users can set up the plugin to update all or selected used projects to their latest versions. Once the plugin is enabled, you can use a wizard to select used projects you want to update and generate the properties file.

To enable/disable the Teamwork Cloud Used Project Updater plugin

1. On the main menu, go to Options > Environment . The Environment Options dialog opens.
2. In the options list on the left side of the dialog, select Plugins and then the Teamwork Cloud Used Project Updater plugin .
3. Do one of the following:
  - Click the Enable button, to enable the plugin. The value in the Enabled column is set to true .
  - Click the Disable button, to disable the plugin. The value in the Enabled column is set to false . [ATTACHMENT filename='Environment_options_Plugins.png']

#### TIP: Creating a dedicated user

Creating a dedicated user

We recommend that you create a dedicated user to work with the Teamwork Cloud Used Project Updater plugin.

Once the Teamwork Cloud Used Project Updater plugin is enabled do the following:

1. Generate the properties file either using the [CONFLUENCE_PAGE title='Using Used Projects Auto Update Wizard' space=''] or [CONFLUENCE_PAGE title='Manually configuring properties file' space=''] .
2. [CONFLUENCE_PAGE title='Updating a used project with a command line' space=''] .

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>The Teamwork Cloud Used Project Updater <span style="color: rgb(62,63,64);">plugin</span> is an internal modeling tool plugin. Users can set up the plugin to update all or selected used projects to their latest versions. Once the plugin is enabled, you can use a wizard to select used projects you want to update and generate the properties file. </p><p><br /></p><p>To enable/disable the Teamwork Cloud Used Project Updater plugin</p><hr /><ol><li>On the main menu, go to <strong>Options</strong> &gt; <strong>Environment</strong>. The <strong>Environment Options </strong>dialog opens.</li><li> In the options list on the left side of the dialog, select <strong>Plugins </strong>and then the <strong>Teamwork Cloud Used Project Updater</strong> plugin<strong>.</strong></li><li>Do one of the following:<ul><li>Click the <strong>Enable</strong> button, to enable the plugin. The value in the <strong>Enabled</strong> column is set to <em>true</em>.</li><li>Click the <strong>Disable</strong> button, to disable the plugin. The value in the <strong>Enabled</strong> column is set to <em>false</em>.<br /><br /><ac:image><ri:attachment ri:filename="Environment_options_Plugins.png" /></ac:image><br /><br /></li></ul></li></ol><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="31a76f7e-49fe-4f39-8fd5-78b169ab02d7"><ac:parameter ac:name="title">Creating a dedicated user</ac:parameter><ac:rich-text-body><p>We recommend that you create a dedicated user to <ac:inline-comment-marker ac:ref="bedc210c-5559-4eaa-a5c2-8800e6e56951">work with the</ac:inline-comment-marker> Teamwork Cloud Used Project Updater plugin.</p></ac:rich-text-body></ac:structured-macro><p><br />Once the Teamwork Cloud Used Project Updater plugin is enabled do the following:</p><ol><li>Generate the properties file either using the <ac:link><ri:page ri:content-title="Using Used Projects Auto Update Wizard" /><ac:plain-text-link-body><![CDATA[Used Projects Auto Update Wizard]]></ac:plain-text-link-body></ac:link> or <ac:link><ri:page ri:content-title="Manually configuring properties file" /><ac:plain-text-link-body><![CDATA[configure the file manually]]></ac:plain-text-link-body></ac:link>.</li><li><ac:link><ri:page ri:content-title="Updating a used project with a command line" /><ac:plain-text-link-body><![CDATA[Use the command line to update used projects]]></ac:plain-text-link-body></ac:link>.</li></ol>
````

<!--NOMAGIC_PAGE id=243970237 space=CM version=1 -->
## PAGE 00330: Using a server project in 3DEXPERIENCE platform

- page_id: `243970237`
- space_key: `CM`
- source_url: https://docs.nomagic.com/spaces/CM/pages/243970237/Using+a+server+project+in+3DEXPERIENCE+platform
- version_number: 1
- version_date: `2025-07-31T10:51:46.961+02:00`
- ancestors: Client-Side Collaborative Modeling Documentation > Collaboration powered by 3DEXPERIENCE platform > Managing project usages in 3DEXPERIENCE platform
- labels: ['indirectly-used-project', 'directly-used-project']

### NORMALIZED CONTENT

If you want to use elements from another server project, you must first use that project in your main project. You can only use projects in the read-only mode.

#### NOTE: Using a local project

Using a local project

If you want to use a local project, first you must [CONFLUENCE_PAGE title='Adding projects to 3DEXPERIENCE platform' space='']add it to the **3D**EXPERIENCE platform.

##### Using a server project in your project

To start using a server project in your project

1. Select one of the following:
  - Options > Project Usages
  - Collaborate > Project Usages > Project usages
2. In the Project Usages dialog, click [ATTACHMENT filename='add_server_project_button.png'] and select Use Server Project . The Use Server Project wizard opens. [ATTACHMENT filename='using_server_projects.png']
3. Select the server project you want to start using and click **Next**. Use the **3DSearch** bar functionalities to find projects quicker.
4. Select the project iteration you want to use and click the Finish button.
5. When the usage is complete, click **OK** to close the **Project Usages** dialog.

All used projects are displayed in the**Project Usages**dialog and the Containment tree of your model, under the*Project Usages*package.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>If you want to use elements from another server project, you must first use that project in your main project. You can only use projects in the read-only mode.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="6719d072-2ed4-4e14-bc92-fba18f76e4c2"><ac:parameter ac:name="title">Using a local project</ac:parameter><ac:rich-text-body><p>If you want to use a local project, first you must <ac:link><ri:page ri:content-title="Adding projects to 3DEXPERIENCE platform" /><ac:link-body>add it to the <strong>3D</strong>EXPERIENCE platform</ac:link-body></ac:link>.</p></ac:rich-text-body></ac:structured-macro><h3>Using a server project in your project</h3><p>To start using a server project in your project</p><hr /><ol><li>Select one of the following:<ul><li><strong>Options</strong> &gt; <strong>Project Usages</strong></li><li><strong>Collaborate</strong> &gt; <strong>Project Usages</strong> &gt; <strong>Project usages</strong></li></ul></li><li>In the <strong>Project Usages</strong> dialog, click <ac:image ac:thumbnail="true" ac:height="17"><ri:attachment ri:filename="add_server_project_button.png" /></ac:image> and select <strong>Use Server Project</strong>. The <strong>Use Server Project</strong> wizard opens.<br /><br /><ac:image><ri:attachment ri:filename="using_server_projects.png" /></ac:image><br /><br /></li><li><p class="auto-cursor-target">Select the server project you want to start using and click <strong>Next</strong>.</p><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="c0cbdddf-f007-41ba-8f48-9ee737d97507"><ac:rich-text-body><p>Use the <strong>3DSearch</strong> bar functionalities to find projects quicker.</p></ac:rich-text-body></ac:structured-macro></li><li>Select the project iteration you want to use and click the <strong>Finish</strong> button.</li><li><p class="auto-cursor-target">When the usage is complete, click <strong>OK</strong> to close the <strong>Project Usages</strong> dialog.</p></li></ol><p><br /></p><p><span style="letter-spacing: 0.0px;">All used projects are displayed in the</span><span style="letter-spacing: 0.0px;"> </span><strong style="letter-spacing: 0.0px;">Project Usages</strong><span style="letter-spacing: 0.0px;"> </span><span style="letter-spacing: 0.0px;">dialog and the Containment tree of your model, under the </span><em style="letter-spacing: 0.0px;">Project Usages</em><span style="letter-spacing: 0.0px;"> </span><span style="letter-spacing: 0.0px;">packag</span>e.</p>
````

<!--NOMAGIC_PAGE id=243970354 space=CM version=1 -->
## PAGE 00331: Using Cameo Collaborator

- page_id: `243970354`
- space_key: `CM`
- source_url: https://docs.nomagic.com/spaces/CM/pages/243970354/Using+Cameo+Collaborator
- version_number: 1
- version_date: `2025-07-31T10:51:48.709+02:00`
- ancestors: Client-Side Collaborative Modeling Documentation > Collaboration powered by 3DEXPERIENCE platform
- labels: []

### NORMALIZED CONTENT

Cameo Collaborator is a web-based product designed to present models in a simplified form for stakeholders, sponsors, customers, and engineering teams. The product is built with scalability in mind, making it possible to deploy it both in a single node and a cluster setting. It works in all form factors (desktop, tablet, and smart phones), making model sharing and reviewing easy.

Use Cameo Collaborator for Teamwork Cloud to:

- Present models to stakeholders, sponsors, or customers.
- Present models to engineering teams (modelers and non-modelers) within your organization.
- Keep stakeholders and engineering teams up-to-date with the precise, consistent information from the single source of truth - model repository.

To learn how to use Cameo Collaborator see the following topics:

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><span style="color: rgb(23,43,77);">Cameo Collaborator is a web-based product designed <ac:inline-comment-marker ac:ref="7f9413e9-c8bc-4794-b9ee-82bac221b465">to present models</ac:inline-comment-marker> in a simplified form for stakeholders, sponsors, customers, and engineering teams. The product is built with scalability in mind, making it possible to deploy it both in a single node and a cluster setting. It works in all form factors (desktop, tablet, and smart phones), making model sharing and reviewing easy.</span></p><p class="bodytext" style="text-align: left;">Use Cameo Collaborator for Teamwork Cloud to:</p><ul style="text-align: left;"><li><p>Present models to stakeholders, sponsors, or customers.</p></li><li><p>Present models to engineering teams (modelers and non-modelers) within your organization.</p></li><li><p>Keep stakeholders and engineering teams up-to-date with the precise, consistent information from the single source of truth - model repository.</p></li></ul><p>To learn how to use Cameo Collaborator see the following topics:</p><p><ac:structured-macro ac:macro-id="3ee9775d-e19b-445f-8b72-08f0816c16fa" ac:name="children" ac:schema-version="2" /></p>
````

<!--NOMAGIC_PAGE id=243969780 space=CM version=2 -->
## PAGE 00332: Using local project file format

- page_id: `243969780`
- space_key: `CM`
- source_url: https://docs.nomagic.com/spaces/CM/pages/243969780/Using+local+project+file+format
- version_number: 2
- version_date: `2025-09-11T15:11:51.601+02:00`
- ancestors: Client-Side Collaborative Modeling Documentation > Using Teamwork Cloud > Collaboration between disconnected teams
- labels: []

### NORMALIZED CONTENT

This feature allows you to import *.mdzip* files that have been previously exported back to the server project. Thus, you can simply [CONFLUENCE_PAGE title='Saving a local copy of Teamwork Cloud project' space=''] as a *.mdzip* file and send this file to another contractor. The contractor is then able to update the very same server project from the local project. Once the contractor completes project editing, he or she can send the project back to you. This life cycle may continue between any amount of contractors. The feature works even when multiple contractors work with separate Teamwork Cloud installations as well as local work environments.

The main contribution workflow is as follows:

1. [CONFLUENCE_PAGE title='Saving a local copy of Teamwork Cloud project' space='']
2. [CONFLUENCE_PAGE title='Working with projects' space='MT']
3. [CONFLUENCE_PAGE title='Updating a server project with local changes' space='']

To update the server project from the local one, you must have the [**Administer Resources** permission](https://docs.nomagic.com/MCS/?contextKey=permissions&version=latest&variant=default).

700500

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>This feature allows <span style="color:var(--ds-text,#333333);">you to import <em>.mdzip</em> files that have been previously exported back to the server project.</span> Thus, you can simply <ac:link><ri:page ri:content-title="Saving a local copy of Teamwork Cloud project" /><ac:plain-text-link-body><![CDATA[save your project locally]]></ac:plain-text-link-body></ac:link> as a <em>.mdzip</em> file and send this file to another contractor. The contractor is then able to update the very same server project from the local project. Once the contractor completes project editing, he or she can send the project back to you. This life cycle may continue between any amount of contractors. The feature works even when multiple contractors work with separate Teamwork Cloud installations as well as l<span style="color:var(--ds-text,#333333);">ocal work environments. </span></p><p>The main contribution workflow is as follows:</p><ol><li><ac:link><ri:page ri:content-title="Saving a local copy of Teamwork Cloud project" /><ac:plain-text-link-body><![CDATA[Contractor A saves the project locally.]]></ac:plain-text-link-body></ac:link></li><li><ac:link><ri:page ri:space-key="MT" ri:content-title="Working with projects" /><ac:plain-text-link-body><![CDATA[Contractor B gets the locally saved project for editing, modifies it and sends back to Contractor A.]]></ac:plain-text-link-body></ac:link></li><li><ac:link><ri:page ri:content-title="Updating a server project with local changes" /><ac:plain-text-link-body><![CDATA[Contractor A receives the modified project and updates the server project.]]></ac:plain-text-link-body></ac:link></li></ol><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="b911a9b2-9fc3-4471-bef7-6f7b7223e7e5"><ac:rich-text-body><p><span style="color:var(--ds-text,#333333);">To update the server project from the local one, you must have the</span> <a href="https://docs.nomagic.com/MCS/?contextKey=permissions&amp;version=latest&amp;variant=default"><strong>Administer Resources</strong> permission</a><span style="color:var(--ds-text,#333333);">.</span></p></ac:rich-text-body></ac:structured-macro><p style="text-align: center;"><br /></p><p style="text-align: center;"><ac:structured-macro ac:name="widget" ac:schema-version="1" ac:macro-id="cc3601cd-5ee1-4932-93ef-fddac2ae9f41"><ac:parameter ac:name="width">700</ac:parameter><ac:parameter ac:name="url"><ri:url ri:value="https://www.youtube.com/watch?v=XDrcB-JYIHw&amp;t=31s&amp;ab_channel=CATIAMBSE" /></ac:parameter><ac:parameter ac:name="height">500</ac:parameter></ac:structured-macro></p>
````

<!--NOMAGIC_PAGE id=314182379 space=CM version=3 -->
## PAGE 00333: Using lock-based editing mode

- page_id: `314182379`
- space_key: `CM`
- source_url: https://docs.nomagic.com/spaces/CM/pages/314182379/Using+lock-based+editing+mode
- version_number: 3
- version_date: `2026-06-30T13:26:12.814+02:00`
- ancestors: Client-Side Collaborative Modeling Documentation > Using Teamwork Cloud
- labels: []

### NORMALIZED CONTENT

By default, you must lock the part of the model you are going to edit to prevent other users from editing it at the same time. Locking is allowed if that part of the model is not locked by another user, because the same item can only be locked by one user at a time.

To learn more, see:

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><span style="color:var(--ds-text,#172B4D);">By default, you must lock the part of the model you are going to edit to prevent other users from editing it at the same time. Locking is allowed if that part of the model is not locked by another user, because the same item can only be locked by one user at a time.</span></p><p><span style="color:var(--ds-text,#172B4D);">To learn more, see:</span></p><p><span style="color:var(--ds-text,#172B4D);"><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="7e93c5d7-d139-43ff-b1dd-da21328eeefb" /></span></p>
````

<!--NOMAGIC_PAGE id=243969844 space=CM version=3 -->
## PAGE 00334: Using lock-free editing mode

- page_id: `243969844`
- space_key: `CM`
- source_url: https://docs.nomagic.com/spaces/CM/pages/243969844/Using+lock-free+editing+mode
- version_number: 3
- version_date: `2026-06-30T13:24:28.470+02:00`
- ancestors: Client-Side Collaborative Modeling Documentation > Using Teamwork Cloud
- labels: []

### NORMALIZED CONTENT

A Lock-Free Editing mode enables users to work with model elements without the need to lock them. Once the option is enabled in **Project Options**, you can edit elements freely; however, keep it in mind that this is applicable to model elements only. Locks for diagrams, project options, and used projects will persist. In other words, you will still have to lock them before editing.

#### TIP: Recommendation

Recommendation

Assigning differentscopeof the model to different users is the recommended way to work in the Lock-Free Editing mode to prevent conflicts that may occur when users' changes interfere with each other.

To enable the Lock-Free Editing mode in the project, you need to have the [**Release Resource Locks** permission](https://docs.nomagic.com/MCS/?contextKey=permissions&version=latest&variant=default) assigned to you.

To start using the Lock-Free Editing mode

1. In the main menu, click Options > Project .
2. In the panel on the left, select General > Collaboration .
3. Under the Locking options, enable Lock-Free Editing , and click OK . [ATTACHMENT filename='project_options_collaboration.png']
4. In the **Question** dialog asking whether you want to commit the changes to the server, select **Continue**. 
[IMAGE alt='' src=''] As soon as the Lock-Free Editing mode is enabled, all elementlocks are released.
5. In the Information dialog, click OK . The Lock-Free Editing mode is enabled. [ATTACHMENT filename='information_dialog_enabled.png']

If the Lock-Required mode is enabled in the project, users who worked without locks will not be able to commit their changes to the server. Therefore, we recommend making sure that all the users working on the model do not have uncommitted changes before switching modes.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>A Lock-Free Editing mode enables users to work with model elements <ac:inline-comment-marker ac:ref="3bbcc18f-73e9-4648-a496-8a8f4baf9de1">without the need</ac:inline-comment-marker> to lock them. Once the option is enabled in <strong>Project Options</strong>, you <ac:inline-comment-marker ac:ref="9d765dd5-1cea-4dce-8a5f-8c2c44e16922">can</ac:inline-comment-marker> edit elements freely; however, keep it in mind that this is applicable to model elements only. Locks for diagrams, project options, and used projects will persist. In other words, <ac:inline-comment-marker ac:ref="f9b76e18-7d85-46d1-a229-1196821965cb">you will still have to lock them before editing</ac:inline-comment-marker>.</p><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="09f91519-1edc-43e4-8d5c-e3d25d948aee"><ac:parameter ac:name="title">Recommendation</ac:parameter><ac:rich-text-body><p><span>Assigning different </span>scope<span> of the model to different users is the recommended way to work in the Lock-Free Editing mode to prevent conflicts that may occur when users' changes interfere with each other.</span></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="951485b2-7ee3-4d01-ae43-57ea26906356"><ac:rich-text-body><p>To enable the Lock-Free Editing mode in the project, you need to have the <a href="https://docs.nomagic.com/MCS/?contextKey=permissions&amp;version=latest&amp;variant=default"><strong>Release Resource Locks</strong> permission</a> assigned to you.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target" style="text-align: center;"><ac:structured-macro ac:name="widget" ac:schema-version="1" ac:macro-id="5f6a5a4d-5969-42c3-b75e-e6fc6a4595d0"><ac:parameter ac:name="url"><ri:url ri:value="https://www.youtube.com/watch?v=aMgoxSg4-Rw" /></ac:parameter></ac:structured-macro></p><p><br /></p><p>To start using the Lock-Free Editing mode</p><hr /><ol><li>In the main menu, click <strong>Options</strong> &gt; <strong>Project</strong>.</li><li>In the panel on the left, select <strong>General</strong> &gt; <strong>Collaboration</strong>.</li><li>Under the <strong>Locking</strong> options, enable <strong>Lock-Free Editing</strong>, and click <strong><ac:inline-comment-marker ac:ref="179d8669-f48e-4d99-97b8-2519f62390ff">OK</ac:inline-comment-marker></strong>. <br /><ac:image><ri:attachment ri:filename="project_options_collaboration.png" /></ac:image></li><li><p class="auto-cursor-target">In the <strong>Question</strong> dialog asking whether you want to commit the changes to the server, select <strong>Continue</strong>. <br /><ac:image><ri:attachment ri:filename="question_dialog.png" /></ac:image></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="36b262bb-dce3-48f4-85ae-77e008dd3b84"><ac:rich-text-body><p>As soon as the Lock-Free Editing mode is enabled, <ac:inline-comment-marker ac:ref="b59000d9-2d22-4021-a891-0cad804e2a32">all element </ac:inline-comment-marker><ac:inline-comment-marker ac:ref="b4f21fdc-1f83-458b-9dc2-ebbd76ccd903"><ac:inline-comment-marker ac:ref="b59000d9-2d22-4021-a891-0cad804e2a32">locks</ac:inline-comment-marker> are released</ac:inline-comment-marker><ac:inline-comment-marker ac:ref="fa12cea8-2006-438c-8591-262f8d2119c6">.</ac:inline-comment-marker></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></li><li>In the <strong>Information</strong> dialog, click <strong>OK</strong>. The <strong>Lock-Free Editing</strong> mode is enabled. <br /><ac:image><ri:attachment ri:filename="information_dialog_enabled.png" /></ac:image></li></ol><ac:structured-macro ac:name="warning" ac:schema-version="1" ac:macro-id="bab8d01c-9b27-4158-a504-20ea5d28d6f6"><ac:rich-text-body><p>If the Lock-Required mode is enabled in the project, users who worked without locks will not be able to commit their changes to the server. Therefore, we recommend making sure that all the users working on the model do not have uncommitted changes before switching modes.</p></ac:rich-text-body></ac:structured-macro><p><br /></p><p><br /></p>
````

<!--NOMAGIC_PAGE id=243969761 space=CM version=1 -->
## PAGE 00335: Using server project file format

- page_id: `243969761`
- space_key: `CM`
- source_url: https://docs.nomagic.com/spaces/CM/pages/243969761/Using+server+project+file+format
- version_number: 1
- version_date: `2025-07-31T10:51:36.982+02:00`
- ancestors: Client-Side Collaborative Modeling Documentation > Using Teamwork Cloud > Collaboration between disconnected teams
- labels: []

### NORMALIZED CONTENT

To ensure faster project export and import while retaining the same project structure, you can use the file exchange format *.szip*. Using this format, you can export a project with or without used projects, add a project as a new server project, and update it from a locally saved server project file.

You cannot open server project files locally. To view the contents of a project, you must add the project or update it using the *.szip* file.

**In this section:**

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p style="margin-left: 0.0px;"><span style="color: rgb(62,63,64);">To ensure faster project export and import while retaining the same project structure, you can use the file exchange format <em>.szip</em>. Using this format, you can export a project with or without used projects, add a project as a new server project, and update it from a locally saved server project file<ac:inline-comment-marker ac:ref="e2806afd-db43-4169-8303-abfd7054376c">.</ac:inline-comment-marker></span></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="6bbff92c-4d1e-40a0-9efe-709b8046ce9f"><ac:rich-text-body><p><span><span style="color: rgb(62,63,64);">You cannot open server project files locally. To view the contents of a project, you must add the project or update it using the <em>.szip</em> file.</span></span></p></ac:rich-text-body></ac:structured-macro><p style="margin-left: 0.0px;"><strong><span style="color: rgb(62,63,64);">In this section:</span></strong></p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="3feaa75c-bd9e-42e9-81c5-a21dff605936" /></p><p class="auto-cursor-target"><br /></p>
````

<!--NOMAGIC_PAGE id=243969987 space=CM version=11 -->
## PAGE 00336: Using server projects

- page_id: `243969987`
- space_key: `CM`
- source_url: https://docs.nomagic.com/spaces/CM/pages/243969987/Using+server+projects
- version_number: 11
- version_date: `2026-07-10T14:45:21.201+02:00`
- ancestors: Client-Side Collaborative Modeling Documentation > Using Teamwork Cloud > Managing project usages
- labels: ['indirectly-used-project', 'directly-used-project']

### NORMALIZED CONTENT

Using other projects in your server project allows you to use the elements of the used projects (e.g., as types) in the main project. You can choose from full usage, where an entire project is used, or partial usage, where you select the specific project scope you want to use. Additionally, [CONFLUENCE_PAGE title='Changing usage type and scope' space=''] at any time.

Projects are used only in read-only mode. For more information about modifying project usages, see [CONFLUENCE_PAGE title='Editing the content of a used project' space=''].

To use a server project in your main project, you must have the Administer Resources permission.

##### Full project usage

Full project usage is the default usage type, where an entire project is used in your main project.

The partial project usage functionality requires the [Element Chooser service](https://docs.nomagic.com/MCS/?contextKey=element-chooser-service&version=latest&variant=default).

To use a server project (full usage)

1. Do one of the following:
  - In the main menu, select Options > Project Usages .
  - In the main menu, select Collaborate > Project Usages > Project Usages .
2. In the Project Usages dialog, click [ATTACHMENT filename='add_server_project_button.png'] and select Use Server Project . [ATTACHMENT filename='project_usages_dialog.png']
3. In the **Use Server Project** dialog, select the project you want to use and click**Next**. You can use the search bar to filter projects by project version, commit tags, author, or comment.
4. Select the project version you want to use and click the Finish button. [ATTACHMENT filename='selecting_project_version.png']
5. Wait for the usage to be established and click OK to close the Project Usages dialog.

Used projects are displayed under the *Project Usages*package in the Containment tree and in the **Project Usages** dialog. Once the usage is established, you can use the elements of a used project in your main project.

##### Partial project usage

Partial project usage allows you to use only the selected part of the project.

The partial project usage functionality requires the [Element Chooser service](https://docs.nomagic.com/MCS/?contextKey=element-chooser-service&version=latest&variant=default).

To use a part of a server project (partial usage)

1. Do one of the following:
  - In the main menu, select Options > Project Usages .
  - In the main menu, select Collaborate > Project Usages > Project Usages .
2. In the Project Usages dialog, click [ATTACHMENT filename='add_server_project_button.png'] and select Use Server Project .
3. [ATTACHMENT filename='project_usages_dialog.png']
4. In the **Use Server Project** dialog, select the project you want to use and click**Next**. You can use the search bar to filter projects by project version, commit tags, author, or comment.
5. Select the project version you want to use.
6. Select the Partial Usage (Technology Preview) check box. [ATTACHMENT filename='partial_project_usage.png']
7. Click the Next button.
8. Select the project elements you want to use. Selecting a parent element automatically includes all of its owned elements in the usage scope. Selecting usage scopeIf the elements in the selected usage scope reference elements outside the scope, these referenced elements will be matched with correspondingelements in the main project. If corresponding elements are not found in the main project and its current usages, all references to them will be removed from the selected scope.For example, if the usage scope contains a part whose type is outside the scope, and the main project does not include that type, the reference to the type will be removed. As a result, the part in the used project will no longer have a type.To minimize the risk of lost references, it is recommended to use all standard profiles of the used project in your main project beforehand. [ATTACHMENT filename='selecting_usage_scope.png']
9. Click the Finish button.
10. Wait for the usage to be established and click OK to close the Project Usages dialog.

Used projects are displayed under the *Project Usages*package in the Containment tree and in the **Project Usages** dialog. Once the usage is established, you can use the elements of a used project in your main project.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>Using other projects in your server project allows you to use the elements of the used projects (e.g., as types) in the main project. You can choose from full usage, where an entire project is used, or partial usage, where you select the specific project scope you want to use. Additionally, <ac:link><ri:page ri:content-title="Changing usage type and scope" /><ac:plain-text-link-body><![CDATA[usage type (full or partial) and scope can be changed]]></ac:plain-text-link-body></ac:link> at any time.</p><p>Projects are used only in read-only mode. For more information about modifying project usages, see <ac:link><ri:page ri:content-title="Editing the content of a used project" /></ac:link>.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="660e2072-9c67-4bfd-a314-4d8ce037351b"><ac:rich-text-body><p>To use a server project in your main project, you must have the Administer Resources permission.</p></ac:rich-text-body></ac:structured-macro><h3>Full project usage</h3><p>Full project usage is the default usage type, where an entire project is used in your main project.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="f105e94a-6e66-455c-add3-8c298aae647e"><ac:rich-text-body><p>The partial project usage functionality requires the <a href="https://docs.nomagic.com/MCS/?contextKey=element-chooser-service&amp;version=latest&amp;variant=default">Element Chooser service</a>.</p></ac:rich-text-body></ac:structured-macro><p>To use a server project (full usage)</p><hr /><ol><li>Do one of the following:<ul><li>In the main menu, select <strong>Options</strong> &gt; <strong>Project Usages</strong>.</li><li>In the main menu, select <strong>Collaborate</strong> &gt; <strong>Project Usages</strong> &gt; <strong>Project Usages</strong>.</li></ul></li><li>In the <strong>Project Usages</strong> dialog, click <ac:image ac:thumbnail="true" ac:height="17"><ri:attachment ri:filename="add_server_project_button.png"><ri:page ri:space-key="MT" ri:content-title="_MD buttons" /></ri:attachment></ac:image> and select <strong>Use Server Project</strong>.<br /><ac:image><ri:attachment ri:filename="project_usages_dialog.png" /></ac:image></li><li><p class="auto-cursor-target">In the <strong>Use Server Project</strong> dialog, select the <span style="letter-spacing: 0.0px;">project you want to use and click </span><strong style="letter-spacing: 0.0px;"><ac:inline-comment-marker ac:ref="ffbd09a6-29f2-4a61-a65a-5b85fcbda24f">Next</ac:inline-comment-marker></strong><span style="letter-spacing: 0.0px;">.</span></p><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="9985c66a-6e7a-4644-911b-86effab3a270"><ac:rich-text-body><p>You can use the search bar to filter projects by project version, commit tags, author, or comment.</p></ac:rich-text-body></ac:structured-macro></li><li>Select the project version you want to use and click the <strong>Finish</strong> button.<br /><ac:image><ri:attachment ri:filename="selecting_project_version.png" /></ac:image></li><li>Wait for the usage to be established and click <strong>OK</strong> to close the <strong>Project Usages</strong> dialog.</li></ol><p>Used projects are displayed under the <em>Project Usages </em>package in the Containment tree and in the <strong>Project Usages</strong> dialog. Once the usage is established, you can use the elements of a used project in your main project.</p><h3>Partial project usage</h3><p>Partial project usage allows you to use only the selected part of the project.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="084c60b0-43ee-459c-8450-b1ee0c8fad9f"><ac:rich-text-body><p>The partial project usage functionality requires the <a href="https://docs.nomagic.com/MCS/?contextKey=element-chooser-service&amp;version=latest&amp;variant=default">Element Chooser service</a>.</p></ac:rich-text-body></ac:structured-macro><p>To use a part of a server project (partial usage)</p><hr /><ol><li>Do one of the following:<ul><li>In the main menu, select <strong>Options</strong> &gt; <strong>Project Usages</strong>.</li><li>In the main menu, select <strong>Collaborate</strong> &gt; <strong>Project Usages</strong> &gt; <strong>Project Usages</strong>.</li></ul></li><li>In the <strong>Project Usages</strong> dialog, click <ac:image ac:thumbnail="true" ac:height="17"><ri:attachment ri:filename="add_server_project_button.png" /></ac:image> and select <strong>Use Server Project</strong>.</li><li data-uuid="713d17f7-6b52-438f-af35-3a2728bda2da"><ac:image><ri:attachment ri:filename="project_usages_dialog.png" /></ac:image></li><li><p class="auto-cursor-target">In the <strong>Use Server Project</strong> dialog, select the <span>project you want to use and click </span><strong>Next</strong><span>.</span></p><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="06e99eed-e41e-43ab-ad5b-233ac661dfa0"><ac:rich-text-body><p>You can use the search bar to filter projects by project version, commit tags, author, or comment.</p></ac:rich-text-body></ac:structured-macro></li><li>Select the project version you want to use.</li><li>Select the <strong>Partial Usage (Technology Preview)</strong> check box.<br /><ac:image><ri:attachment ri:filename="partial_project_usage.png" /></ac:image></li><li>Click the <strong>Next</strong> button.</li><li>Select the project elements you want to use. Selecting a parent element automatically includes all of its owned elements in the usage scope.<br /><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="76bdc881-d944-4027-a8a9-a246c7221a3b"><ac:parameter ac:name="title">Selecting usage scope</ac:parameter><ac:rich-text-body><p><span style="color:var(--ds-text,#172b4d);">If the elements in the selected usage scope reference elements outside the scope, these referenced elements will be matched with corresponding </span><span style="color:var(--ds-text,#172b4d);">elements in the main project</span>. If corresponding elements are not found in the main project and its current usages, all references to them will be removed from the selected scope.</p><p>For example, if the usage scope contains a part whose type is outside the scope, and the main project does not include that type, the reference to the type will be removed. As a result, the part in the used project will no longer have a type.</p><p>To minimize the risk of lost references, it is recommended to use all standard profiles of the used project in your main project beforehand.</p></ac:rich-text-body></ac:structured-macro><ac:image><ri:attachment ri:filename="selecting_usage_scope.png" /></ac:image></li><li>Click the <strong>Finish</strong> button.</li><li>Wait for the usage to be established and click <strong>OK</strong> to close the <strong>Project Usages</strong> dialog.</li></ol><p>Used projects are displayed under the <em>Project Usages </em>package in the Containment tree and in the <strong>Project Usages</strong> dialog. Once the usage is established, you can use the elements of a used project in your main project.</p>
````

<!--NOMAGIC_PAGE id=243969679 space=CM version=8 -->
## PAGE 00337: Using Teamwork Cloud

- page_id: `243969679`
- space_key: `CM`
- source_url: https://docs.nomagic.com/spaces/CM/pages/243969679/Using+Teamwork+Cloud
- version_number: 8
- version_date: `2025-09-23T14:02:07.421+02:00`
- ancestors: Client-Side Collaborative Modeling Documentation
- labels: []

### NORMALIZED CONTENT

##### Introduction

Teamwork Cloud is a repository for collaborative development and versioned storage of models.Teamwork Cloud is intended to improve the areas of model governance, model analysis, and integration with third-party tools. The benefits to enterprise users include:

- Role-Based Access Control enables efficient management of users’ access rights across the enterprise. Additionally, as distributed systems can be challenging to administer, we have built a convenient web-based administrative interface to Teamwork Cloud , which provides a single way to manage user accounts, licensing, access control, LDAP integration, and SSL setup.
- Teamwork Cloud is designed from the ground up to support working with large models. In particular, the efficient delta-based protocol used when users commit and retrieve updates to a model will save time for those users who access the repository through poor network connections. Likewise, the amount of data that is transmitted depends only on the size of the changes being made to the model.
- A database-driven model storage paradigm in Teamwork Cloud unveils powerful client-side features for model changes and history tracking at element level.
- Project Usages location : rather than mounting everything under the main model root element, the Model Browser has a dedicated root for Project Usages in Teamwork Cloud.
- Shared Packages : there are no shared packages in the Teamwork Cloud Project Usages; all content is available for reference. However, a Teamwork Cloud project can be stripped using the [CONFLUENCE_PAGE title='Hiding packages' space=''] feature.
- The mounting of Used Projects in Teamwork Cloud is achieved via a model-based Mount relationship. In order to ensure the same Containment tree structure when adding/migrating projects to Teamwork Cloud, original mounting is re-created by adding the Mount relationship automatically.
- Teamwork Cloud architecture supports the sticky versions (used project versions that remain used until they are changed in the main project) approach of used projects. However, you can easily update a used project to the latest version by setting up a notification that will inform you about the appearance of a new used project version. Alternatively, you can use the [CONFLUENCE_PAGE title='Used Projects Auto Updater Plugin' space=''] that allows the automatic update of used projects.
- In Teamwork Cloud, every new version of the project gets a unique consecutive number, even between different branches, which makes it easier to keep track of the commit history and identify the specific project versions.
- Teamwork Cloud used [CONFLUENCE_PAGE title='Managing project usages' space='']. This helps to prevent cyclic dependencies. We recommend that you open a used project as a stand-alone and edit it there; however, you can move elements to other projects using the [CONFLUENCE_PAGE title='Moving elements to other projects' space=''] in Teamwork Cloud as well. This feature allows transferring data between projects in just a few steps.

You can find more information about the key benefits of Teamwork Cloud, required resources, and the latest news on its official product page here [https://www.3ds.com/products/catia/no-magic/teamwork-cloud](https://www.3ds.com/products/catia/no-magic/teamwork-cloud).

**Related pages**

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><h3>Introduction</h3><p>Teamwork Cloud is a repository for collaborative development and versioned storage of models.<span style="color:var(--ds-background-accent-red-bolder,#c9372c);"> </span>Teamwork Cloud is intended to improve the areas of model governance, model analysis, and integration with third-party tools. The benefits to enterprise users include:</p><ul><li>Role-Based Access Control enables efficient management of users’ access rights across the enterprise. Additionally, as distributed systems can be challenging to administer, we have built a convenient <a href="https://docs.nomagic.com/MCS/?contextKey=admin-web-applications&amp;version=latest&amp;variant=default">web-based administrative interface to Teamwork Cloud</a>, which provides a single way to manage user accounts, licensing, access control, LDAP integration, and SSL setup.</li><li>Teamwork Cloud is designed from the ground up to support working with large models. In particular, the efficient delta-based protocol used when users commit and retrieve updates to a model will save time for those users who access the repository through poor network connections. Likewise, the amount of data that is transmitted depends only on the size of the changes being made to the model.</li><li><span style="color:var(--ds-text,#333333);">A database-driven model storage paradigm in Teamwork Cloud unveils powerful client-side features for model changes and history tracking at element level.</span></li><li><strong>Project Usages location</strong>: rather than mounting everything under the main model root element, the Model Browser has a dedicated root for Project Usages in Teamwork Cloud.</li><li><strong>Shared Packages</strong>: there are no shared packages in the Teamwork Cloud Project Usages; all content is available for reference. However, a Teamwork Cloud project can be stripped using the <ac:link><ri:page ri:content-title="Hiding packages" /></ac:link> feature. </li><li><span style="color:var(--ds-text,#333333);">The mounting of Used Projects in Teamwork Cloud is achieved via a model-based Mount relationship. In order to ensure the same Containment tree structure when adding/migrating projects to Teamwork Cloud, original mounting is re-created by adding the Mount relationship automatically.</span></li><li>Teamwork Cloud architecture supports the sticky versions (used project versions that remain used until they are changed in the main project) approach of used projects. However, you can easily update a used project to the latest version by setting up a notification that will inform you about the appearance of a new used project version. Alternatively, you can use the <ac:link><ri:page ri:content-title="Used Projects Auto Updater Plugin" /><ac:plain-text-link-body><![CDATA[Teamwork Cloud Used Project Updater plugin]]></ac:plain-text-link-body></ac:link> that allows the automatic update of used projects. </li><li><p>In Teamwork Cloud, every new version of the project gets a unique consecutive number, even between different branches, which makes it easier to keep track of the commit history and identify the specific project versions. </p></li><li><p>Teamwork Cloud used <ac:link><ri:page ri:content-title="Managing project usages" /><ac:plain-text-link-body><![CDATA[projects are read-only]]></ac:plain-text-link-body></ac:link>. This helps to prevent cyclic dependencies. We recommend that you open a used project as a stand-alone and edit it there; however, you can move elements to other projects using the <ac:link><ri:page ri:content-title="Moving elements to other projects" /><ac:plain-text-link-body><![CDATA[cross-project refactoring functionality]]></ac:plain-text-link-body></ac:link> in Teamwork Cloud as well. This feature allows transferring data between projects in just a few steps.  <br /><br /></p></li></ul><p>You can find more information about the key benefits of Teamwork Cloud, required resources, and the latest news on its official product page here <a href="https://www.3ds.com/products/catia/no-magic/teamwork-cloud" class="">https://www.3ds.com/products/catia/no-magic/teamwork-cloud</a>.</p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><strong>Related pages</strong></p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="09ed7a7f-f062-4a93-8bd4-82bf2265430f" /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=243970115 space=CM version=2 -->
## PAGE 00338: Using Used Projects Auto Update Wizard

- page_id: `243970115`
- space_key: `CM`
- source_url: https://docs.nomagic.com/spaces/CM/pages/243970115/Using+Used+Projects+Auto+Update+Wizard
- version_number: 2
- version_date: `2025-09-12T12:45:42.092+02:00`
- ancestors: Client-Side Collaborative Modeling Documentation > Using Teamwork Cloud > Used Projects Auto Updater Plugin
- labels: []

### NORMALIZED CONTENT

This section describes how to use the Used Projects Auto Update Wizard to configure and generate a properties file.

#### NOTE: Prerequisites

Prerequisites

- [CONFLUENCE_PAGE title='Used Projects Auto Updater Plugin' space=''] .
- It is highly recommended to log in to Teamwork Cloud with a dedicated user. This is the only way to ensure that all dedicated user permissions are checked and the properties file is configured correctly.
- Projects within the update path will require these permissions: Administer Resources; Edit Resource; Edit Resource Properties; Read Resources. However, the target used project only needs the Read Resources permission. Example: If you have projects: A, B, and C and these projects are in use as follows A->B->C (project A is using project B; project B is using project C). To update project B to the latest version, you only need the Read Resources permission for project B and**the Administer Resources, Edit Resources, Edit Resource Properties, and Read Resource permissions for project A. However, to update used projects B and C, you need the Administer Resources, Edit Resources, Edit Resource Properties, and Read Resources permissions for projects A and B. You will need only the Read Resources permission for project C.

After the plugin is enabled in the **Project Usages**dialog you will see a new button: **Used Projects Auto Update Wizard** [IMAGE alt='' src=''].

To generate a properties file with the Used Projects Auto Update Wizard

1. Log in to Teamwork Cloud with the dedicated user.
2. Open the project the used project of which you want to update.
3. In the main menu, go to Options > Project Usages .
4. In the Project Usages dialog, click [ATTACHMENT filename='Used_project_update_wizard.png'] . In the opened **Used Projects Auto Update Wizard**dialog, you can see the username you are logged in with. This user will be set up in the properties file to automatically update used projects.
5. Depending on your authentication type, fill in the following boxes:
  - [CONFLUENCE_PAGE title='Starting a collaboration session' space='']:
    - Properties file - specify the location and name for the properties file. 
 
[IMAGE alt='' src='']
  - [CONFLUENCE_PAGE title='Single Sign-On Authentication' space='']:
    - **Access Token** - enter a personal access token generated using the My account application in the Teamwork Cloud web UI. To learn more, see [CONFLUENCE_PAGE title='Generating a personal access token' space='MCS']. You can specify only the personal access token generated with your user. An access token generated by another user will not be accepted.
    - Properties file - specify the location and name for the properties file. 
 
[IMAGE alt='' src='']
6. Click the Next button.
7. Select directly and indirectly used projects you want to update. The values listed in the Status column show whether or not a used project can be updated. To see where the selected used project is used, click the Project Usage Information button. This will help to find update paths. An update path is a path of projects that must be updated in order to update a certain used project. The plugin does not update used projects that are involved in cyclic dependencies. [ATTACHMENT filename='selecting_projects.png']
8. Click the Generate button to create the properties file that can later be used in the [CONFLUENCE_PAGE title='Updating a used project with a command line' space='']

##### Possible errors and warnings with explanations

#### NOTE: Warning: Causes version conflict with at least one used project.

Warning: Causes version conflict with at least one used project.

This warning indicates that in this project, there is at least one other unselected used project that is using the same project. In order to achieve consistency on the model, we recommend updating all used projects that use this particular project.

#### WARNING: ERROR: Cannot be updated due to insufficient permissions.

ERROR: Cannot be updated due to insufficient permissions.

This error indicates that the user who is logged in does not have enough permissions to update this particular project. Please add required permissions for the user in order to update this project.

#### WARNING: ERROR: Cannot be updated due to read-only using project

ERROR: Cannot be updated due to read-only using project

This error indicates that the used project is being used in a read-only project (e.g. public branch); thus, we can not commit a new version of a read-only project in order to update the selected project. Please use this project directly or in another project with a branch for which the user has read-writepermissions.

#### WARNING: ERROR: Cannot be updated due to cyclic usage.

ERROR: Cannot be updated due to cyclic usage.

This error indicates that the used project has cyclic dependencies between projects. Please remove any used projects from this used project that would cause a cycle between projects.

#### WARNING: An example

ERROR: Cannot be updated due to missing update path.

This error can appear on indirectly used projects due to a missing update path. An *update path* is a path of projects that must be updated in order to update a certain used project. The following example explains this term:

#### TIP: An example

An example

A Main Project uses project A. Project A uses Project B. In order to update Project B in the Main Project, we are required to update Project B in Project A first and then update Project A in the Main Project. Thus, the update path for Project B is: Main Project > Project A.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>This section describes how to use the Used Projects Auto Update Wizard to configure and generate a <ac:inline-comment-marker ac:ref="92f667a6-75a6-4286-b5c8-e950ad2e359b">properties</ac:inline-comment-marker> file.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="7342971b-38a2-4452-bbb0-73b7078d9019"><ac:parameter ac:name="title">Prerequisites</ac:parameter><ac:rich-text-body><ul><li><ac:link><ri:page ri:content-title="Used Projects Auto Updater Plugin" /><ac:plain-text-link-body><![CDATA[The Used Projects Auto Updater plugin must be enabled in your modeling tool]]></ac:plain-text-link-body></ac:link>.</li><li>It is highly recommended to log in to Teamwork Cloud with a dedicated user. This is the only way to ensure that all dedicated user permissions are checked and the properties file is configured correctly.</li><li>Projects within the update path will require these permissions: Administer Resources; Edit Resource; Edit Resource Properties; Read Resources. However, the target used project only needs the Read Resources permission.<br /><p>Example: If you have projects: A, B, and C and these projects are in use as follows A-&gt;B-&gt;C (project A is using project B; project B is using project C). To update project B to the latest version, you only need the Read Resources permission for project B and<em> </em>the Administer Resources, Edit Resources, Edit Resource Properties, and Read Resource permissions for project A.</p><p>However, to update used projects B and C, you need the Administer Resources, Edit Resources, Edit Resource Properties, and Read Resources permissions for projects A and B. You will need only the Read Resources permission for project C.</p></li></ul></ac:rich-text-body></ac:structured-macro><p>After the plugin is enabled in the <strong>Project Usages </strong>dialog you will see a new button: <strong> <ac:inline-comment-marker ac:ref="41ff9961-fcdf-4017-8be7-954c0ace5cbf">Used Projects Auto Update Wizard</ac:inline-comment-marker> </strong> <ac:image><ri:attachment ri:filename="Used_project_update_wizard.png" /></ac:image>. </p><p><br /></p><p>To generate a properties file with the <span style="color: rgb(62,63,64);">Used Projects Auto Update Wizard</span></p><hr /><ol><li><span>Log in to Teamwork Cloud with the dedicated user.</span></li><li><span>Open the project the used project of which you want to update. </span></li><li>In the main menu, go to <strong>Options</strong> &gt; <strong>Project Usages</strong>.</li><li>In the Project Usages dialog, click <ac:image><ri:attachment ri:filename="Used_project_update_wizard.png" /></ac:image>.<br /><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="d9cc1e87-4bba-495b-a5ee-f3b37f1486e0"><ac:rich-text-body>In the opened <strong style="letter-spacing: 0.0px;">Used Projects Auto Update Wizard</strong><span style="letter-spacing: 0.0px;"> dialog, you can see the username you are logged in with. This user will be set up in the properties file to automatically update used projects.</span></ac:rich-text-body></ac:structured-macro></li><li><span style="letter-spacing: 0.0px;">Depending on your authentication type, fill in the following boxes:</span><ul><li><span style="letter-spacing: 0.0px;"><ac:link><ri:page ri:content-title="Starting a collaboration session" /><ac:plain-text-link-body><![CDATA[For standalone authentication]]></ac:plain-text-link-body></ac:link>:</span><ul><li><strong><span style="letter-spacing: 0.0px;">Properties file</span></strong><span style="letter-spacing: 0.0px;"> - specify the location and name for the properties file.<br /><br /><ac:image><ri:attachment ri:filename="used_projects_auto_update_wizard_standalone.png" /></ac:image><br /><br /></span></li></ul></li><li><span style="letter-spacing: 0.0px;"><ac:link><ri:page ri:content-title="Single Sign-On Authentication" /><ac:plain-text-link-body><![CDATA[For single sign-on authentication]]></ac:plain-text-link-body></ac:link>:</span><ul><li><span style="letter-spacing: 0.0px;"><strong>Access Token</strong> - enter a personal access token generated using the My account application in the Teamwork Cloud web UI. To learn more, see <ac:link><ri:page ri:space-key="MCS" ri:content-title="Generating a personal access token" /></ac:link>.<br /></span><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="a2b11369-2fef-417d-aa05-854dac50e090"><ac:rich-text-body><p>You can specify only the personal access token generated with your user. An access token generated by another user will not be accepted.</p></ac:rich-text-body></ac:structured-macro></li><li><strong><span>Properties file</span></strong><span> - specify the location and name for the properties file.<br /><br /><ac:image><ri:attachment ri:filename="used_projects_auto_update_wizard_SSO.png" /></ac:image><br /><br /></span></li></ul></li></ul></li><li>Click the <strong>Next</strong> button.</li><li>Select directly and indirectly used projects you want to update. The values listed in the Status column show whether or not a used project can be updated.<br /><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="33088006-f2e6-431d-b8a8-74b9461f51e0"><ac:rich-text-body><p>To see where the selected used project is used, click the Project Usage Information button. This will help to find update paths. An  update path is a path of projects that must be updated in order to update a certain used project.</p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="41787576-4817-4308-83e0-109d56142c9e"><ac:rich-text-body><p>The plugin does not update used projects that are involved in cyclic dependencies.</p></ac:rich-text-body></ac:structured-macro><br /><ac:image><ri:attachment ri:filename="selecting_projects.png" /></ac:image><br /><br /></li><li>Click the <strong>Generate</strong> button to create the properties <span style="color: rgb(62,63,64);">file that can later be used in the </span><ac:link><ri:page ri:content-title="Updating a used project with a command line" /><ac:plain-text-link-body><![CDATA[command line tool.]]></ac:plain-text-link-body></ac:link> </li></ol><h3><ac:inline-comment-marker ac:ref="42936a95-7c3a-4b45-83b0-3333ea38106f">Possible errors and warnings with explanations</ac:inline-comment-marker></h3><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="d2e3787b-9670-48f7-bffd-cc788819adcd"><ac:parameter ac:name="title">Warning: Causes version conflict with at least one used project.</ac:parameter><ac:rich-text-body><p>This warning indicates that in this project, there is at least one other unselected used project that is using the same project. In order to achieve consistency on the model, we recommend updating all used projects that use this particular project.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="warning" ac:schema-version="1" ac:macro-id="b5007f5d-eec9-4c30-85a4-5de0682771ae"><ac:parameter ac:name="title">ERROR: Cannot be updated due to insufficient permissions.</ac:parameter><ac:rich-text-body><p>This error indicates that the user who is logged in does not have enough permissions to update this particular project. Please add required permissions for the user in order to update this project.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="warning" ac:schema-version="1" ac:macro-id="5d74f35d-77a1-4e65-86ea-b7b696bb3383"><ac:parameter ac:name="title">ERROR: Cannot be updated due to read-only using project</ac:parameter><ac:rich-text-body><p><ac:inline-comment-marker ac:ref="64ee466b-baa9-43ea-9aa7-c46fb6d48a12">This error indicates that the used project is being used in a read-only project</ac:inline-comment-marker> (e.g. public branch); thus, we can not commit a new version of a read-only project in order to update the selected project. Please use this project directly or in another project with a branch for which the user has read-write<ac:inline-comment-marker ac:ref="49f66af9-f794-4e4a-b44e-0499c823a8ac"> permissions</ac:inline-comment-marker>.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="warning" ac:schema-version="1" ac:macro-id="de592071-950c-48bc-a8ce-e39cdba4b70c"><ac:parameter ac:name="title">ERROR: Cannot be updated due to cyclic usage.</ac:parameter><ac:rich-text-body><p>This error indicates that the used project has cyclic dependencies between projects. Please remove any used projects from this used project that would cause a cycle between projects.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="warning" ac:schema-version="1" ac:macro-id="e23c969d-dcf0-44ef-9631-d829a2f3e72b"><ac:parameter ac:name="title">ERROR: Cannot be updated due to missing update path.</ac:parameter><ac:rich-text-body><p>This error can appear on indirectly used projects due to a missing update path. An <span style="color: rgb(62,63,64);"> <em>update path</em> is a path of projects that must be updated in order to update a certain used project.</span> The following example explains this term:</p><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="f6278403-e177-45ac-9a06-5127b9537bb3"><ac:parameter ac:name="title">An example</ac:parameter><ac:rich-text-body><p>A Main Project uses project A. Project A uses Project B. In order to update Project B in the Main Project, we are required to update Project B in Project A first and then update Project A in the Main Project. Thus, the update path for Project B is: Main Project &gt; Project A. </p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p>
````

<!--NOMAGIC_PAGE id=246155722 space=CM version=1 -->
## PAGE 00339: Versions of Collaborative Modeling Documentation

- page_id: `246155722`
- space_key: `CM`
- source_url: https://docs.nomagic.com/spaces/CM/pages/246155722/Versions+of+Collaborative+Modeling+Documentation
- version_number: 1
- version_date: `2025-08-01T13:12:58.466+02:00`
- ancestors: 
- labels: []

### NORMALIZED CONTENT

2ed10a9d0797a6aefd946e76e739404d

Collaborative Modeling Documentation

documentVersions

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="scroll-document-location" ac:schema-version="1" ac:macro-id="8cdc8815-07eb-4901-ba72-af19a2309ce2"><ac:parameter ac:name="permaId">2ed10a9d0797a6aefd946e76e739404d</ac:parameter><ac:parameter ac:name="documentTitle">Collaborative Modeling Documentation</ac:parameter><ac:parameter ac:name="key">documentVersions</ac:parameter></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=243970213 space=CM version=1 -->
## PAGE 00340: Viewing project history

- page_id: `243970213`
- space_key: `CM`
- source_url: https://docs.nomagic.com/spaces/CM/pages/243970213/Viewing+project+history
- version_number: 1
- version_date: `2025-07-31T10:51:46.044+02:00`
- ancestors: Client-Side Collaborative Modeling Documentation > Collaboration powered by 3DEXPERIENCE platform
- labels: []

### NORMALIZED CONTENT

After logging in to the **3D**EXPERIENCE platform, you can view the history of any project on the server. In addition to seeing who made changes to a project and when, you can also open a historical iteration of a project.

To view project history

1. Do one of the following:
  - In the main menu of a modeling tool, select Collaborate > Projects .
  - In the main menu of a modeling tool, select Collaborate > Open Server Project .
2. In the open dialog, click [IMAGE alt='' src=''] on the tile of the project whose history you want to view and select **Project History**. The **History** dialog opens displaying the project history. [IMAGE alt='' src=''] Viewing version propertiesTo view the properties of a specific project iteration, in the **History** dialog, select a project iteration and click the **Properties** button. The **Iteration Properties** dialog opens displaying project iteration details, such as the commit comment, used projects, and the list of programs and plugins required to open the project.If a specific iteration was merged, the **Iteration** column of the **History** dialog shows the source iteration from which it was merged, e.g., (merged from 2.A (3)).

##### Opening historic project iterations

You can open and view a historic project iteration in a modeling tool as described below. However, historic project iterations cannot be edited, updated, or committed to the server.

To open a historic project iteration

1. Do one of the following:
  - In the main menu of a modeling tool, select Collaborate > Projects .
  - In the main menu of a modeling tool, select Collaborate > Open Server Project .
2. In the open dialog, click [IMAGE alt='' src=''] on the tile of the project whose historical iteration you want to open and select **Project History**.
3. In the History dialog, select the iteration you want to open and click the Open button. [ATTACHMENT filename='opening_historical_version.png']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>After logging in to the <span style="color: rgb(55,65,81);"><strong>3D</strong>EXPERIENCE</span> platform, you can view the history <span style="color: rgb(62,63,64);">of any project on the server. In addition to seeing who made changes to a project and when, you can also open a historical iteration of a project.</span></p><p><br /></p><p>To view project history</p><hr /><ol><li>Do one of the following:<br /><ul><li>In the main menu of a modeling tool, select <strong>Collaborate</strong> &gt; <strong>Projects</strong>.</li><li>In the main menu of a modeling tool, select <strong>Collaborate</strong> &gt; <strong>Open Server Project</strong>.</li></ul></li><li><p class="auto-cursor-target">In the open dialog, click <ac:image ac:thumbnail="true" ac:height="12"><ri:attachment ri:filename="expand_arrow.png" /></ac:image> on the tile of the project whose history you want to view and select <strong>Project History</strong>. The <strong>History</strong> dialog opens displaying the project history.</p><p class="auto-cursor-target"><br /><ac:image><ri:attachment ri:filename="project_history.png" /></ac:image></p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="cd550d4c-e735-4c46-ae95-046b0c320db0"><ac:parameter ac:name="title">Viewing version properties</ac:parameter><ac:rich-text-body><ul><li>To view the properties of a specific project iteration, in the <strong>History</strong> dialog, <span>select a project iteration</span> and click the <strong>Properties</strong> button. The <strong>Iteration Properties</strong> dialog opens displaying project iteration details, such as the commit comment, used projects, and the list of programs and plugins required to open the project.</li><li>If a specific iteration was merged, the <strong>Iteration</strong> column of the <strong>History</strong> dialog shows the source iteration from which it was merged, e.g., (merged from 2.A (3)).</li></ul></ac:rich-text-body></ac:structured-macro></li></ol><h3>Opening historic project iterations</h3><p>You can open and view a historic project iteration in a modeling tool as described below. However, historic project iterations cannot be edited, updated, or committed to the server.</p><p><br /></p><p>To open a historic project iteration</p><hr /><ol><li>Do one of the following:<br /><ul><li>In the main menu of a modeling tool, select <strong>Collaborate</strong> &gt; <strong>Projects</strong>.</li><li>In the main menu of a modeling tool, select <strong>Collaborate</strong> &gt; <strong>Open Server Project</strong>.</li></ul></li><li><p class="auto-cursor-target">In the open dialog, click <ac:image ac:thumbnail="true" ac:height="12"><ri:attachment ri:filename="expand_arrow.png" /></ac:image> on the tile of the project whose historical iteration you want to open and select <strong>Project History</strong>.</p></li><li>In the <strong>History</strong> dialog, select the iteration you want to open and click the <strong>Open</strong> button.<br /><br /><ac:image><ri:attachment ri:filename="opening_historical_version.png" /></ac:image></li></ol>
````

<!--NOMAGIC_PAGE id=243969746 space=CM version=2 -->
## PAGE 00341: Viewing Version Properties

- page_id: `243969746`
- space_key: `CM`
- source_url: https://docs.nomagic.com/spaces/CM/pages/243969746/Viewing+Version+Properties
- version_number: 2
- version_date: `2025-09-12T12:45:09.876+02:00`
- ancestors: Client-Side Collaborative Modeling Documentation > Using Teamwork Cloud > Managing server projects
- labels: []

### NORMALIZED CONTENT

The **Version Properties** dialog shows project version information, for example, comments, tags, modules, and meta information.

To open the Version Properties dialog

1. From the Collaborate menu, select Open Server Project or Projects... .
2. Select a project and click the [ATTACHMENT filename='version_properties.png'] button on the Collaboration toolbar. OR Right-click a project and select Version Properties. 
 
[IMAGE alt='' src='']
3. In the Version Properties dialog, you can:
  - View the project author, version number, and creation date with the time zone: [ATTACHMENT filename='version_properties_project_info.png']
  - View project comments in the Comment tab.
  - Add the Major tag in the Tags tab to set the selected project as the major version: [ATTACHMENT filename='tags_version_properties.png']
  - View used projects in the Used Projects tab.
  - Select the Meta information tab to see which programs and plugins are required to open the selected project: [ATTACHMENT filename='meta_information.png']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>The <strong>Version Properties</strong> dialog shows project version information, for example, comments, tags, modules, and meta information.</p><p>To open the Version Properties dialog</p><hr /><ol><li>From the <strong>Collaborate</strong> menu, select <strong>Open Server Project </strong>or<strong> Projects...</strong>.</li><li>Select a project and click the <ac:image ac:thumbnail="true" ac:height="23"><ri:attachment ri:filename="version_properties.png"><ri:page ri:space-key="MT" ri:content-title="Opening projects from Teamwork Cloud" /></ri:attachment></ac:image> button on the <strong>Collaboration</strong> toolbar.<br />OR<br />Right-click a project and select <strong>Version Properties.<br /><br /><ac:image ac:height="400"><ri:attachment ri:filename="version_properties.png" /></ac:image><br /><br /></strong></li><li>In the Version Properties dialog, you can:<ul><li><span style="letter-spacing: 0.0px;">View the project author, version number, and creation date with the time zone:<br /><br /></span><ac:image ac:height="400"><ri:attachment ri:filename="version_properties_project_info.png" /></ac:image><br /><br /></li><li>View project comments in the <strong>Comment </strong>tab.</li><li>Add the <em>Major </em>tag in the <strong>Tags </strong>tab to set the selected project as the major version:<br /><br /><ac:image ac:height="400"><ri:attachment ri:filename="tags_version_properties.png" /></ac:image><br /><br /></li><li>View used projects in the <strong>Used Projects</strong> tab.</li><li>Select the <strong>Meta information</strong> tab to see which programs and plugins are required to open the selected project:<br /><br /><ac:image ac:height="400"><ri:attachment ri:filename="meta_information.png" /></ac:image></li></ul></li></ol>
````

<!--NOMAGIC_PAGE id=286556224 space=CM version=9 -->
## PAGE 00342: Working in Offline Mode

- page_id: `286556224`
- space_key: `CM`
- source_url: https://docs.nomagic.com/spaces/CM/pages/286556224/Working+in+Offline+Mode
- version_number: 9
- version_date: `2026-02-18T13:20:28.139+01:00`
- ancestors: Client-Side Collaborative Modeling Documentation > Collaboration powered by 3DEXPERIENCE platform > Technical practices
- labels: []

### NORMALIZED CONTENT

This Technical Practice highlights the use of the offline mode in CATIA Magic. In case of low bandwidth or unstable internet connectivity or technical issues, users will learn to create an offline copy of a CATIA Magic project to work without being connected to the**3D**EXPERIENCE platform.It also explains how to synchronize the project once the user is back online.

#### Why

A CATIA Magic user may not need to interact with the platform to independently work on the CATIA magic project. When a user has limited bandwidth, they can avoid unnecessary interaction with the platform to effectively utilize the available bandwidth. When a user is accessing a network with unstable connectivity, there is a possibility of data loss while interacting with the platform.

#### What

This technical practice highlights the use of the offline mode in CATIA Magic. In case of low bandwidth or unstable internet connectivity or technical issues, users will learn to create an offline copy of a CATIA Magic project to work without being connected to the**3D**EXPERIENCE platform. It also explains how to synchronize the project once the user is back online.

#### Target Audience

Systems Engineer, Systems Architect

#### Knowledge

##### Lock and Unlock a Project

Managing access to the projects becomes crucial while working with a team. Let us read more about locking and unlocking of the CATIA Magic project and it's elements.

###### Lock Elements and Diagrams

You must lock the part of the model you are going to edit to prevent other users from editing it at the same time. An element/ object can only be locked by one user at a time. Once it is locked, other users can only access it but not edit it.

The following table lists editable elements after you lock a single element, single diagram, diagram with elements, symbol styles and project usages.

| When you lock... | You can... |
| --- | --- |
| Element | Edit element specification properties (in the Specification window) |
| Diagram | Edit:Diagram specification properties (in the Specification window)Diagram properties (in the Diagram Properties dialog)Symbol layout on the diagram paneSymbol properties (in the Symbol Properties dialog) |
| Diagram with elements | Edit:Diagram specification properties (in the Specification window)Element specification properties (in the Specification window and on the diagram pane)Diagram properties (in the Symbol Properties dialog)Symbol properties (in the Symbol Properties dialog)Symbol layout on the diagram pane |
| Symbol styles | Edit properties of symbol styles (in the Project Options dialog) |
| Project usages | Import used projects as packages into the main projectStop using projectsChange versions of used projects |

###### Unlock Elements and Diagrams

You can use commands from the shortcut menu to unlock elements and diagrams. Unlocking modified elements will trigger to commit the project. 
[IMAGE alt='' src='']

##### Project Branching

Project branching enables multiple users to work on the same model at the same time. For this, you need to create a project branch, which is a copy of the project. You can modify the branch as required, independent of other branches. Branches can be merged back when required. Conflicts between the branches are resolved during the merge process.

#### Use Cases

##### Use Case: Working in Offline Mode

###### Scenario

A systems engineer is assigned to make changes in the CATIA Magic project. He is currently in the low bandwidth area, due to which he cannot be continuously connected to the**3D**EXPERIENCE platform. Let us see how the systems engineer uses CATIA Magic in offline mode for making the changes and later commits the project in the**3D**EXPERIENCE platform.

###### Actors/personas

Mark, Systems Architect: Mark is responsible to make changes in the CATIA Magic model. But due to low bandwidth, he cannot be continuously connected to the**3D**EXPERIENCE platform. He now needs to work on the CATIA Magic model in the offline mode and later commit the modification to the server.

##### Workflow

[IMAGE alt='' src='']

#### How

##### Prerequisite Roles

3DSwymer (IFW-OC), Collaborative Industry Innovator (CSV-OC), Collaborative Designer for CATIA Magic (SSY-OC)

##### Step 1: Open CATIA Magic Model

600400

##### Step 2: Work in Offline Mode

600400

#### Recommandation

There is no need to commit the project at every little change. If a task is in work, the project can be saved locally and committed once all the modifications are complete.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="title topictitle2" style="text-align: left;"><span class="shortdesc" style="color:var(--ds-text,#000000);">This Technical Practice highlights the use of the offline mode in CATIA Magic. In case of low bandwidth or unstable internet connectivity or technical issues, users will learn to create an offline copy of a CATIA Magic project to work without being connected to the<span> </span><span class="ph"><strong><span class="tm-3D">3D</span></strong>EXPERIENCE platform</span>.</span><span style="color:var(--ds-text,#000000);"><span> </span>It also explains how to synchronize the project once the user is back online.</span></p><h2 class="title topictitle2" style="text-align: left;">Why</h2><p>A CATIA Magic user may not need to interact with the platform to independently work on the CATIA magic project. When a user has limited bandwidth, they can avoid unnecessary interaction with the platform to effectively utilize the available bandwidth. When a user is accessing a network with unstable connectivity, there is a possibility of data loss while interacting with the platform.</p><h2 class="title topictitle2" style="text-align: left;">What</h2><p>This technical practice highlights the use of the offline mode in CATIA Magic. In case of low bandwidth or unstable internet connectivity or technical issues, users will learn to create an offline copy of a CATIA Magic project to work without being connected to the<span> </span><span class="ph"><strong><span class="tm-3D">3D</span></strong>EXPERIENCE platform</span>. It also explains how to synchronize the project once the user is back online.</p><h2 class="title topictitle2" style="text-align: left;">Target Audience</h2><p>Systems Engineer, Systems Architect</p><h2 class="title topictitle2" style="text-align: left;">Knowledge</h2><h3 class="title topictitle3" style="text-align: left;margin-left: 0.0px;">Lock and Unlock a Project</h3><p>Managing access to the projects becomes crucial while working with a team. Let us read more about locking and unlocking of the CATIA Magic project and it's elements.</p><h4 class="title topictitle4" style="text-align: left;margin-left: 0.0px;">Lock Elements and Diagrams</h4><p>You must lock the part of the model you are going to edit to prevent other users from editing it at the same time. An element/ object can only be locked by one user at a time. Once it is locked, other users can only access it but not edit it.</p><p>The following table lists editable elements after you lock a single element, single diagram, diagram with elements, symbol styles and project usages.</p><table class="wrapped" style="margin-left: 0.0px;"><thead class=""><tr class=""><th style="text-align: left;vertical-align: middle;">When you lock...</th><th style="text-align: left;vertical-align: middle;">You can...</th></tr></thead><tbody class=""><tr class=""><td>Element</td><td>Edit element specification properties (in the<span> </span><strong><span class="keyword wintitle" style="color:var(--ds-text,#333333);">Specification</span> </strong>window)</td></tr><tr class=""><td>Diagram</td><td>Edit:<ul class="ul"><li class="li" data-uuid="071bbec7-58f9-4da8-bf96-9e24e010b415">Diagram specification properties (in the<span> </span><strong><span class="keyword wintitle" style="color:var(--ds-text,#333333);">Specification</span> </strong>window)</li><li class="li" data-uuid="07e150db-58b4-4639-ac7a-9ba963f8a700">Diagram properties (in the<span> </span><strong><span class="keyword wintitle" style="color:var(--ds-text,#333333);">Diagram Properties</span></strong><span> </span>dialog)</li><li class="li" data-uuid="f64741ad-4a52-4af5-93a0-8a318c9fab28">Symbol layout on the diagram pane</li><li class="li" data-uuid="57830e31-7ca6-4a22-b61c-aee1f8f2e01d">Symbol properties (in the<span> </span><strong><span class="keyword wintitle" style="color:var(--ds-text,#333333);">Symbol Properties</span></strong><span> </span>dialog)</li></ul></td></tr><tr class=""><td>Diagram with elements</td><td>Edit:<ul class="ul"><li class="li" data-uuid="851179ff-4dc6-4361-a280-891a2e1d9451">Diagram specification properties (in the <strong>Specification </strong>window)</li><li class="li" data-uuid="e3df24f0-2d77-4b59-a2cf-0173e6d91730">Element specification properties (in the <strong>Specification </strong>window and on the diagram pane)</li><li class="li" data-uuid="67347eb0-81aa-4dc0-9c93-3060b611e55a">Diagram properties (in the<span> </span><strong><span class="keyword wintitle" style="color:var(--ds-text,#333333);">Symbol Properties</span></strong><span> </span>dialog)</li><li class="li" data-uuid="8da818fa-86ba-4b48-923e-dd49dd1b22b1">Symbol properties (in the<span> </span><strong><span class="keyword wintitle" style="color:var(--ds-text,#333333);">Symbol Properties</span></strong><span> </span>dialog)</li><li class="li" data-uuid="544eddc3-9348-4f76-b6f8-ac368a5f5c4a">Symbol layout on the diagram pane</li></ul></td></tr><tr class=""><td>Symbol styles</td><td>Edit properties of symbol styles (in the<span> </span><span class="keyword wintitle" style="color:var(--ds-text,#333333);"><strong>Project Options</strong><span> </span></span>dialog)</td></tr><tr class=""><td>Project usages</td><td><ul class="ul"><li class="li" data-uuid="a48a7406-cc67-41e3-9498-6d6c3d88d30b">Import used projects as packages into the main project</li><li class="li" data-uuid="48d00eaf-2b24-4eb3-9195-dd62dcfcd345">Stop using projects</li><li class="li" data-uuid="da02b122-0375-4f1c-8a71-c7303884fad7">Change versions of used projects</li></ul></td></tr></tbody></table><h4 class="title topictitle4" style="text-align: left;margin-left: 0.0px;">Unlock Elements and Diagrams</h4><p>You can use commands from the shortcut menu to unlock elements and diagrams. Unlocking modified elements will trigger to commit the project.<br /><ac:image><ri:attachment ri:filename="techPract_OfflineMode_UnlockElements.png" /></ac:image></p><h3 class="title topictitle3" style="text-align: left;margin-left: 0.0px;">Project Branching</h3><p>Project branching enables multiple users to work on the same model at the same time. For this, you need to create a project branch, which is a copy of the project. You can modify the branch as required, independent of other branches. Branches can be merged back when required. Conflicts between the branches are resolved during the merge process.</p><h2 class="title topictitle2" style="text-align: left;">Use Cases</h2><h3 class="title topictitle3" style="text-align: left;margin-left: 0.0px;">Use Case: Working in Offline Mode</h3><h4 class="title topictitle4" style="text-align: left;margin-left: 0.0px;">Scenario</h4><p>A systems engineer is assigned to make changes in the CATIA Magic project. He is currently in the low bandwidth area, due to which he cannot be continuously connected to the<span> </span><span class="ph"><strong><span class="tm-3D">3D</span></strong>EXPERIENCE platform</span>. Let us see how the systems engineer uses CATIA Magic in offline mode for making the changes and later commits the project in the<span> </span><span class="ph"><strong><span class="tm-3D">3D</span></strong>EXPERIENCE platform</span>.</p><h4 class="title topictitle4" style="text-align: left;margin-left: 0.0px;">Actors/personas</h4><p>Mark, Systems Architect: Mark is responsible to make changes in the CATIA Magic model. But due to low bandwidth, he cannot be continuously connected to the<span> </span><span class="ph"><strong><span class="tm-3D">3D</span></strong>EXPERIENCE platform</span>. He now needs to work on the CATIA Magic model in the offline mode and later commit the modification to the server.</p><h3 class="title topictitle3" style="text-align: left;margin-left: 0.0px;">Workflow</h3><p><br /><ac:image ac:height="250"><ri:attachment ri:filename="techPract_OfflineMode_Workflow.png" /></ac:image><br /><br /></p><h2 class="title topictitle2" style="text-align: left;">How</h2><h3 class="title topictitle3" style="text-align: left;margin-left: 0.0px;">Prerequisite Roles</h3><p>3DSwymer (IFW-OC), Collaborative Industry Innovator (CSV-OC), Collaborative Designer for CATIA Magic (SSY-OC)</p><h3 class="title topictitle3" style="text-align: left;margin-left: 0.0px;">Step 1: Open CATIA Magic Model</h3><p><ac:structured-macro ac:name="widget" ac:schema-version="1" ac:macro-id="b61930ba-1e07-4e56-a293-740653d30d85"><ac:parameter ac:name="width">600</ac:parameter><ac:parameter ac:name="url"><ri:url ri:value="https://www.youtube.com/watch?v=k-917SJX3xE&amp;list=PLlvXsDYdI5UMPvWYNEF0F4Rq0w18dsMJz" /></ac:parameter><ac:parameter ac:name="height">400</ac:parameter></ac:structured-macro></p><h3 class="title topictitle3" style="text-align: left;margin-left: 0.0px;">Step 2: Work in Offline Mode</h3><p><ac:structured-macro ac:name="widget" ac:schema-version="1" ac:macro-id="161771aa-527e-4455-bdcc-3a02c07d9329"><ac:parameter ac:name="width">600</ac:parameter><ac:parameter ac:name="url"><ri:url ri:value="https://www.youtube.com/watch?v=Zvlg0fGuiTA&amp;list=PLlvXsDYdI5UMPvWYNEF0F4Rq0w18dsMJz" /></ac:parameter><ac:parameter ac:name="height">400</ac:parameter></ac:structured-macro></p><h2 class="title topictitle2" style="text-align: left;">Recommandation</h2><p>There is no need to commit the project at every little change. If a task is in work, the project can be saved locally and committed once all the modifications are complete.</p>
````
