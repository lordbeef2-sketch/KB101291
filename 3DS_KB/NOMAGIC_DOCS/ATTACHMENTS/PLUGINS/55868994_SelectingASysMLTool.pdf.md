# NOMAGIC ATTACHMENT: SelectingASysMLTool.pdf

- attachment_id: `55868994`
- space_key: `PLUGINS`
- parent_page_id: `55866307`
- parent_page_title: SysML Plugin
- media_type: `application/pdf`
- reported_bytes: 115494
- download_url: https://docs.nomagic.com/download/attachments/55866307/SelectingASysMLTool.pdf?version=1&modificationDate=1586338481912&api=v2
- payload_kind: `pdf-extracted`
- downloaded_sha256: `9cacb1eb3d0710827bb6715d77f33690568bac2862843f8e13587cbd69825129`

## LAYOUT-PRESERVING PDF EXTRACTION

### PDF PAGE 1

```text
SANDIA REPORT

SAND2010-7098
Unlimited Release
February 2011

Process for Selecting Engineering Tools
– Applied to Selecting a SysML Tool

Kent de Jong, Mark J. De Spain, Marjorie E. Hernandez, Debbie S. Post, and Jeffrey L. Taylor

Prepared by
Sandia National Laboratories
Albuquerque, New Mexico 87185 and Livermore, California 94550

Sandia National Laboratories is a multi-program laboratory managed and operated by Sandia Corporation,
a wholly owned subsidiary of Lockheed Martin Corporation, for the U.S. Department of Energy's
National Nuclear Security Administration under contract DE-AC04-94AL85000.
Approved for public release; further dissemination unlimited.
```

### PDF PAGE 2

```text
Issued by Sandia National Laboratories, operated for the United States Department of Energy
by Sandia Corporation.

NOTICE: This report was prepared as an account of work sponsored by an agency of the
United States Government. Neither the United States Government, nor any agency thereof,
nor any of their employees, nor any of their contractors, subcontractors, or their employees,
make any warranty, express or implied, or assume any legal liability or responsibility for the
accuracy, completeness, or usefulness of any information, apparatus, product, or process
disclosed, or represent that its use would not infringe privately owned rights. Reference herein
to any specific commercial product, process, or service by trade name, trademark,
manufacturer, or otherwise, does not necessarily constitute or imply its endorsement,
recommendation, or favoring by the United States Government, any agency thereof, or any of
their contractors or subcontractors. The views and opinions expressed herein do not
necessarily state or reflect those of the United States Government, any agency thereof, or any
of their contractors.

Printed in the United States of America. This report has been reproduced directly from the best
available copy.

Available to DOE and DOE contractors from
      U.S. Department of Energy
      Office of Scientific and Technical Information
      P.O. Box 62
      Oak Ridge, TN 37831

Telephone:     (865) 576-8401

Facsimile:     (865) 576-5728

E-Mail:        reports@adonis.osti.gov

Online ordering: http://www.osti.gov/bridge

Available to the public from
      U.S. Department of Commerce
      National Technical Information Service
      5285 Port Royal Rd.
      Springfield, VA 22161

Telephone:     (800) 553-6847
Facsimile:     (703) 605-6900
E-Mail:        orders@ntis.fedworld.gov
Online order:  http://www.ntis.gov/help/ordermethods.asp?loc=7-4-0#online

                               2
```

### PDF PAGE 3

```text
                                         SAND2010-7098
                                         Unlimited Release

                                           February 2011

 Process for Selecting Engineering Tools –
      Applied to Selecting a SysML Tool

                     Kent de Jong, Marjorie Hernandez and Jeff Taylor
                        Information Services for Product Information
                                  Sandia National Laboratories
                                           P.O. Box 5800
                         Albuquerque, New Mexico 87185-MS0626
                                           Mark De Spain
                         Advanced and Exploratory Systems (A&E)
                                  Sandia National Laboratories
                                           P.O. Box 5800
                         Albuquerque, New Mexico 87185-MS0340
                                            Debbie Post
                               Program Analysis and Integration
                                  Sandia National Laboratories
                                            P.O. Box 969
                             Livermore, California 94551-MS9154

                                              Abstract

Process for Selecting Engineering Tools outlines the process and tools used to select a
SysML (Systems Modeling Language) tool. The process is general in nature and
users could use the process to select most engineering tools and software applications.

                                                   3
```

### PDF PAGE 4

```text
4
```

### PDF PAGE 5

```text
         CONTENTS

1.       Introduction ........................................................................................................ 7

2.       Brief History ....................................................................................................... 7

3.       Methodology ...................................................................................................... 8
    3.1  Team ............................................................................................................................... 8
    3.2  Management Approval.................................................................................................... 8
    3.3  Mission/Goal/Project Objectives/Project Scope/Constraints.......................................... 9
         3.3.1 Mission.............................................................................................................. 9
    3.4  3.3.2 Goal................................................................................................................... 9
    3.5  3.3.3 Project Objectives ............................................................................................. 9
    3.6  3.3.4 Project Scope .................................................................................................. 10
    3.7  3.3.5 Project Constraints .......................................................................................... 10
    3.8  Identified Stakeholder ................................................................................................... 10
    3.9  Discovery Phase............................................................................................................ 10
         Requirements ................................................................................................................ 11
         SysML Classes.............................................................................................................. 12
         Consultation and Training............................................................................................. 12
         Project Plan/Budget ...................................................................................................... 12

4.       Software Licensing ........................................................................................... 13

5.       Computer Security Approvals .......................................................................... 13

6.       Lessons Learned ............................................................................................... 13

7.       Software Selection............................................................................................ 14

8.       Appendix A: Pugh Matrix ................................................................................ 15

9.       Appendix B: Pair Wise Comparison ................................................................ 16

10.      References ........................................................................................................ 17

Distribution ....................................................................................................................... 18

         5
```

### PDF PAGE 6

```text
SNL                      NOMENCLATURE
SysML
COTS   Sandia National Laboratories
UML    Systems Modeling Language
SRN    Commercial off-the-shelf
SCN    Unified Modeling Language
TcSE   Sandia Restricted Network
CSU    Sandia Classified Network
NTK    Teamcenter Systems Engineering
CASA   Computer Support Unit
       Need To Know
       Common Adaptable System Architecture

       6
```

### PDF PAGE 7

```text
                               1. INTRODUCTION

This process for Selecting Engineering Tools will give the reader an understanding of the
process the authors followed to select a SysML software application tool.
SAND2006-0478 “COTS Software Selection Process” was used as a starting point. The
authors extended the previous methodology and chose to use two Six Sigma tools, Pugh
Matrix diagram and Pairwise Comparison diagram, to aid in the selection of the SysML
tool.

In addition to selecting a SysML tool for use at Sandia National Laboratories (SNL), the
authors were tasked with implementing and managing the tool on both the unclassified
and classified computer networks at SNL.

                               2. BRIEF HISTORY

The use of SysML at SNL had its start more than four years ago when Regina Griego, in
the Weapons Systems Integration Department, recommended the use of SysML to
characterize some of the system level analyses being conducted in Mark Bleck’s Use
Control Systems Department. Up to that time, Regina had been using UML (Unified
Modeling Language), which is a close sibling and progenitor of SysML, to analyze
stakeholder requirements and system constructs.

Some four years ago, shortly after taking a course in UML since there was no strictly
SysML related classes being offered at that time, the Telelogic Rhapsody UML tool with
a SysML module was purchased to perform systems modeling and analysis. From that
time up to the initiation of the SysML tool selection process nearly a year ago, the use of
SysML proceeded sporadically within SNL.

After Mark De Spain moved into 2123, the Advanced and Exploratory department, where
the objective was to apply modern analytic and modeling tools to analyze and define
systems, the decision was made to pursue a more structured and better supported
approach to selecting and maintaining a SysML tool. This decision led directly to the
SysML tool selection project that was led out of 2998.

Mark saw a rise in the interest of engineers in SysML tools and potential fits for the
SysML approach for some Advanced & Exploratory projects (e.g., CASA, Reentry
Systems Transformation and Air-delivered Systems Transformation). From our
experience with previous tool deployments, the team saw the need for a more rigorous
trade study process, including exploring the needs of users, identifying the applications
best suited for SysML, understanding the costs of tools and their range of features, and
understanding the systems engineering processes that underlie the use of SysML.

Our other immediate need was to take the burden of administering our existing Rhapsody
licenses from individual systems engineers. Department 2998 is experienced in
administering systems engineering tools, as well as providing training and consulting;

                                                     7
```

### PDF PAGE 8

```text
therefore, a transition of responsibility made sense and would improve the support
provided to all users.

                              3. METHODOLOGY

The following subsections describe the process the team used to select a SysML tool.

The team referenced the methodology outlined in SAND2006-0478, “COTS Software
Selection Process.“ The team extended the methodology used in the previous SAND
report and used a different approach in selecting a tool.

3.1 Team

Mark De Spain requested that Department 2998 manage his Rhapsody software licenses.
Mark also asked 2998 to investigate the use of Rhapsody and possibly other SysML tools
at Sandia. It became apparent that a team needed to be formed to investigate the future
use of SysML tools.

The following team members were chosen:

Kent de Jong, 2998, Information Services for Product Information
Mark De Spain, 2123, Advanced and Exploratory Systems (A&E)
Marjorie Hernandez, 2998, Information Services for Product Information
Debbie Post, 8248, Program Analysis and Integration
Jeff Taylor, 2998, Information Services for Product Information

Kent was chosen because of his systems and requirements engineering experience. The
team felt this experience would be valuable in defining requirements for a tool and
selecting a tool.

Mark was chosen because of his experience and knowledge of SysML and Rhapsody. In
addition, he could represent the user community by being the voice of the customer.

Marjorie was chosen because of her Six Sigma Green belt training and organizational
skills.

Debbie was chosen because of her systems and requirements engineering experience and
could represent the California user community.

Jeff was chosen because of his experience with choosing and deploying engineering
applications on the classified and unclassified networks.

3.2 Management Approval

The team received management approval from Fran Current, manager, 2998, and Steve
Harris. In addition to management approval, the team had two champions, Steve Harris,

                                                     8
```

### PDF PAGE 9

```text
manager, 2123, Advanced and Exploratory Systems (A&E), and Bob Oetken, 8244, CA
Advanced & Exploratory Systems.

3.3 Mission/Goal/Project Objectives/Project Scope/Constraints

3.3.1 Mission

Define a process to select software tools but to also apply this method to the selection of
a SysML tool.

3.3.2 Goal

Use and define a process to select and implement software tools at SNL.

3.3.3 Project Objectives

1. Choose a SysML tool for SNL
2. Centralize and manage existing and future tool licenses and installation packages in

    department 2998 for all users
3. Use industry best practices in Model-Based Systems Engineering to improve how to

    develop and communicate system specifications. For designs of sufficient
    complexity, users need to go beyond PowerPoint and Visio for functional analysis
    and allocation, interface definition, use case definition and requirement definition.
4. Reduce licensing costs by allowing users to share licenses
5. Make tools available at the engineer’s desktop on the SRN and SCN
6. Educate SNL engineers on the Systems Modeling Language and its potential benefits
    and costs
7. Investigate systems engineering problems and processes that benefit from the use of
    SysML
8. Develop a process for creating system specifications with a SysML tool
9. Document commercial tool functionalities with AP233
10. Document adherence of the commercial tools to the latest SysML tool standards
11. Down select to a SysML tool for technical projects at SNL (both New Mexico and
    California sites)
12. Make the SysML tool available on the SCN with appropriate access controls and
    security plans
13. Reduce the cost of stand-alone licensing and establish floating licenses for cost
    sharing on both the SRN and SCN
14. Establish a collaborative website for the SysML team and SysML tool licensing and
    installation information for users
15. Document our SysML tool selection process and results in a SAND report
16. Investigate the integration of SysML models with the Sandia application,
    “Orchestra.” Orchestra was written at Sandia New Mexico and is an embedded
    electronics design tool that can output XML files. The Orchestra users are working
    with SysML users to investigate how SysML might handoff to Orchestra.

                                                     9
```

### PDF PAGE 10

```text
3.3.4 Project Scope

    1. Evaluate and select a COTS (Commercial Off The Self) software package
    2. Stay within cost and schedule

3.3.5 Project Constraints

Team members must continue to meet other deadlines on other projects

3.4 Identified Stakeholder

When the project began, a large group of stakeholders was defined. These stakeholders
included Sandia managers and staff from the California site’s Systems, Surety,
Telemetry, and Program Analysis/Integration organizations. In New Mexico,
stakeholders identified include staff members and managers from the Systems, Surety,
Weapon Program Integration, and Engineering Requirements organizations and the
System Engineer Users Group in 2600.

Due to a cut in the project’s budget, the number of stakeholders was reduced to three
people. The stakeholders were all members of the team: Debra Post, Mark De Spain, and
Kent de Jong. These three staff members did their best by putting on their stakeholders’
hats and representing the stakeholders groups and articulating the needs and desires of
these groups.

3.5 Discovery Phase

After some discussion with systems and subsystems engineers who might benefit from
using SysML, the team realized that SysML is still in its infancy at SNL, and the
following questions could not be answered until training classes were held and a pilot
was conducted:
 What are the expectations for using a modeling tool?
 What is the work approach of systems engineering users?
 What other tools can achieve the same end?
 What kind of engineering problem can best gain value added from using SysML?
 How does SysML support an engineer’s systems engineering process?

Therefore, the team decided that it was out of project scope to develop a systems
engineering process for SysML. SysML is fairly new in the industry, and users are
beginning to apply SysML at SNL. After the team gave several technical presentations,
arranged SysML training, and acquired/deployed floating licenses, the team enabled
several projects to try SysML. After these pilot projects have progressed, the team will
better understand the return on investment for Model-Based Systems Engineering with
SysML.

                                                    10
```

### PDF PAGE 11

```text
3.6 Requirements

The articulation of stakeholders’ needs by the team members resulted in a list of criteria,
which were then driven to requirements categories.

The team collected the criteria and placed it on the team’s SharePoint site as it was
identified. There were two criteria groups, mandatory and desired features. The
mandatory criteria were those requirements that the team felt the tool must have for
Sandia. The desired features were the discriminators between the contending tools.
Mandatory criteria:

     Floating license
     Affordable (less than $1000 including SysML plug-in)
     Supports SysML 1.0 (or later)
     Complete toolset (i.e., you can create models just with this license and don't need

         additional software)
     Provide formatted reports containing model information
     Provide standard output format to other applications (e.g. AP233 or XML)
     Tech Support (Monday – Friday, 8am – 5pm, Mountain Time)
     Must work on SCN with appropriate need to know controls
     Output to Microsoft Office so results can be easily communicated
     A suite of models can be independently developed, and yet can "call" each other
     Good diagnostics/test bench capability to ensure all branches of a model are

         exercised
Desired Features:

          Online tutorial
          Company offers tutorials, training that can be tailor for our uses.
          Easy to learn
          Does simulation
          Interfaces to Teamcenter for Systems Engineering (TcSE)
          A government or volume price discount
          Looks good to us!

Based on the criteria, the team identified several requirements’ groups. The team
continued in the tool selection with these requirement groups rather than developing a
full set of requirements due to time and budget constraints. The requirement groups
were:

Floating license                             Merge multiple into larger system model
Supports SysML 1.0 (or later)                Ease of Use
Provide standard output format to other
applications (e.g. AP233 or XML)             Timeout feature for floating licenses
Tech Support (M-F 8a-5p MT)                  Simulation capability

Works on SCN with need to know controls Operating System

Independent development of a suite of        Model completeness or goodness checks

                                         11
```

### PDF PAGE 12

```text
 models

3.7 SysML Classes

Our team attended and hosted several SysML classes in New Mexico and California. The
schedule was as follows:
SysML for System Engineers in NM – August 7, 2008
SysML Class in NM – September 8, 2008
SysML for System Engineers in CA – October 7, 2008
SysML Class in CA – November 10, 2008
Beginner’s SysML Class in CA – February 2, 2009
Beginner’s SysML Class in NM – April 28, 2009

3.8 Consultation and Training

Upon doing some research through the International Council on Systems Engineering
(INCOSE) and SysML users groups and forums, the team chose a US-based consulting
firm: PivotPoint Technologies, Inc. PivotPoint Technologies is involved in the
development of the SysML and UML language standards and is active in the INCOSE
working group on Model-Based Systems Engineering (MBSE).

The team arranged for three classes and put a consulting contract in place so that users
could continue to work with the vendor as they progressed in their pilot projects. Our
team also received recommendations for criteria for comparing commercial tools that
implement the SysML standard.

The team concluded a modest analysis should be done given the available funding for this
team, down select to reasonable tools, and then monitor the progress of the pilot projects.
SNL engineers, management, and other stakeholders do not have sufficient experience in
the use of SysML to either create a highly detailed requirements document, nor to
understand the value added of this tool. The team recommend that the pilot projects give
seminars to share their experiences with SysML in order to help us assess whether or how
to promote SysML to the SNL systems engineering community.

3.9 Project Plan/Budget

The team started doing work on the project and was working on documenting the project
plan and budget when funding was cut. The team was instructed by management to use
the data and knowledge they had and choose a SysML tool.

In addition to the work listed above, the team planned to schedule and take training on
the Rhapsody SysML software tool so the team would be better able to evaluate the tool
but had to cancel. Mark had training and experience with Rhapsody so the team relied on
his expertise to evaluate Rhapsody.

                                                    12
```

### PDF PAGE 13

```text
                         4. SOFTWARE LICENSING

When Mark came to department 2998 with a need to manage Rhapsody software
licenses, the department investigated how users were using Rhapsody at Sandia.
Rhapsody was being used with standalone licenses. To get the best use out of the tool, the
standalone licenses were converted to floating licenses and the licenses were made
available on both the SRN and SCN networks.

When Magic Draw was selected as a second SysML tool for Sandia, floating licenses
were purchased. Having both Rhapsody and Magic Draw available on a floating license
server, reduced the cost of licensing.

Approval to place both Rhapsody and Magic Draw on the SCN was accomplished by
using the CNARS process. Cyber Security provided proper procedures for placing
applications on the SCN with proper NTK controls.

User procedures were written for installing both applications on the SRN and SCN for the
CSU’s.

A collaborative share site was established for all necessary information and instructions
for using the selected SysML tools on both the SRN and SCN.
Department 9341, CSU Special Projects, will manage the SysML tools selected for use at
SNL. The vendors, No Magic Inc. and IBM, will support our customers in using the
products.

                5. COMPUTER SECURITY APPROVALS

The applications, Magic Draw and Rhapsody, store the data in each user’s diskless work
station, like MS Office Products, a security plan was not needed. Users can share models
by emailing or saving models to Web Fileshare, much like MS Office files.

                           6. LESSONS LEARNED

Since the beginning of this effort, the team has been focused on determining whether the
System Modeling Language methodology could be useful for system engineers and if so,
how the system engineering staff could best learn the methodology.

As part of the work of learning the methodology, members of the group took SysML
classes. The team decided to host the classes with an independent vendor whose focus
was on the methodology. It was during these classes the team learned of some of the
challenges of comprehending and using SysML.

The learning of SysML parallels the learning of a new language. There are new elements
and new constructs in SysML, which new users need to grasp. Once understood, the
implication of the constructs and elements can be put together to communicate ideas and
concepts.

                                                    13
```

### PDF PAGE 14

```text
SysML provides the capability to triangulate between diagram elements. SysML can
compare the content of multiple diagrams and was very helpful in working on a couple of
projects. The comparison of the activity diagram (which represents functional flow) to
the structure of the product (represented in the block definition diagram) uncovered
errors, misinterpretations, and miscommunications.
However, this capability comes with a significant learning curve. SysML requires a
significant persistence to maintain a modicum of fluency. Without that persistence, is
was and is very easy to revert back to just doing 2 dimensional lines and boxes.
Having a tool is critical to using the language, yet it was found that the tool gets in the
way of learning the language. There might be a significant benefit to learning System
Modeling Language without a tool in the classroom.

                         7. SOFTWARE SELECTION

The team used two tools: Pugh Matrix and Pairwise Comparison to help them pick the
best tool to be used by engineers at SNL.
Of the three tools studied, Magic Draw was chosen as the best overall tool and was
implemented on the SRN and SCN.
It was decided to implement Rhapsody too because it has advance capabilities that Magic
Draw and Enterprise Architect do not have. Rhapsody was not the overall winner because
its advanced capabilities are more difficult to use and learn and it is more expensive.
Mark used Rhapsody before the team did the evaluation and had purchased licenses.
Converting the Rhapsody licenses from stand-a-lone to shared licenses was done at a
minimal cost.
Due to budget and schedule constraints, the team quickly chose 3 of the most popular
SysML tools on the market per public forums found on the internet. Our study did not
exhaustively evaluate every possible vendor. Our Pugh Matrix and Pairwise Comparison
scores represent the qualitative opinions of our team.

                                                    14
```

### PDF PAGE 15

```text
                                8. APPENDIX A: PUGH MATRIX

Weighted Pugh Matrix                                        Weight      Baseline                                Magic Draw   Enterprise
Requirements                                                            Rhapsody                                             Architect

Must work on SCN with appropriate need to know controls 10              0                                       0            0

Simulation capability (depending on the cost and ease of                                                                     -8

use tools with and without simulation capability may be                                                                      -4

chosen)                                                     8           0                                       -8           0
                                                                                                                             0
Model completeness or goodness checks (do you have                                                                           3
                                                                                                                             0
orphan diagram objects not connected to anything? do you                                                                     -3
                                                                                                                             2
have dangling interfaces?)                                  8           0                                       0            2
                                                                                                                             -8
Operating System (Apple, PC, Linux, etc. Engineer                       0                                       0
desktops are PC or Apple. Servers are Windows or UNIX.) 7

Supports SysML 1.0 (or later)                               6           0                                       0

A suite of models can be independently developed, and

merge into larger system model                              6           0                                       3

Floating license                                            3           0                                       0

Provide standard output format to other applications (e.g.

AP233 or XML)                                               3           0                                       -3

Tech Support (M-F 8a-5p MT)                                 2           0                                       6

Ease of Use                                                 2           0                                       4

Total                                                                   0                                       2

Notes: Used the pairwise comparison for weight (listing the most important requirement to the least important)

For example, Magic Draw and Enterprise Architect was given a -1 for simulation because neither application does simulation)

                                                                    15
```

### PDF PAGE 16

```text
9. APPENDIX B: PAIR WISE COMPARISON

                                    16
```

### PDF PAGE 17

```text
                                    10. REFERENCES

1. Han Lin, COTS Software Selection Process (U), SAND2006-0478, Sandia National
     Laboratories, Albuquerque, NM, May 2006.

                                                         17
```

### PDF PAGE 18

```text
                          DISTRIBUTION

1 MS0340 Mark De Spain           2123
                                 2998
1 MS0626 Kent de Jong            2998
                                 2998
1 MS0932 Marjorie Hernandez      8248
                                 2123
1 MS0648 Jeff Taylor             2998
                                 8248
1  MS9154  Debbie Post

1  MS0340  Steven Harris

1  MS0626  Tony Hernandez

1  MS9154  Raymond Ng

1 MS0899 Technical Library       9536 (electronic copy)

                             18
```

### PDF PAGE 19

```text

```


## EXACT ATTACHMENT METADATA

````json
{
  "id": "55868994",
  "type": "attachment",
  "status": "current",
  "title": "SelectingASysMLTool.pdf",
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
    "when": "2020-04-08T11:34:41.912+02:00",
    "message": "",
    "number": 1,
    "minorEdit": true,
    "hidden": false,
    "_links": {
      "self": "https://docs.nomagic.com/rest/experimental/content/55868994/version/1"
    },
    "_expandable": {
      "content": "/rest/api/content/55868994"
    }
  },
  "position": -1,
  "container": {
    "id": "55866307",
    "type": "page",
    "status": "current",
    "title": "SysML Plugin",
    "position": -1,
    "extensions": {
      "position": "none"
    },
    "_links": {
      "webui": "/spaces/PLUGINS/pages/55866307/SysML+Plugin",
      "edit": "/pages/resumedraft.action?draftId=55866307&draftShareId=dd483b31-b200-45a9-9395-89a8a8ac0612",
      "tinyui": "/x/w3NUAw",
      "self": "https://docs.nomagic.com/rest/api/content/55866307"
    },
    "_expandable": {
      "container": "/rest/api/space/PLUGINS",
      "metadata": "",
      "operations": "",
      "children": "/rest/api/content/55866307/child",
      "restrictions": "/rest/api/content/55866307/restriction/byOperation",
      "history": "/rest/api/content/55866307/history",
      "ancestors": "",
      "body": "",
      "version": "",
      "descendants": "/rest/api/content/55866307/descendant",
      "space": "/rest/api/space/PLUGINS",
      "relevantViewRestrictions": "/rest/api/content/55866307/restriction/relevantViewRestrictions"
    }
  },
  "metadata": {
    "mediaType": "application/pdf"
  },
  "extensions": {
    "mediaType": "application/pdf",
    "fileSize": 115494,
    "comment": ""
  },
  "_links": {
    "download": "/download/attachments/55866307/SelectingASysMLTool.pdf?version=1&modificationDate=1586338481912&api=v2",
    "webui": "/spaces/PLUGINS/pages/55866307/SysML+Plugin?preview=%2F55866307%2F55868994%2FSelectingASysMLTool.pdf",
    "self": "https://docs.nomagic.com/rest/api/content/55868994"
  },
  "_expandable": {
    "operations": "",
    "children": "/rest/api/content/55868994/child",
    "restrictions": "/rest/api/content/55868994/restriction/byOperation",
    "history": "/rest/api/content/55868994/history",
    "ancestors": "",
    "body": "",
    "descendants": "/rest/api/content/55868994/descendant",
    "space": "/rest/api/space/PLUGINS",
    "relevantViewRestrictions": "/rest/api/content/55868994/restriction/relevantViewRestrictions"
  }
}
````
