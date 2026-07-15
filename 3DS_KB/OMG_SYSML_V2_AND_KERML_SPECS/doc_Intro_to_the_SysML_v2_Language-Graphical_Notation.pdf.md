# AUTHORITATIVE PDF EXTRACTION: Intro to the SysML v2 Language-Graphical Notation.pdf

- source_repository: https://github.com/Systems-Modeling/SysML-v2-Release
- source_commit: `288d129c0d532065d45434bbb48a920898b719af`
- source_path: `doc/Intro to the SysML v2 Language-Graphical Notation.pdf`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Release/blob/288d129c0d532065d45434bbb48a920898b719af/doc/Intro to the SysML v2 Language-Graphical Notation.pdf
- source_bytes: 2129146
- source_sha256: `2f3a3d30de93d2e8262a1643805c033bd5a22a0a4b4ee3af7a1c92aa2f53b70f`
- pdf_pages: 123
- extracted_utc: `2026-07-14T16:48:11.875554+00:00`
- pdf_metadata: `{'/Title': 'SysML v2 Language Intro to Structure and Behavior Modeling', '/Author': 'Ed Seidewitz', '/Subject': '', '/Keywords': '', '/CreationDate': "D:20230313124016-04'00'", '/ModDate': "D:20230313124016-04'00'", '/Producer': 'Microsoft® PowerPoint® for Microsoft 365', '/Creator': 'Microsoft® PowerPoint® for Microsoft 365'}`

## SEMANTIC PAGE-BY-PAGE EXTRACTION

### PDF PAGE 1

SST
         Introduction to the SysML v2 Language
                             Graphical Notation
                                    (2023-03-07)


       This presentation uses the graphical notation to complement the
        textual syntax (i.e., notation) to represent a SysML model. The
        graphical notation is generated manually with Microsoft Visio.








                Copyright © 2021, 2022, 2023 by Sanford Friedenthal
     Licensed under the Creative Commons Attribution 4.0 International License.
To view a copy of this license, visit   http://creativecommons.org/licenses/by/4.0/          or
send a letter to Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.

### PDF PAGE 2

Agenda                                             SST



  Language Background and Overview
  SysML v2 Functional Areas
  Contrasting SysML v2 with SysML v1
  Summary














Refer to date in lower right on each slide to see when it was last modified


2                                                                                          16 January 2023

### PDF PAGE 3

General Caveats                                          SST




 The graphical and textual notation (i.e., syntax) are different renderings of the
  same model

    The textual syntax is formally specified using BNF

    The graphical syntax is formally specified using graphical BNF

    The graphical visualization in this presentation is captured in Visio
    Two visualization prototypes are under development (Tom Sawyer and PlantUML)
 SysML v2 Marker

    Some of the more significant SysML v2 changes in functionality and terminology
     relative to SysML v1 are designated with the SysML v2 marker












3                                                                                      07 March 2023

### PDF PAGE 4

Language Background & Overview


















4                                                       11 November 2022

### PDF PAGE 5

Systems Modeling Language™                                         SST
                                       (SysML®)

     Supports the specification, analysis, design, and verification and validation
       of complex systems that may include hardware, software, information,
                            processes, personnel, and facilities


     SysML   has evolved to address user and vendor needs
         v1.0, adopted in 2006; v1.6, current version; v1.7

     SysML   has facilitated awareness and adoption of MBSE

     Much has been learned from using SysML          for MBSE













5                                                                                  07 March 2023

### PDF PAGE 6

SysML         v2 Objectives                                SST




    Increase adoption and effectiveness of MBSE
    by enhancing…

         Precision and expressiveness of the language
         Consistency and integration among language concepts
         Interoperability with other engineering models and tools
         Usability by model developers and consumers
         Extensibility to support domain specific applications
         Migration path for SysML v1 users and implementors










6                                                                                 11 November 2022

### PDF PAGE 7

Key Elements of SysML                        v2                 SST




 New Metamodel that is not constrained by UML

    Preserves most of UML modeling capabilities with a focus on systems modeling

    Grounded in formal semantics
 Robust visualizations based on flexible view & viewpoint specification
    Graphical, Tabular, Textual
 Standardized API to access the model


















7                                                                               11 November 2022

### PDF PAGE 8

SysML v2 Language Architecture                                                              SST


                                                                                                      Declarative semantic
                                             Systems Modeling Language                                base elements and
                                                         (SysML)                                      domain-specific libraries
                                                                                                      modeled using SysML

                                 Systems                metamodel             Systems and
                                  Syntax              semantic library       Domain Model
                                                                                Libraries
                                              Kernel Modeling Language                               Declarative semantic
                                                         (KerML)                                     base elements modeled
                                                                                                     using KerML
                                   Kernel               metamodel             Kernel Model

                                  Syntax              semantic library            Library


                                                                                                     Direct semantic mapping
                                                         semantic                                    to formal logic
                                    Core               specification               Core
                                  Syntax                                       Semantics


                                                        Root syntactic elements
                                                        without model-level
                                    Root                semantics (e.g., packaging)
                                  Syntax

8                                                                                                                  07 March 2023

### PDF PAGE 9

SysML v2 API & Services                                        SST




 Enables other tools and applications to access SysML models in a standard way
 Provides services to:

    Create, update, and delete elements

    Query and navigate model
    Other services including support for model management, analysis,
     transformation, and file export generation
 Supports common patterns called recipes (GitHub -            Systems-Modeling/SysML-
  v2-API-Cookbook: Recipes for using the SysML v2 API)

    Navigating a decomposition tree

    Creating a branch

    Query with multiple constraints
 Facilitates use of different implementation technologies such as REST/HTTP,
  Java, or OSLC


9                                                                                 11 November 2022

### PDF PAGE 10

Pilot Implementation                             SST
                        Using Standard API


















                                                                   Meta-Model
                                                                 based on KerML










10                                                              11 November 2022

### PDF PAGE 11

SysML v2 Language                             SST
                               Capabilities



































11                                                               11 November 2022

### PDF PAGE 12

Definition and Usage                                        SST
                                   Reuse Pattern

 A definition element defines an element such as a part, action, or requirement
 A usage element is a usage of a definition element in a particular context

    There can be different usages of the same definition element in either different
     contexts or the same context
 Pattern is applied consistently throughout the language





                                                                                     notation

                                                                     defined by








12                                                                                 11 November 2022

### PDF PAGE 13

SysML v2 Notation (1 of 2)                                             SST
                               Textual and Graphical

  package   'Vehicle Parts Tree' {
    part vehicle {
      attribute mass;
      perform  providePower;
      part engine {
        attribute mass;
        perform  providePower.generateTorque;
        part cylinders [6];
      }
      part transmission {
        attribute mass;
        perform  providePower.amplifyTorque;
      }
    }
    }
    action providePower   {
      action generateTorque;
      action amplifyTorque;
    }
  }



13                                                                                        11 November 2022

### PDF PAGE 14

SysML v2 Notation (2 of 2)                                                                  SST
                                       Textual and Graphical


                             interface def Drive {
                                 end  enginePort : DrivePort;
                                 end  transmissionPort : ~DrivePort;
                             }

                             part vehicle : Vehicle {
                                     part engine : Engine { portdrivePort : DrivePort; }
                                     part transmission : Transmission { portdrivePort : ~DrivePort; }

                                     interface : Drive
                                         connect engine.drivePort  to transmission.drivePort;
                              }


                                                                 «part»
                                                            vehicle : Vehicle



                          «part»                                : Drive                               «part»
                      engine: Engine                                                              transmission :
                                               drivePort :                    drivePort :          Transmission
                                                DrivePort                     ~DrivePort

                                Tom Sawyer Visualization Prototype

14                                                                                                                  11 November 2022

### PDF PAGE 15

SysML v2 Spec (Clause 7)                                         SST
                       SysML v2 Language Description


    7.1 Language Overview                         7.14  Interfaces
    7.2  Elements and Relationships               7.15  Allocations
    7.3  Dependencies                             7.16  Actions
    7.4  Annotations                              7.17  States
    7.5  Namespaces and Packages                  7.18  Calculations
    7.6  Definition and Usage                     7.19  Constraints
    7.7  Attributes                               7.20  Requirements
    7.8  Enumerations                             7.21  Cases
    7.9  Occurrences                              7.22  Analysis Cases
    7.10 Items                                    7.23  Verification Cases
    7.11 Parts                                    7.24  Use Cases
    7.12 Ports                                    7.25  Views and Viewpoints
    7.13 Connections                              7.26  Metadata (incl. User Defined Keywords)




15                                                                                         07 March 2023

### PDF PAGE 16

Module 1
               Packages & Element Names

















16                                                     11 November 2022

### PDF PAGE 17

Model Organization                                            SST



  A hierarchy of packages, where packages can contain other           packages and elements
  Packages are namespaces that contain member elements that may be owned or unowned
  A package can import members of another package as unowned members, where deletion
   semantics do not apply, and they can be referred to by their local name

    Nested import notation enables flexible organization























17                                                                                      11 November 2022

### PDF PAGE 18

Import Notation                                    SST




 no star is element import
 single star is package import (content of package)
 double star is recursive including outer package


 Imports can apply to any namespace, but
  packages are most commonly used
 A package import can include filter criteria to select
  elements based on their metadata














18                                                                            11 November 2022

### PDF PAGE 19

Definitions Package                                       SST




 Example: Definitions package contains packages to define different kinds of
  elements

    Ellipsis indicates there is more content







                …


19                                                                              11 November 2022

### PDF PAGE 20

Package Compartments                                      SST




 Packages can include textual compartments
 Filter can be applied to select element kinds




























20                                                                             16 January 2023

### PDF PAGE 21

Qualified Names                                         SST




 A qualified name of a model element is prepended by the name of its owner
  followed by a double colon (::)
 A fully qualified name is prepended by the concatenated names of its owners in
  its containment hierarchy separated by double colons (::)





                        A::B::VehicleB::Vehicle














21                                                                                  11 November 2022

### PDF PAGE 22

Element Names                                           SST



 Each element includes a universally unique identifier (UUID) that is not visible

    Managed by the tool

    Does not change over the life of the element
 Each element can include a name
    Required for an element to be referenced in the textual notation
 Each element can optionally include a short name in angle brackets

    Can be a user or tool selected id
 An element can have one or more aliases in the context of a namespace





                                                              Note: reserved words can be
                                                              shown in «guillemet»   or bold



22                                                                                   11 November 2022

### PDF PAGE 23

Module 2
                      Definition Elements

















23                                                           11 November 2022

### PDF PAGE 24

Part Definition                                         SST



 A Part Definition can contain features such
  as attributes, ports, actions, and states
   A modular unit of structure



























24                                                                                   11 November 2022

### PDF PAGE 25

Other Kinds of Definition Elements                                                               SST
                                                       Terminology

  Each kind of definition element can contain specific kinds of features

     Attribute definition
      ▪  Data type that defines a set of data values
      ▪  Primitive attribute definitions include integer, Real, Complex, Boolean, String, ….
      ▪  Can include quantity kinds such as Torque with units
      ▪  Can include complex data types such as vectors

     Port definition                                                                                            ~      ~
      ▪  Defines a connection point on parts that enable interactions
      ▪  Contain kinds of features including directed features with in, out, and in/out
      ▪  Ports can be conjugated (i.e., reverse direction of directed features)

     Item definition
      ▪  Defines kind of entity that is acted on, such as an input, output or a stored item

     Action definition
      ▪  Defines kind of behavior that transforms inputs and outputs

     State definition
      ▪  Defines kind of behavior that responds to events
      ▪  Enables entry, exit, and do actions


 25                                                                                                            11 November 2022

### PDF PAGE 26

Specialization                                           SST



 Definition elements can be specialized
    Subclass inherits features from its superclass that can be redefined or subsetted

    Subclass can add new features

    Subclass can be a specialization of more than one superclass (i.e., multiple
     inheritance)
















                     inherited
                     added



26                                                                                     11 November 2022

### PDF PAGE 27

Redefinition and Subsetting                                        SST



 An inherited feature can be redefined         by a
  feature whose definition is more specialized
    The more specialized feature overrides the
     inherited feature
    Symbol for redefines (:>>)


 An inherited feature can be subsetted         by one
  or more features with a more constrained
  multiplicity

    The Engine4Cyl contains a subset of the
     cylinders contained by Engine

    First redefine multiplicity to 4

    Then identify the subsetting     features
    Symbol for subsets (:>)

27                                                                                 11 November 2022

### PDF PAGE 28

Module 3
                         Usage Elements

















28                                                          11 November 2022

### PDF PAGE 29

Part                                            SST



  A part is a usage of a part definition
  Part inherits its features from its definition
  Inherited features can be redefined or subsetted, and new features can be added





   redefined
   added

   inherited

















29                                                                                        11 November 2022

### PDF PAGE 30

Other Usage Elements                                          SST
                                         Terminology

 Other kinds of usage elements are defined by specific kinds of definition
  elements

    Attributes defined by attribute definition

    Ports defined by port definition

    Items defined by item definition
    Actions defined by action definition

    States defined by state definition

    …















30                                                                                11 November 2022

### PDF PAGE 31

Enumeration                                         SST



 A data type whose range is restricted to a set of discrete values

    Without units
     ▪ Definition:   enum    def Colors {red; blue; green;}
     ▪ Usage:        attribute  color1: Colors = Colors::blue;



    With units:
     ▪ Definition:   enum    def DiameterChoices      :> ISQ::LengthValue     {
                         enum    = 60 [mm];
                         enum    = 70 [mm];
                         enum    = 80 [mm];
                     }
     ▪ Usage:        attribute  cylinderDiameter: DiameterChoices         = 80 [mm];




31                                                                                11 November 2022

### PDF PAGE 32

Usage Elements Defined By                                           SST
                       Default Definition Elements

 A definition element is a subclass of the most general definition element in the
  SysML v2 library (e.g., Part)
 A usage element is defined by a definition element

    defined by is a kind of specialization
 A usage element that is not provided a definition by the modeler is a subset of
  the most general usage element in the library (e.g., parts)
                                Default part          Default Part Definition

       SysML v2
        Library


      part without
       definition
                                                defined by
       part with
       definition

32                                                                                  11 November 2022

### PDF PAGE 33

Module 4
                     Part Decomposition

















33                                                         11 November 2022

### PDF PAGE 34

SysML v1 Decomposition in SysML v2                                   SST



 defined by relationship is used to create next level of decomposition of a part def








                                                                defined by
















34                                                                         11 November 2022

### PDF PAGE 35

Parts Decomposition                                            SST




  A parts tree is a composition of a part from other parts

    SysML v1 only supports block decomposition

    Definition element can serve as black-box specification without committing to an
     internal structure (e.g., part decomposition)

    Can provide significant advantages (more intuitive, less ambiguous, easier to
     modify a design configuration)







       There is no part-to-part
            decomposition
              In SysML v1



35                                                                                    11 November 2022

### PDF PAGE 36

Parts Tree Reuse & Modification                                    SST
                              Subsetting           a Part

 A part can be a subset of another part

   Equivalent to specializing a part

   Inherits the part decomposition and other features
   Can modify inherited parts and features through redefinition and subsetting

   Can add new parts


                       subsets
















36                                                                            11 November 2022

### PDF PAGE 37

References                                          SST



  A part can refer to other parts that are part of another decomposition

    Not composite (i.e., lifetime semantics do not apply)

    Bind the reference usage



  reference                   bind                           bind                   reference



  A part can refer to an item that it stores












37                                                                                      16 January 2023

### PDF PAGE 38

Multiplicity                                          SST




  Defines the number of features (e.g., parts) in a particular context

    Defines a range with a lower bound and upper bound

    Lower and upper bounds are integers
     ▪  Can be parameterized [x..y] where x and y are expressions
    Default multiplicity is [1..1]

    Optional multiplicity [0..1]


















38                                                                                    11 November 2022

### PDF PAGE 39

Module 5
                      Part Interconnection

















39                                                           11 November 2022

### PDF PAGE 40

Connecting Parts                                                  SST


 Parts can be connected via their ports or without ports

    Parts can be connected directly without connecting to the composite part

    Ports can contain nested ports

    Flows can be shown on connections

    References are dashed

    Conjugate port

    Binding connection





















40                                                                                                11 November 2022

### PDF PAGE 41

Interfaces                                           SST



  A connection definition connects two usage elements (e.g., two parts)
  An interface definition is a connection definition whose ends are compatible ports

    Can contain flows

    Can contain other kinds of features
  An interface defined by an interface definition is used to connect ports

    Ports on parts must be compatible with the interface definition



















41                                                                                     11 November 2022

### PDF PAGE 42

Interface                                                  SST
                           Connecting a Wheel to a Hub


 Usage of WheelToHub      interface definition specifies a compatible connection between a wheel and a hub
    Connects composite ports on wheel and hub

    Decomposes into 5 Wheel Fastener interfaces
 Wheel Fastener interface species a compatible connection between a lugnut        and shank

    Contains features needed for a compatible connection
























 42                                                                                                 11 November 2022

### PDF PAGE 43

Wheel Hub Interface                                      SST



 Usage of WheelHubInterface      to specify interface between rear axle and wheels
































43                                                                                11 November 2022

### PDF PAGE 44

Nested Wheel Hub Interface                          SST





































44                                                                11 November 2022

### PDF PAGE 45

Module 6
                                 Variability

















45                                                                 11 November 2022

### PDF PAGE 46

Variability                                         SST



  Vehicle family is the superset model (150%)
  Variation  points represent elements that can vary

    Can be applied to all definition and usage elements
  A variant represents a particular choice at a variation point
  A choice at one variation point can constrain choices at other variation points
  A system can be configured        by making choices at each variation point



















46                                                                                    11 November 2022

### PDF PAGE 47

Selected Vehicle Configuration                                              SST




  Vehicle_a   subsets vehicleFamily    to represent a particular design configuration
  Selected parts must satisfy variability constraints

    Model is inconsistent if constraints are not satisfied

    Variability modeling applications can automate the selection of valid configurations
























47                                                                                         11 November 2022

### PDF PAGE 48

Behavior


















48                                                                          11 November 2022

### PDF PAGE 49

Module 7
                                  Actions

















49                                                                11 November 2022

### PDF PAGE 50

Actions                                          SST




 Actions are defined by action definitions

    Inherit features (e.g., input and output parameters)

    Can redefine or subset inherited features or add new features

























50                                                                                   11 November 2022

### PDF PAGE 51

Action Decomposition                                   SST




 Actions can be decomposed in a similar way as parts






























51                                                                       11 November 2022

### PDF PAGE 52

Part Performs Actions                                            SST




  A part that performs an action can reference an action in an action tree
  This is done through reference subsetting










providePower













providePower.generateTorque






52                                                                                         07 March 2023

### PDF PAGE 53

Perform Action                                               SST



  Show two kinds

     perform action1

     perform action action1
  The difference between these two is as follows

     Line with arrow
      part  part1  {perform    action1} (example from previous slide)
      this creates an anonymous reference feature that subsets action1 which is often in a
      separate action tree. Name is properly qualified such as package1::action1). This is
      like a call action.

     Line with white diamond
      part  part1  {perform action      action1}
      This creates an explicit reference feature called action1 that can either subset or bind
      to another action


     This pattern is repeated for many different          kinds of features.




53                                                                                             11 November 2022

### PDF PAGE 54

Perform Action                                     SST
                                 Simple Example


  package  PerformActions{
     part part0{
       perform action  action1;
       perform  action2;
     }
     action action2;
  }


                                        Alternatives















54                                                                                07 March 2023

### PDF PAGE 55

Module 8
                             Action Flow

















55                                                             11 November 2022

### PDF PAGE 56

Action Flow                                          SST



 Actions can include successions and input/output flows
 Control nodes include decision, merge, fork, and join nodes
 Actions can include send and accept actions
 Swimlanes represent performers of actions














   Note: Parameter notation subject to change
56                                                                                     16 January 2023

### PDF PAGE 57

Input/Output Flows                                            SST



  A flow is a kind of connection that transfers items from a source output to a
   target input

    A flow is a transfer that continues while the source and target actions execute
     (this is the default)

    A succession flow is a transfer that only occurs after the source action ends and
     before the target action starts





















57                                                                                       16 January 2023

### PDF PAGE 58

Controlling Actions [1]                                          SST




  A start action and done action represent the start and end of an action sequence
  A succession asserts that the target action can start execution only after the
   source action ends execution
  A conditional succession asserts that the target action can start only if the guard
   condition is true (if…then). If the guard is false, the target action cannot start





















58                                                                                     11 November 2022

### PDF PAGE 59

Controlling Actions [2]                                         SST



 Control nodes are kinds of actions (with names) that control outgoing
  successions in response to incoming successions

   Decision node
     ▪ 1 incoming succession and 1.. many outgoing successions
     ▪ One outgoing succession is selected based on the guard condition that is
       satisfied (“else” condition is the complement of all other guard conditions)
   Merge node
     ▪ 1.. many incoming successions and 1 outgoing succession
     ▪ The outgoing succession occurs when any of its incoming successions occur












 59                                                                                    11 November 2022

### PDF PAGE 60

Controlling Actions [3]                                        SST



    Fork node
     ▪ 1 incoming succession and 1.. many outgoing successions
     ▪ All outgoing successions occur when its incoming succession occurs
    Join node
     ▪ 1.. many incoming successions and 1 outgoing succession
     ▪ Outgoing succession occurs when all its incoming successions occur

    Note: Control nodes cannot currently be applied to input/output flows
















60                                                                                   11 November 2022

### PDF PAGE 61

Controlling Actions [4]                                                    SST



  startVehicle subsets startVehicle1   behavior
   which is independent of structure                                               `
  Event occurrences
  Accept actions and send actions

     When a send action executes, it
      transfers an item to a target part

     When a triggering input item is
      received, an accept action executes                                                        `
      and can transfer the input item to
      another action
  driver and vehicle are in a shared
   context (not shown)












61                                                                                                     16 January 2023

### PDF PAGE 62

Scenario_1o                                                                                                   SST
                                                                          Textual Notation


package Scenario_1o{                                                                                  part def Driver{
         item def VehicleStart;                                                                         port p1;
         item def EngineStatus;                                                                         port p2;
                                                                                                      }
         action startVehicle1{                                                                        part def Vehicle{
           event occurrence doorClosed;                                                                 port p1;
           event occurrence driverReady;                                                              }
           first doorClosed   then driverReady;
           first driverReady   then turnVehicleOn;                                                    part part0{
                                                                                                        perform action startVehicle:>startVehicle1{
           action turnVehicleOnsend vs via source{                                                        action :>> turnVehicleOn      send vs via source{
             in vs:VehicleStart;                                                                            in :>> source = driver.p1;
             in source default self;                                                                      }
           }                                                                                              action :>> trigger1 accept vs:VehicleStart       via vehicle.p1;
           action trigger1 accept vs:VehicleStart;
                                                                                                          action :>> sendStatus     send es via source{
           flow of VehicleStartfrom trigger1.vs to startEngine.vs;                                          in es:EngineStatus;
           action startEngine{                                                                              in :>> source = vehicle.p1;
             in item vs:VehicleStart;                                                                     }
             out item es:EngineStatus;                                                                    action :>> trigger2 accept es:EngineStatus         via vehicle.p1;
           }
           flow of EngineStatus     from startEngine.es to sendStatus.es;                               }
                                                                                                        part driver : Driver {
           action sendStatus     send es via source{                                                      perform startVehicle.turnVehicleOn;
             in es:EngineStatus;                                                                          perform startVehicle.trigger2;
             in source default self;                                                                      event startVehicle.driverReady;
           }                                                                                            }
           action trigger2 accept es:EngineStatus;                                                      part vehicle : Vehicle {
                                                                                                          perform startVehicle.trigger1;
           message of VehicleStart      from turnVehicleOn       to trigger1;                             perform startVehicle.startEngine;
           message of es:EngineStatus        from sendStatus     to trigger2;                             perform startVehicle.sendStatus;
         }                                                                                                event startVehicle.doorClosed;
                                                                                                        }
                                                                                                        interface driver.p1 to vehicle.p1;
                                                                                                        interface driver.p2 to vehicle.p1;
                                                                                                      }
                                                                                                   }
62                                                                                                                                                                                     16 January 2023

### PDF PAGE 63

Module 9
                                    States

















63                                                                 11 November 2022

### PDF PAGE 64

States                                           SST




  States can be defined by state definitions

    Inherit features (e.g., actions, nested states, transitions) from its state definition

    Can redefine or subset inherited features or add new features

























64                                                                                          07 March 2023

### PDF PAGE 65

State-based Behavior [1]                                        SST



 States decompose into nested states (without regions, which were in SysML v1)

   A parallel state decomposes into concurrent states
   A non-parallel state (default) decomposes into sequential/exclusive states
 Transitions between sequential states

   Triggered by events

   Can include guard and action



















65                                                                                     07 March 2023

### PDF PAGE 66

State-based Behavior [2]                                        SST




 States can have entry, exit, and do actions that can refer to actions in action
  trees or be defined locally
 States can include constraints


























66                                                                                   07 March 2023

### PDF PAGE 67

Part Exhibits States                                  SST




 A part exhibits states
 Owns its state-based behavior




























67                                                                             07 March 2023

### PDF PAGE 68

Module 10
                              Interactions

















68                                                              11 November 2022

### PDF PAGE 69

Sequence View                                        SST




 Represents an event sequence and messages (refer to action flow on slide 62)
    Event sequence

    Message

    Driver and vehicle are in a shared context (not shown)























69                                                                                  16 January 2023

### PDF PAGE 70

Module 11
                               Individuals

















70                                                               11 November 2022

### PDF PAGE 71

Individuals                                          SST



 An individual definition is a unique member of a class with identity

    A specialization of a class, having only one member

    Has a unique lifetime
 An individual is a usage that is defined by an individual definition

    Can subset a part to represent a particular configuration
    Can have different configurations across Vehicle-1 lifetime



















71                                                                                     11 November 2022

### PDF PAGE 72

Module 12
                   Timeslices      & Snaphots

















73                                                        11 November 2022

### PDF PAGE 73

4D Model & Occurrences                                                  SST




  Each entity called an occurrence has a lifetime

     Distinct from attributes which do not have a lifetime

     Includes a reference clock that can quantify time (defaults to universal clock)

     Can specify time slices and snapshots
  Spatial items are kinds of occurrences that have spatial extent that can change
   over their lifetime

     Specified by shapes with position and orientation within coordinate frames
  Individuals

     Unique occurrence with a lifetime













74                                                                                              11 November 2022

### PDF PAGE 74

Lifetime with                                              SST
                            Snapshots and Time Slices


 Each individual definition has a unique lifetime

    Begins when it is created

    Ends when it is destroyed
 Individual usage exists over some portion of
  Vehicle-1 lifetime
 Individual lifetime can be segmented into time
  slices (i.e., durations of time)
 A time slice whose duration is zero is a snapshot

    Beginning and ending snapshot of a time slice is
     designated as start and      done   snapshot
 The condition of an individual for a time slice or
  snapshot can be specified in terms of the values of
  its features







 75                                                                                           11 November 2022

### PDF PAGE 75

Individuals Playing Different Roles                                             SST




 An individual can play different roles and have different configurations in different time slices
     ▪ Individual wheel (Wheel-1) is left front wheel during vehicle_b_t1-t2 time slice
     ▪ Individual wheel (Wheel-1) is right front wheel during vehicle_b_t2-t3 time slice


         part
         redefine

                                                                                         temporal
      Individual time slice                                                           decomposition


   individual                                                                                  individual








 76                                                                                          11 November 2022

### PDF PAGE 76

Module 13
               Expressions and Calculations

















77                                                        11 November 2022

### PDF PAGE 77

Expressions                                          SST




 Used to compute a result
 Library of mathematical functions (e.g., sum, max,  …)

    Includes arithmetic operators that also apply to vectors and tensors
 Default value means value can be over-ridden using redefinition























78                                                                                  11 November 2022

### PDF PAGE 78

Calculations                                          SST




  A kind of behavior generally used to represent reusable mathematical functions

    Inputs

    Expression

    Returns a single result
     ▪  Can have multiplicity


  Represent a calculation definition using the textual notation
     calc def Force {
         in attribute m:>ISQ::mass;
         in attribute a:>ISQ::acceleration;
         return   f :>ISQ::force = m * a;
     }




79                                                                                    11 November 2022

### PDF PAGE 79

Calculations                                        SST



 Evaluate usage

    Bind values to input parameters. Then evaluate expression and return a result

    calc  force : Force {
        in m=1500 [kg];
        in a=9.806 [m/s^2];
     }
 Can bind a calc return value to an attribute
    attribute  f1  = Force (m=1500 [kg] , a = 9.806  [m/s ^2]);















80                                                                                    16 January 2023

### PDF PAGE 80

Binding Connection                                            SST



  A binding is a kind of connection where both sides of the connection are asserted
   to be equal at all times

    Symbol is «bind» or =

    If both sides are not equal, the model is inconsistent (e.g., 3=4) is inconsistent

    A tool could make both sides equal if the values are not the same
     ▪  In the above example, the values can be set to (3=3) or (4=4)
     ▪  For y = x+3, when x is 1, then y can be set to 4 so that both sides are equal
    Different from the Boolean operator ‘==’, which evaluates whether both sides
     of the ‘==’ have the same value or not, and returns a value of true or false
     (e.g., {3==4} returns a value of false)
  Binding can be used to establish equality of any kind of feature

    A part can be bound (e.g., engine = engine4cyl)

    A port on a composite part can be bound to a port on a nested part to
     constrain them to have equal values

81                                                                                      16 January 2023

### PDF PAGE 81

Module 14
                       Quantities & Units

















82                                                           11 November 2022

### PDF PAGE 82

Quantities and Units                                              SST




  Quantity is an attribute (e.g., mass)
  Quantity is defined by an attribute def of a quantity kind (e.g., MassValue)
  Units conform to the quantity kind (e.g., kilograms conform to MassValue)
  The values are associated with the units
  A change in a unit can apply the unit conversion factor if a tool supports this

    attribute m:MassValue = 25 [kg] (an equivalent value to 55.1 [lbs])

    In SysML v1, a change in unit requires a change in the value type
  Complex quantities and units can be derived from primitive quantities and units

    distancePerVolume    :> scalarQuantities   = distance / volume
  Libraries

    International System of Quantities (ISQ)

    International System of Units (SI)

    US Customary Units (USCustomaryUnits)


83                                                                                       11 November 2022

### PDF PAGE 83

Module 15
                              Constraints

















84                                                             11 November 2022

### PDF PAGE 84

Constraint Expression [1]                                               SST




 A Boolean expression that evaluates to true or false, which includes

    Constraint operators (==), (>),  (>=), (<), (<=), (!=)
     ▪  Used to compare expressions (e.g., {a < b})

    Boolean operators include and, or, xor, not
     ▪  Used to logically combine expressions  (e.g., {A and          B or C})
 Asserting a constraint to be true means the evaluation must be true
  for the model to be consistent
 part def FuelTank      {
          attribute mass :> ISQ::mass;
          ref item fuel:Fuel{
            attribute redefines fuelMass;
          }
          attribute fuelMassMax:>ISQ::mass;
          assert constraint {fuel.fuelMass<=fuelMassMax}
 }



85                                                                                           11 November 2022

### PDF PAGE 85

Constraint Expression [2]                                   SST




 Usage inherits constraint expression and redefines constraint parameters






























86                                                                           11 November 2022

### PDF PAGE 86

Constraint Definition                                       SST




 Enables reuse of a constraint expression
 Default parameter direction is ‘in’
 Can assert a constraint on the usage
 Bind parameters on the usage
 Can mark dependent parameters as derived with slash




















87                                                                                 16 January 2023

### PDF PAGE 87

Binding Constraints                                 SST




 Equivalent to SysML v1 parametric diagram






























88                                                                       11 November 2022

### PDF PAGE 88

Module 16
                          Requirements

















89                                                          11 November 2022

### PDF PAGE 89

Requirement Definition                                                  SST



  A constraint definition that a valid design solution must satisfy that can include:

     Identifier
     Shall statement

     Constraint expression that can be evaluated to true or false
      ▪ can apply to performance, functional, interface and other kinds of requirements if desired

     Assumed constraint expression that is asserted to be true for the requirement to be valid

     Attributes  of the constraint expressions



















90                                                                                               16 January 2023

### PDF PAGE 90

Requirement Specification                                              SST



  A tree of requirements that contains nested requirement usages

     Composite requirement can own or reference other requirements

     Subject of nested requirements is the kind of entity being specified

     Requirement features can redefine features of the requirement definition
composite requirement
           subject



                                      reqt id







                                          assumption


91                                                                                         16 January 2023

### PDF PAGE 91

Satisfying a Requirement                                            SST



  The vehicleSpecification   imposes constraints on the vehicle

    The modeler can assert the vehicle mass satisfies the massRequired
      ▪ Bind the vehicle mass to massActual     of the requirement








                                                     …








92                                                                                       16 January 2023

### PDF PAGE 92

Satisfying a Requirement                           SST
                       Alternative Notation


 Alternative notation































93                                                                 07 March 2023

### PDF PAGE 93

Requirement Allocation vs.                                           SST
                       Requirement Satisfaction

 Allocating a requirement assigns responsibility for realizing a requirement
 Less formal than requirement satisfaction (no explicit constraint assertion)
 Can be decomposed










                                                                  :>>mass = dryMass+fluidMass
                                                                  …














94                                                                                     16 January 2023

### PDF PAGE 94

Derived Requirement                                          SST



  Single original requirement with one or more
   derived requirements
  If the original requirement is satisfied, then all the
   derived requirements must be satisfied

























95                                                                                     16 January 2023

### PDF PAGE 95

Module 17
                               Use Cases

















96                                                              11 November 2022

### PDF PAGE 96

Use Case                                                    SST


  A kind of case

     Subject of the use case (often the system of interest)

     Objective is to provide value to one or more actor
       ▪ Stakeholders are typically external to the system of interest referred to as actors
     Required actions/steps performed by actors and subject to achieve the objective

     Include use cases are always performed as part of the base use case

     Constraints can specify pre and post conditions




















97                                                                                                        16 January 2023

### PDF PAGE 97

Module 18
                           Analysis Cases

















98                                                            11 November 2022

### PDF PAGE 98

Analysis Case                                                 SST



 A set of steps with an objective to evaluate a
  result about a subject of the analysis

    A kind of behavior

    Each step can be an action, calc, or an
     analysis case that can contain
      ▪ subject
      ▪ objective
      ▪ input and output parameters
      ▪ single return parameter (i.e., the result)
      ▪ attributes bound to calculations and/or
        constraints to be solved by a solver
      ▪ bind parameters to the subject
                                                                          convert to liters / 100 km







99                                                                                                  16 January 2023

### PDF PAGE 99

Trade-off Analysis                                                  SST




  A kind of analysis case

     Trade study objective is to select preferred solution
      that maximizes or minimizes some evaluation function

     Subject of the trade study are the vehicle alternatives
      with different engines
      ▪  Alternatives can be modeled as variants

     Evaluate evaluation function for each alternative
      ▪  Criteria are parameters of evaluation function
      ▪  Each criteria may require separate analysis

     Rationale is a kind of annotation













100                                                                                                   11 November 2022

### PDF PAGE 100

Module 19
                         Verification Cases

















101                                                            11 November 2022

### PDF PAGE 101

Verification               Case                                    SST



 A set of steps with an objective to
  evaluate whether the subject of the
  verification satisfies one or more
  requirements

    A kind of behavior
    Steps typically include collect data,
     process/reduce data, evaluate result
    Subject is an input to the verification                  massReqt.massActual= mass

    Returns a result called a verdict
     whose value is pass, fail, inconclusive,
     or error

    Verify relationship relates
     verification case to requirement

    Verification system interacts with
     subject to perform the verification
     case



 102                                                                                                 11 November 2022

### PDF PAGE 102

Module 20
     Dependency, Allocation, and Cause-Effect
                        Relationships















103                                                    11 November 2022

### PDF PAGE 103

Dependency                                          SST



 A directed relationship where the element on the client end may be impacted
  when the element on the supplier end changes

    Example: Use of dependency to represent traceability between specification
     and source document
    Can have 1.. many clients and 1.. many suppliers


                    supplier


                       dependency


                     client








104                                                                               11 November 2022

### PDF PAGE 104

Allocation                                         SST



 A statement of intent that assigns responsibility
  from one set of elements to another set of elements
    A kind of mapping (1 to n)

    Includes definition and usage
    Can include suballocations                              generateTorque

 Examples

    Actions to components
    Logical components to physical components                                         generateTorque

    Logical connections to physical connections                     The torque generator

    Budget allocation (e.g. weight budget)                     Is allocated to the powertrain,
    Software to hardware                                         and realized by the engine

    Requirements to design elements
    …



 105                                                                                     11 November 2022

### PDF PAGE 105

Cause-Effect Relationship                                        SST



  Single relationship can have multiple causes of multiple effects
  Can logically combine different cause-effect relationships











                                                      Vehicle Thermostat Stuck Closed
                                                      Causes engine to overheat
                                                      Causes vehicle to enter degraded state







106                                                                                     16 January 2023

### PDF PAGE 106

Module 21
                              Annotations

















107                                                              11 November 2022

### PDF PAGE 107

Annotations                                              SST




  An Annotating Element is an Element that is used to provide
   additional information about other elements

    Can be named

    Can apply to 0.. many elements
  An annotation is a kind of relationship that relates the
   annotating element to the element being annotated
  Kinds of annotating elements

    Comment
      ▪ Documentation is an owned comment

    Textual representation (e.g., opaque expression)
      ▪ Includes name of language and body

    Metadata feature
      ▪ Used to add structured metadata





108                                                                                        11 November 2022

### PDF PAGE 108

Metadata                                              SST



 Use metadata to mark elements

    Identify parts that are Security or Safety parts (e.g., members of Security of Safety group)

    Can add additional security and safety information













                           Marked as a security part
                                                                                 Marked a safety part
                                                                            Additional info: isMandatory

109                                                                                         11 November 2022

### PDF PAGE 109

Module 22
                           Element Filters

















110                                                            11 November 2022

### PDF PAGE 110

Element Filters                                          SST



  Used to select elements from a group of elements
    Create a package

    Import the part of the model that contains the elements of interest
     ▪  Use a recursive import to include all nested elements

    Define the filter expression to select the imported elements based on the
     selection criteria











  Filter selects parts marked with Safety metadata

111                                                                                     16 January 2023

### PDF PAGE 111

Module 23
                         View & Viewpoint

















112                                                            11 November 2022

### PDF PAGE 112

View and Viewpoint                                                        SST



  A Viewpoint reflects the concerns of one more stakeholders in terms of what they care
   about relative to a domain of interest
  A View specifies an artifact to present to a stakeholder to satisfy their viewpoint

     Exposes the scope of the model to be viewed

     Filters the model to select a particular subset based on a scope and filter criteria
     Renders the filtered results using a particular presentation form and style

     Intended to support document generation (e.g., OpenMBEE)






                                                         structure







                                                                               Include rendering
                                                                               in view compartment



113                                                                                                 11 November 2022

### PDF PAGE 113

SysML v2 Views and Diagrams                                          SST


 A view is a rendering of a selected model elements based on filter expression and
  exposed elements

    Frame is the view element with view name

    View is defined by a view definition (e.g., diagram kind)

    View content























114                                                                               16 January 2023

### PDF PAGE 114

Standard View Definitions                                         SST
                     (SysML v2 vs SysML v1)
               Baseline as of January 04, 2023





Standard views are normative,
but user defined views are valid
if they are consistent with the
abstract syntax and graphical bnf.



















                                                                             16 January 2023

### PDF PAGE 115

SysML v2 Compartments                                         SST



 Compartments are views of the element represented by the node
 Compartment names represent view definitions
 Standard compartments / view definitions

   Textual view of contained elements of a particular kind (e.g.,
    attributes, actions, ports)
   Textual view of elements at the other end of relationships (e.g.,
    allocation, specialization, …)
 A compartment can also be rendered using graphical notation
 Ports and parameters are connectable nested nodes on the
  boundary of a structure or behavior











 116                                                                                16 January 2023

### PDF PAGE 116

Module 24
                     Language Extension

















117                                                       11 November 2022

### PDF PAGE 117

Language Extension                                                 SST




  Provides ability to extend concepts in
   SysML v2 to address domain-specific
   concepts and terminology
  Define concept by subclassing an
   element in the SysML Model Library
  Define the keyword using metadata                        define the
 state 'failure modes'[*] nonunique;                         concept


 metadata def <fm> ’failure mode’ :> SemanticMetadata  {
         :>> baseType = ‘failure modes’ meta SysML::StateUsage;
  }
  Apply the concept to an element by
   annotating it with the metadata                     apply the concept
  #'failure mode' flatTire;

  #fm flatTire;



118                                                                                           16 January 2023

### PDF PAGE 118

Contrasting SysML v2 with SysML v1


















119                                                     11 November 2022

### PDF PAGE 119

SysML v2 to v1                         SST
              Terminology Mapping (partial)



































120                                                         11 November 2022

### PDF PAGE 120

Contrasting SysML v1 with SysML v2                                                  SST



  Simpler to learn and use                               More expressive

    Systems engineering concepts designed                   Variant modeling
     into metamodel versus added-on                          Analysis case

    Consistent definition and usage pattern                 Trade-off analysis

    More consistent terminology                             Individuals, snapshots, time slices

    Ability to decompose parts, actions, …                  More robust quantitative properties

    More flexible model organization                         (e.g., vectors, ..)
     (unowned members, package filters)…                     Simple geometry
  More precise                                              Query/filter expressions

    Textual syntax and expression language                  Metadata

    Formal semantic grounding                            More extensible
    Requirements as constraints                             Simpler language extension capability

    Reified relationships (e.g., membership,                 ▪ Based on model libraries
     annotation)                                          More interoperable

                                                             Standardized API


121                                                                                      11 November 2022

### PDF PAGE 121

Summary


















122                                                             11 November 2022

### PDF PAGE 122

Summary                                           SST



  SysML v2 is addressing SysML v1limitations to improve MBSE adoption and
   effectiveness

    Precision, expressiveness

    Regularity, usability
    Interoperability with other engineering models and tools
  Approach

    Simplified SysML v2 metamodel with formal semantics overcomes fundamental
     UML limitations

    Flexible graphical notations and textual notation

    Standardized API for interoperability
  Specification submitted to OMG on February 20, 2023

    Will request vote to adopt at March 2023 OMG meeting

    Becomes a beta specification if approved




123                                                                                     07 March 2023

### PDF PAGE 123

References                                         SST



 Monthly Release Repository        (release 2023-02)
    https://github.com/Systems-Modeling/SysML-v2-Release


 SysML v2 Specification (revised submission)

    Note: refer to Annex B for Example Vehicle Model


 Introduction to the SysML v2 Language Textual Notation (release 2021-08)


 Friedenthal S., Seidewitz E., A Preview of the Next Generation System Modeling
  Language (SysML v2), Project Performance International (PPI), Systems
  Engineering Newsletter, PPI SyEN        95 27 November, 2020







124                                                                                   07 March 2023

## LAYOUT-PRESERVING POPPLER EXTRACTION

### LAYOUT PDF PAGE 1

```text
                                                   SST

      Introduction to the SysML v2 Language
                   Graphical Notation
                        (2023-03-07)

         This presentation uses the graphical notation to complement the
         textual syntax (i.e., notation) to represent a SysML model. The
         graphical notation is generated manually with Microsoft Visio.

                     Copyright © 2021, 2022, 2023 by Sanford Friedenthal
       Licensed under the Creative Commons Attribution 4.0 International License.
To view a copy of this license, visit http://creativecommons.org/licenses/by/4.0/ or
sen d a let t er t o Crea t ive Co m m o n s, P O B ox 1866, M o un t a in View, CA 94042, US A.
```

### LAYOUT PDF PAGE 2

```text
                            Agenda                                           SST

 Language Background and Overview
 SysML v2 Functional Areas
 Contrasting SysML v2 with SysML v1
 Summary

Refer to date in lower right on each slide to see when it was last modified  16 January 2023

2
```

### LAYOUT PDF PAGE 3

```text
   General Caveats  SST

 The graphical and textual notation (i.e., syntax) are different renderings of the
  same model
   The textual syntax is formally specified using BNF
   The graphical syntax is formally specified using graphical BNF
   The graphical visualization in this presentation is captured in Visio
   Two visualization prototypes are under development (Tom Sawyer and PlantUML)

 SysML v2 Marker
   Some of the more significant SysML v2 changes in functionality and terminology
    relative to SysML v1 are designated with the SysML v2 marker

3                   07 March 2023
```

### LAYOUT PDF PAGE 4

```text
   Language Background & Overview

4  11 November 2022
```

### LAYOUT PDF PAGE 5

```text
   Systems Modeling Language™                              SST

   (SysML®)

   Supports the specification, analysis, design, and verification and validation
     of complex systems that may include hardware, software, information,
                           processes, personnel, and facilities

    SysML has evolved to address user and vendor needs
      v1.0, adopted in 2006; v1.6, current version; v1.7

    SysML has facilitated awareness and adoption of MBSE

    Much has been learned from using SysML for MBSE

5                                                          07 March 2023
```

### LAYOUT PDF PAGE 6

```text
   SysML v2 Objectives                                         SST

   Increase adoption and effectiveness of MBSE
   by enhancing…

    Precision and expressiveness of the language
    Consistency and integration among language concepts
    Interoperability with other engineering models and tools
    Usability by model developers and consumers
    Extensibility to support domain specific applications
    Migration path for SysML v1 users and implementors

6                                                              11 November 2022
```

### LAYOUT PDF PAGE 7

```text
   Key Elements of SysML v2  SST

 New Metamodel that is not constrained by UML
   Preserves most of UML modeling capabilities with a focus on systems modeling
   Grounded in formal semantics

 Robust visualizations based on flexible view & viewpoint specification
   Graphical, Tabular, Textual

 Standardized API to access the model

7                            11 November 2022
```

### LAYOUT PDF PAGE 8

```text
   SysML v2 Language Architecture                   SST

            Systems Modeling Language               Declarative semantic
                         (SysML)                    base elements and
                                                    domain-specific libraries
   Systems    metamodel                Systems and  modeled using SysML
    Syntax  semantic library          Domain Model
                                                    Declarative semantic
                                         Libraries  base elements modeled
                                                    using KerML
            Kernel Modeling Language
                       (KerML)

   Kernel     metamodel               Kernel Model
   Syntax   semantic library              Library

              semantic                              Direct semantic mapping
            specification                           to formal logic

    Core                                   Core
   Syntax                              Semantics

    Root    Root syntactic elements
   Syntax   without model-level
            semantics (e.g., packaging)

8                                                   07 March 2023
```

### LAYOUT PDF PAGE 9

```text
   SysML v2 API & Services  SST

 Enables other tools and applications to access SysML models in a standard way
 Provides services to:

   Create, update, and delete elements
   Query and navigate model
   Other services including support for model management, analysis,

    transformation, and file export generation
 Supports common patterns called recipes (GitHub - Systems-Modeling/SysML-

  v2-API-Cookbook: Recipes for using the SysML v2 API)
   Navigating a decomposition tree
   Creating a branch
   Query with multiple constraints
 Facilitates use of different implementation technologies such as REST/HTTP,
  Java, or OSLC

9                           11 November 2022
```

### LAYOUT PDF PAGE 10

```text
    Pilot Implementation  SST

    Using Standard API

                             Meta-Model
                          based on KerML

10                        11 November 2022
```

### LAYOUT PDF PAGE 11

```text
    SysML v2 Language                    SST

                       Capabilities

     Behavior          Requirements      Analysis
     - function-based                    - analysis cases
     - state-based       SysML v2        - expression language
     - sequence-based    Language
     - use cases                         Verification
                                         - verification cases
    Structure
    - decomposition
    - interconnection
    - classification

                       View & Viewpoint

11                                       11 November 2022
```

### LAYOUT PDF PAGE 12

```text
    Definition and Usage               SST

    Reuse Pattern

 A definition element defines an element such as a part, action, or requirement
 A usage element is a usage of a definition element in a particular context

   There can be different usages of the same definition element in either different
    contexts or the same context

 Pattern is applied consistently throughout the language

    «usage»                  «usage»
    context1                 context2

    «usage»                  «usage»                  notation
    usage1                   usage2
                                       defined by
                  :
              :

              ««definition»
              DDefinitionA

12                                     11 November 2022
```

### LAYOUT PDF PAGE 13

```text
                SysML v2 Notation (1 of 2)         SST
                   Textual and Graphical
                                                11 November 2022
   package 'Vehicle Parts Tree' {
     part vehicle {
       attribute mass;
       perform providePower;
       part engine {
          attribute mass;
          perform providePower.generateTorque;
          part cylinders [6];
       }
       part transmission {
          attribute mass;
          perform providePower.amplifyTorque;
       }
     }

     action providePower {
       action generateTorque;
       action amplifyTorque;

     }
   }

13
```

### LAYOUT PDF PAGE 14

```text
    SysML v2 Notation (2 of 2)                                                  SST

                    Textual and Graphical

    interface def Drive {
        end enginePort : DrivePort;
        end transmissionPort : ~DrivePort;

    }

    part vehicle : Vehicle {
             part engine : Engine { port drivePort : DrivePort; }
             part transmission : Transmission { port drivePort : ~DrivePort; }

             interface : Drive
                 connect engine.drivePort to transmission.drivePort;

    }

                                               «part»
                                         vehicle : Vehicle

         «part»                  : Drive                   «part»
    engine: Engine                                     transmission :
                                                       Transmission
                    drivePort :           drivePort :
                    DrivePort             ~DrivePort

    Tom Sawyer Visualization Prototype

14                                                                              11 November 2022
```

### LAYOUT PDF PAGE 15

```text
    SysML v2 Spec (Clause 7)        SST

    SysML v2 Language Description

    7.1 Language Overview           7.14 Interfaces
    7.2 Elements and Relationships  7.15 Allocations
    7.3 Dependencies                7.16 Actions
    7.4 Annotations                 7.17 States
    7.5 Namespaces and Packages     7.18 Calculations
    7.6 Definition and Usage        7.19 Constraints
    7.7 Attributes                  7.20 Requirements
    7.8 Enumerations                7.21 Cases
    7.9 Occurrences                 7.22 Analysis Cases
    7.10 Items                      7.23 Verification Cases
    7.11 Parts                      7.24 Use Cases
    7.12 Ports                      7.25 Views and Viewpoints
    7.13 Connections                7.26 Metadata (incl. User Defined Keywords)

15                                  07 March 2023
```

### LAYOUT PDF PAGE 16

```text
                Module 1
    Packages & Element Names

16                            11 November 2022
```

### LAYOUT PDF PAGE 17

```text
                                                                      Model Organization                                                                      SST

 A hierarchy of packages, where packages can contain other packages and elements

 Packages are namespaces that contain member elements that may be owned or unowned

 A package can import members of another package as unowned members, where deletion
  semantics do not apply, and they can be referred to by their local name

     Nested import notation enables flexible organization

    SimSpimlepVlehViechleicMleoMdeoldel

    VVeehhiicclleeCCoonnffiigguurraattiioonnss                                                                            SysML Standard
                                                                                                                               Libraries

    VVeehhiicclleeCCoonnffiigguurraattiioonn__aa                                                              «import»*
                                                                                                                      SI
                                                                         DDeeffiinniittiioonnss                              SysML SI                          KerML
                                                                      VVeehhiicclleeAAnnaallyyssiiss                        Standard                          Libraries
                                                                      VVeehhiicclleeVVeerriiffiiccaattiioonn                Libraries
                                                                                                                                                                 ScalarValues
    VVeehhiicclleeCCoonnffiigguurraattiioonn__bb                                                              «import»*
                                                                                                                                              ISQ              ScalarFunctions

                                                                                                                    ISQ
                                                                                                                                              SI

                                                                                                                                KerML              «import»*
                                                                                                                               Libraries
    RReeqquuiirreemmeennttss                      PPaarrttssTTrreeee                                          ScalarValues
                                                                                                               «import»*              ISQ
                                                                                                                                   ScalarValues

                                                                                                              ScalarFunctions

    AAccttiioonnTTrreeee                          SSttaatteess                                                «import»*

                                                                                                                               ScalarFunctions

17                                                                                                                                                            11 November 2022
```

### LAYOUT PDF PAGE 18

```text
    Import Notation                                                    SST

 no star is element import                                «import»
 single star is package import (content of package)      «import» *
 double star is recursive including outer package        «import» **

 Imports can apply to any namespace, but
  packages are most commonly used

 A package import can include filter criteria to select
  elements based on their metadata

18                                                        11 November 2022
```

### LAYOUT PDF PAGE 19

```text
                      Definitions Package                                    SST

 Example: Definitions package contains packages to define different kinds of
  elements
   Ellipsis indicates there is more content

                                 Definitions

    PartDefinitions            ItemDefinitions       ActionDefinitions

    A tt rib ute De finitions  SignalDefinitions     StateDefinitions

     PortDefinitions           InterfaceDefinitions  RequirementDefinitions

    …

19                                                                           11 November 2022
```

### LAYOUT PDF PAGE 20

```text
                     Package Compartments                    SST

 Packages can include textual compartments
 Filter can be applied to select element kinds

                                                Part
                                           Definitions

                                                members
                                           part def Vehicle
                                           part def Engine
                                           ...

20                                                           16 January 2023
```

### LAYOUT PDF PAGE 21

```text
    Qualified Names                   SST

 A qualified name of a model element is prepended by the name of its owner
  followed by a double colon (::)

 A fully qualified name is prepended by the concatenated names of its owners in
  its containment hierarchy separated by double colons (::)

    A::B::Vehicle  A

                        B

                          «part def»
                            Vehicle

                    «part def»
                   A::B::Vehicle

21                                    11 November 2022
```

### LAYOUT PDF PAGE 22

```text
    Element Names                              SST

 Each element includes a universally unique identifier (UUID) that is not visible
   Managed by the tool
   Does not change over the life of the element

 Each element can include a name
   Required for an element to be referenced in the textual notation

 Each element can optionally include a short name in angle brackets
   Can be a user or tool selected id

 An element can have one or more aliases in the context of a namespace

           «part def»
    Sports Utility Vehicle

                «part def»         «part def»  Note: reserved words can be
    <1.1> Sports Utility Vehicle  «alias» SUV  shown in «guillemet» or bold

               «part def»          «part def»
        Sports Utility Vehicle     alias SUV
    «alias» PartDefinitions::SUV

22                                             11 November 2022
```

### LAYOUT PDF PAGE 23

```text
          Module 2
    Definition Elements

23                       11 November 2022
```

### LAYOUT PDF PAGE 24

```text
Part Definition                                SST

 A Part Definition can contain features such            «part def»
  as attributes, ports, actions, and states                Vehicle
   A modular unit of structure
                                                          attributes
24                                             mass:>ISQ::mass
                                               dryMass
                                               cargoMass
                                               electricalPower
                                               position
                                               velocity

                                               ...acceleration

                                                             ports
                                               pwrCmdPort

                                               ...vehicleToRoadPort

                                                     perform actions
                                               providePower
                                               provideBraking

                                               ...controlDirection

                                                       exhibit states
                                               vehicleStates

                                                                                   11 November 2022
```

### LAYOUT PDF PAGE 25

```text
    Other Kinds of Definition Elements SST

                             Terminology

 Each kind of definition element can contain specific kinds of features

 Attribute definition

    ▪ Data type that defines a set of data values                                                                                                          «attribute def»
    ▪ Primitive attribute definitions include integer, Real, Complex, Boolean, String, ….                                                                        Real

   ▪ Can include quantity kinds such as Torque with units                                                                                                           «attribute def»
   ▪ Can include complex data types such as vectors                                                                                                                      Torque
 Port definition
   ▪ Defines a connection point on parts that enable interactions                                                                                           ~ ~ «port def»
                                                                                                                                                                     FuelCmdPort
                                                                                                                                                                  directed features
                                                                                                                                                           in item fuelCmd:FuelCmd

   ▪ Contain kinds of features including directed features with in, out, and in/out                                                                                    attributes
   ▪ Ports can be conjugated (i.e., reverse direction of directed features)                                                                                x:Real
 Item definition
                                                                                                                                                                      «item def»
                                                                                                                                                                       FuelCmd

    ▪ Defines kind of entity that is acted on, such as an input, output or a stored item                                                                   «item def»
                                                                                                                                                              Fuel

 Action definition                                                                                                                      «action def»
                                                                                                                                       ProvidePower
   ▪ Defines kind of behavior that transforms inputs and outputs
                                                                                                                                         parameters
 State definition                                                                                                          in pwrCmd:PwrCmd
                                                                                                                            out torqueToWheels:Torque [*]
                                                                                                               «state def»

   ▪ Defines kind of behavior that responds to events VehicleStates

    ▪ Enables entry, exit, and do actions         actions
                                           do providePower

25                                                                                                                                                         11 November 2022
```

### LAYOUT PDF PAGE 26

```text
                             Specialization        SST

 Definition elements can be specialized

     Subclass inherits features from its superclass that can be redefined or subsetted

     Subclass can add new features

     Subclass can be a specialization of more than one superclass (i.e., multiple

    inheritance)                     «part def»

                                     Axle

                                       attributes
                             mass

                  inherited            «part def»
                  added                FrontAxle

                                       attributes
                             ^mass
                             steeringAngle

26                                                 11 November 2022
```

### LAYOUT PDF PAGE 27

```text
Redefinition and Subsetting                     SST

 An inherited feature can be redefined by a                             «port def»
  feature whose definition is more specialized                        PwrCmdPort
   The more specialized feature overrides the                      directed features
     inherited feature                                       in item pwrCmd:PwrCmd
   Symbol for redefines (:>>)
                                                                         «port def»
 An inherited feature can be subsetted by one                        FuelCmdPort
  or more features with a more constrained                          directed features
  multiplicity                                  in item fuelCmd:FuelCmd redefines pwrCmd
   The Engine4Cyl contains a subset of the
     cylinders contained by Engine                                «part def»
   First redefine multiplicity to 4                               Engine
   Then identify the subsetting features                            parts
   Symbol for subsets (:>)
                                                  cylinders:Cylinder [4..8]
27
                                                                  «part def»
                                                                Engine4Cyl

                                                                     parts
                                                  cylinders [4] redefines cylinders
                                                  cylinder1 [1] subsets cylinders
                                                  cylinder2 [1] subsets cylinders
                                                  cylinder3 [1] subsets cylinders
                                                  cylinder4 [1] subsets cylinders

                                                                             11 November 2022
```

### LAYOUT PDF PAGE 28

```text
        Module 3
    Usage Elements

28                  11 November 2022
```

### LAYOUT PDF PAGE 29

```text
                                                              Part       SST

 A part is a usage of a part definition

 Part inherits its features from its definition

 Inherited features can be redefined or subsetted, and new features can be added

                                                                     «part»
                                                             vehicle_b:Vehicle

    redefined                                      attributes
    added      mass :>> mass = dryMass+cargoMass+fuelTank.fuel.fuelMass
    inherited  dryMass :>> dryMass=sum(partMasses)

               ... cargoMass :>> cargoMass default 0 [kg]

               partMasses = ( )
               ^electricalPower
               ^position
               ^velocity
               ^acceleration

                                                     ports
               fuelCmdPort:FuelCmdPort :>> pwrCmdPort
               vehicleToRoadPort :>> vehicleToRoadPort

                            wheelToRoadPort1:WheelToRoadPort
                            wheelToRoadPort2:WheelToRoadPort

                                  perform actions

               ^providePower
               ^provideBraking
               ^controlDirection

                                  exhibit states

               ^vehicleStates

                                  parts

               fuelTank:FuelTank

29                                                                       11 November 2022
```

### LAYOUT PDF PAGE 30

```text
    Other Usage Elements                                                     SST

    Terminology

 Other kinds of usage elements are defined by specific kinds of definition
  elements
   Attributes defined by attribute definition
   Ports defined by port definition
   Items defined by item definition
   Actions defined by action definition
   States defined by state definition
  …

30                        11 November 2022
```

### LAYOUT PDF PAGE 31

```text
                   Enumeration                                             SST

 A data type whose range is restricted to a set of discrete values

     Without units                                          «enum def»
      ▪ Definition: enum def Colors {red; blue; green;}         C olo rs
      ▪ Usage: attribute color1: Colors = Colors::blue;
                                                                enums
                                                         red
                                                         blue
                                                         green

     With units:

    ▪ Definition: enum def DiameterChoices :> ISQ::LengthValue {

                       enum = 60 [mm];                        «enum def»
                       enum = 70 [mm];                    DiameterChoices
                       enum = 80 [mm];
                   }                                              enums
                                                         =60 [mm]
                                                         =70 [mm]
                                                         =80 [mm]

    ▪ Usage: attribute cylinderDiameter: DiameterChoices = 80 [mm];

31                                                                   11 November 2022
```

### LAYOUT PDF PAGE 32

```text
                    Usage Elements Defined By                      SST

                    Default Definition Elements

 A definition element is a subclass of the most general definition element in the
  SysML v2 library (e.g., Part)

 A usage element is defined by a definition element

 defined by is a kind of specialization

 A usage element that is not provided a definition by the modeler is a subset of

the most general usage element in the library (e.g., parts)

                    Default part          Default Part Definition

SysML v2              «part»              :           «part def»
 Library            parts [0..*]                         Part

      part without       «part»           defined by  «part def»
        definition     vehicle_b                       Vehicle
                                            :
        part with          «part»
        definition  vehicle_b:Vehicle

32                                                                 11 November 2022
```

### LAYOUT PDF PAGE 33

```text
           Module 4
    Part Decomposition

33                      11 November 2022
```

### LAYOUT PDF PAGE 34

```text
    SysML v1 Decomposition in SysML v2 SST

 defined by relationship is used to create next level of decomposition of a part def

                                                                                      «part def»
                                                                                        Vehicle

         «part»                 «part»                 «part»                «part»                        «part»
    engine:Engine  transmission:Transmission  driveshaft:Driveshaft  rearAxleAssembly              fue lT ank:Fue lTan k

                                                                     :                     defined by

                                                                           «part def»
                                                                     R ear Axle Assem bly

                             «part»               «part»                                   «part»      «part»
                   differential:Differential  rearAxle:Axle
                                                                        rearWheel1:Wheel rearWheel2:Wheel

34                                                                                                     11 November 2022
```

### LAYOUT PDF PAGE 35

```text
                   Parts Decomposition                                                                  SST

 A parts tree is a composition of a part from other parts
   SysML v1 only supports block decomposition
   Definition element can serve as black-box specification without committing to an

     internal structure (e.g., part decomposition)

   Can provide significant advantages (more intuitive, less ambiguous, easier to
    modify a design configuration)

                                                                                         «part»
                                                                                 vehicle_b:Vehicle

         «part»                 «part»                 «part»                              «part»               «part»
    engine:Engine  transmission:Transmission  driveshaft:Driveshaft      rearAxleAssembly:AxleAssembly  fue lT ank:Fue lTan k

    There is no part-to-part                            «part»               «part»     «part»          «part»
         decomposition                        differential:Differential  rearAxle:Axle
           In SysML v1                                                                  rearWheel1:Wheel rearWheel2:Wheel

35                                                                                                      11 November 2022
```

### LAYOUT PDF PAGE 36

```text
          Parts Tree Reuse & Modification SST

                     Subsetting a Part

 A part can be a subset of another part
   Equivalent to specializing a part
   Inherits the part decomposition and other features
   Can modify inherited parts and features through redefinition and subsetting
   Can add new parts

                         subsets

             «part»                                                       «part»
      vehicle_c:Vehicle                                            vehicle_b:Vehicle

             «part»           «part»                 «part»                 «part»                              «part»               «part»
    bodyAssy:BodyAssy    engine:Engine  transmission:Transmission  driveshaft:Driveshaft      rearAxleAssembly:AxleAssembly  fue lT ank:Fue lTan k

                                                                             «part»               «part»     «part»          «part»
                                                                   differential:Differential  rearAxle:Axle
                                                                                                             rearWheel1:Wheel rearWheel2:Wheel

36                                                                                                                           11 November 2022
```

### LAYOUT PDF PAGE 37

```text
                                   References                                                                                 SST

 A part can refer to other parts that are part of another decomposition

     Not composite (i.e., lifetime semantics do not apply)

     Bind the reference usage               «part»
                                   vehicle-trailer-system

                «part»                           «part»                                                       «part»
                vehicle                       trailerHitch                                                    trailer

    reference   «part»    bind                                                                          bind                  reference
               hitchBall
                                =   «part»                                              «part»          =     «part»
                                   hitchBall
                                                                                        trailerCoupler        trailerCoupler

 A part can refer to an item that it stores

                                                                              «part»
                                                                            fue lT ank

                                              «item »
                                                fuel

37                                                                                                                            16 January 2023
```

### LAYOUT PDF PAGE 38

```text
                       Multiplicity                                     SST

 Defines the number of features (e.g., parts) in a particular context
   Defines a range with a lower bound and upper bound
   Lower and upper bounds are integers

     ▪ Can be parameterized [x..y] where x and y are expressions

   Default multiplicity is [1..1]
   Optional multiplicity [0..1]

                                                               «part»
                                                     bodyAssy:BodyAssy

           «part»      «part»            «part»
    doors:Door [2..4]   body   sunroof:Sunroof [0..1]

38                                                                      11 November 2022
```

### LAYOUT PDF PAGE 39

```text
           Module 5
    Part Interconnection

39                        11 November 2022
```

### LAYOUT PDF PAGE 40

```text
                                        Connecting Parts                                                                                              SST

 Parts can be connected via their ports or without ports

    Parts can be connected directly without connecting to the composite part
    Ports can contain nested ports
    Flows can be shown on connections
    References are dashed
    Conjugate port
    Binding connection

 «view» vehicle interconnection

                                                                          «part»
                                                                   vehicle_b:Vehicle

               «part»
       fue lT ank:Fue lTan k

               «item »
              fuel:Fuel

                                                                                                                    «part»
                                                                                                  rearAxleAssembly:AxleAssembly

    p1 : FuelOutPort                                                                                                                «part»            =
                                  fuel

    p2 : ~FuelOutPort

    =                                                                                                                               rearWheel1:Wheel

       «part»                                        «part»                 «part»        «part»                     «part»
                                        transmission:Transmission  driveshaft:Driveshaft
       engine:Engine                                                                      differential:Differential  rearAxle:Axle                    =
                                                       «part»
                                                vehicleSoftware                                                                     «part»

                                                       «part»                                                                       rearWheel2:Wheel
                                                vehicleController
       engineStatus

40                                                                                                                                  11 November 2022
```

### LAYOUT PDF PAGE 41

```text
                              Interfaces                             SST

 A connection definition connects two usage elements (e.g., two parts)
 An interface definition is a connection definition whose ends are compatible ports

   Can contain flows
   Can contain other kinds of features
 An interface defined by an interface definition is used to connect ports
   Ports on parts must be compatible with the interface definition

          «interface def»             «part»
     Fue lT ank ToEngine_ IF  fue lT ank:Fue lTan k

                 ports                «item »
    : FuelOutPort                    fuel:Fuel
    : ~ FuelOutPort
                                        p1 : FuelOutPort  fuel:Fuel
              item flows      :FuelTankToEngine_IF
    :Fuel
                              p2 : ~FuelOutPort

                                                   «part»
                                              engine:Engine

41                                                                   11 November 2022
```

### LAYOUT PDF PAGE 42

```text
                                Interface                                                               SST

    Connecting a Wheel to a Hub

 Usage of WheelToHub interface definition specifies a compatible connection between a wheel and a hub
    Connects composite ports on wheel and hub
    Decomposes into 5 Wheel Fastener interfaces

 Wheel Fastener interface species a compatible connection between a lugnut and shank
    Contains features needed for a compatible connection

        «part»                  wheelHub_IF : WheeltoHub_IF                    «part»
    wheel:Wheel                                                               hub:Hub
                                lugNutCompositePort:  shankCompositePort:
                                LugNutCompositePort   ShankCompositePort

                «port def»                                  «interface def»               «port def»
      LugN ut Compo site Po rt                             W hee lt oHu b_IF     Shan kC omposite Port

                   ports                                          ports                      ports
    lugNutPort:LugNutPort [*]   lugNutCompositePort:LugNutCompositePort [1]   shankPort:ShankPort [*]
                                shankCompositePort::ShankCompositePort [1]
                «port def»                                                                «port def»
              LugNutPort                                       interfaces                Shan kPort
                                wheelFastener_IF : WheelFastener_IF [5]                   attributes
                attributes      connect lugNutCompositePort.lugNutPort to     threadDia = 14 [mm]
    threadDia = 14 [mm]         shankCompositePort.shankPort                  threadPitch = 1.5 [mm]
    threadPitch = 1.5 [mm]                                                    shaftLength = 70 [mm]
                                                       «interface def»
                                                    WheelFastener_IF

                                                              ports
                                              lugNutPort:LugNutPort
                                              shankport:ShankPort

                                                           attributes
                                              maxTorque = 90 [ft-lbs]

                                                          constraints
                                              {lugNutPort.threadDia ==
                                              shankPort.threadDia}

42                                                                                                      11 November 2022
```

### LAYOUT PDF PAGE 43

```text
    Wheel Hub Interface                                                         SST

 Usage of WheelHubInterface to specify interface between rear axle and wheels

                                                     «interface def»
                                                    W hee lt oHu b_IF

                                                            ports
                         lugNutCompositePort:LugNutCompositePort [1]
                         shankCompositePort::ShankCompositePort [1]

                                                        interfaces
                         wheelFastener_IF : WheelFastener_IF [5]
                         connect lugNutCompositePort.lugNutPort to
                         shankCompositePort.shankPort

                                 «interface def»
                              WheelFastener_IF

                                        ports
                         lugNutPort:LugNutPort
                         shankport:ShankPort

                                     attributes
                         maxTorque = 90 [ft-lbs]

                                    constraints
                         {lugNutPort.threadDia ==
                         shankPort.threadDia}

43                       11 November 2022
```

### LAYOUT PDF PAGE 44

```text
    Nested Wheel Hub Interface  SST

44                              11 November 2022
```

### LAYOUT PDF PAGE 45

```text
    Module 6
    Variability

45               11 November 2022
```

### LAYOUT PDF PAGE 46

```text
                                        Variability                                                 SST

 Vehicle family is the superset model (150%)
 Variation points represent elements that can vary

   Can be applied to all definition and usage elements
 A variant represents a particular choice at a variation point
 A choice at one variation point can constrain choices at other variation points
 A system can be configured by making choices at each variation point

                                                                             «part»
                                                                        vehicleFamily

                ««vvaarriiaattiioonn»»                «variation»
                   ««ppaarrtt»»                          «part»
                  eennggiinnee
                                                     transmission

     «variant»   «variant»                   «variant»           «variant»
       «part»      «part»                      «part»              «part»

    engine4cyl  engine6cyl              transmissionAuto  transmissionManual

                                                                 constraints
    engine==engine::engine4cyl xor (engine==engine::engine6cyl and transmission==transmissionAuto)

46                                                                 11 November 2022
```

### LAYOUT PDF PAGE 47

```text
    Selected Vehicle Configuration                    SST

 Vehicle_a subsets vehicleFamily to represent a particular design configuration
 Selected parts must satisfy variability constraints

   Model is inconsistent if constraints are not satisfied
   Variability modeling applications can automate the selection of valid configurations

                                                                     «part»
                                                                vehicleFamily

      «part»
    vehicle_a

            «part»                      «part»
    engine=engine6cyl  transmission=transmissionAuto

47                                                    11 November 2022
```

### LAYOUT PDF PAGE 48

```text
    Behavior

48            11 November 2022
```

### LAYOUT PDF PAGE 49

```text
    Module 7
     Actions

49            11 November 2022
```

### LAYOUT PDF PAGE 50

```text
                            Actions                                SST

 Actions are defined by action definitions
   Inherit features (e.g., input and output parameters)
   Can redefine or subset inherited features or add new features

       «action»                    :   «action def»
    providePower                      ProvidePower

                   parameters                      parameters
    in fuelCmd:FuelCmd :>> pwrCmd     in pwrCmd:PwrCmd
    ^out torque [*]                   out torque:Torque [*]

50                                                                 11 November 2022
```

### LAYOUT PDF PAGE 51

```text
                  Action Decomposition                                                      SST

 Actions can be decomposed in a similar way as parts

                                                                 «action»
                                                              providePower

         «action»      «action»            «action»                             «action»
    generateTorque  am plifyTo rq ue  distributeTorque                      transferTorque

51                                                                          11 November 2022
```

### LAYOUT PDF PAGE 52

```text
                                                   Part Performs Actions                               SST

 A part that performs an action can reference an action in an action tree
 This is done through reference subsetting

                  «part»                                           ::     «action»
          vehicle_b:Vehicle                                            providePower

                 perform                                «action»      «action»            «action»         «action»
pprroovvidePowweerr                                generateTorque  am plifyTo rq ue  distributeTorque  transferTorque
provideBraking
controlDirection

                 «part»
            engine:Engine

                perform
pprroovviidePoweerr..ggeenneerarateteTToorqrquuee

52                                                                                                     07 March 2023
```

### LAYOUT PDF PAGE 53

```text
    Perform Action  SST

 Show two kinds
   perform action1
   perform action action1

 The difference between these two is as follows
   Line with arrow
     part part1 {perform action1} (example from previous slide)
     this creates an anonymous reference feature that subsets action1 which is often in a
     separate action tree. Name is properly qualified such as package1::action1). This is
     like a call action.
   Line with white diamond
     part part1 {perform action action1}
     This creates an explicit reference feature called action1 that can either subset or bind
     to another action

   This pattern is repeated for many different kinds of features.

53                  11 November 2022
```

### LAYOUT PDF PAGE 54

```text
                                                       Perform Action                       SST
                                                       Simple Example

    package PerformActions{                                              «part»
      part part0{                                                        part0
         perform action action1;
         perform action2;                              «perform action»          «perform»
      }                                                      action1               action2
      action action2;
                                                       Alternatives
    }
                                                                                 «part»
                                               «part»                            part0
                                                part0

    «perform action»   «perform action»                «perform action»                     «perform action»
          action1     references action2                     action1                            ::> action2

54                                                                                                         07 March 2023
```

### LAYOUT PDF PAGE 55

```text
     Module 8
    Action Flow

55               11 November 2022
```

### LAYOUT PDF PAGE 56

```text
                           Action Flow                                                                                   SST

 Actions can include successions and input/output flows
 Control nodes include decision, merge, fork, and join nodes
 Actions can include send and accept actions
 Swimlanes represent performers of actions

                                                                                       «perform action»
                                                                                         providePower

                                                                                                                         =

=  «perform»                 «perform»           «perform»                                               «perform»
                           am plifyTo rq ue  distributeTorque
   generateTorque                                                                                        transferTorque  =

           «perform»
             trigger1

«accept» es:EngineStarted

   Note: Parameter notation subject to change                                                                            16 January 2023

56
```

### LAYOUT PDF PAGE 57

```text
                               Input/Output Flows                                  SST

 A flow is a kind of connection that transfers items from a source output to a
  target input
   A flow is a transfer that continues while the source and target actions execute
    (this is the default)
   A succession flow is a transfer that only occurs after the source action ends and
    before the target action starts

                                                                                         «perform action»
                                                                                           providePower

                                                                                   =

    =  «perform»                 «perform»           «perform»     «perform»
                               am plifyTo rq ue  distributeTorque
       generateTorque                                              transferTorque  =

               «perform»
                 trigger1

    «accept» es:EngineStarted

57                                                                                 16 January 2023
```

### LAYOUT PDF PAGE 58

```text
                                        Controlling Actions [1]                                                                                          SST

 A start action and done action represent the start and end of an action sequence

 A succession asserts that the target action can start execution only after the
  source action ends execution

 A conditional succession asserts that the target action can start only if the guard
  condition is true (if…then). If the guard is false, the target action cannot start

                                                                           «action»
                                                                    transportPassenger

                          «action»      «action»                    «action»                   «action»              «action»      [vehicleStarted]

                          unlockDoor    openDoor                    enterVehicle               closeDoor             startVehicle

    start

                   fork1    «action»    join1
    merge1                driveVehicle
                                                          «action»
                                                          openDoor                 «action»                «action»                «action»  decision1
                                                                                  exitVehicle             closeDoor                lockDoor             [else]

                             «action»                                                                                                                           done
                          providePower
                                                                                                                                   [anotherDestination]

58                                                                                                                                           11 November 2022
```

### LAYOUT PDF PAGE 59

```text
                                        Controlling Actions [2]                                       SST

 Control nodes are kinds of actions (with names) that control outgoing
  successions in response to incoming successions

 Decision node

    ▪ 1 incoming succession and 1.. many outgoing successions

    ▪ One outgoing succession is selected based on the guard condition that is
      satisfied (“else” condition is the complement of all other guard conditions)

 Merge node

    ▪ 1.. many incoming successions and 1 outgoing succession                                                     [vehicleStarted]

    ▪ The outgoing succession occurs when any of its incoming successions occur

                   fork1    «action»    join1
    merge1                driveVehicle
                                                          «action»
                                                         openDoor    «action»     «action»  «action»  decision1
                                                                    exitVehicle  closeDoor  lockDoor             [else]

                             «action»                                                                                    done
                          providePower
                                                                                            [anotherDestination]

59                                                                                                    11 November 2022
```

### LAYOUT PDF PAGE 60

```text
                                        Controlling Actions [3]                                                   SST

     Fork node
      ▪ 1 incoming succession and 1.. many outgoing successions
      ▪ All outgoing successions occur when its incoming succession occurs

     Join node
      ▪ 1.. many incoming successions and 1 outgoing succession
      ▪ Outgoing succession occurs when all its incoming successions occur

      Note: Control nodes cannot currently be applied to input/output flows

                   fork1    «action»    join1
    merge1                driveVehicle
                                                          «action»
                                                         openDoor    «action»     «action»  «action»  decision1
                                                                    exitVehicle  closeDoor  lockDoor             [else]

                             «action»                                                                                    done
                          providePower
                                                                                            [anotherDestination]

60                                                                                                    11 November 2022
```

### LAYOUT PDF PAGE 61

```text
    Controlling Actions [4]                                                                              SST

 startVehicle subsets startVehicle1 behavior                    ` «perform action»
   which is independent of structure
                                                              startVehicle :> startVehicle1
 Event occurrences
 Accept actions and send actions              driver:Driver                       vehicle:Vehicle

    When a send action executes, it             «event»                                       «event»
      transfers an item to a target part       driverReady                                   doorClosed

    When a triggering input item is                     «perform»                           «perform»
      received, an accept action executes             turnVehicleOn
      and can transfer the input item to                                                `trigger1
      another action                                     «send» vs
                                                                  vs:VehicleStart  «accept» vs:VehicleStart
 driver and vehicle are in a shared
  context (not shown)                                    «perform»                                    vs
                                                           trigger2                                   vs:VehicleStart

                                               «accept» es:EngineStatus                      «perform»
                                                                                            startEngine

                                                                                                      es.EngineStatus
                                                                                                      es:EngineStatus

                                                                                             «perform»
                                                                                            sendStatus
                                                                                            «send» es

61                                                                                                       16 January 2023
```

### LAYOUT PDF PAGE 62

```text
   Scenario_1o                                                                                                                               SST
Textual Notation
                                                                                                                                           16 January 2023
package Scenario_1o{                                                      part def Driver{
         item def VehicleStart;                                             port p1;
         item def EngineStatus;                                             port p2;

         action startVehicle1{                                            }
            event occurrence doorClosed;                                  part def Vehicle{
            event occurrence driverReady;
            first doorClosed then driverReady;                              port p1;
            first driverReady then turnVehicleOn;                         }

            action turnVehicleOn send vs via source{                      part part0{
              in vs:VehicleStart;                                           perform action startVehicle:>startVehicle1{
              in source default self;                                          action :>> turnVehicleOn send vs via source{
                                                                                 in :>> source = driver.p1;
            }                                                                  }
            action trigger1 accept vs:VehicleStart;                            action :>> trigger1 accept vs:VehicleStart via vehicle.p1;

            flow of VehicleStart from trigger1.vs to startEngine.vs;           action :>> sendStatus send es via source{
            action startEngine{                                                  in es:EngineStatus;
                                                                                 in :>> source = vehicle.p1;
              in item vs:VehicleStart;
              out item es:EngineStatus;                                        }
            }                                                                  action :>> trigger2 accept es:EngineStatus via vehicle.p1;
            flow of EngineStatus from startEngine.es to sendStatus.es;
                                                                            }
            action sendStatus send es via source{                           part driver : Driver {
              in es:EngineStatus;
              in source default self;                                          perform startVehicle.turnVehicleOn;
                                                                               perform startVehicle.trigger2;
            }                                                                  event startVehicle.driverReady;
            action trigger2 accept es:EngineStatus;                         }
                                                                            part vehicle : Vehicle {
            message of VehicleStart from turnVehicleOn to trigger1;            perform startVehicle.trigger1;
            message of es:EngineStatus from sendStatus to trigger2;            perform startVehicle.startEngine;
         }                                                                     perform startVehicle.sendStatus;
                                                                               event startVehicle.doorClosed;
62                                                                          }
                                                                            interface driver.p1 to vehicle.p1;
                                                                            interface driver.p2 to vehicle.p1;
                                                                          }
                                                                        }
```

### LAYOUT PDF PAGE 63

```text
    Module 9
     States

63            11 November 2022
```

### LAYOUT PDF PAGE 64

```text
    States                                                 SST

 States can be defined by state definitions
   Inherit features (e.g., actions, nested states, transitions) from its state definition
   Can redefine or subset inherited features or add new features

                «state»      ::   «state def»
            vehicleStates        VehicleStates

            state actions                   state actions
    entry ^action1               entry action1
    do action2' :>> action2      do action2
    exit action3

64                                                         07 March 2023
```

### LAYOUT PDF PAGE 65

```text
             State-based Behavior [1]                                                                SST

 States decompose into nested states (without regions, which were in SysML v1)
   A parallel state decomposes into concurrent states
   A non-parallel state (default) decomposes into sequential/exclusive states

 Transitions between sequential states
   Triggered by events
   Can include guard and action

                                                      «state»
                                                  vehicleStates

                                                    «parallel»

                  «state»                                                    «state»
             operatingStates                                              healthStates

    «state»    vehicelOff                «state»                 «state»                   «state»
       off                                  on                   normal                 maintenance

    vehicleStart
    [brakePedalDepressed]
    / send engineHealthStatus to driver

             «state»          [vehicleStarted]                             «state»
             starting                                                     degraded

65                                                                                                   07 March 2023
```

### LAYOUT PDF PAGE 66

```text
    State-based Behavior [2]                                           SST

 States can have entry, exit, and do actions that can refer to actions in action
  trees or be defined locally

 States can include constraints

                  «state»
             operatingStates

    «state»  vehicleOff                                   «state»
       off                                                   on

    vehicleStart                                    state actions
    [brakePedalDepressed]                entry performSelfTest
    / send engineHealthStatus to driver  do providePower
                                         exit applyParkingBrake

                                                   assert constraints
                                         {electricalPower <= 500 [W]}

                                 «state»            [vehicleStarted]
                                 starting

                             state actions
             do startEngine
             exit send engineStartStatus to driver

66                                                                     07 March 2023
```

### LAYOUT PDF PAGE 67

```text
                           Part Exhibits States                                                                        SST

 A part exhibits states
 Owns its state-based behavior

                «part»                   «state»                                     «state»                «state»
        vehicle_b:Vehicle           operatingStates                              vehicleStates           healthStates

                actions    «state»    vehicelOff                                    «parallel»  «state»                   «state»
    perform providePower      off                                                               normal                 maintenance
                                                                «state»
          perform actions                                          on
    applyParkingBrake
    performSelfTest        vehicleStart
                           [brakePedalDepressed]
           exhibit states  / send engineHealthStatus to driver
    vehicleStates
                                    «state»          [vehicleStarted]                                     «state»
                                    starting                                                             degraded

67                                                                                                                     07 March 2023
```

### LAYOUT PDF PAGE 68

```text
     Module 10
    Interactions

68                11 November 2022
```

### LAYOUT PDF PAGE 69

```text
    Sequence View                                  SST

 Represents an event sequence and messages (refer to action flow on slide 62)
   Event sequence
   Message
   Driver and vehicle are in a shared context (not shown)

        «part»                          «part»
    driver:Driver               vehicle_b:Vehicle

      .                        .

            .driverReady  .doorClosed

     vs:VehicleStart

                              «perfrom»
                             startEngine
    es:EngineStatus

69                                                 16 January 2023
```

### LAYOUT PDF PAGE 70

```text
    Module 11
    Individuals

70               11 November 2022
```

### LAYOUT PDF PAGE 71

```text
                   Individuals                                          SST

 An individual definition is a unique member of a class with identity
   A specialization of a class, having only one member
   Has a unique lifetime

 An individual is a usage that is defined by an individual definition
   Can subset a part to represent a particular configuration
   Can have different configurations across Vehicle-1 lifetime

         «part»           «part»          :  «part def»
    engine:Engine  vehicle_b:Vehicle          Vehicle

                                                       attributes
                                             vin:Integer
                                             mass

                         «individual»     :  «Individual def»
                   vehicle_b-1:Vehicle-1         Vehicle-1

                                                       attributes
                                             vin :>> vin = 1
                                             ^mass

71                                                                      11 November 2022
```

### LAYOUT PDF PAGE 72

```text
           Module 12
    Timeslices & Snaphots

73                         11 November 2022
```

### LAYOUT PDF PAGE 73

```text
    4D Model & Occurrences  SST

 Each entity called an occurrence has a lifetime

   Distinct from attributes which do not have a lifetime
   Includes a reference clock that can quantify time (defaults to universal clock)
   Can specify time slices and snapshots

 Spatial items are kinds of occurrences that have spatial extent that can change
  over their lifetime

   Specified by shapes with position and orientation within coordinate frames

 Individuals

   Unique occurrence with a lifetime

74                          11 November 2022
```

### LAYOUT PDF PAGE 74

```text
    Lifetime with                                                                    SST

    Snapshots and Time Slices

 Each individual definition has a unique lifetime             «Individual def»
   Begins when it is created                                      Vehicle-1
   Ends when it is destroyed                                      attributes

 Individual usage exists over some portion of          vin :>> vin = 1
  Vehicle-1 lifetime                                    ^mass

 Individual lifetime can be segmented into time                   «individual»
  slices (i.e., durations of time)                          vehicle_b-1:Vehicle-1

 A time slice whose duration is zero is a snapshot                «timeslice»
   Beginning and ending snapshot of a time slice is     vehicle_b-t0->t1:Vehicle-1
     designated as start and done snapshot
                                                                    attributes
 The condition of an individual for a time slice or   ^vin = 1
  snapshot can be specified in terms of the values of
  its features                                                     «snapshot»                  «snapshot»
                                                           vehicle_b-t0:Vehicle-1      vehicle_b-t1:Vehicle-1

                                                                    attributes                  attributes
                                                       tstart = 0 [min]            tdone =1 [min]
                                                       ^vin = 1                    ^vin = 1
                                                       mass = 1550 [kg]            mass = 1549.9 [kg]
                                                       position = 0 [m]            position = 1 [km]
                                                       velocity = 60 [km/hr]       velocity = 60 [km/hr]
                                                       acceleration = 0            acceleration = 0

75                                                                                 11 November 2022
```

### LAYOUT PDF PAGE 75

```text
             Individuals Playing Different Roles SST

 An individual can play different roles and have different configurations in different time slices
     ▪ Individual wheel (Wheel-1) is left front wheel during vehicle_b_t1-t2 time slice
     ▪ Individual wheel (Wheel-1) is right front wheel during vehicle_b_t2-t3 time slice

                                                 «part»
                                          vehicle_b:Vehicle

part               «part»                                                  «part»
             leftFront:Wheel                                        rightFront:Wheel

  redefine                                      «indvidual»
Individual time slice                     vehicle_b-1:Vehicle-1

                                  «timelice»         «timeslice»                         temporal
                              vehicle_b_t1->t2    vehicle_b_t2->t3                    decomposition

 individual               «individual»                               «individual»      individual
                       leftFront:Wheel-1                         rightFront:Wheel-1
76                                                                                    11 November 2022
                                  «individual»
                              rightFront:Wheel-2

                                                   «individual»
                                                leftFront:Wheel-2
```

### LAYOUT PDF PAGE 76

```text
                Module 13
    Expressions and Calculations

77                                11 November 2022
```

### LAYOUT PDF PAGE 77

```text
    Expressions  SST

 Used to compute a result
 Library of mathematical functions (e.g., sum, max, …)

   Includes arithmetic operators that also apply to vectors and tensors
 Default value means value can be over-ridden using redefinition

                                                                                      «part»
                                                                               vehicle_b:Vehicle

                                                                                    attributes
mass ::>> mass=dryMass+cargoMass+fuelTank.fuel.fuelMass
dryMass :>> dryMass=sum(partMasses)
cargoMass :>> cargoMass default 0 [kg]
partMasses=(fuelTank.mass,frontAxleAssembly.mass,rearAxleAssembly.mass,engine.mass,transmission.mass,driveshaft.mass)

78               11 November 2022
```

### LAYOUT PDF PAGE 78

```text
                                Calculations                     SST

 A kind of behavior generally used to represent reusable mathematical functions

     Inputs                                 «calc def»
     Expression                                Force
     Returns a single result
                                            parameters
       ▪ Can have multiplicity  in m :> ISQ::mass
                                in a :> ISQ::acceleration
                                return f :> ISQ::force = m*a

 Represent a calculation definition using the textual notation
    calc def Force {
         in attribute m:>ISQ::mass;
         in attribute a:>ISQ::acceleration;
         return f :>ISQ::force = m * a;
    }

79                                                               11 November 2022
```

### LAYOUT PDF PAGE 79

```text
                                  Calculations                 SST

 Evaluate usage
   Bind values to input parameters. Then evaluate expression and return a result
   calc force : Force {

        in m=1500 [kg];
        in a=9.806 [m/s^2];
     }

 Can bind a calc return value to an attribute
   attribute f1 = Force (m=1500 [kg] , a = 9.806 [m/s ^2]);

                 «calc def»                     «calc»
                    Force                    force:Force

                parameters                   parameters
    in m :> ISQ::mass             in m=1500 [kg]
    in a :> ISQ::acceleration     in a=9.806 [m/s^2]
    return f :> ISQ::force = m*a  ^return :> ISQ::force = m*a

80                                                             16 January 2023
```

### LAYOUT PDF PAGE 80

```text
    Binding Connection  SST

 A binding is a kind of connection where both sides of the connection are asserted
  to be equal at all times
   Symbol is «bind» or =
   If both sides are not equal, the model is inconsistent (e.g., 3=4) is inconsistent
   A tool could make both sides equal if the values are not the same
     ▪ In the above example, the values can be set to (3=3) or (4=4)
     ▪ For y = x+3, when x is 1, then y can be set to 4 so that both sides are equal
   Different from the Boolean operator ‘==’, which evaluates whether both sides
    of the ‘==’ have the same value or not, and returns a value of true or false
    (e.g., {3==4} returns a value of false)

 Binding can be used to establish equality of any kind of feature
   A part can be bound (e.g., engine = engine4cyl)
   A port on a composite part can be bound to a port on a nested part to
    constrain them to have equal values

81                      16 January 2023
```

### LAYOUT PDF PAGE 81

```text
         Module 14
    Quantities & Units

82                      11 November 2022
```

### LAYOUT PDF PAGE 82

```text
    Quantities and Units  SST

 Quantity is an attribute (e.g., mass)
 Quantity is defined by an attribute def of a quantity kind (e.g., MassValue)
 Units conform to the quantity kind (e.g., kilograms conform to MassValue)
 The values are associated with the units
 A change in a unit can apply the unit conversion factor if a tool supports this

   attribute m:MassValue = 25 [kg] (an equivalent value to 55.1 [lbs])
   In SysML v1, a change in unit requires a change in the value type

 Complex quantities and units can be derived from primitive quantities and units

   distancePerVolume :> scalarQuantities = distance / volume

 Libraries
   International System of Quantities (ISQ)
   International System of Units (SI)
   US Customary Units (USCustomaryUnits)

83                        11 November 2022
```

### LAYOUT PDF PAGE 83

```text
    Module 15
    Constraints

84               11 November 2022
```

### LAYOUT PDF PAGE 84

```text
    Constraint Expression [1]                                           SST

 A Boolean expression that evaluates to true or false, which includes

 Constraint operators (==), (>), (>=), (<), (<=), (!=)

    ▪ Used to compare expressions (e.g., {a < b})

 Boolean operators include and, or, xor, not

    ▪ Used to logically combine expressions (e.g., {A and B or C})

 Asserting a constraint to be true means the evaluation must be true
  for the model to be consistent

part def FuelTank {                                                       «part def»
         attribute mass :> ISQ::mass;                                      FuelTank
         ref item fuel:Fuel{                                               attributes
           attribute redefines fuelMass;                 fue lM assMa x
         }
         attribute fuelMassMax:>ISQ::mass;                           assert constraints
         assert constraint {fuel.fuelMass<=fuelMassMax}  {fuel.fuelMass <= fuelMassMax}

}                                                                           «item »
                                                                           fuel:Fuel

85                                                                      11 November 2022
```

### LAYOUT PDF PAGE 85

```text
    Constraint Expression [2]                                               SST

 Usage inherits constraint expression and redefines constraint parameters

                     «part def»                         «part»
                      FuelTank                 fue lT ank:Fue lTan k
                      attributes
    fue lM assMa x                                    attributes
                                    :>>fuelMassMax = 60 [kg]
                assert constraints
    {fuel.fuelMass <= fuelMassMax}              assert constraints
                                    ^{fuel.fuelMass<=fuelMassMax}
                       «item »
                      fuel:Fuel                         «item »
                                                    fuel1:>>fuel

86                                  11 November 2022
```

### LAYOUT PDF PAGE 86

```text
Constraint Definition                                     SST

 Enables reuse of a constraint expression
 Default parameter direction is ‘in’
 Can assert a constraint on the usage
 Bind parameters on the usage
 Can mark dependent parameters as derived with slash

                                        «constraint def»                  «assert constraint»
                                    StraightLineDynamics              sld:StraightLineDynamics

                                           parameters                           parameters
                      power :> ISQ::power                 power = vehicle_b.engine.peakHorsePwr
                      m :> ISQ::mass                      m=vehicle_b.mass
                      delta_t :> ISQ::time                delta_t = 0.1 [s]
                      x_in :> ISQ:: length                x_in = vehicle_b.position
                      v_in:>ISQ:: speed                   v_in = vehicle_b.speed
                      x_out :> ISQ::length                /x_out = position_delta_t
                      v_out :> ISQ::speed                 /v_out = speed_delta_t
                      a_out :> ISQ::acceleration          /a_out = acceleration

                                            expression                                                                   16 January 2023
                      a_out == power/(mass*v_avg) and
                      v_out == v_in +a_out*delta_t and
                      x_out == x_in+v_avg*delta_t

87
```

### LAYOUT PDF PAGE 87

```text
                    Binding Constraints      SST

 Equivalent to SysML v1 parametric diagram

88                                           11 November 2022
```

### LAYOUT PDF PAGE 88

```text
      Module 16
    Requirements

89                11 November 2022
```

### LAYOUT PDF PAGE 89

```text
    Requirement Definition  SST

 A constraint definition that a valid design solution must satisfy that can include:
   Identifier
   Shall statement
   Constraint expression that can be evaluated to true or false
      ▪ can apply to performance, functional, interface and other kinds of requirements if desired
   Assumed constraint expression that is asserted to be true for the requirement to be valid
   Attributes of the constraint expressions

                                                                               «requirement def»
                                                                          <1_1> MassRequirement

                                                                                         doc
                                                                The actual mass shall be less than the
                                                                required mass.

90                          16 January 2023
```

### LAYOUT PDF PAGE 90

```text
    Requirement Specification                                                                 SST

 A tree of requirements that contains nested requirement usages

     Composite requirement can own or reference other requirements

     Subject of nested requirements is the kind of entity being specified

     Requirement features can redefine features of the requirement definition

composite requirement                         «requirement»
           subject                         vehicleSpecification
                                            subject v:Vehicle

                     «requirement»         reqt id                          «requirement»
        <1> massReqt:MassRequirement                             <2> fuelEconomyRequirements

                             doc
    The actual vehicle mass shall be less
    than the required vehicle mass.

                                                           «requirement»                          «requirement»
                                           <2_1> city:FuelEconomyRequirementl  <2_2> highway:FuelEconomyRequirement

                                           assumption

91                                                                                            16 January 2023
```

### LAYOUT PDF PAGE 91

```text
Satisfying a Requirement                                                SST

 The vehicleSpecification imposes constraints on the vehicle
   The modeler can assert the vehicle mass satisfies the massRequired
     ▪ Bind the vehicle mass to massActual of the requirement

                         «requirement»
                      vehicleSpecification
                       subject v:Vehicle

                          «requirement»                                 «part»
             <1> massReqt:MassRequirement                        vehicle_b:Vehicle

                                  doc                                 attributes
        The actual vehicle mass shall be less  :>>mass = dryMass + fluidMass
        than the required vehicle mass.        :>>dryMass=sum(partMasses)

                             constraints       … :>>fluidMass = 36 [kg]
        ^require {massActual<=massRequired}
        assume {massFluid<=40 [kg]}                                 requirements
                                               satisfy vehicleSpecification
92
                                                            massReqt.massActual = mass
                                                            massReqt.massFluid = fluidMass

                                                                                                         16 January 2023
```

### LAYOUT PDF PAGE 92

```text
                        Satisfying a Requirement  SST

                        Alternative Notation

 Alternative notation

                          «requirement»                          «part»
                       vehicleSpecification               vehicle_b:Vehicle
                        subject v:Vehicle
                                                               attributes
                          «requirement»        :>>mass = dryMass + fluidMass
             <1> massReqt:MassRequirement
                                               ...
                                  doc
        The actual vehicle mass shall be less                  «satisfy»
        than the required vehicle mass.         vehicleSpecification.massReqt

                             constraints                                                       07 March 2023
        ^require {massActual<=massRequired}
        assume {massFluid<=40 [kg]}

93
```

### LAYOUT PDF PAGE 93

```text
Requirement Allocation vs.                                                                         SST
Requirement Satisfaction

 Allocating a requirement assigns responsibility for realizing a requirement

 Less formal than requirement satisfaction (no explicit constraint assertion)

 Can be decomposed                                                                   «part»
                                                                             specificationContext

                «requirement»                                                  «allocate»                                   «part»
            vehicleSpecification                                                                                     vehicle_b:Vehicle
              subject v:Vehicle                                              «allocate»
                                                                                                                          attributes
                  «requirement»                                                                    :>>mass = dryMass+fluidMass
    <1> massReqt:MassRequirement                                                                   :>>dryMass=sum(partMasses)

                         doc                                                                       … :>>fluidMass = 36 [kg]
The actual vehicle mass shall be less
than the required vehicle mass.                                                                                         requirements
                                                                                                   satisfy vehicleSpecification

                                                                                                                massReqt.massActual = mass
                                                                                                                massReqt.massFluid = fluidMass

                                                             constraints                           16 January 2023
                                        ^require {massActual<=massRequired}
                                        assume {massFluid<=40 [kg]}

94
```

### LAYOUT PDF PAGE 94

```text
                          Derived Requirement                                                SST

 Single original requirement with one or more

    derived requirements                                                   «requirement»
                                                                        engineSpecification

 If the original requirement is satisfied, then all the

    derived requirements must be satisfied               #d erive                    «requirement»
                                                                        <2> massReqt:MassRequirement
                                    «requirement»
                                vehicleSpecification                                        doc
                                                                   The actual engine mass shall be less
                                                                   than the required engine mass.

                      «requirement»        #o rig ina l
        <1> massReqt:MassRequirement
                                                         «#derivation»
                             doc
    The actual vehicle mass shall be less                                      «requirement»
    than the required vehicle mass.                                     transmissionSpecification

                                                         #d erive                    «requirement»
                                                                       <3> massReqt:MassRequirement

                                                                                            doc
                                                                   The actual transmission mass shall be
                                                                   less than the required transmission
                                                                   mass.

95                                                                      16 January 2023
```

### LAYOUT PDF PAGE 95

```text
    Module 17
    Use Cases

96             11 November 2022
```

### LAYOUT PDF PAGE 96

```text
                                         Use Case                                                                   SST

 A kind of case

     Subject of the use case (often the system of interest)

     Objective is to provide value to one or more actor

    ▪ Stakeholders are typically external to the system of interest referred to as actors

     Required actions/steps performed by actors and subject to achieve the objective

     Include use cases are always performed as part of the base use case

     Constraints can specify pre and post conditions

       «use case def»                                                  «subject»
    TransportPassenger                                                  ^vehicle

                         objective
    doc Deiver passenger to destination
    safely, comfortably, and within
    accecptable time

                                         ^driver:Driver                                    «use case»            «actor»
                                                                       transporttPassenger:TransportPassenger  road:Road

                                         ^passengers:Passenger [0..4]  «include»  «include»

                                                   «use case»                                     «use case»
                                         ^getInVehicle:GetInVehicle               ^getOutOfVehicle:GetOutOfVehicle

97                                                                                                             16 January 2023
```

### LAYOUT PDF PAGE 97

```text
      Module 18
    Analysis Cases

98                  11 November 2022
```

### LAYOUT PDF PAGE 98

```text
                          Analysis Case            SST

 A set of steps with an objective to evaluate a                   «analysis»
  result about a subject of the analysis                    fuelEconomyAnalysis
   A kind of behavior
   Each step can be an action, calc, or an        convert to liters / 100 km
     analysis case that can contain
     ▪ subject                                                                          16 January 2023
     ▪ objective
     ▪ input and output parameters
     ▪ single return parameter (i.e., the result)
     ▪ attributes bound to calculations and/or
        constraints to be solved by a solver
     ▪ bind parameters to the subject

       «analysis»
    vehicleAnalysis

           «analysis»            «analysis»
    straightLineDynamics  fuelEconomyAnalysis

99
```

### LAYOUT PDF PAGE 99

```text
     Trade-off Analysis                                      SST

 A kind of analysis case                                                               «analysis»
                                                                      engineTradeOffAnalysis:TradeStudy
   Trade study objective is to select preferred solution
     that maximizes or minimizes some evaluation function                                  subject
                                                             vehicleAlternatives [2] :> vehicle_b
   Subject of the trade study are the vehicle alternatives
     with different engines                                                objective :MaximizeObjective
      ▪ Alternatives can be modeled as variants              doc Select vehicle alternative with the engine
                                                             whose evaluation function returns the max value
   Evaluate evaluation function for each alternative
      ▪ Criteria are parameters of evaluation function                                  alternatives
      ▪ Each criteria may require separate analysis          vehicle_b_engine4cyl:>vehicleAlternatives
                                                             vehicle_b_engine6cyl:>vehicleAlternatives
   Rationale is a kind of annotation
                                                                                            calcs
                                                             :>> evaluationFunction {

                                                                   in part vehicle:>vehicle_b;
                                                                   return attribute eval:Real=EngineEvaluation
                                                                   (vehicle.engine.mass,
                                                                   vehicle.engine.peakHorsePower,
                                                                   vehicle.engine.fuelEfficiency,
                                                                   vehicle.engine.cost)}

100                                                          11 November 2022
```

### LAYOUT PDF PAGE 100

```text
         Module 19
     Verification Cases

101                      11 November 2022
```

### LAYOUT PDF PAGE 101

```text
           Verification Case                                                                             SST

 A set of steps with an objective to                                         «part»                               «part»
  evaluate whether the subject of the                                 verificationContext                  verificationSystem
  verification satisfies one or more
  requirements                                                                «part»                     «perform»
                                                                       vehicle_b:Vehicle
   A kind of behavior                                                                                                   «verification»
                                                                            attributes                             massVerificationTest
   Steps typically include collect data,            :>>mass = dryMass + fluidMass
     process/reduce data, evaluate result            :>>dryMass=sum(partMasses)                                             objective
                                                     :>>fluidMass = 36 [kg]                              doc Verify massRequirement is
   Subject is an input to the verification                                                              satisfied
                                                                          requirements
   Returns a result called a verdict                satisfy vehicleSpecification                                            subject
     whose value is pass, fail, inconclusive,                                                            v:Vehicle:>vehicle_b
     or error                                                      massReqt.massActual = mass

   Verify relationship relates                                                                «verify»
     verification case to requirement
                                                                                                                             actions
                                                                                                         collectData
                                                                                                         processData
                                                                                                         evaluateResult : Verdict

 Verification system interacts with                                   «verification»
                                                                  massVerificationTest
     subject to perform the verification                                                                                                 =
                                                                          «action»                                                    verdict
     case                                       =     «action»          processData                          «action»
                                          v:Vehicle  collectData                                         evaluateResult

102                                                                                                      11 November 2022
```

### LAYOUT PDF PAGE 102

```text
                         Module 20
     Dependency, Allocation, and Cause-Effect

                       Relationships

103  11 November 2022
```

### LAYOUT PDF PAGE 103

```text
               Dependency              SST

 A directed relationship where the element on the client end may be impacted
  when the element on the supplier end changes

   Example: Use of dependency to represent traceability between specification
    and source document

   Can have 1.. many clients and 1.. many suppliers

     supplier        «item »
                 marketSurvey

     dependency

     client      «requirementGroup»
                 vehicleSpecification

104                                    11 November 2022
```

### LAYOUT PDF PAGE 104

```text
                                 Allocation                                              SST

 A statement of intent that assigns responsibility
  from one set of elements to another set of elements

 A kind of mapping (1 to n)                            «part»               «allocate»     «part»
 Includes definition and usage                  torqueGenerator                         powerTrain
 Can include suballocations
                                                  perform actions
                                               gegneenraetreaTteoTrqourqeue

 Examples                                             «allocate»                         «part»
   Actions to components                                                           engine:Engine
   Logical components to physical components
                                                                                   perform actions
                                                                             gegneenraetreaTteoTroqurqeue

 Logical connections to physical connections      The torque generator
 Budget allocation (e.g. weight budget)       Is allocated to the powertrain,
 Software to hardware
                                                 and realized by the engine

 Requirements to design elements

…

105                                                                                      11 November 2022
```

### LAYOUT PDF PAGE 105

```text
                      Cause-Effect Relationship                                                                        SST

 Single relationship can have multiple causes of multiple effects

 Can logically combine different cause-effect relationships

                         «state»                                                             «state»
                      engineStates                                                       vehicleStates

                        «parallel»                                                         «parallel»

                                                                                                            «state»
                                                                                                         healthStates

          «state»        «state»                                              «state»    «state»                          «state»
     operatingStates  healthStates                                      operatingStates  nominal                       maintenance

                      «state»          «state»                     «#causation»
                      nominal       overheating
                                                                                                   «state»
                                                                                                  degraded

          «state»                             «#causation»         Vehicle Thermostat Stuck Closed
     operatingStates                                               Causes engine to overheat
                        «state»                                    Causes vehicle to enter degraded state
                      thermostat
                      «parallel»

                                       «state»
                                   failureStates

                                                          «state»
                                                      stuckClosed

                                «state»
                                healthy

                                                          «state»
                                                       stuckOpen

106                                                                                               16 January 2023
```

### LAYOUT PDF PAGE 106

```text
       Module 21

     Annotations

107               11 November 2022
```

### LAYOUT PDF PAGE 107

```text
     Annotations                                               SST

 An Annotating Element is an Element that is used to provide                           «part»
  additional information about other elements                                    vehicle_b:Vehicle
   Can be named
   Can apply to 0.. many elements                                                   «com men t»
                                                                             Refer to document xyz
 An annotation is a kind of relationship that relates the
  annotating element to the element being annotated                              for full description

 Kinds of annotating elements                                                        «action»
   Comment                                                                     generateTorque
     ▪ Documentation is an owned comment
   Textual representation (e.g., opaque expression)                                    «rep»
     ▪ Includes name of language and body                                 language MATLAB
   Metadata feature                                                      body {
     ▪ Used to add structured metadata
                                                                            x=
                                                                            y=
                                                                          }.

                                                                                   «analysis»
                                                                            straightLineDynamics

                                                                                  «m etada ta»
                                                               ToolMetadata

                                                                 toolName = Tool_X
                                                                 toolURL =
                                                                 behaviorName = Compute vehicle state

108                                                            11 November 2022
```

### LAYOUT PDF PAGE 108

```text
                                                                       Metadata                                                                                SST

 Use metadata to mark elements
   Identify parts that are Security or Safety parts (e.g., members of Security of Safety group)
   Can add additional security and safety information

                                                                                                                                            «part»
                                                                                                                                    vehicle_b:Vehicle

                                                             «part»                 «part»                 «part»
                                                        engine:Engine  transmission:Transmission  driveshaft:Driveshaft

                    «part»                                                                                                        «part»
               interior:Interior                                                                                         bodyAssy:BodyAssy

    «part»               «part»               «part»           «part»            «part»                  «part»              «part»                   «part»          «part»
frontSeat [2]         seatBelt [2]        driverAirBag          alarm  sunroof:Sunroof [0..1]     doors:Door [2..4]           body                 bumper [2]     keylessEntry

                       metadata             metadata         metadata                                                      attributes               metadata        metadata
               Safety               Safety              Security                                                         color:Colors       Safety             Security

                isMandatory=true     isMandatory=false                                                                                       isMandatory=true

                                    Marked as a security part

                                                                                                                             Marked a safety part
                                                                                                                         Additional info: isMandatory

109                                                                                                                                         11 November 2022
```

### LAYOUT PDF PAGE 109

```text
        Module 22
     Element Filters

110                   11 November 2022
```

### LAYOUT PDF PAGE 110

```text
                           Element Filters                                        SST

 Used to select elements from a group of elements
   Create a package
   Import the part of the model that contains the elements of interest
     ▪ Use a recursive import to include all nested elements
   Define the filter expression to select the imported elements based on the
    selection criteria

Safety Parts               Security Parts           Safety & Security Parts
filter @Safety             filter @Security         filter @Safety and @Security

      PPaarrttss TTrreeee        Parts Tree               Parts Tree

  Filter selects parts marked with Safety metadata  16 January 2023

111
```

### LAYOUT PDF PAGE 111

```text
           Module 23

     View & Viewpoint

112                    11 November 2022
```

### LAYOUT PDF PAGE 112

```text
                                 View and Viewpoint                                                       SST

 A Viewpoint reflects the concerns of one more stakeholders in terms of what they care
  about relative to a domain of interest

 A View specifies an artifact to present to a stakeholder to satisfy their viewpoint

    Exposes the scope of the model to be viewed
    Filters the model to select a particular subset based on a scope and filter criteria
    Renders the filtered results using a particular presentation form and style
    Intended to support document generation (e.g., OpenMBEE)

     Vehic le Con figura tion_b

     Requirements                PartsTree                               «view»              «viewpoint»
                                                                  vehiclePartsTree             structure

                                                                       viewpoint            stakeholders
                                                                                    architect
                                            «expose» sstrutrcutucrteure
                                                                                               concerns
                                                                                    system breakdown

     A ctionT ree                States

                                                                                    Include rendering
                                                                                    in view compartment

113                                                                                 11 November 2022
```

### LAYOUT PDF PAGE 113

```text
     SysML v2 Views and Diagrams                                                                                                                          SST

 A view is a rendering of a selected model elements based on filter expression and
  exposed elements

   Frame is the view element with view name
   View is defined by a view definition (e.g., diagram kind)
   View content

     ««vviieeww»» VVeehhiiccllee RReeqquuirireemmeennttss:: TGreneeVriaelwView

                                                                                   «requirement»
                                                                                vehicleSpecification
                                                                                 subject v:Vehicle

                      «requirement»                                                                              «requirement»
         <1> massReqt:MassRequirement                                                                 <2> fuelEconomyRequirements

                              doc
     The actual vehicle mass shall be less
     than the required vehicle mass.

                                                                                                «requirement»                          «requirement»
                                                                                <2_1> city:FuelEconomyRequirementl  <2_2> highway:FuelEconomyRequirement

114                                                                                                                                16 January 2023
```

### LAYOUT PDF PAGE 114

```text
                Standard View Definitions     SST
                  (SysML v2 vs SysML v1)

             Baseline as of January 04, 2023

Standard views are normative,
but user defined views are valid
if they are consistent with the

abstract syntax and graphical bnf.

                                              16 January 2023
```

### LAYOUT PDF PAGE 115

```text
     SysML v2 Compartments                                             SST

 Compartments are views of the element represented by the node                  «part def»
 Compartment names represent view definitions                                     Vehicle
 Standard compartments / view definitions
                                                                                  attributes
   Textual view of contained elements of a particular kind (e.g.,     mass:>ISQ::mass
    attributes, actions, ports)                                        dryMass
                                                                       cargoMass
   Textual view of elements at the other end of relationships (e.g.,  electricalPower
    allocation, specialization, …)                                     position
                                                                       velocity
 A compartment can also be rendered using graphical notation
 Ports and parameters are connectable nested nodes on the             ...acceleration

  boundary of a structure or behavior                                                ports
                                                                       pwrCmdPort

                                                                       ...vehicleToRoadPort

                                                                             perform actions
                                                                       providePower
                                                                       provideBraking

                                                                       ...controlDirection

                                                                               exhibit states
                                                                       vehicleStates

116                                                                    16 January 2023
```

### LAYOUT PDF PAGE 116

```text
           Module 24
     Language Extension

117                      11 November 2022
```

### LAYOUT PDF PAGE 117

```text
               Language Extension                                SST

 Provides ability to extend concepts in  define the             SysML Model
  SysML v2 to address domain-specific      concept                   Library
  concepts and terminology                                            «stateUsage»
                                                                            states
 Define concept by subclassing an
  element in the SysML Model Library                                  «stateUsage»
                                                                      failure modes
 Define the keyword using metadata
                                                                       «#failure mode»
 state 'failure modes'[*] nonunique;                                         flatTire

metadata def <fm> ’failure mode’ :> SemanticMetadata {                        «#fm»
         :>> baseType = ‘failure modes’ meta SysML::StateUsage;              flatTire

}

 Apply the concept to an element by

annotating it with the metadata           apply the concept

#'failure mode' flatTire;

#fm flatTire;

118                                                              16 January 2023
```

### LAYOUT PDF PAGE 118

```text
     Contrasting SysML v2 with SysML v1

119  11 November 2022
```

### LAYOUT PDF PAGE 119

```text
     SysML v2 to v1                 SST

     Terminology Mapping (partial)

                 SysML v2                           SysML v1
               part / part def                part property / block
         attribute / attribute def        value property / value type
              port / port def             proxy port / interface block
            action / action def
             state / state def                   action / activity
       constraint / constraint def           state / state machine
     requirement / requirement def  constraint property / constraint block
      connection / connection def
              view / view def                      requirement
                                        connector / association block

                                                        view

120                                 11 November 2022
```

### LAYOUT PDF PAGE 120

```text
Contrasting SysML v1 with SysML v2 SST

 Simpler to learn and use                      More expressive
    Systems engineering concepts designed        Variant modeling
      into metamodel versus added-on              Analysis case
    Consistent definition and usage pattern      Trade-off analysis
    More consistent terminology                  Individuals, snapshots, time slices
    Ability to decompose parts, actions, …       More robust quantitative properties
    More flexible model organization               (e.g., vectors, ..)
      (unowned members, package filters)…         Simple geometry
                                                  Query/filter expressions
 More precise                                    Metadata
    Textual syntax and expression language
    Formal semantic grounding                  More extensible
    Requirements as constraints                  Simpler language extension capability
    Reified relationships (e.g., membership,       ▪ Based on model libraries
      annotation)
                                                More interoperable
121                                               Standardized API

                                                                                                 11 November 2022
```

### LAYOUT PDF PAGE 121

```text
     Summary

122           11 November 2022
```

### LAYOUT PDF PAGE 122

```text
     Summary  SST

 SysML v2 is addressing SysML v1limitations to improve MBSE adoption and
  effectiveness
   Precision, expressiveness
   Regularity, usability
   Interoperability with other engineering models and tools

 Approach
   Simplified SysML v2 metamodel with formal semantics overcomes fundamental
    UML limitations
   Flexible graphical notations and textual notation
   Standardized API for interoperability

 Specification submitted to OMG on February 20, 2023

   Will request vote to adopt at March 2023 OMG meeting
   Becomes a beta specification if approved

123           07 March 2023
```

### LAYOUT PDF PAGE 123

```text
     References  SST

 Monthly Release Repository (release 2023-02)
   https://github.com/Systems-Modeling/SysML-v2-Release

 SysML v2 Specification (revised submission)
   Note: refer to Annex B for Example Vehicle Model

 Introduction to the SysML v2 Language Textual Notation (release 2021-08)

 Friedenthal S., Seidewitz E., A Preview of the Next Generation System Modeling
  Language (SysML v2), Project Performance International (PPI), Systems
  Engineering Newsletter, PPI SyEN 95 27 November, 2020

124              07 March 2023
```
