# NOMAGIC ATTACHMENT: System_Engineering_Architectural_Framework.pdf

- attachment_id: `55868977`
- space_key: `PLUGINS`
- parent_page_id: `55866305`
- parent_page_title: Cameo Requirements Modeler Plugin
- media_type: `application/pdf`
- reported_bytes: 650357
- download_url: https://docs.nomagic.com/download/attachments/55866305/System_Engineering_Architectural_Framework.pdf?version=1&modificationDate=1586337379507&api=v2
- payload_kind: `pdf-extracted`
- downloaded_sha256: `c5726bb1c9801db7bfaf80dbb9d6a806e5ee1ea0d194f1fae7120634f4afb7d3`

## LAYOUT-PRESERVING PDF EXTRACTION

### PDF PAGE 1

```text
Architectural Frameworks for SysML

Dr. Aurelijus Morkevicius
Solution Architect
aurelijus.morkevicius@nomagic.com
```

### PDF PAGE 2

```text
Contents

   Introduction............................................................................................................................. 3
   Magic Pattern ......................................................................................................................... 3
   Conclusion .............................................................................................................................. 5
   About the Author..................................................................................................................... 6
   Contacts ................................................................................................................................. 6

                                                                                   © 2014 No Magic , Inc. 2
```

### PDF PAGE 3

```text
Introduction

SysML defines neither an architecture framework nor a method. This opens discussions of how
to structure the model, what views to build, which artifacts to deliver and in what sequence.
Every company deals with the same issue a bit differently. Some use defense architecture
frameworks like DoDAF, NAF, MODAF, others use FAS; however, saying there is no need for
an architectural framework just doesn’t work. You always end-up using an architectural
framework whether you want one or not, or whether you intend to or not.
When analyzing available alternatives, the defense frameworks are considered to be
heavyweight, although they do not require using a full set of views, and FAS is not as well-
known and or used yet. Option number three is to define your own custom architectural
framework (AF). This is what usually happens in reality. There are so many domains in system
engineering; it is no wonder the approach for designing different types of systems differs.

Magic Pattern

In this paper, author, being a part of such framework developments in various organizations,
defined a pattern (Magic Pattern) for a custom AF based on SysML (see figure 1).

                                                 Figure 1 Magic Pattern
One can argue that instead of derivation he would use refinement. So go ahead, it is not against
SysML. SysML provides a set of elements; however, it is up to you to interpret their usage in
most of cases.
An example of the pattern shown in figure 1 could be a framework consisting of three levels of
abstraction (see figure 2):

                                                                                   © 2014 No Magic , Inc. 3
```

### PDF PAGE 4

```text
1. Conceptual - defines the core concepts of the system context and their interactions. The
undoubted benefit of views created in the conceptual model is sharing core concepts of the
system context between stakeholders.
2. Functional - defines functional analysis from the behavioral perspective, where functions
instead of structural units are emphasized. Do not mix this up with the Logical architecture. They
are different; however, explaining the difference requires another paper.
3. Physical - defines equipment, their physical interfaces and parameters. The physical model is
usually a subject for simulation and model-based testing.

                                         Figure 2 Example of Magic Pattern
Figure 2 shows a single possible instance of Magic Pattern shown in figure 1. Each of the
architecture models and relationships among them can be represented in SysML using a
different set of elements and views (diagrams, matrices, tables, etc.). E.g. functional
requirements can be depicted in SysML Requirements Diagram or SysML Requirements Table;
conceptual architecture can be depicted in IBD, Use Case diagram, Sequence Diagram etc. See
the figure 3 for our recommendations.

                                                                                   © 2014 No Magic , Inc. 4
```

### PDF PAGE 5

```text
                        Figure 3 Architectural Models to SysML Diagrams Mapping
As you can see in the figure 3, the SysML Package Diagram is marked in Grey. This is because
it can be created in any architecture model or can be skipped. The purpose of this diagram is to
organize the model, thus generally it is created at the beginning and updated afterwards.
The SysML Use Case Diagram is sometimes used to define User Needs. There is a concept of
Business Use Case used for such purpose.
Relationships between architecture models are derived from the relationships between model
elements, e.g. functional requirement derivation from some user need implies the dependency
of the functional requirements model from the user needs model.

Conclusion

Summarizing, it can be clearly seen that there are so many variations of architectures, models,
diagrams and combinations of them (note that we have not touched the process yet), that
crafting a custom architectural framework is not an easy task.

                                                                                   © 2014 No Magic , Inc. 5
```

### PDF PAGE 6

```text
About the Author

                      Dr. Aurelijus Morkevicius
                      Solution Architect
                      aurelijus.morkevicius@nomagic.com

                      Aurelijus is OMG Certified UML, Systems Modeling and BPM Professional. He
                      has been with No Magic, Inc. since 2008. He started as a System Analyst for
                      Enterprise Architecture solutions such as UPDM plugin for MagicDraw. In 2009
                      he moved to Product Manager position for the Cameo Enterprise Architecture
product. By making it one of the most successful products on the market, he decided to work
more on the customer side. Currently he is a solution architect for model-based systems
engineering (mostly based on SysML, UML, and UPDM) and defense architectures (DoDAF,
MODAF, NAF). He also participates actively in various modeling standards creation activities.
He is a chairman and one of the leading architects for the current OMG UPDM standard
development group. On the other side He is actively involved in educational activities. He teach
Enterprise Architecture course in Kaunas University of Technology. He has gained PhD in
Informatics Engineering at the same university in 2013.

Contacts

No Magic Europe, UAB        No Magic, Inc.             No Magic Asia

Savanoriu ave. 363, Kaunas  One Allen Center, 700      719 KPN Tower, 22nd floor,
LT - 49425, Lithuania       Central Expressway South,  Rama IX Road, Bangkapi, Huaykwang,
Phone:+370-37-324032,       Suite 110 Allen, TX 75013  Bangkok 10310, Thailand
Fax:+370-37-320670          Phone: +1-214-291-9100,    Phone: +66 2717 0250
E-mail: sales@nomagic.com   Fax: +1-214-291-9099       Fax: +66 2717 0251
                            E-mail: sales@nomagic.com  E-mail: nomagicth@nomagicasia.com

                                            © 2014 No Magic , Inc. 6
```


## EXACT ATTACHMENT METADATA

````json
{
  "id": "55868977",
  "type": "attachment",
  "status": "current",
  "title": "System_Engineering_Architectural_Framework.pdf",
  "version": {
    "by": {
      "type": "known",
      "username": "agnpal",
      "userKey": "ff80808151426f0e0151af8b0d360002",
      "profilePicture": {
        "path": "/download/attachments/6598412/user-avatar",
        "width": 48,
        "height": 48,
        "isDefault": false
      },
      "displayName": "Agne P.",
      "_links": {
        "self": "https://docs.nomagic.com/rest/api/user?key=ff80808151426f0e0151af8b0d360002"
      },
      "_expandable": {
        "status": ""
      }
    },
    "when": "2020-04-08T11:16:19.507+02:00",
    "message": "",
    "number": 1,
    "minorEdit": true,
    "hidden": false,
    "_links": {
      "self": "https://docs.nomagic.com/rest/experimental/content/55868977/version/1"
    },
    "_expandable": {
      "content": "/rest/api/content/55868977"
    }
  },
  "position": -1,
  "container": {
    "id": "55866305",
    "type": "page",
    "status": "current",
    "title": "Cameo Requirements Modeler Plugin",
    "position": -1,
    "extensions": {
      "position": "none"
    },
    "_links": {
      "webui": "/spaces/PLUGINS/pages/55866305/Cameo+Requirements+Modeler+Plugin",
      "edit": "/pages/resumedraft.action?draftId=55866305&draftShareId=73325de7-2076-4a2f-90ca-8f642bd6a0de",
      "tinyui": "/x/wXNUAw",
      "self": "https://docs.nomagic.com/rest/api/content/55866305"
    },
    "_expandable": {
      "container": "/rest/api/space/PLUGINS",
      "metadata": "",
      "operations": "",
      "children": "/rest/api/content/55866305/child",
      "restrictions": "/rest/api/content/55866305/restriction/byOperation",
      "history": "/rest/api/content/55866305/history",
      "ancestors": "",
      "body": "",
      "version": "",
      "descendants": "/rest/api/content/55866305/descendant",
      "space": "/rest/api/space/PLUGINS",
      "relevantViewRestrictions": "/rest/api/content/55866305/restriction/relevantViewRestrictions"
    }
  },
  "metadata": {
    "mediaType": "application/pdf"
  },
  "extensions": {
    "mediaType": "application/pdf",
    "fileSize": 650357,
    "comment": ""
  },
  "_links": {
    "download": "/download/attachments/55866305/System_Engineering_Architectural_Framework.pdf?version=1&modificationDate=1586337379507&api=v2",
    "webui": "/spaces/PLUGINS/pages/55866305/Cameo+Requirements+Modeler+Plugin?preview=%2F55866305%2F55868977%2FSystem_Engineering_Architectural_Framework.pdf",
    "self": "https://docs.nomagic.com/rest/api/content/55868977"
  },
  "_expandable": {
    "operations": "",
    "children": "/rest/api/content/55868977/child",
    "restrictions": "/rest/api/content/55868977/restriction/byOperation",
    "history": "/rest/api/content/55868977/history",
    "ancestors": "",
    "body": "",
    "descendants": "/rest/api/content/55868977/descendant",
    "space": "/rest/api/space/PLUGINS",
    "relevantViewRestrictions": "/rest/api/content/55868977/restriction/relevantViewRestrictions"
  }
}
````
