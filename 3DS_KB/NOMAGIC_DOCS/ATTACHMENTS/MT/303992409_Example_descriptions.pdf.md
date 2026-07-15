# NOMAGIC ATTACHMENT: Example_descriptions.pdf

- attachment_id: `303992409`
- space_key: `MT`
- parent_page_id: `303992404`
- parent_page_title: (2026x Refresh1) Generating simulation files
- media_type: `application/pdf`
- reported_bytes: 97683
- download_url: https://docs.nomagic.com/download/attachments/303992404/Example_descriptions.pdf?version=1&modificationDate=1777364515960&api=v2
- payload_kind: `pdf-extracted`
- downloaded_sha256: `a1b01464c8edcc21d7a084b22b24a5b3f1495e9cb61979a814b48bbc8e46d20a`

## LAYOUT-PRESERVING PDF EXTRACTION

### PDF PAGE 1

```text
                        Example Cases of Modelica/Simulink Translator Plug-in

    Below, a list of example cases are provided to show the usability of the Modelica/Simulink translator
plug-in for SysML modeling and simulation of physical interactions signal flows. For each example, a
brief description of the example as well as the capabilities of the plug-in that the example attempts to
display.

    1. Humidifier System Example: Humidifying a Room
              a. The purpose of this example is to show how a SysML model of a humidifier system, one
                   that is trying to control the humidity in a room, can be created with state machines and
                   signal flows. It is important to note that the signal flows between system components
                   are unidirectional, and physical conservation laws do not apply in these applications
                   because the same signal can be sent to multiple receiving components. In some cases,
                   the state machines determine a timing or event trigger for when a signal flows between
                   components.
              b. Capabilities: Modeling & simulation of signal flows; translates SysML state machine
                   diagrams to state machines in Simulink’s Stateflow environment.

    2. Circuit Example: Voltage Source, Resistors, Inductor, Capacitor
              a. The purpose of this example is to show how a simple SysML model involving the flow of
                   electric charge (current) from a voltage source to resistors, an inductor, and a capacitor
                   can be translated into Modelica or Simulink/Simscape using the SysML extension plug-in
                   for signal flow and physical interaction. Though the documentation should lead to
                   generating Modelica and Simulink/Simscape files from the SysML model, the already-
                   translated Modelica and Simulink/Simscape files are provided in the package as
                   examples.
              b. Capabilities: Modeling & simulation of physical interactions; translates the SysML
                   plugin’s properties into flow and effort variables for Simulink’s Simscape toolbox
                   (electrical domain).

    3. Signal Processor Example: From Source to Sink
              a. The purpose of this example is to show a SysML model of a signal processor, where a
                   signal is sent from a function generator to be conditioned by an amplifier, frequency
                   filters, and a mixer.

                                                                  Figure 1: Signal processor

                   This example portrays the signal flows between system components. The signal flow is
                   unidirectional, and physical conservation laws do not apply in these applications
```

### PDF PAGE 2

```text
              because the same signal can be sent to multiple receiving components. In this model,
              the function generator is being amplified and then sent to parallel filters (one high-pass
              filter and one low-pass filter), until the mixer combines the filtered signals for the final
              signal processor output.
         b. Capabilities: Modeling & simulation of signal flows.

4. Hydraulics Example: Two Tanks & A Pipe
         a. The purpose of this example is to show how a simple SysML model involving the flow of
              a fluid between two tanks can be translated into Modelica or Simulink/Simscape using
              the SysML extension plug-in for signal flow and physical interaction. Though the
              documentation should lead to generating Modelica and Simulink/Simscape files from
              the SysML model, the already-translated Modelica and Simulink/Simscape files are
              provided in the package as examples.
         b. Capabilities: Modeling & simulation of physical interactions; translates the SysML
              plugin’s properties into flow and effort variables for Simulink’s Simscape toolbox
              (mechanical domain).
```


## EXACT ATTACHMENT METADATA

````json
{
  "id": "303992409",
  "type": "attachment",
  "status": "current",
  "title": "Example_descriptions.pdf",
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
    "when": "2026-04-28T10:21:55.960+02:00",
    "message": "",
    "number": 1,
    "minorEdit": false,
    "hidden": false,
    "_links": {
      "self": "https://docs.nomagic.com/rest/experimental/content/303992409/version/1"
    },
    "_expandable": {
      "content": "/rest/api/content/303992409"
    }
  },
  "position": -1,
  "container": {
    "id": "303992404",
    "type": "page",
    "status": "current",
    "title": "(2026x Refresh1) Generating simulation files",
    "position": 5,
    "extensions": {
      "position": 5
    },
    "_links": {
      "webui": "/spaces/MT/pages/303992404/2026x+Refresh1+Generating+simulation+files",
      "edit": "/pages/resumedraft.action?draftId=303992404",
      "tinyui": "/x/VI4eEg",
      "self": "https://docs.nomagic.com/rest/api/content/303992404"
    },
    "_expandable": {
      "container": "/rest/api/space/MT",
      "metadata": "",
      "operations": "",
      "children": "/rest/api/content/303992404/child",
      "restrictions": "/rest/api/content/303992404/restriction/byOperation",
      "history": "/rest/api/content/303992404/history",
      "ancestors": "",
      "body": "",
      "version": "",
      "descendants": "/rest/api/content/303992404/descendant",
      "space": "/rest/api/space/MT",
      "relevantViewRestrictions": "/rest/api/content/303992404/restriction/relevantViewRestrictions"
    }
  },
  "metadata": {
    "mediaType": "application/pdf"
  },
  "extensions": {
    "mediaType": "application/pdf",
    "fileSize": 97683,
    "comment": ""
  },
  "_links": {
    "download": "/download/attachments/303992404/Example_descriptions.pdf?version=1&modificationDate=1777364515960&api=v2",
    "webui": "/spaces/MT/pages/303992404/2026x+Refresh1+Generating+simulation+files?preview=%2F303992404%2F303992409%2FExample_descriptions.pdf",
    "self": "https://docs.nomagic.com/rest/api/content/303992409"
  },
  "_expandable": {
    "operations": "",
    "children": "/rest/api/content/303992409/child",
    "restrictions": "/rest/api/content/303992409/restriction/byOperation",
    "history": "/rest/api/content/303992409/history",
    "ancestors": "",
    "body": "",
    "descendants": "/rest/api/content/303992409/descendant",
    "space": "/rest/api/space/MT",
    "relevantViewRestrictions": "/rest/api/content/303992409/restriction/relevantViewRestrictions"
  }
}
````
