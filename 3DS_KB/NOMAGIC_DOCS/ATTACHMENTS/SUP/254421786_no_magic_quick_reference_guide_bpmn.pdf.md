# NOMAGIC ATTACHMENT: no_magic_quick_reference_guide_bpmn.pdf

- attachment_id: `254421786`
- space_key: `SUP`
- parent_page_id: `254421775`
- parent_page_title: Quick Reference Guides
- media_type: `application/pdf`
- reported_bytes: 5779275
- download_url: https://docs.nomagic.com/download/attachments/254421775/no_magic_quick_reference_guide_bpmn.pdf?version=1&modificationDate=1757674468566&api=v2
- payload_kind: `pdf-extracted`
- downloaded_sha256: `dd255b30b52f392c98dff97ad9ecab5224e2928f74ee79eb531535b4f8872b18`

## LAYOUT-PRESERVING PDF EXTRACTION

### PDF PAGE 1

```text
                                                                                                       Download This Quick Reference Guide At www.nomagic.com/products/cameo-business-modeler.html

                            Conversation Diagram:                                                                                                              Quick Reference Guide                   EVENTS                                                 activities

A conversation defines a set of logically related   A Call conversation is a wrapper for a globally    A Conversation Link                                AT A GLANCE                                      start  intermediate END                                 A Task is an atomic activity within a process
message exchanges. When marked with a               defined Conversation or Sub-conversation.          connects Conversations                                                                                                                                      flow. A Task is used when the work in a
+ symbol it indicates a Sub-conversation, a         A call to a Sub-conversation is marked with        and Participants.                                   The Truth is in the Models®                 Top-Level                                                   process cannot be broken down into finer
compound conversation element.                      a + symbol.                                                                                                                                             Event Sub-Process                                      levels of detail.
                                                                                                                                                                                                               Interrupting
                                                                                                                                                          Collaboration Diagram:                                    Event Sub-Processing
                                                                                                                                                                                                                        Non-interrupting
                                                                                                                                                                                                                             Catching                                               A Transaction is a specialized type of
                                                                                                                                                                                                                                   Boundary Interrupting                            sub-process whose special behavior is
                                                                                                                                                                                                                                         Boundar y                                  controlled through a transaction protocol.
                                                                                                                                                                                                                                            Non-Interrupting
                                                                                                                                                                                                                                                  Throwing

                                                                                                                                                                                                       None: Untyped events,                                                        An Event SubProcess may occur many
                                                                                                                                                                                                       indicate start point, state of                                               times. Unlike the standard SubProcess that
                                                                                                                                                                                                       changes or final states                                                      uses the flow of the parent process as a
                                                                                                                                                                                                                                                                                    trigger, it has a Start Event as a trigger.
                                                                                                                                                                                                       Message: Receiving and
                                                                                                                                                                                                       sending messages                                                             A Call Activity identifies a point in a
                                                                                                                                                                                                                                                                                    process where a global process is used.
                                                                                                                                                                                                       Timer: Cyclic timer events,                                                  The Call Activity acts as a ‘wrapper’ for
                                                                                                                                                                                                       points in time, time spans,                                                  the invocation of the global process within
                                                                                                                                                                                                       or timeouts                                                                  the execution.

                                                                                                                                                                                                       Escalation: Escalating to a                            Activity Markers – Markers indicate Task Types – Types specify the
                                                                                                                                                                                                       higher level of responsibility
                                                                                                                                                                                                                                                              executive behavior of activities.  nature of the action to be preformed.
                                                                                                                                                                                                       Conditional: Reacting
                            Choreography Diagram:                                                                                                         Process Diagram:                             to changed business                                    SUB-PROCESS MARKER                       SEND TASK
                                                                                                                                                                                                       conditions or integrating                              LOOP MARKER                              RECEIVE TASK
                                                                                                                                                                                                       business rules                                         PARALLEL MI MARKER                       USER TASK
                                                                                                                                                                                                                                                              SEQUENTIAL MI MARKER                     MANUAL TASK
                                                                                                                                                                                                       Link: Off-page connectors.                             AD HOC MARKER                            BUSINESS RULE TASK
                                                                                                                                                                                                       Two corresponding                                      COMPENSATION MARKER                      SERVICE TASK
                                                                                                                                                                                                       link events equal a                                                                             SCRIPT TASK
                                                                                                       Multiple Participants                                                                           sequence flow
                                                                                                       Marker denotes a set                                                                                                                                   connecting objects
                                                                                                       of Participants of the                                                                          Error: Catching or throwing
                                                                                                       same kind.                                                                                      named errors                                                               Sequence Flow

A Choreography Task         A Sub-Choreography contains  A Call Choreography is a wrapper for          A Message decorator                                                                             Cancel: Reacting to                                                                       Data Association
represents an Interaction   a refined choreography with  a globally defined Choreography Task          depicting the content                                                                           cancelled transactions or
(Message Exchange) between  several Interactions.        or Sub-Choreography. A call to                of the message. It can                                                                          triggering cancellations
two Participants.                                        a Sub-Choreography is marked with             only be attached to
                                                         a + symbol.                                   Choreography Tasks.                                                                             Compensation: Handling or
                                                                                                                                                                                                       triggering compensation
                                                                                                                                                                                                                                                                                                 Message Flow
                                                                                                                                                                                                       Signal: Signaling across
                                                                                                                                                                                                       different processes. A signal                                   Default Sequence Flow
                                                                                                                                                                                                       thrown can be caught
                                                                                                                                                                                                       multiple times                                         swimlanes

                                                                                                                                                                                                       Multiple: Catching one out
                                                                                                                                                                                                       of a set of events. Throwing
                                                                                                                                                                                                       all events defined

                                                                                                                                                                                                       Parallel Multiple:
                                                                                                                                                                                                       Catching all out of a set
                                                                                                                                                                                                       of parallel events

                                                                                                                                                                                                       Terminate: Triggering the
                                                                                                                                                                                                       immediate termination of
                                                                                                                                                                                                       a process

                                                                                                                                                                                                                     data objects

                                                                                                                                                                                                                                                              Pools (Participants) and Lanes     Pool
                                                                                                                                                                                                                                                              represent responsibilities for
                                                                                                                                                                                                                                                              activities in a process. A pool or aPool
                                                                                                                                                                                                                                                              lane can be an organization, a role,
Exclusive Gateway – Split – routes sequence             GATEWAYS:                                      Complex Gateway – Gateways that represent                    The Truth is in the Models®                                                               or a system. Lanes subdivide pools
flow to a precise outgoing branch.                                                                     actions not captured by other gateways. Can be                                                                                                         or other lanes hierarchically.
Merge – waits for one incoming branch to            Parallel Gateway – When splitting sequence flow    complex, merging, or branching actions/behaviors.                      www.nomagic.com
finish before triggering an outgoing flow.          – outgoing branches are initiated simultaneously.                                                                                                                                                                                                      The order of message
                                                    When merging parallel branches – the gateway       Exclusive Event – Event-based Gateway                          Corporate Headquarters                                                                                                               exchanges can be specified
Event-based Gateway – Must be followed by a         waits for all incoming branches to finish before   (Instantiate) – Each occurrence of a subsequent                               One Allen Center                                                                                                      by combining message flow
catching event(s) or a receiving task(s). Sequence  triggering outgoing flow.                          event starts a new process instant.                                                                                                                                                                 and sequence flow.
flow is sent to the subsequent event/task which                                                                                                           700 Central Expressway South, Suite 110
happens first.                                      Inclusive Gateway – One or more branches           Parallel Event – Event-based Gateway                                       Allen, Texas 75013                                                          Message Flow symbolizes information flow
                                                    are activated when splitting. All active incoming  (Instantiate) – The occurrence of all subsequent                                                                                                       across organizational boundaries. Message
                                                    branches must complete before merging.             events begins a new process instance.                                    Phone: 214.291.9100                                                           flow can be attached to pools, activities, or
                                                                                                                                                                                   Fax: 214.291.9099                                                          message events. The Message Flow can be
                                                                                                                                                                                                                                                              decorated with an envelope depicting the
                                                                                                                                                                        E-mail: sales@nomagic.com                                                             content of the message.
```

### PDF PAGE 2

```text
                 Organization structure definition:                                                       Download This Quick Reference Guide at www.nomagic.com/products/cameo-business-modeler.html                                                                                              Model analysis:

• Helps to understand business domain concepts                                                                                                             Quick Reference Guide                                                                                                  • Multiple ways to visualize related elements
• C an be reused in business processes
• E nables traceability between process and data views                                                                      AT A GLANCE                                                                                                                                           • Powerful search of related elements

                                                                                                                                                        The Truth is in the Models®                                                                                             #  Name            Documentation

                                                                                                                                                 RETRIEVE REQUIRED PARTS:                                                                                                                          The Sales Department Manager is responsible for the development and performance of all
                                                                                                                                                                                                                                                                                                   sales activities. He staffs and directs a sales team, establishes plan and strategies to expand
                                                                                                                                                                                                                                                                                                   the customer base, and contributes to the development of training and educational programs
                                                                                                                                                                                                                                                                                                   for the sales force.

                                                                                                                                                                                                                                                                                1  Sales Director  Sales Manager Responsibilities
                                                                                                                                                                                                                                                                                                          • Develops a business plan and sales strategy

                                                                                                                                                                                                                                                                                                   • Maintains accurate records of all pricing, sales and activity reports

                                                                                                                                                                                                                                                                                                   • Provides feedback to management regarding performance

                                                                                                                                                                                                                                                                                                   • Assists sales in the preparation of proposals

                                                                                                                                                                                                                                                                                                   • Creates and conducts proposal presentations

                                                                                                                                                                                                                                                                                                   • Responsible for the performance and development of the sales force

                                                                                       #  Name            Documentation                                                                                                                                                                                              The Production Manager coordinates the resources and activities required to produce ordered
                                                                                                                                                                                                                                                                                                                     manufacturing items. This person is responsible for staffing and directing a manufacturing team,
                                                                                                          The Sales Department Manager is responsible for the development and performance of all                                                                                                                     establishes plans and strategies to improve manufacturing processes, and contributes to the
                                                                                                          sales activities. He staffs and directs a sales team, establishes plan and strategies to expand                                                                                                            development of training and educational programs for workers.
                                                                                                          the customer base, and contributes to the development of training and educational programs
                                                                                                          for the sales force.                                                                                                                                                  2 Production Director Production Manager Responsibilities
                                                                                                                                                                                                                                                                                                                            • Responsible for fulfilling all orders, plans and schedules for each worker on a timely basis
                                                                                                                                                                                                                                                                                                                            • Maintains accurate records of all manufacturing, resources and raw material reports
                                                                                                                                                                                                                                                                                                                            • Provides feedback to management regarding staff performance
                                                                                                                                                                                                                                                                                                                            • Plans and schedules tasks for each worker
                                                                                                                                                                                                                                                                                                                            • Responsible for the performance, safety and career development of workers

                                                                                       1  Sales Director  Sales Manager Responsibilities
                                                                                                                 • Develops a business plan and sales strategy

                                                                                                          • Maintains accurate records of all pricing, sales and activity reports

                                                                                                          • Provides feedback to management regarding performance

                                                                                                          • Assists sales in the preparation of proposals

                                                                                                          • Creates and conducts proposal presentations

                                                                                                          • Responsible for the performance and development of the sales force

                                                                                                                            The Production Manager coordinates the resources and activities required to produce ordered
                                                                                                                            manufacturing items. This person is responsible for staffing and directing a manufacturing team,
                                                                                                                            establishes plans and strategies to improve manufacturing processes, and contributes to the
                                                                                                                            development of training and educational programs for workers.

                                                                                       2 Production Director Production Manager Responsibilities
                                                                                                                                   • Responsible for fulfilling all orders, plans and schedules for each worker on a timely basis
                                                                                                                                   • Maintains accurate records of all manufacturing, resources and raw material reports
                                                                                                                                   • Provides feedback to management regarding staff performance
                                                                                                                                   • Plans and schedules tasks for each worker
                                                                                                                                   • Responsible for the performance, safety and career development of workers

Business Process model using BPMN 2.0:

• Represents flow of the process                                                          • Can be drawn at different abstraction levels

                                                                                                                                                                                                                                           Take business process beyond just BPMN.

                                                                                                                                                                                                                                   www.nomagic.com/products/cameo-enterprise-architecture.html

                                                                                                                                                                                                                                                                                                         Business data model:

                                                                                                                                                                                                                                                                                   • H elps to understand business domain concepts
                                                                                                                                                                                                                                                                                   • Can be reused in business processes
                                                                                                                                                                                                                                                                                   • Enables traceability between process and data views

                                                                                                                                                                                                                                   The Truth is in the Models®
                                                                                                                                                                                                                                             www.nomagic.com

Why modeling?                                                                          Leverage the Most Standards-Compliant                                                                                                                   Corporate Headquarters
                                                                                       Business Modeling Solution With No
• M odeling facilitates structural thinking                                           Magic’s Cameo Business Modeler:                                                                                                                                        One Allen Center
• Multi-level models simplify complexity                                                                                                                                                                                          700 Central Expressway South, Suite 110
• A business model is non-ambiguous                                                   • An intuitive and powerful modeling solution
• Allows for integration of various model types                                                                                                                                                                                                           Allen, Texas 75013
• Standard notation is understood by business                                                                                                                                                                                                           Phone: 214.291.9100

  executives, business analysts, and IT staff                                                                                                                                                                                                               Fax: 214.291.9099
•	View the BPMN Quick Reference Guide at                                                                                                                                                                                                        E-mail: sales@nomagic.com

   www.nomagic.com/products/cameo-business-modeler.html                                • Define business processes using the Business Process
                                                                                         Modeling and Notation (BPMN 2.0) standard
Copyright © 2012 No Magic, Inc. MagicDraw is a registered trademark of No Magic, Inc.
                                                                                       • Capture business vocabulary and business                                                             Simulating your business process and executing
                                                                                         data in business process descriptions                                                                   your business rules with complete validation.

                                                                                       • Relate your organization structure to the processes                                      www.nomagic.com/products/magicdraw-addons/cameo-simulation-toolkit.html

                                                                                       • Is the BPMN 2.0 reference model for the OMG
```


## EXACT ATTACHMENT METADATA

````json
{
  "id": "254421786",
  "type": "attachment",
  "status": "current",
  "title": "no_magic_quick_reference_guide_bpmn.pdf",
  "version": {
    "by": {
      "type": "known",
      "username": "ingabe",
      "userKey": "ff80808151f3008c0152c05ba1a40003",
      "profilePicture": {
        "path": "/download/attachments/7415957/user-avatar",
        "width": 48,
        "height": 48,
        "isDefault": false
      },
      "displayName": "Inga A.",
      "_links": {
        "self": "https://docs.nomagic.com/rest/api/user?key=ff80808151f3008c0152c05ba1a40003"
      },
      "_expandable": {
        "status": ""
      }
    },
    "when": "2025-09-12T12:54:28.566+02:00",
    "message": "",
    "number": 1,
    "minorEdit": false,
    "hidden": false,
    "_links": {
      "self": "https://docs.nomagic.com/rest/experimental/content/254421786/version/1"
    },
    "_expandable": {
      "content": "/rest/api/content/254421786"
    }
  },
  "position": -1,
  "container": {
    "id": "254421775",
    "type": "page",
    "status": "current",
    "title": "Quick Reference Guides",
    "position": 1,
    "extensions": {
      "position": 1
    },
    "_links": {
      "webui": "/spaces/SUP/pages/254421775/Quick+Reference+Guides",
      "edit": "/pages/resumedraft.action?draftId=254421775",
      "tinyui": "/x/DysqDw",
      "self": "https://docs.nomagic.com/rest/api/content/254421775"
    },
    "_expandable": {
      "container": "/rest/api/space/SUP",
      "metadata": "",
      "operations": "",
      "children": "/rest/api/content/254421775/child",
      "restrictions": "/rest/api/content/254421775/restriction/byOperation",
      "history": "/rest/api/content/254421775/history",
      "ancestors": "",
      "body": "",
      "version": "",
      "descendants": "/rest/api/content/254421775/descendant",
      "space": "/rest/api/space/SUP",
      "relevantViewRestrictions": "/rest/api/content/254421775/restriction/relevantViewRestrictions"
    }
  },
  "metadata": {
    "mediaType": "application/pdf"
  },
  "extensions": {
    "mediaType": "application/pdf",
    "fileSize": 5779275,
    "comment": ""
  },
  "_links": {
    "download": "/download/attachments/254421775/no_magic_quick_reference_guide_bpmn.pdf?version=1&modificationDate=1757674468566&api=v2",
    "webui": "/spaces/SUP/pages/254421775/Quick+Reference+Guides?preview=%2F254421775%2F254421786%2Fno_magic_quick_reference_guide_bpmn.pdf",
    "self": "https://docs.nomagic.com/rest/api/content/254421786"
  },
  "_expandable": {
    "operations": "",
    "children": "/rest/api/content/254421786/child",
    "restrictions": "/rest/api/content/254421786/restriction/byOperation",
    "history": "/rest/api/content/254421786/history",
    "ancestors": "",
    "body": "",
    "descendants": "/rest/api/content/254421786/descendant",
    "space": "/rest/api/space/SUP",
    "relevantViewRestrictions": "/rest/api/content/254421786/restriction/relevantViewRestrictions"
  }
}
````
