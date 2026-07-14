# AUTHORITATIVE PDF EXTRACTION: Intro to the SysML v2 Language-Textual Notation.pdf

- source_repository: https://github.com/Systems-Modeling/SysML-v2-Release
- source_commit: `288d129c0d532065d45434bbb48a920898b719af`
- source_path: `doc/Intro to the SysML v2 Language-Textual Notation.pdf`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Release/blob/288d129c0d532065d45434bbb48a920898b719af/doc/Intro to the SysML v2 Language-Textual Notation.pdf
- source_bytes: 24097427
- source_sha256: `fa03e51c4ba663b2f0edcadcdddf80016528ef8e1ab34a4a562efa89b7d212f1`
- pdf_pages: 185
- extracted_utc: `2026-07-14T16:48:16.124610+00:00`
- pdf_metadata: `{'/Title': 'SysML v2 Language Intro to Structure and Behavior Modeling', '/Author': 'Ed Seidewitz', '/Subject': '', '/Keywords': '', '/CreationDate': "D:20260514201350+00'00'", '/ModDate': "D:20260514201350+00'00'"}`

## SEMANTIC PAGE-BY-PAGE EXTRACTION

### PDF PAGE 1

Introduction to the SysML v2 Language
                           Textual Notation





           This is a training presentation on the SysML v2 language.
               It is updated as appropriate for each release of the
                  SysML v2 Pilot Implementation maintained by
                the OMG® Systems Modeling Community (SMC)

                                    Release: 2026-04



                      Copyright © 2019-2026 Model Driven Solutions, Inc.
           Licensed under the Creative Commons Attribution 4.0 International License.
        To view a copy of this license, visit http://creativecommons.org/licenses/by/4.0/ or
        send a letter to Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.

### PDF PAGE 2

Changes in this Release





 In SequenceFunctions library model, corrected input parameters to be
  unordered in “size” and following functions through “excludes”.
 In Quantities library model, corrected type of ScalarQuantityValue.

                    To find slides that have changed recently, search for
                                     Last changed: 2026-04
                               (and similarly for earlier releases).













 2                                                                                       Release 2026-04

### PDF PAGE 3

SysML v2 Language Architecture

                                                                                                           Declarative semantic base
                                               Systems Modeling Language                                   elements and domain-
                                                           (SysML)                                         specific libraries modeled
                                                                                                           using SysML

                                                           metamodel               Systems and
                                Systems Syntax          semantic library          Domain Model
                                                                                     Libraries
                                                Kernel Modeling Language                                  Declarative semantic base
                                                           (KerML)                                        elements modeled using
                                                                                                          KerML
                                                           metamodel               Kernel Model
                                 Kernel Syntax          semantic library             Libraries


                                                                                                          Direct semantic mapping to
                                                            semantic                                      formal logic
                                      Core                specification           Core Semantics
                                     Syntax


                                                          Root syntactic elements
                                                          without model-level semantics
                                      Root                (e.g., packaging)
                                     Syntax

3                                                        Last changed: 2020-09                                          Release 2026-04

### PDF PAGE 4

Four-Layer Language Architecture



 Root – Root syntactic elements
    Element, Comment, Documentation, Textual Representation, Namespace
    Relationship, Annotation, Membership, Import, Dependency
 Core – Fundamental semantic concepts – Formal declarative semantics
    Type, Classifier, Feature, Multiplicity
    Feature Membership, Specialization, Conjugation, Type Featuring, Feature Chaining, Feature
     Inverting, Unioning, Intersecting, Differencing
 Kernel – Foundation for building modeling languages – Kernel semantic library
    Class, Data Type, Behavior, Function, Metaclass, Step, Expression, Metadata Feature, Package
    Association, Interaction, Connector, Binding Connector, Succession, Item Flow, Succession Item
     Flow
 Systems – Modeling language for systems engineering – Domain libraries

    Definition and Usage of:
      ▪ Attributes, Enumerations, Occurrences, Items, Parts, Ports, Actions, States, Constraints,
        Requirements, Concerns, Calculations, Cases, Analysis Cases, Verification Cases, Use Cases, Views,
        Viewpoints, Renderings, Metadata
      ▪ Connections, Interfaces, Allocations, Flows, Succession Flows


 4                                Last changed: 2025-02 (“flow connection” renamed ”flow”)             Release 2026-04

### PDF PAGE 5

Packages – Members






 A package acts as a namespace                 A name with spaces or other             An import adds either a single
 for its members and a container                  special characters is
 for its owned members.                           surrounded in single quotes.          imported member or all the
                                                                                        members of an imported package
                                                                                        to the importing package.
                                    package 'Package Example’ {
                                        public import ISQ::TorqueValue;
                                        private import ScalarValues::*;                        A package can introduce

 The owned members of                   part def Automobile;                                   aliases for its owned
 a package are elements                                                                        members or for individual
 directly contained in                  alias Car for Automobile;                              members of other packages.
 the package.                           alias Torque for ISQ::TorqueValue;
                                    }


                                                                 A qualified name is a package name
                                                                  (which may itself be qualified) followed
                                                                  by the name of one of its members,
                                                                  separated by :: .



5                                             Last changed: 2024 -07 (import visibility)                           Release 2026-04

### PDF PAGE 6

Packages – Visibility





    All members from a public import                               !  Visibility must be shown
    are visible (re-exported) from the                                explicitly on import declarations.
    importing package. Members                                        Use private visibility unless re-
    from a private import are not.                                    export is required.


    A private member is             package 'Package Example' {
    not visible outside the             public import ISQ::TorqueValue;
    package (but it is visible          private import ScalarValues::*;
    to subpackages).
                                        private part def Automobile;

                                        public alias Car for Automobile;
                                        alias Torque for ISQ::TorqueValue;
    Members are public by           }
    default but can also be
    marked public
    explicitly.





6                                           Last changed: 2024-07 (import visibility)                        Release 2026-04

### PDF PAGE 7

Comments



A comment begins with /* and        package 'Comment Example’ {
ends with */ .                         /* This is comment, part of the model,
                                        * annotating (by default) it's owning package. */

                                       comment Comment1 /* This is a named comment. */
 A comment  can optionally be          comment about Automobile
 named.                                /* This is an unnamed comment, annotating an

                                        * explicitly specified element.
                                        */                                   What the comment annotates can
Import and alias declarations          part def Automobile;                  be explicitly specified (it is the
can also be commented.                                                       owning namespace by default).
                                       alias Car for Automobile {
                                           /* This is a comment annotating its owning
 A note begins with // and                  * element.
 extends to the end of the line.            */
 (A multiline note begins with         }
 //* and ends with */.)
                                       // This is a note. It is in the text, but not part
                                      // of the model.
                                       alias Torque for ISQ::TorqueValue;
                                    }

7                                  Last changed: 2023-10 (removed "documentary")                 Release 2026-04

### PDF PAGE 8

Documentation





  Documentation is a special
  kind of comment that is
  directly owned by the            package 'Documentation Example' {
  element it documents.               doc   /* This is documentation of the owning

                                             * package.
                                             */

  A documentation comment             part def Automobile {
  can be optionally named                doc  Document1
  like a regular comment.                   /* This is documentation of Automobile. */
                                     }

                                      alias Car for Automobile {
                                          doc /* This is documentation of the alias. */
                                      }
                                      alias Torque for ISQ::TorqueValue;
                                   }





8                                 Last changed: 2023-07 (corrected "ISO" to "ISQ")           Release 2026-04

### PDF PAGE 9

Part and Attribute Definitions



    A part definition is a definition of
    a class of systems or parts of                                                          An attribute usage usage of an
    systems, which are mutable and                                                          attribute definition, used here as
    exist in space and time.                                                                a feature of the part definition.
                                              part def Vehicle {
                                                 attribute mass : ScalarValues::Real;
                                                 part eng : Engine;                         A part usage is a composite
An attribute definition is a definition                                                     feature that is the usage of a
of attributive data that can be used             ref part driver : Person;                  part definition .
to describe systems or parts.                 }
                                                                                            A reference part usage is a
                                              attribute def VehicleStatus {referential feature that is the
  Definitions and usages are also               private import ScalarValuesusage of a part definition::*;              .
   namespaces that allow     import.
                                                 attribute gearSetting : Integer;
                                                 attribute acceleratorPosition : Real;
                                              }                                                   An attribute definition

                                              part def Engine;                                    may not have composite
                                              part def Person;                                    features. Attribute usages
                                                                                                  are always referential.

9                                  Last changed: 2023-10 (corrected callout on attribute features)               Release 2026-04

### PDF PAGE 10

Generalization/Specialization




                                                                                         A specialized definition defines
                                                                                         a subset of the classification of
                            abstract part def          Vehicle;                          its generalization.

An abstract definition      part def     HumanDrivenVehicle            specializes       Vehicle {
is one whose instances             ref part     driver : Person;             The :> symbol is equivalent
must be members of          }                                                to the specializes keyword.

some specialization.        part def     PoweredVehicle          :> Vehicle {
                                   part   eng : Engine;
                            }                                             A specialization can define
                                                                          additional features.
                            part def     HumanDrivenPoweredVehicle                :>
                               HumanDrivenVehicle, PoweredVehicle;

                            part def Engine;                                     A definition can have multiple
                            part def Person;                                     generalizations, inheriting the
                                                                                 features of all general definitions.





10                                                 Last changed: 2020-06                                   Release 2026-04

### PDF PAGE 11

Subsetting





                                                                           Subsetting  asserts that, in any
                                                                           common context, the values of one
                      part def     Vehicle {                               feature are a subset of the values of
                         part   parts :      VehiclePart      [*];         another feature.

                         part   eng : Engine         subsets    parts;
                         part   trans : Transmission             subsets     parts;
                         part   wheels : Wheel[4] :> parts;
                      }                                                    Subsetting  is a kind of
                      abstract     part def      VehiclePart      ;        generalization between features.
                      part def     Engine :>       VehiclePart      ;
                      part def     Transmission :>          VehiclePart      ;
                      part def     Wheel :>       VehiclePart     ;










11                                                Last changed: 2020-06                                  Release 2026-04

### PDF PAGE 12

Redefinition

                                                                                    A specialized definition can
                                                                                    redefine a feature that would
                                 part def      Vehicle {                            otherwise be inherited, to change
                                     part   eng   : Engine;                         its name and/or specialize its type.
                                 }
                                 part def      SmallVehicle       :> Vehicle {
                                     part   smallEng     : SmallEngine redefines eng;
                                 }                                                      The :>> symbol is equivalent
                                 part def BigVehicle :> Vehicle {                       to the redefines keyword.
                                     part bigEng : BigEngine :>> eng;
                                 }                                                   A feature can also specify

 There is shorthand notation     part def Engine {                                   multiplicity.
 for redefining a feature with       part cyl : Cylinder[4..6];
 the same name.                  }                                                     The default multiplicity for
                                 part def SmallEngine :> Engine {                       parts is 1..1.
                                     part redefines cyl[4];
                                 }
                                 part def BigEngine :> Engine {
                                     part redefines cyl[6];
                                 }                                           Redefinition can be used to constrain

                                 part def Cylinder;                          the multiplicity of a feature.



12                                      Last changed: 2021-08 (multiplicity defaults)                    Release 2026-04

### PDF PAGE 13

Enumeration Definitions (1)



                                                        An enumeration definition is a kind
                                                        of attribute definition that defines
                                                        a set of enumerated values.


                enum   def   TrafficLightColor         {
                   enum green;                                        The values of an attribute usage defined
                   enum yellow;                                       by an enumeration definition are limited
                   enum red;                                          to  the defined set of enumerated values.
                }

                part   def   TrafficLight       {
                   attribute     currentColor       : TrafficLightColor;
                }

                part def TrafficLightGo specializes TrafficLight {
                   attribute redefines currentColor = TrafficLightColor::green;
                }

                            This shows an attribute being bound to a
                            specific value (more on binding later).



13                                           Last changed: 2020-12 (new)                             Release 2026-04

### PDF PAGE 14

Enumeration Definitions (2)
                                                                                    An enumeration definition can
                           attribute def ClassificationLevel {                      contain nothing but declarations of its
                              attribute code : String;                              enumerated values. However, it can
                              attribute color : TrafficLightColor;                  specialize a regular attribute
                           }                                                        definition and inherit nested features.

                           enum def ClassificationKind specializes ClassificationLevel {
                              unclassified {
                                 :>> code = "uncl";
                                 :>> color = TrafficLightColor::green;                     !  An enumeration definition
The enum keyword is           }                                                               cannot specialize another
                              confidential {                                                  enumeration definition.
optional when declaring          :>> code = "conf";
enumerated values.               :>> color = TrafficLightColor::yellow;
                              }
                              secret {
                                 :>> code = "secr";                                    The nested features can then be
                                 :>> color = TrafficLightColor::red;
                              }                                                        bound to specific values in each of
                           }                                                           the enumerated values.

                           enum def GradePoints :> Real {
                              A = 4.0;
                              B = 3.0;                 Enumerated values can also be bound
                              C = 2.0;                 directly to specific values of a specialized
                              D = 1.0;                 attribute definition or data type.
                              F = 0.0;
                           }

14                                                Last changed: 2020-12 (new)                                  Release 2026-04

### PDF PAGE 15

Parts (1)





                                    // Definitions
                                    part def      Vehicle {
                                       part    eng   : Engine;
                                    }
                                    part def      Engine {
    Parts can be specified             part    cyl   : Cylinder[4..6];
    outside the context of a        }                                          The  defined by  relationship is a
    specific part definition.       part def      Cylinder;                    kind of generalization.

                                    // Usages
                                    part   smallVehicle         : Vehicle {
                                       part    redefines       eng   {
                                           part   redefines       cyl   [4];
                                       }                                               Parts inherit properties from
                                    }                                                  their definitions and can
                                    part   bigVehicle        : Vehicle {               redefine them, to any level of
                                       part    redefines       eng   {                 nesting.
                                           part   redefines       cyl   [6];
                                       }
                                    }



15                                              Last changed: 2020-12 (editorial)                             Release 2026-04

### PDF PAGE 16

Parts (2)




                             // Definitions
                             part def    Vehicle;
                             part def    Engine;                Composite structure can be
                             part def    Cylinder;              specified entirely on parts.

                             // Usages
                             part  vehicle : Vehicle {
                                part   eng : Engine {
                                   part   cyl   : Cylinder[4..6];               A part can specialize
                                }                                               another part.
                             }
                             part  smallVehicle        :> vehicle {
                                part   redefines     eng   {
                                   part   redefines     cyl  [4];
                                }
                             }
                             part  bigVehicle       :> vehicle {
                                part   redefines     eng   {
                                   part   redefines     cyl  [6];
                                }
                             }


16                                              Last changed: 2020-06                                Release 2026-04

### PDF PAGE 17

Items



   An item definition defines a class of                                       All parts can be treated as items, but
   things that exist in space and time but                                        not all items are parts. The design of a
   are not necessarily considered "parts"                                         system determines what should be
   of a system being modeled.                                                     modeled as its "parts".


                                       item   def    Fuel;                        A system model may reference discrete
                                       item   def    Person;                      items that interact with or pass through

                                       part   def    Vehicle {                    the system.
                                          attribute       mass : Real;

  The default multiplicity               ref   item     driver : Person;
    for attributes and items              part    fuelTank       {
    is also 1..1.                             item   fuel: Fuel;
                                          }                                       Items may also model continuous
                                       }                                          materials that are stored in and/or flow
                                                                                  between parts of a system.
    An item is continuous if any portion of it in space is the
      same kind of thing. A portion of fuel is still fuel. A portion
      of a person is generally no longer a person.

17                                          Last changed: 2021 -08 (multiplicity defaults)                          Release 2026-04

### PDF PAGE 18

Connections (1)



                                   connection def PressureSeat {                                     A connection definition   is
                                       end [1] part bead : TireBead;                                 a part definition whose
                                       end [1] part mountingRim: TireMountingRim;                    usages are connections
Cross multiplicities constrain     }                                                                 between its ends.
the number of connections,         part wheelHubAssembly : WheelHubAssembly {
rather than end values. E.g.,
for every TireBead there               part wheel : WheelAssembly[1] {
must be a PressureSeat                    part t : Tire[1] {
connection to exactly one                     part bead : TireBead[2];
TireMountingRim.                          }
                                          part w: Wheel[1] {
                                              part rim : TireMountingRim[2];
                                              part mountingHoles : LugBoltMountingHole[5];
A connection is a usage of a              }
connection definition,                    connection : PressureSeat
which connects two other                      connect bead references t.bead                      Reference subsetting
                                              to mountingRim references w.rim;
features.                              }                                                          (references or ::>) relates
                                       part lugBoltJoints : LugBoltJoint[0..5];                   feature to a connector ends.
                                       part hub : Hub[1] {                                        “Dot” notation specifies
If a connection definition is             part h : LugBoltThreadableHole[5];                      paths to nested features.
not specified, a generic               }
connection definition                  connect [0..1] lugBoltJoints to [1] wheel.w.mountingHoles;
(called Connection) is used.           connect [0..1] lugBoltJoints to [1] hub.h;
                                   }

 18                                          Last changed: 2024-12 (cross multiplicity)                          Release 2026-04

### PDF PAGE 19

Connections (2)





                                                                                                      These are owned features of
                                                                                                      the part   wheel   , not the part
                                                                                                      definition WheelAssembly.














           Feature chains (“dot notation”) like
           wheel.w.mountingHoles can be
           used to refer to the value of a
           specific feature in context (similarly
           to property paths in SysML v1).



19                                              Last changed: 2024   -12 (feature chain callout)                              Release 2026-04

### PDF PAGE 20

Ports
                                                                                            Ports may have attribute and
                                                                                            reference features. A feature
                                                                                            with a direction (in, out or
                                        port   def    FuelOutPort        {                  inout) is a directed feature.
 A port definition defines                 attribute       temperature : Temp;
 features that can be                      out item      fuelSupply        : Fuel;
 made available via ports.                 in item fuelReturn : Fuel;
 (Replaces interface                    }
 blocks in SysML v1).

                                        port def FuelInPort {
   Directed features are                  attribute temperature : Temp;
    always referential, so it is           in item fuelSupply : Fuel;                         Two ports are compatible for
    not necessary to explicitly            out item fuelReturn : Fuel;                        connection if they have
    use the ref keyword.                }                                                     directed features that match
                                        part def FuelTankAssembly {                           with inverse directions.
 A port is a connection point              port fuelTankPort : FuelOutPort;
 through which a part                   }
 definition makes some of               part def Engine {
 its features available in a               port engineFuelPort : FuelInPort;
 limited way. (Like a proxy             }
 port in SysML v1.)




20                                             Last changed: 2021-05 (editorial)                              Release 2026-04

### PDF PAGE 21

Port Conjugation





                                               port def FuelPort {
                                                  attribute temperature : Temp;
                                                  out item fuelSupply : Fuel;
 Every port definition has an implicit            in item fuelReturn : Fuel;
 conjugate port definition that reverses       }
 input and output features. It has the         part def FuelTankAssembly {
 name of the original definition with ~           port fuelTankPort : FuelPort;
 prepended (e.g., '~FuelPort').                }


                                               part def Engine {
                                                  port engineFuelPort : ~FuelPort;
                                               }

                                                Using a ~ symbol on the port type is a
                                                shorthand for using the conjugate port
                                                definition (e.g., FuelPort::'~FuelPort').





21                                           Last changed: 2021-05 (editorial)                          Release 2026-04

### PDF PAGE 22

Interfaces




An interface definition is a
connection definition
whose ends are ports.
                                   interface     def  FuelInterface       {
  The default cross                  end port    supplierPort       : FuelOutPort;
   multiplicity is 0..*.              end port consumerPort : FuelInPort;
                                   }

                                   part vehicle : Vehicle {
                                      part tankAssy : FuelTankAssembly;
                                      part eng : Engine;
An interface usage is a               interface : FuelInterface connect
connection usage                         supplierPort ::> tankAssy.fuelTankPort to
defined by an interface                  consumerPort ::> eng.engineFuelPort;
definition, connecting             }
two compatible ports.







22                                     Last changed: 2024-12 (cross multiplicity)                 Release 2026-04

### PDF PAGE 23

Interface Decomposition



                                                         «interface def»
                                                          WaterDelivery
                                   [1]                                                       [1..*]
                              suppliedBy :        hot                          hot       deliveredTo :
                              SpigotBank                                                    Faucet

  Every  suppliedBy                             cold                          cold
   SpigotBank     must have                                                                         Connection ends specify the
   one or more connections                                                                          participants  in the
   to deliveredTo    Faucets .                                                                      connection. They always
                                                                                                    have multiplicity 1..1 relative
                              interface def WaterDelivery {                                         to the connection definition.
                                 end [1] port suppliedBy : SpigotBank {
Cross multiplicities                 port hot : Spigot;
correspond to navigating             port cold : Spigot;
across connections.              }
                                 end [1..*] port deliveredTo : Faucet {
                                     port hot : FaucetInlet;                                    Connection usages interconnect
                                     port cold : FaucetInlet;                                   specific participants.
                                 }

                                 connect suppliedBy.hot to deliveredTo.hot;
                                 connect suppliedBy.cold to deliveredTo.cold;
                              }


 23                                            Last changed: 2024 -12 (cross multiplicity)                           Release 2026-04

### PDF PAGE 24

Binding Connections






                     part tank : FuelTankAssembly {                    A binding connection is a connection
                        port redefines fuelTankPort {                  that asserts the equivalence of the
                           out item redefines fuelSupply;              connected features (i.e., they have
                           in item redefines fuelReturn;               equal values in the same context).
                        }

                        bind fuelTankPort.fuelSupply = pump.pumpOut;
                        bind fuelTankPort.fuelReturn = tank.fuelIn;

                        part pump : FuelPump {                         Usages on parts can also have
                           out item pumpOut : Fuel;                    direction (and are automatically
                           in item pumpIn : Fuel;                      referential).
                        }
                        part tank : FuelTank {
                           out item fuelOut : Fuel;
                           in item fuelIn : Fuel;
                        }
                     }




24                                      Last changed: 2021-04 (dot notation)                    Release 2026-04

### PDF PAGE 25

Binding Connections                      – Feature Values







                part   tank :    FuelTankAssembly        {
                   port   redefines     fuelTankPort      {
                      out item     redefines     fuelSupply     = pump.pumpOut;
                      in item redefines fuelReturn;
                   }
                   part pump : FuelPump {                          The feature value notation
                      out item pumpOut : Fuel;                     combines the definition of a
                      in item pumpIn : Fuel;                       feature with a binding connection.

                   }
                   part tank : FuelTank {
                      out item fuelOut : Fuel;
                      in item fuelIn : Fuel = fuelTankPort.fuelReturn;
                   }
                }                                                     ! This is a binding, not an
                                                                        initial or default value.





25                       Last changed: 2023-10 (moved fuelSupply feature value, revised callouts)Release 2026-04

### PDF PAGE 26

Flows





                                                                  «part»        A flow transfers a payload
                                                            vehicle : Vehiclefrom the source output to
                                                                                the target input.

                                   fuelTankPort                                              engineFuelPort
                                 «part»                             Fuel                            «part»
                               tankAssy :          fuelSupply                  fuelSupply            eng :
                                FuelTank                                                            Engine
                               Assembly

                                                                        But it is actually a
                                                                        connection between the
                                                                        source and target ports.



                                 A flow is streaming if the transfer is ongoing between
                                    the source and target, as opposed to happening once
                                    after the source generates its output and before the
                                    target consumes its input.


26                                     Last changed: 2025-02 (“flow connection” renamed ”flow”)                            Release 2026-04

### PDF PAGE 27

Flow Usage









 A flow usage is a transfer of         part   vehicle : Vehicle {
 some payload from an output              part   tankAssy     : FuelTankAssembly;
 of a source port to an input of          part eng : Engine;

 a target port.                           flow of Fuel
                                             from tankAssy.fuelTankPort.fuelSupply
                                            to eng.engineFuelPort.fuelSupply;

 Specifying the payload type             flow of Fuel
    (e.g., “of Fuel”) is optional.           from eng.engineFuelPort.fuelReturn
                                            to tankAssy.fuelTankPort.fuelReturn;
                                       }









27                              Last changed: 2025-02 (“flow connection” renamed ”flow”)            Release 2026-04

### PDF PAGE 28

Flows in Interfaces







           interface def FuelInterface {                     Flows can be defined within
             end supplierPort : FuelOutPort;                 an interface definition.
             end consumerPort : FuelInPort;

             flow supplierPort.fuelSupply to consumerPort.fuelSupply;
             flow consumerPort.fuelReturn to supplierPort.fuelReturn;
           }

           part vehicle : Vehicle {                          The flows are established
             part tankAssy : FuelTankAssembly;               when the interface is used.
             part eng : Engine;

             interface : FuelInterface connect
                supplierPort ::> tankAssy.fuelTankPort to
                consumerPort ::> eng.engineFuelPort;
           }






28                           Last changed: 2025-02 (“flow connection” renamed ”flow”)      Release 2026-04

### PDF PAGE 29

Flow Definitions




   A flow definition is used to assert                                     The definition can (optionally)
   that a flow must exist between                                          constrain the payload
   the instances of part definitions.                                      transferred by usages.


                                      flow def FuelFlow {
                                         ref :>> payload : Fuel;
                                         end port fuelOut : FuelOutPort;                          Note that the default
                                         end port fuelIn : FuelInPort;                            end multiplicities on this
                                      }                                                           connection are 1 to 1.

 This usage realizes the              part vehicle : Vehicle {                                 The payload should be
 required flow between the               part tankAssy : FuelTankAssembly;                     consistent with what is
 tankAssy.fuelTankPort and               part eng : Engine;                                    declared in the flow
 the eng.engineFuelPort.                                                                       definition (if any).
                                         flow : FuelFlow of Fuel
                                            from tankAssy.fuelTankPort.fuelSupply
                                            to eng.engineFuelPort.fuelSupply;
                                      }
                                The connection is defined to be
                                between the ports, but the transfer
                                is still from an output to an input.

29                                       Last changed: 2025-07 (payload in flow usage)                       Release 2026-04

### PDF PAGE 30

Action Definition



An An action definitionaction definition  is a definition is a definition Directed features of an action definition Directed features of an action definition
of some action to be performed.of some action to be performed.           are considered to be action are considered to be action parametersparameters..


                        action defaction def  Focus{ Focus{ in in scene : Scene; scene : Scene; out out image : Image; }image : Image; }
                        action defaction def  Shoot{ Shoot{ in in image : Image; image : Image; out out picture : Picture; } picture : Picture; }
           scene
     «action def»       action defaction def  TakePictureTakePicture  {{
     TakePicture           inin  scene : Scene; scene : Scene;       An An actionaction  is a usage of an action definition is a usage of an action definition
        =  scene           outout  picture : Picture;picture : Picture;performed in a specific context.performed in a specific context.

       «action»            bindbind  focus.scenefocus.scene  = scene;= scene;
        focus
           image
                           actionaction  focus : Focus { focus : Focus { inin  scene; scene; outout  image; };image; };A flow connection can A flow can be used to
           image                                                                            be used to transfer transfer items between
       «action»            flowflow  focus.imagefocus.image  toto  shoot.imageshoot.image;; items between actions.actions.
        shoot
         = picture         actionaction  shoot : Shoot { shoot : Shoot { inin  image; image; outout  picture; }picture; }

           picture
                           bindbind  shoot.pictureshoot.picture  = picture;= picture;
                        }}                                                         An action has parameters An action has parameters
                                                                                   corresponding to its action corresponding to its action
                                                                                   definition.definition.

30                              Last changed: 2025-02 (“flow connection” renamed ”flow”)           Release 2026-04

### PDF PAGE 31

Action Succession (1)





                       action def Focus{ in scene : Scene; out image : Image; }
                       action def Shoot{ in image : Image; out picture : Picture; }

                       action def TakePicture {
           scene          in scene : Scene;
     «action def»         out picture : Picture;
     TakePicture
        =  scene          bind focus.scene = scene;

      «action»            action focus : Focus { in scene; out image; }
        focus
           image
                          flow focus.image to shoot.image;               A succession asserts that the
           image                                                         first action must complete
      «action»            first focus then shoot;                        before the second can begin.
       shoot
        =  picture        action shoot : Shoot { in image; out picture; }

           picture
                          bind shoot.picture = picture;
                       }




31                                   Last changed: 2024-09 (succession graphic)                Release 2026-04

### PDF PAGE 32

Action Succession (2)







                        action def Focus{ in scene : Scene; out image : Image; }
                        action def Shoot{ in image : Image; out picture : Picture; }
           scene
     «action def»       action def TakePicture {
     TakePicture           in scene : Scene;                                        A succession flow requires the
        =  scene           out picture : Picture;                                   first action to finish producing

      «action»                                                                      its output before the second
        focus              bind focus.scene = scene;                                can begin consuming it.
«successionimage
   flow»                   action focus : Focus { in scene; out image; }
           image
      «action»             succession flow focus.image to shoot.image;
        shoot
         = picture         action shoot : Shoot { in image; out picture; }

           picture
                           bind shoot.picture = picture;
                        }




32                                  Last changed: 2024-09 (succession flow graphic)                Release 2026-04

### PDF PAGE 33

Action Notation Shorthands




                         action def Focus{ in scene : Scene; out image : Image; }
           scene         action def Shoot{ in image : Image; out picture : Picture; }
     «action def»                                                                This qualified name refers to the
     TakePicture         action def TakePicture {                                scene parameter of TakePicture,
        =                   in scene : Scene;                                    rather than the parameter of
           scene                                                                 focus with the same name.
       «action»             action focus : Focus {
        focus                   in scene = TakePicture::scene;
           image                out image;
                            }                          This is the same shorthand
           image                                       for binding used previously.
       «action»             flow focus.image to shoot.image;
        shoot
         = picture
                            then action shoot : Shoot {
           picture              in image;
                                out picture;
 This is a shorthand for    }
 a succession between
 the lexically previous     out picture : Picture = shoot.picture;
 action (focus) and this }
 action (shoot).


33                                     Last changed: 2024-09 (succession graphic)                    Release 2026-04

### PDF PAGE 34

Action Decomposition



                       action def Focus{ in scene : Scene; out image : Image; }
                       action def Shoot{ in image : Image; out picture : Picture; }
                       action def TakePicture{in scene : Scene; out picture : Picture;}

           scene       action takePicture : TakePicture {              An action usage can also
      «action»            in scene;                                    be directly decomposed
takePicture : TakePicture                                              into other actions.
        =                 action focus : Focus {
           scene             in scene = takePicture::scene;
      «action»               out image;
        focus             }                                                 takePicture is a usage, so dot
           image                                                            notation could be used here, but
           image          flow focus.image to shoot.image;                  it is unnecessary because scene is
      «action»            then action shoot : Shoot {                       in an outer scope, not nested.
       shoot
           picture           in image;
        =                    out picture;
           picture        }

                          out picture = shoot.picture;
                       }



34                                   Last changed: 2024-09 (succession graphic)                 Release 2026-04

### PDF PAGE 35

Conditional Succession (1)




                           action takePicture : TakePicture {
                             in scene;


            scene             action focus : Focus {
                                 in scene = takePicture::scene;A conditional succession asserts that the
       «action»                  out image;                                  second action must follow the first only
takePicture : TakePicture     }                                              if a guard condition is true. If the guard
         =  scene                                                            is false, succession is not possible.
       «action»               first focus
        focus                    if focus.image.isFocusedthen shoot;                       !  Note that, currently,
   [image.      image                                                                         the target action must
 isFocused]     image         flow focus.image to shoot.image;
                                                                                              be explicitly named (no
       «action»               action shoot : Shoot {                                          shorthand).
        shoot                    in image;
         =  picture              out picture;
                              }

                              out picture = shoot.picture;
                           }



35                                      Last changed: 2024-09 (succession graphic)                      Release 2026-04

### PDF PAGE 36

Conditional Succession (2)




                         action takePicture : TakePicture {
                           in scene;
           scene            out picture;
      «action»
takePicture : TakePicture   action focus : Focus {
        =                      in scene = takePicture::scene;
           scene               out image;This is a shorthand for a conditional succession
      «action»              }               following the lexically previous action.
        focus
   [image.     image        if focus.image.isFocusedthen shoot;
 isFocused]    image
      «action»              flow focus.image to shoot.image;
        shoot
        =  picture          action shoot : Shoot {
                               in image;
           picture             out picture;
                            }

                            out picture = shoot.picture;
                         }



36                                    Last changed: 2024-09 (succession graphic)                  Release 2026-04

### PDF PAGE 37

References the start of      Merge Nodes
              the action as the source
              of the initial succession.

                                action takePicture : TakePicture {
                                    first start;                               A merge node waits for exactly
                                    then merge continue;                       one predecessor to happen
                continue                                                       before continuing.
                                    then action trigger { out item scene; }
                                    flow trigger.scene to focus.scene;
           trigger                  then action focus : Focus {
                                       in scene;
                 scene                 out image;
                 scene              }
           focus                    flow focus.image to shoot.image;
                                    then action shoot : Shoot {
                 image                 in image;
                 image                 out picture;
           shoot                    }
                                    flow shoot.picture to display.picture;
                 picture            then action display {
                 picture               in picture;
          display                   }

                                    then continue;                   References the merge node named
                                }                                    “continue” as the target of the succession.

37                                   Last changed: 2024-09 (succession graphics)                  Release 2026-04

### PDF PAGE 38

Decision Nodes



                                 action def ChargeBattery {
                                    first start;

           continueCharging         then merge continueCharging;
                                    then action monitor : MonitorBattery {
                                        out batteryCharge : Real;
                                    }                              A decision node (decide keyword) chooses
     monitor                                                       exactly one successor to happen after it.
                                    then decide;
                                       if monitor.batteryCharge < 100 then addCharge;
           [batteryCharge >= 100]      if monitor.batteryCharge >= 100 then endCharging;


    [batteryCharge < 100]           action addCharge : AddCharge {
                                       in charge = monitor.batteryCharge;
    addCharge                       }                                        A decision node is  typically followed
                                    then continueCharging;                   by one or more conditional
                                                                             successions (the last “if…then” can
                  endCharging       action endCharging : EndChargingbe replaced by “;        else”).

                                    then done;
                                                             References the end of the action
                                 }                           as the target of a succession.


38                                    Last changed: 2024-09 (succession graphics)                  Release 2026-04

### PDF PAGE 39

Control Structures


                                          Control-structure actions provide a
                                           structured alternative to control
    A loop action repeatedly               nodes for conditionals and looping.
    performs a body action.                                                      This is the body action, which
                                     action def ChargeBattery {                  is given the name charging.
                                        loop action charging {                   (The default name is body.)
An if action performs its body if a         action monitor : MonitorBattery {
Boolean condition is true. (It can             out charge;
also have an else part, which is            }
performed if the condition is false.)
                                            then if monitor.charge < 100 {                       !  if used in this way
                                               action addCharge : AddCharge {                       represents an action,
until introduces a Boolean                         in charge = monitor.charge;                      not a succession.
condition that terminates the                  }
loop when it is true.                       }

                                        } until charging.monitor.charge >= 100;
 A loop action can also begin
   with while (instead of loop),        then action endCharging : EndCharging;
   introducing a Boolean                then done;
   condition that terminates         }
   the loop when it is false.

39                                               Last changed: 2021-12 (new)                                Release 2026-04

### PDF PAGE 40

Fork and Join Nodes

                                                              A fork node enables all its
                                     action def Brake {       successors to happen after it.

            turnOn                      action turnOn;
                                        then fork;                                   The source for all these
                                           then monitorBrakePedal;                   successions is the fork node.
                                           then monitorTraction;
                                           then braking;

  monitor                               action monitorBrakePedal : MonitorBrakePedal {
 BrakePedal                                out brakePressure; }
                                        then joinNode;
                                        action monitorTraction : MonitorTraction {
                                           out modulationFrequency; }
            monitor                     then joinNode;
            Traction                    flow monitorBrakePedal.brakePressure to
                                               braking.breakPressure;
                                        flow monitorTraction.modulationFrequency to
                      braking                braking.modulationFrequency;
                                        action braking : Braking {
                                           in brakePressure;
                                           in modulationFrequency; }
                                        then joinNode;
                                        join joinNode;               A join node waits for all its predecessors
                                        then done;                   to happen before continuing.
                                     }

40                                       Last changed: 2024-09 (succession graphics)                      Release 2026-04

### PDF PAGE 41

Performed Actions






                                                                              takePhoto is the local name
      perform identifies the                                                  of the performing action.
      owner as the performer           part camera : Camera {
      of an action.                        perform action takePhoto[*] ordered
                                              references takePicture;
                                           part f : AutoFocus {                       The performing action
                                              perform takePhoto.focus;                references the performed
    This shorthand simply                  }                                          action takePicture.
    identifies the performed
    action owned elsewhere                 part i : Imager {
    without renaming it locally.              perform takePhoto.shoot;
                                           }
                                       }








41                                    Last changed: 2022-08 (reference subsetting)                   Release 2026-04

### PDF PAGE 42

Terminate Actions (1)




                                       action def MonitoredActivity {
                                          first start;

                                          then fork;                                            monitorCriticalActivity
                                             then performCriticalActivity;                      and criticalActivity are
 performCriticalActivity                     then waitForTimeOut;                               preformed concurrently.

       «perform»                          action performCriticalActivity {
     monitorCritical                         perform monitorCriticalActivity;
        Activity
                                             perform criticalActivity;
       «perform»                             then terminate;                          A terminate action ends its
     criticalActivity                     }                                           immediately containing action. In
                                          then stop;                                  this case, performCriticalActivity
                                                                                      terminates even if monitorCritical
                                          action waitForTimeOut;                      Activity is still ongoing.
                                          then stop;

     stop             waitForTime         action stop terminate;
                          Out          }                                            This terminates MonitoredActivity
                                                                                    when either performCriticalActivity
                                                                                    or waitForTimeOut completes.

42                                              Last changed: 2024-11 (new)                               Release 2026-04

### PDF PAGE 43

Terminate Actions (2)



                      part def Processor {
                         ref action workflowProcess : WorkflowProcess;

                         action internalProcess {
                            // ...
                         }                                                A terminate action can have an
                      }                                                   argument that identifies the action
                                                                          to be terminated (instead of the
                      action terminateProcessing {                        default to the containing action).
                         in processor : Processor;

                         terminate processor.workflowProcess;

                         terminate processor;                       A terminate action can also be used
                      }                                             to terminate (”destroy”) a part.




                       !  A composite action is automatically terminated when its
                          containing part is terminated, but a referential action is
                          not. That is why workflowProcess was terminated
                          explicitly in this example, but not internalProcess.


43                                                                                                    Release 2026-04

### PDF PAGE 44

Assignment Actions


                              action def ComputeMotion {                                         Using := instead of =
                                 in attribute powerProfile :> ISQ::power[*];                     here indicates an
                                 in attribute vehicleMass :> ISQ::mass;                          initial value, instead
A for loop action repeatedly     in attribute initialPosition :> ISQ::length;                    of a binding.
performs its body, setting a     in attribute initialSpeed :> ISQ::speed;
loop variable to successive      in attribute deltaT :> ISQ::time;
values from the result of a      out attribute positions :> ISQ::length[*] := ( );
sequence expression.             private attribute position := initialPosition;
                                 private attribute speed := initialSpeed;

                                 for vehiclePower in powerProfile {
An action may also be               perform action dynamics : StraightLineDynamics {
performed by another                    in power = vehiclePower;
action (similar to a "call").           in mass = vehicleMass;
                                        in delta_t = deltaT;
                                        in x_in = position; in v_in = speed;
An assignment action sets               out x_out; out v_out;
the value of a feature to the       }
result of an expression at          then assign position := dynamics.x_out;
the time of performance of          then assign speed := dynamics.v_out;                    The functions including
the assignment.                     then assign positions :=                                 comes from the
                                        positions->including(position);
                                 }                                                           SequenceFunctions
                              }                                                              library package.

44                                   Last changed: 2025-02 (changed for loop variable)                  Release 2026-04

### PDF PAGE 45

Asynchronous Messaging


An accept action receives                 This is the name                 This is a declaration of what is being
an incoming asynchronous                  of the action.                   received, which can be anything.
transfer any kind of values.

         trigger             action takePicture : TakePicture {
  accept scene : Scene           action trigger accept scene : Scene;

             =  scene            then action focus : Focus {
                scene               in scene = trigger.scene;

         focus                      out image;
                image            }
                image            flow from focus.image to shoot.image;
                                 then action shoot : Shoot {
         shoot                      in image;
                picture             out picture;               This is an expression that
             =  picture          }                             constructs the value to be sent.

   send toShow(picture) screen   then send new Show(shoot.picture) to screen;
                             }
                                                 The notation “ Show(…)” means
        A send action is an                      to create an instance of the                 This is also an expression,
        outgoing transfer of values              definition Show with the given               evaluating to the target (in this
        to a specific target.                    value for its nested attribute.              case just a feature reference).


45                                        Last changed: 2025-02 (constructor notation)                        Release 2026-04

### PDF PAGE 46

Asynchronous Messaging through Ports


                 viewPort                                                     An accept action can be via a specific
             «part»               part camera : Camera {                      port, meaning that the transfer is
            camera                    port viewPort;                          expected to be received by that port.
                                      port displayPort;
            trigger
      acceptvia  sceneviewPort : Scene action takePicture : TakePicture {
                   scene                 action trigger accept scene : Scene via viewPort;
                =  scene
                                         then action focus : Focus {
             focus                          in scene = trigger.scene;
                   image                    out image;
                                         }
                   image                 flow from focus.image to shoot.image;
            shoot                        then action shoot : Shoot {
                   picture                  in image;
                =  picture                  out picture;
                                         }
       send via Show(picture)displayPort
                                         then send new Show(shoot.picture) via displayPort;
                 displayPort          }
     «interface»                  }An asynchronous transfer sent via a
                 displayPort        port has that port as its source. The        A send action can also be sent via
             «part»                 target of the transfer is determined         a port, meaning that the transfer
             screen                 by what the port is connected to.            is sent out from that port.

46                                     Last changed: 2025-02 (constructor notation)                    Release 2026-04

### PDF PAGE 47

Opaque Actions




                                             action def UpdateSensors {
                                                in sensors : Sensor[*];
                                                 language "Alf"
 An "opaque" action definition or                   /*
 usage can be specified using a                      * for (sensor in sensors) {
 textual representation annotation                   *     if (sensor.ready) {
 in a language other than SysML.                     *         Update(sensor);
                                                     *     }
                                                     * }
                                                     */
                                             }
                                                               The textual representation body is written using comment
                                                               syntax. The /*, */ and leading   * symbols are   not included
                                                               in the body text. Note that support for referencing SysML
                                                               elements from the body text is tool    -specific.

    A textual representation annotation can actually be used with any
     kind of element, not just actions. OMG     -standard languages a tool
     may support include "OCL" (Object Constraint Language) and
     "Alf" (Action Language for fUML). A tool can also provide support
     for other languages (e.g., "JavaScript" or "   Modelica").

47                                        Last changed: 2022 -07 (parameter declaration)                         Release 2026-04

### PDF PAGE 48

State Definitions (1)


 A state definition is like a state machine in
 UML and SysML v1. It defines a behavioral
 state that can be exhibited by a system.                    state def VehicleStates {

                     «state def»                                first start then off;
                    VehicleStates                               state off;                             This indicates the the initial
                                                                                                       state after entry is ”off”.
                                                                transition off_to_starting
                                                                    first off
                                                                    accept VehicleStartSignal
                        «state»                                     then starting;
                          off                                   state starting;                   A state definition can specify  a
                                                                                                  set of discrete nested    states .
                             VehicleStartSignal                 transition starting_to_on
                                                                    first starting
                        «state»                                     accept VehicleOnSignal
                        starting                                    then on;                          States are connected by

                                                                state on;                             transitions  that fire on
                             VehicleOnSignal                                                          acceptance of item transfers
                                                                transition on_to_off                  (like accept actions).
                                                                    first on
                        «state»                                     accept VehicleOffSignal
   VehicleOffSignal       on                                        then off;
                                                             }

48                                      Last changed: 2026  -03 (changed “entry” to ”first start”)                     Release 2026-04

### PDF PAGE 49

State Definitions (2)





                     «state def»
                   VehicleStates

                                                           state def VehicleStates {              This is a shorthand for a
                                                              first start then off;               transition  whose source is
                                                                                                  the lexically previous state.
                       «state»                                state off;
                         off                                  accept VehicleStartSignal
                                                                  then starting;

                            VehicleStartSignal                state starting;
                                                              accept VehicleOnSignal
                       «state»                                    then on;
                       starting                               state on;
                                                              accept VehicleOffSignal
                            VehicleOnSignal                       then off;
                                                           }

                       «state»
   VehicleOffSignal      on





49                                     Last changed: 2026-03 (changed “entry” to ”first start”)                    Release 2026-04

### PDF PAGE 50

State Decomposition





                       «state»                                                                        A state can be explicitly
           vehicleStates : VehicleStates                                                              declared to be a usage
                                                          state def VehicleStates;                    of a state definition.

                                                          state vehicleStates : VehicleStates {
                                                             first start then off;
                       «state»
                         off                                 state off;
                                                             accept VehicleStartSignal
                            VehicleStartSignal                   then starting;
                                                                                                        A state can also be
                                                             state starting;                            directly decomposed
                       «state»                               accept VehicleOnSignal                     into other states.
                       starting                                  then on;

                            VehicleOnSignal                  state on;
                                                             accept VehicleOffSignal
                                                                 then off;
                       «state»                            }

   VehicleOffSignal      on





50                                    Last changed: 2026-03 (changed “entry” to ”first start”)                    Release 2026-04

### PDF PAGE 51

Concurrent States

                      «state»                                                                    A parallel state is one whose
           vehicleStates : VehicleStates
                     «parallel»                                                                  nested states are concurrent.
                      «state»                            state def VehicleStates;
                 operationalStates                       state vehicleStates : VehicleStates parallel {


                                                            state operationalStates {
                                                                first start then off;

                       «state»                                  state off;
                         off                                    accept VehicleStartSignal
                                                                    then starting;
                            VehicleStartSignal
                                                                state starting;
                                                                accept VehicleOnSignal
                       «state»                                      then on;
                      starting
                                                                state on;
                            VehicleOnSignal                     accept VehicleOffSignal
                                                                    then off;
                                                            }                                 !  Transitions are not allowed
                      «state»                               state healthStates {                 between concurrent states.
  VehicleOffSignal       on                                     …
                      «state»                               }
                    healthStates                         }


51                                    Last changed: 2026-03 (changed “entry” to ”first start”)                   Release 2026-04

### PDF PAGE 52

State Entry, Do and Exit Actions
                                                                                                        States, like actions,
                    «state»                                                                             can have parameters.
         vehicleStates : VehicleStates                action performSelfTest{in vehicle : Vehicle;}
                  parameters                          state def VehicleStates{in operatingVehicle : Vehicle;}
^in operatingVehicle : Vehicle
                                                      state vehicleStates : VehicleStates {
                                                         in operatingVehicle : Vehicle;

                                                         first start then off;              An entry action is performed
VehicleOffSignal    «state»                                                                  on entry to a state, a  do
                      off                                state off;                          action while in it, and an  exit
                                                         accept VehicleStartSignal
                         VehicleStartSignal                  then starting;                  action on exit from it.

                                                         state starting;
                    «state»                              accept VehicleOnSignal                   A state entry, do or exit
                    starting                                 then on;                             can reference an action
                                                         state on {                               defined elsewhere…
                         VehicleOnSignal                    entry performSelfTest
                                                                { in vehicle = operatingVehicle; }
                    «state»                                 do action providePower { … }
                      on                                    exit action applyParkingBrake { … }
        entry performSelfTest                            }
        do action providePower                           accept VehicleOffSignal
        exit action applyParkingBrake                        then off;                         … or the action can be
                                                      }                                        defined within the state.

52                                    Last changed: 2026-03 (changed “entry” to ”first start”)                   Release 2026-04

### PDF PAGE 53

Transition Guards and Effect Actions



                    «state»                          action performSelfTest{in vehicle : Vehicle;}
         vehicleStates : VehicleStates
                  parameters                         state def VehicleStates {
^in operatingVehicle : Vehicle                          in operatingVehicle : Vehicle;
^in controller: VehicleController                       in controller : VehicleController; }

                                                     state vehicleStates : VehicleStates {
                                                        in operatingVehicle : Vehicle;
                                                        in controller : VehicleController;A guard is a condition
                   «state»                              first start then off;                          that must be true for a
                     off                                                                               transition to fire.
                        VehicleStartSignal              state off;
                        [brakePedalDepressed]/          accept VehicleStartSignal
                        send ControllerStartSignal()        if operatingVehicle.brakePedalDepressed
                                                            do send new ControllerStartSignal() to controller
                   «state»                                  then starting;
                   starting                             state starting;
                                                        accept VehicleOnSignal              An effect action  is performed
                        VehicleOnSignal                     then on;                        when a transition fires, before
                                                                                            entry to the target state.
                   «state»                              state on { … }
VehicleOffSignal     on                                 accept VehicleOffSignal
                                                            then off;
                                                     }

53                                    Last changed: 2026-03 (changed “entry” to ”first start”)                 Release 2026-04

### PDF PAGE 54

Change and Time Triggers


               «state»                     action senseTemperature { out temp : TemperatureValue; }
            healthStates
             parameters                    state healthStates {                            An absolute time
^in operatingVehicle : Vehicle                in vehicle : Vehicle;                        trigger  fires at a
^in controller: VehicleController             in controller : VehicleControllergiven instant of time.;
                                              do senseTemperature;
               actions                        first start then normal;                               A change trigger fires
do senseTemperature(out temp)                                                                        when a given Boolean

when                                          state normal;                                          expression becomes true.
senseTemperature.temp >                       accept at vehicle.maintenanceTime
vehicle.maxTemperature                            then maintenance;
                                              accept when senseTemperature.temp > vehicle.maxTemperature
                    normal                        do send new OverTemp() to controller
                                                  then degraded;                 !  Time instant quantities are defined in the

   at vehicle.             after 48[h]        state maintenance {                   Time package, not the ISQ package.
   maintenanceTime                                entry assign vehicle.maintenanceTime :=
                                                     vehicle.maintenanceTime + vehicle.maintenanceInterval;
                  maintenance                 }                                      A relative time trigger
                                              accept after 48 [h]
                                                  then normal;                       fires after a given
 when                                                                                time duration.
 senseTemperature.temp <=                     state degraded;
 vehicle.maxTemperature                       accept when senseTemperature.temp <= vehicle.maxTemperature
                   degraded                       then normal;                             Change and time triggers can
                                           }
                                                                                             also be used in accept actions.
54                                    Last changed: 2026-03 (changed “entry” to ”first start”)                  Release 2026-04

### PDF PAGE 55

Local Clocks



Redefining the   localClock             part def Server {
feature of a part provides a                part :>> localClock = new Time::Clock();
local time reference for
composite items, parts and                  attribute today : String;
actions nested within it.                   port requestPort;                                    Each Server instance
                                                                                                 will have its own
                                            state ServerBehavior {                               independent Clock.
  A localClock can also be                    first start then off;
   declared for an item or an                                                                  If no localClock    is declared,
   action (or any kind of                      state off;                                         the default is a universalClock
   occurrence that happens                     accept Start via requestPort                       that provides a common time
   over time).                                     then waiting;                                  universal reference.

                                               state waiting;
                                               accept request : Request via requestPort
  All absolute and relative                        then responding;
  time references are                          accept at new Time::Iso8601DateTime(today + "11:59:00")
  relative to the  localClock  .                   then off;

                                               state responding;
                                               accept after 5 [SI::min]
                                                   then waiting;
                                            }
                                        }

 55                                          Last changed: 2025-02 (constructor notation)                           Release 2026-04

### PDF PAGE 56

Exhibited States








                                         part vehicle : Vehicle {

                                            part vehicleController             : VehicleController;
    exhibit identifies the part             exhibit vehicleStates {
    that is exhibiting states that             in operatingVehicle = vehicle;
    are defined elsewhere.                     in controller = vehicleController;

                                            }

                                         }                         Parameters for a state usage can
                                                                   be bound in the same way as
                                                                   parameters of an action usage.

     ! Like performed actions, exhibited states are
       not composite features, therefore, a localClock
       on a part will not apply to performed actions or
       exhibited states of the part.


56                                       Last changed: 2022-07 (localClock warning)                      Release 2026-04

### PDF PAGE 57

Occurrences, Time Slices and Snapshots (1)


                                   An occurrence is something that happens over time.
                                     Items and parts are structural occurrences. Actions are
                                     behavioral occurrences. Attributes are not occurrences.

                                  attribute def Date;
A time slice represents a
portion of the lifetime of        item def Person;
an occurrence over some                                                                      A succession asserts that the
period of time.                   part def Vehicle {                                         first occurrence ends before
                                     timeslice assembly;                                     the second can begin.

                                     first assembly then delivery;

                                     snapshot delivery;
A snapshot represents an             first delivery then ownership;
occurrence at a specific
point in time (a time slice          timeslice ownership[0..*]                 ordered;
with zero duration).
                                     snapshot junked = done;                              done is the name of the
                                  }                                                       end-of-life snapshot of
                                                     Timeslices and snapshots            any occurrence.
                                                      are suboccurrences.

57                                            Last changed: 2021-10 (successions)                             Release 2026-04

### PDF PAGE 58

Occurrences, Time Slices and Snapshots (2)





                                  part def Vehicle {
                                      …

       This is a shorthand            snapshot delivery {
       for a succession after            attribute     deliveryDate        : Date;
       the lexically previous         }
       occurrence.
                                      then timeslice        ownership[0..*]          ordered {
                                         snapshot sale = start;
                                                                                        start is the name of the
                                         ref item owner : Person[1];                    start-of-life snapshot of
 Time slices and snapshots                                                              any occurrence.
 can have nested time                    timeslice     driven[0..*] {
 slices, snapshots and                      ref item driver : Person[1];
 other features applicable               }
 during their occurrence.             }
                                                                                 One occurrence references
                                      snapshot junked = done;                    another during the same
                                  }                                              time period in the other
                                                                                 reference’s lifetime.



58                                             Last changed: 2021-05 (new)                               Release 2026-04

### PDF PAGE 59

Event Occurrences



  An event occurrence is a
  reference to something that
  happens during the lifetime        part driver : Driver {
  of another occurrence.                event occurrence setSpeedSent          ;
                                     }

                                     part vehicle : Vehicle {
                                        part cruiseController        : CruiseController {
                                           event occurrence setSpeedReceived;
                                           then event occurrence sensedSpeedReceived;
            Event occurrences can          then event occurrence fuelCommandSent;
            be sequenced as usual       }
            using succession.
                                        part speedometer : Speedometer {
                                           event occurrence sensedSpeedSent;
                                        }

                                        part engine : Engine {
                                           event occurrence fuelCommandReceived;
                                        }
                                     }



59                                       Last changed: 2021-05 (new)                        Release 2026-04

### PDF PAGE 60

Messages (1)


An occurrence definition defines
a class of occurrences, without
committing to whether they are
structural or behavioral.
                                   occurrence def CruiseControlInteraction {
                                      ref part :>> driver;
A message asserts that there is       ref part :>> vehicle;
a transfer of some payload of a
certain type from one                 message setSpeedMessage of SetSpeed
occurrence to another                    from driver.setSpeedSent
(specifying the payload type is          to vehicle.cruiseController.setSpeedReceived;
optional).
                                      message sensedSpeedMessage of SensedSpeed
                                         from vehicle.speedometer.sensedSpeedSent
Messages can be explicitly               to vehicle.cruiseController.sensedSpeedReceived;

ordered. Otherwise, they are          message fuelCommandMessage of FuelCommand
only partially ordered by the            from vehicle.cruiseController.fuelCommandSent
time-ordering of their respective        to vehicle.engine.fuelCommandReceived;
source and target events.
                                      first setSpeedMessage then sensedSpeedMessage;
                                   }



60                                 Last changed: 2022-09 (source and target events)              Release 2026-04

### PDF PAGE 61

Messages (2)


                                 occurrence def CruiseControlInteraction {
                                    ref part driver : Driver {
 An event can also be specified        event setSpeedMessage.sourceEvent;
 by reference to an identified      }

 occurrence (such as the source     ref part vehicle : Vehicle {
 or target of a message).              part cruiseController : CruiseController {
                                          event setSpeedMessage.targetEvent;
                                          then event sensedSpeedMessage.targetEvent;
                                          then event fuelCommandMessage.sourceEvent;
                                       }
                                       part speedometer : Speedometer {
                                          event sensedSpeedMessage.sourceEvent;
                                       }
                                       part engine : Engine {
 Each message has a                       event fuelCommandMessage.targetEvent;
 sourceEvent and                       }
 targetEvent, even if it is         }
 not explicitly identified in
 the message declaration.           message setSpeedMessage of SetSpeed;
                                    then message sensedSpeedMessage of SensedSpeed;
                                    message fuelCommandMessage of FuelCommand;
                                 }

61                              Last changed: 2022-09 (sourceEvent and targetEvent)          Release 2026-04

### PDF PAGE 62

Interactions

                                       Event occurrences and messages can be used
                                          together to specify an        interaction    between parts
                                          without committing to          how the interaction happens.

                                                                  «occurrence def»
    !  Sequence diagram                                      CruiseControlInteraction
       graphical notation is                                                                «part»
       purely illustrative.                                                                 vehicle


                   «part»                             «part»                                «part»                                 «part»
                    driver                      cruiseController                        speedometer                                engine


                        message    setSpeedMessage                                                           Succession must be
event occurrence                 of SetSpeed               event   occurrence                                specified explicitly for
     setSpeedSent                                          setSpeedReceived                                  events in different lifelines.
   Succession is implicit between                                                            then
   events on a single lifeline.                            message   sensedSpeedMessage
                                  event occurrence                 of SensedSpeed                 event  occurrence

                              sensedSpeedReceived                                                 sensedSpeedSent

                                                           message   fuelCommandMessage                                      event   occurrence
                                  event  occurrence                of FuelCommand                                            fuelCommandReceived
                                   fuelCommandSent


62                                                   Last changed: 2023    -10 (names not bold)                                     Release 2026-04

### PDF PAGE 63

Interaction Realization by Actions (1)

                                                                                 An interaction can be   realized by many
                             part driver_a : Driver {                             different models. A valid realization
                                perform action driverBehavior {                   must have   suboccurrences    that can be
                                    send SetSpeed() to vehicle_a;                 identified with all the events and
                                }                                                 messages in the interaction.
In this model, event         }
occurrences are              part vehicle_a : Vehicle {
realized by nested send         part cruiseController_a : CruiseController {
and accept actions.                 perform action controllerBehavior {
                                       accept SetSpeed via vehicle_a;
                                       then accept SensedSpeed via cruiseController_a;
                                       then send new FuelCommand() to engine_a;
                                    }
                                }

                                part speedometer_a : Speedometer {
Messages are realized               perform action speedometerBehavior {
by the implicit transfers              send new SensedSpeed() to cruiseController_a;
                                    }
between send actions            }
and corresponding                                                                        In more realistic cases, a
accept actions.                 part engine_a : Engine {                                    realizing model will have more
                                    perform action engineBehavior {                         extensive behavior, only a
                                       accept FuelCommand via engine_a;                     subset of which will conform
                                    }                                                       to any one interaction model.
                                }
                             }

63                                             Last changed: 2021-10 (accept via)                             Release 2026-04

### PDF PAGE 64

Interaction Realization by Actions (2)





                                                                  «occurrence»
                                            cruiseControlInteraction_a : CruiseControlInteraction

                                                                                         «part»
                                                                                       vehicle_a

                   «part»                           «part»                               «part»                                «part»
                 :>> driver                  :>> cruiseController                   :>> speedometer                          :>> engine
                :>> driver_a                :>> cruiseController_a                :>> speedometer_a                        :>> engine_a
                  perform                          perform                              perform                               perform
             driverBehavior            cruiseControllerBehavior                 speedometerBehavior                      engineBehavior
                                 SetSpeed
 send setSpeed    ()                                     accept setSpeed                                This succession from the
                                                                                     then               interaction may not actually
                                                                                                        be satisfied by the realization.
                              accept SensedSpeed                   SensedSpeed                 send  SensedSpeed    ()





                              send  FuelCommand    ()             FuelCommand                                                       accept
                                                                                                                                    FuelCommand



64                                                 Last changed: 2023   -10 (names not bold)                                    Release 2026-04

### PDF PAGE 65

Interaction Realization by Flows (1)



                              part driver_b     : Driver {
                                  port  setSpeedPort     {                     Ports are also suboccurrences
                                     out setSpeed : SetSpeed;                   of the parts that contain them.
In this model, event              }
                              }
occurrences are realized      interface driver_b.setSpeedPort to vehicle_b.setSpeedPort {
by values leaving from            flow of SetSpeed      from driver_b.setSpeedPort.setSpeed
and arriving at ports.               to vehicle_b.setSpeedPort.setSpeed;
                              }
                              part vehicle_b : Vehicle {
                                  port setSpeedPort {
                                     in setSpeed : SetSpeed;
                                  }
                                  part cruiseController_b : CruiseController {
                                     port setSpeedPort {
                                         in setSpeed : SetSpeed = vehicle_b.setSpeedPort.setSpeed;
Messages are realized by             }
explicit flows between               port sensedSpeedPort {
                                         in sensedSpeed : SetSpeed;
features of ports.                   }
                                     …
                                  }
                                  flow of SensedSpeed       from speedometer_b.sensedSpeedPort.sensedSpeed
                                    to cruiseController_b.sensedSpeedPort.sensedSpeed;
                                  part speedometer_b : Speedometer {
                                     port sensedSpeedPort {
                                         out sensedSpeed : SensedSpeed;
                                     }
                                  }
                              …
 65                                         Last changed: 2025-02 (constructor notation)                         Release 2026-04

### PDF PAGE 66

Interaction Realization by Flows (2)





                                                                  «occurrence»
                                            cruiseControlInteraction_b : CruiseControlInteraction

                                                                                          «part»
                                                                                        vehicle_b

                   «part»                           «part»                                «part»                                «part»
                 :>> driver                  :>> cruiseController                   :>> speedometer                          :>> engine
                :>> driver_b                :>> cruiseController_b                 :>> speedometer_b                        :>> engine_b
               port                     port                      port                         port                             port
     setSpeedPort            setSpeedPort            port         fuelCommandPort              sensedSpeedPort           fuelCommandPort
                                              sensedSpeedPort              This is a snapshot of

                        flow of   SetSpeed                                 when the     setSpeed     is
     out setSpeed                               in setSpeed                received into the port.

                                                                                   then
                                    in SensedSpeed            flow of   SensedSpeed            out SensedSpeed
This is a snapshot of
when the     setSpeed     is
sent out of the port.
                                  out  FuelCommand            flow of   FuelCommand                                                  in
                                                                                                                                     FuelCommand



66                                                  Last changed: 2023   -10 (names not bold)                                    Release 2026-04

### PDF PAGE 67

Message Payloads


                                                                      The default name for a
        message    setSpeedMessage      of SetSpeed                     message payload is payload.
           from driver.setSpeedSent
           to vehicle.cruiseController.setSpeedReceived;                     The payload of a message
        then message sensedSpeedMessage of SensedSpeed                       can be declared with a
           from vehicle.speedometer.sensedSpeedSent                          name for reference.
           to vehicle.cruiseController.sensedSpeedReceived;

        then message fuelCommandMessage of fuelCommand : FuelCommand
           from vehicle.cruiseController.fuelCommandSent
           to vehicle.engineController.fuelCommandReceived;

        then message fuelCommandForwardingMessage
           of fuelCommand : FuelCommand           = fuelCommandMessage.fuelCommand
           from vehicle.engineController.fuelCommandForwarded
           to vehicle.engine.fuelCommandReceived;


    ! Note that a payload declaration                      The payload of a message can also be bound to
      without a colon names the type of                    a specific value. In this case, the
      the payload, not the payload itself.                 fuelCommandMessage payload is forwarded by
                                                           the engineController to the engine.


67                                        Last changed: 2022-10 (new)                        Release 2026-04

### PDF PAGE 68

Individuals and Snapshots (1)





                                        An individual definition is an                        An individual definition will
                                        occurrence definition (of any kind)                   often specialize a definition of
                                        restricted to model a single individual               the general class of things the
                                        and how it changes over its lifetime.                 individual is one of.
 As occurrences,
 individuals can have
 snapshots that                  individual part def Vehicle_1 :> Vehicle {
 describe them at a
 single instant of time.             snapshot part vehicle_1_t0 : Vehicle_1 {

                                        :>> mass = 2000.0;
                                        :>> status {
 This is a compact                          :>> gearSetting = 0;
 notation for showing                       :>> acceleratorPosition = 0.0;
 redefinition of an                     }
 attribute usage.                    }                                                           An attribute does not have
                                 }                                                               snapshots, but it can be
                                                                                                 asserted to have a specific
                                                                                                 value in a certain snapshot.



68                                      Last changed: 2024-02 (removed PhysicalContext)                          Release 2026-04

### PDF PAGE 69

Individuals and Snapshots (2)




                           individual part def Vehicle_1 :> Vehicle {

                              snapshot part vehicle_1_t0 : Vehicle_1 {
                                 :>> mass = 2000.0;
                                 :>> status {
                                    :>> gearSetting = 0;
                                    :>> acceleratorPosition = 0.0;
                                 }
                              }

                              snapshot part vehicle_1_t1 : Vehicle_1 {
                                 :>> mass = 1500.0;                               The values of the attributes
  As usual, succession asserts   :>> status {                                     of an individual can change
  that the first snapshot           :>> gearSetting = 2;                          over time.
  occurs before the second in       :>> acceleratorPosition = 0.5;
  time, in some context.         }
                              }

                              first vehicle_1_t0 then vehicle_1_t1;
                           }



69                                  Last changed: 2021-05 (occurrence modeling)                 Release 2026-04

### PDF PAGE 70

Individuals and Roles



                        individual      part def Vehicle_1 :> Vehicle {
                           part leftFrontWheel          : Wheel;
                           part rightFrontWheel           : Wheel;
                        }
                        individual part        def Wheel_1 :> Wheel;                    During the first snapshot of
                                                                                        vehicle_1, Wheel_1 has the
                        individual part        vehicle_1 : Vehicle_1 {                  role of the leftFrontWheel.


                           snapshot part       vehicle_1_t0 {
An individual usage           snapshot     leftFrontWheel_t0 : Wheel_1 :>>                 leftFrontWheel       ;
represents an              }
individual during some
portion of its lifetime.   then snapshot part          vehicle_1_t1 {
                              snapshot     rightFrontWheel_t1 : Wheel_1 :>>                 rightFrontWheel       ;
                           }
                        }

                                                                                       During a later snapshot, the
                                                                                       same Wheel_1 has the role
                                                                                       of the rightFrontWheel.



70                                       Last changed: 2024-02 (revised call-outs)                    Release 2026-04

### PDF PAGE 71

Individuals and Time Slices


 A time slice represents      individual item         def Alice :> Person;
 an individual over           individual item         def Bob :> Person;
 some period of time                                                                        During this time slice of
 (that this is a time slice   individual part         : Vehicle_1 {                         Vehicle_1, the Alice has
 of a part is implicit).                                                                    the role of the driver.
                                  timeslice     aliceDriving        {
                                     ref individual item           :>> driver : Alice;
 start and done are
 snapshots at the                    snapshot     :>> start {
 beginning and end of                   :>> mass = 2000.0;
 the time slice.                     }

                                     snapshot     :>> done {
 Succession asserts that                :>> mass = 1500.0;
 the first time slice must           }                                                      During a later time slice
 complete before the              }                                                         of Vehicle_1, Bob has the
 second can begin.                                                                          role of the driver.
                                  then timeslice bobDriving {
                                     ref individual item :>> driver : Bob;
                                  }
                              }




71                                     Last changed: 2021-05 (occurrence modeling)                       Release 2026-04

### PDF PAGE 72

Expressions and Feature Values




          package    MassRollup1 {                                       ISQ::mass is a standard quantity
             private import        ScalarFunctions        ::*;           kind from the International System
             part def     MassedThing       {                            of Quantities library model.

                attribute      simpleMass      :> ISQ::mass;
                attribute      totalMass      :> ISQ::mass;              A feature value is a shorthand for binding
             }                                                           a feature to the result of an expression
                                                                         (here simply the value of another
             part simpleThing         : MassedThing {                    feature).
                attribute :>> totalMass = simpleMass;
             }

             part compositeThing : MassedThing {
                part subcomponents: MassedThing[*];
                attribute :>> totalMass =
                   simpleMass + sum(subcomponents.totalMass);
             }
          }
                An expression in general is a                  The dot notation can be used as an expression to read
                computation expressed using a typical          the values of a feature. Here, the totalMass is
                mathematical operator notation.                collected for each of the subcomponents.


72                                       Last changed: 2024-07 (import visibility)                     Release 2026-04

### PDF PAGE 73

Car Mass Rollup Example (1)



                      private import ScalarValues::*;
                      private import MassRollup1::*;

                      part def CarPart :> MassedThing {
                         attribute serialNumber : String;
                      }
                      part car: CarPart :> compositeThing {
                         attribute vin :>> serialNumber;
                         part carParts : CarPart[*] :>> subcomponents;
                         part engine :> simpleThing, carParts { … }
                         part transmission :> simpleThing, carParts { … }
                      }
                                                                              This is an expression for a quantity
                      // Example usage                                        with a specific numeric value and
                      private import SI::kg;                                  unit. Note that units are identified
                      part c :> car {                                         on the quantity value, not the type.
                         attribute :>> simpleMass = 1000[kg];
                         part :>> engine {
                             attribute :>> simpleMass = 100[kg];
                         }
                         part attribute transmission {
                             attribute :>> simpleMass = 50[kg];
                         }                                              The totalMass   of c can be computed
                      }                                                 using the feature value expressions from

                      // c.totalMass --> 1150.0[kg]                     simpleThing   and compositeThing   .

73                                        Last changed: 2024-11 (import visibility)                      Release 2026-04

### PDF PAGE 74

Default Values





   package    MassRollup2 {                                          A default value is feature value that
      private import       ScalarFunctions       ::*;                applies unless explicitly overridden.
      part def     MassedThing      {
         attribute     simpleMass      :> ISQ::mass;
         attribute     totalMass     :> ISQ::mass        default simpleMass        ;
      }                                                              A default value can be overridden
      part compositeThing         : MassedThing {                    when the feature is redefined,
         part subcomponents: MassedThing[*];                         with a default or bound value.
         attribute :>> totalMass default mass + sum(subcomponents.totalMass);
      }
                                                       Once bound, the value of the
                                                       feature is fixed as the result of the
      part filteredMassThing :> compositeThing {
         attribute minMass : ISQ::mass                 value expression.
         attribute :>> totalMass =
            sum(subcomponents.totalMass.?{in p:>ISQ::mass; p >= minMass)});
      }
   }          A dot can be followed by a
              select expression in order to
              filter a collection of values.


74                                      Last changed: 2024-07 (import visibility)                  Release 2026-04

### PDF PAGE 75

Car Mass Rollup Example (2)


                      private alarValues::*;                       The default of totalMass to
                      private import MassRollup2::*;               simpleMass is inherited.


                      part def CarPart :> MassedThing {                       The default for totalMass is overridden
                         attribute serialNumber : String;                     as specified in compositeThing.
                      }
                      part car: CarPart :> compositeThing {
                         attribute vin :>> serialNumber;
                         part carParts : CarPart[*] :>> subcomponents;
                         part engine :> carParts { … }
                         part transmission :> carParts { … }
                      }

                      // Example usage                            The totalMass default is not
                      private import SI::kg;                      overridden for the nested carParts.
                      part c :> car {
                         attribute :>> simpleMass = 1000[kg];
                         part :>> engine {
                             attribute :>> simpleMass = 100[kg];
                         }
                         part attribute transmission {
                             attribute :>> simpleMass = 50[kg];
                         }                                              When computing the     totalMass
                      }                                                 of c, c.engine and c.transmission,

                      // c.totalMass --> 1150.0[kg]                     the relevant defaults are used.

75                                        Last changed: 2024-11 (import visibility)                       Release 2026-04

### PDF PAGE 76

Calculation Definitions
                  A calculation definition is a reusable,
                  parameterized expression.


calc def Power {                               Similarly to actions, the directed features
   in whlpwr : PowerValue;                     of a calculation are its parameters.
   in Cd : Real;
   in Cf : Real;                       A calculation has a
   in tm : MassValue;
   in v : SpeedValue;                  single return result.
   return : PowerValue;
   attribute drag = Cd * v;                    The calculation can include the
   attribute friction = Cf * tm * v;computation of intermediate values.
                                                                                              !  There is no semicolon
   whlpwr - drag - friction                    The calculation result expression must            at the end of a result
}                                              conform to the return type.                       expression.

calc def Acceleration { in tp: PowerValue; in tm : MassValue; in v: SpeedValue;
   return : AccelerationValue = tp / (tm * v);                              The result expression can also be bound
}                                                                           directly to the return parameter.

calc def Velocity { in dt : TimeValue; in v0 : SpeedValue; in a : AccelValue;
   return : SpeedValue = v0 + a * dt;
}

calc def Position (dt : TimeValue; x0 : LengthValue; v : SpeedValue;
   return : LengthValue = x0 + v * dt;
}

76                                        Last changed: 2022-07 (parameter declaration)                        Release 2026-04

### PDF PAGE 77

Calculation Usages (1)

                                     part def VehicleDynamics {
                                         attribute C_d : Real;
                                         attribute C_f : Real;
                                         attribute wheelPower : PowerValue;
                                         attribute mass : MassValue;
Values are bound to the                  action straightLineDynamics { in delta_t : TimeValue;
parameters of   calculation usages          in v_in : SpeedValue; in x_in : LengthValue;
(similar to action parameters).             calc acc : Acceleration {
                                                in tp = Power(wheelPower, C_d, C_f, mass, v_in);
                                                in tm = mass;
                                                in v = v_in;                       A calculation definition can also be
                                                return a;                          invoked as an expression, with input
                                            }
                                            calc vel : Velocity {                  values given as arguments, evaluating
                                                in dt = delta_t;                   to the result of the calculation.
                                                in v0 = v_in;
                                                in a = acc.a;
                                                return v;
                                            }
                                            calc pos : Position {                 Calculation results can be
                                                in dt = delta_t;                  referenced by name (they are
                                                in x0 = x_in;
                                                in v = vel.v;                     output parameters).
                                                return x;
                                            }

                                            out v_out : SpeedValue = vel.v;
                                            out x_out : LengthValue = pos.x;
                                         }
                                     }
77                                              Last changed: 2023-10 (output binding)                              Release 2026-04

### PDF PAGE 78

Calculation Usages (2)




attribute def DynamicState {
   attribute v: SpeedValue;
   attribute x: LengthValue;
}

part def VehicleDynamics {
   attribute C_d : Real;
   attribute C_f : Real;
   attribute wheelPower : PowerValue;
   attribute mass : MassValueA calculation can be ;
                                    specified without an explicit         Calculations can also
                                    calculation definition.
   calc updateState {                                                     handle structured values.
      in delta_t : TimeValue; in currState : DynamicState;

      attribute totalPower : PowerValue =                                     This is a declaration of the result
         Power(wheelPower, C_d, C_f, mass, currState.v);                      parameter  of the calculation, with
                                                                              bound subattributes  .
      return attribute newState : DynamicState {
         :>> v = Velocity(delta_t, currState.v, Acceleration(totalPower, mass, currState.v));
         :>> x = Position(delta_t, currState.x, currState.v);
      }
   }
}


 78                                     Last changed: 2022-07 (parameter declaration)                      Release 2026-04

### PDF PAGE 79

Constraint Definitions (1)


                                private import ISQ::*;                  A constraint definition is a reusable,
                                private import SI::*;                   parameterized Boolean expression.
                                private import ScalarFunctions::*;
                                constraint def MassConstraint {                         Constraint parameters are always
                                   in partMasses : MassValue[0..*];                     in parameters.

 !  There is no semicolon          in massLimit : MassValue;
    at the end of a                sum(partMasses) <= massLimit                     The constraint expression can be
    constraint expression.      }                                                   any Boolean expression using
                                                                                    the constraint parameters.
                                part def Vehicle {
                                   constraint massConstraint : MassConstraint {
                                      in partMasses = (chassisMass, engine.mass, transmission.mass);
                                      in massLimit = 2500[kg];
 A constraint is the usage         }
 of a constraint definition,                                                          Values are bound to
 which may be true or              attribute chassisMass : MassValue;                 constraint parameters
 false in a given context.         part engine : Engine {                             (similarly to actions).
                                      attribute mass : MassValue;
  A constraint may be             }

     violated (false) without      part transmission : Transmission {
     making the model                 attribute mass : MassValue;
     inconsistent.                 }
                                }

79                                          Last changed: 2024-07 (import visibility)                        Release 2026-04

### PDF PAGE 80

Constraint Definitions (2)



                private import ISQ::*;
                private import SI::*;
                private import ScalarFunctions::*;
                                                                          Alternatively, constraint
                constraint def MassConstraint {                           parameters may be modeled as
                   attribute partMasses : MassValue[0..*];                attribute or reference features.
                   attribute massLimit : MassValue;

                   sum(partMasses) <= massLimit
                }

                part def Vehicle {
                   constraint massConstraint : MassConstraint {
                      redefines partMasses = (chassisMass, engine.mass, transmission.mass);
                      redefines massLimit = 2500[kg];
                   }
                   attribute chassisMass : MassValue;             The constraint parameter
                                                                  properties are then redefined
                   part engine : Engine {                         in order to be bound.
                      attribute mass : MassValue;
                   }

                   part transmission : Engine {
                      attribute mass : MassValue;
                   }
                }

80                                        Last changed: 2024-07 (import visibility)                     Release 2026-04

### PDF PAGE 81

Constraint Assertions (1)



                              private import ISQ::*;
                              private import SI::*;
                              private import ScalarFunctions::*;

                              constraint def MassConstraint {
                                 in partMasses : MassValue[0..*];
                                 in massLimit : MassValue;

                                 sum(partMasses) <= massLimit
                              }

                              part def Vehicle {
                                 assert constraint massConstraint : MassConstraint {
                                    in partMasses = (chassisMass, engine.mass, transmission.mass);
                                    in massLimit = 2500[kg];
 A constraint assertion          }
 asserts that a constraint       attribute chassisMass : MassValue;
 must be true.
                                 part engine : Engine {
                                    attribute mass : MassValue;
  If an assertion is            }

    violated, then the           part transmission : Engine {
    model is inconsistent.          attribute mass : MassValue;
                                 }
                              }

81                                       Last changed: 2024-07 (import visibility)                     Release 2026-04

### PDF PAGE 82

Constraint Assertions (2)




The constraint expression     constraint def MassConstraint {
can also be defined on a         in partMasses : MassValue[0..*];
usage of a constraint def.       in massLimit : MassValue;
                              }
                              constraint massConstraint : MassConstraint {
                                 sum(partMasses) <= massLimit            A named constraint
                              }
                                                                         can be asserted in
                              part def Vehicle {                         multiple contexts.
                                 assert massConstraint  {
                                     in partMasses = (chassisMass, engine.mass, transmission.mass);
                                     in massLimit = 2500[kg];
                                 }

                                 attribute chassisMass : MassValue;

                                 attribute engine : Engine {
                                     value mass : MassValue;
                                 }

                                 attribute transmission : Engine {
                                     value mass : MassValue;
                                 }
                              }


82                                Last changed: 2023-12 (updated constraint def and usage)               Release 2026-04

### PDF PAGE 83

Derivation Constraints



                                                 In UML and SysML v1, constraints are
                                                 often used to define  derived values.
    part vehicle1 : Vehicle {
       attribute totalMass : MassValue;
       assert constraint {totalMass == chassisMass +                  engine.mass + transmission.mass}
    }

    part vehicle2 : Vehicle {
       attribute totalMass : MassValue = chassisMass +                   engine.mass + transmission.mass;
    }
                                                         In SysML v2 this can usually be
    constraint def AveragedDynamics {                    done more directly using a binding.
       in mass: MassValue;
       in initialSpeed : SpeedValue;
       in finalSpeed : SpeedValue;
       in deltaT : TimeValue;                                                           !  Be careful about the
       in force : ForceValue;                                                              difference between    ==,
                                                                                           which is the Boolean-valued
       force * deltaT == mass * (finalSpeed - initialSpeed) and                            equality operator, and =,
       mass > 0[kg]                                                                        which denotes binding.
    }                                  However, constraints
                                       allow for more general
                                       equalities and inequalities
                                       than direct derivation.


83                                      Last changed: 2022-07 (parameter declaration)                        Release 2026-04

### PDF PAGE 84

Analytical Constraints

                                                                                   This constraint definition
constraint def StraightLineDynamicsEquations {                                     provides a reusable
   in p : PowerValue, in m : MassValue, in dt : TimeValue;                         specification of a system
   in x_i : LengthValue; in v_i : SpeedValue;                                      of (coupled) equations.
   in x_f : LengthValue; in v_f : SpeedValue,
   in a : AccelerationValue;

   attribute v_avg : SpeedValue = (v_i + v_f)/2;

   a == Acceleration(p, m, v_avg) and                  Note the use of the            An action definition is inherently
   v_f == Velocity(dt, v_i, a) and                      calculation definitions        "causal" in the sense that outputs
   x_f == Position(dt, x_i, v_avg)                      defined earlier.               are determined in terms of inputs.
}

action def StraightLineDynamics {
   in power : PowerValue; in mass : MassValue; in delta_t : TimeValue;
   in x_in : LengthValue; in v_in : SpeedValue;                                                 A constraint is inherently
   out x_out : LengthValue; out v_out : SpeedValue;                                             "acausal" – it is simply true
   out a_out : AccelerationValue;
                                                                                                or false for given values of
   assert constraint dynamics : StraightLineDynamicsEquations {                                 its parameters.
       in p = power; in m = mass; in dt = delta_t;
       in x_i = x_in; in v_i = v_in;
       in x_f = x_out; in v_f = v_out;                 This specifies that the action outputs
       in a = a_out;                                    must be solved for analytically given
   }                                                    the action inputs, consistent with
}                                                       the asserted constraint.


84                                       Last changed: 2022-07 (parameter declaration)                       Release 2026-04

### PDF PAGE 85

Time Constraints



                                                               TimeOf and DurationOf      are from
              state healthStates {                              the Time package in the Quantities
                  in vehicle : Vehicle;                         and Units Domain Library.

                  entry; then normal;
                                                                 TimeOf returns the time of the
                  state normal;                                  start of an occurrence (in this
                  accept at vehicle.maintenanceTime              example, a state performance).
                     then maintenance;

                  state maintenance {
                     assert constraint { TimeOf(maintenance) > vehicle.maintenanceTime }
                     assert constraint { TimeOf(maintenance) - TimeOf(normal.done) < 2 [s]
              }
                     entry assign vehicle.maintenanceTime :=
                        vehicle.maintenanceTime + vehicle.maintenanceInterval;
                  }
                  accept MaintenanceDone
                     then normal;

                  constraint { DurationOf(maintenance) <= 48 [h] }

              }                                       DurationOf    returns the time duration
                                                      of an occurrence (the different
                                                      between its start and done times).

85                                              Last changed: 2022-01 (new)                                Release 2026-04

### PDF PAGE 86

Requirement Definitions (1)



                                                                              A textual statement of the requirement can
             A requirement definition   is a special                          be  given as a documentation comment in
             kind of constraint definition.                                   the requirement definition body.



                                        requirement def MassLimitationRequirement {
                                            doc /* The actual mass shall be less than or equal
                                             * to the required mass. */

                                            attribute massActual : MassValue;
  Like a constraint definition,             attribute massReqd : MassValue;
  a requirement definition                  require constraint { massActual <= massReqd }
  can be parameterized                  }
  using features.                                                                            The requirement can be
                                                                                             formalized by giving one or
                                                                                             more component required
                                                                                             constraints.








86                                                  Last changed: 2020-08                                     Release 2026-04

### PDF PAGE 87

Requirement Definitions (2)







 part def Vehicle {
     attribute dryMass: MassValue;
     attribute fuelMass: MassValueA requirement definition may have ;                      Actually, any identifiable
     attribute fuelFullMass: MassValuea modeler specified ;     short name,
     …                                                                                      element can have a short
 }                                        which is an alternate name for it.                name, not just requirements.

 requirement def <'1’> VehicleMassLimitationRequirement :> MassLimitationRequirement {
     doc /* The total mass of a vehicle shall be less than or equal to the required mass. */

     subject vehicle : Vehicle;                      A requirement definition is always about some
                                                     subject, which may be implicit or specified explicitly.

     attribute redefines massActual = vehicle.dryMass + vehicle.fuelMass;

     assume constraint { vehicle.fuelMass > 0[kg] }
 }
                                                                                                  Features of the subject
                                                   A requirement definition may also              can be used in the
                                                   specify one or more    assumptions.            requirement definition.




87                                     Last changed: 2023-10 ("human id" to "short name")                     Release 2026-04

### PDF PAGE 88

Requirement Definitions (3)





                              The subject of a requirement definition
                              can have any kind of definition.

   port def ClutchPort;
   action def GenerateTorque;

   requirement def <'2’> DrivePowerInterfaceRequirement {
      doc /* The engine shall transfer its generated torque to the transmission
       * via the clutch interface. */
      subject clutchPort: ClutchPort;
   }

   requirement def <'3’> TorqueGenerationRequirement {
      doc /* The engine shall generate torque as a function of RPM as shown in Table 1. */
      subject generateTorque: GenerateTorque;
   }










88                                       Last changed: 2021-10 (requirement id)                      Release 2026-04

### PDF PAGE 89

Requirement Usages




A requirement may optionally                                  A requirement is the usage of a
have its own short name.                                      requirement definition.


        requirement <'1.1’> fullVehicleMassLimit : VehicleMassLimitationRequirement {
           subject vehicle : Vehicle;
           attribute :>> massReqd = 2000[kg];                     A requirement will often bind
                                                                  requirement definition
           assume constraint {                                    parameters to specific values.
              doc /* Fuel tank is full. */
              vehicle.fuelMass == vehicle.fuelFullMass
           }
        }

        requirement <'1.2’> emptyVehicleMassLimit : VehicleMassLimitationRequirement {
           subject vehicle : Vehicle;
           attribute :>> massReqd = 1500[kg];

           assume constraint {
              doc /* Fuel tank is empty. */
              vehicle.fuelMass == 0[kg]
           }
        }




89                                   Last changed: 2023-10 ("human id" to "short name")                  Release 2026-04

### PDF PAGE 90

Requirement Groups
A requirement may also be used                                                  Grouped requirements are treated as
to group other requirements.                                                     required constraints of the group.


                             requirement vehicleSpecification {
                                 doc /* Overall vehicle requirements group */
                                 subject vehicle : Vehicle;
                                                                                    By default, the subject of grouped
                                 require fullVehicleMassLimit;                      requirements is assumed to be the
                                 require emptyVehicleMassLimit;                     same as that of the group.
                             }
Requirements  can be
grouped by reference…        part def Engine {
                                 port clutchPort: ClutchPort;
                                 perform action generateTorque: GenerateTorque;
                             }                                                               The subject of a grouped

                             requirement engineSpecification {                               requirement can also be
   …or by composition.           doc /* Engine power requirements group */                   bound explicitly.
                                 subject engine : Engine;

                                 requirement drivePowerInterface : DrivePowerInterfaceRequirement {
                                     subject clutchPort = engine.clutchPort;
                                 }

                                 requirement torqueGeneration : TorqueGenerationRequirement {
                                     subject generateTorque = engine.generateTorque;
                                 }
                             }

90                                          Last changed: 2021-04 (dot notation)                          Release 2026-04

### PDF PAGE 91

Requirement Satisfaction








                part vehicle_c1 : Vehicle {
                    part engine_v1: Engine { … }                                     A requirement satisfaction asserts
                    …                                                                that a given requirement is satisfied
                }
                                                                                     when its subject parameter is
                part 'Vehicle c1 Design Context' {                                   bound to a specific thing.
                    ref vehicle_design :> vehicle_c1;

                    satisfy vehicleSpecification by vehicle_design;
                    satisfy engineSpecification by vehicle_design.engine_v1;
                }



                                    Formally, a requirement is     satisfied for a subject
                                      if, when all its assumed constraints are true, then
                                      all its required constraints are true.






91                                            Last changed: 2021-04 (dot notation)                              Release 2026-04

### PDF PAGE 92

Analysis Case Definitions (1)

             An analysis case definition   defines the
             computation of the result of analyzing
             some subject, meeting an     objective.
                                                            The subject may be specified similarly to
      analysis def FuelEconomyAnalysis {                    the subject of a requirement definition.
         subject vehicle : Vehicle;
         objective fuelEconomyAnalysisObjective {                                 The objective is a requirement on
             doc /*                                                               the result of the analysis case.
              * The objective of this analysis is to determine whether the
              * subject vehicle can satisfy the fuel economy requirement.
              */

             assume constraint {
                vehicle.wheelDiameter == 33['in’] and                             The analysis objective is specified as a
                vehicle.driveTrainEfficiency == 0.4                               requirement, allowing both assumed
             }                                                                    and required constraints.

             require constraint {
                 fuelEconomyResult > 30[mi / gallon]
             }                                                                  The analysis result is declared as a return
         }                                                                      result (as for a calculation definition).
         …

         return fuelEconomyResult : DistancePerVolumeValue = …;
      }


92                                            Last changed: 2024 -12 (return result)                           Release 2026-04

### PDF PAGE 93

Analysis Case Definitions (2)



                                   attribute def WayPoint {
                                          time : TimeValue;
                                          position : LengthValue;
The steps of an analysis case             speed : SpeedValue;
are actions that, together,        }
                                   analysis def FuelEconomyAnalysis {
compute the analysis result.          subject vehicle : Vehicle;
                                      objective fuelEconomyAnalysisObjective { … }
                                      in attribute scenario : WayPoint[*];                      Additional parameters
                                      action solveForPower {
                                          out power: PowerValue[*];                             can be specified in the
                                          out acceleration: AccelerationValue[*];               case body.
The first step solves for the             assert constraint {
engine power needed for a                    (1..size(scenario)-1)->forAll {in i : Positive;
given position/velocity scenario.                StraightLineDynamicsEquations (
                                                    power#(i), vehicle.mass,
                                                    scenario.time#(i+1) – scenario.time#(i),
The second step computes the fuel                   scenario.position#(i), scenario.speed#(i),
economy result, given the power                     scenario.position#(i+1), scenario.speed#(i+1),
profile determined in the first step.               acceleration#(i+1)))
                                          }
                                      }
                                      then action solveForFuelEconomy {
                                          in power : PowerValue[*] = solveForPower.power;
                                          out fuelEconomy : DistancePerVolumeValue;
                                          …
                                      }
                                      return fuelEconomyResult : DistancePerVolumeValue;
                                                    = solveForFuelEconomy.fuelEconomy;
                                   … }

93                                             Last changed: 2024-12 (return result)                             Release 2026-04

### PDF PAGE 94

Analysis Case Usages




part vehicleFuelEconomyAnalysisContext {

   requirement vehicleFuelEconomyRequirements{subject vehicle : Vehicle; … }

   attribute cityScenario : WayPoint[*] = { … };
   attribute highwayScenario : WayPoint[*] = { … };

   analysis cityAnalysis : FuelEconomyAnalysis {
      subject vehicle = vehicle_c1;                                           The previously defined analysis is carried
      in scenario = cityScenario;                                             out for a specific vehicle configuration
   }
                                                                              for two different scenarios.
   analysis highwayAnalysis : FuelEconomyAnalysis {
      subject vehicle = vehicle_c1;
      in scenario = highwayScenario;                                          The subject and parameters are
   }                                                                          automatically redefined, so redefinition
   part vehicle_c1 : Vehicle {                                                does not need to be specified explicitly.
      …
      attribute :>> fuelEconomy_city = cityAnalysis.fuelEconomyResult;
      attribute :>> fuelEconomy_highway = highwayAnalysis.fuelEconomyResult;
   }                                                                                If the vehicle fuel economy is set to
                                                                                    the results of the analysis, then this
   satisfy vehicleFuelEconomyRequirements by vehicle_c1;                            configuration is asserted to satisfy the
}                                                                                   desired fuel economy requirements.

94                                          Last changed: 2022-05 (use of WayPoint)                          Release 2026-04

### PDF PAGE 95

Trade-off Study Analysis

The TradeStudy    analysis definition from the                                  A trade  -off study is an analysis with the
TradeStudies    domain library model provides a general                          objective of selecting the optimum
framework for defining basic trade study analyses.                               alternative from a given set based on
                                                                                 an evaluation of each alternative.

 analysis engineTradeStudy : TradeStudies::TradeStudy {                       Bind the analysis subject to the set of
     subject : Engine = (engine4cyl, engine6cyl);
     objective : MaximizeObjective;                                           study alternatives. Select either
     calc :>> evaluationFunction {                                            MaximizeObjective     or MinimizeObjective   .

        in part anEngine :>> alternative : Engine;                                   Redefine the  evaluationFunction
        calc powerRollup: PowerRollup {in engine = anEngine;
            return power : ISQ::PowerValue; }                                        calculation to provide an evaluation
        calc massRollup: MassRollup {in engine = anEngine;                           of each one of the alternatives.
            return mass : ISQ::MassValue; }
        calc efficiencyRollup: EfficiencyRollup {in engine = anEngine;
            return efficiency : Real; }
        calc costRollup: CostRollup {in engine = anEngine;
            return cost : Real; }
        return :>> result : Real = EngineEvaluation(
            powerRollup.power, massRollup.mass,
            efficiencyRollup.efficiency, costRollup.cost                      The result of the analysis will be the
        );                                                                    alternative with either the maximum
     }
                                                                              or minimum evaluated value.
     return part :>> selectedAlternative : Engine;
 }

95                                       Last changed: 2022-07 (parameter declaration)                        Release 2026-04

### PDF PAGE 96

Verification Case Definitions (1)

                                                                 Parameterizing the requirement allows
  requirement vehicleMassRequirement {                           it to be checked against a measured
     subject vehicle : Vehicle;                                  massActual, while asserting (below) that
     in massActual :> ISQ::mass;                                 this must be equal to the vehicle.mass.
     doc     /* The vehicle mass shall be less
              * than or equal to 2500 kg. */
     require constraint {                                         A verification case definition  defines a
         massActual == vehicle.mass and                           process for verifying whether a     subject
         massActual <= 2500[SI::kg] }                             satisfies one or more requirements.
  }
  verification def VehicleMassTest {
     private import VerificationCases::*;                        The subject may be specified similarly to the

     subject testVehicle : Vehicle;                              subject of a requirement or analysis case.

     objective vehicleMassVerificationObjective {
         verify vehicleMassRequirement;                                  The requirements to be verified are declared in
     }                                                                   the verification case objective. The subject of
     return verdict : VerdictKind;                                       the verification case is automatically bound to
  }                                                                      the subject of the verified requirements.


   A verification case always returns a                  VerdictKind is an
   verdict of type VerdictKind. (The                        enumeration with
   default name is verdict, but a different            Last changed: 2020allowed values -11pass, fail,
   name can be used if desired.)                            inconclusive and error.

96                                          Last changed: 2024-12 (massActual binding)                             Release 2026-04

### PDF PAGE 97

Verification Case Definitions (2)



                                verification def VehicleMassTest {
                                   private import VerificationCases::*;

The steps of a verification case   subject testVehicle : Vehicle;
are actions that, together,        objective vehicleMassVerificationObjective {
determine the verdict.                 verify vehicleMassRequirement;
                                   }

                                   action collectData {
                                       in part testVehicle : Vehicle = VehicleMassTest::testVehicle;
                                       out massMeasured :> ISQ::mass;
                                   }
                                   action processData {
PassIf is a utility function that      in massMeasured :> ISQ::mass = collectData.massMeasured;
returns a pass or fail verdict         out massProcessed :> ISQ::mass;
                                   }
depending on whether its           action evaluateData {
argument is true or false.             in massProcessed :> ISQ::mass = processData.massProcessed;
                                       out verdict : VerdictKind =
                                          PassIf(vehicleMassRequirement(
        The use of named                    vehicle = testVehicle,                       This is a check of whether the
         argument notation                   massActual = massProcessed));                requirement is satisfied for
         here is optional.             }                                                  the given parameter values.

                                   return verdict : VerdictKind = evaluateData.verdict;
                                }

97                                         Last changed: 2024-12 (import visibility)                       Release 2026-04

### PDF PAGE 98

Verification Case Usages (1)




 This is a verification case
 usage in which the subject
 has been restricted to a
 specific test configuration.       part vehicleTestConfig : Vehicle { … }


                                    verification vehicleMassTest : VehicleMassTest {
 A verification case can be             subject testVehicle :> vehicleTestConfig;
                                    }
 performed as an action by
 a verification system.             part massVerificationSystem : MassVerificationSystem {
                                        perform vehicleMassTest;

                                        part scale : Scale {
 Parts of the verification                 perform vehicleMassTest.collectData {
 system can perform steps                     in part :>> testVehicle;
 in the overall verification                  bind measurement = testVehicle.mass;
 process.
                                              out :>> massMeasured = measurement;
                                           }                                                       In reality, this would be
                                        }                                                          some more involved
                                    }                                                              process to determine
                                                                                                   the measured mass.


98                                      Last changed: 2022 -05 (dot notation on perform)                       Release 2026-04

### PDF PAGE 99

Verification Case Usages (2)




 Individuals can be used to
 model the carrying out of        individual def TestSystem :> MassVerificationSystem;
 actual tests.                    individual def TestVehicle1 :> Vehicle;
                                  individual def TestVehicle2 :> Vehicle;

                                  individual testSystem : TestSystem :> massVerificationSystem {

                                     timeslice test1 {
  ! The keyword action is                perform action :>> vehicleMassTest {
    required here to permit                 individual :>> testVehicle : TestVehicle1 {
    the local redefinition.                    :>> mass = 2500[SI::kg];
                                            }
                                         }                                         The test on the individual
                                     }                                             TestVehicle1   should pass.

                                     then timeslice test2 {
                                         perform action :>> vehicleMassTest {
                                            individual :>> testVehicle : TestVehicle2 {
                                               :>> mass = 3000[SI::kg];
                                            }
                                         }                                         The test on the individual
                                     }                                             TestVehicle2 should fail.
                                  }



99                                         Last changed: 2021-03 (units notation)                         Release 2026-04

### PDF PAGE 100

Use Case Definition

                                                      A use case definition defines a
                                                      required interaction between its
                                                      subject and certain external actors.
An actor is a parameter of the use
case representing a role played             use case def 'Provide Transportation’ {
by entity external to the subject.             subject vehicle : Vehicle;
                                               actor driver : Person;                           !  Actors are (referential)
                                               actor passengers : Person[0..4];                    part usages and so must
The objective of the use case is               actor environment : Environment;                    have part definitions.
for the subject to provide a                   objective {
result of value to one or more                     doc  /* Transport driver and passengers from
of the actors.                                          * starting location           to ending location.
                                                        */
                                               }
                                            }

  Actors may also be specified for         use case def 'Enter Vehicle’ {
   other kinds of cases and for                subject vehicle : Vehicle;
   requirements.                               actor driver : Person;
                                               actor passengers : Person[0..4];
                                            }

                                            use case def 'Exit Vehicle’ {
                                               subject vehicle : Vehicle;
                                               actor driver : Person;
                                               actor passengers : Person[0..4];
                                            }

100                                               Last changed: 2021-08 (new)                                  Release 2026-04

### PDF PAGE 101

Use Case Usage

                                    use case 'provide transportation' : 'Provide Transportation’ {
                                       subject vehicle;
The required behavior of               first start;
a use case can be                      then include use case 'enter vehicle' : 'Enter Vehicle’ {
specified as for an action.               subject vehicle;
                                          actor :>> driver = 'provide transportation'::driver;
                                          actor :>> passengers = 'provide transportation'::passengers;
A use case can define                  }
sub-use cases within its               then use case 'drive vehicle’ {
                                          subject vehicle;
behavior.                                 actor driver = 'provide transportation'::driver;
                                          actor environment = 'provide transportation'::environment;
                                          include 'add fuel'[0..*] {                    ! A subject must be declared
A use case can  include the                   subject vehicle;                            first, before any actors. It can
performance of a use case                     actor :>> fueler = driver;                  only be omitted if there are no
defined elsewhere (similar                }                                               actors or other parameters.
to performing an action).              }
                                       then include use case 'exit vehicle' : 'Exit Vehicle’ {
                                          subject vehicle;
                                          actor :>> driver = 'provide transportation'::driver;
!  The traditional use case               actor :>> passengers = 'provide transportation'::passengers;
   “extend” relationship is            }                                    The subject of a nested use case is implicitly
   not supported yet.                  then done;
                                    }                                       bound to that of its containing use case, but
                                    use case 'add fuel’ {                   actors need to be explicitly bound.
A use case can also be                 subject vehicle : Vehicle;
specified without an                   actor fueler : Person;
explicit use case definition.          actor 'fuel station' : 'Fuel Station’;
                                    }

101                                         Last changed: 2025 -07 (added subjects)                           Release 2026-04

### PDF PAGE 102

Variation Definitions



                                       attribute def Diameter :> Real;

                                       part def Cylinder {
                                          attribute diameter : Diameter[1];
                                       }

                                       part def Engine {
                                          part cylinder : Cylinder[2..*];
                                       }
                                       part '4cylEngine' : Engine {                 A variation definition will typically
 Any kind of definition can be            part redefines cylinder[4];               specialize a definition from a design
 marked as a   variation,              }                                            model, representing the type of thing
 expressing variability within a       part '6cylEngine' : Engine {                 being varied. The variants must then
                                          part redefines cylinder[6];
 product line model.                   }                                            be valid usages of this type.

                                       // Variability model

                                       variation attribute def DiameterChoices :> Diameter {
                                          variant attribute diameterSmall = 70[mm];
                                          variant attribute diameterLarge = 100[mm];
 A variation defines one or            }
 more variant usages, which            variation part def EngineChoices :> Engine {
 represent the allowed                    variant '4cylEngine';
 choices for that variation.              variant '6cylEngine';                   Variants can also be declared by
                                       }                                          reference to usages defined elsewhere.

102                                          Last changed: 2021 -03 (units notation)                           Release 2026-04

### PDF PAGE 103

Variation Usages
                                                                                           A variation definition can be
                                                                                           used like any other definition,
                                                                                           but valid values of the usage
                                                                                           are restricted to the allowed
                                                                                           variants of the variation.
Any kind of usage can also
be a variation, defining            abstract part vehicleFamily : Vehicle {
allowable variants without a
separate variation definition.          part engine : EngineChoices[1];

                                        variation part transmission : Transmission[1] {
                                           variant manualTransmission;
                                           variant automaticTransmission;
                                        }

                                        assert constraint {
                                           (engine == engine::'4cylEngine’ and
  A constraint can be used to               transmission == transmission::manualTransmission) xor
                                           (engine == engine::'6cylEngine’ and
  model restrictions across the             transmission == transmission::automaticTransmission)
  choices that can be made.             }
                                    }         The operator     xor means "exclusive or". So, this constraint
                                                 means "choose     either a 4cylEngine and a manualTransmission,
                                                 or a 6cylEngine and an automaticTransmission".





103                                          Last changed: 2021-05 (logical operators)                           Release 2026-04

### PDF PAGE 104

Variation Configuration




        An element from a variability model
        with variation usages can be    configured                               A selection is made for a variation
        by specializing it and making selections                                 by binding one of the allowed
        for each of the variations.                                              variants to the variation usage.



                         part vehicle4Cyl :> vehicleFamily {
                             part redefines engine = engine::'4cylEngine';
                             part redefines transmission = transmission::manualTransmission;
                         }

                         part vehicle6Cyl :> vehicleFamily {
                             part redefines engine = engine::'6cylEngine';
                             part redefines transmission = transmission::manualTransmission;
                         }

                                             Choosing a   manualTransmission     with a
                                             6cylEngine is not allowed by the
                                             constraint asserted on   vehicleFamily  ,
                                             so this model of vehicle6Cyl is invalid.




104                                                  Last changed: 2020-06                                     Release 2026-04

### PDF PAGE 105

Dependencies



        package 'Dependency Example' {
            part 'System Assembly' {                              A dependency is a relationship that indicates that
               part 'Computer Subsystem' {                         one or more client elements require one more
                  …                                                supplier elements for their complete specification.
               }                                                   A dependency is entirely a model     -level
               part 'Storage Subsystem' {
                  …                                                relationship, without instance   -level semantics.
               }
            }
            package 'Software Design' {
               item def MessageSchema {
                  …                                             A dependency can be between any kinds of elements,
               }                                                generally meaning that a change to a supplier may
               item def DataSchema {                            necessitate a change to the client element.
                  …
               }
            }

            dependency from 'System Assembly'::'Computer Subsystem' to 'Software Design';

            dependency Schemata
               from 'System Assembly'::'Storage Subsystem'
               to 'Software Design'::MessageSchema, 'Software Design'::DataSchema;
        }

         A dependency can have multiple clients and/or suppliers.

105                                                 Last changed: 2020 -08                                    Release 2026-04

### PDF PAGE 106

Allocation




                                     package LogicalModel {
                                         …
                                         part torqueGenerator : TorqueGenerator {
                                            perform generateTorque;
                                         }
                                     }

                                     package PhysicalModel {                               Allocations define traceable links
                                         private import LogicalModel::*;                    across the various structures and
An allocation   specifies that           …                                                  hierarchies of a system model,
some or all of the responsibility        part powerTrain : PowerTrain {                     perhaps as a precursor to more
for realizing the intent of the             part engine : Engine {
                                                perform generateTorque;                     rigorous specifications and
source is allocated to the target.          }                                               implementations.
                                         }

                                         allocate torqueGenerator to powerTrain {
                                            allocate torqueGenerator.generateTorque
                                                    to powerTrain.engine.generateTorque;
                                         }
                                     }
                                                                                         An allocation can be refined using
                                                                                         nested allocations that give a finer   -
                                                                                         grained decomposition of the
                                                                                         containing allocation mapping.


106                                           Last changed: 2024 -07 (import visibility)                           Release 2026-04

### PDF PAGE 107

Allocation Definition




                                             package LogicalModel {
                                                 …
    !  Unlike SysML v1, an                       part def LogicalElement;
       allocation in SysML v2 is  not            part def TorqueGenerator :> LogicalElement;
       a dependency but, rather, an              part torqueGenerator : TorqueGenerator { … }
       instantiable connection               }
       across model features.
                                             package PhysicalModel {
                                                 private import LogicalModel::*;
                                                 …
                                                 part def PhysicalElement;
            An allocation definition  defines    part def PowerTrain :> PhysicalElement;
            a class of allocations between       part powerTrain : PowerTrain { … }
            features of specific types.          }

                                                 allocation def LogicalToPhysical {
                                                    end logical : LogicalElement;
                                                    end physical : PhysicalElement;
    An allocation usage  must                    }
    allocate features that conform               allocation torqueGenAlloc : LogicalToPhysical
    to the types of the ends of its                 allocate torqueGenerator to powerTrain { … }
    allocation definition.                   }



107                                         Last changed: 2024-07 (import visibility)                        Release 2026-04

### PDF PAGE 108

Metadata (1)



                                           part vehicle {
  Metadata is additional data                part interior {                               The KerML and SysML library
                                                 part alarm;                                 models include all the
   that can be used to annotate                  part seatBelt[2];                           metaclasses from the    KerML
   the elements of a model.                      part frontSeat[2];                          and SysML abstract syntax.
                                                 part driverAirBag;
                                              }
                                              part bodyAssy {
                                                 part body;                              To restrict what kind of element
                                                 part bumper;                            can be annotated, subset the
  Metadata is defined using a                    part keylessEntry;                      annotatedElement feature with
  metadata definition  .                      }                                          the desired element type(s).
                                           }

                                           metadata def SafetyFeature;
                                           metadata def SecurityFeature {
                                              :> annotatedElement : SysML::PartDefinition;
                                              :> annotatedElement : SysML::PartUsage;
                                           }
                                           metadata SafetyFeature about
                                              vehicle::interior::seatBelt,                      At its simplest, a metadata
                                              vehicle::interior::driverAirBag,                   annotation can be used to
A specific type of metadata can               vehicle::bodyAssy::bumper;                         simply "tag" certain
then be applied as an annotation           metadata SecurityFeature about                        elements, so that they can,
to one or more model elements.                vehicle::interior::alarm,                          e.g., be grouped by tooling.
                                              vehicle::bodyAssy::keylessEntry;

108                              Last changed: 2022-03 (metadata definition, annotatedElement)                  Release 2026-04

### PDF PAGE 109

Metadata (2)



                          standard library package AnalysisTooling {
                             private import ScalarValues::*;
                             metadata def ToolExecution {                          The AnalysisTooling
                                 attribute toolName : String;
                                 attribute uri : String;                            package is part of the
                             }                                                      Analysis domain library.
                             metadata def ToolVariable {
                                 attribute name : String;
                             }
                          }                                        If the metadata definition has nested
                          action computeDynamics {                 features, these must be bound to
                             private import AnalysisToolingvalues  in the metadata annotation.::*;

                             metadata ToolExecution {
                                 toolName = "ModelCenter";                                    The @ symbol is equivalent
                                 uri = "aserv://localhost/Vehicle/Equation1";                 to the metadata keyword.
A metadata annotation        }
contained in the body of     in dt : ISQ::TimeValue  {@ToolVariable {name = "deltaT";}}
a namespace (package,        in a : ISQ:: AccelerationValue             {@ToolVariable {name = "mass";}}
definition or usage)  is,    in v_in : ISQ:: VelocityValue              {@ToolVariable {name = "v0";}}
by default, about that       in x_in : ISQ:: LengthValue {@ToolVariable {name = "x0";}}
namespace.                   out v_out : ISQ:: VelocityValue {@ToolVariable {name = "v";}}
                             out x_out : ISQ:: LengthValue              {@ToolVariable {name = "x";}}
                          }

109                                        Last changed: 2024-07 (import visibility)                       Release 2026-04

### PDF PAGE 110

Element Import Filtering (1)




metadata def Safety {                                                                A recursive import (using **)
   attribute isMandatory : Boolean;                                                  imports members of a namespace
}                                                                                    and, recursively, members of any
                                  ! Currently, a metadata annotation must
part vehicle {                      be owned by the annotated element to             nested namespaces.
   part interior {                  be accessed in a filter condition.
      part alarm;
      part seatBelt[2] {                                       package 'Safety Features' {
         @Safety{isMandatory = true;}}                             public import vehicle::**;
      part frontSeat[2];                                           filter @Safety;
      part driverAirBag {                                      }
         @Safety{isMandatory = false;}}
   }                                                           package 'Mandatory Safety Features' {
   part bodyAssy {                                                 public import vehicle::**;
      part body;                                                   filter @Safety and (as Safety).isMandatory;
      part bumper {                                            }
         @Safety{isMandatory = true;}}
      part keylessEntry;
   }
   part wheelAssy {                                       A filter is a Boolean               @ checks life an element
      part wheel[2];                                      condition that must be true
      part antilockBrakes[2] {                                                                has the given metadata
         @Safety{isMandatory = false;}}                   for an element to actually          and as ”casts” to that
   }                                                      be imported into a package.         metadata type.
}


110                                        Last changed: 2026-03 (filter expression)                       Release 2026-04

### PDF PAGE 111

Element Import Filtering (2)

                                                                   The filter keyword is only allowed in a
metadata def Safety {                                               package (or view), but a filtered import can
   attribute isMandatory : Boolean;                                 be used anyplace an import is allowed.
}
part vehicle {                                                   Filter conditions can also be
   part interior {                                               combined with the import itself.
      part alarm;
      part seatBelt[2] {                                        package 'Safety Features' {
          @Safety{isMandatory = true;}}                             public import vehicle::**[@Safety];
      part frontSeat[2];                                        }
      part driverAirBag {
          @Safety{isMandatory = false;}}                        package 'Mandatory Safety Features' {
   }                                                                public import vehicle::**
   part bodyAssy {                                                     [@Safety and (as Safety).isMandatory];
      part body;                                                }
      part bumper {
          @Safety{isMandatory = true;}}
      part keylessEntry;
   }                                                              !  A filter condition expression must be model    -
   part wheelAssy {
      part wheel[2];                                                 level evaluable. It can reference only literals
      part antilockBrakes[2] {                                       and metadata annotations and attributes,
          @Safety{isMandatory = false;}}                             connected using basic arithmetic,
   }                                                                 comparison and Boolean operators.
}


111                                         Last changed: 2026-03 (filter expression)                        Release 2026-04

### PDF PAGE 112

Language Extension (1)
                                                         For a domain  -specific extension to SysML, first
                                                         create a library model of domain   -specific concepts.
library package FailureModeling {                        This can be explicitly identified as a library package.
   abstract occurrence def Situation;
   abstract occurrence situations : Situation[*] nonunique;

   abstract occurrence def Cause {
       attribute probability : Real;
   }
   abstract occurrence causes : Cause[*] nonunique :> situations;
   abstract occurrence def Failure {                                                For each concept, provide a base
       attribute severity : Level;                                                  definition and a base usage
   }                                                                                modeling the concept semantics.
   abstract occurrence failures : Failure[*] nonunique :> situations;

   abstract connection def Causation :> Occurrences::HappensBefore {
       end cause : Situation[*];
       end effect : Situation[*];
   }
   abstract connection causations : Causation[*] nonunique;                         HappensBefore     is the base type
   item def Scenario {                                                              for successions, from the Kernel
       occurrence :>> situations;                                                   Library Occurrences    package.
       occurrence :>> causes :> situations;
       occurrence :>> failures :> situations;
   }
   item scenarios : Scenario[*] nonunique;
}

112                                         Last changed: 2022-09 (library package)                       Release 2026-04

### PDF PAGE 113

Language Extension (2)


       library package FailureModelingMetadata {
          private import FailureModeling::*;                               Declare semantic metadata for
          private import Metaobjects::SemanticMetadata;                    each concept to be included in
                                                                           the language extension.
          metadata def situation :> SemanticMetadata {
             :>> baseType = situations meta SysML::Usage;
          }

          metadata def cause :> SemanticMetadata {                         Bind baseType to the base usage
             :>> baseType = causes meta SysML::Usage;
          }                                                                for the relevant concept.

          metadata def failure :> SemanticMetadata {
             :>> baseType = failures meta SysML::Usage;
          }
                                                                         The meta-cast "meta
          metadata def causation :> SemanticMetadata {                   SysML::Usage" allows failures to
             :>> baseType = causations meta SysML::Usage;be referenced as a usage, rather
          }                                                              than evaluated as an expression.

          metadata def scenario :> SemanticMetadata {
             :>> baseType = scenarios meta SysML::Usage;
          }
       }
113                                    Last changed: 2024-07 (import visibility)              Release 2026-04

### PDF PAGE 114

Language Extension (3)



                                     private import FailureModelingMetadata::*;

                                     #scenario def DeviceFailure {
                                         ref device : Device;                         Implicitly specializes the
                                         attribute minPower : Real;                   library definition Scenario
 A user-defined keyword, starting        #cause 'battery old' {                       (the definition of the
 with # and referencing a semantic          :>> probability = 0.01;                   scenarios base type).
 metadata definition, can be used        }
 to declare a definition or usage.
                                         #causation connect 'battery old’ to 'power low';

 Implicitly specializes the              #situation 'power low' {
 library usage situations                   constraint { device.battery.power < minPower }
 (as given in the semantic               }
 metadata situation).                    #causation connect 'power low’ to 'device shutoff';


                                         #failure 'device shutoff' {
 Inheritance and                            :>> severity = LevelEnum::high;
 redefinition work as for                }
 explicit specialization.            }


114                              Last changed: 2025-07 (changed successions to connections)          Release 2026-04

### PDF PAGE 115

Stakeholders and Concerns



     part def 'Systems Engineer';                A concern is a specific topic that one or more
     part def 'IV&V’;                            stakeholders desire to be addressed.

     concern 'system breakdown' {
        doc /*
         * To ensure that a system covers all its required capabilities,
         * it is necessary to understand how it is broken down into
         * subsystems and components that provide those capabilities.
         */                                                   A subject must be declared first, before any
        subject system;                                     ! stakeholders. It can only be omitted if there
        stakeholder se: 'systems engineer';                   are no stakeholders or other parameters.
        stakeholder ivv: 'IV&V';
     }
     concern modularity {                   A stakeholder is a person, organization or
        doc /*                              other entity with concerns to be addressed.

         * There should be well defined interfaces between the parts of
         * a system that allow each part to be understood individually,
         * as well as being part of the whole system.
         */
        subject system;                                     Stakeholders may be specified for any
        stakeholder 'systems engineer';                      kind of requirement, not just concerns.
     }

115                                     Last changed: 2025-07 (added subjects)                 Release 2026-04

### PDF PAGE 116

Viewpoints



                             A viewpoint is a requirement to present
                             information from a model in a  view that
                             addresses certain stakeholder concerns.


            viewpoint 'system structure perspective' {
               frame 'system breakdown';
               frame modularity;                            A viewpoint frames the concerns that will be

               require constraint {                         addressed by a view that satisfies the viewpoint.
                   doc /*
                    * A system structure view shall show the hierarchical
                    * part decomposition of a system, starting with a
                    * specified root part.
                    */
               }
            }


                                        Any requirement may be modeled
                                          as framing relevant stakeholder
                                          concerns, not just viewpoints.


116                                            Last changed: 2021-05 (new)                            Release 2026-04

### PDF PAGE 117

Views (1)


                                                                                                 A view definition specifies how
                                                                                                 information can be extracted
                                                                                                 from a model in order to satisfy
A view definition can           view def 'Part Structure View' {                                 one or more viewpoints.
filter the elements to              satisfy 'system structure perspective’;
be included in the
views it specifies.                 filter @SysML::PartUsage;                            The SysML library package models
                                }                                                        the SysML abstract syntax, which
                                                                                         can be used to filter on specific
                                view 'vehicle structure view' :                          kinds of model elements.
                                    'Part Structure View' {
A view usage specifies a            expose vehicle::**;                          A view usage exposes the model elements
certain view conforming                                                          to be included in the view, which are
to a view definition.               render asTreeDiagram;                        filtered as specified in the view definition.
                                }

    The view rendering can also be given                        A view usage specifies how the view is
     in the view definition, in which case it                    to be rendered as a physical artifact.
     will be the same for all usages of that
     definition. But only view usages can
     expose elements to be viewed.


117                                                   Last changed: 2021-05 (new)                                   Release 2026-04

### PDF PAGE 118

Views (2)

                                                                        The Views library package includes four
 Specialized kinds of renderings                                         basic kinds of rendering: asTreeDiagram,
 can be defined in a user model.                                         asInterconnectionDiagram,
                                                                         asTextualNotation and asElementTable.

                   rendering asTextualNotationTable :> asElementTable {
                      view :>> columnView[1] {
                         render asTextualNotation;                        ! A more comprehensive
                      }                                                     rendering library model is
                   }                                                        planned for future release.

                   view 'vehicle tabular views’ {
                         view 'safety features view' : 'Part Structure View’ {
 Views can have             expose vehicle::**[@Safety];
 subviews.                  render asElementTable;
                         }

                         view 'non-safety features view' : 'Part Structure View’ {
                            expose vehicle::**[not (@Safety)];
                            render asElementTable;
                         }                                                    Views can specify additional filtering
                   }                                                          conditions on an expose, using the

                                                                              same notation as for an import.

118                                      Last changed: 2021-09 (editorial correction)                 Release 2026-04

### PDF PAGE 119

Example View Rendering





                        view ‘vehicle structure view’ {
                          expose vehicle::**[@SysML::PartUsage];
                          render asTreeDiagram;
                        }

























119                                   Last changed: 2021-05 (new)                     Release 2026-04

### PDF PAGE 120

Kernel Data Type Library




















120                                                                   Release 2026-04

### PDF PAGE 121

Scalar Values






            standard library package ScalarValues {
               private import Base::*;

               abstract datatype ScalarValue specializes Value;
               datatype Boolean specializes ScalarValue;
               datatype String specializes ScalarValue;
               abstract datatype NumericalValue specializes ScalarValue;

               abstract datatype Number specializes NumericalValue;
               datatype Complex specializes Number;
               datatype Real specializes Complex;
               datatype Rational specializes Real;
               datatype Integer specializes Rational;
               datatype Natural specializes Integer;
               datatype Positive specializes Natural;
            }






121                            Last changed: 2022-09 (standard library package)        Release 2026-04

### PDF PAGE 122

Collections (1)



             standard library package Collections {
                …
                abstract datatype Collection {
                   feature elements[0..*] nonunique;
                }
                abstract datatype OrderedCollection :> Collection {
                   feature :>> elements[0..*] ordered nonunique;
                }
                abstract datatype UniqueCollection :> Collection {
                   feature :>> elements[0..*];
                }

                datatype Array :> OrderedCollection {
                   feature dimensions: Positive[0..*] ordered nonunique;
                   feature rank: Natural[1] = size(dimensions);
                   feature flattenedSize: Positive[1] = dimensions->reduce '*' ?? 1;
                   inv { flattenedSize == size(elements) }
                }

                datatype Bag :> Collection;
                datatype Set :> UniqueCollection;
                datatype OrderedSet :> OrderedCollection, UniqueCollection {
                   feature :>> elements[0..*] ordered;
                }
                datatype List :> OrderedCollection;
                …
             }

122                                 Last changed: 2022-09 (standard library package)                Release 2026-04

### PDF PAGE 123

Collections (2)








             standard library package Collections {
                …

                datatype KeyValuePair {
                   feature key: Anything[0..*] ordered nonunique;
                   feature val: Anything[0..*] ordered nonunique;
                }

                datatype Map :> Collection {
                   feature :>> elements: KeyValuePair[0..*];
                }

                datatype OrderedMap :> Map {
                   feature :>> elements: KeyValuePair[0..*] ordered;
                }

             }








123                                  Last changed: 2022-09 (standard library package)                Release 2026-04

### PDF PAGE 124

Vector Values



standard library package VectorValues {
  private import ScalarValues::NumericalValue;
  private import ScalarValues::Real;
  private import Collections::Array;

  abstract datatype VectorValue;

  datatype NumericalVectorValue :> VectorValue, Array {
     feature dimension[0..1] :>> dimensions;
     feature :>> elements : NumericalValue;
  }

  datatype CartesianVectorValue :> NumericalVectorValue {
     feature :>> elements : Real;
  }

  datatype ThreeVectorValue :> NumericalVectorValue {
     feature :>> dimension = 3;
  }

  datatype CartesianThreeVectorValue :> CartesianVectorValue, ThreeVectorValue;
}


 124                            Last changed: 2022-09 (standard library package)      Release 2026-04

### PDF PAGE 125

Kernel Function Library
                       (selected models)



















125                                                             Release 2026-04

### PDF PAGE 126

Base Functions



standard library package BaseFunctions {
   private import Base::Anything;
   private import ScalarValues::*;

   abstract function '==' { in x: Anything[0..1];               in y: Anything[0..1];
       return : Boolean[1];
   }
   function    '!=' {   in x: Anything[0..1];       in y: Anything[0..1];
       return : Boolean[1] =        not (x == y)
   }
   abstract function      '===' {    in x: Anything[0..1];       in y: Anything[0..1];
       return : Boolean[1];
   }
   function    '!==' {   in x: Anything[0..1];        in y: Anything[0..1];
       return : Boolean[1] =        not (x === y)
   }

   function    ToString   { in Anything[0..1];
       return   : String[1];
   }

   abstract    function   '['{ in x: Anything[0..*]         nonunique   ; in y: Anything[0..*]        nonunique  ;
       return   : Anything[0..*]      nonunique   ;
   }
   abstract    function   '#'{   in seq: Anything[0..*]        ordered   nonunique   ; in index: Positive[1..*]         ordered   nonunique   ;
       return   : Anything[0..1];
   }
   abstract    function   ','{
       in seq1: Anything[0..*]        ordered   nonunique   ; seq2: Anything[0..*]        ordered   nonunique   ;
       return   : Anything[0..*]      ordered   nonunique   ;
   }
   …
}
 126                                                Last changed: 2023  -02 (added '[', '#', ',')                            Release 2026-04

### PDF PAGE 127

Data Functions

standard library package DataFunctions {                                     ScalarFunctions   package is similar
  …                                                                            but specialized for ScalarValue.
  abstract function '=='specializes BaseFunctions::'=='
      {in x: DataValue[0..1]; in y: DataValue[0..1]; return : Boolean[1];}
  function '==='specializes BaseFunctions::'==='
      {in x: DataValue[0..1]; in y: DataValue[0..1]; return : Boolean[1];}

  abstract function '+'{in x: DataValue[1]; in y: DataValue[0..1]; return : DataValue[1];}
  abstract function '-'{in x: DataValue[1]; in y: DataValue[0..1]; return : DataValue[1];}
  abstract function '*'{in x: DataValue[1]; in y: DataValue[1]; return : DataValue[1];}
  abstract function '/'{in x: DataValue[1]; in y: DataValue[1]; return : DataValue[1];}
  abstract function '**'{in x: DataValue[1]; in y: DataValue[1]; return : DataValue[1];}
  abstract function '^'{in x: DataValue[1]; in y: DataValue[1]; return : DataValue[1];}
  abstract function '%'{in x: DataValue[1]; in y: DataValue[1]; return : DataValue[1];}
  abstract function 'not'{in x: DataValue[1]; return : DataValue[1];}
  abstract function 'xor'{in x: DataValue[1]; in y: DataValue[1]; return : DataValue[1];}
  abstract function '~'{in x: DataValue[1]; return : DataValue[1];}
  abstract function '|'{in x: DataValue[1]; in y: DataValue[1]; return : DataValue[1];}
  abstract function '&'{in x: DataValue[1]; in y: DataValue[1]; return : DataValue[1];}
  abstract function '<'{in x: DataValue[1]; in y: DataValue[1]; return : Boolean[1];}
  abstract function '>'{in x: DataValue[1]; in y: DataValue[1]; return : Boolean[1];}
  abstract function '<='{in x: DataValue[1]; in y: DataValue[1]; return : Boolean[1];}
  abstract function '>='{in x: DataValue[1]; in y: DataValue[1]; return : Boolean[1];}
  abstract function max{in x: DataValue[1]; return : DataValue[1];}
  abstract function min{in x: DataValue[1]; return : DataValue[1];}
  abstract function '..'
      {in lower:DataValue[1]; in upper:DataValue[1]; return : DataValue[0..*] ordered;
  }
}
 127                              Last changed: 2022-09 (standard library package, "===")            Release 2026-04

### PDF PAGE 128

Boolean Functions




standard library package BooleanFunctions {
  public import ScalarValues::*;

  function 'not' specializes ScalarFunctions::'not’
     {in x: Boolean; return : Boolean;}
  function 'xor' specializes ScalarFunctions::’xor’
     {in x: Boolean; in y: Boolean; return : Boolean;}

  function '|' specializes ScalarFunctions::'|’
     {in x: Boolean; in y: Boolean; return : Boolean;}
  function '&' specializes ScalarFunctions::'&’
     {in x: Boolean; in y: Boolean; return : Boolean;}

  function '==' specializes BaseFunctions::'==‘
     {in x: Boolean; in y: Boolean; return : Boolean;}

  function ToString specializes BaseFunctions::ToString
     {in x: Boolean; return : String;}
  function ToBoolean(x: String): Boolean;
     {in x: String; return : Boolean;}
}


 128                               Last changed: 2024-07 (import visibility)         Release 2026-04

### PDF PAGE 129

String Functions


standard library package StringFunctions {
  public import ScalarValues::*;

  function '+' specializes ScalarFunctions::’+’
     {in x: String; in y: String; return : String;}

  function Size {in x: String; return : Natural;}
  function Substring
     {in x: String; in lower: Integer; in upper: Integer; return : String;}

  function '<' specializes ScalarFunctions::'<‘
     {in x: String; in y: String; return : Boolean;}
  function '>' specializes ScalarFunctions::’>’
     {in x: String; in y: String; return : Boolean;}
  function '<=' specializes ScalarFunctions::'<='
     {in x: String; in y: String; return : Boolean;}
  function '>=' specializes ScalarFunctions::'>='
     {in x: String; in y: String; return : Boolean;}
  function '=' specializes BaseFunctions::'=='
     {in x: String; in y: String; return : Boolean;}

  function ToString specializes BaseFunctions::ToString
     {in x: String; return : String;
}
129                               Last changed: 2024-07 (import visibility)          Release 2026-04

### PDF PAGE 130

Numerical Functions




standard library package NumericalFunctions {
  public import ScalarValues::*;
  function abs {in x: NumericalValue[1]; return : NumericalValue                   [1];}
  abstract    function    ‘+’ specializes     ScalarFunctions     ::‘+’
       {in x: NumericalValue       [1];  in y: NumericalValue      [0..1];   return   : NumericalValue     [1];}
  abstract    function    '-' specializes     ScalarFunctions     ::‘-’
       {in x: NumericalValue       [1];  in y: NumericalValue      [0..1];   return   : NumericalValue     [1];}
  abstract    function    '*' specializes     ScalarFunctions     ::‘*’
       {in x: NumericalValue       [1];  in y: NumericalValue      [1];  return   : NumericalValue     [1];}
  abstract    function    '/' specializes     ScalarFunctions     ::‘/’
       {in x: NumericalValue       [1];  in y: NumericalValue      [0..1];   return   : NumericalValue     [1];}
  abstract    function    '**' specializes      ScalarFunctions    ::‘**’
       {in x: NumericalValue       [1];  in y: NumericalValue      [0..1];   return   : NumericalValue     [1];}
  abstract    function    '^' specializes     ScalarFunctions     ::‘^’
       {in x: NumericalValue       [1];  in y: NumericalValue      [0..1];   return   : NumericalValue     [1];}
  abstract    function    '%' specializes     ScalarFunctions     ::‘%’
       {in x: NumericalValue       [1];  in y: NumericalValue      [0..1];   return   : NumericalValue     [1];}
  abstract    function    '<‘specializes     ScalarFunctions     ::‘<’
       {in x: NumericalValue       [1];  in y: NumericalValue      [0..1];   return   : Boolean[1];}
  abstract    function    ‘>’ specializes     ScalarFunctions     ::‘>’
       {in x: NumericalValue       [1];  in y: NumericalValue      [0..1];   return   : Boolean[1];}
  abstract    function    '<=' specializes      ScalarFunctions    ::‘<=’
       {in x: NumericalValue       [1];  in y: NumericalValue      [0..1];   return   : Boolean[1];}
  abstract    function    '>=' specializes      ScalarFunctions    ::‘>=’
       {in x: NumericalValue       [1];  in y: NumericalValue      [0..1];   return   : Boolean[1];}
  abstract    function    max specializes     ScalarFunctions     ::max
       {in x: NumericalValue       [1];  in y: NumericalValue      [0..1];   return   : NumericalValue     [1];}
  abstract    function    min specializes     ScalarFunctions     ::min
       {in x: NumericalValue       [1];  in y: NumericalValue      [0..1];   return   : NumericalValue     [1];}

  abstract    function    sum {in collection:       NumericalValue    [0..*]   ordered; return      : NumericalValue     [1];}
  abstract    function    product {   in collection:     NumericalValue    [0..*]   ordered; return      : NumericalValue     [1];}
}
  130                                               Last changed: 2024   -07 (import visibility)                               Release 2026-04

### PDF PAGE 131

Complex Functions



standard library package ComplexFunctions {
    public import ScalarValues::*;

    feature i: Complex[1] = rect(0.0, 1.0);

    function rect{in re: Real[1];         in im: Real[1];      return : Complex[1];}
    function   polar{in abs: Real[1];        in arg: Real[1];      return   : Complex[1];}
    function   re{in x: Complex[1];       return   : Real[1];}
    function   im {in x: Complex[1];       return    : Real[1];}

    function   abs specializes      NumericalFunctions     ::abs {  in x: Complex[1];      return    : Real[1];}
    function   {in x: Complex[1];      return    : Real[1];}
    function   '+' specializes      NumericalFunctions     ::'+’
       {in x: Complex[1];       in y: Complex[0..1];       return   : Complex[1];
    function   '-' specializes      NumericalFunctions     ::'-'
       {in x: Complex[1];       in y: Complex[0..1];       return   : Complex[1];
    function   '*' specializes      NumericalFunctions     ::'*'
       {in x: Complex[1];       in y: Complex[1];      return   : Complex[1];
    function   '/' specializes      NumericalFunctions     ::'/'
       {in x: Complex[1];       in y: Complex[1];      return   : Complex[1];
    function   '**' specializes      NumericalFunctions     ::'**'
       {in x: Complex[1];       in y: Complex[1];      return   : Complex[1];
    function   '^' specializes      NumericalFunctions     ::'^'
       {in x: Complex[1];       in y: Complex[1];      return   : Complex[1];
    function   '==' specializes      DataFunctions    ::'=='
       {in x: Complex[1];       in y: Complex[1];      return   : Complex[1];

    function   ToString    specializes    BaseFunctions    ::ToString    {in x: Complex[1];       return   : String[1];}
    function   ToComplex    {in x: String[1];      return   : Complex[1];}

    function   sum specializes      NumericalFunctions     ::sum {  in collection: Complex[0..*];          return   : Complex[1];}
    function   product    specializes    NumericalFunctions     ::product {    in collection: Complex[0..*];         return    : Complex[1];}
}
 131                                               Last changed: 2024   -07 (import visibility)                               Release 2026-04

### PDF PAGE 132

Real Functions



standard library package RealFunctions {
   public import ScalarValues::*;
   function abs specializes ComplexFunctions::abs {in x: Real[1];                     return   : Real[1];}
   function    '+' specializes      ComplexFunctions     ::'+’ {  in x: Real[1];      in y: Real[0..1];      return: Real[1];}
   function    '-' specializes      ComplexFunctions     ::'-' {in x: Real[1];        in y: Real[0..1];      return: Real[1];}
   function    '*' specializes      ComplexFunctions     ::'*' {  in x: Real[1];      in y: Real[1];     return: Real[1];}
   function    '/' specializes      ComplexFunctions     ::'/' {  in x: Real[1];      in y: Real[0..1];      return: Real[1];}
   function    '**'   specializes    ComplexFunctions     ::'**' {   in x: Real[1];     in y: Real[0..1];       return: Real[1];}
   function    '^' specializes      ComplexFunctions     ::'^' {  in x: Real[1];      in y: Real[0..1];      return: Real[1];}
   function    '<' specializes      ComplexFunctions     ::'<'
       {in x: Real[1];      in y: Real[0..1];       return: Boolean[1];}
   function    '>' specializes      ComplexFunctions     ::'>'
       {in x: Real[1];      in y: Real[0..1];       return: Boolean[1];}
   function    '<='   specializes    ComplexFunctions     ::'<='
       {in x: Real[1];      in y: Real[0..1];       return: Boolean[1];}
   function    '>='   specializes    ComplexFunctions     ::'>='
       {in x: Real[1];      in y: Real[0..1];       return: Boolean[1];}
   function    max specializes      ComplexFunctions     ::max {  in x: Real[1];      in y: Real[0..1];      return: Real[1];}
   function    min specializes      ComplexFunctions     ::min {  in x: Real[1];      in y: Real[0..1];      return: Real[1];}
   function    '=='   specializes    ComplexFunctions     ::'==‘
       {in x: Real[1];      in y: Real[0..1];       return: Boolean[1];}
   function    sqrt {  in x: Real[1];      return   : Real[1];}
   function    floor {  in x: Real[1];      return   : Integer[1];}
   function    round {  in x: Real[1];      return   : Integer[1];}

   function    ToString    specializes    ComplexFunctions     ::ToString    {in x: Real[1];       return   : String[1];}
   function    ToInteger    {in x: Real[1];      return   : Integer[1];}
   function    ToRational    {in x: Real[1];      return   : Rational[1];}
   function    ToReal   {in x: String[1];       return   : Real[1];}
   function    ToComplex   (x: Real[1]): Complex;
   function    sum specializes      ComplexFunctions     ::sum {in collection: Real[0..*];           return   : Real[1];}
   function    product    specializes    ComplexFunctions     ::product {in collection: Real[0..*];             return   : Real[1];}
}
  132                                               Last changed: 2024   -07 (import visibility)                               Release 2026-04

### PDF PAGE 133

Rational Functions



standard library package RationalFunctions {
   public import ScalarValues::*;

   function rat {in numer       : Integer[1];     in denum   : Integer[1];     return   : Rational[1];}
   function    numer  {in rat: Rational[1];       return   : Integer[1];}
   function    denom   {in rat: Rational[1];        return   : Integer[1];}

   function    abs specializes      RealFunctions    ::abs {  in x: Rational[1];       return   : Rational[1];}
   function    '+' specializes      RealFunctions    ::’+’ {  in x: Rational[1];       in y: Rational[0..1];       return    : Rational[1];}
   function    '-' specializes      RealFunctions    ::'-' {in x: Rational[1];         in y: Rational[0..1];       return    : Rational[1];}
   function    '*' specializes      RealFunctions    ::'*' {  in x: Rational[1];       in y: Rational[1];       return   : Rational[1];}
   function    '/' specializes      RealFunctions    ::'/' {  in x: Rational[1];       in y: Rational[1];       return   : Rational[1];}
   function    '**'   specializes    RealFunctions    ::'**' {   in x: Rational[1];      in y: Rational[1];       return   : Rational[1];}
   function    '^' specializes      RealFunctions    ::'^' {  in x: Rational[1];       in y: Rational[1];       return   : Rational[1];}
   function    '<' specializes      RealFunctions    ::'<‘ {  in x: Rational[1];       in y: Rational[1];       return   : Boolean[1];
   function    '>' specializes      RealFunctions    ::'>' {  in x: Rational[1];       in y: Rational[1];       return   : Boolean[1];
   function    '<='   specializes    RealFunctions    ::'<=' {   in x: Rational[1];      in y: Rational[1];       return   : Boolean[1];
   function    '>='   specializes    RealFunctions    ::'>=' {   in x: Rational[1];      in y: Rational[1];       return   : Boolean[1];
   function    max specializes      RealFunctions    ::max {  in x: Rational[1];       in y: Rational[1];       return   : Boolean[1];
   function    min specializes      RealFunctions    ::min {  in x: Rational[1];       in y: Rational[1];       return   : Boolean[1];
   function    '=='   specializes    RealFunctions    ::'==' {   in x: Rational[1];      in y: Rational[1];       return   : Boolean[1];

   function    gcd {in x: Rational[1];        in y: Rational[0..1];        return   : Integer[1];}
   function    floor {  in x: Rational[1];       return   : Integer[1];}
   function    round {  in x: Rational[1];       return   : Integer[1];}

   function    ToString    specializes    RealFunctions    ::ToString    {in x: Rational[1];        return : String[1];}
   function    ToInteger    {in x: Rational[1];       return : Integer[1];}
   function    ToRational    {in x: String[1];       return : Rational[1];}

   function    sum specializes      RealFunctions    ::sum {  in collection: Rational[0..*];          return    : Rational[1];}
   function    product    specializes    RealFunctions    ::product {   in collection: Rational[0..*];           return   : Rational[1];}
}
 133                                                Last changed: 2024   -07 (import visibility)                               Release 2026-04

### PDF PAGE 134

Integer Functions





standard library package IntegerFunctions {
   public import ScalarValues::*;

   function abs specializes RationalFunctions::abs {in x: Integer[1];                      return : Natural[1];}
   function    '+' specializes      RationalFunctions     ::'+' {  in x: Integer[1];       in y: Integer[0..1];       return : Integer[1];}
   function    '-' specializes      RationalFunctions     ::'-' {in x: Integer[1];         in y: Integer[0..1];       return : Integer[1];}
   function    '*' specializes      RationalFunctions     ::'*' {  in x: Integer[1];       in y: Integer[1];      return : Integer[1];}
   function    '/' specializes      RationalFunctions     ::'/' {  in x: Integer[1];       in y: Integer[1];      return : Rational[1];}
   function    '**'   specializes    RationalFunctions     ::'**' {   in x: Integer[1];      in y: Natural[1];       return : Integer[1];}
   function    '^' specializes      RationalFunctions     ::'^' {  in x: Integer[1];       in y: Natural[1];      return : Integer[1];}
   function    '%' specializes      NumericalFunctions     ::'%' {   in x: Integer[1];      in y: Integer[1];      return : Integer[1];}
   function    '<' specializes      RationalFunctions     ::'<' {  in x: Integer[1];       in y: Integer[1];      return : Boolean[1];}
   function    '>' specializes      RationalFunctions     ::'>' {  in x: Integer[1];       in y: Integer[1];      return : Boolean[1];}
   function    '<='   specializes    RationalFunctions     ::'<=' {   in x: Integer[1];      in y: Integer[1];       return : Boolean[1];}
   function    '>='   specializes    RationalFunctions     ::'>=' {   in x: Integer[1];      in y: Integer[1];       return : Boolean[1];}

   function    max specializes      RationalFunctions     ::max {  in x: Integer[1];       in y: Integer[1];      return : Integer[1];}
   function    min specializes      RationalFunctions     ::min {  in x: Integer[1];       in y: Integer[1];      return : Integer[1];}


   function    '=='   specializes    DataFunctions    ::'==' {   in x: Integer[0..1];       in y: Integer[0..1];       return : Boolean[1];}
   function    '..'   specializes    ScalarFunctions     ::'..’
       {in lower: Integer[1];        in upper: Integer[1];        return : Integer[0..*];}
   function    ToString    specializes    RationalFunctions      ::ToString    {in x: Integer[1];       return : String[1];}
   function    ToNatural    {in x: Integer[1];       return : Natural[1];}
   function    ToInteger    {in x: String[1];       return : Integer[1];}
   function    sum specializes      RationalFunctions     ::sum {  in collection: Integer[0..*];          return : Integer[1];}
   function    product    specializes    RationalFunctions     ::product {    in collection: Integer[0..*];          return : Integer[1];}
}



 134                                               Last changed: 2024   -07 (import visibility)                               Release 2026-04

### PDF PAGE 135

Natural Functions









standard library package NaturalFunctions {
   public import ScalarValues::*;

   function '+' specializes IntegerFunctions::'+' {in x: Natural[1];                     in y: Natural[0..1];       return : Natural[1];}
   function    '*' specializes      IntegerFunctions    ::'*' {   in x: Natural[1];      in y: Natural[1];      return : Natural[1];}
   function    '/' specializes      IntegerFunctions    ::'/' {   in x: Natural[1];      in y: Natural[1];      return : Natural[1];}
   function    '%' specializes      IntegerFunctions    ::'%' {   in x: Natural[1];      in y: Natural[1];      return : Natural[1];}
   function    '<' specializes      IntegerFunctions    ::'<' {   in x: Natural[1];      in y: Natural[1];      return : Boolean[1];}
   function    '>' specializes      IntegerFunctions    ::'>' {   in x: Natural[1];      in y: Natural[1];      return : Boolean[1];}
   function    '<='   specializes    IntegerFunctions     ::'<=' {  in x: Natural[1];      in y: Natural[1];       return : Boolean[1];}
   function    '>='   specializes    IntegerFunctions     ::'>=' {  in x: Natural[1];      in y: Natural[1];       return : Boolean[1];}


   function    max specializes      IntegerFunctions    ::max {   in x: Natural[1];      in y: Natural[1];      return : Natural[1];}
   function    min specializes      IntegerFunctions    ::min {    n x: Natural[1];      in y: Natural[1];      return : Natural[1];}


   function    '=='   specializes    IntegerFunctions     ::'==‘
       {in x: Natural[0..1];        in y: Natural[0..1];       return : Boolean[1];}
   function    ToString   specializes     IntegerFunctions     ::ToString    {in x: Natural[1];       return : String[1];}
   function    ToNatural   {in x: String[1];      return : Natural[1];}
}






 135                                               Last changed: 2024   -07 (import visibility)                               Release 2026-04

### PDF PAGE 136

Trigonometric Functions



       standard library package TrigFunctions {
          public import ScalarValues::Real;

          feature pi : Real;
          inv piPrecision {
            RealFunctions::round(pi * 1E20) == 314159265358979323846.0
          }

          function deg {in theta_rad : Real[1];return : Real[1];}
          function rad {in theta_deg : Real; return : Real[1];}

          datatype UnitBoundedReal :> Real {
            inv unitBound { -1.0 <= that & that <= 1.0 }
          }
          function sin {in theta : Real[1]; return : UnitBoundedReal[1];}
          function cos {in theta : Real[1]; return : UnitBoundedReal[1];}
          function tan {in theta : Real[1]; return : Real;}
          function cot {in theta : Real; return : Real;}
          function arcsin {in x : UnitBoundedReal[1]; return : Real[1];}
          function arccos {in x : UnitBoundedReal[1]; return : Real[1];}
          function arctan {in x : Real[1]; return : Real[1];}
       }


136                               Last changed: 2024-07 (import visibility)         Release 2026-04

### PDF PAGE 137

Sequence Functions (1)




standard library package SequenceFunctions {
    …
    function equals {in x: Anything[0..*]            ordered nonunique     ; in y: Anything[0..*]        ordered nonunique     ;
       return : Boolean[1];
    }
    function   same {  in x: Anything[0..*]       ordered nonunique     ; in y: Anything[0..*]        ordered nonunique     ;
       return : Boolean[1];
    }

    function   size {  in seq: Anything[0..*]        nonunique  ; return : Natural[1];}
    function   isEmpty   {in seq: Anything[0..*]         nonunique  ; return : Boolean[1];}
    function   notEmpty    {in seq: Anything[0..*]        nonunique   ; return : Boolean[1];}

    function   includes {   in seq1: Anything[0..*]        nonunique   ; in seq2: Anything[0..*]        nonunique   ;
       return : Boolean[1];
    }
    function   excludes {   in seq1: Anything[0..*]        nonunique   ; in seq2: Anything[0..*]        nonunique   ;
       return : Boolean[1];
    }
    function   including {    in seq: Anything[0..*]       ordered   nonunique   ; in values: Anything[0..*]          ordered   nonunique   ;
       return : Anything[0..*]        ordered   nonunique   ;
    }
    function   includingAt    {in seq: Anything[0..*]        ordered   nonunique   ; in values: Anything[0..*]         ordered   nonunique   ;
       in index: Positive[1];        return : Anything[0..*]        ordered   nonunique   ;
    }
    function   excluding {    in seq: Anything[0..*]       ordered   nonunique   ; in values: Anything[0..*]          ordered   nonunique   ;
       return : Anything[0..*]        ordered   nonunique   ;
    }
    function   excludingAt    {in seq: Anything[0..*]        ordered   nonunique   ; in values: Anything[0..*]         ordered   nonunique   ;
       in index: Positive[1];        return : Anything[0..*]        ordered   nonunique   ;
    }
    …

137                             Last changed: 2026=04 (removed “ordered” from input to  “size” through                      Release 2026-04
                                                                 “excludes”)

### PDF PAGE 138

Sequence Functions (2)




      standard library package SequenceFunctions {
          …

          function head {in seq: Anything[0..*] ordered nonunique;
              return : Anything[0..1];
          }
          function tail {in seq: Anything[0..*] ordered nonunique ;
              return : Anything[0..*] ordered nonunique;
          }
          function last {in seq: Anything[0..*] ;
              return : Anything[0..1];
          }

          function '#' specializes BaseFunctions::'#' {
              in seq: Anything[0..*]      ordered   nonunique   ; in index: Natural[1];       return  : Anything[0..1];
          }

          behavior   add {
              inout  seq: Anything[0..*]      ordered   nonunique   ; in values: Anything[0..*]        ordered  nonunique   ;
          }
          behavior   addAt   {
              inout seq: Anything[0..*]       ordered   nonunique   ; in values: Anything[0..*]        ordered  nonunique   ;
              in index: Positive[1];
          }
          behavior   remove{
              inout  seq: Anything[0..*]      ordered   nonunique   ; in values: Anything[0..*];
          }
          behavior   removeAt  {
              inout  seq: Anything[0..*]      ordered   nonunique   ;
              in startIndex   : Positive[1];     in endIndex   : Positive[1]    default startIndex     ;
          }
      }

138                                             Last changed: 2023  -02 (changed '[' to '#')                             Release 2026-04

### PDF PAGE 139

Collection Functions






standard library package CollectionFunctions {
   …
   public import Collections::*;

   function '==' specializes BaseFunctions::'==‘
      {in col1: Collection[0..1]; in col2: Collection[0..1]; return : Boolean[1];}

   function size {in col: Collection[1]; return : Natural[1];}
   function isEmpty {in col: Collection[1]; return : Boolean[1];}
   function notEmpty {in col: Collection[1]; return : Boolean[1];}
   function contains {in col: Collection[1]; in values: Anything[*]; return : Boolean[1];}
   function containsAll {in col1: Collection[1]; in col2: Collection[2]; return : Boolean[1];}
   function head {in col: OrderedCollection[1]; return : Anything[0..1];}
   function tail {in col: OrderedCollection[1];           return : Anything[0..*] ordered nonunique;}
   function last {in col: OrderedCollection[1]; return : Anything[0..1];}

   function '#' specializes BaseFunctions::'#‘
      {in col: OrderedCollection[1]; in index: Positive[1]; return : Anything[0..1];}
   function 'array#' specializes BaseFunctions::'#‘
      {in arr: Array[1]; in indexes: Positive[n] ordered nonunique; return : Anything[0..1];}
}





 139                                     Last changed: 2024-07 (import visibility)                  Release 2026-04

### PDF PAGE 140

Vector Functions (1)




standard library package VectorFunctions {
   …

   public import VectorValues::*;

   abstract function isZeroVector {in v: VectorValue[1]; return : Boolean[1];}
   abstract function '+' specializes DataFunctions::'+'
       {in v: VectorValue[1]; in w: VectorValue[0..1]; return u: VectorValue[1];}
   abstract function '-' specializes DataFunctions::'-'
       {in v: VectorValue[1]; in w: VectorValue[0..1]; return u: VectorValue[1];}

   function VectorOf {in components: NumericalValue[1..*] ordered nonunique;
        return : NumericalVectorValue[1];}

   abstract function scalarVectorMult specializes DataFunctions::'*’
       {in x: NumericalValue[1]; in v: NumericalVectorValue[1]; return w: NumericalVectorValue[1];
   alias '*' for scalarVectorMult;
   abstract function vectorScalarMult specializes DataFunctions::'*’
       {in v: NumericalVectorValue[1]; in x: NumericalValue[1]; return : NumericalVectorValue[1];}
   abstract function vectorScalarDiv specializes DataFunctions::'/’
       {in v: NumericalVectorValue[1]; in x: NumericalValue[1]; return : NumericalVectorValue[1];}
   abstract function inner specializes DataFunctions::'*’
       {in v: NumericalVectorValue[1]; in w: NumericalVectorValue[1]; return x: NumericalValue[1];}
   abstract function norm {in v: NumericalVectorValue[1]; return l : NumericalValue[1];}
   abstract function angle {in v: NumericalVectorValue[1]; in w: NumericalVectorValue[1];
       return theta: NumericalValue[1];}

   …
}

140                                         Last changed: 2024-07 (import visibility)                        Release 2026-04

### PDF PAGE 141

Vector Functions (2)




standard library package VectorFunctions {
  …

  function CartesianVectorOf
      {in components: NumericalValue[1..*] ordered nonunique; return : CartesianVectorValue[1];}
  function CartesianThreeVectorOf specializes CartesianVectorOf
      {in components: Real[3] ordered nonunique; return : CartesianVectorValue[1];}

  function isCartesianZeroVector specializes isZeroVector
      {in v: CartesianVectorValue[1]; return : Boolean[1];}

  function 'cartesian+' specializes '+'
      {in v: CartesianVectorValue[1]; in w: CartesianVectorValue[0..1]; return: CartesianVectorValue[1];
  function 'cartesian-' specializes '-'
      {in v: CartesianVectorValue[1]; in w: CartesianVectorValue[0..1]; return: CartesianVectorValue[1];
  function cartesianScalarVectorMult specializes scalarVectorMult
      {in x: Real[1]; in v: CartesianVectorValue[1]; return : CartesianVectorValue[1];}
  function cartesianVectorScalarMult specializes vectorScalarMult
      {in v: CartesianVectorValue[1]; in x: Real[1]; return : CartesianVectorValue[1];}
  function cartesianInner specializes inner
      {in v: CartesianVectorValue[1]; in w: CartesianVectorValue[0..1]; return : Real[1];}
  function cartesianNorm specializes norm
      {in v: CartesianVectorValue[1]; return : NumericalValue[1];}
  function cartesianAngle specializes angle
      {in v: CartesianVectorValue[1]; in w: CartesianVectorValue[0..1]; return : Real[1];}

  function sum {in coll: CartesianThreeVectorValue[*]; return : CartesianThreeVectorValue[0..1];}
}


  141                                     Last changed: 2022-09 (standard library package)                     Release 2026-04

### PDF PAGE 142

Control Functions



standard library package ControlFunctions {
   private import Base::Anything;
   private import ScalarValues::ScalarValue            ;

   abstract    function    'if’ {in test: Boolean[1];
       in expr thenValue     [0..1] {   return  : Anything[0..*]       ordered   nonunique   ;}
       in expr elseValue     [0..1] {   return  : Anything[0..*]       ordered   nonunique   ;}
       return : Anything[0..*]        ordered   nonunique   ;}
   abstract    function    ‘??’ {in firstValue     : Anything[0..*];
       in expr secondValue      [0..1] {  return   : Anything[0..*]      ordered   nonunique   ;}
       return : Anything[0..*]        ordered   nonunique   ;}

   function    'and’
       {in firstValue    : Anything[0..*];      in expr secondValue      [0..1] {   return   : Boolean[1];}     return   : Boolean[1];}
   function    'or’
       {in firstValue    : Anything[0..*];      in expr secondValue      [0..1] {   return   : Boolean[1];}     return   : Boolean[1];}
   function    'implies’
       {in firstValue    : Anything[0..*];      in expr secondValue      [0..1] {   return   : Boolean[1];}     return   : Boolean[1];}

   abstract    function    collect {  in collection: Anything[0..*]          ordered   nonunique;
       in expr mapper[0..*] (argument: Anything[1]): Anything[0..*]                   ordered   nonunique   ;
       return : Anything[0..*]        ordered   nonunique    {
   }
   abstract    function    select {   in collection: Anything[0..*]          ordered   nonunique;
       in expr selector[0..*] (argument: Anything[1]): Boolean[1];
       return : Anything[0..*]        ordered   nonunique    {
   }
   abstract    function    reject {   in collection: Anything[0..*]          ordered   nonunique;
       in expr rejector[0..*] (argument: Anything[1]): Boolean[1];
       return : Anything[0..*]        ordered   nonunique    {
   }
   …
}
 142                                  Last changed: 2025   -02 (corrected 'and', 'or', 'implies' parameters)                  Release 2026-04

### PDF PAGE 143

Occurrence Functions
                                                                                Test whether two occurrences          represent
standard library package OccurrenceFunctions {                                  different portions of the same entity (i.e.,
   …                                                                            whether they have the same "identity").
   function '==='       specializes BaseFunctions::'===' {                      Can be invoked using the        === operator.
       in x: Occurrence[0..1];        in y: Occurrence[0..1];
       return   : Boolean[1];
   }
   function    isDuring   {                   Test whether a performance
       in occ: Occurrence[1];                 of this function happens
       return   : Boolean[1];
   }                                          during the input occurrence.
   function    create {
       inout   occ: Occurrence[1];
       return   : Occurrence[1];
   }                                                 Create or destroy an
   function    destroy {
       inout   occ: Occurrence[0..1];                occurrence.
       return   : Occurrence[0..1];                                                                     Add a newly created instance
   }                                                                                                    to a group of occurrences.
   function    addNew {
       inout   group: Occurrence[0..*]       nonunique   ; inout   occ: Occurrence[1];
       return   : Occurrence[1];
   }
   function    addNewAt   {
       inout   group: Occurrence[0..*]       ordered   nonunique   ; inout   occ: Occurrence[1];       in index: Positive[1];
       return   : Occurrence[1];
   }                                                                                                        Remove an instance from
   behavior    removeOld   {                                                                                a group of occurrences
       inout   group: Occurrence[0..*]       nonunique   ; inout   occ: Occurrence[0..1];
   }                                                                                                        and destroy it.
   behavior    removeOldAt    {
       inout   group: Occurrence[0..*]       ordered   nonunique   ; in index: Positive[1];
   }
}
 143                                                     Last changed: 2022  -09 (new)                                      Release 2026-04

### PDF PAGE 144

Systems Library
                       (selected models)



















144                                                             Release 2026-04

### PDF PAGE 145

Standard View Definitions









   standard library package StandardViewDefinitions {

        view def <gv> GeneralView;
        view def <iv> InterconnectionView;
        view def <afv> ActionFlowView specializes InterconnectionView;
        view def <stv> StateTransitionView specializes InterconnectionView;
        view def <sv> SequenceView;
        view def <gev> GeometryView;
        view def <gv> GridView;
        view def <bv> BrowserView;
   }










145                            Last changed: 2024-07 (updated to latest version)      Release 2026-04

### PDF PAGE 146

Metadata Domain Library




















146                                                              Release 2026-04

### PDF PAGE 147

Risk Metadata



                                       standard library package RiskMetadata {
                                          private import ScalarValues::Real;
                                          attribute def Level :> Real {
                                              assert constraint { that >= 0.0 and that <= 1.0 }
                                          }
                                          enum def LevelEnum :> Level {
                                              low = 0.25;
                                              medium = 0.50;
                                              high = 0.75;
                                          }
General risk level in terms of            attribute def RiskLevel {
probability and impact.                       attribute probability : Level;
                                              attribute impact : Level [0..1];
                                          }
Standard low, medium and                  enum def RiskLevelEnum :> RiskLevel {
high risk levels.                             low = RiskLevel(probability = LevelEnum::L);
                                              medium = RiskLevel(probability = LevelEnum::M);
                                              high = RiskLevel(probability = LevelEnum::H);
 To be used to annotate                   }
                                          metadata def Risk {
 model elements as to their                   attribute totalRisk : RiskLevel [0..1];
 risk level in typical risk areas.            attribute technicalRisk : RiskLevel [0..1];
                                              attribute scheduleRisk : RiskLevel [0..1];
                                              attribute costRisk : RiskLevel [0..1];
                                          }
                                       }

147                                       Last changed: 2024-07 (import visibility)                     Release 2026-04

### PDF PAGE 148

Modeling Metadata



                                     standard library package ModelingMetadata {
                                         …
                                         enum def StatusKind {
                                            open;
                                            tbd; // To be determined
                                            tbr; // To be resolved
    To be used to annotate                  tbc; // To be confirmed
    model elements with                     done;
    status information.                     closed;
                                         }
                                         metadata def StatusInfo {
                                            attribute originator : String [0..1];
    To be used to give a                    attribute owner : String [0..1];               This is an optional reference
    rationale for a model                   attribute status : StatusKind;
    element.                                attribute risk : Risk [0..1];                  to a feature that further
                                         }                                                 explains this rationale (e.g.,
                                         metadata def Rationale {                          a trade study analysis).
                                            attribute text : String;
    Generic issue annotation.               ref explanation : Anything [0..1];
                                         }
                                         metadata def Issue {
                                            attribute text : String;
    To be used to model a                }
    dependency in which                  metadata def <refinement> Refinement {
    source elements refine                     :>> annotatedElement : SysML::Dependency;
    target elements.                        }
                                     }

148                                    Last changed: 2022-09 (standard library package)                     Release 2026-04

### PDF PAGE 149

Parameters of Interest Metadata








 Semantic metadata for         standard library package ParametersOfInterestMetadata {
                                   private import Metaobjects::SemanticMetadata;
 identifying an attribute
 as a measure of                   attribute measuresOfEffectiveness[*] nonunique;
 effectiveness.                    attribute measuresOfPerformance[*] nonunique;

                                   metadata def <moe> MeasureOfEffectiveness :> SemanticMetadata {
                                      :>> annotatedElement : SysML::Usage;
                                      :>> baseType = measuresOfEffectiveness meta SysML::Usage;
                                   }

 Semantic metadata for             metadata def <mop> MeasureOfPerformance :> SemanticMetadata {
 identifying an attribute             :>> annotatedElement : SysML::Usage;
 as a measure of                      :>> baseType = measuresOfPerformance meta SysML::Usage;
 performance.                      }
                               }








149                                  Last changed: 2022-09 (replaced "as" with "meta")                 Release 2026-04

### PDF PAGE 150

Image Metadata





 Provides data                   standard library package ImageMetadata {
 necessary for the                   private import ScalarValues::String;
 physical definition of a            attribute def Image {                                     Binary data for the image.
 graphical image.                       attribute content : String[0..1];

                                        attribute encoding : String[0..1];                      Binary data character
                                                                                                encoding (e.g., "base64").
                                        attribute type : String[0..1];                         MIME type of the content.

 To be used to annotate                 attribute location : String[0..1];
 a model element with                }                                                         URI for image content,
 an image.                           metadata def Icon {                                       alternative to embedding
                                        attribute fullImage : Image[0..1];                     it in the content attribute.
 Full-sized image for
 rendering the                          attribute smallImage : Image[0..1];
 annotated element.                  }
                                 }

            Smaller image for use as
            an adornment or marker.



150                                          Last changed: 2022-11 (private import)                           Release 2026-04

### PDF PAGE 151

Analysis Domain Library




















151                                                                  Release 2026-04

### PDF PAGE 152

Trade Studies
                                                            An EvaluationFunction is a
standard library package TradeStudies {                     calculation that evaluates a
   private import Base::Anything;                           TradeStudy alternative.
   private import ScalarValues::*;
   private import ScalarFunctions::*;
   abstract calc def EvaluationFunction(alternative) result : ScalarValue[1];
   abstract requirement def TradeStudyObjective {
       subject selectedAlternative : Anything;                                       A TradeStudyObjective      is the
       in ref alternatives : Anything[1..*];                                         base definition for the objective
       in calc eval : EvaluationFunction;                                            of a TradeStudy, requiring the
       out attribute best : ScalarValue;                                             selectedAlternative to have best
       require constraint { eval(selectedAlternative) == best }
   }                                                                                 evaluation according to a given
   requirement def MinimizeObjective :> TradeStudyObjective {                        EvaluationFunction.
       …
       attribute :>> best = alternatives->minimize {in x; eval(x)};
   }
   requirement def MaximizeObjective :> TradeStudyObjective {
       …
       attribute :>> best = alternatives->maximize {in x; eval(x)};
   }                                                                                A TradeStudy is an analysis case whose
   abstract analysis def TradeStudy {
       subject studyAlternatives : Anything[1..*];                                  subject is a set of alternatives and
       abstract calc evaluationFunction : EvaluationFunction;                       whose result is a selection of one of
       objective tradeStudyObjective : TradeStudyObjective {                        those alternatives, based on a given
          subject :>> selectedAlternative;
          in ref :>> alternatives = studyAlternatives;                              EvaluationFunction      such that it satisfies
          in calc :>> eval = evaluationFunction;                                    the objective of the TradeStudy.
       }
       return selectedAlternative : Anything =
          studyAlternatives->selectOne {in ref a; tradeStudyObjective(selectedAlternative = a)};
}
152                                        Last changed: 2025-07 (“fn” changed to “eval”)                          Release 2026-04

### PDF PAGE 153

Analysis Tooling Annotations






                      standard library package AnalysisTooling {
                         private import ScalarValues::*;
                         metadata def ToolExecution {                            ToolExecution metadata
                            attribute toolName : String;                         identifies an external analysis
                            attribute uri : String;                              tool to be used to implement
                         }                                                       the annotated action.


                         metadata def ToolVariable {
                            attribute name : String;
                         }
                      }                                                       ToolVariable metadata is used in the
                                                                              context of an action that has been
                                                                              annotated with ToolExecution
                                                                              metadata. It is used to annotate a
                                                                              parameter or other feature of the
                                                                              action with the name of the variable
                                                                              in the tool that is to correspond to
                                                                              the annotated feature.


153                                  Last changed: 2022-09 (standard library package)                   Release 2026-04

### PDF PAGE 154

State Space Representation (1)




standard library package StateSpaceRepresentation {
   private import ISQ::DurationValue;
   private import Quantities::VectorQuantityValue;
   private import VectorCalculations::*;

   abstract attribute def StateSpace :> VectorQuantityValue;
   abstract attribute def Input :> VectorQuantityValue;
   abstract attribute def Output :> VectorQuantityValue;
   abstract calc def GetNextState
      {in input: Input;      in stateSpace: StateSpace;        in timeStep: DurationValue;        return : StateSpace;}
   abstract calc def GetOutput
      {in input: Input;      in stateSpace: StateSpace; return : Output;}
   abstract action def StateSpaceEventDef;
   action def ZeroCrossingEventDef :> StateSpaceEventDef;
   item def StateSpaceItem;

   abstract action def StateSpaceDynamics {                              StateSpaceDynamics is the simplest
      in attribute input: Input;                                         form of state space representation,
      abstract calc getNextState: GetNextState;                          and getNextState directly computes
      abstract calc getOutput: GetOutput;                                the stateSpace of the next timestep.
      attribute stateSpace: StateSpace;
      out attribute output: Output = getOutput(input, stateSpace);
   }
   abstract attribute def StateDerivative :> VectorQuantityValue { … }
   abstract calc def GetDerivative
      {in input: Input;      in stateSpace: StateSpace; return : StateDerivative;}
   abstract calc def Integrate {in getDerivative: GetDerivative; in input: Input;
      in initialState: StateSpace; in timeInterval: DurationValue; return result: StateSpace;}
   …

154                                          Last changed: 2022-11 (private import)                           Release 2026-04

### PDF PAGE 155

State Space Representation (2)
                                                                            ContinuousStateSpaceDynamics
                                                                            represents continuous behavior. The
                                                                            derivative needs to return a time
   …                                                                        derivative of stateSpace, i.e. dx/dt.

   abstract action def ContinuousStateSpaceDynamics :> StateSpaceDynamics {
      abstract calc getDerivative: GetDerivative;
      calc :>> getNextState: GetNextState {
          calc integrate: Integrate {
             in derivative = ContinuousStateSpaceDynamics::getDerivative;
             in input = GetNextState::input;
             in initialState = GetNextState::stateSpace;
             in timeInterval = GetNextState::timeStep;
             return resultState = result;
          }
      }
      event occurrence zeroCrossingEvents[0..*] : ZeroCrossingEventDef;
   }                                                                    DiscreteStateSpaceDynamics

   abstract calc def GetDifference {                                    represents discrete behavior.
      in input: Input; in stateSpace: StateSpace;                       getDifference returns the difference
      return : StateSpace;}                                             of the stateSpace for each timestep.

   abstract action def DiscreteStateSpaceDynamics :> StateSpaceDynamics {
      abstract calc getifference: GetDifference;
      calc :>> getNextState: GetNextState {
          attribute diff: StateSpace = getDifference(input, stateSpace);
          stateSpace + diff
      }
   }
}

155                                      Last changed: 2022-09 (standard library package)                       Release 2026-04

### PDF PAGE 156

Sampled Functions
                                                                                       SamplePair    is a key-value pair
                                                                                       of a domain  -value and a
                                      standard library package SampledFunctionsrange- value, used as a sample {
SampleFunction    is a variable-size,     …                                            element in SampledFunction      .
ordered collection of  SamplePair         attribute def SamplePair :> KeyValuePair {
elements representing a discretely           attribute domainValue :>> key;
sampled mathematical function.               attribute rangeValue :>> val;
                                          }

                                          attribute def SampledFunction :> OrderedMap {
     Domain and Range return all             attribute samples: SamplePair[0..*] ordered :>> elements;
     the domain values and range             assert constraint { … }                         The function is constrained
                                          }                                                  to be strictly increasing or
     values of a sampled function.                                                           strictly decreasing.
                                          calc def Domain{in fn : SampledFunction;
                                             return : Anything[0..*] = fn.samples.domainValue;}
Sample a calculation on                   calc def Range{in fn : SampledFunction;
given domain values to                       return : Anything[0..*] = fn.samples.rangeValue;}
create a SampledFunction    .             calc def Sample {in calc calculation {in x;}
                                             in attribute domainValues [0..*];
                                             return sampling;
      Interpolate a
      SampledFunction to                  calc def Interpolate {in attribute fn : SampledFunction;
      compute a result for a                 in attribute value;
      given domain value.                    return attribute result;}
                                          calc interpolateLinear : Interpolate { … }
                                      }

 156                                    Last changed: 2022-09 (standard library package)                     Release 2026-04

### PDF PAGE 157

Cause and Effect Domain Library




















157                                                              Release 2026-04

### PDF PAGE 158

Causation Connections






 A connection between one
 or more cause occurrences             standard library package CausationConnections {
 and one or more   effect                 abstract occurrence causes[*];
 occurrences.  Specializations            abstract occurrence effects[*];
 add ends for specific causes
 and effects.                             abstract connection def Multicausation {
                                             abstract constant ref occurrence causes[1..*]
                                                 :>> causes :> participant;
                                             abstract constant ref occurrence effects[1..*]
                                                 :>> effects :> participant;
                                          …
                                          }
                                          abstract connection multicausations : Multicausation[*] {

 A binary connection                      connection def Causation :> Multicausation {
 between a single cause and                  end theCauses[*] occurrence theCause
 a single effect. (But a single                  :>> causes :>> source;
 cause can separately have                   end theEffects[*] occurrence theEffect
                                                 :>> effects :>> target;
 multiple effects, and a                  }
 single effect can separately             abstract connection causations : Causation[*]
 have multiple causes.)                      :> multicausations;
                                       }

158                                 Last changed: 2025-07 (connection feature declarations)                Release 2026-04

### PDF PAGE 159

Cause and Effect Metadata


                                   standard library package CauseAndEffect {
   Used to tag the “cause”             public import CausationConnections::*;
   ends of a multicausation.           private import ScalarValues::*;
                                       private import Metaobjects::SemanticMetadata;
                                       metadata def <cause> CauseMetadata :> SemanticMetadata {
   Used to tag the “effect”               ref :>> annotatedElement : SysML::Usage;
                                          ref :>> baseType = causes meta SysML::Usage;
   ends of a multicausation.           }
                                       metadata def <effect> EffectMetadata :> SemanticMetadata {
Additional metadata about                 ref :>> annotatedElement : SysML::Usage;
                                          ref :>> baseType = effects meta SysML::Usage;
a causation connection.                }
                                       metadata def CausationMetadata {
                                          ref :> annotatedElement : SysML::ConnectionDefinition;
                                          ref :> annotatedElement : SysML::ConnectionUsage;
                                          attribute isNecessary : Boolean default false;
   Semantic metadata for                  attribute isSufficient : Boolean default false;
   multicausation .                       attribute probability : Real[0..1];
                                       }
                                       metadata def <multicausation> MulticausationSemanticMetadata
   Semantic metadata for                  :> CausationMetadata, SemanticMetadata {
   binary cauasation.                     ref :>> baseType = multicausations meta SysML::Usage;
                                       }
                                       metadata def <causation> CausationSemanticMetadadata
                                          :> CausationMetadata, SemanticMetadata {
                                          ref :>> baseType = causations meta SysML::Usage;
                                       }
                                   }
159                                      Last changed: 2024-07 (import visibility)                    Release 2026-04

### PDF PAGE 160

Requirements Derivation Domain Library




















160                                                          Release 2026-04

### PDF PAGE 161

Derivation Connections





A connection between one
original requirement  and one             standard library package DerivationConnections {
or more derived requirements.                 requirement originalRequirements[*];
Specializations add ends for                  requirement derivedRequirements[*];
specific original and derived
requirements.                                 abstract connection def Derivation {
                                                 ref requirement originalRequirement[1]
                                                        :>> originalRequirements :> participant;
      Original requirement must not              ref requirement :>> derivedRequirements[1..*]
      be a derived requirement.                         :> participant;

                                                 private assert constraint originalNotDerived { … }
                                                 private assert constraint originalImpliesDerived { … }
      Whenever the original                   }
      requirement is satisfied, all           abstract connection derivations : Derivation[*];
      the derived requirements            }
      must also be satisfied.








161                                 Last changed: 2025-07 (removed participant redefinition)                Release 2026-04

### PDF PAGE 162

Requirement Derivation Metadata





                                   standard library package RequirementDerivation {
   Used to tag the “original”          public import DerivationConnections::*;
   ends of a derivation.               private import Metaobjects::SemanticMetadata;

                                       metadata def <original> OriginalRequirementMetadata
                                          :> SemanticMetadata {
                                          :> annotatedElement : SysML::Usage;
   Used to tag the “derived”              :>> baseType = originalRequirements meta SysML::Usage;
                                       }
   ends of a derivation.
                                       metadata def <derive> DerivedRequirementMetadata
                                          :> SemanticMetadata {
                                          :> annotatedElement : SysML::Usage;
   Semantic metadata for                  :>> baseType = derivedRequirements meta SysML::Usage;
   requirement derivation.             }

                                       metadata def <derivation> DerivationMetadata
                                          :> SemanticMetadata {
                                          :> annotatedElement : SysML::ConnectionDefinition;
                                          :> annotatedElement : SysML::ConnectionUsage;
                                          :>> baseType = derivations meta SysML::Usage;
                                       }
                                   }



162                                      Last changed: 2024-07 (import visibility)                   Release 2026-04

### PDF PAGE 163

Quantities and Units Domain Library
                      (selected models)



















163                                                         Release 2026-04

### PDF PAGE 164

Quantities

                                                   A tensor quantity value
                                                   represents the value of the most           The numeric value of
standard library package Quantities {              general kind of quantity, a  tensor.       the tensor is given as
                                                                                              an array of numbers .
   abstract attribute def TensorQuantityValue :> Collections::Array {

      attribute num : ScalarValues::Number[1..*] ordered nonunique :>> elements;
      attribute mRef : UnitsAndScales::TensorMeasurementReference;
      attribute :>> dimensions = mRef::dimensions;                                              The value of a tensor
      …                                                                                         quantity is relative to a
   }                                                                                            multi-dimensional tensor

   abstract attribute def VectorQuantityValue :> TensorQuantityValue {                          measurement reference.
      attribute :>> mRef : UnitsAndScales::VectorMeasurementReference;
   }
                                                                                                  A vector is a tensor with
   abstract attribute def ScalarQuantityValue :> VectorQuantityValue {                            a single dimension.
      attribute :>> mRef : UnitsAndScales::ScalarMeasurementReference;
   }
                                                                                      A scalar is a vector with a single
   abstract attribute tensorQuantities: TensorQuantityValue[*] nonuniqueelement. Its measurement ;
   abstract attribute vectorQuantities: VectorQuantityValue[*] nonunique reference may be a :>        tensorQuantitiesmeasurement ;
   abstract attribute scalarQuantities: ScalarQuantityValue[*] nonuniqueunit if the scale is a  :>    vectorQuantitiesratio scale.;

   alias TensorQuantityValue as QuantityValue;
   alias tensorQuantities as quantity;                          A quantity is a usage of a
   …                                                            quantity value to represent
}                                                               a feature of something.

164                             Last changed: 2026-04 (corrected suptype of ScalarQuantityValue)             Release 2026-04

### PDF PAGE 165

Measurement References



                                standard library package MeasurementReferences {
                                   attribute def TensorMeasurementReference :> Array {
                                      attribute mRefs : ScalarMeasurementReference[1..*] :>> elements;
                                      …
                                   }
A tensor measurement reference
is defined as an array of scalar   attribute def VectorMeasurementReference
measurement references   , one                                         :> TensorMeasurementReference {
for each element of the tensor.       attribute :>> dimensions: Positive[0..1];
                                      …
                                   }

                                   attribute def ScalarMeasurementReference
                                                                       :> VectorMeasurementReference {
                                      attribute :>> dimensions = ();
                                      …
                                   }

                                   attribute def CoordinateFrame :> VectorMeasurementReference {
                                      attribute transformation: CoordinateTransformation[0..1];
                                   }
                                   …
                                }                                A coordinate frame is a kind of vector measurement
                                                                 reference that can be located and oriented relative to
                                                                 another frame using a coordinate transformation.

 165                                   Last changed: 2022-09 (standard library package)                    Release 2026-04

### PDF PAGE 166

Units



A measurement unit is a
measurement scale defined as a      standard library package Measurement {
sequence of unit power factors.         …

                                        abstract attribute def MeasurementUnit
A simple unit is a measurement                                               :> ScalarMeasurementReference {
unit with no power factor                  attribute unitPowerFactor : UnitPowerFactor[1..*] ordered;
                                           attribute unitConversion : UnitConversion[0..1];
dependencies on other units.            }

                                        abstract attribute def SimpleUnit :> MeasurementUnit {
                                           attribute redefines unitPowerFactor[1] {
                                              attribute redefines unit = SimpleUnit::self;
A derived unit is any unit that is            attribute redefines exponent = 1;
not simple.                                }
                                        }

                                        abstract attribute def DerivedUnit :> MeasurementUnit;

                                        attribute def UnitPowerFactor {
                                           attribute unit : MeasurementUnit;
A unit power factor is a                   attribute exponent : ScalarValues::Real;
representation of a reference           }
unit raised to an exponent.             …
                                    }


166                                    Last changed: 2022-09 (standard library package)                     Release 2026-04

### PDF PAGE 167

International System of Quantities (ISQ)
                                                                                 The International System of Quantities
                                                                                 defines seven abstract units (length,
                                    standard library package ISQ {               mass, time, electric current,
                                       import ISQBase::*;                        temperature, amount of substance,
                                       import ISQSpaceTime::*;                   luminous intensity) and many other
                                       …                                         units derived from those.
                                    }

                                    standard library package ISQBase {
A length unit is a simple unit.        attribute def LengthUnit :> SimpleUnit {…}

A length value is a quantity           attribute def LengthValue :> ScalarQuantityValue {
value with a real magnitude               attribute redefines num : ScalarValues::Real;
and a length-unit scale.                  attribute redefines mRef : LengthUnit;
                                       }

A length is a quantity with a          attribute length: LengthValue :> quantity;
length value.                          …
                                    }
                                    package ISQSpaceTime {                      The ISQ standard (ISO 80000)
                                       import ISQBase::*;                       is divided into several parts. For
                                       …                                        example, Part 3 defines units
                                    }                                           related to space and time.


167                                   Last changed: 2022-09 (standard library package)                  Release 2026-04

### PDF PAGE 168

International System of Units /
                             Système International (SI)



The International       standard library package SI {
System of Units defines    public import ISQ::*;
base units for the seven   public import SIPrefixes::*;                          A unit can be defined using
abstract ISQ unit types.                                                         prefix-based conversion
                           attribute <g> gram : MassUnit;                        from a reference unit.

                           attribute <m> metre : LengthUnit;
Each unit declaration      attribute <kg> kilogram : MassUnit {
includes the full unit        attribute redefines unitConversion : ConversionByPrefix {
name and its                    attribute redefines prefix = kilo;
abbreviation as an              attribute redefines referenceUnit = g
identifier.                   }
                           }
                           attribute <s> second : TimeUnit;
                           attribute <A> ampere : ElectricCurrentUnit;
                           attribute <K> kelvin : ThermodynamicTemperatureUnitA derived unit can be ;
                           attribute <mol> mole : AmountOfSubstanceUnit;               defined from an
                           attribute <cd> candela : LuminousIntensityUnitarithmetic expression ;
                           …                                                           of other units.

                           attribute <N> newton : ForceUnit = kg * m / s ^ 2;


 168                                  Last changed: 2024-07 (import visibility)              Release 2026-04

### PDF PAGE 169

US Customary Units



  standard library package USCustomaryUnits {
     public import ISQ::*;
     private import SI::*;

     attribute <ft> foot : LengthUnit {
        attribute redefines unitConversion : ConversionByConvention {
           attribute redefines referenceUnit = m,
           attribute redefines conversionFactor = 3048/10000;
        }
     }                                                         US customary units are defined
     …                                                         by conversion from SI units.
     attribute <mi> mile : LengthUnit {
         attribute redefines unitConversion : ConversionByConvention {
           attribute redefines referenceUnit = ft,
           attribute redefines conversionFactor = 5280;
        }
     }

     attribute <'mi/hr'> 'mile per hour' : SpeedUnit = mi / hr;
     alias mph for 'mi/hr’;
     …
  }              An alias for mile per hour.


169                                Last changed: 2024-07 (import visibility)           Release 2026-04

### PDF PAGE 170

Quantity Calculations (1)



 standard library package QuantityCalculations {
     private import ScalarValues::*;
     private import Quantities::ScalarQuantityValue;
     private import MeasurementReferences::ScalarMeasurementReference                   ;
     private   import MeasurementReferences         ::DimensionOneValue     ;

     calc def '[' specializes        BaseFunctions    ::'[' {   in num: Number[1];       in mRef  : ScalarMeasurementReference        [1];
         return quantity :      ScalarQuantityValue      [1]; }
     …
     calc def abs specializes        NumericalFunctions      ::abs
         { in x: ScalarQuantityValue        [1];  return   : ScalarQuantityValue      [1]; }
     calc def '+' specializes        NumericalFunctions      ::'+'
         { in x: ScalarQuantityValue        [1];  in y: ScalarQuantityValue       [0..1];    return  : ScalarQuantityValue       ; }
     calc def '-' specializes        NumericalFunctions      ::'-'
         { in x: ScalarQuantityValue        ; in y: ScalarQuantityValue       [0..1];    return  : ScalarQuantityValue       [1]; }
     calc def '*' specializes        NumericalFunctions      ::'*'
         { in x: ScalarQuantityValue        [1];  in y: ScalarQuantityValue       [1];   return  : ScalarQuantityValue       [1]; }
     calc def '/' specializes        NumericalFunctions      ::'/'
         { in x: ScalarQuantityValue        [1];  in y: ScalarQuantityValue       [1];   return  : ScalarQuantityValue       [1]; }
     calc def '**' specializes        NumericalFunctions      ::'**'
         { in x: ScalarQuantityValue        [1];  in y: Real[1];     return   : ScalarQuantityValue      [1]; }
     calc def '^' specializes        NumericalFunctions      ::'^'
         { in x: ScalarQuantityValue        [1];  in y: Real[1];     return   : ScalarQuantityValue      [1]; }
     calc def '<' specializes        NumericalFunctions      ::'<'
         { in x: ScalarQuantityValue        [1];  in y: ScalarQuantityValue       [1];   return  : Boolean[1]; }
     calc def '>' specializes        NumericalFunctions      ::'>'
         { in x: ScalarQuantityValue        [1];  in y: ScalarQuantityValue       [1];   return  : Boolean[1]; }
     calc def '<=' specializes        NumericalFunctions      ::'<='
         { in x: ScalarQuantityValue        [1];  in y: ScalarQuantityValue       [1];   return  : Boolean[1]; }
     calc def '>=' specializes        NumericalFunctions      ::'>='
         { in x: ScalarQuantityValue        [1];  in y: ScalarQuantityValue       [1];   return  : Boolean[1]; }
     …
 }
170                                                     Last changed: 2023  -02 (new)                                       Release 2026-04

### PDF PAGE 171

Quantity Calculations (2)







 standard library package QuantityCalculations {
     …
     calc def max specializes NumericalFunctions::max
         { in x: ScalarQuantityValue        [1];  in y: ScalarQuantityValue       [1];   return  : ScalarQuantityValue      [1]; }
     calc def min specializes        NumericalFunctions     ::min
         { in x: ScalarQuantityValue        [1];  in y: ScalarQuantityValue       [1];   return  : ScalarQuantityValue      [1]; }

     calc def '==' specializes        DataFunctions    ::'=='
         { in x: ScalarQuantityValue        [1];  in y: ScalarQuantityValue       [1];   return  : Boolean[1]; }
     calc def sqrt{ in x: ScalarQuantityValue            [1]; return    : ScalarQuantityValue      [1]; }

     calc def floor {      in x: ScalarQuantityValue       [1]; return    : ScalarQuantityValue       [1]; }
     calc def round {      in x: ScalarQuantityValue       [1]; return    : ScalarQuantityValue       [1]; }
     calc def ToString      specializes    BaseFunctions    ::ToString    { in x: ScalarQuantityValue        [1];   return  : String; }
     calc def ToInteger      { in x: ScalarQuantityValue        [1];   return  : Integer[1]; }
     calc def ToRational       { in x: ScalarQuantityValue        [1];  return   : Rational[1]; }
     calc def ToReal { in x: ScalarQuantityValue            [1]; return     : Real[1]; }
     calc def ToDimensionOneValue         { in x: Real[1];      return   : DimensionOneValue      [1]; }
     calc def sum specializes        NumericalFunctions     ::sum
         { in collection:      ScalarQuantityValue     [0..*];   return   : ScalarQuantityValue      ; }
     calc def product      specializes    NumericalFunctions      ::product
         { in collection:      ScalarQuantityValue     [0..*];   return   : ScalarQuantityValue      ; }

     calc def ConvertQuantity        { in x: ScalarQuantityValue        [1];  in targetMRef    : ScalarMeasurementReference        [1];
         return : ScalarQuantityValue        [1]; }
 }




171                                                    Last changed: 2023   -02 (new)                                       Release 2026-04

### PDF PAGE 172

Measurement Reference Calculations





 standard library package MeasurementRefCalculations {
    private import ScalarValues::String;
    private import ScalarValues::Real;
    private import MeasurementReferences::MeasurementUnit;
    private import MeasurementReferences::ScalarMeasurementReference;
    private import MeasurementReferences::CoordinateFrame;

    calc def '*' specializes DataFunctions::'*'
       { in x: MeasurementUnit[1]; in y: MeasurementUnit[1]; return : MeasurementUnit[1]; }
    calc def '/' specializes DataFunctions::'/'
       { in x: MeasurementUnit[1]; in y: MeasurementUnit[1]; return : MeasurementUnit[1]; }
    calc def '**' specializes DataFunctions::'**'
       { in x: MeasurementUnit[1]; in y: Real[1]; return : MeasurementUnit[1]; }
    calc def '^' specializes DataFunctions::'^'
       { in x: MeasurementUnit[1]; in y: Real[1]; return : MeasurementUnit[1]; }

    calc def 'CoordinateFrame*' specializes DataFunctions::'*'
       { in x: CoordinateFrame[1]; in y: MeasurementUnit[1]; return : CoordinateFrame[1]; }
    calc def 'CoordinateFrame/' specializes DataFunctions::'/'
       { in x: CoordinateFrame[1]; in y: MeasurementUnit[1]; return : CoordinateFrame[1]; }

    calc def ToString specializes BaseFunctions::ToString
       { in x: ScalarMeasurementReference[1]; return : String[1]; }
 }


172                                         Last changed: 2023-02 (new)                          Release 2026-04

### PDF PAGE 173

Vector Calculations



standard library package VectorCalculations          {
  private import     ScalarValues   ::Boolean;
  private import     ScalarValues   ::Number;
  private import     Quantities::   VectorQuantityValue     ;

  calc def '+' specializes VectorFunctions::'+’
     {in : VectorQuantityValue; in : VectorQuantityValue; return : VectorQuantityValue;}
  calc def '-' specializes VectorFunctions::'-’
     {in : VectorQuantityValue; in : VectorQuantityValue; return : VectorQuantityValue;}

  calc def scalarVectorMult specializes VectorFunctions:: scalarVectorMult
     {in : Number; in : VectorQuantityValue; return : VectorQuantityValue;}
  calc def vectorScalarMult specializes VectorFunctions:: vectorScalarMult
     {in : VectorQuantityValue; in : Number; return : VectorQuantityValue;}
  calc def vectorScalarDiv specializes RealFunctions::'*’
     {in : VectorQuantityValue; in : Number; return : VectorQuantityValue;}
  calc def inner specializes VectorFunctions::inner
     {in : VectorQuantityValue; in : VectorQuantityValue; return : Number;}
  alias scalarVectorMult as '*';

  calc def norm specializes VectorFunctions::norm
     {in : VectorQuantityValue; return : Number;}
  calc def angle specializes VectorFunctions::angle
     {in : VectorQuantityValue; in : VectorQuantityValue; return : Number;}
}

173                               Last changed: 2022-09 (standard library package)            Release 2026-04

### PDF PAGE 174

Tensor Calculations



standard library package TensorCalculations {
   private import ScalarValues::Boolean;
   private import ScalarValues::Number;
   private import Quantities::ScalarQuantityValue;
   private import Quantities::VectorQuantityValue;
   private import Quantities::TensorQuantityValue;
   private import MeasurementReferences::TensorMeasurementReference                  ;
   private   import   MeasurementReferences      ::CoordinateTransformation        ;

   calc def '[' specializes        BaseFunctions    ::'[' {   in elements: Number[1..n]         ordered;
       in mRef: TensorMeasurementReference          [1];  return quantity:      TensorQuantityValue     [1];
       private   attribute    n = mRef.flattenedSize      ;
   }
   …
   calc def '+' :>      DataFunctions    ::'+'
       ]{ in : TensorQuantityValue        [1]; in : TensorQuantityValue        [1];  return   : TensorQuantityValue      [1]; }
   calc def '-' :>      DataFunctions    ::'-'
       { in : TensorQuantityValue       [1]; in : TensorQuantityValue        [1];   return   : TensorQuantityValue      [1]; }
   calc def scalarTensorMult        { in : Number[1];       in : TensorQuantityValue      [1]; return : TensorQuantityValue          [1]; }
   calc def TensorScalarMult        { in : TensorQuantityValue        [1]; in : Number[1];       return : TensorQuantityValue        [1]; }
   calc def scalarQuantityTensorMult
       { in : ScalarQuantityValue       [1]; in : TensorQuantityValue        [1];   return   : TensorQuantityValue      [1]; }
   calc def TensorScalarQuantityMult
       { in : TensorQuantityValue       [1]; in : ScalarQuantityValue        [1];   return   : TensorQuantityValue      [1]; }
   calc def tensorVectorMult
       { in : TensorQuantityValue       [1]; in : VectorQuantityValue        [1];   return   : VectorQuantityValue      [1]; }
   calc def vectorTensorMult
       { in : VectorQuantityValue       [1]; in : TensorQuantityValue        [1];   return   : VectorQuantityValue      [1]; }
   calc def tensorTensorMult
       { in : TensorQuantityValue       [1]; in : TensorQuantityValue        [1];   return   : TensorQuantityValue      [1]; }
   calc def transform {       in transformation :       CoordinateTransformation       ; in sourceTensor     : TensorQuantityValue      ;
       return targetTensor      : TensorQuantityValue       ; }
}
 174                                                     Last changed: 2023  -02 (new)                                      Release 2026-04

### PDF PAGE 175

Time (1)


                                                                                      A singleton universal time
                                        standard library package Time {               reference.

 Clocks is a Kernel Library model          part universalClock : Clock[1] :>
 of the semantics of clocks.                  Clocks::universalClock;


 A clock provides the current              part def Clock :> Clocks::Clock {
 time as a quantity that                      attribute :>> currentTime : TimeInstantValue;
 advances monotonically over               }
 the lifetime of the clock.
                                           calc def TimeOf :> Clocks::TimeOf {
                                              in o : Occurrence[1];
 TimeOf returns the time instant              in clock : Clock[1] default localClock;
 of the start of an occurrence                return timeInstant : TimeInstantValue[1];
 relative to a given clock.                }

 DurationOf returns the                    calc def DurationOf :> Clocks::DurationOf {
 duration of a given occurrence               in o : Occurrence[1];
 relative to a given clock (the               in clock : Clock[1] default localClock;
 time of its end snapshot minus               return duration : DurationValue;
 the time of its start snapshot).          }




175                                   Last changed: 2025-02 (removed “readonly”)                   Release 2026-04

### PDF PAGE 176

Time (2)
                                               Generic time scale to                       Captures the specification
                                               express a time instant.                     of the time instant with
                                                                                           value zero, also known as
       attribute def TimeScale :> IntervalScale {                                          the (reference) epoch.
          attribute :>> unit: DurationUnit[1];
          attribute definitionalEpoch: DefinitionalQuantityValue[1];
          attribute :>> definitionalQuantityValues = definitionalEpoch;
       }                                                                                  Representation of a

       attribute def TimeInstantValue :> ScalarQuantityValue {                            time instant quantity.
          attribute :>> num: Real[1];
          attribute :>> mRef: TimeScale[1];
       }                                                                                  Generic representation of a
       attribute timeInstant: TimeInstantValue :> scalarQuantities;                       time instant as a calendar
       abstract attribute def DateTime :> TimeInstantValue;                               date and time of day.
       abstract attribute def Date :> TimeInstantValue;
       abstract attribute def TimeOfDay :> TimeInstantValue;
                                                                                          Representation of the
       attribute UTC: TimeScale {                                                         Coordinated Universal Time
          attribute :>> longName = "Coordinated Universal Time";                          (UTC) time scale.
          attribute :>> unit = SI::s;
          attribute :>> definitionalEpoch: DefinitionalQuantityValue {
             :>> num = 0;
             :>> definition = "UTC epoch at 1 January 1958 at 0 hour 0 minute 0 second";
          }
       }
       attribute def UtcTimeInstantValue :> DateTime { :>> mRef = UTC; }
       attribute utcTimeInstant: UtcTimeInstantValue;

176                                   Last changed: 2022-09 (standard library package)                    Release 2026-04

### PDF PAGE 177

Time (3)
                                                                                    Representation of an ISO 8601  -1
      attribute def Iso8601DateTimeEncoding :> String;                              date and time in extended
                                                                                    string format.
      attribute def Iso8601DateTime :> UtcTimeInstantValue {
         attribute :>> num = getElapsedUtcTime(val);                                Representation of an ISO 8601
         attribute val: Iso8601DateTimeEncoding;                                    date and time with explicit date
         private calc getElapsedUtcTime                                             and time component attributes.
            {in iso8601DateTime: Iso8601DateTimeEncoding; return : Real;}
      }
      attribute def Iso8601DateTimeStructure :> UtcTimeInstantValue {
         attribute :>> num = getElapsedUtcTime(year, month, day, hour, minute, second,
               microsecond, hourOffset, minuteOffest);
         attribute :>> mRef = UTC;
         attribute year: Integer;
         attribute month: Natural;
         attribute day: Natural;
         attribute hour: Natural;
         attribute minute: Natural;
         attribute second: Natural;
         attribute microsecond: Natural;
         attribute hourOffset: Integer;
         attribute minuteOffest: Integer;
         private calc getElapsedUtcTime(year: Integer, month: Natural, day: Natural,
            hour: Natural, minute: Natural, second: Natural, microsecond: Natural,
            hourOffset: Integer, minuteOffest: Integer) : Real;
      }
      …
   }

177                                  Last changed: 2022-09 (standard library package)                Release 2026-04

### PDF PAGE 178

Geometry Library




















178                                                                     Release 2026-04

### PDF PAGE 179

Spatial Items (1)


standard library package SpatialItems {                         A spatial item is an Item with a three-
   …                                                            dimensional spatial extent that also
   item def SpatialItem :> SpatialFrame {                       acts as a spatial frame of reference.
      item :>> self : SpatialItem;
      item :>> localClock : Clock[1] default Time::universalClock;
      attribute coordinateFrame : ThreeDCoordinateFrame[1]
         default universalCartesianSpatial3dCoordinateFrame;                               A spatial item has local
      item originPoint : Point[1] :> spaceShots;                                           time and space references
                                                                                           used within it.
      item subSpatialItems : SpatialItem[1..*] :> subitems {
         ref item :>> SpatialItem::localClock, subitems::localClock;
      }
      item componentItems : SpatialItem[0..*] ordered :> subSpatialItems {
         ref item :>> SpatialItem::localClock, subSpatialItems::localClock;
         attribute :>> coordinateFrame {
             attribute :>> transformation[1] default nullTransformation { … }
         }
      }
      private attribute cunionNum: Natural [1] = if isEmpty(componentItems) ? 0 else 1;
      private attribute componentUnion[cunionNum] :> unionsOf {
         item :>> elements : SpatialItem[1..*] = componentItems;
      }
      …
   }                                                                            A compound spatial item is a spatial
   …                                                                            item that is a (spatial) union of a
}
                                                                                collection of component spatial items.
 179                                    Last changed: 2025-07 (added subSpatialItem)                      Release 2026-04

### PDF PAGE 180

Spatial Items (2)



standard library package SpatialItems {
   …                                                                                The position of points in space can be
   calc def PositionOf :> SpatialFrames::PositionOf {
       in point : Point[1];                                                         determined relative to the space and
       in timeInstant : TimeInstantValue[1];                                        time references of a spatial item.
       in enclosingItem :>> 'frame' : SpatialItem[1];
       in clock : Clock[1] default enclosingItem.localClock;
       return positionVector : VectorQuantityValue[1];
   }
   calc def CurrentPositionOf :> SpatialFrames::CurrentPositionOf {
       in point : Point[1];
       in enclosingItem :>> 'frame' : SpatialItem[1];                                     The position of a point can move
       in clock : Clock[1] default enclosingItem.localClock;                              over time, with its "current"
       return positionVector : VectorQuantityValue[1];
   }                                                                                      position being relative to the clock
   calc def DisplacementOf :> SpatialFrames::DisplacementOf {                             reference of the spatial item.
       in point1 : Point[1];
       in point2 : Point[1];
       in timeInstant : TimeInstantValue[1];
       in spacialItem :>> 'frame' : SpatialItem[1];
       in clock : Clock[1] default spacialItem.localClock;
       return displacementVector : VectorQuantityValue[1];
   }
   calc def CurrentDisplacementOf :> SpatialFrames::CurrentDisplacementOf {
       in point1 : Point[1];
       in point2 : Point[1];
       in spacialItem :>> 'frame' : SpatialItem[1];
       in clock : Clock[1] default spacialItem.localClock;
       return displacementVector : VectorQuantityValue[1];
   }
}

 180                                       Last changed: 2022-09 (standard library package)                           Release 2026-04

### PDF PAGE 181

Shape Items (1)



                                                                                The ShapeItems package provides
               standard library package ShapeItems {                            a model of items that represent
                  …                                                             basic geometric shapes.
                  item def PlanarCurve :> Curve {
                      attribute :>> length [1];
                      …
                  }

                  item def Line :> PlanarCurve {
                      attribute :>> length;
                      attribute :>> outerSpaceDimension = 1;
                  }

                  item def PlanarSurface :> Surface {
                      attribute :>> area;
                      attribute :>> outerSpaceDimension = 2;
                      item :>> shape : PlanarCurve;
                  }

                  abstract item def Path :> StructuredCurve;
                  abstract item def Shell :> StructuredSurface;

                  …
               }



181                            Last changed: 2025-07 (StructuredCurve and StructuredSurface)            Release 2026-04

### PDF PAGE 182

Shape Items (2)



              standard library package ShapeItems {
                  …
                  item def ConicSection :> Path, PlanarCurve {
                     …
                  }

                  item def Ellipse :> ConicSection {
                     attribute :>> semiMajorAxis;
                     attribute :>> semiMinorAxis;
                     …
                  }

                  item def Circle :> Ellipse {
                     attribute :>> radius;
                     attribute :>> semiMajorAxis = radius;
                     attribute :>> semiMinorAxis = radius;
                     …
                  }
                  …

                 item def Polygon :> Path, PlanarCurve {
                     item :>> edges : Line { item :>> vertices [2]; }
                     attribute :>> isClosed = true;
                     …
                 }
              …
              }

182                                     Last changed: 2023-11 (Updated Circle)                      Release 2026-04

### PDF PAGE 183

Shape Items (3)



               standard library package ShapeItems {
                  …

                  item def Disc :> Shell, PlanarSurface {
                     attribute :>> semiMajorAxis;
                     attribute :>> semiMinorAxis;
                     item :>> shape : Ellipse [1] {
                        attribute :>> semiMajorAxis = Disc::semiMajorAxis;
                        attribute :>> semiMinorAxis = Disc::semiMinorAxis;
                     }
                     …
                  }

                  item def CircularDisc :> Disc {
                     attribute :>> radius [1];
                     attribute :>> semiMajorAxis [1] = radius;
                     attribute :>> semiMinorAxis [1] = radius;
                     item :>> shape : Circle { … }
                     …
                  }

                  item def ConicSurface :> Shell {
                     …
                  }
                  …
               }

183                                  Last changed: 2025-07 (CircularDisc attributes)                Release 2026-04

### PDF PAGE 184

Shape Items (4)




              standard library package ShapeItems {
                  …

                  item def Ellipsoid :> ConicSurface {
                     attribute semiAxis1 : LengthValue [1] :> scalarQuantities;
                     attribute semiAxis2 : LengthValue [1] :> scalarQuantities;
                     attribute semiAxis3 : LengthValue [1] :> scalarQuantities;
                     …
                  }

                  item def Sphere :> Ellipsoid {
                     attribute :>> radius [1];
                     attribute :>> semiAxis1 [1] = radius;
                     attribute :>> semiAxis2 [1] = radius;
                     attribute :>> semiAxis3 [1] = radius;
                  }

                  item def Paraboloid :> ConicSurface {
                     attribute focalDistance : LengthValue [1] :> scalarQuantities;
                     …
                  }

                  …
               }



184                                    Last changed: 2025-07 (Sphere attributes)                   Release 2026-04

### PDF PAGE 185

Shape Items (5)



                   standard library package ShapeItems {
                      …
                      item def ConeOrCylinder :> Shell {
                         attribute :>> semiMajorAxis [1];
                         attribute :>> semiMinorAxis [1];
                         attribute :>> height [1];
                         …
                      }

                      item def Cone :> ConeOrCylinder { … }
                      item def Cylinder :> ConeOrCylinder { … }

                      …

                      item def Polyhedron :>> Shell { … }
                      item def CuboidOrTriangularPrism :> Polyhedron { … }
                      item def Cuboid :> CuboidOrTriangularPrism { … }
                      item def RectangularCuboid :> Cuboid {
                         attribute :>> length [1];
                         attribute :>> width [1];
                         attribute :>> height [1];
                         …
                      }
                      alias Box for RectangularCuboid;

                      …
                   }

185                                 Last changed: 2022-09 (standard library package)                Release 2026-04

## LAYOUT-PRESERVING POPPLER EXTRACTION

### LAYOUT PDF PAGE 1

```text
Introduction to the SysML v2 Language
              Textual Notation

           This is a training presentation on the SysML v2 language.
               It is updated as appropriate for each release of the
                  SysML v2 Pilot Implementation maintained by
                the OMG® Systems Modeling Community (SMC)

                                    Release: 2026-04

                             Copyright © 2019-2026 Model Driven Solutions, Inc.
               Licensed under the Creative Commons Attribution 4.0 International License.
           To view a copy of this license, visit http://creativecommons.org/licenses/by/4.0/ or
           send a letter to Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.
```

### LAYOUT PDF PAGE 2

```text
                      Changes in this Release

 In SequenceFunctions library model, corrected input parameters to be
  unordered in “size” and following functions through “excludes”.

 In Quantities library model, corrected type of ScalarQuantityValue.

                    To find slides that have changed recently, search for
                                     Last changed: 2026-04

                               (and similarly for earlier releases).

2  Release 2026-04
```

### LAYOUT PDF PAGE 3

```text
   SysML v2 Language Architecture

           Systems Modeling Language                        Declarative semantic base
                        (SysML)                             elements and domain-
                                                            specific libraries modeled
   Systems Syntax    metamodel               Systems and    using SysML
                   semantic library         Domain Model
                                                            Declarative semantic base
                                               Libraries    elements modeled using
                                                            KerML
                  Kernel Modeling Language
                              (KerML)

   Kernel Syntax     metamodel              Kernel Model
                   semantic library           Libraries

                     semantic                               Direct semantic mapping to
                   specification                            formal logic

    Core                                    Core Semantics
   Syntax

    Root           Root syntactic elements
   Syntax          without model-level semantics
                   (e.g., packaging)

3                  Last changed: 2020-09                    Release 2026-04
```

### LAYOUT PDF PAGE 4

```text
   Four-Layer Language Architecture

 Root – Root syntactic elements

   Element, Comment, Documentation, Textual Representation, Namespace

   Relationship, Annotation, Membership, Import, Dependency

 Core – Fundamental semantic concepts – Formal declarative semantics

   Type, Classifier, Feature, Multiplicity
   Feature Membership, Specialization, Conjugation, Type Featuring, Feature Chaining, Feature

     Inverting, Unioning, Intersecting, Differencing

 Kernel – Foundation for building modeling languages – Kernel semantic library

   Class, Data Type, Behavior, Function, Metaclass, Step, Expression, Metadata Feature, Package
   Association, Interaction, Connector, Binding Connector, Succession, Item Flow, Succession Item

     Flow

 Systems – Modeling language for systems engineering – Domain libraries

   Definition and Usage of:

       ▪ Attributes, Enumerations, Occurrences, Items, Parts, Ports, Actions, States, Constraints,
         Requirements, Concerns, Calculations, Cases, Analysis Cases, Verification Cases, Use Cases, Views,
         Viewpoints, Renderings, Metadata

       ▪ Connections, Interfaces, Allocations, Flows, Succession Flows

4  Last changed: 2025-02 (“flow connection” renamed ”flow”)  Release 2026-04
```

### LAYOUT PDF PAGE 5

```text
                                    Packages – Members

   A package acts as a namespace     A name with spaces or other              An import adds either a single
   for its members and a container                                             imported member or all the
   for its owned members.               special characters is                  members of an imported package
                                        surrounded in single quotes.

                                                                               to the importing package.

                           package 'Package Example’ {

                                    public import ISQ::TorqueValue;

                                    private import ScalarValues::*;
                                                                                                 A package can introduce

   The owned members of             part def Automobile;                       aliases for its owned
   a package are elements           alias Car for Automobile;                  members or for individual
   directly contained in                                                       members of other packages.

   the package.                     alias Torque for ISQ::TorqueValue;

                           }

                                     A qualified name is a package name

                                        (which may itself be qualified) followed
                                        by the name of one of its members,
                                        separated by :: .

5                                   Last changed: 2024-07 (import visibility)     Release 2026-04
```

### LAYOUT PDF PAGE 6

```text
                               Packages – Visibility

   All members from a public import    ! Visibility must be shown
   are visible (re-exported) from the     explicitly on import declarations.
   importing package. Members             Use private visibility unless re-
   from a private import are not.         export is required.

   A private member is         package 'Package Example' {
   not visible outside the        public import ISQ::TorqueValue;
   package (but it is visible     private import ScalarValues::*;
   to subpackages).
                                  private part def Automobile;
   Members are public by
   default but can also be        public alias Car for Automobile;
   marked public                  alias Torque for ISQ::TorqueValue;
   explicitly.                 }

6                                      Last changed: 2024-07 (import visibility)  Release 2026-04
```

### LAYOUT PDF PAGE 7

```text
                                      Comments

 A comment begins with /* and     package 'Comment Example’ {
 ends with */ .                      /* This is comment, part of the model,
                                       * annotating (by default) it's owning package. */
 A comment can optionally be
 named.                           comment Comment1 /* This is a named comment. */

Import and alias declarations     comment about Automobile
can also be commented.
                                  /* This is an unnamed comment, annotating an
 A note begins with // and
 extends to the end of the line.  * explicitly specified element.
 (A multiline note begins with
 //* and ends with */.)           */                                             What the comment annotates can

7                                 part def Automobile;                           be explicitly specified (it is the
                                                                                 owning namespace by default).

                                  alias Car for Automobile {
                                     /* This is a comment annotating its owning
                                       * element.
                                       */

                                  }

                                     // This is a note. It is in the text, but not part
                                     // of the model.
                                     alias Torque for ISQ::TorqueValue;
                                  }

                                  Last changed: 2023-10 (removed "documentary")  Release 2026-04
```

### LAYOUT PDF PAGE 8

```text
                               Documentation

   Documentation is a special  package 'Documentation Example' {
   kind of comment that is        doc /* This is documentation of the owning
   directly owned by the                    * package.
   element it documents.                    */

   A documentation comment        part def Automobile {
   can be optionally named            doc Document1
   like a regular comment.                /* This is documentation of Automobile. */

                                  }

                                  alias Car for Automobile {
                                        doc /* This is documentation of the alias. */

                                  }
                                  alias Torque for ISQ::TorqueValue;
                               }

8                              Last changed: 2023-07 (corrected "ISO" to "ISQ")  Release 2026-04
```

### LAYOUT PDF PAGE 9

```text
   Part and Attribute Definitions

    A part definition is a definition of                                                      An attribute usage usage of an
    a class of systems or parts of                                                            attribute definition, used here as
    systems, which are mutable and                                                            a feature of the part definition.
    exist in space and time.
                                          part def Vehicle {
An attribute definition is a definition      attribute mass : ScalarValues::Real;
of attributive data that can be used
to describe systems or parts.             part eng : Engine;  A part usage is a composite
                                                              feature that is the usage of a
 Definitions and usages are also
    namespaces that allow import.                                                         part definition.
                                          ref part driver : Person;

                                          }
                                                                                              A reference part usage is a

                                          attribute def VehicleStatus {referential feature that is the
                                             private import ScalarValuesus:a:g*e;of a part definition.

                                          attribute gearSetting : Integer;

                                          attribute acceleratorPosition : Real;

                                          }
                                                                                                     An attribute definition

                                          part def Engine;          may not have composite
                                          part def Person;          features. Attribute usages
                                                                    are always referential.

9  Last changed: 2023-10 (corrected callout on attribute features)                                          Release 2026-04
```

### LAYOUT PDF PAGE 10

```text
                        Generalization/Specialization

                        abstract part def Vehicle;              A specialized definition defines
                                                                a subset of the classification of
                                                                its generalization.

An abstract definition  part def HumanDrivenVehicle specializes Vehicle {
is one whose instances
must be members of      }  ref part driver : Person; The :> symbol is equivalent
some specialization.
                                                    to the specializes keyword.

                        part def PoweredVehicle :> Vehicle {

                           part eng : Engine;

                        }                           A specialization can define

                                                    additional features.

                        part def HumanDrivenPoweredVehicle :>

                           HumanDrivenVehicle, PoweredVehicle;

                        part def Engine;            A definition can have multiple
                        part def Person;            generalizations, inheriting the
                                                    features of all general definitions.

10                         Last changed: 2020-06                                  Release 2026-04
```

### LAYOUT PDF PAGE 11

```text
       Subsetting

    part def Vehicle {                   Subsetting asserts that, in any
       part parts : VehiclePart[*];      common context, the values of one
                                         feature are a subset of the values of
                                         another feature.

       part eng : Engine subsets parts;

       part trans : Transmission subsets parts;

       part wheels : Wheel[4] :> parts;

    }                                    Subsetting is a kind of

    abstract part def VehiclePart;       generalization between features.

    part def Engine :> VehiclePart;

    part def Transmission :> VehiclePart;

    part def Wheel :> VehiclePart;

11     Last changed: 2020-06                                      Release 2026-04
```

### LAYOUT PDF PAGE 12

```text
                                  Redefinition

                                                                                 A specialized definition can

                                                                                 redefine a feature that would

                               part def Vehicle {                                otherwise be inherited, to change
                                  part eng : Engine;                             its name and/or specialize its type.

                               }

                               part def SmallVehicle :> Vehicle {

                                  part smallEng : SmallEngine redefines eng;

                               }                                                 The :>> symbol is equivalent

                               part def BigVehicle :> Vehicle {                  to the redefines keyword.

                                  part bigEng : BigEngine :>> eng;

                               }
                                                                                             A feature can also specify

There is shorthand notation    part def Engine {                                 multiplicity.
for redefining a feature with
the same name.                    part cyl : Cylinder[4..6];

                               }                                                  The default multiplicity for

                               part def SmallEngine :> Engine { parts is 1..1.

                                  part redefines cyl[4];

                               }

                               part def BigEngine :> Engine {

                                  part redefines cyl[6];

                               }
                                                                                   Redefinition can be used to constrain

                               part def Cylinder;             the multiplicity of a feature.

12                                Last changed: 2021-08 (multiplicity defaults)                 Release 2026-04
```

### LAYOUT PDF PAGE 13

```text
    Enumeration Definitions (1)

    An enumeration definition is a kind
    of attribute definition that defines
    a set of enumerated values.

    enum def TrafficLightColor {  The values of an attribute usage defined
       enum green;                by an enumeration definition are limited
       enum yellow;               to the defined set of enumerated values.
       enum red;

    }

    part def TrafficLight {
       attribute currentColor : TrafficLightColor;

    }

    part def TrafficLightGo specializes TrafficLight {
       attribute redefines currentColor = TrafficLightColor::green;

    }

                   This shows an attribute being bound to a
                   specific value (more on binding later).

13  Last changed: 2020-12 (new)                     Release 2026-04
```

### LAYOUT PDF PAGE 14

```text
                            Enumeration Definitions (2)

                         attribute def ClassificationLevel {             An enumeration definition can
                             attribute code : String;                    contain nothing but declarations of its
                             attribute color : TrafficLightColor;        enumerated values. However, it can
                                                                         specialize a regular attribute
                         }                                               definition and inherit nested features.

                         enum def ClassificationKind specializes ClassificationLevel {

                            unclassified {

                            :>> code = "uncl";

The enum keyword is             :>> color = TrafficLightColor::green;    ! An enumeration definition
optional when declaring     }                                               cannot specialize another
                            confidential {                                  enumeration definition.

                                :>> code = "conf";

enumerated values.              :>> color = TrafficLightColor::yellow;
                            }

                            secret {

                                :>> code = "secr";                       The nested features can then be
                                :>> color = TrafficLightColor::red;      bound to specific values in each of
                            }

                         }                                               the enumerated values.

                         enum def GradePoints :> Real {

                            A = 4.0;

                            B = 3.0;        Enumerated values can also be bound
                            C = 2.0;        directly to specific values of a specialized
                            D = 1.0;        attribute definition or data type.
                            F = 0.0;

                         }

14                                          Last changed: 2020-12 (new)                   Release 2026-04
```

### LAYOUT PDF PAGE 15

```text
                                  Parts (1)

                               // Definitions

                               part def Vehicle {

                                  part eng : Engine;

                               }

                               part def Engine {

    Parts can be specified        part cyl : Cylinder[4..6];
    outside the context of a
    specific part definition.  }                                     The defined by relationship is a
                               part def Cylinder;                    kind of generalization.

                               // Usages                             Parts inherit properties from
                               part smallVehicle : Vehicle {         their definitions and can
                                                                     redefine them, to any level of
                                  part redefines eng {               nesting.
                                      part redefines cyl[4];

                                  }
                               }
                               part bigVehicle : Vehicle {

                                  part redefines eng {
                                      part redefines cyl[6];

                                  }
                               }

15                                Last changed: 2020-12 (editorial)  Release 2026-04
```

### LAYOUT PDF PAGE 16

```text
    Parts (2)

    // Definitions      Composite structure can be
    part def Vehicle;   specified entirely on parts.
    part def Engine;
    part def Cylinder;

    // Usages                          A part can specialize
    part vehicle : Vehicle {           another part.

       part eng : Engine {
           part cyl : Cylinder[4..6];

       }
    }
    part smallVehicle :> vehicle {

       part redefines eng {
           part redefines cyl[4];

       }
    }
    part bigVehicle :> vehicle {

       part redefines eng {
           part redefines cyl[6];

       }
    }

16  Last changed: 2020-06                                     Release 2026-04
```

### LAYOUT PDF PAGE 17

```text
                                                  Items

    An item definition defines a class of                            All parts can be treated as items, but
    things that exist in space and time but                             not all items are parts. The design of a
    are not necessarily considered "parts"                              system determines what should be
    of a system being modeled.                                          modeled as its "parts".

                              item def Fuel;                        A system model may reference discrete
                              item def Person;                      items that interact with or pass through
                                                                    the system.
                              part def Vehicle {
                                 attribute mass : Real;

 The default multiplicity       ref item driver : Person;

    for attributes and items     part fuelTank {
    is also 1..1.                    item fuel: Fuel;

                                 }                                  Items may also model continuous

                              }                                     materials that are stored in and/or flow

     An item is continuous if any portion of it in space is the    between parts of a system.

    same kind of thing. A portion of fuel is still fuel. A portion

    of a person is generally no longer a person.

17                                  Last changed: 2021-08 (multiplicity defaults)               Release 2026-04
```

### LAYOUT PDF PAGE 18

```text
                                         Connections (1)

Cross multiplicities constrain  connection def PressureSeat {                        A connection definition is
the number of connections,          end [1] part bead : TireBead;                    a part definition whose
rather than end values. E.g.,       end [1] part mountingRim: TireMountingRim;       usages are connections
for every TireBead there                                                             between its ends.
must be a PressureSeat          }
connection to exactly one
TireMountingRim.                part wheelHubAssembly : WheelHubAssembly {

A connection is a usage of a       part wheel : WheelAssembly[1] {
connection definition,
which connects two other              part t : Tire[1] {
features.
                                         part bead : TireBead[2];
If a connection definition is
not specified, a generic              }
connection definition
(called Connection) is used.          part w: Wheel[1] {

 18                                      part rim : TireMountingRim[2];

                                         part mountingHoles : LugBoltMountingHole[5];

                                      }

                                      connection : PressureSeat

                                         connect bead references t.bead              Reference subsetting
                                         to mountingRim references w.rim;

                                   }                                                 (references or ::>) relates

                                   part lugBoltJoints : LugBoltJoint[0..5];          feature to a connector ends.
                                   part hub : Hub[1] {                               “Dot” notation specifies
                                                                                     paths to nested features.
                                       part h : LugBoltThreadableHole[5];

                                   }

                                   connect [0..1] lugBoltJoints to [1] wheel.w.mountingHoles;

                                   connect [0..1] lugBoltJoints to [1] hub.h;

                                }

                                         Last changed: 2024-12 (cross multiplicity)    Release 2026-04
```

### LAYOUT PDF PAGE 19

```text
    Connections (2)

                                                      These are owned features of
                                                      the part wheel, not the part
                                                      definition WheelAssembly.

    Feature chains (“dot notation”) like
    wheel.w.mountingHoles can be
    used to refer to the value of a
    specific feature in context (similarly
    to property paths in SysML v1).

19  Last changed: 2024-12 (feature chain callout)  Release 2026-04
```

### LAYOUT PDF PAGE 20

```text
                                           Ports                        Ports may have attribute and
                                                                        reference features. A feature
                                  port def FuelOutPort {                with a direction (in, out or
                                     attribute temperature : Temp;      inout) is a directed feature.
                                     out item fuelSupply : Fuel;
A port definition defines            in item fuelReturn : Fuel;
features that can be
made available via ports.         }
(Replaces interface
blocks in SysML v1).              port def FuelInPort {

 Directed features are              attribute temperature : Temp;
    always referential, so it is
    not necessary to explicitly      in item fuelSupply : Fuel;         Two ports are compatible for
    use the ref keyword.             out item fuelReturn : Fuel;        connection if they have
                                  }                                     directed features that match
A port is a connection point
through which a part              part def FuelTankAssembly {           with inverse directions.
definition makes some of
its features available in a          port fuelTankPort : FuelOutPort;
limited way. (Like a proxy
port in SysML v1.)                }

                                  part def Engine {
                                     port engineFuelPort : FuelInPort;

                                  }

20                                   Last changed: 2021-05 (editorial)  Release 2026-04
```

### LAYOUT PDF PAGE 21

```text
                                         Port Conjugation

Every port definition has an implicit    port def FuelPort {
conjugate port definition that reverses     attribute temperature : Temp;
input and output features. It has the       out item fuelSupply : Fuel;
name of the original definition with ~      in item fuelReturn : Fuel;
prepended (e.g., '~FuelPort').
                                         }

                                         part def FuelTankAssembly {
                                            port fuelTankPort : FuelPort;

                                         }

                                         part def Engine {
                                            port engineFuelPort : ~FuelPort;

                                         }

                                         Using a ~ symbol on the port type is a
                                         shorthand for using the conjugate port
                                         definition (e.g., FuelPort::'~FuelPort').

21                                       Last changed: 2021-05 (editorial)          Release 2026-04
```

### LAYOUT PDF PAGE 22

```text
                              Interfaces

An interface definition is a  interface def FuelInterface {
connection definition            end port supplierPort : FuelOutPort;
whose ends are ports.            end port consumerPort : FuelInPort;

 The default cross           }
    multiplicity is 0..*.
                              part vehicle : Vehicle {
An interface usage is a          part tankAssy : FuelTankAssembly;
connection usage                 part eng : Engine;
defined by an interface
definition, connecting           interface : FuelInterface connect
two compatible ports.                supplierPort ::> tankAssy.fuelTankPort to
                                     consumerPort ::> eng.engineFuelPort;

                              }

22                            Last changed: 2024-12 (cross multiplicity)  Release 2026-04
```

### LAYOUT PDF PAGE 23

```text
                             Interface Decomposition

                                              «interface def»
                                              WaterDelivery

                               [1]      hot                    hot                      [1..*]
                          suppliedBy :                                              deliveredTo :
                          SpigotBank
                                                                                       Faucet

 Every suppliedBy                      cold                   cold

SpigotBank must have                                                                    Connection ends specify the
                                                                                        participants in the
one or more connections                                                                 connection. They always
                                                                                        have multiplicity 1..1 relative
to deliveredTo Faucets.                                                                 to the connection definition.

                          interface def WaterDelivery {                             Connection usages interconnect
                                                                                    specific participants.
                          end [1] port suppliedBy : SpigotBank {

Cross multiplicities          port hot : Spigot;
correspond to navigating      port cold : Spigot;
across connections.       }
                          end [1..*] port deliveredTo : Faucet {

                             port hot : FaucetInlet;

                             port cold : FaucetInlet;

                          }

                              connect suppliedBy.hot to deliveredTo.hot;
                              connect suppliedBy.cold to deliveredTo.cold;
                          }

23                                      Last changed: 2024-12 (cross multiplicity)                 Release 2026-04
```

### LAYOUT PDF PAGE 24

```text
       Binding Connections

    part tank : FuelTankAssembly {           A binding connection is a connection

    port redefines fuelTankPort {            that asserts the equivalence of the

       out item redefines fuelSupply; connected features (i.e., they have

       in item redefines fuelReturn; equal values in the same context).

    }

    bind fuelTankPort.fuelSupply = pump.pumpOut;
    bind fuelTankPort.fuelReturn = tank.fuelIn;

       part pump : FuelPump {                Usages on parts can also have
           out item pumpOut : Fuel;          direction (and are automatically
           in item pumpIn : Fuel;            referential).

       }
       part tank : FuelTank {

           out item fuelOut : Fuel;
           in item fuelIn : Fuel;
       }
    }

24     Last changed: 2021-04 (dot notation)       Release 2026-04
```

### LAYOUT PDF PAGE 25

```text
       Binding Connections – Feature Values

    part tank : FuelTankAssembly {
       port redefines fuelTankPort {
           out item redefines fuelSupply = pump.pumpOut;

          in item redefines fuelReturn;
       }

       part pump : FuelPump {            The feature value notation
          out item pumpOut : Fuel;       combines the definition of a
          in item pumpIn : Fuel;         feature with a binding connection.

       }
       part tank : FuelTank {

          out item fuelOut : Fuel;

          in item fuelIn : Fuel = fuelTankPort.fuelReturn;

       }

    }                                    ! This is a binding, not an

                                         initial or default value.

25        Last changed: 2023-10 (moved fuelSupply feature value, revised callouts)  Release 2026-04
```

### LAYOUT PDF PAGE 26

```text
                              Flows

                       «part» A flow transfers a payload
                  vehicle : Vehiclefrom the source output to

                                      the target input.

    fuelTankPort                                 engineFuelPort

    «part»                    Fuel               «part»

    tankAssy :    fuelSupply         fuelSupply   eng :
    FuelTank                                     Engine

    Assembly

                              But it is actually a
                              connection between the
                              source and target ports.

     A flow is streaming if the transfer is ongoing between
        the source and target, as opposed to happening once
        after the source generates its output and before the
        target consumes its input.

26  Last changed: 2025-02 (“flow connection” renamed ”flow”)     Release 2026-04
```

### LAYOUT PDF PAGE 27

```text
                                    Flow Usage

A flow usage is a transfer of       part vehicle : Vehicle {
some payload from an output            part tankAssy : FuelTankAssembly;
of a source port to an input of        part eng : Engine;
a target port.
                                       flow of Fuel
 Specifying the payload type              from tankAssy.fuelTankPort.fuelSupply
    (e.g., “of Fuel”) is optional.         to eng.engineFuelPort.fuelSupply;

                                       flow of Fuel
                                           from eng.engineFuelPort.fuelReturn
                                           to tankAssy.fuelTankPort.fuelReturn;

                                    }

27                                  Last changed: 2025-02 (“flow connection” renamed ”flow”)  Release 2026-04
```

### LAYOUT PDF PAGE 28

```text
    Flows in Interfaces

    interface def FuelInterface {         Flows can be defined within
       end supplierPort : FuelOutPort;    an interface definition.
       end consumerPort : FuelInPort;

       flow supplierPort.fuelSupply to consumerPort.fuelSupply;
       flow consumerPort.fuelReturn to supplierPort.fuelReturn;
    }

    part vehicle : Vehicle {              The flows are established
       part tankAssy : FuelTankAssembly;  when the interface is used.
       part eng : Engine;

       interface : FuelInterface connect
           supplierPort ::> tankAssy.fuelTankPort to
           consumerPort ::> eng.engineFuelPort;

    }

28  Last changed: 2025-02 (“flow connection” renamed ”flow”)           Release 2026-04
```

### LAYOUT PDF PAGE 29

```text
                                         Flow Definitions

    A flow definition is used to assert                          The definition can (optionally)
    that a flow must exist between                               constrain the payload
    the instances of part definitions.                           transferred by usages.

                           flow def FuelFlow {                                          Note that the default
                              ref :>> payload : Fuel;                                   end multiplicities on this
                              end port fuelOut : FuelOutPort;                           connection are 1 to 1.
                              end port fuelIn : FuelInPort;

                           }

This usage realizes the    part vehicle : Vehicle {
required flow between the                part tankAssy : FuelTankAssembly; The payload should be
tankAssy.fuelTankPort and                                                               consistent with what is
the eng.engineFuelPort.                  part eng : Engine;
                                                                                        declared in the flow

                                         flow : FuelFlow of Fuel                        definition (if any).

                                         from tankAssy.fuelTankPort.fuelSupply

                                         to eng.engineFuelPort.fuelSupply;

                           }

                           The connection is defined to be

                           between the ports, but the transfer

                           is still from an output to an input.

29                                       Last changed: 2025-07 (payload in flow usage)            Release 2026-04
```

### LAYOUT PDF PAGE 30

```text
                                      Action Definition

An action definition is a definition                          Directed features of an action definition
of some action to be performed.                               are considered to be action parameters.

                            action def Focus{ in scene : Scene; out image : Image; }
                            action def Shoot{ in image : Image; out picture : Picture; }

                   scene    action def TakePicture {      An action is a usage of an action definition
                               in scene : Scene;          performed in a specific context.
       «action def»            out picture : Picture;
        TakePicture
                               bind focus.scene = scene;
             =
                   scene    action focus : Focus { in scene; out image; }A;flow caonnbeecutisoendctaon

          «action»                                                                    btreanusfeedr titoetmrasnbsefetwr een
            focus
                            flow focus.image to shoot.image;                          iatcetmiosnbs.etween actions.
                   image
                   image    action shoot : Shoot { in image; out picture; }

          «action»             bind shoot.picture = picture;                          An action has parameters
           shoot            }                                                         corresponding to its action
                                                                                      definition.
                   picture
              =             Last changed: 2025-02 (“flow connection” renamed ”flow”)  Release 2026-04

                   picture

30
```

### LAYOUT PDF PAGE 31

```text
                       Action Succession (1)

                       action def Focus{ in scene : Scene; out image : Image; }
                       action def Shoot{ in image : Image; out picture : Picture; }

              scene    action def TakePicture {
                          in scene : Scene;
    «action def»          out picture : Picture;
    TakePicture
                       bind focus.scene = scene;
         =
              scene    action focus : Focus { in scene; out image; }

      «action»         flow focus.image to shoot.image; A succession asserts that the
        focus
                       first focus then shoot;                     first action must complete
              image                                                before the second can begin.

              image    action shoot : Shoot { in image; out picture; }

      «action»            bind shoot.picture = picture;
        shoot          }

              picture
         =

              picture

31                     Last changed: 2024-09 (succession graphic)       Release 2026-04
```

### LAYOUT PDF PAGE 32

```text
                          Action Succession (2)

                          action def Focus{ in scene : Scene; out image : Image; }
                          action def Shoot{ in image : Image; out picture : Picture; }

                 scene    action def TakePicture {                         A succession flow requires the
                             in scene : Scene;                             first action to finish producing
      «action def»           out picture : Picture;                        its output before the second
      TakePicture                                                          can begin consuming it.
                             bind focus.scene = scene;
            =
                 scene    action focus : Focus { in scene; out image; }

        «action»          succession flow focus.image to shoot.image;
          focus
                          action shoot : Shoot { in image; out picture; }
«succession image
    flow» image              bind shoot.picture = picture;
                          }
        «action»
          shoot

                 picture
             =

                 picture

32                        Last changed: 2024-09 (succession flow graphic)  Release 2026-04
```

### LAYOUT PDF PAGE 33

```text
                         Action Notation Shorthands

                scene    action def Focus{ in scene : Scene; out image : Image; }
                         action def Shoot{ in image : Image; out picture : Picture; }
     «action def»
      TakePicture        action def TakePicture {                    This qualified name refers to the
                            in scene : Scene;                        scene parameter of TakePicture,
           =                                                         rather than the parameter of
                scene
                         action focus : Focus {                      focus with the same name.
        «action»
         focus           in scene = TakePicture::scene;

                image       out image;  This is the same shorthand
                         }              for binding used previously.
                image
                         flow focus.image to shoot.image;
        «action»
         shoot           then action shoot : Shoot {
                            in image;
                picture     out picture;
            =
                         }
                picture
                            out picture : Picture = shoot.picture;
This is a shorthand for  }
a succession between
the lexically previous
action (focus) and this
action (shoot).

33                       Last changed: 2024-09 (succession graphic)   Release 2026-04
```

### LAYOUT PDF PAGE 34

```text
                           Action Decomposition

                           action def Focus{ in scene : Scene; out image : Image; }
                           action def Shoot{ in image : Image; out picture : Picture; }
                           action def TakePicture{in scene : Scene; out picture : Picture;}

                  scene    action takePicture : TakePicture { An action usage can also
                                                              be directly decomposed
         «action»          in scene;
takePicture : TakePicture                                     into other actions.

             =             action focus : Focus {                      takePicture is a usage, so dot
                  scene       in scene = takePicture::scene;           notation could be used here, but
                              out image;                               it is unnecessary because scene is
         «action»                                                      in an outer scope, not nested.
           focus           }

                  image    flow focus.image to shoot.image;

                  image    then action shoot : Shoot {
                              in image;
         «action»             out picture;
           shoot
                           }
                  picture
              =

                  picture

                              out picture = shoot.picture;
                           }

34                         Last changed: 2024-09 (succession graphic)                   Release 2026-04
```

### LAYOUT PDF PAGE 35

```text
                              Conditional Succession (1)

                           action takePicture : TakePicture {
                              in scene;

                  scene    action focus : Focus {
                              in scene = takePicture::sceneA;conditional succession asserts that the
         «action»
takePicture : TakePicture     out image;                    second action must follow the first only

                           }                                if a guard condition is true. If the guard

    =                                                       is false, succession is not possible.
         scene

    «action»               first focus                                    ! Note that, currently,
     focus                    if focus.image.isFocused then shoot;           the target action must
                                                                             be explicitly named (no
   [image.    image        flow focus.image to shoot.image;                  shorthand).
isFocused]    image
                           action shoot : Shoot {
    «action»                  in image;
     shoot                    out picture;

        picture            }
    =

                              out picture = shoot.picture;
                           }

35                            Last changed: 2024-09 (succession graphic)  Release 2026-04
```

### LAYOUT PDF PAGE 36

```text
                              Conditional Succession (2)

                  scene    action takePicture : TakePicture {
                              in scene;
         «action»             out picture;
takePicture : TakePicture
                           action focus : Focus {

    =                         in scene = takePicture::scene;
         scene
                              out imageT;his is a shorthand for a conditional succession
    «action»
     focus                 }  following the lexically previous action.

   [image.    image        if focus.image.isFocused then shoot;
isFocused]    image

    «action»               flow focus.image to shoot.image;
     shoot

        picture            action shoot : Shoot {
    =                         in image;
                              out picture;
            picture
                           }

                              out picture = shoot.picture;
                           }

36                            Last changed: 2024-09 (succession graphic)                  Release 2026-04
```

### LAYOUT PDF PAGE 37

```text
    References the start of     Merge Nodes
    the action as the source
    of the initial succession.

                        action takePicture : TakePicture {

                        first start;                                         A merge node waits for exactly
                        then merge continue;                                 one predecessor to happen

             continue                                                          before continuing.
                        then action trigger { out item scene; }
    trigger
                        flow trigger.scene to focus.scene;
               scene
               scene    then action focus : Focus {

     focus                      in scene;

               image            out image;
               image
                        }
     shoot
                        flow focus.image to shoot.image;
               picture
               picture  then action shoot : Shoot {

    display                     in image;

                                out picture;

                        }

                        flow shoot.picture to display.picture;

                        then action display {

                                in picture;

                        }

                           then continue;      References the merge node named
                        }                      “continue” as the target of the succession.

37                              Last changed: 2024-09 (succession graphics)                        Release 2026-04
```

### LAYOUT PDF PAGE 38

```text
                                        Decision Nodes

                                     action def ChargeBattery {
                                        first start;

                                     then merge continueCharging;

             continueCharging        then action monitor : MonitorBattery {
    monitor
                                        out batteryCharge : Real;
             [batteryCharge >= 100]
                                     }              A decision node (decide keyword) chooses

                                     then decide;   exactly one successor to happen after it.

                                        if monitor.batteryCharge < 100 then addCharge;

                                        if monitor.batteryCharge >= 100 then endCharging;

    [batteryCharge < 100]            action addCharge : AddCharge {

    addCharge                           in charge = monitor.batteryCharge;
                        endCharging
                                     }                                               A decision node is typically followed

                                     then continueCharging;                          by one or more conditional

                                                                                     successions (the last “if…then” can

                                     action endCharging : EndChargbienrge;placed by “else”).

                                        then done;  References the end of the action
                                     }              as the target of a succession.

38                                      Last changed: 2024-09 (succession graphics)   Release 2026-04
```

### LAYOUT PDF PAGE 39

```text
                                       Control Structures

                                        Control-structure actions provide a

                                       structured alternative to control

    A loop action repeatedly           nodes for conditionals and looping.

    performs a body action.          action def ChargeBattery { This is the body action, which
                                                                                         is given the name charging.

                                       loop action charging {                 (The default name is body.)

An if action performs its body if a    action monitor : MonitorBattery {

Boolean condition is true. (It can        out charge;

also have an else part, which is       }

performed if the condition is false.)

until introduces a Boolean             then if monitor.charge < 100 {         ! if used in this way
condition that terminates the             action addCharge : AddCharge {         represents an action,
                                              in charge = monitor.charge;        not a succession.
                                          }

loop when it is true.                  }

 A loop action can also begin          } until charging.monitor.charge >= 100;
    with while (instead of loop),
    introducing a Boolean               then action endCharging : EndCharging;
    condition that terminates           then done;
    the loop when it is false.       }

39                                        Last changed: 2021-12 (new)            Release 2026-04
```

### LAYOUT PDF PAGE 40

```text
                                          Fork and Join Nodes

                                                          A fork node enables all its

                                                                     successors to happen after it.

                                       action def Brake {

                 turnOn                   action turnOn;

   monitor                                then fork;                                   The source for all these
 BrakePedal                                   then monitorBrakePedal;                  successions is the fork node.
                                              then monitorTraction;
                monitor
                Traction                  then braking;

                              braking     action monitorBrakePedal : MonitorBrakePedal {
                                              out brakePressure; }
40
                                          then joinNode;
                                          action monitorTraction : MonitorTraction {

                                              out modulationFrequency; }
                                          then joinNode;

                                          flow monitorBrakePedal.brakePressure to

                                          braking.breakPressure;

                                          flow monitorTraction.modulationFrequency to

                                          braking.modulationFrequency;

                                          action braking : Braking {

                                          in brakePressure;

                                          in modulationFrequency; }

                                          then joinNode;

                                          join joinNode;     A join node waits for all its predecessors
                                          then done;         to happen before continuing.

                                       }

                                          Last changed: 2024-09 (succession graphics)                Release 2026-04
```

### LAYOUT PDF PAGE 41

```text
                                  Performed Actions

      perform identifies the                                                    takePhoto is the local name
      owner as the performer                                                    of the performing action.
      of an action.
                                  part camera : Camera {
    This shorthand simply
    identifies the performed      perform action takePhoto[*] ordered
    action owned elsewhere           references takePicture;
    without renaming it locally.
                                  part f : AutoFocus {                          The performing action
                                     perform takePhoto.focus;                   references the performed
                                                                                action takePicture.
                                  }

                                     part i : Imager {
                                         perform takePhoto.shoot;

                                     }
                                  }

41                                Last changed: 2022-08 (reference subsetting)  Release 2026-04
```

### LAYOUT PDF PAGE 42

```text
                                      Terminate Actions (1)

performCriticalActivity               action def MonitoredActivity {          monitorCriticalActivity
                                          first start;                        and criticalActivity are
       «perform»                                                              preformed concurrently.
    monitorCritical                       then fork;
                                             then performCriticalActivity;
         Activity                            then waitForTimeOut;

       «perform»                      action performCriticalActivity {
     criticalActivity                    perform monitorCriticalActivity;

                                         perform criticalActivity;

                                         then terminate;                      A terminate action ends its

                                      }                                       immediately containing action. In

                                      then stop;                              this case, performCriticalActivity

                                                                              terminates even if monitorCritical

                                      action waitForTimeOut;                  Activity is still ongoing.

                                      then stop;

       stop              waitForTime      action stop terminate;              This terminates MonitoredActivity
42                            Out     }                                       when either performCriticalActivity
                                                                              or waitForTimeOut completes.
                                                 Last changed: 2024-11 (new)
                                                                                                           Release 2026-04
```

### LAYOUT PDF PAGE 43

```text
    Terminate Actions (2)

    part def Processor {
        ref action workflowProcess : WorkflowProcess;

        action internalProcess {   A terminate action can have an
            // ...                 argument that identifies the action
                                   to be terminated (instead of the
        }                          default to the containing action).
    }

    action terminateProcessing {
        in processor : Processor;

    terminate processor.workflowProcess;

        terminate processor;       A terminate action can also be used
    }                              to terminate (”destroy”) a part.

    ! A composite action is automatically terminated when its
       containing part is terminated, but a referential action is
       not. That is why workflowProcess was terminated
       explicitly in this example, but not internalProcess.

43                                                                 Release 2026-04
```

### LAYOUT PDF PAGE 44

```text
                                        Assignment Actions

                               action def ComputeMotion {                               Using := instead of =

                                  in attribute powerProfile :> ISQ::power[*]; here indicates an

                                  in attribute vehicleMass :> ISQ::mass;                initial value, instead

A for loop action repeatedly      in attribute initialPosition :> ISQ::length; of a binding.
performs its body, setting a      in attribute initialSpeed :> ISQ::speed;
loop variable to successive       in attribute deltaT :> ISQ::time;
values from the result of a       out attribute positions :> ISQ::length[*] := ( );

sequence expression.              private attribute position := initialPosition;

                                  private attribute speed := initialSpeed;

                                  for vehiclePower in powerProfile {

An action may also be                perform action dynamics : StraightLineDynamics {
performed by another                     in power = vehiclePower;
action (similar to a "call").            in mass = vehicleMass;
                                         in delta_t = deltaT;

                                        in x_in = position; in v_in = speed;

An assignment action sets               out x_out; out v_out;

the value of a feature to the        }

result of an expression at           then assign position := dynamics.x_out;

the time of performance of           then assign speed := dynamics.v_out;                The functions including
the assignment.
                                     then assign positions :=                           comes from the

                                        positions->including(position);

                                  }                                                     SequenceFunctions

                               }                                                        library package.

44                                   Last changed: 2025-02 (changed for loop variable)  Release 2026-04
```

### LAYOUT PDF PAGE 45

```text
                                    Asynchronous Messaging

An accept action receives           This is the name  This is a declaration of what is being
an incoming asynchronous            of the action.    received, which can be anything.
transfer any kind of values.

            trigger              action takePicture : TakePicture {
    accept scene : Scene            action trigger accept scene : Scene;

                        scene    then action focus : Focus {
                   =
                                    in scene = trigger.scene;
                        scene
                                    out image;
             focus
                                 }
                        image
                        image    flow from focus.image to shoot.image;

            shoot                then action shoot : Shoot {

                        picture     in image;
                   = picture
                                    out picture;      This is an expression that
                                 }                    constructs the value to be sent.

    send Show(picture)              then send new Show(shoot.picture) to screen;
          to screen
                                 }
                                                    The notation “Show(…)” means

    A send action is an             to create an instance of the                  This is also an expression,

    outgoing transfer of values     definition Show with the given                evaluating to the target (in this

    to a specific target.           value for its nested attribute.               case just a feature reference).

45                                  Last changed: 2025-02 (constructor notation)        Release 2026-04
```

### LAYOUT PDF PAGE 46

```text
Asynchronous Messaging through Ports

                            viewPort     part camera : Camera {                 An accept action can be via a specific
                                            port viewPort;                      port, meaning that the transfer is
                  «part»                    port displayPort;                   expected to be received by that port.
                 camera
                 trigger                 action takePicture : TakePicture {
         accept scene : Scene               action trigger accept scene : Scene via viewPort;
              via viewPort
                                            then action focus : Focus {
                              scene            in scene = trigger.scene;
                         =                     out image;

                              scene         }
                                            flow from focus.image to shoot.image;
                  focus                     then action shoot : Shoot {

                              image            in image;
                              image            out picture;
                                            }
                 shoot
                                            then send new Show(shoot.picture) via displayPort;
                              picture
                         =               }

                              picture    }An asynchronous transfer sent via a

          send Show(picture)             port has that port as its source. The         A send action can also be sent via
             via displayPort
                                         target of the transfer is determined          a port, meaning that the transfer
                            displayPort
        «interface»                      by what the port is connected to.             is sent out from that port.

                            displayPort  Last changed: 2025-02 (constructor notation)  Release 2026-04

                  «part»
                  screen

46
```

### LAYOUT PDF PAGE 47

```text
                                   Opaque Actions

                                   action def UpdateSensors {

                                      in sensors : Sensor[*];

                                      language "Alf"

An "opaque" action definition or      /*
usage can be specified using a
textual representation annotation     * for (sensor in sensors) {
in a language other than SysML.
                                      *   if (sensor.ready) {

                                      *      Update(sensor);

                                      *   }

                                      *}

                                      */

                                   }

                                          The textual representation body is written using comment

                                          syntax. The /*, */ and leading * symbols are not included

                                          in the body text. Note that support for referencing SysML

                                          elements from the body text is tool-specific.

 A textual representation annotation can actually be used with any
    kind of element, not just actions. OMG-standard languages a tool
    may support include "OCL" (Object Constraint Language) and
    "Alf" (Action Language for fUML). A tool can also provide support
    for other languages (e.g., "JavaScript" or "Modelica").

47                                 Last changed: 2022-07 (parameter declaration)         Release 2026-04
```

### LAYOUT PDF PAGE 48

```text
                               State Definitions (1)

A state definition is like a state machine in    state def VehicleStates {
UML and SysML v1. It defines a behavioral            first start then off;
state that can be exhibited by a system.
                                                    state off;                           This indicates the the initial
                        «state def»                                                      state after entry is ”off”.
                       VehicleStates

                                                    transition off_to_starting

                                                    first off

                                                    accept VehicleStartSignal

                      «state»                       then starting;
                        off
                                                    state starting;                      A state definition can specify a
                             VehicleStartSignal                                          set of discrete nested states.

                                                    transition starting_to_on

                                                    first starting

                      «state»                       accept VehicleOnSignal
                      starting
                                                    then on;                             States are connected by
                             VehicleOnSignal
                                                    state on;                            transitions that fire on

                                                                                         acceptance of item transfers

                                                    transition on_to_off                 (like accept actions).
                                                        first on

                      «state»                       accept VehicleOffSignal
                        on
    VehicleOffSignal                                then off;

                                                 }

48                             Last changed: 2026-03 (changed “entry” to ”first start”)  Release 2026-04
```

### LAYOUT PDF PAGE 49

```text
                                     State Definitions (2)

                       «state def»
                      VehicleStates

                                                 state def VehicleStates {                     This is a shorthand for a
                                                     first start then off;                     transition whose source is
                                                                                               the lexically previous state.

                      «state»                    state off;
                        off
                                                 accept VehicleStartSignal
                             VehicleStartSignal
                                                 then starting;

                      «state»                    state starting;
                      starting                   accept VehicleOnSignal

                             VehicleOnSignal         then on;

                                                     state on;
                                                     accept VehicleOffSignal

                                                         then off;
                                                 }

    VehicleOffSignal  «state»
                        on

49                                   Last changed: 2026-03 (changed “entry” to ”first start”)  Release 2026-04
```

### LAYOUT PDF PAGE 50

```text
                               State Decomposition

                  «state»                                                                A state can be explicitly
    vehicleStates : VehicleStates                                                        declared to be a usage
                                                                                         of a state definition.
                                                 state def VehicleStates;

                                                 state vehicleStates : VehicleStates {
                                                     first start then off;

                      «state»                    state off;                              A state can also be
                        off                      accept VehicleStartSignal               directly decomposed
                                                                                         into other states.
                             VehicleStartSignal      then starting;

                      «state»                    state starting;
                      starting                   accept VehicleOnSignal

                             VehicleOnSignal         then on;

                      «state»                        state on;
                        on                           accept VehicleOffSignal

                                                         then off;
                                                 }

    VehicleOffSignal

50                             Last changed: 2026-03 (changed “entry” to ”first start”)  Release 2026-04
```

### LAYOUT PDF PAGE 51

```text
                                              Concurrent States

                  «state»                                                                     A parallel state is one whose
    vehicleStates : VehicleStates                                                             nested states are concurrent.

                 «parallel»                      state def VehicleStates;

                  «state»                        state vehicleStates : VehicleStates parallel {
           operationalStates

                                                    state operationalStates {
                                                        first start then off;

                      «state»                          state off;
                        off                            accept VehicleStartSignal

                             VehicleStartSignal            then starting;

                      «state»                          state starting;
                      starting                         accept VehicleOnSignal

                             VehicleOnSignal               then on;

                                                       state on;

                                                       accept VehicleOffSignal

                                                          then off;

                                                    }                                         ! Transitions are not allowed

                      «state»                       state healthStates {                      between concurrent states.
                        on
    VehicleOffSignal                                   …

                         «state»                    }
                      healthStates
                                                 }

51                                  Last changed: 2026-03 (changed “entry” to ”first start”)  Release 2026-04
```

### LAYOUT PDF PAGE 52

```text
                  State Entry, Do and Exit Actions

                  «state»                                                                            States, like actions,
    vehicleStates : VehicleStates                                                                    can have parameters.

                                            action performSelfTest{in vehicle : Vehicle;}

                      parameters            state def VehicleStates{in operatingVehicle : Vehicle;}
^in operatingVehicle : Vehicle

                                            state vehicleStates : VehicleStates {
                                                in operatingVehicle : Vehicle;

VehicleOffSignal  «state»                      first start then off;  An entry action is performed
                     off
                                               state off;                                   on entry to a state, a do
                        VehicleStartSignal
                                               accept VehicleStartSignal action while in it, and an exit
                                                                                            action on exit from it.
                                                  then starting;

                                               state starting;

                  «state»                      accept VehicleOnSignal                       A state entry, do or exit
                  starting
                                                  then on;                                  can reference an action
                           VehicleOnSignal
                                               state on {                                   defined elsewhere…
                  «state»
                     on                           entry performSelfTest

    entry performSelfTest                         { in vehicle = operatingVehicle; }
    do action providePower
    exit action applyParkingBrake                 do action providePower { … }

                                                  exit action applyParkingBrake { … }

                                               }

                                               accept VehicleOffSignal

                                                  then off;                                 … or the action can be

                                            }                                               defined within the state.

52                                Last changed: 2026-03 (changed “entry” to ”first start”)  Release 2026-04
```

### LAYOUT PDF PAGE 53

```text
                  Transition Guards and Effect Actions

                         «state»                       action performSelfTest{in vehicle : Vehicle;}
           vehicleStates : VehicleStates
                                                       state def VehicleStates {
                      parameters                           in operatingVehicle : Vehicle;
^in operatingVehicle : Vehicle                             in controller : VehicleController; }
^in controller: VehicleController

                                                       state vehicleStates : VehicleStates {

                                                       in operatingVehicle : Vehicle;

                                                       in controller : VehicleController;A guard is a condition

                  «state»                              first start then off;           that must be true for a
                     off                                                               transition to fire.

                         VehicleStartSignal            state off;
                         [brakePedalDepressed]/        accept VehicleStartSignal
                         send ControllerStartSignal()
                                                           if operatingVehicle.brakePedalDepressed
                  «state»                                  do send new ControllerStartSignal() to controller
                  starting                                 then starting;

                        VehicleOnSignal                    state starting;           An effect action is performed
                                                           accept VehicleOnSignal    when a transition fires, before
                                                                                     entry to the target state.
                                                               then on;
VehicleOffSignal  «state»
                    on                                     state on { … }
                                                           accept VehicleOffSignal

                                                               then off;
                                                       }

53                         Last changed: 2026-03 (changed “entry” to ”first start”)              Release 2026-04
```

### LAYOUT PDF PAGE 54

```text
                                   Change and Time Triggers

                   «state»         action senseTemperature { out temp : TemperatureValue; }
                healthStates
                                   state healthStates {                                      An absolute time
                 parameters
^in operatingVehicle : Vehicle     in vehicle : Vehicle;                                     trigger fires at a
^in controller: VehicleController
                                   in controller : VehicleControllerg;iven instant of time.
                                   do senseTemperature;

                   actions         first start then normal;                                  A change trigger fires
do senseTemperature(out temp)
                                                                                             when a given Boolean
when
senseTemperature.temp >            state normal;                                             expression becomes true.
vehicle.maxTemperature             accept at vehicle.maintenanceTime

                          normal   then maintenance;

                                   accept when senseTemperature.temp > vehicle.maxTemperature

                                   do send new OverTemp() to controller

                                   then degraded;            ! Time instant quantities are defined in the

    at vehicle.      after 48[h]   state maintenance {       Time package, not the ISQ package.
    maintenanceTime
                                   entry assign vehicle.maintenanceTime :=

                                   vehicle.maintenanceTime + vehicle.maintenanceInterval;

    maintenance                    }                         A relative time trigger
                                   accept after 48 [h]       fires after a given

                                       then normal;

when                                                         time duration.
senseTemperature.temp <=
vehicle.maxTemperature             state degraded;

                      degraded     accept when senseTemperature.temp <= vehicle.maxTemperature

                                           then normal;       Change and time triggers can
                                   }

                                                                                             also be used in accept actions.

54                                 Last changed: 2026-03 (changed “entry” to ”first start”)                      Release 2026-04
```

### LAYOUT PDF PAGE 55

```text
                                Local Clocks

Redefining the localClock       part def Server {
feature of a part provides a
local time reference for        part :>> localClock = new Time::Clock();
composite items, parts and
actions nested within it.       attribute today : String;

 A localClock can also be      port requestPort;                             Each Server instance
    declared for an item or an                                                will have its own
    action (or any kind of
    occurrence that happens     state ServerBehavior {                        independent Clock.
    over time).                     first start then off;

   All absolute and relative    state off;                                     If no localClock is declared,
   time references are          accept Start via requestPort                      the default is a universalClock
   relative to the localClock.                                                    that provides a common time
                                    then waiting;                                 universal reference.
 55
                                state waiting;
                                accept request : Request via requestPort

                                    then responding;
                                accept at new Time::Iso8601DateTime(today + "11:59:00")

                                    then off;

                                        state responding;
                                        accept after 5 [SI::min]

                                             then waiting;
                                    }
                                }

                                Last changed: 2025-02 (constructor notation)  Release 2026-04
```

### LAYOUT PDF PAGE 56

```text
                                       Exhibited States

                                    part vehicle : Vehicle {

    exhibit identifies the part        part vehicleController : VehicleController;
    that is exhibiting states that
    are defined elsewhere.             exhibit vehicleStates {
                                          in operatingVehicle = vehicle;
                                          in controller = vehicleController;

                                       }

                                    }                   Parameters for a state usage can

                                                        be bound in the same way as

                                                        parameters of an action usage.

    ! Like performed actions, exhibited states are
      not composite features, therefore, a localClock
      on a part will not apply to performed actions or
      exhibited states of the part.

56                                  Last changed: 2022-07 (localClock warning)            Release 2026-04
```

### LAYOUT PDF PAGE 57

```text
Occurrences, Time Slices and Snapshots (1)

                              An occurrence is something that happens over time.
                                 Items and parts are structural occurrences. Actions are
                                 behavioral occurrences. Attributes are not occurrences.

                             attribute def Date;

A time slice represents a    item def Person;                        A succession asserts that the
portion of the lifetime of                                           first occurrence ends before
an occurrence over some      part def Vehicle {                      the second can begin.
period of time.                 timeslice assembly;

A snapshot represents an        first assembly then delivery;
occurrence at a specific
point in time (a time slice     snapshot delivery;
with zero duration).
                                first delivery then ownership;
57
                                timeslice ownership[0..*] ordered;

                                snapshot junked = done;              done is the name of the
                                                                     end-of-life snapshot of
                             }   Timeslices and snapshots           any occurrence.

                                are suboccurrences.

                                Last changed: 2021-10 (successions)                       Release 2026-04
```

### LAYOUT PDF PAGE 58

```text
    Occurrences, Time Slices and Snapshots (2)

                              part def Vehicle {
                                 …

      This is a shorthand     snapshot delivery {
      for a succession after     attribute deliveryDate : Date;
      the lexically previous
      occurrence.             }

Time slices and snapshots     then timeslice ownership[0..*] ordered {
can have nested time
slices, snapshots and            snapshot sale = start;
other features applicable                                                                  start is the name of the
during their occurrence.
                              ref item owner : Person[1];        start-of-life snapshot of
                                                                 any occurrence.

                              timeslice driven[0..*] {
                                 ref item driver : Person[1];

                              }

                                 }                            One occurrence references
                                                              another during the same
                                 snapshot junked = done;      time period in the other
                              }                               reference’s lifetime.

58                               Last changed: 2021-05 (new)     Release 2026-04
```

### LAYOUT PDF PAGE 59

```text
                                         Event Occurrences

    An event occurrence is a             part driver : Driver {
    reference to something that             event occurrence setSpeedSent;
    happens during the lifetime
    of another occurrence.               }

                  Event occurrences can  part vehicle : Vehicle {
                  be sequenced as usual     part cruiseController : CruiseController {
                  using succession.             event occurrence setSpeedReceived;
                                                then event occurrence sensedSpeedReceived;
                                                then event occurrence fuelCommandSent;
                                            }

                                            part speedometer : Speedometer {
                                                event occurrence sensedSpeedSent;

                                            }

                                            part engine : Engine {
                                                event occurrence fuelCommandReceived;

                                            }
                                         }

59                                       Last changed: 2021-05 (new)  Release 2026-04
```

### LAYOUT PDF PAGE 60

```text
                                   Messages (1)

An occurrence definition defines   occurrence def CruiseControlInteraction {
a class of occurrences, without       ref part :>> driver;
committing to whether they are        ref part :>> vehicle;
structural or behavioral.
                                      message setSpeedMessage of SetSpeed
 A message asserts that there is          from driver.setSpeedSent
 a transfer of some payload of a          to vehicle.cruiseController.setSpeedReceived;
 certain type from one
 occurrence to another                message sensedSpeedMessage of SensedSpeed
 (specifying the payload type is          from vehicle.speedometer.sensedSpeedSent
 optional).                               to vehicle.cruiseController.sensedSpeedReceived;

Messages can be explicitly            message fuelCommandMessage of FuelCommand
ordered. Otherwise, they are              from vehicle.cruiseController.fuelCommandSent
only partially ordered by the             to vehicle.engine.fuelCommandReceived;
time-ordering of their respective
source and target events.             first setSpeedMessage then sensedSpeedMessage;
                                   }

60                                 Last changed: 2022-09 (source and target events)  Release 2026-04
```

### LAYOUT PDF PAGE 61

```text
                                Messages (2)

An event can also be specified  occurrence def CruiseControlInteraction {
by reference to an identified      ref part driver : Driver {
occurrence (such as the source         event setSpeedMessage.sourceEvent;
or target of a message).           }

Each message has a                 ref part vehicle : Vehicle {
sourceEvent and                        part cruiseController : CruiseController {
targetEvent, even if it is                 event setSpeedMessage.targetEvent;
not explicitly identified in               then event sensedSpeedMessage.targetEvent;
the message declaration.                   then event fuelCommandMessage.sourceEvent;
                                       }
                                       part speedometer : Speedometer {
                                           event sensedSpeedMessage.sourceEvent;
                                       }
                                       part engine : Engine {
                                           event fuelCommandMessage.targetEvent;
                                       }

                                   }

                                   message setSpeedMessage of SetSpeed;
                                   then message sensedSpeedMessage of SensedSpeed;
                                   message fuelCommandMessage of FuelCommand;
                                }

61                              Last changed: 2022-09 (sourceEvent and targetEvent)  Release 2026-04
```

### LAYOUT PDF PAGE 62

```text
                                        Interactions

                               Event occurrences and messages can be used
                                  together to specify an interaction between parts
                                  without committing to how the interaction happens.

    ! Sequence diagram                                            «occurrence def»
       graphical notation is                                  CruiseControlInteraction
       purely illustrative.
                                                                                               «part»
                                                                                              vehicle

    «part»                         «part»                                           «part»                  «part»
    driver                    cruiseController                                  speedometer                 engine

event occurrence     message setSpeedMessage                  event occurrence                 Succession must be
       setSpeedSent            of SetSpeed                    setSpeedReceived                 specified explicitly for
                                                                                               events in different lifelines.
    Succession is implicit between
    events on a single lifeline.                                                then

                                            event occurrence  message sensedSpeedMessage  event occurrence
                                      sensedSpeedReceived               of SensedSpeed    sensedSpeedSent

                     event occurrence                         message fuelCommandMessage                    event occurrence
                      fuelCommandSent                                   of FuelCommand                      fuelCommandReceived

62                            Last changed: 2023-10 (names not bold)                                        Release 2026-04
```

### LAYOUT PDF PAGE 63

```text
    Interaction Realization by Actions (1)

                           part driver_a : Driver {                An interaction can be realized by many
                               perform action driverBehavior {        different models. A valid realization
                                   send SetSpeed() to vehicle_a;      must have suboccurrences that can be
                               }                                      identified with all the events and
                                                                      messages in the interaction.
                           }
In this model, event
occurrences are            part vehicle_a : Vehicle {
realized by nested send        part cruiseController_a : CruiseController {
and accept actions.                perform action controllerBehavior {
                                        accept SetSpeed via vehicle_a;
                                        then accept SensedSpeed via cruiseController_a;
                                        then send new FuelCommand() to engine_a;
                                   }
                               }

                              part speedometer_a : Speedometer {

Messages are realized            perform action speedometerBehavior {
by the implicit transfers
between send actions                send new SensedSpeed() to cruiseController_a;
and corresponding
accept actions.                  }

                              }

                              part engine_a : Engine {                   In more realistic cases, a
                                  perform action engineBehavior {           realizing model will have more
                                      accept FuelCommand via engine_a;      extensive behavior, only a
                                  }                                         subset of which will conform
                                                                            to any one interaction model.
                              }

                           }

63                                  Last changed: 2021-10 (accept via)                   Release 2026-04
```

### LAYOUT PDF PAGE 64

```text
                 Interaction Realization by Actions (2)

                                                      «occurrence»
                              cruiseControlInteraction_a : CruiseControlInteraction

                                                       «part»
                                                      vehicle_a

          «part»                  «part»                        «part»                     «part»
        :>> driver        :>> cruiseController           :>> speedometer                 :>> engine
      :>> driver_a      :>> cruiseController_a          :>> speedometer_a              :>> engine_a

          perform                  perform                      perform                    perform
    driverBehavior  cruiseControllerBehavior          speedometerBehavior            engineBehavior

                    SetSpeed

send setSpeed()                      accept setSpeed                                 This succession from the
                                                                                     interaction may not actually
                                                      then                           be satisfied by the realization.

                 accept SensedSpeed  SensedSpeed            send SensedSpeed()

                                     FuelCommand                                     accept
                                                                                     FuelCommand
                 send FuelCommand()

64                            Last changed: 2023-10 (names not bold)                 Release 2026-04
```

### LAYOUT PDF PAGE 65

```text
Interaction Realization by Flows (1)

                          part driver_b : Driver {              Ports are also suboccurrences
                              port setSpeedPort {

                                  out setSpeed : SetSpeed;         of the parts that contain them.
                             }
In this model, event
occurrences are realized  }
by values leaving from
and arriving at ports.    interface driver_b.setSpeedPort to vehicle_b.setSpeedPort {

Messages are realized by     flow of SetSpeed from driver_b.setSpeedPort.setSpeed
explicit flows between
features of ports.              to vehicle_b.setSpeedPort.setSpeed;

 65                       }

                          part vehicle_b : Vehicle {

                             port setSpeedPort {

                                in setSpeed : SetSpeed;

                             }

                             part cruiseController_b : CruiseController {

                                port setSpeedPort {

                                   in setSpeed : SetSpeed = vehicle_b.setSpeedPort.setSpeed;

                                }

                                port sensedSpeedPort {

                                   in sensedSpeed : SetSpeed;

                                }

                                …

                             }

                             flow of SensedSpeed from speedometer_b.sensedSpeedPort.sensedSpeed

                                to cruiseController_b.sensedSpeedPort.sensedSpeed;

                             part speedometer_b : Speedometer {

                                port sensedSpeedPort {

                                   out sensedSpeed : SensedSpeed;

                                }

                             }

                          …

                                   Last changed: 2025-02 (constructor notation)                 Release 2026-04
```

### LAYOUT PDF PAGE 66

```text
                       Interaction Realization by Flows (2)

                                               «occurrence»
                       cruiseControlInteraction_b : CruiseControlInteraction

                                                                         «part»
                                                                       vehicle_b

    «part»                           «part»                                    «part»                  «part»
                                                                                                    :>> engine
    :>> driver         :>> cruiseController                 :>> speedometer                        :>> engine_b

    :>> driver_b       :>> cruiseController_b               :>> speedometer_b                            port
                                                                                                fuelCommandPort
    port               port                           port                     port
                                                                                                               in
    setSpeedPort       setSpeedPort  port             fuelCommandPort          sensedSpeedPort                 FuelCommand

                                     sensedSpeedPort        This is a snapshot of

                  flow of SetSpeed                          when the setSpeed is
                                                            received into the port.
    out setSpeed                     in setSpeed

This is a snapshot of    in SensedSpeed                                  then  out SensedSpeed
when the setSpeed is   out FuelCommand       flow of SensedSpeed
sent out of the port.
                                             flow of FuelCommand

66                                   Last changed: 2023-10 (names not bold)                     Release 2026-04
```

### LAYOUT PDF PAGE 67

```text
    Message Payloads

                                                                           The default name for a

    message setSpeedMessage of SetSpeed                                   message payload is payload.

    from driver.setSpeedSent

    to vehicle.cruiseController.setSpeedReceived; The payload of a message

    then message sensedSpeedMessage of SensedSpeed                        can be declared with a
       from vehicle.speedometer.sensedSpeedSent                           name for reference.

    to vehicle.cruiseController.sensedSpeedReceived;

    then message fuelCommandMessage of fuelCommand : FuelCommand
       from vehicle.cruiseController.fuelCommandSent
       to vehicle.engineController.fuelCommandReceived;

    then message fuelCommandForwardingMessage
       of fuelCommand : FuelCommand = fuelCommandMessage.fuelCommand
       from vehicle.engineController.fuelCommandForwarded
       to vehicle.engine.fuelCommandReceived;

    ! Note that a payload declaration        The payload of a message can also be bound to
       without a colon names the type of     a specific value. In this case, the
       the payload, not the payload itself.  fuelCommandMessage payload is forwarded by
                                             the engineController to the engine.

67                                           Last changed: 2022-10 (new)                            Release 2026-04
```

### LAYOUT PDF PAGE 68

```text
                         Individuals and Snapshots (1)

                               An individual definition is an                   An individual definition will
                               occurrence definition (of any kind)              often specialize a definition of
                               restricted to model a single individual          the general class of things the
                               and how it changes over its lifetime.            individual is one of.

As occurrences,          individual part def Vehicle_1 :> Vehicle {
individuals can have
snapshots that              snapshot part vehicle_1_t0 : Vehicle_1 {
describe them at a
single instant of time.        :>> mass = 2000.0;

This is a compact              :>> status {
notation for showing
redefinition of an                :>> gearSetting = 0;
attribute usage.
                                  :>> acceleratorPosition = 0.0;

                               }

                            }                                                   An attribute does not have

                         }                                                      snapshots, but it can be

                                                                                asserted to have a specific

                                                                                value in a certain snapshot.

68                             Last changed: 2024-02 (removed PhysicalContext)  Release 2026-04
```

### LAYOUT PDF PAGE 69

```text
    Individuals and Snapshots (2)

    individual part def Vehicle_1 :> Vehicle {

                                  snapshot part vehicle_1_t0 : Vehicle_1 {
                                     :>> mass = 2000.0;
                                     :>> status {
                                         :>> gearSetting = 0;
                                         :>> acceleratorPosition = 0.0;
                                     }

                                  }

                                  snapshot part vehicle_1_t1 : Vehicle_1 {

    As usual, succession asserts     :>> mass = 1500.0;                              The values of the attributes
    that the first snapshot          :>> status {                                    of an individual can change
    occurs before the second in                                                      over time.
    time, in some context.               :>> gearSetting = 2;
                                         :>> acceleratorPosition = 0.5;

                                     }

                                  }

       first vehicle_1_t0 then vehicle_1_t1;
    }

69                                      Last changed: 2021-05 (occurrence modeling)  Release 2026-04
```

### LAYOUT PDF PAGE 70

```text
                              Individuals and Roles

                        individual part def Vehicle_1 :> Vehicle {
                           part leftFrontWheel : Wheel;
                           part rightFrontWheel : Wheel;

                        }

                        individual part def Wheel_1 :> Wheel;            During the first snapshot of
                        individual part vehicle_1 : Vehicle_1 {          vehicle_1, Wheel_1 has the
                                                                         role of the leftFrontWheel.

An individual usage        snapshot part vehicle_1_t0 {
                              snapshot leftFrontWheel_t0 : Wheel_1 :>> leftFrontWheel;

represents an              }

individual during some

portion of its lifetime. then snapshot part vehicle_1_t1 {

                              snapshot rightFrontWheel_t1 : Wheel_1 :>> rightFrontWheel;

                           }

                        }

                                                                         During a later snapshot, the
                                                                         same Wheel_1 has the role
                                                                         of the rightFrontWheel.

70                            Last changed: 2024-02 (revised call-outs)  Release 2026-04
```

### LAYOUT PDF PAGE 71

```text
                            Individuals and Time Slices

A time slice represents     individual item def Alice :> Person;
an individual over          individual item def Bob :> Person;
some period of time
(that this is a time slice                                                        During this time slice of
of a part is implicit).
                            individual part : Vehicle_1 {                         Vehicle_1, the Alice has
start and done are                                                                the role of the driver.
snapshots at the
beginning and end of           timeslice aliceDriving {
the time slice.
                                  ref individual item :>> driver : Alice;
Succession asserts that
the first time slice must         snapshot :>> start {
complete before the                   :>> mass = 2000.0;
second can begin.
                                  }

                                  snapshot :>> done {

                                     :>> mass = 1500.0;

                                  }                                               During a later time slice

                               }                                                  of Vehicle_1, Bob has the

                                                                                  role of the driver.

                               then timeslice bobDriving {

                                  ref individual item :>> driver : Bob;

                               }

                            }

71                                   Last changed: 2021-05 (occurrence modeling)  Release 2026-04
```

### LAYOUT PDF PAGE 72

```text
          Expressions and Feature Values

    package MassRollup1 {                        ISQ::mass is a standard quantity
       private import ScalarFunctions::*;        kind from the International System
       part def MassedThing {                    of Quantities library model.

          attribute simpleMass :> ISQ::mass;

          attribute totalMass :> ISQ::mass;      A feature value is a shorthand for binding

       }                                         a feature to the result of an expression

                                                 (here simply the value of another

       part simpleThing : MassedThing {          feature).

          attribute :>> totalMass = simpleMass;

       }

       part compositeThing : MassedThing {

          part subcomponents: MassedThing[*];

          attribute :>> totalMass =
             simpleMass + sum(subcomponents.totalMass);

       }

    }

          An expression in general is a          The dot notation can be used as an expression to read

          computation expressed using a typical  the values of a feature. Here, the totalMass is
          mathematical operator notation.        collected for each of the subcomponents.

72        Last changed: 2024-07 (import visibility)         Release 2026-04
```

### LAYOUT PDF PAGE 73

```text
           Car Mass Rollup Example (1)

    private import ScalarValues::*;
    private import MassRollup1::*;

    part def CarPart :> MassedThing {

       attribute serialNumber : String;

    }

    part car: CarPart :> compositeThing {

       attribute vin :>> serialNumber;

       part carParts : CarPart[*] :>> subcomponents;

       part engine :> simpleThing, carParts { … }

       part transmission :> simpleThing, carParts { … }

    }

                                                                       This is an expression for a quantity

    // Example usage                            with a specific numeric value and
    private import SI::kg;                      unit. Note that units are identified
    part c :> car {                             on the quantity value, not the type.

       attribute :>> simpleMass = 1000[kg];

       part :>> engine {

           attribute :>> simpleMass = 100[kg];

       }

       part attribute transmission {

           attribute :>> simpleMass = 50[kg];

        }                                  The totalMass of c can be computed
    }
                                           using the feature value expressions from

    // c.totalMass --> 1150.0[kg]          simpleThing and compositeThing.

73         Last changed: 2024-11 (import visibility)     Release 2026-04
```

### LAYOUT PDF PAGE 74

```text
                                          Default Values

    package MassRollup2 {                      A default value is feature value that

       private import ScalarFunctions::*;      applies unless explicitly overridden.
       part def MassedThing {

          attribute simpleMass :> ISQ::mass;

          attribute totalMass :> ISQ::mass default simpleMass;

       }                                       A default value can be overridden

       part compositeThing : MassedThing {     when the feature is redefined,
          part subcomponents: MassedThing[*];  with a default or bound value.

          attribute :>> totalMass default mass + sum(subcomponents.totalMass);

       }

                                           Once bound, the value of the

       part filteredMassThing :> compositefeTahtiurnegis {fixed as the result of the

          attribute minMass : ISQ::mass value expression.

          attribute :>> totalMass =

          sum(subcomponents.totalMass.?{in p:>ISQ::mass; p >= minMass)});

       }

    }     A dot can be followed by a

          select expression in order to

          filter a collection of values.

74                         Last changed: 2024-07 (import visibility)                  Release 2026-04
```

### LAYOUT PDF PAGE 75

```text
           Car Mass Rollup Example (2)

    private alarValues::*;              The default of totalMass to
    private import MassRollup2::*;      simpleMass is inherited.

    part def CarPart :> MassedThing {                           The default for totalMass is overridden
        attribute serialNumber : String;                        as specified in compositeThing.

    }

    part car: CarPart :> compositeThing {

       attribute vin :>> serialNumber;

       part carParts : CarPart[*] :>> subcomponents;

       part engine :> carParts { … }

       part transmission :> carParts { … }

    }

    // Example usage                  The totalMass default is not
    private import SI::kg;            overridden for the nested carParts.

    part c :> car {

       attribute :>> simpleMass = 1000[kg];

       part :>> engine {

           attribute :>> simpleMass = 100[kg];

       }

       part attribute transmission {

           attribute :>> simpleMass = 50[kg];

        }                                   When computing the totalMass
    }
                                            of c, c.engine and c.transmission,

    // c.totalMass --> 1150.0[kg]           the relevant defaults are used.

75                   Last changed: 2024-11 (import visibility)               Release 2026-04
```

### LAYOUT PDF PAGE 76

```text
               Calculation Definitions

    A calculation definition is a reusable,
    parameterized expression.

calc def Power {                      Similarly to actions, the directed features
    in whlpwr : PowerValue;           of a calculation are its parameters.
    in Cd : Real;
    in Cf : Real;             A calculation has a
    in tm : MassValue;        single return result.
    in v : SpeedValue;
    return : PowerValue;

    attribute drag = Cd * v;  The calculation can include the

    attribute friction = Cf * tm * vc;omputation of intermediate values.           ! There is no semicolon
                                                                                      at the end of a result
    whlpwr - drag - friction  The calculation result expression must                  expression.
}                             conform to the return type.

calc def Acceleration { in tp: PowerValue; in tm : MassValue; in v: SpeedValue;

    return : AccelerationValue = tp / (tm * v);  The result expression can also be bound
}                                                directly to the return parameter.

calc def Velocity { in dt : TimeValue; in v0 : SpeedValue; in a : AccelValue;
    return : SpeedValue = v0 + a * dt;

}

calc def Position (dt : TimeValue; x0 : LengthValue; v : SpeedValue;
    return : LengthValue = x0 + v * dt;

}

76                            Last changed: 2022-07 (parameter declaration)        Release 2026-04
```

### LAYOUT PDF PAGE 77

```text
                                  Calculation Usages (1)

                                  part def VehicleDynamics {
                                      attribute C_d : Real;
                                      attribute C_f : Real;
                                      attribute wheelPower : PowerValue;
                                      attribute mass : MassValue;

Values are bound to the           action straightLineDynamics { in delta_t : TimeValue;
parameters of calculation usages       in v_in : SpeedValue; in x_in : LengthValue;
(similar to action parameters).
                                         calc acc : Acceleration {

                                            in tp = Power(wheelPower, C_d, C_f, mass, v_in);

                                            in tm = mass;

                                             in v = v_in;           A calculation definition can also be
                                             return a;              invoked as an expression, with input
                                         }                          values given as arguments, evaluating
                                         calc vel : Velocity {

                                            in dt = delta_t;        to the result of the calculation.
                                            in v0 = v_in;

                                            in a = acc.a;

                                            return v;

                                         }

                                         calc pos : Position {      Calculation results can be
                                             in dt = delta_t;       referenced by name (they are
                                             in x0 = x_in;          output parameters).
                                              in v = vel.v;

                                            return x;

                                         }

                                         out v_out : SpeedValue = vel.v;
                                         out x_out : LengthValue = pos.x;

                                      }
                                  }

77                                          Last changed: 2023-10 (output binding)                Release 2026-04
```

### LAYOUT PDF PAGE 78

```text
                               Calculation Usages (2)

attribute def DynamicState {
    attribute v: SpeedValue;
    attribute x: LengthValue;

}

part def VehicleDynamics {

    attribute C_d : Real;

    attribute C_f : Real;

    attribute wheelPower : PowerValue;

    attribute mass : MassValuAe;calculation can be

                            specified without an explicit  Calculations can also
                            calculation definition.        handle structured values.

    calc updateState {

       in delta_t : TimeValue; in currState : DynamicState;

       attribute totalPower : PowerValue =                   This is a declaration of the result

          Power(wheelPower, C_d, C_f, mass, currState.v); parameter of the calculation, with

                                                             bound subattributes.

       return attribute newState : DynamicState {

          :>> v = Velocity(delta_t, currState.v, Acceleration(totalPower, mass, currState.v));

          :>> x = Position(delta_t, currState.x, currState.v);

       }

    }

}

78                             Last changed: 2022-07 (parameter declaration)          Release 2026-04
```

### LAYOUT PDF PAGE 79

```text
                                Constraint Definitions (1)

                             private import ISQ::*;  A constraint definition is a reusable,
                             private import SI::*;   parameterized Boolean expression.

                             private import ScalarFunctions::*;

                             constraint def MassConstraint {                  Constraint parameters are always
                                 in partMasses : MassValue[0..*];             in parameters.
                                 in massLimit : MassValue;
! There is no semicolon

    at the end of a             sum(partMasses) <= massLimit                  The constraint expression can be
                                                                              any Boolean expression using
    constraint expression. }                                                  the constraint parameters.

                             part def Vehicle {

                                constraint massConstraint : MassConstraint {
                                    in partMasses = (chassisMass, engine.mass, transmission.mass);
                                    in massLimit = 2500[kg];

A constraint is the usage       }                                             Values are bound to
of a constraint definition,                                                   constraint parameters
which may be true or            attribute chassisMass : MassValue;            (similarly to actions).
false in a given context.
                                part engine : Engine {
 A constraint may be               attribute mass : MassValue;

                                }

    violated (false) without part transmission : Transmission {

    making the model               attribute mass : MassValue;

    inconsistent.               }

                             }

79                                 Last changed: 2024-07 (import visibility)  Release 2026-04
```

### LAYOUT PDF PAGE 80

```text
    Constraint Definitions (2)

    private import ISQ::*;                       Alternatively, constraint
    private import SI::*;                        parameters may be modeled as
    private import ScalarFunctions::*;           attribute or reference features.

    constraint def MassConstraint {
        attribute partMasses : MassValue[0..*];
        attribute massLimit : MassValue;

        sum(partMasses) <= massLimit
    }

    part def Vehicle {
        constraint massConstraint : MassConstraint {
            redefines partMasses = (chassisMass, engine.mass, transmission.mass);
            redefines massLimit = 2500[kg];
        }

    attribute chassisMass : MassValue;   The constraint parameter
                                         properties are then redefined
    part engine : Engine {               in order to be bound.
        attribute mass : MassValue;

    }

        part transmission : Engine {
            attribute mass : MassValue;

        }
    }

80  Last changed: 2024-07 (import visibility)                           Release 2026-04
```

### LAYOUT PDF PAGE 81

```text
                            Constraint Assertions (1)

                            private import ISQ::*;
                            private import SI::*;
                            private import ScalarFunctions::*;

                            constraint def MassConstraint {
                                in partMasses : MassValue[0..*];
                                in massLimit : MassValue;

                                sum(partMasses) <= massLimit
                            }

A constraint assertion      part def Vehicle {
asserts that a constraint       assert constraint massConstraint : MassConstraint {
must be true.                       in partMasses = (chassisMass, engine.mass, transmission.mass);
                                    in massLimit = 2500[kg];
 If an assertion is            }
    violated, then the
    model is inconsistent.      attribute chassisMass : MassValue;

                                part engine : Engine {
                                    attribute mass : MassValue;

                                }

                                part transmission : Engine {
                                    attribute mass : MassValue;

                                }
                            }

81                          Last changed: 2024-07 (import visibility)  Release 2026-04
```

### LAYOUT PDF PAGE 82

```text
                               Constraint Assertions (2)

The constraint expression   constraint def MassConstraint {
can also be defined on a
usage of a constraint def.     in partMasses : MassValue[0..*];

                               in massLimit : MassValue;

                            }

                            constraint massConstraint : MassConstraint {

                               sum(partMasses) <= massLimit  A named constraint

                            }

                                                             can be asserted in

                            part def Vehicle {               multiple contexts.

                               assert massConstraint {

                                  in partMasses = (chassisMass, engine.mass, transmission.mass);

                                  in massLimit = 2500[kg];

                               }

                               attribute chassisMass : MassValue;

                               attribute engine : Engine {
                                   value mass : MassValue;

                               }

                                attribute transmission : Engine {
                                    value mass : MassValue;

                                }
                            }

82                             Last changed: 2023-12 (updated constraint def and usage)  Release 2026-04
```

### LAYOUT PDF PAGE 83

```text
       Derivation Constraints

                                       In UML and SysML v1, constraints are

                                       often used to define derived values.

    part vehicle1 : Vehicle {

       attribute totalMass : MassValue;

       assert constraint {totalMass == chassisMass + engine.mass + transmission.mass}

    }

    part vehicle2 : Vehicle {

       attribute totalMass : MassValue = chassisMass + engine.mass + transmission.mass;

    }

    constraint def AveragedDynamics {    In SysML v2 this can usually be
        in mass: MassValue;              done more directly using a binding.

       in initialSpeed : SpeedValue;

       in finalSpeed : SpeedValue;                                            ! Be careful about the
       in deltaT : TimeValue;                                                     difference between ==,
       in force : ForceValue;

                                                                              which is the Boolean-valued

       force * deltaT == mass * (finalSpeed - initialSpeed) and               equality operator, and =,
       mass > 0[kg]                                                           which denotes binding.

    }                          However, constraints

                               allow for more general

                               equalities and inequalities

                               than direct derivation.

83                             Last changed: 2022-07 (parameter declaration)  Release 2026-04
```

### LAYOUT PDF PAGE 84

```text
                      Analytical Constraints

constraint def StraightLineDynamicsEquations {                       This constraint definition
    in p : PowerValue, in m : MassValue, in dt : TimeValue;          provides a reusable
    in x_i : LengthValue; in v_i : SpeedValue;                       specification of a system
    in x_f : LengthValue; in v_f : SpeedValue,                       of (coupled) equations.
    in a : AccelerationValue;

    attribute v_avg : SpeedValue = (v_i + v_f)/2;

    a == Acceleration(p, m, v_avg) and   Note the use of the        An action definition is inherently
    v_f == Velocity(dt, v_i, a) and         calculation definitions  "causal" in the sense that outputs
    x_f == Position(dt, x_i, v_avg)         defined earlier.         are determined in terms of inputs.
}

action def StraightLineDynamics {

    in power : PowerValue; in mass : MassValue; in delta_t : TimeValue;

    in x_in : LengthValue; in v_in : SpeedValue;                               A constraint is inherently
    out x_out : LengthValue; out v_out : SpeedValue;                           "acausal" – it is simply true
    out a_out : AccelerationValue;                                             or false for given values of

    assert constraint dynamics : StraightLineDynamicsEquations {               its parameters.

       in p = power; in m = mass; in dt = delta_t;

       in x_i = x_in; in v_i = v_in;

       in x_f = x_out; in v_f = v_out;  This specifies that the action outputs

       in a = a_out;                    must be solved for analytically given

    }                                   the action inputs, consistent with

}                                       the asserted constraint.

84                    Last changed: 2022-07 (parameter declaration)              Release 2026-04
```

### LAYOUT PDF PAGE 85

```text
       Time Constraints

    state healthStates {        TimeOf and DurationOf are from
        in vehicle : Vehicle;      the Time package in the Quantities
                                   and Units Domain Library.

       entry; then normal;                TimeOf returns the time of the
                                          start of an occurrence (in this
       state normal;                      example, a state performance).
       accept at vehicle.maintenanceTime

           then maintenance;

        state maintenance {
            assert constraint { TimeOf(maintenance) > vehicle.maintenanceTime }
            assert constraint { TimeOf(maintenance) - TimeOf(normal.done) < 2 [s]

    }
            entry assign vehicle.maintenanceTime :=
                 vehicle.maintenanceTime + vehicle.maintenanceInterval;

        }
        accept MaintenanceDone

            then normal;

       constraint { DurationOf(maintenance) <= 48 [h] }

    }                          DurationOf returns the time duration

                               of an occurrence (the different

                               between its start and done times).

85                             Last changed: 2022-01 (new)                 Release 2026-04
```

### LAYOUT PDF PAGE 86

```text
                                   Requirement Definitions (1)

    A requirement definition is a special                         A textual statement of the requirement can
    kind of constraint definition.                                be given as a documentation comment in
                                                                  the requirement definition body.

    Like a constraint definition,  requirement def MassLimitationRequirement {
    a requirement definition           doc /* The actual mass shall be less than or equal
    can be parameterized                 * to the required mass. */
    using features.
                                       attribute massActual : MassValue;
                                       attribute massReqd : MassValue;

                                       require constraint { massActual <= massReqd }
                                   }

                                                                                                The requirement can be
                                                                                                formalized by giving one or
                                                                                                more component required
                                                                                                constraints.

86                                         Last changed: 2020-08  Release 2026-04
```

### LAYOUT PDF PAGE 87

```text
                    Requirement Definitions (2)

part def Vehicle {

    attribute dryMass: MassValue;

    attribute  ffuueellFMuaslsl:MaMsass:sVMaalsAusVera;elquueir;ement definition may have   Actually, any identifiable
    attribute                   a modeler specified short name,                                element can have a short
                                                                                               name, not just requirements.
    …

}                               which is an alternate name for it.

requirement def <'1’> VehicleMassLimitationRequirement :> MassLimitationRequirement {
    doc /* The total mass of a vehicle shall be less than or equal to the required mass. */

    subject vehicle : Vehicle;     A requirement definition is always about some
                                   subject, which may be implicit or specified explicitly.

    attribute redefines massActual = vehicle.dryMass + vehicle.fuelMass;

    assume constraint { vehicle.fuelMass > 0[kg] }                                          Features of the subject
}                                                                                           can be used in the
                                                                                            requirement definition.
                                                         A requirement definition may also
                                                         specify one or more assumptions.

87                  Last changed: 2023-10 ("human id" to "short name")                      Release 2026-04
```

### LAYOUT PDF PAGE 88

```text
                    Requirement Definitions (3)

                                      The subject of a requirement definition
                                      can have any kind of definition.

    port def ClutchPort;
    action def GenerateTorque;

    requirement def <'2’> DrivePowerInterfaceRequirement {
        doc /* The engine shall transfer its generated torque to the transmission
          * via the clutch interface. */
        subject clutchPort: ClutchPort;

    }

    requirement def <'3’> TorqueGenerationRequirement {
        doc /* The engine shall generate torque as a function of RPM as shown in Table 1. */
        subject generateTorque: GenerateTorque;

    }

88  Last changed: 2021-10 (requirement id)  Release 2026-04
```

### LAYOUT PDF PAGE 89

```text
                              Requirement Usages

A requirement may optionally               A requirement is the usage of a
have its own short name.                   requirement definition.

    requirement <'1.1’> fullVehicleMassLimit : VehicleMassLimitationRequirement {

       subject vehicle : Vehicle;          A requirement will often bind
       attribute :>> massReqd = 2000[kg];

                                           requirement definition

       assume constraint {                 parameters to specific values.
           doc /* Fuel tank is full. */

          vehicle.fuelMass == vehicle.fuelFullMass

       }

    }

    requirement <'1.2’> emptyVehicleMassLimit : VehicleMassLimitationRequirement {
        subject vehicle : Vehicle;
        attribute :>> massReqd = 1500[kg];

        assume constraint {
            doc /* Fuel tank is empty. */
            vehicle.fuelMass == 0[kg]

        }
    }

89                            Last changed: 2023-10 ("human id" to "short name")  Release 2026-04
```

### LAYOUT PDF PAGE 90

```text
A requirement may also be used  Requirement Groups
to group other requirements.
                                                                                Grouped requirements are treated as
                                                                                   required constraints of the group.

                         requirement vehicleSpecification {

                            doc /* Overall vehicle requirements group */

                            subject vehicle : Vehicle;

                                                                      By default, the subject of grouped

                             require fullVehicleMassLimit;            requirements is assumed to be the
                             require emptyVehicleMassLimit;           same as that of the group.
                         }

Requirements can be      part def Engine {
grouped by reference…
                            port clutchPort: ClutchPort;
    …or by composition.
                            perform action generateTorque: GenerateTorque;

                         }                                                The subject of a grouped

                         requirement engineSpecification {                requirement can also be
                             doc /* Engine power requirements group */    bound explicitly.

                            subject engine : Engine;

                            requirement drivePowerInterface : DrivePowerInterfaceRequirement {
                                  subject clutchPort = engine.clutchPort;

                            }

                             requirement torqueGeneration : TorqueGenerationRequirement {
                                   subject generateTorque = engine.generateTorque;

                             }
                         }

90                              Last changed: 2021-04 (dot notation)        Release 2026-04
```

### LAYOUT PDF PAGE 91

```text
    Requirement Satisfaction

    part vehicle_c1 : Vehicle {            A requirement satisfaction asserts
        part engine_v1: Engine { … }       that a given requirement is satisfied
        …                                  when its subject parameter is
                                           bound to a specific thing.
    }

    part 'Vehicle c1 Design Context' {
        ref vehicle_design :> vehicle_c1;

        satisfy vehicleSpecification by vehicle_design;
        satisfy engineSpecification by vehicle_design.engine_v1;
    }

     Formally, a requirement is satisfied for a subject
        if, when all its assumed constraints are true, then
        all its required constraints are true.

91  Last changed: 2021-04 (dot notation)                          Release 2026-04
```

### LAYOUT PDF PAGE 92

```text
        Analysis Case Definitions (1)

    An analysis case definition defines the
    computation of the result of analyzing
    some subject, meeting an objective.

                                             The subject may be specified similarly to

    analysis def FuelEconomyAnalysis {       the subject of a requirement definition.

    subject vehicle : Vehicle;

    objective fuelEconomyAnalysisObjective {                           The objective is a requirement on
        doc /*                                                         the result of the analysis case.

    * The objective of this analysis is to determine whether the

    * subject vehicle can satisfy the fuel economy requirement.

    */

        assume constraint {                         The analysis objective is specified as a
            vehicle.wheelDiameter == 33['in’] and   requirement, allowing both assumed
            vehicle.driveTrainEfficiency == 0.4     and required constraints.

        }                                          The analysis result is declared as a return
                                                   result (as for a calculation definition).
        require constraint {
              fuelEconomyResult > 30[mi / gallon]

        }
    }
    …

        return fuelEconomyResult : DistancePerVolumeValue = …;
    }

92                              Last changed: 2024-12 (return result)                   Release 2026-04
```

### LAYOUT PDF PAGE 93

```text
                               Analysis Case Definitions (2)

                               attribute def WayPoint {

                                      time : TimeValue;

                                      position : LengthValue;

The steps of an analysis case            speed : SpeedValue;
are actions that, together,    }
compute the analysis result.   analysis def FuelEconomyAnalysis {

                                   subject vehicle : Vehicle;

                                   objective fuelEconomyAnalysisObjective { … }

                                   in attribute scenario : WayPoint[*];          Additional parameters
                                   action solveForPower {                        can be specified in the

                                       out power: PowerValue[*];

The first step solves for the         out acceleration: AccelerationValue[*]; case body.
engine power needed for a
                                      assert constraint {

                                          (1..size(scenario)-1)->forAll {in i : Positive;

given position/velocity scenario.        StraightLineDynamicsEquations (
                                              power#(i), vehicle.mass,

                                         scenario.time#(i+1) – scenario.time#(i),

The second step computes the fuel        scenario.position#(i), scenario.speed#(i),
economy result, given the power          scenario.position#(i+1), scenario.speed#(i+1),
profile determined in the first step. }  acceleration#(i+1)))

                                   }

                                   then action solveForFuelEconomy {

                                      in power : PowerValue[*] = solveForPower.power;

                                      out fuelEconomy : DistancePerVolumeValue;

                                      …

                                   }

                                   return fuelEconomyResult : DistancePerVolumeValue;

                                         = solveForFuelEconomy.fuelEconomy;

                               …}

93                                       Last changed: 2024-12 (return result)             Release 2026-04
```

### LAYOUT PDF PAGE 94

```text
          Analysis Case Usages

part vehicleFuelEconomyAnalysisContext {

    requirement vehicleFuelEconomyRequirements{subject vehicle : Vehicle; … }

    attribute cityScenario : WayPoint[*] = { … };
    attribute highwayScenario : WayPoint[*] = { … };

    analysis cityAnalysis : FuelEconomyAnalysis {

        subject vehicle = vehicle_c1;                      The previously defined analysis is carried
        in scenario = cityScenario;                        out for a specific vehicle configuration
    }

                                                           for two different scenarios.

    analysis highwayAnalysis : FuelEconomyAnalysis {

       subject vehicle = vehicle_c1;

        in scenario = highwayScenario;                     The subject and parameters are
    }                                                      automatically redefined, so redefinition

    part vehicle_c1 : Vehicle {                            does not need to be specified explicitly.

       …

       attribute :>> fuelEconomy_city = cityAnalysis.fuelEconomyResult;

       attribute :>> fuelEconomy_highway = highwayAnalysis.fuelEconomyResult;

    }                                                                     If the vehicle fuel economy is set to

                                                                          the results of the analysis, then this

    satisfy vehicleFuelEconomyRequirements by vehicle_c1;                 configuration is asserted to satisfy the
}                                                                         desired fuel economy requirements.

94                               Last changed: 2022-05 (use of WayPoint)                 Release 2026-04
```

### LAYOUT PDF PAGE 95

```text
    Trade-off Study Analysis

The TradeStudy analysis definition from the                 A trade-off study is an analysis with the
TradeStudies domain library model provides a general           objective of selecting the optimum
framework for defining basic trade study analyses.             alternative from a given set based on
                                                               an evaluation of each alternative.

analysis engineTradeStudy : TradeStudies::TradeStudy {     Bind the analysis subject to the set of

    subject : Engine = (engine4cyl, engine6cyl);

    objective : MaximizeObjective;                         study alternatives. Select either

    calc :>> evaluationFunction {                          MaximizeObjective or MinimizeObjective.

    in part anEngine :>> alternative : Engine;

    calc powerRollup: PowerRollup {in engine = anEngine; Redefine the evaluationFunction

    return power : ISQ::PowerValue; }                      calculation to provide an evaluation

    calc massRollup: MassRollup {in engine = anEngine;     of each one of the alternatives.
        return mass : ISQ::MassValue; }

    calc efficiencyRollup: EfficiencyRollup {in engine = anEngine;

    return efficiency : Real; }

    calc costRollup: CostRollup {in engine = anEngine;

    return cost : Real; }

    return :>> result : Real = EngineEvaluation(

    powerRollup.power, massRollup.mass,

             efficiencyRollup.efficiency, costRollup.cost  The result of the analysis will be the
        );                                                 alternative with either the maximum
    }                                                      or minimum evaluated value.

    return part :>> selectedAlternative : Engine;

}

95                         Last changed: 2022-07 (parameter declaration)  Release 2026-04
```

### LAYOUT PDF PAGE 96

```text
    Verification Case Definitions (1)

requirement vehicleMassRequirement {          Parameterizing the requirement allows
    subject vehicle : Vehicle;                it to be checked against a measured
    in massActual :> ISQ::mass;               massActual, while asserting (below) that
    doc /* The vehicle mass shall be less     this must be equal to the vehicle.mass.
              * than or equal to 2500 kg. */
    require constraint {                       A verification case definition defines a
        massActual == vehicle.mass and         process for verifying whether a subject
        massActual <= 2500[SI::kg] }           satisfies one or more requirements.

}                                             The subject may be specified similarly to the
verification def VehicleMassTest {            subject of a requirement or analysis case.

    private import VerificationCases::*;

    subject testVehicle : Vehicle;

    objective vehicleMassVerificationObjective {  The requirements to be verified are declared in
        verify vehicleMassRequirement;            the verification case objective. The subject of
                                                  the verification case is automatically bound to
    }                                             the subject of the verified requirements.

    return verdict : VerdictKind;
}

    A verification case always returns a        VerdictKind is an
    verdict of type VerdictKind. (The
    default name is verdict, but a different       enumeration with
    name can be used if desired.)             Last cahlalonwgeedd: 2v0a2l0u-e11s pass, fail,

                                                   inconclusive and error.

96  Last changed: 2024-12 (massActual binding)                                                Release 2026-04
```

### LAYOUT PDF PAGE 97

```text
    Verification Case Definitions (2)

                                   verification def VehicleMassTest {
                                       private import VerificationCases::*;

The steps of a verification case   subject testVehicle : Vehicle;
are actions that, together,        objective vehicleMassVerificationObjective {
determine the verdict.
                                       verify vehicleMassRequirement;
                                   }

                                   action collectData {

                                      in part testVehicle : Vehicle = VehicleMassTest::testVehicle;

                                      out massMeasured :> ISQ::mass;

                                   }

                                   action processData {

PassIf is a utility function that     in massMeasured :> ISQ::mass = collectData.massMeasured;
returns a pass or fail verdict
depending on whether its              out massProcessed :> ISQ::mass;
argument is true or false.
                                   }
        The use of named
           argument notation       action evaluateData {
           here is optional.
                                      in massProcessed :> ISQ::mass = processData.massProcessed;

                                      out verdict : VerdictKind =

                                         PassIf(vehicleMassRequirement(

                                         vehicle = testVehicle,                     This is a check of whether the

                                      }  massActual = massProcessed)); requirement is satisfied for

                                                                                    the given parameter values.

                                       return verdict : VerdictKind = evaluateData.verdict;
                                   }

97                                       Last changed: 2024-12 (import visibility)           Release 2026-04
```

### LAYOUT PDF PAGE 98

```text
                              Verification Case Usages (1)

This is a verification case   part vehicleTestConfig : Vehicle { … }
usage in which the subject
has been restricted to a      verification vehicleMassTest : VehicleMassTest {
specific test configuration.      subject testVehicle :> vehicleTestConfig;

A verification case can be    }
performed as an action by
a verification system.        part massVerificationSystem : MassVerificationSystem {
                                  perform vehicleMassTest;
Parts of the verification
system can perform steps      part scale : Scale {
in the overall verification       perform vehicleMassTest.collectData {
process.                              in part :>> testVehicle;

                              bind measurement = testVehicle.mass;

                                           out :>> massMeasured = measurement;  In reality, this would be
                                      }                                         some more involved
                                  }                                             process to determine
                              }                                                 the measured mass.

98                            Last changed: 2022-05 (dot notation on perform)   Release 2026-04
```

### LAYOUT PDF PAGE 99

```text
                             Verification Case Usages (2)

Individuals can be used to   individual def TestSystem :> MassVerificationSystem;
model the carrying out of    individual def TestVehicle1 :> Vehicle;
actual tests.                individual def TestVehicle2 :> Vehicle;

! The keyword action is      individual testSystem : TestSystem :> massVerificationSystem {
    required here to permit
    the local redefinition.     timeslice test1 {

                                   perform action :>> vehicleMassTest {

                                      individual :>> testVehicle : TestVehicle1 {

                                         :>> mass = 2500[SI::kg];

                                      }

                                   }                                          The test on the individual

                                }                                             TestVehicle1 should pass.

                                then timeslice test2 {

                                   perform action :>> vehicleMassTest {

                                      individual :>> testVehicle : TestVehicle2 {

                                         :>> mass = 3000[SI::kg];

                                      }

                                   }                                          The test on the individual

                                }                                             TestVehicle2 should fail.

                             }

99                                    Last changed: 2021-03 (units notation)       Release 2026-04
```

### LAYOUT PDF PAGE 100

```text
                                    Use Case Definition

                                          A use case definition defines a
                                          required interaction between its
                                          subject and certain external actors.

An actor is a parameter of the use  use case def 'Provide Transportation’ {
case representing a role played
by entity external to the subject.     subject vehicle : Vehicle;               ! Actors are (referential)
                                       actor driver : Person;
The objective of the use case is
for the subject to provide a           actor passengers : Person[0..4];         part usages and so must
result of value to one or more
of the actors.                         actor environment : Environment;         have part definitions.
                                       objective {

                                          doc /* Transport driver and passengers from

                                          * starting location to ending location.

                                          */

                                       }

                                    }

 Actors may also be specified for  use case def 'Enter Vehicle’ {
    other kinds of cases and for        subject vehicle : Vehicle;
    requirements.                       actor driver : Person;
                                        actor passengers : Person[0..4];

                                    }

                                    use case def 'Exit Vehicle’ {
                                        subject vehicle : Vehicle;
                                        actor driver : Person;
                                        actor passengers : Person[0..4];

                                    }

100                                       Last changed: 2021-08 (new)                  Release 2026-04
```

### LAYOUT PDF PAGE 101

```text
                                     Use Case Usage

                               use case 'provide transportation' : 'Provide Transportation’ {

                                  subject vehicle;

The required behavior of          first start;
a use case can be
specified as for an action.       then include use case 'enter vehicle' : 'Enter Vehicle’ {

A use case can define                subject vehicle;
sub-use cases within its
behavior.                            actor :>> driver = 'provide transportation'::driver;

A use case can include the           actor :>> passengers = 'provide transportation'::passengers;
performance of a use case
defined elsewhere (similar        }
to performing an action).
                                  then use case 'drive vehicle’ {
! The traditional use case
    “extend” relationship is         subject vehicle;
    not supported yet.
                                     actor driver = 'provide transportation'::driver;
A use case can also be
specified without an                 actor environment = 'provide transportation'::environment;
explicit use case definition.
                                      include 'add fuel'[0..*] {             ! A subject must be declared
101                                       subject vehicle;                      first, before any actors. It can
                                          actor :>> fueler = driver;            only be omitted if there are no
                                                                                actors or other parameters.
                                      }
                                  }

                                  then include use case 'exit vehicle' : 'Exit Vehicle’ {

                                     subject vehicle;

                                     actor :>> driver = 'provide transportation'::driver;

                                     actor :>> passengers = 'provide transportation'::passengers;

                                  }                           The subject of a nested use case is implicitly
                                  then done;

                               }                              bound to that of its containing use case, but

                               use case 'add fuel’ {          actors need to be explicitly bound.

                                  subject vehicle : Vehicle;

                                  actor fueler : Person;

                                  actor 'fuel station' : 'Fuel Station’;

                               }

                                     Last changed: 2025-07 (added subjects)            Release 2026-04
```

### LAYOUT PDF PAGE 102

```text
                                  Variation Definitions

                                  attribute def Diameter :> Real;

                                  part def Cylinder {
                                      attribute diameter : Diameter[1];

                                  }

                                  part def Engine {

                                     part cylinder : Cylinder[2..*];

                                  }

 Any kind of definition can be    part '4cylEngine' : Engine {               A variation definition will typically
 marked as a variation,               part redefines cylinder[4];            specialize a definition from a design
 expressing variability within a                                             model, representing the type of thing
 product line model.              }                                          being varied. The variants must then
                                  part '6cylEngine' : Engine {
 A variation defines one or
 more variant usages, which           part redefines cylinder[6];
 represent the allowed
 choices for that variation.      }                                          be valid usages of this type.

102                               // Variability model

                                  variation attribute def DiameterChoices :> Diameter {

                                     variant attribute diameterSmall = 70[mm];

                                     variant attribute diameterLarge = 100[mm];

                                  }

                                  variation part def EngineChoices :> Engine {

                                     variant '4cylEngine';

                                      variant '6cylEngine';                  Variants can also be declared by
                                  }                                          reference to usages defined elsewhere.

                                     Last changed: 2021-03 (units notation)      Release 2026-04
```

### LAYOUT PDF PAGE 103

```text
                                   Variation Usages

                                                                              A variation definition can be
                                                                              used like any other definition,
                                                                              but valid values of the usage
                                                                              are restricted to the allowed
                                                                              variants of the variation.

Any kind of usage can also      abstract part vehicleFamily : Vehicle {
be a variation, defining            part engine : EngineChoices[1];
allowable variants without a
separate variation definition.

                                   variation part transmission : Transmission[1] {
                                       variant manualTransmission;
                                       variant automaticTransmission;

                                   }

A constraint can be used to        assert constraint {
model restrictions across the          (engine == engine::'4cylEngine’ and
choices that can be made.               transmission == transmission::manualTransmission) xor
                                       (engine == engine::'6cylEngine’ and
                                         transmission == transmission::automaticTransmission)

                                   }

                                }   The operator xor means "exclusive or". So, this constraint

                                   means "choose either a 4cylEngine and a manualTransmission,

                                   or a 6cylEngine and an automaticTransmission".

103                                Last changed: 2021-05 (logical operators)                     Release 2026-04
```

### LAYOUT PDF PAGE 104

```text
     Variation Configuration

     An element from a variability model                              A selection is made for a variation
     with variation usages can be configured                          by binding one of the allowed
     by specializing it and making selections                         variants to the variation usage.
     for each of the variations.

     part vehicle4Cyl :> vehicleFamily {
         part redefines engine = engine::'4cylEngine';
         part redefines transmission = transmission::manualTransmission;

     }

     part vehicle6Cyl :> vehicleFamily {
         part redefines engine = engine::'6cylEngine';
         part redefines transmission = transmission::manualTransmission;

     }

     Choosing a manualTransmission with a
     6cylEngine is not allowed by the
     constraint asserted on vehicleFamily,
     so this model of vehicle6Cyl is invalid.

104                                            Last changed: 2020-06  Release 2026-04
```

### LAYOUT PDF PAGE 105

```text
     Dependencies

     package 'Dependency Example' {        A dependency is a relationship that indicates that
         part 'System Assembly' {             one or more client elements require one more
             part 'Computer Subsystem' {      supplier elements for their complete specification.
                  …                           A dependency is entirely a model-level
             }                                relationship, without instance-level semantics.
             part 'Storage Subsystem' {
                  …                       A dependency can be between any kinds of elements,
             }                            generally meaning that a change to a supplier may
         }                                necessitate a change to the client element.
         package 'Software Design' {
             item def MessageSchema {
                  …
             }
             item def DataSchema {
                  …
             }
         }

     dependency from 'System Assembly'::'Computer Subsystem' to 'Software Design';

         dependency Schemata
             from 'System Assembly'::'Storage Subsystem'
             to 'Software Design'::MessageSchema, 'Software Design'::DataSchema;

     }

     A dependency can have multiple clients and/or suppliers.

105  Last changed: 2020-08                                                        Release 2026-04
```

### LAYOUT PDF PAGE 106

```text
                                          Allocation

                                    package LogicalModel {
                                        …
                                        part torqueGenerator : TorqueGenerator {
                                            perform generateTorque;
                                        }

                                    }

                                    package PhysicalModel {                           Allocations define traceable links
                                                                                         across the various structures and
                                    private import LogicalModel::*;                      hierarchies of a system model,
                                                                                         perhaps as a precursor to more
An allocation specifies that        …                                                    rigorous specifications and
some or all of the responsibility   part powerTrain : PowerTrain {                       implementations.
for realizing the intent of the
                                        part engine : Engine {
                                            perform generateTorque;

source is allocated to the target.     }

                                    }

                                        allocate torqueGenerator to powerTrain {
                                            allocate torqueGenerator.generateTorque
                                                       to powerTrain.engine.generateTorque;

                                        }
                                    }

                                                                                              An allocation can be refined using
                                                                                              nested allocations that give a finer-
                                                                                              grained decomposition of the
                                                                                              containing allocation mapping.

106                                       Last changed: 2024-07 (import visibility)  Release 2026-04
```

### LAYOUT PDF PAGE 107

```text
                                       Allocation Definition

                                       package LogicalModel {

                                       …

     ! Unlike SysML v1, an             part def LogicalElement;
        allocation in SysML v2 is not  part def TorqueGenerator :> LogicalElement;

     a dependency but, rather, an          part torqueGenerator : TorqueGenerator { … }
     instantiable connection           }

     across model features.

                                       package PhysicalModel {

                                       private import LogicalModel::*;

                                       …

                                       part def PhysicalElement;

     An allocation definition defines part def PowerTrain :> PhysicalElement;

     a class of allocations between    part powerTrain : PowerTrain { … }
     features of specific types.       }

     An allocation usage must              allocation def LogicalToPhysical {
     allocate features that conform            end logical : LogicalElement;
     to the types of the ends of its           end physical : PhysicalElement;
     allocation definition.
                                           }

                                           allocation torqueGenAlloc : LogicalToPhysical
                                               allocate torqueGenerator to powerTrain { … }

                                       }

107                                    Last changed: 2024-07 (import visibility)         Release 2026-04
```

### LAYOUT PDF PAGE 108

```text
                                     Metadata (1)

 Metadata is additional data     part vehicle {                   The KerML and SysML library
    that can be used to annotate      part interior {                 models include all the
    the elements of a model.              part alarm;                 metaclasses from the KerML
                                          part seatBelt[2];           and SysML abstract syntax.
  Metadata is defined using a             part frontSeat[2];
  metadata definition.                    part driverAirBag;      To restrict what kind of element
                                      }                           can be annotated, subset the
                                      part bodyAssy {             annotatedElement feature with
                                          part body;              the desired element type(s).
                                          part bumper;
                                          part keylessEntry;
                                      }

                                  }

                                  metadata def SafetyFeature;

                                  metadata def SecurityFeature {

                                     :> annotatedElement : SysML::PartDefinition;

                                     :> annotatedElement : SysML::PartUsage;

                                  }

                                  metadata SafetyFeature about

A specific type of metadata can      vehicle::interior::seatBelt,       At its simplest, a metadata
then be applied as an annotation     vehicle::interior::driverAirBag,      annotation can be used to
to one or more model elements.       vehicle::bodyAssy::bumper;            simply "tag" certain

                                  metadata SecurityFeature about       elements, so that they can,

                                     vehicle::interior::alarm,         e.g., be grouped by tooling.

                                     vehicle::bodyAssy::keylessEntry;

108  Last changed: 2022-03 (metadata definition, annotatedElement)                 Release 2026-04
```

### LAYOUT PDF PAGE 109

```text
                                Metadata (2)

                          standard library package AnalysisTooling {

                             private import ScalarValues::*;

                             metadata def ToolExecution {                   The AnalysisTooling
                                 attribute toolName : String;                  package is part of the
                                 attribute uri : String;                       Analysis domain library.

                             }

                             metadata def ToolVariable {

                                attribute name : String;

                             }

                          }                                If the metadata definition has nested

                          action computeDynamics {         features, these must be bound to

                             private import AnalysisToolivnagl:u:e*s;in the metadata annotation.

                             metadata ToolExecution {

                                toolName = "ModelCenter";                  The @ symbol is equivalent

A metadata annotation        } uri = "aserv://localhost/Vehicle/Equation1"; to the metadata keyword.

contained in the body of in dt : ISQ::TimeValue {@ToolVariable {name = "deltaT";}}

a namespace (package, in a : ISQ:: AccelerationValue {@ToolVariable {name = "mass";}}

definition or usage) is,     in v_in : ISQ:: VelocityValue {@ToolVariable {name = "v0";}}
by default, about that       in x_in : ISQ:: LengthValue {@ToolVariable {name = "x0";}}

namespace.                   out v_out : ISQ:: VelocityValue {@ToolVariable {name = "v";}}

                             out x_out : ISQ:: LengthValue {@ToolVariable {name = "x";}}

                          }

109                             Last changed: 2024-07 (import visibility)                         Release 2026-04
```

### LAYOUT PDF PAGE 110

```text
                          Element Import Filtering (1)

metadata def Safety {                                                       A recursive import (using **)
                                                                            imports members of a namespace
   attribute isMandatory : Boolean;                                         and, recursively, members of any
                                                                            nested namespaces.
}

                          ! Currently, a metadata annotation must

part vehicle {            be owned by the annotated element to
    part interior {       be accessed in a filter condition.
        part alarm;

      part seatBelt[2] {                  package 'Safety Features' {
          @Safety{isMandatory = true;}}       public import vehicle::**;
                                              filter @Safety;
      part frontSeat[2];
      part driverAirBag {                 }

          @Safety{isMandatory = false;}}

   }                                      package 'Mandatory Safety Features' {
   part bodyAssy {                            public import vehicle::**;
                                              filter @Safety and (as Safety).isMandatory;
       part body;
       part bumper {                      }

           @Safety{isMandatory = true;}}

      part keylessEntry;

   }

   part wheelAssy {                       A filter is a Boolean             @ checks life an element
       part wheel[2];                     condition that must be true       has the given metadata
       part antilockBrakes[2] {

      @Safety{isMandatory = false;}}      for an element to actually        and as ”casts” to that

   }                                      be imported into a package.       metadata type.

}

110                              Last changed: 2026-03 (filter expression)  Release 2026-04
```

### LAYOUT PDF PAGE 111

```text
     Element Import Filtering (2)

metadata def Safety {                         The filter keyword is only allowed in a
    attribute isMandatory : Boolean;             package (or view), but a filtered import can
                                                 be used anyplace an import is allowed.
}
                                             Filter conditions can also be
part vehicle {                               combined with the import itself.
    part interior {
        part alarm;                          package 'Safety Features' {
        part seatBelt[2] {                       public import vehicle::**[@Safety];
             @Safety{isMandatory = true;}}
        part frontSeat[2];                   }
        part driverAirBag {
             @Safety{isMandatory = false;}}  package 'Mandatory Safety Features' {
    }                                            public import vehicle::**
    part bodyAssy {                                  [@Safety and (as Safety).isMandatory];
        part body;
        part bumper {                        }
             @Safety{isMandatory = true;}}
        part keylessEntry;                    ! A filter condition expression must be model-
    }                                             level evaluable. It can reference only literals
    part wheelAssy {                              and metadata annotations and attributes,
        part wheel[2];                            connected using basic arithmetic,
        part antilockBrakes[2] {                  comparison and Boolean operators.
             @Safety{isMandatory = false;}}
    }

}

111  Last changed: 2026-03 (filter expression)  Release 2026-04
```

### LAYOUT PDF PAGE 112

```text
        Language Extension (1)

                                                For a domain-specific extension to SysML, first

                                                create a library model of domain-specific concepts.

library package FailureModeling {               This can be explicitly identified as a library package.
    abstract occurrence def Situation;

     abstract occurrence situations : Situation[*] nonunique;

     abstract occurrence def Cause {
         attribute probability : Real;

     }
     abstract occurrence causes : Cause[*] nonunique :> situations;

     abstract occurrence def Failure {                                        For each concept, provide a base
         attribute severity : Level;                                          definition and a base usage
                                                                              modeling the concept semantics.
     }

     abstract occurrence failures : Failure[*] nonunique :> situations;

     abstract connection def Causation :> Occurrences::HappensBefore {

        end cause : Situation[*];

        end effect : Situation[*];

     }

     abstract connection causations : Causation[*] nonunique;                 HappensBefore is the base type

     item def Scenario {                                                      for successions, from the Kernel
         occurrence :>> situations;                                           Library Occurrences package.

        occurrence :>> causes :> situations;

        occurrence :>> failures :> situations;

     }

     item scenarios : Scenario[*] nonunique;

}

112                                  Last changed: 2022-09 (library package)  Release 2026-04
```

### LAYOUT PDF PAGE 113

```text
           Language Extension (2)

     library package FailureModelingMetadata {            Declare semantic metadata for
         private import FailureModeling::*;               each concept to be included in
         private import Metaobjects::SemanticMetadata;    the language extension.

         metadata def situation :> SemanticMetadata {
            :>> baseType = situations meta SysML::Usage;

         }

        metadata def cause :> SemanticMetadata {          Bind baseType to the base usage
           :>> baseType = causes meta SysML::Usage;       for the relevant concept.

        }

        metadata def failure :> SemanticMetadata {

           :>> baseType = failures meta SysML::Usage;

        }

                                                          The meta-cast "meta

        metadata def causation :> SemanticMetadata { SysML::Usage" allows failures to

           :>> baseType = causations meta SysML::Usage; be referenced as a usage, rather

        }                                                 than evaluated as an expression.

        metadata def scenario :> SemanticMetadata {

           :>> baseType = scenarios meta SysML::Usage;

        }

     }

113        Last changed: 2024-07 (import visibility)                           Release 2026-04
```

### LAYOUT PDF PAGE 114

```text
                            Language Extension (3)

                                   private import FailureModelingMetadata::*;

                                   #scenario def DeviceFailure {                        Implicitly specializes the
                                      ref device : Device;                              library definition Scenario
                                      attribute minPower : Real;                        (the definition of the
                                                                                        scenarios base type).
A user-defined keyword, starting   #cause 'battery old' {
with # and referencing a semantic      :>> probability = 0.01;
metadata definition, can be used
to declare a definition or usage.  }

                                   #causation connect 'battery old’ to 'power low';

Implicitly specializes the         #situation 'power low' {
library usage situations               constraint { device.battery.power < minPower }
(as given in the semantic
metadata situation).               }

                                   #causation connect 'power low’ to 'device shutoff';

Inheritance and                       #failure 'device shutoff' {
redefinition work as for                  :>> severity = LevelEnum::high;
explicit specialization.
                                      }
                                   }

114                         Last changed: 2025-07 (changed successions to connections)  Release 2026-04
```

### LAYOUT PDF PAGE 115

```text
            Stakeholders and Concerns

     part def 'Systems Engineer';  A concern is a specific topic that one or more
     part def 'IV&V’;              stakeholders desire to be addressed.

     concern 'system breakdown' {
        doc /*
          * To ensure that a system covers all its required capabilities,

        * it is necessary to understand how it is broken down into

        * subsystems and components that provide those capabilities.

         */                                  ! A subject must be declared first, before any
        subject system;                        stakeholders. It can only be omitted if there
        stakeholder se: 'systems engineer';
        stakeholder ivv: 'IV&V';               are no stakeholders or other parameters.

     }

     concern modularity {          A stakeholder is a person, organization or
        doc /*                     other entity with concerns to be addressed.

        * There should be well defined interfaces between the parts of

        * a system that allow each part to be understood individually,

        * as well as being part of the whole system.

        */

        subject system;                       Stakeholders may be specified for any
        stakeholder 'systems engineer';          kind of requirement, not just concerns.
     }

115                        Last changed: 2025-07 (added subjects)                  Release 2026-04
```

### LAYOUT PDF PAGE 116

```text
                              Viewpoints

                   A viewpoint is a requirement to present
                   information from a model in a view that
                   addresses certain stakeholder concerns.

     viewpoint 'system structure perspective' {

        frame 'system breakdown';

        frame modularity;          A viewpoint frames the concerns that will be

        require constraint {       addressed by a view that satisfies the viewpoint.

           doc /*

           * A system structure view shall show the hierarchical

           * part decomposition of a system, starting with a

           * specified root part.

           */

        }

     }

                    Any requirement may be modeled
                       as framing relevant stakeholder
                       concerns, not just viewpoints.

116                           Last changed: 2021-05 (new)         Release 2026-04
```

### LAYOUT PDF PAGE 117

```text
                                              Views (1)

                                                                           A view definition specifies how

                                                                           information can be extracted

                                                                           from a model in order to satisfy

A view definition can     view def 'Part Structure View' {                 one or more viewpoints.
filter the elements to
be included in the        satisfy 'system structure perspective’;
views it specifies.
                             filter @SysML::PartUsage;                     The SysML library package models
A view usage specifies a  }                                                the SysML abstract syntax, which
certain view conforming                                                    can be used to filter on specific
to a view definition.     view 'vehicle structure view' :                  kinds of model elements.
                             'Part Structure View' {

                             expose vehicle::**;         A view usage exposes the model elements
                                                         to be included in the view, which are
                             render asTreeDiagram;       filtered as specified in the view definition.
                          }

 The view rendering can also be given        A view usage specifies how the view is
    in the view definition, in which case it  to be rendered as a physical artifact.
    will be the same for all usages of that
    definition. But only view usages can
    expose elements to be viewed.

117                                           Last changed: 2021-05 (new)             Release 2026-04
```

### LAYOUT PDF PAGE 118

```text
Specialized kinds of renderings  Views (2)
can be defined in a user model.
                                                           The Views library package includes four
                                                               basic kinds of rendering: asTreeDiagram,
                                                               asInterconnectionDiagram,
                                                               asTextualNotation and asElementTable.

                rendering asTextualNotationTable :> asElementTable {

                view :>> columnView[1] {

                       render asTextualNotation;  ! A more comprehensive
                   }                                 rendering library model is
                }                                    planned for future release.

Views can have  view 'vehicle tabular views’ {
subviews.              view 'safety features view' : 'Part Structure View’ {
                           expose vehicle::**[@Safety];
                           render asElementTable;
                       }

                view 'non-safety features view' : 'Part Structure View’ {

                          expose vehicle::**[not (@Safety)];

                          render asElementTable;

                       }                          Views can specify additional filtering
                }                                 conditions on an expose, using the

                                                  same notation as for an import.

118                              Last changed: 2021-09 (editorial correction)  Release 2026-04
```

### LAYOUT PDF PAGE 119

```text
       Example View Rendering

     view ‘vehicle structure view’ {
        expose vehicle::**[@SysML::PartUsage];
        render asTreeDiagram;

     }

119  Last changed: 2021-05 (new)                Release 2026-04
```

### LAYOUT PDF PAGE 120

```text
     Kernel Data Type Library

120                            Release 2026-04
```

### LAYOUT PDF PAGE 121

```text
     Scalar Values

     standard library package ScalarValues {
        private import Base::*;

        abstract datatype ScalarValue specializes Value;
        datatype Boolean specializes ScalarValue;
        datatype String specializes ScalarValue;
        abstract datatype NumericalValue specializes ScalarValue;

        abstract datatype Number specializes NumericalValue;
        datatype Complex specializes Number;
        datatype Real specializes Complex;
        datatype Rational specializes Real;
        datatype Integer specializes Rational;
        datatype Natural specializes Integer;
        datatype Positive specializes Natural;
     }

121  Last changed: 2022-09 (standard library package)              Release 2026-04
```

### LAYOUT PDF PAGE 122

```text
     Collections (1)

     standard library package Collections {
         …
         abstract datatype Collection {
             feature elements[0..*] nonunique;
         }
         abstract datatype OrderedCollection :> Collection {
             feature :>> elements[0..*] ordered nonunique;
         }
         abstract datatype UniqueCollection :> Collection {
             feature :>> elements[0..*];
         }

     datatype Array :> OrderedCollection {
         feature dimensions: Positive[0..*] ordered nonunique;
         feature rank: Natural[1] = size(dimensions);
         feature flattenedSize: Positive[1] = dimensions->reduce '*' ?? 1;
         inv { flattenedSize == size(elements) }

     }

         datatype Bag :> Collection;
         datatype Set :> UniqueCollection;
         datatype OrderedSet :> OrderedCollection, UniqueCollection {

             feature :>> elements[0..*] ordered;
         }
         datatype List :> OrderedCollection;
         …
     }

122  Last changed: 2022-09 (standard library package)                  Release 2026-04
```

### LAYOUT PDF PAGE 123

```text
     Collections (2)

     standard library package Collections {
         …

         datatype KeyValuePair {
             feature key: Anything[0..*] ordered nonunique;
             feature val: Anything[0..*] ordered nonunique;

         }

         datatype Map :> Collection {
             feature :>> elements: KeyValuePair[0..*];

         }

         datatype OrderedMap :> Map {
             feature :>> elements: KeyValuePair[0..*] ordered;

         }

     }

123  Last changed: 2022-09 (standard library package)           Release 2026-04
```

### LAYOUT PDF PAGE 124

```text
     Vector Values

standard library package VectorValues {
    private import ScalarValues::NumericalValue;
    private import ScalarValues::Real;
    private import Collections::Array;

    abstract datatype VectorValue;

    datatype NumericalVectorValue :> VectorValue, Array {
       feature dimension[0..1] :>> dimensions;
       feature :>> elements : NumericalValue;

    }

    datatype CartesianVectorValue :> NumericalVectorValue {
       feature :>> elements : Real;

    }

    datatype ThreeVectorValue :> NumericalVectorValue {
       feature :>> dimension = 3;

    }

    datatype CartesianThreeVectorValue :> CartesianVectorValue, ThreeVectorValue;
}

124  Last changed: 2022-09 (standard library package)  Release 2026-04
```

### LAYOUT PDF PAGE 125

```text
     Kernel Function Library
        (selected models)

125                           Release 2026-04
```

### LAYOUT PDF PAGE 126

```text
                                          Base Functions

standard library package BaseFunctions {
     private import Base::Anything;
     private import ScalarValues::*;

abstract function '==' { in x: Anything[0..1]; in y: Anything[0..1];
     return : Boolean[1];

}
function '!=' { in x: Anything[0..1]; in y: Anything[0..1];

     return : Boolean[1] = not (x == y)
}
abstract function '===' { in x: Anything[0..1]; in y: Anything[0..1];

     return : Boolean[1];
}
function '!==' { in x: Anything[0..1]; in y: Anything[0..1];

     return : Boolean[1] = not (x === y)
}

function ToString { in Anything[0..1];
     return : String[1];

}

     abstract function '['{ in x: Anything[0..*] nonunique; in y: Anything[0..*] nonunique;
          return : Anything[0..*] nonunique;

     }
     abstract function '#'{ in seq: Anything[0..*] ordered nonunique; in index: Positive[1..*] ordered nonunique;

          return : Anything[0..1];
     }
     abstract function ','{

          in seq1: Anything[0..*] ordered nonunique; seq2: Anything[0..*] ordered nonunique;
          return : Anything[0..*] ordered nonunique;
     }
     …
}

126                                       Last changed: 2023-02 (added '[', '#', ',')  Release 2026-04
```

### LAYOUT PDF PAGE 127

```text
     Data Functions

standard library package DataFunctions {                ScalarFunctions package is similar

…                                                      but specialized for ScalarValue.

abstract function '=='specializes BaseFunctions::'=='

     {in x: DataValue[0..1]; in y: DataValue[0..1]; return : Boolean[1];}

function '==='specializes BaseFunctions::'==='

     {in x: DataValue[0..1]; in y: DataValue[0..1]; return : Boolean[1];}

   abstract function '+'{in x: DataValue[1]; in y: DataValue[0..1]; return : DataValue[1];}
   abstract function '-'{in x: DataValue[1]; in y: DataValue[0..1]; return : DataValue[1];}
   abstract function '*'{in x: DataValue[1]; in y: DataValue[1]; return : DataValue[1];}
   abstract function '/'{in x: DataValue[1]; in y: DataValue[1]; return : DataValue[1];}
   abstract function '**'{in x: DataValue[1]; in y: DataValue[1]; return : DataValue[1];}
   abstract function '^'{in x: DataValue[1]; in y: DataValue[1]; return : DataValue[1];}
   abstract function '%'{in x: DataValue[1]; in y: DataValue[1]; return : DataValue[1];}
   abstract function 'not'{in x: DataValue[1]; return : DataValue[1];}
   abstract function 'xor'{in x: DataValue[1]; in y: DataValue[1]; return : DataValue[1];}
   abstract function '~'{in x: DataValue[1]; return : DataValue[1];}
   abstract function '|'{in x: DataValue[1]; in y: DataValue[1]; return : DataValue[1];}
   abstract function '&'{in x: DataValue[1]; in y: DataValue[1]; return : DataValue[1];}
   abstract function '<'{in x: DataValue[1]; in y: DataValue[1]; return : Boolean[1];}
   abstract function '>'{in x: DataValue[1]; in y: DataValue[1]; return : Boolean[1];}
   abstract function '<='{in x: DataValue[1]; in y: DataValue[1]; return : Boolean[1];}
   abstract function '>='{in x: DataValue[1]; in y: DataValue[1]; return : Boolean[1];}
   abstract function max{in x: DataValue[1]; return : DataValue[1];}
   abstract function min{in x: DataValue[1]; return : DataValue[1];}
   abstract function '..'

        {in lower:DataValue[1]; in upper:DataValue[1]; return : DataValue[0..*] ordered;
   }
}

127  Last changed: 2022-09 (standard library package, "===")               Release 2026-04
```

### LAYOUT PDF PAGE 128

```text
     Boolean Functions

standard library package BooleanFunctions {
   public import ScalarValues::*;

   function 'not' specializes ScalarFunctions::'not’
       {in x: Boolean; return : Boolean;}

   function 'xor' specializes ScalarFunctions::’xor’
       {in x: Boolean; in y: Boolean; return : Boolean;}

   function '|' specializes ScalarFunctions::'|’
       {in x: Boolean; in y: Boolean; return : Boolean;}

   function '&' specializes ScalarFunctions::'&’
       {in x: Boolean; in y: Boolean; return : Boolean;}

   function '==' specializes BaseFunctions::'==‘
       {in x: Boolean; in y: Boolean; return : Boolean;}

   function ToString specializes BaseFunctions::ToString
       {in x: Boolean; return : String;}

   function ToBoolean(x: String): Boolean;
       {in x: String; return : Boolean;}

}

128  Last changed: 2024-07 (import visibility)            Release 2026-04
```

### LAYOUT PDF PAGE 129

```text
     String Functions

standard library package StringFunctions {
   public import ScalarValues::*;

function '+' specializes ScalarFunctions::’+’
   {in x: String; in y: String; return : String;}

function Size {in x: String; return : Natural;}
function Substring

   {in x: String; in lower: Integer; in upper: Integer; return : String;}

function '<' specializes ScalarFunctions::'<‘
   {in x: String; in y: String; return : Boolean;}

function '>' specializes ScalarFunctions::’>’
   {in x: String; in y: String; return : Boolean;}

function '<=' specializes ScalarFunctions::'<='
   {in x: String; in y: String; return : Boolean;}

function '>=' specializes ScalarFunctions::'>='
   {in x: String; in y: String; return : Boolean;}

function '=' specializes BaseFunctions::'=='
   {in x: String; in y: String; return : Boolean;}

   function ToString specializes BaseFunctions::ToString
       {in x: String; return : String;

}

129  Last changed: 2024-07 (import visibility)            Release 2026-04
```

### LAYOUT PDF PAGE 130

```text
     Numerical Functions

standard library package NumericalFunctions {
    public import ScalarValues::*;
    function abs {in x: NumericalValue[1]; return : NumericalValue[1];}
    abstract function ‘+’ specializes ScalarFunctions::‘+’
          {in x: NumericalValue[1]; in y: NumericalValue[0..1]; return : NumericalValue[1];}
    abstract function '-' specializes ScalarFunctions::‘-’
          {in x: NumericalValue[1]; in y: NumericalValue[0..1]; return : NumericalValue[1];}
    abstract function '*' specializes ScalarFunctions::‘*’
          {in x: NumericalValue[1]; in y: NumericalValue[1]; return : NumericalValue[1];}
    abstract function '/' specializes ScalarFunctions::‘/’
          {in x: NumericalValue[1]; in y: NumericalValue[0..1]; return : NumericalValue[1];}
    abstract function '**' specializes ScalarFunctions::‘**’
          {in x: NumericalValue[1]; in y: NumericalValue[0..1]; return : NumericalValue[1];}
    abstract function '^' specializes ScalarFunctions::‘^’
          {in x: NumericalValue[1]; in y: NumericalValue[0..1]; return : NumericalValue[1];}
    abstract function '%' specializes ScalarFunctions::‘%’
          {in x: NumericalValue[1]; in y: NumericalValue[0..1]; return : NumericalValue[1];}
    abstract function '<‘specializes ScalarFunctions::‘<’
          {in x: NumericalValue[1]; in y: NumericalValue[0..1]; return : Boolean[1];}
    abstract function ‘>’ specializes ScalarFunctions::‘>’
          {in x: NumericalValue[1]; in y: NumericalValue[0..1]; return : Boolean[1];}
    abstract function '<=' specializes ScalarFunctions::‘<=’
          {in x: NumericalValue[1]; in y: NumericalValue[0..1]; return : Boolean[1];}
    abstract function '>=' specializes ScalarFunctions::‘>=’
          {in x: NumericalValue[1]; in y: NumericalValue[0..1]; return : Boolean[1];}
    abstract function max specializes ScalarFunctions::max
          {in x: NumericalValue[1]; in y: NumericalValue[0..1]; return : NumericalValue[1];}
    abstract function min specializes ScalarFunctions::min
          {in x: NumericalValue[1]; in y: NumericalValue[0..1]; return : NumericalValue[1];}

   abstract function sum {in collection: NumericalValue[0..*] ordered; return : NumericalValue[1];}
   abstract function product {in collection: NumericalValue[0..*] ordered; return : NumericalValue[1];}
}

130  Last changed: 2024-07 (import visibility)                                                Release 2026-04
```

### LAYOUT PDF PAGE 131

```text
     Complex Functions

standard library package ComplexFunctions {
     public import ScalarValues::*;

feature i: Complex[1] = rect(0.0, 1.0);

function rect{in re: Real[1]; in im: Real[1]; return : Complex[1];}
function polar{in abs: Real[1]; in arg: Real[1]; return : Complex[1];}
function re{in x: Complex[1]; return : Real[1];}
function im {in x: Complex[1]; return : Real[1];}

function abs specializes NumericalFunctions::abs {in x: Complex[1]; return : Real[1];}
function {in x: Complex[1]; return : Real[1];}
function '+' specializes NumericalFunctions::'+’

     {in x: Complex[1]; in y: Complex[0..1]; return : Complex[1];
function '-' specializes NumericalFunctions::'-'

     {in x: Complex[1]; in y: Complex[0..1]; return : Complex[1];
function '*' specializes NumericalFunctions::'*'

     {in x: Complex[1]; in y: Complex[1]; return : Complex[1];
function '/' specializes NumericalFunctions::'/'

     {in x: Complex[1]; in y: Complex[1]; return : Complex[1];
function '**' specializes NumericalFunctions::'**'

     {in x: Complex[1]; in y: Complex[1]; return : Complex[1];
function '^' specializes NumericalFunctions::'^'

     {in x: Complex[1]; in y: Complex[1]; return : Complex[1];
function '==' specializes DataFunctions::'=='

     {in x: Complex[1]; in y: Complex[1]; return : Complex[1];

function ToString specializes BaseFunctions::ToString {in x: Complex[1]; return : String[1];}
function ToComplex {in x: String[1]; return : Complex[1];}

     function sum specializes NumericalFunctions::sum {in collection: Complex[0..*]; return : Complex[1];}
     function product specializes NumericalFunctions::product {in collection: Complex[0..*]; return : Complex[1];}
}

131  Last changed: 2024-07 (import visibility)                                                 Release 2026-04
```

### LAYOUT PDF PAGE 132

```text
     Real Functions

standard library package RealFunctions {
     public import ScalarValues::*;
     function abs specializes ComplexFunctions::abs {in x: Real[1]; return : Real[1];}
     function '+' specializes ComplexFunctions::'+’ {in x: Real[1]; in y: Real[0..1]; return: Real[1];}
     function '-' specializes ComplexFunctions::'-' {in x: Real[1]; in y: Real[0..1]; return: Real[1];}
     function '*' specializes ComplexFunctions::'*' {in x: Real[1]; in y: Real[1]; return: Real[1];}
     function '/' specializes ComplexFunctions::'/' {in x: Real[1]; in y: Real[0..1]; return: Real[1];}
     function '**' specializes ComplexFunctions::'**' {in x: Real[1]; in y: Real[0..1]; return: Real[1];}
     function '^' specializes ComplexFunctions::'^' {in x: Real[1]; in y: Real[0..1]; return: Real[1];}
     function '<' specializes ComplexFunctions::'<'
          {in x: Real[1]; in y: Real[0..1]; return: Boolean[1];}
     function '>' specializes ComplexFunctions::'>'
          {in x: Real[1]; in y: Real[0..1]; return: Boolean[1];}
     function '<=' specializes ComplexFunctions::'<='
          {in x: Real[1]; in y: Real[0..1]; return: Boolean[1];}
     function '>=' specializes ComplexFunctions::'>='
          {in x: Real[1]; in y: Real[0..1]; return: Boolean[1];}
     function max specializes ComplexFunctions::max {in x: Real[1]; in y: Real[0..1]; return: Real[1];}
     function min specializes ComplexFunctions::min {in x: Real[1]; in y: Real[0..1]; return: Real[1];}
     function '==' specializes ComplexFunctions::'==‘
          {in x: Real[1]; in y: Real[0..1]; return: Boolean[1];}
     function sqrt {in x: Real[1]; return : Real[1];}
     function floor {in x: Real[1]; return : Integer[1];}
     function round {in x: Real[1]; return : Integer[1];}

     function ToString specializes ComplexFunctions::ToString {in x: Real[1]; return : String[1];}
     function ToInteger {in x: Real[1]; return : Integer[1];}
     function ToRational {in x: Real[1]; return : Rational[1];}
     function ToReal {in x: String[1]; return : Real[1];}
     function ToComplex(x: Real[1]): Complex;
     function sum specializes ComplexFunctions::sum {in collection: Real[0..*]; return : Real[1];}
     function product specializes ComplexFunctions::product {in collection: Real[0..*]; return : Real[1];}
}

132  Last changed: 2024-07 (import visibility)  Release 2026-04
```

### LAYOUT PDF PAGE 133

```text
     Rational Functions

standard library package RationalFunctions {
     public import ScalarValues::*;

function rat {in numer: Integer[1]; in denum: Integer[1]; return : Rational[1];}
function numer{in rat: Rational[1]; return : Integer[1];}
function denom {in rat: Rational[1]; return : Integer[1];}

function abs specializes RealFunctions::abs {in x: Rational[1]; return : Rational[1];}
function '+' specializes RealFunctions::’+’ {in x: Rational[1]; in y: Rational[0..1]; return : Rational[1];}
function '-' specializes RealFunctions::'-' {in x: Rational[1]; in y: Rational[0..1]; return : Rational[1];}
function '*' specializes RealFunctions::'*' {in x: Rational[1]; in y: Rational[1]; return : Rational[1];}
function '/' specializes RealFunctions::'/' {in x: Rational[1]; in y: Rational[1]; return : Rational[1];}
function '**' specializes RealFunctions::'**' {in x: Rational[1]; in y: Rational[1]; return : Rational[1];}
function '^' specializes RealFunctions::'^' {in x: Rational[1]; in y: Rational[1]; return : Rational[1];}
function '<' specializes RealFunctions::'<‘ {in x: Rational[1]; in y: Rational[1]; return : Boolean[1];
function '>' specializes RealFunctions::'>' {in x: Rational[1]; in y: Rational[1]; return : Boolean[1];
function '<=' specializes RealFunctions::'<=' {in x: Rational[1]; in y: Rational[1]; return : Boolean[1];
function '>=' specializes RealFunctions::'>=' {in x: Rational[1]; in y: Rational[1]; return : Boolean[1];
function max specializes RealFunctions::max {in x: Rational[1]; in y: Rational[1]; return : Boolean[1];
function min specializes RealFunctions::min {in x: Rational[1]; in y: Rational[1]; return : Boolean[1];
function '==' specializes RealFunctions::'==' {in x: Rational[1]; in y: Rational[1]; return : Boolean[1];

function gcd {in x: Rational[1]; in y: Rational[0..1]; return : Integer[1];}
function floor {in x: Rational[1]; return : Integer[1];}
function round {in x: Rational[1]; return : Integer[1];}

function ToString specializes RealFunctions::ToString {in x: Rational[1]; return : String[1];}
function ToInteger {in x: Rational[1]; return : Integer[1];}
function ToRational {in x: String[1]; return : Rational[1];}

     function sum specializes RealFunctions::sum {in collection: Rational[0..*]; return : Rational[1];}
     function product specializes RealFunctions::product {in collection: Rational[0..*]; return : Rational[1];}
}

133  Last changed: 2024-07 (import visibility)                                                  Release 2026-04
```

### LAYOUT PDF PAGE 134

```text
     Integer Functions

standard library package IntegerFunctions {
     public import ScalarValues::*;

     function abs specializes RationalFunctions::abs {in x: Integer[1]; return : Natural[1];}
     function '+' specializes RationalFunctions::'+' {in x: Integer[1]; in y: Integer[0..1]; return : Integer[1];}
     function '-' specializes RationalFunctions::'-' {in x: Integer[1]; in y: Integer[0..1]; return : Integer[1];}
     function '*' specializes RationalFunctions::'*' {in x: Integer[1]; in y: Integer[1]; return : Integer[1];}
     function '/' specializes RationalFunctions::'/' {in x: Integer[1]; in y: Integer[1]; return : Rational[1];}
     function '**' specializes RationalFunctions::'**' {in x: Integer[1]; in y: Natural[1]; return : Integer[1];}
     function '^' specializes RationalFunctions::'^' {in x: Integer[1]; in y: Natural[1]; return : Integer[1];}
     function '%' specializes NumericalFunctions::'%' {in x: Integer[1]; in y: Integer[1]; return : Integer[1];}
     function '<' specializes RationalFunctions::'<' {in x: Integer[1]; in y: Integer[1]; return : Boolean[1];}
     function '>' specializes RationalFunctions::'>' {in x: Integer[1]; in y: Integer[1]; return : Boolean[1];}
     function '<=' specializes RationalFunctions::'<=' {in x: Integer[1]; in y: Integer[1]; return : Boolean[1];}
     function '>=' specializes RationalFunctions::'>=' {in x: Integer[1]; in y: Integer[1]; return : Boolean[1];}

     function max specializes RationalFunctions::max {in x: Integer[1]; in y: Integer[1]; return : Integer[1];}
     function min specializes RationalFunctions::min {in x: Integer[1]; in y: Integer[1]; return : Integer[1];}

     function '==' specializes DataFunctions::'==' {in x: Integer[0..1]; in y: Integer[0..1]; return : Boolean[1];}
     function '..' specializes ScalarFunctions::'..’

          {in lower: Integer[1]; in upper: Integer[1]; return : Integer[0..*];}
     function ToString specializes RationalFunctions::ToString {in x: Integer[1]; return : String[1];}
     function ToNatural {in x: Integer[1]; return : Natural[1];}
     function ToInteger {in x: String[1]; return : Integer[1];}
     function sum specializes RationalFunctions::sum {in collection: Integer[0..*]; return : Integer[1];}
     function product specializes RationalFunctions::product {in collection: Integer[0..*]; return : Integer[1];}
}

134  Last changed: 2024-07 (import visibility)  Release 2026-04
```

### LAYOUT PDF PAGE 135

```text
     Natural Functions

standard library package NaturalFunctions {
     public import ScalarValues::*;

     function '+' specializes IntegerFunctions::'+' {in x: Natural[1]; in y: Natural[0..1]; return : Natural[1];}
     function '*' specializes IntegerFunctions::'*' {in x: Natural[1]; in y: Natural[1]; return : Natural[1];}
     function '/' specializes IntegerFunctions::'/' {in x: Natural[1]; in y: Natural[1]; return : Natural[1];}
     function '%' specializes IntegerFunctions::'%' {in x: Natural[1]; in y: Natural[1]; return : Natural[1];}
     function '<' specializes IntegerFunctions::'<' {in x: Natural[1]; in y: Natural[1]; return : Boolean[1];}
     function '>' specializes IntegerFunctions::'>' {in x: Natural[1]; in y: Natural[1]; return : Boolean[1];}
     function '<=' specializes IntegerFunctions::'<=' {in x: Natural[1]; in y: Natural[1]; return : Boolean[1];}
     function '>=' specializes IntegerFunctions::'>=' {in x: Natural[1]; in y: Natural[1]; return : Boolean[1];}

     function max specializes IntegerFunctions::max {in x: Natural[1]; in y: Natural[1]; return : Natural[1];}
     function min specializes IntegerFunctions::min { n x: Natural[1]; in y: Natural[1]; return : Natural[1];}

     function '==' specializes IntegerFunctions::'==‘
          {in x: Natural[0..1]; in y: Natural[0..1]; return : Boolean[1];}

     function ToString specializes IntegerFunctions::ToString {in x: Natural[1]; return : String[1];}
     function ToNatural{in x: String[1]; return : Natural[1];}
}

135  Last changed: 2024-07 (import visibility)  Release 2026-04
```

### LAYOUT PDF PAGE 136

```text
     Trigonometric Functions

     standard library package TrigFunctions {
         public import ScalarValues::Real;

         feature pi : Real;
         inv piPrecision {

            RealFunctions::round(pi * 1E20) == 314159265358979323846.0
         }

         function deg {in theta_rad : Real[1];return : Real[1];}
         function rad {in theta_deg : Real; return : Real[1];}

         datatype UnitBoundedReal :> Real {
            inv unitBound { -1.0 <= that & that <= 1.0 }

         }
         function sin {in theta : Real[1]; return : UnitBoundedReal[1];}
         function cos {in theta : Real[1]; return : UnitBoundedReal[1];}
         function tan {in theta : Real[1]; return : Real;}
         function cot {in theta : Real; return : Real;}
         function arcsin {in x : UnitBoundedReal[1]; return : Real[1];}
         function arccos {in x : UnitBoundedReal[1]; return : Real[1];}
         function arctan {in x : Real[1]; return : Real[1];}
     }

136  Last changed: 2024-07 (import visibility)  Release 2026-04
```

### LAYOUT PDF PAGE 137

```text
     Sequence Functions (1)

standard library package SequenceFunctions {
     …
     function equals {in x: Anything[0..*] ordered nonunique; in y: Anything[0..*] ordered nonunique;
          return : Boolean[1];
     }
     function same {in x: Anything[0..*] ordered nonunique; in y: Anything[0..*] ordered nonunique;
          return : Boolean[1];
     }

     function size {in seq: Anything[0..*] nonunique; return : Natural[1];}
     function isEmpty {in seq: Anything[0..*] nonunique; return : Boolean[1];}
     function notEmpty {in seq: Anything[0..*] nonunique; return : Boolean[1];}

     function includes {in seq1: Anything[0..*] nonunique; in seq2: Anything[0..*] nonunique;
          return : Boolean[1];

     }
     function excludes {in seq1: Anything[0..*] nonunique; in seq2: Anything[0..*] nonunique;

          return : Boolean[1];
     }
     function including {in seq: Anything[0..*] ordered nonunique; in values: Anything[0..*] ordered nonunique;

          return : Anything[0..*] ordered nonunique;
     }
     function includingAt{in seq: Anything[0..*] ordered nonunique; in values: Anything[0..*] ordered nonunique;

          in index: Positive[1]; return : Anything[0..*] ordered nonunique;
     }
     function excluding {in seq: Anything[0..*] ordered nonunique; in values: Anything[0..*] ordered nonunique;

          return : Anything[0..*] ordered nonunique;
     }
     function excludingAt{in seq: Anything[0..*] ordered nonunique; in values: Anything[0..*] ordered nonunique;

          in index: Positive[1]; return : Anything[0..*] ordered nonunique;
     }
     …

137  Last changed: 2026=04 (removed “ordered” from input to “size” through  Release 2026-04

     “excludes”)
```

### LAYOUT PDF PAGE 138

```text
     Sequence Functions (2)

     standard library package SequenceFunctions {
          …

          function head {in seq: Anything[0..*] ordered nonunique;
               return : Anything[0..1];

          }
          function tail {in seq: Anything[0..*] ordered nonunique ;

               return : Anything[0..*] ordered nonunique;
          }
          function last {in seq: Anything[0..*] ;

               return : Anything[0..1];
          }

          function '#' specializes BaseFunctions::'#' {
               in seq: Anything[0..*] ordered nonunique; in index: Natural[1]; return : Anything[0..1];

          }

          behavior add {
               inout seq: Anything[0..*] ordered nonunique; in values: Anything[0..*] ordered nonunique;

          }
          behavior addAt {

               inout seq: Anything[0..*] ordered nonunique; in values: Anything[0..*] ordered nonunique;
               in index: Positive[1];
          }
          behavior remove{
               inout seq: Anything[0..*] ordered nonunique; in values: Anything[0..*];
          }
          behavior removeAt{
               inout seq: Anything[0..*] ordered nonunique;
               in startIndex: Positive[1]; in endIndex: Positive[1] default startIndex;
          }
     }

138  Last changed: 2023-02 (changed '[' to '#')  Release 2026-04
```

### LAYOUT PDF PAGE 139

```text
     Collection Functions

standard library package CollectionFunctions {
    …
    public import Collections::*;

    function '==' specializes BaseFunctions::'==‘
        {in col1: Collection[0..1]; in col2: Collection[0..1]; return : Boolean[1];}

    function size {in col: Collection[1]; return : Natural[1];}
    function isEmpty {in col: Collection[1]; return : Boolean[1];}
    function notEmpty {in col: Collection[1]; return : Boolean[1];}
    function contains {in col: Collection[1]; in values: Anything[*]; return : Boolean[1];}
    function containsAll {in col1: Collection[1]; in col2: Collection[2]; return : Boolean[1];}
    function head {in col: OrderedCollection[1]; return : Anything[0..1];}
    function tail {in col: OrderedCollection[1]; return : Anything[0..*] ordered nonunique;}
    function last {in col: OrderedCollection[1]; return : Anything[0..1];}

    function '#' specializes BaseFunctions::'#‘
        {in col: OrderedCollection[1]; in index: Positive[1]; return : Anything[0..1];}

    function 'array#' specializes BaseFunctions::'#‘
        {in arr: Array[1]; in indexes: Positive[n] ordered nonunique; return : Anything[0..1];}

}

139  Last changed: 2024-07 (import visibility)  Release 2026-04
```

### LAYOUT PDF PAGE 140

```text
     Vector Functions (1)

standard library package VectorFunctions {
   …

   public import VectorValues::*;

   abstract function isZeroVector {in v: VectorValue[1]; return : Boolean[1];}
   abstract function '+' specializes DataFunctions::'+'

          {in v: VectorValue[1]; in w: VectorValue[0..1]; return u: VectorValue[1];}
   abstract function '-' specializes DataFunctions::'-'

          {in v: VectorValue[1]; in w: VectorValue[0..1]; return u: VectorValue[1];}

   function VectorOf {in components: NumericalValue[1..*] ordered nonunique;
           return : NumericalVectorValue[1];}

   abstract function scalarVectorMult specializes DataFunctions::'*’
          {in x: NumericalValue[1]; in v: NumericalVectorValue[1]; return w: NumericalVectorValue[1];

   alias '*' for scalarVectorMult;
   abstract function vectorScalarMult specializes DataFunctions::'*’

          {in v: NumericalVectorValue[1]; in x: NumericalValue[1]; return : NumericalVectorValue[1];}
   abstract function vectorScalarDiv specializes DataFunctions::'/’

          {in v: NumericalVectorValue[1]; in x: NumericalValue[1]; return : NumericalVectorValue[1];}
   abstract function inner specializes DataFunctions::'*’

          {in v: NumericalVectorValue[1]; in w: NumericalVectorValue[1]; return x: NumericalValue[1];}
   abstract function norm {in v: NumericalVectorValue[1]; return l : NumericalValue[1];}
   abstract function angle {in v: NumericalVectorValue[1]; in w: NumericalVectorValue[1];

          return theta: NumericalValue[1];}

   …
}

140  Last changed: 2024-07 (import visibility)  Release 2026-04
```

### LAYOUT PDF PAGE 141

```text
     Vector Functions (2)

standard library package VectorFunctions {
   …

   function CartesianVectorOf
          {in components: NumericalValue[1..*] ordered nonunique; return : CartesianVectorValue[1];}

   function CartesianThreeVectorOf specializes CartesianVectorOf
          {in components: Real[3] ordered nonunique; return : CartesianVectorValue[1];}

   function isCartesianZeroVector specializes isZeroVector
          {in v: CartesianVectorValue[1]; return : Boolean[1];}

   function 'cartesian+' specializes '+'
          {in v: CartesianVectorValue[1]; in w: CartesianVectorValue[0..1]; return: CartesianVectorValue[1];

   function 'cartesian-' specializes '-'
          {in v: CartesianVectorValue[1]; in w: CartesianVectorValue[0..1]; return: CartesianVectorValue[1];

   function cartesianScalarVectorMult specializes scalarVectorMult
          {in x: Real[1]; in v: CartesianVectorValue[1]; return : CartesianVectorValue[1];}

   function cartesianVectorScalarMult specializes vectorScalarMult
          {in v: CartesianVectorValue[1]; in x: Real[1]; return : CartesianVectorValue[1];}

   function cartesianInner specializes inner
          {in v: CartesianVectorValue[1]; in w: CartesianVectorValue[0..1]; return : Real[1];}

   function cartesianNorm specializes norm
          {in v: CartesianVectorValue[1]; return : NumericalValue[1];}

   function cartesianAngle specializes angle
          {in v: CartesianVectorValue[1]; in w: CartesianVectorValue[0..1]; return : Real[1];}

   function sum {in coll: CartesianThreeVectorValue[*]; return : CartesianThreeVectorValue[0..1];}
}

141  Last changed: 2022-09 (standard library package)  Release 2026-04
```

### LAYOUT PDF PAGE 142

```text
     Control Functions

standard library package ControlFunctions {
     private import Base::Anything;
     private import ScalarValues::ScalarValue;

abstract function 'if’ {in test: Boolean[1];
     in expr thenValue[0..1] {return : Anything[0..*] ordered nonunique;}
     in expr elseValue[0..1] {return : Anything[0..*] ordered nonunique;}
     return : Anything[0..*] ordered nonunique;}

abstract function ‘??’ {in firstValue: Anything[0..*];
     in expr secondValue[0..1] {return : Anything[0..*] ordered nonunique;}
     return : Anything[0..*] ordered nonunique;}

function 'and’
     {in firstValue: Anything[0..*]; in expr secondValue[0..1] {return : Boolean[1];} return : Boolean[1];}

function 'or’
     {in firstValue: Anything[0..*]; in expr secondValue[0..1] {return : Boolean[1];} return : Boolean[1];}

function 'implies’
     {in firstValue: Anything[0..*]; in expr secondValue[0..1] {return : Boolean[1];} return : Boolean[1];}

     abstract function collect {in collection: Anything[0..*] ordered nonunique;
          in expr mapper[0..*] (argument: Anything[1]): Anything[0..*] ordered nonunique;
          return : Anything[0..*] ordered nonunique {

     }
     abstract function select { in collection: Anything[0..*] ordered nonunique;

          in expr selector[0..*] (argument: Anything[1]): Boolean[1];
          return : Anything[0..*] ordered nonunique {
     }
     abstract function reject { in collection: Anything[0..*] ordered nonunique;
          in expr rejector[0..*] (argument: Anything[1]): Boolean[1];
          return : Anything[0..*] ordered nonunique {
     }
     …
}

142  Last changed: 2025-02 (corrected 'and', 'or', 'implies' parameters)                   Release 2026-04
```

### LAYOUT PDF PAGE 143

```text
                                      Occurrence Functions

                                                                    Test whether two occurrences represent

standard library package OccurrenceFunctions {                      different portions of the same entity (i.e.,
     …                                                              whether they have the same "identity").
     function '===' specializes BaseFunctions::'===' {              Can be invoked using the === operator.
          in x: Occurrence[0..1]; in y: Occurrence[0..1];

        return : Boolean[1];

   }                                  Test whether a performance
   function isDuring {                of this function happens
                                      during the input occurrence.
        in occ: Occurrence[1];
        return : Boolean[1];
   }
   function create {

        inout occ: Occurrence[1];
        return : Occurrence[1];

   }                                  Create or destroy an
   function destroy {                 occurrence.

        inout occ: Occurrence[0..1];

        return : Occurrence[0..1];                                               Add a newly created instance
   }                                                                             to a group of occurrences.
   function addNew {

        inout group: Occurrence[0..*] nonunique; inout occ: Occurrence[1];

        return : Occurrence[1];
   }

   function addNewAt {

        inout group: Occurrence[0..*] ordered nonunique; inout occ: Occurrence[1]; in index: Positive[1];
        return : Occurrence[1];

   }                                                                             Remove an instance from
   behavior removeOld {                                                          a group of occurrences

        inout group: Occurrence[0..*] nonunique; inout occ: Occurrence[0..1];

   }                                                                             and destroy it.
   behavior removeOldAt {

        inout group: Occurrence[0..*] ordered nonunique; in index: Positive[1];

   }

}

   143                                Last changed: 2022-09 (new)                Release 2026-04
```

### LAYOUT PDF PAGE 144

```text
     Systems Library
     (selected models)

144                     Release 2026-04
```

### LAYOUT PDF PAGE 145

```text
                      Standard View Definitions

     standard library package StandardViewDefinitions {
            view def <gv> GeneralView;
            view def <iv> InterconnectionView;
            view def <afv> ActionFlowView specializes InterconnectionView;
            view def <stv> StateTransitionView specializes InterconnectionView;
            view def <sv> SequenceView;
            view def <gev> GeometryView;
            view def <gv> GridView;
            view def <bv> BrowserView;

     }

145  Last changed: 2024-07 (updated to latest version)  Release 2026-04
```

### LAYOUT PDF PAGE 146

```text
     Metadata Domain Library

146                           Release 2026-04
```

### LAYOUT PDF PAGE 147

```text
                                    Risk Metadata

 General risk level in terms of     standard library package RiskMetadata {
 probability and impact.                private import ScalarValues::Real;
                                        attribute def Level :> Real {
 Standard low, medium and                   assert constraint { that >= 0.0 and that <= 1.0 }
 high risk levels.                      }
                                        enum def LevelEnum :> Level {
 To be used to annotate                     low = 0.25;
 model elements as to their                 medium = 0.50;
 risk level in typical risk areas.          high = 0.75;
                                        }
147                                     attribute def RiskLevel {
                                            attribute probability : Level;
                                            attribute impact : Level [0..1];
                                        }
                                        enum def RiskLevelEnum :> RiskLevel {
                                            low = RiskLevel(probability = LevelEnum::L);
                                            medium = RiskLevel(probability = LevelEnum::M);
                                            high = RiskLevel(probability = LevelEnum::H);
                                        }
                                        metadata def Risk {
                                            attribute totalRisk : RiskLevel [0..1];
                                            attribute technicalRisk : RiskLevel [0..1];
                                            attribute scheduleRisk : RiskLevel [0..1];
                                            attribute costRisk : RiskLevel [0..1];
                                        }

                                    }

                                    Last changed: 2024-07 (import visibility)  Release 2026-04
```

### LAYOUT PDF PAGE 148

```text
                                   Modeling Metadata

                                standard library package ModelingMetadata {

                                   …

                                   enum def StatusKind {

                                      open;

                                      tbd; // To be determined

                                      tbr; // To be resolved

     To be used to annotate           tbc; // To be confirmed
     model elements with
     status information.              done;

     To be used to give a             closed;
     rationale for a model
     element.                      }

     Generic issue annotation.     metadata def StatusInfo {

     To be used to model a            attribute originator : String [0..1];
     dependency in which
     source elements refine           attribute owner : String [0..1];               This is an optional reference
     target elements.
                                      attribute status : StatusKind;
148
                                      attribute risk : Risk [0..1];                  to a feature that further

                                   }                                                 explains this rationale (e.g.,

                                   metadata def Rationale {                          a trade study analysis).
                                       attribute text : String;

                                      ref explanation : Anything [0..1];

                                   }

                                   metadata def Issue {

                                      attribute text : String;

                                   }

                                   metadata def <refinement> Refinement {

                                         :>> annotatedElement : SysML::Dependency;

                                      }

                                }

                                   Last changed: 2022-09 (standard library package)  Release 2026-04
```

### LAYOUT PDF PAGE 149

```text
                          Parameters of Interest Metadata

Semantic metadata for     standard library package ParametersOfInterestMetadata {
identifying an attribute      private import Metaobjects::SemanticMetadata;
as a measure of
effectiveness.                attribute measuresOfEffectiveness[*] nonunique;
                              attribute measuresOfPerformance[*] nonunique;
Semantic metadata for
identifying an attribute      metadata def <moe> MeasureOfEffectiveness :> SemanticMetadata {
as a measure of                   :>> annotatedElement : SysML::Usage;
performance.                      :>> baseType = measuresOfEffectiveness meta SysML::Usage;

                              }

                              metadata def <mop> MeasureOfPerformance :> SemanticMetadata {
                                  :>> annotatedElement : SysML::Usage;
                                  :>> baseType = measuresOfPerformance meta SysML::Usage;

                              }
                          }

149                       Last changed: 2022-09 (replaced "as" with "meta")  Release 2026-04
```

### LAYOUT PDF PAGE 150

```text
                               Image Metadata

Provides data             standard library package ImageMetadata {     Binary data for the image.
necessary for the             private import ScalarValues::String;
physical definition of a                                               Binary data character
graphical image.              attribute def Image {                    encoding (e.g., "base64").
                                  attribute content : String[0..1];
                                                                       MIME type of the content.
                               attribute encoding : String[0..1];
                                                                       URI for image content,
To be used to annotate            attribute type : String[0..1];       alternative to embedding
a model element with                                                   it in the content attribute.
an image.                         attribute location : String[0..1];
                              }
Full-sized image for
rendering the                 metadata def Icon {
annotated element.                attribute fullImage : Image[0..1];

                                  attribute smallImage : Image[0..1];
                              }
                          }

     Smaller image for use as
     an adornment or marker.

150                            Last changed: 2022-11 (private import)  Release 2026-04
```

### LAYOUT PDF PAGE 151

```text
     Analysis Domain Library

151                           Release 2026-04
```

### LAYOUT PDF PAGE 152

```text
                                       Trade Studies

                                                 An EvaluationFunction is a

standard library package TradeStudies {          calculation that evaluates a
    private import Base::Anything;               TradeStudy alternative.
    private import ScalarValues::*;

   private import ScalarFunctions::*;

   abstract calc def EvaluationFunction(alternative) result : ScalarValue[1];

   abstract requirement def TradeStudyObjective {                 A TradeStudyObjective is the
        subject selectedAlternative : Anything;

      in ref alternatives : Anything[1..*];                       base definition for the objective

        in calc eval : EvaluationFunction;                        of a TradeStudy, requiring the
        out attribute best : ScalarValue;                         selectedAlternative to have best
        require constraint { eval(selectedAlternative) == best }  evaluation according to a given
   }

   requirement def MinimizeObjective :> TradeStudyObjective {     EvaluationFunction.
        …

      attribute :>> best = alternatives->minimize {in x; eval(x)};

   }

   requirement def MaximizeObjective :> TradeStudyObjective {

      …

      attribute :>> best = alternatives->maximize {in x; eval(x)};

   }                                                              A TradeStudy is an analysis case whose
   abstract analysis def TradeStudy {                             subject is a set of alternatives and

        subject studyAlternatives : Anything[1..*];

      abstract calc evaluationFunction : EvaluationFunction;      whose result is a selection of one of
      objective tradeStudyObjective : TradeStudyObjective {       those alternatives, based on a given
                                                                  EvaluationFunction such that it satisfies
           subject :>> selectedAlternative;
           in ref :>> alternatives = studyAlternatives;

         in calc :>> eval = evaluationFunction;                   the objective of the TradeStudy.

      }

      return selectedAlternative : Anything =

         studyAlternatives->selectOne {in ref a; tradeStudyObjective(selectedAlternative = a)};

}

152      Last changed: 2025-07 (“fn” changed to “eval”)                                Release 2026-04
```

### LAYOUT PDF PAGE 153

```text
     Analysis Tooling Annotations

     standard library package AnalysisTooling {
        private import ScalarValues::*;

     metadata def ToolExecution {                      ToolExecution metadata
         attribute toolName : String;                  identifies an external analysis
         attribute uri : String;                       tool to be used to implement
                                                       the annotated action.
     }

        metadata def ToolVariable {    ToolVariable metadata is used in the
            attribute name : String;   context of an action that has been
                                       annotated with ToolExecution
        }                              metadata. It is used to annotate a
     }                                 parameter or other feature of the
                                       action with the name of the variable
                                       in the tool that is to correspond to
                                       the annotated feature.

153  Last changed: 2022-09 (standard library package)  Release 2026-04
```

### LAYOUT PDF PAGE 154

```text
     State Space Representation (1)

standard library package StateSpaceRepresentation {
     private import ISQ::DurationValue;
     private import Quantities::VectorQuantityValue;
     private import VectorCalculations::*;

abstract attribute def StateSpace :> VectorQuantityValue;
abstract attribute def Input :> VectorQuantityValue;
abstract attribute def Output :> VectorQuantityValue;
abstract calc def GetNextState

    {in input: Input; in stateSpace: StateSpace; in timeStep: DurationValue; return : StateSpace;}
abstract calc def GetOutput

    {in input: Input; in stateSpace: StateSpace; return : Output;}
abstract action def StateSpaceEventDef;
action def ZeroCrossingEventDef :> StateSpaceEventDef;
item def StateSpaceItem;

abstract action def StateSpaceDynamics {              StateSpaceDynamics is the simplest

     in attribute input: Input;                       form of state space representation,

     abstract calc getNextState: GetNextState;        and getNextState directly computes
     abstract calc getOutput: GetOutput;              the stateSpace of the next timestep.
     attribute stateSpace: StateSpace;

     out attribute output: Output = getOutput(input, stateSpace);

}

abstract attribute def StateDerivative :> VectorQuantityValue { … }

abstract calc def GetDerivative

     {in input: Input; in stateSpace: StateSpace; return : StateDerivative;}

abstract calc def Integrate {in getDerivative: GetDerivative; in input: Input;

     in initialState: StateSpace; in timeInterval: DurationValue; return result: StateSpace;}

…

154                              Last changed: 2022-11 (private import)         Release 2026-04
```

### LAYOUT PDF PAGE 155

```text
           State Space Representation (2)

                                                        ContinuousStateSpaceDynamics

                                                        represents continuous behavior. The

                                                        derivative needs to return a time

…                                                       derivative of stateSpace, i.e. dx/dt.

abstract action def ContinuousStateSpaceDynamics :> StateSpaceDynamics {

     abstract calc getDerivative: GetDerivative;

     calc :>> getNextState: GetNextState {

        calc integrate: Integrate {

           in derivative = ContinuousStateSpaceDynamics::getDerivative;

           in input = GetNextState::input;

           in initialState = GetNextState::stateSpace;

           in timeInterval = GetNextState::timeStep;

           return resultState = result;

        }

     }

     event occurrence zeroCrossingEvents[0..*] : ZeroCrossingEventDef;

}

                                                                               DiscreteStateSpaceDynamics

abstract calc def GetDifference {                       represents discrete behavior.

     in input: Input; in stateSpace: StateSpace;        getDifference returns the difference
     return : StateSpace;}                              of the stateSpace for each timestep.

     abstract action def DiscreteStateSpaceDynamics :> StateSpaceDynamics {
         abstract calc getifference: GetDifference;
         calc :>> getNextState: GetNextState {
              attribute diff: StateSpace = getDifference(input, stateSpace);
              stateSpace + diff
         }

     }
}

155        Last changed: 2022-09 (standard library package)                                                Release 2026-04
```

### LAYOUT PDF PAGE 156

```text
                                       Sampled Functions

                                                                                         SamplePair is a key-value pair

                                                                                         of a domain-value and a

                                    standard library package SampledFunctrainognes-v{alue, used as a sample

SampleFunction is a variable-size, …                                                     element in SampledFunction.

ordered collection of SamplePair       attribute def SamplePair :> KeyValuePair {
elements representing a discretely         attribute domainValue :>> key;

sampled mathematical function.             attribute rangeValue :>> val;
                                       }

                                       attribute def SampledFunction :> OrderedMap {

     Domain and Range return all       attribute samples: SamplePair[0..*] ordered :>> elements;
     the domain values and range
     values of a sampled function.         assert constraint { … }                       The function is constrained
                                       }                                                 to be strictly increasing or

                                       calc def Domain{in fn : SampledFunctiosnt;rictly decreasing.

                                       return : Anything[0..*] = fn.samples.domainValue;}

Sample a calculation on                calc def Range{in fn : SampledFunction;
given domain values to                     return : Anything[0..*] = fn.samples.rangeValue;}

create a SampledFunction.              calc def Sample {in calc calculation {in x;}

                                       in attribute domainValues [0..*];

                                       return sampling;

     Interpolate a

     SampledFunction to                calc def Interpolate {in attribute fn : SampledFunction;
     compute a result for a                in attribute value;
     given domain value.                   return attribute result;}

                                       calc interpolateLinear : Interpolate { … }

                                    }

156                                    Last changed: 2022-09 (standard library package)  Release 2026-04
```

### LAYOUT PDF PAGE 157

```text
     Cause and Effect Domain Library

157                                   Release 2026-04
```

### LAYOUT PDF PAGE 158

```text
                                Causation Connections

A connection between one        standard library package CausationConnections {
or more cause occurrences           abstract occurrence causes[*];
and one or more effect              abstract occurrence effects[*];
occurrences. Specializations
add ends for specific causes        abstract connection def Multicausation {
and effects.                            abstract constant ref occurrence causes[1..*]
                                             :>> causes :> participant;
A binary connection                     abstract constant ref occurrence effects[1..*]
between a single cause and                   :>> effects :> participant;
a single effect. (But a single
cause can separately have           …
multiple effects, and a             }
single effect can separately        abstract connection multicausations : Multicausation[*] {
have multiple causes.)
                                    connection def Causation :> Multicausation {
                                        end theCauses[*] occurrence theCause
                                             :>> causes :>> source;
                                        end theEffects[*] occurrence theEffect
                                             :>> effects :>> target;

                                    }
                                    abstract connection causations : Causation[*]

                                        :> multicausations;
                                }

158                             Last changed: 2025-07 (connection feature declarations)  Release 2026-04
```

### LAYOUT PDF PAGE 159

```text
                              Cause and Effect Metadata

   Used to tag the “cause”    standard library package CauseAndEffect {
   ends of a multicausation.      public import CausationConnections::*;
   Used to tag the “effect”       private import ScalarValues::*;
   ends of a multicausation.      private import Metaobjects::SemanticMetadata;
Additional metadata about         metadata def <cause> CauseMetadata :> SemanticMetadata {
a causation connection.               ref :>> annotatedElement : SysML::Usage;
                                      ref :>> baseType = causes meta SysML::Usage;
   Semantic metadata for          }
   multicausation.                metadata def <effect> EffectMetadata :> SemanticMetadata {
   Semantic metadata for              ref :>> annotatedElement : SysML::Usage;
   binary cauasation.                 ref :>> baseType = effects meta SysML::Usage;
                                  }
159                               metadata def CausationMetadata {
                                      ref :> annotatedElement : SysML::ConnectionDefinition;
                                      ref :> annotatedElement : SysML::ConnectionUsage;
                                      attribute isNecessary : Boolean default false;
                                      attribute isSufficient : Boolean default false;
                                      attribute probability : Real[0..1];
                                  }
                                  metadata def <multicausation> MulticausationSemanticMetadata
                                      :> CausationMetadata, SemanticMetadata {
                                      ref :>> baseType = multicausations meta SysML::Usage;
                                  }
                                  metadata def <causation> CausationSemanticMetadadata
                                      :> CausationMetadata, SemanticMetadata {
                                      ref :>> baseType = causations meta SysML::Usage;
                                  }

                              }

                              Last changed: 2024-07 (import visibility)  Release 2026-04
```

### LAYOUT PDF PAGE 160

```text
     Requirements Derivation Domain Library

160  Release 2026-04
```

### LAYOUT PDF PAGE 161

```text
     Derivation Connections

A connection between one             standard library package DerivationConnections {
original requirement and one             requirement originalRequirements[*];
or more derived requirements.            requirement derivedRequirements[*];
Specializations add ends for
specific original and derived            abstract connection def Derivation {
requirements.                                ref requirement originalRequirement[1]
                                                      :>> originalRequirements :> participant;
      Original requirement must not          ref requirement :>> derivedRequirements[1..*]
      be a derived requirement.                       :> participant;

      Whenever the original                  private assert constraint originalNotDerived { … }
      requirement is satisfied, all          private assert constraint originalImpliesDerived { … }
      the derived requirements           }
      must also be satisfied.
                                         abstract connection derivations : Derivation[*];
                                     }

161  Last changed: 2025-07 (removed participant redefinition)  Release 2026-04
```

### LAYOUT PDF PAGE 162

```text
     Requirement Derivation Metadata

     Used to tag the “original”  standard library package RequirementDerivation {
     ends of a derivation.           public import DerivationConnections::*;
                                     private import Metaobjects::SemanticMetadata;
     Used to tag the “derived”
     ends of a derivation.           metadata def <original> OriginalRequirementMetadata
                                         :> SemanticMetadata {
     Semantic metadata for               :> annotatedElement : SysML::Usage;
     requirement derivation.             :>> baseType = originalRequirements meta SysML::Usage;

                                     }

                                     metadata def <derive> DerivedRequirementMetadata
                                         :> SemanticMetadata {
                                         :> annotatedElement : SysML::Usage;
                                         :>> baseType = derivedRequirements meta SysML::Usage;

                                     }

                                     metadata def <derivation> DerivationMetadata
                                         :> SemanticMetadata {
                                         :> annotatedElement : SysML::ConnectionDefinition;
                                         :> annotatedElement : SysML::ConnectionUsage;
                                         :>> baseType = derivations meta SysML::Usage;

                                     }
                                 }

162                              Last changed: 2024-07 (import visibility)  Release 2026-04
```

### LAYOUT PDF PAGE 163

```text
     Quantities and Units Domain Library
                 (selected models)

163  Release 2026-04
```

### LAYOUT PDF PAGE 164

```text
     Quantities

                                                             A tensor quantity value           The numeric value of
                                                             represents the value of the most  the tensor is given as
standard library package Quantities { general kind of quantity, a tensor.                      an array of numbers .

abstract attribute def TensorQuantityValue :> Collections::Array {

     attribute num : ScalarValues::Number[1..*] ordered nonunique :>> elements;

     attribute mRef : UnitsAndScales::TensorMeasurementReference;

    attribute :>> dimensions = mRef::dimensions;                                               The value of a tensor
    …                                                                                          quantity is relative to a
}                                                                                              multi-dimensional tensor

abstract attribute def VectorQuantityValue :> TensorQuantityValue { measurement reference.

     attribute :>> mRef : UnitsAndScales::VectorMeasurementReference;

}

                                                                                                               A vector is a tensor with

abstract attribute def ScalarQuantityValue :> VectorQuantityValue { a single dimension.

     attribute :>> mRef : UnitsAndScales::ScalarMeasurementReference;

}

                                                                                                  A scalar is a vector with a single

abstract attribute tensorQuantities: TensorQuantityValue[*] noenleumnieqnut.eI;ts measurement
abstract attribute vectorQuantities: VectorQuantityValue[*] norenfuenrieqnuceem:a>y tbeenasmoreQausuarnetmietnites;
abstract attribute scalarQuantities: ScalarQuantityValue[*] nounnuitniif qthueesc:a>leviseactraotriQousacanltei. ties;

    alias TensorQuantityValue as QuantityValue;  A quantity is a usage of a
    alias tensorQuantities as quantity;          quantity value to represent
    …                                            a feature of something.
}

164  Last changed: 2026-04 (corrected suptype of ScalarQuantityValue)                          Release 2026-04
```

### LAYOUT PDF PAGE 165

```text
                                     Measurement References

                                  standard library package MeasurementReferences {

                                     attribute def TensorMeasurementReference :> Array {

                                        attribute mRefs : ScalarMeasurementReference[1..*] :>> elements;

                                        …

                                     }

A tensor measurement reference

is defined as an array of scalar     attribute def VectorMeasurementReference
measurement references, one                                                           :> TensorMeasurementReference {
for each element of the tensor.
                                         attribute :>> dimensions: Positive[0..1];
                                         …

                                     }

                                     attribute def ScalarMeasurementReference
                                                                                      :> VectorMeasurementReference {

                                         attribute :>> dimensions = ();
                                         …
                                     }

                                     attribute def CoordinateFrame :> VectorMeasurementReference {

                                        attribute transformation: CoordinateTransformation[0..1];

                                     }

                                     …

                                  }        A coordinate frame is a kind of vector measurement

                                           reference that can be located and oriented relative to

                                           another frame using a coordinate transformation.

165                                     Last changed: 2022-09 (standard library package)  Release 2026-04
```

### LAYOUT PDF PAGE 166

```text
                                    Units

A measurement unit is a
measurement scale defined as a standard library package Measurement {
sequence of unit power factors. …

A simple unit is a measurement      abstract attribute def MeasurementUnit
unit with no power factor                                                            :> ScalarMeasurementReference {
dependencies on other units.
                                        attribute unitPowerFactor : UnitPowerFactor[1..*] ordered;
                                        attribute unitConversion : UnitConversion[0..1];
                                    }

A derived unit is any unit that is  abstract attribute def SimpleUnit :> MeasurementUnit {
not simple.                             attribute redefines unitPowerFactor[1] {
                                            attribute redefines unit = SimpleUnit::self;
                                            attribute redefines exponent = 1;
                                        }

                                    }

                                    abstract attribute def DerivedUnit :> MeasurementUnit;

A unit power factor is a                attribute def UnitPowerFactor {
representation of a reference               attribute unit : MeasurementUnit;
unit raised to an exponent.                 attribute exponent : ScalarValues::Real;

                                        }
                                        …
                                    }

166                                 Last changed: 2022-09 (standard library package)  Release 2026-04
```

### LAYOUT PDF PAGE 167

```text
     International System of Quantities (ISQ)

                                                             The International System of Quantities

                                                             defines seven abstract units (length,

                                 standard library package ISQ { mass, time, electric current,

                                    import ISQBase::*;       temperature, amount of substance,

                                    import ISQSpaceTime::*;  luminous intensity) and many other

                                    …                        units derived from those.

                                 }

A length unit is a simple unit.  standard library package ISQBase {
                                    attribute def LengthUnit :> SimpleUnit {…}

A length value is a quantity        attribute def LengthValue :> ScalarQuantityValue {
value with a real magnitude             attribute redefines num : ScalarValues::Real;
and a length-unit scale.                attribute redefines mRef : LengthUnit;

                                    }

A length is a quantity with a       attribute length: LengthValue :> quantity;
length value.                       …
                                 }

                                 package ISQSpaceTime {      The ISQ standard (ISO 80000)
                                    import ISQBase::*;       is divided into several parts. For
                                    …                        example, Part 3 defines units
                                                             related to space and time.
                                 }

167                                 Last changed: 2022-09 (standard library package)  Release 2026-04
```

### LAYOUT PDF PAGE 168

```text
                          International System of Units /
                            Système International (SI)

The International         standard library package SI {                    A unit can be defined using
System of Units defines      public import ISQ::*;                         prefix-based conversion
base units for the seven     public import SIPrefixes::*;                  from a reference unit.
abstract ISQ unit types.
                             attribute <g> gram : MassUnit;

                          attribute <m> metre : LengthUnit;

Each unit declaration     attribute <kg> kilogram : MassUnit {
includes the full unit
name and its                 attribute redefines unitConversion : ConversionByPrefix {
abbreviation as an
identifier.                     attribute redefines prefix = kilo;

                                attribute redefines referenceUnit = g

                             }

                          }

                          attribute <s> second : TimeUnit;

                          attribute <A> ampere : ElectricCurrentUnit;

                          attribute <K> kelvin : ThermodynamicTemperaturAedUenriivted; unit can be

                          attribute <mol> mole : AmountOfSubstanceUnit; defined from an

                          attribute <cd> candela : LuminousIntensityUnita;rithmetic expression

                          …                                                of other units.

                          attribute <N> newton : ForceUnit = kg * m / s ^ 2;

168                             Last changed: 2024-07 (import visibility)  Release 2026-04
```

### LAYOUT PDF PAGE 169

```text
              US Customary Units

     standard library package USCustomaryUnits {
        public import ISQ::*;
        private import SI::*;

        attribute <ft> foot : LengthUnit {

           attribute redefines unitConversion : ConversionByConvention {

              attribute redefines referenceUnit = m,

              attribute redefines conversionFactor = 3048/10000;

           }

        }                                              US customary units are defined

        …                                              by conversion from SI units.

        attribute <mi> mile : LengthUnit {

              attribute redefines unitConversion : ConversionByConvention {

              attribute redefines referenceUnit = ft,

              attribute redefines conversionFactor = 5280;

           }

        }

        attribute <'mi/hr'> 'mile per hour' : SpeedUnit = mi / hr;

        alias mph for 'mi/hr’;

        …

     }        An alias for mile per hour.

169                             Last changed: 2024-07 (import visibility)    Release 2026-04
```

### LAYOUT PDF PAGE 170

```text
     Quantity Calculations (1)

standard library package QuantityCalculations {
     private import ScalarValues::*;
     private import Quantities::ScalarQuantityValue;
     private import MeasurementReferences::ScalarMeasurementReference;
     private import MeasurementReferences::DimensionOneValue;

     calc def '[' specializes BaseFunctions::'[' { in num: Number[1]; in mRef: ScalarMeasurementReference[1];
          return quantity : ScalarQuantityValue[1]; }

     …
     calc def abs specializes NumericalFunctions::abs

          { in x: ScalarQuantityValue[1]; return : ScalarQuantityValue[1]; }
     calc def '+' specializes NumericalFunctions::'+'

          { in x: ScalarQuantityValue[1]; in y: ScalarQuantityValue[0..1]; return : ScalarQuantityValue; }
     calc def '-' specializes NumericalFunctions::'-'

          { in x: ScalarQuantityValue; in y: ScalarQuantityValue[0..1]; return : ScalarQuantityValue[1]; }
     calc def '*' specializes NumericalFunctions::'*'

          { in x: ScalarQuantityValue[1]; in y: ScalarQuantityValue[1]; return : ScalarQuantityValue[1]; }
     calc def '/' specializes NumericalFunctions::'/'

          { in x: ScalarQuantityValue[1]; in y: ScalarQuantityValue[1]; return : ScalarQuantityValue[1]; }
     calc def '**' specializes NumericalFunctions::'**'

          { in x: ScalarQuantityValue[1]; in y: Real[1]; return : ScalarQuantityValue[1]; }
     calc def '^' specializes NumericalFunctions::'^'

          { in x: ScalarQuantityValue[1]; in y: Real[1]; return : ScalarQuantityValue[1]; }
     calc def '<' specializes NumericalFunctions::'<'

          { in x: ScalarQuantityValue[1]; in y: ScalarQuantityValue[1]; return : Boolean[1]; }
     calc def '>' specializes NumericalFunctions::'>'

          { in x: ScalarQuantityValue[1]; in y: ScalarQuantityValue[1]; return : Boolean[1]; }
     calc def '<=' specializes NumericalFunctions::'<='

          { in x: ScalarQuantityValue[1]; in y: ScalarQuantityValue[1]; return : Boolean[1]; }
     calc def '>=' specializes NumericalFunctions::'>='

          { in x: ScalarQuantityValue[1]; in y: ScalarQuantityValue[1]; return : Boolean[1]; }
     …
}

170  Last changed: 2023-02 (new)                                        Release 2026-04
```

### LAYOUT PDF PAGE 171

```text
     Quantity Calculations (2)

standard library package QuantityCalculations {
     …
     calc def max specializes NumericalFunctions::max
          { in x: ScalarQuantityValue[1]; in y: ScalarQuantityValue[1]; return : ScalarQuantityValue[1]; }
     calc def min specializes NumericalFunctions::min
          { in x: ScalarQuantityValue[1]; in y: ScalarQuantityValue[1]; return : ScalarQuantityValue[1]; }

     calc def '==' specializes DataFunctions::'=='
          { in x: ScalarQuantityValue[1]; in y: ScalarQuantityValue[1]; return : Boolean[1]; }

     calc def sqrt{ in x: ScalarQuantityValue[1]; return : ScalarQuantityValue[1]; }

     calc def floor { in x: ScalarQuantityValue[1]; return : ScalarQuantityValue[1]; }
     calc def round { in x: ScalarQuantityValue[1]; return : ScalarQuantityValue[1]; }
     calc def ToString specializes BaseFunctions::ToString { in x: ScalarQuantityValue[1]; return : String; }
     calc def ToInteger { in x: ScalarQuantityValue[1]; return : Integer[1]; }
     calc def ToRational { in x: ScalarQuantityValue[1]; return : Rational[1]; }
     calc def ToReal { in x: ScalarQuantityValue[1]; return : Real[1]; }
     calc def ToDimensionOneValue { in x: Real[1]; return : DimensionOneValue[1]; }
     calc def sum specializes NumericalFunctions::sum

          { in collection: ScalarQuantityValue[0..*]; return : ScalarQuantityValue; }
     calc def product specializes NumericalFunctions::product

          { in collection: ScalarQuantityValue[0..*]; return : ScalarQuantityValue; }

     calc def ConvertQuantity { in x: ScalarQuantityValue[1]; in targetMRef: ScalarMeasurementReference[1];
          return : ScalarQuantityValue[1]; }

}

171  Last changed: 2023-02 (new)  Release 2026-04
```

### LAYOUT PDF PAGE 172

```text
     Measurement Reference Calculations

standard library package MeasurementRefCalculations {
    private import ScalarValues::String;
    private import ScalarValues::Real;
    private import MeasurementReferences::MeasurementUnit;
    private import MeasurementReferences::ScalarMeasurementReference;
    private import MeasurementReferences::CoordinateFrame;

    calc def '*' specializes DataFunctions::'*'
        { in x: MeasurementUnit[1]; in y: MeasurementUnit[1]; return : MeasurementUnit[1]; }

    calc def '/' specializes DataFunctions::'/'
        { in x: MeasurementUnit[1]; in y: MeasurementUnit[1]; return : MeasurementUnit[1]; }

    calc def '**' specializes DataFunctions::'**'
        { in x: MeasurementUnit[1]; in y: Real[1]; return : MeasurementUnit[1]; }

    calc def '^' specializes DataFunctions::'^'
        { in x: MeasurementUnit[1]; in y: Real[1]; return : MeasurementUnit[1]; }

    calc def 'CoordinateFrame*' specializes DataFunctions::'*'
        { in x: CoordinateFrame[1]; in y: MeasurementUnit[1]; return : CoordinateFrame[1]; }

    calc def 'CoordinateFrame/' specializes DataFunctions::'/'
        { in x: CoordinateFrame[1]; in y: MeasurementUnit[1]; return : CoordinateFrame[1]; }

    calc def ToString specializes BaseFunctions::ToString
        { in x: ScalarMeasurementReference[1]; return : String[1]; }

}

172  Last changed: 2023-02 (new)         Release 2026-04
```

### LAYOUT PDF PAGE 173

```text
     Vector Calculations

standard library package VectorCalculations {
    private import ScalarValues::Boolean;
    private import ScalarValues::Number;
    private import Quantities::VectorQuantityValue;

calc def '+' specializes VectorFunctions::'+’
    {in : VectorQuantityValue; in : VectorQuantityValue; return : VectorQuantityValue;}

calc def '-' specializes VectorFunctions::'-’
    {in : VectorQuantityValue; in : VectorQuantityValue; return : VectorQuantityValue;}

calc def scalarVectorMult specializes VectorFunctions:: scalarVectorMult
    {in : Number; in : VectorQuantityValue; return : VectorQuantityValue;}

calc def vectorScalarMult specializes VectorFunctions:: vectorScalarMult
    {in : VectorQuantityValue; in : Number; return : VectorQuantityValue;}

calc def vectorScalarDiv specializes RealFunctions::'*’
    {in : VectorQuantityValue; in : Number; return : VectorQuantityValue;}

calc def inner specializes VectorFunctions::inner
    {in : VectorQuantityValue; in : VectorQuantityValue; return : Number;}

alias scalarVectorMult as '*';

    calc def norm specializes VectorFunctions::norm
        {in : VectorQuantityValue; return : Number;}

    calc def angle specializes VectorFunctions::angle
        {in : VectorQuantityValue; in : VectorQuantityValue; return : Number;}

}

173  Last changed: 2022-09 (standard library package)                           Release 2026-04
```

### LAYOUT PDF PAGE 174

```text
     Tensor Calculations

standard library package TensorCalculations {
     private import ScalarValues::Boolean;
     private import ScalarValues::Number;
     private import Quantities::ScalarQuantityValue;
     private import Quantities::VectorQuantityValue;
     private import Quantities::TensorQuantityValue;
     private import MeasurementReferences::TensorMeasurementReference;
     private import MeasurementReferences::CoordinateTransformation;

     calc def '[' specializes BaseFunctions::'[' { in elements: Number[1..n] ordered;
          in mRef: TensorMeasurementReference[1]; return quantity: TensorQuantityValue[1];
          private attribute n = mRef.flattenedSize;

     }
     …
     calc def '+' :> DataFunctions::'+'

          ]{ in : TensorQuantityValue[1]; in : TensorQuantityValue[1]; return : TensorQuantityValue[1]; }
     calc def '-' :> DataFunctions::'-'

          { in : TensorQuantityValue[1]; in : TensorQuantityValue[1]; return : TensorQuantityValue[1]; }
     calc def scalarTensorMult { in : Number[1]; in : TensorQuantityValue[1]; return : TensorQuantityValue[1]; }
     calc def TensorScalarMult { in : TensorQuantityValue[1]; in : Number[1]; return : TensorQuantityValue[1]; }
     calc def scalarQuantityTensorMult

          { in : ScalarQuantityValue[1]; in : TensorQuantityValue[1]; return : TensorQuantityValue[1]; }
     calc def TensorScalarQuantityMult

          { in : TensorQuantityValue[1]; in : ScalarQuantityValue[1]; return : TensorQuantityValue[1]; }
     calc def tensorVectorMult

          { in : TensorQuantityValue[1]; in : VectorQuantityValue[1]; return : VectorQuantityValue[1]; }
     calc def vectorTensorMult

          { in : VectorQuantityValue[1]; in : TensorQuantityValue[1]; return : VectorQuantityValue[1]; }
     calc def tensorTensorMult

          { in : TensorQuantityValue[1]; in : TensorQuantityValue[1]; return : TensorQuantityValue[1]; }
     calc def transform { in transformation : CoordinateTransformation; in sourceTensor : TensorQuantityValue;

          return targetTensor : TensorQuantityValue; }
}

174  Last changed: 2023-02 (new)                                        Release 2026-04
```

### LAYOUT PDF PAGE 175

```text
Clocks is a Kernel Library model       Time (1)
of the semantics of clocks.
                                                                                             A singleton universal time
A clock provides the current                                                                 reference.
time as a quantity that           standard library package Time {
advances monotonically over
the lifetime of the clock.            part universalClock : Clock[1] :>
                                         Clocks::universalClock;
TimeOf returns the time instant
of the start of an occurrence         part def Clock :> Clocks::Clock {
relative to a given clock.               attribute :>> currentTime : TimeInstantValue;

DurationOf returns the                }
duration of a given occurrence
relative to a given clock (the        calc def TimeOf :> Clocks::TimeOf {
time of its end snapshot minus           in o : Occurrence[1];
the time of its start snapshot).         in clock : Clock[1] default localClock;
                                         return timeInstant : TimeInstantValue[1];

                                      }

                                      calc def DurationOf :> Clocks::DurationOf {
                                         in o : Occurrence[1];
                                         in clock : Clock[1] default localClock;
                                         return duration : DurationValue;

                                      }

175                               Last changed: 2025-02 (removed “readonly”)  Release 2026-04
```

### LAYOUT PDF PAGE 176

```text
                                     Time (2)                              Captures the specification
                                                                           of the time instant with
                                     Generic time scale to                 value zero, also known as
                                     express a time instant.

     attribute def TimeScale :> IntervalScale {                            the (reference) epoch.

        attribute :>> unit: DurationUnit[1];

        attribute definitionalEpoch: DefinitionalQuantityValue[1];

        attribute :>> definitionalQuantityValues = definitionalEpoch;

     }

                                                                                                         Representation of a

     attribute def TimeInstantValue :> ScalarQuantityValue {               time instant quantity.

        attribute :>> num: Real[1];

        attribute :>> mRef: TimeScale[1];

     }                                                                     Generic representation of a

     attribute timeInstant: TimeInstantValue :> scalarQuantities; time instant as a calendar

     abstract attribute def DateTime :> TimeInstantValue;                  date and time of day.

     abstract attribute def Date :> TimeInstantValue;

     abstract attribute def TimeOfDay :> TimeInstantValue;

                                                                           Representation of the

     attribute UTC: TimeScale {                                            Coordinated Universal Time
         attribute :>> longName = "Coordinated Universal Time";            (UTC) time scale.
         attribute :>> unit = SI::s;

        attribute :>> definitionalEpoch: DefinitionalQuantityValue {

           :>> num = 0;

           :>> definition = "UTC epoch at 1 January 1958 at 0 hour 0 minute 0 second";

        }

     }

     attribute def UtcTimeInstantValue :> DateTime { :>> mRef = UTC; }

     attribute utcTimeInstant: UtcTimeInstantValue;

176                      Last changed: 2022-09 (standard library package)  Release 2026-04
```

### LAYOUT PDF PAGE 177

```text
                                            Time (3)

        attribute def Iso8601DateTimeEncoding :> String;        Representation of an ISO 8601-1
                                                                date and time in extended
                                                                string format.

        attribute def Iso8601DateTime :> UtcTimeInstantValue {

           attribute :>> num = getElapsedUtcTime(val);          Representation of an ISO 8601
           attribute val: Iso8601DateTimeEncoding;
                                                                date and time with explicit date
           private calc getElapsedUtcTime
           {in iso8601DateTime: Iso8601DateTimeEncoding; return : Reaanld;t}ime component attributes.

        }

        attribute def Iso8601DateTimeStructure :> UtcTimeInstantValue {

           attribute :>> num = getElapsedUtcTime(year, month, day, hour, minute, second,

           microsecond, hourOffset, minuteOffest);

           attribute :>> mRef = UTC;

           attribute year: Integer;

           attribute month: Natural;

           attribute day: Natural;

           attribute hour: Natural;

           attribute minute: Natural;

           attribute second: Natural;

           attribute microsecond: Natural;

           attribute hourOffset: Integer;

           attribute minuteOffest: Integer;

           private calc getElapsedUtcTime(year: Integer, month: Natural, day: Natural,

           hour: Natural, minute: Natural, second: Natural, microsecond: Natural,

           hourOffset: Integer, minuteOffest: Integer) : Real;

        }

        …

     }

177        Last changed: 2022-09 (standard library package)                        Release 2026-04
```

### LAYOUT PDF PAGE 178

```text
     Geometry Library

178                    Release 2026-04
```

### LAYOUT PDF PAGE 179

```text
                                    Spatial Items (1)

standard library package SpatialItems {           A spatial item is an Item with a three-
    …                                             dimensional spatial extent that also
    item def SpatialItem :> SpatialFrame {        acts as a spatial frame of reference.

      item :>> self : SpatialItem;

      item :>> localClock : Clock[1] default Time::universalClock;

      attribute coordinateFrame : ThreeDCoordinateFrame[1]

         default universalCartesianSpatial3dCoordinateFrame;          A spatial item has local

      item originPoint : Point[1] :> spaceShots;                      time and space references
                                                                      used within it.

      item subSpatialItems : SpatialItem[1..*] :> subitems {

         ref item :>> SpatialItem::localClock, subitems::localClock;

      }

      item componentItems : SpatialItem[0..*] ordered :> subSpatialItems {

         ref item :>> SpatialItem::localClock, subSpatialItems::localClock;

         attribute :>> coordinateFrame {

            attribute :>> transformation[1] default nullTransformation { … }

         }

      }

      private attribute cunionNum: Natural [1] = if isEmpty(componentItems) ? 0 else 1;

      private attribute componentUnion[cunionNum] :> unionsOf {

         item :>> elements : SpatialItem[1..*] = componentItems;

      }

      …

   }                                                          A compound spatial item is a spatial
   …
                                                              item that is a (spatial) union of a
}
                                                              collection of component spatial items.

179         Last changed: 2025-07 (added subSpatialItem)                                   Release 2026-04
```

### LAYOUT PDF PAGE 180

```text
                             Spatial Items (2)

standard library package SpatialItems {

   …                                                                 The position of points in space can be
   calc def PositionOf :> SpatialFrames::PositionOf {

      in point : Point[1];                                           determined relative to the space and

      in timeInstant : TimeInstantValue[1];                          time references of a spatial item.
      in enclosingItem :>> 'frame' : SpatialItem[1];

      in clock : Clock[1] default enclosingItem.localClock;

      return positionVector : VectorQuantityValue[1];

   }

   calc def CurrentPositionOf :> SpatialFrames::CurrentPositionOf {

      in point : Point[1];

        in enclosingItem :>> 'frame' : SpatialItem[1];               The position of a point can move
        in clock : Clock[1] default enclosingItem.localClock;        over time, with its "current"
        return positionVector : VectorQuantityValue[1];              position being relative to the clock
   }

   calc def DisplacementOf :> SpatialFrames::DisplacementOf {        reference of the spatial item.
        in point1 : Point[1];

      in point2 : Point[1];

      in timeInstant : TimeInstantValue[1];

      in spacialItem :>> 'frame' : SpatialItem[1];

      in clock : Clock[1] default spacialItem.localClock;

      return displacementVector : VectorQuantityValue[1];

   }

   calc def CurrentDisplacementOf :> SpatialFrames::CurrentDisplacementOf {

      in point1 : Point[1];

      in point2 : Point[1];

      in spacialItem :>> 'frame' : SpatialItem[1];

      in clock : Clock[1] default spacialItem.localClock;

      return displacementVector : VectorQuantityValue[1];

   }

}

180                          Last changed: 2022-09 (standard library package)  Release 2026-04
```

### LAYOUT PDF PAGE 181

```text
            Shape Items (1)

     standard library package ShapeItems {          The ShapeItems package provides
         …                                          a model of items that represent
         item def PlanarCurve :> Curve {            basic geometric shapes.
             attribute :>> length [1];
             …
         }

     item def Line :> PlanarCurve {
         attribute :>> length;
         attribute :>> outerSpaceDimension = 1;

     }

     item def PlanarSurface :> Surface {
         attribute :>> area;
         attribute :>> outerSpaceDimension = 2;
         item :>> shape : PlanarCurve;

     }

     abstract item def Path :> StructuredCurve;
     abstract item def Shell :> StructuredSurface;

         …
     }

181         Last changed: 2025-07 (StructuredCurve and StructuredSurface)  Release 2026-04
```

### LAYOUT PDF PAGE 182

```text
     Shape Items (2)

     standard library package ShapeItems {
         …
         item def ConicSection :> Path, PlanarCurve {
             …
         }

     item def Ellipse :> ConicSection {
         attribute :>> semiMajorAxis;
         attribute :>> semiMinorAxis;
         …

     }

     item def Circle :> Ellipse {
         attribute :>> radius;
         attribute :>> semiMajorAxis = radius;
         attribute :>> semiMinorAxis = radius;
         …

     }
     …

         item def Polygon :> Path, PlanarCurve {
             item :>> edges : Line { item :>> vertices [2]; }
             attribute :>> isClosed = true;
             …

         }
     …
     }

182  Last changed: 2023-11 (Updated Circle)                    Release 2026-04
```

### LAYOUT PDF PAGE 183

```text
     Shape Items (3)

     standard library package ShapeItems {
         …

         item def Disc :> Shell, PlanarSurface {
             attribute :>> semiMajorAxis;
             attribute :>> semiMinorAxis;
             item :>> shape : Ellipse [1] {
                  attribute :>> semiMajorAxis = Disc::semiMajorAxis;
                  attribute :>> semiMinorAxis = Disc::semiMinorAxis;
             }
             …

         }

         item def CircularDisc :> Disc {
             attribute :>> radius [1];
             attribute :>> semiMajorAxis [1] = radius;
             attribute :>> semiMinorAxis [1] = radius;
             item :>> shape : Circle { … }
             …

         }

         item def ConicSurface :> Shell {
             …

         }
         …
     }

183  Last changed: 2025-07 (CircularDisc attributes)                  Release 2026-04
```

### LAYOUT PDF PAGE 184

```text
     Shape Items (4)

     standard library package ShapeItems {
         …

         item def Ellipsoid :> ConicSurface {
             attribute semiAxis1 : LengthValue [1] :> scalarQuantities;
             attribute semiAxis2 : LengthValue [1] :> scalarQuantities;
             attribute semiAxis3 : LengthValue [1] :> scalarQuantities;
             …

         }

         item def Sphere :> Ellipsoid {
             attribute :>> radius [1];
             attribute :>> semiAxis1 [1] = radius;
             attribute :>> semiAxis2 [1] = radius;
             attribute :>> semiAxis3 [1] = radius;

         }

         item def Paraboloid :> ConicSurface {
             attribute focalDistance : LengthValue [1] :> scalarQuantities;
             …

         }

         …
     }

184  Last changed: 2025-07 (Sphere attributes)                               Release 2026-04
```

### LAYOUT PDF PAGE 185

```text
            Shape Items (5)

     standard library package ShapeItems {
         …
         item def ConeOrCylinder :> Shell {
             attribute :>> semiMajorAxis [1];
             attribute :>> semiMinorAxis [1];
             attribute :>> height [1];
             …
         }

     item def Cone :> ConeOrCylinder { … }
     item def Cylinder :> ConeOrCylinder { … }

     …

     item def Polyhedron :>> Shell { … }
     item def CuboidOrTriangularPrism :> Polyhedron { … }
     item def Cuboid :> CuboidOrTriangularPrism { … }
     item def RectangularCuboid :> Cuboid {

         attribute :>> length [1];
         attribute :>> width [1];
         attribute :>> height [1];
         …
     }
     alias Box for RectangularCuboid;

         …
     }

185         Last changed: 2022-09 (standard library package)  Release 2026-04
```
