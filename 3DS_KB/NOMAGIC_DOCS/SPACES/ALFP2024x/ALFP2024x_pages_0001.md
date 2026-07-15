# NOMAGIC DOCUMENTATION SPACE: Alf Plugin 2024x

<!--NOMAGIC_SPACE key=ALFP2024x chunk=1 -->

<!--NOMAGIC_PAGE id=137986071 space=ALFP2024x version=9 -->
## PAGE 00001: 2024x Version News

- page_id: `137986071`
- space_key: `ALFP2024x`
- source_url: https://docs.nomagic.com/spaces/ALFP2024x/pages/137986071/2024x+Version+News
- version_number: 9
- version_date: `2023-10-10T07:54:22.124+02:00`
- ancestors: Alf Plugin Documentation
- labels: []

### NORMALIZED CONTENT

1287705923

INLINE

1287705943

INLINE

1287705933

INLINE

###### Alf Plugin

Released on: November 10, 2024

1287705922

INLINE

In the 2024x version, Alf can now be utilized as a scripting language to write simple expressions (for example, using dot notation) without the need for compilation. These scripts can be employed in Opaque Actions, Opaque Behaviors, Opaque Expressions, State Machine Guards, and even directly in the Simulation Console. [CONFLUENCE_PAGE title='Alf as scripting language' space='']>>]]>

[IMAGE alt='' src='']

###### Simple Alf scripts used in State Machine diagram

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="e4ee35ae-ed28-415b-8adf-087a1233d052"><ac:parameter ac:name="id">1287705923</ac:parameter><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="cc9b8e1a-a7cf-4175-af73-5f24cc98c42e"><ac:parameter ac:name="id">1287705943</ac:parameter><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="ebeb43f7-0008-4e5e-8989-0344dbef18d5"><ac:parameter ac:name="id">1287705933</ac:parameter><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><h5 style="text-align: center;">Alf Plugin</h5><p style="text-align: center;">Released on: November 10, 2024</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="698eabe6-bc9f-4541-afdd-68d59ae7d2ac"><ac:parameter ac:name="id">1287705922</ac:parameter><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><p>In the 2024x version, Alf can now be utilized as a scripting language to write simple expressions (for example, using dot notation) without the need for compilation. These scripts can be employed in Opaque Actions, Opaque Behaviors, Opaque Expressions, State Machine Guards, and even directly in the Simulation Console. <ac:link><ri:page ri:content-title="Alf as scripting language" /><ac:plain-text-link-body><![CDATA[Learn more >>>]]></ac:plain-text-link-body></ac:link></p><p><ac:image ac:align="center" ac:border="true" ac:height="319" ac:width="539"><ri:attachment ri:filename="State machine.PNG" /></ac:image></p><h6 style="text-align: center;"><span style="color: rgb(128,128,128);">Simple Alf scripts used in State Machine diagram</span></h6></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p>
````

<!--NOMAGIC_PAGE id=137986159 space=ALFP2024x version=1 -->
## PAGE 00002: Accessing context features without using "this"

- page_id: `137986159`
- space_key: `ALFP2024x`
- source_url: https://docs.nomagic.com/spaces/ALFP2024x/pages/137986159/Accessing+context+features+without+using+this
- version_number: 1
- version_date: `2023-09-22T11:48:51.301+02:00`
- ancestors: Alf Plugin Documentation > User Guide > Working with Alf
- labels: []

### NORMALIZED CONTENT

Like Java and JavaScript, Alf uses the keyword *this* to denote the current instance of the context Class in which the *this* expression occurs. Unlike Java and JavaScript, however, the Alf specification requires that *this* be used explicitly in order to access features (Properties, Operations and Receptions) of the context Class. For example,*this* is used extensively in the activity diagram shown below to access context Properties and to invoke the *getCurrentTemp* Operation.

[IMAGE alt='' src='']

###### Accessing context features using *this.*

The Alf Plugin implements an extension to the Alf language that allows context features to be accessed by name without explicitly using a *this* prefix. This is similar to what is allowed in Java and JavaScript. For example, the meaning of the Alf code in the above example remains the same if all the *this* expressions are dropped, as shown below.

[IMAGE alt='' src='']

###### Accessing context features without using *this.*

#### NOTE: Note

Note

Unlike Java and JavaScript, Alf allows new local names to be defined without an explicit declaration. This can result in the masking of errors if the name of a context attribute is misspelled on the left-hand side of an assignment statement. For instance, if the assignment in the action on the lower left in the activity above were changed to*Fcntrol = Fmin;*(with "*Fcontrol"*misspelled to*"Fcntrol*"), this would*not*be reported as an error. Rather, the assignment would simply define a new local name*Fcntrol*within the Opaque Action, which would be assigned*Fmin*as its initial value, with no effect on*Fcontrol.*

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>Like Java and JavaScript, Alf uses the keyword <em>this</em> to denote the current instance of the context Class in which the <em>this</em> expression occurs. Unlike Java and JavaScript, however, the Alf specification requires that <em>this</em> be used explicitly in order to access features (Properties, Operations and Receptions) of the context Class. For example,<em> this</em> is used extensively in the activity diagram shown below to access context Properties and to invoke the <em>getCurrentTemp</em> Operation.</p><p><ac:image ac:align="center"><ri:attachment ri:filename="Accessing_Context_Features_Without_This-Activity_With_This.png"><ri:page ri:space-key="ALFP2024x" ri:content-title="Accessing context features without using &quot;this&quot;" /></ri:attachment></ac:image></p><h6 style="text-align: center;">Accessing context features using <em>this.</em></h6><p>The Alf Plugin implements an extension to the Alf language that allows context features to be accessed by name without explicitly using a <em>this</em> prefix. This is similar to what is allowed in Java and JavaScript. For example, the meaning of the Alf code in the above example remains the same if all the <em>this</em> expressions are dropped, as shown below.</p><p><ac:image ac:align="center"><ri:attachment ri:filename="Accessing_Context_Features_Without_This-Activity_Without_This.png"><ri:page ri:space-key="ALFP2024x" ri:content-title="Accessing context features without using &quot;this&quot;" /></ri:attachment></ac:image></p><h6 style="text-align: center;">Accessing context features without using <em>this.</em></h6><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="5d7c914a-eca5-4ae8-97ba-fac3249cc86f"><ac:parameter ac:name="title">Note</ac:parameter><ac:rich-text-body><p><span><span>Unlike Java and JavaScript, Alf allows new local names to be defined without an explicit declaration. This can result in the masking of errors if the name of a context attribute is misspelled on the left-hand side of an assignment statement. For instance, if the assignment in the action on the lower left in the activity above were changed to </span><em>Fcntrol = Fmin;</em><span> (with &quot;</span><em>Fcontrol&quot;</em><span> misspelled to </span><em>&quot;Fcntrol</em><span>&quot;), this would </span><em>not</em><span> be reported as an error. Rather, the assignment would simply define a new local name </span><em>Fcntrol</em><span> within the Opaque Action, which would be assigned </span><em>Fmin</em><span> as its initial value, with no effect on </span><em>Fcontrol.</em><br /></span></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p>
````

<!--NOMAGIC_PAGE id=137986165 space=ALFP2024x version=1 -->
## PAGE 00003: Accessing current simulation time

- page_id: `137986165`
- space_key: `ALFP2024x`
- source_url: https://docs.nomagic.com/spaces/ALFP2024x/pages/137986165/Accessing+current+simulation+time
- version_number: 1
- version_date: `2023-09-22T11:48:51.774+02:00`
- ancestors: Alf Plugin Documentation > User Guide > Working with Alf > Helper functions
- labels: []

### NORMALIZED CONTENT

Simulation time is a timestamp that is retrieved from a simulation clock. The *GetCurrentTime* function returns the current simulation time of execution:

```text

```

The *timeUnit* argument is optional. If it is provided, then the time value is returned in the named units. Otherwise, the time value is returned in the time unit given by the current simulation configuration.

```text

```

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p>Simulation time is a timestamp that is retrieved from a simulation clock. The <em>GetCurrentTime</em> function returns the current simulation time of execution:</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="92a783e2-38fa-4949-8ef3-4a871a07be7d"><ac:parameter ac:name="language">text</ac:parameter><ac:plain-text-body><![CDATA[GetCurrentTime(in timeUnit: String[0..1]): Real[1]]]></ac:plain-text-body></ac:structured-macro><p><br /></p><p>The <em>timeUnit</em> argument is optional. If it is provided, then the time value is returned in the named units. Otherwise, the time value is returned in the time unit given by the current simulation configuration.</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="0491714d-caca-4c58-be6e-b5045e9f243b"><ac:parameter ac:name="language">text</ac:parameter><ac:plain-text-body><![CDATA[t = GetCurrentTime();			// Get current time in configured units (milliseconds by default).
t = GetCurrentTime("second");	// Get current time in units of seconds.]]></ac:plain-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=137986154 space=ALFP2024x version=1 -->
## PAGE 00004: Accessing data in Activity Edge guards

- page_id: `137986154`
- space_key: `ALFP2024x`
- source_url: https://docs.nomagic.com/spaces/ALFP2024x/pages/137986154/Accessing+data+in+Activity+Edge+guards
- version_number: 1
- version_date: `2023-09-22T11:48:51.014+02:00`
- ancestors: Alf Plugin Documentation > User Guide > Working with Alf > Using Alf in Activity models > Using Alf for Activity Edge guards
- labels: []

### NORMALIZED CONTENT

When an Alf expression is used to specify a guard on an Activity Edge, the guard condition may be based on two source of data:

1. If the Activity containing the Activity Edge has a context Classifier, then the values of the attributes of that Classifier can be accessed.
2. If the Activity Edge is outgoing from a Decision Node, then the *decision input value* for the Decision Node may also be used, if it has one. If a Decision Node has a single incoming Object Flow, then the value on this Object Flow becomes the decision input value for the Decision Node. Alternatively, the decision input flow may be designated explicitly by setting the **decision input flow** property of the Decision Node. If a Decision Node has a single incoming Control Flow (with no **decision input flow**or **decision input**Behavior), then it has no decision input value.

To access context Classifier attributes in Alf:

- Use Alf this expressions, such as this.Tcontrol.

Consider the *Fan* Class shown in the image below. This Class is supposed to control the speed of a fan between given maximum and minimum values, in order to keep a control temperature between maximum and minimum values.

[ATTACHMENT filename='Accessing_Data_In_Activity_Edge_Guards-Fan.png'][IMAGE alt='' src='']

###### A simple Fan control class

The Activity Diagram below shows the classifier behavior of this Class. The first Action in this Activity calls the *getCurrentTemp* operation and sets the *Tcontrol* attribute to the value returned from that call. The value of the *Tcontrol* attribute is then used to determine which branch is taken coming out of the Decision Node. Since all the Activity Edges are Control Flows, the Decision Node has no decision input value.

[IMAGE alt='' src='']

###### Accessing attribute data in guards

To access the decision input value of a Decision Node in Alf:

- Use the name of the Object Node (typically an Activity Parameter Node or Output Pin) that is the source of the decision input flow. OR
- Give the decision input flow a name and use that.

Unless the attribute *Tcontrol* is used elsewhere, its only purpose in the Activity shown in the previous example is to pass the current temperature value from the operation call to the guards. In this case, a simpler way to provide this value to the guards is to make it the decision input value for the Decision Node. In the revised Activity shown below, the result of the operation call is now provided on an Output Pin of the first Action called *Tcurrent* (via the shortcut for [CONFLUENCE_PAGE title='Using Alf expressions in Opaque Actions' space='ALFP2024x']). This Output Pin is then connected to the Decision Node by an Object Flow, so the value on the Output Pin becomes the decision input value for the Decision Node. This value can then be accessed in the guard expressions using the name of the Output Pin.

It is important that the type of an Output Pin used in this way be set properly, so that the guard expressions type check correctly. In this case the Output Pin has been given the type *Integer**,* which is consistent with the return type of *getCurrentTemp* and the types of the *Tmin* and *Tmax* attributes to which *Tcurrent* it will be compared. Note that, while the type of the *Tcurrent* Output Pin is shown in the diagram below, the types of Pins are not usually shown by default.

[IMAGE alt='' src='']

###### Accessing the decision input value in guards

In general, when a Decision Node has a decision input value, the Alf compiler will use the name of the nearest named Object Node providing that value. Most commonly, this will be an Activity Parameter Node or Output Pin, as in the example above. However, if the compiler cannot determine a single relevant name, or if you simply do not want the decision input value name to depend on the name of other Activity Nodes, you can, instead, name the Object Flow that provides the decision input value into the Decision Node. If the incoming decision input flow (whether determined implicitly or explicitly) has a name, then the Alf compiler will use this as the name for the decision input value. For example, in the further revised diagram below, the Object Flow has been given the name *T,* which is now the name used for the decision input value in the guards, rather than the Output Pin name *Tcurrent.*

**

*[IMAGE alt='' src='']*

###### Accessing the decision input value using the Object Flow name

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p>When an Alf expression is used to specify a guard on an Activity Edge, the guard condition may be based on two source of data:</p><ol><li>If the Activity containing the Activity Edge has a context Classifier, then the values of the attributes of that Classifier can be accessed.</li><li><p class="auto-cursor-target">If the Activity Edge is outgoing from a Decision Node, then the <em>decision input value</em> for the Decision Node may also be used, if it has one.</p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="f912ab7c-5468-45ea-aef7-eff9653b5490"><ac:rich-text-body><p>If a Decision Node has a single incoming Object Flow, then the value on this Object Flow becomes the decision input value for the Decision Node. Alternatively, the decision input flow may be designated explicitly by setting the <strong>decision input flow</strong> property of the Decision Node. If a Decision Node has a single incoming Control Flow (with no <strong>decision input flow </strong>or <strong>decision input </strong>Behavior), then it has no decision input value.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></li></ol><p><br /></p><p>To access context Classifier attributes in Alf:</p><hr /><ul><li>Use Alf <em>this</em> expressions, such as <em>this.Tcontrol.</em></li></ul><p><br /></p><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="e6ef98a3-e397-4d88-9292-fefcbea372c6"><ac:rich-text-body><p>Consider the <em>Fan</em> Class shown in the image below. This Class is supposed to control the speed of a fan between given maximum and minimum values, in order to keep a control temperature between maximum and minimum values.</p><p><br /></p><p style="text-align: center;"><ac:link><ri:attachment ri:filename="Accessing_Data_In_Activity_Edge_Guards-Fan.png"><ri:page ri:space-key="ALFP2024x" ri:content-title="Accessing data in Activity Edge guards" /></ri:attachment><ac:link-body><ac:image ac:thumbnail="true" ac:height="170"><ri:attachment ri:filename="Accessing_Data_In_Activity_Edge_Guards-Fan.png"><ri:page ri:space-key="ALFP2024x" ri:content-title="Accessing data in Activity Edge guards" /></ri:attachment></ac:image></ac:link-body></ac:link></p><h6 style="text-align: center;">A simple Fan control class</h6><p>The Activity Diagram below shows the classifier behavior of this Class. The first Action in this Activity calls the <em>getCurrentTemp</em> operation and sets the <em>Tcontrol</em> attribute to the value returned from that call. The value of the <em>Tcontrol</em> attribute is then used to determine which branch is taken coming out of the Decision Node. Since all the Activity Edges are Control Flows, the Decision Node has no decision input value.</p><p><br /></p><p><ac:image ac:align="center"><ri:attachment ri:filename="Accessing_Data_In_Activity_Edge_Guards-Control_Fan_1.png"><ri:page ri:space-key="ALFP2024x" ri:content-title="Accessing data in Activity Edge guards" /></ri:attachment></ac:image></p><h6 style="text-align: center;">Accessing attribute data in guards</h6></ac:rich-text-body></ac:structured-macro><p><br /></p><p>To access the decision input value of a Decision Node in Alf:</p><hr /><ul><li>Use the name of the Object Node (typically an Activity Parameter Node or Output Pin) that is the source of the decision input flow. <br /><br />OR<br /><br /></li><li>Give the decision input flow a name and use that.</li></ul><p><br /></p><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="5a8072b5-47cf-4041-8776-9db41e03418c"><ac:rich-text-body><p>Unless the attribute <em>Tcontrol</em> is used elsewhere, its only purpose in the Activity shown in the previous example is to pass the current temperature value from the operation call to the guards. In this case, a simpler way to provide this value to the guards is to make it the decision input value for the Decision Node. In the revised Activity shown below, the result of the operation call is now provided on an Output Pin of the first Action called <em>Tcurrent</em> (via the shortcut for <ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="Using Alf expressions in Opaque Actions" /><ac:plain-text-link-body><![CDATA[using Alf expressions in Opaque Actions]]></ac:plain-text-link-body></ac:link>). This Output Pin is then connected to the Decision Node by an Object Flow, so the value on the Output Pin becomes the decision input value for the Decision Node. This value can then be accessed in the guard expressions using the name of the Output Pin.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="c54dc91c-37d9-49c1-acc3-b03631cfb752"><ac:rich-text-body><p>It is important that the type of an Output Pin used in this way be set properly, so that the guard expressions type check correctly. In this case the Output Pin has been given the type <em>Integer</em><em>,</em> which is consistent with the return type of <em>getCurrentTemp</em> and the types of the <em>Tmin</em> and <em>Tmax</em> attributes to which <em>Tcurrent</em> it will be compared. Note that, while the type of the <em>Tcurrent</em> Output Pin is shown in the diagram below, the types of Pins are not usually shown by default.</p></ac:rich-text-body></ac:structured-macro><p><br /></p><p><ac:image ac:align="center"><ri:attachment ri:filename="Accessing_Data_In_Activity_Edge_Guards-Control_Fan_2.png"><ri:page ri:space-key="ALFP2024x" ri:content-title="Accessing data in Activity Edge guards" /></ri:attachment></ac:image></p><h6 style="text-align: center;">Accessing the decision input value in guards</h6><p>In general, when a Decision Node has a decision input value, the Alf compiler will use the name of the nearest named Object Node providing that value. Most commonly, this will be an Activity Parameter Node or Output Pin, as in the example above. However, if the compiler cannot determine a single relevant name, or if you simply do not want the decision input value name to depend on the name of other Activity Nodes, you can, instead, name the Object Flow that provides the decision input value into the Decision Node. If the incoming decision input flow (whether determined implicitly or explicitly) has a name, then the Alf compiler will use this as the name for the decision input value. For example, in the further revised diagram below, the Object Flow has been given the name <em>T,</em> which is now the name used for the decision input value in the guards, rather than the Output Pin name <em>Tcurrent.</em></p><p><em><br /></em></p><p><em><ac:image ac:align="center"><ri:attachment ri:filename="Accessing_Data_In_Activity_Edge_Guards-Control_Fan_3.png"><ri:page ri:space-key="ALFP2024x" ri:content-title="Accessing data in Activity Edge guards" /></ri:attachment></ac:image></em></p><h6 style="text-align: center;">Accessing the decision input value using the Object Flow name</h6></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell><ac:layout-cell><p> </p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="two_equal"><ac:layout-cell><p><br /></p></ac:layout-cell><ac:layout-cell><p> </p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=137986132 space=ALFP2024x version=2 -->
## PAGE 00005: Accessing Event data

- page_id: `137986132`
- space_key: `ALFP2024x`
- source_url: https://docs.nomagic.com/spaces/ALFP2024x/pages/137986132/Accessing+Event+data
- version_number: 2
- version_date: `2023-10-02T07:34:18.406+02:00`
- ancestors: Alf Plugin Documentation > User Guide > Working with Alf > Using Alf in State Machine models
- labels: []

### NORMALIZED CONTENT

Transitions on State Machines are triggered by Events. Events may have associated data and, for certain kinds of Events, this data may be accessed within the Alf code used within the State Machine. Specifically:

- For a Signal Event, the values of the attributes of the received Signal instance are the Event data.
- For a Call Event, the values of the Parameters of the called Operation are the Event data.

This event data may be accessed within guard Expressions and effect Behaviors on Transitions and within entry, do-activity and exit Behaviors on States*.* For entry and do-activity Behaviors, the relevant Events are those on the *incoming* Transitions of a State, but, for an exit Behavior, the relevant Events are on the *outgoing* Transitions of the State.

To access Signal Event data in Alf

- Use the special Parameter name *evt*, which has the Signal being received as its type. Use the usual dot notation to access Signal attributes. Signal Properties Visibility needs to be set to **public**to access them with evt Parameter.

Consider an e-commerce application that allows customers to place items in a shopping cart and then check out and pay for them. The *CheckOut* Event can be modeled using a Signal with relevant customer information, as shown below.

[IMAGE alt='' src='']

###### CheckOut Signal

The StateMachine diagram snippet below shows a Transition triggered by the *CheckOut* Signal, targeting a State with an entry Behavior to handle the Signal Event by initializing a new order for the customer.

[IMAGE alt='' src='']

###### Handling the CheckOut Signal Event

The Behavior above first checks if there is an existing customer with the given email and, if not, creates a new customer record using the *CheckOut* data. An alternative approach would be to using different Signals for checking out a new customer and checking out an existing customer, as shown below.

[IMAGE alt='' src='']

###### CheckOutNew and CheckOutExisting Signals

In this case, the *Establishing Customer* State will have two incoming Transitions, one for each Signal. By first checking which kind of Signal was actually received, the Alf code for the entry Behavior can then access the appropriate Event data in order to either create a new customer record or link to an existing customer, as shown below. Note that, because both Signals are specializations of the general Signal *CheckOutCustomer,* it is possible to access the common *shoppingCart* attribute without having to check which Signal was received.

[IMAGE alt='' src='']

###### Handling multiple Signal Events

To access Call Event data in Alf

- Use the names of the Parameters of the Operation to access their values. Output values for *out* and inout Parameters may be set using assignment, and those values are returned at the end of the run-to-completion step for the Call Event. Output Parameters are available in entry and exit Behaviors, but *not* in do-activity Behaviors, since do-activity Behaviors can continue to run asynchronously after the end of the run-to-completion step.

An alternative model would be to give the Order class that owns this StateMachine a *checkOut* Operation, with the StateMachine then handling a call to this Operation using a Call Event, as shown below. The entry Behavior in this case does the same thing as in the case above using a Signal Event, but note that the Parameters of the *checkOut* Operation are now used directly, instead of the property-access notation used for Signal Event data.

[IMAGE alt='' src='']

###### Handling the checkOut Call Event

Unlike Signal Events, access to Call Event data is only allowed if all relevant Transitions for a State Behavior (incoming for entry and do-activity, outgoing for exit) have Call Events for the same Operation. It is also not possible to access the Event data if Signal Events and Call Events are mixed, or are mixed with other kinds of Events (such as Time Events and Change Events).

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p><br /></p><p>Transitions on State Machines are triggered by Events. Events may have associated data and, for certain kinds of Events, this data may be accessed within the Alf code used within the State Machine. Specifically:</p><ul><li>For a Signal Event, the values of the attributes of the received Signal instance are the Event data.</li><li>For a Call Event, the values of the Parameters of the called Operation are the Event data.</li></ul><p>This event data may be accessed within guard Expressions and effect Behaviors on Transitions and within entry, do-activity and exit Behaviors on States<em>.</em> For entry and do-activity Behaviors, the relevant Events are those on the <em>incoming</em> Transitions of a State, but, for an exit Behavior, the relevant Events are on the <em>outgoing</em> Transitions of the State.</p><p><br /></p><p>To access Signal Event data in Alf</p><hr /><ul><li><p class="auto-cursor-target">Use the special Parameter name <em>evt</em>, which has the Signal being received as its type. Use the usual dot notation to access Signal attributes.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="7f2bd8be-95f5-435e-9e5e-5b59408a9369"><ac:rich-text-body><p><span style="color: rgb(23,43,77);">Signal Properties Visibility needs to be set to <strong>public </strong>to access them with evt Parameter.</span></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></li></ul><p><br /></p><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="40e39c0e-34ca-4359-84db-58ee802c1126"><ac:rich-text-body><p>Consider an e-commerce application that allows customers to place items in a shopping cart and then check out and pay for them. The <em>CheckOut</em> Event can be modeled using a Signal with relevant customer information, as shown below.</p><p><br /></p><p style="text-align: center;"><ac:image ac:thumbnail="true" ac:height="150"><ri:attachment ri:filename="Acessing_Event_Data-CheckOut_Signal.png" /></ac:image></p><h6 style="text-align: center;">CheckOut Signal</h6><p style="text-align: left;">The StateMachine diagram snippet below shows a Transition triggered by the <em>CheckOut</em> Signal, targeting a State with an entry Behavior to handle the Signal Event by initializing a new order for the customer.</p><p><br /></p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="Acessing_Event_Data-Handling_CheckOut_Signal_Event.png" /></ac:image></p><h6 style="text-align: center;">Handling the CheckOut Signal Event</h6><p>The Behavior above first checks if there is an existing customer with the given email and, if not, creates a new customer record using the <em>CheckOut</em> data. An alternative approach would be to using different Signals for checking out a new customer and checking out an existing customer, as shown below.</p><p><br /></p><p style="text-align: center;"><ac:image ac:width="500"><ri:attachment ri:filename="Acessing_Event_Data-CheckOutNew_CheckOutExisting_Signals.png" /></ac:image></p><h6 style="text-align: center;">CheckOutNew and CheckOutExisting Signals</h6><p>In this case, the <em>Establishing Customer</em> State will have two incoming Transitions, one for each Signal. By first checking which kind of Signal was actually received, the Alf code for the entry Behavior can then access the appropriate Event data in order to either create a new customer record or link to an existing customer, as shown below. Note that, because both Signals are specializations of the general Signal <em>CheckOutCustomer,</em> it is possible to access the common <em>shoppingCart</em> attribute without having to check which Signal was received.</p><p><br /></p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="Acessing_Event_Data-Handling_Multiple_Signal_Events.png" /></ac:image></p><h6 style="text-align: center;">Handling multiple Signal Events</h6></ac:rich-text-body></ac:structured-macro><p>To access Call Event data in Alf</p><hr /><ul><li><p class="auto-cursor-target">Use the names of the Parameters of the Operation to access their values. Output values for <em>out</em> and inout Parameters may be set using assignment, and those values are returned at the end of the run-to-completion step for the Call Event.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="979df5b7-5bed-4b84-be93-68af61e39d5f"><ac:rich-text-body><p>Output Parameters are available in entry and exit Behaviors, but <em>not</em> in do-activity Behaviors, since do-activity Behaviors can continue to run asynchronously after the end of the run-to-completion step.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></li></ul><p><br /></p><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="9a36e8b6-ca7a-4459-b9b1-883419d11c0a"><ac:rich-text-body><p>An alternative model would be to give the Order class that owns this StateMachine a <em>checkOut</em> Operation, with the StateMachine then handling a call to this Operation using a Call Event, as shown below. The entry Behavior in this case does the same thing as in the case above using a Signal Event, but note that the Parameters of the <em>checkOut</em> Operation are now used directly, instead of the property-access notation used for Signal Event data.</p><p><br /></p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="Acessing_Event_Data-Handling_checkOut_Call_Event.png" /></ac:image></p><h6 style="text-align: center;">Handling the checkOut Call Event</h6><p>Unlike Signal Events, access to Call Event data is only allowed if all relevant Transitions for a State Behavior (incoming for entry and do-activity, outgoing for exit) have Call Events for the same Operation. It is also not possible to access the Event data if Signal Events and Call Events are mixed, or are mixed with other kinds of Events (such as Time Events and Change Events).</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="two_equal"><ac:layout-cell><p><br /></p></ac:layout-cell><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=137986166 space=ALFP2024x version=1 -->
## PAGE 00006: Accessing the simulation time unit

- page_id: `137986166`
- space_key: `ALFP2024x`
- source_url: https://docs.nomagic.com/spaces/ALFP2024x/pages/137986166/Accessing+the+simulation+time+unit
- version_number: 1
- version_date: `2023-09-22T11:48:51.900+02:00`
- ancestors: Alf Plugin Documentation > User Guide > Working with Alf > Helper functions
- labels: []

### NORMALIZED CONTENT

The simulation time unit is defined in the current simulation configuration (in the tag *timeUnit* of a *SimulationConfig* stereotype). If no value is specified in the simulation configuration, the default unit of time is the millisecond. The *GetTimeUnit* function returns the name of the configured unit of time for a simulation.

```text

```

For example:

```text

```

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p>The simulation time unit is defined in the current simulation configuration (in the tag <em>timeUnit</em> of a <em>SimulationConfig</em> stereotype). If no value is specified in the simulation configuration, the default unit of time is the millisecond. The <em>GetTimeUnit</em> function returns the name of the configured unit of time for a simulation.</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="4bda9c26-cad7-4ef5-bbc3-954bf8fe16d5"><ac:parameter ac:name="language">text</ac:parameter><ac:plain-text-body><![CDATA[GetTimeUnit(): String[1]]]></ac:plain-text-body></ac:structured-macro><p><br /></p><p>For example:</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="23f48c62-df1d-424e-ab6f-affcdbd87006"><ac:parameter ac:name="language">text</ac:parameter><ac:plain-text-body><![CDATA[WriteLine("Simulation time unit is " + GetTimeUnit());]]></ac:plain-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=137986196 space=ALFP2024x version=1 -->
## PAGE 00007: Action API

- page_id: `137986196`
- space_key: `ALFP2024x`
- source_url: https://docs.nomagic.com/spaces/ALFP2024x/pages/137986196/Action+API
- version_number: 1
- version_date: `2023-09-22T11:48:54.655+02:00`
- ancestors: Alf Plugin Documentation > Developer Guide
- labels: []

### NORMALIZED CONTENT

The *AlfActionUtil* class also includes a set of static methods that perform operations over the entire active Project. These are:

- parse (with no argument), which parses the Alf bodies of all Elements in the active Project that are annotated as needing recompilation.
- parseAll, which parses all Alf text in the active Project, but does not do any mapping to UML.
- build, which does a [CONFLUENCE_PAGE title='Building and cleaning' space='ALFP2024x'] of the Alf bodies of all elements in the active project that are annotated as needing recompilation and, optionally, also elements annotated with compilation errors (depending on its includeErrorAnnotated argument).
- clean , which deletes all auxiliary template bindings and does a [CONFLUENCE_PAGE title='Building and cleaning' space='ALFP2024x'] of all Alf text in the active project.

In all cases, dependencies are registered for all parsed Elements and any errors are recorded as error Annotations on relevant Elements (see also [CONFLUENCE_PAGE title='The Alf editor' space='ALFP2024x'] and [CONFLUENCE_PAGE title='Dependency Management' space='ALFP2024x']).

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p>The <em>AlfActionUtil</em> class also includes a set of static methods that perform operations over the entire active Project. These are:</p><ul><li><em>parse</em> (with no argument), which parses the Alf bodies of all Elements in the active Project that are annotated as needing recompilation.</li><li><em>parseAll,</em> which parses all Alf text in the active Project, but does not do any mapping to UML.</li><li><em>build,</em> which does a <ac:link ac:anchor="build-project"><ri:page ri:space-key="ALFP2024x" ri:content-title="Building and cleaning" /><ac:plain-text-link-body><![CDATA[normal build]]></ac:plain-text-link-body></ac:link> of the Alf bodies of all elements in the active project that are annotated as needing recompilation and, optionally, also elements annotated with compilation errors (depending on its <em>includeErrorAnnotated</em> argument).</li><li><em>clean</em><em>,</em> which deletes all auxiliary template bindings and does a <ac:link ac:anchor="clean-project"><ri:page ri:space-key="ALFP2024x" ri:content-title="Building and cleaning" /><ac:plain-text-link-body><![CDATA[clean build]]></ac:plain-text-link-body></ac:link> of all Alf text in the active project.</li></ul><p>In all cases, dependencies are registered for all parsed Elements and any errors are recorded as error Annotations on relevant Elements (see also <ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="The Alf editor" /></ac:link> and <ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="Dependency Management" /></ac:link>).</p></ac:layout-cell><ac:layout-cell><p class="auto-cursor-target"><br /></p><p><br /></p><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="two_equal"><ac:layout-cell><p><br /></p></ac:layout-cell><ac:layout-cell><p> </p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=137986082 space=ALFP2024x version=1 -->
## PAGE 00008: Address Book

- page_id: `137986082`
- space_key: `ALFP2024x`
- source_url: https://docs.nomagic.com/spaces/ALFP2024x/pages/137986082/Address+Book
- version_number: 1
- version_date: `2023-09-22T11:48:46.427+02:00`
- ancestors: Alf Plugin Documentation > User Guide > Getting Started > Samples
- labels: []

### NORMALIZED CONTENT

The Address Book sample includes a simple Class model in which the behaviors of Class Operations have been written in Alf. The model includes a Class diagram showing an *Address Book* Class that contains zero or more instances of an *Entry* Class.

To see the Alf code for an Operation of a Class, open the [CONFLUENCE_PAGE title='The Alf editor' space='ALFP2024x'] window (select **Windows > Alf**) and select the Operation in the *Address Book* Class diagram. The Alf code for the Operation will then appear in the window.

[CONFLUENCE_PAGE title='Running a model with Alf' space='ALFP2024x']Executing the *TestAddressBook* Activity (using CST) exercises the functionality of the Address Book model. This activity should be run with the **Animation speed** slider set to its maximum (rightwards) position.

#### PANEL: Related Pages

Related Pages

[CONFLUENCE_PAGE title='Using Alf for Operation methods' space='ALFP2024x']

[CONFLUENCE_PAGE title='Running a model with Alf' space='ALFP2024x']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p>The Address Book sample includes a simple Class model in which the behaviors of Class Operations have been written in Alf. The model includes a Class diagram showing an <em>Address Book</em> Class that contains zero or more instances of an <em>Entry</em> Class.</p><p>To see the Alf code for an Operation of a Class, open the <ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="The Alf editor" /><ac:plain-text-link-body><![CDATA[Alf editor]]></ac:plain-text-link-body></ac:link> window (select <strong>Windows &gt; Alf</strong>) and select the Operation in the <em>Address Book</em> Class diagram. The Alf code for the Operation will then appear in the window.</p><p><ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="Running a model with Alf" /><ac:link-body>Executing the <em>TestAddressBook</em> Activity (using CST)</ac:link-body></ac:link> exercises the functionality of the Address Book model. This activity should be run with the <strong>Animation speed</strong> slider set to its maximum (rightwards) position.</p></ac:layout-cell><ac:layout-cell><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="1fb8a50c-3828-4dc8-b915-871e0191e946"><ac:parameter ac:name="title">Related Pages</ac:parameter><ac:rich-text-body><p><ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="Using Alf for Operation methods" /></ac:link></p><p><ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="Running a model with Alf" /></ac:link></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=137993525 space=ALFP2024x version=1 -->
## PAGE 00009: Alf as scripting language

- page_id: `137993525`
- space_key: `ALFP2024x`
- source_url: https://docs.nomagic.com/spaces/ALFP2024x/pages/137993525/Alf+as+scripting+language
- version_number: 1
- version_date: `2023-10-10T07:47:46.158+02:00`
- ancestors: Alf Plugin Documentation > User Guide
- labels: []

### NORMALIZED CONTENT

Alf may be used as a scripting language to write simple expressions without the need to compile the script. Scripts can be used in the body of Opaque Actions, Opaque Behaviors, Opaque Expressions, State Machine Guards, or even directly in the Simulation Console.

[IMAGE alt='' src='']

###### Simple Alf scripts used in State Machine diagram

###### Using Alf as a scripting language

Alf-Library must be loaded into the project to use as a scripting language.

To load the Alf-Library

- In the modeling tool main menu, click Tools and select Alf > Load Library .

In the script editor window, the language must be set to "Alf Script". The scripting window has an automatic syntax and constraint check, the same as [CONFLUENCE_PAGE title='The Alf editor' space=''][CONFLUENCE_PAGE title='The Alf editor' space=''].

[IMAGE alt='' src='']

Alf scripts do not support the interpretation of all Alf language expressions. Currently supported expressions are:

- Literal expressions
- Name expressions
- "this" expressions
- Parenthesized expressions
- Property access expressions (dot notation, e.g., "expr.feature")
- Instance creation expressions for objects (Constructorless, using the class name, e.g., "new C()")
- Class extent expressions ("C.allInstances()")
- Sequence construction expressions (e.g., "Integer[]{1,2,3}")
- Sequence access expression (e.g., "a[i]")
- Boolean unary expressions ("!")
- BitString unary expressions ("~")
- Numeric unary expressions ("+", "-")
- Cast expressions
- Isolation expressions (but with no isolation semantics)
- Arithmetic Expressions ("*", "/", "%", "+", "-")
- Shift Expressions ("<<", ">>", ">>>")
- Relational Expressions ("<", ">", "<=", ">=")
- Classification Expressions ("instanceof", "hastype")
- Equality Expressions ("=", "!=")
- Logical Expressions ("&", "^", "|")
- Conditional logical expressions ("&&", "||")
- Null-coalescing expressions ("??")
- Conditional test expressions ("… ? ... : … ")
- Assignment expressions
- Increment and decrement expressions ("++", "--")

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>Alf may be used as a scripting language to write simple expressions without the need to compile the script. Scripts can be used in the body of Opaque Actions, Opaque Behaviors, Opaque Expressions, State Machine Guards, or even directly in the Simulation Console. </p><p><ac:image ac:align="center" ac:border="true" ac:height="319" ac:width="539"><ri:attachment ri:filename="State machine.PNG" /></ac:image></p><h6 style="text-align: center;">Simple Alf scripts used in State Machine diagram</h6><h4>Using Alf as a scripting language</h4><p>Alf-Library must be loaded into the project to use as a scripting language.</p><p>   </p><p>To load the Alf-Library</p><hr /><ul><li>In the modeling tool main menu, click <strong>Tools </strong>and select <strong>Alf </strong>&gt; <strong>Load Library</strong>.</li></ul><p>  </p><p>In the script editor window, the language must be set to &quot;Alf Script&quot;. The scripting window has an automatic syntax and constraint check, the same as <ac:link><ri:page ri:content-title="The Alf editor" /><ac:plain-text-link-body><![CDATA[the ]]></ac:plain-text-link-body></ac:link><ac:link><ri:page ri:content-title="The Alf editor" /><ac:plain-text-link-body><![CDATA[Alf editor window]]></ac:plain-text-link-body></ac:link>.</p><p><ac:image ac:align="center" ac:border="true" ac:height="389" ac:width="859"><ri:attachment ri:filename="edit window .png" /></ac:image></p><p>Alf scripts do not support the interpretation of all Alf language expressions. Currently supported expressions are:</p><ul><li>Literal expressions</li><li>Name expressions</li><li>&quot;this&quot; expressions</li><li>Parenthesized expressions</li><li>Property access expressions (dot notation, e.g., &quot;expr.feature&quot;)</li><li>Instance creation expressions for objects (Constructorless, using the class name, e.g., &quot;new C()&quot;)</li><li>Class extent expressions (&quot;C.allInstances()&quot;)</li><li>Sequence construction expressions (e.g., &quot;Integer[]{1,2,3}&quot;)</li><li>Sequence access expression (e.g., &quot;a[i]&quot;)</li><li>Boolean unary expressions (&quot;!&quot;)</li><li>BitString unary expressions (&quot;~&quot;)</li><li>Numeric unary expressions (&quot;+&quot;, &quot;-&quot;)</li><li>Cast expressions</li><li>Isolation expressions (but with no isolation semantics)</li><li>Arithmetic Expressions (&quot;*&quot;, &quot;/&quot;, &quot;%&quot;, &quot;+&quot;, &quot;-&quot;)</li><li>Shift Expressions (&quot;&lt;&lt;&quot;, &quot;&gt;&gt;&quot;, &quot;&gt;&gt;&gt;&quot;)</li><li>Relational Expressions (&quot;&lt;&quot;, &quot;&gt;&quot;, &quot;&lt;=&quot;, &quot;&gt;=&quot;)</li><li>Classification Expressions (&quot;instanceof&quot;, &quot;hastype&quot;)</li><li>Equality Expressions (&quot;=&quot;, &quot;!=&quot;)</li><li>Logical Expressions (&quot;&amp;&quot;, &quot;^&quot;, &quot;|&quot;)</li><li>Conditional logical expressions (&quot;&amp;&amp;&quot;, &quot;||&quot;)</li><li>Null-coalescing expressions (&quot;??&quot;)</li><li>Conditional test expressions (&quot;… ? ... : … &quot;)</li><li>Assignment expressions</li><li>Increment and decrement expressions (&quot;++&quot;, &quot;--&quot;)</li></ul>
````

<!--NOMAGIC_PAGE id=137986068 space=ALFP2024x version=2 -->
## PAGE 00010: Alf Plugin Documentation

- page_id: `137986068`
- space_key: `ALFP2024x`
- source_url: https://docs.nomagic.com/spaces/ALFP2024x/pages/137986068/Alf+Plugin+Documentation
- version_number: 2
- version_date: `2024-05-08T13:22:35.650+02:00`
- ancestors: 
- labels: []

### NORMALIZED CONTENT



### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="3f8791bd-6289-4990-bed4-7b76de13abc5" /></p><p><br /></p>
````

<!--NOMAGIC_PAGE id=137986084 space=ALFP2024x version=1 -->
## PAGE 00011: Alf project template

- page_id: `137986084`
- space_key: `ALFP2024x`
- source_url: https://docs.nomagic.com/spaces/ALFP2024x/pages/137986084/Alf+project+template
- version_number: 1
- version_date: `2023-09-22T11:48:46.620+02:00`
- ancestors: Alf Plugin Documentation > User Guide > Getting Started
- labels: []

### NORMALIZED CONTENT

A project in which Alf is to be used can be created using the *Alf project template.* A project created in this way already has the required *Alf Standard Model Library* included, and it has the language *"Alf"* set as the default for the bodies of opaque behaviors, actions and expressions.

To create a project from the Alf template

1. Select **Create New Project** under **Manage Projects** on the Welcome Screen, or select**File** > **New Project** on the main menu. The **New Project** window will open (see the following figure). 
[IMAGE alt='' src='']
2. On the bottom left, select Project from Template from the Other group (you may need to scroll down).
3. On the bottom right, under Select template , open the Alf folder and select Alf .
4. Enter the project name and location in the usual way and click OK .

If you have the Alf Plugin installed, but you are working on a project that does include the Alf Library, then it will not be possible to edit or compile Alf code. To enable the use of Alf in the project, load the Alf Library by selecting **Tools > Alf > Load Library**.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>A project in which Alf is to be used can be created using the <em>Alf project template.</em> A project created in this way already has the required <em>Alf Standard Model Library</em> included, and it has the language <em>&quot;Alf&quot;</em> set as the default for the bodies of opaque behaviors, actions and expressions.</p><p><br /></p><p>To create a project from the Alf template</p><hr /><ol><li><p class="auto-cursor-target">Select <strong>Create New Project</strong> under <strong>Manage Projects</strong> on the Welcome Screen, or select<strong> File</strong> &gt; <strong>New Project</strong> on the main menu. The <strong>New Project</strong> window will open (see the following figure).<br /><ac:image><ri:attachment ri:filename="AlfProjectTemplate-NewProject.png"><ri:page ri:space-key="ALFP2024x" ri:content-title="Alf project template" /></ri:attachment></ac:image></p></li><li>On the bottom left, select <strong>Project from Template</strong> from the <strong>Other</strong> group (you may need to scroll down).</li><li>On the bottom right, under <strong>Select template</strong>, open the <strong>Alf</strong> folder and select <strong>Alf</strong>.</li><li>Enter the project name and location in the usual way and click <strong>OK</strong>.</li></ol><p><br /></p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="99343bd6-3320-49e7-bfd3-f4799ac59711"><ac:rich-text-body><p>If you have the Alf Plugin installed, but you are working on a project that does include the Alf Library, then it will not be possible to edit or compile Alf code. To enable the use of Alf in the project, load the Alf Library by selecting <strong>Tools &gt; Alf &gt; Load Library</strong>.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p>
````

<!--NOMAGIC_PAGE id=137986198 space=ALFP2024x version=2 -->
## PAGE 00012: Alf Tutorial 1: Hello World

- page_id: `137986198`
- space_key: `ALFP2024x`
- source_url: https://docs.nomagic.com/spaces/ALFP2024x/pages/137986198/Alf+Tutorial+1+Hello+World
- version_number: 2
- version_date: `2024-01-31T12:56:04.446+01:00`
- ancestors: Alf Plugin Documentation > Tutorials
- labels: []

### NORMALIZED CONTENT

This tutorial describes how to create an Alf project containing a very simple "Hello World" activity that can be executed using Cameo Simulation Toolkit. (This Activity is similar to, but even simpler than, the one in the [CONFLUENCE_PAGE title='Hello' space=''] sample model.)

It consists of three steps:

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>This tutorial describes how to create an Alf project containing a very simple &quot;Hello World&quot; activity that can be executed using Cameo Simulation Toolkit. (This Activity is similar to, but even simpler than, the one in the <ac:link><ri:page ri:content-title="Hello" /></ac:link> sample model.)</p><p>It consists of three steps:</p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="bc78428b-c500-470f-a6cc-c99a5175c00c" /></p><p><br /></p>
````

<!--NOMAGIC_PAGE id=137986206 space=ALFP2024x version=2 -->
## PAGE 00013: Alf Tutorial 2: Address Book

- page_id: `137986206`
- space_key: `ALFP2024x`
- source_url: https://docs.nomagic.com/spaces/ALFP2024x/pages/137986206/Alf+Tutorial+2+Address+Book
- version_number: 2
- version_date: `2024-01-31T12:56:16.063+01:00`
- ancestors: Alf Plugin Documentation > Tutorials
- labels: []

### NORMALIZED CONTENT

This tutorial describes how to create an Alf project containing a simple *Address Book* model, along with a test**Activity that can be executed using Cameo Simulation Toolkit. (This model is similar to, but even simpler than, the one in the [CONFLUENCE_PAGE title='Address Book' space=''] sample model.)

It consists of the following steps:

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>This tutorial describes how to create an Alf project containing a simple <em>Address Book</em> model, along with a test<em> </em>Activity that can be executed using Cameo Simulation Toolkit. (This model is similar to, but even simpler than, the one in the <ac:link><ri:page ri:content-title="Address Book" /></ac:link> sample model.)</p><p>It consists of the following steps:</p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="94620dbe-55e6-48b2-b662-ddda751b1336" /></p><p><br /></p>
````

<!--NOMAGIC_PAGE id=137986220 space=ALFP2024x version=2 -->
## PAGE 00014: Alf Tutorial 3: Stopwatch

- page_id: `137986220`
- space_key: `ALFP2024x`
- source_url: https://docs.nomagic.com/spaces/ALFP2024x/pages/137986220/Alf+Tutorial+3+Stopwatch
- version_number: 2
- version_date: `2024-01-31T12:56:27.204+01:00`
- ancestors: Alf Plugin Documentation > Tutorials
- labels: []

### NORMALIZED CONTENT

This tutorial you will construct a state machine model for a simple stopwatch that increments by 1 every second. This model is a version of the stopwatch model used in the [tutorial for Cameo Simulation Toolkit (CST).](https://docs.nomagic.com/display/CSTTWRT/Tutorial) However, unlike in the CST toolkit, Behaviors will be defined using Alf, rather than Activity diagrams.

##### The stopwatch structure

The structure of the stopwatch model in this tutorial is very simple. It only contains a *time* property, which is typed as *Integer.* The *time* property records the elapsed time once the stopwatch receives a starting Signal. Therefore, the structure of the stopwatch system contains a *StopWatch* class that has the *time* property.

##### The stopwatch behavior

The tutorial uses a State Machine diagram to describe the main behavior of the stopwatch. The State Machine consists of four States:

1. ready – The State in which the stopwatch is ready to start.
2. running – The State that the stopwatch enters once it receives a Start signal. The stopwatch runs and the timer starts. The stopwatch is triggered by a Time Event to increment the time value by 1 each second.
3. paused – The State in which the stopwatch is paused and waiting for the user to restart it.
4. stopped – The State in which the stopwatch stops running.

The tutorial consists of the following steps:

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>This tutorial you will construct a state machine model for a simple stopwatch that increments by 1 every second. This model is a version of the stopwatch model used in the <a href="https://docs.nomagic.com/display/CSTTWRT/Tutorial">tutorial for Cameo Simulation Toolkit (CST).</a> However, unlike in the CST toolkit, Behaviors will be defined using Alf, rather than Activity diagrams.</p><h3>The stopwatch structure</h3><p>The structure of the stopwatch model in this tutorial is very simple. It only contains a <em>time</em> property, which is typed as <em>Integer.</em> The <em>time</em> property records the elapsed time once the stopwatch receives a starting Signal. Therefore, the structure of the stopwatch system contains a <em>StopWatch</em> class that has the <em>time</em> property.</p><h3>The stopwatch behavior</h3><p>The tutorial uses a State Machine diagram to describe the main behavior of the stopwatch. The State Machine consists of four States:</p><ol><li><em>ready</em> – The State in which the stopwatch is ready to start.</li><li><em>running</em> – The State that the stopwatch enters once it receives a <em>Start</em> signal. The stopwatch runs and the timer starts. The stopwatch is triggered by a Time Event to increment the <em>time</em> value by 1 each second.</li><li><em>paused</em> – The State in which the stopwatch is paused and waiting for the user to restart it.</li><li><em>stopped</em> – The State in which the stopwatch stops running.</li></ol><p><br /></p><p>The tutorial consists of the following steps:</p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="e427ccf6-3901-4d84-adc1-a7f93231c2e1" /></p><p><br /></p>
````

<!--NOMAGIC_PAGE id=137986178 space=ALFP2024x version=1 -->
## PAGE 00015: Building and cleaning

- page_id: `137986178`
- space_key: `ALFP2024x`
- source_url: https://docs.nomagic.com/spaces/ALFP2024x/pages/137986178/Building+and+cleaning
- version_number: 1
- version_date: `2023-09-22T11:48:52.543+02:00`
- ancestors: Alf Plugin Documentation > User Guide > Compiling Alf
- labels: []

### NORMALIZED CONTENT

As discussed in [CONFLUENCE_PAGE title='Dependency Management' space='ALFP2024x'], when you make changes within a model, the Alf compiler normally automatically processes any Alf code that might be affected by these changes. However, in some cases the Alf compiler may not have enough information to realize that a change in the model will correct an error in previously erroneous Alf code. Or, you may have turned off the [CONFLUENCE_PAGE title='Environment options' space='ALFP2024x']**Build Automatically** environment option, in which case the Alf compiler will mark elements needing recompilation without automatically recompiling them.

For cases such as the above, the Alf plugin provides two commands that allow you to manually trigger the recompilation of Alf code, which is known as doing an Alf *build* of your project. These commands are available by selecting **Tools > Alf** from the main menu.

- **Build Project**[CONFLUENCE_PAGE title='Building and cleaning' space='ALFP2024x'] – A normal build triggers the recompilation of the Alf bodies of all model elements marked as having Alf compilation errors or otherwise needing to be recompiled.
- [CONFLUENCE_PAGE title='Building and cleaning' space='ALFP2024x'] – A clean build triggers the recompilation of all Alf code in your project, whether it is marked as needing recompilation or not.

##### build-projectBuild Project

To initiate a normal build of your project, select **Tools > Alf > Build Project**. If there are any elements in your project that are marked with either an Alf compilation error annotation or an Alf recompilation-needed warning annotation (see [CONFLUENCE_PAGE title='Dependency Management' space='ALFP2024x']), then the Alf bodies for these elements will be recompiled. Any previously erroneous Alf code that compiles successfully has its error annotation removed, while any code with new compilation errors has a new error annotation added. All recompilation-needed warning annotations are removed.

A progress bar will appear to track the progress of the build. If a build takes a long time, then you can cancel it before it is complete. If you cancel a build, then any compilation of Alf code that happened before the cancellation will be reflected in your model. Elements that have not yet been processed will still have the annotations that they had before the build was initiated. To process those remaining elements, initiate a new build.

The figure below shows the error annotations caused by deleting the Association in the [CONFLUENCE_PAGE title='Address Book' space='ALFP2024x'] example and then recreating it as a new Association, so the error annotations remain (see also the discussion of this example in [CONFLUENCE_PAGE title='Dependency Management' space='ALFP2024x']). Selecting **Tools > Alf > Build Project** initiates an Alf build of the project, resulting in the successful recompilation of the indicated operations and the removal of the error annotations.

[IMAGE alt='' src='']

###### Example showing the need to manually rebuild

##### clean-projectClean Project

To initiate a clean build of your project, select **Tools > Alf > Clean Project**. This will result in the removal of all existing Alf annotations in your project and the recompilation of all Alf code. The Alf compiler will then add error annotations to any elements with Alf code that has compilation errors.

Compilation of template bindings in your Alf code result in the generation of instantiated Classes in the [CONFLUENCE_PAGE title='The Alf compiler' space='ALFP2024x']*$$Template Bindings* Package in your project. Over time, Classes in this Package may accumulate that are no longer necessary for your project. A clean rebuild first cleans out this Package, so, at the end of the build, it contains only the instantiations truly needed for the Alf code actually in your project. If your Alf code no longer has any template bindings, then the Package is removed entirely from your model.

If you move a lot of the elements in a project around between Packages, the Alf compiler may lose track of some potential dependencies and not properly mark all necessary recompilations. Therefore, if you do significant restructuring of your model, it is a good idea to then perform a clean rebuild of all the Alf code, which will ensure all the code is checked for errors and that the dependency tracking is properly rebuilt.

If your project contains a lot of Alf code, then a clean rebuild will likely take quite a bit longer than a normal build. A progress bar will appear to track the progress of the build and allow you to cancel it before it completes. However, if you cancel a clean build before it completes, then the model will be updated with the results of only the compilations that occurred before the cancellation, which can result in inconsistencies. To avoid this, you can perform an **Undo** to undo all changes made by the canceled build.

#### PANEL: Table of Contents

Table of Contents

3

#### PANEL: Related pages

Related pages

- [CONFLUENCE_PAGE title='The Alf compiler' space='ALFP2024x']
- [CONFLUENCE_PAGE title='Dependency Management' space='ALFP2024x']
- [CONFLUENCE_PAGE title='Environment options' space='ALFP2024x']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p>As discussed in <ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="Dependency Management" /></ac:link>, when you make changes within a model, the Alf compiler normally automatically processes any Alf code that might be affected by these changes. However, in some cases the Alf compiler may not have enough information to realize that a change in the model will correct an error in previously erroneous Alf code. Or, you may have turned off the <ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="Environment options" /><ac:link-body><strong>Build Automatically</strong> environment option</ac:link-body></ac:link>, in which case the Alf compiler will mark elements needing recompilation without automatically recompiling them.</p><p>For cases such as the above, the Alf plugin provides two commands that allow you to manually trigger the recompilation of Alf code, which is known as doing an Alf <em>build</em> of your project. These commands are available by selecting <strong>Tools &gt; Alf</strong> from the main menu.</p><ul><li><ac:link ac:anchor="build-project"><ac:link-body><strong>Build Project</strong></ac:link-body><ri:page ri:space-key="ALFP2024x" ri:content-title="Building and cleaning" /></ac:link> – A <em>normal build</em> triggers the recompilation of the Alf bodies of all model elements marked as having Alf compilation errors or otherwise needing to be recompiled.</li><li><strong><ac:link ac:anchor="clean-project"><ac:plain-text-link-body><![CDATA[Clean Project]]></ac:plain-text-link-body><ri:page ri:space-key="ALFP2024x" ri:content-title="Building and cleaning" /></ac:link></strong> – A <em>clean build </em>triggers the recompilation of all Alf code in your project, whether it is marked as needing recompilation or not.</li></ul><h3><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="835b7b59-b9a5-4452-b0fc-7032e6338769"><ac:parameter ac:name="">build-project</ac:parameter></ac:structured-macro>Build Project</h3><p>To initiate a normal build of your project, select <strong>Tools &gt; Alf &gt; Build Project</strong>. If there are any elements in your project that are marked with either an Alf compilation error annotation or an Alf recompilation-needed warning annotation (see <ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="Dependency Management" /></ac:link>), then the Alf bodies for these elements will be recompiled. Any previously erroneous Alf code that compiles successfully has its error annotation removed, while any code with new compilation errors has a new error annotation added. All recompilation-needed warning annotations are removed.</p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="9a6f9292-ebed-4169-b1a7-8bb7eafbb004"><ac:rich-text-body><p>A progress bar will appear to track the progress of the build. If a build takes a long time, then you can cancel it before it is complete. If you cancel a build, then any compilation of Alf code that happened before the cancellation will be reflected in your model. Elements that have not yet been processed will still have the annotations that they had before the build was initiated. To process those remaining elements, initiate a new build.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="6d5693e5-3b23-404d-bb36-266ef8ace73f"><ac:rich-text-body><p>The figure below shows the error annotations caused by deleting the Association in the <ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="Address Book" /></ac:link> example and then recreating it as a new Association, so the error annotations remain (see also the discussion of this example in <ac:link ac:anchor="rebuild"><ri:page ri:space-key="ALFP2024x" ri:content-title="Dependency Management" /><ac:plain-text-link-body><![CDATA[Dependency Management]]></ac:plain-text-link-body></ac:link>). Selecting <strong>Tools &gt; Alf &gt; Build Project</strong> initiates an Alf build of the project, resulting in the successful recompilation of the indicated operations and the removal of the error annotations.</p><p><ac:image ac:align="center"><ri:attachment ri:filename="Dependency_Management-Example2.png"><ri:page ri:space-key="ALFP2024x" ri:content-title="Dependency Management" /></ri:attachment></ac:image></p><h6 style="text-align: center;">Example showing the need to manually rebuild</h6></ac:rich-text-body></ac:structured-macro><h3 class="auto-cursor-target"><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="0fce3b76-08c6-4e4f-8727-9a0b875d8c08"><ac:parameter ac:name="">clean-project</ac:parameter></ac:structured-macro>Clean Project</h3><p>To initiate a clean build of your project, select <strong>Tools &gt; Alf &gt; Clean Project</strong>. This will result in the removal of all existing Alf annotations in your project and the recompilation of all Alf code. The Alf compiler will then add error annotations to any elements with Alf code that has compilation errors.</p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="f085f776-8191-4ccd-8237-ba62782d9804"><ac:rich-text-body><p>Compilation of template bindings in your Alf code result in the generation of instantiated Classes in the <ac:link ac:anchor="template-bindings-package"><ri:page ri:space-key="ALFP2024x" ri:content-title="The Alf compiler" /><ac:link-body><em>$$Template Bindings</em> Package</ac:link-body></ac:link> in your project. Over time, Classes in this Package may accumulate that are no longer necessary for your project. A clean rebuild first cleans out this Package, so, at the end of the build, it contains only the instantiations truly needed for the Alf code actually in your project. If your Alf code no longer has any template bindings, then the Package is removed entirely from your model.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="6918dde9-12ea-48a0-9492-1c146a6241a0"><ac:rich-text-body><p>If you move a lot of the elements in a project around between Packages, the Alf compiler may lose track of some potential dependencies and not properly mark all necessary recompilations. Therefore, if you do significant restructuring of your model, it is a good idea to then perform a clean rebuild of all the Alf code, which will ensure all the code is checked for errors and that the dependency tracking is properly rebuilt.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="warning" ac:schema-version="1" ac:macro-id="7c3fbdee-b0ae-4252-95fa-4f9753f297c8"><ac:rich-text-body><p>If your project contains a lot of Alf code, then a clean rebuild will likely take quite a bit longer than a normal build. A progress bar will appear to track the progress of the build and allow you to cancel it before it completes. However, if you cancel a clean build before it completes, then the model will be updated with the results of only the compilations that occurred before the cancellation, which can result in inconsistencies. To avoid this, you can perform an <strong>Undo</strong> to undo all changes made by the canceled build.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell><ac:layout-cell><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="3bb9dab7-127f-430f-8900-581fc0fede63"><ac:parameter ac:name="title">Table of Contents</ac:parameter><ac:rich-text-body><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="cbe3b3d0-62fb-4d34-9fed-d268d335cb69"><ac:parameter ac:name="maxLevel">3</ac:parameter></ac:structured-macro></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="6c0b723d-8d75-4413-a546-848fbb8b267e"><ac:parameter ac:name="title">Related pages</ac:parameter><ac:rich-text-body><ul><li><ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="The Alf compiler" /></ac:link></li><li><ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="Dependency Management" /></ac:link></li><li><ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="Environment options" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=137986164 space=ALFP2024x version=1 -->
## PAGE 00016: Checking a visited State

- page_id: `137986164`
- space_key: `ALFP2024x`
- source_url: https://docs.nomagic.com/spaces/ALFP2024x/pages/137986164/Checking+a+visited+State
- version_number: 1
- version_date: `2023-09-22T11:48:51.679+02:00`
- ancestors: Alf Plugin Documentation > User Guide > Working with Alf > Helper functions
- labels: []

### NORMALIZED CONTENT

The *WasInState* function checks whether the state with the given name has ever been visited for a particular object:

```text

```

Both arguments of the function are required. For example"

```text

```

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p>The <em>WasInState</em> function checks whether the state with the given name has ever been visited for a particular object:</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="78465268-4a73-4879-a5dd-b908c37b2173"><ac:parameter ac:name="language">text</ac:parameter><ac:plain-text-body><![CDATA[WasInState(in object: any[1], in stateName: String): Boolean]]></ac:plain-text-body></ac:structured-macro><p><br /></p><p>Both arguments of the function are required. For example&quot;</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="4b996387-85c6-4eb8-930c-8f16c5dc2c81"><ac:parameter ac:name="language">text</ac:parameter><ac:plain-text-body><![CDATA[if (WasInState(obj, "S1") {
	WriteLine("Obj was in state S1.");
}]]></ac:plain-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=137986163 space=ALFP2024x version=1 -->
## PAGE 00017: Checking the State of an object

- page_id: `137986163`
- space_key: `ALFP2024x`
- source_url: https://docs.nomagic.com/spaces/ALFP2024x/pages/137986163/Checking+the+State+of+an+object
- version_number: 1
- version_date: `2023-09-22T11:48:51.543+02:00`
- ancestors: Alf Plugin Documentation > User Guide > Working with Alf > Helper functions
- labels: []

### NORMALIZED CONTENT

The *InState* function checks if a particular object is in the state with the given name:

```text

```

Both arguments of the function are required. For example:

```text

```

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p>The <em>InState</em> function checks if a particular object is in the state with the given name:<br /><span style="color: rgb(127,0,85);"> </span></p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="d2a7e748-0ab1-47b5-aa35-71a847309a97"><ac:parameter ac:name="language">text</ac:parameter><ac:plain-text-body><![CDATA[InState(in object : any[1], in stateName : String[1]): Boolean[1]
]]></ac:plain-text-body></ac:structured-macro><p><br /></p><p>Both arguments of the function are required. For example:</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="94bef7e0-c006-4015-bd41-5fe5b115b3b4"><ac:parameter ac:name="language">text</ac:parameter><ac:plain-text-body><![CDATA[if (InState(ccobj, "Operating")) {
	force = ccForce;
} else {
	force = acc * 2;
}]]></ac:plain-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=137986188 space=ALFP2024x version=1 -->
## PAGE 00018: Compiler API

- page_id: `137986188`
- space_key: `ALFP2024x`
- source_url: https://docs.nomagic.com/spaces/ALFP2024x/pages/137986188/Compiler+API
- version_number: 1
- version_date: `2023-09-22T11:48:53.490+02:00`
- ancestors: Alf Plugin Documentation > Developer Guide
- labels: []

### NORMALIZED CONTENT

The *AlfCompiler* class provides the basic interface for compiling Alf code. The processing of a single piece of Alf text is called a *compilation,* which takes place in two steps:

1. [CONFLUENCE_PAGE title='Compiler API: Parsing' space='ALFP2024x'] (including constraint checking)
2. [CONFLUENCE_PAGE title='Compiler API: Mapping' space='ALFP2024x']

The API allows you to carry out these steps individually (which is useful if, for example, you wish to parse but not map some code) or using a single call.

#### PANEL: Related Pages

Related Pages

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p>The <em>AlfCompiler</em> class provides the basic interface for compiling Alf code. The processing of a single piece of Alf text is called a <em>compilation,</em> which takes place in two steps:</p><ol><li><ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="Compiler API: Parsing" /><ac:plain-text-link-body><![CDATA[Parsing]]></ac:plain-text-link-body></ac:link> (including constraint checking)</li><li><ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="Compiler API: Mapping" /><ac:plain-text-link-body><![CDATA[Mapping]]></ac:plain-text-link-body></ac:link></li></ol><p>The API allows you to carry out these steps individually (which is useful if, for example, you wish to parse but not map some code) or <span class="confluence-link">using a single call</span>.</p></ac:layout-cell><ac:layout-cell><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="c9e705e7-c70e-4d93-b5f0-d11eaf392bbb"><ac:parameter ac:name="title">
       Related Pages
      </ac:parameter><ac:rich-text-body><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="f1fa4f0e-d74d-43ad-a221-703585bb068a" /></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="two_equal"><ac:layout-cell><p><br /></p></ac:layout-cell><ac:layout-cell><p> </p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=137986190 space=ALFP2024x version=1 -->
## PAGE 00019: Compiler API: Mapping

- page_id: `137986190`
- space_key: `ALFP2024x`
- source_url: https://docs.nomagic.com/spaces/ALFP2024x/pages/137986190/Compiler+API+Mapping
- version_number: 1
- version_date: `2023-09-22T11:48:53.678+02:00`
- ancestors: Alf Plugin Documentation > Developer Guide > Compiler API
- labels: []

### NORMALIZED CONTENT

*Mapping* is the process of generating a UML activity model from the abstract syntax representation of some Alf code. If this mapping is successful, then the Alf compiler updates the context element using the generated elements. How this update is done depends on what the context element is:

- If the context element is an Activity, the nodes and edges of the Activity are replaced with those generated by the compilation.
- If the context element is an Opaque Behavior or Opaque Action, a CompiledRepresentation stereotype is applied with its behavior tag pointing to the compiled Behavior.
- If the context element is an Opaque Expression, its behavior property is set to the compiled Behavior.

In addition, there may be some generated elements that cannot be stored in conjunction with the context element. In particular, generated Instance Specifications are stored in the nearest Package containing the context element, and generated template instantations are stored in the [CONFLUENCE_PAGE title='The Alf compiler' space='ALFP2024x'] package.

If you have successfully parsed some Alf code text, then you can map that code by calling the *map* method. (If the parse was not successful, then calling *map* has no effect.) Normally, unless there is a system error, mapping should always complete successfully. Since mapping results in an update to the UML model, the *map* method should be called within a MagicDraw session. This can be done conveniently using the *AlfActionUtil.executeSession* method, which also ensures that any automatic Alf compilation is turned off during the session, so new compilations are not accidentally triggered by updates from the mapping process.

```java

```

Rather than separately parsing and mapping some Alf text, you can attempt to do both with one call to the *compile* method. This method first parses some text for a given context element and, if that is successful, maps it and updates the UML model appropriately with the results of the mapping. If the parse is not successful, then compilation errors are available using the *getCompilerErrors* method, as after a call to the *parse* method. As for the *map* method, the *compile* method should be called within a MagicDraw session, since it may potentially update the UML model if a mapping is carried out.

```java

```

#### PANEL: Related Pages

Related Pages

- [CONFLUENCE_PAGE title='Compiler API: Parsing' space='ALFP2024x']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p><em>Mapping</em> is the process of generating a UML activity model from the abstract syntax representation of some Alf code. If this mapping is successful, then the Alf compiler updates the context element using the generated elements. How this update is done depends on what the context element is:</p><ul><li>If the context element is an Activity, the nodes and edges of the Activity are replaced with those generated by the compilation.</li><li>If the context element is an Opaque Behavior or Opaque Action, a <em>CompiledRepresentation</em> stereotype is applied with its <em>behavior</em> tag pointing to the compiled Behavior.</li><li>If the context element is an Opaque Expression, its <em>behavior</em> property is set to the compiled Behavior.</li></ul><p>In addition, there may be some generated elements that cannot be stored in conjunction with the context element. In particular, generated Instance Specifications are stored in the nearest Package containing the context element, and generated template instantations are stored in the <ac:link ac:anchor="template-bindings-package"><ri:page ri:space-key="ALFP2024x" ri:content-title="The Alf compiler" /><ac:plain-text-link-body><![CDATA[$$Template Bindings]]></ac:plain-text-link-body></ac:link> package.</p><p>If you have successfully parsed some Alf code text, then you can map that code by calling the <em>map</em> method. (If the parse was not successful, then calling <em>map</em> has no effect.) Normally, unless there is a system error, mapping should always complete successfully. Since mapping results in an update to the UML model, the <em>map</em> method should be called within a MagicDraw session. This can be done conveniently using the <em>AlfActionUtil.executeSession</em> method, which also ensures that any automatic Alf compilation is turned off during the session, so new compilations are not accidentally triggered by updates from the mapping process.</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="122c120f-9064-4027-a2bd-0099d7c61cba"><ac:parameter ac:name="language">
       java
      </ac:parameter><ac:plain-text-body><![CDATA[AlfCompiler compiler = new AlfCompiler();
compiler.setContextElement(element);
compiler.parse(text);
if (compiler.isSuccessful()) {
	AlfActionUtil.executeSession("Map Alf", new Runnable() {
		public void run() {
			compiler.map();
			AlfActionUtil.registerDependencies(compiler);
 		}
 	});
}]]></ac:plain-text-body></ac:structured-macro><p>Rather than separately <span class="confluence-link">parsing</span> and <span class="confluence-link">mapping</span> some Alf text, you can attempt to do both with one call to the <em>compile</em> method. This method first parses some text for a given context element and, if that is successful, maps it and updates the UML model appropriately with the results of the mapping. If the parse is not successful, then compilation errors are available using the <em>getCompilerErrors</em> method, as after a call to the <em>parse</em> method. As for the <em>map</em> method, the <em>compile</em> method should be called within a MagicDraw session, since it may potentially update the UML model if a mapping is carried out.</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="33649f26-e83d-42ba-8e21-89c56e23401a"><ac:parameter ac:name="language">
       java
      </ac:parameter><ac:plain-text-body><![CDATA[Compiler compiler = new AlfCompiler();
AlfActionUtil.executeSession("Compile Alf", new Runnable() {
	public void run() {
		compiler.compile(element, text); 
		AlfActionUtil.registerDependencies(compiler);
	}
});]]></ac:plain-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell><ac:layout-cell><p><br /></p><p class="auto-cursor-target"><br /></p><p><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="20911721-b872-4176-bfa5-9aae19d59ee1"><ac:parameter ac:name="title">
       Related Pages
      </ac:parameter><ac:rich-text-body><ul><li><ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="Compiler API: Parsing" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro><p><br /></p><p class="auto-cursor-target"> </p><p><br /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="two_equal"><ac:layout-cell><p><br /></p><p><br /></p><p><br /></p></ac:layout-cell><ac:layout-cell><p> </p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=137986189 space=ALFP2024x version=1 -->
## PAGE 00020: Compiler API: Parsing

- page_id: `137986189`
- space_key: `ALFP2024x`
- source_url: https://docs.nomagic.com/spaces/ALFP2024x/pages/137986189/Compiler+API+Parsing
- version_number: 1
- version_date: `2023-09-22T11:48:53.600+02:00`
- ancestors: Alf Plugin Documentation > Developer Guide > Compiler API
- labels: []

### NORMALIZED CONTENT

*Parsing* is the process of creating an abstract syntax representation of some Alf code. If parsing is successful, the Alf compiler also performs constraint checking on the resulting abstract syntax tree. *Constraint checking* is the process of doing name resolution and validating the Alf code against the static-semantic constraints defined in the Alf specification.

A compilation takes place in the context of a specific Named Element in the UML model, called the *context element*. During parsing and constraint checking, name resolution is performed in the scope containing the context element (known, in Alf terms, as the *model scope*). After the successful mapping of Alf code to UML, the context element is updated with the results of the compilation. The context element should be an Activity, Opaque Behavior, Opaque Action or Opaque Expression

In UML, a Behavior may have a context Classifier (for example, the Class that owns a State Machine as its classifier behavior is the context Classifier for the State Machine). This use of the term "context" is unrelated to the term "context element" for an Alf compilation.

To compile some Alf code text, first set the context element using the *setContextElement* method and then call the *parse* method, passing the text. What Alf text can be validly parsed depends on what the context element is.

- If the context element is a Value Specification, then the text is assumed to be for an Alf Expression.
- If the context element is an Opaque Action, then the text may be an Alf Expression or Statement Sequence.
- Otherwise the text is assumed to be for an Alf Statement Sequence.

The Alf code associated with an Activity, Opaque Behavior, Opaque Action or Opaque Expression is known as the *Alf body* of that element. The Alf code is saved in the model differently for different kinds of Elements. However, you can use the *AlfElementUtil.getAlfBody* operation to get the Alf body of an Element (if it has one).

After the parsing process completes, you can check if it was successful by calling the *isSuccessful* method. If the parse is successful, then the resulting abstract syntax tree is rooted in an Alf Unit Definition obtained by calling the *getUnit* method, which in turn always contains an Activity Definition (which may be obtained by calling the *UnitDefinition.getDefinition* method). If there were errors, then you can retrieve them using the *get**CompilerErrors* method. A single *AlfCompiler* instance my be used to compile multiple Alf code texts, for the same or different context elements.

Alf abstract syntax classes are found in sub-packages of the package *org.modeldriven.alf.syntax,* which is from the Alf Reference Implementation, with source available [here](https://github.com/ModelDriven/Alf-Reference-Implementation/tree/master/org.modeldriven.alf/src/org/modeldriven/alf/syntax). These abstract syntax classes allow the abstract syntax tree to be navigated based on the structure of the abstract syntax metamodel defined in the Alf specification. For instance, the value of the *definition* property of a *UnitDefinition* is obtained by calling *getDefinition,* the *name* of that definition is obtained using *getName,* etc. (Note that use of the Reference Implementation outside of MagicDraw tooling is subject to its separate open-source licensing terms.)

For the purposes of triggering automatic compilation, the Alf compiler also [manages a record of the dependencies](https://docs.nomagic.com/display/ALFP2024x/Dependency+Management) of Alf code in a model on other model elements. After successfully parsing some Alf code, if you want to update the dependency record based on the parse, you need to call the *AlfActionUtil.registerDependencies* method. If you do multiple parses with the same *AlfCompiler* instance, then you need to call *registerDependencies* after each parse operation.

```java

```

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p><em>Parsing</em> is the process of creating an abstract syntax representation of some Alf code. If parsing is successful, the Alf compiler also performs constraint checking on the resulting abstract syntax tree. <em>Constraint checking</em> is the process of doing name resolution and validating the Alf code against the static-semantic constraints defined in the Alf specification.</p><p>A compilation takes place in the context of a specific Named Element in the UML model, called the <em>context element</em>. During parsing and constraint checking, name resolution is performed in the scope containing the context element (known, in Alf terms, as the <em>model scope</em>). After the successful mapping of Alf code to UML, the context element is updated with the results of the compilation. The context element should be an Activity, Opaque Behavior, Opaque Action or Opaque Expression</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="494e10fc-220c-4e2a-b0bd-98b9d08fa4aa"><ac:rich-text-body><p>In UML, a Behavior may have a context Classifier (for example, the Class that owns a State Machine as its classifier behavior is the context Classifier for the State Machine). This use of the term &quot;context&quot; is unrelated to the term &quot;context element&quot; for an Alf compilation.</p></ac:rich-text-body></ac:structured-macro><p>To compile some Alf code text, first set the context element using the <em>setContextElement</em> method and then call the <em>parse</em> method, passing the text. What Alf text can be validly parsed depends on what the context element is.</p><ul><li>If the context element is a Value Specification, then the text is assumed to be for an Alf Expression.</li><li>If the context element is an Opaque Action, then the text may be an Alf Expression or Statement Sequence.</li><li>Otherwise the text is assumed to be for an Alf Statement Sequence.</li></ul><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="9e8c9d57-224b-4d62-9e49-cd4d5689f5e0"><ac:rich-text-body><p>The Alf code associated with an Activity, Opaque Behavior, Opaque Action or Opaque Expression is known as the <em>Alf body</em> of that element. The Alf code is saved in the model differently for different kinds of Elements. However, you can use the <em>AlfElementUtil.getAlfBody</em> operation to get the Alf body of an Element (if it has one). </p></ac:rich-text-body></ac:structured-macro><p>After the parsing process completes, you can check if it was successful by calling the <em>isSuccessful</em> method. If the parse is successful, then the resulting abstract syntax tree is rooted in an Alf Unit Definition obtained by calling the <em>getUnit</em> method, which in turn always contains an Activity Definition (which may be obtained by calling the <em>UnitDefinition.getDefinition</em> method). If there were errors, then you can retrieve them using the <em>get</em><em>CompilerErrors</em> method. A single <em>AlfCompiler</em> instance my be used to compile multiple Alf code texts, for the same or different context elements.</p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="9ad16a2d-8894-4280-816c-b63c48c9c437"><ac:rich-text-body><p>Alf abstract syntax classes are found in sub-packages of the package <em>org.modeldriven.alf.syntax,</em> which is from the Alf Reference Implementation, with source available <a href="https://github.com/ModelDriven/Alf-Reference-Implementation/tree/master/org.modeldriven.alf/src/org/modeldriven/alf/syntax">here</a>. These abstract syntax classes allow the abstract syntax tree to be navigated based on the structure of the abstract syntax metamodel defined in the Alf specification. For instance, the value of the <em>definition</em> property of a <em>UnitDefinition</em> is obtained by calling <em>getDefinition,</em> the <em>name</em> of that definition is obtained using <em>getName,</em> etc. (Note that use of the Reference Implementation outside of MagicDraw tooling is subject to its separate open-source licensing terms.)</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target">For the purposes of triggering automatic compilation, the Alf compiler also <a href="https://docs.nomagic.com/display/ALFP2024x/Dependency+Management">manages a record of the dependencies</a> of Alf code in a model on other model elements. After successfully parsing some Alf code, if you want to update the dependency record based on the parse, you need to call the <em>AlfActionUtil.registerDependencies</em> method. If you do multiple parses with the same <em>AlfCompiler</em> instance, then you need to call <em>registerDependencies</em> after each parse operation.</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="8c17cab0-e479-4393-b607-716e92aee94a"><ac:parameter ac:name="language">
       java
      </ac:parameter><ac:plain-text-body><![CDATA[AlfCompiler compiler = new AlfCompiler(); 
compiler.setContextElement(element); 
compiler.parse(AlfElementUtil.getAlfBody(element)); 
if (compiler.isSuccessful()) { 
	AlfActionUtil.registerDependencies(compiler); 
	UnitDefinition unit = compiler.getUnit(); 
	... 
} else { 
	for (CompilerError error: compiler.getCompilerErrors()) { 
		... 
	} 
}]]></ac:plain-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell><ac:layout-cell><p> </p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="two_equal"><ac:layout-cell><p><br /></p></ac:layout-cell><ac:layout-cell><p> </p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=137986191 space=ALFP2024x version=1 -->
## PAGE 00021: Compiler API: Utilities

- page_id: `137986191`
- space_key: `ALFP2024x`
- source_url: https://docs.nomagic.com/spaces/ALFP2024x/pages/137986191/Compiler+API+Utilities
- version_number: 1
- version_date: `2023-09-22T11:48:53.799+02:00`
- ancestors: Alf Plugin Documentation > Developer Guide > Compiler API
- labels: []

### NORMALIZED CONTENT

Instead of explicitly creating an *AlfCompiler* object and using its methods, you can alternatively parse and map Alf code using static methods provided by the *AlfActionUtil* class.

The *AlfActionUtil.parse* method takes a Named Element and, using this as the context element, parses and constraint checks the Alf body of the Element, if it has one. If the parsing and constraint checking succeed, then the method also automatically registers dependencies. The method returns a Boolean indicating whether the parse succeeded or not. If the parse fails, Compiler Errors are reported in an error message that is attached to the context element using an error Annotation (which then becomes available as an Active Validation Result, as described in [the Alf editor](https://docs.nomagic.com/display/ALFP2024x/The+Alf+editor)).

```java

```

The *AlfActionUtil.compile* method takes a Named Element and, using this as the context element, both parses and maps the Alf body of the Element, if it has one. If the compilation is successful, then the method updates the context element and automatically registers dependencies. The method returns a Boolean indicating whether the parse succeeded or not. As with the *parse* method, if the compilation fails, Compiler Errors are recorded in an error message that is attached to the context element using an error Annotation. Unlike the *AlfCompiler.map* and *AlfCompiler.compile*methods, you do not need to explicitly start a MagicDraw session to call the *AlfActionUtil.compile* method, because it ensures internally that a session is started for mapping, if necessary.

```java

```

#### PANEL: Related Pages

Related Pages

- [CONFLUENCE_PAGE title='Compiler API: Parsing' space='ALFP2024x']
- [CONFLUENCE_PAGE title='Compiler API: Mapping' space='ALFP2024x']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p>Instead of explicitly creating an <em>AlfCompiler</em> object and using its methods, you can alternatively parse and map Alf code using static methods provided by the <em>AlfActionUtil</em> class.</p><p>The <em>AlfActionUtil.parse</em> method takes a Named Element and, using this as the context element, parses and constraint checks the Alf body of the Element, if it has one. If the parsing and constraint checking succeed, then the method also automatically registers dependencies. The method returns a Boolean indicating whether the parse succeeded or not. If the parse fails, Compiler Errors are reported in an error message that is attached to the context element using an error Annotation (which then becomes available as an Active Validation Result, as described in <a href="https://docs.nomagic.com/display/ALFP2024x/The+Alf+editor">the Alf editor</a>).</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="33649f26-e83d-42ba-8e21-89c56e23401a"><ac:parameter ac:name="language">
       java
      </ac:parameter><ac:plain-text-body><![CDATA[if (AlfActionUtil.parse(element)) {
	// Parse was successful.
	...
}]]></ac:plain-text-body></ac:structured-macro><p class="auto-cursor-target">The <em>AlfActionUtil.compile</em> method takes a Named Element and, using this as the context element, both parses and maps the Alf body of the Element, if it has one. If the compilation is successful, then the method updates the context element and automatically registers dependencies. The method returns a Boolean indicating whether the parse succeeded or not. As with the <em>parse</em> method, if the compilation fails, Compiler Errors are recorded in an error message that is attached to the context element using an error Annotation. Unlike the <em>AlfCompiler.map</em> and <em>AlfCompiler.compile </em>methods, you do not need to explicitly start a MagicDraw session to call the <em>AlfActionUtil.compile</em> method, because it ensures internally that a session is started for mapping, if necessary.</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="7897edae-bc89-4c24-8ea3-cfb85389e49e"><ac:parameter ac:name="language">
       java
      </ac:parameter><ac:plain-text-body><![CDATA[if (AlfActionUtil.compile(element)) {
	// Compilation was successful.
	...
}]]></ac:plain-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell><ac:layout-cell><p><br /></p><p class="auto-cursor-target"><br /></p><p><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="ec166587-49db-4c7d-9533-92f8b7225bb7"><ac:parameter ac:name="title">
       Related Pages
      </ac:parameter><ac:rich-text-body><ul><li><ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="Compiler API: Parsing" /></ac:link></li><li><ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="Compiler API: Mapping" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro><p><br /></p><p class="auto-cursor-target"><br /></p><p><br /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="two_equal"><ac:layout-cell><p><br /></p></ac:layout-cell><ac:layout-cell><p> </p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=137986167 space=ALFP2024x version=1 -->
## PAGE 00022: Compiling Alf

- page_id: `137986167`
- space_key: `ALFP2024x`
- source_url: https://docs.nomagic.com/spaces/ALFP2024x/pages/137986167/Compiling+Alf
- version_number: 1
- version_date: `2023-09-22T11:48:51.992+02:00`
- ancestors: Alf Plugin Documentation > User Guide
- labels: []

### NORMALIZED CONTENT

Alf code is not executed directly. Rather, it is translated into a UML Activity model, which may then be executed using Cameo Simulation Toolkit. This translation process is known as *compilation.*

Generally, the compilation of Alf code takes place automatically as you enter and edit the code. Alf code may also be recompiled automatically when you change other UML elements in the model on which it depends. However, sometimes it is necessary to manually initiate recompilation of the Alf code in your model, and you can also turn off automatic recompilation, so that it only happens if you specifically request it.

This section provides some information on the Alf compilation process and how you can control it.

#### PANEL: Related pages

Related pages

true

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p>Alf code is not executed directly. Rather, it is translated into a UML Activity model, which may then be executed using Cameo Simulation Toolkit. This translation process is known as <em>compilation.</em></p><p>Generally, the compilation of Alf code takes place automatically as you enter and edit the code. Alf code may also be recompiled automatically when you change other UML elements in the model on which it depends. However, sometimes it is necessary to manually initiate recompilation of the Alf code in your model, and you can also turn off automatic recompilation, so that it only happens if you specifically request it.</p><p>This section provides some information on the Alf compilation process and how you can control it.</p></ac:layout-cell><ac:layout-cell><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="95725424-b2e6-45b5-92ef-83af8abadafb"><ac:parameter ac:name="title">Related pages</ac:parameter><ac:rich-text-body><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="ade23ff2-2cb8-4795-b6b3-158de0134344"><ac:parameter ac:name="all">true</ac:parameter></ac:structured-macro></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=137986213 space=ALFP2024x version=1 -->
## PAGE 00023: Creating AddressBook operations

- page_id: `137986213`
- space_key: `ALFP2024x`
- source_url: https://docs.nomagic.com/spaces/ALFP2024x/pages/137986213/Creating+AddressBook+operations
- version_number: 1
- version_date: `2023-09-22T11:48:56.336+02:00`
- ancestors: Alf Plugin Documentation > Tutorials > Alf Tutorial 2: Address Book
- labels: []

### NORMALIZED CONTENT

We will now add two operations to the *AddressBook* class, one to put an entry into an *AddressBook* and another to look up an address for a name.

To add a *put* Operation to *AddressBook*

1. Click on the AddressBook symbol on the Class Diagram. Click on the little Create Element button at the top right of the Class symbol, and select Operation .
2. Type put as the name of the Operation and, inside the parentheses , type the parameter list name: String, address: String, then press Return .
3. Click on the new put Operation, and, in the [CONFLUENCE_PAGE title='The Alf editor' space='ALFP2024x'] window, press Create .
4. Type the Alf code shown in the following figure. [IMAGE alt='' src='']
5. When the text is correct, press Save .

To add a *get* Operation to *AddressBook*

1. Click on the AddressBook symbol on the Class diagram. Click on the little Create Operation button to the top right of the Operations compartment.
2. For the operation and its signature, enter get(name: Sting): String[0..1] and press Return . (Make sure you don't leave the default "()" at the end of what you enter.)
3. Click on the get Operation, and, in the [CONFLUENCE_PAGE title='The Alf editor' space='ALFP2024x'] window, press Create .
4. Type the Alf code shown in the following figure. [IMAGE alt='' src='']
5. When the text is correct, press Save.

You may want to consider yourself how to code a *remove(name: String)* Operation that removes an entry from an *AddressBook.*

Next: [CONFLUENCE_PAGE title='Testing the AddressBook' space='ALFP2024x']

#### PANEL: Related Pages

Related Pages

- [CONFLUENCE_PAGE title='The Alf editor' space='ALFP2024x']
- [CONFLUENCE_PAGE title='Using Alf for Operation methods' space='ALFP2024x']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p>We will now add two operations to the <em>AddressBook</em> class, one to put an entry into an <em>AddressBook</em> and another to look up an address for a name.</p><p><br /></p><p>To add a <em>put</em> Operation to <em>AddressBook</em></p><hr /><ol><li>Click on the <em>AddressBook</em> symbol on the Class Diagram. Click on the little <strong>Create Element</strong> button at the top right of the Class symbol, and select<strong> Operation</strong>.</li><li>Type <em>put</em> as the name of the Operation and, <em>inside the parentheses</em>, type the parameter list <em>name: String, address: String,</em> then press <strong>Return</strong>.</li><li>Click on the new <em>put</em> Operation, and, in the <ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="The Alf editor" /><ac:plain-text-link-body><![CDATA[Alf editor]]></ac:plain-text-link-body></ac:link> window, press <strong>Create</strong>.</li><li><p class="auto-cursor-target">Type the Alf code shown in the following figure.</p><p class="auto-cursor-target"><ac:image><ri:attachment ri:filename="Address_Book-Creating_AddressBook_put.png"><ri:page ri:space-key="ALFP2024x" ri:content-title="Creating AddressBook operations" /></ri:attachment></ac:image><br /><br /></p></li><li>When the text is correct, press <strong>Save</strong>.</li></ol><p><br /></p><p>To add a <em>get</em> Operation to <em>AddressBook</em></p><hr /><ol><li>Click on the <em>AddressBook</em> symbol on the Class diagram. Click on the little <strong>Create Operation</strong> button to the top right of the <em>Operations</em> compartment.</li><li>For the operation and its signature, enter <em>get(name: Sting): String[0..1]</em> and press <strong>Return</strong>. (Make sure you don't leave the default &quot;()&quot; at the end of what you enter.)</li><li>Click on the <em>get</em> Operation, and, in the <ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="The Alf editor" /><ac:plain-text-link-body><![CDATA[Alf editor]]></ac:plain-text-link-body></ac:link> window, press <strong>Create</strong>.</li><li><p class="auto-cursor-target">Type the Alf code shown in the following figure.</p><p class="auto-cursor-target"><ac:image><ri:attachment ri:filename="Address_Book-Creating_AddressBook_get.png"><ri:page ri:space-key="ALFP2024x" ri:content-title="Creating AddressBook operations" /></ri:attachment></ac:image><br /><br /></p></li><li>When the text is correct, press <strong>Save.</strong></li></ol><p><br /></p><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="434f90eb-b19b-45e2-bb8d-b1b2794c1eb0"><ac:rich-text-body><p>You may want to consider yourself how to code a <em>remove(name: String)</em> Operation that removes an entry from an <em>AddressBook.</em></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><p>Next: <ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="Testing the AddressBook" /></ac:link></p></ac:layout-cell><ac:layout-cell><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="bdf60a57-efef-4319-9e4d-839e1cb78d51"><ac:parameter ac:name="title">Related Pages</ac:parameter><ac:rich-text-body><ul><li><ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="The Alf editor" /></ac:link></li><li><ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="Using Alf for Operation methods" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=137986199 space=ALFP2024x version=1 -->
## PAGE 00024: Creating an Alf project for Hello World

- page_id: `137986199`
- space_key: `ALFP2024x`
- source_url: https://docs.nomagic.com/spaces/ALFP2024x/pages/137986199/Creating+an+Alf+project+for+Hello+World
- version_number: 1
- version_date: `2023-09-22T11:48:54.985+02:00`
- ancestors: Alf Plugin Documentation > Tutorials > Alf Tutorial 1: Hello World
- labels: []

### NORMALIZED CONTENT

A project in which Alf is to be used should be created from the [CONFLUENCE_PAGE title='Alf project template' space='ALFP2024x'], to ensure that all necessary library models are included.

To create a new Alf project.

1. Select**File** > **New Project** on the main menu. The **New Project** dialog will open (see the following figure). [IMAGE alt='' src='']
2. On the bottom left, select Project from Template from the Other group (you may need to scroll down).
3. On the bottom right, under Select template , open the Alf folder and select Alf .
4. Enter the project name Hello World and a project location.
5. Click OK .

Next: [CONFLUENCE_PAGE title='Creating the Hello World activity' space='ALFP2024x']

#### PANEL: Related pages

Related pages

- [CONFLUENCE_PAGE title='Alf project template' space='ALFP2024x']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p>A project in which Alf is to be used should be created from the <ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="Alf project template" /></ac:link>, to ensure that all necessary library models are included.</p><p><br /></p><p>To create a new Alf project.</p><hr /><ol><li><p class="auto-cursor-target">Select<strong> File</strong> &gt; <strong>New Project</strong> on the main menu. The <strong>New Project</strong> dialog will open (see the following figure).</p><p class="auto-cursor-target"><ac:image><ri:attachment ri:filename="AlfProjectTemplate-NewProject.png"><ri:page ri:space-key="ALFP2024x" ri:content-title="Alf project template" /></ri:attachment></ac:image></p></li><li>On the bottom left, select <strong>Project from Template</strong> from the <strong>Other</strong> group (you may need to scroll down).</li><li>On the bottom right, under <strong>Select template</strong>, open the <strong>Alf</strong> folder and select <strong>Alf</strong>.</li><li>Enter the project name <em>Hello World </em>and a project location.</li><li>Click <strong>OK</strong>.</li></ol><p><br /></p><p>Next: <ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="Creating the Hello World activity" /></ac:link></p></ac:layout-cell><ac:layout-cell><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="ab616d93-ccff-4934-9fd4-84182722ffde"><ac:parameter ac:name="title">Related pages</ac:parameter><ac:rich-text-body><ul><li><ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="Alf project template" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=137986211 space=ALFP2024x version=1 -->
## PAGE 00025: Creating an Entry constructor

- page_id: `137986211`
- space_key: `ALFP2024x`
- source_url: https://docs.nomagic.com/spaces/ALFP2024x/pages/137986211/Creating+an+Entry+constructor
- version_number: 1
- version_date: `2023-09-22T11:48:56.146+02:00`
- ancestors: Alf Plugin Documentation > Tutorials > Alf Tutorial 2: Address Book
- labels: []

### NORMALIZED CONTENT

By default, when an instance of class is created using an Alf expression of the form *new ClassName()*, each attribute of the new instance has its default value, if this is specified for it, and is null otherwise. However, sometimes it is desirable to perform additional initialization behavior on a newly created instance, beyond just the default initialization. You can do this by defining a *constructor* operation.

A constructor operation is created like any other operation, but it must then have the standard *Create* stereotype applied. A class may have any number of constructors. Conventionally, a constructor often has the same name as the class (which, in Alf, is considered the default), but, in UML, this is not required – constructors can have any name. An Alf instance creation expression identifies a specific constructor to use, with a slightly simplified syntax for the case in which the constructor name is the same as the class name.

In the Address Book model, it will be useful for the *Entry* class to have a constructor operation, so that values can be provided for the *name* and *address* attributes of a new instance when it is created.

To create an *Entry* constructor

1. Click on the little Create Element button at the top right of the Entry symbol on the Class diagram, and select Operation.
2. Type Entry as the name of the Operation, and, inside the parentheses , type the parameter list name: String, address: String, then press Return .
3. Right click on the new Operation, and select Stereotype .
4. Check the Create Stereotype, and click on Apply .
5. With the Entry Operation still selected, open the Alf editor window (select Windows > Alf ), if it isn't already open, and press Create .
6. In the [CONFLUENCE_PAGE title='The Alf editor' space='ALFP2024x'], type the statements shown in the following figure. [ATTACHMENT filename='Address_Book-Creating_Entry_Constructor.png']
7. When the text is correct, press Save .

If you define an explicit constructor operation for a class, then default construction is no longer allowed. For example, since the *Entry* Class now has an explicit constructor, the expression *new Entry()* is no longer legal. You must use the explicit constructor, with *name* and *address* arguments. However, if desired, you can still define an explicit constructor that looks like a default constructor, having the same name as its class and no arguments. Thus, if you added a constructor *Entry()*, with no Parameters, to the *Entry* Class (overloading the constructor of the same name with Parameters), then it would be legal again to code *new Entry()*, which would call the explicit constructor with no Parameters.

Next: [CONFLUENCE_PAGE title='Creating AddressBook operations' space='ALFP2024x']

#### PANEL: Related pages

Related pages

- [CONFLUENCE_PAGE title='The Alf editor' space='ALFP2024x']
- [CONFLUENCE_PAGE title='Using Alf for Operation methods' space='ALFP2024x']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p>By default, when an instance of class is created using an Alf expression of the form <em>new ClassName()</em>, each attribute of the new instance has its default value, if this is specified for it, and is null otherwise. However, sometimes it is desirable to perform additional initialization behavior on a newly created instance, beyond just the default initialization. You can do this by defining a <em>constructor</em> operation.</p><p>A constructor operation is created like any other operation, but it must then have the standard <em>Create</em> stereotype applied. A class may have any number of constructors. Conventionally, a constructor often has the same name as the class (which, in Alf, is considered the default), but, in UML, this is not required – constructors can have any name. An Alf instance creation expression identifies a specific constructor to use, with a slightly simplified syntax for the case in which the constructor name is the same as the class name.</p><p>In the Address Book model, it will be useful for the <em>Entry</em> class to have a constructor operation, so that values can be provided for the <em>name</em> and <em>address</em> attributes of a new instance when it is created.</p><p><br /></p><p>To create an <em>Entry</em> constructor</p><hr /><ol><li>Click on the little <strong>Create Element</strong> button at the top right of the <em>Entry</em> symbol on the Class diagram, and select <strong>Operation.</strong></li><li>Type <em>Entry</em> as the name of the Operation, and, <em>inside the parentheses</em>, type the parameter list <em>name: String, address: String,</em> then press <strong>Return</strong>.</li><li>Right click on the new Operation, and select <strong>Stereotype</strong>.</li><li>Check the <strong>Create</strong> Stereotype, and click on <strong>Apply</strong>.</li><li>With the <em>Entry</em> Operation still selected, open the Alf editor window (select <strong>Windows &gt; Alf</strong>), if it isn't already open, and press <strong>Create</strong>.</li><li><p class="auto-cursor-target">In the <ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="The Alf editor" /><ac:plain-text-link-body><![CDATA[Alf editor]]></ac:plain-text-link-body></ac:link>, type the statements shown in the following figure.<br /><br /></p><ac:image><ri:attachment ri:filename="Address_Book-Creating_Entry_Constructor.png"><ri:page ri:space-key="ALFP2024x" ri:content-title="Creating an Entry constructor" /></ri:attachment></ac:image><br /><br /></li><li>When the text is correct, press <strong>Save</strong>.</li></ol><p><br /></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="5b59fdab-4bf1-42d7-9151-88686d454a6c"><ac:rich-text-body><p>If you define an explicit constructor operation for a class, then default construction is no longer allowed. For example, since the <em>Entry</em> Class now has an explicit constructor, the expression <em>new Entry()</em> is no longer legal. You must use the explicit constructor, with <em>name</em> and <em>address</em> arguments. However, if desired, you can still define an explicit constructor that looks like a default constructor, having the same name as its class and no arguments. Thus, if you added a constructor <em>Entry()</em>, with no Parameters, to the <em>Entry</em> Class (overloading the constructor of the same name with Parameters), then it would be legal again to code <em>new Entry()</em>, which would call the explicit constructor with no Parameters.</p></ac:rich-text-body></ac:structured-macro><p><span style="color: rgb(0,51,102);">Next: <ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="Creating AddressBook operations" /></ac:link><br /></span></p></ac:layout-cell><ac:layout-cell><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="a9102805-045c-40c4-b248-5748408b8019"><ac:parameter ac:name="title">Related pages</ac:parameter><ac:rich-text-body><ul><li><ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="The Alf editor" /></ac:link></li><li><ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="Using Alf for Operation methods" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=137986209 space=ALFP2024x version=1 -->
## PAGE 00026: Creating Entry attributes

- page_id: `137986209`
- space_key: `ALFP2024x`
- source_url: https://docs.nomagic.com/spaces/ALFP2024x/pages/137986209/Creating+Entry+attributes
- version_number: 1
- version_date: `2023-09-22T11:48:55.940+02:00`
- ancestors: Alf Plugin Documentation > Tutorials > Alf Tutorial 2: Address Book
- labels: []

### NORMALIZED CONTENT

An *Entry* comprises a name and an address for that name. For our simple model, we will represent this data using *name* and *address* attributes of *Entry,* both of type *String.*

To create the *Entry* attributes

1. Click the Entry Class symbol in the Class diagram.
2. Click on the small Create Element button on the right side of the Entry Class symbol, and select Property . A new attribute will be created.
3. Type name: String to define the new attribute, and press Return .
4. Right click on the name attribute and select the visibility public .
5. Click on the small Create Property button on the right side of the attributes compartment to create another attribute.
6. Type address: Strin g to define the new attribute, and press Return .
7. Right click on the *address* attribute and select the visibility **public**. [ATTACHMENT filename='Address_Book-Creating_Entry_Attributes.png']

Next: [CONFLUENCE_PAGE title='Creating an Entry constructor' space='ALFP2024x']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p>An <em>Entry</em> comprises a name and an address for that name. For our simple model, we will represent this data using <em>name</em> and <em>address</em> attributes of <em>Entry,</em> both of type <em>String.</em></p><p><br /></p><p>To create the <em>Entry</em> attributes</p><hr /><ol><li>Click the <em>Entry</em> Class symbol in the Class diagram.</li><li>Click on the small <strong>Create Element</strong> button on the right side of the <em>Entry</em> Class symbol, and select <strong>Property</strong>. A new attribute will be created.</li><li>Type <em>name: String</em> to define the new attribute, and press <strong>Return</strong>.</li><li>Right click on the <em>name</em> attribute and select the visibility <strong>public</strong>.</li><li>Click on the small <strong>Create Property</strong> button on the right side of the <em>attributes</em> compartment to create another attribute.</li><li>Type <em>address: Strin</em><em>g</em> to define the new attribute, and press <strong>Return</strong>.</li><li><p class="auto-cursor-target">Right click on the <em>address</em> attribute and select the visibility <strong>public</strong>.</p><ac:image><ri:attachment ri:filename="Address_Book-Creating_Entry_Attributes.png"><ri:page ri:space-key="ALFP2024x" ri:content-title="Creating Entry attributes" /></ri:attachment></ac:image><p class="auto-cursor-target"><br /></p></li></ol><p>Next: <ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="Creating an Entry constructor" /></ac:link></p></ac:layout-cell><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=137986207 space=ALFP2024x version=1 -->
## PAGE 00027: Creating the Address Book class diagram

- page_id: `137986207`
- space_key: `ALFP2024x`
- source_url: https://docs.nomagic.com/spaces/ALFP2024x/pages/137986207/Creating+the+Address+Book+class+diagram
- version_number: 1
- version_date: `2023-09-22T11:48:55.784+02:00`
- ancestors: Alf Plugin Documentation > Tutorials > Alf Tutorial 2: Address Book
- labels: []

### NORMALIZED CONTENT

The Address Book model consists of an *AddressBook* class associated with an Entry class. We will create these classes on a Class diagram.

To create the *Address Book* class diagram

1. Create a new Alf project as described in [CONFLUENCE_PAGE title='Alf project template' space='ALFP2024x'] , using the name Address Book for the project.
2. In the new project, click the Create Diagram button on the toolbar and select Class Diagram . Name the diagram Address Book .
3. Use the **Class Diagram** toolbar to create a new Class named *AddressBook.* For simplicity in later code, we are using camel case for the class name here, with no space between "Address" and "Book".
4. Create a another new Class named Entry.
5. Click on the [ATTACHMENT filename='show_filters.png'] next to Composition on the Class Diagram toolbar and select Directed Composition .
6. Draw an Association from AddressBook to Entry on the Class diagram.
7. Right click on the Entry end of the Association and select Edit Name .
8. Type *entries* for the Association end name.
9. Right click on the *entries* Association end and select the multiplicity **0..***. [IMAGE alt='' src='']

Next: [CONFLUENCE_PAGE title='Creating Entry attributes' space='ALFP2024x']

#### PANEL: Related pages

Related pages

- [CONFLUENCE_PAGE title='Alf project template' space='ALFP2024x']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p>The Address Book model consists of an <em>AddressBook</em> class associated with an Entry class. We will create these classes on a Class diagram.</p><p><br /></p><p>To create the <em>Address Book</em> class diagram</p><hr /><ol><li>Create a new Alf project as described in <ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="Alf project template" /></ac:link>, using the name <em>Address Book</em> for the project.</li><li>In the new project, click the <strong>Create Diagram</strong> button on the toolbar and select <strong>Class Diagram</strong>. Name the diagram <em>Address Book</em><em>.</em></li><li><p class="auto-cursor-target">Use the <strong>Class Diagram</strong> toolbar to create a new Class named <em>AddressBook.</em></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="695d985e-60c8-4750-aadf-d6badb2fd071"><ac:rich-text-body><p>For simplicity in later code, we are using camel case for the class name here, with no space between &quot;Address&quot; and &quot;Book&quot;.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></li><li>Create a another new Class named <em>Entry.</em></li><li>Click on the <ac:image ac:thumbnail="true" ac:height="15"><ri:attachment ri:filename="show_filters.png"><ri:page ri:space-key="CCTWRT" ri:content-title="_Buttons" /></ri:attachment></ac:image> next to <strong>Composition</strong> on the <strong>Class Diagram</strong> toolbar and select <strong>Directed Composition</strong>.</li><li>Draw an Association from <em>AddressBook</em> to <em>Entry</em> on the Class diagram.</li><li>Right click on the <em>Entry</em> end of the Association and select <strong>Edit Name</strong>.</li><li><p class="auto-cursor-target">Type <em>entries</em> for the Association end name.</p></li><li><p class="auto-cursor-target">Right click on the <em>entries</em> Association end and select the multiplicity <strong>0..*</strong>.</p><p class="auto-cursor-target"><ac:image><ri:attachment ri:filename="Address_Book-Creating_Classes.png"><ri:page ri:space-key="ALFP2024x" ri:content-title="Creating the Address Book class diagram" /></ri:attachment></ac:image></p></li></ol><p>Next: <ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="Creating Entry attributes" /></ac:link></p></ac:layout-cell><ac:layout-cell><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="55172402-6d50-4c60-a2d4-72c4d61dd456"><ac:parameter ac:name="title">Related pages</ac:parameter><ac:rich-text-body><ul><li><ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="Alf project template" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=137986200 space=ALFP2024x version=1 -->
## PAGE 00028: Creating the Hello World activity

- page_id: `137986200`
- space_key: `ALFP2024x`
- source_url: https://docs.nomagic.com/spaces/ALFP2024x/pages/137986200/Creating+the+Hello+World+activity
- version_number: 1
- version_date: `2023-09-22T11:48:55.102+02:00`
- ancestors: Alf Plugin Documentation > Tutorials > Alf Tutorial 1: Hello World
- labels: []

### NORMALIZED CONTENT

To define a new activity using Alf, first the Activity needs to be created in the model, and then Alf code needs to be written for it and compiled.

To create the *Hello World* Activity

1. Right click on the root Model and select Create Element > Activity .
2. Enter the name *Hello World*. [IMAGE alt='' src='']

To create an Alf body for *Hello World*

1. Select the new Activity in the Model Browser and open the Alf editor window (select **Windows > Alf**), if it isn't already open.
2. In the [CONFLUENCE_PAGE title='The Alf editor' space='ALFP2024x'] window, type *WriteLine("Hello World!");*``
3. If there are any errors in your code, fix them.
4. When the code is entered correctly, click the **Save** button. The Alf code will be compiled into Activity Nodes and Edges within the selected Activity. 
 
[IMAGE alt='' src='']

Next: [CONFLUENCE_PAGE title='Running the Hello World activity' space='ALFP2024x']

#### PANEL: Related pages

Related pages

- [CONFLUENCE_PAGE title='Working with Alf' space='ALFP2024x']
  - [CONFLUENCE_PAGE title='The Alf editor' space='ALFP2024x']
  - [CONFLUENCE_PAGE title='Using Alf to define Activities' space='ALFP2024x']
- [CONFLUENCE_PAGE title='Compiling Alf' space='ALFP2024x']
  - [CONFLUENCE_PAGE title='The Alf compiler' space='ALFP2024x']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p>To define a new activity using Alf, first the Activity needs to be created in the model, and then Alf code needs to be written for it and compiled.</p><p><br /></p><p>To create the <em>Hello World</em> Activity</p><hr /><ol><li>Right click on the root <em>Model</em> and select <strong>Create Element</strong> &gt; <strong>Activity</strong>.</li><li><p>Enter the name <em>Hello World</em>.</p><p class="auto-cursor-target"><ac:image><ri:attachment ri:filename="Hello_World-Creating_Activity.png"><ri:page ri:space-key="ALFP2024x" ri:content-title="Creating the Hello World activity" /></ri:attachment></ac:image></p></li></ol><p><br /></p><p>To create an Alf body for <em>Hello World</em></p><hr /><ol><li><p class="auto-cursor-target">Select the new Activity in the Model Browser and open the Alf editor window (select <strong>Windows &gt; Alf</strong>), if it isn't already open.</p></li><li><p class="auto-cursor-target">In the <ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="The Alf editor" /><ac:plain-text-link-body><![CDATA[Alf editor]]></ac:plain-text-link-body></ac:link> window, type <em>WriteLine(&quot;Hello World!&quot;);</em><code> <br /></code></p></li><li>If there are any errors in your code, fix them.</li><li><p class="auto-cursor-target">When the code is entered correctly, click the <strong>Save</strong> button. The Alf code will be compiled into Activity Nodes and Edges within the selected Activity.<br /><br /><ac:image><ri:attachment ri:filename="Hello_World-Creating_Alf_Body.png"><ri:page ri:space-key="ALFP2024x" ri:content-title="Creating the Hello World activity" /></ri:attachment></ac:image></p></li></ol><p><br /></p><p>Next: <ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="Running the Hello World activity" /></ac:link></p></ac:layout-cell><ac:layout-cell><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="ba3cafe6-d881-42db-b28d-c9cc4b02bda0"><ac:parameter ac:name="title">Related pages</ac:parameter><ac:rich-text-body><ul><li><ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="Working with Alf" /></ac:link><ul><li><ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="The Alf editor" /></ac:link></li><li class="confluence-link"><ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="Using Alf to define Activities" /></ac:link></li></ul></li><li><ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="Compiling Alf" /></ac:link><ul><li><ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="The Alf compiler" /></ac:link></li></ul></li></ul></ac:rich-text-body></ac:structured-macro><br /><p> </p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=137986226 space=ALFP2024x version=1 -->
## PAGE 00029: Creating the StopWatch state machine

- page_id: `137986226`
- space_key: `ALFP2024x`
- source_url: https://docs.nomagic.com/spaces/ALFP2024x/pages/137986226/Creating+the+StopWatch+state+machine
- version_number: 1
- version_date: `2023-09-22T11:48:57.510+02:00`
- ancestors: Alf Plugin Documentation > Tutorials > Alf Tutorial 3: Stopwatch
- labels: []

### NORMALIZED CONTENT

Now that you have created the *StopWatch* Class, next create a State Machine to be its classifier behavior. This State Machine defines the active behavior of a *StopWatch,* which may be executed using Cameo SImulation Toolkit. 
 
 To define the State Machine for the *StopWatch* class

1. Right click on the StopWatch symbol on the Class diagram and select Create Diagram > State Machine Diagram . A new State Machine element will be created under the StopWatch class with a new State Machine diagram.
2. Make sure that the StopWatch state machine is the classifier behavior of the StopWatch class. To see the classifier behavior of the StopWatch class, right click on the StopWatch symbol in the Model Browser and select Specification from the context menu. The Specification window will open.
3. Select **All** from the **Properties** drop-down menu (see the following figure).
4. Scroll down to see the Classifier Behavior row and you will see that the classifier behavior of the StopWatch Class is defined by the StopWatch State Machine (see the following figure). (If it is not, then click on the Classifier Behavior property and choose the StopWatch State Machine to be the classifier behavior.) [ATTACHMENT filename='Stopwatch-Checking_Classifier_Behavior.png']

Now create the States and Transitions for the *StopWatch* State Machine.

To add the *ready, running, paused,* and *stopped* States

1. The State Machine diagram is automatically created with an initial Pseudostate having a Transition to a starting State. Name the starting State *ready* (see the following figure). [ATTACHMENT filename='Stopwatch-Creating_State_ready.png']
2. Click State on the State Machine Diagram toolbar, and then click any area on the diagram to place a State. Name the created State running (see the following figure).
3. Repeat Step 2 to create the paused , and stopped states. [ATTACHMENT filename='Stopwatch-Creating_Other_States.png']

To add a Final State to the State Machine diagram

- Click Final State on the State Machine Diagram toolbar, and then click any area on the diagram to place the Final State (see the following figure). [ATTACHMENT filename='Stopwatch-Creating_Final_State.png']

Next you need to add Transitions between the States on the State Machine diagram. 
 
To add Transitions to the State Machine diagram

1. Click on a State (e.g., the ready state) that will be the source of the Transition to be created. The smart manipulator toolbar will open (see the following figure).
2. Click the **Transition** icon on the smart manipulator toolbar (see the following figure). [IMAGE alt='' src='']
3. Click a State (e.g., the *running* State) that will be the target of the Transition (see the following figure). [IMAGE alt='' src='']
4. Repeat Steps 1 to 3 to create more transitions between the following states (see the following figure): from the running State to the paused State from the running State to the stopped State from the paused State to the running State from the paused State to the stopped State from the stopped State to the ready State from the stopped State to the final State [ATTACHMENT filename='Stopwatch-Creating_Other_Transitions.png']
5. Create a looping transition to the running state by clicking the Transition to Self icon on the smart manipulator toolbar (see the following figure). [ATTACHMENT filename='Stopwatch-Creating_Transition_To_Self.png']
6. Now your StopWatch State Machine diagram will look similar to the the following figure. [ATTACHMENT filename='Stopwatch-All_Transitions.png']

Some of the Transitions just created will have Signal Event triggers. These triggers reference Signal elements, which will be stored in a separate Package. You can add a Package and create the Signal elements by using the Model Browser context menu. 
 
To add a new Package for the Signal elements

1. Right click on the Model node in the Model Browser and select Create Element > Package .
2. Name the created Package signals (see the following figure). [ATTACHMENT filename='Stopwatch-Creating_Package_signals.png']

To create Signal elements

1. Right click on the signals Package and select Create Element > Signal . (If you don't see an entry for Signal , click on Expert in the lower left-hand corner of the Create Element window.)
2. Name the created Signal reset . The reset Signal will be created and stored in the signals Package.
3. Repeat steps 1 and 2 to create the split, start, stop, and unsplit Signal elements (see the following figure). [ATTACHMENT filename='Stopwatch-Creating_Signals.png']

To create Signal Events for the Transitions on the *StopWatch* State Machine diagram

- Drag a signal element from the Model Browser to a transition on the State Machine diagram (see the following figure). The Signal Event will later be specified as the trigger of the Transition. [ATTACHMENT filename='Stopwatch-Dragging_Signal.png']

To create a Signal Event for each Transition (see the following figure)

1. Drag the start Signal to the Transition between the ready and running States.
2. Drag the split Signal to the Transition between the running and paused States.
3. Drag the stop Signal to the Transition between the running and stopped States.
4. Drag the unsplit Signal to the Transition between the paused and running States.
5. Drag the stop Signal to the Transition between the paused and stopped States.
6. Drag the reset Signal to the Transition between the stopped and ready States.
7. Drag the stop Signal to the Transition between the stopped and final States. [ATTACHMENT filename='Stopwatch-All_Triggers.png']

Now each and every Transition between the States has its own Signal Event. Next, you will also need to create a Time Event for the **Transition****to****Self** of the *running* State.

To create a Time Event for the **Transition****to****Self**of the *running* state

1. Right click the Transition to Self of the running state and select Specification to open its Specification window.
2. Click the Categorized View button to open the properties of the transition in the categorized view (see the following figure).
3. Click the Event Type row in the Trigger category and select TimeEvent from the drop-down menu (see the following figure). [ATTACHMENT filename='Stopwatch-Creating_Time_Event.png']
4. Click the When row in the Trigger category and type "1s" to specify that the Time Event will occur every second (see the following figure).
5. Check the Is Relative box, so it is true (see the following figure). [ATTACHMENT filename='Stopwatch-Specifying_Time_Event.png']
6. Click Close . Your State Machine should look similar to the following figure. [ATTACHMENT filename='Stopwatch-With_Time_Event.png']

Next: [CONFLUENCE_PAGE title='Defining the Stopwatch operations using Alf' space='ALFP2024x']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p>Now that you have created the <em>StopWatch</em> Class, next create a State Machine to be its classifier behavior. This State Machine defines the active behavior of a <em>StopWatch,</em> which may be executed using Cameo SImulation Toolkit.<br class="atl-forced-newline" /> <br class="atl-forced-newline" /> To define the State Machine for the <em>StopWatch</em> class</p><hr /><ol><li>Right click on the <em>StopWatch</em> symbol on the Class diagram and select <strong>Create Diagram</strong> &gt; <strong>State Machine Diagram</strong>. A new State Machine element will be created under the <em>StopWatch</em> class with a new State Machine diagram.</li><li>Make sure that the <em>StopWatch</em> state machine is the classifier behavior of the <em>StopWatch</em> class. To see the classifier behavior of the <em>StopWatch</em> class, right click on the <em>StopWatch</em> symbol in the Model Browser and select <strong>Specification</strong> from the context menu. The Specification window will open.</li><li><p>Select <strong>All</strong> from the <strong>Properties</strong> drop-down menu (see the following figure).</p></li><li>Scroll down to see the <strong>Classifier</strong><strong> Behavior</strong> row and you will see that the classifier behavior of the <em>StopWatch</em> Class is defined by the <em>StopWatch</em> State Machine (see the following figure). (If it is not, then click on the <strong>Classifier Behavior</strong> property and choose the <em>StopWatch</em> State Machine to be the classifier behavior.)<br /><br /><ac:image><ri:attachment ri:filename="Stopwatch-Checking_Classifier_Behavior.png"><ri:page ri:space-key="ALFP2024x" ri:content-title="Creating the StopWatch state machine" /></ri:attachment></ac:image></li></ol><p><br /></p><p>Now create the States and Transitions for the <em>StopWatch</em> State Machine.</p><p><br /></p><p>To add the <em>ready, running, paused,</em> and <em>stopped</em> States</p><hr /><ol><li><p class="auto-cursor-target">The State Machine diagram is automatically created with an initial Pseudostate having a Transition to a starting State. Name the starting State <em>ready</em> (see the following figure).<br /><br /></p><ac:image ac:height="400"><ri:attachment ri:filename="Stopwatch-Creating_State_ready.png"><ri:page ri:space-key="ALFP2024x" ri:content-title="Creating the StopWatch state machine" /></ri:attachment></ac:image><br /><br /></li><li>Click <strong>State</strong> on the State Machine Diagram toolbar, and then click any area on the diagram to place a State. Name the created State <em>running</em> (see the following figure).</li><li>Repeat Step 2 to create the <em>paused</em>, and <em>stopped</em> states. <br /><br /><ac:image ac:height="400"><ri:attachment ri:filename="Stopwatch-Creating_Other_States.png"><ri:page ri:space-key="ALFP2024x" ri:content-title="Creating the StopWatch state machine" /></ri:attachment></ac:image></li></ol><p><br class="atl-forced-newline" />To add a Final State to the State Machine diagram</p><hr /><ul><li>Click <strong>Final </strong><strong>State</strong> on the State Machine Diagram toolbar, and then click any area on the diagram to place the Final State (see the following figure). <br /><br /><ac:image ac:height="400"><ri:attachment ri:filename="Stopwatch-Creating_Final_State.png"><ri:page ri:space-key="ALFP2024x" ri:content-title="Creating the StopWatch state machine" /></ri:attachment></ac:image></li></ul><p><br /> Next you need to add Transitions between the States on the State Machine diagram. <br class="atl-forced-newline" /><br class="atl-forced-newline" />To add Transitions to the State Machine diagram</p><hr /><ol><li>Click on a State (e.g., the <em>ready</em> state) that will be the source of the Transition to be created. The smart manipulator toolbar will open (see the following figure).</li><li><p class="auto-cursor-target">Click the <strong>Transition</strong> icon on the smart manipulator toolbar (see the following figure).</p><p class="auto-cursor-target"><ac:image><ri:attachment ri:filename="Stopwatch-Starting_Transition.png"><ri:page ri:space-key="ALFP2024x" ri:content-title="Creating the StopWatch state machine" /></ri:attachment></ac:image></p></li><li><p class="auto-cursor-target">Click a State (e.g., the <em>running</em> State) that will be the target of the Transition (see the following figure).</p><p class="auto-cursor-target"><ac:image><ri:attachment ri:filename="Stopwatch-Finishing_Transition.png"><ri:page ri:space-key="ALFP2024x" ri:content-title="Creating the StopWatch state machine" /></ri:attachment></ac:image><br /><br /></p></li><li>Repeat Steps 1 to 3 to create more transitions between the following states (see the following figure): <br /><br />from the <em>running</em> State to the <em>paused</em> State <br class="atl-forced-newline" />from the <em>running</em> State to the <em>stopped</em> State <br class="atl-forced-newline" />from the <em>paused</em> State to the <em>running</em> State <br class="atl-forced-newline" />from the <em>paused</em> State to the <em>stopped</em> State <br class="atl-forced-newline" />from the <em>stopped</em> State to the <em>ready</em> State <br class="atl-forced-newline" />from the <em>stopped</em> State to the final State<br /><br /><ac:image><ri:attachment ri:filename="Stopwatch-Creating_Other_Transitions.png"><ri:page ri:space-key="ALFP2024x" ri:content-title="Creating the StopWatch state machine" /></ri:attachment></ac:image><br /><br /></li><li>Create a looping transition to the <em>running</em> state by clicking the <strong>Transition</strong><strong> to</strong><strong> Self</strong> icon on the smart manipulator toolbar (see the following figure).<br /> <br /><ac:image ac:thumbnail="true" ac:height="104"><ri:attachment ri:filename="Stopwatch-Creating_Transition_To_Self.png"><ri:page ri:space-key="ALFP2024x" ri:content-title="Creating the StopWatch state machine" /></ri:attachment></ac:image><br /><br /></li><li>Now your <em>StopWatch</em> State Machine diagram will look similar to the the following figure. <br /><br /><ac:image><ri:attachment ri:filename="Stopwatch-All_Transitions.png"><ri:page ri:space-key="ALFP2024x" ri:content-title="Creating the StopWatch state machine" /></ri:attachment></ac:image></li></ol><p><br /></p><p>Some of the Transitions just created will have Signal Event triggers. These triggers reference Signal elements, which will be stored in a separate Package. You can add a Package and create the Signal elements by using the Model Browser context menu.<br class="atl-forced-newline" /><br class="atl-forced-newline" />To add a new Package for the Signal elements</p><hr /><ol><li>Right click on the <em>Model</em> node in the Model Browser and select <strong>Create Element</strong> &gt; <strong>Package</strong>.</li><li>Name the created Package <em>signals</em> (see the following figure). <br /><br /><ac:image ac:height="400"><ri:attachment ri:filename="Stopwatch-Creating_Package_signals.png"><ri:page ri:space-key="ALFP2024x" ri:content-title="Creating the StopWatch state machine" /></ri:attachment></ac:image></li></ol><p><br class="atl-forced-newline" />To create Signal elements</p><hr /><ol><li>Right click on the <em>signals</em> Package and select <strong>Create Element</strong> &gt; <strong>Signal</strong>. (If you don't see an entry for <strong>Signal</strong>, click on <strong>Expert</strong> in the lower left-hand corner of the Create Element window.)</li><li>Name the created Signal <em>reset</em>. The <em>reset</em> Signal will be created and stored in the <em>signals</em> Package.</li><li>Repeat steps 1 and 2 to create the <em>split, start, stop,</em> and <em>unsplit</em> Signal elements (see the following figure).<br /><br /><ac:image ac:height="400"><ri:attachment ri:filename="Stopwatch-Creating_Signals.png"><ri:page ri:space-key="ALFP2024x" ri:content-title="Creating the StopWatch state machine" /></ri:attachment></ac:image></li></ol><p><br class="atl-forced-newline" />To create Signal Events for the Transitions on the <em>StopWatch</em> State Machine diagram</p><hr /><ul><li>Drag a signal element from the Model Browser to a transition on the State Machine diagram (see the following figure). The Signal Event will later be specified as the trigger of the Transition. <br /><br /><ac:image><ri:attachment ri:filename="Stopwatch-Dragging_Signal.png"><ri:page ri:space-key="ALFP2024x" ri:content-title="Creating the StopWatch state machine" /></ri:attachment></ac:image></li></ul><p><br /></p><p>To create a Signal Event for each Transition (see the following figure)</p><hr /><ol><li>Drag the <em>start</em> Signal to the Transition between the <em>ready</em> and <em>running</em> States.</li><li>Drag the <em>split</em> Signal to the Transition between the <em>running</em> and <em>paused</em> States.</li><li>Drag the <em>stop</em> Signal to the Transition between the <em>running</em> and <em>stopped</em> States.</li><li>Drag the <em>unsplit</em> Signal to the Transition between the <em>paused</em> and <em>running</em> States.</li><li>Drag the <em>stop</em> Signal to the Transition between the <em>paused</em> and <em>stopped</em> States.</li><li>Drag the <em>reset</em> Signal to the Transition between the <em>stopped</em> and <em>ready</em> States.</li><li>Drag the stop Signal to the Transition between the <em>stopped</em> and final States. <br /><br /><ac:image><ri:attachment ri:filename="Stopwatch-All_Triggers.png"><ri:page ri:space-key="ALFP2024x" ri:content-title="Creating the StopWatch state machine" /></ri:attachment></ac:image></li></ol><p><br class="atl-forced-newline" /> Now each and every Transition between the States has its own Signal Event. Next, you will also need to create a Time Event for the <strong>Transition </strong><strong>to </strong><strong>Self</strong> of the <em>running</em> State.</p><p><br class="atl-forced-newline" />To create a Time Event for the <strong>Transition </strong><strong>to </strong><strong>Self </strong>of the <em>running</em> state</p><hr /><ol><li>Right click the <strong>Transition</strong><strong> to</strong><strong> Self</strong> of the <em>running</em> state and select <strong>Specification</strong> to open its Specification window.</li><li>Click the <strong>Categorized View</strong> button to open the properties of the transition in the categorized view (see the following figure).</li><li>Click the <strong>Event </strong><strong>Type</strong> row in the <strong>Trigger</strong> category and select <strong>TimeEvent</strong> from the drop-down menu (see the following figure).<br /><br /><ac:image><ri:attachment ri:filename="Stopwatch-Creating_Time_Event.png"><ri:page ri:space-key="ALFP2024x" ri:content-title="Creating the StopWatch state machine" /></ri:attachment></ac:image><br /><br /></li><li>Click the <strong>When</strong> row in the <strong>Trigger</strong> category and type <em>&quot;1s&quot;</em> to specify that the Time Event will occur every second (see the following figure).</li><li>Check the <strong>Is Relative</strong> box, so it is <em>true</em> (see the following figure).<br /><br /><ac:image><ri:attachment ri:filename="Stopwatch-Specifying_Time_Event.png"><ri:page ri:space-key="ALFP2024x" ri:content-title="Creating the StopWatch state machine" /></ri:attachment></ac:image><br /><br /></li><li>Click <strong>Close</strong>. Your State Machine should look similar to the following figure.<br /><br /><ac:image><ri:attachment ri:filename="Stopwatch-With_Time_Event.png"><ri:page ri:space-key="ALFP2024x" ri:content-title="Creating the StopWatch state machine" /></ri:attachment></ac:image></li></ol><p><br /></p><p>Next: <ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="Defining the Stopwatch operations using Alf" /></ac:link></p></ac:layout-cell><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=137986221 space=ALFP2024x version=1 -->
## PAGE 00030: Creating the StopWatch structure

- page_id: `137986221`
- space_key: `ALFP2024x`
- source_url: https://docs.nomagic.com/spaces/ALFP2024x/pages/137986221/Creating+the+StopWatch+structure
- version_number: 1
- version_date: `2023-09-22T11:48:57.240+02:00`
- ancestors: Alf Plugin Documentation > Tutorials > Alf Tutorial 3: Stopwatch
- labels: []

### NORMALIZED CONTENT

First, use the [CONFLUENCE_PAGE title='Alf project template' space='ALFP2024x'] to create a new project called *StopWatch.*Next, define a stopwatch Class and its attributes using a Class diagram.

To create a *StopWatch* Class (on a Class diagram in a new Package)

1. Right click *Model* in the Model Browser and select **Create Element** > **Package**. A new Package will be created under the *Model* node. Name the created Package *system* (see the following figure). [ATTACHMENT filename='Stopwatch-Creating_System_Package.png']
2. Click on the system package and create a new Class diagram in the package by clicking the Create Diagram button on the toolbar. The Create Diagram dialog will open (see the following figure). Select Class Diagram . [ATTACHMENT filename='Stopwatch-Creating_Class_Diagram.png']
3. Name the class diagram *System*. You can also use the context menu of the *system* package to create a new Class diagram by right-clicking the *system* package and selecting **Create Diagram** > **Class Diagram**.
4. Use the diagram toolbar of Class Diagram to create a new Class element and name the created Class StopWatch (see the following figure). [ATTACHMENT filename='Stopwatch-Creating_Class_StopWatch.png']

Now add a *time* attribute to the *StopWatch* class. Since this attribute represents the elapsed time in seconds, type it as *Integer.*

To add a *time* attribute to the *StopWatch*****class

1. Click the small Create Element button on the StopWatch class and select Property . A new attribute will be created in the StopWatch class.
2. Name the attribute time and give it type Integer by directly typing that into the attribute compartment of the StopWatch class (see the following figure). [ATTACHMENT filename='Stopwatch-Creating_Attribute_time.png']

Next: [CONFLUENCE_PAGE title='Creating the StopWatch state machine' space='ALFP2024x']

#### PANEL: Related pages

Related pages

- [CONFLUENCE_PAGE title='Alf project template' space='ALFP2024x']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p>First, use the <ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="Alf project template" /></ac:link> to create a new project called <em>StopWatch.  </em>Next, define a stopwatch Class and its attributes using a Class diagram.</p><p><br /></p><p>To create a <em>StopWatch</em> Class (on a Class diagram in a new Package)</p><hr /><ol><li><p>Right click <em>Model</em> in the Model Browser and select <strong>Create Element</strong> &gt; <strong>Package</strong>. A new Package will be created under the <em>Model</em> node. Name the created Package <em>system</em> (see the following figure).<br /><br /></p><ac:image ac:height="400"><ri:attachment ri:filename="Stopwatch-Creating_System_Package.png"><ri:page ri:space-key="ALFP2024x" ri:content-title="Creating the StopWatch structure" /></ri:attachment></ac:image><br /><br /></li><li>Click on the <em>system</em> package and create a new Class diagram in the package by clicking the <strong>Create Diagram</strong> button on the toolbar. The <strong>Create </strong><strong>Diagram</strong> dialog will open (see the following figure). Select <strong>Class Diagram</strong>.<br /><br /><ac:image ac:height="400"><ri:attachment ri:filename="Stopwatch-Creating_Class_Diagram.png"><ri:page ri:space-key="ALFP2024x" ri:content-title="Creating the StopWatch structure" /></ri:attachment></ac:image><br /><br /></li><li><p>Name the class diagram <em>System</em>.</p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="5e5a136e-6442-460b-b98a-c6ebc3e6e013"><ac:rich-text-body><p>You can also use the context menu of the <em>system</em> package to create a new Class diagram by right-clicking the <em>system</em> package and selecting <strong>Create Diagram</strong> &gt; <strong>Class Diagram</strong>.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></li><li>Use the diagram toolbar of <strong>Class </strong><strong>Diagram</strong> to create a new <strong>Class</strong> element and name the created Class <em>StopWatch </em>(see the following figure). <br /><br /><ac:image ac:height="400"><ri:attachment ri:filename="Stopwatch-Creating_Class_StopWatch.png"><ri:page ri:space-key="ALFP2024x" ri:content-title="Creating the StopWatch structure" /></ri:attachment></ac:image></li></ol><p><br class="atl-forced-newline" /> Now add a <em>time</em> attribute to the <em>StopWatch</em> class. Since this attribute represents the elapsed time in seconds, type it as <em>Integer.</em><br class="atl-forced-newline" /><br class="atl-forced-newline" /></p><p>To add a <em>time</em> attribute to the <em>StopWatch</em><strong> </strong>class</p><hr /><ol><li>Click the small <strong>Create Element</strong> button on the <em>StopWatch</em> class and select <strong>Property</strong>. A new attribute will be created in the <em>StopWatch</em> class.</li><li>Name the attribute <em>time</em> and give it type <em>Integer</em> by directly typing that into the attribute compartment of the <em>StopWatch</em> class (see the following figure).<br /><br /><ac:image ac:height="400"><ri:attachment ri:filename="Stopwatch-Creating_Attribute_time.png"><ri:page ri:space-key="ALFP2024x" ri:content-title="Creating the StopWatch structure" /></ri:attachment></ac:image></li></ol><p><br /></p><p>Next:  <ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="Creating the StopWatch state machine" /></ac:link></p></ac:layout-cell><ac:layout-cell><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="74d036fa-abda-4b77-b9e8-b6d8c8c33e57"><ac:parameter ac:name="title">Related pages</ac:parameter><ac:rich-text-body><ul><li><ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="Alf project template" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=137986247 space=ALFP2024x version=1 -->
## PAGE 00031: Defining the Ready and Running behaviors using Alf

- page_id: `137986247`
- space_key: `ALFP2024x`
- source_url: https://docs.nomagic.com/spaces/ALFP2024x/pages/137986247/Defining+the+Ready+and+Running+behaviors+using+Alf
- version_number: 1
- version_date: `2023-09-22T11:48:58.663+02:00`
- ancestors: Alf Plugin Documentation > Tutorials > Alf Tutorial 3: Stopwatch
- labels: []

### NORMALIZED CONTENT

Next, add entry Behaviors to the *ready* and *running* States of the *StopWatch* State Machine.

To add an entry Behavior to the *ready* State

1. Click on the ready state and, in the Alf editor window, press Create .
2. Type the Alf code shown in the figure below. [ATTACHMENT filename='Stopwatch-Creating_State_Entry_Body_ready.png']
3. When the code is correct, press Save . The Alf code should now appear in the entry Behavior for the ready State, as shown in the figure below. [ATTACHMENT filename='Stopwatch-State_Entry_ready.png']

To add an entry Behavior to the *running* State

1. Click on the running state and, in the Alf editor window, press Create .
2. Type the Alf code shown in the figure below. [ATTACHMENT filename='Stopwatch-Creating_State_Entry_Body_running.png']
3. When the code is correct, press **Save**. The Alf code should now appear in the entry Behavior for the *running* State, as shown in the figure below. [IMAGE alt='' src='']

At this point the *StopWatch* has been completely modeled. You can now execute the *StopWatch* Class using Cameo Simulation Toolkit.

Next: [CONFLUENCE_PAGE title='Running the Stopwatch model' space='ALFP2024x']

#### PANEL: Related pages

Related pages

- [CONFLUENCE_PAGE title='The Alf editor' space='ALFP2024x']
- [CONFLUENCE_PAGE title='Using Alf for State Behaviors' space='ALFP2024x']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p>Next, add entry Behaviors to the <em>ready</em> and <em>running</em> States of the <em>StopWatch</em> State Machine.</p><p><br /></p><p>To add an entry Behavior to the <em>ready</em> State</p><hr /><ol><li>Click on the <em>ready</em> state and, in the Alf editor window, press <strong>Create</strong>.</li><li>Type the Alf code shown in the figure below.<br /><br /><ac:image ac:width="420"><ri:attachment ri:filename="Stopwatch-Creating_State_Entry_Body_ready.png"><ri:page ri:space-key="ALFP2024x" ri:content-title="Defining the Ready and Running behaviors using Alf" /></ri:attachment></ac:image><br /><br /></li><li>When the code is correct, press <strong>Save</strong>. The Alf code should now appear in the entry Behavior for the <em>ready</em> State, as shown in the figure below.<br /><br /><ac:image ac:width="420"><ri:attachment ri:filename="Stopwatch-State_Entry_ready.png"><ri:page ri:space-key="ALFP2024x" ri:content-title="Defining the Ready and Running behaviors using Alf" /></ri:attachment></ac:image></li></ol><p><span class="confluence-embedded-file-wrapper"><span><br /></span></span></p><p><span class="confluence-embedded-file-wrapper"><span>To add an entry Behavior to the <em>running</em> State</span></span></p><hr /><ol><li>Click on the running state and, in the Alf editor window, press <strong>Create</strong>.</li><li>Type the Alf code shown in the figure below.<br /><br /><ac:image ac:width="420"><ri:attachment ri:filename="Stopwatch-Creating_State_Entry_Body_running.png"><ri:page ri:space-key="ALFP2024x" ri:content-title="Defining the Ready and Running behaviors using Alf" /></ri:attachment></ac:image></li><li><p class="auto-cursor-target">When the code is correct, press <strong>Save</strong>. The Alf code should now appear in the entry Behavior for the <em>running</em> State, as shown in the figure below.<span class="confluence-embedded-file-wrapper"><br /></span></p><p class="auto-cursor-target"><span class="confluence-embedded-file-wrapper"><span class="confluence-embedded-file-wrapper"><span><ac:image ac:width="420"><ri:attachment ri:filename="Stopwatch-State_Entry_running.png"><ri:page ri:space-key="ALFP2024x" ri:content-title="Defining the Ready and Running behaviors using Alf" /></ri:attachment></ac:image></span></span></span></p></li></ol><p><span class="confluence-embedded-file-wrapper"><span><br /></span></span></p><p><span class="confluence-embedded-file-wrapper"><span>At this point the <em>StopWatch</em> has been completely modeled. You can now execute the <em>StopWatch</em> Class using Cameo Simulation Toolkit.</span></span></p><p><span class="confluence-embedded-file-wrapper"><span>Next: <ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="Running the Stopwatch model" /></ac:link><br /></span></span></p></ac:layout-cell><ac:layout-cell><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="907c2efc-4efd-4508-9f8b-8242a5ec3f02"><ac:parameter ac:name="title">Related pages</ac:parameter><ac:rich-text-body><ul><li><ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="The Alf editor" /></ac:link></li><li><ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="Using Alf for State Behaviors" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=137986243 space=ALFP2024x version=1 -->
## PAGE 00032: Defining the Stopwatch operations using Alf

- page_id: `137986243`
- space_key: `ALFP2024x`
- source_url: https://docs.nomagic.com/spaces/ALFP2024x/pages/137986243/Defining+the+Stopwatch+operations+using+Alf
- version_number: 1
- version_date: `2023-09-22T11:48:58.365+02:00`
- ancestors: Alf Plugin Documentation > Tutorials > Alf Tutorial 3: Stopwatch
- labels: []

### NORMALIZED CONTENT

When the *StopWatch* State Machine enters the *ready* State, the elapsed time defined by the attribute *time: Integer* should be reset to zero. In addition, the elapsed time should increment by 1 every second while the *StopWatch* is in the *running* state. You can define this functionality using Alf in two Operations on the *StopWatch* Class: *resetTime* and *increaseTime.* These operations will later be called from the entry Behaviors of the appropriate states in the *StopWatch* State Machine.

To create the *resetTime* Operation

1. Right-click the StopWatch class in the Model Browser and select Create Element > Operation .
2. Name the new operation resetTime (see the following figure). [ATTACHMENT filename='Stopwatch-Creating_Operation_resetTime.png'][IMAGE alt='' src='']
3. While resetTime operation is selected, open the [CONFLUENCE_PAGE title='The Alf editor' space='ALFP2024x'] window (select Windows > Alf ), if it isn't already open, and press Create .
4. Enter the Alf code shown in the figure below. [IMAGE alt='' src='']
5. When the Alf code is correct, press Save .

To create the *increaseTime* Operation

1. Right-click the StopWatch class in the Model Browser and select Create Element > Operation .
2. Name the new operation increaseTime .
3. Click on the *increaseTime* operation and, in the [CONFLUENCE_PAGE title='The Alf editor' space='ALFP2024x'] window, press **Create**.
4. Enter the Alf code shown in the figure below. [ATTACHMENT filename='Stopwatch-Creating_Operation_Method_increaseTime.png']
5. When the Alf code is correct, click Save .

Next: [CONFLUENCE_PAGE title='Defining the Ready and Running behaviors using Alf' space='ALFP2024x']

#### PANEL: Related pages

Related pages

- [CONFLUENCE_PAGE title='The Alf editor' space='ALFP2024x']
- [CONFLUENCE_PAGE title='Using Alf for Operation methods' space='ALFP2024x']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p>When the <em>StopWatch</em> State Machine enters the <em>ready</em> State, the elapsed time defined by the attribute <em>time: Integer</em> should be reset to zero. In addition, the elapsed time should increment by 1 every second while the <em>StopWatch</em> is in the <em>running</em> state. You can define this functionality using Alf in two Operations on the <em>StopWatch</em> Class: <em>resetTime</em> and <em>increaseTime.</em> These operations will later be called from the entry Behaviors of the appropriate states in the <em>StopWatch</em> State Machine.</p><p><br /></p><p>To create the <em>resetTime</em> Operation</p><hr /><ol><li>Right-click the <em>StopWatch</em> class in the Model Browser and select <strong>Create Element</strong> &gt; <strong>Operation</strong>.</li><li>Name the new operation <em>resetTime</em> (see the following figure).<br /><br /><ac:link><ri:attachment ri:filename="Stopwatch-Creating_Operation_resetTime.png"><ri:page ri:space-key="ALFP2024x" ri:content-title="Defining the Stopwatch operations using Alf" /></ri:attachment><ac:link-body><ac:image ac:height="400"><ri:attachment ri:filename="Stopwatch-Creating_Operation_resetTime.png"><ri:page ri:space-key="ALFP2024x" ri:content-title="Defining the Stopwatch operations using Alf" /></ri:attachment></ac:image></ac:link-body></ac:link><br /><br /></li><li>While <em>resetTime</em> operation is selected, open the <ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="The Alf editor" /><ac:plain-text-link-body><![CDATA[Alf editor]]></ac:plain-text-link-body></ac:link> window (select <strong>Windows &gt; Alf</strong>), if it isn't already open, and press <strong>Create</strong>.</li><li><p class="auto-cursor-target">Enter the Alf code shown in the figure below.<br /><br /></p><span class="confluence-link"><ac:image><ri:attachment ri:filename="Stopwatch-Creating_Operation_Method_resetTime.png"><ri:page ri:space-key="ALFP2024x" ri:content-title="Defining the Stopwatch operations using Alf" /></ri:attachment></ac:image></span><br /><br /></li><li>When the Alf code is correct, press <strong>Save</strong>.</li></ol><p><br /></p><p>To create the <em>increaseTime</em> Operation</p><hr /><ol><li>Right-click the <em>StopWatch</em> class in the Model Browser and select <strong>Create Element</strong> &gt; <strong>Operation</strong>.</li><li>Name the new operation <em>increaseTime</em>.</li><li><p class="auto-cursor-target">Click on the <em>increaseTime</em> operation and, in the <ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="The Alf editor" /><ac:plain-text-link-body><![CDATA[Alf editor]]></ac:plain-text-link-body></ac:link> window, press <strong>Create</strong>.</p></li><li><p class="auto-cursor-target">Enter the Alf code shown in the figure below.<br /><br /></p><ac:image><ri:attachment ri:filename="Stopwatch-Creating_Operation_Method_increaseTime.png"><ri:page ri:space-key="ALFP2024x" ri:content-title="Defining the Stopwatch operations using Alf" /></ri:attachment></ac:image><br /><br /></li><li>When the Alf code is correct, click <strong>Save</strong>.</li></ol><p><br /></p><p>Next: <ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="Defining the Ready and Running behaviors using Alf" /></ac:link></p></ac:layout-cell><ac:layout-cell><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="97b996ee-56a5-4206-8f3f-d19500988fe5"><ac:parameter ac:name="title">Related pages</ac:parameter><ac:rich-text-body><ul><li><ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="The Alf editor" /></ac:link></li><li><ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="Using Alf for Operation methods" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=137986174 space=ALFP2024x version=1 -->
## PAGE 00033: Dependency Management

- page_id: `137986174`
- space_key: `ALFP2024x`
- source_url: https://docs.nomagic.com/spaces/ALFP2024x/pages/137986174/Dependency+Management
- version_number: 1
- version_date: `2023-09-22T11:48:52.378+02:00`
- ancestors: Alf Plugin Documentation > User Guide > Compiling Alf
- labels: []

### NORMALIZED CONTENT

##### Dependency Tracking

Alf code usually references various elements of the model that contains the Alf text. [CONFLUENCE_PAGE title='The Alf compiler' space='ALFP2024x'] keeps track of such dependencies, so that it can tell you when a change in the model causes an error in dependent Alf code. When you first open a project with Alf code in it, the Alf compiler will automatically parse all the code in the project, in order to re-establish the dependencies of the code on other model elements.

You can cancel the processing of Alf code on project open, but, if you do, dependencies will only be established for code that has been fully parsed up to that point. The Alf compiler will then be unable to determine when it is necessary to recompile code for which dependencies have not been established. Therefore, do not cancel the dependency processing on project open if you intend to make any changes to the model you are opening. If you do cancel the initial processing, you can later re-establish all dependencies by using the **Tools > Alf > Clean Project** command to do a [CONFLUENCE_PAGE title='Building and cleaning' space='ALFP2024x'] of the project.

For example the figure below shows a class diagram from the [CONFLUENCE_PAGE title='Address Book' space='ALFP2024x'], in which the Association end name *entries* has been changed to *contents.* The Alf compiler has detected that the Alf code for the Operations *addEntry, removeEntry and findEntry* depend on this Association end, and, so, the compiler has marked that these Operations now have compilation errors. The Alf code for *addEntry* is shown in the Alf editor, showing the error on the reference *this.entries.* Changing this reference to *this.contents* eliminates the error for this Operation.

###### Dependency tracking example

##### rebuildRebuilding manually

Sometimes, the Alf compiler will lose track of dependencies and will not be recognize that an element marked as having Alf compilation errors could be recompiled successfully. This may happen, for example, if you delete a referenced element and create a new element with the same name, or if you use **Undo** to reverse the change that cause the errors in the first place. In such cases, you can manually initiate recompilation using the **Tools > Alf > Build Project** command to [CONFLUENCE_PAGE title='Building and cleaning' space='ALFP2024x'].

If, in the previous example, suppose, instead of changing the Association end name, that you delete the Association. Then you create a new Association, with the same end name *entries.* Even though the end name is the same, it is a different model element than in the old Association, so the Alf compiler has no record of any code dependency on it. However, if you do an Alf build of the project, then the code compiles successfully.

[IMAGE alt='' src='']

###### Example with a new Association with the same end name, but still needing to be rebuilt

If you change some Alf code with compilation errors to correct those errors, and then **Undo** that change, the compilation error annotation may not be restored. In this case, the Alf compiler will not recognize the need to recompile the code on a normal Alf build of the project, so the code will not be marked as having compilation errors, even though it is erroneous. In order to restore the proper error annotation, use the **Tools > Alf > Clean Project** command to do a [CONFLUENCE_PAGE title='Building and cleaning' space='ALFP2024x'].

##### recompileTurning off automatic building

If you don't want the Alf compiler to automatically rebuilding your project when it detects code that needs to be compiled, you can set the [CONFLUENCE_PAGE title='Environment options' space='ALFP2024x']Alf environment option **Build Automatically** to**false**. If you do this, the Alf compiler will mark elements that need to be recompiled with a warning annotation, rather than automatically recompiling them. This may be useful if you want to make several model changes outside the Alf code, and then recompile all the Alf code at once. To force actual recompilation of the Alf code for elements marked as needing recompilation, use the **Tools > Alf > Build Project** command to [CONFLUENCE_PAGE title='Building and cleaning' space='ALFP2024x'].

If the association end in the Address Book example is changed with the **Build Automatically** option turned off, then the affected operations are marked with warning annotations as shown below. [CONFLUENCE_PAGE title='Building and cleaning' space='ALFP2024x'] then results in error annotations, as shown previously.

[IMAGE alt='' src='']

###### Example showing recompilation-needed warning annotations

#### PANEL: Table of Contents

Table of Contents

3

#### PANEL: Related pages

Related pages

- [CONFLUENCE_PAGE title='The Alf compiler' space='ALFP2024x']
- [CONFLUENCE_PAGE title='Building and cleaning' space='ALFP2024x']
- [CONFLUENCE_PAGE title='Environment options' space='ALFP2024x']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><h3>Dependency Tracking</h3><p>Alf code usually references various elements of the model that contains the Alf text. <ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="The Alf compiler" /></ac:link> keeps track of such dependencies, so that it can tell you when a change in the model causes an error in dependent Alf code. When you first open a project with Alf code in it, the Alf compiler will automatically parse all the code in the project, in order to re-establish the dependencies of the code on other model elements.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="dbd0e355-5095-49f9-bed2-5aaeb8906639"><ac:rich-text-body><p>You can cancel the processing of Alf code on project open, but, if you do, dependencies will only be established for code that has been fully parsed up to that point. The Alf compiler will then be unable to determine when it is necessary to recompile code for which dependencies have not been established. Therefore, do not cancel the dependency processing on project open if you intend to make any changes to the model you are opening. If you do cancel the initial processing, you can later re-establish all dependencies by using the <strong>Tools &gt; Alf &gt; Clean Project</strong> command to do a <ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="Building and cleaning" /><ac:plain-text-link-body><![CDATA[clean rebuild]]></ac:plain-text-link-body></ac:link> of the project.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="4766e673-3667-49dc-8164-5dbe55ca7198"><ac:rich-text-body><p style="text-align: left;">For example the figure below shows a class diagram from the <ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="Address Book" /><ac:plain-text-link-body><![CDATA[Address Book sample model]]></ac:plain-text-link-body></ac:link>, in which the Association end name <em>entries</em> has been changed to <em>contents.</em> The Alf compiler has detected that the Alf code for the Operations <em>addEntry, removeEntry and findEntry</em> depend on this Association end, and, so, the compiler has marked that these Operations now have compilation errors. The Alf code for <em>addEntry</em> is shown in the Alf editor, showing the error on the reference <em>this.entries.</em> Changing this reference to <em>this.contents</em> eliminates the error for this Operation.</p><ac:image ac:align="center"><ri:attachment ri:filename="Dependency_Management-Example1.png"><ri:page ri:space-key="ALFP2024x" ri:content-title="Dependency Management" /></ri:attachment></ac:image><h6 class="auto-cursor-target" style="text-align: center;">Dependency tracking example</h6></ac:rich-text-body></ac:structured-macro><h3 class="auto-cursor-target"><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="58a7b2b7-42b5-4550-99b9-86fd4ade663b"><ac:parameter ac:name="">rebuild</ac:parameter></ac:structured-macro>Rebuilding manually</h3><p>Sometimes, the Alf compiler will lose track of dependencies and will not be recognize that an element marked as having Alf compilation errors could be recompiled successfully. This may happen, for example, if you delete a referenced element and create a new element with the same name, or if you use <strong>Undo</strong> to reverse the change that cause the errors in the first place. In such cases, you can manually initiate recompilation using the <strong>Tools &gt; Alf &gt; Build Project</strong> command to <ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="Building and cleaning" /><ac:plain-text-link-body><![CDATA[rebuild your project]]></ac:plain-text-link-body></ac:link>.</p><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="9653b11f-ee1b-465e-b960-e2986b13e81f"><ac:rich-text-body><p>If, in the previous example, suppose, instead of changing the Association end name, that you delete the Association. Then you create a new Association, with the same end name <em>entries.</em> Even though the end name is the same, it is a different model element than in the old Association, so the Alf compiler has no record of any code dependency on it. However, if you do an Alf build of the project, then the code compiles successfully.</p><p><ac:image ac:align="center"><ri:attachment ri:filename="Dependency_Management-Example2.png"><ri:page ri:space-key="ALFP2024x" ri:content-title="Dependency Management" /></ri:attachment></ac:image></p><h6 style="text-align: center;">Example with a new Association with the same end name, but still needing to be rebuilt</h6></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="warning" ac:schema-version="1" ac:macro-id="410aca12-862d-4a22-8b55-5cad79e6d304"><ac:rich-text-body><p>If you change some Alf code with compilation errors to correct those errors, and then <strong>Undo</strong> that change, the compilation error annotation may not be restored. In this case, the Alf compiler will not recognize the need to recompile the code on a normal Alf build of the project, so the code will not be marked as having compilation errors, even though it is erroneous. In order to restore the proper error annotation, use the <strong>Tools &gt; Alf &gt; Clean Project</strong> command to do a <ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="Building and cleaning" /><ac:plain-text-link-body><![CDATA[clean build of the entire project]]></ac:plain-text-link-body></ac:link>.</p></ac:rich-text-body></ac:structured-macro><h3 class="auto-cursor-target"><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="6f3785c4-ff50-470c-a220-4d12378c65f3"><ac:parameter ac:name="">recompile</ac:parameter></ac:structured-macro>Turning off automatic building</h3><p>If you don't want the Alf compiler to automatically rebuilding your project when it detects code that needs to be compiled, you can set the <ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="Environment options" /><ac:link-body>Alf environment option <strong>Build Automatically</strong></ac:link-body></ac:link> to<strong> false</strong>. If you do this, the Alf compiler will mark elements that need to be recompiled with a warning annotation, rather than automatically recompiling them. This may be useful if you want to make several model changes outside the Alf code, and then recompile all the Alf code at once. To force actual recompilation of the Alf code for elements marked as needing recompilation, use the <strong>Tools &gt; Alf &gt; Build Project</strong> command to <ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="Building and cleaning" /><ac:plain-text-link-body><![CDATA[rebuild the project]]></ac:plain-text-link-body></ac:link>.</p><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="bef943b4-c2fa-4109-8c79-9957d3a10209"><ac:rich-text-body><p>If the association end in the Address Book example is changed with the <strong>Build Automatically</strong> option turned off, then the affected operations are marked with warning annotations as shown below. <ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="Building and cleaning" /><ac:plain-text-link-body><![CDATA[Rebuilding the project]]></ac:plain-text-link-body></ac:link> then results in error annotations, as shown previously.</p><p><ac:image ac:align="center"><ri:attachment ri:filename="Dependency_Management-Example3.png"><ri:page ri:space-key="ALFP2024x" ri:content-title="Dependency Management" /></ri:attachment></ac:image></p><h6 style="text-align: center;">Example showing recompilation-needed warning annotations</h6></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell><ac:layout-cell><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="fd4e8ab6-68fa-4ab4-b4ea-20808d945995"><ac:parameter ac:name="title">Table of Contents</ac:parameter><ac:rich-text-body><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="38ca36a0-ccf2-414f-8b28-2587bc776ac8"><ac:parameter ac:name="maxLevel">3</ac:parameter></ac:structured-macro></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="e77f8129-7edd-45d2-a741-d3c2af2d6776"><ac:parameter ac:name="title">Related pages</ac:parameter><ac:rich-text-body><ul><li><ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="The Alf compiler" /></ac:link></li><li><ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="Building and cleaning" /></ac:link></li><li><ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="Environment options" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=137986186 space=ALFP2024x version=1 -->
## PAGE 00034: Developer Guide

- page_id: `137986186`
- space_key: `ALFP2024x`
- source_url: https://docs.nomagic.com/spaces/ALFP2024x/pages/137986186/Developer+Guide
- version_number: 1
- version_date: `2023-09-22T11:48:53.242+02:00`
- ancestors: Alf Plugin Documentation
- labels: []

### NORMALIZED CONTENT

h4

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="f90bc20b-d070-4205-a906-d9b7a37c06e4"><ac:parameter ac:name="style">h4</ac:parameter></ac:structured-macro></p>
````

<!--NOMAGIC_PAGE id=137986179 space=ALFP2024x version=1 -->
## PAGE 00035: Environment options

- page_id: `137986179`
- space_key: `ALFP2024x`
- source_url: https://docs.nomagic.com/spaces/ALFP2024x/pages/137986179/Environment+options
- version_number: 1
- version_date: `2023-09-22T11:48:52.692+02:00`
- ancestors: Alf Plugin Documentation > User Guide > Compiling Alf
- labels: []

### NORMALIZED CONTENT

*Environment options* are options that you can set for your MagicDraw installation that apply across all the projects you create or open. The Alf plugin has two such options.

- Build On Project Open – The default for this option is false, in which case, when a project with Alf code is opened, the Alf compiler parses all the code in the project in order to [CONFLUENCE_PAGE title='Dependency Management' space='ALFP2024x'] of the code on other model elements. Set this option to true to automatically perform a [CONFLUENCE_PAGE title='Building and cleaning' space='ALFP2024x'] on a project when it is open, which not only parses all the Alf code, but also recompiles it.
- Build Automatically – The default for this option is true, in which case the Alf compiler will automatically recompile Alf code whenever it may be necessary due to changes in model elements on which the code depends. Set this option to false to prevent automatic recompilation, in which case the Alf compiler will instead just mark elements having Alf code needing recompilation with [CONFLUENCE_PAGE title='Dependency Management' space='ALFP2024x'] .

To access the Alf environment options

1. Select Options > Environment from the main menu
2. On the left-hand side, select the entry for Alf .
3. The Alf environment options appear on the right-hand side. [ATTACHMENT filename='Environment_Options-Alf_Options.png']

#### PANEL: Related pages

Related pages

- [CONFLUENCE_PAGE title='The Alf compiler' space='ALFP2024x']
- [CONFLUENCE_PAGE title='Dependency Management' space='ALFP2024x']
- [CONFLUENCE_PAGE title='Building and cleaning' space='ALFP2024x']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p><em>Environment options</em> are options that you can set for your MagicDraw installation that apply across all the projects you create or open. The Alf plugin has two such options.</p><ul><li><strong>Build On Project Open</strong> – The default for this option is <em>false,</em> in which case, when a project with Alf code is opened, the Alf compiler parses all the code in the project in order to <ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="Dependency Management" /><ac:plain-text-link-body><![CDATA[establish dependencies]]></ac:plain-text-link-body></ac:link> of the code on other model elements. Set this option to <em>true</em> to automatically perform a <ac:link ac:anchor="clean-project"><ri:page ri:space-key="ALFP2024x" ri:content-title="Building and cleaning" /><ac:plain-text-link-body><![CDATA[clean build]]></ac:plain-text-link-body></ac:link> on a project when it is open, which not only parses all the Alf code, but also recompiles it.</li><li><strong>Build Automatically</strong> – The default for this option is <em>true,</em> in which case the Alf compiler will automatically recompile Alf code whenever it may be necessary due to changes in model elements on which the code depends. Set this option to <em>false</em> to prevent automatic recompilation, in which case the Alf compiler will instead just mark elements having Alf code needing recompilation with <ac:link ac:anchor="recompile"><ri:page ri:space-key="ALFP2024x" ri:content-title="Dependency Management" /><ac:plain-text-link-body><![CDATA[warning annotations]]></ac:plain-text-link-body></ac:link>.</li></ul><p><br /></p><p>To access the Alf environment options</p><hr /><ol><li>Select <strong>Options &gt; Environment</strong> from the main menu</li><li>On the left-hand side, select the entry for <strong>Alf</strong>.</li><li>The Alf environment options appear on the right-hand side.<br /><br /><ac:image><ri:attachment ri:filename="Environment_Options-Alf_Options.png"><ri:page ri:space-key="ALFP2024x" ri:content-title="Environment options" /></ri:attachment></ac:image></li></ol></ac:layout-cell><ac:layout-cell><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="50b20bf8-eb4f-43c0-85de-cdf2f2ed8ebc"><ac:parameter ac:name="title">Related pages</ac:parameter><ac:rich-text-body><ul><li><ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="The Alf compiler" /></ac:link></li><li><ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="Dependency Management" /></ac:link></li><li><ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="Building and cleaning" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=137986073 space=ALFP2024x version=1 -->
## PAGE 00036: Getting Started

- page_id: `137986073`
- space_key: `ALFP2024x`
- source_url: https://docs.nomagic.com/spaces/ALFP2024x/pages/137986073/Getting+Started
- version_number: 1
- version_date: `2023-09-22T11:48:45.312+02:00`
- ancestors: Alf Plugin Documentation > User Guide
- labels: []

### NORMALIZED CONTENT

h4

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="a1fdf69e-3c7f-48e9-895d-a8bbe9bc8d14"><ac:parameter ac:name="style">h4</ac:parameter></ac:structured-macro><p> </p></ac:layout-cell><ac:layout-cell><p> </p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=137986081 space=ALFP2024x version=1 -->
## PAGE 00037: Hello

- page_id: `137986081`
- space_key: `ALFP2024x`
- source_url: https://docs.nomagic.com/spaces/ALFP2024x/pages/137986081/Hello
- version_number: 1
- version_date: `2023-09-22T11:48:46.229+02:00`
- ancestors: Alf Plugin Documentation > User Guide > Getting Started > Samples
- labels: []

### NORMALIZED CONTENT

The Hello sample is a simple model that contains two activities:

- Hello( name : String ) – Writes "Hello" followed by the input name.
- Hello World() – Calls Hello with the input "World".

Both these activities were compiled from Alf. To see the original Alf code, open the [CONFLUENCE_PAGE title='The Alf editor' space='ALFP2024x'] window (select **Window > Alf**) and select either activity. The Alf code will appear in the window.

When [CONFLUENCE_PAGE title='Running a model with Alf' space='ALFP2024x'], the *Hello World* should write "Hello World!" in the console pane of the simulation window.

#### PANEL: Related Pages

Related Pages

[CONFLUENCE_PAGE title='The Alf editor' space='ALFP2024x']

[CONFLUENCE_PAGE title='Running a model with Alf' space='ALFP2024x']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p>The Hello sample is a simple model that contains two activities:</p><ul><li><em>Hello( name : String )</em> – Writes &quot;Hello&quot; followed by the input name.</li><li><em>Hello World()</em> – Calls <em>Hello</em> with the input &quot;World&quot;.</li></ul><p>Both these activities were compiled from Alf. To see the original Alf code, open the <ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="The Alf editor" /><ac:plain-text-link-body><![CDATA[Alf editor ]]></ac:plain-text-link-body></ac:link> window (select <strong>Window &gt; Alf</strong>) and select either activity. The Alf code will appear in the window.</p><p>When <ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="Running a model with Alf" /><ac:plain-text-link-body><![CDATA[executed (using CST)]]></ac:plain-text-link-body></ac:link>, the <em>Hello World</em> should write &quot;Hello World!&quot; in the console pane of the simulation window.</p></ac:layout-cell><ac:layout-cell><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="5c2054a7-2f4e-40f3-9117-8696f02a1985"><ac:parameter ac:name="title">Related Pages</ac:parameter><ac:rich-text-body><p><ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="The Alf editor" /></ac:link></p><p><ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="Running a model with Alf" /></ac:link></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=137986162 space=ALFP2024x version=1 -->
## PAGE 00038: Helper functions

- page_id: `137986162`
- space_key: `ALFP2024x`
- source_url: https://docs.nomagic.com/spaces/ALFP2024x/pages/137986162/Helper+functions
- version_number: 1
- version_date: `2023-09-22T11:48:51.451+02:00`
- ancestors: Alf Plugin Documentation > User Guide > Working with Alf
- labels: []

### NORMALIZED CONTENT

Cameo Simulation Toolkit provides an Action Language Helper (ALH) API for accessing executing models. Many of the capabilities in this API are natively available as part of the Alf language (such as reading and writing structural feature values, sending signals, etc.). However, the API also provides some additional functionality that is not covered by the Alf language itself, but can still be used from Alf code. The Alf *Helper Functions* provide access to this functionality, including checking if an object currently is or previously was in a given state and accessing the current simulation time and simulation time unit.

#### PANEL: Related pages

Related pages

- [CONFLUENCE_PAGE title='Checking the State of an object' space='ALFP2024x']
- [CONFLUENCE_PAGE title='Checking a visited State' space='ALFP2024x']
- [CONFLUENCE_PAGE title='Accessing current simulation time' space='ALFP2024x']
- [CONFLUENCE_PAGE title='Accessing the simulation time unit' space='ALFP2024x']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p>Cameo Simulation Toolkit provides an Action Language Helper (ALH) API for accessing executing models. Many of the capabilities in this API are natively available as part of the Alf language (such as reading and writing structural feature values, sending signals, etc.). However, the API also provides some additional functionality that is not covered by the Alf language itself, but can still be used from Alf code. The Alf <em>Helper Functions</em> provide access to this functionality, including checking if an object currently is or previously was in a given state and accessing the current simulation time and simulation time unit.</p></ac:layout-cell><ac:layout-cell><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="281b1859-6448-4a1e-9f31-059a9aa33d9a"><ac:parameter ac:name="title">Related pages</ac:parameter><ac:rich-text-body><ul><li><ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="Checking the State of an object" /></ac:link></li><li><ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="Checking a visited State" /></ac:link></li><li><ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="Accessing current simulation time" /></ac:link></li><li><ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="Accessing the simulation time unit" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=137986192 space=ALFP2024x version=1 -->
## PAGE 00039: Importer API

- page_id: `137986192`
- space_key: `ALFP2024x`
- source_url: https://docs.nomagic.com/spaces/ALFP2024x/pages/137986192/Importer+API
- version_number: 1
- version_date: `2023-09-22T11:48:53.932+02:00`
- ancestors: Alf Plugin Documentation > Developer Guide
- labels: []

### NORMALIZED CONTENT

The *AlfImporter* class provides the basic interface for importing Alf code from external files. An *AlfImporter* is instantiated with two pieces of information:

1. A string giving the path to the model directory , which is the root directory for all files being imported.
2. An optional *ProgressStatus* object, the description of which is updated with the names of files being imported. (This argument may be null, if you do not wish to display progress status.)

Importing of Alf code then takes place in two steps:

1. [CONFLUENCE_PAGE title='Importer API: Parsing' space='ALFP2024x'] one or more Alf model units (along with their subunits) from files in the model directory, caching their resulting abstract syntax representations.
2. [CONFLUENCE_PAGE title='Importer API: Mapping' space='ALFP2024x'] (after constraint checking) all parsed units into the UML model in MagicDraw.

The API allows you to carry out these steps individually (which is useful if, for example, you wish to import multiple model unit files before mapping) or using a single call (for a single model unit file).

Importation takes place into the currently open and active Project. Once you instantiate an *AlfImporter* object in a Project, it is no longer consistent to use an *AlfCompiler* object in that Project. Instead, once you have completed any importation, you must use the *AlfActionUtil,.resetActiveProject* method to return the currently active project to a state in which the *AlfCompiler* can be used (see [CONFLUENCE_PAGE title='Importer API: Mapping' space='ALFP2024x']). Alternatively, you can use the *AlfActionUtil.importFrom* method to do the importation (as described in [CONFLUENCE_PAGE title='Importer API: Utilities' space='ALFP2024x']), in which case the Project will be restored for normal Alf operations at the completion of the method.

#### PANEL: Related Pages

Related Pages

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p>The <em>AlfImporter</em> class provides the basic interface for importing Alf code from external files. An <em>AlfImporter</em> is instantiated with two pieces of information:</p><ol><li>A string giving the path to the <em>model directory</em><em>,</em> which is the root directory for all files being imported.</li><li>An optional <a href="https://docs.nomagic.com/display/MDTWRT/Running+action+with+progress"> <em>ProgressStatus</em> </a> object, the description of which is updated with the names of files being imported. (This argument may be null, if you do not wish to display progress status.)</li></ol><p>Importing of Alf code then takes place in two steps:</p><ol><li><ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="Importer API: Parsing" /><ac:plain-text-link-body><![CDATA[Parsing]]></ac:plain-text-link-body></ac:link> one or more Alf model units (along with their subunits) from files in the model directory, caching their resulting abstract syntax representations.</li><li><ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="Importer API: Mapping" /><ac:plain-text-link-body><![CDATA[Mapping]]></ac:plain-text-link-body></ac:link> (after constraint checking) all parsed units into the UML model in MagicDraw.</li></ol><p>The API allows you to carry out these steps individually (which is useful if, for example, you wish to import multiple model unit files before mapping) or <span class="confluence-link">using a single call</span> (for a single model unit file).</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="c97d22d8-4b1a-4cb6-bf07-330b4cad2990"><ac:rich-text-body><p>Importation takes place into the currently open and active Project. Once you instantiate an <em>AlfImporter</em> object in a Project, it is no longer consistent to use an <em>AlfCompiler</em> object in that Project. Instead, once you have completed any importation, you must use the <em>AlfActionUtil,.resetActiveProject</em> method to return the currently active project to a state in which the <em>AlfCompiler</em> can be used (see <ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="Importer API: Mapping" /></ac:link>). Alternatively, you can use the <em>AlfActionUtil.importFrom</em> method to do the importation (as described in <ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="Importer API: Utilities" /></ac:link>), in which case the Project will be restored for normal Alf operations at the completion of the method.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell><ac:layout-cell><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="c9e705e7-c70e-4d93-b5f0-d11eaf392bbb"><ac:parameter ac:name="title">
       Related Pages
      </ac:parameter><ac:rich-text-body><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="f1fa4f0e-d74d-43ad-a221-703585bb068a" /></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"> </p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="two_equal"><ac:layout-cell><p><br /></p></ac:layout-cell><ac:layout-cell><p> </p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=137986194 space=ALFP2024x version=1 -->
## PAGE 00040: Importer API: Mapping

- page_id: `137986194`
- space_key: `ALFP2024x`
- source_url: https://docs.nomagic.com/spaces/ALFP2024x/pages/137986194/Importer+API+Mapping
- version_number: 1
- version_date: `2023-09-22T11:48:54.273+02:00`
- ancestors: Alf Plugin Documentation > Developer Guide > Importer API
- labels: []

### NORMALIZED CONTENT

Once one or more Alf model unit files (and their subunits, if any) have been [CONFLUENCE_PAGE title='Importer API: Parsing' space='ALFP2024x'], you can use the *AlfImporter.compile* method to constraint check all cached units and, if there are no constraint violations, map them into the UML model. If there are constraint violations, then these are reported in the MagicDraw [CONFLUENCE_PAGE title='Showing notifications, adding text into Message Window' space='MDTWRT']. The *compile* method returns a Boolean indicating whether constraint checking was successful or not. You can also check the success of the last compilation by calling the *isSuccessful* operation.

The *compile* method takes a Java Path as a parameter, but this is only used to update the *ProgressStatus* object provided when**the AlfImporter was [CONFLUENCE_PAGE title='Importer API' space='ALFP2024x'] (if any), and it may be null (in which case the progress status is not updated). Since mapping results in an update to the UML model, the *compile* method should be called within a MagicDraw session. This can be done conveniently using the *AlfActionUtil.executeSession* method, which also ensures that any automatic Alf compilation is turned off during the session, so new compilations are not accidentally triggered by updates from the mapping process.

Using an *AlfImporter* in a Project is incompatible with subsequently using an *AlfCompiler* in that Project. Once you have completed an importation, you must use the *AlfActionUtil,.resetActiveProject* method to return the currently active project to a state in which the *AlfCompiler* can be used, or use to *AlfActionUtil.resetProject* method to similarly reset a specific project. You should do this even if the importation was not successful. Alternatively, you can use the *AlfActionUtil.importFrom* method, which allows for subsequent Alf compilation after importation (see [CONFLUENCE_PAGE title='Importer API: Utilities' space='ALFP2024x']).

```java

```

Rather than separately parsing and then compiling imported Alf files, you can do both with one call to the *importFile* method. Given a Java *Path* object for a single file in the model directory identified when the *AlfImporter* object was [CONFLUENCE_PAGE title='Importer API' space='ALFP2024x'], the *importFile* method parses the model unit in the given file (and its subunits, if any), performs constraint checking and, if that is all successful, compiles the unit into the UML model. The method returns a Boolean indicating whether the import was successful or not. If not, any syntactic errors or constraint violations are reported in the MagicDraw [CONFLUENCE_PAGE title='Showing notifications, adding text into Message Window' space='MDTWRT']. As for the *compile* method, the *importFile* method should be called within a MagicDraw session, since it may potentially update the UML model if a mapping is carried out.

```java

```

#### PANEL: Related Pages

Related Pages

- [CONFLUENCE_PAGE title='Importer API: Parsing' space='ALFP2024x']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p>Once one or more Alf model unit files (and their subunits, if any) have been <ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="Importer API: Parsing" /><ac:plain-text-link-body><![CDATA[parsed]]></ac:plain-text-link-body></ac:link>, you can use the <em>AlfImporter.compile</em> method to constraint check all cached units and, if there are no constraint violations, map them into the UML model. If there are constraint violations, then these are reported in the MagicDraw <ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Showing notifications, adding text into Message Window" /><ac:plain-text-link-body><![CDATA[Message Window]]></ac:plain-text-link-body></ac:link>. The <em>compile</em> method returns a Boolean indicating whether constraint checking was successful or not. You can also check the success of the last compilation by calling the <em>isSuccessful</em> operation.</p><p>The <em>compile</em> method takes a Java Path as a parameter, but this is only used to update the <em>ProgressStatus</em> object provided when<em> </em>the AlfImporter was <ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="Importer API" /><ac:plain-text-link-body><![CDATA[created]]></ac:plain-text-link-body></ac:link> (if any), and it may be null (in which case the progress status is not updated). Since mapping results in an update to the UML model, the <em>compile</em> method should be called within a MagicDraw session. This can be done conveniently using the <em>AlfActionUtil.executeSession</em> method, which also ensures that any automatic Alf compilation is turned off during the session, so new compilations are not accidentally triggered by updates from the mapping process.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="6c62f364-34df-485c-9204-3d6cc85273a4"><ac:rich-text-body><p>Using an <em>AlfImporter</em> in a Project is incompatible with subsequently using an <em>AlfCompiler</em> in that Project. Once you have completed an importation, you must use the <em>AlfActionUtil,.resetActiveProject</em> method to return the currently active project to a state in which the <em>AlfCompiler</em> can be used, or use to <em>AlfActionUtil.resetProject</em> method to similarly reset a specific project. You should do this even if the importation was not successful. Alternatively, you can use the <em>AlfActionUtil.importFrom</em> method, which allows for subsequent Alf compilation after importation (see <ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="Importer API: Utilities" /></ac:link>).</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="333122a9-c35a-40b3-bf04-3f941f6852ee"><ac:parameter ac:name="language">java</ac:parameter><ac:plain-text-body><![CDATA[AlfImporter importer = new AlfImporter(modelDirectory, progressStatus);
Path path = Paths.get(modelDirectory, modelFileName);
if (importer.parse(path)) {
    AlfActionUtil.executeSession("Import Alf", new Runnable() {
        public void run() {
            importer.compile(path);                    
        }
    });
}
// It is unsafe to use the AlfCompiler API at this point.

AlfActionUtil.resetActiveProject();

// It is safe to use the AlfCompiler API from here on...]]></ac:plain-text-body></ac:structured-macro><p>Rather than separately parsing and then compiling imported Alf files, you can do both with one call to the <em>importFile</em> method. Given a Java <em>Path</em> object for a single file in the model directory identified when the <em>AlfImporter</em> object was <ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="Importer API" /><ac:plain-text-link-body><![CDATA[created]]></ac:plain-text-link-body></ac:link>, the <em>importFile</em> method <span class="confluence-link">parses</span> the model unit in the given file (and its subunits, if any), performs constraint checking and, if that is all successful, <span class="confluence-link">compiles</span> the unit into the UML model. The method returns a Boolean indicating whether the import was successful or not. If not, any syntactic errors or constraint violations are reported in the MagicDraw <ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Showing notifications, adding text into Message Window" /><ac:plain-text-link-body><![CDATA[Message Window]]></ac:plain-text-link-body></ac:link>. As for the <em>compile</em> method, the <em>importFile</em> method should be called within a MagicDraw session, since it may potentially update the UML model if a mapping is carried out.</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="9d89c795-bd38-4aa0-9526-737e355e0305"><ac:parameter ac:name="language">java</ac:parameter><ac:plain-text-body><![CDATA[AlfImporter importer = new AlfImporter(modelDirectory, progressStatus);
AlfActionUtil.executeSession("Import Alf", new Runnable() {
    public void run() {
        importer.importFile(Paths.get(modelDirectory, modelFileName));                    
    }
});
AlfActionUtil.resetActiveProject();]]></ac:plain-text-body></ac:structured-macro><p><br /></p><p class="auto-cursor-target"><br /></p><p><br /></p></ac:layout-cell><ac:layout-cell><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="9018d0c1-71e5-43df-adf5-f936d2aa27f2"><ac:parameter ac:name="title">
       Related Pages
      </ac:parameter><ac:rich-text-body><ul><li><ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="Importer API: Parsing" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="two_equal"><ac:layout-cell><p><br /></p></ac:layout-cell><ac:layout-cell><p> </p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=137986193 space=ALFP2024x version=1 -->
## PAGE 00041: Importer API: Parsing

- page_id: `137986193`
- space_key: `ALFP2024x`
- source_url: https://docs.nomagic.com/spaces/ALFP2024x/pages/137986193/Importer+API+Parsing
- version_number: 1
- version_date: `2023-09-22T11:48:54.080+02:00`
- ancestors: Alf Plugin Documentation > Developer Guide > Importer API
- labels: []

### NORMALIZED CONTENT

An Alf model unit file may be initially imported using the *AlfImporter.parse* method, passing in a Java *Path* object for the file. The file must be in the model directory identified when the *AlfImporter* object was [CONFLUENCE_PAGE title='Importer API' space='ALFP2024x']. The Alf code in the given file is then parsed and the resulting abstract syntax tree is cached. Any subunits of the Alf unit in the given file are also imported. In addition, when the import process identifies a reference that cannot be resolved within the file being imported (or within the UML model being imported into), it will attempt to find another associated file in which the reference can be resolved. The importer uses the conventions of the Alf Reference Implementation when resolving Alf unit names to file names, starting from the model directory identified for the importation (for more information, see the Alf Reference Implementation documentation [here](https://github.com/ModelDriven/Alf-Reference-Implementation/wiki/Unit-Management#the-model-directory)).

The *parse* method returns a Boolean indicating whether all parsing completed successfully or not. You can also check the success of the last parse by calling the *isSuccessful* operation. You can call the *parse* method multiple times to load multiple different files (which must all be from the same model directory) into the import cache. Note that the *isSuccessful* flag is reset after each parse operation.

Unlike parsing using the *AlfCompiler,* the parse process in the *AlfImporter* does *not* include constraint checking. Instead, constraint checking is done as part of the [CONFLUENCE_PAGE title='Importer API: Mapping' space='ALFP2024x'] process, on all cached model units and their subunits together. This means that any errors reported from parsing imported code will be syntactic errors. All such errors are reported as messages in the MagicDraw [CONFLUENCE_PAGE title='Showing notifications, adding text into Message Window' space='MDTWRT']. It is also possible for the parse to be unsuccessful without reporting any syntax errors, for one of the following reasons:

- The identified file is not found or attempting to read it results in an IO exception (though no exception is propagated).
- The identified file has a valid Alf unit in it, but the name of that unit does not match the name of the file.

```java

```

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p>An Alf model unit file may be initially imported using the <em>AlfImporter.parse</em> method, passing in a Java <em>Path</em> object for the file. The file must be in the model directory identified when the <em>AlfImporter</em> object was <ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="Importer API" /><ac:plain-text-link-body><![CDATA[created]]></ac:plain-text-link-body></ac:link>. The Alf code in the given file is then parsed and the resulting abstract syntax tree is cached. Any subunits of the Alf unit in the given file are also imported. In addition, when the import process identifies a reference that cannot be resolved within the file being imported (or within the UML model being imported into), it will attempt to find another associated file in which the reference can be resolved. The importer uses the conventions of the Alf Reference Implementation when resolving Alf unit names to file names, starting from the model directory identified for the importation (for more information, see the Alf Reference Implementation documentation <a href="https://github.com/ModelDriven/Alf-Reference-Implementation/wiki/Unit-Management#the-model-directory" class="external-link" rel="nofollow">here</a>).</p><p>The <em>parse</em> method returns a Boolean indicating whether all parsing completed successfully or not. You can also check the success of the last parse by calling the <em>isSuccessful</em> operation. You can call the <em>parse</em> method multiple times to load multiple different files (which must all be from the same model directory) into the import cache. Note that the <em>isSuccessful</em> flag is reset after each parse operation.</p><p>Unlike parsing using the <em>AlfCompiler,</em> the parse process in the <em>AlfImporter</em> does <em>not</em> include constraint checking. Instead, constraint checking is done as part of the <ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="Importer API: Mapping" /><ac:plain-text-link-body><![CDATA[mapping]]></ac:plain-text-link-body></ac:link> process, on all cached model units and their subunits together. This means that any errors reported from parsing imported code will be syntactic errors. All such errors are reported as messages in the MagicDraw <ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Showing notifications, adding text into Message Window" /><ac:plain-text-link-body><![CDATA[Message Window]]></ac:plain-text-link-body></ac:link>. It is also possible for the parse to be unsuccessful without reporting any syntax errors, for one of the following reasons:</p><ul><li>The identified file is not found or attempting to read it results in an IO exception (though no exception is propagated).</li><li>The identified file has a valid Alf unit in it, but the name of that unit does not match the name of the file.</li></ul><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="f8f456eb-1f4f-4740-a49d-8ce76c205dda"><ac:parameter ac:name="language">
       java
      </ac:parameter><ac:plain-text-body><![CDATA[AlfImporter importer = new AlfImporter(modelDirectory, progressStatus);
if (importer.parse(Paths.get(modelDirectory, "Utilities.alf"))) {
	importer.parse(Paths.get(modelDirectory, "Main.alf"));
}]]></ac:plain-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell><ac:layout-cell><p> </p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="two_equal"><ac:layout-cell><p><br /></p></ac:layout-cell><ac:layout-cell><p> </p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=137986195 space=ALFP2024x version=1 -->
## PAGE 00042: Importer API: Utilities

- page_id: `137986195`
- space_key: `ALFP2024x`
- source_url: https://docs.nomagic.com/spaces/ALFP2024x/pages/137986195/Importer+API+Utilities
- version_number: 1
- version_date: `2023-09-22T11:48:54.535+02:00`
- ancestors: Alf Plugin Documentation > Developer Guide > Importer API
- labels: []

### NORMALIZED CONTENT

*AlfActionUtil.importFrom* is a static method that takes a directory path (as a string) and a file name, and carries out the functionality of the **Import From > Alf File** command (see [CONFLUENCE_PAGE title='Importing Alf' space='ALFP2024x']). That is, it does the following:

1. If there is no Project currently open, it creates a new Project using the [CONFLUENCE_PAGE title='Alf project template' space='ALFP2024x'] and makes it the active Project.
2. It imports the given file into the currently active Project, with progress status, in a MagicDraw session.
3. It marks the active Project as dirty (but does not save it or close it).

When the method completes, it is safe to continue to perform Alf compiler operations on the Project. Any parsing, constraint checking or mapping errors (but not IO exceptions) are reported to the MagicDraw [CONFLUENCE_PAGE title='Showing notifications, adding text into Message Window' space='MDTWRT'].

```java

```

#### PANEL: Related Pages

Related Pages

- [CONFLUENCE_PAGE title='Importer API: Parsing' space='ALFP2024x']
- [CONFLUENCE_PAGE title='Importer API: Mapping' space='ALFP2024x']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p><em>AlfActionUtil.importFrom</em> is a static method that takes a directory path (as a string) and a file name, and carries out the functionality of the <strong>Import From &gt; Alf File</strong> command (see <ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="Importing Alf" /></ac:link>). That is, it does the following:</p><ol><li>If there is no Project currently open, it creates a new Project using the <ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="Alf project template" /></ac:link> and makes it the active Project.</li><li>It imports the given file into the currently active Project, with progress status, in a MagicDraw session.</li><li>It marks the active Project as dirty (but does not save it or close it).</li></ol><p>When the method completes, it is safe to continue to perform Alf compiler operations on the Project. Any parsing, constraint checking or mapping errors (but not IO exceptions) are reported to the MagicDraw <ac:link><ri:page ri:space-key="MDTWRT" ri:content-title="Showing notifications, adding text into Message Window" /><ac:plain-text-link-body><![CDATA[Message Window]]></ac:plain-text-link-body></ac:link>.</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="0dea758e-a91a-417d-a963-e7c104a1306b"><ac:parameter ac:name="language">java</ac:parameter><ac:plain-text-body><![CDATA[AlfActionUtil.importFrom(modelDirectory, modelFileName);]]></ac:plain-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell><ac:layout-cell><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="4560008f-b192-4a42-86bd-9d1f67956d11"><ac:parameter ac:name="title">
       Related Pages
      </ac:parameter><ac:rich-text-body><ul><li><ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="Importer API: Parsing" /></ac:link></li><li><ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="Importer API: Mapping" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="two_equal"><ac:layout-cell><p><br /></p></ac:layout-cell><ac:layout-cell><p> </p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=137986184 space=ALFP2024x version=1 -->
## PAGE 00043: Importing Alf

- page_id: `137986184`
- space_key: `ALFP2024x`
- source_url: https://docs.nomagic.com/spaces/ALFP2024x/pages/137986184/Importing+Alf
- version_number: 1
- version_date: `2023-09-22T11:48:53.050+02:00`
- ancestors: Alf Plugin Documentation > User Guide
- labels: []

### NORMALIZED CONTENT

Alf may be used in MagicDraw to textually specify detailed behavior. However, the Alf specification also provides an *extended* level that includes notation for the static modeling constructs of Foundational UML, including packages, classes, data types, associations and signals. An Alf representation such as this may be imported from a file into MagicDraw, creating the specified model elements and inserting Alf bodies as appropriate.

To import an Alf file from the Welcome Screen:

1. From the Welcome Screen (i.e, with no projects open), select File > Import From > Alf File .
2. Choose the file to be imported and click Open .
3. A new, untitled project is created, and the selected Alf file is imported into it.
4. Save the project.

If there are any syntactic errors or constraint violations in the Alf being imported, the import will fail and no model will be created in MagicDraw. The Notification Window will open to show the compilation errors.

It is possible for a model to be represented by multiple Alf files that reference each other. In this case, you should select the root file as the one to import. When the import process identifies a reference that cannot be resolved within the file being imported, it will attempt to find another associated file in which the reference can be resolved. When importing, the Alf plugin uses the conventions of the Alf Reference Implementation when resolving Alf unit names to file name, considering the directory of the selected file to be the "model directory" (for more information, see the Alf Reference Implementation documentation [here](https://github.com/ModelDriven/Alf-Reference-Implementation/wiki/Unit-Management#the-model-directory)).

To import an Alf file into an existing project:

1. Open the existing project you want to import into.
2. Select File > Import From > Alf File .
3. Choose the file to be imported and click Open .
4. The selected Alf file will be imported, with new model elements created within the open project.

If the Alf in the imported file contains external references, then the Alf compiler will attempt to resolve these against existing elements within the model, before searching for another file from which to resolve them.

If you have projects open, and you want to import Alf into a new project, but don't want to close the currently open projects, then first use **File > New Project** to create a [CONFLUENCE_PAGE title='Alf project template' space='ALFP2024x'], and import the Alf file into that, as above.

As an example, consider the following simple *Address Book Model* represented in Alf:

```text
select e (e.name == name)[1];
            if (entry == null) {
                this.entry->add(new Entry(name,address));
            } else {
                entry.address = address;
            }
        }
        
        public get(in name: String): String[0..1] {
            return this.entry->select e (e.name == name)[1].address;
        }
    }

}]]>
```

Importing the example above into MagicDraw results in the model structure shown below. Note that not diagrams are created by the import process. You will need to create any diagrams by hand once the import is completed.

[IMAGE alt='' src='']

###### Imported Address Book Model

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p>Alf may be used in MagicDraw to textually specify detailed behavior. However, the Alf specification also provides an <em>extended</em> level that includes notation for the static modeling constructs of Foundational UML, including packages, classes, data types, associations and signals. An Alf representation such as this may be imported from a file into MagicDraw, creating the specified model elements and inserting Alf bodies as appropriate.</p><p><br /></p><p>To import an Alf file from the Welcome Screen:</p><hr /><ol><li>From the Welcome Screen (i.e, with no projects open), select <strong>File &gt; Import From &gt; Alf File</strong>.</li><li>Choose the file to be imported and click <strong>Open</strong>.</li><li>A new, untitled project is created, and the selected Alf file is imported into it.</li><li>Save the project.</li></ol><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="ce2e9b1b-d0ac-4988-9c83-dfc8d7f9705c"><ac:rich-text-body><p>If there are any syntactic errors or constraint violations in the Alf being imported, the import will fail and no model will be created in MagicDraw. The Notification Window will open to show the compilation errors.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="c580b2ed-bf7b-4df1-9dd1-f5b6efee644a"><ac:rich-text-body><p>It is possible for a model to be represented by multiple Alf files that reference each other. In this case, you should select the root file as the one to import. When the import process identifies a reference that cannot be resolved within the file being imported, it will attempt to find another associated file in which the reference can be resolved. When importing, the Alf plugin uses the conventions of the Alf Reference Implementation when resolving Alf unit names to file name, considering the directory of the selected file to be the &quot;model directory&quot; (for more information, see the Alf Reference Implementation documentation <a href="https://github.com/ModelDriven/Alf-Reference-Implementation/wiki/Unit-Management#the-model-directory">here</a>).</p></ac:rich-text-body></ac:structured-macro><p><br /></p><p>To import an Alf file into an existing project:</p><hr /><ol><li>Open the existing project you want to import into.</li><li>Select <strong>File &gt; Import From &gt; Alf File</strong>.</li><li>Choose the file to be imported and click <strong>Open</strong>.</li><li>The selected Alf file will be imported, with new model elements created within the open project.</li></ol><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="17bce7ad-72cf-440d-959c-11c5cf9947c8"><ac:rich-text-body><p>If the Alf in the imported file contains external references, then the Alf compiler will attempt to resolve these against existing elements within the model, before searching for another file from which to resolve them.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="07ff26fa-515b-4c48-819e-c41e4df83c17"><ac:rich-text-body><p>If you have projects open, and you want to import Alf into a new project, but don't want to close the currently open projects, then first use <strong>File &gt; New Project</strong> to create a <ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="Alf project template" /><ac:plain-text-link-body><![CDATA[new Alf project]]></ac:plain-text-link-body></ac:link>, and import the Alf file into that, as above.</p></ac:rich-text-body></ac:structured-macro><p><br /></p><p>As an example, consider the following simple <em>Address Book Model</em> represented in Alf:</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="32a445ac-1716-4faa-b52a-afcab540b15e"><ac:parameter ac:name="language">text</ac:parameter><ac:plain-text-body><![CDATA[package 'Address Book Model' {

    public class Entry {
        public name: String;
        public address: String;
        
        @Create public Entry(in name: String, in address: String) {
            this.name = name;
            this.address = address;
        }
    }
        
    public assoc AddressBook_Entry {
        public addressBook: AddressBook;
        public entry: compose Entry[*];
    }
        
    public class AddressBook {
        public add(in name: String, in address: String) {
            entry = this.entry->select e (e.name == name)[1];
            if (entry == null) {
                this.entry->add(new Entry(name,address));
            } else {
                entry.address = address;
            }
        }
        
        public get(in name: String): String[0..1] {
            return this.entry->select e (e.name == name)[1].address;
        }
    }

}]]></ac:plain-text-body></ac:structured-macro><p>Importing the example above into MagicDraw results in the model structure shown below. Note that not diagrams are created by the import process. You will need to create any diagrams by hand once the import is completed.</p><p><ac:image ac:align="center" ac:width="400"><ri:attachment ri:filename="Importing_Alf-Address_Book_Model.png"><ri:page ri:space-key="ALFP2024x" ri:content-title="Importing Alf" /></ri:attachment></ac:image></p><h6 style="text-align: center;">Imported Address Book Model</h6><p><br /></p></ac:layout-cell><ac:layout-cell><p> </p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="two_equal"><ac:layout-cell><p><br /></p></ac:layout-cell><ac:layout-cell><p> </p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=137986075 space=ALFP2024x version=1 -->
## PAGE 00044: Installation

- page_id: `137986075`
- space_key: `ALFP2024x`
- source_url: https://docs.nomagic.com/spaces/ALFP2024x/pages/137986075/Installation
- version_number: 1
- version_date: `2023-09-22T11:48:45.600+02:00`
- ancestors: Alf Plugin Documentation > User Guide > Getting Started
- labels: []

### NORMALIZED CONTENT

#### NOTE: Note

Note

The Alf Plugin of the current version requires that [Cameo Simulation Toolkit](https://docs.nomagic.com/display/CSTTWRT/Installation+and+licensing) of the current version is already installed.

For information regarding installation, licensing, and system requirements, visit the [CONFLUENCE_PAGE title='Installation, licensing, and system requirements' space='IL2024x'] page.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><br /></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="b1a275f0-42fe-43de-bd56-e6a2a76c91e3"><ac:parameter ac:name="title">Note</ac:parameter><ac:rich-text-body><p>The Alf Plugin of the current version requires that <a href="https://docs.nomagic.com/display/CSTTWRT/Installation+and+licensing">Cameo Simulation Toolkit</a> of the current version is already installed.</p></ac:rich-text-body></ac:structured-macro><p class="with-breadcrumbs">For information regarding installation, licensing, and system requirements, visit the <ac:link><ri:page ri:space-key="IL2024x" ri:content-title="Installation, licensing, and system requirements" /></ac:link> page.</p>
````

<!--NOMAGIC_PAGE id=137986074 space=ALFP2024x version=1 -->
## PAGE 00045: Introduction

- page_id: `137986074`
- space_key: `ALFP2024x`
- source_url: https://docs.nomagic.com/spaces/ALFP2024x/pages/137986074/Introduction
- version_number: 1
- version_date: `2023-09-22T11:48:45.454+02:00`
- ancestors: Alf Plugin Documentation > User Guide > Getting Started
- labels: []

### NORMALIZED CONTENT

Alf (the *[Action Language for Foundation UML](http://www.omg.org/spec/ALF)*) is a textual language for coding detailed, executable behavior within an overall UML model. Alf is a standard of the Object Management Group (OMG), which is also the organization that maintains the UML specification. Alf is one of a suite of OMG specifications related to defining precise execution semantics for UML, building on the original [Foundational UML (fUML)](http://www.omg.org/spec/FUML) specification.

The Alf Plugin for MagicDraw allows you to use the Alf language within MagicDraw. It implements Alf at what is formally called the "Full Conformance" level. That is, it provides a complete action language for representing behavior within a UML model created in the usual way in MagicDraw.

Within MagicDraw, the Alf Plugin provides both a syntax-aware editor for entering and updating Alf code and a compiler for translating Alf code into fUML activity models. [Cameo Simulation Toolkit](https://docs.nomagic.com/display/CSTTWRT/Cameo+Simulation+Toolkit+Documentation) (CST) provides an engine for executing fUML activities within MagicDraw. Therefore, when used in conjunction with CST, behavioral specifications written using Alf code are fully executable in the context of class, activity and state machine models.

The Alf Users Guide provides basic documentation on how to use the Alf Plugin within MagicDraw. It is not intended as an introduction to Alf and presumes a general understanding of the language and its use within a UML model. It also presumes knowledge of Cameo Simulation Toolkit, in order to execute the models within which Alf is being used. (For more information on the Alf language itself, see the formal [Alf specification](https://www.omg.org/spec/ALF) or the informal [Reference Guide](https://github.com/ModelDriven/Alf-Reference-Implementation/blob/master/org.modeldriven.alf/doc/Alf%20v1.1%20Language%20Reference%20Guide.pdf) provided with the Alf Reference Implementation.)

#### PANEL: Related Pages

Related Pages

- Cameo Simulation Toolkit Documentation
- [CONFLUENCE_PAGE title='Installation' space='ALFP2024x']
- [CONFLUENCE_PAGE title='Samples' space='ALFP2024x']
- [CONFLUENCE_PAGE title='Alf project template' space='ALFP2024x']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p>Alf (the <em><a href="http://www.omg.org/spec/ALF">Action Language for Foundation UML</a></em>) is a textual language for coding detailed, executable behavior within an overall UML model. Alf is a standard of the Object Management Group (OMG), which is also the organization that maintains the UML specification. Alf is one of a suite of OMG specifications related to defining precise execution semantics for UML, building on the original <a href="http://www.omg.org/spec/FUML">Foundational UML (fUML)</a> specification.</p><p>The Alf Plugin for MagicDraw allows you to use the Alf language within MagicDraw. It implements Alf at what is formally called the &quot;Full Conformance&quot; level. That is, it provides a complete action language for representing behavior within a UML model created in the usual way in MagicDraw.</p><p>Within MagicDraw, the Alf Plugin provides both a syntax-aware editor for entering and updating Alf code and a compiler for translating Alf code into fUML activity models. <a href="https://docs.nomagic.com/display/CSTTWRT/Cameo+Simulation+Toolkit+Documentation">Cameo Simulation Toolkit</a> (CST) provides an engine for executing fUML activities within MagicDraw. Therefore, when used in conjunction with CST, behavioral specifications written using Alf code are fully executable in the context of class, activity and state machine models.</p><p>The Alf Users Guide provides basic documentation on how to use the Alf Plugin within MagicDraw. It is not intended as an introduction to Alf and presumes a general understanding of the language and its use within a UML model. It also presumes knowledge of Cameo Simulation Toolkit, in order to execute the models within which Alf is being used. (For more information on the Alf language itself, see the formal <a href="https://www.omg.org/spec/ALF">Alf specification</a> or the informal <a href="https://github.com/ModelDriven/Alf-Reference-Implementation/blob/master/org.modeldriven.alf/doc/Alf%20v1.1%20Language%20Reference%20Guide.pdf">Reference Guide</a> provided with the Alf Reference Implementation.)</p></ac:layout-cell><ac:layout-cell><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="00715427-706e-4488-9381-c4fd16b31690"><ac:parameter ac:name="title">Related Pages</ac:parameter><ac:rich-text-body><ul><li><a href="https://docs.nomagic.com/display/CSTTWRT/Cameo+Simulation+Toolkit+Documentation">Cameo Simulation Toolkit Documentation</a><br /><br /></li><li><ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="Installation" /><ac:plain-text-link-body><![CDATA[Alf plugin installation]]></ac:plain-text-link-body></ac:link></li><li><ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="Samples" /><ac:plain-text-link-body><![CDATA[Alf samples]]></ac:plain-text-link-body></ac:link></li><li><ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="Alf project template" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=137986187 space=ALFP2024x version=1 -->
## PAGE 00046: Introduction to the Alf API

- page_id: `137986187`
- space_key: `ALFP2024x`
- source_url: https://docs.nomagic.com/spaces/ALFP2024x/pages/137986187/Introduction+to+the+Alf+API
- version_number: 1
- version_date: `2023-09-22T11:48:53.349+02:00`
- ancestors: Alf Plugin Documentation > Developer Guide
- labels: []

### NORMALIZED CONTENT

The Alf Plugin provides a basic Application Programming Interface (API) that can be used to programmatically compile Alf code and import Alf files into a UML model. The Alf API classes are package in the *alf_api.jar* file located at:

- <MagicDraw installation directory>/plugins/com.nomagic.magicdraw.alf/alf_api.jar

You can also find JavaDoc for the Alf API at:

- <MagicDraw installation directory>/openapi/docs/alf/AlfJavaDoc.zip

For general information about creating a new MagicDraw plugin using Open APIs, see the MagicDraw [CONFLUENCE_PAGE title='Developer Guide' space='MD190'].

Before using the Alf Open API in your Java code, make sure that*alf-base.jar, alf.jar* and*alf_api.jar*have all been added to your IDE classpath.

#### PANEL: Related Pages

Related Pages

- [CONFLUENCE_PAGE title='Compiler API' space='ALFP2024x']
- [CONFLUENCE_PAGE title='Importer API' space='ALFP2024x']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p> </p><p>The Alf Plugin provides a basic Application Programming Interface (API) that can be used to programmatically compile Alf code and import Alf files into a UML model. The Alf API classes are package in the <em>alf_api.jar</em> file located at:</p><ul><li><em>&lt;MagicDraw installation directory&gt;/plugins/com.nomagic.magicdraw.alf/alf_api.jar</em></li></ul><p>You can also find JavaDoc for the Alf API at:</p><ul><li><em>&lt;MagicDraw installation directory&gt;/openapi/docs/alf/AlfJavaDoc.zip</em></li></ul><p>For general information about creating a new MagicDraw plugin using Open APIs, see the MagicDraw <ac:link><ri:page ri:space-key="MD190" ri:content-title="Developer Guide" /></ac:link>.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="2330889b-cd1e-4182-bc87-162f0aeaf5b6"><ac:rich-text-body><p><span>Before using the Alf Open API in your Java code, make sure that </span><em>alf-base.jar, alf.jar</em> and<em> alf_api.jar</em><span> have all been added to your IDE classpath.</span></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell><ac:layout-cell><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="97dbcebf-31e5-437e-a932-c13d87d59cf3"><ac:parameter ac:name="title">
       Related Pages
      </ac:parameter><ac:rich-text-body><ul><li><ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="Compiler API" /></ac:link></li><li><ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="Importer API" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p> </ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=137986115 space=ALFP2024x version=1 -->
## PAGE 00047: Making invocations through ports

- page_id: `137986115`
- space_key: `ALFP2024x`
- source_url: https://docs.nomagic.com/spaces/ALFP2024x/pages/137986115/Making+invocations+through+ports
- version_number: 1
- version_date: `2023-09-22T11:48:48.703+02:00`
- ancestors: Alf Plugin Documentation > User Guide > Working with Alf > Using Alf in Class models
- labels: []

### NORMALIZED CONTENT

You can access a Port using the usual Alf notation for a Property. Sending a Signal or calling an Operation on the Port (consistent with the Port's type) then makes an invocation through the Port and across any Connector attached to the Port. That is, the Alf invocation is mapped into an invocation action whose **onPort** property is set to the target Port.

#### TIP: Tip

Tip

The Alf language specification requires that the type of a Port (or any Property) that is the target of a Signal send have a Signal Reception for the Signal being sent. However, the Alf Plugin implements an extension to Alf that allows the sending of a Signal without having to target a Reception. The name of the Signal being sent must be visible in the namespace of the sender, which may require that the Signal (or its containing Package) be imported. And the target Port (or other Property) must still have a type (which may be an Interface or a Class).

[IMAGE alt='' src='']

###### Using Alf to send Signals through a Port

#### PANEL: Related pages

Related pages

- [CONFLUENCE_PAGE title='The Alf editor' space='ALFP2024x']
- [CONFLUENCE_PAGE title='The Alf compiler' space='ALFP2024x']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p>You can access a Port using the usual Alf notation for a Property. Sending a Signal or calling an Operation on the Port (consistent with the Port's type) then makes an invocation through the Port and across any Connector attached to the Port. That is, the Alf invocation is mapped into an invocation action whose <strong>onPort</strong> property is set to the target Port.</p><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="ed23ffc3-e71c-435d-a6bb-9836a877e834"><ac:parameter ac:name="title">Tip</ac:parameter><ac:rich-text-body><p>The Alf language specification requires that the type of a Port (or any Property) that is the target of a Signal send have a Signal Reception for the Signal being sent. However, the Alf Plugin implements an extension to Alf that allows the sending of a Signal without having to target a Reception. The name of the Signal being sent must be visible in the namespace of the sender, which may require that the Signal (or its containing Package) be imported. And the target Port (or other Property) must still have a type (which may be an Interface or a Class).</p></ac:rich-text-body></ac:structured-macro><p><ac:image ac:align="center"><ri:attachment ri:filename="Making_An_Invocation_Through_A_Port.png"><ri:page ri:space-key="ALFP2024x" ri:content-title="Making invocations through ports" /></ri:attachment></ac:image></p><h6 style="text-align: center;">Using Alf to send Signals through a Port</h6></ac:layout-cell><ac:layout-cell><p> </p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="3d989ba0-f93c-4bba-abf5-b26648f4b158"><ac:parameter ac:name="title">Related pages</ac:parameter><ac:rich-text-body><ul><li><ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="The Alf editor" /></ac:link></li><li><ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="The Alf compiler" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=137986083 space=ALFP2024x version=1 -->
## PAGE 00048: Ordering

- page_id: `137986083`
- space_key: `ALFP2024x`
- source_url: https://docs.nomagic.com/spaces/ALFP2024x/pages/137986083/Ordering
- version_number: 1
- version_date: `2023-09-22T11:48:46.545+02:00`
- ancestors: Alf Plugin Documentation > User Guide > Getting Started > Samples
- labels: []

### NORMALIZED CONTENT

The Ordering model demonstrates the use of Alf as the action language within an executable model using State Machines. It includes the following diagrams:

- Order Classes – A Class diagram of an Order consisting of multiple OrderLine Items , placed by a Customer, which may be paid using a CreditCard.
- Order_Behavior – A State Machine diagram of the active Behavior of an Order.
- CreditCardCharge_Behavior – A State Machine diagram of the active Behavior of a CreditCardCharge (this is just a stub for testing purposes).
- Customer_Behavior – A State Machine diagram of the active Behavior of a Customer (this is just a stub for testing purposes).
- Test – A Class diagram of a simple Test Class with a classifier behavior that acts as a test driver.

Alf is used to define the behavior of all Operations in the *Order Classes* model, entry Behaviors in all the state machines and the classifier behavior for *Test.* To view any of the Alf code, open the [CONFLUENCE_PAGE title='The Alf editor' space='ALFP2024x'] window (select **Windows > Alf**) and then select the desired Operation, entry Behavior or Activity. The Alf code will appear in the window.

To run the test, do either of the following

- Press the start button on the main toolbar.
- Right-click OrderingSimConfig and select Simulation > Run .

#### PANEL: Related pages

Related pages

[CONFLUENCE_PAGE title='Using Alf for Operation methods' space='ALFP2024x']

[CONFLUENCE_PAGE title='Using Alf for State Behaviors' space='ALFP2024x']

[CONFLUENCE_PAGE title='Using Alf for classifier behaviors' space='ALFP2024x']

[CONFLUENCE_PAGE title='Running a model with Alf' space='ALFP2024x']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p>The Ordering model demonstrates the use of Alf as the action language within an executable model using State Machines. It includes the following diagrams:</p><ul><li><em>Order Classes</em> – A Class diagram of an <em>Order</em> consisting of multiple <em>OrderLine</em><em>Items</em><em>,</em> placed by a <em>Customer,</em> which may be paid using a <em>CreditCard.</em></li><li><em>Order_Behavior</em> – A State Machine diagram of the active Behavior of an <em>Order.</em></li><li><em>CreditCardCharge_Behavior</em> – A State Machine diagram of the active Behavior of a <em>CreditCardCharge</em> (this is just a stub for testing purposes).</li><li><em>Customer_Behavior</em> – A State Machine diagram of the active Behavior of a <em>Customer</em> (this is just a stub for testing purposes).</li><li><em>Test</em> – A Class diagram of a simple <em>Test</em> Class with a classifier behavior that acts as a test driver.</li></ul><p>Alf is used to define the behavior of all Operations in the <em>Order Classes</em> model, entry Behaviors in all the state machines and the classifier behavior for <em>Test.</em> To view any of the Alf code, open the <ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="The Alf editor" /><ac:plain-text-link-body><![CDATA[Alf editor]]></ac:plain-text-link-body></ac:link> window (select <strong>Windows &gt; Alf</strong>) and then select the desired Operation, entry Behavior or Activity. The Alf code will appear in the window.</p><p><br /></p><p>To run the test, do either of the following</p><hr /><ul><li>Press the start button on the main toolbar.</li><li>Right-click <strong>OrderingSimConfig</strong> and select <strong>Simulation </strong>&gt;<strong> Run</strong>.</li></ul></ac:layout-cell><ac:layout-cell><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="3b65c267-334e-4d52-a600-b60aeebb7c78"><ac:parameter ac:name="title">Related pages</ac:parameter><ac:rich-text-body><p><ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="Using Alf for Operation methods" /></ac:link></p><p><ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="Using Alf for State Behaviors" /></ac:link></p><p><ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="Using Alf for classifier behaviors" /></ac:link></p><p><ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="Running a model with Alf" /></ac:link></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=137986181 space=ALFP2024x version=2 -->
## PAGE 00049: Running a model with Alf

- page_id: `137986181`
- space_key: `ALFP2024x`
- source_url: https://docs.nomagic.com/spaces/ALFP2024x/pages/137986181/Running+a+model+with+Alf
- version_number: 2
- version_date: `2023-10-10T08:15:56.972+02:00`
- ancestors: Alf Plugin Documentation > User Guide
- labels: []

### NORMALIZED CONTENT

The Alf code in your project is not executed directly ([CONFLUENCE_PAGE title='Alf as scripting language' space='']). Rather, it is translated by the[CONFLUENCE_PAGE title='The Alf compiler' space='']into UML Activities within the larger model containing the Alf code. These Activities can then be executed using [CONFLUENCE_PAGE title='Cameo Simulation Toolkit Documentation' space='CSTTWRT'] (CST), as part of an overall simulation of your UML model.

A simulation of a model that contains Alf code is run as for any other executable model using CST. Either click on an executable element in your model and select **Simulation > Run** (or **Run in Context**, as appropriate) or create a [CONFLUENCE_PAGE title='Simulation Configuration and UI modeling' space='CSTTWRT']and run that.

If an active Class is instantiated using an Alf instance creation expression, then the classifier behavior for the Class is explicitly started on the newly created instance *after* the completion of initialization of the instance. However, the default MagicDraw option is to **Autostart Active Objects**, in which case the classifier behavior for an active object will be automatically started as soon as the object is created. While MagicDraw will ensure that any Properties with default values are properly initialized before the classifier behavior is started, if you have initialization code in a constructor for an active Class, then this will *not* execute before the classifier behavior starts.

Therefore, if you intend to instantiate an active Class from Alf code using a constructor that carries out initialization on which the classifier behavior depends, it is important to make sure that the classifier behavior waits for the constructor execution to complete. You can do this by having the classifier behavior wait for a special *Start* Signal before carrying out any other behavior, and having the constructor invoke *this.Start()* when it is done with its initialization behavior. (If the classifier behavior is an activity, then use an Accept Event Action to wait for the Start signal. If the classifier behavior is a State Machine, have the State Machine transition from its initial Pseudostate to a *Waiting* State that is exited by a Transition triggered by the *Start* Signal.)

Alternatively, you can turn off the **Autostart Active Objects** option:

1. Select Options > Envronment from the main menu.
2. Choose Simulation (the last option group on the left).
3. Uncheck the Autostart Active Objects option under Simulation Frameworks (so it is false ).

However, doing this will turn off the option globally for all projects, which may cause some other simulation projects to not work. You can turn this option off for just a specific project if you use a simulation configuration, by setting the [CONFLUENCE_PAGE title='Automatic start of active objects' space='CSTTWRT']**Autostart Active Objects****property to *false* in your configuration.

#### PANEL: Related pages

Related pages

- Alf Plugin
  - [CONFLUENCE_PAGE title='The Alf compiler' space='']
- Cameo Simulation Toolkit
  - [CONFLUENCE_PAGE title='Simulation Configuration and UI modeling' space='CSTTWRT']
  - [CONFLUENCE_PAGE title='Simulation debugging' space='CSTTWRT']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p><span style="color: rgb(62,63,64);">The Alf code in your project is not executed directly (</span><ac:link><ri:page ri:content-title="Alf as scripting language" /><ac:plain-text-link-body><![CDATA[unless Alf Script is used]]></ac:plain-text-link-body></ac:link><span style="color: rgb(62,63,64);">). Rather, it is translated by the </span><ac:link><ri:page ri:content-title="The Alf compiler" /><ac:plain-text-link-body><![CDATA[Alf compiler]]></ac:plain-text-link-body></ac:link><span style="color: rgb(62,63,64);"><span> </span>into UML Activities within the larger model containing the Alf code.<span> </span></span> These Activities can then be executed using <ac:link><ri:page ri:space-key="CSTTWRT" ri:content-title="Cameo Simulation Toolkit Documentation" /><ac:plain-text-link-body><![CDATA[Cameo Simulation Toolkit]]></ac:plain-text-link-body></ac:link> (CST), as part of an overall simulation of your UML model.</p><p>A simulation of a model that contains Alf code is run as for any other executable model using CST. Either click on an executable element in your model and select <strong>Simulation &gt; Run</strong> (or <strong>Run in Context</strong>, as appropriate) or create a <ac:link><ri:page ri:space-key="CSTTWRT" ri:content-title="Simulation Configuration and UI modeling" /><ac:plain-text-link-body><![CDATA[simulation configuration ]]></ac:plain-text-link-body></ac:link>and run that.</p><ac:structured-macro ac:name="warning" ac:schema-version="1" ac:macro-id="ceea5383-ed17-4e04-8ad7-6ecabe3358b9"><ac:rich-text-body><p>If an active Class is instantiated using an Alf instance creation expression, then the classifier behavior for the Class is explicitly started on the newly created instance <em>after</em> the completion of initialization of the instance. However, the default MagicDraw option is to <strong>Autostart Active Objects</strong>, in which case the classifier behavior for an active object will be automatically started as soon as the object is created. While MagicDraw will ensure that any Properties with default values are properly initialized before the classifier behavior is started, if you have initialization code in a constructor for an active Class, then this will <em>not</em> execute before the classifier behavior starts.</p><p>Therefore, if you intend to instantiate an active Class from Alf code using a constructor that carries out initialization on which the classifier behavior depends, it is important to make sure that the classifier behavior waits for the constructor execution to complete. You can do this by having the classifier behavior wait for a special <em>Start</em> Signal before carrying out any other behavior, and having the constructor invoke <em>this.Start()</em> when it is done with its initialization behavior. (If the classifier behavior is an activity, then use an Accept Event Action to wait for the Start signal. If the classifier behavior is a State Machine, have the State Machine transition from its initial Pseudostate to a <em>Waiting</em> State that is exited by a Transition triggered by the <em>Start</em> Signal.)</p><p>Alternatively, you can turn off the <strong>Autostart Active Objects</strong> option:</p><ol><li>Select <strong>Options &gt; Envronment</strong> from the main menu.</li><li>Choose <strong>Simulation</strong> (the last option group on the left).</li><li>Uncheck the <strong>Autostart Active Objects</strong> option under <strong>Simulation Frameworks</strong> (so it is <em>false</em>).</li></ol><p>However, doing this will turn off the option globally for all projects, which may cause some other simulation projects to not work. You can turn this option off for just a specific project if you use a simulation configuration, by setting the <ac:link><ri:page ri:space-key="CSTTWRT" ri:content-title="Automatic start of active objects" /><ac:link-body><strong>Autostart Active Objects</strong><em> </em>property</ac:link-body></ac:link> to <em>false</em> in your configuration.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell><ac:layout-cell><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="cd3238e7-9c10-499e-b3c0-2819d1b4b491"><ac:parameter ac:name="title">Related pages</ac:parameter><ac:rich-text-body><ul><li>Alf Plugin<ul><li><ac:link><ri:page ri:content-title="The Alf compiler" /></ac:link></li></ul></li><li>Cameo Simulation Toolkit<ul><li><ac:link><ri:page ri:space-key="CSTTWRT" ri:content-title="Simulation Configuration and UI modeling" /><ac:plain-text-link-body><![CDATA[Simulation configuration and UI modeling]]></ac:plain-text-link-body></ac:link></li><li><ac:link><ri:page ri:space-key="CSTTWRT" ri:content-title="Simulation debugging" /></ac:link></li></ul></li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=137986203 space=ALFP2024x version=1 -->
## PAGE 00050: Running the Hello World activity

- page_id: `137986203`
- space_key: `ALFP2024x`
- source_url: https://docs.nomagic.com/spaces/ALFP2024x/pages/137986203/Running+the+Hello+World+activity
- version_number: 1
- version_date: `2023-09-22T11:48:55.338+02:00`
- ancestors: Alf Plugin Documentation > Tutorials > Alf Tutorial 1: Hello World
- labels: []

### NORMALIZED CONTENT

Once the Alf code for an Activity has been compiled, the Activity can be executed using Cameo Simulation Toolkit, just as for an Activity that had been entered using a graphical Activity diagram.

To run *Hello World*

1. Right click on Hello World in the Model Browser and select Simulation > Run . The Simulation window will appear, with Hello World listed as "Ready" under the Sessions pane. [ATTACHMENT filename='Hello_World-Running.png']
2. Click on the **Start** button at the top left of the Simulation window. The output *Hello World!* should appear in the Console pane. 
 
[IMAGE alt='' src='']

#### PANEL: Related pages

Related pages

- [CONFLUENCE_PAGE title='Running a model with Alf' space='ALFP2024x']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p>Once the Alf code for an Activity has been compiled, the Activity can be executed using Cameo Simulation Toolkit, just as for an Activity that had been entered using a graphical Activity diagram.</p><p><br /></p><p>To run <em>Hello World</em></p><hr /><ol><li>Right click on <em>Hello World</em> in the Model Browser and select <strong>Simulation &gt; Run</strong>. The Simulation window will appear, with <em>Hello World</em> listed as &quot;Ready&quot; under the Sessions pane.<br /><br /><ac:image ac:height="250"><ri:attachment ri:filename="Hello_World-Running.png"><ri:page ri:space-key="ALFP2024x" ri:content-title="Running the Hello World activity" /></ri:attachment></ac:image><br /><br /></li><li><p class="auto-cursor-target">Click on the <strong>Start</strong> button at the top left of the Simulation window. The output <em>Hello World!</em> should appear in the Console pane.<br /><br /><ac:image ac:height="250"><ri:attachment ri:filename="Hello_World-Output.png"><ri:page ri:space-key="ALFP2024x" ri:content-title="Running the Hello World activity" /></ri:attachment></ac:image></p></li></ol></ac:layout-cell><ac:layout-cell><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="364b7519-a3a0-429a-8563-137452db5272"><ac:parameter ac:name="title">Related pages</ac:parameter><ac:rich-text-body><ul><li><ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="Running a model with Alf" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=137986254 space=ALFP2024x version=1 -->
## PAGE 00051: Running the Stopwatch model

- page_id: `137986254`
- space_key: `ALFP2024x`
- source_url: https://docs.nomagic.com/spaces/ALFP2024x/pages/137986254/Running+the+Stopwatch+model
- version_number: 1
- version_date: `2023-09-22T11:48:59.148+02:00`
- ancestors: Alf Plugin Documentation > Tutorials > Alf Tutorial 3: Stopwatch
- labels: []

### NORMALIZED CONTENT

The *StopWatch* class is now ready to be executed. You can execute the *StopWatch* class either from the Model Browser or from the Class diagram.

To run the *StopWatch* Class

1. Right click on the StopWatch class in the Model Browser and select Simulation > Run (see the following figure). [ATTACHMENT filename='Stopwatch-Running_StopWatch.png']
2. The Simulation window will open. It contains four tabs: Sessions, Console, Variables, and Breakpoints. At this point, an instance of the StopWatch class is created, which you can see in the Variables tab. In addition, a simulation session to execute the StopWatch class is created, which you can see tn the Sessions tab of the Simulation window. (See the following figure.) [ATTACHMENT filename='Stopwatch-Simulation_Session.png']
3. Click the **Start** button [ATTACHMENT filename='start_button.png'] on the Simulation window toolbar.

Once you have clicked the **Start** button, the classifier behavior of the *StopWatch* Class, which is the *StopWatch* State Machine, starts executing. A new session to execute the *StopWatch* state machine is created under the simulation session of the *StopWatch* class, and the *StopWatch* state machine diagram will be open and ready for the simulation.

The *StopWatch* State Machine execution will start from the initial Pseudostate and automatically move to the *ready* state because the Transition that connects the initial Pseudostate to the *ready* State does not have a defined trigger. When the *ready* State is entered, its entry Behavior is executed, which calls the *resetTime* operation. After this, the *StopWatch* State Machine is in the *ready* State, and the *time* attribute is set to 0 (see the following figure).

[IMAGE alt='' src=''] 
 
Now we want to trigger the *StopWatch* object to move from the *ready* State to the *running* State. To do this, we need to send a *start* signal to the *StopWatch* object. 
 
To send a *start* Signal to the *StopWatch* object

1. Select the StopWatch node in the Variables tab. The signals that can be sent to the StopWatch will be listed in the Trigger drop-down menu.
2. Select the start signal from the Trigger drop-down menu (see the following figure). [ATTACHMENT filename='Stopwatch-Triggering_start.png']

Once the *start* Signal has been sent, the *StopWatch* enters the *running* State. On entry to the *running* state, its entry Behavior is executed, which calls the *increaseTime* operation, incrementing the *time* attribute by 1 (as shown in the **Variables** tab in the figure below).

[IMAGE alt='' src='']

The *StopWatch* object stays in the *running* State, and the Time Event is triggered in this State every second. Therefore, a new simulation session will be created to call the *increaseTime* operation every second, and the *time* value will increment by one every time the operation is executed (see the following figure).

[IMAGE alt='' src=''] 
 
 While the *StopWatch* object is in the *running* state, we can send a *split* signal to trigger a transition to the *paused* state or send a *stop* signal to trigger a transition to the *stopped* state. 
 
 To send a *split* Signal to the *StopWatch* object

1. Select the StopWatch object in the Variables tab.
2. Select the split Signal from the Trigger drop-down menu on the Simulation window toolbar. (You may have to temporarily reduce the animation speed in order to be able to select a trigger before the Time Event fires.) The state of the StopWatch object will be changed to the paused state (see the following figure). [ATTACHMENT filename='Stopwatch-In_State_paused.png']

You can transition the paused *StopWatch* object to the *running* state by sending an *unsplit* Signal to the object. 
 
To send an *unsplit* Signal to the *StopWatch* object

1. Select the StopWatch object in the Variables tab.
2. Select the unsplit Signal from the Trigger drop-down menu on the Simulation window toolbar. The state of the StopWatch object will be changed to the running state (see the following figure), and the time value will start to continuously increase again. [ATTACHMENT filename='Stopwatch-Resuming_State_running.png']

To send a *stop* Signal to the *StopWatch* object

1. Select the StopWatch object in the Variables tab.
2. Select the stop Signal from the Trigger drop-down menu on the Simulation window toolbar. (You may have to temporarily reduce the animation speed in order to be able to select a trigger before the Time Event fires.) The state of the StopWatch object will be changed to the stopped state (see the following figure). [ATTACHMENT filename='Stopwatch-In_State_stopped.png']

In the *stopped* state, if the *reset* Signal is sent to the *StopWatch* object, the object will go to the ***ready*** State, and the *time* value will be reset to zero by calling the *resetTime* operation. If, instead, the *stop* Signal is sent to the object again, the object will go to the Final State, the simulation will stop, and all of the simulation sessions will be closed.

From this point, you can also explore additional features of Cameo Simulation Toolkit for executing the *StopWatch* model, as described in the CST Tutorial:

- Executing the StopWatch instance specification
- Executing the StopWatch using Simulation Configuration
- Creating User Interface mockups for the stopwatch model

#### PANEL: Related pages

Related pages

- Alf Plugin
  - [CONFLUENCE_PAGE title='Running a model with Alf' space='ALFP2024x']
- Cameo Simulation Toolkit
  - Executing the stopwatch model
  - Creating User Interface mockups for the stopwatch model

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p>The <em>StopWatch</em> class is now ready to be executed. You can execute the <em>StopWatch</em> class either from the Model Browser or from the Class diagram.</p><p>To run the <em>StopWatch</em> Class</p><hr /><ol><li>Right click on the <em>StopWatch</em> class in the Model Browser and select <strong>Simulation</strong> &gt; <strong>Run</strong> (see the following figure). <br /> <br /> <ac:image><ri:attachment ri:filename="Stopwatch-Running_StopWatch.png"><ri:page ri:space-key="ALFP2024x" ri:content-title="Running the Stopwatch model" /></ri:attachment></ac:image><br /><br /></li><li>The Simulation window will open. It contains four tabs: <strong>Sessions, Console, Variables,</strong> and <strong>Breakpoints.</strong> At this point, an instance of the StopWatch class is created, which you can see in the <strong>Variables</strong> tab. In addition, a simulation session to execute the <em>StopWatch</em> class is created, which you can see tn the <strong>Sessions</strong> tab of the Simulation window. (See the following figure.)<br /> <br /> <ac:image><ri:attachment ri:filename="Stopwatch-Simulation_Session.png"><ri:page ri:space-key="ALFP2024x" ri:content-title="Running the Stopwatch model" /></ri:attachment></ac:image><br /><br /></li><li>Click the <span> <strong>Start</strong> </span> button <ac:image><ri:attachment ri:filename="start_button.png"><ri:page ri:space-key="ALFP2024x" ri:content-title="Running the Stopwatch model" /></ri:attachment></ac:image> on the Simulation window toolbar. </li></ol><p><br class="atl-forced-newline" /> Once you have clicked the <strong>Start</strong> button, the classifier behavior of the <em>StopWatch</em> Class, which is the <em>StopWatch</em> State Machine, starts executing. A new session to execute the <em>StopWatch</em> state machine is created under the simulation session of the <em>StopWatch</em> class, and the <em>StopWatch</em> state machine diagram will be open and ready for the simulation.</p><p>The <em>StopWatch</em> State Machine execution will start from the initial Pseudostate and automatically move to the <em>ready</em> state because the Transition that connects the initial Pseudostate to the <em>ready</em> State does not have a defined trigger. When the <em>ready</em> State is entered, its entry Behavior is executed, which calls the <em>resetTime</em> operation. After this, the <em>StopWatch</em> State Machine is in the <em>ready</em> State, and the <em>time</em> attribute is set to 0 (see the following figure).</p><p><ac:image><ri:attachment ri:filename="Stopwatch-Simulation_Start.png"><ri:page ri:space-key="ALFP2024x" ri:content-title="Running the Stopwatch model" /></ri:attachment></ac:image> <br /> <br />Now we want to trigger the <em>StopWatch</em> object to move from the <em>ready</em> State to the <em>running</em> State. To do this, we need to send a <em>start</em> signal to the <em>StopWatch</em> object.  <br /> <br />To send a <em>start</em> Signal to the <em>StopWatch</em> object</p><hr /><ol><li>Select the <em>StopWatch</em> node in the <strong>Variables</strong> tab. The signals that can be sent to the <em>StopWatch</em> will be listed in the <strong>Trigger</strong> drop-down menu.</li><li>Select the <strong>start</strong> signal from the <strong>Trigger</strong> drop-down menu (see the following figure).<br /> <br /> <ac:image><ri:attachment ri:filename="Stopwatch-Triggering_start.png"><ri:page ri:space-key="ALFP2024x" ri:content-title="Running the Stopwatch model" /></ri:attachment></ac:image></li></ol><p><br class="atl-forced-newline" /> Once the <em>start</em> Signal has been sent, the <em>StopWatch</em> enters the <em>running</em> State. On entry to the <em>running</em> state, its entry Behavior is executed, which calls the <em>increaseTime</em> operation, incrementing the <em>time</em> attribute by 1 (as shown in the <strong>Variables</strong> tab in the figure below).</p><p><ac:image><ri:attachment ri:filename="Stopwatch-In_State_running.png"><ri:page ri:space-key="ALFP2024x" ri:content-title="Running the Stopwatch model" /></ri:attachment></ac:image></p><p>The <em>StopWatch</em> object stays in the <em>running</em> State, and the Time Event is triggered in this State every second. Therefore, a new simulation session will be created to call the <em>increaseTime</em> operation every second, and the <em>time</em> value will increment by one every time the operation is executed (see the following figure).</p><p><ac:image><ri:attachment ri:filename="Stopwatch-Executing_increaseTime.png"><ri:page ri:space-key="ALFP2024x" ri:content-title="Running the Stopwatch model" /></ri:attachment></ac:image><br /><br class="atl-forced-newline" /> While the <em>StopWatch</em> object is in the <em>running</em> state, we can send a <em>split</em> signal to trigger a transition to the <em>paused</em> state or send a <em>stop</em> signal to trigger a transition to the <em>stopped</em> state. <br class="atl-forced-newline" /> <br class="atl-forced-newline" /> To send a <em>split</em> Signal to the <em>StopWatch</em> object</p><hr /><ol><li>Select the <em>StopWatch</em> object in the <strong>Variables</strong> tab.</li><li>Select the <strong>split</strong> Signal from the <strong>Trigger</strong> drop-down menu on the Simulation window toolbar. (You may have to temporarily reduce the animation speed in order to be able to select a trigger before the Time Event fires.) The state of the <em>StopWatch</em> object will be changed to the <em>paused</em> state (see the following figure).<br /> <br /> <ac:image><ri:attachment ri:filename="Stopwatch-In_State_paused.png"><ri:page ri:space-key="ALFP2024x" ri:content-title="Running the Stopwatch model" /></ri:attachment></ac:image></li></ol><p><br /> You can transition the paused <em>StopWatch</em> object to the <em>running</em> state by sending an <em>unsplit</em> Signal to the object.<br class="atl-forced-newline" /> <br class="atl-forced-newline" />To send an <em>unsplit</em> Signal to the <em>StopWatch</em> object</p><hr /><ol><li>Select the <em>StopWatch</em> object in the <strong>Variables</strong> tab.</li><li>Select the <strong>unsplit</strong> Signal from the <strong>Trigger</strong> drop-down menu on the Simulation window toolbar. The state of the <em>StopWatch</em> object will be changed to the <em>running</em> state (see the following figure), and the <em>time</em> value will start to continuously increase again. <br /> <br /> <ac:image><ri:attachment ri:filename="Stopwatch-Resuming_State_running.png"><ri:page ri:space-key="ALFP2024x" ri:content-title="Running the Stopwatch model" /></ri:attachment></ac:image></li></ol><p><br class="atl-forced-newline" />To send a <em>stop</em> Signal to the <em>StopWatch</em> object</p><hr /><ol><li>Select the <em>StopWatch</em> object in the <strong>Variables</strong> tab.</li><li>Select the <strong>stop</strong> Signal from the <strong>Trigger</strong> drop-down menu on the Simulation window toolbar. (You may have to temporarily reduce the animation speed in order to be able to select a trigger before the Time Event fires.) The state of the <em>StopWatch</em> object will be changed to the <em>stopped</em> state (see the following figure).<br /> <br /> <ac:image><ri:attachment ri:filename="Stopwatch-In_State_stopped.png"><ri:page ri:space-key="ALFP2024x" ri:content-title="Running the Stopwatch model" /></ri:attachment></ac:image></li></ol><p><br /></p><p>In the <em>stopped</em> state, if the <em>reset</em> Signal is sent to the <em>StopWatch</em> object, the object will go to the <em> <strong>ready</strong> </em> State, and the <em>time</em> value will be reset to zero by calling the <em>resetTime</em> operation. If, instead, the <em>stop</em> Signal is sent to the object again, the object will go to the Final State, the simulation will stop, and all of the simulation sessions will be closed.</p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="2e469a75-cae5-4b6c-b1a6-53f9477316c5"><ac:rich-text-body><p>From this point, you can also explore additional features of Cameo Simulation Toolkit for executing the <em>StopWatch</em> model, as described in the CST Tutorial:</p><ul><li><a href="https://docs.nomagic.com/display/CSTTWRT/Executing+the+StopWatch+instance+specification">Executing the StopWatch instance specification</a></li><li><a href="https://docs.nomagic.com/display/CSTTWRT/Executing+the+StopWatch+using+Simulation+Configuration">Executing the StopWatch using Simulation Configuration</a></li><li><a href="https://docs.nomagic.com/display/CSTTWRT/Creating+User+Interface+mockups+for+the+stopwatch+model">Creating User Interface mockups for the stopwatch model</a></li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell><ac:layout-cell><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="248e740b-1cd3-4847-a584-a8f613827580"><ac:parameter ac:name="title">Related pages</ac:parameter><ac:rich-text-body><ul><li>Alf Plugin<ul><li><ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="Running a model with Alf" /></ac:link></li></ul></li><li>Cameo Simulation Toolkit<ul><li><a href="https://docs.nomagic.com/display/CSTTWRT/Executing+the+stopwatch+model">Executing the stopwatch model</a></li><li><a href="https://docs.nomagic.com/display/CSTTWRT/Creating+User+Interface+mockups+for+the+stopwatch+model">Creating User Interface mockups for the stopwatch model</a></li></ul></li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=137986079 space=ALFP2024x version=1 -->
## PAGE 00052: Samples

- page_id: `137986079`
- space_key: `ALFP2024x`
- source_url: https://docs.nomagic.com/spaces/ALFP2024x/pages/137986079/Samples
- version_number: 1
- version_date: `2023-09-22T11:48:46.006+02:00`
- ancestors: Alf Plugin Documentation > User Guide > Getting Started
- labels: []

### NORMALIZED CONTENT

The Alf Plugin comes with the sample models described in the related pages shown on the right of this page. To load one of these models, click on "Samples" on the MagicDraw Welcome Screen. If the Alf Plugin is installed, the pop-up Samples window will include the sample models in the section entitled **"Alf"**. Click on the name of the same model to open it.

[IMAGE alt='' src='']

###### Welcome screen showing Alf samples

#### PANEL: Related pages

Related pages

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p>The Alf Plugin comes with the sample models described in the related pages shown on the right of this page. To load one of these models, click on &quot;Samples&quot; on the MagicDraw Welcome Screen. If the Alf Plugin is installed, the pop-up Samples window will include the sample models in the section entitled <strong>&quot;Alf&quot;</strong>. Click on the name of the same model to open it.</p><p class="auto-cursor-target"><br /><ac:image><ri:attachment ri:filename="Samples-Window.png"><ri:page ri:space-key="ALFP2024x" ri:content-title="Samples" /></ri:attachment></ac:image></p><h6 style="text-align: center;">Welcome screen showing Alf samples</h6></ac:layout-cell><ac:layout-cell><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="aa741570-e042-40e0-a102-3cb870a949aa"><ac:parameter ac:name="title">Related pages</ac:parameter><ac:rich-text-body><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="80285c4e-c3db-480f-8439-f2c31021dd1a" /></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=137986216 space=ALFP2024x version=1 -->
## PAGE 00053: Testing the AddressBook

- page_id: `137986216`
- space_key: `ALFP2024x`
- source_url: https://docs.nomagic.com/spaces/ALFP2024x/pages/137986216/Testing+the+AddressBook
- version_number: 1
- version_date: `2023-09-22T11:48:56.716+02:00`
- ancestors: Alf Plugin Documentation > Tutorials > Alf Tutorial 2: Address Book
- labels: []

### NORMALIZED CONTENT

To test the *AddressBook* Class, we will create a simple *Test* Activity that puts an entry into an *AddressBook* and then gets it back again.

To create a *Test* Activity

1. Right click on the root Model in the Model Browser, select Create Element , and then select Activity.
2. Enter Test as the name of the Activity.
3. Click on Test , and open the [CONFLUENCE_PAGE title='The Alf editor' space='ALFP2024x'] window (select Windows > Alf ), if it isn't already open [CONFLUENCE_PAGE title='The Alf editor' space='ALFP2024x']
4. Type the Alf code shown in the figure below. [IMAGE alt='' src='']
5. When the text is correct, click Save .

To run the *Test*

1. Right click on Test in the Model Browser, and select Simulation > Run . [ATTACHMENT filename='Address_Book-Running_Test.png']
2. Click on the **Start** button. The output should appear in the **Console** pane, as shown in the figure below. 
 
[IMAGE alt='' src='']

#### PANEL: Related pages

Related pages

- [CONFLUENCE_PAGE title='The Alf editor' space='ALFP2024x']
- [CONFLUENCE_PAGE title='Running a model with Alf' space='ALFP2024x']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p>To test the <em>AddressBook</em> Class, we will create a simple <em>Test</em> Activity that puts an entry into an <em>AddressBook</em> and then gets it back again.</p><p><br /></p><p>To create a <em>Test</em> Activity</p><hr /><ol><li>Right click on the root <em>Model</em> in the Model Browser, select <strong>Create Element</strong>, and then select Activity.</li><li>Enter <em>Test</em> as the name of the Activity.</li><li>Click on <em>Test</em>, and open the <ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="The Alf editor" /><ac:plain-text-link-body><![CDATA[Alf editor]]></ac:plain-text-link-body></ac:link> window (select <strong>Windows &gt; Alf</strong>), if it isn't already open<ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="The Alf editor" /><ac:plain-text-link-body><![CDATA[.]]></ac:plain-text-link-body></ac:link></li><li><p class="auto-cursor-target">Type the Alf code shown in the figure below.</p><p class="auto-cursor-target"><ac:image><ri:attachment ri:filename="Address_Book-Creating_Test.png"><ri:page ri:space-key="ALFP2024x" ri:content-title="Testing the AddressBook" /></ri:attachment></ac:image><br /><br /></p></li><li>When the text is correct, click <strong>Save</strong>.</li></ol><p><br /></p><p>To run the <em>Test</em></p><hr /><ol><li>Right click on <em>Test</em> in the Model Browser, and select <strong>Simulation &gt; Run</strong>.<br /><br /><ac:image ac:height="250"><ri:attachment ri:filename="Address_Book-Running_Test.png"><ri:page ri:space-key="ALFP2024x" ri:content-title="Testing the AddressBook" /></ri:attachment></ac:image><br /><br /></li><li><p class="auto-cursor-target">Click on the <strong>Start</strong> button. The output should appear in the <strong>Console</strong> pane, as shown in the figure below.<br /><br /><ac:image ac:height="250"><ri:attachment ri:filename="Address_Book-Test_Output.png"><ri:page ri:space-key="ALFP2024x" ri:content-title="Testing the AddressBook" /></ri:attachment></ac:image></p></li></ol></ac:layout-cell><ac:layout-cell><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="f2a6ad00-ae77-4cb9-ae4f-f6274b12e48b"><ac:parameter ac:name="title">Related pages</ac:parameter><ac:rich-text-body><ul><li><ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="The Alf editor" /></ac:link></li><li><ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="Running a model with Alf" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=137986168 space=ALFP2024x version=1 -->
## PAGE 00054: The Alf compiler

- page_id: `137986168`
- space_key: `ALFP2024x`
- source_url: https://docs.nomagic.com/spaces/ALFP2024x/pages/137986168/The+Alf+compiler
- version_number: 1
- version_date: `2023-09-22T11:48:52.100+02:00`
- ancestors: Alf Plugin Documentation > User Guide > Compiling Alf
- labels: []

### NORMALIZED CONTENT

The *Alf compiler* is the part of the Alf plugin that carries out the compilation process. The Alf compiler is automatically invoked when you save Alf code into your model (unless you turn off automatic building; see [CONFLUENCE_PAGE title='Environment options' space='ALFP2024x']). The activity model resulting from an Alf compilation is also stored in your model. Exactly where it is stored depends on which kind of element the Alf code is the body.

##### Activity compilation

When the Alf compiler processes the Alf body of an Activity, the resulting Activity model is saved as the Activity Nodes and Edges owned within that Activity. The Alf text itself is stored in a Comment element owned by the Activity, which has the *TextualRepresentation* stereotype applied. (See also [CONFLUENCE_PAGE title='Using Alf to define Activities' space='ALFP2024x'] and [CONFLUENCE_PAGE title='Using Alf for Operation methods' space='ALFP2024x'].)

[IMAGE alt='' src='']

###### Activity compilation

The compilation of an activity may also result in certain auxiliary elements, such as Instance Specifications, that cannot be not stored within the Activity. These are generally inserted into the nearest Package containing the Activity (which may be the top-level Model). Also, in certain cases, template instantiations are saved in a special package called *$$Template Bindings*[CONFLUENCE_PAGE title='The Alf compiler' space='ALFP2024x'] (described below).

##### Opaque Behavior and Opaque Action compilation

When the Alf compiler processes the Alf body of an Opaque Behavior or Opaque Action, it creates a corresponding Activity in which to store the result of the compilation. For an Opaque Behavior, the generated Activity is saved as a child of the Opaque Behavior. For an Opaque Action, the generated Activity is saved as a child of the Activity containing the Opaque Action. In either case, the Activity is also linked to the original Opaque Behavior or Action by applying the *CompiledRepresentation* stereotype. When the Opaque Behavior or Action is later executed using Cameo Simulation Toolkit, it is the linked Activity that actually provides the executable behavior.

[IMAGE alt='' src='']

###### Opaque Behavior compilation

[IMAGE alt='' src='']

###### Opaque Action compilation

##### Opaque Expression compilation

When the Alf compiler processes the Alf body of an Opaque Expression, it creates a corresponding Activity in which to store the results of the compilation. This Activity is generally saved in the nearest Classifier containing the Opaque Expression. If the Opaque Expression specifies the guard on a Transition, then the generated Activity will be saved as a child of the State Machine containing the Transition. And, if the Opaque Expression specifies the guard on an Activity Edge, then the generated Activity will be saved as a child of the Activity containing the Activity Edge.

In all cases, the Activity is referenced in the **Behavior** property of the original Opaque Expression. When the Opaque Expression is later evaluated using Cameo Simulation Toolkit, it is the **Behavior** Activity that is actually executed in order to provide the value of the Expression.

[IMAGE alt='' src='']

###### Opaque Expression compilation (example shown is for an Activity Edge guard)

##### template-bindings-packageThe $$Template Bindings package

The *$$Template Bindings* package is a special package used by the Alf compiler to save instantiations of template Classifiers that result of explicit template bindings in Alf code (e.g., *Set<Integer>*). These instantiations are stored in a common place, so that similar bindings in Alf code across your model can be compiled to references to the same instantiation. For example, a binding of a standard Alf collection class, such as *Set<Integer>,* results in the generation of an instantiated class in the *$$Template Bindings* package with a long encoded name similar to *$$Model$$Alf$$Library$$CollectionClasses$$Set__$$Model$$'UML Standard Profile'$$'UML2 Metamodel'PrimitiveTypes$$Integer__.* If you use *Set<Integer>* in more than once in Alf code in your model, it will still result in only the one instantiated class, and the Activity models compiled from your Alf code will all refer to this class.

The *$$Template Bindings* package should only appear if you use template bindings in your Alf code. It is automatically created the first time such a binding is compiled in your model.

You should never manually alter any of the contents of the *$$Template Bindings* package.

When you delete the code for a template binding with an Alf body, the instantiated class generated from that Alf code is *not* automatically deleted from the *$$Template Bindings* package, since that class might also be referenced elsewhere in your model. Thus, if you use templates in your Alf code, it is possible, over time, for the *$$Template Bindings* package to accumulate contents that are no longer useful. If necessary, this can be cleaned up by doing a *[CONFLUENCE_PAGE title='Building and cleaning' space='ALFP2024x']* of your project.

[IMAGE alt='' src='']

###### The *$$Template Bindings* package, showing the instantiation of *Set<Integer>*

#### PANEL: Table of Contents

Table of Contents

3

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p>The <em>Alf compiler</em> is the part of the Alf plugin that carries out the compilation process. The Alf compiler is automatically invoked when you save Alf code into your model (unless you turn off automatic building; see <ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="Environment options" /></ac:link>). The activity model resulting from an Alf compilation is also stored in your model. Exactly where it is stored depends on which kind of element the Alf code is the body.</p><h3>Activity compilation</h3><p>When the Alf compiler processes the Alf body of an Activity, the resulting Activity model is saved as the Activity Nodes and Edges owned within that Activity. The Alf text itself is stored in a Comment element owned by the Activity, which has the <em>TextualRepresentation</em> stereotype applied. (See also <ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="Using Alf to define Activities" /></ac:link> and <ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="Using Alf for Operation methods" /></ac:link>.)</p><p><ac:image ac:align="center"><ri:attachment ri:filename="The_Alf_Compiler-Activity_Compilation.png"><ri:page ri:space-key="ALFP2024x" ri:content-title="The Alf compiler" /></ri:attachment></ac:image></p><h6 style="text-align: center;">Activity compilation</h6><p class="auto-cursor-target">The compilation of an activity may also result in certain auxiliary elements, such as Instance Specifications, that cannot be not stored within the Activity. These are generally inserted into the nearest Package containing the Activity (which may be the top-level Model). Also, in certain cases, template instantiations are saved in a <ac:link ac:anchor="template-bindings-package"><ac:link-body>special package called <em>$$Template Bindings</em></ac:link-body><ri:page ri:space-key="ALFP2024x" ri:content-title="The Alf compiler" /></ac:link> (described below).</p><h3>Opaque Behavior and Opaque Action compilation</h3><p>When the Alf compiler processes the Alf body of an Opaque Behavior or Opaque Action, it creates a corresponding Activity in which to store the result of the compilation. For an Opaque Behavior, the generated Activity is saved as a child of the Opaque Behavior. For an Opaque Action, the generated Activity is saved as a child of the Activity containing the Opaque Action. In either case, the Activity is also linked to the original Opaque Behavior or Action by applying the <em>CompiledRepresentation</em> stereotype. When the Opaque Behavior or Action is later executed using Cameo Simulation Toolkit, it is the linked Activity that actually provides the executable behavior.</p><p><ac:image ac:align="center"><ri:attachment ri:filename="The_Alf_Compiler-Opaque_Behavior_Compilation.png"><ri:page ri:space-key="ALFP2024x" ri:content-title="The Alf compiler" /></ri:attachment></ac:image></p><h6 style="text-align: center;">Opaque Behavior compilation</h6><p><br /></p><p><ac:image><ri:attachment ri:filename="The_Alf_Compiler-Opaque_Action_Compilation.png"><ri:page ri:space-key="ALFP2024x" ri:content-title="The Alf compiler" /></ri:attachment></ac:image></p><h6 style="text-align: center;">Opaque Action compilation</h6><h3>Opaque Expression compilation</h3><p>When the Alf compiler processes the Alf body of an Opaque Expression, it creates a corresponding Activity in which to store the results of the compilation. This Activity is generally saved in the nearest Classifier containing the Opaque Expression. If the Opaque Expression specifies the guard on a Transition, then the generated Activity will be saved as a child of the State Machine containing the Transition. And, if the Opaque Expression specifies the guard on an Activity Edge, then the generated Activity will be saved as a child of the Activity containing the Activity Edge.</p><p>In all cases, the Activity is referenced in the <strong>Behavior</strong> property of the original Opaque Expression. When the Opaque Expression is later evaluated using Cameo Simulation Toolkit, it is the <strong>Behavior</strong> Activity that is actually executed in order to provide the value of the Expression.</p><p><ac:image><ri:attachment ri:filename="The_Alf_Compiler-Opaque_Expression_Compilation.png"><ri:page ri:space-key="ALFP2024x" ri:content-title="The Alf compiler" /></ri:attachment></ac:image></p><h6 style="text-align: center;">Opaque Expression compilation (example shown is for an Activity Edge guard)</h6><h3><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="1659d13e-8b77-4436-b79c-f061bc94af8d"><ac:parameter ac:name="">template-bindings-package</ac:parameter></ac:structured-macro>The $$Template Bindings package</h3><p>The <em>$$Template Bindings</em> package is a special package used by the Alf compiler to save instantiations of template Classifiers that result of explicit template bindings in Alf code (e.g., <em>Set&lt;Integer&gt;</em>). These instantiations are stored in a common place, so that similar bindings in Alf code across your model can be compiled to references to the same instantiation. For example, a binding of a standard Alf collection class, such as <em>Set&lt;Integer&gt;,</em> results in the generation of an instantiated class in the <em>$$Template Bindings</em> package with a long encoded name similar to <em>$$Model$$Alf$$Library$$CollectionClasses$$Set__$$Model$$'UML Standard Profile'$$'UML2 Metamodel'PrimitiveTypes$$Integer__.</em> If you use <em>Set&lt;Integer&gt;</em> in more than once in Alf code in your model, it will still result in only the one instantiated class, and the Activity models compiled from your Alf code will all refer to this class.</p><p>The <em>$$Template Bindings</em> package should only appear if you use template bindings in your Alf code. It is automatically created the first time such a binding is compiled in your model.</p><ac:structured-macro ac:name="warning" ac:schema-version="1" ac:macro-id="98256e16-821f-4c79-b06d-61f4b59fd336"><ac:rich-text-body><p>You should never manually alter any of the contents of the <em>$$Template Bindings</em> package.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="7a90b997-4f25-42f3-821b-85c7de472bf9"><ac:rich-text-body><p>When you delete the code for a template binding with an Alf body, the instantiated class generated from that Alf code is <em>not</em> automatically deleted from the <em>$$Template Bindings</em> package, since that class might also be referenced elsewhere in your model. Thus, if you use templates in your Alf code, it is possible, over time, for the <em>$$Template Bindings</em> package to accumulate contents that are no longer useful. If necessary, this can be cleaned up by doing a <em><ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="Building and cleaning" /><ac:plain-text-link-body><![CDATA[clean build]]></ac:plain-text-link-body></ac:link></em> of your project.</p></ac:rich-text-body></ac:structured-macro><p><ac:image ac:align="center"><ri:attachment ri:filename="The_Alf_Compiler-Auxiliary_Elements.png"><ri:page ri:space-key="ALFP2024x" ri:content-title="The Alf compiler" /></ri:attachment></ac:image></p><h6 style="text-align: center;">The <em>$$Template Bindings</em> package, showing the instantiation of <em>Set&lt;Integer&gt;</em></h6></ac:layout-cell><ac:layout-cell><p><br /></p><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="48e9d2df-5f80-4be1-abe5-45cc8f0faf9c"><ac:parameter ac:name="title">Table of Contents</ac:parameter><ac:rich-text-body><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="bed0b8b9-7764-47bb-823b-ee0927eb0b3f"><ac:parameter ac:name="maxLevel">3</ac:parameter></ac:structured-macro></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=137986087 space=ALFP2024x version=1 -->
## PAGE 00055: The Alf editor

- page_id: `137986087`
- space_key: `ALFP2024x`
- source_url: https://docs.nomagic.com/spaces/ALFP2024x/pages/137986087/The+Alf+editor
- version_number: 1
- version_date: `2023-09-22T11:48:46.802+02:00`
- ancestors: Alf Plugin Documentation > User Guide > Working with Alf
- labels: []

### NORMALIZED CONTENT

##### The Alf editor window

The Alf editor window provides a general way to edit the Alf code of any element with an Alf body. If your project was created using the [Alf project template](https://docs.nomagic.com/display/ALFP2024x/Alf+project+template), then the Alf editor window will already be open and docked in the lower left window pane. But, if it is not open, you can open it by selecting **Windows > Alf** (the window will initially appear at the bottom of the main MagicDraw window, but it may be moved and docked like other MagicDraw windows). The Alf editor window remains open and in the same position for a given project, even when the project is closed and opened again. For opaque behaviors, expression and actions, associated Alf code may also be edited as the body of those elements (for more details on editing the Alf bodies of these kinds of model elements, see the child pages of this page).

To edit Alf code in the Alf editor window, open the window (if it is not already open) and select the element whose Alf body is to be edited. If the element has an Alf body (or if it is possible to add a new Alf body to it), then the Alf code appears in the window. As shown in the sample image below, the code is displayed with keywords and syntactic elements highlighted in different colors.

[IMAGE alt='' src='']

###### The Alf Editor window.

The buttons at the bottom right of the window have the following functions.

| Button name | Description |
| --- | --- |
| Create | Create a behavior for the selected element, which can have an Alf body. This button will only be active if the selected element cannot itself have an Alf body, but an associated Behavior can be created for it (such as an entry Behavior for a State, or a method Behavior for an Operation). If more there is more than one possibility (such as entry, exit and do-activity Behaviors for a State), then you will be able to select one from a pop-up menu. |
| Save | Save changes that have been made to the Alf body being edited. If, after making changes to the Alf code, you select a different element, then your changes will be automatically saved, even if you have not pressed the Save button. |
| Revert | Revert the contents of the window to the last saved version of the Alf body. An changes made since the last save will be lost. |

##### Alf compilation errors

When you save Alf code from the editor, if the code has no errors, then it is automatically compiled so that it becomes executable. If the code has errors, however, then it can still be saved as text, but it cannot be compiled.

An Alf body that is saved with compilation errors may have been previously compiled successfully. In this case, the executable behavior of the element with which it is associated will still reflect that generated from the last successful compilation.

The Alf editor will detect errors in Alf code as it is being edited. Detected errors are identified by underlining the relevant text in red and showing a red marker to the left of any line containing an identified error. Alf code may have two kinds of errors: *syntax* *errors*, which result from a failure to parse the text being edited as Alf code, and *constraint violations**,* which are violations of the semantic checks made on Alf code that has been parsed successfully.

The image below shows an example of code with errors. As shown, more than one syntax error may be highlighted in the code. Hovering the cursor over the marked text (or the marker to the left of the line) shows the cause of the error. The example below shows the description of a syntax error.

[IMAGE alt='' src='']

###### A syntax error.

For text that parses successfully, the Alf editor runs a series of *constraint checks* (so called because these checks are formally specified in the Alf standard as constraints on the abstract syntax tree of parsed Alf code). The example below shows the description of a constraint violation. Note that, even if there are syntax errors in some of the code, the Alf editor will attempt to run constraint checks on other parts of the code. However, once you correct the syntax errors, the editor may identify additional constraint violations due to checks that could not be run previously.

[IMAGE alt='' src='']

###### Constraint violation.

If you save Alf code with errors, then these errors will also be recorded in the Active Validation Results window (as shown below).

Depending on your Active Validation environment options, it may take a couple of seconds after you save your Alf code before the error notifications appear in the Active Validation Results (or before they disappear, once they are corrected)

By default, the Active Validation Option **Validate Only Visible Diagrams** is set to *true* for a project. This means that only Alf errors on currently visible diagrams will appear in the Active Validation Results. If you would like all Alf errors included in the results, then select **Analyze > Validation > Active Validation Options** and set the **Validate Only Visible Diagrams** option to *false.* This is particularly useful to provide a summary when there are compilation errors in various Alf bodies across your project. Note, however, that setting this option to *false* means that *all* active validations will be carried out across your project, not just the collection of Alf errors. This could result in a degradation of performance, if your project is large or you have a large number of validations being performed.

[IMAGE alt='' src='']

###### Alf compilation errors in Active Validation Results.

##### Removing error annotations

Sometimes, an element will remain marked with an Alf compilation error annotation, even though, when you look at the Alf code associated with it in the Alf Editor, there are no errors. For example, if you enter Alf code that references a property that does not exist, this will be marked as an error. If you later create a property consistent with the reference in the Alf code, the original error annotation remains, because no dependency of the Alf code on the property could be recorded before the property existed. However, if you then look at the Alf code in the Alf Editor, it will not have any errors. To remove the error annotations, simply press the **Save** button in the Alf Editor (even if you have made no changes to the text). Doing a [CONFLUENCE_PAGE title='Building and cleaning' space='ALFP2024x'] will also clear the annotations.

[IMAGE alt='' src='']

###### Saving from the Alf Editor to remove an error annotation.

##### Read-only Alf bodies

Sometimes an Alf body will be attached to an element that is editable, such as when it is in a read-only used project or a part of a Teamwork Cloud project that is not locked for edit. In this case, the Alf Editor will still show the Alf code for the element, but on a gray background to indicate that the code is not editable. If the element becomes editable (for instance, by locking it for edit in Teamwork Cloud), then the Alf Editor will allow the code to be edited.

[IMAGE alt='' src='']

###### Viewing the Alf body of a read-only element.

#### PANEL: Table of Contents

Table of Contents

3

#### PANEL: Related pages

Related pages

- [CONFLUENCE_PAGE title='Working with Alf' space='ALFP2024x']
  - [CONFLUENCE_PAGE title='Using Alf to define Behaviors' space='ALFP2024x']
  - [CONFLUENCE_PAGE title='Using Alf in Class models' space='ALFP2024x']
  - [CONFLUENCE_PAGE title='Using Alf in State Machine models' space='ALFP2024x']
  - [CONFLUENCE_PAGE title='Using Alf in Activity models' space='ALFP2024x']
- [CONFLUENCE_PAGE title='The Alf compiler' space='ALFP2024x']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><h3>The Alf editor window</h3><p>The Alf editor window provides a general way to edit the Alf code of any element with an Alf body. If your project was created using the <a href="https://docs.nomagic.com/display/ALFP2024x/Alf+project+template">Alf project template</a>, then the Alf editor window will already be open and docked in the lower left window pane. But, if it is not open, you can open it by selecting <strong>Windows &gt; Alf</strong> (the window will initially appear at the bottom of the main MagicDraw window, but it may be moved and docked like other MagicDraw windows). The Alf editor window remains open and in the same position for a given project, even when the project is closed and opened again. For opaque behaviors, expression and actions, associated Alf code may also be edited as the body of those elements (for more details on editing the Alf bodies of these kinds of model elements, see the child pages of this page).</p><p>To edit Alf code in the Alf editor window, open the window (if it is not already open) and select the element whose Alf body is to be edited. If the element has an Alf body (or if it is possible to add a new Alf body to it), then the Alf code appears in the window. As shown in the sample image below, the code is displayed with keywords and syntactic elements highlighted in different colors.</p><p><br /></p><p class="auto-cursor-target" style="text-align: center;"><ac:image ac:height="400"><ri:attachment ri:filename="The_Alf_Editor-Window.png"><ri:page ri:space-key="ALFP2024x" ri:content-title="The Alf editor" /></ri:attachment></ac:image></p><h6 style="text-align: center;">The Alf Editor window.</h6><p>The buttons at the bottom right of the window have the following functions.</p><table class="wrapped"><colgroup><col /><col /></colgroup><tbody><tr><th>Button name</th><th>Description</th></tr><tr><td colspan="1">Create</td><td colspan="1">Create a behavior for the selected element, which can have an Alf body. This button will only be active if the selected element cannot itself have an Alf body, but an associated Behavior can be created for it (such as an entry Behavior for a State, or a method Behavior for an Operation). If more there is more than one possibility (such as entry, exit and do-activity Behaviors for a State), then you will be able to select one from a pop-up menu.</td></tr><tr><td>Save</td><td>Save changes that have been made to the Alf body being edited. If, after making changes to the Alf code, you select a different element, then your changes will be automatically saved, even if you have not pressed the <strong>Save</strong> button.</td></tr><tr><td>Revert</td><td>Revert the contents of the window to the last saved version of the Alf body. An changes made since the last save will be lost.</td></tr></tbody></table><h3>Alf compilation errors</h3><p>When you save Alf code from the editor, if the code has no errors, then it is automatically compiled so that it becomes executable. If the code has errors, however, then it can still be saved as text, but it cannot be compiled.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="77a61317-1b99-49f8-b5bc-affef4fc3156"><ac:rich-text-body><p>An Alf body that is saved with compilation errors may have been previously compiled successfully. In this case, the executable behavior of the element with which it is associated will still reflect that generated from the last successful compilation.</p></ac:rich-text-body></ac:structured-macro><p>The Alf editor will detect errors in Alf code as it is being edited. Detected errors are identified by underlining the relevant text in red and showing a red marker to the left of any line containing an identified error. Alf code may have two kinds of errors: <em>syntax</em> <em>errors</em>, which result from a failure to parse the text being edited as Alf code, and <em>constraint violations</em><em>,</em> which are violations of the semantic checks made on Alf code that has been parsed successfully.</p><p>The image below shows an example of code with errors. As shown, more than one syntax error may be highlighted in the code. Hovering the cursor over the marked text (or the marker to the left of the line) shows the cause of the error. The example below shows the description of a syntax error.</p><p><br /></p><p><ac:image ac:align="center" ac:height="400"><ri:attachment ri:filename="The_Alf_Editor-Syntax_Error.png"><ri:page ri:space-key="ALFP2024x" ri:content-title="The Alf editor" /></ri:attachment></ac:image></p><h6 style="text-align: center;">A syntax error.</h6><p>For text that parses successfully, the Alf editor runs a series of <em>constraint checks</em> (so called because these checks are formally specified in the Alf standard as constraints on the abstract syntax tree of parsed Alf code). The example below shows the description of a constraint violation. Note that, even if there are syntax errors in some of the code, the Alf editor will attempt to run constraint checks on other parts of the code. However, once you correct the syntax errors, the editor may identify additional constraint violations due to checks that could not be run previously.</p><p><br /></p><p style="text-align: center;"><ac:image ac:height="400"><ri:attachment ri:filename="The_Alf_Editor-Constraint_Violation.png"><ri:page ri:space-key="ALFP2024x" ri:content-title="The Alf editor" /></ri:attachment></ac:image></p><h6 style="text-align: center;">Constraint violation.</h6><p>If you save Alf code with errors, then these errors will also be recorded in the Active Validation Results window (as shown below).</p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="e0b2210d-c143-44c0-8a8c-d1d74527b659"><ac:rich-text-body><p>Depending on your Active Validation environment options, it may take a couple of seconds after you save your Alf code before the error notifications appear in the Active Validation Results (or before they disappear, once they are corrected)</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="6680b2fc-9aab-4c21-95ec-9b4c9fa68e37"><ac:rich-text-body><p>By default, the Active Validation Option <strong>Validate Only Visible Diagrams</strong> is set to <em>true</em> for a project. This means that only Alf errors on currently visible diagrams will appear in the Active Validation Results. If you would like all Alf errors included in the results, then select <strong>Analyze &gt; Validation &gt; Active Validation Options</strong> and set the <strong>Validate Only Visible Diagrams</strong> option to <em>false.</em> This is particularly useful to provide a summary when there are compilation errors in various Alf bodies across your project. Note, however, that setting this option to <em>false</em> means that <em>all</em> active validations will be carried out across your project, not just the collection of Alf errors. This could result in a degradation of performance, if your project is large or you have a large number of validations being performed.</p></ac:rich-text-body></ac:structured-macro><p><ac:image ac:align="center"><ri:attachment ri:filename="The_Alf_Editor-Active_Validation_Results .png"><ri:page ri:space-key="ALFP2024x" ri:content-title="The Alf editor" /></ri:attachment></ac:image></p><h6 class="auto-cursor-target" style="text-align: center;">Alf compilation errors in Active Validation Results.</h6><h3>Removing error annotations</h3><p>Sometimes, an element will remain marked with an Alf compilation error annotation, even though, when you look at the Alf code associated with it in the Alf Editor, there are no errors. For example, if you enter Alf code that references a property that does not exist, this will be marked as an error. If you later create a property consistent with the reference in the Alf code, the original error annotation remains, because no dependency of the Alf code on the property could be recorded before the property existed. However, if you then look at the Alf code in the Alf Editor, it will not have any errors. To remove the error annotations, simply press the <strong>Save</strong> button in the Alf Editor (even if you have made no changes to the text). Doing a <ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="Building and cleaning" /><ac:plain-text-link-body><![CDATA[project build]]></ac:plain-text-link-body></ac:link> will also clear the annotations.</p><p><ac:image ac:align="center" ac:width="400"><ri:attachment ri:filename="Saving_To_Resolve_Errors.png"><ri:page ri:space-key="ALFP2024x" ri:content-title="The Alf editor" /></ri:attachment></ac:image></p><h6 style="text-align: center;">Saving from the Alf Editor to remove an error annotation.</h6><h3>Read-only Alf bodies</h3><p>Sometimes an Alf body will be attached to an element that is editable, such as when it is in a read-only used project or a part of a Teamwork Cloud project that is not locked for edit. In this case, the Alf Editor will still show the Alf code for the element, but on a gray background to indicate that the code is not editable. If the element becomes editable (for instance, by locking it for edit in Teamwork Cloud), then the Alf Editor will allow the code to be edited.</p><p><br /></p><p style="text-align: center;"><ac:image ac:height="250"><ri:attachment ri:filename="Viewing_A_Read_Only_Alf_Body.png"><ri:page ri:space-key="ALFP2024x" ri:content-title="The Alf editor" /></ri:attachment></ac:image></p><p style="text-align: center;"><br /></p><h6 style="text-align: center;">Viewing the Alf body of a read-only element.</h6></ac:layout-cell><ac:layout-cell><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="fd4e8ab6-68fa-4ab4-b4ea-20808d945995"><ac:parameter ac:name="title">Table of Contents</ac:parameter><ac:rich-text-body><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="38ca36a0-ccf2-414f-8b28-2587bc776ac8"><ac:parameter ac:name="maxLevel">3</ac:parameter></ac:structured-macro></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="281b1859-6448-4a1e-9f31-059a9aa33d9a"><ac:parameter ac:name="title">Related pages</ac:parameter><ac:rich-text-body><ul><li><ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="Working with Alf" /></ac:link><ul><li><ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="Using Alf to define Behaviors" /></ac:link></li><li><ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="Using Alf in Class models" /></ac:link></li><li><ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="Using Alf in State Machine models" /></ac:link></li><li><ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="Using Alf in Activity models" /></ac:link></li></ul></li><li><ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="The Alf compiler" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=137986197 space=ALFP2024x version=1 -->
## PAGE 00056: Tutorials

- page_id: `137986197`
- space_key: `ALFP2024x`
- source_url: https://docs.nomagic.com/spaces/ALFP2024x/pages/137986197/Tutorials
- version_number: 1
- version_date: `2023-09-22T11:48:54.762+02:00`
- ancestors: Alf Plugin Documentation
- labels: []

### NORMALIZED CONTENT

The following tutorials are listed in order of increasing complexity. Note that these are tutorials about the Alf *plugin*, not the *language,* and presume basic knowledge of the Alf language itself.

h4

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>The following tutorials are listed in order of increasing complexity. Note that these are tutorials about the Alf <em>plugin</em>, not the <em>language,</em> and presume basic knowledge of the Alf language itself.</p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="35b30a1e-e2fd-4b23-b1b1-25a910453655"><ac:parameter ac:name="style">h4</ac:parameter></ac:structured-macro></p>
````

<!--NOMAGIC_PAGE id=137986072 space=ALFP2024x version=1 -->
## PAGE 00057: User Guide

- page_id: `137986072`
- space_key: `ALFP2024x`
- source_url: https://docs.nomagic.com/spaces/ALFP2024x/pages/137986072/User+Guide
- version_number: 1
- version_date: `2023-09-22T11:48:45.233+02:00`
- ancestors: Alf Plugin Documentation
- labels: []

### NORMALIZED CONTENT

h4

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="f90bc20b-d070-4205-a906-d9b7a37c06e4"><ac:parameter ac:name="style">h4</ac:parameter></ac:structured-macro></p>
````

<!--NOMAGIC_PAGE id=137986146 space=ALFP2024x version=1 -->
## PAGE 00058: Using Alf expressions in Opaque Actions

- page_id: `137986146`
- space_key: `ALFP2024x`
- source_url: https://docs.nomagic.com/spaces/ALFP2024x/pages/137986146/Using+Alf+expressions+in+Opaque+Actions
- version_number: 1
- version_date: `2023-09-22T11:48:50.558+02:00`
- ancestors: Alf Plugin Documentation > User Guide > Working with Alf > Using Alf in Activity models > Using Alf in Opaque Action bodies
- labels: []

### NORMALIZED CONTENT

The Alf specification states that a sequence of Alf statements (each ending in a semicolon) may be used in the body of an Opaque Action. However, it is not uncommon that such an Action will simply compute a single value, to be used in later computations or as the basis for a decision. In such a case, the Alf plugin allows you to use a shortcut, in which you can use an Alf expression in the body rather than a statement. The Opaque Action must have a single Output Pin, and the type of the expression must be compatible with the type of the Output Pin. When the Opaque Action is executed, the Alf expression is evaluated and the result is placed on the Output Pin of the action.

In order to be recognized as an expression, not a statement, the Alf code entered into the Opaque Action must *not* have a semicolon at the end. If you put a semicolon at the end, then this is still valid Alf code, but it becomes an expression *statement**,* and result of the expression will then *not* be automatically put on Output Pin of the Opaque Action (instead you would have to assign the value explicitly to the name of the Output Pin).

The expression shortcut for Opaque Actions is particularly useful in the context of Activities that carry out some functional computation. For example, the following Activity computes the factorial function, which is mathematically defined as *Factorial(0) = 1* and *Factorial(n) = n * Factorial(n-1)* for *n > 0.*

*[IMAGE alt='' src='']*

The above model is equivalent to the more verbose use of Alf shown in the diagram below, which does does not use the expression shortcut.

The Alf standard does not currently require support for the use of Alf expressions in Opaque Actions, so, if you create a model using the expression shortcut in MagicDraw, it may not be supported if you import your model into a tool with a different Alf implementation.

#### PANEL: Related pages

Related pages

- [CONFLUENCE_PAGE title='Using Alf in Opaque Action bodies' space='ALFP2024x']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p>The Alf specification states that a sequence of Alf statements (each ending in a semicolon) may be used in the body of an Opaque Action. However, it is not uncommon that such an Action will simply compute a single value, to be used in later computations or as the basis for a decision. In such a case, the Alf plugin allows you to use a shortcut, in which you can use an Alf expression in the body rather than a statement. The Opaque Action must have a single Output Pin, and the type of the expression must be compatible with the type of the Output Pin. When the Opaque Action is executed, the Alf expression is evaluated and the result is placed on the Output Pin of the action.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="9e6ec38c-19bd-47f7-ac87-95050cdb34d3"><ac:rich-text-body><p>In order to be recognized as an expression, not a statement, the Alf code entered into the Opaque Action must <em>not</em> have a semicolon at the end. If you put a semicolon at the end, then this is still valid Alf code, but it becomes an expression <em>statement</em><em>,</em> and result of the expression will then <em>not</em> be automatically put on Output Pin of the Opaque Action (instead you would have to assign the value explicitly to the name of the Output Pin).</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="d649442d-089f-45cb-81e5-dc6898860175"><ac:rich-text-body><p>The expression shortcut for Opaque Actions is particularly useful in the context of Activities that carry out some functional computation. For example, the following Activity computes the factorial function, which is mathematically defined as <em>Factorial(0) = 1</em> and <em>Factorial(n) = n * Factorial(n-1)</em> for <em>n &gt; 0.</em></p><p><em><ac:image ac:align="center" ac:height="400"><ri:attachment ri:filename="Using_Alf_Expressions_In_Opaque_Actions-Example1.png"><ri:page ri:space-key="ALFP2024x" ri:content-title="Using Alf expressions in Opaque Actions" /></ri:attachment></ac:image><br /></em></p><p class="auto-cursor-target">The above model is equivalent to the more verbose use of Alf shown in the diagram below, which does does not use the expression shortcut.</p><ac:image ac:align="center" ac:height="400"><ri:attachment ri:filename="Using_Alf_Expressions_In_Opaque_Actions-Example2.png"><ri:page ri:space-key="ALFP2024x" ri:content-title="Using Alf expressions in Opaque Actions" /></ri:attachment></ac:image></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="ba5a3b20-2216-4051-9f08-c37ab0daaa50"><ac:rich-text-body><p>The Alf standard does not currently require support for the use of Alf expressions in Opaque Actions, so, if you create a model using the expression shortcut in MagicDraw, it may not be supported if you import your model into a tool with a different Alf implementation.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell><ac:layout-cell><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="71851550-e38a-401b-8737-49b98cd02b38"><ac:parameter ac:name="title">Related pages</ac:parameter><ac:rich-text-body><ul><li><ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="Using Alf in Opaque Action bodies" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=137986149 space=ALFP2024x version=1 -->
## PAGE 00059: Using Alf for Activity Edge guards

- page_id: `137986149`
- space_key: `ALFP2024x`
- source_url: https://docs.nomagic.com/spaces/ALFP2024x/pages/137986149/Using+Alf+for+Activity+Edge+guards
- version_number: 1
- version_date: `2023-09-22T11:48:50.796+02:00`
- ancestors: Alf Plugin Documentation > User Guide > Working with Alf > Using Alf in Activity models
- labels: []

### NORMALIZED CONTENT

You can use the [CONFLUENCE_PAGE title='The Alf editor' space='ALFP2024x'] to create an Alf Expression for the guard for an Activity Edge (Object Flow or Control Flow) in an Activity or to edit an existing guard Expression.

To create an Alf guard Expression

1. Select the Activity Edge and open the Alf editor window (select Windows > Alf ), if it isn't already open.
2. In the Alf editor window, press Create .
3. Enter the Alf code for the Expression and press **Save** to compile and save it. Note that the text entered must be for an *expression,* not a statement. Therefore, it must *not* have a semicolon at the end. The Expression can access attribute values of the context Classifier of the Activity containing its Activity Edge (using Alf *this* expressions) or the decision input value for the Decision Node (see [CONFLUENCE_PAGE title='Accessing data in Activity Edge guards' space='ALFP2024x']). [IMAGE alt='' src='']

To edit an Alf guard Expression

1. Select the Activity Edge and open the Alf editor window (select Windows > Alf ), if it isn't already open.
2. Edit the guard Expression and click Save to save and compile it. [ATTACHMENT filename='Using_Alf_For_Activity_Edge_Guards-Editing.png']

The Alf code for a guard Expression can also be entered or edited directly in the **Guard** property in the Specification window of the Activity Edge. If you open the Edit Guard window, then the Alf code can be edited just as in the Alf editor window. However, instead of **Save** and **Revert** buttons, this window has **OK** and **Cancel** buttons, either of which will close it. If you press **OK**, then the Alf text is saved, and, if it has no errors, compiled. If you press **Cancel**, the Alf text is *not* saved.

[IMAGE alt='' src='']

###### Editing code for an Activity Edge guard Expression in the Edit Guard window

To be recognized as Alf code, the **Body** of an Opaque Expression must have the **Language** Alf. If your project was created using the Alf project template, then Alf will be the default language. Otherwise, select Alf from the **Language** menu (you may have to scroll upwards in the menu to find the selection for *Alf*).

To make Alf the default language for Opaque Expressions

1. Select Options > Environment .
2. From the General options, select Editing .
3. For the Opaque Expression Default Language option, type Alf (with exactly that spelling and capitalization). Click OK

#### PANEL: Related pages

Related pages

- [CONFLUENCE_PAGE title='Accessing data in Activity Edge guards' space='ALFP2024x']
- [CONFLUENCE_PAGE title='The Alf editor' space='ALFP2024x']
- [CONFLUENCE_PAGE title='The Alf compiler' space='ALFP2024x']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p><br /></p><p>You can use the <ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="The Alf editor" /><ac:plain-text-link-body><![CDATA[Alf editor]]></ac:plain-text-link-body></ac:link> to create an Alf Expression for the guard for an Activity Edge (Object Flow or Control Flow) in an Activity or to edit an existing guard Expression.</p><p><br /></p><p>To create an Alf guard Expression</p><hr /><ol><li>Select the Activity Edge and open the Alf editor window (select <strong>Windows &gt; Alf</strong>), if it isn't already open.</li><li>In the Alf editor window, press <strong>Create</strong>.</li><li><p class="auto-cursor-target">Enter the Alf code for the Expression and press <strong>Save</strong> to compile and save it.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="5aa5f4bb-7ff5-4fd5-a07c-70738a97f080"><ac:rich-text-body><p>Note that the text entered must be for an <em>expression,</em> not a statement. Therefore, it must <em>not</em> have a semicolon at the end.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="5d82e97d-fd95-41d8-95c4-8c76eae8c85c"><ac:rich-text-body><p>The Expression can access attribute values of the context Classifier of the Activity containing its Activity Edge (using Alf <em>this</em> expressions) or the <span class="confluence-link">decision input value for the Decision Node</span> (see <ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="Accessing data in Activity Edge guards" /></ac:link>).</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /><ac:image><ri:attachment ri:filename="Using_Alf_For_Activity_Edge_Guards-Creating.png"><ri:page ri:space-key="ALFP2024x" ri:content-title="Using Alf for Activity Edge guards" /></ri:attachment></ac:image></p></li></ol><p><br /></p><p>To edit an Alf guard Expression</p><hr /><ol><li>Select the Activity Edge and open the Alf editor window (select <strong>Windows &gt; Alf</strong>), if it isn't already open.</li><li>Edit the guard Expression and click <strong>Save</strong> to save and compile it.<br /><br /><ac:image><ri:attachment ri:filename="Using_Alf_For_Activity_Edge_Guards-Editing.png"><ri:page ri:space-key="ALFP2024x" ri:content-title="Using Alf for Activity Edge guards" /></ri:attachment></ac:image></li></ol><p><br /></p><p>The Alf code for a guard Expression can also be entered or edited directly in the <strong>Guard</strong> property in the Specification window of the Activity Edge. If you open the Edit Guard window, then the Alf code can be edited just as in the Alf editor window. However, instead of <strong>Save</strong> and <strong>Revert</strong> buttons, this window has <strong>OK</strong> and <strong>Cancel</strong> buttons, either of which will close it. If you press <strong>OK</strong>, then the Alf text is saved, and, if it has no errors, compiled. If you press <strong>Cancel</strong>, the Alf text is <em>not</em> saved.</p><p><ac:image ac:align="center"><ri:attachment ri:filename="Using_Alf_For_Activity_Edge_Guards-Editing_Body.png"><ri:page ri:space-key="ALFP2024x" ri:content-title="Using Alf for Activity Edge guards" /></ri:attachment></ac:image></p><h6 style="text-align: center;">Editing code for an Activity Edge guard Expression in the Edit Guard window</h6><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="35b1121a-e94c-4d76-ac25-f8839b2b2bf3"><ac:rich-text-body><p>To be recognized as Alf code, the <strong>Body</strong> of an Opaque Expression must have the <strong>Language</strong> Alf. If your project was created using the Alf project template, then Alf will be the default language. Otherwise, select Alf from the <strong>Language</strong> menu (you may have to scroll upwards in the menu to find the selection for <em>Alf</em>).</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="6c1dc32f-7897-4fa6-8937-039bc4a4a55a"><ac:rich-text-body><p>To make Alf the default language for Opaque Expressions</p><hr /><ol><li>Select <strong>Options &gt; Environment</strong>.</li><li>From the <strong>General</strong> options, select <strong>Editing</strong>.</li><li>For the <strong>Opaque Expression Default Language</strong> option, type <em>Alf</em> (with exactly that spelling and capitalization). Click <strong>OK</strong></li></ol></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell><ac:layout-cell><p><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="fcd59470-9da1-40d5-bf65-8ac8f428d4ba"><ac:parameter ac:name="title">Related pages</ac:parameter><ac:rich-text-body><ul><li><ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="Accessing data in Activity Edge guards" /></ac:link><br /><br /></li><li><ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="The Alf editor" /></ac:link></li><li><ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="The Alf compiler" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=137986107 space=ALFP2024x version=1 -->
## PAGE 00060: Using Alf for classifier behaviors

- page_id: `137986107`
- space_key: `ALFP2024x`
- source_url: https://docs.nomagic.com/spaces/ALFP2024x/pages/137986107/Using+Alf+for+classifier+behaviors
- version_number: 1
- version_date: `2023-09-22T11:48:48.255+02:00`
- ancestors: Alf Plugin Documentation > User Guide > Working with Alf > Using Alf in Class models
- labels: []

### NORMALIZED CONTENT

An *active Class* is one that has a *classifier behavior* associated with it, which defines the asynchronous behavior of instances of the class. When such a classifier behavior is an Activity or an Opaque Behavior, you can specify it using Alf code.

If an active Class is instantiated using an Alf instance creation expression, then the classifier behavior for the Class is explicitly started on the newly created instance *after* the completion of initialization of the instance. However, the default Cameo Simulation Toolkit option is to **Autostart Active Objects**, in which case the classifier behavior for an active object will be automatically started as soon as the object is created. While CST will ensure that any Properties with default values are properly initialized before the classifier behavior is started, if you have initialization code in a constructor for an active Class, then this will *not* execute before the classifier behavior starts.

Therefore, if you intend to instantiate an active Class from Alf code using a constructor that carries out initialization on which the classifier behavior depends, make sure that the classifier behavior waits for the constructor execution to complete. You can do this by having the classifier behavior wait for a special *Start* Signal before carrying out any other behavior, and having the constructor invoke *this.Start()* when it is done with its initialization behavior. (If the classifier behavior is an activity, then use an Accept Event Action to wait for the Start signal. If the classifier behavior is a State Machine, have the State Machine transition from its initial Pseudostate to a *Waiting* State that is exited by a Transition triggered by the *Start* Signal.)

Alternatively, you can turn off the **Autostart Active Objects** option:

1. Select Options > Environment from the main menu.
2. Choose Simulation (the last option group on the left).
3. Uncheck the Autostart Active Objects option under Simulation Frameworks (so it is false ).

However, doing this will turn off the option globally for all projects, which may cause some other simulation projects to not work. You can turn this option off for just a specific project if you use a simulation configuration, by setting the [**Autostart Active Objects****property](https://docs.nomagic.com/display/CSTTWRT/Automatic+start+of+active+objects) to *false* in your configuration.

To create a classifier behavior using Alf

1. Open the Specification window for the Class and check the **Is Active** property. If the **Is Active** property does not appear in the Specification window, select **All** from the **Properties** drop-down at the top right of the window.
2. Close the Specification window.
3. Select the Class and open the Alf editor window (select **Windows > Alf**), if it isn't already open.
4. If the Class does not have a classifier behavior yet, then no code will appear in the Alf editor window, but the Create button will be active. Press Create to create a new classifier behavior for the Class.
5. Enter the Alf code for the classifier behavior and press **Save** to compile and save the code.

To edit an existing Alf body for a classifier behavior

- Select the Class in the Model Browser or on a Class diagram and open the Alf editor window (select **Windows > Alf**), if it isn't already open. The existing Alf code will appear in the window. The Alf code for an Operation is actually stored as the Alf body of the method Behavior of the Operation (which is an Activity or Opaque Behavior, as created above). It is therefore possible to directly the edit the code on the method Behavior (as described in [Using Alf to define Behaviors](https://docs.nomagic.com/display/ALFP2024x/Using+Alf+to+define+Behaviors)), but it is usually easier to act directly on the Operation. [ATTACHMENT filename='Using_Alf_To_Define_Classifier_Behaviors-Editing.png']

While a classifier behavior may be edited like any other Behavior with an Alf body, as an asynchronous Behavior it is allowed to have Alf *accept* statements, which can handle Signals sent to instances of its active Class and are not allowed in synchronously called Behaviors. However, Alf requires that, for any Signal appearing in an *accept* statement, the containing Class must have a Reception (as shown below).

[IMAGE alt='' src='']

###### Referencing a Reception in an Alf accept statement

#### PANEL: Related pages

Related pages

- The Alf editor
- The Alf compiler

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p>An <em>active Class</em> is one that has a <em>classifier behavior</em> associated with it, which defines the asynchronous behavior of instances of the class. When such a classifier behavior is an Activity or an Opaque Behavior, you can specify it using Alf code.</p><ac:structured-macro ac:name="warning" ac:schema-version="1" ac:macro-id="ceea5383-ed17-4e04-8ad7-6ecabe3358b9"><ac:rich-text-body><p>If an active Class is instantiated using an Alf instance creation expression, then the classifier behavior for the Class is explicitly started on the newly created instance <em>after</em> the completion of initialization of the instance. However, the default Cameo Simulation Toolkit option is to <strong>Autostart Active Objects</strong>, in which case the classifier behavior for an active object will be automatically started as soon as the object is created. While CST will ensure that any Properties with default values are properly initialized before the classifier behavior is started, if you have initialization code in a constructor for an active Class, then this will <em>not</em> execute before the classifier behavior starts.</p><p>Therefore, if you intend to instantiate an active Class from Alf code using a constructor that carries out initialization on which the classifier behavior depends, make sure that the classifier behavior waits for the constructor execution to complete. You can do this by having the classifier behavior wait for a special <em>Start</em> Signal before carrying out any other behavior, and having the constructor invoke <em>this.Start()</em> when it is done with its initialization behavior. (If the classifier behavior is an activity, then use an Accept Event Action to wait for the Start signal. If the classifier behavior is a State Machine, have the State Machine transition from its initial Pseudostate to a <em>Waiting</em> State that is exited by a Transition triggered by the <em>Start</em> Signal.)</p><p>Alternatively, you can turn off the <strong>Autostart Active Objects</strong> option:</p><ol><li>Select <strong>Options &gt; Environment</strong> from the main menu.</li><li>Choose <strong>Simulation</strong> (the last option group on the left).</li><li>Uncheck the <strong>Autostart Active Objects</strong> option under <strong>Simulation Frameworks</strong> (so it is <em>false</em>).</li></ol><p>However, doing this will turn off the option globally for all projects, which may cause some other simulation projects to not work. You can turn this option off for just a specific project if you use a simulation configuration, by setting the <a href="https://docs.nomagic.com/display/CSTTWRT/Automatic+start+of+active+objects"><strong>Autostart Active Objects</strong><em> </em>property</a> to <em>false</em> in your configuration.</p></ac:rich-text-body></ac:structured-macro><p><br /></p><p>To create a classifier behavior using Alf</p><hr /><ol><li><p class="auto-cursor-target">Open the Specification window for the Class and check the <strong>Is Active</strong> property.</p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="45970784-8390-48b7-8def-4328e5d9e5fc"><ac:rich-text-body><p>If the <strong>Is Active</strong> property does not appear in the Specification window, select <strong>All</strong> from the <strong>Properties</strong> drop-down at the top right of the window.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></li><li>Close the Specification window.</li><li><p class="auto-cursor-target">Select the Class and open the Alf editor window (select <strong>Windows &gt; Alf</strong>), if it isn't already open.</p></li><li>If the Class does not have a classifier behavior yet, then no code will appear in the Alf editor window, but the <strong>Create</strong> button will be active. Press <strong>Create</strong> to create a new classifier behavior for the Class.</li><li><p>Enter the Alf code for the classifier behavior and press <strong>Save</strong> to compile and save the code.</p></li></ol><p><br /></p><p>To edit an existing Alf body for a classifier behavior</p><hr /><ul><li class="auto-cursor-target"><p class="auto-cursor-target">Select the Class in the Model Browser or on a Class diagram and open the Alf editor window (select <strong>Windows &gt; Alf</strong>), if it isn't already open. The existing Alf code will appear in the window.</p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="c4c9a727-3926-4f0a-b6e0-ac1e1bd61226"><ac:rich-text-body>The Alf code for an Operation is actually stored as the Alf body of the method Behavior of the Operation (which is an Activity or Opaque Behavior, as created above). It is therefore possible to directly the edit the code on the method Behavior (as described in <a href="https://docs.nomagic.com/display/ALFP2024x/Using+Alf+to+define+Behaviors">Using Alf to define Behaviors</a>), but it is usually easier to act directly on the Operation.</ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:image><ri:attachment ri:filename="Using_Alf_To_Define_Classifier_Behaviors-Editing.png"><ri:page ri:space-key="ALFP2024x" ri:content-title="Using Alf for classifier behaviors" /></ri:attachment></ac:image></li></ul><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="de0ff9e8-046b-4ec3-8f70-363a9c239935"><ac:rich-text-body><p>While a classifier behavior may be edited like any other Behavior with an Alf body, as an asynchronous Behavior it is allowed to have Alf <em>accept</em> statements, which can handle Signals sent to instances of its active Class and are not allowed in synchronously called Behaviors. However, Alf requires that, for any Signal appearing in an <em>accept</em> statement, the containing Class must have a Reception (as shown below).</p><p><ac:image ac:align="center"><ri:attachment ri:filename="Using_Alf_To_Define_Classifier_Behaviors-Reception.png"><ri:page ri:space-key="ALFP2024x" ri:content-title="Using Alf for classifier behaviors" /></ri:attachment></ac:image></p><h6 style="text-align: center;">Referencing a Reception in an Alf accept statement</h6></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell><ac:layout-cell><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="346f11bf-3ef9-44b6-90b6-cc9597609ef1"><ac:parameter ac:name="title">Related pages</ac:parameter><ac:rich-text-body><ul><li><a href="https://docs.nomagic.com/display/ALFP2024x/The+Alf+editor">The Alf editor</a></li><li><a href="https://docs.nomagic.com/display/ALFP2024x/The+Alf+compiler">The Alf compiler</a></li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=137986104 space=ALFP2024x version=1 -->
## PAGE 00061: Using Alf for Operation methods

- page_id: `137986104`
- space_key: `ALFP2024x`
- source_url: https://docs.nomagic.com/spaces/ALFP2024x/pages/137986104/Using+Alf+for+Operation+methods
- version_number: 1
- version_date: `2023-09-22T11:48:48.133+02:00`
- ancestors: Alf Plugin Documentation > User Guide > Working with Alf > Using Alf in Class models
- labels: []

### NORMALIZED CONTENT

In UML, the behavior of an Operation of a Class can be defined using a Behavior element called the *method* of the Operation. You can use the [CONFLUENCE_PAGE title='The Alf editor' space='ALFP2024x'] to create an Alf body for a new Operation method or to edit the existing Alf body of a method.

To create an Alf body for a new method

1. Select the Operation in the Model Browser or on a Class diagram and open the Alf editor window (select Windows > Alf ), if it isn't already open.
2. If the Operation has no method yet, then no code will appear in the Alf editor window, but the Create button will be active.
3. Press Create to create a method for the operation.
4. Enter the Alf code for the Operation and press Save to compile and save the code.

To edit an existing Alf body for an Operation

- Select the Operation in the Model Browser or on a Class diagram and open the Alf editor window (select **Windows > Alf**), if it isn't already open. The existing Alf code will appear in the window. The Alf code for an Operation is actually stored as the Alf body of the method Behavior of the Operation (which is an Activity or Opaque Behavior, as created above). It is therefore possible to directly the edit the code on the method Behavior (as described in [CONFLUENCE_PAGE title='Using Alf to define Behaviors' space='ALFP2024x']), but it is usually easier to act directly on the Operation. [IMAGE alt='' src='']

#### PANEL: Related pages

Related pages

- [CONFLUENCE_PAGE title='The Alf editor' space='ALFP2024x']
- [CONFLUENCE_PAGE title='The Alf compiler' space='ALFP2024x']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p><br /></p><p>In UML, the behavior of an Operation of a Class can be defined using a Behavior element called the <em>method</em> of the Operation. You can use the <ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="The Alf editor" /><ac:plain-text-link-body><![CDATA[Alf editor]]></ac:plain-text-link-body></ac:link> to create an Alf body for a new Operation method or to edit the existing Alf body of a method.</p><p><br /></p><p>To create an Alf body for a new method</p><hr /><ol><li>Select the Operation in the Model Browser or on a Class diagram and open the Alf editor window (select <strong>Windows &gt; Alf</strong>), if it isn't already open.</li><li>If the Operation has no method yet, then no code will appear in the Alf editor window, but the <strong>Create</strong> button will be active.</li><li>Press <strong>Create</strong> to create a method for the operation.</li><li>Enter the Alf code for the Operation and press <strong>Save</strong> to compile and save the code.</li></ol><p><br /></p><p>To edit an existing Alf body for an Operation</p><hr /><ul><li><p class="auto-cursor-target">Select the Operation in the Model Browser or on a Class diagram and open the Alf editor window (select <strong>Windows &gt; Alf</strong>), if it isn't already open. The existing Alf code will appear in the window.</p><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="81a2b288-f5d8-4b7a-8873-b9a01c5c94be"><ac:rich-text-body><p>The Alf code for an Operation is actually stored as the Alf body of the method Behavior of the Operation (which is an Activity or Opaque Behavior, as created above). It is therefore possible to directly the edit the code on the method Behavior (as described in <ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="Using Alf to define Behaviors" /></ac:link>), but it is usually easier to act directly on the Operation.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><ac:image><ri:attachment ri:filename="Using_Alf_To_Define_Operation_Methods-Editing.png"><ri:page ri:space-key="ALFP2024x" ri:content-title="Using Alf for Operation methods" /></ri:attachment></ac:image></p></li></ul><p class="auto-cursor-target"><br /></p></ac:layout-cell><ac:layout-cell><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="3d989ba0-f93c-4bba-abf5-b26648f4b158"><ac:parameter ac:name="title">Related pages</ac:parameter><ac:rich-text-body><ul><li><ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="The Alf editor" /></ac:link></li><li><ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="The Alf compiler" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=137986110 space=ALFP2024x version=1 -->
## PAGE 00062: Using Alf for Property default values

- page_id: `137986110`
- space_key: `ALFP2024x`
- source_url: https://docs.nomagic.com/spaces/ALFP2024x/pages/137986110/Using+Alf+for+Property+default+values
- version_number: 1
- version_date: `2023-09-22T11:48:48.406+02:00`
- ancestors: Alf Plugin Documentation > User Guide > Working with Alf > Using Alf in Class models
- labels: []

### NORMALIZED CONTENT

You can use the[CONFLUENCE_PAGE title='The Alf editor' space='ALFP2024x'] to create an Alf body for a new default value for a Property (e.g., the attribute of a Class) or to edit the existing Alf body of a Property. The Alf expression for a default value is stored as the the body of an Opaque Expression with the language *Alf.* Compiling this Alf code results in the creation of an executable Activity that returns the value of the Alf expression. This Activity is linked to the Opaque Expression as its the **Behavior** property. (See also the discussion on [CONFLUENCE_PAGE title='The Alf compiler' space='ALFP2024x'])

To create a new default value for a Property using Alf

1. Open the Specification window for the Property (from either the Model Browser or its representation on a Class diagram).
2. Click on the Default Value field, press the Show Shortcut Menu button (see the figure below) and select Value Specification > Opaque Expression . [ATTACHMENT filename='Using_Alf_To_Define_Default_Values-Creating.png']
3. Close the Specification window.
4. Select the Property (either in the Model Browser or as it appears on a Class diagram) and open the Alf editor window (select Windows > Alf ), if it isn't already open.
5. Enter an Alf expression and click on the **Save** button to compile and save the code. Note that the text entered must be for an *expression,* not a statement. Therefore, it must *not* have a semicolon at the end. If the Property already has a non-Alf default value, then, to enter an Alf default value, open its Specification window and proceed as above to create a new default value with an Alf body, replacing the previous default value.

To edit an existing Alf body for the default value of a Property

- Select the Property in the Model Browser or on a Class Diagram and open the Alf editor window (select Windows > Alf ), if it isn't already open. The existing Alf expression will be displayed in the window. [ATTACHMENT filename='Using_Alf_To_Define_Default_Values-Editing.png']

The Alf code for a default value can also be entered or edited directly in the **Body and Language** property in the Specification window for the Opaque Expression. If you open the Edit Body and Language window, then the Alf code may be edited just as in the Alf editor window. However, instead of **Save** and **Revert** buttons, this window has **OK** and **Cancel** buttons, either of which will close it. If you press **OK**, then the Alf text is saved, and, if it has no errors, compiled. If you press **Cancel**, the Alf text is *not* saved.

[IMAGE alt='' src='']

###### Editing Alf code for a default value in an Opaque Expression body

To be recognized as Alf code, the **Body** of an Opaque Expression must have the **Language** Alf. If your project was created using the Alf project template, then Alf will be the default language. Otherwise, select Alf from the **Language** menu (you may have to scroll upwards in the menu to find the selection for *Alf*).

To make Alf the default language for Opaque Expressions

1. Select Options > Project .
2. On the left, under Default model properties , select Opaque Expression .
3. Click on the Language field and then on the small + button on the right.
4. Enter Alf (spelled and capitalized in exactly that way) and click on OK .
5. Click on OK to close the options window.

.

#### PANEL: Related pages

Related pages

- [CONFLUENCE_PAGE title='The Alf editor' space='ALFP2024x']
- [CONFLUENCE_PAGE title='The Alf compiler' space='ALFP2024x']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p>You can use the<ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="The Alf editor" /><ac:plain-text-link-body><![CDATA[ Alf editor]]></ac:plain-text-link-body></ac:link> to create an Alf body for a new default value for a Property (e.g., the attribute of a Class) or to edit the existing Alf body of a Property. The Alf expression for a default value is stored as the the body of an Opaque Expression with the language <em>Alf.</em> Compiling this Alf code results in the creation of an executable Activity that returns the value of the Alf expression. This Activity is linked to the Opaque Expression as its the <strong>Behavior</strong> property. (See also the discussion on <ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="The Alf compiler" /><ac:plain-text-link-body><![CDATA[the Alf compiler]]></ac:plain-text-link-body></ac:link>)</p><p><br /></p><p>To create a new default value for a Property using Alf</p><hr /><ol><li>Open the Specification window for the Property (from either the Model Browser or its representation on a Class diagram).</li><li>Click on the <strong>Default Value</strong> field, press the <strong>Show Shortcut Menu</strong> button (see the figure below) and select <strong>Value Specification &gt; Opaque Expression</strong>.<br /><br /><ac:image><ri:attachment ri:filename="Using_Alf_To_Define_Default_Values-Creating.png"><ri:page ri:space-key="ALFP2024x" ri:content-title="Using Alf for Property default values" /></ri:attachment></ac:image><br /><br /></li><li>Close the Specification window.</li><li>Select the Property (either in the Model Browser or as it appears on a Class diagram) and open the Alf editor window (select <strong>Windows &gt; Alf</strong>), if it isn't already open.</li><li><p class="auto-cursor-target">Enter an Alf expression and click on the <strong>Save</strong> button to compile and save the code.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="c2a517be-44c4-4462-adb4-5bddd9a6c837"><ac:rich-text-body><p>Note that the text entered must be for an <em>expression,</em> not a statement. Therefore, it must <em>not</em> have a semicolon at the end.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="12f55cf8-1018-4eec-846e-ef7b3df2ca59"><ac:rich-text-body><p>If the Property already has a non-Alf default value, then, to enter an Alf default value, open its Specification window and proceed as above to create a new default value with an Alf body, replacing the previous default value.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></li></ol><p><br /></p><p>To edit an existing Alf body for the default value of a Property</p><hr /><ul><li>Select the Property in the Model Browser or on a Class Diagram and open the Alf editor window (select <strong>Windows &gt; Alf</strong>), if it isn't already open. The existing Alf expression will be displayed in the window.<br /><ac:image><ri:attachment ri:filename="Using_Alf_To_Define_Default_Values-Editing.png"><ri:page ri:space-key="ALFP2024x" ri:content-title="Using Alf for Property default values" /></ri:attachment></ac:image></li></ul><p>The Alf code for a default value can also be entered or edited directly in the <strong>Body and Language</strong> property in the Specification window for the Opaque Expression. If you open the Edit Body and Language window, then the Alf code may be edited just as in the Alf editor window. However, instead of <strong>Save</strong> and <strong>Revert</strong> buttons, this window has <strong>OK</strong> and <strong>Cancel</strong> buttons, either of which will close it. If you press <strong>OK</strong>, then the Alf text is saved, and, if it has no errors, compiled. If you press <strong>Cancel</strong>, the Alf text is <em>not</em> saved.</p><p class="auto-cursor-target"><ac:image><ri:attachment ri:filename="Using_Alf_To_Define_Default_Values-Editing_Body.png"><ri:page ri:space-key="ALFP2024x" ri:content-title="Using Alf for Property default values" /></ri:attachment></ac:image></p><h6 style="text-align: center;">Editing Alf code for a default value in an Opaque Expression body</h6><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="98378a4c-9ab8-412c-a621-14fd4bbe2518"><ac:rich-text-body><p>To be recognized as Alf code, the <strong>Body</strong> of an Opaque Expression must have the <strong>Language</strong> Alf. If your project was created using the Alf project template, then Alf will be the default language. Otherwise, select Alf from the <strong>Language</strong> menu (you may have to scroll upwards in the menu to find the selection for <em>Alf</em>).</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="11b9fa3c-bdbf-4a14-a927-0692307c0445"><ac:rich-text-body><p>To make Alf the default language for Opaque Expressions</p><hr /><ol><li>Select <strong>Options &gt; Project</strong>.</li><li>On the left, under <strong>Default model properties</strong>, select <strong>Opaque Expression</strong>.</li><li>Click on the <strong>Language</strong> field and then on the small + button on the right.</li><li>Enter <em>Alf</em> (spelled and capitalized in exactly that way) and click on <strong>OK</strong>.</li><li>Click on <strong>OK</strong> to close the options window.</li></ol></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><p>.</p></ac:layout-cell><ac:layout-cell><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="9eb6015c-992c-47e3-b787-78444fa59b54"><ac:parameter ac:name="title">Related pages</ac:parameter><ac:rich-text-body><ul><li><ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="The Alf editor" /></ac:link></li><li><ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="The Alf compiler" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=137986118 space=ALFP2024x version=1 -->
## PAGE 00063: Using Alf for State Behaviors

- page_id: `137986118`
- space_key: `ALFP2024x`
- source_url: https://docs.nomagic.com/spaces/ALFP2024x/pages/137986118/Using+Alf+for+State+Behaviors
- version_number: 1
- version_date: `2023-09-22T11:48:48.837+02:00`
- ancestors: Alf Plugin Documentation > User Guide > Working with Alf > Using Alf in State Machine models
- labels: []

### NORMALIZED CONTENT

A State in a State Machine can have an entry Behavior (which is executed when the State is entered), an exit Behavior (which is executed when the State is exited) and/or a do-activity Behavior (which is executed asynchronously while the State is active). You can us the [CONFLUENCE_PAGE title='The Alf editor' space='ALFP2024x'] to create an Alf body for, or edit the existing Alf body of, any one of these kinds of Behaviors.

To create and Alf body for a State behavior

1. Select the State (in the Model Browser or on a State Machine diagram) and open the Alf editor window (select Windows > Alf ), it it isn't already open.
2. In the Alf editor window, press Create . A menu will pop up with available options for creating a State Behavior. [ATTACHMENT filename='Using_Alf_For_State_Behaviors-Creating.png']
3. Select Entry Behavior , Do Activity Behavior or Exit Behavior as appropriate.
4. Enter the Alf code for the Behavior and press **Save** to compile and save it. The Alf code for a State Behavior can access attribute values of the context Classifier of the State Machine containing its State (using Alf *this* expressions). It can also [CONFLUENCE_PAGE title='Accessing Event data' space='ALFP2024x'] in the Event occurrence that triggered its execution (e.g., the attribute data of a received Signal).

To edit the Alf code for a State Behavior

- Select the Behavior (in the Model Browser or as represented on a State Machine diagram) and open the Alf editor window (select **Windows > Alf**), if it isn't already open. The Alf code will appear in the window. To edit a State Behavior on a State Machine diagram, be sure to select the specific Behavior that you want to edit (entry, do or exit), and not on the State itself [IMAGE alt='' src=''] Note that, even while you are editing an existing State Behavior, the **Create** button stays active if there are remaining State Behaviors that could be created. For instance, while you are editing an entry Behavior, you can press **Create** in order to create an exit Behavior (if the State does not already have one).

If you create a State Behavior as an Opaque Behavior, then Alf code for it can also be entered or edited directly in the **Body and Language** property for it in the Specification window for the State. If you open the Edit Body and Language window, then the Alf code may be edited just as in the Alf editor window. However, instead of **Save** and******Revert** buttons, this window has **OK** and **Cancel** buttons, either of which will close it. If you press **OK**, then the text is saved, and, if it has no errors, compiled. If you press **Cancel**, the Alf text is *not* saved.

[IMAGE alt='' src='']

###### Editing Alf code for a State Behavior in an Opaque Behavior body

To be recognized as Alf code, the **Body** of an Opaque Behavior must have the **Language** Alf. If your project was created using the Alf project template, then Alf will be the default language. Otherwise, select Alf from the **Language** menu (you may have to scroll upwards in the menu to find the selection for *Alf).*

To make Alf the default language for Opaque Behaviors

1. Select Options > Project .
2. On the left, under Default model properties , select Opaque Behavior .
3. Click on the Language field and then on the small + button on the right.
4. Enter Alf (spelled and capitalized in exactly that way) and click on OK .
5. Click on OK to close the options window.

If the **Opaque Behavior Display Mode** symbol property of a State is set to Body, then any State Behaviors that are Opaque Behaviors can also be edited directly on a State Machine diagram showing the State and its behaviors. Since such editing does not use the Alf editor, no parsing or constraint checking happens while Alf code is being edited. The code is compiled once you finish editing it, and, if there are compilation errors, they will be recorded in an error annotation on the Opaque Behavior.

#### PANEL: Related pages

Related pages

- [CONFLUENCE_PAGE title='The Alf editor' space='ALFP2024x']
- [CONFLUENCE_PAGE title='The Alf compiler' space='ALFP2024x']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p>A State in a State Machine can have an entry Behavior (which is executed when the State is entered), an exit Behavior (which is executed when the State is exited) and/or a do-activity Behavior (which is executed asynchronously while the State is active). You can us the <ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="The Alf editor" /><ac:plain-text-link-body><![CDATA[Alf editor]]></ac:plain-text-link-body></ac:link> to create an Alf body for, or edit the existing Alf body of, any one of these kinds of Behaviors.</p><p><br /></p><p>To create and Alf body for a State behavior</p><hr /><ol><li>Select the State (in the Model Browser or on a State Machine diagram) and open the Alf editor window (select <strong>Windows &gt; Alf</strong>), it it isn't already open.</li><li>In the Alf editor window, press <strong>Create</strong>. A menu will pop up with available options for creating a State Behavior.<br /><ac:image><ri:attachment ri:filename="Using_Alf_For_State_Behaviors-Creating.png"><ri:page ri:space-key="ALFP2024x" ri:content-title="Using Alf for State Behaviors" /></ri:attachment></ac:image></li><li>Select <strong>Entry Behavior</strong>, <strong>Do Activity Behavior</strong> or <strong>Exit Behavior</strong> as appropriate.</li><li><p class="auto-cursor-target">Enter the Alf code for the Behavior and press <strong>Save</strong> to compile and save it.</p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="e30bb31a-1e14-4768-a924-ca87f8034c67"><ac:rich-text-body><p>The Alf code for a State Behavior can access attribute values of the context Classifier of the State Machine containing its State (using Alf <em>this</em> expressions). It can also <ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="Accessing Event data" /><ac:plain-text-link-body><![CDATA[access the data]]></ac:plain-text-link-body></ac:link> in the Event occurrence that triggered its execution (e.g., the attribute data of a received Signal).</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></li></ol><p><br /></p><p>To edit the Alf code for a State Behavior</p><hr /><ul><li><p class="auto-cursor-target">Select the Behavior (in the Model Browser or as represented on a State Machine diagram) and open the Alf editor window (select <strong>Windows &gt; Alf</strong>), if it isn't already open. The Alf code will appear in the window.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="3c19f983-2bde-4abe-8c55-03e8f8f0d7b2"><ac:rich-text-body><p>To edit a State Behavior on a State Machine diagram, be sure to select the specific Behavior that you want to edit (entry, do or exit), and not on the State itself</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><ac:image><ri:attachment ri:filename="Using_Alf_For_State_Behaviors-Editing.png"><ri:page ri:space-key="ALFP2024x" ri:content-title="Using Alf for State Behaviors" /></ri:attachment></ac:image></p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="ffafe7df-780a-4dcc-af9d-61b9e134c98f"><ac:rich-text-body><p>Note that, even while you are editing an existing State Behavior, the <strong>Create</strong> button stays active if there are remaining State Behaviors that could be created. For instance, while you are editing an entry Behavior, you can press <strong>Create</strong> in order to create an exit Behavior (if the State does not already have one).</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></li></ul><p><br /></p><p>If you create a State Behavior as an Opaque Behavior, then Alf code for it  can also be entered or edited directly in the <strong>Body and Language</strong> property for it in the Specification window for the State. If you open the Edit Body and Language window, then the Alf code may be edited just as in the Alf editor window. However, instead of <strong>Save</strong> and<strong> </strong><strong>Revert</strong> buttons, this window has <strong>OK</strong> and <strong>Cancel</strong> buttons, either of which will close it. If you press <strong>OK</strong>, then the text is saved, and, if it has no errors, compiled. If you press <strong>Cancel</strong>, the Alf text is <em>not</em> saved.</p><p class="auto-cursor-target"><ac:image><ri:attachment ri:filename="Using_Alf_For_State_Behaviors-Editing_Body.png"><ri:page ri:space-key="ALFP2024x" ri:content-title="Using Alf for State Behaviors" /></ri:attachment></ac:image></p><h6 style="text-align: center;">Editing Alf code for a State Behavior in an Opaque Behavior body</h6><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="ee76b391-b2a5-4ee4-864b-6860b30444ab"><ac:rich-text-body><p>To be recognized as Alf code, the <strong>Body</strong> of an Opaque Behavior must have the <strong>Language</strong> Alf. If your project was created using the Alf project template, then Alf will be the default language. Otherwise, select Alf from the <strong>Language</strong> menu (you may have to scroll upwards in the menu to find the selection for <em>Alf).</em></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="11b9fa3c-bdbf-4a14-a927-0692307c0445"><ac:rich-text-body><p>To make Alf the default language for Opaque Behaviors</p><hr /><ol><li>Select <strong>Options &gt; Project</strong>.</li><li>On the left, under <strong>Default model properties</strong>, select <strong>Opaque Behavior</strong>.</li><li>Click on the <strong>Language</strong> field and then on the small + button on the right.</li><li>Enter <em>Alf</em> (spelled and capitalized in exactly that way) and click on <strong>OK</strong>.</li><li>Click on <strong>OK</strong> to close the options window.</li></ol></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target">If the <strong>Opaque Behavior Display Mode</strong> symbol property of a State is set to Body, then any State Behaviors that are Opaque Behaviors can also be edited directly on a State Machine diagram showing the State and its behaviors. Since such editing does not use the Alf editor, no parsing or constraint checking happens while Alf code is being edited. The code is compiled once you finish editing it, and, if there are compilation errors, they will be recorded in an error annotation on the Opaque Behavior.</p></ac:layout-cell><ac:layout-cell><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="e9973a0a-e5aa-4add-93d7-4071328c7f81"><ac:parameter ac:name="title">Related pages</ac:parameter><ac:rich-text-body><ul><li><ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="The Alf editor" /></ac:link></li><li><ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="The Alf compiler" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=137986122 space=ALFP2024x version=1 -->
## PAGE 00064: Using Alf for Transition effect Behaviors

- page_id: `137986122`
- space_key: `ALFP2024x`
- source_url: https://docs.nomagic.com/spaces/ALFP2024x/pages/137986122/Using+Alf+for+Transition+effect+Behaviors
- version_number: 1
- version_date: `2023-09-22T11:48:49.027+02:00`
- ancestors: Alf Plugin Documentation > User Guide > Working with Alf > Using Alf in State Machine models
- labels: []

### NORMALIZED CONTENT

You can use the [CONFLUENCE_PAGE title='The Alf editor' space='ALFP2024x'] to create an Alf body for the effect Behavior of a Transition in a State Machine or to edit the existing Alf body of an effect Behavior.

To create an Alf body for an effect Behavior

1. Select the Transition (in the Model Browser or as represented on a State Machine diagram) and open the Alf editor window (select Windows > Alf ), if it isn't already open.
2. In the Alf editor window, press Create . A menu will pop up with available options for creating Transition Behaviors. [ATTACHMENT filename='Using_Alf_For_Transition_Effect_Behaviors-Creating.png']
3. Select Effect Behavior .
4. Enter the Alf code for the Behavior and press **Save** to compile and save it. The Alf code for an effect Behavior can access attribute values of the context Classifier of the State Machine containing its Transition (using Alf *this* expressions). It can also [CONFLUENCE_PAGE title='Accessing Event data' space='ALFP2024x'] in the Event occurrence that triggered its execution (e.g., the attribute data of a received Signal).

To edit the Alf code for an effect Behavior

- Select the Transition (in the Model Browser or as represented on a State Machine diagram) and open the Alf editor window (select **Windows > Alf**), if it isn't already open. The Alf code will appear in the window. 
 
[IMAGE alt='' src=''] Even while you are editing an existing effect Behavior, the **Create** button stays active if the Transition does not have a guard. Press **Create** in order to [CONFLUENCE_PAGE title='Using Alf for Transition guard Expressions' space='ALFP2024x'] on the Transaction.

If you create an effect Behavior as an Opaque Behavior, then Alf code for it can also be entered or edited directly in the **Body and Language** property for it in the Specification window for the Transition. If you open the Edit Body and Language window, then the Alf code may be edited just as in the Alf editor window. However, instead of **Save** and **Revert** buttons, this window has **OK** and **Cancel** buttons, either of which will close it. If you press **OK**, then the text is saved, and, if it has no errors, compiled. If you press **Cancel**, the Alf text is *not* saved.

[IMAGE alt='' src='']

###### Editing Alf code for a Transition effect Behavior in an Opaque Behavior body

To be recognized as Alf code, the **Body** of an Opaque Behavior must have the **Language** Alf. If your project was created using the Alf project template, then Alf will be the default language. Otherwise, select Alf from the **Language** menu (you may have to scroll upwards in the menu to find the selection for *Alf*).

To make Alf the default language for Opaque Behaviors

1. Select Options > Project .
2. On the left, under Default model properties , select Opaque Behavior .
3. Click on the Language field and then on the small + button on the right.
4. Enter Alf (spelled and capitalized in exactly that way) and click on OK .
5. Click on OK to close the options window.

#### PANEL: Related pages

Related pages

- [CONFLUENCE_PAGE title='The Alf editor' space='ALFP2024x']
- [CONFLUENCE_PAGE title='The Alf compiler' space='ALFP2024x']
- [CONFLUENCE_PAGE title='Using Alf for Transition guard Expressions' space='ALFP2024x']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p>You can use the <ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="The Alf editor" /><ac:plain-text-link-body><![CDATA[Alf editor]]></ac:plain-text-link-body></ac:link> to create an Alf body for the effect Behavior of a Transition in a State Machine or to edit the existing Alf body of an effect Behavior.</p><p><br /></p><p>To create an Alf body for an effect Behavior</p><hr /><ol><li>Select the Transition (in the Model Browser or as represented on a State Machine diagram) and open the Alf editor window (select <strong>Windows &gt; Alf</strong>), if it isn't already open.</li><li>In the Alf editor window, press <strong>Create</strong>. A menu will pop up with available options for creating Transition Behaviors.<br /><ac:image><ri:attachment ri:filename="Using_Alf_For_Transition_Effect_Behaviors-Creating.png"><ri:page ri:space-key="ALFP2024x" ri:content-title="Using Alf for Transition effect Behaviors" /></ri:attachment></ac:image></li><li>Select <strong>Effect Behavior</strong>.</li><li><p class="auto-cursor-target">Enter the Alf code for the Behavior and press <strong>Save</strong> to compile and save it.</p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="3bbcd71d-6769-4ef7-acb5-c20aee438d12"><ac:rich-text-body><p>The Alf code for an effect Behavior can access attribute values of the context Classifier of the State Machine containing its Transition (using Alf <em>this</em> expressions). It can also <ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="Accessing Event data" /><ac:plain-text-link-body><![CDATA[access the data]]></ac:plain-text-link-body></ac:link> in the Event occurrence that triggered its execution (e.g., the attribute data of a received Signal).</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></li></ol><p><br /></p><p>To edit the Alf code for an effect Behavior</p><hr /><ul><li><p class="auto-cursor-target">Select the Transition (in the Model Browser or as represented on a State Machine diagram) and open the Alf editor window (select <strong>Windows &gt; Alf</strong>), if it isn't already open. The Alf code will appear in the window.<br /><br /><ac:image><ri:attachment ri:filename="Using_Alf_For_Transition_Effect_Behaviors-Editing.png"><ri:page ri:space-key="ALFP2024x" ri:content-title="Using Alf for Transition effect Behaviors" /></ri:attachment></ac:image></p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="62693fe8-8344-4bf2-b436-6dd8321f1552"><ac:rich-text-body><p>Even while you are editing an existing effect Behavior, the <strong>Create</strong> button stays active if the Transition does not have a guard. Press <strong>Create</strong> in order to <ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="Using Alf for Transition guard Expressions" /><ac:plain-text-link-body><![CDATA[create a guard expression]]></ac:plain-text-link-body></ac:link> on the Transaction.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></li></ul><p class="auto-cursor-target"><br /></p><p><br /></p><p>If you create an effect Behavior as an Opaque Behavior, then Alf code for it can also be entered or edited directly in the <strong>Body and Language</strong> property for it in the Specification window for the Transition. If you open the Edit Body and Language window, then the Alf code may be edited just as in the Alf editor window. However, instead of <strong>Save</strong> and <strong>Revert</strong> buttons, this window has <strong>OK</strong> and <strong>Cancel</strong> buttons, either of which will close it. If you press <strong>OK</strong>, then the text is saved, and, if it has no errors, compiled. If you press <strong>Cancel</strong>, the Alf text is <em>not</em> saved.</p><p class="auto-cursor-target"><ac:image ac:align="center"><ri:attachment ri:filename="Using_Alf_For_Transition_Effect_Behaviors-Editing_Body.png"><ri:page ri:space-key="ALFP2024x" ri:content-title="Using Alf for Transition effect Behaviors" /></ri:attachment></ac:image></p><h6 style="text-align: center;">Editing Alf code for a Transition effect Behavior in an Opaque Behavior body</h6><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="ee76b391-b2a5-4ee4-864b-6860b30444ab"><ac:rich-text-body><p>To be recognized as Alf code, the <strong>Body</strong> of an Opaque Behavior must have the <strong>Language</strong> Alf. If your project was created using the Alf project template, then Alf will be the default language. Otherwise, select Alf from the <strong>Language</strong> menu (you may have to scroll upwards in the menu to find the selection for <em>Alf</em>).</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="11b9fa3c-bdbf-4a14-a927-0692307c0445"><ac:rich-text-body><p>To make Alf the default language for Opaque Behaviors</p><hr /><ol><li>Select <strong>Options &gt; Project</strong>.</li><li>On the left, under <strong>Default model properties</strong>, select <strong>Opaque Behavior</strong>.</li><li>Click on the <strong>Language</strong> field and then on the small + button on the right.</li><li>Enter <em>Alf</em> (spelled and capitalized in exactly that way) and click on <strong>OK</strong>.</li><li>Click on <strong>OK</strong> to close the options window.</li></ol></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell><ac:layout-cell><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="8e5d8541-78cb-408b-9469-ac93a3eb0173"><ac:parameter ac:name="title">Related pages</ac:parameter><ac:rich-text-body><ul><li><ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="The Alf editor" /></ac:link></li><li><ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="The Alf compiler" /></ac:link></li><li><ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="Using Alf for Transition guard Expressions" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=137986126 space=ALFP2024x version=1 -->
## PAGE 00065: Using Alf for Transition guard Expressions

- page_id: `137986126`
- space_key: `ALFP2024x`
- source_url: https://docs.nomagic.com/spaces/ALFP2024x/pages/137986126/Using+Alf+for+Transition+guard+Expressions
- version_number: 1
- version_date: `2023-09-22T11:48:49.563+02:00`
- ancestors: Alf Plugin Documentation > User Guide > Working with Alf > Using Alf in State Machine models
- labels: []

### NORMALIZED CONTENT

You can use the [CONFLUENCE_PAGE title='The Alf editor' space='ALFP2024x'] to create an Alf Expression for the guard of a Transition in a State Machine or to edit an existing guard Expression.

To create an Alf guard Expression

1. Select the Transition (in the Model Browser or as represented on a State Machine diagram) and open the Alf editor window (select Windows > Alf ), if it isn't already open.
2. In the Alf editor window, press Create . A menu will pop up with available options for creating a Transition effect Behavior or guard Expression. [ATTACHMENT filename='Using_Alf_For_Transition_Guard_Expressions-Creating.png']
3. Select Guard Expression .
4. Enter the Alf code for the Expression and press **Save** to compile and save it. Note that the text entered must be an *expression,* not a statement. Therefore, it must *not* have a semicolon at the end. The expression can access attribute values of the context Classifier of the Activity containing its Activity Edge (using Alf *this* expressions) or the decision input value for the Decision Node (see [Accessing data in Activity Edge guards](https://docs.nomagic.com/display/ALFP2024x/Accessing+data+in+Activity+Edge+guards)).

To edit an Alf guard Expression

1. Open the Alf editor window (select Window > Alf ), if it is not already open.
2. On the State Machine diagram, click on the *text* of the Transition trigger with the guard to be edited. If a Transition has a guard Expression in Alf, but no effect Behavior, than selecting the Transition on a diagram results in the Alf code for the guard being displayed in the Alf editor window. However, if the Transition also has an effect Behavior in Alf, then selecting the Transition *line* on a diagram results in the Alf code for the *Behavior* being displayed in the Alf Editor. In order to edit the *guard,* select the *text* for the trigger of Transition.
3. Enter the Alf code for the guard Expression and press Save to compile and save it. [IMAGE alt='' src='']

The Alf code for a guard Expression can also be entered or edited directly in the **Guard** property in the Specification window of the Transition. If you open the Edit Guard window, then the Alf code can be edited just as in the Alf editor window. However, instead of **Save** and **Revert** buttons, this window has **OK** and **Cancel** buttons, either of which will close it. If you press **OK**, then the Alf text is saved, and, if it has no errors, compiled. If you press **Cancel**, the Alf text is *not* saved.

[IMAGE alt='' src='']

###### Editing code for a Transition guard Expression in the Edit Guard Window

To be recognized as Alf code, the **Body** of an Opaque Expression must have the **Language** Alf. If your project was created using the Alf project template, then Alf will be the default language. Otherwise, select Alf from the **Language** menu (you may have to scroll upwards in the menu to find the selection for *Alf*).

To make Alf the default language for Opaque Expressions

1. Select Options > Environment .
2. From the General options, select Editing .
3. For the Opaque Expression Default Language option, type Alf (with exactly that spelling and capitalization). Click OK

#### PANEL: Related pages

Related pages

- [CONFLUENCE_PAGE title='The Alf editor' space='ALFP2024x']
- [CONFLUENCE_PAGE title='The Alf compiler' space='ALFP2024x']
- [CONFLUENCE_PAGE title='Using Alf for Transition effect Behaviors' space='ALFP2024x']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p><br /></p><p><br /></p><p>You can use the <ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="The Alf editor" /><ac:plain-text-link-body><![CDATA[Alf editor]]></ac:plain-text-link-body></ac:link> to create an Alf Expression for the guard of a Transition in a State Machine or to edit an existing guard Expression.</p><p><br /></p><p>To create an Alf guard Expression</p><hr /><ol><li>Select the Transition (in the Model Browser or as represented on a State Machine diagram) and open the Alf editor window (select <strong>Windows &gt; Alf</strong>), if it isn't already open.</li><li>In the Alf editor window, press <strong>Create</strong>. A menu will pop up with available options for creating a Transition effect Behavior or guard Expression.<br /><ac:image><ri:attachment ri:filename="Using_Alf_For_Transition_Guard_Expressions-Creating.png"><ri:page ri:space-key="ALFP2024x" ri:content-title="Using Alf for Transition guard Expressions" /></ri:attachment></ac:image></li><li>Select <strong>Guard Expression</strong>.</li><li><p class="auto-cursor-target">Enter the Alf code for the Expression and press <strong>Save</strong> to compile and save it.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="7bf0c2d9-3850-4817-9595-c47eb12e127d"><ac:rich-text-body><p>Note that the text entered must be an <em>expression,</em> not a statement. Therefore, it must <em>not</em> have a semicolon at the end.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="bd903332-600e-4d75-8be6-a73ce9e64c0f"><ac:rich-text-body><p>The expression can access attribute values of the context Classifier of the Activity containing its Activity Edge (using Alf <em>this</em> expressions) or the <span class="confluence-link">decision input value for the Decision Node</span> (see <a href="https://docs.nomagic.com/display/ALFP2024x/Accessing+data+in+Activity+Edge+guards">Accessing data in Activity Edge guards</a>).</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></li></ol><p><br /></p><p>To edit an Alf guard Expression</p><hr /><ol><li>Open the Alf editor window (select <strong>Window &gt; Alf</strong>), if it is not already open.</li><li><p class="auto-cursor-target">On the State Machine diagram, click on the <em>text</em> of the Transition trigger with the guard to be edited.</p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="22a38bed-b8b3-443d-9458-1a0811f5ff2f"><ac:rich-text-body><p>If a Transition has a guard Expression in Alf, but no effect Behavior, than selecting the Transition on a diagram results in the Alf code for the guard being displayed in the Alf editor window. However, if the Transition also has an effect Behavior in Alf, then selecting the Transition <em>line</em> on a diagram results in the Alf code for the <em>Behavior</em> being displayed in the Alf Editor. In order to edit the <em>guard,</em> select the <em>text</em> for the trigger of Transition.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></li><li>Enter the Alf code for the guard Expression and press <strong>Save</strong> to compile and save it.<br /><p class="auto-cursor-target"><ac:image ac:height="400"><ri:attachment ri:filename="Using_Alf_For_Transition_Guard_Expressions-Editing-18.5.png"><ri:page ri:space-key="ALFP2024x" ri:content-title="Using Alf for Transition guard Expressions" /></ri:attachment></ac:image></p></li></ol><p><br /></p><p>The Alf code for a guard Expression can also be entered or edited directly in the <strong>Guard</strong> property in the Specification window of the Transition. If you open the Edit Guard window, then the Alf code can be edited just as in the Alf editor window. However, instead of <strong>Save</strong> and <strong>Revert</strong> buttons, this window has <strong>OK</strong> and <strong>Cancel</strong> buttons, either of which will close it. If you press <strong>OK</strong>, then the Alf text is saved, and, if it has no errors, compiled. If you press <strong>Cancel</strong>, the Alf text is <em>not</em> saved.</p><p><ac:image ac:align="center"><ri:attachment ri:filename="Using_Alf_For_Transition_Guard_Expressions-Editing_Body.png"><ri:page ri:space-key="ALFP2024x" ri:content-title="Using Alf for Transition guard Expressions" /></ri:attachment></ac:image></p><h6 style="text-align: center;">Editing code for a Transition guard Expression in the Edit Guard Window</h6><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="ee76b391-b2a5-4ee4-864b-6860b30444ab"><ac:rich-text-body><p>To be recognized as Alf code, the <strong>Body</strong> of an Opaque Expression must have the <strong>Language</strong> Alf. If your project was created using the Alf project template, then Alf will be the default language. Otherwise, select Alf from the <strong>Language</strong> menu (you may have to scroll upwards in the menu to find the selection for <em>Alf</em>).</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="6c1dc32f-7897-4fa6-8937-039bc4a4a55a"><ac:rich-text-body><p>To make Alf the default language for Opaque Expressions</p><hr /><ol><li>Select <strong>Options &gt; Environment</strong>.</li><li>From the <strong>General</strong> options, select <strong>Editing</strong>.</li><li>For the <strong>Opaque Expression Default Language</strong> option, type <em>Alf</em> (with exactly that spelling and capitalization). Click <strong>OK</strong></li></ol></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell><ac:layout-cell><p><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="fcd59470-9da1-40d5-bf65-8ac8f428d4ba"><ac:parameter ac:name="title">Related pages</ac:parameter><ac:rich-text-body><ul><li><ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="The Alf editor" /></ac:link></li><li><ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="The Alf compiler" /></ac:link></li><li><ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="Using Alf for Transition effect Behaviors" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=137986138 space=ALFP2024x version=1 -->
## PAGE 00066: Using Alf in Activity models

- page_id: `137986138`
- space_key: `ALFP2024x`
- source_url: https://docs.nomagic.com/spaces/ALFP2024x/pages/137986138/Using+Alf+in+Activity+models
- version_number: 1
- version_date: `2023-09-22T11:48:50.243+02:00`
- ancestors: Alf Plugin Documentation > User Guide > Working with Alf
- labels: []

### NORMALIZED CONTENT

The following kinds of elements in an Activity model can have Alf bodies:

- Opaque Actions
- Opaque Expressions used as guards on Activity Edges

In general, to edit the Alf body of such an element in the Alf editor window, you select it either in the Model Browser or directly on its symbol if it appears on an Activity diagram.

#### PANEL: Related pages

Related pages

- [CONFLUENCE_PAGE title='The Alf editor' space='ALFP2024x']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p>The following kinds of elements in an Activity model can have Alf bodies:</p><ul><li>Opaque Actions</li><li>Opaque Expressions used as guards on Activity Edges</li></ul><p>In general, to edit the Alf body of such an element in the Alf editor window, you select it either in the Model Browser or directly on its symbol if it appears on an Activity diagram.</p></ac:layout-cell><ac:layout-cell><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="d2a86025-0b6e-4965-83d6-ff254a31d7bd"><ac:parameter ac:name="title">Related pages</ac:parameter><ac:rich-text-body><ul><li><ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="The Alf editor" /></ac:link></li></ul><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="82d87929-21eb-4c12-bb24-3c891e0ca454" /></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=137986103 space=ALFP2024x version=1 -->
## PAGE 00067: Using Alf in Class models

- page_id: `137986103`
- space_key: `ALFP2024x`
- source_url: https://docs.nomagic.com/spaces/ALFP2024x/pages/137986103/Using+Alf+in+Class+models
- version_number: 1
- version_date: `2023-09-22T11:48:47.982+02:00`
- ancestors: Alf Plugin Documentation > User Guide > Working with Alf
- labels: []

### NORMALIZED CONTENT

The following kinds of elements in a Class model can have Alf bodies:

- The method of an Operation.
- The classifier behavior of a Class.

In general, to edit the Alf body of such an element in the Alf editor window, you select it either in the Model Browser or directly on its symbol if it appears on a Class diagram.

#### PANEL: Related pages

Related pages

- [CONFLUENCE_PAGE title='The Alf editor' space='ALFP2024x']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p>The following kinds of elements in a Class model can have Alf bodies:</p><ul><li>The method of an Operation.</li><li>The classifier behavior of a Class.</li></ul><p>In general, to edit the Alf body of such an element in the Alf editor window, you select it either in the Model Browser or directly on its symbol if it appears on a Class diagram.</p></ac:layout-cell><ac:layout-cell><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="22498a82-777c-493e-8607-b02503b17a96"><ac:parameter ac:name="title">Related pages</ac:parameter><ac:rich-text-body><ul><li><ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="The Alf editor" /></ac:link></li></ul><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="70e544ea-275c-425a-92ca-78ee8d504357" /></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=137986139 space=ALFP2024x version=1 -->
## PAGE 00068: Using Alf in Opaque Action bodies

- page_id: `137986139`
- space_key: `ALFP2024x`
- source_url: https://docs.nomagic.com/spaces/ALFP2024x/pages/137986139/Using+Alf+in+Opaque+Action+bodies
- version_number: 1
- version_date: `2023-09-22T11:48:50.313+02:00`
- ancestors: Alf Plugin Documentation > User Guide > Working with Alf > Using Alf in Activity models
- labels: []

### NORMALIZED CONTENT

You can use the [CONFLUENCE_PAGE title='The Alf editor' space='ALFP2024x'] to create an Alf body for an Opaque Action in an Activity or to edit the existing Alf body of an Opaque Action. The Alf code for an Opaque Action is stored as the body of the Opaque Action with the language *Alf.* Compiling this Alf code results in the creation of an executable Activity reflecting the behavior defined by the Alf code. This Activity is attached to the Opaque Behavior as a tagged value of the special *CompiledRepresentation* stereotype. (See also the discussion on [CONFLUENCE_PAGE title='The Alf compiler' space='ALFP2024x'].)

To create an Alf body for an Opaque Action

1. Select the Opaque Action in an Activity diagram (or in the Model Browser, though this usually not convenient) and open the Alf editor window (select Windows > Alf ), if it isn't already open.
2. Enter the Alf code for the Opaque Action and press **Save** to compile and save the code. The Alf code in an Opaque Action can comprise one or more Alf statements. The names of the Input and Output Pins of the Action may be used as local names in the Alf code. The local names for Input Pins have the values that are on the Pins when the Action executes. The local names for Output Pins are assignable with the values to be placed on those pins when the Action is done executing. (But see also [CONFLUENCE_PAGE title='Using Alf expressions in Opaque Actions' space='ALFP2024x'].)

To edit the Alf code for an Opaque Action

- Select the Opaque Action and open the Alf editor window (select Windows > Alf ), if it isn't already open. The existing Alf code will appear in the window. [ATTACHMENT filename='Using_Alf_In_Opaque_Action_Bodies-Editing.png']

When the *CompiledRepresentation* stereotype is applied to an Opaque Action by the Alf compiler, MagicDraw may, by default, show the Stereotype and its tagged values in the Opaque Action symbol (as shown below). If you do not want this depicted in your diagram (as in the diagram above), you can turn it off in the Opaque Action symbol properties.

###### [IMAGE alt='' src='']Opaque Action showing the CompiledRepresentation Sterotype

To not show Stereotypes or tagged values on Opaque Actions

1. Right click on the Opaque Action symbol and select Symbol Properties to open the Symbol Properties window.
2. Select Expert from the Apply Style menu at the top right (or All , if necessary).
3. Uncheck the box for the Show Tagged Values property (so it is false ).
4. Click on the Show Stereotypes property and select Do Not Display from the drop down menu.
5. Click on Close to close the Symbol Properties window.

[IMAGE alt='' src='']

To change the default for showing Stereotypes and tagged values on Opaque Actions

1. Select Options > Project from the main menu.
2. On the left, under Symbol styles > Default > Shapes , select Opaque Action .
3. On the right, change the relevant symbol properties, as above. If you want to update the properties on existing diagrams, continue. Otherwise skip to step 9.
4. Click on Apply . The Select Diagrams window will open.
5. Click on Select All (or select specific diagrams on which to apply the new defaults).
6. Click on OK . The Select Properties to Apply window will open.
7. Under Selected , choose Show Tagged Values , click on the < button, then choose Show Stereotypes , and click on the < button again.
8. Click on OK to close the Select Properties to Apply window.
9. Click on OK to close the Project Options window.

The Alf code for an Opaque Action can also be entered or edited directly in the **Body and Language** property for it in the Specification window for the Opaque Action. If you open the Edit Body and Language window, then the Alf code may be edited just as in the Alf editor window. However, instead of **Save** and **Revert** buttons, this window has **OK** and **Cancel** buttons, either of which will close it. If you press **OK**, then the text is saved, and, if it has no errors, compiled. If you press **Cancel**, the Alf text is *not* saved.

[IMAGE alt='' src='']

###### Editing Alf code in an Opaque Action body

To be recognized as Alf code, the **Body** of an Opaque Action must have the **Language** Alf. If your project was created using the Alf project template, then Alf will be the default language. Otherwise, select Alf from the **Language** menu (you may have to scroll upwards in the menu to find the selection for *Alf).*

To make Alf the default language for Opaque Actions

1. Select Options > Project .
2. On the left, under Default model properties , select Opaque Action .
3. Click on the Language field and then on the small + button on the right.
4. Enter Alf (spelled and capitalized in exactly that way) and click on OK .
5. Click on OK to close the options window.

If the **Name Display Mode** symbol property of an Opaque Expression is set to Body, then the Alf code for the Opaque Behavior can also be edited directly on an Activity diagram showing the Opaque Action. Since such editing does not use the Alf editor, no parsing or constraint checking happens while Alf code is being edited. The code is compiled once you finish editing it, and, if there are compilation errors, they will be recorded in an error annotation on the Opaque Action.

#### PANEL: Related pages

Related pages

- [CONFLUENCE_PAGE title='The Alf editor' space='ALFP2024x']
- [CONFLUENCE_PAGE title='The Alf compiler' space='ALFP2024x']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p>You can use the <ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="The Alf editor" /><ac:plain-text-link-body><![CDATA[Alf editor]]></ac:plain-text-link-body></ac:link> to create an Alf body for an Opaque Action in an Activity or to edit the existing Alf body of an Opaque Action. The Alf code for an Opaque Action is stored as the body of the Opaque Action with the language <em>Alf.</em> Compiling this Alf code results in the creation of an executable Activity reflecting the behavior defined by the Alf code. This Activity is attached to the Opaque Behavior as a tagged value of the special <em>CompiledRepresentation</em> stereotype. (See also the discussion on <ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="The Alf compiler" /><ac:plain-text-link-body><![CDATA[the Alf compiler]]></ac:plain-text-link-body></ac:link>.)</p><p><br /></p><p>To create an Alf body for an Opaque Action</p><hr /><ol><li>Select the Opaque Action in an Activity diagram (or in the Model Browser, though this usually not convenient) and open the Alf editor window (select <strong>Windows &gt; Alf</strong>), if it isn't already open.</li><li><p class="auto-cursor-target">Enter the Alf code for the Opaque Action and press <strong>Save</strong> to compile and save the code.</p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="4bf58a9d-5e5b-48f5-913a-a0ef1e5b86e5"><ac:rich-text-body><p>The Alf code in an Opaque Action can comprise one or more Alf statements. The names of the Input and Output Pins of the Action may be used as local names in the Alf code. The local names for Input Pins have the values that are on the Pins when the Action executes. The local names for Output Pins are assignable with the values to be placed on those pins when the Action is done executing. (But see also <ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="Using Alf expressions in Opaque Actions" /></ac:link>.)</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></li></ol><p><br /></p><p>To edit the Alf code for an Opaque Action</p><hr /><ul><li>Select the Opaque Action and open the Alf editor window (select <strong>Windows &gt; Alf</strong>), if it isn't already open. The existing Alf code will appear in the window.<br /><br /><ac:image><ri:attachment ri:filename="Using_Alf_In_Opaque_Action_Bodies-Editing.png"><ri:page ri:space-key="ALFP2024x" ri:content-title="Using Alf in Opaque Action bodies" /></ri:attachment></ac:image></li></ul><p class="auto-cursor-target"><br /></p><p><br /></p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="eddc40e8-a9ba-40d6-b2bb-fd021742110a"><ac:rich-text-body><p>When the <em>CompiledRepresentation</em> stereotype is applied to an Opaque Action by the Alf compiler, MagicDraw may, by default, show the Stereotype and its tagged values in the Opaque Action symbol (as shown below). If you do not want this depicted in your diagram (as in the diagram above), you can turn it off in the Opaque Action symbol properties.</p><h6 style="text-align: center;"><ac:image ac:align="center" ac:width="350"><ri:attachment ri:filename="Using_Alf_In_Opaque_Action_Bodies-Stereotyped.png"><ri:page ri:space-key="ALFP2024x" ri:content-title="Using Alf in Opaque Action bodies" /></ri:attachment></ac:image>Opaque Action showing the CompiledRepresentation Sterotype</h6><p><br /></p><p>To not show Stereotypes or tagged values on Opaque Actions</p><hr /><ol><li>Right click on the Opaque Action symbol and select <strong>Symbol Properties</strong> to open the Symbol Properties window.</li><li>Select <strong>Expert</strong> from the <strong>Apply Style</strong> menu at the top right (or <strong>All</strong>, if necessary).</li><li>Uncheck the box for the <strong>Show Tagged Values</strong> property (so it is <em>false</em>).</li><li>Click on the <strong>Show Stereotypes</strong> property and select <strong>Do Not Display</strong> from the drop down menu.</li><li>Click on <strong>Close</strong> to close the Symbol Properties window.</li></ol><p><ac:image><ri:attachment ri:filename="Using_Alf_In_Opaque_Action_Bodies-Symbol_Properties.png"><ri:page ri:space-key="ALFP2024x" ri:content-title="Using Alf in Opaque Action bodies" /></ri:attachment></ac:image></p><p><br /></p><p>To change the default for showing Stereotypes and tagged values on Opaque Actions</p><hr /><ol><li>Select <strong>Options &gt; Project</strong> from the main menu.</li><li>On the left, under <strong>Symbol styles &gt; Default &gt; Shapes</strong>, select <strong>Opaque Action</strong>.</li><li>On the right, change the relevant symbol properties, as above.<br /><em>If you want to update the properties on existing diagrams, continue. Otherwise skip to step 9.</em></li><li>Click on <strong>Apply</strong>. The Select Diagrams window will open.</li><li>Click on <strong>Select All</strong> (or select specific diagrams on which to apply the new defaults).</li><li>Click on <strong>OK</strong>. The Select Properties to Apply window will open.</li><li>Under <strong>Selected</strong>, choose <strong>Show Tagged Values</strong>, click on the <strong>&lt;</strong> button, then choose <strong>Show Stereotypes</strong>, and click on the <strong>&lt;</strong> button again.</li><li>Click on <strong>OK</strong> to close the Select Properties to Apply window.</li><li>Click on <strong>OK</strong> to close the Project Options window.<strong> </strong></li></ol></ac:rich-text-body></ac:structured-macro><p>The Alf code for an Opaque Action can also be entered or edited directly in the <strong>Body and Language</strong> property for it in the Specification window for the Opaque Action. If you open the Edit Body and Language window, then the Alf code may be edited just as in the Alf editor window. However, instead of <strong>Save</strong> and <strong>Revert</strong> buttons, this window has <strong>OK</strong> and <strong>Cancel</strong> buttons, either of which will close it. If you press <strong>OK</strong>, then the text is saved, and, if it has no errors, compiled. If you press <strong>Cancel</strong>, the Alf text is <em>not</em> saved.</p><p class="auto-cursor-target"><ac:image><ri:attachment ri:filename="Using_Alf_In_Opaque_Action_Bodies-Editing_Body.png"><ri:page ri:space-key="ALFP2024x" ri:content-title="Using Alf in Opaque Action bodies" /></ri:attachment></ac:image></p><h6 style="text-align: center;">Editing Alf code in an Opaque Action body</h6><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="0b619525-533c-4fbb-b06f-12bbc994bc97"><ac:rich-text-body><p>To be recognized as Alf code, the <strong>Body</strong> of an Opaque Action must have the <strong>Language</strong> Alf. If your project was created using the Alf project template, then Alf will be the default language. Otherwise, select Alf from the <strong>Language</strong> menu (you may have to scroll upwards in the menu to find the selection for <em>Alf).</em></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="45689fcf-a95f-49ee-aa41-ac5752bd67f8"><ac:rich-text-body><p>To make Alf the default language for Opaque Actions</p><hr /><ol><li>Select <strong>Options &gt; Project</strong>.</li><li>On the left, under <strong>Default model properties</strong>, select <strong>Opaque Action</strong>.</li><li>Click on the <strong>Language</strong> field and then on the small + button on the right.</li><li>Enter <em>Alf</em> (spelled and capitalized in exactly that way) and click on <strong>OK</strong>.</li><li>Click on <strong>OK</strong> to close the options window.</li></ol></ac:rich-text-body></ac:structured-macro><p>If the <strong>Name Display Mode</strong> symbol property of an Opaque Expression is set to Body, then the Alf code for the Opaque Behavior can also be edited directly on an Activity diagram showing the Opaque Action. Since such editing does not use the Alf editor, no parsing or constraint checking happens while Alf code is being edited. The code is compiled once you finish editing it, and, if there are compilation errors, they will be recorded in an error annotation on the Opaque Action.</p></ac:layout-cell><ac:layout-cell><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="6b833a85-fa3e-4022-96b4-4c62e45adc33"><ac:parameter ac:name="title">Related pages</ac:parameter><ac:rich-text-body><ul><li><ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="The Alf editor" /></ac:link></li><li><ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="The Alf compiler" /></ac:link></li></ul><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="d6bddf95-8815-4aac-8f9f-9e19e74a8ca4" /></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=137986099 space=ALFP2024x version=1 -->
## PAGE 00069: Using Alf in Opaque Behavior bodies

- page_id: `137986099`
- space_key: `ALFP2024x`
- source_url: https://docs.nomagic.com/spaces/ALFP2024x/pages/137986099/Using+Alf+in+Opaque+Behavior+bodies
- version_number: 1
- version_date: `2023-09-22T11:48:47.648+02:00`
- ancestors: Alf Plugin Documentation > User Guide > Working with Alf > Using Alf to define Behaviors
- labels: []

### NORMALIZED CONTENT

[CONFLUENCE_PAGE title='The Alf editor' space='ALFP2024x'] may be used to create an Alf body for a new Opaque Behavior or to edit the existing Alf body of an Opaque Behavior. The Alf code for an Opaque Behavior is stored as the body of the Opaque Behavior with the language *Alf.* Compiling this Alf code results in the creation of an executable Activity reflecting the behavior defined by the Alf code. This Activity is attached to the Opaque Behavior as a tagged value of the special *CompiledRepresentation* stereotype. (See also the discussion on [CONFLUENCE_PAGE title='The Alf compiler' space='ALFP2024x'].)

A Function Behavior is simply a special kind of Opaque Behavior that should produce a return value and have no side effects. The procedures below apply to Function Behaviors as well as Opaque Behaviors.

To create an Opaque Behavior with an Alf body

1. Create an Opaque Behavior in the Model Browser.
2. Add Parameters to the Opaque Behavior as desired. The easiest way to create an Opaque Behavior with Parameters is to type the complete signature for the Opaque Behavior with its name when you create it. For example, if you type "*Compute(x: Integer): Integer*" for the Opaque Behavior name, this results in an Opaque Behavior named "*Compute*" with an Integer input parameter named *x* and a return type of Integer. Parameter declarations may also be prefixed with *in, out* or *inout* to specify the Parameter direction.
3. Select the Opaque Behavior in the Model Browser and open the Alf editor window (select **Windows > Alf**), if it isn't already open.
4. Enter the Alf code for the Opaque Behavior and press **Save** to compile and save the code.

To edit an existing Alf body for an Opaque Behavior

- Select the Opaque Behavior in the Model Browser and open the Alf editor window (select Windows > Alf ), if it isn't already open. The existing Alf code will be displayed in the window. [ATTACHMENT filename='Using_Alf_To_Define_OpaqueBehaviors-Editing.png']

The Alf code for an Opaque Behavior can also be entered or edited directly in the **Body and Language** property in the Specification window for the Opaque Behavior. If you open the Edit Body and Language window, then the Alf code may be edited just as in the Alf editor window. However, instead of **Save** and **Revert** buttons, this window has **OK** and **Cancel** buttons, either of which will close it. If you press **OK**, then the text is saved, and, if it has no errors, compiled. If you press **Cancel**, the Alf text is *not* saved.

[IMAGE alt='' src='']

###### Editing Alf in an Opaque Behavior body

To be recognized as Alf code, the **Body** of an Opaque Behavior must have the **Language** Alf. If your project was created using the Alf project template, then Alf will be the default language. Otherwise, select Alf from the **Language** menu (you may have to scroll upwards in the menu to find the selection for *Alf*).

To make Alf the default language for Opaque Behaviors

1. Select Options > Project .
2. On the left, under Default model properties , select Opaque Behavior .
3. Click on the Language field and then on the small + button on the right.
4. Enter Alf (spelled and capitalized in exactly that way) and press OK .
5. Press OK to close the options window.

#### PANEL: Related pages

Related pages

- [CONFLUENCE_PAGE title='The Alf editor' space='ALFP2024x']
- [CONFLUENCE_PAGE title='The Alf compiler' space='ALFP2024x']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p><ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="The Alf editor" /></ac:link> may be used to create an Alf body for a new Opaque Behavior or to edit the existing Alf body of an Opaque Behavior. The Alf code for an Opaque Behavior is stored as the body of the Opaque Behavior with the language <em>Alf.</em> Compiling this Alf code results in the creation of an executable Activity reflecting the behavior defined by the Alf code. This Activity is attached to the Opaque Behavior as a tagged value of the special <em>CompiledRepresentation</em> stereotype. (See also the discussion on <ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="The Alf compiler" /><ac:plain-text-link-body><![CDATA[the Alf compiler]]></ac:plain-text-link-body></ac:link>.)</p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="34dba45a-c586-4359-9aca-cf939b873c83"><ac:rich-text-body><p>A Function Behavior is simply a special kind of Opaque Behavior that should produce a return value and have no side effects. The procedures below apply to Function Behaviors as well as Opaque Behaviors.</p></ac:rich-text-body></ac:structured-macro><p><br /></p><p>To create an Opaque Behavior with an Alf body</p><hr /><ol><li>Create an Opaque Behavior in the Model Browser.</li><li><p class="auto-cursor-target">Add Parameters to the Opaque Behavior as desired.</p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="88dc110d-9daf-454c-8d5d-c7b662744b2b"><ac:rich-text-body><p>The easiest way to create an Opaque Behavior with Parameters is to type the complete signature for the Opaque Behavior with its name when you create it. For example, if you type &quot;<em>Compute(x: Integer): Integer</em>&quot; for the Opaque Behavior name, this results in an Opaque Behavior named &quot;<em>Compute</em>&quot; with an Integer input parameter named <em>x</em> and a return type of Integer. Parameter declarations may also be prefixed with <em>in, out</em> or <em>inout</em> to specify the Parameter direction.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></li><li><p class="auto-cursor-target">Select the Opaque Behavior in the Model Browser and open the Alf editor window (select <strong>Windows &gt; Alf</strong>), if it isn't already open.</p></li><li><p class="auto-cursor-target">Enter the Alf code for the Opaque Behavior and press <strong>Save</strong> to compile and save the code.</p></li></ol><p><br /></p><p>To edit an existing Alf body for an Opaque Behavior</p><hr /><ul><li>Select the Opaque Behavior in the Model Browser and open the Alf editor window (select <strong>Windows &gt; Alf</strong>), if it isn't already open. The existing Alf code will be displayed in the window.<br /><br /><ac:image><ri:attachment ri:filename="Using_Alf_To_Define_OpaqueBehaviors-Editing.png"><ri:page ri:space-key="ALFP2024x" ri:content-title="Using Alf in Opaque Behavior bodies" /></ri:attachment></ac:image></li></ul><p>The Alf code for an Opaque Behavior can also be entered or edited directly in the <strong>Body and Language</strong> property in the Specification window for the Opaque Behavior. If you open the Edit Body and Language window, then the Alf code may be edited just as in the Alf editor window. However, instead of <strong>Save</strong> and <strong>Revert</strong> buttons, this window has <strong>OK</strong> and <strong>Cancel</strong> buttons, either of which will close it. If you press <strong>OK</strong>, then the text is saved, and, if it has no errors, compiled. If you press <strong>Cancel</strong>, the Alf text is <em>not</em> saved.</p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="Using_Alf_To_Define_OpaqueBehaviors-Editing_Body.png"><ri:page ri:space-key="ALFP2024x" ri:content-title="Using Alf in Opaque Behavior bodies" /></ri:attachment></ac:image></p><h6 style="text-align: center;">Editing Alf in an Opaque Behavior body</h6><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="98378a4c-9ab8-412c-a621-14fd4bbe2518"><ac:rich-text-body><p>To be recognized as Alf code, the <strong>Body</strong> of an Opaque Behavior must have the <strong>Language</strong> Alf. If your project was created using the Alf project template, then Alf will be the default language. Otherwise, select Alf from the <strong>Language</strong> menu (you may have to scroll upwards in the menu to find the selection for <em>Alf</em>).</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="11b9fa3c-bdbf-4a14-a927-0692307c0445"><ac:rich-text-body><p>To make Alf the default language for Opaque Behaviors</p><hr /><ol><li>Select <strong>Options &gt; Project</strong>.</li><li>On the left, under <strong>Default model properties</strong>, select <strong>Opaque Behavior</strong>.</li><li>Click on the <strong>Language</strong> field and then on the small + button on the right.</li><li>Enter <em>Alf</em> (spelled and capitalized in exactly that way) and press <strong>OK</strong>.</li><li>Press <strong>OK</strong> to close the options window.</li></ol></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell><ac:layout-cell><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="e213249c-683a-4747-8e47-0344f0201393"><ac:parameter ac:name="title">Related pages</ac:parameter><ac:rich-text-body><ul><li><ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="The Alf editor" /></ac:link></li><li><ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="The Alf compiler" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=137986117 space=ALFP2024x version=1 -->
## PAGE 00070: Using Alf in State Machine models

- page_id: `137986117`
- space_key: `ALFP2024x`
- source_url: https://docs.nomagic.com/spaces/ALFP2024x/pages/137986117/Using+Alf+in+State+Machine+models
- version_number: 1
- version_date: `2023-09-22T11:48:48.778+02:00`
- ancestors: Alf Plugin Documentation > User Guide > Working with Alf
- labels: []

### NORMALIZED CONTENT

The following kinds of elements in a State Machine model can have Alf bodies:

- The entry, do activity and exit Behaviors of a State.
- The guard Expression and effect Behavior of a Transition.

In general, to edit the Alf body of such an element in the Alf editor window, you select it either in the Model Browser or directly on its symbol if it appears on a State Machine diagram.

#### PANEL: Related pages

Related pages

- [CONFLUENCE_PAGE title='The Alf editor' space='ALFP2024x']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p>The following kinds of elements in a State Machine model can have Alf bodies:</p><ul><li>The entry, do activity and exit Behaviors of a State.</li><li>The guard Expression and effect Behavior of a Transition.</li></ul><p>In general, to edit the Alf body of such an element in the Alf editor window, you select it either in the Model Browser or directly on its symbol if it appears on a State Machine diagram.</p></ac:layout-cell><ac:layout-cell><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="d3f9c0c9-8298-4f8a-b8b7-92aeca29e0d5"><ac:parameter ac:name="title">Related pages</ac:parameter><ac:rich-text-body><ul><li><ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="The Alf editor" /></ac:link></li></ul><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="2e153442-a548-45f3-8b53-2d3777c651f3" /></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=137986096 space=ALFP2024x version=1 -->
## PAGE 00071: Using Alf to define Activities

- page_id: `137986096`
- space_key: `ALFP2024x`
- source_url: https://docs.nomagic.com/spaces/ALFP2024x/pages/137986096/Using+Alf+to+define+Activities
- version_number: 1
- version_date: `2023-09-22T11:48:47.361+02:00`
- ancestors: Alf Plugin Documentation > User Guide > Working with Alf > Using Alf to define Behaviors
- labels: []

### NORMALIZED CONTENT

You can use the [CONFLUENCE_PAGE title='The Alf editor' space='ALFP2024x'] to create an Alf body for a new Activity or to edit the existing Alf body of an Activity. Compiling the Alf body of an Activity results in the generation of Activity Nodes and Activity Edges within the Activity. Executing the Activity then has the behavior specified by the original Alf code. The Alf code itself is stored in a Comment owned by the Activity, which has the *TextualRepresentation* stereotype applied. Normally, you should not modify any of the contents of an Activity with an Alf body, other than by editing its Alf code using the Alf editor. (See also the discussion on [CONFLUENCE_PAGE title='The Alf compiler' space='ALFP2024x'].)

To create an Activity with an Alf body

1. Create an Activity in the Model Browser, but do not create an Activity diagram.
2. Add Parameters to the Activity as desired. The easiest way to create an Activity with Parameters is to type the complete signature for the Activity with its name when you create it. For example, if you type *Compute(x: Integer): Integer* for the Activity name, this results in an Activity named "*Compute*" with an *Integer* input parameter named *x* and a return type of *Integer.* Parameter declarations may also be prefixed with *in, out* or *inout* to specify the Parameter direction.
3. Select the new Activity in the Model Browser and open the Alf editor window (select **Windows > Alf**), if it isn't already open.
4. Enter the Alf code for the Activity and press **Save** to compile and save the code.

To edit an existing Alf body for an Activity

If an Activity has been defined using an Activity diagram, then it is not possible to enter Alf code for it. If you want to re-define an existing Activity using Alf, then, first, open the Activity diagram and delete all Activity Nodes on it other than Activity Parameter Nodes. Then you can proceed to enter Alf code for it as above.

#### PANEL: Related pages

Related pages

- [CONFLUENCE_PAGE title='The Alf editor' space='ALFP2024x']
- [CONFLUENCE_PAGE title='The Alf compiler' space='ALFP2024x']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p>You can use the <ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="The Alf editor" /><ac:plain-text-link-body><![CDATA[Alf editor]]></ac:plain-text-link-body></ac:link> to create an Alf body for a new Activity or to edit the existing Alf body of an Activity. Compiling the Alf body of an Activity results in the generation of Activity Nodes and Activity Edges within the Activity. Executing the Activity then has the behavior specified by the original Alf code. The Alf code itself is stored in a Comment owned by the Activity, which has the <em>TextualRepresentation</em> stereotype applied. Normally, you should not modify any of the contents of an Activity with an Alf body, other than by editing its Alf code using the Alf editor. (See also the discussion on <ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="The Alf compiler" /><ac:plain-text-link-body><![CDATA[the Alf compiler]]></ac:plain-text-link-body></ac:link>.)</p><p><br /></p><p>To create an Activity with an Alf body</p><hr /><ol><li>Create an Activity in the Model Browser, but do <em>not</em> create an Activity diagram.</li><li><p class="auto-cursor-target">Add Parameters to the Activity as desired.</p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="88dc110d-9daf-454c-8d5d-c7b662744b2b"><ac:rich-text-body><p>The easiest way to create an Activity with Parameters is to type the complete signature for the Activity with its name when you create it. For example, if you type <em>Compute(x: Integer): Integer</em> for the Activity name, this results in an Activity named &quot;<em>Compute</em>&quot; with an <em>Integer</em> input parameter named <em>x</em> and a return type of <em>Integer.</em> Parameter declarations may also be prefixed with <em>in, out</em> or <em>inout</em> to specify the Parameter direction.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></li><li><p class="auto-cursor-target">Select the new Activity in the Model Browser and open the Alf editor window (select <strong>Windows &gt; Alf</strong>), if it isn't already open.</p></li><li><p class="auto-cursor-target">Enter the Alf code for the Activity and press <strong>Save</strong> to compile and save the code.</p></li></ol><p><br /></p><p>To edit an existing Alf body for an Activity</p><hr /><ul><ul><li>Select the Activity in the Model Browser and open the Alf editor window (select <strong>Windows &gt; Alf</strong>), if it isn't already open. The existing Alf code will be displayed in the window.<br /><br /><ac:image ac:align="center"><ri:attachment ri:filename="Using_Alf_To_Define_Activities-Editing.png"><ri:page ri:space-key="ALFP2024x" ri:content-title="Using Alf to define Activities" /></ri:attachment></ac:image></li></ul></ul><p><br /></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="5d112dfa-726a-4cfd-9e08-7c220d74a40a"><ac:rich-text-body><p>If an Activity has been defined using an Activity diagram, then it is not possible to enter Alf code for it. If you want to re-define an existing Activity using Alf, then, first, open the Activity diagram and delete all Activity Nodes on it other than Activity Parameter Nodes. Then you can proceed to enter Alf code for it as above.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell><ac:layout-cell><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="a8b97560-041a-4937-b0a6-d3737576cba5"><ac:parameter ac:name="title">Related pages</ac:parameter><ac:rich-text-body><ul><li><ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="The Alf editor" /></ac:link></li><li><ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="The Alf compiler" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=137986095 space=ALFP2024x version=1 -->
## PAGE 00072: Using Alf to define Behaviors

- page_id: `137986095`
- space_key: `ALFP2024x`
- source_url: https://docs.nomagic.com/spaces/ALFP2024x/pages/137986095/Using+Alf+to+define+Behaviors
- version_number: 1
- version_date: `2023-09-22T11:48:47.212+02:00`
- ancestors: Alf Plugin Documentation > User Guide > Working with Alf
- labels: []

### NORMALIZED CONTENT

Two kinds of UML Behaviors may directly have Alf bodies: Activities and Opaque Behaviors. You can edit the Alf body of either kind of Behavior using the [CONFLUENCE_PAGE title='The Alf editor' space='ALFP2024x'] window. You can also edit the body of an Opaque Behavior directly through its Specification.

#### PANEL: Related pages

Related pages

- [CONFLUENCE_PAGE title='The Alf editor' space='ALFP2024x']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p>Two kinds of UML Behaviors may directly have Alf bodies: Activities and Opaque Behaviors. You can edit the Alf body of either kind of Behavior using the <ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="The Alf editor" /><ac:plain-text-link-body><![CDATA[Alf editor]]></ac:plain-text-link-body></ac:link> window. You can also edit the body of an Opaque Behavior directly through its Specification.</p></ac:layout-cell><ac:layout-cell><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="84c985ab-3b45-44f7-9694-49aa4e05bd62"><ac:parameter ac:name="title">Related pages</ac:parameter><ac:rich-text-body><ul><li><ac:link><ri:page ri:space-key="ALFP2024x" ri:content-title="The Alf editor" /></ac:link></li></ul><p style="margin-left: 30.0px;"><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="5222eb93-7cd5-4535-a41e-dc3e7b04f20d" /></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=137986086 space=ALFP2024x version=1 -->
## PAGE 00073: Working with Alf

- page_id: `137986086`
- space_key: `ALFP2024x`
- source_url: https://docs.nomagic.com/spaces/ALFP2024x/pages/137986086/Working+with+Alf
- version_number: 1
- version_date: `2023-09-22T11:48:46.733+02:00`
- ancestors: Alf Plugin Documentation > User Guide
- labels: []

### NORMALIZED CONTENT

Alf code may be used to define the behavior associated with various kinds of elements in a UML model. The Alf code associated with an element is known as the *Alf body* of that element. The *Alf editor* provides a consistent way to edit the Alf body of any element to which Alf code may be attached.

This section includes, first, a description of how to use the Alf editor in general, followed by additional information on how Alf is used with each kind of model element that may have an Alf body.

#### PANEL: Related Pages

Related Pages

true

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p>Alf code may be used to define the behavior associated with various kinds of elements in a UML model. The Alf code associated with an element is known as the <em>Alf body</em> of that element. The <em>Alf editor</em> provides a consistent way to edit the Alf body of any element to which Alf code may be attached.</p><p>This section includes, first, a description of how to use the Alf editor in general, followed by additional information on how Alf is used with each kind of model element that may have an Alf body.</p><p><br /></p></ac:layout-cell><ac:layout-cell><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="d4745788-3e59-4a27-8525-3a7fe1aea8d5"><ac:parameter ac:name="title">Related Pages</ac:parameter><ac:rich-text-body><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="b8dd877e-baff-40cc-b012-ff9e3009945e"><ac:parameter ac:name="all">true</ac:parameter></ac:structured-macro></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````
