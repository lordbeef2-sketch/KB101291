# NOMAGIC DOCUMENTATION SPACE: SysML v2 Modeling

<!--NOMAGIC_SPACE key=SYSML2P chunk=12 -->

<!--NOMAGIC_PAGE id=249577495 space=SYSML2P version=8 -->
## PAGE 00736: Use case scenario

- page_id: `249577495`
- space_key: `SYSML2P`
- source_url: https://docs.nomagic.com/spaces/SYSML2P/pages/249577495/Use+case+scenario
- version_number: 8
- version_date: `2025-12-17T15:28:05.740+01:00`
- ancestors: SysML v2 Plugin Documentation > Model composition > Behavior > Use cases
- labels: []

### NORMALIZED CONTENT

A use case scenario can be captured in an include use case symbol with a swimlane grid, where each swimlane represents the subject and actor parameters responsible for performing specific actions, depicting the use case scenario of expected interaction between involved participants.

The swimlane grid symbol allows you to model and organize actions based on the elements that are responsible for performing those actions. For more information on swimlanes, see the [CONFLUENCE_PAGE title='Swimlane grid' space=''] page.

Within the context of a part that owns or inherits an include use case, the include use case contains actions that are performed by the subject and actor parameters owned or inherited by the include use case. Thus, the swimlane grid symbol is displayed for the include use case, where each individual swimlane in the swimlane pool represents each subject and actor. You can use swimlanes to model actions and their sequencing based on the performers, i.e., subject and actors that perform each action. The subject and actor names are indicated in the swimlane headers.

###### The use case*find person in distress*is included directly under the context part*drone in search and rescue mission*because it is specific to this context.Swimlanes in the include use case represent subject and actor parameters as performers of the actions in their corresponding swimlanes. These parameters are related to the subparts of the contextual part via subsetting.

##### Prerequisites

1. The include use case whose swimlanes represent the subject and actors is [CONFLUENCE_PAGE title='Displaying elements in symbolic views' space=''] in the view.
2. The include use case's subject and actors are already related to the contextual part's subparts via [CONFLUENCE_PAGE title='Subsetting' space='']. See the procedures:
  1. 
  2. 

###### Relating the include use case's subject and actors to the contextual part's subparts through subsetting via the Textual Editor

To relate the include use case's subject and actors to the contextual part's subparts through subsetting via the Textual Editor

1. In the Textual Editor, within the body of the contextual part, [CONFLUENCE_PAGE title='Creating use cases' space=''] with the [CONFLUENCE_PAGE title='Subjects, actors, and objectives for use cases' space=''] .
2. [CONFLUENCE_PAGE title='Subsetting' space=''] the contextual part’s subparts by the appropriate parameters of the include use case. You can now proceed to on the include use case symbol. part'drone in search and rescue mission'{part'ground control station';part'person in distress';part'search drone';includeusecase'find person in distress'{subject:>'search drone';actor:>'ground control station';actor:>'person in distress';}}

###### Relating the include use case's subject and actors to the contextual part's subparts throughsubsetting via the Drag and Drop handler in a view

To relate the include use case's subject and actors to the contextual part's subparts through subsetting via the Drag and Drop handler in a view

1. On the contextual part's symbol displayed in a view, [CONFLUENCE_PAGE title='Creating use cases' space=''] .
2. [CONFLUENCE_PAGE title='Subjects, actors, and objectives for use cases' space=''] the contextual part’s subparts by the appropriate parameters of the include use case using the Drag and Drop handler commands **Create Subject**, **Create Actor**, or **Set Subsetted Feature** .

##### Managing swimlanes

###### Displaying the swimlane grid and creating additional swimlanes

To display the swimlane grid or create additional swimlanes

- To display the swimlane grid:
  - Right-click the include use case symbol and in the shortcut menu, click [CONFLUENCE_PAGE title='Displaying elements in symbolic views' space=''] , then Display Swimlanes . The swimlane grid is displayed with swimlanes (along with any actions and connectors that may already be defined in the model), representing subject and actors owned or inherited by the part that owns or inherits the include use case.

50%

part'drone in search and rescue mission'{part'ground control station';part'person in distress';part'search drone';includeusecase'find person in distress'{subject:>'search drone';actor:>'ground control station';actor:>'person in distress';}}

50%

[IMAGE alt='' src='']

- To create additional swimlanes:
  - Select the header of an existing swimlane and click the + button on the left or the right side of the swimlane, to create a swimlane to the left or the right of the existing one. Creating a new swimlane creates an actor for the include use case, represented by the new swimlane. However, no related subpart is created for the part that owns or inherits the include use case.

50%

[IMAGE alt='' src='']

part'drone in search and rescue mission'{part'ground control station';part'person in distress';part'search drone';includeusecase'find person in distress'{subject:>'search drone';actor:>'ground control station';actor:>'person in distress';}}

50%

[IMAGE alt='' src='']

part'drone in search and rescue mission'{part'ground control station';part'person in distress';part'search drone';includeusecase'find person in distress'{subject:>'search drone';actor:>'ground control station';actor:>'person in distress'; 
 actor actor1; // new actor represented by the newly created swimlane}}

If the include use case owns or inherits actors that are not yet displayed as swimlanes, clicking the + button displays a dropdown menu with the following categories:

- Display that has the following options:
  - actor <the name of the actor that does not yet have the corresponding swimlane displayed in the view> . Click to create the corresponding swimlane.
  - All . Click to create the corresponding swimlanes for all actors that are not represented in the swimlane symbol.
- Create that has the following option:
  - actor . Click to create an actor, represented by a new swimlane.

50%

[IMAGE alt='' src='']

50%

part'drone in search and rescue mission'{part'ground control station';part'person in distress';part'search drone';includeusecase'find person in distress'{subject:>'search drone';actor:>'ground control station';actor:>'person in distress'; // actor whose representative swimlane is not displayed yet, thus it is available in the Display dropdown menu}}

###### Displaying actions in swimlanes

To display actions in swimlanes

- Select one swimlane by right-clicking its header or all swimlanes by right-clicking the swimlane pool. In the shortcut menu, click [CONFLUENCE_PAGE title='Displaying elements in symbolic views' space='']**Display** , then Display Actions in the dropdown menu . The specific swimlane's shortcut menu contains the same commands as the part element symbol (subject or actor) it represents.

###### Displaying parameters, connectors, or other features for element symbols in swimlanes

To display parameters, connectors, or other features for element symbols in swimlanes

- Right-click element symbol(s) in the swimlane(s). In the shortcut menu, click [CONFLUENCE_PAGE title='Displaying elements in symbolic views' space='']**Display** , then click the appropriate command in its dropdown menu.

##### Modeling actions with swimlanes

###### Creating actions in swimlanes

You may create actions and the appropriate subject's or actor's perform actions via the Textual Editor and then display the actions in swimlanes via the procedure. However, you can create actions in swimlanes using the view palette. This way, the appropriate perform actions are automatically created for the subject and actors in whose representative swimlanes the actions are created.

To create actions in swimlanes

1. .
2. In the view palette, under the Actions group, click the button for the needed action.
3. Click on the swimlane representing the subject or actor that you want to perform the action. Indicate the start and end of an action sequenceusing start and done actions. See the [CONFLUENCE_PAGE title='Start and done actions' space=''] page.Connect and sequence actions using successions, flows, and succession flows. See the [CONFLUENCE_PAGE title='Action succession and flow' space=''] page.Control the sequencing of actions using control nodes. See the [CONFLUENCE_PAGE title='Control nodes' space=''] page.Start and done actions, as well as control nodes, are not performed, thus subject/actors in whose representative swimlanes they are displayed, do not have perform actions for performing them. These actions and nodes are owned by the include use case that owns the swimlane grid symbol, while their symbols are owned by the swimlane grid symbol.

50%

[IMAGE alt='' src='']

part'drone in search and rescue mission'{part'ground control station';part'search drone';includeusecase'find person in distress'{subject:>'search drone';actor:>'ground control station';}}

50%

[IMAGE alt='' src='']

part'drone in search and rescue mission'{ 
part'ground control station'; 
part'search drone'; 
includeusecase'find person in distress'{ 
subject:>'search drone'{ 
perform'fly to destination'; // perform action automatically created for the subject once theaction 'fly to destination'was created in the swimlane that represents the subject 'search drone' 
} 
actor:>'ground control station'{ 
perform'start mission'; // perform action automatically created for the part once the action 'start mission' was created in the swimlane that represents the actor 'ground control station' 
} 
action'start mission'{outmd; } // action created via view 
action'fly to destination'{inmd; } // action created via view 
successionflowof'Exchange Items'::'Mission Data'from'start mission'.mdto'fly to destination'.md; // succession flow created via view 
} 
}

###### Deleting actions in swimlanes

To delete actions in swimlanes

- To delete an action element or symbol in swimlane, see the procedure [CONFLUENCE_PAGE title='Managing elements' space=''] on the [CONFLUENCE_PAGE title='Managing elements' space=''] page. Deleting an action element via swimlane deletes the appropriate perform action from the subject/actor responsible for performing the deleted action. Any associated connectors are deleted as well.

###### Changing which subject or actor is responsible for performing actions via swimlanes

You can move actions between swimlanes to change which subject or actor is responsible for performing these actions. The responsible subject/actor is indicated in the header of the swimlane with the keyword «performer».

To change which subject or actor is responsible for performing actions via swimlanes

- Click and drag the action symbol itself from its source swimlane to the target swimlane of the needed include use case.

**Details regarding the change:**

- If the source and target swimlanes are in the same swimlane grid symbol owned by the common include use case, m oving an action from one swimlane to another updates which subject/actor is the owner of the perform action responsible for performing the moved action.

50%

[IMAGE alt='' src='']

part 'drone in search and rescue mission' { 
part 'ground control station'; 
 part 'search drone'; 
 include use case 'find person in distress' { 
 subject :> 'search drone'; 
 actor :> 'ground control station' { 
 perform 'start mission'; // perform action is owned bythe actor 'ground control station' 
 } 
 action 'start mission'; 
 } 
}

50%

[IMAGE alt='' src='']

part 'drone in search and rescue mission' { 
part 'ground control station'; 
 part 'search drone'; 
 include use case 'find person in distress' { 
 subject :> 'search drone' { 
 perform 'start mission'; // perform action is owned bythe subject 'search drone' 
 } 
 actor :> 'ground control station'; 
 action 'start mission'; 
 } 
}

- If the source and target swimlanes are in different swimlane grid symbols owned by different include use cases (see example below), m oving an action updates:
  - the moved action's owner to the new include use case;
  - which subject/actor is the owner of the perform action responsible for performing the moved action;
- The same applies ifthe moved action is not inherited or owned by the include use case that owns the target swimlane.

50%

[IMAGE alt='' src='']

part'drone mission'{ 
part'drone in any mission'{ 
part'ground control station'; 
part'search drone'; 
includeusecase'locate target'{ 
subject:>'search drone'; 
actor:>'ground control station'{ 
perform'start mission';// the actor 'ground control station' is the owner of the perform action responsible for performing the action 'start mission' 
} 
action'start mission';// the owner of the action 'start mission' is the include use case 'locate target' 
} 
} 
part'drone in search and rescue mission'{ 
part'ground control station'; 
part'search drone'; 
includeusecase'find person in distress'{ 
subject:>'search drone'; 
actor:>'ground control station'; 
} 
} 
}

50%

[IMAGE alt='' src='']

part'drone mission'{ 
part'drone in any mission'{ 
part'ground control station'; 
part'search drone'; 
includeusecase'locate target'{ 
subject:>'search drone'; 
actor:>'ground control station';// the previously owned action 'start mission' and the perform action for performing it is moved out 
} 
} 
part'drone in search and rescue mission'{ 
part'ground control station'; 
part'search drone'; 
includeusecase'find person in distress'{ 
subject:>'search drone'; 
actor:>'ground control station'{ 
perform'start mission';// the actor 'ground control station' is updated as the owner of the perform action responsible for performing the action 'start mission' 
} 
action'start mission';// the owner of the action 'start mission' is updated to the include use case 'find person in distress' 
} 
} 
}

###### Deleting subject or actor responsible for performing actions via swimlanes

To delete subject or actor responsible for performing actions via swimlanes

1. Select the header of the swimlane representing the subject or actor you want to delete.
2. Follow the procedure [CONFLUENCE_PAGE title='Managing elements' space=''] on the [CONFLUENCE_PAGE title='Managing elements' space=''] page.

Deleting subject or actor responsible for performing actions via swimlanes also deletes perform actions contained by the deleted subject/actor.

##### Extracting and/or reusing a common use caseand adapting its actions todifferent contexts using swimlanes

You can reuse a common use case and adapt it to different contexts without affecting the original reused use case. A common reusable use case may be created from scratch or extracted from an include use case element. The following are descriptions with steps for achieving this, as well as two cases with visual examples demonstrating use case extraction and reusability.

###### Extracting a reusable use case from an include use case

1. Say you have an include use case with common parameters and/or other features (actions, perform actions, successions, succession flows, etc.) that can be reused in other contexts. For ease of extraction, it is best if the include use case's parameters do not subset any subparts of the contextual part at this stage, as all subsetting relationships are moved to the extracted use case, requiring you additional modifications to reinstate the previously specified relations for the include use case.
2. Use the [CONFLUENCE_PAGE title='Extract Definition and Usage' space=''] command on the include use case to extract a use case with the include use case's parameters and features . As a result:
  1. The include use case's parameters and features are moved to the extracted use case. The subject parameter (and any perform actions it may contain) is not moved to the extracted use case; instead, a new empty subject is created for the extracted usage. To ensure reuse:1. Manually[CONFLUENCE_PAGE title='Element ownership change' space='']the subject (and its contained elements) from the include use case to the extracted usage, replacing the newly created empty subject; 
2.Make sure the include use case's subject redefines the extracted use case's subject so that the former inherits the latter's features.
  2. The include use case [CONFLUENCE_PAGE title='Reference subsetting' space=''] the extracted use case. Because the extracted use case is given the same name as the include use case from which it was extracted, the include use case's keyword is changed to *include*and the reference subsetting symbol/keyword may not be displayed. If you want to rename the include use case, you must change the element's keyword to *include use case*and use the reference subsetting symbol/keyword explicitly. For more information on referencing use cases, see the [CONFLUENCE_PAGE title='Include use case' space=''] page.

###### Reusing a use case in different contexts

You can reuse (i.e., include) a common use case (extracted or created manually) in include use cases in as many other contexts as needed:

1. Identify the include use case within the context for which you want to reuse a use case and its parameters/features.
2. [CONFLUENCE_PAGE title='Include use case' space=''] the extracted use case. The referencing include use case element inherits the parameters of the referenced use case.

###### Adapting the reused use case to different contexts

You can now adapt the included use case as needed without affecting the reused use case:

1. 
2. relevant to this context, which creates actors for the referencing include use case element.
3. [CONFLUENCE_PAGE title='Redefinition' space=''] . To easily redefine the inherited parameters via the swimlane headers, right-click the header of the swimlane that represents the parameter you want to redefine. In the shortcut menu, click**Refactor**, then**Redefine**.
  1. [CONFLUENCE_PAGE title='Redefinition' space=''] the actions in these swimlanes via the Textual Editor. If an action is not owned but simply referenced by the perform action that is an inherited feature of the parameter represented by the swimlane, the action is displayed with the ^ prefix. See the example below.
  2. [CONFLUENCE_PAGE title='Managing elements' space=''] action symbols that are unnecessary in this context.
  3. needed in this context. They are owned by the referencing include use case element.

###### Case 1. Light reuse. Reusing a use case with common parameters

In this scenario, the use case parameters are reused in different contexts. Since both include use case elements contain common parameters, you can extract the 'provide value using drones' use case and reuse it by referencing it in each include use case element.

[IMAGE alt='' src='']

###### The use case 'provide value using drone' is extracted from the include use case 'provide goods to customer' via the Extract Usage **Extract All Features** command. As a result, the include use case element's parameters are moved to the extracted use case and the include use case element 'provide goods to customer' reference subsets the extracted use case. The extracted use case is also reused for the include use case element 'find person in distress' via reference subsetting. Therefore, both includes inherit the extracted use case's parameters. The inherited parameters are then adapted to the specific context by redefining them and subsetting the related subparts of the contextual part. Afterward, the use case scenario is modeled in the swimlane grid by creating actions, successions, and succession flows.

###### Case 2. Full reuse. Reusing a use case with common parameters and scenario

In this scenario, the common use case parameters andscenario (e.g., successions and succession flows) is reused in different contexts. Since both include use case elements contain common parameters and actions to be performed during the missions, you can extract them to the 'provide value using drones' use case and reuse it by referencing it in each include use case element.

[IMAGE alt='' src='']

###### The use case 'provide value using drone' is extracted from the include use case 'provide goods to customer' via the Extract Usage **Extract All Features**command. As a result, the include use case element's parameters, actions, perform actions, successions, succession flow, etc. are moved to the extracted use case and the include use case element 'provide goods to customer' reference subsets the extracted use case. The extracted use case is also reused for the include use case element 'find person in distress' via reference subsetting. Therefore, both includes inherit the extracted use case's parameters and other features. The inherited parameters are then adapted to the specific context by redefining them and subsetting the related subparts of the contextual part. Afterward, the use case scenario is modeled in the swimlane grid by displaying the reusable inherited scenario (actions, which are displayed with the ^ prefix and can be redefined if needed, successions, etc.), and extending it by creating any needed additional actions, successions, succession flows, etc, needed in this context.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p><span style="letter-spacing: 0.0px;">A use case scenario can be captured in an include use case symbol with a swimlane grid, where each swimlane represents the subject and actor parameters responsible for performing specific actions, depicting the use case scenario of expected interaction between involved participants.    </span></p><p><span style="color:var(--ds-text,#172b4d);"><span style="color:var(--ds-text,#172b4d);">The swimlane grid symbol allows you to model and organize actions based on the elements that are responsible for performing those actions. For more information on swimlanes, see the <ac:link><ri:page ri:content-title="Swimlane grid" /></ac:link> page.</span></span></p><p><span>Within the context of a part that owns or inherits an include use case, the include use case contains actions that are performed by the subject and actor parameters owned or inherited by the include use case. Thus, the swimlane grid symbol is displayed for the include use case, where each individual swimlane in the swimlane pool represents each subject and actor. You can use swimlanes to model actions and their sequencing based on the performers, i.e., subject and actors that perform each action. The subject and actor names are indicated in the swimlane headers.</span></p><ac:image ac:align="center"><ri:attachment ri:filename="swimlanes_example_include_use_case.png" /></ac:image><h6 style="text-align: center;"><span style="letter-spacing: 0.0px;text-align: left;font-size: 14.0px;font-weight: 400;">The use case </span><em style="letter-spacing: 0.0px;text-align: left;font-size: 14.0px;font-weight: 400;">find person in distress</em><span style="letter-spacing: 0.0px;text-align: left;font-size: 14.0px;font-weight: 400;"> is included directly under the context part </span><em style="letter-spacing: 0.0px;text-align: left;font-size: 14.0px;font-weight: 400;">drone in search and rescue mission </em><span style="letter-spacing: 0.0px;text-align: left;font-size: 14.0px;font-weight: 400;">because it is specific to this context. </span><span style="letter-spacing: 0.0px;text-align: left;font-size: 14.0px;font-weight: 400;">Swimlanes in the include use case represent subject and actor parameters as performers of the actions in their corresponding swimlanes. These parameters are related to the subparts of the contextual part via subsetting.</span></h6></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><h3>Prerequisites</h3><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="b59b5e23-aa6d-43ea-bd71-733c86427282"><ac:rich-text-body><ol><li><span>The include use case whose swimlanes represent the subject and actors is </span><ac:link><ri:page ri:content-title="Displaying elements in symbolic views" /><ac:plain-text-link-body><![CDATA[displayed]]></ac:plain-text-link-body></ac:link><span> in the view.</span></li><li><span>The include use case's subject and actors are already related to the contextual part's subparts via <ac:link><ri:page ri:content-title="Subsetting" /><ac:plain-text-link-body><![CDATA[subsetting]]></ac:plain-text-link-body></ac:link>. See the procedures:</span><ol><li data-uuid="bb259817-f716-40a4-8a11-bd898ecad5d7"><span><ac:link ac:anchor="Relating the include use case's subject and actors to the contextual part's subparts through subsetting via the Textual Editor" /></span></li><li data-uuid="bb259817-f716-40a4-8a11-bd898ecad5d7"><span><ac:link ac:anchor="Relating the include use case's subject and actors to the contextual part's subparts through subsetting via the Drag and Drop handler in a view" /></span></li></ol></li></ol></ac:rich-text-body></ac:structured-macro><h4>Relating the include use case's subject and actors to the contextual part's subparts through subsetting via the Textual Editor</h4><p><span><span>To relate the include use case's subject and actors to the contextual part's subparts through subsetting via the Textual Editor</span></span></p><hr /><ol><li>In the Textual Editor, within the body of the contextual part, <ac:link ac:anchor="Creating use case usage and definition elements via the Textual Editor"><ri:page ri:content-title="Creating use cases" /><ac:plain-text-link-body><![CDATA[declare an include use case]]></ac:plain-text-link-body></ac:link> with the <ac:link ac:anchor="Specifying subjects, actors, and objectives for use cases via Textual Editor"><ri:page ri:content-title="Subjects, actors, and objectives for use cases" /><ac:plain-text-link-body><![CDATA[subject and actor parameters]]></ac:plain-text-link-body></ac:link>.</li><li><ac:link ac:anchor="Subsetting a usage via the Textual Editor"><ri:page ri:content-title="Subsetting" /><ac:plain-text-link-body><![CDATA[Subset]]></ac:plain-text-link-body></ac:link> the contextual part’s subparts by the appropriate parameters of the include use case.<br />You can now proceed to <ac:link ac:anchor="Displaying the swimlane grid and creating additional swimlanes"><ac:plain-text-link-body><![CDATA[display the swimlane grid]]></ac:plain-text-link-body></ac:link> on the include use case symbol.<br /><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="f51f2efa-b47a-45d5-9252-1f165ba7c0d3"><ac:rich-text-body><p><span style="color:var(--ds-text-accent-blue,#0055cc);">part</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">'drone in search and rescue mission'</span><span style="color:var(--ds-text,#000000);"> {<br /></span><span style="color:var(--ds-text,#000000);">      </span><span style="color:var(--ds-text-accent-blue,#0055cc);">part</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">'ground control station'</span><span style="color:var(--ds-text,#000000);">;<br /></span><span style="color:var(--ds-text,#000000);">      </span><span style="color:var(--ds-text-accent-blue,#0055cc);">part</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">'person in distress'</span><span style="color:var(--ds-text,#000000);">;<br /></span><span style="color:var(--ds-text,#000000);">      </span><span style="color:var(--ds-text-accent-blue,#0055cc);">part</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">'search drone'</span><span style="color:var(--ds-text,#000000);">;<br /></span><span style="color:var(--ds-text,#000000);">      </span><span style="color:var(--ds-text-accent-blue,#0055cc);">include</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">use</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">case</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">'find person in distress'</span><span style="color:var(--ds-text,#000000);"> {<br /></span><span style="color:var(--ds-text-accent-blue,#0055cc);"><span style="color:var(--ds-text,#000000);">      </span><span style="color:var(--ds-text,#000000);">      </span>subject</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text,#000000);">:&gt; </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">'search drone'</span><span style="color:var(--ds-text,#000000);">;<br /></span><span style="color:var(--ds-text,#000000);">            </span><span style="color:var(--ds-text-accent-blue,#0055cc);">actor</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text,#000000);">:&gt; </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">'ground control station'</span><span style="color:var(--ds-text,#000000);">;<br /></span><span style="color:var(--ds-text,#000000);">            </span><span style="color:var(--ds-text-accent-blue,#0055cc);">actor</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text,#000000);">:&gt; </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">'person in distress'</span><span style="color:var(--ds-text,#000000);">;<br /></span><span style="color:var(--ds-text,#000000);">      }<br /></span><span style="color:var(--ds-text,#000000);">}</span></p></ac:rich-text-body></ac:structured-macro></li></ol><h4><span>Relating the include use case's subject and actors to the contextual part's subparts through </span>subsetting via the Drag and Drop handler in a view</h4><p><span>To relate the include use case's subject and actors to the contextual part's subparts through subsetting via the Drag and Drop handler in a view</span></p><hr /><ol><li>On the contextual part's symbol displayed in a view, <ac:link ac:anchor="Creating use case usage and definition elements via the view palette"><ri:page ri:content-title="Creating use cases" /><ac:plain-text-link-body><![CDATA[create an include use case]]></ac:plain-text-link-body></ac:link>.</li><li><ac:link ac:anchor="Specifying subjects, actors, and objectives for use cases via the Drag and Drop handler in a view"><ri:page ri:content-title="Subjects, actors, and objectives for use cases" /><ac:plain-text-link-body><![CDATA[Subset]]></ac:plain-text-link-body></ac:link> the contextual part’s subparts by the appropriate parameters of the include use case using the Drag and Drop handler commands <span style="color:var(--ds-text,#172b4d);"><span><strong>Create Subject</strong>, <strong>Create Actor</strong>, or <strong>Set Subsetted Feature</strong></span></span>.</li></ol><h3>Managing swimlanes</h3><h4>Displaying the swimlane grid and creating additional swimlanes</h4><p>To display the swimlane grid or create additional swimlanes</p><hr /><ul><li>To display the swimlane grid:<ul><li>Right-click the include use case symbol and in the shortcut menu, click <strong><ac:link><ri:page ri:content-title="Displaying elements in symbolic views" /><ac:plain-text-link-body><![CDATA[Display]]></ac:plain-text-link-body></ac:link></strong>, then<strong> Display Swimlanes</strong>.<br />The swimlane grid is displayed with swimlanes (along with any actions and connectors that may already be defined in the model), representing subject and actors owned or inherited by the part that owns or inherits the include use case.</li></ul></li></ul></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><ac:structured-macro ac:name="section" ac:schema-version="1" ac:macro-id="9ca8f20e-0fa2-4592-981b-868eeda574e8"><ac:rich-text-body><ac:structured-macro ac:name="column" ac:schema-version="1" ac:macro-id="ee74a7e4-3305-4dda-a8ea-5dcb6fb21b5b"><ac:parameter ac:name="width">50%</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="eadb8db9-9d97-416c-a068-cf38bc4fd134"><ac:rich-text-body><p><span style="color:var(--ds-text-accent-blue,#0055cc);">part</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">'drone in search and rescue mission'</span><span style="color:var(--ds-text,#000000);"> {<br /></span><span style="letter-spacing: 0.0px;color:var(--ds-text,#000000);">      </span><span style="color:var(--ds-text-accent-blue,#0055cc);">part</span><span style="letter-spacing: 0.0px;color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">'ground control station'</span><span style="letter-spacing: 0.0px;color:var(--ds-text,#000000);">;<br /></span><span style="letter-spacing: 0.0px;color:var(--ds-text,#000000);">      </span><span style="color:var(--ds-text-accent-blue,#0055cc);">part</span><span style="letter-spacing: 0.0px;color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">'person in distress'</span><span style="letter-spacing: 0.0px;color:var(--ds-text,#000000);">;<br /></span><span style="letter-spacing: 0.0px;color:var(--ds-text,#000000);">      </span><span style="color:var(--ds-text-accent-blue,#0055cc);">part</span><span style="letter-spacing: 0.0px;color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">'search drone'</span><span style="letter-spacing: 0.0px;color:var(--ds-text,#000000);">;<br /></span><span style="color:var(--ds-text,#000000);">      </span><span style="color:var(--ds-text-accent-blue,#0055cc);">include</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">use</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">case</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">'find person in distress'</span><span style="color:var(--ds-text,#000000);"> {<br /></span><span style="color:var(--ds-text-accent-blue,#0055cc);"><span style="color:var(--ds-text,#000000);">      </span><span style="color:var(--ds-text,#000000);">      </span>subject</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text,#000000);">:&gt; </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">'search drone'</span><span style="color:var(--ds-text,#000000);"><span style="color:var(--ds-text,#000000);">;<br /></span></span><span style="color:var(--ds-text,#000000);">            </span><span style="color:var(--ds-text-accent-blue,#0055cc);">actor</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text,#000000);">:&gt; </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">'ground control station'</span><span style="color:var(--ds-text,#000000);"><span style="color:var(--ds-text,#000000);">;<br /></span></span><span style="color:var(--ds-text,#000000);">            </span><span style="color:var(--ds-text-accent-blue,#0055cc);">actor</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text,#000000);">:&gt; </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">'person in distress'</span><span style="color:var(--ds-text,#000000);"><span style="color:var(--ds-text,#000000);">;<br /></span></span><span style="letter-spacing: 0.0px;color:var(--ds-text,#000000);">      }<br /></span><span style="letter-spacing: 0.0px;color:var(--ds-text,#000000);">}</span></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="column" ac:schema-version="1" ac:macro-id="79d8dce0-8790-4d51-adb7-847ad5eefca5"><ac:parameter ac:name="width">50%</ac:parameter><ac:rich-text-body><p><ac:image ac:align="center"><ri:attachment ri:filename="display_swimlanes_include_use_case.png" /></ac:image></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><ul><li>To create additional swimlanes:<ul><li>Select the header of an existing swimlane and click the <strong>+</strong> button on the left or the right side of the swimlane, to create a swimlane to the left or the right of the existing one.<br />Creating a new swimlane creates an actor for the include use case, represented by the new swimlane. However, no related subpart is created for the part that owns or inherits the include use case.</li></ul></li></ul></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><ac:structured-macro ac:name="section" ac:schema-version="1" ac:macro-id="85ca53ea-c814-4360-bbc5-9ab7907d2083"><ac:rich-text-body><ac:structured-macro ac:name="column" ac:schema-version="1" ac:macro-id="38ea0124-ea9b-471b-b61a-1b94d7975593"><ac:parameter ac:name="width">50%</ac:parameter><ac:rich-text-body><p><ac:image ac:align="center"><ri:attachment ri:filename="display_swimlanes_include_use_case_1.png" /></ac:image></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="fcffad3c-0477-4249-b439-89c0664d79be"><ac:rich-text-body><p><span style="color:var(--ds-text-accent-blue,#0055cc);">part</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">'drone in search and rescue mission'</span><span style="color:var(--ds-text,#000000);"> {<br /></span><span style="color:var(--ds-text,#000000);">      </span><span style="color:var(--ds-text-accent-blue,#0055cc);">part</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">'ground control station'</span><span style="color:var(--ds-text,#000000);">;<br /></span><span style="color:var(--ds-text,#000000);">      </span><span style="color:var(--ds-text-accent-blue,#0055cc);">part</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">'person in distress'</span><span style="color:var(--ds-text,#000000);">;<br /></span><span style="color:var(--ds-text,#000000);">      </span><span style="color:var(--ds-text-accent-blue,#0055cc);">part</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">'search drone'</span><span style="color:var(--ds-text,#000000);">;<br /></span><span style="color:var(--ds-text,#000000);">      </span><span style="color:var(--ds-text-accent-blue,#0055cc);">include</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">use</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">case</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">'find person in distress'</span><span style="color:var(--ds-text,#000000);"> {<br /></span><span style="color:var(--ds-text-accent-blue,#0055cc);"><span style="color:var(--ds-text,#000000);">      </span><span style="color:var(--ds-text,#000000);">      </span>subject</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text,#000000);">:&gt; </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">'search drone'</span><span style="color:var(--ds-text,#000000);">;<br /></span><span style="color:var(--ds-text,#000000);">            </span><span style="color:var(--ds-text-accent-blue,#0055cc);">actor</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text,#000000);">:&gt; </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">'ground control station'</span><span style="color:var(--ds-text,#000000);">;<br /></span><span style="color:var(--ds-text,#000000);">            </span><span style="color:var(--ds-text-accent-blue,#0055cc);">actor</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text,#000000);">:&gt; </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">'person in distress'</span><span style="color:var(--ds-text,#000000);">;<br /></span><span style="color:var(--ds-text,#000000);">      }<br /></span><span style="color:var(--ds-text,#000000);">}</span></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="column" ac:schema-version="1" ac:macro-id="8ee53628-7d5d-40a5-a924-ad3c46bada6d"><ac:parameter ac:name="width">50%</ac:parameter><ac:rich-text-body><p><ac:image ac:align="center"><ri:attachment ri:filename="display_swimlanes_include_use_case_2.png" /></ac:image></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="e5f8c333-af4d-42c8-b4bb-5614a3bfc99f"><ac:rich-text-body><p><span style="color:var(--ds-text-accent-blue,#0055cc);">part</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">'drone in search and rescue mission'</span><span style="color:var(--ds-text,#000000);"> {<br /></span><span style="color:var(--ds-text,#000000);">      </span><span style="color:var(--ds-text-accent-blue,#0055cc);">part</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">'ground control station'</span><span style="color:var(--ds-text,#000000);">;<br /></span><span style="color:var(--ds-text,#000000);">      </span><span style="color:var(--ds-text-accent-blue,#0055cc);">part</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">'person in distress'</span><span style="color:var(--ds-text,#000000);">;<br /></span><span style="color:var(--ds-text,#000000);">      </span><span style="color:var(--ds-text-accent-blue,#0055cc);">part</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">'search drone'</span><span style="color:var(--ds-text,#000000);">;<br /></span><span style="color:var(--ds-text,#000000);">      </span><span style="color:var(--ds-text-accent-blue,#0055cc);">include</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">use</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">case</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">'find person in distress'</span><span style="color:var(--ds-text,#000000);"> {<br /></span><span style="color:var(--ds-text-accent-blue,#0055cc);"><span style="color:var(--ds-text,#000000);">      </span><span style="color:var(--ds-text,#000000);">      </span>subject</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text,#000000);">:&gt; </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">'search drone'</span><span style="color:var(--ds-text,#000000);">;<br /></span><span style="color:var(--ds-text,#000000);">            </span><span style="color:var(--ds-text-accent-blue,#0055cc);">actor</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text,#000000);">:&gt; </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">'ground control station'</span><span style="color:var(--ds-text,#000000);">;<br /></span><span style="color:var(--ds-text,#000000);">            </span><span style="color:var(--ds-text-accent-blue,#0055cc);">actor</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text,#000000);">:&gt; </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">'person in distress'</span><span style="color:var(--ds-text,#000000);">;<br />            <span style="color:var(--ds-text-accent-blue,#0055cc);">actor</span> <span style="color:var(--ds-text-accent-blue-bolder,#09326c);">actor1</span>;     <span style="color:var(--ds-text-accent-green-bolder,#164b35);">// new actor represented by the newly created swimlane</span><br /></span><span style="color:var(--ds-text,#000000);">      }<br /></span><span style="color:var(--ds-text,#000000);">}</span></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="b6e37a9b-b22f-4dc4-b1ba-251f9dd62e20"><ac:rich-text-body><p>If the include use case owns or inherits actors that are not yet displayed as swimlanes, clicking the + button displays a dropdown menu with the following categories:</p><ul><li><strong>Display </strong>that has the following options:<ul><li><em>actor &lt;the name of the actor that does not yet have the corresponding swimlane displayed in the view&gt;</em>. Click to create the corresponding swimlane.</li><li><em>All</em>. Click to create the corresponding swimlanes for all actors that are not represented in the swimlane symbol.</li></ul></li><li><strong>Create </strong>that has the following option:<ul><li><em>actor</em>. Click to create an actor, represented by a new swimlane. </li></ul></li></ul><ac:structured-macro ac:name="section" ac:schema-version="1" ac:macro-id="30d73de6-05d6-43f1-aeba-ee268dee1ddd"><ac:rich-text-body><ac:structured-macro ac:name="column" ac:schema-version="1" ac:macro-id="22152961-2e0a-4145-959f-e027fb338f90"><ac:parameter ac:name="width">50%</ac:parameter><ac:rich-text-body><p><ac:image><ri:attachment ri:filename="create_or_display_swimlanes_include_use_case.png" /></ac:image></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="column" ac:schema-version="1" ac:macro-id="32d6fccb-fb30-48f0-8cae-17cf3b7acbf8"><ac:parameter ac:name="width">50%</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="2f4806e6-66b3-41fa-855b-c826161cd615"><ac:rich-text-body><p><span style="color:var(--ds-text-accent-blue,#0055cc);">part</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">'drone in search and rescue mission'</span><span style="color:var(--ds-text,#000000);"> {<br /></span><span style="color:var(--ds-text,#000000);">      </span><span style="color:var(--ds-text-accent-blue,#0055cc);">part</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">'ground control station'</span><span style="color:var(--ds-text,#000000);">;<br /></span><span style="color:var(--ds-text,#000000);">      </span><span style="color:var(--ds-text-accent-blue,#0055cc);">part</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">'person in distress'</span><span style="color:var(--ds-text,#000000);">;<br /></span><span style="color:var(--ds-text,#000000);">      </span><span style="color:var(--ds-text-accent-blue,#0055cc);">part</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">'search drone'</span><span style="color:var(--ds-text,#000000);">;<br /></span><span style="color:var(--ds-text,#000000);">      </span><span style="color:var(--ds-text-accent-blue,#0055cc);">include</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">use</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">case</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">'find person in distress'</span><span style="color:var(--ds-text,#000000);"> {<br /></span><span style="color:var(--ds-text-accent-blue,#0055cc);"><span style="color:var(--ds-text,#000000);">      </span><span style="color:var(--ds-text,#000000);">      </span>subject</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text,#000000);">:&gt; </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">'search drone'</span><span style="color:var(--ds-text,#000000);">;<br /></span><span style="color:var(--ds-text,#000000);">            </span><span style="color:var(--ds-text-accent-blue,#0055cc);">actor</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text,#000000);">:&gt; </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">'ground control station'</span><span style="color:var(--ds-text,#000000);">;<br /></span><span style="color:var(--ds-text,#000000);">            </span><span style="color:var(--ds-text-accent-blue,#0055cc);">actor</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text,#000000);">:&gt; </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">'person in distress'</span><span style="color:var(--ds-text,#000000);">; <span style="color:var(--ds-text,#000000);">   <span style="color:var(--ds-text-accent-green-bolder,#164b35);">// actor whose representative swimlane is not displayed yet, thus it is available in the Display dropdown menu</span></span><br /></span><span style="color:var(--ds-text,#000000);">      }<br /></span><span style="color:var(--ds-text,#000000);">}</span></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro><h4>Displaying actions in swimlanes</h4><p>To display actions in swimlanes</p><hr /><ul><li>Select one swimlane by right-clicking its header or all swimlanes by right-clicking the swimlane pool. In the shortcut menu, <span>click </span><ac:link><ri:page ri:content-title="Displaying elements in symbolic views" /><ac:link-body><strong>Display</strong></ac:link-body></ac:link><span>, then</span><span> </span><strong>Display Actions </strong>in the dropdown menu<span>. <br /></span><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="3dc1898d-3456-4fd1-8697-4223a6d0f6c7"><ac:rich-text-body><p><span style="color:var(--ds-text,#172b4d);">The specific swimlane's shortcut menu contains the same commands as the</span> part element symbol (subject or actor) it represents<span style="color:var(--ds-text,#172b4d);">. </span><span style="color:var(--ds-text,#172b4d);"><br /></span></p></ac:rich-text-body></ac:structured-macro></li></ul><h4><span>Displaying parameters, connectors, or other features for element symbols in swimlanes</span></h4><p><span>To display parameters, connectors, or other features for element symbols in swimlanes</span></p><hr /><ul><li>Right-click element symbol(s) in the swimlane(s). In the shortcut menu, click <ac:link><ri:page ri:content-title="Displaying elements in symbolic views" /><ac:link-body><strong>Display</strong></ac:link-body></ac:link>, then click the appropriate command in its dropdown menu. </li></ul><h3>Modeling actions with swimlanes</h3><h4>Creating actions in swimlanes</h4><p>You may create actions and the appropriate subject's or actor's perform actions via the Textual Editor and then display the actions in swimlanes via the <ac:link ac:anchor="Displaying actions in swimlanes" /> procedure. However, you can create actions in swimlanes using the view palette. This way, the appropriate perform actions are automatically created for the subject and actors in whose representative swimlanes the actions are created.</p><p>To create actions in swimlanes </p><hr /><ol><li><ac:link ac:anchor="Displaying the swimlane grid and creating additional swimlanes"><ac:plain-text-link-body><![CDATA[Display or create swimlanes for the perform action in a view]]></ac:plain-text-link-body></ac:link>.</li><li>In the view palette, under the Actions group, click the button for the needed action.</li><li>Click on the swimlane representing the subject or actor that you want to perform the action.<br /><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="8538ff03-a6b8-4378-9cb3-b2761aa73c73"><ac:rich-text-body><ul><li><span><span style="color:var(--ds-text,#172b4d);">Indicate the start and end of an action sequence </span>using start and done actions<span style="color:var(--ds-text,#172b4d);">. See the <ac:link><ri:page ri:content-title="Start and done actions" /></ac:link> page.</span></span></li><li><span>Connect and sequence actions using successions, flows, and succession flows. See the <ac:link><ri:page ri:content-title="Action succession and flow" /></ac:link> page.</span></li><li><span>Control the sequencing of actions using control nodes. See the <ac:link><ri:page ri:content-title="Control nodes" /></ac:link> page.</span></li></ul><p><span>Start and done actions, as well as control nodes, are not performed, thus subject/actors in whose representative swimlanes they are displayed, do not have perform actions for performing them. These actions and nodes are owned by the include use case that owns the swimlane grid symbol, while their symbols are owned by the swimlane grid symbol. </span></p></ac:rich-text-body></ac:structured-macro></li></ol></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><ac:structured-macro ac:name="section" ac:schema-version="1" ac:macro-id="c2a4dae6-4687-49e5-b207-2996fd511373"><ac:rich-text-body><ac:structured-macro ac:name="column" ac:schema-version="1" ac:macro-id="46e4059e-ced6-4760-9a66-d8b446344031"><ac:parameter ac:name="width">50%</ac:parameter><ac:rich-text-body><p style="text-align: center;"><ac:image ac:align="center"><ri:attachment ri:filename="create_action_in_swimlane_include_use_case_before.png" /></ac:image></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="9814e6e0-e219-46e9-8a83-9b95acb814e0"><ac:rich-text-body><p><span style="color:var(--ds-text-accent-blue,#0055cc);">part</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">'drone in search and rescue mission'</span><span style="color:var(--ds-text,#000000);"> {<br /></span><span style="color:var(--ds-text,#000000);">      </span><span style="color:var(--ds-text-accent-blue,#0055cc);">part</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">'ground control station'</span><span style="color:var(--ds-text,#000000);">;</span><span style="color:var(--ds-text,#000000);"><br /></span><span style="color:var(--ds-text,#000000);">      </span><span style="color:var(--ds-text-accent-blue,#0055cc);">part</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">'search drone'</span><span style="color:var(--ds-text,#000000);">;<br /></span><span style="color:var(--ds-text,#000000);">      </span><span style="color:var(--ds-text-accent-blue,#0055cc);">include</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">use</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">case</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">'find person in distress'</span><span style="color:var(--ds-text,#000000);"> {<br /></span><span style="color:var(--ds-text-accent-blue,#0055cc);"><span style="color:var(--ds-text,#000000);">      </span><span style="color:var(--ds-text,#000000);">      </span>subject</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text,#000000);">:&gt; </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">'search drone'</span><span style="color:var(--ds-text,#000000);">;<br /></span><span style="color:var(--ds-text,#000000);">            </span><span style="color:var(--ds-text-accent-blue,#0055cc);">actor</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text,#000000);">:&gt; </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">'ground control station'</span><span style="color:var(--ds-text,#000000);">;</span><span style="color:var(--ds-text,#000000);"><br /></span><span style="color:var(--ds-text,#000000);">      }<br /></span><span style="color:var(--ds-text,#000000);">}</span></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="column" ac:schema-version="1" ac:macro-id="3394d1a6-c991-4cb8-bb6d-8535e2695190"><ac:parameter ac:name="width">50%</ac:parameter><ac:rich-text-body><p><ac:image ac:align="center"><ri:attachment ri:filename="create_action_in_swimlane_include_use_case_after.png" /></ac:image></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="9cbb8236-6503-4583-a1a7-c5b35723b86e"><ac:rich-text-body><p><span style="color:var(--ds-text-accent-blue,#0055cc);">part</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">'drone in search and rescue mission'</span><span style="color:var(--ds-text,#000000);"> {</span><br /><span style="color:var(--ds-text-accent-blue,#0055cc);"><span style="color:var(--ds-text,#000000);">    </span>part</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">'ground control station'</span><span style="color:var(--ds-text,#000000);">;</span><br /><span style="color:var(--ds-text,#000000);">    </span><span style="color:var(--ds-text-accent-blue,#0055cc);">part</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">'search drone'</span><span style="color:var(--ds-text,#000000);">;</span><br /><span style="color:var(--ds-text,#000000);">    </span><span style="color:var(--ds-text-accent-blue,#0055cc);">include</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">use</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">case</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">'find person in distress'</span><span style="color:var(--ds-text,#000000);"> {</span><br /><span style="color:var(--ds-text,#000000);">        </span><span style="color:var(--ds-text-accent-blue,#0055cc);">subject</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text,#000000);">:&gt; </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">'search drone'</span><span style="color:var(--ds-text,#000000);"> {</span><br /><span style="color:var(--ds-text,#000000);">            </span><span style="color:var(--ds-text-accent-blue,#0055cc);">perform</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">'fly to destination'</span><span style="color:var(--ds-text,#000000);">;   <span style="color:var(--ds-text-accent-green-bolder,#164b35);">// perform action automatically created for the subject once the</span><span style="color:var(--ds-text-accent-green-bolder,#164b35);"> action 'fly to destination'</span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);"> </span><span style="color:var(--ds-text-accent-green-bolder,#164b35);">was created in the swimlane that represents the subject 'search drone'</span></span><br /><span style="color:var(--ds-text,#000000);">        }</span><br /><span style="color:var(--ds-text,#000000);">        </span><span style="color:var(--ds-text-accent-blue,#0055cc);">actor</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text,#000000);">:&gt; </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">'ground control station'</span><span style="color:var(--ds-text,#000000);"> {</span><br /><span style="color:var(--ds-text,#000000);">            </span><span style="color:var(--ds-text-accent-blue,#0055cc);">perform</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">'start mission'</span><span style="color:var(--ds-text,#000000);">;  <span style="color:var(--ds-text-accent-green-bolder,#164b35);">// perform action automatically created for the part once the action 'start mission' was created in the swimlane that represents the actor 'ground control station'</span></span><br /><span style="color:var(--ds-text,#000000);">        }</span><br /><span style="color:var(--ds-text,#000000);">        </span><span style="color:var(--ds-text-accent-blue,#0055cc);">action</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">'start mission'</span><span style="color:var(--ds-text,#000000);"> { </span><span style="color:var(--ds-text-accent-blue,#0055cc);">out</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">md</span><span style="color:var(--ds-text,#000000);">; }  <span style="color:var(--ds-text-accent-green-bolder,#164b35);">// action created via view</span></span><br /><span style="color:var(--ds-text,#000000);">        </span><span style="color:var(--ds-text-accent-blue,#0055cc);">action</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">'fly to destination'</span><span style="color:var(--ds-text,#000000);"> { </span><span style="color:var(--ds-text-accent-blue,#0055cc);">in</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">md</span><span style="color:var(--ds-text,#000000);">; }  <span style="color:var(--ds-text-accent-green-bolder,#164b35);">// action created via view</span></span><br /><span style="color:var(--ds-text,#000000);">        </span><span style="color:var(--ds-text-accent-blue,#0055cc);">succession</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">flow</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">of</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-teal,#206a83);">'Exchange Items'</span><span style="color:var(--ds-text-accent-teal,#206a83);">::</span><span style="color:var(--ds-text-accent-teal,#206a83);">'Mission Data'</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">from</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">'start mission'</span><span style="color:var(--ds-text,#000000);">.</span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">md</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">to</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">'fly to destination'</span><span style="color:var(--ds-text,#000000);">.</span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">md</span><span style="color:var(--ds-text,#000000);">; <span style="color:var(--ds-text-accent-green-bolder,#164b35);">// succession flow created via view</span></span><br /><span style="color:var(--ds-text,#000000);">    }</span><br /><span style="color:var(--ds-text,#000000);">}</span></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><h4>Deleting actions in swimlanes</h4><p>To delete actions in swimlanes</p><hr /><ul><li>To delete an action element or symbol in swimlane, see the procedure <ac:link ac:anchor="Deleting an element or its symbol via a view"><ri:page ri:content-title="Managing elements" /><ac:plain-text-link-body><![CDATA[Deleting an element or its symbol via a view]]></ac:plain-text-link-body></ac:link> on the <ac:link><ri:page ri:content-title="Managing elements" /></ac:link> page.<br /><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="23004a7d-2f45-46df-a439-5977de4cbf46"><ac:rich-text-body><p>Deleting an action element via swimlane deletes the appropriate perform action from the subject/actor responsible for performing the deleted action. Any associated connectors are deleted as well.</p></ac:rich-text-body></ac:structured-macro></li></ul><h4>Changing which subject or actor is responsible for performing actions via swimlanes</h4><p>You can move actions between swimlanes to change which subject or actor is responsible for performing these actions. The responsible subject/actor is indicated in the header of the swimlane with the keyword <span>«performer»</span>.</p><p>To change which subject or actor is responsible for performing actions via swimlanes </p><hr /><ul><li>Click and drag the action symbol itself from its source swimlane to the target swimlane of the needed include use case.</li></ul><p><br /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><strong style="letter-spacing: 0.0px;">Details regarding the change:</strong></p><ul><li>If the source and target <span style="color:var(--ds-text,#172b4d);">swimlanes are in the same swimlane grid symbol owned by the common include use case, m</span>oving an action from one swimlane to another updates which subject/actor is the owner of the perform action responsible for performing the moved action. </li></ul></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><ac:structured-macro ac:name="section" ac:schema-version="1" ac:macro-id="f9adda5b-b47a-4011-b958-1becb5f79551"><ac:rich-text-body><ac:structured-macro ac:name="column" ac:schema-version="1" ac:macro-id="5f44852c-a068-4055-ac1d-8c7e8d9bc149"><ac:parameter ac:name="width">50%</ac:parameter><ac:rich-text-body><p style="text-align: center;"><ac:image ac:align="center"><ri:attachment ri:filename="move_action_to_another_swimlane_include_use_case_before.png" /></ac:image></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="14c4792e-81c3-4f98-8891-cf63f8c83512"><ac:rich-text-body><p><span style="color:var(--ds-text,#000000);"><span style="color:var(--ds-text-accent-blue,#0055cc);">part</span> <span style="color:var(--ds-text-accent-blue-bolder,#09326c);">'drone in search and rescue mission'</span> {<br /><span style="color:var(--ds-text-accent-blue,#0055cc);"><span style="color:var(--ds-text,#000000);">    </span>part</span> <span style="color:var(--ds-text-accent-blue-bolder,#09326c);">'ground control station'</span>;<br />    <span style="color:var(--ds-text-accent-blue,#0055cc);">part</span> <span style="color:var(--ds-text-accent-blue-bolder,#09326c);">'search drone'</span>;<br />    <span style="color:var(--ds-text-accent-blue,#0055cc);">include</span> <span style="color:var(--ds-text-accent-blue,#0055cc);">use</span> <span style="color:var(--ds-text-accent-blue,#0055cc);">case</span> <span style="color:var(--ds-text-accent-blue-bolder,#09326c);">'find person in distress'</span> {<br />        <span style="color:var(--ds-text-accent-blue,#0055cc);">subject</span> :&gt; <span style="color:var(--ds-text-accent-blue-bolder,#09326c);">'search drone';</span><br />        <span style="color:var(--ds-text-accent-blue,#0055cc);">actor</span> :&gt; <span style="color:var(--ds-text-accent-blue-bolder,#09326c);">'ground control station'</span> {<br />            <span style="color:var(--ds-text-accent-blue,#0055cc);">perform</span> <span style="color:var(--ds-text-accent-blue-bolder,#09326c);">'start mission'</span><span style="color:var(--ds-text,#000000);">;  <span style="color:var(--ds-text-accent-green-bolder,#164b35);">// <span style="color:var(--ds-text-accent-green-bolder,#164b35);">perform action is owned by </span>the actor 'ground control station'</span></span><br />        }<br />        <span style="color:var(--ds-text-accent-blue,#0055cc);">action</span> <span style="color:var(--ds-text-accent-blue-bolder,#09326c);">'start mission';</span><br />    }<br />}</span></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="column" ac:schema-version="1" ac:macro-id="e53cb876-8354-47c1-8d7f-58823de84f96"><ac:parameter ac:name="width">50%</ac:parameter><ac:rich-text-body><p><ac:image ac:align="center"><ri:attachment ri:filename="move_action_to_another_swimlane_include_use_case_after.png" /></ac:image></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="88de83e7-84a3-4d89-9191-69a61dfd3a5f"><ac:rich-text-body><p><span style="color:var(--ds-text,#000000);"><span style="color:var(--ds-text-accent-blue,#0055cc);">part</span> <span style="color:var(--ds-text-accent-blue-bolder,#09326c);">'drone in search and rescue mission'</span> {<br /><span style="color:var(--ds-text-accent-blue,#0055cc);"><span style="color:var(--ds-text,#000000);">    </span>part</span> <span style="color:var(--ds-text-accent-blue-bolder,#09326c);">'ground control station'</span>;<br />    <span style="color:var(--ds-text-accent-blue,#0055cc);">part</span> <span style="color:var(--ds-text-accent-blue-bolder,#09326c);">'search drone'</span>;<br />    <span style="color:var(--ds-text-accent-blue,#0055cc);">include</span> <span style="color:var(--ds-text-accent-blue,#0055cc);">use</span> <span style="color:var(--ds-text-accent-blue,#0055cc);">case</span> <span style="color:var(--ds-text-accent-blue-bolder,#09326c);">'find person in distress'</span> {<br />        <span style="color:var(--ds-text-accent-blue,#0055cc);">subject</span> :&gt; <span style="color:var(--ds-text-accent-blue-bolder,#09326c);">'search drone' <span style="color:var(--ds-text,#000000);"> {<br />            <span style="color:var(--ds-text-accent-blue,#0055cc);">perform</span> <span style="color:var(--ds-text-accent-blue-bolder,#09326c);">'start mission'</span><span style="color:var(--ds-text,#000000);">;  <span style="color:var(--ds-text-accent-green-bolder,#164b35);">// <span style="color:var(--ds-text-accent-green-bolder,#164b35);">perform action is owned by </span>the subject 'search drone'</span></span><br />        }</span></span><br />        <span style="color:var(--ds-text-accent-blue,#0055cc);">actor</span> :&gt; <span style="color:var(--ds-text-accent-blue-bolder,#09326c);">'ground control station';</span><br />        <span style="color:var(--ds-text-accent-blue,#0055cc);">action</span> <span style="color:var(--ds-text-accent-blue-bolder,#09326c);">'start mission';</span><br />    }<br />}</span></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><ul><li>If the source and target <span style="color:var(--ds-text,#172b4d);">swimlanes are in different swimlane grid symbols owned by different include use cases (see example below), m</span>oving an action updates:<ul><li>the moved action's owner to the new include use case;</li><li>which subject/actor is the owner of the perform action responsible for performing the moved action;</li></ul></li><li><span style="letter-spacing: 0.0px;">The same applies if<span style="color:var(--ds-text,#172b4d);"> the moved action is not inherited or owned by the include use case that owns the target swimlane. </span><br /></span></li></ul></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><ac:structured-macro ac:name="section" ac:schema-version="1" ac:macro-id="45af3bb8-3630-4d6a-8b67-1b303fe4d07b"><ac:rich-text-body><ac:structured-macro ac:name="column" ac:schema-version="1" ac:macro-id="1851b683-1c02-4010-95a3-60edb6797a94"><ac:parameter ac:name="width">50%</ac:parameter><ac:rich-text-body><p style="text-align: center;"><ac:image ac:align="center"><ri:attachment ri:filename="move_action_to_different_swimlane_symbol_include_use_case_before.png" /></ac:image></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="1eae025a-02e8-424d-aefe-dfcb557d00fb"><ac:rich-text-body><p><span style="color:var(--ds-text-accent-blue,#0055cc);">part</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">'drone mission'</span><span style="color:var(--ds-text,#000000);"> {</span><br /><span style="color:var(--ds-text,#000000);">    </span><span style="color:var(--ds-text-accent-blue,#0055cc);">part</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">'drone in any mission'</span><span style="color:var(--ds-text,#000000);"> {</span><br /><span style="color:var(--ds-text,#000000);">        </span><span style="color:var(--ds-text-accent-blue,#0055cc);">part</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">'ground control station'</span><span style="color:var(--ds-text,#000000);">;</span><br /><span style="color:var(--ds-text,#000000);">        </span><span style="color:var(--ds-text-accent-blue,#0055cc);">part</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">'search drone'</span><span style="color:var(--ds-text,#000000);">;</span><br /><span style="color:var(--ds-text,#000000);">        </span><span style="color:var(--ds-text-accent-blue,#0055cc);">include</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">use</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">case</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">'locate target'</span><span style="color:var(--ds-text,#000000);"> {</span><br /><span style="color:var(--ds-text,#000000);">            </span><span style="color:var(--ds-text-accent-blue,#0055cc);">subject</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text,#000000);">:&gt; </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">'search drone'</span><span style="color:var(--ds-text,#000000);">;</span><br /><span style="color:var(--ds-text,#000000);">            </span><span style="color:var(--ds-text-accent-blue,#0055cc);">actor</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text,#000000);">:&gt; </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">'ground control station'</span><span style="color:var(--ds-text,#000000);"> {</span><br /><span style="color:var(--ds-text,#000000);">                </span><span style="color:var(--ds-text-accent-blue,#0055cc);">perform</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">'start mission'</span><span style="color:var(--ds-text,#000000);">; </span><span style="color:var(--ds-text-accent-green-bolder,#164b35);">// the actor 'ground control station' is the owner of the perform action responsible for performing the action 'start mission'</span><br /><span style="color:var(--ds-text,#000000);">            }</span><br /><span style="color:var(--ds-text,#000000);">            </span><span style="color:var(--ds-text-accent-blue,#0055cc);">action</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">'start mission'</span><span style="color:var(--ds-text,#000000);">; </span><span style="color:var(--ds-text-accent-green-bolder,#164b35);">// the owner of the action 'start mission' is the include use case 'locate target'</span><br /><span style="color:var(--ds-text,#000000);">        }</span><br /><span style="color:var(--ds-text,#000000);">    }</span><br /><span style="color:var(--ds-text,#000000);">    </span><span style="color:var(--ds-text-accent-blue,#0055cc);">part</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">'drone in search and rescue mission'</span><span style="color:var(--ds-text,#000000);"> {</span><br /><span style="color:var(--ds-text,#000000);">        </span><span style="color:var(--ds-text-accent-blue,#0055cc);">part</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">'ground control station'</span><span style="color:var(--ds-text,#000000);">;</span><br /><span style="color:var(--ds-text,#000000);">        </span><span style="color:var(--ds-text-accent-blue,#0055cc);">part</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">'search drone'</span><span style="color:var(--ds-text,#000000);">;</span><br /><span style="color:var(--ds-text,#000000);">        </span><span style="color:var(--ds-text-accent-blue,#0055cc);">include</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">use</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">case</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">'find person in distress'</span><span style="color:var(--ds-text,#000000);"> {</span><br /><span style="color:var(--ds-text,#000000);">            </span><span style="color:var(--ds-text-accent-blue,#0055cc);">subject</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text,#000000);">:&gt; </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">'search drone'</span><span style="color:var(--ds-text,#000000);">;</span><br /><span style="color:var(--ds-text,#000000);">            </span><span style="color:var(--ds-text-accent-blue,#0055cc);">actor</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text,#000000);">:&gt; </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">'ground control station'</span><span style="color:var(--ds-text,#000000);">;</span><br /><span style="color:var(--ds-text,#000000);">        }</span><br /><span style="color:var(--ds-text,#000000);">    }</span><br /><span style="color:var(--ds-text,#000000);">}</span></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="column" ac:schema-version="1" ac:macro-id="7e76023b-9e08-4c52-8f90-db3da40a0833"><ac:parameter ac:name="width">50%</ac:parameter><ac:rich-text-body><p style="text-align: center;"><ac:image ac:align="center"><ri:attachment ri:filename="move_action_to_different_swimlane_symbol_include_use_case_after.png" /></ac:image></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="8fefd25d-d556-4a7d-80f6-154339de961b"><ac:rich-text-body><p><span style="color:var(--ds-text-accent-blue,#0055cc);">part</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">'drone mission'</span><span style="color:var(--ds-text,#000000);"> {</span><br /><span style="color:var(--ds-text,#000000);">    </span><span style="color:var(--ds-text-accent-blue,#0055cc);">part</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">'drone in any mission'</span><span style="color:var(--ds-text,#000000);"> {</span><br /><span style="color:var(--ds-text,#000000);">        </span><span style="color:var(--ds-text-accent-blue,#0055cc);">part</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">'ground control station'</span><span style="color:var(--ds-text,#000000);">;</span><br /><span style="color:var(--ds-text,#000000);">        </span><span style="color:var(--ds-text-accent-blue,#0055cc);">part</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">'search drone'</span><span style="color:var(--ds-text,#000000);">;</span><br /><span style="color:var(--ds-text,#000000);">        </span><span style="color:var(--ds-text-accent-blue,#0055cc);">include</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">use</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">case</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">'locate target'</span><span style="color:var(--ds-text,#000000);"> {</span><br /><span style="color:var(--ds-text,#000000);">            </span><span style="color:var(--ds-text-accent-blue,#0055cc);">subject</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text,#000000);">:&gt; </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">'search drone'</span><span style="color:var(--ds-text,#000000);">;</span><br /><span style="color:var(--ds-text,#000000);">            </span><span style="color:var(--ds-text-accent-blue,#0055cc);">actor</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text,#000000);">:&gt; </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">'ground control station'</span><span style="color:var(--ds-text,#000000);">; </span><span style="color:var(--ds-text-accent-green-bolder,#164b35);">// the previously owned action 'start mission' and the perform action for performing it is moved out</span><br /><span style="color:var(--ds-text,#000000);">        }</span><br /><span style="color:var(--ds-text,#000000);">    }</span><br /><span style="color:var(--ds-text,#000000);">    </span><span style="color:var(--ds-text-accent-blue,#0055cc);">part</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">'drone in search and rescue mission'</span><span style="color:var(--ds-text,#000000);"> {</span><br /><span style="color:var(--ds-text,#000000);">        </span><span style="color:var(--ds-text-accent-blue,#0055cc);">part</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">'ground control station'</span><span style="color:var(--ds-text,#000000);">;</span><br /><span style="color:var(--ds-text,#000000);">        </span><span style="color:var(--ds-text-accent-blue,#0055cc);">part</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">'search drone'</span><span style="color:var(--ds-text,#000000);">;</span><br /><span style="color:var(--ds-text,#000000);">        </span><span style="color:var(--ds-text-accent-blue,#0055cc);">include</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">use</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">case</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">'find person in distress'</span><span style="color:var(--ds-text,#000000);"> {</span><br /><span style="color:var(--ds-text,#000000);">            </span><span style="color:var(--ds-text-accent-blue,#0055cc);">subject</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text,#000000);">:&gt; </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">'search drone'</span><span style="color:var(--ds-text,#000000);">;</span><br /><span style="color:var(--ds-text,#000000);">            </span><span style="color:var(--ds-text-accent-blue,#0055cc);">actor</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text,#000000);">:&gt; </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">'ground control station'</span><span style="color:var(--ds-text,#000000);"> { </span><br /><span style="color:var(--ds-text,#000000);">                </span><span style="color:var(--ds-text-accent-blue,#0055cc);">perform</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">'start mission'</span><span style="color:var(--ds-text,#000000);">; </span><span style="color:var(--ds-text-accent-green-bolder,#164b35);">// the actor 'ground control station' is updated as the owner of the perform action responsible for performing the action 'start mission'</span><br /><span style="color:var(--ds-text,#000000);">            }</span><br /><span style="color:var(--ds-text,#000000);">            </span><span style="color:var(--ds-text-accent-blue,#0055cc);">action</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">'start mission'</span><span style="color:var(--ds-text,#000000);">; </span><span style="color:var(--ds-text-accent-green-bolder,#164b35);">// the owner of the action 'start mission' is updated to the include use case 'find person in distress'</span><br /><span style="color:var(--ds-text,#000000);">        }</span><br /><span style="color:var(--ds-text,#000000);">    }</span><br /><span style="color:var(--ds-text,#000000);">}</span></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><h4>Deleting subject or actor responsible for performing actions via swimlanes </h4><p>To delete subject or actor responsible for performing actions via swimlanes </p><hr /><ol><li>Select the header of the swimlane representing the subject or actor you want to delete. </li><li>Follow the procedure <ac:link ac:anchor="Deleting an element or its symbol via a view"><ri:page ri:content-title="Managing elements" /><ac:plain-text-link-body><![CDATA[Deleting an element or its symbol via a view]]></ac:plain-text-link-body></ac:link><span style="letter-spacing: 0.0px;"> on the </span><ac:link><ri:page ri:content-title="Managing elements" /></ac:link><span style="letter-spacing: 0.0px;"> page.</span></li></ol><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="5fb24ce6-d020-4b1f-b5c6-0516b68bd973"><ac:rich-text-body><p>Deleting subject or actor responsible for performing actions via swimlanes also deletes perform actions contained by the deleted subject/actor. </p></ac:rich-text-body></ac:structured-macro></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><h3><span style="letter-spacing: -0.003em;">Extracting and/or reusing a common use case </span><span>and adapting its actions to </span><span style="letter-spacing: -0.003em;">different contexts using swimlanes </span></h3><p align="justify">You can reuse a common use case and adapt it to different contexts without affecting the original reused use case. A common reusable use case may be created from scratch or extracted from an include use case element. <span style="text-align: left;letter-spacing: 0.0px;">The following are descriptions with steps for achieving this, as well as two cases with visual examples demonstrating use case extraction and reusability. </span></p><h4><span style="letter-spacing: 0.0px;text-align: left;">Extracting a reusable use case from an include use case </span></h4><ol><li><span style="text-align: left;letter-spacing: 0.0px;">Say you have an include use case with common parameters and/or other features (<span>actions, perform actions, successions, succession flows, etc.</span>) that can be reused in other contexts. </span><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="c5ee18e5-e7ba-4e1e-ada5-7e922bb3800a"><ac:rich-text-body><p><span>For ease of extraction, it is best if the include use case's parameters do not subset any subparts of the contextual part at this stage, as all subsetting relationships are moved to the extracted use case, requiring you additional modifications to reinstate the previously specified relations for the include use case.</span></p></ac:rich-text-body></ac:structured-macro></li><li><span style="text-align: left;letter-spacing: 0.0px;">Use the <ac:link><ri:page ri:content-title="Extract Definition and Usage" /><ac:plain-text-link-body><![CDATA[Extract Usage Extract All Features]]></ac:plain-text-link-body></ac:link> command on the include use case to extract a use case </span>with the include use case's parameters and features<span style="text-align: left;letter-spacing: 0.0px;">. As a result: </span><ol><li><span>The include use case's parameters and features are moved to the <span>extracted use case. </span></span><br /><ac:structured-macro ac:name="warning" ac:schema-version="1" ac:macro-id="f8ef9557-45d1-4023-9a32-42a4aa011296"><ac:rich-text-body><p>The subject parameter (and any perform actions it may contain) is not moved to the extracted use case; instead, a new empty subject is created for the extracted usage. To ensure reuse:</p><p style="margin-left: 40.0px;"><span style="letter-spacing: 0.0px;">1. Manually </span><ac:link><ri:page ri:content-title="Element ownership change" /><ac:plain-text-link-body><![CDATA[move]]></ac:plain-text-link-body></ac:link><span style="letter-spacing: 0.0px;"> the subject (and its contained elements) from the include use case to the extracted usage, replacing the newly created empty subject;<br />2. </span><span style="letter-spacing: 0.0px;">Make sure the include use case's subject redefines the extracted use case's subject so that the former inherits the latter's features.</span></p></ac:rich-text-body></ac:structured-macro></li><li><span style="letter-spacing: 0.0px;">The include use case </span><span style="letter-spacing: 0.0px;"><ac:link><ri:page ri:content-title="Reference subsetting" /><ac:plain-text-link-body><![CDATA[reference subsets]]></ac:plain-text-link-body></ac:link></span><span style="letter-spacing: 0.0px;"> the extracted use case.<br /></span><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="da254a56-52a7-4a4f-8811-207f8d6b41f0"><ac:rich-text-body><p>Because the extracted use case is given the same name as the include use case from which it was extracted, the include use case's keyword is changed to <em>include </em>and the reference subsetting symbol/keyword may not be displayed. If you want to rename the include use case, you must change the element's keyword to <em>include use case </em>and use the reference subsetting symbol/keyword explicitly. For more information on referencing use cases, see the <ac:link><ri:page ri:content-title="Include use case" /></ac:link> page. </p></ac:rich-text-body></ac:structured-macro></li></ol></li></ol><h4><span style="letter-spacing: 0.0px;">Reusing a use case in different contexts </span></h4><p><span style="letter-spacing: 0.0px;">You can reuse (i.e., include) a common use case (extracted or created <span>manually</span>) in <span>include use cases in as many other contexts as needed</span>:</span></p><ol><li><span style="text-align: left;letter-spacing: 0.0px;">Identify the include use case within the context for which you want to reuse a use case and its parameters/features.</span></li><li><span style="text-align: left;letter-spacing: 0.0px;"><ac:link ac:anchor="Including a use case by referencing included use case usage defined elsewhere in the model"><ri:page ri:content-title="Include use case" /><ac:plain-text-link-body><![CDATA[Reference subset]]></ac:plain-text-link-body></ac:link> the extracted use case. The referencing include use case element inherits the parameters of the referenced use case. </span></li></ol><h4><span style="text-align: left;letter-spacing: 0.0px;">Adapting the reused use case to different contexts</span></h4><p><span style="text-align: left;letter-spacing: 0.0px;">You can now adapt the included use case as needed without affecting the reused use case: </span></p><ol><li><ac:link ac:anchor="Displaying the swimlane grid and creating additional swimlanes"><ac:plain-text-link-body><![CDATA[Display the swimlane grid. ]]></ac:plain-text-link-body></ac:link></li><li><ac:link ac:anchor="Displaying the swimlane grid and creating additional swimlanes"><ac:plain-text-link-body><![CDATA[Create new swimlanes]]></ac:plain-text-link-body></ac:link> relevant to this context, which creates actors for the referencing include use case element. </li><li><ac:link ac:anchor="Redefining a usage via the symbol shortcut menu in a view"><ri:page ri:content-title="Redefinition" /><ac:plain-text-link-body><![CDATA[Redefine the inherited parameters]]></ac:plain-text-link-body></ac:link>.<br /><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="e609f944-5b3f-41fa-9617-1bdce90298c8"><ac:rich-text-body><p>To easily redefine the inherited parameters via the swimlane headers, <span>right-click the header of the swimlane that represents the parameter you want to redefine. In the shortcut menu, click </span><strong>Refactor</strong><span>, then </span><strong>Redefine</strong><span>.</span></p></ac:rich-text-body></ac:structured-macro><ol><li><ac:link ac:anchor="Redefining a usage via the Textual Editor"><ri:page ri:content-title="Redefinition" /><ac:plain-text-link-body><![CDATA[Redefine]]></ac:plain-text-link-body></ac:link> the actions in these swimlanes via the Textual Editor. <br /><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="0799d009-b499-4153-8f0d-7b183f0f57da"><ac:rich-text-body><p><span style="color:var(--ds-text,#172b4d);">If an action is not owned but simply referenced by the perform action that is an inherited feature of the parameter represented by the swimlane, the action is displayed with the ^ prefix. See the <ac:link ac:anchor="Case 2. Full reuse. Reusing a use case with common parameters and scenario "><ac:plain-text-link-body><![CDATA[Case 2]]></ac:plain-text-link-body></ac:link> example below.<br /></span></p></ac:rich-text-body></ac:structured-macro></li><li><ac:link ac:anchor="Deleting an element or its symbol via a view"><ri:page ri:content-title="Managing elements" /><ac:plain-text-link-body><![CDATA[Remove from the view]]></ac:plain-text-link-body></ac:link> action symbols that are unnecessary in this context.</li><li><ac:link ac:anchor="Creating actions in swimlanes"><ac:plain-text-link-body><![CDATA[Create actions]]></ac:plain-text-link-body></ac:link> needed in this context. They are owned by the referencing include use case element.</li></ol></li></ol><h4><span>Case 1. Light reuse. Reusing a use case with common parameters</span></h4><p align="justify"><span>In this scenario, the use case parameters are reused in different contexts. Since both include use case elements contain common parameters, you can extract the 'provide value using drones' use case and reuse it by referencing it in each include use case element.</span></p><p style="text-align: center;" align="justify"><ac:image><ri:attachment ri:filename="case_1_light_reuse.png" /></ac:image></p><h6 style="text-align: center;">The use case 'provide value using drone' is extracted from the include use case 'provide goods to customer' via the Extract Usage <strong>Extract All Features</strong> command. As a result, the include use case element's parameters are moved to the extracted use case and the include use case element 'provide goods to customer' reference subsets the extracted use case. The extracted use case is also reused for the include use case element 'find person in distress' via reference subsetting. Therefore, both includes inherit the extracted use case's parameters. The inherited parameters are then adapted to the specific context by redefining them and subsetting the related subparts of the contextual part. Afterward, the use case scenario is modeled in the swimlane grid by creating actions, successions, and succession flows. </h6><h4>Case 2. Full reuse. Reusing a use case with common parameters and scenario<span style="text-align: left;letter-spacing: 0.0px;"> </span></h4><p align="justify"><span style="text-align: left;letter-spacing: 0.0px;">In this scenario, the common use case <span>parameters and </span>scenario (e.g., successions and succession <span>flows</span>) is reused in different contexts. Since both include use case elements contain common parameters and actions to be performed during the missions, you can extract them to the 'provide value using drones' use case and reuse it by referencing it in each include use case element.</span></p><p style="text-align: center;" align="justify"><ac:image><ri:attachment ri:filename="case_2_full_reuse.png" /></ac:image></p><h6 style="text-align: center;">The use case 'provide value using drone' is extracted from the include use case 'provide goods to customer' via the Extract Usage <strong>Extract All Features </strong>command. As a result, the include use case element's parameters, actions, perform actions, successions, succession flow, etc. are moved to the extracted use case and the include use case element 'provide goods to customer' reference subsets the extracted use case. The extracted use case is also reused for the include use case element 'find person in distress' via reference subsetting. Therefore, both includes inherit the extracted use case's parameters and other features. The inherited parameters are then adapted to the specific context by redefining them and subsetting the related subparts of the contextual part. Afterward, the use case scenario is modeled in the swimlane grid by displaying the reusable inherited scenario (actions, which are displayed with the ^ prefix and can be redefined if needed, successions, etc.), and extending it by creating any needed additional actions, successions, succession flows, etc, needed in this context. </h6></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=249577481 space=SYSML2P version=2 -->
## PAGE 00737: Use cases

- page_id: `249577481`
- space_key: `SYSML2P`
- source_url: https://docs.nomagic.com/spaces/SYSML2P/pages/249577481/Use+cases
- version_number: 2
- version_date: `2025-09-19T15:34:58.385+02:00`
- ancestors: SysML v2 Plugin Documentation > Model composition > Behavior
- labels: []

### NORMALIZED CONTENT

This section provides procedures for modeling use cases.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><span style="color:var(--ds-text,#333333);">This section provides procedures for modeling use cases. </span></p>
````

<!--NOMAGIC_PAGE id=249576732 space=SYSML2P version=4 -->
## PAGE 00738: User interface

- page_id: `249576732`
- space_key: `SYSML2P`
- source_url: https://docs.nomagic.com/spaces/SYSML2P/pages/249576732/User+interface
- version_number: 4
- version_date: `2025-12-03T08:27:51.904+01:00`
- ancestors: SysML v2 Plugin Documentation > Project management > Modeling tool environment
- labels: []

### NORMALIZED CONTENT

Explore the following content to familiarize yourself with the user interface. The modeling tool contains the following UI items:

- [CONFLUENCE_PAGE title='Main menu' space='']
- [CONFLUENCE_PAGE title='Toolbars' space='']
- [CONFLUENCE_PAGE title='Working with Containment tree' space='']
- [CONFLUENCE_PAGE title='Quick Properties Panel' space='']
- [CONFLUENCE_PAGE title='Editor Tabs' space='']
- [CONFLUENCE_PAGE title='Editor Tabs' space='']
- [CONFLUENCE_PAGE title='Specification panel' space='']
- [CONFLUENCE_PAGE title='Status Line' space='']

[IMAGE alt='' src='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>Explore the following content to familiarize yourself with the user interface. The modeling tool contains the following UI items:</p><ul><li><ac:link><ri:page ri:content-title="Main menu" /></ac:link></li><li><ac:link><ri:page ri:content-title="Toolbars" /></ac:link></li><li><ac:link><ri:page ri:content-title="Working with Containment tree" /><ac:plain-text-link-body><![CDATA[Containment tab]]></ac:plain-text-link-body></ac:link></li><li data-uuid="0732d9e7-b6a2-44b7-88e2-53b4e88e3e3c"><ac:link><ri:page ri:content-title="Quick Properties Panel" /></ac:link></li><li><ac:link><ri:page ri:content-title="Editor Tabs" /><ac:plain-text-link-body><![CDATA[View Editor tab]]></ac:plain-text-link-body></ac:link> </li><li><ac:link><ri:page ri:content-title="Editor Tabs" /><ac:plain-text-link-body><![CDATA[Textual Editor tab]]></ac:plain-text-link-body></ac:link></li><li><ac:link><ri:page ri:content-title="Specification panel" /><ac:plain-text-link-body><![CDATA[Specification tab]]></ac:plain-text-link-body></ac:link></li><li><ac:link><ri:page ri:content-title="Status Line" /></ac:link><br /><br /></li></ul><p><ac:image ac:align="center"><ri:attachment ri:filename="SysMLv2_ui.png" /></ac:image></p>
````

<!--NOMAGIC_PAGE id=249576825 space=SYSML2P version=2 -->
## PAGE 00739: Using Model Patch

- page_id: `249576825`
- space_key: `SYSML2P`
- source_url: https://docs.nomagic.com/spaces/SYSML2P/pages/249576825/Using+Model+Patch
- version_number: 2
- version_date: `2025-09-19T15:13:17.866+02:00`
- ancestors: SysML v2 Plugin Documentation > Project management > Working with projects > Tools > Model Patch
- labels: []

### NORMALIZED CONTENT

#### NOTE: Before creating a patch

Before creating a patch

Since model elements are usually related to and depend on other elements, you must include the necessary elements in the patch scope. The Model Patch mechanism does not automatically check dependencies or include them in the patch data.

To avoid data loss, do one of the following:

- Check if all the elements that the elements in a patch depend on are also included in the patch.
- Make sure that the target model already has the dependencies of the elements included in the patch.

##### Creating a model patch

To create a model patch

1. Open the source project.
2. In the Containment tree, right-click the element you want to include in the patch and select Tools > Create Patch . The element from which you initiate the **Create Patch** command is set as the patch scope. All the elements under the patch scope element are automatically included in the patch.
3. In the **Create a Patch** dialog, select the type of patch you want to create:
  - All selected content - This type of patch brings all the selected scope to the target project potentially overriding existing elements.
  - Changes from specific version. This type of patch adds the selected scope to the target project as concurrent changes. If you select this patch type, also select a project version. All changes from the selected version, subsequent versions, and the current project version will be included in the patch. This patch type is only available for Teamwork Cloud projects. [ATTACHMENT filename='patch_types.png']
4. Click Next.
5. Click [ATTACHMENT filename='three_dots_button.png'] and select the location where you want to save the patch file.
6. Click Save.

##### Applying model patch

To apply a model patch

1. Open the target project.
2. In the main menu, select Tools > Patch > Apply Patch .
3. Select the patch file and click Open.
4. In the Apply Patch window, review the changes that will be applied to the project. [ATTACHMENT filename='apply_patch.png']
5. Click the Apply Patch button.
6. Investigate the results:
  - If you receive a massage that the patch is applied successfully, it means all changes from the patch were successfully applied.
  - If you receive a warning that the patch has been applied, but some changes could not be applied, click **OK** and review the changes that were not applied in the open **Changes That Are Not Applied** pane. In the **Changes That Are Not Applied** pane, select each change and read the description explaining the reason of the issue. To avoid such issues, remember tobefore creating a model patch. [ATTACHMENT filename='not_applied_changes.png']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="eebc9eee-fecc-4c21-be1e-e04dc0acf870"><ac:parameter ac:name="title">Before creating a patch</ac:parameter><ac:rich-text-body><p><span style="letter-spacing: 0.0px;color:var(--ds-text,#000000);">Since model elements are usually related to and depend on other elements, you must include the necessary elements in the patch scope. The Model Patch mechanism does not automatically check dependencies or include them in the patch data.</span></p><p><span style="color:var(--ds-text,#000000);">To avoid data loss, do one of the following:</span></p><ul><li><span style="letter-spacing: 0.0px;color:var(--ds-text,#000000);">Check if all the elements that the elements in a patch depend on are also included in the patch.</span></li><li><span style="letter-spacing: 0.0px;color:var(--ds-text,#000000);">Make sure </span><span style="letter-spacing: 0.0px;color:var(--ds-text,#000000);">that the target model already has the dependencies of the elements included in the patch.</span></li></ul></ac:rich-text-body></ac:structured-macro><h3>Creating a model patch</h3><p>To create a model patch</p><hr /><ol><li>Open the source project.</li><li>In the Containment tree, right-click the element you want to include in the patch and select <strong style="letter-spacing: 0.0px;">Tools &gt; Create Patch</strong>.<br /><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="26c1300c-1cb4-4b69-8a8f-3d98d5d52607"><ac:rich-text-body>The element from which you initiate the <strong>Create Patch</strong> command is set as the patch scope. All the elements under the patch scope element are automatically included in the patch.</ac:rich-text-body></ac:structured-macro></li><li><span style="letter-spacing: 0.0px;">In the <strong>Create a Patch</strong> dialog, select the type of patch you want to create:</span><ul><li><strong style="letter-spacing: 0.0px;">All selected content</strong><span style="letter-spacing: 0.0px;"> - This type of patch brings all the selected scope to the target project potentially overriding existing elements. </span></li><li><strong>Changes from specific version.</strong> This type of patch adds the selected scope to the target project as concurrent changes. If you select this patch type, also select a project version. All changes from the selected version, subsequent versions, and the current project version will be included in the patch.<br /><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="bb75f378-42e7-45bb-940c-f58495270cf7"><ac:rich-text-body>This patch type is only available for Teamwork Cloud projects.</ac:rich-text-body></ac:structured-macro><br /><ac:image><ri:attachment ri:filename="patch_types.png" /></ac:image><br /><br /></li></ul></li><li>Click <strong>Next.</strong></li><li>Click <ac:image ac:thumbnail="true" ac:height="18"><ri:attachment ri:filename="three_dots_button.png" /></ac:image> and select the location where you want to save the patch file.</li><li>Click <strong>Save.</strong></li></ol><h3>Applying model patch</h3><p><br /></p><p>To apply a model patch</p><hr /><ol><li>Open the target project.</li><li>In the main menu, select <strong>Tools &gt; Patch &gt; Apply Patch</strong>.</li><li>Select the patch file and click <strong>Open.</strong></li><li>In the <strong>Apply Patch</strong> window, review the changes that will be applied to the project.<br /><br /><ac:image><ri:attachment ri:filename="apply_patch.png" /></ac:image><br /><br /></li><li>Click the <strong>Apply Patch</strong> button.</li><li>Investigate the results:<ul><li><p>If you receive a massage that the patch is applied successfully, it means all changes from the patch were successfully applied.</p></li><li><p>If you receive a warning that the patch has been applied, but some changes could not be applied, click <strong>OK</strong> and review the changes that were not applied in the open <span><strong>Changes That Are Not Applied</strong> pane</span>.</p><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="e6144784-c49b-43c1-8ae4-d7fef3cf21b4"><ac:rich-text-body><span>In the <strong>Changes That Are Not Applied</strong> pane, select each change and read the description explaining the reason of the issue. To avoid such issues, remember to </span><ac:link ac:anchor="Note"><ac:plain-text-link-body><![CDATA[check element dependencies ]]></ac:plain-text-link-body></ac:link><span>before creating a model patch.</span></ac:rich-text-body></ac:structured-macro><br /><ac:image><ri:attachment ri:filename="not_applied_changes.png" /></ac:image></li></ul></li></ol>
````

<!--NOMAGIC_PAGE id=306282499 space=SYSML2P version=3 -->
## PAGE 00740: Using projects from the local repository

- page_id: `306282499`
- space_key: `SYSML2P`
- source_url: https://docs.nomagic.com/spaces/SYSML2P/pages/306282499/Using+projects+from+the+local+repository
- version_number: 3
- version_date: `2026-05-08T13:16:08.852+02:00`
- ancestors: SysML v2 Plugin Documentation > Project management > Working with projects > Managing local used projects
- labels: []

### NORMALIZED CONTENT

Used projects employ the sticky versions approach. Once a specific version of a project is used, the main project continues to use that exact version until you update it manually. This means that even if you modify a used project and save it as a new version, the main project will still use the previously added version. This prevents unexpected changes or damage to the main project.

A project must be stored in the [CONFLUENCE_PAGE title='Managing local projects' space=''] before it can be used locally.

**[IMAGE alt='' src='']**

###### The main project uses only the specified versions of the used projects, despite the newer versions they may have.

###### Using a project from the local repository via the Use Local Project command

To use a project from the local repository via the Use Local Project command

1. In the main menu, select File > Use Project > Use Local Project . The Use Project dialog opens. If there are no other projects in the local repository or all of them are already used in the open project, the **Use Local Project**command is disabled.
2. In the Use Project dialog, select the project you want to use and click the Next button.
3. Select the project version you want to use and click the Finish button. Used projects are displayed under the Used Projects node in the Containment tree of your model. [ATTACHMENT filename='Used Projects node in the Containment tree.png']

###### Using a project from the local repository via the Project Usages dialog

To use a project from the local repository via the Project Usages dialog

1. [CONFLUENCE_PAGE title='Managing local used projects' space='']Open the **Project Usages** dialog .
2. In the Project Usages dialog's toolbar, click the Use Project [IMAGE alt='' src=''] button. The Use Project dialog opens.
3. In the Use Project dialog, select the project you want to use and click the OK button. [ATTACHMENT filename='Using a project from the local repository via the Project Usages dialog.png']
4. Click the OK button to close the Project Usages dialog. Used projects are displayed under the Used Projects node in the Containment tree of your model.

###### Using a project from the local repository via the Advanced Project Usages Configuration dialog

To use a project from the local repository via the Advanced Project Usages Configuration dialog

1. [CONFLUENCE_PAGE title='Managing local used projects' space='']Open the **Advanced Project Usages Configuration**dialog .
2. In the Advanced Project Usages Configuration dialog's toolbar, click the **Add** [IMAGE alt='' src=''] button , and in its dropdown menu, click Use Project . The Use Project dialog opens.
3. In the Use Project dialog, select the project you want to use and click the OK button. The cell in the Action column for the added used project states ' Add '. [ATTACHMENT filename='Using a project from the local repository via the Advanced Usages Configuration dialog.png']
4. (Optional) To undo the action, do one of the following:
  1. In the dialog's toolbar, click the Reset Changes for Selection [ATTACHMENT filename='reset_changes_for_selection_button.png'] button.
  2. Right-click the used project and in the shortcut menu, click the Reset Changes for Selection command.
5. Do one of the following:
  1. To save changes and keep the dialog open, click the Apply button.
  2. To save changes and close the dialog, click the OK button.
  3. To discard changes and close the dialog, click the Cancel button.
6. Click the OK button to close the Project Usages dialog.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>Used projects employ the sticky versions approach. Once a specific version of a project is used, the main project continues to use that exact version until you update it manually. This means that even if you modify a used project and save it as a new version, the main project will still use the previously added version. This prevents unexpected changes or damage to the main project.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="d6d6403b-461c-48bf-a780-7b77a1ed129e"><ac:rich-text-body><p>A project must be stored in the <ac:link><ri:page ri:content-title="Managing local projects" /><ac:plain-text-link-body><![CDATA[local repository]]></ac:plain-text-link-body></ac:link> before it can be used locally.</p></ac:rich-text-body></ac:structured-macro><p style="text-align: center;"><span style="color:var(--ds-background-accent-red-subtle,#f87168);"><strong><ac:image><ri:attachment ri:filename="sticky_versions.png" /></ac:image></strong></span></p><h6 style="text-align: center;">The main project uses only the specified versions of the used projects, despite the newer versions they may have. </h6><h4>Using a project from the local repository via the Use Local Project command</h4><p>To use a project from the local repository via the Use Local Project command</p><hr /><ol><li data-uuid="ee2e66fd-36ba-4099-9bf9-834aa11e3f0c">In the main menu, select <strong>File </strong>&gt; <strong>Use Project </strong>&gt; <strong>Use Local Project</strong>. The <strong>Use Project</strong> dialog opens.<br /><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="77e67fd0-936a-4e83-8893-f0e346ec6731"><ac:rich-text-body><p>If there are no other projects in the local repository or all of them are already used in the open project, the <strong>Use Local Project </strong>command is disabled.</p></ac:rich-text-body></ac:structured-macro></li><li data-uuid="f2b73152-4cbd-4b36-a7f6-4e3172caf712">In the <strong>Use Project</strong> dialog, select the project you want to use and click the <strong>Next </strong>button.</li><li data-uuid="00487bb7-abb7-45b1-98cd-ce9e23ac9df8">Select the project version you want to use and click the <strong>Finish</strong> button.<br />Used projects are displayed under the <strong>Used Projects</strong> node in the Containment tree of your model.<br /><ac:image><ri:attachment ri:filename="Used Projects node in the Containment tree.png" /></ac:image></li></ol><h4>Using a project from the local repository via the Project Usages dialog</h4><p>To use a project from the local repository via the Project Usages dialog</p><hr /><ol><li data-uuid="08db1b6b-6d51-4e4b-a86e-721d22ed06e7"><ac:link ac:anchor="Opening the Project Usages dialog"><ri:page ri:content-title="Managing local used projects" /><ac:link-body>Open the <strong>Project Usages</strong> dialog</ac:link-body></ac:link>. </li><li data-uuid="2c4c8e38-a5f3-4419-8f18-a2245b821d62">In the <strong>Project Usages </strong>dialog's toolbar, click the <strong>Use Project <ac:image><ri:attachment ri:filename="use_project_button.png" /></ac:image> </strong>button. The <strong>Use Project</strong> dialog opens.</li><li data-uuid="ab526153-2a5f-4f93-9184-529442c4d7a0">In the <strong>Use Project</strong> dialog, select the project you want to use and click the <strong>OK </strong>button.<br /><ac:image><ri:attachment ri:filename="Using a project from the local repository via the Project Usages dialog.png" /></ac:image></li><li data-uuid="241af7f5-678b-459d-9b73-a7ca04496061">Click the <strong>OK</strong> button to close the <strong>Project Usages</strong> dialog.<br />Used projects are displayed under the <strong>Used Projects</strong> node in the Containment tree of your model.</li></ol><h4>Using a project from the local repository via the Advanced Project Usages Configuration dialog</h4><p>To use a project from the local repository via the Advanced Project Usages Configuration dialog</p><hr /><ol><li data-uuid="9fe684c8-c14b-49ae-954c-a526685dd3ec"><ac:link ac:anchor="Opening the Advanced Project Usages Configuration dialog"><ri:page ri:content-title="Managing local used projects" /><ac:link-body>Open the <strong>Advanced Project Usages Configuration </strong>dialog</ac:link-body></ac:link>.</li><li data-uuid="76be2c26-3126-463d-906a-bc323d19f20b">In the <strong>Advanced Project Usages Configuration</strong> dialog's toolbar, <span>click the <strong>Add</strong> <ac:image><ri:attachment ri:filename="add_button.png" /></ac:image> button</span>, and in its dropdown menu, click <strong>Use Project</strong><span>. </span>The <strong>Use Project</strong> dialog opens.</li><li data-uuid="eaecb8f8-e0b1-4c30-9cdf-7753caa94c9c">In the <strong>Use Project</strong> dialog, select the project you want to use and click the <strong>OK </strong>button. The cell in the <strong>Action</strong> column for the added used project states '<strong>Add</strong>'.  <br /><ac:image><ri:attachment ri:filename="Using a project from the local repository via the Advanced Usages Configuration dialog.png" /></ac:image></li><li data-uuid="592b5117-694d-40ad-a0e2-04afbf6b2655">(Optional) To undo the action, do one of the following:<ol><li>In the dialog's toolbar, click the <strong>Reset Changes for Selection</strong> <ac:image><ri:attachment ri:filename="reset_changes_for_selection_button.png" /></ac:image> button.</li><li>Right-click the used project and in the shortcut menu, click the <strong>Reset Changes for Selection </strong>command.</li></ol></li><li data-uuid="300e64ff-d3c5-4476-85f7-e7275111c0a3">Do one of the following:<ol><li>To save changes and keep the dialog open, click the <strong>Apply </strong>button.</li><li>To save changes and close the dialog, click the <strong>OK </strong>button.</li><li>To discard changes and close the dialog, click the <strong>Cancel</strong> button.</li></ol></li><li data-uuid="8a57881b-ad94-4abe-a865-2cf8c501fa7e">Click the <strong>OK </strong>button to close the <strong>Project Usages </strong>dialog.</li></ol><p><br /></p>
````

<!--NOMAGIC_PAGE id=286557674 space=SYSML2P version=15 -->
## PAGE 00741: Validating the model

- page_id: `286557674`
- space_key: `SYSML2P`
- source_url: https://docs.nomagic.com/spaces/SYSML2P/pages/286557674/Validating+the+model
- version_number: 15
- version_date: `2026-02-26T14:50:51.016+01:00`
- ancestors: SysML v2 Plugin Documentation > Model analysis > Validation
- labels: []

### NORMALIZED CONTENT

You can validate the model against [CONFLUENCE_PAGE title='Enabling validation suites' space=''] using the following options:

- Validate elements recursively via the .
- Elements that fail validation are automatically highlighted in views. You can review the validation results in the [CONFLUENCE_PAGE title='Reviewing validation results' space=''] .
- Elements that fail validation are automatically highlighted in the Textual Editor when the [CONFLUENCE_PAGE title='Environment options' space='']**Run Validation** environment option is enabled. You can view the validation results in the [CONFLUENCE_PAGE title='Reviewing validation results' space=''] . Currently, only active validation is supported in the modeling tool. Active validation runs automatically, i.e., elements are automatically checked against [CONFLUENCE_PAGE title='Enabling validation suites' space=''] without user input, and failing elements' symbols are highlighted in views.

##### Validating the model

###### Validating model elements via the Validate command

To validate model elements via the Validate command

- Right-click an element in the Containment tree or an element symbol in a view and in the shortcut menu, click Validate . The element is validated recursively against [CONFLUENCE_PAGE title='Enabling validation suites' space=''] . The [CONFLUENCE_PAGE title='Reviewing validation results' space=''] opens, allowing you to review the validation results. If you modify the element(s) for which the **Validation Results panel**was opened, you need to repeat the validation to update its results. [ATTACHMENT filename='Validating Elements.png']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>You can validate the model against <ac:link><ri:page ri:content-title="Enabling validation suites" /><ac:plain-text-link-body><![CDATA[enabled validation suites]]></ac:plain-text-link-body></ac:link> using the following options:</p><ul><li>Validate elements recursively via the <ac:link ac:anchor="Validating model elements via the Validate command"><ac:plain-text-link-body><![CDATA[Validate command]]></ac:plain-text-link-body></ac:link>.</li><li data-uuid="c47bc1dc-3c7f-43e4-b229-d21774eeb5c6">Elements that fail validation are automatically highlighted in views. You can review the validation results in the <ac:link><ri:page ri:content-title="Reviewing validation results" /><ac:plain-text-link-body><![CDATA[Validation Results panel]]></ac:plain-text-link-body></ac:link>.</li><li data-uuid="9436e0ba-3be4-49c0-ae5d-b25858e2df49">Elements that fail validation are automatically highlighted in the Textual Editor when the <ac:link><ri:page ri:content-title="Environment options" /><ac:link-body><strong>Run Validation</strong> environment option</ac:link-body></ac:link> is enabled. You can view the validation results in the <ac:link><ri:page ri:content-title="Reviewing validation results" /><ac:plain-text-link-body><![CDATA[Validation Results panel]]></ac:plain-text-link-body></ac:link>.<br /><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="6d952c51-3cf3-4bda-95fd-fbb11fe5f027"><ac:rich-text-body><p>Currently, only active validation is supported in the modeling tool. Active validation runs automatically, i.e., elements are automatically checked against <ac:link><ri:page ri:content-title="Enabling validation suites" /><ac:plain-text-link-body><![CDATA[enabled validation suites]]></ac:plain-text-link-body></ac:link> without user input, and failing elements' symbols are highlighted in views.</p></ac:rich-text-body></ac:structured-macro></li></ul><h3>Validating the model</h3><h4>Validating model elements via the Validate command</h4><p>To validate model elements via the Validate command</p><hr /><ul><li data-uuid="61dc6f07-2f54-4c84-9e1b-c694c13d018f">Right-click an element in the Containment tree or an element symbol in a view and in the shortcut menu, click <strong>Validate</strong>.<br />The element is validated recursively against <ac:link><ri:page ri:content-title="Enabling validation suites" /><ac:plain-text-link-body><![CDATA[enabled validation suites]]></ac:plain-text-link-body></ac:link>. The <strong><ac:link><ri:page ri:content-title="Reviewing validation results" /><ac:plain-text-link-body><![CDATA[Validation Results panel]]></ac:plain-text-link-body></ac:link></strong> opens, allowing you to review the validation results.<br /><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="86e032dc-2a78-4c03-9e9c-f14fe25353eb"><ac:rich-text-body><p>If you modify the element(s) for which the <strong>Validation Results panel </strong>was opened, you need to repeat the validation to update its results.</p></ac:rich-text-body></ac:structured-macro><ac:image><ri:attachment ri:filename="Validating Elements.png" /></ac:image></li></ul>
````

<!--NOMAGIC_PAGE id=314180982 space=SYSML2P version=7 -->
## PAGE 00742: Validating the transformed model

- page_id: `314180982`
- space_key: `SYSML2P`
- source_url: https://docs.nomagic.com/spaces/SYSML2P/pages/314180982/Validating+the+transformed+model
- version_number: 7
- version_date: `2026-06-25T11:29:57.398+02:00`
- ancestors: SysML v2 Plugin Documentation > SysML v1 to SysML v2 transition > SysML v1 to v2 model conversion
- labels: []

### NORMALIZED CONTENT

**[IMAGE alt='' src='']**

##### Overview

This activity diagram describes the final validation activities used to verify that the transformed SysML v2 model preserves the intent of the original SysML v1 model.

##### Process

Validation begins by ensuring that the SysML v2 model supports the required standard views used for engineering activities.

The transformed model is then evaluated to confirm that its structure, semantics, and behavior remain consistent with the original SysML v1 model.

Typical validation activities include:

- Validating model accuracy.
- Comparing SysML v1 and SysML v2 model structures.
- Comparing execution results.
- Comparing analysis results.

Examples may include comparing:

- Structural hierarchies.
- Requirements relationships.
- Simulation outputs.
- Analysis metrics such as mass, performance, or other calculated values.

Equivalent execution and analysis results provide confidence that the transformed model maintains the same engineering intent as the original source model.

Finally, diagram layouts may be adjusted manually to improve readability and presentation quality after migration.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong><ac:image><ri:attachment ri:filename="Validating the transformed model.jpg" /></ac:image></strong></p><h3>Overview</h3><p>This activity diagram describes the final validation activities used to verify that the transformed SysML v2 model preserves the intent of the original SysML v1 model.</p><h3>Process </h3><p>Validation begins by ensuring that the SysML v2 model supports the required standard views used for engineering activities.</p><p>The transformed model is then evaluated to confirm that its structure, semantics, and behavior remain consistent with the original SysML v1 model.</p><p>Typical validation activities include:</p><ul><li data-uuid="71654189-e363-4fd5-ac6f-6cfc520a02bd">Validating model accuracy.</li><li data-uuid="cbfce7fc-3f30-4ade-8dbe-397104dea1e0">Comparing SysML v1 and SysML v2 model structures.</li><li data-uuid="89f06a3b-a3b4-45ce-b73b-4d5669be3181">Comparing execution results.</li><li data-uuid="d85e47f1-8c6e-414c-ae03-966eeaa8b0f4">Comparing analysis results.</li></ul><p>Examples may include comparing:</p><ul><li data-uuid="3d1d10b0-0af0-4b2b-a509-e1e715fe68d0">Structural hierarchies.</li><li data-uuid="8ffa6979-ca53-4975-944d-619fe64bf877">Requirements relationships.</li><li data-uuid="6d05e539-176d-4ee0-be37-f33adfe27639">Simulation outputs.</li><li data-uuid="52967c4a-79a7-4fb2-b125-c7fe2cb4f750">Analysis metrics such as mass, performance, or other calculated values.</li></ul><p>Equivalent execution and analysis results provide confidence that the transformed model maintains the same engineering intent as the original source model.</p><p>Finally, diagram layouts may be adjusted manually to improve readability and presentation quality after migration.</p><p><br /></p>
````

<!--NOMAGIC_PAGE id=286557629 space=SYSML2P version=12 -->
## PAGE 00743: Validation

- page_id: `286557629`
- space_key: `SYSML2P`
- source_url: https://docs.nomagic.com/spaces/SYSML2P/pages/286557629/Validation
- version_number: 12
- version_date: `2026-06-26T11:32:36.564+02:00`
- ancestors: SysML v2 Plugin Documentation > Model analysis
- labels: []

### NORMALIZED CONTENT

This release introduces model validation, which helps ensurethe accuracy, completeness, and consistency of your models.The modeling tool checks elements against validation rules delivered through SysML, KerML, and Dassault Systèmes predefined validation rules. By automatically identifying modeling issues, validation helps maintain model quality and supports compliance with modeling standards.

For more information, see the pages in this section.

600450

[IMAGE alt='' src='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p style="text-align: left;"><span style="color:var(--ds-text,#172b4d);">This release introduces model validation, which helps ensure<span> </span></span><span style="color:var(--ds-text,#172b4d);">the accuracy, completeness, and consistency of your models.<span> </span></span><span style="color:var(--ds-text,#172b4d);">The modeling tool checks elements against validation rules delivered through SysML, KerML, and Dassault Systèmes predefined validation rules. By automatically identifying modeling issues, validation helps maintain model quality and supports compliance with modeling standards.</span></p><p style="text-align: left;">For more information, see the pages in this section.</p><p style="text-align: center;"><ac:structured-macro ac:name="widget" ac:schema-version="1" ac:macro-id="cc953d0d-c63e-4166-9a90-08015dd4323a"><ac:parameter ac:name="width">600</ac:parameter><ac:parameter ac:name="url"><ri:url ri:value="https://youtu.be/0BCAk6hI4SY" /></ac:parameter><ac:parameter ac:name="height">450</ac:parameter></ac:structured-macro></p><p style="text-align: center;"><ac:image ac:align="center"><ri:attachment ri:filename="Validating Elements in Views.png" /></ac:image></p>
````

<!--NOMAGIC_PAGE id=303464473 space=SYSML2P version=2 -->
## PAGE 00744: Variability

- page_id: `303464473`
- space_key: `SYSML2P`
- source_url: https://docs.nomagic.com/spaces/SYSML2P/pages/303464473/Variability
- version_number: 2
- version_date: `2026-04-24T15:43:21.168+02:00`
- ancestors: SysML v2 Plugin Documentation > Element management > Working with elements
- labels: []

### NORMALIZED CONTENT

Variability is commonly associated with a family of design configurations, which is modeled using variations and variants.

- A variation identifies an element in the model that can differ between design configurations.
- Each variation defines a set of design choices, called variants .

**Variation**

- Can be applied to any definition or usage in the model (except enumeration).
- Specifies all possible variants for that variation.

**Variant**

- Is a usage element.
- Its semantics depend on the kind of variation:
  - If the variation is a definition element, each variant is implicitly defined by that variation definition.
  - If the variation is a usage element, each variant implicitly subsets the variation usage.

- For more information on using multiple keywords and their order in element declaration, see the [CONFLUENCE_PAGE title='Managing textual notation' space=''] section on the [CONFLUENCE_PAGE title='Managing textual notation' space=''] page.
- The variation keyword display on the element symbol can be controlled via the Show Modifiers symbol style. See [CONFLUENCE_PAGE title='Modifying styles of individual symbols' space=''] section on the [CONFLUENCE_PAGE title='Modifying styles of individual symbols' space=''] page.
- The variant keyword display in the Containment tree can be controlled via the Show Element Keyword environment option. See the [CONFLUENCE_PAGE title='Environment options' space=''] page.

##### Specifying element variability

###### Specifying element variability via the Textual Editor

To specify element variability via the Textual Editor

1. In the Textual Editor, place the cursor before the element keyword and specify the needed variability keyword: *variation*or *variant*.
2. Click the Synchronize button.

variationpartdefTransmissionChoices:>Transmission{ 
variantpartmanual:ManualTransmission; 
variantpartautomatic:AutomaticTransmission; 
}

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p data-start="127" data-end="244">Variability is commonly associated with a family of design configurations, which is modeled using variations and variants.</p><ul data-start="246" data-end="422"><li data-section-id="1g8hqpc" data-start="246" data-end="347" data-uuid="f91ac59d-ae57-495c-92a0-97cb6d40e1ce">A <em>variation</em> identifies an element in the model that can differ between design configurations.</li><li data-section-id="tad2md" data-start="348" data-end="422" data-uuid="2ff5171e-0ac3-4b9a-a75b-6b6de116ea15">Each variation defines a set of design choices, called <em>variants</em>.</li></ul><p data-start="424" data-end="437"><strong>Variation</strong></p><ul data-start="438" data-end="584"><li data-section-id="1b68btw" data-start="438" data-end="530" data-uuid="6e12c44c-b75a-458a-b0e5-0a06a038a407">Can be applied to any definition or usage in the model (except enumeration).</li><li data-section-id="urzy6g" data-start="531" data-end="584" data-uuid="9352e8f7-c23e-447f-8815-176bc5d588ee">Specifies all possible variants for that variation.</li></ul><p data-start="586" data-end="597"><strong data-start="586" data-end="597">Variant</strong></p><ul data-start="598" data-end="873"><li data-section-id="zscch2" data-start="598" data-end="625" data-uuid="f621c94c-abab-4aed-8040-af67e1e69d2f">Is a usage element.</li><li data-section-id="qtpn2u" data-start="626" data-end="873" data-uuid="65fed2e0-c1bb-471b-ad5a-e8fec92d13c1">Its semantics depend on the kind of variation:<ul data-start="677" data-end="873"><li data-section-id="1palbfw" data-start="677" data-end="783">If the variation is a definition element, each variant is implicitly defined by that variation definition.</li><li data-section-id="14i0gx5" data-start="786" data-end="873">If the variation is a usage element, each variant implicitly subsets the variation usage.</li></ul></li></ul><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="392a7c75-7a2b-4bf6-8c99-23706bcc3b9d"><ac:rich-text-body><ul><li data-uuid="d8907f93-b548-474a-a722-e610c7b0e568">For more information on using multiple keywords and their order in element declaration, see the <ac:link ac:anchor="Keywords"><ri:page ri:content-title="Managing textual notation" /><ac:plain-text-link-body><![CDATA[Keywords]]></ac:plain-text-link-body></ac:link> section on the <ac:link ac:anchor="Keywords"><ri:page ri:content-title="Managing textual notation" /><ac:plain-text-link-body><![CDATA[Managing textual notation]]></ac:plain-text-link-body></ac:link> page. </li><li data-uuid="7f57d6d4-e5b7-4fc1-998b-24d8cc9f9b1d">The <em>variation </em>keyword display on the element symbol can be controlled via the <strong>Show Modifiers</strong> symbol style. See <ac:link ac:anchor="The Symbol Style dialog"><ri:page ri:content-title="Modifying styles of individual symbols" /><ac:plain-text-link-body><![CDATA[The Symbol Style dialog]]></ac:plain-text-link-body></ac:link> section on the <ac:link><ri:page ri:content-title="Modifying styles of individual symbols" /></ac:link> page.</li><li data-uuid="f5480846-3582-4d67-8cbe-6451e01ce710">The <em>variant </em>keyword display in the Containment tree can be controlled via the <strong>Show Element Keyword </strong>environment option. See the <ac:link><ri:page ri:content-title="Environment options" /></ac:link> page.</li></ul></ac:rich-text-body></ac:structured-macro><h3>Specifying element variability</h3><h4>Specifying element variability via the Textual Editor</h4><p>To specify element variability via the Textual Editor</p><hr /><ol><li data-uuid="b2e76c0d-c69a-4d5d-a833-fdf86c6603f1"><span style="color:var(--ds-text,#172b4d);">In the Textual Editor, place the cursor before the element keyword and specify the needed variability keyword: <em>variation </em>or <em>variant</em>.</span></li><li data-uuid="7f5fa46a-aec2-4f63-b55a-cb20e35bbbc6">Click the<span> </span><strong>Synchronize<span> </span></strong>button.</li></ol><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="c69e3e67-cf45-4c01-b7cc-4568c4a1c30a"><ac:rich-text-body><p><span style="color:var(--ds-text-accent-blue,#0055CC);">variation</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055CC);">part</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055CC);">def</span><span style="color:var(--ds-chart-gray-bold,#8590A2);"> </span><span style="color:var(--ds-text-accent-teal,#206A83);">TransmissionChoices</span><span style="color:var(--ds-text,#000000);"> :&gt; </span><span style="color:var(--ds-text-accent-teal,#206A83);">Transmission</span><span style="color:var(--ds-text,#000000);"> {</span><br /><span style="color:var(--ds-text,#000000);">    </span><span style="color:var(--ds-text-accent-blue,#0055CC);">variant</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055CC);">part</span><span style="color:var(--ds-chart-gray-bold,#8590A2);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326C);">manual</span><span style="color:var(--ds-text,#000000);"> : </span><span style="color:var(--ds-text-accent-teal,#206A83);">ManualTransmission</span><span style="color:var(--ds-text,#000000);">;</span><br /><span style="color:var(--ds-text,#000000);">    </span><span style="color:var(--ds-text-accent-blue,#0055CC);">variant</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055CC);">part</span><span style="color:var(--ds-chart-gray-bold,#8590A2);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326C);">automatic</span><span style="color:var(--ds-text,#000000);"> : </span><span style="color:var(--ds-text-accent-teal,#206A83);">AutomaticTransmission</span><span style="color:var(--ds-text,#000000);">;</span><br /><span style="color:var(--ds-text,#000000);">}</span></p></ac:rich-text-body></ac:structured-macro><p><br /></p>
````

<!--NOMAGIC_PAGE id=249577888 space=SYSML2P version=6 -->
## PAGE 00745: Verification case

- page_id: `249577888`
- space_key: `SYSML2P`
- source_url: https://docs.nomagic.com/spaces/SYSML2P/pages/249577888/Verification+case
- version_number: 6
- version_date: `2025-09-30T14:55:29.076+02:00`
- ancestors: SysML v2 Plugin Documentation > Model composition > Analysis & Verification
- labels: []

### NORMALIZED CONTENT

A verification case is a kind of case whose result is a verdict on whether the subject of the case satisfies certain requirements. A typical verification case includes a set of verification actions that collect data about the subject, analyze it, and evaluate the results based on the objective to produce a verdict.

##### Creating verification case usage and definition elements

###### Creating verification case usage and definition elements via the Textual Editor

To create verification case usage and definition elements via the Textual Editor

1. In the Textual Editor, place the cursor where you want to create the element and declare the keyword:
  1. *verification def*for a verification definition.
  2. *verification* for a verification usage.
2. Specify the element name.
3. Specify the verification features in the element body.
4. Click the Synchronize button. verificationdefVehicleMassTest{ // verification definition 
subjecttestVehicle:Vehicle; 
objectivevehicleMassVerificationObjective{ 
verifyvehicleMassRequirement; 
} 
actioncollectData{ 
// ... 
} 
actionprocessData{ 
// ... 
} 
actionevaluateData{ 
// ... 
} 
returnverdict:VerificationCases::VerdictKind=evaluateData.verdict; 
}verificationvehicleMassTest:VehicleMassTest; // verification usage

###### Creating verification case usage and definition elements via the Create Element command

To create verification case usage and definition elements via the Create Element command

1. In the Containment tree, right-click an element, and in the shortcut menu, click **Create Element**.
2. In the Create Element dialog, select one of the following:
  1. verification def to create a verification definition element.
  2. verification to create a verification usage element.
3. Name the element.
4. Specify the verification features.

###### Creating verification case usage and definition elements via the view palette

To create verification case usage and definition elements via the view palette

1. In the view palette, under the Cases group, click one of the following:
  1. The **verification** def button to create a part definition element.
  2. The **verification** button to create a part usage element. If the needed button is not displayed, click the down-facing arrow next to either the **verification**or the **verification def**button and select the needed button in the dropdown menu.
2. Click in the view pane where you want to create the element symbol.
3. (Optional) Specify the verification features.

###### Auto-creating verification case definition elements via the Extract Definition commands

To auto-create verification case definition elements via the Extract Definition commands

- See the [CONFLUENCE_PAGE title='Extract Definition and Usage' space='']page.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>A verification case is a kind of case whose result is a verdict on whether the subject of the case satisfies certain requirements. A typical verification case includes a set of verification actions that collect data about the subject, analyze it, and evaluate the results based on the objective to produce a verdict.</p><h3>Creating verification case usage and definition elements</h3><h4>Creating verification case usage and definition elements via the Textual Editor</h4><p>To create verification case usage and definition elements via the Textual Editor</p><hr /><ol><li>In the Textual Editor, place the cursor where you want to create the element and declare the keyword: <ol><li><p class="auto-cursor-target"><span> </span><em>verification def</em><span> </span>for a verification definition.</p></li><li><span> <em>verification</em></span><em><span> </span></em>for a verification usage.</li></ol></li><li>Specify the element name.</li><li>Specify the verification features in the element body.</li><li>Click the <strong>Synchronize </strong>button.<br /><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="f1af8d45-8838-424f-8130-2fa40803394a"><ac:rich-text-body><p><span style="color:var(--ds-text-accent-blue,#0055cc);">verification</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">def</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-teal,#206a83);">VehicleMassTest</span><span style="color:var(--ds-text,#000000);"> {  <span style="color:var(--ds-text-accent-green-bolder,#164b35);">// verification definition</span></span><br /><span style="color:var(--ds-text,#000000);">    </span><span style="color:var(--ds-text-accent-blue,#0055cc);">subject</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">testVehicle</span><span style="color:var(--ds-text,#000000);"> : </span><span style="color:var(--ds-text-accent-teal,#206a83);">Vehicle</span><span style="color:var(--ds-text,#000000);">;</span><br /><span style="color:var(--ds-text,#000000);">    </span><span style="color:var(--ds-text-accent-blue,#0055cc);">objective</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">vehicleMassVerificationObjective</span><span style="color:var(--ds-text,#000000);"> {</span><br /><span style="color:var(--ds-text,#000000);">        </span><span style="color:var(--ds-text-accent-blue,#0055cc);">verify</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">vehicleMassRequirement</span><span style="color:var(--ds-text,#000000);">;</span><br /><span style="color:var(--ds-text,#000000);">    }</span><br /><span style="color:var(--ds-text,#000000);">    </span><span style="color:var(--ds-text-accent-blue,#0055cc);">action</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">collectData</span><span style="color:var(--ds-text,#000000);"> {</span><br /><span style="color:var(--ds-text,#000000);">        </span><span style="color:var(--ds-text-accent-green-bolder,#164b35);">// ...</span><br /><span style="color:var(--ds-text,#000000);">    }</span><br /><span style="color:var(--ds-text,#000000);">    </span><span style="color:var(--ds-text-accent-blue,#0055cc);">action</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">processData</span><span style="color:var(--ds-text,#000000);"> {</span><br /><span style="color:var(--ds-text,#000000);">        </span><span style="color:var(--ds-text-accent-green-bolder,#164b35);">// ...</span><br /><span style="color:var(--ds-text,#000000);">    }</span><br /><span style="color:var(--ds-text,#000000);">    </span><span style="color:var(--ds-text-accent-blue,#0055cc);">action</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">evaluateData</span><span style="color:var(--ds-text,#000000);"> {</span><br /><span style="color:var(--ds-text,#000000);">        </span><span style="color:var(--ds-text-accent-green-bolder,#164b35);">// ...</span><br /><span style="color:var(--ds-text,#000000);">    }</span><br /><span style="color:var(--ds-text,#000000);">    </span><span style="color:var(--ds-text-accent-blue,#0055cc);">return</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">verdict</span><span style="color:var(--ds-text,#000000);"> : </span><span style="color:var(--ds-text-accent-teal,#206a83);">VerificationCases::VerdictKind</span><span style="color:var(--ds-text,#000000);"> = </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">evaluateData.verdict</span><span style="color:var(--ds-text,#000000);">;</span><br /><span style="color:var(--ds-text,#000000);">}</span></p><p><span style="color:var(--ds-text-accent-blue,#0055cc);">verification</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">vehicleMassTest</span><span style="color:var(--ds-text,#000000);"> : </span><span style="color:var(--ds-text-accent-teal,#206a83);">VehicleMassTest</span><span style="color:var(--ds-text,#000000);">;    <span style="color:var(--ds-text-accent-green-bolder,#164b35);">// verification usage</span></span></p></ac:rich-text-body></ac:structured-macro></li></ol><h4>Creating verification case usage and definition elements via the Create Element command</h4><p>To create verification case usage and definition elements via the Create Element command</p><hr /><ol><li><p class="auto-cursor-target">In the Containment tree, right-click an element, and in the shortcut menu, click <strong>Create Element</strong>.</p></li><li>In the <strong>Create Element</strong> dialog, select one of the following:<ol><li><strong>verification def</strong> to create a verification definition element.</li><li><strong>verification </strong>to create a verification usage element.</li></ol></li><li>Name the element.</li><li>Specify the verification features.</li></ol><h4 class="auto-cursor-target">Creating verification case usage and definition elements via the view palette</h4><p>To create verification case usage and definition elements via the view palette</p><hr /><ol><li data-uuid="82615852-e7fc-40b2-8d08-39c3adc43fa7">In the view palette, under the Cases group, click one of the following:<ol><li>The<span> <strong>verification </strong></span><strong>def </strong>button to create a part definition element.</li><li>The<span> <strong>verification</strong></span> button to create a part usage element.<br /><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="769c3a3a-7b27-471d-b151-165748c95ab6"><ac:rich-text-body><p>If the needed button is not displayed, click the down-facing arrow next to either the <strong>verification </strong>or the <strong>verification def </strong>button and select the needed button in the dropdown menu.</p></ac:rich-text-body></ac:structured-macro></li></ol></li><li data-uuid="cc56ef2e-941a-4441-b1e1-a2b8ba7c85ba">Click in the view pane where you want to create the element symbol.</li><li data-uuid="d7ffdbb8-bb17-4bc1-8aa3-308ee2e98686">(Optional) Specify the verification features.</li></ol><h4>Auto-creating verification case definition elements via the Extract Definition commands</h4><p><span>To auto-create verification case definition elements via the Extract Definition commands</span></p><hr /><ul><li><span><span style="color:var(--ds-text,#172b4d);">See the <ac:link><ri:page ri:content-title="Extract Definition and Usage" /></ac:link></span><span style="color:var(--ds-text,#172b4d);"> </span><span style="color:var(--ds-text,#172b4d);">page.</span></span></li></ul>
````

<!--NOMAGIC_PAGE id=254410784 space=SYSML2P version=1 -->
## PAGE 00746: Versions of SysML v2 Plugin Documentation

- page_id: `254410784`
- space_key: `SYSML2P`
- source_url: https://docs.nomagic.com/spaces/SYSML2P/pages/254410784/Versions+of+SysML+v2+Plugin+Documentation
- version_number: 1
- version_date: `2025-09-11T09:31:39.626+02:00`
- ancestors: 
- labels: []

### NORMALIZED CONTENT

94aa0f655f4ee3100f0a30caeddc4f1e

SysML v2 Plugin Documentation

documentVersions

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="scroll-document-location" ac:schema-version="1" ac:macro-id="d5f7e2fa-9afc-4a08-b60c-b4f50e80eecf"><ac:parameter ac:name="permaId">94aa0f655f4ee3100f0a30caeddc4f1e</ac:parameter><ac:parameter ac:name="documentTitle">SysML v2 Plugin Documentation</ac:parameter><ac:parameter ac:name="key">documentVersions</ac:parameter></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=249577124 space=SYSML2P version=4 -->
## PAGE 00747: View image export

- page_id: `249577124`
- space_key: `SYSML2P`
- source_url: https://docs.nomagic.com/spaces/SYSML2P/pages/249577124/View+image+export
- version_number: 4
- version_date: `2025-09-22T13:43:57.044+02:00`
- ancestors: SysML v2 Plugin Documentation > Model management > Working with views
- labels: []

### NORMALIZED CONTENT

Before exporting a diagram, you should specify the Image Export options in the **Project Options** dialog. You can also make additional image export changes in the**Environment Options** dialog. These options are applicable to all operations dedicated to exporting or previewing diagrams, such as:

- [CONFLUENCE_PAGE title='Saving as image' space='']
- [CONFLUENCE_PAGE title='Printing' space='']
- [CONFLUENCE_PAGE title='Printing' space='']

##### Specifying Project Options for diagram image export

Via the Image Export options in the **Project Options** dialog, you can specify the dimensions for the exported diagram, what should be done if these dimensions are exceeded, and the time it can take to build it (the latter applies only to tables and matrices). The changes you make in the **Project Options** dialog apply only to a specific project.

To specify project options for diagram image export

- In the main menu, select Options > Project > under the General group, select Diagrams > modify the options in the Image Export group.

In the table below, you can see the descriptions of the diagram Image Export options and their default values.

| Project Option | Default Value | Description |
| --- | --- | --- |
| Time Limit to Build Diagram | 60 | Specify the maximum time (in seconds) allotted for diagram building while exporting a diagram. If the time limit is exceeded, the diagram is not exported. Set to 0 to export diagram without the time limit. |
| Image Height Limit | 10 000 | Specify the maximum image height (in pixels) for diagram export. If the height limit is exceeded, the exported diagram is cropped, or the diagram is not exported at all, depending on the selected preference. Set to 0 to export the diagram without the image height limit. |
| Image Width Limit | 10 000 | Specify the maximum image width (in pixels) for diagram export. If the width limit is exceeded, the exported diagram is cropped, or the diagram is not exported at all, depending on the selected preference. Set to 0 to export diagram without the image width limit. |
| Export Preference When Limits Exceeded | Export Cropped Diagram | Specify the diagram export preference if the diagram image height and/or width limits are exceeded.If the Export Preference When Limits Exceeded value is set to Export Cropped Diagram, the previewed or exported diagram is cropped based on the specified dimensions, displaying an incomplete view of the diagram that looks like the image below. |

##### Specifying Environment Options for image export

You can also make additional image export changes in the modeling tool's environment, such as image resolution and compression quality. The modifications you make in the **Environment Options** dialog persist when the application is closed and re-opened and thus apply to all projects.

To specify environment options for image export

- In the main menu, select **Options** > **Environment** > under the **General** group, select**Image Export** > modify the options in the **Image Export** group.

In the table below, you can see the descriptions of the environment Image Export options and their default values.

| Environment Option | Default Value | Description |
| --- | --- | --- |
| Save Diagram Background in Image | false | Set to true to save the diagram together with its background as an image. Otherwise, the diagram background becomes white after saving the diagram as an image. |
| JPEG Compression Quality | 1.0 | Specify the quality for saving an image as a JPEG file. Set the value to 1.0 to define the highest quality. |
| Use SVG <text> Tag for Text Output | false | Set to true to turn all text into SVG shapes during the image conversion. |
| Roboto Font Inclusion in SVG | Web Font Link | The option controls how the Roboto font is handled in the exported SVG file. Select 'None' to exclude font data or font references in the SVG; text may fall back to system fonts depending in the viewer's environment. Select 'Web Font Link' to reference the Roboto font from Google Fonts for consistent rendering across systems; requires internet access. Select 'Embed TTF' to embed the Roboto font as a TrueType Font in the SVG for offline portability and consistent rendering; increases file size. This option is ignored if 'Use SVG <text> Tag for Text Output' option is disabled. |
| Letter Spacing Reduction in SVG | 3 | Specify spacing reduction between letters when exporting SVG with <text> tag. Use the slider to specify a number between 0 and 10, where 1 means -0.1 px. Increasing the number reduces the spacing between the letters. Enable the Use SVG <text> Tag for Text Output option to use the Letter Spacing Reduction in SVG option. |
| Render SVG Icons as Raster Images in EMF | false | Set to true to render SVG icons as raster images in the EMF output. Otherwise, the SVG icons are rendered as vector graphics. |
| Image Resolution (DPI) | 72 | Specify the measure for spatial printing. |
| Exported Image Size [%] | 100 | Specify exported image scaling ratio in percent. If the set value is higher than 100, then the view is enlarged (zoomed in) before generating an image. Raster image will not lose its quality as additional pixels are introduced. |
| TIFF Color Space | RGB | Specify the color format for the tagged image file format (TIFF). |
| TIFF Compression | LZW | Specify the type for compression of the tagged image file format (TIFF). |

##### Diagram image export notifications and statistics

The following table displays the expected results of specific diagram image export options.

| Export option | Successful export | Diagram does not comply with Image Export options or the export failed |  |
| --- | --- | --- | --- |
| Save as Image | All diagrams are saved as they are in the modeling tool.The file location is opened. | Single diagram export | Multiple diagrams export |
| The diagram is saved as it is in the modeling tool.The file location is opened. | A notification is displayed with the information about image export, e.g.: Click Details... to see Diagram Image Export Statistics. |  |  |

The **Details...** link in the notifications opens the **Notification Window**, which displays **Diagram Image Export Statistics**with the following information:

- Total : the number of exported diagrams.
- Cropped : the number of diagrams exported with limited dimensions if the Export Preference When Limits Exceeded option is set to Export Cropped Diagram .
- **Failed**: the number of diagrams not exported due to the exceeded building time and/or dimension limits if the **Export Preference When Limits Exceeded** option is set to *Do Not Export*. It also displays the number of diagrams whose export failed. The **Failed**and**Cropped** indications are only displayed if there are any cropped or failed diagram images. [IMAGE alt='' src='']

##### Image export as a SVG file

Diagrams and symbols that were created in the model can be saved as images in the Scalable Vector Graphics (*.svg) format via the following options:

- [CONFLUENCE_PAGE title='Saving as image' space='']

###### Disabling SVG image caching

By default, SVG images are cached in the modeling tool. However, you can disable the caching anytime by following the procedure below.

To disable SVG image caching

1. Open the <modeling tool name>.properties file, which is located at <modeling tool installation directory>\bin .
2. In the JAVA_ARGS line, add the following property: -Dexport.svg.without.caching=true
3. Save the file and restart the modeling tool.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>Before exporting a diagram, you should specify the Image Export options in the <strong>Project Options</strong> dialog. You can also make additional image export changes in the<strong> Environment Options</strong> dialog. These options are applicable to all operations dedicated to exporting or previewing diagrams, such as:</p><ul><li><ac:link><ri:page ri:content-title="Saving as image" /><ac:plain-text-link-body><![CDATA[Save as Image]]></ac:plain-text-link-body></ac:link></li><li><ac:link><ri:page ri:content-title="Printing" /><ac:plain-text-link-body><![CDATA[Print]]></ac:plain-text-link-body></ac:link></li><li><ac:link ac:anchor="Print preview"><ri:page ri:content-title="Printing" /><ac:plain-text-link-body><![CDATA[Print Preview]]></ac:plain-text-link-body></ac:link></li></ul><h3>Specifying Project Options for diagram image export</h3><p>Via the Image Export options in the <strong>Project Options</strong> dialog, you can specify the dimensions for the exported diagram, what should be done if these dimensions are exceeded, and the time it can take to build it (the latter applies only to tables and matrices). The changes you make in the <strong>Project Options</strong> dialog apply only to a specific project.</p><p><br /></p><p>To specify project options for diagram image export</p><hr /><ul><li>In the main menu, select <strong>Options</strong> &gt; <strong>Project</strong> &gt; under the <strong>General</strong> group, select <strong>Diagrams</strong> &gt; modify the options in the <strong>Image Export</strong> group.</li></ul><p><br /></p><p>In the table below, you can see the descriptions of the diagram Image Export options and their default values.</p><table class="relative-table wrapped" style="width: 99.9333%;"><colgroup> <col style="width: 19.9635%;" /> <col style="width: 14.222%;" /> <col style="width: 65.8261%;" /> </colgroup><tbody><tr><th>Project Option</th><th>Default Value</th><th>Description</th></tr><tr><td>Time Limit to Build Diagram</td><td>60</td><td><div class="content-wrapper"><p>Specify the maximum time (in seconds) allotted for diagram building while exporting a diagram. If the time limit is exceeded, the diagram is not exported. Set to 0 to export diagram without the time limit.</p></div></td></tr><tr><td>Image Height Limit<span> </span></td><td>10 000<span> </span></td><td><p>Specify the maximum image height (in pixels) for diagram export. If the height limit is exceeded, the exported diagram is cropped, or the diagram is not exported at all, depending on the selected preference. Set to 0 to export the diagram without the image height limit.</p></td></tr><tr><td>Image Width Limit<span> </span></td><td>10 000<span> </span></td><td><p>Specify the maximum image width (in pixels) for diagram export. If the width limit is exceeded, the exported diagram is cropped, or the diagram is not exported at all, depending on the selected preference. Set to 0 to export diagram without the image width limit.</p></td></tr><tr><td colspan="1">Export Preference When Limits Exceeded</td><td colspan="1"><p>Export Cropped Diagram</p></td><td colspan="1"><div class="content-wrapper"><p>Specify the diagram export preference if the diagram image height and/or width limits are exceeded.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="0817ac24-d800-4be7-ae7f-4322c23b9ac1"><ac:rich-text-body><p>If the <strong>Export Preference When Limits Exceeded</strong> value is set to <span><strong>Export Cropped Diagram</strong>, the previewed or exported diagram is cropped based on the specified dimensions, displaying an incomplete view of the diagram that looks like the image below.<br /><ac:image><ri:attachment ri:filename="Export_Cropped_Diagram.jpg" /></ac:image><br /></span></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></div></td></tr></tbody></table><h3><span>Specifying Environment Options for image export</span></h3><p><span>You can also make additional image export changes in the modeling tool's environment, such as image resolution and compression quality. The modifications you make in the <strong>Environment Options</strong> dialog persist when the application is closed and re-opened and thus apply to all projects.<br /></span></p><p><span> <br /></span></p><p><span>To specify environment options for image export</span></p><hr /><ul><li><span>In the main menu, select <strong>Options</strong> &gt; <strong>Environment</strong> &gt; under the <strong>General</strong> group, select<strong> Image Export</strong> &gt; modify the options in the <strong>Image Export</strong> group.<br class="_mce_tagged_br" /></span></li></ul><p><span> <br /></span></p><p><span>In the table below, you can see the descriptions of the environment Image Export options and their default values.</span></p><table class="relative-table wrapped" style="width: 99.9333%;"><colgroup><col style="width: 26.1878%;" /><col style="width: 11.423%;" /><col style="width: 62.4008%;" /></colgroup><tbody><tr><th>Environment Option</th><th>Default Value</th><th>Description</th></tr><tr><td>Save Diagram Background in Image</td><td>false</td><td>Set to true to save the diagram together with its background as an image. Otherwise, the diagram background becomes white after saving the diagram as an image.</td></tr><tr><td>JPEG Compression Quality</td><td>1.0</td><td>Specify the quality for saving an image as a JPEG file. Set the value to 1.0 to define the highest quality.</td></tr><tr><td>Use SVG &lt;text&gt; Tag for Text Output</td><td>false</td><td>Set to true to turn all text into SVG shapes during the image conversion.</td></tr><tr><td>Roboto Font Inclusion in SVG</td><td>Web Font Link</td><td><p>The option controls how the Roboto font is handled in the exported SVG file. </p><ul><li data-uuid="d4531ef2-201f-45fe-9012-8b0dbabf5d72">Select 'None' to exclude font data or font references in the SVG; text may fall back to system fonts depending in the viewer's environment. </li><li data-uuid="177b014a-233b-444d-9b69-d04a32ecbef8">Select 'Web Font Link' to reference the Roboto font from Google Fonts for consistent rendering across systems; requires internet access. </li><li data-uuid="77b6fff3-8244-44d1-abad-1ebca456da6b">Select 'Embed TTF' to embed the Roboto font as a TrueType Font in the SVG for offline portability and consistent rendering; increases file size. This option is ignored if 'Use SVG &lt;text&gt; Tag for Text Output' option is disabled.</li></ul></td></tr><tr><td>Letter Spacing Reduction in SVG</td><td>3</td><td><div class="content-wrapper"><p>Specify spacing reduction between letters when exporting SVG with &lt;text&gt; tag. Use the slider to specify a number between 0 and 10, where 1 means -0.1 px. Increasing the number reduces the spacing between the letters. </p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="e5b7108b-5cbc-481e-b651-d102d5a2a0ce"><ac:rich-text-body><p>Enable the <strong>Use SVG &lt;text&gt; Tag for Text Output</strong> option to use the <strong>Letter Spacing Reduction in SVG</strong> option.</p></ac:rich-text-body></ac:structured-macro></div></td></tr><tr><td>Render SVG Icons as Raster Images in EMF</td><td>false</td><td>Set to true to render SVG icons as raster images in the EMF output. Otherwise, the SVG icons are rendered as vector graphics.</td></tr><tr><td>Image Resolution (DPI)</td><td>72</td><td>Specify the measure for spatial printing.</td></tr><tr><td>Exported Image Size [%]</td><td>100</td><td>Specify exported image scaling ratio in percent. If the set value is higher than 100, then the view is enlarged (zoomed in) before generating an image. Raster image will not lose its quality as additional pixels are introduced.</td></tr><tr><td>TIFF Color Space</td><td>RGB</td><td>Specify the color format for the tagged image file format (TIFF).</td></tr><tr><td>TIFF Compression</td><td>LZW</td><td>Specify the type for compression of the tagged image file format (TIFF).</td></tr></tbody></table><h3><span>Diagram image export notifications and statistics</span></h3><p><span>The following table displays the expected results of specific diagram image export options.</span></p><table class="relative-table wrapped" style="width: 98.9326%;"><colgroup><col style="width: 17.68%;" /><col style="width: 13.1588%;" /><col style="width: 17.5456%;" /><col style="width: 23.4841%;" /><col style="width: 28.1433%;" /></colgroup><tbody><tr><th style="text-align: left;"><span>Export option</span></th><th style="text-align: left;" colspan="2">Successful export</th><th style="text-align: left;" colspan="2"><span>Diagram does not comply with Image Export options or the export failed</span></th></tr><tr><td rowspan="2">Save as Image</td><td colspan="2" rowspan="2"><ul><li>All diagrams are saved as they are in the modeling tool.</li><li>The file location is opened.</li></ul><p><br /></p></td><th class="highlight-grey" data-highlight-colour="grey"><span title="">Single diagram export</span></th><th class="highlight-grey" data-highlight-colour="grey"><span title="">Multiple diagrams export</span></th></tr><tr><td><ul><li>The diagram is saved as it is in the modeling tool.</li><li>The file location is opened.</li></ul></td><td><div class="content-wrapper"><ul><li>A notification is displayed with the information about image export, e.g.:<br /><ac:image><ri:attachment ri:filename="save_as_image_notification.png" /></ac:image> <br />Click <strong>Details...</strong> to see <strong>Diagram Image Export Statistics</strong>.</li></ul></div></td></tr></tbody></table><p>The <strong>Details...</strong> link in the notifications opens the <strong>Notification Window</strong>, which displays <span> <strong>Diagram Image Export Statistics </strong>with the following information:</span></p><ul><li><strong>Total</strong>: the number of exported diagrams.</li><li><strong>Cropped</strong>: the number of diagrams exported with limited dimensions if the <strong>Export Preference When Limits Exceeded</strong> option is set to <em>Export Cropped Diagram</em>. </li><li><p class="auto-cursor-target"><strong>Failed</strong>: the number of diagrams not exported due to the exceeded building time and/or dimension limits if the <strong>Export Preference When Limits Exceeded</strong> option is set to <em>Do Not Export</em>. It also displays the number of diagrams whose export failed.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="7adbb902-2246-47db-90a3-853e75ffcdb6"><ac:rich-text-body><p>The <strong>Failed </strong>and<strong> Cropped</strong> indications are only displayed if there are any cropped or failed diagram images.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><ac:image><ri:attachment ri:filename="Diagram_image_export_notification_window.png" /></ac:image></p></li></ul><h3 class="auto-cursor-target">Image export as a SVG file</h3><p>Diagrams and symbols that were created in the model can be saved as images in the <span>Scalable Vector Graphics (*.svg) format via the following options: </span></p><ul><li><ac:link><ri:page ri:content-title="Saving as image" /><ac:plain-text-link-body><![CDATA[Save as Image]]></ac:plain-text-link-body></ac:link></li></ul><h4>Disabling SVG image caching</h4><p>By default, SVG images are cached in the modeling tool. However, you can disable the caching anytime by following the procedure below.</p><p>To disable SVG image caching</p><hr /><ol><li>Open the <em>&lt;modeling tool name&gt;.properties</em> file, which is located at <em>&lt;modeling tool installation directory&gt;\bin</em>.</li><li>In the JAVA_ARGS line, add the following property: <em>-Dexport.svg.without.caching=true</em></li><li>Save the file and restart the modeling tool.</li></ol>
````

<!--NOMAGIC_PAGE id=249577878 space=SYSML2P version=3 -->
## PAGE 00748: Viewpoint

- page_id: `249577878`
- space_key: `SYSML2P`
- source_url: https://docs.nomagic.com/spaces/SYSML2P/pages/249577878/Viewpoint
- version_number: 3
- version_date: `2025-09-24T13:11:03.989+02:00`
- ancestors: SysML v2 Plugin Documentation > Model composition
- labels: []

### NORMALIZED CONTENT

A viewpoint definition is a kind of requirement definition that frames the concerns of one or more stakeholders regarding information about a modeled system or domain of interest. The subject of a viewpoint is a view that is required to address the stakeholder concerns. A viewpoint frames the concerns that will be addressed by a view that satisfies the viewpoint. A viewpoint can be specified with assumed and required constraints.****

##### Creating viewpoint usage and definition elements

###### Creating viewpoint usage and definition elements via the Textual Editor

To create viewpoint usage and definition elements via the Textual Editor

1. In the Textual Editor, place the cursor where you want to create the element and declare the keyword:
  1. *viewpoint def*for a viewpoint definition.
  2. *viewpoint* for a viewpoint usage.
2. Specify the element name.
3. .
4. Click the Synchronize button. concern'system breakdown'{ 
stakeholderse:'Systems Engineer'; 
stakeholderivv:'IV&V'; 
} 
concernmodularity{ 
stakeholderse:'Systems Engineer'; 
} 
viewpointdef'System Structure Perspective'{ 
frame'system breakdown'; 
frame'modularity'; 
requireconstraint{ 
doc 
/* A system structure view shall show the hierarchicalpart decomposition of a system, starting with aspecified root part.*/ 
} 
}

###### Auto-creating viewpoint definition elements via the Extract Definition commands

To auto-create viewpoint definition elements via the Extract Definition commands

- See the [CONFLUENCE_PAGE title='Extract Definition and Usage' space='']page.

##### Specifying viewpoints

###### Framing concerns for viewpoints

It is typical for a viewpoint definition to be structured as framing****a set of stakeholder concerns regarding information about a modeled system or domain of interest. The viewpoint then models the requirement for the view in order to address the framed concerns.

- For procedures on concern creation, see the [CONFLUENCE_PAGE title='Concerns' space=''] subsection on the [CONFLUENCE_PAGE title='Concerns' space=''] page.
- You can frame concerns for viewpoints the same way as for requirements. For procedures on concern framing, see the [CONFLUENCE_PAGE title='Concerns' space=''] subsection on the [CONFLUENCE_PAGE title='Concerns' space=''] page.

#### PANEL: Textual notation example of a viewpoint definition with framed concern

Textual notation example of a viewpoint definition with framed concern

concern'system breakdown'{ 
stakeholderse:'Systems Engineer'; 
stakeholderivv:'IV&V'; 
} 
 
viewpointdef'System Structure Perspective'{ 
frame'system breakdown'; 
}

###### Specifying assumed and required constraints for viewpoints

A viewpoint can be specified with assumed and required constraints.

- You can specify assumed and required constraints for viewpoints the same way as for requirements. For procedures on assumed and required constraints creation, see the [CONFLUENCE_PAGE title='Requirement constraints' space=''] page.

#### PANEL: Textual notation example of a viewpoint definition with a require constraint

Textual notation example of a viewpoint definition with a require constraint

viewpointdef'System Structure Perspective'{ 
requireconstraint{ 
doc 
/* A system structure view shall show the hierarchical 
* part decomposition of a system, starting with a 
* specified root part. 
*/ 
} 
}

###### Satisfying viewpoints

Since a viewpoint usage is a kind of requirement usage, a view usage can be declared to satisfy a viewpoint usage using a [CONFLUENCE_PAGE title='Satisfy requirement' space='']. However, as a shortcut, any composite viewpoint usage nested in a view definition or usage is asserted to be satisfied by that view.

#### PANEL: Textual notation example of a viewpoint usage satisfied by a view definition

Textual notation example of a viewpoint usage satisfied by a view definition

viewdef'Part Structure View'{ 
// This viewpoint is asserted to be satisfied by anyinstance of the view definition. 
viewpointvp:'System Structure Perspective'; 
//... 
}

Alternatively, a satisfy requirement usage can be used explicitly between a viewpoint and a view. In particular, a satisfy requirement usage for a viewpoint that is nested in a view definition or usage will, by default, have the containing view as its satisfying feature.

#### PANEL: Textual notation example of a viewpoint usage satisfied by a view usage

Textual notation example of a viewpoint usage satisfied by a view usage

viewpoint'vehicle structure perspective':'System Structure Perspective'{ 
subject:Vehicle; 
} 
view'vehicle parts view':'Part Structure View'{ 
// This asserts that the given viewpoint 'vehicle structure perspective' is satisfied by the 'vehicle parts view'. 
satisfy'vehicle structure perspective'; 
// ... 
}

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>A viewpoint definition is a kind of requirement definition that frames the concerns of one or more stakeholders regarding information about a modeled system or domain of interest. The subject of a viewpoint is a view that is required to address the stakeholder concerns. A viewpoint frames the concerns that will be addressed by a view that satisfies the viewpoint. A viewpoint can be specified with assumed and required constraints.<strong> </strong></p><h3>Creating viewpoint usage and definition elements</h3><h4>Creating viewpoint usage and definition elements via the Textual Editor</h4><p>To create viewpoint usage and definition elements via the Textual Editor</p><hr /><ol><li>In the Textual Editor, place the cursor where you want to create the element and declare the keyword: <ol><li><p class="auto-cursor-target"><span> </span><em>viewpoint def</em><span> </span>for a viewpoint definition.</p></li><li><span> <em>viewpoint</em></span><em><span> </span></em>for a viewpoint usage.</li></ol></li><li>Specify the element name.</li><li><ac:link ac:anchor="Specifying viewpoints"><ac:plain-text-link-body><![CDATA[Specify the viewpoint's features in the element body]]></ac:plain-text-link-body></ac:link>.</li><li>Click the <strong>Synchronize </strong>button.<br /><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="cfface28-484d-4e43-89a3-45c435d448ce"><ac:rich-text-body><p><span style="color:var(--ds-text-accent-blue,#0055cc);">concern</span><span style="color:var(--ds-text,#333333);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">'system breakdown'</span><span style="color:var(--ds-text,#333333);"> {</span><br /><span style="color:var(--ds-text,#333333);">    </span><span style="color:var(--ds-text-accent-blue,#0055cc);">stakeholder</span><span style="color:var(--ds-text,#333333);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">se</span><span style="color:var(--ds-text,#333333);"> : </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">'Systems Engineer'</span><span style="color:var(--ds-text,#333333);">;</span><br /><span style="color:var(--ds-text,#333333);">    </span><span style="color:var(--ds-text-accent-blue,#0055cc);">stakeholder</span><span style="color:var(--ds-text,#333333);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">ivv</span><span style="color:var(--ds-text,#333333);"> : </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">'IV&amp;V'</span><span style="color:var(--ds-text,#333333);">;</span><br /><span style="color:var(--ds-text,#333333);">}</span><br /><span style="color:var(--ds-text-accent-blue,#0055cc);">concern</span><span style="color:var(--ds-text,#333333);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">modularity</span><span style="color:var(--ds-text,#333333);"> {</span><br /><span style="color:var(--ds-text,#333333);">    </span><span style="color:var(--ds-text-accent-blue,#0055cc);">stakeholder</span><span style="color:var(--ds-text,#333333);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">se</span><span style="color:var(--ds-text,#333333);"> : </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">'Systems Engineer'</span><span style="color:var(--ds-text,#333333);">;</span><br /><span style="color:var(--ds-text,#333333);">}</span><br /><span style="color:var(--ds-text-accent-blue,#0055cc);">viewpoint</span><span style="color:var(--ds-text,#333333);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">def</span><span style="color:var(--ds-text,#333333);"> </span><span style="color:var(--ds-text-accent-teal,#206a83);">'System Structure Perspective'</span><span style="color:var(--ds-text,#333333);"> {</span><br /><span style="color:var(--ds-text,#333333);">    </span><span style="color:var(--ds-text-accent-blue,#0055cc);">frame</span><span style="color:var(--ds-text,#333333);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">'system breakdown'</span><span style="color:var(--ds-text,#333333);">;</span><br /><span style="color:var(--ds-text,#333333);">    </span><span style="color:var(--ds-text-accent-blue,#0055cc);">frame</span><span style="color:var(--ds-text,#333333);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">'modularity'</span><span style="color:var(--ds-text,#333333);">;</span><br /><span style="color:var(--ds-text,#333333);">    </span><span style="color:var(--ds-text-accent-blue,#0055cc);">require</span><span style="color:var(--ds-text,#333333);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">constraint</span><span style="color:var(--ds-text,#333333);"> {</span><br /><span style="color:var(--ds-text,#333333);">        </span><span style="color:var(--ds-text-accent-blue,#0055cc);">doc</span><br /><span style="color:var(--ds-text,#333333);">        </span><span style="color:var(--ds-text-accent-green-bolder,#164b35);">/* A system structure view shall show the hierarchical </span><span style="color:var(--ds-text-accent-green-bolder,#164b35);">part decomposition of a system, starting with a </span><span style="color:var(--ds-text-accent-green-bolder,#164b35);">specified root part. </span><span style="color:var(--ds-text-accent-green-bolder,#164b35);">*/</span><br /><span style="color:var(--ds-text,#333333);">    }</span><br /><span style="color:var(--ds-text,#333333);">}</span></p></ac:rich-text-body></ac:structured-macro></li></ol><h4>Auto-creating viewpoint definition elements via the Extract Definition commands</h4><p><span>To auto-create viewpoint definition elements via the Extract Definition commands</span></p><hr /><ul><li><span><span style="color:var(--ds-text,#172b4d);">See the <ac:link><ri:page ri:content-title="Extract Definition and Usage" /></ac:link></span><span style="color:var(--ds-text,#172b4d);"> </span><span style="color:var(--ds-text,#172b4d);">page.</span></span></li></ul><h3>Specifying viewpoints</h3><h4>Framing concerns for viewpoints</h4><p>It is typical for a viewpoint definition to be structured as framing<strong> </strong>a set of stakeholder concerns regarding information about a modeled system or domain of interest. The viewpoint then models the requirement for the view in order to address the framed concerns.</p><ul><li>For procedures on concern creation, see the <ac:link ac:anchor="Creating concern usage and definition elements"><ri:page ri:content-title="Concerns" /><ac:plain-text-link-body><![CDATA[Creating concern usage and definition elements]]></ac:plain-text-link-body></ac:link> subsection on the <ac:link><ri:page ri:content-title="Concerns" /></ac:link> page.</li><li>You can frame concerns for viewpoints the same way as for requirements. For procedures on concern framing, see the <ac:link ac:anchor="Framing concerns"><ri:page ri:content-title="Concerns" /><ac:plain-text-link-body><![CDATA[Framing concerns]]></ac:plain-text-link-body></ac:link> subsection on the <ac:link><ri:page ri:content-title="Concerns" /></ac:link> page.</li></ul><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="3c2930d1-83ec-488d-82aa-0b478730b854"><ac:parameter ac:name="title">Textual notation example of a viewpoint definition with framed concern </ac:parameter><ac:rich-text-body><p><span style="color:var(--ds-text-accent-blue,#0055cc);">concern</span><span style="color:var(--ds-text,#333333);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">'system breakdown'</span><span style="color:var(--ds-text,#333333);"> {</span><br /><span style="color:var(--ds-text,#333333);">    </span><span style="color:var(--ds-text-accent-blue,#0055cc);">stakeholder</span><span style="color:var(--ds-text,#333333);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">se</span><span style="color:var(--ds-text,#333333);"> : </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">'Systems Engineer'</span><span style="color:var(--ds-text,#333333);">;</span><br /><span style="color:var(--ds-text,#333333);">    </span><span style="color:var(--ds-text-accent-blue,#0055cc);">stakeholder</span><span style="color:var(--ds-text,#333333);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">ivv</span><span style="color:var(--ds-text,#333333);"> : </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">'IV&amp;V'</span><span style="color:var(--ds-text,#333333);">;</span><br /><span style="color:var(--ds-text,#333333);">}</span><br /><br /><span style="color:var(--ds-text-accent-blue,#0055cc);">viewpoint</span><span style="color:var(--ds-text,#333333);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">def</span><span style="color:var(--ds-text,#333333);"> </span><span style="color:var(--ds-text-accent-teal,#206a83);">'System Structure Perspective'</span><span style="color:var(--ds-text,#333333);"> {</span><br /><span style="color:var(--ds-text,#333333);">    </span><span style="color:var(--ds-text-accent-blue,#0055cc);">frame</span><span style="color:var(--ds-text,#333333);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">'system breakdown'</span><span style="color:var(--ds-text,#333333);">;</span><br /><span style="color:var(--ds-text,#333333);">}</span></p></ac:rich-text-body></ac:structured-macro><h4>Specifying assumed and required constraints for viewpoints</h4><p>A viewpoint can be specified with assumed and required constraints.</p><ul><li>You can specify assumed and required constraints for viewpoints the same way as for requirements. For procedures on assumed and required constraints creation, see the <ac:link><ri:page ri:content-title="Requirement constraints" /></ac:link> page.</li></ul><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="214d4b95-a4b1-4bb0-9c09-0417af32d49c"><ac:parameter ac:name="title">Textual notation example of a viewpoint definition with a require constraint</ac:parameter><ac:rich-text-body><p><span style="color:var(--ds-text-accent-blue,#0055cc);">viewpoint</span><span style="color:var(--ds-text,#333333);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">def</span><span style="color:var(--ds-text,#333333);"> </span><span style="color:var(--ds-text-accent-teal,#206a83);">'System Structure Perspective'</span><span style="color:var(--ds-text,#333333);"> {</span><br /><span style="color:var(--ds-text,#333333);">    </span><span style="color:var(--ds-text-accent-blue,#0055cc);">require</span><span style="color:var(--ds-text,#333333);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">constraint</span><span style="color:var(--ds-text,#333333);"> {</span><br /><span style="color:var(--ds-text,#333333);">        </span><span style="color:var(--ds-text-accent-blue,#0055cc);">doc</span><br /><span style="color:var(--ds-text,#333333);">        </span><span style="color:var(--ds-text-accent-green-bolder,#164b35);">/* A system structure view shall show the hierarchical</span><br /><span style="color:var(--ds-text-accent-green-bolder,#164b35);">        * part decomposition of a system, starting with a</span><br /><span style="color:var(--ds-text-accent-green-bolder,#164b35);">        * specified root part.</span><br /><span style="color:var(--ds-text-accent-green-bolder,#164b35);">    */</span><br /><span style="color:var(--ds-text,#333333);">    }</span><br /><span style="color:var(--ds-text,#333333);">}</span></p></ac:rich-text-body></ac:structured-macro><h4>Satisfying viewpoints</h4><p>Since a viewpoint usage is a kind of requirement usage, a view usage can be declared to satisfy a viewpoint usage using a <ac:link><ri:page ri:content-title="Satisfy requirement" /><ac:plain-text-link-body><![CDATA[satisfy requirement usage]]></ac:plain-text-link-body></ac:link>. However, as a shortcut, any composite viewpoint usage nested in a view definition or usage is asserted to be satisfied by that view.</p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="7abec7b6-ecab-4a9d-93ca-516cfe9c97ed"><ac:parameter ac:name="title">Textual notation example of a viewpoint usage satisfied by a view definition</ac:parameter><ac:rich-text-body><p><span style="color:var(--ds-text-accent-blue,#0055cc);">view</span><span style="color:var(--ds-text,#333333);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">def</span><span style="color:var(--ds-text,#333333);"> </span><span style="color:var(--ds-text-accent-teal,#206a83);">'Part Structure View'</span><span style="color:var(--ds-text,#333333);"> {</span><br /><span style="color:var(--ds-text,#333333);">    </span><span style="color:var(--ds-text-accent-green-bolder,#164b35);">// This viewpoint is asserted to be satisfied by any</span><span style="color:var(--ds-text-accent-green-bolder,#164b35);"> instance of the view definition.</span><br /><span style="color:var(--ds-text,#333333);">    </span><span style="color:var(--ds-text-accent-blue,#0055cc);">viewpoint</span><span style="color:var(--ds-text,#333333);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">vp</span><span style="color:var(--ds-text,#333333);"> : </span><span style="color:var(--ds-text-accent-teal,#206a83);">'System Structure Perspective'</span><span style="color:var(--ds-text,#333333);">;</span><br /><span style="color:var(--ds-text,#333333);">    </span><span style="color:var(--ds-text-accent-green-bolder,#164b35);">//...</span><br /><span style="color:var(--ds-text,#333333);">}</span></p></ac:rich-text-body></ac:structured-macro><p>Alternatively, a satisfy requirement usage can be used explicitly between a viewpoint and a view. In particular, a satisfy requirement usage for a viewpoint that is nested in a view definition or usage will, by default, have the containing view as its satisfying feature.</p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="6829e3a4-c138-4cad-a4b0-64671b77c84a"><ac:parameter ac:name="title">Textual notation example of a viewpoint usage satisfied by a view usage</ac:parameter><ac:rich-text-body><p><span style="color:var(--ds-text-accent-blue,#0055cc);">viewpoint</span><span style="color:var(--ds-text,#333333);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">'vehicle structure perspective'</span><span style="color:var(--ds-text,#333333);"> : </span><span style="color:var(--ds-text-accent-teal,#206a83);">'System Structure Perspective'</span><span style="color:var(--ds-text,#333333);"> {</span><br /><span style="color:var(--ds-text,#333333);">    </span><span style="color:var(--ds-text-accent-blue,#0055cc);">subject</span><span style="color:var(--ds-text,#333333);"> : </span><span style="color:var(--ds-text-accent-teal,#206a83);">Vehicle</span><span style="color:var(--ds-text,#333333);">;</span><br /><span style="color:var(--ds-text,#333333);">}</span><br /><span style="color:var(--ds-text-accent-blue,#0055cc);">view</span><span style="color:var(--ds-text,#333333);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">'vehicle parts view'</span><span style="color:var(--ds-text,#333333);"> : </span><span style="color:var(--ds-text-accent-teal,#206a83);">'Part Structure View'</span><span style="color:var(--ds-text,#333333);"> {</span><br /><span style="color:var(--ds-text,#333333);">    </span><span style="color:var(--ds-text-accent-green-bolder,#164b35);">// This asserts that the given viewpoint 'vehicle structure perspective' is satisfied by the 'vehicle parts view'.</span><br /><span style="color:var(--ds-text,#333333);">    </span><span style="color:var(--ds-text-accent-blue,#0055cc);">satisfy</span><span style="color:var(--ds-text,#333333);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">'vehicle structure perspective'</span><span style="color:var(--ds-text,#333333);">;</span><br /><span style="color:var(--ds-text,#333333);">    </span><span style="color:var(--ds-text-accent-green-bolder,#164b35);">// ...</span><br /><span style="color:var(--ds-text,#333333);">}</span></p></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=249577679 space=SYSML2P version=2 -->
## PAGE 00749: Views

- page_id: `249577679`
- space_key: `SYSML2P`
- source_url: https://docs.nomagic.com/spaces/SYSML2P/pages/249577679/Views
- version_number: 2
- version_date: `2026-06-30T14:03:59.349+02:00`
- ancestors: SysML v2 Plugin Documentation > Model composition
- labels: []

### NORMALIZED CONTENT

A rendered view artifact (i.e., view) is a rendered view usage element that provides a specific view of the model. A view does not display the model in its entirety with all of the elements the model contains. It represents a particular set of model elements, encompassing a particular view of the model. As the Containment tree and the Textual Editor, views can be used as a tool for modeling. Creating, editing, or deleting elements via a view modifies the model itself. The changes are visible both in the Containment tree and the Textual Editor.

Creating a rendered view artifact (i.e., view) encompasses:

1. [CONFLUENCE_PAGE title='Creating views' space=''] element;
  1. Typically, a view usage is defined by a view definition that contains a renderer. View definitions may also contain filters and other customizations (e.g., [CONFLUENCE_PAGE title='Custom symbolic view definitions' space=''], [CONFLUENCE_PAGE title='Modeling tabular view columns' space='']) .
2. (Optional) Specifying what elements should be [CONFLUENCE_PAGE title='Exposing elements for views' space=''] by the view;
  1. Exposition must be specified for tabular views; it is optional for symbolic ones.
  2. Typically, exposition is specified for each view individually.
3. (Optional) [CONFLUENCE_PAGE title='Filtering elements for views' space=''] based on specified conditions;
  1. Typically, filters are specified for the view definition defining a view.
4. [CONFLUENCE_PAGE title='Rendering views' space=''] , so that the view and its exposed elements can be displayed in the specified rendering style.
  1. Typically, the renderer is specified for the view definition defining a view.

Once the view is created following the above-listed steps, you can [CONFLUENCE_PAGE title='Opening views' space=''] and [CONFLUENCE_PAGE title='Displaying elements in views' space='']

The subpages of this section contain procedures for all the listed steps.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>A rendered view artifact (i.e., view) is a rendered view usage element that provides a specific view of the model. A view <span style="color:var(--ds-text,#333333);">does not display the model in its entirety with all of the elements the model contains. It represents a particular set of model elements, encompassing a particular view of the model. As the Containment tree and the Textual Editor, views can be used as a tool for modeling. Creating, editing, or deleting elements via a view modifies the model itself. The changes are visible both in the Containment tree and the Textual Editor.</span></p><p>Creating a rendered view artifact (i.e., view) encompasses: </p><ol><li><ac:link><ri:page ri:content-title="Creating views" /><ac:plain-text-link-body><![CDATA[Creating a view usage]]></ac:plain-text-link-body></ac:link> element;<ol><li>Typically, a view usage is defined by a view definition that contains a renderer. View definitions may also contain filters and <span style="color:var(--ds-text,#172b4d);">other customizations (e.g., <ac:link><ri:page ri:content-title="Custom symbolic view definitions" /><ac:plain-text-link-body><![CDATA[specific symbolic view palettes]]></ac:plain-text-link-body></ac:link>, <ac:link><ri:page ri:content-title="Modeling tabular view columns" /><ac:plain-text-link-body><![CDATA[tabular view columns]]></ac:plain-text-link-body></ac:link>)</span>.</li></ol></li><li>(Optional) Specifying what elements should be <ac:link><ri:page ri:content-title="Exposing elements for views" /><ac:plain-text-link-body><![CDATA[exposed]]></ac:plain-text-link-body></ac:link> by the view;<ol><li>Exposition must be specified for tabular views; it is optional for symbolic ones. </li><li>Typically, exposition is specified for each view individually.</li></ol></li><li>(Optional) <ac:link><ri:page ri:content-title="Filtering elements for views" /><ac:plain-text-link-body><![CDATA[Filtering exposed elements]]></ac:plain-text-link-body></ac:link> based on specified conditions;<ol><li>Typically, filters are specified for the view definition defining a view.</li></ol></li><li><ac:link><ri:page ri:content-title="Rendering views" /><ac:plain-text-link-body><![CDATA[Rendering the view]]></ac:plain-text-link-body></ac:link>, so that the view and its exposed elements can be displayed in the specified rendering style.<ol><li>Typically, the renderer is specified for the view definition defining a view.</li></ol></li></ol><p>Once the view is created following the above-listed steps, you can <ac:link><ri:page ri:content-title="Opening views" /><ac:plain-text-link-body><![CDATA[open the view]]></ac:plain-text-link-body></ac:link> and <ac:link><ri:page ri:content-title="Displaying elements in views" /><ac:plain-text-link-body><![CDATA[display element symbols on it.]]></ac:plain-text-link-body></ac:link></p><p>The subpages of this section contain procedures for all the listed steps.</p><p><br /></p>
````

<!--NOMAGIC_PAGE id=249577770 space=SYSML2P version=4 -->
## PAGE 00750: Views basics

- page_id: `249577770`
- space_key: `SYSML2P`
- source_url: https://docs.nomagic.com/spaces/SYSML2P/pages/249577770/Views+basics
- version_number: 4
- version_date: `2025-09-30T14:54:42.540+02:00`
- ancestors: SysML v2 Plugin Documentation > Model composition > Views > Creating views
- labels: []

### NORMALIZED CONTENT

See the basic procedures for working with views and view definitions.

##### Creating view usage and definition elements

###### Creating view usage and definition elements via the Textual Editor

To create view usage and definition elements via the Textual Editor

1. In the Textual Editor, place the cursor where you want to create the element and declare the keyword:
  1. *view def*for a view definition.
  2. *view* for a view usage.
2. Specify the element name.
3. Specify the view's features in the element body.
4. Click the Synchronize button. viewdef'Part Structure View'{ // view definition 
privateimportViews::*; 
filter@SysML::Systems::SysML::PartUsage; 
renderasNewTreeDiagram; 
}view 'vehicle parts view' : 'Part Structure View'; // view usage

###### Creating view usage and definition elements via the Create Element command

To create view usage and definition elements via the Create Element command

1. In the Containment tree, right-click an element, and in the shortcut menu, click **Create Element**.
2. In the Create Element dialog, select one of the following:
  1. view def to create a view definition element.
  2. view to create a view usage element.
3. Name the element.
4. Specify the view's features.

###### Auto-creating view definition elements via the Extract Definition commands

To auto-create view definition elements via the Extract Definition commands

- See the [CONFLUENCE_PAGE title='Extract Definition and Usage' space='']page.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>See the basic procedures for working with views and view definitions.</p><h3>Creating view usage and definition elements</h3><h4>Creating view usage and definition elements via the Textual Editor</h4><p>To create view usage and definition elements via the Textual Editor</p><hr /><ol><li>In the Textual Editor, place the cursor where you want to create the element and declare the keyword: <ol><li><p class="auto-cursor-target"><span> </span><em>view def</em><span> </span>for a view definition.</p></li><li><span> <em>view</em></span><em><span> </span></em>for a view usage.</li></ol></li><li>Specify the element name.</li><li>Specify the view's features in the element body.</li><li>Click the <strong>Synchronize </strong>button.<br /><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="f1af8d45-8838-424f-8130-2fa40803394a"><ac:rich-text-body><p><span style="color:var(--ds-text-accent-blue,#0055cc);">view</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">def</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-teal,#206a83);">'Part Structure View'</span><span style="color:var(--ds-text,#000000);"> {  <span style="color:var(--ds-text-accent-green-bolder,#164b35);">// view definition </span></span><br /><span style="color:var(--ds-text,#000000);">    </span><span style="color:var(--ds-text-accent-blue,#0055cc);">private</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">import</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-teal,#206a83);">Views</span><span style="color:var(--ds-text,#000000);">::*;</span><br /><span style="color:var(--ds-text,#000000);">    </span><span style="color:var(--ds-text-accent-blue,#0055cc);">filter</span><span style="color:var(--ds-text,#000000);"> @<span style="color:var(--ds-text-accent-teal,#206a83);">SysML::Systems::SysML::PartUsage</span>;</span><br /><span style="color:var(--ds-text,#000000);">    </span><span style="color:var(--ds-text-accent-blue,#0055cc);">render</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">asNewTreeDiagram</span><span style="color:var(--ds-text,#000000);">;</span><br /><span style="color:var(--ds-text,#000000);">}</span></p><p><span style="color:var(--ds-text,#000000);"><span style="color:var(--ds-text-accent-blue,#0055cc);">view</span> <span style="color:var(--ds-text-accent-blue-bolder,#09326c);">'vehicle parts view'</span> : <span style="color:var(--ds-text-accent-teal,#206a83);">'Part Structure View';  <span style="color:var(--ds-text-accent-green-bolder,#164b35);">// view usage</span></span></span></p></ac:rich-text-body></ac:structured-macro></li></ol><h4>Creating view usage and definition elements via the Create Element command</h4><p>To create view usage and definition elements via the Create Element command</p><hr /><ol><li><p class="auto-cursor-target">In the Containment tree, right-click an element, and in the shortcut menu, click <strong>Create Element</strong>.</p></li><li>In the <strong>Create Element</strong> dialog, select one of the following:<ol><li><strong>view def</strong> to create a view definition element.</li><li><strong>view </strong>to create a view usage element.</li></ol></li><li>Name the element.</li><li>Specify the view's features.</li></ol><h4>Auto-creating view definition elements via the Extract Definition commands</h4><p><span>To auto-create view definition elements via the Extract Definition commands</span></p><hr /><ul><li><span><span style="color:var(--ds-text,#172b4d);">See the <ac:link><ri:page ri:content-title="Extract Definition and Usage" /></ac:link></span><span style="color:var(--ds-text,#172b4d);"> </span><span style="color:var(--ds-text,#172b4d);">page.</span></span></li></ul>
````

<!--NOMAGIC_PAGE id=249577210 space=SYSML2P version=2 -->
## PAGE 00751: Visibility

- page_id: `249577210`
- space_key: `SYSML2P`
- source_url: https://docs.nomagic.com/spaces/SYSML2P/pages/249577210/Visibility
- version_number: 2
- version_date: `2026-04-24T15:30:53.950+02:00`
- ancestors: SysML v2 Plugin Documentation > Element management > Working with elements
- labels: []

### NORMALIZED CONTENT

Declaring an element within the body of a namespace denotes that the element is an owned member of the namespace, i.e., there is an owning membership relationship between the namespace and the member element. The visibility of such membership can be specified using the following keywords:

- public (default) - membership is visible outside the namespace.
- private - membership is invisible from outside the namespace.
- protected - membership is invisible outside the namespace, except in inheritance, where it behaves like public.

Visibility must be specified for [CONFLUENCE_PAGE title='Importing and filtering elements' space=''].

##### Specifying element visibility

###### Specifying element visibility via the Textual Editor

To specify element visibility via the Textual Editor

1. In the Textual Editor, place the cursor before the element keyword and specify the needed visibility keyword: *public*, *private*, or *protected*.
2. Click the Synchronize button.

package'Vehicle Information'{ 
partvehicleSpecs;// public by default 
privatepartvehicleRecord;// private 
}

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>Declaring an element within the body of a namespace denotes that the element is an owned member of the namespace, i.e., there is an owning membership relationship between the namespace and the member element. The visibility of such membership can be specified using the following keywords:</p><ul><li><em>public</em><span> (default) - membership is visible outside the namespace.</span></li><li><em>private</em><span> </span>- membership is invisible from outside the namespace.</li><li><em>protected</em><span> </span>- membership is invisible outside the namespace, except in inheritance, where it behaves like public.</li></ul><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="d390f551-0ab3-4bb4-9555-a73503ae7f62"><ac:rich-text-body><p>Visibility must be specified for <ac:link><ri:page ri:content-title="Importing and filtering elements" /><ac:plain-text-link-body><![CDATA[element import]]></ac:plain-text-link-body></ac:link>.</p></ac:rich-text-body></ac:structured-macro><h3>Specifying element visibility</h3><h4>Specifying element visibility via the Textual Editor</h4><p>To specify element visibility via the Textual Editor</p><hr /><ol><li><span style="color:var(--ds-text,#172b4d);">In the Textual Editor, place the cursor before the element keyword and specify the needed visibility keyword: <em>public</em>, <em>private</em>, or <em>protected</em>.</span></li><li>Click the<span> </span><strong>Synchronize<span> </span></strong>button.</li></ol><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="c69e3e67-cf45-4c01-b7cc-4568c4a1c30a"><ac:rich-text-body><p><span style="color:var(--ds-text-accent-blue,#0055cc);">package</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-teal,#206a83);">'Vehicle Information'</span><span style="color:var(--ds-text,#000000);"> {</span><br /><span style="color:var(--ds-text,#000000);">    </span><span style="color:var(--ds-text-accent-blue,#0055cc);">part</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">vehicleSpecs</span><span style="color:var(--ds-text,#000000);">; </span><span style="color:var(--ds-text-accent-green-bolder,#164b35);">// public by default</span><br /><span style="color:var(--ds-text,#000000);">    </span><span style="color:var(--ds-text-accent-blue,#0055cc);">private</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">part</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">vehicleRecord</span><span style="color:var(--ds-text,#000000);">; </span><span style="color:var(--ds-text-accent-green-bolder,#164b35);">// private</span><br /><span style="color:var(--ds-text,#000000);">}</span></p></ac:rich-text-body></ac:structured-macro><p><br /></p>
````

<!--NOMAGIC_PAGE id=249577551 space=SYSML2P version=2 -->
## PAGE 00752: While and for loop actions

- page_id: `249577551`
- space_key: `SYSML2P`
- source_url: https://docs.nomagic.com/spaces/SYSML2P/pages/249577551/While+and+for+loop+actions
- version_number: 2
- version_date: `2025-09-19T15:36:12.391+02:00`
- ancestors: SysML v2 Plugin Documentation > Model composition > Behavior > Actions > Controlling actions > Structured control actions
- labels: []

### NORMALIZED CONTENT

There are two forms of loop action usages:

- A while loop action usage performs a body clause action usage iteratively, as long as its while expression continues to evaluate to true and its until expression continues to evaluate to false .
- A for loop action usage performs a body clause action usage iteratively, assigning a loop variable successively for each iteration to the values resulting from the evaluation of a sequence expression.

##### Specifying while loop actions for actions

###### Specifying while loop actions for actions via the Textual Editor

To specify while loop actions for actions via the Textual Editor

1. In the Textual Editor, place the cursor where you want to create the while loop action and do one of the following:
  1. For an unnamed while loop action usage, declare the keyword while .
  2. For a named while loop action usage, declare the keyword action , specify the element name, and then the keyword while . You can also use keywords *loop*or *while true*(interchangeably) and omit the while expression, allowing the action to loop until the until expression evaluates to *true*.
2. (Optional) Follow with the expression for the while action usage.
3. Specify the body clause by doing one of the following:
  1. For an unnamed body clause, follow with the body for the body clause.
  2. For a named body clause, declare the keyword action , specify the clause name, and follow with the body for the body clause.
4. (Optional) Specify the *until*keyword followed by a boolean-valued until expression.
5. Click the Synchronize button.

// ---------- while loop action usage

actionbatteryMonitor{

// unnamed while loop action usage with a while expression 'battery<100' and an unnamed body clause:whilebattery<100{ 
// named 'batteryCheck' while loop action usage with a while expression 'battery<100' and a named body clause 'actionchargeBattery':actionbatteryCheckwhilebattery<100actionchargeBattery{

actionAddCharge; 
}untilcharge>=100; 
}

// ---------- keywords 'loop' and 'while true' are equivalent and can be used interchangeably

actionbatteryMonitor{

// unnamed while loop action usagewithout a while expressionand an unnamed body clause:loop{ 
// named 'batteryCharge' while loop action usage without a while expression, witha named body clause 'actionchargeBattery':actionbatteryChargeloopactionchargeBattery {// unnamed while loop action usage with a while expression 'true' and an unnamed body clause: 
whiletrue{ 
// named 'batteryCharge'while loop action usage with a while expression 'true'anda named body clause 'actionchargeBattery':actionbatteryChargewhiletrueactionchargeBattery{

actionAddCharge; 
}untilcharge>=100; 
}

###### Specifying while loop actions for actions via the view palette

To specify while loop actions for actions via the view palette

1. In the view palette, under the Other Actions group, click the while button to create a while loop action usage element.
2. Click on an action symbol in the view pane where you want to create the while loop symbol.
3. (Optional) Specify the element via the Textual Editor.

##### Specifying for loop actions for actions

For a for loop action usage, the action declaration part is followed by the keyword *for*, which introduces a loop variable declaration****followed by the keyword *in*and a sequence expression, and, after that, a body clause.

###### Specifying for loop actions for actions via the Textual Editor

To specify for loop actions for actions via the Textual Editor

1. In the Textual Editor, place the cursor where you want to create the for loop action and do one of the following:
  1. For an unnamed for loop action usage, declare the keyword for .
  2. For a named for loop action usage, declare the keyword action , specify the element name, and then the keyword for .
2. Follow with the loop variable declaration for the for action usage.
3. Specify the keyword in and the sequence expression.
4. Specify the body clause by doing one of the following:
  1. For an unnamed body clause, follow with the body for the body clause.
  2. For a named body clause, declare the keyword action , specify the clause name, and follow with the body for the body clause.
5. Click the Synchronize button.

actionupdatePosition{

// unnamedfor loop action usage with a loop variable declaration 'power', sequence expression 'powerProfile' and an unnamed body clause:forpowerinpowerProfile{// named'dynamicScenario' for loop action usage with a loop variable declaration 'power', sequence expression 'powerProfile' and a named 'dynamicsStep' body clause:actiondynamicScenarioforpowerinpowerProfileactiondynamicsStep{ 
assignposition:=ComputeDynamics(position,power); 
} 
}

###### Specifying for loop actions for actions via the view palette

To specify for loop actions for actions via the view palette

1. In the view palette, under the Other Actions group, click the for button to create a for loop action usage element.
2. Click on an action symbol in the view pane where you want to create the for loop symbol.
3. (Optional) Specify the element via the Textual Editor.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>There are two forms of loop action usages:</p><ul><li>A <strong>while loop action usage </strong>performs a<strong> </strong>body clause action usage iteratively, as long as its while expression continues to evaluate to <em>true</em> and its until expression continues to evaluate to <em>false</em>.</li><li>A <strong>for loop action usage </strong>performs a body clause action usage iteratively, assigning a loop variable successively for each iteration to the values resulting from the evaluation of a sequence expression.</li></ul><h3>Specifying while loop actions for actions</h3><h4>Specifying while loop actions for actions via the Textual Editor</h4><p>To specify while loop actions for actions via the Textual Editor</p><hr /><ol><li><p class="auto-cursor-target" style="text-align: left;">In the Textual Editor, place the cursor where you want to create the while loop action and do one of the following:</p><ol><li>For an unnamed while loop action usage, declare the keyword <em>while</em>.</li><li>For a named while loop action usage, declare the keyword <em>action</em>, specify the element name, and then the keyword <em>while</em>.<br /><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="c88c0b86-662a-4ab4-8309-1d1e38e9f9f5"><ac:rich-text-body><p>You can also use keywords <em>loop </em>or <em>while true </em>(interchangeably) and omit the while expression, allowing the action to loop until the until expression evaluates to <em>true</em>.</p></ac:rich-text-body></ac:structured-macro></li></ol></li><li>(Optional) Follow with the expression for the while action usage.</li><li>Specify the body clause by doing one of the following:<ol><li>For an unnamed body clause, follow with the body for the body clause.</li><li>For a named body clause, declare the keyword <em>action</em>, specify the clause name, and follow with the body for the body clause.</li></ol></li><li><span style="color:var(--ds-text,#172b4d);">(Optional) Specify the <em>until </em>keyword followed by a boolean-valued until expression. </span></li><li><span style="color:var(--ds-text,#172b4d);">Click the </span><strong style="text-align: left;">Synchronize<span> </span></strong><span style="color:var(--ds-text,#172b4d);">button.</span></li></ol><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="7c636319-62bd-47f7-9d6f-20aeebcd883c"><ac:rich-text-body><p><span style="color:var(--ds-text-accent-green-bolder,#164b35);">// ---------- while loop action usage </span></p><p><span style="color:var(--ds-text-accent-blue,#0055cc);">action</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">batteryMonitor</span><span style="color:var(--ds-text,#000000);"> {</span></p><p><span style="color:var(--ds-text,#000000);"><span style="color:var(--ds-text-accent-green-bolder,#164b35);"><span style="color:var(--ds-text,#000000);">    </span>// unnamed while loop action usage with a while expression <span style="color:var(--ds-text-accent-green-bolder,#164b35);"><span style="color:var(--ds-text-accent-green-bolder,#164b35);">'<span style="color:var(--ds-text-accent-green-bolder,#164b35);"><span style="color:var(--ds-text-accent-green-bolder,#164b35);"><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">battery</span><span style="color:var(--ds-text,#000000);"> &lt; </span><span style="color:var(--ds-background-accent-green-bolder,#1f845a);">100</span></span></span>'</span></span> and an unnamed body clause:</span><br />    </span><span style="color:var(--ds-text-accent-blue,#0055cc);">while</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">battery</span><span style="color:var(--ds-text,#000000);"> &lt; </span><span style="color:var(--ds-background-accent-green-bolder,#1f845a);">100</span><span style="color:var(--ds-text,#000000);"> {<br /><span style="color:var(--ds-text-accent-green-bolder,#164b35);"><span style="color:var(--ds-text-accent-green-bolder,#164b35);"><span style="color:var(--ds-text,#000000);"><span style="color:var(--ds-text,#000000);">    </span></span>// named '<span style="color:var(--ds-text-accent-blue-bolder,#09326c);"><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">batteryCheck</span></span>' while loop action usage with a while expression '<span style="color:var(--ds-text-accent-green-bolder,#164b35);"><span style="color:var(--ds-text-accent-green-bolder,#164b35);"><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">battery</span><span style="color:var(--ds-text,#000000);"> &lt; </span><span style="color:var(--ds-background-accent-green-bolder,#1f845a);">100</span></span></span>' and a named body clause '<span style="color:var(--ds-text-accent-green-bolder,#164b35);"><span style="color:var(--ds-text-accent-green-bolder,#164b35);"><span style="color:var(--ds-text-accent-blue,#0055cc);">action</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">chargeBattery</span></span></span>':</span></span><span style="color:var(--ds-text-accent-green-bolder,#164b35);"><br /><span style="color:var(--ds-text,#000000);">    </span><span style="color:var(--ds-text-accent-blue,#0055cc);">action</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">batteryCheck</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">while</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">battery</span><span style="color:var(--ds-text,#000000);"> &lt; </span><span style="color:var(--ds-background-accent-green-bolder,#1f845a);">100</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">action</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">chargeBattery</span><span style="color:var(--ds-text,#000000);"> {</span></span></span></p><p><span style="color:var(--ds-text,#000000);">        </span><span style="color:var(--ds-text-accent-blue,#0055cc);">action</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">AddCharge</span><span style="color:var(--ds-text,#000000);">;</span><br /><span style="color:var(--ds-text,#000000);">    } </span><span style="color:var(--ds-text-accent-blue,#0055cc);">until</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">charge</span><span style="color:var(--ds-text,#000000);"> &gt;= </span><span style="color:var(--ds-background-accent-green-bolder,#1f845a);">100</span><span style="color:var(--ds-text,#000000);">;</span><br /><span style="color:var(--ds-text,#000000);">}</span></p><p><span style="color:var(--ds-text-accent-green-bolder,#164b35);">// ---------- keywords 'loop' and 'while true' are equivalent and can be used interchangeably</span></p><p><span style="color:var(--ds-text-accent-blue,#0055cc);">action</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">batteryMonitor</span><span style="color:var(--ds-text,#000000);"> {</span></p><p><span style="color:var(--ds-text,#000000);"><span style="color:var(--ds-text-accent-green-bolder,#164b35);"><span style="color:var(--ds-text,#000000);">    </span>// unnamed while loop action usage<span style="color:var(--ds-text-accent-green-bolder,#164b35);"><span style="color:var(--ds-text-accent-green-bolder,#164b35);"> without a while expression<span style="color:var(--ds-text-accent-green-bolder,#164b35);"><span style="color:var(--ds-text-accent-green-bolder,#164b35);"> and an unnamed <span style="color:var(--ds-text-accent-green-bolder,#164b35);"><span style="color:var(--ds-text-accent-green-bolder,#164b35);">body clause:</span></span></span></span></span></span></span><br />    </span><span style="color:var(--ds-text-accent-blue,#0055cc);">loop</span><span style="color:var(--ds-text,#000000);"> {<br /><span style="color:var(--ds-text-accent-green-bolder,#164b35);"><span style="color:var(--ds-text-accent-green-bolder,#164b35);"><span style="color:var(--ds-text,#000000);">    </span>// named '<span style="color:var(--ds-text-accent-blue-bolder,#09326c);"><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">batteryCharge</span></span>' while loop action usage without a while expression, with<span style="color:var(--ds-text-accent-green-bolder,#164b35);"><span style="color:var(--ds-text-accent-green-bolder,#164b35);"> a named body clause '<span style="color:var(--ds-text-accent-green-bolder,#164b35);"><span style="color:var(--ds-text-accent-green-bolder,#164b35);"><span style="color:var(--ds-text-accent-blue,#0055cc);">action</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">chargeBattery</span></span></span>':</span></span></span></span><span style="color:var(--ds-text-accent-green-bolder,#164b35);"><br /><span style="color:var(--ds-text-accent-blue,#0055cc);"><span style="color:var(--ds-text,#000000);">    <span style="color:var(--ds-text-accent-green-bolder,#164b35);"><span style="color:var(--ds-text-accent-blue,#0055cc);">action</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">batteryCharge</span><span style="color:var(--ds-text,#000000);"> </span></span></span>loop</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">action</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">chargeBattery {<span style="color:var(--ds-text,#000000);"><br /><span style="color:var(--ds-text-accent-green-bolder,#164b35);"><span style="color:var(--ds-text-accent-green-bolder,#164b35);"><span style="color:var(--ds-text,#000000);"><span style="color:var(--ds-text,#000000);">    </span></span>// unnamed while loop action usage with <span style="color:var(--ds-text-accent-green-bolder,#164b35);"><span style="color:var(--ds-text-accent-green-bolder,#164b35);">a while expression '<span style="color:var(--ds-text-accent-blue,#0055cc);"><span style="color:var(--ds-text-accent-blue,#0055cc);">true</span></span>' and an unnamed <span style="color:var(--ds-text-accent-green-bolder,#164b35);"><span style="color:var(--ds-text-accent-green-bolder,#164b35);">body clause:</span></span></span></span></span></span></span><br /><span style="color:var(--ds-text-accent-blue,#0055cc);"><span style="color:var(--ds-text,#000000);">    </span>while</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">true</span><span style="color:var(--ds-text,#000000);"> {<br /><span style="color:var(--ds-text-accent-green-bolder,#164b35);"><span style="color:var(--ds-text-accent-green-bolder,#164b35);"><span style="color:var(--ds-text,#000000);"><span style="color:var(--ds-text,#000000);">    </span></span>// named <span style="color:var(--ds-text-accent-green-bolder,#164b35);"><span style="color:var(--ds-text-accent-green-bolder,#164b35);">'<span style="color:var(--ds-text-accent-blue-bolder,#09326c);"><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">batteryCharge</span></span>' </span></span>while loop action usage <span style="color:var(--ds-text-accent-green-bolder,#164b35);"><span style="color:var(--ds-text-accent-green-bolder,#164b35);">with <span style="color:var(--ds-text-accent-green-bolder,#164b35);"><span style="color:var(--ds-text-accent-green-bolder,#164b35);">a while expression '<span style="color:var(--ds-text-accent-blue,#0055cc);"><span style="color:var(--ds-text-accent-blue,#0055cc);">true</span></span>' </span></span></span></span><span style="color:var(--ds-text-accent-green-bolder,#164b35);"><span style="color:var(--ds-text-accent-green-bolder,#164b35);">and<span style="color:var(--ds-text-accent-green-bolder,#164b35);"><span style="color:var(--ds-text-accent-green-bolder,#164b35);"> a named body clause '<span style="color:var(--ds-text-accent-green-bolder,#164b35);"><span style="color:var(--ds-text-accent-green-bolder,#164b35);"><span style="color:var(--ds-text-accent-blue,#0055cc);">action</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">chargeBattery</span></span></span>':</span></span></span></span></span></span></span><br /></span></span></span><span style="color:var(--ds-text-accent-blue,#0055cc);"><span style="color:var(--ds-text,#000000);">    <span style="color:var(--ds-text-accent-green-bolder,#164b35);"><span style="color:var(--ds-text-accent-blue,#0055cc);">action</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">batteryCharge</span><span style="color:var(--ds-text,#000000);"> </span></span></span>while</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">true</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">action</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">chargeBattery</span><span style="color:var(--ds-text,#000000);"> {</span></p><p><span style="color:var(--ds-text,#000000);">        </span><span style="color:var(--ds-text-accent-blue,#0055cc);">action</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">AddCharge</span><span style="color:var(--ds-text,#000000);">;</span><br /><span style="color:var(--ds-text,#000000);">    } </span><span style="color:var(--ds-text-accent-blue,#0055cc);">until</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">charge</span><span style="color:var(--ds-text,#000000);"> &gt;= </span><span style="color:var(--ds-background-accent-green-bolder,#1f845a);">100</span><span style="color:var(--ds-text,#000000);">;</span><br /><span style="color:var(--ds-text,#000000);">}</span></p></ac:rich-text-body></ac:structured-macro><h4>Specifying while loop actions for actions via the view palette</h4><p>To specify while loop actions for actions via the view palette</p><hr /><ol><li>In the view palette, under the Other Actions group, click the <strong>while </strong>button to create a while loop action usage element.</li><li>Click on an action symbol in the view pane where you want to create the while loop symbol.</li><li>(Optional)<span> </span>Specify the element via the Textual Editor.</li></ol><h3>Specifying for loop actions for actions</h3><p>For a for loop action usage, the action declaration part is followed by the keyword <em>for</em>, which introduces a loop variable declaration<strong> </strong>followed by the keyword <em>in </em>and a sequence expression, and, after that, a body clause. </p><h4>Specifying for loop actions for actions via the Textual Editor</h4><p>To specify for loop actions for actions via the Textual Editor</p><hr /><ol><li><p class="auto-cursor-target" style="text-align: left;">In the Textual Editor, place the cursor where you want to create the for loop action and do one of the following:</p><ol><li>For an unnamed for loop action usage, declare the keyword <em>for</em>.</li><li>For a named for loop action usage, declare the keyword <em>action</em>, specify the element name, and then the keyword <em>for</em>.</li></ol></li><li>Follow with the loop variable declaration for the for action usage.</li><li>Specify the keyword <em>in</em> and the sequence expression.</li><li>Specify the body clause by doing one of the following:<ol><li>For an unnamed body clause, follow with the body for the body clause.</li><li>For a named body clause, declare the keyword <em>action</em>, specify the clause name, and follow with the body for the body clause.</li></ol></li><li><span style="color:var(--ds-text,#172b4d);">Click the </span><strong style="text-align: left;">Synchronize<span> </span></strong><span style="color:var(--ds-text,#172b4d);">button.</span></li></ol><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="eca08f03-dd70-4bb0-99e9-1751c6bf1cf4"><ac:rich-text-body><p><span style="color:var(--ds-text-accent-blue,#0055cc);">action</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">updatePosition</span><span style="color:var(--ds-text,#000000);"> {</span></p><p><span style="color:var(--ds-text-accent-green-bolder,#164b35);"><span style="color:var(--ds-text,#000000);">    </span>// unnamed<span style="color:var(--ds-text-accent-green-bolder,#164b35);"><span style="color:var(--ds-text-accent-green-bolder,#164b35);"> for loop action usage with a loop variable declaration '<span style="color:var(--ds-text-accent-blue-bolder,#09326c);">power</span>', sequence expression '<span style="color:var(--ds-text-accent-blue-bolder,#09326c);">powerProfile</span>' and an unnamed body clause:</span></span><br /></span><span style="color:var(--ds-text,#000000);">    </span><span style="color:var(--ds-text-accent-blue,#0055cc);">for</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">power</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">in</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">powerProfile</span><span style="color:var(--ds-text,#000000);"> {<br /></span><span style="color:var(--ds-text-accent-green-bolder,#164b35);"><span style="color:var(--ds-text,#000000);">    </span>// named<span style="color:var(--ds-text-accent-green-bolder,#164b35);"><span style="color:var(--ds-text-accent-green-bolder,#164b35);"> '<span style="color:var(--ds-text-accent-blue-bolder,#09326c);">dynamicScenario</span>' for loop action usage with a loop variable declaration '<span style="color:var(--ds-text-accent-blue-bolder,#09326c);">power</span>', sequence expression '<span style="color:var(--ds-text-accent-blue-bolder,#09326c);">powerProfile</span>' and a named '<span style="color:var(--ds-text-accent-blue-bolder,#09326c);">dynamicsStep</span>' body clause:<br /></span></span></span><span style="color:var(--ds-text,#000000);">    </span><span style="color:var(--ds-text-accent-blue,#0055cc);">action</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">dynamicScenario</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">for</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">power</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">in</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">powerProfile</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">action</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">dynamicsStep</span><span style="color:var(--ds-text,#000000);"> {</span><br /><span style="color:var(--ds-text,#000000);">        </span><span style="color:var(--ds-text-accent-blue,#0055cc);">assign</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">position</span><span style="color:var(--ds-text,#000000);"> := </span><span style="color:var(--ds-text-accent-teal,#206a83);">ComputeDynamics</span><span style="color:var(--ds-text,#000000);">(</span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">position</span><span style="color:var(--ds-text,#000000);">, </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">power</span><span style="color:var(--ds-text,#000000);">);</span><br /><span style="color:var(--ds-text,#000000);">    }</span><br /><span style="color:var(--ds-text,#000000);">}</span></p></ac:rich-text-body></ac:structured-macro><h4>Specifying for loop actions for actions via the view palette</h4><p>To specify for loop actions for actions via the view palette</p><hr /><ol><li>In the view palette, under the Other Actions group, click the <strong>for </strong>button to create a for loop action usage element.</li><li>Click on an action symbol in the view pane where you want to create the for loop symbol.</li><li>(Optional)<span> </span>Specify the element via the Textual Editor.</li></ol>
````

<!--NOMAGIC_PAGE id=249576863 space=SYSML2P version=4 -->
## PAGE 00753: Working with Containment tree

- page_id: `249576863`
- space_key: `SYSML2P`
- source_url: https://docs.nomagic.com/spaces/SYSML2P/pages/249576863/Working+with+Containment+tree
- version_number: 4
- version_date: `2025-09-19T15:13:52.535+02:00`
- ancestors: SysML v2 Plugin Documentation > Model management
- labels: []

### NORMALIZED CONTENT

The Containment tree provides a visual representation of the hierarchy of your model elements. It is displayed in the Containment tab, which groups model elements into logical sets, displaying their hierarchy as a Containment tree. It allows you to manage your model data, including root namespaces, packages, elements, and other data.

[IMAGE alt='' src='']

##### The Containment Tab toolbar

The Containment Tab toolbar contains the following commands.

| Command icon | Command name | Description |
| --- | --- | --- |
|  | Collapse All | Collapses all expanded elements to display only the global and root namespaces, as well as libraries. |
|  | Collapse Selected Recursively | Collapses all expanded elements of the selected element. |
|  | Quick Find | Allows you to search for elements by their name. See the page. |
|  | Options | Displays a dropdown menu with available options:Show Essential Elements Only>]]>Show Implied RelationshipsThis option controls the display of implied relationships in the Containment tree. Enabling it shows relationships between model elements that are automatically created by the modeling tool based on the model's structure and semantics, even though they are not explicitly defined by the user. The option is disabled by default.Attempting to display an element hidden by any of the options displays a question dialog in the modeling tool, allowing you to enable/disable the needed option. |

##### The Essential Elements Only modeThe Essential Elements Only mode

The Essential Elements Only mode allows you to control the level of model detail displayed in the Containment tree of a specific project:

- Enabled (default). Displays the model containing only the model's essential elements that are the most relevant to your modeling process. It also displays elements with their essential representation names instead of full element names.
- Disabled. Displays all model elements, including those that may be less relevant to your modeling process (Memberships (e.g., OwningMembership, FeatureMembership), Specializations (e.g., Subsetting, Redefinition, FeatureTyping), multiplicity, etc.). Elements are displayed with their full element names.

The following UI components use simplified essential representation names, omitting feature modifiers (except direction), specializations, and values, regardless of the Essential Elements Only mode:

- Element shortcut menu
- Select/create input/output submenu
- [CONFLUENCE_PAGE title='Element navigation' space=''] submenu
- [CONFLUENCE_PAGE title='Specification panel' space='']
- [CONFLUENCE_PAGE title='Specification window' space='']

###### Switching the Essential Elements Only mode

To switch the Essential Elements Only mode

1. In the Containment tab, click the **Options** button in the top right corner.
2. In the dropdown menu, click the **Show Essential Elements Only** option.

[IMAGE alt='' src='']

##### Selecting elements in the Containment tree

You can easily select the needed elements in the Contrainment tree from the Textual Editor, symbol in a view, or the Specification Panel.

To select elements in the Containment tree

- In the Textual Editor, do one of the following:
  - Place the cursor on the element and press Alt+B.
  - Right-click an element and in the shortcut menu, click **Select in Containment Tree** .
- In a view, do one of the following:
  - Select an element and press Alt+B.
  - Right-click an element and in the shortcut menu, click **Select in Containment Tree** .
  - Select an element and in the view toolbar, click the **Select in Containment Tree**button.
- In the Specification Panel, click the **Select in Containment Tree**button in the Navigation bar.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><span style="color:var(--ds-text,#333333);"><span style="color:var(--ds-text,#333333);">The Containment tree provides a visual representation of the hierarchy of your model elements. It is displayed in the Containment tab, which groups model elements into logical sets, displaying their hierarchy as a Containment tree. It allows you to manage your model data, including root namespaces, packages, elements, and other data. </span></span></p><p><span style="color:var(--ds-text,#333333);"><ac:image ac:align="center"><ri:attachment ri:filename="Containment_Tab.png" /></ac:image><br /></span></p><h3>The Containment Tab toolbar</h3><p><span style="color:var(--ds-text,#333333);">The Containment Tab toolbar contains the following commands.</span></p><table class="wrapped"><colgroup><col /><col /><col /></colgroup><tbody><tr><th scope="col">Command icon</th><th scope="col">Command name</th><th scope="col">Description</th></tr><tr><td><div class="content-wrapper"><p><ac:image><ri:attachment ri:filename="Collapse All.png" /></ac:image></p></div></td><td>Collapse All</td><td>Collapses all expanded elements to display only the global and root namespaces, as well as libraries.</td></tr><tr><td><div class="content-wrapper"><p><ac:image><ri:attachment ri:filename="Collapse Selected Recursively.png" /></ac:image></p></div></td><td>Collapse Selected Recursively</td><td>Collapses all expanded elements of the selected element.</td></tr><tr><td><div class="content-wrapper"><p><ac:image><ri:attachment ri:filename="quick_find_button.png" /></ac:image></p></div></td><td>Quick Find</td><td>Allows you to search for elements by their name. See the <ac:link><ri:page ri:content-title="Quick find" /></ac:link> page.</td></tr><tr><td><div class="content-wrapper"><p><ac:image><ri:attachment ri:filename="Options.png" /></ac:image></p></div></td><td>Options</td><td><div class="content-wrapper"><p>Displays a dropdown menu with available options:</p><ul><li><strong>Show Essential Elements Only</strong><ul><li><ac:link ac:anchor="The Essential Elements Only mode"><ac:plain-text-link-body><![CDATA[Learn more >>]]></ac:plain-text-link-body></ac:link></li></ul></li><li><strong>Show Implied Relationships</strong><ul><li>This option controls the display of implied relationships in the Containment tree. Enabling it shows relationships between model elements that are automatically created by the modeling tool based on the model's structure and semantics, even though they are not explicitly defined by the user. The option is disabled by default.</li></ul></li></ul><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="1f2893b7-4392-43ae-8991-582bc15d7a4a"><ac:rich-text-body><p>Attempting to display an element hidden by any of the options displays a question dialog in the modeling tool, allowing you to enable/disable the needed option. </p></ac:rich-text-body></ac:structured-macro></div></td></tr></tbody></table><h3><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="ea7c6677-11f1-4017-8cc5-4c14c91c09a3"><ac:parameter ac:name="">The Essential Elements Only mode</ac:parameter></ac:structured-macro>The Essential Elements Only mode</h3><p><span style="color:var(--ds-text,#333333);">The Essential Elements Only mode allows you to control the level of model detail displayed in the Containment tree of a specific project:</span></p><ul><li><span style="color:var(--ds-text,#333333);">Enabled (default). Displays the model containing only the model's essential elements that are the most relevant to your modeling process. It also displays elements with their essential representation names instead of full element names.</span></li><li><span style="color:var(--ds-text,#333333);">Disabled. Displays all model elements, including those that may be less relevant to your modeling process <span style="color:var(--ds-text,#333333);">(</span><span style="color:var(--ds-text,#172b4d);">Memberships (e.g., OwningMembership, FeatureMembership), Specializations (e.g., Subsetting, Redefinition, FeatureTyping), multiplicity, etc.</span><span style="color:var(--ds-text,#333333);">)</span>. Elements are displayed with their full element names.</span></li></ul><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="3ce0aace-ae0f-477b-a071-e78627fe017a"><ac:rich-text-body><p>The following UI components use simplified essential representation names, omitting feature modifiers (except direction), specializations, and values, regardless of the Essential Elements Only mode:</p><ul style="text-align: left;"><li>Element shortcut menu</li><li>Select/create input/output submenu</li><li><ac:link><ri:page ri:content-title="Element navigation" /><ac:plain-text-link-body><![CDATA[Go To]]></ac:plain-text-link-body></ac:link> submenu</li><li><ac:link><ri:page ri:content-title="Specification panel" /></ac:link></li><li><ac:link><ri:page ri:content-title="Specification window" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro><h4>Switching the Essential Elements Only mode</h4><p><span style="color:var(--ds-text,#333333);">To switch the Essential Elements Only mode</span></p><hr /><ol><li><span style="color:var(--ds-text,#333333);">In the <span style="color:var(--ds-text,#333333);">Containment tab</span>, click the <strong>Options</strong> button in the top right corner.</span></li><li><span style="color:var(--ds-text,#333333);">In the dropdown menu, click the <strong>Show Essential Elements Only</strong> option.</span></li></ol><p><ac:image ac:align="center"><ri:attachment ri:filename="Essential_Elements_Only_mode.png" /></ac:image></p><p><br /></p><h3>Selecting elements in the Containment tree</h3><p>You can easily select the needed elements in the Contrainment tree from the Textual Editor, symbol in a view, or the Specification Panel.</p><p>To select elements in the Containment tree</p><hr /><ul style="text-align: left;"><li data-uuid="2138ac58-e1a3-44b4-81fc-5f8794d9e979">In the Textual Editor, do one of the following:<ul style="text-align: left;"><li data-uuid="9c574b33-b979-49b1-95f0-2e9c74e9abfd">Place the cursor on the element and press Alt+B.</li><li data-uuid="eb20e73f-aad6-4e4e-a756-7b4f259656be">Right-click an element and in the shortcut menu, click<span> <strong>Select in Containment Tree</strong></span>.</li></ul></li><li data-uuid="53e9ca0c-d095-4e50-8894-e02f862e3d9d">In a view, do one of the following:<ul style="text-align: left;"><li data-uuid="376fb1e0-b72a-4568-821c-3dfb11ac637b">Select an element and press Alt+B.</li><li data-uuid="c93f601c-1877-4df3-a552-3b79fcc9aad6">Right-click an element and in the shortcut menu, click<span> <strong>Select in Containment Tree</strong></span>.</li><li data-uuid="e7db57d2-544d-4a5b-9ec8-9216cd24a2f6">Select an element and in the view toolbar, click the <span><strong>Select in Containment Tree </strong>button.</span></li></ul></li><li data-uuid="6c51c70b-81c9-449c-ab52-53dde4bf7d93"><span>In the Specification Panel, click the <span><strong>Select in Containment Tree </strong>button in the Navigation bar.</span></span></li></ul>
````

<!--NOMAGIC_PAGE id=249577164 space=SYSML2P version=2 -->
## PAGE 00754: Working with elements

- page_id: `249577164`
- space_key: `SYSML2P`
- source_url: https://docs.nomagic.com/spaces/SYSML2P/pages/249577164/Working+with+elements
- version_number: 2
- version_date: `2025-09-19T15:20:40.971+02:00`
- ancestors: SysML v2 Plugin Documentation > Element management
- labels: []

### NORMALIZED CONTENT

This section contains information for working with elements.

For a comprehensive list of SysML v2 elements and procedures for working with them, see the [CONFLUENCE_PAGE title='Model composition' space=''] section.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>This section contains information for working with elements.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="be5c24a2-85f7-4642-84ab-c2023ab6ffa7"><ac:rich-text-body><p>For <span style="color:var(--ds-text,#333333);">a comprehensive list of SysML v2 elements and procedures for working with them, see the <ac:link><ri:page ri:content-title="Model composition" /></ac:link> section. </span></p></ac:rich-text-body></ac:structured-macro><p><br /></p>
````

<!--NOMAGIC_PAGE id=249576768 space=SYSML2P version=2 -->
## PAGE 00755: Working with projects

- page_id: `249576768`
- space_key: `SYSML2P`
- source_url: https://docs.nomagic.com/spaces/SYSML2P/pages/249576768/Working+with+projects
- version_number: 2
- version_date: `2025-09-19T15:09:47.601+02:00`
- ancestors: SysML v2 Plugin Documentation > Project management
- labels: []

### NORMALIZED CONTENT

This section contains information regarding project management.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>This section contains information regarding project management.</p>
````

<!--NOMAGIC_PAGE id=249577059 space=SYSML2P version=2 -->
## PAGE 00756: Working with symbols

- page_id: `249577059`
- space_key: `SYSML2P`
- source_url: https://docs.nomagic.com/spaces/SYSML2P/pages/249577059/Working+with+symbols
- version_number: 2
- version_date: `2025-09-19T15:16:29.735+02:00`
- ancestors: SysML v2 Plugin Documentation > Model management > Working with views
- labels: []

### NORMALIZED CONTENT

Symbolic views allow you to display elements as symbols, including shapes and paths. See the pages in this section for symbol-specific procedures and related information.

For information regarding symbol styles, see the [CONFLUENCE_PAGE title='Symbol styles' space=''] section.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><span style="color:var(--ds-text,#172b4d);">Symbolic views allow you to display elements as symbols, including shapes and paths. See the pages in this section for symbol-specific procedures and related information.</span></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="abbb375e-dd0d-49fa-afdc-0f7eba0c0b5a"><ac:rich-text-body><p>For information regarding symbol styles, see the <ac:link><ri:page ri:content-title="Symbol styles" /></ac:link> section. </p></ac:rich-text-body></ac:structured-macro><p><br /></p>
````

<!--NOMAGIC_PAGE id=249576875 space=SYSML2P version=14 -->
## PAGE 00757: Working with Textual Editor

- page_id: `249576875`
- space_key: `SYSML2P`
- source_url: https://docs.nomagic.com/spaces/SYSML2P/pages/249576875/Working+with+Textual+Editor
- version_number: 14
- version_date: `2026-04-16T08:17:52.922+02:00`
- ancestors: SysML v2 Plugin Documentation > Model management
- labels: []

### NORMALIZED CONTENT

The SysML v2 Textual Editor is akin to a code editor allowing you to view and create your model using textual notation in a code-like format.Any model changes made in a view or the Containment tree are reflected in the textual notation and vice versa. You can simply develop your model using textual notation and then easily display the created elements in a view using the [CONFLUENCE_PAGE title='Displaying elements in symbolic views' space=''].The Textual Editor tab is comprised of the Textual Editor pane, minimap, sticky header, and theeditor toolbar.

For SysML v2 Textual Editor-related environment options, see the [CONFLUENCE_PAGE title='Environment options' space=''] page.

###### [IMAGE alt='' src=''] 
The Textual Editor tab is comprised of the Textual Editor pane, sticky header, minimap, and Textual Editor toolbar.

##### Textual Editor areas

###### The Textual Editor pane

The Textual Editor pane is where you write the textual notation.

**The Textual Editor pane details:**

- The Textual Editor pane displays the model of a specific root namespace as textual notation.
- Selecting an element in the Containment tree highlights its associated textual notation in the Textual Editor.
- The left side of the pane displays line numbers for easier navigation.
- Each element has a display ID next to the element keyword once the textual notation is saved. Unsaved elements do not have IDs. [IMAGE alt='' src='']If you want to copy the textual notation and paste it into the Textual Editor with the display IDs, use the Cut (Ctrl+X) command instead of Copy (Ctrl+C). The display IDs are discarded when pasting the notation anywhere outside the editor, regardless of whether Copy or Cut was performed.
- The Textual Editor provides syntax highlighting.

###### Minimap

The minimap allows you to scroll the textual notation more quickly. It is located on the right side of the Textual Editor as the vertical section displaying the entirety of the textual notation.

To use the minimap

1. Hover over the minimap, then click the grey rectangle representing the visible part of the text.
2. Move it up or down to quickly navigate the textual notation.

You can enable or disable the minimap via the **Enable Minimap** [CONFLUENCE_PAGE title='Environment options' space=''].

###### Sticky header

The sticky header is displayed at the top of the Textual Editor pane, which displays the owner of the currently visible notation at the top of the editor. You can control the sticky header with the following environment options:

- **Enable Sticky Header**. The option allows you to enable or disable the sticky header.
- **Sticky Header Line Count**. The option allows you to specify the maximum number of lines to display in the sticky header.

For more information, see the [CONFLUENCE_PAGE title='Environment options' space=''] page.

###### Textual Editor toolbar

| Button | Shortcut keys | Description |
| --- | --- | --- |
| Back | Alt+Left Arrow | Click to navigate to the previously opened view. Permanently disabled. |
| Forward | Alt+Right Arrow | Click to navigate to the previously opened view. Permanently disabled. |
| Synchronize Model with Textual Notation | Alt+S | Click to synchronize the model with the changes made in the Textual Editor. |
| Select in Containment Tree | Alt+B | Click to select the element associated with the cursor position in the Containment tree. The button is disabled if the model is not synchronized. |
| Enable Editing / Disable Editing | - | Click to disable or enable editing in the Textual Editor. The button is disabled if the model is not synchronized. |

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p style="text-align: left;"><span style="color:var(--ds-text,#333333);"><span style="color:var(--ds-text,#333333);">The SysML v2 Textual Editor is akin to a code editor allowing you to view and create your model using textual notation in a code-like format. </span></span><span style="color:var(--ds-text,#333333);">Any model changes made in a view or the Containment tree are reflected in the textual notation and vice versa. <span style="color:var(--ds-text,#333333);">You can simply develop your model using textual notation and then easily display the created elements in a view using the <ac:link><ri:page ri:content-title="Displaying elements in symbolic views" /></ac:link>. </span></span><span style="letter-spacing: 0.0px;color:var(--ds-text,#333333);">The Textual Editor tab is comprised of the Textual Editor pane, <span style="color:var(--ds-text,#333333);">minimap, sticky header, and the </span>editor toolbar. </span><span style="letter-spacing: 0.0px;color:var(--ds-text,#333333);"> </span></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="d46203b2-e0ed-492e-a688-bf954ea2c4e0"><ac:rich-text-body><p>For SysML v2 Textual Editor-related environment options, see the <ac:link><ri:page ri:content-title="Environment options" /></ac:link> page.</p></ac:rich-text-body></ac:structured-macro><h6 style="text-align: center;"><ac:image><ri:attachment ri:filename="textual_editor_example.png" /></ac:image><br /><span style="color:var(--ds-text,#333333);">The Textual Editor tab is comprised of the Textual Editor pane, sticky header, minimap, and  Textual Editor toolbar. </span></h6><h3>Textual Editor areas</h3><h4>The Textual Editor pane</h4><p><span style="color:var(--ds-text,#333333);">The Textual Editor pane is where you write the textual notation. </span></p><p><strong><span style="color:var(--ds-text,#333333);">The Textual Editor pane details:</span></strong></p><ul><li><span style="color:var(--ds-text,#333333);"><span style="color:var(--ds-text,#172b4d);">The Textual Editor pane displays the model of a specific root namespace as textual notation. </span></span></li><li data-uuid="8804f931-4fe2-487b-afaf-96c1180f7c2f"><span style="color:var(--ds-text,#333333);"><span style="color:var(--ds-text,#172b4d);">Selecting an element in the Containment tree highlights its associated textual notation in the Textual Editor.</span></span></li><li><span style="color:var(--ds-text,#333333);">The left side of the pane displays line numbers for easier navigation. </span></li><li><span style="color:var(--ds-text,#333333);">Each element has a display ID next to the element keyword once the textual notation is saved. Unsaved elements do not have IDs.</span><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="642d8e21-4e29-40ca-82ea-4c2e305715c3"><ac:rich-text-body><p class="auto-cursor-target"><ac:image><ri:attachment ri:filename="element_IDs_in_textual_notation.png" /></ac:image></p><p>If you want to copy the textual notation and paste it into the Textual Editor with the display IDs, use the Cut (Ctrl+X) command instead of Copy (Ctrl+C). The display IDs are discarded when pasting the notation anywhere outside the editor, regardless of whether Copy or Cut was performed.</p></ac:rich-text-body></ac:structured-macro></li><li data-uuid="a56a475b-6a37-439f-bb5c-60b46c13293f"><span style="color:var(--ds-text,#333333);">The Textual Editor provides syntax highlighting.</span></li></ul><h4>Minimap</h4><p>The minimap allows you to scroll the textual notation more quickly. It is located on the right side of the Textual Editor as the vertical section displaying the entirety of the textual notation.</p><p>To use the minimap</p><hr /><ol><li>Hover over the minimap, then click the grey rectangle representing the visible part of the text.</li><li>Move it up or down to quickly navigate the textual notation. </li></ol><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="26491a5c-2042-456b-b953-219a9f6bb1d3"><ac:rich-text-body><p>You can enable or disable the minimap via the <strong>Enable Minimap</strong> <ac:link><ri:page ri:content-title="Environment options" /><ac:plain-text-link-body><![CDATA[environment option]]></ac:plain-text-link-body></ac:link>. </p></ac:rich-text-body></ac:structured-macro><h4>Sticky header</h4><p>The sticky header is displayed at the top of the Textual Editor pane, <span style="color:var(--ds-text,#172b4d);">which displays the owner of the currently visible notation at the top of the editor. You can control the sticky header with the following environment options:</span></p><ul><li data-uuid="69202d74-f874-4c49-8317-34d367964276"><span style="color:var(--ds-text,#172b4d);"><strong>Enable Sticky Header</strong>. The option allows you to enable or disable the sticky header.</span></li><li data-uuid="8240fd64-794b-4250-b377-86f57a30e3dd"><span style="color:var(--ds-text,#172b4d);"><strong>Sticky Header Line Count</strong>. The option allows you to specify the maximum number of lines to display in the sticky header. </span></li></ul><p><span style="color:var(--ds-text,#172b4d);">For more information, see the <ac:link><ri:page ri:content-title="Environment options" /></ac:link> page.</span></p><h4>Textual Editor toolbar</h4><table class="relative-table wrapped" style="width: 90.8838%;"><colgroup> <col style="width: 26.5427%;" /> <col style="width: 11.3208%;" /> <col style="width: 62.1088%;" /> </colgroup><tbody><tr><th scope="col">Button</th><th scope="col">Shortcut keys</th><th scope="col">Description</th></tr><tr><td><div class="content-wrapper"><p><ac:image><ri:attachment ri:filename="back_diagram_toolbar.png" /></ac:image> <span style="color:var(--ds-text,#333333);">Back</span></p></div></td><td style="text-align: left;">Alt+Left Arrow</td><td style="text-align: left;"><p>Click to navigate to the previously opened <span style="color:var(--ds-text,#333333);">view</span>. Permanently disabled.</p></td></tr><tr><td><div class="content-wrapper"><p><ac:image><ri:attachment ri:filename="forward_diagram_toolbar.png" /></ac:image> <span style="color:var(--ds-text,#333333);">Forward</span></p></div></td><td style="text-align: left;"><p>Alt+Right Arrow</p></td><td style="text-align: left;"><p>Click to navigate to the previously opened <span style="color:var(--ds-text,#333333);">view</span>. Permanently disabled.</p></td></tr><tr><td><div class="content-wrapper"><p><ac:image><ri:attachment ri:filename="sync_button.png" /></ac:image> Synchronize Model with Textual Notation</p></div></td><td>Alt+S</td><td>Click to synchronize the model with the changes made in the Textual Editor.</td></tr><tr><td style="vertical-align: top;"><div class="content-wrapper"><p><ac:image><ri:attachment ri:filename="select_in_containment_tree_button.png" /></ac:image> <span style="color:var(--ds-text,#333333);">Select in Containment Tree</span></p></div></td><td>Alt+B</td><td><div class="content-wrapper"><p>Click to select the element associated with the cursor position in the Containment tree. The button is disabled if the model is not synchronized.</p></div></td></tr><tr><td><div class="content-wrapper"><p><ac:image><ri:attachment ri:filename="read_only_button.png" /></ac:image> Enable Editing / Disable Editing</p></div></td><td>-</td><td><div class="content-wrapper"><p class="auto-cursor-target"><ac:inline-comment-marker ac:ref="779a0da7-56ff-4359-b165-b6314133ffa3">Click to disable</ac:inline-comment-marker> or enable editing in the Textual Editor. The button is disabled if the model is not synchronized.</p></div></td></tr></tbody></table><p class="auto-cursor-target"><br /></p>
````

<!--NOMAGIC_PAGE id=249576960 space=SYSML2P version=8 -->
## PAGE 00758: Working with views

- page_id: `249576960`
- space_key: `SYSML2P`
- source_url: https://docs.nomagic.com/spaces/SYSML2P/pages/249576960/Working+with+views
- version_number: 8
- version_date: `2026-05-06T18:28:59.037+02:00`
- ancestors: SysML v2 Plugin Documentation > Model management
- labels: []

### NORMALIZED CONTENT

A rendered view artifact is a rendered view usage element that provides a specific view of the model in its diagrammatic representation. A view does not display the model in its entirety with all of the elements the model contains. It represents a particular set of model elements, encompassing a particular view of the model. As the Containment tree and the Textual Editor, views can be used as a tool for modeling. Creating, editing, or deleting elements via a view modifies the model itself. The changes are visible both in the Containment tree and the Textual Editor.

See the subpages in the [CONFLUENCE_PAGE title='Views' space=''] section to learn about modeling views and symbol styles.

###### [IMAGE alt='' src=''] 
The image displays a standard predefined symbolicGeneric View and a standard predefined tabular Generic Table view.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>A rendered view artifact is a rendered view usage element that provides a specific view of the model in its diagrammatic representation. A view <span style="color:var(--ds-text,#333333);">does not display the model in its entirety with all of the elements the model contains. It represents a particular set of model elements, encompassing a particular view of the model. As the Containment tree and the Textual Editor, views can be used as a tool for modeling. Creating, editing, or deleting elements via a view modifies the model itself. The changes are visible both in the Containment tree and the Textual Editor.</span></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="e4be5f0f-1d2a-4887-8d43-c2ea14bd43be"><ac:rich-text-body><p>See the subpages in the <ac:link><ri:page ri:content-title="Views" /></ac:link> section to learn about modeling views and symbol styles.</p></ac:rich-text-body></ac:structured-macro><h6 style="text-align: center;"><span style="color:var(--ds-text,#333333);"><ac:image><ri:attachment ri:filename="views.png" /></ac:image><br />The image displays a standard predefined symbolic </span>Generic View and a standard predefined tabular Generic Table view. </h6>
````
